@Subroutine
def PreInit():
    Unknown12019('75626c00000000000000000000000000')

@Subroutine
def MatchInit():
    Health(20000)
    JumpYVelocity(19000)
    SuperJumpYVelocity(24000)
    Unknown12007(4000)
    Unknown12008(6600)
    Unknown12009(4000)
    Unknown12010(6600)
    Unknown12011(1200)
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
    Unknown15018(500)
    Unknown15019(100)
    Move_Register('ReactionFBrake', 0x0)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('ReactionBBrake', 0x0)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    Unknown15013(2000)
    Unknown14015(0, 450000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_2nd', 0x1)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14015(0, 600000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_3rd', 0x1)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14015(0, 600000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_4th', 0x1)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14015(0, 600000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown15013(1)
    Unknown14015(0, 650000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B_2nd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 650000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown15013(1)
    Unknown14015(0, 600000, -200000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown15021(1)
    Unknown15013(2000)
    Unknown14015(0, 550000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown15015(100, 100)
    Unknown14015(0, 650000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 450000, -150000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(0, 450000, -150000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(0, 500000, -450000, 50000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15012(3000)
    Unknown14015(750000, 1500000, -450000, 50000, 500, 25)
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
    Move_Register('DashAtack', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Unknown15013(2000)
    Unknown14015(450000, 800000, -200000, 300000, 500, 5)
    Move_EndRegister()
    Move_Register('ShotBeamA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 450000, -200000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('ShotBeamB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15013(1)
    Unknown14015(650000, 1500000, -200000, 300000, 500, 25)
    Move_EndRegister()
    Move_Register('ShotBeamC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(2000)
    Unknown15012(1)
    Unknown14015(650000, 1500000, 150000, 450000, 250, 10)
    Move_EndRegister()
    Move_Register('AirShotBeamA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown14015(0, 500000, -400000, 200000, 250, 15)
    Move_EndRegister()
    Move_Register('AirShotBeamB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown14015(600000, 1200000, -400000, 200000, 250, 15)
    Move_EndRegister()
    Move_Register('AirShotBeamC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(1)
    Unknown14015(750000, 1500000, -400000, 200000, 250, 15)
    Move_EndRegister()
    Move_Register('GrenadeA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown14015(0, 700000, -200000, 200000, 250, 20)
    Move_EndRegister()
    Move_Register('GrenadeB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(550000, 1200000, -200000, 150000, 250, 10)
    Move_EndRegister()
    Move_Register('GrenadeC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown14015(0, 1200000, -200000, 150000, 150, 10)
    Move_EndRegister()
    Move_Register('AirGrenadeA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown14015(0, 650000, -300000, 50000, 500, 25)
    Move_EndRegister()
    Move_Register('AirGrenadeB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown14015(450000, 1100000, -300000, 50000, 250, 20)
    Move_EndRegister()
    Move_Register('AirGrenadeC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown14015(0, 1200000, -300000, 50000, 150, 10)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(1)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14013('CmnActInvincibleAttack')
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateBeam', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(1)
    Unknown15012(1)
    Unknown15013(2000)
    Unknown15014(10000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(350000, 2000000, -200000, 350000, 50, 1)
    Move_EndRegister()
    Move_Register('UltimateBeamSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(1)
    Unknown15012(1)
    Unknown15013(2000)
    Unknown15014(10000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(350000, 2000000, -200000, 350000, 50, 1)
    Move_EndRegister()
    Move_Register('UltimateRush', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(350000, 800000, -200000, 250000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateRushSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(350000, 800000, -200000, 250000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 900000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A_2nd', 10000000)
    Unknown15024('NmlAtk5A_2nd', 'NmlAtk5A_3rd', 10000000)
    Unknown15024('NmlAtk5A_3rd', 'NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B_2nd', 10000000)
    Unknown15024('NmlAtk5B_2nd', 'ShotBeamC', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2B', 'DashAtack', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5B', 'AirShotBeamB', 10000000)
    Unknown15024('NmlAtkAIR5C', 'ShotBeamA', 10000000)
    Unknown15024('NmlAtkAIR5C', 'ShotBeamB', 10000000)
    Unknown30093(1, 1, 95, 0, 0)
    Unknown3060('0000000076725f6c61796572303000000000000000000000000000000000000000000000')
    Unknown3061(0, 5)
    Unknown3063(0, 0)
    Unknown3062(0, 548000)
    Unknown12018(0, 'ubl062_01')
    Unknown12018(1, 'ubl062_01')
    Unknown12018(2, 'ubl062_01')
    Unknown12018(3, 'ubl062_01')
    Unknown12018(4, 'ubl062_01')
    Unknown12018(5, 'ubl062_01')
    Unknown12018(6, 'ubl062_01')
    Unknown12018(7, 'ubl040_00')
    Unknown12018(8, 'ubl040_00')
    Unknown12018(9, 'ubl045_01')
    Unknown12018(10, 'ubl000_00')
    Unknown12018(11, 'ubl062_01')
    Unknown12018(12, 'ubl062_01')
    Unknown12018(13, 'ubl062_01')
    Unknown12018(14, 'ubl063_02')
    Unknown12018(15, 'ubl063_04')
    Unknown12018(16, 'ubl050_00')
    Unknown12018(17, 'ubl054_00')
    Unknown12018(18, 'ubl062_00')
    Unknown12018(25, 'ubl063_00')
    Unknown12018(26, 'ubl063_01')
    Unknown12018(27, 'ubl063_02')
    Unknown12018(28, 'ubl063_02')
    Unknown12018(29, 'ubl063_04')
    Unknown12018(24, 'ubl073_02')
    Unknown7010(0, 'ubl000')
    Unknown7010(1, 'ubl001')
    Unknown7010(2, 'ubl002')
    Unknown7010(3, 'ubl003')
    Unknown7010(4, 'ubl004')
    Unknown7010(5, 'ubl005')
    Unknown7010(6, 'ubl006')
    Unknown7010(7, 'ubl007')
    Unknown7010(8, 'ubl008')
    Unknown7010(9, 'ubl009')
    Unknown7010(10, 'ubl010')
    Unknown7010(15, 'ubl011')
    Unknown7010(16, 'ubl012')
    Unknown7010(17, 'ubl013')
    Unknown7010(18, 'ubl014')
    Unknown7010(19, 'ubl015')
    Unknown7010(20, 'ubl016')
    Unknown7010(21, 'ubl017')
    Unknown7010(22, 'ubl018')
    Unknown7010(23, 'ubl019')
    Unknown7010(24, 'ubl020')
    Unknown7010(25, 'ubl021')
    Unknown7010(28, 'ubl022')
    Unknown7010(29, 'ubl023')
    Unknown7010(30, 'ubl024')
    Unknown7010(31, 'ubl025')
    Unknown7010(32, 'ubl026')
    Unknown7010(33, 'ubl027')
    Unknown7010(34, 'ubl028')
    Unknown7010(35, 'ubl029')
    Unknown7010(36, 'ubl030')
    Unknown7010(37, 'ubl031')
    Unknown7010(39, 'ubl032')
    Unknown7010(42, 'ubl033')
    Unknown7010(43, 'ubl034')
    Unknown7010(44, 'ubl035')
    Unknown7010(45, 'ubl036')
    Unknown7010(46, 'ubl037')
    Unknown7010(47, 'ubl038')
    Unknown7010(48, 'ubl039')
    Unknown7010(49, 'ubl040')
    Unknown7010(50, 'ubl041')
    Unknown7010(52, 'ubl042')
    Unknown7010(53, 'ubl043')
    Unknown7010(54, 'ubl100_0')
    Unknown7010(55, 'ubl100_1')
    Unknown7010(56, 'ubl100_2')
    Unknown7010(63, 'ubl101_0')
    Unknown7010(64, 'ubl101_1')
    Unknown7010(65, 'ubl101_2')
    Unknown7010(57, 'ubl102_0')
    Unknown7010(58, 'ubl102_1')
    Unknown7010(59, 'ubl102_2')
    Unknown7010(66, 'ubl103_0')
    Unknown7010(67, 'ubl103_1')
    Unknown7010(68, 'ubl103_2')
    Unknown7010(60, 'ubl104_0')
    Unknown7010(61, 'ubl104_1')
    Unknown7010(62, 'ubl104_2')
    Unknown7010(69, 'ubl105_0')
    Unknown7010(70, 'ubl105_1')
    Unknown7010(71, 'ubl105_2')
    Unknown7010(72, 'ubl150')
    Unknown7010(73, 'ubl151')
    Unknown7010(74, 'ubl152')
    Unknown7010(85, 'ubl153')
    Unknown7010(87, 'ubl154')
    Unknown7010(88, 'ubl155')
    Unknown7010(96, 'ubl161_0')
    Unknown7010(97, 'ubl161_1')
    Unknown7010(92, 'ubl162_0')
    Unknown7010(93, 'ubl162_1')
    Unknown7010(98, 'ubl163_0')
    Unknown7010(99, 'ubl163_1')
    Unknown7010(100, 'ubl164_0')
    Unknown7010(101, 'ubl164_1')
    Unknown7010(105, 'ubl165_0')
    Unknown7010(106, 'ubl165_1')
    Unknown7010(102, 'ubl166_0')
    Unknown7010(103, 'ubl166_1')
    Unknown7010(90, 'ubl167_0')
    Unknown7010(91, 'ubl167_1')
    Unknown7010(107, 'ubl168_0')
    Unknown7010(108, 'ubl168_1')
    Unknown7010(110, 'ubl169_0')
    Unknown7010(111, 'ubl169_1')
    Unknown7010(112, 'ubl159_0')
    Unknown7010(113, 'ubl159_1')
    Unknown7010(94, 'ubl400_0')
    Unknown7010(95, 'ubl400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174654265616d0000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d6174654265616d5350000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465527573680000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465527573685350000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def MatchInit2():
    if SLOT_100:
        Health(40000)

@Subroutine
def CheckAtemiMuteki():
    SLOT_59 = 1
    if Unknown23145('CmnActInvincibleAttack'):
        setInvincibleFor(3)
        SLOT_4 = 1
    if Unknown23145('InvincibleAttack2nd'):
        setInvincibleFor(3)
        SLOT_4 = 0

    def upon_45():
        if (SLOT_18 > 3):
            clearUponHandler(45)
            SLOT_4 = 0

@Subroutine
def UniqueZLine():
    Unknown2019(10)
    if SLOT_158:
        Unknown2020(300)

@Subroutine
def UniqueZLineSpecial():
    Unknown2019(10)
    if SLOT_158:
        Unknown2020(300)

@Subroutine
def UniqueZLineUltimate():
    Unknown2019(10)

@State
def CmnActStand():

    def upon_IMMEDIATE():
        callSubroutine('UniqueZLine')
    label(0)
    sprite('ubl000_00', 1)	# 1-1
    sprite('ubl000_01', 1)	# 2-2
    sprite('ubl000_02', 1)	# 3-3
    sprite('ubl000_03', 1)	# 4-4
    sprite('ubl000_04', 1)	# 5-5
    sprite('ubl000_05', 1)	# 6-6
    sprite('ubl000_06', 1)	# 7-7
    sprite('ubl000_07', 1)	# 8-8
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 100)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('ubl000_00', 4)	# 9-12
    SLOT_88 = 960
    loopRest()
    gotoLabel(0)

@State
def ReactionFBrake():

    def upon_IMMEDIATE():
        callSubroutine('InitBrakeCancel')
    sprite('ubl004_00', 2)	# 1-2
    sprite('ubl004_01', 2)	# 3-4
    sprite('ubl004_02', 6)	# 5-10
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 6)	# 11-16
    sprite('ubl004_04', 6)	# 17-22
    sprite('ubl004_05', 6)	# 23-28
    sprite('ubl004_06', 6)	# 29-34
    sprite('ubl004_07', 6)	# 35-40
    sprite('ubl004_08', 6)	# 41-46

@State
def ReactionBBrake():

    def upon_IMMEDIATE():
        callSubroutine('InitBrakeCancel')
    sprite('ubl005_00', 6)	# 1-6
    sprite('ubl005_01', 6)	# 7-12
    sprite('ubl005_02', 6)	# 13-18
    sprite('ubl005_03', 6)	# 19-24
    sprite('ubl005_04', 6)	# 25-30
    sprite('ubl005_05', 3)	# 31-33
    sprite('ubl005_06', 3)	# 34-36
    sprite('ubl005_07', 3)	# 37-39
    sprite('ubl005_08', 3)	# 40-42

@Subroutine
def InitBrakeCancel():
    Unknown17013()
    Unknown13001(1)
    Unknown13002(1)
    Unknown13003(1)
    Unknown13005(1)
    Unknown13006(1)
    Unknown13014(1)
    Unknown13015(1)
    Unknown13031(1)
    Unknown13008(1)
    Unknown13016(1)
    Unknown13021(1)
    Unknown13019(1)
    Unknown13029(1)
    Unknown13028(1)

@State
def CmnActStandTurn():
    sprite('ubl003_00', 3)	# 1-3
    sprite('ubl003_02', 3)	# 4-6
    sprite('ubl003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():

    def upon_IMMEDIATE():
        callSubroutine('UniqueZLine')
    sprite('ubl010_00', 2)	# 1-2
    sprite('ubl010_01', 2)	# 3-4
    SFX_3('ublse_02')
    sprite('ubl010_02', 2)	# 5-6
    sprite('ubl010_03', 2)	# 7-8

@State
def CmnActCrouch():

    def upon_IMMEDIATE():
        callSubroutine('UniqueZLine')
    label(0)
    sprite('ubl010_04', 1)	# 1-1
    sprite('ubl010_05', 1)	# 2-2
    sprite('ubl010_06', 1)	# 3-3
    sprite('ubl010_07', 1)	# 4-4
    sprite('ubl010_08', 1)	# 5-5
    sprite('ubl010_09', 1)	# 6-6
    sprite('ubl010_10', 1)	# 7-7
    sprite('ubl010_11', 1)	# 8-8
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ubl013_00', 3)	# 1-3
    sprite('ubl013_02', 3)	# 4-6
    sprite('ubl013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('ubl010_03', 2)	# 1-2
    sprite('ubl010_02', 2)	# 3-4
    sprite('ubl010_01', 2)	# 5-6
    sprite('ubl010_00', 2)	# 7-8

@State
def CmnActJumpPre():
    if SLOT_37:
        if SLOT_93:
            if SLOT_16:
                pass
    sprite('ubl010_00', 6)	# 1-6

@State
def CmnActJumpUpper():
    label(0)
    sprite('ubl020_00', 3)	# 1-3
    sprite('ubl020_01', 3)	# 4-6
    sprite('ubl020_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ubl020_00', 3)	# 1-3
    sprite('ubl020_01', 3)	# 4-6
    sprite('ubl020_02', 3)	# 7-9

@State
def CmnActJumpDown():
    label(0)
    sprite('ubl020_00', 3)	# 1-3
    sprite('ubl020_01', 3)	# 4-6
    sprite('ubl020_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ubl252_14', 6)	# 1-6
    ScreenShake(0, 10000)
    GFX_1('ublef_landing_pos', 100)
    SFX_3('ublse_16')
    sprite('ubl252_15', 4)	# 7-10
    sprite('ubl252_16', 4)	# 11-14

@State
def CmnActLandingStiffLoop():
    sprite('ubl010_00', 2)	# 1-2
    sprite('ubl010_01', 32767)	# 3-32769

@State
def CmnActLandingStiffEnd():
    sprite('ubl010_00', 3)	# 1-3
    sprite('ubl010_00', 3)	# 4-6

@State
def CmnActFWalk():
    if Unknown23145('ReactionFBrake'):
        gotoLabel(1)
    if Unknown23145('ReactionBBrake'):
        gotoLabel(2)
    gotoLabel(0)
    label(1)
    sprite('ubl403_01', 3)	# 1-3
    sprite('ubl403_00', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('ubl005_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    label(0)
    sprite('ubl030_00', 1)	# 10-10
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_01', 1)	# 11-11
    SFX_3('ublse_00')
    sprite('ubl030_02', 1)	# 12-12
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_03', 1)	# 13-13
    sprite('ubl030_04', 1)	# 14-14
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_05', 1)	# 15-15
    sprite('ubl030_06', 1)	# 16-16
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_07', 1)	# 17-17
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    if Unknown23145('ReactionFBrake'):
        gotoLabel(1)
    if Unknown23145('ReactionBBrake'):
        gotoLabel(2)
    gotoLabel(0)
    label(1)
    sprite('ubl403_01', 3)	# 1-3
    sprite('ubl403_00', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('ubl005_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    label(0)
    sprite('ubl030_07', 1)	# 10-10
    GFX_0('ubl_backward_Eff', 100)
    sprite('ubl030_06', 1)	# 11-11
    SFX_3('ublse_00')
    sprite('ubl030_05', 1)	# 12-12
    GFX_0('ubl_backward_Eff', 100)
    sprite('ubl030_04', 1)	# 13-13
    sprite('ubl030_03', 1)	# 14-14
    GFX_0('ubl_backward_Eff', 100)
    sprite('ubl030_01', 1)	# 15-15
    sprite('ubl030_00', 1)	# 16-16
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    label(0)
    sprite('ubl030_00', 1)	# 1-1
    sprite('ubl030_01', 1)	# 2-2
    sprite('ubl030_02', 1)	# 3-3
    sprite('ubl030_03', 1)	# 4-4
    sprite('ubl030_04', 1)	# 5-5
    sprite('ubl030_05', 1)	# 6-6
    sprite('ubl030_06', 1)	# 7-7
    sprite('ubl030_07', 1)	# 8-8
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():

    def upon_IMMEDIATE():
        Unknown13019(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 4):
                Unknown13005(1)
                Unknown13001(1)
    sprite('ubl032_10', 3)	# 1-3
    sprite('ubl032_11', 3)	# 4-6
    sprite('ubl032_12', 3)	# 7-9
    sprite('ubl032_13', 3)	# 10-12
    sprite('ubl032_14', 3)	# 13-15

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown1084(1)
        Unknown23076()
        setInvincibleFor(7)
    sprite('ubl033_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    GFX_0('ubl_BDash_Eff', 100)
    sprite('ubl033_00', 2)	# 3-4
    SFX_3('ublse_01')
    physicsXImpulse(-24000)
    GFX_0('ubl_BDash_Eff', 100)
    sprite('ubl033_01', 4)	# 5-8
    Unknown1019(40)
    GFX_0('ubl_BDash_Eff', 100)
    SFX_3('ublse_00')
    sprite('ubl033_02', 3)	# 9-11
    GFX_0('ubl_BDash_Eff', 100)
    sprite('ubl033_03', 3)	# 12-14
    Unknown1019(40)
    GFX_0('ubl_BDash_Eff', 100)
    SFX_3('ublse_00')
    sprite('ubl033_04', 3)	# 15-17
    GFX_0('ubl_BDash_Eff', 100)
    sprite('ubl033_02', 3)	# 18-20
    GFX_0('ubl_BDash_Eff', 100)
    sprite('ubl033_03', 3)	# 21-23
    Unknown1019(0)
    sprite('keep', 1)	# 24-24
    enterState('ReactionBBrake')

@State
def CmnActBDashLanding():
    sprite('ny033_05', 4)	# 1-4
    sprite('ny033_06', 4)	# 5-8

@State
def CmnActAirFDash():
    sprite('ubl035_00', 2)	# 1-2
    label(0)
    sprite('ubl035_01', 3)	# 3-5
    sprite('ubl035_02', 3)	# 6-8
    sprite('ubl035_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ubl033_00', 3)	# 1-3
    label(0)
    sprite('ubl033_01', 3)	# 4-6
    sprite('ubl033_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ubl050_00', 1)	# 1-1
    sprite('ubl050_01', 1)	# 2-2
    sprite('ubl050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ubl050_01', 1)	# 1-1
    sprite('ubl050_02', 1)	# 2-2
    sprite('ubl050_01', 2)	# 3-4
    sprite('ubl050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ubl050_02', 1)	# 1-1
    sprite('ubl050_02', 1)	# 2-2
    sprite('ubl050_02', 2)	# 3-4
    sprite('ubl050_01', 2)	# 5-6
    sprite('ubl050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ubl050_02', 1)	# 1-1
    sprite('ubl050_03', 1)	# 2-2
    sprite('ubl050_02', 2)	# 3-4
    sprite('ubl050_02', 2)	# 5-6
    sprite('ubl050_01', 2)	# 7-8
    sprite('ubl050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ubl050_03', 1)	# 1-1
    sprite('ubl050_03', 1)	# 2-2
    sprite('ubl050_03', 2)	# 3-4
    sprite('ubl050_02', 2)	# 5-6
    sprite('ubl050_02', 2)	# 7-8
    sprite('ubl050_01', 2)	# 9-10
    sprite('ubl050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ubl052_00', 1)	# 1-1
    sprite('ubl052_01', 1)	# 2-2
    sprite('ubl052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ubl052_01', 1)	# 1-1
    sprite('ubl052_02', 1)	# 2-2
    sprite('ubl052_01', 2)	# 3-4
    sprite('ubl052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ubl052_02', 1)	# 1-1
    sprite('ubl052_02', 1)	# 2-2
    sprite('ubl052_02', 2)	# 3-4
    sprite('ubl052_01', 2)	# 5-6
    sprite('ubl052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ubl052_02', 1)	# 1-1
    sprite('ubl052_03', 1)	# 2-2
    sprite('ubl052_02', 2)	# 3-4
    sprite('ubl052_02', 2)	# 5-6
    sprite('ubl052_01', 2)	# 7-8
    sprite('ubl052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ubl052_03', 1)	# 1-1
    sprite('ubl052_03', 1)	# 2-2
    sprite('ubl052_03', 2)	# 3-4
    sprite('ubl052_02', 2)	# 5-6
    sprite('ubl052_02', 2)	# 7-8
    sprite('ubl052_01', 2)	# 9-10
    sprite('ubl052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ubl054_00', 1)	# 1-1
    sprite('ubl054_01', 1)	# 2-2
    sprite('ubl054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ubl054_01', 1)	# 1-1
    sprite('ubl054_02', 1)	# 2-2
    sprite('ubl054_01', 2)	# 3-4
    sprite('ubl054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ubl054_02', 1)	# 1-1
    sprite('ubl054_02', 1)	# 2-2
    sprite('ubl054_02', 2)	# 3-4
    sprite('ubl054_01', 2)	# 5-6
    sprite('ubl054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ubl054_02', 1)	# 1-1
    sprite('ubl054_03', 1)	# 2-2
    sprite('ubl054_02', 2)	# 3-4
    sprite('ubl054_02', 2)	# 5-6
    sprite('ubl054_01', 2)	# 7-8
    sprite('ubl054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ubl054_03', 1)	# 1-1
    sprite('ubl054_03', 1)	# 2-2
    sprite('ubl054_03', 2)	# 3-4
    sprite('ubl054_02', 2)	# 5-6
    sprite('ubl054_02', 2)	# 7-8
    sprite('ubl054_01', 2)	# 9-10
    sprite('ubl054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ubl062_00', 3)	# 1-3
    label(0)
    sprite('ubl062_01', 3)	# 4-6
    sprite('ubl062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ubl062_03', 2)	# 1-2
    sprite('ubl062_04', 2)	# 3-4

@State
def CmnActBDownDown():
    sprite('ubl062_05', 3)	# 1-3
    sprite('ubl062_06', 3)	# 4-6
    label(0)
    sprite('ubl062_07', 3)	# 7-9
    sprite('ubl062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ubl062_09', 2)	# 1-2
    sprite('ubl062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('ubl063_05', 2)	# 1-2
    sprite('ubl063_06', 2)	# 3-4
    sprite('ubl063_07', 2)	# 5-6
    sprite('ubl063_08', 3)	# 7-9
    sprite('ubl063_09', 3)	# 10-12

@State
def CmnActBDownLoop():
    sprite('ubl063_08', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('ubl061_00', 3)	# 1-3
    SFX_0('205_runjump_garden_0')
    sprite('ubl061_01', 3)	# 4-6
    sprite('ubl061_02', 3)	# 7-9
    sprite('ubl061_03', 3)	# 10-12
    sprite('ubl061_04', 3)	# 13-15
    sprite('ubl061_05', 3)	# 16-18
    sprite('ubl061_06', 3)	# 19-21
    sprite('ubl061_07', 3)	# 22-24
    sprite('ubl061_08', 2)	# 25-26
    sprite('ubl061_09', 2)	# 27-28

@State
def CmnActFDownUpper():
    sprite('ubl063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ubl063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ubl063_02', 3)	# 1-3
    sprite('ubl063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ubl063_04', 3)	# 1-3
    sprite('ubl063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('ubl063_05', 2)	# 1-2
    sprite('ubl063_06', 2)	# 3-4
    sprite('ubl063_07', 3)	# 5-7
    sprite('ubl063_08', 3)	# 8-10
    sprite('ubl063_09', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('ubl063_09', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ubl064_00', 2)	# 1-2
    sprite('ubl064_01', 3)	# 3-5
    sprite('ubl064_02', 3)	# 6-8
    sprite('ubl064_03', 3)	# 9-11
    sprite('ubl010_02', 3)	# 12-14
    sprite('ubl010_01', 3)	# 15-17
    sprite('ubl010_00', 3)	# 18-20

@State
def CmnActVDownUpper():
    sprite('ubl062_00', 3)	# 1-3
    label(0)
    sprite('ubl062_01', 3)	# 4-6
    sprite('ubl062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ubl062_03', 2)	# 1-2
    sprite('ubl062_04', 2)	# 3-4

@State
def CmnActVDownDown():
    sprite('ubl062_05', 3)	# 1-3
    sprite('ubl062_06', 3)	# 4-6
    label(0)
    sprite('ubl062_07', 3)	# 7-9
    sprite('ubl062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ubl063_04', 3)	# 1-3
    sprite('ubl063_05', 3)	# 4-6

@State
def CmnActBlowoff():
    sprite('ubl062_06', 3)	# 1-3
    label(0)
    sprite('ubl062_07', 3)	# 4-6
    sprite('ubl062_08', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    sprite('ubl062_06', 3)	# 1-3
    label(0)
    sprite('ubl062_07', 3)	# 4-6
    sprite('ubl062_08', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('null', 1)	# 1-1

@State
def CmnActFreeze():
    sprite('ubl062_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ubl073_00', 3)	# 1-3
    sprite('ubl073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('ubl073_03', 3)	# 1-3
    label(0)
    sprite('ubl062_07', 3)	# 4-6
    sprite('ubl062_08', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ubl070_00', 3)	# 1-3
    label(0)
    sprite('ubl070_01', 4)	# 4-7
    sprite('ubl070_02', 4)	# 8-11
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('ubl070_03', 8)	# 1-8
    sprite('ubl070_04', 8)	# 9-16
    sprite('ubl070_05', 8)	# 17-24

@State
def CmnActUkemiStagger():
    sprite('ubl070_06', 3)	# 1-3
    sprite('ubl070_07', 2)	# 4-5
    sprite('ubl070_08', 2)	# 6-7

@State
def CmnActUkemiAirF():
    sprite('ubl113_00', 3)	# 1-3
    sprite('ubl113_01', 3)	# 4-6
    sprite('ubl113_00', 3)	# 7-9
    sprite('ubl113_01', 3)	# 10-12
    sprite('ubl113_00', 3)	# 13-15

@State
def CmnActUkemiAirB():
    sprite('ubl113_00', 3)	# 1-3
    sprite('ubl113_01', 3)	# 4-6
    sprite('ubl113_00', 3)	# 7-9
    sprite('ubl113_01', 3)	# 10-12
    sprite('ubl113_00', 3)	# 13-15

@State
def CmnActUkemiAirN():
    sprite('ubl113_00', 3)	# 1-3
    sprite('ubl113_01', 3)	# 4-6
    sprite('ubl113_00', 3)	# 7-9
    sprite('ubl113_01', 3)	# 10-12
    sprite('ubl113_00', 3)	# 13-15

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
    sprite('null', 1)	# 1-1

@State
def CmnActUkemiLandN():
    sprite('ubl112_00', 3)	# 1-3
    sprite('ubl112_01', 3)	# 4-6
    sprite('ubl112_02', 3)	# 7-9
    sprite('ubl112_03', 3)	# 10-12
    sprite('ubl112_04', 3)	# 13-15
    label(0)
    sprite('ubl020_00', 2)	# 16-17
    sprite('ubl020_01', 2)	# 18-19
    sprite('ubl020_01', 2)	# 20-21
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('ubl010_00', 3)	# 1-3
    SFX_3('ublse_16')
    sprite('ubl010_01', 3)	# 4-6
    sprite('ubl010_02', 3)	# 7-9
    sprite('ubl010_01', 3)	# 10-12
    sprite('ubl010_00', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('ubl040_00', 6)	# 1-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ubl040_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ubl040_00', 6)	# 1-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('ubl040_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ubl040_00', 6)	# 1-6

@State
def CmnActHighGuardPre():
    sprite('ubl040_00', 6)	# 1-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ubl040_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ubl040_01', 3)	# 1-3
    sprite('ubl040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('ubl040_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ubl040_00', 6)	# 1-6

@State
def CmnActCrouchGuardPre():
    sprite('ubl043_00', 6)	# 1-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ubl043_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ubl043_00', 6)	# 1-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('ubl043_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ubl043_00', 6)	# 1-6

@State
def CmnActAirGuardPre():
    sprite('ubl045_00', 6)	# 1-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ubl045_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ubl045_00', 6)	# 1-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('ubl045_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ubl045_00', 6)	# 1-6

@State
def CmnActGuardBreakStand():
    sprite('ubl040_01', 5)	# 1-5
    Unknown2042(1)
    sprite('ubl040_00', 12)	# 6-17

@State
def CmnActGuardBreakCrouch():
    sprite('ubl043_04', 2)	# 1-2
    sprite('ubl043_04', 2)	# 3-4
    sprite('ubl043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ubl043_02', 4)	# 6-9
    sprite('ubl043_01', 4)	# 10-13
    sprite('ubl043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ubl045_04', 2)	# 1-2
    sprite('ubl045_04', 2)	# 3-4
    sprite('ubl045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ubl045_02', 4)	# 6-9
    sprite('ubl045_01', 4)	# 10-13
    sprite('ubl045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('ubl025_00', 2)	# 1-2
    sprite('ubl025_01', 2)	# 3-4
    sprite('ubl025_02', 4)	# 5-8
    sprite('ubl025_01ex01', 2)	# 9-10
    sprite('ubl025_00ex01', 2)	# 11-12

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():

    def upon_IMMEDIATE():
        callSubroutine('UniqueZLine')
    sprite('ubl200_00ex', 3)	# 1-3	 **attackbox here**
    sprite('ubl200_01ex', 2)	# 4-5	 **attackbox here**
    sprite('ubl200_02ex', 3)	# 6-8	 **attackbox here**
    sprite('ubl200_03ex', 3)	# 9-11	 **attackbox here**
    sprite('ubl200_03ex', 3)	# 12-14	 **attackbox here**
    sprite('ubl200_03ex', 3)	# 15-17	 **attackbox here**
    sprite('ubl200_04ex', 3)	# 18-20	 **attackbox here**
    sprite('ubl200_05ex', 4)	# 21-24	 **attackbox here**
    sprite('ubl200_06ex', 4)	# 25-28	 **attackbox here**

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
    sprite('ubl077_00', 2)	# 1-2
    sprite('ubl077_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    label(0)
    sprite('ubl077_00', 2)	# 1-2
    sprite('ubl077_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ubl077_02', 3)	# 1-3
    sprite('ubl077_03', 3)	# 4-6
    sprite('ubl077_04', 3)	# 7-9

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
    sprite('ubl333_00', 3)	# 1-3
    sprite('ubl333_01', 3)	# 4-6
    sprite('ubl333_02', 32767)	# 7-32773
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ubl333_03', 2)	# 1-2
    sprite('ubl333_04', 2)	# 3-4
    GFX_0('ubl_Eye00_Eff', 0)
    GFX_0('ubl_Eye01_Eff', 1)
    sprite('ubl333_05', 2)	# 5-6
    sprite('ubl333_06', 2)	# 7-8
    label(0)
    sprite('ubl333_04', 2)	# 9-10
    sprite('ubl333_05', 2)	# 11-12
    sprite('ubl333_06', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('ubl333_07', 4)	# 5-8
    sprite('ubl333_08', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('ubl333_09', 3)	# 1-3
    sprite('ubl333_01', 3)	# 4-6
    sprite('ubl333_02', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ubl333_03', 2)	# 1-2
    sprite('ubl333_04', 2)	# 3-4
    GFX_0('ubl_Eye00_Eff', 0)
    GFX_0('ubl_Eye01_Eff', 1)
    sprite('ubl333_05', 2)	# 5-6
    sprite('ubl333_06', 2)	# 7-8
    label(0)
    sprite('ubl333_04', 2)	# 9-10
    sprite('ubl333_05', 2)	# 11-12
    sprite('ubl333_06', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ubl333_10', 3)	# 1-3
    sprite('ubl333_11', 3)	# 4-6
    label(0)
    sprite('ubl020_00', 3)	# 7-9
    sprite('ubl020_01', 3)	# 10-12
    sprite('ubl020_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ubl333_00', 3)	# 1-3
    sprite('ubl333_01', 3)	# 4-6
    sprite('ubl333_02', 32767)	# 7-32773
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ubl333_03', 2)	# 1-2
    label(0)
    sprite('ubl333_04', 2)	# 3-4
    sprite('ubl333_05', 2)	# 5-6
    sprite('ubl333_06', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('ubl333_07', 4)	# 5-8
    sprite('ubl333_08', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('ubl333_09', 3)	# 1-3
    sprite('ubl333_01', 3)	# 4-6
    sprite('ubl333_02', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ubl333_03', 2)	# 1-2
    label(0)
    sprite('ubl333_04', 2)	# 3-4
    sprite('ubl333_05', 2)	# 5-6
    sprite('ubl333_06', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ubl333_10', 3)	# 1-3
    sprite('ubl333_11', 3)	# 4-6
    label(0)
    sprite('ubl020_00', 3)	# 7-9
    sprite('ubl020_01', 3)	# 10-12
    sprite('ubl020_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('ubl333_00', 3)	# 1-3
    sprite('ubl333_01', 3)	# 4-6
    sprite('ubl333_02', 32767)	# 7-32773
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('ubl333_03', 2)	# 1-2
    label(0)
    sprite('ubl333_04', 2)	# 3-4
    sprite('ubl333_05', 2)	# 5-6
    sprite('ubl333_06', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('keep', 4)	# 1-4
    sprite('ubl333_07', 4)	# 5-8
    sprite('ubl333_08', 4)	# 9-12

@State
def CmnActAirCrossChangeBegin():
    sprite('ubl333_09', 3)	# 1-3
    sprite('ubl333_01', 3)	# 4-6
    sprite('ubl333_02', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('ubl333_03', 2)	# 1-2
    label(0)
    sprite('ubl333_04', 2)	# 3-4
    sprite('ubl333_05', 2)	# 5-6
    sprite('ubl333_06', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ubl333_10', 3)	# 1-3
    sprite('ubl333_11', 3)	# 4-6
    label(0)
    sprite('ubl020_00', 3)	# 7-9
    sprite('ubl020_01', 3)	# 10-12
    sprite('ubl020_02', 3)	# 13-15
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
        Unknown9015(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            sendToLabel(2)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 28)	# 603-630
    label(0)
    sprite('ubl252_00', 2)	# 631-632
    Unknown1086(22)
    teleportRelativeX(-130000)
    teleportRelativeY(1500000)
    physicsYImpulse(-300000)
    setGravity(0)
    Unknown2053(1)
    EnableCollision(1)
    SFX_3('ublse_23')
    sprite('ubl252_01', 2)	# 633-634	 **attackbox here**
    label(1)
    sprite('ubl252_02', 3)	# 635-637	 **attackbox here**
    sprite('ubl252_03', 3)	# 638-640	 **attackbox here**
    sprite('ubl252_01', 3)	# 641-643	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ubl252_03', 4)	# 644-647	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 30000)
    sprite('ubl252_13', 7)	# 648-654
    sprite('ubl252_14', 4)	# 655-658
    sprite('ubl252_15', 5)	# 659-663
    sprite('ubl252_16', 5)	# 664-668

@State
def CmnActChangePartnerQuickIn():
    sprite('ubl004_01', 2)	# 1-2
    sprite('ubl004_02', 3)	# 3-5
    GFX_0('ubl_Brake_Eff', 100)
    SFX_3('ublse_04')
    SFX_3('ublse_15')
    SFX_3('ublse_23')
    sprite('ubl004_03', 4)	# 6-9
    sprite('ubl004_04', 4)	# 10-13
    sprite('ubl004_05', 4)	# 14-17
    sprite('ubl004_06', 4)	# 18-21
    sprite('ubl004_07', 4)	# 22-25
    sprite('ubl004_08', 4)	# 26-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ubl010_00', 3)	# 1-3
    sprite('ubl020_00', 3)	# 4-6
    sprite('ubl020_01', 3)	# 7-9
    sprite('ubl020_02', 3)	# 10-12
    sprite('ubl020_00', 3)	# 13-15
    sprite('ubl020_01', 3)	# 16-18
    sprite('ubl020_02', 3)	# 19-21
    sprite('ubl020_00', 3)	# 22-24
    sprite('ubl020_01', 3)	# 25-27
    sprite('ubl020_02', 3)	# 28-30
    loopRest()
    sprite('keep', 34)	# 31-64

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        callSubroutine('CheckAtemiMuteki')
    sprite('ubl033_00', 3)	# 1-3
    sprite('ubl033_01', 4)	# 4-7
    Unknown3001(255)
    Unknown3004(-42)
    physicsXImpulse(-4000)
    sprite('ubl033_02', 3)	# 8-10
    Unknown1019(40)
    sprite('ubl033_03', 3)	# 11-13
    Unknown1019(40)
    sprite('ubl033_04', 3)	# 14-16
    sprite('ubl033_02', 4)	# 17-20
    sprite('ubl033_03', 4)	# 21-24

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
        loopRelated(17, 55)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
    sprite('ubl300_00', 7)	# 1-7
    sprite('ubl300_01', 7)	# 8-14
    GFX_0('ublef_Idling_Eff', 0)
    GFX_0('ublef_smoke_Eff', 0)
    sprite('ubl300_02', 7)	# 15-21
    GFX_0('ublef_Idling_Eff', 0)
    label(0)
    sprite('ubl300_03', 1)	# 22-22
    sprite('ubl300_04', 1)	# 23-23
    sprite('ubl300_05', 1)	# 24-24
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ubl300_06', 7)	# 25-31
    sprite('ubl300_07', 7)	# 32-38
    sprite('ubl300_08', 7)	# 39-45
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
    sprite('ubl020_00', 3)	# 3-5
    Unknown1019(95)
    sprite('ubl020_01', 3)	# 6-8
    Unknown1019(95)
    sprite('ubl020_02', 3)	# 9-11
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ubl010_01', 2)	# 12-13
    Unknown8000(100, 1, 1)
    SFX_3('ublse_16')
    sprite('keep', 100)	# 14-113

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()
    sprite('ubl400_10', 8)	# 1-8
    sprite('ubl400_11', 7)	# 9-15
    sprite('ubl400_12', 7)	# 16-22
    sprite('ubl400_13', 6)	# 23-28
    sprite('ubl400_14', 1)	# 29-29
    GFX_0('ShotBeam_Middle', 0)
    Unknown23029(1, 1101, 0)
    SFX_3('ublse_07')
    sprite('ubl400_14', 3)	# 30-32
    sprite('ubl400_14', 5)	# 33-37
    sprite('ubl400_15', 6)	# 38-43
    sprite('ubl400_16', 6)	# 44-49
    sprite('ubl400_17', 6)	# 50-55
    sprite('ubl400_18', 6)	# 56-61
    sprite('ubl400_19', 6)	# 62-67

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(750)
        AttackP1(70)
        AttackP2(85)
        Unknown11001(0, 0, 0)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Hitstop(2)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9266(6)
        Unknown2006()
        callSubroutine('AtkEffLightning')
        Unknown2021(1)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ubl320_00', 2)	# 1-2
    sprite('ubl320_01', 2)	# 3-4
    sprite('ubl320_02', 3)	# 5-7
    SFX_3('ublse_20')
    sprite('ubl320_03', 2)	# 8-9
    GFX_0('ubl_320_NearSpark_Eff', 100)
    GFX_0('ubl_310_BackSpark_Eff', 100)
    SFX_0('014_electric_sl')
    SFX_0('014_electric_sl')
    Unknown23119(4128831, 3, -1)
    sprite('ubl320_04', 1)	# 10-10	 **attackbox here**
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_05', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_06', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_07', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_05', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_07', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_07', 10)	# 23-32	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown26('ubl_310_NearSpark_Eff')
    Unknown26('ubl_310_BackSpark_Eff')
    SFX_0('014_electric_s')
    SFX_0('014_electric_m')
    sprite('ubl320_05', 7)	# 33-39	 **attackbox here**
    sprite('ubl320_08', 12)	# 40-51
    sprite('ubl320_09', 10)	# 52-61

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2200)
        AttackP1(70)
        Hitstop(20)
        AirPushbackX(2500)
        AirPushbackY(40000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(35000)
        AirUntechableTime(60)
        Unknown11032('d0dd0600ffffffffffffffffffffffff')
        Unknown11056(0)
        ScreenShake(4000, 4000)
        Unknown30040(1)
        Unknown2006()
        Unknown11042(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)

        def upon_77():
            clearUponHandler(3)
            clearUponHandler(77)
            sendToLabel(9)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(4000, 4000)
    sprite('ubl431_00', 3)	# 1-3
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl431_01', 2)	# 4-5
    GFX_0('ubl_forward_Eff', 100)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 < 200000):
            clearUponHandler(3)
            SLOT_51 = 1
            Unknown1019(0)
            Unknown1045(50000)
    sprite('ubl431_02', 2)	# 6-7
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl431_03', 2)	# 8-9
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl431_04', 2)	# 10-11
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl431_09', 3)	# 12-14
    GFX_0('ubl_Dash_Eff', 100)
    physicsXImpulse(62000)
    SFX_3('ublse_01')
    sprite('ubl403_02', 3)	# 15-17	 **attackbox here**
    SFX_3('ublse_15')
    SFX_3('ublse_21')
    sprite('ubl403_03', 3)	# 18-20	 **attackbox here**
    if SLOT_51:
        sendToLabel(9)
    sprite('ubl403_04', 3)	# 21-23	 **attackbox here**
    loopRest()
    label(9)
    sprite('ubl004_00', 2)	# 24-25
    Unknown1019(10)
    clearUponHandler(3)
    clearUponHandler(77)
    setInvincible(0)
    DisableAttackRestOfMove()
    sprite('ubl004_01', 2)	# 26-27
    sprite('ubl004_02', 6)	# 28-33
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 6)	# 34-39
    sprite('ubl004_04', 6)	# 40-45
    physicsXImpulse(0)
    Unknown1045(0)
    Unknown26('ubl_Dash_Eff')
    sprite('ubl004_05', 6)	# 46-51
    sprite('ubl004_06', 6)	# 52-57
    sprite('ubl004_07', 6)	# 58-63
    sprite('ubl004_08', 6)	# 64-69

@State
def CmnActChangePartnerDD():

    def upon_IMMEDIATE():
        setInvincible(1)
        if SLOT_162:
            SLOT_58 = 1
        Unknown30063(1)
        Unknown30039(24)
        Unknown30040(1)
        Unknown30019('0000000002000000')

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('null', 1)	# 1-1
    Unknown2036(105, -1, 0)
    Unknown1086(24)
    EnableCollision(0)
    Unknown2053(0)
    Unknown2034(0)
    setInvincible(1)
    teleportRelativeY(0)
    Unknown30080('')
    sendToLabelUpon(2, 1)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-550000)
    Unknown1019(4)
    label(0)
    sprite('ubl020_00', 3)	# 3-5
    sprite('ubl020_01', 3)	# 6-8
    sprite('ubl020_02', 3)	# 9-11
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 12-21
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    SFX_3('ublse_16')
    Unknown30019('0000000001000000')
    if SLOT_58:
        enterState('ChangePartnerDDOD_Exe')
    else:
        enterState('ChangePartnerDD_Exe')

@State
def ChangePartnerDD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        Unknown1084(1)
        setInvincible(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 40):
                Unknown20000(0)
            if (SLOT_51 >= 7):
                clearUponHandler(3)
                sendToLabel(1)
        loopRelated(17, 166)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
        callSubroutine('UniqueZLineUltimate')
    sprite('ubl430_00', 3)	# 1-3
    sprite('ubl430_01', 3)	# 4-6
    sprite('ubl430_02', 3)	# 7-9
    SFX_3('ublse_03')
    SFX_3('ublse_03')
    sprite('ubl430_03', 3)	# 10-12
    Unknown20000(1)
    sprite('ubl430_04', 3)	# 13-15
    sprite('ubl430_05', 2)	# 16-17
    sprite('ubl430_06', 2)	# 18-19
    sprite('ubl430_07', 2)	# 20-21
    GFX_0('ubl_UltimateBeam_Charge_Eff', 0)
    SFX_3('ublse_14')
    SFX_3('ublse_14')
    SFX_3('ublse_12')
    SFX_3('ublse_12')
    sprite('ubl430_08', 2)	# 22-23
    sprite('ubl430_09', 2)	# 24-25
    GFX_0('ubl_UltimateBeam_Lightbullet_Ef', 0)
    label(0)
    sprite('ubl430_10', 3)	# 26-28
    SLOT_51 = (SLOT_51 + 1)
    sprite('ubl430_11', 3)	# 29-31
    sprite('ubl430_12', 3)	# 32-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl430_13', 3)	# 35-37
    Unknown26('ubl_UltimateBeam_Charge_Eff')
    Unknown26('ubl_UltimateBeam_Lightbullet_Ef')
    GFX_0('ubl_UltimateBeam_Eff', 0)
    GFX_0('ubl_UltimateBeam_Muzzle_Eff', 0)
    GFX_0('ubl_UltimateBeam_Wave_Eff', 0)
    GFX_0('UltimateBeam_AtkCol', 0)
    Unknown23029(1, 2002, 0)
    SFX_3('ublse_07')
    SFX_3('ublse_08')
    label(2)
    sprite('ubl430_14', 3)	# 38-40
    setInvincible(0)
    sprite('ubl430_15', 3)	# 41-43
    sprite('ubl430_16', 3)	# 44-46
    sprite('ubl430_13', 3)	# 47-49
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('ubl430_17', 3)	# 50-52
    SFX_3('ublse_02')
    sprite('ubl430_18', 3)	# 53-55
    sprite('ubl430_19', 3)	# 56-58
    sprite('ubl430_20', 3)	# 59-61
    sprite('ubl430_21', 3)	# 62-64
    sprite('ubl430_22', 3)	# 65-67
    sprite('ubl430_23', 3)	# 68-70
    SFX_3('ublse_04')
    sprite('ubl430_24', 3)	# 71-73
    sprite('ubl430_25', 3)	# 74-76
    sprite('ubl430_26', 3)	# 77-79

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        Unknown1084(1)
        setInvincible(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 40):
                Unknown20000(0)
            if (SLOT_51 >= 7):
                clearUponHandler(3)
                sendToLabel(1)
        loopRelated(17, 226)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
        callSubroutine('UniqueZLineUltimate')
    sprite('ubl430_00', 3)	# 1-3
    sprite('ubl430_01', 3)	# 4-6
    sprite('ubl430_02', 3)	# 7-9
    SFX_3('ublse_03')
    SFX_3('ublse_03')
    sprite('ubl430_03', 3)	# 10-12
    Unknown20000(1)
    sprite('ubl430_04', 3)	# 13-15
    sprite('ubl430_05', 2)	# 16-17
    sprite('ubl430_06', 2)	# 18-19
    sprite('ubl430_07', 2)	# 20-21
    GFX_0('ubl_UltimateBeam_Charge_Eff', 0)
    SFX_3('ublse_14')
    SFX_3('ublse_14')
    SFX_3('ublse_12')
    SFX_3('ublse_12')
    sprite('ubl430_08', 2)	# 22-23
    sprite('ubl430_09', 2)	# 24-25
    GFX_0('ubl_UltimateBeam_Lightbullet_Ef', 0)
    label(0)
    sprite('ubl430_10', 3)	# 26-28
    SLOT_51 = (SLOT_51 + 1)
    sprite('ubl430_11', 3)	# 29-31
    sprite('ubl430_12', 3)	# 32-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl430_13', 3)	# 35-37
    Unknown26('ubl_UltimateBeam_Charge_Eff')
    Unknown26('ubl_UltimateBeam_Lightbullet_Ef')
    GFX_0('ubl_UltimateBeam_Eff', 0)
    GFX_0('ubl_UltimateBeam_Muzzle_Eff', 0)
    GFX_0('ubl_UltimateBeam_Wave_Eff', 0)
    GFX_0('UltimateBeam_AtkCol', 0)
    Unknown23029(1, 2003, 0)
    SFX_3('ublse_07')
    SFX_3('ublse_08')
    label(2)
    sprite('ubl430_14', 3)	# 38-40
    setInvincible(0)
    sprite('ubl430_15', 3)	# 41-43
    sprite('ubl430_16', 3)	# 44-46
    sprite('ubl430_13', 3)	# 47-49
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('ubl430_17', 3)	# 50-52
    SFX_3('ublse_02')
    sprite('ubl430_18', 3)	# 53-55
    sprite('ubl430_19', 3)	# 56-58
    sprite('ubl430_20', 3)	# 59-61
    sprite('ubl430_21', 3)	# 62-64
    sprite('ubl430_22', 3)	# 65-67
    sprite('ubl430_23', 3)	# 68-70
    SFX_3('ublse_04')
    sprite('ubl430_24', 3)	# 71-73
    sprite('ubl430_25', 3)	# 74-76
    sprite('ubl430_26', 3)	# 77-79

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('rg600_16', 5)	# 1-5
    Unknown1084(1)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('rg600_15', 5)	# 6-10
    sprite('rg600_14', 5)	# 11-15
    sprite('rg600_04', 5)	# 16-20
    sprite('rg600_05', 5)	# 21-25
    sprite('rg600_06', 12)	# 26-37
    sprite('rg600_07', 4)	# 38-41
    sprite('rg600_08', 4)	# 42-45
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 46-51
    sprite('rg600_10', 5)	# 52-56
    sprite('rg600_11', 6)	# 57-62
    sprite('rg600_12', 10)	# 63-72
    label(1)
    sprite('rg600_12', 1)	# 73-73
    Unknown30042(24)
    if SLOT_ReturnVal:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rg600_13', 3)	# 74-76
    sprite('rg600_14', 3)	# 77-79
    sprite('rg600_15', 3)	# 80-82
    sprite('rg600_16', 3)	# 83-85

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('ubl252_01', 3)	# 121-123	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    SFX_3('ublse_14')
    SFX_3('ublse_22')
    label(1)
    sprite('ubl252_02', 3)	# 124-126	 **attackbox here**
    sprite('ubl252_03', 3)	# 127-129	 **attackbox here**
    sprite('ubl252_01', 3)	# 130-132	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ubl252_13', 13)	# 133-145
    Unknown8000(100, 1, 1)
    SFX_3('ublse_16')
    Unknown1084(1)
    ScreenShake(0, 7500)
    GFX_1('tgef_dustB', 0)
    GFX_1('tgef_dustB', 1)
    GFX_1('tgef_dustA', 2)
    sprite('ubl252_14', 6)	# 146-151
    sprite('ubl252_15', 6)	# 152-157
    sprite('ubl252_16', 6)	# 158-163

@State
def CmnActChangeReturnAppealBurst():

    def upon_IMMEDIATE():
        loopRelated(17, 48)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
    sprite('ubl300_00', 4)	# 1-4
    sprite('ubl300_01', 4)	# 5-8
    sprite('ubl300_02', 4)	# 9-12
    label(0)
    sprite('ubl300_03', 1)	# 13-13
    sprite('ubl300_04', 1)	# 14-14
    sprite('ubl300_05', 1)	# 15-15
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ubl300_06', 4)	# 16-19
    sprite('ubl300_07', 4)	# 20-23
    sprite('ubl300_08', 4)	# 24-27
    loopRest()

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')

        def upon_STATE_END():
            Unknown2015(-1)
        Unknown26('ubl_201_Fire_Eff')
    sprite('ubl203_00', 3)	# 1-3
    Unknown1018()
    Unknown1019(80)
    sprite('ubl203_01', 4)	# 4-7
    GFX_0('ubl_Dash_Eff', 100)
    Unknown1019(80)
    sprite('ubl203_02', 3)	# 8-10
    sprite('ubl203_03', 3)	# 11-13
    physicsXImpulse(15000)
    Unknown2015(200)
    SFX_3('ublse_15')
    SFX_3('ublse_23')
    sprite('ubl203_04', 3)	# 14-16
    sprite('ubl203_05', 3)	# 17-19
    physicsXImpulse(30000)
    sprite('ubl203_06', 3)	# 20-22
    sprite('ubl203_07', 3)	# 23-25
    SFX_3('ublse_14')
    sprite('ubl203_08', 3)	# 26-28	 **attackbox here**
    Unknown1019(20)
    sprite('ubl203_09', 3)	# 29-31
    setInvincible(0)
    Unknown26('ubl_Dash_Eff')
    SFX_3('ublse_00')
    sprite('ubl203_10', 2)	# 32-33
    sprite('ubl203_11', 2)	# 34-35
    Unknown1019(20)
    sprite('ubl203_12', 2)	# 36-37
    sprite('ubl203_13', 3)	# 38-40
    Unknown1084(1)
    sprite('ubl203_14', 3)	# 41-43
    sprite('ubl203_15', 3)	# 44-46

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
    sprite('ubl203_09', 2)	# 2-3
    sprite('ubl203_10', 3)	# 4-6
    sprite('ubl203_11', 3)	# 7-9
    sprite('ubl203_12', 3)	# 10-12
    sprite('ubl203_13', 3)	# 13-15
    sprite('ubl203_14', 3)	# 16-18
    sprite('ubl203_15', 3)	# 19-21
    sprite('ubl200_00ex', 2)	# 22-23	 **attackbox here**
    sprite('ubl200_01ex', 2)	# 24-25	 **attackbox here**
    sprite('ubl200_01ex', 2)	# 26-27	 **attackbox here**
    sprite('ubl200_02ex', 2)	# 28-29	 **attackbox here**
    sprite('ubl200_03ex', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_200_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    SFX_0('016_explode_1')
    sprite('ubl200_03ex', 3)	# 32-34	 **attackbox here**
    GFX_0('ubl_200_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    sprite('ubl200_03ex', 3)	# 35-37	 **attackbox here**
    GFX_0('ubl_200_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    sprite('ubl200_04ex', 6)	# 38-43	 **attackbox here**
    sprite('ubl200_05ex', 6)	# 44-49	 **attackbox here**
    sprite('ubl200_06ex', 6)	# 50-55	 **attackbox here**
    label(0)
    sprite('ubl000_00', 1)	# 56-56
    sprite('ubl000_01', 1)	# 57-57
    sprite('ubl000_02', 1)	# 58-58
    sprite('ubl000_03', 1)	# 59-59
    sprite('ubl000_04', 1)	# 60-60
    sprite('ubl000_05', 1)	# 61-61
    sprite('ubl000_06', 1)	# 62-62
    sprite('ubl000_07', 1)	# 63-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 64-64

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        Unknown9017(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ubl201_00', 4)	# 1-4
    sprite('ubl201_00', 3)	# 5-7
    sprite('ubl201_01', 4)	# 8-11
    sprite('ubl201_02', 3)	# 12-14
    sprite('ubl201_03', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_201_Fire_Eff', 0)
    SFX_3('ublse_06')
    SFX_3('ublse_20')
    sprite('ubl201_04', 7)	# 18-24	 **attackbox here**
    sprite('ubl201_05', 7)	# 25-31	 **attackbox here**
    sprite('ubl201_06', 7)	# 32-38
    sprite('ubl201_07', 7)	# 39-45
    label(0)
    sprite('ubl000_00', 1)	# 46-46
    sprite('ubl000_01', 1)	# 47-47
    sprite('ubl000_02', 1)	# 48-48
    sprite('ubl000_03', 1)	# 49-49
    sprite('ubl000_04', 1)	# 50-50
    sprite('ubl000_05', 1)	# 51-51
    sprite('ubl000_06', 1)	# 52-52
    sprite('ubl000_07', 1)	# 53-53
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 54-54

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9017(1)

        def upon_11():
            GFX_0('XhitEff_Denkou', -1)
    sprite('ubl270_00', 9)	# 1-9
    sprite('ubl270_01', 5)	# 10-14
    Unknown1045(-10000)
    sprite('ubl270_02', 5)	# 15-19
    sprite('ubl270_03', 5)	# 20-24	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_270_Shot_Eff', 0)
    GFX_0('ubl_270_Bomb_Eff', 1)
    SFX_0('016_explode_2')
    sprite('ubl270_04', 6)	# 25-30
    sprite('ubl270_05', 6)	# 31-36
    sprite('ubl270_06', 6)	# 37-42
    sprite('ubl270_07', 6)	# 43-48
    sprite('ubl270_08', 6)	# 49-54
    sprite('ubl270_09', 6)	# 55-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        Unknown9017(1)

        def upon_11():
            GFX_0('XhitEff_Denkou', -1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('ubl000_00', 1)	# 1-1
    sprite('ubl000_01', 1)	# 2-2
    sprite('ubl000_02', 1)	# 3-3
    sprite('ubl000_03', 1)	# 4-4
    sprite('ubl000_04', 1)	# 5-5
    sprite('ubl000_05', 1)	# 6-6
    sprite('ubl000_06', 1)	# 7-7
    sprite('ubl000_07', 1)	# 8-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl270_00', 9)	# 9-17
    sprite('ubl270_01', 5)	# 18-22
    Unknown1045(-10000)
    sprite('ubl270_02', 5)	# 23-27
    sprite('ubl270_03', 5)	# 28-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_270_Shot_Eff', 0)
    GFX_0('ubl_270_Bomb_Eff', 1)
    SFX_0('016_explode_2')
    sprite('ubl270_04', 6)	# 33-38
    sprite('ubl270_05', 6)	# 39-44
    sprite('ubl270_06', 6)	# 45-50
    sprite('ubl270_07', 6)	# 51-56
    sprite('ubl270_08', 6)	# 57-62
    sprite('ubl270_09', 6)	# 63-68

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        DisableAttackRestOfMove()

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 42):
                RefreshMultihit()
            if (SLOT_18 == 43):
                sendToLabel(9)
    sprite('null', 22)	# 1-22
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 23-23
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-3000000)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    Unknown1015(12000)
    sprite('ubl403_02', 3)	# 24-26	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl403_03', 3)	# 27-29	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    SFX_3('ublse_01')
    sprite('ubl403_04', 3)	# 30-32	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl403_02', 3)	# 33-35	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl403_03', 3)	# 36-38	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl403_04', 3)	# 39-41	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl403_02', 3)	# 42-44	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_forward_Eff', 100)
    Unknown1019(0)
    Unknown1045(10000)
    label(9)
    sprite('ubl004_00', 2)	# 45-46
    sprite('ubl004_01', 2)	# 47-48
    sprite('ubl004_02', 6)	# 49-54
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 6)	# 55-60
    sprite('ubl004_04', 6)	# 61-66
    sprite('ubl004_05', 6)	# 67-72
    sprite('ubl004_06', 6)	# 73-78
    sprite('ubl004_07', 6)	# 79-84
    sprite('ubl004_08', 6)	# 85-90
    label(10)
    sprite('ubl000_00', 1)	# 91-91
    Unknown1084(1)
    sprite('ubl000_01', 1)	# 92-92
    sprite('ubl000_02', 1)	# 93-93
    sprite('ubl000_03', 1)	# 94-94
    sprite('ubl000_04', 1)	# 95-95
    sprite('ubl000_05', 1)	# 96-96
    sprite('ubl000_06', 1)	# 97-97
    sprite('ubl000_07', 1)	# 98-98
    loopRest()
    gotoLabel(10)

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9017(1)
    sprite('ubl201_00', 3)	# 1-3
    sprite('ubl201_00', 2)	# 4-5
    sprite('ubl201_01', 3)	# 6-8
    sprite('ubl201_02', 3)	# 9-11
    sprite('ubl201_03', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_201_Fire_Eff', 0)
    SFX_3('ublse_06')
    sprite('ubl201_04', 7)	# 15-21	 **attackbox here**
    sprite('ubl201_05', 7)	# 22-28	 **attackbox here**
    sprite('ubl201_06', 7)	# 29-35
    sprite('ubl201_07', 7)	# 36-42
    label(0)
    sprite('ubl000_00', 1)	# 43-43
    sprite('ubl000_01', 1)	# 44-44
    sprite('ubl000_02', 1)	# 45-45
    sprite('ubl000_03', 1)	# 46-46
    sprite('ubl000_04', 1)	# 47-47
    sprite('ubl000_05', 1)	# 48-48
    sprite('ubl000_06', 1)	# 49-49
    sprite('ubl000_07', 1)	# 50-50
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 51-51

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9017(1)

        def upon_11():
            GFX_0('XhitEff_Denkou', -1)
    sprite('ubl270_00', 9)	# 1-9
    sprite('ubl270_01', 5)	# 10-14
    Unknown1045(-10000)
    sprite('ubl270_02', 5)	# 15-19
    sprite('ubl270_03', 5)	# 20-24	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_270_Shot_Eff', 0)
    GFX_0('ubl_270_Bomb_Eff', 1)
    SFX_0('016_explode_2')
    sprite('ubl270_04', 6)	# 25-30
    sprite('ubl270_05', 6)	# 31-36
    sprite('ubl270_06', 6)	# 37-42
    sprite('ubl270_07', 6)	# 43-48
    sprite('ubl270_08', 6)	# 49-54
    sprite('ubl270_09', 6)	# 55-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        Unknown9017(1)

        def upon_11():
            GFX_0('XhitEff_Denkou', -1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('ubl000_00', 1)	# 1-1
    sprite('ubl000_01', 1)	# 2-2
    sprite('ubl000_02', 1)	# 3-3
    sprite('ubl000_03', 1)	# 4-4
    sprite('ubl000_04', 1)	# 5-5
    sprite('ubl000_05', 1)	# 6-6
    sprite('ubl000_06', 1)	# 7-7
    sprite('ubl000_07', 1)	# 8-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl270_00', 9)	# 9-17
    sprite('ubl270_01', 5)	# 18-22
    Unknown1045(-10000)
    sprite('ubl270_02', 5)	# 23-27
    sprite('ubl270_03', 5)	# 28-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_270_Shot_Eff', 0)
    GFX_0('ubl_270_Bomb_Eff', 1)
    SFX_0('016_explode_2')
    sprite('ubl270_04', 6)	# 33-38
    sprite('ubl270_05', 6)	# 39-44
    sprite('ubl270_06', 6)	# 45-50
    sprite('ubl270_07', 6)	# 51-56
    sprite('ubl270_08', 6)	# 57-62
    sprite('ubl270_09', 6)	# 63-68

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(12000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('ubl000_00', 3)	# 1-3
    label(0)
    sprite('ubl030_00', 1)	# 4-4
    GFX_0('ubl_forward_Eff', 100)
    SFX_3('ublse_00')
    sprite('ubl030_01', 1)	# 5-5
    sprite('ubl030_02', 1)	# 6-6
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_03', 1)	# 7-7
    sprite('ubl030_04', 1)	# 8-8
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_05', 1)	# 9-9
    sprite('ubl030_06', 1)	# 10-10
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_07', 1)	# 11-11
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl310_00', 2)	# 12-13
    clearUponHandler(3)
    Unknown1019(10)
    SFX_3('ublse_04')
    sprite('ubl310_01', 1)	# 14-14
    sprite('ubl310_02', 3)	# 15-17	 **attackbox here**
    Unknown1084(1)
    sprite('ubl310_03', 3)	# 18-20
    sprite('ubl310_04', 8)	# 21-28
    sprite('ubl310_05', 8)	# 29-36
    sprite('ubl310_06', 4)	# 37-40

@Subroutine
def InitThrowExe():
    Unknown17012(1, 0, 0)
    AttackLevel_(3)
    Damage(300)
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
    StarterRating(2)
    Unknown2004(1, 0)
    Unknown14077(0)
    Unknown9266(6)
    Unknown2018(0, 80)

@State
def ThrowExe():

    def upon_IMMEDIATE():
        callSubroutine('InitThrowExe')
        Unknown11069('ThrowExe')
    sprite('ubl310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ubl311_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ubl311_00', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown7009(0)
    SFX_3('ublse_22')
    GFX_0('ubl_310_NearSpark_Eff', 100)
    GFX_0('ubl_310_BackSpark_Eff', 100)
    Unknown23119(4128831, 3, -1)
    sprite('ubl311_01', 3)	# 10-12	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_sl')
    SFX_0('014_electric_l')
    sprite('ubl311_02', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    sprite('ubl311_01', 3)	# 16-18	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_l')
    sprite('ubl311_02', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    sprite('ubl311_01', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_l')
    sprite('ubl311_02', 3)	# 25-27	 **attackbox here**
    Unknown7009(0)
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_l')
    sprite('ubl311_03', 3)	# 28-30
    Unknown26('ubl_310_NearSpark_Eff')
    sprite('ubl311_04', 3)	# 31-33
    sprite('ubl270_02', 2)	# 34-35
    sprite('ubl270_03', 3)	# 36-38	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(5)
    Damage(500)
    GroundedHitstunAnimation(10)
    AirPushbackX(5000)
    AirPushbackY(40000)
    AirUntechableTime(60)
    Unknown11064(0)
    Unknown11092(1)
    Unknown14077(1)
    Unknown9266(1)
    Unknown11069('')
    GFX_0('ubl_270_Bomb_Eff', 0)
    sprite('ubl270_04', 5)	# 39-43
    setInvincible(0)
    Recovery()
    sprite('ubl270_05', 5)	# 44-48
    sprite('ubl270_06', 5)	# 49-53
    sprite('ubl270_07', 5)	# 54-58
    sprite('ubl270_08', 5)	# 59-63
    sprite('ubl270_09', 5)	# 64-68

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(12000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('ubl000_00', 3)	# 1-3
    label(0)
    sprite('ubl030_00', 1)	# 4-4
    GFX_0('ubl_backward_Eff', 100)
    SFX_3('ublse_00')
    sprite('ubl030_01', 1)	# 5-5
    sprite('ubl030_02', 1)	# 6-6
    GFX_0('ubl_backward_Eff', 100)
    sprite('ubl030_03', 1)	# 7-7
    sprite('ubl030_04', 1)	# 8-8
    GFX_0('ubl_backward_Eff', 100)
    sprite('ubl030_05', 1)	# 9-9
    sprite('ubl030_06', 1)	# 10-10
    GFX_0('ubl_backward_Eff', 100)
    sprite('ubl030_07', 1)	# 11-11
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl310_00', 2)	# 12-13
    clearUponHandler(3)
    Unknown1019(10)
    SFX_3('ublse_04')
    sprite('ubl310_01', 1)	# 14-14
    sprite('ubl310_02', 3)	# 15-17	 **attackbox here**
    Unknown1084(1)
    sprite('ubl310_03', 3)	# 18-20
    sprite('ubl310_04', 8)	# 21-28
    sprite('ubl310_05', 8)	# 29-36
    sprite('ubl310_06', 4)	# 37-40

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        callSubroutine('InitThrowExe')
        Unknown11069('BackThrowExe')
    sprite('ubl310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ubl313_00', 1)	# 4-4
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ubl313_01', 1)	# 5-5
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ubl313_02', 1)	# 6-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ubl313_03', 1)	# 7-7
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('ubl313_02', 1)	# 8-8
    Unknown2005()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ubl313_01', 1)	# 9-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ubl313_00', 1)	# 10-10
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ubl311_00', 3)	# 11-13
    Unknown23119(4128831, 3, -1)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown7009(0)
    SFX_3('ublse_22')
    GFX_0('ubl_310_NearSpark_Eff', 100)
    GFX_0('ubl_310_BackSpark_Eff', 100)
    Unknown23119(4128831, 3, -1)
    sprite('ubl311_01', 3)	# 14-16	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_sl')
    SFX_0('014_electric_l')
    sprite('ubl311_02', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    sprite('ubl311_01', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_l')
    sprite('ubl311_02', 3)	# 23-25	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    SFX_0('014_electric_l')
    sprite('ubl311_01', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_l')
    sprite('ubl311_02', 3)	# 29-31	 **attackbox here**
    Unknown7009(0)
    SFX_0('014_electric_ll')
    SFX_0('014_electric_s')
    SFX_0('014_electric_ml')
    SFX_0('014_electric_l')
    sprite('ubl311_03', 3)	# 32-34
    Unknown26('ubl_310_NearSpark_Eff')
    sprite('ubl311_04', 3)	# 35-37
    sprite('ubl270_02', 2)	# 38-39
    sprite('ubl270_03', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(5)
    Damage(500)
    GroundedHitstunAnimation(10)
    AirPushbackX(5000)
    AirPushbackY(40000)
    AirUntechableTime(60)
    Unknown11064(0)
    Unknown11092(1)
    Unknown14077(1)
    Unknown9266(1)
    Unknown11069('')
    GFX_0('ubl_270_Bomb_Eff', 0)
    sprite('ubl270_04', 5)	# 43-47
    setInvincible(0)
    Recovery()
    sprite('ubl270_05', 5)	# 48-52
    sprite('ubl270_06', 5)	# 53-57
    sprite('ubl270_07', 5)	# 58-62
    sprite('ubl270_08', 5)	# 63-67
    sprite('ubl270_09', 5)	# 68-72

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
    sprite('ubl252_05', 2)	# 32-33	 **attackbox here**
    SFX_3('ublse_01')
    sprite('ubl252_06', 2)	# 34-35	 **attackbox here**
    SFX_3('ublse_21')
    label(2)
    sprite('ubl252_05', 3)	# 36-38	 **attackbox here**
    sprite('ubl252_06', 3)	# 39-41	 **attackbox here**
    gotoLabel(2)
    label(1)
    sprite('keep', 1)	# 42-42
    sprite('ubl252_13', 12)	# 43-54
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    StartMultihit()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 30000)
    SFX_3('ublse_16')
    sprite('ubl252_14', 6)	# 55-60
    sprite('ubl010_01', 6)	# 61-66
    sprite('ubl010_00', 6)	# 67-72

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ubl252_14', 5)	# 1-5
    sprite('ubl252_15', 5)	# 6-10
    sprite('ubl252_16', 5)	# 11-15
    sprite('ubl270_00', 9)	# 16-24
    sprite('ubl270_01', 5)	# 25-29
    Unknown1045(-10000)
    sprite('ubl270_02', 5)	# 30-34
    sprite('ubl270_03', 5)	# 35-39	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_270_Shot_Eff', 0)
    GFX_0('ubl_270_Bomb_Eff', 1)
    SFX_0('016_explode_2')
    sprite('ubl270_04', 6)	# 40-45
    sprite('ubl270_05', 6)	# 46-51
    sprite('ubl270_06', 6)	# 52-57
    sprite('ubl270_07', 6)	# 58-63
    sprite('ubl270_08', 6)	# 64-69
    sprite('ubl270_09', 6)	# 70-75

@Subroutine
def InitNmlAtk5AData():
    AttackDefaults_StandingNormal()
    AttackLevel_(3)
    Damage(650)
    AirPushbackX(8000)
    AirPushbackY(10000)
    PushbackX(5000)
    hitstun(21)
    AirUntechableTime(21)
    ChipDamagePct(5)
    ProjectileDurabilityLvl(1)
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('CmnActCrushAttack')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtkThrow')
    HitOrBlockCancel('NmlAtkBackThrow')
    Hitstop(3)
    Unknown11092(1)
    Unknown1112('')
    HitJumpCancel(1)
    SLOT_51 = 1

    def upon_CLEAR_OR_EXIT():
        if CheckInput(0x6b):
            physicsXImpulse(0)
        if CheckInput(0x78):
            physicsXImpulse(8000)
        if CheckInput(0x5e):
            physicsXImpulse(-6000)
        if SLOT_IsUnlimitedCharacter:
            physicsXImpulse(8000)

@Subroutine
def InitArmarStandParam():
    GuardPoint_(1)
    Unknown22030(0)
    Unknown22031(15, -1)
    Unknown22035(50)
    setInvincible(1)
    Unknown22019('0000000001000000000000000100000000000000')
    callSubroutine('InitArrmorVisualFunc')

@Subroutine
def InitArrmorVisualFunc():

    def upon_42():
        ScreenShake(15000, 5000)
        SFX_3('ublse_09')
        SFX_3('ublse_09')

@Subroutine
def Stand5ACancelInput():
    Unknown14070('CmnActCrushAttack')
    Unknown14070('NmlAtkThrow')
    Unknown14070('NmlAtkBackThrow')
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk2A')
    Unknown14070('NmlAtk2B')
    Unknown14070('NmlAtk2C')
    Unknown14070('CmnActInvincibleAttack')
    Unknown14070('DashAtack')
    Unknown14070('ShotBeamA')
    Unknown14070('ShotBeamB')
    Unknown14070('ShotBeamC')
    Unknown14070('GrenadeA')
    Unknown14070('GrenadeB')
    Unknown14070('GrenadeC')
    Unknown14070('UltimateBeam')
    Unknown14070('UltimateBeamSP')
    Unknown14070('UltimateRush')
    Unknown14070('UltimateRushSP')
    Unknown14070('AstralHeat')

@Subroutine
def Stand5ACancelBegin():
    Unknown14072('CmnActCrushAttack')
    Unknown14072('NmlAtkThrow')
    Unknown14072('NmlAtkBackThrow')
    Unknown14072('NmlAtk5B')
    Unknown14072('NmlAtk2A')
    Unknown14072('NmlAtk2B')
    Unknown14072('NmlAtk2C')
    Unknown14072('CmnActInvincibleAttack')
    Unknown14072('DashAtack')
    Unknown14072('ShotBeamA')
    Unknown14072('ShotBeamB')
    Unknown14072('ShotBeamC')
    Unknown14072('GrenadeA')
    Unknown14072('GrenadeB')
    Unknown14072('GrenadeC')
    Unknown14072('UltimateBeam')
    Unknown14072('UltimateBeamSP')
    Unknown14072('UltimateRush')
    Unknown14072('UltimateRushSP')
    Unknown14072('AstralHeat')

@Subroutine
def Stand5ACancelClear():
    Unknown14074('CmnActCrushAttack')
    Unknown14074('NmlAtkThrow')
    Unknown14074('NmlAtkBackThrow')
    Unknown14074('NmlAtk5B')
    Unknown14074('NmlAtk2A')
    Unknown14074('NmlAtk2B')
    Unknown14074('NmlAtk2C')
    Unknown14074('CmnActInvincibleAttack')

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        callSubroutine('InitNmlAtk5AData')
        callSubroutine('CheckAtemiMuteki')
        AttackP1(90)
        callSubroutine('UniqueZLine')
        GFX_0('Stand5ACaterpillar', 100)
    sprite('ubl200_00', 2)	# 1-2
    sprite('ubl200_01', 1)	# 3-3
    sprite('ubl200_01', 3)	# 4-6
    callSubroutine('InitArmarStandParam')
    sprite('ubl200_02', 2)	# 7-8
    callSubroutine('Stand5ACancelInput')
    sprite('ubl200_02', 1)	# 9-9
    sprite('ubl200_03_01', 2)	# 10-11	 **attackbox here**
    SFX_3('ublse_05')
    SFX_0('016_explode_1')
    GFX_0('ubl_200_Vulcan_Eff', 0)
    sprite('ubl200_03', 2)	# 12-13	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    GFX_0('ubl_200_Vulcan_Eff', 0)
    sprite('ubl200_03', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_200_Vulcan_Eff', 0)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5A_2nd')
        Unknown2037(1)
    sprite('ubl200_04', 7)	# 16-22
    Recovery()
    if SLOT_2:
        callSubroutine('Stand5ACancelBegin')
    if CheckInput(0x1):
        sendToLabel(10)
    else:
        setInvincible(0)
    if SLOT_IsUnlimitedCharacter:
        sendToLabel(10)
    sprite('ubl200_05', 7)	# 23-29
    Unknown2063()
    callSubroutine('Stand5ACancelClear')
    sprite('ubl200_06', 4)	# 30-33
    sprite('ubl200_06', 4)	# 34-37
    ExitState()
    label(10)
    sprite('keep', 1)	# 38-38
    enterState('NmlAtk5A_2nd')

@State
def NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('InitNmlAtk5AData')
        callSubroutine('UniqueZLine')
        GFX_0('Stand5ACaterpillar', 100)
    sprite('ubl200_03', 2)	# 1-2	 **attackbox here**
    SFX_3('ublse_05')
    SFX_0('016_explode_1')
    GFX_0('ubl_200_Vulcan_Eff', 0)
    callSubroutine('Stand5ACancelInput')
    sprite('ubl200_03', 2)	# 3-4	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_200_Vulcan_Eff', 0)
    sprite('ubl200_03', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_200_Vulcan_Eff', 0)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5A_3rd')
        Unknown2037(1)
    sprite('ubl200_04', 8)	# 7-14
    Recovery()
    if SLOT_2:
        callSubroutine('Stand5ACancelBegin')
    if CheckInput(0x1):
        sendToLabel(10)
    else:
        setInvincible(0)
    if SLOT_IsUnlimitedCharacter:
        sendToLabel(10)
    sprite('ubl200_05', 8)	# 15-22
    Unknown2063()
    callSubroutine('Stand5ACancelClear')
    sprite('ubl200_06', 4)	# 23-26
    sprite('ubl200_06', 5)	# 27-31
    ExitState()
    label(10)
    sprite('keep', 1)	# 32-32
    enterState('NmlAtk5A_3rd')

@State
def NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        callSubroutine('InitNmlAtk5AData')
        AirPushbackY(14000)
        Unknown14085('NmlAtkThrow')
        Unknown14085('NmlAtkBackThrow')
        callSubroutine('UniqueZLine')
        GFX_0('Stand5ACaterpillar', 100)
    sprite('ubl200_03', 2)	# 1-2	 **attackbox here**
    callSubroutine('Stand5ACancelInput')
    SFX_3('ublse_05')
    SFX_0('016_explode_1')
    GFX_0('ubl_200_Vulcan_Eff', 0)
    sprite('ubl200_03', 2)	# 3-4	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_200_Vulcan_Eff', 0)
    sprite('ubl200_03', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_200_Vulcan_Eff', 0)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5A_4th')
        Unknown2037(1)
    Unknown14070('NmlAtk5A_4th')
    sprite('ubl200_04', 8)	# 7-14
    Recovery()
    if SLOT_2:
        callSubroutine('Stand5ACancelBegin')
    Unknown14072('NmlAtk5A_4th')
    Unknown14074('NmlAtkThrow')
    Unknown14074('NmlAtkBackThrow')
    if CheckInput(0x1):
        sendToLabel(10)
    else:
        setInvincible(0)
    if SLOT_IsUnlimitedCharacter:
        sendToLabel(10)
    sprite('ubl200_05', 8)	# 15-22
    Unknown2063()
    Unknown14074('NmlAtk5A_4th')
    callSubroutine('Stand5ACancelClear')
    sprite('ubl200_06', 4)	# 23-26
    sprite('ubl200_06', 5)	# 27-31
    ExitState()
    label(10)
    sprite('keep', 1)	# 32-32
    enterState('NmlAtk5A_4th')

@State
def NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(2500)
        GroundedHitstunAnimation(10)
        PushbackX(19800)
        AirPushbackX(15000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        Unknown9266(1)
        ChipDamagePct(5)
        JumpCancel_(0)
        Unknown11044(1)
        Unknown30088(1)
        callSubroutine('UniqueZLine')
    sprite('ubl270_01', 3)	# 1-3
    Unknown1045(-10000)
    sprite('ubl270_02', 3)	# 4-6
    sprite('ubl270_03', 3)	# 7-9	 **attackbox here**
    GFX_0('ubl_270_Shot_Eff', 0)
    GFX_0('ubl_270_Bomb_Eff', 1)
    sprite('ubl270_04', 6)	# 10-15
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ubl270_05', 6)	# 16-21
    sprite('ubl270_06', 6)	# 22-27
    sprite('ubl270_07', 6)	# 28-33
    sprite('ubl270_08', 6)	# 34-39
    sprite('ubl270_09', 6)	# 40-45

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1500)
        PushbackX(9800)
        AirPushbackX(15000)
        AirPushbackY(15000)
        AttackP1(90)
        AirUntechableTime(30)
        Hitstop(11)
        Unknown9266(1)
        ChipDamagePct(5)
        ProjectileDurabilityLvl(1)
        HitOrBlockCancel('NmlAtk5B_2nd')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        callSubroutine('CheckAtemiMuteki')
        callSubroutine('UniqueZLine')
    sprite('ubl201_00', 3)	# 1-3
    sprite('ubl201_00', 2)	# 4-5
    callSubroutine('InitArmarStandParam')
    SFX_3('ublse_20')
    sprite('ubl201_01', 3)	# 6-8
    sprite('ubl201_02', 3)	# 9-11
    sprite('ubl201_03ex', 1)	# 12-12	 **attackbox here**
    GFX_0('ubl_201_Fire_Eff', 0)
    SFX_3('ublse_06')
    Unknown1045(-1000)
    sprite('ubl201_03', 2)	# 13-14	 **attackbox here**
    sprite('ubl201_04', 2)	# 15-16	 **attackbox here**
    setInvincible(0)
    sprite('ubl201_04ex', 5)	# 17-21	 **attackbox here**
    sprite('ubl201_05', 7)	# 22-28	 **attackbox here**
    sprite('ubl201_05', 7)	# 29-35	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ubl201_06', 7)	# 36-42
    sprite('ubl201_07', 7)	# 43-49

@State
def NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(90)
        GroundedHitstunAnimation(10)
        AirPushbackY(30000)
        AirUntechableTime(40)
        Unknown11056(0)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown2016(300)
        Unknown26('ubl_201_Fire_Eff')
        callSubroutine('UniqueZLine')
    sprite('ubl271_00', 3)	# 1-3
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl271_01', 3)	# 4-6
    GFX_0('ubl_forward_Eff', 100)
    callSubroutine('InitArmarStandParam')
    physicsXImpulse(62000)
    SFX_3('ublse_01')
    sprite('ubl271_02', 3)	# 7-9
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl271_03', 3)	# 10-12
    GFX_0('ubl_forward_Eff', 100)
    SFX_3('ublse_00')
    sprite('ubl271_04', 3)	# 13-15
    GFX_0('ubl_forward_Eff', 100)
    Unknown1019(20)
    SFX_3('ublse_14')
    sprite('ubl271_05', 3)	# 16-18	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl271_06', 3)	# 19-21
    Unknown2016(-1)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ubl271_07', 7)	# 22-28
    Unknown1019(0)
    sprite('ubl271_08', 7)	# 29-35
    sprite('ubl271_09', 7)	# 36-42
    sprite('ubl271_10', 7)	# 43-49
    sprite('ubl271_11', 2)	# 50-51
    sprite('ubl271_12', 2)	# 52-53

@Subroutine
def InitArmarCrouchParam():
    GuardPoint_(1)
    Unknown22030(0)
    Unknown22031(15, -1)
    Unknown22035(50)
    setInvincible(1)
    Unknown22019('0000000000000000010000000100000000000000')
    callSubroutine('InitArrmorVisualFunc')

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1000)
        HitLow(2)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('CheckAtemiMuteki')
        callSubroutine('UniqueZLine')
    sprite('ubl230_00', 3)	# 1-3
    sprite('ubl230_01', 4)	# 4-7
    callSubroutine('InitArmarStandParam')
    SFX_3('ublse_03')
    SFX_3('ublse_00')
    SFX_3('ublse_23')
    sprite('ubl230_02', 3)	# 8-10	 **attackbox here**
    GFX_0('ubl_230_Eff', 0)
    sprite('ubl230_03', 3)	# 11-13
    setInvincible(0)
    Recovery()
    Unknown2063()
    SFX_3('ublse_00')
    sprite('ubl230_04', 7)	# 14-20
    sprite('ubl230_05', 8)	# 21-28

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        Unknown11092(1)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        Unknown26('ubl_201_Fire_Eff')
        callSubroutine('CheckAtemiMuteki')
        callSubroutine('UniqueZLine')
    sprite('ubl231_00', 3)	# 1-3
    sprite('ubl231_01', 3)	# 4-6
    callSubroutine('InitArmarStandParam')
    physicsXImpulse(18000)
    SFX_3('ublse_00')
    sprite('ubl231_02', 3)	# 7-9
    SFX_3('ublse_22')
    sprite('ubl231_03', 2)	# 10-11
    GFX_0('ubl_231_Eff', 0)
    SFX_3('ublse_03')
    SFX_3('ublse_00')
    sprite('ubl231_04', 3)	# 12-14	 **attackbox here**
    Unknown1019(20)
    sprite('ubl231_05', 3)	# 15-17
    setInvincible(0)
    SFX_3('ublse_04')
    sprite('ubl231_06', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    sprite('ubl231_07', 5)	# 21-25
    Recovery()
    Unknown2063()
    SFX_3('ublse_00')
    sprite('ubl231_08', 5)	# 26-30
    sprite('ubl231_09', 5)	# 31-35
    sprite('ubl231_10', 5)	# 36-40

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(2000)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(10000)
        AirPushbackY(8000)
        blockstun(21)
        AirUntechableTime(30)
        AttackP1(90)
        HitLow(2)
        Unknown11056(0)
        Unknown26('ubl_201_Fire_Eff')
        callSubroutine('CheckAtemiMuteki')
        callSubroutine('UniqueZLine')
    sprite('ubl232_00', 3)	# 1-3
    sprite('ubl232_00', 4)	# 4-7
    callSubroutine('InitArmarStandParam')
    sprite('ubl232_01', 7)	# 8-14
    sprite('ubl232_02', 5)	# 15-19
    physicsXImpulse(24000)
    GFX_0('ubl_232_Eff', 0)
    GFX_0('ubl_232_b_Eff', 1)
    SFX_3('ublse_15')
    SFX_3('ublse_23')
    sprite('ubl232_03', 5)	# 20-24
    SFX_3('ublse_00')
    sprite('ubl232_04', 3)	# 25-27	 **attackbox here**
    Unknown26('ubl_232_Eff')
    Unknown26('ubl_232_b_Eff')
    Unknown26('ubl_232_smoke_Eff')
    Unknown26('ubl_232_b_smoke_Eff')
    GFX_0('ubl_232_Eff', 0)
    GFX_0('ubl_232_b_Eff', 1)
    Unknown1019(40)
    SFX_3('ublse_14')
    sprite('ubl232_05', 3)	# 28-30
    setInvincible(0)
    Recovery()
    Unknown2063()
    Unknown26('ubl_232_Eff')
    Unknown26('ubl_232_b_Eff')
    Unknown1019(40)
    SFX_3('ublse_15')
    sprite('ubl232_06', 3)	# 31-33
    Unknown1019(40)
    Unknown1019(0)
    SFX_3('ublse_00')
    sprite('ubl232_07', 3)	# 34-36
    sprite('ubl232_08', 4)	# 37-40
    sprite('ubl232_09', 4)	# 41-44

@Subroutine
def InitArmarAirParam():
    GuardPoint_(1)
    Unknown22030(0)
    Unknown22031(15, -1)
    Unknown22035(50)
    setInvincible(1)
    Unknown22019('0100000000000000000000000100000000000000')
    callSubroutine('InitArrmorVisualFunc')

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP1(80)
        HitOverhead(0)
        AirPushbackX(8000)
        AirPushbackY(10000)
        PushbackX(5000)
        ProjectileDurabilityLvl(1)
        ChipDamagePct(5)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Hitstop(3)
        Unknown11092(1)
        callSubroutine('CheckAtemiMuteki')
        callSubroutine('UniqueZLine')
    sprite('ubl250_00', 3)	# 1-3
    sprite('ubl250_01', 3)	# 4-6
    callSubroutine('InitArmarAirParam')
    sprite('ubl250_02ex', 1)	# 7-7	 **attackbox here**
    GFX_0('ubl_250_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    SFX_0('016_explode_1')
    Unknown22004(12, 1)
    sprite('ubl250_02', 1)	# 8-8	 **attackbox here**
    sprite('ubl250_02', 2)	# 9-10	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    GFX_0('ubl_250_Vulcan_Eff', 0)
    sprite('ubl250_02', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_250_Vulcan_Eff', 0)
    label(0)
    if (not (SLOT_51 >= 4)):
        SLOT_51 = (SLOT_51 + 1)
        if (not CheckInput(0x1)):
            sendToLabel(1)
    else:
        sendToLabel(1)
    sprite('ubl250_02', 2)	# 13-14	 **attackbox here**
    GFX_0('ubl_250_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    SFX_0('016_explode_1')
    sprite('ubl250_02', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_250_Vulcan_Eff', 0)
    sprite('ubl250_02', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    GFX_0('ubl_250_Vulcan_Eff', 0)
    loopRest()
    sendToLabel(0)
    label(1)
    sprite('ubl250_03', 3)	# 19-21
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ubl250_04', 3)	# 22-24
    sprite('ubl250_05', 3)	# 25-27

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Hitstop(3)
        Unknown11092(1)
        ProjectileDurabilityLvl(1)
        callSubroutine('UniqueZLine')
    sprite('ubl250_00', 3)	# 1-3
    sprite('ubl250_01', 3)	# 4-6
    sprite('ubl250_02', 1)	# 7-7	 **attackbox here**
    GFX_0('ubl_250_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    SFX_0('016_explode_1')
    sprite('ubl250_02', 1)	# 8-8	 **attackbox here**
    RefreshMultihit()
    sprite('ubl250_02', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    sprite('ubl250_03', 3)	# 10-12
    sprite('ubl250_04', 3)	# 13-15
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ubl250_05', 3)	# 16-18

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1800)
        AttackP1(80)
        AirPushbackY(-20000)
        AirUntechableTime(60)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        Unknown9118(1)
        Unknown9310(17)
        ChipDamagePct(5)
        ProjectileDurabilityLvl(1)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Hitstop(3)
        Unknown11092(1)
        callSubroutine('CheckAtemiMuteki')
        callSubroutine('UniqueZLine')
    sprite('ubl251_00', 3)	# 1-3
    sprite('ubl251_01', 3)	# 4-6
    Unknown1084(1)
    callSubroutine('InitArmarAirParam')
    sprite('ubl251_02', 7)	# 7-13
    sprite('ubl251_03', 3)	# 14-16	 **attackbox here**
    GFX_0('ubl_251_Shot_Eff', 0)
    GFX_0('ubl_251_Bomber_Eff', 1)
    physicsXImpulse(-10400)
    physicsYImpulse(28600)
    setGravity(2600)
    Unknown22004(12, 1)
    sprite('ubl251_04', 3)	# 17-19
    setInvincible(0)
    Recovery()
    Unknown2063()
    SFX_0('204_runjump_normal_2')
    sprite('ubl251_04', 4)	# 20-23
    sprite('ubl251_05', 6)	# 24-29
    sprite('ubl251_06', 6)	# 30-35
    sprite('ubl251_07', 6)	# 36-41

@Subroutine
def JCCancelInput():
    Unknown14070('CmnActInvincibleAttack')
    Unknown14070('DashAtack')
    Unknown14070('ShotBeamA')
    Unknown14070('ShotBeamB')
    Unknown14070('ShotBeamC')
    Unknown14070('GrenadeA')
    Unknown14070('GrenadeB')
    Unknown14070('GrenadeC')
    Unknown14070('UltimateBeam')
    Unknown14070('UltimateBeamSP')
    Unknown14070('UltimateRush')
    Unknown14070('UltimateRushSP')
    Unknown14070('AstralHeat')

@Subroutine
def JCCancelBegin():
    Unknown14072('CmnActInvincibleAttack')
    Unknown14072('DashAtack')
    Unknown14072('ShotBeamA')
    Unknown14072('ShotBeamB')
    Unknown14072('ShotBeamC')
    Unknown14072('GrenadeA')
    Unknown14072('GrenadeB')
    Unknown14072('GrenadeC')
    Unknown14072('UltimateBeam')
    Unknown14072('UltimateBeamSP')
    Unknown14072('UltimateRush')
    Unknown14072('UltimateRushSP')
    Unknown14072('AstralHeat')

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        AirPushbackX(2500)
        AirPushbackY(-16000)
        Unknown14077(0)

        def upon_11():
            SLOT_51 = 1
        Unknown2003(1)

        def upon_43():
            if (SLOT_48 == 1011):
                Unknown2037(1)
        callSubroutine('CheckAtemiMuteki')
        callSubroutine('UniqueZLine')
    sprite('ubl252_00', 3)	# 1-3
    sprite('ubl252_01', 3)	# 4-6	 **attackbox here**
    Unknown1017()
    Unknown1084(1)
    callSubroutine('InitArmarAirParam')
    StartMultihit()
    SFX_3('ublse_15')
    sprite('ubl252_02', 3)	# 7-9	 **attackbox here**
    StartMultihit()
    SFX_3('ublse_23')
    sprite('ubl252_03', 3)	# 10-12	 **attackbox here**
    StartMultihit()
    sprite('ubl252_01', 3)	# 13-15	 **attackbox here**
    StartMultihit()
    sprite('ubl252_02', 3)	# 16-18	 **attackbox here**
    StartMultihit()
    sprite('ubl252_03', 3)	# 19-21	 **attackbox here**
    StartMultihit()
    sprite('ubl252_01', 3)	# 22-24	 **attackbox here**
    StartMultihit()
    sprite('ubl252_02', 3)	# 25-27	 **attackbox here**
    Unknown1018()
    setGravity(2000)
    Unknown1015(10000)
    Unknown1021(-30000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    callSubroutine('JCCancelInput')
    sprite('ubl252_03', 3)	# 28-30	 **attackbox here**
    sprite('ubl252_01', 3)	# 31-33	 **attackbox here**
    label(0)
    sprite('ubl252_02', 3)	# 34-36	 **attackbox here**
    Unknown1018()
    setGravity(2000)
    Unknown1015(10000)
    Unknown1021(-30000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('ubl252_03', 3)	# 37-39	 **attackbox here**
    sprite('ubl252_01', 3)	# 40-42	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('ubl252_09', 2)	# 43-44
    GFX_1('ublef_252_landing_pos', 100)
    Recovery()
    Unknown2063()
    setInvincible(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    SFX_3('ublse_16')
    SFX_0('016_explode_2')
    ScreenShake(0, 30000)
    if (not SLOT_51):
        GFX_0('Air5CShakeAtk', -1)
    sprite('ubl252_10', 4)	# 45-48
    sprite('ubl252_11', 3)	# 49-51
    sprite('ubl252_12', 4)	# 52-55
    if SLOT_2:
        callSubroutine('JCCancelBegin')
    sprite('ubl252_13', 4)	# 56-59
    sprite('ubl252_14', 4)	# 60-63
    sprite('ubl252_15', 4)	# 64-67
    sprite('ubl252_16', 4)	# 68-71
    loopRest()

@Subroutine
def AtemiSwitch():
    if SLOT_4:
        SLOT_4 = 0
    else:
        SLOT_4 = 1

@Subroutine
def KoseiInit():
    if SLOT_36:
        Unknown17025('')
        clearUponHandler(2)

        def upon_5():
            Unknown1084(1)
    else:
        Unknown17024('')
        Unknown1084(1)
    GuardPoint_(1)
    Unknown22031(15, 21)

    def upon_52():
        Unknown2021(1)
        if Unknown23037():
            Unknown22031(-1, -1)

    def upon_42():
        clearUponHandler(42)
        Unknown23022(1)
        Unknown2037(1)
        Unknown2006()
        GFX_0('EffOffensiveGuardSuccess', 102)
        SFX_3('SE195_CounterBalanceB')
        GuardPoint_(0)
        if Unknown48('1900000002000000000000001a000000020000009e000000'):
            if Unknown23036():
                if (SLOT_19 <= 400000):
                    if SLOT_36:
                        enterState('OffensiveCounterAir')
                    else:
                        enterState('OffensiveCounterLand')
        callSubroutine('AtemiSwitch')

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 10):
                clearUponHandler(3)
                SLOT_51 = 0
                WhiffCancelEnable(1)
                Unknown13014(1)
                Unknown13015(1)
                Unknown13008(1)

    def upon_STATE_END():
        SLOT_4 = 0

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        callSubroutine('KoseiInit')
        SLOT_4 = 0
        SFX_3('SE193_GuardShieldInit')
        SFX_3('SE011')
    sprite('ubl040_00', 1)	# 1-1
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    GFX_0('EffOffensiveGuardStart', 0)
    GFX_0('EffOffensiveGuardBarier', 0)
    sprite('ubl040_00', 1)	# 2-2
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 3-3
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 4-4
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 5-5
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 6-6
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 7-7
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 8-8
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 9-9
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 10-10
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 11-11
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 12-12
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 13-13
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 14-14
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 15-15
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 16-16
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 17-17
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 18-18
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 19-19
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 20-20
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 21-21
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 22-22
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 23-23
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 24-24
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 25-25
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 26-26
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    setInvincible(0)
    sprite('ubl040_00', 1)	# 27-27
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 28-28
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 29-29
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 30-30
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 31-31
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 32-32
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 33-33
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 34-34
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 35-35
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 36-36
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 37-37
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 38-38
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 39-39
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 40-40
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 41-41
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_01', 1)	# 42-42
    Unknown23183('75626c3034355f30310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 43-43
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl040_00', 1)	# 44-44
    Unknown23183('75626c3034355f30300000000000000000000000000000000000000000000000010000000200000024000000')

@State
def OffensiveCounterLand():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(750)
        AttackP1(80)
        AttackP2(60)
        Unknown11001(0, 0, 0)
        AirPushbackX(12000)
        AirPushbackY(17000)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown30065(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown9266(6)
        Unknown2006()
        Unknown11092(1)
        callSubroutine('AtkEffLightning')
        Unknown2021(1)
        Unknown14083(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ubl320_00', 2)	# 1-2
    setInvincible(1)
    sprite('ubl320_01', 1)	# 3-3
    sprite('ubl320_02', 1)	# 4-4
    sprite('ubl320_03', 1)	# 5-5
    GFX_0('ubl_320_NearSpark_Eff', 100)
    GFX_0('ubl_310_BackSpark_Eff', 100)
    SFX_0('014_electric_sl')
    SFX_0('014_electric_sl')
    Unknown23119(4128831, 3, -1)
    sprite('ubl320_04', 1)	# 6-6	 **attackbox here**
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    SFX_0('014_electric_s')
    sprite('ubl320_07', 7)	# 19-25	 **attackbox here**
    StartMultihit()
    sprite('ubl320_08', 8)	# 26-33
    sprite('ubl320_09', 8)	# 34-41

@State
def OffensiveCounterAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(750)
        AttackP1(80)
        AttackP2(60)
        Unknown11001(0, 0, 0)
        AirPushbackX(12000)
        AirPushbackY(17000)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown30065(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown9266(6)
        Unknown2006()
        Unknown11092(1)
        callSubroutine('AtkEffLightning')
        Unknown2021(1)
        Unknown14083(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ubl320_00', 2)	# 1-2
    setInvincible(1)
    physicsXImpulse(5000)
    Unknown1028(-500)
    physicsYImpulse(0)
    setGravity(0)
    sprite('ubl320_01', 1)	# 3-3
    sprite('ubl320_02', 1)	# 4-4
    physicsXImpulse(0)
    Unknown1028(0)
    sprite('ubl320_03', 1)	# 5-5
    GFX_0('ubl_320_NearSpark_Eff', 100)
    GFX_0('ubl_310_BackSpark_Eff', 100)
    SFX_0('014_electric_sl')
    SFX_0('014_electric_sl')
    Unknown23119(4128831, 3, -1)
    sprite('ubl320_04', 1)	# 6-6	 **attackbox here**
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    SFX_0('014_electric_s')
    sprite('ubl320_07', 7)	# 19-25	 **attackbox here**
    StartMultihit()
    Unknown1043()
    sprite('ubl320_08', 2)	# 26-27
    sprite('ubl320_09', 2)	# 28-29
    label(0)
    sprite('ubl020_00', 3)	# 30-32
    sprite('ubl020_01', 3)	# 33-35
    sprite('ubl020_02', 3)	# 36-38
    loopRest()
    gotoLabel(0)

@State
def DashAtack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2000)
        AttackP1(80)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(36000)
        AirPushbackY(23000)
        blockstun(23)
        AirUntechableTime(40)
        Hitstop(20)
        ScreenShake(4000, 4000)
        Unknown11032('d0dd0600ffffffffffffffffffffffff')
        Unknown11001(0, -4, 4)
        Unknown11056(0)
        callSubroutine('InitArrmorVisualFunc')
        SLOT_4 = 1

        def upon_77():
            clearUponHandler(3)
            clearUponHandler(77)
            sendToLabel(1)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(4000, 4000)
    sprite('ubl403_00', 3)	# 1-3
    GFX_0('ubl_Dash_Eff', 100)
    SFX_3('ublse_01')
    SFX_3('ublse_01')
    sprite('ubl403_01', 3)	# 4-6
    physicsXImpulse(62000)
    setInvincible(1)
    Unknown22019('0000000001000000000000000100000000000000')
    Unknown22030(0)
    GuardPoint_(1)
    Unknown22035(50)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 < 200000):
            clearUponHandler(3)
            SLOT_51 = 1
            Unknown1019(0)
            Unknown1045(50000)
    SFX_3('ublse_21')
    sprite('ubl403_02', 1)	# 7-7	 **attackbox here**
    SFX_3('ublse_15')
    sprite('ubl403_02', 2)	# 8-9	 **attackbox here**
    setInvincible(0)
    if SLOT_51:
        sendToLabel(2)
    sprite('ubl403_03', 3)	# 10-12	 **attackbox here**
    SFX_3('ublse_15')
    sprite('ubl403_04', 3)	# 13-15	 **attackbox here**
    sprite('ubl403_04', 3)	# 16-18	 **attackbox here**
    SFX_3('ublse_15')
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('ubl004_00', 2)	# 19-20
    Unknown1019(10)
    clearUponHandler(3)
    clearUponHandler(77)
    setInvincible(0)
    DisableAttackRestOfMove()
    SFX_3('ublse_15')
    sprite('ubl004_01', 2)	# 21-22
    sprite('ubl004_02', 3)	# 23-25
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 4)	# 26-29
    SFX_3('ublse_15')
    sprite('ubl004_04', 4)	# 30-33
    physicsXImpulse(0)
    Unknown1045(0)
    Unknown26('ubl_Dash_Eff')
    sprite('ubl004_05', 3)	# 34-36
    sprite('ubl004_06', 3)	# 37-39
    sprite('ubl004_07', 3)	# 40-42
    sprite('ubl004_08', 3)	# 43-45
    ExitState()
    label(2)
    sprite('ubl004_00', 2)	# 46-47
    Unknown1019(10)
    clearUponHandler(3)
    clearUponHandler(77)
    setInvincible(0)
    DisableAttackRestOfMove()
    SFX_3('ublse_15')
    sprite('ubl004_01', 2)	# 48-49
    sprite('ubl004_02', 6)	# 50-55
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 6)	# 56-61
    SFX_3('ublse_15')
    sprite('ubl004_04', 6)	# 62-67
    physicsXImpulse(0)
    Unknown1045(0)
    Unknown26('ubl_Dash_Eff')
    sprite('ubl004_05', 6)	# 68-73
    sprite('ubl004_06', 6)	# 74-79
    sprite('ubl004_07', 6)	# 80-85
    sprite('ubl004_08', 6)	# 86-91

@State
def ShotBeamA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl400_00', 4)	# 1-4
    sprite('ubl400_01', 4)	# 5-8
    sprite('ubl400_02', 4)	# 9-12
    sprite('ubl400_03', 2)	# 13-14
    sprite('ubl400_04', 1)	# 15-15
    GFX_0('ShotBeam_Low', 0)
    SFX_3('ublse_07')
    sprite('ubl400_04', 3)	# 16-18
    sprite('ubl400_04', 5)	# 19-23
    sprite('ubl400_05', 5)	# 24-28
    sprite('ubl400_06', 5)	# 29-33
    sprite('ubl400_07', 5)	# 34-38
    sprite('ubl400_08', 5)	# 39-43
    sprite('ubl400_09', 4)	# 44-47

@State
def ShotBeamB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl400_10', 4)	# 1-4
    sprite('ubl400_11', 4)	# 5-8
    sprite('ubl400_12', 4)	# 9-12
    sprite('ubl400_13', 2)	# 13-14
    sprite('ubl400_14', 1)	# 15-15
    GFX_0('ShotBeam_Middle', 0)
    SFX_3('ublse_07')
    sprite('ubl400_14', 3)	# 16-18
    sprite('ubl400_14', 5)	# 19-23
    sprite('ubl400_15', 6)	# 24-29
    sprite('ubl400_16', 6)	# 30-35
    sprite('ubl400_17', 6)	# 36-41
    sprite('ubl400_18', 6)	# 42-47
    sprite('ubl400_19', 6)	# 48-53

@State
def ShotBeamC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl400_20', 4)	# 1-4
    sprite('ubl400_21', 4)	# 5-8
    sprite('ubl400_22', 4)	# 9-12
    sprite('ubl400_23', 2)	# 13-14
    sprite('ubl400_24', 1)	# 15-15
    GFX_0('ShotBeam_High', 0)
    SFX_3('ublse_07')
    sprite('ubl400_24', 3)	# 16-18
    sprite('ubl400_25', 4)	# 19-22
    sprite('ubl400_26', 4)	# 23-26
    sprite('ubl400_27', 4)	# 27-30
    sprite('ubl400_28', 4)	# 31-34
    sprite('ubl400_29', 4)	# 35-38

@State
def AirShotBeamA():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl401_00', 3)	# 1-3
    sprite('ubl401_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    sprite('ubl401_02', 3)	# 7-9
    sprite('ubl401_03', 2)	# 10-11
    sprite('ubl401_04', 1)	# 12-12
    GFX_0('AirShotBeam_Low', 0)
    SFX_3('ublse_07')
    sprite('ubl401_04', 3)	# 13-15
    sprite('ubl401_05', 5)	# 16-20
    Unknown1018()
    Unknown1043()
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('ubl401_06', 5)	# 21-25
    sprite('ubl401_07', 5)	# 26-30
    sprite('ubl401_08', 5)	# 31-35
    sprite('ubl401_09', 5)	# 36-40
    label(0)
    sprite('ubl020_00', 3)	# 41-43
    sprite('ubl020_01', 3)	# 44-46
    sprite('ubl020_02', 3)	# 47-49
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl252_14', 6)	# 50-55
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('ublef_landing_pos', 100)
    SFX_3('ublse_16')
    sprite('ubl252_15', 2)	# 56-57
    sprite('ubl252_16', 2)	# 58-59

@State
def AirShotBeamB():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl401_10', 3)	# 1-3
    sprite('ubl401_11', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    sprite('ubl401_12', 3)	# 7-9
    sprite('ubl401_13', 2)	# 10-11
    sprite('ubl401_14', 1)	# 12-12
    GFX_0('AirShotBeam_Middle', 0)
    SFX_3('ublse_07')
    sprite('ubl401_14', 3)	# 13-15
    sprite('ubl401_15', 5)	# 16-20
    Unknown1018()
    Unknown1043()
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('ubl401_16', 5)	# 21-25
    sprite('ubl401_17', 5)	# 26-30
    sprite('ubl401_18', 5)	# 31-35
    sprite('ubl401_19', 5)	# 36-40
    label(0)
    sprite('ubl020_00', 3)	# 41-43
    sprite('ubl020_01', 3)	# 44-46
    sprite('ubl020_02', 3)	# 47-49
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl252_14', 6)	# 50-55
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('ublef_landing_pos', 100)
    SFX_3('ublse_16')
    sprite('ubl252_15', 2)	# 56-57
    sprite('ubl252_16', 2)	# 58-59

@State
def AirShotBeamC():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(12, 1)
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl401_10', 3)	# 1-3
    sprite('ubl401_11', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    sprite('ubl401_12', 3)	# 7-9
    sprite('ubl401_13', 2)	# 10-11
    sprite('ubl401_14', 1)	# 12-12
    GFX_0('AirShotBeam_High', 0)
    SFX_3('ublse_07')
    sprite('ubl401_14', 3)	# 13-15
    sprite('ubl401_15', 5)	# 16-20
    Unknown1018()
    Unknown1043()
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('ubl401_16', 5)	# 21-25
    sprite('ubl401_17', 5)	# 26-30
    sprite('ubl401_18', 5)	# 31-35
    sprite('ubl401_19', 5)	# 36-40
    label(0)
    sprite('ubl020_00', 3)	# 41-43
    sprite('ubl020_01', 3)	# 44-46
    sprite('ubl020_02', 3)	# 47-49
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl252_14', 6)	# 50-55
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('ublef_landing_pos', 100)
    SFX_3('ublse_16')
    sprite('ubl252_15', 2)	# 56-57
    sprite('ubl252_16', 2)	# 58-59

@State
def GrenadeA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl402_00', 3)	# 1-3
    sprite('ubl402_01', 3)	# 4-6
    sprite('ubl402_02', 3)	# 7-9
    sprite('ubl402_03', 3)	# 10-12
    sprite('ubl402_02', 3)	# 13-15
    sprite('ubl402_03', 3)	# 16-18
    sprite('ubl402_04', 3)	# 19-21
    sprite('ubl402_05', 4)	# 22-25
    GFX_0('GrenadeA_Shot', 0)
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    sprite('ubl402_06', 5)	# 26-30
    sprite('ubl402_07', 5)	# 31-35
    sprite('ubl402_08', 5)	# 36-40
    sprite('ubl402_09', 5)	# 41-45
    sprite('ubl402_10', 5)	# 46-50

@State
def GrenadeB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl402_00', 3)	# 1-3
    sprite('ubl402_01', 3)	# 4-6
    sprite('ubl402_02', 3)	# 7-9
    sprite('ubl402_03', 3)	# 10-12
    sprite('ubl402_02', 3)	# 13-15
    sprite('ubl402_03', 3)	# 16-18
    sprite('ubl402_04', 3)	# 19-21
    sprite('ubl402_05', 4)	# 22-25
    GFX_0('GrenadeB_Shot', 0)
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    sprite('ubl402_06', 5)	# 26-30
    sprite('ubl402_07', 5)	# 31-35
    sprite('ubl402_08', 5)	# 36-40
    sprite('ubl402_09', 5)	# 41-45
    sprite('ubl402_10', 5)	# 46-50

@State
def GrenadeC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl402_00', 2)	# 1-2
    sprite('ubl402_01', 1)	# 3-3
    sprite('ubl402_01', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('ubl402_02', 2)	# 5-6
    sprite('ubl402_03', 2)	# 7-8
    sprite('ubl402_02', 2)	# 9-10
    sprite('ubl402_03', 2)	# 11-12
    sprite('ubl402_04', 2)	# 13-14
    sprite('ubl402_05', 3)	# 15-17
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    GFX_0('GrenadeA_Shot', 2)
    Unknown38(6, 1)
    GFX_0('GrenadeB_Shot', 0)
    Unknown38(7, 1)
    GFX_0('GrenadeC_Shot', 1)
    Unknown38(8, 1)
    Unknown23029(6, 1012, 0)
    Unknown23029(7, 1013, 0)
    Unknown23029(8, 1014, 0)
    sprite('ubl402_06', 4)	# 18-21
    sprite('ubl402_07', 4)	# 22-25
    sprite('ubl402_08', 4)	# 26-29
    sprite('ubl402_09', 4)	# 30-33
    sprite('ubl402_10', 4)	# 34-37

@State
def AirGrenadeA():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)

        def upon_LANDING():
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            ScreenShake(0, 10000)
            GFX_1('ublef_landing_pos', 100)
            SFX_3('ublse_16')
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl402_00', 1)	# 1-1
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_00', 1)	# 2-2
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_00', 1)	# 3-3
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_01', 1)	# 4-4
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_36:
        Unknown1019(50)
    sprite('ubl402_01', 1)	# 5-5
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_01', 1)	# 6-6
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 7-7
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 8-8
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 9-9
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 10-10
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 11-11
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 12-12
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 13-13
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 14-14
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 15-15
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 16-16
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 17-17
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 18-18
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 19-19
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 20-20
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 21-21
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 22-22
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    if SLOT_36:
        GFX_0('GrenadeA_Shot', 0)
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_37:
        GFX_0('GrenadeA_Shot', 0)
    sprite('ubl402_05', 1)	# 23-23
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 24-24
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 25-25
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 26-26
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 27-27
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 28-28
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 29-29
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 30-30
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 31-31
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 32-32
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 33-33
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 34-34
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 35-35
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 36-36
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 37-37
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 38-38
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 39-39
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 40-40
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 41-41
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 42-42
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 43-43
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 44-44
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 45-45
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 46-46
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 47-47
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 48-48
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 49-49
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 50-50
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_36:
        sendToLabel(0)
        sendToLabelUpon(5, 1)
    else:
        sendToLabel(1)
    label(0)
    sprite('ubl020_00', 3)	# 51-53
    Unknown22004(7, 1)
    sprite('ubl020_01', 3)	# 54-56
    sprite('ubl020_02', 3)	# 57-59
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 60-60

@State
def AirGrenadeB():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)

        def upon_LANDING():
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            ScreenShake(0, 10000)
            GFX_1('ublef_landing_pos', 100)
            SFX_3('ublse_16')
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl402_00', 1)	# 1-1
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_00', 1)	# 2-2
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_00', 1)	# 3-3
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_01', 1)	# 4-4
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_36:
        Unknown1019(50)
    sprite('ubl402_01', 1)	# 5-5
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_01', 1)	# 6-6
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 7-7
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 8-8
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 9-9
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 10-10
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 11-11
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 12-12
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 13-13
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 14-14
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 15-15
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 16-16
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 17-17
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 18-18
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 19-19
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 20-20
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 21-21
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 22-22
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    if SLOT_36:
        GFX_0('GrenadeB_Shot', 0)
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_37:
        GFX_0('GrenadeB_Shot', 0)
    sprite('ubl402_05', 1)	# 23-23
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 24-24
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 25-25
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 26-26
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 27-27
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 28-28
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 29-29
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 30-30
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 31-31
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 32-32
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 33-33
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 34-34
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 35-35
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 36-36
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 37-37
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 38-38
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 39-39
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 40-40
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 41-41
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 42-42
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 43-43
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 44-44
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 45-45
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 46-46
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 47-47
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 48-48
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 49-49
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 50-50
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_36:
        sendToLabel(0)
        sendToLabelUpon(5, 1)
    else:
        sendToLabel(1)
    label(0)
    sprite('ubl020_00', 3)	# 51-53
    Unknown22004(7, 1)
    sprite('ubl020_01', 3)	# 54-56
    sprite('ubl020_02', 3)	# 57-59
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 60-60

@State
def AirGrenadeC():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)

        def upon_LANDING():
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            ScreenShake(0, 10000)
            GFX_1('ublef_landing_pos', 100)
            SFX_3('ublse_16')
        callSubroutine('UniqueZLineSpecial')
    sprite('ubl402_00', 1)	# 1-1
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_00', 1)	# 2-2
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_00', 1)	# 3-3
    Unknown23183('75626c3430325f31310000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_01', 1)	# 4-4
    if SLOT_37:
        Unknown23125('')
        ConsumeSuperMeter(-5000)
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_36:
        Unknown1019(50)
        Unknown23125('')
        ConsumeSuperMeter(-5000)
    sprite('ubl402_01', 1)	# 5-5
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_01', 1)	# 6-6
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 7-7
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 8-8
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 9-9
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 10-10
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 11-11
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 12-12
    Unknown23183('75626c3430325f31340000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 13-13
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 14-14
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_02', 1)	# 15-15
    Unknown23183('75626c3430325f31320000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 16-16
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 17-17
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_03', 1)	# 18-18
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 19-19
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 20-20
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_04', 1)	# 21-21
    Unknown23183('75626c3430325f31350000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 22-22
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    if SLOT_36:
        GFX_0('GrenadeA_Shot', 2)
        Unknown38(6, 1)
        GFX_0('GrenadeB_Shot', 0)
        Unknown38(7, 1)
        GFX_0('GrenadeC_Shot', 1)
        Unknown38(8, 1)
        Unknown23029(6, 1012, 0)
        Unknown23029(7, 1013, 0)
        Unknown23029(8, 1014, 0)
    Unknown23183('75626c3430325f31330000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_37:
        GFX_0('GrenadeA_Shot', 2)
        Unknown38(6, 1)
        GFX_0('GrenadeB_Shot', 0)
        Unknown38(7, 1)
        GFX_0('GrenadeC_Shot', 1)
        Unknown38(8, 1)
        Unknown23029(6, 1012, 0)
        Unknown23029(7, 1013, 0)
        Unknown23029(8, 1014, 0)
    sprite('ubl402_05', 1)	# 23-23
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 24-24
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_05', 1)	# 25-25
    Unknown23183('75626c3430325f31360000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 26-26
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 27-27
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 28-28
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_06', 1)	# 29-29
    Unknown23183('75626c3430325f31370000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 30-30
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 31-31
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 32-32
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_07', 1)	# 33-33
    Unknown23183('75626c3430325f31380000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 34-34
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 35-35
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 36-36
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_08', 1)	# 37-37
    Unknown23183('75626c3430325f31390000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 38-38
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 39-39
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 40-40
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_09', 1)	# 41-41
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 42-42
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 43-43
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 44-44
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    sprite('ubl402_10', 1)	# 45-45
    Unknown23183('75626c3430325f32300000000000000000000000000000000000000000000000010000000200000024000000')
    if SLOT_36:
        sendToLabel(0)
        sendToLabelUpon(5, 1)
    else:
        sendToLabel(1)
    label(0)
    sprite('ubl020_00', 3)	# 46-48
    Unknown22004(7, 1)
    sprite('ubl020_01', 3)	# 49-51
    sprite('ubl020_02', 3)	# 52-54
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 55-55

@State
def UltimateBeam():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 40):
                Unknown20000(0)
            if (SLOT_51 >= 7):
                clearUponHandler(3)
                sendToLabel(1)
        loopRelated(17, 183)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
        callSubroutine('UniqueZLineUltimate')
    sprite('ubl430_00', 3)	# 1-3
    Unknown2036(80, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    setInvincibleFor(80)
    sprite('ubl430_01', 3)	# 4-6
    sprite('ubl430_02', 3)	# 7-9
    SFX_3('ublse_03')
    SFX_3('ublse_03')
    sprite('ubl430_03', 3)	# 10-12
    Unknown20000(1)
    sprite('ubl430_04', 3)	# 13-15
    sprite('ubl430_05', 3)	# 16-18
    sprite('ubl430_06', 3)	# 19-21
    sprite('ubl430_07', 3)	# 22-24
    GFX_0('ubl_UltimateBeam_Charge_Eff', 0)
    SFX_3('ublse_14')
    SFX_3('ublse_14')
    SFX_3('ublse_12')
    SFX_3('ublse_12')
    sprite('ubl430_08', 3)	# 25-27
    sprite('ubl430_09', 3)	# 28-30
    GFX_0('ubl_UltimateBeam_Lightbullet_Ef', 0)
    label(0)
    sprite('ubl430_10', 3)	# 31-33
    SLOT_51 = (SLOT_51 + 1)
    sprite('ubl430_11', 3)	# 34-36
    sprite('ubl430_12', 3)	# 37-39
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl430_13', 3)	# 40-42
    GFX_0('UltimateBeam_AtkCol', 0)
    Unknown26('ubl_UltimateBeam_Charge_Eff')
    Unknown26('ubl_UltimateBeam_Lightbullet_Ef')
    GFX_0('ubl_UltimateBeam_Eff', 0)
    GFX_0('ubl_UltimateBeam_Muzzle_Eff', 0)
    GFX_0('ubl_UltimateBeam_Wave_Eff', 0)
    SFX_3('ublse_07')
    SFX_3('ublse_08')
    label(2)
    sprite('ubl430_14', 3)	# 43-45
    sprite('ubl430_15', 3)	# 46-48
    sprite('ubl430_16', 3)	# 49-51
    sprite('ubl430_13', 3)	# 52-54
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('ubl430_17', 3)	# 55-57
    SFX_3('ublse_02')
    sprite('ubl430_18', 3)	# 58-60
    sprite('ubl430_19', 3)	# 61-63
    sprite('ubl430_20', 3)	# 64-66
    sprite('ubl430_21', 3)	# 67-69
    sprite('ubl430_22', 3)	# 70-72
    sprite('ubl430_23', 3)	# 73-75
    SFX_3('ublse_04')
    sprite('ubl430_24', 3)	# 76-78
    sprite('ubl430_25', 3)	# 79-81
    sprite('ubl430_26', 3)	# 82-84

@State
def UltimateBeamSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 40):
                Unknown20000(0)
            if (SLOT_51 >= 7):
                clearUponHandler(3)
                sendToLabel(1)
        loopRelated(17, 235)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
        callSubroutine('UniqueZLineUltimate')
    sprite('ubl430_00', 3)	# 1-3
    Unknown2036(80, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    setInvincibleFor(80)
    sprite('ubl430_01', 3)	# 4-6
    sprite('ubl430_02', 3)	# 7-9
    SFX_3('ublse_03')
    SFX_3('ublse_03')
    sprite('ubl430_03', 3)	# 10-12
    Unknown20000(1)
    sprite('ubl430_04', 3)	# 13-15
    sprite('ubl430_05', 3)	# 16-18
    sprite('ubl430_06', 3)	# 19-21
    sprite('ubl430_07', 3)	# 22-24
    GFX_0('ubl_UltimateBeam_Charge_Eff', 0)
    SFX_3('ublse_14')
    SFX_3('ublse_14')
    SFX_3('ublse_12')
    SFX_3('ublse_12')
    sprite('ubl430_08', 3)	# 25-27
    sprite('ubl430_09', 3)	# 28-30
    GFX_0('ubl_UltimateBeam_Lightbullet_Ef', 0)
    label(0)
    sprite('ubl430_10', 3)	# 31-33
    SLOT_51 = (SLOT_51 + 1)
    sprite('ubl430_11', 3)	# 34-36
    sprite('ubl430_12', 3)	# 37-39
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl430_13', 3)	# 40-42
    GFX_0('UltimateBeam_AtkCol', 0)
    Unknown23029(1, 2001, 0)
    Unknown26('ubl_UltimateBeam_Charge_Eff')
    Unknown26('ubl_UltimateBeam_Lightbullet_Ef')
    GFX_0('ubl_UltimateBeam_Eff', 0)
    GFX_0('ubl_UltimateBeam_Muzzle_Eff', 0)
    GFX_0('ubl_UltimateBeam_Wave_Eff', 0)
    SFX_3('ublse_07')
    SFX_3('ublse_08')
    label(2)
    sprite('ubl430_14', 3)	# 43-45
    sprite('ubl430_15', 3)	# 46-48
    sprite('ubl430_16', 3)	# 49-51
    sprite('ubl430_13', 3)	# 52-54
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('ubl430_17', 3)	# 55-57
    SFX_3('ublse_02')
    sprite('ubl430_18', 3)	# 58-60
    sprite('ubl430_19', 3)	# 61-63
    sprite('ubl430_20', 3)	# 64-66
    sprite('ubl430_21', 3)	# 67-69
    sprite('ubl430_22', 3)	# 70-72
    sprite('ubl430_23', 3)	# 73-75
    SFX_3('ublse_04')
    sprite('ubl430_24', 3)	# 76-78
    sprite('ubl430_25', 3)	# 79-81
    sprite('ubl430_26', 3)	# 82-84

@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
        setInvincible(1)
        AttackLevel_(5)
        Damage(4000)
        AttackP1(80)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        YImpluseBeforeWallbounce(160)
        Unknown9310(1)
        AirPushbackX(0)
        AirPushbackY(8000)
        AirUntechableTime(500)
        Hitstop(40)
        MinimumDamagePct(22)
        Unknown11069('UltimateRush')

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(17)
            EnableCollision(0)
            Unknown3077(950)
            Unknown13024(0)
            ScreenShake(20000, 40000)
            sendToLabel(10)

        def upon_80():
            clearUponHandler(80)
            clearUponHandler(17)
            sendToLabel(9)

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 93):
                Unknown20000(0)
                Unknown1015(500)
                Unknown3029(1)
                Unknown3069(1)
                Unknown3070(3)
                Unknown3071(10)
                Unknown3076(1100)
            if (SLOT_51 >= 120):
                clearUponHandler(3)
                sendToLabel(1)
        loopRelated(17, 130)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)

        def upon_STATE_END():
            EnableCollision(1)
        callSubroutine('UniqueZLineUltimate')
    sprite('ubl431_00', 3)	# 1-3
    Unknown2036(115, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    GFX_0('ubl_Dash_Eff', 100)
    GFX_0('ubl_431_Smoke_Eff', 100)
    GFX_0('ubl_431_Eyes_Eff', 100)
    sprite('ubl431_01', 3)	# 4-6
    sprite('ubl431_02', 3)	# 7-9
    SFX_3('ublse_11')
    SFX_3('ublse_11')
    sprite('ubl431_03', 3)	# 10-12
    Unknown20000(1)
    Unknown2016(400)
    sprite('ubl431_04', 3)	# 13-15
    label(0)
    sprite('ubl431_05', 3)	# 16-18
    sprite('ubl431_06', 3)	# 19-21
    sprite('ubl431_07', 3)	# 22-24
    sprite('ubl431_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl431_09', 3)	# 28-30
    GFX_0('ubl_431_Dash_Eff', 100)
    GFX_0('ubl_431_Dash02_Eff', 100)
    Unknown1015(110000)
    SFX_3('ublse_01')
    SFX_3('ublse_01')
    SFX_3('ublse_21')
    label(2)
    sprite('ubl403_02', 3)	# 31-33	 **attackbox here**
    GFX_0('ubl_431_Dash_Eff', 100)
    SFX_3('ublse_15')
    sprite('ubl403_03', 3)	# 34-36	 **attackbox here**
    SFX_3('ublse_15')
    sprite('ubl403_04', 3)	# 37-39	 **attackbox here**
    SFX_3('ublse_15')
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('ubl403_02', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(80000)
    AirUntechableTime(500)
    Hitstop(0)
    Unknown9095()
    Unknown11001(0, 0, 0)
    Unknown11023(1)
    Unknown11069('')
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    ScreenShake(20000, 40000)
    SFX_0('025_cleanhit_grap')
    sprite('ubl403_03', 3)	# 43-45	 **attackbox here**
    sprite('ubl403_04', 50)	# 46-95	 **attackbox here**
    SFX_3('ublse_15')
    SFX_0('016_explode_2')
    label(9)
    sprite('ubl004_00', 2)	# 96-97
    Unknown1019(0)
    Unknown1045(10000)
    setInvincible(0)
    Unknown2016(-1)
    Unknown26('ubl_Dash_Eff')
    Unknown26('ubl_431_Smoke_Eff')
    Unknown26('ubl_431_Dash_Eff')
    SFX_3('ublse_03')
    SFX_3('ublse_00')
    sprite('ubl004_01', 2)	# 98-99
    sprite('ubl004_02', 8)	# 100-107
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 8)	# 108-115
    sprite('ubl004_04', 8)	# 116-123
    sprite('ubl004_05', 8)	# 124-131
    Unknown13024(1)
    sprite('ubl004_06', 8)	# 132-139
    sprite('ubl004_07', 2)	# 140-141
    sprite('ubl004_07', 6)	# 142-147
    if (SLOT_163 < 0):
        sendToLabel(20)
    sprite('ubl004_08', 8)	# 148-155
    loopRest()
    ExitState()
    label(20)
    sprite('ubl003_00', 4)	# 156-159
    Unknown2005()
    sprite('ubl003_02', 5)	# 160-164
    sprite('ubl003_00ex01', 5)	# 165-169

@State
def UltimateRushSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
        setInvincible(1)
        AttackLevel_(5)
        Damage(4700)
        AttackP1(80)
        MinimumDamagePct(22)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        YImpluseBeforeWallbounce(160)
        AirPushbackX(0)
        AirPushbackY(8000)
        Unknown9310(1)
        AirUntechableTime(500)
        Hitstop(40)
        Unknown11069('UltimateRushSP')

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(17)
            EnableCollision(0)
            Unknown3077(950)
            Unknown13024(0)
            Unknown20000(1)
            ScreenShake(30000, 50000)
            sendToLabel(10)

        def upon_80():
            clearUponHandler(80)
            clearUponHandler(17)
            sendToLabel(9)

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 93):
                Unknown20000(0)
                Unknown1015(500)
                Unknown3029(1)
                Unknown3069(1)
                Unknown3070(3)
                Unknown3071(10)
                Unknown3076(1100)
            if (SLOT_51 >= 120):
                clearUponHandler(3)
                sendToLabel(1)
        loopRelated(17, 130)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)

        def upon_STATE_END():
            Unknown20000(0)
            EnableCollision(1)
        callSubroutine('UniqueZLineUltimate')
    sprite('ubl431_00', 3)	# 1-3
    Unknown2036(115, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    GFX_0('ubl_Dash_Eff', 100)
    GFX_0('ubl_431_Smoke_Eff', 100)
    GFX_0('ubl_431_Eyes_Eff', 100)
    sprite('ubl431_01', 3)	# 4-6
    sprite('ubl431_02', 3)	# 7-9
    SFX_3('ublse_11')
    SFX_3('ublse_11')
    sprite('ubl431_03', 3)	# 10-12
    Unknown20000(1)
    Unknown2016(400)
    sprite('ubl431_04', 3)	# 13-15
    label(0)
    sprite('ubl431_05', 3)	# 16-18
    sprite('ubl431_06', 3)	# 19-21
    sprite('ubl431_07', 3)	# 22-24
    sprite('ubl431_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl431_09', 3)	# 28-30
    Unknown1015(110000)
    SFX_3('ublse_01')
    SFX_3('ublse_01')
    SFX_3('ublse_21')
    GFX_0('ubl_431_Dash_Eff', 100)
    GFX_0('ubl_431_Dash02_Eff', 100)
    label(2)
    sprite('ubl403_02', 3)	# 31-33	 **attackbox here**
    GFX_0('ubl_431_Dash_Eff', 100)
    SFX_3('ublse_15')
    sprite('ubl403_03', 3)	# 34-36	 **attackbox here**
    SFX_3('ublse_15')
    sprite('ubl403_04', 3)	# 37-39	 **attackbox here**
    SFX_3('ublse_15')
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('ubl403_02', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(80000)
    AirUntechableTime(500)
    Hitstop(0)
    Unknown9095()
    Unknown11001(0, 0, 0)
    Unknown11023(1)
    Unknown11069('')
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    ScreenShake(30000, 50000)
    SFX_0('025_cleanhit_grap')
    sprite('ubl403_03', 3)	# 43-45	 **attackbox here**
    sprite('ubl403_04', 50)	# 46-95	 **attackbox here**
    Unknown1019(0)
    Unknown1045(124000)
    SLOT_52 = 1
    SFX_3('ublse_15')
    SFX_0('016_explode_2')
    label(9)
    sprite('ubl004_00', 2)	# 96-97
    Unknown1019(0)
    if (not SLOT_52):
        Unknown1045(10000)
    setInvincible(0)
    Unknown2016(-1)
    Unknown26('ubl_Dash_Eff')
    Unknown26('ubl_431_Dash_Eff')
    Unknown26('ubl_431_Smoke_Eff')
    SFX_3('ublse_03')
    SFX_3('ublse_00')
    sprite('ubl004_01', 2)	# 98-99
    sprite('ubl004_02', 8)	# 100-107
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 8)	# 108-115
    sprite('ubl004_04', 8)	# 116-123
    sprite('ubl004_05', 8)	# 124-131
    Unknown20000(0)
    Unknown13024(1)
    sprite('ubl004_06', 8)	# 132-139
    sprite('ubl004_07', 2)	# 140-141
    sprite('ubl004_07', 6)	# 142-147
    if (SLOT_163 < 0):
        sendToLabel(20)
    sprite('ubl004_08', 8)	# 148-155
    loopRest()
    ExitState()
    label(20)
    sprite('ubl003_00', 4)	# 156-159
    Unknown2005()
    sprite('ubl003_02', 5)	# 160-164
    sprite('ubl003_00ex01', 5)	# 165-169

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Damage(0)
        Unknown11056(0)
        AirUntechableTime(60)
        hitstun(60)
        AirPushbackX(-12500)
        AirPushbackY(36000)
        PushbackX(-19800)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11072(1, 50000, 0)
        Unknown11068(1)
        Unknown11078(1)
        AirUntechableTime(999)

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(11)
            Unknown23088(1, 1)
            PushbackX(0)
            Unknown11069('Grenade_Shot_Astral')
            enterState('AstralHeatExe')
            SFX_0('025_cleanhit_grap')

        def upon_11():
            clearUponHandler(3)
            sendToLabel(9)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 100):
                sendToLabel(1)
            if (SLOT_18 == 120):
                sendToLabel(9)
        callSubroutine('UniqueZLineUltimate')
    sprite('ubl431_00', 3)	# 1-3
    setInvincible(1)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2036(85, -1, 2)
    Unknown23147()
    Unknown2015(10)
    sprite('ubl431_01', 3)	# 4-6
    GFX_0('ubl_Dash_Eff', 100)
    GFX_0('ubl_431_Smoke_Eff', 100)
    GFX_0('ubl_431_Eyes_Eff', 100)
    sprite('ubl431_02', 3)	# 7-9
    SFX_3('ublse_11')
    SFX_3('ublse_11')
    sprite('ubl431_03', 3)	# 10-12
    sprite('ubl431_04', 3)	# 13-15
    label(0)
    sprite('ubl431_05', 3)	# 16-18
    sprite('ubl431_06', 3)	# 19-21
    sprite('ubl431_07', 3)	# 22-24
    sprite('ubl431_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ubl431_09', 3)	# 28-30
    GFX_0('ubl_431_Dash_Eff', 100)
    SFX_3('ublse_01')
    SFX_3('ublse_01')
    Unknown1015(110000)
    label(2)
    sprite('ubl403_02', 3)	# 31-33	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    SFX_3('ublse_15')
    sprite('ubl403_03', 3)	# 34-36	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    SFX_3('ublse_15')
    sprite('ubl403_04', 3)	# 37-39	 **attackbox here**
    SFX_3('ublse_15')
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ubl403_02', 3)	# 40-42	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    StartMultihit()
    Unknown1019(40)
    EnableCollision(0)
    setInvincible(0)
    sprite('ubl403_03', 3)	# 43-45	 **attackbox here**
    GFX_0('ubl_forward_Eff', 100)
    SFX_3('ublse_15')
    StartMultihit()
    loopRest()
    sprite('ubl450_00', 3)	# 46-48
    sprite('ubl450_01', 3)	# 49-51
    Unknown1019(80)
    EnableCollision(1)
    Unknown2015(-1)
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_02', 3)	# 52-54
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    sprite('ubl450_03', 3)	# 55-57
    Unknown1019(80)
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_04', 3)	# 58-60
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    sprite('ubl450_05', 8)	# 61-68
    Unknown1019(80)
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_06', 8)	# 69-76
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    sprite('ubl450_07', 8)	# 77-84
    Unknown1019(80)
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_08', 8)	# 85-92
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    sprite('ubl450_09', 8)	# 93-100
    Unknown1019(80)
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_10', 8)	# 101-108
    Unknown1019(0)
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    GFX_0('ubl_AH_LampTrajectory01_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory01_Eff', 1)
    SFX_3('ublse_02')
    SFX_3('ublse_03')
    sprite('ubl450_11', 8)	# 109-116
    Unknown2005()
    Unknown26('ubl_AH_Lamp_Eff')
    Unknown26('ubl_Dash_Eff')
    Unknown26('ubl_431_Smoke_Eff')
    Unknown26('ubl_431_Dash_Eff')
    sprite('ubl450_12', 3)	# 117-119
    sprite('ubl450_13', 3)	# 120-122
    sprite('ubl450_14', 3)	# 123-125
    sprite('ubl450_15', 3)	# 126-128
    sprite('ubl450_16', 3)	# 129-131

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown23157(0)
        Unknown23084(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown2053(0)
        setInvincible(1)
        AttackLevel_(3)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(150)
        AirPushbackY(50000)
        Unknown11064(1)
        MinimumDamagePct(100)
        Unknown9016(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 30):
                Unknown36(22)
                teleportRelativeY(30000)
                Unknown1084(1)
                setGravity(0)
                Unknown3001(0)
                Unknown2005()
                Unknown35()
            if (SLOT_18 == 130):
                sendToLabel(3)
        GFX_0('IchigekiCamera', 100)
        Unknown4004('534345465f42425441475f527975686169596f6b6f000000000000000000000064000000')
        Unknown38(9, 1)
        GFX_0('UBLAstBG_Start', -1)
    sprite('ubl450_00', 3)	# 1-3
    Unknown1045(150000)
    EnableCollision(0)
    GFX_0('ubl_Dash_Eff', 100)
    GFX_0('ubl_450_Dash_Eff', 100)
    SFX_3('ublse_15')
    sprite('ubl450_01', 3)	# 4-6
    sprite('ubl450_02', 3)	# 7-9
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory000_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_03', 3)	# 10-12
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    Unknown26('ubl_AH_LampTrajectory000_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory000_Eff', 1)
    sprite('ubl450_04', 3)	# 13-15
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    Unknown26('ubl_AH_LampTrajectory000_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory000_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_05', 11)	# 16-26
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    Unknown26('ubl_AH_LampTrajectory000_Eff')
    GFX_0('ubl_AH_LampTrajectory00_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory000_Eff', 1)
    sprite('ubl450_06', 11)	# 27-37
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory00_Eff')
    Unknown26('ubl_AH_LampTrajectory000_Eff')
    GFX_0('ubl_AH_LampTrajectory01_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory010_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_07', 11)	# 38-48
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory01_Eff')
    Unknown26('ubl_AH_LampTrajectory010_Eff')
    GFX_0('ubl_AH_LampTrajectory02_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory020_Eff', 1)
    sprite('ubl450_08', 11)	# 49-59
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory02_Eff')
    Unknown26('ubl_AH_LampTrajectory020_Eff')
    GFX_0('ubl_AH_LampTrajectory02_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory020_Eff', 1)
    SFX_3('ublse_15')
    sprite('ubl450_09', 11)	# 60-70
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory02_Eff')
    Unknown26('ubl_AH_LampTrajectory020_Eff')
    GFX_0('ubl_AH_LampTrajectory02_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory020_Eff', 1)
    sprite('ubl450_10', 8)	# 71-78
    Unknown26('ubl_AH_Lamp_Eff')
    GFX_0('ubl_AH_Lamp_Eff', 0)
    GFX_0('ubl_AH_Lamp_Eff', 1)
    Unknown26('ubl_AH_LampTrajectory02_Eff')
    Unknown26('ubl_AH_LampTrajectory020_Eff')
    GFX_0('ubl_AH_LampTrajectory02_Eff', 0)
    GFX_0('ubl_AH_LampTrajectory020_Eff', 1)
    SFX_3('ublse_02')
    SFX_3('ublse_03')
    sprite('ubl450_11', 8)	# 79-86
    Unknown2005()
    Unknown26('ubl_AH_Lamp_Eff')
    Unknown26('ubl_Dash_Eff')
    Unknown26('ubl_450_Dash_Eff')
    Unknown26('ubl_431_Smoke_Eff')
    sprite('ubl450_12', 2)	# 87-88
    GFX_0('ubl_450_backward_Eff', 100)
    sprite('ubl450_13', 2)	# 89-90
    sprite('ubl450_14', 2)	# 91-92
    sprite('ubl450_15', 2)	# 93-94
    sprite('ubl450_16', 2)	# 95-96
    label(1)
    sprite('ubl450_17', 3)	# 97-99
    GFX_0('ubl_450_Vulcan_Eff', 0)
    GFX_0('ubl_450_Vulcan_Eff', 0)
    sprite('ubl450_19', 3)	# 100-102
    GFX_0('ubl_450_Vulcan_Eff', 0)
    sprite('ubl450_17', 3)	# 103-105
    GFX_0('ubl_450_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    sprite('ubl450_18', 3)	# 106-108
    GFX_0('ubl_450_Vulcan_Eff', 0)
    GFX_0('Grenade_Shot_Astral', 2)
    Unknown38(4, 1)
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    sprite('ubl450_19', 3)	# 109-111
    GFX_0('ubl_450_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    GFX_0('Grenade_Shot_Astral', 1)
    Unknown38(5, 1)
    SFX_3('ublse_08')
    SFX_0('016_explode_2')
    loopRest()
    label(2)
    sprite('ubl450_17', 3)	# 112-114
    GFX_0('ubl_450_Vulcan_Eff', 0)
    SFX_3('ublse_05')
    sprite('ubl450_18', 3)	# 115-117
    GFX_0('ubl_450_Vulcan_Eff', 0)
    sprite('ubl450_19', 3)	# 118-120
    GFX_0('ubl_450_Vulcan_Eff', 0)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ubl450_20', 3)	# 121-123
    SFX_3('ublse_02')
    sprite('ubl450_21', 3)	# 124-126
    sprite('ubl005_00', 3)	# 127-129
    Unknown36(9)
    Unknown3004(-12)
    Unknown35()
    sprite('ubl005_00', 7)	# 130-136
    Unknown26('ubl_450_backward_Eff')
    sprite('ubl005_01', 6)	# 137-142
    sprite('ubl005_02', 6)	# 143-148
    SFX_3('ublse_22')
    sprite('ubl005_03', 6)	# 149-154
    sprite('ubl005_04', 6)	# 155-160
    sprite('ubl005_05', 10)	# 161-170
    sprite('ubl005_06', 10)	# 171-180
    sprite('ubl005_07', 13)	# 181-193
    SFX_3('ublse_21')
    sprite('ubl005_08', 13)	# 194-206
    Unknown26('SCEF_BBTAG_RyuhaiYoko')
    sprite('keep', 1)	# 207-207
    enterState('AstralHeatFinish')

@State
def AstralHeatFinish():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown23157(0)
        Unknown23084(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown2053(0)
        setInvincible(1)
        AttackLevel_(4)
        Damage(1750)
        Hitstop(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(120)
        Unknown11057(500)
        AirPushbackX(2500)
        AirPushbackY(-50000)
        Unknown11064(1)
        MinimumDamagePct(100)
        Unknown9016(1)
        Unknown9310(10)
        Unknown1018()
        Unknown1023()
        Unknown1043()
        Unknown23024(3)
        SLOT_51 = 1
        DisableAttackRestOfMove()
        Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000b90b000000000000')

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 150):
                sendToLabel(3)
            if (SLOT_18 == 210):
                Unknown4004('534345465f42425441475f527975686169596f6b6f000000000000000000000064000000')
                sendToLabel(4)
            if (SLOT_18 == 215):
                Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000ba0b000000000000')
            if (SLOT_18 == 300):
                Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000b80b000000000000')
                Unknown36(22)
                Unknown2005()
                Unknown3001(255)
                teleportRelativeY(270000)
                setGravity(150)
                Unknown35()
                sendToLabel(10)
            if (SLOT_18 == 300):
                Unknown23029(4, 3004, 0)
            if (SLOT_18 == 307):
                Unknown23029(5, 3005, 0)
            if (SLOT_18 == 360):
                sendToLabel(20)
                Unknown26('UBLAstBG_Start')
            if (SLOT_18 == 480):
                sendToLabel(21)
                Unknown26('SCEF_BBTAG_RyuhaiYoko')
    sprite('keep', 3)	# 1-3
    StartMultihit()
    Unknown1019(75)
    YAccel(40)
    setGravity(0)
    Unknown38(11, 1)
    sprite('ubl000_00', 3)	# 4-6
    Unknown2006()
    sprite('ubl430_00', 3)	# 7-9
    sprite('ubl430_01', 3)	# 10-12
    sprite('ubl430_02', 3)	# 13-15
    sprite('ubl430_03', 3)	# 16-18
    SFX_3('ublse_03')
    SFX_3('ublse_03')
    sprite('ubl430_04', 6)	# 19-24
    sprite('ubl430_05', 6)	# 25-30
    sprite('ubl430_06', 6)	# 31-36
    sprite('ubl430_07', 6)	# 37-42
    GFX_0('ubl_UltimateBeam_Charge_Eff', 0)
    SFX_3('ublse_14')
    SFX_3('ublse_14')
    SFX_3('ublse_12')
    SFX_3('ublse_12')
    sprite('ubl430_08', 6)	# 43-48
    sprite('ubl430_09', 6)	# 49-54
    GFX_0('ubl_UltimateBeamAH_Lightbullet_', 0)
    label(3)
    sprite('ubl430_10', 3)	# 55-57
    SLOT_51 = (SLOT_51 + 1)
    SFX_3('ublse_13')
    sprite('ubl430_11', 3)	# 58-60
    sprite('ubl430_12', 3)	# 61-63
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('ubl430_13', 3)	# 64-66
    Unknown26('ubl_UltimateBeam_Charge_Eff')
    Unknown26('ubl_UltimateBeamAH_Lightbullet_')
    GFX_0('ubl_UltimateBeam_Eff', 0)
    GFX_0('ubl_UltimateBeam_Muzzle_Eff', 0)
    GFX_0('ubl_UltimateBeamAH_rootWave_Eff', 0)
    GFX_0('ubl450_Fade_Eff', 100)
    Unknown23029(1, 2002, 0)
    SFX_3('ublse_07')
    SFX_3('ublse_08')
    ScreenShake(9000, 25000)
    label(5)
    sprite('ubl430_14', 3)	# 67-69
    sprite('ubl430_15', 3)	# 70-72
    sprite('ubl430_16', 3)	# 73-75
    sprite('ubl430_13', 3)	# 76-78
    loopRest()
    gotoLabel(5)
    label(10)
    sprite('null', 999)	# 79-1077
    Unknown26('ubl_UltimateBeam_Eff')
    Unknown26('ubl_UltimateBeam_Muzzle_Eff')
    Unknown26('ubl_UltimateBeamAH_rootWave_Eff')
    Unknown21012('75626c3435305f466164655f456666000000000000000000000000000000000020000000')
    GFX_0('ubl_UltimateBeamAH_Eff', 100)
    label(20)
    sprite('null', 1000)	# 1078-2077
    GFX_0('IchigekiCameraFinishAtkCol', 100)
    label(21)
    sprite('null', 65)	# 2078-2142
    sprite('null', 15)	# 2143-2157
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000bb0b000000000000')
    Unknown23024(0)
    Unknown20009(1000)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown20000(1)
    Unknown20001(1)
    label(99)
    sprite('ubl430_17', 15)	# 2158-2172
    GFX_0('ubl_UltimateBeamAH_smoke_Eff', 100)
    sprite('ubl430_18', 6)	# 2173-2178
    SFX_3('ublse_14')
    sprite('ubl430_19', 6)	# 2179-2184
    sprite('ubl430_20', 6)	# 2185-2190
    GFX_0('ubl_UltimateBeamAH_smokepa_Eff', 100)
    SFX_3('ublse_04')
    sprite('ubl430_21', 6)	# 2191-2196
    Unknown18010()
    Unknown21011(180)
    sprite('ubl430_22', 6)	# 2197-2202
    SFX_3('ublse_03')
    sprite('ubl430_23', 6)	# 2203-2208
    sprite('ubl430_24', 6)	# 2209-2214
    sprite('ubl430_25', 6)	# 2215-2220
    sprite('ubl430_26', 6)	# 2221-2226
    sprite('ubl300_00', 7)	# 2227-2233
    sprite('ubl300_01', 7)	# 2234-2240
    sprite('ubl300_02', 7)	# 2241-2247
    loopRelated(17, 60)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(101)
    label(100)
    sprite('ubl300_03', 3)	# 2248-2250
    sprite('ubl300_04', 3)	# 2251-2253
    sprite('ubl300_05', 3)	# 2254-2256
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('ubl300_06', 7)	# 2257-2263
    sprite('ubl300_07', 7)	# 2264-2270
    sprite('ubl300_08', 7)	# 2271-2277
    label(999)
    sprite('ubl000_00', 1)	# 2278-2278
    sprite('ubl000_01', 1)	# 2279-2279
    sprite('ubl000_02', 1)	# 2280-2280
    sprite('ubl000_03', 1)	# 2281-2281
    sprite('ubl000_04', 1)	# 2282-2282
    sprite('ubl000_05', 1)	# 2283-2283
    sprite('ubl000_06', 1)	# 2284-2284
    sprite('ubl000_07', 1)	# 2285-2285
    loopRest()
    gotoLabel(999)

@State
def CmnActEntry():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(1)
    sprite('ubl000_00', 1)	# 2-2
    Unknown2019(1000)
    Unknown2037(10)
    label(2)
    sprite('ubl000_00', 1)	# 3-3
    sprite('ubl000_01', 1)	# 4-4
    sprite('ubl000_02', 1)	# 5-5
    sprite('ubl000_03', 1)	# 6-6
    sprite('ubl000_04', 1)	# 7-7
    sprite('ubl000_05', 1)	# 8-8
    sprite('ubl000_06', 1)	# 9-9
    sprite('ubl000_07', 1)	# 10-10
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(2)
    sprite('ubl000_00', 20)	# 11-30
    sprite('ubl000_00', 65)	# 31-95
    GFX_0('ubl_000_Eyes_Eff', 100)
    Unknown21011(80)
    label(3)
    sprite('ubl000_00', 1)	# 96-96
    sprite('ubl000_01', 1)	# 97-97
    sprite('ubl000_02', 1)	# 98-98
    sprite('ubl000_03', 1)	# 99-99
    sprite('ubl000_04', 1)	# 100-100
    sprite('ubl000_05', 1)	# 101-101
    sprite('ubl000_06', 1)	# 102-102
    sprite('ubl000_07', 1)	# 103-103
    gotoLabel(3)
    ExitState()
    label(10)
    sprite('ubl000_00', 1)	# 104-104
    Unknown2053(0)
    Unknown1000(-2500000)
    physicsXImpulse(34700)
    Unknown2019(1000)
    sprite('ubl431_00', 3)	# 105-107
    GFX_0('ubl_Dash_Eff', 100)
    GFX_0('ubl_431_Smoke_Eff', 100)
    SFX_3('ublse_01')
    SFX_3('ublse_20')
    sprite('ubl431_01', 3)	# 108-110
    Unknown2037(3)
    label(11)
    sprite('ubl403_02', 3)	# 111-113	 **attackbox here**
    GFX_0('ubl_431_Dash_Eff', 100)
    Unknown2038(-1)
    SFX_3('ublse_15')
    sprite('ubl403_03', 3)	# 114-116	 **attackbox here**
    sprite('ubl403_04', 3)	# 117-119	 **attackbox here**
    if SLOT_2:
        _gotolabel(11)
    sprite('ubl004_00', 2)	# 120-121
    Unknown1019(0)
    Unknown1045(10000)
    Unknown26('ubl_Dash_Eff')
    Unknown26('ubl_431_Smoke_Eff')
    Unknown26('ubl_431_Dash_Eff')
    sprite('ubl004_01', 2)	# 122-123
    sprite('ubl004_02', 8)	# 124-131
    GFX_0('ubl_Brake_Eff', 100)
    sprite('ubl004_03', 8)	# 132-139
    sprite('ubl004_04', 8)	# 140-147
    sprite('ubl004_05', 8)	# 148-155
    sprite('ubl004_06', 8)	# 156-163
    sprite('ubl004_07', 2)	# 164-165
    sprite('ubl004_07', 6)	# 166-171
    sprite('ubl004_08', 8)	# 172-179
    sprite('ubl000_00', 1)	# 180-180
    GFX_0('ubl_000_Eyes_Eff', 100)
    Unknown21011(60)
    label(12)
    sprite('ubl000_00', 1)	# 181-181
    sprite('ubl000_01', 1)	# 182-182
    sprite('ubl000_02', 1)	# 183-183
    sprite('ubl000_03', 1)	# 184-184
    sprite('ubl000_04', 1)	# 185-185
    sprite('ubl000_05', 1)	# 186-186
    sprite('ubl000_06', 1)	# 187-187
    sprite('ubl000_07', 1)	# 188-188
    gotoLabel(12)
    ExitState()
    label(100)
    label(991)
    sprite('ubl000_00', 1)	# 189-189
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ubl000_00', 1)	# 190-190
    sprite('ubl000_01', 1)	# 191-191
    sprite('ubl000_02', 1)	# 192-192
    sprite('ubl000_03', 1)	# 193-193
    sprite('ubl000_04', 1)	# 194-194
    sprite('ubl000_05', 1)	# 195-195
    sprite('ubl000_06', 1)	# 196-196
    sprite('ubl000_07', 1)	# 197-197
    loopRest()
    gotoLabel(992)

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
            pass
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(1)
    sprite('ubl000_00', 1)	# 4-4
    Unknown2037(10)
    label(2)
    sprite('ubl000_00', 1)	# 5-5
    sprite('ubl000_01', 1)	# 6-6
    sprite('ubl000_02', 1)	# 7-7
    sprite('ubl000_03', 1)	# 8-8
    sprite('ubl000_04', 1)	# 9-9
    sprite('ubl000_05', 1)	# 10-10
    sprite('ubl000_06', 1)	# 11-11
    sprite('ubl000_07', 1)	# 12-12
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(2)
    sprite('ubl000_00', 20)	# 13-32
    sprite('ubl000_00', 65)	# 33-97
    GFX_0('ubl_000_Eyes_Eff', 100)
    Unknown21011(80)
    label(3)
    sprite('ubl000_00', 1)	# 98-98
    sprite('ubl000_01', 1)	# 99-99
    sprite('ubl000_02', 1)	# 100-100
    sprite('ubl000_03', 1)	# 101-101
    sprite('ubl000_04', 1)	# 102-102
    sprite('ubl000_05', 1)	# 103-103
    sprite('ubl000_06', 1)	# 104-104
    sprite('ubl000_07', 1)	# 105-105
    gotoLabel(3)
    ExitState()
    label(10)
    sprite('ubl300_00', 7)	# 106-112
    Unknown2037(15)
    sprite('ubl300_01', 7)	# 113-119
    GFX_0('ublef_Idling_Eff', 0)
    GFX_0('ublef_smoke_Eff', 0)
    SFX_3('ublse_23')
    sprite('ubl300_02', 7)	# 120-126
    GFX_0('ublef_Idling_Eff', 0)
    label(11)
    sprite('ubl300_03', 1)	# 127-127
    Unknown2038(-1)
    sprite('ubl300_04', 1)	# 128-128
    sprite('ubl300_05', 1)	# 129-129
    loopRest()
    if SLOT_2:
        _gotolabel(11)
    sprite('ubl300_06', 7)	# 130-136
    sprite('ubl300_07', 7)	# 137-143
    sprite('ubl300_08', 7)	# 144-150
    Unknown21011(30)
    label(12)
    sprite('ubl000_00', 1)	# 151-151
    sprite('ubl000_01', 1)	# 152-152
    sprite('ubl000_02', 1)	# 153-153
    sprite('ubl000_03', 1)	# 154-154
    sprite('ubl000_04', 1)	# 155-155
    sprite('ubl000_05', 1)	# 156-156
    sprite('ubl000_06', 1)	# 157-157
    sprite('ubl000_07', 1)	# 158-158
    gotoLabel(12)
    ExitState()

@State
def CmnActLose():
    sprite('ubl070_00', 3)	# 1-3
    Unknown2037(10)
    label(0)
    sprite('ubl070_01', 4)	# 4-7
    Unknown2038(-1)
    sprite('ubl070_02', 4)	# 8-11
    if SLOT_2:
        _gotolabel(0)
    sprite('ubl070_02', 45)	# 12-56
    sprite('ubl070_03', 6)	# 57-62
    SFX_3('ublse_02')
    sprite('ubl070_04', 6)	# 63-68
    sprite('ubl070_05', 32767)	# 69-32835
    Unknown21011(30)