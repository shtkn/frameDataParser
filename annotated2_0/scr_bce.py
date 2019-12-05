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
    sprite('ce000_00', 7)	# 1-7
    sprite('ce000_01', 7)	# 8-14
    sprite('ce000_02', 7)	# 15-21
    sprite('ce000_03', 7)	# 22-28
    sprite('ce000_04', 7)	# 29-35
    sprite('ce000_05', 7)	# 36-42
    sprite('ce000_06', 7)	# 43-49
    sprite('ce000_07', 7)	# 50-56
    sprite('ce000_08', 7)	# 57-63
    sprite('ce000_09', 7)	# 64-70
    sprite('ce000_10', 7)	# 71-77
    sprite('ce000_11', 7)	# 78-84
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('ce001_00', 6)	# 85-90
    SLOT_62 = 1
    Unknown23029(11, 112, 0)
    SLOT_88 = 960
    SFX_1('bce000')
    sprite('ce001_01', 6)	# 91-96
    sprite('ce001_02', 6)	# 97-102
    sprite('ce001_03', 6)	# 103-108
    sprite('ce001_04', 6)	# 109-114
    sprite('ce001_05', 6)	# 115-120
    label(9)
    sprite('ce001_06', 8)	# 121-128
    sprite('ce001_06ex00', 8)	# 129-136
    sprite('ce001_06ex01', 29)	# 137-165
    sprite('ce001_06', 8)	# 166-173
    sprite('ce001_06ex02', 8)	# 174-181
    sprite('ce001_06ex03', 29)	# 182-210
    gotoLabel(9)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('ce603_01', 6)	# 211-216
    SLOT_88 = 960
    sprite('ce603_00', 90)	# 217-306
    sprite('ce603_01', 6)	# 307-312
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        Unknown23029(11, 101, 0)
    sprite('ce003_00', 3)	# 1-3
    sprite('ce003_01', 3)	# 4-6
    sprite('ce003_00ex', 3)	# 7-9

@State
def CmnActStand2Crouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_00', 4)	# 1-4
    sprite('ce010_01', 4)	# 5-8

@State
def CmnActCrouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    label(0)
    sprite('ce010_02', 6)	# 1-6
    sprite('ce010_03', 6)	# 7-12
    sprite('ce010_04', 6)	# 13-18
    sprite('ce010_05', 6)	# 19-24
    sprite('ce010_06', 6)	# 25-30
    sprite('ce010_07', 6)	# 31-36
    sprite('ce010_08', 6)	# 37-42
    sprite('ce010_09', 6)	# 43-48
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        Unknown23029(11, 101, 0)
    sprite('ce013_00', 3)	# 1-3
    sprite('ce013_01', 3)	# 4-6
    sprite('ce013_00ex', 3)	# 7-9

@State
def CmnActCrouch2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    sprite('ce010_01', 4)	# 1-4
    sprite('ce010_00', 4)	# 5-8

@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
        if SLOT_37:
            if SLOT_93:
                if SLOT_16:
                    Unknown1045(15000)
    sprite('ce023_00', 2)	# 1-2
    sprite('ce023_01', 2)	# 3-4

@State
def CmnActJumpUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce020_00', 4)	# 1-4
    sprite('ce020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce020_02', 3)	# 1-3
    sprite('ce020_03', 3)	# 4-6
    sprite('ce020_04', 3)	# 7-9

@State
def CmnActJumpDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce020_05', 3)	# 1-3
    sprite('ce020_06', 3)	# 4-6
    label(0)
    sprite('ce020_07', 4)	# 7-10
    sprite('ce020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_01', 3)	# 1-3
    sprite('ce024_02', 4)	# 4-7
    sprite('ce024_03', 5)	# 8-12
    sprite('ce024_04', 3)	# 13-15
    sprite('ce024_05', 3)	# 16-18

@State
def CmnActLandingStiffLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_00', 2)	# 1-2
    sprite('ce024_01', 2)	# 3-4
    sprite('ce024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_03', 3)	# 1-3
    sprite('ce024_04', 3)	# 4-6
    sprite('ce024_05', 3)	# 7-9

