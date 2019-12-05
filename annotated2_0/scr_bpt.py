@Subroutine
def StuffColorShuffle():
    op(0, 2, 0, 0, 1)
    op(3, 2, 0, 0, 2)
    Unknown61(0, 1, 0, 8, 0, 0, 2, 0, 0, 9999, 0, 9999)
    SLOT_4 = 1
    SLOT_59 = SLOT_0
    Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def StuffColorReset():
    SLOT_4 = 0
    SLOT_59 = 0
    Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def WeaponCreate_Assist_Near():
    SLOT_59 = 0
    Unknown61(0, 1, 0, 3, 0, 0, 2, 0, 0, 9999, 0, 9999)
    SLOT_59 = SLOT_0
    SLOT_4 = 1
    if SLOT_5:
        if random_(2, 0, 33):
            SLOT_59 = 1
    SLOT_59 = (SLOT_59 * 2)
    Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def Weapon_Assist_Near():
    if (SLOT_59 == 2):
        sendToLabel(1)
    if (SLOT_59 == 4):
        sendToLabel(2)
    if (SLOT_59 == 6):
        sendToLabel(3)
    if (SLOT_59 == 8):
        sendToLabel(4)

@Subroutine
def WeaponCreate_Assist_Far():
    SLOT_59 = 0
    Unknown61(0, 5, 0, 8, 0, 0, 2, 0, 0, 9999, 0, 9999)
    SLOT_59 = SLOT_0
    SLOT_4 = 1
    if (SLOT_59 == 7):
        if random_(2, 0, 33):
            SLOT_59 = (SLOT_59 + (-2))
        elif random_(2, 0, 50):
            SLOT_59 = (SLOT_59 + (-1))
        else:
            SLOT_59 = (SLOT_59 + 1)
    SLOT_59 = (SLOT_59 * 2)
    Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def WeaponThrow_Assist_Far():
    if (SLOT_59 == 10):
        if SLOT_58:
            GFX_0('SpBomb_TAG', 0)
            if (not SLOT_7):
                Unknown7006('bpt319_0', 100, 863268962, 811544626, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown7006('bpt319_1', 100, 863268962, 828321842, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            GFX_0('Bomb_TAG', 0)
            if (not SLOT_7):
                Unknown7006('bpt317_0', 100, 863268962, 811546673, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown7006('bpt317_1', 100, 863268962, 828323889, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if (SLOT_59 == 12):
        if SLOT_58:
            GFX_0('SpMissile_TAG', 1)
            if (not SLOT_7):
                Unknown7006('bpt323_0', 100, 863268962, 811545650, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown7006('bpt323_1', 100, 863268962, 828322866, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            GFX_0('Missile_TAG', 1)
            if (not SLOT_7):
                Unknown7006('bpt321_0', 100, 863268962, 811545138, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown7006('bpt321_1', 100, 863268962, 828322354, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if (SLOT_59 == 14):
        pass

@Subroutine
def TrapUpDate():
    if Unknown46(6):
        if (not Unknown46(5)):
            Unknown38(5, 6)
        else:
            Unknown21007(6, 32)
    if Unknown46(5):
        Unknown38(6, 5)
    GFX_0('Trap', 0)
    Unknown38(5, 1)

@Subroutine
def SpTrapUpDate():
    if Unknown46(6):
        if (not Unknown46(5)):
            Unknown38(5, 6)
        else:
            Unknown21007(6, 32)
    if Unknown46(5):
        Unknown38(6, 5)
    GFX_0('SpTrap', 0)
    Unknown38(5, 1)

@Subroutine
def CheckHiWeapon():
    SLOT_47 = 0
    if (not SLOT_5):
        SLOT_47 = 1

@Subroutine
def PreInit():
    Unknown12019('62707400000000000000000000000000')

@Subroutine
def MatchInit():
    DashFInitialVelocity(20000)
    Unknown12038(26000)
    Unknown12034(30)
    Unknown12024(1)
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
    Unknown14015(0, 500000, -100000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 220000, -100000, 200000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 600000, -200000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 600000, -200000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x1)
    MoveMaxChainRepeat(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown15021(5000)
    Unknown15013(50)
    Unknown14015(0, 450000, 0, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 150000, 1000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15021(1)
    Unknown14015(0, 450000, 0, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown14015(100000, 350000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 100000, 2500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(200000, 500000, 100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15008()
    Unknown14015(50000, 400000, -150000, 250000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown15008()
    Unknown14015(-100000, 200000, -350000, 0, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15008()
    Unknown14015(-100000, 250000, -400000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15008()
    Unknown15021(500)
    Unknown14015(50000, 400000, -150000, 250000, 2000, 50)
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
    Move_Register('Surfing_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15009()
    Unknown15012(1)
    Unknown15013(1)
    Unknown14015(0, 500000, -200000, 150000, 250, 20)
    Move_EndRegister()
    Move_Register('Surfing_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown15012(1)
    Unknown15013(1)
    Unknown14015(0, 400000, -200000, 400000, 250, 20)
    Move_EndRegister()
    Move_Register('DriveShot_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(700000, 1300000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('DriveShot_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(700000, 1300000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('AirDriveShot_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(150000, 350000, -400000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('AirDriveShot_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(550000, 1150000, -400000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('HoppingA', INPUT_SPECIALMOVE)
    Unknown14013('Hopping')
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15012(1)
    Unknown14015(-50000, 300000, -250000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('AirSlide', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3002)
    Unknown14015(-200000, 200000, -400000, -100000, 7000, 50)
    Move_EndRegister()
    Move_Register('HoppingPlus_A', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3036)
    Unknown14015(50000, 300000, -300000, 100000, 20000, 50)
    Move_EndRegister()
    Move_Register('HoppingPlus_B', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3036)
    Unknown14015(-150000, 150000, -300000, -50000, 10000, 50)
    Move_EndRegister()
    Move_Register('HoppingPlus_C', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3036)
    Unknown14015(-200000, 50000, -300000, -50000, 10000, 50)
    Move_EndRegister()
    Move_Register('Surfing_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15021(500)
    Unknown14015(0, 500000, -200000, 150000, 250, 10)
    Move_EndRegister()
    Move_Register('AirSlide_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3002)
    Unknown14015(-200000, 200000, -400000, -100000, 250, 10)
    Move_EndRegister()
    Move_Register('DriveShot_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(700000, 1300000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('AirDriveShot_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(550000, 1150000, -400000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(0, 200000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('HiWeapon', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(2500)
    Unknown14015(0, 0, 0, 0, 0, 40)
    Move_EndRegister()
    Move_Register('HiWeapon_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(2500)
    Unknown14015(0, 0, 0, 0, 0, 40)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15013(1000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-130000, 130000, -200000, 150000, 10000, 50)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15013(1000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-130000, 130000, -200000, 150000, 10000, 50)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 2000000, -150000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BBB', 'Surfing_B', 10000000)
    Unknown15024('NmlAtk5BBB', 'Surfing_Ex', 10000000)
    Unknown15024('NmlAtk5BBB', 'UltimateAssault', 10000000)
    Unknown15024('NmlAtk5BBB', 'UltimateAssault_OD', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5BB', 'HiWeapon', 10000000)
    Unknown15024('NmlAtk5BB', 'HiWeapon_OD', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2C', 'Surfing_B', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateAssault', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateAssault_OD', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown12018(0, 'pt062_01')
    Unknown12018(1, 'pt062_03')
    Unknown12018(2, 'pt062_04')
    Unknown12018(3, 'pt062_05')
    Unknown12018(4, 'pt062_05')
    Unknown12018(5, 'pt062_06')
    Unknown12018(6, 'pt062_07')
    Unknown12018(7, 'pt041_02')
    Unknown12018(8, 'pt040_02')
    Unknown12018(9, 'pt045_02')
    Unknown12018(10, 'pt060_00')
    Unknown12018(11, 'pt060_01')
    Unknown12018(12, 'pt060_03')
    Unknown12018(13, 'pt060_05')
    Unknown12018(14, 'pt060_07')
    Unknown12018(15, 'pt060_14')
    Unknown12018(16, 'pt050_00')
    Unknown12018(17, 'pt052_00')
    Unknown12018(18, 'pt054_00')
    Unknown12018(19, 'pt000_00')
    Unknown12018(20, 'pt000_00')
    Unknown12018(25, 'pt063_00')
    Unknown12018(26, 'pt063_01')
    Unknown12018(27, 'pt063_02')
    Unknown12018(28, 'pt063_04')
    Unknown12018(29, 'pt063_10')
    Unknown12018(24, 'pt073_01')
    GFX_0('PaletteControlObj1', -1)
    GFX_0('PaletteControlObj2', -1)
    GFX_0('PaletteControlObj3', -1)
    GFX_0('PaletteControlObj4', -1)
    GFX_0('PaletteControlObj5', -1)
    GFX_0('PaletteControlObj6', -1)
    GFX_0('PaletteControlObj7', -1)
    GFX_0('PaletteControlObj8', -1)
    GFX_0('SphereLight', -1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('040000004869576561706f6e000000000000000000000000000000000000000000000000')
    Unknown12059('050000004869576561706f6e5f4f44000000000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    if random_(2, 0, 50):
        SLOT_7 = 0
    else:
        SLOT_7 = 1
    Unknown23003(0, 1, 9, 1, 60000, 0, -60269, -60269)

@Subroutine
def OnFrameStep():
    if (not SLOT_7):
        Unknown7010(0, 'bpt000_0')
        Unknown7010(1, 'bpt001_0')
        Unknown7010(2, 'bpt002_0')
        Unknown7010(3, 'bpt003_0')
        Unknown7010(4, 'bpt004_0')
        Unknown7010(5, 'bpt005_0')
        Unknown7010(6, 'bpt006_0')
        Unknown7010(7, 'bpt007_0')
        Unknown7010(8, 'bpt008_0')
        Unknown7010(9, 'bpt009_0')
        Unknown7010(10, 'bpt010_0')
        Unknown7010(15, 'bpt011_0')
        Unknown7010(16, 'bpt012_0')
        Unknown7010(17, 'bpt013_0')
        Unknown7010(18, 'bpt014_0')
        Unknown7010(19, 'bpt015_0')
        Unknown7010(20, 'bpt016_0')
        Unknown7010(21, 'bpt017_0')
        Unknown7010(22, 'bpt018_0')
        Unknown7010(23, 'bpt019_0')
        Unknown7010(24, 'bpt020_0')
        Unknown7010(25, 'bpt021_0')
        Unknown7010(28, 'bpt022_0')
        Unknown7010(29, 'bpt023_0')
        Unknown7010(30, 'bpt024_0')
        Unknown7010(31, 'bpt025_0')
        Unknown7010(32, 'bpt026_0')
        Unknown7010(33, 'bpt027_0')
        Unknown7010(34, 'bpt028_0')
        Unknown7010(35, 'bpt029_0')
        Unknown7010(36, 'bpt030_0')
        Unknown7010(37, 'bpt031_0')
        Unknown7010(39, 'bpt032_0')
        Unknown7010(42, 'bpt033_0')
        Unknown7010(43, 'bpt034_0')
        Unknown7010(44, 'bpt035_0')
        Unknown7010(45, 'bpt036_0')
        Unknown7010(46, 'bpt037_0')
        Unknown7010(47, 'bpt038_0')
        Unknown7010(48, 'bpt039_0')
        Unknown7010(49, 'bpt040_0')
        Unknown7010(50, 'bpt041_0')
        Unknown7010(52, 'bpt042_0')
        Unknown7010(53, 'bpt043_0')
        Unknown7010(54, 'bpt100_0')
        Unknown7010(55, 'bpt101_0')
        Unknown7010(56, 'bpt100_0')
        Unknown7010(63, 'bpt100_0')
        Unknown7010(64, 'bpt101_0')
        Unknown7010(65, 'bpt101_0')
        Unknown7010(57, 'bpt102_0')
        Unknown7010(58, 'bpt103_0')
        Unknown7010(59, 'bpt102_0')
        Unknown7010(66, 'bpt102_0')
        Unknown7010(67, 'bpt103_0')
        Unknown7010(68, 'bpt103_0')
        Unknown7010(60, 'bpt104_0')
        Unknown7010(61, 'bpt105_0')
        Unknown7010(62, 'bpt104_0')
        Unknown7010(69, 'bpt104_0')
        Unknown7010(70, 'bpt105_0')
        Unknown7010(71, 'bpt105_0')
        Unknown7010(72, 'bpt150_0')
        Unknown7010(73, 'bpt151_0')
        Unknown7010(74, 'bpt152_0')
        Unknown7010(85, 'bpt153_0')
        Unknown7010(87, 'bpt154_0')
        Unknown7010(88, 'bpt155_0')
        Unknown7010(96, 'bpt161_0')
        Unknown7010(97, 'bpt161_0')
        Unknown7010(92, 'bpt162_0')
        Unknown7010(93, 'bpt162_0')
        Unknown7010(98, 'bpt163_0')
        Unknown7010(99, 'bpt163_0')
        Unknown7010(100, 'bpt164_0')
        Unknown7010(101, 'bpt164_0')
        Unknown7010(105, 'bpt165_0')
        Unknown7010(106, 'bpt165_0')
        Unknown7010(102, 'bpt166_0')
        Unknown7010(103, 'bpt166_0')
        Unknown7010(90, 'bpt167_0')
        Unknown7010(91, 'bpt167_0')
        Unknown7010(107, 'bpt168_0')
        Unknown7010(108, 'bpt168_0')
        Unknown7010(110, 'bpt169_0')
        Unknown7010(111, 'bpt169_0')
        Unknown7010(112, 'bpt159_0')
        Unknown7010(113, 'bpt159_0')
        Unknown7010(94, 'bpt400_0')
        Unknown7010(95, 'bpt400_0')
    if SLOT_7:
        Unknown7010(0, 'bpt000_1')
        Unknown7010(1, 'bpt001_1')
        Unknown7010(2, 'bpt002_1')
        Unknown7010(3, 'bpt003_1')
        Unknown7010(4, 'bpt004_1')
        Unknown7010(5, 'bpt005_1')
        Unknown7010(6, 'bpt006_1')
        Unknown7010(7, 'bpt007_1')
        Unknown7010(8, 'bpt008_1')
        Unknown7010(9, 'bpt009_1')
        Unknown7010(10, 'bpt010_1')
        Unknown7010(15, 'bpt011_1')
        Unknown7010(16, 'bpt012_1')
        Unknown7010(17, 'bpt013_1')
        Unknown7010(18, 'bpt014_1')
        Unknown7010(19, 'bpt015_1')
        Unknown7010(20, 'bpt016_1')
        Unknown7010(21, 'bpt017_1')
        Unknown7010(22, 'bpt018_1')
        Unknown7010(23, 'bpt019_1')
        Unknown7010(24, 'bpt020_1')
        Unknown7010(25, 'bpt021_1')
        Unknown7010(28, 'bpt022_1')
        Unknown7010(29, 'bpt023_1')
        Unknown7010(30, 'bpt024_1')
        Unknown7010(31, 'bpt025_1')
        Unknown7010(32, 'bpt026_1')
        Unknown7010(33, 'bpt027_1')
        Unknown7010(34, 'bpt028_1')
        Unknown7010(35, 'bpt029_1')
        Unknown7010(36, 'bpt030_1')
        Unknown7010(37, 'bpt031_1')
        Unknown7010(39, 'bpt032_1')
        Unknown7010(42, 'bpt033_1')
        Unknown7010(43, 'bpt034_1')
        Unknown7010(44, 'bpt035_1')
        Unknown7010(45, 'bpt036_1')
        Unknown7010(46, 'bpt037_1')
        Unknown7010(47, 'bpt038_1')
        Unknown7010(48, 'bpt039_1')
        Unknown7010(49, 'bpt040_1')
        Unknown7010(50, 'bpt041_1')
        Unknown7010(52, 'bpt042_1')
        Unknown7010(53, 'bpt043_1')
        Unknown7010(54, 'bpt100_1')
        Unknown7010(55, 'bpt101_1')
        Unknown7010(56, 'bpt100_1')
        Unknown7010(63, 'bpt100_1')
        Unknown7010(64, 'bpt101_1')
        Unknown7010(65, 'bpt101_1')
        Unknown7010(57, 'bpt102_1')
        Unknown7010(58, 'bpt103_1')
        Unknown7010(59, 'bpt102_1')
        Unknown7010(66, 'bpt102_1')
        Unknown7010(67, 'bpt103_1')
        Unknown7010(68, 'bpt103_1')
        Unknown7010(60, 'bpt104_1')
        Unknown7010(61, 'bpt105_1')
        Unknown7010(62, 'bpt104_1')
        Unknown7010(69, 'bpt104_1')
        Unknown7010(70, 'bpt105_1')
        Unknown7010(71, 'bpt105_1')
        Unknown7010(72, 'bpt150_1')
        Unknown7010(73, 'bpt151_1')
        Unknown7010(74, 'bpt152_1')
        Unknown7010(85, 'bpt153_1')
        Unknown7010(87, 'bpt154_1')
        Unknown7010(88, 'bpt155_1')
        Unknown7010(96, 'bpt161_1')
        Unknown7010(97, 'bpt161_1')
        Unknown7010(92, 'bpt162_1')
        Unknown7010(93, 'bpt162_1')
        Unknown7010(98, 'bpt163_1')
        Unknown7010(99, 'bpt163_1')
        Unknown7010(100, 'bpt164_1')
        Unknown7010(101, 'bpt164_1')
        Unknown7010(105, 'bpt165_1')
        Unknown7010(106, 'bpt165_1')
        Unknown7010(102, 'bpt166_1')
        Unknown7010(103, 'bpt166_1')
        Unknown7010(90, 'bpt167_1')
        Unknown7010(91, 'bpt167_1')
        Unknown7010(107, 'bpt168_1')
        Unknown7010(108, 'bpt168_1')
        Unknown7010(110, 'bpt169_1')
        Unknown7010(111, 'bpt169_1')
        Unknown7010(112, 'bpt159_1')
        Unknown7010(113, 'bpt159_1')
        Unknown7010(94, 'bpt400_1')
        Unknown7010(95, 'bpt400_1')
    if (not SLOT_5):
        Unknown23008(0, 0)
    else:
        Unknown23008(0, 1)
    if (not SLOT_31):
        SLOT_5 = 0
    if SLOT_31:
        if (not 
        if (not Unknown23148('HiWeapon')):
            Unknown23148('HiWeapon_OD')):
            if (SLOT_5 >= 1):
                if (not SLOT_114):
                    SLOT_31 = (SLOT_31 + (-50))
    if SLOT_IsPlayer2:
        Unknown58('TRI_BPTPowerUp', 2, 67)
        if (SLOT_67 == 1):
            SLOT_31 = 60000
            SLOT_5 = 1
    if SLOT_170:
        SLOT_31 = 0
    if (not SLOT_63):
        if (not SLOT_28):
            SLOT_63 = 1
    elif SLOT_28:
        SLOT_63 = 0
        if (not SLOT_63):
            GFX_0('SphereLight_Shutsugen', 108)
            SLOT_63 = 34
    if SLOT_63:
        SLOT_63 = (SLOT_63 + (-1))
    if SLOT_37:
        SLOT_6 = 1
    if (not SLOT_8):
        SLOT_8 = 1
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1

@Subroutine
def OnMainEnemyComboBreak():
    if random_(2, 0, 50):
        SLOT_7 = 0
    else:
        SLOT_7 = 1

@Subroutine
def OnActionBegin():
    Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def OnFinalize():
    callSubroutine('StuffColorReset')

@State
def CmnActStand():
    label(0)
    sprite('pt000_00', 7)	# 1-7
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('pt001_00', 7)	# 99-105
    SLOT_88 = 960
    if (not SLOT_7):
        SFX_4('bpt000_0')
    else:
        SFX_4('bpt000_1')
    sprite('pt001_01', 5)	# 106-110
    sprite('pt001_02', 8)	# 111-118
    sprite('pt001_03', 8)	# 119-126
    sprite('pt001_04', 8)	# 127-134
    sprite('pt001_05', 8)	# 135-142
    sprite('pt001_06', 5)	# 143-147
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('pt003_00', 3)	# 1-3
    sprite('pt003_01', 3)	# 4-6
    sprite('pt003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('pt010_00', 4)	# 1-4
    sprite('pt010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('pt010_02', 6)	# 1-6
    sprite('pt010_03', 6)	# 7-12
    sprite('pt010_04', 6)	# 13-18
    sprite('pt010_05', 6)	# 19-24
    sprite('pt010_06', 6)	# 25-30
    sprite('pt010_07', 6)	# 31-36
    sprite('pt010_08', 6)	# 37-42
    sprite('pt010_09', 6)	# 43-48
    sprite('pt010_10', 6)	# 49-54
    sprite('pt010_11', 6)	# 55-60
    sprite('pt010_12', 6)	# 61-66
    sprite('pt010_13', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('pt013_00', 3)	# 1-3
    sprite('pt013_01', 3)	# 4-6
    sprite('pt013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('pt010_01', 4)	# 1-4
    sprite('pt010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('pt023_00', 2)	# 1-2
    sprite('pt023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    sprite('pt020_00', 4)	# 1-4
    sprite('pt020_01', 4)	# 5-8
    SFX_4('pt002')
    gotoLabel(0)
    label(1)
    sprite('pt020_00', 4)	# 9-12
    sprite('pt020_01', 4)	# 13-16
    SFX_4('pt002')
    gotoLabel(0)
    label(2)
    sprite('pt020_00', 4)	# 17-20
    sprite('pt020_01', 4)	# 21-24
    SFX_4('pt003')
    gotoLabel(0)
    label(0)
    sprite('pt020_00', 4)	# 25-28
    sprite('pt020_01', 4)	# 29-32
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('pt020_02', 3)	# 1-3
    sprite('pt020_03', 3)	# 4-6
    sprite('pt020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('pt020_05', 3)	# 1-3
    sprite('pt020_06', 3)	# 4-6
    label(0)
    sprite('pt020_07', 4)	# 7-10
    sprite('pt020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('pt024_00', 3)	# 1-3
    sprite('pt024_01', 3)	# 4-6
    sprite('pt024_02', 3)	# 7-9

@State
def CmnActLandingStiffLoop():
    sprite('pt024_00', 4)	# 1-4
    sprite('pt024_01', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('pt024_02', 6)	# 1-6

@State
def CmnActFWalk():
    sprite('pt030_00', 5)	# 1-5
    sprite('pt030_01', 5)	# 6-10
    label(0)
    sprite('pt030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 16-20
    sprite('pt030_04', 5)	# 21-25
    sprite('pt030_05', 5)	# 26-30
    sprite('pt030_06', 5)	# 31-35
    sprite('pt030_07', 5)	# 36-40
    sprite('pt030_08', 5)	# 41-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 46-50
    sprite('pt030_10', 5)	# 51-55
    sprite('pt030_11', 5)	# 56-60
    sprite('pt030_12', 5)	# 61-65
    sprite('pt030_13', 5)	# 66-70
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('pt031_00', 7)	# 1-7
    sprite('pt031_01', 7)	# 8-14
    label(0)
    sprite('pt031_02', 7)	# 15-21
    sprite('pt031_03', 7)	# 22-28
    sprite('pt031_04', 7)	# 29-35
    sprite('pt031_05', 7)	# 36-42
    sprite('pt031_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt031_07', 7)	# 50-56
    sprite('pt031_08', 7)	# 57-63
    sprite('pt031_09', 7)	# 64-70
    sprite('pt031_10', 7)	# 71-77
    sprite('pt031_11', 7)	# 78-84
    sprite('pt031_12', 7)	# 85-91
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt031_13', 7)	# 92-98
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('pt030_00', 5)	# 1-5
    sprite('pt032_00', 2)	# 6-7
    sprite('pt032_01', 2)	# 8-9
    label(0)
    sprite('pt032_02', 4)	# 10-13
    sprite('pt032_03', 4)	# 14-17
    Unknown8006(100, 1, 1)
    sprite('pt032_04', 4)	# 18-21
    sprite('pt032_05', 4)	# 22-25
    sprite('pt032_06', 4)	# 26-29
    sprite('pt032_07', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('pt032_08', 4)	# 34-37
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('pt032_09', 4)	# 1-4
    sprite('pt032_10', 4)	# 5-8
    sprite('pt032_11', 4)	# 9-12

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
    sprite('pt033_00', 1)	# 1-1
    sprite('pt033_01', 2)	# 2-3
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    SFX_4('pt005')
    sprite('pt033_02', 2)	# 4-5
    sprite('pt033_02', 1)	# 6-6
    sprite('pt033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('pt033_02', 3)	# 10-12
    sprite('pt033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt033_04', 2)	# 16-17
    sprite('pt033_05', 2)	# 18-19
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('pt033_06', 2)	# 20-21

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('pt035_00', 3)	# 1-3
    SFX_4('pt004')
    label(0)
    sprite('pt035_01', 4)	# 4-7
    sprite('pt035_02', 4)	# 8-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('pt036_00', 3)	# 1-3
    SFX_4('pt006')
    label(0)
    sprite('pt036_01', 4)	# 4-7
    sprite('pt036_02', 4)	# 8-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('pt050_00', 1)	# 1-1
    sprite('pt050_01', 1)	# 2-2
    sprite('pt050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('pt050_01', 1)	# 1-1
    sprite('pt050_02', 1)	# 2-2
    sprite('pt050_01', 2)	# 3-4
    sprite('pt050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('pt050_02', 1)	# 1-1
    sprite('pt050_03', 1)	# 2-2
    sprite('pt050_02', 2)	# 3-4
    sprite('pt050_01', 2)	# 5-6
    sprite('pt050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('pt050_03', 1)	# 1-1
    sprite('pt050_04', 1)	# 2-2
    sprite('pt050_03', 2)	# 3-4
    sprite('pt050_02', 2)	# 5-6
    sprite('pt050_01', 2)	# 7-8
    sprite('pt050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('pt050_04', 1)	# 1-1
    sprite('pt050_04', 1)	# 2-2
    sprite('pt050_04', 2)	# 3-4
    sprite('pt050_03', 2)	# 5-6
    sprite('pt050_02', 2)	# 7-8
    sprite('pt050_01', 2)	# 9-10
    sprite('pt050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('pt052_00', 1)	# 1-1
    sprite('pt052_01', 1)	# 2-2
    sprite('pt052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('pt052_01', 1)	# 1-1
    sprite('pt052_02', 1)	# 2-2
    sprite('pt052_01', 2)	# 3-4
    sprite('pt052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('pt052_02', 1)	# 1-1
    sprite('pt052_03', 1)	# 2-2
    sprite('pt052_02', 2)	# 3-4
    sprite('pt052_01', 2)	# 5-6
    sprite('pt052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('pt052_03', 1)	# 1-1
    sprite('pt052_04', 1)	# 2-2
    sprite('pt052_03', 2)	# 3-4
    sprite('pt052_02', 2)	# 5-6
    sprite('pt052_01', 2)	# 7-8
    sprite('pt052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('pt052_04', 1)	# 1-1
    sprite('pt052_04', 1)	# 2-2
    sprite('pt052_04', 2)	# 3-4
    sprite('pt052_03', 2)	# 5-6
    sprite('pt052_02', 2)	# 7-8
    sprite('pt052_01', 2)	# 9-10
    sprite('pt052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('pt054_00', 1)	# 1-1
    sprite('pt054_01', 1)	# 2-2
    sprite('pt054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('pt054_01', 1)	# 1-1
    sprite('pt054_02', 1)	# 2-2
    sprite('pt054_01', 2)	# 3-4
    sprite('pt054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('pt054_02', 1)	# 1-1
    sprite('pt054_03', 1)	# 2-2
    sprite('pt054_02', 2)	# 3-4
    sprite('pt054_01', 2)	# 5-6
    sprite('pt054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('pt054_03', 1)	# 1-1
    sprite('pt054_04', 1)	# 2-2
    sprite('pt054_03', 2)	# 3-4
    sprite('pt054_02', 2)	# 5-6
    sprite('pt054_01', 2)	# 7-8
    sprite('pt054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('pt054_04', 1)	# 1-1
    sprite('pt054_04', 1)	# 2-2
    sprite('pt054_04', 2)	# 3-4
    sprite('pt054_03', 2)	# 5-6
    sprite('pt054_02', 2)	# 7-8
    sprite('pt054_01', 2)	# 9-10
    sprite('pt054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('pt060_00', 4)	# 1-4
    label(0)
    sprite('pt060_01', 4)	# 5-8
    sprite('pt060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('pt060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('pt062_05', 3)	# 1-3
    sprite('pt062_06', 3)	# 4-6
    label(0)
    sprite('pt062_07', 3)	# 7-9
    sprite('pt062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('pt062_09', 2)	# 1-2
    sprite('pt062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('pt063_06', 2)	# 1-2
    sprite('pt063_07', 2)	# 3-4
    sprite('pt063_08', 3)	# 5-7
    sprite('pt063_09', 3)	# 8-10
    sprite('pt063_10', 3)	# 11-13

@State
def CmnActBDownLoop():
    sprite('pt063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('pt064_00', 2)	# 1-2
    sprite('pt064_01', 2)	# 3-4
    sprite('pt064_02', 2)	# 5-6
    sprite('pt064_03', 2)	# 7-8
    sprite('pt064_04', 2)	# 9-10
    sprite('pt064_05', 2)	# 11-12
    sprite('pt064_06', 2)	# 13-14
    sprite('pt064_07', 2)	# 15-16
    sprite('pt064_08', 2)	# 17-18
    sprite('pt064_09', 2)	# 19-20
    sprite('pt064_10', 2)	# 21-22

@State
def CmnActFDownUpper():
    sprite('pt063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('pt063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('pt063_02', 3)	# 1-3
    sprite('pt063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('pt063_04', 3)	# 1-3
    sprite('pt063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('pt063_06', 2)	# 1-2
    sprite('pt063_07', 2)	# 3-4
    sprite('pt063_08', 3)	# 5-7
    sprite('pt063_09', 3)	# 8-10
    sprite('pt063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('pt063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('pt064_00', 2)	# 1-2
    sprite('pt064_01', 2)	# 3-4
    sprite('pt064_02', 2)	# 5-6
    sprite('pt064_03', 2)	# 7-8
    sprite('pt064_04', 2)	# 9-10
    sprite('pt064_05', 2)	# 11-12
    sprite('pt064_06', 2)	# 13-14
    sprite('pt064_07', 2)	# 15-16
    sprite('pt064_08', 2)	# 17-18
    sprite('pt064_09', 2)	# 19-20
    sprite('pt064_10', 2)	# 21-22

@State
def CmnActVDownUpper():
    sprite('pt062_00', 3)	# 1-3
    label(0)
    sprite('pt062_01', 3)	# 4-6
    sprite('pt062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('pt062_03', 3)	# 1-3
    sprite('pt062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('pt062_05', 3)	# 1-3
    sprite('pt062_06', 3)	# 4-6
    label(0)
    sprite('pt062_07', 3)	# 7-9
    sprite('pt062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('pt062_09', 2)	# 1-2
    sprite('pt062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('pt072_00', 3)	# 1-3
    sprite('pt072_01', 3)	# 4-6
    sprite('pt072_02', 3)	# 7-9
    label(0)
    sprite('pt072_01', 3)	# 10-12
    sprite('pt072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('pt074_00', 3)	# 1-3
    sprite('pt074_01', 3)	# 4-6
    sprite('pt074_02', 3)	# 7-9
    sprite('pt074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('pt082_00', 2)	# 1-2
    sprite('pt082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('pt071_06', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('pt073_00', 3)	# 1-3
    sprite('pt073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('pt073_02', 3)	# 1-3
    label(0)
    sprite('pt073_03', 3)	# 4-6
    sprite('pt073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('pt070_00', 2)	# 1-2
    sprite('pt070_01', 2)	# 3-4
    label(0)
    sprite('pt070_02', 3)	# 5-7
    sprite('pt070_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('pt070_04', 3)	# 1-3
    sprite('pt070_05', 3)	# 4-6
    GFX_0('StaggerSoul', -1)
    sprite('pt070_06', 2)	# 7-8
    sprite('pt070_07', 6)	# 9-14
    sprite('pt070_08', 6)	# 15-20
    sprite('pt070_09', 5)	# 21-25

@State
def CmnActUkemiStagger():

    def upon_IMMEDIATE():
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1
    sprite('pt070_10', 5)	# 1-5
    sprite('pt070_11', 2)	# 6-7
    sprite('pt070_12', 3)	# 8-10
    sprite('pt070_13', 3)	# 11-13

@State
def CmnActUkemiAirF():

    def upon_IMMEDIATE():
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1
    sprite('pt113_00', 3)	# 1-3
    sprite('pt113_01', 3)	# 4-6
    sprite('pt113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():

    def upon_IMMEDIATE():
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1
    sprite('pt113_00', 3)	# 1-3
    sprite('pt113_01', 3)	# 4-6
    sprite('pt113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():

    def upon_IMMEDIATE():
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1
    sprite('pt113_00', 3)	# 1-3
    sprite('pt113_01', 3)	# 4-6
    sprite('pt113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():

    def upon_IMMEDIATE():
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1
    sprite('pt110_00', 2)	# 1-2
    sprite('pt110_01', 2)	# 3-4
    sprite('pt110_02', 2)	# 5-6
    sprite('pt110_03', 2)	# 7-8
    sprite('pt110_04', 2)	# 9-10
    sprite('pt110_05', 2)	# 11-12
    sprite('pt110_06', 2)	# 13-14
    sprite('pt110_07', 2)	# 15-16
    sprite('pt110_08', 200)	# 17-216
    sprite('pt110_09', 6)	# 217-222

@State
def CmnActUkemiLandB():

    def upon_IMMEDIATE():
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1
    sprite('pt111_00', 3)	# 1-3
    sprite('pt111_01', 3)	# 4-6
    sprite('pt110_05', 3)	# 7-9
    sprite('pt110_04', 3)	# 10-12
    sprite('pt110_03', 3)	# 13-15
    sprite('pt110_02', 3)	# 16-18
    sprite('pt111_06', 3)	# 19-21
    sprite('pt111_07', 3)	# 22-24
    sprite('pt111_08', 200)	# 25-224
    sprite('pt111_09', 6)	# 225-230

@State
def CmnActUkemiLandN():

    def upon_IMMEDIATE():
        if random_(2, 0, 50):
            SLOT_7 = 0
        else:
            SLOT_7 = 1
    sprite('pt112_00', 2)	# 1-2
    sprite('pt112_01', 2)	# 3-4
    sprite('pt112_02', 2)	# 5-6
    sprite('pt112_03', 2)	# 7-8
    sprite('pt112_04', 2)	# 9-10
    sprite('pt112_05', 2)	# 11-12
    sprite('pt112_06', 2)	# 13-14
    sprite('pt112_07', 2)	# 15-16
    sprite('pt112_08', 2)	# 17-18

@State
def CmnActUkemiLandNLanding():
    sprite('pt024_00', 3)	# 1-3
    sprite('pt024_01', 3)	# 4-6
    sprite('pt024_02', 3)	# 7-9
    sprite('pt024_03', 3)	# 10-12
    sprite('pt024_04', 3)	# 13-15
    sprite('pt024_05', 3)	# 16-18

@State
def CmnActMidGuardPre():
    sprite('pt041_00', 3)	# 1-3
    sprite('pt041_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('pt040_00', 5)	# 1-5
    sprite('pt040_01', 5)	# 6-10
    sprite('pt040_02', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('pt041_01', 3)	# 1-3
    sprite('pt041_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('pt040_03', 3)	# 1-3
    label(0)
    sprite('pt040_01', 5)	# 4-8
    sprite('pt040_02', 5)	# 9-13
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('pt040_01', 3)	# 1-3
    sprite('pt040_00', 3)	# 4-6
    sprite('pt041_01', 3)	# 7-9
    sprite('pt041_00', 3)	# 10-12

@State
def CmnActHighGuardPre():
    sprite('pt041_00', 3)	# 1-3
    sprite('pt041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('pt041_02', 5)	# 1-5
    sprite('pt041_03', 5)	# 6-10
    sprite('pt041_04', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('pt041_01', 3)	# 1-3
    sprite('pt041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('pt041_05', 5)	# 1-5
    label(0)
    sprite('pt041_02', 5)	# 6-10
    sprite('pt041_03', 5)	# 11-15
    sprite('pt041_04', 5)	# 16-20
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('pt041_01', 3)	# 1-3
    sprite('pt041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('pt043_00', 3)	# 1-3
    sprite('pt043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('pt043_02', 3)	# 1-3
    sprite('pt043_03', 3)	# 4-6
    sprite('pt043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('pt043_01', 3)	# 1-3
    sprite('pt043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('pt043_05', 3)	# 1-3
    label(0)
    sprite('pt043_02', 3)	# 4-6
    sprite('pt043_03', 3)	# 7-9
    sprite('pt043_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('pt043_01', 3)	# 1-3
    sprite('pt043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('pt045_00', 3)	# 1-3
    sprite('pt045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('pt045_02', 3)	# 1-3
    sprite('pt045_03', 3)	# 4-6
    sprite('pt045_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('pt045_01', 3)	# 1-3
    sprite('pt045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('pt045_05', 3)	# 1-3
    label(0)
    sprite('pt045_02', 3)	# 4-6
    sprite('pt045_03', 3)	# 7-9
    sprite('pt045_04', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('pt045_01', 3)	# 1-3
    sprite('pt045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('pt090_00', 2)	# 1-2
    sprite('pt090_01', 2)	# 3-4
    sprite('pt090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('pt090_03', 6)	# 6-11
    sprite('pt090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('pt091_00', 2)	# 1-2
    sprite('pt091_01', 2)	# 3-4
    sprite('pt091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('pt091_03', 6)	# 6-11
    sprite('pt091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('pt092_00', 2)	# 1-2
    sprite('pt092_01', 2)	# 3-4
    sprite('pt092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('pt092_03', 6)	# 6-11
    sprite('pt092_04', 6)	# 12-17

@State
def CmnActCrossRushBegin():
    sprite('pt333_00', 3)	# 1-3
    sprite('pt333_01', 3)	# 4-6
    sprite('pt333_02', 3)	# 7-9
    sprite('pt333_03', 32767)	# 10-32776
    GFX_0('EMB_PT_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('pt333_04', 3)	# 1-3
    label(0)
    sprite('pt333_05', 3)	# 4-6
    sprite('pt333_06', 3)	# 7-9
    sprite('pt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('pt333_08', 4)	# 1-4
    sprite('pt333_09', 4)	# 5-8
    sprite('pt333_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('pt333_11', 3)	# 1-3
    sprite('pt333_12', 3)	# 4-6
    sprite('pt333_13', 3)	# 7-9
    sprite('pt333_14', 32767)	# 10-32776
    GFX_0('EMB_PT_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('pt333_15', 3)	# 1-3
    label(0)
    sprite('pt333_05', 3)	# 4-6
    sprite('pt333_06', 3)	# 7-9
    sprite('pt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('pt333_16', 2)	# 1-2
    sprite('pt333_17', 2)	# 3-4
    sprite('pt333_18', 2)	# 5-6
    sprite('pt020_05', 3)	# 7-9
    sprite('pt020_06', 3)	# 10-12
    label(0)
    sprite('pt020_07', 4)	# 13-16
    sprite('pt020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActAirTurn():
    sprite('pt025_00', 4)	# 1-4
    sprite('pt025_01', 4)	# 5-8
    sprite('pt025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('pt040_02', 1)	# 1-1
    sprite('pt040_01', 3)	# 2-4
    sprite('pt040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('pt312_00', 2)	# 1-2
    sprite('pt312_01', 4)	# 3-6
    sprite('pt312_02', 8)	# 7-14	 **attackbox here**
    sprite('pt312_03', 6)	# 15-20
    sprite('pt312_04', 5)	# 21-25
    sprite('pt312_05', 5)	# 26-30

@State
def CmnActAirLockWait():
    sprite('pt045_02', 1)	# 1-1
    sprite('pt045_01', 3)	# 2-4
    sprite('pt045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('pt000_00', 2)	# 1-2
    sprite('pt322_01', 2)	# 3-4
    sprite('pt322_02', 8)	# 5-12	 **attackbox here**
    sprite('pt322_03', 2)	# 13-14
    sprite('pt322_04', 3)	# 15-17
    sprite('pt322_05', 3)	# 18-20

@State
def CmnActLandSpin():
    sprite('pt071_00', 4)	# 1-4
    sprite('pt071_01', 4)	# 5-8
    label(0)
    sprite('pt071_02', 2)	# 9-10
    sprite('pt071_03', 2)	# 11-12
    sprite('pt071_04', 2)	# 13-14
    sprite('pt071_05', 2)	# 15-16
    sprite('pt071_06', 2)	# 17-18
    sprite('pt071_07', 2)	# 19-20
    sprite('pt071_08', 2)	# 21-22
    sprite('pt071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('pt071_10', 6)	# 1-6
    sprite('pt071_11', 5)	# 7-11
    sprite('pt071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('pt071_02', 2)	# 1-2
    sprite('pt071_03', 2)	# 3-4
    sprite('pt071_04', 2)	# 5-6
    sprite('pt071_05', 2)	# 7-8
    sprite('pt071_06', 2)	# 9-10
    sprite('pt071_07', 2)	# 11-12
    sprite('pt071_08', 2)	# 13-14
    sprite('pt071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('pt077_00', 2)	# 1-2
    sprite('pt077_01', 2)	# 3-4
    sprite('pt077_00ex00', 2)	# 5-6
    sprite('pt077_01ex00', 2)	# 7-8
    sprite('pt077_00ex01', 2)	# 9-10
    sprite('pt077_01ex01', 2)	# 11-12
    sprite('pt077_00ex02', 2)	# 13-14
    sprite('pt077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('pt077_02', 4)	# 1-4
    label(0)
    sprite('pt077_03', 3)	# 5-7
    sprite('pt077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('pt077_05', 5)	# 1-5

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('pt060_07', 3)	# 1-3
    sprite('pt060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('pt060_11', 4)	# 1-4
    sprite('pt060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('pt331_00', 2)	# 1-2
    sprite('pt331_01', 2)	# 3-4
    label(0)
    sprite('pt331_02', 3)	# 5-7
    sprite('pt331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('pt331_04', 2)	# 1-2
    sprite('pt331_05', 2)	# 3-4
    label(0)
    sprite('pt331_06', 3)	# 5-7
    sprite('pt331_07', 3)	# 8-10
    sprite('pt331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('pt331_09', 3)	# 1-3
    sprite('pt331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('pt331_11', 2)	# 1-2
    sprite('pt331_12', 2)	# 3-4
    label(0)
    sprite('pt331_02', 3)	# 5-7
    sprite('pt331_03', 2)	# 8-9
    sprite('pt331_04', 2)	# 10-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('pt331_05', 2)	# 1-2
    label(0)
    sprite('pt331_06', 2)	# 3-4
    sprite('pt331_07', 2)	# 5-6
    sprite('pt331_08', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('pt331_13', 4)	# 1-4
    sprite('pt331_14', 3)	# 5-7
    label(0)
    sprite('pt020_07', 4)	# 8-11
    sprite('pt020_08', 4)	# 12-15
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('pt333_00', 3)	# 1-3
    sprite('pt333_01', 3)	# 4-6
    sprite('pt333_02', 3)	# 7-9
    sprite('pt333_03', 32767)	# 10-32776
    GFX_0('EMB_PT_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('pt333_04', 3)	# 1-3
    label(0)
    sprite('pt333_05', 3)	# 4-6
    sprite('pt333_06', 3)	# 7-9
    sprite('pt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('pt333_08', 4)	# 1-4
    sprite('pt333_09', 4)	# 5-8
    sprite('pt333_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('pt333_11', 3)	# 1-3
    sprite('pt333_12', 3)	# 4-6
    sprite('pt333_13', 3)	# 7-9
    sprite('pt333_14', 32767)	# 10-32776
    GFX_0('EMB_PT_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('pt333_15', 3)	# 1-3
    label(0)
    sprite('pt333_05', 3)	# 4-6
    sprite('pt333_06', 3)	# 7-9
    sprite('pt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('pt333_16', 2)	# 1-2
    sprite('pt333_17', 2)	# 3-4
    sprite('pt333_18', 2)	# 5-6
    sprite('pt020_05', 3)	# 7-9
    sprite('pt020_06', 3)	# 10-12
    label(0)
    sprite('pt020_07', 4)	# 13-16
    sprite('pt020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('pt331_00', 2)	# 1-2
    sprite('pt331_01', 2)	# 3-4
    label(0)
    sprite('pt331_02', 3)	# 5-7
    sprite('pt331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('pt331_04', 2)	# 1-2
    sprite('pt331_05', 2)	# 3-4
    label(0)
    sprite('pt331_06', 3)	# 5-7
    sprite('pt331_07', 3)	# 8-10
    sprite('pt331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('pt331_09', 3)	# 1-3
    sprite('pt331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('pt331_11', 2)	# 1-2
    sprite('pt331_12', 2)	# 3-4
    label(0)
    sprite('pt331_02', 3)	# 5-7
    sprite('pt331_03', 2)	# 8-9
    sprite('pt331_04', 2)	# 10-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('pt331_05', 2)	# 1-2
    label(0)
    sprite('pt331_06', 2)	# 3-4
    sprite('pt331_07', 2)	# 5-6
    sprite('pt331_08', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('pt331_13', 3)	# 1-3
    sprite('pt331_14', 3)	# 4-6
    sprite('pt020_07', 3)	# 7-9
    sprite('pt020_08', 3)	# 10-12
    label(0)
    sprite('pt020_07', 4)	# 13-16
    sprite('pt020_08', 4)	# 17-20
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

        def upon_41():
            clearUponHandler(41)
            sendToLabel(200)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(200)
    sprite('null', 28)	# 603-630
    sprite('null', 1)	# 631-631
    Unknown1086(22)
    teleportRelativeX(-10000)
    teleportRelativeY(2400000)
    physicsYImpulse(-480000)
    setGravity(0)
    Unknown2053(1)
    EnableCollision(1)
    if SLOT_5:
        sendToLabel(100)
    else:
        sendToLabelUpon(2, 5)
        sendToLabel(1)
    label(1)
    sprite('pt255_04', 3)	# 632-634	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_05', 3)	# 635-637	 **attackbox here**
    sprite('pt255_06', 3)	# 638-640	 **attackbox here**
    sprite('pt255_07', 3)	# 641-643	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_08', 3)	# 644-646	 **attackbox here**
    sprite('pt255_09', 3)	# 647-649	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(5)
    sprite('pt255_10', 3)	# 650-652	 **attackbox here**
    clearUponHandler(2)
    Unknown2006()
    Unknown1084(1)
    SFX_3('ptse_02')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_airhammerDwave', -1)
    sprite('pt255_11', 4)	# 653-656	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    sprite('pt255_12', 5)	# 657-661
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    Recovery()
    sprite('pt255_13', 4)	# 662-665
    sprite('pt255_14', 4)	# 666-669
    sprite('pt255_15', 5)	# 670-674
    ExitState()
    label(100)
    sprite('keep', 1)	# 675-675
    sendToLabelUpon(2, 105)
    label(101)
    sprite('pt255_18', 3)	# 676-678	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_19', 3)	# 679-681	 **attackbox here**
    sprite('pt255_20', 3)	# 682-684	 **attackbox here**
    sprite('pt255_21', 3)	# 685-687	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_22', 3)	# 688-690	 **attackbox here**
    sprite('pt255_17', 3)	# 691-693	 **attackbox here**
    loopRest()
    gotoLabel(101)
    label(105)
    sprite('pt255_23', 3)	# 694-696	 **attackbox here**
    clearUponHandler(2)
    Unknown2006()
    Unknown1084(1)
    SFX_0('100_hit_grap_2')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_hammerDshock', 0)
    sprite('pt255_24', 4)	# 697-700	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    GFX_1('ptef_204dellight00', 3)
    sprite('pt255_12', 4)	# 701-704
    sprite('pt255_13', 4)	# 705-708
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    GFX_1('ptef_204dellight', 3)
    GFX_1('ptef_204dellight', 4)
    sprite('pt255_14', 4)	# 709-712
    sprite('pt255_15', 5)	# 713-717
    loopRest()

@State
def CmnActChangePartnerQuickIn():
    sprite('pt032_08', 3)	# 1-3
    sprite('pt032_09', 5)	# 4-8
    sprite('pt032_09', 7)	# 9-15
    sprite('pt032_10', 7)	# 16-22
    sprite('pt032_11', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('pt033_02ex01', 3)	# 1-3
    sprite('pt033_03ex01', 3)	# 4-6
    sprite('pt033_02ex01', 3)	# 7-9
    sprite('pt033_03ex01', 3)	# 10-12
    sprite('pt033_02ex01', 3)	# 13-15
    sprite('pt033_03ex01', 3)	# 16-18
    sprite('pt033_02ex01', 3)	# 19-21
    sprite('pt033_03ex01', 3)	# 22-24
    sprite('pt033_02ex01', 3)	# 25-27
    sprite('pt033_03ex01', 3)	# 28-30
    sprite('pt033_02ex01', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('pt033_00ex01', 1)	# 1-1
    sprite('pt033_01ex01', 2)	# 2-3
    sprite('pt033_02ex01', 2)	# 4-5
    sprite('pt033_02ex01', 1)	# 6-6
    sprite('pt033_03ex01', 3)	# 7-9
    loopRest()
    label(0)
    sprite('pt033_02ex01', 3)	# 10-12
    sprite('pt033_03ex01', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt033_04ex01', 2)	# 16-17
    sprite('pt033_05ex01', 2)	# 18-19
    sprite('pt033_06ex01', 2)	# 20-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('pt300_00', 4)	# 1-4
    sprite('pt300_01', 4)	# 5-8
    sprite('pt300_02', 4)	# 9-12
    sprite('pt300_03', 6)	# 13-18
    sprite('pt300_04', 6)	# 19-24
    sprite('pt300_05', 7)	# 25-31
    sprite('pt300_06', 20)	# 32-51
    sprite('pt300_07', 7)	# 52-58
    SFX_3('ptse_00')
    sprite('pt300_08', 9)	# 59-67
    sprite('pt300_09', 6)	# 68-73
    sprite('pt000_00', 30)	# 74-103

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
    sprite('pt020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('pt020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('pt010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
        Unknown2006()
        if SLOT_5:
            SLOT_58 = 1
    sprite('keep', 1)	# 1-1
    callSubroutine('WeaponCreate_Assist_Far')
    if (SLOT_59 == 10):
        sendToLabel(5)
    if (SLOT_59 == 16):
        sendToLabel(8)
    label(0)
    sprite('pt208_00', 3)	# 2-4
    Unknown1084(1)
    sprite('pt208_01', 3)	# 5-7
    sprite('pt208_02', 3)	# 8-10
    sprite('pt208_03', 3)	# 11-13
    sprite('pt208_04', 3)	# 14-16
    sprite('pt208_02', 3)	# 17-19
    sprite('pt208_05', 3)	# 20-22
    sprite('pt208_06', 1)	# 23-23
    physicsXImpulse(-20000)
    GFX_1('ptef_drivethrow', 1)
    callSubroutine('WeaponThrow_Assist_Far')
    sprite('pt208_06', 9)	# 24-32
    Unknown1019(70)
    sprite('pt208_06', 5)	# 33-37
    Unknown1019(30)
    sprite('pt208_07', 3)	# 38-40
    sprite('pt208_08', 3)	# 41-43
    Recovery()
    callSubroutine('StuffColorReset')
    Unknown1019(0)
    sprite('pt208_09', 3)	# 44-46
    sprite('pt208_10', 3)	# 47-49
    ExitState()
    label(5)
    sprite('pt208_00', 2)	# 50-51
    Unknown1084(1)
    sprite('keep', 1)	# 52-52
    if SLOT_58:
        sendToLabel(15)
    sprite('pt405_00', 3)	# 53-55
    sprite('pt405_01', 3)	# 56-58
    sprite('pt405_02', 3)	# 59-61
    sprite('pt405_03', 3)	# 62-64
    sprite('pt405_04', 3)	# 65-67
    if (not SLOT_7):
        Unknown7006('bpt317_0', 100, 863268962, 811546673, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt317_1', 100, 863268962, 828323889, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt405_05', 3)	# 68-70
    GFX_0('Bomb_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1401, 0)
    GFX_1('ptef_throwsmokeshort', 0)
    sprite('pt405_05', 3)	# 71-73
    GFX_0('Bomb_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1402, 0)
    GFX_1('ptef_throwsmokeshort', 1)
    sprite('pt405_05', 4)	# 74-77
    GFX_0('Bomb_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1403, 0)
    GFX_1('ptef_throwsmokeshort', 2)
    sprite('pt405_06', 3)	# 78-80
    sprite('pt208_08', 3)	# 81-83
    sprite('pt208_09', 3)	# 84-86
    sprite('pt208_10', 3)	# 87-89
    ExitState()
    label(15)
    sprite('pt405_00', 3)	# 90-92
    sprite('pt405_01', 3)	# 93-95
    sprite('pt405_02', 3)	# 96-98
    sprite('pt405_03', 3)	# 99-101
    sprite('pt405_04', 2)	# 102-103
    if (not SLOT_7):
        Unknown7006('bpt319_0', 100, 863268962, 811544626, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt319_1', 100, 863268962, 828321842, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt405_04', 1)	# 104-104
    GFX_1('ptef_throwsmoke', 2)
    SFX_0('016_explode_0')
    SFX_3('ptse_01')
    sprite('pt405_05', 3)	# 105-107
    GFX_0('SpBomb_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1401, 0)
    sprite('pt405_05', 3)	# 108-110
    GFX_0('SpBomb_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1402, 0)
    sprite('pt405_05', 4)	# 111-114
    GFX_0('SpBomb_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1403, 0)
    sprite('pt405_06', 3)	# 115-117
    sprite('pt208_08', 3)	# 118-120
    sprite('pt208_09', 3)	# 121-123
    sprite('pt208_10', 3)	# 124-126
    ExitState()
    label(8)
    sprite('pt409_00', 3)	# 127-129
    Unknown1084(1)
    sprite('pt409_01', 2)	# 130-131
    GFX_0('ptef_409_ring', -1)
    sprite('keep', 1)	# 132-132
    if SLOT_58:
        sendToLabel(18)
    sprite('pt409_02', 5)	# 133-137
    sprite('pt409_03', 5)	# 138-142
    sprite('pt409_04', 2)	# 143-144
    if (not SLOT_7):
        Unknown7006('bpt329_0', 100, 863268962, 811544627, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt329_1', 100, 863268962, 828321843, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown2015(175)
    sprite('pt409_05', 2)	# 145-146
    Unknown2015(200)
    SFX_0('009_swing_rapier_2')
    sprite('pt409_06', 3)	# 147-149
    GFX_1('ptef409_feather', 1)
    Unknown21007(7, 32)
    GFX_0('BoomerangAtk', 0)
    Unknown38(7, 1)
    sprite('pt409_07', 3)	# 150-152
    sprite('pt409_08', 3)	# 153-155
    Unknown2015(175)
    WhiffCancelEnable(1)
    sprite('pt409_09', 3)	# 156-158
    Unknown2015(-1)
    sprite('pt409_10ex01', 4)	# 159-162
    Recovery()
    callSubroutine('StuffColorReset')
    sprite('pt409_11', 3)	# 163-165
    sprite('pt409_12', 3)	# 166-168
    ExitState()
    label(18)
    sprite('pt409_02', 5)	# 169-173
    sprite('pt409_03', 5)	# 174-178
    sprite('pt409_04', 2)	# 179-180
    if (not SLOT_7):
        Unknown7006('bpt331_0', 100, 863268962, 811545139, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt331_1', 100, 863268962, 828322355, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt409_05', 2)	# 181-182
    SFX_0('009_swing_rapier_2')
    sprite('pt409_06', 3)	# 183-185
    GFX_1('ptef409_feather', 1)
    Unknown21007(7, 32)
    GFX_0('SPBoomerangAtk', 0)
    Unknown38(7, 1)
    sprite('pt409_07', 3)	# 186-188
    sprite('pt409_08', 3)	# 189-191
    Unknown2015(175)
    WhiffCancelEnable(1)
    sprite('pt409_09', 3)	# 192-194
    Unknown2015(-1)
    sprite('pt409_10ex01', 4)	# 195-198
    Recovery()
    callSubroutine('StuffColorReset')
    sprite('pt409_11', 3)	# 199-201
    sprite('pt409_12', 3)	# 202-204
    ExitState()

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackP1(70)
        Unknown11042(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
        Unknown2006()
        if SLOT_5:
            SLOT_58 = 1
        SLOT_55 = 0

        def upon_78():
            SLOT_55 = 1
    sprite('pt032_02', 3)	# 1-3
    physicsXImpulse(18000)
    sprite('pt032_03', 3)	# 4-6
    Unknown8006(100, 1, 1)
    sprite('pt203_02', 3)	# 7-9
    if (not SLOT_7):
        SFX_1('bpt333_0')
    else:
        SFX_1('bpt333_1')
    GFX_0('pt203_mahojin', -1)
    GFX_0('pt203_mahojinsub', -1)
    GFX_0('pt203_aura1', -1)
    GFX_0('pt203_aura2', -1)
    GFX_0('pt203_aura3', -1)
    sprite('pt203_02', 3)	# 10-12
    sprite('pt203_03ex02', 4)	# 13-16	 **attackbox here**
    AttackLevel_(4)
    Damage(1200)
    AttackP1(70)
    AttackP2(80)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(6000)
    AirPushbackY(40000)
    AirUntechableTime(60)
    Unknown11042(1)
    GFX_0('pt203_stick', 0)
    physicsXImpulse(0)
    sprite('pt203_04', 2)	# 17-18
    callSubroutine('WeaponCreate_Assist_Near')
    SFX_3('ptse_13')
    sprite('pt203_05', 5)	# 19-23
    sprite('pt203_06', 2)	# 24-25
    sprite('pt203_07', 2)	# 26-27
    sprite('pt203_08', 2)	# 28-29
    sprite('pt203_09', 2)	# 30-31
    sprite('pt203_10', 2)	# 32-33
    sprite('pt203_11', 1)	# 34-34
    sprite('keep', 1)	# 35-35
    callSubroutine('Weapon_Assist_Near')
    label(1)
    sprite('pt023_00', 1)	# 36-36
    Unknown2006()
    sprite('pt023_01', 1)	# 37-37
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('pt020_00', 2)	# 38-39
    physicsXImpulse(21000)
    physicsYImpulse(48300)
    Unknown1047(45925)
    Unknown1043()

    def upon_CLEAR_OR_EXIT():
        if (SLOT_19 <= 250000):
            clearUponHandler(3)
            Unknown1019(25)
    sprite('pt020_01', 2)	# 40-41
    sprite('pt020_01', 2)	# 42-43
    sprite('pt020_02', 1)	# 44-44
    sprite('pt255_00', 3)	# 45-47
    if SLOT_58:
        sendToLabel(11)
    sprite('pt255_01', 1)	# 48-48
    AttackLevel_(5)
    Damage(1000)
    AttackP2(90)
    Unknown11092(1)
    PushbackX(0)
    AirPushbackX(-1000)
    AirPushbackY(-30000)
    AirUntechableTime(30)
    Unknown9310(20)
    HitOverhead(0)
    Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
    clearUponHandler(2)
    clearUponHandler(3)
    sendToLabelUpon(2, 102)
    Unknown1019(0)
    Unknown1051(10)
    physicsYImpulse(1000)
    setGravity(10)
    sprite('pt255_02', 2)	# 49-50
    sprite('pt255_03', 2)	# 51-52
    if (not SLOT_7):
        SFX_1('bpt302_0')
    else:
        SFX_1('bpt302_1')
    Unknown1084(1)
    Unknown1019(10)
    sprite('pt255_04', 3)	# 53-55	 **attackbox here**
    setGravity(2000)
    RefreshMultihit()
    label(101)
    sprite('pt255_05', 3)	# 56-58	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_06', 3)	# 59-61	 **attackbox here**
    sprite('pt255_07', 3)	# 62-64	 **attackbox here**
    sprite('pt255_08', 3)	# 65-67	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_09', 3)	# 68-70	 **attackbox here**
    sprite('pt255_04', 3)	# 71-73	 **attackbox here**
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('pt255_10', 4)	# 74-77	 **attackbox here**
    Unknown2006()
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    PushbackX(39900)
    Unknown9071()
    ScreenShake(0, 7500)
    Unknown1084(1)
    SFX_3('ptse_02')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_airhammerDwave', -1)
    sprite('pt255_11', 9)	# 78-86	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    sprite('pt255_12', 4)	# 87-90
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    Recovery()
    callSubroutine('StuffColorReset')
    sprite('pt255_13', 4)	# 91-94
    sprite('pt255_14', 4)	# 95-98
    sprite('pt255_15', 5)	# 99-103
    ExitState()
    label(11)
    sprite('pt255_01', 1)	# 104-104
    AttackLevel_(5)
    Damage(1200)
    AttackP2(90)
    Unknown11092(1)
    PushbackX(4000)
    AirPushbackX(-1000)
    AirPushbackY(-60000)
    AirUntechableTime(30)
    Unknown9310(1)
    HitOverhead(0)
    clearUponHandler(2)
    clearUponHandler(3)

    def upon_11():
        SLOT_53 = 1
    sendToLabelUpon(2, 112)
    Unknown1019(0)
    Unknown1051(10)
    physicsYImpulse(1000)
    setGravity(10)
    sprite('pt255_02', 2)	# 105-106
    sprite('pt255_16', 2)	# 107-108
    if (not SLOT_7):
        SFX_1('bpt304_0')
    else:
        SFX_1('bpt304_1')
    Unknown1084(1)
    Unknown1019(25)
    sprite('pt255_17', 3)	# 109-111	 **attackbox here**
    RefreshMultihit()
    setGravity(2000)
    label(111)
    sprite('pt255_18', 3)	# 112-114	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_19', 3)	# 115-117	 **attackbox here**
    sprite('pt255_20', 3)	# 118-120	 **attackbox here**
    sprite('pt255_21', 3)	# 121-123	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_22', 3)	# 124-126	 **attackbox here**
    sprite('pt255_17', 3)	# 127-129	 **attackbox here**
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('pt255_23', 4)	# 130-133	 **attackbox here**
    Unknown2006()
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    PushbackX(39900)
    Unknown9071()
    Unknown1084(1)
    SFX_0('100_hit_grap_2')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_hammerDshock', 0)
    ScreenShake(0, 50000)
    sprite('pt255_24', 9)	# 134-142	 **attackbox here**
    if (not SLOT_53):
        GFX_0('Atk5DHiquake_Assist', -1)
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    GFX_1('ptef_204dellight00', 3)
    Recovery()
    sprite('pt255_12', 4)	# 143-146
    sprite('pt255_13', 4)	# 147-150
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    GFX_1('ptef_204dellight', 3)
    GFX_1('ptef_204dellight', 4)
    sprite('pt255_14', 4)	# 151-154
    sprite('pt255_15', 5)	# 155-159
    ExitState()
    label(2)
    sprite('pt204_00', 1)	# 160-160
    Unknown2006()
    sprite('pt204_01', 1)	# 161-161
    sprite('pt204_02', 1)	# 162-162
    if SLOT_58:
        sendToLabel(12)
    sprite('pt206_00', 3)	# 163-165	 **attackbox here**
    AttackLevel_(4)
    Damage(1500)
    AttackP2(85)
    Unknown9310(0)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(12000)
    AirPushbackY(-55000)
    AirUntechableTime(70)
    Unknown9190(1)
    Unknown9118(50)
    Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
    sprite('pt206_01', 60)	# 166-225
    if SLOT_55:

        def upon_CLEAR_OR_EXIT():
            if (SLOT_20 < 340000):
                clearUponHandler(3)
                sendToLabel(21)
    else:
        sendToLabel(21)
    label(21)
    sprite('pt206_01', 1)	# 226-226
    clearUponHandler(3)
    physicsXImpulse(35000)
    sprite('pt206_02', 1)	# 227-227
    if (not SLOT_7):
        SFX_1('bpt305_0')
    else:
        SFX_1('bpt305_1')
    sprite('pt206_03', 8)	# 228-235	 **attackbox here**
    Unknown1084(1)
    GFX_1('ptef_hammerDwave02', 0)
    SFX_0('005_swing_grap_2_2')
    SFX_3('ptse_24')
    RefreshMultihit()
    sprite('pt206_04', 5)	# 236-240	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_206dellight00', 1)
    GFX_1('ptef_206dellight00', 2)
    GFX_1('ptef_lightrod00', 2)
    GFX_1('ptef_lightrod00', 3)
    GFX_1('ptef_206dellight00', 4)
    Recovery()
    sprite('pt206_05', 3)	# 241-243	 **attackbox here**
    GFX_1('ptef_206dellight', 0)
    GFX_1('ptef_206dellight', 1)
    GFX_1('ptef_206dellight', 2)
    callSubroutine('StuffColorReset')
    sprite('pt206_05ex00', 2)	# 244-245	 **attackbox here**
    sprite('pt204_09', 5)	# 246-250
    sprite('pt204_10', 5)	# 251-255
    sprite('pt204_11', 5)	# 256-260
    sprite('pt204_12', 5)	# 261-265
    sprite('pt204_13', 5)	# 266-270
    ExitState()
    label(12)
    sprite('pt206_06', 3)	# 271-273	 **attackbox here**
    AttackLevel_(4)
    Damage(2550)
    AttackP2(85)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(16000)
    AirPushbackY(-65000)
    AirUntechableTime(80)
    Unknown9190(1)
    Unknown9118(50)
    Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
    sprite('pt206_07', 60)	# 274-333
    if SLOT_55:

        def upon_CLEAR_OR_EXIT():
            if (SLOT_20 < 340000):
                clearUponHandler(3)
                sendToLabel(22)
    else:
        sendToLabel(22)
    label(22)
    sprite('pt206_07', 1)	# 334-334
    clearUponHandler(3)
    physicsXImpulse(35000)
    sprite('pt206_08', 1)	# 335-335
    if (not SLOT_7):
        SFX_1('bpt307_0')
    else:
        SFX_1('bpt307_1')
    sprite('pt206_09', 8)	# 336-343	 **attackbox here**
    Unknown1084(1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('ptse_07')
    RefreshMultihit()
    sprite('pt206_10', 5)	# 344-348	 **attackbox here**
    GFX_1('ptef_206dellight00', 0)
    GFX_1('ptef_206dellight00', 1)
    GFX_1('ptef_206dellight00', 3)
    GFX_1('ptef_206dellight00', 5)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 4)
    GFX_1('ptef_lightrod00', 5)
    Recovery()
    sprite('pt206_11', 3)	# 349-351	 **attackbox here**
    GFX_1('ptef_206dellight', 0)
    GFX_1('ptef_206dellight', 1)
    GFX_1('ptef_206dellight', 2)
    GFX_1('ptef_206dellight', 3)
    GFX_1('ptef_206dellight', 4)
    GFX_1('ptef_206dellight', 5)
    callSubroutine('StuffColorReset')
    sprite('pt206_11', 3)	# 352-354	 **attackbox here**
    sprite('pt204_09', 5)	# 355-359
    sprite('pt204_10', 5)	# 360-364
    sprite('pt204_11', 5)	# 365-369
    sprite('pt204_12', 5)	# 370-374
    sprite('pt204_13', 5)	# 375-379
    ExitState()
    label(3)

    def upon_CLEAR_OR_EXIT():
        (SLOT_19 < 250000)
        if op(5, 2, 0, 2, 52):
            clearUponHandler(3)
            sendToLabel(14)
    sprite('pt404_00', 2)	# 380-381
    Unknown2006()
    physicsXImpulse(-8000)
    sprite('pt404_00', 3)	# 382-384
    physicsXImpulse(0)
    sprite('pt404_01', 2)	# 385-386
    sprite('pt404_02', 2)	# 387-388
    Unknown8006(100, 1, 1)
    physicsXImpulse(34000)
    SFX_0('000_airdash_0')
    SFX_3('ptse_23')
    sprite('pt404_03', 2)	# 389-390
    SLOT_52 = 1
    sprite('pt404_04', 2)	# 391-392
    sprite('pt404_02', 2)	# 393-394
    sprite('pt404_03', 2)	# 395-396
    sprite('pt404_04', 2)	# 397-398
    sprite('pt404_02', 2)	# 399-400
    sprite('pt404_03', 2)	# 401-402
    sprite('pt404_04', 2)	# 403-404
    sprite('pt404_02', 2)	# 405-406
    sprite('pt404_03', 2)	# 407-408
    sprite('pt404_04', 2)	# 409-410
    label(14)
    sprite('pt205_00', 2)	# 411-412
    clearUponHandler(3)
    Unknown1084(1)
    Unknown1047(9000)
    sprite('keep', 1)	# 413-413
    if SLOT_58:
        sendToLabel(13)
    sprite('pt205_01', 2)	# 414-415
    AttackLevel_(4)
    Damage(1500)
    AttackP2(85)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(10)
    AirPushbackX(4000)
    AirPushbackY(36000)
    Unknown9130(50)
    Unknown9142(50)
    hitstun(30)
    AirUntechableTime(60)
    Hitstop(15)
    PushbackX(30400)
    Unknown11050('06000000707465665f6869745f66726970616e0000000000000000000000000000000000')
    RefreshMultihit()
    sprite('pt207_00', 2)	# 416-417
    sprite('pt207_01', 2)	# 418-419	 **attackbox here**
    if (not SLOT_7):
        SFX_1('bpt309_0')
    else:
        SFX_1('bpt309_1')
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_2')
    sprite('pt207_02', 2)	# 420-421	 **attackbox here**
    sprite('pt207_03', 2)	# 422-423	 **attackbox here**
    GFX_1('ptef_207dellight00', 0)
    GFX_1('ptef_207dellight00', 1)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    sprite('pt207_04', 5)	# 424-428
    GFX_1('ptef_207dellight', 0)
    GFX_1('ptef_207dellight', 1)
    Recovery()
    sprite('pt205_07ex01', 6)	# 429-434	 **attackbox here**
    callSubroutine('StuffColorReset')
    sprite('pt205_08', 7)	# 435-441
    sprite('pt205_09', 6)	# 442-447
    sprite('pt205_10', 6)	# 448-453
    ExitState()
    label(13)
    sprite('pt205_01', 2)	# 454-455
    AttackLevel_(4)
    Damage(2550)
    AttackP2(85)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(10)
    AirPushbackX(4000)
    AirPushbackY(36000)
    Unknown9130(50)
    Unknown9142(50)
    hitstun(40)
    AirUntechableTime(60)
    Hitstop(20)
    Unknown11050('02000000707465665f6869745f6861726973656e00000000000000000000000000000000')
    RefreshMultihit()
    sprite('pt207_05', 2)	# 456-457
    sprite('pt207_06', 2)	# 458-459	 **attackbox here**
    if (not SLOT_7):
        SFX_1('bpt311_0')
    else:
        SFX_1('bpt311_1')
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_2')
    sprite('pt207_07', 2)	# 460-461	 **attackbox here**
    sprite('pt207_08', 2)	# 462-463	 **attackbox here**
    GFX_1('ptef_207dellight00', 1)
    GFX_1('ptef_207dellight00', 2)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt207_09', 5)	# 464-468
    GFX_1('ptef_207dellight', 0)
    GFX_1('ptef_207dellight', 1)
    Recovery()
    sprite('pt205_07ex01', 6)	# 469-474	 **attackbox here**
    callSubroutine('StuffColorReset')
    sprite('pt205_08', 7)	# 475-481
    sprite('pt205_09', 6)	# 482-487
    sprite('pt205_10', 6)	# 488-493
    ExitState()
    label(4)
    sprite('pt023_00', 2)	# 494-495
    sprite('pt023_01', 2)	# 496-497
    sprite('pt020_00', 1)	# 498-498
    physicsXImpulse(21000)
    physicsYImpulse(32200)
    Unknown1043()
    sprite('pt256_00', 1)	# 499-499
    clearUponHandler(2)
    sendToLabelUpon(2, 145)
    sprite('keep', 1)	# 500-500
    if SLOT_58:
        sendToLabel(14)
    sprite('pt256_01', 1)	# 501-501
    AttackLevel_(3)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(52000)
    AirPushbackY(32000)
    AirUntechableTime(60)
    Hitstop(22)
    Unknown9178(1)
    AirHitstunAfterWallbounce(60)
    Unknown11050('06000000707465665f6869745f6261740000000000000000000000000000000000000000')
    Unknown1084(1)
    sprite('pt256_01', 3)	# 502-504
    physicsYImpulse(16000)
    physicsXImpulse(8000)
    setGravity(1850)
    sprite('pt256_02', 3)	# 505-507
    if (not SLOT_7):
        SFX_1('bpt314_0')
    else:
        SFX_1('bpt314_1')
    sprite('pt256_03', 1)	# 508-508	 **attackbox here**
    callSubroutine('ItemConsume')
    SFX_0('005_swing_grap_2_2')
    sprite('pt256_03', 2)	# 509-510	 **attackbox here**
    sprite('pt256_04', 1)	# 511-511	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt256_04', 4)	# 512-515	 **attackbox here**
    sprite('pt256_05', 2)	# 516-517
    Unknown1043()
    sprite('pt256_06', 4)	# 518-521
    GFX_1('ptef_205dellight', 0)
    GFX_1('ptef_205dellight', 1)
    GFX_1('ptef_205dellight', 2)
    sprite('pt256_07', 3)	# 522-524
    sprite('pt256_08', 3)	# 525-527
    sprite('pt256_09', 4)	# 528-531
    sprite('pt256_10', 3)	# 532-534
    sprite('pt256_11', 3)	# 535-537
    sendToLabel(140)
    label(14)
    sprite('pt256_01', 1)	# 538-538
    AttackLevel_(4)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(65000)
    AirPushbackY(42000)
    Hitstop(26)
    AirUntechableTime(30)
    Unknown9178(1)
    AirHitstunAfterWallbounce(60)
    Unknown11050('06000000707465665f6869745f6b616e61626f7500000000000000000000000000000000')
    Unknown1084(1)
    sprite('pt256_01', 3)	# 539-541
    physicsYImpulse(16000)
    physicsXImpulse(2000)
    setGravity(1850)
    sprite('pt256_12', 3)	# 542-544
    if (not SLOT_7):
        SFX_1('bpt316_0')
    else:
        SFX_1('bpt316_1')
    sprite('pt256_13', 1)	# 545-545	 **attackbox here**
    callSubroutine('ItemConsume')
    SFX_0('005_swing_grap_2_2')
    sprite('pt256_13', 4)	# 546-549	 **attackbox here**
    sprite('pt256_14', 5)	# 550-554	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt256_15', 1)	# 555-555
    Unknown1043()
    sprite('pt256_16', 4)	# 556-559
    GFX_1('ptef_205dellight00', 0)
    GFX_1('ptef_205dellight00', 1)
    GFX_1('ptef_205dellight00', 2)
    sprite('pt256_07', 3)	# 560-562
    sprite('pt256_08', 3)	# 563-565
    sprite('pt256_09', 4)	# 566-569
    sprite('pt256_10', 3)	# 570-572
    sprite('pt256_11', 3)	# 573-575
    label(140)
    sprite('pt020_05', 3)	# 576-578
    sprite('pt020_06', 3)	# 579-581
    label(141)
    sprite('pt020_07', 4)	# 582-585
    sprite('pt020_08', 4)	# 586-589
    loopRest()
    gotoLabel(141)
    label(145)
    sprite('pt024_00', 2)	# 590-591
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('pt024_01', 4)	# 592-595
    sprite('pt024_02', 3)	# 596-598

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(-47000)
        AirPushbackX(6000)
        Unknown9190(1)
        Unknown9118(60)
        AirUntechableTime(60)
        YImpluseBeforeWallbounce(0)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        Unknown11054(170000)
        sendToLabelUpon(2, 1)
        DisableAttackRestOfMove()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(1)
        Unknown2006()
        Unknown11042(1)
    sprite('pt000_00', 3)	# 1-3
    sprite('pt403_07ex', 3)	# 4-6
    SLOT_67 = SLOT_19
    if (SLOT_67 > 600000):
        SLOT_67 = 600000
    SLOT_12 = SLOT_67
    Unknown1019(8)
    physicsYImpulse(19000)
    setGravity(3300)
    if (not SLOT_7):
        SFX_1('bpt206_0')
    else:
        SFX_1('bpt206_1')
    sprite('pt403_08ex', 2)	# 7-8
    sprite('pt403_09ex', 2)	# 9-10
    sprite('pt403_10ex', 2)	# 11-12
    sprite('pt403_17ex', 2)	# 13-14
    sprite('pt403_18ex', 2)	# 15-16
    sprite('pt403_19ex', 1)	# 17-17
    sprite('pt403_20ex', 32767)	# 18-32784	 **attackbox here**
    SFX_3('ptse_08')
    RefreshMultihit()
    label(1)
    sprite('pt403_21ex', 2)	# 32785-32786	 **attackbox here**
    clearUponHandler(2)
    clearUponHandler(10)
    Unknown1017()
    Unknown1084(1)
    Unknown8000(104, 1, 1)
    sprite('pt403_20ex', 2)	# 32787-32788	 **attackbox here**
    sprite('pt403_21ex', 2)	# 32789-32790	 **attackbox here**
    Unknown1018()
    Unknown28(2, 'CmnActJumpLanding')
    physicsXImpulse(-3000)
    physicsYImpulse(30000)
    setGravity(3700)
    sprite('pt403_22ex', 7)	# 32791-32797
    Recovery()
    sprite('pt403_29ex', 3)	# 32798-32800
    sprite('pt403_30ex', 3)	# 32801-32803
    sprite('pt403_06ex', 3)	# 32804-32806
    sprite('pt403_07ex', 32767)	# 32807-65573
    clearUponHandler(2)
    sendToLabelUpon(2, 10)
    label(10)
    sprite('pt024_00', 3)	# 65574-65576
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('pt024_01', 3)	# 65577-65579
    sprite('pt024_02', 3)	# 65580-65582

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
    Unknown2036(106, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('pt020_07', 4)	# 3-6
    sprite('pt020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateAssaultDDDOD')
    else:
        enterState('UltimateAssaultDDD')

@State
def UltimateAssaultDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(4)
        Damage(164)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        MinimumDamagePct(100)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(-6000)
        AirPushbackY(18000)
        AirUntechableTime(100)
        hitstun(100)
        Unknown1084(1)
        setInvincible(1)

        def upon_78():
            if SLOT_51:
                clearUponHandler(78)
                Damage(153)
            SLOT_51 = 1
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('pt431_00', 3)	# 2-4
    sprite('pt431_00', 3)	# 5-7
    sprite('pt431_01', 3)	# 8-10
    sprite('pt431_02', 3)	# 11-13
    sprite('pt431_03', 3)	# 14-16
    sprite('pt431_04', 3)	# 17-19
    GFX_0('pt431_aura3', -1)
    GFX_0('pt431_aura3', -1)
    sprite('pt431_05', 40)	# 20-59
    GFX_0('pt431_startcircle', 0)
    GFX_0('ptef_431aura', 0)
    GFX_0('pt431_floorcircle', -1)
    sprite('pt431_05', 10)	# 60-69
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    sprite('pt431_06', 3)	# 70-72
    GFX_0('pt431_tornado', -1)
    sprite('pt431_07', 3)	# 73-75

    def upon_16():
        if (not SLOT_38):
            if (SLOT_40 >= 10000):
                Unknown1015(500)
            if (SLOT_40 < (-10000)):
                Unknown1015(-500)
            Unknown1019(95)
            YAccel(95)
        else:
            if (SLOT_40 >= 10000):
                Unknown1015(-500)
            if (SLOT_40 < (-10000)):
                Unknown1015(500)
            Unknown1019(95)
            YAccel(95)
        if SLOT_51:
            setGravity(700)
    sprite('pt431_08', 3)	# 76-78
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_09', 3)	# 79-81
    sprite('pt431_10', 1)	# 82-82	 **attackbox here**
    sprite('pt431_10', 3)	# 83-85	 **attackbox here**
    setInvincible(0)
    sprite('pt431_11', 3)	# 86-88
    sprite('pt431_12', 3)	# 89-91
    sprite('pt431_13', 3)	# 92-94
    sprite('pt431_09', 3)	# 95-97
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_10', 4)	# 98-101	 **attackbox here**
    RefreshMultihit()
    sprite('pt431_11', 3)	# 102-104
    sprite('pt431_12', 3)	# 105-107
    sprite('pt431_13', 3)	# 108-110
    AirPushbackX(-5000)
    AirPushbackY(8000)
    Unknown30056('a08601003200000000000000')
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 111-113	 **attackbox here**
    SLOT_51 = 1
    GFX_0('pt431_ranbucircle', -1)
    GFX_0('pt431_tornado', -1)
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    GFX_0('pt431_smoke', -1)
    if (not SLOT_7):
        SFX_1('bpt252_0')
    else:
        SFX_1('bpt252_1')
    sprite('pt431_15', 3)	# 114-116	 **attackbox here**
    sprite('pt431_16', 3)	# 117-119	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 120-122	 **attackbox here**
    sprite('pt431_15', 3)	# 123-125	 **attackbox here**
    sprite('pt431_16', 3)	# 126-128	 **attackbox here**
    Hitstop(0)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 129-131	 **attackbox here**
    sprite('pt431_15', 3)	# 132-134	 **attackbox here**
    sprite('pt431_16', 3)	# 135-137	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 138-140	 **attackbox here**
    sprite('pt431_15', 3)	# 141-143	 **attackbox here**
    sprite('pt431_16', 3)	# 144-146	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 147-149	 **attackbox here**
    sprite('pt431_15', 3)	# 150-152	 **attackbox here**
    sprite('pt431_16', 3)	# 153-155	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 156-158	 **attackbox here**
    sprite('pt431_15', 3)	# 159-161	 **attackbox here**
    sprite('pt431_16', 3)	# 162-164	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 165-167	 **attackbox here**
    sprite('pt431_15', 3)	# 168-170	 **attackbox here**
    sprite('pt431_16', 3)	# 171-173	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 174-176	 **attackbox here**
    sprite('pt431_15', 3)	# 177-179	 **attackbox here**
    sprite('pt431_16', 3)	# 180-182	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 183-185	 **attackbox here**
    sprite('pt431_15', 3)	# 186-188	 **attackbox here**
    sprite('pt431_16', 3)	# 189-191	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 192-194	 **attackbox here**
    sprite('pt431_15', 3)	# 195-197	 **attackbox here**
    sprite('pt431_16', 3)	# 198-200	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 201-203	 **attackbox here**
    sprite('pt431_15', 3)	# 204-206	 **attackbox here**
    sprite('pt431_16', 3)	# 207-209	 **attackbox here**

    def upon_12():
        Unknown2038(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(30000)
    AirPushbackY(24000)
    YImpluseBeforeWallbounce(1000)
    AirUntechableTime(150)
    Unknown9310(36)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_16', 2)	# 210-211	 **attackbox here**
    label(5)
    sprite('pt431_14', 3)	# 212-214	 **attackbox here**
    setGravity(1200)
    DisableAttackRestOfMove()
    clearUponHandler(16)

    def upon_CLEAR_OR_EXIT():
        if SLOT_37:
            sendToLabel(10)
    sprite('pt431_15', 3)	# 215-217	 **attackbox here**
    sprite('pt431_16', 3)	# 218-220	 **attackbox here**
    gotoLabel(5)
    label(10)
    sprite('pt431_17', 5)	# 221-225
    clearUponHandler(3)
    sprite('pt431_18', 5)	# 226-230

    def upon_16():
        Unknown1019(90)
    sprite('pt431_19', 5)	# 231-235
    sprite('pt431_20', 5)	# 236-240
    sprite('pt431_21', 5)	# 241-245
    sprite('pt431_22', 5)	# 246-250
    loopRest()
    Unknown1084(1)
    if SLOT_2:
        gotoLabel(0)
    sprite('pt431_31', 7)	# 251-257
    sprite('pt431_32', 7)	# 258-264
    ExitState()
    label(0)
    sprite('pt431_23', 6)	# 265-270
    if (not SLOT_7):
        SFX_1('bpt253_0')
    else:
        SFX_1('bpt253_1')
    GFX_0('pt203_mahojin', -1)
    GFX_0('pt203_mahojinsub', -1)
    GFX_0('pt203_aura1', -1)
    GFX_0('pt203_aura2', -1)
    GFX_0('pt203_aura3', -1)
    sprite('pt431_24', 6)	# 271-276
    sprite('pt431_25', 6)	# 277-282
    sprite('pt431_26', 6)	# 283-288
    sprite('pt431_27', 8)	# 289-296
    GFX_0('pt203_stick', 0)
    SFX_3('ptse_13')
    sprite('pt431_27', 8)	# 297-304
    sprite('pt431_27', 8)	# 305-312
    sprite('pt431_27', 8)	# 313-320
    sprite('pt431_28', 6)	# 321-326
    sprite('pt431_29', 6)	# 327-332
    sprite('pt431_30', 6)	# 333-338
    ExitState()

@State
def UltimateAssaultDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(4)
        Damage(167)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        MinimumDamagePct(100)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(-6000)
        AirPushbackY(18000)
        AirUntechableTime(100)
        hitstun(100)
        Unknown1084(1)
        setInvincible(1)

        def upon_78():
            SLOT_51 = 1
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('pt431_00', 3)	# 2-4
    sprite('pt431_00', 3)	# 5-7
    sprite('pt431_01', 3)	# 8-10
    sprite('pt431_02', 3)	# 11-13
    sprite('pt431_03', 3)	# 14-16
    sprite('pt431_04', 3)	# 17-19
    GFX_0('pt431_aura3', -1)
    GFX_0('pt431_aura3', -1)
    sprite('pt431_05', 40)	# 20-59
    GFX_0('pt431_startcircle', 0)
    GFX_0('ptef_431aura', 0)
    GFX_0('pt431_floorcircle', -1)
    sprite('pt431_05', 10)	# 60-69
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    sprite('pt431_06', 3)	# 70-72
    GFX_0('pt431_tornado', -1)
    sprite('pt431_07', 3)	# 73-75

    def upon_16():
        if (not SLOT_38):
            if (SLOT_40 >= 10000):
                Unknown1015(1500)
            if (SLOT_40 < (-10000)):
                Unknown1015(-1500)
            Unknown1019(90)
            YAccel(90)
        else:
            if (SLOT_40 >= 10000):
                Unknown1015(-1500)
            if (SLOT_40 < (-10000)):
                Unknown1015(1500)
            Unknown1019(90)
            YAccel(90)
        if SLOT_51:
            setGravity(700)
    sprite('pt431_08', 3)	# 76-78
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_09', 3)	# 79-81
    sprite('pt431_10', 1)	# 82-82	 **attackbox here**
    sprite('pt431_10', 3)	# 83-85	 **attackbox here**
    setInvincible(0)
    sprite('pt431_11', 3)	# 86-88
    sprite('pt431_12', 3)	# 89-91
    sprite('pt431_13', 3)	# 92-94
    sprite('pt431_09', 3)	# 95-97
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_10', 4)	# 98-101	 **attackbox here**
    RefreshMultihit()
    sprite('pt431_11', 3)	# 102-104
    sprite('pt431_12', 3)	# 105-107
    sprite('pt431_13', 3)	# 108-110
    AirPushbackX(-5000)
    AirPushbackY(8000)
    Unknown30056('a08601003200000000000000')
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 111-113	 **attackbox here**
    SLOT_51 = 1
    GFX_0('pt431_ranbucircle', -1)
    GFX_0('pt431_tornado', -1)
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    GFX_0('pt431_smoke', -1)
    if (not SLOT_7):
        SFX_1('bpt252_0')
    else:
        SFX_1('bpt252_1')
    sprite('pt431_15', 3)	# 114-116	 **attackbox here**
    sprite('pt431_16', 3)	# 117-119	 **attackbox here**
    Damage(166)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 120-121	 **attackbox here**
    sprite('pt431_15', 2)	# 122-123	 **attackbox here**
    sprite('pt431_16', 2)	# 124-125	 **attackbox here**
    Damage(100)
    Hitstop(0)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 126-127	 **attackbox here**
    sprite('pt431_15', 2)	# 128-129	 **attackbox here**
    sprite('pt431_16', 2)	# 130-131	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 132-133	 **attackbox here**
    sprite('pt431_15', 2)	# 134-135	 **attackbox here**
    sprite('pt431_16', 2)	# 136-137	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 138-139	 **attackbox here**
    sprite('pt431_15', 2)	# 140-141	 **attackbox here**
    sprite('pt431_16', 2)	# 142-143	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 144-145	 **attackbox here**
    sprite('pt431_15', 2)	# 146-147	 **attackbox here**
    sprite('pt431_16', 2)	# 148-149	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 150-151	 **attackbox here**
    sprite('pt431_15', 2)	# 152-153	 **attackbox here**
    sprite('pt431_16', 2)	# 154-155	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 156-157	 **attackbox here**
    sprite('pt431_15', 2)	# 158-159	 **attackbox here**
    sprite('pt431_16', 2)	# 160-161	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 162-163	 **attackbox here**
    sprite('pt431_15', 2)	# 164-165	 **attackbox here**
    sprite('pt431_16', 2)	# 166-167	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 168-169	 **attackbox here**
    sprite('pt431_15', 2)	# 170-171	 **attackbox here**
    sprite('pt431_16', 2)	# 172-173	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 174-175	 **attackbox here**
    sprite('pt431_15', 2)	# 176-177	 **attackbox here**
    sprite('pt431_16', 2)	# 178-179	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 180-181	 **attackbox here**
    sprite('pt431_15', 2)	# 182-183	 **attackbox here**
    sprite('pt431_16', 2)	# 184-185	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 186-187	 **attackbox here**
    sprite('pt431_15', 2)	# 188-189	 **attackbox here**
    sprite('pt431_16', 2)	# 190-191	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 192-193	 **attackbox here**
    sprite('pt431_15', 2)	# 194-195	 **attackbox here**
    sprite('pt431_16', 2)	# 196-197	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 198-199	 **attackbox here**
    sprite('pt431_15', 2)	# 200-201	 **attackbox here**
    sprite('pt431_16', 2)	# 202-203	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 204-205	 **attackbox here**
    sprite('pt431_15', 2)	# 206-207	 **attackbox here**
    sprite('pt431_16', 2)	# 208-209	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 210-211	 **attackbox here**
    sprite('pt431_15', 2)	# 212-213	 **attackbox here**
    sprite('pt431_16', 2)	# 214-215	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 216-217	 **attackbox here**
    sprite('pt431_15', 2)	# 218-219	 **attackbox here**
    sprite('pt431_16', 2)	# 220-221	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 222-223	 **attackbox here**
    sprite('pt431_15', 2)	# 224-225	 **attackbox here**
    sprite('pt431_16', 2)	# 226-227	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 228-229	 **attackbox here**
    sprite('pt431_15', 2)	# 230-231	 **attackbox here**
    sprite('pt431_16', 2)	# 232-233	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 234-235	 **attackbox here**
    sprite('pt431_15', 2)	# 236-237	 **attackbox here**
    sprite('pt431_16', 2)	# 238-239	 **attackbox here**

    def upon_12():
        Unknown2038(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(30000)
    AirPushbackY(24000)
    YImpluseBeforeWallbounce(1000)
    AirUntechableTime(150)
    Unknown9310(36)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_16', 2)	# 240-241	 **attackbox here**
    label(5)
    sprite('pt431_14', 3)	# 242-244	 **attackbox here**
    setGravity(1200)
    DisableAttackRestOfMove()
    clearUponHandler(16)

    def upon_CLEAR_OR_EXIT():
        if SLOT_37:
            sendToLabel(10)
    sprite('pt431_15', 3)	# 245-247	 **attackbox here**
    sprite('pt431_16', 3)	# 248-250	 **attackbox here**
    gotoLabel(5)
    label(10)
    sprite('pt431_17', 5)	# 251-255
    clearUponHandler(3)
    sprite('pt431_18', 5)	# 256-260

    def upon_16():
        Unknown1019(90)
    sprite('pt431_19', 5)	# 261-265
    sprite('pt431_20', 5)	# 266-270
    sprite('pt431_21', 5)	# 271-275
    sprite('pt431_22', 5)	# 276-280
    loopRest()
    Unknown1084(1)
    if SLOT_2:
        gotoLabel(0)
    sprite('pt431_31', 7)	# 281-287
    sprite('pt431_32', 7)	# 288-294
    ExitState()
    label(0)
    sprite('pt431_23', 6)	# 295-300
    if (not SLOT_7):
        SFX_1('bpt253_0')
    else:
        SFX_1('bpt253_1')
    GFX_0('pt203_mahojin', -1)
    GFX_0('pt203_mahojinsub', -1)
    GFX_0('pt203_aura1', -1)
    GFX_0('pt203_aura2', -1)
    GFX_0('pt203_aura3', -1)
    sprite('pt431_24', 6)	# 301-306
    sprite('pt431_25', 6)	# 307-312
    sprite('pt431_26', 6)	# 313-318
    sprite('pt431_27', 8)	# 319-326
    GFX_0('pt203_stick', 0)
    SFX_3('ptse_13')
    sprite('pt431_27', 8)	# 327-334
    sprite('pt431_27', 8)	# 335-342
    sprite('pt431_27', 8)	# 343-350
    sprite('pt431_28', 6)	# 351-356
    sprite('pt431_29', 6)	# 357-362
    sprite('pt431_30', 6)	# 363-368
    ExitState()

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('pt406_00', 3)	# 1-3
    sprite('pt406_01', 3)	# 4-6
    sprite('pt406_02', 3)	# 7-9
    sprite('pt406_03', 8)	# 10-17	 **attackbox here**
    SFX_3('ptse_00')
    sprite('pt406_04', 8)	# 18-25	 **attackbox here**
    sprite('pt406_05', 8)	# 26-33	 **attackbox here**
    sprite('pt406_06', 8)	# 34-41	 **attackbox here**
    sprite('pt406_03', 8)	# 42-49	 **attackbox here**
    SFX_3('ptse_00')
    sprite('pt406_07', 5)	# 50-54
    sprite('pt406_08', 5)	# 55-59
    sprite('pt406_09', 5)	# 60-64
    sprite('pt406_10', 5)	# 65-69
    sprite('pt406_11', 5)	# 70-74
    sprite('pt406_12', 5)	# 75-79

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 1)	# 121-121
    Unknown1086(22)
    teleportRelativeX(-1000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    if SLOT_5:
        sendToLabel(100)
    else:
        sendToLabelUpon(2, 5)
        sendToLabel(1)
    label(1)
    sprite('pt255_04', 3)	# 122-124	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_05', 3)	# 125-127	 **attackbox here**
    sprite('pt255_06', 3)	# 128-130	 **attackbox here**
    sprite('pt255_07', 3)	# 131-133	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_08', 3)	# 134-136	 **attackbox here**
    sprite('pt255_09', 3)	# 137-139	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(5)
    sprite('pt255_10', 5)	# 140-144	 **attackbox here**
    clearUponHandler(2)
    Unknown2006()
    Unknown1084(1)
    SFX_3('ptse_02')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_airhammerDwave', -1)
    sprite('pt255_11', 5)	# 145-149	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    sprite('pt255_12', 6)	# 150-155
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    sprite('pt255_13', 5)	# 156-160
    sprite('pt255_14', 5)	# 161-165
    sprite('pt255_15', 5)	# 166-170
    ExitState()
    label(100)
    sprite('keep', 1)	# 171-171
    sendToLabelUpon(2, 105)
    label(101)
    sprite('pt255_18', 3)	# 172-174	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_19', 3)	# 175-177	 **attackbox here**
    sprite('pt255_20', 3)	# 178-180	 **attackbox here**
    sprite('pt255_21', 3)	# 181-183	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_22', 3)	# 184-186	 **attackbox here**
    sprite('pt255_17', 3)	# 187-189	 **attackbox here**
    loopRest()
    gotoLabel(101)
    label(105)
    sprite('pt255_23', 5)	# 190-194	 **attackbox here**
    clearUponHandler(2)
    Unknown2006()
    Unknown1084(1)
    SFX_0('100_hit_grap_2')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_hammerDshock', 0)
    sprite('pt255_24', 5)	# 195-199	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    GFX_1('ptef_204dellight00', 3)
    sprite('pt255_12', 6)	# 200-205
    sprite('pt255_13', 5)	# 206-210
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    GFX_1('ptef_204dellight', 3)
    GFX_1('ptef_204dellight', 4)
    sprite('pt255_14', 4)	# 211-214
    sprite('pt255_15', 5)	# 215-219
    loopRest()

@State
def CmnActChangeReturnAppealBurst():
    sprite('pt070_00', 5)	# 1-5
    sprite('pt070_01', 5)	# 6-10
    label(0)
    sprite('pt070_02', 10)	# 11-20
    sprite('pt070_03', 20)	# 21-40
    gotoLabel(0)

@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_64 = 0
        if SLOT_5:
            SLOT_64 = 1

            def upon_LANDING():
                clearUponHandler(2)
                sendToLabel(101)
        else:

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
    if SLOT_5:
        sendToLabel(100)
    label(0)
    sprite('pt255_04', 3)	# 32-34	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_05', 3)	# 35-37	 **attackbox here**
    sprite('pt255_06', 3)	# 38-40	 **attackbox here**
    sprite('pt255_07', 3)	# 41-43	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_08', 3)	# 44-46	 **attackbox here**
    sprite('pt255_09', 3)	# 47-49	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt255_10', 1)	# 50-50	 **attackbox here**
    sprite('pt255_11', 7)	# 51-57	 **attackbox here**
    StartMultihit()
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown1084(1)
    SFX_3('ptse_02')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_airhammerDwave', -1)
    sprite('pt255_13', 7)	# 58-64
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    GFX_1('ptef_204dellight', 3)
    GFX_1('ptef_204dellight', 4)
    sprite('pt255_14', 8)	# 65-72
    sprite('pt255_15', 8)	# 73-80
    ExitState()
    label(100)
    sprite('pt255_18', 3)	# 81-83	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_19', 3)	# 84-86	 **attackbox here**
    sprite('pt255_20', 3)	# 87-89	 **attackbox here**
    sprite('pt255_21', 3)	# 90-92	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_22', 3)	# 93-95	 **attackbox here**
    sprite('pt255_17', 3)	# 96-98	 **attackbox here**
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('pt255_23', 1)	# 99-99	 **attackbox here**
    sprite('pt255_24', 7)	# 100-106	 **attackbox here**
    StartMultihit()
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown1084(1)
    SFX_0('100_hit_grap_2')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_hammerDshock', 0)
    sprite('pt255_13', 7)	# 107-113
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    GFX_1('ptef_204dellight', 3)
    GFX_1('ptef_204dellight', 4)
    sprite('pt255_14', 8)	# 114-121
    sprite('pt255_15', 8)	# 122-129

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('pt255_11', 6)	# 2-7	 **attackbox here**
    Unknown23183('70743235355f3233000000000000000000000000000000000000000000000000060000000200000040000000')
    StartMultihit()
    sprite('pt255_12', 2)	# 8-9
    sprite('pt255_13', 2)	# 10-11
    sprite('pt255_14', 2)	# 12-13
    sprite('pt255_15', 2)	# 14-15
    sprite('pt404_17', 10)	# 16-25
    sprite('pt404_18', 5)	# 26-30
    Unknown7009(2)
    sprite('pt404_19', 4)	# 31-34
    sprite('pt404_20', 3)	# 35-37	 **attackbox here**
    GFX_1('ptef_404kiss', 1)
    SFX_3('ptse_15')
    SFX_0('016_explode_2')
    GFX_1('ptef_bomber_heart', 0)
    sprite('pt404_21', 3)	# 38-40
    DisableAttackRestOfMove()
    sprite('pt404_22', 3)	# 41-43
    sprite('pt404_22', 3)	# 44-46
    sprite('pt404_23', 3)	# 47-49	 **attackbox here**
    sprite('pt404_23', 3)	# 50-52	 **attackbox here**
    sprite('pt404_24', 3)	# 53-55
    sprite('pt404_25', 3)	# 56-58
    sprite('pt404_26', 5)	# 59-63
    GFX_0('CommandThrowRod', 0)
    sprite('pt404_27', 4)	# 64-67
    sprite('pt404_28', 4)	# 68-71
    sprite('pt404_29', 4)	# 72-75
    SLOT_64 = 0

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Unknown11050('06000000707465665f6869745f6c6f770000000000000000000000000000000000000000')
        WhiffCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('pt200_00', 2)	# 1-2
    random_(2, 0, 34)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    sprite('pt200_01', 1)	# 3-3
    sprite('pt200_01', 2)	# 4-5
    SFX_0('003_swing_grap_0_0')
    sprite('pt200_02ex01', 2)	# 6-7	 **attackbox here**
    Unknown7009(0)
    sprite('pt200_03ex01', 3)	# 8-10
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    gotoLabel(2)
    label(0)
    sprite('pt200_01', 1)	# 11-11
    sprite('pt200_01', 2)	# 12-13
    SFX_0('003_swing_grap_0_0')
    sprite('pt200_02', 2)	# 14-15	 **attackbox here**
    Unknown7009(0)
    sprite('pt200_03', 3)	# 16-18
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    gotoLabel(2)
    label(1)
    sprite('pt200_01', 1)	# 19-19
    sprite('pt200_01', 2)	# 20-21
    SFX_0('003_swing_grap_0_0')
    Unknown42('pt')
    sprite('pt200_02ex00', 2)	# 22-23	 **attackbox here**
    Unknown7009(0)
    sprite('pt200_03ex00', 3)	# 24-26
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    gotoLabel(2)
    label(2)
    sprite('pt200_04', 4)	# 27-30
    sprite('pt200_05', 4)	# 31-34
    WhiffCancelEnable(0)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(14000)
        AirHitstunAnimation(10)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        Unknown2004(1, 0)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
    sprite('pt201_00', 3)	# 1-3
    sprite('pt201_01', 4)	# 4-7
    sprite('pt201_02', 2)	# 8-9
    physicsXImpulse(8000)
    sprite('pt201_03', 1)	# 10-10
    SFX_0('008_swing_pole_2')
    sprite('pt201_04', 4)	# 11-14	 **attackbox here**
    Unknown7009(1)
    sprite('pt201_05', 2)	# 15-16	 **attackbox here**
    Unknown1019(20)
    sprite('pt201_06', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('pt201_07', 3)	# 20-22
    physicsXImpulse(0)
    sprite('pt201_08', 3)	# 23-25
    sprite('pt201_09', 2)	# 26-27
    Unknown8000(100, 1, 1)
    sprite('pt201_10', 2)	# 28-29
    sprite('pt201_11', 2)	# 30-31

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(-60000)
        AirUntechableTime(60)
        PushbackX(19800)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        SLOT_4 = 1
        SLOT_59 = 3
    sprite('pt204_00', 1)	# 1-1
    sprite('pt204_01', 1)	# 2-2
    sprite('pt204_02', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt206_00', 3)	# 4-6	 **attackbox here**
    AttackP2(75)
    Unknown9310(1)
    sprite('pt206_01', 3)	# 7-9
    sprite('pt206_02', 1)	# 10-10
    if (not SLOT_7):
        SFX_4('bpt305_0')
    else:
        SFX_4('bpt305_1')
    sprite('pt206_03ex01', 8)	# 11-18	 **attackbox here**
    GFX_1('ptef_hammerDwave02', 0)
    SFX_0('005_swing_grap_2_2')
    SFX_3('ptse_24')
    sprite('pt206_04', 3)	# 19-21	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_206dellight00', 1)
    GFX_1('ptef_206dellight00', 2)
    GFX_1('ptef_lightrod00', 2)
    GFX_1('ptef_lightrod00', 3)
    GFX_1('ptef_206dellight00', 4)
    Recovery()
    Unknown2063()
    sprite('pt206_05', 3)	# 22-24	 **attackbox here**
    GFX_1('ptef_206dellight', 0)
    GFX_1('ptef_206dellight', 1)
    GFX_1('ptef_206dellight', 2)
    sprite('pt206_05ex00', 2)	# 25-26	 **attackbox here**
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('pt206_06', 3)	# 27-29	 **attackbox here**
    Damage(2040)
    AttackP2(85)
    Unknown9190(1)
    Unknown9118(45)
    Unknown23159('SpCat')
    sprite('pt206_07', 3)	# 30-32
    sprite('pt206_08', 1)	# 33-33
    if (not SLOT_7):
        SFX_4('bpt307_0')
    else:
        SFX_4('bpt307_1')
    sprite('pt206_09ex01', 8)	# 34-41	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    SFX_3('ptse_07')
    sprite('pt206_10', 3)	# 42-44	 **attackbox here**
    GFX_1('ptef_206dellight00', 0)
    GFX_1('ptef_206dellight00', 1)
    GFX_1('ptef_206dellight00', 3)
    GFX_1('ptef_206dellight00', 5)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 4)
    GFX_1('ptef_lightrod00', 5)
    Recovery()
    Unknown2063()
    sprite('pt206_11', 3)	# 45-47	 **attackbox here**
    GFX_1('ptef_206dellight', 0)
    GFX_1('ptef_206dellight', 1)
    GFX_1('ptef_206dellight', 2)
    GFX_1('ptef_206dellight', 3)
    GFX_1('ptef_206dellight', 4)
    GFX_1('ptef_206dellight', 5)
    sprite('pt206_11', 2)	# 48-49	 **attackbox here**
    label(9)
    sprite('pt204_09', 2)	# 50-51
    callSubroutine('StuffColorReset')
    sprite('pt204_10', 2)	# 52-53
    sprite('pt204_11', 2)	# 54-55
    sprite('pt204_12', 2)	# 56-57
    sprite('pt204_13', 2)	# 58-59

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(-19000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        AirUntechableTime(60)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        Unknown11054(170000)
        sendToLabelUpon(2, 1)
        DisableAttackRestOfMove()
        HitOrBlockCancel('NmlAtk5AAAA')
    sprite('pt403_07ex', 1)	# 1-1
    SLOT_67 = SLOT_19
    if (SLOT_67 > 750000):
        SLOT_67 = 750000
    SLOT_12 = SLOT_67
    Unknown1019(8)
    physicsYImpulse(19000)
    setGravity(4400)
    if (not SLOT_7):
        SFX_4('bpt206_0')
    else:
        SFX_4('bpt206_1')
    sprite('pt403_08ex', 2)	# 2-3
    sprite('pt403_09ex', 2)	# 4-5
    sprite('pt403_10ex', 2)	# 6-7
    sprite('pt403_17ex', 2)	# 8-9
    sprite('pt403_18ex', 32767)	# 10-32776
    label(1)
    sprite('pt403_19ex', 1)	# 32777-32777
    Unknown1017()
    Unknown1084(1)
    Unknown8000(104, 1, 1)
    sprite('pt403_20ex', 2)	# 32778-32779	 **attackbox here**
    SFX_3('ptse_08')
    RefreshMultihit()
    sprite('pt403_21ex', 2)	# 32780-32781	 **attackbox here**
    sprite('pt403_20ex', 2)	# 32782-32783	 **attackbox here**
    sprite('pt403_21ex', 2)	# 32784-32785	 **attackbox here**
    Unknown1018()
    Unknown28(2, 'CmnActJumpLanding')
    physicsXImpulse(-3000)
    physicsYImpulse(30000)
    setGravity(3700)
    Unknown14077(0)
    sprite('pt403_22ex', 7)	# 32786-32792
    Recovery()
    Unknown2063()
    sprite('pt403_29ex', 3)	# 32793-32795
    sprite('pt403_30ex', 3)	# 32796-32798
    sprite('pt403_06ex', 3)	# 32799-32801
    sprite('pt403_07ex', 32767)	# 32802-65568

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        JumpCancel_(0)
        Unknown2004(1, 0)
        Unknown11044(1)
    sprite('pt407_00', 2)	# 1-2
    sprite('pt407_01', 3)	# 3-5
    sprite('pt407_02', 3)	# 6-8	 **attackbox here**
    if (not SLOT_7):
        Unknown7006('bpt106_0', 100, 829714530, 811546672, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt106_1', 100, 829714530, 828323888, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt407_03', 3)	# 9-11	 **attackbox here**
    sprite('pt407_04', 3)	# 12-14	 **attackbox here**
    sprite('pt407_05', 3)	# 15-17	 **attackbox here**
    sprite('pt407_06', 4)	# 18-21	 **attackbox here**
    SFX_3('ptse_08')
    SFX_3('ptse_02')
    Unknown4048(90000)
    Unknown4045('707465665f67756172646372757368707463000000000000000000000000000000000000')
    Unknown30088(1)
    sprite('pt407_07', 6)	# 22-27	 **attackbox here**
    physicsXImpulse(-5000)
    Recovery()
    Unknown2063()
    sprite('pt407_08', 6)	# 28-33	 **attackbox here**
    Unknown1019(70)
    sprite('pt407_09', 6)	# 34-39	 **attackbox here**
    Unknown1019(40)
    sprite('pt407_10', 6)	# 40-45
    physicsXImpulse(0)
    sprite('pt407_11', 3)	# 46-48
    sprite('pt407_12', 3)	# 49-51

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirHitstunAnimation(10)
        AirPushbackY(22000)
        AirUntechableTime(24)
        PushbackX(12000)
        AirPushbackY(15000)
        Unknown11050('06000000707465665f6869745f6c6f770000000000000000000000000000000000000000')
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
    sprite('pt210_00', 3)	# 1-3
    sprite('pt210_01', 2)	# 4-5
    sprite('pt210_01', 3)	# 6-8
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('pt210_02', 3)	# 9-11
    sprite('pt210_03', 4)	# 12-15	 **attackbox here**
    Unknown7009(0)
    SFX_0('009_swing_rapier_0')
    sprite('pt210_04', 3)	# 16-18
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('pt210_05', 3)	# 19-21
    sprite('pt210_06', 3)	# 22-24
    sprite('pt210_07', 3)	# 25-27
    sprite('pt210_08', 3)	# 28-30
    sprite('pt210_09', 3)	# 31-33
    sprite('pt210_10', 2)	# 34-35
    sprite('pt210_11', 2)	# 36-37

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown11050('06000000707465665f6869745f6869676800000000000000000000000000000000000000')
        AirUntechableTime(20)
        PushbackX(12000)
        AirPushbackY(15000)
        HitOrBlockCancel('NmlAtk5BBB')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
    sprite('pt202_00', 2)	# 1-2
    sprite('pt202_01', 3)	# 3-5
    sprite('pt202_03', 3)	# 6-8
    SFX_0('003_swing_grap_0_1')
    sprite('pt202_04', 6)	# 9-14	 **attackbox here**
    Unknown7009(2)
    sprite('pt202_05', 4)	# 15-18
    SFX_0('014_electric_m')
    Recovery()
    Unknown2063()
    sprite('pt202_06', 4)	# 19-22
    sprite('pt202_07', 4)	# 23-26
    sprite('pt202_08', 1)	# 27-27
    sprite('pt202_09', 2)	# 28-29
    sprite('pt202_10', 4)	# 30-33

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(4000)
        HitJumpCancel(1)
        SLOT_4 = 1
        SLOT_59 = 5
    sprite('pt205_00', 2)	# 1-2
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt205_01', 3)	# 4-6
    AttackLevel_(4)
    AttackP2(75)
    AirUntechableTime(40)
    Hitstop(15)
    Unknown11050('06000000707465665f6869745f66726970616e0000000000000000000000000000000000')
    sprite('pt207_00', 3)	# 7-9
    sprite('pt207_01', 2)	# 10-11	 **attackbox here**
    if (not SLOT_7):
        SFX_4('bpt309_0')
    else:
        SFX_4('bpt309_1')
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_2')
    sprite('pt207_02', 2)	# 12-13	 **attackbox here**
    sprite('pt207_03', 2)	# 14-15	 **attackbox here**
    GFX_1('ptef_207dellight00', 0)
    GFX_1('ptef_207dellight00', 1)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    sprite('pt207_04', 5)	# 16-20
    GFX_1('ptef_207dellight', 0)
    GFX_1('ptef_207dellight', 1)
    Recovery()
    Unknown2063()
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('pt205_01', 3)	# 21-23
    AttackLevel_(4)
    Damage(2040)
    AttackP2(85)
    AirUntechableTime(40)
    Hitstop(15)
    Unknown11050('06000000707465665f6869745f66726970616e0000000000000000000000000000000000')
    Unknown11050('02000000707465665f6869745f6861726973656e00000000000000000000000000000000')
    Unknown23159('SpHarisen')
    sprite('pt207_05', 3)	# 24-26
    sprite('pt207_06', 2)	# 27-28	 **attackbox here**
    if (not SLOT_7):
        SFX_4('bpt311_0')
    else:
        SFX_4('bpt311_1')
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_2')
    sprite('pt207_07', 2)	# 29-30	 **attackbox here**
    sprite('pt207_08', 2)	# 31-32	 **attackbox here**
    GFX_1('ptef_207dellight00', 1)
    GFX_1('ptef_207dellight00', 2)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt207_09', 5)	# 33-37
    GFX_1('ptef_207dellight', 0)
    GFX_1('ptef_207dellight', 1)
    Recovery()
    Unknown2063()
    label(9)
    sprite('pt205_07', 5)	# 38-42	 **attackbox here**
    sprite('pt205_08', 4)	# 43-46
    sprite('pt205_09', 3)	# 47-49
    sprite('pt205_10', 3)	# 50-52

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        AttackP1(90)
        HitLow(2)
        Unknown11050('06000000707465665f6869745f6c6f770000000000000000000000000000000000000000')
        HitAirUnblockable(0)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('pt230_00', 3)	# 1-3
    Unknown1051(60)
    sprite('pt230_01', 2)	# 4-5
    sprite('pt230_02', 3)	# 6-8	 **attackbox here**
    SFX_0('007_swing_knife_0')
    Unknown7009(0)
    sprite('pt230_03', 3)	# 9-11
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('pt230_04', 4)	# 12-15
    sprite('pt230_05', 3)	# 16-18

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('pt231_00', 2)	# 1-2
    sprite('pt231_01', 4)	# 3-6
    sprite('pt231_02', 2)	# 7-8
    sprite('pt231_03', 1)	# 9-9
    Unknown7009(1)
    SFX_0('008_swing_pole_2')
    sprite('pt231_04', 3)	# 10-12	 **attackbox here**
    sprite('pt231_05', 5)	# 13-17
    Recovery()
    Unknown2063()
    sprite('pt231_06', 6)	# 18-23
    sprite('pt231_07', 5)	# 24-28
    sprite('pt231_08', 5)	# 29-33

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        HitLow(2)
        AirPushbackX(3000)
        AirPushbackY(17000)
        AirUntechableTime(30)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('pt234_00', 3)	# 1-3
    sprite('pt234_01', 4)	# 4-7
    sprite('pt234_02', 2)	# 8-9
    Unknown12046(50)
    sprite('pt234_03', 2)	# 10-11
    SFX_0('009_swing_rapier_2')
    if (not SLOT_7):
        SFX_4('bpt107_0')
    else:
        SFX_4('bpt107_1')
    Unknown12046(100)
    sprite('pt234_04', 3)	# 12-14	 **attackbox here**
    Unknown12046(200)
    sprite('pt234_05', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('pt234_06', 2)	# 18-19
    Unknown12046(100)
    sprite('pt234_07', 2)	# 20-21
    Unknown12046(50)
    sprite('pt234_08', 3)	# 22-24
    Unknown12046(0)
    sprite('pt234_09', 3)	# 25-27
    sprite('pt234_10', 3)	# 28-30
    sprite('pt234_11', 3)	# 31-33
    sprite('pt234_12', 3)	# 34-36
    sprite('pt234_13', 2)	# 37-38

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Unknown11050('06000000707465665f6869745f6869676800000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('pt252_00', 1)	# 1-1
    sprite('pt252_01', 2)	# 2-3
    sprite('pt252_02', 3)	# 4-6
    sprite('pt252_03', 2)	# 7-8
    sprite('pt252_04', 3)	# 9-11
    Unknown7009(2)
    sprite('pt252_05', 3)	# 12-14	 **attackbox here**
    SFX_0('008_swing_pole_2')
    sprite('pt252_06', 1)	# 15-15	 **attackbox here**
    sprite('pt252_06', 2)	# 16-17	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('pt252_07', 4)	# 18-21
    sprite('pt252_08', 4)	# 22-25
    sprite('pt252_09', 3)	# 26-28

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        AirPushbackY(20000)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('pt251_00', 1)	# 1-1
    sprite('pt251_01', 2)	# 2-3
    sprite('pt251_02', 2)	# 4-5
    sprite('pt251_03', 2)	# 6-7
    Unknown7009(1)
    SFX_0('019_cloth_a')
    SFX_0('019_cloth_a')
    sprite('pt251_04', 3)	# 8-10	 **attackbox here**
    sprite('pt251_05', 3)	# 11-13	 **attackbox here**
    sprite('pt251_06', 3)	# 14-16
    Recovery()
    Unknown2063()
    sprite('pt251_07', 3)	# 17-19
    sprite('pt251_08', 3)	# 20-22

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(600)
        Unknown11092(1)
        Hitstop(4)
        AirPushbackY(14000)
        Unknown11050('06000000707465665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('pt253_00', 2)	# 1-2
    sprite('pt253_01', 2)	# 3-4
    sprite('pt253_02', 2)	# 5-6
    sprite('pt253_03', 2)	# 7-8
    sprite('pt253_04', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    Unknown22004(3, 1)
    Unknown7009(2)
    SFX_0('004_swing_grap_1_0')
    SFX_3('ptse_23')
    sprite('pt253_05', 2)	# 11-12	 **attackbox here**
    sprite('pt253_04', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('pt253_05', 2)	# 15-16	 **attackbox here**
    sprite('pt253_04', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('pt253_05', 2)	# 19-20	 **attackbox here**
    sprite('pt253_04', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('pt253_06', 4)	# 23-26
    Recovery()
    Unknown2063()
    sprite('pt253_07', 4)	# 27-30
    sprite('pt253_08', 4)	# 31-34
    sprite('pt253_09', 4)	# 35-38
    sprite('pt253_10', 4)	# 39-42
    sprite('pt253_11', 4)	# 43-46

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown2057(0)
        SLOT_4 = 1
        SLOT_59 = 5
    sprite('pt257_00', 2)	# 1-2
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt258_00', 1)	# 4-4
    AttackLevel_(3)
    Damage(1800)
    AttackP1(80)
    AttackP2(70)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(-72000)
    YImpluseBeforeWallbounce(0)
    AirUntechableTime(50)
    Unknown9190(1)
    Unknown9118(10)
    Hitstop(15)
    Unknown11050('06000000707465665f6869745f66726970616e0000000000000000000000000000000000')
    physicsYImpulse(15000)
    physicsXImpulse(2000)
    Unknown1043()
    Unknown22004(12, 1)
    sprite('pt258_00', 2)	# 5-6
    sprite('pt258_01', 4)	# 7-10
    sprite('pt258_02', 3)	# 11-13
    if (not SLOT_7):
        SFX_4('bpt310_0')
    else:
        SFX_4('bpt310_1')
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_2')
    sprite('pt258_03', 2)	# 14-15	 **attackbox here**
    sprite('pt258_04', 2)	# 16-17	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt258_04', 5)	# 18-22	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('pt258_05', 2)	# 23-24	 **attackbox here**
    GFX_1('ptef_207dellight', 0)
    GFX_1('ptef_207dellight', 1)
    sprite('pt257_07', 3)	# 25-27
    sprite('pt257_08ex01', 3)	# 28-30
    callSubroutine('StuffColorReset')
    sprite('pt257_09', 3)	# 31-33
    sprite('pt257_10', 3)	# 34-36
    sprite('pt257_11', 3)	# 37-39
    sprite('pt257_12', 3)	# 40-42
    ExitState()
    label(100)
    sprite('pt258_06', 2)	# 43-44
    AttackLevel_(3)
    Damage(2160)
    AttackP1(80)
    AttackP2(80)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(-72000)
    YImpluseBeforeWallbounce(0)
    AirUntechableTime(50)
    Unknown9190(1)
    Unknown9118(10)
    Hitstop(20)
    Unknown11050('02000000707465665f6869745f6861726973656e00000000000000000000000000000000')
    Unknown23159('SpAirHarisen')
    sprite('pt258_06', 2)	# 45-46
    physicsYImpulse(15000)
    physicsXImpulse(2000)
    Unknown1043()
    Unknown22004(12, 1)
    sprite('pt258_07', 3)	# 47-49
    sprite('pt258_08', 3)	# 50-52
    if (not SLOT_7):
        SFX_4('bpt312_0')
    else:
        SFX_4('bpt312_1')
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_2')
    sprite('pt258_09', 2)	# 53-54	 **attackbox here**
    sprite('pt258_10', 2)	# 55-56	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    GFX_1('ptef_lightrod00', 3)
    GFX_1('ptef_207dellight', 4)
    sprite('pt258_10', 5)	# 57-61	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('pt258_11', 2)	# 62-63	 **attackbox here**
    GFX_1('ptef_207dellight', 0)
    GFX_1('ptef_207dellight', 1)
    GFX_1('ptef_207dellight', 2)
    sprite('pt257_07', 3)	# 64-66
    sprite('pt257_08ex01', 3)	# 67-69
    callSubroutine('StuffColorReset')
    sprite('pt257_09', 3)	# 70-72
    sprite('pt257_10', 3)	# 73-75
    sprite('pt257_11', 3)	# 76-78
    sprite('pt257_12', 3)	# 79-81
    ExitState()

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        SLOT_4 = 1
        SLOT_59 = 1
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('pt204_00', 2)	# 1-2
    sprite('pt204_01', 2)	# 3-4
    sprite('pt204_02', 1)	# 5-5
    if SLOT_5:
        sendToLabel(100)
    sprite('pt204_02', 4)	# 6-9
    Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
    sprite('pt204_03', 4)	# 10-13	 **attackbox here**
    sprite('pt204_04', 4)	# 14-17
    sprite('pt204_05', 2)	# 18-19
    if (not SLOT_7):
        SFX_1('bpt301_0')
    else:
        SFX_1('bpt301_1')
    sprite('pt204_06', 2)	# 20-21	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_hammerDwave', 0)
    ScreenShake(0, 2500)
    SFX_3('ptse_02')
    SFX_0('003_swing_grap_0_2')
    sprite('pt204_06', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    sprite('pt204_07', 3)	# 25-27	 **attackbox here**
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    GFX_1('ptef_204dellight00', 3)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    GFX_1('ptef_lightrod00', 3)
    sprite('pt204_08', 3)	# 28-30	 **attackbox here**
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    sprite('pt204_08ex00', 3)	# 31-33	 **attackbox here**
    sprite('pt204_09', 3)	# 34-36
    callSubroutine('StuffColorReset')
    sprite('pt204_10', 3)	# 37-39
    sprite('pt204_11', 3)	# 40-42
    sprite('pt204_12', 3)	# 43-45
    sprite('pt204_13', 3)	# 46-48
    ExitState()
    label(100)
    sprite('pt204_02', 3)	# 49-51

    def upon_11():
        SLOT_53 = 1
    Unknown23159('SpHammer')
    sprite('pt204_14', 4)	# 52-55	 **attackbox here**
    sprite('pt204_15', 5)	# 56-60
    sprite('pt204_16', 2)	# 61-62
    if (not SLOT_7):
        SFX_1('bpt303_0')
    else:
        SFX_1('bpt303_1')
    sprite('pt204_17', 2)	# 63-64	 **attackbox here**
    GFX_1('ptef_hammerDshock', 0)
    SFX_0('005_swing_grap_2_1')
    ScreenShake(0, 12000)
    StartMultihit()
    sprite('pt204_17', 3)	# 65-67	 **attackbox here**
    RefreshMultihit()
    sprite('pt204_18', 3)	# 68-70	 **attackbox here**
    if (not SLOT_53):
        GFX_0('Atk5DHiquake', 100)
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    GFX_1('ptef_204dellight00', 3)
    GFX_1('ptef_204dellight00', 4)
    GFX_1('ptef_204dellight00', 5)
    GFX_1('ptef_lightrod00', 2)
    GFX_1('ptef_lightrod00', 3)
    GFX_1('ptef_lightrod00', 4)
    GFX_1('ptef_lightrod00', 6)
    sprite('pt204_19', 3)	# 71-73	 **attackbox here**
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    GFX_1('ptef_204dellight', 3)
    GFX_1('ptef_204dellight', 4)
    GFX_1('ptef_204dellight', 5)
    sprite('pt204_19ex00', 3)	# 74-76	 **attackbox here**
    sprite('pt204_09', 3)	# 77-79
    callSubroutine('StuffColorReset')
    sprite('pt204_10', 3)	# 80-82
    sprite('pt204_11', 3)	# 83-85
    sprite('pt204_12', 3)	# 86-88
    sprite('pt204_13', 3)	# 89-91

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    SLOT_4 = 1
    SLOT_59 = 1
    Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('pt204_07', 2)	# 2-3	 **attackbox here**
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    GFX_1('ptef_204dellight00', 3)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    GFX_1('ptef_lightrod00', 3)
    sprite('pt204_08', 2)	# 4-5	 **attackbox here**
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    sprite('pt204_08ex00', 2)	# 6-7	 **attackbox here**
    sprite('pt204_09', 2)	# 8-9
    callSubroutine('StuffColorReset')
    sprite('pt204_10', 2)	# 10-11
    sprite('pt204_11', 2)	# 12-13
    sprite('pt204_12', 1)	# 14-14
    sprite('pt204_13', 1)	# 15-15
    sprite('pt407_00', 2)	# 16-17
    sprite('pt407_01', 1)	# 18-18
    SFX_1('pt159')
    sprite('pt407_01', 1)	# 19-19
    sprite('pt407_02', 2)	# 20-21	 **attackbox here**
    sprite('pt407_03', 2)	# 22-23	 **attackbox here**
    sprite('pt407_04', 2)	# 24-25	 **attackbox here**
    sprite('pt407_05', 2)	# 26-27	 **attackbox here**
    if (not SLOT_7):
        SFX_1('bpt157_0')
    else:
        SFX_1('bpt157_1')
    sprite('pt407_03', 2)	# 28-29	 **attackbox here**
    sprite('pt407_06', 1)	# 30-30	 **attackbox here**
    RefreshMultihit()
    SFX_3('ptse_08')
    SFX_3('ptse_02')
    Unknown4048(90000)
    Unknown4045('707465665f67756172646372757368707463000000000000000000000000000000000000')
    sprite('pt407_06', 2)	# 31-32	 **attackbox here**
    StartMultihit()
    sprite('pt407_07', 2)	# 33-34	 **attackbox here**
    physicsXImpulse(-3000)
    sprite('pt407_08', 3)	# 35-37	 **attackbox here**
    Unknown1019(60)
    sprite('pt407_09', 3)	# 38-40	 **attackbox here**
    Unknown1019(20)
    sprite('pt407_10', 3)	# 41-43
    physicsXImpulse(0)
    sprite('pt407_11', 2)	# 44-45
    sprite('pt407_12', 2)	# 46-47
    label(0)
    sprite('pt000_00', 7)	# 48-54
    sprite('pt000_01', 7)	# 55-61
    sprite('pt000_02', 7)	# 62-68
    sprite('pt000_03', 7)	# 69-75
    sprite('pt000_04', 7)	# 76-82
    sprite('pt000_05', 7)	# 83-89
    sprite('pt000_06', 7)	# 90-96
    sprite('pt000_07', 7)	# 97-103
    sprite('pt000_08', 7)	# 104-110
    sprite('pt000_09', 7)	# 111-117
    sprite('pt000_10', 7)	# 118-124
    sprite('pt000_11', 7)	# 125-131
    sprite('pt000_12', 7)	# 132-138
    sprite('pt000_13', 7)	# 139-145
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 146-146

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        SLOT_4 = 1
        SLOT_59 = 7
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown11050('06000000707465665f6869745f6261740000000000000000000000000000000000000000')
    sprite('pt205_00', 2)	# 1-2
    sprite('pt205_00', 1)	# 3-3
    if SLOT_5:
        sendToLabel(1)
    sprite('pt205_01', 4)	# 4-7
    sprite('pt205_02', 4)	# 8-11
    sprite('pt205_03', 1)	# 12-12	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('pt205_04', 2)	# 13-14	 **attackbox here**
    sprite('pt205_05', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    GFX_1('ptef_205dellight00', 0)
    GFX_1('ptef_205dellight00', 1)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    sprite('pt205_06', 4)	# 16-19
    GFX_1('ptef_205dellight', 0)
    GFX_1('ptef_205dellight', 1)
    GFX_1('ptef_205dellight', 2)
    sprite('pt205_07', 2)	# 20-21	 **attackbox here**
    sprite('pt205_08', 2)	# 22-23
    sprite('pt205_09', 2)	# 24-25
    callSubroutine('StuffColorReset')
    gotoLabel(5)
    label(1)
    sprite('pt205_01', 4)	# 26-29
    Unknown11050('06000000707465665f6869745f6b616e61626f7500000000000000000000000000000000')
    sprite('pt205_11', 4)	# 30-33
    sprite('pt205_12', 1)	# 34-34	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('pt205_13', 2)	# 35-36	 **attackbox here**
    sprite('pt205_14', 1)	# 37-37	 **attackbox here**
    RefreshMultihit()
    GFX_1('ptef_205dellight00', 0)
    GFX_1('ptef_205dellight00', 1)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt205_15', 3)	# 38-40
    GFX_1('ptef_205dellight', 0)
    GFX_1('ptef_205dellight', 1)
    GFX_1('ptef_205dellight', 2)
    sprite('pt205_07', 3)	# 41-43	 **attackbox here**
    sprite('pt205_08', 2)	# 44-45
    sprite('pt205_09', 2)	# 46-47
    callSubroutine('StuffColorReset')
    label(5)
    sprite('pt404_09', 2)	# 48-49
    sprite('pt404_10', 3)	# 50-52
    sprite('pt404_11', 3)	# 53-55
    sprite('pt404_12', 3)	# 56-58
    sprite('pt404_13', 2)	# 59-60
    sprite('pt404_14', 2)	# 61-62
    sprite('pt404_15', 2)	# 63-64
    sprite('pt404_16', 2)	# 65-66
    sprite('pt404_17', 32767)	# 67-32833
    label(1)
    sprite('keep', 1)	# 32834-32834

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('pt404_17', 10)	# 1-10
    sprite('pt404_18', 5)	# 11-15
    if (not SLOT_7):
        SFX_1('bpt158_0')
    else:
        SFX_1('bpt158_1')
    sprite('pt404_19', 4)	# 16-19
    sprite('pt404_20', 3)	# 20-22	 **attackbox here**
    GFX_1('ptef_404kiss', 1)
    SFX_3('ptse_15')
    SFX_0('016_explode_2')
    GFX_1('ptef_bomber_heart', 0)
    sprite('pt404_21', 3)	# 23-25
    DisableAttackRestOfMove()
    sprite('pt404_22', 3)	# 26-28
    sprite('pt404_22', 3)	# 29-31
    sprite('pt404_23', 3)	# 32-34	 **attackbox here**
    sprite('pt404_23', 3)	# 35-37	 **attackbox here**
    sprite('pt404_24', 3)	# 38-40
    sprite('pt404_25', 3)	# 41-43
    sprite('pt404_26', 5)	# 44-48
    GFX_0('CommandThrowRod', 0)
    sprite('pt404_27', 4)	# 49-52
    sprite('pt404_28', 4)	# 53-56
    sprite('pt404_29', 4)	# 57-60
    loopRest()

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('pt404_17', 1)	# 1-1
    sprite('pt404_17', 32767)	# 2-32768
    label(1)
    sprite('pt404_17', 10)	# 32769-32778
    sprite('pt404_18', 5)	# 32779-32783
    if (not SLOT_7):
        SFX_1('bpt158_0')
    else:
        SFX_1('bpt158_1')
    sprite('pt404_19', 4)	# 32784-32787
    sprite('pt404_20', 3)	# 32788-32790	 **attackbox here**
    GFX_1('ptef_404kiss', 1)
    SFX_3('ptse_15')
    SFX_0('016_explode_2')
    GFX_1('ptef_bomber_heart', 0)
    sprite('pt404_21', 3)	# 32791-32793
    DisableAttackRestOfMove()
    sprite('pt404_22', 3)	# 32794-32796
    sprite('pt404_22', 3)	# 32797-32799
    sprite('pt404_23', 3)	# 32800-32802	 **attackbox here**
    sprite('pt404_23', 3)	# 32803-32805	 **attackbox here**
    sprite('pt404_24', 3)	# 32806-32808
    sprite('pt404_25', 3)	# 32809-32811
    sprite('pt404_26', 5)	# 32812-32816
    GFX_0('CommandThrowRod', 0)
    sprite('pt404_27', 4)	# 32817-32820
    sprite('pt404_28', 4)	# 32821-32824
    sprite('pt404_29', 4)	# 32825-32828

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        DisableAttackRestOfMove()
        SLOT_4 = 1
        SLOT_59 = 1
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 27)	# 1-27
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 28-28
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-250000)
    Unknown1007(600000)
    physicsYImpulse(-45000)
    setGravity(0)
    if SLOT_5:
        sendToLabel(100)
    else:
        sendToLabel(0)
    label(0)
    sprite('null', 1)	# 29-29

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(5)
    label(1)
    sprite('pt255_04', 3)	# 30-32	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_05', 3)	# 33-35	 **attackbox here**
    sprite('pt255_06', 3)	# 36-38	 **attackbox here**
    sprite('pt255_07', 3)	# 39-41	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    sprite('pt255_08', 3)	# 42-44	 **attackbox here**
    sprite('pt255_09', 3)	# 45-47	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(5)
    sprite('pt255_10', 1)	# 48-48	 **attackbox here**
    Unknown2006()
    RefreshMultihit()
    Unknown1084(1)
    SFX_3('ptse_02')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_airhammerDwave', -1)
    sprite('pt255_11', 2)	# 49-50	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    sprite('pt255_12', 2)	# 51-52
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    callSubroutine('StuffColorReset')
    sprite('pt255_13', 2)	# 53-54
    sprite('pt255_14', 2)	# 55-56
    sprite('pt255_15', 1)	# 57-57
    loopRest()
    gotoLabel(900)
    label(100)
    sprite('null', 1)	# 58-58

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(105)
    label(101)
    sprite('pt255_18', 3)	# 59-61	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_19', 3)	# 62-64	 **attackbox here**
    sprite('pt255_20', 3)	# 65-67	 **attackbox here**
    sprite('pt255_21', 3)	# 68-70	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    sprite('pt255_22', 3)	# 71-73	 **attackbox here**
    sprite('pt255_17', 3)	# 74-76	 **attackbox here**
    loopRest()
    gotoLabel(101)
    label(105)
    sprite('pt255_23', 3)	# 77-79	 **attackbox here**
    Unknown2006()
    RefreshMultihit()
    Unknown1084(1)
    SFX_0('100_hit_grap_2')
    Unknown8000(100, 1, 1)
    GFX_1('ptef_hammerDshock', 0)
    sprite('pt255_24', 2)	# 80-81	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_204dellight00', 0)
    GFX_1('ptef_204dellight00', 1)
    GFX_1('ptef_204dellight00', 2)
    GFX_1('ptef_204dellight00', 3)
    sprite('pt255_12', 2)	# 82-83
    sprite('pt255_13', 2)	# 84-85
    GFX_1('ptef_204dellight', 0)
    GFX_1('ptef_204dellight', 1)
    GFX_1('ptef_204dellight', 2)
    GFX_1('ptef_204dellight', 3)
    GFX_1('ptef_204dellight', 4)
    callSubroutine('StuffColorReset')
    sprite('pt255_14', 2)	# 86-87
    sprite('pt255_15', 3)	# 88-90
    loopRest()
    label(900)
    sprite('pt000_00', 7)	# 91-97
    sprite('pt000_01', 7)	# 98-104
    sprite('pt000_02', 7)	# 105-111
    sprite('pt000_03', 7)	# 112-118
    sprite('pt000_04', 7)	# 119-125
    sprite('pt000_05', 7)	# 126-132
    sprite('pt000_06', 7)	# 133-139
    sprite('pt000_07', 7)	# 140-146
    sprite('pt000_08', 7)	# 147-153
    sprite('pt000_09', 7)	# 154-160
    sprite('pt000_10', 7)	# 161-167
    sprite('pt000_11', 7)	# 168-174
    sprite('pt000_12', 7)	# 175-181
    sprite('pt000_13', 7)	# 182-188
    gotoLabel(0)

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
    sprite('pt210_00', 3)	# 1-3
    sprite('pt210_01', 2)	# 4-5
    sprite('pt210_01', 3)	# 6-8
    sprite('pt210_02', 3)	# 9-11
    sprite('pt210_03', 4)	# 12-15	 **attackbox here**
    Unknown7009(0)
    SFX_0('009_swing_rapier_0')
    sprite('pt210_04', 3)	# 16-18
    label(0)
    Unknown1084(1)
    sprite('pt404_10', 2)	# 19-20
    sprite('pt404_11', 2)	# 21-22
    sprite('pt404_12', 3)	# 23-25
    sprite('pt404_13', 2)	# 26-27
    sprite('pt404_14', 2)	# 28-29
    sprite('pt404_15', 1)	# 30-30
    sprite('pt404_16', 2)	# 31-32
    sprite('pt404_17', 32767)	# 33-32799

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('pt404_17', 10)	# 1-10
    sprite('pt404_18', 5)	# 11-15
    sprite('pt404_19', 4)	# 16-19
    sprite('pt404_20', 3)	# 20-22	 **attackbox here**
    GFX_1('ptef_404kiss', 1)
    SFX_3('ptse_15')
    SFX_0('016_explode_2')
    GFX_1('ptef_bomber_heart', 0)
    sprite('pt404_21', 3)	# 23-25
    DisableAttackRestOfMove()
    sprite('pt404_22', 3)	# 26-28
    sprite('pt404_22', 3)	# 29-31
    sprite('pt404_23', 3)	# 32-34	 **attackbox here**
    sprite('pt404_23', 3)	# 35-37	 **attackbox here**
    sprite('pt404_24', 3)	# 38-40
    sprite('pt404_25', 3)	# 41-43
    sprite('pt404_26', 5)	# 44-48
    GFX_0('CommandThrowRod', 0)
    sprite('pt404_27', 4)	# 49-52
    sprite('pt404_28', 4)	# 53-56
    sprite('pt404_29', 4)	# 57-60
    loopRest()

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('pt404_17', 1)	# 1-1
    sprite('pt404_17', 32767)	# 2-32768
    label(1)
    sprite('pt404_17', 10)	# 32769-32778
    sprite('pt404_18', 5)	# 32779-32783
    sprite('pt404_19', 4)	# 32784-32787
    sprite('pt404_20', 3)	# 32788-32790	 **attackbox here**
    GFX_1('ptef_404kiss', 1)
    SFX_3('ptse_15')
    SFX_0('016_explode_2')
    GFX_1('ptef_bomber_heart', 0)
    sprite('pt404_21', 3)	# 32791-32793
    DisableAttackRestOfMove()
    sprite('pt404_22', 3)	# 32794-32796
    sprite('pt404_22', 3)	# 32797-32799
    sprite('pt404_23', 3)	# 32800-32802	 **attackbox here**
    sprite('pt404_23', 3)	# 32803-32805	 **attackbox here**
    sprite('pt404_24', 3)	# 32806-32808
    sprite('pt404_25', 3)	# 32809-32811
    sprite('pt404_26', 5)	# 32812-32816
    GFX_0('CommandThrowRod', 0)
    sprite('pt404_27', 4)	# 32817-32820
    sprite('pt404_28', 4)	# 32821-32824
    sprite('pt404_29', 4)	# 32825-32828

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('pt030_00', 5)	# 1-5
    sprite('pt032_00', 2)	# 6-7
    sprite('pt032_01', 2)	# 8-9
    label(0)
    sprite('pt032_02', 4)	# 10-13
    sprite('pt032_03', 4)	# 14-17
    Unknown8006(100, 1, 1)
    sprite('pt032_04', 4)	# 18-21
    sprite('pt032_05', 4)	# 22-25
    sprite('pt032_06', 4)	# 26-29
    sprite('pt032_07', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('pt032_08', 4)	# 34-37
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt310_00', 1)	# 38-38
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('pt310_01', 2)	# 39-40
    SFX_0('010_swing_sword_0')
    sprite('pt310_02', 3)	# 41-43	 **attackbox here**
    Unknown1084(1)
    sprite('pt310_03', 3)	# 44-46
    if (not SLOT_7):
        SFX_4('bpt155_0')
    else:
        SFX_4('bpt155_1')
    sprite('pt310_04', 3)	# 47-49
    sprite('pt310_05', 3)	# 50-52
    sprite('pt310_04', 3)	# 53-55
    sprite('pt310_05', 3)	# 56-58
    sprite('pt310_06', 3)	# 59-61
    sprite('pt310_07', 3)	# 62-64
    sprite('pt310_08', 2)	# 65-66

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        Hitstop(20)
        PushbackX(10133)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(7200)
        AirPushbackY(33500)
        YImpluseBeforeWallbounce(1800)
        AirUntechableTime(60)
        Unknown11050('06000000707465665f6869745f7468726f77000000000000000000000000000000000000')
        Unknown2003(1)

        def upon_12():
            Unknown21007(8, 35)
    sprite('pt310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('pt310_08', 3)	# 4-6
    GFX_0('ThrowKousoku', 0)
    Unknown38(4, 1)
    SFX_1('pt153')
    if (not SLOT_7):
        SFX_1('bpt153_0')
    else:
        SFX_1('bpt153_1')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('pt311_00', 4)	# 7-10
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('pt203_00ex01', 4)	# 11-14
    SFX_0('022_magiccircle_b')
    SFX_3('ptse_17')
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('pt203_01ex01', 5)	# 15-19
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('pt203_02ex01', 5)	# 20-24
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('pt203_03ex01', 5)	# 25-29
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Kemuri', 0)
    sprite('pt203_04ex01', 5)	# 30-34
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('MagicIron', 0)
    Unknown38(8, 1)
    Unknown21007(8, 32)
    Unknown13(4)
    sprite('pt203_05ex01', 15)	# 35-49	 **attackbox here**
    sprite('pt203_05ex01', 1)	# 50-50	 **attackbox here**
    Unknown2003(0)
    sprite('pt203_06ex01', 4)	# 51-54
    sprite('pt203_07ex01', 4)	# 55-58
    sprite('pt203_08ex01', 4)	# 59-62
    sprite('pt203_09ex01', 4)	# 63-66
    sprite('pt203_10ex01', 4)	# 67-70
    sprite('pt203_11ex01', 3)	# 71-73
    SFX_FOOTSTEP_(100, 1, 1)

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('pt030_00', 5)	# 1-5
    sprite('pt032_00', 2)	# 6-7
    sprite('pt032_01', 2)	# 8-9
    label(0)
    sprite('pt032_02', 4)	# 10-13
    sprite('pt032_03', 4)	# 14-17
    Unknown8006(100, 1, 1)
    sprite('pt032_04', 4)	# 18-21
    sprite('pt032_05', 4)	# 22-25
    sprite('pt032_06', 4)	# 26-29
    sprite('pt032_07', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('pt032_08', 4)	# 34-37
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt310_00', 1)	# 38-38
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('pt310_01', 2)	# 39-40
    SFX_0('010_swing_sword_0')
    sprite('pt310_02', 3)	# 41-43	 **attackbox here**
    Unknown1084(1)
    sprite('pt310_03', 3)	# 44-46
    if (not SLOT_7):
        SFX_4('bpt155_0')
    else:
        SFX_4('bpt155_1')
    sprite('pt310_04', 3)	# 47-49
    sprite('pt310_05', 3)	# 50-52
    sprite('pt310_04', 3)	# 53-55
    sprite('pt310_05', 3)	# 56-58
    sprite('pt310_06', 3)	# 59-61
    sprite('pt310_07', 3)	# 62-64
    sprite('pt310_08', 2)	# 65-66

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
        Unknown9346(1)
        Unknown9178(1)
        WallbounceReboundTime(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('BackThrowExeAdd')
        Unknown13021(1)
        Unknown21005(1)
        DisableAttackRestOfMove()
        Unknown13024(0)
        JumpCancel_(0)
    sprite('pt310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('pt310_02', 1)	# 4-4	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('ThrowKousoku', 0)
    Unknown38(4, 1)
    SFX_0('022_magiccircle_b')
    SFX_3('ptse_17')
    Unknown11083(0)
    sprite('pt310_02', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11083(1)
    Unknown11001(100, 100, 100)
    sprite('pt203_07ex01', 3)	# 6-8
    Unknown2015(50)
    EnableCollision(0)
    physicsXImpulse(60000)
    sprite('pt203_08ex01', 5)	# 9-13
    Unknown1019(33)
    sprite('pt203_09ex01', 5)	# 14-18
    Unknown1019(50)
    sprite('pt203_10ex01', 5)	# 19-23
    Unknown1019(50)
    sprite('keep', 5)	# 24-28
    enterState('BackThrowExeAdd')

@State
def BackThrowExeAdd():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        Unknown11056(3)
        Hitstop(20)
        PushbackX(15200)
        Unknown11001(0, 0, 5)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(7200)
        AirPushbackY(33500)
        YImpluseBeforeWallbounce(1800)
        AirUntechableTime(60)
        Unknown11050('06000000707465665f6869745f7468726f77000000000000000000000000000000000000')
        Unknown13021(1)
        Unknown21005(1)
        DisableAttackRestOfMove()

        def upon_12():
            Unknown21007(8, 35)
    sprite('pt203_00ex01', 3)	# 1-3
    Unknown2006()
    Unknown2015(100)
    EnableCollision(1)
    Unknown1019(0)
    if (not SLOT_7):
        SFX_1('bpt153_0')
    else:
        SFX_1('bpt153_1')
    sprite('pt203_01ex01', 4)	# 4-7
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('pt203_02ex01', 4)	# 8-11
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Kemuri', 0)
    sprite('pt203_03ex01', 5)	# 12-16
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('MagicIron', 0)
    Unknown38(8, 1)
    Unknown21007(8, 32)
    sprite('pt203_04ex01', 5)	# 17-21
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('pt203_05ex01', 8)	# 22-29	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown13(4)
    sprite('pt203_05ex01', 1)	# 30-30	 **attackbox here**
    RefreshMultihit()
    sprite('pt203_06ex01', 4)	# 31-34
    sprite('pt203_07ex01', 4)	# 35-38
    sprite('pt203_08ex01', 4)	# 39-42
    sprite('pt203_09ex01', 4)	# 43-46
    sprite('pt203_10ex01', 4)	# 47-50
    sprite('pt203_11ex01', 3)	# 51-53
    SFX_FOOTSTEP_(100, 1, 1)

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        SLOT_4 = 1
        SLOT_59 = 7
    sprite('pt205_00', 2)	# 1-2
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        Unknown23159('SpBat')
        sendToLabel(100)
    sprite('pt205_01', 4)	# 4-7
    AttackLevel_(3)
    Damage(2000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(25000)
    AirPushbackY(46000)
    YImpluseBeforeWallbounce(2800)
    Hitstop(22)
    AirUntechableTime(60)
    Unknown11050('06000000707465665f6869745f6261740000000000000000000000000000000000000000')
    sprite('pt205_02', 3)	# 8-10
    if (not SLOT_7):
        SFX_1('bpt313_0')
    else:
        SFX_1('bpt313_1')
    sprite('pt205_03', 1)	# 11-11	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('pt205_04', 2)	# 12-13	 **attackbox here**
    setInvincible(0)
    sprite('pt205_05', 1)	# 14-14	 **attackbox here**
    GFX_1('ptef_205dellight00', 0)
    GFX_1('ptef_205dellight00', 1)
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    sprite('pt205_06', 9)	# 15-23
    GFX_1('ptef_205dellight', 0)
    GFX_1('ptef_205dellight', 1)
    GFX_1('ptef_205dellight', 2)
    sprite('pt205_07ex01', 11)	# 24-34	 **attackbox here**
    callSubroutine('StuffColorReset')
    sprite('pt205_08', 8)	# 35-42
    sprite('pt205_09', 8)	# 43-50
    sprite('pt205_10', 7)	# 51-57
    ExitState()
    label(100)
    sprite('pt205_01', 4)	# 58-61
    AttackLevel_(3)
    Damage(2500)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(25000)
    AirPushbackY(46000)
    YImpluseBeforeWallbounce(2800)
    Hitstop(22)
    AirUntechableTime(60)
    Unknown11050('06000000707465665f6869745f6b616e61626f7500000000000000000000000000000000')
    sprite('pt205_11', 3)	# 62-64
    if (not SLOT_7):
        SFX_1('bpt315_0')
    else:
        SFX_1('bpt315_1')
    sprite('pt205_12', 1)	# 65-65	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('pt205_13', 1)	# 66-66	 **attackbox here**
    sprite('pt205_14', 2)	# 67-68	 **attackbox here**
    GFX_1('ptef_205dellight00', 0)
    GFX_1('ptef_205dellight00', 1)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt205_15', 9)	# 69-77
    setInvincible(0)
    GFX_1('ptef_205dellight', 0)
    GFX_1('ptef_205dellight', 1)
    GFX_1('ptef_205dellight', 2)
    sprite('pt205_07ex01', 11)	# 78-88	 **attackbox here**
    callSubroutine('StuffColorReset')
    sprite('pt205_08', 8)	# 89-96
    sprite('pt205_09', 8)	# 97-104
    sprite('pt205_10', 7)	# 105-111
    ExitState()

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        SLOT_4 = 1
        SLOT_59 = 7
        clearUponHandler(2)
    sprite('pt256_00', 2)	# 1-2
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        Unknown23159('SpAirBat')
        sendToLabel(100)
    sprite('pt256_01', 1)	# 4-4
    AttackLevel_(3)
    Damage(2000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(13000)
    AirPushbackY(30000)
    Hitstop(22)
    AirUntechableTime(40)
    Unknown11050('06000000707465665f6869745f6261740000000000000000000000000000000000000000')
    Unknown1084(1)
    sprite('pt256_01', 3)	# 5-7
    sendToLabelUpon(2, 500)
    physicsYImpulse(16000)
    physicsXImpulse(2000)
    setGravity(1850)
    sprite('pt256_02', 3)	# 8-10
    if (not SLOT_7):
        SFX_1('bpt314_0')
    else:
        SFX_1('bpt314_1')
    sprite('pt256_03', 1)	# 11-11	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('pt256_03', 2)	# 12-13	 **attackbox here**
    setInvincible(0)
    sprite('pt256_04', 1)	# 14-14	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt256_04', 4)	# 15-18	 **attackbox here**
    sprite('pt256_05', 2)	# 19-20
    Unknown1043()
    sprite('pt256_06', 4)	# 21-24
    GFX_1('ptef_205dellight', 0)
    GFX_1('ptef_205dellight', 1)
    GFX_1('ptef_205dellight', 2)
    callSubroutine('StuffColorReset')
    sprite('pt256_07', 3)	# 25-27
    sprite('pt256_08', 3)	# 28-30
    sprite('pt256_09', 4)	# 31-34
    sprite('pt256_10', 3)	# 35-37
    sprite('pt256_11', 3)	# 38-40
    loopRest()
    gotoLabel(450)
    label(100)
    sprite('pt256_01', 1)	# 41-41
    AttackLevel_(3)
    Damage(2500)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(13000)
    AirPushbackY(30000)
    Hitstop(22)
    AirUntechableTime(40)
    Unknown11050('06000000707465665f6869745f6b616e61626f7500000000000000000000000000000000')
    Unknown1084(1)
    sprite('pt256_01', 3)	# 42-44
    physicsYImpulse(16000)
    physicsXImpulse(2000)
    setGravity(1850)
    sendToLabelUpon(2, 500)
    sprite('pt256_12', 3)	# 45-47
    if (not SLOT_7):
        SFX_1('bpt316_0')
    else:
        SFX_1('bpt316_1')
    sprite('pt256_13', 1)	# 48-48	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('pt256_13', 4)	# 49-52	 **attackbox here**
    setInvincible(0)
    sprite('pt256_14', 5)	# 53-57	 **attackbox here**
    GFX_1('ptef_lightrod00', 0)
    GFX_1('ptef_lightrod00', 1)
    GFX_1('ptef_lightrod00', 2)
    sprite('pt256_15', 1)	# 58-58
    Unknown1043()
    sprite('pt256_16', 4)	# 59-62
    GFX_1('ptef_205dellight00', 0)
    GFX_1('ptef_205dellight00', 1)
    GFX_1('ptef_205dellight00', 2)
    callSubroutine('StuffColorReset')
    sprite('pt256_07', 3)	# 63-65
    sprite('pt256_08', 3)	# 66-68
    sprite('pt256_09', 4)	# 69-72
    sprite('pt256_10', 3)	# 73-75
    sprite('pt256_11', 3)	# 76-78
    loopRest()
    gotoLabel(450)
    label(450)
    sprite('pt020_05', 3)	# 79-81
    sprite('pt020_06', 3)	# 82-84
    label(451)
    sprite('pt020_07', 4)	# 85-88
    sprite('pt020_08', 4)	# 89-92
    loopRest()
    gotoLabel(451)
    label(500)
    sprite('pt024_00', 7)	# 93-99
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('pt024_01', 11)	# 100-110
    sprite('pt024_02', 8)	# 111-118

@State
def Surfing_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        AirPushbackX(16000)
        AirPushbackY(14000)
        YImpluseBeforeWallbounce(3000)
        AirUntechableTime(26)
        Unknown9202(5)
        Unknown11050('06000000707465665f6869745f6869676800000000000000000000000000000000000000')
        Unknown2016(120)

        def upon_11():
            physicsXImpulse(45000)
            clearUponHandler(11)
            sendToLabel(0)
    sprite('pt408_00', 3)	# 1-3
    sprite('pt408_01', 3)	# 4-6
    GFX_1('ptef_specialmc', -1)
    physicsXImpulse(10000)
    physicsYImpulse(7500)
    Unknown1043()
    Unknown8001(1, 100)
    sprite('pt408_02', 2)	# 7-8
    if (not SLOT_7):
        SFX_1('bpt203_0')
    else:
        SFX_1('bpt203_1')
    sprite('pt408_03', 2)	# 9-10
    SFX_3('ptse_21')
    sprite('pt408_04', 2)	# 11-12
    Unknown1019(150)
    sprite('pt408_05', 3)	# 13-15	 **attackbox here**
    Unknown1019(200)
    GFX_0('ptef_408_splash', -1)
    sprite('pt408_06', 3)	# 16-18	 **attackbox here**
    Unknown1019(150)
    sprite('pt408_07', 3)	# 19-21	 **attackbox here**
    sprite('pt408_05', 3)	# 22-24	 **attackbox here**
    sprite('pt408_06', 3)	# 25-27	 **attackbox here**
    label(0)
    sprite('pt408_08', 3)	# 28-30
    Unknown1019(70)
    Recovery()
    Unknown26('ptef_408_splash')
    sprite('pt408_09', 3)	# 31-33
    Unknown1019(70)
    sprite('pt402_09ex01', 4)	# 34-37
    Unknown1019(40)
    physicsYImpulse(12500)
    sendToLabelUpon(2, 1)
    sprite('pt402_10ex01', 3)	# 38-40
    sprite('pt402_11ex01', 32767)	# 41-32807
    label(1)
    sprite('pt408_10', 3)	# 32808-32810
    Unknown1084(1)
    Unknown8000(104, 1, 1)
    sprite('pt402_13ex01', 3)	# 32811-32813
    sprite('pt402_14ex01', 3)	# 32814-32816
    sprite('pt402_15ex01', 2)	# 32817-32818

@State
def Surfing_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        AirUntechableTime(60)
        GroundedHitstunAnimation(9)
        HitOverhead(2)
        Unknown11058('0100000000000000000000000000000000000000')
        AirPushbackY(-45000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(50)
        Unknown11050('06000000707465665f6869745f6869676800000000000000000000000000000000000000')
        Unknown23087(120000)
        sendToLabelUpon(2, 1)
    sprite('pt402_00', 2)	# 1-2
    sprite('pt402_01', 2)	# 3-4
    sprite('pt402_02', 2)	# 5-6
    GFX_1('ptef_specialmc', -1)
    physicsXImpulse(-12000)
    physicsYImpulse(18000)
    Unknown8001(1, 100)
    sprite('pt402_03', 3)	# 7-9
    Unknown1019(50)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    SFX_3('ptse_21')
    sprite('pt402_03', 2)	# 10-11
    if (not SLOT_7):
        SFX_1('bpt202_0')
    else:
        SFX_1('bpt202_1')
    physicsXImpulse(20000)
    physicsYImpulse(30000)
    Unknown1007(75000)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_03', 3)	# 12-14
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_04', 3)	# 15-17
    Unknown1019(150)
    Unknown1007(40000)
    setGravity(4000)
    YAccel(50)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    StartMultihit()
    sprite('pt402_05', 2)	# 18-19	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    StartMultihit()
    sprite('pt402_05', 2)	# 20-21	 **attackbox here**
    Unknown1019(75)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 22-23	 **attackbox here**
    Unknown1007(-40000)
    Unknown1019(80)
    YAccel(40)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 24-25	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 26-27	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 28-29	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 32767)	# 30-32796	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    label(1)
    sprite('pt402_07', 3)	# 32797-32799
    setGravity(-100)
    physicsXImpulse(0)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    Recovery()
    sprite('pt402_08', 3)	# 32800-32802
    physicsYImpulse(15000)
    setGravity(3500)
    GFX_1('ptef_402light', 0)
    sprite('pt402_09', 3)	# 32803-32805
    GFX_1('ptef_402light', 0)
    sprite('pt402_10', 3)	# 32806-32808
    sprite('pt402_11', 3)	# 32809-32811
    sprite('pt402_12', 32767)	# 32812-65578
    sendToLabelUpon(2, 2)
    label(2)
    sprite('pt402_13', 2)	# 65579-65580
    Unknown1084(1)
    Unknown8000(104, 1, 1)
    sprite('pt402_14', 2)	# 65581-65582
    sprite('pt402_15', 3)	# 65583-65585

@State
def Surfing_Ex():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2400)
        AttackP1(80)
        AttackP2(80)
        AirUntechableTime(60)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11058('0100000000000000000000000000000000000000')
        AirPushbackX(60000)
        Unknown9178(1)
        WallbounceReboundTime(20)
        Unknown9362(1)
        Unknown9364(40)
        AirHitstunAfterWallbounce(60)
        Unknown11050('06000000707465665f6869745f6869676800000000000000000000000000000000000000')
        Unknown23087(120000)
        MinimumDamagePct(10)
        Unknown30065(0)
        sendToLabelUpon(2, 1)
    sprite('pt402_00', 2)	# 1-2
    sprite('pt402_01', 1)	# 3-3
    sprite('pt402_01', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('pt402_02', 2)	# 5-6
    GFX_1('ptef_specialmc', -1)
    physicsYImpulse(18000)
    Unknown8001(1, 100)
    sprite('pt402_03', 3)	# 7-9
    physicsXImpulse(3000)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    SFX_3('ptse_21')
    sprite('pt402_04', 2)	# 10-11
    if (not SLOT_7):
        SFX_1('bpt202_0')
    else:
        SFX_1('bpt202_1')
    physicsXImpulse(33000)
    physicsYImpulse(14000)
    Unknown1007(75000)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_04', 3)	# 12-14
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_05', 3)	# 15-17	 **attackbox here**
    physicsXImpulse(60000)
    setGravity(3000)
    YAccel(50)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    StartMultihit()
    sprite('pt402_05', 2)	# 18-19	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_05', 2)	# 20-21	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 22-23	 **attackbox here**
    YAccel(40)
    Unknown1019(70)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 24-25	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 26-27	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 2)	# 28-29	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt402_06', 32767)	# 30-32796	 **attackbox here**
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    label(1)
    sprite('pt402_07', 3)	# 32797-32799
    setGravity(-100)
    physicsXImpulse(0)
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    Recovery()
    sprite('pt402_08', 3)	# 32800-32802
    physicsYImpulse(24000)
    GFX_1('ptef_402light', 0)
    sprite('pt402_09', 3)	# 32803-32805
    physicsYImpulse(12000)
    setGravity(3500)
    GFX_1('ptef_402light', 0)
    sprite('pt402_10', 3)	# 32806-32808
    sprite('pt402_11', 3)	# 32809-32811
    sprite('pt402_12', 32767)	# 32812-65578
    sendToLabelUpon(2, 2)
    label(2)
    sprite('pt402_13', 3)	# 65579-65581
    Unknown1084(1)
    Unknown8000(104, 1, 1)
    sprite('pt402_14', 3)	# 65582-65584
    sprite('pt402_15', 4)	# 65585-65588

@State
def DriveShot_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        JumpCancel_(0)
        SLOT_4 = 1
        SLOT_59 = 11
    sprite('pt208_00', 2)	# 1-2
    Unknown1084(1)
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt208_01', 3)	# 4-6
    sprite('pt208_02', 3)	# 7-9
    sprite('pt208_03', 3)	# 10-12
    sprite('pt208_04', 3)	# 13-15
    sprite('pt208_02', 3)	# 16-18
    sprite('pt208_05', 3)	# 19-21
    if (not SLOT_7):
        Unknown7006('bpt321_0', 100, 863268962, 811545138, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt321_1', 100, 863268962, 828322354, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 22-22
    physicsXImpulse(-20000)
    GFX_0('Missile', 1)
    GFX_1('ptef_drivethrow', 1)
    sprite('pt208_06', 9)	# 23-31
    Unknown1019(70)
    sprite('pt208_06', 5)	# 32-36
    Unknown1019(30)
    sprite('pt208_07', 3)	# 37-39
    sprite('pt208_08', 3)	# 40-42
    Recovery()
    callSubroutine('StuffColorReset')
    Unknown1019(0)
    sprite('pt208_09', 3)	# 43-45
    sprite('pt208_10', 3)	# 46-48
    ExitState()
    label(100)
    sprite('pt208_01', 3)	# 49-51
    sprite('pt208_02', 3)	# 52-54
    sprite('pt208_03', 3)	# 55-57
    sprite('pt208_04', 3)	# 58-60
    sprite('pt208_02', 3)	# 61-63
    sprite('pt208_05', 3)	# 64-66
    if (not SLOT_7):
        Unknown7006('bpt323_0', 100, 863268962, 811545650, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt323_1', 100, 863268962, 828322866, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 67-67
    physicsXImpulse(-20000)
    GFX_0('SpMissile', 1)
    GFX_1('ptef_drivethrow', 1)
    sprite('pt208_06', 9)	# 68-76
    Unknown1019(70)
    sprite('pt208_06', 5)	# 77-81
    Unknown1019(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)	# 82-84
    Unknown1019(0)
    sprite('pt208_08', 3)	# 85-87
    Recovery()
    callSubroutine('StuffColorReset')
    sprite('pt208_09', 3)	# 88-90
    sprite('pt208_10', 3)	# 91-93
    ExitState()

@State
def DriveShot_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        JumpCancel_(0)
        SLOT_4 = 1
        SLOT_59 = 11
    sprite('pt208_00', 2)	# 1-2
    Unknown1084(1)
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt208_01', 3)	# 4-6
    sprite('pt208_02', 3)	# 7-9
    sprite('pt208_03', 3)	# 10-12
    sprite('pt208_04', 3)	# 13-15
    sprite('pt208_02', 3)	# 16-18
    sprite('pt208_05', 3)	# 19-21
    if (not SLOT_7):
        Unknown7006('bpt321_0', 100, 863268962, 811545138, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt321_1', 100, 863268962, 828322354, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 22-22
    physicsXImpulse(-20000)
    GFX_0('MissileB', 1)
    GFX_1('ptef_drivethrow', 1)
    sprite('pt208_06', 9)	# 23-31
    Unknown1019(70)
    sprite('pt208_06', 5)	# 32-36
    Unknown1019(30)
    sprite('pt208_07', 3)	# 37-39
    sprite('pt208_08', 3)	# 40-42
    Recovery()
    callSubroutine('StuffColorReset')
    Unknown1019(0)
    sprite('pt208_09', 3)	# 43-45
    sprite('pt208_10', 3)	# 46-48
    ExitState()
    label(100)
    sprite('pt208_01', 3)	# 49-51
    sprite('pt208_02', 3)	# 52-54
    sprite('pt208_03', 3)	# 55-57
    sprite('pt208_04', 3)	# 58-60
    sprite('pt208_02', 3)	# 61-63
    sprite('pt208_05', 3)	# 64-66
    if (not SLOT_7):
        Unknown7006('bpt323_0', 100, 863268962, 811545650, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt323_1', 100, 863268962, 828322866, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 67-67
    physicsXImpulse(-20000)
    GFX_0('SpMissileB', 1)
    GFX_1('ptef_drivethrow', 1)
    sprite('pt208_06', 9)	# 68-76
    Unknown1019(70)
    sprite('pt208_06', 5)	# 77-81
    Unknown1019(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)	# 82-84
    Unknown1019(0)
    sprite('pt208_08', 3)	# 85-87
    Recovery()
    callSubroutine('StuffColorReset')
    sprite('pt208_09', 3)	# 88-90
    sprite('pt208_10', 3)	# 91-93
    ExitState()

@State
def AirDriveShot_A():

    def upon_IMMEDIATE():
        Unknown17003()
        JumpCancel_(0)
        SLOT_4 = 1
        SLOT_59 = 9
    sprite('pt208_00', 2)	# 1-2
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt208_01', 3)	# 4-6
    Unknown1084(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    Unknown1019(20)
    setGravity(1500)
    Unknown22004(10, 1)
    sprite('pt208_02', 3)	# 7-9
    sprite('pt208_03', 3)	# 10-12
    sprite('pt208_04', 3)	# 13-15
    sprite('pt208_05', 3)	# 16-18
    if (not SLOT_7):
        Unknown7006('bpt317_0', 100, 863268962, 811546673, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt317_1', 100, 863268962, 828323889, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 19-19
    physicsXImpulse(-10000)
    GFX_0('Bomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1404, 0)
    callSubroutine('BombThrowCtrl')
    GFX_1('ptef_drivethrow', 0)
    sprite('pt208_06', 4)	# 20-23
    Unknown1019(70)
    sprite('pt208_06', 5)	# 24-28
    Unknown1019(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)	# 29-31
    Unknown1044()
    sprite('pt208_08', 3)	# 32-34
    Recovery()
    callSubroutine('StuffColorReset')
    Unknown1019(0)
    sprite('pt208_09', 3)	# 35-37
    sprite('pt208_10', 3)	# 38-40
    label(0)
    sprite('pt020_07', 4)	# 41-44
    sprite('pt020_08', 4)	# 45-48
    loopRest()
    gotoLabel(0)
    ExitState()
    label(100)
    sprite('pt208_01', 3)	# 49-51
    Unknown1084(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    Unknown1019(20)
    setGravity(1500)
    Unknown22004(10, 1)
    sprite('pt208_02', 3)	# 52-54
    sprite('pt208_03', 3)	# 55-57
    sprite('pt208_04', 3)	# 58-60
    sprite('pt208_05', 3)	# 61-63
    if (not SLOT_7):
        Unknown7006('bpt319_0', 100, 863268962, 811544626, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt319_1', 100, 863268962, 828321842, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 64-64
    physicsXImpulse(-10000)
    GFX_0('SpBomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1404, 0)
    GFX_1('ptef_drivethrow', 0)
    sprite('pt208_06', 4)	# 65-68
    Unknown1019(70)
    sprite('pt208_06', 5)	# 69-73
    Unknown1019(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)	# 74-76
    Unknown1044()
    sprite('pt208_08', 3)	# 77-79
    Recovery()
    callSubroutine('StuffColorReset')
    Unknown1019(0)
    sprite('pt208_09', 3)	# 80-82
    sprite('pt208_10', 3)	# 83-85
    label(101)
    sprite('pt020_07', 4)	# 86-89
    sprite('pt020_08', 4)	# 90-93
    loopRest()
    gotoLabel(101)
    ExitState()

@State
def AirDriveShot_B():

    def upon_IMMEDIATE():
        Unknown17003()
        JumpCancel_(0)
        SLOT_4 = 1
        SLOT_59 = 9
    sprite('pt208_00', 2)	# 1-2
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt208_01', 3)	# 4-6
    Unknown1084(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    Unknown1019(20)
    setGravity(1500)
    Unknown22004(10, 1)
    sprite('pt208_02', 3)	# 7-9
    sprite('pt208_03', 3)	# 10-12
    sprite('pt208_04', 3)	# 13-15
    sprite('pt208_05', 3)	# 16-18
    if (not SLOT_7):
        Unknown7006('bpt317_0', 100, 863268962, 811546673, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt317_1', 100, 863268962, 828323889, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 19-19
    physicsXImpulse(-10000)
    GFX_0('Bomb', 0)
    Unknown38(4, 1)
    callSubroutine('BombThrowCtrl')
    GFX_1('ptef_drivethrow', 0)
    sprite('pt208_06', 4)	# 20-23
    Unknown1019(70)
    sprite('pt208_06', 5)	# 24-28
    Unknown1019(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)	# 29-31
    Unknown1044()
    sprite('pt208_08', 3)	# 32-34
    Recovery()
    callSubroutine('StuffColorReset')
    Unknown1019(0)
    sprite('pt208_09', 3)	# 35-37
    sprite('pt208_10', 3)	# 38-40
    label(0)
    sprite('pt020_07', 4)	# 41-44
    sprite('pt020_08', 4)	# 45-48
    loopRest()
    gotoLabel(0)
    ExitState()
    label(100)
    sprite('pt208_01', 3)	# 49-51
    Unknown1084(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    Unknown1019(20)
    setGravity(1500)
    Unknown22004(10, 1)
    sprite('pt208_02', 3)	# 52-54
    sprite('pt208_03', 3)	# 55-57
    sprite('pt208_04', 3)	# 58-60
    sprite('pt208_05', 3)	# 61-63
    if (not SLOT_7):
        Unknown7006('bpt319_0', 100, 863268962, 811544626, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt319_1', 100, 863268962, 828321842, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt208_06', 1)	# 64-64
    physicsXImpulse(-10000)
    GFX_0('SpBomb', 0)
    Unknown38(4, 1)
    GFX_1('ptef_drivethrow', 0)
    sprite('pt208_06', 4)	# 65-68
    Unknown1019(70)
    sprite('pt208_06', 5)	# 69-73
    Unknown1019(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)	# 74-76
    Unknown1044()
    sprite('pt208_08', 3)	# 77-79
    Recovery()
    callSubroutine('StuffColorReset')
    Unknown1019(0)
    sprite('pt208_09', 3)	# 80-82
    sprite('pt208_10', 3)	# 83-85
    label(101)
    sprite('pt020_07', 4)	# 86-89
    sprite('pt020_08', 4)	# 90-93
    loopRest()
    gotoLabel(101)
    ExitState()

@Subroutine
def Hopping_Default():
    AttackLevel_(3)
    Damage(1200)
    AttackP1(80)
    AttackP2(80)
    if SLOT_62:
        AttackP1(64)
        AttackP2(100)
    Unknown23182(3)
    GroundedHitstunAnimation(4)
    AirPushbackY(20000)
    hitstun(20)
    AirUntechableTime(20)
    PushbackX(8000)
    Unknown11056(0)
    Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
    Unknown2061(1)
    Unknown30068(1)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)

    def upon_LANDING():
        Unknown1084(1)
    HitOrBlockCancel('HoppingPlus_A')
    HitOrBlockCancel('HoppingPlus_B')
    HitOrBlockCancel('HoppingPlus_C')
    if SLOT_61:
        Unknown30065(0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)

    def upon_12():
        SLOT_62 = (SLOT_62 + 1)

@State
def HoppingPlus_A():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('Hopping_Default')

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(50)
            Unknown1028(200)
            Unknown1015(-4000)
            physicsYImpulse(15000)
            setGravity(2800)
            if SLOT_61:
                Unknown1019(50)
                Unknown1028(100)
                Unknown1015(-3000)
                physicsYImpulse(15000)
                setGravity(3000)
            if (SLOT_60 == 0):
                GroundedHitstunAnimation(11)
                AirPushbackX(20000)
                AirPushbackY(-50000)
                AirUntechableTime(40)
                Unknown9202(1)
                Unknown1015(-500)
        Unknown22004(8, 1)
        if (SLOT_62 == 1):
            Unknown23159('HoppingPlus_A2nd')
        if (SLOT_62 == 2):
            Unknown23159('HoppingPlus_A3rd')
    sprite('pt403_17', 1)	# 1-1
    if (SLOT_60 == 1):
        Unknown14085('HoppingPlus_A')
        Unknown14085('HoppingPlus_B')
        Unknown14085('HoppingPlus_C')
    sprite('pt403_18', 2)	# 2-3
    sprite('pt403_19', 2)	# 4-5
    sprite('pt403_20', 3)	# 6-8	 **attackbox here**
    SLOT_60 = (SLOT_60 + (-1))
    GFX_0('AssaultBwave', 0)
    SFX_3('ptse_08')
    sprite('pt403_21', 3)	# 9-11	 **attackbox here**
    sprite('pt403_22', 3)	# 12-14
    Recovery()
    sprite('pt403_10', 1)	# 15-15
    if (SLOT_60 == 0):
        gotoLabel(0)
    sprite('pt403_10', 32767)	# 16-32782
    label(1)
    sprite('pt024_01', 4)	# 32783-32786
    Unknown1084(1)
    clearUponHandler(2)
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('pt024_02', 3)	# 32787-32789
    ExitState()
    label(0)
    sprite('pt403_29', 3)	# 32790-32792
    clearUponHandler(2)

    def upon_LANDING():
        physicsXImpulse(0)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('pt403_30', 3)	# 32793-32795
    sprite('pt403_06', 3)	# 32796-32798
    sprite('pt403_07', 3)	# 32799-32801

@State
def HoppingPlus_B():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('Hopping_Default')
        AirPushbackX(10000)

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(50)
            Unknown1028(200)
            Unknown1015(2000)
            YAccel(30)
            Unknown1021(25000)
            setGravity(3000)
            if SLOT_61:
                Unknown1019(50)
                Unknown1028(100)
                Unknown1015(1000)
                YAccel(30)
                Unknown1021(15000)
                setGravity(3000)
            if (SLOT_60 == 0):
                GroundedHitstunAnimation(11)
                AirPushbackX(15000)
                GroundedHitstunAnimation(9)
                AirPushbackY(-60000)
                YImpluseBeforeWallbounce(0)
                AirUntechableTime(40)
                Unknown9310(1)
        Unknown22004(8, 1)
        if (SLOT_62 == 1):
            Unknown23159('HoppingPlus_B2nd')
        if (SLOT_62 == 2):
            Unknown23159('HoppingPlus_B3rd')
    sprite('pt403_11', 1)	# 1-1
    if (SLOT_60 == 1):
        Unknown14085('HoppingPlus_A')
        Unknown14085('HoppingPlus_B')
        Unknown14085('HoppingPlus_C')
    sprite('pt403_12', 2)	# 2-3
    sprite('pt403_13', 2)	# 4-5
    sprite('pt403_14', 3)	# 6-8	 **attackbox here**
    SLOT_60 = (SLOT_60 + (-1))
    SFX_3('ptse_08')
    sprite('pt403_15', 3)	# 9-11	 **attackbox here**
    GFX_0('AssaultAwave', 0)
    sprite('pt403_16', 3)	# 12-14
    Recovery()
    sprite('pt403_10', 1)	# 15-15
    if (SLOT_60 == 0):
        gotoLabel(0)
    sprite('pt403_10', 30)	# 16-45
    label(1)
    sprite('pt024_01', 4)	# 46-49
    Unknown1084(1)
    clearUponHandler(2)
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('pt024_02', 3)	# 50-52
    ExitState()
    label(0)
    sprite('pt403_29', 3)	# 53-55
    clearUponHandler(2)

    def upon_LANDING():
        physicsXImpulse(0)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('pt403_30', 3)	# 56-58
    sprite('pt403_06', 3)	# 59-61
    sprite('pt403_07', 3)	# 62-64

@State
def HoppingPlus_C():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('Hopping_Default')
        AirPushbackX(11500)
        AirPushbackY(15000)

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(40)
            Unknown1028(200)
            Unknown1015(1500)
            YAccel(30)
            Unknown1021(25000)
            setGravity(3000)
            if SLOT_61:
                Unknown1019(40)
                Unknown1028(200)
                Unknown1015(4000)
                physicsYImpulse(12000)
                setGravity(3000)
            if (SLOT_60 == 0):
                GroundedHitstunAnimation(11)
                AirPushbackX(20000)
                AirPushbackY(-50000)
                AirUntechableTime(40)
                Unknown9202(1)
                Unknown1015(-500)
                Unknown11056(1)
        Unknown22004(8, 1)
        if (SLOT_62 == 1):
            Unknown23159('HoppingPlus_C2nd')
        if (SLOT_62 == 2):
            Unknown23159('HoppingPlus_C3rd')
    sprite('pt403_23', 1)	# 1-1
    if (SLOT_60 == 1):
        Unknown14085('HoppingPlus_A')
        Unknown14085('HoppingPlus_B')
        Unknown14085('HoppingPlus_C')
    sprite('pt403_24', 2)	# 2-3
    sprite('pt403_25', 2)	# 4-5
    sprite('pt403_26', 3)	# 6-8	 **attackbox here**
    SLOT_60 = (SLOT_60 + (-1))
    GFX_0('AssaultCwave', 0)
    SFX_3('ptse_08')
    sprite('pt403_27', 3)	# 9-11	 **attackbox here**
    sprite('pt403_28', 3)	# 12-14
    Recovery()
    sprite('pt403_10', 1)	# 15-15
    if (SLOT_60 == 0):
        gotoLabel(0)
    sprite('pt403_10', 32767)	# 16-32782
    label(1)
    sprite('pt024_01', 4)	# 32783-32786
    Unknown1084(1)
    clearUponHandler(2)
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('pt024_02', 3)	# 32787-32789
    ExitState()
    label(0)
    sprite('pt403_29', 3)	# 32790-32792
    clearUponHandler(2)

    def upon_LANDING():
        physicsXImpulse(0)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('pt403_30', 3)	# 32793-32795
    sprite('pt403_06', 3)	# 32796-32798
    sprite('pt403_07', 3)	# 32799-32801

@State
def Hopping():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        sendToLabelUpon(2, 0)
        WhiffCancel('HoppingPlus_A')
        WhiffCancel('HoppingPlus_B')
        WhiffCancel('HoppingPlus_C')

        def upon_STATE_END():
            Unknown1019(50)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_19 <= 55000):
                clearUponHandler(3)
                Unknown1019(55)
                Unknown1051(20)
    sprite('pt403_08', 2)	# 1-2
    if (not SLOT_7):
        SFX_1('bpt204_0')
    else:
        SFX_1('bpt204_1')
    physicsXImpulse(21000)
    physicsYImpulse(30000)
    setGravity(2400)
    SLOT_60 = 3
    SLOT_61 = 0
    SLOT_62 = 0
    sprite('pt403_09', 1)	# 3-3
    sprite('pt403_09', 1)	# 4-4
    Unknown8009(1)
    sprite('pt403_10', 2)	# 5-6
    sprite('pt403_17', 32767)	# 7-32773
    WhiffCancelEnable(1)
    label(0)
    sprite('pt403_29', 2)	# 32774-32775
    Unknown1084(1)
    clearUponHandler(2)
    sprite('pt403_30', 2)	# 32776-32777
    sprite('pt024_02', 2)	# 32778-32779

@State
def AirSlide():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        SLOT_6 = 0
        Unknown2037(0)

        def upon_STATE_END():
            if (SLOT_18 >= 4):
                Unknown1043()
                SFX_0('100_hit_grap_0')
                GFX_0('AirSlideBalloon', -1)

        def upon_CLEAR_OR_EXIT():
            Unknown2006()
            if SLOT_2:
                if CheckInput(0x5f):
                    physicsXImpulse(-3000)
                    physicsYImpulse(10)
                if CheckInput(0x79):
                    physicsXImpulse(3000)
                    physicsYImpulse(10)
                if CheckInput(0x45):
                    physicsYImpulse(-4000)
                if CheckInput(0x93):
                    physicsYImpulse(2500)

        def upon_LANDING():
            SFX_0('100_hit_grap_1')
            GFX_0('AirSlideBalloon', -1)
    sprite('pt401_00', 2)	# 1-2
    if (not SLOT_7):
        SFX_1('bpt201_0')
    else:
        SFX_1('bpt201_1')
    GFX_0('AirSlideMcirle', -1)
    Unknown1019(70)
    setGravity(10)
    Unknown1045(0)
    sprite('pt401_01', 1)	# 3-3	 **attackbox here**
    Unknown1019(40)
    Unknown1052(1)
    sprite('pt401_02', 5)	# 4-8	 **attackbox here**
    YAccel(0)
    Unknown2037(1)
    sprite('pt401_08', 5)	# 9-13	 **attackbox here**
    SFX_3('ptse_00')
    sprite('pt401_07', 4)	# 14-17	 **attackbox here**
    Unknown13014(1)
    Unknown13015(1)
    sprite('pt401_08', 6)	# 18-23	 **attackbox here**
    sprite('pt401_02', 6)	# 24-29	 **attackbox here**
    sprite('pt401_09', 6)	# 30-35	 **attackbox here**
    sprite('pt401_10', 6)	# 36-41	 **attackbox here**
    sprite('pt401_09', 6)	# 42-47	 **attackbox here**
    sprite('pt401_02', 6)	# 48-53	 **attackbox here**
    sprite('pt401_08', 6)	# 54-59	 **attackbox here**
    SFX_3('ptse_00')
    sprite('pt401_07', 6)	# 60-65	 **attackbox here**
    sprite('pt401_08', 6)	# 66-71	 **attackbox here**
    sprite('pt401_02', 7)	# 72-78	 **attackbox here**
    sprite('pt401_03', 3)	# 79-81
    clearUponHandler(3)
    clearUponHandler(1)
    SFX_0('100_hit_grap_0')
    GFX_0('AirSlideBalloon', -1)
    physicsYImpulse(32000)
    Unknown1043()
    sprite('pt401_04', 3)	# 82-84
    YAccel(40)
    sprite('pt401_05', 3)	# 85-87
    YAccel(30)
    sprite('pt401_06', 2)	# 88-89
    YAccel(10)
    label(0)
    sprite('pt401_06', 1)	# 90-90
    Unknown1043()

@State
def AirSlide_Ex():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        SLOT_6 = 0
        Unknown2037(0)

        def upon_STATE_END():
            if (SLOT_18 >= 4):
                Unknown1043()
                SFX_0('100_hit_grap_0')
                GFX_0('AirSlideBalloon', -1)

        def upon_CLEAR_OR_EXIT():
            Unknown2006()
            if SLOT_2:
                if CheckInput(0x5f):
                    physicsXImpulse(-3000)
                    physicsYImpulse(10)
                if CheckInput(0x79):
                    physicsXImpulse(3000)
                    physicsYImpulse(10)
                if CheckInput(0x45):
                    physicsYImpulse(-4000)
                if CheckInput(0x93):
                    physicsYImpulse(2500)

        def upon_LANDING():
            SFX_0('100_hit_grap_1')
            GFX_0('AirSlideBalloon', -1)
    sprite('pt401_00', 2)	# 1-2
    if (not SLOT_7):
        SFX_1('bpt201_0')
    else:
        SFX_1('bpt201_1')
    GFX_0('AirSlideMcirle', -1)
    Unknown1019(70)
    setGravity(10)
    Unknown1045(0)
    sprite('pt401_01', 1)	# 3-3	 **attackbox here**
    Unknown1019(40)
    Unknown1052(1)
    sprite('pt401_02', 5)	# 4-8	 **attackbox here**
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    setInvincible(1)
    Unknown22019('0100000001000000010000000100000000000000')
    YAccel(0)
    Unknown2037(1)
    sprite('pt401_08', 5)	# 9-13	 **attackbox here**
    SFX_3('ptse_00')
    Unknown13014(1)
    Unknown13015(1)
    sprite('pt401_07', 4)	# 14-17	 **attackbox here**
    sprite('pt401_08', 6)	# 18-23	 **attackbox here**
    sprite('pt401_02', 6)	# 24-29	 **attackbox here**
    sprite('pt401_09', 6)	# 30-35	 **attackbox here**
    sprite('pt401_10', 6)	# 36-41	 **attackbox here**
    sprite('pt401_09', 6)	# 42-47	 **attackbox here**
    sprite('pt401_02', 6)	# 48-53	 **attackbox here**
    sprite('pt401_08', 6)	# 54-59	 **attackbox here**
    SFX_3('ptse_00')
    sprite('pt401_07', 6)	# 60-65	 **attackbox here**
    sprite('pt401_08', 6)	# 66-71	 **attackbox here**
    sprite('pt401_02', 7)	# 72-78	 **attackbox here**
    sprite('pt401_03', 3)	# 79-81
    clearUponHandler(3)
    clearUponHandler(1)
    SFX_0('100_hit_grap_0')
    GFX_0('AirSlideBalloon', -1)
    physicsYImpulse(32000)
    Unknown1043()
    setInvincible(0)
    sprite('pt401_04', 3)	# 82-84
    YAccel(40)
    sprite('pt401_05', 3)	# 85-87
    YAccel(30)
    sprite('pt401_06', 2)	# 88-89
    YAccel(10)
    label(0)
    sprite('pt401_06', 1)	# 90-90
    Unknown1043()

@State
def DriveShot_Ex():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_4 = 1
        SLOT_59 = 11
    sprite('pt208_00', 2)	# 1-2
    Unknown1084(1)
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt405_00', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('pt405_01', 3)	# 7-9
    sprite('pt405_02', 3)	# 10-12
    sprite('pt405_03', 3)	# 13-15
    sprite('pt405_04', 3)	# 16-18
    if (not SLOT_7):
        Unknown7006('bpt207_0', 100, 846491746, 811546672, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt207_1', 100, 846491746, 828323888, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt405_05', 1)	# 19-19
    physicsXImpulse(-20000)
    GFX_0('Missile', 1)
    Unknown38(4, 1)
    Unknown23029(4, 1301, 1)
    GFX_1('ptef_throwsmokeshort', 1)
    sprite('pt405_05', 3)	# 20-22
    Unknown1019(70)
    sprite('pt405_05', 4)	# 23-26
    GFX_0('Missile', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1302, 1)
    GFX_1('ptef_throwsmokeshort', 0)
    sprite('pt405_05', 7)	# 27-33
    Unknown1019(30)
    GFX_0('Missile', 2)
    Unknown38(4, 1)
    Unknown23029(4, 1303, 1)
    GFX_1('ptef_throwsmokeshort', 2)
    sprite('pt405_06', 5)	# 34-38
    Unknown1019(10)
    sprite('pt208_08', 3)	# 39-41
    Unknown1019(0)
    sprite('pt208_09', 3)	# 42-44
    sprite('pt208_10', 3)	# 45-47
    ExitState()
    label(100)
    sprite('pt405_00', 2)	# 48-49
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('pt405_01', 2)	# 50-51
    sprite('pt405_02', 2)	# 52-53
    sprite('pt405_03', 2)	# 54-55
    sprite('pt405_04', 2)	# 56-57
    if (not SLOT_7):
        Unknown7006('bpt207_0', 100, 846491746, 811546672, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt207_1', 100, 846491746, 828323888, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt405_05', 1)	# 58-58
    physicsXImpulse(-30000)
    GFX_0('SpMissile', 1)
    Unknown38(4, 1)
    Unknown23029(4, 1301, 1)
    GFX_1('ptef_throwsmoke', 0)
    sprite('pt405_05', 2)	# 59-60
    Unknown1019(70)
    sprite('pt405_05', 2)	# 61-62
    Unknown1019(50)
    sprite('pt405_05', 2)	# 63-64
    Unknown1019(30)
    sprite('pt405_06', 2)	# 65-66
    Unknown1019(10)
    sprite('pt208_08', 2)	# 67-68
    Unknown1019(0)
    sprite('pt208_00', 2)	# 69-70
    Unknown1084(1)
    sprite('pt405_01', 2)	# 71-72
    sprite('pt405_02', 2)	# 73-74
    sprite('pt405_03', 2)	# 75-76
    sprite('pt405_04', 2)	# 77-78
    sprite('pt405_05', 1)	# 79-79
    physicsXImpulse(-30000)
    GFX_0('SpMissile', 1)
    Unknown38(4, 1)
    Unknown23029(4, 1301, 1)
    GFX_1('ptef_throwsmoke', 0)
    sprite('pt405_05', 2)	# 80-81
    Unknown1019(70)
    sprite('pt405_05', 2)	# 82-83
    Unknown1019(50)
    sprite('pt405_05', 2)	# 84-85
    Unknown1019(30)
    sprite('pt405_06', 2)	# 86-87
    Unknown1019(10)
    sprite('pt208_08', 2)	# 88-89
    Unknown1019(0)
    sprite('pt208_00', 2)	# 90-91
    Unknown1084(1)
    sprite('pt405_01', 2)	# 92-93
    sprite('pt405_02', 2)	# 94-95
    sprite('pt405_03', 2)	# 96-97
    sprite('pt405_04', 2)	# 98-99
    sprite('pt405_05', 1)	# 100-100
    physicsXImpulse(-30000)
    GFX_0('SpMissile', 1)
    Unknown38(4, 1)
    Unknown23029(4, 1303, 1)
    GFX_1('ptef_throwsmoke', 0)
    callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 3)	# 101-103
    Unknown1019(70)
    sprite('pt405_05', 4)	# 104-107
    Unknown1019(50)
    sprite('pt405_05', 4)	# 108-111
    Unknown1019(30)
    sprite('pt405_06', 3)	# 112-114
    Unknown1019(10)
    sprite('pt208_08', 3)	# 115-117
    Unknown1019(0)
    sprite('pt208_09', 3)	# 118-120
    sprite('pt208_10', 3)	# 121-123
    ExitState()

@State
def AirDriveShot_Ex():

    def upon_IMMEDIATE():
        Unknown17003()
        SLOT_4 = 1
        SLOT_59 = 9
    sprite('pt208_00', 2)	# 1-2
    Unknown1084(1)
    sprite('keep', 1)	# 3-3
    if SLOT_5:
        sendToLabel(100)
    sprite('pt405_00', 1)	# 4-4
    Unknown1084(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    Unknown1019(20)
    setGravity(1500)
    Unknown22004(10, 1)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('pt405_00', 2)	# 5-6
    sprite('pt405_01', 3)	# 7-9
    sprite('pt405_02', 3)	# 10-12
    sprite('pt405_03', 3)	# 13-15
    sprite('pt405_01', 3)	# 16-18
    sprite('pt405_02', 1)	# 19-19
    sprite('pt405_04', 3)	# 20-22
    if (not SLOT_7):
        Unknown7006('bpt207_0', 100, 846491746, 811546672, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt207_1', 100, 846491746, 828323888, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt405_05', 3)	# 23-25
    GFX_0('Bomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1401, 0)
    GFX_1('ptef_throwsmokeshort', 0)
    sprite('pt405_05', 3)	# 26-28
    GFX_0('Bomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1402, 0)
    Unknown21007(1, 33)
    GFX_1('ptef_throwsmokeshort', 1)
    sprite('pt405_05', 4)	# 29-32
    GFX_0('Bomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1403, 0)
    GFX_1('ptef_throwsmokeshort', 2)
    sprite('pt405_06', 8)	# 33-40
    sprite('pt208_08', 3)	# 41-43
    Recovery()
    callSubroutine('StuffColorReset')
    sprite('pt208_09', 3)	# 44-46
    sprite('pt208_10', 3)	# 47-49
    label(0)
    sprite('pt020_07', 4)	# 50-53
    sprite('pt020_08', 4)	# 54-57
    loopRest()
    gotoLabel(0)
    ExitState()
    label(100)
    sprite('pt405_00', 3)	# 58-60
    Unknown1084(1)
    physicsYImpulse(22000)
    physicsXImpulse(-10000)
    Unknown1019(20)
    setGravity(1500)
    Unknown22004(10, 1)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('pt405_01', 3)	# 61-63
    setGravity(1500)
    sprite('pt405_02', 3)	# 64-66
    sprite('pt405_03', 3)	# 67-69
    sprite('pt208_02', 3)	# 70-72
    sprite('pt208_03', 1)	# 73-73
    sprite('pt405_04', 2)	# 74-75
    if (not SLOT_7):
        Unknown7006('bpt207_0', 100, 846491746, 811546672, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('bpt207_1', 100, 846491746, 828323888, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt405_04', 1)	# 76-76
    GFX_1('ptef_throwsmoke', 2)
    SFX_0('016_explode_0')
    SFX_3('ptse_01')
    sprite('pt405_05', 1)	# 77-77
    physicsXImpulse(-10000)
    GFX_0('SpBomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1401, 0)
    sprite('pt405_05', 2)	# 78-79
    physicsXImpulse(-10000)
    Unknown1019(70)
    sprite('pt405_05', 3)	# 80-82
    GFX_0('SpBomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1402, 0)
    sprite('pt405_05', 4)	# 83-86
    GFX_0('SpBomb', 0)
    Unknown38(4, 1)
    Unknown23029(4, 1403, 0)
    sprite('pt405_06', 8)	# 87-94
    Unknown1019(30)
    sprite('pt208_08', 3)	# 95-97
    Recovery()
    callSubroutine('StuffColorReset')
    sprite('pt208_09', 3)	# 98-100
    sprite('pt208_10', 3)	# 101-103
    label(101)
    sprite('pt020_07', 4)	# 104-107
    sprite('pt020_08', 4)	# 108-111
    loopRest()
    gotoLabel(101)
    ExitState()

@State
def HiWeapon():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)
    sprite('pt430_00', 3)	# 1-3
    setInvincible(1)
    Unknown2036(125, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown23083(1)
    Unknown30080('')
    sprite('pt430_01', 3)	# 4-6
    sprite('pt430_02', 3)	# 7-9
    if (not SLOT_7):
        SFX_1('bpt250_0')
    else:
        SFX_1('bpt250_1')
    sprite('pt430_03', 3)	# 10-12
    sprite('pt430_04', 3)	# 13-15
    sprite('pt430_05', 3)	# 16-18
    sprite('pt430_06', 3)	# 19-21
    sprite('pt430_07', 3)	# 22-24
    GFX_0('pt430_mahojin', 0)
    GFX_0('pt203_mahojinsub', 0)
    GFX_0('pt430_circle1', 1)
    GFX_0('pt430_circle2', 1)
    sprite('pt430_08', 3)	# 25-27
    sprite('pt430_09', 3)	# 28-30
    sprite('pt430_10', 3)	# 31-33
    sprite('pt430_11', 3)	# 34-36
    GFX_0('ptef_430power', 0)
    sprite('pt430_12', 3)	# 37-39
    sprite('pt430_13', 3)	# 40-42
    sprite('pt203_02', 40)	# 43-82
    GFX_0('pt430_mahojinsub', 0)
    GFX_0('pt430_aura1', 0)
    GFX_0('pt430_aura2', 0)
    GFX_0('pt430_aura3', 0)
    sprite('pt203_03', 3)	# 83-85
    GFX_0('pt430_stick', 0)
    Unknown21012('5370686572654c696768745f4d6f64656c00000000000000000000000000000020000000')
    SFX_3('ptse_13')
    SLOT_5 = 1
    SLOT_31 = 60000
    sprite('pt203_04', 3)	# 86-88
    sprite('pt203_05', 30)	# 89-118
    sprite('pt203_06', 3)	# 119-121
    sprite('pt203_07', 3)	# 122-124
    sprite('pt203_08', 2)	# 125-126
    sprite('pt203_08', 1)	# 127-127
    setInvincible(0)
    sprite('pt203_09', 3)	# 128-130
    sprite('pt203_10', 3)	# 131-133
    sprite('pt203_11', 3)	# 134-136

@State
def HiWeapon_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)
    sprite('pt430_00', 3)	# 1-3
    setInvincible(1)
    Unknown2036(125, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown23083(1)
    Unknown30080('')
    sprite('pt430_01', 3)	# 4-6
    sprite('pt430_02', 3)	# 7-9
    if (not SLOT_7):
        SFX_1('bpt250_0')
    else:
        SFX_1('bpt250_1')
    sprite('pt430_03', 3)	# 10-12
    sprite('pt430_04', 3)	# 13-15
    sprite('pt430_05', 3)	# 16-18
    sprite('pt430_06', 3)	# 19-21
    sprite('pt430_07', 3)	# 22-24
    GFX_0('pt430_mahojin', 0)
    GFX_0('pt203_mahojinsub', 0)
    GFX_0('pt430_circle1', 1)
    GFX_0('pt430_circle2', 1)
    sprite('pt430_08', 3)	# 25-27
    sprite('pt430_09', 3)	# 28-30
    sprite('pt430_10', 3)	# 31-33
    sprite('pt430_11', 3)	# 34-36
    GFX_0('ptef_430power', 0)
    sprite('pt430_12', 3)	# 37-39
    sprite('pt430_13', 3)	# 40-42
    sprite('pt203_02', 40)	# 43-82
    GFX_0('pt430_mahojinsub', 0)
    GFX_0('pt430_aura1', 0)
    GFX_0('pt430_aura2', 0)
    GFX_0('pt430_aura3', 0)
    sprite('pt203_03', 3)	# 83-85
    GFX_0('pt430_stick', 0)
    Unknown21012('5370686572654c696768745f4d6f64656c00000000000000000000000000000020000000')
    SFX_3('ptse_13')
    SLOT_5 = 1
    SLOT_31 = 60000
    sprite('pt203_04', 3)	# 86-88
    sprite('pt203_05', 30)	# 89-118
    sprite('pt203_06', 3)	# 119-121
    sprite('pt203_07', 3)	# 122-124
    sprite('pt203_08', 2)	# 125-126
    sprite('pt203_08', 1)	# 127-127
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('pt203_09', 3)	# 128-130
    sprite('pt203_10', 3)	# 131-133
    sprite('pt203_11', 3)	# 134-136

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(990)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        MinimumDamagePct(14)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(-6000)
        AirPushbackY(18000)
        AirUntechableTime(100)
        hitstun(100)
        Unknown1084(1)
        if SLOT_37:
            sendToLabel(100)
        if SLOT_36:
            sendToLabel(101)
            Unknown23159('UltimateAssaultAir')
        setInvincible(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    label(101)
    sprite('pt431_03', 3)	# 2-4
    sprite('pt431_03', 1)	# 5-5
    if (not SLOT_7):
        SFX_1('bpt251_0')
    else:
        SFX_1('bpt251_1')
    Unknown2036(70, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('pt431_03', 2)	# 6-7
    gotoLabel(102)
    label(100)
    sprite('pt431_00', 3)	# 8-10
    sprite('pt431_00', 3)	# 11-13
    if (not SLOT_7):
        SFX_1('bpt251_0')
    else:
        SFX_1('bpt251_1')
    Unknown2036(76, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('pt431_01', 3)	# 14-16
    sprite('pt431_02', 3)	# 17-19
    label(102)
    sprite('pt431_03', 5)	# 20-24
    sprite('pt431_04', 3)	# 25-27
    GFX_0('pt431_aura3', -1)
    GFX_0('pt431_aura3', -1)
    sprite('pt431_05', 40)	# 28-67
    GFX_0('pt431_startcircle', 0)
    GFX_0('ptef_431aura', 0)
    GFX_0('pt431_floorcircle', -1)
    sprite('pt431_05', 10)	# 68-77
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    sprite('pt431_06', 3)	# 78-80
    GFX_0('pt431_tornado', -1)
    sprite('pt431_07', 3)	# 81-83

    def upon_16():
        if (not SLOT_38):
            if (SLOT_40 >= 10000):
                Unknown1015(500)
            if (SLOT_40 < (-10000)):
                Unknown1015(-500)
            Unknown1019(95)
            YAccel(95)
        else:
            if (SLOT_40 >= 10000):
                Unknown1015(-500)
            if (SLOT_40 < (-10000)):
                Unknown1015(500)
            Unknown1019(95)
            YAccel(95)
        if SLOT_51:
            setGravity(700)
    sprite('pt431_08', 3)	# 84-86
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_09', 3)	# 87-89
    sprite('pt431_10', 1)	# 90-90	 **attackbox here**
    sprite('pt431_10', 3)	# 91-93	 **attackbox here**
    sprite('pt431_11', 3)	# 94-96
    sprite('pt431_12', 3)	# 97-99
    sprite('pt431_13', 3)	# 100-102
    sprite('pt431_09', 3)	# 103-105
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_10', 4)	# 106-109	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    sprite('pt431_11', 3)	# 110-112
    sprite('pt431_12', 3)	# 113-115
    sprite('pt431_13', 3)	# 116-118
    AirPushbackX(-5000)
    AirPushbackY(8000)
    Unknown30056('a08601003200000000000000')
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 119-121	 **attackbox here**
    SLOT_51 = 1
    GFX_0('pt431_ranbucircle', -1)
    GFX_0('pt431_tornado', -1)
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    GFX_0('pt431_smoke', -1)
    if (not SLOT_7):
        SFX_1('bpt252_0')
    else:
        SFX_1('bpt252_1')
    sprite('pt431_15', 3)	# 122-124	 **attackbox here**
    sprite('pt431_16', 3)	# 125-127	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 128-130	 **attackbox here**
    sprite('pt431_15', 3)	# 131-133	 **attackbox here**
    sprite('pt431_16', 3)	# 134-136	 **attackbox here**
    Hitstop(0)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 137-139	 **attackbox here**
    sprite('pt431_15', 3)	# 140-142	 **attackbox here**
    sprite('pt431_16', 3)	# 143-145	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 146-148	 **attackbox here**
    sprite('pt431_15', 3)	# 149-151	 **attackbox here**
    sprite('pt431_16', 3)	# 152-154	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 155-157	 **attackbox here**
    sprite('pt431_15', 3)	# 158-160	 **attackbox here**
    sprite('pt431_16', 3)	# 161-163	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 164-166	 **attackbox here**
    sprite('pt431_15', 3)	# 167-169	 **attackbox here**
    sprite('pt431_16', 3)	# 170-172	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 173-175	 **attackbox here**
    sprite('pt431_15', 3)	# 176-178	 **attackbox here**
    sprite('pt431_16', 3)	# 179-181	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 182-184	 **attackbox here**
    sprite('pt431_15', 3)	# 185-187	 **attackbox here**
    sprite('pt431_16', 3)	# 188-190	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 191-193	 **attackbox here**
    sprite('pt431_15', 3)	# 194-196	 **attackbox here**
    sprite('pt431_16', 3)	# 197-199	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 200-202	 **attackbox here**
    sprite('pt431_15', 3)	# 203-205	 **attackbox here**
    sprite('pt431_16', 3)	# 206-208	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 209-211	 **attackbox here**
    sprite('pt431_15', 3)	# 212-214	 **attackbox here**
    sprite('pt431_16', 3)	# 215-217	 **attackbox here**

    def upon_12():
        Unknown2038(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(30000)
    AirPushbackY(24000)
    YImpluseBeforeWallbounce(1000)
    AirUntechableTime(150)
    Unknown9310(36)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_16', 2)	# 218-219	 **attackbox here**
    label(5)
    sprite('pt431_14', 3)	# 220-222	 **attackbox here**
    setGravity(1200)
    DisableAttackRestOfMove()
    clearUponHandler(16)

    def upon_CLEAR_OR_EXIT():
        if SLOT_37:
            sendToLabel(10)
    sprite('pt431_15', 3)	# 223-225	 **attackbox here**
    sprite('pt431_16', 3)	# 226-228	 **attackbox here**
    gotoLabel(5)
    label(10)
    sprite('pt431_17', 5)	# 229-233
    clearUponHandler(3)
    sprite('pt431_18', 5)	# 234-238

    def upon_16():
        Unknown1019(90)
    sprite('pt431_19', 5)	# 239-243
    sprite('pt431_20', 5)	# 244-248
    sprite('pt431_21', 5)	# 249-253
    sprite('pt431_22', 5)	# 254-258
    loopRest()
    Unknown1084(1)
    if SLOT_2:
        gotoLabel(0)
    sprite('pt431_31', 7)	# 259-265
    sprite('pt431_32', 7)	# 266-272
    ExitState()
    label(0)
    sprite('pt431_23', 6)	# 273-278
    if (not SLOT_7):
        SFX_1('bpt253_0')
    else:
        SFX_1('bpt253_1')
    GFX_0('pt203_mahojin', -1)
    GFX_0('pt203_mahojinsub', -1)
    GFX_0('pt203_aura1', -1)
    GFX_0('pt203_aura2', -1)
    GFX_0('pt203_aura3', -1)
    sprite('pt431_24', 6)	# 279-284
    sprite('pt431_25', 6)	# 285-290
    sprite('pt431_26', 6)	# 291-296
    sprite('pt431_27', 8)	# 297-304
    GFX_0('pt203_stick', 0)
    SFX_3('ptse_13')
    sprite('pt431_27', 8)	# 305-312
    sprite('pt431_27', 8)	# 313-320
    sprite('pt431_27', 8)	# 321-328
    sprite('pt431_28', 6)	# 329-334
    sprite('pt431_29', 6)	# 335-340
    sprite('pt431_30', 6)	# 341-346
    ExitState()

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        MinimumDamagePct(13)
        Unknown11050('06000000707465665f6869745f6d6964646c650000000000000000000000000000000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(-6000)
        AirPushbackY(18000)
        AirUntechableTime(100)
        hitstun(100)
        Unknown11110(80)
        Unknown1084(1)
        if SLOT_37:
            sendToLabel(100)
        if SLOT_36:
            Unknown23159('UltimateAssaultAir_OD')
            sendToLabel(101)
        setInvincible(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    label(101)
    sprite('pt431_03', 3)	# 2-4
    sprite('pt431_03', 1)	# 5-5
    if (not SLOT_7):
        SFX_1('bpt251_0')
    else:
        SFX_1('bpt251_1')
    Unknown2036(70, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('pt431_03', 2)	# 6-7
    gotoLabel(102)
    label(100)
    sprite('pt431_00', 3)	# 8-10
    sprite('pt431_00', 3)	# 11-13
    if (not SLOT_7):
        SFX_1('bpt251_0')
    else:
        SFX_1('bpt251_1')
    Unknown2036(76, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('pt431_01', 3)	# 14-16
    sprite('pt431_02', 3)	# 17-19
    label(102)
    sprite('pt431_03', 5)	# 20-24
    sprite('pt431_04', 3)	# 25-27
    GFX_0('pt431_aura3', -1)
    GFX_0('pt431_aura3', -1)
    sprite('pt431_05', 40)	# 28-67
    GFX_0('pt431_startcircle', 0)
    GFX_0('ptef_431aura', 0)
    GFX_0('pt431_floorcircle', -1)
    sprite('pt431_05', 10)	# 68-77
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    sprite('pt431_06', 3)	# 78-80
    GFX_0('pt431_tornado', -1)
    sprite('pt431_07', 3)	# 81-83

    def upon_16():
        if (not SLOT_38):
            if (SLOT_40 >= 10000):
                Unknown1015(1500)
            if (SLOT_40 < (-10000)):
                Unknown1015(-1500)
            Unknown1019(90)
            YAccel(90)
        else:
            if (SLOT_40 >= 10000):
                Unknown1015(-1500)
            if (SLOT_40 < (-10000)):
                Unknown1015(1500)
            Unknown1019(90)
            YAccel(90)
        if SLOT_51:
            setGravity(700)
    sprite('pt431_08', 3)	# 84-86
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_09', 3)	# 87-89
    sprite('pt431_10', 1)	# 90-90	 **attackbox here**
    sprite('pt431_10', 3)	# 91-93	 **attackbox here**
    sprite('pt431_11', 3)	# 94-96
    sprite('pt431_12', 3)	# 97-99
    sprite('pt431_13', 3)	# 100-102
    sprite('pt431_09', 3)	# 103-105
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_10', 4)	# 106-109	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    sprite('pt431_11', 3)	# 110-112
    sprite('pt431_12', 3)	# 113-115
    sprite('pt431_13', 3)	# 116-118
    AirPushbackX(-5000)
    AirPushbackY(8000)
    Unknown30056('a08601003200000000000000')
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 119-121	 **attackbox here**
    SLOT_51 = 1
    GFX_0('pt431_ranbucircle', -1)
    GFX_0('pt431_tornado', -1)
    GFX_0('pt431_aura1', -1)
    GFX_0('pt431_aura2', -1)
    GFX_0('pt431_smoke', -1)
    if (not SLOT_7):
        SFX_1('bpt252_0')
    else:
        SFX_1('bpt252_1')
    sprite('pt431_15', 3)	# 122-124	 **attackbox here**
    sprite('pt431_16', 3)	# 125-127	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 128-129	 **attackbox here**
    sprite('pt431_15', 2)	# 130-131	 **attackbox here**
    sprite('pt431_16', 2)	# 132-133	 **attackbox here**
    Damage(670)
    Hitstop(0)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 134-135	 **attackbox here**
    sprite('pt431_15', 2)	# 136-137	 **attackbox here**
    sprite('pt431_16', 2)	# 138-139	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 140-141	 **attackbox here**
    sprite('pt431_15', 2)	# 142-143	 **attackbox here**
    sprite('pt431_16', 2)	# 144-145	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 146-147	 **attackbox here**
    sprite('pt431_15', 2)	# 148-149	 **attackbox here**
    sprite('pt431_16', 2)	# 150-151	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 152-153	 **attackbox here**
    sprite('pt431_15', 2)	# 154-155	 **attackbox here**
    sprite('pt431_16', 2)	# 156-157	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 158-159	 **attackbox here**
    sprite('pt431_15', 2)	# 160-161	 **attackbox here**
    sprite('pt431_16', 2)	# 162-163	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 164-165	 **attackbox here**
    sprite('pt431_15', 2)	# 166-167	 **attackbox here**
    sprite('pt431_16', 2)	# 168-169	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 170-171	 **attackbox here**
    sprite('pt431_15', 2)	# 172-173	 **attackbox here**
    sprite('pt431_16', 2)	# 174-175	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 176-177	 **attackbox here**
    sprite('pt431_15', 2)	# 178-179	 **attackbox here**
    sprite('pt431_16', 2)	# 180-181	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 182-183	 **attackbox here**
    sprite('pt431_15', 2)	# 184-185	 **attackbox here**
    sprite('pt431_16', 2)	# 186-187	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 188-189	 **attackbox here**
    sprite('pt431_15', 2)	# 190-191	 **attackbox here**
    sprite('pt431_16', 2)	# 192-193	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 194-195	 **attackbox here**
    sprite('pt431_15', 2)	# 196-197	 **attackbox here**
    sprite('pt431_16', 2)	# 198-199	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 200-201	 **attackbox here**
    sprite('pt431_15', 2)	# 202-203	 **attackbox here**
    sprite('pt431_16', 2)	# 204-205	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 206-207	 **attackbox here**
    sprite('pt431_15', 2)	# 208-209	 **attackbox here**
    sprite('pt431_16', 2)	# 210-211	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 212-213	 **attackbox here**
    sprite('pt431_15', 2)	# 214-215	 **attackbox here**
    sprite('pt431_16', 2)	# 216-217	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 218-219	 **attackbox here**
    sprite('pt431_15', 2)	# 220-221	 **attackbox here**
    sprite('pt431_16', 2)	# 222-223	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 224-225	 **attackbox here**
    sprite('pt431_15', 2)	# 226-227	 **attackbox here**
    sprite('pt431_16', 2)	# 228-229	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 230-231	 **attackbox here**
    sprite('pt431_15', 2)	# 232-233	 **attackbox here**
    sprite('pt431_16', 2)	# 234-235	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 236-237	 **attackbox here**
    sprite('pt431_15', 2)	# 238-239	 **attackbox here**
    sprite('pt431_16', 2)	# 240-241	 **attackbox here**
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 2)	# 242-243	 **attackbox here**
    sprite('pt431_15', 2)	# 244-245	 **attackbox here**
    sprite('pt431_16', 2)	# 246-247	 **attackbox here**

    def upon_12():
        Unknown2038(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(30000)
    AirPushbackY(24000)
    YImpluseBeforeWallbounce(1000)
    AirUntechableTime(150)
    Unknown9310(36)
    RefreshMultihit()
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_16', 2)	# 248-249	 **attackbox here**
    label(5)
    sprite('pt431_14', 3)	# 250-252	 **attackbox here**
    setGravity(1200)
    DisableAttackRestOfMove()
    clearUponHandler(16)

    def upon_CLEAR_OR_EXIT():
        if SLOT_37:
            sendToLabel(10)
    sprite('pt431_15', 3)	# 253-255	 **attackbox here**
    sprite('pt431_16', 3)	# 256-258	 **attackbox here**
    gotoLabel(5)
    label(10)
    sprite('pt431_17', 5)	# 259-263
    clearUponHandler(3)
    sprite('pt431_18', 5)	# 264-268

    def upon_16():
        Unknown1019(90)
    sprite('pt431_19', 5)	# 269-273
    sprite('pt431_20', 5)	# 274-278
    sprite('pt431_21', 5)	# 279-283
    sprite('pt431_22', 5)	# 284-288
    loopRest()
    Unknown1084(1)
    if SLOT_2:
        gotoLabel(0)
    sprite('pt431_31', 7)	# 289-295
    sprite('pt431_32', 7)	# 296-302
    ExitState()
    label(0)
    sprite('pt431_23', 6)	# 303-308
    if (not SLOT_7):
        SFX_1('bpt253_0')
    else:
        SFX_1('bpt253_1')
    GFX_0('pt203_mahojin', -1)
    GFX_0('pt203_mahojinsub', -1)
    GFX_0('pt203_aura1', -1)
    GFX_0('pt203_aura2', -1)
    GFX_0('pt203_aura3', -1)
    sprite('pt431_24', 6)	# 309-314
    sprite('pt431_25', 6)	# 315-320
    sprite('pt431_26', 6)	# 321-326
    sprite('pt431_27', 8)	# 327-334
    GFX_0('pt203_stick', 0)
    SFX_3('ptse_13')
    sprite('pt431_27', 8)	# 335-342
    sprite('pt431_27', 8)	# 343-350
    sprite('pt431_27', 8)	# 351-358
    sprite('pt431_28', 6)	# 359-364
    sprite('pt431_29', 6)	# 365-370
    sprite('pt431_30', 6)	# 371-376
    ExitState()

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11064(1)
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        Unknown11034(0)
        ProjectileDurabilityLvl(3)
        Unknown11058('0000000000000000000000000100000000000000')
        MinimumDamagePct(100)
        setInvincible(1)
        Unknown1084(1)
        Unknown11001(0, 525, 525)
        Unknown11072(3, 128000, 0)

        def upon_12():
            Unknown2037(1)
            Unknown23088(1, 1)
            Unknown23157(1)
            Unknown23024(3)
            Unknown23084(1)
            setInvincible(1)
    if SLOT_37:
        gotoLabel(0)
    if SLOT_36:
        Unknown23159('AstralHeatAir')
        gotoLabel(1)
    label(0)
    sprite('pt450_00', 4)	# 1-4
    if (not SLOT_7):
        SFX_1('bpt290_0')
    else:
        SFX_1('bpt290_1')
    gotoLabel(3)
    label(1)
    sprite('pt450_21', 4)	# 5-8
    if (not SLOT_7):
        SFX_1('bpt290_0')
    else:
        SFX_1('bpt290_1')
    gotoLabel(3)
    label(3)
    sprite('pt450_01', 1)	# 9-9
    sprite('pt450_01', 3)	# 10-12
    Unknown2036(69, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_PT_AH', -1)
    physicsYImpulse(900)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(1)
    Unknown3071(6)
    Unknown3074('00000000ff0000009600000096000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    sprite('pt450_02', 7)	# 13-19
    GFX_1('ptef_specialmc', -1)
    sprite('pt450_03', 7)	# 20-26
    sprite('pt450_04', 7)	# 27-33
    sprite('pt450_05', 7)	# 34-40
    sprite('pt450_06', 7)	# 41-47
    sprite('pt450_07', 7)	# 48-54
    sprite('pt450_08', 5)	# 55-59
    physicsYImpulse(0)
    sprite('pt450_09', 4)	# 60-63
    GFX_0('Astral1stBeam', 0)
    SFX_3('ptse_12')
    sprite('pt450_10', 3)	# 64-66
    SFX_3('ptse_09')
    SFX_3('ptse_09')
    sprite('pt450_11', 3)	# 67-69	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 70-72
    sprite('pt450_10', 3)	# 73-75
    sprite('pt450_11', 3)	# 76-78	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 79-81
    sprite('pt450_10', 3)	# 82-84
    sprite('pt450_11', 3)	# 85-87	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 88-90
    sprite('pt450_10', 3)	# 91-93
    sprite('pt450_11', 3)	# 94-96	 **attackbox here**
    ScreenShake(20000, 0)
    loopRest()
    if SLOT_2:
        gotoLabel(4)
    sprite('pt450_09', 3)	# 97-99
    setInvincible(0)
    Unknown21012('41737472616c3173744265616d0000000000000000000000000000000000000020000000')
    Unknown3029(0)
    sprite('pt450_22', 3)	# 100-102
    sprite('pt450_23', 3)	# 103-105
    Unknown1043()
    loopRest()
    ExitState()
    label(4)
    clearUponHandler(12)
    sprite('pt450_09', 3)	# 106-108
    GFX_0('AstralAura', -1)
    GFX_0('AstralAura02', -1)
    GFX_0('AstralMcircle', -1)
    sprite('pt450_10', 3)	# 109-111
    sprite('pt450_11', 3)	# 112-114	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 115-117
    sprite('pt450_10', 3)	# 118-120
    sprite('pt450_11', 3)	# 121-123	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 124-126
    Unknown23117(16777215, 9)
    sprite('pt450_10', 3)	# 127-129
    sprite('pt450_11', 3)	# 130-132	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 133-135
    Unknown23120()
    GFX_0('Fade1', -1)
    sprite('pt450_10', 3)	# 136-138
    sprite('pt450_11', 3)	# 139-141	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 142-144
    sprite('pt450_10', 3)	# 145-147
    sprite('pt450_11', 3)	# 148-150	 **attackbox here**
    if (not SLOT_7):
        SFX_1('bpt291_0')
    else:
        SFX_1('bpt291_1')
    StartMultihit()
    sprite('pt450_09', 3)	# 151-153
    sprite('pt450_10', 3)	# 154-156
    sprite('pt450_11', 3)	# 157-159	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 160-162
    GFX_0('pt450cutin_hand', -1)
    GFX_0('pt450cutin_handbg', -1)
    sprite('pt450_10', 3)	# 163-165
    sprite('pt450_11', 3)	# 166-168	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 169-171
    sprite('pt450_10', 3)	# 172-174
    sprite('pt450_11', 3)	# 175-177	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 178-180
    sprite('pt450_10', 3)	# 181-183
    sprite('pt450_11', 3)	# 184-186	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 187-189
    sprite('pt450_10', 3)	# 190-192
    sprite('pt450_11', 3)	# 193-195	 **attackbox here**
    sprite('pt450_09', 3)	# 196-198
    sprite('pt450_10', 3)	# 199-201
    sprite('pt450_11', 3)	# 202-204	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 205-207
    GFX_0('pt450cutin_leg', -1)
    GFX_0('pt450cutin_legbg', -1)
    sprite('pt450_10', 3)	# 208-210
    sprite('pt450_11', 3)	# 211-213	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 214-216
    sprite('pt450_10', 3)	# 217-219
    sprite('pt450_11', 3)	# 220-222	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 223-225
    sprite('pt450_10', 3)	# 226-228
    sprite('pt450_11', 3)	# 229-231	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 232-234
    sprite('pt450_10', 3)	# 235-237
    sprite('pt450_11', 3)	# 238-240	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 241-243
    sprite('pt450_10', 3)	# 244-246
    sprite('pt450_11', 3)	# 247-249	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 250-252
    GFX_0('pt450cutin_bustupbg', -1)
    sprite('pt450_10', 3)	# 253-255
    sprite('pt450_11', 3)	# 256-258	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 259-261
    GFX_0('pt450cutin_bustup', -1)
    sprite('pt450_10', 3)	# 262-264
    sprite('pt450_11', 3)	# 265-267	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 268-270
    sprite('pt450_10', 3)	# 271-273
    sprite('pt450_11', 3)	# 274-276	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 277-279
    sprite('pt450_10', 3)	# 280-282
    sprite('pt450_11', 3)	# 283-285	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 286-288
    sprite('pt450_10', 3)	# 289-291
    sprite('pt450_11', 3)	# 292-294	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 295-297
    sprite('pt450_10', 3)	# 298-300
    sprite('pt450_11', 3)	# 301-303	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 304-306
    sprite('pt450_10', 3)	# 307-309
    sprite('pt450_11', 3)	# 310-312	 **attackbox here**
    if (not SLOT_7):
        SFX_1('bpt292_0')
    else:
        SFX_1('bpt292_1')
    StartMultihit()
    sprite('pt450_09', 3)	# 313-315
    sprite('pt450_10', 3)	# 316-318
    sprite('pt450_11', 3)	# 319-321	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 322-324
    sprite('pt450_10', 3)	# 325-327
    sprite('pt450_11', 3)	# 328-330	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 331-333
    sprite('pt450_10', 3)	# 334-336
    sprite('pt450_11', 3)	# 337-339	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 340-342
    sprite('pt450_10', 3)	# 343-345
    sprite('pt450_11', 3)	# 346-348	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 349-351
    sprite('pt450_10', 3)	# 352-354
    sprite('pt450_11', 3)	# 355-357	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 358-360
    sprite('pt450_10', 3)	# 361-363
    sprite('pt450_11', 3)	# 364-366	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 367-369
    sprite('pt450_10', 3)	# 370-372
    sprite('pt450_11', 3)	# 373-375	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 376-378
    sprite('pt450_10', 3)	# 379-381
    sprite('pt450_11', 3)	# 382-384	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 385-387
    sprite('pt450_10', 3)	# 388-390
    sprite('pt450_11', 3)	# 391-393	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 394-396
    sprite('pt450_10', 3)	# 397-399
    sprite('pt450_11', 3)	# 400-402	 **attackbox here**
    StartMultihit()
    sprite('pt450_09', 3)	# 403-405
    sprite('pt450_10', 3)	# 406-408
    sprite('pt450_11', 3)	# 409-411	 **attackbox here**
    StartMultihit()
    GFX_1('ptef_450change2nd', 1)
    sprite('pt450_12', 3)	# 412-414	 **attackbox here**
    StartMultihit()
    GFX_0('pt450_mahojin1', -1)
    Unknown21012('41737472616c417572610000000000000000000000000000000000000000000020000000')
    Unknown21012('41737472616c3173744265616d0000000000000000000000000000000000000020000000')
    sprite('pt450_13', 3)	# 415-417
    Unknown23117(0, 9)
    sprite('pt450_14', 3)	# 418-420
    sprite('pt450_12', 3)	# 421-423	 **attackbox here**
    SFX_3('ptse_22')
    StartMultihit()
    sprite('pt450_13', 3)	# 424-426
    Unknown23120()
    sprite('pt450_14', 3)	# 427-429
    sprite('pt450_12', 3)	# 430-432	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 433-435
    sprite('pt450_14', 3)	# 436-438
    sprite('pt450_12', 3)	# 439-441	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 442-444
    sprite('pt450_14', 3)	# 445-447
    sprite('pt450_12', 3)	# 448-450	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 451-453
    sprite('pt450_14', 3)	# 454-456
    sprite('pt450_12', 3)	# 457-459	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 460-462
    sprite('pt450_14', 3)	# 463-465
    sprite('pt450_12', 3)	# 466-468	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 469-471
    sprite('pt450_14', 3)	# 472-474
    GFX_0('pt450_mahojin2', -1)
    GFX_0('pt450_mahojin3', -1)
    sprite('pt450_12', 3)	# 475-477	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 478-480
    if (not SLOT_7):
        SFX_1('bpt293_0')
    else:
        SFX_1('bpt293_1')
    sprite('pt450_14', 3)	# 481-483
    sprite('pt450_12', 3)	# 484-486	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 487-489
    sprite('pt450_14', 3)	# 490-492
    sprite('pt450_12', 3)	# 493-495	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 496-498
    sprite('pt450_14', 3)	# 499-501
    sprite('pt450_12', 3)	# 502-504	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 505-507
    sprite('pt450_14', 3)	# 508-510
    sprite('pt450_12', 3)	# 511-513	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 514-516
    sprite('pt450_14', 3)	# 517-519
    sprite('pt450_12', 3)	# 520-522	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 523-525
    sprite('pt450_14', 3)	# 526-528
    sprite('pt450_12', 3)	# 529-531	 **attackbox here**
    GFX_1('ptef_450second', 0)
    StartMultihit()
    sprite('pt450_13', 3)	# 532-534
    sprite('pt450_14', 3)	# 535-537
    sprite('pt450_12', 3)	# 538-540	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 541-543
    sprite('pt450_14', 3)	# 544-546
    sprite('pt450_12', 3)	# 547-549	 **attackbox here**
    GFX_0('pt450Beam', 3)
    StartMultihit()
    sprite('pt450_13', 3)	# 550-552
    sprite('pt450_14', 3)	# 553-555
    sprite('pt450_12', 3)	# 556-558	 **attackbox here**
    StartMultihit()
    sprite('pt450_13', 3)	# 559-561
    sprite('pt450_14', 3)	# 562-564
    sprite('pt450_12', 3)	# 565-567	 **attackbox here**
    ScreenShake(0, 90000)
    StartMultihit()
    sprite('pt450_13', 3)	# 568-570
    sprite('pt450_14', 3)	# 571-573
    sprite('pt450_12', 5)	# 574-578	 **attackbox here**
    RefreshMultihit()
    Damage(20000)
    Unknown11064(3)
    Unknown11023(1)
    Hitstop(0)
    YImpluseBeforeWallbounce(0)
    Unknown11072(3, 0, 0)
    Unknown11001(0, 2000, 2000)
    GroundedHitstunAnimation(4)
    sprite('pt450_12', 15)	# 579-593	 **attackbox here**
    StartMultihit()
    sprite('pt450_12', 15)	# 594-608	 **attackbox here**
    StartMultihit()
    GFX_0('FadeWhite', -1)
    sprite('pt450_13', 45)	# 609-653
    Unknown23024(0)
    Unknown20000(1)
    Unknown20003(1)
    Unknown20004(1)
    teleportRelativeY(70000)
    Unknown1000(0)
    Unknown21012('41737472616c417572613032000000000000000000000000000000000000000020000000')
    Unknown3029(0)
    setInvincible(0)
    Unknown36(22)
    Unknown3038(1)
    teleportRelativeY(4000000)
    Unknown1000(1865000)
    Unknown35()
    sprite('pt450_13', 15)	# 654-668
    GFX_0('AstralAuraWin', -1)
    sprite('pt450_14', 6)	# 669-674
    sprite('pt450_15', 6)	# 675-680
    sprite('pt450_16', 6)	# 681-686
    sprite('pt450_17', 6)	# 687-692
    sprite('pt450_18', 6)	# 693-698
    sprite('pt450_19', 6)	# 699-704
    sprite('pt450_20', 6)	# 705-710
    Unknown18010()
    if SLOT_43:
        Unknown21011(240)
    else:
        Unknown21011(290)
    sprite('pt450_18', 6)	# 711-716
    Unknown4045('707465665f34353077696e00000000000000000000000000000000000000000000000000')
    SFX_3('ptse_16')
    sprite('pt450_19', 6)	# 717-722
    sprite('pt450_20', 6)	# 723-728
    sprite('pt450_18', 6)	# 729-734
    sprite('pt450_19', 6)	# 735-740
    if (not SLOT_7):
        SFX_1('bpt300_0')
    else:
        SFX_1('bpt300_1')
    sprite('pt450_20', 6)	# 741-746
    sprite('pt450_18', 6)	# 747-752
    sprite('pt450_19', 6)	# 753-758
    sprite('pt450_20', 6)	# 759-764
    label(5)
    sprite('pt450_18', 6)	# 765-770
    Unknown4045('707465665f34353077696e00000000000000000000000000000000000000000000000000')
    SFX_3('ptse_16')
    sprite('pt450_19', 6)	# 771-776
    sprite('pt450_20', 6)	# 777-782
    sprite('pt450_18', 6)	# 783-788
    sprite('pt450_19', 6)	# 789-794
    sprite('pt450_20', 6)	# 795-800
    sprite('pt450_18', 6)	# 801-806
    sprite('pt450_19', 6)	# 807-812
    sprite('pt450_20', 6)	# 813-818
    gotoLabel(5)

@Subroutine
def MouthTableInit():
    Unknown18011('bpt000_0', 14689, 14179, 14433, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt000_1', 14689, 14435, 14177, 14179, 14177, 14435, 12641, 25395, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt500_0', 12643, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt500_0', '001')
    Unknown18011('bpt500_1', 12643, 12641, 25397, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt500_1', '002')
    Unknown18011('bpt501_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt501_0', '003')
    Unknown18011('bpt501_1', 12643, 12897, 25397, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt501_1', '004')
    Unknown18011('bpt502_0', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt502_0', '005')
    Unknown18011('bpt503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt503', '006')
    Unknown18011('bpt504_0', 12643, 12641, 25392, 14130, 14177, 14179, 14177, 14691, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt504_0', '007')
    Unknown18011('bpt504_1', 12643, 12897, 25394, 24887, 25399, 24887, 12850, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt504_1', '008')
    Unknown18011('bpt505_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt505_0', '009')
    Unknown18011('bpt505_1', 12643, 12641, 25395, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt505_1', '010')
    Unknown18011('bpt520', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 13617, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt520', '011')
    Unknown18011('bpt521', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt521', '012')
    Unknown18011('bpt522_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 14132, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt522_0', '013')
    Unknown18011('bpt522_1', 12643, 12897, 25392, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt522_1', '014')
    Unknown18011('bpt523_0', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt523_0', '015')
    Unknown18011('bpt523_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 12853, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13618, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt523_1', '016')
    Unknown18011('bpt524_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt524_0', '017')
    Unknown18011('bpt524_1', 12643, 12897, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt524_1', '018')
    Unknown18011('bpt525_0', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt525_0', '019')
    Unknown18011('bpt525_1', 12643, 13665, 13667, 14177, 14691, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt525_1', '020')
    Unknown18011('bpt402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt403_0', 14689, 14179, 14433, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt403_1', 14689, 14179, 14433, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt602', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600bes_1', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 14133, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600bes_2', 12643, 12897, 25392, 12342, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600bhz', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600bjb_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 13363, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600bjb_2', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600brg_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600brg_2', 12643, 14177, 14179, 12897, 25392, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600pce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 12851, 14177, 14179, 14177, 14179, 14177, 14691, 12897, 25392, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 25397, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt601pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt601rwi', 12643, 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600uli', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt601uyu', 12643, 12897, 13617, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600bce', 12899, 14433, 14435, 14433, 14435, 14433, 13155, 24884, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 12337, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt600pku', 13411, 14177, 14179, 14177, 14179, 12897, 25392, 24887, 25398, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12594, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt601ahe', 12643, 12641, 25392, 24887, 25399, 24887, 25398, 24886, 25398, 13873, 14177, 14179, 14177, 14179, 13921, 13923, 12641, 25394, 24887, 25399, 24887, 25398, 24886, 12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt602', '025')
    Unknown30092('bpt600bes_1', '026')
    Unknown30092('bpt600bes_2', '027')
    Unknown30092('bpt600bhz', '028')
    Unknown30092('bpt600bjb_1', '029')
    Unknown30092('bpt600bjb_2', '030')
    Unknown30092('bpt600brg_1', '031')
    Unknown30092('bpt600brg_2', '032')
    Unknown30092('bpt600pce', '033')
    Unknown30092('bpt600pla', '034')
    Unknown30092('bpt600uli', '035')
    Unknown30092('bpt601pyo', '036')
    Unknown30092('bpt601rwi', '037')
    Unknown30092('bpt601uyu', '038')
    Unknown30092('bpt600bce', '039')
    Unknown30092('bpt600pku', '040')
    Unknown30092('bpt601ahe', '041')
    Unknown18011('bpt701bes_1', 12643, 14177, 13155, 24880, 25397, 24885, 13617, 13155, 24887, 25399, 24887, 13617, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 13620, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt701bes_2', 12643, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt701bhz', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13619, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700bjb_1', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700bjb_2', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 25392, 14133, 14177, 14179, 14177, 12899, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700brg_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700brg_2', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700pce', 12643, 14177, 12643, 24882, 12339, 14179, 14177, 13155, 24887, 25399, 24887, 13618, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12339, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700pyo', 12643, 14177, 12643, 24882, 12341, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt700rwi', 12643, 14177, 13155, 24880, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 12338, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 13618, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt701uli', 12643, 14177, 12899, 24882, 25397, 24885, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt701uyu', 12643, 12641, 12338, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt701bce', 12899, 12641, 25394, 13874, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 12899, 24882, 14129, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt701pku', 12643, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25398, 24886, 25398, 12594, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt701ahe', 14177, 14179, 12641, 25399, 13874, 12641, 25394, 12849, 13921, 13923, 13921, 13923, 13921, 13923, 14433, 14435, 14433, 14435, 13921, 13923, 13921, 13923, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt700bjb_1', '042')
    Unknown30092('bpt700bjb_2', '043')
    Unknown30092('bpt700brg_1', '044')
    Unknown30092('bpt700brg_2', '045')
    Unknown30092('bpt700pce', '046')
    Unknown30092('bpt700pla', '047')
    Unknown30092('bpt700pyo', '048')
    Unknown30092('bpt700rwi', '049')
    Unknown30092('bpt701bes_1', '050')
    Unknown30092('bpt701bes_2', '051')
    Unknown30092('bpt701bhz', '052')
    Unknown30092('bpt701uli', '053')
    Unknown30092('bpt701uyu', '054')
    Unknown30092('bpt700bce', '055')
    Unknown30092('bpt701bce', '056')
    Unknown30092('bpt701pku', '057')
    Unknown30092('bpt701ahe', '058')
    Unknown18011('bpt292_0', 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt292_1', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt300_0', 12643, 13155, 14177, 12899, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 24887, 25399, 25394, 24881, 25399, 25393, 24882, 25399, 24887, 25399, 24887, 25397, 24881, 25399, 24887, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bpt300_1', 12643, 13155, 13921, 13155, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 13409, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bpt300_0', '059')
    Unknown30092('bpt300_1', '060')
    if SLOT_172:
        Unknown18011('bpt000_0', 14689, 14179, 14433, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt000_1', 14689, 14435, 14177, 14179, 14177, 14435, 12641, 25395, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt500_0', 12643, 12643, 14177, 13923, 13411, 13921, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt500_1', 12643, 13667, 14177, 14179, 13409, 13155, 14177, 14179, 14177, 13155, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt501_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt501_1', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14177, 13411, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt502_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt503', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12899, 14177, 14179, 14177, 14179, 13921, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt504_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 13411, 14177, 14179, 14177, 14179, 13409, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt504_1', 12643, 13411, 14177, 13923, 14691, 14177, 14179, 14177, 14179, 14177, 12643, 13921, 13411, 12641, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt505_0', 12643, 12643, 14177, 13923, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 14177, 14179, 14177, 14179, 13153, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt505_1', 12643, 13667, 14177, 12899, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt520', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14435, 14177, 14179, 14177, 12899, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 14177, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt521', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt522_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 24889, 25399, 24887, 25394, 24888, 25399, 24887, 25399, 24887, 25399, 24883, 25399, 25399, 24881, 25399, 24887, 25399, 24887, 25395, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt522_1', 12643, 13411, 14177, 14179, 14177, 14179, 12641, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt523_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt523_1', 12643, 12899, 14177, 13411, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt524_0', 12643, 12643, 14177, 12899, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt524_1', 12643, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt525_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 24882, 25399, 24887, 25399, 25397, 24882, 25399, 24887, 25399, 24887, 25396, 24882, 25399, 24887, 25399, 24887, 25399, 13361, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt525_1', 12643, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14179, 14177, 12899, 12899, 14177, 14179, 14177, 14179, 13921, 13155, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt402_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt402_1', 12643, 12643, 14177, 14179, 14177, 13667, 13667, 14177, 14179, 14177, 14179, 13409, 12899, 14177, 14179, 14177, 14179, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt403_0', 12643, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt403_1', 12643, 12899, 14177, 14179, 13665, 12899, 12641, 13155, 24884, 25399, 24887, 25399, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt602', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 24880, 25399, 25394, 24883, 25399, 24887, 25397, 24882, 25399, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 13105, 14177, 14179, 14177, 13667, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600bes_1', 12643, 12643, 14177, 14179, 12897, 13155, 13153, 12643, 24886, 25399, 24887, 25399, 24887, 25399, 25399, 24882, 25399, 24887, 25399, 24887, 25399, 25398, 24882, 25396, 13108, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600bes_2', 12643, 13923, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 25395, 24884, 25395, 12596, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600bhz', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 13153, 13411, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 14130, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600bjb_1', 12643, 12899, 14177, 14179, 14177, 14179, 12897, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 24882, 25399, 24887, 25399, 24887, 25399, 25395, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600bjb_2', 12643, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 13667, 12899, 24884, 25399, 24887, 25396, 24881, 25399, 24887, 25397, 24886, 25399, 24887, 25393, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600brg_1', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600brg_2', 12643, 14691, 14177, 14179, 14177, 14179, 12897, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24889, 25399, 24887, 25399, 24887, 25399, 25393, 24886, 25399, 24887, 25399, 24887, 25394, 13105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600pce', 12643, 12643, 14177, 14179, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 12641, 12643, 24884, 25399, 24887, 25399, 24883, 25399, 25397, 24885, 25399, 24887, 25399, 24887, 25399, 25398, 24887, 25399, 24887, 25399, 24887, 25399, 24881, 25399, 24887, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600pla', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13155, 13665, 12643, 24886, 25399, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24883, 25399, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt601pyo', 12643, 13155, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 14179, 13409, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt601rwi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13411, 13153, 12643, 24880, 25399, 24887, 25399, 24887, 25393, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24882, 25399, 25397, 24884, 25399, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600uli', 12643, 12899, 14177, 14179, 14177, 14179, 12897, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13155, 14177, 12899, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24882, 25399, 25396, 24881, 25399, 25394, 24881, 25399, 24887, 25393, 24883, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt601uyu', 12643, 12643, 14177, 14179, 14177, 13411, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 14177, 14179, 14177, 13155, 12643, 13921, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600bce', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt600pku', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 14179, 14177, 14179, 14177, 14179, 12641, 13411, 14177, 14179, 12897, 12643, 12897, 12899, 13665, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt601ahe', 12643, 12643, 14177, 14179, 14177, 14179, 12643, 14177, 13667, 12643, 14177, 14179, 13409, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 14177, 14179, 13153, 13667, 13409, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701bes_1', 12643, 13155, 14177, 14179, 12897, 13155, 14177, 14179, 14177, 14179, 13665, 12899, 12641, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701bes_2', 12643, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701bhz', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24882, 25393, 14386, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700bjb_1', 12643, 12643, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700bjb_2', 12643, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13155, 24882, 25399, 25394, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700brg_1', 12643, 12643, 14177, 14179, 14177, 13411, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 24888, 25399, 25396, 24883, 25399, 24887, 25399, 24887, 25399, 25394, 12849, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700brg_2', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 13409, 12899, 24882, 25399, 24887, 25399, 25399, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 24881, 25399, 24887, 25399, 24887, 25396, 14641, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700pce', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 13665, 12643, 24885, 25399, 24887, 25399, 24887, 25396, 24883, 25399, 24887, 25399, 24887, 25394, 24883, 25397, 13105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700pla', 12643, 12899, 14177, 13667, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 13921, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700pyo', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14179, 14177, 13155, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt700rwi', 12643, 12643, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 24887, 25399, 25399, 24883, 25399, 24887, 25399, 25396, 24884, 25399, 25399, 24882, 25399, 24887, 25399, 24887, 25399, 25395, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701uli', 12643, 13923, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 24882, 25399, 24887, 25399, 24887, 25393, 12337, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 14177, 14179, 14177, 14179, 14177, 13667, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701uyu', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13411, 14177, 14179, 14177, 14179, 13155, 13921, 12643, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701bce', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 13411, 14177, 14179, 12899, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 14179, 14177, 12643, 24889, 25399, 25395, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701pku', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24885, 25399, 24887, 25395, 24883, 25399, 24887, 25399, 24887, 25393, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt701ahe', 12643, 12643, 14177, 14179, 14177, 14179, 13153, 13155, 13921, 14691, 14177, 14179, 14177, 13411, 12643, 14177, 12643, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt292_0', 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt292_1', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt300_0', 12643, 12643, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 14179, 13409, 12643, 14177, 13923, 13155, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bpt300_1', 12643, 12643, 14177, 13667, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('62706800000000000000000000000000626a62000000000000000000000000006268610000000000000000000000000062707400000000000000000000000000'):
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
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bhz')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('bes')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bjb')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('pyo')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('pce')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('uli')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('rwi')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('uyu')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('pla')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('bce')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('ahe')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('pku')
    if SLOT_ReturnVal:
        _gotolabel(220)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 33)
    if SLOT_ReturnVal:
        _gotolabel(10)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(20)
    sprite('pt600_00', 39)	# 2-40
    tag_voice(1, 'bpt500_0', 'bpt501_0', 'bpt504_0', 'bpt505_0')
    label(1)
    sprite('pt600_00', 1)	# 41-41
    if SLOT_97:
        _gotolabel(1)
    sprite('pt600_00', 30)	# 42-71
    sprite('pt600_00', 1)	# 72-72
    tag_voice(0, 'bpt500_1', 'bpt501_1', 'bpt504_1', 'bpt505_1')
    label(2)
    sprite('pt600_00', 1)	# 73-73
    if SLOT_97:
        _gotolabel(2)
    sprite('pt600_00', 20)	# 74-93
    sprite('pt600_01', 6)	# 94-99
    sprite('pt600_02', 6)	# 100-105
    SFX_0('008_swing_pole_2')
    sprite('pt600_03', 6)	# 106-111
    sprite('pt600_04', 6)	# 112-117
    sprite('pt600_05', 7)	# 118-124
    SFX_0('008_swing_pole_2')
    sprite('pt600_06', 5)	# 125-129
    GFX_1('ptef_entrylightA', 0)
    sprite('pt600_07', 5)	# 130-134
    Unknown23119(13145800, 16, 2)
    sprite('pt600_08', 4)	# 135-138
    sprite('pt600_08', 3)	# 139-141
    GFX_1('ptef_entrylightB', 0)
    sprite('pt600_08', 3)	# 142-144
    sprite('pt600_09', 6)	# 145-150
    sprite('pt600_10', 15)	# 151-165	 **attackbox here**
    GFX_0('yugami_ring', 0)
    GFX_1('ptef_entrymc', 0)
    SFX_0('019_cloth_c')
    SFX_3('ptse_13')
    sprite('pt600_11', 6)	# 166-171	 **attackbox here**
    sprite('pt600_12', 5)	# 172-176	 **attackbox here**
    sprite('pt600_10ex00', 5)	# 177-181	 **attackbox here**
    sprite('pt600_11ex00', 5)	# 182-186	 **attackbox here**
    sprite('pt600_12ex00', 5)	# 187-191
    sprite('pt600_13', 6)	# 192-197
    sprite('pt600_14', 6)	# 198-203
    sprite('pt600_15', 6)	# 204-209
    sprite('pt600_16', 6)	# 210-215
    Unknown23018(1)
    label(3)
    sprite('pt000_00', 7)	# 216-222
    sprite('pt000_01', 7)	# 223-229
    sprite('pt000_02', 7)	# 230-236
    sprite('pt000_03', 7)	# 237-243
    sprite('pt000_04', 7)	# 244-250
    sprite('pt000_05', 7)	# 251-257
    sprite('pt000_06', 7)	# 258-264
    sprite('pt000_07', 7)	# 265-271
    sprite('pt000_08', 7)	# 272-278
    sprite('pt000_09', 7)	# 279-285
    sprite('pt000_10', 7)	# 286-292
    sprite('pt000_11', 7)	# 293-299
    sprite('pt000_12', 7)	# 300-306
    sprite('pt000_13', 7)	# 307-313
    gotoLabel(3)
    ExitState()
    label(10)
    sprite('pt601_00', 30)	# 314-343
    if random_(2, 0, 50):
        SFX_1('bpt503')
    else:
        Unknown2037(1)
    label(11)
    sprite('pt601_00', 1)	# 344-344
    if SLOT_97:
        _gotolabel(11)
    sprite('pt601_00', 15)	# 345-359
    GFX_1('ptef_entryheartA', 0)
    SFX_3('ptse_15')
    sprite('pt601_01', 6)	# 360-365
    sprite('pt601_02', 6)	# 366-371
    GFX_0('EntryHeart', 0)
    SFX_3('ptse_21')
    sprite('pt601_03', 6)	# 372-377
    sprite('pt601_04', 6)	# 378-383
    sprite('pt601_05', 6)	# 384-389
    sprite('pt601_06', 6)	# 390-395
    sprite('pt601_07', 6)	# 396-401
    sprite('pt601_05', 6)	# 402-407
    sprite('pt601_06', 6)	# 408-413
    sprite('pt601_07', 6)	# 414-419
    sprite('pt601_05', 6)	# 420-425
    sprite('pt601_06', 6)	# 426-431
    sprite('pt601_07', 6)	# 432-437
    sprite('pt601_05', 6)	# 438-443
    sprite('pt601_06', 6)	# 444-449
    GFX_0('EntryRod', -1)
    sprite('pt601_07', 6)	# 450-455
    sprite('pt601_08', 6)	# 456-461
    sprite('pt601_09', 6)	# 462-467
    sprite('pt601_10', 5)	# 468-472
    GFX_1('ptef_450light01', 0)
    SFX_0('003_swing_grap_0_1')
    SFX_0('100_hit_grap_0')
    sprite('pt601_11', 5)	# 473-477
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_12', 5)	# 478-482
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_13', 5)	# 483-487
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_14', 5)	# 488-492
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_15', 4)	# 493-496
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    sprite('pt601_16', 3)	# 497-499
    GFX_1('ptef_450light01', 0)
    sprite('pt601_17', 7)	# 500-506
    GFX_0('yugami_ring', 0)
    GFX_1('ptef_entrymc', 0)
    GFX_1('ptef_450light01', 0)
    SFX_3('ptse_13')
    sprite('pt601_18', 6)	# 507-512
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    if SLOT_2:
        SFX_1('bpt502_0')
    sprite('pt601_19', 6)	# 513-518
    label(12)
    sprite('pt601_20', 1)	# 519-519
    if SLOT_97:
        _gotolabel(12)
    sprite('pt601_20', 20)	# 520-539
    sprite('pt601_21', 6)	# 540-545
    sprite('pt601_22', 5)	# 546-550
    Unknown23018(1)
    label(13)
    sprite('pt000_00', 7)	# 551-557
    sprite('pt000_01', 7)	# 558-564
    sprite('pt000_02', 7)	# 565-571
    sprite('pt000_03', 7)	# 572-578
    sprite('pt000_04', 7)	# 579-585
    sprite('pt000_05', 7)	# 586-592
    sprite('pt000_06', 7)	# 593-599
    sprite('pt000_07', 7)	# 600-606
    sprite('pt000_08', 7)	# 607-613
    sprite('pt000_09', 7)	# 614-620
    sprite('pt000_10', 7)	# 621-627
    sprite('pt000_11', 7)	# 628-634
    sprite('pt000_12', 7)	# 635-641
    sprite('pt000_13', 7)	# 642-648
    gotoLabel(13)
    ExitState()
    label(20)
    sprite('pt331_05', 100)	# 649-748
    GFX_0('FusenEntry', -1)
    Unknown1000(-1461000)
    teleportRelativeY(350000)
    physicsXImpulse(1500)
    setGravity(7)
    Unknown3038(1)
    if random_(2, 0, 50):
        SFX_1('bpt500_0')
        SLOT_51 = 1
    else:
        SFX_1('bpt501_0')
        Unknown2037(1)
    sprite('pt331_05', 37)	# 749-785
    if SLOT_51:
        SFX_1('bpt500_1')
    sprite('pt331_05', 37)	# 786-822
    if SLOT_2:
        SFX_1('bpt501_1')
    sprite('pt331_06', 3)	# 823-825
    GFX_1('ptef_entrysmoke', 0)
    Unknown1084(1)
    physicsYImpulse(24000)
    Unknown3038(0)
    sprite('pt331_07', 4)	# 826-829
    YAccel(40)
    sprite('pt331_08', 6)	# 830-835
    setGravity(1300)
    sprite('pt331_06', 6)	# 836-841
    sprite('pt331_07', 6)	# 842-847
    sprite('pt331_08', 6)	# 848-853
    sprite('pt331_13', 6)	# 854-859
    physicsXImpulse(0)
    sendToLabelUpon(2, 22)
    sprite('pt331_14', 6)	# 860-865
    label(21)
    sprite('pt020_07', 6)	# 866-871
    sprite('pt020_08', 6)	# 872-877
    loopRest()
    gotoLabel(21)
    label(22)
    sprite('pt024_00', 3)	# 878-880
    Unknown1000(-1230000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('pt024_01', 9)	# 881-889
    sprite('pt024_02', 5)	# 890-894
    sprite('pt024_03', 5)	# 895-899
    sprite('pt024_04', 5)	# 900-904
    sprite('pt024_05', 5)	# 905-909
    sprite('pt000_00', 3)	# 910-912
    Unknown23018(1)
    label(23)
    sprite('pt000_00', 7)	# 913-919
    sprite('pt000_01', 7)	# 920-926
    sprite('pt000_02', 7)	# 927-933
    sprite('pt000_03', 7)	# 934-940
    sprite('pt000_04', 7)	# 941-947
    sprite('pt000_05', 7)	# 948-954
    sprite('pt000_06', 7)	# 955-961
    sprite('pt000_07', 7)	# 962-968
    sprite('pt000_08', 7)	# 969-975
    sprite('pt000_09', 7)	# 976-982
    sprite('pt000_10', 7)	# 983-989
    sprite('pt000_11', 7)	# 990-996
    sprite('pt000_12', 7)	# 997-1003
    sprite('pt000_13', 7)	# 1004-1010
    gotoLabel(23)
    ExitState()
    label(30)
    sprite('pt000_00', 1)	# 1011-1011
    SFX_1('bpt700pla')
    label(31)
    sprite('pt000_00', 7)	# 1012-1018
    sprite('pt000_01', 7)	# 1019-1025
    sprite('pt000_02', 7)	# 1026-1032
    sprite('pt000_03', 7)	# 1033-1039
    sprite('pt000_04', 7)	# 1040-1046
    sprite('pt000_05', 7)	# 1047-1053
    sprite('pt000_06', 7)	# 1054-1060
    sprite('pt000_07', 7)	# 1061-1067
    sprite('pt000_08', 7)	# 1068-1074
    sprite('pt000_09', 7)	# 1075-1081
    sprite('pt000_10', 7)	# 1082-1088
    sprite('pt000_11', 7)	# 1089-1095
    sprite('pt000_12', 7)	# 1096-1102
    sprite('pt000_13', 7)	# 1103-1109
    gotoLabel(31)
    label(100)
    sprite('pt000_00', 1)	# 1110-1110
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown2037(2)
    if random_(2, 0, 50):
        SFX_1('bpt600brg_1')
    else:
        SFX_1('bpt600brg_2')
    label(101)
    sprite('pt000_00', 7)	# 1111-1117
    sprite('pt000_01', 7)	# 1118-1124
    sprite('pt000_02', 7)	# 1125-1131
    sprite('pt000_03', 7)	# 1132-1138
    sprite('pt000_04', 7)	# 1139-1145
    sprite('pt000_05', 7)	# 1146-1152
    sprite('pt000_06', 7)	# 1153-1159
    sprite('pt000_07', 7)	# 1160-1166
    sprite('pt000_08', 7)	# 1167-1173
    sprite('pt000_09', 7)	# 1174-1180
    sprite('pt000_10', 7)	# 1181-1187
    sprite('pt000_11', 7)	# 1188-1194
    sprite('pt000_12', 7)	# 1195-1201
    sprite('pt000_13', 7)	# 1202-1208
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(101)
    sprite('pt001_00', 7)	# 1209-1215
    sprite('pt001_01', 5)	# 1216-1220
    sprite('pt001_02', 8)	# 1221-1228
    sprite('pt001_03', 8)	# 1229-1236
    sprite('pt001_04', 8)	# 1237-1244
    sprite('pt001_05', 8)	# 1245-1252
    sprite('pt001_06', 5)	# 1253-1257
    Unknown21011(180)
    label(102)
    sprite('pt000_00', 7)	# 1258-1264
    sprite('pt000_01', 7)	# 1265-1271
    sprite('pt000_02', 7)	# 1272-1278
    sprite('pt000_03', 7)	# 1279-1285
    Unknown21007(24, 40)
    sprite('pt000_04', 7)	# 1286-1292
    sprite('pt000_05', 7)	# 1293-1299
    sprite('pt000_06', 7)	# 1300-1306
    sprite('pt000_07', 7)	# 1307-1313
    sprite('pt000_08', 7)	# 1314-1320
    sprite('pt000_09', 7)	# 1321-1327
    sprite('pt000_10', 7)	# 1328-1334
    sprite('pt000_11', 7)	# 1335-1341
    sprite('pt000_12', 7)	# 1342-1348
    sprite('pt000_13', 7)	# 1349-1355
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('pt000_00', 1)	# 1356-1356
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        Unknown21007(4, 32)
    GFX_0('ptPhantom_NoSound', 0)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(-20000)
    Unknown35()
    SFX_1('bpt600bhz')
    label(111)
    sprite('pt000_00', 7)	# 1357-1363
    sprite('pt000_01', 7)	# 1364-1370
    sprite('pt000_02', 7)	# 1371-1377
    sprite('pt000_03', 7)	# 1378-1384
    sprite('pt000_04', 7)	# 1385-1391
    sprite('pt000_05', 7)	# 1392-1398
    sprite('pt000_06', 7)	# 1399-1405
    sprite('pt000_07', 7)	# 1406-1412
    sprite('pt000_08', 7)	# 1413-1419
    sprite('pt000_09', 7)	# 1420-1426
    sprite('pt000_10', 7)	# 1427-1433
    sprite('pt000_11', 7)	# 1434-1440
    sprite('pt000_12', 7)	# 1441-1447
    sprite('pt000_13', 7)	# 1448-1454
    if SLOT_97:
        _gotolabel(111)
    sprite('pt000_00', 1)	# 1455-1455
    Unknown21007(24, 40)
    Unknown21011(360)
    label(112)
    sprite('pt000_00', 7)	# 1456-1462
    sprite('pt000_01', 7)	# 1463-1469
    sprite('pt000_02', 7)	# 1470-1476
    sprite('pt000_03', 7)	# 1477-1483
    sprite('pt000_04', 7)	# 1484-1490
    sprite('pt000_05', 7)	# 1491-1497
    sprite('pt000_06', 7)	# 1498-1504
    sprite('pt000_07', 7)	# 1505-1511
    sprite('pt000_08', 7)	# 1512-1518
    sprite('pt000_09', 7)	# 1519-1525
    sprite('pt000_10', 7)	# 1526-1532
    sprite('pt000_11', 7)	# 1533-1539
    sprite('pt000_12', 7)	# 1540-1546
    sprite('pt000_13', 7)	# 1547-1553
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('pt650_00', 20)	# 1554-1573
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)
    sprite('pt650_00', 1)	# 1574-1574
    SFX_1('bpt600bes_1')
    label(121)
    sprite('pt650_00', 1)	# 1575-1575
    if SLOT_97:
        _gotolabel(121)
    sprite('pt650_00', 30)	# 1576-1605
    sprite('pt650_00', 1)	# 1606-1606
    SFX_1('bpt600bes_2')
    label(122)
    sprite('pt650_00', 1)	# 1607-1607
    if SLOT_97:
        _gotolabel(122)
    sprite('pt650_00', 45)	# 1608-1652
    sprite('pt650_00', 32767)	# 1653-34419
    Unknown21007(24, 40)
    Unknown21011(240)
    ExitState()
    label(130)
    sprite('pt601_00', 30)	# 34420-34449
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bpt600bjb_2')
    label(131)
    sprite('pt601_00', 1)	# 34450-34450
    if SLOT_97:
        _gotolabel(131)
    sprite('pt601_00', 15)	# 34451-34465
    GFX_1('ptef_entryheartA', 0)
    SFX_3('ptse_15')
    sprite('pt601_01', 6)	# 34466-34471
    sprite('pt601_02', 6)	# 34472-34477
    GFX_0('EntryHeart', 0)
    SFX_3('ptse_21')
    sprite('pt601_03', 6)	# 34478-34483
    sprite('pt601_04', 6)	# 34484-34489
    sprite('pt601_05', 6)	# 34490-34495
    sprite('pt601_06', 6)	# 34496-34501
    sprite('pt601_07', 6)	# 34502-34507
    sprite('pt601_05', 6)	# 34508-34513
    sprite('pt601_06', 6)	# 34514-34519
    sprite('pt601_07', 6)	# 34520-34525
    sprite('pt601_05', 6)	# 34526-34531
    sprite('pt601_06', 6)	# 34532-34537
    sprite('pt601_07', 6)	# 34538-34543
    sprite('pt601_05', 6)	# 34544-34549
    sprite('pt601_06', 6)	# 34550-34555
    GFX_0('EntryRod', -1)
    sprite('pt601_07', 6)	# 34556-34561
    sprite('pt601_08', 6)	# 34562-34567
    sprite('pt601_09', 6)	# 34568-34573
    sprite('pt601_10', 5)	# 34574-34578
    GFX_1('ptef_450light01', 0)
    SFX_0('003_swing_grap_0_1')
    SFX_0('100_hit_grap_0')
    sprite('pt601_11', 5)	# 34579-34583
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_12', 5)	# 34584-34588
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_13', 5)	# 34589-34593
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_14', 5)	# 34594-34598
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_15', 4)	# 34599-34602
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    sprite('pt601_16', 3)	# 34603-34605
    GFX_1('ptef_450light01', 0)
    sprite('pt601_17', 7)	# 34606-34612
    GFX_0('yugami_ring', 0)
    GFX_1('ptef_entrymc', 0)
    GFX_1('ptef_450light01', 0)
    SFX_3('ptse_13')
    sprite('pt601_18', 6)	# 34613-34618
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_1('bpt600bjb_1')
    sprite('pt601_19', 6)	# 34619-34624
    label(132)
    sprite('pt601_20', 1)	# 34625-34625
    if SLOT_97:
        _gotolabel(132)
    sprite('pt601_20', 30)	# 34626-34655
    sprite('pt601_21', 6)	# 34656-34661
    Unknown21007(24, 40)
    sprite('pt601_22', 5)	# 34662-34666
    Unknown21011(240)
    label(133)
    sprite('pt000_00', 7)	# 34667-34673
    sprite('pt000_01', 7)	# 34674-34680
    sprite('pt000_02', 7)	# 34681-34687
    sprite('pt000_03', 7)	# 34688-34694
    sprite('pt000_04', 7)	# 34695-34701
    sprite('pt000_05', 7)	# 34702-34708
    sprite('pt000_06', 7)	# 34709-34715
    sprite('pt000_07', 7)	# 34716-34722
    sprite('pt000_08', 7)	# 34723-34729
    sprite('pt000_09', 7)	# 34730-34736
    sprite('pt000_10', 7)	# 34737-34743
    sprite('pt000_11', 7)	# 34744-34750
    sprite('pt000_12', 7)	# 34751-34757
    sprite('pt000_13', 7)	# 34758-34764
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('pt000_00', 1)	# 34765-34765
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('pt000_00', 7)	# 34766-34772
    sprite('pt000_01', 7)	# 34773-34779
    sprite('pt000_02', 7)	# 34780-34786
    sprite('pt000_03', 7)	# 34787-34793
    sprite('pt000_04', 7)	# 34794-34800
    sprite('pt000_05', 7)	# 34801-34807
    sprite('pt000_06', 7)	# 34808-34814
    sprite('pt000_07', 7)	# 34815-34821
    sprite('pt000_08', 7)	# 34822-34828
    sprite('pt000_09', 7)	# 34829-34835
    sprite('pt000_10', 7)	# 34836-34842
    sprite('pt000_11', 7)	# 34843-34849
    sprite('pt000_12', 7)	# 34850-34856
    sprite('pt000_13', 7)	# 34857-34863
    gotoLabel(141)
    label(142)
    sprite('pt300_00', 4)	# 34864-34867
    if SLOT_158:
        Unknown2005()
    sprite('pt300_01', 4)	# 34868-34871
    SFX_1('bpt601pyo')
    sprite('pt300_02', 4)	# 34872-34875
    sprite('pt300_03', 6)	# 34876-34881
    sprite('pt300_04', 6)	# 34882-34887
    sprite('pt300_05', 7)	# 34888-34894
    label(143)
    sprite('pt300_06', 1)	# 34895-34895
    if SLOT_97:
        _gotolabel(143)
    sprite('pt300_06', 20)	# 34896-34915
    sprite('pt300_06', 32767)	# 34916-67682
    SFX_3('ptse_00')
    Unknown21007(24, 40)
    Unknown21011(150)
    ExitState()
    label(150)
    sprite('pt601_00', 30)	# 67683-67712
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bpt600pce')
    sprite('pt601_00', 15)	# 67713-67727
    GFX_1('ptef_entryheartA', 0)
    SFX_3('ptse_15')
    sprite('pt601_01', 6)	# 67728-67733
    sprite('pt601_02', 6)	# 67734-67739
    GFX_0('EntryHeart', 0)
    SFX_3('ptse_21')
    sprite('pt601_03', 6)	# 67740-67745
    sprite('pt601_04', 6)	# 67746-67751
    sprite('pt601_05', 6)	# 67752-67757
    sprite('pt601_06', 6)	# 67758-67763
    sprite('pt601_07', 6)	# 67764-67769
    sprite('pt601_05', 6)	# 67770-67775
    sprite('pt601_06', 6)	# 67776-67781
    sprite('pt601_07', 6)	# 67782-67787
    sprite('pt601_05', 6)	# 67788-67793
    sprite('pt601_06', 6)	# 67794-67799
    sprite('pt601_07', 6)	# 67800-67805
    sprite('pt601_05', 6)	# 67806-67811
    sprite('pt601_06', 6)	# 67812-67817
    GFX_0('EntryRod', -1)
    sprite('pt601_07', 6)	# 67818-67823
    sprite('pt601_08', 6)	# 67824-67829
    sprite('pt601_09', 6)	# 67830-67835
    sprite('pt601_10', 5)	# 67836-67840
    GFX_1('ptef_450light01', 0)
    SFX_0('003_swing_grap_0_1')
    SFX_0('100_hit_grap_0')
    sprite('pt601_11', 5)	# 67841-67845
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_12', 5)	# 67846-67850
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_13', 5)	# 67851-67855
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_14', 5)	# 67856-67860
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_15', 4)	# 67861-67864
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    sprite('pt601_16', 3)	# 67865-67867
    GFX_1('ptef_450light01', 0)
    sprite('pt601_17', 7)	# 67868-67874
    GFX_0('yugami_ring', 0)
    GFX_1('ptef_entrymc', 0)
    GFX_1('ptef_450light01', 0)
    SFX_3('ptse_13')
    sprite('pt601_18', 6)	# 67875-67880
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_1('pt415')
    sprite('pt601_19', 6)	# 67881-67886
    sprite('pt601_20', 60)	# 67887-67946
    sprite('pt601_21', 6)	# 67947-67952
    Unknown21007(24, 40)
    sprite('pt601_22', 5)	# 67953-67957
    Unknown21011(200)
    label(151)
    sprite('pt000_00', 7)	# 67958-67964
    sprite('pt000_01', 7)	# 67965-67971
    sprite('pt000_02', 7)	# 67972-67978
    sprite('pt000_03', 7)	# 67979-67985
    sprite('pt000_04', 7)	# 67986-67992
    sprite('pt000_05', 7)	# 67993-67999
    sprite('pt000_06', 7)	# 68000-68006
    sprite('pt000_07', 7)	# 68007-68013
    sprite('pt000_08', 7)	# 68014-68020
    sprite('pt000_09', 7)	# 68021-68027
    sprite('pt000_10', 7)	# 68028-68034
    sprite('pt000_11', 7)	# 68035-68041
    sprite('pt000_12', 7)	# 68042-68048
    sprite('pt000_13', 7)	# 68049-68055
    gotoLabel(151)
    ExitState()
    label(160)
    sprite('pt600_00', 39)	# 68056-68094
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bpt600uli')
    sprite('pt600_00', 120)	# 68095-68214
    sprite('pt600_01', 6)	# 68215-68220
    sprite('pt600_02', 6)	# 68221-68226
    SFX_0('008_swing_pole_2')
    sprite('pt600_03', 6)	# 68227-68232
    sprite('pt600_04', 6)	# 68233-68238
    sprite('pt600_05', 7)	# 68239-68245
    SFX_0('008_swing_pole_2')
    sprite('pt600_06', 5)	# 68246-68250
    GFX_1('ptef_entrylightA', 0)
    sprite('pt600_07', 5)	# 68251-68255
    Unknown23119(13145800, 16, 2)
    sprite('pt600_08', 4)	# 68256-68259
    sprite('pt600_08', 3)	# 68260-68262
    GFX_1('ptef_entrylightB', 0)
    sprite('pt600_08', 3)	# 68263-68265
    sprite('pt600_09', 6)	# 68266-68271
    sprite('pt600_10', 15)	# 68272-68286	 **attackbox here**
    GFX_0('yugami_ring', 0)
    GFX_1('ptef_entrymc', 0)
    SFX_0('019_cloth_c')
    SFX_3('ptse_13')
    SFX_1('pt413')
    sprite('pt600_11', 6)	# 68287-68292	 **attackbox here**
    sprite('pt600_12', 5)	# 68293-68297	 **attackbox here**
    sprite('pt600_10ex00', 5)	# 68298-68302	 **attackbox here**
    sprite('pt600_11ex00', 5)	# 68303-68307	 **attackbox here**
    sprite('pt600_12ex00', 5)	# 68308-68312
    sprite('pt600_13', 40)	# 68313-68352
    sprite('pt600_14', 6)	# 68353-68358
    sprite('pt600_15', 6)	# 68359-68364
    Unknown21007(24, 40)
    sprite('pt600_16', 6)	# 68365-68370
    Unknown21011(240)
    label(161)
    sprite('pt000_00', 7)	# 68371-68377
    sprite('pt000_01', 7)	# 68378-68384
    sprite('pt000_02', 7)	# 68385-68391
    sprite('pt000_03', 7)	# 68392-68398
    sprite('pt000_04', 7)	# 68399-68405
    sprite('pt000_05', 7)	# 68406-68412
    sprite('pt000_06', 7)	# 68413-68419
    sprite('pt000_07', 7)	# 68420-68426
    sprite('pt000_08', 7)	# 68427-68433
    sprite('pt000_09', 7)	# 68434-68440
    sprite('pt000_10', 7)	# 68441-68447
    sprite('pt000_11', 7)	# 68448-68454
    sprite('pt000_12', 7)	# 68455-68461
    sprite('pt000_13', 7)	# 68462-68468
    gotoLabel(161)
    ExitState()
    label(170)
    sprite('pt000_00', 1)	# 68469-68469
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
        if SLOT_158:
            Unknown2005()
    label(171)
    sprite('pt000_00', 7)	# 68470-68476
    sprite('pt000_01', 7)	# 68477-68483
    sprite('pt000_02', 7)	# 68484-68490
    sprite('pt000_03', 7)	# 68491-68497
    sprite('pt000_04', 7)	# 68498-68504
    sprite('pt000_05', 7)	# 68505-68511
    sprite('pt000_06', 7)	# 68512-68518
    sprite('pt000_07', 7)	# 68519-68525
    sprite('pt000_08', 7)	# 68526-68532
    sprite('pt000_09', 7)	# 68533-68539
    sprite('pt000_10', 7)	# 68540-68546
    sprite('pt000_11', 7)	# 68547-68553
    sprite('pt000_12', 7)	# 68554-68560
    sprite('pt000_13', 7)	# 68561-68567
    gotoLabel(171)
    label(172)
    sprite('pt300_00', 4)	# 68568-68571
    sprite('pt300_01', 4)	# 68572-68575
    SFX_1('bpt601rwi')
    sprite('pt300_02', 4)	# 68576-68579
    sprite('pt300_03', 6)	# 68580-68585
    sprite('pt300_04', 6)	# 68586-68591
    sprite('pt300_05', 7)	# 68592-68598
    label(173)
    sprite('pt300_06', 1)	# 68599-68599
    if SLOT_97:
        _gotolabel(173)
    sprite('pt300_06', 30)	# 68600-68629
    sprite('pt300_07', 7)	# 68630-68636
    SFX_3('ptse_00')
    sprite('pt300_08', 9)	# 68637-68645
    sprite('pt300_09', 6)	# 68646-68651
    Unknown23018(1)
    label(174)
    sprite('pt000_00', 7)	# 68652-68658
    sprite('pt000_01', 7)	# 68659-68665
    sprite('pt000_02', 7)	# 68666-68672
    sprite('pt000_03', 7)	# 68673-68679
    sprite('pt000_04', 7)	# 68680-68686
    sprite('pt000_05', 7)	# 68687-68693
    sprite('pt000_06', 7)	# 68694-68700
    sprite('pt000_07', 7)	# 68701-68707
    sprite('pt000_08', 7)	# 68708-68714
    sprite('pt000_09', 7)	# 68715-68721
    sprite('pt000_10', 7)	# 68722-68728
    sprite('pt000_11', 7)	# 68729-68735
    sprite('pt000_12', 7)	# 68736-68742
    sprite('pt000_13', 7)	# 68743-68749
    gotoLabel(174)
    label(180)
    sprite('pt000_00', 1)	# 68750-68750
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1334000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)

    def upon_39():
        clearUponHandler(39)
        sendToLabel(183)
    Unknown2019(500)
    label(181)
    sprite('pt000_00', 7)	# 68751-68757
    sprite('pt000_01', 7)	# 68758-68764
    sprite('pt000_02', 7)	# 68765-68771
    sprite('pt000_03', 7)	# 68772-68778
    sprite('pt000_04', 7)	# 68779-68785
    sprite('pt000_05', 7)	# 68786-68792
    sprite('pt000_06', 7)	# 68793-68799
    sprite('pt000_07', 7)	# 68800-68806
    sprite('pt000_08', 7)	# 68807-68813
    sprite('pt000_09', 7)	# 68814-68820
    sprite('pt000_10', 7)	# 68821-68827
    sprite('pt000_11', 7)	# 68828-68834
    sprite('pt000_12', 7)	# 68835-68841
    sprite('pt000_13', 7)	# 68842-68848
    gotoLabel(181)
    label(182)
    sprite('pt636_00', 6)	# 68849-68854
    sprite('pt636_01', 32767)	# 68855-101621
    label(183)
    sprite('pt636_02', 10)	# 101622-101631
    SFX_1('bpt601uyu')
    sprite('pt636_03', 6)	# 101632-101637
    sprite('pt636_04', 6)	# 101638-101643
    Unknown23018(1)
    label(184)
    sprite('pt636_02', 10)	# 101644-101653
    sprite('pt636_03', 6)	# 101654-101659
    sprite('pt636_04', 6)	# 101660-101665
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('pt000_00', 7)	# 101666-101672
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('pt000_01', 7)	# 101673-101679
    sprite('pt000_02', 7)	# 101680-101686
    sprite('pt000_03', 7)	# 101687-101693
    sprite('pt001_00', 7)	# 101694-101700
    SFX_1('bpt600pla')
    sprite('pt001_01', 5)	# 101701-101705
    sprite('pt001_02', 8)	# 101706-101713
    sprite('pt001_03', 8)	# 101714-101721
    sprite('pt001_04', 8)	# 101722-101729
    sprite('pt001_05', 8)	# 101730-101737
    sprite('pt001_06', 5)	# 101738-101742
    label(191)
    sprite('pt000_00', 7)	# 101743-101749
    sprite('pt000_01', 7)	# 101750-101756
    sprite('pt000_02', 7)	# 101757-101763
    sprite('pt000_03', 7)	# 101764-101770
    sprite('pt000_04', 7)	# 101771-101777
    sprite('pt000_05', 7)	# 101778-101784
    sprite('pt000_06', 7)	# 101785-101791
    sprite('pt000_07', 7)	# 101792-101798
    sprite('pt000_08', 7)	# 101799-101805
    sprite('pt000_09', 7)	# 101806-101812
    sprite('pt000_10', 7)	# 101813-101819
    sprite('pt000_11', 7)	# 101820-101826
    sprite('pt000_12', 7)	# 101827-101833
    sprite('pt000_13', 7)	# 101834-101840
    if SLOT_97:
        _gotolabel(191)
    sprite('pt000_00', 1)	# 101841-101841
    Unknown21007(24, 40)
    Unknown21011(360)
    label(192)
    sprite('pt000_00', 7)	# 101842-101848
    sprite('pt000_01', 7)	# 101849-101855
    sprite('pt000_02', 7)	# 101856-101862
    sprite('pt000_03', 7)	# 101863-101869
    sprite('pt000_04', 7)	# 101870-101876
    sprite('pt000_05', 7)	# 101877-101883
    sprite('pt000_06', 7)	# 101884-101890
    sprite('pt000_07', 7)	# 101891-101897
    sprite('pt000_08', 7)	# 101898-101904
    sprite('pt000_09', 7)	# 101905-101911
    sprite('pt000_10', 7)	# 101912-101918
    sprite('pt000_11', 7)	# 101919-101925
    sprite('pt000_12', 7)	# 101926-101932
    sprite('pt000_13', 7)	# 101933-101939
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('pt000_00', 7)	# 101940-101946
    if SLOT_158:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        Unknown21007(4, 32)
    GFX_0('ptPhantom_NoSound', 0)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(-20000)
    Unknown35()
    SFX_0('022_magiccircle_b')
    sprite('pt000_01', 7)	# 101947-101953
    sprite('pt000_02', 7)	# 101954-101960
    SFX_1('bpt600bce')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(360)
    label(201)
    sprite('pt000_00', 7)	# 101961-101967
    sprite('pt000_01', 7)	# 101968-101974
    sprite('pt000_02', 7)	# 101975-101981
    sprite('pt000_03', 7)	# 101982-101988
    sprite('pt000_04', 7)	# 101989-101995
    sprite('pt000_05', 7)	# 101996-102002
    sprite('pt000_06', 7)	# 102003-102009
    sprite('pt000_07', 7)	# 102010-102016
    sprite('pt000_08', 7)	# 102017-102023
    sprite('pt000_09', 7)	# 102024-102030
    sprite('pt000_10', 7)	# 102031-102037
    sprite('pt000_11', 7)	# 102038-102044
    sprite('pt000_12', 7)	# 102045-102051
    sprite('pt000_13', 7)	# 102052-102058
    gotoLabel(201)
    ExitState()
    label(210)
    sprite('pt601_00', 32767)	# 102059-134825

    def upon_40():
        clearUponHandler(40)
        sendToLabel(211)
    label(211)
    sprite('pt601_00', 1)	# 134826-134826
    sprite('pt601_00', 15)	# 134827-134841
    GFX_1('ptef_entryheartA', 0)
    SFX_3('ptse_15')
    sprite('pt601_01', 6)	# 134842-134847
    sprite('pt601_02', 6)	# 134848-134853
    GFX_0('EntryHeart', 0)
    SFX_3('ptse_21')
    sprite('pt601_03', 6)	# 134854-134859
    sprite('pt601_04', 6)	# 134860-134865
    sprite('pt601_05', 6)	# 134866-134871
    sprite('pt601_06', 6)	# 134872-134877
    sprite('pt601_07', 6)	# 134878-134883
    sprite('pt601_05', 6)	# 134884-134889
    sprite('pt601_06', 6)	# 134890-134895
    sprite('pt601_07', 6)	# 134896-134901
    sprite('pt601_05', 6)	# 134902-134907
    sprite('pt601_06', 6)	# 134908-134913
    sprite('pt601_07', 6)	# 134914-134919
    sprite('pt601_05', 6)	# 134920-134925
    sprite('pt601_06', 6)	# 134926-134931
    GFX_0('EntryRod', -1)
    sprite('pt601_07', 6)	# 134932-134937
    sprite('pt601_08', 6)	# 134938-134943
    sprite('pt601_09', 6)	# 134944-134949
    sprite('pt601_10', 5)	# 134950-134954
    GFX_1('ptef_450light01', 0)
    SFX_0('003_swing_grap_0_1')
    SFX_0('100_hit_grap_0')
    sprite('pt601_11', 5)	# 134955-134959
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_12', 5)	# 134960-134964
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_13', 5)	# 134965-134969
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    GFX_1('ptef_450light01', 2)
    sprite('pt601_14', 5)	# 134970-134974
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    SFX_0('008_swing_pole_0')
    sprite('pt601_15', 4)	# 134975-134978
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    sprite('pt601_16', 3)	# 134979-134981
    GFX_1('ptef_450light01', 0)
    sprite('pt601_17', 7)	# 134982-134988
    GFX_0('yugami_ring', 0)
    GFX_1('ptef_entrymc', 0)
    GFX_1('ptef_450light01', 0)
    SFX_3('ptse_13')
    SFX_1('bpt601ahe')
    sprite('pt601_18', 6)	# 134989-134994
    GFX_1('ptef_450light01', 0)
    GFX_1('ptef_450light01', 1)
    sprite('pt601_19', 6)	# 134995-135000
    sprite('pt601_20', 32767)	# 135001-167767
    Unknown23018(1)
    ExitState()
    label(220)
    sprite('pt650_00', 20)	# 167768-167787
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)
    sprite('pt650_00', 1)	# 167788-167788
    SFX_1('bpt600pku')
    label(221)
    sprite('pt650_00', 1)	# 167789-167789
    if SLOT_97:
        _gotolabel(221)
    sprite('pt650_00', 30)	# 167790-167819
    sprite('pt650_00', 32767)	# 167820-200586
    Unknown21007(24, 40)
    Unknown21011(120)
    label(991)
    sprite('pt000_00', 1)	# 200587-200587
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('pt000_00', 7)	# 200588-200594
    sprite('pt000_01', 7)	# 200595-200601
    sprite('pt000_02', 7)	# 200602-200608
    sprite('pt000_03', 7)	# 200609-200615
    sprite('pt000_04', 7)	# 200616-200622
    sprite('pt000_05', 7)	# 200623-200629
    sprite('pt000_06', 7)	# 200630-200636
    sprite('pt000_07', 7)	# 200637-200643
    sprite('pt000_08', 7)	# 200644-200650
    sprite('pt000_09', 7)	# 200651-200657
    sprite('pt000_10', 7)	# 200658-200664
    sprite('pt000_11', 7)	# 200665-200671
    sprite('pt000_12', 7)	# 200672-200678
    sprite('pt000_13', 7)	# 200679-200685
    gotoLabel(992)
    label(993)
    sprite('pt033_00', 2)	# 200686-200687

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(995)

    def upon_STATE_END():
        Unknown2019(0)
        Unknown3038(1)
        Unknown3001(255)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown3001(255)
    Unknown3004(-20)
    physicsXImpulse(-51000)
    physicsYImpulse(18800)
    setGravity(1500)
    Unknown8002()
    sprite('pt033_01', 3)	# 200688-200690
    label(994)
    sprite('pt033_02', 3)	# 200691-200693
    sprite('pt033_01', 3)	# 200694-200696
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 200697-200699
    ExitState()
    label(1000)
    sprite('pt000_00', 1)	# 200700-200700
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 10002):
            SFX_1('bpt602')
            sendToLabel(1002)
        if (SLOT_48 == 10004):
            clearUponHandler(43)
            sendToLabel(1004)
    label(1001)
    sprite('pt000_00', 7)	# 200701-200707
    sprite('pt000_01', 7)	# 200708-200714
    sprite('pt000_02', 7)	# 200715-200721
    sprite('pt000_03', 7)	# 200722-200728
    sprite('pt000_04', 7)	# 200729-200735
    sprite('pt000_05', 7)	# 200736-200742
    sprite('pt000_06', 7)	# 200743-200749
    sprite('pt000_07', 7)	# 200750-200756
    sprite('pt000_08', 7)	# 200757-200763
    sprite('pt000_09', 7)	# 200764-200770
    sprite('pt000_10', 7)	# 200771-200777
    sprite('pt000_11', 7)	# 200778-200784
    sprite('pt000_12', 7)	# 200785-200791
    sprite('pt000_13', 7)	# 200792-200798
    gotoLabel(1001)
    label(1002)
    sprite('pt070_13', 6)	# 200799-200804
    sprite('pt070_12', 6)	# 200805-200810
    sprite('pt070_11', 6)	# 200811-200816
    label(1003)
    sprite('pt650_00', 1)	# 200817-200817
    if SLOT_97:
        _gotolabel(1003)
    sprite('pt650_00', 20)	# 200818-200837
    sprite('pt650_00', 32767)	# 200838-233604
    Unknown23029(24, 10003, 0)
    Unknown23029(22, 10003, 0)
    Unknown23029(23, 10003, 0)
    label(1004)
    sprite('pt070_10', 6)	# 233605-233610
    sprite('pt070_11', 6)	# 233611-233616
    sprite('pt070_12', 6)	# 233617-233622
    sprite('pt070_13', 6)	# 233623-233628
    sprite('pt203_00', 1)	# 233629-233629
    sprite('pt203_01', 2)	# 233630-233631
    sprite('pt203_02', 2)	# 233632-233633
    GFX_0('pt203_mahojin', -1)
    GFX_0('pt203_mahojinsub', -1)
    GFX_0('pt203_aura1', -1)
    GFX_0('pt203_aura2', -1)
    GFX_0('pt203_aura3', -1)
    sprite('pt203_02', 2)	# 233634-233635
    sprite('pt203_03', 1)	# 233636-233636
    GFX_0('pt203_stick', 0)
    sprite('pt203_04', 2)	# 233637-233638
    SFX_3('ptse_13')
    sprite('pt203_05', 5)	# 233639-233643
    sprite('pt203_06', 2)	# 233644-233645
    sprite('pt203_07', 2)	# 233646-233647
    sprite('pt203_08', 2)	# 233648-233649
    sprite('pt203_09', 2)	# 233650-233651
    sprite('pt203_10', 2)	# 233652-233653
    sprite('pt203_11', 1)	# 233654-233654
    Unknown18008()
    label(1005)
    sprite('pt000_00', 7)	# 233655-233661
    sprite('pt000_01', 7)	# 233662-233668
    sprite('pt000_02', 7)	# 233669-233675
    sprite('pt000_03', 7)	# 233676-233682
    sprite('pt000_04', 7)	# 233683-233689
    sprite('pt000_05', 7)	# 233690-233696
    sprite('pt000_06', 7)	# 233697-233703
    sprite('pt000_07', 7)	# 233704-233710
    sprite('pt000_08', 7)	# 233711-233717
    sprite('pt000_09', 7)	# 233718-233724
    sprite('pt000_10', 7)	# 233725-233731
    sprite('pt000_11', 7)	# 233732-233738
    sprite('pt000_12', 7)	# 233739-233745
    sprite('pt000_13', 7)	# 233746-233752
    gotoLabel(1005)

@State
def CmnActRoundWin():
    Unknown20000(1)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('pt030_00', 5)	# 1-5
    sprite('pt030_01', 5)	# 6-10
    label(0)
    sprite('pt030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 16-20
    sprite('pt030_04', 5)	# 21-25
    sprite('pt030_05', 5)	# 26-30
    sprite('pt030_06', 5)	# 31-35
    sprite('pt030_07', 5)	# 36-40
    sprite('pt030_08', 5)	# 41-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 46-50
    sprite('pt030_10', 5)	# 51-55
    sprite('pt030_11', 5)	# 56-60
    sprite('pt030_12', 5)	# 61-65
    sprite('pt030_13', 5)	# 66-70
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    sprite('pt615_00', 5)	# 71-75
    sprite('pt615_01', 5)	# 76-80
    sprite('pt615_02', 5)	# 81-85
    SFX_0('019_cloth_b')
    sprite('pt615_03', 5)	# 86-90
    sprite('pt615_04', 5)	# 91-95
    sprite('pt615_05', 5)	# 96-100
    sprite('pt615_06', 5)	# 101-105
    if random_(2, 0, 50):
        SFX_1('pt400')
        Unknown23018(1)
    else:
        SFX_1('pt401')
        Unknown23018(1)
    sprite('pt615_07', 5)	# 106-110
    sprite('pt615_08', 5)	# 111-115
    sprite('pt615_09', 5)	# 116-120
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 121-125
    label(2)
    sprite('pt615_09', 5)	# 126-130
    sprite('pt615_08', 5)	# 131-135
    sprite('pt615_09', 5)	# 136-140
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 141-145
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('pt615_06', 32767)	# 146-32912
    loopRest()

@State
def CmnActMatchWin():
    if SLOT_169:
        _gotolabel(482)
    if SLOT_122:
        _gotolabel(482)
    if SLOT_123:
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
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    if (SLOT_29 < 500000):
                        sendToLabel(130)
                        clearUponHandler(3)
                        Unknown36(24)
                        SLOT_53 = 1
                        Unknown35()
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    if (SLOT_29 < 500000):
                        sendToLabel(140)
                        clearUponHandler(3)
                        Unknown36(24)
                        SLOT_53 = 1
                        Unknown35()
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('bjb'):
                if (SLOT_145 <= 900000):
                    if (SLOT_145 >= 200000):
                        sendToLabel(170)
                        clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 700000):
                    if (SLOT_145 >= 250000):
                        sendToLabel(180)
                        clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('bce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('ahe'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('pku'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    if SLOT_122:
        if random_(2, 0, 50):
            sendToLabel(0)
        else:
            sendToLabel(10)
    if SLOT_123:
        if random_(2, 0, 50):
            sendToLabel(0)
        else:
            sendToLabel(10)
    sprite('keep', 1)	# 4-4
    if SLOT_158:
        if SLOT_108:
            if SLOT_52:
                sendToLabel(10)
            elif random_(2, 0, 50):
                sendToLabel(0)
            else:
                sendToLabel(10)
        elif SLOT_52:
            sendToLabel(10)
        elif random_(2, 0, 33):
            sendToLabel(0)
        elif random_(2, 0, 50):
            sendToLabel(10)
        else:
            sendToLabel(20)
    else:
        sendToLabel(10)
    label(0)
    sprite('keep', 1)	# 5-5
    clearUponHandler(3)
    Unknown2018(1, 100)
    Unknown2037(1)
    Unknown2053(0)
    Unknown2034(0)
    Unknown20000(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 200000):
                Unknown2037(0)
                sendToLabel(2)
        if (not SLOT_2):
            Unknown36(22)
            Unknown2053(0)
            Unknown2034(0)
            Unknown35()
            if (SLOT_29 >= 1600000):
                sendToLabel(4)
    sprite('pt610_00', 3)	# 6-8
    physicsXImpulse(5000)
    Unknown7014('ptse_14')
    sprite('pt610_01', 3)	# 9-11
    sprite('pt610_02', 3)	# 12-14
    sprite('pt610_03', 3)	# 15-17
    sprite('pt610_04', 3)	# 18-20
    sprite('pt610_05', 3)	# 21-23
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    label(1)
    sprite('pt610_06', 6)	# 24-29
    sprite('pt610_07', 6)	# 30-35
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_08', 6)	# 36-41
    sprite('pt610_06', 6)	# 42-47
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_07', 6)	# 48-53
    sprite('pt610_08', 6)	# 54-59
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('pt610_06', 6)	# 60-65
    physicsXImpulse(5000)
    if SLOT_108:
        if random_(2, 0, 50):
            SFX_1('bpt402_0')
        else:
            SFX_1('bpt402_1')
    elif random_(2, 0, 50):
        SFX_1('bpt520')
    else:
        SFX_1('bpt521')
    Unknown23018(1)
    sprite('pt610_07', 6)	# 66-71
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_08', 6)	# 72-77
    sprite('pt610_06', 6)	# 78-83
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_07', 6)	# 84-89
    sprite('pt610_08', 6)	# 90-95
    sprite('pt610_06', 6)	# 96-101
    sprite('pt610_07', 6)	# 102-107
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_08', 6)	# 108-113
    sprite('pt610_09', 3)	# 114-116
    sprite('pt610_10', 3)	# 117-119
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_11', 3)	# 120-122
    physicsXImpulse(0)
    Unknown2018(0, 100)
    Unknown20000(0)
    Unknown20007(1)
    sprite('pt610_10ex01', 3)	# 123-125
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_09ex01', 3)	# 126-128
    physicsXImpulse(-5000)
    physicsYImpulse(700)
    label(3)
    sprite('pt610_06ex01', 6)	# 129-134
    sprite('pt610_07ex01', 6)	# 135-140
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_08ex01', 6)	# 141-146
    sprite('pt610_06ex01', 6)	# 147-152
    GFX_1('ptef_402light', 0)
    GFX_1('ptef_402light', 1)
    sprite('pt610_07ex01', 6)	# 153-158
    sprite('pt610_08ex01', 6)	# 159-164
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('pt610_07ex01', 32767)	# 165-32931
    Unknown1084(1)
    label(10)
    sprite('pt611_00', 3)	# 32932-32934
    sprite('pt611_01', 4)	# 32935-32938
    sprite('pt611_02', 4)	# 32939-32942	 **attackbox here**
    GFX_1('ptef_drivethrow', 0)
    GFX_1('ptef_winsmoke', 1)
    GFX_1('ptef_winsmoke', 2)
    SFX_0('016_explode_0')
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bpt525_0', 100, 896823394, 811545650, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bpt402_0', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bpt523_0', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt611_03', 6)	# 32943-32948	 **attackbox here**
    sprite('pt611_04', 8)	# 32949-32956	 **attackbox here**
    sprite('pt611_05', 4)	# 32957-32960	 **attackbox here**
    sprite('pt611_06', 4)	# 32961-32964	 **attackbox here**
    sprite('pt611_07', 5)	# 32965-32969
    SFX_3('ptse_03')
    sprite('pt611_08', 5)	# 32970-32974
    sprite('pt611_09', 4)	# 32975-32978	 **attackbox here**
    sprite('pt611_10', 4)	# 32979-32982	 **attackbox here**
    sprite('pt611_11', 4)	# 32983-32986	 **attackbox here**
    sprite('pt611_12', 4)	# 32987-32990	 **attackbox here**
    sprite('pt611_13', 6)	# 32991-32996
    sprite('pt611_14', 6)	# 32997-33002	 **attackbox here**
    sprite('pt611_15', 6)	# 33003-33008
    sprite('pt611_14ex00', 6)	# 33009-33014	 **attackbox here**
    label(11)
    sprite('pt611_16', 7)	# 33015-33021
    GFX_1('ptef_winheart', 0)
    SFX_3('ptse_15')
    sprite('pt611_17', 7)	# 33022-33028
    sprite('pt611_18', 7)	# 33029-33035
    sprite('pt611_17', 7)	# 33036-33042
    sprite('pt611_16', 7)	# 33043-33049
    sprite('pt611_17', 7)	# 33050-33056
    sprite('pt611_18', 7)	# 33057-33063
    sprite('pt611_17', 7)	# 33064-33070
    sprite('pt611_16', 7)	# 33071-33077
    sprite('pt611_17', 7)	# 33078-33084
    sprite('pt611_18', 7)	# 33085-33091
    sprite('pt611_17', 7)	# 33092-33098
    if SLOT_97:
        _gotolabel(11)
    sprite('pt611_16', 1)	# 33099-33099
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bpt525_1', 100, 896823394, 828322866, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bpt402_1', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bpt523_1', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(12)
    sprite('pt611_16', 7)	# 33100-33106
    GFX_1('ptef_winheart', 0)
    SFX_3('ptse_15')
    sprite('pt611_17', 7)	# 33107-33113
    sprite('pt611_18', 7)	# 33114-33120
    sprite('pt611_17', 7)	# 33121-33127
    sprite('pt611_16', 7)	# 33128-33134
    sprite('pt611_17', 7)	# 33135-33141
    sprite('pt611_18', 7)	# 33142-33148
    sprite('pt611_17', 7)	# 33149-33155
    sprite('pt611_16', 7)	# 33156-33162
    sprite('pt611_17', 7)	# 33163-33169
    sprite('pt611_18', 7)	# 33170-33176
    sprite('pt611_17', 7)	# 33177-33183
    gotoLabel(12)
    label(20)
    physicsXImpulse(5000)
    Unknown2037(1)
    Unknown20000(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(22)
    sprite('pt030_00', 5)	# 33184-33188
    sprite('pt030_01', 5)	# 33189-33193
    label(21)
    sprite('pt030_02', 5)	# 33194-33198
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 33199-33203
    sprite('pt030_04', 5)	# 33204-33208
    sprite('pt030_05', 5)	# 33209-33213
    sprite('pt030_06', 5)	# 33214-33218
    sprite('pt030_07', 5)	# 33219-33223
    sprite('pt030_08', 5)	# 33224-33228
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 33229-33233
    sprite('pt030_10', 5)	# 33234-33238
    sprite('pt030_11', 5)	# 33239-33243
    sprite('pt030_12', 5)	# 33244-33248
    sprite('pt030_13', 5)	# 33249-33253
    loopRest()
    gotoLabel(21)
    label(22)
    physicsXImpulse(0)
    sprite('pt615_00', 5)	# 33254-33258
    sprite('pt615_01', 5)	# 33259-33263
    sprite('pt615_02', 5)	# 33264-33268
    SFX_0('019_cloth_b')
    sprite('pt615_03', 5)	# 33269-33273
    sprite('pt615_04', 5)	# 33274-33278
    sprite('pt615_05', 5)	# 33279-33283
    sprite('pt615_06', 5)	# 33284-33288
    if SLOT_158:
        tag_voice(1, 'bpt522_0', '', '', '')
    label(23)
    sprite('pt615_06', 1)	# 33289-33289
    if SLOT_97:
        _gotolabel(23)
    sprite('pt615_06', 20)	# 33290-33309
    sprite('pt615_06', 1)	# 33310-33310
    if SLOT_158:
        tag_voice(0, 'bpt522_1', '', '', '')
    Unknown23018(1)
    label(24)
    sprite('pt615_06', 1)	# 33311-33311
    loopRest()
    gotoLabel(24)
    ExitState()
    label(100)
    sprite('pt001_00', 7)	# 33312-33318
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
    if random_(2, 0, 50):
        SFX_1('bpt700brg_1')
    else:
        SFX_1('bpt700brg_2')
    sprite('pt001_01', 5)	# 33319-33323
    sprite('pt001_02', 8)	# 33324-33331
    sprite('pt001_03', 8)	# 33332-33339
    sprite('pt001_04', 8)	# 33340-33347
    sprite('pt001_05', 8)	# 33348-33355
    sprite('pt001_06', 5)	# 33356-33360
    label(101)
    sprite('pt000_00', 7)	# 33361-33367
    sprite('pt000_01', 7)	# 33368-33374
    sprite('pt000_02', 7)	# 33375-33381
    sprite('pt000_03', 7)	# 33382-33388
    sprite('pt000_04', 7)	# 33389-33395
    sprite('pt000_05', 7)	# 33396-33402
    sprite('pt000_06', 7)	# 33403-33409
    sprite('pt000_07', 7)	# 33410-33416
    sprite('pt000_08', 7)	# 33417-33423
    sprite('pt000_09', 7)	# 33424-33430
    sprite('pt000_10', 7)	# 33431-33437
    sprite('pt000_11', 7)	# 33438-33444
    sprite('pt000_12', 7)	# 33445-33451
    sprite('pt000_13', 7)	# 33452-33458
    if SLOT_97:
        _gotolabel(101)
    sprite('pt000_00', 1)	# 33459-33459
    Unknown21007(24, 40)
    Unknown21011(180)
    label(102)
    sprite('pt000_00', 7)	# 33460-33466
    sprite('pt000_01', 7)	# 33467-33473
    sprite('pt000_02', 7)	# 33474-33480
    sprite('pt000_03', 7)	# 33481-33487
    sprite('pt000_04', 7)	# 33488-33494
    sprite('pt000_05', 7)	# 33495-33501
    sprite('pt000_06', 7)	# 33502-33508
    sprite('pt000_07', 7)	# 33509-33515
    sprite('pt000_08', 7)	# 33516-33522
    sprite('pt000_09', 7)	# 33523-33529
    sprite('pt000_10', 7)	# 33530-33536
    sprite('pt000_11', 7)	# 33537-33543
    sprite('pt000_12', 7)	# 33544-33550
    sprite('pt000_13', 7)	# 33551-33557
    gotoLabel(102)
    label(110)
    sprite('pt000_00', 1)	# 33558-33558

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('pt000_00', 7)	# 33559-33565
    sprite('pt000_01', 7)	# 33566-33572
    sprite('pt000_02', 7)	# 33573-33579
    sprite('pt000_03', 7)	# 33580-33586
    sprite('pt000_04', 7)	# 33587-33593
    sprite('pt000_05', 7)	# 33594-33600
    sprite('pt000_06', 7)	# 33601-33607
    sprite('pt000_07', 7)	# 33608-33614
    sprite('pt000_08', 7)	# 33615-33621
    sprite('pt000_09', 7)	# 33622-33628
    sprite('pt000_10', 7)	# 33629-33635
    sprite('pt000_11', 7)	# 33636-33642
    sprite('pt000_12', 7)	# 33643-33649
    sprite('pt000_13', 7)	# 33650-33656
    gotoLabel(111)
    label(112)
    sprite('pt000_00', 1)	# 33657-33657
    GFX_0('ptPhantom_NoSound', 0)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(-20000)
    Unknown35()
    SFX_1('bpt701bhz')
    label(113)
    sprite('pt000_00', 7)	# 33658-33664
    sprite('pt000_01', 7)	# 33665-33671
    sprite('pt000_02', 7)	# 33672-33678
    sprite('pt000_03', 7)	# 33679-33685
    sprite('pt000_04', 7)	# 33686-33692
    sprite('pt000_05', 7)	# 33693-33699
    sprite('pt000_06', 7)	# 33700-33706
    sprite('pt000_07', 7)	# 33707-33713
    sprite('pt000_08', 7)	# 33714-33720
    sprite('pt000_09', 7)	# 33721-33727
    sprite('pt000_10', 7)	# 33728-33734
    sprite('pt000_11', 7)	# 33735-33741
    sprite('pt000_12', 7)	# 33742-33748
    sprite('pt000_13', 7)	# 33749-33755
    if SLOT_97:
        _gotolabel(113)
    sprite('pt000_00', 1)	# 33756-33756
    Unknown21007(4, 32)
    Unknown23018(1)
    label(114)
    sprite('pt000_00', 7)	# 33757-33763
    sprite('pt000_01', 7)	# 33764-33770
    sprite('pt000_02', 7)	# 33771-33777
    sprite('pt000_03', 7)	# 33778-33784
    sprite('pt000_04', 7)	# 33785-33791
    sprite('pt000_05', 7)	# 33792-33798
    sprite('pt000_06', 7)	# 33799-33805
    sprite('pt000_07', 7)	# 33806-33812
    sprite('pt000_08', 7)	# 33813-33819
    sprite('pt000_09', 7)	# 33820-33826
    sprite('pt000_10', 7)	# 33827-33833
    sprite('pt000_11', 7)	# 33834-33840
    sprite('pt000_12', 7)	# 33841-33847
    sprite('pt000_13', 7)	# 33848-33854
    gotoLabel(114)
    label(120)
    sprite('pt000_00', 1)	# 33855-33855

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('pt000_00', 7)	# 33856-33862
    sprite('pt000_01', 7)	# 33863-33869
    sprite('pt000_02', 7)	# 33870-33876
    sprite('pt000_03', 7)	# 33877-33883
    sprite('pt000_04', 7)	# 33884-33890
    sprite('pt000_05', 7)	# 33891-33897
    sprite('pt000_06', 7)	# 33898-33904
    sprite('pt000_07', 7)	# 33905-33911
    sprite('pt000_08', 7)	# 33912-33918
    sprite('pt000_09', 7)	# 33919-33925
    sprite('pt000_10', 7)	# 33926-33932
    sprite('pt000_11', 7)	# 33933-33939
    sprite('pt000_12', 7)	# 33940-33946
    sprite('pt000_13', 7)	# 33947-33953
    gotoLabel(121)
    label(122)
    sprite('pt001_00', 7)	# 33954-33960
    SFX_1('bpt701bes_1')
    sprite('pt001_01', 5)	# 33961-33965
    sprite('pt001_02', 8)	# 33966-33973
    sprite('pt001_03', 8)	# 33974-33981
    sprite('pt001_04', 8)	# 33982-33989
    sprite('pt001_05', 8)	# 33990-33997
    sprite('pt001_06', 5)	# 33998-34002
    label(123)
    sprite('pt000_00', 7)	# 34003-34009
    sprite('pt000_01', 7)	# 34010-34016
    sprite('pt000_02', 7)	# 34017-34023
    sprite('pt000_03', 7)	# 34024-34030
    sprite('pt000_04', 7)	# 34031-34037
    sprite('pt000_05', 7)	# 34038-34044
    sprite('pt000_06', 7)	# 34045-34051
    sprite('pt000_07', 7)	# 34052-34058
    sprite('pt000_08', 7)	# 34059-34065
    sprite('pt000_09', 7)	# 34066-34072
    sprite('pt000_10', 7)	# 34073-34079
    sprite('pt000_11', 7)	# 34080-34086
    sprite('pt000_12', 7)	# 34087-34093
    sprite('pt000_13', 7)	# 34094-34100
    if SLOT_97:
        _gotolabel(123)
    sprite('pt000_00', 1)	# 34101-34101
    SFX_1('bpt701bes_2')
    Unknown23018(1)
    label(124)
    sprite('pt000_00', 7)	# 34102-34108
    sprite('pt000_01', 7)	# 34109-34115
    sprite('pt000_02', 7)	# 34116-34122
    sprite('pt000_03', 7)	# 34123-34129
    sprite('pt000_04', 7)	# 34130-34136
    sprite('pt000_05', 7)	# 34137-34143
    sprite('pt000_06', 7)	# 34144-34150
    sprite('pt000_07', 7)	# 34151-34157
    sprite('pt000_08', 7)	# 34158-34164
    sprite('pt000_09', 7)	# 34165-34171
    sprite('pt000_10', 7)	# 34172-34178
    sprite('pt000_11', 7)	# 34179-34185
    sprite('pt000_12', 7)	# 34186-34192
    sprite('pt000_13', 7)	# 34193-34199
    gotoLabel(124)
    label(130)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(132)
    sprite('pt030_00', 5)	# 34200-34204
    sprite('pt030_01', 5)	# 34205-34209
    label(131)
    sprite('pt030_02', 5)	# 34210-34214
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 34215-34219
    sprite('pt030_04', 5)	# 34220-34224
    sprite('pt030_05', 5)	# 34225-34229
    sprite('pt030_06', 5)	# 34230-34234
    sprite('pt030_07', 5)	# 34235-34239
    sprite('pt030_08', 5)	# 34240-34244
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 34245-34249
    sprite('pt030_10', 5)	# 34250-34254
    sprite('pt030_11', 5)	# 34255-34259
    sprite('pt030_12', 5)	# 34260-34264
    sprite('pt030_13', 5)	# 34265-34269
    loopRest()
    gotoLabel(131)
    label(132)
    clearUponHandler(3)
    physicsXImpulse(0)
    sprite('pt615_00', 5)	# 34270-34274
    sprite('pt615_01', 5)	# 34275-34279
    sprite('pt615_02', 5)	# 34280-34284
    SFX_0('019_cloth_b')
    sprite('pt615_03', 5)	# 34285-34289
    sprite('pt615_04', 5)	# 34290-34294
    sprite('pt615_05', 5)	# 34295-34299
    sprite('pt615_06', 5)	# 34300-34304
    SFX_1('bpt700pyo')
    sprite('pt615_07', 5)	# 34305-34309
    sprite('pt615_08', 5)	# 34310-34314
    sprite('pt615_09', 5)	# 34315-34319
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 34320-34324
    label(133)
    sprite('pt615_09', 5)	# 34325-34329
    sprite('pt615_08', 5)	# 34330-34334
    sprite('pt615_09', 5)	# 34335-34339
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 34340-34344
    loopRest()
    if SLOT_97:
        _gotolabel(133)
    sprite('pt615_09', 1)	# 34345-34345
    Unknown21007(24, 40)
    Unknown21011(150)
    label(134)
    sprite('pt615_09', 5)	# 34346-34350
    sprite('pt615_08', 5)	# 34351-34355
    sprite('pt615_09', 5)	# 34356-34360
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 34361-34365
    loopRest()
    gotoLabel(134)
    label(140)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(142)
    sprite('pt030_00', 5)	# 34366-34370
    sprite('pt030_01', 5)	# 34371-34375
    label(141)
    sprite('pt030_02', 5)	# 34376-34380
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 34381-34385
    sprite('pt030_04', 5)	# 34386-34390
    sprite('pt030_05', 5)	# 34391-34395
    sprite('pt030_06', 5)	# 34396-34400
    sprite('pt030_07', 5)	# 34401-34405
    sprite('pt030_08', 5)	# 34406-34410
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 34411-34415
    sprite('pt030_10', 5)	# 34416-34420
    sprite('pt030_11', 5)	# 34421-34425
    sprite('pt030_12', 5)	# 34426-34430
    sprite('pt030_13', 5)	# 34431-34435
    loopRest()
    gotoLabel(141)
    label(142)
    clearUponHandler(3)
    physicsXImpulse(0)
    sprite('pt615_00', 5)	# 34436-34440
    sprite('pt615_01', 5)	# 34441-34445
    sprite('pt615_02', 5)	# 34446-34450
    SFX_0('019_cloth_b')
    sprite('pt615_03', 5)	# 34451-34455
    sprite('pt615_04', 5)	# 34456-34460
    sprite('pt615_05', 5)	# 34461-34465
    sprite('pt615_06', 5)	# 34466-34470
    SFX_1('bpt700pce')
    sprite('pt615_07', 5)	# 34471-34475
    sprite('pt615_08', 5)	# 34476-34480
    sprite('pt615_09', 5)	# 34481-34485
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 34486-34490
    label(143)
    sprite('pt615_09', 5)	# 34491-34495
    sprite('pt615_08', 5)	# 34496-34500
    sprite('pt615_09', 5)	# 34501-34505
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 34506-34510
    loopRest()
    if SLOT_97:
        _gotolabel(143)
    sprite('pt615_09', 1)	# 34511-34511
    Unknown21007(24, 40)
    Unknown21011(240)
    label(144)
    sprite('pt615_09', 5)	# 34512-34516
    sprite('pt615_08', 5)	# 34517-34521
    sprite('pt615_09', 5)	# 34522-34526
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 34527-34531
    loopRest()
    gotoLabel(144)
    label(150)
    sprite('pt000_00', 1)	# 34532-34532

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('pt000_00', 7)	# 34533-34539
    sprite('pt000_01', 7)	# 34540-34546
    sprite('pt000_02', 7)	# 34547-34553
    sprite('pt000_03', 7)	# 34554-34560
    sprite('pt000_04', 7)	# 34561-34567
    sprite('pt000_05', 7)	# 34568-34574
    sprite('pt000_06', 7)	# 34575-34581
    sprite('pt000_07', 7)	# 34582-34588
    sprite('pt000_08', 7)	# 34589-34595
    sprite('pt000_09', 7)	# 34596-34602
    sprite('pt000_10', 7)	# 34603-34609
    sprite('pt000_11', 7)	# 34610-34616
    sprite('pt000_12', 7)	# 34617-34623
    sprite('pt000_13', 7)	# 34624-34630
    gotoLabel(151)
    label(152)
    sprite('pt001_00', 7)	# 34631-34637
    SFX_1('bpt701uli')
    sprite('pt001_01', 5)	# 34638-34642
    sprite('pt001_02', 8)	# 34643-34650
    sprite('pt001_03', 8)	# 34651-34658
    sprite('pt001_04', 8)	# 34659-34666
    sprite('pt001_05', 8)	# 34667-34674
    sprite('pt001_06', 5)	# 34675-34679
    Unknown23018(1)
    label(153)
    sprite('pt000_00', 7)	# 34680-34686
    sprite('pt000_01', 7)	# 34687-34693
    sprite('pt000_02', 7)	# 34694-34700
    sprite('pt000_03', 7)	# 34701-34707
    sprite('pt000_04', 7)	# 34708-34714
    sprite('pt000_05', 7)	# 34715-34721
    sprite('pt000_06', 7)	# 34722-34728
    sprite('pt000_07', 7)	# 34729-34735
    sprite('pt000_08', 7)	# 34736-34742
    sprite('pt000_09', 7)	# 34743-34749
    sprite('pt000_10', 7)	# 34750-34756
    sprite('pt000_11', 7)	# 34757-34763
    sprite('pt000_12', 7)	# 34764-34770
    sprite('pt000_13', 7)	# 34771-34777
    gotoLabel(153)
    label(160)
    sprite('pt001_00', 7)	# 34778-34784
    SFX_1('bpt700rwi')
    sprite('pt001_01', 5)	# 34785-34789
    sprite('pt001_02', 8)	# 34790-34797
    sprite('pt001_03', 8)	# 34798-34805
    sprite('pt001_04', 8)	# 34806-34813
    sprite('pt001_05', 8)	# 34814-34821
    sprite('pt001_06', 5)	# 34822-34826
    sprite('pt000_00', 7)	# 34827-34833
    sprite('pt000_01', 7)	# 34834-34840
    sprite('pt000_02', 7)	# 34841-34847
    sprite('pt000_03', 7)	# 34848-34854
    sprite('pt000_04', 7)	# 34855-34861
    sprite('pt000_05', 7)	# 34862-34868
    sprite('pt000_06', 7)	# 34869-34875
    sprite('pt000_07', 7)	# 34876-34882
    sprite('pt000_08', 7)	# 34883-34889
    sprite('pt000_09', 7)	# 34890-34896
    sprite('pt000_10', 7)	# 34897-34903
    sprite('pt000_11', 7)	# 34904-34910
    sprite('pt000_12', 7)	# 34911-34917
    sprite('pt000_13', 7)	# 34918-34924
    Unknown2037(1)
    label(161)
    sprite('pt000_00', 7)	# 34925-34931
    sprite('pt000_01', 7)	# 34932-34938
    sprite('pt000_02', 7)	# 34939-34945
    sprite('pt000_03', 7)	# 34946-34952
    sprite('pt000_04', 7)	# 34953-34959
    sprite('pt000_05', 7)	# 34960-34966
    sprite('pt000_06', 7)	# 34967-34973
    sprite('pt000_07', 7)	# 34974-34980
    sprite('pt000_08', 7)	# 34981-34987
    sprite('pt000_09', 7)	# 34988-34994
    if (not SLOT_2):
        Unknown21007(24, 40)
        Unknown21011(240)
    sprite('pt000_10', 7)	# 34995-35001
    sprite('pt000_11', 7)	# 35002-35008
    sprite('pt000_12', 7)	# 35009-35015
    sprite('pt000_13', 7)	# 35016-35022
    Unknown2038(-1)
    gotoLabel(161)
    label(170)
    sprite('keep', 1)	# 35023-35023
    Unknown2037(1)
    Unknown2019(500)
    sprite('keep', 1)	# 35024-35024
    Unknown48('190000000200000036000000180000000200000036000000')
    if SLOT_IsInOverdrive2:
        if (not SLOT_39):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                pass
            else:
                Unknown2005()
        else:
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                pass
            else:
                Unknown2005()
    sprite('pt030_00', 5)	# 35025-35029
    physicsXImpulse(5000)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_145 < 120000):
                Unknown2037(0)
                sendToLabel(172)
    Unknown20000(1)
    sprite('pt030_01', 5)	# 35030-35034
    label(171)
    sprite('pt030_02', 5)	# 35035-35039
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 35040-35044
    sprite('pt030_04', 5)	# 35045-35049
    sprite('pt030_05', 5)	# 35050-35054
    sprite('pt030_06', 5)	# 35055-35059
    sprite('pt030_07', 5)	# 35060-35064
    sprite('pt030_08', 5)	# 35065-35069
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 35070-35074
    sprite('pt030_10', 5)	# 35075-35079
    sprite('pt030_11', 5)	# 35080-35084
    sprite('pt030_12', 5)	# 35085-35089
    sprite('pt030_13', 5)	# 35090-35094
    loopRest()
    gotoLabel(171)
    label(172)
    clearUponHandler(3)
    physicsXImpulse(0)
    sprite('pt611_03ex', 6)	# 35095-35100	 **attackbox here**
    Unknown2019(0)
    Unknown21007(24, 40)
    sprite('pt611_04ex', 8)	# 35101-35108	 **attackbox here**
    sprite('pt611_05ex', 4)	# 35109-35112	 **attackbox here**
    sprite('pt635_00', 7)	# 35113-35119
    sprite('pt635_01', 7)	# 35120-35126
    sprite('pt635_02', 7)	# 35127-35133
    if random_(2, 0, 50):
        SFX_1('bpt700bjb_1')
    else:
        SFX_1('bpt700bjb_2')
    sprite('pt635_03', 7)	# 35134-35140
    label(173)
    sprite('pt635_04', 1)	# 35141-35141
    if SLOT_97:
        _gotolabel(173)
    sprite('pt635_04', 20)	# 35142-35161
    sprite('pt635_04', 32767)	# 35162-67928
    Unknown21007(24, 39)
    Unknown21011(220)
    label(180)
    sprite('pt000_00', 1)	# 67929-67929

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)

    def upon_39():
        clearUponHandler(39)
        sendToLabel(183)
    Unknown2019(500)
    label(181)
    sprite('pt000_00', 7)	# 67930-67936
    sprite('pt000_01', 7)	# 67937-67943
    sprite('pt000_02', 7)	# 67944-67950
    sprite('pt000_03', 7)	# 67951-67957
    sprite('pt000_04', 7)	# 67958-67964
    sprite('pt000_05', 7)	# 67965-67971
    sprite('pt000_06', 7)	# 67972-67978
    sprite('pt000_07', 7)	# 67979-67985
    sprite('pt000_08', 7)	# 67986-67992
    sprite('pt000_09', 7)	# 67993-67999
    sprite('pt000_10', 7)	# 68000-68006
    sprite('pt000_11', 7)	# 68007-68013
    sprite('pt000_12', 7)	# 68014-68020
    sprite('pt000_13', 7)	# 68021-68027
    gotoLabel(181)
    label(182)
    sprite('pt636_00', 6)	# 68028-68033
    sprite('pt636_01', 32767)	# 68034-100800
    label(183)
    sprite('pt636_02', 10)	# 100801-100810
    SFX_1('bpt701uyu')
    sprite('pt636_03', 6)	# 100811-100816
    sprite('pt636_04', 6)	# 100817-100822
    Unknown23018(1)
    label(184)
    sprite('pt636_02', 10)	# 100823-100832
    sprite('pt636_03', 6)	# 100833-100838
    sprite('pt636_04', 6)	# 100839-100844
    gotoLabel(184)
    label(190)
    sprite('keep', 1)	# 100845-100845
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
    if (not SLOT_2):
        sendToLabel(191)
    sprite('pt003_00', 3)	# 100846-100848
    Unknown2005()
    sprite('pt003_01', 3)	# 100849-100851
    sprite('pt003_02', 3)	# 100852-100854
    label(191)
    sprite('pt001_00', 7)	# 100855-100861
    SFX_1('bpt700pla')
    sprite('pt001_01', 5)	# 100862-100866
    sprite('pt001_02', 8)	# 100867-100874
    sprite('pt001_03', 8)	# 100875-100882
    sprite('pt001_04', 8)	# 100883-100890
    sprite('pt001_05', 8)	# 100891-100898
    sprite('pt001_06', 5)	# 100899-100903
    Unknown2037(1)
    Unknown21011(370)
    label(192)
    sprite('pt000_00', 7)	# 100904-100910
    sprite('pt000_01', 7)	# 100911-100917
    sprite('pt000_02', 7)	# 100918-100924
    sprite('pt000_03', 7)	# 100925-100931
    sprite('pt000_04', 7)	# 100932-100938
    sprite('pt000_05', 7)	# 100939-100945
    if (not SLOT_2):
        Unknown21007(24, 40)
    sprite('pt000_06', 7)	# 100946-100952
    sprite('pt000_07', 7)	# 100953-100959
    sprite('pt000_08', 7)	# 100960-100966
    sprite('pt000_09', 7)	# 100967-100973
    sprite('pt000_10', 7)	# 100974-100980
    sprite('pt000_11', 7)	# 100981-100987
    sprite('pt000_12', 7)	# 100988-100994
    sprite('pt000_13', 7)	# 100995-101001
    Unknown2038(-1)
    gotoLabel(192)
    label(200)
    sprite('pt650_00', 1)	# 101002-101002
    SFX_1('bpt701bce')
    label(201)
    sprite('pt650_00', 1)	# 101003-101003
    if SLOT_97:
        _gotolabel(201)
    sprite('pt650_00', 30)	# 101004-101033
    sprite('pt650_00', 32767)	# 101034-133800
    Unknown21007(24, 40)
    Unknown21011(150)
    label(210)
    sprite('pt611_00', 3)	# 133801-133803

    def upon_40():
        clearUponHandler(40)
        SFX_1('bpt701ahe')
        Unknown23018(1)
    sprite('pt611_01', 4)	# 133804-133807
    sprite('pt611_02', 4)	# 133808-133811	 **attackbox here**
    GFX_1('ptef_drivethrow', 0)
    GFX_1('ptef_winsmoke', 1)
    GFX_1('ptef_winsmoke', 2)
    SFX_0('016_explode_0')
    sprite('pt611_03', 6)	# 133812-133817	 **attackbox here**
    sprite('pt611_04', 8)	# 133818-133825	 **attackbox here**
    sprite('pt611_05', 4)	# 133826-133829	 **attackbox here**
    sprite('pt611_06', 4)	# 133830-133833	 **attackbox here**
    sprite('pt611_07', 5)	# 133834-133838
    SFX_3('ptse_03')
    sprite('pt611_08', 5)	# 133839-133843
    sprite('pt611_09', 4)	# 133844-133847	 **attackbox here**
    sprite('pt611_10', 4)	# 133848-133851	 **attackbox here**
    sprite('pt611_11', 4)	# 133852-133855	 **attackbox here**
    sprite('pt611_12', 4)	# 133856-133859	 **attackbox here**
    sprite('pt611_13', 6)	# 133860-133865
    sprite('pt611_14', 6)	# 133866-133871	 **attackbox here**
    sprite('pt611_15', 6)	# 133872-133877
    sprite('pt611_14ex00', 6)	# 133878-133883	 **attackbox here**
    label(211)
    sprite('pt611_16', 7)	# 133884-133890
    GFX_1('ptef_winheart', 0)
    SFX_3('ptse_15')
    sprite('pt611_17', 7)	# 133891-133897
    sprite('pt611_18', 7)	# 133898-133904
    sprite('pt611_17', 7)	# 133905-133911
    sprite('pt611_16', 7)	# 133912-133918
    sprite('pt611_17', 7)	# 133919-133925
    sprite('pt611_18', 7)	# 133926-133932
    sprite('pt611_17', 7)	# 133933-133939
    sprite('pt611_16', 7)	# 133940-133946
    sprite('pt611_17', 7)	# 133947-133953
    sprite('pt611_18', 7)	# 133954-133960
    sprite('pt611_17', 7)	# 133961-133967
    gotoLabel(211)
    label(220)
    sprite('keep', 1)	# 133968-133968
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(224)
        elif (SLOT_38 == 1):
            sendToLabel(224)
    label(221)
    sprite('keep', 1)	# 133969-133969

    def upon_40():
        clearUponHandler(40)
        SFX_1('bpt701pku')
        sendToLabel(223)
    label(222)
    sprite('pt000_00', 7)	# 133970-133976
    sprite('pt000_01', 7)	# 133977-133983
    sprite('pt000_02', 7)	# 133984-133990
    sprite('pt000_03', 7)	# 133991-133997
    sprite('pt000_04', 7)	# 133998-134004
    sprite('pt000_05', 7)	# 134005-134011
    sprite('pt000_06', 7)	# 134012-134018
    sprite('pt000_07', 7)	# 134019-134025
    sprite('pt000_08', 7)	# 134026-134032
    sprite('pt000_09', 7)	# 134033-134039
    sprite('pt000_10', 7)	# 134040-134046
    sprite('pt000_11', 7)	# 134047-134053
    sprite('pt000_12', 7)	# 134054-134060
    sprite('pt000_13', 7)	# 134061-134067
    gotoLabel(222)
    label(223)
    sprite('pt650_00', 32767)	# 134068-166834
    Unknown23018(1)
    label(224)
    sprite('pt003_00', 4)	# 166835-166838
    Unknown2005()
    sprite('pt003_01', 4)	# 166839-166842
    sprite('pt003_02', 4)	# 166843-166846
    gotoLabel(221)

@State
def CmnActLose():
    sprite('pt620_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('bpt403_0', 100, 880046178, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt620_01', 6)	# 7-12
    sprite('pt620_02', 6)	# 13-18
    sprite('pt620_03', 6)	# 19-24
    SFX_0('019_cloth_b')
    sprite('pt620_04', 6)	# 25-30
    sprite('pt620_05', 6)	# 31-36
    sprite('pt620_06', 6)	# 37-42
    sprite('pt620_07', 6)	# 43-48
    sprite('pt620_08', 6)	# 49-54
    Unknown7014('ptse_05')
    sprite('pt620_09', 6)	# 55-60
    sprite('pt620_10', 6)	# 61-66
    sprite('pt620_09', 6)	# 67-72
    sprite('pt620_08', 6)	# 73-78
    sprite('pt620_09', 6)	# 79-84
    sprite('pt620_10', 6)	# 85-90
    sprite('pt620_11', 6)	# 91-96
    Unknown7015()
    sprite('pt620_12', 12)	# 97-108
    sprite('pt620_11', 6)	# 109-114
    Unknown23018(1)
    sprite('pt620_10', 6)	# 115-120
    SFX_3('ptse_29')
    sprite('pt620_09', 6)	# 121-126
    sprite('pt620_08', 6)	# 127-132
    sprite('pt620_09', 6)	# 133-138
    label(0)
    sprite('pt620_10', 6)	# 139-144
    sprite('pt620_09', 6)	# 145-150
    sprite('pt620_08', 6)	# 151-156
    sprite('pt620_09', 6)	# 157-162
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryWait():
    label(0)
    sprite('pt000_00', 7)	# 1-7
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
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
    label(0)
    sprite('pt620_10', 6)	# 1-6
    sprite('pt620_09', 6)	# 7-12
    sprite('pt620_08', 6)	# 13-18
    sprite('pt620_09', 6)	# 19-24
    gotoLabel(0)

@State
def EventDefLose2():
    sprite('pt063_11', 32767)	# 1-32767

@State
def EventNoDisp():
    sprite('keep', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventChouhatsu():
    sprite('pt300_00', 4)	# 1-4
    sprite('pt300_01', 4)	# 5-8
    sprite('pt300_02', 4)	# 9-12
    sprite('pt300_03', 6)	# 13-18
    sprite('pt300_04', 6)	# 19-24
    sprite('pt300_05', 7)	# 25-31
    sprite('pt300_06', 30)	# 32-61
    sprite('pt300_07', 7)	# 62-68
    SFX_3('ptse_00')
    sprite('pt300_08', 9)	# 69-77
    sprite('pt300_09', 6)	# 78-83
    sprite('pt000_00', 1)	# 84-84
    enterState('CmnActStand')

@State
def EventDownFaceUp():
    sprite('pt060_14', 32767)	# 1-32767
    loopRest()

@State
def EventDownFaceUpToStand():
    sprite('pt061_00', 3)	# 1-3
    sprite('pt061_01', 3)	# 4-6
    sprite('pt061_02', 3)	# 7-9
    sprite('pt061_03', 3)	# 10-12
    sprite('pt061_04', 3)	# 13-15
    sprite('pt061_05', 3)	# 16-18
    sprite('pt061_06', 2)	# 19-20
    sprite('pt061_07', 2)	# 21-22
    sprite('pt061_08', 2)	# 23-24
    sprite('pt061_09', 2)	# 25-26
    loopRest()
    enterState('CmnActStand')

@State
def EventDashLeaveOpposite():
    sprite('pt003_00', 3)	# 1-3
    Unknown2006()
    Unknown2005()
    sprite('pt003_01', 3)	# 4-6
    sprite('pt003_02', 3)	# 7-9
    sprite('pt032_00', 2)	# 10-11
    physicsXImpulse(25000)
    Unknown8007(100, 1, 1)
    EnableCollision(0)
    Unknown2034(0)
    sprite('pt032_01', 2)	# 12-13
    label(0)
    sprite('pt032_02', 4)	# 14-17
    sprite('pt032_03', 4)	# 18-21
    Unknown8006(100, 1, 1)
    sprite('pt032_04', 4)	# 22-25
    sprite('pt032_05', 4)	# 26-29
    sprite('pt032_06', 4)	# 30-33
    sprite('pt032_07', 4)	# 34-37
    Unknown8006(100, 1, 1)
    sprite('pt032_08', 4)	# 38-41
    loopRest()
    gotoLabel(0)

@State
def EventDefLose3():
    sprite('pt620_05', 32767)	# 1-32767

@State
def EventSitting():
    sprite('pt064_02', 32767)	# 1-32767

@State
def EventSittingEnd():
    sprite('pt064_02', 7)	# 1-7
    sprite('pt064_03', 7)	# 8-14
    sprite('pt064_04', 7)	# 15-21
    sprite('pt064_05', 7)	# 22-28
    sprite('pt064_06', 7)	# 29-35
    sprite('pt064_07', 7)	# 36-42
    sprite('pt064_08', 7)	# 43-49
    sprite('pt064_09', 7)	# 50-56
    sprite('pt064_10', 7)	# 57-63
    sprite('pt000_00', 1)	# 64-64
    enterState('CmnActStand')

@State
def EventVSAR1():
    Unknown2034(0)
    Unknown1000(-2400000)
    sprite('null', 32767)	# 1-32767

@State
def EventVSAR2():
    Unknown2034(0)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('pt030_00', 7)	# 1-7
    Unknown20000(1)
    sprite('pt030_01', 6)	# 8-13
    physicsXImpulse(1650)
    label(0)
    sprite('pt030_02', 6)	# 14-19
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 6)	# 20-25
    sprite('pt030_04', 6)	# 26-31
    sprite('pt030_05', 6)	# 32-37
    sprite('pt030_06', 6)	# 38-43
    sprite('pt030_07', 6)	# 44-49
    sprite('pt030_08', 6)	# 50-55
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 6)	# 56-61
    sprite('pt030_10', 6)	# 62-67
    sprite('pt030_11', 6)	# 68-73
    sprite('pt030_12', 6)	# 74-79
    sprite('pt030_13', 6)	# 80-85
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    Unknown20000(0)
    enterState('CmnActStand')

@State
def EventVSHA1():
    sprite('pt070_13', 8)	# 1-8
    sprite('pt070_12', 8)	# 9-16
    sprite('pt070_11', 8)	# 17-24
    sprite('pt070_10', 32767)	# 25-32791

@State
def EventPhantom():
    sprite('pt000_00', 7)	# 1-7
    GFX_0('ptPhantom_2', 0)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(-20000)
    Unknown2019(-500)
    Unknown35()
    SFX_0('022_magiccircle_b')
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    loopRest()
    enterState('CmnActStand')

@State
def EventPhantomDelete():
    sprite('keep', 2)	# 1-2
    Unknown21007(4, 32)
    loopRest()
    enterState('CmnActStand')

@State
def EventVSHA2():
    sprite('pt070_10', 8)	# 1-8
    sprite('pt070_11', 8)	# 9-16
    sprite('pt070_12', 8)	# 17-24
    sprite('pt070_13', 8)	# 25-32
    loopRest()
    enterState('EventPhantom')

@State
def EventTKVsPT_StompTao():
    Unknown2006()
    Unknown1000(-1100000)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2018(1, 80)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_19 < 100000):
            sendToLabel(1)
    sprite('pt030_00', 7)	# 1-7
    sprite('pt030_01', 5)	# 8-12
    Unknown20000(1)
    physicsXImpulse(8000)
    loopRest()
    label(0)
    sprite('pt030_02', 5)	# 13-17
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 18-22
    sprite('pt030_04', 5)	# 23-27
    sprite('pt030_05', 5)	# 28-32
    sprite('pt030_06', 5)	# 33-37
    sprite('pt030_07', 5)	# 38-42
    sprite('pt030_08', 5)	# 43-47
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 48-52
    sprite('pt030_10', 5)	# 53-57
    sprite('pt030_11', 5)	# 58-62
    sprite('pt030_12', 5)	# 63-67
    sprite('pt030_13', 5)	# 68-72
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    Unknown20000(0)
    Unknown1084(1)
    sprite('keep', 32767)	# 73-32839
    SFX_3('ptse_00')
    SFX_0('021_bonecleak_0')
    ScreenShake(0, 8000)
    GFX_1('ef_hits', -1)
    GFX_1('ef_jumpsmoke00', -1)
    loopRest()

@State
def EventTKVsPT_Surprised():
    EnableCollision(0)
    Unknown2018(1, 80)
    sprite('pt000_00', 4)	# 1-4
    sprite('pt050_00', 4)	# 5-8
    sprite('pt050_00', 2)	# 9-10
    physicsXImpulse(-40000)
    sprite('pt050_01', 2)	# 11-12
    sprite('pt050_01', 2)	# 13-14
    physicsXImpulse(0)
    Unknown1004()
    teleportRelativeX(1000)
    loopRest()
    SLOT_51 = 0
    label(0)
    sprite('pt050_01', 2)	# 15-16
    teleportRelativeX(-2000)
    sprite('pt050_01', 2)	# 17-18
    teleportRelativeX(2000)
    SLOT_51 = (SLOT_51 + 1)
    loopRest()
    (SLOT_51 < 8)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('pt050_01', 4)	# 19-22
    Unknown1005()
    sprite('pt050_00', 4)	# 23-26
    sprite('pt615_00', 4)	# 27-30
    sprite('pt615_01', 4)	# 31-34
    sprite('pt615_02', 4)	# 35-38
    SFX_0('019_cloth_b')
    sprite('pt615_03', 4)	# 39-42
    sprite('pt615_04', 4)	# 43-46
    sprite('pt615_05', 4)	# 47-50
    sprite('pt615_06', 4)	# 51-54
    sprite('pt615_07', 4)	# 55-58
    loopRest()
    SLOT_51 = 0
    label(1)
    sprite('pt615_08', 5)	# 59-63
    sprite('pt615_09', 5)	# 64-68
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 69-73
    sprite('pt615_09', 5)	# 74-78
    sprite('pt615_08', 5)	# 79-83
    sprite('pt615_09', 5)	# 84-88
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 89-93
    sprite('pt615_09', 90)	# 94-183
    SLOT_51 = (SLOT_51 + 1)
    loopRest()
    (SLOT_51 < 3)
    if SLOT_ReturnVal:
        _gotolabel(1)
    sprite('pt615_09', 32767)	# 184-32950
    loopRest()

@State
def EventTKVsPT_JumpAway():
    EnableCollision(0)
    Unknown2018(1, 80)
    sprite('pt615_03', 2)	# 1-2
    sprite('pt615_02', 2)	# 3-4
    sprite('pt052_01', 2)	# 5-6
    sprite('pt052_02', 2)	# 7-8
    sprite('pt052_03', 2)	# 9-10
    Unknown1004()
    teleportRelativeX(2000)
    loopRest()
    SLOT_51 = 0
    label(0)
    sprite('pt052_03', 2)	# 11-12
    teleportRelativeX(-4000)
    sprite('pt052_03', 2)	# 13-14
    teleportRelativeX(4000)
    SLOT_51 = (SLOT_51 + 1)
    loopRest()
    (SLOT_51 < 8)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('pt052_02', 2)	# 15-16
    Unknown1005()
    loopRest()
    sendToLabelUpon(2, 2)
    sprite('pt033_01', 1)	# 17-17
    physicsXImpulse(-32000)
    physicsYImpulse(2000)
    setGravity(1500)
    Unknown8002()
    sprite('pt033_02', 1)	# 18-18
    sprite('pt033_03', 1)	# 19-19
    loopRest()
    label(1)
    sprite('pt033_02', 3)	# 20-22
    sprite('pt033_03', 3)	# 23-25
    loopRest()
    gotoLabel(1)
    label(2)
    clearUponHandler(2)
    sprite('pt033_04', 2)	# 26-27
    sprite('pt033_05', 2)	# 28-29
    Unknown1084(1)
    Unknown1000(-260000)
    Unknown8000(100, 1, 1)
    sprite('pt033_06', 2)	# 30-31
    loopRest()
    enterState('CmnActStand')

@State
def EventPTHood():
    sprite('pt600_00', 32767)	# 1-32767

@State
def EventPTHoodEnd():
    sprite('pt600_01', 6)	# 1-6
    sprite('pt600_02', 6)	# 7-12
    SFX_0('019_cloth_c')
    sprite('pt600_03', 6)	# 13-18
    sprite('pt600_04', 6)	# 19-24
    sprite('pt600_05', 7)	# 25-31
    sprite('pt600_06', 5)	# 32-36
    GFX_1('ptef_entrylightA', 0)
    sprite('pt600_07', 5)	# 37-41
    Unknown23119(13145800, 16, 2)
    sprite('pt600_08', 4)	# 42-45
    sprite('pt600_08', 3)	# 46-48
    GFX_1('ptef_entrylightB', 0)
    sprite('pt600_08', 3)	# 49-51
    sprite('pt600_09', 6)	# 52-57
    sprite('pt600_10', 8)	# 58-65	 **attackbox here**
    SFX_3('ptse_13')
    GFX_0('yugami_ring', 0)
    GFX_1('ptef_entrymc', 0)
    sprite('pt600_11', 6)	# 66-71	 **attackbox here**
    sprite('pt600_12', 5)	# 72-76	 **attackbox here**
    sprite('pt600_10ex00', 5)	# 77-81	 **attackbox here**
    sprite('pt600_11ex00', 5)	# 82-86	 **attackbox here**
    sprite('pt600_12ex00', 5)	# 87-91
    sprite('pt600_13', 6)	# 92-97
    sprite('pt600_14', 6)	# 98-103
    sprite('pt600_15', 6)	# 104-109
    sprite('pt600_16', 6)	# 110-115
    enterState('CmnActStand')

@State
def EventPTWalkaway():
    EnableCollision(0)
    Unknown2034(0)
    physicsXImpulse(6200)
    sprite('pt030_00', 5)	# 1-5
    sprite('pt030_01', 5)	# 6-10
    sprite('pt030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 16-20
    sprite('pt030_04', 5)	# 21-25
    sprite('pt030_05', 5)	# 26-30
    sprite('pt030_06', 5)	# 31-35
    sprite('pt030_07', 5)	# 36-40
    sprite('pt030_08', 5)	# 41-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 46-50
    sprite('pt030_10', 5)	# 51-55
    sprite('pt030_11', 5)	# 56-60
    sprite('pt030_12', 5)	# 61-65
    sprite('pt030_13', 5)	# 66-70
    sprite('pt030_02', 5)	# 71-75
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 76-80
    sprite('pt030_04', 5)	# 81-85
    sprite('pt030_05', 5)	# 86-90
    sprite('pt030_06', 5)	# 91-95
    sprite('pt030_07', 5)	# 96-100
    sprite('pt030_08', 5)	# 101-105
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 106-110
    sprite('pt030_10', 5)	# 111-115
    sprite('pt030_11', 5)	# 116-120
    sprite('pt030_12', 5)	# 121-125
    sprite('pt030_13', 5)	# 126-130
    sprite('pt030_02', 5)	# 131-135
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 136-140
    sprite('pt030_04', 5)	# 141-145
    sprite('pt030_05', 5)	# 146-150
    sprite('pt030_06', 5)	# 151-155
    sprite('pt030_07', 5)	# 156-160
    sprite('pt030_08', 5)	# 161-165
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 166-170
    sprite('pt030_10', 5)	# 171-175
    sprite('pt030_11', 5)	# 176-180
    sprite('pt030_12', 5)	# 181-185
    sprite('pt030_13', 5)	# 186-190

@State
def EventYorokeStart():
    sprite('pt070_00', 5)	# 1-5
    sprite('pt070_01', 5)	# 6-10
    label(0)
    sprite('pt070_02', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def EventYorokeEnd():
    sprite('pt070_03', 5)	# 1-5
    sprite('pt070_02', 5)	# 6-10
    sprite('pt070_01', 5)	# 11-15
    sprite('pt070_00', 5)	# 16-20
    loopRest()
    enterState('CmnActStand')

@State
def EventWarp():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown2034(0)
        Unknown3032()
    sprite('pt071_00', 4)	# 1-4
    sprite('pt071_01', 4)	# 5-8
    sprite('pt071_02', 2)	# 9-10
    sprite('pt071_03', 2)	# 11-12
    sprite('pt071_04', 2)	# 13-14
    sprite('pt071_05', 2)	# 15-16
    sprite('pt071_06', 2)	# 17-18
    sprite('pt071_07', 2)	# 19-20
    sprite('pt071_08', 2)	# 21-22
    sprite('pt071_09', 2)	# 23-24
    sprite('pt071_02', 2)	# 25-26
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    sprite('pt071_03', 2)	# 27-28
    sprite('pt071_04', 2)	# 29-30
    sprite('pt071_05', 2)	# 31-32
    sprite('pt071_06', 2)	# 33-34
    sprite('pt071_07', 2)	# 35-36
    sprite('pt071_08', 2)	# 37-38
    sprite('pt071_09', 2)	# 39-40
    sprite('pt071_02', 2)	# 41-42
    sprite('pt071_03', 2)	# 43-44
    sprite('pt071_04', 2)	# 45-46
    sprite('pt071_05', 2)	# 47-48
    sprite('pt071_06', 2)	# 49-50
    sprite('pt071_07', 2)	# 51-52
    GFX_1('haef_event_lose_end', 103)
    Unknown1000(-500000)
    sprite('pt071_08', 2)	# 53-54
    sprite('pt071_09', 2)	# 55-56
    sprite('null', 32767)	# 57-32823
    loopRest()

@State
def EventPTFrameOut():
    Unknown2034(0)
    Unknown1000(-900000)
    sprite('null', 32767)	# 1-32767

@State
def EventPTWalkFrameIn():
    Unknown2034(0)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('pt030_00', 7)	# 1-7
    sprite('pt030_01', 5)	# 8-12
    physicsXImpulse(4650)
    label(0)
    sprite('pt030_02', 5)	# 13-17
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 18-22
    sprite('pt030_04', 5)	# 23-27
    sprite('pt030_05', 5)	# 28-32
    sprite('pt030_06', 5)	# 33-37
    sprite('pt030_07', 5)	# 38-42
    sprite('pt030_08', 5)	# 43-47
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 48-52
    sprite('pt030_10', 5)	# 53-57
    sprite('pt030_11', 5)	# 58-62
    sprite('pt030_12', 5)	# 63-67
    sprite('pt030_13', 5)	# 68-72
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventPTSuwari():
    sprite('pt620_00', 6)	# 1-6
    sprite('pt620_01', 6)	# 7-12
    sprite('pt620_02', 6)	# 13-18
    Unknown8000(100, 1, 1)
    sprite('pt620_03', 6)	# 19-24
    sprite('pt620_04', 6)	# 25-30
    sprite('pt620_05', 32767)	# 31-32797

@State
def EventPTFSitDown():
    sprite('pt064_10', 5)	# 1-5
    sprite('pt064_09', 5)	# 6-10
    sprite('pt064_08', 5)	# 11-15
    sprite('pt064_07', 5)	# 16-20
    sprite('pt064_06', 5)	# 21-25
    sprite('pt064_05', 5)	# 26-30
    sprite('pt064_04', 5)	# 31-35
    Unknown8000(100, 1, 1)
    sprite('pt064_03', 32767)	# 36-32802

@State
def EventPTFSitDown02():
    sprite('pt064_02', 5)	# 1-5
    sprite('pt064_01', 5)	# 6-10
    sprite('pt064_00', 5)	# 11-15
    sprite('pt063_11', 32767)	# 16-32782
    Unknown8003(100, 1, 1)

@State
def EventPTFDownLoop():
    sprite('pt063_11', 32767)	# 1-32767

@State
def EventPTFDown2Stand01():
    sprite('pt064_00', 5)	# 1-5
    sprite('pt064_01', 5)	# 6-10
    sprite('pt064_02', 5)	# 11-15
    sprite('pt064_03', 32767)	# 16-32782

@State
def EventPTFDown2Stand02():
    sprite('pt064_04', 5)	# 1-5
    sprite('pt064_05', 5)	# 6-10
    sprite('pt064_06', 5)	# 11-15
    sprite('pt064_07', 5)	# 16-20
    sprite('pt064_08', 5)	# 21-25
    sprite('pt064_09', 5)	# 26-30
    sprite('pt064_10', 5)	# 31-35
    sprite('pt000_00', 1)	# 36-36
    enterState('CmnActStand')

@State
def EventPTExcite():
    sprite('pt300_00', 4)	# 1-4
    sprite('pt300_01', 4)	# 5-8
    sprite('pt300_02', 4)	# 9-12
    sprite('pt300_03', 6)	# 13-18
    sprite('pt300_04', 6)	# 19-24
    sprite('pt300_05', 7)	# 25-31
    sprite('pt300_06', 30)	# 32-61
    sprite('pt300_07', 7)	# 62-68
    SFX_3('ptse_00')
    sprite('pt300_08', 9)	# 69-77
    sprite('pt300_09', 6)	# 78-83
    sprite('pt000_00', 1)	# 84-84
    enterState('CmnActStand')

@State
def EventStartWithBN():
    Unknown2018(1, 100)
    Unknown13(7)
    GFX_0('EventPT01_ibbn', -1)
    Unknown38(7, 1)
    sprite('pt063_11', 32767)	# 1-32767
    loopRest()

@State
def EventWorpOutBN():
    sprite('keep', 100)	# 1-100
    Unknown21007(7, 32)
    sprite('keep', 32767)	# 101-32867
    Unknown13(7)
    loopRest()

@State
def EventHZVsPT_Yoroke():
    sprite('pt043_00', 32767)	# 1-32767
    loopRest()

@State
def EventHZVsPT_YorokeToWarp():
    sprite('pt010_01', 6)	# 1-6
    sprite('pt010_00', 6)	# 7-12
    loopRest()
    enterState('EventWarp')

@State
def EventVSHAWalk():
    Unknown2034(0)
    Unknown2037(1)
    Unknown1000(-900000)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('pt030_00', 7)	# 1-7
    Unknown20000(1)
    GFX_0('ptPhantom_2', 0)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(-40000)
    physicsXImpulse(3250)
    Unknown2019(-500)
    Unknown35()
    physicsXImpulse(3250)
    sprite('pt030_01_ex', 6)	# 8-13
    label(0)
    sprite('pt030_02_ex', 6)	# 14-19
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 6)	# 20-25
    sprite('pt030_04_ex', 6)	# 26-31
    sprite('pt030_05_ex', 6)	# 32-37
    sprite('pt030_06_ex', 6)	# 38-43
    sprite('pt030_07_ex', 6)	# 44-49
    sprite('pt030_08_ex', 6)	# 50-55
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 6)	# 56-61
    sprite('pt030_10_ex', 6)	# 62-67
    sprite('pt030_11_ex', 6)	# 68-73
    sprite('pt030_12_ex', 6)	# 74-79
    sprite('pt030_13_ex', 6)	# 80-85
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    Unknown20000(0)
    Unknown36(4)
    physicsXImpulse(0)
    Unknown35()
    enterState('CmnActStand')

@State
def EventPHTeni():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown2034(0)
        Unknown3032()
    label(0)
    sprite('pt070_02', 5)	# 1-5
    sprite('pt070_03', 5)	# 6-10
    sprite('pt070_02', 5)	# 11-15
    sprite('pt070_03', 5)	# 16-20
    sprite('pt070_02', 5)	# 21-25
    Unknown3004(-5)
    sprite('pt070_03', 5)	# 26-30
    sprite('pt070_02', 5)	# 31-35
    sprite('pt070_03', 5)	# 36-40
    sprite('pt070_02', 5)	# 41-45
    sprite('pt070_03', 5)	# 46-50
    sprite('pt070_02', 5)	# 51-55
    sprite('pt070_03', 5)	# 56-60
    sprite('pt070_02', 5)	# 61-65
    sprite('pt070_03', 5)	# 66-70
    sprite('pt070_02', 5)	# 71-75
    sprite('pt070_03', 5)	# 76-80
    GFX_1('haef_event_lose_end', 103)
    Unknown1000(-500000)
    sprite('pt070_02', 5)	# 81-85
    sprite('pt070_03', 5)	# 86-90
    sprite('null', 32767)	# 91-32857
    loopRest()

@State
def EventNoAtk5C():
    sprite('pt202_00', 2)	# 1-2
    sprite('pt202_01', 3)	# 3-5
    sprite('pt202_03', 4)	# 6-9
    SFX_0('003_swing_grap_0_1')
    sprite('pt202_04', 6)	# 10-15	 **attackbox here**
    sprite('pt202_05', 4)	# 16-19
    SFX_0('014_electric_m')
    sprite('pt202_06', 4)	# 20-23
    sprite('pt202_07', 4)	# 24-27
    sprite('pt202_08', 1)	# 28-28
    sprite('pt202_09', 2)	# 29-30
    sprite('pt202_10', 4)	# 31-34
    loopRest()
    enterState('CmnActStand')

@State
def EventVSTKTunTUn():
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 200000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('pt030_00', 7)	# 1-7
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(-40000)
    physicsXImpulse(3250)
    Unknown2019(-1000)
    Unknown35()
    physicsXImpulse(3250)
    sprite('pt030_01', 6)	# 8-13
    label(0)
    sprite('pt030_02_ex', 6)	# 14-19
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 6)	# 20-25
    sprite('pt030_04_ex', 6)	# 26-31
    sprite('pt030_05_ex', 6)	# 32-37
    sprite('pt030_06_ex', 6)	# 38-43
    sprite('pt030_07_ex', 6)	# 44-49
    sprite('pt030_08_ex', 6)	# 50-55
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 6)	# 56-61
    sprite('pt030_10_ex', 6)	# 62-67
    sprite('pt030_11_ex', 6)	# 68-73
    sprite('pt030_12_ex', 6)	# 74-79
    sprite('pt030_13_ex', 6)	# 80-85
    gotoLabel(0)
    label(1)
    sprite('pt615_00', 4)	# 86-89
    physicsXImpulse(0)
    sprite('pt615_01', 4)	# 90-93
    sprite('pt615_02', 4)	# 94-97
    SFX_0('019_cloth_b')
    sprite('pt615_03', 4)	# 98-101
    sprite('pt615_04', 4)	# 102-105
    sprite('pt615_05', 4)	# 106-109
    sprite('pt615_06', 4)	# 110-113
    sprite('pt615_07', 4)	# 114-117
    loopRest()
    label(2)
    sprite('pt615_09', 5)	# 118-122
    sprite('pt615_08', 5)	# 123-127
    sprite('pt615_09', 5)	# 128-132
    SFX_3('ptse_25')
    sprite('pt615_10', 5)	# 133-137
    loopRest()
    gotoLabel(2)

@State
def EventVSBLWalk():
    Unknown2034(0)
    Unknown2037(1)
    Unknown1000(-900000)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 120000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('pt030_00', 7)	# 1-7
    physicsXImpulse(5300)
    sprite('pt030_01', 6)	# 8-13
    label(0)
    sprite('pt030_02', 6)	# 14-19
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 6)	# 20-25
    sprite('pt030_04', 6)	# 26-31
    sprite('pt030_05', 6)	# 32-37
    sprite('pt030_06', 6)	# 38-43
    sprite('pt030_07', 6)	# 44-49
    sprite('pt030_08', 6)	# 50-55
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 6)	# 56-61
    sprite('pt030_10', 6)	# 62-67
    sprite('pt030_11', 6)	# 68-73
    sprite('pt030_12', 6)	# 74-79
    sprite('pt030_13', 6)	# 80-85
    gotoLabel(0)
    label(1)
    sprite('pt033_00', 1)	# 86-86
    sprite('pt033_01', 2)	# 87-88
    physicsXImpulse(-18500)
    physicsYImpulse(12800)
    setGravity(1550)
    Unknown8002()
    sprite('pt033_02', 3)	# 89-91
    sendToLabelUpon(2, 3)
    label(2)
    sprite('pt033_03', 3)	# 92-94
    sprite('pt033_02', 3)	# 95-97
    gotoLabel(2)
    label(3)
    clearUponHandler(2)
    sprite('pt033_04', 2)	# 98-99
    sprite('pt033_05', 2)	# 100-101
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('pt033_06', 2)	# 102-103
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventDefEntryReverseWait():
    sprite('pt000_00', 7)	# 1-7
    Unknown2005()
    label(0)
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    sprite('pt000_00', 7)	# 99-105
    loopRest()
    gotoLabel(0)

@State
def EventStandTurn():
    sprite('pt003_00', 3)	# 1-3
    Unknown2005()
    sprite('pt003_01', 3)	# 4-6
    sprite('pt003_02', 3)	# 7-9
    loopRest()
    enterState('CmnActStand')

@State
def EventUltimateLoop():

    def upon_IMMEDIATE():
        Unknown1084(1)
    sprite('pt431_00', 3)	# 1-3
    sprite('pt431_00', 3)	# 4-6
    sprite('pt431_01', 3)	# 7-9
    sprite('pt431_02', 3)	# 10-12
    sprite('pt431_03', 3)	# 13-15
    sprite('pt431_04', 3)	# 16-18
    sprite('pt431_05', 10)	# 19-28
    sprite('pt431_06', 3)	# 29-31
    GFX_0('pt431_tornado', -1)
    sprite('pt431_07', 3)	# 32-34
    sprite('pt431_08', 3)	# 35-37
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_09', 3)	# 38-40
    sprite('pt431_10', 3)	# 41-43	 **attackbox here**
    sprite('pt431_11', 3)	# 44-46
    sprite('pt431_12', 3)	# 47-49
    sprite('pt431_13', 3)	# 50-52
    loopRest()
    sprite('pt431_09', 3)	# 53-55
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_10', 4)	# 56-59	 **attackbox here**
    sprite('pt431_11', 3)	# 60-62
    sprite('pt431_12', 3)	# 63-65
    sprite('pt431_13', 3)	# 66-68
    SFX_0('005_swing_grap_2_0')
    sprite('pt431_14', 3)	# 69-71	 **attackbox here**
    GFX_0('pt431_smoke', -1)
    sprite('pt431_15', 3)	# 72-74	 **attackbox here**
    sprite('pt431_16', 3)	# 75-77	 **attackbox here**
    SFX_0('005_swing_grap_2_0')
    label(0)
    sprite('pt431_14', 3)	# 78-80	 **attackbox here**
    GFX_0('pt431_smoke', -1)
    sprite('pt431_15', 3)	# 81-83	 **attackbox here**
    sprite('pt431_16', 3)	# 84-86	 **attackbox here**
    SFX_0('005_swing_grap_2_0')
    loopRest()
    gotoLabel(0)

@State
def EventUltimateLoopToStop():
    sprite('pt431_17', 5)	# 1-5
    sprite('pt431_18', 5)	# 6-10
    sprite('pt431_19', 5)	# 11-15
    sprite('pt431_20', 5)	# 16-20
    sprite('pt431_21', 5)	# 21-25
    sprite('pt431_22', 5)	# 26-30
    loopRest()
    sprite('pt431_23', 6)	# 31-36
    sprite('pt431_24', 6)	# 37-42
    sprite('pt431_25', 6)	# 43-48
    sprite('pt431_26', 6)	# 49-54
    sprite('pt431_27', 32767)	# 55-32821
    loopRest()

@State
def EventUltimateLoopEnd():
    sprite('pt431_28', 6)	# 1-6
    sprite('pt431_29', 6)	# 7-12
    sprite('pt431_30', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def Act2Evetn_Down():
    sprite('pt063_11', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_tmvspt_00():
    sprite('keep', 1)	# 1-1
    Unknown1000(-360000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_tmvspt_01():

    def upon_IMMEDIATE():

        def upon_CLEAR_OR_EXIT():
            if SLOT_38:
                if (SLOT_22 < 260000):
                    Unknown1084(1)
                    Unknown1000(-260000)
                    sendToLabel(0)
                    clearUponHandler(3)
            elif (SLOT_22 > (-260000)):
                Unknown1084(1)
                Unknown1000(-260000)
                sendToLabel(0)
                clearUponHandler(3)
    sprite('pt030_00', 7)	# 1-7
    physicsXImpulse(1000)
    sprite('pt030_01_ex', 8)	# 8-15
    label(9)
    sprite('pt030_02_ex', 8)	# 16-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)	# 24-31
    sprite('pt030_04_ex', 8)	# 32-39
    sprite('pt030_05_ex', 8)	# 40-47
    sprite('pt030_06_ex', 8)	# 48-55
    sprite('pt030_07_ex', 8)	# 56-63
    sprite('pt030_08_ex', 8)	# 64-71
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 8)	# 72-79
    sprite('pt030_10_ex', 8)	# 80-87
    sprite('pt030_11_ex', 8)	# 88-95
    sprite('pt030_12_ex', 8)	# 96-103
    sprite('pt030_13_ex', 8)	# 104-111
    gotoLabel(9)
    label(0)
    sprite('keep', 2)	# 112-113
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_tmvspt_02():
    sprite('pt063_11', 32767)	# 1-32767
    Unknown1000(-160000)
    loopRest()

@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_WalkIn():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1000(-720000)

        def upon_CLEAR_OR_EXIT():
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
    sprite('pt030_00', 5)	# 1-5
    physicsXImpulse(4650)
    sprite('pt030_01', 5)	# 6-10
    label(9)
    sprite('pt030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)	# 16-20
    sprite('pt030_04', 5)	# 21-25
    sprite('pt030_05', 5)	# 26-30
    sprite('pt030_06', 5)	# 31-35
    sprite('pt030_07', 5)	# 36-40
    sprite('pt030_08', 5)	# 41-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)	# 46-50
    sprite('pt030_10', 5)	# 51-55
    sprite('pt030_11', 5)	# 56-60
    sprite('pt030_12', 5)	# 61-65
    sprite('pt030_13', 5)	# 66-70
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)	# 71-71
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Muchorin():
    sprite('pt203_00', 4)	# 1-4
    sprite('pt203_01', 4)	# 5-8
    sprite('pt203_02', 4)	# 9-12
    sprite('pt203_02', 4)	# 13-16
    sprite('pt203_03', 4)	# 17-20
    GFX_0('pt203_stick', 0)
    sprite('pt203_04', 4)	# 21-24
    SFX_3('ptse_13')
    sprite('pt203_05', 32767)	# 25-32791
    loopRest()

@State
def Act2Event_MuchorinEnd():
    sprite('pt203_06', 4)	# 1-4
    sprite('pt203_07', 4)	# 5-8
    sprite('pt203_08', 4)	# 9-12
    sprite('pt203_09', 4)	# 13-16
    sprite('pt203_10', 4)	# 17-20
    sprite('pt203_11', 4)	# 21-24
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Yoin():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        Unknown1000(-290000)
    sprite('pt201_05', 10)	# 1-10	 **attackbox here**
    SFX_3('ptse_16')
    sprite('pt201_06', 5)	# 11-15
    sprite('pt201_07', 5)	# 16-20
    sprite('pt201_08', 5)	# 21-25
    sprite('pt201_09', 4)	# 26-29
    Unknown8000(100, 1, 1)
    sprite('pt201_10', 5)	# 30-34
    sprite('pt201_11', 5)	# 35-39
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Chouhatsu():
    sprite('pt300_00', 4)	# 1-4
    sprite('pt300_01', 4)	# 5-8
    sprite('pt300_02', 4)	# 9-12
    sprite('pt300_03', 6)	# 13-18
    sprite('pt300_04', 6)	# 19-24
    sprite('pt300_05', 7)	# 25-31
    sprite('pt300_06', 30)	# 32-61
    sprite('pt300_07', 7)	# 62-68
    SFX_3('ptse_00')
    sprite('pt300_08', 9)	# 69-77
    sprite('pt300_09', 6)	# 78-83
    sprite('pt000_00', 1)	# 84-84
    enterState('CmnActStand')

@State
def Act2Event_Magica():
    sprite('pt406_00', 5)	# 1-5
    sprite('pt406_01', 5)	# 6-10
    sprite('pt406_02', 5)	# 11-15
    label(0)
    sprite('pt406_03', 8)	# 16-23	 **attackbox here**
    SFX_3('ptse_00')
    sprite('pt406_04', 7)	# 24-30	 **attackbox here**
    sprite('pt406_05', 7)	# 31-37	 **attackbox here**
    sprite('pt406_06', 8)	# 38-45	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act2Event_MagicaEnd():
    sprite('keep', 2)	# 1-2
    sprite('pt406_07', 5)	# 3-7
    sprite('pt406_08', 5)	# 8-12
    sprite('pt406_09', 5)	# 13-17
    sprite('pt406_10', 5)	# 18-22
    sprite('pt406_11', 5)	# 23-27
    sprite('pt406_12', 5)	# 28-32
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_RunOut():

    def upon_IMMEDIATE():
        Unknown2034(0)
        EnableCollision(0)
    sprite('pt032_00', 3)	# 1-3
    physicsXImpulse(24000)
    sprite('pt032_01', 3)	# 4-6
    Unknown2037(4)
    label(0)
    sprite('pt032_02', 4)	# 7-10
    Unknown2038(-1)
    sprite('pt032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('pt032_04', 4)	# 15-18
    sprite('pt032_05', 4)	# 19-22
    sprite('pt032_06', 4)	# 23-26
    sprite('pt032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('pt032_08', 4)	# 31-34
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('null', 32767)	# 35-32801
    Unknown1084(1)
    Unknown3038(1)
    loopRest()

@State
def Act2Event_cevspt_00():
    sprite('pt203_00', 4)	# 1-4
    sprite('pt203_01', 4)	# 5-8
    sprite('pt203_02', 4)	# 9-12
    sprite('pt203_02', 4)	# 13-16
    sprite('pt203_03', 4)	# 17-20
    GFX_0('pt203_stick', 0)
    sprite('pt203_04', 4)	# 21-24
    SFX_3('ptse_13')
    sprite('pt203_05', 32767)	# 25-32791
    loopRest()

@State
def Act2Event_cevspt_01():
    sprite('pt203_06', 4)	# 1-4
    sprite('pt203_07', 4)	# 5-8
    sprite('pt203_08', 4)	# 9-12
    sprite('pt203_09', 4)	# 13-16
    sprite('pt203_10', 4)	# 17-20
    sprite('pt203_11', 4)	# 21-24
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_cevspt_02():
    sprite('pt030_00', 7)	# 1-7
    physicsXImpulse(1000)
    sprite('pt030_01_ex', 8)	# 8-15
    sprite('pt030_02_ex', 8)	# 16-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)	# 24-31
    sprite('pt030_04_ex', 8)	# 32-39
    sprite('pt030_05_ex', 8)	# 40-47
    sprite('pt030_06_ex', 8)	# 48-55
    sprite('pt030_07_ex', 8)	# 56-63
    sprite('pt030_08_ex', 8)	# 64-71
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 8)	# 72-79
    sprite('pt030_10_ex', 8)	# 80-87
    sprite('pt030_11_ex', 8)	# 88-95
    sprite('pt030_12_ex', 8)	# 96-103
    sprite('pt030_13_ex', 8)	# 104-111
    sprite('pt063_00', 3)	# 112-114
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    Unknown1043()
    sprite('pt063_01', 3)	# 115-117
    sprite('pt063_02', 3)	# 118-120
    sprite('pt063_03', 3)	# 121-123
    sprite('pt063_04', 3)	# 124-126
    sprite('pt063_05', 3)	# 127-129
    sprite('pt063_06', 2)	# 130-131
    physicsXImpulse(0)
    physicsYImpulse(3000)
    Unknown1043()
    SFX_0('209_down_normal_0')
    sprite('pt063_07', 2)	# 132-133
    sprite('pt063_08', 3)	# 134-136
    sprite('pt063_09', 3)	# 137-139
    sprite('pt063_10', 3)	# 140-142
    sprite('pt063_11', 32767)	# 143-32909
    loopRest()

@State
def Act2Event_ptvsmi_00():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown1000(-920000)
    sprite('pt000_00', 7)	# 1-7
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    Unknown20000(0)
    GFX_0('Act2Event_Camera', -1)
    Unknown38(11, 1)
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    label(0)
    sprite('pt000_00', 7)	# 99-105
    sprite('pt000_01', 7)	# 106-112
    sprite('pt000_02', 7)	# 113-119
    sprite('pt000_03', 7)	# 120-126
    sprite('pt000_04', 7)	# 127-133
    sprite('pt000_05', 7)	# 134-140
    sprite('pt000_06', 7)	# 141-147
    sprite('pt000_07', 7)	# 148-154
    sprite('pt000_08', 7)	# 155-161
    sprite('pt000_09', 7)	# 162-168
    sprite('pt000_10', 7)	# 169-175
    sprite('pt000_11', 7)	# 176-182
    sprite('pt000_12', 7)	# 183-189
    sprite('pt000_13', 7)	# 190-196
    loopRest()
    gotoLabel(0)

@State
def Act2Event_ptvsmi_01():
    sprite('keep', 1)	# 1-1
    Unknown21007(11, 32)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ptvsmi_02():
    sprite('keep', 1)	# 1-1
    Unknown21007(11, 41)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ptvsmi_03():

    def upon_IMMEDIATE():

        def upon_CLEAR_OR_EXIT():
            if SLOT_38:
                if (SLOT_22 < 260000):
                    Unknown1084(1)
                    Unknown1000(-260000)
                    sendToLabel(0)
                    clearUponHandler(3)
            elif (SLOT_22 > (-260000)):
                Unknown1084(1)
                Unknown1000(-260000)
                sendToLabel(0)
                clearUponHandler(3)
    sprite('pt030_00', 7)	# 1-7
    physicsXImpulse(3000)
    sprite('pt030_01_ex', 6)	# 8-13
    label(9)
    sprite('pt030_02_ex', 6)	# 14-19
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 6)	# 20-25
    sprite('pt030_04_ex', 6)	# 26-31
    sprite('pt030_05_ex', 6)	# 32-37
    sprite('pt030_06_ex', 6)	# 38-43
    sprite('pt030_07_ex', 6)	# 44-49
    sprite('pt030_08_ex', 6)	# 50-55
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 6)	# 56-61
    sprite('pt030_10_ex', 6)	# 62-67
    sprite('pt030_11_ex', 6)	# 68-73
    sprite('pt030_12_ex', 6)	# 74-79
    sprite('pt030_13_ex', 6)	# 80-85
    gotoLabel(9)
    label(0)
    sprite('keep', 1)	# 86-86
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ptvsmi_04():
    sprite('pt041_00', 4)	# 1-4
    sprite('pt041_01', 4)	# 5-8
    label(0)
    sprite('pt040_00', 5)	# 9-13
    sprite('pt040_01', 5)	# 14-18
    sprite('pt040_02', 5)	# 19-23
    loopRest()
    gotoLabel(0)

@State
def Act2Event_ptvsmi_05():
    sprite('keep', 2)	# 1-2
    GFX_0('Act2Event_Fade', -1)
    SFX_0('022_magiccircle_c')
    Unknown3004(-4)
    Unknown36(22)
    Unknown3004(-4)
    Unknown21007(11, 39)
    Unknown35()
    label(0)
    sprite('pt040_00', 5)	# 3-7
    sprite('pt040_01', 5)	# 8-12
    sprite('pt040_02', 5)	# 13-17
    loopRest()
    gotoLabel(0)

@State
def Act2Event_ptvsaz_00():
    sprite('pt030_00', 7)	# 1-7
    physicsXImpulse(1000)
    sprite('pt030_01_ex', 8)	# 8-15
    sprite('pt030_02_ex', 8)	# 16-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)	# 24-31
    sprite('pt030_04_ex', 8)	# 32-39
    sprite('pt030_05_ex', 8)	# 40-47
    sprite('pt030_06_ex', 8)	# 48-55
    sprite('pt030_07_ex', 8)	# 56-63
    sprite('pt030_08_ex', 8)	# 64-71
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 8)	# 72-79
    sprite('pt030_10_ex', 8)	# 80-87
    sprite('pt030_11_ex', 8)	# 88-95
    sprite('pt030_12_ex', 8)	# 96-103
    sprite('pt030_13_ex', 8)	# 104-111
    sprite('pt030_02_ex', 8)	# 112-119
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)	# 120-127
    sprite('pt030_04_ex', 8)	# 128-135
    sprite('pt030_05_ex', 8)	# 136-143
    sprite('pt063_00', 3)	# 144-146
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    Unknown1043()
    sprite('pt063_01', 3)	# 147-149
    sprite('pt063_02', 3)	# 150-152
    sprite('pt063_03', 3)	# 153-155
    sprite('pt063_04', 3)	# 156-158
    sprite('pt063_05', 3)	# 159-161
    sprite('pt063_06', 2)	# 162-163
    physicsXImpulse(0)
    physicsYImpulse(3000)
    Unknown1043()
    SFX_0('209_down_normal_0')
    sprite('pt063_07', 2)	# 164-165
    sprite('pt063_08', 3)	# 166-168
    sprite('pt063_09', 3)	# 169-171
    sprite('pt063_10', 3)	# 172-174
    sprite('pt063_11', 32767)	# 175-32941
    loopRest()

@State
def Act2Event_ptvsaz_01():
    sprite('pt064_00', 4)	# 1-4
    sprite('pt064_01', 4)	# 5-8
    sprite('pt064_02', 4)	# 9-12
    sprite('pt064_03', 4)	# 13-16
    sprite('pt064_04', 4)	# 17-20
    sprite('pt064_05', 4)	# 21-24
    sprite('pt064_06', 4)	# 25-28
    sprite('pt064_07', 4)	# 29-32
    sprite('pt064_08', 4)	# 33-36
    sprite('pt064_09', 4)	# 37-40
    sprite('pt064_10', 4)	# 41-44
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ptvsaz_02():
    sprite('pt310_02', 4)	# 1-4	 **attackbox here**
    sprite('pt310_06', 4)	# 5-8
    label(0)
    sprite('pt310_04', 4)	# 9-12
    sprite('pt310_05', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Guard():
    sprite('pt041_00', 4)	# 1-4
    sprite('pt041_01', 4)	# 5-8
    sprite('pt041_02', 4)	# 9-12
    sprite('pt041_03', 4)	# 13-16
    sprite('pt041_04', 15)	# 17-31
    sprite('pt041_03', 4)	# 32-35
    sprite('pt041_02', 4)	# 36-39
    sprite('pt041_01', 4)	# 40-43
    sprite('pt041_00', 4)	# 44-47
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_GuardStop():
    sprite('pt041_00', 4)	# 1-4
    sprite('pt041_01', 4)	# 5-8
    label(0)
    sprite('pt041_02', 4)	# 9-12
    sprite('pt041_03', 4)	# 13-16
    sprite('pt041_04', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def Act2Event_GuardEnd():
    sprite('pt041_01', 4)	# 1-4
    sprite('pt041_00', 4)	# 5-8
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ptvsph_00():

    def upon_IMMEDIATE():
        Unknown2037(0)
        sendToLabelUpon(33, 1)

        def upon_32():
            GFX_0('Act3Event_FadeWhite', -1)
            SFX_3('ptse_12')
            Unknown2038(1)
    sprite('pt064_02', 3)	# 1-3
    sprite('pt064_03', 3)	# 4-6
    sprite('pt064_04', 3)	# 7-9
    sprite('pt064_05', 3)	# 10-12
    sprite('pt064_06', 3)	# 13-15
    sprite('pt064_07', 3)	# 16-18
    sprite('pt064_08', 3)	# 19-21
    sprite('pt064_09', 3)	# 22-24
    sprite('pt064_10', 3)	# 25-27
    sprite('pt000_00', 5)	# 28-32
    GFX_0('AstralAura02', -1)
    label(0)
    sprite('pt040_01', 5)	# 33-37
    Unknown23117(16777215, 30)
    if (SLOT_2 == 0):
        SFX_0('022_magiccircle_d')
    sprite('pt040_02', 5)	# 38-42
    sprite('pt040_00', 5)	# 43-47
    sprite('pt040_01', 5)	# 48-52
    sprite('pt040_02', 5)	# 53-57
    sprite('pt040_00', 5)	# 58-62
    sprite('pt040_01', 5)	# 63-67
    Unknown23117(0, 30)
    sprite('pt040_02', 5)	# 68-72
    sprite('pt040_00', 5)	# 73-77
    sprite('pt040_01', 5)	# 78-82
    sprite('pt040_02', 5)	# 83-87
    sprite('pt040_00', 5)	# 88-92
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 32767)	# 93-32859
    clearUponHandler(3)
    Unknown21012('416374334576656e745f4661646557686974650000000000000000000000000020000000')
    Unknown21012('41737472616c417572613032000000000000000000000000000000000000000020000000')
    Unknown3038(1)

@State
def Act3Event_ptvsph_01():
    sprite('pt001_00', 7)	# 1-7
    sprite('pt001_01', 5)	# 8-12
    sprite('pt001_02', 8)	# 13-20
    sprite('pt001_03', 8)	# 21-28
    sprite('pt001_04', 8)	# 29-36
    sprite('pt001_05', 8)	# 37-44
    sprite('pt001_06', 5)	# 45-49
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ptvstm_00():
    sprite('pt003_00', 3)	# 1-3
    Unknown2005()
    Unknown20000(1)
    sprite('pt003_01', 3)	# 4-6
    sprite('pt003_02', 3)	# 7-9
    loopRest()
    sprite('pt001_00', 7)	# 10-16
    sprite('pt001_01', 5)	# 17-21
    sprite('pt001_02', 8)	# 22-29
    sprite('pt001_03', 8)	# 30-37
    sprite('pt001_04', 8)	# 38-45
    sprite('pt001_05', 8)	# 46-53
    sprite('pt001_06', 5)	# 54-58
    label(0)
    sprite('pt000_00', 7)	# 59-65
    sprite('pt000_01', 7)	# 66-72
    sprite('pt000_02', 7)	# 73-79
    sprite('pt000_03', 7)	# 80-86
    sprite('pt000_04', 7)	# 87-93
    sprite('pt000_05', 7)	# 94-100
    sprite('pt000_06', 7)	# 101-107
    sprite('pt000_07', 7)	# 108-114
    sprite('pt000_08', 7)	# 115-121
    sprite('pt000_09', 7)	# 122-128
    sprite('pt000_10', 7)	# 129-135
    sprite('pt000_11', 7)	# 136-142
    sprite('pt000_12', 7)	# 143-149
    sprite('pt000_13', 7)	# 150-156
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptvstm_01_Loop():
    sprite('pt620_00', 5)	# 1-5
    Unknown20000(1)
    sprite('pt620_01', 5)	# 6-10
    sprite('pt620_02', 32767)	# 11-32777

@State
def Act3Event_ptvstm_01_LoopEnd():
    sprite('pt620_01', 5)	# 1-5
    Unknown20000(1)
    sprite('pt620_00', 5)	# 6-10
    loopRest()
    label(0)
    sprite('pt000_00', 7)	# 11-17
    sprite('pt000_01', 7)	# 18-24
    sprite('pt000_02', 7)	# 25-31
    sprite('pt000_03', 7)	# 32-38
    sprite('pt000_04', 7)	# 39-45
    sprite('pt000_05', 7)	# 46-52
    sprite('pt000_06', 7)	# 53-59
    sprite('pt000_07', 7)	# 60-66
    sprite('pt000_08', 7)	# 67-73
    sprite('pt000_09', 7)	# 74-80
    sprite('pt000_10', 7)	# 81-87
    sprite('pt000_11', 7)	# 88-94
    sprite('pt000_12', 7)	# 95-101
    sprite('pt000_13', 7)	# 102-108
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptvstm_02():
    sprite('pt003_00', 3)	# 1-3
    Unknown2005()
    Unknown20000(0)
    sprite('pt003_01', 3)	# 4-6
    sprite('pt003_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('pt000_00', 7)	# 10-16
    sprite('pt000_01', 7)	# 17-23
    sprite('pt000_02', 7)	# 24-30
    sprite('pt000_03', 7)	# 31-37
    sprite('pt000_04', 7)	# 38-44
    sprite('pt000_05', 7)	# 45-51
    sprite('pt000_06', 7)	# 52-58
    sprite('pt000_07', 7)	# 59-65
    sprite('pt000_08', 7)	# 66-72
    sprite('pt000_09', 7)	# 73-79
    sprite('pt000_10', 7)	# 80-86
    sprite('pt000_11', 7)	# 87-93
    sprite('pt000_12', 7)	# 94-100
    sprite('pt000_13', 7)	# 101-107
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptvstm_03():
    label(0)
    sprite('pt010_02', 6)	# 1-6
    sprite('pt010_03', 6)	# 7-12
    sprite('pt010_04', 6)	# 13-18
    sprite('pt010_05', 6)	# 19-24
    sprite('pt010_06', 6)	# 25-30
    sprite('pt010_07', 6)	# 31-36
    sprite('pt010_08', 6)	# 37-42
    sprite('pt010_09', 6)	# 43-48
    sprite('pt010_10', 6)	# 49-54
    sprite('pt010_11', 6)	# 55-60
    sprite('pt010_12', 6)	# 61-66
    sprite('pt010_13', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptvstm_04():
    sprite('pt010_01', 6)	# 1-6
    sprite('pt010_00', 6)	# 7-12
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ptvsrl_00():

    def upon_IMMEDIATE():
        Unknown2037(1)

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 36):
                Unknown3004(5)
            else:
                Unknown3004(-5)
                if SLOT_2:
                    Unknown2037(0)
                    SFX_0('022_magiccircle_d')
    label(0)
    sprite('pt000_00', 7)	# 1-7
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptvsrl_01():
    sprite('pt620_00', 5)	# 1-5
    sprite('pt620_01', 5)	# 6-10
    sprite('pt620_02', 32767)	# 11-32777

@State
def Act3Event_ptvsrl_02():
    sprite('pt620_01', 5)	# 1-5
    sprite('pt620_00', 5)	# 6-10
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ptvsrl_03():
    sprite('pt041_00', 3)	# 1-3
    sprite('pt041_01', 3)	# 4-6
    label(0)
    sprite('pt040_00', 5)	# 7-11
    sprite('pt040_01', 5)	# 12-16
    sprite('pt040_02', 5)	# 17-21
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptvsrl_04():
    sprite('pt064_00', 5)	# 1-5
    sprite('pt064_01', 5)	# 6-10
    sprite('pt064_02', 5)	# 11-15
    sprite('pt064_03', 32767)	# 16-32782

@State
def Act3Event_ptvsrl_05():

    def upon_IMMEDIATE():
        Unknown2037(1)

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 36):
                Unknown3004(5)
                if (SLOT_51 >= 84):
                    SLOT_51 = 0
                    Unknown2037(1)
            else:
                Unknown3004(-5)
                if SLOT_2:
                    Unknown2037(0)
                    SFX_0('022_magiccircle_d')
    sprite('pt064_03', 32767)	# 1-32767

@State
def Act3Event_ptvsrl_06():

    def upon_IMMEDIATE():
        loopRelated(17, 240)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('pt000_00', 7)	# 1-7
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    loopRest()
    gotoLabel(0)
    label(1)
    loopRest()
    enterState('EventChouhatsu')

@State
def Act3Event_ptvsjn_00():

    def upon_IMMEDIATE():
        Unknown2037(1)

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 36):
                Unknown3004(5)
                if (SLOT_51 >= 84):
                    SLOT_51 = 0
                    Unknown2037(1)
            else:
                Unknown3004(-5)
                if SLOT_2:
                    Unknown2037(0)
                    SFX_0('022_magiccircle_d')
    sprite('pt070_13', 4)	# 1-4
    sprite('pt070_12', 4)	# 5-8
    sprite('pt070_11', 4)	# 9-12
    sprite('pt070_10', 32767)	# 13-32779
    loopRest()

@State
def Act3Event_ptvsjn_01():
    sprite('pt070_11', 4)	# 1-4
    Unknown3004(255)
    sprite('pt070_12', 4)	# 5-8
    sprite('pt070_13', 4)	# 9-12
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ptvsjn_02():
    sprite('pt620_00', 6)	# 1-6
    sprite('pt620_01', 6)	# 7-12
    sprite('pt620_02', 6)	# 13-18
    sprite('pt620_03', 6)	# 19-24
    SFX_0('019_cloth_b')
    sprite('pt620_04', 6)	# 25-30
    sprite('pt620_05', 6)	# 31-36
    sprite('pt620_06', 6)	# 37-42
    sprite('pt620_07', 6)	# 43-48
    label(0)
    sprite('pt620_08', 6)	# 49-54
    SFX_3('ptse_05')
    sprite('pt620_09', 6)	# 55-60
    sprite('pt620_10', 6)	# 61-66
    sprite('pt620_09', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptvsjn_03():
    sprite('pt620_07', 4)	# 1-4
    sprite('pt620_06', 4)	# 5-8
    sprite('pt620_05', 4)	# 9-12
    sprite('pt620_03', 4)	# 13-16
    sprite('pt620_02', 4)	# 17-20
    sprite('pt620_01', 4)	# 21-24
    sprite('pt620_00', 4)	# 25-28
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ptvsjn_04():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        Unknown1000(-60000)
    label(0)
    sprite('pt000_00', 7)	# 1-7
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt070_00', 2)	# 99-100
    Unknown4045('65665f67697264627265616b000000000000000000000000000000000000000067000000')
    SFX_0('104_guard_grap_1')
    SFX_0('106_guard_crush')
    ScreenShake(3000, 18000)
    Unknown1045(-20000)
    sprite('pt070_01', 2)	# 101-102
    Unknown2037(6)
    label(2)
    sprite('pt070_02', 5)	# 103-107
    sprite('pt070_03', 5)	# 108-112
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(2)
    sprite('pt070_04', 4)	# 113-116
    sprite('pt070_05', 4)	# 117-120
    sprite('pt070_06', 4)	# 121-124
    sprite('pt070_07', 6)	# 125-130
    sprite('pt070_08', 6)	# 131-136
    sprite('pt070_09', 5)	# 137-141
    sprite('pt063_11', 32767)	# 142-32908
    Unknown8003(100, 1, 1)
    teleportRelativeX(80000)

@State
def Act3Event_ptvsjn_05():
    sprite('pt064_00', 7)	# 1-7
    sprite('pt064_01', 7)	# 8-14
    sprite('pt064_02', 32767)	# 15-32781

@State
def Act3Event_ptvsjn_06():
    sprite('pt064_03', 4)	# 1-4
    sprite('pt064_04', 4)	# 5-8
    sprite('pt064_05', 4)	# 9-12
    sprite('pt064_06', 4)	# 13-16
    sprite('pt064_07', 4)	# 17-20
    sprite('pt064_08', 4)	# 21-24
    sprite('pt064_09', 4)	# 25-28
    sprite('pt064_10', 4)	# 29-32
    sprite('pt000_00', 1)	# 33-33
    enterState('Act3Event_ptvsph_01')

@State
def Act3Event_ptvsjn_07():
    sprite('pt430_00', 3)	# 1-3
    sprite('pt430_01', 3)	# 4-6
    sprite('pt430_02', 3)	# 7-9
    SFX_0('008_swing_pole_2')
    sprite('pt430_03', 3)	# 10-12
    sprite('pt430_04', 3)	# 13-15
    sprite('pt430_05', 3)	# 16-18
    sprite('pt430_06', 3)	# 19-21
    sprite('pt430_07', 3)	# 22-24
    GFX_0('pt430_mahojin', 0)
    GFX_0('pt203_mahojinsub', 0)
    GFX_0('pt430_circle1', 1)
    GFX_0('pt430_circle2', 1)
    sprite('pt430_08', 3)	# 25-27
    sprite('pt430_09', 3)	# 28-30
    sprite('pt430_10', 3)	# 31-33
    sprite('pt430_11', 3)	# 34-36
    GFX_0('ptef_430power', 0)
    SFX_0('022_magiccircle_b')
    sprite('pt430_12', 3)	# 37-39
    sprite('pt203_02', 32767)	# 40-32806
    GFX_0('pt430_mahojinsub', 0)
    GFX_0('pt430_aura1', 0)
    GFX_0('pt430_aura2', 0)
    GFX_0('pt430_aura3', 0)

@State
def Act3Event_mavspt_00():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown20000(1)

        def upon_32():
            Unknown20000(0)
    label(0)
    sprite('pt000_00', 7)	# 1-7
    sprite('pt000_01', 7)	# 8-14
    sprite('pt000_02', 7)	# 15-21
    sprite('pt000_03', 7)	# 22-28
    sprite('pt000_04', 7)	# 29-35
    sprite('pt000_05', 7)	# 36-42
    sprite('pt000_06', 7)	# 43-49
    sprite('pt000_07', 7)	# 50-56
    sprite('pt000_08', 7)	# 57-63
    sprite('pt000_09', 7)	# 64-70
    sprite('pt000_10', 7)	# 71-77
    sprite('pt000_11', 7)	# 78-84
    sprite('pt000_12', 7)	# 85-91
    sprite('pt000_13', 7)	# 92-98
    loopRest()
    gotoLabel(0)

@State
def Act3Event_mavspt_01():
    sprite('pt003_00', 4)	# 1-4
    Unknown2005()
    Unknown20000(0)
    sprite('pt003_01', 4)	# 5-8
    sprite('pt003_02', 4)	# 9-12
    loopRest()
    label(0)
    sprite('pt000_00', 7)	# 13-19
    sprite('pt000_01', 7)	# 20-26
    sprite('pt000_02', 7)	# 27-33
    sprite('pt000_03', 7)	# 34-40
    sprite('pt000_04', 7)	# 41-47
    sprite('pt000_05', 7)	# 48-54
    sprite('pt000_06', 7)	# 55-61
    sprite('pt000_07', 7)	# 62-68
    sprite('pt000_08', 7)	# 69-75
    sprite('pt000_09', 7)	# 76-82
    sprite('pt000_10', 7)	# 83-89
    sprite('pt000_11', 7)	# 90-96
    sprite('pt000_12', 7)	# 97-103
    sprite('pt000_13', 7)	# 104-110
    loopRest()
    gotoLabel(0)

@State
def Act3Event_mavspt_02():

    def upon_IMMEDIATE():
        Unknown1000(-200000)
    sprite('pt070_00', 3)	# 1-3
    sprite('pt070_01', 3)	# 4-6
    label(0)
    sprite('pt070_02', 4)	# 7-10
    sprite('pt070_03', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def Act3Event_mavspt_03():
    sprite('pt070_10', 5)	# 1-5
    sprite('pt070_11', 5)	# 6-10
    sprite('pt070_12', 5)	# 11-15
    sprite('pt070_13', 5)	# 16-20
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mavspt_04():
    sprite('pt620_00', 6)	# 1-6
    sprite('pt620_01', 6)	# 7-12
    sprite('pt620_02', 6)	# 13-18
    sprite('pt620_03', 6)	# 19-24
    SFX_0('019_cloth_b')
    sprite('pt620_04', 6)	# 25-30
    sprite('pt620_05', 32767)	# 31-32797
    loopRest()

@State
def Act3Event_mavspt_05():
    sprite('pt620_06', 6)	# 1-6
    sprite('pt620_07', 6)	# 7-12
    label(0)
    sprite('pt620_08', 6)	# 13-18
    sprite('pt620_09', 6)	# 19-24
    sprite('pt620_10', 6)	# 25-30
    sprite('pt620_09', 6)	# 31-36
    loopRest()
    gotoLabel(0)

@State
def Act3Event_mavspt_06():
    sprite('keep', 2)	# 1-2
    sprite('pt620_11', 6)	# 3-8
    sprite('pt620_12', 32767)	# 9-32775
    loopRest()

@State
def Act3Event_mavspt_07():
    sprite('pt620_11', 6)	# 1-6
    label(0)
    sprite('pt620_08', 6)	# 7-12
    sprite('pt620_09', 6)	# 13-18
    sprite('pt620_10', 6)	# 19-24
    sprite('pt620_09', 6)	# 25-30
    loopRest()
    gotoLabel(0)
    loopRest()

@State
def Act3Event_mavspt_08():
    sprite('pt064_03', 4)	# 1-4
    sprite('pt064_04', 4)	# 5-8
    sprite('pt064_05', 4)	# 9-12
    sprite('pt064_06', 4)	# 13-16
    sprite('pt064_07', 4)	# 17-20
    sprite('pt064_08', 4)	# 21-24
    sprite('pt064_09', 4)	# 25-28
    sprite('pt064_10', 4)	# 29-32
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mavspt_09():
    sprite('pt033_00', 3)	# 1-3
    sprite('pt033_01', 3)	# 4-6
    physicsXImpulse(-10000)
    physicsYImpulse(5000)
    setGravity(1550)
    sendToLabelUpon(2, 1)
    sprite('pt033_02', 3)	# 7-9
    sprite('pt033_03', 3)	# 10-12
    loopRest()
    label(0)
    sprite('pt033_02', 3)	# 13-15
    sprite('pt033_03', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt033_04', 4)	# 19-22
    Unknown1084(1)
    sprite('pt033_05', 4)	# 23-26
    Unknown8000(100, 1, 1)
    sprite('pt033_06', 4)	# 27-30
    loopRest()
    enterState('CmnActStand')