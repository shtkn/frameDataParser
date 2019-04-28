@Subroutine
def PreInit():
    Unknown12019('62746700000000000000000000000000')

@Subroutine
def MatchInit():
    Health(20000)
    WalkBSpeed(4500)
    DashFInitialVelocity(9000)
    DashFAccel(0)
    JumpYVelocity(26000)
    SuperJumpYVelocity(36000)
    Unknown12007(6000)
    Unknown12008(8500)
    Unknown12009(5500)
    Unknown12010(7500)
    Unknown12011(1250)
    DoubleJumpCount(0)
    AirDashCount(0)
    Unknown12024(4)
    Unknown13039(3)
    Unknown2049(1)
    Unknown12025(12000)
    Unknown12026(8000)
    Unknown12027(800)
    Unknown12014(0)
    Unknown12046(35)
    Unknown12029(0)
    Move_Register('NmlAtk5A', 0x7)
    Unknown14015(300000, 600000, -100000, 700000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Unknown14015(300000, 500000, -200000, 400000, 1000, 50)
    Unknown15012(900)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown14015(500000, 800000, -100000, 500000, 1000, 50)
    Unknown15012(300)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Unknown14015(300000, 600000, -400000, 300000, 1000, 50)
    Unknown15012(100)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(50000, 400000, -100000, 300000, 2000, 50)
    Unknown15012(200)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    Unknown14005(1)
    Unknown14015(50000, 450000, 0, 200000, 1000, 50)
    Unknown15012(200)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    Unknown14005(1)
    Unknown14015(0, 600000, -100000, 300000, 1000, 50)
    Unknown15012(200)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14015(0, 350000, 100000, 1000000, 500, 50)
    Unknown15021(4000)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14015(500000, 800000, 0, 300000, 3000, 300)
    Unknown15016(1, 40, 70)
    Unknown15012(50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14015(300000, 1500000, -200000, 300000, 1500, 300)
    Unknown15014(100)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown14015(0, 350000, -200000, 200000, 500, 0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown14015(150000, 400000, 0, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(100000, 450000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown14015(150000, 500000, 0, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(200000, 700000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(0, 500000, -400000, 150000, 1000, 0)
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
    Move_Register('Oiuchi', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('CheckAirOiuchiActive')
    Unknown14015(0, 800000, -500000, 300000, 250, 0)
    Unknown15013(100000)
    Move_EndRegister()
    Move_Register('Oiuchi_B', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('Oiuchi')
    Unknown14024('CheckAirOiuchiActive')
    Unknown14015(0, 800000, -500000, 300000, 250, 0)
    Unknown15013(100000)
    Move_EndRegister()
    Move_Register('Oiuchi_C', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('Oiuchi')
    Unknown14024('CheckAirOiuchiActive')
    Unknown14015(0, 800000, -500000, 300000, 250, 0)
    Unknown15013(100000)
    Move_EndRegister()
    Move_Register('Oiuchi_Throw', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('CheckAirOiuchiActive')
    Unknown14015(0, 800000, -500000, 300000, 250, 0)
    Unknown15013(100000)
    Move_EndRegister()
    Move_Register('Oiuchi_Throw_B', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('Oiuchi_Throw')
    Unknown14024('CheckAirOiuchiActive')
    Unknown14015(0, 800000, -500000, 300000, 250, 0)
    Unknown15013(100000)
    Move_EndRegister()
    Move_Register('Oiuchi_Throw_C', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('Oiuchi_Throw')
    Unknown14024('CheckAirOiuchiActive')
    Unknown14015(0, 800000, -500000, 300000, 250, 0)
    Unknown15013(100000)
    Move_EndRegister()
    Move_Register('AntiAir_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 600000, 150000, 600000, 100, 0)
    Unknown15021(4000)
    Move_EndRegister()
    Move_Register('AntiAir_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 1200000, 400000, 600000, 100, 0)
    Unknown15016(1, 40, 60)
    Unknown15021(60000)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(700000, 2000000, -200000, 300000, 1000, 0)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('CommandThrow', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 300000, -200000, 200000, 2000, 0)
    Unknown15021(100)
    Unknown15012(5000)
    Unknown15013(0)
    Move_EndRegister()
    Move_Register('CommandThrowB2', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 600000, -200000, 200000, 500, 0)
    Unknown15021(100)
    Unknown15012(5000)
    Unknown15013(100)
    Unknown15014(3000)
    Move_EndRegister()
    Move_Register('CommandThrowEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 200000, 2000, 0)
    Unknown15016(2, 20, 60)
    Unknown15021(100)
    Unknown15013(100)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('CommandThrowC_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 350000, 1000, 0)
    Unknown15021(6000)
    Move_EndRegister()
    Move_Register('CommandThrowC_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 350000, 1000, 0)
    Unknown15016(1, 20, 60)
    Unknown15021(6000)
    Unknown15013(0)
    Move_EndRegister()
    Move_Register('CommandThrowC_C', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 350000, 1000, 0)
    Unknown15016(2, 20, 60)
    Unknown15021(6000)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(0, 550000, -200000, 300000, 500, 10)
    Unknown15014(3000)
    Move_EndRegister()
    Move_Register('MTH', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(-100000, 400000, 0, 200000, 1000, 1)
    Unknown15014(3000)
    Move_EndRegister()
    Move_Register('MTH_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(-100000, 400000, 0, 200000, 1000, 1)
    Unknown15014(3000)
    Move_EndRegister()
    Move_Register('GETB', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 400000, -120000, 150000, 3000, 0)
    Unknown15016(2, 20, 60)
    Unknown15021(100)
    Unknown15013(0)
    Move_EndRegister()
    Move_Register('GETB_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 400000, -120000, 150000, 3000, 0)
    Unknown15016(2, 20, 60)
    Unknown15021(100)
    Unknown15013(0)
    Move_EndRegister()
    Move_Register('Air_GETB', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 350000, 3000, 0)
    Unknown15016(2, 20, 60)
    Unknown15021(6000)
    Unknown15013(0)
    Move_EndRegister()
    Move_Register('Air_GETB_OD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 350000, 3000, 0)
    Unknown15016(2, 20, 60)
    Unknown15021(6000)
    Unknown15013(0)
    Move_EndRegister()
    Move_Register('GETB_TRUE', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(0xcb)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('GETB_OD_TRUE', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(0xcb)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('Air_GETB_TRUE', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(0xcb)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('Air_GETB_OD_TRUE', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(0xcb)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15013(4000)
    Unknown15014(4000)
    Unknown14015(-250000, 250000, -200000, 800000, 1000, 1)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2A', 'AntiAir_A', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk2B', 'Shot', 10000000)
    Unknown12018(0, 'tg062_01')
    Unknown12018(1, 'tg062_03')
    Unknown12018(2, 'tg062_04')
    Unknown12018(3, 'tg062_05')
    Unknown12018(4, 'tg062_06')
    Unknown12018(5, 'tg062_06')
    Unknown12018(6, 'tg062_07')
    Unknown12018(7, 'tg041_02')
    Unknown12018(8, 'tg040_02')
    Unknown12018(9, 'tg045_02')
    Unknown12018(10, 'tg060_00')
    Unknown12018(11, 'tg060_01')
    Unknown12018(12, 'tg060_03')
    Unknown12018(13, 'tg060_05')
    Unknown12018(14, 'tg060_07')
    Unknown12018(15, 'tg060_15')
    Unknown12018(16, 'tg050_00')
    Unknown12018(17, 'tg052_00')
    Unknown12018(18, 'tg054_00')
    Unknown12018(19, 'tg000_00')
    Unknown12018(20, 'tg000_00')
    Unknown12018(25, 'tg063_00')
    Unknown12018(26, 'tg063_01')
    Unknown12018(27, 'tg063_02')
    Unknown12018(28, 'tg063_04')
    Unknown12018(29, 'tg063_11')
    Unknown12018(24, 'tg073_01')
    Unknown7010(0, 'btg000')
    Unknown7010(1, 'btg001')
    Unknown7010(2, 'btg002')
    Unknown7010(3, 'btg003')
    Unknown7010(4, 'btg004')
    Unknown7010(5, 'btg005')
    Unknown7010(6, 'btg006')
    Unknown7010(7, 'btg007')
    Unknown7010(8, 'btg008')
    Unknown7010(9, 'btg009')
    Unknown7010(10, 'btg010')
    Unknown7010(15, 'btg011')
    Unknown7010(16, 'btg012')
    Unknown7010(17, 'btg013')
    Unknown7010(18, 'btg014')
    Unknown7010(19, 'btg015')
    Unknown7010(20, 'btg016')
    Unknown7010(21, 'btg017')
    Unknown7010(22, 'btg018')
    Unknown7010(23, 'btg019')
    Unknown7010(24, 'btg020')
    Unknown7010(25, 'btg021')
    Unknown7010(28, 'btg022')
    Unknown7010(29, 'btg023')
    Unknown7010(30, 'btg024')
    Unknown7010(31, 'btg025')
    Unknown7010(32, 'btg026')
    Unknown7010(33, 'btg027')
    Unknown7010(34, 'btg028')
    Unknown7010(35, 'btg029')
    Unknown7010(36, 'btg030')
    Unknown7010(37, 'btg031')
    Unknown7010(39, 'btg032')
    Unknown7010(42, 'btg033')
    Unknown7010(43, 'btg034')
    Unknown7010(44, 'btg035')
    Unknown7010(45, 'btg036')
    Unknown7010(46, 'btg037')
    Unknown7010(47, 'btg038')
    Unknown7010(48, 'btg039')
    Unknown7010(49, 'btg040')
    Unknown7010(50, 'btg041')
    Unknown7010(52, 'btg042')
    Unknown7010(53, 'btg043')
    Unknown7010(54, 'btg100_0')
    Unknown7010(55, 'btg100_1')
    Unknown7010(56, 'btg100_2')
    Unknown7010(63, 'btg101_0')
    Unknown7010(64, 'btg101_1')
    Unknown7010(65, 'btg101_2')
    Unknown7010(57, 'btg102_0')
    Unknown7010(58, 'btg102_1')
    Unknown7010(59, 'btg102_2')
    Unknown7010(66, 'btg103_0')
    Unknown7010(67, 'btg103_1')
    Unknown7010(68, 'btg103_2')
    Unknown7010(60, 'btg104_0')
    Unknown7010(61, 'btg104_1')
    Unknown7010(62, 'btg104_2')
    Unknown7010(69, 'btg105_0')
    Unknown7010(70, 'btg105_1')
    Unknown7010(71, 'btg105_2')
    Unknown7010(72, 'btg150')
    Unknown7010(73, 'btg151')
    Unknown7010(74, 'btg152')
    Unknown7010(85, 'btg153')
    Unknown7010(87, 'btg154')
    Unknown7010(88, 'btg155')
    Unknown7010(96, 'btg161_0')
    Unknown7010(97, 'btg161_1')
    Unknown7010(92, 'btg162_0')
    Unknown7010(93, 'btg162_1')
    Unknown7010(98, 'btg163_0')
    Unknown7010(99, 'btg163_1')
    Unknown7010(100, 'btg164_0')
    Unknown7010(101, 'btg164_1')
    Unknown7010(105, 'btg165_0')
    Unknown7010(106, 'btg165_1')
    Unknown7010(102, 'btg166_0')
    Unknown7010(103, 'btg166_1')
    Unknown7010(90, 'btg167_0')
    Unknown7010(91, 'btg167_1')
    Unknown7010(107, 'btg168_0')
    Unknown7010(108, 'btg168_1')
    Unknown7010(110, 'btg169_0')
    Unknown7010(111, 'btg169_1')
    Unknown7010(94, 'btg400_0')
    Unknown7010(95, 'btg400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('020000004d54480000000000000000000000000000000000000000000000000000000000')
    Unknown12059('030000004d54485f4f440000000000000000000000000000000000000000000000000000')
    Unknown12059('040000004745544200000000000000000000000000000000000000000000000000000000')
    Unknown12059('05000000474554425f4f4400000000000000000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def komanageEff():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3072('80000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    Unknown3074('000000000400000032000000a0000000')
    Unknown3075('00000000000000000000000010000000')
    Unknown3076(1010)
    Unknown3077(900)

@Subroutine
def MAGNET_RESET():

    def upon_STATE_END():
        Unknown21003(0, 0)

@Subroutine
def OnFrameStep():
    Unknown48('19000000020000003d00000016000000020000004b000000')
    if SLOT_61:
        SLOT_61 = 1
    else:
        SLOT_61 = 0

@Subroutine
def CheckAirOiuchiActive():
    (SLOT_61 == 1)
    SLOT_47 = SLOT_0

@Subroutine
def MatchInit2():
    SLOT_66 = 1

@Subroutine
def OnLanding():
    if (not SLOT_66):
        SLOT_66 = 1

@Subroutine
def CheckAirAssaultActive():
    (SLOT_66 == 1)
    SLOT_47 = SLOT_0

@State
def CmnActStand():
    label(0)
    sprite('tg000_00', 6)	# 1-6
    sprite('tg000_01', 6)	# 7-12
    sprite('tg000_02', 6)	# 13-18
    sprite('tg000_03', 6)	# 19-24
    sprite('tg000_04', 6)	# 25-30
    sprite('tg000_05', 6)	# 31-36
    sprite('tg000_06', 6)	# 37-42
    sprite('tg000_05', 6)	# 43-48
    sprite('tg000_04', 6)	# 49-54
    sprite('tg000_03', 6)	# 55-60
    sprite('tg000_02', 6)	# 61-66
    sprite('tg000_01', 6)	# 67-72
    sprite('tg000_00', 6)	# 73-78
    sprite('tg000_01', 6)	# 79-84
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 85-90
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 91-96
    SFX_0('014_electric_s')
    sprite('tg000_04', 6)	# 97-102
    sprite('tg000_05', 6)	# 103-108
    sprite('tg000_06', 6)	# 109-114
    sprite('tg000_05', 6)	# 115-120
    sprite('tg000_04', 6)	# 121-126
    sprite('tg000_03', 6)	# 127-132
    sprite('tg000_02', 6)	# 133-138
    sprite('tg000_01', 6)	# 139-144
    sprite('tg000_00', 6)	# 145-150
    sprite('tg000_01', 6)	# 151-156
    sprite('tg000_02', 6)	# 157-162
    sprite('tg000_03', 6)	# 163-168
    sprite('tg000_04', 6)	# 169-174
    sprite('tg000_05', 6)	# 175-180
    sprite('tg000_06', 6)	# 181-186
    sprite('tg000_05', 6)	# 187-192
    sprite('tg000_04', 6)	# 193-198
    sprite('tg000_03', 6)	# 199-204
    sprite('tg000_02', 6)	# 205-210
    sprite('tg000_01', 6)	# 211-216
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    if random_(2, 0, 80):
        gotoLabel(0)
    sprite('tg001_00', 8)	# 217-224
    SLOT_88 = 960
    sprite('tg001_01', 8)	# 225-232
    sprite('tg001_02', 8)	# 233-240
    SFX_4('btg000')
    sprite('tg001_03', 8)	# 241-248
    SFX_3('tgse_00')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000000000000')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000001000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000002000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000003000000')
    sprite('tg001_04', 8)	# 249-256
    sprite('tg001_05', 8)	# 257-264
    sprite('tg001_06', 8)	# 265-272
    sprite('tg001_07', 8)	# 273-280
    sprite('tg001_08', 8)	# 281-288
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('tg003_00', 4)	# 1-4
    sprite('tg003_01', 4)	# 5-8
    sprite('tg003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('tg010_00', 3)	# 1-3
    sprite('tg010_01', 3)	# 4-6

@State
def CmnActCrouch():
    label(0)
    sprite('tg010_02', 6)	# 1-6
    sprite('tg010_03', 6)	# 7-12
    sprite('tg010_04', 6)	# 13-18
    sprite('tg010_05', 6)	# 19-24
    sprite('tg010_06', 6)	# 25-30
    sprite('tg010_07', 6)	# 31-36
    sprite('tg010_08', 6)	# 37-42
    sprite('tg010_07', 6)	# 43-48
    sprite('tg010_06', 6)	# 49-54
    sprite('tg010_05', 6)	# 55-60
    sprite('tg010_04', 6)	# 61-66
    sprite('tg010_03', 6)	# 67-72
    sprite('tg010_02', 6)	# 73-78
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('tg013_00', 4)	# 1-4
    sprite('tg013_01', 4)	# 5-8
    sprite('tg013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('tg010_01', 4)	# 1-4
    sprite('tg010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('tg023_00', 3)	# 1-3
    sprite('tg023_01', 3)	# 4-6

@State
def CmnActJumpUpper():
    label(0)
    sprite('tg020_00', 3)	# 1-3
    sprite('tg020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('tg020_02', 3)	# 1-3
    sprite('tg020_03', 3)	# 4-6
    sprite('tg020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('tg020_05', 3)	# 1-3
    sprite('tg020_06', 3)	# 4-6
    label(0)
    sprite('tg020_07', 3)	# 7-9
    sprite('tg020_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('tg024_00', 3)	# 1-3
    ScreenShake(0, 3500)
    SFX_0('019_quake_0')
    SFX_3('tgse_26')
    sprite('tg024_01', 3)	# 4-6
    sprite('tg024_02', 3)	# 7-9
    sprite('tg024_03', 3)	# 10-12
    sprite('tg024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('tg024_01', 3)	# 1-3
    ScreenShake(0, 3500)
    sprite('tg024_02', 32767)	# 4-32770

@State
def CmnActLandingStiffEnd():
    sprite('tg024_03', 3)	# 1-3
    sprite('tg024_04', 3)	# 4-6

@State
def CmnActFWalk():

    def upon_IMMEDIATE():
        Unknown2042(1)
    sprite('tg030_00', 5)	# 1-5
    label(0)
    sprite('tg030_01', 5)	# 6-10
    sprite('tg030_02', 5)	# 11-15
    sprite('tg030_03', 5)	# 16-20
    sprite('tg030_04', 5)	# 21-25
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 5)	# 26-30
    sprite('tg030_06', 5)	# 31-35
    sprite('tg030_07', 5)	# 36-40
    sprite('tg030_08', 5)	# 41-45
    sprite('tg030_09', 5)	# 46-50
    sprite('tg030_10', 5)	# 51-55
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 5)	# 56-60
    sprite('tg030_12', 5)	# 61-65
    loopRest()
    gotoLabel(0)

@State
def CmnActFWalkEnd():
    sprite('tg030_01', 3)	# 1-3
    sprite('tg030_00', 3)	# 4-6

@State
def CmnActBWalk():

    def upon_IMMEDIATE():
        Unknown2042(1)
    sprite('tg031_00', 6)	# 1-6
    sprite('tg031_01', 6)	# 7-12
    label(0)
    sprite('tg031_02', 6)	# 13-18
    sprite('tg031_03', 6)	# 19-24
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg031_04', 6)	# 25-30
    sprite('tg031_05', 6)	# 31-36
    sprite('tg031_06', 6)	# 37-42
    sprite('tg031_07', 6)	# 43-48
    sprite('tg031_08', 6)	# 49-54
    sprite('tg031_09', 6)	# 55-60
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg031_10', 6)	# 61-66
    sprite('tg031_11', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalkEnd():
    sprite('tg031_01', 3)	# 1-3
    sprite('tg031_00', 3)	# 4-6

@State
def CmnActFDash():
    sprite('tg030_00', 6)	# 1-6

@State
def CmnActFDashStop():
    sprite('tg030_11', 6)	# 1-6
    sprite('tg030_12', 6)	# 7-12

@State
def CmnActBDash():
    sprite('tg033_00', 1)	# 1-1
    Unknown22008(20)
    physicsYImpulse(10000)
    physicsXImpulse(-6500)
    sprite('tg033_01', 1)	# 2-2
    sprite('tg033_02', 3)	# 3-5
    label(0)
    sprite('tg033_03', 3)	# 6-8
    sprite('tg033_04', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBDashLanding():
    sprite('tg033_05', 3)	# 1-3
    SFX_3('tgse_26')
    sprite('tg033_06', 3)	# 4-6
    sprite('tg033_07', 3)	# 7-9
    sprite('tg033_08', 3)	# 10-12

@State
def CmnActAirFDash():
    sprite('tg252_00', 3)	# 1-3
    sprite('tg252_01', 3)	# 4-6
    sprite('tg252_02', 5)	# 7-11
    sprite('tg252_03', 12)	# 12-23	 **attackbox here**

@State
def CmnActAirBDash():
    sprite('tg033_00', 1)	# 1-1
    sprite('tg033_01', 1)	# 2-2
    sprite('tg033_02', 3)	# 3-5
    label(0)
    sprite('tg033_03', 3)	# 6-8
    sprite('tg033_04', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('tg050_00', 1)	# 1-1
    sprite('tg050_01', 1)	# 2-2
    sprite('tg050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('tg050_01', 1)	# 1-1
    sprite('tg050_02', 1)	# 2-2
    sprite('tg050_01', 2)	# 3-4
    sprite('tg050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('tg050_02', 1)	# 1-1
    sprite('tg050_03', 1)	# 2-2
    sprite('tg050_02', 2)	# 3-4
    sprite('tg050_01', 2)	# 5-6
    sprite('tg050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('tg050_03', 1)	# 1-1
    sprite('tg050_04', 1)	# 2-2
    sprite('tg050_03', 2)	# 3-4
    sprite('tg050_02', 2)	# 5-6
    sprite('tg050_01', 2)	# 7-8
    sprite('tg050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('tg050_04', 1)	# 1-1
    sprite('tg050_04', 1)	# 2-2
    sprite('tg050_04', 2)	# 3-4
    sprite('tg050_03', 2)	# 5-6
    sprite('tg050_02', 2)	# 7-8
    sprite('tg050_01', 2)	# 9-10
    sprite('tg050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('tg052_00', 1)	# 1-1
    sprite('tg052_01', 1)	# 2-2
    sprite('tg052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('tg052_01', 1)	# 1-1
    sprite('tg052_02', 1)	# 2-2
    sprite('tg052_01', 2)	# 3-4
    sprite('tg052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('tg052_02', 1)	# 1-1
    sprite('tg052_03', 1)	# 2-2
    sprite('tg052_02', 2)	# 3-4
    sprite('tg052_01', 2)	# 5-6
    sprite('tg052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('tg052_03', 1)	# 1-1
    sprite('tg052_04', 1)	# 2-2
    sprite('tg052_03', 2)	# 3-4
    sprite('tg052_02', 2)	# 5-6
    sprite('tg052_01', 2)	# 7-8
    sprite('tg052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('tg052_04', 1)	# 1-1
    sprite('tg052_04', 1)	# 2-2
    sprite('tg052_04', 2)	# 3-4
    sprite('tg052_03', 2)	# 5-6
    sprite('tg052_02', 2)	# 7-8
    sprite('tg052_01', 2)	# 9-10
    sprite('tg052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('tg054_00', 1)	# 1-1
    sprite('tg054_01', 1)	# 2-2
    sprite('tg054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('tg054_01', 1)	# 1-1
    sprite('tg054_02', 1)	# 2-2
    sprite('tg054_01', 2)	# 3-4
    sprite('tg054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('tg054_02', 1)	# 1-1
    sprite('tg054_03', 1)	# 2-2
    sprite('tg054_02', 2)	# 3-4
    sprite('tg054_01', 2)	# 5-6
    sprite('tg054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('tg054_03', 1)	# 1-1
    sprite('tg054_04', 1)	# 2-2
    sprite('tg054_03', 2)	# 3-4
    sprite('tg054_02', 2)	# 5-6
    sprite('tg054_01', 2)	# 7-8
    sprite('tg054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('tg054_04', 1)	# 1-1
    sprite('tg054_04', 1)	# 2-2
    sprite('tg054_04', 2)	# 3-4
    sprite('tg054_03', 2)	# 5-6
    sprite('tg054_02', 2)	# 7-8
    sprite('tg054_01', 2)	# 9-10
    sprite('tg054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('tg060_00', 6)	# 1-6
    label(0)
    sprite('tg060_01', 4)	# 7-10
    sprite('tg060_02', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('tg062_05', 4)	# 1-4
    sprite('tg062_06', 4)	# 5-8

@State
def CmnActBDownDown():
    label(0)
    sprite('tg062_07', 4)	# 1-4
    sprite('tg062_08', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('tg063_04', 3)	# 1-3
    sprite('tg063_05', 3)	# 4-6

@State
def CmnActBDownBound():
    sprite('tg063_06', 3)	# 1-3
    sprite('tg063_07', 3)	# 4-6
    sprite('tg063_08', 3)	# 7-9
    sprite('tg063_09', 3)	# 10-12
    sprite('tg063_10', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('tg063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('tg064_00', 4)	# 1-4
    sprite('tg064_01', 5)	# 5-9
    sprite('tg064_02', 6)	# 10-15
    sprite('tg064_03', 3)	# 16-18
    sprite('tg064_04', 3)	# 19-21
    sprite('tg064_05', 3)	# 22-24
    sprite('tg064_06', 3)	# 25-27
    sprite('tg064_07', 3)	# 28-30
    sprite('tg064_08', 3)	# 31-33
    sprite('tg064_09', 3)	# 34-36
    sprite('tg064_10', 4)	# 37-40
    sprite('tg064_11', 4)	# 41-44
    sprite('tg064_12', 5)	# 45-49
    sprite('tg064_13', 6)	# 50-55
    sprite('tg064_14', 7)	# 56-62

@State
def CmnActFDownUpper():
    sprite('tg063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('tg063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    sprite('tg063_01', 3)	# 1-3
    label(0)
    sprite('tg063_02', 3)	# 4-6
    sprite('tg063_03', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('tg063_04', 3)	# 1-3
    sprite('tg063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('tg063_05', 3)	# 1-3
    sprite('tg063_06', 3)	# 4-6
    sprite('tg063_07', 3)	# 7-9
    sprite('tg063_08', 3)	# 10-12
    sprite('tg063_09', 3)	# 13-15
    sprite('tg063_10', 3)	# 16-18

@State
def CmnActFDownLoop():
    sprite('tg063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('tg064_00', 4)	# 1-4
    sprite('tg064_01', 5)	# 5-9
    sprite('tg064_02', 6)	# 10-15
    sprite('tg064_03', 3)	# 16-18
    sprite('tg064_04', 3)	# 19-21
    sprite('tg064_05', 3)	# 22-24
    sprite('tg064_06', 3)	# 25-27
    sprite('tg064_07', 3)	# 28-30
    sprite('tg064_08', 3)	# 31-33
    sprite('tg064_09', 3)	# 34-36
    sprite('tg064_10', 4)	# 37-40
    sprite('tg064_11', 4)	# 41-44
    sprite('tg064_12', 5)	# 45-49
    sprite('tg064_13', 6)	# 50-55
    sprite('tg064_14', 7)	# 56-62

@State
def CmnActVDownUpper():
    sprite('tg062_00', 4)	# 1-4
    label(0)
    sprite('tg062_01', 4)	# 5-8
    sprite('tg062_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('tg062_03', 3)	# 1-3
    sprite('tg062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('tg062_05', 4)	# 1-4
    sprite('tg062_06', 4)	# 5-8
    label(0)
    sprite('tg062_07', 4)	# 9-12
    sprite('tg062_08', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('tg062_09', 2)	# 1-2
    sprite('tg062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('tg072_00', 3)	# 1-3
    label(0)
    sprite('tg072_01', 3)	# 4-6
    sprite('tg072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('tg074_00', 3)	# 1-3
    sprite('tg074_01', 3)	# 4-6
    sprite('tg074_02', 3)	# 7-9
    sprite('tg074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    pass

@State
def CmnActFreeze():
    sprite('tg052_02', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('tg073_00', 3)	# 1-3
    sprite('tg073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('tg073_02', 3)	# 1-3
    label(0)
    sprite('tg073_03', 3)	# 4-6
    sprite('tg073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('tg070_02', 3)	# 1-3
    sprite('tg070_01', 3)	# 4-6
    sprite('tg070_02', 3)	# 7-9
    sprite('tg070_04', 3)	# 10-12

@State
def CmnActStaggerDown():
    sprite('tg070_06', 3)	# 1-3
    sprite('tg070_07', 3)	# 4-6
    sprite('tg070_08', 4)	# 7-10
    sprite('tg070_09', 3)	# 11-13
    sprite('tg070_10', 3)	# 14-16
    sprite('tg070_11', 3)	# 17-19
    sprite('tg070_12', 3)	# 20-22
    sprite('tg070_13', 3)	# 23-25

@State
def CmnActUkemiStagger():
    sprite('tg070_14', 2)	# 1-2
    sprite('tg070_15', 2)	# 3-4
    sprite('tg070_16', 3)	# 5-7
    sprite('tg070_17', 3)	# 8-10

@State
def CmnActUkemiAirF():
    sprite('tg113_00', 2)	# 1-2
    sprite('tg113_01', 2)	# 3-4
    sprite('tg113_02', 2)	# 5-6

@State
def CmnActUkemiAirB():
    sprite('tg113_00', 2)	# 1-2
    sprite('tg113_01', 2)	# 3-4
    sprite('tg113_02', 2)	# 5-6

@State
def CmnActUkemiAirN():
    sprite('tg113_00', 2)	# 1-2
    sprite('tg113_01', 2)	# 3-4
    sprite('tg113_02', 2)	# 5-6

@State
def CmnActUkemiLandF():
    sprite('tg112_00', 3)	# 1-3
    Unknown2017(0)
    sprite('tg112_01', 3)	# 4-6
    sprite('tg112_02', 3)	# 7-9
    sprite('tg112_03', 3)	# 10-12
    sprite('tg112_04', 3)	# 13-15
    sprite('tg112_05', 3)	# 16-18
    sprite('tg112_06', 3)	# 19-21
    sprite('tg112_07', 3)	# 22-24
    sprite('tg112_08', 3)	# 25-27
    sprite('tg112_09', 3)	# 28-30
    sprite('tg112_10', 3)	# 31-33

@State
def CmnActUkemiLandB():
    sprite('tg112_00', 3)	# 1-3
    sprite('tg112_01', 3)	# 4-6
    sprite('tg112_02', 3)	# 7-9
    sprite('tg112_03', 3)	# 10-12
    sprite('tg112_04', 3)	# 13-15
    sprite('tg112_05', 3)	# 16-18
    sprite('tg112_06', 3)	# 19-21
    sprite('tg112_07', 3)	# 22-24
    sprite('tg112_08', 3)	# 25-27
    sprite('tg112_09', 3)	# 28-30
    sprite('tg112_10', 3)	# 31-33

@State
def CmnActUkemiLandN():
    sprite('tg112_00', 3)	# 1-3
    sprite('tg112_01', 3)	# 4-6
    sprite('tg112_02', 3)	# 7-9
    sprite('tg112_03', 3)	# 10-12
    sprite('tg112_04', 3)	# 13-15
    sprite('tg112_05', 3)	# 16-18
    sprite('tg112_06', 3)	# 19-21
    sprite('tg112_07', 3)	# 22-24
    sprite('tg112_08', 3)	# 25-27
    sprite('tg112_09', 3)	# 28-30
    sprite('tg112_10', 3)	# 31-33

@State
def CmnActUkemiLandNLanding():
    sprite('tg024_01', 3)	# 1-3
    sprite('tg024_02', 3)	# 4-6
    sprite('tg024_03', 3)	# 7-9
    sprite('tg024_04', 3)	# 10-12

@State
def CmnActMidGuardPre():
    sprite('tg040_00', 3)	# 1-3
    sprite('tg040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    sprite('tg040_02', 3)	# 1-3

@State
def CmnActMidGuardEnd():
    sprite('tg040_01', 3)	# 1-3
    sprite('tg040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('tg040_03', 3)	# 1-3
    sprite('tg040_02', 3)	# 4-6

@State
def CmnActMidHeavyGuardEnd():
    sprite('tg040_01', 3)	# 1-3
    sprite('tg040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('tg041_00', 3)	# 1-3
    sprite('tg041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('tg041_02', 3)	# 1-3

@State
def CmnActHighGuardEnd():
    sprite('tg041_01', 3)	# 1-3
    sprite('tg041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('tg041_03', 3)	# 1-3
    sprite('tg041_02', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('tg041_01', 3)	# 1-3
    sprite('tg041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('tg043_00', 3)	# 1-3
    sprite('tg043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    sprite('tg043_02', 3)	# 1-3

@State
def CmnActCrouchGuardEnd():
    sprite('tg043_01', 3)	# 1-3
    sprite('tg043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('tg043_03', 3)	# 1-3
    sprite('tg043_02', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('tg043_01', 3)	# 1-3
    sprite('tg043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('tg045_00', 3)	# 1-3
    sprite('tg045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    sprite('tg045_02', 3)	# 1-3

@State
def CmnActAirGuardEnd():
    sprite('tg045_01', 3)	# 1-3
    sprite('tg045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('tg045_03', 3)	# 1-3
    sprite('tg045_02', 3)	# 4-6

@State
def CmnActAirHeavyGuardEnd():
    sprite('tg045_01', 3)	# 1-3
    sprite('tg045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('tg090_00', 2)	# 1-2
    sprite('tg090_01', 2)	# 3-4
    sprite('tg090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('tg090_03', 6)	# 6-11
    sprite('tg090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    pass

@State
def CmnActGuardBreakAir():
    pass

@State
def CmnActAirTurn():
    sprite('tg025_00', 4)	# 1-4
    sprite('tg025_01', 4)	# 5-8
    sprite('tg025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('tg040_02', 1)	# 1-1
    sprite('tg040_01', 3)	# 2-4
    sprite('tg040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('tg312_00', 4)	# 1-4
    sprite('tg312_01', 4)	# 5-8
    sprite('tg312_01', 2)	# 9-10
    sprite('tg312_03', 3)	# 11-13	 **attackbox here**
    sprite('tg312_04', 5)	# 14-18
    sprite('tg312_05', 5)	# 19-23
    sprite('tg312_06', 5)	# 24-28
    sprite('tg312_07', 5)	# 29-33

@State
def CmnActAirLockWait():
    sprite('tg045_02', 1)	# 1-1
    sprite('tg045_01', 3)	# 2-4
    sprite('tg045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('tg322_00', 5)	# 1-5
    sprite('tg322_01', 2)	# 6-7
    sprite('tg322_02', 1)	# 8-8
    sprite('tg322_03', 3)	# 9-11	 **attackbox here**
    sprite('tg322_04', 4)	# 12-15
    sprite('tg322_05', 4)	# 16-19

@State
def CmnActLandSpin():
    pass

@State
def CmnActLandSpinDown():
    pass

@State
def CmnActVertSpin():
    pass

@State
def CmnActSlideAir():
    label(0)
    sprite('tg077_00', 2)	# 1-2
    sprite('tg077_01', 2)	# 3-4
    sprite('tg077_00ex01', 2)	# 5-6
    sprite('tg077_01ex01', 2)	# 7-8
    sprite('tg077_00ex02', 2)	# 9-10
    sprite('tg077_01ex02', 2)	# 11-12
    sprite('tg077_00ex03', 2)	# 13-14
    sprite('tg077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('tg077_02', 3)	# 1-3
    label(0)
    sprite('tg077_03', 3)	# 4-6
    sprite('tg077_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('tg077_05', 3)	# 1-3
    sprite('tg077_06', 3)	# 4-6
    sprite('tg077_07', 3)	# 7-9

@State
def CmnActAomukeSlideKeep():
    pass

@State
def CmnActAomukeSlideEnd():
    pass

@State
def CmnActBurstBegin():
    pass

@State
def CmnActBurstLoop():
    pass

@State
def CmnActBurstEnd():
    pass

@State
def CmnActAirBurstBegin():
    pass

@State
def CmnActAirBurstLoop():
    pass

@State
def CmnActAirBurstEnd():
    pass

@State
def CmnActOverDriveBegin():
    sprite('tg333_00', 3)	# 1-3
    sprite('tg333_01', 3)	# 4-6
    sprite('tg333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_0('tgef_overdrive_bigen', 0)
    GFX_0('tgef_overdrive_bigen', 1)
    sprite('tg333_03', 32767)	# 10-32776
    GFX_0('EMB_TG_OD', -1)
    GFX_0('tgef_overdrive_eye', 2)
    GFX_0('tgef_overdrive_eye', 3)
    GFX_0('tgef_overdrive_loop', 0)
    GFX_0('tgef_overdrive_loop2', 0)
    GFX_0('tgef_overdrive_loop3', 0)
    GFX_0('tgef_overdrive_loop', 1)
    GFX_0('tgef_overdrive_loop2', 1)
    GFX_0('tgef_overdrive_loop3', 1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('tg333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    GFX_0('tgef_overdrive_eye_keep', 2)
    GFX_0('tgef_overdrive_eye_keep', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    sprite('tg333_05', 3)	# 4-6
    Unknown26('tgef_overdrive_eye_keep')
    GFX_0('tgef_overdrive_eyeflash', 2)
    GFX_0('tgef_overdrive_eyeflash', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 7-9
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    label(0)
    sprite('tg333_05', 3)	# 10-12
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 13-15
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('tg333_07', 4)	# 1-4
    Unknown26('tgef_overdrive_eyeflash')
    sprite('tg333_08', 4)	# 5-8
    sprite('tg333_09', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('tg333_10', 3)	# 1-3
    sprite('tg333_11', 3)	# 4-6
    sprite('tg333_12', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_1('tgef_overdrive_bigen', 0)
    GFX_1('tgef_overdrive_bigen', 1)
    sprite('tg333_13', 32767)	# 10-32776
    GFX_0('EMB_TG_OD', -1)
    GFX_0('tgef_overdrive_eye', 2)
    GFX_0('tgef_overdrive_eye', 3)
    GFX_0('tgef_overdrive_loop', 0)
    GFX_0('tgef_overdrive_loop2', 0)
    GFX_0('tgef_overdrive_loop3', 0)
    GFX_0('tgef_overdrive_loop', 1)
    GFX_0('tgef_overdrive_loop2', 1)
    GFX_0('tgef_overdrive_loop3', 1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('tg333_14', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    GFX_0('tgef_overdrive_eye_keep', 2)
    GFX_0('tgef_overdrive_eye_keep', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    sprite('tg333_05', 3)	# 4-6
    Unknown26('tgef_overdrive_eye_keep')
    GFX_0('tgef_overdrive_eyeflash', 2)
    GFX_0('tgef_overdrive_eyeflash', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 7-9
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    label(0)
    sprite('tg333_05', 3)	# 10-12
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 13-15
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('tg333_15', 4)	# 1-4
    Unknown26('tgef_overdrive_eyeflash')
    sprite('tg333_16', 4)	# 5-8
    sprite('tg333_17', 4)	# 9-12
    label(0)
    sprite('tg020_07', 4)	# 13-16
    sprite('tg020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('tg333_00', 3)	# 1-3
    sprite('tg333_01', 3)	# 4-6
    sprite('tg333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_0('tgef_overdrive_bigen', 0)
    GFX_0('tgef_overdrive_bigen', 1)
    sprite('tg333_03', 32767)	# 10-32776
    GFX_0('EMB_TG_OD', -1)
    GFX_0('tgef_overdrive_eye', 2)
    GFX_0('tgef_overdrive_eye', 3)
    GFX_0('tgef_overdrive_loop', 0)
    GFX_0('tgef_overdrive_loop2', 0)
    GFX_0('tgef_overdrive_loop3', 0)
    GFX_0('tgef_overdrive_loop', 1)
    GFX_0('tgef_overdrive_loop2', 1)
    GFX_0('tgef_overdrive_loop3', 1)

@State
def CmnActCrossRushLoop():
    sprite('tg333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    GFX_0('tgef_overdrive_eye_keep', 2)
    GFX_0('tgef_overdrive_eye_keep', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    sprite('tg333_05', 3)	# 4-6
    Unknown26('tgef_overdrive_eye_keep')
    GFX_0('tgef_overdrive_eyeflash', 2)
    GFX_0('tgef_overdrive_eyeflash', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 7-9
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    label(0)
    sprite('tg333_05', 3)	# 10-12
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 13-15
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('tg333_07', 4)	# 1-4
    Unknown26('tgef_overdrive_eyeflash')
    sprite('tg333_08', 4)	# 5-8
    sprite('tg333_09', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('tg333_10', 3)	# 1-3
    sprite('tg333_11', 3)	# 4-6
    sprite('tg333_12', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_1('tgef_overdrive_bigen', 0)
    GFX_1('tgef_overdrive_bigen', 1)
    sprite('tg333_13', 32767)	# 10-32776
    GFX_0('EMB_TG_OD', -1)
    GFX_0('tgef_overdrive_eye', 2)
    GFX_0('tgef_overdrive_eye', 3)
    GFX_0('tgef_overdrive_loop', 0)
    GFX_0('tgef_overdrive_loop2', 0)
    GFX_0('tgef_overdrive_loop3', 0)
    GFX_0('tgef_overdrive_loop', 1)
    GFX_0('tgef_overdrive_loop2', 1)
    GFX_0('tgef_overdrive_loop3', 1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('tg333_14', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    GFX_0('tgef_overdrive_eye_keep', 2)
    GFX_0('tgef_overdrive_eye_keep', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    sprite('tg333_05', 3)	# 4-6
    Unknown26('tgef_overdrive_eye_keep')
    GFX_0('tgef_overdrive_eyeflash', 2)
    GFX_0('tgef_overdrive_eyeflash', 3)
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 7-9
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    label(0)
    sprite('tg333_05', 3)	# 10-12
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    sprite('tg333_06', 3)	# 13-15
    GFX_0('tgef_overdrive', 0)
    GFX_0('tgef_overdrive', 1)
    GFX_0('tgef_overdrive_thunder', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('tg333_15', 4)	# 1-4
    Unknown26('tgef_overdrive_eyeflash')
    sprite('tg333_16', 4)	# 5-8
    sprite('tg333_17', 4)	# 9-12
    label(0)
    sprite('tg020_07', 4)	# 13-16
    sprite('tg020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('tg331_00', 4)	# 1-4
    label(0)
    sprite('tg331_01', 3)	# 5-7
    sprite('tg331_02', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('tg331_03', 3)	# 1-3
    label(0)
    sprite('tg331_04', 3)	# 4-6
    sprite('tg331_05', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('tg331_06', 3)	# 1-3
    sprite('tg331_07', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('tg332_00', 4)	# 1-4
    label(0)
    sprite('tg332_01', 3)	# 5-7
    sprite('tg332_02', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('tg332_03', 3)	# 1-3
    label(0)
    sprite('tg332_04', 2)	# 4-5
    sprite('tg332_05', 2)	# 6-7
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('tg332_06', 3)	# 1-3
    sprite('tg332_07', 3)	# 4-6
    sprite('tg020_05', 3)	# 7-9
    sprite('tg020_06', 3)	# 10-12
    label(0)
    sprite('tg020_07', 4)	# 13-16
    sprite('tg020_08', 4)	# 17-20
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

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('tg260_04', 3)	# 26-28	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    label(1)
    sprite('tg260_05ex', 3)	# 29-31	 **attackbox here**
    sprite('tg260_04ex', 3)	# 32-34	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('tg260_06', 13)	# 35-47	 **attackbox here**
    Unknown8000(100, 1, 1)
    SFX_3('tgse_26')
    Unknown1084(1)
    ScreenShake(0, 7500)
    SFX_0('213_bound_1')
    GFX_1('tgef_dustB', 0)
    GFX_1('tgef_dustB', 1)
    GFX_1('tgef_dustA', 2)
    sprite('tg260_07', 4)	# 48-51
    sprite('tg260_08', 4)	# 52-55
    sprite('tg260_09', 4)	# 56-59

@State
def CmnActChangePartnerQuickIn():
    sprite('tg233_12', 3)	# 1-3	 **attackbox here**
    sprite('tg233_14', 5)	# 4-8
    sprite('tg233_15', 7)	# 9-15
    sprite('tg233_16', 7)	# 16-22
    sprite('tg233_17', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('tg033_03', 3)	# 1-3
    sprite('tg033_04', 3)	# 4-6
    sprite('tg033_03', 3)	# 7-9
    sprite('tg033_04', 3)	# 10-12
    sprite('tg033_03', 3)	# 13-15
    sprite('tg033_04', 3)	# 16-18
    sprite('tg033_03', 3)	# 19-21
    sprite('tg033_04', 3)	# 22-24
    sprite('tg033_03', 3)	# 25-27
    sprite('tg033_04', 3)	# 28-30
    sprite('tg033_03', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('tg033_00', 1)	# 1-1
    sprite('tg033_01', 1)	# 2-2
    sprite('tg033_02', 1)	# 3-3
    sprite('tg033_03', 3)	# 4-6
    sprite('tg033_04', 3)	# 7-9
    loopRest()
    label(0)
    sprite('tg033_03', 3)	# 10-12
    sprite('tg033_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg033_05', 2)	# 16-17
    sprite('tg033_06', 2)	# 18-19
    sprite('tg033_07', 1)	# 20-20
    sprite('tg033_08', 1)	# 21-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('tg300_00', 7)	# 1-7
    sprite('tg300_01', 8)	# 8-15
    sprite('tg300_02', 10)	# 16-25
    sprite('tg300_03', 10)	# 26-35
    sprite('tg300_04', 10)	# 36-45
    sprite('tg300_02', 10)	# 46-55
    sprite('tg300_03', 10)	# 56-65
    sprite('tg300_04', 10)	# 66-75
    sprite('tg300_05', 5)	# 76-80
    sprite('tg300_06', 6)	# 81-86

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
    sprite('tg020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('tg020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('tg010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    ScreenShake(0, 3500)
    SFX_0('019_quake_0')
    SFX_3('tgse_26')
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown2006()
        Unknown11063(1)
    sprite('tg405_00', 5)	# 1-5
    SFX_3('tgse_03')
    sprite('tg405_01', 1)	# 6-6
    sprite('tg405_01', 4)	# 7-10
    sprite('tg405_02', 5)	# 11-15
    GFX_1('tgef_stock_AM', 0)
    SFX_3('tgse_27')
    sprite('tg405_02', 5)	# 16-20
    sprite('tg405_02', 5)	# 21-25
    sprite('tg405_02', 5)	# 26-30
    GFX_1('tgef_stock_AM', 0)
    SFX_3('tgse_27')
    sprite('tg405_02', 5)	# 31-35
    sprite('tg405_02', 5)	# 36-40
    sprite('tg405_02', 5)	# 41-45
    GFX_1('tgef_stock_AM', 0)
    SFX_3('tgse_27')
    sprite('tg405_02', 5)	# 46-50
    sprite('tg405_02', 5)	# 51-55
    clearUponHandler(67)
    clearUponHandler(68)
    sprite('tg405_03', 4)	# 56-59
    GFX_1('tgef_stock', 0)
    ScreenShake(0, 5000)
    sprite('tg405_04', 6)	# 60-65
    SFX_3('tgse_02')
    SFX_0('200_walk_normal_2')
    sprite('tg405_05', 7)	# 66-72
    sprite('tg405_06', 4)	# 73-76
    sprite('tg403_00', 3)	# 77-79
    sprite('tg403_01', 3)	# 80-82
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    GFX_0('ShotObjCharge', 1)
    sprite('tg403_02', 3)	# 83-85
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    sprite('tg403_03', 3)	# 86-88
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    sprite('tg403_04', 3)	# 89-91
    Unknown7007('6274673230355f300000000000000000640000006274673230355f310000000000000000640000006274673230355f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('ShotMagicCircle', 1)
    sprite('tg403_05', 5)	# 92-96	 **attackbox here**
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('StayMagneticB', 3)
    GFX_0('StayMagneticB', 4)
    GFX_0('ShotObj_AS', 6)
    SFX_3('tgse_08')
    GFX_1('tgef_side_shockA', 5)
    GFX_0('tgef_tg403pla', 7)
    ScreenShake(0, 5000)
    sprite('tg403_06', 17)	# 97-113
    sprite('tg403_07', 4)	# 114-117
    sprite('tg403_08', 4)	# 118-121
    sprite('tg403_10', 6)	# 122-127
    ExitState()
    label(0)
    sprite('tg405_03', 4)	# 128-131
    clearUponHandler(67)
    clearUponHandler(68)
    GFX_1('tgef_stock', 0)
    ScreenShake(0, 5000)
    setInvincible(0)
    sprite('tg405_04', 6)	# 132-137
    SFX_3('tgse_02')
    SFX_0('200_walk_normal_2')
    sprite('tg405_05', 4)	# 138-141
    sprite('tg405_06', 4)	# 142-145

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown2006()
        Unknown11063(1)
    sprite('tg405_00', 5)	# 1-5
    SFX_3('tgse_03')
    sprite('tg405_01', 1)	# 6-6
    sprite('tg405_01', 4)	# 7-10
    sprite('tg405_02', 5)	# 11-15
    GFX_1('tgef_stock_AM', 0)
    SFX_3('tgse_27')
    sprite('tg405_02', 5)	# 16-20
    sprite('tg405_02', 5)	# 21-25
    clearUponHandler(67)
    clearUponHandler(68)
    sprite('tg405_03', 4)	# 26-29
    GFX_1('tgef_stock', 0)
    ScreenShake(0, 5000)
    sprite('tg405_04', 6)	# 30-35
    SFX_3('tgse_02')
    SFX_0('200_walk_normal_2')
    sprite('tg405_05', 7)	# 36-42
    sprite('tg405_06', 4)	# 43-46
    sprite('tg403_00', 2)	# 47-48
    sprite('tg403_01', 2)	# 49-50
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    GFX_0('ShotObjCharge', 1)
    sprite('tg403_02', 2)	# 51-52
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    sprite('tg403_03', 2)	# 53-54
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    sprite('tg408_00', 3)	# 55-57
    Unknown7007('6274673230365f300000000000000000640000006274673230365f310000000000000000640000006274673230365f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('ShotMagicCircle', 1)
    sprite('tg408_01', 5)	# 58-62
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('StayMagneticB', 3)
    GFX_0('StayMagneticB', 4)
    GFX_0('AntiAirShotObj', 6)
    SFX_3('tgse_08')
    GFX_1('tgef_side_shockA', 5)
    GFX_0('tgef_tg403pla', 7)
    ScreenShake(0, 5000)
    sprite('tg408_02', 17)	# 63-79
    sprite('tg408_03', 4)	# 80-83
    sprite('tg403_08', 4)	# 84-87
    sprite('tg403_10', 6)	# 88-93
    ExitState()
    label(0)
    sprite('tg405_03', 4)	# 94-97
    clearUponHandler(67)
    clearUponHandler(68)
    GFX_1('tgef_stock', 0)
    ScreenShake(0, 5000)
    setInvincible(0)
    sprite('tg405_04', 6)	# 98-103
    SFX_3('tgse_02')
    SFX_0('200_walk_normal_2')
    sprite('tg405_05', 4)	# 104-107
    sprite('tg405_06', 4)	# 108-111

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(70)
        AirPushbackY(38000)
        Unknown9154(26)
        AirUntechableTime(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        HitAirUnblockable(0)
        PushbackX(20000)
        Unknown2004(1, 0)
        Unknown2006()
        Unknown11042(1)
    sprite('tg401_00', 2)	# 1-2
    sprite('tg401_01', 2)	# 3-4
    sprite('tg401_02', 2)	# 5-6
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    sprite('tg401_03', 6)	# 7-12
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_04', 2)	# 13-14
    Unknown7007('6274673230335f300000000000000000640000006274673230335f310000000000000000640000006274673230335f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    physicsXImpulse(150000)
    Unknown2015(175)
    sprite('tg401_05', 2)	# 15-16
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg401_06', 9)	# 17-25	 **attackbox here**
    GFX_0('RollingAttackEff', 3)
    Unknown1019(5)
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    SFX_0('213_bound_1')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_08', 1)	# 26-26
    Unknown1084(1)
    Recovery()
    sprite('tg401_08', 4)	# 27-30
    sprite('tg401_09', 4)	# 31-34
    sprite('tg401_10', 3)	# 35-37
    sprite('tg401_11', 3)	# 38-40
    sprite('tg401_12', 2)	# 41-42
    sprite('tg401_13', 2)	# 43-44

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
    Unknown2036(68, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-245000)
    Unknown1019(4)
    label(0)
    sprite('tg020_07', 4)	# 3-6
    sprite('tg020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('ChangePartnerDDOD_Exe')
    else:
        enterState('ChangePartnerDD_Exe')

@State
def ChangePartnerDD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown9190(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(72000)
        AirPushbackY(100)
        YImpluseBeforeWallbounce(0)
        Hitstop(18)
        AirUntechableTime(80)
        WallbounceReboundTime(0)
        Unknown9015(1)
        Unknown11056(0)
        Unknown23055('')
        setInvincible(1)
        Unknown2004(1, 0)
        Unknown30063(1)
    sprite('tg431_00', 4)	# 1-4
    SFX_3('tgse_01')
    sprite('tg431_01', 4)	# 5-8
    GFX_0('tgef_430_light', 0)
    sprite('tg431_02', 15)	# 9-23
    Unknown20000(1)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_02', 13)	# 24-36
    SFX_3('tgse_08')
    GFX_0('MTH_punch_str', 1)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_03', 3)	# 37-39
    Unknown20000(0)
    Unknown20009(1100)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_04', 2)	# 40-41
    GFX_0('tgef_430_light', 0)
    sprite('tg431_05', 2)	# 42-43
    GFX_0('tgef_430_light', 0)
    sprite('tg431_06ex', 3)	# 44-46	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    GFX_0('tgef_430_light', 2)
    GFX_0('tgef_appB', 3)
    GFX_0('tgef_DD_MH_finish', 4)
    SFX_0('016_explode_2')
    SFX_3('tgse_21')
    sprite('tg431_07ex', 3)	# 47-49	 **attackbox here**
    tag_voice(1, 'btg252_0', 'btg252_1', '', '')
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    GFX_0('tgef_430_light', 2)
    SFX_0('014_electric_s')
    sprite('tg431_08ex', 3)	# 50-52	 **attackbox here**
    sprite('tg431_09', 6)	# 53-58
    setInvincible(0)
    sprite('tg431_10', 6)	# 59-64
    GFX_0('tgef_430_light', 0)
    sprite('tg431_11', 6)	# 65-70
    sprite('tg431_12', 6)	# 71-76
    sprite('tg431_13', 6)	# 77-82
    sprite('tg431_14', 6)	# 83-88
    sprite('tg431_15', 6)	# 89-94

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(2500)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown9190(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(72000)
        AirPushbackY(100)
        YImpluseBeforeWallbounce(0)
        Hitstop(18)
        AirUntechableTime(80)
        WallbounceReboundTime(0)
        Unknown9015(1)
        Unknown11056(0)
        setInvincible(1)
        Unknown2004(1, 0)
        Unknown30063(1)
    sprite('tg431_00', 4)	# 1-4
    SFX_3('tgse_01')
    sprite('tg431_01', 4)	# 5-8
    GFX_0('tgef_430_light', 0)
    sprite('tg431_02', 15)	# 9-23
    Unknown20000(1)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_02', 13)	# 24-36
    SFX_3('tgse_08')
    GFX_0('MTH_punch_str', 1)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_03', 3)	# 37-39
    Unknown20000(0)
    Unknown20009(1100)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_04', 2)	# 40-41
    GFX_0('tgef_430_light', 0)
    sprite('tg431_05', 2)	# 42-43
    GFX_0('tgef_430_light', 0)
    sprite('tg431_06ex', 3)	# 44-46	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    GFX_0('tgef_430_light', 2)
    GFX_0('tgef_appB', 3)
    GFX_0('tgef_DD_MH_finish', 4)
    SFX_0('016_explode_2')
    SFX_3('tgse_21')
    sprite('tg431_07ex', 3)	# 47-49	 **attackbox here**
    tag_voice(1, 'btg252_0', 'btg252_1', '', '')
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    GFX_0('tgef_430_light', 2)
    SFX_0('014_electric_s')
    sprite('tg431_08ex', 3)	# 50-52	 **attackbox here**
    sprite('tg431_09', 6)	# 53-58
    setInvincible(0)
    sprite('tg431_10', 6)	# 59-64
    GFX_0('tgef_430_light', 0)
    sprite('tg431_11', 6)	# 65-70
    sprite('tg431_12', 6)	# 71-76
    sprite('tg431_13', 6)	# 77-82
    sprite('tg431_14', 6)	# 83-88
    sprite('tg431_15', 6)	# 89-94

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('tg300_00', 9)	# 1-9
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('tg300_01', 9)	# 10-18
    sprite('tg300_02', 9)	# 19-27
    sprite('tg300_03', 9)	# 28-36
    sprite('tg300_04', 9)	# 37-45
    sprite('tg300_02', 9)	# 46-54
    sprite('tg300_03', 9)	# 55-63
    sprite('tg300_04', 10)	# 64-73
    label(1)
    sprite('tg300_04', 1)	# 74-74
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('tg300_05', 4)	# 75-78
    sprite('tg300_06', 4)	# 79-82
    sprite('tg300_00', 4)	# 83-86

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown23027()

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('tg260_04', 3)	# 121-123	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('tg260_05ex', 3)	# 124-126	 **attackbox here**
    sprite('tg260_04ex', 3)	# 127-129	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('tg260_06', 13)	# 130-142	 **attackbox here**
    Unknown8000(100, 1, 1)
    SFX_3('tgse_26')
    Unknown1084(1)
    ScreenShake(0, 7500)
    SFX_0('213_bound_1')
    GFX_1('tgef_dustB', 0)
    GFX_1('tgef_dustB', 1)
    GFX_1('tgef_dustA', 2)
    sprite('tg260_07', 6)	# 143-148
    sprite('tg260_08', 6)	# 149-154
    sprite('tg260_09', 6)	# 155-160

@State
def CmnActChangeReturnAppealBurst():
    sprite('tg111_07', 6)	# 1-6
    ScreenShake(0, 3500)
    SFX_0('019_quake_0')
    SFX_3('tgse_26')
    sprite('tg111_08', 3)	# 7-9
    sprite('tg111_09', 3)	# 10-12
    sprite('tg111_09', 3)	# 13-15
    sprite('tg111_09', 3)	# 16-18
    sprite('tg111_09', 3)	# 19-21
    sprite('tg111_09', 3)	# 22-24
    sprite('tg111_09', 18)	# 25-42
    sprite('tg111_10', 6)	# 43-48
    sprite('tg111_11', 6)	# 49-54
    sprite('tg111_12', 30)	# 55-84

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP2(80)
        Unknown9154(21)
        AirUntechableTime(23)
        HitAirUnblockable(0)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('tg202_00', 3)	# 1-3
    sprite('tg202_01', 3)	# 4-6
    sprite('tg202_03', 4)	# 7-10
    SFX_0('005_swing_grap_2_2')
    sprite('tg202_05', 4)	# 11-14
    Unknown7009(2)
    sprite('tg202_06', 4)	# 15-18	 **attackbox here**
    sprite('tg202_07', 3)	# 19-21	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('tg202_08', 3)	# 22-24
    sprite('tg202_09', 3)	# 25-27
    sprite('tg202_10', 3)	# 28-30
    sprite('tg202_11', 3)	# 31-33
    sprite('tg202_12', 3)	# 34-36

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(80)
        PushbackX(-39900)
        AirPushbackX(-30000)
        AirPushbackY(-46000)
        Unknown9154(21)
        AirUntechableTime(25)
        Unknown9202(25)
        HitAirUnblockable(0)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('CommandThrow')
        HitOrBlockCancel('CommandThrowB2')
        HitOrBlockCancel('CommandThrowEX')
        HitOrBlockCancel('GETB')
        HitOrBlockCancel('GETB_OD')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown2018(0, 60)
        callSubroutine('MAGNET_RESET')

        def upon_23():
            SLOT_52 = 1
            clearUponHandler(23)
    sprite('tg210_00', 2)	# 1-2
    sprite('tg210_01', 2)	# 3-4
    sprite('tg210_02', 3)	# 5-7	 **attackbox here**
    GFX_0('tgef210_ShotDeleteex1', -1)
    SFX_0('014_electric_s')
    Unknown21003(1500, 650)
    sprite('tg210_02', 2)	# 8-9	 **attackbox here**
    GFX_0('tgef210_ShotDeleteex2', -1)
    SFX_0('014_electric_s')
    loopRest()

    def upon_3():
        if SLOT_52:
            sendToLabel(0)
    sprite('tg210_02', 2)	# 10-11	 **attackbox here**
    sprite('tg210_02', 2)	# 12-13	 **attackbox here**
    sprite('tg210_02', 2)	# 14-15	 **attackbox here**
    sprite('tg210_02', 2)	# 16-17	 **attackbox here**
    setInvincible(1)
    Unknown22019('0100000001000000000000000100000000000000')
    Unknown22030(0)
    GuardPoint_(1)
    Unknown22035(50)
    Unknown22031(15, -1)
    Unknown8004(100, 1, 1)
    Unknown21003(2300, 650)
    sprite('tg210_02', 2)	# 18-19	 **attackbox here**
    sprite('tg210_02', 2)	# 20-21	 **attackbox here**
    sprite('tg210_02', 2)	# 22-23	 **attackbox here**
    sprite('tg210_02', 2)	# 24-25	 **attackbox here**
    sprite('tg210_02', 2)	# 26-27	 **attackbox here**
    sprite('tg210_02', 2)	# 28-29	 **attackbox here**
    sprite('tg210_02', 2)	# 30-31	 **attackbox here**
    sprite('tg210_02', 2)	# 32-33	 **attackbox here**
    sprite('tg210_02', 2)	# 34-35	 **attackbox here**
    sprite('tg210_02', 2)	# 36-37	 **attackbox here**
    sprite('tg210_02', 2)	# 38-39	 **attackbox here**
    sprite('tg210_02', 1)	# 40-40	 **attackbox here**
    sprite('tg210_02', 1)	# 41-41	 **attackbox here**
    Damage(2500)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(11)
    Unknown9154(30)
    AirUntechableTime(26)
    Unknown9202(26)
    Hitstop(15)
    label(0)
    clearUponHandler(23)
    clearUponHandler(3)
    sprite('tg210_02', 3)	# 42-44	 **attackbox here**
    GFX_0('tgef210_ShotDelete', -1)
    SFX_0('014_electric_s')
    sprite('tg210_03', 3)	# 45-47	 **attackbox here**
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    sprite('tg210_04', 2)	# 48-49	 **attackbox here**
    Unknown7009(1)
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    SFX_3('tgse_20')
    sprite('tg210_05', 2)	# 50-51	 **attackbox here**
    Unknown21003(0, 0)
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    sprite('tg210_06', 1)	# 52-52	 **attackbox here**
    sprite('tg210_06', 3)	# 53-55	 **attackbox here**
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    sprite('tg210_07', 3)	# 56-58	 **attackbox here**
    SFX_0('014_electric_s')
    sprite('tg210_08', 3)	# 59-61	 **attackbox here**
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('tg210_09', 3)	# 62-64	 **attackbox here**
    sprite('tg210_10', 3)	# 65-67
    sprite('tg210_10', 6)	# 68-73
    sprite('tg210_11', 3)	# 74-76
    sprite('tg210_12', 3)	# 77-79
    sprite('tg210_13', 3)	# 80-82
    sprite('tg210_14', 3)	# 83-85

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AttackP2(85)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(15000)
        AirPushbackY(25000)
        PushbackX(48000)
        AirUntechableTime(30)
        HitAirUnblockable(0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1200)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('CmnActCrushAttack')
        callSubroutine('MAGNET_RESET')
    sprite('tg203_00', 4)	# 1-4
    sprite('tg203_01', 4)	# 5-8
    Unknown21003(1500, 1500)
    SFX_3('tgse_03')
    sprite('tg203_02', 3)	# 9-11
    sprite('tg203_03', 3)	# 12-14
    Unknown7009(3)
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    SFX_0('014_electric_m')
    Unknown23118(0)
    Unknown23119(16744448, 12, 2)
    sprite('tg203_04', 3)	# 15-17	 **attackbox here**
    Unknown21003(4000, 3600)
    GFX_0('StayMagneticB', 0)
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_m')
    sprite('tg203_05', 2)	# 18-19	 **attackbox here**
    GFX_1('tgef_side_shockA', 3)
    sprite('tg203_06', 3)	# 20-22	 **attackbox here**
    SFX_3('tgse_26')
    GFX_0('tgef203mc', 0)
    GFX_0('AddMagnetPtc', 0)
    ScreenShake(0, 5000)
    GFX_0('StayMagneticB203', 0)
    GFX_0('StayMagneticB203', 1)
    GFX_0('StayMagneticB203', 2)
    GFX_0('StayMagneticB203', 3)
    GFX_0('StayMagneticB203', 4)
    GFX_0('StayMagneticB203', 5)
    Unknown21003(0, 0)
    sprite('tg203_06', 1)	# 23-23	 **attackbox here**
    sprite('tg203_07', 5)	# 24-28	 **attackbox here**
    Unknown4048(290000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000000000000')
    Unknown4048(250000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    sprite('tg203_08', 6)	# 29-34	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('tg203_09', 6)	# 35-40
    SFX_3('tgse_00')
    Unknown3029(0)
    sprite('tg203_10', 6)	# 41-46
    sprite('tg203_11', 6)	# 47-52
    sprite('tg203_12', 6)	# 53-58

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AttackP1(80)
        AttackP2(85)
        HitOverhead(2)
        GroundedHitstunAnimation(10)
        AirPushbackX(-1000)
        AirPushbackY(-44000)
        Unknown9310(1)
        HitAirUnblockable(0)

        def upon_STATE_END():
            Unknown12046(35)
        HitOrBlockCancel('NmlAtk5B')

        def upon_78():
            HitOrBlockCancel('Oiuchi')
    sprite('tg212_01', 6)	# 1-6
    sprite('tg212_03', 6)	# 7-12
    sprite('tg212_05', 6)	# 13-18
    sprite('tg212_07', 3)	# 19-21
    Unknown12046(70)
    SFX_0('005_swing_grap_2_2')
    Unknown7007('6274673130385f300000000000000000640000006274673130385f310000000000000000640000006274673130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('tg212_10', 2)	# 22-23
    Unknown12046(105)
    SFX_3('tgse_26')
    SFX_0('019_quake_0')
    sprite('tg212_11', 2)	# 24-25	 **attackbox here**
    Unknown12046(140)
    GFX_1('tgef_dustB', 0)
    GFX_0('ShockB', 1)
    ScreenShake(0, 5000)
    sprite('tg212_12', 3)	# 26-28
    Recovery()
    Unknown2063()
    sprite('tg212_14', 8)	# 29-36
    sprite('tg212_16', 6)	# 37-42
    Unknown12046(105)
    sprite('tg212_17', 4)	# 43-46
    Unknown12046(70)
    sprite('tg212_18', 3)	# 47-49
    Unknown12046(35)
    sprite('tg212_19', 4)	# 50-53
    sprite('tg212_20', 5)	# 54-58

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackX(2000)
        AirPushbackY(12000)
        HitAirUnblockable(0)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('tg200_00', 2)	# 1-2
    Unknown1051(60)
    sprite('tg200_01', 3)	# 3-5
    sprite('tg200_02', 2)	# 6-7
    Unknown7009(0)
    SFX_0('005_swing_grap_2_0')
    sprite('tg200_03', 3)	# 8-10	 **attackbox here**
    sprite('tg200_04', 6)	# 11-16
    Recovery()
    Unknown2063()
    sprite('tg200_05', 5)	# 17-21

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AttackP1(90)
        AirPushbackY(20000)
        HitLow(2)
        HitAirUnblockable(0)
        Unknown11058('0000000000000000010000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('tg201_01', 2)	# 1-2
    sprite('tg201_02', 1)	# 3-3
    sprite('tg201_02', 2)	# 4-5
    Unknown7009(1)
    sprite('tg201_03', 4)	# 6-9
    SFX_0('005_swing_grap_2_0')
    sprite('tg201_05', 3)	# 10-12	 **attackbox here**
    sprite('tg201_06', 5)	# 13-17
    Recovery()
    Unknown2063()
    sprite('tg201_07', 5)	# 18-22
    sprite('tg201_09', 4)	# 23-26

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(8000)
        HitAirUnblockable(0)
        AirUntechableTime(29)
        Unknown11028(21)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1200)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        callSubroutine('MAGNET_RESET')
    sprite('tg213_00', 2)	# 1-2
    sprite('tg213_01', 2)	# 3-4
    Unknown23118(0)
    Unknown23119(16744448, 12, 2)
    sprite('tg213_02', 1)	# 5-5	 **attackbox here**
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    SFX_0('014_electric_sl')
    SFX_0('014_electric_m')
    SFX_3('tgse_00')
    sprite('tg213_02', 3)	# 6-8	 **attackbox here**
    Unknown7007('6274673130345f300000000000000000640000006274673130345f310000000000000000640000006274673130345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('tg213_03', 4)	# 9-12	 **attackbox here**
    GFX_0('StayMagneticB', 0)
    ScreenShake(0, 5000)
    Unknown21003(6000, 3000)
    sprite('tg213_04', 2)	# 13-14	 **attackbox here**
    Unknown21003(4000, 2000)
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('AddMagnetPtc', 0)
    GFX_0('tgef213mc', 0)
    Unknown4048(290000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    Unknown4048(250000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000002000000')
    sprite('tg213_05', 2)	# 15-16	 **attackbox here**
    Unknown21003(0, 0)
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    physicsXImpulse(-8000)
    sprite('tg213_06', 4)	# 17-20
    Recovery()
    Unknown2063()
    physicsXImpulse(-1000)
    sprite('tg213_07', 3)	# 21-23
    Unknown1084(1)
    sprite('tg213_08', 3)	# 24-26
    sprite('tg213_09', 3)	# 27-29
    sprite('tg213_10', 3)	# 30-32
    sprite('tg213_11', 3)	# 33-35
    Unknown1084(1)

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(36000)
        AirUntechableTime(25)
        HitAirUnblockable(0)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('tg232_00', 2)	# 1-2
    sprite('tg232_01', 2)	# 3-4
    sprite('tg232_02', 2)	# 5-6
    sprite('tg232_03', 2)	# 7-8
    SFX_0('005_swing_grap_2_2')
    sprite('tg232_04', 2)	# 9-10
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    Unknown7007('6274673130365f300000000000000000640000006274673130365f310000000000000000640000006274673130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('tg232_05', 2)	# 11-12
    sprite('tg232_06', 2)	# 13-14	 **attackbox here**
    setInvincible(0)
    sprite('tg232_07', 2)	# 15-16	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('tg232_08', 8)	# 17-24
    sprite('tg232_09', 6)	# 25-30
    sprite('tg232_10', 5)	# 31-35
    sprite('tg232_11', 4)	# 36-39
    sprite('tg232_12', 4)	# 40-43

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        Unknown9154(21)
        AirUntechableTime(40)
        AirHitstunAnimation(9)
        AirPushbackX(15000)
        HitAirUnblockable(0)
        PushbackX(20000)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0000000000000000000000000100000000000000')
        Unknown22024(20000)
        Unknown22030(0)
        Unknown22031(-1, -1)

        def upon_52():
            if Unknown23037():
                GFX_0('RollAtkShotBreak', 102)
                clearUponHandler(52)
        Unknown2004(1, 0)
        HitCancel('NmlAtk2A')
        HitCancel('NmlAtk2B')
        HitCancel('CmnActCrushAttack')
        HitCancel('NmlAtk2C')
        WhiffCancel('NmlAtk5B2nd')
        JumpCancel_(0)

        def upon_24():
            SLOT_52 = 1
            clearUponHandler(24)
    sprite('tg401_00', 3)	# 1-3
    sprite('tg401_01', 3)	# 4-6
    sprite('tg401_02', 2)	# 7-8
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    sprite('tg401_02', 2)	# 9-10
    Unknown22019('0100000001000000000000000100000000000000')
    sprite('tg401_03', 4)	# 11-14
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_03', 6)	# 15-20
    sprite('tg401_03', 1)	# 21-21
    loopRest()

    def upon_3():
        if SLOT_52:
            sendToLabel(0)
    sprite('tg401_03', 5)	# 22-26
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_03', 5)	# 27-31
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_03', 5)	# 32-36
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    loopRest()
    SLOT_53 = 1
    sprite('tg401_03', 5)	# 37-41
    ScreenShake(1000, 4000)
    Unknown8004(100, 1, 1)
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_03', 5)	# 42-46
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_03', 5)	# 47-51
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    loopRest()
    SLOT_53 = 2
    Damage(2500)
    label(0)
    clearUponHandler(24)
    clearUponHandler(3)
    sprite('tg401_03', 4)	# 52-55
    sprite('tg401_04', 3)	# 56-58
    Unknown22019('0000000000000000000000000100000000000000')
    tag_voice(1, 'btg203_0', 'btg203_1', 'btg203_2', '')
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    physicsXImpulse(75000)
    if (SLOT_53 == 1):
        physicsXImpulse(100000)
    if (SLOT_53 == 2):
        physicsXImpulse(150000)
    sprite('tg401_05', 2)	# 59-60
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg401_06', 4)	# 61-64	 **attackbox here**

    def upon_ON_HIT_OR_BLOCK():
        WhiffCancelEnable(1)
        clearUponHandler(10)
    GFX_0('RollingAttackEff', 3)
    if (SLOT_53 == 2):
        AirPushbackX(30000)
    Unknown1019(5)
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    SFX_0('213_bound_1')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_08', 1)	# 65-65
    WhiffCancelEnable(1)
    Unknown1084(1)
    Recovery()
    sprite('tg401_08', 4)	# 66-69
    setInvincible(0)
    sprite('tg401_09', 4)	# 70-73
    sprite('tg401_10', 3)	# 74-76
    WhiffCancelEnable(0)
    sprite('tg401_11', 3)	# 77-79
    sprite('tg401_12', 2)	# 80-81
    sprite('tg401_13', 2)	# 82-83

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        GroundedHitstunAnimation(9)
        AirPushbackX(1000)
        AirPushbackY(-48000)
        Unknown9310(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        HitOverhead(2)
        Unknown11058('0000000001000000000000000000000000000000')
        JumpCancel_(0)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0100000001000000000000000100000000000000')
        Unknown22030(0)
        Unknown22031(-2, -1)

        def upon_42():
            GFX_0('RollAtkShotBreak', 102)
            clearUponHandler(42)
        physicsXImpulse(12000)
        Unknown1051(60)
        Unknown2004(1, 0)

        def upon_78():
            SLOT_51 = 1
    sprite('tg402_00', 3)	# 1-3
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    sprite('tg402_01', 3)	# 4-6
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    sprite('tg402_02', 3)	# 7-9
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    Unknown1047(12000)
    sprite('tg402_03', 6)	# 10-15
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg402_04', 1)	# 16-16
    SFX_0('005_swing_grap_2_2')
    tag_voice(0, 'btg204_0', 'btg204_1', 'btg204_2', '')
    sprite('tg402_05', 1)	# 17-17
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('SledgeHammerEFF', 0)
    sprite('tg402_06', 1)	# 18-18
    sprite('tg402_07', 6)	# 19-24	 **attackbox here**
    Unknown1019(0)
    Unknown1051(0)
    setInvincible(0)
    SFX_3('tgse_20')
    SFX_0('213_bound_0')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('ShockB402', 6)
    Unknown8000(6, 1, 1)
    sprite('tg402_07', 10)	# 25-34	 **attackbox here**
    Recovery()
    if SLOT_51:
        HitOrBlockCancel('Oiuchi_B')
    Unknown23027()
    sprite('tg402_08', 4)	# 35-38
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg402_09', 4)	# 39-42
    sprite('tg402_10', 4)	# 43-46
    sprite('tg402_11', 4)	# 47-50
    sprite('tg402_12', 4)	# 51-54

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(5)
        AttackP1(80)
        AirHitstunAnimation(10)
        AirPushbackX(40000)
        AirPushbackY(0)
        Unknown9202(10)
        AirUntechableTime(31)
        Hitstop(15)
        Unknown11058('0000000000000000010000000000000000000000')
        HitAirUnblockable(0)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(9)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1200)
        callSubroutine('MAGNET_RESET')
    sprite('tg233_01', 5)	# 1-5
    sprite('tg233_02', 6)	# 6-11
    SFX_3('tgse_03')
    sprite('tg233_03', 4)	# 12-15
    Unknown21003(800, 100)
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    SFX_0('014_electric_m')
    Unknown23118(0)
    Unknown23119(16744448, 12, 2)
    sprite('tg233_03', 4)	# 16-19
    SFX_0('014_electric_m')
    sprite('tg233_06', 3)	# 20-22	 **attackbox here**
    sprite('tg233_08', 3)	# 23-25	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(40000)
    Unknown7007('6274673130355f300000000000000000640000006274673130355f310000000000000000640000006274673130355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('tg233_09', 6)	# 26-31	 **attackbox here**
    Unknown21003(5000, 100)
    Unknown1019(200)
    GFX_0('tgef233mc', 6)
    GFX_0('AddMagnetPtc', 6)
    GFX_0('StayMagneticB233', 1)
    GFX_0('StayMagneticB233', 2)
    GFX_0('StayMagneticB233', 3)
    GFX_0('StayMagneticB233', 4)
    GFX_0('StayMagneticB233', 5)
    ScreenShake(0, 5000)
    sprite('tg233_10', 4)	# 32-35	 **attackbox here**
    Recovery()
    SFX_3('tgse_26')
    loopRest()
    label(9)
    sprite('tg233_11', 3)	# 36-38	 **attackbox here**
    Unknown1019(20)
    Unknown21003(0, 0)
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    SFX_0('014_electric_m')
    Recovery()
    Unknown2063()
    sprite('tg233_12', 3)	# 39-41	 **attackbox here**
    sprite('tg233_14', 3)	# 42-44
    Unknown1019(0)
    sprite('tg233_15', 3)	# 45-47
    Unknown3029(0)
    sprite('tg233_16', 3)	# 48-50
    sprite('tg233_17', 3)	# 51-53

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(0)
        AirPushbackY(19000)
        AirUntechableTime(30)
        HitLow(2)
        HitAirUnblockable(0)
        HitOrBlockCancel('NmlAtk5B')

        def upon_78():
            HitOrBlockCancel('Oiuchi_C')
    sprite('tg234_00', 3)	# 1-3
    sprite('tg234_01', 3)	# 4-6
    sprite('tg234_02', 2)	# 7-8
    sprite('tg234_03', 2)	# 9-10
    Unknown7007('6274673130375f300000000000000000640000006274673130375f310000000000000000640000006274673130375f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_2')
    sprite('tg234_04', 2)	# 11-12
    sprite('tg234_05', 3)	# 13-15	 **attackbox here**
    sprite('tg234_06', 8)	# 16-23
    Recovery()
    Unknown2063()
    sprite('tg234_07', 5)	# 24-28
    sprite('tg234_08', 5)	# 29-33
    sprite('tg234_09', 4)	# 34-37

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(28000)
        AirHitstunAfterWallbounce(60)
        Unknown9118(70)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('tg251_00', 2)	# 1-2
    sprite('tg251_01', 2)	# 3-4
    sprite('tg251_03', 2)	# 5-6
    SFX_0('004_swing_grap_1_1')
    sprite('tg251_04', 4)	# 7-10	 **attackbox here**
    Unknown7009(1)
    SFX_0('014_electric_s')
    GFX_0('LoopHandAtk', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg251_05', 4)	# 11-14	 **attackbox here**
    SFX_0('014_electric_s')
    sprite('tg251_04', 4)	# 15-18	 **attackbox here**
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg251_05', 4)	# 19-22	 **attackbox here**
    SFX_0('014_electric_s')
    sprite('tg251_06', 5)	# 23-27
    Recovery()
    Unknown2063()
    sprite('tg251_07', 5)	# 28-32
    sprite('tg251_08', 5)	# 33-37
    sprite('tg251_09', 5)	# 38-42

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirUntechableTime(22)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('tg252_00', 6)	# 1-6
    sprite('tg252_02', 3)	# 7-9
    Unknown7009(4)
    SFX_0('004_swing_grap_1_2')
    sprite('tg252_04', 3)	# 10-12
    sprite('tg252_03', 5)	# 13-17	 **attackbox here**
    GFX_0('HeadBatAtk', 0)
    sprite('tg252_04', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('tg252_05', 3)	# 21-23
    sprite('tg252_06', 2)	# 24-25
    sprite('tg252_07', 2)	# 26-27
    sprite('tg252_09', 2)	# 28-29

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        PushbackX(-7000)
        AirPushbackX(8000)
        Unknown9154(25)
        AirUntechableTime(25)
        Hitstop(15)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1200)
        Unknown22004(8, 1)
        callSubroutine('MAGNET_RESET')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('tg253_00', 4)	# 1-4
    sprite('tg253_02', 5)	# 5-9
    SFX_3('tgse_03')
    sprite('tg253_03', 4)	# 10-13	 **attackbox here**
    Unknown21003(2500, 2500)
    Unknown7007('6274673130345f300000000000000000640000006274673130345f310000000000000000640000006274673130345f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('StayMagneticB', 3)
    GFX_0('StayMagneticB', 4)
    GFX_0('StayMagneticB', 4)
    SFX_0('014_electric_m')
    Unknown23118(0)
    Unknown23119(16744448, 12, 2)
    sprite('tg253_03', 4)	# 14-17	 **attackbox here**
    Unknown21003(5000, 5000)
    SFX_0('014_electric_m')
    sprite('tg253_04', 4)	# 18-21	 **attackbox here**
    Unknown21003(2500, 2500)
    SFX_0('005_swing_grap_2_2')
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    sprite('tg253_05', 1)	# 22-22	 **attackbox here**
    GFX_0('AddMagnetPtc', 0)
    GFX_0('tgef253mc', 1)
    GFX_0('StayMagneticB253', 0)
    GFX_0('StayMagneticB253', 1)
    GFX_0('StayMagneticB253', 2)
    GFX_0('StayMagneticB253', 3)
    GFX_0('StayMagneticB253', 4)
    sprite('tg253_05', 3)	# 23-25	 **attackbox here**
    Unknown21003(0, 0)
    sprite('tg253_06', 5)	# 26-30	 **attackbox here**
    SFX_0('014_electric_l')
    Recovery()
    Unknown2063()
    sprite('tg253_07', 4)	# 31-34	 **attackbox here**
    sprite('tg253_08', 3)	# 35-37
    sprite('tg253_09', 3)	# 38-40
    Unknown3029(0)
    sprite('tg253_10', 3)	# 41-43

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        Unknown9310(40)
        AirPushbackX(3000)
        AirPushbackY(-20000)
        Unknown11044(1)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11068(1)
        HitOverhead(0)
        Unknown2037(0)
        Unknown22004(4, 1)

        def upon_78():
            clearUponHandler(78)
            physicsXImpulse(0)
            physicsYImpulse(20000)
            Unknown1043()
            Unknown2037(1)
            Unknown11069('AirAssaultExe')
            JumpCancel_(0)
    sprite('tg409_00', 3)	# 1-3
    sprite('tg409_01', 3)	# 4-6
    Unknown1015(26000)
    Unknown1019(25)
    physicsYImpulse(18000)
    setGravity(1500)
    Unknown7007('6274673230385f300000000000000000640000006274673230385f3100000000000000006400000000000000000000000000000000000000640000000000000000000000000000000000000000000000')
    SLOT_66 = 0
    sprite('tg409_02', 2)	# 7-8
    sprite('tg409_03', 2)	# 9-10
    sprite('tg409_04', 2)	# 11-12
    SFX_0('005_swing_grap_2_2')
    sprite('tg409_05', 2)	# 13-14
    setGravity(1200)
    sprite('tg409_06', 3)	# 15-17	 **attackbox here**
    sprite('tg409_07', 3)	# 18-20	 **attackbox here**
    StartMultihit()
    sprite('tg409_08', 3)	# 21-23
    Recovery()
    sprite('keep', 1)	# 24-24
    if SLOT_2:
        enterState('AirAssaultExe')
    sprite('tg409_20', 3)	# 25-27
    Unknown1043()
    sprite('tg409_21', 3)	# 28-30
    sprite('tg409_22', 3)	# 31-33

@State
def AirAssaultExe():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Unknown9310(26)
        AirPushbackX(1000)
        AirPushbackY(-20000)
        Unknown11108('03000000')
        Unknown11068(1)
        Unknown30048(1)
        setInvincible(1)
        Unknown2017(0)
        Unknown1019(50)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        JumpCancel_(0)
    sprite('keep', 1)	# 1-1
    sprite('tg409_09', 5)	# 2-6
    Unknown2006()
    SLOT_67 = SLOT_19
    if (SLOT_67 > 750000):
        SLOT_67 = 750000
    SLOT_12 = SLOT_67
    Unknown1019(12)
    Unknown1019(12)
    sprite('tg409_10', 5)	# 7-11
    setGravity(1600)
    sprite('tg409_11', 5)	# 12-16
    label(0)
    sprite('tg409_12', 3)	# 17-19
    sprite('tg409_13', 3)	# 20-22
    gotoLabel(0)
    label(1)
    sprite('tg409_14', 10)	# 23-32	 **attackbox here**
    Unknown8004(100, 1, 1)
    ScreenShake(0, 30000)
    Unknown1084(1)
    sprite('tg409_15', 10)	# 33-42
    setInvincible(0)
    Recovery()
    sprite('tg409_16', 6)	# 43-48
    sprite('tg409_17', 6)	# 49-54
    sprite('tg409_18', 6)	# 55-60
    Unknown2017(1)
    sprite('tg409_19', 6)	# 61-66

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('tg411_00', 2)	# 1-2
    sprite('tg411_01', 1)	# 3-3
    sprite('tg411_01', 2)	# 4-5
    tag_voice(1, 'btg156_0', 'btg156_1', '', '')
    sprite('tg411_02', 3)	# 6-8
    sprite('tg411_03', 4)	# 9-12
    sprite('tg411_06', 3)	# 13-15
    SFX_3('tgse_20')
    sprite('tg411_07', 3)	# 16-18
    sprite('tg411_08', 3)	# 19-21
    SFX_0('005_swing_grap_2_2')
    sprite('tg411_09', 3)	# 22-24	 **attackbox here**
    GFX_0('tgef_guardcrash', 0)
    GFX_0('tgef_guardcrash_stump', 0)
    GFX_0('tgef_guardcrash_stump_b', 1)
    GFX_0('tgef_guardcrash_stump_b', 2)
    GFX_0('tgef_guardcrash_stump_b', 3)
    GFX_0('tgef_guardcrash_stump_b', 4)
    GFX_1('tgef_guardcrash_stamp_c', 0)
    ScreenShake(0, 15000)
    SFX_3('tgse_26')
    SFX_0('019_quake_0')
    sprite('tg411_10', 6)	# 25-30
    sprite('tg411_11', 6)	# 31-36
    sprite('tg411_12', 6)	# 37-42
    sprite('tg411_13', 6)	# 43-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('tg411_09', 3)	# 2-4	 **attackbox here**
    sprite('tg411_10', 3)	# 5-7
    sprite('tg411_11', 3)	# 8-10
    sprite('tg411_12', 3)	# 11-13
    sprite('tg411_13', 4)	# 14-17
    sprite('tg202_00', 3)	# 18-20
    sprite('tg202_01', 3)	# 21-23
    sprite('tg202_03', 3)	# 24-26
    SFX_0('005_swing_grap_2_2')
    sprite('tg202_05', 3)	# 27-29
    sprite('tg202_06', 1)	# 30-30	 **attackbox here**
    RefreshMultihit()
    sprite('tg202_07', 2)	# 31-32	 **attackbox here**
    StartMultihit()
    sprite('tg202_08', 2)	# 33-34
    sprite('tg202_09', 2)	# 35-36
    sprite('tg202_10', 2)	# 37-38
    sprite('tg010_00', 1)	# 39-39
    sprite('tg010_01', 1)	# 40-40
    sprite('tg232_00', 2)	# 41-42
    sprite('tg232_01', 2)	# 43-44
    sprite('tg232_02', 60)	# 45-104
    sprite('tg000_00', 6)	# 105-110
    sprite('tg000_01', 6)	# 111-116
    sprite('tg000_02', 6)	# 117-122
    sprite('tg000_03', 6)	# 123-128
    sprite('tg000_04', 6)	# 129-134
    sprite('tg000_05', 6)	# 135-140
    sprite('tg000_06', 6)	# 141-146
    sprite('tg000_05', 6)	# 147-152
    sprite('tg000_04', 6)	# 153-158
    sprite('tg000_03', 6)	# 159-164
    sprite('tg000_02', 6)	# 165-170
    sprite('tg000_01', 6)	# 171-176
    sprite('tg000_00', 6)	# 177-182
    sprite('tg000_01', 6)	# 183-188
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 189-194
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 195-200
    SFX_0('014_electric_s')
    sprite('tg000_04', 6)	# 201-206
    sprite('tg000_05', 6)	# 207-212
    sprite('tg000_06', 6)	# 213-218
    sprite('tg000_05', 6)	# 219-224
    sprite('tg000_04', 6)	# 225-230
    sprite('tg000_03', 6)	# 231-236
    sprite('tg000_02', 6)	# 237-242
    sprite('tg000_01', 6)	# 243-248
    label(0)
    sprite('tg000_00', 6)	# 249-254
    sprite('tg000_01', 6)	# 255-260
    sprite('tg000_02', 6)	# 261-266
    sprite('tg000_03', 6)	# 267-272
    sprite('tg000_04', 6)	# 273-278
    sprite('tg000_05', 6)	# 279-284
    sprite('tg000_06', 6)	# 285-290
    sprite('tg000_05', 6)	# 291-296
    sprite('tg000_04', 6)	# 297-302
    sprite('tg000_03', 6)	# 303-308
    sprite('tg000_02', 6)	# 309-314
    sprite('tg000_01', 6)	# 315-320
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 321-321

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('tg232_02', 4)	# 1-4
    sprite('tg232_03', 4)	# 5-8
    SFX_0('005_swing_grap_2_2')
    sprite('tg232_04', 3)	# 9-11
    tag_voice(0, 'btg157_0', 'btg157_1', '', '')
    sprite('tg232_05', 3)	# 12-14
    sprite('tg232_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('tg232_07', 2)	# 17-18	 **attackbox here**
    StartMultihit()
    sprite('tg232_08', 8)	# 19-26
    sprite('tg232_09', 6)	# 27-32
    sprite('tg232_10', 5)	# 33-37
    sprite('tg232_11', 4)	# 38-41
    sprite('tg232_12', 4)	# 42-45
    sprite('tg010_01', 4)	# 46-49
    sprite('tg010_00', 4)	# 50-53
    sprite('tg000_00', 6)	# 54-59
    sprite('tg000_01', 6)	# 60-65
    sprite('tg000_02', 6)	# 66-71
    sprite('tg000_03', 6)	# 72-77
    sprite('tg000_04', 6)	# 78-83
    sprite('tg000_05', 6)	# 84-89
    sprite('tg000_06', 6)	# 90-95
    sprite('tg000_05', 6)	# 96-101
    sprite('tg000_04', 6)	# 102-107
    sprite('tg000_03', 6)	# 108-113
    sprite('tg000_02', 6)	# 114-119
    sprite('tg000_01', 6)	# 120-125
    sprite('tg000_00', 6)	# 126-131
    sprite('tg000_01', 6)	# 132-137
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 138-143
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 144-149
    SFX_0('014_electric_s')
    sprite('tg000_04', 6)	# 150-155
    sprite('tg000_05', 6)	# 156-161
    sprite('tg000_06', 6)	# 162-167
    sprite('tg000_05', 6)	# 168-173
    sprite('tg000_04', 6)	# 174-179
    sprite('tg000_03', 6)	# 180-185
    sprite('tg000_02', 6)	# 186-191
    sprite('tg000_01', 6)	# 192-197
    label(0)
    sprite('tg000_00', 6)	# 198-203
    sprite('tg000_01', 6)	# 204-209
    sprite('tg000_02', 6)	# 210-215
    sprite('tg000_03', 6)	# 216-221
    sprite('tg000_04', 6)	# 222-227
    sprite('tg000_05', 6)	# 228-233
    sprite('tg000_06', 6)	# 234-239
    sprite('tg000_05', 6)	# 240-245
    sprite('tg000_04', 6)	# 246-251
    sprite('tg000_03', 6)	# 252-257
    sprite('tg000_02', 6)	# 258-263
    sprite('tg000_01', 6)	# 264-269
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 270-270

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('tg430_22', 1)	# 1-1
    teleportRelativeX(-95000)
    physicsXImpulse(-10000)
    sprite('tg430_21', 1)	# 2-2
    sprite('tg430_20', 1)	# 3-3
    sprite('tg430_19', 1)	# 4-4
    sprite('tg430_18', 2)	# 5-6
    Unknown1084(1)
    sprite('tg430_17', 2)	# 7-8	 **attackbox here**
    sprite('tg431_00', 1)	# 9-9
    sprite('tg431_01', 2)	# 10-11
    sprite('tg431_02', 2)	# 12-13
    sprite('tg431_03', 2)	# 14-15
    tag_voice(0, 'btg158_0', 'btg158_1', '', '')
    sprite('tg431_04', 2)	# 16-17
    sprite('tg431_05', 2)	# 18-19
    sprite('tg431_06', 4)	# 20-23	 **attackbox here**
    SFX_0('016_explode_2')
    SFX_3('tgse_21')
    sprite('tg431_07', 4)	# 24-27	 **attackbox here**
    sprite('tg431_08', 4)	# 28-31	 **attackbox here**
    sprite('tg431_09', 5)	# 32-36
    sprite('tg431_10', 4)	# 37-40
    sprite('tg431_11', 4)	# 41-44
    sprite('tg431_12', 4)	# 45-48
    sprite('tg431_13', 4)	# 49-52
    sprite('tg431_14', 4)	# 53-56
    sprite('tg431_15', 4)	# 57-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown30081('')
    sprite('tg401_00', 2)	# 26-27
    Unknown1086(22)
    teleportRelativeX(-2000000)
    SLOT_12 = SLOT_19
    Unknown1019(5)
    sprite('tg401_01', 2)	# 28-29
    sprite('tg401_02', 3)	# 30-32
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    sprite('tg401_03', 4)	# 33-36
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_04', 3)	# 37-39
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    Unknown2015(175)
    sprite('tg401_05', 2)	# 40-41
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg401_06', 4)	# 42-45	 **attackbox here**
    GFX_0('RollingAttackEff', 3)
    Unknown1084(1)
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    SFX_0('213_bound_1')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg402_00', 3)	# 46-48
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    sprite('tg402_01', 3)	# 49-51
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    sprite('tg402_02', 3)	# 52-54
    Unknown1047(12000)
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg402_03', 60)	# 55-114

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('tg402_03', 2)	# 1-2
    sprite('tg402_03', 6)	# 3-8
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg402_04', 1)	# 9-9
    SFX_0('005_swing_grap_2_2')
    sprite('tg402_05', 1)	# 10-10
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('SledgeHammerEFF', 0)
    sprite('tg402_06', 1)	# 11-11
    sprite('tg402_07', 6)	# 12-17	 **attackbox here**
    Unknown1019(0)
    Unknown1051(0)
    SFX_3('tgse_20')
    SFX_0('213_bound_0')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('ShockB402', 6)
    Unknown8000(6, 1, 1)
    sprite('tg402_07', 10)	# 18-27	 **attackbox here**
    Unknown23027()
    sprite('tg402_08', 4)	# 28-31
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg402_09', 4)	# 32-35
    sprite('tg402_10', 4)	# 36-39
    sprite('tg402_11', 4)	# 40-43
    sprite('tg402_12', 4)	# 44-47
    sprite('tg000_00', 6)	# 48-53
    teleportRelativeX(-120000)
    sprite('tg000_01', 6)	# 54-59
    sprite('tg000_02', 6)	# 60-65
    sprite('tg000_03', 6)	# 66-71
    sprite('tg000_04', 6)	# 72-77
    sprite('tg000_05', 6)	# 78-83
    sprite('tg000_06', 6)	# 84-89
    sprite('tg000_05', 6)	# 90-95
    sprite('tg000_04', 6)	# 96-101
    sprite('tg000_03', 6)	# 102-107
    sprite('tg000_02', 6)	# 108-113
    sprite('tg000_01', 6)	# 114-119
    sprite('tg000_00', 6)	# 120-125
    sprite('tg000_01', 6)	# 126-131
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 132-137
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 138-143
    SFX_0('014_electric_s')
    sprite('tg000_04', 6)	# 144-149
    sprite('tg000_05', 6)	# 150-155
    sprite('tg000_06', 6)	# 156-161
    sprite('tg000_05', 6)	# 162-167
    sprite('tg000_04', 6)	# 168-173
    sprite('tg000_03', 6)	# 174-179
    sprite('tg000_02', 6)	# 180-185
    sprite('tg000_01', 6)	# 186-191
    label(0)
    sprite('tg000_00', 6)	# 192-197
    sprite('tg000_01', 6)	# 198-203
    sprite('tg000_02', 6)	# 204-209
    sprite('tg000_03', 6)	# 210-215
    sprite('tg000_04', 6)	# 216-221
    sprite('tg000_05', 6)	# 222-227
    sprite('tg000_06', 6)	# 228-233
    sprite('tg000_05', 6)	# 234-239
    sprite('tg000_04', 6)	# 240-245
    sprite('tg000_03', 6)	# 246-251
    sprite('tg000_02', 6)	# 252-257
    sprite('tg000_01', 6)	# 258-263
    loopRest()
    gotoLabel(0)

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('tg430_22', 1)	# 1-1
    teleportRelativeX(-95000)
    physicsXImpulse(-10000)
    sprite('tg430_21', 1)	# 2-2
    sprite('tg430_20', 1)	# 3-3
    sprite('tg430_19', 1)	# 4-4
    sprite('tg430_18', 2)	# 5-6
    Unknown1084(1)
    sprite('tg430_17', 2)	# 7-8	 **attackbox here**
    sprite('tg431_00', 1)	# 9-9
    sprite('tg431_01', 2)	# 10-11
    sprite('tg431_02', 2)	# 12-13
    sprite('tg431_03', 2)	# 14-15
    sprite('tg431_04', 2)	# 16-17
    sprite('tg431_05', 2)	# 18-19
    sprite('tg431_06', 4)	# 20-23	 **attackbox here**
    SFX_0('016_explode_2')
    SFX_3('tgse_21')
    sprite('tg431_07', 4)	# 24-27	 **attackbox here**
    sprite('tg431_08', 4)	# 28-31	 **attackbox here**
    sprite('tg431_09', 5)	# 32-36
    sprite('tg431_10', 4)	# 37-40
    sprite('tg431_11', 4)	# 41-44
    sprite('tg431_12', 4)	# 45-48
    sprite('tg431_13', 4)	# 49-52
    sprite('tg431_14', 4)	# 53-56
    sprite('tg431_15', 4)	# 57-60

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        Unknown2018(0, 80)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('tg030_00', 5)	# 1-5
    label(0)
    sprite('tg030_01', 5)	# 6-10
    sprite('tg030_02', 5)	# 11-15
    sprite('tg030_03', 5)	# 16-20
    sprite('tg030_04', 5)	# 21-25
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 5)	# 26-30
    sprite('tg030_06', 5)	# 31-35
    sprite('tg030_07', 5)	# 36-40
    sprite('tg030_08', 5)	# 41-45
    sprite('tg030_09', 5)	# 46-50
    sprite('tg030_10', 5)	# 51-55
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 5)	# 56-60
    sprite('tg030_12', 5)	# 61-65
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg310_00', 2)	# 66-67
    clearUponHandler(3)
    Unknown1019(10)
    sprite('tg310_01', 1)	# 68-68
    sprite('tg310_02', 3)	# 69-71	 **attackbox here**
    Unknown1084(1)
    sprite('tg310_03', 3)	# 72-74
    SFX_0('004_swing_grap_1_1')
    SFX_4('btg155')
    sprite('tg310_04', 8)	# 75-82
    sprite('tg310_05', 4)	# 83-86
    sprite('tg310_06', 4)	# 87-90
    sprite('tg310_07', 4)	# 91-94

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2018(0, 80)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirPushbackY(-35000)
        AirPushbackX(4000)
        Unknown9190(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(100)
        Unknown11062(0)
        Unknown30048(1)
    sprite('tg310_02', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('tg311_00', 3)	# 4-6
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg311_01', 4)	# 7-10
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg311_02', 5)	# 11-15
    SFX_1('btg153')
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg311_03', 8)	# 16-23
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg311_04', 24)	# 24-47
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg311_06', 3)	# 48-50
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    sprite('tg311_07', 2)	# 51-52
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg311_08', 2)	# 53-54	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(0, 5000)
    GFX_1('tgef_dustA', 1)
    SFX_0('016_explode_2')
    sprite('tg311_08', 3)	# 55-57	 **attackbox here**
    sprite('tg311_10', 3)	# 58-60
    sprite('tg311_11', 3)	# 61-63
    sprite('tg311_12', 3)	# 64-66
    sprite('tg311_13', 3)	# 67-69
    sprite('tg311_14', 3)	# 70-72

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        Unknown2018(0, 80)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('tg030_00', 5)	# 1-5
    label(0)
    sprite('tg030_01', 5)	# 6-10
    sprite('tg030_02', 5)	# 11-15
    sprite('tg030_03', 5)	# 16-20
    sprite('tg030_04', 5)	# 21-25
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 5)	# 26-30
    sprite('tg030_06', 5)	# 31-35
    sprite('tg030_07', 5)	# 36-40
    sprite('tg030_08', 5)	# 41-45
    sprite('tg030_09', 5)	# 46-50
    sprite('tg030_10', 5)	# 51-55
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 5)	# 56-60
    sprite('tg030_12', 5)	# 61-65
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg310_00', 2)	# 66-67
    clearUponHandler(3)
    Unknown1019(10)
    sprite('tg310_01', 1)	# 68-68
    sprite('tg310_02', 3)	# 69-71	 **attackbox here**
    Unknown1084(1)
    sprite('tg310_03', 3)	# 72-74
    SFX_0('004_swing_grap_1_1')
    SFX_4('btg155')
    sprite('tg310_04', 8)	# 75-82
    sprite('tg310_05', 4)	# 83-86
    sprite('tg310_06', 4)	# 87-90
    sprite('tg310_07', 4)	# 91-94

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2018(0, 80)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirPushbackY(-42000)
        AirPushbackX(3000)
        Unknown9190(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(100)
        Unknown11062(0)
        Unknown11099(1)
        Unknown30048(1)
        Unknown13021(1)
        Unknown21005(1)
    sprite('tg310_02', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('tg313_00', 8)	# 4-11
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg313_02', 12)	# 12-23
    SFX_1('btg153')
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg313_04', 4)	# 24-27
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    sprite('tg313_05', 3)	# 28-30
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg313_06', 3)	# 31-33	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000002000000')
    ScreenShake(0, 5000)
    GFX_1('tgef_dustA', 1)
    GFX_0('ShockA', 2)
    SFX_0('016_explode_2')
    sprite('tg313_07', 2)	# 34-35
    sprite('tg313_08', 3)	# 36-38
    sprite('tg313_09', 3)	# 39-41
    sprite('tg313_11', 2)	# 42-43
    sprite('tg313_12', 2)	# 44-45
    sprite('tg313_13', 2)	# 46-47
    sprite('tg313_14', 3)	# 48-50
    sprite('tg313_15', 3)	# 51-53
    sprite('tg313_16', 3)	# 54-56

@State
def Oiuchi():

    def upon_IMMEDIATE():
        Unknown17011('OiuchiExe', 2, 0, 0)
        Unknown11069('OiuchiExe')
        Unknown11032('ffffffffffffffff905f010000000000')
        Unknown11054(500000)
        Unknown11002(-1)
        Unknown11025(0)
        Unknown11045(0)
        Unknown11046(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown30068(1)
        callSubroutine('MAGNET_RESET')
    sprite('tg406_00', 1)	# 1-1
    Unknown21003(6000, 2000)
    sprite('tg406_00', 1)	# 2-2
    Unknown21003(3000, 2000)
    sprite('tg406_01', 4)	# 3-6
    sprite('tg406_02', 4)	# 7-10	 **attackbox here**
    Unknown7007('6274673230375f300000000000000000640000006274673230375f310000000000000000640000006274673230375f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('014_electric_m')
    Unknown4047(232, 223, 208)
    Unknown4045('746765665f6f69756368696c6f636b5f7374617274000000000000000000000001000000')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_03', 4)	# 11-14	 **attackbox here**
    SFX_0('014_electric_m')
    Unknown4047(232, 223, 208)
    Unknown4045('746765665f6f697563686900000000000000000000000000000000000000000001000000')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_02', 4)	# 15-18	 **attackbox here**
    SFX_0('014_electric_m')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_02', 4)	# 19-22	 **attackbox here**
    SFX_0('014_electric_m')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_03', 3)	# 23-25	 **attackbox here**
    SFX_0('014_electric_m')
    Unknown4047(232, 223, 208)
    Unknown4045('746765665f6f697563686900000000000000000000000000000000000000000001000000')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_04', 2)	# 26-27
    Recovery()
    sprite('tg406_05', 2)	# 28-29
    sprite('tg406_06', 2)	# 30-31
    sprite('tg406_07', 3)	# 32-34

@State
def Oiuchi_Throw():

    def upon_IMMEDIATE():
        Unknown17011('OiuchiExe', 2, 0, 0)
        Unknown11069('OiuchiExe')
        Unknown11032('ffffffffffffffff905f010000000000')
        Unknown11054(500000)
        Unknown11002(-1)
        Unknown11025(0)
        Unknown11045(0)
        Unknown11046(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown30068(1)
        Unknown14083(0)
        callSubroutine('MAGNET_RESET')
        Unknown13045(0)
    sprite('tg406_00', 1)	# 1-1
    Unknown21003(6000, 2000)
    sprite('tg406_00', 1)	# 2-2
    Unknown21003(3000, 2000)
    sprite('tg406_01', 4)	# 3-6
    sprite('tg406_02', 4)	# 7-10	 **attackbox here**
    Unknown7007('6274673230375f300000000000000000640000006274673230375f310000000000000000640000006274673230375f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('014_electric_m')
    Unknown4047(232, 223, 208)
    Unknown4045('746765665f6f69756368696c6f636b5f7374617274000000000000000000000001000000')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_03', 4)	# 11-14	 **attackbox here**
    SFX_0('014_electric_m')
    Unknown4047(232, 223, 208)
    Unknown4045('746765665f6f697563686900000000000000000000000000000000000000000001000000')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_02', 4)	# 15-18	 **attackbox here**
    SFX_0('014_electric_m')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_02', 4)	# 19-22	 **attackbox here**
    SFX_0('014_electric_m')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_03', 3)	# 23-25	 **attackbox here**
    SFX_0('014_electric_m')
    Unknown4047(232, 223, 208)
    Unknown4045('746765665f6f697563686900000000000000000000000000000000000000000001000000')
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg406_04', 2)	# 26-27
    Recovery()
    sprite('tg406_05', 2)	# 28-29
    sprite('tg406_06', 2)	# 30-31
    sprite('tg406_07', 3)	# 32-34

@State
def OiuchiExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        Unknown1084(1)
        AttackLevel_(0)
        Damage(100)
        Unknown11091(100)
        Unknown11064(1)
        AirHitstunAnimation(5)
        GroundedHitstunAnimation(5)
        Unknown11094(1)
        Unknown9154(36)
        AirUntechableTime(36)
        AirPushbackX(3000)
        AirPushbackY(5000)
        YImpluseBeforeWallbounce(1200)
        PushbackX(0)
        Hitstop(0)
        Unknown9020(0)
        Unknown23027()
        Unknown11062(0)
        Unknown30048(1)
        Unknown30061(0)
        Unknown14083(1)
        Unknown11108('03000000')
    sprite('tg406_02', 30)	# 1-30	 **attackbox here**
    Unknown5000(28, 0)
    Unknown5001('0000000005000000050000000400000000000000')
    GFX_0('OiuchiBallEffect', -1)
    sprite('tg407_00', 4)	# 31-34
    Unknown5000(10, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('tg407_01', 4)	# 35-38
    Unknown5000(10, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('tg407_02ex01', 2)	# 39-40
    Unknown5000(10, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('tg407_02', 2)	# 41-42
    Unknown5000(10, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('tg407_02', 10)	# 43-52
    Unknown5000(10, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('tg407_02', 10)	# 53-62
    Unknown5000(10, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    Unknown23118(0)
    Unknown23119(16744448, 12, 2)
    sprite('tg407_03', 2)	# 63-64	 **attackbox here**
    Unknown5000(10, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    RefreshMultihit()
    Unknown21015('4f697563686942616c6c456666656374000000000000000000000000000000009101000000000000')
    SFX_0('014_electric_sl')
    SFX_0('014_electric_ml')
    sprite('tg407_04', 20)	# 65-84
    sprite('tg407_05', 5)	# 85-89
    sprite('tg407_06', 5)	# 90-94

@State
def AntiAir_A():

    def upon_IMMEDIATE():
        Unknown17011('AntiAir_AExe', 2, 0, 0)
        Unknown2018(0, 80)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown11045(0)
        Unknown11046(1)
        Unknown11025(0)
        Unknown30048(1)
        Unknown30061(0)
        AttackP1(90)
        AttackP2(100)
    sprite('tg404_00', 2)	# 1-2
    sprite('tg404_01', 1)	# 3-3
    sprite('tg404_01', 1)	# 4-4
    Unknown22008(12)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('tg404_02', 2)	# 5-6
    sprite('tg404_03', 2)	# 7-8
    sprite('tg404_04', 3)	# 9-11
    sprite('tg404_05', 1)	# 12-12
    sprite('tg404_06', 1)	# 13-13
    Unknown7007('6274673230325f300000000000000000640000006274673230325f310000000000000000640000006274673230325f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_2')
    sprite('tg404_07', 1)	# 14-14
    sprite('tg404_08', 1)	# 15-15
    Unknown4048(120000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000000000000')
    Unknown4048(200000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    Unknown4048(280000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000002000000')
    ScreenShake(0, 5000)
    SFX_3('tgse_00')
    sprite('tg404_09', 4)	# 16-19	 **attackbox here**
    sprite('tg404_24', 5)	# 20-24
    Recovery()
    sprite('tg404_25', 4)	# 25-28
    sprite('tg404_26', 4)	# 29-32
    sprite('tg404_27', 6)	# 33-38

@State
def AntiAir_AExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        Unknown2018(0, 80)
        AttackLevel_(4)
        Damage(3500)
        AttackP2(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(62)
        Unknown9310(10)
        Hitstop(8)
        Unknown9190(1)
        Unknown9118(100)
        Unknown11068(0)
        Unknown11091(5)
        Unknown11078(0)
        Unknown11062(0)
        Unknown11108('03000000')
        Unknown30048(1)
        AirPushbackY(-15000)
        AirPushbackX(-2190)
        Unknown11072(3, 120000, 0)
        Unknown13021(1)
        Unknown21005(1)
    sprite('tg404_11', 4)	# 1-4
    StartMultihit()
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('005_swing_grap_2_0')
    sprite('tg404_12', 4)	# 5-8
    StartMultihit()
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_13', 3)	# 9-11
    StartMultihit()
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_14', 3)	# 12-14
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_15', 2)	# 15-16
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_16', 2)	# 17-18	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(0, 5000)
    GFX_1('tgef_dustA', 1)
    GFX_0('ShockA', 2)
    SFX_0('209_down_normal_1')
    sprite('tg404_17', 6)	# 19-24
    sprite('tg404_18', 5)	# 25-29
    sprite('tg404_19', 3)	# 30-32
    sprite('tg404_20', 3)	# 33-35
    Unknown14070('Oiuchi_Throw')
    Unknown14070('Oiuchi_Throw_B')
    Unknown14070('Oiuchi_Throw_C')
    sprite('tg404_21', 6)	# 36-41
    sprite('tg404_22', 3)	# 42-44
    Unknown14072('Oiuchi_Throw')
    Unknown14072('Oiuchi_Throw_B')
    Unknown14072('Oiuchi_Throw_C')
    sprite('tg404_23', 4)	# 45-48
    Unknown14074('Oiuchi_Throw')
    Unknown14074('Oiuchi_Throw_B')
    Unknown14074('Oiuchi_Throw_C')
    sprite('tg404_23', 5)	# 49-53

@State
def AntiAir_B():

    def upon_IMMEDIATE():
        Unknown17011('AntiAir_BExe', 2, 0, 0)
        Unknown2018(0, 80)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown11045(0)
        Unknown11046(1)
        Unknown11025(0)
        Unknown30048(1)
        Unknown30061(0)
        AttackP1(90)
        AttackP2(100)

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0xa)):
                    clearUponHandler(3)
                    sendToLabel(1)
        sendToLabelUpon(17, 1)

        def upon_43():
            if (SLOT_48 == 601):
                sendToLabel(1)
        callSubroutine('MAGNET_RESET')
    sprite('tg404_00', 3)	# 1-3
    loopRelated(17, 70)
    sprite('tg404_01', 2)	# 4-5
    sprite('tg404_01', 1)	# 6-6
    Unknown22008(30)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('tg404_02', 3)	# 7-9
    sprite('tg404_03', 3)	# 10-12
    sprite('tg404_04', 3)	# 13-15
    sprite('tg404_05', 3)	# 16-18
    sprite('tg404_06', 3)	# 19-21
    Unknown7007('6274673230325f300000000000000000640000006274673230325f310000000000000000640000006274673230325f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_2')
    sprite('tg404_07', 3)	# 22-24
    sprite('tg404_08', 3)	# 25-27
    Unknown4048(120000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000000000000')
    Unknown4048(200000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    Unknown4048(280000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000002000000')
    ScreenShake(0, 5000)
    SFX_3('tgse_00')
    sprite('tg404_09', 4)	# 28-31	 **attackbox here**
    GFX_0('AntiAirDmyMagnet', 0)
    GFX_0('StayMagneticA', 0)
    StartMultihit()
    Unknown2037(1)
    sprite('tg404_10', 4)	# 32-35	 **attackbox here**
    GFX_0('StayMagneticA', 0)
    StartMultihit()
    loopRest()
    label(0)
    sprite('tg404_09', 4)	# 36-39	 **attackbox here**
    SFX_0('014_electric_m')
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA404', 1)
    GFX_0('StayMagneticA404', 2)
    GFX_0('StayMagneticA404', 3)
    StartMultihit()
    sprite('tg404_10', 4)	# 40-43	 **attackbox here**
    SFX_0('014_electric_m')
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA404', 1)
    GFX_0('StayMagneticA404', 2)
    GFX_0('StayMagneticA404', 3)
    StartMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(3)
    sprite('tg404_09', 4)	# 44-47	 **attackbox here**
    Unknown21015('416e7469416972446d794d61676e657400000000000000000000000000000000bd02000000000000')
    sprite('tg404_24', 5)	# 48-52
    Recovery()
    sprite('tg404_25', 4)	# 53-56
    sprite('tg404_26', 4)	# 57-60
    sprite('tg404_27', 6)	# 61-66

@State
def AntiAir_BExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        Unknown2018(0, 80)
        AttackLevel_(4)
        Damage(3500)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AttackP2(60)
        AirUntechableTime(62)
        AirPushbackX(-1190)
        AirPushbackY(-35000)
        Unknown9190(1)
        Unknown9118(80)
        Unknown11068(0)
        Unknown11091(5)
        Unknown11078(0)
        Unknown11062(0)
        Unknown11108('03000000')
        Unknown30048(1)
        Unknown11072(3, 120000, 0)
        Unknown13021(1)
        Unknown21005(1)
    sprite('tg404_11', 4)	# 1-4
    StartMultihit()
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('005_swing_grap_2_0')
    sprite('tg404_12', 4)	# 5-8
    StartMultihit()
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_13', 3)	# 9-11
    StartMultihit()
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_14', 3)	# 12-14
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_15', 2)	# 15-16
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg404_16', 2)	# 17-18	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(0, 5000)
    GFX_1('tgef_dustA', 1)
    GFX_0('ShockA', 2)
    SFX_0('209_down_normal_1')
    sprite('tg404_17', 2)	# 19-20
    sprite('tg404_18', 2)	# 21-22
    sprite('tg404_19', 2)	# 23-24
    sprite('tg404_20', 2)	# 25-26
    sprite('tg404_21', 2)	# 27-28
    sprite('tg404_22', 2)	# 29-30
    sprite('tg404_23', 2)	# 31-32

@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('tg403_00', 2)	# 1-2
    sprite('tg403_01', 1)	# 3-3
    sprite('tg403_01', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    GFX_0('ShotObjCharge', 1)
    sprite('tg403_02', 1)	# 6-6
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    sprite('tg403_03', 2)	# 7-8
    SFX_0('014_electric_m')
    GFX_0('StayMagneticB', 0)
    sprite('tg403_04', 3)	# 9-11
    Unknown7007('6274673230355f300000000000000000640000006274673230355f310000000000000000640000006274673230355f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('ShotMagicCircle', 1)
    sprite('tg403_05', 5)	# 12-16	 **attackbox here**
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('StayMagneticB', 3)
    GFX_0('StayMagneticB', 4)
    GFX_0('ShotObj', 6)
    SFX_3('tgse_08')
    GFX_1('tgef_side_shockA', 5)
    GFX_0('tgef_tg403pla', 7)
    ScreenShake(0, 5000)
    sprite('tg403_06', 17)	# 17-33
    sprite('tg403_07', 4)	# 34-37
    sprite('tg403_08', 4)	# 38-41
    sprite('tg403_10', 6)	# 42-47

@State
def CommandThrow():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowUchiage', 2, 0, 0)
        Unknown11054(320000)
        Unknown11032('801a060001000000ffffffffffffffff')
        AttackP2(100)
        Unknown2018(0, 80)
        Unknown30048(1)
        Unknown11069('CommandThrowUchiage')
        Unknown14083(0)
    sprite('tg400_00', 2)	# 1-2
    sprite('tg400_00', 1)	# 3-3
    sprite('tg400_02', 2)	# 4-5
    sprite('tg400_04', 1)	# 6-6	 **attackbox here**
    sprite('tg400_04', 1)	# 7-7	 **attackbox here**
    sprite('tg400_34', 5)	# 8-12
    SFX_0('006_swing_blade_0')
    sprite('tg400_35', 8)	# 13-20
    sprite('tg400_36', 4)	# 21-24
    SFX_1('btg155')
    sprite('tg400_37', 4)	# 25-28
    sprite('tg400_37', 4)	# 29-32
    sprite('tg400_39', 4)	# 33-36
    sprite('tg400_40', 4)	# 37-40

@State
def CommandThrowUchiage():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        Damage(0)
        AttackP2(100)
        AirPushbackX(-3000)
        AirPushbackY(100000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirUntechableTime(200)
        Unknown11068(1)
        Unknown11078(1)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown13024(0)
        Unknown30048(1)
        Unknown30061(0)
        setInvincible(1)
        Unknown11069('CommandThrowJump')
        Unknown14083(0)
        Unknown30068(1)
    sprite('tg400_04', 16)	# 1-16	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg400_05', 3)	# 17-19	 **attackbox here**
    SFX_0('100_hit_grap_2')
    sprite('tg400_06', 11)	# 20-30
    tag_voice(1, 'btg200_0', 'btg200_1', 'btg200_2', '')
    GFX_1('tgef_shockwaveA', 0)
    sprite('tg400_08', 3)	# 31-33
    sprite('tg400_09', 3)	# 34-36
    sprite('tg400_10', 6)	# 37-42
    GFX_0('ShockB', 0)
    GFX_1('tgef_shockwaveB', 1)
    loopRest()
    enterState('CommandThrowJump')

@State
def CommandThrowJump():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowDrop', 2, 1, 0)
        Unknown11069('CommandThrowDrop')
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown14083(0)
        Unknown30068(1)
        Unknown2018(0, 80)
        physicsYImpulse(120000)
        setGravity(2400)
        Unknown20000(1)
        SFX_0('002_highjump_2')
        Unknown13045(0)
        setInvincible(1)
    label(0)
    sprite('tg400_12', 3)	# 1-3	 **attackbox here**
    sprite('tg400_13', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CommandThrowDrop():

    def upon_IMMEDIATE():
        Unknown17012(2, 1, 0)
        AttackLevel_(4)
        Damage(4200)
        AttackP2(50)
        Unknown11068(1)
        Unknown11078(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(12000)
        AirPushbackY(20000)
        AirUntechableTime(100)
        Unknown9310(1)
        Unknown11062(0)
        Unknown30068(1)
        setInvincible(1)
        Unknown2018(0, 80)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown20000(1)
        Unknown13024(0)
        Unknown1023()
        YAccel(75)
        Unknown1038()
        Unknown30048(1)
        Unknown30061(0)
        Unknown13045(0)
        if (SLOT_134 >= 4):
            Unknown11091(5)
    sprite('tg400_15', 30)	# 1-30
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_17', 6)	# 31-36
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(0)
    sprite('tg400_19', 4)	# 37-40
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_20', 4)	# 41-44
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg400_21', 3)	# 45-47
    Unknown1084(1)
    tag_voice(0, 'btg201_0', 'btg201_1', 'btg201_2', '')
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown8000(100, 1, 1)
    GFX_0('ShockB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    ScreenShake(0, 7500)
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    sprite('tg400_22', 5)	# 48-52	 **attackbox here**
    sprite('tg400_23', 5)	# 53-57
    Unknown14070('Oiuchi_Throw')
    Unknown14070('Oiuchi_Throw_B')
    Unknown14070('Oiuchi_Throw_C')
    sprite('tg400_24', 5)	# 58-62
    sprite('tg400_26', 15)	# 63-77
    sprite('tg400_27', 5)	# 78-82
    sprite('tg400_29', 5)	# 83-87
    sprite('tg400_30', 5)	# 88-92
    Unknown14072('Oiuchi_Throw')
    Unknown14072('Oiuchi_Throw_B')
    Unknown14072('Oiuchi_Throw_C')

@State
def CommandThrowB2():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowB2_Exe', 2, 0, 0)
        Unknown11054(210000)
        Unknown11032('801a060001000000ffffffffffffffff')
        Unknown2018(0, 80)
        Unknown11002(-1)
        AttackP2(100)
        Unknown30048(1)
        Unknown11069('CommandThrowB2_Exe')
        callSubroutine('MAGNET_RESET')
        Unknown30061(0)
    sprite('tg412_00', 5)	# 1-5
    sprite('tg412_01', 6)	# 6-11
    Unknown21003(1000, 1000)
    setInvincible(1)
    GFX_0('StayMagneticA400', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    GFX_0('StayMagneticA400', 5)
    GFX_0('MagneticStorm', 6)
    SFX_0('014_electric_m')
    sprite('tg412_02', 6)	# 12-17
    GFX_0('StayMagneticA400', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    GFX_0('StayMagneticA400', 5)
    GFX_0('MagneticStorm', 6)
    SFX_0('014_electric_m')
    sprite('tg412_03', 3)	# 18-20
    GFX_0('StayMagneticA400', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    GFX_0('StayMagneticA400', 5)
    SFX_0('014_electric_m')
    sprite('tg412_03', 3)	# 21-23
    Unknown21003(10000, 1000)
    sprite('tg412_04', 6)	# 24-29
    GFX_0('StayMagneticA400', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    GFX_0('StayMagneticA400', 5)
    SFX_0('014_electric_m')
    Unknown21003(2000, 0)
    sprite('tg412_05', 4)	# 30-33	 **attackbox here**
    Unknown21003(0, 0)
    setInvincible(0)
    sprite('tg412_17', 6)	# 34-39
    SFX_1('btg155')
    SFX_0('004_swing_grap_1_1')
    sprite('tg412_18', 18)	# 40-57
    sprite('tg412_19', 6)	# 58-63

@State
def CommandThrowB2_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        Damage(0)
        AttackP2(100)
        AirPushbackX(80000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        Hitstop(0)
        AirUntechableTime(200)
        Unknown11099(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11068(1)
        Unknown11078(1)
        Unknown11023(1)
        Unknown11064(1)
        Unknown2018(0, 80)
        Unknown30048(1)
        Unknown30061(0)
        if (SLOT_134 >= 2):
            Unknown11091(5)
        Unknown2003(1)
        Unknown2004(1, 0)
        Unknown13024(0)
        Unknown14083(0)
    sprite('tg412_05', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg412_06', 10)	# 5-14
    Unknown23022(1)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg412_07', 5)	# 15-19
    Unknown7007('6274673231305f300000000000000000640000006274673231305f310000000000000000640000006274673231305f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg412_08', 5)	# 20-24
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg412_09', 6)	# 25-30
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg412_10', 3)	# 31-33
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('tgef_412_throw', -1)
    sprite('tg412_11', 1)	# 34-34	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown1045(30000)
    sprite('tg412_11', 6)	# 35-40	 **attackbox here**
    Unknown2003(0)
    sprite('tg412_12', 6)	# 41-46	 **attackbox here**
    sprite('tg412_12', 10)	# 47-56	 **attackbox here**
    RefreshMultihit()
    Unknown11099(1)
    Damage(800)
    AirPushbackX(-13000)
    AirPushbackY(44000)
    YImpluseBeforeWallbounce(1600)
    Hitstop(6)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    Unknown11062(1)

    def upon_12():
        Unknown14083(1)
        Unknown23072()
        Unknown36(22)
        Unknown8008(102, 1, 1)
        ScreenShake(20000, 5000)
        teleportRelativeY(110000)
        Unknown35()
    sprite('tg412_12', 16)	# 57-72	 **attackbox here**
    sprite('tg412_20', 2)	# 73-74
    sprite('tg412_19', 2)	# 75-76
    Unknown2005()
    teleportRelativeX(110000)

@State
def CommandThrowEX():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowUchiageEX', 2, 0, 0)
        Unknown11069('CommandThrowUchiageEX')
        Unknown11054(320000)
        Unknown11032('801a060001000000ffffffffffffffff')
        Unknown2018(0, 80)
        Unknown11002(-1)
        sendToLabelUpon(17, 1)
        Unknown14083(0)
        Unknown30048(1)
        Unknown30061(0)
        callSubroutine('MAGNET_RESET')
    sprite('tg400_00', 3)	# 1-3
    Unknown21003(3450, 0)
    loopRelated(17, 15)
    sprite('tg400_02', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('tg400_02', 1)	# 5-5
    sprite('tg400_04', 1)	# 6-6	 **attackbox here**
    loopRest()
    sendToLabelUpon(25, 1)
    sprite('tg400_04', 1)	# 7-7	 **attackbox here**
    label(0)
    sprite('tg400_04', 2)	# 8-9	 **attackbox here**
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg400_04', 2)	# 10-11	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg400_04ex01', 2)	# 12-13	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg400_04ex01', 2)	# 14-15	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(25)
    sprite('tg400_34', 5)	# 16-20
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg400_35', 8)	# 21-28
    sprite('tg400_36', 4)	# 29-32
    SFX_1('btg155')
    sprite('tg400_37', 4)	# 33-36
    sprite('tg400_37', 4)	# 37-40
    sprite('tg400_39', 4)	# 41-44
    sprite('tg400_40', 4)	# 45-48

@State
def CommandThrowUchiageEX():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        Damage(0)
        AttackP2(100)
        AirPushbackX(-3000)
        AirPushbackY(100000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirUntechableTime(200)
        Unknown11068(1)
        Unknown11078(1)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown13024(0)
        Unknown30048(1)
        Unknown30061(0)
        setInvincible(1)
        Unknown11069('CommandThrowJumpEX')
        callSubroutine('komanageEff')
        Unknown14083(0)
        Unknown30068(1)
    sprite('tg400_04', 16)	# 1-16	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg400_05', 3)	# 17-19	 **attackbox here**
    SFX_0('100_hit_grap_2')
    sprite('tg400_06', 11)	# 20-30
    tag_voice(1, 'btg200_0', 'btg200_1', 'btg200_2', '')
    GFX_1('tgef_shockwaveA', 0)
    sprite('tg400_08', 3)	# 31-33
    sprite('tg400_09', 3)	# 34-36
    sprite('tg400_10', 6)	# 37-42
    GFX_0('ShockB', 0)
    GFX_1('tgef_shockwaveB', 1)
    loopRest()
    enterState('CommandThrowJumpEX')

@State
def CommandThrowJumpEX():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowDropEX', 2, 1, 0)
        Unknown11069('CommandThrowDropEX')
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown30068(1)
        Unknown2018(0, 80)
        physicsYImpulse(120000)
        setGravity(2400)
        Unknown20000(1)
        SFX_0('002_highjump_2')
        Unknown14083(0)
        Unknown13045(0)
        setInvincible(1)
        callSubroutine('komanageEff')
    label(0)
    sprite('tg400_12', 3)	# 1-3	 **attackbox here**
    sprite('tg400_13', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CommandThrowDropEX():

    def upon_IMMEDIATE():
        Unknown17012(2, 1, 0)
        AttackLevel_(4)
        Damage(4200)
        AttackP2(50)
        Unknown11068(1)
        Unknown11078(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(12000)
        AirPushbackY(20000)
        AirUntechableTime(100)
        Unknown9310(1)
        Unknown11062(0)
        Unknown30065(0)
        setInvincible(1)
        Unknown2018(0, 80)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown20000(1)
        Unknown13024(0)
        Unknown1023()
        YAccel(75)
        Unknown1038()
        Unknown30048(1)
        Unknown30061(0)
        Unknown13045(0)
        callSubroutine('komanageEff')
        if (SLOT_134 >= 4):
            Unknown11091(10)
    sprite('tg400_15', 30)	# 1-30
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_17', 6)	# 31-36
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(0)
    sprite('tg400_19', 4)	# 37-40
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_20', 4)	# 41-44
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg400_21', 3)	# 45-47
    Unknown1084(1)
    tag_voice(0, 'btg201_0', 'btg201_1', 'btg201_2', '')
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown8000(100, 1, 1)
    GFX_0('ShockB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    ScreenShake(0, 7500)
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    sprite('tg400_22', 5)	# 48-52	 **attackbox here**
    sprite('tg400_23', 5)	# 53-57
    Unknown14070('Oiuchi_Throw')
    Unknown14070('Oiuchi_Throw_B')
    Unknown14070('Oiuchi_Throw_C')
    sprite('tg400_24', 5)	# 58-62
    sprite('tg400_26', 15)	# 63-77
    sprite('tg400_27', 5)	# 78-82
    sprite('tg400_29', 5)	# 83-87
    sprite('tg400_30', 5)	# 88-92
    Unknown14072('Oiuchi_Throw')
    Unknown14072('Oiuchi_Throw_B')
    Unknown14072('Oiuchi_Throw_C')

@State
def CommandThrowC_A():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowUchiageC_B', 2, 1, 0)
        Unknown11054(210000)
        Unknown2018(0, 80)
        Unknown30048(1)
        Unknown14083(0)
        Unknown23001(0, 0)
        Unknown11069('CommandThrowUchiageC_B')
    sprite('tg410_00', 3)	# 1-3
    sprite('tg410_00', 2)	# 4-5
    sprite('tg410_01', 1)	# 6-6	 **attackbox here**
    Unknown22004(13, 1)
    loopRest()
    sprite('tg410_01', 1)	# 7-7	 **attackbox here**
    sprite('tg410_02', 1)	# 8-8	 **attackbox here**
    setGravity(1200)
    Unknown2015(-1)
    sprite('tg410_08', 5)	# 9-13
    SFX_0('006_swing_blade_0')
    sprite('tg410_09', 4)	# 14-17
    sprite('tg410_10', 4)	# 18-21
    SFX_1('btg155')
    sprite('tg410_11', 4)	# 22-25
    sprite('tg410_11', 4)	# 26-29
    sprite('tg410_12', 4)	# 30-33
    sprite('tg410_13', 4)	# 34-37
    sprite('tg020_05', 3)	# 38-40
    sprite('tg020_06', 3)	# 41-43
    label(2)
    sprite('tg020_07', 3)	# 44-46
    sprite('tg020_08', 3)	# 47-49
    gotoLabel(2)

@State
def CommandThrowC_B():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowUchiageC_B', 2, 1, 0)
        Unknown11054(210000)
        Unknown2018(0, 80)
        loopRelated(17, 83)
        sendToLabelUpon(17, 1)
        Unknown30048(1)
        Unknown14083(0)
        Unknown23001(0, 0)
        Unknown11069('CommandThrowUchiageC_B')
        callSubroutine('MAGNET_RESET')
    sprite('tg410_00', 3)	# 1-3
    sprite('tg410_00', 3)	# 4-6
    Unknown1084(1)
    sprite('tg410_01', 4)	# 7-10	 **attackbox here**
    StartMultihit()
    GFX_0('AntiAirDmyMagnet2', 0)
    Unknown22004(13, 1)
    sprite('tg410_01', 3)	# 11-13	 **attackbox here**
    StartMultihit()
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 3)	# 14-16	 **attackbox here**
    StartMultihit()
    SFX_0('014_electric_m')
    sprite('tg410_01', 3)	# 17-19	 **attackbox here**
    StartMultihit()
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 3)	# 20-22	 **attackbox here**
    StartMultihit()
    SFX_0('014_electric_m')
    sprite('tg410_01', 1)	# 23-23	 **attackbox here**
    Unknown21015('416e7469416972446d794d61676e657400000000000000000000000000000000bd02000000000000')
    Unknown22004(13, 1)
    loopRest()
    sendToLabelUpon(24, 1)
    sprite('tg410_01', 1)	# 24-24	 **attackbox here**
    label(0)
    sprite('tg410_01', 2)	# 25-26	 **attackbox here**
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 27-28	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 29-30	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 31-32	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg410_02', 1)	# 33-33	 **attackbox here**
    clearUponHandler(17)
    clearUponHandler(24)
    Unknown21015('416e7469416972446d794d61676e657400000000000000000000000000000000bd02000000000000')
    Unknown21003(0, 0)
    setGravity(1200)
    Unknown2015(-1)
    StartMultihit()
    sprite('tg410_08', 5)	# 34-38
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg410_09', 4)	# 39-42
    sprite('tg410_10', 4)	# 43-46
    SFX_1('btg155')
    sprite('tg410_11', 4)	# 47-50
    sprite('tg410_11', 4)	# 51-54
    sprite('tg410_12', 4)	# 55-58
    sprite('tg410_13', 4)	# 59-62
    sprite('tg020_05', 3)	# 63-65
    sprite('tg020_06', 3)	# 66-68
    label(2)
    sprite('tg020_07', 3)	# 69-71
    sprite('tg020_08', 3)	# 72-74
    gotoLabel(2)

@State
def CommandThrowUchiageC_B():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AirPushbackX(-4000)
        AirPushbackY(70000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Damage(0)
        AttackP2(100)
        AirUntechableTime(200)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown14083(0)
        setInvincible(1)
        Unknown22004(0, 0)
        Unknown11069('CommandThrowJumpC_B')
        Unknown30068(1)
    sprite('tg410_02', 16)	# 1-16	 **attackbox here**
    StartMultihit()
    Unknown5000(9, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg410_03', 3)	# 17-19	 **attackbox here**
    SFX_0('100_hit_grap_2')
    sprite('tg410_04', 11)	# 20-30
    GFX_1('tgef_shockwaveA', 0)
    sprite('tg410_05', 3)	# 31-33
    sprite('tg410_06', 3)	# 34-36
    sprite('tg410_07', 6)	# 37-42
    tag_voice(1, 'btg209_0', 'btg209_1', 'btg209_2', '')
    GFX_0('ShockB', 0)
    GFX_1('tgef_shockwaveB', 1)
    loopRest()
    enterState('CommandThrowJumpC_B')

@State
def CommandThrowJumpC_B():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowDropC_B', 2, 1, 0)
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown2018(0, 80)
        physicsYImpulse(120000)
        setGravity(2400)
        Unknown20000(1)
        SFX_0('002_highjump_2')
        Unknown14083(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown13045(0)
        Unknown30068(1)
        setInvincible(1)
        Unknown11069('CommandThrowDropC_B')
    label(0)
    sprite('tg400_12', 3)	# 1-3	 **attackbox here**
    sprite('tg400_13', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CommandThrowDropC_B():

    def upon_IMMEDIATE():
        Unknown17012(2, 1, 0)
        AttackLevel_(4)
        Damage(4500)
        AttackP2(50)
        Unknown11068(1)
        Unknown11078(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(12000)
        AirPushbackY(20000)
        AirUntechableTime(100)
        Unknown9310(1)
        Unknown11062(0)
        Unknown30048(1)
        Unknown30061(0)
        Unknown13045(0)
        Unknown30068(1)
        setInvincible(1)
        Unknown2018(0, 80)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown20000(1)
        Unknown13024(0)
        Unknown1023()
        YAccel(75)
        Unknown1038()
        if (SLOT_134 >= 4):
            Unknown11091(5)
    sprite('tg400_15', 30)	# 1-30
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_17', 6)	# 31-36
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(0)
    sprite('tg400_19', 4)	# 37-40
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_20', 4)	# 41-44
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg400_21', 3)	# 45-47
    Unknown1084(1)
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown8000(100, 1, 1)
    GFX_0('ShockB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    ScreenShake(0, 12500)
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    sprite('tg400_22', 5)	# 48-52	 **attackbox here**
    sprite('tg400_23', 5)	# 53-57
    Unknown14070('Oiuchi_Throw')
    Unknown14070('Oiuchi_Throw_B')
    Unknown14070('Oiuchi_Throw_C')
    sprite('tg400_24', 5)	# 58-62
    sprite('tg400_26', 15)	# 63-77
    sprite('tg400_27', 5)	# 78-82
    sprite('tg400_29', 5)	# 83-87
    sprite('tg400_30', 5)	# 88-92
    Unknown14072('Oiuchi_Throw')
    Unknown14072('Oiuchi_Throw_B')
    Unknown14072('Oiuchi_Throw_C')

@State
def CommandThrowC_C():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowUchiageC', 2, 1, 0)
        Unknown11054(210000)
        Unknown2018(0, 80)
        Unknown11002(-1)
        sendToLabelUpon(17, 1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown14083(0)
        Unknown23001(0, 0)
        Unknown11069('CommandThrowUchiageC')
        callSubroutine('MAGNET_RESET')
    sprite('tg410_00', 3)	# 1-3
    Unknown21003(0, 3450)
    loopRelated(17, 40)
    sprite('tg410_00', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    Unknown1084(1)
    sprite('tg410_00', 1)	# 5-5
    sprite('tg410_01', 1)	# 6-6	 **attackbox here**
    GFX_0('AntiAirDmyMagnet2', 0)
    Unknown22004(13, 1)
    loopRest()
    sendToLabelUpon(25, 1)
    sprite('tg410_01', 1)	# 7-7	 **attackbox here**
    label(0)
    sprite('tg410_01', 2)	# 8-9	 **attackbox here**
    Unknown1084(1)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 10-11	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 12-13	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 14-15	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(25)
    sprite('tg410_02', 1)	# 16-16	 **attackbox here**
    Unknown21003(0, 0)
    setGravity(1200)
    Unknown2015(-1)
    sprite('tg410_08', 5)	# 17-21
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg410_09', 4)	# 22-25
    sprite('tg410_10', 4)	# 26-29
    SFX_1('btg155')
    sprite('tg410_11', 4)	# 30-33
    sprite('tg410_11', 4)	# 34-37
    sprite('tg410_12', 4)	# 38-41
    sprite('tg410_13', 4)	# 42-45
    sprite('tg020_05', 3)	# 46-48
    sprite('tg020_06', 3)	# 49-51
    label(2)
    sprite('tg020_07', 3)	# 52-54
    sprite('tg020_08', 3)	# 55-57
    gotoLabel(2)

@State
def CommandThrowUchiageC():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AirPushbackX(-4000)
        AirPushbackY(70000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Damage(0)
        AttackP2(100)
        AirUntechableTime(200)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown14083(0)
        setInvincible(1)
        Unknown22004(0, 0)
        Unknown11069('CommandThrowJumpC')
        callSubroutine('komanageEff')
        Unknown30068(1)
    sprite('tg410_02', 16)	# 1-16	 **attackbox here**
    StartMultihit()
    Unknown5000(9, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg410_03', 3)	# 17-19	 **attackbox here**
    SFX_0('100_hit_grap_2')
    sprite('tg410_04', 11)	# 20-30
    GFX_1('tgef_shockwaveA', 0)
    sprite('tg410_05', 3)	# 31-33
    sprite('tg410_06', 3)	# 34-36
    sprite('tg410_07', 6)	# 37-42
    tag_voice(1, 'btg209_0', 'btg209_1', 'btg209_2', '')
    GFX_0('ShockB', 0)
    GFX_1('tgef_shockwaveB', 1)
    loopRest()
    enterState('CommandThrowJumpC')

@State
def CommandThrowJumpC():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowDropC', 2, 1, 0)
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown2018(0, 80)
        physicsYImpulse(120000)
        setGravity(2400)
        Unknown20000(1)
        SFX_0('002_highjump_2')
        Unknown14083(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown30068(1)
        setInvincible(1)
        Unknown11069('CommandThrowDropC')
        Unknown13045(0)
        callSubroutine('komanageEff')
    label(0)
    sprite('tg400_12', 3)	# 1-3	 **attackbox here**
    sprite('tg400_13', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CommandThrowDropC():

    def upon_IMMEDIATE():
        Unknown17012(2, 1, 0)
        AttackLevel_(4)
        Damage(4500)
        AttackP2(50)
        Unknown11068(1)
        Unknown11078(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(12000)
        AirPushbackY(20000)
        AirUntechableTime(100)
        Unknown9310(1)
        Unknown11062(0)
        Unknown30048(1)
        Unknown30061(0)
        Unknown30065(0)
        Unknown13045(0)
        setInvincible(1)
        Unknown2018(0, 80)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown20000(1)
        Unknown13024(0)
        Unknown1023()
        YAccel(75)
        Unknown1038()
        if (SLOT_134 >= 4):
            Unknown11091(10)
        callSubroutine('komanageEff')
    sprite('tg400_15', 30)	# 1-30
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_17', 6)	# 31-36
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(0)
    sprite('tg400_19', 4)	# 37-40
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg400_20', 4)	# 41-44
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg400_21', 3)	# 45-47
    Unknown1084(1)
    Unknown5000(3, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown8000(100, 1, 1)
    GFX_0('ShockB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    ScreenShake(0, 12500)
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    sprite('tg400_22', 5)	# 48-52	 **attackbox here**
    sprite('tg400_23', 5)	# 53-57
    Unknown14070('Oiuchi_Throw')
    Unknown14070('Oiuchi_Throw_B')
    Unknown14070('Oiuchi_Throw_C')
    sprite('tg400_24', 5)	# 58-62
    sprite('tg400_26', 15)	# 63-77
    sprite('tg400_27', 5)	# 78-82
    sprite('tg400_29', 5)	# 83-87
    sprite('tg400_30', 5)	# 88-92
    Unknown14072('Oiuchi_Throw')
    Unknown14072('Oiuchi_Throw_B')
    Unknown14072('Oiuchi_Throw_C')

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2760)
        AirPushbackX(10000)
        AirPushbackY(50000)
        YImpluseBeforeWallbounce(2300)
        AirUntechableTime(70)
        HitAirUnblockable(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        setInvincible(1)
        GuardPoint_(1)
    sprite('tg405_00', 3)	# 1-3
    SFX_3('tgse_03')
    sprite('tg405_01', 1)	# 4-4
    sprite('tg405_01', 2)	# 5-6
    sprite('tg405_02', 1)	# 7-7
    sprite('tg405_02', 2)	# 8-9
    GFX_1('tgef_stock_AM', 0)
    SFX_3('tgse_27')
    sprite('tg405_02', 3)	# 10-12
    sprite('tg403_04ex01', 3)	# 13-15
    sprite('tg440_06', 5)	# 16-20	 **attackbox here**
    Unknown7007('6274673330345f300000000000000000640000006274673330345f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('BurstHodenEndStop', -1)
    GFX_0('BurstHodenBodyRay', -1)
    ScreenShake(5000, 20000)
    SFX_3('tgse_08')
    sprite('tg440_07', 5)	# 21-25
    setInvincible(0)
    GFX_0('BurstHodenEndStop', -1)
    sprite('tg440_08', 5)	# 26-30
    Unknown26('BurstHodenBodyRay')
    sprite('tg440_09', 5)	# 31-35
    GFX_0('BurstDDSmokeA', -1)
    loopRest()
    sprite('tg440_10', 3)	# 36-38
    sprite('tg440_11', 3)	# 39-41
    sprite('tg440_10', 3)	# 42-44
    sprite('tg440_11', 3)	# 45-47
    sprite('tg440_10', 3)	# 48-50
    sprite('tg440_11', 3)	# 51-53
    sprite('tg440_10', 3)	# 54-56
    sprite('tg403_08ex01', 5)	# 57-61
    sprite('tg403_10ex01', 5)	# 62-66

@State
def MTH():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(200)
        AttackP1(80)
        AttackP2(100)
        AirPushbackX(-2000)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(300)
        AirUntechableTime(60)
        Unknown9310(1)
        Hitstop(0)
        PushbackX(-22000)
        Unknown11057(600)
        Unknown11056(1)
        setInvincible(1)
        GuardPoint_(1)

        def upon_3():
            if SLOT_51:
                if (SLOT_2 >= 2):
                    Unknown2037(0)
                    SFX_0('005_swing_grap_2_0')
                    SFX_0('014_electric_m')
                    SFX_0('014_electric_l')
                    SFX_0('013_thunder_0')
                    GFX_0('tgef_430_light', 0)
                    GFX_0('tgef_430_light', 1)
                else:
                    Unknown2038(1)
        Unknown30055('a08601003200000000000000')
        Unknown30056('a08601003200000000000000')
    sprite('tg212_01', 6)	# 1-6
    SFX_3('tgse_02')
    tag_voice(1, 'btg250_0', 'btg250_1', '', '')
    sprite('tg212_03', 44)	# 7-50
    Unknown2036(38, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg430_00', 3)	# 51-53	 **attackbox here**
    sprite('tg430_01', 3)	# 54-56	 **attackbox here**
    sprite('tg430_02', 4)	# 57-60	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(5000)
    loopRest()
    SLOT_51 = 2
    label(0)
    sprite('tg430_03', 2)	# 61-62	 **attackbox here**
    RefreshMultihit()
    Unknown1015(-1000)
    sprite('tg430_04', 2)	# 63-64	 **attackbox here**
    RefreshMultihit()
    Unknown22022(0)
    sprite('tg430_05', 2)	# 65-66	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_06', 2)	# 67-68	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_07', 2)	# 69-70	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_08', 1)	# 71-71	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_08', 1)	# 72-72	 **attackbox here**
    if SLOT_51:
        sendToLabel(0)
        SLOT_51 = (SLOT_51 + (-1))
    else:
        sendToLabel(1)
    loopRest()
    label(1)
    sprite('tg430_09', 4)	# 73-76	 **attackbox here**
    clearUponHandler(3)
    setInvincible(0)
    Unknown2017(1)
    GFX_0('MTH_rotate_end', -1)
    GFX_0('MTH_punch_down', -1)
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg430_10', 4)	# 77-80	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    physicsXImpulse(0)
    Unknown1015(0)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg430_11', 5)	# 81-85	 **attackbox here**
    tag_voice(0, 'btg251_0', 'btg251_1', '', '')
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg430_12', 2)	# 86-87	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    SFX_0('005_swing_grap_2_2')
    sprite('tg430_13', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(4000)
    AttackP2(60)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirUntechableTime(80)
    AirPushbackX(6000)
    AirPushbackY(-55000)
    YImpluseBeforeWallbounce(2500)
    Unknown9190(1)
    Unknown11073(1)
    Unknown9310(0)
    Hitstop(28)
    PushbackX(12000)
    Unknown11057(1000)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown11056(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown20000(1)
    Unknown11072(1, 135000, 1000)
    SFX_0('209_down_normal_1')
    GFX_1('tgef_dustB', 0)
    GFX_0('StayMagneticA430b', 1)
    GFX_0('StayMagneticA430b', 2)
    GFX_0('GroundShake430', 3)
    GFX_0('tgef_430_light', 4)
    GFX_0('tgef_430_light', 5)
    ScreenShake(0, 10000)
    sprite('tg430_14', 15)	# 91-105	 **attackbox here**
    GFX_0('tgef_430_light', 3)
    GFX_0('tgef_430_light', 4)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    SFX_3('tgse_08')
    sprite('tg430_15', 10)	# 106-115	 **attackbox here**
    sprite('tg430_16', 9)	# 116-124	 **attackbox here**
    sprite('tg430_17', 5)	# 125-129	 **attackbox here**
    sprite('tg430_18', 10)	# 130-139
    sprite('tg430_19', 8)	# 140-147
    sprite('tg430_20', 5)	# 148-152
    sprite('tg430_21', 5)	# 153-157
    sprite('tg430_22', 5)	# 158-162

@State
def MTH_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(200)
        AttackP1(80)
        AttackP2(100)
        AirPushbackX(-2000)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(300)
        AirUntechableTime(60)
        Unknown9310(1)
        Hitstop(0)
        PushbackX(-22000)
        Unknown11057(600)
        Unknown11056(1)
        Unknown11091(20)
        setInvincible(1)
        GuardPoint_(1)

        def upon_3():
            if SLOT_51:
                if (SLOT_2 >= 2):
                    Unknown2037(0)
                    SFX_0('005_swing_grap_2_0')
                    SFX_0('014_electric_m')
                    SFX_0('014_electric_l')
                    SFX_0('013_thunder_0')
                    GFX_0('tgef_430_light', 0)
                    GFX_0('tgef_430_light', 1)
                else:
                    Unknown2038(1)
        Unknown30055('a08601003200000000000000')
        Unknown30056('a08601003200000000000000')
    sprite('tg212_01', 6)	# 1-6
    SFX_3('tgse_02')
    tag_voice(1, 'btg250_0', 'btg250_1', '', '')
    sprite('tg212_03', 44)	# 7-50
    Unknown2036(38, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg430_00', 3)	# 51-53	 **attackbox here**
    sprite('tg430_01', 3)	# 54-56	 **attackbox here**
    sprite('tg430_02', 4)	# 57-60	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(5000)
    loopRest()
    SLOT_51 = 2
    label(0)
    sprite('tg430_03', 2)	# 61-62	 **attackbox here**
    RefreshMultihit()
    Unknown1015(-1000)
    sprite('tg430_04', 2)	# 63-64	 **attackbox here**
    RefreshMultihit()
    Unknown22022(0)
    sprite('tg430_05', 2)	# 65-66	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_06', 2)	# 67-68	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_07', 2)	# 69-70	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_08', 1)	# 71-71	 **attackbox here**
    RefreshMultihit()
    sprite('tg430_08', 1)	# 72-72	 **attackbox here**
    if SLOT_51:
        sendToLabel(0)
        SLOT_51 = (SLOT_51 + (-1))
    else:
        sendToLabel(1)
    loopRest()
    label(1)
    sprite('tg430_09', 4)	# 73-76	 **attackbox here**
    tag_voice(0, 'btg251_0', 'btg251_1', '', '')
    clearUponHandler(3)
    setInvincible(0)
    Unknown2017(1)
    GFX_0('MTH_rotate_end', -1)
    GFX_0('MTH_punch_down', -1)
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg430_10', 4)	# 77-80	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    physicsXImpulse(0)
    Unknown1015(0)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg430_11', 5)	# 81-85	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg430_12', 2)	# 86-87	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    SFX_0('005_swing_grap_2_2')
    sprite('tg430_13', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(4000)
    AttackP2(60)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirUntechableTime(80)
    AirPushbackX(6000)
    AirPushbackY(-55000)
    YImpluseBeforeWallbounce(2300)
    Unknown9190(1)
    Unknown11073(1)
    Unknown9310(0)
    Hitstop(28)
    PushbackX(12000)
    Unknown11057(1000)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown11056(0)
    Unknown11072(1, 135000, 1000)
    SFX_0('209_down_normal_1')
    GFX_1('tgef_dustB', 0)
    GFX_0('StayMagneticA430b', 1)
    GFX_0('StayMagneticA430b', 2)
    GFX_0('GroundShake430', 3)
    GFX_0('tgef_430_light', 4)
    GFX_0('tgef_430_light', 5)
    ScreenShake(0, 10000)

    def upon_ON_HIT_OR_BLOCK():
        sendToLabel(99)
    sprite('tg430_14', 15)	# 91-105	 **attackbox here**
    GFX_0('tgef_430_light', 3)
    GFX_0('tgef_430_light', 4)
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    SFX_3('tgse_08')
    sprite('tg430_15', 5)	# 106-110	 **attackbox here**
    sprite('tg430_16', 9)	# 111-119	 **attackbox here**
    sprite('tg430_17', 5)	# 120-124	 **attackbox here**
    sprite('tg430_18', 10)	# 125-134
    sprite('tg430_19', 8)	# 135-142
    sprite('tg430_20', 5)	# 143-147
    sprite('tg430_21', 5)	# 148-152
    sprite('tg430_22', 5)	# 153-157
    ExitState()
    label(99)
    clearUponHandler(10)
    sprite('tg430_15', 5)	# 158-162	 **attackbox here**
    sprite('tg430_16', 9)	# 163-171	 **attackbox here**
    sprite('tg430_17', 4)	# 172-175	 **attackbox here**
    sprite('tg430_17', 1)	# 176-176	 **attackbox here**
    Unknown20000(1)
    sprite('tg431_02', 13)	# 177-189
    SFX_3('tgse_08')
    GFX_0('MTH_punch_str', 1)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_03', 3)	# 190-192
    Unknown20000(0)
    GFX_0('tgef_430_light', 0)
    sprite('tg431_04', 2)	# 193-194
    GFX_0('tgef_430_light', 0)
    sprite('tg431_05', 2)	# 195-196
    GFX_0('tgef_430_light', 0)
    SFX_3('tgse_08')
    sprite('tg431_06', 4)	# 197-200	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(3000)
    AttackP2(100)
    Unknown9190(0)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(72000)
    AirPushbackY(100)
    YImpluseBeforeWallbounce(0)
    Hitstop(18)
    AirUntechableTime(80)
    WallbounceReboundTime(0)
    Unknown9015(1)
    Unknown11056(0)
    Unknown2004(1, 0)
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    GFX_0('tgef_430_light', 2)
    GFX_0('tgef_appB', 3)
    GFX_0('tgef_DD_MH_finish', 4)
    SFX_0('016_explode_2')
    SFX_3('tgse_21')
    tag_voice(0, 'btg252_0', 'btg252_1', '', '')
    sprite('tg431_07', 4)	# 201-204	 **attackbox here**
    GFX_0('tgef_430_light', 0)
    GFX_0('tgef_430_light', 1)
    GFX_0('tgef_430_light', 2)
    SFX_0('014_electric_s')
    sprite('tg431_08', 4)	# 205-208	 **attackbox here**
    sprite('tg431_09', 6)	# 209-214
    sprite('tg431_10', 6)	# 215-220
    GFX_0('tgef_430_light', 0)
    sprite('tg431_11', 6)	# 221-226
    sprite('tg431_12', 6)	# 227-232
    sprite('tg431_13', 6)	# 233-238
    sprite('tg431_14', 6)	# 239-244
    sprite('tg431_15', 6)	# 245-250

@State
def GETB():

    def upon_IMMEDIATE():
        Unknown17011('GETBexe', 3, 0, 0)
        Unknown23055('')
        Unknown11054(320000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('GETBexe')
        SLOT_5 = 0

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        sendToLabelUpon(17, 1)
        SLOT_6 = 0
        callSubroutine('MAGNET_RESET')
    sprite('tg432_00', 3)	# 1-3
    SFX_3('tgse_02')
    loopRelated(17, 90)
    Unknown21003(600, 0)
    sprite('tg432_00', 2)	# 4-5
    Unknown21003(1200, 0)
    sprite('tg432_01', 2)	# 6-7	 **attackbox here**
    StartMultihit()
    Unknown21003(26000, 0)
    sprite('tg432_01', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    Unknown21003(1200, 0)
    sprite('tg432_01', 28)	# 10-37	 **attackbox here**
    StartMultihit()
    Unknown2036(28, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg432_01', 1)	# 38-38	 **attackbox here**
    RefreshMultihit()
    sprite('tg432_01', 1)	# 39-39	 **attackbox here**
    sprite('tg432_01', 2)	# 40-41	 **attackbox here**
    setInvincible(0)
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg432_01', 2)	# 42-43	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    sprite('tg432_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 46-47	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg432_48', 7)	# 50-56
    clearUponHandler(17)
    clearUponHandler(3)
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg432_49', 8)	# 57-64
    sprite('tg432_50', 7)	# 65-71
    SFX_1('btg155')
    sprite('tg432_51', 7)	# 72-78
    sprite('tg432_52', 6)	# 79-84
    sprite('tg432_53', 6)	# 85-90

@State
def GETB_TRUE():

    def upon_IMMEDIATE():
        Unknown17011('GETBexe', 3, 0, 0)
        Unknown23055('')
        Unknown11054(320000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('GETBexe')
        SLOT_5 = 0

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        sendToLabelUpon(17, 1)
        callSubroutine('MAGNET_RESET')
        SLOT_6 = 1
    sprite('tg432_00', 3)	# 1-3
    SFX_3('tgse_02')
    loopRelated(17, 90)
    Unknown21003(600, 0)
    sprite('tg432_00', 2)	# 4-5
    Unknown21003(1200, 0)
    sprite('tg432_01', 2)	# 6-7	 **attackbox here**
    StartMultihit()
    Unknown21003(26000, 0)
    sprite('tg432_01', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    Unknown21003(1200, 0)
    sprite('tg432_01', 28)	# 10-37	 **attackbox here**
    StartMultihit()
    Unknown2036(29, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg432_01', 1)	# 38-38	 **attackbox here**
    RefreshMultihit()
    sprite('tg432_01', 1)	# 39-39	 **attackbox here**
    sprite('tg432_01', 2)	# 40-41	 **attackbox here**
    setInvincible(0)
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg432_01', 2)	# 42-43	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    sprite('tg432_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 46-47	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg432_48', 7)	# 50-56
    clearUponHandler(17)
    clearUponHandler(3)
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg432_49', 8)	# 57-64
    sprite('tg432_50', 7)	# 65-71
    SFX_1('btg155')
    sprite('tg432_51', 7)	# 72-78
    sprite('tg432_52', 6)	# 79-84
    sprite('tg432_53', 6)	# 85-90

@State
def GETBexe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AirPushbackX(-2000)
        AirPushbackY(335000)
        YImpluseBeforeWallbounce(1600)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        AirUntechableTime(1000)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown23083(1)
        Unknown2004(1, 0)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11069('GETBJump')
        setInvincible(1)
    sprite('tg432_01', 6)	# 1-6	 **attackbox here**
    tag_voice(1, 'btg253_0', 'btg253_1', '', '')
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg432_02', 5)	# 7-11
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_04', 5)	# 12-16
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_05', 5)	# 17-21
    Unknown2018(1, 80)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_07', 5)	# 22-26
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_08', 5)	# 27-31
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_09', 5)	# 32-36
    Unknown2018(0, 80)
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_10', 5)	# 37-41
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_11', 5)	# 42-46
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_12', 5)	# 47-51
    Unknown2018(1, 80)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_14', 6)	# 52-57	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('100_hit_grap_2')
    sprite('tg432_15', 8)	# 58-65
    sprite('tg432_16', 8)	# 66-73
    sprite('tg432_18', 8)	# 74-81
    sprite('tg432_19', 8)	# 82-89
    sprite('tg432_20', 10)	# 90-99
    sprite('tg432_21', 25)	# 100-124
    SFX_3('tgse_00')
    SFX_0('209_down_normal_1')
    GFX_1('tgef432_janp', -1)
    ScreenShake(0, 12500)
    loopRest()
    enterState('GETBJump')

@State
def GETBJump():

    def upon_IMMEDIATE():
        Unknown17011('GETBDrop', 3, 1, 0)
        Unknown23056('')
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11025(0)
        AirUntechableTime(100)
        Unknown2018(0, 80)
        AttackP1(100)
        AttackP2(100)
        physicsYImpulse(490000)
        setGravity(5500)
        Unknown20000(1)
        Unknown20001(1)
        Unknown20002(1)
        Unknown8002()
        SFX_0('002_highjump_2')
        SFX_0('001_airbackdash_0')
        Unknown23083(1)
        Unknown11023(1)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11069('GETBDrop')
        setInvincible(1)
    sprite('tg432_24', 3)	# 1-3
    GFX_1('tgef_dustB', -1)
    GFX_0('GETBJumpEFF', 0)
    Unknown3029(1)
    tag_voice(0, 'btg254_0', 'btg254_1', '', '')
    sprite('tg432_25', 3)	# 4-6
    sprite('tg432_24', 3)	# 7-9
    ScreenShake(0, 5000)
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 10-12
    sprite('tg432_24', 3)	# 13-15
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 16-18
    sprite('tg432_24', 3)	# 19-21
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 22-24
    sprite('tg432_24', 3)	# 25-27
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 28-30
    sprite('tg432_24', 3)	# 31-33
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 34-36
    sprite('tg432_24', 3)	# 37-39
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 40-42
    sprite('tg432_24', 3)	# 43-45
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 46-48
    sprite('tg432_24', 3)	# 49-51
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 52-54
    sprite('tg432_24', 3)	# 55-57
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 58-60
    sprite('tg432_24', 3)	# 61-63
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 64-66
    sprite('tg432_24', 3)	# 67-69
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 70-72
    sprite('tg432_24', 3)	# 73-75
    sprite('tg432_24', 3)	# 76-78
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 79-81
    sprite('tg432_24', 3)	# 82-84
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 85-87
    sprite('tg432_24', 3)	# 88-90
    loopRest()
    tag_voice(0, 'btg255_0', 'btg255_1', '', '')
    label(0)
    sprite('tg432_27', 3)	# 91-93	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def GETBDrop():

    def upon_IMMEDIATE():
        Unknown17012(3, 1, 0)
        Unknown23056('')
        Unknown1018()
        Unknown1023()
        Unknown1038()
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown2018(0, 80)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown20000(1)
        Unknown20001(1)
        Unknown20002(1)
        Unknown13021(1)
        Unknown21005(1)
        Unknown23083(1)
        Hitstop(20)
        Damage(6120)
        if SLOT_6:
            Damage(6620)
        Unknown11068(1)
        Unknown11078(1)
        AirPushbackX(30000)
        AirPushbackY(-30000)
        AirUntechableTime(100)
        Unknown9310(52)
        AttackP2(60)
        Unknown11062(0)
        Unknown11099(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown13024(0)
        setInvincible(1)
    sprite('tg432_27', 7)	# 1-7	 **attackbox here**
    StartMultihit()
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    setGravity(5000)
    sprite('tg432_28', 1)	# 8-8
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    GFX_0('GETB_Fall', -1)
    sprite('tg432_30', 3)	# 9-11
    GFX_0('tgef_guardcrash', 6)
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    sprite('tg432_31', 2)	# 12-13
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 14-16
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(2000, 2000)
    sprite('tg432_31', 2)	# 17-18
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 19-21
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(3000, 3000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 22-23
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 24-26
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 27-28
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 29-31
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 32-33
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 34-36
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 37-38
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 39-41
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 42-43
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 44-46
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 47-48
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 49-51
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 52-53
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 54-56
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 57-58
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    label(0)
    sprite('tg432_30', 3)	# 59-61
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(5000, 5000)
    SFX_0('000_airdash_2')
    SFX_3('tgse_01')
    sprite('tg432_31', 2)	# 62-63
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg432_32', 3)	# 64-66
    Unknown13024(1)
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    Unknown8000(100, 1, 1)
    ScreenShake(0, 7500)
    GFX_0('GETB_Crash', -1)
    GFX_1('tgef_dustC', -1)
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    AttackLevel_(4)
    tag_voice(0, 'btg256_0', 'btg256_1', '', '')
    sprite('tg432_33', 3)	# 67-69	 **attackbox here**
    Unknown5000(29, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    GFX_0('tgefGETBexpl', -1)
    GFX_1('tgef_dustA03', 1)
    GFX_1('tgef_dustA03', 2)
    SFX_3('tgse_00')
    sprite('tg432_34', 3)	# 70-72	 **attackbox here**
    Unknown4048(400000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    Unknown4048(-410000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000002000000')
    ScreenShake(0, 5000)
    sprite('tg432_35', 23)	# 73-95
    sprite('tg432_36', 6)	# 96-101
    sprite('tg432_37', 6)	# 102-107
    sprite('tg432_38', 6)	# 108-113
    sprite('tg432_39', 6)	# 114-119
    sprite('tg432_40', 5)	# 120-124
    sprite('tg432_41', 5)	# 125-129
    sprite('tg432_42', 5)	# 130-134
    sprite('tg432_43', 5)	# 135-139
    sprite('tg432_44', 5)	# 140-144
    SLOT_6 = 0

@State
def GETB_OD():

    def upon_IMMEDIATE():
        Unknown17011('GETBexe_OD', 3, 0, 0)
        Unknown23055('')
        AttackP1(100)
        AttackP2(100)
        Unknown11054(320000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        Unknown11069('GETBexe_OD')
        SLOT_5 = 0

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        Unknown30048(1)
        SLOT_6 = 0
        sendToLabelUpon(17, 1)
        setInvincible(1)
        callSubroutine('MAGNET_RESET')
    sprite('tg432_00', 3)	# 1-3
    SFX_3('tgse_02')
    loopRelated(17, 90)
    Unknown21003(600, 0)
    sprite('tg432_00', 2)	# 4-5
    Unknown21003(1200, 0)
    sprite('tg432_01', 2)	# 6-7	 **attackbox here**
    StartMultihit()
    Unknown21003(26000, 0)
    sprite('tg432_01', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    Unknown21003(1200, 0)
    sprite('tg432_01', 28)	# 10-37	 **attackbox here**
    StartMultihit()
    Unknown2036(28, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg432_01', 1)	# 38-38	 **attackbox here**
    RefreshMultihit()
    sprite('tg432_01', 1)	# 39-39	 **attackbox here**
    sprite('tg432_01', 2)	# 40-41	 **attackbox here**
    setInvincible(0)
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg432_01', 2)	# 42-43	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    sprite('tg432_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 46-47	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg432_48', 7)	# 50-56
    clearUponHandler(17)
    clearUponHandler(3)
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg432_49', 8)	# 57-64
    sprite('tg432_50', 7)	# 65-71
    SFX_1('btg155')
    sprite('tg432_51', 7)	# 72-78
    sprite('tg432_52', 6)	# 79-84
    sprite('tg432_53', 6)	# 85-90

@State
def GETB_OD_TRUE():

    def upon_IMMEDIATE():
        Unknown17011('GETBexe_OD', 3, 0, 0)
        Unknown23055('')
        AttackP1(100)
        AttackP2(100)
        Unknown11054(320000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        Unknown11069('GETBexe_OD')
        SLOT_5 = 0

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        Unknown30048(1)
        sendToLabelUpon(17, 1)
        setInvincible(1)
        callSubroutine('MAGNET_RESET')
        SLOT_6 = 1
    sprite('tg432_00', 3)	# 1-3
    SFX_3('tgse_02')
    loopRelated(17, 90)
    Unknown21003(600, 0)
    sprite('tg432_00', 2)	# 4-5
    Unknown21003(1200, 0)
    sprite('tg432_01', 2)	# 6-7	 **attackbox here**
    StartMultihit()
    Unknown21003(26000, 0)
    sprite('tg432_01', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    Unknown21003(1200, 0)
    sprite('tg432_01', 28)	# 10-37	 **attackbox here**
    StartMultihit()
    Unknown2036(28, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg432_01', 1)	# 38-38	 **attackbox here**
    RefreshMultihit()
    sprite('tg432_01', 1)	# 39-39	 **attackbox here**
    sprite('tg432_01', 2)	# 40-41	 **attackbox here**
    setInvincible(0)
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg432_01', 2)	# 42-43	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    sprite('tg432_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 46-47	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg432_48', 7)	# 50-56
    clearUponHandler(17)
    clearUponHandler(3)
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg432_49', 8)	# 57-64
    sprite('tg432_50', 7)	# 65-71
    SFX_1('btg155')
    sprite('tg432_51', 7)	# 72-78
    sprite('tg432_52', 6)	# 79-84
    sprite('tg432_53', 6)	# 85-90

@State
def GETBexe_OD():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AirPushbackX(-2000)
        AirPushbackY(335000)
        YImpluseBeforeWallbounce(1600)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Damage(0)
        AirUntechableTime(1000)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown23083(1)
        Unknown2004(1, 0)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11069('GETBJump_OD')
        setInvincible(1)
    sprite('tg432_01', 6)	# 1-6	 **attackbox here**
    tag_voice(1, 'btg253_0', 'btg253_1', '', '')
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg432_02', 5)	# 7-11
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_04', 5)	# 12-16
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_05', 5)	# 17-21
    Unknown2018(1, 80)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_07', 5)	# 22-26
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_08', 5)	# 27-31
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_09', 5)	# 32-36
    Unknown2018(0, 80)
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_10', 5)	# 37-41
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_11', 5)	# 42-46
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_12', 5)	# 47-51
    Unknown2018(1, 80)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_14', 6)	# 52-57	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('100_hit_grap_2')
    sprite('tg432_15', 8)	# 58-65
    sprite('tg432_16', 8)	# 66-73
    sprite('tg432_18', 8)	# 74-81
    sprite('tg432_19', 8)	# 82-89
    sprite('tg432_20', 10)	# 90-99
    sprite('tg432_21', 25)	# 100-124
    SFX_3('tgse_00')
    SFX_0('209_down_normal_1')
    GFX_1('tgef432_janp', -1)
    ScreenShake(0, 12500)
    loopRest()
    enterState('GETBJump_OD')

@State
def GETBJump_OD():

    def upon_IMMEDIATE():
        Unknown17011('GETBDrop_OD', 3, 1, 0)
        Unknown23056('')
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11025(0)
        AirUntechableTime(100)
        Unknown2018(0, 80)
        AttackP1(100)
        AttackP2(100)
        physicsYImpulse(490000)
        setGravity(5500)
        Unknown20000(1)
        Unknown20001(1)
        Unknown20002(1)
        Unknown8002()
        SFX_0('002_highjump_2')
        SFX_0('001_airbackdash_0')
        Unknown23083(1)
        Unknown11023(1)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11069('GETBDrop_OD')
        setInvincible(1)
    sprite('tg432_24', 3)	# 1-3
    GFX_1('tgef_dustB', -1)
    GFX_0('GETBJumpEFF', 0)
    Unknown3029(1)
    tag_voice(0, 'btg254_0', 'btg254_1', '', '')
    sprite('tg432_25', 3)	# 4-6
    sprite('tg432_24', 3)	# 7-9
    ScreenShake(0, 5000)
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 10-12
    sprite('tg432_24', 3)	# 13-15
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 16-18
    sprite('tg432_24', 3)	# 19-21
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 22-24
    sprite('tg432_24', 3)	# 25-27
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 28-30
    sprite('tg432_24', 3)	# 31-33
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 34-36
    sprite('tg432_24', 3)	# 37-39
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 40-42
    sprite('tg432_24', 3)	# 43-45
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 46-48
    sprite('tg432_24', 3)	# 49-51
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 52-54
    sprite('tg432_24', 3)	# 55-57
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 58-60
    sprite('tg432_24', 3)	# 61-63
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 64-66
    sprite('tg432_24', 3)	# 67-69
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 70-72
    sprite('tg432_24', 3)	# 73-75
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 76-78
    sprite('tg432_24', 3)	# 79-81
    GFX_0('GETBJumpEFF', 0)
    sprite('tg432_25', 3)	# 82-84
    sprite('tg432_24', 3)	# 85-87
    loopRest()
    tag_voice(0, 'btg255_0', 'btg255_1', '', '')
    label(0)
    sprite('tg432_27', 3)	# 88-90	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def GETBDrop_OD():

    def upon_IMMEDIATE():
        Unknown17012(3, 1, 0)
        Unknown23056('')
        Unknown1018()
        Unknown1023()
        Unknown1038()
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown2018(0, 80)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown20000(1)
        Unknown20001(1)
        Unknown20002(1)
        Unknown13021(1)
        Unknown21005(1)
        Unknown23083(1)
        Hitstop(20)
        Damage(7120)
        if SLOT_6:
            Damage(7620)
        Unknown11068(1)
        Unknown11078(1)
        AirPushbackX(30000)
        AirPushbackY(-30000)
        AirUntechableTime(100)
        Unknown9310(52)
        AttackP2(60)
        Unknown11062(0)
        Unknown13024(0)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11099(1)
        setInvincible(1)
    sprite('tg432_27', 7)	# 1-7	 **attackbox here**
    StartMultihit()
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    setGravity(5000)
    sprite('tg432_28', 1)	# 8-8
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    GFX_0('GETB_Fall', -1)
    sprite('tg432_30', 3)	# 9-11
    GFX_0('tgef_guardcrash', 6)
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    sprite('tg432_31', 2)	# 12-13
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 14-16
    GFX_0('OdHandThunder', 6)
    GFX_0('OdFallEff', -1)
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(2000, 2000)
    sprite('tg432_31', 2)	# 17-18
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 19-21
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(3000, 3000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 22-23
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 24-26
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 27-28
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 29-31
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 32-33
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 34-36
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 37-38
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 39-41
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 42-43
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 44-46
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 47-48
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 49-51
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 52-53
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    sprite('tg432_30', 3)	# 54-56
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(4000, 4000)
    SFX_3('tgse_01')
    SFX_0('000_airdash_2')
    sprite('tg432_31', 2)	# 57-58
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    label(0)
    sprite('tg432_30', 3)	# 59-61
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('GETBFallBody', 5)
    ScreenShake(5000, 5000)
    SFX_0('000_airdash_2')
    SFX_3('tgse_01')
    sprite('tg432_31', 2)	# 62-63
    Unknown5000(27, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg432_32', 3)	# 64-66
    Unknown13024(1)
    Unknown21015('4f6448616e645468756e64657200000000000000000000000000000000000000f501000000000000')
    GFX_0('OdFallThunder', -1)
    Unknown5000(28, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    Unknown8000(100, 1, 1)
    ScreenShake(0, 7500)
    GFX_0('GETB_Crash', -1)
    GFX_1('tgef_dustC', -1)
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    AttackLevel_(4)
    tag_voice(0, 'btg256_0', 'btg256_1', '', '')
    sprite('tg432_33', 3)	# 67-69	 **attackbox here**
    Unknown5000(29, 0)
    Unknown5001('0700000000000000000000000000000001000000')
    GFX_0('tgefGETBexpl', -1)
    GFX_1('tgef_dustA03', 1)
    GFX_1('tgef_dustA03', 2)
    SFX_3('tgse_00')
    sprite('tg432_34', 3)	# 70-72	 **attackbox here**
    Unknown4048(400000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    Unknown4048(-410000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000002000000')
    ScreenShake(0, 5000)
    sprite('tg432_35', 23)	# 73-95
    sprite('tg432_36', 6)	# 96-101
    sprite('tg432_37', 6)	# 102-107
    sprite('tg432_38', 6)	# 108-113
    sprite('tg432_39', 6)	# 114-119
    sprite('tg432_40', 5)	# 120-124
    sprite('tg432_41', 5)	# 125-129
    sprite('tg432_42', 5)	# 130-134
    sprite('tg432_43', 5)	# 135-139
    sprite('tg432_44', 5)	# 140-144

@State
def Air_GETB():

    def upon_IMMEDIATE():
        Unknown17011('Air_GETBExe', 3, 1, 0)
        Unknown23055('')
        Unknown11032('801a060001000000ffffffffffffffff')
        Unknown11054(210000)
        Damage(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown2018(0, 80)
        loopRelated(17, 101)
        sendToLabelUpon(17, 1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown23001(0, 0)
        Unknown11069('Air_GETBExe')
        callSubroutine('MAGNET_RESET')
        setInvincible(1)

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        SLOT_6 = 0
    sprite('tg410_00', 5)	# 1-5
    sprite('tg410_01', 27)	# 6-32	 **attackbox here**
    Unknown1084(1)
    StartMultihit()
    Unknown2036(28, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg410_01', 1)	# 33-33	 **attackbox here**
    GFX_0('AirGETBDmyMagnet2', 6)
    Unknown22004(13, 1)
    sprite('tg410_01', 2)	# 34-35	 **attackbox here**
    setInvincible(0)
    Unknown1084(1)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 36-37	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 38-39	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 40-41	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg410_01', 2)	# 42-43	 **attackbox here**
    Unknown1084(1)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 46-47	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(24)
    clearUponHandler(25)
    clearUponHandler(3)
    sprite('tg410_02', 1)	# 50-50	 **attackbox here**
    Unknown2015(-1)
    sprite('tg410_08', 5)	# 51-55
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg410_09', 4)	# 56-59
    sprite('tg410_10', 4)	# 60-63
    SFX_1('btg155')
    sprite('tg410_11', 4)	# 64-67
    setGravity(800)
    sprite('tg410_11', 4)	# 68-71
    sprite('tg410_12', 4)	# 72-75
    sprite('tg410_13', 4)	# 76-79
    sprite('tg020_05', 3)	# 80-82
    sprite('tg020_06', 3)	# 83-85
    label(2)
    sprite('tg020_07', 3)	# 86-88
    sprite('tg020_08', 3)	# 89-91
    gotoLabel(2)

@State
def Air_GETB_TRUE():

    def upon_IMMEDIATE():
        Unknown17011('Air_GETBExe', 3, 1, 0)
        Unknown23055('')
        Unknown11032('801a060001000000ffffffffffffffff')
        Unknown11054(210000)
        Damage(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown2018(0, 80)
        loopRelated(17, 101)
        sendToLabelUpon(17, 1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown23001(0, 0)
        Unknown11069('Air_GETBExe')
        callSubroutine('MAGNET_RESET')
        setInvincible(1)

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        SLOT_6 = 1
    sprite('tg410_00', 5)	# 1-5
    sprite('tg410_01', 27)	# 6-32	 **attackbox here**
    Unknown1084(1)
    StartMultihit()
    Unknown2036(28, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg410_01', 1)	# 33-33	 **attackbox here**
    GFX_0('AirGETBDmyMagnet2', 6)
    Unknown22004(13, 1)
    sprite('tg410_01', 2)	# 34-35	 **attackbox here**
    setInvincible(0)
    Unknown1084(1)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 36-37	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 38-39	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 40-41	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg410_01', 2)	# 42-43	 **attackbox here**
    Unknown1084(1)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 46-47	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(24)
    clearUponHandler(25)
    clearUponHandler(3)
    sprite('tg410_02', 1)	# 50-50	 **attackbox here**
    Unknown2015(-1)
    sprite('tg410_08', 5)	# 51-55
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg410_09', 4)	# 56-59
    sprite('tg410_10', 4)	# 60-63
    SFX_1('btg155')
    sprite('tg410_11', 4)	# 64-67
    setGravity(800)
    sprite('tg410_11', 4)	# 68-71
    sprite('tg410_12', 4)	# 72-75
    sprite('tg410_13', 4)	# 76-79
    sprite('tg020_05', 3)	# 80-82
    sprite('tg020_06', 3)	# 83-85
    label(2)
    sprite('tg020_07', 3)	# 86-88
    sprite('tg020_08', 3)	# 89-91
    gotoLabel(2)

@State
def Air_GETBExe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Unknown11068(1)
        Unknown11078(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(-300000)
        YImpluseBeforeWallbounce(0)
        Unknown11099(1)
        Hitstop(0)
        AirUntechableTime(600)
        Unknown9310(600)
        Unknown11062(0)
        Unknown23083(1)
        Unknown11069('Air_GETBExe')
        Unknown13021(1)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
    sprite('tg320_02', 2)	# 1-2	 **attackbox here**
    tag_voice(1, 'btg257_0', 'btg257_1', '', '')
    StartMultihit()
    Unknown5000(9, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('tg321_00', 3)	# 3-5
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    sprite('tg321_01', 3)	# 6-8
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg321_02', 3)	# 9-11
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg321_03', 3)	# 12-14
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg321_04', 3)	# 15-17	 **attackbox here**
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown2018(0, 80)
    AttackLevel_(3)
    sprite('tg321_05', 3)	# 18-20
    sprite('tg321_06', 3)	# 21-23
    sprite('tg321_07', 3)	# 24-26
    sprite('tg321_08', 3)	# 27-29
    Unknown1043()
    sprite('tg260_00', 2)	# 30-31
    Unknown2006()
    sprite('tg260_01', 2)	# 32-33

    def upon_LANDING():
        RefreshMultihit()
        sendToLabel(1)
    physicsXImpulse(0)
    physicsYImpulse(-10)
    setGravity(10)
    sprite('tg260_02', 3)	# 34-36
    sprite('tg260_03', 3)	# 37-39
    SFX_0('005_swing_grap_2_2')
    sprite('tg260_04', 3)	# 40-42	 **attackbox here**
    setGravity(2000)
    loopRest()
    tag_voice(0, 'btg258_0', 'btg258_1', '', '')
    label(0)
    sprite('tg260_05', 3)	# 43-45	 **attackbox here**
    sprite('tg260_04', 3)	# 46-48	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg260_06', 2)	# 49-50	 **attackbox here**
    Unknown36(22)
    teleportRelativeY(0)
    Unknown35()
    Damage(730)
    Unknown11099(0)
    YImpluseBeforeWallbounce(1000)
    AirPushbackY(20000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown9190(1)
    Unknown2018(0, 80)
    Unknown20000(1)
    Unknown23083(1)
    Unknown2004(1, 0)
    Unknown13024(0)
    Unknown11068(1)
    Unknown11078(1)
    Unknown30048(1)
    Unknown30061(0)
    Unknown11064(1)
    setInvincible(1)
    Unknown11069('Air_GETBExe2')
    Unknown8000(100, 1, 1)
    SFX_3('tgse_26')
    Unknown1084(1)
    ScreenShake(0, 7500)
    SFX_0('213_bound_1')
    GFX_1('tgef_dustB', 0)
    GFX_1('tgef_dustB', 1)
    GFX_1('tgef_dustA', 2)
    Unknown11023(1)
    sprite('tg260_06', 8)	# 51-58	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('tg260_07', 3)	# 59-61
    sprite('tg260_08', 3)	# 62-64
    sprite('tg260_09', 4)	# 65-68
    sprite('tg010_00', 3)	# 69-71
    ScreenShake(0, 3500)
    SFX_0('019_quake_0')
    SFX_3('tgse_26')
    Unknown8000(100, 1, 1)
    sprite('tg010_01', 3)	# 72-74
    enterState('Air_GETBExe2')

@State
def Air_GETBExe2():

    def upon_IMMEDIATE():
        Unknown17011('Air_GETBExe3', 3, 1, 0)
        Unknown23056('')
        Damage(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11054(320000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        Unknown23083(1)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('Air_GETBExe3')
        callSubroutine('MAGNET_RESET')
        Unknown30061(0)
        Unknown11002(-1)
    sprite('tg432_00', 2)	# 1-2
    Unknown21003(26000, 0)
    SFX_3('tgse_02')
    sprite('tg432_00', 2)	# 3-4
    Unknown21003(1200, 0)
    sprite('tg432_01', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    sprite('tg432_01', 1)	# 6-6	 **attackbox here**
    sprite('tg432_01', 2)	# 7-8	 **attackbox here**
    setInvincible(0)
    sprite('tg432_48', 7)	# 9-15
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg432_49', 8)	# 16-23
    sprite('tg432_50', 7)	# 24-30
    SFX_1('btg155')
    sprite('tg432_51', 7)	# 31-37
    sprite('tg432_52', 6)	# 38-43
    sprite('tg432_53', 6)	# 44-49

@State
def Air_GETBExe3():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AirPushbackX(-2000)
        AirPushbackY(335000)
        YImpluseBeforeWallbounce(1600)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Damage(0)
        AirUntechableTime(1000)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown23083(1)
        Unknown2004(1, 0)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('GETBJump')
        setInvincible(1)
    sprite('tg432_01', 6)	# 1-6	 **attackbox here**
    tag_voice(0, 'btg253_0', 'btg253_1', '', '')
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg432_02', 5)	# 7-11
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_04', 5)	# 12-16
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_05', 5)	# 17-21
    Unknown2018(1, 80)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_07', 5)	# 22-26
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_08', 5)	# 27-31
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_09', 5)	# 32-36
    Unknown2018(0, 80)
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_10', 5)	# 37-41
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_11', 5)	# 42-46
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_12', 5)	# 47-51
    Unknown2018(1, 80)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_14', 6)	# 52-57	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('100_hit_grap_2')
    sprite('tg432_15', 8)	# 58-65
    sprite('tg432_16', 8)	# 66-73
    sprite('tg432_18', 8)	# 74-81
    sprite('tg432_19', 8)	# 82-89
    sprite('tg432_20', 10)	# 90-99
    sprite('tg432_21', 25)	# 100-124
    SFX_3('tgse_00')
    SFX_0('209_down_normal_1')
    GFX_1('tgef432_janp', -1)
    ScreenShake(0, 12500)
    loopRest()
    enterState('GETBJump')

@State
def Air_GETB_OD():

    def upon_IMMEDIATE():
        Unknown17011('Air_GETBExeOD', 3, 1, 0)
        Unknown23055('')
        Damage(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11054(210000)
        Unknown11032('801a060001000000ffffffffffffffff')
        Unknown2018(0, 80)
        loopRelated(17, 111)
        sendToLabelUpon(17, 1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown23001(0, 0)
        Unknown11069('Air_GETBExeOD')
        callSubroutine('MAGNET_RESET')
        setInvincible(1)

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        SLOT_6 = 0
    sprite('tg410_00', 5)	# 1-5
    sprite('tg410_01', 27)	# 6-32	 **attackbox here**
    Unknown1084(1)
    StartMultihit()
    Unknown2036(28, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg410_01', 1)	# 33-33	 **attackbox here**
    GFX_0('AirGETBDmyMagnet2', 6)
    Unknown22004(13, 1)
    sprite('tg410_01', 2)	# 34-35	 **attackbox here**
    setInvincible(0)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 36-37	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 38-39	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 40-41	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg410_01', 2)	# 42-43	 **attackbox here**
    Unknown1084(1)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 46-47	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(24)
    clearUponHandler(25)
    clearUponHandler(3)
    sprite('tg410_02', 1)	# 50-50	 **attackbox here**
    Unknown2015(-1)
    sprite('tg410_08', 5)	# 51-55
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg410_09', 4)	# 56-59
    sprite('tg410_10', 4)	# 60-63
    SFX_1('btg155')
    sprite('tg410_11', 4)	# 64-67
    setGravity(800)
    sprite('tg410_11', 4)	# 68-71
    sprite('tg410_12', 4)	# 72-75
    sprite('tg410_13', 4)	# 76-79
    sprite('tg020_05', 3)	# 80-82
    sprite('tg020_06', 3)	# 83-85
    label(2)
    sprite('tg020_07', 3)	# 86-88
    sprite('tg020_08', 3)	# 89-91
    gotoLabel(2)

@State
def Air_GETB_OD_TRUE():

    def upon_IMMEDIATE():
        Unknown17011('Air_GETBExeOD', 3, 1, 0)
        Unknown23055('')
        Damage(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11054(210000)
        Unknown11032('801a060001000000ffffffffffffffff')
        Unknown2018(0, 80)
        loopRelated(17, 111)
        sendToLabelUpon(17, 1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown23001(0, 0)
        Unknown11069('Air_GETBExeOD')
        callSubroutine('MAGNET_RESET')
        setInvincible(1)

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
        SLOT_6 = 1
    sprite('tg410_00', 5)	# 1-5
    sprite('tg410_01', 27)	# 6-32	 **attackbox here**
    Unknown1084(1)
    StartMultihit()
    Unknown2036(28, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('tg410_01', 1)	# 33-33	 **attackbox here**
    GFX_0('AirGETBDmyMagnet2', 6)
    Unknown22004(13, 1)
    sprite('tg410_01', 2)	# 34-35	 **attackbox here**
    setInvincible(0)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 36-37	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 38-39	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 40-41	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg410_01', 2)	# 42-43	 **attackbox here**
    Unknown1084(1)
    Unknown21003(1150, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 44-45	 **attackbox here**
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 46-47	 **attackbox here**
    Unknown21003(575, 0)
    GFX_0('MagneticStorm', 0)
    GFX_0('StayMagneticA400', 1)
    GFX_0('StayMagneticA400', 2)
    GFX_0('StayMagneticA400', 3)
    GFX_0('StayMagneticA400', 4)
    SFX_0('014_electric_m')
    sprite('tg410_01', 2)	# 48-49	 **attackbox here**
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(24)
    clearUponHandler(25)
    clearUponHandler(3)
    sprite('tg410_02', 1)	# 50-50	 **attackbox here**
    Unknown2015(-1)
    sprite('tg410_08', 5)	# 51-55
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg410_09', 4)	# 56-59
    sprite('tg410_10', 4)	# 60-63
    SFX_1('btg155')
    sprite('tg410_11', 4)	# 64-67
    setGravity(800)
    sprite('tg410_11', 4)	# 68-71
    sprite('tg410_12', 4)	# 72-75
    sprite('tg410_13', 4)	# 76-79
    sprite('tg020_05', 3)	# 80-82
    sprite('tg020_06', 3)	# 83-85
    label(2)
    sprite('tg020_07', 3)	# 86-88
    sprite('tg020_08', 3)	# 89-91
    gotoLabel(2)

@State
def Air_GETBExeOD():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        Damage(0)
        Unknown11068(1)
        Unknown11078(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(-300000)
        YImpluseBeforeWallbounce(0)
        Unknown11099(1)
        Hitstop(0)
        AirUntechableTime(600)
        Unknown9310(600)
        Unknown11062(0)
        Unknown23083(1)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('Air_GETBExeOD')
        Unknown13021(1)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
    sprite('tg320_02', 2)	# 1-2	 **attackbox here**
    tag_voice(1, 'btg257_0', 'btg257_1', '', '')
    StartMultihit()
    Unknown5000(9, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('tg321_00', 3)	# 3-5
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    sprite('tg321_01', 3)	# 6-8
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg321_02', 3)	# 9-11
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg321_03', 3)	# 12-14
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg321_04', 3)	# 15-17	 **attackbox here**
    Unknown5000(4, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown2018(0, 80)
    AttackLevel_(3)
    sprite('tg321_05', 3)	# 18-20
    sprite('tg321_06', 3)	# 21-23
    sprite('tg321_07', 3)	# 24-26
    sprite('tg321_08', 3)	# 27-29
    Unknown1043()
    sprite('tg260_00', 2)	# 30-31
    Unknown2006()
    sprite('tg260_01', 2)	# 32-33

    def upon_LANDING():
        RefreshMultihit()
        sendToLabel(1)
    physicsXImpulse(0)
    physicsYImpulse(-10)
    setGravity(10)
    sprite('tg260_02', 3)	# 34-36
    sprite('tg260_03', 3)	# 37-39
    SFX_0('005_swing_grap_2_2')
    sprite('tg260_04', 3)	# 40-42	 **attackbox here**
    setGravity(2000)
    loopRest()
    tag_voice(0, 'btg258_0', 'btg0258_1', '', '')
    label(0)
    sprite('tg260_05', 3)	# 43-45	 **attackbox here**
    sprite('tg260_04', 3)	# 46-48	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg260_06', 2)	# 49-50	 **attackbox here**
    Unknown36(22)
    teleportRelativeY(0)
    Unknown35()
    Unknown11099(0)
    Damage(730)
    YImpluseBeforeWallbounce(1000)
    AirPushbackY(20000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown9190(1)
    Unknown2018(0, 80)
    Unknown20000(1)
    Unknown23083(1)
    Unknown2004(1, 0)
    Unknown13024(0)
    Unknown11068(1)
    Unknown11078(1)
    Unknown11064(1)
    Unknown30048(1)
    Unknown30061(0)
    setInvincible(1)
    Unknown11069('Air_GETBExe2OD')
    Unknown8000(100, 1, 1)
    SFX_3('tgse_26')
    Unknown1084(1)
    ScreenShake(0, 7500)
    SFX_0('213_bound_1')
    GFX_1('tgef_dustB', 0)
    GFX_1('tgef_dustB', 1)
    GFX_1('tgef_dustA', 2)
    Unknown11023(1)
    sprite('tg260_06', 8)	# 51-58	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('tg260_07', 3)	# 59-61
    sprite('tg260_08', 3)	# 62-64
    sprite('tg260_09', 4)	# 65-68
    sprite('tg010_00', 3)	# 69-71
    ScreenShake(0, 3500)
    SFX_0('019_quake_0')
    SFX_3('tgse_26')
    Unknown8000(100, 1, 1)
    sprite('tg010_01', 3)	# 72-74
    enterState('Air_GETBExe2OD')

@State
def Air_GETBExe2OD():

    def upon_IMMEDIATE():
        Unknown17011('Air_GETBExe3OD', 3, 1, 0)
        Unknown23056('')
        Damage(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11054(320000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        Unknown23083(1)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('Air_GETBExe3OD')
        SLOT_5 = 0

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0x13)):
                    clearUponHandler(3)
                    sendToLabel(1)
        sendToLabelUpon(17, 1)
        callSubroutine('MAGNET_RESET')
        Unknown30061(0)
        Unknown11002(-1)
    sprite('tg432_00', 2)	# 1-2
    Unknown21003(26000, 0)
    SFX_3('tgse_02')
    loopRelated(17, 90)
    sprite('tg432_00', 2)	# 3-4
    Unknown21003(1200, 0)
    sprite('tg432_01', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    sprite('tg432_01', 1)	# 6-6	 **attackbox here**
    sprite('tg432_01', 2)	# 7-8	 **attackbox here**
    setInvincible(0)
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg432_01', 2)	# 9-10	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    sprite('tg432_01', 2)	# 11-12	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 13-14	 **attackbox here**
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 2)
    GFX_0('StayMagneticA432', 3)
    GFX_0('StayMagneticA432', 4)
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg432_01ex01', 2)	# 15-16	 **attackbox here**
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tg432_48', 7)	# 17-23
    clearUponHandler(17)
    clearUponHandler(3)
    Unknown21003(0, 0)
    SFX_0('006_swing_blade_0')
    sprite('tg432_49', 8)	# 24-31
    sprite('tg432_50', 7)	# 32-38
    SFX_1('btg155')
    sprite('tg432_51', 7)	# 39-45
    sprite('tg432_52', 6)	# 46-51
    sprite('tg432_53', 6)	# 52-57

@State
def Air_GETBExe3OD():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AirPushbackX(-2000)
        AirPushbackY(335000)
        YImpluseBeforeWallbounce(1600)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Damage(0)
        AirUntechableTime(1000)
        Unknown2018(0, 80)
        Unknown20000(1)
        Unknown23083(1)
        Unknown2004(1, 0)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown30048(1)
        Unknown30061(0)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('GETBJump_OD')
        setInvincible(1)
    sprite('tg432_01', 6)	# 1-6	 **attackbox here**
    tag_voice(0, 'btg253_0', 'btg253_1', '', '')
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tg432_02', 5)	# 7-11
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_04', 5)	# 12-16
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_05', 5)	# 17-21
    Unknown2018(1, 80)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_07', 5)	# 22-26
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_08', 5)	# 27-31
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_09', 5)	# 32-36
    Unknown2018(0, 80)
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_10', 5)	# 37-41
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_11', 5)	# 42-46
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('tg432_12', 5)	# 47-51
    Unknown2018(1, 80)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('tg432_14', 6)	# 52-57	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('100_hit_grap_2')
    sprite('tg432_15', 8)	# 58-65
    sprite('tg432_16', 8)	# 66-73
    sprite('tg432_18', 8)	# 74-81
    sprite('tg432_19', 8)	# 82-89
    sprite('tg432_20', 10)	# 90-99
    sprite('tg432_21', 25)	# 100-124
    SFX_3('tgse_00')
    SFX_0('209_down_normal_1')
    GFX_1('tgef432_janp', -1)
    ScreenShake(0, 12500)
    loopRest()
    enterState('GETBJump_OD')

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown17011('AstralHeat2', 6, 0, 0)
        Unknown11069('AstralHeat2')
        Unknown11002(-1)
        AttackLevel_(5)
        Unknown9130(220)
        Unknown9142(200)
        Unknown11054(320000)
        Unknown11032('80ee36000100000000e20400ffffffff')
        Unknown11045(0)
        Unknown30061(0)
        Unknown2006()
        Unknown2018(0, 80)
        Unknown2004(1, 0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11091(100)
        setInvincible(1)

        def upon_3():
            if SLOT_2:
                if (not CheckInput(0xa)):
                    if (not CheckInput(0x13)):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (not CheckInput(0x13)):
                    if (not CheckInput(0xa)):
                        clearUponHandler(3)
                        sendToLabel(1)

        def upon_STATE_END():
            Unknown3025(-1, 1)
        sendToLabelUpon(17, 1)
    sprite('tg450_00', 4)	# 1-4
    loopRelated(17, 128)
    sprite('tg450_01', 55)	# 5-59
    Unknown2036(50, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_TG_AH', -1)
    GFX_1('tgef_asthandpow', 0)
    GFX_1('tgef_asthandpow', 1)
    tag_voice(1, 'btg290_0', 'btg290_1', '', '')
    loopRest()
    Unknown2037(1)
    label(0)
    sprite('tg450_01', 2)	# 60-61
    Unknown21003(4500, 3000)
    if (SLOT_19 <= 180000):
        Unknown21003(0, 3000)
    GFX_0('MagneticStorm', 0)
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 0)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 0)
    sprite('tg450_01', 2)	# 62-63
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg450_01', 2)	# 64-65
    Unknown21003(4500, 3000)
    if (SLOT_19 <= 180000):
        Unknown21003(0, 3000)
    GFX_0('MagneticStorm', 0)
    GFX_0('MagneticStorm', 1)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 0)
    GFX_0('StayMagneticA432', 1)
    GFX_0('StayMagneticA432', 0)
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    sprite('tg450_01', 2)	# 66-67
    SFX_0('014_electric_m')
    SFX_0('014_electric_l')
    loopRest()
    setInvincible(0)
    gotoLabel(0)
    label(1)
    sprite('tg450_01', 6)	# 68-73
    clearUponHandler(17)
    clearUponHandler(3)
    sprite('tg450_02', 4)	# 74-77
    Unknown21003(0, 0)
    sprite('tg450_03', 4)	# 78-81	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    SFX_0('006_swing_blade_0')
    sprite('tg450_24', 4)	# 82-85
    setInvincible(0)
    Unknown23024(0)
    Unknown3026(-1)
    Unknown3025(-8355712, 4)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_25', 4)	# 86-89
    SFX_3('tgse_08')
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_26', 4)	# 90-93
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_27', 4)	# 94-97
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_28', 4)	# 98-101
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_25', 4)	# 102-105
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    SFX_3('tgse_08')
    sprite('tg450_26', 4)	# 106-109
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_27', 4)	# 110-113
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_28', 4)	# 114-117
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_25', 4)	# 118-121
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    SFX_3('tgse_08')
    sprite('tg450_26', 4)	# 122-125
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_27', 4)	# 126-129
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_28', 4)	# 130-133
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    GFX_1('tgef_blacksmoke', 106)
    sprite('tg450_29', 6)	# 134-139
    Unknown3025(-1, 30)
    sprite('tg450_30', 6)	# 140-145
    sprite('tg450_31', 6)	# 146-151
    sprite('tg450_32', 6)	# 152-157

@State
def AstralHeat2():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(100)
        Unknown9310(52)
        Hitstop(25)
        AirPushbackX(20000)
        AirPushbackY(-60000)
        Unknown11067(1)
        Unknown2017(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20001(0)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20004(1)
        Unknown23083(1)
        Unknown23084(1)
        Unknown2004(1, 0)
        Unknown13024(0)
        Unknown11068(1)
        Unknown11091(100)
        Unknown11078(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        setInvincible(1)
        Unknown23157(1)
        Unknown23088(1, 1)
        Unknown1018()
        Unknown1023()
        Unknown1038()
        Unknown1028(0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(4)
        Unknown3076(1000)
        Unknown3077(1050)
    sprite('tg450_03', 60)	# 1-60	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    GFX_1('tgef_asthandthrow', 1)
    GFX_1('tgef_astcatchlight', 1)
    GFX_0('LookAtPos', -1)
    SFX_3('tgse_00')
    SFX_3('tgse_08')
    sprite('tg450_04', 6)	# 61-66
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    SFX_0('019_cloth_a')
    SFX_0('005_swing_grap_2_2')
    SFX_0('006_swing_blade_0')
    sprite('tg450_05', 5)	# 67-71
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    Unknown2018(0, 80)
    sprite('tg450_06', 5)	# 72-76
    Unknown5000(14, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_07', 6)	# 77-82
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_08', 6)	# 83-88
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_09', 90)	# 89-178
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    ScreenShake(0, 16000)
    GFX_1('tgef_astsparks', -1)
    Unknown3026(-8355712)
    Unknown3025(-65536, 30)
    Unknown3071(6)
    Unknown3074('000000000000000000000000ff000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3076(1000)
    Unknown3077(1100)
    SFX_3('tgse_03')
    SFX_0('016_explode_1')
    SFX_0('019_quake_1')
    sprite('tg450_07', 5)	# 179-183
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    ScreenShake(0, 32000)
    GFX_1('tgef_astsparks', -1)
    Unknown3026(-8355712)
    Unknown3025(-49088, 30)
    Unknown3071(8)
    Unknown3074('00000000800000000000000080000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3076(1000)
    Unknown3077(1300)
    SFX_3('tgse_03')
    SFX_0('016_explode_1')
    SFX_0('019_quake_1')
    sprite('tg450_08', 5)	# 184-188
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_09', 65)	# 189-253
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_07', 5)	# 254-258
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    ScreenShake(0, 128000)
    GFX_1('tgef_astsparks', -1)
    Unknown3026(-8355712)
    Unknown3025(-32640, 30)
    Unknown3071(10)
    Unknown3074('00000000ff0000000000000000000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3076(1000)
    Unknown3077(1500)
    SFX_3('tgse_03')
    SFX_3('tgse_04')
    SFX_0('016_explode_1')
    SFX_0('019_quake_1')
    sprite('tg450_08', 5)	# 259-263
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_09', 45)	# 264-308
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_10', 30)	# 309-338
    SFX_3('tgse_22')
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    Unknown1007(256000)
    physicsYImpulse(128000)
    GFX_0('AstJumpExpl', -1)
    SFX_0('002_highjump_2')
    SFX_0('001_airbackdash_0')
    SFX_0('015_blaze_2')
    SFX_0('016_explode_1')
    SFX_0('016_explode_2')
    SFX_0('019_quake_1')
    sprite('null', 20)	# 339-358
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000020000000')
    Unknown3029(0)
    Unknown2005()
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('tg450_10', 130)	# 359-488
    Unknown23088(1, 1)
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000010000000')
    physicsYImpulse(0)
    setGravity(-2800)
    Unknown2018(1, 80)
    Unknown20005(130, 30)
    GFX_0('TG_AST_A', -1)
    GFX_0('TG_AST_B', -1)
    GFX_0('AstWhiteOut', -1)
    Unknown23024(3)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    SFX_0('002_highjump_2')
    SFX_0('000_airdash_2')
    sprite('null', 40)	# 489-528
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000020000000')
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown1000(0)
    teleportRelativeY(41900000)
    Unknown1084(1)
    setGravity(0)
    sprite('tg450_11', 100)	# 529-628
    Unknown5001('0000000001000000010000000000000020000000')
    setGravity(50)
    Unknown20005(100, 200)
    Unknown20001(1)
    Unknown23117(16776960, 50)
    Unknown3029(0)
    GFX_0('AstLight', 2)
    GFX_0('AstBackLight', 2)
    GFX_0('TG_AST_D', 2)
    SFX_0('015_blaze_1')
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    tag_voice(0, 'btg291_0', 'btg291_1', '', '')
    sprite('tg450_11', 2)	# 629-630
    SFX_3('tgse_23')
    Unknown5000(14, 0)
    Unknown5001('0000000001000000010000000000000010000000')
    Unknown1084(1)
    setGravity(2500)
    Unknown20005(180, 20)
    GFX_0('TG_AST_C', -1)
    GFX_0('TG_AST_E', -1)
    SFX_3('tgse_00')
    SFX_3('tgse_01')
    SFX_3('tgse_07')
    tag_voice(0, 'btg292_0', 'btg292_1', '', '')
    sprite('tg450_11', 3)	# 631-633
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    SFX_0('019_quake_0')
    SFX_3('tgse_00')
    SFX_3('tgse_01')
    sprite('tg450_12', 3)	# 634-636
    Unknown5000(14, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    sprite('tg450_13', 3)	# 637-639
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_14', 3)	# 640-642
    Unknown5000(14, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    sprite('tg450_11', 3)	# 643-645
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    SFX_0('019_quake_0')
    SFX_3('tgse_00')
    SFX_3('tgse_01')
    sprite('tg450_12', 3)	# 646-648
    Unknown5000(14, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    sprite('tg450_13', 3)	# 649-651
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('tg450_14', 3)	# 652-654
    Unknown5000(14, 0)
    Unknown5001('0000000001000000010000000000000008000000')
    label(0)
    sprite('tg450_11', 3)	# 655-657
    Unknown5000(15, 0)
    Unknown5001('0100000001000000010000000000000001000000')
    SFX_0('019_quake_0')
    SFX_3('tgse_00')
    SFX_3('tgse_01')
    sprite('tg450_12', 3)	# 658-660
    Unknown5000(14, 0)
    Unknown5001('0100000001000000010000000000000008000000')
    sprite('tg450_13', 3)	# 661-663
    Unknown5000(15, 0)
    Unknown5001('0100000001000000010000000000000001000000')
    sprite('tg450_14', 3)	# 664-666
    Unknown5000(14, 0)
    Unknown5001('0100000001000000010000000000000008000000')
    loopRest()
    gotoLabel(0)
    sprite('tg450_11ex01', 1)	# 667-667	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0100000001000000010000000000000020000000')
    StartMultihit()
    Unknown1084(1)
    Unknown20001(0)
    Unknown2005()
    teleportRelativeY(0)
    label(1)
    sprite('tg450_11ex01', 80)	# 668-747	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0100000001000000010000000000000020000000')
    Unknown11064(3)
    Unknown11023(1)
    AttackLevel_(4)
    Damage(22400)
    AirPushbackX(0)
    AirPushbackY(1024000)
    YImpluseBeforeWallbounce(-5000)
    Unknown11072(1, 0, 3072000)
    RefreshMultihit()
    SLOT_61 = 1
    Unknown23118(0)
    Unknown3026(-16777216)
    Unknown3025(-12574720, 30)
    GFX_0('TG_AST_F', -1)
    GFX_0('TG_AST_G', -1)
    GFX_0('TG_AST_H', -1)
    ScreenShake(108000, 108000)
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    SFX_3('tgse_24')
    SFX_3('tgse_25')
    sprite('tg450_15', 20)	# 748-767
    Unknown3029(1)
    Unknown3069(1)
    Unknown3071(10)
    Unknown3076(1000)
    Unknown3077(1100)
    Unknown18010()
    Unknown21011(200)
    GFX_0('TG_AST_I', -1)
    SFX_0('019_quake_0')
    sprite('tg450_15', 20)	# 768-787
    SFX_0('019_quake_0')
    sprite('tg450_15', 20)	# 788-807
    SFX_0('019_quake_0')
    sprite('tg450_16', 10)	# 808-817
    sprite('tg450_17', 10)	# 818-827
    SFX_0('019_quake_0')
    sprite('tg450_18', 20)	# 828-847
    Unknown7007('6274673532300000000000000000000064000000627467353231000000000000000000000000000062746735323200000000000000000000640000006274673532330000000000000000000064000000')
    SFX_0('019_quake_0')
    Unknown23018(1)
    sprite('tg450_18', 20)	# 848-867
    SFX_0('019_quake_0')
    label(2)
    sprite('tg450_18', 20)	# 868-887
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(2)

@Subroutine
def MouthTableInit():
    Unknown18011('btg000', 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg500', 12643, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg501', 12643, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg502', 12643, 13363, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg503', 12643, 13362, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg504', 12643, 12338, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg505', 12643, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg520', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg521', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg522', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg523', 12643, 24889, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg524', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg403_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg403_1', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg601bha', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg600bmk', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg602bmk', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg601pag', 12643, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg601pak', 12643, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg600pka', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg601ryn', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg600ugo1', 12643, 14177, 14179, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg600ugo2', 12643, 14177, 14179, 12897, 25392, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg601uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 12849, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg600uwa', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg701bha', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg701bmk', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg700pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg700pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg700pka', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg701ryn', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg701ugo', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg701uhy', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('btg701uwa', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pag')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(180)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('tg600_00', 1)	# 2-2
    Unknown3038(1)
    teleportRelativeY(400000)
    setGravity(0)
    sprite('tg600_00', 2)	# 3-4
    sendToLabelUpon(2, 1)
    Unknown3038(0)
    physicsYImpulse(-40000)
    sprite('tg600_00', 6)	# 5-10
    sprite('tg600_01', 6)	# 11-16
    sprite('tg600_02', 6)	# 17-22
    label(1)
    sprite('tg600_03', 20)	# 23-42
    Unknown21007(24, 41)
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    Unknown1043()
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_0('ShockB', 0)
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('213_bound_1')
    Unknown1084(1)
    loopRest()
    sprite('tg600_03', 20)	# 43-62
    sprite('tg600_03', 140)	# 63-202
    Unknown7006('btg500', 100, 895972450, 12592, 0, 0, 100, 895972450, 13360, 0, 0, 100, 895972450, 13616, 0, 0, 100)
    sprite('tg600_04', 6)	# 203-208
    sprite('tg600_05', 6)	# 209-214
    sprite('tg600_06', 6)	# 215-220
    sprite('tg600_07', 6)	# 221-226
    sprite('tg600_08', 6)	# 227-232
    sprite('tg600_09', 6)	# 233-238
    sprite('tg600_10', 6)	# 239-244
    sprite('tg600_11', 6)	# 245-250
    Unknown23018(1)
    label(2)
    sprite('tg000_00', 6)	# 251-256
    sprite('tg000_01', 6)	# 257-262
    sprite('tg000_02', 6)	# 263-268
    sprite('tg000_03', 6)	# 269-274
    sprite('tg000_04', 6)	# 275-280
    sprite('tg000_05', 6)	# 281-286
    sprite('tg000_06', 6)	# 287-292
    sprite('tg000_05', 6)	# 293-298
    sprite('tg000_04', 6)	# 299-304
    sprite('tg000_03', 6)	# 305-310
    sprite('tg000_02', 6)	# 311-316
    sprite('tg000_01', 6)	# 317-322
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('tg601_00', 2)	# 323-324
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 325-326
    Unknown7006('btg502', 100, 895972450, 13104, 0, 0, 100, 895972450, 13360, 0, 0, 100, 895972450, 13616, 0, 0, 100)
    sprite('tg601_00', 2)	# 327-328
    sprite('tg601_01', 2)	# 329-330
    sprite('tg601_00', 2)	# 331-332
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 333-334
    sprite('tg601_00', 2)	# 335-336
    sprite('tg601_01', 2)	# 337-338
    sprite('tg601_00', 2)	# 339-340
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 341-342
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 343-344
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 345-346
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 347-348
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 349-350
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 351-352
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 353-354
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 355-356
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 357-358
    SFX_1('tg416')
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 359-360
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 361-362
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 363-364
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 365-366
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 367-368
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 369-370
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 371-372
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 373-374
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 375-376
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 377-378
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 379-380
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 381-382
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 383-384
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 385-386
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 387-388
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 389-390
    SFX_3('tgse_08')
    SFX_0('014_electric_l')
    ScreenShake(0, 5000)
    GFX_0('tgef_appB', 0)
    sprite('tg601_02', 6)	# 391-396
    SFX_0('014_electric_s')
    sprite('tg601_03', 6)	# 397-402
    SFX_0('014_electric_s')
    sprite('tg601_04', 6)	# 403-408
    Unknown21007(24, 41)
    sprite('tg601_05', 6)	# 409-414
    sprite('tg601_06', 6)	# 415-420
    sprite('tg601_07', 6)	# 421-426
    sprite('tg601_08', 6)	# 427-432
    sprite('tg601_09', 6)	# 433-438
    Unknown23018(1)
    label(11)
    sprite('tg000_00', 6)	# 439-444
    sprite('tg000_01', 6)	# 445-450
    sprite('tg000_02', 6)	# 451-456
    sprite('tg000_03', 6)	# 457-462
    sprite('tg000_04', 6)	# 463-468
    sprite('tg000_05', 6)	# 469-474
    sprite('tg000_06', 6)	# 475-480
    sprite('tg000_05', 6)	# 481-486
    sprite('tg000_04', 6)	# 487-492
    sprite('tg000_03', 6)	# 493-498
    sprite('tg000_02', 6)	# 499-504
    sprite('tg000_01', 6)	# 505-510
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('tg000_00', 1)	# 511-511
    SFX_1('btg701ryn')
    label(21)
    sprite('tg000_00', 6)	# 512-517
    sprite('tg000_01', 6)	# 518-523
    sprite('tg000_02', 6)	# 524-529
    sprite('tg000_03', 6)	# 530-535
    sprite('tg000_04', 6)	# 536-541
    sprite('tg000_05', 6)	# 542-547
    sprite('tg000_06', 6)	# 548-553
    sprite('tg000_05', 6)	# 554-559
    sprite('tg000_04', 6)	# 560-565
    sprite('tg000_03', 6)	# 566-571
    sprite('tg000_02', 6)	# 572-577
    sprite('tg000_01', 6)	# 578-583
    gotoLabel(21)
    label(100)
    sprite('tg000_00', 1)	# 584-584
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1515000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('tg000_00', 6)	# 585-590
    sprite('tg000_01', 6)	# 591-596
    sprite('tg000_02', 6)	# 597-602
    sprite('tg000_03', 6)	# 603-608
    sprite('tg000_04', 6)	# 609-614
    sprite('tg000_05', 6)	# 615-620
    sprite('tg000_06', 6)	# 621-626
    sprite('tg000_05', 6)	# 627-632
    sprite('tg000_04', 6)	# 633-638
    sprite('tg000_03', 6)	# 639-644
    sprite('tg000_02', 6)	# 645-650
    sprite('tg000_01', 6)	# 651-656
    gotoLabel(101)
    label(102)
    sprite('tg300_00', 8)	# 657-664
    SFX_1('btg601bha')
    sprite('tg300_01', 8)	# 665-672
    sprite('tg300_02', 10)	# 673-682
    sprite('tg300_03', 10)	# 683-692
    sprite('tg300_04', 10)	# 693-702
    sprite('tg300_02', 10)	# 703-712
    sprite('tg300_03', 10)	# 713-722
    label(103)
    sprite('tg300_04', 1)	# 723-723
    if SLOT_97:
        _gotolabel(103)
    sprite('tg300_04', 30)	# 724-753
    sprite('tg300_05', 10)	# 754-763
    sprite('tg300_06', 10)	# 764-773
    Unknown23018(1)
    label(104)
    sprite('tg000_00', 6)	# 774-779
    sprite('tg000_01', 6)	# 780-785
    sprite('tg000_02', 6)	# 786-791
    sprite('tg000_03', 6)	# 792-797
    sprite('tg000_04', 6)	# 798-803
    sprite('tg000_05', 6)	# 804-809
    sprite('tg000_06', 6)	# 810-815
    sprite('tg000_05', 6)	# 816-821
    sprite('tg000_04', 6)	# 822-827
    sprite('tg000_03', 6)	# 828-833
    sprite('tg000_02', 6)	# 834-839
    sprite('tg000_01', 6)	# 840-845
    gotoLabel(104)
    ExitState()
    label(110)
    sprite('tg000_00', 1)	# 846-846
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('tg000_00', 6)	# 847-852
    sprite('tg000_01', 6)	# 853-858
    sprite('tg000_02', 6)	# 859-864
    sprite('tg000_03', 6)	# 865-870
    sprite('tg000_04', 6)	# 871-876
    sprite('tg000_05', 6)	# 877-882
    sprite('tg000_06', 6)	# 883-888
    sprite('tg000_05', 6)	# 889-894
    sprite('tg000_04', 6)	# 895-900
    sprite('tg000_03', 6)	# 901-906
    sprite('tg000_02', 6)	# 907-912
    sprite('tg000_01', 6)	# 913-918
    gotoLabel(111)
    label(112)
    sprite('tg300_00', 8)	# 919-926
    SFX_1('btg601uhy')
    sprite('tg300_01', 8)	# 927-934
    sprite('tg300_02', 10)	# 935-944
    sprite('tg300_03', 10)	# 945-954
    sprite('tg300_04', 10)	# 955-964
    sprite('tg300_02', 10)	# 965-974
    sprite('tg300_03', 10)	# 975-984
    label(113)
    sprite('tg300_04', 1)	# 985-985
    if SLOT_97:
        _gotolabel(113)
    sprite('tg300_04', 30)	# 986-1015
    sprite('tg300_05', 10)	# 1016-1025
    sprite('tg300_06', 10)	# 1026-1035
    Unknown23018(1)
    label(114)
    sprite('tg000_00', 6)	# 1036-1041
    sprite('tg000_01', 6)	# 1042-1047
    sprite('tg000_02', 6)	# 1048-1053
    sprite('tg000_03', 6)	# 1054-1059
    sprite('tg000_04', 6)	# 1060-1065
    sprite('tg000_05', 6)	# 1066-1071
    sprite('tg000_06', 6)	# 1072-1077
    sprite('tg000_05', 6)	# 1078-1083
    sprite('tg000_04', 6)	# 1084-1089
    sprite('tg000_03', 6)	# 1090-1095
    sprite('tg000_02', 6)	# 1096-1101
    sprite('tg000_01', 6)	# 1102-1107
    gotoLabel(114)
    ExitState()
    label(120)
    sprite('tg000_00', 6)	# 1108-1113
    if SLOT_158:
        Unknown1000(-1210000)
    else:
        Unknown1000(-1525000)
    sprite('tg000_01', 6)	# 1114-1119
    SFX_1('btg600uwa')
    sprite('tg000_02', 6)	# 1120-1125
    sprite('tg000_03', 6)	# 1126-1131
    sprite('tg000_04', 6)	# 1132-1137
    sprite('tg000_05', 6)	# 1138-1143
    sprite('tg000_06', 6)	# 1144-1149
    sprite('tg000_05', 6)	# 1150-1155
    sprite('tg000_04', 6)	# 1156-1161
    sprite('tg000_03', 6)	# 1162-1167
    sprite('tg000_02', 6)	# 1168-1173
    sprite('tg000_01', 6)	# 1174-1179
    sprite('tg001_00', 6)	# 1180-1185
    sprite('tg001_01', 6)	# 1186-1191
    sprite('tg001_02', 6)	# 1192-1197
    sprite('tg001_03', 8)	# 1198-1205
    SFX_3('tgse_00')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000000000000')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000001000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000002000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000003000000')
    sprite('tg001_04', 8)	# 1206-1213
    sprite('tg001_05', 8)	# 1214-1221
    sprite('tg001_06', 8)	# 1222-1229
    sprite('tg001_07', 8)	# 1230-1237
    sprite('tg001_08', 8)	# 1238-1245
    sprite('tg000_00', 6)	# 1246-1251
    sprite('tg300_00', 8)	# 1252-1259
    sprite('tg300_01', 8)	# 1260-1267
    sprite('tg300_02', 10)	# 1268-1277
    sprite('tg300_03', 10)	# 1278-1287
    sprite('tg300_04', 10)	# 1288-1297
    sprite('tg300_02', 10)	# 1298-1307
    sprite('tg300_03', 10)	# 1308-1317
    label(121)
    sprite('tg300_04', 1)	# 1318-1318
    if SLOT_97:
        _gotolabel(121)
    sprite('tg300_04', 30)	# 1319-1348
    sprite('tg300_05', 10)	# 1349-1358
    Unknown21007(24, 40)
    sprite('tg300_06', 10)	# 1359-1368
    sprite('tg000_00', 1)	# 1369-1369
    Unknown21011(180)
    label(122)
    sprite('tg000_00', 6)	# 1370-1375
    sprite('tg000_01', 6)	# 1376-1381
    sprite('tg000_02', 6)	# 1382-1387
    sprite('tg000_03', 6)	# 1388-1393
    sprite('tg000_04', 6)	# 1394-1399
    sprite('tg000_05', 6)	# 1400-1405
    sprite('tg000_06', 6)	# 1406-1411
    sprite('tg000_05', 6)	# 1412-1417
    sprite('tg000_04', 6)	# 1418-1423
    sprite('tg000_03', 6)	# 1424-1429
    sprite('tg000_02', 6)	# 1430-1435
    sprite('tg000_01', 6)	# 1436-1441
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('tg000_00', 6)	# 1442-1447
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-100)
    else:
        Unknown1000(-1465000)
        Unknown2019(1000)
    sprite('tg000_01', 6)	# 1448-1453
    Unknown7006('btg600ugo2', 100, 912749666, 1735733296, 12655, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('tg000_02', 6)	# 1454-1459
    sprite('tg000_03', 6)	# 1460-1465
    sprite('tg000_04', 6)	# 1466-1471
    sprite('tg000_05', 6)	# 1472-1477
    sprite('tg000_06', 6)	# 1478-1483
    sprite('tg000_05', 6)	# 1484-1489
    sprite('tg000_04', 6)	# 1490-1495
    sprite('tg000_03', 6)	# 1496-1501
    sprite('tg000_02', 6)	# 1502-1507
    sprite('tg000_01', 6)	# 1508-1513
    sprite('tg001_00', 6)	# 1514-1519
    sprite('tg001_01', 6)	# 1520-1525
    sprite('tg001_02', 6)	# 1526-1531
    sprite('tg001_03', 8)	# 1532-1539
    SFX_3('tgse_00')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000000000000')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000001000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000002000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000003000000')
    sprite('tg001_04', 8)	# 1540-1547
    sprite('tg001_05', 8)	# 1548-1555
    sprite('tg001_06', 8)	# 1556-1563
    sprite('tg001_07', 8)	# 1564-1571
    sprite('tg001_08', 8)	# 1572-1579
    sprite('tg000_00', 6)	# 1580-1585
    sprite('tg300_00', 8)	# 1586-1593
    sprite('tg300_01', 8)	# 1594-1601
    sprite('tg300_02', 10)	# 1602-1611
    sprite('tg300_03', 10)	# 1612-1621
    sprite('tg300_04', 10)	# 1622-1631
    sprite('tg300_02', 10)	# 1632-1641
    sprite('tg300_03', 10)	# 1642-1651
    label(131)
    sprite('tg300_04', 1)	# 1652-1652
    if SLOT_97:
        _gotolabel(131)
    sprite('tg300_04', 30)	# 1653-1682
    sprite('tg300_05', 10)	# 1683-1692
    Unknown21007(24, 40)
    sprite('tg300_06', 10)	# 1693-1702
    sprite('tg000_00', 1)	# 1703-1703
    Unknown21011(120)
    label(132)
    sprite('tg000_00', 6)	# 1704-1709
    sprite('tg000_01', 6)	# 1710-1715
    sprite('tg000_02', 6)	# 1716-1721
    sprite('tg000_03', 6)	# 1722-1727
    sprite('tg000_04', 6)	# 1728-1733
    sprite('tg000_05', 6)	# 1734-1739
    sprite('tg000_06', 6)	# 1740-1745
    sprite('tg000_05', 6)	# 1746-1751
    sprite('tg000_04', 6)	# 1752-1757
    sprite('tg000_03', 6)	# 1758-1763
    sprite('tg000_02', 6)	# 1764-1769
    sprite('tg000_01', 6)	# 1770-1775
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('tg300_00', 8)	# 1776-1783
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('btg600bmk')
    sprite('tg300_01', 8)	# 1784-1791
    sprite('tg300_02', 10)	# 1792-1801
    sprite('tg300_03', 10)	# 1802-1811
    sprite('tg300_04', 10)	# 1812-1821
    sprite('tg300_02', 10)	# 1822-1831
    sprite('tg300_03', 10)	# 1832-1841
    sprite('tg300_04', 120)	# 1842-1961
    sprite('tg300_05', 10)	# 1962-1971
    sprite('tg300_06', 10)	# 1972-1981
    Unknown21007(24, 40)
    sprite('tg000_00', 1)	# 1982-1982

    def upon_40():
        clearUponHandler(40)
        SFX_1('btg602bmk')
        Unknown21011(120)
    label(141)
    sprite('tg000_00', 6)	# 1983-1988
    sprite('tg000_01', 6)	# 1989-1994
    sprite('tg000_02', 6)	# 1995-2000
    sprite('tg000_03', 6)	# 2001-2006
    sprite('tg000_04', 6)	# 2007-2012
    sprite('tg000_05', 6)	# 2013-2018
    sprite('tg000_06', 6)	# 2019-2024
    sprite('tg000_05', 6)	# 2025-2030
    sprite('tg000_04', 6)	# 2031-2036
    sprite('tg000_03', 6)	# 2037-2042
    sprite('tg000_02', 6)	# 2043-2048
    sprite('tg000_01', 6)	# 2049-2054
    gotoLabel(141)
    ExitState()
    label(150)
    sprite('tg000_00', 6)	# 2055-2060
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('tg000_01', 6)	# 2061-2066
    sprite('tg000_02', 6)	# 2067-2072
    sprite('tg000_03', 6)	# 2073-2078
    sprite('tg000_04', 6)	# 2079-2084
    sprite('tg000_05', 6)	# 2085-2090
    sprite('tg000_06', 6)	# 2091-2096
    sprite('tg000_05', 6)	# 2097-2102
    sprite('tg000_04', 6)	# 2103-2108
    sprite('tg000_03', 6)	# 2109-2114
    sprite('tg000_02', 6)	# 2115-2120
    sprite('tg000_01', 6)	# 2121-2126
    sprite('tg300_01', 8)	# 2127-2134
    SFX_1('btg600pka')
    sprite('tg300_02', 10)	# 2135-2144
    sprite('tg300_03', 10)	# 2145-2154
    sprite('tg300_04', 10)	# 2155-2164
    sprite('tg300_02', 10)	# 2165-2174
    sprite('tg300_03', 10)	# 2175-2184
    label(151)
    sprite('tg300_04', 1)	# 2185-2185
    if SLOT_97:
        _gotolabel(151)
    sprite('tg300_04', 30)	# 2186-2215
    sprite('tg300_05', 10)	# 2216-2225
    sprite('tg300_06', 10)	# 2226-2235
    Unknown21007(24, 40)
    sprite('tg000_00', 1)	# 2236-2236
    Unknown21011(120)
    label(152)
    sprite('tg000_00', 6)	# 2237-2242
    sprite('tg000_01', 6)	# 2243-2248
    sprite('tg000_02', 6)	# 2249-2254
    sprite('tg000_03', 6)	# 2255-2260
    sprite('tg000_04', 6)	# 2261-2266
    sprite('tg000_05', 6)	# 2267-2272
    sprite('tg000_06', 6)	# 2273-2278
    sprite('tg000_05', 6)	# 2279-2284
    sprite('tg000_04', 6)	# 2285-2290
    sprite('tg000_03', 6)	# 2291-2296
    sprite('tg000_02', 6)	# 2297-2302
    sprite('tg000_01', 6)	# 2303-2308
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('tg600_00', 32767)	# 2309-35075
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(161)
    Unknown3038(1)
    teleportRelativeY(400000)
    setGravity(0)
    label(161)
    sprite('tg600_00', 2)	# 35076-35077
    sendToLabelUpon(2, 162)
    Unknown3038(0)
    physicsYImpulse(-40000)
    sprite('tg600_00', 6)	# 35078-35083
    sprite('tg600_01', 6)	# 35084-35089
    sprite('tg600_02', 6)	# 35090-35095
    label(162)
    sprite('tg600_03', 20)	# 35096-35115
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    Unknown1043()
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_0('ShockB', 0)
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('213_bound_1')
    Unknown1084(1)
    loopRest()
    sprite('tg600_03', 20)	# 35116-35135
    sprite('tg600_03', 70)	# 35136-35205
    SFX_1('btg601pag')
    sprite('tg600_04', 6)	# 35206-35211
    sprite('tg600_05', 6)	# 35212-35217
    sprite('tg600_06', 6)	# 35218-35223
    sprite('tg600_07', 6)	# 35224-35229
    sprite('tg600_08', 6)	# 35230-35235
    sprite('tg600_09', 6)	# 35236-35241
    sprite('tg600_10', 6)	# 35242-35247
    sprite('tg600_11', 6)	# 35248-35253
    Unknown21011(120)
    label(163)
    sprite('tg000_00', 6)	# 35254-35259
    sprite('tg000_01', 6)	# 35260-35265
    sprite('tg000_02', 6)	# 35266-35271
    sprite('tg000_03', 6)	# 35272-35277
    sprite('tg000_04', 6)	# 35278-35283
    sprite('tg000_05', 6)	# 35284-35289
    sprite('tg000_06', 6)	# 35290-35295
    sprite('tg000_05', 6)	# 35296-35301
    sprite('tg000_04', 6)	# 35302-35307
    sprite('tg000_03', 6)	# 35308-35313
    sprite('tg000_02', 6)	# 35314-35319
    sprite('tg000_01', 6)	# 35320-35325
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('tg000_00', 1)	# 35326-35326
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('tg000_00', 6)	# 35327-35332
    sprite('tg000_01', 6)	# 35333-35338
    sprite('tg000_02', 6)	# 35339-35344
    sprite('tg000_03', 6)	# 35345-35350
    sprite('tg000_04', 6)	# 35351-35356
    sprite('tg000_05', 6)	# 35357-35362
    sprite('tg000_06', 6)	# 35363-35368
    sprite('tg000_05', 6)	# 35369-35374
    sprite('tg000_04', 6)	# 35375-35380
    sprite('tg000_03', 6)	# 35381-35386
    sprite('tg000_02', 6)	# 35387-35392
    sprite('tg000_01', 6)	# 35393-35398
    gotoLabel(171)
    label(172)
    sprite('tg300_00', 8)	# 35399-35406
    SFX_1('btg601ryn')
    sprite('tg300_01', 8)	# 35407-35414
    sprite('tg300_02', 10)	# 35415-35424
    sprite('tg300_03', 10)	# 35425-35434
    sprite('tg300_04', 10)	# 35435-35444
    sprite('tg300_02', 10)	# 35445-35454
    sprite('tg300_03', 10)	# 35455-35464
    label(173)
    sprite('tg300_04', 1)	# 35465-35465
    if SLOT_97:
        _gotolabel(173)
    sprite('tg300_04', 30)	# 35466-35495
    sprite('tg300_05', 10)	# 35496-35505
    sprite('tg300_06', 10)	# 35506-35515
    Unknown23018(1)
    label(174)
    sprite('tg000_00', 6)	# 35516-35521
    sprite('tg000_01', 6)	# 35522-35527
    sprite('tg000_02', 6)	# 35528-35533
    sprite('tg000_03', 6)	# 35534-35539
    sprite('tg000_04', 6)	# 35540-35545
    sprite('tg000_05', 6)	# 35546-35551
    sprite('tg000_06', 6)	# 35552-35557
    sprite('tg000_05', 6)	# 35558-35563
    sprite('tg000_04', 6)	# 35564-35569
    sprite('tg000_03', 6)	# 35570-35575
    sprite('tg000_02', 6)	# 35576-35581
    sprite('tg000_01', 6)	# 35582-35587
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('tg000_00', 1)	# 35588-35588
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('tg000_00', 6)	# 35589-35594
    sprite('tg000_01', 6)	# 35595-35600
    sprite('tg000_02', 6)	# 35601-35606
    sprite('tg000_03', 6)	# 35607-35612
    sprite('tg000_04', 6)	# 35613-35618
    sprite('tg000_05', 6)	# 35619-35624
    sprite('tg000_06', 6)	# 35625-35630
    sprite('tg000_05', 6)	# 35631-35636
    sprite('tg000_04', 6)	# 35637-35642
    sprite('tg000_03', 6)	# 35643-35648
    sprite('tg000_02', 6)	# 35649-35654
    sprite('tg000_01', 6)	# 35655-35660
    gotoLabel(181)
    label(182)
    sprite('tg300_00', 8)	# 35661-35668
    SFX_1('btg601pak')
    sprite('tg300_01', 8)	# 35669-35676
    sprite('tg300_02', 10)	# 35677-35686
    sprite('tg300_03', 10)	# 35687-35696
    sprite('tg300_04', 10)	# 35697-35706
    sprite('tg300_02', 10)	# 35707-35716
    sprite('tg300_03', 10)	# 35717-35726
    label(183)
    sprite('tg300_04', 1)	# 35727-35727
    if SLOT_97:
        _gotolabel(183)
    sprite('tg300_04', 30)	# 35728-35757
    sprite('tg300_05', 10)	# 35758-35767
    sprite('tg300_06', 10)	# 35768-35777
    Unknown23018(1)
    label(184)
    sprite('tg000_00', 6)	# 35778-35783
    sprite('tg000_01', 6)	# 35784-35789
    sprite('tg000_02', 6)	# 35790-35795
    sprite('tg000_03', 6)	# 35796-35801
    sprite('tg000_04', 6)	# 35802-35807
    sprite('tg000_05', 6)	# 35808-35813
    sprite('tg000_06', 6)	# 35814-35819
    sprite('tg000_05', 6)	# 35820-35825
    sprite('tg000_04', 6)	# 35826-35831
    sprite('tg000_03', 6)	# 35832-35837
    sprite('tg000_02', 6)	# 35838-35843
    sprite('tg000_01', 6)	# 35844-35849
    gotoLabel(184)
    ExitState()
    label(991)
    sprite('tg000_00', 1)	# 35850-35850
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('tg000_00', 6)	# 35851-35856
    sprite('tg000_01', 6)	# 35857-35862
    sprite('tg000_02', 6)	# 35863-35868
    sprite('tg000_03', 6)	# 35869-35874
    sprite('tg000_04', 6)	# 35875-35880
    sprite('tg000_05', 6)	# 35881-35886
    sprite('tg000_06', 6)	# 35887-35892
    sprite('tg000_05', 6)	# 35893-35898
    sprite('tg000_04', 6)	# 35899-35904
    sprite('tg000_03', 6)	# 35905-35910
    sprite('tg000_02', 6)	# 35911-35916
    sprite('tg000_01', 6)	# 35917-35922
    gotoLabel(992)
    label(993)
    sprite('tg033_00', 2)	# 35923-35924

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
    sprite('tg033_01', 2)	# 35925-35926
    label(994)
    sprite('tg033_02', 3)	# 35927-35929
    sprite('tg033_01', 3)	# 35930-35932
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 35933-35935
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
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('tg610_00', 4)	# 4-7
    sprite('tg610_01', 8)	# 8-15
    sprite('tg610_02', 4)	# 16-19
    sprite('tg610_03', 4)	# 20-23
    sprite('tg610_04', 10)	# 24-33
    if SLOT_158:
        if SLOT_52:
            Unknown7006('btg524', 100, 895972450, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('btg402_0', 100, 879195234, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('btg522', 100, 895972450, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('tg610_05', 3)	# 34-36
    sprite('tg610_06', 3)	# 37-39
    sprite('tg610_07', 3)	# 40-42
    sprite('tg610_08', 3)	# 43-45
    SFX_3('tgse_03')
    Unknown23018(1)
    Unknown51(1)
    loopRest()
    ExitState()
    label(10)
    sprite('tg300_00', 8)	# 46-53
    if SLOT_158:
        if SLOT_52:
            Unknown7006('btg524', 100, 895972450, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('btg402_0', 100, 879195234, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('btg520', 100, 895972450, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('tg300_01', 8)	# 54-61
    sprite('tg300_02', 10)	# 62-71
    sprite('tg300_03', 10)	# 72-81
    sprite('tg300_04', 10)	# 82-91
    sprite('tg300_02', 10)	# 92-101
    sprite('tg300_03', 10)	# 102-111
    Unknown23018(1)
    sprite('tg300_04', 32767)	# 112-32878
    label(100)
    sprite('tg000_00', 1)	# 32879-32879
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('tg000_00', 6)	# 32880-32885
    sprite('tg000_01', 6)	# 32886-32891
    sprite('tg000_02', 6)	# 32892-32897
    sprite('tg000_03', 6)	# 32898-32903
    sprite('tg000_04', 6)	# 32904-32909
    sprite('tg000_05', 6)	# 32910-32915
    sprite('tg000_06', 6)	# 32916-32921
    sprite('tg000_05', 6)	# 32922-32927
    sprite('tg000_04', 6)	# 32928-32933
    sprite('tg000_03', 6)	# 32934-32939
    sprite('tg000_02', 6)	# 32940-32945
    sprite('tg000_01', 6)	# 32946-32951
    gotoLabel(101)
    label(102)
    sprite('tg610_00', 4)	# 32952-32955
    sprite('tg610_01', 8)	# 32956-32963
    sprite('tg610_02', 4)	# 32964-32967
    sprite('tg610_03', 4)	# 32968-32971
    sprite('tg610_04', 10)	# 32972-32981
    SFX_1('btg701bha')
    sprite('tg610_05', 3)	# 32982-32984
    sprite('tg610_06', 3)	# 32985-32987
    sprite('tg610_07', 3)	# 32988-32990
    Unknown23018(1)
    sprite('tg610_08', 32767)	# 32991-65757
    SFX_3('tgse_03')
    loopRest()
    ExitState()
    label(110)
    sprite('tg000_00', 1)	# 65758-65758
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('tg000_00', 6)	# 65759-65764
    sprite('tg000_01', 6)	# 65765-65770
    sprite('tg000_02', 6)	# 65771-65776
    sprite('tg000_03', 6)	# 65777-65782
    sprite('tg000_04', 6)	# 65783-65788
    sprite('tg000_05', 6)	# 65789-65794
    sprite('tg000_06', 6)	# 65795-65800
    sprite('tg000_05', 6)	# 65801-65806
    sprite('tg000_04', 6)	# 65807-65812
    sprite('tg000_03', 6)	# 65813-65818
    sprite('tg000_02', 6)	# 65819-65824
    sprite('tg000_01', 6)	# 65825-65830
    gotoLabel(111)
    label(112)
    sprite('tg300_00', 8)	# 65831-65838
    SFX_1('btg701bmk')
    sprite('tg300_01', 8)	# 65839-65846
    sprite('tg300_02', 10)	# 65847-65856
    sprite('tg300_03', 10)	# 65857-65866
    sprite('tg300_04', 10)	# 65867-65876
    sprite('tg300_02', 10)	# 65877-65886
    sprite('tg300_03', 10)	# 65887-65896
    label(113)
    sprite('tg300_04', 1)	# 65897-65897
    if SLOT_97:
        _gotolabel(113)
    sprite('tg300_04', 32767)	# 65898-98664
    Unknown23018(1)
    label(120)
    sprite('tg300_00', 8)	# 98665-98672
    Unknown2019(1000)
    SFX_1('btg700pka')
    sprite('tg300_01', 8)	# 98673-98680
    sprite('tg300_02', 10)	# 98681-98690
    sprite('tg300_03', 10)	# 98691-98700
    sprite('tg300_04', 10)	# 98701-98710
    sprite('tg300_02', 10)	# 98711-98720
    sprite('tg300_03', 10)	# 98721-98730
    label(121)
    sprite('tg300_04', 1)	# 98731-98731
    if SLOT_97:
        _gotolabel(121)
    sprite('tg300_04', 15)	# 98732-98746
    sprite('tg300_04', 32767)	# 98747-131513
    Unknown21007(24, 40)
    Unknown21011(330)
    label(130)
    sprite('tg000_00', 1)	# 131514-131514
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('tg000_00', 6)	# 131515-131520
    sprite('tg000_01', 6)	# 131521-131526
    sprite('tg000_02', 6)	# 131527-131532
    sprite('tg000_03', 6)	# 131533-131538
    sprite('tg000_04', 6)	# 131539-131544
    sprite('tg000_05', 6)	# 131545-131550
    sprite('tg000_06', 6)	# 131551-131556
    sprite('tg000_05', 6)	# 131557-131562
    sprite('tg000_04', 6)	# 131563-131568
    sprite('tg000_03', 6)	# 131569-131574
    sprite('tg000_02', 6)	# 131575-131580
    sprite('tg000_01', 6)	# 131581-131586
    gotoLabel(131)
    label(132)
    sprite('tg300_00', 8)	# 131587-131594
    SFX_1('btg701uhy')
    sprite('tg300_01', 8)	# 131595-131602
    sprite('tg300_02', 10)	# 131603-131612
    sprite('tg300_03', 10)	# 131613-131622
    label(133)
    sprite('tg300_04', 1)	# 131623-131623
    if SLOT_97:
        _gotolabel(133)
    sprite('tg300_04', 30)	# 131624-131653
    Unknown23018(1)
    sprite('tg300_04', 32767)	# 131654-164420
    label(140)
    sprite('tg000_00', 1)	# 164421-164421

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('tg000_00', 6)	# 164422-164427
    sprite('tg000_01', 6)	# 164428-164433
    sprite('tg000_02', 6)	# 164434-164439
    sprite('tg000_03', 6)	# 164440-164445
    sprite('tg000_04', 6)	# 164446-164451
    sprite('tg000_05', 6)	# 164452-164457
    sprite('tg000_06', 6)	# 164458-164463
    sprite('tg000_05', 6)	# 164464-164469
    sprite('tg000_04', 6)	# 164470-164475
    sprite('tg000_03', 6)	# 164476-164481
    sprite('tg000_02', 6)	# 164482-164487
    sprite('tg000_01', 6)	# 164488-164493
    gotoLabel(141)
    label(142)
    sprite('tg300_00', 8)	# 164494-164501
    SFX_1('btg701uwa')
    sprite('tg300_01', 8)	# 164502-164509
    sprite('tg300_02', 10)	# 164510-164519
    sprite('tg300_03', 10)	# 164520-164529
    label(143)
    sprite('tg300_04', 1)	# 164530-164530
    if SLOT_97:
        _gotolabel(143)
    sprite('tg300_04', 30)	# 164531-164560
    Unknown21011(120)
    sprite('tg300_02', 10)	# 164561-164570
    sprite('tg300_03', 10)	# 164571-164580
    sprite('tg300_04', 32767)	# 164581-197347
    label(150)
    sprite('tg000_00', 1)	# 197348-197348
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('tg000_00', 6)	# 197349-197354
    sprite('tg000_01', 6)	# 197355-197360
    sprite('tg000_02', 6)	# 197361-197366
    sprite('tg000_03', 6)	# 197367-197372
    sprite('tg000_04', 6)	# 197373-197378
    sprite('tg000_05', 6)	# 197379-197384
    sprite('tg000_06', 6)	# 197385-197390
    sprite('tg000_05', 6)	# 197391-197396
    sprite('tg000_04', 6)	# 197397-197402
    sprite('tg000_03', 6)	# 197403-197408
    sprite('tg000_02', 6)	# 197409-197414
    sprite('tg000_01', 6)	# 197415-197420
    gotoLabel(151)
    label(152)
    sprite('tg300_00', 8)	# 197421-197428
    SFX_1('btg701ugo')
    sprite('tg300_01', 8)	# 197429-197436
    sprite('tg300_02', 10)	# 197437-197446
    sprite('tg300_03', 10)	# 197447-197456
    sprite('tg300_04', 10)	# 197457-197466
    sprite('tg300_02', 10)	# 197467-197476
    sprite('tg300_03', 10)	# 197477-197486
    label(153)
    sprite('tg300_04', 1)	# 197487-197487
    if SLOT_97:
        _gotolabel(153)
    sprite('tg300_04', 32767)	# 197488-230254
    Unknown23018(1)
    label(160)
    sprite('tg001_00', 8)	# 230255-230262
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(163)
    sprite('tg001_01', 8)	# 230263-230270
    SFX_1('btg700pag')
    sprite('tg001_02', 8)	# 230271-230278
    sprite('tg001_03', 8)	# 230279-230286
    SFX_3('tgse_00')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000000000000')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000001000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000002000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000003000000')
    sprite('tg001_04', 8)	# 230287-230294
    sprite('tg001_05', 8)	# 230295-230302
    sprite('tg001_06', 8)	# 230303-230310
    sprite('tg001_07', 8)	# 230311-230318
    sprite('tg001_08', 8)	# 230319-230326
    label(161)
    sprite('tg000_00', 6)	# 230327-230332
    sprite('tg000_01', 6)	# 230333-230338
    sprite('tg000_02', 6)	# 230339-230344
    sprite('tg000_03', 6)	# 230345-230350
    sprite('tg000_04', 6)	# 230351-230356
    sprite('tg000_05', 6)	# 230357-230362
    sprite('tg000_06', 6)	# 230363-230368
    sprite('tg000_05', 6)	# 230369-230374
    sprite('tg000_04', 6)	# 230375-230380
    sprite('tg000_03', 6)	# 230381-230386
    sprite('tg000_02', 6)	# 230387-230392
    sprite('tg000_01', 6)	# 230393-230398
    if SLOT_97:
        _gotolabel(161)
    sprite('tg000_00', 1)	# 230399-230399
    Unknown21007(24, 40)
    Unknown21011(200)
    label(162)
    sprite('tg000_00', 6)	# 230400-230405
    sprite('tg000_01', 6)	# 230406-230411
    sprite('tg000_02', 6)	# 230412-230417
    sprite('tg000_03', 6)	# 230418-230423
    sprite('tg000_04', 6)	# 230424-230429
    sprite('tg000_05', 6)	# 230430-230435
    sprite('tg000_06', 6)	# 230436-230441
    sprite('tg000_05', 6)	# 230442-230447
    sprite('tg000_04', 6)	# 230448-230453
    sprite('tg000_03', 6)	# 230454-230459
    sprite('tg000_02', 6)	# 230460-230465
    sprite('tg000_01', 6)	# 230466-230471
    gotoLabel(162)
    label(163)
    sprite('tg600_11', 6)	# 230472-230477
    sprite('tg600_10', 6)	# 230478-230483
    sprite('tg600_09', 6)	# 230484-230489
    sprite('tg600_08', 6)	# 230490-230495
    sprite('tg600_07', 6)	# 230496-230501
    sprite('tg600_06', 6)	# 230502-230507
    sprite('tg600_05', 6)	# 230508-230513
    sprite('tg600_04', 6)	# 230514-230519
    sprite('tg600_03', 20)	# 230520-230539
    SFX_3('tgse_00')
    SFX_0('209_down_normal_1')
    GFX_1('tgef432_janp', -1)
    ScreenShake(0, 12500)
    sprite('tg020_00', 1)	# 230540-230540
    physicsYImpulse(25000)
    label(164)
    sprite('tg020_00', 3)	# 230541-230543
    sprite('tg020_01', 3)	# 230544-230546
    Unknown1021(5000)
    loopRest()
    gotoLabel(164)
    label(170)
    sprite('tg000_00', 1)	# 230547-230547
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('tg000_00', 6)	# 230548-230553
    sprite('tg000_01', 6)	# 230554-230559
    sprite('tg000_02', 6)	# 230560-230565
    sprite('tg000_03', 6)	# 230566-230571
    sprite('tg000_04', 6)	# 230572-230577
    sprite('tg000_05', 6)	# 230578-230583
    sprite('tg000_06', 6)	# 230584-230589
    sprite('tg000_05', 6)	# 230590-230595
    sprite('tg000_04', 6)	# 230596-230601
    sprite('tg000_03', 6)	# 230602-230607
    sprite('tg000_02', 6)	# 230608-230613
    sprite('tg000_01', 6)	# 230614-230619
    gotoLabel(171)
    label(172)
    sprite('tg300_00', 8)	# 230620-230627
    SFX_1('btg701ryn')
    sprite('tg300_01', 8)	# 230628-230635
    sprite('tg300_02', 10)	# 230636-230645
    sprite('tg300_03', 10)	# 230646-230655
    sprite('tg300_04', 10)	# 230656-230665
    sprite('tg300_02', 10)	# 230666-230675
    sprite('tg300_03', 10)	# 230676-230685
    label(173)
    sprite('tg300_04', 1)	# 230686-230686
    if SLOT_97:
        _gotolabel(173)
    sprite('tg300_04', 32767)	# 230687-263453
    Unknown23018(1)
    label(180)
    sprite('tg300_00', 8)	# 263454-263461
    Unknown2019(1000)
    SFX_1('btg700pak')
    sprite('tg300_01', 8)	# 263462-263469
    sprite('tg300_02', 10)	# 263470-263479
    sprite('tg300_03', 10)	# 263480-263489
    sprite('tg300_04', 10)	# 263490-263499
    sprite('tg300_02', 10)	# 263500-263509
    sprite('tg300_03', 10)	# 263510-263519
    label(181)
    sprite('tg300_04', 1)	# 263520-263520
    if SLOT_97:
        _gotolabel(181)
    sprite('tg300_04', 10)	# 263521-263530
    sprite('tg300_04', 32767)	# 263531-296297
    Unknown21007(24, 40)
    Unknown21011(220)

@State
def CmnActLose():
    sprite('tg620_00', 6)	# 1-6
    if SLOT_158:
        if random_(2, 0, 50):
            SFX_1('btg403_0')
        else:
            SFX_1('btg403_1')
    sprite('tg620_01', 6)	# 7-12
    SFX_3('tgse_03')
    sprite('tg620_02', 20)	# 13-32
    sprite('tg620_03', 8)	# 33-40
    sprite('tg620_04', 8)	# 41-48
    sprite('tg620_05', 12)	# 49-60
    sprite('tg620_06', 6)	# 61-66
    SFX_3('tgse_04')
    sprite('tg620_07', 6)	# 67-72
    Unknown8000(0, 1, 0)
    SFX_0('209_down_normal_1')
    ScreenShake(0, 10000)
    Unknown51(1)
    Unknown23018(1)

@State
def EventDefEntryWait():
    label(0)
    sprite('tg000_00', 6)	# 1-6
    sprite('tg000_01', 6)	# 7-12
    sprite('tg000_02', 6)	# 13-18
    sprite('tg000_03', 6)	# 19-24
    sprite('tg000_04', 6)	# 25-30
    sprite('tg000_05', 6)	# 31-36
    sprite('tg000_06', 6)	# 37-42
    sprite('tg000_05', 6)	# 43-48
    sprite('tg000_04', 6)	# 49-54
    sprite('tg000_03', 6)	# 55-60
    sprite('tg000_02', 6)	# 61-66
    sprite('tg000_01', 6)	# 67-72
    sprite('tg000_00', 6)	# 73-78
    sprite('tg000_01', 6)	# 79-84
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 85-90
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 91-96
    sprite('tg000_04', 6)	# 97-102
    sprite('tg000_05', 6)	# 103-108
    sprite('tg000_06', 6)	# 109-114
    sprite('tg000_05', 6)	# 115-120
    sprite('tg000_04', 6)	# 121-126
    sprite('tg000_03', 6)	# 127-132
    sprite('tg000_02', 6)	# 133-138
    sprite('tg000_01', 6)	# 139-144
    sprite('tg000_00', 6)	# 145-150
    sprite('tg000_01', 6)	# 151-156
    sprite('tg000_02', 6)	# 157-162
    sprite('tg000_03', 6)	# 163-168
    sprite('tg000_04', 6)	# 169-174
    sprite('tg000_05', 6)	# 175-180
    sprite('tg000_06', 6)	# 181-186
    sprite('tg000_05', 6)	# 187-192
    sprite('tg000_04', 6)	# 193-198
    sprite('tg000_03', 6)	# 199-204
    sprite('tg000_02', 6)	# 205-210
    sprite('tg000_01', 6)	# 211-216
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryStand():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefWin():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefLose():
    sprite('tg620_06', 32767)	# 1-32767

@State
def EventStandReaction():
    sprite('tg001_00', 8)	# 1-8
    sprite('tg001_01', 8)	# 9-16
    sprite('tg001_02', 8)	# 17-24
    sprite('tg001_03', 8)	# 25-32
    SFX_3('tgse_00')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000000000000')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000001000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000002000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000003000000')
    sprite('tg001_04', 8)	# 33-40
    sprite('tg001_05', 8)	# 41-48
    sprite('tg001_06', 8)	# 49-56
    sprite('tg001_07', 8)	# 57-64
    sprite('tg001_08', 8)	# 65-72
    loopRest()
    enterState('CmnActStand')

@State
def EventTimeUpLose():
    sprite('tg620_00', 6)	# 1-6
    sprite('tg620_01', 6)	# 7-12
    SFX_3('tgse_03')
    sprite('tg620_02', 20)	# 13-32
    sprite('tg620_03', 8)	# 33-40
    sprite('tg620_04', 8)	# 41-48
    sprite('tg620_05', 12)	# 49-60
    sprite('tg620_06', 6)	# 61-66
    SFX_3('tgse_04')
    sprite('tg620_07', 32767)	# 67-32833
    Unknown8000(0, 1, 0)
    SFX_0('209_down_normal_1')
    ScreenShake(0, 10000)

@State
def EventCollapse():
    sprite('tg620_00', 8)	# 1-8
    sprite('tg620_01', 6)	# 9-14
    SFX_3('tgse_03')
    sprite('tg620_02', 4)	# 15-18
    sprite('tg620_03', 6)	# 19-24
    sprite('tg620_07', 32767)	# 25-32791

@State
def EventCollapseToStand():
    sprite('tg620_03', 6)	# 1-6
    sprite('tg620_02', 4)	# 7-10
    sprite('tg620_01', 6)	# 11-16
    sprite('tg620_00', 8)	# 17-24
    loopRest()
    enterState('CmnActStand')

@State
def EventExcite():
    sprite('tg300_00', 8)	# 1-8
    sprite('tg300_01', 8)	# 9-16
    sprite('tg300_02', 10)	# 17-26
    sprite('tg300_03', 10)	# 27-36
    sprite('tg300_04', 10)	# 37-46
    sprite('tg300_02', 10)	# 47-56
    sprite('tg300_03', 10)	# 57-66
    sprite('tg300_04', 32767)	# 67-32833

@State
def EventExciteEnd():
    sprite('tg300_05', 8)	# 1-8
    sprite('tg300_06', 8)	# 9-16
    loopRest()
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('keep', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventFall():
    sprite('tg600_00', 2)	# 1-2
    sendToLabelUpon(2, 35)
    teleportRelativeY(400000)
    physicsYImpulse(-40000)
    sprite('tg600_00', 6)	# 3-8
    sprite('tg600_01', 6)	# 9-14
    sprite('tg600_02', 32767)	# 15-32781
    label(35)
    sprite('tg600_03', 20)	# 32782-32801
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    Unknown1043()
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_0('ShockB', 0)
    ScreenShake(0, 10000)
    loopRest()
    sprite('tg600_03', 80)	# 32802-32881
    sprite('tg600_04', 6)	# 32882-32887
    sprite('tg600_05', 6)	# 32888-32893
    sprite('tg600_06', 6)	# 32894-32899
    sprite('tg600_07', 6)	# 32900-32905
    sprite('tg600_08', 6)	# 32906-32911
    sprite('tg600_09', 6)	# 32912-32917
    sprite('tg600_10', 6)	# 32918-32923
    sprite('tg600_11', 6)	# 32924-32929
    loopRest()
    enterState('CmnActStand')

@State
def EventTGvsAZ1():
    sprite('tg600_05', 6)	# 1-6
    sprite('tg600_06', 6)	# 7-12
    sprite('tg600_07', 6)	# 13-18
    sprite('tg600_08', 6)	# 19-24
    sprite('tg600_09', 6)	# 25-30
    sprite('tg600_10', 6)	# 31-36
    sprite('tg600_11', 6)	# 37-42
    loopRest()
    enterState('CmnActStand')

@State
def EventTGvsAZ2():
    Unknown2034(0)
    sprite('tg033_00', 1)	# 1-1
    physicsXImpulse(-20000)
    physicsYImpulse(20000)
    Unknown1043()
    sprite('tg033_01', 1)	# 2-2
    sprite('tg033_02', 2)	# 3-4
    sprite('tg033_03', 2)	# 5-6
    Unknown1084(1)
    sprite('tg033_04', 30)	# 7-36
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-7)
    sprite('tg033_04', 30)	# 37-66
    SFX_0('014_electric_sl')
    sprite('tg033_04', 1)	# 67-67
    GFX_1('haef_event_lose_end', 103)
    Unknown1000(-500000)
    sprite('null', 32767)	# 68-32834
    loopRest()

@State
def EventVSAR1():
    label(0)
    sprite('tg601_00', 2)	# 1-2
    GFX_0('tgef_appA', 0)
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 3-4
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 5-6
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 7-8
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 9-10
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 11-12
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 13-14
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 15-16
    SFX_0('014_electric_l')
    loopRest()
    gotoLabel(0)

@State
def EventVSAR2():
    sprite('tg601_00', 2)	# 1-2
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 3-4
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 5-6
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 7-8
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 9-10
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 11-12
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 13-14
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 15-16
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 17-18
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 19-20
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 21-22
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 23-24
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 25-26
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 27-28
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 29-30
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 31-32
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 33-34
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 35-36
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 37-38
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 39-40
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 41-42
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 43-44
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 45-46
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 47-48
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 49-50
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 51-52
    SFX_3('tgse_08')
    SFX_0('014_electric_l')
    ScreenShake(0, 5000)
    GFX_0('tgef_appB', 0)
    sprite('tg601_02', 6)	# 53-58
    SFX_0('014_electric_s')
    sprite('tg601_03', 6)	# 59-64
    SFX_0('014_electric_s')
    sprite('tg601_04', 6)	# 65-70
    sprite('tg601_05', 6)	# 71-76
    sprite('tg601_06', 6)	# 77-82
    sprite('tg601_07', 6)	# 83-88
    sprite('tg601_08', 6)	# 89-94
    sprite('tg601_09', 6)	# 95-100
    loopRest()
    enterState('CmnActStand')

@State
def EventEntryElectric():
    sprite('tg601_09', 6)	# 1-6
    sprite('tg601_08', 6)	# 7-12
    sprite('tg601_07', 6)	# 13-18
    sprite('tg601_06', 6)	# 19-24
    sprite('tg601_05', 6)	# 25-30
    sprite('tg601_04', 6)	# 31-36
    sprite('tg601_03', 6)	# 37-42
    sprite('tg601_02', 6)	# 43-48
    sprite('tg601_01', 2)	# 49-50
    enterState('EventVSAR1')

@State
def EventChargeStart():
    sprite('tg405_00', 5)	# 1-5
    SFX_3('tgse_03')
    sprite('tg405_01', 5)	# 6-10
    loopRest()
    enterState('EventCharge')

@State
def EventCharge():
    label(0)
    sprite('tg405_02', 5)	# 1-5
    GFX_1('tgef_stock_AM', 0)
    SFX_3('tgse_27')
    sprite('tg405_02', 5)	# 6-10
    sprite('tg405_02', 5)	# 11-15
    gotoLabel(0)

@State
def EventChargeNoSound():
    label(0)
    sprite('tg405_02', 5)	# 1-5
    GFX_1('tgef_stock_AM', 0)
    sprite('tg405_02', 5)	# 6-10
    sprite('tg405_02', 5)	# 11-15
    gotoLabel(0)

@State
def EventChargeEnd():
    sprite('tg405_03', 5)	# 1-5
    GFX_1('tgef_stock', 0)
    ScreenShake(0, 5000)
    sprite('tg405_04', 8)	# 6-13
    SFX_3('tgse_02')
    SFX_0('200_walk_normal_2')
    sprite('tg405_05', 5)	# 14-18
    sprite('tg405_06', 5)	# 19-23
    loopRest()
    enterState('CmnActStand')

@State
def EventChargeEndNoShake():
    sprite('tg405_03', 5)	# 1-5
    GFX_1('tgef_stock', 0)
    sprite('tg405_04', 8)	# 6-13
    SFX_3('tgse_02')
    SFX_0('200_walk_normal_2')
    sprite('tg405_05', 5)	# 14-18
    sprite('tg405_06', 5)	# 19-23
    loopRest()
    enterState('CmnActStand')

@State
def EventVsTgEntry01():
    sprite('tg620_00', 6)	# 1-6
    sprite('tg620_01', 6)	# 7-12
    SFX_3('tgse_03')
    sprite('tg620_02', 20)	# 13-32
    sprite('tg620_03', 8)	# 33-40
    sprite('tg620_04', 8)	# 41-48
    sprite('tg620_05', 12)	# 49-60
    sprite('tg620_06', 6)	# 61-66

@State
def EventNoise():
    sprite('keep', 60)	# 1-60
    GFX_0('NOISE', -1)
    SFX_0('023_noize')
    enterState('CmnActStand')

@State
def EventNoise_Long():
    sprite('keep', 60)	# 1-60
    GFX_0('NOISE_Long', -1)
    SFX_0('023_noize')
    enterState('CmnActStand')

@State
def EventRlVsTgEntry01():
    sprite('tg300_01', 8)	# 1-8
    sprite('tg300_02', 10)	# 9-18
    sprite('tg300_03', 10)	# 19-28
    sprite('tg300_04', 10)	# 29-38
    sprite('tg300_02', 10)	# 39-48
    sprite('tg300_03', 10)	# 49-58
    sprite('tg300_04', 10)	# 59-68

@State
def EventRlVsTgEntry02():
    sprite('tg300_05', 8)	# 1-8
    sprite('tg300_06', 8)	# 9-16
    sprite('tg000_00', 6)	# 17-22
    sprite('tg620_00', 6)	# 23-28
    sprite('tg620_01', 6)	# 29-34
    sprite('tg620_02', 6)	# 35-40
    sprite('tg620_03', 6)	# 41-46

@State
def EventRlVsTgEntry03():
    sprite('tg620_03', 180)	# 1-180
    sprite('tg620_02', 6)	# 181-186
    sprite('tg620_01', 6)	# 187-192
    sprite('tg620_00', 6)	# 193-198
    label(0)
    sprite('tg000_00', 6)	# 199-204
    sprite('tg000_01', 6)	# 205-210
    sprite('tg000_02', 6)	# 211-216
    sprite('tg000_03', 6)	# 217-222
    sprite('tg000_04', 6)	# 223-228
    sprite('tg000_05', 6)	# 229-234
    sprite('tg000_06', 6)	# 235-240
    sprite('tg000_05', 6)	# 241-246
    sprite('tg000_04', 6)	# 247-252
    sprite('tg000_03', 6)	# 253-258
    sprite('tg000_02', 6)	# 259-264
    sprite('tg000_01', 6)	# 265-270
    sprite('tg000_00', 6)	# 271-276
    sprite('tg000_01', 6)	# 277-282
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 283-288
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 289-294
    sprite('tg000_04', 6)	# 295-300
    sprite('tg000_05', 6)	# 301-306
    sprite('tg000_06', 6)	# 307-312
    sprite('tg000_05', 6)	# 313-318
    sprite('tg000_04', 6)	# 319-324
    sprite('tg000_03', 6)	# 325-330
    sprite('tg000_02', 6)	# 331-336
    sprite('tg000_01', 6)	# 337-342
    sprite('tg000_00', 6)	# 343-348
    sprite('tg000_01', 6)	# 349-354
    sprite('tg000_02', 6)	# 355-360
    sprite('tg000_03', 6)	# 361-366
    sprite('tg000_04', 6)	# 367-372
    sprite('tg000_05', 6)	# 373-378
    sprite('tg000_06', 6)	# 379-384
    sprite('tg000_05', 6)	# 385-390
    sprite('tg000_04', 6)	# 391-396
    sprite('tg000_03', 6)	# 397-402
    sprite('tg000_02', 6)	# 403-408
    sprite('tg000_01', 6)	# 409-414
    loopRest()
    gotoLabel(0)

@State
def EventRlVsTgLose01():
    sprite('tg620_03', 32767)	# 1-32767

@State
def EventRlVsTgLose02():
    sprite('tg620_03', 210)	# 1-210
    sprite('tg070_08', 6)	# 211-216
    teleportRelativeX(-82000)
    sprite('tg070_09', 6)	# 217-222
    sprite('tg070_10', 6)	# 223-228
    sprite('tg070_11', 6)	# 229-234
    sprite('tg070_12', 6)	# 235-240
    sprite('tg070_13', 6)	# 241-246
    sprite('tg063_09', 6)	# 247-252
    teleportRelativeX(164000)
    SFX_0('209_down_normal_1')
    Unknown8000(0, 1, 0)
    sprite('tg063_10', 6)	# 253-258
    sprite('tg063_11', 6)	# 259-264

@State
def EventTGWarp():
    Unknown2034(0)
    sprite('tg405_00', 6)	# 1-6
    Unknown1043()
    sprite('tg405_01', 6)	# 7-12
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('tg405_02', 6)	# 13-18
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('tg405_02', 6)	# 19-24
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('tg405_02', 6)	# 25-30
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-7)
    sprite('tg405_02', 30)	# 31-60
    SFX_0('014_electric_sl')
    GFX_1('haef_event_lose_end', 103)
    sprite('tg405_02', 1)	# 61-61
    Unknown1000(-500000)
    sprite('null', 32767)	# 62-32828
    loopRest()

@State
def EventVSKG01():
    sprite('keep', 32767)	# 1-32767
    Unknown3038(1)
    GFX_0('EventBL', -1)

@State
def EventVSKG02():
    sprite('keep', 32767)	# 1-32767
    GFX_0('EventBLBDash', -1)

@State
def EventVSKG1():
    sprite('tg000_00', 6)	# 1-6
    sprite('tg000_01', 6)	# 7-12
    sprite('tg000_02', 6)	# 13-18
    sprite('tg000_03', 6)	# 19-24
    sprite('tg000_04', 6)	# 25-30
    sprite('tg000_05', 6)	# 31-36
    sprite('tg000_06', 6)	# 37-42
    sprite('tg000_05', 6)	# 43-48
    sprite('tg000_04', 6)	# 49-54
    sprite('tg000_03', 6)	# 55-60
    sprite('tg000_02', 6)	# 61-66
    sprite('tg000_01', 6)	# 67-72
    enterState('EventExcite')

@State
def EventVSKG1End():
    sprite('keep', 1)	# 1-1
    Unknown21012('4576656e74424c0000000000000000000000000000000000000000000000000020000000')
    enterState('EventExciteEnd')

@State
def EventBL2():

    def upon_IMMEDIATE():
        Unknown1000(-260000)
    GFX_0('EventBLBDash', -1)
    enterState('CmnActStand')

@State
def EventStandTurn():
    sprite('tg003_00', 4)	# 1-4
    Unknown2005()
    sprite('tg003_01', 4)	# 5-8
    sprite('tg003_02', 4)	# 9-12
    sprite('tg000_00', 6)	# 13-18
    label(0)
    sprite('tg000_01', 6)	# 19-24
    sprite('tg000_02', 6)	# 25-30
    sprite('tg000_03', 6)	# 31-36
    sprite('tg000_04', 6)	# 37-42
    sprite('tg000_05', 6)	# 43-48
    sprite('tg000_06', 6)	# 49-54
    sprite('tg000_05', 6)	# 55-60
    sprite('tg000_04', 6)	# 61-66
    sprite('tg000_03', 6)	# 67-72
    sprite('tg000_02', 6)	# 73-78
    sprite('tg000_01', 6)	# 79-84
    sprite('tg000_00', 6)	# 85-90
    gotoLabel(0)

@State
def EventVSKG2():

    def upon_IMMEDIATE():
        Unknown1000(100000)
    sprite('keep', 1)	# 1-1
    GFX_0('EventBL2', -1)
    enterState('CmnActStand')

@State
def EventVSAZ01():
    sprite('keep', 32767)	# 1-32767
    GFX_0('EventBL', -1)
    enterState('CmnActStand')

@State
def EventVSAZ02():
    sprite('tg601_00', 2)	# 1-2
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 3-4
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 5-6
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 7-8
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 9-10
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 11-12
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 13-14
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 15-16
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 17-18
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 19-20
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 21-22
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 23-24
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 25-26
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 27-28
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 29-30
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 31-32
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 33-34
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 35-36
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 37-38
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 39-40
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 41-42
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 43-44
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 45-46
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 47-48
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 49-50
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 51-52
    SFX_3('tgse_08')
    SFX_0('014_electric_l')
    ScreenShake(0, 5000)
    GFX_0('tgef_appB', 0)
    sprite('tg601_02', 6)	# 53-58
    SFX_0('014_electric_s')
    Unknown21012('4576656e74424c0000000000000000000000000000000000000000000000000020000000')
    sprite('tg601_03', 6)	# 59-64
    SFX_0('014_electric_s')
    sprite('tg601_04', 6)	# 65-70
    sprite('tg601_05', 6)	# 71-76
    sprite('tg601_06', 6)	# 77-82
    sprite('tg601_07', 6)	# 83-88
    sprite('tg601_08', 6)	# 89-94
    sprite('tg601_09', 6)	# 95-100
    loopRest()
    enterState('CmnActStand')

@State
def EventTGWarp2():
    Unknown2034(0)
    sprite('keep', 6)	# 1-6
    Unknown1043()
    sprite('keep', 6)	# 7-12
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('keep', 6)	# 13-18
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('keep', 6)	# 19-24
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('keep', 6)	# 25-30
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-7)
    sprite('keep', 30)	# 31-60
    SFX_0('014_electric_sl')
    GFX_1('haef_event_lose_end', 103)
    sprite('keep', 1)	# 61-61
    Unknown1000(-500000)
    sprite('null', 32767)	# 62-32828
    loopRest()

@State
def EventVSAZ03():
    sprite('tg040_00', 4)	# 1-4
    label(0)
    sprite('tg040_01', 6)	# 5-10
    loopRest()
    gotoLabel(0)

@State
def EventVSAZ03End():
    sprite('tg040_01', 4)	# 1-4
    sprite('tg040_00', 4)	# 5-8
    Unknown21012('4576656e74424c0000000000000000000000000000000000000000000000000020000000')
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Lose():
    sprite('tg620_00', 6)	# 1-6
    sprite('tg620_01', 6)	# 7-12
    SFX_3('tgse_03')
    sprite('tg620_02', 20)	# 13-32
    sprite('tg620_03', 8)	# 33-40
    sprite('tg620_04', 8)	# 41-48
    sprite('tg620_05', 12)	# 49-60
    sprite('tg620_06', 6)	# 61-66
    SFX_3('tgse_04')
    sprite('tg620_07', 32767)	# 67-32833
    Unknown8000(0, 1, 0)
    SFX_0('209_down_normal_1')

@State
def Act2Event_tgvsmi_00():
    sprite('tg611_00', 7)	# 1-7
    sprite('tg611_01', 7)	# 8-14
    sprite('tg611_02', 7)	# 15-21
    sprite('tg611_03', 7)	# 22-28
    sprite('tg611_04', 7)	# 29-35
    sprite('tg611_05', 7)	# 36-42
    sprite('tg611_06', 7)	# 43-49
    sprite('tg611_07', 7)	# 50-56
    sprite('tg611_08', 60)	# 57-116
    sprite('tg611_08', 7)	# 117-123
    SFX_3('tgse_07')
    sprite('tg611_09', 7)	# 124-130
    sprite('tg611_10', 7)	# 131-137
    sprite('tg611_11', 7)	# 138-144
    sprite('tg611_12', 7)	# 145-151
    sprite('tg611_13', 7)	# 152-158
    sprite('tg611_11', 7)	# 159-165
    sprite('tg611_10', 20)	# 166-185
    sprite('tg611_05', 7)	# 186-192
    sprite('tg611_04', 7)	# 193-199
    sprite('tg611_03', 18)	# 200-217
    sprite('tg611_02', 7)	# 218-224
    sprite('tg611_01', 7)	# 225-231
    SFX_3('tgse_05')
    sprite('tg611_00', 7)	# 232-238
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_havstg():
    sprite('tg611_00', 7)	# 1-7
    Unknown2005()
    sprite('tg611_01', 7)	# 8-14
    sprite('tg611_02', 7)	# 15-21
    sprite('tg611_03', 7)	# 22-28
    sprite('tg611_04', 7)	# 29-35
    sprite('tg611_05', 7)	# 36-42
    sprite('tg611_06', 7)	# 43-49
    sprite('tg611_07', 7)	# 50-56
    sprite('tg611_08', 120)	# 57-176
    sprite('tg611_09', 7)	# 177-183
    sprite('tg611_10', 7)	# 184-190
    sprite('tg611_11', 7)	# 191-197
    sprite('tg611_12', 32767)	# 198-32964
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_havstgEnd():
    sprite('tg611_11', 7)	# 1-7
    sprite('tg611_10', 7)	# 8-14
    sprite('tg611_06', 7)	# 15-21
    sprite('tg611_05', 7)	# 22-28
    sprite('tg611_04', 7)	# 29-35
    sprite('tg611_03', 7)	# 36-42
    sprite('tg611_02', 7)	# 43-49
    sprite('tg611_01', 7)	# 50-56
    sprite('tg611_00', 7)	# 57-63
    Unknown2005()
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventNoDisp():
    sprite('keep', 32767)	# 1-32767
    Unknown3038(1)

@State
def Act2Event_Fall():
    sprite('tg600_00', 2)	# 1-2
    sendToLabelUpon(2, 35)
    teleportRelativeY(400000)
    physicsYImpulse(-40000)
    sprite('tg600_00', 6)	# 3-8
    sprite('tg600_01', 6)	# 9-14
    sprite('tg600_02', 32767)	# 15-32781
    label(35)
    sprite('tg600_03', 20)	# 32782-32801
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    Unknown1043()
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_1('tgef_dustB', -1)
    GFX_0('ShockB', 0)
    ScreenShake(0, 10000)
    loopRest()
    sprite('tg600_03', 20)	# 32802-32821
    sprite('tg600_04', 6)	# 32822-32827
    sprite('tg600_05', 6)	# 32828-32833
    sprite('tg600_06', 6)	# 32834-32839
    sprite('tg600_07', 6)	# 32840-32845
    sprite('tg600_08', 6)	# 32846-32851
    sprite('tg600_09', 6)	# 32852-32857
    sprite('tg600_10', 6)	# 32858-32863
    sprite('tg600_11', 6)	# 32864-32869
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_LoseInartia():
    Unknown1000(0)
    sprite('tg620_00', 4)	# 1-4
    SFX_0('104_guard_grap_1')
    ScreenShake(3000, 18000)
    Unknown1047(-40000)
    SFX_0('015_blaze_2')
    SFX_0('015_blaze_1')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('tg620_01', 4)	# 5-8
    SFX_3('tgse_03')
    sprite('tg620_02', 6)	# 9-14
    sprite('tg620_03', 8)	# 15-22
    sprite('tg620_06', 32767)	# 23-32789
    Unknown1084(1)
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventChouhatu():
    sprite('tg300_00', 8)	# 1-8
    sprite('tg300_01', 8)	# 9-16
    sprite('tg300_02', 10)	# 17-26
    sprite('tg300_03', 10)	# 27-36
    sprite('tg300_04', 10)	# 37-46
    sprite('tg300_02', 10)	# 47-56
    sprite('tg300_03', 10)	# 57-66
    sprite('tg300_04', 32767)	# 67-32833

@State
def Act2EventChouhatuEnd():
    sprite('tg300_05', 8)	# 1-8
    sprite('tg300_06', 8)	# 9-16
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventChargeStart():
    sprite('tg405_00', 5)	# 1-5
    SFX_3('tgse_03')
    sprite('tg405_01', 5)	# 6-10
    loopRest()
    enterState('Act2EventCharge')

@State
def Act2EventCharge():
    label(0)
    sprite('tg405_02', 5)	# 1-5
    GFX_1('tgef_stock_AM', 0)
    SFX_3('tgse_27')
    sprite('tg405_02', 5)	# 6-10
    sprite('tg405_02', 5)	# 11-15
    gotoLabel(0)

@State
def Act2EventChargeEnd():
    sprite('tg405_03', 5)	# 1-5
    GFX_1('tgef_stock', 0)
    ScreenShake(0, 5000)
    sprite('tg405_04', 8)	# 6-13
    SFX_3('tgse_02')
    SFX_0('200_walk_normal_2')
    sprite('tg405_05', 5)	# 14-18
    sprite('tg405_06', 5)	# 19-23
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventWarpOut():
    Unknown2034(0)
    sprite('tg033_00', 1)	# 1-1
    physicsXImpulse(-20000)
    physicsYImpulse(20000)
    Unknown1043()
    sprite('tg033_01', 1)	# 2-2
    sprite('tg033_02', 2)	# 3-4
    sprite('tg033_03', 2)	# 5-6
    Unknown1084(1)
    sprite('tg033_04', 30)	# 7-36
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-7)
    sprite('tg033_04', 30)	# 37-66
    SFX_0('014_electric_sl')
    sprite('tg033_04', 1)	# 67-67
    GFX_1('haef_event_lose_end', 103)
    Unknown1000(-500000)
    sprite('null', 32767)	# 68-32834
    loopRest()

@State
def Act2EventStandReaction():
    sprite('tg001_00', 8)	# 1-8
    sprite('tg001_01', 8)	# 9-16
    sprite('tg001_02', 8)	# 17-24
    sprite('tg001_03', 8)	# 25-32
    SFX_3('tgse_00')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000000000000')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000001000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000002000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000003000000')
    sprite('tg001_04', 8)	# 33-40
    sprite('tg001_05', 8)	# 41-48
    sprite('tg001_06', 8)	# 49-56
    sprite('tg001_07', 8)	# 57-64
    sprite('tg001_08', 8)	# 65-72
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventSledgetame():
    sprite('tg401_00', 3)	# 1-3
    sprite('tg401_01', 3)	# 4-6
    sprite('tg401_02', 4)	# 7-10
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    label(0)
    sprite('tg401_03', 4)	# 11-14
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_03', 4)	# 15-18
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    loopRest()
    gotoLabel(0)

@State
def Act2EventSledgeStop():
    sprite('tg401_02', 6)	# 1-6
    sprite('tg401_01', 6)	# 7-12
    sprite('tg401_00', 6)	# 13-18
    enterState('CmnActStand')

@State
def Act2EventWalkEntryWait_tgvsha():
    sprite('null', 1)	# 1-1
    Unknown2034(0)
    Unknown2017(0)
    sprite('null', 1)	# 2-2
    Unknown1000(-2200000)
    sprite('null', 32767)	# 3-32769
    loopRest()

@State
def Act2EventWalkEntry_tgvha00():
    Unknown20000(1)
    Unknown2034(0)
    Unknown2037(1)

    def upon_3():
        if SLOT_2:
            if (SLOT_19 < 1610000):
                Unknown2037(0)
                sendToLabel(2)
        if SLOT_51:
            if (SLOT_19 < 520000):
                SLOT_51 = 0
                SLOT_52 = 1
                Unknown20000(0)
                sendToLabel(2)

    def upon_32():
        SLOT_51 = 1
        clearUponHandler(32)
        sendToLabel(0)
    label(0)
    sprite('tg030_00', 6)	# 1-6
    physicsXImpulse(4800)
    label(1)
    sprite('tg030_01', 6)	# 7-12
    sprite('tg030_02', 6)	# 13-18
    sprite('tg030_03', 6)	# 19-24
    sprite('tg030_04', 6)	# 25-30
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 6)	# 31-36
    sprite('tg030_06', 6)	# 37-42
    sprite('tg030_07', 6)	# 43-48
    sprite('tg030_08', 6)	# 49-54
    sprite('tg030_09', 6)	# 55-60
    sprite('tg030_10', 6)	# 61-66
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 6)	# 67-72
    sprite('tg030_12', 6)	# 73-78
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('tg030_00', 4)	# 79-82
    Unknown1084(1)
    if SLOT_52:
        Unknown20000(0)
        Unknown1000(-260000)
    loopRest()
    label(3)
    sprite('tg000_00', 6)	# 83-88
    sprite('tg000_01', 6)	# 89-94
    sprite('tg000_02', 6)	# 95-100
    sprite('tg000_03', 6)	# 101-106
    sprite('tg000_04', 6)	# 107-112
    sprite('tg000_05', 6)	# 113-118
    sprite('tg000_06', 6)	# 119-124
    sprite('tg000_05', 6)	# 125-130
    sprite('tg000_04', 6)	# 131-136
    sprite('tg000_03', 6)	# 137-142
    sprite('tg000_02', 6)	# 143-148
    sprite('tg000_01', 6)	# 149-154
    sprite('tg000_00', 6)	# 155-160
    sprite('tg000_01', 6)	# 161-166
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 167-172
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 173-178
    SFX_0('014_electric_s')
    sprite('tg000_04', 6)	# 179-184
    sprite('tg000_05', 6)	# 185-190
    sprite('tg000_06', 6)	# 191-196
    sprite('tg000_05', 6)	# 197-202
    sprite('tg000_04', 6)	# 203-208
    sprite('tg000_03', 6)	# 209-214
    sprite('tg000_02', 6)	# 215-220
    sprite('tg000_01', 6)	# 221-226
    sprite('tg000_00', 6)	# 227-232
    sprite('tg000_01', 6)	# 233-238
    sprite('tg000_02', 6)	# 239-244
    sprite('tg000_03', 6)	# 245-250
    sprite('tg000_04', 6)	# 251-256
    sprite('tg000_05', 6)	# 257-262
    sprite('tg000_06', 6)	# 263-268
    sprite('tg000_05', 6)	# 269-274
    sprite('tg000_04', 6)	# 275-280
    sprite('tg000_03', 6)	# 281-286
    sprite('tg000_02', 6)	# 287-292
    sprite('tg000_01', 6)	# 293-298
    loopRest()
    gotoLabel(3)

@State
def Act2EventBattle_tgvsha():

    def upon_IMMEDIATE():
        Unknown23022(1)
        teleportRelativeX(-56000)
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
    label(0)
    sprite('keep', 5)	# 1-5
    sprite('tg401_00', 2)	# 6-7
    sprite('tg401_01', 2)	# 8-9
    sprite('tg401_02', 3)	# 10-12
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    sprite('tg401_03', 7)	# 13-19
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_04', 7)	# 20-26
    teleportRelativeX(100000)
    Unknown1047(15000)
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_05', 4)	# 27-30
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('RollingAttackEff', 0)
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg401_06', 3)	# 31-33	 **attackbox here**
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    SFX_0('213_bound_1')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_08', 2)	# 34-35
    RefreshMultihit()
    sprite('tg402_00', 6)	# 36-41
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    sprite('tg402_01', 6)	# 42-47
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    sprite('tg402_02', 6)	# 48-53
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    Unknown1047(12000)
    sprite('tg402_03', 6)	# 54-59
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg402_04', 1)	# 60-60
    SFX_0('005_swing_grap_2_2')
    sprite('tg402_05', 1)	# 61-61
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('SledgeHammerEFF', 0)
    sprite('tg402_06', 1)	# 62-62
    sprite('tg402_07', 6)	# 63-68	 **attackbox here**
    SFX_3('tgse_20')
    SFX_0('213_bound_0')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('ShockB402', 6)
    Unknown8000(6, 1, 1)
    sprite('tg402_07', 10)	# 69-78	 **attackbox here**
    sprite('tg402_08', 4)	# 79-82
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg402_09', 6)	# 83-88
    sprite('tg402_10', 6)	# 89-94
    sprite('tg402_11', 6)	# 95-100
    sprite('tg402_12', 7)	# 101-107
    sprite('tg033_00', 1)	# 108-108
    Unknown22008(20)
    physicsYImpulse(10000)
    physicsXImpulse(-6500)
    setGravity(1000)

    def upon_LANDING():
        Unknown1084(1)
        sendToLabel(2)
    sprite('tg033_01', 1)	# 109-109
    sprite('tg033_02', 3)	# 110-112
    label(1)
    sprite('tg033_03', 3)	# 113-115
    sprite('tg033_04', 3)	# 116-118
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('tg033_05', 3)	# 119-121
    SFX_3('tgse_26')
    sprite('tg033_06', 3)	# 122-124
    sprite('tg033_07', 3)	# 125-127
    sprite('tg033_08', 3)	# 128-130
    sprite('tg620_00', 4)	# 131-134
    SFX_0('104_guard_grap_1')
    ScreenShake(3000, 18000)
    physicsXImpulse(-42000)
    SFX_0('015_blaze_2')
    SFX_0('015_blaze_1')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('tg620_01', 4)	# 135-138
    Unknown1019(80)
    SFX_3('tgse_03')
    sprite('tg620_02', 4)	# 139-142
    Unknown1019(80)
    sprite('tg620_02', 2)	# 143-144
    sprite('tg620_03', 2)	# 145-146
    Unknown1019(80)
    sprite('tg620_03', 4)	# 147-150
    Unknown1019(80)
    sprite('tg620_03', 2)	# 151-152
    sprite('tg620_06', 2)	# 153-154
    Unknown1019(50)
    sprite('tg620_06', 32767)	# 155-32921
    Unknown1084(1)
    GFX_0('Act2EventCamera_tgvsha', 100)
    loopRest()

@State
def Act2Event_tgvsha00():
    sprite('keep', 32767)	# 1-32767
    Unknown21012('416374324576656e7443616d6572615f7467767368610000000000000000000020000000')

@State
def Act2Event_tgvsha01():

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 >= 8):
            ScreenShake(3000, 2000)
            Unknown2038(-8)
            SFX_0('019_quake_0')
    sprite('tg620_03', 6)	# 1-6
    SFX_0('014_electric_sl')
    sprite('tg620_02', 4)	# 7-10
    sprite('tg620_01', 6)	# 11-16
    sprite('tg620_00', 8)	# 17-24
    loopRest()
    label(0)
    sprite('tg000_00', 6)	# 25-30
    sprite('tg000_01', 6)	# 31-36
    sprite('tg000_02', 6)	# 37-42
    sprite('tg000_03', 6)	# 43-48
    sprite('tg000_04', 6)	# 49-54
    sprite('tg000_05', 6)	# 55-60
    sprite('tg000_06', 6)	# 61-66
    sprite('tg000_05', 6)	# 67-72
    sprite('tg000_04', 6)	# 73-78
    sprite('tg000_03', 6)	# 79-84
    sprite('tg000_02', 6)	# 85-90
    sprite('tg000_01', 6)	# 91-96
    sprite('tg000_00', 6)	# 97-102
    sprite('tg000_01', 6)	# 103-108
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 109-114
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 115-120
    SFX_0('014_electric_s')
    sprite('tg000_04', 6)	# 121-126
    sprite('tg000_05', 6)	# 127-132
    sprite('tg000_06', 6)	# 133-138
    sprite('tg000_05', 6)	# 139-144
    sprite('tg000_04', 6)	# 145-150
    sprite('tg000_03', 6)	# 151-156
    sprite('tg000_02', 6)	# 157-162
    sprite('tg000_01', 6)	# 163-168
    sprite('tg000_00', 6)	# 169-174
    sprite('tg000_01', 6)	# 175-180
    sprite('tg000_02', 6)	# 181-186
    sprite('tg000_03', 6)	# 187-192
    sprite('tg000_04', 6)	# 193-198
    sprite('tg000_05', 6)	# 199-204
    sprite('tg000_06', 6)	# 205-210
    sprite('tg000_05', 6)	# 211-216
    sprite('tg000_04', 6)	# 217-222
    sprite('tg000_03', 6)	# 223-228
    sprite('tg000_02', 6)	# 229-234
    sprite('tg000_01', 6)	# 235-240
    loopRest()
    gotoLabel(0)

@State
def Act2EventKeep():
    sprite('keep', 32767)	# 1-32767
    Unknown21007(22, 32)
    loopRest()

@State
def Act2EventTG_StepOut():
    sprite('tg033_00', 3)	# 1-3
    Unknown2034(0)
    physicsYImpulse(13000)
    physicsXImpulse(-15000)
    setGravity(700)
    sendToLabelUpon(2, 1)
    sprite('tg033_01', 3)	# 4-6
    sprite('tg033_02', 3)	# 7-9
    SFX_0('000_airdash_2')
    label(0)
    sprite('tg033_03', 3)	# 10-12
    sprite('tg033_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 32767)	# 16-32782
    loopRest()

@State
def Act2EventTG_WalkOut_tgvskk():
    sprite('tg003_00', 4)	# 1-4
    Unknown2034(0)
    Unknown2005()
    sprite('tg003_01', 4)	# 5-8
    sprite('tg003_02', 4)	# 9-12
    sprite('tg030_00', 6)	# 13-18
    physicsXImpulse(4800)
    label(1)
    sprite('tg030_01', 6)	# 19-24
    sprite('tg030_02', 6)	# 25-30
    sprite('tg030_03', 6)	# 31-36
    sprite('tg030_04', 6)	# 37-42
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 6)	# 43-48
    sprite('tg030_06', 6)	# 49-54
    sprite('tg030_07', 6)	# 55-60
    sprite('tg030_08', 6)	# 61-66
    sprite('tg030_09', 6)	# 67-72
    sprite('tg030_10', 6)	# 73-78
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 6)	# 79-84
    sprite('tg030_12', 6)	# 85-90
    sprite('tg030_01', 6)	# 91-96
    sprite('tg030_02', 6)	# 97-102
    sprite('tg030_03', 6)	# 103-108
    sprite('tg030_04', 6)	# 109-114
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 6)	# 115-120
    sprite('tg030_06', 6)	# 121-126
    sprite('tg030_07', 6)	# 127-132
    sprite('tg030_08', 6)	# 133-138
    sprite('tg030_09', 6)	# 139-144
    sprite('tg030_10', 6)	# 145-150
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 6)	# 151-156
    sprite('tg030_12', 6)	# 157-162
    sprite('tg030_01', 6)	# 163-168
    sprite('tg030_02', 6)	# 169-174
    sprite('tg030_03', 6)	# 175-180
    sprite('tg030_04', 6)	# 181-186
    sprite('tg030_05', 6)	# 187-192
    sprite('tg030_06', 6)	# 193-198
    sprite('tg030_07', 6)	# 199-204
    sprite('tg030_08', 6)	# 205-210
    sprite('tg030_09', 6)	# 211-216
    sprite('tg030_10', 6)	# 217-222
    sprite('tg030_11', 6)	# 223-228
    sprite('tg030_12', 6)	# 229-234
    sprite('null', 32767)	# 235-33001
    loopRest()

@State
def Act3Event_NoDisp():

    def upon_IMMEDIATE():
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act3Event_Stand():
    label(0)
    sprite('tg000_00', 6)	# 1-6
    sprite('tg000_01', 6)	# 7-12
    sprite('tg000_02', 6)	# 13-18
    sprite('tg000_03', 6)	# 19-24
    sprite('tg000_04', 6)	# 25-30
    sprite('tg000_05', 6)	# 31-36
    sprite('tg000_06', 6)	# 37-42
    sprite('tg000_05', 6)	# 43-48
    sprite('tg000_04', 6)	# 49-54
    sprite('tg000_03', 6)	# 55-60
    sprite('tg000_02', 6)	# 61-66
    sprite('tg000_01', 6)	# 67-72
    sprite('tg000_00', 6)	# 73-78
    sprite('tg000_01', 6)	# 79-84
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 85-90
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 91-96
    sprite('tg000_04', 6)	# 97-102
    sprite('tg000_05', 6)	# 103-108
    sprite('tg000_06', 6)	# 109-114
    sprite('tg000_05', 6)	# 115-120
    sprite('tg000_04', 6)	# 121-126
    sprite('tg000_03', 6)	# 127-132
    sprite('tg000_02', 6)	# 133-138
    sprite('tg000_01', 6)	# 139-144
    sprite('tg000_00', 6)	# 145-150
    sprite('tg000_01', 6)	# 151-156
    sprite('tg000_02', 6)	# 157-162
    sprite('tg000_03', 6)	# 163-168
    sprite('tg000_04', 6)	# 169-174
    sprite('tg000_05', 6)	# 175-180
    sprite('tg000_06', 6)	# 181-186
    sprite('tg000_05', 6)	# 187-192
    sprite('tg000_04', 6)	# 193-198
    sprite('tg000_03', 6)	# 199-204
    sprite('tg000_02', 6)	# 205-210
    sprite('tg000_01', 6)	# 211-216
    loopRest()
    gotoLabel(0)

@State
def Act3Event_Chouhatsu():
    sprite('tg300_00', 8)	# 1-8
    sprite('tg300_01', 8)	# 9-16
    sprite('tg300_02', 10)	# 17-26
    sprite('tg300_03', 10)	# 27-36
    sprite('tg300_04', 10)	# 37-46
    sprite('tg300_02', 10)	# 47-56
    sprite('tg300_03', 10)	# 57-66
    sprite('tg300_04', 32767)	# 67-32833

@State
def Act3Event_ChouhatsuEnd():
    sprite('tg300_05', 8)	# 1-8
    sprite('tg300_06', 8)	# 9-16
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_Fall():

    def upon_IMMEDIATE():
        teleportRelativeY(960000)
        physicsYImpulse(-30000)
        Unknown1043()

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(0)
            Unknown8000(100, 1, 0)
            Unknown8000(100, 1, 0)
            Unknown8000(100, 1, 0)
            Unknown8000(100, 1, 0)
            Unknown8000(100, 1, 1)
            Unknown8001(3, 0)
            GFX_1('tgef_dustB', -1)
            GFX_1('tgef_dustB', -1)
            GFX_1('tgef_dustB', -1)
            GFX_1('tgef_dustB', -1)
            GFX_0('ShockB', 0)
            ScreenShake(0, 10000)
    sprite('tg600_00', 6)	# 1-6
    sprite('tg600_01', 6)	# 7-12
    sprite('tg600_02', 32767)	# 13-32779
    label(0)
    sprite('tg600_03', 40)	# 32780-32819
    sprite('tg600_04', 6)	# 32820-32825
    sprite('tg600_05', 6)	# 32826-32831
    sprite('tg600_06', 6)	# 32832-32837
    sprite('tg600_07', 6)	# 32838-32843
    sprite('tg600_08', 6)	# 32844-32849
    sprite('tg600_09', 6)	# 32850-32855
    sprite('tg600_10', 6)	# 32856-32861
    sprite('tg600_11', 6)	# 32862-32867
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsar_00():
    sprite('tg600_03', 32767)	# 1-32767
    loopRest()

@State
def Act3Event_tgvsar_01():
    sprite('tg600_03', 20)	# 1-20
    sprite('tg600_04', 6)	# 21-26
    sprite('tg600_05', 6)	# 27-32
    sprite('tg600_06', 6)	# 33-38
    sprite('tg600_07', 6)	# 39-44
    sprite('tg600_08', 6)	# 45-50
    sprite('tg600_09', 6)	# 51-56
    sprite('tg600_10', 6)	# 57-62
    sprite('tg600_11', 6)	# 63-68
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsar_02():
    sprite('tg601_09', 7)	# 1-7
    sprite('tg601_08', 7)	# 8-14
    sprite('tg601_07', 7)	# 15-21
    sprite('tg601_06', 7)	# 22-28
    sprite('tg601_05', 7)	# 29-35
    sprite('tg601_02', 7)	# 36-42
    sprite('tg333_07', 2)	# 43-44
    teleportRelativeX(-35000)
    sprite('tg601_01', 10)	# 45-54
    teleportRelativeX(35000)
    SFX_3('tgse_08')
    ScreenShake(0, 20000)
    label(0)
    sprite('tg601_00', 2)	# 55-56
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 57-58
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 59-60
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 61-62
    SFX_0('014_electric_l')
    loopRest()
    gotoLabel(0)

@State
def Act3Event_tgvsar_03():
    sprite('tg601_00', 2)	# 1-2
    SFX_0('014_electric_l')
    GFX_0('tgef_appA', 0)
    sprite('tg601_01', 2)	# 3-4
    SFX_0('014_electric_l')
    sprite('tg601_00', 2)	# 5-6
    SFX_0('014_electric_l')
    sprite('tg601_01', 2)	# 7-8
    SFX_3('tgse_08')
    SFX_0('014_electric_l')
    ScreenShake(0, 5000)
    GFX_0('tgef_appB', 0)
    sprite('tg601_02', 6)	# 9-14
    SFX_0('014_electric_s')
    sprite('tg601_03', 6)	# 15-20
    SFX_0('014_electric_s')
    sprite('tg601_04', 6)	# 21-26
    sprite('tg601_05', 6)	# 27-32
    sprite('tg601_06', 6)	# 33-38
    sprite('tg601_07', 6)	# 39-44
    sprite('tg601_08', 6)	# 45-50
    sprite('tg601_09', 6)	# 51-56
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsar_04():

    def upon_IMMEDIATE():
        Unknown2003(1)
        Unknown2019(-750)
    sprite('tg203_03', 2)	# 1-2
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    SFX_0('014_electric_m')
    sprite('tg203_04', 3)	# 3-5	 **attackbox here**
    GFX_0('StayMagneticB', 0)
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_m')
    sprite('tg203_05', 2)	# 6-7	 **attackbox here**
    GFX_1('tgef_side_shockA', 3)
    sprite('tg203_06', 19)	# 8-26	 **attackbox here**
    SFX_3('tgse_26')
    GFX_0('tgef203mc', 0)
    GFX_0('AddMagnetPtc', 0)
    GFX_0('StayMagneticB203', 0)
    GFX_0('StayMagneticB203', 1)
    GFX_0('StayMagneticB203', 2)
    GFX_0('StayMagneticB203', 3)
    GFX_0('StayMagneticB203', 4)
    GFX_0('StayMagneticB203', 5)
    sprite('tg203_07', 5)	# 27-31	 **attackbox here**
    Unknown4048(290000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000000000000')
    Unknown4048(250000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    sprite('tg203_08', 5)	# 32-36	 **attackbox here**
    sprite('tg203_09', 5)	# 37-41
    SFX_3('tgse_00')
    sprite('tg203_10', 5)	# 42-46
    sprite('tg203_11', 5)	# 47-51
    sprite('tg203_12', 5)	# 52-56
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsar_05():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('tg401_00', 4)	# 1-4
    sprite('tg401_01', 4)	# 5-8
    sprite('tg401_02', 4)	# 9-12
    SFX_0('014_electric_s')
    GFX_0('StayMagneticA', 0)
    sprite('tg401_03', 10)	# 13-22
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_03', 10)	# 23-32
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    sprite('tg401_04', 3)	# 33-35
    teleportRelativeX(100000)
    Unknown1047(25000)
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_05', 2)	# 36-37
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('RollingAttackEff', 0)
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg401_06', 3)	# 38-40	 **attackbox here**
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    SFX_0('213_bound_1')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_08', 1)	# 41-41
    sprite('tg401_08', 2)	# 42-43
    Unknown1051(25)
    sprite('tg401_09', 3)	# 44-46
    sprite('tg401_10', 3)	# 47-49
    Unknown1084(1)
    sprite('tg401_11', 3)	# 50-52
    sprite('tg401_12', 3)	# 53-55
    sprite('tg401_13', 3)	# 56-58
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsca_00():

    def upon_IMMEDIATE():
        Unknown2037(10)

        def upon_3():
            if SLOT_2:
                Unknown2038(-1)
                if (SLOT_2 <= 0):
                    sendToLabel(1)
                    Unknown61(0, 10, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0)
                    SLOT_2 = SLOT_0
                    SFX_0('014_electric_s')
                    SFX_0('014_electric_l')
                    GFX_0('StayMagneticA', 0)
                    GFX_0('StayMagneticA', 1)
    sprite('tg401_00', 4)	# 1-4
    sprite('tg401_01', 4)	# 5-8
    sprite('tg401_02', 4)	# 9-12
    label(0)
    sprite('tg401_03', 32767)	# 13-32779
    loopRest()
    label(1)
    sprite('tg401_03', 2)	# 32780-32781
    loopRest()
    gotoLabel(0)

@State
def Act3Event_tgvsca_01():
    sprite('tg401_02', 6)	# 1-6
    sprite('tg401_01', 6)	# 7-12
    sprite('tg401_00', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsmk_00():

    def upon_IMMEDIATE():
        Unknown1000(-210000)
    sprite('keep', 1)	# 1-1
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsmk_01():
    sprite('tg300_05', 8)	# 1-8
    sprite('tg300_06', 8)	# 9-16
    loopRest()
    enterState('Act3Event_tgvsmk_02')

@State
def Act3Event_tgvsmk_02():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)

        def upon_STATE_END():
            Unknown1084(1)
            Unknown1000(-260000)
    label(9)
    sprite('tg000_00', 6)	# 1-6
    sprite('tg000_01', 6)	# 7-12
    sprite('tg000_02', 6)	# 13-18
    sprite('tg000_03', 6)	# 19-24
    sprite('tg000_04', 6)	# 25-30
    sprite('tg000_05', 6)	# 31-36
    sprite('tg000_06', 6)	# 37-42
    sprite('tg000_05', 6)	# 43-48
    sprite('tg000_04', 6)	# 49-54
    sprite('tg000_03', 6)	# 55-60
    sprite('tg000_02', 6)	# 61-66
    sprite('tg000_01', 6)	# 67-72
    sprite('tg000_00', 6)	# 73-78
    sprite('tg000_01', 6)	# 79-84
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    GFX_0('StayMagneticA', 6)
    GFX_0('StayMagneticA', 7)
    sprite('tg000_02', 6)	# 85-90
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    GFX_0('StayMagneticA', 5)
    sprite('tg000_03', 6)	# 91-96
    sprite('tg000_04', 6)	# 97-102
    sprite('tg000_05', 6)	# 103-108
    sprite('tg000_06', 6)	# 109-114
    sprite('tg000_05', 6)	# 115-120
    sprite('tg000_04', 6)	# 121-126
    sprite('tg000_03', 6)	# 127-132
    sprite('tg000_02', 6)	# 133-138
    sprite('tg000_01', 6)	# 139-144
    sprite('tg000_00', 6)	# 145-150
    sprite('tg000_01', 6)	# 151-156
    sprite('tg000_02', 6)	# 157-162
    sprite('tg000_03', 6)	# 163-168
    sprite('tg000_04', 6)	# 169-174
    sprite('tg000_05', 6)	# 175-180
    sprite('tg000_06', 6)	# 181-186
    sprite('tg000_05', 6)	# 187-192
    sprite('tg000_04', 6)	# 193-198
    sprite('tg000_03', 6)	# 199-204
    sprite('tg000_02', 6)	# 205-210
    sprite('tg000_01', 6)	# 211-216
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('tg040_00', 3)	# 217-219
    sprite('tg040_01', 3)	# 220-222
    sprite('tg040_02', 19)	# 223-241
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('104_guard_grap_2')
    ScreenShake(5000, 20000)
    sprite('tg040_02', 14)	# 242-255
    Unknown1047(-6000)
    sprite('tg040_01', 7)	# 256-262
    sprite('tg040_00', 7)	# 263-269
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsmk_03():
    sprite('tg001_00', 8)	# 1-8
    sprite('tg001_01', 8)	# 9-16
    sprite('tg001_02', 8)	# 17-24
    sprite('tg001_03', 8)	# 25-32
    SFX_3('tgse_00')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000000000000')
    Unknown4048(300000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000001000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000002000000')
    Unknown4048(210000)
    Unknown4045('746765665f73746561420000000000000000000000000000000000000000000003000000')
    sprite('tg001_04', 8)	# 33-40
    sprite('tg001_05', 8)	# 41-48
    sprite('tg001_06', 8)	# 49-56
    sprite('tg001_07', 8)	# 57-64
    sprite('tg001_08', 8)	# 65-72
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsmk_04():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('tg213_03', 4)	# 1-4	 **attackbox here**
    GFX_0('StayMagneticB', 0)
    sprite('tg213_04', 11)	# 5-15	 **attackbox here**
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    GFX_0('tgef213mc', 0)
    Unknown4048(290000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000001000000')
    Unknown4048(250000)
    Unknown4045('746765665f73746561410000000000000000000000000000000000000000000002000000')
    sprite('tg213_05', 2)	# 16-17	 **attackbox here**
    GFX_0('StayMagneticB', 0)
    GFX_0('StayMagneticB', 1)
    GFX_0('StayMagneticB', 2)
    sprite('tg213_06', 4)	# 18-21
    sprite('tg213_07', 4)	# 22-25
    sprite('tg213_08', 4)	# 26-29
    sprite('tg213_09', 4)	# 30-33
    sprite('tg213_10', 4)	# 34-37
    sprite('tg213_11', 4)	# 38-41
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsmk_05():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('tg030_00', 6)	# 1-6
    physicsXImpulse(4800)
    Unknown2037(5)
    label(0)
    sprite('tg030_01', 6)	# 7-12
    Unknown2038(-1)
    sprite('tg030_02', 6)	# 13-18
    sprite('tg030_03', 6)	# 19-24
    sprite('tg030_04', 6)	# 25-30
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 6)	# 31-36
    sprite('tg030_06', 6)	# 37-42
    sprite('tg030_07', 6)	# 43-48
    sprite('tg030_08', 6)	# 49-54
    sprite('tg030_09', 6)	# 55-60
    sprite('tg030_10', 6)	# 61-66
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 6)	# 67-72
    sprite('tg030_12', 6)	# 73-78
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('null', 32767)	# 79-32845
    Unknown3038(1)
    Unknown1084(1)

@State
def Act3Event_tgvsno_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1000(-960000)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 260000):
                    clearUponHandler(3)
                    Unknown1000(-260000)
                    Unknown1084(1)
                    sendToLabel(0)
            elif (SLOT_22 > (-260000)):
                clearUponHandler(3)
                Unknown1000(-260000)
                Unknown1084(1)
                sendToLabel(0)
    sprite('tg030_00', 6)	# 1-6
    physicsXImpulse(4800)
    label(9)
    sprite('tg030_01', 6)	# 7-12
    sprite('tg030_02', 6)	# 13-18
    sprite('tg030_03', 6)	# 19-24
    sprite('tg030_04', 6)	# 25-30
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 6)	# 31-36
    sprite('tg030_06', 6)	# 37-42
    sprite('tg030_07', 6)	# 43-48
    sprite('tg030_08', 6)	# 49-54
    sprite('tg030_09', 6)	# 55-60
    sprite('tg030_10', 6)	# 61-66
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 6)	# 67-72
    sprite('tg030_12', 6)	# 73-78
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('tg030_00', 3)	# 79-81
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsno_01():
    sprite('tg030_00', 6)	# 1-6
    physicsXImpulse(2000)
    sprite('tg030_01', 6)	# 7-12
    sprite('tg030_02', 6)	# 13-18
    sprite('tg030_03', 6)	# 19-24
    sprite('tg030_04', 6)	# 25-30
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_01', 3)	# 31-33
    Unknown1084(1)
    sprite('tg030_00', 3)	# 34-36
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_tgvsno_02():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown1084(1)
            Unknown1000(-260000)
    sprite('tg040_00', 3)	# 1-3
    sprite('tg040_01', 3)	# 4-6
    sprite('tg040_02', 16)	# 7-22
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('104_guard_grap_2')
    ScreenShake(5000, 20000)
    sprite('tg040_02', 14)	# 23-36
    Unknown1047(-6000)
    sprite('tg040_01', 7)	# 37-43
    sprite('tg040_00', 7)	# 44-50
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsno_03():

    def upon_IMMEDIATE():
        Unknown2017(0)
        Unknown2034(0)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 0):
                    clearUponHandler(3)
                    Unknown1084(1)
                    sendToLabel(0)
            elif (SLOT_22 > 0):
                clearUponHandler(3)
                Unknown1084(1)
                sendToLabel(0)
    sprite('tg030_00', 6)	# 1-6
    physicsXImpulse(4800)
    label(9)
    sprite('tg030_01', 6)	# 7-12
    sprite('tg030_02', 6)	# 13-18
    sprite('tg030_03', 6)	# 19-24
    sprite('tg030_04', 6)	# 25-30
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_05', 6)	# 31-36
    sprite('tg030_06', 6)	# 37-42
    sprite('tg030_07', 6)	# 43-48
    sprite('tg030_08', 6)	# 49-54
    sprite('tg030_09', 6)	# 55-60
    sprite('tg030_10', 6)	# 61-66
    SFX_FOOTSTEP_(0, 1, 1)
    sprite('tg030_11', 6)	# 67-72
    sprite('tg030_12', 6)	# 73-78
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('tg600_11', 6)	# 79-84
    sprite('tg600_10', 6)	# 85-90
    sprite('tg600_09', 6)	# 91-96
    sprite('tg600_08', 6)	# 97-102
    sprite('tg600_07', 6)	# 103-108
    sprite('tg600_06', 6)	# 109-114
    sprite('tg600_05', 32767)	# 115-32881

@State
def Act3Event_muvstg_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('tg040_02', 7)	# 1-7
    sprite('tg090_00', 19)	# 8-26
    Unknown4045('65665f67697264627265616b000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    SFX_0('106_guard_crush')
    ScreenShake(3000, 20000)
    sprite('tg090_01', 3)	# 27-29
    Unknown1047(-11000)
    sprite('tg090_02', 18)	# 30-47
    sprite('tg090_03', 5)	# 48-52
    sprite('tg090_04', 6)	# 53-58
    sprite('tg620_00', 6)	# 59-64
    Unknown1084(1)
    sprite('tg620_01', 6)	# 65-70
    SFX_3('tgse_03')
    sprite('tg620_02', 20)	# 71-90
    sprite('tg620_03', 8)	# 91-98
    sprite('tg620_04', 8)	# 99-106
    sprite('tg620_05', 12)	# 107-118
    sprite('tg620_06', 6)	# 119-124
    SFX_3('tgse_04')
    sprite('tg620_07', 32767)	# 125-32891
    Unknown8000(0, 1, 0)
    SFX_0('209_down_normal_1')
    ScreenShake(0, 10000)

@State
def Act3Event_mkvstg_00():

    def upon_IMMEDIATE():
        Unknown2003(1)

        def upon_STATE_END():
            Unknown1000(-260000)
    sprite('tg401_04', 4)	# 1-4
    teleportRelativeX(100000)
    SFX_0('005_swing_grap_2_2')
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_05', 3)	# 5-7
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    GFX_0('RollingAttackEff', 0)
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    GFX_0('StayMagneticA', 3)
    GFX_0('StayMagneticA', 4)
    sprite('tg401_06', 3)	# 8-10	 **attackbox here**
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    SFX_0('213_bound_1')
    GFX_0('StayMagneticA', 0)
    GFX_0('StayMagneticA', 1)
    GFX_0('StayMagneticA', 2)
    sprite('tg401_08', 4)	# 11-14
    sprite('tg401_09', 4)	# 15-18
    sprite('tg401_10', 4)	# 19-22
    sprite('tg401_11', 4)	# 23-26
    teleportRelativeX(-30000)
    sprite('tg401_12', 4)	# 27-30
    teleportRelativeX(-30000)
    sprite('tg401_13', 4)	# 31-34
    teleportRelativeX(-30000)
    loopRest()
    enterState('Act3Event_Stand')

@State
def Act3Event_mkvstg_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('tg000_00', 7)	# 1-7
    sprite('tg070_00', 17)	# 8-24
    GFX_1('ef_hitmd', 103)
    SFX_0('100_hit_grap_1')
    ScreenShake(1000, 20000)
    sprite('tg070_00', 4)	# 25-28
    Unknown1047(-11000)
    sprite('tg070_01', 4)	# 29-32
    sprite('tg070_02', 4)	# 33-36
    sprite('tg070_03', 32767)	# 37-32803

@State
def Act3Event_mkvstg_02():
    sprite('tg070_14', 6)	# 1-6
    sprite('tg070_15', 6)	# 7-12
    sprite('tg070_16', 6)	# 13-18
    sprite('tg620_00', 5)	# 19-23
    sprite('tg620_01', 5)	# 24-28
    SFX_3('tgse_03')
    sprite('tg620_02', 6)	# 29-34
    sprite('tg620_03', 20)	# 35-54
    sprite('tg620_04', 8)	# 55-62
    sprite('tg620_05', 12)	# 63-74
    sprite('tg620_06', 6)	# 75-80
    SFX_3('tgse_04')
    sprite('tg620_07', 32767)	# 81-32847
    Unknown8000(0, 1, 0)
    SFX_0('209_down_normal_1')
    ScreenShake(0, 10000)

@State
def Act3Event_rlvstg_00():

    def upon_IMMEDIATE():
        loopRelated(17, 360)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown2034(0)
    sprite('tg003_00', 3)	# 1-3
    Unknown2005()
    sprite('tg404_23', 3)	# 4-6
    Unknown2005()
    sprite('tg404_22', 3)	# 7-9
    sprite('tg404_21', 3)	# 10-12
    sprite('tg432_19', 3)	# 13-15
    teleportRelativeX(-680000)
    sprite('tg432_20', 6)	# 16-21
    sprite('tg432_21', 12)	# 22-33
    sprite('tg432_24', 6)	# 34-39
    teleportRelativeX(560000)
    ScreenShake(0, 20000)
    Unknown8002()
    GFX_0('GETBJumpEFF', 0)
    physicsYImpulse(100000)
    Unknown8001(3, 0)
    label(5)
    sprite('tg432_25', 6)	# 40-45
    sprite('tg432_24', 6)	# 46-51
    loopRest()
    gotoLabel(5)
    label(1)
    sprite('null', 32767)	# 52-32818
    physicsYImpulse(0)

@State
def Act3Event_rlvstg_01():

    def upon_IMMEDIATE():
        Unknown1000(100000)
    sprite('tg620_00', 4)	# 1-4
    SFX_0('104_guard_grap_1')
    ScreenShake(3000, 18000)
    Unknown1047(-40000)
    SFX_0('015_blaze_2')
    SFX_0('015_blaze_1')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('tg620_01', 4)	# 5-8
    SFX_3('tgse_03')
    sprite('tg620_02', 6)	# 9-14
    sprite('tg620_03', 8)	# 15-22
    sprite('tg620_06', 32767)	# 23-32789
    Unknown1084(1)
    loopRest()
    enterState('CmnActStand')