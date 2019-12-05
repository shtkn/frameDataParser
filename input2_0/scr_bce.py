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
    Unknown12019('62636500000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown15013(2000)
    Unknown14015(100000, 550000, -200000, 300000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown14015(0, 300000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk4ALoop', 0x1)
    Unknown14027('NmlAtk4A')
    Move_Input_(0x5e)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown14015(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(100000, 500000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(300000, 650000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(350000, 900000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown14015(0, 350000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown15021(1500)
    Unknown14015(100000, 450000, 0, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14015(0, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown15009()
    Unknown14015(0, 450000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2BB', 0x16)
    Unknown14005(1)
    Unknown15009()
    Unknown14015(0, 400000, -200000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 300000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15021(1)
    Unknown15009()
    Unknown14015(0, 350000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 450000, -200000, 400000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(0, 300000, -300000, 300000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(0, 350000, -500000, 80000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown14015(100000, 450000, -600000, 80000, 500, 1)
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
    Move_Register('ShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(1)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1500)
    Unknown15011(10000)
    Unknown14015(650000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1500)
    Unknown15011(10000)
    Unknown14015(650000, 1200000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('ShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(1)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15011(10000)
    Unknown14015(650000, 1400000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(450000, 900000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AssaultFP', INPUT_SPECIALMOVE)
    Unknown14024('CheckMinervaFullPower')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15027(250)
    Unknown14015(900000, 2000000, -200000, 800000, 10, 500)
    Move_EndRegister()
    Move_Register('MidAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(0, 450000, -200000, 300000, 500, 10)
    Move_EndRegister()
    Move_Register('MidAssaultFP', INPUT_SPECIALMOVE)
    Unknown14024('CheckMinervaFullPower')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(0, 450000, -200000, 300000, 500, 10)
    Move_EndRegister()
    Move_Register('SpecialHeal', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(1200000, 1500000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('SpecialHealFP', INPUT_SPECIALMOVE)
    Unknown14024('CheckMinervaFullPower')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(1200000, 1500000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 600000, 250, 5)
    Move_EndRegister()
    Move_Register('InvincibleAttackFP', 0x64)
    Unknown14024('CheckMinervaFullPower')
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 600000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(2000)
    Unknown14015(650000, 1400000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateShotSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(2000)
    Unknown14015(650000, 1400000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(4000)
    Unknown14015(0, 450000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(4000)
    Unknown14015(0, 450000, -200000, 200000, 500, 0)
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
    Unknown15024('NmlAtk5AA', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5AAA', 'Assault', 10000000)
    Unknown15024('NmlAtk5AAA', 'AssaultFP', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk2C', 'Assault', 10000000)
    Unknown15024('NmlAtk2C', 'AssaultFP', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateAssault', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateAssaultSP', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BBB', 'Assault', 10000000)
    Unknown15024('NmlAtk5BBB', 'AssaultFP', 10000000)
    Unknown15024('NmlAtk5BBB', 'MidAssault', 10000000)
    Unknown15024('NmlAtk5BBB', 'MidAssaultFP', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AssaultFP', 10000000)
    Unknown12018(0, 'ce062_01')
    Unknown12018(1, 'ce062_03')
    Unknown12018(2, 'ce062_04')
    Unknown12018(3, 'ce062_05')
    Unknown12018(4, 'ce062_05')
    Unknown12018(5, 'ce062_06')
    Unknown12018(6, 'ce062_07')
    Unknown12018(7, 'ce041_02')
    Unknown12018(8, 'ce040_02')
    Unknown12018(9, 'ce045_02')
    Unknown12018(10, 'ce060_00')
    Unknown12018(11, 'ce060_01')
    Unknown12018(12, 'ce060_03')
    Unknown12018(13, 'ce060_05')
    Unknown12018(14, 'ce060_07')
    Unknown12018(15, 'ce060_14')
    Unknown12018(16, 'ce050_00')
    Unknown12018(17, 'ce052_00')
    Unknown12018(18, 'ce054_00')
    Unknown12018(19, 'ce000_00')
    Unknown12018(20, 'ce000_00')
    Unknown12018(25, 'ce063_00')
    Unknown12018(26, 'ce063_01')
    Unknown12018(27, 'ce063_02')
    Unknown12018(28, 'ce063_04')
    Unknown12018(29, 'ce063_10')
    Unknown12018(24, 'ce073_01')
    Unknown7010(0, 'bce000')
    Unknown7010(1, 'bce001')
    Unknown7010(2, 'bce002')
    Unknown7010(3, 'bce003')
    Unknown7010(4, 'bce004')
    Unknown7010(5, 'bce005')
    Unknown7010(6, 'bce006')
    Unknown7010(7, 'bce007')
    Unknown7010(8, 'bce008')
    Unknown7010(9, 'bce009')
    Unknown7010(10, 'bce010')
    Unknown7010(15, 'bce011')
    Unknown7010(16, 'bce012')
    Unknown7010(17, 'bce013')
    Unknown7010(18, 'bce014')
    Unknown7010(19, 'bce015')
    Unknown7010(20, 'bce016')
    Unknown7010(21, 'bce017')
    Unknown7010(22, 'bce018')
    Unknown7010(23, 'bce019')
    Unknown7010(24, 'bce020')
    Unknown7010(25, 'bce021')
    Unknown7010(28, 'bce022')
    Unknown7010(29, 'bce023')
    Unknown7010(30, 'bce024')
    Unknown7010(31, 'bce025')
    Unknown7010(32, 'bce026')
    Unknown7010(33, 'bce027')
    Unknown7010(34, 'bce028')
    Unknown7010(35, 'bce029')
    Unknown7010(36, 'bce030')
    Unknown7010(37, 'bce031')
    Unknown7010(39, 'bce032')
    Unknown7010(42, 'bce033')
    Unknown7010(43, 'bce034')
    Unknown7010(44, 'bce035')
    Unknown7010(45, 'bce036')
    Unknown7010(46, 'bce037')
    Unknown7010(47, 'bce038')
    Unknown7010(48, 'bce039')
    Unknown7010(49, 'bce040')
    Unknown7010(50, 'bce041')
    Unknown7010(52, 'bce042')
    Unknown7010(53, 'bce043')
    Unknown7010(54, 'bce100_0')
    Unknown7010(55, 'bce100_1')
    Unknown7010(56, 'bce100_2')
    Unknown7010(63, 'bce101_0')
    Unknown7010(64, 'bce101_1')
    Unknown7010(65, 'bce101_2')
    Unknown7010(57, 'bce102_0')
    Unknown7010(58, 'bce102_1')
    Unknown7010(59, 'bce102_2')
    Unknown7010(66, 'bce103_0')
    Unknown7010(67, 'bce103_1')
    Unknown7010(68, 'bce103_2')
    Unknown7010(60, 'bce104_0')
    Unknown7010(61, 'bce104_1')
    Unknown7010(62, 'bce104_2')
    Unknown7010(69, 'bce105_0')
    Unknown7010(70, 'bce105_1')
    Unknown7010(71, 'bce105_2')
    Unknown7010(72, 'bce150')
    Unknown7010(73, 'bce151')
    Unknown7010(74, 'bce152')
    Unknown7010(85, 'bce153')
    Unknown7010(87, 'bce154')
    Unknown7010(88, 'bce155')
    Unknown7010(96, 'bce161_0')
    Unknown7010(97, 'bce161_1')
    Unknown7010(92, 'bce162_0')
    Unknown7010(93, 'bce162_1')
    Unknown7010(98, 'bce163_0')
    Unknown7010(99, 'bce163_1')
    Unknown7010(100, 'bce164_0')
    Unknown7010(101, 'bce164_1')
    Unknown7010(105, 'bce165_0')
    Unknown7010(106, 'bce165_1')
    Unknown7010(102, 'bce166_0')
    Unknown7010(103, 'bce166_1')
    Unknown7010(90, 'bce167_0')
    Unknown7010(91, 'bce167_1')
    Unknown7010(107, 'bce168_0')
    Unknown7010(108, 'bce168_1')
    Unknown7010(110, 'bce169_0')
    Unknown7010(111, 'bce169_1')
    Unknown7010(112, 'bce159_0')
    Unknown7010(113, 'bce159_1')
    Unknown7010(94, 'bce400_0')
    Unknown7010(95, 'bce400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745350000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746541737361756c745350000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    GFX_0('MinervaCreate', -1)
    Unknown38(11, 1)

@Subroutine
def OnFrameStep():
    if SLOT_21:
        if SLOT_30:
            if Unknown64(3):
                if (SLOT_61 >= 2):
                    SLOT_4 = 1

@Subroutine
def OnDamage():
    SLOT_6 = 0

@Subroutine
def OnGuard():
    SLOT_6 = 0

@Subroutine
def OnActionBeginPre():
    SLOT_4 = 0

@Subroutine
def OnActionBegin():
    SLOT_60 = 1
    if Unknown23148('CmnActTagBattleWait'):
        SLOT_60 = 0
    if SLOT_161:
        SLOT_60 = 0
    if SLOT_IsPlayer2:
        Unknown58('TRI_BCEPowerUp', 2, 67)
        if (SLOT_67 == 1):
            SLOT_60 = 1
        if (SLOT_67 == 2):
            SLOT_60 = 0
        if SLOT_170:
            SLOT_60 = 0
    if SLOT_30:
        SLOT_60 = 0
    if (not SLOT_21):
        SLOT_60 = 0
    if SLOT_60:
        if (not Unknown46(5)):
            GFX_0('RecoveryCapa', 103)
            Unknown38(5, 1)
    else:
        callSubroutine('RCEffCheck')
    Unknown23029(11, 999, 0)

@Subroutine
def RCEffCheck():
    if Unknown46(5):
        Unknown26('RecoveryCapa')

@Subroutine
def CheckShotAvailable():
    SLOT_47 = 1
    if SLOT_5:
        SLOT_47 = 0

@Subroutine
def CheckMinervaFullPower():
    SLOT_47 = 1
    if SLOT_161:
        SLOT_47 = 0
    if SLOT_IsPlayer2:
        Unknown58('TRI_BCEPowerUp', 2, 67)
        if (SLOT_67 == 1):
            SLOT_47 = 1
        if (SLOT_67 == 2):
            SLOT_47 = 0

@Subroutine
def MinervaNoneCall():

    def upon_48():
        SLOT_61 = 0

@Subroutine
def MinervaCall():
    SLOT_4 = 1
    loopRelated(17, 2)

    def upon_48():
        SLOT_61 = 2

@Subroutine
def MinervaCallAttack():
    SLOT_4 = 1
    loopRelated(17, 2)

    def upon_48():
        SLOT_61 = 3

@Subroutine
def MinervaNoneCallAttack():

    def upon_48():
        SLOT_61 = 1

@Subroutine
def MinervaCallCrushAssault():
    SLOT_4 = 1

    def upon_48():
        SLOT_61 = 2

@State
def CmnActStand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        Unknown2004(1, 0)
        Unknown23029(11, 100, 0)

        def upon_STATE_END():
            if SLOT_62:
                Unknown23029(11, 100, 0)
                SLOT_62 = 0
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('ce001_00', 6)
    SLOT_62 = 1
    Unknown23029(11, 112, 0)
    SLOT_88 = 960
    SFX_1('bce000')
    sprite('ce001_01', 6)
    sprite('ce001_02', 6)
    sprite('ce001_03', 6)
    sprite('ce001_04', 6)
    sprite('ce001_05', 6)
    label(9)
    sprite('ce001_06', 8)
    sprite('ce001_06ex00', 8)
    sprite('ce001_06ex01', 29)
    sprite('ce001_06', 8)
    sprite('ce001_06ex02', 8)
    sprite('ce001_06ex03', 29)
    gotoLabel(9)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('ce603_01', 6)
    SLOT_88 = 960
    sprite('ce603_00', 90)
    sprite('ce603_01', 6)
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        Unknown23029(11, 101, 0)
    sprite('ce003_00', 3)
    sprite('ce003_01', 3)
    sprite('ce003_00ex', 3)

@State
def CmnActStand2Crouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_00', 4)
    sprite('ce010_01', 4)

@State
def CmnActCrouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    label(0)
    sprite('ce010_02', 6)
    sprite('ce010_03', 6)
    sprite('ce010_04', 6)
    sprite('ce010_05', 6)
    sprite('ce010_06', 6)
    sprite('ce010_07', 6)
    sprite('ce010_08', 6)
    sprite('ce010_09', 6)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        Unknown23029(11, 101, 0)
    sprite('ce013_00', 3)
    sprite('ce013_01', 3)
    sprite('ce013_00ex', 3)

@State
def CmnActCrouch2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_01', 4)
    sprite('ce010_00', 4)

@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        if SLOT_37:
            if SLOT_93:
                if SLOT_16:
                    Unknown1045(15000)
    sprite('ce023_00', 2)
    sprite('ce023_01', 2)

@State
def CmnActJumpUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce020_00', 4)
    sprite('ce020_01', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce020_02', 3)
    sprite('ce020_03', 3)
    sprite('ce020_04', 3)

@State
def CmnActJumpDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce020_05', 3)
    sprite('ce020_06', 3)
    label(0)
    sprite('ce020_07', 4)
    sprite('ce020_08', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_01', 3)
    sprite('ce024_02', 4)
    sprite('ce024_03', 5)
    sprite('ce024_04', 3)
    sprite('ce024_05', 3)

@State
def CmnActLandingStiffLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_00', 2)
    sprite('ce024_01', 2)
    sprite('ce024_02', 32767)

@State
def CmnActLandingStiffEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_03', 3)
    sprite('ce024_04', 3)
    sprite('ce024_05', 3)

@State
def CmnActFWalk():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')

        def upon_17():
            Unknown23029(11, 102, 0)

        def upon_STATE_END():
            Unknown23029(11, 100, 0)
    sprite('ce030_00', 7)
    label(0)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')

        def upon_17():
            Unknown23029(11, 103, 0)

        def upon_STATE_END():
            Unknown23029(11, 100, 0)
    sprite('ce030_00ex', 7)
    label(0)
    sprite('ce030_01ex', 7)
    sprite('ce030_02ex', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03ex', 7)
    sprite('ce030_04ex', 7)
    sprite('ce030_05ex', 7)
    sprite('ce030_06ex', 7)
    sprite('ce030_07ex', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08ex', 7)
    sprite('ce030_09ex', 7)
    sprite('ce030_10ex', 7)
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')

        def upon_IMMEDIATE():

            def upon_STATE_END():
                if (SLOT_18 <= 5):
                    Unknown1019(25)
    sprite('ce032_00', 3)
    label(0)
    sprite('ce032_01', 4)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    sprite('ce032_02', 4)
    SFX_3('cese_04')
    sprite('ce032_03', 4)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')

        def upon_IMMEDIATE():
            Unknown13019(1)

            def upon_CLEAR_OR_EXIT():
                if (SLOT_18 == 4):
                    Unknown13005(1)
                    Unknown13001(1)
    sprite('ce032_04', 3)
    sprite('ce032_05', 3)
    sprite('ce032_06', 3)
    sprite('ce032_07', 3)

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        callSubroutine('MinervaNoneCall')
        Unknown23001(100, 0)
        Unknown23076()
        setInvincibleFor(7)
        Unknown1084(1)
    sprite('ce033_00', 2)
    SFX_3('cese_16')
    sprite('ce033_01', 2)
    physicsXImpulse(-20000)
    sprite('ce033_02', 2)
    teleportRelativeX(-20000)
    Unknown1019(150)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 1)
    Unknown1019(150)
    sprite('ce033_03', 3)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_04', 4)
    Unknown1019(15)
    Unknown8000(100, 1, 1)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_05', 4)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_06', 4)
    Unknown1019(15)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_07', 3)
    physicsXImpulse(0)

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce035_00', 3)
    label(0)
    sprite('ce035_01', 3)
    GFX_0('ceAirDashEff', 0)
    GFX_0('ceAirDashEff', 1)
    GFX_0('ceAirDashEff', 2)
    sprite('ce035_02', 3)
    sprite('ce035_03', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce036_00', 3)
    label(0)
    sprite('ce036_01', 3)
    GFX_0('ceAirBDashEff', 0)
    GFX_0('ceAirBDashEff', 1)
    GFX_0('ceAirDashEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    sprite('ce036_02', 3)
    sprite('ce036_03', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_00', 1)
    sprite('ce050_01', 1)
    sprite('ce050_00', 2)

@State
def CmnActHitStandLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_01', 1)
    sprite('ce050_02', 1)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)

@State
def CmnActHitStandLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_02', 1)
    sprite('ce050_03', 1)
    sprite('ce050_02', 2)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)

@State
def CmnActHitStandLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_03', 1)
    sprite('ce050_04', 1)
    sprite('ce050_03', 2)
    sprite('ce050_02', 2)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)

@State
def CmnActHitStandLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_04', 1)
    sprite('ce050_04', 1)
    sprite('ce050_04', 2)
    sprite('ce050_03', 2)
    sprite('ce050_02', 2)
    sprite('ce050_01', 2)
    sprite('ce050_00', 2)

@State
def CmnActHitStandLowLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_00', 1)
    sprite('ce052_01', 1)
    sprite('ce052_00', 2)

@State
def CmnActHitStandLowLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_01', 1)
    sprite('ce052_02', 1)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)

@State
def CmnActHitStandLowLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_02', 1)
    sprite('ce052_03', 1)
    sprite('ce052_02', 2)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)

@State
def CmnActHitStandLowLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_03', 1)
    sprite('ce052_04', 1)
    sprite('ce052_03', 2)
    sprite('ce052_02', 2)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)

@State
def CmnActHitStandLowLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_04', 1)
    sprite('ce052_04', 1)
    sprite('ce052_04', 2)
    sprite('ce052_03', 2)
    sprite('ce052_02', 2)
    sprite('ce052_01', 2)
    sprite('ce052_00', 2)

@State
def CmnActHitCrouchLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_00', 1)
    sprite('ce054_01', 1)
    sprite('ce054_00', 2)

@State
def CmnActHitCrouchLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_01', 1)
    sprite('ce054_02', 1)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)

@State
def CmnActHitCrouchLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_02', 1)
    sprite('ce054_03', 1)
    sprite('ce054_02', 2)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)

@State
def CmnActHitCrouchLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_03', 1)
    sprite('ce054_04', 1)
    sprite('ce054_03', 2)
    sprite('ce054_02', 2)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)

@State
def CmnActHitCrouchLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_04', 1)
    sprite('ce054_04', 1)
    sprite('ce054_04', 2)
    sprite('ce054_03', 2)
    sprite('ce054_02', 2)
    sprite('ce054_01', 2)
    sprite('ce054_00', 2)

@State
def CmnActBDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_00', 4)
    label(0)
    sprite('ce060_01', 4)
    sprite('ce060_02', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_03', 3)
    sprite('ce062_04', 3)

@State
def CmnActBDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_05', 3)
    sprite('ce062_06', 3)
    label(0)
    sprite('ce062_07', 3)
    sprite('ce062_08', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_04', 3)
    sprite('ce063_05', 3)

@State
def CmnActBDownBound():
    sprite('null', 60)

@State
def CmnActBDownLoop():
    sprite('null', 60)

@State
def CmnActBDown2Stand():
    sprite('null', 60)

@State
def CmnActFDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_00', 3)

@State
def CmnActFDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_01', 3)

@State
def CmnActFDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce063_02', 3)
    sprite('ce063_03', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_04', 3)
    sprite('ce063_05', 3)

@State
def CmnActFDownBound():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_06', 2)
    sprite('ce063_07', 2)
    sprite('ce063_08', 3)
    sprite('ce063_09', 3)
    sprite('ce063_10', 3)

@State
def CmnActFDownLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_11', 3)

@State
def CmnActFDown2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce064_00', 2)
    sprite('ce064_01', 2)
    sprite('ce064_02', 2)
    sprite('ce064_03', 2)
    sprite('ce064_04', 2)
    sprite('ce064_05', 2)
    sprite('ce064_06', 2)
    sprite('ce064_07', 2)
    sprite('ce064_08', 3)
    sprite('ce064_09', 3)

@State
def CmnActVDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_00', 3)
    label(0)
    sprite('ce062_01', 3)
    sprite('ce062_02', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_03', 3)
    sprite('ce062_04', 3)

@State
def CmnActVDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_05', 3)
    sprite('ce062_06', 3)
    label(0)
    sprite('ce062_07', 3)
    sprite('ce062_08', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_09', 2)
    sprite('ce062_10', 2)

@State
def CmnActBlowoff():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce072_00', 5)
    sprite('ce072_01', 3)
    sprite('ce072_02', 3)
    label(0)
    sprite('ce072_01', 3)
    sprite('ce072_02', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce074_00', 3)
    sprite('ce074_01', 3)
    sprite('ce074_02', 3)
    sprite('ce074_03', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('null', 60)

@State
def CmnActFreeze():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce071_04', 1)

@State
def CmnActWallBound():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce073_00', 3)
    sprite('ce073_01', 3)

@State
def CmnActWallBoundDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce073_02', 3)
    label(0)
    sprite('ce073_03', 3)
    sprite('ce073_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_00', 3)
    sprite('ce070_01', 3)
    label(0)
    sprite('ce070_02', 3)
    sprite('ce070_03', 3)
    gotoLabel(0)

@State
def CmnActStaggerDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_04', 4)
    sprite('ce070_05', 4)
    sprite('ce070_06', 4)
    sprite('ce070_07', 4)
    sprite('ce070_08', 4)
    sprite('ce070_09', 4)

@State
def CmnActUkemiStagger():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_10', 1)
    sprite('ce070_11', 2)
    sprite('ce070_12', 3)
    sprite('ce070_13', 3)

@State
def CmnActUkemiAirF():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)
    sprite('ce113_01', 3)
    sprite('ce113_02', 3)

@State
def CmnActUkemiAirB():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)
    sprite('ce113_01', 3)
    sprite('ce113_02', 3)

@State
def CmnActUkemiAirN():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)
    sprite('ce113_01', 3)
    sprite('ce113_02', 3)

@State
def CmnActUkemiLandF():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce110_00', 2)
    sprite('ce110_01', 2)
    sprite('ce110_02', 2)
    sprite('ce110_03', 2)
    sprite('ce110_04', 2)
    sprite('ce110_05', 2)
    sprite('ce110_06', 2)
    sprite('ce110_07', 200)
    sprite('ce110_08', 3)
    sprite('ce110_09', 3)

@State
def CmnActUkemiLandB():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce111_00', 3)
    sprite('ce111_01', 3)
    sprite('ce111_02', 3)
    sprite('ce111_03', 3)
    sprite('ce111_04', 3)
    sprite('ce111_06', 3)
    sprite('ce111_07', 200)
    sprite('ce111_08', 3)
    sprite('ce111_09', 3)

@State
def CmnActUkemiLandN():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce112_00', 2)
    sprite('ce112_01', 2)
    sprite('ce112_02', 2)
    sprite('ce112_03', 2)
    sprite('ce112_04', 2)
    sprite('ce112_05', 2)
    sprite('ce112_06', 2)
    sprite('ce112_07', 2)
    sprite('ce112_08', 2)

@State
def CmnActUkemiLandNLanding():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_00', 3)
    sprite('ce024_01', 3)
    sprite('ce024_02', 3)
    sprite('ce024_03', 3)
    sprite('ce024_04', 3)

@State
def CmnActMidGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_00', 3)
    sprite('ce040_01', 3)

@State
def CmnActMidGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce040_02', 3)
    sprite('ce040_03', 3)
    sprite('ce040_04', 3)
    gotoLabel(0)

@State
def CmnActMidGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_01', 3)
    sprite('ce040_00', 3)

@State
def CmnActMidHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_05', 3)
    label(0)
    sprite('ce040_02', 3)
    sprite('ce040_03', 3)
    sprite('ce040_04', 3)
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_01', 3)
    sprite('ce040_00', 3)

@State
def CmnActHighGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_00', 3)
    sprite('ce041_01', 3)

@State
def CmnActHighGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce041_02', 3)
    sprite('ce041_03', 3)
    sprite('ce041_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_01', 3)
    sprite('ce041_00', 3)

@State
def CmnActHighHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_05', 3)
    label(0)
    sprite('ce041_02', 3)
    sprite('ce041_03', 3)
    sprite('ce041_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_01', 3)
    sprite('ce041_00', 3)

@State
def CmnActCrouchGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_00', 3)
    sprite('ce043_01', 3)

@State
def CmnActCrouchGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce043_02', 3)
    sprite('ce043_03', 3)
    sprite('ce043_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_01', 3)
    sprite('ce043_00', 3)

@State
def CmnActCrouchHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_05', 3)
    label(0)
    sprite('ce043_02', 3)
    sprite('ce043_03', 3)
    sprite('ce043_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_01', 3)
    sprite('ce043_00', 3)

@State
def CmnActAirGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_00', 3)
    sprite('ce045_01', 3)

@State
def CmnActAirGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce045_02', 3)
    sprite('ce045_03', 3)
    sprite('ce045_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_01', 3)
    sprite('ce045_00', 3)

@State
def CmnActAirHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_05', 3)
    label(0)
    sprite('ce045_02', 3)
    sprite('ce045_03', 3)
    sprite('ce045_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_01', 3)
    sprite('ce045_00', 3)

@State
def CmnActGuardBreakStand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce090_00', 2)
    sprite('ce090_01', 2)
    sprite('ce090_02', 1)
    Unknown2042(1)
    sprite('ce090_03', 6)
    sprite('ce090_04', 6)

@State
def CmnActGuardBreakCrouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce091_00', 2)
    sprite('ce091_01', 2)
    sprite('ce091_02', 1)
    Unknown2042(1)
    sprite('ce091_03', 6)
    sprite('ce091_04', 6)

@State
def CmnActGuardBreakAir():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce092_00', 2)
    sprite('ce092_01', 2)
    sprite('ce092_02', 1)
    Unknown2042(1)
    sprite('ce092_03', 6)
    sprite('ce092_04', 6)

@State
def CmnActAirTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce025_00', 3)
    sprite('ce025_01', 3)
    sprite('ce025_00ex', 3)

@State
def CmnActLockWait():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_02', 1)
    sprite('ce040_01', 3)
    sprite('ce040_00', 3)

@State
def CmnActLockReject():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce312_00', 7)
    sprite('ce312_01', 7)
    sprite('ce312_02', 2)
    sprite('ce312_03', 2)
    sprite('ce312_04', 3)
    sprite('ce312_05', 3)
    sprite('ce312_06', 3)
    sprite('ce312_07', 3)

@State
def CmnActAirLockWait():
    sprite('null', 60)

@State
def CmnActAirLockReject():
    sprite('null', 60)

@State
def CmnActLandSpin():
    sprite('null', 60)

@State
def CmnActLandSpinDown():
    sprite('null', 60)

@State
def CmnActVertSpin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce071_02', 2)
    sprite('ce071_03', 2)
    sprite('ce071_04', 2)
    sprite('ce071_05', 2)
    sprite('ce071_06', 2)
    sprite('ce071_07', 2)
    sprite('ce071_08', 2)
    sprite('ce071_09', 2)
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce077_00', 2)
    sprite('ce077_01', 2)
    sprite('ce077_00ex01', 2)
    sprite('ce077_01ex01', 2)
    sprite('ce077_00ex02', 2)
    sprite('ce077_01ex02', 2)
    sprite('ce077_00ex03', 2)
    sprite('ce077_01ex03', 2)
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce077_02', 4)
    label(0)
    sprite('ce077_03', 3)
    sprite('ce077_04', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce077_05', 5)
    sprite('ce077_06', 4)

@State
def CmnActAomukeSlideKeep():
    sprite('null', 60)

@State
def CmnActAomukeSlideEnd():
    sprite('null', 60)

@State
def CmnActBurstBegin():
    sprite('null', 60)

@State
def CmnActBurstLoop():
    sprite('null', 60)

@State
def CmnActBurstEnd():
    sprite('null', 60)

@State
def CmnActAirBurstBegin():
    sprite('null', 60)

@State
def CmnActAirBurstLoop():
    sprite('null', 60)

@State
def CmnActAirBurstEnd():
    sprite('null', 60)

@State
def CmnActOverDriveBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_00', 3)
    sprite('ce333_01', 3)
    sprite('ce333_02', 3)
    sprite('ce333_03', 32767)
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActOverDriveLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_04', 3)
    label(0)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_08', 6)
    sprite('ce333_09', 6)

@State
def CmnActAirOverDriveBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_10', 3)
    sprite('ce333_11', 3)
    sprite('ce333_12', 3)
    sprite('ce333_13', 32767)
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActAirOverDriveLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_14', 3)
    label(0)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_15', 3)
    sprite('ce333_16', 3)
    sprite('ce020_05', 3)
    sprite('ce020_06', 3)
    label(0)
    sprite('ce020_07', 4)
    sprite('ce020_08', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_00', 3)
    sprite('ce333_01', 3)
    sprite('ce333_02', 3)
    sprite('ce333_03', 32767)
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActCrossRushLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_04', 3)
    label(0)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_08', 6)
    sprite('ce333_09', 6)

@State
def CmnActAirCrossRushBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_10', 3)
    sprite('ce333_11', 3)
    sprite('ce333_12', 3)
    sprite('ce333_13', 32767)
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActAirCrossRushLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_14', 3)
    label(0)
    sprite('ce333_05', 3)
    sprite('ce333_06', 3)
    sprite('ce333_07', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_15', 3)
    sprite('ce333_16', 3)
    sprite('ce020_05', 3)
    sprite('ce020_06', 3)
    label(0)
    sprite('ce020_07', 4)
    sprite('ce020_08', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_00', 2)
    sprite('ce331_01', 2)
    label(0)
    sprite('ce331_02', 3)
    sprite('ce331_03', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_04', 2)
    sprite('ce331_05', 2)
    label(0)
    sprite('ce331_06', 3)
    sprite('ce331_07', 3)
    sprite('ce331_08', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_09', 3)
    sprite('ce331_10', 3)

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_11', 2)
    sprite('ce331_12', 2)
    label(0)
    sprite('ce331_02', 3)
    sprite('ce331_03', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_04', 2)
    sprite('ce331_05', 2)
    label(0)
    sprite('ce331_06', 3)
    sprite('ce331_07', 3)
    sprite('ce331_08', 3)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_13', 3)
    sprite('ce331_14', 3)
    sprite('ce020_05', 3)
    sprite('ce020_06', 3)
    label(0)
    sprite('ce020_07', 4)
    sprite('ce020_08', 4)
    loopRest()
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        EnableCollision(0)
        Unknown2034(0)
        teleportRelativeY(0)
    sprite('null', 32767)

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
        Unknown11050('020000006365343034537461724566660000000000000000000000000000000000000000')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 2)
    sprite('null', 600)
    label(100)
    sprite('null', 28)
    sprite('null', 1)
    Unknown1086(22)
    teleportRelativeX(-180000)
    teleportRelativeX(-800000)
    teleportRelativeY(1800000)
    physicsXImpulse(160000)
    physicsYImpulse(-360000)
    callSubroutine('MinervaCallAttack')
    Unknown23029(11, 252, 0)
sprite('ce404_04', 2)
sprite('ce404_05', 3)
GFX_0('ce404KickEff', 100)
sprite('ce404_06', 3)
label(0)
sprite('ce404_05', 3)
sprite('ce404_06', 3)
gotoLabel(0)
label(9)
sprite('keep', 3)
Unknown1019(30)
sprite('ce404_07', 3)
Unknown21012('63653430344b69636b456666000000000000000000000000000000000000000020000000')
clearUponHandler(2)
Unknown21007(11, 32)
Unknown1084(1)
sprite('ce404_08', 6)
sprite('ce404_09', 6)
sprite('ce404_10', 4)
sprite('ce404_11', 3)
endState()

@State
def CmnActChangePartnerQuickIn():
    sprite('ce032_01', 3)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    sprite('ce032_02', 3)
    sprite('ce032_03', 3)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    sprite('ce032_04', 5)
    sprite('ce032_05', 5)
    sprite('ce032_06', 5)
    sprite('ce032_07', 5)

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ce033_01', 3)
    physicsYImpulse(0)
    setGravity(0)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 3)
    sprite('ce033_03', 3)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_01', 3)
    sprite('ce033_02', 3)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_03', 3)
    sprite('ce033_01', 3)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 3)
    sprite('ce033_03', 3)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_01', 3)
    sprite('keep', 30)

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ce033_00', 2)
    sprite('ce033_01', 2)
    sprite('ce033_02', 2)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    callSubroutine('RCEffCheck')
    sprite('ce033_03', 3)
    label(0)
    sprite('ce033_01', 2)
    sprite('ce033_02', 2)
    sprite('ce033_03', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce033_04', 2)
    sprite('ce033_05', 2)
    sprite('ce033_06', 2)

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
        callSubroutine('MinervaCall')
    sprite('ce620_00', 4)
    Unknown23029(11, 604, 0)
    sprite('ce620_01', 4)
    sprite('ce620_02', 8)
    sprite('ce620_03', 12)
    sprite('ce620_04', 8)
    sprite('ce620_05', 12)
    sprite('ce620_02', 8)
    sprite('ce620_03', 12)
    sprite('ce001_00', 4)
    sprite('ce000_00', 4)
    sprite('ce000_00', 30)
    loopRest()

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(99)
    sprite('null', 2)
    label(0)
    sprite('ce020_07', 4)
    Unknown1019(95)
    sprite('ce020_08', 4)
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ce024_01', 2)
    Unknown8000(100, 1, 1)
    sprite('keep', 100)

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 403, 0)
        Unknown4020(11)
    sprite('ce610_00', 3)
    sprite('ce610_01', 3)
    sprite('ce610_02', 3)
    sprite('ce610_03', 3)
    tag_voice(1, 'bce104_0', 'bce104_1', 'bce104_2', '')
    sprite('ce610_04', 3)
    sprite('ce610_05', 12)
    sprite('ce610_02', 6)
    sprite('ce610_01', 6)
    sprite('ce610_00', 6)
    sprite('ce000_00', 5)
    sprite('ce208_00', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_01', 5)
    sprite('ce208_00', 5)

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown11063(1)
        SLOT_54 = 5

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if (SLOT_145 > 400000):
                    Unknown2037(0)
                    SLOT_54 = 0
                if Unknown48('1900000002000000000000001800000002000000aa000000'):
                    Unknown2037(0)
                    SLOT_54 = 0
            if SLOT_53:
                Unknown30078(10)
                Unknown21000(3)
                SLOT_53 = (SLOT_53 + (-25))
                if (SLOT_161 == 1):
                    Unknown21000(1)
                    Unknown30030(1)
                if (not Unknown48('1900000002000000000000001800000002000000aa000000')):
                    Unknown36(24)
                    Unknown30078(10)
                    Unknown21000(3)
                    Unknown35()
    sprite('ce432_00', 6)
    Unknown23029(11, 100, 0)
    sprite('ce432_01', 6)
    sprite('ce432_04', 6)
    tag_voice(1, 'bce109_0', 'bce109_1', 'bce109_2', '')
    sprite('ce432_05', 6)
    sprite('ce432_06', 6)
    sprite('ce432_07', 6)
    sprite('ce432_08', 6)
    sprite('ce432_09', 3)
    Unknown23029(11, 404, 0)
    sprite('ce432_09', 3)
    GFX_0('SuperHealEff', -1)
    sprite('ce432_10', 6)
    Unknown30078(200)
    Unknown21000(50)
    if (not Unknown48('1900000002000000000000001800000002000000aa000000')):
        Unknown36(24)
        Unknown30078(200)
        Unknown21000(50)
        Unknown35()
    sprite('ce432_11', 5)
    sprite('keep', 1)
    Unknown2037(1)
    label(0)
    sprite('ce432_09', 6)
    SLOT_53 = (SLOT_53 + 500)
    sprite('ce432_10', 6)
    sprite('ce432_11', 5)
    sprite('keep', 1)
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 < 0):
        SLOT_54 = 0
    loopRest()
    if SLOT_IsInOverdrive2:
        _gotolabel(0)
    label(1)
    sprite('ce432_12', 6)
    Unknown21012('53757065724865616c456666000000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_13', 6)
    sprite('ce432_14', 6)
    sprite('ce432_15', 6)

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('PartnerSkillInit')
        AttackLevel_(4)
        Damage(2000)
        Unknown11050('02000000636565665f686974656666440000000000000000000000000000000000000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        AirPushbackY(35000)
    sprite('ce260_00', 2)
    sprite('ce214_00', 3)
    physicsXImpulse(10000)
    sprite('ce214_01', 3)
    Unknown1019(500)
    sprite('ce214_02', 2)
    sprite('ce214_03', 2)
    StartMultihit()
    Unknown1019(50)
    Unknown7009(4)
    sprite('ce214_04', 3)
    RefreshMultihit()
    Unknown1019(50)
    GFX_0('mv214Eff', -1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_18')
    sprite('ce214_05', 2)
    Recovery()
    Unknown1019(75)
    sprite('ce214_06', 2)
    Unknown1019(75)
    sprite('ce214_07', 2)
    Unknown1019(75)
    sprite('ce214_08', 2)
    Unknown1084(1)
    sprite('ce260_00', 3)
    sprite('ce260_01', 3)
    sprite('ce260_02', 3)
    sprite('ce260_03', 3)
    sprite('ce260_04', 3)
    sprite('ce260_05', 3)

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
    sprite('null', 1)
    Unknown2036(95, -1, 0)
    sprite('null', 1)
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-400000)
    Unknown1019(4)
    label(0)
    sprite('ce020_07', 3)
    sprite('ce020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)
    if SLOT_58:
        enterState('UltimateDUOSP')
    else:
        enterState('UltimateDUO')

@State
def UltimateDUO():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 432, 0)
        Unknown4020(11)
        Unknown23056('')
        Unknown30063(1)
        Unknown2003(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 434):
                clearUponHandler(43)
                setInvincible(0)
        loopRelated(17, 160)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce208_00', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 1)
    sprite('ce208_02', 4)
    sprite('ce208_00', 5)
    sprite('ce207_00', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    setInvincible(0)
    sprite('ce207_04', 5)
    label(0)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_00', 5)

@State
def UltimateDUOSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 433, 0)
        Unknown4020(11)
        Unknown23056('')
        Unknown30063(1)
        Unknown2003(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 434):
                clearUponHandler(43)
                setInvincible(0)
        loopRelated(17, 160)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce208_00', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 1)
    sprite('ce208_02', 4)
    sprite('ce208_00', 5)
    sprite('ce207_00', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    setInvincible(0)
    sprite('ce207_04', 5)
    label(0)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_00', 5)

@State
def CmnActChangeRequest():
    sprite('null', 60)

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)
    label(0)
    sprite('null', 8)
    Unknown1086(22)
    teleportRelativeX(-50000)
    teleportRelativeX(-580000)
    Unknown1007(2900000)
    physicsXImpulse(20000)
    physicsYImpulse(-100000)
    sendToLabelUpon(2, 9)
    label(1)
    sprite('ce213_08ex00', 3)
    GFX_0('mv213Eff', -1)
    sprite('ce213_08ex01', 3)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 1)
    Unknown1084(1)
    clearUponHandler(2)
    GFX_1('ceef_402_stone', 0)
    sprite('ce213_08', 2)
    StartMultihit()
    Unknown8004(100, 1, 1)
    Unknown26('mv213Eff')
    sprite('ce213_09', 3)
    sprite('ce213_10', 3)
    sprite('ce213_11', 3)
    sprite('ce260_00', 3)
    sprite('ce260_01', 3)
    sprite('ce260_02', 3)
    sprite('ce260_03', 4)
    sprite('ce260_04', 4)
    sprite('ce260_05', 3)

@State
def CmnActChangeReturnAppealBurst():
    sprite('ce111_05', 6)
    sprite('ce111_06', 6)
    sprite('ce111_07', 32)
    sprite('ce111_08', 8)
    sprite('ce111_09', 30)

@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 30)
    sprite('null', 1)
    teleportRelativeX(-25000)
    Unknown1007(600000)
    setGravity(0)
    physicsYImpulse(-60000)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    label(0)
    sprite('ce213_08ex00', 3)
    GFX_0('mv213Eff', -1)
    sprite('ce213_08ex01', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    Unknown1084(1)
    clearUponHandler(2)
    GFX_1('ceef_402_stone', 0)
    sprite('ce213_08', 3)
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    StartMultihit()
    Unknown8004(100, 1, 1)
    Unknown26('mv213Eff')
    sprite('ce213_09', 3)
    sprite('ce213_10', 3)
    sprite('ce213_11', 3)
    sprite('ce260_00', 3)
    sprite('ce260_01', 3)
    sprite('ce260_02', 3)
    sprite('ce260_03', 3)
    sprite('ce260_04', 3)
    sprite('ce260_05', 3)

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('keep', 1)
    StartMultihit()
    sprite('ce213_09', 5)
    sprite('ce213_10', 5)
    sprite('ce213_11', 5)
    sprite('ce205_00', 2)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 2)
    sprite('ce205_02', 2)
    sprite('ce205_03', 3)
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)
    sprite('ce205_03ex02', 3)
    sprite('ce205_04', 1)
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    Unknown7007('6263653130365f300000000000000000640000006263653130365f310000000000000000640000006263653130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ce205_06', 2)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)
    Unknown1019(50)
    sprite('ce205_07', 8)
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)
    Unknown1019(50)
    sprite('ce205_09', 7)
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)
    sprite('ce205_11', 7)

@Subroutine
def DriveInitFirst():
    Hitstop(9)
    Unknown61(0, 1, 0, 5, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    SLOT_59 = SLOT_0

    def upon_CLEAR_OR_EXIT():
        if SLOT_51:
            clearUponHandler(3)
            if (SLOT_59 == 1):
                SFX_4('bce110_0')
            if (SLOT_59 == 2):
                SFX_4('bce110_1')
            if (SLOT_59 == 3):
                SFX_4('bce110_2')
            if (SLOT_59 == 4):
                SFX_4('bce300_0')
            if (SLOT_59 == 5):
                SFX_4('bce300_1')
    callSubroutine('MinervaNoneCallAttack')

@Subroutine
def DriveInitSecond():
    Hitstop(9)

    def upon_CLEAR_OR_EXIT():
        if SLOT_51:
            clearUponHandler(3)
            if (SLOT_59 == 1):
                SFX_4('bce111_0')
            if (SLOT_59 == 2):
                SFX_4('bce111_1')
            if (SLOT_59 == 3):
                SFX_4('bce111_2')
            if (SLOT_59 == 4):
                SFX_4('bce301_0')
            if (SLOT_59 == 5):
                SFX_4('bce301_1')
    callSubroutine('MinervaNoneCallAttack')

@Subroutine
def DriveInitThird():

    def upon_CLEAR_OR_EXIT():
        if SLOT_51:
            clearUponHandler(3)
            if (SLOT_59 == 1):
                SFX_4('bce112_0')
            if (SLOT_59 == 2):
                SFX_4('bce112_1')
            if (SLOT_59 == 3):
                SFX_4('bce112_2')
            if (SLOT_59 == 4):
                SFX_4('bce302_0')
            if (SLOT_59 == 5):
                SFX_4('bce302_1')
    callSubroutine('MinervaNoneCallAttack')

@Subroutine
def DeriveInputFirst():
    Unknown14070('NmlAtk5BB')
    Unknown14070('NmlAtk2BB')

@Subroutine
def DeriveTimingFirst():
    Unknown14072('NmlAtk5BB')
    Unknown14072('NmlAtk2BB')

@Subroutine
def DeriveInputSecond():
    Unknown14070('NmlAtk5BBB')

@Subroutine
def DeriveTimingSecond():
    Unknown14072('NmlAtk5BBB')

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        Unknown2003(1)
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
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 200, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce207_00', 3)
    sprite('ce207_00', 2)
    Unknown7009(1)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_00', 5)

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 201, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce218_00', 3)
    sprite('ce218_00', 2)
    sprite('ce218_01', 5)
    sprite('ce218_02', 5)
    sprite('ce218_03', 5)
    sprite('ce218_04', 5)
    sprite('ce218_01', 5)
    sprite('ce218_00', 5)

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 202, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce217_00', 3)
    sprite('ce217_00', 2)
    Unknown7007('6263653131335f300000000000000000640000006263653131335f310000000000000000640000006263653131335f320000000000000000000000000000000000000000000000000000000000000000')
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_04', 5)
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_00', 5)

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        JumpCancel_(0)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 203, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce217_00', 3)
    sprite('ce208_01', 4)
    sprite('ce208_02', 4)
    sprite('ce208_03', 4)
    sprite('ce208_04', 4)
    sprite('ce208_01', 5)
    sprite('ce440_00', 4)
    physicsXImpulse(-3000)
    sprite('ce440_01', 4)
    Unknown1019(200)
    sprite('ce440_02', 4)
    Unknown7007('6263653238325f300000000000000000640000006263653238325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ce440_03', 4)
    Unknown1019(80)
    sprite('ce440_04', 4)
    Unknown1019(80)
    sprite('ce440_05', 4)
    Unknown1019(80)
    sprite('ce440_06', 4)
    Unknown1019(80)
    sprite('ce440_07', 4)
    Unknown1084(1)
    sprite('ce440_08', 20)
    Unknown18009(1)
    sprite('ce440_09', 6)
    sprite('ce440_10', 6)

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11092(1)
        HitOrBlockCancel('NmlAtk5A')
        WhiffCancel('AN_NmlAtk4ALoop')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
    sprite('ce200_00', 3)
    Unknown1051(60)
    sprite('ce200_01', 2)
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    sprite('ce200_02', 2)
    sprite('keep', 1)
    if (not CheckInput(0x1)):
        sendToLabel(0)
    sprite('ce200_03', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_04', 3)
    RefreshMultihit()
    sprite('ce200_05', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)
    sprite('ce200_00', 3)
    ExitState()
    label(0)
    sprite('ce200_03', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 4)
    sprite('ce200_00', 4)
    ExitState()

@State
def AN_NmlAtk4ALoop():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11092(1)
        HitOrBlockCancel('NmlAtk5A')
        WhiffCancel('AN_NmlAtk4ALoop')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
    sprite('ce200_05', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_02', 2)
    sprite('keep', 1)
    if (not CheckInput(0x1)):
        sendToLabel(0)
    sprite('ce200_03', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_04', 3)
    RefreshMultihit()
    sprite('ce200_05', 5)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)
    sprite('ce200_00', 3)
    ExitState()
    label(0)
    sprite('ce200_03', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 4)
    sprite('ce200_00', 4)
    ExitState()

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(600)
        AttackP1(90)
        AttackP2(75)
        Unknown11092(1)
        AirPushbackX(4000)
        AirPushbackY(23000)
        Unknown14077(0)
        Unknown1112('')
    sprite('ce260_00', 3)
    sprite('ce214_00', 2)
    physicsXImpulse(5000)
    sprite('ce214_01', 2)
    Unknown1019(500)
    sprite('ce214_02', 2)
    sprite('ce214_03', 2)
    Unknown1019(50)
    SLOT_51 = 1
    callSubroutine('DeriveInputFirst')
    Hitstop(6)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ce214_04', 4)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1700)
    Unknown11050('02000000636565665f686974656666440000000000000000000000000000000000000000')
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirUntechableTime(30)
    Hitstop(9)
    PushbackX(19950)
    Unknown14077(1)
    HitOrBlockJumpCancel(1)
    Unknown1019(50)
    callSubroutine('DriveInitFirst')
    GFX_0('mv214Eff', -1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_18')
    sprite('ce214_05', 3)
    Unknown1019(75)
    setInvincible(0)
    sprite('ce214_06', 3)
    Unknown1019(75)
    Recovery()
    Unknown2063()
    sprite('ce214_07', 3)
    Unknown1019(75)
    sprite('ce214_08', 3)
    sprite('keep', 2)
    Unknown1019(0)
    callSubroutine('DeriveTimingFirst')
    sprite('ce260_00', 2)
    sprite('keep', 2)
    enterState('DriveEnd')

@State
def DriveEnd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Recovery()
    sprite('ce260_01', 4)
    sprite('ce260_02', 4)
    sprite('ce260_03', 4)
    sprite('ce260_04', 4)
    sprite('ce260_05', 4)

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(550)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(2000)
        PushbackX(2500)
        Unknown9190(1)
        Unknown11057(400)
        Unknown11058('0000000000000000010000000000000000000000')
        callSubroutine('DriveInitSecond')
        Hitstop(2)
        DisableAttackRestOfMove()
        JumpCancel_(0)
    sprite('ce260_00', 2)
    sprite('ce204_01', 2)
    sprite('ce204_02', 2)
    setInvincible(1)
    GuardPoint_(0)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown22036(0)
    Unknown22026(0)
    physicsXImpulse(10000)
    sprite('ce204_03', 3)
    RefreshMultihit()
    AirPushbackX(1750)
    AirPushbackY(-25000)
    callSubroutine('DeriveInputSecond')
    sprite('ce204_04', 2)
    SLOT_51 = 1
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(2000)
    Unknown9190(0)
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    physicsXImpulse(40000)
    sprite('ce204_05', 2)
    Unknown1019(120)
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv204ringLoops', -1)
    sprite('ce204_04', 2)
    RefreshMultihit()
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_05', 2)
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_04', 2)
    RefreshMultihit()
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_05', 2)
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_04', 2)
    RefreshMultihit()
    physicsXImpulse(55000)
    EnableCollision(0)
    AirHitstunAnimation(10)
    AirPushbackX(5400)
    AirPushbackY(24000)
    PushbackX(19800)
    AirUntechableTime(34)
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    sprite('ce204_05', 2)
    sprite('ce204_06', 2)
    setInvincible(0)
    Recovery()
    Unknown2063()
    Unknown23073()
    Unknown1019(80)
    Unknown26('mv204ringLoops')
    sprite('ce204_07', 2)
    Unknown1019(80)
    sprite('ce204_08', 2)
    Unknown1019(80)
    callSubroutine('DeriveTimingSecond')
    JumpCancel_(1)
    sprite('ce204_09', 2)
    Unknown1019(80)
    sprite('keep', 2)
    Unknown1019(0)
    sprite('ce260_00', 2)
    sprite('keep', 2)
    enterState('DriveEnd')

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(60)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(15000)
        AirPushbackY(28000)
        Unknown11050('02000000636565665f686974656666440000000000000000000000000000000000000000')
        callSubroutine('DriveInitThird')

        def upon_12():
            Unknown2037(1)
    sprite('ce270_00', 3)
    sprite('ce270_01', 3)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce270_02', 2)
    sprite('ce270_03', 2)
    sprite('ce270_04', 2)
    SLOT_51 = 1
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_22')
    sprite('ce270_05', 4)
    GFX_0('ceef_270', 4)
    GFX_1('ceef_270burner', 1)
    GFX_1('ceef_270burner', 2)
    GFX_1('ceef_270burner', 3)
    sprite('ce270_06', 3)
    sprite('ce270_07', 3)
    loopRest()
    if SLOT_2:
        enterState('Finish_Healing')
    sprite('ce270_11', 3)
    sprite('ce270_12', 3)
    loopRest()
    enterState('DriveEnd')

@State
def Finish_Healing():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)

        def upon_CLEAR_OR_EXIT():
            if SLOT_53:
                Unknown30078(100)
                SLOT_53 = (SLOT_53 + (-100))
                if (SLOT_161 == 1):
                    Unknown21000(1)
                    Unknown30030(1)
    sprite('ce270_08', 6)
    sprite('ce270_09', 6)
    sprite('ce270_10', 6)
    sprite('ce432_09', 3)
    callSubroutine('MinervaCallAttack')
    Unknown23029(11, 404, 0)
    sprite('ce432_09', 3)
    GFX_0('SuperHealEff', -1)
    SLOT_53 = (SLOT_53 + 3000)
    sprite('ce432_10', 6)
    sprite('ce432_11', 6)
    sprite('ce432_12', 5)
    Unknown21012('53757065724865616c456666000000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_13', 4)
    sprite('ce432_14', 4)
    sprite('ce432_15', 4)

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8004(100, 1, 1)
            sendToLabel(1)
    sprite('ce213_00', 3)
    sprite('ce213_01', 3)
    physicsXImpulse(15000)
    physicsYImpulse(20000)
    setGravity(2800)
    tag_voice(1, 'bce156_0', 'bce156_1', '', '')
    sprite('ce213_02', 3)
    sprite('ce213_03', 3)
    sprite('ce213_04', 3)
    sprite('ce213_05', 3)
    label(0)
    sprite('ce213_06', 3)
    GFX_0('mv213Eff', -1)
    SFX_3('cese_19')
    sprite('ce213_07', 3)
    gotoLabel(0)
    label(1)
    sprite('ce213_08', 3)
    sprite('ce213_11', 3)
    sprite('ce260_01', 3)
    sprite('ce260_02', 3)
    sprite('ce260_03', 5)
    sprite('ce260_04', 5)
    sprite('ce260_05', 5)

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 3)
    sprite('ce213_11', 3)
    sprite('ce260_01', 3)
    sprite('ce260_02', 3)
    sprite('ce260_03', 3)
    sprite('ce260_04', 3)
    sprite('ce260_05', 3)
    sprite('ce203_00', 4)
    tag_voice(0, 'bce157_0', 'bce157_1', '', '')
    sprite('ce203_01', 4)
    sprite('ce203_02', 3)
    RefreshMultihit()
    GFX_0('mv203Eff', -1)
    SFX_0('003_swing_grap_0_0')
    SFX_3('cese_19')
    sprite('ce203_03', 4)
    sprite('ce203_04', 3)
    sprite('ce203_05', 2)
    sprite('keep', 2)
    sprite('ce260_00', 2)
    sprite('ce260_01', 4)
    sprite('ce260_02', 4)
    sprite('ce260_03', 4)
    sprite('ce260_04', 4)
    sprite('ce260_05', 4)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce340_00', 2)
    sprite('ce340_01', 2)
    GFX_0('mv340ConsentEff', 0)
    sprite('ce340_03', 2)
    sprite('ce340_04', 3)
    sprite('ce340_05', 2)
    sprite('ce340_06', 3)
    sprite('ce340_10', 1)
    RefreshMultihit()
    GFX_1('ceef_340_tukieff', 0)
    SFX_3('cese_06')
    sprite('ce340_10', 2)
    Unknown21012('6d76333430436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown8004(100, 1, 1)
    sprite('ce340_11', 6)
    sprite('ce340_12', 6)
    sprite('ce340_13', 3)
    sprite('ce340_14', 3)
    sprite('ce340_15', 3)
    sprite('ce340_16', 2)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('ce401_00', 1)
    sprite('ce401_01', 1)
    sprite('ce205_00', 2)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)
    sprite('ce205_02', 2)
    sprite('ce205_03', 3)
    tag_voice(0, 'bce158_0', 'bce158_1', '', '')
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)
    sprite('ce205_03ex02', 3)
    sprite('ce205_04', 1)
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)
    Unknown1019(50)
    sprite('ce205_07', 8)
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)
    Unknown1019(50)
    sprite('ce205_09', 7)
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)
    sprite('ce205_11', 7)

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCallCrushAssault')
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce401_00', 1)
    SLOT_4 = 0
    callSubroutine('MinervaNoneCallAttack')
    sprite('ce401_01', 1)
    sprite('ce205_00', 2)
    tag_voice(0, 'bce158_0', 'bce158_1', '', '')
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)
    sprite('ce205_02', 2)
    sprite('ce205_03', 3)
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)
    sprite('ce205_03ex02', 3)
    sprite('ce205_04', 1)
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)
    Unknown1019(50)
    sprite('ce205_07', 8)
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)
    Unknown1019(50)
    sprite('ce205_09', 7)
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)
    sprite('ce205_11', 7)

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('null', 13)
    sprite('null', 1)
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-800000)
    sprite('ce602_00', 3)
    physicsXImpulse(30000)
    callSubroutine('MinervaCallCrushAssault')
    Unknown23029(11, 100, 0)
    sprite('ce602_01', 3)
    Unknown23029(11, 111, 0)
    sprite('ce602_02', 3)
    sprite('ce602_03', 3)
    sprite('ce602_04', 3)
    sprite('ce602_05', 3)
    sprite('ce210_05', 6)
    Unknown1019(20)
    sprite('ce210_06', 3)
    Unknown1019(20)
    sprite('ce210_07', 3)
    Unknown1019(25)
    physicsYImpulse(10000)
    setGravity(1000)
    RefreshMultihit()
    sprite('ce210_07', 6)
    StartMultihit()
    sprite('ce210_08', 8)
    StartMultihit()
    sprite('ce210_09', 5)
    StartMultihit()
    Unknown1019(25)
    Unknown8000(100, 1, 1)
    sprite('ce210_10', 4)
    sprite('ce210_11', 4)
    Unknown1084(1)
    sprite('ce210_12', 4)
    sprite('ce210_13', 4)
    sprite('ce210_14', 4)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        callSubroutine('MinervaCallCrushAssault')
    sprite('keep', 11)
    StartMultihit()
    setGravity(1000)
    sprite('ce210_09', 5)
    RefreshMultihit()
    Unknown1019(25)
    Unknown8000(100, 1, 1)
    sprite('ce210_10', 4)
    Unknown23029(11, 100, 0)
    sprite('ce210_11', 4)
    Unknown1084(1)
    sprite('ce210_12', 4)
    sprite('ce210_13', 4)
    sprite('ce210_14', 4)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ce401_00', 1)
    sprite('ce401_01', 1)
    sprite('ce205_00', 2)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)
    sprite('ce205_02', 2)
    sprite('ce205_03', 3)
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)
    sprite('ce205_03ex02', 3)
    sprite('ce205_04', 1)
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)
    Unknown1019(50)
    sprite('ce205_07', 8)
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)
    Unknown1019(50)
    sprite('ce205_09', 7)
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)
    sprite('ce205_11', 7)

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCallCrushAssault')
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    label(0)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce401_00', 1)
    SLOT_4 = 0
    callSubroutine('MinervaNoneCallAttack')
    sprite('ce401_01', 1)
    sprite('ce205_00', 2)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)
    sprite('ce205_02', 2)
    sprite('ce205_03', 3)
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)
    sprite('ce205_03ex02', 3)
    sprite('ce205_04', 1)
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)
    Unknown1019(50)
    sprite('ce205_07', 8)
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)
    Unknown1019(50)
    sprite('ce205_09', 7)
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)
    sprite('ce205_11', 7)

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Unknown2003(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 230, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce237_00', 3)
    Unknown1051(60)
    sprite('ce237_00', 2)
    Unknown7009(1)
    sprite('ce237_01', 5)
    sprite('ce237_02', 5)
    sprite('ce237_03', 5)
    sprite('ce237_03', 3)
    sprite('ce237_00', 5)

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirPushbackX(-2500)
        AirPushbackY(20000)
        PushbackX(10000)
        AirUntechableTime(24)
        GroundedHitstunAnimation(11)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11050('02000000636565665f686974656666440000000000000000000000000000000000000000')
        callSubroutine('DriveInitFirst')
    sprite('ce233_00', 3)
    sprite('ce233_01', 3)
    sprite('ce233_02', 6)
    sprite('ce233_03', 6)
    callSubroutine('DeriveInputFirst')
    SLOT_51 = 1
    sprite('ce233_04', 4)
    physicsXImpulse(35000)
    GFX_0('mv233Eff', 0)
    SFX_0('003_swing_grap_0_2')
    SFX_3('cese_19')
    sprite('ce233_05', 3)
    Unknown1019(50)
    sprite('ce233_06', 3)
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('ce233_07', 2)
    Unknown1019(0)
    sprite('keep', 2)
    callSubroutine('DeriveTimingFirst')
    sprite('ce260_00', 2)
    sprite('keep', 2)
    enterState('DriveEnd')

@State
def NmlAtk2BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        HitLow(2)
        AttackP1(90)
        GroundedHitstunAnimation(11)
        AirUntechableTime(34)
        AirPushbackX(1000)
        AirPushbackY(23000)
        PushbackX(19950)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11050('02000000636565665f686974656666440000000000000000000000000000000000000000')
        callSubroutine('DriveInitSecond')
    sprite('ce260_00', 2)
    sprite('ce234_00', 2)
    GFX_0('mv234ConsentEff', 0)
    sprite('ce234_01', 2)
    sprite('ce234_02', 2)
    sprite('ce234_03', 2)
    callSubroutine('DeriveInputSecond')
    SLOT_51 = 1
    sprite('ce234_04', 3)
    RefreshMultihit()
    GFX_0('mv234Eff', -1)
    SFX_0('003_swing_grap_0_1')
    SFX_3('cese_18')
    sprite('ce234_05', 3)
    Recovery()
    Unknown2063()
    Unknown21012('6d76323334436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('ce234_06', 3)
    sprite('ce234_07', 2)
    Unknown21012('6d76323334436f6e73656e74456666000000000000000000000000000000000021000000')
    sprite('keep', 2)
    callSubroutine('DeriveTimingSecond')
    sprite('ce260_00', 3)
    sprite('keep', 2)
    enterState('DriveEnd')

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Unknown2003(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 231, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce238_00', 3)
    Unknown1051(60)
    sprite('ce238_00', 2)
    Unknown7009(5)
    sprite('ce238_01', 5)
    sprite('ce238_02', 5)
    sprite('ce238_03', 5)
    sprite('ce238_04', 5)
    sprite('ce238_01', 5)
    sprite('ce238_02', 5)
    sprite('ce238_00', 5)

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown2003(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 250, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce258_00', 3)
    sprite('ce258_00', 2)
    Unknown7009(1)
    sprite('ce258_01', 5)
    sprite('ce258_02', 5)
    sprite('ce258_03', 5)
    sprite('ce258_04', 5)
    sprite('ce258_01', 5)
    sprite('ce258_02', 5)
    sprite('ce258_00', 5)

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown2003(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 251, 0)
        Unknown4020(11)

        def upon_43():
            if (SLOT_48 == 800):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ce257_00', 3)
    sprite('ce257_00', 2)
    sprite('ce257_01', 5)
    sprite('ce257_02', 5)
    sprite('ce257_03', 5)
    sprite('ce257_04', 5)
    sprite('ce257_00', 5)

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(-60000)
        Unknown9310(1)
        Unknown11001(0, 0, 0)
        AirUntechableTime(30)
        PushbackX(15000)
        callSubroutine('DriveInitFirst')
        HitOverhead(0)
        Hitstop(3)
        Unknown11050('02000000636565665f686974656666440000000000000000000000000000000000000000')
    sprite('ce253_00', 3)
    sprite('ce253_01', 3)
    Unknown1084(1)
    physicsXImpulse(4500)
    Unknown1028(300)
    physicsYImpulse(25000)
    setGravity(2200)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)

    def upon_4():
        clearUponHandler(4)
        sendToLabel(100)
    Unknown23087(100000)
    sprite('ce253_02', 3)
    sprite('ce213_03', 3)
    sprite('ce213_04', 3)
    sprite('ce213_05', 2)
    sprite('ce213_06', 32767)
    label(100)
    sprite('keep', 3)
    SLOT_51 = 1
    callSubroutine('DeriveInputFirst')
    Unknown1021(-30000)
    SFX_3('cese_19')
    label(0)
    sprite('ce213_08ex00', 3)
    GFX_0('mv213Eff', -1)
    sprite('ce213_08ex01', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    Unknown1084(1)
    callSubroutine('DeriveInputFirst')
    clearUponHandler(2)
    GFX_1('ceef_402_stone', 0)
    sprite('ce213_08', 2)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    Unknown11001(0, 0, 8)
    AirPushbackX(6500)
    AirPushbackY(-18000)
    Unknown9190(1)
    Unknown9118(100)
    Unknown9311()
    Hitstop(9)
    Unknown8004(100, 1, 1)
    Unknown26('mv213Eff')
    sprite('ce213_09', 3)
    Recovery()
    Unknown2063()
    sprite('ce213_10', 3)
    sprite('ce213_11', 3)
    sprite('ce260_00', 5)
    callSubroutine('DeriveTimingFirst')
    sprite('keep', 2)
    enterState('DriveEnd')

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1900)
        AirUntechableTime(29)
        GroundedHitstunAnimation(9)
        AirPushbackX(65000)
        AirPushbackY(-70000)
        Unknown9310(1)
        Unknown11056(0)
        Unknown11050('020000006365343034537461724566660000000000000000000000000000000000000000')
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown1084(1)
        Unknown14082(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 252, 0)
    sprite('ce404_00', 3)
    physicsXImpulse(10000)
    physicsYImpulse(40000)
    sprite('ce404_01', 3)
    Unknown1019(75)
    YAccel(75)
    Unknown7007('6263653130385f300000000000000000640000006263653130385f310000000000000000640000006263653130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ce404_02', 3)
    Unknown1019(75)
    YAccel(75)
    sprite('ce404_03', 3)
    Unknown1019(75)
    YAccel(75)
    sprite('ce404_04', 2)
    Unknown1019(75)
    YAccel(75)
    sprite('ce404_05', 3)
    GFX_0('ce404KickEff', 100)
    Unknown1084(1)
    physicsXImpulse(54000)
    physicsYImpulse(-63000)
    SFX_0('000_airdash_0')
    SFX_0('004_swing_grap_1_2')
    SFX_3('cese_01')
    sprite('ce404_06', 3)
    label(0)
    sprite('ce404_05', 3)
    sprite('ce404_06', 3)
    gotoLabel(0)
    label(1)
    sprite('ce404_07', 5)
    Unknown21012('63653430344b69636b456666000000000000000000000000000000000000000020000000')
    clearUponHandler(2)
    Unknown21007(11, 32)
    Unknown1084(1)
    Recovery()
    sprite('ce404_08', 5)
    sprite('ce404_09', 5)
    sprite('ce404_10', 5)
    sprite('ce404_11', 5)

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
            Unknown8010(100, 1, 1)
            sendToLabel(1)
        if (SLOT_18 >= 3):
            if (SLOT_19 < 180000):
                Unknown8010(100, 1, 1)
                sendToLabel(1)

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('ce032_00', 3)
    label(0)
    sprite('ce032_01', 4)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    sprite('ce032_02', 4)
    SFX_3('cese_04')
    sprite('ce032_03', 4)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce310_00', 2)
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ce310_01', 1)
    sprite('ce310_02', 3)
    Unknown1084(1)
    sprite('ce310_03', 2)
    SFX_1('bce154')
    SFX_0('010_swing_sword_0')
    sprite('ce310_04', 2)
    sprite('ce310_05', 4)
    sprite('ce310_06', 5)
    sprite('ce310_07', 5)
    sprite('ce310_08', 5)

@Subroutine
def ThrowSpecialCancelInput():
    Unknown14070('CmnActInvincibleAttack')
    Unknown14070('InvincibleAttackFP')
    Unknown14070('ShotA')
    Unknown14070('ShotB')
    Unknown14070('ShotEx')
    Unknown14070('Assault')
    Unknown14070('AssaultFP')
    Unknown14070('MidAssault')
    Unknown14070('MidAssaultFP')
    Unknown14070('SpecialHeal')
    Unknown14070('SpecialHealFP')
    Unknown14070('UltimateShot')
    Unknown14070('UltimateShotSP')
    Unknown14070('UltimateAssault')
    Unknown14070('UltimateAssaultSP')
    Unknown14070('AstralHeat')

@Subroutine
def ThrowSpecialCancelBegin():
    Unknown14072('CmnActInvincibleAttack')
    Unknown14072('InvincibleAttackFP')
    Unknown14072('ShotA')
    Unknown14072('ShotB')
    Unknown14072('ShotEx')
    Unknown14072('Assault')
    Unknown14072('AssaultFP')
    Unknown14072('MidAssault')
    Unknown14072('MidAssaultFP')
    Unknown14072('SpecialHeal')
    Unknown14072('SpecialHealFP')
    Unknown14072('UltimateShot')
    Unknown14072('UltimateShotSP')
    Unknown14072('UltimateAssault')
    Unknown14072('UltimateAssaultSP')
    Unknown14072('AstralHeat')

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(2000)
        AttackP2(50)
        Hitstop(0)
        Unknown11001(0, 15, 15)
        Unknown9266(4)
        Unknown9016(1)
        AirPushbackX(10000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown2018(1, 80)
        Unknown2004(1, 0)
        JumpCancel_(0)
    sprite('ce310_02', 6)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ce311_00', 6)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('mv311ConsentEff', 1)
    sprite('ce311_01', 6)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('bce153')
    sprite('ce311_02', 20)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_03', 4)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_04', 4)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_3('cese_20')
    sprite('ce311_05', 4)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)
    callSubroutine('ThrowSpecialCancelInput')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_07', 3)
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown11072(1, 150000, 100000)
    sprite('ce311_08', 2)
    GFX_0('mv311Eff', -1)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000021000000')
    sprite('ce311_10', 3)
    callSubroutine('ThrowSpecialCancelBegin')
    sprite('ce311_11', 3)
    sprite('ce311_12', 3)
    sprite('ce311_13', 3)
    sprite('ce311_14', 3)

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('ce032_00', 3)
    label(0)
    sprite('ce032_01', 4)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    sprite('ce032_02', 4)
    SFX_3('cese_04')
    sprite('ce032_03', 4)
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce310_00', 2)
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ce310_01', 1)
    sprite('ce310_02', 3)
    Unknown1084(1)
    sprite('ce310_03', 2)
    SFX_1('bce154')
    SFX_0('010_swing_sword_0')
    sprite('ce310_04', 2)
    sprite('ce310_05', 4)
    sprite('ce310_06', 5)
    sprite('ce310_07', 5)
    sprite('ce310_08', 5)

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(2000)
        AttackP2(50)
        Hitstop(0)
        Unknown11001(0, 15, 15)
        Unknown9266(4)
        Unknown9016(1)
        AirPushbackX(10000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown2018(1, 80)
        Unknown13021(1)
        Unknown21005(1)
        Unknown2004(1, 0)
        JumpCancel_(0)
    sprite('ce310_02', 3)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ce310_00ex', 3)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce003_00ex01', 3)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce003_01ex01', 3)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce003_00ex02', 3)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce310_00exex01', 3)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_02', 6)
    Unknown2005()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('mv311ConsentEff', 1)
    SFX_1('bce153')
    sprite('ce311_03', 20)
    teleportRelativeX(110000)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_04', 4)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_3('cese_20')
    sprite('ce311_05', 4)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)
    callSubroutine('ThrowSpecialCancelInput')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_07', 1)
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown11072(1, 150000, 100000)
    sprite('ce311_08', 2)
    GFX_0('mv311Eff', -1)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    sprite('ce311_09', 2)
    sprite('ce311_08', 2)
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000021000000')
    sprite('ce311_10', 3)
    callSubroutine('ThrowSpecialCancelBegin')
    sprite('ce311_11', 3)
    sprite('ce311_12', 3)
    sprite('ce311_13', 3)
    sprite('ce311_14', 3)

@Subroutine
def DriveCancelDirection():
    if SLOT_6:
        Unknown2006()

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(3)
        Damage(2100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(8000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Unknown11050('02000000636565665f686974656666480000000000000000000000000000000000000000')
        GuardPoint_(1)
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
    sprite('ce401_00', 1)
    sprite('ce401_01', 1)
    sprite('ce205_00', 2)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)
    sprite('ce205_02', 2)
    sprite('ce205_02', 1)
    label(1)
    sprite('ce205_04', 2)
    tag_voice(1, 'bce200_0', 'bce200_1', 'bce200_2', '')
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_11')
    physicsXImpulse(30000)
    sprite('ce205_06', 3)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(80)
    sprite('ce205_06', 3)
    Unknown1019(50)
    sprite('ce205_07', 6)
    Unknown8004(100, 1, 1)
    setInvincible(0)
    Unknown1019(25)
    sprite('ce205_08', 6)
    Unknown1019(50)
    sprite('ce260_01', 7)
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce260_02', 7)
    sprite('ce260_03', 7)
    sprite('ce260_04', 7)
    sprite('ce260_05', 7)

@State
def InvincibleAttackFP():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2400)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(8000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Hitstop(20)
        Unknown11050('02000000636565665f686974656666480000000000000000000000000000000000000000')
        GuardPoint_(1)
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
        Unknown30070('436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    sprite('ce401_00', 1)
    Unknown23119(14474340, 10, 2)
    sprite('ce401_01', 1)
    sprite('ce401_02', 2)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce401_03', 1)
    sprite('ce401_04', 1)
    sprite('ce401_05', 1)
    sprite('ce401_05', 1)
    label(101)
    sprite('ce401_07', 2)
    tag_voice(1, 'bce200_0', 'bce200_1', 'bce200_2', '')
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce401_08', 2)
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_11')
    physicsXImpulse(30000)
    sprite('ce401_09', 3)
    GFX_0('ce401PanchEff', -1)
    Unknown1019(80)
    sprite('ce401_09', 3)
    Unknown1019(50)
    sprite('ce401_10', 6)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    setInvincible(0)
    Unknown1019(25)
    sprite('ce401_11', 6)
    Unknown1019(50)
    sprite('ce260_01', 7)
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce260_02', 7)
    sprite('ce260_03', 7)
    sprite('ce260_04', 7)
    sprite('ce260_05', 7)

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 400, 0)
        Unknown4020(11)
        Unknown23029(11, 413, 0)
    sprite('ce208_00', 5)
    sprite('ce208_01', 5)
    tag_voice(1, 'bce201_0', 'bce201_1', 'bce201_2', '')
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    SFX_3('cese_08')
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_01', 3)
    sprite('ce208_00', 3)

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 401, 0)
        Unknown4020(11)
        Unknown23029(11, 413, 0)
    sprite('ce208_00', 5)
    sprite('ce208_01', 5)
    tag_voice(1, 'bce201_0', 'bce201_1', 'bce201_2', '')
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    SFX_3('cese_08')
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_01', 3)
    sprite('ce208_00', 3)

@State
def ShotEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 402, 0)
        Unknown4020(11)
    sprite('ce208_00', 3)
    sprite('ce208_00', 2)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('ce208_01', 5)
    tag_voice(1, 'bce105_0', 'bce105_1', 'bce105_2', '')
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    SFX_3('cese_08')
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_01', 3)
    sprite('ce208_00', 3)

@Subroutine
def CableDispON():
    GFX_0('AssaultPlug', 0)
    Unknown38(6, 1)
    SLOT_52 = 1
    Unknown13(7)
    GFX_0('Cable', 109)
    Unknown38(7, 1)
    Unknown4020(7)

@Subroutine
def CableDispOFF():
    Unknown21007(6, 33)
    SLOT_52 = 0
    Unknown13(7)

@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(2000)
        AirPushbackX(20000)
        AirPushbackY(13000)
        PushbackX(50000)
        GroundedHitstunAnimation(9)
        AttackP1(80)
        AirUntechableTime(33)
        Unknown11056(0)
        Unknown11050('02000000636565665f686974656666480000000000000000000000000000000000000000')
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown22019('0000000000000000000000000100000000000000')
        GuardPoint_(1)
        Unknown22031(-2, -1)
        Unknown22035(10)
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
        Unknown2016(260)
        Unknown2037(0)

        def upon_42():
            Unknown2037(1)

        def upon_11():
            clearUponHandler(11)
            sendToLabel(1)
    sprite('ce400_00', 1)
    sprite('ce400_01', 1)
    physicsXImpulse(-8000)
    sprite('ce400_02', 1)
    Unknown1019(50)
    sprite('ce215_00', 1)
    GFX_0('mv215ConsentEff', 0)
    Unknown1019(50)
    sprite('ce215_00', 1)
    Unknown1019(50)
    sprite('ce215_01', 2)
    sprite('ce215_02', 2)
    tag_voice(1, 'bce202_0', 'bce202_1', 'bce202_2', '')
    sprite('ce215_03', 2)
    setInvincible(1)
    sprite('ce215_04', 1)
    physicsXImpulse(0)
    sprite('ce215_05', 2)
    StartMultihit()
    physicsXImpulse(30000)
    SFX_3('cese_22')
    GFX_0('ce215JetEff', 1)
    GFX_0('ce215JetEff', 2)
    callSubroutine('CableDispON')
    sprite('ce215_06', 2)
    Unknown1019(200)
    sprite('ce215_05', 2)
    Unknown1019(140)
    sprite('ce215_06', 2)
    sprite('ce215_05', 2)
    loopRest()
    Unknown19(0, 2, 2)
    sprite('ce215_06', 2)
    sprite('ce215_05', 2)
    label(0)
    sprite('ce215_07', 2)
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('63653231354a657445666600000000000000000000000000000000000000000020000000')
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce215_07', 2)
    Unknown1019(50)
    sprite('ce215_08', 5)
    callSubroutine('CableDispOFF')
    Unknown1019(50)
    sprite('ce215_09', 5)
    Unknown1019(40)
    sprite('ce215_10', 4)
    Unknown1019(40)
    sprite('ce215_11', 4)
    Unknown1019(40)
    sprite('ce215_12', 4)
    Unknown1019(0)
    ExitState()
    label(1)
    sprite('keep', 3)
    Unknown1019(80)
    sprite('ce215_07', 2)
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('63653231354a657445666600000000000000000000000000000000000000000020000000')
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce215_07', 2)
    Unknown1019(25)
    sprite('ce215_08', 3)
    callSubroutine('CableDispOFF')
    Unknown1019(25)
    sprite('ce215_09', 3)
    Unknown1084(1)
    sprite('ce215_10', 3)
    sprite('ce215_11', 3)
    sprite('ce215_12', 3)

@State
def AssaultFP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2200)
        AirPushbackX(28000)
        AirPushbackY(18000)
        PushbackX(50000)
        GroundedHitstunAnimation(9)
        AttackP1(80)
        AirUntechableTime(33)
        Unknown11056(0)
        Unknown11050('02000000636565665f686974656666480000000000000000000000000000000000000000')
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown22019('0000000000000000000000000100000000000000')
        GuardPoint_(1)
        Unknown22031(-1, -1)
        Unknown22035(10)
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
        Unknown2016(260)
        Unknown2037(0)

        def upon_42():
            Unknown2037(1)

        def upon_11():
            clearUponHandler(11)
            Unknown21012('63653430304a65744566664261636b4669726541746b0000000000000000000021000000')
            sendToLabel(1)
    sprite('ce400_00', 1)
    Unknown23119(14474340, 10, 2)
    sprite('ce400_01', 1)
    physicsXImpulse(-8000)
    sprite('ce400_02', 1)
    Unknown1019(50)
    sprite('ce400_03', 1)
    GFX_0('mv215ConsentEff', 0)
    Unknown1019(50)
    sprite('ce400_03', 1)
    Unknown1019(50)
    sprite('ce400_04', 1)
    setInvincible(1)
    sprite('ce400_05', 1)
    sprite('ce400_06', 2)
    tag_voice(1, 'bce202_0', 'bce202_1', 'bce202_2', '')
    sprite('ce400_07', 2)
    sprite('ce400_08', 1)
    Unknown1019(0)
    sprite('ce400_09', 2)
    StartMultihit()
    physicsXImpulse(30000)
    SFX_3('cese_09')
    GFX_0('ce400JetEff', 1)
    GFX_0('ce400JetEff', 2)
    GFX_0('ce400JetEffBackFireAtk', 3)
    GFX_0('mv400windMatome', -1)
    callSubroutine('CableDispON')
    sprite('ce400_10', 2)
    Unknown1019(200)
    sprite('ce400_09', 2)
    Unknown1019(140)
    sprite('ce400_10', 2)
    sprite('ce400_09', 2)
    loopRest()
    Unknown19(0, 2, 2)
    sprite('ce400_10', 2)
    sprite('ce400_09', 2)
    label(0)
    sprite('ce400_11', 2)
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown21012('63653430304a657445666600000000000000000000000000000000000000000020000000')
    Unknown26('mv400windMatome')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce400_11', 2)
    Unknown1019(50)
    sprite('ce215_08', 5)
    Unknown21012('63653430304a65744566664261636b4669726541746b0000000000000000000021000000')
    callSubroutine('CableDispOFF')
    Unknown1019(50)
    sprite('ce215_09', 5)
    Unknown1019(40)
    sprite('ce215_10', 4)
    Unknown1019(40)
    sprite('ce215_11', 4)
    Unknown1019(40)
    sprite('ce215_12', 4)
    Unknown1019(0)
    ExitState()
    label(1)
    sprite('keep', 3)
    Unknown1019(80)
    sprite('ce400_11', 2)
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown21012('63653430304a657445666600000000000000000000000000000000000000000020000000')
    Unknown26('mv400windMatome')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce400_11', 2)
    Unknown1019(50)
    sprite('ce215_08', 3)
    Unknown21012('63653430304a65744566664261636b4669726541746b0000000000000000000021000000')
    callSubroutine('CableDispOFF')
    Unknown1019(25)
    sprite('ce215_09', 3)
    Unknown1084(1)
    sprite('ce215_10', 3)
    sprite('ce215_11', 3)
    sprite('ce215_12', 3)

@State
def MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(2300)
        AttackP1(80)
        AirUntechableTime(37)
        Hitstop(16)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        AirPushbackY(-40000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(25)
        Unknown11056(0)
        Unknown22019('0100000001000000000000000100000000000000')
        GuardPoint_(1)
        Unknown22031(-2, -1)
        Unknown22035(10)
        Unknown2016(240)
        Unknown2015(200)
        Unknown11050('02000000636565665f686974656666480000000000000000000000000000000000000000')
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
    sprite('ce402_00', 3)
    sprite('ce402_01', 3)
    sprite('ce402_02', 4)
    sprite('ce235_00', 3)
    GFX_0('mv235ConsentEff', 0)
    sprite('ce235_01', 3)
    setInvincible(1)
    sprite('ce235_02', 2)
    tag_voice(1, 'bce203_0', 'bce203_1', 'bce203_2', '')
    sprite('ce235_03', 2)
    sprite('ce235_04', 5)
    SFX_0('005_swing_grap_2_2')
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000020000000')
    physicsXImpulse(60000)
    Unknown1028(-7000)
    sprite('ce235_05', 5)
    SFX_3('cese_22')
    GFX_0('mv235Eff', -1)
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown8004(100, 1, 1)
    Unknown1084(1)
    Unknown2016(100)
    Unknown2015(100)
    sprite('ce235_06', 6)
    setInvincible(0)
    Recovery()
    sprite('ce235_07', 6)
    sprite('ce235_08', 4)
    sprite('ce235_09', 4)
    sprite('ce235_10', 4)

@State
def MidAssaultFP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2500)
        GroundedHitstunAnimation(9)
        AttackP1(80)
        AirUntechableTime(39)
        Hitstop(16)
        HitOverhead(2)
        AirPushbackY(-60000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(25)
        Unknown11056(0)
        Unknown22019('0100000001000000000000000100000000000000')
        GuardPoint_(1)
        Unknown22031(-1, -1)
        Unknown22035(10)
        Unknown2016(240)
        Unknown2015(200)
        Unknown11050('02000000636565665f686974656666480000000000000000000000000000000000000000')
        callSubroutine('MinervaNoneCallAttack')
        callSubroutine('DriveCancelDirection')
    sprite('ce402_00', 3)
    Unknown23119(14474340, 10, 2)
    sprite('ce402_01', 3)
    sprite('ce402_02', 4)
    sprite('ce402_03', 3)
    GFX_0('mv235ConsentEff', 0)
    sprite('ce402_04', 3)
    setInvincible(1)
    sprite('ce402_05', 4)
    tag_voice(1, 'bce203_0', 'bce203_1', 'bce203_2', '')
    sprite('ce235_04', 5)
    SFX_0('005_swing_grap_2_2')
    GFX_1('ceef_402_dashsmoke', 0)
    GFX_1('ceef_402_dashsmoke', 1)
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000020000000')
    physicsXImpulse(90000)
    Unknown1028(-7000)
    sprite('ce402_06', 5)
    SFX_3('cese_10')
    GFX_0('mv402Eff', -1)
    GFX_1('ceef_402_stone', 0)
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    Unknown1084(1)
    Unknown2016(100)
    Unknown2015(100)
    sprite('ce402_07', 6)
    setInvincible(0)
    Recovery()
    sprite('ce402_08', 6)
    sprite('ce235_08', 4)
    sprite('ce235_09', 4)
    sprite('ce235_10', 4)

@State
def SpecialHeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 100, 0)
        loopRelated(17, 66)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(101)
    sprite('ce432_00', 3)
    GFX_0('ceef_healjunbieff', -1)
    sprite('ce432_01', 3)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 404, 0)
    GFX_0('ceef_HealJunbiAnim_R', -1)
    GFX_0('ceef_HealJunbiAnim_L', -1)
    tag_voice(1, 'bce204_0', 'bce204_1', 'bce204_2', '')
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    Unknown21012('636565665f6865616c6a756e626965666600000000000000000000000000000020000000')
    GFX_0('ceef_HealKurukuru', -1)
    sprite('ce432_04', 6)
    sprite('ce432_05', 6)
    sprite('ce432_06', 6)
    sprite('ce432_07', 6)
    sprite('ce432_08', 6)
    sprite('ce432_09', 6)
    GFX_0('SuperHealEff', -1)
    Unknown30078(17000)
    Unknown21000(1)
    Unknown30030(1)
    label(100)
    sprite('ce432_10', 6)
    sprite('ce432_11', 6)
    sprite('ce432_09', 6)
    gotoLabel(100)
    label(101)
    sprite('ce432_12', 6)
    Unknown21012('53757065724865616c456666000000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_13', 6)
    sprite('ce432_14', 6)
    sprite('ce432_15', 6)

@State
def SpecialHealFP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 100, 0)
        loopRelated(17, 66)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(101)

        def upon_CLEAR_OR_EXIT():
            if SLOT_53:
                Unknown21000(100)
                SLOT_53 = (SLOT_53 + (-100))
    sprite('ce432_00', 3)
    GFX_0('ceef_healjunbieff', -1)
    sprite('ce432_01', 3)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 404, 0)
    GFX_0('ceef_HealJunbiAnim_R', -1)
    GFX_0('ceef_HealJunbiAnim_L', -1)
    tag_voice(1, 'bce204_0', 'bce204_1', 'bce204_2', '')
    sprite('ce432_02', 3)
    sprite('ce432_03', 3)
    Unknown21012('636565665f6865616c6a756e626965666600000000000000000000000000000020000000')
    GFX_0('ceef_HealKurukuru', -1)
    sprite('ce432_04', 6)
    sprite('ce432_05', 6)
    sprite('ce432_06', 6)
    sprite('ce432_07', 6)
    sprite('ce432_08', 6)
    sprite('ce432_09', 6)
    GFX_0('SuperHealEffSP', -1)
    SLOT_53 = (SLOT_53 + 3000)
    label(100)
    sprite('ce432_10', 6)
    sprite('ce432_11', 6)
    sprite('ce432_09', 6)
    gotoLabel(100)
    label(101)
    sprite('ce432_12', 6)
    sprite('ce432_13', 6)
    sprite('ce432_14', 6)
    Unknown21012('53757065724865616c456666535000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_15', 6)

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 430, 0)
        Unknown4020(11)
        Unknown23055('')
        Unknown2003(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 434):
                clearUponHandler(43)
                setInvincible(0)
        loopRelated(17, 160)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce208_00', 5)
    Unknown30080('')
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce250_0', 'bce250_1', '', '')
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 1)
    sprite('ce208_02', 4)
    sprite('ce208_00', 5)
    sprite('ce207_00', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    setInvincible(0)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    tag_voice(0, 'bce251_0', 'bce251_1', '', '')
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    label(0)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_00', 5)

@State
def UltimateShotSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 431, 0)
        Unknown4020(11)
        Unknown23055('')
        Unknown2003(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 434):
                clearUponHandler(43)
                setInvincible(0)
        loopRelated(17, 160)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce208_00', 5)
    Unknown30080('')
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce250_0', 'bce250_1', '', '')
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 5)
    sprite('ce208_03', 5)
    sprite('ce208_04', 5)
    sprite('ce208_01', 5)
    sprite('ce208_02', 1)
    sprite('ce208_02', 4)
    sprite('ce208_00', 5)
    sprite('ce207_00', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    setInvincible(0)
    sprite('ce207_04', 5)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    tag_voice(0, 'bce251_0', 'bce251_1', '', '')
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    label(0)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_03', 5)
    sprite('ce207_04', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)
    sprite('ce207_02', 5)
    sprite('ce207_00', 5)

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(3)
            Unknown20001(1)
            Unknown20007(1)
            Unknown20003(1)
            Unknown2053(0)
            Unknown13024(0)
            sendToLabel(3)
        sendToLabelUpon(33, 4)
        sendToLabelUpon(32, 9)
        AttackLevel_(3)
        Damage(100)
        MinimumDamagePct(50)
        Unknown11092(1)
        Unknown11064(1)
        Unknown11084(1)
        Unknown11066(1)
        Unknown32('43654d696e657276614c696768740000')
        AirHitstunAnimation(4)
        AirUntechableTime(35)
        hitstun(35)
        Hitstop(1)
        PushbackX(0)
        Unknown11084(1)
        Unknown11056(0)
        Unknown9016(1)
        Unknown3032()
        Unknown11069('UltimateAssaultAddAttack')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown20002(0)
            Unknown20003(0)
            Unknown20004(0)
            Unknown23084(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_38:
                Unknown23045('73000000')
                if (SLOT_22 < SLOT_0):
                    sendToLabel(1)
            else:
                Unknown23045('73000000')
                if (SLOT_22 > SLOT_0):
                    sendToLabel(1)
        callSubroutine('MinervaNoneCallAttack')
    sprite('mv430_00', 5)
    setInvincible(1)
    Unknown22026(0)
    Unknown30080('')
    Unknown2036(113, -1, 2)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce252_0', 'bce252_1', '', '')
    sprite('mv430_01', 5)
    GFX_0('mv430ConsentEff', 0)
    sprite('mv430_02', 3)
    GFX_0('ThrowUpCelica', -1)
    Unknown22026(1)
    callSubroutine('RCEffCheck')
    sprite('mv430_03', 3)
    sprite('mv430_04', 8)
    Unknown20002(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown20005(60, 120)
    sprite('mv430_05', 6)
    sprite('mv430_06', 6)
    sprite('mv430_07', 6)
    sprite('mv430_08', 6)
    sprite('mv430_09', 2)
    sprite('mv430_10', 8)
    GFX_0('HensinThunder', -1)
    Unknown21012('6d76343330436f6e73656e74456666000000000000000000000000000000000020000000')
    ScreenShake(0, 200000)
    sprite('mv430_11', 30)
    sprite('mv430_12', 10)
    physicsXImpulse(2500)
    Unknown3029(1)
    Unknown3070(3)
    Unknown3071(3)
    Unknown3072('c8000000c8000000fa000000fa000000')
    Unknown3073('9600000096000000c8000000c8000000')
    Unknown3076(1000)
    Unknown3077(1000)
    sprite('mv430_13', 10)
    Unknown1019(200)
    Unknown20002(0)
    Unknown20003(0)
    Unknown20004(0)
    sprite('mv430_14', 10)
    Unknown26('HensinThunder')
    Unknown1019(200)
    Unknown3001(255)
    Unknown3004(-21)
    sprite('mv430_15', 3)
    Unknown3001(64)
    Unknown3004(0)
    StartMultihit()
    Unknown8009(1)
    SFX_3('cese_09')
    EnableCollision(0)
    Unknown2015(250)
    Unknown2053(0)
    Unknown2034(0)
    sprite('mv430_15', 60)
    Unknown3029(0)
    Unknown1019(900)
    Unknown1028(1000)
    label(1)
    sprite('null', 5)
    Unknown2005()
    Unknown1084(1)
    Unknown23032(0)
    EnableCollision(1)
    Unknown2015(100)
    Unknown2053(1)
    Unknown2034(1)
    sprite('null', 15)
    Unknown23024(0)
    sprite('ce020_07', 2)
    sendToLabelUpon(2, 12)
    Unknown23033(40)
    physicsYImpulse(-30000)
    Unknown1043()
    Unknown3004(21)
    label(11)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(11)
    label(12)
    sprite('ce024_00', 3)
    clearUponHandler(2)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 15000)
    GFX_1('ceef_600falleff', -1)
    Unknown3001(255)
    setInvincible(0)
    sprite('ce024_01', 4)
    sprite('ce024_02', 4)
    sprite('ce024_03', 6)
    sprite('ce024_04', 6)
    ExitState()
    label(3)
    sprite('mv430_15', 5)
    Unknown3001(64)
    Unknown3004(-12)
    StartMultihit()
    Unknown1028(0)
    Unknown2015(150)
    sprite('mv430_15', 25)
    physicsXImpulse(0)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 130)
    GFX_0('ShungokuEff', -1)
    Unknown23084(1)
    GFX_0('UltimateAssaultAddAttack', -1)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    label(4)
    sprite('mv430_15', 2)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(3000)
    MinimumDamagePct(10)
    Unknown11064(0)
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9142(9999)
    Unknown9130(60)
    Unknown9132(60)
    Hitstop(0)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')
    Unknown23159('UltimateAssaultFinish')
    Unknown3001(255)
    Unknown3038(0)
    Unknown36(22)
    Unknown3001(255)
    Unknown3038(0)
    Unknown35()
    physicsXImpulse(30000)
    sprite('mv430_15', 1)
    sprite('mv430_20', 6)
    Unknown26('ShungokuEff')
    Unknown23084(0)
    Unknown23024(1)
    Unknown13024(1)
    Unknown2053(1)
    Unknown2034(1)
    Unknown1019(130)
    Unknown20007(0)
    Unknown20003(0)
    Unknown20004(0)
    sprite('mv430_21', 8)
    Unknown1019(50)
    sprite('mv430_22', 10)
    Unknown1019(50)
    sprite('mv430_22', 10)
    Unknown1019(50)
    sprite('mv430_23', 6)
    Unknown1019(50)
    sprite('mv430_24', 6)
    Unknown1019(50)
    sprite('mv430_19', 180)
    Unknown2005()
    Unknown13021(1)
    GFX_0('ThrowDownCelica', -1)
    Unknown1019(0)
    label(9)
    sprite('ce024_02', 1)
    Unknown23024(0)
    clearUponHandler(32)
    EnableCollision(1)
    setInvincible(0)
    SFX_0('024_getset_a')
    sprite('ce024_02', 4)
    sprite('ce024_03', 5)
    tag_voice(1, 'bce253_0', 'bce253_1', '', '')
    sprite('ce024_04', 5)
    sprite('ce024_05', 5)

@State
def UltimateAssaultSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(3)
            Unknown20001(1)
            Unknown20007(1)
            Unknown20003(1)
            Unknown2053(0)
            Unknown13024(0)
            sendToLabel(3)
        sendToLabelUpon(33, 4)
        sendToLabelUpon(32, 9)
        AttackLevel_(3)
        Damage(1000)
        MinimumDamagePct(10)
        Unknown11092(1)
        Unknown11064(1)
        Unknown11084(1)
        Unknown11066(1)
        Unknown32('43654d696e657276614c696768740000')
        AirHitstunAnimation(4)
        AirUntechableTime(25)
        hitstun(25)
        Hitstop(1)
        PushbackX(0)
        Unknown11084(1)
        Unknown11056(0)
        Unknown9016(1)
        Unknown3032()
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('UltimateAssaultSP')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown20002(0)
            Unknown20003(0)
            Unknown20004(0)
            Unknown23084(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_38:
                Unknown23045('73000000')
                if (SLOT_22 < SLOT_0):
                    sendToLabel(1)
            else:
                Unknown23045('73000000')
                if (SLOT_22 > SLOT_0):
                    sendToLabel(1)
        callSubroutine('MinervaNoneCallAttack')
    sprite('mv430_00', 5)
    setInvincible(1)
    Unknown22026(0)
    Unknown30080('')
    Unknown2036(113, -1, 2)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce252_0', 'bce252_1', '', '')
    sprite('mv430_01', 5)
    GFX_0('mv430ConsentEff', 0)
    sprite('mv430_02', 3)
    GFX_0('ThrowUpCelica', -1)
    Unknown22026(1)
    callSubroutine('RCEffCheck')
    sprite('mv430_03', 3)
    sprite('mv430_04', 8)
    Unknown20002(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown20005(60, 120)
    sprite('mv430_05', 6)
    sprite('mv430_06', 6)
    sprite('mv430_07', 6)
    sprite('mv430_08', 6)
    sprite('mv430_09', 2)
    sprite('mv430_10', 8)
    Unknown21012('6d76343330436f6e73656e74456666000000000000000000000000000000000020000000')
    GFX_0('HensinThunder', -1)
    ScreenShake(0, 200000)
    sprite('mv430_11', 30)
    sprite('mv430_12', 10)
    physicsXImpulse(2500)
    Unknown3029(1)
    Unknown3070(3)
    Unknown3071(3)
    Unknown3072('c8000000c8000000fa000000fa000000')
    Unknown3073('9600000096000000c8000000c8000000')
    Unknown3076(1000)
    Unknown3077(1000)
    sprite('mv430_13', 10)
    Unknown1019(200)
    Unknown20002(0)
    Unknown20003(0)
    Unknown20004(0)
    sprite('mv430_14', 10)
    Unknown26('HensinThunder')
    Unknown1019(200)
    Unknown3001(255)
    Unknown3004(-12)
    sprite('mv430_15', 3)
    Unknown3001(128)
    Unknown3004(0)
    StartMultihit()
    Unknown8009(1)
    SFX_3('cese_09')
    EnableCollision(0)
    Unknown2015(250)
    Unknown2053(0)
    Unknown2034(0)
    sprite('mv430_15', 60)
    Unknown3029(0)
    Unknown1019(900)
    Unknown1028(1000)
    label(1)
    sprite('null', 5)
    Unknown2005()
    Unknown1084(1)
    Unknown23032(0)
    EnableCollision(1)
    Unknown2015(100)
    Unknown2053(1)
    Unknown2034(1)
    sprite('null', 15)
    Unknown23024(0)
    sprite('ce020_07', 2)
    sendToLabelUpon(2, 12)
    Unknown23033(40)
    physicsYImpulse(-30000)
    Unknown1043()
    Unknown3004(21)
    label(11)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(11)
    label(12)
    sprite('ce024_00', 3)
    clearUponHandler(2)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 15000)
    GFX_1('ceef_600falleff', -1)
    Unknown3001(255)
    setInvincible(0)
    sprite('ce024_01', 4)
    sprite('ce024_02', 4)
    sprite('ce024_03', 6)
    sprite('ce024_04', 6)
    ExitState()
    label(3)
    sprite('mv430_20', 1)
    physicsXImpulse(90000)
    Unknown1028(0)
    Unknown23011(1)
    sprite('mv430_20', 1)
    Unknown23011(1)
    sprite('mv430_20', 1)
    Unknown23011(1)
    sprite('mv430_21', 3)
    GFX_0('ShungokuODSlashEff', -1)
    sprite('mv430_22', 2)
    Unknown1019(30)
    sprite('mv430_22', 4)
    Unknown1019(50)
    sprite('mv430_15', 1)
    RefreshMultihit()
    AirUntechableTime(40)
    hitstun(40)
    Unknown9016(1)
    Unknown11057(700)
    Unknown2005()
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('mv430_20', 1)
    physicsXImpulse(90000)
    Unknown23011(1)
    sprite('mv430_20', 1)
    Unknown23011(1)
    sprite('mv430_20', 1)
    Unknown23011(1)
    GFX_0('ShungokuODSlashEff2', -1)
    sprite('mv430_21', 3)
    Unknown1019(25)
    sprite('mv430_22', 2)
    Unknown1019(50)
    sprite('mv430_22', 1)
    sprite('mv430_22', 22)
    sprite('mv430_15', 3)
    sendToLabelUpon(12, 100)
    Unknown2005()
    physicsXImpulse(9000)
    StartMultihit()
    sprite('mv430_15', 15)
    Unknown1019(1500)
    RefreshMultihit()
    Hitstop(0)
    GFX_0('ShungokuODSlashEff3', -1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('UltimateAssaultAddAttackSP')
    sprite('keep', 1)
    sendToLabel(1)
    label(100)
    sprite('mv430_15', 3)
    clearUponHandler(12)
    Unknown3001(64)
    Unknown3004(-21)
    StartMultihit()
    Unknown2015(150)
    sprite('mv430_15', 25)
    physicsXImpulse(0)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 130)
    GFX_0('ShungokuEff', -1)
    Unknown23084(1)
    GFX_0('UltimateAssaultAddAttackSP', -1)
    GFX_0('ShungokuODFinishEff', -1)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    Unknown35()
    label(4)
    sprite('mv430_15', 2)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(3000)
    MinimumDamagePct(19)
    Unknown11064(0)
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9142(9999)
    Unknown9130(60)
    Unknown9132(60)
    Unknown11069('')
    Unknown3038(0)
    Unknown3001(255)
    Unknown3004(0)
    Unknown36(22)
    Unknown3001(255)
    Unknown3004(0)
    Unknown3038(0)
    Unknown35()
    physicsXImpulse(30000)
    Unknown23159('UltimateAssaultODFinish')
    sprite('mv430_15', 1)
    sprite('mv430_20', 6)
    Unknown26('ShungokuEff')
    Unknown23084(0)
    Unknown23024(1)
    Unknown13024(1)
    Unknown2053(1)
    Unknown2034(1)
    Unknown1019(130)
    Unknown20007(0)
    Unknown20003(0)
    Unknown20004(0)
    sprite('mv430_21', 8)
    Unknown1019(50)
    sprite('mv430_22', 10)
    Unknown1019(50)
    sprite('mv430_22', 10)
    Unknown1019(50)
    sprite('mv430_23', 6)
    Unknown1019(50)
    sprite('mv430_24', 6)
    Unknown1019(50)
    sprite('mv430_19', 180)
    Unknown2005()
    Unknown13021(1)
    GFX_0('ThrowDownCelica', -1)
    Unknown1019(0)
    label(9)
    sprite('ce024_02', 1)
    Unknown23024(0)
    clearUponHandler(32)
    EnableCollision(1)
    setInvincible(0)
    SFX_0('024_getset_a')
    sprite('ce024_02', 4)
    sprite('ce024_03', 5)
    tag_voice(1, 'bce253_0', 'bce253_1', '', '')
    sprite('ce024_04', 5)
    sprite('ce024_05', 5)

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(2100)
        Unknown9142(2000)
        AirUntechableTime(500)
        PushbackX(30000)
        Hitstop(0)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11056(0)
        Unknown11072(1, 100000, 0)
        Unknown11064(1)
        Unknown11069('AstralHeatExe')
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown28(12, 'AstralHeatExe')
        Unknown2054(1)
        Unknown1084(1)
        setInvincible(1)
        DisableAttackRestOfMove()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 100, 0)
    sprite('ce450_00', 6)
    sprite('ce450_01', 4)
    Unknown2036(52, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_CE_AH', -1)
    tag_voice(1, 'bce290_0', 'bce290_1', '', '')
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    GFX_0('ceef450_Kousoku', -1)
    RefreshMultihit()
    SFX_0('022_magiccircle_a')
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_02', 4)
    sprite('ce450_03', 4)
    sprite('ce450_04', 4)
    sprite('ce450_28', 5)
    sprite('ce450_29', 5)
    sprite('ce450_23', 5)
    sprite('ce450_24', 5)
    sprite('ce450_25', 5)
    sprite('ce450_26', 5)
    Unknown8000(100, 1, 1)
    sprite('ce450_27', 5)

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(0)
        MinimumDamagePct(100)
        Unknown11068(1)
        Hitstop(0)
        Unknown11064(1)
        AirPushbackX(1000)
        AirPushbackY(-50000)
        Unknown9310(150)
        Unknown11084(1)
        Unknown11072(1, 50000, 100000)
        EnableCollision(0)
        Unknown23088(1, 1)
        Unknown23157(0)
        Unknown20002(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)
        Unknown20006(1)
        Unknown2053(0)
        Unknown2034(0)
        DisableAttackRestOfMove()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 500, 0)
        Unknown4020(11)
        SFX_0('107_throw_catch')

        def upon_31():
            if SLOT_2:
                Unknown36(22)
                Unknown21000(100)
                Unknown35()
    sprite('ce450_02', 5)
    Unknown21012('636565663435305f4b6f75736f6b75000000000000000000000000000000000020000000')
    sprite('ce450_03', 5)
    sprite('ce450_04', 5)
    sprite('ce450_05', 5)
    sprite('ce450_06', 5)
    sprite('ce450_07', 5)
    sprite('ce450_08', 5)
    tag_voice(0, 'bce291_0', 'bce291_1', '', '')
    sprite('ce450_09', 5)
    sprite('ce450_10', 5)
    sprite('ce450_11', 5)
    sprite('ce450_12', 5)
    sprite('ce450_13', 5)
    sprite('ce450_14', 5)
    sprite('ce450_15', 5)
    Unknown2037(1)
    GFX_0('ceef450_BG', -1)
    SFX_3('cese_03')
    Unknown21012('636565663435305f4b6f75736f6b75000000000000000000000000000000000021000000')
    callSubroutine('RCEffCheck')
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    tag_voice(0, 'bce292_0', 'bce292_1', '', '')
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    tag_voice(0, 'bce293_0', 'bce293_1', '', '')
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    Unknown21012('636565663435305f42470000000000000000000000000000000000000000000020000000')
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    Unknown20000(0)
    sprite('ce450_15', 5)
    GFX_0('AstCameraObj', -1)
    Unknown38(4, 1)
    sprite('ce450_16', 30)
    Unknown3032()
    Unknown3004(-26)
    Unknown2037(0)
    Unknown36(22)
    Unknown21000(100000)
    Unknown3032()
    Unknown3004(-26)
    teleportRelativeY(100000000)
    setGravity(0)
    Unknown35()
    Unknown23024(3)
    Unknown23084(1)
    sprite('ce450_16', 260)
    GFX_0('AHCamera', -1)
    GFX_0('AHKiraEff', -1)
    sprite('ce450_16', 10)
    Unknown23024(2)
    sprite('ce450_16', 25)
    Unknown36(22)
    teleportRelativeY(0)
    Unknown35()
    Unknown21012('414843616d65726100000000000000000000000000000000000000000000000020000000')
    sprite('ce450_16', 10)
    sprite('ce450_16', 5)
    GFX_0('ceef450_BG3', -1)
    Unknown3004(26)
    Unknown36(22)
    Unknown3032()
    Unknown3004(26)
    Unknown35()
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    tag_voice(0, 'bce294_0', 'bce294_1', '', '')
    sprite('ce450_16', 5)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    Unknown21007(11, 32)
    RefreshMultihit()
    Unknown11067(1)
    Unknown11072(0, -1, -1)
    Unknown11050('02000000636565665f686974656666417374000000000000000000000000000000000000')
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(-200000)
    AirPushbackY(50000)
    AirUntechableTime(200)
    Unknown9310(200)
    Hitstop(60)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_15', 5)
    sprite('ce450_16', 5)
    GFX_0('mv450HanaTiri', -1)
    GFX_0('mv450SmokeMato', -1)
    sprite('ce450_17', 5)
    sprite('ce450_18', 5)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    GFX_0('AstDeathAttack', -1)
    GFX_0('mv450WhiteOut', -1)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    Unknown21007(4, 32)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_19', 2)
    sprite('ce450_20', 2)
    sprite('ce450_21', 2)
    sprite('ce450_22', 5)
    Unknown1000(260000)
    sprite('ce450_23', 5)
    sprite('ce450_24', 5)
    sprite('ce450_25', 5)
    sprite('ce450_26', 5)
    Unknown8000(100, 1, 1)
    sprite('ce450_27', 5)
    Unknown21007(11, 33)
    label(100)
    sprite('ce000_00', 50)
    Unknown21012('636565663435305f42473300000000000000000000000000000000000000000020000000')
    Unknown21012('414843616d65726100000000000000000000000000000000000000000000000021000000')
    sprite('ce620_00', 8)
    Unknown18010()
    tag_voice(0, 'bce295_0', 'bce295_1', '', '')
    sprite('ce620_01', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_04', 8)
    sprite('ce620_05', 8)
    sprite('ce620_04', 8)
    sprite('ce620_03', 8)
    sprite('ce620_02', 8)
    sprite('ce000_00', 8)
    sprite('ce610_00', 8)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 75)
    sprite('ce610_05', 32767)
    Unknown18008()
    loopRest()

@Subroutine
def MouthTableInit():
    Unknown18011('bce000', 13155, 14177, 14179, 14177, 14179, 13153, 25392, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bce600def', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24886, 25398, 24886, 25398, 24886, 12849, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600def', '001')
    Unknown18011('bce601def', 14177, 13155, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601def', '002')
    Unknown18011('bce602def', 12899, 12897, 25396, 13362, 12897, 25396, 14390, 12641, 25393, 12339, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce602def', '003')
    Unknown18011('bce603def', 12643, 12593, 13921, 13411, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce603def', '004')
    Unknown18011('bce604def', 14177, 14179, 14433, 14435, 14433, 14435, 12641, 25392, 24886, 25398, 24886, 25398, 24887, 25399, 24887, 25399, 24887, 25400, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce604def', '005')
    Unknown18011('bce605def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 12339, 13921, 13923, 13921, 13923, 13921, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce605def', '006')
    Unknown18011('bce700def', 14433, 14435, 14433, 14435, 12641, 25400, 12855, 14433, 13155, 24884, 25398, 24886, 25398, 24886, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce700def', '007')
    Unknown18011('bce701def', 12643, 13921, 13923, 13921, 13923, 12641, 25394, 12850, 14177, 14179, 14177, 14179, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701def', '008')
    Unknown18011('bce702def', 12899, 13665, 13411, 24888, 25400, 24888, 12337, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce702def', '009')
    Unknown18011('bce703def', 14433, 14435, 14433, 14435, 14433, 13155, 24883, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce703def', '010')
    Unknown18011('bce704def', 12643, 13921, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce704def', '011')
    Unknown18011('bce705def', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13155, 24886, 25400, 24888, 25400, 24888, 13361, 14179, 14177, 14179, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce705def', '012')
    Unknown18011('bce402_0', 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 13873, 13921, 13923, 13921, 13923, 14689, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bce402_1', 13155, 14177, 14179, 14177, 14179, 12641, 25395, 12594, 14177, 14179, 13921, 13923, 13921, 13923, 12641, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bce403_0', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25394, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bce403_1', 13923, 12897, 25396, 13619, 12641, 25395, 13105, 12641, 25395, 13105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bce601brg', 12641, 25392, 13109, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12643, 24887, 25398, 24886, 12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601brg', '017')
    Unknown18011('bce600bno', 13409, 25392, 14131, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 14689, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600bno', '018')
    Unknown18011('bce601bny', 14435, 14177, 14179, 14177, 14179, 14177, 12899, 24883, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 13107, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601bny', '019')
    Unknown18011('bce601bpt', 12643, 24880, 25398, 24886, 25398, 24886, 12849, 13667, 24882, 25398, 24886, 25400, 24888, 25400, 24888, 25400, 24888, 25399, 24887, 25398, 24886, 13873, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601bpt', '020')
    Unknown18011('bce601bph', 13155, 12897, 25393, 24887, 25400, 24888, 12337, 12643, 24880, 12337, 12899, 24881, 25399, 24887, 25400, 24888, 25399, 24887, 25400, 24888, 12338, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601bph', '021')
    Unknown18011('bce600pyu', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600pyu', '022')
    Unknown18011('bce601pka', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24881, 25398, 24886, 25398, 14641, 13665, 13667, 13665, 13667, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601pka', '023')
    Unknown18011('bce601pag', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24886, 25399, 24887, 25399, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601pag', '024')
    Unknown18011('bce600pel', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600pel', '025')
    Unknown18011('bce600uli', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25394, 13363, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600uli', '026')
    Unknown18011('bce601ume', 13921, 13923, 13921, 13923, 13921, 13923, 14433, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601ume', '027')
    Unknown18011('bce600uva', 12641, 25400, 14642, 12641, 25396, 12341, 12641, 25392, 24889, 25399, 24887, 25399, 24887, 12338, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600uva', '028')
    Unknown18011('bce600ryn', 14179, 14177, 14179, 14177, 14179, 12897, 25400, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 12641, 25392, 24887, 25399, 13361, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600ryn', '029')
    Unknown18011('bce601ahe', 14433, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25401, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce601ahe', '030')
    Unknown18011('bce602', 12899, 12897, 25392, 13874, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce602', '031')
    Unknown18011('bce600rne', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce600rne', '032')
    Unknown18011('bce700brg', 14433, 14435, 12641, 25394, 24888, 25400, 13876, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce700brg', '048')
    Unknown18011('bce701bno', 14433, 13155, 24888, 25399, 24887, 25399, 24887, 25399, 12594, 14177, 14179, 14177, 14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701bno', '033')
    Unknown18011('bce701bny', 13665, 12643, 24880, 25400, 13875, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701bny', '034')
    Unknown18011('bce702bpt', 14179, 13921, 13411, 24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24885, 25398, 24886, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce702bpt', '035')
    Unknown18011('bce701bph', 12643, 12897, 25396, 12849, 12641, 25392, 12337, 12641, 25392, 13874, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25398, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701bph', '036')
    Unknown18011('bce701pyu', 14177, 14179, 13921, 13923, 13921, 13155, 24886, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701pyu', '037')
    Unknown18011('bce700pka', 12897, 25392, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce700pka', '038')
    Unknown18011('bce701pag', 14435, 13921, 13923, 13921, 13923, 13921, 12643, 24889, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701pag', '039')
    Unknown18011('bce701pel', 12641, 14435, 12897, 25401, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12849, 13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701pel', '040')
    Unknown18011('bce700uli', 12643, 12897, 25393, 12595, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce700uli', '041')
    Unknown18011('bce701ume', 13411, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25398, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701ume', '042')
    Unknown18011('bce700uva', 13921, 13923, 14177, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce700uva', '043')
    Unknown18011('bce701ryn', 13923, 13921, 13923, 13921, 13923, 13153, 25400, 24885, 25397, 24885, 25397, 24885, 12594, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701ryn', '044')
    Unknown18011('bce701ahe', 14177, 14179, 14177, 14179, 12641, 25397, 24887, 12593, 14179, 14177, 14179, 12641, 25393, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce701ahe', '045')
    Unknown18011('bce700rne', 13921, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce700rne', '046')
    Unknown18011('bce702rne', 13921, 13923, 13921, 13155, 24881, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce702rne', '047')
    Unknown18011('bce295_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 13665, 12899, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bce295_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bce295_0', '049')
    Unknown30092('bce295_1', '050')
    if SLOT_172:
        Unknown18011('bce600def', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601def', 12643, 12899, 14177, 14179, 14177, 14179, 12643, 24888, 25398, 24881, 25399, 25395, 24884, 25399, 24887, 25399, 24887, 25399, 24883, 25398, 13617, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce602def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24881, 25399, 25394, 24881, 25399, 24887, 25399, 24887, 25399, 25399, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce603def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 13411, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 24886, 25396, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce604def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13411, 14177, 14179, 13153, 13923, 14177, 14179, 14177, 14179, 12641, 13411, 13921, 12643, 14177, 14179, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce605def', 12643, 12643, 14177, 14179, 14177, 13411, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 24882, 25399, 24887, 25399, 25398, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 24882, 25399, 25396, 24881, 25399, 24887, 25399, 24887, 25393, 24882, 25399, 12849, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce700def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24888, 25399, 24887, 25399, 25398, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24882, 25399, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13411, 13665, 12643, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce702def', 12643, 14177, 13923, 13155, 24880, 25399, 24887, 25396, 13105, 14177, 12899, 12899, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24881, 25399, 25394, 24884, 25395, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce703def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 25399, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce704def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 24889, 25399, 24887, 25399, 25398, 24882, 25399, 25398, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 24884, 25399, 24887, 25396, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce705def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 24881, 25399, 24887, 25396, 24882, 25399, 24887, 25399, 25399, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce402_0', 12643, 14177, 14179, 13153, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce402_1', 12643, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 14177, 14179, 14177, 12643, 13411, 13409, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce403_0', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 12899, 13411, 14177, 14179, 14177, 14179, 14433, 13667, 12643, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601brg', 12643, 12643, 14177, 14179, 14177, 13667, 12643, 14177, 13155, 12643, 24881, 25399, 24887, 25395, 24882, 25399, 25398, 24881, 25399, 24887, 25395, 24882, 25399, 24887, 25399, 24887, 25399, 25396, 24881, 25399, 24887, 25399, 24887, 25393, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce600bno', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 14691, 14177, 14179, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601bny', 12643, 12899, 14177, 14179, 12641, 12643, 12897, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 13923, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601bpt', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 13921, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 24882, 25399, 24887, 25399, 25393, 24888, 25399, 25397, 13617, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601bph', 12643, 12899, 14177, 14179, 13665, 12643, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13667, 14177, 14179, 14177, 14179, 13921, 13923, 14177, 14179, 12641, 12643, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce600pyu', 12643, 12643, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 13411, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601pka', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 13409, 13411, 14177, 14179, 14177, 12643, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601pag', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce600pel', 12643, 13411, 14177, 14179, 14177, 13667, 13155, 14177, 14179, 14177, 14179, 14177, 13155, 13411, 24884, 25399, 24886, 25399, 24887, 25399, 24887, 25396, 24881, 25399, 24887, 25399, 24887, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce600uli', 12643, 13155, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 13155, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 14177, 13155, 13411, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 13409, 12899, 14177, 14179, 14689, 14179, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601ume', 12643, 14177, 14179, 14177, 13155, 14177, 14179, 14177, 13667, 12899, 13921, 12643, 12897, 12643, 12897, 12899, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24883, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce600uva', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13923, 14177, 13155, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 24887, 25399, 24887, 25400, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce600ryn', 12643, 13155, 14177, 14179, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce601ahe', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13155, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce602', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 24882, 25399, 24887, 25399, 25393, 24881, 25399, 24887, 25399, 24887, 25394, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce600rne', 12643, 12643, 14177, 12643, 12643, 13409, 13155, 14177, 14179, 14177, 14179, 13665, 14179, 14177, 13155, 12899, 14177, 12899, 13411, 14177, 14179, 14177, 13923, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce700brg', 12643, 12899, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 12899, 12899, 14177, 14179, 12897, 14179, 12641, 13667, 14177, 14179, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701bno', 12643, 14177, 14179, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 14179, 12897, 13667, 14177, 14179, 14177, 14179, 14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701bny', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce702bpt', 12643, 14177, 14179, 13665, 13155, 14177, 14179, 13665, 13155, 14177, 14179, 14177, 13923, 13411, 14177, 14179, 12897, 12643, 13665, 14435, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 12643, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701bph', 12643, 12643, 14177, 14179, 13921, 12899, 14177, 13411, 12643, 14177, 13155, 12899, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 14177, 13923, 12899, 14177, 13667, 13155, 14177, 14179, 14177, 13923, 12643, 14177, 12899, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 13921, 13155, 13153, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701pyu', 12643, 12643, 14177, 14179, 14177, 14179, 13665, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 14179, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce700pka', 12643, 12899, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 12899, 12643, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 24880, 25399, 24887, 25399, 24887, 25393, 14130, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 13923, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701pag', 12643, 12643, 14177, 14179, 14177, 14179, 13409, 12899, 14177, 14179, 14177, 13155, 12899, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701pel', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce700uli', 12643, 12643, 14177, 14179, 12897, 14179, 13921, 13155, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701ume', 12643, 12643, 14177, 14179, 14177, 13411, 13923, 14177, 14179, 14177, 13411, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14177, 13155, 12643, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce700uva', 12643, 12643, 14177, 14179, 14177, 14179, 13665, 12643, 24882, 25399, 25397, 24883, 25399, 24887, 25399, 24887, 25399, 25394, 24885, 25399, 24887, 25394, 24883, 24886, 25396, 12593, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701ryn', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 24883, 25399, 24887, 25399, 24887, 25396, 24882, 25399, 25398, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce701ahe', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce700rne', 12643, 14177, 14179, 14177, 14179, 13153, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 24885, 25399, 24887, 25397, 24885, 25399, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce702rne', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 12897, 14179, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 14179, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce295_0', 12643, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 12641, 12643, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bce295_1', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 13409, 12643, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('6263650000000000000000000000000062726700000000000000000000000000626a6e00000000000000000000000000626e6f00000000000000000000000000'):
        SLOT_171 = 1
    label(0)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    if SLOT_86:
        _gotolabel(482)
    if SLOT_171:
        _gotolabel(1000)
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bno')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('bny')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bpt')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('bph')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('pyu')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('pka')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('pag')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('pel')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uli')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('ume')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('uva')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('ryn')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('ahe')
    if SLOT_ReturnVal:
        _gotolabel(230)
    PartnerChar('rne')
    if SLOT_ReturnVal:
        _gotolabel(240)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(1)
    sprite('ce020_07', 1)
    Unknown3038(1)
    teleportRelativeY(700000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        gotoLabel(1)
    sprite('ce020_07', 2)
    sendToLabelUpon(2, 3)
    Unknown3038(0)
    physicsYImpulse(-40000)
    label(2)
    sprite('ce020_08', 5)
    sprite('ce020_07', 5)
    gotoLabel(2)
    label(3)
    sprite('ce024_00', 3)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 0)
    Unknown8000(0, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 15000)
    GFX_1('ceef_600falleff', -1)
    sprite('ce024_01', 6)
    sprite('ce024_02', 6)
    sprite('ce024_03', 8)
    sprite('ce024_04', 8)
    sprite('ce600_00', 6)
    sprite('ce600_01', 6)
    sprite('ce600_01ex1', 6)
    sprite('ce600_01ex2', 6)
    Unknown7006('bce600def', 100, 912614242, 1701065008, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(4)
    sprite('ce600_01', 1)
    if SLOT_97:
        _gotolabel(4)
    sprite('ce600_01', 15)
    sprite('ce600_02', 8)
    loopRest()
    ExitState()
    label(10)
    sprite('ce601_00', 3)
    callSubroutine('MinervaCall')
    Unknown23029(11, 600, 0)
    if SLOT_17:
        _gotolabel(10)
    sprite('ce601_00', 1)
    if random_(2, 0, 25):
        Unknown2037(1)
        sendToLabel(11)
    else:
        Unknown7006('bce602def', 100, 912614242, 1701065520, 102, 0, 100, 912614242, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0)
    sprite('ce601_00', 70)
    label(11)
    sprite('ce601_00', 30)
    sprite('ce601_01', 6)
    Unknown23029(11, 601, 0)
    sprite('ce601_02', 6)
    sprite('ce601_03', 1)
    if SLOT_2:
        SFX_1('bce604def')
    label(12)
    sprite('ce601_03', 1)
    if SLOT_97:
        _gotolabel(12)
    sprite('ce601_03', 30)
    sprite('ce601_04', 6)
    sprite('ce601_05', 4)
    sprite('ce601_06', 4)
    sprite('ce601_07', 6)
    ExitState()
    label(100)
    sprite('ce000_00', 1)
    if SLOT_158:
        Unknown1000(-1465000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce601brg')

        def upon_CLEAR_OR_EXIT():
            if (not SLOT_97):
                clearUponHandler(3)
                sendToLabel(102)
    label(101)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(101)
    label(102)
    sprite('ce401_00', 5)
    SLOT_4 = 0
    sprite('ce401_01', 5)
    sprite('ce205_00', 5)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 5)
    sprite('ce205_02', 7)
    sprite('ce205_03', 3)
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 4)
    sprite('ce205_03ex02', 4)
    Unknown21011(50)
    label(103)
    sprite('ce205_03ex01', 4)
    sprite('ce205_03ex02', 4)
    gotoLabel(103)
    label(110)
    sprite('ce000_00', 1)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce000_00', 6)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    SFX_1('bce600bno')
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    label(111)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    if SLOT_97:
        _gotolabel(111)
    sprite('ce000_00', 1)
    Unknown21007(24, 40)
    Unknown21011(120)
    label(112)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(112)
    label(120)
    sprite('ce000_00', 1)
    if SLOT_158:
        Unknown1000(-1465000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(121)
    label(122)
    sprite('ce610_00', 8)
    Unknown2005()
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    SFX_1('bce601bny')
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    label(123)
    sprite('ce610_05', 3)
    if SLOT_97:
        _gotolabel(123)
    sprite('ce610_05', 32767)
    Unknown23018(1)
    label(130)
    sprite('ce000_00', 1)
    if (not SLOT_158):
        Unknown1000(-1230000)
    Unknown2005()
    callSubroutine('MinervaCall')
    Unknown23029(11, 610, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(131)
    label(132)
    sprite('ce610_00', 8)
    Unknown2005()
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    SFX_1('bce601bpt')
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    label(133)
    sprite('ce610_05', 3)
    if SLOT_97:
        _gotolabel(133)
    sprite('ce610_05', 10)
    sprite('ce610_05', 32767)
    Unknown21007(24, 40)
    Unknown21011(10)
    label(140)
    sprite('ce656_01', 7)
    Unknown2019(0)
    if SLOT_158:
        Unknown2005()
    else:
        Unknown1000(-1356000)
    sprite('ce656_01', 32767)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce601bph')
        Unknown23018(1)
    label(150)
    sprite('ce000_00', 7)
    Unknown2019(1000)
    Unknown1000(-1150000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    SFX_1('bce600pyu')

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            clearUponHandler(3)
            sendToLabel(152)
    label(151)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    gotoLabel(151)
    label(152)
    sprite('ce401_00', 5)
    SLOT_4 = 0
    sprite('ce401_01', 5)
    sprite('ce205_00', 5)
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 5)
    sprite('ce205_02', 7)
    sprite('ce205_03', 3)
    GFX_0('mv401tameMatome', -1)
    Unknown21007(24, 40)
    Unknown21011(200)
    label(153)
    sprite('ce205_03ex01', 4)
    sprite('ce205_03ex02', 4)
    gotoLabel(153)
    label(160)
    sprite('ce000_00', 1)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce601pka')

        def upon_CLEAR_OR_EXIT():
            if (not SLOT_97):
                clearUponHandler(3)
                sendToLabel(162)
    label(161)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(161)
    label(162)
    sprite('ce217_00', 3)
    Unknown23029(11, 611, 0)
    sprite('ce217_00', 2)
    sprite('ce217_00', 2)
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_04', 5)
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_04', 5)
    Unknown21011(30)
    label(163)
    sprite('ce217_01', 5)
    sprite('ce217_02', 5)
    sprite('ce217_03', 5)
    sprite('ce217_04', 5)
    gotoLabel(163)
    label(170)
    sprite('ce000_00', 1)
    if SLOT_158:
        Unknown2005()
        callSubroutine('MinervaCall')
        Unknown23029(11, 610, 0)
    else:
        callSubroutine('MinervaCall')
        Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(171)
    label(172)
    sprite('ce610_00', 8)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    sprite('ce610_05', 32767)
    SFX_1('bce601pag')
    Unknown23018(1)
    label(180)
    sprite('ce620_02', 5)
    Unknown1000(-1230000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce620_03', 23)
    sprite('ce620_04', 6)
    sprite('ce620_05', 23)
    sprite('ce620_02', 8)
    sprite('ce620_03', 23)
    sprite('ce620_04', 6)
    sprite('ce620_05', 23)
    SFX_1('bce600pel')
    label(181)
    sprite('ce620_05', 1)
    if SLOT_97:
        _gotolabel(181)
    sprite('ce620_05', 30)
    sprite('ce620_05', 32767)
    Unknown21007(24, 40)
    Unknown21011(200)
    loopRest()
    label(190)
    sprite('ce000_00', 1)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    Unknown2037(30)
    sprite('ce000_00', 6)
    sprite('ce000_01', 7)
    SFX_1('bce600uli')
    Unknown23018(1)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
    label(191)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    gotoLabel(191)
    label(200)
    sprite('ce000_00', 1)
    Unknown1000(-1605000)
    Unknown2005()
    callSubroutine('MinervaCall')
    Unknown23029(11, 610, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(201)
    label(202)
    sprite('keep', 1)
    SLOT_4 = 0
    Unknown23076()
    Unknown1084(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(204)
    sprite('ce033_00', 2)
    SFX_3('cese_16')
    sprite('ce033_01', 2)
    physicsXImpulse(-20000)
    sprite('ce033_02', 2)
    teleportRelativeX(-20000)
    Unknown1019(150)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 1)
    Unknown1019(150)
    sprite('ce033_03', 3)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_04', 4)
    Unknown1019(15)
    Unknown8000(100, 1, 1)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_05', 4)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_06', 4)
    Unknown1019(15)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_07', 3)
    physicsXImpulse(0)
    sprite('ce000_00', 1)
    SLOT_4 = 1
    label(203)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(203)
    label(204)
    sprite('ce200_00', 3)
    sprite('ce200_01', 3)
    SFX_1('bce601ume')
    label(205)
    sprite('ce200_02', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_03', 3)
    sprite('ce200_04', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_05', 5)
    if SLOT_97:
        _gotolabel(205)
    sprite('ce200_02', 3)
    SFX_0('003_swing_grap_0_0')
    Unknown23018(1)
    label(206)
    sprite('ce200_03', 3)
    sprite('ce200_04', 3)
    sprite('ce200_05', 5)
    sprite('ce200_02', 3)
    gotoLabel(206)
    label(210)
    sprite('ce601_00', 1)
    if SLOT_158:
        Unknown1000(-1465000)
    if SLOT_17:
        _gotolabel(210)
    sprite('ce601_00', 3)
    Unknown2005()
    callSubroutine('MinervaCall')
    Unknown23029(11, 600, 0)
    SFX_1('bce600uva')
    label(211)
    sprite('ce601_00', 215)
    sprite('ce601_01', 6)
    sprite('ce601_02', 6)
    Unknown23029(11, 601, 0)
    label(212)
    sprite('ce601_03', 1)
    if SLOT_97:
        _gotolabel(212)
    sprite('ce601_03', 32767)
    Unknown21007(24, 40)
    Unknown23018(1)
    label(220)
    sprite('ce620_02', 5)
    Unknown1000(-1230000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce620_03', 1)
    SFX_1('bce600ryn')
    label(221)
    sprite('ce620_03', 1)
    if SLOT_97:
        _gotolabel(221)
    sprite('ce620_03', 20)
    sprite('ce620_03', 32767)
    Unknown21007(24, 40)
    Unknown23018(1)
    loopRest()
    label(230)
    sprite('ce000_00', 1)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce601ahe')
        Unknown23018(1)
    label(231)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(231)
    label(240)
    sprite('ce000_00', 1)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce000_00', 6)
    SFX_1('bce600rne')

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            clearUponHandler(3)
            Unknown21007(24, 40)
            Unknown23018(1)
    label(241)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    gotoLabel(241)
    label(991)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(992)
    label(1000)
    sprite('ce000_00', 7)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 10002):
            sendToLabel(1002)
        if (SLOT_48 == 10004):
            clearUponHandler(43)
            Unknown18008()
    label(1001)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    gotoLabel(1001)
    label(1002)
    sprite('ce603_01', 6)
    sprite('ce603_00', 6)
    SFX_1('bce602')
    label(1003)
    sprite('ce603_00', 6)
    if SLOT_97:
        _gotolabel(1003)
    sprite('ce603_00', 32767)
    Unknown23029(24, 10003, 0)
    Unknown23029(22, 10003, 0)
    Unknown23029(23, 10003, 0)

@State
def CmnActMatchWin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    if SLOT_108:
        _gotolabel(0)
    sprite('keep', 2)

    def upon_CLEAR_OR_EXIT():
        SLOT_58 = 1
        Unknown48('19000000020000003400000018000000020000003a000000')
        if SLOT_52:
            if PartnerChar('brg'):
                if (SLOT_145 <= 500000):
                    clearUponHandler(3)
                    sendToLabel(100)
            if PartnerChar('bno'):
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
            if PartnerChar('bph'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('ume'):
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
            if PartnerChar('ahe'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('pel'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
            if PartnerChar('rne'):
                if (SLOT_145 <= 500000):
                    sendToLabel(240)
                    clearUponHandler(3)
    label(482)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('ce610_00', 8)
    Unknown23029(11, 604, 0)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    if SLOT_158:
        if SLOT_52:
            SFX_1('bce704def')
        elif SLOT_108:
            Unknown7006('bce402_0', 100, 879059810, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bce700def', 100, 929391458, 1701065008, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(1)
    sprite('ce610_05', 3)
    if SLOT_97:
        _gotolabel(1)
    sprite('ce610_05', 3)
    Unknown23018(1)
    sprite('ce610_05', 32767)
    loopRest()
    label(10)
    sprite('keep', 1)
    if SLOT_158:
        Unknown20000(1)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(12)
    sprite('ce030_00', 7)
    Unknown23029(11, 605, 0)
    label(11)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(11)
    label(12)
    physicsXImpulse(0)
    Unknown2019(250)
    Unknown21012('4d696e6572766157696e3032000000000000000000000000000000000000000020000000')
    sprite('ce010_00', 7)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    if SLOT_158:
        if SLOT_52:
            SFX_1('bce705def')
        else:
            Unknown7006('bce702def', 100, 929391458, 1701065520, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ce611_00', 7)
    Unknown23018(1)
    label(13)
    sprite('ce611_01', 8)
    sprite('ce611_02', 8)
    sprite('ce611_03', 21)
    sprite('ce611_01', 8)
    sprite('ce611_04', 8)
    sprite('ce611_05', 21)
    sprite('ce611_04', 8)
    sprite('ce611_01', 40)
    gotoLabel(13)
    label(100)
    Unknown20000(1)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(102)
    sprite('ce030_00', 7)
    Unknown23029(11, 605, 0)
    label(101)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(101)
    label(102)
    physicsXImpulse(0)
    Unknown2019(250)
    Unknown21012('4d696e6572766157696e3032000000000000000000000000000000000000000020000000')
    sprite('ce010_00', 7)
    sprite('ce010_01', 7)
    sprite('ce010_02', 7)
    SFX_1('bce700brg')
    sprite('ce611_00', 7)
    label(103)
    sprite('ce611_01', 8)
    sprite('ce611_02', 8)
    sprite('ce611_03', 21)
    sprite('ce611_01', 8)
    sprite('ce611_04', 8)
    sprite('ce611_05', 21)
    sprite('ce611_04', 8)
    sprite('ce611_01', 40)
    if SLOT_97:
        _gotolabel(103)
    sprite('ce611_01', 1)
    Unknown21007(24, 40)
    Unknown21011(300)
    label(104)
    sprite('ce611_01', 8)
    sprite('ce611_02', 8)
    sprite('ce611_03', 21)
    sprite('ce611_01', 8)
    sprite('ce611_04', 8)
    sprite('ce611_05', 21)
    sprite('ce611_04', 8)
    sprite('ce611_01', 40)
    gotoLabel(104)
    ExitState()
    label(110)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(111)
    label(112)
    sprite('ce610_00', 8)
    Unknown23029(11, 609, 0)
    Unknown2005()
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    sprite('ce610_05', 32767)
    SFX_1('bce701bno')
    Unknown23018(1)
    label(120)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(121)
    sprite('ce000_00', 7)
    sprite('ce601_07', 7)
    sprite('ce601_06', 6)
    sprite('ce601_05', 4)
    sprite('ce601_04', 3)
    sprite('ce601_00', 32767)
    label(121)
    sprite('ce601_00', 32767)
    SFX_1('bce701bny')
    Unknown23018(1)
    label(130)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(131)
    label(132)
    sprite('ce610_00', 8)
    Unknown23029(11, 604, 0)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    sprite('ce610_05', 32767)
    SFX_1('bce702bpt')
    Unknown23018(1)
    label(140)
    sprite('ce000_00', 7)
    if SLOT_158:
        Unknown2019(0)
    else:
        Unknown2019(-500)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    sprite('ce000_00', 7)
    gotoLabel(141)
    label(142)
    sprite('ce656_00', 7)
    sprite('ce656_01', 32767)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce701bph')
        Unknown23018(1)
    Unknown23029(11, 604, 0)
    label(150)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(151)
    label(152)
    sprite('ce030_00', 7)
    Unknown23029(11, 603, 0)
    Unknown20000(1)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(154)
    label(153)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(153)
    label(154)
    sprite('ce615_00', 9)
    clearUponHandler(3)
    physicsXImpulse(0)
    Unknown21012('4d696e65727661526f756e6457696e000000000000000000000000000000000020000000')
    sprite('ce615_01', 9)
    sprite('ce615_02', 9)
    sprite('ce615_03', 6)
    sprite('ce615_04', 6)
    SFX_1('bce701pyu')
    GFX_0('ce615Eff', 0)
    GFX_0('ce615Eff2', -1)
    SFX_3('cese_03')
    Unknown23018(1)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            clearUponHandler(3)
            Unknown21007(24, 40)
    label(155)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    gotoLabel(155)
    label(160)
    sprite('ce030_00', 7)
    Unknown23029(11, 603, 0)
    Unknown20000(1)
    Unknown2013(24)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_145 < 280000):
                Unknown2037(0)
                sendToLabel(162)
    label(161)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(161)
    label(162)
    physicsXImpulse(0)
    Unknown21012('4d696e65727661526f756e6457696e000000000000000000000000000000000020000000')
    sprite('ce615_00', 9)
    sprite('ce615_01', 9)
    sprite('ce615_02', 9)
    sprite('ce615_03', 6)
    sprite('ce615_04', 6)
    SFX_1('bce700pka')
    GFX_0('ce615Eff', 0)
    GFX_0('ce615Eff3', -1)
    SFX_3('cese_03')
    label(163)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    if SLOT_97:
        _gotolabel(163)
    sprite('keep', 1)
    Unknown21007(24, 40)
    Unknown21011(150)
    label(164)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    gotoLabel(164)
    loopRest()
    label(170)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(171)
    label(172)
    sprite('ce610_00', 8)
    Unknown23029(11, 604, 0)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    sprite('ce610_05', 8)
    SFX_1('bce701pag')
    label(173)
    sprite('ce610_05', 1)
    if SLOT_97:
        _gotolabel(173)
    sprite('ce610_05', 32767)
    Unknown23018(1)
    label(180)
    sprite('ce030_00', 7)
    Unknown23029(11, 603, 0)
    Unknown20000(1)
    Unknown2013(24)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_145 < 280000):
                Unknown2037(0)
                sendToLabel(182)
    label(181)
    sprite('ce030_01', 7)
    sprite('ce030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)
    sprite('ce030_04', 7)
    sprite('ce030_05', 7)
    sprite('ce030_06', 7)
    sprite('ce030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)
    sprite('ce030_09', 7)
    sprite('ce030_10', 7)
    loopRest()
    gotoLabel(181)
    label(182)
    physicsXImpulse(0)
    Unknown21012('4d696e65727661526f756e6457696e000000000000000000000000000000000020000000')
    sprite('ce615_00', 9)
    sprite('ce615_01', 9)
    sprite('ce615_02', 9)
    sprite('ce615_03', 6)
    sprite('ce615_04', 6)
    SFX_1('bce700uli')
    GFX_0('ce615Eff', 0)
    GFX_0('ce615Eff3', -1)
    SFX_3('cese_03')
    label(183)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    if SLOT_97:
        _gotolabel(183)
    sprite('keep', 1)
    Unknown21007(24, 40)
    Unknown21011(180)
    label(184)
    sprite('ce615_05', 8)
    sprite('ce615_06', 8)
    sprite('ce615_07', 8)
    gotoLabel(184)
    label(190)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(191)
    label(192)
    sprite('ce200_00', 3)
    sprite('ce200_01', 3)
    SFX_1('bce701ume')
    Unknown23018(1)
    label(193)
    sprite('ce200_02', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_03', 3)
    sprite('ce200_04', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_05', 5)
    gotoLabel(193)
    label(200)
    sprite('ce000_00', 7)
    sprite('ce601_07', 7)
    sprite('ce601_06', 6)
    sprite('ce601_05', 4)
    sprite('ce601_04', 3)
    sprite('ce601_00', 60)
    sprite('ce601_01', 4)
    sprite('ce601_02', 3)
    sprite('ce601_03', 1)
    SFX_1('bce700uva')
    label(201)
    sprite('ce601_03', 1)
    if SLOT_97:
        _gotolabel(201)
    sprite('ce601_03', 30)
    sprite('ce601_03', 32767)
    Unknown21007(24, 40)
    Unknown21011(150)
    label(210)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(211)
    label(212)
    sprite('ce620_02', 5)
    sprite('ce620_03', 32767)
    SFX_1('bce701ryn')
    Unknown23018(1)
    label(220)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(221)
    label(222)
    sprite('ce610_00', 1)
    Unknown23029(11, 609, 0)
    Unknown2005()
    sprite('ce610_00', 7)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_05', 32767)
    SFX_1('bce701ahe')
    Unknown23018(1)
    label(230)
    sprite('ce000_00', 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('ce000_00', 7)
    sprite('ce000_01', 7)
    sprite('ce000_02', 7)
    sprite('ce000_03', 7)
    sprite('ce000_04', 7)
    sprite('ce000_05', 7)
    sprite('ce000_06', 7)
    sprite('ce000_07', 7)
    sprite('ce000_08', 7)
    sprite('ce000_09', 7)
    sprite('ce000_10', 7)
    sprite('ce000_11', 7)
    gotoLabel(231)
    label(232)
    sprite('ce620_02', 5)
    sprite('ce620_03', 23)
    sprite('ce620_04', 6)
    sprite('ce620_05', 23)
    sprite('ce620_02', 8)
    sprite('ce620_03', 32767)
    SFX_1('bce701pel')
    Unknown23018(1)
    label(240)
    sprite('ce610_00', 8)
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    sprite('ce610_01', 8)
    sprite('ce610_02', 8)
    sprite('ce610_03', 8)
    sprite('ce610_04', 8)
    sprite('ce610_05', 8)
    SFX_1('bce700rne')
    label(241)
    sprite('ce610_05', 1)
    if SLOT_97:
        _gotolabel(241)
    sprite('ce610_05', 15)
    sprite('ce610_05', 32767)
    Unknown21007(24, 40)
    label(242)
    sprite('ce620_00', 7)
    sprite('ce620_01', 7)
    sprite('ce620_02', 5)
    SFX_1('bce702rne')
    sprite('ce620_03', 8)
    sprite('ce620_04', 6)
    sprite('ce620_05', 8)
    sprite('ce620_04', 6)
    sprite('ce620_03', 8)
    sprite('ce620_02', 8)
    sprite('ce620_02', 32767)
    Unknown23018(1)

@State
def CmnActLose():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        Unknown23029(11, 606, 0)
    sprite('ce620_00', 7)
    sprite('ce620_01', 7)
    sprite('ce620_02', 5)
    sprite('ce620_03', 8)
    sprite('ce620_04', 6)
    sprite('ce620_05', 8)
    sprite('ce620_02', 8)
    sprite('ce620_03', 8)
    sprite('ce620_01', 20)
    sprite('ce620_06', 8)
    Unknown7006('bce403_0', 100, 879059810, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ce620_07', 8)
    label(0)
    sprite('ce620_08', 3)
    if SLOT_97:
        _gotolabel(0)
    sprite('ce620_08', 32767)
    Unknown21011(30)