@State
def CmnActFWalk():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')

        def upon_17():
            Unknown23029(11, 102, 0)

        def upon_STATE_END():
            Unknown23029(11, 100, 0)
    sprite('ce030_00', 7)	# 1-7
    label(0)
    sprite('ce030_01', 7)	# 8-14
    sprite('ce030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)	# 22-28
    sprite('ce030_04', 7)	# 29-35
    sprite('ce030_05', 7)	# 36-42
    sprite('ce030_06', 7)	# 43-49
    sprite('ce030_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)	# 57-63
    sprite('ce030_09', 7)	# 64-70
    sprite('ce030_10', 7)	# 71-77
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
    sprite('ce030_00ex', 7)	# 1-7
    label(0)
    sprite('ce030_01ex', 7)	# 8-14
    sprite('ce030_02ex', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03ex', 7)	# 22-28
    sprite('ce030_04ex', 7)	# 29-35
    sprite('ce030_05ex', 7)	# 36-42
    sprite('ce030_06ex', 7)	# 43-49
    sprite('ce030_07ex', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08ex', 7)	# 57-63
    sprite('ce030_09ex', 7)	# 64-70
    sprite('ce030_10ex', 7)	# 71-77
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
    sprite('ce032_00', 3)	# 1-3
    label(0)
    sprite('ce032_01', 4)	# 4-7
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    sprite('ce032_02', 4)	# 8-11
    SFX_3('cese_04')
    sprite('ce032_03', 4)	# 12-15
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
    sprite('ce032_04', 3)	# 1-3
    sprite('ce032_05', 3)	# 4-6
    sprite('ce032_06', 3)	# 7-9
    sprite('ce032_07', 3)	# 10-12

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
    sprite('ce033_00', 2)	# 1-2
    SFX_3('cese_16')
    sprite('ce033_01', 2)	# 3-4
    physicsXImpulse(-20000)
    sprite('ce033_02', 2)	# 5-6
    teleportRelativeX(-20000)
    Unknown1019(150)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 1)	# 7-7
    Unknown1019(150)
    sprite('ce033_03', 3)	# 8-10
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_04', 4)	# 11-14
    Unknown1019(15)
    Unknown8000(100, 1, 1)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_05', 4)	# 15-18
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_06', 4)	# 19-22
    Unknown1019(15)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_07', 3)	# 23-25
    physicsXImpulse(0)

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce035_00', 3)	# 1-3
    label(0)
    sprite('ce035_01', 3)	# 4-6
    GFX_0('ceAirDashEff', 0)
    GFX_0('ceAirDashEff', 1)
    GFX_0('ceAirDashEff', 2)
    sprite('ce035_02', 3)	# 7-9
    sprite('ce035_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce036_00', 3)	# 1-3
    label(0)
    sprite('ce036_01', 3)	# 4-6
    GFX_0('ceAirBDashEff', 0)
    GFX_0('ceAirBDashEff', 1)
    GFX_0('ceAirDashEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    sprite('ce036_02', 3)	# 7-9
    sprite('ce036_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_00', 1)	# 1-1
    sprite('ce050_01', 1)	# 2-2
    sprite('ce050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_01', 1)	# 1-1
    sprite('ce050_02', 1)	# 2-2
    sprite('ce050_01', 2)	# 3-4
    sprite('ce050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_02', 1)	# 1-1
    sprite('ce050_03', 1)	# 2-2
    sprite('ce050_02', 2)	# 3-4
    sprite('ce050_01', 2)	# 5-6
    sprite('ce050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_03', 1)	# 1-1
    sprite('ce050_04', 1)	# 2-2
    sprite('ce050_03', 2)	# 3-4
    sprite('ce050_02', 2)	# 5-6
    sprite('ce050_01', 2)	# 7-8
    sprite('ce050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce050_04', 1)	# 1-1
    sprite('ce050_04', 1)	# 2-2
    sprite('ce050_04', 2)	# 3-4
    sprite('ce050_03', 2)	# 5-6
    sprite('ce050_02', 2)	# 7-8
    sprite('ce050_01', 2)	# 9-10
    sprite('ce050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_00', 1)	# 1-1
    sprite('ce052_01', 1)	# 2-2
    sprite('ce052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_01', 1)	# 1-1
    sprite('ce052_02', 1)	# 2-2
    sprite('ce052_01', 2)	# 3-4
    sprite('ce052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_02', 1)	# 1-1
    sprite('ce052_03', 1)	# 2-2
    sprite('ce052_02', 2)	# 3-4
    sprite('ce052_01', 2)	# 5-6
    sprite('ce052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_03', 1)	# 1-1
    sprite('ce052_04', 1)	# 2-2
    sprite('ce052_03', 2)	# 3-4
    sprite('ce052_02', 2)	# 5-6
    sprite('ce052_01', 2)	# 7-8
    sprite('ce052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce052_04', 1)	# 1-1
    sprite('ce052_04', 1)	# 2-2
    sprite('ce052_04', 2)	# 3-4
    sprite('ce052_03', 2)	# 5-6
    sprite('ce052_02', 2)	# 7-8
    sprite('ce052_01', 2)	# 9-10
    sprite('ce052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_00', 1)	# 1-1
    sprite('ce054_01', 1)	# 2-2
    sprite('ce054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_01', 1)	# 1-1
    sprite('ce054_02', 1)	# 2-2
    sprite('ce054_01', 2)	# 3-4
    sprite('ce054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_02', 1)	# 1-1
    sprite('ce054_03', 1)	# 2-2
    sprite('ce054_02', 2)	# 3-4
    sprite('ce054_01', 2)	# 5-6
    sprite('ce054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_03', 1)	# 1-1
    sprite('ce054_04', 1)	# 2-2
    sprite('ce054_03', 2)	# 3-4
    sprite('ce054_02', 2)	# 5-6
    sprite('ce054_01', 2)	# 7-8
    sprite('ce054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce054_04', 1)	# 1-1
    sprite('ce054_04', 1)	# 2-2
    sprite('ce054_04', 2)	# 3-4
    sprite('ce054_03', 2)	# 5-6
    sprite('ce054_02', 2)	# 7-8
    sprite('ce054_01', 2)	# 9-10
    sprite('ce054_00', 2)	# 11-12

@State
def CmnActBDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce060_00', 4)	# 1-4
    label(0)
    sprite('ce060_01', 4)	# 5-8
    sprite('ce060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_03', 3)	# 1-3
    sprite('ce062_04', 3)	# 4-6

@State
def CmnActBDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_05', 3)	# 1-3
    sprite('ce062_06', 3)	# 4-6
    label(0)
    sprite('ce062_07', 3)	# 7-9
    sprite('ce062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_04', 3)	# 1-3
    sprite('ce063_05', 3)	# 4-6

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

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_01', 3)	# 1-3

@State
def CmnActFDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce063_02', 3)	# 1-3
    sprite('ce063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_04', 3)	# 1-3
    sprite('ce063_05', 3)	# 4-6

@State
def CmnActFDownBound():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_06', 2)	# 1-2
    sprite('ce063_07', 2)	# 3-4
    sprite('ce063_08', 3)	# 5-7
    sprite('ce063_09', 3)	# 8-10
    sprite('ce063_10', 3)	# 11-13

@State
def CmnActFDownLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce064_00', 2)	# 1-2
    sprite('ce064_01', 2)	# 3-4
    sprite('ce064_02', 2)	# 5-6
    sprite('ce064_03', 2)	# 7-8
    sprite('ce064_04', 2)	# 9-10
    sprite('ce064_05', 2)	# 11-12
    sprite('ce064_06', 2)	# 13-14
    sprite('ce064_07', 2)	# 15-16
    sprite('ce064_08', 3)	# 17-19
    sprite('ce064_09', 3)	# 20-22

@State
def CmnActVDownUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_00', 3)	# 1-3
    label(0)
    sprite('ce062_01', 3)	# 4-6
    sprite('ce062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_03', 3)	# 1-3
    sprite('ce062_04', 3)	# 4-6

@State
def CmnActVDownDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_05', 3)	# 1-3
    sprite('ce062_06', 3)	# 4-6
    label(0)
    sprite('ce062_07', 3)	# 7-9
    sprite('ce062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce062_09', 2)	# 1-2
    sprite('ce062_10', 2)	# 3-4

@State
def CmnActBlowoff():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce072_00', 5)	# 1-5
    sprite('ce072_01', 3)	# 6-8
    sprite('ce072_02', 3)	# 9-11
    label(0)
    sprite('ce072_01', 3)	# 12-14
    sprite('ce072_02', 3)	# 15-17
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce074_00', 3)	# 1-3
    sprite('ce074_01', 3)	# 4-6
    sprite('ce074_02', 3)	# 7-9
    sprite('ce074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('null', 60)	# 1-60

@State
def CmnActFreeze():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce071_04', 1)	# 1-1

@State
def CmnActWallBound():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce073_00', 3)	# 1-3
    sprite('ce073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce073_02', 3)	# 1-3
    label(0)
    sprite('ce073_03', 3)	# 4-6
    sprite('ce073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_00', 3)	# 1-3
    sprite('ce070_01', 3)	# 4-6
    label(0)
    sprite('ce070_02', 3)	# 7-9
    sprite('ce070_03', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActStaggerDown():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_04', 4)	# 1-4
    sprite('ce070_05', 4)	# 5-8
    sprite('ce070_06', 4)	# 9-12
    sprite('ce070_07', 4)	# 13-16
    sprite('ce070_08', 4)	# 17-20
    sprite('ce070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce070_10', 1)	# 1-1
    sprite('ce070_11', 2)	# 2-3
    sprite('ce070_12', 3)	# 4-6
    sprite('ce070_13', 3)	# 7-9

@State
def CmnActUkemiAirF():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)	# 1-3
    sprite('ce113_01', 3)	# 4-6
    sprite('ce113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)	# 1-3
    sprite('ce113_01', 3)	# 4-6
    sprite('ce113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce113_00', 3)	# 1-3
    sprite('ce113_01', 3)	# 4-6
    sprite('ce113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce110_00', 2)	# 1-2
    sprite('ce110_01', 2)	# 3-4
    sprite('ce110_02', 2)	# 5-6
    sprite('ce110_03', 2)	# 7-8
    sprite('ce110_04', 2)	# 9-10
    sprite('ce110_05', 2)	# 11-12
    sprite('ce110_06', 2)	# 13-14
    sprite('ce110_07', 200)	# 15-214
    sprite('ce110_08', 3)	# 215-217
    sprite('ce110_09', 3)	# 218-220

@State
def CmnActUkemiLandB():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce111_00', 3)	# 1-3
    sprite('ce111_01', 3)	# 4-6
    sprite('ce111_02', 3)	# 7-9
    sprite('ce111_03', 3)	# 10-12
    sprite('ce111_04', 3)	# 13-15
    sprite('ce111_06', 3)	# 16-18
    sprite('ce111_07', 200)	# 19-218
    sprite('ce111_08', 3)	# 219-221
    sprite('ce111_09', 3)	# 222-224

@State
def CmnActUkemiLandN():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce112_00', 2)	# 1-2
    sprite('ce112_01', 2)	# 3-4
    sprite('ce112_02', 2)	# 5-6
    sprite('ce112_03', 2)	# 7-8
    sprite('ce112_04', 2)	# 9-10
    sprite('ce112_05', 2)	# 11-12
    sprite('ce112_06', 2)	# 13-14
    sprite('ce112_07', 2)	# 15-16
    sprite('ce112_08', 2)	# 17-18

@State
def CmnActUkemiLandNLanding():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce024_00', 3)	# 1-3
    sprite('ce024_01', 3)	# 4-6
    sprite('ce024_02', 3)	# 7-9
    sprite('ce024_03', 3)	# 10-12
    sprite('ce024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_00', 3)	# 1-3	 **attackbox here**
    sprite('ce040_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce040_02', 3)	# 1-3	 **attackbox here**
    sprite('ce040_03', 3)	# 4-6	 **attackbox here**
    sprite('ce040_04', 3)	# 7-9	 **attackbox here**
    gotoLabel(0)

@State
def CmnActMidGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_01', 3)	# 1-3	 **attackbox here**
    sprite('ce040_00', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_05', 3)	# 1-3	 **attackbox here**
    label(0)
    sprite('ce040_02', 3)	# 4-6	 **attackbox here**
    sprite('ce040_03', 3)	# 7-9	 **attackbox here**
    sprite('ce040_04', 3)	# 10-12	 **attackbox here**
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_01', 3)	# 1-3	 **attackbox here**
    sprite('ce040_00', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_00', 3)	# 1-3
    sprite('ce041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce041_02', 3)	# 1-3
    sprite('ce041_03', 3)	# 4-6
    sprite('ce041_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_01', 3)	# 1-3
    sprite('ce041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_05', 3)	# 1-3
    label(0)
    sprite('ce041_02', 3)	# 4-6
    sprite('ce041_03', 3)	# 7-9
    sprite('ce041_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce041_01', 3)	# 1-3
    sprite('ce041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_00', 3)	# 1-3
    sprite('ce043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce043_02', 3)	# 1-3
    sprite('ce043_03', 3)	# 4-6
    sprite('ce043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_01', 3)	# 1-3
    sprite('ce043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_05', 3)	# 1-3
    label(0)
    sprite('ce043_02', 3)	# 4-6
    sprite('ce043_03', 3)	# 7-9
    sprite('ce043_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce043_01', 3)	# 1-3
    sprite('ce043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_00', 3)	# 1-3
    sprite('ce045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce045_02', 3)	# 1-3
    sprite('ce045_03', 3)	# 4-6
    sprite('ce045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_01', 3)	# 1-3
    sprite('ce045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_05', 3)	# 1-3
    label(0)
    sprite('ce045_02', 3)	# 4-6
    sprite('ce045_03', 3)	# 7-9
    sprite('ce045_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce045_01', 3)	# 1-3
    sprite('ce045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce090_00', 2)	# 1-2
    sprite('ce090_01', 2)	# 3-4
    sprite('ce090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ce090_03', 6)	# 6-11
    sprite('ce090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce091_00', 2)	# 1-2
    sprite('ce091_01', 2)	# 3-4
    sprite('ce091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ce091_03', 6)	# 6-11
    sprite('ce091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce092_00', 2)	# 1-2
    sprite('ce092_01', 2)	# 3-4
    sprite('ce092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ce092_03', 6)	# 6-11
    sprite('ce092_04', 6)	# 12-17

@State
def CmnActAirTurn():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce025_00', 3)	# 1-3
    sprite('ce025_01', 3)	# 4-6
    sprite('ce025_00ex', 3)	# 7-9

@State
def CmnActLockWait():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce040_02', 1)	# 1-1	 **attackbox here**
    sprite('ce040_01', 3)	# 2-4	 **attackbox here**
    sprite('ce040_00', 3)	# 5-7	 **attackbox here**

@State
def CmnActLockReject():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce312_00', 7)	# 1-7	 **attackbox here**
    sprite('ce312_01', 7)	# 8-14	 **attackbox here**
    sprite('ce312_02', 2)	# 15-16	 **attackbox here**
    sprite('ce312_03', 2)	# 17-18	 **attackbox here**
    sprite('ce312_04', 3)	# 19-21	 **attackbox here**
    sprite('ce312_05', 3)	# 22-24	 **attackbox here**
    sprite('ce312_06', 3)	# 25-27	 **attackbox here**
    sprite('ce312_07', 3)	# 28-30	 **attackbox here**

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

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce071_02', 2)	# 1-2
    sprite('ce071_03', 2)	# 3-4
    sprite('ce071_04', 2)	# 5-6
    sprite('ce071_05', 2)	# 7-8
    sprite('ce071_06', 2)	# 9-10
    sprite('ce071_07', 2)	# 11-12
    sprite('ce071_08', 2)	# 13-14
    sprite('ce071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    label(0)
    sprite('ce077_00', 2)	# 1-2
    sprite('ce077_01', 2)	# 3-4
    sprite('ce077_00ex01', 2)	# 5-6
    sprite('ce077_01ex01', 2)	# 7-8
    sprite('ce077_00ex02', 2)	# 9-10
    sprite('ce077_01ex02', 2)	# 11-12
    sprite('ce077_00ex03', 2)	# 13-14
    sprite('ce077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce077_02', 4)	# 1-4
    label(0)
    sprite('ce077_03', 3)	# 5-7
    sprite('ce077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce077_05', 5)	# 1-5
    sprite('ce077_06', 4)	# 6-9

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

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_00', 3)	# 1-3
    sprite('ce333_01', 3)	# 4-6
    sprite('ce333_02', 3)	# 7-9
    sprite('ce333_03', 32767)	# 10-32776
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActOverDriveLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_04', 3)	# 1-3
    label(0)
    sprite('ce333_05', 3)	# 4-6
    sprite('ce333_06', 3)	# 7-9
    sprite('ce333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_08', 6)	# 1-6
    sprite('ce333_09', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_10', 3)	# 1-3
    sprite('ce333_11', 3)	# 4-6
    sprite('ce333_12', 3)	# 7-9
    sprite('ce333_13', 32767)	# 10-32776
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActAirOverDriveLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_14', 3)	# 1-3
    label(0)
    sprite('ce333_05', 3)	# 4-6
    sprite('ce333_06', 3)	# 7-9
    sprite('ce333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_15', 3)	# 1-3
    sprite('ce333_16', 3)	# 4-6
    sprite('ce020_05', 3)	# 7-9
    sprite('ce020_06', 3)	# 10-12
    label(0)
    sprite('ce020_07', 4)	# 13-16
    sprite('ce020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_00', 3)	# 1-3
    sprite('ce333_01', 3)	# 4-6
    sprite('ce333_02', 3)	# 7-9
    sprite('ce333_03', 32767)	# 10-32776
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActCrossRushLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_04', 3)	# 1-3
    label(0)
    sprite('ce333_05', 3)	# 4-6
    sprite('ce333_06', 3)	# 7-9
    sprite('ce333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_08', 6)	# 1-6
    sprite('ce333_09', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_10', 3)	# 1-3
    sprite('ce333_11', 3)	# 4-6
    sprite('ce333_12', 3)	# 7-9
    sprite('ce333_13', 32767)	# 10-32776
    GFX_0('EMB_CE_OD', 0)
    loopRest()

@State
def CmnActAirCrossRushLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_14', 3)	# 1-3
    label(0)
    sprite('ce333_05', 3)	# 4-6
    sprite('ce333_06', 3)	# 7-9
    sprite('ce333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce333_15', 3)	# 1-3
    sprite('ce333_16', 3)	# 4-6
    sprite('ce020_05', 3)	# 7-9
    sprite('ce020_06', 3)	# 10-12
    label(0)
    sprite('ce020_07', 4)	# 13-16
    sprite('ce020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_00', 2)	# 1-2
    sprite('ce331_01', 2)	# 3-4
    label(0)
    sprite('ce331_02', 3)	# 5-7
    sprite('ce331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_04', 2)	# 1-2
    sprite('ce331_05', 2)	# 3-4
    label(0)
    sprite('ce331_06', 3)	# 5-7
    sprite('ce331_07', 3)	# 8-10
    sprite('ce331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_09', 3)	# 1-3
    sprite('ce331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_11', 2)	# 1-2
    sprite('ce331_12', 2)	# 3-4
    label(0)
    sprite('ce331_02', 3)	# 5-7
    sprite('ce331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_04', 2)	# 1-2
    sprite('ce331_05', 2)	# 3-4
    label(0)
    sprite('ce331_06', 3)	# 5-7
    sprite('ce331_07', 3)	# 8-10
    sprite('ce331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():

    def upon_IMMEDIATE():
        callSubroutine('MinervaNoneCall')
    sprite('ce331_13', 3)	# 1-3
    sprite('ce331_14', 3)	# 4-6
    sprite('ce020_05', 3)	# 7-9
    sprite('ce020_06', 3)	# 10-12
    label(0)
    sprite('ce020_07', 4)	# 13-16
    sprite('ce020_08', 4)	# 17-20
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
        DisableAttackRestOfMove()
        Unknown11050('020000006365343034537461724566660000000000000000000000000000000000000000')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 28)	# 603-630
    sprite('null', 1)	# 631-631
    Unknown1086(22)
    teleportRelativeX(-180000)
    teleportRelativeX(-800000)
    teleportRelativeY(1800000)
    physicsXImpulse(160000)
    physicsYImpulse(-360000)
    callSubroutine('MinervaCallAttack')
    Unknown23029(11, 252, 0)
sprite('ce404_04', 2)	# 632-633
sprite('ce404_05', 3)	# 634-636	 **attackbox here**
GFX_0('ce404KickEff', 100)
sprite('ce404_06', 3)	# 637-639	 **attackbox here**
label(0)
sprite('ce404_05', 3)	# 640-642	 **attackbox here**
sprite('ce404_06', 3)	# 643-645	 **attackbox here**
gotoLabel(0)
label(9)
sprite('keep', 3)	# 646-648
Unknown1019(30)
sprite('ce404_07', 3)	# 649-651
Unknown21012('63653430344b69636b456666000000000000000000000000000000000000000020000000')
clearUponHandler(2)
Unknown21007(11, 32)
Unknown1084(1)
sprite('ce404_08', 6)	# 652-657
sprite('ce404_09', 6)	# 658-663
sprite('ce404_10', 4)	# 664-667
sprite('ce404_11', 3)	# 668-670
endState()

@State
def CmnActChangePartnerQuickIn():
    sprite('ce032_01', 3)	# 1-3
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    sprite('ce032_02', 3)	# 4-6
    sprite('ce032_03', 3)	# 7-9
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    sprite('ce032_04', 5)	# 10-14
    sprite('ce032_05', 5)	# 15-19
    sprite('ce032_06', 5)	# 20-24
    sprite('ce032_07', 5)	# 25-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ce033_01', 3)	# 1-3
    physicsYImpulse(0)
    setGravity(0)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 3)	# 4-6
    sprite('ce033_03', 3)	# 7-9
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_01', 3)	# 10-12
    sprite('ce033_02', 3)	# 13-15
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_03', 3)	# 16-18
    sprite('ce033_01', 3)	# 19-21
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 3)	# 22-24
    sprite('ce033_03', 3)	# 25-27
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_01', 3)	# 28-30
    sprite('keep', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ce033_00', 2)	# 1-2
    sprite('ce033_01', 2)	# 3-4
    sprite('ce033_02', 2)	# 5-6
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    callSubroutine('RCEffCheck')
    sprite('ce033_03', 3)	# 7-9
    label(0)
    sprite('ce033_01', 2)	# 10-11
    sprite('ce033_02', 2)	# 12-13
    sprite('ce033_03', 2)	# 14-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce033_04', 2)	# 16-17
    sprite('ce033_05', 2)	# 18-19
    sprite('ce033_06', 2)	# 20-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
        callSubroutine('MinervaCall')
    sprite('ce620_00', 4)	# 1-4
    Unknown23029(11, 604, 0)
    sprite('ce620_01', 4)	# 5-8
    sprite('ce620_02', 8)	# 9-16
    sprite('ce620_03', 12)	# 17-28
    sprite('ce620_04', 8)	# 29-36
    sprite('ce620_05', 12)	# 37-48
    sprite('ce620_02', 8)	# 49-56
    sprite('ce620_03', 12)	# 57-68
    sprite('ce001_00', 4)	# 69-72
    sprite('ce000_00', 4)	# 73-76
    sprite('ce000_00', 30)	# 77-106
    loopRest()

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
    sprite('ce020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ce020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ce024_01', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 403, 0)
        Unknown4020(11)
    sprite('ce610_00', 3)	# 1-3
    sprite('ce610_01', 3)	# 4-6
    sprite('ce610_02', 3)	# 7-9
    sprite('ce610_03', 3)	# 10-12
    tag_voice(1, 'bce104_0', 'bce104_1', 'bce104_2', '')
    sprite('ce610_04', 3)	# 13-15
    sprite('ce610_05', 12)	# 16-27
    sprite('ce610_02', 6)	# 28-33
    sprite('ce610_01', 6)	# 34-39
    sprite('ce610_00', 6)	# 40-45
    sprite('ce000_00', 5)	# 46-50
    sprite('ce208_00', 5)	# 51-55
    sprite('ce208_01', 5)	# 56-60
    sprite('ce208_02', 5)	# 61-65
    sprite('ce208_03', 5)	# 66-70
    sprite('ce208_04', 5)	# 71-75
    sprite('ce208_01', 5)	# 76-80
    sprite('ce208_02', 5)	# 81-85
    sprite('ce208_03', 5)	# 86-90
    sprite('ce208_01', 5)	# 91-95
    sprite('ce208_00', 5)	# 96-100

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
    sprite('ce432_00', 6)	# 1-6
    Unknown23029(11, 100, 0)
    sprite('ce432_01', 6)	# 7-12
    sprite('ce432_04', 6)	# 13-18
    tag_voice(1, 'bce109_0', 'bce109_1', 'bce109_2', '')
    sprite('ce432_05', 6)	# 19-24
    sprite('ce432_06', 6)	# 25-30
    sprite('ce432_07', 6)	# 31-36
    sprite('ce432_08', 6)	# 37-42
    sprite('ce432_09', 3)	# 43-45
    Unknown23029(11, 404, 0)
    sprite('ce432_09', 3)	# 46-48
    GFX_0('SuperHealEff', -1)
    sprite('ce432_10', 6)	# 49-54
    Unknown30078(200)
    Unknown21000(50)
    if (not Unknown48('1900000002000000000000001800000002000000aa000000')):
        Unknown36(24)
        Unknown30078(200)
        Unknown21000(50)
        Unknown35()
    sprite('ce432_11', 5)	# 55-59
    sprite('keep', 1)	# 60-60
    Unknown2037(1)
    label(0)
    sprite('ce432_09', 6)	# 61-66
    SLOT_53 = (SLOT_53 + 500)
    sprite('ce432_10', 6)	# 67-72
    sprite('ce432_11', 5)	# 73-77
    sprite('keep', 1)	# 78-78
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 < 0):
        SLOT_54 = 0
    loopRest()
    if SLOT_IsInOverdrive2:
        _gotolabel(0)
    label(1)
    sprite('ce432_12', 6)	# 79-84
    Unknown21012('53757065724865616c456666000000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_13', 6)	# 85-90
    sprite('ce432_14', 6)	# 91-96
    sprite('ce432_15', 6)	# 97-102

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
    sprite('ce260_00', 2)	# 1-2
    sprite('ce214_00', 3)	# 3-5
    physicsXImpulse(10000)
    sprite('ce214_01', 3)	# 6-8
    Unknown1019(500)
    sprite('ce214_02', 2)	# 9-10
    sprite('ce214_03', 2)	# 11-12	 **attackbox here**
    StartMultihit()
    Unknown1019(50)
    Unknown7009(4)
    sprite('ce214_04', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    Unknown1019(50)
    GFX_0('mv214Eff', -1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_18')
    sprite('ce214_05', 2)	# 16-17	 **attackbox here**
    Recovery()
    Unknown1019(75)
    sprite('ce214_06', 2)	# 18-19
    Unknown1019(75)
    sprite('ce214_07', 2)	# 20-21
    Unknown1019(75)
    sprite('ce214_08', 2)	# 22-23
    Unknown1084(1)
    sprite('ce260_00', 3)	# 24-26
    sprite('ce260_01', 3)	# 27-29
    sprite('ce260_02', 3)	# 30-32
    sprite('ce260_03', 3)	# 33-35
    sprite('ce260_04', 3)	# 36-38
    sprite('ce260_05', 3)	# 39-41

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
    Unknown2036(95, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-400000)
    Unknown1019(4)
    label(0)
    sprite('ce020_07', 3)	# 3-5
    sprite('ce020_08', 3)	# 6-8
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
    sprite('ce208_00', 5)	# 1-5
    sprite('ce208_01', 5)	# 6-10
    sprite('ce208_02', 5)	# 11-15
    sprite('ce208_03', 5)	# 16-20
    sprite('ce208_04', 5)	# 21-25
    sprite('ce208_01', 5)	# 26-30
    sprite('ce208_02', 5)	# 31-35
    sprite('ce208_03', 5)	# 36-40
    sprite('ce208_04', 5)	# 41-45
    sprite('ce208_01', 5)	# 46-50
    sprite('ce208_02', 1)	# 51-51
    sprite('ce208_02', 4)	# 52-55
    sprite('ce208_00', 5)	# 56-60
    sprite('ce207_00', 5)	# 61-65
    sprite('ce207_01', 5)	# 66-70
    sprite('ce207_02', 5)	# 71-75
    sprite('ce207_03', 5)	# 76-80
    setInvincible(0)
    sprite('ce207_04', 5)	# 81-85
    label(0)
    sprite('ce207_01', 5)	# 86-90
    sprite('ce207_02', 5)	# 91-95
    sprite('ce207_03', 5)	# 96-100
    sprite('ce207_04', 5)	# 101-105
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)	# 106-110
    sprite('ce207_02', 5)	# 111-115
    sprite('ce207_00', 5)	# 116-120

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
    sprite('ce208_00', 5)	# 1-5
    sprite('ce208_01', 5)	# 6-10
    sprite('ce208_02', 5)	# 11-15
    sprite('ce208_03', 5)	# 16-20
    sprite('ce208_04', 5)	# 21-25
    sprite('ce208_01', 5)	# 26-30
    sprite('ce208_02', 5)	# 31-35
    sprite('ce208_03', 5)	# 36-40
    sprite('ce208_04', 5)	# 41-45
    sprite('ce208_01', 5)	# 46-50
    sprite('ce208_02', 1)	# 51-51
    sprite('ce208_02', 4)	# 52-55
    sprite('ce208_00', 5)	# 56-60
    sprite('ce207_00', 5)	# 61-65
    sprite('ce207_01', 5)	# 66-70
    sprite('ce207_02', 5)	# 71-75
    sprite('ce207_03', 5)	# 76-80
    setInvincible(0)
    sprite('ce207_04', 5)	# 81-85
    label(0)
    sprite('ce207_01', 5)	# 86-90
    sprite('ce207_02', 5)	# 91-95
    sprite('ce207_03', 5)	# 96-100
    sprite('ce207_04', 5)	# 101-105
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)	# 106-110
    sprite('ce207_02', 5)	# 111-115
    sprite('ce207_00', 5)	# 116-120

@State
def CmnActChangeRequest():
    sprite('null', 60)	# 1-60

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 8)	# 121-128
    Unknown1086(22)
    teleportRelativeX(-50000)
    teleportRelativeX(-580000)
    Unknown1007(2900000)
    physicsXImpulse(20000)
    physicsYImpulse(-100000)
    sendToLabelUpon(2, 9)
    label(1)
    sprite('ce213_08ex00', 3)	# 129-131	 **attackbox here**
    GFX_0('mv213Eff', -1)
    sprite('ce213_08ex01', 3)	# 132-134	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 1)	# 135-135
    Unknown1084(1)
    clearUponHandler(2)
    GFX_1('ceef_402_stone', 0)
    sprite('ce213_08', 2)	# 136-137	 **attackbox here**
    StartMultihit()
    Unknown8004(100, 1, 1)
    Unknown26('mv213Eff')
    sprite('ce213_09', 3)	# 138-140
    sprite('ce213_10', 3)	# 141-143
    sprite('ce213_11', 3)	# 144-146
    sprite('ce260_00', 3)	# 147-149
    sprite('ce260_01', 3)	# 150-152
    sprite('ce260_02', 3)	# 153-155
    sprite('ce260_03', 4)	# 156-159
    sprite('ce260_04', 4)	# 160-163
    sprite('ce260_05', 3)	# 164-166

@State
def CmnActChangeReturnAppealBurst():
    sprite('ce111_05', 6)	# 1-6
    sprite('ce111_06', 6)	# 7-12
    sprite('ce111_07', 32)	# 13-44
    sprite('ce111_08', 8)	# 45-52
    sprite('ce111_09', 30)	# 53-82

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
    label(0)
    sprite('ce213_08ex00', 3)	# 32-34	 **attackbox here**
    GFX_0('mv213Eff', -1)
    sprite('ce213_08ex01', 3)	# 35-37	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 38-38
    Unknown1084(1)
    clearUponHandler(2)
    GFX_1('ceef_402_stone', 0)
    sprite('ce213_08', 3)	# 39-41	 **attackbox here**
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    StartMultihit()
    Unknown8004(100, 1, 1)
    Unknown26('mv213Eff')
    sprite('ce213_09', 3)	# 42-44
    sprite('ce213_10', 3)	# 45-47
    sprite('ce213_11', 3)	# 48-50
    sprite('ce260_00', 3)	# 51-53
    sprite('ce260_01', 3)	# 54-56
    sprite('ce260_02', 3)	# 57-59
    sprite('ce260_03', 3)	# 60-62
    sprite('ce260_04', 3)	# 63-65
    sprite('ce260_05', 3)	# 66-68

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('ce213_09', 5)	# 2-6
    sprite('ce213_10', 5)	# 7-11
    sprite('ce213_11', 5)	# 12-16
    sprite('ce205_00', 2)	# 17-18
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 2)	# 19-20
    sprite('ce205_02', 2)	# 21-22
    sprite('ce205_03', 3)	# 23-25
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)	# 26-28
    sprite('ce205_03ex02', 3)	# 29-31
    sprite('ce205_04', 1)	# 32-32
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)	# 33-34
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    Unknown7007('6263653130365f300000000000000000640000006263653130365f310000000000000000640000006263653130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ce205_06', 2)	# 35-36	 **attackbox here**
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)	# 37-38	 **attackbox here**
    Unknown1019(50)
    sprite('ce205_07', 8)	# 39-46
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)	# 47-54
    Unknown1019(50)
    sprite('ce205_09', 7)	# 55-61
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)	# 62-68
    sprite('ce205_11', 7)	# 69-75

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
    sprite('ce207_00', 3)	# 1-3
    sprite('ce207_00', 2)	# 4-5
    Unknown7009(1)
    sprite('ce207_01', 5)	# 6-10
    sprite('ce207_02', 5)	# 11-15
    sprite('ce207_03', 5)	# 16-20
    sprite('ce207_04', 5)	# 21-25
    sprite('ce207_01', 5)	# 26-30
    sprite('ce207_00', 5)	# 31-35

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
    sprite('ce218_00', 3)	# 1-3
    sprite('ce218_00', 2)	# 4-5
    sprite('ce218_01', 5)	# 6-10
    sprite('ce218_02', 5)	# 11-15
    sprite('ce218_03', 5)	# 16-20
    sprite('ce218_04', 5)	# 21-25
    sprite('ce218_01', 5)	# 26-30
    sprite('ce218_00', 5)	# 31-35

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
    sprite('ce217_00', 3)	# 1-3
    sprite('ce217_00', 2)	# 4-5
    Unknown7007('6263653131335f300000000000000000640000006263653131335f310000000000000000640000006263653131335f320000000000000000000000000000000000000000000000000000000000000000')
    sprite('ce217_01', 5)	# 6-10
    sprite('ce217_02', 5)	# 11-15
    sprite('ce217_03', 5)	# 16-20
    sprite('ce217_04', 5)	# 21-25
    sprite('ce217_01', 5)	# 26-30
    sprite('ce217_02', 5)	# 31-35
    sprite('ce217_03', 5)	# 36-40
    sprite('ce217_00', 5)	# 41-45

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
    sprite('ce217_00', 3)	# 1-3
    sprite('ce208_01', 4)	# 4-7
    sprite('ce208_02', 4)	# 8-11
    sprite('ce208_03', 4)	# 12-15
    sprite('ce208_04', 4)	# 16-19
    sprite('ce208_01', 5)	# 20-24
    sprite('ce440_00', 4)	# 25-28
    physicsXImpulse(-3000)
    sprite('ce440_01', 4)	# 29-32
    Unknown1019(200)
    sprite('ce440_02', 4)	# 33-36
    Unknown7007('6263653238325f300000000000000000640000006263653238325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ce440_03', 4)	# 37-40
    Unknown1019(80)
    sprite('ce440_04', 4)	# 41-44
    Unknown1019(80)
    sprite('ce440_05', 4)	# 45-48
    Unknown1019(80)
    sprite('ce440_06', 4)	# 49-52
    Unknown1019(80)
    sprite('ce440_07', 4)	# 53-56
    Unknown1084(1)
    sprite('ce440_08', 20)	# 57-76
    Unknown18009(1)
    sprite('ce440_09', 6)	# 77-82
    sprite('ce440_10', 6)	# 83-88

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
    sprite('ce200_00', 3)	# 1-3
    Unknown1051(60)
    sprite('ce200_01', 2)	# 4-5
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    sprite('ce200_02', 2)	# 6-7	 **attackbox here**
    sprite('keep', 1)	# 8-8
    if (not CheckInput(0x1)):
        sendToLabel(0)
    sprite('ce200_03', 3)	# 9-11
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_04', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('ce200_05', 5)	# 15-19
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)	# 20-22
    sprite('ce200_00', 3)	# 23-25
    ExitState()
    label(0)
    sprite('ce200_03', 3)	# 26-28
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 4)	# 29-32
    sprite('ce200_00', 4)	# 33-36
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
    sprite('ce200_05', 3)	# 1-3
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_02', 2)	# 4-5	 **attackbox here**
    sprite('keep', 1)	# 6-6
    if (not CheckInput(0x1)):
        sendToLabel(0)
    sprite('ce200_03', 3)	# 7-9
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_04', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('ce200_05', 5)	# 13-17
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 3)	# 18-20
    sprite('ce200_00', 3)	# 21-23
    ExitState()
    label(0)
    sprite('ce200_03', 3)	# 24-26
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ce200_01', 4)	# 27-30
    sprite('ce200_00', 4)	# 31-34
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
    sprite('ce260_00', 3)	# 1-3
    sprite('ce214_00', 2)	# 4-5
    physicsXImpulse(5000)
    sprite('ce214_01', 2)	# 6-7
    Unknown1019(500)
    sprite('ce214_02', 2)	# 8-9
    sprite('ce214_03', 2)	# 10-11	 **attackbox here**
    Unknown1019(50)
    SLOT_51 = 1
    callSubroutine('DeriveInputFirst')
    Hitstop(6)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ce214_04', 4)	# 12-15	 **attackbox here**
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
    sprite('ce214_05', 3)	# 16-18	 **attackbox here**
    Unknown1019(75)
    setInvincible(0)
    sprite('ce214_06', 3)	# 19-21
    Unknown1019(75)
    Recovery()
    Unknown2063()
    sprite('ce214_07', 3)	# 22-24
    Unknown1019(75)
    sprite('ce214_08', 3)	# 25-27
    sprite('keep', 2)	# 28-29
    Unknown1019(0)
    callSubroutine('DeriveTimingFirst')
    sprite('ce260_00', 2)	# 30-31
    sprite('keep', 2)	# 32-33
    enterState('DriveEnd')

