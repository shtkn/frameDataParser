@Subroutine
def PreInit():
    Unknown12019('70796f00000000000000000000000000')

@Subroutine
def MatchInit():
    Health(14000)
    WalkFSpeed(9000)
    WalkBSpeed(8500)
    DashFInitialVelocity(23000)
    DashFMaxVelocity(41000)
    JumpYVelocity(41000)
    SuperJumpYVelocity(48000)
    Unknown12007(10000)
    Unknown12011(2000)
    AirBDashDuration(13)
    Unknown12037(-2000)
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
    Unknown14015(0, 300000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 350000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 350000, -150000, 300000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 220000, -100000, 180000, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 350000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 500000, -100000, 400000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkA4th', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 500000, -300000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    Unknown15009()
    Unknown14015(0, 300000, -250000, 50000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Move_AirGround_(0x300e)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 500000, -300000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(100000, 650000, -300000, 250000, 1500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(200000, 800000, -300000, 100000, 1500, 0)
    Unknown15015(32, 36)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(3000)
    Unknown14015(-50000, 350000, 100000, 450000, 500, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15021(1)
    Unknown15014(1)
    Unknown14015(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 450000, -200000, 0, 1500, 50)
    Move_EndRegister()
    Move_Register('CmnActBDash', 0x1)
    Move_Input_(0xdb)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('CmnActAirFDash', 0x1)
    Move_Input_(0xda)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('CmnActAirBDash', 0x1)
    Move_Input_(0xdb)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(4)
    Unknown15021(2000)
    Unknown14015(0, 300000, -250000, 300000, 1000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15021(500)
    Unknown14015(0, 300000, -250000, 300000, 1000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15009()
    Unknown15021(100)
    Unknown14015(-300000, 300000, -650000, -150000, 1000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAir5A2nd', 0x10)
    Unknown14027('NmlAtkAIR5A')
    Unknown14005(1)
    Unknown14015(0, 250000, -150000, 250000, 1000, 20)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('KakeagariA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(1)
    Unknown14015(0, 650000, -200000, 100000, 400, 0)
    Move_EndRegister()
    Move_Register('KakeagariB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown14015(0, 800000, -200000, 100000, 400, 0)
    Move_EndRegister()
    Move_Register('KakeagariEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(1)
    Unknown14015(0, 800000, -200000, 100000, 200, 0)
    Move_EndRegister()
    Move_Register('MoonsaltSlash', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('MoonsaltMoveR', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_AirGround_(0x300a)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown14015(300000, 500000, -650000, 100000, 700, 0)
    Unknown15015(20, 23)
    Move_EndRegister()
    Move_Register('MoonsaltMoveL', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown14015(300000, 500000, -650000, 100000, 700, 0)
    Unknown15015(20, 23)
    Move_EndRegister()
    Move_Register('MoonsaltMove_Hasei', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15021(1)
    Unknown14015(300000, 500000, -650000, 100000, 700, 0)
    Unknown15015(20, 23)
    Move_EndRegister()
    Move_Register('MoonsaltMoveR_Hasei', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Unknown14013('MoonsaltMoveR')
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_AirGround_(0x300a)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15021(1)
    Unknown14015(300000, 500000, -650000, 100000, 700, 0)
    Unknown15015(20, 23)
    Move_EndRegister()
    Move_Register('MoonsaltMoveL_Hasei', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Unknown14013('MoonsaltMoveL')
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_AirGround_(0x3009)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15021(1)
    Unknown14015(300000, 500000, -650000, 100000, 700, 0)
    Unknown15015(20, 23)
    Move_EndRegister()
    Move_Register('MoonsaltMove_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(1)
    Unknown14015(0, 400000, -650000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('MoonsaltMove_Ex_Back', INPUT_SPECIALMOVE)
    Unknown14013('MoonsaltMove_Ex')
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('MoonsaltMove_Ex_Hasei', INPUT_SPECIALMOVE)
    Unknown14013('MoonsaltMove_Ex')
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3003)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('VSlash_R', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300c)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 400000, -650000, 100000, 500, 20)
    Move_EndRegister()
    Move_Register('VSlash_L', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300c)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 400000, -650000, 100000, 500, 20)
    Move_EndRegister()
    Move_Register('VSlash_Hasei', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300c)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('VSlash_R_Hasei', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Unknown14013('VSlash_R')
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300c)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('VSlash_L_Hasei', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Unknown14013('VSlash_L')
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300c)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(3000)
    Unknown14015(-50000, 300000, -100000, 350000, 400, 0)
    Move_EndRegister()
    Move_Register('UltimateTatsumaki', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(2000)
    Unknown14015(0, 300000, -100000, 300000, 500, 5)
    Move_EndRegister()
    Move_Register('UltimateTatsumakiOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(2000)
    Unknown14015(0, 300000, -100000, 300000, 500, 5)
    Move_EndRegister()
    Move_Register('UltimateKunai', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(5000)
    Unknown14015(0, 450000, -100000, 300000, 500, 5)
    Move_EndRegister()
    Move_Register('UltimateKunaiOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(5000)
    Unknown14015(0, 450000, -100000, 300000, 500, 5)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtkA4th', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtkA4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'NmlAtk5B3rd', 10000000)
    Unknown15024('NmlAtk5B3rd', 'KakeagariA', 10000000)
    Unknown15024('NmlAtk5B2nd', 'KakeagariA', 10000000)
    Unknown15024('NmlAtk2C', 'KakeagariA', 10000000)
    Unknown15024('NmlAtkAIR5C', 'KakeagariB', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAir5A2nd', 10000000)
    Unknown15024('NmlAtkAir5A2nd', 'NmlAtkAIR5A', 10000000)
    Unknown15024('KakeagariA', 'VSlash_R', 10000000)
    Unknown15024('KakeagariA', 'VSlash_L', 10000000)
    Unknown15024('KakeagariB', 'MoonsaltMoveR', 10000000)
    Unknown15024('KakeagariB', 'MoonsaltMoveL', 10000000)
    Unknown15024('KakeagariB', 'MoonsaltMove_Ex', 10000000)
    Unknown15024('KakeagariEX', 'MoonsaltMoveR', 10000000)
    Unknown15024('KakeagariEX', 'MoonsaltMoveL', 10000000)
    Unknown15024('MoonsaltMoveR', 'MoonsaltSlash', 10000000)
    Unknown15024('MoonsaltMoveL', 'MoonsaltSlash', 10000000)
    Unknown15024('MoonsaltMoveR_Hasei', 'MoonsaltSlash', 10000000)
    Unknown15024('MoonsaltMoveL_Hasei', 'MoonsaltSlash', 10000000)
    Unknown15024('MoonsaltMove_Hasei', 'MoonsaltSlash', 10000000)
    Unknown15024('MoonsaltSlash', 'MoonsaltMoveR_Hasei', 10000000)
    Unknown15024('MoonsaltSlash', 'MoonsaltMoveL_Hasei', 10000000)
    Unknown15024('MoonsaltMove_Ex', 'MoonsaltMoveR_Hasei', 10000000)
    Unknown15024('MoonsaltMove_Ex', 'MoonsaltMoveL_Hasei', 10000000)
    Unknown15024('MoonsaltMove_Ex', 'MoonsaltMove_Hasei', 10000000)
    Unknown15024('NmlAtkThrowExe', 'KakeagariB', 10000000)
    Unknown15024('NmlAtkThrowExe', 'KakeagariEX', 10000000)
    Unknown15024('NmlAtkBackThrowExe', 'KakeagariB', 10000000)
    Unknown15024('NmlAtkBackThrowExe', 'KakeagariEX', 10000000)
    Unknown7010(0, 'pyo000')
    Unknown7010(1, 'pyo001')
    Unknown7010(2, 'pyo002')
    Unknown7010(3, 'pyo003')
    Unknown7010(4, 'pyo004')
    Unknown7010(5, 'pyo005')
    Unknown7010(6, 'pyo006')
    Unknown7010(7, 'pyo007')
    Unknown7010(8, 'pyo008')
    Unknown7010(9, 'pyo009')
    Unknown7010(10, 'pyo010')
    Unknown7010(15, 'pyo015')
    Unknown7010(16, 'pyo016')
    Unknown7010(17, 'pyo017')
    Unknown7010(18, 'pyo018')
    Unknown7010(19, 'pyo019')
    Unknown7010(20, 'pyo020')
    Unknown7010(21, 'pyo021')
    Unknown7010(22, 'pyo022')
    Unknown7010(23, 'pyo023')
    Unknown7010(24, 'pyo024')
    Unknown7010(25, 'pyo025')
    Unknown7010(28, 'pyo028')
    Unknown7010(29, 'pyo029')
    Unknown7010(30, 'pyo030')
    Unknown7010(31, 'pyo031')
    Unknown7010(32, 'pyo032')
    Unknown7010(33, 'pyo033')
    Unknown7010(34, 'pyo034')
    Unknown7010(35, 'pyo035')
    Unknown7010(36, 'pyo036')
    Unknown7010(37, 'pyo037')
    Unknown7010(39, 'pyo039')
    Unknown7010(42, 'pyo042')
    Unknown7010(43, 'pyo043')
    Unknown7010(44, 'pyo044')
    Unknown7010(45, 'pyo045')
    Unknown7010(46, 'pyo046')
    Unknown7010(47, 'pyo047')
    Unknown7010(48, 'pyo048')
    Unknown7010(49, 'pyo049')
    Unknown7010(50, 'pyo050')
    Unknown7010(52, 'pyo052')
    Unknown7010(53, 'pyo053')
    Unknown7010(54, 'pyo100_0')
    Unknown7010(55, 'pyo100_1')
    Unknown7010(56, 'pyo100_2')
    Unknown7010(63, 'pyo101_0')
    Unknown7010(64, 'pyo101_1')
    Unknown7010(65, 'pyo101_2')
    Unknown7010(57, 'pyo102_0')
    Unknown7010(58, 'pyo102_1')
    Unknown7010(59, 'pyo102_2')
    Unknown7010(66, 'pyo103_0')
    Unknown7010(67, 'pyo103_1')
    Unknown7010(68, 'pyo103_2')
    Unknown7010(60, 'pyo104_0')
    Unknown7010(61, 'pyo104_1')
    Unknown7010(62, 'pyo104_2')
    Unknown7010(69, 'pyo105_0')
    Unknown7010(70, 'pyo105_1')
    Unknown7010(71, 'pyo105_2')
    Unknown7010(72, 'pyo150')
    Unknown7010(73, 'pyo151')
    Unknown7010(74, 'pyo152')
    Unknown7010(85, 'pyo153')
    Unknown7010(87, 'pyo154')
    Unknown7010(88, 'pyo155')
    Unknown7010(96, 'pyo161_0')
    Unknown7010(97, 'pyo161_1')
    Unknown7010(92, 'pyo162_0')
    Unknown7010(93, 'pyo162_1')
    Unknown7010(98, 'pyo163_0')
    Unknown7010(99, 'pyo163_1')
    Unknown7010(100, 'pyo164_0')
    Unknown7010(101, 'pyo164_1')
    Unknown7010(105, 'pyo165_0')
    Unknown7010(106, 'pyo165_1')
    Unknown7010(102, 'pyo166_0')
    Unknown7010(103, 'pyo166_1')
    Unknown7010(90, 'pyo167_0')
    Unknown7010(91, 'pyo167_1')
    Unknown7010(107, 'pyo168_0')
    Unknown7010(108, 'pyo168_1')
    Unknown7010(110, 'pyo169_0')
    Unknown7010(111, 'pyo169_1')
    Unknown7010(94, 'pyo400_0')
    Unknown7010(95, 'pyo400_1')
    Unknown12018(0, 'yo060_00')
    Unknown12018(1, 'yo060_01')
    Unknown12018(2, 'yo060_02')
    Unknown12018(3, 'yo060_03')
    Unknown12018(4, 'yo060_04')
    Unknown12018(5, 'yo060_05')
    Unknown12018(6, 'yo060_06')
    Unknown12018(7, 'yo041_02')
    Unknown12018(8, 'yo040_02')
    Unknown12018(9, 'yo045_02')
    Unknown12018(10, 'yo060_00')
    Unknown12018(11, 'yo060_01')
    Unknown12018(12, 'yo060_03')
    Unknown12018(13, 'yo060_05')
    Unknown12018(14, 'yo060_07')
    Unknown12018(15, 'yo125_00')
    Unknown12018(16, 'yo050_00')
    Unknown12018(17, 'yo052_00')
    Unknown12018(18, 'yo054_00')
    Unknown12018(19, 'yo000_00')
    Unknown12018(20, 'yo000_00')
    Unknown12018(25, 'yo063_00')
    Unknown12018(26, 'yo063_01')
    Unknown12018(27, 'yo063_02')
    Unknown12018(28, 'yo063_05')
    Unknown12018(29, 'yo060_12')
    Unknown12018(24, 'yo072_03')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746554617473756d616b69000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746554617473756d616b694f4400000000000000000000000000')
    Unknown12059('04000000556c74696d6174654b756e616900000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174654b756e61694f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    GFX_0('PYO_PersonaCreate', -1)
    Unknown38(11, 1)

@Subroutine
def OnFrameStep():
    if SLOT_158:
        SLOT_64 = 0
    SLOT_7 = 0
    if SLOT_62:
        if (SLOT_60 < 4):
            SLOT_7 = 1
    elif (SLOT_60 < 3):
        SLOT_7 = 1

@Subroutine
def OnLanding():
    callSubroutine('LandingRegReset')

@Subroutine
def LandingRegReset():
    SLOT_60 = 0
    SLOT_5 = 0
    SLOT_6 = 0
    SLOT_8 = 0
    SLOT_63 = 0
    SLOT_65 = 0
    SLOT_66 = 0

@Subroutine
def Kakeagari_DeriveInput():
    Unknown14070('VSlash_R')
    Unknown14070('VSlash_L')
    Unknown14070('VSlash_Hasei')
    Unknown14070('VSlash_R_Hasei')
    Unknown14070('VSlash_L_Hasei')
    Unknown14070('MoonsaltMoveR')
    Unknown14070('MoonsaltMoveL')
    Unknown14070('MoonsaltMove_Hasei')
    Unknown14070('MoonsaltMoveR_Hasei')
    Unknown14070('MoonsaltMoveL_Hasei')
    Unknown14070('MoonsaltMove_Ex')
    Unknown14070('MoonsaltMove_Ex_Back')
    Unknown14070('MoonsaltMove_Ex_Hasei')

@Subroutine
def Kakeagari_DeriveTiming():
    Unknown14072('VSlash_R')
    Unknown14072('VSlash_L')
    Unknown14072('VSlash_Hasei')
    Unknown14072('VSlash_R_Hasei')
    Unknown14072('VSlash_L_Hasei')
    Unknown14072('MoonsaltMoveR')
    Unknown14072('MoonsaltMoveL')
    Unknown14072('MoonsaltMove_Hasei')
    Unknown14072('MoonsaltMoveR_Hasei')
    Unknown14072('MoonsaltMoveL_Hasei')
    Unknown14072('MoonsaltMove_Ex')
    Unknown14072('MoonsaltMove_Ex_Back')
    Unknown14072('MoonsaltMove_Ex_Hasei')

@Subroutine
def Kakeagari_DeriveClear():
    Unknown14074('VSlash_R')
    Unknown14074('VSlash_L')
    Unknown14074('VSlash_Hasei')
    Unknown14074('VSlash_R_Hasei')
    Unknown14074('VSlash_L_Hasei')
    Unknown14074('MoonsaltMoveR')
    Unknown14074('MoonsaltMoveL')
    Unknown14074('MoonsaltMove_Hasei')
    Unknown14074('MoonsaltMoveR_Hasei')
    Unknown14074('MoonsaltMoveL_Hasei')
    Unknown14074('MoonsaltMove_Ex')
    Unknown14074('MoonsaltMove_Ex_Back')
    Unknown14074('MoonsaltMove_Ex_Hasei')

@Subroutine
def Moonsalt_DeriveInput():
    Unknown14070('VSlash_R')
    Unknown14070('VSlash_L')
    Unknown14070('VSlash_Hasei')
    Unknown14070('VSlash_R_Hasei')
    Unknown14070('VSlash_L_Hasei')
    Unknown14070('MoonsaltMoveR')
    Unknown14070('MoonsaltMoveL')
    Unknown14070('MoonsaltMoveR_Hasei')
    Unknown14070('MoonsaltMoveL_Hasei')
    Unknown14070('MoonsaltMove_Ex')
    Unknown14070('MoonsaltMove_Ex_Back')
    Unknown14070('MoonsaltMove_Ex_Hasei')
    Unknown14070('MoonsaltSlash')

@Subroutine
def Moonsalt_DeriveTiming():
    Unknown14072('VSlash_R')
    Unknown14072('VSlash_L')
    Unknown14072('VSlash_Hasei')
    Unknown14072('VSlash_R_Hasei')
    Unknown14072('VSlash_L_Hasei')
    Unknown14072('MoonsaltMoveR')
    Unknown14072('MoonsaltMoveL')
    Unknown14072('MoonsaltMoveR_Hasei')
    Unknown14072('MoonsaltMoveL_Hasei')
    Unknown14072('MoonsaltMove_Ex')
    Unknown14072('MoonsaltMove_Ex_Back')
    Unknown14072('MoonsaltMove_Ex_Hasei')
    Unknown14072('MoonsaltSlash')

@Subroutine
def Moonsalt_DeriveClear():
    Unknown14074('VSlash_R')
    Unknown14074('VSlash_L')
    Unknown14074('VSlash_Hasei')
    Unknown14074('VSlash_R_Hasei')
    Unknown14074('VSlash_L_Hasei')
    Unknown14074('MoonsaltMoveR')
    Unknown14074('MoonsaltMoveL')
    Unknown14074('MoonsaltMoveR_Hasei')
    Unknown14074('MoonsaltMoveL_Hasei')
    Unknown14074('MoonsaltMove_Ex')
    Unknown14074('MoonsaltMove_Ex_Back')
    Unknown14074('MoonsaltMove_Ex_Hasei')

@Subroutine
def AirSpecialAttack_DeriveInput():
    Unknown14070('MoonsaltMoveR')
    Unknown14070('MoonsaltMoveL')
    Unknown14070('MoonsaltMoveR_Hasei')
    Unknown14070('MoonsaltMoveL_Hasei')
    Unknown14070('MoonsaltMove_Ex')
    Unknown14070('MoonsaltMove_Ex_Back')
    Unknown14070('MoonsaltMove_Ex_Hasei')

@Subroutine
def AirSpecialAttack_DeriveTiming():
    Unknown14072('MoonsaltMoveR')
    Unknown14072('MoonsaltMoveL')
    Unknown14072('MoonsaltMoveR_Hasei')
    Unknown14072('MoonsaltMoveL_Hasei')
    Unknown14072('MoonsaltMove_Ex')
    Unknown14072('MoonsaltMove_Ex_Back')
    Unknown14072('MoonsaltMove_Ex_Hasei')

@Subroutine
def AirSpecialAttack_DeriveClear():
    Unknown14074('MoonsaltMoveR')
    Unknown14074('MoonsaltMoveL')
    Unknown14074('MoonsaltMoveR_Hasei')
    Unknown14074('MoonsaltMoveL_Hasei')
    Unknown14074('MoonsaltMove_Ex')
    Unknown14074('MoonsaltMove_Ex_Back')
    Unknown14074('MoonsaltMove_Ex_Hasei')

@Subroutine
def LandSpecialAttack_DeriveInput():
    Unknown14070('KakeagariA')
    Unknown14070('KakeagariB')
    Unknown14070('KakeagariEX')
    Unknown14070('UltimateTatsumaki')
    Unknown14070('UltimateTatsumakiOD')
    Unknown14070('UltimateKunai')
    Unknown14070('UltimateKunaiOD')
    Unknown14070('AstralHeat')

@Subroutine
def LandSpecialAttack_DeriveTiming():
    Unknown14072('KakeagariA')
    Unknown14072('KakeagariB')
    Unknown14072('KakeagariEX')
    Unknown14072('UltimateTatsumaki')
    Unknown14072('UltimateTatsumakiOD')
    Unknown14072('UltimateKunai')
    Unknown14072('UltimateKunaiOD')
    Unknown14072('AstralHeat')

@Subroutine
def LandSpecialAttack_DeriveClear():
    Unknown14074('KakeagariA')
    Unknown14074('KakeagariB')
    Unknown14074('KakeagariEX')
    Unknown14074('UltimateTatsumaki')
    Unknown14074('UltimateTatsumakiOD')
    Unknown14074('UltimateKunai')
    Unknown14074('UltimateKunaiOD')
    Unknown14074('AstralHeat')

@Subroutine
def DoNotBeginCancel():
    if Unknown23145('KakeagariA'):
        Unknown30068(1)
    if Unknown23145('KakeagariB'):
        Unknown30068(1)
    if Unknown23145('KakeagariEX'):
        Unknown30068(1)
    if Unknown23145('MoonsaltSlash'):
        Unknown30068(1)
    if Unknown23145('MoonsaltMoveR'):
        Unknown30068(1)
    if Unknown23145('MoonsaltMoveL'):
        Unknown30068(1)
    if Unknown23145('MoonsaltMove_Hasei'):
        Unknown30068(1)
    if Unknown23145('MoonsaltMove_Ex'):
        Unknown30068(1)
    if Unknown23145('MoonsaltSlash'):
        Unknown30068(1)
    if Unknown23145('VSlash_R'):
        Unknown30068(1)
    if Unknown23145('VSlash_L'):
        Unknown30068(1)
    if Unknown23145('VSlash_Hasei'):
        Unknown30068(1)

@State
def CmnActStand():
    label(0)
    sprite('yo000_00', 6)	# 1-6
    sprite('yo000_01', 6)	# 7-12
    sprite('yo000_02', 6)	# 13-18
    sprite('yo000_03', 6)	# 19-24
    sprite('yo000_04', 6)	# 25-30
    sprite('yo000_05', 6)	# 31-36
    sprite('yo000_06', 6)	# 37-42
    sprite('yo000_07', 6)	# 43-48
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('yo001_00', 5)	# 49-53
    SLOT_88 = 960
    SFX_4('pyo000')
    sprite('yo001_01', 5)	# 54-58
    sprite('yo001_02', 5)	# 59-63
    sprite('yo001_03', 10)	# 64-73
    GFX_0('yoef_reaction', 0)
    SFX_3('slash_knife_slow')
    sprite('yo001_04', 5)	# 74-78
    SFX_3('slash_knife_slow')
    sprite('yo001_01', 10)	# 79-88
    sprite('yo001_02', 5)	# 89-93
    sprite('yo001_03', 10)	# 94-103
    GFX_0('yoef_reaction', 0)
    SFX_3('slash_knife_slow')
    sprite('yo001_04', 5)	# 104-108
    SFX_3('slash_knife_slow')
    sprite('yo001_02', 5)	# 109-113
    sprite('yo001_01', 5)	# 114-118
    sprite('yo001_00', 5)	# 119-123
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('yo003_00', 4)	# 1-4
    sprite('yo003_01', 4)	# 5-8
    sprite('yo003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('yo010_00', 4)	# 1-4
    sprite('yo010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('yo010_02', 6)	# 1-6
    sprite('yo010_03', 6)	# 7-12
    sprite('yo010_04', 6)	# 13-18
    sprite('yo010_05', 6)	# 19-24
    sprite('yo010_06', 6)	# 25-30
    sprite('yo010_07', 6)	# 31-36
    sprite('yo010_08', 6)	# 37-42
    sprite('yo010_09', 6)	# 43-48
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('yo013_02', 4)	# 1-4
    sprite('yo013_01', 4)	# 5-8
    sprite('yo013_00', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('yo010_01', 4)	# 1-4
    sprite('yo010_00', 4)	# 5-8

@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        SLOT_4 = 0
    sprite('yo010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('yo020_00', 4)	# 1-4
    sprite('yo020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('yo020_02', 3)	# 1-3
    sprite('yo020_03', 3)	# 4-6
    sprite('yo020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('yo020_05', 3)	# 1-3
    sprite('yo020_06', 3)	# 4-6
    label(0)
    sprite('yo020_07', 4)	# 7-10
    sprite('yo020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('yo010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('yo231_00', 2)	# 1-2
    sprite('yo231_01', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('yo231_01', 3)	# 1-3
    sprite('yo231_00', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('yo030_00', 5)	# 1-5
    sprite('yo030_01', 5)	# 6-10
    label(0)
    sprite('yo030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yo030_03', 5)	# 16-20
    sprite('yo030_04', 5)	# 21-25
    sprite('yo030_05', 5)	# 26-30
    sprite('yo030_06', 5)	# 31-35
    sprite('yo030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yo030_08', 5)	# 41-45
    sprite('yo030_09', 5)	# 46-50
    sprite('yo030_10', 5)	# 51-55
    sprite('yo030_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('yo031_00', 6)	# 1-6
    sprite('yo031_01', 6)	# 7-12
    label(0)
    sprite('yo031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yo031_03', 6)	# 19-24
    sprite('yo031_04', 6)	# 25-30
    sprite('yo031_05', 6)	# 31-36
    sprite('yo031_06', 6)	# 37-42
    sprite('yo031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yo031_08', 6)	# 49-54
    sprite('yo031_09', 6)	# 55-60
    sprite('yo031_10', 6)	# 61-66
    sprite('yo031_11', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('yo032_10', 4)	# 1-4
    sprite('yo032_00', 3)	# 5-7
    label(3)
    sprite('yo032_01', 3)	# 8-10
    sprite('yo032_02', 3)	# 11-13
    sprite('yo032_03', 3)	# 14-16
    Unknown8006(100, 1, 1)
    sprite('yo032_04', 3)	# 17-19
    sprite('yo032_05', 3)	# 20-22
    sprite('yo032_06', 3)	# 23-25
    sprite('yo032_07', 3)	# 26-28
    Unknown8006(100, 1, 1)
    sprite('yo032_08', 3)	# 29-31
    loopRest()
    gotoLabel(3)

@State
def CmnActFDashStop():
    sprite('yo032_09', 4)	# 1-4
    sprite('yo032_10', 4)	# 5-8

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
        Unknown1084(1)
    sprite('yo033_00', 2)	# 1-2
    sprite('yo033_01', 3)	# 3-5
    physicsXImpulse(-23000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('yo033_02', 3)	# 6-8
    sprite('yo033_01', 3)	# 9-11
    sprite('yo033_02', 3)	# 12-14
    label(0)
    sprite('yo033_01', 3)	# 15-17
    sprite('yo033_02', 3)	# 18-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yo033_03', 3)	# 21-23
    setInvincible(0)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('yo033_04', 3)	# 24-26

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirTurn():
    sprite('yo025_00', 1)	# 1-1
    sprite('yo025_01', 2)	# 2-3
    sprite('yo025_02', 1)	# 4-4

@State
def CmnActAirFDash():
    sprite('yo035_00', 3)	# 1-3
    label(0)
    sprite('yo035_01', 3)	# 4-6
    sprite('yo035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('yo033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('yo033_02', 2)	# 4-5
    sprite('yo033_01', 2)	# 6-7
    sprite('yo033_02', 2)	# 8-9
    sprite('yo033_01', 2)	# 10-11
    sprite('yo033_02', 2)	# 12-13
    sprite('yo033_00', 4)	# 14-17
    sprite('yo020_05', 2)	# 18-19
    sprite('yo020_06', 3)	# 20-22
    label(0)
    sprite('yo020_07', 8)	# 23-30
    sprite('yo020_08', 8)	# 31-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('yo050_00', 1)	# 1-1
    sprite('yo050_01', 1)	# 2-2
    sprite('yo050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('yo050_01', 1)	# 1-1
    sprite('yo050_02', 1)	# 2-2
    sprite('yo050_01', 2)	# 3-4
    sprite('yo050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('yo050_02', 1)	# 1-1
    sprite('yo050_03', 1)	# 2-2
    sprite('yo050_02', 2)	# 3-4
    sprite('yo050_01', 2)	# 5-6
    sprite('yo050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('yo050_03', 1)	# 1-1
    sprite('yo050_04', 1)	# 2-2
    sprite('yo050_03', 2)	# 3-4
    sprite('yo050_02', 2)	# 5-6
    sprite('yo050_01', 2)	# 7-8
    sprite('yo050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('yo050_04', 1)	# 1-1
    sprite('yo050_04', 1)	# 2-2
    sprite('yo050_04', 2)	# 3-4
    sprite('yo050_03', 2)	# 5-6
    sprite('yo050_02', 2)	# 7-8
    sprite('yo050_01', 2)	# 9-10
    sprite('yo050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('yo052_00', 1)	# 1-1
    sprite('yo052_01', 1)	# 2-2
    sprite('yo052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('yo052_01', 1)	# 1-1
    sprite('yo052_02', 1)	# 2-2
    sprite('yo052_01', 2)	# 3-4
    sprite('yo052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('yo052_02', 1)	# 1-1
    sprite('yo052_03', 1)	# 2-2
    sprite('yo052_02', 2)	# 3-4
    sprite('yo052_01', 2)	# 5-6
    sprite('yo052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('yo052_03', 1)	# 1-1
    sprite('yo052_04', 1)	# 2-2
    sprite('yo052_03', 2)	# 3-4
    sprite('yo052_02', 2)	# 5-6
    sprite('yo052_01', 2)	# 7-8
    sprite('yo052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('yo052_04', 1)	# 1-1
    sprite('yo052_04', 1)	# 2-2
    sprite('yo052_04', 2)	# 3-4
    sprite('yo052_03', 2)	# 5-6
    sprite('yo052_02', 2)	# 7-8
    sprite('yo052_01', 2)	# 9-10
    sprite('yo052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('yo054_00', 1)	# 1-1
    sprite('yo054_01', 1)	# 2-2
    sprite('yo054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('yo054_01', 1)	# 1-1
    sprite('yo054_02', 1)	# 2-2
    sprite('yo054_01', 2)	# 3-4
    sprite('yo054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('yo054_02', 1)	# 1-1
    sprite('yo054_03', 1)	# 2-2
    sprite('yo054_02', 2)	# 3-4
    sprite('yo054_01', 2)	# 5-6
    sprite('yo054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('yo054_03', 1)	# 1-1
    sprite('yo054_04', 1)	# 2-2
    sprite('yo054_03', 2)	# 3-4
    sprite('yo054_02', 2)	# 5-6
    sprite('yo054_01', 2)	# 7-8
    sprite('yo054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('yo054_04', 1)	# 1-1
    sprite('yo054_04', 1)	# 2-2
    sprite('yo054_04', 2)	# 3-4
    sprite('yo054_03', 2)	# 5-6
    sprite('yo054_02', 2)	# 7-8
    sprite('yo054_01', 2)	# 9-10
    sprite('yo054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('yo060_00', 4)	# 1-4
    label(0)
    sprite('yo060_01', 4)	# 5-8
    sprite('yo060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('yo060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('yo060_04', 8)	# 1-8
    label(1)
    sprite('yo060_05', 4)	# 9-12
    sprite('yo060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('yo063_05', 6)	# 1-6

@State
def CmnActBDownBound():
    sprite('yo060_08', 2)	# 1-2
    sprite('yo060_09', 2)	# 3-4
    sprite('yo060_10', 2)	# 5-6
    sprite('yo060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('yo060_12', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('yo064_00', 6)	# 1-6
    sprite('yo064_01', 6)	# 7-12
    sprite('yo064_02', 6)	# 13-18
    sprite('yo064_03', 6)	# 19-24

@State
def CmnActFDownUpper():
    sprite('yo063_00', 4)	# 1-4

@State
def CmnActFDownUpperEnd():
    sprite('yo063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('yo063_03', 3)	# 1-3
    sprite('yo063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('yo063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('yo060_08', 2)	# 1-2
    sprite('yo060_09', 2)	# 3-4
    sprite('yo060_10', 2)	# 5-6
    sprite('yo060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('yo060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('yo064_00', 6)	# 1-6
    sprite('yo064_01', 6)	# 7-12
    sprite('yo064_02', 6)	# 13-18
    sprite('yo064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('yo060_00', 4)	# 1-4
    label(0)
    sprite('yo060_01', 4)	# 5-8
    sprite('yo060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('yo060_03', 4)	# 1-4
    sprite('yo060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('yo060_04', 8)	# 1-8
    label(0)
    sprite('yo060_05', 4)	# 9-12
    sprite('yo060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('yo060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('yo072_00', 3)	# 1-3
    sprite('yo072_01', 3)	# 4-6
    sprite('yo072_02', 3)	# 7-9
    label(0)
    sprite('yo072_01', 3)	# 10-12
    sprite('yo072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('yo074_00', 2)	# 1-2
    sprite('yo074_01', 2)	# 3-4
    sprite('yo074_02', 2)	# 5-6
    sprite('yo074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('yo072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('yo063_00', 3)	# 1-3
    label(0)
    sprite('yo063_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('yo082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('yo052_01', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('yo070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('yo070_01', 4)	# 1-4
    sprite('yo070_02', 4)	# 5-8
    sprite('yo070_03', 4)	# 9-12
    sprite('yo070_04', 4)	# 13-16
    sprite('yo070_05', 4)	# 17-20
    sprite('yo070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('yo040_03', 2)	# 1-2
    sprite('yo040_02', 2)	# 3-4
    sprite('yo040_01', 2)	# 5-6
    sprite('yo040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('yo020_02', 3)	# 1-3
    sprite('yo020_03', 3)	# 4-6
    sprite('yo020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('yo020_02', 3)	# 1-3
    sprite('yo020_03', 3)	# 4-6
    sprite('yo020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('yo020_02', 3)	# 1-3
    sprite('yo020_03', 3)	# 4-6
    sprite('yo020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('yo112_00', 3)	# 1-3
    sprite('yo112_01', 3)	# 4-6
    sprite('yo112_02', 3)	# 7-9
    sprite('yo112_03', 3)	# 10-12
    sprite('yo112_04', 3)	# 13-15
    sprite('yo112_05', 3)	# 16-18
    sprite('yo020_07', 4)	# 19-22
    sprite('yo020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandF():
    sprite('yo112_00', 3)	# 1-3
    sprite('yo112_01', 3)	# 4-6
    sprite('yo112_02', 3)	# 7-9
    sprite('yo112_03', 3)	# 10-12
    sprite('yo112_04', 3)	# 13-15
    sprite('yo112_05', 3)	# 16-18
    sprite('yo020_07', 4)	# 19-22
    sprite('yo020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('yo112_00', 3)	# 1-3
    sprite('yo112_01', 3)	# 4-6
    sprite('yo112_02', 3)	# 7-9
    sprite('yo112_03', 3)	# 10-12
    sprite('yo112_04', 3)	# 13-15
    sprite('yo112_05', 3)	# 16-18
    sprite('yo020_07', 4)	# 19-22
    sprite('yo020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('yo010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('yo040_00', 3)	# 1-3
    sprite('yo040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('yo040_02', 5)	# 1-5
    sprite('yo040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('yo040_01', 3)	# 1-3
    sprite('yo040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('yo040_04', 1)	# 1-1
    label(0)
    sprite('yo040_02', 5)	# 2-6
    sprite('yo040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('yo040_01', 3)	# 1-3
    sprite('yo040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('yo040_00', 3)	# 1-3
    sprite('yo040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('yo040_04', 1)	# 1-1
    label(0)
    sprite('yo040_02', 5)	# 2-6
    sprite('yo040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('yo040_01', 3)	# 1-3
    sprite('yo040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('yo040_04', 1)	# 1-1
    label(0)
    sprite('yo040_02', 5)	# 2-6
    sprite('yo040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('yo040_01', 3)	# 1-3
    sprite('yo040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('yo043_00', 3)	# 1-3
    sprite('yo043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('yo043_02', 5)	# 1-5
    sprite('yo043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('yo043_01', 3)	# 1-3
    sprite('yo043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('yo043_04', 1)	# 1-1
    label(0)
    sprite('yo043_02', 5)	# 2-6
    sprite('yo043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('yo043_01', 3)	# 1-3
    sprite('yo043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('yo045_00', 3)	# 1-3
    sprite('yo045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('yo045_02', 5)	# 1-5
    sprite('yo045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('yo045_01', 3)	# 1-3
    sprite('yo045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('yo045_04', 1)	# 1-1
    label(0)
    sprite('yo045_02', 5)	# 2-6
    sprite('yo045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('yo045_01', 3)	# 1-3
    sprite('yo045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('yo040_04', 2)	# 1-2
    sprite('yo040_04', 2)	# 3-4
    sprite('yo040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('yo040_02', 4)	# 6-9
    sprite('yo040_01', 4)	# 10-13
    sprite('yo040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('yo043_04', 2)	# 1-2
    sprite('yo043_04', 2)	# 3-4
    sprite('yo043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('yo043_02', 4)	# 6-9
    sprite('yo043_01', 4)	# 10-13
    sprite('yo043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('yo045_04', 2)	# 1-2
    sprite('yo045_04', 2)	# 3-4
    sprite('yo045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('yo045_02', 4)	# 6-9
    sprite('yo045_01', 4)	# 10-13
    sprite('yo045_00', 4)	# 14-17

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('yo200_00', 8)	# 1-8
    sprite('yo200_01', 5)	# 9-13
    sprite('yo200_02', 5)	# 14-18	 **attackbox here**
    sprite('yo200_04', 4)	# 19-22	 **attackbox here**
    sprite('yo200_05', 4)	# 23-26
    sprite('yo200_06', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('nt045_02', 1)	# 1-1
    sprite('nt045_01', 3)	# 2-4
    sprite('nt045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('yo250_00', 3)	# 1-3
    sprite('yo250_01', 3)	# 4-6
    sprite('yo250_03', 3)	# 7-9	 **attackbox here**
    Unknown7009(0)
    sprite('yo250_03', 7)	# 10-16	 **attackbox here**
    Unknown23027()
    sprite('yo250_04', 3)	# 17-19
    sprite('yo250_05', 3)	# 20-22
    sprite('yo250_06', 3)	# 23-25
    Unknown2001()

@State
def CmnActLandSpin():
    sprite('yo071_00', 2)	# 1-2
    label(0)
    sprite('yo071_01', 2)	# 3-4
    sprite('yo071_02', 2)	# 5-6
    sprite('yo071_03', 2)	# 7-8
    sprite('yo071_04', 2)	# 9-10
    sprite('yo071_05', 2)	# 11-12
    sprite('yo071_06', 2)	# 13-14
    sprite('yo071_07', 2)	# 15-16
    sprite('yo071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('yo040_02', 3)	# 1-3
    sprite('yo040_01', 3)	# 4-6
    sprite('yo040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('yo071_00', 2)	# 1-2
    label(0)
    sprite('yo071_01', 2)	# 3-4
    sprite('yo071_02', 2)	# 5-6
    sprite('yo071_03', 2)	# 7-8
    sprite('yo071_04', 2)	# 9-10
    sprite('yo071_05', 2)	# 11-12
    sprite('yo071_06', 2)	# 13-14
    sprite('yo071_07', 2)	# 15-16
    sprite('yo071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('yo124_00', 2)	# 1-2
    label(0)
    sprite('yo124_01', 2)	# 3-4
    sprite('yo124_02', 2)	# 5-6
    sprite('yo124_03', 2)	# 7-8
    sprite('yo124_04', 2)	# 9-10
    sprite('yo124_05', 2)	# 11-12
    sprite('yo124_06', 2)	# 13-14
    sprite('yo124_07', 2)	# 15-16
    sprite('yo124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('yo077_02', 4)	# 1-4
    label(0)
    sprite('yo077_03', 3)	# 5-7
    sprite('yo077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('yo077_05', 5)	# 1-5
    sprite('yo077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('yo077_02', 4)	# 1-4
    label(0)
    sprite('yo077_03', 3)	# 5-7
    sprite('yo077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('yo077_05', 5)	# 1-5
    sprite('yo077_06', 4)	# 6-9

@State
def CmnActBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    label(0)
    sprite('yo121_00', 2)	# 1-2
    sprite('yo121_01', 2)	# 3-4
    sprite('yo121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('yo121_03', 3)	# 1-3
    label(1)
    sprite('yo121_04', 2)	# 4-5
    sprite('yo121_05', 2)	# 6-7
    sprite('yo121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActBurstEnd():
    sprite('yo121_07', 3)	# 1-3
    sprite('yo121_08', 3)	# 4-6
    sprite('yo020_04', 3)	# 7-9
    sprite('yo020_05', 3)	# 10-12
    sprite('yo020_06', 3)	# 13-15
    sprite('yo020_07', 4)	# 16-19
    sprite('yo020_08', 4)	# 20-23
    loopRest()

@State
def CmnActAirBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    sprite('nt331_11', 2)	# 1-2
    sprite('nt331_12', 2)	# 3-4
    label(0)
    sprite('nt331_02', 3)	# 5-7
    sprite('nt331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('nt331_04', 2)	# 1-2
    sprite('nt331_05', 2)	# 3-4
    label(0)
    sprite('nt331_06', 3)	# 5-7
    sprite('nt331_07', 3)	# 8-10
    sprite('nt331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('yo121_07', 2)	# 1-2
    sprite('yo121_08', 2)	# 3-4
    sprite('yo020_05', 3)	# 5-7
    sprite('yo020_06', 3)	# 8-10
    label(0)
    sprite('yo020_07', 4)	# 11-14
    sprite('yo020_08', 4)	# 15-18
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('yo121_00', 2)	# 1-2
    sprite('yo121_01', 2)	# 3-4
    sprite('yo121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('yo121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('yo121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('yo121_04', 2)	# 4-5
    sprite('yo121_05', 2)	# 6-7
    sprite('yo121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActOverDriveEnd():
    sprite('yo121_07', 4)	# 1-4
    sprite('yo121_08', 4)	# 5-8
    sprite('yo010_00', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('yo121_00', 2)	# 1-2
    sprite('yo121_01', 2)	# 3-4
    sprite('yo121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('yo121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('yo121_03', 3)	# 1-3
    label(1)
    sprite('yo121_04', 2)	# 4-5
    sprite('yo121_05', 2)	# 6-7
    sprite('yo121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirOverDriveEnd():
    sprite('yo121_07', 2)	# 1-2
    sprite('yo121_08', 2)	# 3-4
    sprite('yo020_04', 3)	# 5-7
    sprite('yo020_05', 3)	# 8-10
    sprite('yo020_06', 2)	# 11-12
    label(0)
    sprite('yo020_07', 4)	# 13-16
    sprite('yo020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('yo121_00', 2)	# 1-2
    sprite('yo121_01', 2)	# 3-4
    sprite('yo121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(11)
    Unknown23148('PYO_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 10, 0)
    sprite('yo121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('yo121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('yo121_04', 2)	# 4-5
    sprite('yo121_05', 2)	# 6-7
    sprite('yo121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossRushEnd():
    sprite('yo121_07', 2)	# 1-2
    sprite('yo121_08', 2)	# 3-4
    sprite('yo020_04', 2)	# 5-6
    sprite('yo020_05', 2)	# 7-8
    sprite('yo020_06', 2)	# 9-10
    sprite('yo020_07', 2)	# 11-12

@State
def CmnActAirCrossRushBegin():
    sprite('yo121_00', 2)	# 1-2
    sprite('yo121_01', 2)	# 3-4
    sprite('yo121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(11)
    Unknown23148('PYO_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 10, 0)
    sprite('yo121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('yo121_03', 3)	# 1-3
    label(1)
    sprite('yo121_04', 2)	# 4-5
    sprite('yo121_05', 2)	# 6-7
    sprite('yo121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossRushEnd():
    sprite('yo121_07', 2)	# 1-2
    sprite('yo121_08', 2)	# 3-4
    sprite('yo020_04', 3)	# 5-7
    sprite('yo020_05', 3)	# 8-10
    sprite('yo020_06', 2)	# 11-12
    label(0)
    sprite('yo020_07', 4)	# 13-16
    sprite('yo020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
        Unknown36(11)
        Unknown23148('PYO_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 10, 0)
    label(0)
    sprite('yo121_00', 2)	# 1-2
    sprite('yo121_01', 2)	# 3-4
    sprite('yo121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('yo121_03', 3)	# 1-3
    label(1)
    sprite('yo121_04', 2)	# 4-5
    sprite('yo121_05', 2)	# 6-7
    sprite('yo121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossChangeEnd():
    sprite('yo121_07', 3)	# 1-3
    sprite('yo121_08', 3)	# 4-6
    sprite('yo020_04', 3)	# 7-9
    sprite('yo020_05', 3)	# 10-12
    sprite('yo020_06', 3)	# 13-15
    sprite('yo020_07', 4)	# 16-19
    sprite('yo020_08', 4)	# 20-23
    loopRest()

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
        Unknown36(11)
        Unknown23148('PYO_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 10, 0)
    label(0)
    sprite('yo121_00', 2)	# 1-2
    sprite('yo121_01', 2)	# 3-4
    sprite('yo121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('yo121_03', 3)	# 1-3
    label(1)
    sprite('yo121_04', 2)	# 4-5
    sprite('yo121_05', 2)	# 6-7
    sprite('yo121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossChangeEnd():
    sprite('yo121_07', 3)	# 1-3
    sprite('yo121_08', 3)	# 4-6
    sprite('yo020_04', 3)	# 7-9
    sprite('yo020_05', 3)	# 10-12
    sprite('yo020_06', 3)	# 13-15
    label(0)
    sprite('yo020_07', 4)	# 16-19
    sprite('yo020_08', 4)	# 20-23
    loopRest()
    gotoLabel(0)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(630)
        Unknown11092(1)
        Hitstop(3)
        Unknown9016(1)
        PushbackX(12000)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('yo203_00', 2)	# 1-2
    sprite('yo203_01', 2)	# 3-4
    sprite('yo203_02', 2)	# 5-6
    sprite('yo203_03', 2)	# 7-8
    sprite('yo203_04', 2)	# 9-10	 **attackbox here**
    Unknown7009(1)
    SFX_3('slash_knife_middle')
    sprite('yo203_05', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_knife_middle')
    sprite('yo203_06', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_knife_middle')
    sprite('yo203_07', 5)	# 15-19
    Recovery()
    Unknown2063()
    sprite('yo203_08', 6)	# 20-25
    sprite('yo203_09', 5)	# 26-30

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1300)
        Unknown9016(1)
        AirPushbackY(-8000)
        Unknown9190(1)
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('yo201_00', 2)	# 1-2
    sprite('yo201_01', 2)	# 3-4
    sprite('yo201_02', 2)	# 5-6
    sprite('yo201_03', 2)	# 7-8
    SFX_3('slash_knife_middle')
    sprite('yo201_06', 4)	# 9-12	 **attackbox here**
    Unknown23054('796f3230315f303400000000000000000000000000000000000000000000000004000000')
    RefreshMultihit()
    Unknown7009(1)
    sprite('yo201_06', 4)	# 13-16	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('yo201_07', 3)	# 17-19
    sprite('yo201_08', 3)	# 20-22
    sprite('yo201_09', 4)	# 23-26

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(750)
        AttackP2(75)
        Unknown11092(1)
        AirUntechableTime(30)
        Unknown9016(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(32000)
        PushbackX(19800)
        Hitstop(4)
        sendToLabelUpon(2, 1)
        HitJumpCancel(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
    sprite('yo202_00', 2)	# 1-2
    sprite('yo202_01', 4)	# 3-6
    physicsXImpulse(24000)
    sprite('yo202_02', 1)	# 7-7
    sprite('yo202_03', 1)	# 8-8
    sprite('yo202_04', 1)	# 9-9
    SFX_3('hit_m_middle')
    Unknown7009(2)
    sprite('yo202_06', 2)	# 10-11	 **attackbox here**
    Unknown1019(80)
    physicsXImpulse(3000)
    physicsYImpulse(30000)
    setGravity(2000)
    SFX_3('slash_knife_slow')
    Unknown14070('NmlAtkA4th')
    Unknown14070('MoonsaltMoveR')
    Unknown14070('MoonsaltMoveL')
    Unknown14070('VSlash_R')
    Unknown14070('VSlash_L')
    Unknown14070('UltimateTatsumaki')
    Unknown14070('UltimateTatsumakiOD')
    Unknown14070('UltimateKunai')
    Unknown14070('UltimateKunaiOD')
    sprite('yo202_06', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    Unknown23054('796f3230325f303500000000000000000000000000000000000000000000000004000000')
    sprite('yo202_06', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('yo202_07', 3)	# 16-18
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('yo202_08', 3)	# 19-21
    if SLOT_2:
        Unknown14072('NmlAtkA4th')
        Unknown14072('MoonsaltMoveR')
        Unknown14072('MoonsaltMoveL')
        Unknown14072('VSlash_R')
        Unknown14072('VSlash_L')
        Unknown14072('UltimateTatsumaki')
        Unknown14072('UltimateTatsumakiOD')
        Unknown14072('UltimateKunai')
        Unknown14072('UltimateKunaiOD')
    label(0)
    sprite('yo020_07', 4)	# 22-25
    sprite('yo020_08', 4)	# 26-29
    gotoLabel(0)
    label(1)
    sprite('yo010_00', 3)	# 30-32
    Unknown1084(1)
    Unknown8000(100, 1, 1)

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        AirPushbackY(16000)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown9016(1)
    sprite('yo200_00', 2)	# 1-2
    sprite('yo200_01', 3)	# 3-5
    sprite('yo200_04', 3)	# 6-8	 **attackbox here**
    Unknown23054('796f3230305f303200000000000000000000000000000000000000000000000003000000')
    Unknown7009(0)
    SFX_3('slash_knife_fast')
    WhiffCancelEnable(1)
    sprite('yo200_04', 3)	# 9-11	 **attackbox here**
    sprite('yo200_05', 4)	# 12-15
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('yo200_06', 4)	# 16-19

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1300)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('yo207_01', 4)	# 1-4
    teleportRelativeX(20000)
    sprite('yo207_02', 3)	# 5-7
    SFX_3('slash_knife_middle')
    sprite('yo207_04', 3)	# 8-10	 **attackbox here**
    Unknown23054('796f3230375f303300000000000000000000000000000000000000000000000003000000')
    Unknown7009(1)
    sprite('yo207_04', 5)	# 11-15	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('yo207_05', 5)	# 16-20
    sprite('yo207_06', 5)	# 21-25
    sprite('yo207_07', 5)	# 26-30

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP2(75)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(-1000)
        HitOverhead(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
    sprite('yo208_00', 4)	# 1-4
    physicsXImpulse(20000)
    sprite('yo208_01', 3)	# 5-7
    physicsXImpulse(5000)
    sprite('yo208_02', 2)	# 8-9
    sprite('yo208_04ex', 3)	# 10-12	 **attackbox here**
    Unknown23054('796f3230385f303300000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_m_middle')
    Unknown7009(2)
    physicsXImpulse(-6000)
    physicsYImpulse(22000)
    setGravity(2000)
    Unknown14070('NmlAtkA4th')
    Unknown14070('MoonsaltMoveR')
    Unknown14070('MoonsaltMoveL')
    Unknown14070('VSlash_R')
    Unknown14070('VSlash_L')
    Unknown14070('UltimateTatsumaki')
    Unknown14070('UltimateTatsumakiOD')
    Unknown14070('UltimateKunai')
    Unknown14070('UltimateKunaiOD')
    sprite('yo208_04', 2)	# 13-14	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('yo208_05', 2)	# 15-16
    sprite('yo208_06', 2)	# 17-18
    Unknown23027()
    if SLOT_2:
        Unknown14072('NmlAtkA4th')
        Unknown14072('MoonsaltMoveR')
        Unknown14072('MoonsaltMoveL')
        Unknown14072('VSlash_R')
        Unknown14072('VSlash_L')
        Unknown14072('UltimateTatsumaki')
        Unknown14072('UltimateTatsumakiOD')
        Unknown14072('UltimateKunai')
        Unknown14072('UltimateKunaiOD')
    sprite('yo208_07', 3)	# 19-21
    sprite('yo208_08', 3)	# 22-24
    sprite('yo208_09', 6)	# 25-30
    sprite('yo020_05', 3)	# 31-33
    sprite('yo020_06', 3)	# 34-36
    label(0)
    sprite('yo020_07', 3)	# 37-39
    sprite('yo020_08', 3)	# 40-42
    gotoLabel(0)

@State
def NmlAtkA4th():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)
        callSubroutine('DoNotBeginCancel')
    sprite('yo404_00', 2)	# 1-2
    SFX_3('yo005')
    sprite('yo404_01', 2)	# 3-4
    sprite('yo404_50', 1)	# 5-5
    Unknown7007('70796f3230395f3000000000000000006400000070796f3231305f3000000000000000006400000070796f3231305f3100000000000000006400000070796f3231305f32000000000000000064000000')
    physicsXImpulse(-2000)
    physicsYImpulse(8000)
    setGravity(0)
    Unknown1051(0)
    SLOT_66 = (SLOT_66 + 1)
    sprite('yo404_02', 6)	# 6-11
    GFX_1('yoef_kunai_flash', 0)
    GFX_1('yoef_kunai_flash', 1)
    sprite('yo404_03', 2)	# 12-13
    physicsXImpulse(-10000)
    physicsYImpulse(30000)
    setGravity(2000)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('yo404_04', 1)	# 14-14
    GFX_0('kunaishotA_Matome', 100)
    SFX_3('yo006')
    sprite('yo404_04', 2)	# 15-16
    SFX_3('yo006')
    sprite('yo404_05', 5)	# 17-21
    SFX_3('yo006')
    sprite('yo404_06', 5)	# 22-26
    sprite('yo404_07', 5)	# 27-31
    sprite('yo404_08', 3)	# 32-34
    sprite('yo404_09', 3)	# 35-37
    sprite('yo404_10', 5)	# 38-42
    Recovery()
    sprite('yo020_04', 5)	# 43-47
    sprite('yo020_05', 5)	# 48-52
    sprite('yo020_06', 5)	# 53-57
    label(0)
    sprite('yo020_07', 5)	# 58-62
    sprite('yo020_08', 5)	# 63-67
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yo010_00', 6)	# 68-73
    Unknown1084(1)
    Unknown8000(100, 1, 1)

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        Unknown9016(1)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('yo230_00', 2)	# 1-2
    sprite('yo230_01', 2)	# 3-4
    sprite('yo230_02', 2)	# 5-6
    sprite('yo230_04', 3)	# 7-9	 **attackbox here**
    Unknown23054('796f3233305f303300000000000000000000000000000000000000000000000003000000')
    Unknown7009(0)
    SFX_3('hit_m_fast')
    SFX_3('slash_knife_fast')
    sprite('yo230_04', 3)	# 10-12	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('yo230_02', 6)	# 13-18
    sprite('yo230_00', 6)	# 19-24

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B2nd')
        HitJumpCancel(1)
    sprite('yo204_00', 3)	# 1-3
    sprite('yo204_01', 4)	# 4-7
    Unknown23029(11, 101, 0)
    Unknown7007('70796f3132305f3000000000000000006400000070796f3132305f3100000000000000006400000070796f3132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yo204_02', 3)	# 8-10
    sprite('yo204_03', 3)	# 11-13
    GFX_1('persona_enter_ply', 0)
    sprite('yo204_04', 1)	# 14-14
    sprite('yo204_04', 2)	# 15-16
    Recovery()
    Unknown2063()
    sprite('yo204_05', 3)	# 17-19
    sprite('yo204_06', 3)	# 20-22
    sprite('yo204_04', 3)	# 23-25
    sprite('yo204_05', 3)	# 26-28
    sprite('yo204_06', 3)	# 29-31
    sprite('yo204_05', 4)	# 32-35
    sprite('yo204_02', 3)	# 36-38
    sprite('yo204_01', 4)	# 39-42
    sprite('yo204_00', 2)	# 43-44

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5B3rd')
        HitOrBlockCancel('NmlAtk2C')
    sprite('yo205_00', 2)	# 1-2
    sprite('yo205_01', 2)	# 3-4
    sprite('yo205_01', 1)	# 5-5
    Unknown7007('70796f3132335f3000000000000000006400000070796f3132335f3200000000000000006400000070796f3132315f3000000000000000006400000070796f3132315f31000000000000000064000000')
    Unknown23029(11, 201, 0)
    sprite('yo205_02', 3)	# 6-8
    sprite('yo205_03', 3)	# 9-11
    GFX_1('persona_enter_ply', 0)
    sprite('yo205_04', 3)	# 12-14
    sprite('yo205_05', 3)	# 15-17
    sprite('yo205_06', 1)	# 18-18
    sprite('yo205_06', 2)	# 19-20
    Recovery()
    Unknown2063()
    sprite('yo205_04', 3)	# 21-23
    sprite('yo205_05', 3)	# 24-26
    sprite('yo205_06', 3)	# 27-29
    sprite('yo205_04', 3)	# 30-32
    sprite('yo205_02', 3)	# 33-35
    sprite('yo205_01', 3)	# 36-38
    sprite('yo205_00', 2)	# 39-40

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(1)
        callSubroutine('DoNotBeginCancel')
        JumpCancel_(0)
    sprite('yo402_00', 3)	# 1-3
    sprite('yo402_01', 3)	# 4-6
    sprite('yo402_01', 3)	# 7-9
    tag_voice(1, 'pyo203_0', 'pyo203_2', 'pyo205_0', 'pyo205_1')
    sprite('yo402_02', 4)	# 10-13
    Unknown23029(11, 401, 0)
    sprite('yo402_03', 4)	# 14-17
    GFX_1('persona_enter_ply', 0)
    sprite('yo402_50', 2)	# 18-19
    sprite('yo402_50', 18)	# 20-37
    Recovery()
    sprite('yo402_05', 5)	# 38-42
    sprite('yo402_06', 5)	# 43-47
    loopRest()
    ExitState()
    label(1)
    clearUponHandler(43)
    sprite('yo402_50', 40)	# 48-87
    setInvincible(1)
    sprite('yo402_50', 15)	# 88-102
    callSubroutine('LandSpecialAttack_DeriveInput')
    sprite('yo402_04', 20)	# 103-122
    tag_voice(0, 'pyo204_0', 'pyo204_2', 'pyo206_0', 'pyo206_1')
    sprite('yo402_04', 10)	# 123-132
    callSubroutine('LandSpecialAttack_DeriveTiming')
    sprite('yo402_05', 5)	# 133-137
    sprite('yo402_06', 5)	# 138-142

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackX(6000)
        AirPushbackY(27000)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        AirUntechableTime(20)
        Unknown28(8, 'CmnActStand')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
    sprite('yo231_00', 2)	# 1-2
    sprite('yo231_01', 2)	# 3-4
    sprite('yo231_02', 1)	# 5-5
    sprite('yo231_03', 2)	# 6-7
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('yo231_04', 1)	# 8-8
    sprite('yo231_06', 4)	# 9-12	 **attackbox here**
    Unknown23054('796f3233315f303500000000000000000000000000000000000000000000000004000000')
    Unknown7007('70796f3130365f3000000000000000006400000070796f3130365f3100000000000000006400000070796f3130365f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_knife_slow')
    sprite('yo231_06', 11)	# 13-23	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('yo231_07', 3)	# 24-26
    sprite('yo231_08', 3)	# 27-29
    sprite('yo231_09', 3)	# 30-32
    sprite('yo231_10', 3)	# 33-35
    sprite('yo231_11', 3)	# 36-38

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9016(1)
        AirPushbackX(3000)
        AirPushbackY(15000)
        AirUntechableTime(40)
    sprite('yo211_00', 3)	# 1-3
    sprite('yo211_00', 1)	# 4-4
    sprite('yo211_01', 3)	# 5-7
    physicsXImpulse(23000)
    Unknown8006(100, 1, 0)
    sprite('yo211_01', 3)	# 8-10
    Unknown8006(100, 1, 0)
    Unknown7007('70796f3130375f3000000000000000006400000070796f3130375f3100000000000000006400000070796f3130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yo211_02', 3)	# 11-13	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    SFX_3('slash_knife_middle')
    sprite('yo211_03', 4)	# 14-17
    Unknown1019(90)
    Recovery()
    sprite('yo211_04', 4)	# 18-21
    Unknown1019(60)
    sprite('yo211_05', 4)	# 22-25
    Unknown1019(60)
    sprite('yo211_06', 3)	# 26-28
    Unknown1019(60)
    sprite('yo211_06', 1)	# 29-29
    physicsXImpulse(0)
    sprite('yo211_06', 2)	# 30-31
    sprite('yo211_07', 3)	# 32-34
    sprite('yo211_08', 3)	# 35-37

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1000)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAir5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('yo251_06', 2)	# 1-2
    sprite('yo251_00', 3)	# 3-5
    sprite('yo251_01', 4)	# 6-9
    sprite('yo251_02', 2)	# 10-11	 **attackbox here**
    Unknown7009(4)
    SFX_3('slash_knife_middle')
    sprite('yo251_02', 2)	# 12-13	 **attackbox here**
    sprite('yo251_03', 3)	# 14-16
    Recovery()
    Unknown2063()
    sprite('yo251_07', 3)	# 17-19
    sprite('yo251_08', 4)	# 20-23

@State
def NmlAtkAir5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1000)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('yo250_00', 2)	# 1-2
    sprite('yo250_01', 2)	# 3-4
    sprite('yo250_02', 2)	# 5-6
    Unknown7009(3)
    SFX_3('slash_knife_fast')
    sprite('yo250_03', 3)	# 7-9	 **attackbox here**
    sprite('yo250_05', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('yo250_05', 4)	# 13-16
    WhiffCancelEnable(1)
    sprite('yo250_06', 4)	# 17-20

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        HitOrBlockCancel('NmlAtkAIR5C')
        AttackDefaults_AirNormal()

        def upon_LANDING():
            Unknown23029(11, 3001, 0)

        def upon_STATE_END():
            Unknown23029(11, 3003, 0)
            Unknown21015('4169723543746f726e61646f3030000000000000000000000000000000000000bb0b000000000000')
            Unknown21015('4169723543746f726e61646f3031000000000000000000000000000000000000bb0b000000000000')
    sprite('yo254_00', 3)	# 1-3
    sprite('yo254_01', 4)	# 4-7
    Unknown23029(11, 301, 0)
    sprite('yo254_02', 2)	# 8-9
    Unknown7007('70796f3132305f3000000000000000006400000070796f3132305f3200000000000000006400000070796f3132315f3100000000000000006400000070796f3132335f30000000000000000064000000')
    Unknown1019(70)
    YAccel(70)
    setGravity(2100)
    sprite('yo254_03', 3)	# 10-12
    GFX_1('persona_enter_ply', 0)
    sprite('yo254_04', 3)	# 13-15
    sprite('yo254_05', 3)	# 16-18
    sprite('yo254_06', 3)	# 19-21
    sprite('yo254_04', 3)	# 22-24
    sprite('yo254_05', 3)	# 25-27
    sprite('yo254_06', 3)	# 28-30
    sprite('yo254_03', 2)	# 31-32
    sprite('yo254_02', 2)	# 33-34
    sprite('yo254_01', 4)	# 35-38
    sprite('yo254_00', 2)	# 39-40

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Hitstop(4)
        Unknown9016(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HitOverhead(0)
        HitLow(2)
        AirPushbackX(3000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown23001(0, 0)
        Unknown23014()
        Unknown3029(0)
    sprite('yo406_00', 3)	# 1-3
    sprite('yo406_01', 3)	# 4-6
    Unknown2006()
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 421, 0)
    Unknown1084(1)
    Unknown2017(0)
    sprite('yo406_02', 5)	# 7-11
    setInvincible(1)
    Unknown13015(1)
    SLOT_65 = (SLOT_65 + 1)
    SLOT_5 = 0
    SLOT_6 = 0
    sprite('yo406_02', 13)	# 12-24
    Unknown3038(1)
    SFX_3('yo001')
    sprite('yo406_03', 7)	# 25-31
    sprite('yo406_03', 2)	# 32-33
    setInvincible(0)
    Unknown3038(0)
    Unknown18009(1)
    SFX_3('yo000')
    Unknown2017(1)
    teleportRelativeY(0)
    Unknown1084(0)
    teleportRelativeX(-100000)
    Unknown13015(0)
    GFX_0('Warp_Out', 103)
    callSubroutine('LandingRegReset')
    sprite('yo406_04', 2)	# 34-35
    physicsXImpulse(7000)
    Unknown7007('70796f3231335f3000000000000000006400000070796f3231335f3100000000000000006400000070796f3231335f3200000000000000006400000070796f3231345f32000000000000000064000000')
    sprite('yo406_06', 2)	# 36-37	 **attackbox here**
    RefreshMultihit()
    Unknown1019(1000)
    sprite('yo406_05', 2)	# 38-39	 **attackbox here**
    sprite('yo406_06', 3)	# 40-42	 **attackbox here**
    Unknown1019(60)
    sprite('yo406_07', 3)	# 43-45
    Unknown1019(60)
    Recovery()
    sprite('yo406_07', 3)	# 46-48
    Unknown1019(60)
    sprite('yo406_08', 2)	# 49-50
    Unknown1019(50)
    sprite('yo406_08', 2)	# 51-52
    Unknown1019(50)
    sprite('yo406_08', 2)	# 53-54
    Unknown1019(50)
    sprite('yo406_08', 5)	# 55-59
    Unknown1019(0)
    sprite('yo406_09', 4)	# 60-63
    sprite('yo406_10', 4)	# 64-67

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(9000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(23000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 41000):
                    SLOT_12 = 41000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('yo032_10', 4)	# 1-4
    sprite('yo032_00', 3)	# 5-7
    label(0)
    sprite('yo032_01', 3)	# 8-10
    sprite('yo032_02', 3)	# 11-13
    sprite('yo032_03', 3)	# 14-16
    Unknown8006(100, 1, 1)
    sprite('yo032_04', 3)	# 17-19
    sprite('yo032_05', 3)	# 20-22
    sprite('yo032_06', 3)	# 23-25
    sprite('yo032_07', 3)	# 26-28
    Unknown8006(100, 1, 1)
    sprite('yo032_08', 3)	# 29-31
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yo310_00', 2)	# 32-33
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('yo310_01', 1)	# 34-34
    sprite('yo310_02', 3)	# 35-37	 **attackbox here**
    Unknown1084(1)
    sprite('yo310_03', 3)	# 38-40
    sprite('yo310_04', 10)	# 41-50
    SFX_4('pyo154')
    sprite('yo310_03', 4)	# 51-54
    sprite('yo310_01', 4)	# 55-58
    sprite('yo310_00', 2)	# 59-60

@State
def NmlAtkThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(50)
        Unknown11092(1)
        GroundedHitstunAnimation(4)
        Unknown9154(40)
        AirPushbackX(0)
        PushbackX(0)
        Unknown11050('06000000796f65665f7468726f7700000000000000000000000000000000000000000000')
        Unknown9016(1)
        Hitstop(0)
        Unknown2017(0)
        Unknown2018(0, 30)
        Unknown2034(0)
        Unknown12051(2)

        def upon_77():
            Unknown2038(1)
            SFX_0('101_hit_slash_1')
            if (SLOT_2 >= 2):
                JumpCancel_(1)
                if SLOT_62:
                    HitOrBlockCancel('Sukukaja5A')
                    HitOrBlockCancel('CmnActAirFDash')
                    HitOrBlockCancel('CmnActAirBDash')
        JumpCancel_(0)
        Unknown11064(1)
    sprite('yo310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown2018(0, 80)
    Unknown5003(1)
    sprite('yo311_00', 7)	# 5-11
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    SFX_4('pyo153')
    sprite('yo311_01', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(120000)
    SFX_3('damage_slash_h')

    def upon_55():
        SLOT_51 = 1
    sprite('yo311_02', 3)	# 15-17
    Unknown1019(20)
    sprite('yo311_03', 4)	# 18-21
    Unknown1019(0)
    sprite('yo311_04', 8)	# 22-29
    sprite('yo311_05', 4)	# 30-33	 **attackbox here**
    RefreshMultihit()
    Unknown11064(0)
    GroundedHitstunAnimation(0)
    physicsXImpulse(-115000)
    SFX_3('damage_slash_h')
    clearUponHandler(55)
    if SLOT_51:
        physicsXImpulse(-85000)
    sprite('yo311_06', 10)	# 34-43	 **attackbox here**
    Unknown1019(0)
    sprite('yo311_07', 4)	# 44-47
    Unknown1019(0)
    sprite('yo311_08', 4)	# 48-51
    sprite('yo311_09', 4)	# 52-55
    sprite('yo311_10', 4)	# 56-59

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkBackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(9000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(23000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 41000):
                    SLOT_12 = 41000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('yo032_10', 4)	# 1-4
    sprite('yo032_00', 3)	# 5-7
    label(0)
    sprite('yo032_01', 3)	# 8-10
    sprite('yo032_02', 3)	# 11-13
    sprite('yo032_03', 3)	# 14-16
    Unknown8006(100, 1, 1)
    sprite('yo032_04', 3)	# 17-19
    sprite('yo032_05', 3)	# 20-22
    sprite('yo032_06', 3)	# 23-25
    sprite('yo032_07', 3)	# 26-28
    Unknown8006(100, 1, 1)
    sprite('yo032_08', 3)	# 29-31
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yo310_00', 2)	# 32-33
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('yo310_01', 1)	# 34-34
    sprite('yo310_02', 3)	# 35-37	 **attackbox here**
    Unknown1084(1)
    sprite('yo310_03', 3)	# 38-40
    sprite('yo310_04', 10)	# 41-50
    SFX_4('pyo154')
    sprite('yo310_03', 4)	# 51-54
    sprite('yo310_01', 4)	# 55-58
    sprite('yo310_00', 2)	# 59-60

@State
def NmlAtkBackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(50)
        Unknown11092(1)
        GroundedHitstunAnimation(4)
        Unknown9154(40)
        PushbackX(0)
        Unknown11050('06000000796f65665f7468726f7700000000000000000000000000000000000000000000')
        Unknown9016(1)
        Hitstop(0)
        Unknown2018(0, 30)
        Unknown2034(0)
        Unknown12051(2)
        Unknown2004(1, 0)

        def upon_77():
            Unknown2038(1)
            SFX_0('101_hit_slash_1')
            if (SLOT_2 >= 2):
                JumpCancel_(1)
                if SLOT_62:
                    HitOrBlockCancel('Sukukaja5A')
                    HitOrBlockCancel('CmnActAirFDash')
                    HitOrBlockCancel('CmnActAirBDash')
        JumpCancel_(0)
        Unknown11064(1)
    sprite('yo310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown2018(0, 80)
    Unknown5003(1)
    sprite('yo311_00', 7)	# 5-11
    Unknown2005()
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    SFX_4('pyo153')
    sprite('yo311_01', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(120000)
    SFX_3('damage_slash_h')

    def upon_55():
        SLOT_51 = 1
    sprite('yo311_02', 3)	# 15-17
    Unknown1019(20)
    sprite('yo311_03', 4)	# 18-21
    Unknown1019(0)
    sprite('yo311_04', 8)	# 22-29
    sprite('yo311_05', 4)	# 30-33	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(0)
    Unknown11064(0)
    physicsXImpulse(-115000)
    SFX_3('damage_slash_h')
    clearUponHandler(55)
    if SLOT_51:
        physicsXImpulse(-85000)
    sprite('yo311_06', 10)	# 34-43	 **attackbox here**
    Unknown1019(0)
    sprite('yo311_07', 4)	# 44-47
    Unknown1019(0)
    sprite('yo311_08', 4)	# 48-51
    sprite('yo311_09', 4)	# 52-55
    sprite('yo311_10', 4)	# 56-59

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(0)
        Damage(500)
        Unknown11092(1)
        Hitstop(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-8000)
        AirPushbackY(-40000)
        Unknown11084(1)
        Unknown11066(1)
        Unknown11042(1)
        AirUntechableTime(60)
        Unknown9202(1)
        Unknown9310(30)
        Unknown11032('801a06006079feffc0d4010000000000')
        Unknown11063(1)
        Unknown11064(1)
        Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11051('080000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown36(22)
        Unknown11051('080000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown35()
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0100000001000000010000000100000001000000')
        Unknown22031(-1, 17)

        def upon_52():
            clearUponHandler(52)
            sendToLabel(0)
    sprite('yo400_00', 3)	# 1-3
    Unknown1084(0)
    Unknown11085(1)
    tag_voice(1, 'pyo200_0', 'pyo200_1', 'pyo200_2', '')
    sprite('yo400_01', 3)	# 4-6
    SFX_3('slash_knife_slow')
    sprite('yo400_02', 3)	# 7-9
    sprite('yo400_03', 3)	# 10-12
    sprite('yo400_00', 3)	# 13-15
    sprite('yo400_01', 3)	# 16-18
    setInvincible(0)
    SFX_3('slash_knife_slow')
    sprite('yo400_03', 9)	# 19-27
    sprite('yo400_04', 12)	# 28-39
    sprite('yo400_05', 3)	# 40-42
    sprite('yo400_06', 3)	# 43-45
    tag_voice(0, 'pyo201_0', 'pyo201_1', 'pyo201_2', '')
    ExitState()
    label(0)
    sprite('yo401_00', 3)	# 46-48	 **attackbox here**
    Unknown23027()
    setInvincible(1)
    GuardPoint_(0)
    Unknown2018(0, 60)

    def upon_78():
        clearUponHandler(78)
        Unknown2038(1)
    sprite('yo401_01', 3)	# 49-51	 **attackbox here**
    sprite('yo401_02', 3)	# 52-54	 **attackbox here**
    Unknown23029(11, 441, 0)
    sprite('yo401_03', 3)	# 55-57	 **attackbox here**
    tag_voice(0, 'pyo202_0', 'pyo202_1', 'pyo202_2', '')
    sprite('yo401_04', 5)	# 58-62	 **attackbox here**
    sprite('yo401_04', 5)	# 63-67	 **attackbox here**
    sprite('yo401_04', 4)	# 68-71	 **attackbox here**
    setInvincible(0)
    sprite('yo401_04', 2)	# 72-73	 **attackbox here**
    sprite('yo401_04', 5)	# 74-78	 **attackbox here**
    sprite('yo401_03', 6)	# 79-84	 **attackbox here**
    sprite('yo401_05', 6)	# 85-90
    ExitState()

@State
def KakeagariA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        AttackP2(70)
        Unknown11092(1)
        Hitstop(0)
        Unknown11001(8, 8, 8)
        Unknown9310(1)
        AirHitstunAnimation(11)
        Unknown9154(20)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(-20000)
        PushbackX(8000)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1084(1)
            Unknown23027()
            callSubroutine('Kakeagari_DeriveInput')
            sendToLabel(1)

        def upon_3():
            if SLOT_51:
                if (SLOT_19 < 300000):
                    clearUponHandler(3)
                    sendToLabel(0)
                    SLOT_51 = 0

        def upon_LANDING():
            callSubroutine('Kakeagari_DeriveClear')
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            Unknown18009(1)
            sendToLabel(9)
        callSubroutine('DoNotBeginCancel')
    sprite('yo403_00', 2)	# 1-2
    sprite('yo403_01', 4)	# 3-6
    sprite('yo403_02', 2)	# 7-8
    Unknown7007('70796f3230375f3000000000000000006400000070796f3230375f3100000000000000006400000070796f3230375f3200000000000000006400000070796f3230385f30000000000000000064000000')
    physicsXImpulse(49000)
    SFX_3('runjump_stone_light')
    sprite('yo403_03', 2)	# 9-10
    SFX_3('airdash_m')
    sprite('yo403_04', 2)	# 11-12
    SLOT_51 = 1
    sprite('yo403_05', 2)	# 13-14
    sprite('yo403_06', 2)	# 15-16
    sprite('yo403_03', 2)	# 17-18
    SFX_3('runjump_stone_light')
    sprite('yo403_04', 2)	# 19-20
    sprite('yo403_05', 2)	# 21-22
    label(2)
    sprite('yo403_21', 2)	# 23-24
    SLOT_51 = 0
    Unknown1019(30)
    Recovery()
    sprite('yo403_22', 4)	# 25-28
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_23', 4)	# 29-32
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_24', 4)	# 33-36
    Unknown1019(50)
    sprite('yo403_25', 4)	# 37-40
    Unknown1019(0)
    loopRest()
    ExitState()
    label(0)
    sprite('yo403_07', 2)	# 41-42
    sprite('yo403_08', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('yo403_08', 2)	# 46-47	 **attackbox here**
    sprite('yo403_09', 2)	# 48-49	 **attackbox here**
    sprite('yo403_10', 2)	# 50-51
    physicsXImpulse(10000)
    physicsYImpulse(20000)
    setGravity(4500)
    sprite('yo403_11', 2)	# 52-53
    sprite('yo403_12', 2)	# 54-55	 **attackbox here**
    Unknown2015(40)
    Unknown1084(1)
    sprite('yo403_13', 3)	# 56-58	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(22000)
    Hitstop(9)
    Unknown9310(-1)
    sprite('yo403_14', 3)	# 59-61	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2015(-1)
    sprite('yo403_15', 3)	# 62-64
    Unknown1007(50000)
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    setGravity(2400)
    sprite('yo403_16', 3)	# 65-67
    clearUponHandler(3)
    callSubroutine('Kakeagari_DeriveTiming')
    sprite('yo403_17', 3)	# 68-70
    sprite('yo403_18', 3)	# 71-73
    sprite('yo403_19', 3)	# 74-76
    sprite('yo403_20', 3)	# 77-79
    label(3)
    sprite('yo020_07', 3)	# 80-82
    sprite('yo020_08', 3)	# 83-85
    loopRest()
    gotoLabel(3)
    label(9)
    sprite('yo231_00', 1)	# 86-86
    sprite('yo231_01', 2)	# 87-88
    sprite('yo231_00', 1)	# 89-89

@State
def KakeagariB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(80)
        AttackP2(75)
        Unknown11092(1)
        Hitstop(0)
        Unknown11001(8, 8, 8)
        Unknown9310(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9154(20)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(-20000)
        PushbackX(8000)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1084(1)
            Unknown23027()
            callSubroutine('Kakeagari_DeriveInput')
            sendToLabel(1)

        def upon_3():
            if SLOT_51:
                if (SLOT_19 < 300000):
                    clearUponHandler(3)
                    sendToLabel(0)
                    SLOT_51 = 0

        def upon_LANDING():
            callSubroutine('Kakeagari_DeriveClear')
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            Unknown18009(1)
            sendToLabel(9)
        callSubroutine('DoNotBeginCancel')
    sprite('yo403_00', 3)	# 1-3
    sprite('yo403_01', 8)	# 4-11
    sprite('yo403_02', 3)	# 12-14
    Unknown7007('70796f3230375f3000000000000000006400000070796f3230375f3100000000000000006400000070796f3230375f3200000000000000006400000070796f3230385f30000000000000000064000000')
    physicsXImpulse(49000)
    SFX_3('runjump_stone_light')
    sprite('yo403_03', 2)	# 15-16
    SFX_3('airdash_m')
    sprite('yo403_04', 2)	# 17-18
    SLOT_51 = 1
    sprite('yo403_05', 2)	# 19-20
    sprite('yo403_06', 2)	# 21-22
    sprite('yo403_03', 2)	# 23-24
    SFX_3('runjump_stone_light')
    sprite('yo403_04', 2)	# 25-26
    sprite('yo403_05', 2)	# 27-28
    sprite('yo403_06', 2)	# 29-30
    sprite('yo403_03', 2)	# 31-32
    label(2)
    sprite('yo403_21', 2)	# 33-34
    SLOT_51 = 0
    Unknown1019(30)
    Recovery()
    sprite('yo403_22', 4)	# 35-38
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_23', 4)	# 39-42
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_24', 4)	# 43-46
    Unknown1019(50)
    sprite('yo403_25', 4)	# 47-50
    Unknown1019(0)
    loopRest()
    ExitState()
    label(0)
    sprite('yo403_07', 2)	# 51-52
    sprite('yo403_08', 3)	# 53-55	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('yo403_08', 2)	# 56-57	 **attackbox here**
    sprite('yo403_09', 2)	# 58-59	 **attackbox here**
    sprite('yo403_10', 2)	# 60-61
    physicsXImpulse(10000)
    physicsYImpulse(20000)
    setGravity(4500)
    sprite('yo403_11', 2)	# 62-63
    sprite('yo403_12', 2)	# 64-65	 **attackbox here**
    Unknown2015(40)
    Unknown1084(1)
    sprite('yo403_13', 3)	# 66-68	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(36000)
    Hitstop(9)
    Unknown9310(-1)
    sprite('yo403_14', 3)	# 69-71	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2015(-1)
    sprite('yo403_15', 6)	# 72-77
    Unknown1007(50000)
    physicsXImpulse(-5000)
    physicsYImpulse(32000)
    setGravity(2400)
    sprite('yo403_16', 6)	# 78-83
    clearUponHandler(3)
    callSubroutine('Kakeagari_DeriveTiming')
    sprite('yo403_17', 6)	# 84-89
    sprite('yo403_18', 4)	# 90-93
    sprite('yo403_19', 4)	# 94-97
    sprite('yo403_20', 4)	# 98-101
    label(3)
    sprite('yo020_07', 3)	# 102-104
    sprite('yo020_08', 3)	# 105-107
    loopRest()
    gotoLabel(3)
    label(9)
    sprite('yo231_00', 3)	# 108-110
    sprite('yo231_01', 7)	# 111-117
    sprite('yo231_00', 3)	# 118-120

@State
def KakeagariEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(0)
        Unknown11001(8, 8, 8)
        Unknown9310(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9154(20)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(-20000)
        PushbackX(8000)
        Unknown11084(1)
        Unknown30065(0)
        Unknown11091(10)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1084(1)
            Unknown23027()
            callSubroutine('Kakeagari_DeriveInput')
            sendToLabel(1)

        def upon_3():
            if SLOT_51:
                if (SLOT_19 < 300000):
                    clearUponHandler(3)
                    sendToLabel(0)
                    SLOT_51 = 0

        def upon_LANDING():
            callSubroutine('Kakeagari_DeriveClear')
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            Unknown18009(1)
            sendToLabel(9)
        callSubroutine('DoNotBeginCancel')
    sprite('yo403_00', 3)	# 1-3
    sprite('yo403_01', 8)	# 4-11
    Unknown23125('')
    Unknown2058(-5000)
    sprite('yo403_02', 3)	# 12-14
    Unknown7007('70796f3230375f3000000000000000006400000070796f3230375f3100000000000000006400000070796f3230375f3200000000000000006400000070796f3230385f30000000000000000064000000')
    physicsXImpulse(58800)
    SFX_3('runjump_stone_light')
    sprite('yo403_03', 2)	# 15-16
    SFX_3('airdash_m')
    sprite('yo403_04', 2)	# 17-18
    SLOT_51 = 1
    sprite('yo403_05', 2)	# 19-20
    sprite('yo403_06', 2)	# 21-22
    sprite('yo403_03', 2)	# 23-24
    SFX_3('runjump_stone_light')
    sprite('yo403_04', 2)	# 25-26
    sprite('yo403_05', 2)	# 27-28
    sprite('yo403_06', 2)	# 29-30
    sprite('yo403_03', 2)	# 31-32
    label(2)
    sprite('yo403_21', 2)	# 33-34
    SLOT_51 = 0
    Unknown1019(30)
    Recovery()
    sprite('yo403_22', 4)	# 35-38
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_23', 4)	# 39-42
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_24', 4)	# 43-46
    Unknown1019(50)
    sprite('yo403_25', 4)	# 47-50
    Unknown1019(0)
    loopRest()
    ExitState()
    label(0)
    sprite('yo403_07', 2)	# 51-52
    sprite('yo403_08', 3)	# 53-55	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('yo403_08', 2)	# 56-57	 **attackbox here**
    sprite('yo403_09', 2)	# 58-59	 **attackbox here**
    sprite('yo403_10', 2)	# 60-61
    physicsXImpulse(10000)
    physicsYImpulse(20000)
    setGravity(4500)
    sprite('yo403_11', 2)	# 62-63
    sprite('yo403_12', 2)	# 64-65	 **attackbox here**
    Unknown2015(40)
    Unknown1084(1)
    sprite('yo403_13', 3)	# 66-68	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(36000)
    Hitstop(9)
    Unknown9310(-1)
    sprite('yo403_14', 3)	# 69-71	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2015(-1)
    sprite('yo403_15', 3)	# 72-74
    Unknown1007(50000)
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    setGravity(2400)
    sprite('yo403_16', 3)	# 75-77
    clearUponHandler(3)
    callSubroutine('Kakeagari_DeriveTiming')
    sprite('yo403_17', 3)	# 78-80
    sprite('yo403_18', 3)	# 81-83
    sprite('yo403_19', 3)	# 84-86
    sprite('yo403_20', 3)	# 87-89
    label(3)
    sprite('yo020_07', 3)	# 90-92
    sprite('yo020_08', 3)	# 93-95
    loopRest()
    gotoLabel(3)
    label(9)
    sprite('yo231_00', 3)	# 96-98
    sprite('yo231_01', 7)	# 99-105
    sprite('yo231_00', 3)	# 106-108

@State
def MoonsaltMove_Hasei():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('DoNotBeginCancel')
    sprite('keep', 1)	# 1-1
    if SLOT_38:
        enterState('MoonsaltMoveL')
    else:
        enterState('MoonsaltMoveR')

@State
def MoonsaltMoveR():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('DoNotBeginCancel')
    sprite('yo405_00', 3)	# 1-3
    sprite('yo405_01', 1)	# 4-4
    SFX_3('highjump_l')
    Unknown2008()
    if SLOT_112:
        Unknown2006()
    setInvincible(1)
    SLOT_60 = (SLOT_60 + 1)
    SLOT_5 = 0
    SLOT_6 = 1
    Unknown1084(1)
    physicsXImpulse(20000)
    physicsYImpulse(54000)
    setGravity(4000)
    Unknown22004(10, 1)
    Unknown2017(0)
    Unknown2015(40)
    sprite('yo405_01', 3)	# 5-7
    sprite('yo405_02', 4)	# 8-11
    Unknown2005()
    sprite('yo405_03', 4)	# 12-15
    setInvincible(0)
    callSubroutine('Moonsalt_DeriveInput')
    sprite('yo405_04', 4)	# 16-19
    sprite('yo405_04', 4)	# 20-23
    callSubroutine('Moonsalt_DeriveTiming')
    sprite('yo405_05', 3)	# 24-26
    sprite('yo405_06', 3)	# 27-29
    sprite('yo405_08', 3)	# 30-32
    sprite('yo405_09', 3)	# 33-35
    sprite('yo405_10', 3)	# 36-38
    sprite('yo405_11', 3)	# 39-41
    sprite('yo020_04', 3)	# 42-44
    sprite('yo020_05', 3)	# 45-47
    sprite('yo020_06', 3)	# 48-50
    label(0)
    sprite('yo020_07', 3)	# 51-53
    sprite('yo020_08', 3)	# 54-56
    gotoLabel(0)

@State
def MoonsaltMoveL():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('DoNotBeginCancel')
    sprite('yo405_00', 3)	# 1-3
    sprite('yo405_01', 1)	# 4-4
    SFX_3('highjump_l')
    Unknown2007()
    if SLOT_112:
        Unknown2006()
    setInvincible(1)
    SLOT_60 = (SLOT_60 + 1)
    SLOT_5 = 1
    SLOT_6 = 0
    Unknown1084(1)
    physicsXImpulse(20000)
    physicsYImpulse(54000)
    setGravity(4000)
    Unknown22004(10, 1)
    Unknown2017(0)
    Unknown2015(40)
    sprite('yo405_01', 3)	# 5-7
    sprite('yo405_02', 4)	# 8-11
    Unknown2005()
    sprite('yo405_03', 4)	# 12-15
    setInvincible(0)
    callSubroutine('Moonsalt_DeriveInput')
    sprite('yo405_04', 4)	# 16-19
    sprite('yo405_04', 4)	# 20-23
    callSubroutine('Moonsalt_DeriveTiming')
    sprite('yo405_05', 3)	# 24-26
    sprite('yo405_06', 3)	# 27-29
    sprite('yo405_08', 3)	# 30-32
    sprite('yo405_09', 3)	# 33-35
    sprite('yo405_10', 3)	# 36-38
    sprite('yo405_11', 3)	# 39-41
    sprite('yo020_04', 3)	# 42-44
    sprite('yo020_05', 3)	# 45-47
    sprite('yo020_06', 3)	# 48-50
    label(0)
    sprite('yo020_07', 3)	# 51-53
    sprite('yo020_08', 3)	# 54-56
    gotoLabel(0)

@State
def MoonsaltMove_Ex():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AirPushbackX(0)
        AirPushbackY(36000)
        AirUntechableTime(32)
        Hitstop(8)
        Unknown11001(0, 3, 3)
        PushbackX(8000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9016(1)
        HitOverhead(2)
        Unknown11032('c0270900102700000000000000000000')
        Unknown30055('f04902001e00000000000000')
        Unknown30065(0)
        Unknown11091(10)
        SLOT_60 = (SLOT_60 + 1)
        if (SLOT_60 == 3):
            AirPushbackX(20000)
            AirPushbackY(-60000)
            Unknown9310(1)
        HitOrBlockCancel('VSlash_R')
        HitOrBlockCancel('VSlash_L')
        HitOrBlockCancel('VSlash_Hasei')
        HitOrBlockCancel('VSlash_R_Hasei')
        HitOrBlockCancel('VSlash_L_Hasei')
        HitOrBlockCancel('MoonsaltMoveR')
        HitOrBlockCancel('MoonsaltMoveL')
        HitOrBlockCancel('MoonsaltMove_Hasei')
        HitOrBlockCancel('MoonsaltMoveR_Hasei')
        HitOrBlockCancel('MoonsaltMoveL_Hasei')
        HitOrBlockCancel('MoonsaltMove_Ex')
        HitOrBlockCancel('MoonsaltMove_Ex_Back')
        HitOrBlockCancel('MoonsaltMove_Ex_Hasei')

        def upon_11():
            Unknown1019(30)
            physicsYImpulse(8000)
            Unknown2037(1)

        def upon_12():
            SLOT_63 = (SLOT_63 + 1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        callSubroutine('DoNotBeginCancel')
        if (SLOT_60 == 2):
            Unknown23159('MoonsaltMove_Ex2')
        if (SLOT_60 == 3):
            Unknown23159('MoonsaltMove_Ex3')
    sprite('yo025_02', 3)	# 1-3
    Unknown2006()
    physicsXImpulse(0)
    Unknown1045(0)
    physicsYImpulse(40000)
    setGravity(3000)
    sprite('yo025_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    setInvincible(1)
    Unknown2005()
    sprite('yo405_00', 2)	# 5-6
    sprite('yo405_01', 2)	# 7-8
    sprite('yo405_02', 2)	# 9-10
    Unknown2005()
    sprite('yo405_03', 4)	# 11-14
    setInvincible(0)
    sprite('yo405_04', 3)	# 15-17
    sprite('yo405_05', 3)	# 18-20
    sprite('yo405_06', 1)	# 21-21
    sprite('yo405_06', 1)	# 22-22
    sprite('yo405_07', 8)	# 23-30	 **attackbox here**
    GFX_0('yoef_moonslash', 100)
    RefreshMultihit()
    sprite('yo405_08', 3)	# 31-33
    Recovery()
    sprite('yo405_09', 3)	# 34-36
    sprite('yo405_10', 3)	# 37-39
    sprite('yo405_11', 3)	# 40-42
    sprite('yo020_05', 3)	# 43-45
    sprite('yo020_06', 3)	# 46-48
    label(0)
    sprite('yo020_07', 3)	# 49-51
    sprite('yo020_08', 3)	# 52-54
    gotoLabel(0)
    label(9)
    sprite('yo231_00', 2)	# 55-56
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('yo231_01', 4)	# 57-60
    sprite('yo231_00', 3)	# 61-63

@State
def MoonsaltSlash():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AttackP1(80)
        AirPushbackX(0)
        AirPushbackY(44000)
        AirUntechableTime(32)
        Hitstop(8)
        Unknown11001(0, 3, 3)
        PushbackX(8000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9016(1)
        HitOverhead(2)
        Unknown11032('c0270900102700000000000000000000')
        Unknown30055('f04902001e00000000000000')
        if (SLOT_60 == 3):
            AirPushbackX(12000)
            AirPushbackY(-45000)
            Unknown9310(1)
        HitOrBlockCancel('VSlash_R')
        HitOrBlockCancel('VSlash_L')
        HitOrBlockCancel('VSlash_Hasei')
        HitOrBlockCancel('VSlash_R_Hasei')
        HitOrBlockCancel('VSlash_L_Hasei')
        HitOrBlockCancel('MoonsaltMoveR')
        HitOrBlockCancel('MoonsaltMoveL')
        HitOrBlockCancel('MoonsaltMove_Hasei')
        HitOrBlockCancel('MoonsaltMoveR_Hasei')
        HitOrBlockCancel('MoonsaltMoveL_Hasei')
        HitOrBlockCancel('MoonsaltMove_Ex')
        HitOrBlockCancel('MoonsaltMove_Ex_Back')
        HitOrBlockCancel('MoonsaltMove_Ex_Hasei')

        def upon_11():
            Unknown1019(30)
            physicsYImpulse(8000)
            Unknown2037(1)

        def upon_12():
            SLOT_63 = (SLOT_63 + 1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        callSubroutine('DoNotBeginCancel')
        if (SLOT_60 == 2):
            Unknown23159('MoonsaltSlash2')
        if (SLOT_60 == 3):
            Unknown23159('MoonsaltSlash3')
    sprite('yo405_06', 4)	# 1-4
    Unknown2017(0)
    Unknown2015(40)
    Unknown1019(30)
    Unknown1043()
    sprite('yo405_07', 2)	# 5-6	 **attackbox here**
    GFX_0('yoef_moonslash', 100)
    RefreshMultihit()
    Unknown7007('70796f3231315f3000000000000000006400000070796f3231315f3100000000000000006400000070796f3231315f3200000000000000006400000070796f3231325f30000000000000000064000000')
    SFX_3('slash_knife_slow')
    Unknown2017(1)
    sprite('yo405_07', 6)	# 7-12	 **attackbox here**
    sprite('yo405_08', 3)	# 13-15
    Unknown23027()
    Recovery()
    sprite('yo405_09', 3)	# 16-18
    sprite('yo405_10', 3)	# 19-21
    sprite('yo405_11', 3)	# 22-24
    clearUponHandler(3)
    sprite('yo020_04', 3)	# 25-27
    Recovery()
    sprite('yo020_05', 3)	# 28-30
    sprite('yo020_06', 3)	# 31-33
    label(0)
    sprite('yo020_07', 3)	# 34-36
    sprite('yo020_08', 3)	# 37-39
    gotoLabel(0)
    label(9)
    sprite('yo231_00', 2)	# 40-41
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('yo231_01', 4)	# 42-45
    sprite('yo231_00', 3)	# 46-48

@State
def VSlash_Hasei():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('DoNotBeginCancel')
    sprite('keep', 1)	# 1-1
    if SLOT_38:
        enterState('VSlash_L')
    else:
        enterState('VSlash_R')

@State
def VSlash_R():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(80)
        Hitstop(6)
        Unknown11001(0, -1, -1)
        AirUntechableTime(40)
        AirPushbackX(25000)
        AirPushbackY(-78000)
        Unknown30055('f04902005000000000000000')
        Unknown30056('905f01005000000000000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        Unknown9118(50)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown23001(0, 0)
        Unknown23014()
        Unknown21005(1)
        sendToLabelUpon(2, 0)

        def upon_11():
            SLOT_52 = 1

        def upon_8():
            Unknown2006()
        SLOT_51 = SLOT_60
        SLOT_52 = 1
        callSubroutine('DoNotBeginCancel')
    sprite('yo407_00', 3)	# 1-3
    sprite('yo407_00', 1)	# 4-4
    SLOT_8 = 1
    sprite('yo407_01', 3)	# 5-7
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 431, 0)
    Unknown1084(1)
    Unknown2008()
    if SLOT_112:
        Unknown2006()
    sprite('yo407_02', 5)	# 8-12
    Unknown7007('70796f3231355f3000000000000000006400000070796f3231355f3100000000000000006400000070796f3231355f3200000000000000006400000070796f3231365f30000000000000000064000000')
    SFX_3('airdash_m')
    SFX_3('slash_rapier_middle')
    sprite('yo407_03', 1)	# 13-13	 **attackbox here**
    sprite('yo407_03', 3)	# 14-16	 **attackbox here**
    SFX_3('slash_blade_slow')
    physicsXImpulse(50000)
    physicsYImpulse(-95000)
    sprite('yo407_04', 3)	# 17-19	 **attackbox here**
    sprite('yo407_05', 3)	# 20-22	 **attackbox here**
    label(1)
    sprite('yo407_03', 3)	# 23-25	 **attackbox here**
    sprite('yo407_04', 3)	# 26-28	 **attackbox here**
    sprite('yo407_05', 3)	# 29-31	 **attackbox here**
    gotoLabel(1)
    label(0)
    sprite('yo407_06', 4)	# 32-35
    clearUponHandler(2)
    Unknown8004(100, 1, 1)
    Unknown8000(-1, 1, 1)
    Unknown1084(1)
    GFX_0('V-Slasher', 100)
    SLOT_60 = SLOT_51
    SLOT_8 = SLOT_52
    sprite('yo231_00', 3)	# 36-38
    sprite('yo231_01', 3)	# 39-41
    SFX_3('slash_rapier_middle')
    sprite('yo407_10', 1)	# 42-42	 **attackbox here**
    AirUntechableTime(60)
    AirPushbackX(0)
    AirPushbackY(30000)
    Unknown30055('a08601005000000000000000')
    Unknown30056('a08601005000000000000000')
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown9190(0)
    Unknown9016(1)
    if SLOT_52:
        physicsXImpulse(60000)
        physicsYImpulse(85000)
        Unknown2017(0)
        Unknown2015(99)
    else:
        physicsXImpulse(60000)
        physicsYImpulse(80000)
    Unknown22001(-1)
    Unknown22003(-1)
    RefreshMultihit()
    sprite('yo407_11', 4)	# 43-46	 **attackbox here**
    Unknown1019(60)
    YAccel(60)
    sprite('yo407_12', 4)	# 47-50
    Unknown23027()
    Recovery()
    Unknown1019(60)
    YAccel(60)
    sprite('yo407_13', 4)	# 51-54
    Unknown1019(60)
    YAccel(60)
    sprite('yo407_13', 1)	# 55-55
    Unknown2017(1)
    Unknown2015(-1)
    sprite('yo407_13', 6)	# 56-61
    Unknown1019(40)
    YAccel(40)
    sprite('yo407_14', 5)	# 62-66
    setGravity(2600)
    sprite('yo407_14', 5)	# 67-71

@State
def VSlash_L():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(80)
        Hitstop(6)
        Unknown11001(0, -1, -1)
        AirUntechableTime(40)
        AirPushbackX(25000)
        AirPushbackY(-78000)
        Unknown30055('f04902005000000000000000')
        Unknown30056('905f01005000000000000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        Unknown9118(50)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown23001(0, 0)
        Unknown23014()
        Unknown21005(1)
        sendToLabelUpon(2, 0)

        def upon_11():
            SLOT_52 = 1

        def upon_8():
            Unknown2006()
        SLOT_51 = SLOT_60
        SLOT_52 = 1
        callSubroutine('DoNotBeginCancel')
    sprite('yo407_00', 3)	# 1-3
    sprite('yo407_00', 1)	# 4-4
    SLOT_8 = 1
    sprite('yo407_01', 3)	# 5-7
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 431, 0)
    Unknown1084(1)
    Unknown2007()
    if SLOT_112:
        Unknown2006()
    sprite('yo407_02', 5)	# 8-12
    Unknown7007('70796f3231355f3000000000000000006400000070796f3231355f3100000000000000006400000070796f3231355f3200000000000000006400000070796f3231365f30000000000000000064000000')
    SFX_3('airdash_m')
    SFX_3('slash_rapier_middle')
    sprite('yo407_03', 1)	# 13-13	 **attackbox here**
    sprite('yo407_03', 3)	# 14-16	 **attackbox here**
    SFX_3('slash_blade_slow')
    physicsXImpulse(50000)
    physicsYImpulse(-95000)
    sprite('yo407_04', 3)	# 17-19	 **attackbox here**
    sprite('yo407_05', 3)	# 20-22	 **attackbox here**
    label(1)
    sprite('yo407_03', 3)	# 23-25	 **attackbox here**
    sprite('yo407_04', 3)	# 26-28	 **attackbox here**
    sprite('yo407_05', 3)	# 29-31	 **attackbox here**
    gotoLabel(1)
    label(0)
    sprite('yo407_06', 4)	# 32-35
    clearUponHandler(2)
    Unknown8004(100, 1, 1)
    Unknown8000(-1, 1, 1)
    Unknown1084(1)
    GFX_0('V-Slasher', 100)
    SLOT_60 = SLOT_51
    SLOT_8 = SLOT_52
    sprite('yo231_00', 3)	# 36-38
    sprite('yo231_01', 3)	# 39-41
    SFX_3('slash_rapier_middle')
    sprite('yo407_10', 1)	# 42-42	 **attackbox here**
    AirUntechableTime(60)
    AirPushbackX(0)
    AirPushbackY(30000)
    Unknown30055('a08601005000000000000000')
    Unknown30056('a08601005000000000000000')
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown9190(0)
    Unknown9016(1)
    if SLOT_52:
        physicsXImpulse(60000)
        physicsYImpulse(85000)
        Unknown2017(0)
        Unknown2015(99)
    else:
        physicsXImpulse(60000)
        physicsYImpulse(80000)
    Unknown22001(-1)
    Unknown22003(-1)
    RefreshMultihit()
    sprite('yo407_11', 4)	# 43-46	 **attackbox here**
    Unknown1019(60)
    YAccel(60)
    sprite('yo407_12', 4)	# 47-50
    Unknown23027()
    Recovery()
    Unknown1019(60)
    YAccel(60)
    sprite('yo407_13', 4)	# 51-54
    Unknown1019(60)
    YAccel(60)
    sprite('yo407_13', 1)	# 55-55
    Unknown2017(1)
    Unknown2015(-1)
    sprite('yo407_13', 6)	# 56-61
    Unknown1019(40)
    YAccel(40)
    sprite('yo407_14', 5)	# 62-66
    setGravity(2600)
    sprite('yo407_14', 5)	# 67-71

@State
def UltimateTatsumaki():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        sendToLabelUpon(2, 6)

        def upon_3():
            if (SLOT_23 >= 2600000):
                teleportRelativeY(2600000)
            if SLOT_51:
                Unknown1019(97)
                YAccel(97)
                if (SLOT_23 < 50000):
                    teleportRelativeY(50000)
                    physicsYImpulse(0)
                SLOT_67 = SLOT_40
                if (SLOT_40 > 100):
                    SLOT_67 = (SLOT_67 / 1024)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                if (SLOT_40 < (-100)):
                    SLOT_67 = (SLOT_67 / 1024)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                SLOT_67 = SLOT_41
                if (SLOT_41 > 100):
                    SLOT_67 = (SLOT_67 / 1024)
                    SLOT_13 = (SLOT_13 + SLOT_67)
                if (SLOT_41 < (-100)):
                    SLOT_67 = (SLOT_67 / 1024)
                    SLOT_13 = (SLOT_13 + SLOT_67)
        if SLOT_36:
            Unknown23159('AirUltimateTatsumaki')
    sprite('yo431_00', 4)	# 1-4
    Unknown1084(1)
    physicsYImpulse(10000)
    physicsXImpulse(1000)
    setGravity(100)
    setInvincible(1)
    sprite('yo431_01', 4)	# 5-8
    YAccel(70)
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(60000)
    physicsYImpulse(-1500)
    Unknown35()
    sprite('yo431_02', 4)	# 9-12
    YAccel(70)
    Unknown2036(53, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pyo252_0', 'pyo252_1', '', '')
    sprite('yo431_03', 4)	# 13-16
    YAccel(70)
    sprite('yo431_04', 4)	# 17-20
    YAccel(70)
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('yo431_05', 4)	# 21-24
    Unknown23029(11, 501, 0)
    YAccel(70)
    YAccel(0)
    Unknown1019(0)
    setGravity(0)
    sprite('yo431_06', 3)	# 25-27
    sprite('yo431_07', 3)	# 28-30
    sprite('yo431_06', 3)	# 31-33
    sprite('yo431_07', 3)	# 34-36
    sprite('yo431_06', 3)	# 37-39
    sprite('yo431_07', 3)	# 40-42
    sprite('yo431_06', 3)	# 43-45
    sprite('yo431_07', 3)	# 46-48
    sprite('yo431_06', 3)	# 49-51
    sprite('yo431_07', 3)	# 52-54
    sprite('yo431_06', 3)	# 55-57
    sprite('yo431_07', 3)	# 58-60
    sprite('yo431_11', 5)	# 61-65
    SLOT_51 = 1
    setGravity(100)
    sprite('yo431_08', 5)	# 66-70
    sprite('yo431_09', 5)	# 71-75
    setInvincible(0)
    sprite('yo431_10', 4)	# 76-79
    tag_voice(0, 'pyo253_0', 'pyo253_1', '', '')
    sprite('yo431_11', 3)	# 80-82
    sprite('yo431_08', 1)	# 83-83
    sprite('yo431_09', 1)	# 84-84
    sprite('yo431_10', 1)	# 85-85
    sprite('yo431_11', 1)	# 86-86
    sprite('yo431_08', 1)	# 87-87
    sprite('yo431_09', 1)	# 88-88
    sprite('yo431_10', 1)	# 89-89
    sprite('yo431_11', 1)	# 90-90
    sprite('yo431_08', 1)	# 91-91
    sprite('yo431_09', 1)	# 92-92
    sprite('yo431_10', 1)	# 93-93
    sprite('yo431_11', 1)	# 94-94
    sprite('yo431_08', 1)	# 95-95
    sprite('yo431_09', 1)	# 96-96
    sprite('yo431_10', 1)	# 97-97
    sprite('yo431_11', 1)	# 98-98
    sprite('yo431_08', 1)	# 99-99
    sprite('yo431_09', 1)	# 100-100
    sprite('yo431_10', 1)	# 101-101
    sprite('yo431_11', 1)	# 102-102
    sprite('yo431_08', 1)	# 103-103
    sprite('yo431_09', 1)	# 104-104
    sprite('yo431_10', 1)	# 105-105
    sprite('yo431_11', 1)	# 106-106
    sprite('yo431_08', 1)	# 107-107
    sprite('yo431_09', 1)	# 108-108
    sprite('yo431_10', 1)	# 109-109
    sprite('yo431_11', 1)	# 110-110
    sprite('yo431_08', 1)	# 111-111
    sprite('yo431_09', 1)	# 112-112
    sprite('yo431_10', 1)	# 113-113
    sprite('yo431_11', 1)	# 114-114
    sprite('yo431_08', 1)	# 115-115
    sprite('yo431_09', 1)	# 116-116
    sprite('yo431_10', 1)	# 117-117
    sprite('yo431_11', 1)	# 118-118
    sprite('yo431_08', 1)	# 119-119
    sprite('yo431_09', 1)	# 120-120
    sprite('yo431_10', 1)	# 121-121
    sprite('yo431_11', 1)	# 122-122
    sprite('yo431_08', 1)	# 123-123
    sprite('yo431_09', 1)	# 124-124
    sprite('yo431_10', 1)	# 125-125
    sprite('yo431_11', 1)	# 126-126
    sprite('yo431_08', 1)	# 127-127
    sprite('yo431_09', 1)	# 128-128
    sprite('yo431_10', 1)	# 129-129
    sprite('yo431_11', 1)	# 130-130
    sprite('yo431_08', 1)	# 131-131
    sprite('yo431_09', 1)	# 132-132
    sprite('yo431_10', 1)	# 133-133
    sprite('yo431_11', 1)	# 134-134
    sprite('yo431_08', 1)	# 135-135
    sprite('yo431_09', 1)	# 136-136
    sprite('yo431_10', 1)	# 137-137
    sprite('yo431_11', 1)	# 138-138
    sprite('yo431_08', 1)	# 139-139
    sprite('yo431_09', 1)	# 140-140
    sprite('yo431_10', 1)	# 141-141
    sprite('yo431_11', 1)	# 142-142
    sprite('yo431_08', 2)	# 143-144
    sprite('yo431_09', 2)	# 145-146
    sprite('yo431_10', 2)	# 147-148
    sprite('yo431_11', 2)	# 149-150
    sprite('yo431_08', 2)	# 151-152
    sprite('yo431_09', 2)	# 153-154
    sprite('yo431_10', 2)	# 155-156
    sprite('yo431_11', 2)	# 157-158
    sprite('yo431_08', 2)	# 159-160
    sprite('yo431_09', 2)	# 161-162
    sprite('yo431_10', 2)	# 163-164
    sprite('yo431_11', 2)	# 165-166
    sprite('yo431_08', 2)	# 167-168
    sprite('yo431_09', 2)	# 169-170
    sprite('yo431_10', 2)	# 171-172
    sprite('yo431_11', 2)	# 173-174
    sprite('yo431_08', 2)	# 175-176
    sprite('yo431_09', 2)	# 177-178
    sprite('yo431_10', 2)	# 179-180
    sprite('yo431_11', 2)	# 181-182
    sprite('yo431_08', 2)	# 183-184
    sprite('yo431_09', 2)	# 185-186
    sprite('yo431_10', 2)	# 187-188
    sprite('yo431_11', 2)	# 189-190
    sprite('yo431_08', 2)	# 191-192
    sprite('yo431_09', 2)	# 193-194
    sprite('yo431_10', 2)	# 195-196
    sprite('yo431_11', 2)	# 197-198
    sprite('yo431_08', 2)	# 199-200
    sprite('yo431_09', 2)	# 201-202
    sprite('yo431_10', 2)	# 203-204
    sprite('yo431_11', 2)	# 205-206
    sprite('yo431_08', 2)	# 207-208
    sprite('yo431_09', 2)	# 209-210
    sprite('yo431_10', 2)	# 211-212
    sprite('yo431_11', 2)	# 213-214
    loopRest()
    SLOT_51 = 0
    setGravity(2000)
    Unknown1019(70)
    Unknown1021(5000)
    Unknown21012('54617473756d616b69000000000000000000000000000000000000000000000020000000')
    sprite('yo431_08', 3)	# 215-217
    GFX_0('TatsumakiYoin', 103)
    Unknown38(6, 1)
    sprite('yo431_09', 3)	# 218-220
    sprite('yo431_10', 3)	# 221-223
    sprite('yo431_11', 3)	# 224-226
    label(0)
    sprite('yo431_08', 4)	# 227-230
    sprite('yo431_09', 4)	# 231-234
    sprite('yo431_10', 4)	# 235-238
    sprite('yo431_11', 4)	# 239-242
    loopRest()
    gotoLabel(0)
    label(6)
    SLOT_51 = 0
    physicsXImpulse(1000)
    sprite('yo431_09', 4)	# 243-246
    Unknown23029(1, 5001, 0)
    sprite('yo431_10', 4)	# 247-250
    sprite('yo431_12', 4)	# 251-254
    Unknown1019(70)
    sprite('yo431_13', 4)	# 255-258
    sprite('yo431_14', 4)	# 259-262
    Unknown1019(0)
    sprite('yo431_15', 10)	# 263-272
    sprite('yo431_16', 4)	# 273-276
    sprite('yo431_17', 4)	# 277-280

@State
def UltimateTatsumakiOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        sendToLabelUpon(2, 6)

        def upon_3():
            if (SLOT_23 >= 2600000):
                teleportRelativeY(2600000)
            if SLOT_51:
                Unknown1019(97)
                YAccel(97)
                if (SLOT_23 < 50000):
                    teleportRelativeY(50000)
                    physicsYImpulse(0)
                SLOT_67 = SLOT_40
                if (SLOT_40 > 100):
                    SLOT_67 = (SLOT_67 / 640)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                if (SLOT_40 < (-100)):
                    SLOT_67 = (SLOT_67 / 640)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                SLOT_67 = SLOT_41
                if (SLOT_41 > 100):
                    SLOT_67 = (SLOT_67 / 640)
                    SLOT_13 = (SLOT_13 + SLOT_67)
                if (SLOT_41 < (-100)):
                    SLOT_67 = (SLOT_67 / 640)
                    SLOT_13 = (SLOT_13 + SLOT_67)
        if SLOT_36:
            Unknown23159('AirUltimateTatsumakiOD')
    sprite('yo431_00', 4)	# 1-4
    Unknown1084(1)
    physicsYImpulse(10000)
    physicsXImpulse(1000)
    setGravity(100)
    setInvincible(1)
    sprite('yo431_01', 4)	# 5-8
    YAccel(70)
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(60000)
    physicsYImpulse(-1500)
    Unknown35()
    sprite('yo431_02', 4)	# 9-12
    YAccel(70)
    Unknown2036(53, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pyo252_0', 'pyo252_1', '', '')
    sprite('yo431_03', 4)	# 13-16
    YAccel(70)
    sprite('yo431_04', 4)	# 17-20
    YAccel(70)
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('yo431_05', 4)	# 21-24
    Unknown23029(11, 502, 0)
    YAccel(70)
    YAccel(0)
    Unknown1019(0)
    setGravity(0)
    sprite('yo431_06', 3)	# 25-27
    sprite('yo431_07', 3)	# 28-30
    sprite('yo431_06', 3)	# 31-33
    sprite('yo431_07', 3)	# 34-36
    sprite('yo431_06', 3)	# 37-39
    sprite('yo431_07', 3)	# 40-42
    sprite('yo431_06', 3)	# 43-45
    sprite('yo431_07', 3)	# 46-48
    sprite('yo431_06', 3)	# 49-51
    sprite('yo431_07', 3)	# 52-54
    sprite('yo431_06', 3)	# 55-57
    sprite('yo431_07', 3)	# 58-60
    sprite('yo431_11', 5)	# 61-65
    SLOT_51 = 1
    setGravity(100)
    sprite('yo431_08', 5)	# 66-70
    sprite('yo431_09', 5)	# 71-75
    setInvincible(0)
    sprite('yo431_10', 4)	# 76-79
    tag_voice(0, 'pyo253_0', 'pyo253_1', '', '')
    sprite('yo431_11', 3)	# 80-82
    sprite('yo431_08', 1)	# 83-83
    sprite('yo431_09', 1)	# 84-84
    sprite('yo431_10', 1)	# 85-85
    sprite('yo431_11', 1)	# 86-86
    sprite('yo431_08', 1)	# 87-87
    sprite('yo431_09', 1)	# 88-88
    sprite('yo431_10', 1)	# 89-89
    sprite('yo431_11', 1)	# 90-90
    sprite('yo431_08', 1)	# 91-91
    sprite('yo431_09', 1)	# 92-92
    sprite('yo431_10', 1)	# 93-93
    sprite('yo431_11', 1)	# 94-94
    sprite('yo431_08', 1)	# 95-95
    sprite('yo431_09', 1)	# 96-96
    sprite('yo431_10', 1)	# 97-97
    sprite('yo431_11', 1)	# 98-98
    sprite('yo431_08', 1)	# 99-99
    sprite('yo431_09', 1)	# 100-100
    sprite('yo431_10', 1)	# 101-101
    sprite('yo431_11', 1)	# 102-102
    sprite('yo431_08', 1)	# 103-103
    sprite('yo431_09', 1)	# 104-104
    sprite('yo431_10', 1)	# 105-105
    sprite('yo431_11', 1)	# 106-106
    sprite('yo431_08', 1)	# 107-107
    sprite('yo431_09', 1)	# 108-108
    sprite('yo431_10', 1)	# 109-109
    sprite('yo431_11', 1)	# 110-110
    sprite('yo431_08', 1)	# 111-111
    sprite('yo431_09', 1)	# 112-112
    sprite('yo431_10', 1)	# 113-113
    sprite('yo431_11', 1)	# 114-114
    sprite('yo431_08', 1)	# 115-115
    sprite('yo431_09', 1)	# 116-116
    sprite('yo431_10', 1)	# 117-117
    sprite('yo431_11', 1)	# 118-118
    sprite('yo431_08', 1)	# 119-119
    sprite('yo431_09', 1)	# 120-120
    sprite('yo431_10', 1)	# 121-121
    sprite('yo431_11', 1)	# 122-122
    sprite('yo431_08', 1)	# 123-123
    sprite('yo431_09', 1)	# 124-124
    sprite('yo431_10', 1)	# 125-125
    sprite('yo431_11', 1)	# 126-126
    sprite('yo431_08', 1)	# 127-127
    sprite('yo431_09', 1)	# 128-128
    sprite('yo431_10', 1)	# 129-129
    sprite('yo431_11', 1)	# 130-130
    sprite('yo431_08', 1)	# 131-131
    sprite('yo431_09', 1)	# 132-132
    sprite('yo431_10', 1)	# 133-133
    sprite('yo431_11', 1)	# 134-134
    sprite('yo431_08', 1)	# 135-135
    sprite('yo431_09', 1)	# 136-136
    sprite('yo431_10', 1)	# 137-137
    sprite('yo431_11', 1)	# 138-138
    sprite('yo431_08', 1)	# 139-139
    sprite('yo431_09', 1)	# 140-140
    sprite('yo431_10', 1)	# 141-141
    sprite('yo431_11', 1)	# 142-142
    sprite('yo431_08', 2)	# 143-144
    sprite('yo431_09', 2)	# 145-146
    sprite('yo431_10', 2)	# 147-148
    sprite('yo431_11', 2)	# 149-150
    sprite('yo431_08', 2)	# 151-152
    sprite('yo431_09', 2)	# 153-154
    sprite('yo431_10', 2)	# 155-156
    sprite('yo431_11', 2)	# 157-158
    sprite('yo431_08', 2)	# 159-160
    sprite('yo431_09', 2)	# 161-162
    sprite('yo431_10', 2)	# 163-164
    sprite('yo431_11', 2)	# 165-166
    sprite('yo431_08', 2)	# 167-168
    sprite('yo431_09', 2)	# 169-170
    sprite('yo431_10', 2)	# 171-172
    sprite('yo431_11', 2)	# 173-174
    sprite('yo431_08', 2)	# 175-176
    sprite('yo431_09', 2)	# 177-178
    sprite('yo431_10', 2)	# 179-180
    sprite('yo431_11', 2)	# 181-182
    sprite('yo431_08', 2)	# 183-184
    sprite('yo431_09', 2)	# 185-186
    sprite('yo431_10', 2)	# 187-188
    sprite('yo431_11', 2)	# 189-190
    sprite('yo431_08', 2)	# 191-192
    sprite('yo431_09', 2)	# 193-194
    sprite('yo431_10', 2)	# 195-196
    sprite('yo431_11', 2)	# 197-198
    sprite('yo431_08', 2)	# 199-200
    sprite('yo431_09', 2)	# 201-202
    sprite('yo431_10', 2)	# 203-204
    sprite('yo431_11', 2)	# 205-206
    sprite('yo431_08', 2)	# 207-208
    sprite('yo431_09', 2)	# 209-210
    sprite('yo431_10', 2)	# 211-212
    sprite('yo431_11', 2)	# 213-214
    loopRest()
    SLOT_51 = 0
    setGravity(2000)
    Unknown1019(70)
    Unknown1021(5000)
    Unknown21012('54617473756d616b694f4400000000000000000000000000000000000000000020000000')
    sprite('yo431_08', 3)	# 215-217
    GFX_0('TatsumakiYoin', 103)
    Unknown38(6, 1)
    sprite('yo431_09', 3)	# 218-220
    sprite('yo431_10', 3)	# 221-223
    sprite('yo431_11', 3)	# 224-226
    label(0)
    sprite('yo431_08', 4)	# 227-230
    sprite('yo431_09', 4)	# 231-234
    sprite('yo431_10', 4)	# 235-238
    sprite('yo431_11', 4)	# 239-242
    loopRest()
    gotoLabel(0)
    label(6)
    SLOT_51 = 0
    physicsXImpulse(1000)
    sprite('yo431_09', 4)	# 243-246
    Unknown23029(1, 5001, 0)
    sprite('yo431_10', 4)	# 247-250
    sprite('yo431_12', 4)	# 251-254
    Unknown1019(70)
    sprite('yo431_13', 4)	# 255-258
    sprite('yo431_14', 4)	# 259-262
    Unknown1019(0)
    sprite('yo431_15', 10)	# 263-272
    sprite('yo431_16', 4)	# 273-276
    sprite('yo431_17', 4)	# 277-280

@State
def UltimateKunai():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        AttackP2(100)
        Hitstop(20)
        AirUntechableTime(120)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(36000)
        Unknown30055('f04902005000000000000000')
        Unknown11056(2)
        Unknown11068(1)
        Unknown11084(1)
        Unknown11064(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11069('UltimateKunaiExe')

        def upon_78():
            clearUponHandler(11)
            Unknown13024(0)
            Unknown23024(2)
            Unknown23025(1)
            enterState('UltimateKunaiExe')
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        Unknown1084(1)
        setInvincible(1)
        if SLOT_36:
            Unknown23159('AirUltimateKunai')
    sprite('yo432_00', 3)	# 1-3
    sprite('yo432_01', 1)	# 4-4
    physicsYImpulse(1000)
    setGravity(-100)
    sprite('yo432_02', 36)	# 5-40
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pyo254_0', 'pyo254_1', '', '')
    Unknown1084(1)
    YAccel(0)
    setGravity(0)
    sprite('yo432_03', 3)	# 41-43	 **attackbox here**
    StartMultihit()
    physicsXImpulse(60000)
    Unknown1028(-2000)
    physicsYImpulse(26000)
    setGravity(2000)
    SFX_3('airdash_m')
    sprite('yo432_04', 3)	# 44-46	 **attackbox here**
    sprite('yo432_03', 3)	# 47-49	 **attackbox here**
    sprite('yo432_04', 3)	# 50-52	 **attackbox here**
    sprite('yo432_03', 3)	# 53-55	 **attackbox here**
    sprite('yo432_04', 3)	# 56-58	 **attackbox here**
    Unknown1019(60)
    Unknown1034(0)
    sprite('yo432_20', 4)	# 59-62
    setInvincible(0)
    Unknown1019(60)
    sprite('yo432_21', 4)	# 63-66
    Unknown1019(60)
    sprite('yo432_22', 4)	# 67-70
    Unknown1019(60)
    label(2)
    sprite('yo020_07', 4)	# 71-74
    sprite('yo020_08', 4)	# 75-78
    gotoLabel(2)
    label(9)
    sprite('yo231_00', 2)	# 79-80
    Unknown1084(1)
    Unknown2006()
    sprite('yo231_01', 12)	# 81-92
    sprite('yo231_00', 4)	# 93-96

@State
def UltimateKunaiOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        AttackP2(100)
        Hitstop(20)
        AirUntechableTime(120)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(36000)
        Unknown30055('f04902005000000000000000')
        Unknown11056(2)
        Unknown11068(1)
        Unknown11084(1)
        Unknown11064(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11069('UltimateKunaiODExe')

        def upon_78():
            clearUponHandler(11)
            Unknown13024(0)
            Unknown23024(2)
            Unknown23025(1)
            enterState('UltimateKunaiODExe')
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        Unknown1084(1)
        setInvincible(1)
        if SLOT_36:
            Unknown23159('AirUltimateKunaiOD')
    sprite('yo432_00', 3)	# 1-3
    sprite('yo432_01', 1)	# 4-4
    physicsYImpulse(1000)
    setGravity(-100)
    sprite('yo432_02', 36)	# 5-40
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pyo254_0', 'pyo254_1', '', '')
    Unknown1084(1)
    YAccel(0)
    setGravity(0)
    sprite('yo432_03', 3)	# 41-43	 **attackbox here**
    StartMultihit()
    physicsXImpulse(60000)
    Unknown1028(-2000)
    physicsYImpulse(26000)
    setGravity(2000)
    SFX_3('airdash_m')
    sprite('yo432_04', 3)	# 44-46	 **attackbox here**
    sprite('yo432_03', 3)	# 47-49	 **attackbox here**
    sprite('yo432_04', 3)	# 50-52	 **attackbox here**
    sprite('yo432_03', 3)	# 53-55	 **attackbox here**
    sprite('yo432_04', 3)	# 56-58	 **attackbox here**
    Unknown1019(60)
    Unknown1034(0)
    sprite('yo432_20', 4)	# 59-62
    setInvincible(0)
    Unknown1019(60)
    sprite('yo432_21', 4)	# 63-66
    Unknown1019(60)
    sprite('yo432_22', 4)	# 67-70
    Unknown1019(60)
    label(2)
    sprite('yo020_07', 4)	# 71-74
    sprite('yo020_08', 4)	# 75-78
    gotoLabel(2)
    label(9)
    sprite('yo231_00', 2)	# 79-80
    Unknown1084(1)
    Unknown2006()
    sprite('yo231_01', 12)	# 81-92
    sprite('yo231_00', 4)	# 93-96

@State
def UltimateKunaiExe():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        AttackLevel_(5)
        AirUntechableTime(100)
        Hitstop(8)
        Unknown11001(0, 10, 10)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(8000)
        AirPushbackY(42000)
        YImpluseBeforeWallbounce(500)
        Unknown11023(1)
        Unknown11072(1, 110000, -50000)
        Unknown11056(2)
        Unknown11068(1)
        Unknown11084(1)
        Unknown11064(1)
        Unknown30048(1)
        Unknown13024(0)
        Unknown20000(1)

        def upon_3():
            if SLOT_56:
                op(4, 2, 18, 0, 5)
                if (SLOT_0 == 0):
                    GFX_0('KunaiZanzoh', 100)
        Unknown11069('ultimatekunai3')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(0)
    sprite('keep', 2)	# 1-2
    Unknown1034(50)
    setInvincible(1)
    sprite('yo432_05', 5)	# 3-7
    Unknown1084(1)
    sprite('yo432_06', 5)	# 8-12	 **attackbox here**
    RefreshMultihit()
    sprite('yo432_07', 2)	# 13-14	 **attackbox here**
    physicsXImpulse(-8000)
    physicsYImpulse(24000)
    setGravity(500)
    SLOT_56 = 1
    SFX_3('runjump_stone_light')
    sprite('yo432_07', 2)	# 15-16	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    sprite('yo432_07', 2)	# 17-18	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5204, 0)
    sprite('yo432_07', 2)	# 19-20	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5205, 0)
    sprite('yo432_07', 2)	# 21-22	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5206, 0)
    sprite('yo432_08', 2)	# 23-24
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5207, 0)
    sprite('yo432_08', 2)	# 25-26
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5208, 0)
    loopRest()
    sprite('yo432_08', 2)	# 27-28
    GFX_0('ultimatekunai3', 103)
    sprite('yo432_09', 2)	# 29-30
    Unknown1019(40)
    YAccel(40)
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5204, 0)
    sprite('yo432_09', 2)	# 31-32
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5205, 0)
    sprite('yo432_09', 2)	# 33-34
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5206, 0)
    sprite('yo432_09', 2)	# 35-36
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5207, 0)
    sprite('yo432_09', 2)	# 37-38
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5208, 0)
    sprite('yo432_09', 2)	# 39-40
    GFX_0('ultimatekunai3', 103)
    sprite('yo432_09', 2)	# 41-42
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5204, 0)
    sprite('yo432_10', 2)	# 43-44
    Unknown1019(40)
    YAccel(40)
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5205, 0)
    sprite('yo432_10', 2)	# 45-46
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5206, 0)
    sprite('yo432_10', 2)	# 47-48
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5207, 0)
    sprite('yo432_10', 2)	# 49-50
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5208, 0)
    loopRest()
    sprite('yo432_11', 4)	# 51-54
    YAccel(40)
    sprite('yo432_12', 4)	# 55-58
    Unknown21015('756c74696d6174656b756e6169330000000000000000000000000000000000005114000000000000')
    YAccel(40)
    sprite('yo432_13', 17)	# 59-75
    YAccel(50)
    Unknown1019(50)
    Unknown1039(50)
    sprite('yo432_14', 13)	# 76-88
    Unknown23029(11, 521, 0)
    SLOT_56 = 0
    YAccel(20)
    Unknown1019(20)
    Unknown1039(20)
    sprite('yo432_14', 15)	# 89-103
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(60000)
    physicsYImpulse(-1500)
    Unknown35()
    Unknown1084(1)
    Unknown2036(46, -1, 0)
    Unknown21015('756c74696d6174656b756e6169330000000000000000000000000000000000005214000000000000')
    sprite('yo432_14', 3)	# 104-106
    SFX_3('slash_knife_slow')
    sprite('yo432_14', 3)	# 107-109
    SFX_3('slash_knife_slow')
    sprite('yo432_14', 17)	# 110-126
    SFX_3('slash_knife_slow')
    sprite('yo432_15', 3)	# 127-129
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    tag_voice(0, 'pyo255_0', 'pyo255_1', '', '')
    sprite('yo432_16', 3)	# 130-132
    sprite('yo432_15', 3)	# 133-135
    Unknown20000(0)
    sprite('yo432_16', 3)	# 136-138
    sprite('yo432_15', 3)	# 139-141
    sprite('yo432_16', 3)	# 142-144
    sprite('yo432_15', 3)	# 145-147
    Unknown21015('756c74696d6174656b756e6169330000000000000000000000000000000000005314000000000000')
    sprite('yo432_16', 3)	# 148-150
    sprite('yo432_15', 3)	# 151-153
    sprite('yo432_16', 3)	# 154-156
    sprite('yo432_15', 3)	# 157-159
    Unknown13024(1)
    sprite('yo432_16', 3)	# 160-162
    sprite('yo432_15', 3)	# 163-165
    sprite('yo432_16', 3)	# 166-168
    sprite('yo432_15', 3)	# 169-171
    sprite('yo432_16', 3)	# 172-174
    sprite('yo432_15', 3)	# 175-177
    sprite('yo432_16', 3)	# 178-180
    sprite('yo432_15', 3)	# 181-183
    sprite('yo432_16', 3)	# 184-186
    sprite('yo432_15', 3)	# 187-189
    sprite('yo432_16', 3)	# 190-192
    sprite('yo432_17', 3)	# 193-195
    clearUponHandler(3)
    physicsYImpulse(12000)
    setGravity(3100)
    sprite('yo432_18', 3)	# 196-198
    sprite('yo432_19', 3)	# 199-201
    Unknown23025(0)
    label(14)
    sprite('yo020_07', 4)	# 202-205
    sprite('yo020_08', 4)	# 206-209
    gotoLabel(14)
    label(0)
    sprite('yo010_00', 3)	# 210-212
    sprite('yo000_00', 3)	# 213-215
    sprite('yo400_00', 3)	# 216-218
    sprite('yo400_01', 3)	# 219-221
    SFX_3('slash_knife_slow')
    sprite('yo400_02', 3)	# 222-224
    sprite('yo400_03', 3)	# 225-227
    sprite('yo400_00', 3)	# 228-230
    sprite('yo400_01', 3)	# 231-233
    SFX_3('slash_knife_slow')
    sprite('yo400_02', 3)	# 234-236
    sprite('yo400_03', 12)	# 237-248

@State
def UltimateKunaiODExe():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        AttackLevel_(5)
        AirUntechableTime(100)
        Hitstop(8)
        Unknown11001(0, 10, 10)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(8000)
        AirPushbackY(42000)
        YImpluseBeforeWallbounce(500)
        Unknown11023(1)
        Unknown11072(1, 110000, -50000)
        Unknown11056(2)
        Unknown11068(1)
        Unknown11084(1)
        Unknown11064(1)
        Unknown30048(1)
        Unknown13024(0)
        Unknown20000(1)

        def upon_3():
            if SLOT_56:
                op(4, 2, 18, 0, 5)
                if (SLOT_0 == 0):
                    GFX_0('KunaiZanzoh', 100)
        Unknown11069('ultimatekunai3')
        Unknown11091(20)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(0)
    sprite('keep', 2)	# 1-2
    Unknown1034(50)
    setInvincible(1)
    sprite('yo432_05', 5)	# 3-7
    Unknown1084(1)
    sprite('yo432_06', 5)	# 8-12	 **attackbox here**
    RefreshMultihit()
    sprite('yo432_07', 2)	# 13-14	 **attackbox here**
    physicsXImpulse(-8000)
    physicsYImpulse(24000)
    setGravity(500)
    SLOT_56 = 1
    SFX_3('runjump_stone_light')
    sprite('yo432_07', 1)	# 15-15	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    sprite('yo432_07', 1)	# 16-16	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5209, 0)
    sprite('yo432_07', 1)	# 17-17	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5204, 0)
    sprite('yo432_07', 1)	# 18-18	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5210, 0)
    sprite('yo432_07', 1)	# 19-19	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5205, 0)
    sprite('yo432_07', 1)	# 20-20	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5211, 0)
    sprite('yo432_07', 1)	# 21-21	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5206, 0)
    sprite('yo432_07', 1)	# 22-22	 **attackbox here**
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5212, 0)
    sprite('yo432_08', 1)	# 23-23
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5207, 0)
    sprite('yo432_08', 1)	# 24-24
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5213, 0)
    sprite('yo432_08', 1)	# 25-25
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5208, 0)
    sprite('yo432_08', 1)	# 26-26
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5214, 0)
    loopRest()
    sprite('yo432_08', 1)	# 27-27
    GFX_0('ultimatekunai3', 103)
    sprite('yo432_08', 1)	# 28-28
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5209, 0)
    sprite('yo432_09', 1)	# 29-29
    Unknown1019(40)
    YAccel(40)
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5204, 0)
    sprite('yo432_09', 1)	# 30-30
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5210, 0)
    sprite('yo432_09', 1)	# 31-31
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5205, 0)
    sprite('yo432_09', 1)	# 32-32
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5211, 0)
    sprite('yo432_09', 1)	# 33-33
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5206, 0)
    sprite('yo432_09', 1)	# 34-34
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5212, 0)
    sprite('yo432_09', 1)	# 35-35
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5207, 0)
    sprite('yo432_09', 1)	# 36-36
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5213, 0)
    sprite('yo432_09', 1)	# 37-37
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5208, 0)
    sprite('yo432_09', 1)	# 38-38
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5214, 0)
    sprite('yo432_09', 1)	# 39-39
    GFX_0('ultimatekunai3', 103)
    sprite('yo432_09', 1)	# 40-40
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5209, 0)
    sprite('yo432_09', 1)	# 41-41
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5204, 0)
    sprite('yo432_09', 1)	# 42-42
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5210, 0)
    sprite('yo432_10', 1)	# 43-43
    Unknown1019(40)
    YAccel(40)
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5205, 0)
    sprite('yo432_10', 1)	# 44-44
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5211, 0)
    sprite('yo432_10', 1)	# 45-45
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5206, 0)
    sprite('yo432_10', 1)	# 46-46
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5212, 0)
    sprite('yo432_10', 1)	# 47-47
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5207, 0)
    sprite('yo432_10', 1)	# 48-48
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5213, 0)
    sprite('yo432_10', 1)	# 49-49
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5208, 0)
    sprite('yo432_10', 1)	# 50-50
    GFX_0('ultimatekunai3', 103)
    Unknown23029(1, 5214, 0)
    loopRest()
    sprite('yo432_11', 4)	# 51-54
    YAccel(40)
    sprite('yo432_12', 4)	# 55-58
    Unknown21015('756c74696d6174656b756e6169330000000000000000000000000000000000005114000000000000')
    YAccel(40)
    sprite('yo432_13', 17)	# 59-75
    YAccel(50)
    Unknown1019(50)
    Unknown1039(50)
    sprite('yo432_14', 13)	# 76-88
    Unknown23029(11, 521, 0)
    SLOT_56 = 0
    YAccel(20)
    Unknown1019(20)
    Unknown1039(20)
    sprite('yo432_14', 15)	# 89-103
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(60000)
    physicsYImpulse(-1500)
    Unknown35()
    Unknown1084(1)
    Unknown2036(46, -1, 0)
    Unknown21015('756c74696d6174656b756e6169330000000000000000000000000000000000005214000000000000')
    sprite('yo432_14', 3)	# 104-106
    SFX_3('slash_knife_slow')
    sprite('yo432_14', 3)	# 107-109
    SFX_3('slash_knife_slow')
    sprite('yo432_14', 17)	# 110-126
    SFX_3('slash_knife_slow')
    sprite('yo432_15', 3)	# 127-129
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    tag_voice(0, 'pyo255_0', 'pyo255_1', '', '')
    sprite('yo432_16', 3)	# 130-132
    sprite('yo432_15', 3)	# 133-135
    Unknown20000(0)
    sprite('yo432_16', 3)	# 136-138
    sprite('yo432_15', 3)	# 139-141
    sprite('yo432_16', 3)	# 142-144
    sprite('yo432_15', 3)	# 145-147
    Unknown21015('756c74696d6174656b756e6169330000000000000000000000000000000000005314000000000000')
    sprite('yo432_16', 3)	# 148-150
    sprite('yo432_15', 3)	# 151-153
    sprite('yo432_16', 3)	# 154-156
    sprite('yo432_15', 3)	# 157-159
    Unknown13024(1)
    sprite('yo432_16', 3)	# 160-162
    sprite('yo432_15', 3)	# 163-165
    sprite('yo432_16', 3)	# 166-168
    sprite('yo432_15', 3)	# 169-171
    sprite('yo432_16', 3)	# 172-174
    sprite('yo432_15', 3)	# 175-177
    sprite('yo432_16', 3)	# 178-180
    sprite('yo432_15', 3)	# 181-183
    sprite('yo432_16', 3)	# 184-186
    sprite('yo432_15', 3)	# 187-189
    sprite('yo432_16', 3)	# 190-192
    sprite('yo432_17', 3)	# 193-195
    clearUponHandler(3)
    physicsYImpulse(12000)
    setGravity(3100)
    sprite('yo432_18', 3)	# 196-198
    sprite('yo432_19', 3)	# 199-201
    Unknown23025(0)
    label(14)
    sprite('yo020_07', 4)	# 202-205
    sprite('yo020_08', 4)	# 206-209
    gotoLabel(14)
    label(0)
    sprite('yo010_00', 3)	# 210-212
    sprite('yo000_00', 3)	# 213-215
    sprite('yo400_00', 3)	# 216-218
    sprite('yo400_01', 3)	# 219-221
    SFX_3('slash_knife_slow')
    sprite('yo400_02', 3)	# 222-224
    sprite('yo400_03', 3)	# 225-227
    sprite('yo400_00', 3)	# 228-230
    sprite('yo400_01', 3)	# 231-233
    SFX_3('slash_knife_slow')
    sprite('yo400_02', 3)	# 234-236
    sprite('yo400_03', 12)	# 237-248

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(300)
        Unknown11091(100)

        def upon_32():
            SLOT_51 = 1
            Unknown13024(0)
            Unknown23157(1)
            Unknown23088(1, 1)
            Unknown23084(1)
        sendToLabelUpon(33, 3)

        def upon_STATE_END():
            pass
        setInvincible(1)
    sprite('yo450_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('yo450_01', 3)	# 4-6
    Unknown2036(78, -1, 2)
    Unknown23147()
    GFX_0('P4U_Cutin_Parent', 100)
    tag_voice(1, 'pyo290_0', 'pyo290_1', '', '')
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    physicsYImpulse(-500)
    Unknown35()
    sprite('yo450_02', 3)	# 7-9
    sprite('yo450_03', 3)	# 10-12
    sprite('yo450_01', 3)	# 13-15
    sprite('yo450_02', 3)	# 16-18
    sprite('yo450_03', 3)	# 19-21
    sprite('yo450_01', 3)	# 22-24
    sprite('yo450_02', 3)	# 25-27
    sprite('yo450_03', 3)	# 28-30
    sprite('yo450_04', 3)	# 31-33
    Unknown2015(200)
    physicsYImpulse(20000)
    setGravity(2000)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('yo450_05', 1)	# 34-34
    SFX_3('highjump_l')
    sprite('yo450_05', 1)	# 35-35
    SFX_3('highjump_l')
    sprite('yo450_05', 1)	# 36-36
    SFX_3('highjump_l')
    sprite('yo450_06', 3)	# 37-39
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    sprite('yo450_07', 3)	# 40-42
    Unknown23029(11, 601, 0)
    sprite('yo450_08', 3)	# 43-45
    sprite('yo450_09', 3)	# 46-48
    sprite('yo450_09', 32767)	# 49-32815
    label(1)
    sprite('yo450_10', 3)	# 32816-32818
    sprite('yo450_11', 3)	# 32819-32821
    sprite('yo450_12', 3)	# 32822-32824
    sprite('yo450_13', 3)	# 32825-32827
    SFX_3('cloth_l')
    sprite('yo450_11', 3)	# 32828-32830
    sprite('yo450_12', 3)	# 32831-32833
    sprite('yo450_13', 3)	# 32834-32836
    sprite('yo450_11', 3)	# 32837-32839
    SFX_3('cloth_l')
    sprite('yo450_12', 3)	# 32840-32842
    sprite('yo450_13', 3)	# 32843-32845
    sprite('yo450_11', 3)	# 32846-32848
    sprite('yo450_12', 3)	# 32849-32851
    SFX_3('cloth_l')
    sprite('yo450_13', 3)	# 32852-32854
    sprite('yo450_11', 3)	# 32855-32857
    sprite('yo450_12', 3)	# 32858-32860
    sprite('yo450_13', 3)	# 32861-32863
    SFX_3('cloth_l')
    sprite('yo450_11', 3)	# 32864-32866
    sprite('yo450_12', 3)	# 32867-32869
    sprite('yo450_13', 3)	# 32870-32872
    sprite('yo450_11', 3)	# 32873-32875
    SFX_3('cloth_l')
    sprite('yo450_12', 3)	# 32876-32878
    sprite('yo450_13', 3)	# 32879-32881
    sprite('yo450_11', 3)	# 32882-32884
    sprite('yo450_12', 3)	# 32885-32887
    SFX_3('cloth_l')
    if (not SLOT_51):
        setInvincible(0)
    sprite('yo450_13', 3)	# 32888-32890
    sprite('yo450_11', 3)	# 32891-32893
    sprite('yo450_12', 3)	# 32894-32896
    sprite('yo450_13', 3)	# 32897-32899
    SFX_3('cloth_l')
    sprite('yo450_11', 3)	# 32900-32902
    sprite('yo450_12', 3)	# 32903-32905
    sprite('yo450_13', 3)	# 32906-32908
    sprite('yo450_11', 3)	# 32909-32911
    SFX_3('cloth_l')
    sprite('yo450_12', 3)	# 32912-32914
    sprite('yo450_13', 3)	# 32915-32917
    sprite('yo450_11', 3)	# 32918-32920
    sprite('yo450_12', 3)	# 32921-32923
    SFX_3('cloth_l')
    sprite('yo450_13', 3)	# 32924-32926
    clearUponHandler(32)
    if SLOT_51:
        _gotolabel(2)
    sprite('yo450_11', 3)	# 32927-32929
    sprite('yo450_12', 3)	# 32930-32932
    sprite('yo450_13', 3)	# 32933-32935
    sprite('yo450_11', 3)	# 32936-32938
    sprite('yo450_12', 3)	# 32939-32941
    sprite('yo450_13', 3)	# 32942-32944
    sprite('yo450_11', 3)	# 32945-32947
    sprite('yo450_12', 3)	# 32948-32950
    sprite('yo450_13', 3)	# 32951-32953
    sprite('yo450_14', 6)	# 32954-32959
    loopRest()
    ExitState()
    label(2)
    sprite('yo450_11', 73)	# 32960-33032
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000021000000')
    sprite('yo020_04', 50)	# 33033-33082
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('yo020_04', 10)	# 33083-33092
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    sprite('yo020_04', 30)	# 33093-33122
    tag_voice(1, 'pyo291_0', 'pyo291_1', '', '')
    GFX_0('IchigekiCutIn', 0)
    sprite('yo020_04', 2)	# 33123-33124
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000024000000')
    sprite('dmy_atk02', 4)	# 33125-33128
    Unknown1086(22)
    Unknown36(22)
    physicsYImpulse(0)
    Unknown35()
    physicsYImpulse(0)
    setGravity(0)
    teleportRelativeX(-150000)
    Damage(1500)
    AirUntechableTime(10000)
    Unknown9310(60)
    PushbackX(0)
    AirPushbackX(0)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(0)
    Hitstop(0)
    Unknown9016(1)
    sprite('dmy_atk02', 18)	# 33129-33146
    GFX_0('RanbuYousuke_L', 1)
    RefreshMultihit()
    AirHitstunAnimation(12)
    Unknown11099(1)
    sprite('dmy_atk02', 16)	# 33147-33162
    GFX_0('RanbuYousuke_DownL', 2)
    RefreshMultihit()
    AirHitstunAnimation(11)
    Unknown11099(0)
    sprite('dmy_atk02', 14)	# 33163-33176
    GFX_0('RanbuYousuke_R', 0)
    RefreshMultihit()
    AirHitstunAnimation(13)
    Unknown11099(1)
    sprite('dmy_atk02', 12)	# 33177-33188
    GFX_0('RanbuYousuke_UpR', 3)
    RefreshMultihit()
    AirHitstunAnimation(12)
    Unknown11099(1)
    sprite('dmy_atk02', 10)	# 33189-33198
    GFX_0('RanbuYousuke_L', 1)
    RefreshMultihit()
    AirHitstunAnimation(11)
    Unknown11099(0)
    sprite('dmy_atk02', 8)	# 33199-33206
    GFX_0('RanbuYousuke_UpR', 3)
    RefreshMultihit()
    AirHitstunAnimation(13)
    Unknown11099(1)
    sprite('dmy_atk02', 6)	# 33207-33212
    GFX_0('RanbuYousuke_DownL', 2)
    RefreshMultihit()
    AirHitstunAnimation(12)
    Unknown11099(1)
    sprite('dmy_atk02', 4)	# 33213-33216
    GFX_0('RanbuYousuke_R', 0)
    RefreshMultihit()
    AirHitstunAnimation(11)
    Unknown11099(0)
    sprite('dmy_atk02', 4)	# 33217-33220
    GFX_0('RanbuYousuke_UpR', 3)
    RefreshMultihit()
    AirHitstunAnimation(13)
    Unknown11099(1)
    sprite('dmy_atk02', 4)	# 33221-33224
    GFX_0('RanbuYousuke_L', 1)
    RefreshMultihit()
    sprite('dmy_atk02', 4)	# 33225-33228
    GFX_0('RanbuYousuke_UpR', 3)
    RefreshMultihit()
    sprite('dmy_atk02', 4)	# 33229-33232
    GFX_0('RanbuYousuke_DownL', 2)
    RefreshMultihit()
    sprite('dmy_atk02', 4)	# 33233-33236
    GFX_0('RanbuYousuke_R', 0)
    RefreshMultihit()
    sprite('null', 4)	# 33237-33240
    setGravity(0)
    sprite('null', 32767)	# 33241-66007
    tag_voice(1, 'pyo292_0', 'pyo292_1', '', '')
    label(3)
    sprite('yo020_04', 100)	# 66008-66107
    Unknown23024(0)
    physicsYImpulse(0)
    setGravity(0)
    teleportRelativeY(5000000)
    sprite('yo020_07', 32767)	# 66108-98874
    setGravity(2800)
    sendToLabelUpon(2, 4)
    label(4)
    sprite('yo450_11', 3)	# 98875-98877
    tag_voice(0, 'pyo293_0', 'pyo293_1', '', '')
    sprite('yo450_12', 3)	# 98878-98880
    sprite('yo450_13', 3)	# 98881-98883
    sprite('yo450_11', 3)	# 98884-98886
    SFX_3('cloth_l')
    sprite('yo450_12', 3)	# 98887-98889
    sprite('yo450_13', 3)	# 98890-98892
    sprite('yo450_11', 3)	# 98893-98895
    sprite('yo450_12', 3)	# 98896-98898
    SFX_3('cloth_l')
    sprite('yo450_13', 3)	# 98899-98901
    sprite('yo450_11', 3)	# 98902-98904
    sprite('yo450_12', 3)	# 98905-98907
    sprite('yo450_13', 3)	# 98908-98910
    SFX_3('cloth_l')
    sprite('yo450_11', 3)	# 98911-98913
    sprite('yo450_12', 3)	# 98914-98916
    sprite('yo450_13', 3)	# 98917-98919
    sprite('yo450_11', 3)	# 98920-98922
    SFX_3('cloth_l')
    sprite('yo450_12', 3)	# 98923-98925
    sprite('yo450_13', 3)	# 98926-98928
    sprite('yo450_11', 3)	# 98929-98931
    sprite('yo450_12', 3)	# 98932-98934
    SFX_3('cloth_l')
    sprite('yo450_13', 3)	# 98935-98937
    sprite('yo450_11', 3)	# 98938-98940
    sprite('yo450_12', 3)	# 98941-98943
    sprite('yo450_13', 3)	# 98944-98946
    SFX_3('cloth_l')
    sprite('yo450_14', 6)	# 98947-98952
    sprite('yo010_02', 4)	# 98953-98956
    sprite('yo010_01', 4)	# 98957-98960
    sprite('yo010_00', 4)	# 98961-98964
    sprite('yo000_00', 4)	# 98965-98968
    loopRest()

@State
def CmnActChangePartnerQuickIn():
    sprite('yo032_05', 3)	# 1-3
    sprite('yo032_06', 5)	# 4-8
    sprite('yo032_09', 7)	# 9-15
    sprite('yo032_09', 7)	# 16-22
    sprite('yo032_10', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('yo033_00', 1)	# 1-1
    sprite('yo033_01', 2)	# 2-3
    sprite('yo033_01', 2)	# 4-5
    sprite('yo033_02', 1)	# 6-6
    sprite('yo033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('yo033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yo033_03', 3)	# 13-15
    sprite('yo033_04', 3)	# 16-18

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_64 = 0

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(99)
    sprite('null', 2)	# 1-2
    label(0)
    sprite('yo020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('yo020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('yo010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown2017(0)
        Unknown2034(0)
        teleportRelativeY(0)
        SLOT_64 = 1
    label(0)
    sprite('null', 1)	# 1-1
    gotoLabel(0)

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        AttackLevel_(4)
        Unknown11028(24)
        Hitstop(20)
        Unknown9016(1)
        Unknown23027()

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)

        def upon_77():
            clearUponHandler(77)
            ScreenShake(10000, 10000)
    sprite('null', 5)	# 1-5
    sprite('null', 5)	# 6-10
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(400000)
    Unknown2053(1)
    sprite('null', 5)	# 11-15
    GFX_1('yoef_airthrow', 103)
    sprite('yo321_01', 4)	# 16-19
    sprite('yo321_02', 4)	# 20-23
    sprite('yo321_03', 4)	# 24-27
    sprite('yo321_04', 4)	# 28-31
    sprite('yo321_05', 4)	# 32-35	 **attackbox here**
    physicsYImpulse(-100000)
    sprite('yo321_06', 4)	# 36-39	 **attackbox here**
    label(1)
    sprite('yo321_05', 4)	# 40-43	 **attackbox here**
    sprite('yo321_06', 4)	# 44-47	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 48-50
    Unknown1084(1)
    sprite('yo321_07', 3)	# 51-53
    Unknown8000(-1, 1, 1)
    sprite('yo321_08', 3)	# 54-56
    sprite('yo321_09', 13)	# 57-69
    sprite('yo321_10', 3)	# 70-72

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('yo033_01', 3)	# 1-3
    sprite('yo033_02', 3)	# 4-6
    sprite('yo033_01', 3)	# 7-9
    sprite('yo033_02', 3)	# 10-12
    sprite('yo033_01', 3)	# 13-15
    sprite('yo033_02', 3)	# 16-18
    sprite('yo033_01', 3)	# 19-21
    sprite('yo033_02', 3)	# 22-24
    sprite('yo033_01', 3)	# 25-27
    sprite('yo033_02', 3)	# 28-30
    sprite('yo033_01', 30)	# 31-60

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
                SFX_3('301_overdrive_end')
            if (SLOT_18 == 53):
                sendToLabel(1)
    sprite('yo204_00', 5)	# 1-5
    sprite('yo204_01', 4)	# 6-9
    sprite('yo204_02', 4)	# 10-13
    sprite('yo204_03', 4)	# 14-17
    label(0)
    sprite('yo204_04', 4)	# 18-21
    sprite('yo204_05', 4)	# 22-25
    sprite('yo204_06', 4)	# 26-29
    gotoLabel(0)
    label(1)
    sprite('yo204_02', 3)	# 30-32
    sprite('yo204_01', 4)	# 33-36
    sprite('yo204_00', 2)	# 37-38

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
                SFX_3('301_overdrive_end')
            if (SLOT_18 == 59):
                Unknown1018()
                Unknown1023()
                Unknown1038()
                Unknown1019(40)
                YAccel(40)
            if (SLOT_18 == 71):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('yo255_00', 6)	# 1-6
    sprite('yo255_01', 7)	# 7-13
    sprite('yo255_02', 2)	# 14-15
    sprite('yo255_03', 2)	# 16-17
    label(0)
    sprite('yo255_04', 2)	# 18-19
    sprite('yo255_05', 2)	# 20-21
    sprite('yo255_06', 2)	# 22-23
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yo255_02', 3)	# 24-26
    sprite('yo255_01', 3)	# 27-29
    sprite('yo255_00', 3)	# 30-32

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17015()
        Unknown2034(0)
    sprite('yo400_00', 3)	# 1-3
    sprite('yo400_01', 4)	# 4-7
    sprite('yo400_02', 6)	# 8-13
    sprite('yo400_03', 6)	# 14-19
    sprite('yo400_00', 6)	# 20-25
    sprite('yo400_01', 6)	# 26-31
    sprite('yo400_02', 6)	# 32-37
    sprite('yo400_03', 6)	# 38-43
    sprite('yo400_01', 6)	# 44-49
    sprite('yo400_02', 6)	# 50-55
    sprite('yo400_03', 11)	# 56-66
    sprite('yo400_00', 3)	# 67-69

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('yo001_00', 5)	# 1-5
    sprite('yo001_01', 5)	# 6-10
    sprite('yo001_02', 5)	# 11-15
    sprite('yo001_03', 10)	# 16-25
    GFX_0('yoef_reaction', 0)
    sprite('yo001_04', 5)	# 26-30
    sprite('yo001_01', 10)	# 31-40
    sprite('yo001_02', 5)	# 41-45
    sprite('yo001_03', 10)	# 46-55
    GFX_0('yoef_reaction', 0)
    sprite('yo001_04', 5)	# 56-60
    sprite('yo001_01', 10)	# 61-70
    sprite('yo001_00', 30)	# 71-100

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()

        def upon_43():
            if (SLOT_48 == 155):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('yo205_00', 3)	# 1-3
    sprite('yo205_01', 4)	# 4-7
    Unknown23029(11, 102, 0)
    sprite('yo205_02', 3)	# 8-10
    Unknown7007('70796f3132305f3000000000000000006400000070796f3132305f3200000000000000006400000070796f3132315f3100000000000000006400000070796f3132335f30000000000000000064000000')
    sprite('yo205_03', 3)	# 11-13
    GFX_1('persona_enter_ply', 0)
    sprite('yo205_04', 3)	# 14-16
    sprite('yo205_05', 3)	# 17-19
    sprite('yo205_06', 3)	# 20-22
    sprite('yo205_04', 3)	# 23-25
    sprite('yo205_05', 3)	# 26-28
    sprite('yo205_06', 3)	# 29-31
    sprite('yo205_04', 3)	# 32-34
    sprite('yo205_05', 3)	# 35-37
    sprite('yo205_06', 3)	# 38-40
    sprite('yo205_04', 3)	# 41-43
    sprite('yo205_05', 3)	# 44-46
    sprite('yo205_06', 3)	# 47-49
    sprite('yo205_04', 3)	# 50-52
    sprite('yo205_05', 3)	# 53-55
    sprite('yo205_06', 3)	# 56-58
    sprite('yo205_04', 3)	# 59-61
    sprite('yo205_05', 3)	# 62-64
    sprite('yo205_06', 3)	# 65-67
    sprite('yo205_04', 3)	# 68-70
    sprite('yo205_05', 3)	# 71-73
    sprite('yo205_06', 3)	# 74-76
    sprite('yo205_04', 3)	# 77-79
    sprite('yo205_05', 3)	# 80-82
    sprite('yo205_06', 3)	# 83-85
    sprite('yo205_02', 3)	# 86-88
    Recovery()
    clearUponHandler(43)
    sprite('yo205_01', 4)	# 89-92
    sprite('yo205_00', 2)	# 93-94
    loopRest()
    ExitState()
    label(1)
    sprite('yo204_00', 3)	# 95-97
    sprite('yo204_01', 1)	# 98-98
    sprite('yo204_01', 3)	# 99-101
    sprite('yo204_02', 3)	# 102-104
    sprite('yo204_03', 3)	# 105-107
    GFX_1('persona_enter_ply', 0)
    sprite('yo204_04', 3)	# 108-110
    sprite('yo204_05', 3)	# 111-113
    sprite('yo204_06', 3)	# 114-116
    sprite('yo204_04', 3)	# 117-119
    sprite('yo204_05', 3)	# 120-122
    sprite('yo204_06', 3)	# 123-125
    sprite('yo204_04', 3)	# 126-128
    sprite('yo204_05', 3)	# 129-131
    sprite('yo204_06', 3)	# 132-134
    Recovery()
    sprite('yo204_04', 3)	# 135-137
    sprite('yo204_05', 3)	# 138-140
    sprite('yo204_06', 3)	# 141-143
    sprite('yo204_04', 3)	# 144-146
    sprite('yo204_05', 3)	# 147-149
    sprite('yo204_06', 3)	# 150-152
    sprite('yo204_02', 6)	# 153-158
    sprite('yo204_01', 3)	# 159-161
    sprite('yo204_00', 3)	# 162-164

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirUntechableTime(60)
        Unknown9016(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(40000)
        PushbackX(19800)
        Unknown11042(1)
        sendToLabelUpon(2, 1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('yo202_00', 2)	# 1-2
    sprite('yo202_01', 4)	# 3-6
    physicsXImpulse(24000)
    sprite('yo202_02', 1)	# 7-7
    sprite('yo202_03', 1)	# 8-8
    sprite('yo202_04', 1)	# 9-9
    SFX_3('hit_m_middle')
    Unknown7009(2)
    sprite('yo202_05', 2)	# 10-11	 **attackbox here**
    Unknown1019(80)
    SFX_3('slash_knife_slow')
    sprite('yo202_06', 2)	# 12-13	 **attackbox here**
    Unknown23054('796f3230325f303500000000000000000000000000000000000000000000000004000000')
    physicsXImpulse(3000)
    physicsYImpulse(30000)
    setGravity(2000)
    sprite('yo202_06', 2)	# 14-15	 **attackbox here**
    sprite('yo202_07', 3)	# 16-18
    Unknown23027()
    Recovery()
    sprite('yo202_08', 3)	# 19-21
    label(0)
    sprite('yo020_07', 4)	# 22-25
    sprite('yo020_08', 4)	# 26-29
    gotoLabel(0)
    label(1)
    sprite('yo010_00', 3)	# 30-32
    Unknown1084(1)

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
        AttackP1(70)
        Unknown11092(1)
        Hitstop(0)
        Unknown11001(8, 8, 8)
        Unknown9310(1)
        AirHitstunAnimation(11)
        Unknown9154(20)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(-20000)
        PushbackX(8000)
        Unknown11084(1)
        Unknown11042(1)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(1)

        def upon_3():
            if SLOT_51:
                if (SLOT_19 < 300000):
                    clearUponHandler(3)
                    sendToLabel(0)
                    SLOT_51 = 0
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
        callSubroutine('DoNotBeginCancel')
    sprite('yo403_00', 2)	# 1-2
    sprite('yo403_01', 4)	# 3-6
    sprite('yo403_02', 2)	# 7-8
    Unknown7007('70796f3230375f3000000000000000006400000070796f3230375f3100000000000000006400000070796f3230375f3200000000000000006400000070796f3230385f30000000000000000064000000')
    physicsXImpulse(49000)
    SFX_3('runjump_stone_light')
    sprite('yo403_03', 2)	# 9-10
    SFX_3('airdash_m')
    sprite('yo403_04', 2)	# 11-12
    SLOT_51 = 1
    sprite('yo403_05', 2)	# 13-14
    sprite('yo403_06', 2)	# 15-16
    sprite('yo403_03', 2)	# 17-18
    SFX_3('runjump_stone_light')
    sprite('yo403_04', 2)	# 19-20
    sprite('yo403_05', 2)	# 21-22
    label(2)
    sprite('yo403_21', 2)	# 23-24
    SLOT_51 = 0
    Unknown1019(30)
    Recovery()
    sprite('yo403_22', 4)	# 25-28
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_23', 4)	# 29-32
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('yo403_24', 4)	# 33-36
    Unknown1019(50)
    sprite('yo403_25', 4)	# 37-40
    Unknown1019(0)
    loopRest()
    ExitState()
    label(0)
    sprite('yo403_07', 2)	# 41-42
    sprite('yo403_08', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('yo403_08', 2)	# 46-47	 **attackbox here**
    Unknown1084(1)
    Unknown23027()
    clearUponHandler(10)
    sprite('yo403_09', 2)	# 48-49	 **attackbox here**
    sprite('yo403_10', 2)	# 50-51
    Unknown1084(1)
    physicsXImpulse(10000)
    physicsYImpulse(20000)
    setGravity(4500)
    sprite('yo403_11', 2)	# 52-53
    sprite('yo403_12', 2)	# 54-55	 **attackbox here**
    Unknown2015(40)
    Unknown1084(1)
    sprite('yo403_13', 3)	# 56-58	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(22000)
    Hitstop(9)
    Unknown9310(-1)
    sprite('yo403_14', 3)	# 59-61	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2015(-1)
    sprite('yo403_15', 3)	# 62-64
    Unknown1007(50000)
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    setGravity(2400)
    sendToLabelUpon(2, 4)
    sprite('yo403_16', 3)	# 65-67
    clearUponHandler(3)
    sprite('yo403_17', 3)	# 68-70
    sprite('yo403_18', 3)	# 71-73
    sprite('yo403_19', 3)	# 74-76
    sprite('yo403_20', 3)	# 77-79
    label(3)
    sprite('yo020_07', 3)	# 80-82
    sprite('yo020_08', 3)	# 83-85
    loopRest()
    gotoLabel(3)
    label(4)
    Unknown1084(1)
    Unknown18009(1)
    clearUponHandler(2)
    sprite('yo231_00', 1)	# 86-86
    Unknown8000(100, 1, 0)
    sprite('yo231_01', 2)	# 87-88
    sprite('yo231_00', 1)	# 89-89
    sprite('yo010_01', 4)	# 90-93
    sprite('yo010_00', 4)	# 94-97

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
    Unknown2036(92, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('yo020_07', 4)	# 3-6
    sprite('yo020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateTatsumakiDDDOD')
    else:
        enterState('UltimateTatsumakiDDD')

@State
def UltimateTatsumakiDDD():

    def upon_IMMEDIATE():
        Unknown2006()
        AttackDefaults_StandingDD()
        Unknown30063(1)

        def upon_3():
            if (SLOT_23 >= 2600000):
                teleportRelativeY(2600000)
            if SLOT_51:
                Unknown1019(97)
                YAccel(97)
                if (SLOT_23 < 50000):
                    teleportRelativeY(50000)
                    physicsYImpulse(0)
                SLOT_67 = SLOT_40
                if (SLOT_40 > 100):
                    SLOT_67 = (SLOT_67 / 640)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                if (SLOT_40 < (-100)):
                    SLOT_67 = (SLOT_67 / 640)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                SLOT_67 = SLOT_41
                if (SLOT_41 > 100):
                    SLOT_67 = (SLOT_67 / 640)
                    SLOT_13 = (SLOT_13 + SLOT_67)
                if (SLOT_41 < (-100)):
                    SLOT_67 = (SLOT_67 / 640)
                    SLOT_13 = (SLOT_13 + SLOT_67)
        sendToLabelUpon(2, 6)
    sprite('yo431_00', 3)	# 1-3
    Unknown1084(1)
    physicsYImpulse(10000)
    physicsXImpulse(1000)
    setGravity(100)
    setInvincible(1)
    sprite('yo431_01', 4)	# 4-7
    YAccel(70)
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(60000)
    physicsYImpulse(-1500)
    Unknown35()
    sprite('yo431_02', 4)	# 8-11
    YAccel(70)
    sprite('yo431_03', 4)	# 12-15
    YAccel(70)
    sprite('yo431_04', 4)	# 16-19
    YAccel(70)
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('yo431_05', 4)	# 20-23
    Unknown23029(11, 152, 0)
    YAccel(70)
    YAccel(0)
    Unknown1019(0)
    setGravity(0)
    sprite('yo431_06', 3)	# 24-26
    sprite('yo431_07', 3)	# 27-29
    sprite('yo431_06', 3)	# 30-32
    sprite('yo431_07', 3)	# 33-35
    sprite('yo431_06', 3)	# 36-38
    sprite('yo431_07', 3)	# 39-41
    sprite('yo431_06', 3)	# 42-44
    sprite('yo431_07', 3)	# 45-47
    sprite('yo431_06', 3)	# 48-50
    sprite('yo431_07', 3)	# 51-53
    sprite('yo431_06', 3)	# 54-56
    sprite('yo431_07', 3)	# 57-59
    sprite('yo431_11', 5)	# 60-64
    SLOT_51 = 1
    setGravity(100)
    sprite('yo431_08', 5)	# 65-69
    sprite('yo431_09', 5)	# 70-74
    setInvincible(0)
    sprite('yo431_10', 4)	# 75-78
    tag_voice(1, 'pyo253_0', 'pyo253_1', '', '')
    sprite('yo431_11', 3)	# 79-81
    sprite('yo431_08', 1)	# 82-82
    sprite('yo431_09', 1)	# 83-83
    sprite('yo431_10', 1)	# 84-84
    sprite('yo431_11', 1)	# 85-85
    sprite('yo431_08', 1)	# 86-86
    sprite('yo431_09', 1)	# 87-87
    sprite('yo431_10', 1)	# 88-88
    sprite('yo431_11', 1)	# 89-89
    sprite('yo431_08', 1)	# 90-90
    sprite('yo431_09', 1)	# 91-91
    sprite('yo431_10', 1)	# 92-92
    sprite('yo431_11', 1)	# 93-93
    sprite('yo431_08', 1)	# 94-94
    sprite('yo431_09', 1)	# 95-95
    sprite('yo431_10', 1)	# 96-96
    sprite('yo431_11', 1)	# 97-97
    sprite('yo431_08', 1)	# 98-98
    sprite('yo431_09', 1)	# 99-99
    sprite('yo431_10', 1)	# 100-100
    sprite('yo431_11', 1)	# 101-101
    sprite('yo431_08', 1)	# 102-102
    sprite('yo431_09', 1)	# 103-103
    sprite('yo431_10', 1)	# 104-104
    sprite('yo431_11', 1)	# 105-105
    sprite('yo431_08', 1)	# 106-106
    sprite('yo431_09', 1)	# 107-107
    sprite('yo431_10', 1)	# 108-108
    sprite('yo431_11', 1)	# 109-109
    sprite('yo431_08', 1)	# 110-110
    sprite('yo431_09', 1)	# 111-111
    sprite('yo431_10', 1)	# 112-112
    sprite('yo431_11', 1)	# 113-113
    sprite('yo431_08', 1)	# 114-114
    sprite('yo431_09', 1)	# 115-115
    sprite('yo431_10', 1)	# 116-116
    sprite('yo431_11', 1)	# 117-117
    sprite('yo431_08', 1)	# 118-118
    sprite('yo431_09', 1)	# 119-119
    sprite('yo431_10', 1)	# 120-120
    sprite('yo431_11', 1)	# 121-121
    sprite('yo431_08', 1)	# 122-122
    sprite('yo431_09', 1)	# 123-123
    sprite('yo431_10', 1)	# 124-124
    sprite('yo431_11', 1)	# 125-125
    sprite('yo431_08', 1)	# 126-126
    sprite('yo431_09', 1)	# 127-127
    sprite('yo431_10', 1)	# 128-128
    sprite('yo431_11', 1)	# 129-129
    sprite('yo431_08', 1)	# 130-130
    sprite('yo431_09', 1)	# 131-131
    sprite('yo431_10', 1)	# 132-132
    sprite('yo431_11', 1)	# 133-133
    sprite('yo431_08', 1)	# 134-134
    sprite('yo431_09', 1)	# 135-135
    sprite('yo431_10', 1)	# 136-136
    sprite('yo431_11', 1)	# 137-137
    sprite('yo431_08', 1)	# 138-138
    sprite('yo431_09', 1)	# 139-139
    sprite('yo431_10', 1)	# 140-140
    sprite('yo431_11', 1)	# 141-141
    sprite('yo431_08', 2)	# 142-143
    sprite('yo431_09', 2)	# 144-145
    sprite('yo431_10', 2)	# 146-147
    sprite('yo431_11', 2)	# 148-149
    sprite('yo431_08', 2)	# 150-151
    sprite('yo431_09', 2)	# 152-153
    sprite('yo431_10', 2)	# 154-155
    sprite('yo431_11', 2)	# 156-157
    sprite('yo431_08', 2)	# 158-159
    sprite('yo431_09', 2)	# 160-161
    sprite('yo431_10', 2)	# 162-163
    sprite('yo431_11', 2)	# 164-165
    sprite('yo431_08', 2)	# 166-167
    sprite('yo431_09', 2)	# 168-169
    sprite('yo431_10', 2)	# 170-171
    sprite('yo431_11', 2)	# 172-173
    sprite('yo431_08', 2)	# 174-175
    sprite('yo431_09', 2)	# 176-177
    sprite('yo431_10', 2)	# 178-179
    sprite('yo431_11', 2)	# 180-181
    sprite('yo431_08', 2)	# 182-183
    sprite('yo431_09', 2)	# 184-185
    sprite('yo431_10', 2)	# 186-187
    sprite('yo431_11', 2)	# 188-189
    sprite('yo431_08', 2)	# 190-191
    sprite('yo431_09', 2)	# 192-193
    sprite('yo431_10', 2)	# 194-195
    sprite('yo431_11', 2)	# 196-197
    sprite('yo431_08', 2)	# 198-199
    sprite('yo431_09', 2)	# 200-201
    sprite('yo431_10', 2)	# 202-203
    sprite('yo431_11', 2)	# 204-205
    sprite('yo431_08', 2)	# 206-207
    sprite('yo431_09', 2)	# 208-209
    sprite('yo431_10', 2)	# 210-211
    sprite('yo431_11', 2)	# 212-213
    loopRest()
    SLOT_51 = 0
    setGravity(2000)
    Unknown1019(70)
    Unknown1021(5000)
    sprite('yo431_08', 3)	# 214-216
    Unknown38(6, 1)
    sprite('yo431_09', 3)	# 217-219
    sprite('yo431_10', 3)	# 220-222
    sprite('yo431_11', 3)	# 223-225
    label(0)
    sprite('yo431_08', 4)	# 226-229
    sprite('yo431_09', 4)	# 230-233
    sprite('yo431_10', 4)	# 234-237
    sprite('yo431_11', 4)	# 238-241
    loopRest()
    gotoLabel(0)
    label(6)
    SLOT_51 = 0
    physicsXImpulse(1000)
    sprite('yo431_09', 4)	# 242-245
    Unknown23029(1, 5001, 0)
    GFX_0('DDD_Wind', -1)
    sprite('yo431_10', 4)	# 246-249
    sprite('yo431_12', 4)	# 250-253
    Unknown1019(70)
    sprite('yo431_13', 4)	# 254-257
    sprite('yo431_14', 4)	# 258-261
    Unknown1019(0)
    sprite('yo431_15', 10)	# 262-271
    sprite('yo431_16', 4)	# 272-275
    sprite('yo431_17', 4)	# 276-279

@State
def UltimateTatsumakiDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown2006()
        Unknown1084(1)
        physicsYImpulse(10000)
        physicsXImpulse(1000)
        setGravity(100)
        setInvincible(1)

        def upon_3():
            if (SLOT_23 >= 2600000):
                teleportRelativeY(2600000)
            if SLOT_51:
                Unknown1019(97)
                YAccel(97)
                if (SLOT_23 < 50000):
                    teleportRelativeY(50000)
                    physicsYImpulse(0)
                SLOT_67 = SLOT_40
                if (SLOT_40 > 100):
                    SLOT_67 = (SLOT_67 / 640)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                if (SLOT_40 < (-100)):
                    SLOT_67 = (SLOT_67 / 640)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                SLOT_67 = SLOT_41
                if (SLOT_41 > 100):
                    SLOT_67 = (SLOT_67 / 640)
                    SLOT_13 = (SLOT_13 + SLOT_67)
                if (SLOT_41 < (-100)):
                    SLOT_67 = (SLOT_67 / 640)
                    SLOT_13 = (SLOT_13 + SLOT_67)
    sprite('yo431_00', 3)	# 1-3
    sprite('yo431_01', 4)	# 4-7
    YAccel(70)
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(60000)
    physicsYImpulse(-1500)
    Unknown35()
    sendToLabelUpon(2, 72)
    sprite('yo431_02', 4)	# 8-11
    YAccel(70)
    sprite('yo431_03', 4)	# 12-15
    YAccel(70)
    sprite('yo431_04', 4)	# 16-19
    YAccel(70)
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('yo431_05', 4)	# 20-23
    Unknown23029(11, 153, 0)
    YAccel(70)
    YAccel(0)
    Unknown1019(0)
    setGravity(0)
    sprite('yo431_06', 3)	# 24-26
    sprite('yo431_07', 3)	# 27-29
    sprite('yo431_06', 3)	# 30-32
    sprite('yo431_07', 3)	# 33-35
    sprite('yo431_06', 3)	# 36-38
    sprite('yo431_07', 3)	# 39-41
    sprite('yo431_06', 3)	# 42-44
    sprite('yo431_07', 3)	# 45-47
    sprite('yo431_06', 3)	# 48-50
    sprite('yo431_07', 3)	# 51-53
    sprite('yo431_06', 3)	# 54-56
    sprite('yo431_07', 3)	# 57-59
    sprite('yo431_11', 5)	# 60-64
    SLOT_51 = 1
    setGravity(100)
    sprite('yo431_08', 5)	# 65-69
    sprite('yo431_09', 5)	# 70-74
    setInvincible(0)
    sprite('yo431_10', 4)	# 75-78
    tag_voice(1, 'pyo253_0', 'pyo253_1', '', '')
    sprite('yo431_11', 3)	# 79-81
    sprite('yo431_08', 1)	# 82-82
    sprite('yo431_09', 1)	# 83-83
    sprite('yo431_10', 1)	# 84-84
    sprite('yo431_11', 1)	# 85-85
    sprite('yo431_08', 1)	# 86-86
    sprite('yo431_09', 1)	# 87-87
    sprite('yo431_10', 1)	# 88-88
    sprite('yo431_11', 1)	# 89-89
    sprite('yo431_08', 1)	# 90-90
    sprite('yo431_09', 1)	# 91-91
    sprite('yo431_10', 1)	# 92-92
    sprite('yo431_11', 1)	# 93-93
    sprite('yo431_08', 1)	# 94-94
    sprite('yo431_09', 1)	# 95-95
    sprite('yo431_10', 1)	# 96-96
    sprite('yo431_11', 1)	# 97-97
    sprite('yo431_08', 1)	# 98-98
    sprite('yo431_09', 1)	# 99-99
    sprite('yo431_10', 1)	# 100-100
    sprite('yo431_11', 1)	# 101-101
    sprite('yo431_08', 1)	# 102-102
    sprite('yo431_09', 1)	# 103-103
    sprite('yo431_10', 1)	# 104-104
    sprite('yo431_11', 1)	# 105-105
    sprite('yo431_08', 1)	# 106-106
    sprite('yo431_09', 1)	# 107-107
    sprite('yo431_10', 1)	# 108-108
    sprite('yo431_11', 1)	# 109-109
    sprite('yo431_08', 1)	# 110-110
    sprite('yo431_09', 1)	# 111-111
    sprite('yo431_10', 1)	# 112-112
    sprite('yo431_11', 1)	# 113-113
    sprite('yo431_08', 1)	# 114-114
    sprite('yo431_09', 1)	# 115-115
    sprite('yo431_10', 1)	# 116-116
    sprite('yo431_11', 1)	# 117-117
    sprite('yo431_08', 1)	# 118-118
    sprite('yo431_09', 1)	# 119-119
    sprite('yo431_10', 1)	# 120-120
    sprite('yo431_11', 1)	# 121-121
    sprite('yo431_08', 1)	# 122-122
    sprite('yo431_09', 1)	# 123-123
    sprite('yo431_10', 1)	# 124-124
    sprite('yo431_11', 1)	# 125-125
    sprite('yo431_08', 1)	# 126-126
    sprite('yo431_09', 1)	# 127-127
    sprite('yo431_10', 1)	# 128-128
    sprite('yo431_11', 1)	# 129-129
    sprite('yo431_08', 1)	# 130-130
    sprite('yo431_09', 1)	# 131-131
    sprite('yo431_10', 1)	# 132-132
    sprite('yo431_11', 1)	# 133-133
    sprite('yo431_08', 1)	# 134-134
    sprite('yo431_09', 1)	# 135-135
    sprite('yo431_10', 1)	# 136-136
    sprite('yo431_11', 1)	# 137-137
    sprite('yo431_08', 1)	# 138-138
    sprite('yo431_09', 1)	# 139-139
    sprite('yo431_10', 1)	# 140-140
    sprite('yo431_11', 1)	# 141-141
    sprite('yo431_08', 2)	# 142-143
    sprite('yo431_09', 2)	# 144-145
    sprite('yo431_10', 2)	# 146-147
    sprite('yo431_11', 2)	# 148-149
    sprite('yo431_08', 2)	# 150-151
    sprite('yo431_09', 2)	# 152-153
    sprite('yo431_10', 2)	# 154-155
    sprite('yo431_11', 2)	# 156-157
    sprite('yo431_08', 2)	# 158-159
    sprite('yo431_09', 2)	# 160-161
    sprite('yo431_10', 2)	# 162-163
    sprite('yo431_11', 2)	# 164-165
    sprite('yo431_08', 2)	# 166-167
    sprite('yo431_09', 2)	# 168-169
    sprite('yo431_10', 2)	# 170-171
    sprite('yo431_11', 2)	# 172-173
    sprite('yo431_08', 2)	# 174-175
    sprite('yo431_09', 2)	# 176-177
    sprite('yo431_10', 2)	# 178-179
    sprite('yo431_11', 2)	# 180-181
    sprite('yo431_08', 2)	# 182-183
    sprite('yo431_09', 2)	# 184-185
    sprite('yo431_10', 2)	# 186-187
    sprite('yo431_11', 2)	# 188-189
    sprite('yo431_08', 2)	# 190-191
    sprite('yo431_09', 2)	# 192-193
    sprite('yo431_10', 2)	# 194-195
    sprite('yo431_11', 2)	# 196-197
    sprite('yo431_08', 2)	# 198-199
    sprite('yo431_09', 2)	# 200-201
    sprite('yo431_10', 2)	# 202-203
    sprite('yo431_11', 2)	# 204-205
    sprite('yo431_08', 2)	# 206-207
    sprite('yo431_09', 2)	# 208-209
    sprite('yo431_10', 2)	# 210-211
    sprite('yo431_11', 2)	# 212-213
    loopRest()
    SLOT_51 = 0
    setGravity(2000)
    Unknown1019(70)
    Unknown1021(5000)
    sprite('yo431_08', 3)	# 214-216
    GFX_0('TatsumakiYoin', 103)
    Unknown38(6, 1)
    sprite('yo431_09', 3)	# 217-219
    sprite('yo431_10', 3)	# 220-222
    sprite('yo431_11', 3)	# 223-225
    label(70)
    sprite('yo431_08', 4)	# 226-229
    sprite('yo431_09', 4)	# 230-233
    sprite('yo431_10', 4)	# 234-237
    sprite('yo431_11', 4)	# 238-241
    loopRest()
    gotoLabel(70)
    label(72)
    SLOT_51 = 0
    physicsXImpulse(1000)
    sprite('yo431_09', 4)	# 242-245
    Unknown23029(1, 5001, 0)
    GFX_0('DDD_Wind', -1)
    sprite('yo431_10', 4)	# 246-249
    sprite('yo431_12', 4)	# 250-253
    Unknown1019(70)
    sprite('yo431_13', 4)	# 254-257
    sprite('yo431_14', 4)	# 258-261
    Unknown1019(0)
    sprite('yo431_15', 10)	# 262-271
    sprite('yo431_16', 4)	# 272-275
    sprite('yo431_17', 4)	# 276-279

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
    sprite('null', 5)	# 121-125
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(400000)
    Unknown2053(1)
    sprite('null', 5)	# 126-130
    GFX_1('yoef_airthrow', 103)
    sprite('yo321_01', 4)	# 131-134
    sprite('yo321_02', 4)	# 135-138
    sprite('yo321_03', 4)	# 139-142
    sprite('yo321_04', 4)	# 143-146
    sprite('yo321_05', 4)	# 147-150	 **attackbox here**
    physicsYImpulse(-100000)
    sprite('yo321_06', 4)	# 151-154	 **attackbox here**
    label(1)
    sprite('yo321_05', 4)	# 155-158	 **attackbox here**
    sprite('yo321_06', 4)	# 159-162	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 163-165
    Unknown1084(1)
    sprite('yo321_07', 4)	# 166-169
    Unknown8000(-1, 1, 1)
    sprite('yo321_08', 4)	# 170-173
    sprite('yo321_09', 16)	# 174-189
    sprite('yo321_10', 4)	# 190-193

@State
def CmnActChangeReturnAppealBurst():
    sprite('yo064_01', 30)	# 1-30
    sprite('yo064_02', 5)	# 31-35
    sprite('yo064_03', 5)	# 36-40
    sprite('yo010_02', 5)	# 41-45
    sprite('yo010_01', 5)	# 46-50
    sprite('yo010_00', 5)	# 51-55
    sprite('yo000_00', 30)	# 56-85

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('yo210_00', 1)	# 1-1
    sprite('yo210_01', 2)	# 2-3
    sprite('yo210_02', 2)	# 4-5
    tag_voice(1, 'pyo156_0', 'pyo156_1', '', '')
    sprite('yo210_03', 2)	# 6-7
    sprite('yo210_04', 2)	# 8-9
    sprite('yo210_05', 2)	# 10-11
    physicsXImpulse(15000)
    physicsYImpulse(20000)
    setGravity(5000)
    sprite('yo210_05', 4)	# 12-15
    sprite('yo210_06', 3)	# 16-18
    sprite('yo210_07', 3)	# 19-21
    sprite('yo210_09', 3)	# 22-24	 **attackbox here**
    Unknown23054('796f3231305f303800000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    Unknown23086(1)
    SFX_3('slash_knife_slow')
    Unknown1084(1)
    sprite('yo210_09', 8)	# 25-32	 **attackbox here**
    Unknown23027()
    sprite('yo210_10', 5)	# 33-37
    sprite('yo210_11', 5)	# 38-42
    sprite('yo010_02', 2)	# 43-44
    sprite('yo010_01', 2)	# 45-46
    sprite('yo010_00', 2)	# 47-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown9016(1)
    sprite('yo210_09', 4)	# 1-4	 **attackbox here**
    StartMultihit()
    Unknown1084(1)
    sprite('yo210_09', 3)	# 5-7	 **attackbox here**
    sprite('yo210_10', 6)	# 8-13
    sprite('yo210_11', 6)	# 14-19
    sprite('yo203_00', 2)	# 20-21
    sprite('yo203_01', 2)	# 22-23
    sprite('yo203_02', 2)	# 24-25
    sprite('yo203_03', 2)	# 26-27
    sprite('yo203_04', 2)	# 28-29	 **attackbox here**
    StartMultihit()
    SFX_3('slash_knife_middle')
    sprite('yo203_06', 2)	# 30-31	 **attackbox here**
    Unknown23054('796f3230335f303500000000000000000000000000000000000000000000000006000000')
    RefreshMultihit()
    tag_voice(0, 'pyo157_0', 'pyo157_1', '', '')
    SFX_3('slash_knife_middle')
    sprite('yo203_07', 4)	# 32-35
    sprite('yo203_08', 4)	# 36-39
    sprite('yo203_09', 4)	# 40-43
    label(0)
    sprite('yo000_00', 6)	# 44-49
    sprite('yo000_01', 6)	# 50-55
    sprite('yo000_02', 6)	# 56-61
    sprite('yo000_03', 6)	# 62-67
    sprite('yo000_04', 6)	# 68-73
    sprite('yo000_05', 6)	# 74-79
    sprite('yo000_06', 6)	# 80-85
    sprite('yo000_07', 6)	# 86-91
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 92-92

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown9016(1)
    sprite('yo207_01', 11)	# 1-11
    sprite('yo207_02', 3)	# 12-14
    SFX_3('slash_knife_middle')
    sprite('yo207_04', 3)	# 15-17	 **attackbox here**
    Unknown23054('796f3230375f303300000000000000000000000000000000000000000000000006000000')
    RefreshMultihit()
    sprite('yo207_04', 6)	# 18-23	 **attackbox here**
    Unknown23027()
    sprite('yo207_05', 6)	# 24-29
    sprite('yo207_06', 6)	# 30-35
    sprite('yo207_07', 6)	# 36-41
    label(0)
    sprite('yo000_00', 6)	# 42-47
    sprite('yo000_01', 6)	# 48-53
    sprite('yo000_02', 6)	# 54-59
    sprite('yo000_03', 6)	# 60-65
    sprite('yo000_04', 6)	# 66-71
    sprite('yo000_05', 6)	# 72-77
    sprite('yo000_06', 6)	# 78-83
    sprite('yo000_07', 6)	# 84-89
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 90-90

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('yo204_00', 11)	# 1-11
    Unknown2017(0)
    sprite('yo204_01', 4)	# 12-15
    Unknown23029(11, 104, 0)
    Unknown4020(11)
    sprite('yo204_02', 3)	# 16-18
    tag_voice(0, 'pyo158_0', 'pyo158_1', '', '')
    sprite('yo204_03', 3)	# 19-21
    GFX_1('persona_enter_ply', 0)
    sprite('yo204_04', 3)	# 22-24
    Unknown4020(0)
    sprite('yo204_05', 3)	# 25-27
    sprite('yo204_06', 3)	# 28-30
    sprite('yo204_04', 3)	# 31-33
    sprite('yo204_05', 3)	# 34-36
    sprite('yo204_06', 3)	# 37-39
    sprite('yo204_04', 3)	# 40-42
    sprite('yo204_05', 3)	# 43-45
    sprite('yo204_06', 3)	# 46-48
    Unknown2017(1)
    sprite('yo204_02', 4)	# 49-52
    sprite('yo204_01', 4)	# 53-56
    sprite('yo204_00', 4)	# 57-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 26)	# 1-26
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 27-27
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('yo407_01', 2)	# 28-29
    StartMultihit()
    SFX_3('airdash_l')
    SFX_3('slash_pole_middle')
    physicsXImpulse(7500)
    physicsYImpulse(-6500)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(0)
    sprite('yo407_02', 10)	# 30-39
    physicsXImpulse(50000)
    physicsYImpulse(-39000)
    sprite('yo407_02', 2)	# 40-41
    SFX_3('airdash_m')
    SFX_3('slash_rapier_middle')
    sprite('yo407_03', 1)	# 42-42	 **attackbox here**
    RefreshMultihit()
    sprite('yo407_03', 3)	# 43-45	 **attackbox here**
    StartMultihit()
    SFX_3('slash_blade_slow')
    sprite('yo407_04', 3)	# 46-48	 **attackbox here**
    sprite('yo407_05', 3)	# 49-51	 **attackbox here**
    label(1)
    sprite('yo407_03', 3)	# 52-54	 **attackbox here**
    StartMultihit()
    sprite('yo407_04', 3)	# 55-57	 **attackbox here**
    StartMultihit()
    sprite('yo407_05', 3)	# 58-60	 **attackbox here**
    StartMultihit()
    gotoLabel(1)
    label(0)
    sprite('yo407_06', 4)	# 61-64
    clearUponHandler(2)
    Unknown8004(100, 1, 1)
    Unknown1084(1)
    sprite('yo231_00', 3)	# 65-67
    sprite('yo231_01', 3)	# 68-70
    sprite('yo000_00', 6)	# 71-76
    sprite('yo000_01', 6)	# 77-82
    sprite('yo000_02', 6)	# 83-88
    sprite('yo000_03', 6)	# 89-94
    sprite('yo000_04', 6)	# 95-100
    sprite('yo000_05', 6)	# 101-106
    sprite('yo000_06', 6)	# 107-112
    sprite('yo000_07', 6)	# 113-118
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('yo201_00', 2)	# 1-2
    sprite('yo201_01', 3)	# 3-5
    sprite('yo201_02', 3)	# 6-8
    sprite('yo201_03', 3)	# 9-11
    SFX_3('slash_knife_middle')
    sprite('yo201_06', 4)	# 12-15	 **attackbox here**
    Unknown23054('796f3230315f303400000000000000000000000000000000000000000000000004000000')
    RefreshMultihit()
    sprite('yo201_06', 6)	# 16-21	 **attackbox here**
    sprite('yo201_07', 6)	# 22-27
    sprite('yo201_08', 6)	# 28-33
    sprite('yo201_09', 6)	# 34-39
    loopRest()
    sprite('yo000_00', 6)	# 40-45
    sprite('yo000_01', 6)	# 46-51
    sprite('yo000_02', 6)	# 52-57
    sprite('yo000_03', 6)	# 58-63
    sprite('yo000_04', 6)	# 64-69
    sprite('yo000_05', 6)	# 70-75
    sprite('yo000_06', 6)	# 76-81
    sprite('yo000_07', 6)	# 82-87
    loopRest()

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('yo204_00', 11)	# 1-11
    Unknown2017(0)
    sprite('yo204_01', 4)	# 12-15
    Unknown23029(11, 104, 0)
    Unknown4020(11)
    sprite('yo204_02', 3)	# 16-18
    sprite('yo204_03', 3)	# 19-21
    GFX_1('persona_enter_ply', 0)
    sprite('yo204_04', 3)	# 22-24
    Unknown4020(0)
    sprite('yo204_05', 3)	# 25-27
    sprite('yo204_06', 3)	# 28-30
    sprite('yo204_04', 3)	# 31-33
    sprite('yo204_05', 3)	# 34-36
    sprite('yo204_06', 3)	# 37-39
    sprite('yo204_04', 3)	# 40-42
    sprite('yo204_05', 3)	# 43-45
    sprite('yo204_06', 3)	# 46-48
    Unknown2017(1)
    sprite('yo204_02', 4)	# 49-52
    sprite('yo204_01', 4)	# 53-56
    sprite('yo204_00', 4)	# 57-60

@Subroutine
def MouthTableInit():
    Unknown18011('pyo000', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo293_0', 12643, 13409, 13411, 14177, 14691, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo293_1', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo500', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo501', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24888, 25397, 24885, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo502', 12899, 24885, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo503', 14179, 24880, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo504_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo504_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo505_0', 12643, 14177, 14179, 13921, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo505_1', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo506', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo507', 12643, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo508', 14691, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo509', 14691, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo520', 14177, 14179, 12641, 25394, 12340, 13409, 13411, 13409, 13411, 24880, 24887, 25399, 24887, 25399, 24887, 25399, 12849, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo521', 14177, 14179, 14177, 14179, 14177, 13411, 24885, 25397, 24885, 25397, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo522', 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 25399, 24887, 12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo523', 12641, 25392, 12342, 14689, 14691, 14177, 14179, 13921, 13923, 13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo524', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo525', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo403_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo403_1', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600bhz', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600bjn', 12643, 12641, 25396, 12338, 14177, 12643, 24880, 25399, 12339, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600bph', 12643, 14177, 14179, 12641, 25396, 12339, 13665, 13667, 13665, 12643, 24888, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600bpt', 12643, 13409, 13411, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25393, 24887, 12593, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600pbc', 12643, 12641, 25396, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13105, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600pka', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600ryn', 12643, 13665, 13667, 13665, 12643, 24884, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo600uli', 12643, 13409, 13411, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13106, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo601bes', 12643, 13409, 13411, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo601bmk', 12643, 14177, 12643, 24887, 13362, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo601pce', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo601uyu', 12643, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo602bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo602bpt', 12643, 14177, 12643, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo700bes', 12643, 14177, 14179, 12641, 25396, 14131, 12641, 25392, 12339, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo700bhz', 12643, 14177, 14179, 12641, 25392, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo700bmk', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo700pbc', 12643, 13409, 13411, 12641, 25394, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo700pce', 12643, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo700uli', 12643, 12641, 25394, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo700uyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo701bjn', 12643, 12641, 25396, 12338, 14177, 12643, 24882, 25396, 24884, 25399, 14132, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo701bph', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo701bpt', 12643, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo701pka', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo701pka_a', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 12899, 24882, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo701ryn', 12643, 13665, 13667, 12641, 25396, 24887, 25397, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo702bes', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo702bhz', 12643, 13409, 13411, 13409, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyo702uli', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bjn')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bhz')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('uyu')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(200)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(210)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 25)
    if SLOT_0:
        _gotolabel(10)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(20)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(30)
    sprite('yo600_00', 30)	# 2-31
    Unknown3001(0)
    GFX_0('Entry_wind', 0)
    sprite('yo600_00', 4)	# 32-35
    Unknown3001(255)
    sprite('yo600_01', 4)	# 36-39
    if SLOT_158:
        Unknown7006('pyo500', 100, 896498032, 12592, 0, 0, 100, 896498032, 13872, 0, 0, 100, 896498032, 14128, 0, 0, 100)
    sprite('yo600_02', 4)	# 40-43
    SFX_3('cloth_l')
    label(1)
    sprite('yo600_00', 6)	# 44-49
    sprite('yo600_01', 6)	# 50-55
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 56-61
    sprite('yo600_00', 8)	# 62-69
    sprite('yo600_01', 8)	# 70-77
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 78-85
    if SLOT_97:
        _gotolabel(1)
    sprite('yo600_03', 3)	# 86-88
    sprite('yo600_04', 3)	# 89-91
    sprite('yo600_05', 6)	# 92-97
    sprite('yo600_06', 2)	# 98-99
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 100-101
    sprite('yo600_08', 2)	# 102-103
    sprite('yo600_09', 18)	# 104-121
    sprite('yo600_10', 6)	# 122-127
    loopRest()
    ExitState()
    label(10)
    sprite('yo601_00', 12)	# 128-139
    teleportRelativeY(510000)
    setGravity(2000)
    physicsYImpulse(-10000)
    sprite('yo601_01', 5)	# 140-144
    sprite('yo601_02', 10)	# 145-154
    if random_(2, 0, 50):
        SFX_1('pyo502')
        SLOT_51 = 1
    else:
        SFX_1('pyo503')
    Unknown1084(1)
    sprite('yo601_03', 15)	# 155-169
    SFX_3('wring_string')
    sprite('yo601_04', 5)	# 170-174
    sprite('yo601_05', 5)	# 175-179
    sprite('yo601_06', 5)	# 180-184
    sprite('yo601_07', 5)	# 185-189
    sprite('yo601_08', 5)	# 190-194
    sprite('yo601_09', 5)	# 195-199
    sprite('yo601_10', 5)	# 200-204
    sprite('yo601_11', 5)	# 205-209
    sprite('yo601_12', 5)	# 210-214
    sprite('yo601_13', 80)	# 215-294
    GFX_0('Entry_2', 0)
    sprite('yo601_13', 30)	# 295-324
    if SLOT_51:
        sendToLabel(12)
    label(12)
    sprite('yo601_14', 3)	# 325-327
    GFX_0('Entry_2rope_ex00', 100)
    setGravity(2000)
    sendToLabelUpon(2, 11)
    SFX_3('grip_fast')
    sprite('yo601_15', 3)	# 328-330
    sprite('yo601_16', 3)	# 331-333
    sprite('yo601_17', 3)	# 334-336
    sprite('yo601_16', 3)	# 337-339
    sprite('yo601_17', 3)	# 340-342
    sprite('yo601_16', 3)	# 343-345
    sprite('yo601_17', 3)	# 346-348
    sprite('yo601_16', 3)	# 349-351
    sprite('yo601_17', 3)	# 352-354
    label(11)
    sprite('yo060_08', 3)	# 355-357
    GFX_1('yoef_entry2_bound', 100)
    ScreenShake(10000, 0)
    GFX_0('Entry_2rope_ex01', 100)
    Unknown21011(120)
    sprite('yo060_09', 3)	# 358-360
    sprite('yo060_10', 3)	# 361-363
    sprite('yo060_11', 3)	# 364-366
    sprite('yo060_12', 30)	# 367-396
    sprite('yo064_00', 4)	# 397-400
    sprite('yo064_01', 4)	# 401-404
    sprite('yo064_02', 4)	# 405-408
    sprite('yo064_03', 4)	# 409-412
    sprite('yo010_02', 3)	# 413-415
    sprite('yo010_01', 3)	# 416-418
    sprite('yo010_00', 3)	# 419-421
    loopRest()
    ExitState()
    label(20)
    sprite('yo602_00', 80)	# 422-501

    def upon_3():
        Unknown2053(0)
    Unknown1000(0)
    Unknown2034(0)
    Unknown2019(-100)
    SFX_1('pyo505_0')
    sprite('yo602_00', 12)	# 502-513
    physicsXImpulse(-40000)
    SFX_3('yo007')
    sprite('yo602_01', 6)	# 514-519
    sprite('yo602_00', 6)	# 520-525
    sprite('yo602_01', 6)	# 526-531
    sprite('yo602_00', 6)	# 532-537
    sprite('yo602_01', 6)	# 538-543
    sprite('yo602_00', 6)	# 544-549
    sprite('yo602_01', 6)	# 550-555
    sprite('yo602_00', 6)	# 556-561
    sprite('yo602_01', 6)	# 562-567
    sprite('yo602_00', 6)	# 568-573
    sprite('yo602_01', 6)	# 574-579
    sprite('yo602_00', 6)	# 580-585
    Unknown1084(1)
    ScreenShake(0, 20000)
    GFX_0('Entry_clashsmoke', 100)
    SFX_3('damage_hit_mh')
    SFX_1('yo508')
    sprite('yo602_02ex', 67)	# 586-652
    Unknown1000(-2210000)
    teleportRelativeY(100000)
    physicsXImpulse(14626)
    physicsYImpulse(50000)
    setGravity(1500)
    Unknown1074(15750)
    sprite('yo602_02', 60)	# 653-712
    clearUponHandler(3)
    SFX_3('hit_h_fast')
    Unknown1000(-1230000)
    Unknown1084(0)
    Unknown1074(0)
    Unknown1072(0)
    teleportRelativeY(0)
    sprite('yo602_02', 2)	# 713-714
    Unknown1072(-3000)
    if random_(2, 0, 50):
        SFX_1('pyo508')
    else:
        SFX_1('pyo509')
    Unknown23018(1)
    sprite('yo602_02', 2)	# 715-716
    Unknown1072(0)
    sprite('yo602_02', 2)	# 717-718
    Unknown1072(3000)
    sprite('yo602_02', 2)	# 719-720
    Unknown1072(0)
    sprite('yo602_02', 2)	# 721-722
    Unknown1072(-3000)
    sprite('yo602_02', 2)	# 723-724
    Unknown1072(0)
    sprite('yo602_02', 2)	# 725-726
    Unknown1072(3000)
    sprite('yo602_02', 2)	# 727-728
    Unknown1072(0)
    sprite('yo602_02', 2)	# 729-730
    Unknown1072(-3000)
    sprite('yo602_02', 2)	# 731-732
    Unknown1072(0)
    sprite('yo602_02', 2)	# 733-734
    Unknown1072(3000)
    sprite('yo602_02', 2)	# 735-736
    Unknown1072(0)
    sprite('yo602_02', 2)	# 737-738
    Unknown1072(-3000)
    sprite('yo602_02', 2)	# 739-740
    Unknown1072(0)
    sprite('yo602_02', 60)	# 741-800
    Unknown1072(0)
    sprite('yo602_03', 3)	# 801-803
    Unknown21007(24, 41)
    sprite('yo602_04', 3)	# 804-806
    SFX_3('hit_m_slow')
    sprite('yo602_05', 3)	# 807-809
    sprite('yo602_06', 3)	# 810-812
    sprite('yo602_07', 3)	# 813-815
    sprite('yo602_08', 6)	# 816-821
    GFX_0('yoef_baketsu', 0)
    sprite('yo602_09', 8)	# 822-829
    sprite('yo600_00', 8)	# 830-837
    sprite('yo600_01', 8)	# 838-845
    sprite('yo600_02', 8)	# 846-853
    sprite('yo600_03', 3)	# 854-856
    sprite('yo600_04', 3)	# 857-859
    sprite('yo600_05', 6)	# 860-865
    sprite('yo600_06', 2)	# 866-867
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 868-869
    sprite('yo600_08', 2)	# 870-871
    sprite('yo600_09', 18)	# 872-889
    sprite('yo600_10', 6)	# 890-895
    label(21)
    sprite('yo000_00', 6)	# 896-901
    sprite('yo000_01', 6)	# 902-907
    sprite('yo000_02', 6)	# 908-913
    sprite('yo000_03', 6)	# 914-919
    sprite('yo000_04', 6)	# 920-925
    sprite('yo000_05', 6)	# 926-931
    sprite('yo000_06', 6)	# 932-937
    sprite('yo000_07', 6)	# 938-943
    gotoLabel(21)
    ExitState()
    label(30)
    sprite('yo602_00', 110)	# 944-1053

    def upon_3():
        Unknown2053(0)
    Unknown1000(0)
    Unknown2034(0)
    SFX_1('pyo504_0')
    sprite('yo602_00', 6)	# 1054-1059
    physicsXImpulse(-40000)
    SFX_3('yo007')
    sprite('yo602_01', 6)	# 1060-1065
    sprite('yo602_00', 6)	# 1066-1071
    sprite('yo602_01', 6)	# 1072-1077
    sprite('yo602_00', 6)	# 1078-1083
    sprite('yo602_01', 6)	# 1084-1089
    sprite('yo602_00', 6)	# 1090-1095
    sprite('yo602_01', 6)	# 1096-1101
    sprite('yo602_00', 6)	# 1102-1107
    sprite('yo602_01', 6)	# 1108-1113
    sprite('yo602_00', 6)	# 1114-1119
    sprite('yo602_01', 46)	# 1120-1165
    sprite('yo602_00', 6)	# 1166-1171
    Unknown1084(1)
    ScreenShake(0, 20000)
    GFX_0('Entry_clashsmoke', 100)
    SFX_3('damage_hit_mh')
    sprite('null', 80)	# 1172-1251
    Unknown1000(-2210000)
    sprite('null', 10)	# 1252-1261
    sprite('yo032_01', 3)	# 1262-1264
    physicsXImpulse(49000)
    if random_(2, 0, 50):
        SFX_1('pyo504_1')
    else:
        SFX_1('pyo505_1')
    Unknown23018(1)
    sprite('yo032_02', 3)	# 1265-1267
    sprite('yo032_03', 3)	# 1268-1270
    sprite('yo032_04', 3)	# 1271-1273
    sprite('yo032_05', 3)	# 1274-1276
    Unknown21007(24, 41)
    Unknown8006(100, 1, 1)
    sprite('yo032_09', 1)	# 1277-1277
    Unknown1019(88)
    sprite('yo032_09', 1)	# 1278-1278
    Unknown1019(88)
    sprite('yo032_09', 1)	# 1279-1279
    Unknown1019(88)
    sprite('yo032_09', 1)	# 1280-1280
    Unknown1019(80)
    sprite('yo032_09', 1)	# 1281-1281
    Unknown1019(80)
    sprite('yo032_09', 1)	# 1282-1282
    Unknown1019(80)
    sprite('yo032_09', 1)	# 1283-1283
    Unknown1019(80)
    sprite('yo032_09', 1)	# 1284-1284
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1285-1285
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1286-1286
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1287-1287
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1288-1288
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1289-1289
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1290-1290
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1291-1291
    Unknown1019(80)
    sprite('yo032_10', 1)	# 1292-1292
    Unknown1019(0)
    Unknown1000(-1230000)
    label(31)
    sprite('yo000_00', 6)	# 1293-1298
    sprite('yo000_01', 6)	# 1299-1304
    sprite('yo000_02', 6)	# 1305-1310
    sprite('yo000_03', 6)	# 1311-1316
    sprite('yo000_04', 6)	# 1317-1322
    sprite('yo000_05', 6)	# 1323-1328
    sprite('yo000_06', 6)	# 1329-1334
    sprite('yo000_07', 6)	# 1335-1340
    gotoLabel(31)
    ExitState()
    label(40)
    sprite('yo000_00', 1)	# 1341-1341
    SFX_1('pyo701ryn')
    label(41)
    sprite('yo000_00', 6)	# 1342-1347
    sprite('yo000_01', 6)	# 1348-1353
    sprite('yo000_02', 6)	# 1354-1359
    sprite('yo000_03', 6)	# 1360-1365
    sprite('yo000_04', 6)	# 1366-1371
    sprite('yo000_05', 6)	# 1372-1377
    sprite('yo000_06', 6)	# 1378-1383
    sprite('yo000_07', 6)	# 1384-1389
    gotoLabel(41)
    label(100)
    sprite('yo600_00', 4)	# 1390-1393
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1495000)
    sprite('yo600_01', 4)	# 1394-1397
    SFX_1('pyo600bjn')
    sprite('yo600_02', 4)	# 1398-1401
    SFX_3('cloth_l')
    label(101)
    sprite('yo600_00', 6)	# 1402-1407
    sprite('yo600_01', 6)	# 1408-1413
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 1414-1419
    sprite('yo600_00', 8)	# 1420-1427
    sprite('yo600_01', 8)	# 1428-1435
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 1436-1443
    if SLOT_97:
        _gotolabel(101)
    sprite('yo600_03', 3)	# 1444-1446
    sprite('yo600_04', 3)	# 1447-1449
    sprite('yo600_05', 6)	# 1450-1455
    sprite('yo600_06', 2)	# 1456-1457
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 1458-1459
    Unknown21007(24, 40)
    sprite('yo600_08', 2)	# 1460-1461
    sprite('yo600_09', 18)	# 1462-1479
    sprite('yo600_10', 6)	# 1480-1485
    Unknown21011(180)
    label(102)
    sprite('yo000_00', 6)	# 1486-1491
    sprite('yo000_01', 6)	# 1492-1497
    sprite('yo000_02', 6)	# 1498-1503
    sprite('yo000_03', 6)	# 1504-1509
    sprite('yo000_04', 6)	# 1510-1515
    sprite('yo000_05', 6)	# 1516-1521
    sprite('yo000_06', 6)	# 1522-1527
    sprite('yo000_07', 6)	# 1528-1533
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('yo600_00', 4)	# 1534-1537
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('yo600_01', 4)	# 1538-1541
    SFX_1('pyo600bhz')
    sprite('yo600_02', 4)	# 1542-1545

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
        SFX_1('pyo602bhz')
        Unknown23018(1)
    Unknown2037(4)
    SFX_3('cloth_l')
    label(111)
    sprite('yo600_00', 6)	# 1546-1551
    sprite('yo600_01', 6)	# 1552-1557
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 1558-1563
    sprite('yo600_00', 8)	# 1564-1571
    sprite('yo600_01', 8)	# 1572-1579
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 1580-1587
    Unknown2038(-1)
    if (not SLOT_2):
        Unknown21007(24, 40)
    gotoLabel(111)
    label(112)
    sprite('yo600_03', 3)	# 1588-1590
    sprite('yo600_04', 3)	# 1591-1593
    sprite('yo600_05', 6)	# 1594-1599
    sprite('yo600_06', 2)	# 1600-1601
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 1602-1603
    sprite('yo600_08', 2)	# 1604-1605
    sprite('yo600_09', 18)	# 1606-1623
    sprite('yo600_10', 6)	# 1624-1629
    Unknown21011(120)
    label(113)
    sprite('yo000_00', 6)	# 1630-1635
    sprite('yo000_01', 6)	# 1636-1641
    sprite('yo000_02', 6)	# 1642-1647
    sprite('yo000_03', 6)	# 1648-1653
    sprite('yo000_04', 6)	# 1654-1659
    sprite('yo000_05', 6)	# 1660-1665
    sprite('yo000_06', 6)	# 1666-1671
    sprite('yo000_07', 6)	# 1672-1677
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('yo600_00', 4)	# 1678-1681
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('yo600_01', 4)	# 1682-1685
    SFX_1('pyo600bpt')
    sprite('yo600_02', 4)	# 1686-1689
    SFX_3('cloth_l')
    label(121)
    sprite('yo600_00', 6)	# 1690-1695
    sprite('yo600_01', 6)	# 1696-1701
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 1702-1707
    sprite('yo600_00', 8)	# 1708-1715
    sprite('yo600_01', 8)	# 1716-1723
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 1724-1731
    if SLOT_97:
        _gotolabel(121)
    sprite('yo600_03', 3)	# 1732-1734
    sprite('yo600_04', 3)	# 1735-1737
    sprite('yo600_05', 6)	# 1738-1743
    sprite('yo600_06', 2)	# 1744-1745
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 1746-1747
    sprite('yo600_08', 2)	# 1748-1749
    sprite('yo600_09', 18)	# 1750-1767
    sprite('yo600_10', 6)	# 1768-1773

    def upon_40():
        clearUponHandler(40)
        sendToLabel(123)
        SFX_1('pyo602bpt')
        Unknown23018(1)
    Unknown21007(24, 40)
    label(122)
    sprite('yo000_00', 6)	# 1774-1779
    sprite('yo000_01', 6)	# 1780-1785
    sprite('yo000_02', 6)	# 1786-1791
    sprite('yo000_03', 6)	# 1792-1797
    sprite('yo000_04', 6)	# 1798-1803
    sprite('yo000_05', 6)	# 1804-1809
    sprite('yo000_06', 6)	# 1810-1815
    sprite('yo000_07', 6)	# 1816-1821
    gotoLabel(122)
    label(123)
    sprite('yo070_00', 2)	# 1822-1823
    if SLOT_158:
        Unknown2005()
    label(124)
    sprite('yo070_00', 2)	# 1824-1825
    teleportRelativeX(-2000)
    sprite('yo070_00', 2)	# 1826-1827
    teleportRelativeX(2000)
    gotoLabel(124)
    ExitState()
    label(130)
    sprite('yo600_00', 1)	# 1828-1828
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('yo600_00', 6)	# 1829-1834
    sprite('yo600_01', 6)	# 1835-1840
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 1841-1846
    sprite('yo600_00', 8)	# 1847-1854
    sprite('yo600_01', 8)	# 1855-1862
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 1863-1870
    gotoLabel(131)
    label(132)
    sprite('yo600_00', 6)	# 1871-1876
    sprite('yo600_01', 6)	# 1877-1882
    SFX_1('pyo601bes')
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 1883-1888
    label(133)
    sprite('yo600_00', 8)	# 1889-1896
    sprite('yo600_01', 8)	# 1897-1904
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 1905-1912
    if SLOT_97:
        _gotolabel(133)
    sprite('yo600_03', 3)	# 1913-1915
    sprite('yo600_04', 3)	# 1916-1918
    sprite('yo600_05', 6)	# 1919-1924
    sprite('yo600_06', 2)	# 1925-1926
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 1927-1928
    sprite('yo600_08', 2)	# 1929-1930
    sprite('yo600_09', 18)	# 1931-1948
    sprite('yo600_10', 6)	# 1949-1954
    Unknown21011(120)
    label(134)
    sprite('yo000_00', 6)	# 1955-1960
    sprite('yo000_01', 6)	# 1961-1966
    sprite('yo000_02', 6)	# 1967-1972
    sprite('yo000_03', 6)	# 1973-1978
    sprite('yo000_04', 6)	# 1979-1984
    sprite('yo000_05', 6)	# 1985-1990
    sprite('yo000_06', 6)	# 1991-1996
    sprite('yo000_07', 6)	# 1997-2002
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('yo600_00', 1)	# 2003-2003
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('yo600_00', 6)	# 2004-2009
    sprite('yo600_01', 6)	# 2010-2015
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 2016-2021
    sprite('yo600_00', 8)	# 2022-2029
    sprite('yo600_01', 8)	# 2030-2037
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 2038-2045
    gotoLabel(141)
    label(142)
    sprite('yo600_00', 6)	# 2046-2051
    sprite('yo600_01', 6)	# 2052-2057
    SFX_1('pyo601pce')
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 2058-2063
    label(143)
    sprite('yo600_00', 8)	# 2064-2071
    sprite('yo600_01', 8)	# 2072-2079
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 2080-2087
    if SLOT_97:
        _gotolabel(143)
    sprite('yo600_03', 3)	# 2088-2090
    sprite('yo600_04', 3)	# 2091-2093
    sprite('yo600_05', 6)	# 2094-2099
    sprite('yo600_06', 2)	# 2100-2101
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 2102-2103
    sprite('yo600_08', 2)	# 2104-2105
    sprite('yo600_09', 18)	# 2106-2123
    sprite('yo600_10', 6)	# 2124-2129
    Unknown21011(120)
    label(144)
    sprite('yo000_00', 6)	# 2130-2135
    sprite('yo000_01', 6)	# 2136-2141
    sprite('yo000_02', 6)	# 2142-2147
    sprite('yo000_03', 6)	# 2148-2153
    sprite('yo000_04', 6)	# 2154-2159
    sprite('yo000_05', 6)	# 2160-2165
    sprite('yo000_06', 6)	# 2166-2171
    sprite('yo000_07', 6)	# 2172-2177
    gotoLabel(144)
    ExitState()
    label(150)
    sprite('yo600_00', 30)	# 2178-2207
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3001(0)
    GFX_0('Entry_wind', 0)
    sprite('yo600_00', 4)	# 2208-2211
    Unknown3001(255)
    sprite('yo600_01', 4)	# 2212-2215
    SFX_1('pyo600uli')
    sprite('yo600_02', 4)	# 2216-2219
    SFX_3('cloth_l')
    label(151)
    sprite('yo600_00', 6)	# 2220-2225
    sprite('yo600_01', 6)	# 2226-2231
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 2232-2237
    sprite('yo600_00', 8)	# 2238-2245
    sprite('yo600_01', 8)	# 2246-2253
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 2254-2261
    if SLOT_97:
        _gotolabel(151)
    sprite('yo600_03', 3)	# 2262-2264
    sprite('yo600_04', 3)	# 2265-2267
    sprite('yo600_05', 6)	# 2268-2273
    sprite('yo600_06', 2)	# 2274-2275
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 2276-2277
    sprite('yo600_08', 2)	# 2278-2279
    sprite('yo600_09', 18)	# 2280-2297
    sprite('yo600_10', 6)	# 2298-2303
    Unknown21007(24, 40)
    Unknown21011(60)
    label(152)
    sprite('yo000_00', 6)	# 2304-2309
    sprite('yo000_01', 6)	# 2310-2315
    sprite('yo000_02', 6)	# 2316-2321
    sprite('yo000_03', 6)	# 2322-2327
    sprite('yo000_04', 6)	# 2328-2333
    sprite('yo000_05', 6)	# 2334-2339
    sprite('yo000_06', 6)	# 2340-2345
    sprite('yo000_07', 6)	# 2346-2351
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('yo635_00', 1)	# 2352-2352
    Unknown2019(-100)
    if SLOT_158:
        Unknown1000(-1360000)
    else:
        Unknown1000(-1360000)
    SFX_1('pyo600pbc')
    label(161)
    sprite('yo635_00', 1)	# 2353-2353
    if SLOT_97:
        _gotolabel(161)
    sprite('yo635_00', 50)	# 2354-2403
    Unknown21007(24, 40)
    sprite('yo635_01', 6)	# 2404-2409
    sprite('yo635_02', 6)	# 2410-2415
    sprite('yo635_03', 6)	# 2416-2421
    sprite('yo635_04', 30)	# 2422-2451
    sprite('yo635_05', 6)	# 2452-2457
    sprite('yo635_06', 6)	# 2458-2463
    sprite('yo635_07', 6)	# 2464-2469
    Unknown21011(120)
    sprite('yo635_08', 32767)	# 2470-35236
    ExitState()
    label(170)
    sprite('yo600_00', 1)	# 35237-35237
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('yo600_00', 6)	# 35238-35243
    sprite('yo600_01', 6)	# 35244-35249
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 35250-35255
    sprite('yo600_00', 8)	# 35256-35263
    sprite('yo600_01', 8)	# 35264-35271
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 35272-35279
    gotoLabel(171)
    label(172)
    sprite('yo600_00', 6)	# 35280-35285
    sprite('yo600_01', 6)	# 35286-35291
    SFX_1('pyo601bmk')
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 35292-35297
    label(173)
    sprite('yo600_00', 8)	# 35298-35305
    sprite('yo600_01', 8)	# 35306-35313
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 35314-35321
    if SLOT_97:
        _gotolabel(173)
    sprite('yo600_03', 3)	# 35322-35324
    sprite('yo600_04', 3)	# 35325-35327
    sprite('yo600_05', 6)	# 35328-35333
    sprite('yo600_06', 2)	# 35334-35335
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 35336-35337
    sprite('yo600_08', 2)	# 35338-35339
    sprite('yo600_09', 18)	# 35340-35357
    sprite('yo600_10', 6)	# 35358-35363
    Unknown21011(60)
    label(174)
    sprite('yo000_00', 6)	# 35364-35369
    sprite('yo000_01', 6)	# 35370-35375
    sprite('yo000_02', 6)	# 35376-35381
    sprite('yo000_03', 6)	# 35382-35387
    sprite('yo000_04', 6)	# 35388-35393
    sprite('yo000_05', 6)	# 35394-35399
    sprite('yo000_06', 6)	# 35400-35405
    sprite('yo000_07', 6)	# 35406-35411
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('yo600_00', 30)	# 35412-35441
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3001(0)
    GFX_0('Entry_wind', 0)
    sprite('yo600_00', 4)	# 35442-35445
    Unknown3001(255)
    sprite('yo600_01', 4)	# 35446-35449
    SFX_1('pyo600pka')
    sprite('yo600_02', 4)	# 35450-35453
    SFX_3('cloth_l')
    label(181)
    sprite('yo600_00', 6)	# 35454-35459
    sprite('yo600_01', 6)	# 35460-35465
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 35466-35471
    sprite('yo600_00', 8)	# 35472-35479
    sprite('yo600_01', 8)	# 35480-35487
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 35488-35495
    if SLOT_97:
        _gotolabel(181)
    sprite('yo600_03', 3)	# 35496-35498
    sprite('yo600_04', 3)	# 35499-35501
    sprite('yo600_05', 6)	# 35502-35507
    sprite('yo600_06', 2)	# 35508-35509
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 35510-35511
    sprite('yo600_08', 2)	# 35512-35513
    sprite('yo600_09', 18)	# 35514-35531
    sprite('yo600_10', 6)	# 35532-35537
    Unknown21007(24, 40)
    Unknown21011(120)
    label(182)
    sprite('yo000_00', 6)	# 35538-35543
    sprite('yo000_01', 6)	# 35544-35549
    sprite('yo000_02', 6)	# 35550-35555
    sprite('yo000_03', 6)	# 35556-35561
    sprite('yo000_04', 6)	# 35562-35567
    sprite('yo000_05', 6)	# 35568-35573
    sprite('yo000_06', 6)	# 35574-35579
    sprite('yo000_07', 6)	# 35580-35585
    gotoLabel(182)
    ExitState()
    label(190)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('yo600_00', 6)	# 35586-35591
    sprite('yo600_01', 6)	# 35592-35597
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 35598-35603
    sprite('yo600_00', 8)	# 35604-35611
    sprite('yo600_01', 8)	# 35612-35619
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 35620-35627
    gotoLabel(191)
    label(192)
    sprite('yo600_00', 6)	# 35628-35633
    sprite('yo600_01', 6)	# 35634-35639
    SFX_1('pyo601uyu')
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 35640-35645
    label(193)
    sprite('yo600_00', 8)	# 35646-35653
    sprite('yo600_01', 8)	# 35654-35661
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 35662-35669
    if SLOT_97:
        _gotolabel(193)
    sprite('yo600_03', 3)	# 35670-35672
    sprite('yo600_04', 3)	# 35673-35675
    sprite('yo600_05', 6)	# 35676-35681
    sprite('yo600_06', 2)	# 35682-35683
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 35684-35685
    sprite('yo600_08', 2)	# 35686-35687
    sprite('yo600_09', 18)	# 35688-35705
    sprite('yo600_10', 6)	# 35706-35711
    Unknown23018(1)
    label(194)
    sprite('yo000_00', 6)	# 35712-35717
    sprite('yo000_01', 6)	# 35718-35723
    sprite('yo000_02', 6)	# 35724-35729
    sprite('yo000_03', 6)	# 35730-35735
    sprite('yo000_04', 6)	# 35736-35741
    sprite('yo000_05', 6)	# 35742-35747
    sprite('yo000_06', 6)	# 35748-35753
    sprite('yo000_07', 6)	# 35754-35759
    gotoLabel(194)
    ExitState()
    label(200)
    sprite('yo602_02ex', 67)	# 35760-35826
    Unknown1000(-2210000)
    teleportRelativeY(100000)
    physicsXImpulse(14626)
    physicsYImpulse(50000)
    setGravity(1500)
    Unknown1074(15750)
    Unknown2034(0)
    Unknown2053(0)
    sprite('yo602_02', 20)	# 35827-35846
    clearUponHandler(3)
    SFX_3('hit_h_fast')
    Unknown1000(-1230000)
    Unknown1084(0)
    Unknown1074(0)
    Unknown1072(0)
    teleportRelativeY(0)
    SFX_1('pyo600ryn')
    sprite('yo602_02', 2)	# 35847-35848
    Unknown1072(-3000)
    sprite('yo602_02', 2)	# 35849-35850
    Unknown1072(0)
    sprite('yo602_02', 2)	# 35851-35852
    Unknown1072(3000)
    sprite('yo602_02', 2)	# 35853-35854
    Unknown1072(0)
    sprite('yo602_02', 2)	# 35855-35856
    Unknown1072(-3000)
    sprite('yo602_02', 2)	# 35857-35858
    Unknown1072(0)
    sprite('yo602_02', 2)	# 35859-35860
    Unknown1072(3000)
    sprite('yo602_02', 2)	# 35861-35862
    Unknown1072(0)
    sprite('yo602_02', 2)	# 35863-35864
    Unknown1072(-3000)
    sprite('yo602_02', 2)	# 35865-35866
    Unknown1072(0)
    sprite('yo602_02', 2)	# 35867-35868
    Unknown1072(3000)
    sprite('yo602_02', 2)	# 35869-35870
    Unknown1072(0)
    sprite('yo602_02', 2)	# 35871-35872
    Unknown1072(-3000)
    sprite('yo602_02', 2)	# 35873-35874
    Unknown1072(0)
    sprite('yo602_02', 20)	# 35875-35894
    Unknown1072(0)
    sprite('yo602_03', 3)	# 35895-35897
    sprite('yo602_04', 3)	# 35898-35900
    SFX_3('hit_m_slow')
    sprite('yo602_05', 3)	# 35901-35903
    sprite('yo602_06', 3)	# 35904-35906
    sprite('yo602_07', 3)	# 35907-35909
    sprite('yo602_08', 6)	# 35910-35915
    GFX_0('yoef_baketsu', 0)
    sprite('yo602_09', 8)	# 35916-35923
    sprite('yo600_00', 8)	# 35924-35931
    sprite('yo600_01', 8)	# 35932-35939
    sprite('yo600_02', 8)	# 35940-35947
    sprite('yo600_03', 3)	# 35948-35950
    sprite('yo600_04', 3)	# 35951-35953
    sprite('yo600_05', 6)	# 35954-35959
    sprite('yo600_06', 2)	# 35960-35961
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 35962-35963
    sprite('yo600_08', 2)	# 35964-35965
    sprite('yo600_09', 18)	# 35966-35983
    sprite('yo600_10', 6)	# 35984-35989
    Unknown21011(200)
    label(201)
    sprite('yo000_00', 6)	# 35990-35995
    sprite('yo000_01', 6)	# 35996-36001
    sprite('yo000_02', 6)	# 36002-36007
    sprite('yo000_03', 6)	# 36008-36013
    sprite('yo000_04', 6)	# 36014-36019
    Unknown21007(24, 40)
    sprite('yo000_05', 6)	# 36020-36025
    sprite('yo000_06', 6)	# 36026-36031
    sprite('yo000_07', 6)	# 36032-36037
    gotoLabel(201)
    ExitState()
    label(210)
    sprite('yo600_00', 30)	# 36038-36067
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('yo600_00', 4)	# 36068-36071
    sprite('yo600_01', 4)	# 36072-36075
    SFX_1('pyo600bph')
    sprite('yo600_02', 4)	# 36076-36079
    SFX_3('cloth_l')
    label(211)
    sprite('yo600_00', 6)	# 36080-36085
    sprite('yo600_01', 6)	# 36086-36091
    SFX_3('cloth_l')
    sprite('yo600_02', 6)	# 36092-36097
    sprite('yo600_00', 8)	# 36098-36105
    sprite('yo600_01', 8)	# 36106-36113
    SFX_3('cloth_l')
    sprite('yo600_02', 8)	# 36114-36121
    if SLOT_97:
        _gotolabel(211)
    sprite('yo600_03', 3)	# 36122-36124
    sprite('yo600_04', 3)	# 36125-36127
    sprite('yo600_05', 6)	# 36128-36133
    sprite('yo600_06', 2)	# 36134-36135
    SFX_3('yo006')
    sprite('yo600_07', 2)	# 36136-36137
    sprite('yo600_08', 2)	# 36138-36139
    sprite('yo600_09', 18)	# 36140-36157
    sprite('yo600_10', 6)	# 36158-36163
    Unknown21007(24, 40)
    Unknown21011(300)
    label(222)
    sprite('yo000_00', 6)	# 36164-36169
    sprite('yo000_01', 6)	# 36170-36175
    sprite('yo000_02', 6)	# 36176-36181
    sprite('yo000_03', 6)	# 36182-36187
    sprite('yo000_04', 6)	# 36188-36193
    sprite('yo000_05', 6)	# 36194-36199
    sprite('yo000_06', 6)	# 36200-36205
    sprite('yo000_07', 6)	# 36206-36211
    gotoLabel(222)
    ExitState()
    label(991)
    sprite('yo000_00', 1)	# 36212-36212
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('yo000_00', 6)	# 36213-36218
    sprite('yo000_01', 6)	# 36219-36224
    sprite('yo000_02', 6)	# 36225-36230
    sprite('yo000_03', 6)	# 36231-36236
    sprite('yo000_04', 6)	# 36237-36242
    sprite('yo000_05', 6)	# 36243-36248
    sprite('yo000_06', 6)	# 36249-36254
    sprite('yo000_07', 6)	# 36255-36260
    gotoLabel(992)
    label(993)
    sprite('yo033_00', 2)	# 36261-36262

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
    sprite('yo033_01', 3)	# 36263-36265
    label(994)
    sprite('yo033_02', 3)	# 36266-36268
    sprite('yo033_01', 3)	# 36269-36271
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 36272-36274
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
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
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
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('bph'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('yo610_00', 6)	# 4-9
    sprite('yo610_01', 8)	# 10-17
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 18-27
    sprite('yo610_03', 6)	# 28-33
    sprite('yo610_04', 6)	# 34-39
    sprite('yo610_05', 12)	# 40-51
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pyo524', 100, 896498032, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pyo402_0', 100, 879720816, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pyo522', 100, 896498032, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('yo610_06', 4)	# 52-55
    sprite('yo610_07', 7)	# 56-62
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 63-69
    sprite('yo610_09', 7)	# 70-76
    sprite('yo610_10', 6)	# 77-82
    label(1)
    sprite('yo610_11', 6)	# 83-88
    sprite('yo610_12', 6)	# 89-94
    sprite('yo610_13', 6)	# 95-100
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('yo611_00', 6)	# 101-106
    Unknown36(24)
    Unknown2034(0)
    Unknown2053(0)
    Unknown35()
    Unknown2004(1, 0)
    Unknown2034(0)
    if SLOT_158:
        Unknown20000(1)
    sprite('yo611_01', 6)	# 107-112
    sprite('yo611_02', 6)	# 113-118
    sprite('yo611_03', 6)	# 119-124
    sprite('yo611_04', 6)	# 125-130
    sprite('yo611_05', 6)	# 131-136
    GFX_0('win_bomber', 0)
    SFX_3('yo000')
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pyo524', 100, 896498032, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pyo402_0', 100, 879720816, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pyo520', 100, 896498032, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(11)
    sprite('yo611_06', 6)	# 137-142
    sprite('yo611_07', 6)	# 143-148
    sprite('yo611_08', 6)	# 149-154
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('yo000_00', 1)	# 155-155

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('yo000_00', 6)	# 156-161
    sprite('yo000_01', 6)	# 162-167
    sprite('yo000_02', 6)	# 168-173
    sprite('yo000_03', 6)	# 174-179
    sprite('yo000_04', 6)	# 180-185
    sprite('yo000_05', 6)	# 186-191
    sprite('yo000_06', 6)	# 192-197
    sprite('yo000_07', 6)	# 198-203
    gotoLabel(101)
    label(102)
    sprite('yo610_00', 6)	# 204-209
    SFX_1('pyo701bjn')
    sprite('yo610_01', 8)	# 210-217
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 218-227
    sprite('yo610_03', 6)	# 228-233
    sprite('yo610_04', 6)	# 234-239
    sprite('yo610_05', 12)	# 240-251
    sprite('yo610_06', 4)	# 252-255
    sprite('yo610_07', 7)	# 256-262
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 263-269
    sprite('yo610_09', 7)	# 270-276
    sprite('yo610_10', 6)	# 277-282
    label(103)
    sprite('yo610_11', 6)	# 283-288
    sprite('yo610_12', 6)	# 289-294
    sprite('yo610_13', 6)	# 295-300
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(103)
    sprite('yo610_11', 1)	# 301-301
    Unknown21007(24, 40)
    Unknown21011(50)
    label(104)
    sprite('yo610_11', 6)	# 302-307
    sprite('yo610_12', 6)	# 308-313
    sprite('yo610_13', 6)	# 314-319
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(104)
    label(110)
    sprite('yo610_00', 6)	# 320-325

    def upon_40():
        clearUponHandler(40)
        SFX_1('pyo702bhz')
        Unknown23018(1)
    sprite('yo610_01', 8)	# 326-333
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 334-343
    sprite('yo610_03', 6)	# 344-349
    sprite('yo610_04', 6)	# 350-355
    sprite('yo610_05', 12)	# 356-367
    SFX_1('pyo700bhz')
    sprite('yo610_06', 4)	# 368-371
    sprite('yo610_07', 7)	# 372-378
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 379-385
    sprite('yo610_09', 7)	# 386-392
    sprite('yo610_10', 6)	# 393-398
    label(111)
    sprite('yo610_11', 6)	# 399-404
    sprite('yo610_12', 6)	# 405-410
    sprite('yo610_13', 6)	# 411-416
    SFX_3('cloth_l')
    if SLOT_97:
        _gotolabel(111)
    sprite('yo610_11', 1)	# 417-417
    Unknown21007(24, 40)
    label(112)
    sprite('yo610_11', 6)	# 418-423
    sprite('yo610_12', 6)	# 424-429
    sprite('yo610_13', 6)	# 430-435
    SFX_3('cloth_l')
    gotoLabel(112)
    label(120)
    sprite('yo611_00', 6)	# 436-441
    Unknown2004(1, 0)
    Unknown2034(0)
    sprite('yo611_01', 6)	# 442-447
    sprite('yo611_02', 6)	# 448-453
    sprite('yo611_03', 6)	# 454-459
    sprite('yo611_04', 6)	# 460-465
    sprite('yo611_05', 6)	# 466-471
    GFX_0('win_bomber', 0)
    SFX_3('yo000')
    SFX_1('pyo700bmk')
    label(121)
    sprite('yo611_06', 6)	# 472-477
    sprite('yo611_07', 6)	# 478-483
    sprite('yo611_08', 6)	# 484-489
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('yo611_06', 1)	# 490-490
    Unknown21007(24, 40)
    Unknown21011(260)
    label(122)
    sprite('yo611_06', 6)	# 491-496
    sprite('yo611_07', 6)	# 497-502
    sprite('yo611_08', 6)	# 503-508
    SFX_3('cloth_l')
    gotoLabel(122)
    label(130)
    sprite('yo000_00', 1)	# 509-509
    if (not SLOT_53):
        if random_(2, 0, 50):
            sendToLabel(0)
        else:
            sendToLabel(10)
    sprite('yo000_00', 1)	# 510-510
    Unknown2053(0)
    Unknown2034(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('yo000_00', 6)	# 511-516
    sprite('yo000_01', 6)	# 517-522
    sprite('yo000_02', 6)	# 523-528
    sprite('yo000_03', 6)	# 529-534
    sprite('yo000_04', 6)	# 535-540
    sprite('yo000_05', 6)	# 541-546
    sprite('yo000_06', 6)	# 547-552
    sprite('yo000_07', 6)	# 553-558
    gotoLabel(131)
    label(132)
    sprite('yo610_00', 6)	# 559-564
    sprite('yo610_01', 8)	# 565-572
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 573-582
    sprite('yo610_03', 6)	# 583-588
    sprite('yo610_04', 6)	# 589-594
    sprite('yo610_05', 12)	# 595-606
    SFX_1('pyo701bpt')
    sprite('yo610_06', 4)	# 607-610
    sprite('yo610_07', 7)	# 611-617
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 618-624
    sprite('yo610_09', 7)	# 625-631
    sprite('yo610_10', 6)	# 632-637
    Unknown23018(1)
    label(133)
    sprite('yo610_11', 6)	# 638-643
    sprite('yo610_12', 6)	# 644-649
    sprite('yo610_13', 6)	# 650-655
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(133)
    label(140)
    sprite('yo610_00', 6)	# 656-661

    def upon_40():
        clearUponHandler(40)
        SFX_1('pyo702bes')
        Unknown21011(180)
    sprite('yo610_01', 8)	# 662-669
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 670-679
    sprite('yo610_03', 6)	# 680-685
    sprite('yo610_04', 6)	# 686-691
    sprite('yo610_05', 12)	# 692-703
    SFX_1('pyo700bes')
    sprite('yo610_06', 4)	# 704-707
    sprite('yo610_07', 7)	# 708-714
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 715-721
    sprite('yo610_09', 7)	# 722-728
    sprite('yo610_10', 6)	# 729-734
    label(141)
    sprite('yo610_11', 6)	# 735-740
    sprite('yo610_12', 6)	# 741-746
    sprite('yo610_13', 6)	# 747-752
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('yo610_11', 6)	# 753-758
    sprite('yo610_12', 6)	# 759-764
    sprite('yo610_13', 6)	# 765-770
    sprite('yo610_11', 6)	# 771-776
    sprite('yo610_12', 6)	# 777-782
    sprite('yo610_13', 6)	# 783-788
    Unknown21007(24, 40)
    label(142)
    sprite('yo610_11', 6)	# 789-794
    sprite('yo610_12', 6)	# 795-800
    sprite('yo610_13', 6)	# 801-806
    SFX_3('cloth_l')
    gotoLabel(142)
    label(150)
    sprite('yo610_00', 6)	# 807-812
    sprite('yo610_01', 8)	# 813-820
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 821-830
    sprite('yo610_03', 6)	# 831-836
    sprite('yo610_04', 6)	# 837-842
    sprite('yo610_05', 12)	# 843-854
    SFX_1('pyo700pbc')
    sprite('yo610_06', 4)	# 855-858
    sprite('yo610_07', 7)	# 859-865
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 866-872
    sprite('yo610_09', 7)	# 873-879
    sprite('yo610_10', 6)	# 880-885
    label(151)
    sprite('yo610_11', 6)	# 886-891
    sprite('yo610_12', 6)	# 892-897
    sprite('yo610_13', 6)	# 898-903
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(151)
    sprite('yo610_11', 1)	# 904-904
    Unknown21007(24, 40)
    Unknown21011(240)
    label(152)
    sprite('yo610_11', 6)	# 905-910
    sprite('yo610_12', 6)	# 911-916
    sprite('yo610_13', 6)	# 917-922
    SFX_3('cloth_l')
    gotoLabel(152)
    label(160)
    sprite('yo611_00', 6)	# 923-928
    Unknown2004(1, 0)
    Unknown2034(0)
    sprite('yo611_01', 6)	# 929-934
    sprite('yo611_02', 6)	# 935-940
    sprite('yo611_03', 6)	# 941-946
    sprite('yo611_04', 6)	# 947-952
    sprite('yo611_05', 6)	# 953-958
    GFX_0('win_bomber', 0)
    SFX_3('yo000')
    SFX_1('pyo700pce')
    label(161)
    sprite('yo611_06', 6)	# 959-964
    sprite('yo611_07', 6)	# 965-970
    sprite('yo611_08', 6)	# 971-976
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(161)
    sprite('yo611_06', 6)	# 977-982
    sprite('yo611_07', 6)	# 983-988
    sprite('yo611_08', 6)	# 989-994
    Unknown21007(24, 40)
    Unknown21011(200)
    label(162)
    sprite('yo611_06', 6)	# 995-1000
    sprite('yo611_07', 6)	# 1001-1006
    sprite('yo611_08', 6)	# 1007-1012
    SFX_3('cloth_l')
    gotoLabel(162)
    label(170)
    sprite('yo000_00', 1)	# 1013-1013

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('yo000_00', 6)	# 1014-1019
    sprite('yo000_01', 6)	# 1020-1025
    sprite('yo000_02', 6)	# 1026-1031
    sprite('yo000_03', 6)	# 1032-1037
    sprite('yo000_04', 6)	# 1038-1043
    sprite('yo000_05', 6)	# 1044-1049
    sprite('yo000_06', 6)	# 1050-1055
    sprite('yo000_07', 6)	# 1056-1061
    gotoLabel(171)
    label(172)
    sprite('yo610_00', 6)	# 1062-1067
    sprite('yo610_01', 8)	# 1068-1075
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 1076-1085
    sprite('yo610_03', 6)	# 1086-1091
    sprite('yo610_04', 6)	# 1092-1097
    sprite('yo610_05', 12)	# 1098-1109
    SFX_1('pyo701pka_a')
    sprite('yo610_06', 4)	# 1110-1113
    sprite('yo610_07', 7)	# 1114-1120
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 1121-1127
    sprite('yo610_09', 7)	# 1128-1134
    sprite('yo610_10', 6)	# 1135-1140
    Unknown23018(1)
    label(173)
    sprite('yo610_11', 6)	# 1141-1146
    sprite('yo610_12', 6)	# 1147-1152
    sprite('yo610_13', 6)	# 1153-1158
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(173)
    label(180)
    sprite('yo611_00', 6)	# 1159-1164
    Unknown2004(1, 0)
    Unknown2034(0)

    def upon_40():
        SLOT_51 = 1
    sprite('yo611_01', 6)	# 1165-1170
    sprite('yo611_02', 6)	# 1171-1176
    sprite('yo611_03', 6)	# 1177-1182
    sprite('yo611_04', 6)	# 1183-1188
    sprite('yo611_05', 6)	# 1189-1194
    GFX_0('win_bomber', 0)
    SFX_3('yo000')
    SFX_1('pyo700uli')
    label(181)
    sprite('yo611_06', 6)	# 1195-1200
    sprite('yo611_07', 6)	# 1201-1206
    sprite('yo611_08', 6)	# 1207-1212
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(181)
    sprite('yo611_06', 1)	# 1213-1213
    Unknown21007(24, 40)
    label(182)
    sprite('yo611_06', 6)	# 1214-1219
    if SLOT_51:
        sendToLabel(183)
    sprite('yo611_07', 6)	# 1220-1225
    sprite('yo611_08', 6)	# 1226-1231
    SFX_3('cloth_l')
    gotoLabel(182)
    label(183)
    sprite('yo611_06', 1)	# 1232-1232
    SFX_1('pyo702uli')
    label(184)
    sprite('yo611_06', 6)	# 1233-1238
    sprite('yo611_07', 6)	# 1239-1244
    sprite('yo611_08', 6)	# 1245-1250
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(184)
    sprite('yo611_06', 1)	# 1251-1251
    Unknown21007(24, 39)
    Unknown21011(60)
    label(185)
    sprite('yo611_06', 6)	# 1252-1257
    sprite('yo611_07', 6)	# 1258-1263
    sprite('yo611_08', 6)	# 1264-1269
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(185)
    label(190)
    sprite('yo611_00', 6)	# 1270-1275
    Unknown2004(1, 0)
    Unknown2034(0)
    sprite('yo611_01', 6)	# 1276-1281
    sprite('yo611_02', 6)	# 1282-1287
    sprite('yo611_03', 6)	# 1288-1293
    sprite('yo611_04', 6)	# 1294-1299
    sprite('yo611_05', 6)	# 1300-1305
    GFX_0('win_bomber', 0)
    SFX_3('yo000')
    SFX_1('pyo700uyu')
    label(191)
    sprite('yo611_06', 6)	# 1306-1311
    sprite('yo611_07', 6)	# 1312-1317
    sprite('yo611_08', 6)	# 1318-1323
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(191)
    sprite('yo611_06', 6)	# 1324-1329
    sprite('yo611_07', 6)	# 1330-1335
    sprite('yo611_08', 6)	# 1336-1341
    Unknown21007(24, 40)
    Unknown21011(240)
    label(192)
    sprite('yo611_06', 6)	# 1342-1347
    sprite('yo611_07', 6)	# 1348-1353
    sprite('yo611_08', 6)	# 1354-1359
    SFX_3('cloth_l')
    gotoLabel(192)
    label(200)
    sprite('yo000_00', 1)	# 1360-1360

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('yo000_00', 6)	# 1361-1366
    sprite('yo000_01', 6)	# 1367-1372
    sprite('yo000_02', 6)	# 1373-1378
    sprite('yo000_03', 6)	# 1379-1384
    sprite('yo000_04', 6)	# 1385-1390
    sprite('yo000_05', 6)	# 1391-1396
    sprite('yo000_06', 6)	# 1397-1402
    sprite('yo000_07', 6)	# 1403-1408
    gotoLabel(201)
    label(202)
    sprite('yo610_00', 6)	# 1409-1414
    sprite('yo610_01', 8)	# 1415-1422
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 1423-1432
    sprite('yo610_03', 6)	# 1433-1438
    sprite('yo610_04', 6)	# 1439-1444
    sprite('yo610_05', 12)	# 1445-1456
    SFX_1('pyo701ryn')
    sprite('yo610_06', 4)	# 1457-1460
    sprite('yo610_07', 7)	# 1461-1467
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 1468-1474
    sprite('yo610_09', 7)	# 1475-1481
    sprite('yo610_10', 6)	# 1482-1487
    Unknown23018(1)
    label(203)
    sprite('yo610_11', 6)	# 1488-1493
    sprite('yo610_12', 6)	# 1494-1499
    sprite('yo610_13', 6)	# 1500-1505
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(203)
    label(210)
    sprite('yo000_00', 1)	# 1506-1506

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('yo000_00', 6)	# 1507-1512
    sprite('yo000_01', 6)	# 1513-1518
    sprite('yo000_02', 6)	# 1519-1524
    sprite('yo000_03', 6)	# 1525-1530
    sprite('yo000_04', 6)	# 1531-1536
    sprite('yo000_05', 6)	# 1537-1542
    sprite('yo000_06', 6)	# 1543-1548
    sprite('yo000_07', 6)	# 1549-1554
    gotoLabel(211)
    label(212)
    sprite('yo610_00', 6)	# 1555-1560
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
    sprite('yo610_01', 8)	# 1561-1568
    GFX_0('win_kunai', 100)
    sprite('yo610_02', 10)	# 1569-1578
    sprite('yo610_03', 6)	# 1579-1584
    sprite('yo610_04', 6)	# 1585-1590
    sprite('yo610_05', 12)	# 1591-1602
    SFX_1('pyo701bph')
    sprite('yo610_06', 4)	# 1603-1606
    sprite('yo610_07', 7)	# 1607-1613
    GFX_1('yoef_matchwin_sweat', 0)
    GFX_1('yoef_matchwin_sweat', 1)
    sprite('yo610_08', 7)	# 1614-1620
    sprite('yo610_09', 7)	# 1621-1627
    sprite('yo610_10', 6)	# 1628-1633
    Unknown23018(1)
    label(213)
    sprite('yo610_11', 6)	# 1634-1639
    sprite('yo610_12', 6)	# 1640-1645
    sprite('yo610_13', 6)	# 1646-1651
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(213)

@State
def CmnActLose():
    sprite('yo070_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('pyo403_0', 100, 879720816, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('yo070_01', 6)	# 7-12
    sprite('yo070_02', 2)	# 13-14
    sprite('yo070_03', 32767)	# 15-32781
    Unknown21011(30)