@Subroutine
def PreInit():
    Unknown12019('62657300000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFAccel(1000)
    DashFMaxVelocity(32000)
    JumpYVelocity(30000)
    SuperJumpYVelocity(37000)
    Unknown12011(1500)
    Unknown12038(23000)
    Unknown12036(-1500)
    Unknown12024(1)
    Unknown13039(1)
    Unknown2049(1)
    Unknown15018(2000)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    Unknown15013(2000)
    Unknown14015(0, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Unknown14015(200000, 500000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown15013(2000)
    Unknown14015(-50000, 250000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown14015(0, 450000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown15013(2000)
    Unknown14015(0, 350000, -200000, 125000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    Unknown15013(2000)
    Unknown14015(0, 400000, -100000, 100000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(5000)
    Unknown14015(-200000, 300000, 200000, 500000, 300, 5)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15014(0)
    Unknown15013(0)
    Unknown14015(0, 350000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(0)
    Unknown14015(0, 500000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15013(2500)
    Unknown14015(0, 450000, -100000, 300000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown14015(0, 450000, -250000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(-350000, 400000, -400000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-250000, 350000, -900000, -300000, 3000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 250000, -200000, 100000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 250000, -200000, 100000, 1200, 0)
    Move_EndRegister()
    Move_Register('ShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(0)
    Unknown15014(0)
    Unknown15013(0)
    Unknown15011(10000)
    Unknown14015(800000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(0)
    Unknown15014(0)
    Unknown15013(0)
    Unknown15011(10000)
    Unknown14015(800000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('ShotEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15021(0)
    Unknown15014(0)
    Unknown15013(0)
    Unknown15011(10000)
    Unknown14015(800000, 1200000, -200000, 200000, 500, 10)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('ShotA_2nd', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15021(0)
    Unknown15014(0)
    Unknown15013(5000)
    Unknown14015(800000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('ShotB_2nd', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15021(0)
    Unknown15014(0)
    Unknown15013(5000)
    Unknown14015(800000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AirShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('EnableAirShot')
    Unknown15021(0)
    Unknown15013(0)
    Unknown14015(450000, 800000, -500000, -200000, 250, 10)
    Move_EndRegister()
    Move_Register('AirShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14024('EnableAirShot')
    Unknown15021(0)
    Unknown15013(0)
    Unknown14015(800000, 1200000, -400000, -100000, 250, 10)
    Move_EndRegister()
    Move_Register('AirShotEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14024('EnableAirShot')
    Unknown15021(0)
    Unknown15013(0)
    Unknown14015(450000, 800000, -500000, -200000, 250, 10)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('AirShotA_2nd', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14015(350000, 900000, -700000, -100000, 10000, 10)
    Move_EndRegister()
    Move_Register('AirShotB_2nd', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14015(700000, 1300000, -700000, -100000, 10000, 10)
    Move_EndRegister()
    Move_Register('SpecialThrow', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15010()
    Unknown15014(0)
    Unknown15021(0)
    Unknown15012(6000)
    Unknown14015(200000, 450000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('MidAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15016(1, 15, 40)
    Unknown15008()
    Unknown15014(0)
    Unknown15013(4000)
    Unknown15012(4000)
    Unknown15025('000000000000000001000000e8030000c4090000')
    Unknown14015(300000, 550000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(500)
    Unknown15012(500)
    Unknown15025('000000000000000001000000e8030000d0070000')
    Unknown14015(0, 400000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_2nd', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15012(1)
    Unknown14015(0, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(1)
    Unknown15025('000000000000000001000000e8030000b80b0000')
    Unknown14015(0, 400000, -200000, 150000, 200, 0)
    Move_EndRegister()
    Move_Register('AntiAir2nd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15012(1)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15013(4000)
    Unknown15012(1)
    Unknown15025('000000000000000001000000e8030000d0070000')
    Unknown14015(-200000, 450000, 50000, 350000, 250, 0)
    Move_EndRegister()
    Move_Register('AirAntiAir2nd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15012(1)
    Move_EndRegister()
    Move_Register('UltimateShot_LandA', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(0)
    Unknown15013(0)
    Unknown14015(700000, 1200000, -200000, 100000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateShot_LandAOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(0)
    Unknown15013(0)
    Unknown14015(700000, 1200000, -200000, 100000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(0)
    Unknown14015(0, 450000, -200000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(0)
    Unknown14015(0, 450000, -200000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateShot_AirA', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(0)
    Unknown15013(0)
    Unknown14015(700000, 1200000, -200000, 100000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateShot_AirAOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(0)
    Unknown15013(0)
    Unknown14015(700000, 1200000, -200000, 100000, 500, 10)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Move_EndRegister()
    Unknown15024('NmlAtk4A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 20000000)
    Unknown15024('NmlAtk5A3rd', 'Assault', 10000000)
    Unknown15024('NmlAtk5A3rd', 'UltimateAssault', 3000000)
    Unknown15024('NmlAtk5A3rd', 'UltimateAssaultOD', 3000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'Assault', 10000000)
    Unknown15024('NmlAtk5B2nd', 'UltimateAssault', 3000000)
    Unknown15024('NmlAtk5B2nd', 'UltimateAssaultOD', 3000000)
    Unknown15024('Assault', 'Assault_2nd', 10000000)
    Unknown15024('NmlAtk2C', 'Assault', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateAssault', 3000000)
    Unknown15024('NmlAtk2C', 'UltimateAssaultOD', 3000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A2nd', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'CmnActInvincibleAttackAir', 1000000)
    Unknown15024('CmnActInvincibleAttackAir', 'AirAntiAir2nd', 1000000)
    Unknown15024('BackThrowExe', 'SpecialThrow', 10000000)
    Unknown12018(0, 'es062_01')
    Unknown12018(1, 'es062_03')
    Unknown12018(2, 'es062_04')
    Unknown12018(3, 'es062_05')
    Unknown12018(4, 'es062_05')
    Unknown12018(5, 'es062_06')
    Unknown12018(6, 'es062_07')
    Unknown12018(7, 'es041_02')
    Unknown12018(8, 'es040_02')
    Unknown12018(9, 'es045_02')
    Unknown12018(10, 'es060_00')
    Unknown12018(11, 'es060_01')
    Unknown12018(12, 'es060_03')
    Unknown12018(13, 'es060_05')
    Unknown12018(14, 'es060_07')
    Unknown12018(15, 'es060_14')
    Unknown12018(16, 'es050_00')
    Unknown12018(17, 'es052_00')
    Unknown12018(18, 'es054_00')
    Unknown12018(19, 'es000_00')
    Unknown12018(20, 'es000_00')
    Unknown12018(25, 'es063_00')
    Unknown12018(26, 'es063_01')
    Unknown12018(27, 'es063_02')
    Unknown12018(28, 'es063_04')
    Unknown12018(29, 'es063_10')
    Unknown12018(24, 'es073_01')
    Unknown7010(0, 'bes000')
    Unknown7010(1, 'bes001')
    Unknown7010(2, 'bes002')
    Unknown7010(3, 'bes003')
    Unknown7010(4, 'bes004')
    Unknown7010(5, 'bes005')
    Unknown7010(6, 'bes006')
    Unknown7010(7, 'bes007')
    Unknown7010(8, 'bes008')
    Unknown7010(9, 'bes009')
    Unknown7010(10, 'bes010')
    Unknown7010(15, 'bes011')
    Unknown7010(16, 'bes012')
    Unknown7010(17, 'bes013')
    Unknown7010(18, 'bes014')
    Unknown7010(19, 'bes015')
    Unknown7010(20, 'bes016')
    Unknown7010(21, 'bes017')
    Unknown7010(22, 'bes018')
    Unknown7010(23, 'bes019')
    Unknown7010(24, 'bes020')
    Unknown7010(25, 'bes021')
    Unknown7010(28, 'bes022')
    Unknown7010(29, 'bes023')
    Unknown7010(30, 'bes024')
    Unknown7010(31, 'bes025')
    Unknown7010(32, 'bes026')
    Unknown7010(33, 'bes027')
    Unknown7010(34, 'bes028')
    Unknown7010(35, 'bes029')
    Unknown7010(36, 'bes030')
    Unknown7010(37, 'bes031')
    Unknown7010(39, 'bes032')
    Unknown7010(42, 'bes033')
    Unknown7010(43, 'bes034')
    Unknown7010(44, 'bes035')
    Unknown7010(45, 'bes036')
    Unknown7010(46, 'bes037')
    Unknown7010(47, 'bes038')
    Unknown7010(48, 'bes039')
    Unknown7010(49, 'bes040')
    Unknown7010(50, 'bes041')
    Unknown7010(52, 'bes042')
    Unknown7010(53, 'bes043')
    Unknown7010(54, 'bes100_0')
    Unknown7010(55, 'bes100_1')
    Unknown7010(56, 'bes100_2')
    Unknown7010(63, 'bes101_0')
    Unknown7010(64, 'bes101_1')
    Unknown7010(65, 'bes101_2')
    Unknown7010(57, 'bes102_0')
    Unknown7010(58, 'bes102_1')
    Unknown7010(59, 'bes102_2')
    Unknown7010(66, 'bes103_0')
    Unknown7010(67, 'bes103_1')
    Unknown7010(68, 'bes103_2')
    Unknown7010(60, 'bes104_0')
    Unknown7010(61, 'bes104_1')
    Unknown7010(62, 'bes104_2')
    Unknown7010(69, 'bes105_0')
    Unknown7010(70, 'bes105_1')
    Unknown7010(71, 'bes105_2')
    Unknown7010(72, 'bes150')
    Unknown7010(73, 'bes151')
    Unknown7010(74, 'bes152')
    Unknown7010(85, 'bes153')
    Unknown7010(87, 'bes154')
    Unknown7010(88, 'bes155')
    Unknown7010(96, 'bes161_0')
    Unknown7010(97, 'bes161_1')
    Unknown7010(92, 'bes162_0')
    Unknown7010(93, 'bes162_1')
    Unknown7010(98, 'bes163_0')
    Unknown7010(99, 'bes163_1')
    Unknown7010(100, 'bes164_0')
    Unknown7010(101, 'bes164_1')
    Unknown7010(105, 'bes165_0')
    Unknown7010(106, 'bes165_1')
    Unknown7010(102, 'bes166_0')
    Unknown7010(103, 'bes166_1')
    Unknown7010(90, 'bes167_0')
    Unknown7010(91, 'bes167_1')
    Unknown7010(107, 'bes168_0')
    Unknown7010(108, 'bes168_1')
    Unknown7010(110, 'bes169_0')
    Unknown7010(111, 'bes169_1')
    Unknown7010(94, 'bes400_0')
    Unknown7010(95, 'bes400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f745f4c616e64410000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745f4c616e64414f44000000000000000000000000')
    Unknown12059('04000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746541737361756c744f44000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if (not SLOT_158):
        Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006e00000000000000')
        Unknown26('esef_431Camera')

@Subroutine
def MatchInit2():
    Unknown30007('00000000')
    Unknown30011('')

@Subroutine
def ChageAtk_flash():
    Unknown23030('65735f7370656369616c5f666c617368000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def EXkeizokuEff():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3072('80000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    Unknown3074('000000000400000032000000a0000000')
    Unknown3075('00000000000000000000000010000000')
    Unknown3076(1010)
    Unknown3077(900)

@Subroutine
def EnableAirShot():
    SLOT_47 = 0
    if (not SLOT_59):
        SLOT_47 = 1

@Subroutine
def OnLanding():
    SLOT_59 = 0

@State
def CmnActStand():
    label(0)
    sprite('es000_00', 7)	# 1-7
    sprite('es000_01', 7)	# 8-14
    sprite('es000_02', 7)	# 15-21
    sprite('es000_03', 7)	# 22-28
    sprite('es000_04', 7)	# 29-35
    sprite('es000_05', 7)	# 36-42
    sprite('es000_06', 7)	# 43-49
    sprite('es000_07', 7)	# 50-56
    sprite('es000_08', 7)	# 57-63
    sprite('es000_09', 7)	# 64-70
    sprite('es000_10', 7)	# 71-77
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('es001_00', 6)	# 78-83
    SLOT_88 = 960
    sprite('es001_01', 6)	# 84-89
    sprite('es001_02', 6)	# 90-95
    sprite('es001_03', 6)	# 96-101
    GFX_0('esef_001', 0)
    Unknown36(1)
    Unknown1072(65000)
    Unknown35()
    SFX_3('esse_08')
    GFX_0('esef_001_tame_add', 0)
    GFX_0('esef_001_tame_add', 1)
    GFX_0('esef_001_tame_add', 2)
    SFX_4('bes000')
    sprite('es001_04', 6)	# 102-107
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 108-113
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 114-119
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 120-125
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 126-131
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 132-137
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 138-143
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 144-149
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 150-155
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 156-161
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 162-167
    sprite('es001_02', 6)	# 168-173
    sprite('es001_01', 6)	# 174-179
    sprite('es001_00', 6)	# 180-185
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('es003_00', 3)	# 1-3
    sprite('es003_01', 2)	# 4-5
    sprite('es003_01ex00', 2)	# 6-7
    sprite('es003_00ex00', 3)	# 8-10

@State
def CmnActStand2Crouch():
    sprite('es010_00', 4)	# 1-4
    sprite('es010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('es010_02', 6)	# 1-6
    sprite('es010_03', 6)	# 7-12
    sprite('es010_04', 6)	# 13-18
    sprite('es010_05', 6)	# 19-24
    sprite('es010_06', 6)	# 25-30
    sprite('es010_07', 6)	# 31-36
    sprite('es010_08', 6)	# 37-42
    sprite('es010_09', 6)	# 43-48
    sprite('es010_10', 6)	# 49-54
    sprite('es010_11', 6)	# 55-60
    sprite('es010_12', 6)	# 61-66
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('es013_00', 3)	# 1-3
    sprite('es013_01', 2)	# 4-5
    sprite('es013_01ex00', 2)	# 6-7
    sprite('es013_00ex00', 3)	# 8-10

@State
def CmnActCrouch2Stand():
    sprite('es010_01', 4)	# 1-4
    sprite('es010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('es023_00', 2)	# 1-2
    sprite('es023_01', 2)	# 3-4
    if SLOT_37:
        if SLOT_93:
            if SLOT_16:
                Unknown1045(15000)

@State
def CmnActJumpUpper():
    label(0)
    sprite('es020_00', 4)	# 1-4
    sprite('es020_01', 4)	# 5-8
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('es020_02', 3)	# 1-3
    sprite('es020_03', 3)	# 4-6
    sprite('es020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('es020_05', 3)	# 1-3
    sprite('es020_06', 3)	# 4-6
    label(0)
    sprite('es020_07', 4)	# 7-10
    sprite('es020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('es024_00', 3)	# 1-3
    sprite('es024_01', 3)	# 4-6
    sprite('es024_02', 3)	# 7-9
    sprite('es024_03', 3)	# 10-12
    sprite('es024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('es024_00', 2)	# 1-2
    sprite('es024_01', 2)	# 3-4
    sprite('es024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('es024_03', 3)	# 1-3
    sprite('es024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('es030_00', 7)	# 1-7
    label(0)
    sprite('es030_01', 7)	# 8-14
    sprite('es030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('es030_03', 7)	# 22-28
    sprite('es030_04', 7)	# 29-35
    sprite('es030_05', 7)	# 36-42
    sprite('es030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('es030_07', 7)	# 50-56
    sprite('es030_08', 7)	# 57-63
    sprite('es030_09', 7)	# 64-70
    sprite('es030_10', 7)	# 71-77
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('es031_00', 7)	# 1-7
    label(0)
    sprite('es031_01', 7)	# 8-14
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('es031_02', 7)	# 15-21
    sprite('es031_03', 7)	# 22-28
    sprite('es031_04', 7)	# 29-35
    sprite('es031_05', 7)	# 36-42
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('es031_06', 7)	# 43-49
    sprite('es031_07', 7)	# 50-56
    sprite('es031_08', 7)	# 57-63
    sprite('es031_09', 7)	# 64-70
    sprite('es031_10', 7)	# 71-77
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            if (SLOT_18 <= 5):
                Unknown1019(25)
    sprite('es030_01', 2)	# 1-2
    sprite('es030_02', 3)	# 3-5
    sprite('es032_00', 3)	# 6-8
    sprite('es032_01', 2)	# 9-10
    label(0)
    sprite('es032_02', 4)	# 11-14
    sprite('es032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('es032_04', 4)	# 19-22
    sprite('es032_05', 4)	# 23-26
    sprite('es032_06', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('es032_07', 4)	# 31-34
    sprite('es032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():

    def upon_IMMEDIATE():
        Unknown13019(1)

        def upon_3():
            if (SLOT_18 == 4):
                Unknown13005(1)
                Unknown13001(1)
    sprite('es032_09', 3)	# 1-3
    sprite('es032_10', 3)	# 4-6
    sprite('es032_11', 3)	# 7-9
    sprite('es032_12', 3)	# 10-12

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
    sprite('es033_00', 1)	# 1-1
    sprite('es033_00', 2)	# 2-3
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    SFX_4('bes005')
    sprite('es033_01', 2)	# 4-5
    sprite('es033_02', 1)	# 6-6
    sprite('es033_02', 2)	# 7-8
    sprite('es033_03', 3)	# 9-11
    sprite('es033_04', 3)	# 12-14
    sprite('es033_05', 32767)	# 15-32781
    label(1)
    sprite('es033_06', 3)	# 32782-32784
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('es033_07', 3)	# 32785-32787
    sprite('es033_08', 3)	# 32788-32790

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        Unknown48('19000000020000003300000019000000020000000d000000')
        Unknown1022()
    sprite('es035_00', 3)	# 1-3
    Unknown1023()
    Unknown1021(180000)
    YAccel(10)
    sprite('es035_01', 3)	# 4-6
    sprite('es035_02', 3)	# 7-9
    sprite('es035_03', 2)	# 10-11
    sprite('es035_04', 2)	# 12-13
    sprite('es035_05', 2)	# 14-15
    sprite('es035_06', 2)	# 16-17
    sprite('es035_07', 2)	# 18-19

@State
def CmnActAirBDash():
    sprite('es036_00', 3)	# 1-3
    label(0)
    sprite('es036_01', 3)	# 4-6
    sprite('es036_02', 3)	# 7-9
    sprite('es036_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('es050_00', 1)	# 1-1
    sprite('es050_01', 1)	# 2-2
    sprite('es050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('es050_01', 1)	# 1-1
    sprite('es050_02', 1)	# 2-2
    sprite('es050_01', 2)	# 3-4
    sprite('es050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('es050_02', 1)	# 1-1
    sprite('es050_03', 1)	# 2-2
    sprite('es050_02', 2)	# 3-4
    sprite('es050_01', 2)	# 5-6
    sprite('es050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('es050_03', 1)	# 1-1
    sprite('es050_04', 1)	# 2-2
    sprite('es050_03', 2)	# 3-4
    sprite('es050_02', 2)	# 5-6
    sprite('es050_01', 2)	# 7-8
    sprite('es050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('es050_04', 1)	# 1-1
    sprite('es050_04', 1)	# 2-2
    sprite('es050_04', 2)	# 3-4
    sprite('es050_03', 2)	# 5-6
    sprite('es050_02', 2)	# 7-8
    sprite('es050_01', 2)	# 9-10
    sprite('es050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('es052_00', 1)	# 1-1
    sprite('es052_01', 1)	# 2-2
    sprite('es052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('es052_01', 1)	# 1-1
    sprite('es052_02', 1)	# 2-2
    sprite('es052_01', 2)	# 3-4
    sprite('es052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('es052_02', 1)	# 1-1
    sprite('es052_03', 1)	# 2-2
    sprite('es052_02', 2)	# 3-4
    sprite('es052_01', 2)	# 5-6
    sprite('es052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('es052_03', 1)	# 1-1
    sprite('es052_04', 1)	# 2-2
    sprite('es052_03', 2)	# 3-4
    sprite('es052_02', 2)	# 5-6
    sprite('es052_01', 2)	# 7-8
    sprite('es052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('es052_04', 1)	# 1-1
    sprite('es052_04', 1)	# 2-2
    sprite('es052_04', 2)	# 3-4
    sprite('es052_03', 2)	# 5-6
    sprite('es052_02', 2)	# 7-8
    sprite('es052_01', 2)	# 9-10
    sprite('es052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('es054_00', 1)	# 1-1
    sprite('es054_01', 1)	# 2-2
    sprite('es054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('es054_01', 1)	# 1-1
    sprite('es054_02', 1)	# 2-2
    sprite('es054_01', 2)	# 3-4
    sprite('es054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('es054_02', 1)	# 1-1
    sprite('es054_03', 1)	# 2-2
    sprite('es054_02', 2)	# 3-4
    sprite('es054_01', 2)	# 5-6
    sprite('es054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('es054_03', 1)	# 1-1
    sprite('es054_04', 1)	# 2-2
    sprite('es054_03', 2)	# 3-4
    sprite('es054_02', 2)	# 5-6
    sprite('es054_01', 2)	# 7-8
    sprite('es054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('es054_04', 1)	# 1-1
    sprite('es054_04', 1)	# 2-2
    sprite('es054_04', 2)	# 3-4
    sprite('es054_03', 2)	# 5-6
    sprite('es054_02', 2)	# 7-8
    sprite('es054_01', 2)	# 9-10
    sprite('es054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('es060_00', 4)	# 1-4
    label(0)
    sprite('es060_01', 4)	# 5-8
    sprite('es060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('es062_03', 3)	# 1-3
    sprite('es062_04', 3)	# 4-6

@State
def CmnActBDownDown():
    sprite('es062_05', 3)	# 1-3
    sprite('es062_06', 3)	# 4-6
    label(0)
    sprite('es062_07', 3)	# 7-9
    sprite('es062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('es063_04', 3)	# 1-3
    sprite('es063_05', 3)	# 4-6

@State
def CmnActBDownBound():
    sprite('es063_06', 2)	# 1-2
    sprite('es063_07', 2)	# 3-4
    sprite('es063_08', 3)	# 5-7
    sprite('es063_09', 3)	# 8-10
    sprite('es063_10', 3)	# 11-13

@State
def CmnActBDownLoop():
    sprite('es063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('es064_00', 3)	# 1-3
    sprite('es064_01', 3)	# 4-6
    sprite('es064_02', 3)	# 7-9
    sprite('es064_03', 3)	# 10-12
    sprite('es064_04', 3)	# 13-15
    sprite('es064_05', 3)	# 16-18
    sprite('es064_06', 3)	# 19-21
    sprite('es064_07', 3)	# 22-24
    sprite('es064_08', 3)	# 25-27

@State
def CmnActFDownUpper():
    sprite('es063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('es063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('es063_02', 3)	# 1-3
    sprite('es063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('es063_04', 3)	# 1-3
    sprite('es063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('es063_06', 2)	# 1-2
    sprite('es063_07', 2)	# 3-4
    sprite('es063_08', 3)	# 5-7
    sprite('es063_09', 3)	# 8-10
    sprite('es063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('es063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('es064_00', 3)	# 1-3
    sprite('es064_01', 3)	# 4-6
    sprite('es064_02', 3)	# 7-9
    sprite('es064_03', 3)	# 10-12
    sprite('es064_04', 3)	# 13-15
    sprite('es064_05', 3)	# 16-18
    sprite('es064_06', 3)	# 19-21
    sprite('es064_07', 3)	# 22-24
    sprite('es064_08', 3)	# 25-27

@State
def CmnActVDownUpper():
    sprite('es062_00', 3)	# 1-3
    label(0)
    sprite('es062_01', 3)	# 4-6
    sprite('es062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('es062_03', 3)	# 1-3
    sprite('es062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('es062_05', 3)	# 1-3
    sprite('es062_06', 3)	# 4-6
    label(0)
    sprite('es062_07', 3)	# 7-9
    sprite('es062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('es062_09', 2)	# 1-2
    sprite('es062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('es072_00', 3)	# 1-3
    sprite('es072_01', 3)	# 4-6
    sprite('es072_02', 3)	# 7-9
    label(0)
    sprite('es072_01', 3)	# 10-12
    sprite('es072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('es074_00', 3)	# 1-3
    sprite('es074_01', 3)	# 4-6
    sprite('es074_02', 3)	# 7-9
    sprite('es074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    pass

@State
def CmnActFreeze():
    sprite('es071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('es073_00', 3)	# 1-3
    sprite('es073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('es073_02', 3)	# 1-3
    label(0)
    sprite('es073_03', 3)	# 4-6
    sprite('es073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('es070_00', 3)	# 1-3
    sprite('es070_01', 3)	# 4-6
    label(1)
    sprite('es070_02', 5)	# 7-11
    sprite('es070_03', 5)	# 12-16
    loopRest()
    gotoLabel(1)

@State
def CmnActStaggerDown():
    sprite('es070_04', 4)	# 1-4
    sprite('es070_05', 4)	# 5-8
    sprite('es070_06', 4)	# 9-12
    sprite('es070_07', 4)	# 13-16
    sprite('es070_08', 4)	# 17-20
    sprite('es070_09', 5)	# 21-25

@State
def CmnActUkemiStagger():
    sprite('es070_10', 2)	# 1-2
    sprite('es070_11', 2)	# 3-4
    sprite('es070_12', 2)	# 5-6
    sprite('es070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('es113_00', 3)	# 1-3
    sprite('es113_01', 3)	# 4-6
    sprite('es113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('es113_00', 3)	# 1-3
    sprite('es113_01', 3)	# 4-6
    sprite('es113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('es113_00', 3)	# 1-3
    sprite('es113_01', 3)	# 4-6
    sprite('es113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('es110_00', 3)	# 1-3
    Unknown2017(0)
    sprite('es110_01', 3)	# 4-6
    sprite('es110_02', 3)	# 7-9
    sprite('es110_03', 3)	# 10-12
    sprite('es110_04', 200)	# 13-212
    sprite('es110_05', 2)	# 213-214
    sprite('es110_06', 2)	# 215-216
    sprite('es110_07', 2)	# 217-218

@State
def CmnActUkemiLandB():
    sprite('es111_00', 3)	# 1-3
    sprite('es111_01', 3)	# 4-6
    sprite('es111_02', 3)	# 7-9
    sprite('es111_03', 3)	# 10-12
    sprite('es111_04', 200)	# 13-212
    sprite('es111_05', 2)	# 213-214
    sprite('es111_06', 2)	# 215-216
    sprite('es111_07', 2)	# 217-218

@State
def CmnActUkemiLandN():
    sprite('es112_00', 2)	# 1-2
    sprite('es112_01', 2)	# 3-4
    sprite('es112_02', 2)	# 5-6
    sprite('es112_03', 2)	# 7-8
    sprite('es112_04', 3)	# 9-11
    sprite('es112_05', 3)	# 12-14
    sprite('es112_06', 3)	# 15-17
    sprite('es112_07', 3)	# 18-20
    sprite('es020_05', 3)	# 21-23
    sprite('es020_06', 3)	# 24-26
    label(1)
    sprite('es020_07', 3)	# 27-29
    sprite('es020_08', 3)	# 30-32
    gotoLabel(1)

@State
def CmnActUkemiLandNLanding():
    sprite('es024_00', 3)	# 1-3
    sprite('es024_01', 3)	# 4-6
    sprite('es024_02', 3)	# 7-9
    sprite('es024_03', 3)	# 10-12
    sprite('es024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('es040_00', 3)	# 1-3
    sprite('es040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('es040_02', 3)	# 1-3
    sprite('es040_03', 3)	# 4-6
    sprite('es040_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('es040_01', 3)	# 1-3
    sprite('es040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('es040_05', 3)	# 1-3
    label(0)
    sprite('es040_02', 4)	# 4-7
    sprite('es040_03', 4)	# 8-11
    sprite('es040_04', 4)	# 12-15
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('es040_01', 3)	# 1-3
    sprite('es040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('es041_00', 3)	# 1-3
    sprite('es041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('es041_02', 3)	# 1-3
    sprite('es041_03', 3)	# 4-6
    sprite('es041_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('es041_01', 3)	# 1-3
    sprite('es041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('es041_05', 3)	# 1-3
    label(0)
    sprite('es041_02', 4)	# 4-7
    sprite('es041_03', 4)	# 8-11
    sprite('es041_04', 4)	# 12-15
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('es041_01', 3)	# 1-3
    sprite('es041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('es043_00', 3)	# 1-3
    sprite('es043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('es043_02', 4)	# 1-4
    sprite('es043_03', 4)	# 5-8
    sprite('es043_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('es043_01', 3)	# 1-3
    sprite('es043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('es043_05', 3)	# 1-3
    label(0)
    sprite('es043_02', 4)	# 4-7
    sprite('es043_03', 4)	# 8-11
    sprite('es043_04', 4)	# 12-15
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('es043_01', 3)	# 1-3
    sprite('es043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('es045_00', 3)	# 1-3
    sprite('es045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('es045_02', 4)	# 1-4
    sprite('es045_03', 4)	# 5-8
    sprite('es045_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('es045_01', 3)	# 1-3
    sprite('es045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('es045_05', 3)	# 1-3
    label(0)
    sprite('es045_02', 4)	# 4-7
    sprite('es045_03', 4)	# 8-11
    sprite('es045_04', 4)	# 12-15
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('es045_01', 3)	# 1-3
    sprite('es045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('es090_00', 2)	# 1-2
    sprite('es090_01', 2)	# 3-4
    sprite('es090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('es090_03', 6)	# 6-11
    sprite('es090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    pass

@State
def CmnActGuardBreakAir():
    pass

@State
def CmnActAirTurn():
    sprite('es025_00', 4)	# 1-4
    sprite('es025_01', 3)	# 5-7
    sprite('es025_01ex00', 3)	# 8-10
    sprite('es025_00ex00', 4)	# 11-14

@State
def CmnActLockWait():
    sprite('es040_02', 1)	# 1-1
    sprite('es040_01', 3)	# 2-4
    sprite('es040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('es312_00', 3)	# 1-3
    sprite('es312_01', 3)	# 4-6
    sprite('es312_02', 3)	# 7-9
    sprite('es312_03', 5)	# 10-14	 **attackbox here**
    sprite('es312_04', 3)	# 15-17
    sprite('es312_05', 3)	# 18-20
    sprite('es312_06', 3)	# 21-23
    sprite('es312_07', 3)	# 24-26
    sprite('es312_08', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('es045_02', 1)	# 1-1
    sprite('es045_01', 3)	# 2-4
    sprite('es045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('es322_00', 3)	# 1-3
    sprite('es322_01', 3)	# 4-6
    sprite('es322_02', 3)	# 7-9
    sprite('es322_03', 5)	# 10-14	 **attackbox here**
    sprite('es322_04', 4)	# 15-18
    sprite('es322_05', 4)	# 19-22
    sprite('es322_06', 4)	# 23-26
    sprite('es322_07', 4)	# 27-30

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
    sprite('es077_00', 2)	# 1-2
    sprite('es077_01', 2)	# 3-4
    sprite('es077_00ex00', 2)	# 5-6
    sprite('es077_01ex00', 2)	# 7-8
    sprite('es077_00ex01', 2)	# 9-10
    sprite('es077_01ex01', 2)	# 11-12
    sprite('es077_00ex02', 2)	# 13-14
    sprite('es077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('es077_02', 4)	# 1-4
    label(0)
    sprite('es077_03', 3)	# 5-7
    sprite('es077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('es077_05', 5)	# 1-5
    sprite('es077_06', 4)	# 6-9

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
    sprite('es333_00', 3)	# 1-3
    sprite('es333_01', 3)	# 4-6
    sprite('es333_02', 3)	# 7-9
    GFX_0('EMB_OD', -1)
    sprite('es333_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('es333_04', 3)	# 1-3
    GFX_0('esef_333Eff', -1)
    label(0)
    sprite('es333_05', 3)	# 4-6
    sprite('es333_06', 3)	# 7-9
    sprite('es333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('es333_08', 6)	# 1-6
    sprite('es333_09', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('es333_10', 3)	# 1-3
    sprite('es333_11', 3)	# 4-6
    sprite('es333_12', 3)	# 7-9
    GFX_0('EMB_OD', -1)
    sprite('es333_13', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('es333_14', 3)	# 1-3
    GFX_0('esef_333Eff', -1)
    label(0)
    sprite('es333_05', 3)	# 4-6
    sprite('es333_06', 3)	# 7-9
    sprite('es333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('es333_15', 6)	# 1-6
    sprite('es333_16', 6)	# 7-12
    label(0)
    sprite('es020_07', 4)	# 13-16
    sprite('es020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('es333_00', 3)	# 1-3
    sprite('es333_01', 3)	# 4-6
    sprite('es333_02', 3)	# 7-9
    GFX_0('EMB_OD', -1)
    sprite('es333_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('es333_04', 3)	# 1-3
    GFX_0('esef_333Eff', -1)
    label(0)
    sprite('es333_05', 3)	# 4-6
    sprite('es333_06', 3)	# 7-9
    sprite('es333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('es333_08', 6)	# 1-6
    sprite('es333_09', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('es333_10', 3)	# 1-3
    sprite('es333_11', 3)	# 4-6
    sprite('es333_12', 3)	# 7-9
    GFX_0('EMB_OD', -1)
    sprite('es333_13', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('es333_14', 3)	# 1-3
    GFX_0('esef_333Eff', -1)
    label(0)
    sprite('es333_05', 3)	# 4-6
    sprite('es333_06', 3)	# 7-9
    sprite('es333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('es331_13', 3)	# 1-3
    sprite('es331_14', 3)	# 4-6
    sprite('es020_05', 3)	# 7-9
    sprite('es020_06', 3)	# 10-12
    label(0)
    sprite('es020_07', 4)	# 13-16
    sprite('es020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('es331_00', 2)	# 1-2
    sprite('es331_01', 2)	# 3-4
    label(0)
    sprite('es331_02', 3)	# 5-7
    sprite('es331_03', 3)	# 8-10
    sprite('es331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('es331_05', 2)	# 1-2
    label(0)
    sprite('es331_06', 3)	# 3-5
    sprite('es331_07', 3)	# 6-8
    sprite('es331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('es331_09', 3)	# 1-3
    sprite('es331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('es331_11', 2)	# 1-2
    sprite('es331_12', 2)	# 3-4
    label(0)
    sprite('es331_02', 3)	# 5-7
    sprite('es331_03', 3)	# 8-10
    sprite('es331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('es331_05', 2)	# 1-2
    label(0)
    sprite('es331_06', 3)	# 3-5
    sprite('es331_07', 3)	# 6-8
    sprite('es331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('es331_13', 3)	# 1-3
    sprite('es331_14', 3)	# 4-6
    sprite('es020_05', 3)	# 7-9
    sprite('es020_06', 3)	# 10-12
    label(0)
    sprite('es020_07', 4)	# 13-16
    sprite('es020_08', 4)	# 17-20
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
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('es409_19', 3)	# 26-28	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    GFX_0('esef_409_3rd', -1)
    SFX_3('esse_01')
    label(1)
    sprite('es409_19', 3)	# 29-31	 **attackbox here**
    sprite('es409_19', 3)	# 32-34	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('es409_19', 3)	# 35-37	 **attackbox here**
    sprite('es024_00', 5)	# 38-42
    sprite('es024_01', 5)	# 43-47
    sprite('es024_02', 3)	# 48-50
    sprite('es024_03', 3)	# 51-53
    sprite('es024_04', 3)	# 54-56
    sprite('es000_00', 3)	# 57-59

@State
def CmnActChangePartnerQuickIn():
    sprite('es032_05', 9)	# 1-9
    sprite('es032_08', 2)	# 10-11
    sprite('es032_09', 7)	# 12-18
    sprite('es032_10', 6)	# 19-24
    sprite('es032_11', 3)	# 25-27
    sprite('es032_12', 2)	# 28-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('es033_01', 3)	# 1-3
    sprite('es033_02', 3)	# 4-6
    sprite('es033_03', 3)	# 7-9
    sprite('es033_04', 3)	# 10-12
    sprite('es033_05', 3)	# 13-15
    sprite('es033_05', 45)	# 16-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('es033_00', 1)	# 1-1
    sprite('es033_00', 2)	# 2-3
    sprite('es033_01', 2)	# 4-5
    sprite('es033_02', 1)	# 6-6
    sprite('es033_02', 2)	# 7-8
    sprite('es033_03', 3)	# 9-11
    sprite('es033_04', 3)	# 12-14
    label(0)
    sprite('es020_07', 4)	# 15-18
    sprite('es020_08', 4)	# 19-22
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('es024_03', 3)	# 23-25
    sprite('es024_04', 3)	# 26-28

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('es300_00', 8)	# 1-8
    sprite('es300_01', 8)	# 9-16
    sprite('es300_02', 8)	# 17-24
    sprite('es300_03', 6)	# 25-30
    sprite('es300_04', 8)	# 31-38
    sprite('es300_05', 8)	# 39-46
    sprite('es300_06', 8)	# 47-54
    sprite('es300_08', 16)	# 55-70
    sprite('es300_07', 8)	# 71-78

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
    sprite('es020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('es020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('es010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('es400_00', 2)	# 1-2
    sprite('es400_01', 3)	# 3-5
    sprite('es400_02', 3)	# 6-8
    sprite('es400_03', 3)	# 9-11
    tag_voice(1, 'bes200_0', 'bes200_1', 'bes200_2', '')
    sprite('es400_01', 3)	# 12-14
    sprite('es400_04', 3)	# 15-17
    Unknown14070('ShotA_2nd')
    Unknown14070('ShotB_2nd')
    sprite('es400_05', 3)	# 18-20
    sprite('es400_06', 3)	# 21-23
    sprite('es400_07', 4)	# 24-27
    GFX_0('esef_400_zanzou', -1)
    GFX_0('es400_B', -1)
    Unknown38(5, 1)
    Unknown23029(5, 126, 0)
    sprite('es400_13', 2)	# 28-29
    sprite('es400_14', 4)	# 30-33
    sprite('es400_15', 4)	# 34-37
    sprite('es400_16', 2)	# 38-39
    sprite('es400_17', 3)	# 40-42
    GFX_0('esef_400_zanzou2', -1)
    GFX_0('es400_EX_2ndEX_ASS', -1)
    Unknown38(6, 1)
    Unknown2037(1)
    sprite('es400_18', 4)	# 43-46
    tag_voice(0, 'bes201_0', 'bes201_1', 'bes201_2', '')
    sprite('es400_19', 4)	# 47-50
    sprite('es400_20', 4)	# 51-54
    sprite('es400_18', 3)	# 55-57
    sprite('es400_21', 3)	# 58-60
    sprite('es400_22', 3)	# 61-63
    Recovery()
    sprite('es400_23', 3)	# 64-66
    sprite('es400_24', 3)	# 67-69

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AirPushbackX(3000)
        AirPushbackY(25000)
        AttackP1(70)
        Unknown9154(24)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(46)
        Unknown11058('0100000000000000000000000000000000000000')
        PushbackX(19800)
        Unknown9016(1)
        Unknown11042(1)
        JumpCancel_(0)
        sendToLabelUpon(2, 2)
    sprite('es213_00', 1)	# 1-1
    sprite('es213_01', 1)	# 2-2
    sprite('es213_01', 1)	# 3-3
    Unknown21007(10, 33)
    sprite('es213_02', 2)	# 4-5
    GFX_0('eseff_DTame', 0)
    Unknown36(1)
    Unknown1072(155000)
    Unknown1096(800)
    Unknown35()
    SFX_3('esse_02')
    sprite('es213_03', 2)	# 6-7
    SFX_3('esse_02')
    sprite('es213_05', 3)	# 8-10
    physicsXImpulse(20000)
    Unknown21015('65736566665f4454616d650000000000000000000000000000000000000000006400000000000000')
    SFX_0('006_swing_blade_2')
    Unknown7009(3)
    sprite('es213_06', 2)	# 11-12
    sprite('es213_07', 2)	# 13-14
    sprite('es213_08', 2)	# 15-16
    physicsXImpulse(-2500)
    physicsYImpulse(10000)
    setGravity(1000)
    sprite('es213_09', 4)	# 17-20	 **attackbox here**
    GFX_0('esef_213', -1)
    SFX_3('esse_00')
    GFX_0('es213_effAtk', -1)
    Unknown38(11, 1)
    sprite('es213_09', 2)	# 21-22	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('es213_10', 5)	# 23-27
    sprite('es213_11', 5)	# 28-32
    sprite('es213_12', 32767)	# 33-32799
    label(2)
    sprite('es213_13', 1)	# 32800-32800
    clearUponHandler(2)
    setInvincible(0)
    Unknown1084(1)
    sprite('es213_14', 3)	# 32801-32803
    sprite('es213_15', 2)	# 32804-32805
    sprite('es213_16', 2)	# 32806-32807
    sprite('es213_17', 2)	# 32808-32809

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AttackP2(85)
        AirPushbackX(4000)
        AirPushbackY(22000)
        PushbackX(2000)
        Unknown9154(24)
        AirUntechableTime(40)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11042(1)
        Unknown30055('90d003001e0000001e000000')

        def upon_3():
            (SLOT_19 < 300000)
            if op(5, 2, 0, 2, 51):
                sendToLabel(0)
        Unknown2004(1, 0)
    sprite('es406_00', 3)	# 1-3
    sprite('es406_01', 3)	# 4-6
    tag_voice(1, 'bes207_0', 'bes207_1', 'bes207_2', '')
    physicsXImpulse(45000)
    Unknown8007(100, 1, 0)
    SFX_0('001_airbackdash_0')
    sprite('es406_02', 3)	# 7-9
    Unknown8006(100, 1, 0)
    sprite('es406_01', 3)	# 10-12
    Unknown8006(100, 1, 0)
    SLOT_51 = 1
    sprite('es406_02', 3)	# 13-15
    Unknown8006(100, 1, 0)
    label(0)
    sprite('es406_03', 4)	# 16-19
    clearUponHandler(3)
    Unknown8010(100, 1, 0)
    SFX_0('006_swing_blade_2')
    Unknown1019(60)
    SLOT_51 = 0
    sprite('es406_04', 2)	# 20-21
    Unknown1019(60)
    sprite('es406_05', 2)	# 22-23	 **attackbox here**

    def upon_78():
        clearUponHandler(78)
        Unknown2037(1)
    SFX_3('esse_00')
    GFX_0('esef_406Eff', -1)
    Unknown1084(1)
    sprite('es406_05', 2)	# 24-25	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('es406_06', 2)	# 26-27
    sprite('es406_06', 2)	# 28-29
    sprite('es406_07', 4)	# 30-33
    if SLOT_2:
        sendToLabel(10)
        Unknown21015('657365665f3430364566660000000000000000000000000000000000000000006f00000000000000')
        Unknown21015('657365665f3430364566664558000000000000000000000000000000000000006f00000000000000')
        Unknown21015('657365665f3430364566666164640000000000000000000000000000000000006f00000000000000')
    else:
        Unknown21015('657365665f3430364566660000000000000000000000000000000000000000006500000000000000')
        Unknown21015('657365665f3430364566664558000000000000000000000000000000000000006600000000000000')
    sprite('es406_08', 4)	# 34-37
    sprite('es202_09ex00', 4)	# 38-41
    sprite('es202_10ex00', 3)	# 42-44
    sprite('es202_11ex00', 3)	# 45-47
    ExitState()
    label(10)
    sprite('es407_00', 2)	# 48-49
    physicsXImpulse(10000)
    sprite('es407_01', 2)	# 50-51
    SFX_0('006_swing_blade_2')
    sprite('es407_02', 2)	# 52-53
    sprite('es407_03', 2)	# 54-55
    sendToLabelUpon(2, 2)
    Unknown1019(20)
    physicsYImpulse(20000)
    setGravity(1500)
    sprite('es407_04', 4)	# 56-59	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(22000)
    YImpluseBeforeWallbounce(1600)
    PushbackX(19800)
    AirUntechableTime(55)
    Unknown9016(1)
    tag_voice(0, 'bes208_0', 'bes208_1', 'bes208_2', '')
    GFX_0('esef_406Eff2', -1)
    sprite('es407_05', 4)	# 60-63
    Recovery()
    sprite('es407_06', 4)	# 64-67
    sprite('es407_07', 4)	# 68-71
    sprite('es407_08', 4)	# 72-75
    sprite('es407_09', 4)	# 76-79
    sprite('es407_10', 4)	# 80-83
    label(1)
    sprite('es020_07', 3)	# 84-86
    sprite('es020_08', 3)	# 87-89
    gotoLabel(1)
    label(2)
    sprite('es024_00', 1)	# 90-90
    Unknown1084(1)
    sprite('es024_01', 5)	# 91-95
    sprite('es024_02', 5)	# 96-100
    sprite('es024_03', 5)	# 101-105

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
    Unknown2036(79, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-245000)
    Unknown1019(4)
    label(0)
    sprite('es020_07', 4)	# 3-6
    sprite('es020_08', 4)	# 7-10
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
        Unknown30063(1)
        AttackLevel_(4)
        Damage(700)
        AttackP1(100)
        Unknown11091(100)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown9154(60)
        Unknown11056(0)
        Unknown11069('ChangePartnerDD_Exe')
        Unknown11064(1)
        Unknown30048(1)
        Unknown23056('')

        def upon_12():
            clearUponHandler(12)
            Unknown13024(0)
            Unknown21005(1)
            Unknown13021(1)
            sendToLabel(0)
            Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown13024(0)

        def upon_STATE_END():
            Unknown26('esef_431Camera')
            Unknown3001(255)
            Unknown3004(0)
    sprite('es431_00', 4)	# 1-4
    setInvincible(1)
    sprite('es431_01', 1)	# 5-5
    sprite('es431_01', 3)	# 6-8
    sprite('es431_02', 4)	# 9-12
    sprite('es431_03', 16)	# 13-28
    GFX_0('esef_431Eff', -1)
    tag_voice(1, 'bes252_0', 'bes252_1', '', '')
    sprite('es431_04', 6)	# 29-34
    sprite('es431_05', 6)	# 35-40
    sprite('es431_06', 6)	# 41-46
    sprite('es431_07', 5)	# 47-51
    sprite('es431_08', 3)	# 52-54
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006800000000000000')
    Unknown3029(1)
    physicsXImpulse(15000)
    physicsYImpulse(18000)
    SFX_3('esse_04')
    SFX_0('000_airdash_0')
    sprite('es431_09', 3)	# 55-57	 **attackbox here**
    Unknown1019(500)
    physicsYImpulse(0)
    sprite('es431_10', 3)	# 58-60	 **attackbox here**
    sprite('es431_09', 3)	# 61-63	 **attackbox here**
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    sprite('es431_11', 4)	# 64-67
    setInvincible(0)
    Unknown1019(70)
    teleportRelativeY(0)
    sprite('es110_03ex00', 4)	# 68-71
    Unknown1019(70)
    sprite('es110_04ex00', 4)	# 72-75
    Unknown1019(70)
    sprite('es110_05ex00', 4)	# 76-79
    Unknown1019(70)
    sprite('es110_06ex00', 4)	# 80-83
    Unknown1019(70)
    sprite('es110_07ex00', 4)	# 84-87
    Unknown1084(1)
    Unknown3029(0)
    ExitState()
    label(0)
    sprite('es431_12', 5)	# 88-92
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    Unknown1019(50)
    sprite('es431_13', 5)	# 93-97
    Unknown1019(50)
    sprite('es431_14', 5)	# 98-102
    Unknown2017(0)
    Unknown1019(50)
    sprite('es431_15', 5)	# 103-107
    Unknown1019(50)
    Unknown3004(-8)
    sprite('es431_16', 5)	# 108-112
    sprite('es431_17', 5)	# 113-117
    GFX_0('esef_431Eff2', -1)
    SFX_3('esse_09')
    SFX_3('esse_09')
    tag_voice(0, 'bes253_0', 'bes253_1', '', '')
    sprite('es431_18', 3)	# 118-120	 **attackbox here**
    Unknown3029(0)
    Unknown1019(0)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(0)
    sprite('es431_18', 9)	# 121-129	 **attackbox here**
    GFX_0('esef_431EffSlash', -1)
    GFX_0('esef_431Camera', -1)
    GFX_0('esef_431EffEsRay', 100)
    Unknown2015(50)
    physicsXImpulse(96000)
    Unknown1028(-8000)
    Unknown3004(42)
    Damage(1800)
    AttackP2(100)
    Unknown11091(100)
    Hitstop(0)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    PushbackX(-30000)
    Unknown9130(50)
    Unknown9142(200)
    Unknown9132(50)
    Unknown9016(1)
    Unknown11023(1)
    Unknown11069('')
    Unknown11064(0)
    Unknown11066(1)
    Unknown11084(1)
    RefreshMultihit()
    sprite('es431_18', 3)	# 130-132	 **attackbox here**
    Unknown2017(1)
    Unknown2015(-1)
    GFX_0('esef_431EffScrew', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('es431_19', 2)	# 133-134	 **attackbox here**
    sprite('es431_20', 2)	# 135-136	 **attackbox here**
    sprite('es431_21', 2)	# 137-138	 **attackbox here**
    sprite('es431_22', 2)	# 139-140	 **attackbox here**
    sprite('es431_19', 2)	# 141-142	 **attackbox here**
    sprite('es431_20', 2)	# 143-144	 **attackbox here**
    sprite('es431_21', 2)	# 145-146	 **attackbox here**
    sprite('es431_22', 2)	# 147-148	 **attackbox here**
    sprite('es431_19', 3)	# 149-151	 **attackbox here**
    sprite('es431_20', 3)	# 152-154	 **attackbox here**
    sprite('es431_21', 3)	# 155-157	 **attackbox here**
    sprite('es431_22', 3)	# 158-160	 **attackbox here**
    sprite('es431_19', 4)	# 161-164	 **attackbox here**
    sprite('es431_20', 4)	# 165-168	 **attackbox here**
    sprite('es431_21', 4)	# 169-172	 **attackbox here**
    sprite('es431_22', 4)	# 173-176	 **attackbox here**
    sprite('es431_19', 4)	# 177-180	 **attackbox here**
    sprite('es431_20', 4)	# 181-184	 **attackbox here**
    sprite('es431_21', 4)	# 185-188	 **attackbox here**
    sprite('es431_22', 3)	# 189-191	 **attackbox here**
    sprite('es431_22', 1)	# 192-192	 **attackbox here**
    Unknown26('esef_431Camera')
    sprite('es431_23', 5)	# 193-197
    sprite('es431_24', 5)	# 198-202

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(4)
        Damage(700)
        AttackP1(100)
        Unknown11091(100)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown9154(60)
        Unknown11056(0)
        Unknown12051(0)
        Unknown11069('ChangePartnerDDOD_Exe')
        Unknown9001(5)
        Unknown11064(1)
        Unknown30048(1)
        Unknown23056('')

        def upon_12():
            clearUponHandler(12)
            Unknown13024(0)
            Unknown21005(1)
            Unknown13021(1)
            sendToLabel(0)
            Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown13024(0)

        def upon_STATE_END():
            Unknown26('esef_431Camera')
            Unknown3001(255)
            Unknown3004(0)
    sprite('es431_00', 4)	# 1-4
    setInvincible(1)
    sprite('es431_01', 1)	# 5-5
    sprite('es431_01', 3)	# 6-8
    sprite('es431_02', 4)	# 9-12
    sprite('es431_03', 16)	# 13-28
    tag_voice(1, 'bes252_0', 'bes252_1', '', '')
    GFX_0('esef_431Eff', -1)
    sprite('es431_04', 6)	# 29-34
    sprite('es431_05', 6)	# 35-40
    sprite('es431_06', 6)	# 41-46
    sprite('es431_07', 5)	# 47-51
    sprite('es431_08', 3)	# 52-54
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006800000000000000')
    Unknown3029(1)
    physicsXImpulse(15000)
    physicsYImpulse(18000)
    SFX_3('esse_04')
    SFX_0('000_airdash_0')
    sprite('es431_09', 3)	# 55-57	 **attackbox here**
    Unknown1019(500)
    physicsYImpulse(0)
    sprite('es431_10', 3)	# 58-60	 **attackbox here**
    sprite('es431_09', 3)	# 61-63	 **attackbox here**
    sprite('es431_11', 4)	# 64-67
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    setInvincible(0)
    Unknown1019(70)
    teleportRelativeY(0)
    sprite('es110_03ex00', 4)	# 68-71
    Unknown1019(70)
    sprite('es110_04ex00', 4)	# 72-75
    Unknown1019(70)
    sprite('es110_05ex00', 4)	# 76-79
    Unknown1019(70)
    sprite('es110_06ex00', 4)	# 80-83
    Unknown1019(70)
    sprite('es110_07ex00', 4)	# 84-87
    Unknown3029(0)
    Unknown1084(1)
    ExitState()
    label(0)
    sprite('es431_12', 5)	# 88-92
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    Unknown1019(50)
    Unknown23024(2)
    sprite('es431_13', 5)	# 93-97
    Unknown1019(50)
    sprite('es431_14', 5)	# 98-102
    Unknown2017(0)
    Unknown1019(50)
    sprite('es431_15', 5)	# 103-107
    Unknown1019(50)
    Unknown3004(-8)
    sprite('es431_16', 5)	# 108-112
    sprite('es431_17', 5)	# 113-117
    GFX_0('esef_431Eff2', -1)
    SFX_3('esse_09')
    SFX_3('esse_09')
    tag_voice(0, 'bes253_0', 'bes253_1', '', '')
    sprite('es431_18', 3)	# 118-120	 **attackbox here**
    Unknown1019(0)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(0)
    Unknown3029(0)
    sprite('es431_18', 3)	# 121-123	 **attackbox here**
    GFX_0('esef_431EffSlashOD', -1)
    GFX_0('esef_431Camera', -1)
    GFX_0('esef_431EffEsRay', 100)
    SFX_0('025_cleanhit_slash')
    Unknown2015(50)
    physicsXImpulse(120000)
    Unknown1028(-10000)
    Unknown3004(42)
    Damage(80)
    AttackP2(100)
    Unknown11091(100)
    Hitstop(0)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    PushbackX(-30000)
    Unknown9130(50)
    Unknown9142(200)
    Unknown9132(50)
    Unknown9016(1)
    Unknown11057(600)
    Unknown11023(1)
    Unknown11066(1)
    Unknown11084(1)
    RefreshMultihit()
    sprite('es431_18', 1)	# 124-124	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 125-125	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 126-126	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 127-127	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 128-128	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 129-129	 **attackbox here**
    Damage(1820)
    AttackP2(100)
    Unknown11091(100)
    Unknown11057(1000)
    Unknown11069('')
    Unknown11064(0)
    RefreshMultihit()
    sprite('es431_18', 3)	# 130-132	 **attackbox here**
    Unknown2017(1)
    Unknown2015(-1)
    GFX_0('esef_431EffScrew', -1)
    GFX_0('esef_431EffScrewOD', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    Unknown23024(1)
    sprite('es431_19', 2)	# 133-134	 **attackbox here**
    sprite('es431_20', 2)	# 135-136	 **attackbox here**
    sprite('es431_21', 2)	# 137-138	 **attackbox here**
    sprite('es431_22', 2)	# 139-140	 **attackbox here**
    sprite('es431_19', 2)	# 141-142	 **attackbox here**
    sprite('es431_20', 2)	# 143-144	 **attackbox here**
    sprite('es431_21', 2)	# 145-146	 **attackbox here**
    sprite('es431_22', 2)	# 147-148	 **attackbox here**
    sprite('es431_19', 2)	# 149-150	 **attackbox here**
    sprite('es431_20', 2)	# 151-152	 **attackbox here**
    sprite('es431_21', 2)	# 153-154	 **attackbox here**
    sprite('es431_22', 2)	# 155-156	 **attackbox here**
    sprite('es431_19', 3)	# 157-159	 **attackbox here**
    sprite('es431_20', 3)	# 160-162	 **attackbox here**
    sprite('es431_21', 3)	# 163-165	 **attackbox here**
    sprite('es431_22', 3)	# 166-168	 **attackbox here**
    sprite('es431_19', 4)	# 169-172	 **attackbox here**
    sprite('es431_20', 4)	# 173-176	 **attackbox here**
    sprite('es431_21', 4)	# 177-180	 **attackbox here**
    sprite('es431_22', 4)	# 181-184	 **attackbox here**
    sprite('es431_19', 4)	# 185-188	 **attackbox here**
    sprite('es431_20', 4)	# 189-192	 **attackbox here**
    sprite('es431_21', 4)	# 193-196	 **attackbox here**
    sprite('es431_22', 3)	# 197-199	 **attackbox here**
    sprite('es431_22', 1)	# 200-200	 **attackbox here**
    Unknown13024(1)
    Unknown26('esef_431Camera')
    sprite('es431_23', 5)	# 201-205
    sprite('es431_24', 5)	# 206-210

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('es300_00', 10)	# 1-10
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('es300_01', 10)	# 11-20
    sprite('es300_02', 10)	# 21-30
    sprite('es300_03', 8)	# 31-38
    sprite('es300_04', 10)	# 39-48
    sprite('es300_05', 10)	# 49-58
    sprite('es300_06', 10)	# 59-68
    label(1)
    sprite('es300_06', 1)	# 69-69
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es300_08', 11)	# 70-80
    sprite('es300_07', 5)	# 81-85

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
        Unknown9016(1)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('es409_19', 3)	# 121-123	 **attackbox here**
    GFX_0('esef_409_3rd', -1)
    SFX_3('esse_01')
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('es409_19', 3)	# 124-126	 **attackbox here**
    sprite('es409_19', 3)	# 127-129	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('es024_00', 5)	# 130-134
    sprite('es024_01', 5)	# 135-139
    sprite('es024_02', 5)	# 140-144
    sprite('es024_03', 5)	# 145-149
    sprite('es024_04', 5)	# 150-154
    sprite('es000_00', 6)	# 155-160

@State
def CmnActChangeReturnAppealBurst():
    sprite('es404_20', 5)	# 1-5
    sprite('es404_21', 47)	# 6-52
    sprite('es404_22', 5)	# 53-57
    sprite('es404_23', 5)	# 58-62
    sprite('es010_01', 4)	# 63-66
    sprite('es010_00', 4)	# 67-70

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(10000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        Unknown1112('')
    sprite('es201_00', 2)	# 1-2
    sprite('es201_01', 2)	# 3-4
    sprite('es201_02', 2)	# 5-6
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 7-8
    Unknown7009(1)
    sprite('es201_04', 5)	# 9-13	 **attackbox here**
    GFX_0('esef_201', -1)
    sprite('es201_05', 4)	# 14-17
    Recovery()
    Unknown2063()
    sprite('es201_06', 4)	# 18-21
    sprite('es201_07', 4)	# 22-25
    sprite('es201_08', 4)	# 26-29
    sprite('es201_09', 4)	# 30-33
    sprite('es201_10', 5)	# 34-38

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(15000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        Unknown2004(1, 0)
        Unknown1112('')
    sprite('es202_00', 3)	# 1-3
    sprite('es202_01', 2)	# 4-5
    sprite('es202_02', 3)	# 6-8
    SFX_0('006_swing_blade_1')
    sprite('es202_03', 3)	# 9-11
    Unknown7009(2)
    sprite('es202_04', 3)	# 12-14	 **attackbox here**
    GFX_0('esef_202', -1)
    sprite('es202_05', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('es202_06', 3)	# 18-20
    sprite('es202_07', 3)	# 21-23
    sprite('es202_08', 3)	# 24-26
    sprite('es202_09', 3)	# 27-29
    sprite('es202_10', 3)	# 30-32
    sprite('es202_11', 3)	# 33-35

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirUntechableTime(24)
        AirHitstunAnimation(11)
        AirPushbackX(15000)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('CmnActCrushAttack')
        Unknown2004(1, 0)
    sprite('es212_00', 1)	# 1-1
    sprite('es212_00', 1)	# 2-2
    SFX_0('019_cloth_a')
    sprite('es212_01', 2)	# 3-4
    GFX_1('esef_212dash', -1)
    physicsXImpulse(24000)
    SFX_0('019_cloth_b')
    sprite('es212_02', 2)	# 5-6
    GFX_1('esef_212dash', -1)
    sprite('es212_01', 2)	# 7-8
    GFX_1('esef_212dash', -1)
    sprite('es212_02', 2)	# 9-10
    GFX_1('esef_212dash', -1)
    sprite('es212_03', 2)	# 11-12
    Unknown1019(20)
    GFX_1('esef_212dash', -1)
    SFX_0('009_swing_rapier_2')
    Unknown7009(2)
    sprite('es212_04', 3)	# 13-15	 **attackbox here**
    ScreenShake(4000, 2000)
    Unknown1084(1)
    GFX_0('esef_212', 0)
    sprite('es212_05', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('es212_06', 3)	# 19-21
    sprite('es212_07', 3)	# 22-24
    sprite('es212_08', 3)	# 25-27
    sprite('es212_09', 3)	# 28-30
    sprite('es212_10', 3)	# 31-33

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackY(18000)
        AirPushbackX(35000)
        PushbackX(8000)
        AirUntechableTime(60)
        Unknown9016(1)
        JumpCancel_(0)
    sprite('es340_00', 2)	# 1-2
    GFX_0('esef_340', 103)
    sprite('es340_01', 1)	# 3-3
    SFX_3('esse_06')
    Unknown7007('6265733130365f300000000000000000640000006265733130365f310000000000000000640000006265733130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('es340_01', 1)	# 4-4
    sprite('es340_02', 2)	# 5-6
    sprite('es340_03', 2)	# 7-8
    sprite('es340_01', 2)	# 9-10
    sprite('es340_04', 2)	# 11-12
    clearUponHandler(3)
    Unknown26('esef_340')
    SFX_0('006_swing_blade_2')
    sprite('es340_05', 2)	# 13-14
    sprite('es340_06', 2)	# 15-16
    GFX_0('esef_340_blade', -1)
    Unknown21015('657365665f3334305f636972636c6531000000000000000000000000000000006400000000000000')
    Unknown21015('657365665f3334305f636972636c6532000000000000000000000000000000006400000000000000')
    SFX_3('esse_01')
    sprite('es340_07', 1)	# 17-17	 **attackbox here**
    GFX_0('esef_340_zanzou', -1)
    sprite('es340_07', 2)	# 18-19	 **attackbox here**
    Unknown23027()
    Unknown3029(0)
    Recovery()
    Unknown2063()
    sprite('es340_08', 4)	# 20-23
    sprite('es340_09', 4)	# 24-27
    sprite('es340_10', 4)	# 28-31
    sprite('es340_11', 4)	# 32-35
    sprite('es340_12', 4)	# 36-39
    sprite('es340_13', 3)	# 40-42

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('es200_00', 1)	# 1-1
    Unknown1051(60)
    sprite('es200_01', 2)	# 2-3
    sprite('es200_02', 2)	# 4-5
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    sprite('es200_03', 3)	# 6-8	 **attackbox here**
    sprite('es200_03', 1)	# 9-9	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('es200_04', 3)	# 10-12
    sprite('es200_05', 3)	# 13-15
    sprite('es200_06', 3)	# 16-18

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(1250)
        AttackP1(90)
        Unknown9154(15)
        HitLow(2)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown2004(1, 0)
    sprite('es231_00', 2)	# 1-2
    sprite('es231_01', 2)	# 3-4
    SFX_0('006_swing_blade_0')
    sprite('es231_02', 2)	# 5-6
    sprite('es231_03', 3)	# 7-9
    Unknown7009(1)
    sprite('es231_04', 3)	# 10-12	 **attackbox here**
    GFX_0('esef_231', -1)
    sprite('es231_05', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('es231_06', 4)	# 17-20
    sprite('es231_07', 4)	# 21-24
    sprite('es231_08', 4)	# 25-28
    sprite('es231_09', 4)	# 29-32

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        PushbackX(39900)
        AirPushbackX(15000)
        AirPushbackY(-100000)
        Unknown9310(10)
        Unknown9202(1)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B2nd')
        Unknown1112('')
        Unknown2004(1, 0)
    sprite('es203_00', 3)	# 1-3
    sprite('es203_01', 3)	# 4-6
    Unknown23029(11, 110, 0)
    GFX_0('eseff_DTame', 0)
    Unknown36(1)
    Unknown1072(42500)
    Unknown35()
    SFX_3('esse_02')
    sprite('es203_02', 2)	# 7-8
    sprite('es203_03', 2)	# 9-10
    SFX_3('esse_02')
    sprite('es203_02', 2)	# 11-12
    sprite('es203_03', 2)	# 13-14
    SFX_3('esse_02')
    sprite('es203_04', 2)	# 15-16
    Unknown21015('65736566665f4454616d650000000000000000000000000000000000000000006400000000000000')
    SFX_0('006_swing_blade_2')
    Unknown7009(3)
    sprite('es203_05', 3)	# 17-19
    sprite('es203_06', 2)	# 20-21
    sprite('es203_07', 2)	# 22-23
    sprite('es203_08', 5)	# 24-28	 **attackbox here**
    Unknown2015(200)
    GFX_0('esef_203', -1)
    SFX_3('esse_00')
    GFX_0('es203_effAtk', -1)
    Unknown38(11, 1)
    sprite('es203_09', 9)	# 29-37
    Recovery()
    Unknown2063()
    sprite('es203_10', 5)	# 38-42
    sprite('es203_11', 5)	# 43-47
    sprite('es203_12', 5)	# 48-52
    Unknown2015(-1)
    sprite('es203_13', 5)	# 53-57
    sprite('es203_14', 4)	# 58-61

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(10)
        PushbackX(39900)
        AirPushbackX(15000)
        AirPushbackY(20000)
        Unknown9154(22)
        AirUntechableTime(40)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('es233_00', 3)	# 1-3
    sprite('es233_01', 3)	# 4-6
    Unknown21007(11, 33)
    GFX_0('eseff_DTame', 0)
    Unknown36(1)
    Unknown1072(63000)
    Unknown1056(700)
    Unknown1064(900)
    Unknown35()
    SFX_3('esse_02')
    sprite('es233_02', 3)	# 7-9
    sprite('es233_03', 3)	# 10-12
    SFX_3('esse_02')
    sprite('es233_04', 2)	# 13-14
    Unknown21015('65736566665f4454616d650000000000000000000000000000000000000000006400000000000000')
    physicsXImpulse(25000)
    sprite('es233_04', 2)	# 15-16
    Unknown1019(90)
    SFX_0('000_airdash_0')
    sprite('es233_05', 2)	# 17-18
    Unknown1019(90)
    sprite('es233_05', 2)	# 19-20
    Unknown1019(90)
    sprite('es233_06', 3)	# 21-23
    Unknown1019(50)
    SFX_0('006_swing_blade_2')
    Unknown7009(3)
    sprite('es233_07', 3)	# 24-26
    Unknown1019(50)
    sprite('es233_08', 6)	# 27-32	 **attackbox here**
    GFX_0('esef_233', -1)
    SFX_3('esse_00')
    GFX_0('es233_effAtk', -1)
    Unknown38(11, 1)
    Unknown1084(1)
    sprite('es233_09', 3)	# 33-35
    Recovery()
    Unknown2063()
    sprite('es233_10', 5)	# 36-40
    sprite('es233_11', 5)	# 41-45
    sprite('es233_12', 4)	# 46-49
    sprite('es233_13', 4)	# 50-53
    sprite('es233_14', 4)	# 54-57
    sprite('es233_15', 5)	# 58-62

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(80)
        AirPushbackY(28000)
        AirUntechableTime(22)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)
    sprite('es232_00', 2)	# 1-2
    sprite('es232_01', 2)	# 3-4
    sprite('es232_02', 3)	# 5-7
    SFX_0('006_swing_blade_1')
    sprite('es232_03', 2)	# 8-9
    Unknown7007('6265733130375f300000000000000000640000006265733130375f310000000000000000640000006265733130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('es232_04', 3)	# 10-12	 **attackbox here**
    GFX_0('esef_232', -1)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('es232_05', 4)	# 13-16
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('es232_06', 4)	# 17-20
    sprite('es232_07', 6)	# 21-26
    sprite('es232_08', 6)	# 27-32
    sprite('es232_09', 6)	# 33-38
    sprite('es232_10', 6)	# 39-44

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(20000)
        AirUntechableTime(40)
        HitLow(2)
        Unknown9016(1)
    sprite('es235_00', 3)	# 1-3
    sprite('es235_01', 3)	# 4-6
    GFX_0('esef_235', -1)
    SFX_0('006_swing_blade_1')
    sprite('es235_02', 3)	# 7-9
    sprite('es235_03', 3)	# 10-12
    Unknown7007('6265733130385f300000000000000000640000006265733130385f310000000000000000640000006265733130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('es235_04', 3)	# 13-15	 **attackbox here**
    sprite('es235_05', 4)	# 16-19
    Recovery()
    Unknown2063()
    sprite('es235_06', 4)	# 20-23
    sprite('es235_07', 4)	# 24-27
    sprite('es235_08', 3)	# 28-30
    sprite('es235_09', 3)	# 31-33
    sprite('es235_10', 3)	# 34-36
    sprite('es235_11', 3)	# 37-39

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AttackP1(80)
        AttackP2(85)
        AirUntechableTime(17)
        AirPushbackY(16000)
        Unknown9016(1)
        WhiffCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('es251_00', 2)	# 1-2
    sprite('es251_01', 1)	# 3-3
    sprite('es251_01', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es251_02', 3)	# 6-8
    Unknown7009(1)
    sprite('es251_03', 3)	# 9-11	 **attackbox here**
    GFX_0('esef_251', -1)
    sprite('es251_04', 4)	# 12-15
    Recovery()
    Unknown2063()
    sprite('es251_04', 4)	# 16-19
    WhiffCancelEnable(1)
    sprite('es251_05', 6)	# 20-25
    WhiffCancelEnable(0)
    sprite('es251_06', 4)	# 26-29

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AttackP1(80)
        AttackP2(85)
        AirUntechableTime(17)
        AirPushbackY(18000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('es251_05', 3)	# 1-3
    SFX_0('006_swing_blade_0')
    sprite('es251_07', 3)	# 4-6
    Unknown7009(1)
    sprite('es251_08', 3)	# 7-9	 **attackbox here**
    GFX_0('esef_251_2', -1)
    sprite('es251_09', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('es251_10', 3)	# 14-16
    sprite('es251_11', 3)	# 17-19
    sprite('es251_12', 3)	# 20-22
    sprite('es251_13', 3)	# 23-25
    sprite('es251_14', 3)	# 26-28

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        AirUntechableTime(30)
        AirPushbackY(-20000)
        Unknown9016(1)
        HitCancel('NmlAtkAIR5C')
    sprite('es252_00', 3)	# 1-3
    sprite('es252_01', 3)	# 4-6
    sprite('es252_02', 3)	# 7-9
    SFX_0('006_swing_blade_1')
    Unknown7009(2)
    sprite('es252_03', 2)	# 10-11
    sprite('es252_04', 4)	# 12-15	 **attackbox here**
    GFX_0('esef_252', -1)
    sprite('es252_05', 4)	# 16-19
    Recovery()
    Unknown2063()
    sprite('es252_06', 4)	# 20-23
    sprite('es252_07', 5)	# 24-28
    sprite('es252_08', 5)	# 29-33
    sprite('es252_09', 5)	# 34-38
    sprite('es252_10', 3)	# 39-41

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackY(18000)
        AirUntechableTime(25)
        Unknown9016(1)
    sprite('es253_00', 3)	# 1-3
    sprite('es253_00', 1)	# 4-4
    Unknown23029(11, 110, 0)
    sprite('es253_01', 3)	# 5-7
    Unknown22004(9, 1)
    GFX_0('eseff_DTame', 0)
    Unknown36(1)
    Unknown1072(120000)
    Unknown35()
    SFX_3('esse_02')
    sprite('es253_02', 3)	# 8-10
    sprite('es253_03', 3)	# 11-13
    SFX_3('esse_02')
    Unknown21015('65736566665f4454616d650000000000000000000000000000000000000000006400000000000000')
    sprite('es253_04', 3)	# 14-16
    SFX_0('006_swing_blade_2')
    sprite('es253_05', 3)	# 17-19
    GFX_0('esef_253_wari', -1)
    sprite('es253_06', 3)	# 20-22
    GFX_0('esef_253_wari2', -1)
    Unknown26('esef_253_wari')
    sprite('es253_07', 5)	# 23-27	 **attackbox here**
    Unknown7009(3)
    Unknown26('esef_253_wari2')
    GFX_0('esef_253', -1)
    SFX_3('esse_00')
    GFX_0('es253_effAtk', -1)
    Unknown38(11, 1)
    sprite('es253_08', 4)	# 28-31
    Recovery()
    Unknown2063()
    sprite('es253_09', 7)	# 32-38
    sprite('es253_10', 3)	# 39-41
    sprite('es253_11', 3)	# 42-44
    sprite('es253_12', 3)	# 45-47
    sprite('es253_13', 3)	# 48-50

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('es210_00', 3)	# 1-3
    Unknown1045(10000)
    sprite('es210_01', 3)	# 4-6
    tag_voice(1, 'bes156_0', 'bes156_1', '', '')
    sprite('es210_02', 3)	# 7-9
    sprite('es210_03', 3)	# 10-12
    sprite('es210_04', 3)	# 13-15
    sprite('es210_05', 3)	# 16-18
    SFX_0('003_swing_grap_0_1')
    sprite('es210_06', 3)	# 19-21
    sprite('es210_07', 3)	# 22-24	 **attackbox here**
    Unknown1051(0)
    sprite('es210_08', 3)	# 25-27
    Unknown8000(100, 1, 1)
    sprite('es210_09', 3)	# 28-30
    sprite('es210_10', 4)	# 31-34
    sprite('es210_11', 4)	# 35-38
    sprite('es210_12', 5)	# 39-43
    sprite('es210_13', 5)	# 44-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown23027()
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('es210_08', 2)	# 2-3
    Unknown8000(100, 1, 1)
    sprite('es210_09', 2)	# 4-5
    sprite('es210_10', 3)	# 6-8
    sprite('es210_11', 3)	# 9-11
    sprite('es210_12', 3)	# 12-14
    sprite('es210_13', 3)	# 15-17
    sprite('es202_00', 3)	# 18-20
    sprite('es202_01', 3)	# 21-23
    sprite('es202_02', 3)	# 24-26
    SFX_0('006_swing_blade_1')
    sprite('es202_03', 3)	# 27-29
    tag_voice(0, 'bes157_0', 'bes157_1', '', '')
    sprite('es202_04', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    GFX_0('esef_202', -1)
    sprite('es202_05', 1)	# 32-32
    sprite('es202_06', 1)	# 33-33
    sprite('es202_07', 2)	# 34-35
    sprite('es202_08', 2)	# 36-37
    sprite('es202_09', 2)	# 38-39
    sprite('es202_10', 2)	# 40-41
    sprite('es202_11', 2)	# 42-43
    label(0)
    sprite('es000_00', 7)	# 44-50
    sprite('es000_01', 7)	# 51-57
    sprite('es000_02', 7)	# 58-64
    sprite('es000_03', 7)	# 65-71
    sprite('es000_04', 7)	# 72-78
    sprite('es000_05', 7)	# 79-85
    sprite('es000_06', 7)	# 86-92
    sprite('es000_07', 7)	# 93-99
    sprite('es000_08', 7)	# 100-106
    sprite('es000_09', 7)	# 107-113
    sprite('es000_10', 7)	# 114-120
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('es001_00', 6)	# 121-126
    sprite('es001_01', 6)	# 127-132
    sprite('es001_02', 6)	# 133-138
    sprite('es001_03', 6)	# 139-144
    GFX_0('esef_001', 0)
    Unknown36(1)
    Unknown1072(65000)
    Unknown35()
    SFX_3('esse_08')
    GFX_0('esef_001_tame_add', 0)
    GFX_0('esef_001_tame_add', 1)
    GFX_0('esef_001_tame_add', 2)
    SFX_4('bes000')
    sprite('es001_04', 6)	# 145-150
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 151-156
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 157-162
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 163-168
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 169-174
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 175-180
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 181-186
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 187-192
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 193-198
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 199-204
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 205-210
    sprite('es001_02', 6)	# 211-216
    sprite('es001_01', 6)	# 217-222
    sprite('es001_00', 6)	# 223-228
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 229-229

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('es404_00ex00', 3)	# 1-3
    sprite('es404_01ex00', 3)	# 4-6
    sprite('es404_02ex00', 3)	# 7-9
    SFX_0('004_swing_grap_1_2')
    sprite('es440_03', 3)	# 10-12
    physicsXImpulse(12500)
    sprite('es404_10ex00', 2)	# 13-14	 **attackbox here**
    sendToLabelUpon(2, 1)
    physicsXImpulse(-7000)
    Unknown1028(300)
    physicsYImpulse(18000)
    setGravity(1800)
    Unknown23027()
    GFX_0('esef_404_kick_BDD', -1)
    sprite('es404_10ex00', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('es404_11ex00', 2)	# 18-19
    sprite('es404_12ex00', 2)	# 20-21
    sprite('es404_13ex00', 2)	# 22-23
    sprite('es404_14ex00', 2)	# 24-25
    sprite('es404_15ex00', 2)	# 26-27
    sprite('es404_16ex00', 2)	# 28-29
    sprite('es020_05', 2)	# 30-31
    sprite('es020_06', 2)	# 32-33
    label(0)
    sprite('es020_07', 3)	# 34-36
    sprite('es020_08', 3)	# 37-39
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('es024_00', 3)	# 40-42
    Unknown1084(1)
    sprite('es024_01', 3)	# 43-45
    sprite('es024_02', 4)	# 46-49
    sprite('es024_03', 3)	# 50-52
    sprite('es024_04', 3)	# 53-55
    label(0)
    sprite('es000_00', 7)	# 56-62
    sprite('es000_01', 7)	# 63-69
    sprite('es000_02', 7)	# 70-76
    sprite('es000_03', 7)	# 77-83
    sprite('es000_04', 7)	# 84-90
    sprite('es000_05', 7)	# 91-97
    sprite('es000_06', 7)	# 98-104
    sprite('es000_07', 7)	# 105-111
    sprite('es000_08', 7)	# 112-118
    sprite('es000_09', 7)	# 119-125
    sprite('es000_10', 7)	# 126-132
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('es001_00', 6)	# 133-138
    sprite('es001_01', 6)	# 139-144
    sprite('es001_02', 6)	# 145-150
    sprite('es001_03', 6)	# 151-156
    GFX_0('esef_001', 0)
    Unknown36(1)
    Unknown1072(65000)
    Unknown35()
    SFX_3('esse_08')
    GFX_0('esef_001_tame_add', 0)
    GFX_0('esef_001_tame_add', 1)
    GFX_0('esef_001_tame_add', 2)
    SFX_4('bes000')
    sprite('es001_04', 6)	# 157-162
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 163-168
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 169-174
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 175-180
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 181-186
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 187-192
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 193-198
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 199-204
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 205-210
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 211-216
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 217-222
    sprite('es001_02', 6)	# 223-228
    sprite('es001_01', 6)	# 229-234
    sprite('es001_00', 6)	# 235-240
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 241-241

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('es233_00', 1)	# 1-1
    sprite('es233_01', 2)	# 2-3
    Unknown23029(11, 110, 0)
    GFX_0('eseff_DTame', 0)
    Unknown36(1)
    Unknown1072(63000)
    Unknown1056(700)
    Unknown1064(900)
    Unknown35()
    SFX_3('esse_02')
    sprite('es233_02', 2)	# 4-5
    sprite('es233_03', 2)	# 6-7
    SFX_3('esse_02')
    sprite('es233_04', 2)	# 8-9
    Unknown21015('65736566665f4454616d650000000000000000000000000000000000000000006400000000000000')
    physicsXImpulse(3500)
    sprite('es233_04', 2)	# 10-11
    Unknown1019(90)
    SFX_0('000_airdash_0')
    sprite('es233_05', 2)	# 12-13
    Unknown1019(90)
    sprite('es233_05', 2)	# 14-15
    Unknown1019(90)
    sprite('es233_06', 2)	# 16-17
    Unknown1019(50)
    SFX_0('006_swing_blade_2')
    tag_voice(0, 'bes158_0', 'bes158_1', '', '')
    sprite('es233_07', 2)	# 18-19
    Unknown1019(50)
    sprite('es233_08', 6)	# 20-25	 **attackbox here**
    GFX_0('esef_233', -1)
    SFX_3('esse_00')
    Unknown38(11, 1)
    Unknown1084(1)
    sprite('es233_09', 4)	# 26-29
    sprite('es233_10', 4)	# 30-33
    sprite('es233_11', 4)	# 34-37
    sprite('es233_12', 4)	# 38-41
    sprite('es233_13', 4)	# 42-45
    sprite('es233_14', 4)	# 46-49
    sprite('es233_15', 4)	# 50-53
    sprite('es010_02', 2)	# 54-55
    sprite('es010_01', 3)	# 56-58
    sprite('es010_00', 2)	# 59-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 22)	# 1-22
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 23-23
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('es405_05', 4)	# 24-27
    physicsXImpulse(30000)
    physicsYImpulse(18000)
    setGravity(2000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('es405_06', 4)	# 28-31
    sprite('es405_07', 3)	# 32-34
    sprite('es405_08', 3)	# 35-37
    loopRest()
    sprite('es405_09', 2)	# 38-39
    SFX_0('006_swing_blade_2')
    sprite('es405_10', 2)	# 40-41
    sprite('es405_11', 4)	# 42-45	 **attackbox here**
    SFX_3('esse_00')
    GFX_0('esef_405Eff', -1)
    Unknown1019(80)
    label(0)
    sprite('es405_12', 3)	# 46-48
    Recovery()
    setInvincible(0)
    sprite('es405_13', 3)	# 49-51
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('es405_14', 2)	# 52-53
    clearUponHandler(2)
    Unknown8000(-1, 1, 1)
    teleportRelativeX(50000)
    Unknown1084(1)
    sprite('es024_01', 2)	# 54-55
    sprite('es024_02', 3)	# 56-58
    sprite('es024_03', 3)	# 59-61
    sprite('es024_04', 3)	# 62-64
    label(0)
    sprite('es000_00', 7)	# 65-71
    sprite('es000_01', 7)	# 72-78
    sprite('es000_02', 7)	# 79-85
    sprite('es000_03', 7)	# 86-92
    sprite('es000_04', 7)	# 93-99
    sprite('es000_05', 7)	# 100-106
    sprite('es000_06', 7)	# 107-113
    sprite('es000_07', 7)	# 114-120
    sprite('es000_08', 7)	# 121-127
    sprite('es000_09', 7)	# 128-134
    sprite('es000_10', 7)	# 135-141
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('es001_00', 6)	# 142-147
    sprite('es001_01', 6)	# 148-153
    sprite('es001_02', 6)	# 154-159
    sprite('es001_03', 6)	# 160-165
    GFX_0('esef_001', 0)
    Unknown36(1)
    Unknown1072(65000)
    Unknown35()
    SFX_3('esse_08')
    GFX_0('esef_001_tame_add', 0)
    GFX_0('esef_001_tame_add', 1)
    GFX_0('esef_001_tame_add', 2)
    SFX_4('bes000')
    sprite('es001_04', 6)	# 166-171
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 172-177
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 178-183
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 184-189
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 190-195
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 196-201
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 202-207
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 208-213
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 214-219
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 220-225
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 226-231
    sprite('es001_02', 6)	# 232-237
    sprite('es001_01', 6)	# 238-243
    sprite('es001_00', 6)	# 244-249
    loopRest()
    gotoLabel(0)

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('es203_00', 2)	# 1-2
    sprite('es203_01', 2)	# 3-4
    Unknown23029(11, 110, 0)
    SFX_3('esse_02')
    sprite('es203_02', 1)	# 5-5
    sprite('es203_03', 1)	# 6-6
    SFX_3('esse_02')
    sprite('es203_01', 1)	# 7-7
    sprite('es203_04', 1)	# 8-8
    SFX_0('006_swing_blade_2')
    sprite('es203_05', 1)	# 9-9
    sprite('es203_06', 1)	# 10-10
    sprite('es203_07', 1)	# 11-11
    sprite('es203_08', 5)	# 12-16	 **attackbox here**
    GFX_0('esef_203', -1)
    SFX_3('esse_00')
    sprite('es203_09', 5)	# 17-21
    Recovery()
    Unknown2063()
    sprite('es203_10', 5)	# 22-26
    sprite('es203_11', 5)	# 27-31
    sprite('es203_12', 5)	# 32-36
    sprite('es203_13', 5)	# 37-41
    sprite('es203_14', 4)	# 42-45
    label(0)
    sprite('es000_00', 7)	# 46-52
    sprite('es000_01', 7)	# 53-59
    sprite('es000_02', 7)	# 60-66
    sprite('es000_03', 7)	# 67-73
    sprite('es000_04', 7)	# 74-80
    sprite('es000_05', 7)	# 81-87
    sprite('es000_06', 7)	# 88-94
    sprite('es000_07', 7)	# 95-101
    sprite('es000_08', 7)	# 102-108
    sprite('es000_09', 7)	# 109-115
    sprite('es000_10', 7)	# 116-122
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('es001_00', 6)	# 123-128
    sprite('es001_01', 6)	# 129-134
    sprite('es001_02', 6)	# 135-140
    sprite('es001_03', 6)	# 141-146
    GFX_0('esef_001', 0)
    Unknown36(1)
    Unknown1072(65000)
    Unknown35()
    SFX_3('esse_08')
    GFX_0('esef_001_tame_add', 0)
    GFX_0('esef_001_tame_add', 1)
    GFX_0('esef_001_tame_add', 2)
    SFX_4('bes000')
    sprite('es001_04', 6)	# 147-152
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 153-158
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 159-164
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 165-170
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 171-176
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 177-182
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 183-188
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 189-194
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 195-200
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 201-206
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 207-212
    sprite('es001_02', 6)	# 213-218
    sprite('es001_01', 6)	# 219-224
    sprite('es001_00', 6)	# 225-230
    loopRest()
    gotoLabel(0)

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('es233_00', 1)	# 1-1
    sprite('es233_01', 2)	# 2-3
    Unknown23029(11, 110, 0)
    GFX_0('eseff_DTame', 0)
    Unknown36(1)
    Unknown1072(63000)
    Unknown1056(700)
    Unknown1064(900)
    Unknown35()
    SFX_3('esse_02')
    sprite('es233_02', 2)	# 4-5
    sprite('es233_03', 2)	# 6-7
    SFX_3('esse_02')
    sprite('es233_04', 2)	# 8-9
    Unknown21015('65736566665f4454616d650000000000000000000000000000000000000000006400000000000000')
    physicsXImpulse(3500)
    sprite('es233_04', 2)	# 10-11
    Unknown1019(90)
    SFX_0('000_airdash_0')
    sprite('es233_05', 2)	# 12-13
    Unknown1019(90)
    sprite('es233_05', 2)	# 14-15
    Unknown1019(90)
    sprite('es233_06', 2)	# 16-17
    Unknown1019(50)
    SFX_0('006_swing_blade_2')
    sprite('es233_07', 2)	# 18-19
    Unknown1019(50)
    sprite('es233_08', 6)	# 20-25	 **attackbox here**
    GFX_0('esef_233', -1)
    SFX_3('esse_00')
    Unknown38(11, 1)
    Unknown1084(1)
    sprite('es233_09', 4)	# 26-29
    sprite('es233_10', 4)	# 30-33
    sprite('es233_11', 4)	# 34-37
    sprite('es233_12', 4)	# 38-41
    sprite('es233_13', 4)	# 42-45
    sprite('es233_14', 4)	# 46-49
    sprite('es233_15', 4)	# 50-53
    sprite('es010_02', 2)	# 54-55
    sprite('es010_01', 3)	# 56-58
    sprite('es010_00', 2)	# 59-60

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
    sprite('es030_01', 2)	# 1-2
    sprite('es030_02', 3)	# 3-5
    sprite('es032_00', 3)	# 6-8
    sprite('es032_01', 2)	# 9-10
    label(0)
    sprite('es032_02', 4)	# 11-14
    sprite('es032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('es032_04', 4)	# 19-22
    sprite('es032_05', 4)	# 23-26
    sprite('es032_06', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('es032_07', 4)	# 31-34
    sprite('es032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('es310_00', 2)	# 39-40
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('es310_01', 1)	# 41-41
    sprite('es310_02', 3)	# 42-44	 **attackbox here**
    Unknown1084(1)
    sprite('es310_04', 3)	# 45-47
    SFX_0('010_swing_sword_0')
    SFX_1('bes154')
    sprite('es310_04', 3)	# 48-50
    sprite('es310_05', 8)	# 51-58
    sprite('es310_06', 3)	# 59-61
    sprite('es310_07', 3)	# 62-64
    sprite('es310_08', 3)	# 65-67

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(500)
        AttackP2(50)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(60000)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown11001(-1, -2, -1)
        Unknown9016(1)
        Unknown11064(1)
        Unknown13024(0)
        JumpCancel_(0)
        Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')
    sprite('es310_02', 6)	# 1-6	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    Unknown23027()
    sprite('es311_00', 6)	# 7-12
    GFX_0('esef_ThrowEff', -1)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_3('esse_00')
    sprite('es311_01', 6)	# 13-18
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('es311_02', 6)	# 19-24
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('es311_03', 6)	# 25-30
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_1('bes153')
    sprite('es311_04', 1)	# 31-31	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown21015('657365665f5468726f77456666000000000000000000000000000000000000007500000000000000')
    RefreshMultihit()
    SFX_3('esse_01')
    sprite('es311_04', 1)	# 32-32	 **attackbox here**
    RefreshMultihit()
    sprite('es311_04', 2)	# 33-34	 **attackbox here**
    Unknown11064(0)
    RefreshMultihit()
    Damage(1000)
    Hitstop(8)
    AirPushbackX(2000)
    AirPushbackY(30000)
    YImpluseBeforeWallbounce(1800)

    def upon_11():
        Unknown13024(1)
        JumpCancel_(1)
    sprite('es311_05', 5)	# 35-39
    sprite('es311_06', 5)	# 40-44
    sprite('es311_07', 5)	# 45-49
    sprite('es311_08', 5)	# 50-54
    sprite('es311_09', 4)	# 55-58
    sprite('es311_10', 4)	# 59-62

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
    sprite('es030_01', 2)	# 1-2
    sprite('es030_02', 3)	# 3-5
    sprite('es032_00', 3)	# 6-8
    sprite('es032_01', 2)	# 9-10
    label(0)
    sprite('es032_02', 4)	# 11-14
    sprite('es032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('es032_04', 4)	# 19-22
    sprite('es032_05', 4)	# 23-26
    sprite('es032_06', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('es032_07', 4)	# 31-34
    sprite('es032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('es310_00', 2)	# 39-40
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('es310_01', 1)	# 41-41
    sprite('es310_02', 3)	# 42-44	 **attackbox here**
    Unknown1084(1)
    sprite('es310_04', 3)	# 45-47
    SFX_0('010_swing_sword_0')
    SFX_1('bes154')
    sprite('es310_04', 3)	# 48-50
    sprite('es310_05', 8)	# 51-58
    sprite('es310_06', 3)	# 59-61
    sprite('es310_07', 3)	# 62-64
    sprite('es310_08', 3)	# 65-67

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(2000)
        AttackP2(50)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9130(48)
        Unknown9142(35)
        Unknown9154(20)
        PushbackX(14000)
        Unknown9016(1)
        Unknown11099(1)
        Unknown11072(1, -180000, 0)
        Unknown13021(1)
        Unknown21005(1)
        Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')
    sprite('es310_02', 6)	# 1-6	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    Unknown23027()
    sprite('es313_00', 4)	# 7-10
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    GFX_0('esef_BackThrowEff', -1)
    SFX_3('esse_00')
    sprite('es313_01', 4)	# 11-14
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('es313_02', 4)	# 15-18
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('es313_03', 8)	# 19-26
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('es313_04', 4)	# 27-30
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('es313_05', 3)	# 31-33	 **attackbox here**
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_1('bes153')
    sprite('es313_05', 3)	# 34-36	 **attackbox here**
    Unknown21015('657365665f4261636b5468726f774566660000000000000000000000000000007600000000000000')
    RefreshMultihit()
    SFX_3('esse_01')
    sprite('es313_06', 4)	# 37-40
    sprite('es313_07', 4)	# 41-44
    sprite('es313_08', 4)	# 45-48
    sprite('es313_09', 4)	# 49-52
    sprite('es313_10', 4)	# 53-56
    sprite('es313_11', 4)	# 57-60

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('es400_00', 2)	# 1-2
    sprite('es400_01', 1)	# 3-3
    sprite('es400_01', 2)	# 4-5
    tag_voice(1, 'bes200_0', 'bes200_1', 'bes200_2', '')
    sprite('es400_04', 3)	# 6-8
    sprite('es400_05', 3)	# 9-11
    sprite('es400_06', 3)	# 12-14
    Unknown14070('ShotA_2nd')
    Unknown14070('ShotB_2nd')
    sprite('es400_07', 3)	# 15-17
    GFX_0('esef_400_zanzou', -1)
    GFX_0('es400_A', -1)
    Unknown38(4, 1)
    sprite('es400_08', 3)	# 18-20
    Unknown14072('ShotA_2nd')
    Unknown14072('ShotB_2nd')
    sprite('es400_09', 3)	# 21-23
    sprite('es400_10', 3)	# 24-26
    sprite('es400_08', 3)	# 27-29
    sprite('es400_09', 3)	# 30-32
    sprite('es400_10', 3)	# 33-35
    Unknown14074('ShotA_2nd')
    Unknown14074('ShotB_2nd')
    sprite('es400_08', 3)	# 36-38
    sprite('es400_11', 3)	# 39-41
    Recovery()
    sprite('es400_12', 3)	# 42-44

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('es400_00', 2)	# 1-2
    sprite('es400_01', 3)	# 3-5
    sprite('es400_02', 3)	# 6-8
    sprite('es400_03', 3)	# 9-11
    tag_voice(1, 'bes200_0', 'bes200_1', 'bes200_2', '')
    sprite('es400_01', 3)	# 12-14
    sprite('es400_04', 3)	# 15-17
    Unknown14070('ShotA_2nd')
    Unknown14070('ShotB_2nd')
    sprite('es400_05', 3)	# 18-20
    sprite('es400_06', 3)	# 21-23
    sprite('es400_07', 3)	# 24-26
    GFX_0('esef_400_zanzou', -1)
    GFX_0('es400_B', -1)
    Unknown38(5, 1)
    sprite('es400_08', 3)	# 27-29
    Unknown14072('ShotA_2nd')
    Unknown14072('ShotB_2nd')
    sprite('es400_09', 3)	# 30-32
    sprite('es400_10', 3)	# 33-35
    sprite('es400_08', 3)	# 36-38
    sprite('es400_09', 3)	# 39-41
    Unknown14074('ShotA_2nd')
    Unknown14074('ShotB_2nd')
    sprite('es400_10', 3)	# 42-44
    sprite('es400_11', 2)	# 45-46
    Recovery()
    sprite('es400_12', 2)	# 47-48

@State
def ShotEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('es400_00', 2)	# 1-2
    sprite('es400_01', 1)	# 3-3
    sprite('es400_01', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    sprite('es400_04', 2)	# 6-7
    sprite('es400_05', 2)	# 8-9
    sprite('es400_06', 2)	# 10-11
    sprite('es400_07', 4)	# 12-15
    GFX_0('esef_400_zanzou', -1)
    GFX_0('es400_B', -1)
    Unknown38(5, 1)
    Unknown23029(5, 126, 0)
    sprite('es400_14', 2)	# 16-17
    sprite('es400_15', 2)	# 18-19
    sprite('es400_17', 4)	# 20-23
    GFX_0('esef_400_zanzou2', -1)
    GFX_0('es400_EX_2ndEX', -1)
    Unknown38(6, 1)
    Unknown2037(1)
    sprite('es400_18', 4)	# 24-27
    tag_voice(1, 'bes201_0', 'bes201_1', 'bes201_2', '')
    sprite('es400_19', 4)	# 28-31
    sprite('es400_20', 4)	# 32-35
    sprite('es400_18', 3)	# 36-38
    sprite('es400_21', 3)	# 39-41
    sprite('es400_22', 3)	# 42-44
    Recovery()
    sprite('es400_23', 3)	# 45-47
    sprite('es400_24', 3)	# 48-50

@State
def ShotA_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23029(5, 126, 0)
        Unknown30068(1)
    sprite('es400_13', 2)	# 1-2
    sprite('es400_14', 4)	# 3-6
    sprite('es400_15', 4)	# 7-10
    sprite('es400_16', 2)	# 11-12
    sprite('es400_17', 3)	# 13-15
    GFX_0('esef_400_zanzou2', -1)
    if Unknown46(5):
        GFX_0('es400_A_2ndEX', -1)
    elif Unknown23145('ShotA'):
        GFX_0('es400_A_2nd', -1)
    else:
        GFX_0('es400_A_2ndB', -1)
    sprite('es400_18', 4)	# 16-19
    tag_voice(0, 'bes201_0', 'bes201_1', 'bes201_2', '')
    sprite('es400_19', 4)	# 20-23
    sprite('es400_20', 4)	# 24-27
    sprite('es400_18', 3)	# 28-30
    sprite('es400_21', 3)	# 31-33
    sprite('es400_22', 3)	# 34-36
    Recovery()
    sprite('es400_23', 3)	# 37-39
    sprite('es400_24', 3)	# 40-42

@State
def ShotB_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        if Unknown23145('ShotA'):
            SLOT_51 = 1

            def upon_3():
                if Unknown46(4):
                    if SLOT_2:
                        Unknown59('04000000670000000600000067000000')
                        if (SLOT_0 < 50000):
                            clearUponHandler(3)
                            Unknown21015('65733430305f425f326e640000000000000000000000000000000000000000007700000000000000')
                            Unknown21015('65733430305f425f326e644200000000000000000000000000000000000000007700000000000000')
    sprite('es400_13', 2)	# 1-2
    sprite('es400_14', 4)	# 3-6
    sprite('es400_15', 4)	# 7-10
    sprite('es400_16', 2)	# 11-12
    sprite('es400_17', 3)	# 13-15
    GFX_0('esef_400_zanzou2', -1)
    if Unknown23145('ShotA'):
        GFX_0('es400_B_2nd', -1)
    else:
        GFX_0('es400_B_2ndB', -1)
    Unknown38(6, 1)
    Unknown2037(1)
    sprite('es400_18', 4)	# 16-19
    tag_voice(0, 'bes201_0', 'bes201_1', 'bes201_2', '')
    sprite('es400_19', 4)	# 20-23
    sprite('es400_20', 4)	# 24-27
    sprite('es400_18', 3)	# 28-30
    sprite('es400_21', 3)	# 31-33
    sprite('es400_22', 3)	# 34-36
    Recovery()
    sprite('es400_23', 3)	# 37-39
    sprite('es400_24', 3)	# 40-42

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown17003()
        SLOT_59 = 1
    sprite('es401_00', 2)	# 1-2
    Unknown22004(10, 1)
    Unknown1019(150)
    Unknown1019(20)
    Unknown1037()
    Unknown1039(50)
    Unknown1021(100000)
    YAccel(20)
    sprite('es401_01', 3)	# 3-5
    sprite('es401_02', 3)	# 6-8
    tag_voice(1, 'bes200_0', 'bes200_1', 'bes200_2', '')
    sprite('es401_03', 3)	# 9-11
    sprite('es401_04', 3)	# 12-14
    sprite('es401_05', 2)	# 15-16
    Unknown14070('AirShotA_2nd')
    Unknown14070('AirShotB_2nd')
    Unknown1038()
    sprite('es401_06', 4)	# 17-20
    GFX_0('esef_401_zanzou', -1)
    GFX_0('es401_A', -1)
    sprite('es401_07', 3)	# 21-23
    Unknown14072('AirShotA_2nd')
    Unknown14072('AirShotB_2nd')
    sprite('es401_08', 3)	# 24-26
    sprite('es401_09', 3)	# 27-29
    sprite('es401_07', 3)	# 30-32
    sprite('es401_08', 3)	# 33-35
    sprite('es401_09', 3)	# 36-38
    sprite('es401_07', 3)	# 39-41
    Unknown14074('AirShotA_2nd')
    Unknown14074('AirShotB_2nd')
    sprite('es401_10', 2)	# 42-43
    sprite('es401_11', 2)	# 44-45
    sprite('es401_12', 2)	# 46-47

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown17003()
        SLOT_59 = 1
    sprite('es401_00', 2)	# 1-2
    Unknown22004(10, 1)
    Unknown1019(200)
    Unknown1019(20)
    Unknown1037()
    Unknown1039(50)
    Unknown1021(70000)
    YAccel(20)
    sprite('es401_01', 3)	# 3-5
    sprite('es401_02', 3)	# 6-8
    sprite('es401_03', 3)	# 9-11
    sprite('es401_01', 3)	# 12-14
    sprite('es401_02', 3)	# 15-17
    tag_voice(1, 'bes200_0', 'bes200_1', 'bes200_2', '')
    sprite('es401_03', 3)	# 18-20
    sprite('es401_04', 3)	# 21-23
    sprite('es401_05', 2)	# 24-25
    Unknown14070('AirShotA_2nd')
    Unknown14070('AirShotB_2nd')
    Unknown1038()
    sprite('es401_06', 4)	# 26-29
    GFX_0('esef_401_zanzou', -1)
    GFX_0('es401_B', -1)
    sprite('es401_07', 3)	# 30-32
    Unknown14072('AirShotA_2nd')
    Unknown14072('AirShotB_2nd')
    sprite('es401_08', 3)	# 33-35
    sprite('es401_09', 3)	# 36-38
    sprite('es401_07', 3)	# 39-41
    Unknown14074('AirShotA_2nd')
    Unknown14074('AirShotB_2nd')
    sprite('es401_10', 2)	# 42-43
    sprite('es401_11', 2)	# 44-45
    sprite('es401_12', 2)	# 46-47

@State
def AirShotEX():

    def upon_IMMEDIATE():
        Unknown17003()
        SLOT_59 = 1
    sprite('es401_00', 1)	# 1-1
    Unknown1019(150)
    Unknown1019(20)
    Unknown1037()
    Unknown1039(50)
    Unknown1021(100000)
    YAccel(20)
    sprite('es401_01', 2)	# 2-3
    sprite('es401_02', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'bes201_0', 'bes201_1', 'bes201_2', '')
    sprite('es401_03', 2)	# 6-7
    sprite('es401_04', 2)	# 8-9
    sprite('es401_05', 2)	# 10-11
    Unknown1038()
    sprite('es401_06', 3)	# 12-14
    GFX_0('esef_401_zanzou', -1)
    GFX_0('es401_EX', -1)
    sprite('es401_07', 1)	# 15-15
    sprite('es401_13', 3)	# 16-18
    Unknown1084(1)
    setGravity(-1200)
    sprite('es401_14', 2)	# 19-20
    sprite('es401_15', 1)	# 21-21
    sprite('es401_16', 2)	# 22-23
    Unknown1019(60)
    sprite('es401_17', 3)	# 24-26
    GFX_0('esef_401_zanzou2', -1)
    GFX_0('es401_EX_2nd', -1)
    setGravity(2000)
    sprite('es401_18', 3)	# 27-29
    sprite('es401_21', 3)	# 30-32
    sprite('es401_22', 3)	# 33-35
    sprite('es401_23', 3)	# 36-38

@State
def AirShotA_2nd():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1017()
        if Unknown23145('AirShotA'):
            SLOT_51 = 1
        Unknown30068(1)
    sprite('es401_13', 3)	# 1-3
    Unknown22004(10, 1)
    Unknown22001(-1)
    Unknown22003(-1)
    Unknown1084(1)
    setGravity(-1200)
    sprite('es401_14', 3)	# 4-6
    sprite('es401_15', 3)	# 7-9
    sprite('es401_16', 3)	# 10-12
    Unknown1018()
    Unknown1019(60)
    sprite('es401_17', 3)	# 13-15
    GFX_0('esef_401_zanzou2', -1)
    if SLOT_51:
        GFX_0('es401_A_2nd', -1)
    else:
        GFX_0('es401_A_2ndB', -1)
    tag_voice(0, 'bes201_0', 'bes201_1', 'bes201_2', '')
    setGravity(1500)
    sprite('es401_18', 3)	# 16-18
    loopRest()
    Unknown19(0, 2, 51)
    sprite('es401_19', 3)	# 19-21
    sprite('es401_20', 3)	# 22-24
    sprite('es401_18', 3)	# 25-27
    sprite('es401_19', 3)	# 28-30
    label(0)
    sprite('es401_21', 3)	# 31-33
    sprite('es401_22', 3)	# 34-36
    sprite('es401_23', 3)	# 37-39

@State
def AirShotB_2nd():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1017()
        if Unknown23145('AirShotA'):
            SLOT_51 = 1
        Unknown30068(1)
    sprite('es401_13', 3)	# 1-3
    Unknown22004(10, 1)
    Unknown22001(-1)
    Unknown22003(-1)
    Unknown1084(1)
    setGravity(-1200)
    sprite('es401_14', 3)	# 4-6
    sprite('es401_15', 3)	# 7-9
    sprite('es401_16', 3)	# 10-12
    Unknown1018()
    Unknown1019(60)
    sprite('es401_17', 3)	# 13-15
    GFX_0('esef_401_zanzou2', -1)
    if SLOT_51:
        GFX_0('es401_B_2nd', -1)
    else:
        GFX_0('es401_B_2ndB', -1)
    tag_voice(0, 'bes201_0', 'bes201_1', 'bes201_2', '')
    setGravity(1500)
    sprite('es401_18', 3)	# 16-18
    loopRest()
    Unknown19(0, 2, 51)
    sprite('es401_19', 3)	# 19-21
    sprite('es401_20', 3)	# 22-24
    sprite('es401_18', 3)	# 25-27
    sprite('es401_19', 3)	# 28-30
    label(0)
    sprite('es401_21', 3)	# 31-33
    sprite('es401_22', 3)	# 34-36
    sprite('es401_23', 3)	# 37-39

@State
def SpecialThrow():

    def upon_IMMEDIATE():
        Unknown17011('SpecialThrowExe', 2, 0, 0)
        AttackP1(100)
        AttackP2(100)
        Unknown11032('e093040001000000ffffffffffffffff')
        Unknown11045(1)
        Unknown11002(-1)
        Unknown30061(0)
        Unknown30048(1)
        Unknown11061(1)
        Unknown11058('0100000000000000000000000000000000000000')
        sendToLabelUpon(2, 2)
    sprite('es404_00', 2)	# 1-2
    sprite('es404_01', 1)	# 3-3
    sprite('es404_01', 1)	# 4-4
    SFX_0('000_airdash_0')
    sprite('es404_02', 2)	# 5-6
    sprite('es404_03', 2)	# 7-8
    sprite('es035_00ex00', 2)	# 9-10
    tag_voice(1, 'bes204_0', 'bes204_1', 'bes204_2', '')
    physicsXImpulse(20000)
    physicsYImpulse(26000)
    setGravity(1500)
    Unknown23087(65000)
    Unknown8001(0, 0)
    sprite('es035_01ex00', 3)	# 11-13
    sprite('es035_02ex00', 3)	# 14-16
    sprite('es035_03ex00', 2)	# 17-18
    sprite('es035_04ex00', 2)	# 19-20
    sprite('es035_05ex00', 2)	# 21-22
    sprite('es404_04', 3)	# 23-25	 **attackbox here**
    Unknown1039(120)
    StartMultihit()
    sprite('es404_05', 3)	# 26-28	 **attackbox here**
    sprite('es404_04', 3)	# 29-31	 **attackbox here**
    sprite('es404_05', 3)	# 32-34	 **attackbox here**
    label(1)
    sprite('es404_04', 3)	# 35-37	 **attackbox here**
    Recovery()
    Unknown23027()
    sprite('es404_05', 3)	# 38-40	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es404_17', 5)	# 41-45
    physicsYImpulse(7000)
    setGravity(1200)
    Unknown1019(40)
    Unknown18009(1)
    Unknown8000(-1, 1, 1)
    sendToLabelUpon(2, 3)
    sprite('es404_18', 5)	# 46-50
    sprite('es404_19', 32767)	# 51-32817
    label(3)
    sprite('es404_20', 3)	# 32818-32820
    Unknown1019(50)
    Unknown8000(-1, 1, 1)
    sprite('es404_21', 15)	# 32821-32835
    Unknown1084(1)
    SFX_1('bes154')
    sprite('es404_22', 3)	# 32836-32838
    sprite('es404_23', 3)	# 32839-32841

@State
def SpecialThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 1, 0)
        AttackLevel_(3)
        Damage(2500)
        AttackP2(75)
        AirUntechableTime(100)
        Unknown11091(5)
        Hitstop(0)
        Unknown11001(-1, -1, -1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(1600)
        Unknown30061(0)
        Unknown11072(1, 60000, -50000)
        Unknown11108('03000000')
        Unknown11078(1)
        Unknown11002(-1)

        def upon_STATE_END():
            setGravity(1500)
        Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
        Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')
    sprite('es404_06', 6)	# 1-6
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('es404_07', 6)	# 7-12
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('es404_08', 20)	# 13-32
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('es404_09', 5)	# 33-37
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    tag_voice(1, 'bes205_0', 'bes205_1', 'bes205_2', '')
    sprite('es404_10', 5)	# 38-42	 **attackbox here**
    teleportRelativeX(-30000)
    Unknown1007(-50000)
    physicsXImpulse(-3000)
    physicsYImpulse(16000)
    setGravity(1000)
    GFX_0('esef_404_kick', -1)
    SFX_0('004_swing_grap_1_1')
    SFX_3('esse_11')
    sprite('es404_11', 5)	# 43-47
    sprite('es404_12', 4)	# 48-51
    sprite('es404_13', 4)	# 52-55
    sprite('es404_14', 4)	# 56-59
    sprite('es404_15', 4)	# 60-63
    sprite('es404_16', 4)	# 64-67
    Unknown1043()
    label(1)
    sprite('es020_07', 3)	# 68-70
    sprite('es020_08', 3)	# 71-73
    gotoLabel(1)

@State
def MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        GroundedHitstunAnimation(3)
        AirHitstunAnimation(10)
        AirPushbackY(-60000)
        YImpluseBeforeWallbounce(0)
        PushbackX(19800)
        Unknown9154(22)
        AirUntechableTime(40)
        Unknown11058('0100000000000000000000000000000000000000')
        HitOverhead(2)
        Unknown9016(1)
        JumpCancel_(0)
        sendToLabelUpon(2, 0)
    sprite('es405_00', 1)	# 1-1
    sprite('es405_01', 1)	# 2-2
    sprite('es405_02', 2)	# 3-4
    sprite('es405_03', 1)	# 5-5
    sprite('es405_04', 3)	# 6-8
    Unknown7007('6265733230365f300000000000000000640000006265733230365f310000000000000000640000006265733230365f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23087(30000)
    physicsXImpulse(16000)
    physicsYImpulse(20000)
    setGravity(1500)
    Unknown8001(2, 100)
    SFX_0('000_airdash_0')
    sprite('es405_05', 4)	# 9-12
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000001000000')
    sprite('es405_06', 4)	# 13-16
    sprite('es405_07', 3)	# 17-19
    if CheckInput(0xa):
        sendToLabelUpon(2, 3)
        SLOT_51 = 1
    else:
        sendToLabelUpon(2, 1)
    sprite('es405_08', 3)	# 20-22
    loopRest()
    if SLOT_51:
        _gotolabel(2)
    sprite('es405_09', 2)	# 23-24
    SFX_0('006_swing_blade_2')
    sprite('es405_10', 2)	# 25-26
    sprite('es405_11', 4)	# 27-30	 **attackbox here**
    SFX_3('esse_00')
    if SLOT_2:
        GFX_0('esef_405EffEX', -1)
    else:
        GFX_0('esef_405Eff', -1)
    Unknown1019(80)
    label(0)
    sprite('es405_12', 3)	# 31-33
    Recovery()
    setInvincible(0)
    sprite('es405_13', 3)	# 34-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('es405_14', 2)	# 37-38
    clearUponHandler(2)
    Unknown8000(-1, 1, 1)
    teleportRelativeX(50000)
    Unknown1084(1)
    sprite('es024_01', 2)	# 39-40
    sprite('es024_02', 3)	# 41-43
    sprite('es024_03', 3)	# 44-46
    sprite('es024_04', 3)	# 47-49
    ExitState()
    label(2)
    sprite('es405_08', 3)	# 50-52
    sprite('es405_07', 3)	# 53-55
    sprite('es405_08', 3)	# 56-58
    SFX_0('006_swing_blade_2')
    sprite('es405_15', 2)	# 59-60
    sprite('es405_16', 30)	# 61-90
    label(3)
    sprite('es405_17', 3)	# 91-93	 **attackbox here**
    clearUponHandler(2)
    Unknown8000(-1, 1, 1)
    Unknown1084(1)
    Unknown18009(1)
    ScreenShake(8000, 8000)
    Unknown23159('MidAssault_Tame')
    AttackLevel_(4)
    Damage(2200)
    AttackP2(75)
    GroundedHitstunAnimation(10)
    Unknown9118(35)
    Unknown9202(8)
    SFX_3('esse_00')
    if SLOT_2:
        GFX_0('esef_405EffEX', -1)
    else:
        GFX_0('esef_405Eff', -1)
    sprite('es405_18', 3)	# 94-96
    Recovery()
    setInvincible(0)
    sprite('es405_19', 3)	# 97-99
    sprite('es405_20', 3)	# 100-102
    sprite('es405_21', 2)	# 103-104
    sprite('es405_22', 2)	# 105-106

@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AirPushbackX(4000)
        AirPushbackY(22000)
        PushbackX(2000)
        Unknown9154(24)
        AirUntechableTime(40)
        Unknown11056(0)
        Unknown9016(1)
        Unknown30055('90d003001e0000001e000000')

        def upon_3():
            (SLOT_19 < 300000)
            if op(5, 2, 0, 2, 51):
                sendToLabel(0)
        Unknown2004(1, 0)
    sprite('es406_00', 3)	# 1-3
    sprite('es406_01', 3)	# 4-6
    tag_voice(1, 'bes207_0', 'bes207_1', 'bes207_2', '')
    physicsXImpulse(45000)
    Unknown8007(100, 1, 0)
    SFX_0('001_airbackdash_0')
    sprite('es406_02', 3)	# 7-9
    Unknown8006(100, 1, 0)
    sprite('es406_01', 3)	# 10-12
    Unknown8006(100, 1, 0)
    SLOT_51 = 1
    sprite('es406_02', 3)	# 13-15
    Unknown8006(100, 1, 0)
    label(0)
    sprite('es406_03', 4)	# 16-19
    clearUponHandler(3)
    Unknown8010(100, 1, 0)
    SFX_0('006_swing_blade_2')
    Unknown1019(60)
    SLOT_51 = 0
    Unknown14070('Assault_2nd')
    sprite('es406_04', 2)	# 20-21
    Unknown1019(60)
    sprite('es406_05', 2)	# 22-23	 **attackbox here**
    SFX_3('esse_00')
    GFX_0('esef_406Eff', -1)
    Unknown1084(1)
    sprite('es406_05', 2)	# 24-25	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('es406_06', 2)	# 26-27
    sprite('es406_06', 2)	# 28-29
    Unknown14072('Assault_2nd')
    sprite('es406_07', 4)	# 30-33
    Unknown14073('Assault_2nd')
    Unknown21015('657365665f3430364566660000000000000000000000000000000000000000006500000000000000')
    Unknown21015('657365665f3430364566664558000000000000000000000000000000000000006600000000000000')
    sprite('es406_08', 4)	# 34-37
    sprite('es202_09ex00', 4)	# 38-41
    sprite('es202_10ex00', 3)	# 42-44
    sprite('es202_11ex00', 3)	# 45-47

@State
def Assault_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(12000)
        AirPushbackY(29000)
        YImpluseBeforeWallbounce(1600)
        PushbackX(19800)
        AirUntechableTime(55)
        Unknown9016(1)
        Unknown30068(1)
        Unknown21015('657365665f3430364566660000000000000000000000000000000000000000006f00000000000000')
        Unknown21015('657365665f3430364566664558000000000000000000000000000000000000006f00000000000000')
        Unknown21015('657365665f3430364566666164640000000000000000000000000000000000006f00000000000000')
    sprite('es406_07', 1)	# 1-1
    sprite('es406_08', 1)	# 2-2
    sprite('es407_00', 2)	# 3-4
    physicsXImpulse(10000)
    sprite('es407_01', 2)	# 5-6
    SFX_0('006_swing_blade_2')
    sprite('es407_02', 2)	# 7-8
    sprite('es407_03', 2)	# 9-10
    sendToLabelUpon(2, 2)
    Unknown1019(20)
    physicsYImpulse(20000)
    setGravity(1500)
    sprite('es407_04', 4)	# 11-14	 **attackbox here**
    tag_voice(0, 'bes208_0', 'bes208_1', 'bes208_2', '')
    GFX_0('esef_406Eff2', -1)
    sprite('es407_05', 4)	# 15-18
    Recovery()
    sprite('es407_06', 4)	# 19-22
    sprite('es407_07', 4)	# 23-26
    sprite('es407_08', 4)	# 27-30
    sprite('es407_09', 4)	# 31-34
    sprite('es407_10', 4)	# 35-38
    label(1)
    sprite('es020_07', 3)	# 39-41
    sprite('es020_08', 3)	# 42-44
    gotoLabel(1)
    label(2)
    sprite('es024_00', 1)	# 45-45
    Unknown1084(1)
    sprite('es024_01', 4)	# 46-49
    sprite('es024_02', 4)	# 50-53
    sprite('es024_03', 4)	# 54-57

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1400)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirUntechableTime(55)
        PushbackX(8000)
        Unknown11056(2)
        Unknown9016(1)

        def upon_78():
            SLOT_51 = 1
    sprite('es402_00', 2)	# 1-2
    Unknown1084(1)
    SFX_0('006_swing_blade_2')
    sprite('es402_01', 3)	# 3-5
    sprite('es402_02', 3)	# 6-8
    sprite('es402_03', 2)	# 9-10
    sprite('es402_04', 2)	# 11-12
    sprite('es402_05', 3)	# 13-15	 **attackbox here**
    GFX_0('esef_402_zanzou', -1)
    Unknown38(4, 1)
    tag_voice(1, 'bes202_0', 'bes202_1', 'bes202_2', '')
    sprite('es402_06', 2)	# 16-17
    setInvincible(0)
    sprite('es402_07', 2)	# 18-19
    sprite('es402_08', 2)	# 20-21
    sprite('es402_09', 3)	# 22-24
    physicsXImpulse(40000)
    SFX_0('006_swing_blade_2')
    sprite('es402_10', 3)	# 25-27
    physicsXImpulse(30000)
    sprite('es402_11', 1)	# 28-28	 **attackbox here**
    sendToLabelUpon(2, 2)
    Unknown4020(4)

    def upon_ON_HIT_OR_BLOCK():
        GFX_0('esef_402Eff', -1)
        clearUponHandler(10)
    SFX_3('esse_07')
    SFX_3('esse_00')
    physicsYImpulse(28000)
    setGravity(1500)
    Unknown1019(50)
    Unknown1028(-1000)
    GroundedHitstunAnimation(10)
    AirPushbackY(50000)
    Unknown9215()
    RefreshMultihit()
    Unknown14070('AntiAir2nd')
    sprite('es402_11', 2)	# 29-30	 **attackbox here**
    clearUponHandler(10)
    GFX_0('esef_402Eff', -1)
    sprite('es402_12', 3)	# 31-33	 **attackbox here**
    sprite('es402_13', 3)	# 34-36	 **attackbox here**
    sprite('es402_14', 4)	# 37-40
    Unknown4020(0)
    sprite('es402_15', 4)	# 41-44
    Unknown1019(0)
    Unknown1034(0)
    sprite('es402_16', 4)	# 45-48
    sprite('es402_17', 4)	# 49-52
    if SLOT_51:
        Unknown14072('AntiAir2nd')
    sprite('es402_18', 4)	# 53-56
    Unknown14074('AntiAir2nd')
    sprite('es402_19', 4)	# 57-60
    sprite('es402_20', 4)	# 61-64
    label(1)
    sprite('es020_07', 3)	# 65-67
    sprite('es020_08', 3)	# 68-70
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es024_00', 4)	# 71-74
    clearUponHandler(2)
    Unknown1084(1)
    sprite('es024_01', 5)	# 75-79
    sprite('es024_02', 5)	# 80-84
    sprite('es024_03', 5)	# 85-89

@State
def AntiAir2nd():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        Unknown30068(1)
        Unknown14083(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 2)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)

        def upon_43():
            if (SLOT_48 == 139):
                Recovery()
    sprite('es403_00', 4)	# 1-4
    physicsYImpulse(25000)
    setGravity(1500)
    SLOT_12 = SLOT_40
    if SLOT_38:
        Unknown1019(-5)
    else:
        Unknown1019(5)
    sprite('es403_01', 4)	# 5-8
    sprite('es403_02', 4)	# 9-12
    Unknown1019(50)
    sprite('es403_03', 4)	# 13-16
    Unknown1019(30)
    sprite('es403_04', 4)	# 17-20
    tag_voice(0, 'bes203_0', 'bes203_1', 'bes203_2', '')
    SFX_3('esse_01')
    GFX_0('es403_Atk', -1)
    sprite('es403_05', 4)	# 21-24
    physicsXImpulse(0)
    physicsYImpulse(20000)
    sprite('es403_06', 4)	# 25-28
    sprite('es403_07', 4)	# 29-32
    sprite('es403_08', 4)	# 33-36
    sprite('es403_09', 4)	# 37-40
    label(1)
    sprite('es020_07', 3)	# 41-43
    sprite('es020_08', 3)	# 44-46
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es024_00', 4)	# 47-50
    clearUponHandler(2)
    Unknown1084(1)
    sprite('es024_01', 5)	# 51-55
    sprite('es024_02', 5)	# 56-60
    sprite('es024_03', 5)	# 61-65

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1400)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(55)
        Unknown11056(2)
        Unknown9016(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 2)

        def upon_78():
            SLOT_51 = 1
    sprite('es402_00', 1)	# 1-1
    Unknown1084(1)
    physicsYImpulse(12000)
    setGravity(1000)
    SFX_0('006_swing_blade_2')
    sprite('es402_01', 2)	# 2-3
    sprite('es402_02', 2)	# 4-5
    sprite('es402_03', 2)	# 6-7
    sprite('es402_04', 2)	# 8-9
    sprite('es402_05', 3)	# 10-12	 **attackbox here**
    GFX_0('esef_402_zanzou', -1)
    Unknown38(4, 1)
    tag_voice(1, 'bes202_0', 'bes202_1', 'bes202_2', '')
    sprite('es402_06', 2)	# 13-14
    setInvincible(0)
    sprite('es402_07', 2)	# 15-16
    sprite('es402_08', 2)	# 17-18
    sprite('es402_09', 3)	# 19-21
    physicsXImpulse(15000)
    physicsYImpulse(14000)
    setGravity(1500)
    SFX_0('006_swing_blade_2')
    sprite('es402_10', 3)	# 22-24
    sprite('es402_11', 1)	# 25-25	 **attackbox here**
    Unknown4020(4)

    def upon_ON_HIT_OR_BLOCK():
        GFX_0('esef_402Eff', -1)
        clearUponHandler(10)
    SFX_3('esse_07')
    SFX_3('esse_00')
    physicsYImpulse(28000)
    Unknown1028(-1000)
    AirPushbackY(50000)
    Unknown1028(-1000)
    GroundedHitstunAnimation(10)
    Unknown9215()
    RefreshMultihit()
    Unknown14070('AirAntiAir2nd')
    sprite('es402_11', 2)	# 26-27	 **attackbox here**
    GFX_0('esef_402Eff', -1)
    sprite('es402_12', 3)	# 28-30	 **attackbox here**
    sprite('es402_13', 3)	# 31-33	 **attackbox here**
    sprite('es402_14', 4)	# 34-37
    Unknown4020(0)
    sprite('es402_15', 4)	# 38-41
    Unknown1019(0)
    Unknown1034(0)
    sprite('es402_16', 4)	# 42-45
    sprite('es402_17', 4)	# 46-49
    if SLOT_51:
        Unknown14072('AirAntiAir2nd')
    sprite('es402_18', 4)	# 50-53
    Unknown14074('AirAntiAir2nd')
    sprite('es402_19', 4)	# 54-57
    sprite('es402_20', 4)	# 58-61
    label(1)
    sprite('es020_07', 3)	# 62-64
    sprite('es020_08', 3)	# 65-67
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es024_00', 4)	# 68-71
    clearUponHandler(2)
    Unknown1084(1)
    sprite('es024_01', 5)	# 72-76
    sprite('es024_02', 5)	# 77-81
    sprite('es024_03', 5)	# 82-86

@State
def AirAntiAir2nd():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        Unknown30068(1)
        Unknown14083(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 2)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)

        def upon_43():
            if (SLOT_48 == 139):
                Recovery()
    sprite('es403_00', 4)	# 1-4
    physicsYImpulse(25000)
    setGravity(1500)
    SLOT_12 = SLOT_40
    if SLOT_38:
        Unknown1019(-5)
    else:
        Unknown1019(5)
    sprite('es403_01', 4)	# 5-8
    sprite('es403_02', 4)	# 9-12
    Unknown1019(50)
    sprite('es403_03', 4)	# 13-16
    Unknown1019(30)
    sprite('es403_04', 4)	# 17-20
    SFX_1('es203')
    tag_voice(0, 'bes203_0', 'bes203_1', 'bes203_2', '')
    SFX_3('esse_01')
    GFX_0('es403_Atk', -1)
    sprite('es403_05', 4)	# 21-24
    physicsXImpulse(0)
    physicsYImpulse(20000)
    sprite('es403_06', 4)	# 25-28
    sprite('es403_07', 4)	# 29-32
    sprite('es403_08', 4)	# 33-36
    sprite('es403_09', 4)	# 37-40
    label(1)
    sprite('es020_07', 3)	# 41-43
    sprite('es020_08', 3)	# 44-46
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es024_00', 4)	# 47-50
    clearUponHandler(2)
    Unknown1084(1)
    sprite('es024_01', 5)	# 51-55
    sprite('es024_02', 5)	# 56-60
    sprite('es024_03', 5)	# 61-65

@State
def UltimateShot_LandA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
    sprite('es430_00', 2)	# 1-2
    setInvincible(1)
    sprite('es430_01', 4)	# 3-6
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'bes250_0', 'bes250_1', '', '')
    sprite('es430_02', 4)	# 7-10
    sprite('es430_03', 4)	# 11-14
    sprite('es430_04', 4)	# 15-18
    GFX_0('esef_430EffStart', -1)
    sprite('es430_05', 4)	# 19-22
    sprite('es430_06', 4)	# 23-26
    sprite('es430_07', 4)	# 27-30
    sprite('es430_08', 4)	# 31-34
    sprite('es430_09', 4)	# 35-38
    Unknown21015('657365665f3433304566665374617274000000000000000000000000000000007000000000000000')
    sprite('es430_10', 4)	# 39-42
    sprite('es430_11', 4)	# 43-46
    Unknown2015(150)
    teleportRelativeX(60000)
    sprite('es430_12', 4)	# 47-50
    teleportRelativeX(30000)
    sprite('es430_13', 4)	# 51-54
    teleportRelativeX(30000)
    sprite('es430_14', 4)	# 55-58
    tag_voice(0, 'bes251_0', 'bes251_1', '', '')
    Unknown21015('657365665f3433304566665374617274000000000000000000000000000000007100000000000000')
    GFX_0('es430LandA', -1)
    sendToLabelUpon(2, 1)
    physicsXImpulse(20000)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown2015(-1)
    sprite('es430_15', 4)	# 59-62
    sprite('es430_16', 4)	# 63-66
    setInvincible(0)
    Unknown1019(60)
    sprite('es430_17', 4)	# 67-70
    Unknown1019(80)
    sprite('es430_18', 4)	# 71-74
    Unknown1019(80)
    sprite('es430_19', 4)	# 75-78
    Unknown1019(80)
    sprite('es430_20', 100)	# 79-178
    label(1)
    sprite('es024_01', 3)	# 179-181
    teleportRelativeX(40000)
    Unknown1084(1)
    sprite('es024_02', 3)	# 182-184
    sprite('es024_03', 3)	# 185-187
    sprite('es024_04', 3)	# 188-190

@State
def UltimateShot_LandAOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
    sprite('es430_00', 2)	# 1-2
    setInvincible(1)
    sprite('es430_01', 4)	# 3-6
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'bes250_0', 'bes250_1', '', '')
    sprite('es430_02', 4)	# 7-10
    sprite('es430_03', 4)	# 11-14
    sprite('es430_04', 4)	# 15-18
    GFX_0('esef_430EffStartOD', -1)
    sprite('es430_05', 4)	# 19-22
    sprite('es430_06', 4)	# 23-26
    sprite('es430_07', 4)	# 27-30
    sprite('es430_08', 4)	# 31-34
    sprite('es430_09', 4)	# 35-38
    Unknown21015('657365665f34333045666653746172744f4400000000000000000000000000007200000000000000')
    sprite('es430_10', 4)	# 39-42
    sprite('es430_11', 4)	# 43-46
    Unknown2015(150)
    teleportRelativeX(60000)
    sprite('es430_12', 4)	# 47-50
    teleportRelativeX(30000)
    sprite('es430_13', 4)	# 51-54
    teleportRelativeX(30000)
    sprite('es430_14', 4)	# 55-58
    tag_voice(0, 'bes251_0', 'bes251_1', '', '')
    Unknown21015('657365665f34333045666653746172744f4400000000000000000000000000007300000000000000')
    GFX_0('es430LandAOD', -1)
    sendToLabelUpon(2, 1)
    physicsXImpulse(20000)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown2015(-1)
    sprite('es430_15', 4)	# 59-62
    sprite('es430_16', 4)	# 63-66
    setInvincible(0)
    Unknown1019(60)
    sprite('es430_17', 4)	# 67-70
    Unknown1019(80)
    sprite('es430_18', 4)	# 71-74
    Unknown1019(80)
    sprite('es430_19', 4)	# 75-78
    Unknown1019(80)
    sprite('es430_20', 100)	# 79-178
    label(1)
    sprite('es024_01', 3)	# 179-181
    teleportRelativeX(40000)
    Unknown1084(1)
    sprite('es024_02', 3)	# 182-184
    sprite('es024_03', 3)	# 185-187
    sprite('es024_04', 3)	# 188-190

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(2500)
        AttackP1(80)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown9154(60)
        Unknown11056(0)
        Unknown11069('UltimateAssault')
        Unknown11064(1)
        Unknown30048(1)
        Unknown23055('')

        def upon_12():
            clearUponHandler(12)
            Unknown13024(0)
            Unknown21005(1)
            Unknown13021(1)
            sendToLabel(0)
            Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')

        def upon_STATE_END():
            Unknown26('esef_431Camera')
            Unknown3001(255)
            Unknown3004(0)

        def upon_3():
            if (not SLOT_158):
                clearUponHandler(3)
                Unknown26('esef_431Camera')
    sprite('es431_00', 2)	# 1-2
    setInvincible(1)
    sprite('es431_01', 1)	# 3-3
    sprite('es431_01', 3)	# 4-6
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('es431_02', 4)	# 7-10
    sprite('es431_03', 16)	# 11-26
    GFX_0('esef_431Eff', -1)
    tag_voice(1, 'bes252_0', 'bes252_1', '', '')
    sprite('es431_04', 6)	# 27-32
    sprite('es431_05', 6)	# 33-38
    sprite('es431_06', 6)	# 39-44
    sprite('es431_07', 5)	# 45-49
    sprite('es431_08', 3)	# 50-52
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006800000000000000')
    Unknown3029(1)
    physicsXImpulse(15000)
    physicsYImpulse(18000)
    SFX_3('esse_04')
    SFX_0('000_airdash_0')
    sprite('es431_09', 3)	# 53-55	 **attackbox here**
    Unknown1019(700)
    physicsYImpulse(0)
    sprite('es431_10', 3)	# 56-58	 **attackbox here**
    sprite('es431_09', 3)	# 59-61	 **attackbox here**
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    sprite('es431_11', 4)	# 62-65
    setInvincible(0)
    Unknown1019(70)
    teleportRelativeY(0)
    sprite('es110_03ex00', 4)	# 66-69
    Unknown1019(70)
    sprite('es110_04ex00', 4)	# 70-73
    Unknown1019(70)
    sprite('es110_05ex00', 4)	# 74-77
    Unknown1019(70)
    sprite('es110_06ex00', 4)	# 78-81
    Unknown1019(70)
    sprite('es110_07ex00', 4)	# 82-85
    Unknown1084(1)
    Unknown3029(0)
    ExitState()
    label(0)
    sprite('es431_12', 5)	# 86-90
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    Unknown1019(50)
    sprite('es431_13', 5)	# 91-95
    Unknown1019(50)
    sprite('es431_14', 5)	# 96-100
    Unknown2017(0)
    Unknown1019(50)
    sprite('es431_15', 5)	# 101-105
    Unknown1019(50)
    Unknown3004(-8)
    sprite('es431_16', 5)	# 106-110
    sprite('es431_17', 5)	# 111-115
    GFX_0('esef_431Eff2', -1)
    SFX_3('esse_09')
    SFX_3('esse_09')
    tag_voice(0, 'bes253_0', 'bes253_1', '', '')
    sprite('es431_18', 3)	# 116-118	 **attackbox here**
    Unknown3029(0)
    Unknown1019(0)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(0)
    sprite('es431_18', 9)	# 119-127	 **attackbox here**
    GFX_0('esef_431EffSlash', -1)
    GFX_0('esef_431Camera', -1)
    GFX_0('esef_431EffEsRay', 100)
    Unknown2015(50)
    physicsXImpulse(96000)
    Unknown1028(-8000)
    Unknown3004(42)
    Damage(4300)
    Unknown11091(33)
    AttackP2(60)
    Hitstop(0)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    PushbackX(-30000)
    Unknown9130(50)
    Unknown9142(200)
    Unknown9132(50)
    Unknown9144(200)
    Unknown9016(1)
    Unknown11023(1)
    Unknown11069('')
    Unknown11064(0)
    Unknown11066(1)
    Unknown11084(1)
    Unknown13024(1)
    RefreshMultihit()
    sprite('es431_18', 3)	# 128-130	 **attackbox here**
    Unknown2017(1)
    Unknown2015(-1)
    GFX_0('esef_431EffScrew', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('es431_19', 2)	# 131-132	 **attackbox here**
    sprite('es431_20', 2)	# 133-134	 **attackbox here**
    sprite('es431_21', 2)	# 135-136	 **attackbox here**
    sprite('es431_22', 2)	# 137-138	 **attackbox here**
    sprite('es431_19', 2)	# 139-140	 **attackbox here**
    sprite('es431_20', 2)	# 141-142	 **attackbox here**
    sprite('es431_21', 2)	# 143-144	 **attackbox here**
    sprite('es431_22', 2)	# 145-146	 **attackbox here**
    sprite('es431_19', 3)	# 147-149	 **attackbox here**
    sprite('es431_20', 3)	# 150-152	 **attackbox here**
    sprite('es431_21', 3)	# 153-155	 **attackbox here**
    sprite('es431_22', 3)	# 156-158	 **attackbox here**
    sprite('es431_19', 4)	# 159-162	 **attackbox here**
    sprite('es431_20', 4)	# 163-166	 **attackbox here**
    sprite('es431_21', 4)	# 167-170	 **attackbox here**
    sprite('es431_22', 4)	# 171-174	 **attackbox here**
    sprite('es431_19', 4)	# 175-178	 **attackbox here**
    sprite('es431_20', 4)	# 179-182	 **attackbox here**
    sprite('es431_21', 4)	# 183-186	 **attackbox here**
    sprite('es431_22', 3)	# 187-189	 **attackbox here**
    sprite('es431_22', 1)	# 190-190	 **attackbox here**
    Unknown26('esef_431Camera')
    sprite('es431_23', 5)	# 191-195
    sprite('es431_24', 5)	# 196-200

@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(2500)
        AttackP1(80)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown9154(60)
        Unknown11056(0)
        Unknown12051(0)
        Unknown11069('UltimateAssaultOD')
        Unknown11064(1)
        Unknown23055('')
        Unknown30048(1)

        def upon_12():
            clearUponHandler(12)
            Unknown13024(0)
            Unknown21005(1)
            Unknown13021(1)
            sendToLabel(0)
            Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')

        def upon_STATE_END():
            Unknown26('esef_431Camera')
            Unknown3001(255)
            Unknown3004(0)

        def upon_3():
            if (not SLOT_158):
                clearUponHandler(3)
                Unknown26('esef_431Camera')
    sprite('es431_00', 2)	# 1-2
    setInvincible(1)
    sprite('es431_01', 1)	# 3-3
    sprite('es431_01', 3)	# 4-6
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('es431_02', 4)	# 7-10
    sprite('es431_03', 16)	# 11-26
    tag_voice(1, 'bes252_0', 'bes252_1', '', '')
    GFX_0('esef_431Eff', -1)
    sprite('es431_04', 6)	# 27-32
    sprite('es431_05', 6)	# 33-38
    sprite('es431_06', 6)	# 39-44
    sprite('es431_07', 5)	# 45-49
    sprite('es431_08', 3)	# 50-52
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006800000000000000')
    Unknown3029(1)
    physicsXImpulse(15000)
    physicsYImpulse(18000)
    SFX_3('esse_04')
    SFX_0('000_airdash_0')
    sprite('es431_09', 3)	# 53-55	 **attackbox here**
    Unknown1019(500)
    physicsYImpulse(0)
    sprite('es431_10', 3)	# 56-58	 **attackbox here**
    sprite('es431_09', 3)	# 59-61	 **attackbox here**
    sprite('es431_11', 4)	# 62-65
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    setInvincible(0)
    Unknown1019(70)
    teleportRelativeY(0)
    sprite('es110_03ex00', 4)	# 66-69
    Unknown1019(70)
    sprite('es110_04ex00', 4)	# 70-73
    Unknown1019(70)
    sprite('es110_05ex00', 4)	# 74-77
    Unknown1019(70)
    sprite('es110_06ex00', 4)	# 78-81
    Unknown1019(70)
    sprite('es110_07ex00', 4)	# 82-85
    Unknown3029(0)
    Unknown1084(1)
    ExitState()
    label(0)
    sprite('es431_12', 5)	# 86-90
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    Unknown1019(50)
    Unknown23024(2)
    sprite('es431_13', 5)	# 91-95
    Unknown1019(50)
    sprite('es431_14', 5)	# 96-100
    Unknown2017(0)
    Unknown1019(50)
    sprite('es431_15', 5)	# 101-105
    Unknown1019(50)
    Unknown3004(-8)
    sprite('es431_16', 5)	# 106-110
    sprite('es431_17', 5)	# 111-115
    GFX_0('esef_431Eff2', -1)
    SFX_3('esse_09')
    SFX_3('esse_09')
    tag_voice(0, 'bes253_0', 'bes253_1', '', '')
    sprite('es431_18', 3)	# 116-118	 **attackbox here**
    Unknown1019(0)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(0)
    Unknown3029(0)
    sprite('es431_18', 3)	# 119-121	 **attackbox here**
    GFX_0('esef_431EffSlashOD', -1)
    GFX_0('esef_431Camera', -1)
    GFX_0('esef_431EffEsRay', 100)
    SFX_0('025_cleanhit_slash')
    Unknown2015(50)
    physicsXImpulse(120000)
    Unknown1028(-10000)
    Unknown3004(42)
    Damage(250)
    Unknown11091(25)
    Hitstop(0)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    PushbackX(-30000)
    Unknown9130(50)
    Unknown9142(200)
    Unknown9132(50)
    Unknown9144(200)
    Unknown9016(1)
    Unknown11057(600)
    Unknown11023(1)
    Unknown11066(1)
    Unknown11084(1)
    RefreshMultihit()
    sprite('es431_18', 1)	# 122-122	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 123-123	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 124-124	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 125-125	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 126-126	 **attackbox here**
    RefreshMultihit()
    sprite('es431_18', 1)	# 127-127	 **attackbox here**
    Damage(4300)
    AttackP2(60)
    Unknown11092(0)
    Unknown11091(30)
    Unknown11057(1000)
    Unknown11069('')
    Unknown11064(0)
    RefreshMultihit()
    sprite('es431_18', 3)	# 128-130	 **attackbox here**
    Unknown2017(1)
    Unknown2015(-1)
    GFX_0('esef_431EffScrew', -1)
    GFX_0('esef_431EffScrewOD', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    Unknown23024(1)
    Unknown13024(1)
    sprite('es431_19', 2)	# 131-132	 **attackbox here**
    sprite('es431_20', 2)	# 133-134	 **attackbox here**
    sprite('es431_21', 2)	# 135-136	 **attackbox here**
    sprite('es431_22', 2)	# 137-138	 **attackbox here**
    sprite('es431_19', 2)	# 139-140	 **attackbox here**
    sprite('es431_20', 2)	# 141-142	 **attackbox here**
    sprite('es431_21', 2)	# 143-144	 **attackbox here**
    sprite('es431_22', 2)	# 145-146	 **attackbox here**
    sprite('es431_19', 2)	# 147-148	 **attackbox here**
    sprite('es431_20', 2)	# 149-150	 **attackbox here**
    sprite('es431_21', 2)	# 151-152	 **attackbox here**
    sprite('es431_22', 2)	# 153-154	 **attackbox here**
    sprite('es431_19', 3)	# 155-157	 **attackbox here**
    sprite('es431_20', 3)	# 158-160	 **attackbox here**
    sprite('es431_21', 3)	# 161-163	 **attackbox here**
    sprite('es431_22', 3)	# 164-166	 **attackbox here**
    sprite('es431_19', 4)	# 167-170	 **attackbox here**
    sprite('es431_20', 4)	# 171-174	 **attackbox here**
    sprite('es431_21', 4)	# 175-178	 **attackbox here**
    sprite('es431_22', 4)	# 179-182	 **attackbox here**
    sprite('es431_19', 4)	# 183-186	 **attackbox here**
    sprite('es431_20', 4)	# 187-190	 **attackbox here**
    sprite('es431_21', 4)	# 191-194	 **attackbox here**
    sprite('es431_22', 3)	# 195-197	 **attackbox here**
    sprite('es431_22', 1)	# 198-198	 **attackbox here**
    Unknown26('esef_431Camera')
    sprite('es431_23', 5)	# 199-203
    sprite('es431_24', 5)	# 204-208

@State
def UltimateShot_AirA():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
    sprite('es430_21', 2)	# 1-2
    GFX_0('esef_430EffAsiba', -1)
    setInvincible(1)
    Unknown1084(1)
    sprite('es430_01ex00', 4)	# 3-6
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'bes250_0', 'bes250_1', '', '')
    sprite('es430_02ex00', 4)	# 7-10
    sprite('es430_03ex00', 4)	# 11-14
    sprite('es430_04ex00', 4)	# 15-18
    GFX_0('esef_430EffStart', -1)
    Unknown36(1)
    Unknown1007(30000)
    Unknown35()
    sprite('es430_05ex00', 4)	# 19-22
    sprite('es430_06ex00', 4)	# 23-26
    sprite('es430_07ex00', 4)	# 27-30
    sprite('es430_08ex00', 4)	# 31-34
    sprite('es430_09ex00', 4)	# 35-38
    Unknown21015('657365665f3433304566665374617274000000000000000000000000000000007000000000000000')
    sprite('es430_10ex00', 4)	# 39-42
    sprite('es430_11ex00', 4)	# 43-46
    Unknown2015(150)
    teleportRelativeX(60000)
    sprite('es430_12ex00', 4)	# 47-50
    teleportRelativeX(30000)
    sprite('es430_13ex00', 4)	# 51-54
    teleportRelativeX(30000)
    sprite('es430_14ex00', 4)	# 55-58
    tag_voice(0, 'bes251_0', 'bes251_1', '', '')
    Unknown21015('657365665f3433304566665374617274000000000000000000000000000000007100000000000000')
    GFX_0('es430AirA', -1)
    clearUponHandler(2)
    sendToLabelUpon(2, 2)
    physicsXImpulse(20000)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown2015(-1)
    Unknown21015('657365665f3433304566664173696261000000000000000000000000000000007400000000000000')
    sprite('es430_15ex00', 4)	# 59-62
    sprite('es430_16ex00', 4)	# 63-66
    setInvincible(0)
    Unknown1019(60)
    sprite('es430_17ex00', 4)	# 67-70
    Unknown1019(80)
    sprite('es430_18ex00', 4)	# 71-74
    Unknown1019(80)
    sprite('es430_19ex00', 4)	# 75-78
    Unknown1019(80)
    sprite('es430_22', 4)	# 79-82
    sprite('es020_04', 4)	# 83-86
    sprite('es020_05', 4)	# 87-90
    sprite('es020_06', 4)	# 91-94
    label(1)
    sprite('es020_07', 4)	# 95-98
    sprite('es020_08', 4)	# 99-102
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es024_00', 3)	# 103-105
    Unknown1084(1)
    sprite('es024_01', 3)	# 106-108
    sprite('es024_02', 3)	# 109-111
    sprite('es024_03', 3)	# 112-114
    sprite('es024_04', 3)	# 115-117

@State
def UltimateShot_AirAOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
    sprite('es430_21', 2)	# 1-2
    GFX_0('esef_430EffAsiba', -1)
    setInvincible(1)
    Unknown1084(1)
    sprite('es430_01ex00', 4)	# 3-6
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'bes250_0', 'bes250_1', '', '')
    sprite('es430_02ex00', 4)	# 7-10
    sprite('es430_03ex00', 4)	# 11-14
    sprite('es430_04ex00', 4)	# 15-18
    GFX_0('esef_430EffStartOD', -1)
    Unknown36(1)
    Unknown1007(30000)
    Unknown35()
    sprite('es430_05ex00', 4)	# 19-22
    sprite('es430_06ex00', 4)	# 23-26
    sprite('es430_07ex00', 4)	# 27-30
    sprite('es430_08ex00', 4)	# 31-34
    sprite('es430_09ex00', 4)	# 35-38
    Unknown21015('657365665f34333045666653746172744f4400000000000000000000000000007200000000000000')
    sprite('es430_10ex00', 4)	# 39-42
    sprite('es430_11ex00', 4)	# 43-46
    Unknown2015(150)
    teleportRelativeX(60000)
    sprite('es430_12ex00', 4)	# 47-50
    teleportRelativeX(30000)
    sprite('es430_13ex00', 4)	# 51-54
    teleportRelativeX(30000)
    sprite('es430_14ex00', 4)	# 55-58
    tag_voice(0, 'bes251_0', 'bes251_1', '', '')
    Unknown21015('657365665f34333045666653746172744f4400000000000000000000000000007300000000000000')
    GFX_0('es430AirAOD', -1)
    clearUponHandler(2)
    sendToLabelUpon(2, 2)
    physicsXImpulse(20000)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown2015(-1)
    Unknown21015('657365665f3433304566664173696261000000000000000000000000000000007400000000000000')
    sprite('es430_15ex00', 4)	# 59-62
    sprite('es430_16ex00', 4)	# 63-66
    setInvincible(0)
    Unknown1019(60)
    sprite('es430_17ex00', 4)	# 67-70
    Unknown1019(80)
    sprite('es430_18ex00', 4)	# 71-74
    Unknown1019(80)
    sprite('es430_19ex00', 4)	# 75-78
    Unknown1019(80)
    sprite('es430_22', 4)	# 79-82
    sprite('es020_04', 4)	# 83-86
    sprite('es020_05', 4)	# 87-90
    sprite('es020_06', 4)	# 91-94
    label(1)
    sprite('es020_07', 4)	# 95-98
    sprite('es020_08', 4)	# 99-102
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('es024_00', 3)	# 103-105
    Unknown1084(1)
    sprite('es024_01', 3)	# 106-108
    sprite('es024_02', 3)	# 109-111
    sprite('es024_03', 3)	# 112-114
    sprite('es024_04', 3)	# 115-117

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11069('AstralHeat')
        AttackLevel_(5)
        Damage(0)
        Unknown11091(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11072(1, 250000, 10000)
        AirPushbackX(16000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(0)
        Unknown9154(1200)
        AirUntechableTime(1200)
        Unknown9016(1)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11078(1)
        Hitstop(0)
        Unknown11001(20, 10, 10)

        def upon_12():
            clearUponHandler(12)
            GFX_0('AstralHeat_Camera', -1)
            SLOT_66 = 1
            PushbackX(0)
            Unknown23088(1, 1)
            Unknown23157(1)
            Unknown11023(1)
            Unknown11067(1)
            Unknown2017(0)
            Unknown2053(0)
            Unknown2034(0)
            sendToLabel(1)
    sprite('es450_00', 3)	# 1-3
    setInvincible(1)
    Unknown1084(1)
    sprite('es450_01', 3)	# 4-6
    Unknown2036(55, -1, 2)
    Unknown23147()
    GFX_0('EMB_ES_AH', -1)
    tag_voice(1, 'bes290_0', 'bes290_1', '', '')
    sprite('es450_02', 4)	# 7-10
    sprite('es450_03', 4)	# 11-14
    sprite('es450_04', 4)	# 15-18
    sprite('es450_02', 4)	# 19-22
    sprite('es450_03', 4)	# 23-26
    sprite('es450_04', 4)	# 27-30
    sprite('es450_02', 4)	# 31-34
    sprite('es450_03', 4)	# 35-38
    sprite('es450_04', 4)	# 39-42
    sprite('es450_02', 4)	# 43-46
    sprite('es450_03', 4)	# 47-50
    sprite('es450_04', 4)	# 51-54
    GFX_0('esef_430EffSlash', -1)
    sprite('es450_05', 3)	# 55-57
    sprite('es450_06', 3)	# 58-60
    SFX_0('006_swing_blade_2')
    SFX_3('esse_00')
    SFX_3('esse_07')
    sprite('es450_07', 4)	# 61-64
    sprite('es450_08', 3)	# 65-67
    sprite('es450_09', 3)	# 68-70
    sprite('es450_10', 3)	# 71-73	 **attackbox here**
    sprite('es450_11', 4)	# 74-77
    setInvincible(0)
    sprite('es450_12', 4)	# 78-81
    sprite('es450_13', 4)	# 82-85
    sprite('es450_11', 4)	# 86-89
    sprite('es450_12', 4)	# 90-93
    sprite('es450_13', 4)	# 94-97
    sprite('es450_11', 4)	# 98-101
    sprite('es450_12', 4)	# 102-105
    sprite('es450_13', 4)	# 106-109
    sprite('es450_11', 4)	# 110-113
    sprite('es450_12', 4)	# 114-117
    sprite('es450_13', 4)	# 118-121
    sprite('es450_14', 4)	# 122-125
    sprite('es203_11ex00', 4)	# 126-129
    sprite('es203_12ex00', 4)	# 130-133
    sprite('es203_13ex00', 4)	# 134-137
    sprite('es203_14ex00', 4)	# 138-141
    ExitState()
    label(1)
    sprite('keep', 2)	# 142-143
    Unknown23084(1)
    Unknown2018(0, 70)
    sprite('es450_11', 4)	# 144-147
    sprite('es450_12', 4)	# 148-151
    sprite('es450_13', 4)	# 152-155
    GFX_0('esef_430EffBG', -1)
    GFX_0('esef_430EffBGAdd', -1)
    sprite('es450_11', 4)	# 156-159
    Unknown21015('41737472616c486561745f43616d6572610000000000000000000000000000008200000000000000')
    sprite('es450_12', 4)	# 160-163
    sprite('es450_13', 4)	# 164-167
    Unknown36(22)
    Unknown1084(1)
    physicsYImpulse(1)
    Unknown51(1)
    Unknown35()
    sprite('es450_11ex', 4)	# 168-171
    GFX_0('esef_450ChangeSordEff', 0)
    SFX_3('esse_00')
    SFX_3('esse_01')
    sprite('es450_12ex', 4)	# 172-175
    sprite('es450_13ex', 4)	# 176-179
    sprite('es450_11ex', 4)	# 180-183
    sprite('es450_12ex', 4)	# 184-187
    sprite('es450_13ex', 4)	# 188-191
    sprite('es450_11ex', 4)	# 192-195
    sprite('es450_12ex', 4)	# 196-199
    sprite('es450_13ex', 4)	# 200-203
    sprite('es450_11ex', 4)	# 204-207
    sprite('es450_12ex', 4)	# 208-211
    sprite('es450_13ex', 4)	# 212-215
    sprite('es450_11ex', 4)	# 216-219
    sprite('es450_12ex', 4)	# 220-223
    sprite('es450_13ex', 4)	# 224-227
    sprite('es450_11ex', 4)	# 228-231
    sprite('es450_12ex', 4)	# 232-235
    sprite('es450_13ex', 4)	# 236-239
    sprite('es450_15', 4)	# 240-243
    Unknown21015('41737472616c486561745f43616d6572610000000000000000000000000000008300000000000000')
    Unknown21015('657365665f3433304566664247000000000000000000000000000000000000008700000000000000')
    Unknown21015('657365665f3433304566664247416464000000000000000000000000000000008900000000000000')
    sprite('es450_16', 4)	# 244-247
    sprite('es450_17', 4)	# 248-251
    sprite('es450_18', 3)	# 252-254
    physicsXImpulse(35000)
    physicsYImpulse(40000)
    setGravity(1500)
    tag_voice(0, 'bes291_0', 'bes291_1', '', '')
    sprite('es450_19', 3)	# 255-257
    sprite('es450_20', 3)	# 258-260	 **attackbox here**
    SFX_3('esse_09')
    SFX_3('esse_03')
    SFX_0('000_airdash_0')
    GFX_0('esef_430EffAtkSlash', -1)
    Unknown36(1)
    Unknown1073(-35000)
    Unknown35()
    Damage(2000)
    Hitstop(12)
    Unknown11001(0, 0, 0)
    Unknown11072(0, 0, 0)
    Unknown11101(30)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(-3000)
    AirPushbackY(55000)
    Unknown9095()
    RefreshMultihit()
    sprite('es450_21', 5)	# 261-265
    Unknown2018(1, 70)
    Unknown1096(1040)
    sprite('es450_22', 4)	# 266-269
    Unknown1096(1080)
    sprite('es450_23', 4)	# 270-273
    Unknown1096(1120)
    sprite('es450_24', 4)	# 274-277
    Unknown1096(1160)
    GFX_0('esef_430EffAasiba', -1)
    Unknown36(1)
    Unknown1073(-35000)
    teleportRelativeX(200000)
    Unknown1007(120000)
    Unknown1099(-1)
    Unknown35()
    sprite('es450_25', 15)	# 278-292
    Unknown1096(1200)
    Unknown1084(1)
    sprite('es450_26', 3)	# 293-295
    physicsXImpulse(-50000)
    physicsYImpulse(32000)
    tag_voice(0, 'bes292_0', 'bes292_1', '', '')
    sprite('es450_27', 3)	# 296-298
    Unknown1096(1100)
    sprite('es450_28', 3)	# 299-301	 **attackbox here**
    Unknown1096(1000)
    SFX_3('esse_09')
    SFX_3('esse_03')
    SFX_0('000_airdash_0')
    GFX_0('esef_430EffAtkSlash', -1)
    Unknown36(1)
    Unknown1073(35000)
    Unknown35()
    Damage(4000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(46000)
    RefreshMultihit()
    sprite('es450_29', 5)	# 302-306
    Unknown2018(0, 70)
    Unknown1096(900)
    sprite('es450_30', 3)	# 307-309
    Unknown1096(880)
    sprite('es450_31', 3)	# 310-312
    Unknown1096(860)
    sprite('es450_32', 3)	# 313-315
    Unknown1096(840)
    sprite('es450_33', 3)	# 316-318
    Unknown1096(820)
    sprite('es450_34', 18)	# 319-336
    Unknown1096(800)
    GFX_0('esef_430EffAasiba', -1)
    Unknown36(1)
    Unknown1073(-45000)
    teleportRelativeX(-80000)
    Unknown1007(350000)
    Unknown35()
    Unknown1084(1)
    sprite('null', 18)	# 337-354
    Unknown1096(1000)
    Unknown3038(1)
    GFX_0('esef_430EffCutIn', -1)
    Unknown36(22)
    Unknown3038(1)
    physicsXImpulse(0)
    physicsYImpulse(1)
    setGravity(0)
    Unknown1000(-1380000)
    teleportRelativeY(1500000)
    Unknown2005()
    Unknown35()
    Unknown21015('657365665f3433304566664247000000000000000000000000000000000000008800000000000000')
    sprite('null', 40)	# 355-394
    tag_voice(0, 'bes293_0', 'bes293_1', '', '')
    sprite('null', 2)	# 395-396
    Unknown21015('41737472616c486561745f43616d6572610000000000000000000000000000008400000000000000')
    sprite('es450_35', 1)	# 397-397	 **attackbox here**
    Unknown36(22)
    Unknown3038(0)
    Unknown35()
    Unknown26('esef_430EffCutIn')
    GFX_0('esef_450SlashLast', -1)
    SFX_3('esse_09')
    SFX_3('esse_03')
    SFX_0('000_airdash_0')
    Damage(6000)
    Hitstop(3)
    Unknown11001(3, 3, 3)
    AirPushbackX(130000)
    AirPushbackY(-120000)
    YImpluseBeforeWallbounce(0)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    Unknown11056(2)
    RefreshMultihit()
    Unknown21015('41737472616c486561745f43616d6572610000000000000000000000000000008500000000000000')
    sprite('es450_35', 13)	# 398-410	 **attackbox here**
    sprite('es450_35', 6)	# 411-416	 **attackbox here**
    Unknown3038(0)
    Unknown1000(660000)
    teleportRelativeY(0)
    Unknown8001(2, 100)
    Unknown2018(1, 70)
    Unknown36(22)
    Unknown1019(5)
    YAccel(5)
    Unknown35()
    sprite('es450_36', 6)	# 417-422
    sprite('es450_37', 6)	# 423-428
    sprite('es450_38', 6)	# 429-434
    sprite('es450_39', 6)	# 435-440
    sprite('es450_39', 70)	# 441-510
    GFX_0('esef_450EffEmb', -1)
    Unknown23118(-1)
    Unknown36(22)
    Unknown23118(-1)
    Unknown51(1)
    Unknown1084(1)
    Unknown35()
    SFX_3('esse_10')
    sprite('es450_40', 4)	# 511-514
    Unknown26('esef_450EffEmb')
    Unknown23118(-16777216)
    Unknown36(22)
    Unknown23118(-16777216)
    Unknown35()
    Unknown4045('65736566665f3435305f666c6173683200000000000000000000000000000000ffffffff')
    GFX_0('esef_450EffWing', -1)
    GFX_0('esef_450EffWingAdd', -1)
    sprite('es450_35', 6)	# 515-520	 **attackbox here**
    sprite('es450_41', 6)	# 521-526	 **attackbox here**
    sprite('es450_42', 6)	# 527-532	 **attackbox here**
    sprite('es450_35', 6)	# 533-538	 **attackbox here**
    sprite('es450_41', 6)	# 539-544	 **attackbox here**
    sprite('es450_42', 6)	# 545-550	 **attackbox here**
    sprite('es450_35', 6)	# 551-556	 **attackbox here**
    sprite('es450_41', 6)	# 557-562	 **attackbox here**
    sprite('es450_42', 6)	# 563-568	 **attackbox here**
    sprite('es450_35', 6)	# 569-574	 **attackbox here**
    sprite('es450_41', 6)	# 575-580	 **attackbox here**
    sprite('es450_42', 6)	# 581-586	 **attackbox here**
    sprite('es450_35', 6)	# 587-592	 **attackbox here**
    sprite('es450_41', 6)	# 593-598	 **attackbox here**
    sprite('es450_42', 6)	# 599-604	 **attackbox here**
    sprite('es450_35', 6)	# 605-610	 **attackbox here**
    sprite('es450_41', 6)	# 611-616	 **attackbox here**
    sprite('es450_42', 6)	# 617-622	 **attackbox here**
    sprite('es450_35', 6)	# 623-628	 **attackbox here**
    sprite('es450_41', 6)	# 629-634	 **attackbox here**
    sprite('es450_42', 6)	# 635-640	 **attackbox here**
    sprite('es450_35', 5)	# 641-645	 **attackbox here**
    sprite('es450_41', 5)	# 646-650	 **attackbox here**
    sprite('es450_42', 5)	# 651-655	 **attackbox here**
    sprite('es450_35', 5)	# 656-660	 **attackbox here**
    sprite('es450_41', 5)	# 661-665	 **attackbox here**
    sprite('es450_42', 5)	# 666-670	 **attackbox here**
    Unknown21015('657365665f34353045666657696e6741646400000000000000000000000000008a00000000000000')
    Unknown36(22)
    Unknown23119(16777215, 60, 1)
    Unknown35()
    sprite('es450_35', 5)	# 671-675	 **attackbox here**
    sprite('es450_41', 5)	# 676-680	 **attackbox here**
    sprite('es450_42', 5)	# 681-685	 **attackbox here**
    sprite('es450_35', 5)	# 686-690	 **attackbox here**
    sprite('es450_41', 4)	# 691-694	 **attackbox here**
    sprite('es450_42', 4)	# 695-698	 **attackbox here**
    sprite('es450_35', 4)	# 699-702	 **attackbox here**
    sprite('es450_41', 4)	# 703-706	 **attackbox here**
    sprite('es450_42', 4)	# 707-710	 **attackbox here**
    sprite('es450_35', 4)	# 711-714	 **attackbox here**
    sprite('es450_41', 4)	# 715-718	 **attackbox here**
    GFX_1('eseff_450_flash2', -1)
    Unknown26('esef_450EffWing')
    Unknown26('esef_450EffWingAdd')
    GFX_0('esef_450EffBGClash', -1)
    GFX_0('esef_450EffClashA', -1)
    GFX_0('esef_450EffClashB', -1)
    GFX_0('esef_450EffClashC', -1)
    Unknown36(22)
    Unknown51(0)
    Unknown1000(-260000)
    Unknown3001(0)
    Unknown2047(0)
    Unknown2035(0)
    Unknown35()
    sprite('es450_42', 4)	# 719-722	 **attackbox here**
    sprite('es450_35', 4)	# 723-726	 **attackbox here**
    sprite('es450_41', 4)	# 727-730	 **attackbox here**
    sprite('es450_42', 4)	# 731-734	 **attackbox here**
    sprite('es450_35', 4)	# 735-738	 **attackbox here**
    sprite('es450_41', 4)	# 739-742	 **attackbox here**
    sprite('es450_42', 4)	# 743-746	 **attackbox here**
    Damage(30000)
    Unknown11064(3)
    AirPushbackX(0)
    AirPushbackY(-20000)
    YImpluseBeforeWallbounce(2000)
    Hitstop(0)
    Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
    RefreshMultihit()
    Unknown11072(1, 2500000, 0)
    sprite('es450_35', 4)	# 747-750	 **attackbox here**
    sprite('es450_41', 4)	# 751-754	 **attackbox here**
    sprite('es450_42', 4)	# 755-758	 **attackbox here**
    sprite('es450_35', 4)	# 759-762	 **attackbox here**
    sprite('es450_41', 4)	# 763-766	 **attackbox here**
    sprite('es450_42', 4)	# 767-770	 **attackbox here**
    sprite('es450_35', 4)	# 771-774	 **attackbox here**
    sprite('es450_41', 4)	# 775-778	 **attackbox here**
    sprite('es450_42', 4)	# 779-782	 **attackbox here**
    sprite('es450_35', 4)	# 783-786	 **attackbox here**
    sprite('es450_41', 3)	# 787-789	 **attackbox here**
    GFX_0('esef_450EffClashAmove', -1)
    sprite('es450_42', 3)	# 790-792	 **attackbox here**
    GFX_0('esef_450EffClashBmove', -1)
    sprite('es450_35', 3)	# 793-795	 **attackbox here**
    GFX_0('esef_450EffClashCmove', -1)
    sprite('es450_41', 3)	# 796-798	 **attackbox here**
    sprite('es450_42', 3)	# 799-801	 **attackbox here**
    sprite('es450_35', 3)	# 802-804	 **attackbox here**
    sprite('es450_41', 3)	# 805-807	 **attackbox here**
    sprite('es450_42', 3)	# 808-810	 **attackbox here**
    sprite('es450_35', 3)	# 811-813	 **attackbox here**
    sprite('es450_41', 3)	# 814-816	 **attackbox here**
    sprite('es450_42', 3)	# 817-819	 **attackbox here**
    sprite('es450_35', 3)	# 820-822	 **attackbox here**
    GFX_0('esef_450PaticleInf', -1)
    GFX_0('esef_450WhiteOut', -1)
    sprite('es450_41', 3)	# 823-825	 **attackbox here**
    sprite('es450_42', 3)	# 826-828	 **attackbox here**
    sprite('es450_35', 3)	# 829-831	 **attackbox here**
    sprite('es450_41', 3)	# 832-834	 **attackbox here**
    sprite('es450_42', 3)	# 835-837	 **attackbox here**
    sprite('es450_35', 3)	# 838-840	 **attackbox here**
    sprite('es450_41', 3)	# 841-843	 **attackbox here**
    sprite('es450_42', 3)	# 844-846	 **attackbox here**
    sprite('es450_35', 3)	# 847-849	 **attackbox here**
    sprite('es450_41', 3)	# 850-852	 **attackbox here**
    sprite('es450_42', 3)	# 853-855	 **attackbox here**
    sprite('es450_35', 3)	# 856-858	 **attackbox here**
    sprite('es450_41', 3)	# 859-861	 **attackbox here**
    Unknown20000(1)
    Unknown20001(1)
    sprite('es450_42', 3)	# 862-864	 **attackbox here**
    sprite('es450_35', 3)	# 865-867	 **attackbox here**
    sprite('es450_41', 3)	# 868-870	 **attackbox here**
    sprite('es450_42', 3)	# 871-873	 **attackbox here**
    sprite('es450_35', 3)	# 874-876	 **attackbox here**
    sprite('es450_41', 3)	# 877-879	 **attackbox here**
    sprite('es450_42', 3)	# 880-882	 **attackbox here**
    sprite('es450_35', 3)	# 883-885	 **attackbox here**
    sprite('es615_00ex', 7)	# 886-892
    Unknown21015('41737472616c486561745f43616d6572610000000000000000000000000000008600000000000000')
    Unknown1000(260000)
    Unknown26('esef_450EffBGClash')
    GFX_0('esef_450EffBGLast', -1)
    Unknown18010()
    sprite('es615_01ex', 7)	# 893-899
    sprite('es615_02ex', 7)	# 900-906
    sprite('es615_03ex', 7)	# 907-913
    GFX_0('esef_450SordLostMaso', -1)
    sprite('es615_04ex', 7)	# 914-920
    sprite('es615_05ex', 7)	# 921-927
    sprite('es615_06ex', 7)	# 928-934
    sprite('es615_07ex', 7)	# 935-941
    Unknown23018(1)
    tag_voice(0, 'bes294_0', 'bes294_1', '', '')
    label(2)
    sprite('es615_04ex', 7)	# 942-948
    sprite('es615_05ex', 7)	# 949-955
    sprite('es615_06ex', 7)	# 956-962
    sprite('es615_07ex', 7)	# 963-969
    gotoLabel(2)

@Subroutine
def MouthTableInit():
    Unknown18011('bes000', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14435, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 24885, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes503', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes504', 12643, 14177, 14179, 14177, 14179, 14177, 14435, 24882, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes520', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes521', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes522', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes525', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes403_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes403_1', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600bny', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes601bpt', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 12849, 14177, 14435, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes601brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 14137, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes601pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600uli', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes600uva', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes602uva', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes604uva', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes700bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes700bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 12641, 25394, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes700bpt', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes701brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 24882, 25399, 24887, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes700pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes700pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes700pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes701pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes701rrb', 12643, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes700uli', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes701uva', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bes701uvaB', 12643, 12641, 25392, 12337, 12641, 25392, 12337, 12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bny')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pna')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('uva')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(1)
    sprite('null', 30)	# 2-31
    Unknown13044(1)
    loopRest()
    if SLOT_17:
        _gotolabel(1)
    sprite('es600_00', 16)	# 32-47
    Unknown3038(1)
    teleportRelativeY(120000)
    GFX_0('suef_600_screen', -1)
    GFX_0('suef_600_light_core', 103)
    GFX_0('suef_600_light', 103)
    SFX_0('022_magiccircle_b')
    sprite('es600_00', 16)	# 48-63
    GFX_0('suef_600_es', -1)
    sprite('es600_00', 16)	# 64-79
    Unknown3038(0)
    GFX_0('esef_600light_end', 103)
    Unknown7006('bes500', 100, 896755042, 12592, 0, 0, 100, 896755042, 13360, 0, 0, 100, 896755042, 13616, 0, 0, 100)
    sprite('es600_01', 7)	# 80-86
    sprite('es600_02', 7)	# 87-93
    SFX_3('esse_01')
    sprite('es600_03', 7)	# 94-100
    sprite('es600_04', 7)	# 101-107
    sprite('es600_05', 7)	# 108-114
    sprite('es600_06', 7)	# 115-121
    sprite('es600_07', 7)	# 122-128
    sprite('es600_08', 7)	# 129-135
    GFX_0('esef_600_particle', -1)
    sprite('es600_09', 30)	# 136-165
    physicsYImpulse(-5000)
    setGravity(500)
    sendToLabelUpon(2, 2)
    label(2)
    sprite('es600_10', 6)	# 166-171
    clearUponHandler(2)
    Unknown1084(1)
    Unknown21007(24, 41)
    sprite('es024_01', 6)	# 172-177
    Unknown26('esef_600_particle')
    Unknown36(22)
    Unknown3026(-1)
    Unknown35()
    sprite('es024_02', 6)	# 178-183
    sprite('es024_03', 6)	# 184-189
    sprite('es024_04', 6)	# 190-195
    Unknown23018(1)
    label(3)
    sprite('es000_00', 7)	# 196-202
    sprite('es000_01', 7)	# 203-209
    sprite('es000_02', 7)	# 210-216
    sprite('es000_03', 7)	# 217-223
    sprite('es000_04', 7)	# 224-230
    sprite('es000_05', 7)	# 231-237
    sprite('es000_06', 7)	# 238-244
    sprite('es000_07', 7)	# 245-251
    sprite('es000_08', 7)	# 252-258
    sprite('es000_09', 7)	# 259-265
    sprite('es000_10', 7)	# 266-272
    loopRest()
    gotoLabel(3)
    ExitState()
    label(10)
    sprite('es601_00', 1)	# 273-273
    GFX_0('esef_601', -1)
    SFX_0('022_magiccircle_b')
    Unknown7006('bes502', 100, 896755042, 13104, 0, 0, 100, 896755042, 13360, 0, 0, 100, 896755042, 13616, 0, 0, 100)
    sprite('es601_00', 6)	# 274-279
    Unknown21012('657365665f3630315f73776f726400000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f73776f72645f616464000000000000000000000000000020000000')
    sendToLabelUpon(32, 12)
    label(11)
    sprite('es601_01', 7)	# 280-286
    sprite('es601_02', 7)	# 287-293
    sprite('es601_03', 7)	# 294-300
    sprite('es601_00', 7)	# 301-307
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('keep', 4)	# 308-311
    sprite('es601_04', 7)	# 312-318
    sprite('es601_05', 7)	# 319-325
    sprite('es601_06', 7)	# 326-332
    Unknown21007(24, 41)
    SFX_3('esse_00')
    sprite('es601_07', 7)	# 333-339
    sprite('es601_08', 7)	# 340-346
    sprite('es601_09', 7)	# 347-353
    Unknown26('esef_601_sword_particle')
    Unknown21012('657365665f3630315f626c6f6f6d00000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f737562000000000000000000000000000000000000000020000000')
    GFX_0('esef_601_zanzou', -1)
    sprite('es601_10', 7)	# 354-360
    sprite('es601_11', 7)	# 361-367
    sprite('es601_12', 7)	# 368-374
    sprite('es601_13', 7)	# 375-381
    Unknown23018(1)
    sprite('es601_14', 7)	# 382-388
    sprite('es601_15', 7)	# 389-395
    label(13)
    sprite('es000_00', 7)	# 396-402
    sprite('es000_01', 7)	# 403-409
    sprite('es000_02', 7)	# 410-416
    sprite('es000_03', 7)	# 417-423
    sprite('es000_04', 7)	# 424-430
    sprite('es000_05', 7)	# 431-437
    sprite('es000_06', 7)	# 438-444
    sprite('es000_07', 7)	# 445-451
    sprite('es000_08', 7)	# 452-458
    sprite('es000_09', 7)	# 459-465
    sprite('es000_10', 7)	# 466-472
    loopRest()
    gotoLabel(13)
    ExitState()
    label(20)
    sprite('es000_00', 1)	# 473-473
    SFX_1('bes700pla')
    label(21)
    sprite('es000_00', 7)	# 474-480
    sprite('es000_01', 7)	# 481-487
    sprite('es000_02', 7)	# 488-494
    sprite('es000_03', 7)	# 495-501
    sprite('es000_04', 7)	# 502-508
    sprite('es000_05', 7)	# 509-515
    sprite('es000_06', 7)	# 516-522
    sprite('es000_07', 7)	# 523-529
    sprite('es000_08', 7)	# 530-536
    sprite('es000_09', 7)	# 537-543
    sprite('es000_10', 7)	# 544-550
    gotoLabel(21)
    label(100)
    if (not SLOT_158):
        Unknown1000(-1230000)
    label(101)
    sprite('null', 30)	# 551-580
    Unknown13044(1)
    loopRest()
    if SLOT_17:
        _gotolabel(101)
    sprite('es600_00', 16)	# 581-596
    Unknown3038(1)
    teleportRelativeY(120000)
    GFX_0('suef_600_screen', -1)
    GFX_0('suef_600_light_core', 103)
    GFX_0('suef_600_light', 103)
    SFX_0('022_magiccircle_b')
    sprite('es600_00', 16)	# 597-612
    GFX_0('suef_600_es', -1)
    sprite('es600_00', 16)	# 613-628
    Unknown21007(24, 40)
    Unknown3038(0)
    GFX_0('esef_600light_end', 103)
    sprite('es600_01', 7)	# 629-635
    sprite('es600_02', 7)	# 636-642
    SFX_3('esse_01')
    sprite('es600_03', 7)	# 643-649
    sprite('es600_04', 7)	# 650-656
    sprite('es600_05', 7)	# 657-663
    sprite('es600_06', 7)	# 664-670
    sprite('es600_07', 7)	# 671-677
    sprite('es600_08', 7)	# 678-684
    GFX_0('esef_600_particle', -1)
    sprite('es600_09', 30)	# 685-714
    physicsYImpulse(-5000)
    setGravity(500)
    sendToLabelUpon(2, 102)
    label(102)
    sprite('es600_10', 6)	# 715-720
    clearUponHandler(2)
    Unknown1084(1)
    sprite('es024_01', 6)	# 721-726
    Unknown26('esef_600_particle')
    Unknown36(22)
    Unknown3026(-1)
    Unknown35()
    sprite('es024_02', 6)	# 727-732
    sprite('es024_03', 6)	# 733-738
    sprite('es024_04', 6)	# 739-744

    def upon_40():
        clearUponHandler(40)
        sendToLabel(104)
    label(103)
    sprite('es000_00', 7)	# 745-751
    sprite('es000_01', 7)	# 752-758
    sprite('es000_02', 7)	# 759-765
    sprite('es000_03', 7)	# 766-772
    sprite('es000_04', 7)	# 773-779
    sprite('es000_05', 7)	# 780-786
    sprite('es000_06', 7)	# 787-793
    sprite('es000_07', 7)	# 794-800
    sprite('es000_08', 7)	# 801-807
    sprite('es000_09', 7)	# 808-814
    sprite('es000_10', 7)	# 815-821
    gotoLabel(103)
    label(104)
    sprite('es003_00', 6)	# 822-827
    Unknown2005()
    sprite('es003_01', 4)	# 828-831
    sprite('es003_01ex00', 4)	# 832-835
    sprite('es003_00ex00', 5)	# 836-840
    sprite('es300_00', 8)	# 841-848
    SFX_1('bes601brc')
    sprite('es300_01', 8)	# 849-856
    sprite('es300_02', 8)	# 857-864
    sprite('es300_03', 6)	# 865-870
    sprite('es300_04', 8)	# 871-878
    sprite('es300_05', 8)	# 879-886
    sprite('es300_06', 8)	# 887-894
    label(105)
    sprite('es300_08', 1)	# 895-895
    if SLOT_97:
        _gotolabel(105)
    sprite('es300_08', 32767)	# 896-33662
    Unknown21011(60)
    ExitState()
    label(110)
    sprite('es601_00', 1)	# 33663-33663
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1515000)
    GFX_0('esef_601', -1)
    SFX_0('022_magiccircle_b')
    SFX_1('bes600bha')
    sprite('es601_00', 6)	# 33664-33669
    Unknown21012('657365665f3630315f73776f726400000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f73776f72645f616464000000000000000000000000000020000000')
    sendToLabelUpon(32, 112)
    label(111)
    sprite('es601_01', 7)	# 33670-33676
    sprite('es601_02', 7)	# 33677-33683
    sprite('es601_03', 7)	# 33684-33690
    sprite('es601_00', 7)	# 33691-33697
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('keep', 4)	# 33698-33701
    sprite('es601_04', 7)	# 33702-33708
    SFX_1('es417')
    sprite('es601_05', 7)	# 33709-33715
    sprite('es601_06', 7)	# 33716-33722
    SFX_3('esse_00')
    sprite('es601_07', 7)	# 33723-33729
    sprite('es601_08', 7)	# 33730-33736
    sprite('es601_09', 7)	# 33737-33743
    Unknown26('esef_601_sword_particle')
    Unknown21012('657365665f3630315f626c6f6f6d00000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f737562000000000000000000000000000000000000000020000000')
    GFX_0('esef_601_zanzou', -1)
    sprite('es601_10', 7)	# 33744-33750
    sprite('es601_11', 7)	# 33751-33757
    sprite('es601_12', 7)	# 33758-33764
    sprite('es601_13', 7)	# 33765-33771
    sprite('es601_14', 7)	# 33772-33778
    sprite('es601_15', 7)	# 33779-33785
    Unknown21011(360)
    label(113)
    sprite('es000_00', 7)	# 33786-33792
    sprite('es000_01', 7)	# 33793-33799
    sprite('es000_02', 7)	# 33800-33806
    sprite('es000_03', 7)	# 33807-33813
    sprite('es000_04', 7)	# 33814-33820
    sprite('es000_05', 7)	# 33821-33827
    sprite('es000_06', 7)	# 33828-33834
    sprite('es000_07', 7)	# 33835-33841
    sprite('es000_08', 7)	# 33842-33848
    sprite('es000_09', 7)	# 33849-33855
    Unknown21007(24, 40)
    sprite('es000_10', 7)	# 33856-33862
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('es000_00', 1)	# 33863-33863
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown2037(2)
    SFX_1('bes600bny')
    label(121)
    sprite('es000_00', 7)	# 33864-33870
    sprite('es000_01', 7)	# 33871-33877
    sprite('es000_02', 7)	# 33878-33884
    sprite('es000_03', 7)	# 33885-33891
    sprite('es000_04', 7)	# 33892-33898
    sprite('es000_05', 7)	# 33899-33905
    sprite('es000_06', 7)	# 33906-33912
    sprite('es000_07', 7)	# 33913-33919
    sprite('es000_08', 7)	# 33920-33926
    sprite('es000_09', 7)	# 33927-33933
    sprite('es000_10', 7)	# 33934-33940
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(121)
    label(122)
    sprite('es408_00', 7)	# 33941-33947
    SFX_3('esse_05')
    sprite('es408_01', 7)	# 33948-33954

    def upon_40():
        clearUponHandler(40)
        sendToLabel(124)
    Unknown2037(3)
    label(123)
    sprite('es408_02', 7)	# 33955-33961
    sprite('es408_03', 7)	# 33962-33968
    sprite('es408_04', 7)	# 33969-33975
    sprite('es408_05', 7)	# 33976-33982
    sprite('es408_06', 7)	# 33983-33989
    if (not SLOT_2):
        Unknown21007(24, 40)
    Unknown2038(-1)
    gotoLabel(123)
    label(124)
    sprite('es408_07', 7)	# 33990-33996
    sprite('es408_08', 7)	# 33997-34003
    Unknown21011(120)
    label(125)
    sprite('es000_00', 7)	# 34004-34010
    sprite('es000_01', 7)	# 34011-34017
    sprite('es000_02', 7)	# 34018-34024
    sprite('es000_03', 7)	# 34025-34031
    sprite('es000_04', 7)	# 34032-34038
    sprite('es000_05', 7)	# 34039-34045
    sprite('es000_06', 7)	# 34046-34052
    sprite('es000_07', 7)	# 34053-34059
    sprite('es000_08', 7)	# 34060-34066
    sprite('es000_09', 7)	# 34067-34073
    sprite('es000_10', 7)	# 34074-34080
    gotoLabel(125)
    ExitState()
    label(130)
    sprite('es000_00', 1)	# 34081-34081
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('es000_00', 7)	# 34082-34088
    sprite('es000_01', 7)	# 34089-34095
    sprite('es000_02', 7)	# 34096-34102
    sprite('es000_03', 7)	# 34103-34109
    sprite('es000_04', 7)	# 34110-34116
    sprite('es000_05', 7)	# 34117-34123
    sprite('es000_06', 7)	# 34124-34130
    sprite('es000_07', 7)	# 34131-34137
    sprite('es000_08', 7)	# 34138-34144
    sprite('es000_09', 7)	# 34145-34151
    sprite('es000_10', 7)	# 34152-34158
    gotoLabel(131)
    label(132)
    sprite('es300_00', 8)	# 34159-34166
    SFX_1('bes601bpt')
    sprite('es300_01', 8)	# 34167-34174
    sprite('es300_02', 8)	# 34175-34182
    sprite('es300_03', 6)	# 34183-34188
    sprite('es300_04', 8)	# 34189-34196
    sprite('es300_05', 8)	# 34197-34204
    sprite('es300_06', 8)	# 34205-34212
    label(133)
    sprite('es300_08', 1)	# 34213-34213
    if SLOT_97:
        _gotolabel(133)
    sprite('es300_08', 32767)	# 34214-66980
    Unknown23018(1)
    ExitState()
    label(140)
    sprite('es600_00', 16)	# 66981-66996
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(1)
    teleportRelativeY(120000)
    GFX_0('suef_600_screen', -1)
    GFX_0('suef_600_light_core', 103)
    GFX_0('suef_600_light', 103)
    SFX_0('022_magiccircle_b')
    sprite('es600_00', 16)	# 66997-67012
    GFX_0('suef_600_es', -1)
    sprite('es600_00', 16)	# 67013-67028
    Unknown3038(0)
    GFX_0('esef_600light_end', 103)
    SFX_1('bes600pbc')
    sprite('es600_01', 7)	# 67029-67035
    sprite('es600_02', 7)	# 67036-67042
    SFX_3('esse_01')
    sprite('es600_03', 7)	# 67043-67049
    sprite('es600_04', 7)	# 67050-67056
    sprite('es600_05', 7)	# 67057-67063
    sprite('es600_06', 7)	# 67064-67070
    sprite('es600_07', 7)	# 67071-67077
    sprite('es600_08', 7)	# 67078-67084
    GFX_0('esef_600_particle', -1)
    sprite('es600_09', 30)	# 67085-67114
    physicsYImpulse(-5000)
    setGravity(500)
    sendToLabelUpon(2, 141)
    label(141)
    sprite('es600_10', 6)	# 67115-67120
    clearUponHandler(2)
    Unknown1084(1)
    sprite('es024_01', 6)	# 67121-67126
    Unknown26('esef_600_particle')
    Unknown36(22)
    Unknown3026(-1)
    Unknown35()
    sprite('es024_02', 6)	# 67127-67132
    sprite('es024_03', 6)	# 67133-67138
    sprite('es024_04', 6)	# 67139-67144
    label(142)
    sprite('es000_00', 7)	# 67145-67151
    sprite('es000_01', 7)	# 67152-67158
    sprite('es000_02', 7)	# 67159-67165
    sprite('es000_03', 7)	# 67166-67172
    sprite('es000_04', 7)	# 67173-67179
    sprite('es000_05', 7)	# 67180-67186
    sprite('es000_06', 7)	# 67187-67193
    sprite('es000_07', 7)	# 67194-67200
    sprite('es000_08', 7)	# 67201-67207
    sprite('es000_09', 7)	# 67208-67214
    sprite('es000_10', 7)	# 67215-67221
    if SLOT_97:
        _gotolabel(142)
    sprite('es000_00', 1)	# 67222-67222
    Unknown21007(24, 40)
    Unknown21011(60)
    label(143)
    sprite('es000_00', 7)	# 67223-67229
    sprite('es000_01', 7)	# 67230-67236
    sprite('es000_02', 7)	# 67237-67243
    sprite('es000_03', 7)	# 67244-67250
    sprite('es000_04', 7)	# 67251-67257
    sprite('es000_05', 7)	# 67258-67264
    sprite('es000_06', 7)	# 67265-67271
    sprite('es000_07', 7)	# 67272-67278
    sprite('es000_08', 7)	# 67279-67285
    sprite('es000_09', 7)	# 67286-67292
    sprite('es000_10', 7)	# 67293-67299
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('es000_00', 7)	# 67300-67306
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('es000_01', 7)	# 67307-67313
    sprite('es000_02', 7)	# 67314-67320
    sprite('es000_03', 7)	# 67321-67327
    sprite('es000_04', 7)	# 67328-67334
    sprite('es000_05', 7)	# 67335-67341
    sprite('es000_06', 7)	# 67342-67348
    sprite('es000_07', 7)	# 67349-67355
    sprite('es000_08', 7)	# 67356-67362
    sprite('es000_09', 7)	# 67363-67369
    sprite('es000_10', 7)	# 67370-67376
    sprite('es300_00', 8)	# 67377-67384
    SFX_1('bes600pyo')
    sprite('es300_01', 8)	# 67385-67392
    sprite('es300_02', 8)	# 67393-67400
    sprite('es300_03', 6)	# 67401-67406
    sprite('es300_04', 8)	# 67407-67414
    sprite('es300_05', 8)	# 67415-67422
    sprite('es300_06', 8)	# 67423-67430
    label(151)
    sprite('es300_08', 1)	# 67431-67431
    if SLOT_97:
        _gotolabel(151)
    sprite('es300_08', 30)	# 67432-67461
    sprite('es300_07', 6)	# 67462-67467
    Unknown21007(24, 40)
    Unknown21011(120)
    label(152)
    sprite('es000_00', 7)	# 67468-67474
    sprite('es000_01', 7)	# 67475-67481
    sprite('es000_02', 7)	# 67482-67488
    sprite('es000_03', 7)	# 67489-67495
    sprite('es000_04', 7)	# 67496-67502
    sprite('es000_05', 7)	# 67503-67509
    sprite('es000_06', 7)	# 67510-67516
    sprite('es000_07', 7)	# 67517-67523
    sprite('es000_08', 7)	# 67524-67530
    sprite('es000_09', 7)	# 67531-67537
    sprite('es000_10', 7)	# 67538-67544
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('es000_00', 7)	# 67545-67551
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('es000_01', 7)	# 67552-67558
    sprite('es000_02', 7)	# 67559-67565
    sprite('es000_03', 7)	# 67566-67572
    sprite('es000_04', 7)	# 67573-67579
    sprite('es000_05', 7)	# 67580-67586
    sprite('es000_06', 7)	# 67587-67593
    sprite('es000_07', 7)	# 67594-67600
    sprite('es000_08', 7)	# 67601-67607
    sprite('es000_09', 7)	# 67608-67614
    sprite('es000_10', 7)	# 67615-67621
    sprite('es001_00', 6)	# 67622-67627
    sprite('es001_01', 6)	# 67628-67633
    sprite('es001_02', 6)	# 67634-67639
    sprite('es001_03', 6)	# 67640-67645
    GFX_0('esef_001', 0)
    Unknown36(1)
    Unknown1072(65000)
    Unknown35()
    SFX_3('esse_08')
    GFX_0('esef_001_tame_add', 0)
    GFX_0('esef_001_tame_add', 1)
    GFX_0('esef_001_tame_add', 2)
    SFX_1('bes600uli')
    sprite('es001_04', 6)	# 67646-67651
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 67652-67657
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 67658-67663
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 67664-67669
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 67670-67675
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 67676-67681
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 67682-67687
    SFX_3('esse_08')
    sprite('es001_03', 6)	# 67688-67693
    SFX_3('esse_08')
    sprite('es001_04', 6)	# 67694-67699
    SFX_3('esse_08')
    sprite('es001_05', 6)	# 67700-67705
    SFX_3('esse_08')
    sprite('es001_06', 6)	# 67706-67711
    SFX_3('esse_08')
    label(161)
    sprite('es001_03', 6)	# 67712-67717
    sprite('es001_04', 6)	# 67718-67723
    sprite('es001_05', 6)	# 67724-67729
    sprite('es001_06', 6)	# 67730-67735
    if SLOT_97:
        _gotolabel(161)
    sprite('es001_02', 6)	# 67736-67741
    sprite('es001_01', 6)	# 67742-67747
    sprite('es001_00', 6)	# 67748-67753
    Unknown21007(24, 40)
    Unknown21011(120)
    label(162)
    sprite('es000_00', 7)	# 67754-67760
    sprite('es000_01', 7)	# 67761-67767
    sprite('es000_02', 7)	# 67768-67774
    sprite('es000_03', 7)	# 67775-67781
    sprite('es000_04', 7)	# 67782-67788
    sprite('es000_05', 7)	# 67789-67795
    sprite('es000_06', 7)	# 67796-67802
    sprite('es000_07', 7)	# 67803-67809
    sprite('es000_08', 7)	# 67810-67816
    sprite('es000_09', 7)	# 67817-67823
    sprite('es000_10', 7)	# 67824-67830
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('es000_00', 7)	# 67831-67837
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)
    sprite('es000_01', 7)	# 67838-67844
    sprite('es000_02', 7)	# 67845-67851
    sprite('es000_03', 7)	# 67852-67858
    sprite('es000_04', 7)	# 67859-67865
    sprite('es000_05', 7)	# 67866-67872
    sprite('es000_06', 7)	# 67873-67879
    sprite('es000_07', 7)	# 67880-67886
    sprite('es000_08', 7)	# 67887-67893
    sprite('es000_09', 7)	# 67894-67900
    sprite('es000_10', 7)	# 67901-67907
    sprite('es300_00', 8)	# 67908-67915
    SFX_1('bes600rrb')
    sprite('es300_01', 8)	# 67916-67923
    sprite('es300_02', 8)	# 67924-67931
    sprite('es300_03', 6)	# 67932-67937
    sprite('es300_04', 8)	# 67938-67945
    sprite('es300_05', 8)	# 67946-67953
    sprite('es300_06', 8)	# 67954-67961
    label(171)
    sprite('es300_08', 1)	# 67962-67962
    if SLOT_97:
        _gotolabel(171)
    sprite('es300_08', 30)	# 67963-67992
    sprite('es300_07', 6)	# 67993-67998
    Unknown21007(24, 40)
    Unknown21011(120)
    label(172)
    sprite('es000_00', 7)	# 67999-68005
    sprite('es000_01', 7)	# 68006-68012
    sprite('es000_02', 7)	# 68013-68019
    sprite('es000_03', 7)	# 68020-68026
    sprite('es000_04', 7)	# 68027-68033
    sprite('es000_05', 7)	# 68034-68040
    sprite('es000_06', 7)	# 68041-68047
    sprite('es000_07', 7)	# 68048-68054
    sprite('es000_08', 7)	# 68055-68061
    sprite('es000_09', 7)	# 68062-68068
    sprite('es000_10', 7)	# 68069-68075
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('es601_00', 1)	# 68076-68076
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1515000)
    GFX_0('esef_601', -1)
    SFX_0('022_magiccircle_b')
    SFX_1('es416')
    sprite('es601_00', 6)	# 68077-68082
    Unknown21012('657365665f3630315f73776f726400000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f73776f72645f616464000000000000000000000000000020000000')
    sendToLabelUpon(32, 182)
    label(181)
    sprite('es601_01', 7)	# 68083-68089
    sprite('es601_02', 7)	# 68090-68096
    sprite('es601_03', 7)	# 68097-68103
    sprite('es601_00', 7)	# 68104-68110
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('keep', 4)	# 68111-68114
    sprite('es601_04', 7)	# 68115-68121
    SFX_1('bes600pna')
    sprite('es601_05', 7)	# 68122-68128
    sprite('es601_06', 7)	# 68129-68135
    SFX_3('esse_00')
    sprite('es601_07', 7)	# 68136-68142
    sprite('es601_08', 7)	# 68143-68149
    sprite('es601_09', 7)	# 68150-68156
    Unknown26('esef_601_sword_particle')
    Unknown21012('657365665f3630315f626c6f6f6d00000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f737562000000000000000000000000000000000000000020000000')
    GFX_0('esef_601_zanzou', -1)
    sprite('es601_10', 7)	# 68157-68163
    sprite('es601_11', 7)	# 68164-68170
    sprite('es601_12', 7)	# 68171-68177
    sprite('es601_13', 7)	# 68178-68184
    sprite('es601_14', 7)	# 68185-68191
    sprite('es601_15', 7)	# 68192-68198
    label(183)
    sprite('es000_00', 7)	# 68199-68205
    sprite('es000_01', 7)	# 68206-68212
    sprite('es000_02', 7)	# 68213-68219
    sprite('es000_03', 7)	# 68220-68226
    sprite('es000_04', 7)	# 68227-68233
    sprite('es000_05', 7)	# 68234-68240
    sprite('es000_06', 7)	# 68241-68247
    sprite('es000_07', 7)	# 68248-68254
    sprite('es000_08', 7)	# 68255-68261
    sprite('es000_09', 7)	# 68262-68268
    sprite('es000_10', 7)	# 68269-68275
    if SLOT_97:
        _gotolabel(183)
    sprite('es000_00', 1)	# 68276-68276
    Unknown21007(24, 40)
    Unknown21011(240)
    label(184)
    sprite('es000_00', 7)	# 68277-68283
    sprite('es000_01', 7)	# 68284-68290
    sprite('es000_02', 7)	# 68291-68297
    sprite('es000_03', 7)	# 68298-68304
    sprite('es000_04', 7)	# 68305-68311
    sprite('es000_05', 7)	# 68312-68318
    sprite('es000_06', 7)	# 68319-68325
    sprite('es000_07', 7)	# 68326-68332
    sprite('es000_08', 7)	# 68333-68339
    sprite('es000_09', 7)	# 68340-68346
    sprite('es000_10', 7)	# 68347-68353
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('es601_00', 6)	# 68354-68359
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(194)
        SFX_1('bes602uva')

    def upon_39():
        clearUponHandler(39)
        sendToLabel(196)
    GFX_0('esef_601', -1)
    SFX_0('022_magiccircle_b')
    sprite('es601_00', 6)	# 68360-68365
    Unknown21012('657365665f3630315f73776f726400000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f73776f72645f616464000000000000000000000000000020000000')
    sendToLabelUpon(32, 192)
    SFX_1('bes600uva')
    label(191)
    sprite('es601_01', 7)	# 68366-68372
    sprite('es601_02', 7)	# 68373-68379
    sprite('es601_03', 7)	# 68380-68386
    sprite('es601_00', 7)	# 68387-68393
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('keep', 4)	# 68394-68397
    sprite('es601_04', 7)	# 68398-68404
    sprite('es601_05', 7)	# 68405-68411
    sprite('es601_06', 7)	# 68412-68418
    SFX_3('esse_00')
    sprite('es601_07', 7)	# 68419-68425
    sprite('es601_08', 7)	# 68426-68432
    sprite('es601_09', 7)	# 68433-68439
    Unknown26('esef_601_sword_particle')
    Unknown21012('657365665f3630315f626c6f6f6d00000000000000000000000000000000000020000000')
    Unknown21012('657365665f3630315f737562000000000000000000000000000000000000000020000000')
    GFX_0('esef_601_zanzou', -1)
    sprite('es601_10', 7)	# 68440-68446
    sprite('es601_11', 7)	# 68447-68453
    sprite('es601_12', 7)	# 68454-68460
    sprite('es601_13', 7)	# 68461-68467
    sprite('es601_14', 7)	# 68468-68474
    sprite('es601_15', 7)	# 68475-68481
    Unknown21007(24, 40)
    label(193)
    sprite('es000_00', 7)	# 68482-68488
    sprite('es000_01', 7)	# 68489-68495
    sprite('es000_02', 7)	# 68496-68502
    sprite('es000_03', 7)	# 68503-68509
    sprite('es000_04', 7)	# 68510-68516
    sprite('es000_05', 7)	# 68517-68523
    sprite('es000_06', 7)	# 68524-68530
    sprite('es000_07', 7)	# 68531-68537
    sprite('es000_08', 7)	# 68538-68544
    sprite('es000_09', 7)	# 68545-68551
    sprite('es000_10', 7)	# 68552-68558
    gotoLabel(193)
    label(194)
    sprite('es408_00', 7)	# 68559-68565
    sprite('es408_01', 7)	# 68566-68572
    sprite('es408_02', 7)	# 68573-68579
    sprite('es408_03', 7)	# 68580-68586
    sprite('es408_04', 7)	# 68587-68593
    sprite('es408_05', 7)	# 68594-68600
    sprite('es408_06', 7)	# 68601-68607
    sprite('es408_02', 1)	# 68608-68608
    Unknown21007(24, 39)
    label(195)
    sprite('es408_02', 7)	# 68609-68615
    sprite('es408_03', 7)	# 68616-68622
    sprite('es408_04', 7)	# 68623-68629
    sprite('es408_05', 7)	# 68630-68636
    sprite('es408_06', 7)	# 68637-68643
    gotoLabel(195)
    label(196)
    sprite('es408_02', 7)	# 68644-68650
    GFX_0('esef_408Eff', -1)
    SFX_1('bes604uva')
    sprite('es408_03', 7)	# 68651-68657
    SFX_3('esse_05')
    SFX_3('esse_05')
    sprite('es408_04', 7)	# 68658-68664
    sprite('es408_02', 7)	# 68665-68671
    sprite('es408_03', 7)	# 68672-68678
    sprite('es408_04', 7)	# 68679-68685
    sprite('es408_05', 7)	# 68686-68692
    sprite('es408_06', 7)	# 68693-68699
    sprite('es408_07', 7)	# 68700-68706
    sprite('es408_08', 7)	# 68707-68713
    Unknown23018(1)
    label(197)
    sprite('es000_00', 7)	# 68714-68720
    sprite('es000_01', 7)	# 68721-68727
    sprite('es000_02', 7)	# 68728-68734
    sprite('es000_03', 7)	# 68735-68741
    sprite('es000_04', 7)	# 68742-68748
    sprite('es000_05', 7)	# 68749-68755
    sprite('es000_06', 7)	# 68756-68762
    sprite('es000_07', 7)	# 68763-68769
    sprite('es000_08', 7)	# 68770-68776
    sprite('es000_09', 7)	# 68777-68783
    sprite('es000_10', 7)	# 68784-68790
    gotoLabel(197)
    ExitState()
    label(200)
    sprite('es000_00', 1)	# 68791-68791
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        SLOT_51 = 1

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('es000_00', 7)	# 68792-68798
    sprite('es000_01', 7)	# 68799-68805
    sprite('es000_02', 7)	# 68806-68812
    sprite('es000_03', 7)	# 68813-68819
    sprite('es000_04', 7)	# 68820-68826
    sprite('es000_05', 7)	# 68827-68833
    sprite('es000_06', 7)	# 68834-68840
    sprite('es000_07', 7)	# 68841-68847
    sprite('es000_08', 7)	# 68848-68854
    sprite('es000_09', 7)	# 68855-68861
    sprite('es000_10', 7)	# 68862-68868
    gotoLabel(201)
    label(202)
    sprite('es000_00', 1)	# 68869-68869
    if SLOT_51:
        sendToLabel(203)
    sprite('es003_00', 6)	# 68870-68875
    Unknown2005()
    sprite('es003_01', 4)	# 68876-68879
    sprite('es003_01ex00', 4)	# 68880-68883
    sprite('es003_00ex00', 5)	# 68884-68888
    label(203)
    sprite('es300_00', 8)	# 68889-68896
    SFX_1('bes601pla')
    sprite('es300_01', 8)	# 68897-68904
    sprite('es300_02', 8)	# 68905-68912
    sprite('es300_03', 6)	# 68913-68918
    sprite('es300_04', 8)	# 68919-68926
    sprite('es300_05', 8)	# 68927-68934
    sprite('es300_06', 8)	# 68935-68942
    label(204)
    sprite('es300_08', 1)	# 68943-68943
    if SLOT_97:
        _gotolabel(204)
    sprite('es300_08', 20)	# 68944-68963
    sprite('es300_07', 6)	# 68964-68969
    Unknown21007(24, 40)
    Unknown21011(360)
    label(205)
    sprite('es000_00', 7)	# 68970-68976
    sprite('es000_01', 7)	# 68977-68983
    sprite('es000_02', 7)	# 68984-68990
    sprite('es000_03', 7)	# 68991-68997
    sprite('es000_04', 7)	# 68998-69004
    sprite('es000_05', 7)	# 69005-69011
    sprite('es000_06', 7)	# 69012-69018
    sprite('es000_07', 7)	# 69019-69025
    sprite('es000_08', 7)	# 69026-69032
    sprite('es000_09', 7)	# 69033-69039
    sprite('es000_10', 7)	# 69040-69046
    gotoLabel(205)
    ExitState()
    label(991)
    sprite('es000_00', 1)	# 69047-69047
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('es000_00', 7)	# 69048-69054
    sprite('es000_01', 7)	# 69055-69061
    sprite('es000_02', 7)	# 69062-69068
    sprite('es000_03', 7)	# 69069-69075
    sprite('es000_04', 7)	# 69076-69082
    sprite('es000_05', 7)	# 69083-69089
    sprite('es000_06', 7)	# 69090-69096
    sprite('es000_07', 7)	# 69097-69103
    sprite('es000_08', 7)	# 69104-69110
    sprite('es000_09', 7)	# 69111-69117
    sprite('es000_10', 7)	# 69118-69124
    gotoLabel(992)
    label(993)
    sprite('es033_00', 3)	# 69125-69127

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
    sprite('es033_01', 3)	# 69128-69130
    sprite('es033_02', 3)	# 69131-69133
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 69134-69136
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
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bny'):
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
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    if Unknown42('brg'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bjn'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bno'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('brc'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('btg'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bha'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bny'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bhz'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bmk'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bpt'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('biz'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('baz'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bph'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bes'):
        if random_(2, 0, 50):
            sendToLabel(10)
    if Unknown42('bjb'):
        if random_(2, 0, 50):
            sendToLabel(10)
    sprite('es300_00', 8)	# 4-11
    if SLOT_158:
        Unknown20000(1)
    sprite('es300_01', 8)	# 12-19
    sprite('es300_02', 8)	# 20-27
    sprite('es300_03', 6)	# 28-33
    sprite('es300_04', 8)	# 34-41
    sprite('es300_05', 8)	# 42-49
    if SLOT_158:
        if SLOT_52:
            SFX_1('bes524')
        elif SLOT_108:
            Unknown7006('bes402_0', 100, 879977826, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bes520', 100, 896755042, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('es300_06', 8)	# 50-57
    sprite('es300_08', 80)	# 58-137
    sprite('es300_07', 6)	# 138-143
    sprite('es611_00', 7)	# 144-150
    teleportRelativeY(0)
    Unknown3026(-1)
    SFX_0('019_cloth_c')
    sprite('es611_01', 7)	# 151-157
    SFX_0('019_cloth_b')
    sprite('es611_02', 7)	# 158-164
    GFX_0('esef_611', -1)
    SFX_3('esse_10')
    sprite('es611_03', 7)	# 165-171
    physicsYImpulse(3000)
    sprite('es611_04', 7)	# 172-178
    sprite('es611_05', 7)	# 179-185
    physicsYImpulse(2000)
    sprite('es611_06', 7)	# 186-192
    physicsYImpulse(1000)
    sprite('es611_07', 7)	# 193-199
    GFX_0('esef_611_es_add', -1)
    sprite('es611_08', 7)	# 200-206
    physicsYImpulse(500)
    sprite('es611_09', 7)	# 207-213
    Unknown23119(16777215, 14, 1)
    sprite('es611_10', 7)	# 214-220
    sprite('es611_11', 7)	# 221-227
    Unknown23118(-1)
    Unknown3004(-11)
    sprite('es611_11', 15)	# 228-242
    physicsYImpulse(0)
    sprite('null', 32767)	# 243-33009
    loopRest()
    label(10)
    sprite('es610_00', 9)	# 33010-33018
    sprite('es610_01', 9)	# 33019-33027
    sprite('es610_02', 9)	# 33028-33036
    sprite('es610_03', 9)	# 33037-33045
    if Unknown42('brg'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bjn'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bno'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('brc'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('btg'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bha'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bny'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bhz'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bmk'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bpt'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('biz'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('baz'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bph'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bes'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if Unknown42('bjb'):
        GFX_0('esef_610_emblem', 0)
        SFX_0('022_magiccircle_b')
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bes524', 100, 896755042, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bes402_0', 100, 879977826, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bes522', 100, 896755042, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(11)
    sprite('es610_04', 8)	# 33046-33053
    sprite('es610_05', 8)	# 33054-33061
    sprite('es610_06', 8)	# 33062-33069
    sprite('es610_07', 8)	# 33070-33077
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('es000_00', 1)	# 33078-33078

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('es000_00', 7)	# 33079-33085
    sprite('es000_01', 7)	# 33086-33092
    sprite('es000_02', 7)	# 33093-33099
    sprite('es000_03', 7)	# 33100-33106
    sprite('es000_04', 7)	# 33107-33113
    sprite('es000_05', 7)	# 33114-33120
    sprite('es000_06', 7)	# 33121-33127
    sprite('es000_07', 7)	# 33128-33134
    sprite('es000_08', 7)	# 33135-33141
    sprite('es000_09', 7)	# 33142-33148
    sprite('es000_10', 7)	# 33149-33155
    gotoLabel(101)
    label(102)
    sprite('es615_00', 7)	# 33156-33162
    sprite('es615_01', 7)	# 33163-33169
    sprite('es615_02', 7)	# 33170-33176
    sprite('es615_03', 7)	# 33177-33183
    SFX_1('bes701brc')
    label(103)
    sprite('es615_04', 7)	# 33184-33190
    sprite('es615_05', 7)	# 33191-33197
    sprite('es615_06', 7)	# 33198-33204
    sprite('es615_07', 7)	# 33205-33211
    if SLOT_97:
        _gotolabel(103)
    sprite('es615_04', 1)	# 33212-33212
    Unknown18008()
    label(104)
    sprite('es615_04', 7)	# 33213-33219
    sprite('es615_05', 7)	# 33220-33226
    sprite('es615_06', 7)	# 33227-33233
    sprite('es615_07', 7)	# 33234-33240
    gotoLabel(104)
    label(110)
    sprite('es615_00', 7)	# 33241-33247
    sprite('es615_01', 7)	# 33248-33254
    sprite('es615_02', 7)	# 33255-33261
    sprite('es615_03', 7)	# 33262-33268
    SFX_1('bes700bha')
    label(111)
    sprite('es615_04', 7)	# 33269-33275
    sprite('es615_05', 7)	# 33276-33282
    sprite('es615_06', 7)	# 33283-33289
    sprite('es615_07', 7)	# 33290-33296
    if SLOT_97:
        _gotolabel(111)
    sprite('es615_04', 1)	# 33297-33297
    Unknown21007(24, 40)
    Unknown21011(420)
    label(112)
    sprite('es615_04', 7)	# 33298-33304
    sprite('es615_05', 7)	# 33305-33311
    sprite('es615_06', 7)	# 33312-33318
    sprite('es615_07', 7)	# 33319-33325
    gotoLabel(112)
    label(120)
    sprite('es615_00', 7)	# 33326-33332
    sprite('es615_01', 7)	# 33333-33339
    sprite('es615_02', 7)	# 33340-33346
    sprite('es615_03', 7)	# 33347-33353
    SFX_1('bes700bny')
    label(121)
    sprite('es615_04', 7)	# 33354-33360
    sprite('es615_05', 7)	# 33361-33367
    sprite('es615_06', 7)	# 33368-33374
    sprite('es615_07', 7)	# 33375-33381
    if SLOT_97:
        _gotolabel(121)
    sprite('es615_04', 1)	# 33382-33382
    Unknown21007(24, 40)
    Unknown21011(270)
    label(122)
    sprite('es615_04', 7)	# 33383-33389
    sprite('es615_05', 7)	# 33390-33396
    sprite('es615_06', 7)	# 33397-33403
    sprite('es615_07', 7)	# 33404-33410
    gotoLabel(122)
    label(130)
    sprite('es615_00', 7)	# 33411-33417
    sprite('es615_01', 7)	# 33418-33424
    sprite('es615_02', 7)	# 33425-33431
    sprite('es615_03', 7)	# 33432-33438
    SFX_1('bes700bpt')
    label(131)
    sprite('es615_04', 7)	# 33439-33445
    sprite('es615_05', 7)	# 33446-33452
    sprite('es615_06', 7)	# 33453-33459
    sprite('es615_07', 7)	# 33460-33466
    if SLOT_97:
        _gotolabel(131)
    sprite('es615_04', 7)	# 33467-33473
    sprite('es615_05', 7)	# 33474-33480
    sprite('es615_06', 7)	# 33481-33487
    sprite('es615_07', 7)	# 33488-33494
    sprite('es615_04', 1)	# 33495-33495
    Unknown21007(24, 40)
    Unknown21011(600)
    label(132)
    sprite('es615_04', 7)	# 33496-33502
    sprite('es615_05', 7)	# 33503-33509
    sprite('es615_06', 7)	# 33510-33516
    sprite('es615_07', 7)	# 33517-33523
    gotoLabel(132)
    label(140)
    sprite('es300_00', 8)	# 33524-33531
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
    sprite('es300_01', 8)	# 33532-33539
    sprite('es300_02', 8)	# 33540-33547
    sprite('es300_03', 6)	# 33548-33553
    sprite('es300_04', 8)	# 33554-33561
    sprite('es300_05', 8)	# 33562-33569
    SFX_1('bes700pbc')
    sprite('es300_06', 8)	# 33570-33577
    label(141)
    sprite('es300_08', 1)	# 33578-33578
    if SLOT_97:
        _gotolabel(141)
    sprite('es300_08', 30)	# 33579-33608
    sprite('es300_08', 32767)	# 33609-66375
    Unknown21007(24, 40)
    Unknown21011(270)
    label(150)
    sprite('es615_00', 7)	# 66376-66382
    sprite('es615_01', 7)	# 66383-66389
    sprite('es615_02', 7)	# 66390-66396
    sprite('es615_03', 7)	# 66397-66403
    SFX_1('bes700pna')
    label(151)
    sprite('es615_04', 7)	# 66404-66410
    sprite('es615_05', 7)	# 66411-66417
    sprite('es615_06', 7)	# 66418-66424
    sprite('es615_07', 7)	# 66425-66431
    if SLOT_97:
        _gotolabel(151)
    sprite('es615_04', 1)	# 66432-66432
    Unknown21007(24, 40)
    Unknown21011(180)
    label(152)
    sprite('es615_04', 7)	# 66433-66439
    sprite('es615_05', 7)	# 66440-66446
    sprite('es615_06', 7)	# 66447-66453
    sprite('es615_07', 7)	# 66454-66460
    gotoLabel(152)
    label(160)
    sprite('es000_00', 1)	# 66461-66461

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('es000_00', 7)	# 66462-66468
    sprite('es000_01', 7)	# 66469-66475
    sprite('es000_02', 7)	# 66476-66482
    sprite('es000_03', 7)	# 66483-66489
    sprite('es000_04', 7)	# 66490-66496
    sprite('es000_05', 7)	# 66497-66503
    sprite('es000_06', 7)	# 66504-66510
    sprite('es000_07', 7)	# 66511-66517
    sprite('es000_08', 7)	# 66518-66524
    sprite('es000_09', 7)	# 66525-66531
    sprite('es000_10', 7)	# 66532-66538
    gotoLabel(161)
    label(162)
    sprite('es615_00', 7)	# 66539-66545
    sprite('es615_01', 7)	# 66546-66552
    sprite('es615_02', 7)	# 66553-66559
    SFX_1('bes701pyo')
    sprite('es615_03', 7)	# 66560-66566
    label(163)
    sprite('es615_04', 7)	# 66567-66573
    sprite('es615_05', 7)	# 66574-66580
    sprite('es615_06', 7)	# 66581-66587
    sprite('es615_07', 7)	# 66588-66594
    if SLOT_97:
        _gotolabel(163)
    sprite('es615_04', 7)	# 66595-66601
    Unknown21007(24, 40)
    Unknown21011(180)
    sprite('es615_05', 7)	# 66602-66608
    sprite('es615_06', 7)	# 66609-66615
    sprite('es615_07', 7)	# 66616-66622
    label(164)
    sprite('es615_04', 7)	# 66623-66629
    sprite('es615_05', 7)	# 66630-66636
    sprite('es615_06', 7)	# 66637-66643
    sprite('es615_07', 7)	# 66644-66650
    gotoLabel(164)
    label(170)
    sprite('es615_00', 7)	# 66651-66657
    sprite('es615_01', 7)	# 66658-66664
    sprite('es615_02', 7)	# 66665-66671
    sprite('es615_03', 7)	# 66672-66678
    SFX_1('bes700uli')
    label(171)
    sprite('es615_04', 7)	# 66679-66685
    sprite('es615_05', 7)	# 66686-66692
    sprite('es615_06', 7)	# 66693-66699
    sprite('es615_07', 7)	# 66700-66706
    if SLOT_97:
        _gotolabel(171)
    sprite('es615_04', 1)	# 66707-66707
    Unknown21007(24, 40)
    Unknown21011(120)
    label(172)
    sprite('es615_04', 7)	# 66708-66714
    sprite('es615_05', 7)	# 66715-66721
    sprite('es615_06', 7)	# 66722-66728
    sprite('es615_07', 7)	# 66729-66735
    gotoLabel(172)
    label(180)
    sprite('es000_00', 1)	# 66736-66736

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('es000_00', 7)	# 66737-66743
    sprite('es000_01', 7)	# 66744-66750
    sprite('es000_02', 7)	# 66751-66757
    sprite('es000_03', 7)	# 66758-66764
    sprite('es000_04', 7)	# 66765-66771
    sprite('es000_05', 7)	# 66772-66778
    sprite('es000_06', 7)	# 66779-66785
    sprite('es000_07', 7)	# 66786-66792
    sprite('es000_08', 7)	# 66793-66799
    sprite('es000_09', 7)	# 66800-66806
    sprite('es000_10', 7)	# 66807-66813
    gotoLabel(181)
    label(182)
    sprite('es300_00', 8)	# 66814-66821
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
    sprite('es300_01', 8)	# 66822-66829
    sprite('es300_02', 8)	# 66830-66837
    sprite('es300_03', 6)	# 66838-66843
    sprite('es300_04', 8)	# 66844-66851
    SFX_1('bes701rrb')
    sprite('es300_05', 8)	# 66852-66859
    sprite('es300_06', 8)	# 66860-66867
    label(183)
    sprite('es300_08', 1)	# 66868-66868
    if SLOT_97:
        _gotolabel(183)
    sprite('es300_08', 32767)	# 66869-99635
    Unknown23018(1)
    label(190)
    sprite('es000_00', 1)	# 99636-99636

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
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
    label(191)
    sprite('es000_00', 7)	# 99637-99643
    sprite('es000_01', 7)	# 99644-99650
    sprite('es000_02', 7)	# 99651-99657
    sprite('es000_03', 7)	# 99658-99664
    sprite('es000_04', 7)	# 99665-99671
    sprite('es000_05', 7)	# 99672-99678
    sprite('es000_06', 7)	# 99679-99685
    sprite('es000_07', 7)	# 99686-99692
    sprite('es000_08', 7)	# 99693-99699
    sprite('es000_09', 7)	# 99700-99706
    sprite('es000_10', 7)	# 99707-99713
    gotoLabel(191)
    label(192)
    sprite('keep', 1)	# 99714-99714
    if (not SLOT_2):
        sendToLabel(193)
    sprite('es003_00', 6)	# 99715-99720
    Unknown2005()
    sprite('es003_01', 4)	# 99721-99724
    sprite('es003_01ex00', 4)	# 99725-99728
    sprite('es003_00ex00', 5)	# 99729-99733
    label(193)
    sprite('es300_00', 8)	# 99734-99741
    sprite('es300_01', 8)	# 99742-99749
    sprite('es300_02', 8)	# 99750-99757
    sprite('es300_03', 6)	# 99758-99763
    sprite('es300_04', 8)	# 99764-99771
    sprite('es639_00', 8)	# 99772-99779
    sprite('es639_01', 8)	# 99780-99787
    sprite('es639_02', 8)	# 99788-99795
    SFX_1('bes701uvaB')
    Unknown23018(1)
    sprite('es639_03', 8)	# 99796-99803
    sprite('es639_04', 8)	# 99804-99811
    sprite('es639_05', 8)	# 99812-99819
    label(194)
    sprite('es639_06', 8)	# 99820-99827
    sprite('es639_07', 8)	# 99828-99835
    sprite('es639_08', 8)	# 99836-99843
    sprite('es639_09', 8)	# 99844-99851
    loopRest()
    gotoLabel(194)
    label(200)
    sprite('keep', 1)	# 99852-99852
    if (SLOT_38 == 1):
        if (SLOT_152 == 1):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                Unknown2037(1)
                Unknown36(24)
                Unknown2037(1)
                Unknown35()
    if (SLOT_38 == 0):
        if (SLOT_152 == 0):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                Unknown2037(1)
                Unknown36(24)
                Unknown2037(1)
                Unknown35()
    sprite('keep', 1)	# 99853-99853
    if (not SLOT_2):
        sendToLabel(201)
    sprite('es003_00', 6)	# 99854-99859
    Unknown2005()
    sprite('es003_01', 4)	# 99860-99863
    sprite('es003_01ex00', 4)	# 99864-99867
    sprite('es003_00ex00', 5)	# 99868-99872
    label(201)
    sprite('es300_00', 8)	# 99873-99880
    SFX_1('bes700pla')
    sprite('es300_01', 8)	# 99881-99888
    sprite('es300_02', 8)	# 99889-99896
    sprite('es300_03', 6)	# 99897-99902
    sprite('es300_04', 8)	# 99903-99910
    sprite('es300_05', 8)	# 99911-99918
    sprite('es300_06', 8)	# 99919-99926
    label(202)
    sprite('es300_08', 1)	# 99927-99927
    if SLOT_97:
        _gotolabel(202)
    sprite('es300_08', 20)	# 99928-99947
    sprite('es300_08', 32767)	# 99948-132714
    Unknown21007(24, 40)
    Unknown21011(360)

@State
def CmnActLose():
    sprite('es620_00', 7)	# 1-7
    SFX_0('019_cloth_c')
    sprite('es620_01', 7)	# 8-14
    sprite('es620_02', 7)	# 15-21
    if random_(2, 0, 50):
        SFX_1('bes403_0')
    else:
        SFX_1('bes403_1')
    sprite('es620_03', 7)	# 22-28
    sprite('es620_04', 7)	# 29-35
    sprite('es620_05', 7)	# 36-42
    sprite('es620_06', 7)	# 43-49
    sprite('es620_07', 7)	# 50-56
    Unknown23018(1)
    sprite('es620_08', 32767)	# 57-32823