@State
def DriveEnd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Recovery()
    sprite('ce260_01', 4)	# 1-4
    sprite('ce260_02', 4)	# 5-8
    sprite('ce260_03', 4)	# 9-12
    sprite('ce260_04', 4)	# 13-16
    sprite('ce260_05', 4)	# 17-20

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
    sprite('ce260_00', 2)	# 1-2
    sprite('ce204_01', 2)	# 3-4
    sprite('ce204_02', 2)	# 5-6
    setInvincible(1)
    GuardPoint_(0)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown22036(0)
    Unknown22026(0)
    physicsXImpulse(10000)
    sprite('ce204_03', 3)	# 7-9	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(1750)
    AirPushbackY(-25000)
    callSubroutine('DeriveInputSecond')
    sprite('ce204_04', 2)	# 10-11	 **attackbox here**
    SLOT_51 = 1
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(2000)
    Unknown9190(0)
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    physicsXImpulse(40000)
    sprite('ce204_05', 2)	# 12-13	 **attackbox here**
    Unknown1019(120)
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    GFX_0('mv204Smoke', -1)
    GFX_0('mv204ringLoops', -1)
    sprite('ce204_04', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_05', 2)	# 16-17	 **attackbox here**
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_04', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_05', 2)	# 20-21	 **attackbox here**
    GFX_1('ceef_204eff', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_17')
    sprite('ce204_04', 2)	# 22-23	 **attackbox here**
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
    sprite('ce204_05', 2)	# 24-25	 **attackbox here**
    sprite('ce204_06', 2)	# 26-27
    setInvincible(0)
    Recovery()
    Unknown2063()
    Unknown23073()
    Unknown1019(80)
    Unknown26('mv204ringLoops')
    sprite('ce204_07', 2)	# 28-29
    Unknown1019(80)
    sprite('ce204_08', 2)	# 30-31
    Unknown1019(80)
    callSubroutine('DeriveTimingSecond')
    JumpCancel_(1)
    sprite('ce204_09', 2)	# 32-33
    Unknown1019(80)
    sprite('keep', 2)	# 34-35
    Unknown1019(0)
    sprite('ce260_00', 2)	# 36-37
    sprite('keep', 2)	# 38-39
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
    sprite('ce270_00', 3)	# 1-3
    sprite('ce270_01', 3)	# 4-6
    GFX_0('mv205ConsentEff', 0)
    sprite('ce270_02', 2)	# 7-8
    sprite('ce270_03', 2)	# 9-10	 **attackbox here**
    sprite('ce270_04', 2)	# 11-12	 **attackbox here**
    SLOT_51 = 1
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_22')
    sprite('ce270_05', 4)	# 13-16	 **attackbox here**
    GFX_0('ceef_270', 4)
    GFX_1('ceef_270burner', 1)
    GFX_1('ceef_270burner', 2)
    GFX_1('ceef_270burner', 3)
    sprite('ce270_06', 3)	# 17-19	 **attackbox here**
    sprite('ce270_07', 3)	# 20-22
    loopRest()
    if SLOT_2:
        enterState('Finish_Healing')
    sprite('ce270_11', 3)	# 23-25	 **attackbox here**
    sprite('ce270_12', 3)	# 26-28	 **attackbox here**
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
    sprite('ce270_08', 6)	# 1-6	 **attackbox here**
    sprite('ce270_09', 6)	# 7-12	 **attackbox here**
    sprite('ce270_10', 6)	# 13-18	 **attackbox here**
    sprite('ce432_09', 3)	# 19-21
    callSubroutine('MinervaCallAttack')
    Unknown23029(11, 404, 0)
    sprite('ce432_09', 3)	# 22-24
    GFX_0('SuperHealEff', -1)
    SLOT_53 = (SLOT_53 + 3000)
    sprite('ce432_10', 6)	# 25-30
    sprite('ce432_11', 6)	# 31-36
    sprite('ce432_12', 5)	# 37-41
    Unknown21012('53757065724865616c456666000000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_13', 4)	# 42-45
    sprite('ce432_14', 4)	# 46-49
    sprite('ce432_15', 4)	# 50-53

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8004(100, 1, 1)
            sendToLabel(1)
    sprite('ce213_00', 3)	# 1-3
    sprite('ce213_01', 3)	# 4-6
    physicsXImpulse(15000)
    physicsYImpulse(20000)
    setGravity(2800)
    tag_voice(1, 'bce156_0', 'bce156_1', '', '')
    sprite('ce213_02', 3)	# 7-9
    sprite('ce213_03', 3)	# 10-12
    sprite('ce213_04', 3)	# 13-15
    sprite('ce213_05', 3)	# 16-18
    label(0)
    sprite('ce213_06', 3)	# 19-21
    GFX_0('mv213Eff', -1)
    SFX_3('cese_19')
    sprite('ce213_07', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('ce213_08', 3)	# 25-27	 **attackbox here**
    sprite('ce213_11', 3)	# 28-30
    sprite('ce260_01', 3)	# 31-33
    sprite('ce260_02', 3)	# 34-36
    sprite('ce260_03', 5)	# 37-41
    sprite('ce260_04', 5)	# 42-46
    sprite('ce260_05', 5)	# 47-51

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 3)	# 1-3
    sprite('ce213_11', 3)	# 4-6
    sprite('ce260_01', 3)	# 7-9
    sprite('ce260_02', 3)	# 10-12
    sprite('ce260_03', 3)	# 13-15
    sprite('ce260_04', 3)	# 16-18
    sprite('ce260_05', 3)	# 19-21
    sprite('ce203_00', 4)	# 22-25
    tag_voice(0, 'bce157_0', 'bce157_1', '', '')
    sprite('ce203_01', 4)	# 26-29
    sprite('ce203_02', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('mv203Eff', -1)
    SFX_0('003_swing_grap_0_0')
    SFX_3('cese_19')
    sprite('ce203_03', 4)	# 33-36
    sprite('ce203_04', 3)	# 37-39
    sprite('ce203_05', 2)	# 40-41
    sprite('keep', 2)	# 42-43
    sprite('ce260_00', 2)	# 44-45
    sprite('ce260_01', 4)	# 46-49
    sprite('ce260_02', 4)	# 50-53
    sprite('ce260_03', 4)	# 54-57
    sprite('ce260_04', 4)	# 58-61
    sprite('ce260_05', 4)	# 62-65
    sprite('ce000_00', 7)	# 66-72
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)	# 73-79
    sprite('ce000_02', 7)	# 80-86
    sprite('ce000_03', 7)	# 87-93
    sprite('ce000_04', 7)	# 94-100
    sprite('ce000_05', 7)	# 101-107
    sprite('ce000_06', 7)	# 108-114
    sprite('ce000_07', 7)	# 115-121
    sprite('ce000_08', 7)	# 122-128
    sprite('ce000_09', 7)	# 129-135
    sprite('ce000_10', 7)	# 136-142
    sprite('ce000_11', 7)	# 143-149
    label(0)
    sprite('ce000_00', 7)	# 150-156
    sprite('ce000_01', 7)	# 157-163
    sprite('ce000_02', 7)	# 164-170
    sprite('ce000_03', 7)	# 171-177
    sprite('ce000_04', 7)	# 178-184
    sprite('ce000_05', 7)	# 185-191
    sprite('ce000_06', 7)	# 192-198
    sprite('ce000_07', 7)	# 199-205
    sprite('ce000_08', 7)	# 206-212
    sprite('ce000_09', 7)	# 213-219
    sprite('ce000_10', 7)	# 220-226
    sprite('ce000_11', 7)	# 227-233
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 234-234

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce340_00', 2)	# 1-2
    sprite('ce340_01', 2)	# 3-4
    GFX_0('mv340ConsentEff', 0)
    sprite('ce340_03', 2)	# 5-6
    sprite('ce340_04', 3)	# 7-9
    sprite('ce340_05', 2)	# 10-11
    sprite('ce340_06', 3)	# 12-14
    sprite('ce340_10', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    GFX_1('ceef_340_tukieff', 0)
    SFX_3('cese_06')
    sprite('ce340_10', 2)	# 16-17	 **attackbox here**
    Unknown21012('6d76333430436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown8004(100, 1, 1)
    sprite('ce340_11', 6)	# 18-23
    sprite('ce340_12', 6)	# 24-29
    sprite('ce340_13', 3)	# 30-32
    sprite('ce340_14', 3)	# 33-35
    sprite('ce340_15', 3)	# 36-38
    sprite('ce340_16', 2)	# 39-40
    sprite('ce000_00', 7)	# 41-47
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)	# 48-54
    sprite('ce000_02', 7)	# 55-61
    sprite('ce000_03', 7)	# 62-68
    sprite('ce000_04', 7)	# 69-75
    sprite('ce000_05', 7)	# 76-82
    sprite('ce000_06', 7)	# 83-89
    sprite('ce000_07', 7)	# 90-96
    sprite('ce000_08', 7)	# 97-103
    sprite('ce000_09', 7)	# 104-110
    sprite('ce000_10', 7)	# 111-117
    sprite('ce000_11', 7)	# 118-124
    label(0)
    sprite('ce000_00', 7)	# 125-131
    sprite('ce000_01', 7)	# 132-138
    sprite('ce000_02', 7)	# 139-145
    sprite('ce000_03', 7)	# 146-152
    sprite('ce000_04', 7)	# 153-159
    sprite('ce000_05', 7)	# 160-166
    sprite('ce000_06', 7)	# 167-173
    sprite('ce000_07', 7)	# 174-180
    sprite('ce000_08', 7)	# 181-187
    sprite('ce000_09', 7)	# 188-194
    sprite('ce000_10', 7)	# 195-201
    sprite('ce000_11', 7)	# 202-208
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 209-209

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('ce401_00', 1)	# 1-1
    sprite('ce401_01', 1)	# 2-2
    sprite('ce205_00', 2)	# 3-4
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)	# 5-5
    sprite('ce205_02', 2)	# 6-7
    sprite('ce205_03', 3)	# 8-10
    tag_voice(0, 'bce158_0', 'bce158_1', '', '')
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)	# 11-13
    sprite('ce205_03ex02', 3)	# 14-16
    sprite('ce205_04', 1)	# 17-17
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)	# 18-19
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)	# 20-21	 **attackbox here**
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)	# 22-23	 **attackbox here**
    Unknown1019(50)
    sprite('ce205_07', 8)	# 24-31
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)	# 32-39
    Unknown1019(50)
    sprite('ce205_09', 7)	# 40-46
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)	# 47-53
    sprite('ce205_11', 7)	# 54-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce000_00', 7)	# 1-7
    callSubroutine('MinervaCallCrushAssault')
    sprite('ce000_01', 7)	# 8-14
    sprite('ce000_02', 7)	# 15-21
    sprite('ce000_03', 7)	# 22-28
    sprite('ce000_04', 7)	# 29-35
    sprite('ce000_05', 7)	# 36-42
    sprite('ce000_06', 7)	# 43-49
    sprite('ce000_07', 7)	# 50-56
    sprite('ce000_08', 7)	# 57-63
    sprite('ce000_09', 7)	# 64-70
    sprite('ce000_10', 7)	# 71-77
    sprite('ce000_11', 7)	# 78-84
    label(0)
    sprite('ce000_00', 7)	# 85-91
    sprite('ce000_01', 7)	# 92-98
    sprite('ce000_02', 7)	# 99-105
    sprite('ce000_03', 7)	# 106-112
    sprite('ce000_04', 7)	# 113-119
    sprite('ce000_05', 7)	# 120-126
    sprite('ce000_06', 7)	# 127-133
    sprite('ce000_07', 7)	# 134-140
    sprite('ce000_08', 7)	# 141-147
    sprite('ce000_09', 7)	# 148-154
    sprite('ce000_10', 7)	# 155-161
    sprite('ce000_11', 7)	# 162-168
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce401_00', 1)	# 169-169
    SLOT_4 = 0
    callSubroutine('MinervaNoneCallAttack')
    sprite('ce401_01', 1)	# 170-170
    sprite('ce205_00', 2)	# 171-172
    tag_voice(0, 'bce158_0', 'bce158_1', '', '')
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)	# 173-173
    sprite('ce205_02', 2)	# 174-175
    sprite('ce205_03', 3)	# 176-178
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)	# 179-181
    sprite('ce205_03ex02', 3)	# 182-184
    sprite('ce205_04', 1)	# 185-185
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)	# 186-187
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)	# 188-189	 **attackbox here**
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)	# 190-191	 **attackbox here**
    Unknown1019(50)
    sprite('ce205_07', 8)	# 192-199
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)	# 200-207
    Unknown1019(50)
    sprite('ce205_09', 7)	# 208-214
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)	# 215-221
    sprite('ce205_11', 7)	# 222-228

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('null', 13)	# 1-13
    sprite('null', 1)	# 14-14
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-800000)
    sprite('ce602_00', 3)	# 15-17
    physicsXImpulse(30000)
    callSubroutine('MinervaCallCrushAssault')
    Unknown23029(11, 100, 0)
    sprite('ce602_01', 3)	# 18-20
    Unknown23029(11, 111, 0)
    sprite('ce602_02', 3)	# 21-23
    sprite('ce602_03', 3)	# 24-26
    sprite('ce602_04', 3)	# 27-29
    sprite('ce602_05', 3)	# 30-32
    sprite('ce210_05', 6)	# 33-38
    Unknown1019(20)
    sprite('ce210_06', 3)	# 39-41
    Unknown1019(20)
    sprite('ce210_07', 3)	# 42-44	 **attackbox here**
    Unknown1019(25)
    physicsYImpulse(10000)
    setGravity(1000)
    RefreshMultihit()
    sprite('ce210_07', 6)	# 45-50	 **attackbox here**
    StartMultihit()
    sprite('ce210_08', 8)	# 51-58	 **attackbox here**
    StartMultihit()
    sprite('ce210_09', 5)	# 59-63	 **attackbox here**
    StartMultihit()
    Unknown1019(25)
    Unknown8000(100, 1, 1)
    sprite('ce210_10', 4)	# 64-67
    sprite('ce210_11', 4)	# 68-71
    Unknown1084(1)
    sprite('ce210_12', 4)	# 72-75
    sprite('ce210_13', 4)	# 76-79
    sprite('ce210_14', 4)	# 80-83
    sprite('ce000_00', 7)	# 84-90
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)	# 91-97
    sprite('ce000_02', 7)	# 98-104
    sprite('ce000_03', 7)	# 105-111
    sprite('ce000_04', 7)	# 112-118
    sprite('ce000_05', 7)	# 119-125
    sprite('ce000_06', 7)	# 126-132
    sprite('ce000_07', 7)	# 133-139
    sprite('ce000_08', 7)	# 140-146
    sprite('ce000_09', 7)	# 147-153
    sprite('ce000_10', 7)	# 154-160
    sprite('ce000_11', 7)	# 161-167
    label(0)
    sprite('ce000_00', 7)	# 168-174
    sprite('ce000_01', 7)	# 175-181
    sprite('ce000_02', 7)	# 182-188
    sprite('ce000_03', 7)	# 189-195
    sprite('ce000_04', 7)	# 196-202
    sprite('ce000_05', 7)	# 203-209
    sprite('ce000_06', 7)	# 210-216
    sprite('ce000_07', 7)	# 217-223
    sprite('ce000_08', 7)	# 224-230
    sprite('ce000_09', 7)	# 231-237
    sprite('ce000_10', 7)	# 238-244
    sprite('ce000_11', 7)	# 245-251
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 252-252

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        callSubroutine('MinervaCallCrushAssault')
    sprite('keep', 11)	# 1-11
    StartMultihit()
    setGravity(1000)
    sprite('ce210_09', 5)	# 12-16	 **attackbox here**
    RefreshMultihit()
    Unknown1019(25)
    Unknown8000(100, 1, 1)
    sprite('ce210_10', 4)	# 17-20
    Unknown23029(11, 100, 0)
    sprite('ce210_11', 4)	# 21-24
    Unknown1084(1)
    sprite('ce210_12', 4)	# 25-28
    sprite('ce210_13', 4)	# 29-32
    sprite('ce210_14', 4)	# 33-36
    sprite('ce000_00', 7)	# 37-43
    callSubroutine('MinervaCallCrushAssault')
    Unknown2004(1, 0)
    sprite('ce000_01', 7)	# 44-50
    sprite('ce000_02', 7)	# 51-57
    sprite('ce000_03', 7)	# 58-64
    sprite('ce000_04', 7)	# 65-71
    sprite('ce000_05', 7)	# 72-78
    sprite('ce000_06', 7)	# 79-85
    sprite('ce000_07', 7)	# 86-92
    sprite('ce000_08', 7)	# 93-99
    sprite('ce000_09', 7)	# 100-106
    sprite('ce000_10', 7)	# 107-113
    sprite('ce000_11', 7)	# 114-120
    label(0)
    sprite('ce000_00', 7)	# 121-127
    sprite('ce000_01', 7)	# 128-134
    sprite('ce000_02', 7)	# 135-141
    sprite('ce000_03', 7)	# 142-148
    sprite('ce000_04', 7)	# 149-155
    sprite('ce000_05', 7)	# 156-162
    sprite('ce000_06', 7)	# 163-169
    sprite('ce000_07', 7)	# 170-176
    sprite('ce000_08', 7)	# 177-183
    sprite('ce000_09', 7)	# 184-190
    sprite('ce000_10', 7)	# 191-197
    sprite('ce000_11', 7)	# 198-204
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 205-205

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ce401_00', 1)	# 1-1
    sprite('ce401_01', 1)	# 2-2
    sprite('ce205_00', 2)	# 3-4
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)	# 5-5
    sprite('ce205_02', 2)	# 6-7
    sprite('ce205_03', 3)	# 8-10
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)	# 11-13
    sprite('ce205_03ex02', 3)	# 14-16
    sprite('ce205_04', 1)	# 17-17
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)	# 18-19
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)	# 20-21	 **attackbox here**
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)	# 22-23	 **attackbox here**
    Unknown1019(50)
    sprite('ce205_07', 8)	# 24-31
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)	# 32-39
    Unknown1019(50)
    sprite('ce205_09', 7)	# 40-46
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)	# 47-53
    sprite('ce205_11', 7)	# 54-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ce000_00', 7)	# 1-7
    callSubroutine('MinervaCallCrushAssault')
    sprite('ce000_01', 7)	# 8-14
    sprite('ce000_02', 7)	# 15-21
    sprite('ce000_03', 7)	# 22-28
    sprite('ce000_04', 7)	# 29-35
    sprite('ce000_05', 7)	# 36-42
    sprite('ce000_06', 7)	# 43-49
    sprite('ce000_07', 7)	# 50-56
    sprite('ce000_08', 7)	# 57-63
    sprite('ce000_09', 7)	# 64-70
    sprite('ce000_10', 7)	# 71-77
    sprite('ce000_11', 7)	# 78-84
    label(0)
    sprite('ce000_00', 7)	# 85-91
    sprite('ce000_01', 7)	# 92-98
    sprite('ce000_02', 7)	# 99-105
    sprite('ce000_03', 7)	# 106-112
    sprite('ce000_04', 7)	# 113-119
    sprite('ce000_05', 7)	# 120-126
    sprite('ce000_06', 7)	# 127-133
    sprite('ce000_07', 7)	# 134-140
    sprite('ce000_08', 7)	# 141-147
    sprite('ce000_09', 7)	# 148-154
    sprite('ce000_10', 7)	# 155-161
    sprite('ce000_11', 7)	# 162-168
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce401_00', 1)	# 169-169
    SLOT_4 = 0
    callSubroutine('MinervaNoneCallAttack')
    sprite('ce401_01', 1)	# 170-170
    sprite('ce205_00', 2)	# 171-172
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)	# 173-173
    sprite('ce205_02', 2)	# 174-175
    sprite('ce205_03', 3)	# 176-178
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 3)	# 179-181
    sprite('ce205_03ex02', 3)	# 182-184
    sprite('ce205_04', 1)	# 185-185
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)	# 186-187
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(45000)
    sprite('ce205_06', 2)	# 188-189	 **attackbox here**
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(40)
    sprite('ce205_06', 2)	# 190-191	 **attackbox here**
    Unknown1019(50)
    sprite('ce205_07', 8)	# 192-199
    Unknown8004(100, 1, 1)
    Unknown1019(50)
    sprite('ce205_08', 8)	# 200-207
    Unknown1019(50)
    sprite('ce205_09', 7)	# 208-214
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce205_10', 7)	# 215-221
    sprite('ce205_11', 7)	# 222-228

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
    sprite('ce237_00', 3)	# 1-3
    Unknown1051(60)
    sprite('ce237_00', 2)	# 4-5
    Unknown7009(1)
    sprite('ce237_01', 5)	# 6-10
    sprite('ce237_02', 5)	# 11-15
    sprite('ce237_03', 5)	# 16-20
    sprite('ce237_03', 3)	# 21-23
    sprite('ce237_00', 5)	# 24-28

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
    sprite('ce233_00', 3)	# 1-3
    sprite('ce233_01', 3)	# 4-6
    sprite('ce233_02', 6)	# 7-12
    sprite('ce233_03', 6)	# 13-18
    callSubroutine('DeriveInputFirst')
    SLOT_51 = 1
    sprite('ce233_04', 4)	# 19-22	 **attackbox here**
    physicsXImpulse(35000)
    GFX_0('mv233Eff', 0)
    SFX_0('003_swing_grap_0_2')
    SFX_3('cese_19')
    sprite('ce233_05', 3)	# 23-25	 **attackbox here**
    Unknown1019(50)
    sprite('ce233_06', 3)	# 26-28
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('ce233_07', 2)	# 29-30
    Unknown1019(0)
    sprite('keep', 2)	# 31-32
    callSubroutine('DeriveTimingFirst')
    sprite('ce260_00', 2)	# 33-34
    sprite('keep', 2)	# 35-36
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
    sprite('ce260_00', 2)	# 1-2
    sprite('ce234_00', 2)	# 3-4
    GFX_0('mv234ConsentEff', 0)
    sprite('ce234_01', 2)	# 5-6
    sprite('ce234_02', 2)	# 7-8
    sprite('ce234_03', 2)	# 9-10	 **attackbox here**
    callSubroutine('DeriveInputSecond')
    SLOT_51 = 1
    sprite('ce234_04', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    GFX_0('mv234Eff', -1)
    SFX_0('003_swing_grap_0_1')
    SFX_3('cese_18')
    sprite('ce234_05', 3)	# 14-16
    Recovery()
    Unknown2063()
    Unknown21012('6d76323334436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('ce234_06', 3)	# 17-19
    sprite('ce234_07', 2)	# 20-21
    Unknown21012('6d76323334436f6e73656e74456666000000000000000000000000000000000021000000')
    sprite('keep', 2)	# 22-23
    callSubroutine('DeriveTimingSecond')
    sprite('ce260_00', 3)	# 24-26
    sprite('keep', 2)	# 27-28
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
    sprite('ce238_00', 3)	# 1-3
    Unknown1051(60)
    sprite('ce238_00', 2)	# 4-5
    Unknown7009(5)
    sprite('ce238_01', 5)	# 6-10
    sprite('ce238_02', 5)	# 11-15
    sprite('ce238_03', 5)	# 16-20
    sprite('ce238_04', 5)	# 21-25
    sprite('ce238_01', 5)	# 26-30
    sprite('ce238_02', 5)	# 31-35
    sprite('ce238_00', 5)	# 36-40

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
    sprite('ce258_00', 3)	# 1-3
    sprite('ce258_00', 2)	# 4-5
    Unknown7009(1)
    sprite('ce258_01', 5)	# 6-10
    sprite('ce258_02', 5)	# 11-15
    sprite('ce258_03', 5)	# 16-20
    sprite('ce258_04', 5)	# 21-25
    sprite('ce258_01', 5)	# 26-30
    sprite('ce258_02', 5)	# 31-35
    sprite('ce258_00', 5)	# 36-40

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
    sprite('ce257_00', 3)	# 1-3
    sprite('ce257_00', 2)	# 4-5
    sprite('ce257_01', 5)	# 6-10
    sprite('ce257_02', 5)	# 11-15
    sprite('ce257_03', 5)	# 16-20
    sprite('ce257_04', 5)	# 21-25
    sprite('ce257_00', 5)	# 26-30

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
    sprite('ce253_00', 3)	# 1-3
    sprite('ce253_01', 3)	# 4-6
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
    sprite('ce253_02', 3)	# 7-9
    sprite('ce213_03', 3)	# 10-12
    sprite('ce213_04', 3)	# 13-15
    sprite('ce213_05', 2)	# 16-17
    sprite('ce213_06', 32767)	# 18-32784
    label(100)
    sprite('keep', 3)	# 32785-32787
    SLOT_51 = 1
    callSubroutine('DeriveInputFirst')
    Unknown1021(-30000)
    SFX_3('cese_19')
    label(0)
    sprite('ce213_08ex00', 3)	# 32788-32790	 **attackbox here**
    GFX_0('mv213Eff', -1)
    sprite('ce213_08ex01', 3)	# 32791-32793	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 32794-32794
    Unknown1084(1)
    callSubroutine('DeriveInputFirst')
    clearUponHandler(2)
    GFX_1('ceef_402_stone', 0)
    sprite('ce213_08', 2)	# 32795-32796	 **attackbox here**
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
    sprite('ce213_09', 3)	# 32797-32799
    Recovery()
    Unknown2063()
    sprite('ce213_10', 3)	# 32800-32802
    sprite('ce213_11', 3)	# 32803-32805
    sprite('ce260_00', 5)	# 32806-32810
    callSubroutine('DeriveTimingFirst')
    sprite('keep', 2)	# 32811-32812
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
    sprite('ce404_00', 3)	# 1-3
    physicsXImpulse(10000)
    physicsYImpulse(40000)
    sprite('ce404_01', 3)	# 4-6
    Unknown1019(75)
    YAccel(75)
    Unknown7007('6263653130385f300000000000000000640000006263653130385f310000000000000000640000006263653130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ce404_02', 3)	# 7-9
    Unknown1019(75)
    YAccel(75)
    sprite('ce404_03', 3)	# 10-12
    Unknown1019(75)
    YAccel(75)
    sprite('ce404_04', 2)	# 13-14
    Unknown1019(75)
    YAccel(75)
    sprite('ce404_05', 3)	# 15-17	 **attackbox here**
    GFX_0('ce404KickEff', 100)
    Unknown1084(1)
    physicsXImpulse(54000)
    physicsYImpulse(-63000)
    SFX_0('000_airdash_0')
    SFX_0('004_swing_grap_1_2')
    SFX_3('cese_01')
    sprite('ce404_06', 3)	# 18-20	 **attackbox here**
    label(0)
    sprite('ce404_05', 3)	# 21-23	 **attackbox here**
    sprite('ce404_06', 3)	# 24-26	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('ce404_07', 5)	# 27-31
    Unknown21012('63653430344b69636b456666000000000000000000000000000000000000000020000000')
    clearUponHandler(2)
    Unknown21007(11, 32)
    Unknown1084(1)
    Recovery()
    sprite('ce404_08', 5)	# 32-36
    sprite('ce404_09', 5)	# 37-41
    sprite('ce404_10', 5)	# 42-46
    sprite('ce404_11', 5)	# 47-51

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
    sprite('ce032_00', 3)	# 1-3
    label(0)
    sprite('ce032_01', 4)	# 4-7
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    sprite('ce032_02', 4)	# 8-11
    SFX_3('cese_04')
    sprite('ce032_03', 4)	# 12-15
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce310_00', 2)	# 16-17
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ce310_01', 1)	# 18-18
    sprite('ce310_02', 3)	# 19-21	 **attackbox here**
    Unknown1084(1)
    sprite('ce310_03', 2)	# 22-23
    SFX_1('bce154')
    SFX_0('010_swing_sword_0')
    sprite('ce310_04', 2)	# 24-25
    sprite('ce310_05', 4)	# 26-29
    sprite('ce310_06', 5)	# 30-34
    sprite('ce310_07', 5)	# 35-39
    sprite('ce310_08', 5)	# 40-44

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
    sprite('ce310_02', 6)	# 1-6	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ce311_00', 6)	# 7-12	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('mv311ConsentEff', 1)
    sprite('ce311_01', 6)	# 13-18	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('bce153')
    sprite('ce311_02', 20)	# 19-38	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_03', 4)	# 39-42	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_04', 4)	# 43-46	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_3('cese_20')
    sprite('ce311_05', 4)	# 47-50	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)	# 51-55	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)	# 56-60	 **attackbox here**
    callSubroutine('ThrowSpecialCancelInput')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_07', 3)	# 61-63	 **attackbox here**
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown11072(1, 150000, 100000)
    sprite('ce311_08', 2)	# 64-65	 **attackbox here**
    GFX_0('mv311Eff', -1)
    sprite('ce311_09', 2)	# 66-67	 **attackbox here**
    sprite('ce311_08', 2)	# 68-69	 **attackbox here**
    sprite('ce311_09', 2)	# 70-71	 **attackbox here**
    sprite('ce311_08', 2)	# 72-73	 **attackbox here**
    sprite('ce311_09', 2)	# 74-75	 **attackbox here**
    sprite('ce311_08', 2)	# 76-77	 **attackbox here**
    sprite('ce311_09', 2)	# 78-79	 **attackbox here**
    sprite('ce311_08', 2)	# 80-81	 **attackbox here**
    sprite('ce311_09', 2)	# 82-83	 **attackbox here**
    sprite('ce311_08', 2)	# 84-85	 **attackbox here**
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000021000000')
    sprite('ce311_10', 3)	# 86-88	 **attackbox here**
    callSubroutine('ThrowSpecialCancelBegin')
    sprite('ce311_11', 3)	# 89-91	 **attackbox here**
    sprite('ce311_12', 3)	# 92-94	 **attackbox here**
    sprite('ce311_13', 3)	# 95-97	 **attackbox here**
    sprite('ce311_14', 3)	# 98-100	 **attackbox here**

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('ce032_00', 3)	# 1-3
    label(0)
    sprite('ce032_01', 4)	# 4-7
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    sprite('ce032_02', 4)	# 8-11
    SFX_3('cese_04')
    sprite('ce032_03', 4)	# 12-15
    GFX_1('ceef_dasheff_line', 0)
    GFX_1('ceef_dasheff_line', 1)
    SFX_3('cese_04')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce310_00', 2)	# 16-17
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ce310_01', 1)	# 18-18
    sprite('ce310_02', 3)	# 19-21	 **attackbox here**
    Unknown1084(1)
    sprite('ce310_03', 2)	# 22-23
    SFX_1('bce154')
    SFX_0('010_swing_sword_0')
    sprite('ce310_04', 2)	# 24-25
    sprite('ce310_05', 4)	# 26-29
    sprite('ce310_06', 5)	# 30-34
    sprite('ce310_07', 5)	# 35-39
    sprite('ce310_08', 5)	# 40-44

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
    sprite('ce310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ce310_00ex', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce003_00ex01', 3)	# 7-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce003_01ex01', 3)	# 10-12	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce003_00ex02', 3)	# 13-15	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce310_00exex01', 3)	# 16-18	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_02', 6)	# 19-24	 **attackbox here**
    Unknown2005()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('mv311ConsentEff', 1)
    SFX_1('bce153')
    sprite('ce311_03', 20)	# 25-44	 **attackbox here**
    teleportRelativeX(110000)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_04', 4)	# 45-48	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_3('cese_20')
    sprite('ce311_05', 4)	# 49-52	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)	# 53-57	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_06', 5)	# 58-62	 **attackbox here**
    callSubroutine('ThrowSpecialCancelInput')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ce311_07', 1)	# 63-63	 **attackbox here**
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown11072(1, 150000, 100000)
    sprite('ce311_08', 2)	# 64-65	 **attackbox here**
    GFX_0('mv311Eff', -1)
    sprite('ce311_09', 2)	# 66-67	 **attackbox here**
    sprite('ce311_08', 2)	# 68-69	 **attackbox here**
    sprite('ce311_09', 2)	# 70-71	 **attackbox here**
    sprite('ce311_08', 2)	# 72-73	 **attackbox here**
    sprite('ce311_09', 2)	# 74-75	 **attackbox here**
    sprite('ce311_08', 2)	# 76-77	 **attackbox here**
    sprite('ce311_09', 2)	# 78-79	 **attackbox here**
    sprite('ce311_08', 2)	# 80-81	 **attackbox here**
    sprite('ce311_09', 2)	# 82-83	 **attackbox here**
    sprite('ce311_08', 2)	# 84-85	 **attackbox here**
    Unknown21012('6d76333131436f6e73656e74456666000000000000000000000000000000000021000000')
    sprite('ce311_10', 3)	# 86-88	 **attackbox here**
    callSubroutine('ThrowSpecialCancelBegin')
    sprite('ce311_11', 3)	# 89-91	 **attackbox here**
    sprite('ce311_12', 3)	# 92-94	 **attackbox here**
    sprite('ce311_13', 3)	# 95-97	 **attackbox here**
    sprite('ce311_14', 3)	# 98-100	 **attackbox here**

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
    sprite('ce401_00', 1)	# 1-1
    sprite('ce401_01', 1)	# 2-2
    sprite('ce205_00', 2)	# 3-4
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 1)	# 5-5
    sprite('ce205_02', 2)	# 6-7
    sprite('ce205_02', 1)	# 8-8
    label(1)
    sprite('ce205_04', 2)	# 9-10
    tag_voice(1, 'bce200_0', 'bce200_1', 'bce200_2', '')
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce205_05', 2)	# 11-12
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_11')
    physicsXImpulse(30000)
    sprite('ce205_06', 3)	# 13-15	 **attackbox here**
    GFX_0('mv204Smoke', -1)
    GFX_0('mv205Eff', -1)
    Unknown1019(80)
    sprite('ce205_06', 3)	# 16-18	 **attackbox here**
    Unknown1019(50)
    sprite('ce205_07', 6)	# 19-24
    Unknown8004(100, 1, 1)
    setInvincible(0)
    Unknown1019(25)
    sprite('ce205_08', 6)	# 25-30
    Unknown1019(50)
    sprite('ce260_01', 7)	# 31-37
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce260_02', 7)	# 38-44
    sprite('ce260_03', 7)	# 45-51
    sprite('ce260_04', 7)	# 52-58
    sprite('ce260_05', 7)	# 59-65

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
    sprite('ce401_00', 1)	# 1-1
    Unknown23119(14474340, 10, 2)
    sprite('ce401_01', 1)	# 2-2
    sprite('ce401_02', 2)	# 3-4
    GFX_0('mv205ConsentEff', 0)
    sprite('ce401_03', 1)	# 5-5	 **attackbox here**
    sprite('ce401_04', 1)	# 6-6	 **attackbox here**
    sprite('ce401_05', 1)	# 7-7	 **attackbox here**
    sprite('ce401_05', 1)	# 8-8	 **attackbox here**
    label(101)
    sprite('ce401_07', 2)	# 9-10
    tag_voice(1, 'bce200_0', 'bce200_1', 'bce200_2', '')
    Unknown21012('6d7634303174616d654d61746f6d65000000000000000000000000000000000020000000')
    sprite('ce401_08', 2)	# 11-12
    SFX_0('005_swing_grap_2_2')
    SFX_3('cese_11')
    physicsXImpulse(30000)
    sprite('ce401_09', 3)	# 13-15	 **attackbox here**
    GFX_0('ce401PanchEff', -1)
    Unknown1019(80)
    sprite('ce401_09', 3)	# 16-18	 **attackbox here**
    Unknown1019(50)
    sprite('ce401_10', 6)	# 19-24
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    setInvincible(0)
    Unknown1019(25)
    sprite('ce401_11', 6)	# 25-30
    Unknown1019(50)
    sprite('ce260_01', 7)	# 31-37
    Unknown21012('6d76323035436f6e73656e74456666000000000000000000000000000000000020000000')
    Unknown1019(0)
    sprite('ce260_02', 7)	# 38-44
    sprite('ce260_03', 7)	# 45-51
    sprite('ce260_04', 7)	# 52-58
    sprite('ce260_05', 7)	# 59-65

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 400, 0)
        Unknown4020(11)
        Unknown23029(11, 413, 0)
    sprite('ce208_00', 5)	# 1-5
    sprite('ce208_01', 5)	# 6-10
    tag_voice(1, 'bce201_0', 'bce201_1', 'bce201_2', '')
    sprite('ce208_02', 5)	# 11-15
    sprite('ce208_03', 5)	# 16-20
    SFX_3('cese_08')
    sprite('ce208_04', 5)	# 21-25
    sprite('ce208_01', 5)	# 26-30
    sprite('ce208_02', 5)	# 31-35
    sprite('ce208_03', 5)	# 36-40
    sprite('ce208_01', 3)	# 41-43
    sprite('ce208_00', 3)	# 44-46

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 401, 0)
        Unknown4020(11)
        Unknown23029(11, 413, 0)
    sprite('ce208_00', 5)	# 1-5
    sprite('ce208_01', 5)	# 6-10
    tag_voice(1, 'bce201_0', 'bce201_1', 'bce201_2', '')
    sprite('ce208_02', 5)	# 11-15
    sprite('ce208_03', 5)	# 16-20
    SFX_3('cese_08')
    sprite('ce208_04', 5)	# 21-25
    sprite('ce208_01', 5)	# 26-30
    sprite('ce208_02', 5)	# 31-35
    sprite('ce208_03', 5)	# 36-40
    sprite('ce208_01', 3)	# 41-43
    sprite('ce208_00', 3)	# 44-46

@State
def ShotEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('MinervaCallAttack')
        Unknown23029(11, 402, 0)
        Unknown4020(11)
    sprite('ce208_00', 3)	# 1-3
    sprite('ce208_00', 2)	# 4-5
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('ce208_01', 5)	# 6-10
    tag_voice(1, 'bce105_0', 'bce105_1', 'bce105_2', '')
    sprite('ce208_02', 5)	# 11-15
    sprite('ce208_03', 5)	# 16-20
    SFX_3('cese_08')
    sprite('ce208_04', 5)	# 21-25
    sprite('ce208_01', 5)	# 26-30
    sprite('ce208_02', 5)	# 31-35
    sprite('ce208_03', 5)	# 36-40
    sprite('ce208_01', 5)	# 41-45
    sprite('ce208_02', 5)	# 46-50
    sprite('ce208_01', 3)	# 51-53
    sprite('ce208_00', 3)	# 54-56

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
    sprite('ce400_00', 1)	# 1-1
    sprite('ce400_01', 1)	# 2-2
    physicsXImpulse(-8000)
    sprite('ce400_02', 1)	# 3-3
    Unknown1019(50)
    sprite('ce215_00', 1)	# 4-4
    GFX_0('mv215ConsentEff', 0)
    Unknown1019(50)
    sprite('ce215_00', 1)	# 5-5
    Unknown1019(50)
    sprite('ce215_01', 2)	# 6-7
    sprite('ce215_02', 2)	# 8-9
    tag_voice(1, 'bce202_0', 'bce202_1', 'bce202_2', '')
    sprite('ce215_03', 2)	# 10-11
    setInvincible(1)
    sprite('ce215_04', 1)	# 12-12
    physicsXImpulse(0)
    sprite('ce215_05', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    physicsXImpulse(30000)
    SFX_3('cese_22')
    GFX_0('ce215JetEff', 1)
    GFX_0('ce215JetEff', 2)
    callSubroutine('CableDispON')
    sprite('ce215_06', 2)	# 15-16	 **attackbox here**
    Unknown1019(200)
    sprite('ce215_05', 2)	# 17-18	 **attackbox here**
    Unknown1019(140)
    sprite('ce215_06', 2)	# 19-20	 **attackbox here**
    sprite('ce215_05', 2)	# 21-22	 **attackbox here**
    loopRest()
    Unknown19(0, 2, 2)
    sprite('ce215_06', 2)	# 23-24	 **attackbox here**
    sprite('ce215_05', 2)	# 25-26	 **attackbox here**
    label(0)
    sprite('ce215_07', 2)	# 27-28
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('63653231354a657445666600000000000000000000000000000000000000000020000000')
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce215_07', 2)	# 29-30
    Unknown1019(50)
    sprite('ce215_08', 5)	# 31-35
    callSubroutine('CableDispOFF')
    Unknown1019(50)
    sprite('ce215_09', 5)	# 36-40
    Unknown1019(40)
    sprite('ce215_10', 4)	# 41-44
    Unknown1019(40)
    sprite('ce215_11', 4)	# 45-48
    Unknown1019(40)
    sprite('ce215_12', 4)	# 49-52
    Unknown1019(0)
    ExitState()
    label(1)
    sprite('keep', 3)	# 53-55
    Unknown1019(80)
    sprite('ce215_07', 2)	# 56-57
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('63653231354a657445666600000000000000000000000000000000000000000020000000')
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce215_07', 2)	# 58-59
    Unknown1019(25)
    sprite('ce215_08', 3)	# 60-62
    callSubroutine('CableDispOFF')
    Unknown1019(25)
    sprite('ce215_09', 3)	# 63-65
    Unknown1084(1)
    sprite('ce215_10', 3)	# 66-68
    sprite('ce215_11', 3)	# 69-71
    sprite('ce215_12', 3)	# 72-74

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
    sprite('ce400_00', 1)	# 1-1
    Unknown23119(14474340, 10, 2)
    sprite('ce400_01', 1)	# 2-2
    physicsXImpulse(-8000)
    sprite('ce400_02', 1)	# 3-3
    Unknown1019(50)
    sprite('ce400_03', 1)	# 4-4
    GFX_0('mv215ConsentEff', 0)
    Unknown1019(50)
    sprite('ce400_03', 1)	# 5-5
    Unknown1019(50)
    sprite('ce400_04', 1)	# 6-6
    setInvincible(1)
    sprite('ce400_05', 1)	# 7-7
    sprite('ce400_06', 2)	# 8-9
    tag_voice(1, 'bce202_0', 'bce202_1', 'bce202_2', '')
    sprite('ce400_07', 2)	# 10-11
    sprite('ce400_08', 1)	# 12-12
    Unknown1019(0)
    sprite('ce400_09', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    physicsXImpulse(30000)
    SFX_3('cese_09')
    GFX_0('ce400JetEff', 1)
    GFX_0('ce400JetEff', 2)
    GFX_0('ce400JetEffBackFireAtk', 3)
    GFX_0('mv400windMatome', -1)
    callSubroutine('CableDispON')
    sprite('ce400_10', 2)	# 15-16	 **attackbox here**
    Unknown1019(200)
    sprite('ce400_09', 2)	# 17-18	 **attackbox here**
    Unknown1019(140)
    sprite('ce400_10', 2)	# 19-20	 **attackbox here**
    sprite('ce400_09', 2)	# 21-22	 **attackbox here**
    loopRest()
    Unknown19(0, 2, 2)
    sprite('ce400_10', 2)	# 23-24	 **attackbox here**
    sprite('ce400_09', 2)	# 25-26	 **attackbox here**
    label(0)
    sprite('ce400_11', 2)	# 27-28
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown21012('63653430304a657445666600000000000000000000000000000000000000000020000000')
    Unknown26('mv400windMatome')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce400_11', 2)	# 29-30
    Unknown1019(50)
    sprite('ce215_08', 5)	# 31-35
    Unknown21012('63653430304a65744566664261636b4669726541746b0000000000000000000021000000')
    callSubroutine('CableDispOFF')
    Unknown1019(50)
    sprite('ce215_09', 5)	# 36-40
    Unknown1019(40)
    sprite('ce215_10', 4)	# 41-44
    Unknown1019(40)
    sprite('ce215_11', 4)	# 45-48
    Unknown1019(40)
    sprite('ce215_12', 4)	# 49-52
    Unknown1019(0)
    ExitState()
    label(1)
    sprite('keep', 3)	# 53-55
    Unknown1019(80)
    sprite('ce400_11', 2)	# 56-57
    clearUponHandler(11)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown21012('6d76323135436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown21012('63653430304a657445666600000000000000000000000000000000000000000020000000')
    Unknown26('mv400windMatome')
    Unknown1019(50)
    setInvincible(0)
    Recovery()
    sprite('ce400_11', 2)	# 58-59
    Unknown1019(50)
    sprite('ce215_08', 3)	# 60-62
    Unknown21012('63653430304a65744566664261636b4669726541746b0000000000000000000021000000')
    callSubroutine('CableDispOFF')
    Unknown1019(25)
    sprite('ce215_09', 3)	# 63-65
    Unknown1084(1)
    sprite('ce215_10', 3)	# 66-68
    sprite('ce215_11', 3)	# 69-71
    sprite('ce215_12', 3)	# 72-74

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
    sprite('ce402_00', 3)	# 1-3
    sprite('ce402_01', 3)	# 4-6
    sprite('ce402_02', 4)	# 7-10
    sprite('ce235_00', 3)	# 11-13
    GFX_0('mv235ConsentEff', 0)
    sprite('ce235_01', 3)	# 14-16
    setInvincible(1)
    sprite('ce235_02', 2)	# 17-18
    tag_voice(1, 'bce203_0', 'bce203_1', 'bce203_2', '')
    sprite('ce235_03', 2)	# 19-20
    sprite('ce235_04', 5)	# 21-25
    SFX_0('005_swing_grap_2_2')
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000020000000')
    physicsXImpulse(60000)
    Unknown1028(-7000)
    sprite('ce235_05', 5)	# 26-30	 **attackbox here**
    SFX_3('cese_22')
    GFX_0('mv235Eff', -1)
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown8004(100, 1, 1)
    Unknown1084(1)
    Unknown2016(100)
    Unknown2015(100)
    sprite('ce235_06', 6)	# 31-36
    setInvincible(0)
    Recovery()
    sprite('ce235_07', 6)	# 37-42
    sprite('ce235_08', 4)	# 43-46
    sprite('ce235_09', 4)	# 47-50
    sprite('ce235_10', 4)	# 51-54

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
    sprite('ce402_00', 3)	# 1-3
    Unknown23119(14474340, 10, 2)
    sprite('ce402_01', 3)	# 4-6
    sprite('ce402_02', 4)	# 7-10
    sprite('ce402_03', 3)	# 11-13
    GFX_0('mv235ConsentEff', 0)
    sprite('ce402_04', 3)	# 14-16
    setInvincible(1)
    sprite('ce402_05', 4)	# 17-20
    tag_voice(1, 'bce203_0', 'bce203_1', 'bce203_2', '')
    sprite('ce235_04', 5)	# 21-25
    SFX_0('005_swing_grap_2_2')
    GFX_1('ceef_402_dashsmoke', 0)
    GFX_1('ceef_402_dashsmoke', 1)
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000020000000')
    physicsXImpulse(90000)
    Unknown1028(-7000)
    sprite('ce402_06', 5)	# 26-30	 **attackbox here**
    SFX_3('cese_10')
    GFX_0('mv402Eff', -1)
    GFX_1('ceef_402_stone', 0)
    Unknown21012('6d76323335436f6e73656e74456666000000000000000000000000000000000021000000')
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    Unknown1084(1)
    Unknown2016(100)
    Unknown2015(100)
    sprite('ce402_07', 6)	# 31-36
    setInvincible(0)
    Recovery()
    sprite('ce402_08', 6)	# 37-42
    sprite('ce235_08', 4)	# 43-46
    sprite('ce235_09', 4)	# 47-50
    sprite('ce235_10', 4)	# 51-54

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
    sprite('ce432_00', 3)	# 1-3
    GFX_0('ceef_healjunbieff', -1)
    sprite('ce432_01', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 404, 0)
    GFX_0('ceef_HealJunbiAnim_R', -1)
    GFX_0('ceef_HealJunbiAnim_L', -1)
    tag_voice(1, 'bce204_0', 'bce204_1', 'bce204_2', '')
    sprite('ce432_02', 3)	# 7-9
    sprite('ce432_03', 3)	# 10-12
    Unknown21012('636565665f6865616c6a756e626965666600000000000000000000000000000020000000')
    GFX_0('ceef_HealKurukuru', -1)
    sprite('ce432_04', 6)	# 13-18
    sprite('ce432_05', 6)	# 19-24
    sprite('ce432_06', 6)	# 25-30
    sprite('ce432_07', 6)	# 31-36
    sprite('ce432_08', 6)	# 37-42
    sprite('ce432_09', 6)	# 43-48
    GFX_0('SuperHealEff', -1)
    Unknown30078(17000)
    Unknown21000(1)
    Unknown30030(1)
    label(100)
    sprite('ce432_10', 6)	# 49-54
    sprite('ce432_11', 6)	# 55-60
    sprite('ce432_09', 6)	# 61-66
    gotoLabel(100)
    label(101)
    sprite('ce432_12', 6)	# 67-72
    Unknown21012('53757065724865616c456666000000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_13', 6)	# 73-78
    sprite('ce432_14', 6)	# 79-84
    sprite('ce432_15', 6)	# 85-90

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
    sprite('ce432_00', 3)	# 1-3
    GFX_0('ceef_healjunbieff', -1)
    sprite('ce432_01', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 404, 0)
    GFX_0('ceef_HealJunbiAnim_R', -1)
    GFX_0('ceef_HealJunbiAnim_L', -1)
    tag_voice(1, 'bce204_0', 'bce204_1', 'bce204_2', '')
    sprite('ce432_02', 3)	# 7-9
    sprite('ce432_03', 3)	# 10-12
    Unknown21012('636565665f6865616c6a756e626965666600000000000000000000000000000020000000')
    GFX_0('ceef_HealKurukuru', -1)
    sprite('ce432_04', 6)	# 13-18
    sprite('ce432_05', 6)	# 19-24
    sprite('ce432_06', 6)	# 25-30
    sprite('ce432_07', 6)	# 31-36
    sprite('ce432_08', 6)	# 37-42
    sprite('ce432_09', 6)	# 43-48
    GFX_0('SuperHealEffSP', -1)
    SLOT_53 = (SLOT_53 + 3000)
    label(100)
    sprite('ce432_10', 6)	# 49-54
    sprite('ce432_11', 6)	# 55-60
    sprite('ce432_09', 6)	# 61-66
    gotoLabel(100)
    label(101)
    sprite('ce432_12', 6)	# 67-72
    sprite('ce432_13', 6)	# 73-78
    sprite('ce432_14', 6)	# 79-84
    Unknown21012('53757065724865616c456666535000000000000000000000000000000000000020000000')
    Unknown23029(11, 405, 0)
    sprite('ce432_15', 6)	# 85-90

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
    sprite('ce208_00', 5)	# 1-5
    Unknown30080('')
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce250_0', 'bce250_1', '', '')
    sprite('ce208_01', 5)	# 6-10
    sprite('ce208_02', 5)	# 11-15
    sprite('ce208_03', 5)	# 16-20
    sprite('ce208_04', 5)	# 21-25
    sprite('ce208_01', 5)	# 26-30
    sprite('ce208_02', 5)	# 31-35
    sprite('ce208_03', 5)	# 36-40
    sprite('ce208_04', 5)	# 41-45
    sprite('ce208_01', 5)	# 46-50
    sprite('ce208_02', 1)	# 51-51
    sprite('ce208_02', 4)	# 52-55
    sprite('ce208_00', 5)	# 56-60
    sprite('ce207_00', 5)	# 61-65
    sprite('ce207_01', 5)	# 66-70
    sprite('ce207_02', 5)	# 71-75
    sprite('ce207_03', 5)	# 76-80
    setInvincible(0)
    sprite('ce207_04', 5)	# 81-85
    sprite('ce207_01', 5)	# 86-90
    sprite('ce207_02', 5)	# 91-95
    tag_voice(0, 'bce251_0', 'bce251_1', '', '')
    sprite('ce207_03', 5)	# 96-100
    sprite('ce207_04', 5)	# 101-105
    label(0)
    sprite('ce207_01', 5)	# 106-110
    sprite('ce207_02', 5)	# 111-115
    sprite('ce207_03', 5)	# 116-120
    sprite('ce207_04', 5)	# 121-125
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)	# 126-130
    sprite('ce207_02', 5)	# 131-135
    sprite('ce207_00', 5)	# 136-140

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
    sprite('ce208_00', 5)	# 1-5
    Unknown30080('')
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce250_0', 'bce250_1', '', '')
    sprite('ce208_01', 5)	# 6-10
    sprite('ce208_02', 5)	# 11-15
    sprite('ce208_03', 5)	# 16-20
    sprite('ce208_04', 5)	# 21-25
    sprite('ce208_01', 5)	# 26-30
    sprite('ce208_02', 5)	# 31-35
    sprite('ce208_03', 5)	# 36-40
    sprite('ce208_04', 5)	# 41-45
    sprite('ce208_01', 5)	# 46-50
    sprite('ce208_02', 1)	# 51-51
    sprite('ce208_02', 4)	# 52-55
    sprite('ce208_00', 5)	# 56-60
    sprite('ce207_00', 5)	# 61-65
    sprite('ce207_01', 5)	# 66-70
    sprite('ce207_02', 5)	# 71-75
    sprite('ce207_03', 5)	# 76-80
    setInvincible(0)
    sprite('ce207_04', 5)	# 81-85
    sprite('ce207_01', 5)	# 86-90
    sprite('ce207_02', 5)	# 91-95
    tag_voice(0, 'bce251_0', 'bce251_1', '', '')
    sprite('ce207_03', 5)	# 96-100
    sprite('ce207_04', 5)	# 101-105
    label(0)
    sprite('ce207_01', 5)	# 106-110
    sprite('ce207_02', 5)	# 111-115
    sprite('ce207_03', 5)	# 116-120
    sprite('ce207_04', 5)	# 121-125
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce207_01', 5)	# 126-130
    sprite('ce207_02', 5)	# 131-135
    sprite('ce207_00', 5)	# 136-140

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
    sprite('mv430_00', 5)	# 1-5
    setInvincible(1)
    Unknown22026(0)
    Unknown30080('')
    Unknown2036(113, -1, 2)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce252_0', 'bce252_1', '', '')
    sprite('mv430_01', 5)	# 6-10
    GFX_0('mv430ConsentEff', 0)
    sprite('mv430_02', 3)	# 11-13
    GFX_0('ThrowUpCelica', -1)
    Unknown22026(1)
    callSubroutine('RCEffCheck')
    sprite('mv430_03', 3)	# 14-16
    sprite('mv430_04', 8)	# 17-24
    Unknown20002(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown20005(60, 120)
    sprite('mv430_05', 6)	# 25-30
    sprite('mv430_06', 6)	# 31-36
    sprite('mv430_07', 6)	# 37-42
    sprite('mv430_08', 6)	# 43-48
    sprite('mv430_09', 2)	# 49-50
    sprite('mv430_10', 8)	# 51-58
    GFX_0('HensinThunder', -1)
    Unknown21012('6d76343330436f6e73656e74456666000000000000000000000000000000000020000000')
    ScreenShake(0, 200000)
    sprite('mv430_11', 30)	# 59-88
    sprite('mv430_12', 10)	# 89-98
    physicsXImpulse(2500)
    Unknown3029(1)
    Unknown3070(3)
    Unknown3071(3)
    Unknown3072('c8000000c8000000fa000000fa000000')
    Unknown3073('9600000096000000c8000000c8000000')
    Unknown3076(1000)
    Unknown3077(1000)
    sprite('mv430_13', 10)	# 99-108
    Unknown1019(200)
    Unknown20002(0)
    Unknown20003(0)
    Unknown20004(0)
    sprite('mv430_14', 10)	# 109-118
    Unknown26('HensinThunder')
    Unknown1019(200)
    Unknown3001(255)
    Unknown3004(-21)
    sprite('mv430_15', 3)	# 119-121	 **attackbox here**
    Unknown3001(64)
    Unknown3004(0)
    StartMultihit()
    Unknown8009(1)
    SFX_3('cese_09')
    EnableCollision(0)
    Unknown2015(250)
    Unknown2053(0)
    Unknown2034(0)
    sprite('mv430_15', 60)	# 122-181	 **attackbox here**
    Unknown3029(0)
    Unknown1019(900)
    Unknown1028(1000)
    label(1)
    sprite('null', 5)	# 182-186
    Unknown2005()
    Unknown1084(1)
    Unknown23032(0)
    EnableCollision(1)
    Unknown2015(100)
    Unknown2053(1)
    Unknown2034(1)
    sprite('null', 15)	# 187-201
    Unknown23024(0)
    sprite('ce020_07', 2)	# 202-203
    sendToLabelUpon(2, 12)
    Unknown23033(40)
    physicsYImpulse(-30000)
    Unknown1043()
    Unknown3004(21)
    label(11)
    sprite('ce020_08', 5)	# 204-208
    sprite('ce020_07', 5)	# 209-213
    gotoLabel(11)
    label(12)
    sprite('ce024_00', 3)	# 214-216
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
    sprite('ce024_01', 4)	# 217-220
    sprite('ce024_02', 4)	# 221-224
    sprite('ce024_03', 6)	# 225-230
    sprite('ce024_04', 6)	# 231-236
    ExitState()
    label(3)
    sprite('mv430_15', 5)	# 237-241	 **attackbox here**
    Unknown3001(64)
    Unknown3004(-12)
    StartMultihit()
    Unknown1028(0)
    Unknown2015(150)
    sprite('mv430_15', 25)	# 242-266	 **attackbox here**
    physicsXImpulse(0)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 130)	# 267-396
    GFX_0('ShungokuEff', -1)
    Unknown23084(1)
    GFX_0('UltimateAssaultAddAttack', -1)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    label(4)
    sprite('mv430_15', 2)	# 397-398	 **attackbox here**
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
    sprite('mv430_15', 1)	# 399-399	 **attackbox here**
    sprite('mv430_20', 6)	# 400-405
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
    sprite('mv430_21', 8)	# 406-413
    Unknown1019(50)
    sprite('mv430_22', 10)	# 414-423
    Unknown1019(50)
    sprite('mv430_22', 10)	# 424-433
    Unknown1019(50)
    sprite('mv430_23', 6)	# 434-439
    Unknown1019(50)
    sprite('mv430_24', 6)	# 440-445
    Unknown1019(50)
    sprite('mv430_19', 180)	# 446-625
    Unknown2005()
    Unknown13021(1)
    GFX_0('ThrowDownCelica', -1)
    Unknown1019(0)
    label(9)
    sprite('ce024_02', 1)	# 626-626
    Unknown23024(0)
    clearUponHandler(32)
    EnableCollision(1)
    setInvincible(0)
    SFX_0('024_getset_a')
    sprite('ce024_02', 4)	# 627-630
    sprite('ce024_03', 5)	# 631-635
    tag_voice(1, 'bce253_0', 'bce253_1', '', '')
    sprite('ce024_04', 5)	# 636-640
    sprite('ce024_05', 5)	# 641-645

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
    sprite('mv430_00', 5)	# 1-5
    setInvincible(1)
    Unknown22026(0)
    Unknown30080('')
    Unknown2036(113, -1, 2)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bce252_0', 'bce252_1', '', '')
    sprite('mv430_01', 5)	# 6-10
    GFX_0('mv430ConsentEff', 0)
    sprite('mv430_02', 3)	# 11-13
    GFX_0('ThrowUpCelica', -1)
    Unknown22026(1)
    callSubroutine('RCEffCheck')
    sprite('mv430_03', 3)	# 14-16
    sprite('mv430_04', 8)	# 17-24
    Unknown20002(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown20005(60, 120)
    sprite('mv430_05', 6)	# 25-30
    sprite('mv430_06', 6)	# 31-36
    sprite('mv430_07', 6)	# 37-42
    sprite('mv430_08', 6)	# 43-48
    sprite('mv430_09', 2)	# 49-50
    sprite('mv430_10', 8)	# 51-58
    Unknown21012('6d76343330436f6e73656e74456666000000000000000000000000000000000020000000')
    GFX_0('HensinThunder', -1)
    ScreenShake(0, 200000)
    sprite('mv430_11', 30)	# 59-88
    sprite('mv430_12', 10)	# 89-98
    physicsXImpulse(2500)
    Unknown3029(1)
    Unknown3070(3)
    Unknown3071(3)
    Unknown3072('c8000000c8000000fa000000fa000000')
    Unknown3073('9600000096000000c8000000c8000000')
    Unknown3076(1000)
    Unknown3077(1000)
    sprite('mv430_13', 10)	# 99-108
    Unknown1019(200)
    Unknown20002(0)
    Unknown20003(0)
    Unknown20004(0)
    sprite('mv430_14', 10)	# 109-118
    Unknown26('HensinThunder')
    Unknown1019(200)
    Unknown3001(255)
    Unknown3004(-12)
    sprite('mv430_15', 3)	# 119-121	 **attackbox here**
    Unknown3001(128)
    Unknown3004(0)
    StartMultihit()
    Unknown8009(1)
    SFX_3('cese_09')
    EnableCollision(0)
    Unknown2015(250)
    Unknown2053(0)
    Unknown2034(0)
    sprite('mv430_15', 60)	# 122-181	 **attackbox here**
    Unknown3029(0)
    Unknown1019(900)
    Unknown1028(1000)
    label(1)
    sprite('null', 5)	# 182-186
    Unknown2005()
    Unknown1084(1)
    Unknown23032(0)
    EnableCollision(1)
    Unknown2015(100)
    Unknown2053(1)
    Unknown2034(1)
    sprite('null', 15)	# 187-201
    Unknown23024(0)
    sprite('ce020_07', 2)	# 202-203
    sendToLabelUpon(2, 12)
    Unknown23033(40)
    physicsYImpulse(-30000)
    Unknown1043()
    Unknown3004(21)
    label(11)
    sprite('ce020_08', 5)	# 204-208
    sprite('ce020_07', 5)	# 209-213
    gotoLabel(11)
    label(12)
    sprite('ce024_00', 3)	# 214-216
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
    sprite('ce024_01', 4)	# 217-220
    sprite('ce024_02', 4)	# 221-224
    sprite('ce024_03', 6)	# 225-230
    sprite('ce024_04', 6)	# 231-236
    ExitState()
    label(3)
    sprite('mv430_20', 1)	# 237-237
    physicsXImpulse(90000)
    Unknown1028(0)
    Unknown23011(1)
    sprite('mv430_20', 1)	# 238-238
    Unknown23011(1)
    sprite('mv430_20', 1)	# 239-239
    Unknown23011(1)
    sprite('mv430_21', 3)	# 240-242
    GFX_0('ShungokuODSlashEff', -1)
    sprite('mv430_22', 2)	# 243-244
    Unknown1019(30)
    sprite('mv430_22', 4)	# 245-248
    Unknown1019(50)
    sprite('mv430_15', 1)	# 249-249	 **attackbox here**
    RefreshMultihit()
    AirUntechableTime(40)
    hitstun(40)
    Unknown9016(1)
    Unknown11057(700)
    Unknown2005()
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('mv430_20', 1)	# 250-250
    physicsXImpulse(90000)
    Unknown23011(1)
    sprite('mv430_20', 1)	# 251-251
    Unknown23011(1)
    sprite('mv430_20', 1)	# 252-252
    Unknown23011(1)
    GFX_0('ShungokuODSlashEff2', -1)
    sprite('mv430_21', 3)	# 253-255
    Unknown1019(25)
    sprite('mv430_22', 2)	# 256-257
    Unknown1019(50)
    sprite('mv430_22', 1)	# 258-258
    sprite('mv430_22', 22)	# 259-280
    sprite('mv430_15', 3)	# 281-283	 **attackbox here**
    sendToLabelUpon(12, 100)
    Unknown2005()
    physicsXImpulse(9000)
    StartMultihit()
    sprite('mv430_15', 15)	# 284-298	 **attackbox here**
    Unknown1019(1500)
    RefreshMultihit()
    Hitstop(0)
    GFX_0('ShungokuODSlashEff3', -1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('UltimateAssaultAddAttackSP')
    sprite('keep', 1)	# 299-299
    sendToLabel(1)
    label(100)
    sprite('mv430_15', 3)	# 300-302	 **attackbox here**
    clearUponHandler(12)
    Unknown3001(64)
    Unknown3004(-21)
    StartMultihit()
    Unknown2015(150)
    sprite('mv430_15', 25)	# 303-327	 **attackbox here**
    physicsXImpulse(0)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 130)	# 328-457
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
    sprite('mv430_15', 2)	# 458-459	 **attackbox here**
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
    sprite('mv430_15', 1)	# 460-460	 **attackbox here**
    sprite('mv430_20', 6)	# 461-466
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
    sprite('mv430_21', 8)	# 467-474
    Unknown1019(50)
    sprite('mv430_22', 10)	# 475-484
    Unknown1019(50)
    sprite('mv430_22', 10)	# 485-494
    Unknown1019(50)
    sprite('mv430_23', 6)	# 495-500
    Unknown1019(50)
    sprite('mv430_24', 6)	# 501-506
    Unknown1019(50)
    sprite('mv430_19', 180)	# 507-686
    Unknown2005()
    Unknown13021(1)
    GFX_0('ThrowDownCelica', -1)
    Unknown1019(0)
    label(9)
    sprite('ce024_02', 1)	# 687-687
    Unknown23024(0)
    clearUponHandler(32)
    EnableCollision(1)
    setInvincible(0)
    SFX_0('024_getset_a')
    sprite('ce024_02', 4)	# 688-691
    sprite('ce024_03', 5)	# 692-696
    tag_voice(1, 'bce253_0', 'bce253_1', '', '')
    sprite('ce024_04', 5)	# 697-701
    sprite('ce024_05', 5)	# 702-706

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
    sprite('ce450_00', 6)	# 1-6
    sprite('ce450_01', 4)	# 7-10	 **attackbox here**
    Unknown2036(52, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_CE_AH', -1)
    tag_voice(1, 'bce290_0', 'bce290_1', '', '')
    sprite('ce450_02', 4)	# 11-14	 **attackbox here**
    sprite('ce450_03', 4)	# 15-18	 **attackbox here**
    sprite('ce450_04', 4)	# 19-22	 **attackbox here**
    sprite('ce450_02', 4)	# 23-26	 **attackbox here**
    sprite('ce450_03', 4)	# 27-30	 **attackbox here**
    sprite('ce450_04', 4)	# 31-34	 **attackbox here**
    sprite('ce450_02', 4)	# 35-38	 **attackbox here**
    sprite('ce450_03', 4)	# 39-42	 **attackbox here**
    sprite('ce450_04', 4)	# 43-46	 **attackbox here**
    sprite('ce450_02', 4)	# 47-50	 **attackbox here**
    sprite('ce450_03', 4)	# 51-54	 **attackbox here**
    sprite('ce450_04', 4)	# 55-58	 **attackbox here**
    sprite('ce450_02', 4)	# 59-62	 **attackbox here**
    sprite('ce450_03', 4)	# 63-66	 **attackbox here**
    sprite('ce450_04', 4)	# 67-70	 **attackbox here**
    sprite('ce450_02', 4)	# 71-74	 **attackbox here**
    GFX_0('ceef450_Kousoku', -1)
    RefreshMultihit()
    SFX_0('022_magiccircle_a')
    sprite('ce450_03', 4)	# 75-78	 **attackbox here**
    sprite('ce450_04', 4)	# 79-82	 **attackbox here**
    sprite('ce450_02', 4)	# 83-86	 **attackbox here**
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('ce450_03', 4)	# 87-90	 **attackbox here**
    sprite('ce450_04', 4)	# 91-94	 **attackbox here**
    sprite('ce450_02', 4)	# 95-98	 **attackbox here**
    sprite('ce450_03', 4)	# 99-102	 **attackbox here**
    sprite('ce450_04', 4)	# 103-106	 **attackbox here**
    sprite('ce450_28', 5)	# 107-111
    sprite('ce450_29', 5)	# 112-116
    sprite('ce450_23', 5)	# 117-121
    sprite('ce450_24', 5)	# 122-126
    sprite('ce450_25', 5)	# 127-131
    sprite('ce450_26', 5)	# 132-136
    Unknown8000(100, 1, 1)
    sprite('ce450_27', 5)	# 137-141

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
    sprite('ce450_02', 5)	# 1-5	 **attackbox here**
    Unknown21012('636565663435305f4b6f75736f6b75000000000000000000000000000000000020000000')
    sprite('ce450_03', 5)	# 6-10	 **attackbox here**
    sprite('ce450_04', 5)	# 11-15	 **attackbox here**
    sprite('ce450_05', 5)	# 16-20
    sprite('ce450_06', 5)	# 21-25
    sprite('ce450_07', 5)	# 26-30
    sprite('ce450_08', 5)	# 31-35
    tag_voice(0, 'bce291_0', 'bce291_1', '', '')
    sprite('ce450_09', 5)	# 36-40
    sprite('ce450_10', 5)	# 41-45
    sprite('ce450_11', 5)	# 46-50
    sprite('ce450_12', 5)	# 51-55
    sprite('ce450_13', 5)	# 56-60
    sprite('ce450_14', 5)	# 61-65
    sprite('ce450_15', 5)	# 66-70
    Unknown2037(1)
    GFX_0('ceef450_BG', -1)
    SFX_3('cese_03')
    Unknown21012('636565663435305f4b6f75736f6b75000000000000000000000000000000000021000000')
    callSubroutine('RCEffCheck')
    sprite('ce450_16', 5)	# 71-75
    sprite('ce450_17', 5)	# 76-80
    sprite('ce450_18', 5)	# 81-85
    sprite('ce450_15', 5)	# 86-90
    sprite('ce450_16', 5)	# 91-95
    tag_voice(0, 'bce292_0', 'bce292_1', '', '')
    sprite('ce450_17', 5)	# 96-100
    sprite('ce450_18', 5)	# 101-105
    sprite('ce450_15', 5)	# 106-110
    sprite('ce450_16', 5)	# 111-115
    sprite('ce450_17', 5)	# 116-120
    sprite('ce450_18', 5)	# 121-125
    sprite('ce450_15', 5)	# 126-130
    sprite('ce450_16', 5)	# 131-135
    sprite('ce450_17', 5)	# 136-140
    sprite('ce450_18', 5)	# 141-145
    sprite('ce450_15', 5)	# 146-150
    sprite('ce450_16', 5)	# 151-155
    sprite('ce450_17', 5)	# 156-160
    sprite('ce450_18', 5)	# 161-165
    sprite('ce450_15', 5)	# 166-170
    sprite('ce450_16', 5)	# 171-175
    sprite('ce450_17', 5)	# 176-180
    sprite('ce450_18', 5)	# 181-185
    sprite('ce450_15', 5)	# 186-190
    tag_voice(0, 'bce293_0', 'bce293_1', '', '')
    sprite('ce450_16', 5)	# 191-195
    sprite('ce450_17', 5)	# 196-200
    sprite('ce450_18', 5)	# 201-205
    sprite('ce450_15', 5)	# 206-210
    sprite('ce450_16', 5)	# 211-215
    sprite('ce450_17', 5)	# 216-220
    sprite('ce450_18', 5)	# 221-225
    sprite('ce450_15', 5)	# 226-230
    sprite('ce450_16', 5)	# 231-235
    Unknown21012('636565663435305f42470000000000000000000000000000000000000000000020000000')
    sprite('ce450_17', 5)	# 236-240
    sprite('ce450_18', 5)	# 241-245
    Unknown20000(0)
    sprite('ce450_15', 5)	# 246-250
    GFX_0('AstCameraObj', -1)
    Unknown38(4, 1)
    sprite('ce450_16', 30)	# 251-280
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
    sprite('ce450_16', 260)	# 281-540
    GFX_0('AHCamera', -1)
    GFX_0('AHKiraEff', -1)
    sprite('ce450_16', 10)	# 541-550
    Unknown23024(2)
    sprite('ce450_16', 25)	# 551-575
    Unknown36(22)
    teleportRelativeY(0)
    Unknown35()
    Unknown21012('414843616d65726100000000000000000000000000000000000000000000000020000000')
    sprite('ce450_16', 10)	# 576-585
    sprite('ce450_16', 5)	# 586-590
    GFX_0('ceef450_BG3', -1)
    Unknown3004(26)
    Unknown36(22)
    Unknown3032()
    Unknown3004(26)
    Unknown35()
    sprite('ce450_17', 5)	# 591-595
    sprite('ce450_18', 5)	# 596-600
    sprite('ce450_15', 5)	# 601-605
    sprite('ce450_16', 5)	# 606-610
    sprite('ce450_17', 5)	# 611-615
    sprite('ce450_18', 5)	# 616-620
    sprite('ce450_15', 5)	# 621-625
    tag_voice(0, 'bce294_0', 'bce294_1', '', '')
    sprite('ce450_16', 5)	# 626-630
    sprite('ce450_17', 5)	# 631-635
    sprite('ce450_18', 5)	# 636-640
    sprite('ce450_15', 5)	# 641-645
    sprite('ce450_16', 5)	# 646-650
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
    sprite('ce450_17', 5)	# 651-655
    sprite('ce450_18', 5)	# 656-660
    sprite('ce450_15', 5)	# 661-665
    sprite('ce450_16', 5)	# 666-670
    GFX_0('mv450HanaTiri', -1)
    GFX_0('mv450SmokeMato', -1)
    sprite('ce450_17', 5)	# 671-675
    sprite('ce450_18', 5)	# 676-680
    sprite('ce450_19', 2)	# 681-682
    sprite('ce450_20', 2)	# 683-684
    sprite('ce450_21', 2)	# 685-686
    sprite('ce450_19', 2)	# 687-688
    GFX_0('AstDeathAttack', -1)
    GFX_0('mv450WhiteOut', -1)
    sprite('ce450_20', 2)	# 689-690
    sprite('ce450_21', 2)	# 691-692
    sprite('ce450_19', 2)	# 693-694
    sprite('ce450_20', 2)	# 695-696
    sprite('ce450_21', 2)	# 697-698
    sprite('ce450_19', 2)	# 699-700
    sprite('ce450_20', 2)	# 701-702
    sprite('ce450_21', 2)	# 703-704
    sprite('ce450_19', 2)	# 705-706
    sprite('ce450_20', 2)	# 707-708
    sprite('ce450_21', 2)	# 709-710
    sprite('ce450_19', 2)	# 711-712
    sprite('ce450_20', 2)	# 713-714
    sprite('ce450_21', 2)	# 715-716
    sprite('ce450_19', 2)	# 717-718
    sprite('ce450_20', 2)	# 719-720
    Unknown21007(4, 32)
    sprite('ce450_21', 2)	# 721-722
    sprite('ce450_19', 2)	# 723-724
    sprite('ce450_20', 2)	# 725-726
    sprite('ce450_21', 2)	# 727-728
    sprite('ce450_19', 2)	# 729-730
    sprite('ce450_20', 2)	# 731-732
    sprite('ce450_21', 2)	# 733-734
    sprite('ce450_19', 2)	# 735-736
    sprite('ce450_20', 2)	# 737-738
    sprite('ce450_21', 2)	# 739-740
    sprite('ce450_19', 2)	# 741-742
    sprite('ce450_20', 2)	# 743-744
    sprite('ce450_21', 2)	# 745-746
    sprite('ce450_19', 2)	# 747-748
    sprite('ce450_20', 2)	# 749-750
    sprite('ce450_21', 2)	# 751-752
    sprite('ce450_19', 2)	# 753-754
    sprite('ce450_20', 2)	# 755-756
    sprite('ce450_21', 2)	# 757-758
    sprite('ce450_19', 2)	# 759-760
    sprite('ce450_20', 2)	# 761-762
    sprite('ce450_21', 2)	# 763-764
    sprite('ce450_19', 2)	# 765-766
    sprite('ce450_20', 2)	# 767-768
    sprite('ce450_21', 2)	# 769-770
    sprite('ce450_19', 2)	# 771-772
    sprite('ce450_20', 2)	# 773-774
    sprite('ce450_21', 2)	# 775-776
    sprite('ce450_19', 2)	# 777-778
    sprite('ce450_20', 2)	# 779-780
    sprite('ce450_21', 2)	# 781-782
    sprite('ce450_22', 5)	# 783-787
    Unknown1000(260000)
    sprite('ce450_23', 5)	# 788-792
    sprite('ce450_24', 5)	# 793-797
    sprite('ce450_25', 5)	# 798-802
    sprite('ce450_26', 5)	# 803-807
    Unknown8000(100, 1, 1)
    sprite('ce450_27', 5)	# 808-812
    Unknown21007(11, 33)
    label(100)
    sprite('ce000_00', 50)	# 813-862
    Unknown21012('636565663435305f42473300000000000000000000000000000000000000000020000000')
    Unknown21012('414843616d65726100000000000000000000000000000000000000000000000021000000')
    sprite('ce620_00', 8)	# 863-870
    Unknown18010()
    tag_voice(0, 'bce295_0', 'bce295_1', '', '')
    sprite('ce620_01', 8)	# 871-878
    sprite('ce620_02', 8)	# 879-886
    sprite('ce620_03', 8)	# 887-894
    sprite('ce620_04', 8)	# 895-902
    sprite('ce620_05', 8)	# 903-910
    sprite('ce620_04', 8)	# 911-918
    sprite('ce620_03', 8)	# 919-926
    sprite('ce620_02', 8)	# 927-934
    sprite('ce000_00', 8)	# 935-942
    sprite('ce610_00', 8)	# 943-950
    sprite('ce610_01', 8)	# 951-958
    sprite('ce610_02', 8)	# 959-966
    sprite('ce610_03', 8)	# 967-974
    sprite('ce610_04', 75)	# 975-1049
    sprite('ce610_05', 32767)	# 1050-33816
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
    sprite('null', 1)	# 1-1
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
    sprite('ce020_07', 1)	# 2-2
    Unknown3038(1)
    teleportRelativeY(700000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        gotoLabel(1)
    sprite('ce020_07', 2)	# 3-4
    sendToLabelUpon(2, 3)
    Unknown3038(0)
    physicsYImpulse(-40000)
    label(2)
    sprite('ce020_08', 5)	# 5-9
    sprite('ce020_07', 5)	# 10-14
    gotoLabel(2)
    label(3)
    sprite('ce024_00', 3)	# 15-17
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
    sprite('ce024_01', 6)	# 18-23
    sprite('ce024_02', 6)	# 24-29
    sprite('ce024_03', 8)	# 30-37
    sprite('ce024_04', 8)	# 38-45
    sprite('ce600_00', 6)	# 46-51
    sprite('ce600_01', 6)	# 52-57
    sprite('ce600_01ex1', 6)	# 58-63
    sprite('ce600_01ex2', 6)	# 64-69
    Unknown7006('bce600def', 100, 912614242, 1701065008, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(4)
    sprite('ce600_01', 1)	# 70-70
    if SLOT_97:
        _gotolabel(4)
    sprite('ce600_01', 15)	# 71-85
    sprite('ce600_02', 8)	# 86-93
    loopRest()
    ExitState()
    label(10)
    sprite('ce601_00', 3)	# 94-96
    callSubroutine('MinervaCall')
    Unknown23029(11, 600, 0)
    if SLOT_17:
        _gotolabel(10)
    sprite('ce601_00', 1)	# 97-97
    if random_(2, 0, 25):
        Unknown2037(1)
        sendToLabel(11)
    else:
        Unknown7006('bce602def', 100, 912614242, 1701065520, 102, 0, 100, 912614242, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0)
    sprite('ce601_00', 70)	# 98-167
    label(11)
    sprite('ce601_00', 30)	# 168-197
    sprite('ce601_01', 6)	# 198-203
    Unknown23029(11, 601, 0)
    sprite('ce601_02', 6)	# 204-209
    sprite('ce601_03', 1)	# 210-210
    if SLOT_2:
        SFX_1('bce604def')
    label(12)
    sprite('ce601_03', 1)	# 211-211
    if SLOT_97:
        _gotolabel(12)
    sprite('ce601_03', 30)	# 212-241
    sprite('ce601_04', 6)	# 242-247
    sprite('ce601_05', 4)	# 248-251
    sprite('ce601_06', 4)	# 252-255
    sprite('ce601_07', 6)	# 256-261
    ExitState()
    label(100)
    sprite('ce000_00', 1)	# 262-262
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
    sprite('ce000_00', 7)	# 263-269
    sprite('ce000_01', 7)	# 270-276
    sprite('ce000_02', 7)	# 277-283
    sprite('ce000_03', 7)	# 284-290
    sprite('ce000_04', 7)	# 291-297
    sprite('ce000_05', 7)	# 298-304
    sprite('ce000_06', 7)	# 305-311
    sprite('ce000_07', 7)	# 312-318
    sprite('ce000_08', 7)	# 319-325
    sprite('ce000_09', 7)	# 326-332
    sprite('ce000_10', 7)	# 333-339
    sprite('ce000_11', 7)	# 340-346
    gotoLabel(101)
    label(102)
    sprite('ce401_00', 5)	# 347-351
    SLOT_4 = 0
    sprite('ce401_01', 5)	# 352-356
    sprite('ce205_00', 5)	# 357-361
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 5)	# 362-366
    sprite('ce205_02', 7)	# 367-373
    sprite('ce205_03', 3)	# 374-376
    GFX_0('mv401tameMatome', -1)
    sprite('ce205_03ex01', 4)	# 377-380
    sprite('ce205_03ex02', 4)	# 381-384
    Unknown21011(50)
    label(103)
    sprite('ce205_03ex01', 4)	# 385-388
    sprite('ce205_03ex02', 4)	# 389-392
    gotoLabel(103)
    label(110)
    sprite('ce000_00', 1)	# 393-393
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce000_00', 6)	# 394-399
    sprite('ce000_01', 7)	# 400-406
    sprite('ce000_02', 7)	# 407-413
    SFX_1('bce600bno')
    sprite('ce000_03', 7)	# 414-420
    sprite('ce000_04', 7)	# 421-427
    sprite('ce000_05', 7)	# 428-434
    sprite('ce000_06', 7)	# 435-441
    sprite('ce000_07', 7)	# 442-448
    sprite('ce000_08', 7)	# 449-455
    sprite('ce000_09', 7)	# 456-462
    sprite('ce000_10', 7)	# 463-469
    sprite('ce000_11', 7)	# 470-476
    label(111)
    sprite('ce000_00', 7)	# 477-483
    sprite('ce000_01', 7)	# 484-490
    sprite('ce000_02', 7)	# 491-497
    sprite('ce000_03', 7)	# 498-504
    sprite('ce000_04', 7)	# 505-511
    sprite('ce000_05', 7)	# 512-518
    sprite('ce000_06', 7)	# 519-525
    sprite('ce000_07', 7)	# 526-532
    sprite('ce000_08', 7)	# 533-539
    sprite('ce000_09', 7)	# 540-546
    sprite('ce000_10', 7)	# 547-553
    sprite('ce000_11', 7)	# 554-560
    if SLOT_97:
        _gotolabel(111)
    sprite('ce000_00', 1)	# 561-561
    Unknown21007(24, 40)
    Unknown21011(120)
    label(112)
    sprite('ce000_00', 7)	# 562-568
    sprite('ce000_01', 7)	# 569-575
    sprite('ce000_02', 7)	# 576-582
    sprite('ce000_03', 7)	# 583-589
    sprite('ce000_04', 7)	# 590-596
    sprite('ce000_05', 7)	# 597-603
    sprite('ce000_06', 7)	# 604-610
    sprite('ce000_07', 7)	# 611-617
    sprite('ce000_08', 7)	# 618-624
    sprite('ce000_09', 7)	# 625-631
    sprite('ce000_10', 7)	# 632-638
    sprite('ce000_11', 7)	# 639-645
    gotoLabel(112)
    label(120)
    sprite('ce000_00', 1)	# 646-646
    if SLOT_158:
        Unknown1000(-1465000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ce000_00', 7)	# 647-653
    sprite('ce000_01', 7)	# 654-660
    sprite('ce000_02', 7)	# 661-667
    sprite('ce000_03', 7)	# 668-674
    sprite('ce000_04', 7)	# 675-681
    sprite('ce000_05', 7)	# 682-688
    sprite('ce000_06', 7)	# 689-695
    sprite('ce000_07', 7)	# 696-702
    sprite('ce000_08', 7)	# 703-709
    sprite('ce000_09', 7)	# 710-716
    sprite('ce000_10', 7)	# 717-723
    sprite('ce000_11', 7)	# 724-730
    gotoLabel(121)
    label(122)
    sprite('ce610_00', 8)	# 731-738
    Unknown2005()
    sprite('ce610_01', 8)	# 739-746
    sprite('ce610_02', 8)	# 747-754
    SFX_1('bce601bny')
    sprite('ce610_03', 8)	# 755-762
    sprite('ce610_04', 8)	# 763-770
    label(123)
    sprite('ce610_05', 3)	# 771-773
    if SLOT_97:
        _gotolabel(123)
    sprite('ce610_05', 32767)	# 774-33540
    Unknown23018(1)
    label(130)
    sprite('ce000_00', 1)	# 33541-33541
    if (not SLOT_158):
        Unknown1000(-1230000)
    Unknown2005()
    callSubroutine('MinervaCall')
    Unknown23029(11, 610, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ce000_00', 7)	# 33542-33548
    sprite('ce000_01', 7)	# 33549-33555
    sprite('ce000_02', 7)	# 33556-33562
    sprite('ce000_03', 7)	# 33563-33569
    sprite('ce000_04', 7)	# 33570-33576
    sprite('ce000_05', 7)	# 33577-33583
    sprite('ce000_06', 7)	# 33584-33590
    sprite('ce000_07', 7)	# 33591-33597
    sprite('ce000_08', 7)	# 33598-33604
    sprite('ce000_09', 7)	# 33605-33611
    sprite('ce000_10', 7)	# 33612-33618
    sprite('ce000_11', 7)	# 33619-33625
    gotoLabel(131)
    label(132)
    sprite('ce610_00', 8)	# 33626-33633
    Unknown2005()
    sprite('ce610_01', 8)	# 33634-33641
    sprite('ce610_02', 8)	# 33642-33649
    SFX_1('bce601bpt')
    sprite('ce610_03', 8)	# 33650-33657
    sprite('ce610_04', 8)	# 33658-33665
    label(133)
    sprite('ce610_05', 3)	# 33666-33668
    if SLOT_97:
        _gotolabel(133)
    sprite('ce610_05', 10)	# 33669-33678
    sprite('ce610_05', 32767)	# 33679-66445
    Unknown21007(24, 40)
    Unknown21011(10)
    label(140)
    sprite('ce656_01', 7)	# 66446-66452
    Unknown2019(0)
    if SLOT_158:
        Unknown2005()
    else:
        Unknown1000(-1356000)
    sprite('ce656_01', 32767)	# 66453-99219

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce601bph')
        Unknown23018(1)
    label(150)
    sprite('ce000_00', 7)	# 99220-99226
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
    sprite('ce000_01', 7)	# 99227-99233
    sprite('ce000_02', 7)	# 99234-99240
    sprite('ce000_03', 7)	# 99241-99247
    sprite('ce000_04', 7)	# 99248-99254
    sprite('ce000_05', 7)	# 99255-99261
    sprite('ce000_06', 7)	# 99262-99268
    sprite('ce000_07', 7)	# 99269-99275
    sprite('ce000_08', 7)	# 99276-99282
    sprite('ce000_09', 7)	# 99283-99289
    sprite('ce000_10', 7)	# 99290-99296
    sprite('ce000_11', 7)	# 99297-99303
    sprite('ce000_00', 7)	# 99304-99310
    gotoLabel(151)
    label(152)
    sprite('ce401_00', 5)	# 99311-99315
    SLOT_4 = 0
    sprite('ce401_01', 5)	# 99316-99320
    sprite('ce205_00', 5)	# 99321-99325
    GFX_0('mv205ConsentEff', 0)
    sprite('ce205_01', 5)	# 99326-99330
    sprite('ce205_02', 7)	# 99331-99337
    sprite('ce205_03', 3)	# 99338-99340
    GFX_0('mv401tameMatome', -1)
    Unknown21007(24, 40)
    Unknown21011(200)
    label(153)
    sprite('ce205_03ex01', 4)	# 99341-99344
    sprite('ce205_03ex02', 4)	# 99345-99348
    gotoLabel(153)
    label(160)
    sprite('ce000_00', 1)	# 99349-99349
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
    sprite('ce000_00', 7)	# 99350-99356
    sprite('ce000_01', 7)	# 99357-99363
    sprite('ce000_02', 7)	# 99364-99370
    sprite('ce000_03', 7)	# 99371-99377
    sprite('ce000_04', 7)	# 99378-99384
    sprite('ce000_05', 7)	# 99385-99391
    sprite('ce000_06', 7)	# 99392-99398
    sprite('ce000_07', 7)	# 99399-99405
    sprite('ce000_08', 7)	# 99406-99412
    sprite('ce000_09', 7)	# 99413-99419
    sprite('ce000_10', 7)	# 99420-99426
    sprite('ce000_11', 7)	# 99427-99433
    gotoLabel(161)
    label(162)
    sprite('ce217_00', 3)	# 99434-99436
    Unknown23029(11, 611, 0)
    sprite('ce217_00', 2)	# 99437-99438
    sprite('ce217_00', 2)	# 99439-99440
    sprite('ce217_01', 5)	# 99441-99445
    sprite('ce217_02', 5)	# 99446-99450
    sprite('ce217_03', 5)	# 99451-99455
    sprite('ce217_04', 5)	# 99456-99460
    sprite('ce217_01', 5)	# 99461-99465
    sprite('ce217_02', 5)	# 99466-99470
    sprite('ce217_03', 5)	# 99471-99475
    sprite('ce217_04', 5)	# 99476-99480
    Unknown21011(30)
    label(163)
    sprite('ce217_01', 5)	# 99481-99485
    sprite('ce217_02', 5)	# 99486-99490
    sprite('ce217_03', 5)	# 99491-99495
    sprite('ce217_04', 5)	# 99496-99500
    gotoLabel(163)
    label(170)
    sprite('ce000_00', 1)	# 99501-99501
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
    sprite('ce000_00', 7)	# 99502-99508
    sprite('ce000_01', 7)	# 99509-99515
    sprite('ce000_02', 7)	# 99516-99522
    sprite('ce000_03', 7)	# 99523-99529
    sprite('ce000_04', 7)	# 99530-99536
    sprite('ce000_05', 7)	# 99537-99543
    sprite('ce000_06', 7)	# 99544-99550
    sprite('ce000_07', 7)	# 99551-99557
    sprite('ce000_08', 7)	# 99558-99564
    sprite('ce000_09', 7)	# 99565-99571
    sprite('ce000_10', 7)	# 99572-99578
    sprite('ce000_11', 7)	# 99579-99585
    gotoLabel(171)
    label(172)
    sprite('ce610_00', 8)	# 99586-99593
    sprite('ce610_01', 8)	# 99594-99601
    sprite('ce610_02', 8)	# 99602-99609
    sprite('ce610_03', 8)	# 99610-99617
    sprite('ce610_04', 8)	# 99618-99625
    sprite('ce610_05', 32767)	# 99626-132392
    SFX_1('bce601pag')
    Unknown23018(1)
    label(180)
    sprite('ce620_02', 5)	# 132393-132397
    Unknown1000(-1230000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce620_03', 23)	# 132398-132420
    sprite('ce620_04', 6)	# 132421-132426
    sprite('ce620_05', 23)	# 132427-132449
    sprite('ce620_02', 8)	# 132450-132457
    sprite('ce620_03', 23)	# 132458-132480
    sprite('ce620_04', 6)	# 132481-132486
    sprite('ce620_05', 23)	# 132487-132509
    SFX_1('bce600pel')
    label(181)
    sprite('ce620_05', 1)	# 132510-132510
    if SLOT_97:
        _gotolabel(181)
    sprite('ce620_05', 30)	# 132511-132540
    sprite('ce620_05', 32767)	# 132541-165307
    Unknown21007(24, 40)
    Unknown21011(200)
    loopRest()
    label(190)
    sprite('ce000_00', 1)	# 165308-165308
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    Unknown2037(30)
    sprite('ce000_00', 6)	# 165309-165314
    sprite('ce000_01', 7)	# 165315-165321
    SFX_1('bce600uli')
    Unknown23018(1)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
    label(191)
    sprite('ce000_02', 7)	# 165322-165328
    sprite('ce000_03', 7)	# 165329-165335
    sprite('ce000_04', 7)	# 165336-165342
    sprite('ce000_05', 7)	# 165343-165349
    sprite('ce000_06', 7)	# 165350-165356
    sprite('ce000_07', 7)	# 165357-165363
    sprite('ce000_08', 7)	# 165364-165370
    sprite('ce000_09', 7)	# 165371-165377
    sprite('ce000_10', 7)	# 165378-165384
    sprite('ce000_11', 7)	# 165385-165391
    sprite('ce000_00', 7)	# 165392-165398
    sprite('ce000_01', 7)	# 165399-165405
    gotoLabel(191)
    label(200)
    sprite('ce000_00', 1)	# 165406-165406
    Unknown1000(-1605000)
    Unknown2005()
    callSubroutine('MinervaCall')
    Unknown23029(11, 610, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ce000_00', 7)	# 165407-165413
    sprite('ce000_01', 7)	# 165414-165420
    sprite('ce000_02', 7)	# 165421-165427
    sprite('ce000_03', 7)	# 165428-165434
    sprite('ce000_04', 7)	# 165435-165441
    sprite('ce000_05', 7)	# 165442-165448
    sprite('ce000_06', 7)	# 165449-165455
    sprite('ce000_07', 7)	# 165456-165462
    sprite('ce000_08', 7)	# 165463-165469
    sprite('ce000_09', 7)	# 165470-165476
    sprite('ce000_10', 7)	# 165477-165483
    sprite('ce000_11', 7)	# 165484-165490
    gotoLabel(201)
    label(202)
    sprite('keep', 1)	# 165491-165491
    SLOT_4 = 0
    Unknown23076()
    Unknown1084(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(204)
    sprite('ce033_00', 2)	# 165492-165493
    SFX_3('cese_16')
    sprite('ce033_01', 2)	# 165494-165495
    physicsXImpulse(-20000)
    sprite('ce033_02', 2)	# 165496-165497
    teleportRelativeX(-20000)
    Unknown1019(150)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_02', 1)	# 165498-165498
    Unknown1019(150)
    sprite('ce033_03', 3)	# 165499-165501
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_04', 4)	# 165502-165505
    Unknown1019(15)
    Unknown8000(100, 1, 1)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_05', 4)	# 165506-165509
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_06', 4)	# 165510-165513
    Unknown1019(15)
    GFX_1('ceef_bstepeff_line', 0)
    GFX_1('ceef_bstepeff_line', 1)
    sprite('ce033_07', 3)	# 165514-165516
    physicsXImpulse(0)
    sprite('ce000_00', 1)	# 165517-165517
    SLOT_4 = 1
    label(203)
    sprite('ce000_00', 7)	# 165518-165524
    sprite('ce000_01', 7)	# 165525-165531
    sprite('ce000_02', 7)	# 165532-165538
    sprite('ce000_03', 7)	# 165539-165545
    sprite('ce000_04', 7)	# 165546-165552
    sprite('ce000_05', 7)	# 165553-165559
    sprite('ce000_06', 7)	# 165560-165566
    sprite('ce000_07', 7)	# 165567-165573
    sprite('ce000_08', 7)	# 165574-165580
    sprite('ce000_09', 7)	# 165581-165587
    sprite('ce000_10', 7)	# 165588-165594
    sprite('ce000_11', 7)	# 165595-165601
    gotoLabel(203)
    label(204)
    sprite('ce200_00', 3)	# 165602-165604
    sprite('ce200_01', 3)	# 165605-165607
    SFX_1('bce601ume')
    label(205)
    sprite('ce200_02', 3)	# 165608-165610	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_03', 3)	# 165611-165613
    sprite('ce200_04', 3)	# 165614-165616	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_05', 5)	# 165617-165621
    if SLOT_97:
        _gotolabel(205)
    sprite('ce200_02', 3)	# 165622-165624	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown23018(1)
    label(206)
    sprite('ce200_03', 3)	# 165625-165627
    sprite('ce200_04', 3)	# 165628-165630	 **attackbox here**
    sprite('ce200_05', 5)	# 165631-165635
    sprite('ce200_02', 3)	# 165636-165638	 **attackbox here**
    gotoLabel(206)
    label(210)
    sprite('ce601_00', 1)	# 165639-165639
    if SLOT_158:
        Unknown1000(-1465000)
    if SLOT_17:
        _gotolabel(210)
    sprite('ce601_00', 3)	# 165640-165642
    Unknown2005()
    callSubroutine('MinervaCall')
    Unknown23029(11, 600, 0)
    SFX_1('bce600uva')
    label(211)
    sprite('ce601_00', 215)	# 165643-165857
    sprite('ce601_01', 6)	# 165858-165863
    sprite('ce601_02', 6)	# 165864-165869
    Unknown23029(11, 601, 0)
    label(212)
    sprite('ce601_03', 1)	# 165870-165870
    if SLOT_97:
        _gotolabel(212)
    sprite('ce601_03', 32767)	# 165871-198637
    Unknown21007(24, 40)
    Unknown23018(1)
    label(220)
    sprite('ce620_02', 5)	# 198638-198642
    Unknown1000(-1230000)
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce620_03', 1)	# 198643-198643
    SFX_1('bce600ryn')
    label(221)
    sprite('ce620_03', 1)	# 198644-198644
    if SLOT_97:
        _gotolabel(221)
    sprite('ce620_03', 20)	# 198645-198664
    sprite('ce620_03', 32767)	# 198665-231431
    Unknown21007(24, 40)
    Unknown23018(1)
    loopRest()
    label(230)
    sprite('ce000_00', 1)	# 231432-231432
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce601ahe')
        Unknown23018(1)
    label(231)
    sprite('ce000_00', 7)	# 231433-231439
    sprite('ce000_01', 7)	# 231440-231446
    sprite('ce000_02', 7)	# 231447-231453
    sprite('ce000_03', 7)	# 231454-231460
    sprite('ce000_04', 7)	# 231461-231467
    sprite('ce000_05', 7)	# 231468-231474
    sprite('ce000_06', 7)	# 231475-231481
    sprite('ce000_07', 7)	# 231482-231488
    sprite('ce000_08', 7)	# 231489-231495
    sprite('ce000_09', 7)	# 231496-231502
    sprite('ce000_10', 7)	# 231503-231509
    sprite('ce000_11', 7)	# 231510-231516
    gotoLabel(231)
    label(240)
    sprite('ce000_00', 1)	# 231517-231517
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    sprite('ce000_00', 6)	# 231518-231523
    SFX_1('bce600rne')

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            clearUponHandler(3)
            Unknown21007(24, 40)
            Unknown23018(1)
    label(241)
    sprite('ce000_01', 7)	# 231524-231530
    sprite('ce000_02', 7)	# 231531-231537
    sprite('ce000_03', 7)	# 231538-231544
    sprite('ce000_04', 7)	# 231545-231551
    sprite('ce000_05', 7)	# 231552-231558
    sprite('ce000_06', 7)	# 231559-231565
    sprite('ce000_07', 7)	# 231566-231572
    sprite('ce000_08', 7)	# 231573-231579
    sprite('ce000_09', 7)	# 231580-231586
    sprite('ce000_10', 7)	# 231587-231593
    sprite('ce000_11', 7)	# 231594-231600
    sprite('ce000_00', 7)	# 231601-231607
    gotoLabel(241)
    label(991)
    sprite('ce000_00', 7)	# 231608-231614
    callSubroutine('MinervaCall')
    Unknown23029(11, 609, 0)
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ce000_00', 7)	# 231615-231621
    sprite('ce000_01', 7)	# 231622-231628
    sprite('ce000_02', 7)	# 231629-231635
    sprite('ce000_03', 7)	# 231636-231642
    sprite('ce000_04', 7)	# 231643-231649
    sprite('ce000_05', 7)	# 231650-231656
    sprite('ce000_06', 7)	# 231657-231663
    sprite('ce000_07', 7)	# 231664-231670
    sprite('ce000_08', 7)	# 231671-231677
    sprite('ce000_09', 7)	# 231678-231684
    sprite('ce000_10', 7)	# 231685-231691
    sprite('ce000_11', 7)	# 231692-231698
    gotoLabel(992)
    label(1000)
    sprite('ce000_00', 7)	# 231699-231705
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
    sprite('ce000_01', 7)	# 231706-231712
    sprite('ce000_02', 7)	# 231713-231719
    sprite('ce000_03', 7)	# 231720-231726
    sprite('ce000_04', 7)	# 231727-231733
    sprite('ce000_05', 7)	# 231734-231740
    sprite('ce000_06', 7)	# 231741-231747
    sprite('ce000_07', 7)	# 231748-231754
    sprite('ce000_08', 7)	# 231755-231761
    sprite('ce000_09', 7)	# 231762-231768
    sprite('ce000_10', 7)	# 231769-231775
    sprite('ce000_11', 7)	# 231776-231782
    sprite('ce000_00', 7)	# 231783-231789
    gotoLabel(1001)
    label(1002)
    sprite('ce603_01', 6)	# 231790-231795
    sprite('ce603_00', 6)	# 231796-231801
    SFX_1('bce602')
    label(1003)
    sprite('ce603_00', 6)	# 231802-231807
    if SLOT_97:
        _gotolabel(1003)
    sprite('ce603_00', 32767)	# 231808-264574
    Unknown23029(24, 10003, 0)
    Unknown23029(22, 10003, 0)
    Unknown23029(23, 10003, 0)

@State
def CmnActMatchWin():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
    if SLOT_108:
        _gotolabel(0)
    sprite('keep', 2)	# 1-2

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
    sprite('ce610_00', 8)	# 3-10
    Unknown23029(11, 604, 0)
    sprite('ce610_01', 8)	# 11-18
    sprite('ce610_02', 8)	# 19-26
    sprite('ce610_03', 8)	# 27-34
    sprite('ce610_04', 8)	# 35-42
    if SLOT_158:
        if SLOT_52:
            SFX_1('bce704def')
        elif SLOT_108:
            Unknown7006('bce402_0', 100, 879059810, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bce700def', 100, 929391458, 1701065008, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(1)
    sprite('ce610_05', 3)	# 43-45
    if SLOT_97:
        _gotolabel(1)
    sprite('ce610_05', 3)	# 46-48
    Unknown23018(1)
    sprite('ce610_05', 32767)	# 49-32815
    loopRest()
    label(10)
    sprite('keep', 1)	# 32816-32816
    if SLOT_158:
        Unknown20000(1)
    physicsXImpulse(5000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(12)
    sprite('ce030_00', 7)	# 32817-32823
    Unknown23029(11, 605, 0)
    label(11)
    sprite('ce030_01', 7)	# 32824-32830
    sprite('ce030_02', 7)	# 32831-32837
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)	# 32838-32844
    sprite('ce030_04', 7)	# 32845-32851
    sprite('ce030_05', 7)	# 32852-32858
    sprite('ce030_06', 7)	# 32859-32865
    sprite('ce030_07', 7)	# 32866-32872
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)	# 32873-32879
    sprite('ce030_09', 7)	# 32880-32886
    sprite('ce030_10', 7)	# 32887-32893
    loopRest()
    gotoLabel(11)
    label(12)
    physicsXImpulse(0)
    Unknown2019(250)
    Unknown21012('4d696e6572766157696e3032000000000000000000000000000000000000000020000000')
    sprite('ce010_00', 7)	# 32894-32900
    sprite('ce010_01', 7)	# 32901-32907
    sprite('ce010_02', 7)	# 32908-32914
    if SLOT_158:
        if SLOT_52:
            SFX_1('bce705def')
        else:
            Unknown7006('bce702def', 100, 929391458, 1701065520, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ce611_00', 7)	# 32915-32921	 **attackbox here**
    Unknown23018(1)
    label(13)
    sprite('ce611_01', 8)	# 32922-32929	 **attackbox here**
    sprite('ce611_02', 8)	# 32930-32937	 **attackbox here**
    sprite('ce611_03', 21)	# 32938-32958	 **attackbox here**
    sprite('ce611_01', 8)	# 32959-32966	 **attackbox here**
    sprite('ce611_04', 8)	# 32967-32974	 **attackbox here**
    sprite('ce611_05', 21)	# 32975-32995	 **attackbox here**
    sprite('ce611_04', 8)	# 32996-33003	 **attackbox here**
    sprite('ce611_01', 40)	# 33004-33043	 **attackbox here**
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
    sprite('ce030_00', 7)	# 33044-33050
    Unknown23029(11, 605, 0)
    label(101)
    sprite('ce030_01', 7)	# 33051-33057
    sprite('ce030_02', 7)	# 33058-33064
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)	# 33065-33071
    sprite('ce030_04', 7)	# 33072-33078
    sprite('ce030_05', 7)	# 33079-33085
    sprite('ce030_06', 7)	# 33086-33092
    sprite('ce030_07', 7)	# 33093-33099
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)	# 33100-33106
    sprite('ce030_09', 7)	# 33107-33113
    sprite('ce030_10', 7)	# 33114-33120
    loopRest()
    gotoLabel(101)
    label(102)
    physicsXImpulse(0)
    Unknown2019(250)
    Unknown21012('4d696e6572766157696e3032000000000000000000000000000000000000000020000000')
    sprite('ce010_00', 7)	# 33121-33127
    sprite('ce010_01', 7)	# 33128-33134
    sprite('ce010_02', 7)	# 33135-33141
    SFX_1('bce700brg')
    sprite('ce611_00', 7)	# 33142-33148	 **attackbox here**
    label(103)
    sprite('ce611_01', 8)	# 33149-33156	 **attackbox here**
    sprite('ce611_02', 8)	# 33157-33164	 **attackbox here**
    sprite('ce611_03', 21)	# 33165-33185	 **attackbox here**
    sprite('ce611_01', 8)	# 33186-33193	 **attackbox here**
    sprite('ce611_04', 8)	# 33194-33201	 **attackbox here**
    sprite('ce611_05', 21)	# 33202-33222	 **attackbox here**
    sprite('ce611_04', 8)	# 33223-33230	 **attackbox here**
    sprite('ce611_01', 40)	# 33231-33270	 **attackbox here**
    if SLOT_97:
        _gotolabel(103)
    sprite('ce611_01', 1)	# 33271-33271	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    label(104)
    sprite('ce611_01', 8)	# 33272-33279	 **attackbox here**
    sprite('ce611_02', 8)	# 33280-33287	 **attackbox here**
    sprite('ce611_03', 21)	# 33288-33308	 **attackbox here**
    sprite('ce611_01', 8)	# 33309-33316	 **attackbox here**
    sprite('ce611_04', 8)	# 33317-33324	 **attackbox here**
    sprite('ce611_05', 21)	# 33325-33345	 **attackbox here**
    sprite('ce611_04', 8)	# 33346-33353	 **attackbox here**
    sprite('ce611_01', 40)	# 33354-33393	 **attackbox here**
    gotoLabel(104)
    ExitState()
    label(110)
    sprite('ce000_00', 1)	# 33394-33394

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ce000_00', 7)	# 33395-33401
    sprite('ce000_01', 7)	# 33402-33408
    sprite('ce000_02', 7)	# 33409-33415
    sprite('ce000_03', 7)	# 33416-33422
    sprite('ce000_04', 7)	# 33423-33429
    sprite('ce000_05', 7)	# 33430-33436
    sprite('ce000_06', 7)	# 33437-33443
    sprite('ce000_07', 7)	# 33444-33450
    sprite('ce000_08', 7)	# 33451-33457
    sprite('ce000_09', 7)	# 33458-33464
    sprite('ce000_10', 7)	# 33465-33471
    sprite('ce000_11', 7)	# 33472-33478
    gotoLabel(111)
    label(112)
    sprite('ce610_00', 8)	# 33479-33486
    Unknown23029(11, 609, 0)
    Unknown2005()
    sprite('ce610_01', 8)	# 33487-33494
    sprite('ce610_02', 8)	# 33495-33502
    sprite('ce610_03', 8)	# 33503-33510
    sprite('ce610_04', 8)	# 33511-33518
    sprite('ce610_05', 32767)	# 33519-66285
    SFX_1('bce701bno')
    Unknown23018(1)
    label(120)
    sprite('ce000_00', 1)	# 66286-66286

    def upon_40():
        clearUponHandler(40)
        sendToLabel(121)
    sprite('ce000_00', 7)	# 66287-66293
    sprite('ce601_07', 7)	# 66294-66300
    sprite('ce601_06', 6)	# 66301-66306
    sprite('ce601_05', 4)	# 66307-66310
    sprite('ce601_04', 3)	# 66311-66313
    sprite('ce601_00', 32767)	# 66314-99080
    label(121)
    sprite('ce601_00', 32767)	# 99081-131847
    SFX_1('bce701bny')
    Unknown23018(1)
    label(130)
    sprite('ce000_00', 1)	# 131848-131848

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ce000_00', 7)	# 131849-131855
    sprite('ce000_01', 7)	# 131856-131862
    sprite('ce000_02', 7)	# 131863-131869
    sprite('ce000_03', 7)	# 131870-131876
    sprite('ce000_04', 7)	# 131877-131883
    sprite('ce000_05', 7)	# 131884-131890
    sprite('ce000_06', 7)	# 131891-131897
    sprite('ce000_07', 7)	# 131898-131904
    sprite('ce000_08', 7)	# 131905-131911
    sprite('ce000_09', 7)	# 131912-131918
    sprite('ce000_10', 7)	# 131919-131925
    sprite('ce000_11', 7)	# 131926-131932
    gotoLabel(131)
    label(132)
    sprite('ce610_00', 8)	# 131933-131940
    Unknown23029(11, 604, 0)
    sprite('ce610_01', 8)	# 131941-131948
    sprite('ce610_02', 8)	# 131949-131956
    sprite('ce610_03', 8)	# 131957-131964
    sprite('ce610_04', 8)	# 131965-131972
    sprite('ce610_05', 32767)	# 131973-164739
    SFX_1('bce702bpt')
    Unknown23018(1)
    label(140)
    sprite('ce000_00', 7)	# 164740-164746
    if SLOT_158:
        Unknown2019(0)
    else:
        Unknown2019(-500)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ce000_01', 7)	# 164747-164753
    sprite('ce000_02', 7)	# 164754-164760
    sprite('ce000_03', 7)	# 164761-164767
    sprite('ce000_04', 7)	# 164768-164774
    sprite('ce000_05', 7)	# 164775-164781
    sprite('ce000_06', 7)	# 164782-164788
    sprite('ce000_07', 7)	# 164789-164795
    sprite('ce000_08', 7)	# 164796-164802
    sprite('ce000_09', 7)	# 164803-164809
    sprite('ce000_10', 7)	# 164810-164816
    sprite('ce000_11', 7)	# 164817-164823
    sprite('ce000_00', 7)	# 164824-164830
    gotoLabel(141)
    label(142)
    sprite('ce656_00', 7)	# 164831-164837
    sprite('ce656_01', 32767)	# 164838-197604

    def upon_40():
        clearUponHandler(40)
        SFX_1('bce701bph')
        Unknown23018(1)
    Unknown23029(11, 604, 0)
    label(150)
    sprite('ce000_00', 1)	# 197605-197605

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ce000_00', 7)	# 197606-197612
    sprite('ce000_01', 7)	# 197613-197619
    sprite('ce000_02', 7)	# 197620-197626
    sprite('ce000_03', 7)	# 197627-197633
    sprite('ce000_04', 7)	# 197634-197640
    sprite('ce000_05', 7)	# 197641-197647
    sprite('ce000_06', 7)	# 197648-197654
    sprite('ce000_07', 7)	# 197655-197661
    sprite('ce000_08', 7)	# 197662-197668
    sprite('ce000_09', 7)	# 197669-197675
    sprite('ce000_10', 7)	# 197676-197682
    sprite('ce000_11', 7)	# 197683-197689
    gotoLabel(151)
    label(152)
    sprite('ce030_00', 7)	# 197690-197696
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
    sprite('ce030_01', 7)	# 197697-197703
    sprite('ce030_02', 7)	# 197704-197710
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)	# 197711-197717
    sprite('ce030_04', 7)	# 197718-197724
    sprite('ce030_05', 7)	# 197725-197731
    sprite('ce030_06', 7)	# 197732-197738
    sprite('ce030_07', 7)	# 197739-197745
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)	# 197746-197752
    sprite('ce030_09', 7)	# 197753-197759
    sprite('ce030_10', 7)	# 197760-197766
    loopRest()
    gotoLabel(153)
    label(154)
    sprite('ce615_00', 9)	# 197767-197775
    clearUponHandler(3)
    physicsXImpulse(0)
    Unknown21012('4d696e65727661526f756e6457696e000000000000000000000000000000000020000000')
    sprite('ce615_01', 9)	# 197776-197784
    sprite('ce615_02', 9)	# 197785-197793
    sprite('ce615_03', 6)	# 197794-197799
    sprite('ce615_04', 6)	# 197800-197805
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
    sprite('ce615_05', 8)	# 197806-197813
    sprite('ce615_06', 8)	# 197814-197821
    sprite('ce615_07', 8)	# 197822-197829
    gotoLabel(155)
    label(160)
    sprite('ce030_00', 7)	# 197830-197836
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
    sprite('ce030_01', 7)	# 197837-197843
    sprite('ce030_02', 7)	# 197844-197850
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)	# 197851-197857
    sprite('ce030_04', 7)	# 197858-197864
    sprite('ce030_05', 7)	# 197865-197871
    sprite('ce030_06', 7)	# 197872-197878
    sprite('ce030_07', 7)	# 197879-197885
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)	# 197886-197892
    sprite('ce030_09', 7)	# 197893-197899
    sprite('ce030_10', 7)	# 197900-197906
    loopRest()
    gotoLabel(161)
    label(162)
    physicsXImpulse(0)
    Unknown21012('4d696e65727661526f756e6457696e000000000000000000000000000000000020000000')
    sprite('ce615_00', 9)	# 197907-197915
    sprite('ce615_01', 9)	# 197916-197924
    sprite('ce615_02', 9)	# 197925-197933
    sprite('ce615_03', 6)	# 197934-197939
    sprite('ce615_04', 6)	# 197940-197945
    SFX_1('bce700pka')
    GFX_0('ce615Eff', 0)
    GFX_0('ce615Eff3', -1)
    SFX_3('cese_03')
    label(163)
    sprite('ce615_05', 8)	# 197946-197953
    sprite('ce615_06', 8)	# 197954-197961
    sprite('ce615_07', 8)	# 197962-197969
    if SLOT_97:
        _gotolabel(163)
    sprite('keep', 1)	# 197970-197970
    Unknown21007(24, 40)
    Unknown21011(150)
    label(164)
    sprite('ce615_05', 8)	# 197971-197978
    sprite('ce615_06', 8)	# 197979-197986
    sprite('ce615_07', 8)	# 197987-197994
    gotoLabel(164)
    loopRest()
    label(170)
    sprite('ce000_00', 1)	# 197995-197995

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ce000_00', 7)	# 197996-198002
    sprite('ce000_01', 7)	# 198003-198009
    sprite('ce000_02', 7)	# 198010-198016
    sprite('ce000_03', 7)	# 198017-198023
    sprite('ce000_04', 7)	# 198024-198030
    sprite('ce000_05', 7)	# 198031-198037
    sprite('ce000_06', 7)	# 198038-198044
    sprite('ce000_07', 7)	# 198045-198051
    sprite('ce000_08', 7)	# 198052-198058
    sprite('ce000_09', 7)	# 198059-198065
    sprite('ce000_10', 7)	# 198066-198072
    sprite('ce000_11', 7)	# 198073-198079
    gotoLabel(171)
    label(172)
    sprite('ce610_00', 8)	# 198080-198087
    Unknown23029(11, 604, 0)
    sprite('ce610_01', 8)	# 198088-198095
    sprite('ce610_02', 8)	# 198096-198103
    sprite('ce610_03', 8)	# 198104-198111
    sprite('ce610_04', 8)	# 198112-198119
    sprite('ce610_05', 8)	# 198120-198127
    SFX_1('bce701pag')
    label(173)
    sprite('ce610_05', 1)	# 198128-198128
    if SLOT_97:
        _gotolabel(173)
    sprite('ce610_05', 32767)	# 198129-230895
    Unknown23018(1)
    label(180)
    sprite('ce030_00', 7)	# 230896-230902
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
    sprite('ce030_01', 7)	# 230903-230909
    sprite('ce030_02', 7)	# 230910-230916
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_03', 7)	# 230917-230923
    sprite('ce030_04', 7)	# 230924-230930
    sprite('ce030_05', 7)	# 230931-230937
    sprite('ce030_06', 7)	# 230938-230944
    sprite('ce030_07', 7)	# 230945-230951
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_08', 7)	# 230952-230958
    sprite('ce030_09', 7)	# 230959-230965
    sprite('ce030_10', 7)	# 230966-230972
    loopRest()
    gotoLabel(181)
    label(182)
    physicsXImpulse(0)
    Unknown21012('4d696e65727661526f756e6457696e000000000000000000000000000000000020000000')
    sprite('ce615_00', 9)	# 230973-230981
    sprite('ce615_01', 9)	# 230982-230990
    sprite('ce615_02', 9)	# 230991-230999
    sprite('ce615_03', 6)	# 231000-231005
    sprite('ce615_04', 6)	# 231006-231011
    SFX_1('bce700uli')
    GFX_0('ce615Eff', 0)
    GFX_0('ce615Eff3', -1)
    SFX_3('cese_03')
    label(183)
    sprite('ce615_05', 8)	# 231012-231019
    sprite('ce615_06', 8)	# 231020-231027
    sprite('ce615_07', 8)	# 231028-231035
    if SLOT_97:
        _gotolabel(183)
    sprite('keep', 1)	# 231036-231036
    Unknown21007(24, 40)
    Unknown21011(180)
    label(184)
    sprite('ce615_05', 8)	# 231037-231044
    sprite('ce615_06', 8)	# 231045-231052
    sprite('ce615_07', 8)	# 231053-231060
    gotoLabel(184)
    label(190)
    sprite('ce000_00', 1)	# 231061-231061

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ce000_00', 7)	# 231062-231068
    sprite('ce000_01', 7)	# 231069-231075
    sprite('ce000_02', 7)	# 231076-231082
    sprite('ce000_03', 7)	# 231083-231089
    sprite('ce000_04', 7)	# 231090-231096
    sprite('ce000_05', 7)	# 231097-231103
    sprite('ce000_06', 7)	# 231104-231110
    sprite('ce000_07', 7)	# 231111-231117
    sprite('ce000_08', 7)	# 231118-231124
    sprite('ce000_09', 7)	# 231125-231131
    sprite('ce000_10', 7)	# 231132-231138
    sprite('ce000_11', 7)	# 231139-231145
    gotoLabel(191)
    label(192)
    sprite('ce200_00', 3)	# 231146-231148
    sprite('ce200_01', 3)	# 231149-231151
    SFX_1('bce701ume')
    Unknown23018(1)
    label(193)
    sprite('ce200_02', 3)	# 231152-231154	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_03', 3)	# 231155-231157
    sprite('ce200_04', 3)	# 231158-231160	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('ce200_05', 5)	# 231161-231165
    gotoLabel(193)
    label(200)
    sprite('ce000_00', 7)	# 231166-231172
    sprite('ce601_07', 7)	# 231173-231179
    sprite('ce601_06', 6)	# 231180-231185
    sprite('ce601_05', 4)	# 231186-231189
    sprite('ce601_04', 3)	# 231190-231192
    sprite('ce601_00', 60)	# 231193-231252
    sprite('ce601_01', 4)	# 231253-231256
    sprite('ce601_02', 3)	# 231257-231259
    sprite('ce601_03', 1)	# 231260-231260
    SFX_1('bce700uva')
    label(201)
    sprite('ce601_03', 1)	# 231261-231261
    if SLOT_97:
        _gotolabel(201)
    sprite('ce601_03', 30)	# 231262-231291
    sprite('ce601_03', 32767)	# 231292-264058
    Unknown21007(24, 40)
    Unknown21011(150)
    label(210)
    sprite('ce000_00', 1)	# 264059-264059

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('ce000_00', 7)	# 264060-264066
    sprite('ce000_01', 7)	# 264067-264073
    sprite('ce000_02', 7)	# 264074-264080
    sprite('ce000_03', 7)	# 264081-264087
    sprite('ce000_04', 7)	# 264088-264094
    sprite('ce000_05', 7)	# 264095-264101
    sprite('ce000_06', 7)	# 264102-264108
    sprite('ce000_07', 7)	# 264109-264115
    sprite('ce000_08', 7)	# 264116-264122
    sprite('ce000_09', 7)	# 264123-264129
    sprite('ce000_10', 7)	# 264130-264136
    sprite('ce000_11', 7)	# 264137-264143
    gotoLabel(211)
    label(212)
    sprite('ce620_02', 5)	# 264144-264148
    sprite('ce620_03', 32767)	# 264149-296915
    SFX_1('bce701ryn')
    Unknown23018(1)
    label(220)
    sprite('ce000_00', 1)	# 296916-296916

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('ce000_00', 7)	# 296917-296923
    sprite('ce000_01', 7)	# 296924-296930
    sprite('ce000_02', 7)	# 296931-296937
    sprite('ce000_03', 7)	# 296938-296944
    sprite('ce000_04', 7)	# 296945-296951
    sprite('ce000_05', 7)	# 296952-296958
    sprite('ce000_06', 7)	# 296959-296965
    sprite('ce000_07', 7)	# 296966-296972
    sprite('ce000_08', 7)	# 296973-296979
    sprite('ce000_09', 7)	# 296980-296986
    sprite('ce000_10', 7)	# 296987-296993
    sprite('ce000_11', 7)	# 296994-297000
    gotoLabel(221)
    label(222)
    sprite('ce610_00', 1)	# 297001-297001
    Unknown23029(11, 609, 0)
    Unknown2005()
    sprite('ce610_00', 7)	# 297002-297008
    sprite('ce610_01', 8)	# 297009-297016
    sprite('ce610_02', 8)	# 297017-297024
    sprite('ce610_03', 8)	# 297025-297032
    sprite('ce610_05', 32767)	# 297033-329799
    SFX_1('bce701ahe')
    Unknown23018(1)
    label(230)
    sprite('ce000_00', 1)	# 329800-329800

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('ce000_00', 7)	# 329801-329807
    sprite('ce000_01', 7)	# 329808-329814
    sprite('ce000_02', 7)	# 329815-329821
    sprite('ce000_03', 7)	# 329822-329828
    sprite('ce000_04', 7)	# 329829-329835
    sprite('ce000_05', 7)	# 329836-329842
    sprite('ce000_06', 7)	# 329843-329849
    sprite('ce000_07', 7)	# 329850-329856
    sprite('ce000_08', 7)	# 329857-329863
    sprite('ce000_09', 7)	# 329864-329870
    sprite('ce000_10', 7)	# 329871-329877
    sprite('ce000_11', 7)	# 329878-329884
    gotoLabel(231)
    label(232)
    sprite('ce620_02', 5)	# 329885-329889
    sprite('ce620_03', 23)	# 329890-329912
    sprite('ce620_04', 6)	# 329913-329918
    sprite('ce620_05', 23)	# 329919-329941
    sprite('ce620_02', 8)	# 329942-329949
    sprite('ce620_03', 32767)	# 329950-362716
    SFX_1('bce701pel')
    Unknown23018(1)
    label(240)
    sprite('ce610_00', 8)	# 362717-362724
    Unknown23029(11, 609, 0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    sprite('ce610_01', 8)	# 362725-362732
    sprite('ce610_02', 8)	# 362733-362740
    sprite('ce610_03', 8)	# 362741-362748
    sprite('ce610_04', 8)	# 362749-362756
    sprite('ce610_05', 8)	# 362757-362764
    SFX_1('bce700rne')
    label(241)
    sprite('ce610_05', 1)	# 362765-362765
    if SLOT_97:
        _gotolabel(241)
    sprite('ce610_05', 15)	# 362766-362780
    sprite('ce610_05', 32767)	# 362781-395547
    Unknown21007(24, 40)
    label(242)
    sprite('ce620_00', 7)	# 395548-395554
    sprite('ce620_01', 7)	# 395555-395561
    sprite('ce620_02', 5)	# 395562-395566
    SFX_1('bce702rne')
    sprite('ce620_03', 8)	# 395567-395574
    sprite('ce620_04', 6)	# 395575-395580
    sprite('ce620_05', 8)	# 395581-395588
    sprite('ce620_04', 6)	# 395589-395594
    sprite('ce620_03', 8)	# 395595-395602
    sprite('ce620_02', 8)	# 395603-395610
    sprite('ce620_02', 32767)	# 395611-428377
    Unknown23018(1)

@State
def CmnActLose():

    def upon_IMMEDIATE():
        callSubroutine('MinervaCall')
        Unknown23029(11, 606, 0)
    sprite('ce620_00', 7)	# 1-7
    sprite('ce620_01', 7)	# 8-14
    sprite('ce620_02', 5)	# 15-19
    sprite('ce620_03', 8)	# 20-27
    sprite('ce620_04', 6)	# 28-33
    sprite('ce620_05', 8)	# 34-41
    sprite('ce620_02', 8)	# 42-49
    sprite('ce620_03', 8)	# 50-57
    sprite('ce620_01', 20)	# 58-77
    sprite('ce620_06', 8)	# 78-85
    Unknown7006('bce403_0', 100, 879059810, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ce620_07', 8)	# 86-93
    label(0)
    sprite('ce620_08', 3)	# 94-96
    if SLOT_97:
        _gotolabel(0)
    sprite('ce620_08', 32767)	# 97-32863
    Unknown21011(30)