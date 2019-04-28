@Subroutine
def PreInit():
    Unknown12019('70626300000000000000000000000000')

@Subroutine
def MatchInit():
    AirBDashDuration(13)
    Unknown12037(-1800)
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
    Unknown14015(2000, 580000, -117000, 143000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(14000, 168000, -70000, 131000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14013('NmlAtk5A4th')
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    MoveMaxChainRepeat(3)
    Unknown15009()
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    MoveMaxChainRepeat(1)
    Unknown14015(124000, 852000, -223000, 238000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(4000)
    Unknown15013(4000)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14015(-10000, 323000, -209000, 417000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(20000, 430000, -219000, -66000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(20000, 430000, -219000, -66000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(10000, 377000, -218000, 131000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(18000, 619000, -128000, 153000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15008()
    Unknown14015(210000, 702000, -417000, 209000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('ShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3083)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3083)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('ShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3083)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('AirShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3083)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('AirShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3083)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('AirShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3083)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('LowAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3083)
    Unknown15009()
    Unknown15021(250)
    Unknown14015(18000, 790000, -221000, -11000, 1000, 50)
    Move_EndRegister()
    Move_Register('LowAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3083)
    Unknown15009()
    Unknown15021(250)
    Unknown14015(16000, 1044000, -231000, 51000, 500, 50)
    Move_EndRegister()
    Move_Register('LowAssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3083)
    Unknown15009()
    Unknown15021(250)
    Unknown14015(16000, 1044000, -231000, 51000, 500, 50)
    Move_EndRegister()
    Move_Register('InvincibleAttackAdd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15013(4000)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 266000, -123000, 755000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 266000, -123000, 755000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateLaser', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(279000, 1879000, -91000, 280000, 50, 50)
    Move_EndRegister()
    Move_Register('UltimateLaserOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(279000, 1879000, -91000, 280000, 50, 50)
    Move_EndRegister()
    Move_Register('UltimateBlade', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 649000, -113000, 92000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateBladeOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 649000, -113000, 92000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15000(0)
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtk4A4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'ShotB', 10000000)
    Unknown15024('NmlAtk5B2nd', 'ShotEx', 10000000)
    Unknown7010(0, 'pbc000')
    Unknown7010(1, 'pbc001')
    Unknown7010(2, 'pbc002')
    Unknown7010(3, 'pbc003')
    Unknown7010(4, 'pbc004')
    Unknown7010(5, 'pbc005')
    Unknown7010(6, 'pbc006')
    Unknown7010(7, 'pbc007')
    Unknown7010(8, 'pbc008')
    Unknown7010(9, 'pbc009')
    Unknown7010(10, 'pbc010')
    Unknown7010(15, 'pbc011')
    Unknown7010(16, 'pbc012')
    Unknown7010(17, 'pbc013')
    Unknown7010(18, 'pbc014')
    Unknown7010(19, 'pbc015')
    Unknown7010(20, 'pbc016')
    Unknown7010(21, 'pbc017')
    Unknown7010(22, 'pbc018')
    Unknown7010(23, 'pbc019')
    Unknown7010(24, 'pbc020')
    Unknown7010(25, 'pbc021')
    Unknown7010(28, 'pbc022')
    Unknown7010(29, 'pbc023')
    Unknown7010(30, 'pbc024')
    Unknown7010(31, 'pbc025')
    Unknown7010(32, 'pbc026')
    Unknown7010(33, 'pbc027')
    Unknown7010(34, 'pbc028')
    Unknown7010(35, 'pbc029')
    Unknown7010(36, 'pbc030')
    Unknown7010(37, 'pbc031')
    Unknown7010(39, 'pbc032')
    Unknown7010(42, 'pbc033')
    Unknown7010(43, 'pbc034')
    Unknown7010(44, 'pbc035')
    Unknown7010(45, 'pbc036')
    Unknown7010(46, 'pbc037')
    Unknown7010(47, 'pbc038')
    Unknown7010(48, 'pbc039')
    Unknown7010(49, 'pbc040')
    Unknown7010(50, 'pbc041')
    Unknown7010(52, 'pbc042')
    Unknown7010(53, 'pbc043')
    Unknown7010(54, 'pbc100_0')
    Unknown7010(55, 'pbc100_1')
    Unknown7010(56, 'pbc100_2')
    Unknown7010(63, 'pbc101_0')
    Unknown7010(64, 'pbc101_1')
    Unknown7010(65, 'pbc101_2')
    Unknown7010(57, 'pbc102_0')
    Unknown7010(58, 'pbc102_1')
    Unknown7010(59, 'pbc102_2')
    Unknown7010(66, 'pbc103_0')
    Unknown7010(67, 'pbc103_1')
    Unknown7010(68, 'pbc103_2')
    Unknown7010(60, 'pbc104_0')
    Unknown7010(61, 'pbc104_1')
    Unknown7010(62, 'pbc104_2')
    Unknown7010(69, 'pbc105_0')
    Unknown7010(70, 'pbc105_1')
    Unknown7010(71, 'pbc105_2')
    Unknown7010(72, 'pbc150')
    Unknown7010(73, 'pbc151')
    Unknown7010(74, 'pbc152')
    Unknown7010(85, 'pbc153')
    Unknown7010(87, 'pbc154')
    Unknown7010(88, 'pbc155')
    Unknown7010(96, 'pbc161_0')
    Unknown7010(97, 'pbc161_1')
    Unknown7010(92, 'pbc162_0')
    Unknown7010(93, 'pbc162_1')
    Unknown7010(98, 'pbc163_0')
    Unknown7010(99, 'pbc163_1')
    Unknown7010(100, 'pbc164_0')
    Unknown7010(101, 'pbc164_1')
    Unknown7010(105, 'pbc165_0')
    Unknown7010(106, 'pbc165_1')
    Unknown7010(102, 'pbc166_0')
    Unknown7010(103, 'pbc166_1')
    Unknown7010(90, 'pbc167_0')
    Unknown7010(91, 'pbc167_1')
    Unknown7010(107, 'pbc168_0')
    Unknown7010(108, 'pbc168_1')
    Unknown7010(110, 'pbc169_0')
    Unknown7010(111, 'pbc169_1')
    Unknown7010(94, 'pbc400_0')
    Unknown7010(95, 'pbc400_1')
    Unknown12018(0, 'bc060_00')
    Unknown12018(1, 'bc060_01')
    Unknown12018(2, 'bc060_02')
    Unknown12018(3, 'bc060_03')
    Unknown12018(4, 'bc060_04')
    Unknown12018(5, 'bc060_05')
    Unknown12018(6, 'bc060_06')
    Unknown12018(7, 'bc041_02')
    Unknown12018(8, 'bc040_02')
    Unknown12018(9, 'bc045_02')
    Unknown12018(10, 'bc060_00')
    Unknown12018(11, 'bc060_01')
    Unknown12018(12, 'bc060_03')
    Unknown12018(13, 'bc060_05')
    Unknown12018(14, 'bc060_07')
    Unknown12018(15, 'bc125_00')
    Unknown12018(16, 'bc050_00')
    Unknown12018(17, 'bc052_00')
    Unknown12018(18, 'bc054_00')
    Unknown12018(19, 'bc000_00')
    Unknown12018(20, 'bc000_00')
    Unknown12018(25, 'bc063_00')
    Unknown12018(26, 'bc063_01')
    Unknown12018(27, 'bc063_02')
    Unknown12018(28, 'bc063_05')
    Unknown12018(29, 'bc060_12')
    Unknown12018(24, 'bc072_03')
    Unknown30036('5042435f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174654c6173657200000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d6174654c617365724f440000000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465426c61646500000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465426c6164654f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def MidAssault_koutyoku():
    if (SLOT_23 >= 200000):
        SLOT_51 = 1
    if (SLOT_23 >= 500000):
        SLOT_52 = 1

    def upon_11():
        SLOT_51 = 0
        SLOT_52 = 0

    def upon_3():
        if SLOT_51:
            if SLOT_52:
                sendToLabelUpon(2, 3)
            else:
                sendToLabelUpon(2, 2)
        else:
            sendToLabelUpon(2, 1)

@State
def CmnActStand():
    label(0)
    sprite('bc000_00', 6)	# 1-6
    sprite('bc000_01', 6)	# 7-12
    sprite('bc000_02', 6)	# 13-18
    sprite('bc000_03', 6)	# 19-24
    sprite('bc000_04', 6)	# 25-30
    sprite('bc000_05', 6)	# 31-36
    sprite('bc000_06', 6)	# 37-42
    sprite('bc000_07', 6)	# 43-48
    sprite('bc000_08', 6)	# 49-54
    sprite('bc000_09', 6)	# 55-60
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('bc001_00', 7)	# 61-67
    SLOT_88 = 960
    sprite('bc001_01', 7)	# 68-74
    sprite('bc001_02', 7)	# 75-81
    sprite('bc001_03', 7)	# 82-88
    sprite('bc001_04', 7)	# 89-95
    sprite('bc001_05', 7)	# 96-102
    SFX_4('pbc000')
    sprite('bc001_06', 60)	# 103-162
    sprite('bc001_00', 7)	# 163-169
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('bc003_00', 4)	# 1-4
    sprite('bc003_01', 4)	# 5-8
    sprite('bc003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('bc010_00', 4)	# 1-4
    sprite('bc010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('bc010_02', 6)	# 1-6
    sprite('bc010_03', 6)	# 7-12
    sprite('bc010_04', 6)	# 13-18
    sprite('bc010_05', 6)	# 19-24
    sprite('bc010_06', 6)	# 25-30
    sprite('bc010_07', 6)	# 31-36
    sprite('bc010_08', 6)	# 37-42
    sprite('bc010_09', 6)	# 43-48
    sprite('bc010_10', 6)	# 49-54
    sprite('bc010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('bc013_00', 4)	# 1-4
    sprite('bc013_01', 4)	# 5-8
    sprite('bc013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('bc010_01', 4)	# 1-4
    sprite('bc010_00', 4)	# 5-8

@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        SLOT_4 = 0
    sprite('bc010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('bc020_00', 4)	# 1-4
    sprite('bc020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpper():
    label(0)
    sprite('bc020_00', 4)	# 1-4
    sprite('bc020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('bc020_02', 3)	# 1-3
    sprite('bc020_03', 3)	# 4-6
    sprite('bc020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('bc020_05', 3)	# 1-3
    sprite('bc020_06', 3)	# 4-6
    label(0)
    sprite('bc020_07', 4)	# 7-10
    sprite('bc020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('bc010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('bc120_01', 2)	# 1-2
    sprite('bc120_00', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('bc120_01', 2)	# 1-2
    sprite('bc120_02', 2)	# 3-4
    sprite('bc120_03', 2)	# 5-6

@State
def CmnActFWalk():
    sprite('bc030_00', 5)	# 1-5
    sprite('bc030_01', 5)	# 6-10
    label(0)
    sprite('bc030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bc030_03', 5)	# 16-20
    sprite('bc030_04', 5)	# 21-25
    sprite('bc030_05', 5)	# 26-30
    sprite('bc030_06', 5)	# 31-35
    sprite('bc030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bc030_08', 5)	# 41-45
    sprite('bc030_09', 5)	# 46-50
    sprite('bc030_10', 5)	# 51-55
    sprite('bc030_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)
    sprite('bc030_00', 3)	# 61-63

@State
def CmnActBWalk():
    sprite('bc031_00', 6)	# 1-6
    sprite('bc031_01', 6)	# 7-12
    label(0)
    sprite('bc031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bc031_03', 6)	# 19-24
    sprite('bc031_04', 6)	# 25-30
    sprite('bc031_05', 6)	# 31-36
    sprite('bc031_06', 6)	# 37-42
    sprite('bc031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('bc031_08', 6)	# 49-54
    sprite('bc031_09', 6)	# 55-60
    sprite('bc031_10', 6)	# 61-66
    sprite('bc031_11', 6)	# 67-72
    loopRest()
    gotoLabel(0)
    sprite('bc031_00', 3)	# 73-75

@State
def CmnActFDash():
    sprite('bc032_10', 3)	# 1-3
    sprite('bc032_00', 4)	# 4-7
    sprite('bc032_01', 4)	# 8-11
    sprite('bc032_02', 4)	# 12-15
    label(0)
    sprite('bc032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('bc032_04', 4)	# 20-23
    sprite('bc032_05', 4)	# 24-27
    sprite('bc032_06', 4)	# 28-31
    sprite('bc032_07', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('bc032_08', 4)	# 36-39
    sprite('bc032_01', 4)	# 40-43
    sprite('bc032_02', 4)	# 44-47
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('bc032_09', 6)	# 1-6
    sprite('bc032_10', 6)	# 7-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('bc033_00', 2)	# 1-2
    sprite('bc033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('bc033_02', 3)	# 6-8
    sprite('bc033_01', 3)	# 9-11
    sprite('bc033_02', 3)	# 12-14
    label(0)
    sprite('bc033_01', 3)	# 15-17
    sprite('bc033_02', 3)	# 18-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc033_03', 3)	# 21-23
    setInvincible(0)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('bc033_04', 3)	# 24-26

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirTurn():
    sprite('bc025_00', 1)	# 1-1
    sprite('bc025_01', 2)	# 2-3
    sprite('bc025_02', 1)	# 4-4

@State
def CmnActAirFDash():
    sprite('bc035_00', 3)	# 1-3
    label(0)
    sprite('bc035_01', 3)	# 4-6
    sprite('bc035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    sprite('bc035_00', 4)	# 10-13

@State
def CmnActAirBDash():
    sprite('bc033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('bc033_02', 3)	# 4-6
    sprite('bc033_01', 3)	# 7-9
    sprite('bc033_02', 3)	# 10-12
    sprite('bc033_01', 3)	# 13-15
    sprite('bc033_02', 3)	# 16-18
    sprite('bc033_01', 3)	# 19-21
    sprite('bc033_02', 3)	# 22-24
    sprite('bc020_05', 3)	# 25-27
    sprite('bc020_06', 3)	# 28-30
    label(0)
    sprite('bc020_07', 4)	# 31-34
    sprite('bc020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('bc050_00', 1)	# 1-1
    sprite('bc050_01', 1)	# 2-2
    sprite('bc050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('bc050_01', 1)	# 1-1
    sprite('bc050_02', 1)	# 2-2
    sprite('bc050_01', 2)	# 3-4
    sprite('bc050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('bc050_02', 1)	# 1-1
    sprite('bc050_03', 1)	# 2-2
    sprite('bc050_02', 2)	# 3-4
    sprite('bc050_01', 2)	# 5-6
    sprite('bc050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('bc050_03', 1)	# 1-1
    sprite('bc050_04', 1)	# 2-2
    sprite('bc050_03', 2)	# 3-4
    sprite('bc050_02', 2)	# 5-6
    sprite('bc050_01', 2)	# 7-8
    sprite('bc050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('bc050_04', 1)	# 1-1
    sprite('bc050_04', 1)	# 2-2
    sprite('bc050_04', 2)	# 3-4
    sprite('bc050_03', 2)	# 5-6
    sprite('bc050_02', 2)	# 7-8
    sprite('bc050_01', 2)	# 9-10
    sprite('bc050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('bc052_00', 1)	# 1-1
    sprite('bc052_01', 1)	# 2-2
    sprite('bc052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('bc052_01', 1)	# 1-1
    sprite('bc052_02', 1)	# 2-2
    sprite('bc052_01', 2)	# 3-4
    sprite('bc052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('bc052_02', 1)	# 1-1
    sprite('bc052_03', 1)	# 2-2
    sprite('bc052_02', 2)	# 3-4
    sprite('bc052_01', 2)	# 5-6
    sprite('bc052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('bc052_03', 1)	# 1-1
    sprite('bc052_04', 1)	# 2-2
    sprite('bc052_03', 2)	# 3-4
    sprite('bc052_02', 2)	# 5-6
    sprite('bc052_01', 2)	# 7-8
    sprite('bc052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('bc052_04', 1)	# 1-1
    sprite('bc052_04', 1)	# 2-2
    sprite('bc052_04', 2)	# 3-4
    sprite('bc052_03', 2)	# 5-6
    sprite('bc052_02', 2)	# 7-8
    sprite('bc052_01', 2)	# 9-10
    sprite('bc052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('bc054_00', 1)	# 1-1
    sprite('bc054_01', 1)	# 2-2
    sprite('bc054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('bc054_01', 1)	# 1-1
    sprite('bc054_02', 1)	# 2-2
    sprite('bc054_01', 2)	# 3-4
    sprite('bc054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('bc054_02', 1)	# 1-1
    sprite('bc054_03', 1)	# 2-2
    sprite('bc054_02', 2)	# 3-4
    sprite('bc054_01', 2)	# 5-6
    sprite('bc054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('bc054_03', 1)	# 1-1
    sprite('bc054_04', 1)	# 2-2
    sprite('bc054_03', 2)	# 3-4
    sprite('bc054_02', 2)	# 5-6
    sprite('bc054_01', 2)	# 7-8
    sprite('bc054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('bc054_04', 1)	# 1-1
    sprite('bc054_04', 1)	# 2-2
    sprite('bc054_04', 2)	# 3-4
    sprite('bc054_03', 2)	# 5-6
    sprite('bc054_02', 2)	# 7-8
    sprite('bc054_01', 2)	# 9-10
    sprite('bc054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('bc060_00', 4)	# 1-4
    label(0)
    sprite('bc060_01', 4)	# 5-8
    sprite('bc060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('bc060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('bc060_04', 8)	# 1-8
    label(1)
    sprite('bc060_05', 4)	# 9-12
    sprite('bc060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('bc063_05', 6)	# 1-6

@State
def CmnActBDownBound():
    sprite('bc060_08', 2)	# 1-2
    sprite('bc060_09', 2)	# 3-4
    sprite('bc060_10', 2)	# 5-6
    sprite('bc060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('bc060_12', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('bc064_00', 6)	# 1-6
    sprite('bc064_01', 6)	# 7-12
    sprite('bc064_02', 6)	# 13-18
    sprite('bc064_03', 6)	# 19-24

@State
def CmnActFDownUpper():
    sprite('bc063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('bc063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('bc063_03', 3)	# 1-3
    sprite('bc063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('bc063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('bc060_08', 2)	# 1-2
    sprite('bc060_09', 2)	# 3-4
    sprite('bc060_10', 2)	# 5-6
    sprite('bc060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('bc060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('bc064_00', 6)	# 1-6
    sprite('bc064_01', 6)	# 7-12
    sprite('bc064_02', 6)	# 13-18
    sprite('bc064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('bc060_00', 4)	# 1-4
    label(0)
    sprite('bc060_01', 4)	# 5-8
    sprite('bc060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('bc060_03', 4)	# 1-4
    sprite('bc060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('bc060_04', 8)	# 1-8
    label(0)
    sprite('bc060_05', 4)	# 9-12
    sprite('bc060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('bc060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('bc072_00', 3)	# 1-3
    sprite('bc072_01', 3)	# 4-6
    sprite('bc072_02', 3)	# 7-9
    label(0)
    sprite('bc072_01', 3)	# 10-12
    sprite('bc072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('bc074_00', 2)	# 1-2
    sprite('bc074_01', 2)	# 3-4
    sprite('bc074_02', 2)	# 5-6
    sprite('bc074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('bc072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('bc063_00', 3)	# 1-3
    label(0)
    sprite('bc063_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('bc082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('bc052_01', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('bc070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('bc070_01', 4)	# 1-4
    sprite('bc070_02', 4)	# 5-8
    sprite('bc070_03', 4)	# 9-12
    sprite('bc070_04', 4)	# 13-16
    sprite('bc070_05', 4)	# 17-20
    sprite('bc070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('bc040_03', 2)	# 1-2
    sprite('bc040_02', 2)	# 3-4
    sprite('bc040_01', 2)	# 5-6
    sprite('bc040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('bc020_02', 3)	# 1-3
    sprite('bc020_03', 3)	# 4-6
    sprite('bc020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('bc020_02', 3)	# 1-3
    sprite('bc020_03', 3)	# 4-6
    sprite('bc020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('bc020_02', 3)	# 1-3
    sprite('bc020_03', 3)	# 4-6
    sprite('bc020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('bc112_00', 3)	# 1-3
    sprite('bc112_01', 3)	# 4-6
    sprite('bc112_02', 3)	# 7-9
    sprite('bc112_03', 3)	# 10-12
    sprite('bc112_04', 3)	# 13-15
    sprite('bc112_05', 3)	# 16-18
    sprite('bc020_07', 4)	# 19-22
    sprite('bc020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandF():
    sprite('bc112_00', 3)	# 1-3
    sprite('bc112_01', 3)	# 4-6
    sprite('bc112_02', 3)	# 7-9
    sprite('bc112_03', 3)	# 10-12
    sprite('bc112_04', 3)	# 13-15
    sprite('bc112_05', 3)	# 16-18
    sprite('bc020_07', 4)	# 19-22
    sprite('bc020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('bc112_00', 3)	# 1-3
    sprite('bc112_01', 3)	# 4-6
    sprite('bc112_02', 3)	# 7-9
    sprite('bc112_03', 3)	# 10-12
    sprite('bc112_04', 3)	# 13-15
    sprite('bc112_05', 3)	# 16-18
    sprite('bc020_07', 4)	# 19-22
    sprite('bc020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('bc010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('bc040_00', 3)	# 1-3
    sprite('bc040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('bc040_02', 5)	# 1-5
    sprite('bc040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('bc040_01', 3)	# 1-3
    sprite('bc040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('bc040_04', 1)	# 1-1
    label(0)
    sprite('bc040_02', 5)	# 2-6
    sprite('bc040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('bc040_01', 3)	# 1-3
    sprite('bc040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('bc040_00', 3)	# 1-3
    sprite('bc040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('bc040_04', 1)	# 1-1
    label(0)
    sprite('bc040_02', 5)	# 2-6
    sprite('bc040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('bc040_01', 3)	# 1-3
    sprite('bc040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('bc040_04', 1)	# 1-1
    label(0)
    sprite('bc040_02', 5)	# 2-6
    sprite('bc040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('bc040_01', 3)	# 1-3
    sprite('bc040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('bc043_00', 3)	# 1-3
    sprite('bc043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('bc043_02', 5)	# 1-5
    sprite('bc043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('bc043_01', 3)	# 1-3
    sprite('bc043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('bc043_04', 1)	# 1-1
    label(0)
    sprite('bc043_02', 5)	# 2-6
    sprite('bc043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('bc043_01', 3)	# 1-3
    sprite('bc043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('bc045_00', 3)	# 1-3
    sprite('bc045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('bc045_02', 5)	# 1-5
    sprite('bc045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('bc045_01', 3)	# 1-3
    sprite('bc045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('bc045_04', 1)	# 1-1
    label(0)
    sprite('bc045_02', 5)	# 2-6
    sprite('bc045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('bc045_01', 3)	# 1-3
    sprite('bc045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('bc040_04', 2)	# 1-2
    sprite('bc040_04', 2)	# 3-4
    sprite('bc040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('bc040_02', 4)	# 6-9
    sprite('bc040_01', 4)	# 10-13
    sprite('bc040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('bc043_04', 2)	# 1-2
    sprite('bc043_04', 2)	# 3-4
    sprite('bc043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('bc043_02', 4)	# 6-9
    sprite('bc043_01', 4)	# 10-13
    sprite('bc043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('bc045_04', 2)	# 1-2
    sprite('bc045_04', 2)	# 3-4
    sprite('bc045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('bc045_02', 4)	# 6-9
    sprite('bc045_01', 4)	# 10-13
    sprite('bc045_00', 4)	# 14-17

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('bc201_00', 3)	# 1-3
    sprite('bc201_01', 3)	# 4-6
    sprite('bc201_02', 3)	# 7-9
    sprite('bc201_05', 14)	# 10-23	 **attackbox here**
    sprite('bc201_06', 3)	# 24-26
    sprite('bc201_07', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('bc045_02', 1)	# 1-1
    sprite('bc045_01', 3)	# 2-4
    sprite('bc045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('bc250_00', 3)	# 1-3
    sprite('bc250_01', 3)	# 4-6
    sprite('bc250_03', 3)	# 7-9	 **attackbox here**
    Unknown7009(0)
    sprite('bc250_03', 7)	# 10-16	 **attackbox here**
    Unknown23027()
    sprite('bc250_04', 3)	# 17-19
    sprite('bc250_05', 3)	# 20-22
    sprite('bc250_06', 3)	# 23-25
    Unknown2001()

@State
def CmnActLandSpin():
    sprite('bc071_00', 2)	# 1-2
    label(0)
    sprite('bc071_01', 2)	# 3-4
    sprite('bc071_02', 2)	# 5-6
    sprite('bc071_03', 2)	# 7-8
    sprite('bc071_04', 2)	# 9-10
    sprite('bc071_05', 2)	# 11-12
    sprite('bc071_06', 2)	# 13-14
    sprite('bc071_07', 2)	# 15-16
    sprite('bc071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('bc040_02', 3)	# 1-3
    sprite('bc040_01', 3)	# 4-6
    sprite('bc040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('bc071_00', 2)	# 1-2
    label(0)
    sprite('bc071_01', 2)	# 3-4
    sprite('bc071_02', 2)	# 5-6
    sprite('bc071_03', 2)	# 7-8
    sprite('bc071_04', 2)	# 9-10
    sprite('bc071_05', 2)	# 11-12
    sprite('bc071_06', 2)	# 13-14
    sprite('bc071_07', 2)	# 15-16
    sprite('bc071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('bc124_00', 2)	# 1-2
    label(0)
    sprite('bc124_01', 2)	# 3-4
    sprite('bc124_02', 2)	# 5-6
    sprite('bc124_03', 2)	# 7-8
    sprite('bc124_04', 2)	# 9-10
    sprite('bc124_05', 2)	# 11-12
    sprite('bc124_06', 2)	# 13-14
    sprite('bc124_07', 2)	# 15-16
    sprite('bc124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('bc077_02', 4)	# 1-4
    label(0)
    sprite('bc077_03', 3)	# 5-7
    sprite('bc077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('bc077_05', 5)	# 1-5
    sprite('bc077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('bc077_02', 4)	# 1-4
    label(0)
    sprite('bc077_03', 3)	# 5-7
    sprite('bc077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('bc077_05', 5)	# 1-5
    sprite('bc077_06', 4)	# 6-9

@State
def CmnActBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    label(0)
    sprite('bc121_00', 2)	# 1-2
    sprite('bc121_01', 2)	# 3-4
    sprite('bc121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('bc121_03', 3)	# 1-3
    label(1)
    sprite('bc121_04', 2)	# 4-5
    sprite('bc121_05', 2)	# 6-7
    sprite('bc121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActBurstEnd():
    sprite('bc121_07', 3)	# 1-3
    sprite('bc121_08', 3)	# 4-6
    sprite('bc020_04', 3)	# 7-9
    sprite('bc020_05', 3)	# 10-12
    sprite('bc020_06', 3)	# 13-15
    sprite('bc020_07', 4)	# 16-19
    sprite('bc020_08', 4)	# 20-23
    loopRest()

@State
def CmnActAirBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    sprite('bc331_11', 2)	# 1-2
    sprite('bc331_12', 2)	# 3-4
    label(0)
    sprite('bc331_02', 3)	# 5-7
    sprite('bc331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('bc331_04', 2)	# 1-2
    sprite('bc331_05', 2)	# 3-4
    label(0)
    sprite('bc331_06', 3)	# 5-7
    sprite('bc331_07', 3)	# 8-10
    sprite('bc331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('bc121_07', 2)	# 1-2
    sprite('bc121_08', 2)	# 3-4
    sprite('bc020_05', 3)	# 5-7
    sprite('bc020_06', 3)	# 8-10
    label(0)
    sprite('bc020_07', 4)	# 11-14
    sprite('bc020_08', 4)	# 15-18
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('bc121_00', 2)	# 1-2
    sprite('bc121_01', 2)	# 3-4
    sprite('bc121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('bc121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('bc121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('bc121_04', 2)	# 4-5
    sprite('bc121_05', 2)	# 6-7
    sprite('bc121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActOverDriveEnd():
    sprite('bc121_07', 6)	# 1-6
    sprite('bc010_00', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('bc121_00', 2)	# 1-2
    sprite('bc121_01', 2)	# 3-4
    sprite('bc121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('bc121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('bc121_03', 3)	# 1-3
    label(1)
    sprite('bc121_04', 2)	# 4-5
    sprite('bc121_05', 2)	# 6-7
    sprite('bc121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirOverDriveEnd():
    sprite('bc121_07', 2)	# 1-2
    sprite('bc121_08', 2)	# 3-4
    sprite('bc020_04', 3)	# 5-7
    sprite('bc020_05', 3)	# 8-10
    sprite('bc020_06', 2)	# 11-12
    label(0)
    sprite('bc020_07', 4)	# 13-16
    sprite('bc020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('bc121_00', 2)	# 1-2
    sprite('bc121_01', 2)	# 3-4
    sprite('bc121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PBC_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('bc121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('bc121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('bc121_04', 2)	# 4-5
    sprite('bc121_05', 2)	# 6-7
    sprite('bc121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossRushEnd():
    sprite('bc121_07', 2)	# 1-2
    sprite('bc121_08', 2)	# 3-4
    sprite('bc020_04', 2)	# 5-6
    sprite('bc020_05', 2)	# 7-8
    sprite('bc020_06', 2)	# 9-10
    sprite('bc020_07', 2)	# 11-12

@State
def CmnActAirCrossRushBegin():
    sprite('bc121_00', 2)	# 1-2
    sprite('bc121_01', 2)	# 3-4
    sprite('bc121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PBC_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('bc121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('bc121_03', 3)	# 1-3
    label(1)
    sprite('bc121_04', 2)	# 4-5
    sprite('bc121_05', 2)	# 6-7
    sprite('bc121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossRushEnd():
    sprite('bc121_07', 2)	# 1-2
    sprite('bc121_08', 2)	# 3-4
    sprite('bc020_04', 3)	# 5-7
    sprite('bc020_05', 3)	# 8-10
    sprite('bc020_06', 2)	# 11-12
    label(0)
    sprite('bc020_07', 4)	# 13-16
    sprite('bc020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
        Unknown36(28)
        Unknown23148('PBC_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('bc121_00', 2)	# 1-2
    sprite('bc121_01', 2)	# 3-4
    sprite('bc121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('bc121_03', 3)	# 1-3
    label(1)
    sprite('bc121_04', 2)	# 4-5
    sprite('bc121_05', 2)	# 6-7
    sprite('bc121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossChangeEnd():
    sprite('bc121_07', 3)	# 1-3
    sprite('bc121_08', 3)	# 4-6
    sprite('bc020_04', 3)	# 7-9
    sprite('bc020_05', 3)	# 10-12
    sprite('bc020_06', 3)	# 13-15
    sprite('bc020_07', 4)	# 16-19
    sprite('bc020_08', 4)	# 20-23
    loopRest()

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
        Unknown36(28)
        Unknown23148('PBC_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('bc121_00', 2)	# 1-2
    sprite('bc121_01', 2)	# 3-4
    sprite('bc121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('bc121_03', 3)	# 1-3
    label(1)
    sprite('bc121_04', 2)	# 4-5
    sprite('bc121_05', 2)	# 6-7
    sprite('bc121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossChangeEnd():
    sprite('bc121_07', 3)	# 1-3
    sprite('bc121_08', 3)	# 4-6
    sprite('bc020_04', 3)	# 7-9
    sprite('bc020_05', 3)	# 10-12
    sprite('bc020_06', 3)	# 13-15
    label(0)
    sprite('bc020_07', 4)	# 16-19
    sprite('bc020_08', 4)	# 20-23
    loopRest()
    gotoLabel(2)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('bc203_00', 2)	# 1-2
    sprite('bc203_01', 2)	# 3-4
    sprite('bc203_02', 1)	# 5-5
    sprite('bc203_03', 1)	# 6-6
    sprite('bc203_04', 2)	# 7-8
    GFX_0('Zanzoh_5B', 100)
    SFX_3('slash_rapier_middle')
    sprite('bc203_06', 3)	# 9-11	 **attackbox here**
    Unknown23054('62633230335f303500000000000000000000000000000000000000000000000003000000')
    Unknown7009(1)
    sprite('bc203_06', 6)	# 12-17	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('bc203_07', 5)	# 18-22
    sprite('bc203_08', 5)	# 23-27
    sprite('bc203_09', 5)	# 28-32
    sprite('bc203_10', 5)	# 33-37

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('bc204_00', 4)	# 1-4
    sprite('bc204_01', 4)	# 5-8
    Unknown7007('7062633132305f300000000000000000640000007062633132305f310000000000000000640000007062633132305f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23029(11, 220, 0)
    sprite('bc204_02', 4)	# 9-12
    GFX_1('persona_enter_ply2', 0)
    sprite('bc204_03', 3)	# 13-15
    sprite('bc204_03', 1)	# 16-16
    Recovery()
    Unknown2063()
    sprite('bc204_04', 4)	# 17-20
    sprite('bc204_05', 4)	# 21-24
    sprite('bc204_03', 4)	# 25-28
    sprite('bc204_04', 4)	# 29-32
    sprite('bc204_05', 4)	# 33-36
    sprite('bc204_03', 4)	# 37-40
    sprite('bc204_04', 4)	# 41-44
    sprite('bc204_05', 3)	# 45-47
    sprite('bc204_00', 3)	# 48-50

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('bc403_00', 3)	# 1-3
    sprite('bc403_01', 1)	# 4-4
    sprite('bc403_01', 7)	# 5-11
    Unknown23029(11, 230, 0)
    sprite('bc403_02', 4)	# 12-15
    GFX_1('persona_enter_ply', 0)
    Unknown7007('7062633132335f300000000000000000640000007062633132335f310000000000000000640000007062633132315f300000000000000000640000007062633132315f31000000000000000064000000')
    sprite('bc403_03', 1)	# 16-16
    sprite('bc403_03', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('bc403_04', 4)	# 20-23
    sprite('bc403_05', 4)	# 24-27
    sprite('bc403_03', 4)	# 28-31
    sprite('bc403_04', 4)	# 32-35
    sprite('bc403_05', 5)	# 36-40
    sprite('bc403_03', 4)	# 41-44
    sprite('bc403_04', 4)	# 45-48
    sprite('bc403_00', 4)	# 49-52

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('bc205_00', 4)	# 1-4
    sprite('bc205_01', 4)	# 5-8
    Unknown23029(11, 210, 0)
    tag_voice(1, 'pbc206_0', 'pbc206_1', 'pbc206_2', '')
    sprite('bc205_02', 4)	# 9-12
    sprite('bc205_03', 4)	# 13-16
    GFX_1('persona_enter_ply', 0)
    sprite('bc205_04', 4)	# 17-20
    sprite('bc205_05', 4)	# 21-24
    sprite('bc205_06', 4)	# 25-28
    sprite('bc205_04', 4)	# 29-32
    Recovery()
    Unknown2063()
    sprite('bc205_05', 4)	# 33-36
    sprite('bc205_06', 4)	# 37-40
    sprite('bc205_04', 4)	# 41-44
    sprite('bc205_05', 4)	# 45-48
    sprite('bc205_06', 4)	# 49-52
    sprite('bc205_00', 4)	# 53-56

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')

        def upon_43():
            if (SLOT_48 == 12):
                HitOrBlockCancel('NmlAtk5B2nd')
                HitOrBlockCancel('NmlAtk2B')
                HitOrBlockCancel('NmlAtk2C')
                HitOrBlockCancel('NmlAtk5A')
                HitOrBlockCancel('CmnActCrushAttack')
                HitJumpCancel(1)
        if Unknown23145('NmlAtk5A3rd'):
            SLOT_51 = 1
    sprite('bc205_00', 4)	# 1-4
    sprite('bc205_01', 4)	# 5-8
    if (not SLOT_51):
        Unknown7007('7062633132315f300000000000000000640000007062633132315f310000000000000000640000007062633132315f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown7007('7062633330355f300000000000000000640000007062633230385f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23029(11, 240, 0)
    sprite('bc205_02', 4)	# 9-12
    sprite('bc205_03', 4)	# 13-16
    GFX_1('persona_enter_ply', 0)
    sprite('bc205_04', 4)	# 17-20
    sprite('bc205_05', 4)	# 21-24
    sprite('bc205_06', 4)	# 25-28
    sprite('bc205_04', 4)	# 29-32
    sprite('bc205_05', 4)	# 33-36
    sprite('bc205_06', 4)	# 37-40
    sprite('bc205_04', 4)	# 41-44
    sprite('bc205_05', 1)	# 45-45
    sprite('bc205_05', 3)	# 46-48
    Recovery()
    Unknown2063()
    sprite('bc205_06', 4)	# 49-52
    sprite('bc205_04', 4)	# 53-56
    sprite('bc205_05', 4)	# 57-60
    sprite('bc205_06', 4)	# 61-64
    sprite('bc205_00', 4)	# 65-68

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('bc403_00', 3)	# 1-3
    Unknown23029(11, 250, 0)
    sprite('bc403_01', 8)	# 4-11
    sprite('bc403_02', 4)	# 12-15
    GFX_1('persona_enter_ply', 0)
    sprite('bc403_03', 4)	# 16-19
    Recovery()
    Unknown2063()
    sprite('bc403_04', 4)	# 20-23
    sprite('bc403_05', 4)	# 24-27
    sprite('bc403_03', 4)	# 28-31
    sprite('bc403_04', 4)	# 32-35
    sprite('bc403_05', 5)	# 36-40
    sprite('bc403_03', 5)	# 41-45
    sprite('bc403_04', 5)	# 46-50
    sprite('bc403_00', 5)	# 51-55

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('bc200_00', 1)	# 1-1
    sprite('bc200_01', 2)	# 2-3
    sprite('bc200_02', 2)	# 4-5
    sprite('bc200_04', 3)	# 6-8	 **attackbox here**
    Unknown23054('62633230305f303300000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_m_fast')
    Unknown7009(0)
    sprite('bc200_04', 3)	# 9-11	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('bc200_05', 5)	# 12-16
    sprite('bc200_06', 6)	# 17-22

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('bc201_00', 2)	# 1-2
    sprite('bc201_01', 2)	# 3-4
    sprite('bc201_02', 2)	# 5-6
    SFX_3('hit_m_middle')
    Unknown7009(1)
    sprite('bc201_04', 4)	# 7-10	 **attackbox here**
    Unknown23054('62633230315f303300000000000000000000000000000000000000000000000002000000')
    sprite('bc201_04', 6)	# 11-16	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('bc201_05', 4)	# 17-20	 **attackbox here**
    sprite('bc201_06', 4)	# 21-24
    sprite('bc201_07', 4)	# 25-28

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(-40000)
        Unknown11001(0, -3, 2)
        Unknown9154(22)
        Unknown9310(1)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk4A4th')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('bc202_00', 2)	# 1-2
    sprite('bc202_01', 2)	# 3-4
    sprite('bc202_02', 2)	# 5-6
    sprite('bc202_03', 2)	# 7-8
    GFX_0('Zanzoh_5A3rd', 100)
    sprite('bc202_05', 3)	# 9-11	 **attackbox here**
    Unknown23054('62633230325f303400000000000000000000000000000000000000000000000003000000')
    SFX_3('slash_sword_middle')
    Unknown7009(2)
    sprite('bc202_06', 3)	# 12-14
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('bc202_05', 3)	# 15-17	 **attackbox here**
    sprite('bc202_06', 4)	# 18-21
    sprite('bc202_05', 4)	# 22-25	 **attackbox here**
    sprite('bc202_07', 4)	# 26-29
    sprite('bc202_08', 4)	# 30-33

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('bc230_00', 2)	# 1-2
    sprite('bc230_01', 1)	# 3-3
    sprite('bc230_01', 1)	# 4-4
    Unknown1051(80)
    sprite('bc230_02', 2)	# 5-6
    SFX_3('hit_m_fast')
    Unknown7009(0)
    sprite('bc230_03', 3)	# 7-9	 **attackbox here**
    sprite('bc230_04', 5)	# 10-14
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('bc230_01', 4)	# 15-18
    sprite('bc230_00', 3)	# 19-21

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1100)
        AttackP1(90)
        Unknown11092(1)
        AirPushbackX(6000)
        AirPushbackY(27000)
        Unknown11092(1)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Hitstop(7)
        AirUntechableTime(22)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        Unknown28(8, '_NEUTRAL')
    sprite('bc231_00', 2)	# 1-2
    sprite('bc231_01', 2)	# 3-4
    sprite('bc231_02', 3)	# 5-7
    GFX_0('Zanzoh_2B', 100)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    SFX_3('slash_rapier_middle')
    Unknown7007('7062633130365f300000000000000000640000007062633130365f310000000000000000640000007062633130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('bc231_03', 2)	# 8-9	 **attackbox here**
    Unknown18009(0)
    sprite('bc231_05', 3)	# 10-12	 **attackbox here**
    Unknown23054('62633233315f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    setInvincible(0)
    sprite('bc231_50', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('bc231_51', 3)	# 16-18
    sprite('bc231_05', 3)	# 19-21	 **attackbox here**
    Unknown23027()
    sprite('bc231_50', 3)	# 22-24
    sprite('bc231_51', 3)	# 25-27
    sprite('bc231_05', 3)	# 28-30	 **attackbox here**
    Unknown23027()
    sprite('bc231_06', 5)	# 31-35
    sprite('bc231_07', 4)	# 36-39
    sprite('bc231_08', 4)	# 40-43

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
    sprite('bc211_00', 2)	# 1-2
    sprite('bc211_01', 1)	# 3-3
    sprite('bc211_01', 1)	# 4-4
    sprite('bc211_02', 2)	# 5-6
    sprite('bc211_03', 2)	# 7-8
    sprite('bc211_04', 2)	# 9-10
    SFX_3('slash_rapier_middle')
    sprite('bc211_05', 2)	# 11-12
    GFX_0('Zanzoh_2AB', 100)
    SFX_3('slash_sword_fast')
    Unknown7007('7062633130375f300000000000000000640000007062633130375f310000000000000000640000007062633130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('bc211_07', 3)	# 13-15	 **attackbox here**
    Unknown23054('62633231315f303600000000000000000000000000000000000000000000000003000000')
    sprite('bc211_07', 3)	# 16-18	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('bc211_08', 3)	# 19-21
    sprite('bc211_09', 3)	# 22-24
    sprite('bc211_10', 3)	# 25-27
    sprite('bc211_11', 4)	# 28-31
    sprite('bc211_12', 4)	# 32-35

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('bc210_00', 2)	# 1-2
    sprite('bc210_01', 2)	# 3-4
    sprite('bc210_02', 2)	# 5-6
    sprite('bc210_03', 3)	# 7-9
    sprite('bc210_04', 3)	# 10-12
    sprite('bc210_05', 3)	# 13-15
    sprite('bc210_06', 3)	# 16-18
    sprite('bc210_07', 3)	# 19-21
    SFX_3('slash_blade_fast')
    tag_voice(1, 'pbc156_0', 'pbc156_1', '', '')
    sprite('bc210_09', 3)	# 22-24	 **attackbox here**
    Unknown23054('62633231305f303800000000000000000000000000000000000000000000000005000000')
    GFX_0('Zanzoh_5AB', 100)
    sprite('bc210_09', 4)	# 25-28	 **attackbox here**
    Unknown23027()
    sprite('bc210_10', 4)	# 29-32
    sprite('bc210_11', 4)	# 33-36
    sprite('bc210_12', 4)	# 37-40
    sprite('bc210_13', 4)	# 41-44
    sprite('bc210_14', 4)	# 45-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        Unknown9016(1)
        setGravity(3000)
    sprite('bc210_10', 5)	# 1-5
    sprite('bc210_11', 5)	# 6-10
    sprite('bc210_12', 5)	# 11-15
    sprite('bc210_13', 3)	# 16-18
    sprite('bc210_14', 3)	# 19-21
    sprite('bc203_00', 2)	# 22-23
    sprite('bc203_01', 2)	# 24-25
    sprite('bc203_02', 1)	# 26-26
    sprite('bc203_03', 1)	# 27-27
    sprite('bc203_04', 2)	# 28-29
    GFX_0('Zanzoh_5B', 100)
    SFX_3('slash_rapier_middle')
    tag_voice(1, 'pbc157_0', 'pbc157_1', '', '')
    sprite('bc203_06', 3)	# 30-32	 **attackbox here**
    Unknown23054('62633230335f303500000000000000000000000000000000000000000000000003000000')
    sprite('bc203_06', 6)	# 33-38	 **attackbox here**
    sprite('bc203_07', 5)	# 39-43
    sprite('bc203_08', 5)	# 44-48
    sprite('bc203_09', 5)	# 49-53
    sprite('bc203_10', 5)	# 54-58
    sprite('bc000_00', 6)	# 59-64
    sprite('bc000_01', 6)	# 65-70
    sprite('bc000_02', 6)	# 71-76
    sprite('bc000_03', 6)	# 77-82
    sprite('bc000_04', 6)	# 83-88
    sprite('bc000_05', 6)	# 89-94
    sprite('bc000_06', 6)	# 95-100
    sprite('bc000_07', 6)	# 101-106
    sprite('bc000_08', 6)	# 107-112
    sprite('bc000_09', 6)	# 113-118
    label(10)
    sprite('bc000_00', 6)	# 119-124
    sprite('bc000_01', 6)	# 125-130
    sprite('bc000_02', 6)	# 131-136
    sprite('bc000_03', 6)	# 137-142
    sprite('bc000_04', 6)	# 143-148
    sprite('bc000_05', 6)	# 149-154
    sprite('bc000_06', 6)	# 155-160
    sprite('bc000_07', 6)	# 161-166
    sprite('bc000_08', 6)	# 167-172
    sprite('bc000_09', 6)	# 173-178
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 179-179

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown9016(1)
    sprite('bc208_00', 3)	# 1-3
    sprite('bc208_01', 3)	# 4-6

    def upon_3():
        if (SLOT_29 >= 300000):
            clearUponHandler(3)
            physicsXImpulse(6000)
    sprite('bc208_02', 3)	# 7-9	 **attackbox here**
    clearUponHandler(3)
    StartMultihit()
    sprite('bc208_03', 3)	# 10-12
    StartMultihit()
    SFX_3('slash_sword_middle')
    sprite('bc208_04', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    physicsYImpulse(12000)
    setGravity(2000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(10)
    sprite('bc208_06', 4)	# 15-18	 **attackbox here**
    YAccel(225)
    SFX_3('slash_sword_middle')
    sprite('bc208_07', 5)	# 19-23	 **attackbox here**
    Unknown1019(50)
    YAccel(65)
    GFX_0('Zanzoh_5A3rd_new', 100)
    sprite('bc208_09', 5)	# 24-28
    Unknown1019(50)
    sprite('bc208_09', 10)	# 29-38
    Unknown1019(50)
    label(10)
    sprite('bc010_00', 3)	# 39-41
    Unknown1084(1)
    sprite('bc000_00', 5)	# 42-46
    loopRest()
    sprite('bc000_00', 6)	# 47-52
    sprite('bc000_01', 6)	# 53-58
    sprite('bc000_02', 6)	# 59-64
    sprite('bc000_03', 6)	# 65-70
    sprite('bc000_04', 6)	# 71-76
    sprite('bc000_05', 6)	# 77-82
    sprite('bc000_06', 6)	# 83-88
    sprite('bc000_07', 6)	# 89-94
    sprite('bc000_08', 6)	# 95-100
    sprite('bc000_09', 6)	# 101-106
    label(0)
    sprite('bc000_00', 6)	# 107-112
    sprite('bc000_01', 6)	# 113-118
    sprite('bc000_02', 6)	# 119-124
    sprite('bc000_03', 6)	# 125-130
    sprite('bc000_04', 6)	# 131-136
    sprite('bc000_05', 6)	# 137-142
    sprite('bc000_06', 6)	# 143-148
    sprite('bc000_07', 6)	# 149-154
    sprite('bc000_08', 6)	# 155-160
    sprite('bc000_09', 6)	# 161-166
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 167-167

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('bc430_00', 4)	# 1-4
    sprite('bc430_01', 3)	# 5-7
    sprite('bc430_05', 3)	# 8-10
    Unknown2004(1, 0)
    GFX_0('jumonjiBcSlash', 100)
    sprite('bc430_06', 3)	# 11-13
    teleportRelativeX(-30000)
    sprite('bc430_07', 3)	# 14-16
    SFX_3('cut_l')
    teleportRelativeX(-30000)
    sprite('bc430_08', 3)	# 17-19
    tag_voice(0, 'pbc158_0', 'pbc158_1', '', '')
    teleportRelativeX(-30000)
    sprite('bc430_10', 3)	# 20-22	 **attackbox here**
    Unknown23054('62633433305f303900000000000000000000000000000000000000000000000003000000')
    SFX_3('bc001')
    sprite('bc430_10', 6)	# 23-28	 **attackbox here**
    sprite('bc430_11', 4)	# 29-32
    sprite('bc430_13', 4)	# 33-36
    sprite('bc430_14', 4)	# 37-40
    sprite('bc430_15', 4)	# 41-44
    sprite('bc430_16', 4)	# 45-48
    teleportRelativeX(30000)
    sprite('bc430_17', 4)	# 49-52
    teleportRelativeX(30000)
    sprite('bc430_18', 4)	# 53-56
    teleportRelativeX(30000)
    sprite('bc430_19', 4)	# 57-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 27)	# 1-27
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 28-28
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('bc401_09', 2)	# 29-30	 **attackbox here**
    StartMultihit()
    SFX_3('airdash_l')
    SFX_3('slash_pole_middle')
    physicsXImpulse(7500)
    physicsYImpulse(-6500)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('bc401_10', 2)	# 31-32	 **attackbox here**
    StartMultihit()
    physicsXImpulse(50000)
    physicsYImpulse(-39000)
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    Unknown4048(-45000)
    Unknown4045('626365665f6d696461737361756c745f6164645f30330000000000000000000000000000')
    sprite('bc401_11', 3)	# 33-35	 **attackbox here**
    StartMultihit()
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    sprite('bc401_10', 3)	# 36-38	 **attackbox here**
    StartMultihit()
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    sprite('bc401_11', 3)	# 39-41	 **attackbox here**
    StartMultihit()
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    sprite('bc401_11', 3)	# 42-44	 **attackbox here**
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    sprite('bc401_11', 3)	# 45-47	 **attackbox here**
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    label(1)
    sprite('bc401_12', 3)	# 48-50
    Unknown8000(100, 1, 1)
    setGravity(0)
    physicsYImpulse(0)
    Unknown1019(0)
    Unknown13(4)
    Unknown23087(0)
    sprite('bc401_13', 3)	# 51-53
    sprite('bc401_13', 3)	# 54-56
    sprite('bc401_14', 4)	# 57-60
    sprite('bc401_15', 4)	# 61-64
    sprite('bc000_00', 6)	# 65-70
    sprite('bc000_01', 6)	# 71-76
    sprite('bc000_02', 6)	# 77-82
    sprite('bc000_03', 6)	# 83-88
    sprite('bc000_04', 6)	# 89-94
    sprite('bc000_05', 6)	# 95-100
    sprite('bc000_06', 6)	# 101-106
    sprite('bc000_07', 6)	# 107-112
    sprite('bc000_08', 6)	# 113-118
    sprite('bc000_09', 6)	# 119-124

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('bc403_00', 2)	# 1-2
    sprite('bc403_00', 3)	# 3-5
    sprite('bc403_01', 8)	# 6-13
    Unknown23029(11, 700, 0)
    Unknown4020(11)
    sprite('bc403_02', 4)	# 14-17
    GFX_1('persona_enter_ply', 0)
    sprite('bc403_03', 4)	# 18-21
    sprite('bc403_04', 4)	# 22-25
    sprite('bc403_05', 4)	# 26-29
    sprite('bc403_03', 4)	# 30-33
    sprite('bc403_04', 4)	# 34-37
    sprite('bc403_05', 5)	# 38-42
    sprite('bc403_03', 5)	# 43-47
    sprite('bc403_04', 5)	# 48-52
    sprite('bc403_00', 5)	# 53-57
    loopRest()
    sprite('bc000_00', 6)	# 58-63
    sprite('bc000_01', 6)	# 64-69
    sprite('bc000_02', 6)	# 70-75
    sprite('bc000_03', 6)	# 76-81
    sprite('bc000_04', 6)	# 82-87
    sprite('bc000_05', 6)	# 88-93
    sprite('bc000_06', 6)	# 94-99
    sprite('bc000_07', 6)	# 100-105
    sprite('bc000_08', 6)	# 106-111
    sprite('bc000_09', 6)	# 112-117

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('bc430_00', 4)	# 1-4
    sprite('bc430_01', 3)	# 5-7
    sprite('bc430_05', 3)	# 8-10
    Unknown2004(1, 0)
    GFX_0('jumonjiBcSlash', 100)
    sprite('bc430_06', 3)	# 11-13
    teleportRelativeX(-30000)
    sprite('bc430_07', 3)	# 14-16
    SFX_3('cut_l')
    teleportRelativeX(-30000)
    sprite('bc430_08', 3)	# 17-19
    teleportRelativeX(-30000)
    sprite('bc430_10', 3)	# 20-22	 **attackbox here**
    Unknown23054('62633433305f303900000000000000000000000000000000000000000000000003000000')
    SFX_3('bc001')
    sprite('bc430_10', 6)	# 23-28	 **attackbox here**
    sprite('bc430_11', 4)	# 29-32
    sprite('bc430_13', 4)	# 33-36
    sprite('bc430_14', 4)	# 37-40
    sprite('bc430_15', 4)	# 41-44
    sprite('bc430_16', 4)	# 45-48
    teleportRelativeX(30000)
    sprite('bc430_17', 4)	# 49-52
    teleportRelativeX(30000)
    sprite('bc430_18', 4)	# 53-56
    teleportRelativeX(30000)
    sprite('bc430_19', 4)	# 57-60

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Unknown11092(1)
        AirPushbackY(17000)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('bc251_00', 2)	# 1-2
    sprite('bc251_01', 2)	# 3-4
    sprite('bc251_02', 3)	# 5-7
    GFX_0('Zanzoh_Air5B', 100)
    SFX_3('slash_rapier_middle')
    Unknown7009(4)
    sprite('bc251_03', 3)	# 8-10	 **attackbox here**
    sprite('bc251_05', 3)	# 11-13	 **attackbox here**
    Unknown23054('62633235315f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('bc251_05', 3)	# 14-16	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('bc251_06', 5)	# 17-21
    sprite('bc251_07', 5)	# 22-26
    sprite('bc251_08', 4)	# 27-30

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('bc252_00', 2)	# 1-2
    sprite('bc252_01', 2)	# 3-4
    sprite('bc252_02', 2)	# 5-6
    GFX_0('Zanzoh_Air5B2nd', 100)
    SFX_3('slash_rapier_middle')
    Unknown7009(5)
    sprite('bc252_03', 3)	# 7-9	 **attackbox here**
    sprite('bc252_04', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('bc252_05', 4)	# 14-17
    sprite('bc252_06', 4)	# 18-21
    sprite('bc252_07', 3)	# 22-24

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_LANDING():
            Unknown23029(11, 261, 0)

        def upon_STATE_END():
            Unknown23029(11, 262, 0)
    sprite('bc254_00', 3)	# 1-3
    sprite('bc254_01', 2)	# 4-5
    sprite('bc254_01', 2)	# 6-7
    Unknown23029(11, 260, 0)
    Unknown7007('7062633132305f300000000000000000640000007062633132305f310000000000000000640000007062633132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('bc254_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    sprite('bc254_03', 2)	# 12-13
    sprite('bc254_03', 2)	# 14-15
    Recovery()
    Unknown2063()
    sprite('bc254_04', 4)	# 16-19
    sprite('bc254_05', 4)	# 20-23
    sprite('bc254_03', 5)	# 24-28
    sprite('bc254_04', 5)	# 29-33
    sprite('bc254_05', 6)	# 34-39
    sprite('bc254_00', 6)	# 40-45

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(55000)
        AirPushbackY(-40000)
        AirUntechableTime(36)
        Unknown9202(1)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        HitOverhead(2)
        JumpCancel_(0)
        callSubroutine('MidAssault_koutyoku')
    sprite('bc401_01', 3)	# 1-3
    sprite('bc401_02', 3)	# 4-6
    Unknown1084(1)
    physicsXImpulse(10000)
    physicsYImpulse(22500)
    setGravity(2000)
    Unknown3029(1)
    SFX_3('highjump_l')
    Unknown23087(80000)
    sprite('bc401_03', 2)	# 7-8
    sprite('bc401_04', 2)	# 9-10
    sprite('bc401_05', 2)	# 11-12
    sprite('bc401_06', 2)	# 13-14
    Unknown7009(5)
    sprite('bc401_09', 2)	# 15-16	 **attackbox here**
    SFX_3('airdash_m')
    SFX_3('slash_pole_middle')
    physicsXImpulse(33750)
    physicsYImpulse(-29250)
    setGravity(0)
    sprite('bc401_10', 2)	# 17-18	 **attackbox here**
    GFX_0('AirMidAssault', 0)
    Unknown38(4, 1)
    Unknown4048(-45000)
    Unknown4045('626365665f6d696461737361756c745f6164645f30330000000000000000000000000000')
    sprite('bc401_11', 3)	# 19-21	 **attackbox here**
    GFX_0('AirMidAssault', 0)
    Unknown38(4, 1)
    label(0)
    sprite('bc401_10', 3)	# 22-24	 **attackbox here**
    GFX_0('AirMidAssault', 0)
    Unknown38(4, 1)
    Unknown4048(-45000)
    Unknown4045('626365665f6d696461737361756c745f6164645f30330000000000000000000000000000')
    sprite('bc401_11', 3)	# 25-27	 **attackbox here**
    GFX_0('AirMidAssault', 0)
    Unknown38(4, 1)
    Unknown1015(22500)
    Unknown1021(-19500)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc401_12', 4)	# 28-31
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    setGravity(0)
    physicsYImpulse(0)
    Unknown1019(60)
    Unknown13(4)
    Recovery()
    Unknown23087(-1)
    sprite('bc401_13', 4)	# 32-35
    Unknown1019(30)
    sprite('bc401_14', 5)	# 36-40
    Unknown1019(0)
    sprite('bc401_15', 5)	# 41-45
    loopRest()
    ExitState()
    label(2)
    sprite('bc401_12', 3)	# 46-48
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    setGravity(0)
    physicsYImpulse(0)
    Unknown1019(60)
    Unknown13(4)
    Recovery()
    Unknown23087(-1)
    sprite('bc401_12', 3)	# 49-51
    Unknown1019(60)
    sprite('bc401_12', 3)	# 52-54
    Unknown1019(30)
    sprite('bc401_13', 3)	# 55-57
    Unknown1019(20)
    sprite('bc401_13', 3)	# 58-60
    Unknown1019(0)
    sprite('bc401_13', 3)	# 61-63
    sprite('bc401_14', 5)	# 64-68
    sprite('bc401_15', 5)	# 69-73
    loopRest()
    ExitState()
    label(3)
    sprite('bc401_12', 4)	# 74-77
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    setGravity(0)
    physicsYImpulse(0)
    Unknown1019(60)
    Unknown13(4)
    Recovery()
    Unknown23087(-1)
    sprite('bc401_12', 4)	# 78-81
    Unknown1019(60)
    sprite('bc401_12', 4)	# 82-85
    Unknown1019(30)
    sprite('bc401_13', 4)	# 86-89
    Unknown1019(20)
    sprite('bc401_13', 4)	# 90-93
    Unknown1019(0)
    sprite('bc401_13', 4)	# 94-97
    sprite('bc401_14', 7)	# 98-104
    sprite('bc401_15', 7)	# 105-111

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
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
    sprite('bc032_10', 3)	# 1-3
    sprite('bc032_00', 4)	# 4-7
    sprite('bc032_01', 4)	# 8-11
    sprite('bc032_02', 4)	# 12-15
    label(0)
    sprite('bc032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('bc032_04', 4)	# 20-23
    sprite('bc032_05', 4)	# 24-27
    sprite('bc032_06', 4)	# 28-31
    sprite('bc032_07', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('bc032_08', 4)	# 36-39
    sprite('bc032_01', 4)	# 40-43
    sprite('bc032_02', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc310_00', 1)	# 48-48
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('bc310_01', 2)	# 49-50
    sprite('bc310_02', 3)	# 51-53	 **attackbox here**
    Unknown1084(1)
    sprite('bc310_03', 3)	# 54-56
    sprite('bc310_04', 10)	# 57-66
    SFX_4('pbc154')
    sprite('bc310_03', 4)	# 67-70
    sprite('bc310_01', 4)	# 71-74
    sprite('bc310_00', 2)	# 75-76

@State
def NmlAtkThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AttackP2(50)
        AirPushbackY(40000)
        Unknown2004(1, 0)
    sprite('bc310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('bc311_00', 4)	# 5-8
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('bc311_01', 4)	# 9-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_3('hit_m_fast')
    SFX_4('pbc153')
    sprite('bc311_02', 4)	# 13-16	 **attackbox here**
    RefreshMultihit()
    sprite('bc311_03', 9)	# 17-25	 **attackbox here**
    Unknown23027()
    sprite('bc311_04', 6)	# 26-31
    sprite('bc311_05', 6)	# 32-37
    sprite('bc311_06', 5)	# 38-42
    sprite('bc311_07', 5)	# 43-47

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkBackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
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
    sprite('bc032_10', 3)	# 1-3
    sprite('bc032_00', 4)	# 4-7
    sprite('bc032_01', 4)	# 8-11
    sprite('bc032_02', 4)	# 12-15
    label(0)
    sprite('bc032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('bc032_04', 4)	# 20-23
    sprite('bc032_05', 4)	# 24-27
    sprite('bc032_06', 4)	# 28-31
    sprite('bc032_07', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('bc032_08', 4)	# 36-39
    sprite('bc032_01', 4)	# 40-43
    sprite('bc032_02', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc310_00', 1)	# 48-48
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('bc310_01', 2)	# 49-50
    sprite('bc310_02', 3)	# 51-53	 **attackbox here**
    Unknown1084(1)
    sprite('bc310_03', 3)	# 54-56
    sprite('bc310_04', 10)	# 57-66
    SFX_4('pbc154')
    sprite('bc310_03', 4)	# 67-70
    sprite('bc310_01', 4)	# 71-74
    sprite('bc310_00', 2)	# 75-76

@State
def NmlAtkBackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AttackP2(50)
        AirPushbackY(40000)
        Unknown2004(1, 0)
    sprite('bc310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('bc311_00', 4)	# 5-8
    Unknown2005()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    Unknown2018(1, 80)
    sprite('bc311_01', 4)	# 9-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_3('hit_m_fast')
    SFX_4('pbc153')
    sprite('bc311_02', 4)	# 13-16	 **attackbox here**
    RefreshMultihit()
    sprite('bc311_03', 9)	# 17-25	 **attackbox here**
    Unknown23027()
    sprite('bc311_04', 6)	# 26-31
    sprite('bc311_05', 6)	# 32-37
    sprite('bc311_06', 5)	# 38-42
    sprite('bc311_07', 5)	# 43-47

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1700)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(30000)
        AirPushbackX(8000)
        Unknown9016(1)
        Unknown9266(4)
        AirUntechableTime(60)
        Unknown1084(0)
        sendToLabelUpon(2, 1)
    sprite('bc400_00', 3)	# 1-3
    Unknown7007('6263333030000000000000000000000064000000626332303300000000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('bc400_01', 3)	# 4-6
    label(10)
    sprite('bc400_02', 3)	# 7-9
    physicsXImpulse(15000)
    sprite('bc400_03', 3)	# 10-12	 **attackbox here**
    SFX_3('slash_sword_fast')
    SFX_3('bc002')
    tag_voice(1, 'pbc200_0', 'pbc200_1', 'pbc200_2', '')
    RefreshMultihit()
    GFX_0('ReversalNigiyakasi', 100)
    GFX_1('bcef_jumonjithunder_04', 0)
    sprite('bc400_04', 10)	# 13-22	 **attackbox here**
    SFX_3('slash_sword_slow')
    SFX_3('slash_rapier_middle')
    RefreshMultihit()
    GFX_1('bcef_jumonjithunder_04', 0)
    AirPushbackY(50000)
    AirPushbackX(4000)
    physicsYImpulse(46000)
    physicsXImpulse(6000)
    setGravity(2100)
    Unknown22004(10, 10)
    sprite('bc400_05', 3)	# 23-25
    GFX_1('bcef_jumonjithunder_04', 0)
    setInvincible(0)
    sprite('bc400_06', 3)	# 26-28
    GFX_1('bcef_jumonjithunder_04', 0)
    sprite('bc400_07', 3)	# 29-31
    sprite('bc400_08', 3)	# 32-34
    sprite('bc400_09', 3)	# 35-37
    sprite('bc020_04', 3)	# 38-40
    sprite('bc020_05', 3)	# 41-43
    sprite('bc020_06', 3)	# 44-46
    label(0)
    sprite('bc020_07', 4)	# 47-50
    sprite('bc020_08', 4)	# 51-54
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc120_01', 2)	# 55-56
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    Unknown1084(1)
    sprite('bc120_00', 7)	# 57-63
    loopRest()

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1700)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        AirPushbackX(8000)
        Unknown9016(1)
        Unknown11092(1)
        Unknown9266(4)
        AirUntechableTime(39)
        Unknown1084(0)
        Unknown13024(0)
        Unknown13045(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('bc400_10', 3)	# 1-3
    sprite('bc400_11', 3)	# 4-6	 **attackbox here**
    SFX_3('slash_sword_fast')
    SFX_3('bc002')
    tag_voice(1, 'pbc200_0', 'pbc200_1', 'pbc200_2', '')
    RefreshMultihit()
    GFX_0('ReversalNigiyakasi', 100)
    GFX_1('bcef_jumonjithunder_04', 0)
    sprite('bc400_04', 3)	# 7-9	 **attackbox here**
    SFX_3('slash_sword_slow')
    SFX_3('slash_rapier_middle')
    RefreshMultihit()
    GFX_1('bcef_jumonjithunder_04', 0)
    AirPushbackY(45000)
    physicsYImpulse(38000)
    physicsXImpulse(2000)
    setGravity(2100)
    sprite('bc400_05', 3)	# 10-12
    GFX_1('bcef_jumonjithunder_04', 0)
    Unknown21012('526576657273616c416374696f6e00000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('bc400_06', 3)	# 13-15
    GFX_1('bcef_jumonjithunder_04', 0)
    sprite('bc400_07', 3)	# 16-18
    sprite('bc400_08', 3)	# 19-21
    sprite('bc400_09', 3)	# 22-24
    sprite('bc020_04', 3)	# 25-27
    sprite('bc020_05', 3)	# 28-30
    sprite('bc020_06', 3)	# 31-33
    label(0)
    sprite('bc020_07', 4)	# 34-37
    sprite('bc020_08', 4)	# 38-41
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc120_01', 2)	# 42-43
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    Unknown1084(1)
    sprite('bc120_00', 7)	# 44-50
    loopRest()

@State
def LowAssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(26000)
        AirPushbackY(18000)
        AirUntechableTime(60)
        Unknown11058('0000000000000000010000000000000000000000')
        HitLow(2)
        Unknown9016(1)
        Unknown9266(4)
        Unknown23027()
    sprite('bc402_00', 2)	# 1-2
    sprite('bc402_01', 2)	# 3-4
    sprite('bc402_02', 2)	# 5-6
    GFX_1('persona_enter_ply', 0)
    Unknown18009(1)
    Unknown23029(11, 530, 0)
    Unknown4020(11)
    sprite('bc402_02', 2)	# 7-8
    physicsXImpulse(6000)
    SFX_3('airdash_m')
    tag_voice(1, 'pbc204_0', 'pbc204_1', 'pbc204_2', '')
    sprite('bc402_03', 2)	# 9-10
    Unknown1019(300)
    sprite('bc402_03', 2)	# 11-12
    Unknown1019(300)
    sprite('bc402_04', 2)	# 13-14	 **attackbox here**
    sprite('bc402_05', 2)	# 15-16	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    sprite('bc402_04', 2)	# 17-18	 **attackbox here**
    sprite('bc402_05', 2)	# 19-20	 **attackbox here**
    sprite('bc402_04', 2)	# 21-22	 **attackbox here**
    Unknown1019(50)
    sprite('bc402_06', 5)	# 23-27
    Unknown1019(0)
    Recovery()
    Unknown4020(0)
    sprite('bc402_07', 5)	# 28-32
    sprite('bc402_08', 5)	# 33-37
    sprite('bc402_09', 5)	# 38-42

@State
def LowAssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(70)
        Unknown11092(1)
        AirPushbackY(1000)
        AirUntechableTime(60)
        Unknown9310(1)
        Hitstop(1)
        Unknown11058('0000000000000000010000000000000000000000')
        HitLow(2)
        Unknown9016(1)
        Unknown9266(4)
        Unknown11057(700)
        Unknown23027()
    sprite('bc402_00', 3)	# 1-3
    sprite('bc402_01', 3)	# 4-6
    sprite('bc402_02', 2)	# 7-8
    GFX_1('persona_enter_ply', 0)
    Unknown18009(1)
    Unknown23029(11, 540, 0)
    Unknown4020(11)
    sprite('bc402_02', 2)	# 9-10
    physicsXImpulse(6000)
    SFX_3('airdash_m')
    tag_voice(1, 'pbc204_0', 'pbc204_1', 'pbc204_2', '')
    sprite('bc402_03', 2)	# 11-12
    Unknown1019(300)
    sprite('bc402_03', 2)	# 13-14
    Unknown1019(300)
    sprite('bc402_04', 3)	# 15-17	 **attackbox here**
    sprite('bc402_05', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    sprite('bc402_04', 3)	# 21-23	 **attackbox here**
    sprite('bc402_05', 3)	# 24-26	 **attackbox here**
    sprite('bc402_04', 3)	# 27-29	 **attackbox here**
    RefreshMultihit()
    sprite('bc402_05', 3)	# 30-32	 **attackbox here**
    sprite('bc402_04', 3)	# 33-35	 **attackbox here**
    sprite('bc402_05', 3)	# 36-38	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(12000)
    AirPushbackY(18000)
    Unknown9310(0)
    Hitstop(12)
    Unknown1019(50)
    sprite('bc402_06', 7)	# 39-45
    Unknown1019(0)
    Recovery()
    Unknown4020(0)
    sprite('bc402_07', 7)	# 46-52
    sprite('bc402_08', 7)	# 53-59
    sprite('bc402_09', 8)	# 60-67

@State
def LowAssaultEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        AttackP1(70)
        Unknown11092(1)
        AirPushbackY(1000)
        AirUntechableTime(60)
        Unknown9310(1)
        Hitstop(1)
        Unknown11058('0000000000000000010000000000000000000000')
        HitLow(2)
        Unknown9016(1)
        Unknown9266(4)
        Unknown11057(700)
        Unknown30065(0)
        Unknown23027()
        Unknown11091(10)
    sprite('bc402_00', 1)	# 1-1
    sprite('bc402_01', 2)	# 2-3
    sprite('bc402_02', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    GFX_1('persona_enter_ply', 0)
    Unknown18009(1)
    Unknown23029(11, 550, 0)
    Unknown4020(11)
    physicsXImpulse(6000)
    SFX_3('airdash_m')
    tag_voice(1, 'pbc204_0', 'pbc204_1', 'pbc204_2', '')
    sprite('bc402_03', 3)	# 6-8
    Unknown1019(900)
    sprite('bc402_04', 3)	# 9-11	 **attackbox here**
    sprite('bc402_05', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('bc402_04', 3)	# 15-17	 **attackbox here**
    sprite('bc402_05', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    sprite('bc402_04', 3)	# 21-23	 **attackbox here**
    sprite('bc402_05', 3)	# 24-26	 **attackbox here**
    RefreshMultihit()
    sprite('bc402_04', 3)	# 27-29	 **attackbox here**
    sprite('bc402_05', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    sprite('bc402_04', 3)	# 33-35	 **attackbox here**
    sprite('bc402_05', 3)	# 36-38	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(8000)
    AirPushbackY(18000)
    Unknown9310(0)
    Hitstop(12)
    Unknown1019(50)
    HitCancel('InvincibleAttackAdd')
    sprite('bc402_06', 7)	# 39-45
    Unknown1019(0)
    Recovery()
    Unknown2063()
    Unknown4020(0)
    sprite('bc402_07', 7)	# 46-52
    sprite('bc402_08', 7)	# 53-59
    sprite('bc402_09', 8)	# 60-67

@State
def InvincibleAttackAdd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(700)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown9266(4)
        Unknown30065(0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
        Unknown1084(0)
        physicsXImpulse(15000)
        sendToLabelUpon(2, 1)
        Unknown30068(1)
        Unknown11091(10)
    sprite('bc400_02', 3)	# 1-3
    sprite('bc400_03', 3)	# 4-6	 **attackbox here**
    SFX_3('slash_sword_fast')
    SFX_3('bc002')
    RefreshMultihit()
    GFX_0('ReversalNigiyakasi', 100)
    GFX_1('bcef_jumonjithunder_04', 0)
    sprite('bc400_04', 5)	# 7-11	 **attackbox here**
    SFX_3('slash_sword_slow')
    SFX_3('slash_rapier_middle')
    RefreshMultihit()
    GFX_1('bcef_jumonjithunder_04', 0)
    physicsYImpulse(46000)
    physicsXImpulse(6000)
    setGravity(2100)
    AirPushbackY(40000)
    sprite('bc400_04', 5)	# 12-16	 **attackbox here**
    RefreshMultihit()
    sprite('bc400_05', 3)	# 17-19
    GFX_1('bcef_jumonjithunder_04', 0)
    Recovery()
    sprite('bc400_06', 3)	# 20-22
    GFX_1('bcef_jumonjithunder_04', 0)
    sprite('bc400_07', 3)	# 23-25
    sprite('bc400_08', 3)	# 26-28
    sprite('bc400_09', 3)	# 29-31
    sprite('bc020_04', 3)	# 32-34
    sprite('bc020_05', 3)	# 35-37
    sprite('bc020_06', 3)	# 38-40
    label(0)
    sprite('bc020_07', 4)	# 41-44
    sprite('bc020_08', 4)	# 45-48
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc120_01', 2)	# 49-50
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    Unknown1084(1)
    sprite('bc120_00', 7)	# 51-57

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('bc403_00', 3)	# 1-3
    sprite('bc403_01', 4)	# 4-7
    Unknown23029(11, 500, 0)
    Unknown7006('pbc206_0', 100, 845374064, 828323376, 0, 0, 100, 845374064, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('bc403_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    sprite('bc403_03', 4)	# 12-15
    sprite('bc403_04', 4)	# 16-19
    sprite('bc403_05', 4)	# 20-23
    sprite('bc403_03', 4)	# 24-27
    sprite('bc403_04', 4)	# 28-31
    sprite('bc403_05', 4)	# 32-35
    sprite('bc403_03', 4)	# 36-39
    Recovery()
    sprite('bc403_04', 4)	# 40-43
    sprite('bc403_00', 4)	# 44-47

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('bc403_00', 3)	# 1-3
    sprite('bc403_01', 4)	# 4-7
    Unknown23029(11, 510, 0)
    Unknown7006('pbc206_0', 100, 845374064, 828323376, 0, 0, 100, 845374064, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('bc403_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    sprite('bc403_03', 4)	# 12-15
    sprite('bc403_04', 4)	# 16-19
    sprite('bc403_05', 4)	# 20-23
    sprite('bc403_03', 4)	# 24-27
    sprite('bc403_04', 4)	# 28-31
    sprite('bc403_05', 4)	# 32-35
    sprite('bc403_03', 4)	# 36-39
    sprite('bc403_04', 4)	# 40-43
    sprite('bc403_05', 4)	# 44-47
    Recovery()
    sprite('bc403_03', 4)	# 48-51
    sprite('bc403_00', 4)	# 52-55

@State
def ShotEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('bc403_00', 3)	# 1-3
    Unknown1084(1)
    sprite('bc403_01', 4)	# 4-7
    Unknown23125('')
    Unknown2058(-5000)
    Unknown23029(11, 520, 0)
    Unknown7006('pbc207_0', 100, 845374064, 828323632, 0, 0, 100, 845374064, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('bc403_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    sprite('bc403_03', 4)	# 12-15
    sprite('bc403_04', 4)	# 16-19
    sprite('bc403_05', 4)	# 20-23
    sprite('bc403_03', 4)	# 24-27
    sprite('bc403_04', 4)	# 28-31
    sprite('bc403_05', 4)	# 32-35
    sprite('bc403_03', 4)	# 36-39
    sprite('bc403_04', 4)	# 40-43
    sprite('bc403_05', 4)	# 44-47
    Recovery()
    sprite('bc403_03', 4)	# 48-51
    sprite('bc403_00', 4)	# 52-55

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown17003()
        if Unknown23145('NmlAtkAir5C'):
            Unknown1018()
            Unknown1023()
            Unknown1038()
        Unknown22004(9, 1)
    sprite('bc255_00', 3)	# 1-3
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('bc255_01', 4)	# 4-7
    Unknown23029(11, 500, 0)
    Unknown7006('pbc206_0', 100, 845374064, 828323376, 0, 0, 100, 845374064, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('bc255_02', 4)	# 8-11
    sprite('bc255_03', 4)	# 12-15
    GFX_1('persona_enter_ply', 0)
    sprite('bc255_04', 4)	# 16-19
    sprite('bc255_05', 4)	# 20-23
    sprite('bc255_06', 4)	# 24-27
    sprite('bc255_04', 4)	# 28-31
    sprite('bc255_05', 4)	# 32-35
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1043()
    Unknown1019(50)
    YAccel(85)
    sprite('bc255_06', 4)	# 36-39
    sprite('bc255_04', 4)	# 40-43
    sprite('bc255_05', 4)	# 44-47
    Recovery()
    sprite('bc255_00', 3)	# 48-50

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown17003()
        if Unknown23145('NmlAtkAir5C'):
            Unknown1018()
            Unknown1023()
            Unknown1038()
        Unknown22004(9, 1)
    sprite('bc255_00', 3)	# 1-3
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('bc255_01', 4)	# 4-7
    Unknown23029(11, 510, 0)
    Unknown7006('pbc206_0', 100, 845374064, 828323376, 0, 0, 100, 845374064, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('bc255_02', 4)	# 8-11
    sprite('bc255_03', 4)	# 12-15
    GFX_1('persona_enter_ply', 0)
    sprite('bc255_04', 4)	# 16-19
    sprite('bc255_05', 4)	# 20-23
    sprite('bc255_06', 4)	# 24-27
    sprite('bc255_04', 4)	# 28-31
    sprite('bc255_05', 4)	# 32-35
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1043()
    Unknown1019(50)
    YAccel(85)
    sprite('bc255_06', 4)	# 36-39
    sprite('bc255_04', 4)	# 40-43
    sprite('bc255_05', 4)	# 44-47
    Recovery()
    sprite('bc255_00', 3)	# 48-50

@State
def AirShotEx():

    def upon_IMMEDIATE():
        Unknown17003()
        if Unknown23145('NmlAtkAir5C'):
            Unknown1018()
            Unknown1023()
            Unknown1038()
        Unknown22004(9, 1)
    sprite('bc255_00', 3)	# 1-3
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('bc255_01', 4)	# 4-7
    Unknown23125('')
    Unknown2058(-5000)
    Unknown23029(11, 520, 0)
    Unknown7006('pbc207_0', 100, 845374064, 828323632, 0, 0, 100, 845374064, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('bc255_02', 4)	# 8-11
    sprite('bc255_03', 4)	# 12-15
    GFX_1('persona_enter_ply', 0)
    sprite('bc255_04', 4)	# 16-19
    sprite('bc255_05', 4)	# 20-23
    sprite('bc255_06', 4)	# 24-27
    sprite('bc255_04', 4)	# 28-31
    sprite('bc255_05', 4)	# 32-35
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1043()
    Unknown1019(50)
    YAccel(85)
    sprite('bc255_06', 4)	# 36-39
    sprite('bc255_04', 4)	# 40-43
    sprite('bc255_05', 4)	# 44-47
    Recovery()
    sprite('bc255_00', 3)	# 48-50

@State
def UltimateLaser():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
    sprite('bc431_00', 4)	# 1-4
    Unknown1084(1)
    if SLOT_36:
        GFX_0('UltimateLaserAsiba', 100)
    sprite('bc431_01', 4)	# 5-8
    tag_voice(1, 'pbc252_0', 'pbc252_1', '', '')
    Unknown2036(33, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('bc431_02', 3)	# 9-11
    Unknown23029(11, 900, 0)
    sprite('bc431_03', 4)	# 12-15
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(10, 1)
    Unknown36(10)
    Unknown1007(61200)
    physicsYImpulse(-1800)
    Unknown35()
    sprite('bc431_01', 3)	# 16-18
    sprite('bc431_02', 3)	# 19-21
    sprite('bc431_03', 3)	# 22-24
    sprite('bc431_01', 3)	# 25-27
    sprite('bc431_02', 3)	# 28-30
    sprite('bc431_03', 3)	# 31-33
    sprite('bc431_01', 3)	# 34-36
    sprite('bc431_02', 3)	# 37-39
    sprite('bc431_03', 3)	# 40-42
    sprite('bc431_04', 3)	# 43-45
    sprite('bc431_05', 3)	# 46-48
    Unknown13(10)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('bc431_06', 3)	# 49-51
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 52-54
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 55-57
    setInvincible(0)
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 58-60
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 61-63
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 64-66
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 67-69
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 70-72
    tag_voice(0, 'pbc253_0', 'pbc253_1', '', '')
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 73-75
    GFX_1('persona_enter_ply', 0)
    if SLOT_85:
        _gotolabel(1)
    sprite('bc431_06', 3)	# 76-78
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 79-81
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 82-84
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 85-87
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 88-90
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 91-93
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 94-96
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 97-99
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 100-102
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 103-105
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 106-108
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 109-111
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 112-114
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 115-117
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 118-120
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 121-123
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 124-126
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 127-129
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 130-132
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 133-135
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 136-138
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 4)	# 139-142
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 4)	# 143-146
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 4)	# 147-150
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 5)	# 151-155
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 5)	# 156-160
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 5)	# 161-165
    sprite('bc431_06', 6)	# 166-171
    sprite('bc431_07', 6)	# 172-177
    label(1)
    sprite('bc431_08', 6)	# 178-183
    sprite('bc431_06', 6)	# 184-189
    if SLOT_36:
        Unknown23159('AirUltimateLaser')
        sendToLabel(99)
    sprite('bc431_09', 6)	# 190-195
    sprite('bc431_10', 6)	# 196-201
    loopRest()
    ExitState()
    label(99)
    sprite('bc431_09', 6)	# 202-207
    sprite('bc431_10', 6)	# 208-213
    sprite('bc010_00', 3)	# 214-216
    sprite('bc020_00', 3)	# 217-219
    physicsYImpulse(10000)
    sprite('bc020_01', 3)	# 220-222
    YAccel(20)

@State
def UltimateLaserOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
    sprite('bc431_00', 4)	# 1-4
    Unknown1084(1)
    if SLOT_36:
        GFX_0('UltimateLaserAsibaOD', 100)
    sprite('bc431_01', 4)	# 5-8
    tag_voice(1, 'pbc252_0', 'pbc252_1', '', '')
    Unknown2036(33, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('bc431_02', 3)	# 9-11
    Unknown23029(11, 910, 0)
    sprite('bc431_03', 4)	# 12-15
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(10, 1)
    Unknown36(10)
    Unknown1007(64500)
    physicsYImpulse(-1500)
    Unknown35()
    sprite('bc431_01', 3)	# 16-18
    sprite('bc431_02', 3)	# 19-21
    sprite('bc431_03', 3)	# 22-24
    sprite('bc431_01', 3)	# 25-27
    sprite('bc431_02', 3)	# 28-30
    sprite('bc431_03', 3)	# 31-33
    sprite('bc431_01', 3)	# 34-36
    sprite('bc431_02', 3)	# 37-39
    sprite('bc431_03', 3)	# 40-42
    sprite('bc431_04', 3)	# 43-45
    sprite('bc431_05', 3)	# 46-48
    Unknown13(10)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('bc431_06', 3)	# 49-51
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 52-54
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 55-57
    setInvincible(0)
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 58-60
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 61-63
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 64-66
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 67-69
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 70-72
    tag_voice(0, 'pbc253_0', 'pbc253_1', '', '')
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 73-75
    GFX_1('persona_enter_ply', 0)
    if SLOT_85:
        _gotolabel(1)
    sprite('bc431_06', 3)	# 76-78
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 79-81
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 82-84
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 85-87
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 88-90
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 91-93
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 94-96
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 97-99
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 100-102
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 103-105
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 106-108
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 109-111
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 112-114
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 115-117
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 118-120
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 121-123
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 124-126
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 127-129
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 3)	# 130-132
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 3)	# 133-135
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 3)	# 136-138
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 4)	# 139-142
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 4)	# 143-146
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 4)	# 147-150
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_06', 5)	# 151-155
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_07', 5)	# 156-160
    GFX_1('persona_enter_ply', 0)
    sprite('bc431_08', 5)	# 161-165
    sprite('bc431_06', 6)	# 166-171
    sprite('bc431_07', 6)	# 172-177
    label(1)
    sprite('bc431_08', 6)	# 178-183
    sprite('bc431_06', 6)	# 184-189
    if SLOT_36:
        Unknown23159('AirUltimateLaserOD')
        sendToLabel(99)
    sprite('bc431_09', 6)	# 190-195
    sprite('bc431_10', 6)	# 196-201
    loopRest()
    ExitState()
    label(99)
    sprite('bc431_09', 6)	# 202-207
    sprite('bc431_10', 6)	# 208-213
    sprite('bc010_00', 3)	# 214-216
    sprite('bc020_00', 3)	# 217-219
    physicsYImpulse(10000)
    sprite('bc020_01', 3)	# 220-222
    YAccel(20)

@State
def UltimateBlade():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2500)
        Unknown11091(25)
        AttackP2(100)
        Unknown9154(100)
        Unknown9310(1)
        Unknown9016(1)
        Unknown9266(4)
        AirHitstunAnimation(5)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown9266(4)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11062(1)
        Unknown2004(1, 0)
        setInvincible(1)

        def upon_78():
            Unknown13024(0)
            SLOT_51 = 1
            GFX_0('jumonjiBigslashYoko', 0)
            Unknown11069('PBC_PersonaUltimateBlade')
    sprite('bc430_00', 5)	# 1-5
    sprite('bc430_01', 5)	# 6-10
    sprite('bc430_02', 3)	# 11-13
    GFX_0('jumonjiSwordAura', 0)
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    Unknown2036(70, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pbc250_0', 'pbc250_1', '', '')
    sprite('bc430_03', 3)	# 14-16
    sprite('bc430_04', 3)	# 17-19
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_02', 3)	# 20-22
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_03', 3)	# 23-25
    sprite('bc430_04', 3)	# 26-28
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 29-31
    sprite('bc430_03', 3)	# 32-34
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_04', 3)	# 35-37
    sprite('bc430_02', 3)	# 38-40
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 41-43
    sprite('bc430_04', 3)	# 44-46
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_02', 3)	# 47-49
    sprite('bc430_03', 3)	# 50-52
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 53-55
    sprite('bc430_02', 3)	# 56-58
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 59-61
    sprite('bc430_04', 3)	# 62-64
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 65-67
    sprite('bc430_03', 3)	# 68-70
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 71-73
    sprite('bc430_05', 3)	# 74-76
    Unknown13(1)
    GFX_0('jumonjiBcSlash', 100)
    sprite('bc430_06', 3)	# 77-79
    sprite('bc430_07', 3)	# 80-82
    SFX_3('cut_l')
    sprite('bc430_08', 3)	# 83-85
    sprite('bc430_10', 3)	# 86-88	 **attackbox here**
    Unknown23054('62633433305f303900000000000000000000000000000000000000000000000003000000')
    SFX_3('bc001')
    RefreshMultihit()
    sprite('bc430_10', 4)	# 89-92	 **attackbox here**
    sprite('bc430_11', 4)	# 93-96
    Unknown23027()
    setInvincible(0)
    loopRest()
    Unknown19(2, 2, 51)
    sprite('bc430_12', 4)	# 97-100
    Unknown23029(11, 920, 0)
    tag_voice(0, 'pbc251_0', 'pbc251_1', '', '')
    sprite('bc430_10', 4)	# 101-104	 **attackbox here**
    sprite('bc430_11', 4)	# 105-108
    sprite('bc430_12', 4)	# 109-112
    sprite('bc430_10', 4)	# 113-116	 **attackbox here**
    sprite('bc430_11', 4)	# 117-120
    sprite('bc430_12', 4)	# 121-124
    sprite('bc430_10', 4)	# 125-128	 **attackbox here**
    sprite('bc430_11', 4)	# 129-132
    sprite('bc430_12', 4)	# 133-136
    sprite('bc430_10', 4)	# 137-140	 **attackbox here**
    sprite('bc430_11', 4)	# 141-144
    sprite('bc430_12', 4)	# 145-148
    sprite('bc430_10', 4)	# 149-152	 **attackbox here**
    sprite('bc430_11', 4)	# 153-156
    sprite('bc430_12', 4)	# 157-160
    sprite('bc430_10', 4)	# 161-164	 **attackbox here**
    sprite('bc430_11', 4)	# 165-168
    sprite('bc430_12', 4)	# 169-172
    sprite('bc430_10', 4)	# 173-176	 **attackbox here**
    sprite('bc430_11', 4)	# 177-180
    sprite('bc430_12', 4)	# 181-184
    sprite('bc430_10', 4)	# 185-188	 **attackbox here**
    label(2)
    sprite('bc430_10', 4)	# 189-192	 **attackbox here**
    sprite('bc430_13', 4)	# 193-196
    sprite('bc430_14', 4)	# 197-200
    sprite('bc430_15', 4)	# 201-204
    sprite('bc430_16', 4)	# 205-208
    sprite('bc430_17', 4)	# 209-212
    sprite('bc430_18', 4)	# 213-216
    sprite('bc430_19', 3)	# 217-219
    sprite('bc430_19', 1)	# 220-220
    if SLOT_51:
        Unknown23029(11, 9999, 0)

@State
def UltimateBladeOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2500)
        Unknown11091(25)
        AttackP2(100)
        Unknown9154(100)
        Unknown9310(1)
        Unknown9016(1)
        Unknown9266(4)
        AirHitstunAnimation(5)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown9266(4)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11062(1)
        Unknown2004(1, 0)
        setInvincible(1)

        def upon_78():
            Unknown13024(0)
            SLOT_51 = 1
            GFX_0('jumonjiBigslashYoko', 0)
            Unknown23029(1, 970, 0)
            Unknown11069('PBC_PersonaUltimateBladeOD')
    sprite('bc430_00', 5)	# 1-5
    sprite('bc430_01', 5)	# 6-10
    sprite('bc430_02', 3)	# 11-13
    GFX_0('jumonjiSwordAura', 0)
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    Unknown2036(70, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pbc250_0', 'pbc250_1', '', '')
    sprite('bc430_03', 3)	# 14-16
    sprite('bc430_04', 3)	# 17-19
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_02', 3)	# 20-22
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_03', 3)	# 23-25
    sprite('bc430_04', 3)	# 26-28
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 29-31
    sprite('bc430_03', 3)	# 32-34
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_04', 3)	# 35-37
    sprite('bc430_02', 3)	# 38-40
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 41-43
    sprite('bc430_04', 3)	# 44-46
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_02', 3)	# 47-49
    sprite('bc430_03', 3)	# 50-52
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 53-55
    sprite('bc430_02', 3)	# 56-58
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 59-61
    sprite('bc430_04', 3)	# 62-64
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 65-67
    sprite('bc430_03', 3)	# 68-70
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 71-73
    sprite('bc430_05', 3)	# 74-76
    Unknown13(1)
    GFX_0('jumonjiBcSlash', 100)
    sprite('bc430_06', 3)	# 77-79
    sprite('bc430_07', 3)	# 80-82
    SFX_3('cut_l')
    sprite('bc430_08', 3)	# 83-85
    sprite('bc430_10', 3)	# 86-88	 **attackbox here**
    Unknown23054('62633433305f303900000000000000000000000000000000000000000000000003000000')
    SFX_3('bc001')
    RefreshMultihit()
    sprite('bc430_10', 4)	# 89-92	 **attackbox here**
    sprite('bc430_11', 4)	# 93-96
    Unknown23027()
    setInvincible(0)
    loopRest()
    Unknown19(2, 2, 51)
    sprite('bc430_13', 4)	# 97-100
    sprite('bc430_14', 4)	# 101-104
    sprite('bc430_15', 4)	# 105-108
    sprite('bc430_16', 4)	# 109-112
    sprite('bc430_17', 4)	# 113-116
    sprite('bc430_18', 4)	# 117-120
    sprite('bc433_17', 8)	# 121-128
    sprite('bc433_18', 8)	# 129-136
    sprite('bc433_19', 8)	# 137-144
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(10, 1)
    Unknown36(10)
    Unknown1007(61200)
    physicsYImpulse(-1800)
    Unknown35()
    sprite('bc433_20', 4)	# 145-148
    Unknown13(10)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    Unknown2036(60, -1, 0)
    Unknown23029(11, 930, 0)
    tag_voice(0, 'pbc251_0', 'pbc251_1', '', '')
    sprite('bc433_21', 4)	# 149-152
    sprite('bc433_22', 4)	# 153-156
    sprite('bc433_23', 4)	# 157-160
    sprite('bc433_21', 4)	# 161-164
    sprite('bc433_22', 4)	# 165-168
    sprite('bc433_23', 4)	# 169-172
    sprite('bc433_21', 4)	# 173-176
    sprite('bc433_22', 4)	# 177-180
    sprite('bc433_23', 4)	# 181-184
    sprite('bc433_21', 4)	# 185-188
    sprite('bc433_22', 4)	# 189-192
    sprite('bc433_23', 4)	# 193-196
    sprite('bc433_21', 4)	# 197-200
    sprite('bc433_22', 4)	# 201-204
    sprite('bc433_23', 4)	# 205-208
    sprite('bc433_21', 4)	# 209-212
    sprite('bc433_22', 4)	# 213-216
    sprite('bc433_23', 4)	# 217-220
    sprite('bc433_21', 4)	# 221-224
    sprite('bc433_22', 4)	# 225-228
    sprite('bc433_23', 4)	# 229-232
    sprite('bc433_21', 4)	# 233-236
    sprite('bc433_22', 4)	# 237-240
    sprite('bc433_23', 4)	# 241-244
    sprite('bc433_21', 4)	# 245-248
    sprite('bc433_22', 4)	# 249-252
    sprite('bc433_23', 4)	# 253-256
    sprite('bc433_21', 4)	# 257-260
    sprite('bc433_22', 4)	# 261-264
    sprite('bc433_23', 4)	# 265-268
    sprite('bc433_21', 4)	# 269-272
    sprite('bc433_22', 4)	# 273-276
    sprite('bc433_23', 4)	# 277-280
    sprite('bc433_21', 4)	# 281-284
    sprite('bc433_22', 4)	# 285-288
    sprite('bc433_23', 4)	# 289-292
    sprite('bc433_21', 4)	# 293-296
    sprite('bc433_22', 4)	# 297-300
    sprite('bc433_23', 4)	# 301-304
    sprite('bc433_21', 4)	# 305-308
    sprite('bc433_22', 4)	# 309-312
    sprite('bc433_23', 4)	# 313-316
    sprite('bc433_21', 4)	# 317-320
    sprite('bc433_24', 4)	# 321-324
    sprite('bc433_25', 4)	# 325-328
    sprite('bc433_26', 3)	# 329-331
    ExitState()
    label(2)
    sprite('bc430_10', 4)	# 332-335	 **attackbox here**
    sprite('bc430_13', 4)	# 336-339
    sprite('bc430_14', 4)	# 340-343
    sprite('bc430_15', 4)	# 344-347
    sprite('bc430_16', 4)	# 348-351
    sprite('bc430_17', 4)	# 352-355
    sprite('bc430_18', 4)	# 356-359
    sprite('bc430_19', 4)	# 360-363

@State
def TagExitChar():

    def upon_IMMEDIATE():
        pass
    sprite('keep', 32767)	# 1-32767
    Unknown3038(1)
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(-2000000)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown2017(0)
        Unknown2034(0)
        teleportRelativeY(0)
    label(0)
    sprite('null', 1)	# 1-1
    gotoLabel(0)

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('bc401_10', 3)	# 26-28	 **attackbox here**
    GFX_0('MidAssault', 0)
    Unknown38(4, 1)
    Unknown1086(22)
    teleportRelativeX(-300000)
    teleportRelativeX(-1450000)
    teleportRelativeY(1000000)
    physicsXImpulse(150000)
    physicsYImpulse(-100000)
    setGravity(0)
    label(0)
    sprite('bc401_10', 3)	# 29-31	 **attackbox here**
    sprite('bc401_11', 3)	# 32-34	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 3)	# 35-37
    Unknown1019(30)
    sprite('bc401_12', 8)	# 38-45
    Unknown8000(100, 1, 1)
    Unknown13(4)
    Unknown1019(10)
    sprite('bc401_13', 8)	# 46-53
    sprite('bc401_14', 3)	# 54-56
    Unknown1084(1)
    sprite('bc401_15', 3)	# 57-59

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('bc033_01', 3)	# 1-3
    sprite('bc033_02', 3)	# 4-6
    sprite('bc033_01', 3)	# 7-9
    sprite('bc033_02', 3)	# 10-12
    sprite('bc033_01', 3)	# 13-15
    sprite('bc033_02', 3)	# 16-18
    sprite('bc033_01', 3)	# 19-21
    sprite('bc033_02', 3)	# 22-24
    sprite('bc033_01', 3)	# 25-27
    sprite('bc033_02', 3)	# 28-30
    sprite('bc033_01', 30)	# 31-60

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('bc205_00', 5)	# 1-5
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    sprite('bc205_01', 4)	# 6-9
    sprite('bc205_02', 4)	# 10-13
    sprite('bc205_03', 4)	# 14-17
    sprite('bc205_04', 4)	# 18-21
    sprite('bc205_05', 4)	# 22-25
    sprite('bc205_06', 4)	# 26-29
    sprite('bc205_04', 4)	# 30-33
    sprite('bc205_05', 4)	# 34-37
    sprite('bc205_06', 4)	# 38-41
    sprite('bc205_04', 4)	# 42-45
    sprite('bc205_05', 4)	# 46-49
    sprite('bc205_05', 4)	# 50-53
    sprite('bc205_06', 4)	# 54-57
    sprite('bc205_00', 5)	# 58-62

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        Unknown17015()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('bc045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('bc045_00', 3)	# 2-4
    sprite('bc045_01', 4)	# 5-8
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    label(0)
    sprite('bc045_02', 5)	# 9-13
    sprite('bc045_03', 5)	# 14-18
    loopRest()
    Unknown2038(1)
    if (SLOT_2 == 5):
        Unknown1018()
        Unknown1023()
        Unknown1038()
        Unknown1019(40)
        YAccel(40)
    (SLOT_2 >= 6)
    if SLOT_0:
        _gotolabel(1)
    gotoLabel(0)
    label(1)
    sprite('bc045_01', 6)	# 19-24
    sprite('bc045_00', 6)	# 25-30

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17015()
    sprite('bc001_00', 7)	# 1-7
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    Unknown2067(2500, 240)
    sprite('bc001_01', 7)	# 8-14
    sprite('bc001_02', 7)	# 15-21
    sprite('bc001_03', 7)	# 22-28
    sprite('bc001_04', 7)	# 29-35
    sprite('bc001_05', 7)	# 36-42
    label(1)
    sprite('bc001_06', 15)	# 43-57
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('bc001_00', 7)	# 58-64

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('bc001_00', 7)	# 1-7
    sprite('bc001_01', 7)	# 8-14
    sprite('bc001_02', 7)	# 15-21
    sprite('bc001_03', 7)	# 22-28
    sprite('bc001_04', 7)	# 29-35
    sprite('bc001_05', 7)	# 36-42
    sprite('bc001_06', 27)	# 43-69
    sprite('bc001_00', 30)	# 70-99

@State
def CmnActChangePartnerQuickIn():
    sprite('bc032_05', 3)	# 1-3
    sprite('bc032_06', 5)	# 4-8
    sprite('bc032_09', 7)	# 9-15
    sprite('bc032_09', 7)	# 16-22
    sprite('bc032_10', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('bc033_00', 1)	# 1-1
    sprite('bc033_01', 2)	# 2-3
    sprite('bc033_01', 2)	# 4-5
    sprite('bc033_02', 1)	# 6-6
    sprite('bc033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('bc033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc033_03', 3)	# 13-15
    sprite('bc033_04', 3)	# 16-18

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
    sprite('bc020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('bc020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('bc010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()

        def upon_43():
            if (SLOT_48 == 201):
                clearUponHandler(17)
                clearUponHandler(43)
                sendToLabel(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            clearUponHandler(43)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('bc205_00', 2)	# 1-2
    sprite('bc205_01', 4)	# 3-6
    sprite('bc205_02', 4)	# 7-10
    sprite('bc205_03', 4)	# 11-14
    Unknown7007('7062633132315f300000000000000000640000007062633132315f310000000000000000640000007062633132315f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23029(11, 200, 0)
    GFX_1('persona_enter_ply', 0)
    label(0)
    sprite('bc205_04', 4)	# 15-18
    sprite('bc205_05', 4)	# 19-22
    sprite('bc205_06', 4)	# 23-26
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bc205_04', 4)	# 27-30
    sprite('bc205_05', 4)	# 31-34
    sprite('bc205_06', 4)	# 35-38
    sprite('bc205_00', 4)	# 39-42

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()
        Unknown11042(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('bc403_00', 3)	# 1-3
    sprite('bc403_01', 4)	# 4-7
    sprite('bc403_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 202, 0)
    Unknown7007('7062633132305f300000000000000000640000007062633132305f310000000000000000640000007062633132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('bc403_03', 4)	# 12-15
    sprite('bc403_04', 4)	# 16-19
    sprite('bc403_05', 4)	# 20-23
    sprite('bc403_03', 4)	# 24-27
    sprite('bc403_04', 4)	# 28-31
    sprite('bc403_05', 4)	# 32-35
    sprite('bc403_03', 4)	# 36-39
    sprite('bc403_04', 4)	# 40-43
    sprite('bc403_05', 4)	# 44-47
    sprite('bc403_03', 4)	# 48-51
    sprite('bc403_04', 4)	# 52-55
    sprite('bc403_05', 4)	# 56-59
    sprite('bc403_03', 4)	# 60-63
    sprite('bc403_04', 4)	# 64-67
    sprite('bc403_05', 5)	# 68-72
    sprite('bc403_03', 5)	# 73-77
    sprite('bc403_04', 5)	# 78-82
    sprite('bc403_00', 5)	# 83-87
    sprite('bc000_00', 6)	# 88-93

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
        Damage(1500)
        AttackP1(70)
        Hitstop(6)
        AirHitstunAnimation(10)
        Unknown9016(1)
        AirPushbackY(6000)
        AirPushbackX(10000)
        Unknown11042(1)
        Unknown9215()
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)

        def upon_12():
            clearUponHandler(12)
            Unknown2037(1)
            sendToLabel(1)

        def upon_11():
            clearUponHandler(11)
            sendToLabel(1)
    sprite('bc432_00', 2)	# 1-2
    teleportRelativeX(40000)
    sprite('bc432_01', 2)	# 3-4
    sprite('bc432_02', 2)	# 5-6
    sprite('bc432_03', 2)	# 7-8
    Unknown1084(1)
    sprite('bc432_04', 2)	# 9-10
    sprite('bc432_05', 2)	# 11-12
    sprite('bc432_07', 2)	# 13-14
    sprite('bc432_08', 1)	# 15-15	 **attackbox here**
    SFX_3('airbackdash_m')
    Unknown3029(1)
    Unknown8007(100, 1, 1)
    physicsXImpulse(40000)
    GFX_1('bcef_432sword', 0)
    tag_voice(1, 'pbc214_0', 'pbc214_1', 'pbc214_2', '')
    sprite('bc432_08', 1)	# 16-16	 **attackbox here**
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 17-17	 **attackbox here**
    SFX_3('airbackdash_m')
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 18-18	 **attackbox here**
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 19-19	 **attackbox here**
    SFX_3('airbackdash_m')
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 20-20	 **attackbox here**
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 21-21	 **attackbox here**
    SFX_3('airbackdash_m')
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 22-22	 **attackbox here**
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 23-23	 **attackbox here**
    SFX_3('airbackdash_m')
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 2)	# 24-25	 **attackbox here**
    sprite('bc432_08', 2)	# 26-27	 **attackbox here**
    gotoLabel(10)
    label(1)
    sprite('bc432_08', 1)	# 28-28	 **attackbox here**
    Unknown23027()
    Unknown3070(2)
    Unknown3071(6)
    Unknown1019(80)
    Unknown11068(0)
    GFX_1('bcef_432sword', 0)
    sprite('bc432_08', 1)	# 29-29	 **attackbox here**
    sprite('bc432_08', 1)	# 30-30	 **attackbox here**
    GFX_1('bcef_432sword', 0)
    Unknown1019(60)
    sprite('bc432_08', 1)	# 31-31	 **attackbox here**
    Unknown1019(60)
    sprite('bc432_08', 1)	# 32-32	 **attackbox here**
    Unknown1019(0)
    sprite('bc432_10', 1)	# 33-33
    label(10)
    sprite('bc432_10', 1)	# 34-34
    Unknown1019(60)
    clearUponHandler(12)
    clearUponHandler(11)
    sprite('bc432_11', 1)	# 35-35
    sprite('bc432_12', 3)	# 36-38	 **attackbox here**
    SFX_3('cut_l')
    GFX_1('bcef_432sword', 0)
    Unknown20007(0)
    Unknown20001(0)
    Unknown3029(0)
    Unknown8004(100, 1, 0)
    Unknown1019(0)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        ScreenShake(35000, 5000)
        GFX_1('bcef_432finish', 0)
    RefreshMultihit()
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    WallbounceReboundTime(15)
    Unknown9215()
    AirPushbackX(80000)
    AirPushbackY(20000)
    Hitstop(13)
    AirUntechableTime(60)
    Unknown9266(4)
    Unknown11057(1000)
    sprite('bc432_50', 5)	# 39-43	 **attackbox here**
    Unknown23027()
    sprite('bc432_51', 5)	# 44-48	 **attackbox here**
    sprite('bc432_50', 5)	# 49-53	 **attackbox here**
    sprite('bc432_51', 5)	# 54-58	 **attackbox here**
    sprite('bc432_13', 6)	# 59-64
    sprite('bc432_14', 6)	# 65-70
    sprite('bc432_15', 7)	# 71-77
    sprite('bc432_16', 7)	# 78-84

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
    Unknown2036(101, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-290000)
    Unknown1019(4)
    label(0)
    sprite('bc020_07', 4)	# 3-6
    sprite('bc020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateBladeDDDOD')
    else:
        enterState('UltimateBladeDDD')

@State
def UltimateBladeDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        Unknown9016(1)
        AirHitstunAnimation(5)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown9266(4)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11062(1)
        Unknown2004(1, 0)
        Unknown9154(40)
        Unknown9310(1)
        Unknown30063(1)
        setInvincible(1)

        def upon_78():
            Unknown9154(100)
            SLOT_51 = 1
            Unknown23083(1)
            GFX_0('jumonjiBigslashYoko', 0)
            Unknown11069('PBC_PersonaUltimateBladeTAG')
    sprite('bc430_00', 5)	# 1-5
    Unknown2053(1)
    Unknown2034(1)
    Unknown1084(1)
    sprite('bc430_01', 5)	# 6-10
    sprite('bc430_02', 3)	# 11-13
    GFX_0('jumonjiSwordAura', 0)
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 14-16
    sprite('bc430_04', 3)	# 17-19
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 20-22
    sprite('bc430_03', 3)	# 23-25
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_04', 3)	# 26-28
    sprite('bc430_02', 3)	# 29-31
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 32-34
    sprite('bc430_04', 3)	# 35-37
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_02', 3)	# 38-40
    sprite('bc430_03', 3)	# 41-43
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 44-46
    sprite('bc430_02', 3)	# 47-49
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 50-52
    sprite('bc430_04', 3)	# 53-55
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 56-58
    sprite('bc430_03', 3)	# 59-61
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 62-64
    sprite('bc430_05', 3)	# 65-67
    Unknown13(1)
    GFX_0('jumonjiBcSlash', 100)
    sprite('bc430_06', 3)	# 68-70
    sprite('bc430_07', 3)	# 71-73
    SFX_3('cut_l')
    sprite('bc430_08', 3)	# 74-76
    sprite('bc430_10', 3)	# 77-79	 **attackbox here**
    Unknown23054('62633433305f303900000000000000000000000000000000000000000000000003000000')
    SFX_3('bc001')
    RefreshMultihit()
    sprite('bc430_10', 4)	# 80-83	 **attackbox here**
    sprite('bc430_11', 4)	# 84-87
    Unknown23027()
    setInvincible(0)
    loopRest()
    Unknown19(2, 2, 51)
    sprite('bc430_12', 4)	# 88-91
    Unknown23029(11, 940, 0)
    Unknown7007('7062633235315f300000000000000000640000007062633235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('bc430_10', 4)	# 92-95	 **attackbox here**
    sprite('bc430_11', 4)	# 96-99
    sprite('bc430_12', 4)	# 100-103
    sprite('bc430_10', 4)	# 104-107	 **attackbox here**
    sprite('bc430_11', 4)	# 108-111
    sprite('bc430_12', 4)	# 112-115
    sprite('bc430_10', 4)	# 116-119	 **attackbox here**
    sprite('bc430_11', 4)	# 120-123
    sprite('bc430_12', 4)	# 124-127
    sprite('bc430_10', 4)	# 128-131	 **attackbox here**
    sprite('bc430_11', 4)	# 132-135
    sprite('bc430_12', 4)	# 136-139
    sprite('bc430_10', 4)	# 140-143	 **attackbox here**
    sprite('bc430_11', 4)	# 144-147
    sprite('bc430_12', 4)	# 148-151
    sprite('bc430_10', 4)	# 152-155	 **attackbox here**
    sprite('bc430_11', 4)	# 156-159
    sprite('bc430_12', 4)	# 160-163
    sprite('bc430_10', 4)	# 164-167	 **attackbox here**
    sprite('bc430_11', 4)	# 168-171
    sprite('bc430_12', 4)	# 172-175
    GFX_0('bcef_432ground_thunder', -1)
    sprite('bc430_10', 4)	# 176-179	 **attackbox here**
    sprite('bc430_11', 4)	# 180-183
    sprite('bc430_12', 4)	# 184-187
    sprite('bc430_10', 4)	# 188-191	 **attackbox here**
    sprite('bc430_11', 4)	# 192-195
    sprite('bc430_12', 4)	# 196-199
    sprite('bc430_10', 4)	# 200-203	 **attackbox here**
    sprite('bc430_11', 4)	# 204-207
    sprite('bc430_12', 4)	# 208-211
    label(2)
    sprite('bc430_10', 4)	# 212-215	 **attackbox here**
    sprite('bc430_13', 4)	# 216-219
    sprite('bc430_14', 4)	# 220-223
    sprite('bc430_15', 4)	# 224-227
    Unknown2001()
    sprite('bc430_16', 4)	# 228-231
    sprite('bc430_17', 4)	# 232-235
    sprite('bc430_18', 4)	# 236-239
    sprite('bc430_19', 4)	# 240-243

@State
def UltimateBladeDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        Unknown9016(1)
        AirHitstunAnimation(5)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown9266(4)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11062(1)
        Unknown9154(40)
        Unknown9310(1)
        Unknown30063(1)
        Unknown2004(1, 0)
        setInvincible(1)

        def upon_78():
            SLOT_51 = 1
            Unknown23083(1)
            Unknown9154(100)
            GFX_0('jumonjiBigslashYoko', 0)
            Unknown23029(1, 970, 0)
            Unknown11069('PBC_PersonaUltimateBladeODTAG')
    sprite('bc430_00', 5)	# 1-5
    sprite('bc430_01', 5)	# 6-10
    sprite('bc430_02', 3)	# 11-13
    GFX_0('jumonjiSwordAura', 0)
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 14-16
    sprite('bc430_04', 3)	# 17-19
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 20-22
    sprite('bc430_03', 3)	# 23-25
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_04', 3)	# 26-28
    sprite('bc430_02', 3)	# 29-31
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 32-34
    sprite('bc430_04', 3)	# 35-37
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    SFX_3('bc000')
    sprite('bc430_02', 3)	# 38-40
    sprite('bc430_03', 3)	# 41-43
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 44-46
    sprite('bc430_02', 3)	# 47-49
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_03', 3)	# 50-52
    sprite('bc430_04', 3)	# 53-55
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_02', 3)	# 56-58
    sprite('bc430_03', 3)	# 59-61
    GFX_1('izef_enagyballthunder_04', 0)
    GFX_1('izef_enagyballthunder_04', 1)
    GFX_1('izef_enagyballthunder_04', 2)
    sprite('bc430_04', 3)	# 62-64
    sprite('bc430_05', 3)	# 65-67
    Unknown13(1)
    GFX_0('jumonjiBcSlash', 100)
    sprite('bc430_06', 3)	# 68-70
    sprite('bc430_07', 3)	# 71-73
    SFX_3('cut_l')
    sprite('bc430_08', 3)	# 74-76
    sprite('bc430_10', 3)	# 77-79	 **attackbox here**
    Unknown23054('62633433305f303900000000000000000000000000000000000000000000000003000000')
    SFX_3('bc001')
    RefreshMultihit()
    sprite('bc430_10', 4)	# 80-83	 **attackbox here**
    sprite('bc430_11', 4)	# 84-87
    Unknown23027()
    setInvincible(0)
    loopRest()
    Unknown19(2, 2, 51)
    sprite('bc430_13', 4)	# 88-91
    sprite('bc430_14', 4)	# 92-95
    sprite('bc430_15', 4)	# 96-99
    sprite('bc430_16', 4)	# 100-103
    sprite('bc430_17', 4)	# 104-107
    sprite('bc430_18', 4)	# 108-111
    sprite('bc433_17', 8)	# 112-119
    sprite('bc433_18', 8)	# 120-127
    sprite('bc433_19', 8)	# 128-135
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(10, 1)
    Unknown36(10)
    Unknown1007(61200)
    physicsYImpulse(-1800)
    Unknown35()
    sprite('bc433_20', 4)	# 136-139
    Unknown13(10)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    Unknown2036(60, -1, 0)
    Unknown23029(11, 950, 0)
    Unknown7007('7062633235315f300000000000000000640000007062633235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('bc433_21', 4)	# 140-143
    sprite('bc433_22', 4)	# 144-147
    sprite('bc433_23', 4)	# 148-151
    sprite('bc433_21', 4)	# 152-155
    sprite('bc433_22', 4)	# 156-159
    sprite('bc433_23', 4)	# 160-163
    sprite('bc433_21', 4)	# 164-167
    sprite('bc433_22', 4)	# 168-171
    sprite('bc433_23', 4)	# 172-175
    sprite('bc433_21', 4)	# 176-179
    sprite('bc433_22', 4)	# 180-183
    sprite('bc433_23', 4)	# 184-187
    sprite('bc433_21', 4)	# 188-191
    sprite('bc433_22', 4)	# 192-195
    sprite('bc433_23', 4)	# 196-199
    sprite('bc433_21', 4)	# 200-203
    sprite('bc433_22', 4)	# 204-207
    sprite('bc433_23', 4)	# 208-211
    GFX_0('bcef_432ground_thunderOD', -1)
    sprite('bc433_21', 4)	# 212-215
    sprite('bc433_22', 4)	# 216-219
    sprite('bc433_23', 4)	# 220-223
    sprite('bc433_21', 4)	# 224-227
    sprite('bc433_22', 4)	# 228-231
    sprite('bc433_23', 4)	# 232-235
    sprite('bc433_21', 4)	# 236-239
    sprite('bc433_22', 4)	# 240-243
    sprite('bc433_23', 4)	# 244-247
    sprite('bc433_21', 4)	# 248-251
    sprite('bc433_22', 4)	# 252-255
    sprite('bc433_23', 4)	# 256-259
    sprite('bc433_21', 4)	# 260-263
    sprite('bc433_22', 4)	# 264-267
    sprite('bc433_23', 4)	# 268-271
    sprite('bc433_21', 4)	# 272-275
    sprite('bc433_22', 4)	# 276-279
    sprite('bc433_23', 4)	# 280-283
    sprite('bc433_21', 4)	# 284-287
    sprite('bc433_22', 4)	# 288-291
    sprite('bc433_23', 4)	# 292-295
    sprite('bc433_21', 4)	# 296-299
    sprite('bc433_22', 4)	# 300-303
    sprite('bc433_23', 4)	# 304-307
    sprite('bc433_21', 4)	# 308-311
    sprite('bc433_22', 4)	# 312-315
    sprite('bc433_23', 4)	# 316-319
    sprite('bc433_24', 4)	# 320-323
    sprite('bc433_25', 4)	# 324-327
    sprite('bc433_26', 4)	# 328-331
    ExitState()
    label(2)
    sprite('bc430_10', 4)	# 332-335	 **attackbox here**
    sprite('bc430_13', 4)	# 336-339
    sprite('bc430_14', 4)	# 340-343
    sprite('bc430_15', 4)	# 344-347
    Unknown2001()
    sprite('bc430_16', 4)	# 348-351
    sprite('bc430_17', 4)	# 352-355
    sprite('bc430_18', 4)	# 356-359
    sprite('bc430_19', 4)	# 360-363

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
    sprite('bc253_00', 3)	# 121-123
    Unknown1086(22)
    teleportRelativeX(-100000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    sprite('bc253_01', 3)	# 124-126
    sprite('bc253_02', 3)	# 127-129
    sprite('bc253_03', 3)	# 130-132
    sprite('bc253_04', 3)	# 133-135
    label(1)
    sprite('bc253_05ex00', 3)	# 136-138	 **attackbox here**
    sprite('bc253_06ex00', 3)	# 139-141	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 142-144
    Unknown1084(1)
    sprite('bc120_01', 4)	# 145-148
    Unknown8000(-1, 1, 1)
    sprite('bc120_00', 12)	# 149-160
    sprite('bc120_01', 4)	# 161-164
    sprite('bc120_02', 4)	# 165-168
    sprite('bc120_03', 4)	# 169-172

@State
def CmnActChangeReturnAppealBurst():
    sprite('bc064_02', 35)	# 1-35
    sprite('bc064_03', 5)	# 36-40
    sprite('bc010_02', 5)	# 41-45
    sprite('bc010_01', 5)	# 46-50
    sprite('bc010_00', 5)	# 51-55
    sprite('bc000_00', 30)	# 56-85

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(5000)
        Unknown11091(100)
        Unknown11034(0)
        Unknown11033(3)
        Unknown11058('0000000000000000000000000100000000000000')
        Hitstop(0)
        Unknown11001(12, 6, 6)
        Unknown11064(1)
        Unknown9266(4)
        GroundedHitstunAnimation(1)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(9999)
        Unknown9310(60)
        Unknown11056(0)

        def upon_78():
            clearUponHandler(78)
            SLOT_51 = 1
            PushbackX(0)
            Unknown13024(0)
            Unknown23084(1)
            Unknown23088(1, 1)
            Unknown23157(1)
            Unknown11067(1)
            Unknown2017(0)
            Unknown2053(0)
            Unknown2034(0)
            GFX_0('IchigekiCamera', 100)
            Unknown38(5, 1)
            SFX_3('bc001')

        def upon_STATE_END():
            Unknown20000(0)
            Unknown21007(4, 32)
            Unknown21012('506572736f6e614963686967656b69000000000000000000000000000000000020000000')
            setInvincible(0)
        Unknown2004(1, 0)
    sprite('bc000_00', 6)	# 1-6
    setInvincible(1)
    sprite('bc450_01', 4)	# 7-10
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    physicsYImpulse(-2000)
    Unknown35()
    Unknown2036(90, -1, 2)
    Unknown23147()
    GFX_0('P4U_Cutin_Parent', 100)
    sprite('bc450_02', 4)	# 11-14
    sprite('bc450_03', 4)	# 15-18
    sprite('bc450_04', 4)	# 19-22
    sprite('bc450_05', 22)	# 23-44
    sprite('bc450_05', 6)	# 45-50
    tag_voice(1, 'pbc290_0', 'pbc290_1', '', '')
    sprite('bc450_06', 6)	# 51-56
    sprite('bc450_07', 6)	# 57-62
    sprite('bc450_08', 6)	# 63-68
    sprite('bc450_09', 6)	# 69-74
    sprite('bc450_10', 6)	# 75-80
    sprite('bc450_11', 18)	# 81-98
    sprite('bc450_12', 6)	# 99-104
    sprite('bc450_13', 1)	# 105-105
    Unknown21007(4, 32)
    GFX_1('izef_cardcrash_03', 100)
    SFX_3('slash_rapier_middle')
    sprite('bc450_13', 5)	# 106-110
    SFX_3('persona_destroy')
    sprite('bc450_14', 6)	# 111-116	 **attackbox here**
    GFX_1('bcef_denkigshock_06', 0)
    sprite('bc450_15', 6)	# 117-122	 **attackbox here**
    GFX_0('IchigekiGroundDenki', 0)
    RefreshMultihit()
    SFX_3('electric_l')
    SFX_3('bc000')
    Unknown23086(1)
    sprite('bc450_16', 6)	# 123-128	 **attackbox here**
    SFX_3('bc000')
    sprite('bc450_17', 6)	# 129-134	 **attackbox here**
    SFX_3('electric_l')
    sprite('bc450_17', 6)	# 135-140	 **attackbox here**
    SFX_3('bc000')
    sprite('bc450_17', 8)	# 141-148	 **attackbox here**
    SFX_3('electric_l')
    Unknown23027()
    loopRest()
    if SLOT_51:
        _gotolabel(2)
    label(0)
    sprite('bc450_17', 20)	# 149-168	 **attackbox here**
    Unknown23027()
    clearUponHandler(78)
    setInvincible(0)
    sprite('bc450_18', 6)	# 169-174
    sprite('bc450_19', 6)	# 175-180
    sprite('bc450_20', 6)	# 181-186
    sprite('bc000_00', 6)	# 187-192
    loopRest()
    ExitState()
    label(2)
    sprite('bc450_17', 14)	# 193-206	 **attackbox here**
    sprite('bc450_17', 15)	# 207-221	 **attackbox here**
    Unknown20000(0)
    Unknown4004('534345465f536861736861496e0000000000000000000000000000000000000064000000')
    Unknown23029(11, 960, 0)
    Unknown21007(5, 33)
    sprite('bc450_17', 15)	# 222-236	 **attackbox here**
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    Unknown23024(3)
    sprite('bc450_17', 40)	# 237-276	 **attackbox here**
    Unknown21007(5, 34)
    tag_voice(0, 'pbc291_0', 'pbc291_1', '', '')
    sprite('bc450_17', 10)	# 277-286	 **attackbox here**
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown4004('534345465f5368617368614f757400000000000000000000000000000000000064000000')
    Unknown26('SCEF_ShashaIn')
    sprite('bc450_17', 20)	# 287-306	 **attackbox here**
    Unknown26('SCEF_FadeBlack12In')
    Unknown21012('506572736f6e614963686967656b69000000000000000000000000000000000021000000')
    sendToLabelUpon(33, 3)
    sprite('keep', 32767)	# 307-33073
    label(3)
    sprite('bc450_17', 40)	# 33074-33113	 **attackbox here**
    Unknown36(22)
    Unknown23119(-1, 500, 1)
    Unknown35()
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    clearUponHandler(33)
    Unknown36(22)
    Unknown1000(0)
    Unknown35()
    Unknown21007(5, 36)
    sprite('bc450_17', 10)	# 33114-33123	 **attackbox here**
    Unknown26('SCEF_ShashaIn')
    Unknown4004('534345465f5368617368614f757400000000000000000000000000000000000064000000')
    sprite('bc450_17', 30)	# 33124-33153	 **attackbox here**
    Unknown26('SCEF_FadeBlack12In')
    sprite('bc450_17', 6)	# 33154-33159	 **attackbox here**
    Unknown48('190000000200000033000000050000000200000016000000')
    Unknown48('190000000200000034000000050000000200000017000000')
    Unknown36(5)
    physicsYImpulse(-240000)
    Unknown35()
    sprite('bc450_17', 100)	# 33160-33259	 **attackbox here**
    GFX_0('IchigekiBeamJizoku', 100)
    Unknown38(4, 1)
    Unknown48('040000000200000016000000190000000200000033000000')
    Unknown48('040000000200000017000000190000000200000034000000')
    Unknown36(4)
    Unknown1007(800000)
    physicsYImpulse(-240000)
    Unknown35()
    sprite('bc450_17', 10)	# 33260-33269	 **attackbox here**
    Unknown48('190000000200000033000000050000000200000016000000')
    Unknown48('190000000200000034000000050000000200000017000000')
    Unknown48('160000000200000016000000190000000200000033000000')
    Unknown48('160000000200000017000000190000000200000034000000')
    Unknown36(22)
    Unknown1007(-2600000)
    Unknown35()
    sprite('bc450_17', 1)	# 33270-33270	 **attackbox here**
    Unknown36(5)
    Unknown1084(1)
    Unknown35()
    sprite('bc450_17', 5)	# 33271-33275	 **attackbox here**
    GFX_0('IchigekiShake', 100)
    SFX_3('counter_hit_l45')
    SFX_3('blaze_long')
    Unknown21012('4963686967656b694265616d4a697a6f6b75000000000000000000000000000021000000')
    sprite('bc450_17', 5)	# 33276-33280	 **attackbox here**
    SFX_3('thunder_l')
    SFX_3('blaze_long')
    SFX_3('damage_ichigeki_hit')
    SFX_3('bomb_l')
    sprite('bc450_17', 5)	# 33281-33285	 **attackbox here**
    SFX_3('thunder_l')
    SFX_3('blaze_long')
    SFX_3('damage_ichigeki_hit')
    SFX_3('bomb_l')
    sprite('bc450_17', 30)	# 33286-33315	 **attackbox here**
    SFX_3('thunder_l')
    SFX_3('blaze_long')
    SFX_3('damage_ichigeki_hit')
    SFX_3('bomb_l')
    Unknown36(4)
    physicsYImpulse(0)
    Unknown35()
    GFX_0('IchigekiFinish_Effect', 100)
    sprite('bc450_17', 60)	# 33316-33375	 **attackbox here**
    sprite('bc450_17', 1)	# 33376-33376	 **attackbox here**
    Unknown21007(4, 32)
    AttackLevel_(5)
    Damage(32000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(0)
    YImpluseBeforeWallbounce(0)
    Unknown11064(3)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    RefreshMultihit()
    Unknown30057('')
    Unknown4004('534345465f55737567757261690000000000000000000000000000000000000064000000')
    sprite('bc000_00', 100)	# 33377-33476
    label(4)
    sprite('bc000_00', 5)	# 33477-33481
    Unknown1000(0)
    Unknown23024(0)
    Unknown21007(5, 37)
    Unknown23029(11, 1100, 0)
    SLOT_59 = 1
    sendToLabelUpon(34, 6)
    label(5)
    sprite('bc000_00', 6)	# 33482-33487
    sprite('bc000_01', 6)	# 33488-33493
    sprite('bc000_02', 6)	# 33494-33499
    sprite('bc000_03', 6)	# 33500-33505
    sprite('bc000_04', 6)	# 33506-33511
    sprite('bc000_05', 6)	# 33512-33517
    sprite('bc000_06', 6)	# 33518-33523
    sprite('bc000_07', 6)	# 33524-33529
    sprite('bc000_08', 6)	# 33530-33535
    sprite('bc000_09', 6)	# 33536-33541
    loopRest()
    gotoLabel(5)
    label(6)
    sprite('keep', 1)	# 33542-33542

@Subroutine
def MouthTableInit():
    Unknown18011('pbc000', 12897, 25392, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc293_0', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc293_1', 12643, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc500', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13667, 24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc501', 12643, 13921, 13923, 13921, 13411, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc502', 12643, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc503', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc504', 12643, 13921, 25392, 12342, 13921, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc505', 12643, 13921, 25392, 12342, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc506', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc507', 12643, 13921, 13923, 13921, 13923, 13921, 13667, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc520', 14691, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc521', 12643, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc522', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc523', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc524', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc525', 12643, 13921, 13923, 13921, 13923, 13921, 13667, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc402_0', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc402_1', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc403_0', 14691, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc403_1', 14691, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc600bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc600brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc600pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc600pce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc600pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc600pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc600ugo', 12643, 12641, 25396, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601bes', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601pka', 12643, 12641, 25396, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601pna', 12643, 12641, 25396, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601pyo', 12643, 12641, 25396, 14134, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601uhy', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12344, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc601uyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc602brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc604brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc606brg', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc700bha', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc700pce', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc700pna', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc700rrb', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701bes', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701brg', 12643, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701pka', 12643, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701pla', 12643, 13921, 13923, 13921, 13923, 14177, 13155, 24887, 25399, 24887, 25399, 14133, 13921, 13923, 13921, 13923, 13921, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701pyo', 12643, 14177, 14435, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701pyu', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701rwi', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701ugo', 12643, 12641, 25396, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701uhy', 12643, 12641, 25396, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pbc701uyu', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12853, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('brg')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('pna')
    if SLOT_0:
        _gotolabel(200)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(210)
    PartnerChar('pag')
    if SLOT_0:
        _gotolabel(220)
    PartnerChar('uyu')
    if SLOT_0:
        _gotolabel(230)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(240)
    PartnerChar('biz')
    if SLOT_0:
        _gotolabel(250)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('bc600_00', 6)	# 2-7
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 8-13
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 14-19
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_00', 6)	# 20-25
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 26-31
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 32-37
    GFX_1('bcef_entry_00', 0)
    sprite('bc204_02', 4)	# 38-41
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_03', 4)	# 42-45
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_04', 4)	# 46-49
    Unknown23029(11, 1000, 0)
    sprite('bc204_05', 4)	# 50-53
    Unknown7006('pbc500', 100, 895705712, 12592, 0, 0, 100, 895705712, 12848, 0, 0, 100, 895705712, 14128, 0, 0, 100)
    label(1)
    sprite('bc204_03', 4)	# 54-57
    sprite('bc204_04', 4)	# 58-61
    sprite('bc204_05', 4)	# 62-65
    if SLOT_97:
        _gotolabel(1)
    sprite('bc204_00', 4)	# 66-69
    Unknown23018(1)
    sprite('bc000_00', 6)	# 70-75
    sprite('bc000_01', 6)	# 76-81
    sprite('bc000_02', 6)	# 82-87
    sprite('bc000_03', 6)	# 88-93
    sprite('bc000_04', 6)	# 94-99
    Unknown21007(24, 41)
    sprite('bc000_05', 6)	# 100-105
    sprite('bc000_06', 6)	# 106-111
    sprite('bc000_07', 6)	# 112-117
    sprite('bc000_08', 6)	# 118-123
    sprite('bc000_09', 6)	# 124-129
    loopRest()
    ExitState()
    label(10)
    sprite('bc601_00', 6)	# 130-135
    Unknown7006('pbc503', 100, 895705712, 13360, 0, 0, 100, 895705712, 13616, 0, 0, 100, 895705712, 13872, 0, 0, 100)
    sprite('bc601_01', 6)	# 136-141
    sprite('bc601_02', 6)	# 142-147
    sprite('bc601_00', 6)	# 148-153
    sprite('bc601_01', 6)	# 154-159
    sprite('bc601_02', 6)	# 160-165
    sprite('bc601_00', 6)	# 166-171
    sprite('bc601_01', 6)	# 172-177
    sprite('bc601_02', 6)	# 178-183
    sprite('bc601_00', 6)	# 184-189
    sprite('bc601_01', 6)	# 190-195
    sprite('bc601_02', 6)	# 196-201
    sprite('bc601_00', 6)	# 202-207
    sprite('bc601_01', 6)	# 208-213
    sprite('bc601_02', 6)	# 214-219
    sprite('bc601_00', 6)	# 220-225
    sprite('bc601_01', 6)	# 226-231
    sprite('bc601_02', 6)	# 232-237
    sprite('bc601_03', 6)	# 238-243
    sprite('bc601_04', 6)	# 244-249
    sprite('bc601_05', 6)	# 250-255
    sprite('bc601_06', 6)	# 256-261
    sprite('bc601_07', 6)	# 262-267
    Unknown21007(24, 41)
    sprite('bc601_08', 6)	# 268-273
    SFX_3('slash_knife_slow')
    SFX_3('guard_slash_s')
    sprite('bc601_09', 6)	# 274-279
    GFX_1('bcef_entry2_02', 0)
    sprite('bc601_10', 6)	# 280-285
    sprite('bc601_11', 6)	# 286-291
    sprite('bc601_12', 6)	# 292-297
    sprite('bc601_13', 6)	# 298-303
    sprite('bc601_14', 6)	# 304-309
    sprite('bc601_15', 6)	# 310-315
    sprite('bc601_16', 6)	# 316-321
    SFX_3('slash_rapier_fast')
    GFX_0('Entry2', 0)
    sprite('bc601_17', 6)	# 322-327
    Unknown21011(60)
    sprite('bc601_18', 6)	# 328-333
    ExitState()
    label(20)
    sprite('bc000_00', 1)	# 334-334
    SFX_1('pbc701uyu')
    label(21)
    sprite('bc000_00', 6)	# 335-340
    sprite('bc000_01', 6)	# 341-346
    sprite('bc000_02', 6)	# 347-352
    sprite('bc000_03', 6)	# 353-358
    sprite('bc000_04', 6)	# 359-364
    sprite('bc000_05', 6)	# 365-370
    sprite('bc000_06', 6)	# 371-376
    sprite('bc000_07', 6)	# 377-382
    sprite('bc000_08', 6)	# 383-388
    sprite('bc000_09', 6)	# 389-394
    gotoLabel(21)
    label(100)
    sprite('bc600_00', 6)	# 395-400
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 401-406
    SFX_1('pbc600brg')
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 407-412
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_00', 6)	# 413-418
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 419-424
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 425-430
    GFX_1('bcef_entry_00', 0)
    sprite('bc204_02', 4)	# 431-434
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_03', 4)	# 435-438
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_04', 4)	# 439-442
    Unknown23029(11, 1000, 0)
    sprite('bc204_05', 4)	# 443-446
    label(101)
    sprite('bc204_03', 4)	# 447-450
    sprite('bc204_04', 4)	# 451-454
    sprite('bc204_05', 4)	# 455-458
    if SLOT_97:
        _gotolabel(101)
    sprite('bc204_03', 4)	# 459-462
    sprite('bc204_04', 4)	# 463-466
    sprite('bc204_05', 4)	# 467-470
    sprite('bc204_03', 4)	# 471-474
    sprite('bc204_04', 4)	# 475-478
    sprite('bc204_05', 4)	# 479-482
    sprite('bc204_00', 4)	# 483-486
    Unknown21007(24, 40)
    sprite('bc000_00', 1)	# 487-487

    def upon_39():
        clearUponHandler(39)
        sendToLabel(103)
    label(102)
    sprite('bc000_00', 6)	# 488-493
    sprite('bc000_01', 6)	# 494-499
    sprite('bc000_02', 6)	# 500-505
    sprite('bc000_03', 6)	# 506-511
    sprite('bc000_04', 6)	# 512-517
    sprite('bc000_05', 6)	# 518-523
    sprite('bc000_06', 6)	# 524-529
    sprite('bc000_07', 6)	# 530-535
    sprite('bc000_08', 6)	# 536-541
    sprite('bc000_09', 6)	# 542-547
    gotoLabel(102)
    label(103)
    sprite('bc001_00', 7)	# 548-554

    def upon_38():
        clearUponHandler(38)
        sendToLabel(106)
    sprite('bc001_01', 7)	# 555-561
    SFX_1('pbc602brg')
    sprite('bc001_02', 7)	# 562-568
    sprite('bc001_03', 7)	# 569-575
    sprite('bc001_04', 7)	# 576-582
    sprite('bc001_05', 7)	# 583-589
    sprite('bc001_06', 7)	# 590-596
    label(104)
    sprite('bc001_01', 1)	# 597-597
    if SLOT_97:
        _gotolabel(104)
    sprite('bc001_01', 30)	# 598-627
    sprite('bc001_00', 7)	# 628-634
    Unknown21007(24, 39)
    label(105)
    sprite('bc000_00', 6)	# 635-640
    sprite('bc000_01', 6)	# 641-646
    sprite('bc000_02', 6)	# 647-652
    sprite('bc000_03', 6)	# 653-658
    sprite('bc000_04', 6)	# 659-664
    sprite('bc000_05', 6)	# 665-670
    sprite('bc000_06', 6)	# 671-676
    sprite('bc000_07', 6)	# 677-682
    sprite('bc000_08', 6)	# 683-688
    sprite('bc000_09', 6)	# 689-694
    gotoLabel(105)
    label(106)
    sprite('bc204_00', 6)	# 695-700
    SFX_1('pbc604brg')
    sprite('bc204_01', 6)	# 701-706
    sprite('bc204_02', 6)	# 707-712
    Unknown2037(5)
    label(107)
    sprite('bc204_03', 6)	# 713-718
    sprite('bc204_04', 6)	# 719-724
    sprite('bc204_05', 6)	# 725-730
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(107)
    sprite('bc204_03', 6)	# 731-736
    Unknown21007(24, 38)
    sprite('bc204_04', 6)	# 737-742
    sprite('bc204_05', 6)	# 743-748
    sprite('bc204_03', 6)	# 749-754
    sprite('bc204_04', 6)	# 755-760
    sprite('bc204_05', 6)	# 761-766
    sprite('bc205_00', 6)	# 767-772
    sprite('bc205_01', 6)	# 773-778
    sprite('bc205_02', 6)	# 779-784
    sprite('bc205_03', 6)	# 785-790
    SFX_1('pbc606brg')
    sprite('bc205_04', 6)	# 791-796
    sprite('bc205_05', 6)	# 797-802
    sprite('bc205_06', 6)	# 803-808
    sprite('bc205_04', 6)	# 809-814
    sprite('bc205_05', 6)	# 815-820
    sprite('bc205_06', 6)	# 821-826
    Unknown23018(1)
    label(108)
    sprite('bc205_04', 6)	# 827-832
    sprite('bc205_05', 6)	# 833-838
    sprite('bc205_06', 6)	# 839-844
    gotoLabel(108)
    ExitState()
    label(110)
    sprite('bc600_00', 6)	# 845-850
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 851-856
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 857-862
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_00', 6)	# 863-868
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 869-874
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 875-880
    GFX_1('bcef_entry_00', 0)
    sprite('bc204_02', 4)	# 881-884
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_03', 4)	# 885-888
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_04', 4)	# 889-892
    Unknown23029(11, 1000, 0)
    sprite('bc204_05', 4)	# 893-896
    SFX_1('pbc600bha')
    label(111)
    sprite('bc204_03', 4)	# 897-900
    sprite('bc204_04', 4)	# 901-904
    sprite('bc204_05', 4)	# 905-908
    if SLOT_97:
        _gotolabel(111)
    sprite('bc204_03', 4)	# 909-912
    sprite('bc204_04', 4)	# 913-916
    sprite('bc204_05', 4)	# 917-920
    sprite('bc204_03', 4)	# 921-924
    sprite('bc204_04', 4)	# 925-928
    sprite('bc204_05', 4)	# 929-932
    sprite('bc204_03', 4)	# 933-936
    sprite('bc204_04', 4)	# 937-940
    sprite('bc204_05', 4)	# 941-944
    sprite('bc000_00', 1)	# 945-945
    Unknown21007(24, 40)
    Unknown21011(360)
    label(112)
    sprite('bc000_00', 6)	# 946-951
    sprite('bc000_01', 6)	# 952-957
    sprite('bc000_02', 6)	# 958-963
    sprite('bc000_03', 6)	# 964-969
    sprite('bc000_04', 6)	# 970-975
    sprite('bc000_05', 6)	# 976-981
    sprite('bc000_06', 6)	# 982-987
    sprite('bc000_07', 6)	# 988-993
    sprite('bc000_08', 6)	# 994-999
    sprite('bc000_09', 6)	# 1000-1005
    gotoLabel(112)
    ExitState()
    label(120)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('bc601_00', 1)	# 1006-1006

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
        SFX_1('pbc601bes')
    label(121)
    sprite('bc601_00', 6)	# 1007-1012
    sprite('bc601_01', 6)	# 1013-1018
    sprite('bc601_02', 6)	# 1019-1024
    gotoLabel(121)
    label(122)
    sprite('bc601_00', 6)	# 1025-1030
    sprite('bc601_01', 6)	# 1031-1036
    sprite('bc601_02', 6)	# 1037-1042
    if SLOT_97:
        _gotolabel(122)
    sprite('bc601_03', 6)	# 1043-1048
    sprite('bc601_04', 6)	# 1049-1054
    sprite('bc601_05', 6)	# 1055-1060
    sprite('bc601_06', 6)	# 1061-1066
    sprite('bc601_07', 6)	# 1067-1072
    sprite('bc601_08', 6)	# 1073-1078
    SFX_3('slash_knife_slow')
    SFX_3('guard_slash_s')
    sprite('bc601_09', 6)	# 1079-1084
    GFX_1('bcef_entry2_02', 0)
    sprite('bc601_10', 6)	# 1085-1090
    sprite('bc601_11', 6)	# 1091-1096
    sprite('bc601_12', 6)	# 1097-1102
    sprite('bc601_13', 6)	# 1103-1108
    sprite('bc601_14', 6)	# 1109-1114
    sprite('bc601_15', 6)	# 1115-1120
    sprite('bc601_16', 6)	# 1121-1126
    SFX_3('slash_rapier_fast')
    GFX_0('Entry2', 0)
    sprite('bc601_17', 6)	# 1127-1132
    sprite('bc601_18', 6)	# 1133-1138
    Unknown21011(90)
    label(123)
    sprite('bc000_00', 6)	# 1139-1144
    sprite('bc000_01', 6)	# 1145-1150
    sprite('bc000_02', 6)	# 1151-1156
    sprite('bc000_03', 6)	# 1157-1162
    sprite('bc000_04', 6)	# 1163-1168
    sprite('bc000_05', 6)	# 1169-1174
    sprite('bc000_06', 6)	# 1175-1180
    sprite('bc000_07', 6)	# 1181-1186
    sprite('bc000_08', 6)	# 1187-1192
    sprite('bc000_09', 6)	# 1193-1198
    gotoLabel(123)
    ExitState()
    label(130)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('bc600_00', 6)	# 1199-1204
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 1205-1210
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 1211-1216
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_00', 6)	# 1217-1222
    GFX_0('Entry', 0)
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_01', 6)	# 1223-1228
    GFX_1('bcef_entry_00', 0)
    sprite('bc600_02', 6)	# 1229-1234
    GFX_1('bcef_entry_00', 0)
    sprite('bc204_02', 4)	# 1235-1238
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_03', 4)	# 1239-1242
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_04', 4)	# 1243-1246
    Unknown23029(11, 1000, 0)
    sprite('bc204_05', 4)	# 1247-1250
    SFX_1('pbc600pce')
    label(131)
    sprite('bc204_03', 4)	# 1251-1254
    sprite('bc204_04', 4)	# 1255-1258
    sprite('bc204_05', 4)	# 1259-1262
    if SLOT_97:
        _gotolabel(131)
    sprite('bc204_03', 4)	# 1263-1266
    sprite('bc204_04', 4)	# 1267-1270
    sprite('bc204_05', 4)	# 1271-1274
    sprite('bc204_03', 4)	# 1275-1278
    sprite('bc204_04', 4)	# 1279-1282
    sprite('bc204_05', 4)	# 1283-1286
    sprite('bc204_00', 4)	# 1287-1290
    Unknown21007(24, 40)
    Unknown21011(120)
    label(132)
    sprite('bc000_00', 6)	# 1291-1296
    sprite('bc000_01', 6)	# 1297-1302
    sprite('bc000_02', 6)	# 1303-1308
    sprite('bc000_03', 6)	# 1309-1314
    sprite('bc000_04', 6)	# 1315-1320
    sprite('bc000_05', 6)	# 1321-1326
    sprite('bc000_06', 6)	# 1327-1332
    sprite('bc000_07', 6)	# 1333-1338
    sprite('bc000_08', 6)	# 1339-1344
    sprite('bc000_09', 6)	# 1345-1350
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('bc601_00', 6)	# 1351-1356
    if (not SLOT_158):
        Unknown1000(-1230000)
    sprite('bc601_01', 6)	# 1357-1362
    sprite('bc601_02', 6)	# 1363-1368
    sprite('bc601_00', 6)	# 1369-1374
    sprite('bc601_01', 6)	# 1375-1380
    sprite('bc601_02', 6)	# 1381-1386
    sprite('bc601_00', 6)	# 1387-1392
    sprite('bc601_01', 6)	# 1393-1398
    sprite('bc601_02', 6)	# 1399-1404
    sprite('bc601_00', 6)	# 1405-1410
    sprite('bc601_01', 6)	# 1411-1416
    sprite('bc601_02', 6)	# 1417-1422
    SFX_1('pbc600pyu')
    sprite('bc601_00', 6)	# 1423-1428
    sprite('bc601_01', 6)	# 1429-1434
    sprite('bc601_02', 6)	# 1435-1440
    sprite('bc601_00', 6)	# 1441-1446
    sprite('bc601_01', 6)	# 1447-1452
    sprite('bc601_02', 6)	# 1453-1458
    sprite('bc601_03', 6)	# 1459-1464
    sprite('bc601_04', 6)	# 1465-1470
    sprite('bc601_05', 6)	# 1471-1476
    sprite('bc601_06', 6)	# 1477-1482
    sprite('bc601_07', 6)	# 1483-1488
    sprite('bc601_08', 6)	# 1489-1494
    SFX_3('slash_knife_slow')
    SFX_3('guard_slash_s')
    sprite('bc601_09', 6)	# 1495-1500
    GFX_1('bcef_entry2_02', 0)
    sprite('bc601_10', 6)	# 1501-1506
    sprite('bc601_11', 6)	# 1507-1512
    Unknown21007(24, 40)
    sprite('bc601_12', 6)	# 1513-1518
    sprite('bc601_13', 6)	# 1519-1524
    sprite('bc601_14', 6)	# 1525-1530
    sprite('bc601_15', 6)	# 1531-1536
    sprite('bc601_16', 6)	# 1537-1542
    SFX_3('slash_rapier_fast')
    GFX_0('Entry2', 0)
    sprite('bc601_17', 6)	# 1543-1548
    sprite('bc601_18', 6)	# 1549-1554
    Unknown21011(120)
    label(141)
    sprite('bc000_00', 6)	# 1555-1560
    sprite('bc000_01', 6)	# 1561-1566
    sprite('bc000_02', 6)	# 1567-1572
    sprite('bc000_03', 6)	# 1573-1578
    sprite('bc000_04', 6)	# 1579-1584
    sprite('bc000_05', 6)	# 1585-1590
    sprite('bc000_06', 6)	# 1591-1596
    sprite('bc000_07', 6)	# 1597-1602
    sprite('bc000_08', 6)	# 1603-1608
    sprite('bc000_09', 6)	# 1609-1614
    gotoLabel(141)
    ExitState()
    label(150)
    sprite('bc000_00', 1)	# 1615-1615
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('bc000_00', 6)	# 1616-1621
    sprite('bc000_01', 6)	# 1622-1627
    sprite('bc000_02', 6)	# 1628-1633
    sprite('bc000_03', 6)	# 1634-1639
    sprite('bc000_04', 6)	# 1640-1645
    sprite('bc000_05', 6)	# 1646-1651
    sprite('bc000_06', 6)	# 1652-1657
    sprite('bc000_07', 6)	# 1658-1663
    sprite('bc000_08', 6)	# 1664-1669
    sprite('bc000_09', 6)	# 1670-1675
    gotoLabel(151)
    label(152)
    sprite('bc001_00', 7)	# 1676-1682
    SFX_1('pbc601uhy')
    sprite('bc001_01', 7)	# 1683-1689
    sprite('bc001_02', 7)	# 1690-1696
    sprite('bc001_03', 7)	# 1697-1703
    sprite('bc001_04', 7)	# 1704-1710
    sprite('bc001_05', 7)	# 1711-1717
    sprite('bc001_06', 7)	# 1718-1724
    sprite('bc001_01', 100)	# 1725-1824
    sprite('bc001_00', 7)	# 1825-1831
    sprite('bc000_00', 6)	# 1832-1837
    sprite('bc000_01', 6)	# 1838-1843
    sprite('bc000_02', 6)	# 1844-1849
    sprite('bc000_03', 6)	# 1850-1855
    sprite('bc204_00', 4)	# 1856-1859
    sprite('bc204_01', 4)	# 1860-1863
    sprite('bc204_02', 4)	# 1864-1867
    sprite('bc204_03', 4)	# 1868-1871
    sprite('bc204_04', 4)	# 1872-1875
    sprite('bc204_05', 4)	# 1876-1879
    sprite('bc204_03', 4)	# 1880-1883
    sprite('bc204_04', 4)	# 1884-1887
    sprite('bc204_05', 4)	# 1888-1891
    sprite('bc204_03', 4)	# 1892-1895
    sprite('bc204_04', 4)	# 1896-1899
    sprite('bc204_05', 4)	# 1900-1903
    sprite('bc204_03', 4)	# 1904-1907
    sprite('bc204_04', 4)	# 1908-1911
    sprite('bc204_05', 4)	# 1912-1915
    sprite('bc204_03', 4)	# 1916-1919
    sprite('bc204_04', 4)	# 1920-1923
    sprite('bc204_05', 4)	# 1924-1927
    sprite('bc204_03', 4)	# 1928-1931
    sprite('bc204_04', 4)	# 1932-1935
    sprite('bc204_05', 4)	# 1936-1939
    sprite('bc204_03', 4)	# 1940-1943
    sprite('bc204_04', 4)	# 1944-1947
    Unknown23029(11, 1000, 0)
    sprite('bc204_05', 4)	# 1948-1951
    label(153)
    sprite('bc204_03', 4)	# 1952-1955
    sprite('bc204_04', 4)	# 1956-1959
    sprite('bc204_05', 4)	# 1960-1963
    if SLOT_97:
        _gotolabel(153)
    sprite('bc204_03', 4)	# 1964-1967
    sprite('bc204_04', 4)	# 1968-1971
    sprite('bc204_05', 4)	# 1972-1975
    sprite('bc204_03', 4)	# 1976-1979
    sprite('bc204_04', 4)	# 1980-1983
    sprite('bc204_05', 4)	# 1984-1987
    sprite('bc204_00', 4)	# 1988-1991
    Unknown23018(1)
    label(154)
    sprite('bc000_00', 6)	# 1992-1997
    sprite('bc000_01', 6)	# 1998-2003
    sprite('bc000_02', 6)	# 2004-2009
    sprite('bc000_03', 6)	# 2010-2015
    sprite('bc000_04', 6)	# 2016-2021
    sprite('bc000_05', 6)	# 2022-2027
    sprite('bc000_06', 6)	# 2028-2033
    sprite('bc000_07', 6)	# 2034-2039
    sprite('bc000_08', 6)	# 2040-2045
    sprite('bc000_09', 6)	# 2046-2051
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('bc001_00', 7)	# 2052-2058
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1485000)
    sprite('bc001_01', 7)	# 2059-2065
    SFX_1('pbc600ugo')
    sprite('bc001_02', 7)	# 2066-2072
    sprite('bc001_03', 7)	# 2073-2079
    sprite('bc001_04', 7)	# 2080-2086
    sprite('bc001_05', 7)	# 2087-2093
    sprite('bc001_06', 7)	# 2094-2100
    label(161)
    sprite('bc001_01', 1)	# 2101-2101
    if SLOT_97:
        _gotolabel(161)
    sprite('bc001_01', 30)	# 2102-2131
    sprite('bc001_00', 7)	# 2132-2138
    Unknown21007(24, 40)
    Unknown21011(120)
    label(162)
    sprite('bc000_00', 6)	# 2139-2144
    sprite('bc000_01', 6)	# 2145-2150
    sprite('bc000_02', 6)	# 2151-2156
    sprite('bc000_03', 6)	# 2157-2162
    sprite('bc000_04', 6)	# 2163-2168
    sprite('bc000_05', 6)	# 2169-2174
    sprite('bc000_06', 6)	# 2175-2180
    sprite('bc000_07', 6)	# 2181-2186
    sprite('bc000_08', 6)	# 2187-2192
    sprite('bc000_09', 6)	# 2193-2198
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('bc601_00', 1)	# 2199-2199
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
        SFX_1('pbc601rrb')
    label(171)
    sprite('bc601_00', 6)	# 2200-2205
    sprite('bc601_01', 6)	# 2206-2211
    sprite('bc601_02', 6)	# 2212-2217
    gotoLabel(171)
    label(172)
    sprite('bc601_00', 6)	# 2218-2223
    sprite('bc601_01', 6)	# 2224-2229
    sprite('bc601_02', 6)	# 2230-2235
    sprite('bc601_03', 6)	# 2236-2241
    sprite('bc601_04', 6)	# 2242-2247
    sprite('bc601_05', 6)	# 2248-2253
    sprite('bc601_06', 6)	# 2254-2259
    sprite('bc601_07', 6)	# 2260-2265
    sprite('bc601_08', 6)	# 2266-2271
    SFX_3('slash_knife_slow')
    SFX_3('guard_slash_s')
    sprite('bc601_09', 6)	# 2272-2277
    GFX_1('bcef_entry2_02', 0)
    sprite('bc601_10', 6)	# 2278-2283
    sprite('bc601_11', 6)	# 2284-2289
    sprite('bc601_12', 6)	# 2290-2295
    sprite('bc601_13', 6)	# 2296-2301
    sprite('bc601_14', 6)	# 2302-2307
    sprite('bc601_15', 6)	# 2308-2313
    sprite('bc601_16', 6)	# 2314-2319
    SFX_3('slash_rapier_fast')
    GFX_0('Entry2', 0)
    sprite('bc601_17', 6)	# 2320-2325
    sprite('bc601_18', 6)	# 2326-2331
    Unknown23018(1)
    label(173)
    sprite('bc000_00', 6)	# 2332-2337
    sprite('bc000_01', 6)	# 2338-2343
    sprite('bc000_02', 6)	# 2344-2349
    sprite('bc000_03', 6)	# 2350-2355
    sprite('bc000_04', 6)	# 2356-2361
    sprite('bc000_05', 6)	# 2362-2367
    sprite('bc000_06', 6)	# 2368-2373
    sprite('bc000_07', 6)	# 2374-2379
    sprite('bc000_08', 6)	# 2380-2385
    sprite('bc000_09', 6)	# 2386-2391
    gotoLabel(173)
    ExitState()
    label(180)
    sprite('bc601_00', 1)	# 2392-2392
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
        SFX_1('pbc601rwi')
    label(181)
    sprite('bc601_00', 6)	# 2393-2398
    sprite('bc601_01', 6)	# 2399-2404
    sprite('bc601_02', 6)	# 2405-2410
    gotoLabel(181)
    label(182)
    sprite('bc601_00', 6)	# 2411-2416
    sprite('bc601_01', 6)	# 2417-2422
    sprite('bc601_02', 6)	# 2423-2428
    if SLOT_97:
        _gotolabel(182)
    sprite('bc601_03', 6)	# 2429-2434
    sprite('bc601_04', 6)	# 2435-2440
    sprite('bc601_05', 6)	# 2441-2446
    sprite('bc601_06', 6)	# 2447-2452
    sprite('bc601_07', 6)	# 2453-2458
    sprite('bc601_08', 6)	# 2459-2464
    SFX_3('slash_knife_slow')
    SFX_3('guard_slash_s')
    sprite('bc601_09', 6)	# 2465-2470
    GFX_1('bcef_entry2_02', 0)
    sprite('bc601_10', 6)	# 2471-2476
    sprite('bc601_11', 6)	# 2477-2482
    sprite('bc601_12', 6)	# 2483-2488
    sprite('bc601_13', 6)	# 2489-2494
    sprite('bc601_14', 6)	# 2495-2500
    sprite('bc601_15', 6)	# 2501-2506
    sprite('bc601_16', 6)	# 2507-2512
    SFX_3('slash_rapier_fast')
    GFX_0('Entry2', 0)
    sprite('bc601_17', 6)	# 2513-2518
    sprite('bc601_18', 6)	# 2519-2524
    Unknown21011(120)
    label(183)
    sprite('bc000_00', 6)	# 2525-2530
    sprite('bc000_01', 6)	# 2531-2536
    sprite('bc000_02', 6)	# 2537-2542
    sprite('bc000_03', 6)	# 2543-2548
    sprite('bc000_04', 6)	# 2549-2554
    sprite('bc000_05', 6)	# 2555-2560
    sprite('bc000_06', 6)	# 2561-2566
    sprite('bc000_07', 6)	# 2567-2572
    sprite('bc000_08', 6)	# 2573-2578
    sprite('bc000_09', 6)	# 2579-2584
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('bc635_00', 32767)	# 2585-35351
    Unknown2019(100)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(191)
    label(191)
    sprite('bc635_00', 15)	# 35352-35366
    sprite('bc635_00', 35)	# 35367-35401
    SFX_1('pbc601pyo')
    sprite('bc635_01', 6)	# 35402-35407
    sprite('bc635_02', 6)	# 35408-35413
    sprite('bc635_03', 6)	# 35414-35419
    sprite('bc635_04', 30)	# 35420-35449
    sprite('bc635_05', 6)	# 35450-35455
    sprite('bc635_06', 6)	# 35456-35461
    SFX_3('slap_fast')
    sprite('bc635_07', 6)	# 35462-35467
    Unknown21011(120)
    sprite('bc635_08', 32767)	# 35468-68234
    ExitState()
    label(200)
    sprite('bc000_00', 1)	# 68235-68235
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('bc000_00', 6)	# 68236-68241
    sprite('bc000_01', 6)	# 68242-68247
    sprite('bc000_02', 6)	# 68248-68253
    sprite('bc000_03', 6)	# 68254-68259
    sprite('bc000_04', 6)	# 68260-68265
    sprite('bc000_05', 6)	# 68266-68271
    sprite('bc000_06', 6)	# 68272-68277
    sprite('bc000_07', 6)	# 68278-68283
    sprite('bc000_08', 6)	# 68284-68289
    sprite('bc000_09', 6)	# 68290-68295
    gotoLabel(201)
    label(202)
    sprite('bc204_00', 6)	# 68296-68301
    SFX_1('pbc601pna')
    sprite('bc204_01', 6)	# 68302-68307
    sprite('bc204_02', 6)	# 68308-68313
    label(203)
    sprite('bc204_03', 6)	# 68314-68319
    sprite('bc204_04', 6)	# 68320-68325
    sprite('bc204_05', 6)	# 68326-68331
    if SLOT_97:
        _gotolabel(203)
    sprite('bc204_00', 6)	# 68332-68337
    Unknown23018(1)
    label(204)
    sprite('bc000_00', 6)	# 68338-68343
    sprite('bc000_01', 6)	# 68344-68349
    sprite('bc000_02', 6)	# 68350-68355
    sprite('bc000_03', 6)	# 68356-68361
    sprite('bc000_04', 6)	# 68362-68367
    sprite('bc000_05', 6)	# 68368-68373
    sprite('bc000_06', 6)	# 68374-68379
    sprite('bc000_07', 6)	# 68380-68385
    sprite('bc000_08', 6)	# 68386-68391
    sprite('bc000_09', 6)	# 68392-68397
    gotoLabel(204)
    ExitState()
    label(210)
    sprite('bc000_00', 1)	# 68398-68398
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('bc000_00', 6)	# 68399-68404
    sprite('bc000_01', 6)	# 68405-68410
    sprite('bc000_02', 6)	# 68411-68416
    sprite('bc000_03', 6)	# 68417-68422
    sprite('bc000_04', 6)	# 68423-68428
    sprite('bc000_05', 6)	# 68429-68434
    sprite('bc000_06', 6)	# 68435-68440
    sprite('bc000_07', 6)	# 68441-68446
    sprite('bc000_08', 6)	# 68447-68452
    sprite('bc000_09', 6)	# 68453-68458
    gotoLabel(211)
    label(212)
    sprite('bc204_00', 6)	# 68459-68464
    SFX_1('pbc601pka')
    sprite('bc204_01', 6)	# 68465-68470
    sprite('bc204_02', 6)	# 68471-68476
    label(213)
    sprite('bc204_03', 6)	# 68477-68482
    sprite('bc204_04', 6)	# 68483-68488
    sprite('bc204_05', 6)	# 68489-68494
    if SLOT_97:
        _gotolabel(213)
    sprite('bc204_00', 6)	# 68495-68500
    Unknown21011(120)
    label(214)
    sprite('bc000_00', 6)	# 68501-68506
    sprite('bc000_01', 6)	# 68507-68512
    sprite('bc000_02', 6)	# 68513-68518
    sprite('bc000_03', 6)	# 68519-68524
    sprite('bc000_04', 6)	# 68525-68530
    sprite('bc000_05', 6)	# 68531-68536
    sprite('bc000_06', 6)	# 68537-68542
    sprite('bc000_07', 6)	# 68543-68548
    sprite('bc000_08', 6)	# 68549-68554
    sprite('bc000_09', 6)	# 68555-68560
    gotoLabel(214)
    ExitState()
    label(220)
    sprite('bc001_00', 7)	# 68561-68567
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('bc001_01', 7)	# 68568-68574
    SFX_1('pbc600pag')
    sprite('bc001_02', 7)	# 68575-68581
    sprite('bc001_03', 7)	# 68582-68588
    sprite('bc001_04', 7)	# 68589-68595
    sprite('bc001_05', 7)	# 68596-68602
    sprite('bc001_06', 7)	# 68603-68609
    sprite('bc001_01', 67)	# 68610-68676
    sprite('bc001_00', 7)	# 68677-68683
    label(221)
    sprite('bc000_00', 6)	# 68684-68689
    sprite('bc000_01', 6)	# 68690-68695
    sprite('bc000_02', 6)	# 68696-68701
    sprite('bc000_03', 6)	# 68702-68707
    sprite('bc000_04', 6)	# 68708-68713
    sprite('bc000_05', 6)	# 68714-68719
    sprite('bc000_06', 6)	# 68720-68725
    sprite('bc000_07', 6)	# 68726-68731
    sprite('bc000_08', 6)	# 68732-68737
    sprite('bc000_09', 6)	# 68738-68743
    if SLOT_97:
        _gotolabel(221)
    sprite('bc000_00', 1)	# 68744-68744
    Unknown21007(24, 40)
    Unknown21011(120)
    label(222)
    sprite('bc000_00', 6)	# 68745-68750
    sprite('bc000_01', 6)	# 68751-68756
    sprite('bc000_02', 6)	# 68757-68762
    sprite('bc000_03', 6)	# 68763-68768
    sprite('bc000_04', 6)	# 68769-68774
    sprite('bc000_05', 6)	# 68775-68780
    sprite('bc000_06', 6)	# 68781-68786
    sprite('bc000_07', 6)	# 68787-68792
    sprite('bc000_08', 6)	# 68793-68798
    sprite('bc000_09', 6)	# 68799-68804
    gotoLabel(222)
    ExitState()
    label(230)
    sprite('bc000_00', 1)	# 68805-68805
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('bc000_00', 6)	# 68806-68811
    sprite('bc000_01', 6)	# 68812-68817
    sprite('bc000_02', 6)	# 68818-68823
    sprite('bc000_03', 6)	# 68824-68829
    sprite('bc000_04', 6)	# 68830-68835
    sprite('bc000_05', 6)	# 68836-68841
    sprite('bc000_06', 6)	# 68842-68847
    sprite('bc000_07', 6)	# 68848-68853
    sprite('bc000_08', 6)	# 68854-68859
    sprite('bc000_09', 6)	# 68860-68865
    gotoLabel(231)
    label(232)
    sprite('bc001_00', 7)	# 68866-68872
    SFX_1('pbc601uyu')
    sprite('bc001_01', 7)	# 68873-68879
    sprite('bc001_02', 7)	# 68880-68886
    sprite('bc001_03', 7)	# 68887-68893
    sprite('bc001_04', 7)	# 68894-68900
    sprite('bc001_05', 7)	# 68901-68907
    sprite('bc001_06', 7)	# 68908-68914
    sprite('bc001_01', 100)	# 68915-69014
    sprite('bc001_00', 7)	# 69015-69021
    sprite('bc000_00', 6)	# 69022-69027
    sprite('bc000_01', 6)	# 69028-69033
    sprite('bc000_02', 6)	# 69034-69039
    sprite('bc000_03', 6)	# 69040-69045
    sprite('bc204_00', 4)	# 69046-69049
    sprite('bc204_01', 4)	# 69050-69053
    sprite('bc204_02', 4)	# 69054-69057
    sprite('bc204_03', 4)	# 69058-69061
    sprite('bc204_04', 4)	# 69062-69065
    sprite('bc204_05', 4)	# 69066-69069
    sprite('bc204_03', 4)	# 69070-69073
    sprite('bc204_04', 4)	# 69074-69077
    sprite('bc204_05', 4)	# 69078-69081
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_03', 4)	# 69082-69085
    GFX_1('persona_enter_ply', 0)
    sprite('bc204_04', 4)	# 69086-69089
    Unknown23029(11, 1000, 0)
    sprite('bc204_05', 4)	# 69090-69093
    label(233)
    sprite('bc204_03', 4)	# 69094-69097
    sprite('bc204_04', 4)	# 69098-69101
    sprite('bc204_05', 4)	# 69102-69105
    if SLOT_97:
        _gotolabel(233)
    sprite('bc204_03', 4)	# 69106-69109
    sprite('bc204_04', 4)	# 69110-69113
    sprite('bc204_05', 4)	# 69114-69117
    sprite('bc204_03', 4)	# 69118-69121
    sprite('bc204_04', 4)	# 69122-69125
    sprite('bc204_05', 4)	# 69126-69129
    sprite('bc204_03', 4)	# 69130-69133
    sprite('bc204_04', 4)	# 69134-69137
    sprite('bc204_05', 4)	# 69138-69141
    Unknown23018(1)
    label(234)
    sprite('bc000_00', 6)	# 69142-69147
    sprite('bc000_01', 6)	# 69148-69153
    sprite('bc000_02', 6)	# 69154-69159
    sprite('bc000_03', 6)	# 69160-69165
    sprite('bc000_04', 6)	# 69166-69171
    sprite('bc000_05', 6)	# 69172-69177
    sprite('bc000_06', 6)	# 69178-69183
    sprite('bc000_07', 6)	# 69184-69189
    sprite('bc000_08', 6)	# 69190-69195
    sprite('bc000_09', 6)	# 69196-69201
    gotoLabel(234)
    ExitState()
    label(240)
    sprite('bc601_00', 6)	# 69202-69207
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('bc601_01', 6)	# 69208-69213
    sprite('bc601_02', 6)	# 69214-69219
    sprite('bc601_00', 6)	# 69220-69225
    SFX_1('pbc600pla')
    sprite('bc601_01', 6)	# 69226-69231
    sprite('bc601_02', 6)	# 69232-69237
    sprite('bc601_00', 6)	# 69238-69243
    sprite('bc601_01', 6)	# 69244-69249
    sprite('bc601_02', 6)	# 69250-69255
    sprite('bc601_00', 6)	# 69256-69261
    sprite('bc601_01', 6)	# 69262-69267
    sprite('bc601_02', 6)	# 69268-69273
    sprite('bc601_00', 6)	# 69274-69279
    sprite('bc601_01', 6)	# 69280-69285
    sprite('bc601_02', 6)	# 69286-69291
    sprite('bc601_00', 6)	# 69292-69297
    sprite('bc601_01', 6)	# 69298-69303
    sprite('bc601_02', 6)	# 69304-69309
    sprite('bc601_03', 6)	# 69310-69315
    Unknown21007(24, 40)
    sprite('bc601_04', 6)	# 69316-69321
    sprite('bc601_05', 6)	# 69322-69327
    sprite('bc601_06', 6)	# 69328-69333
    sprite('bc601_07', 6)	# 69334-69339
    sprite('bc601_08', 6)	# 69340-69345
    SFX_3('slash_knife_slow')
    SFX_3('guard_slash_s')
    sprite('bc601_09', 6)	# 69346-69351
    GFX_1('bcef_entry2_02', 0)
    sprite('bc601_10', 6)	# 69352-69357
    sprite('bc601_11', 6)	# 69358-69363
    sprite('bc601_12', 6)	# 69364-69369
    sprite('bc601_13', 6)	# 69370-69375
    sprite('bc601_14', 6)	# 69376-69381
    sprite('bc601_15', 6)	# 69382-69387
    sprite('bc601_16', 6)	# 69388-69393
    SFX_3('slash_rapier_fast')
    GFX_0('Entry2', 0)
    sprite('bc601_17', 6)	# 69394-69399
    sprite('bc601_18', 6)	# 69400-69405
    Unknown21011(450)
    label(241)
    sprite('bc000_00', 6)	# 69406-69411
    sprite('bc000_01', 6)	# 69412-69417
    sprite('bc000_02', 6)	# 69418-69423
    sprite('bc000_03', 6)	# 69424-69429
    sprite('bc000_04', 6)	# 69430-69435
    sprite('bc000_05', 6)	# 69436-69441
    sprite('bc000_06', 6)	# 69442-69447
    sprite('bc000_07', 6)	# 69448-69453
    sprite('bc000_08', 6)	# 69454-69459
    sprite('bc000_09', 6)	# 69460-69465
    gotoLabel(241)
    ExitState()
    label(250)
    sprite('bc601_00', 1)	# 69466-69466
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(252)
        SFX_1('pbc601biz')
    label(251)
    sprite('bc601_00', 6)	# 69467-69472
    sprite('bc601_01', 6)	# 69473-69478
    sprite('bc601_02', 6)	# 69479-69484
    gotoLabel(251)
    label(252)
    sprite('bc601_00', 6)	# 69485-69490
    sprite('bc601_01', 6)	# 69491-69496
    sprite('bc601_02', 6)	# 69497-69502
    if SLOT_97:
        _gotolabel(252)
    sprite('bc601_03', 6)	# 69503-69508
    sprite('bc601_04', 6)	# 69509-69514
    sprite('bc601_05', 6)	# 69515-69520
    sprite('bc601_06', 6)	# 69521-69526
    sprite('bc601_07', 6)	# 69527-69532
    sprite('bc601_08', 6)	# 69533-69538
    SFX_3('slash_knife_slow')
    SFX_3('guard_slash_s')
    sprite('bc601_09', 6)	# 69539-69544
    GFX_1('bcef_entry2_02', 0)
    sprite('bc601_10', 6)	# 69545-69550
    sprite('bc601_11', 6)	# 69551-69556
    sprite('bc601_12', 6)	# 69557-69562
    sprite('bc601_13', 6)	# 69563-69568
    sprite('bc601_14', 6)	# 69569-69574
    sprite('bc601_15', 6)	# 69575-69580
    sprite('bc601_16', 6)	# 69581-69586
    SFX_3('slash_rapier_fast')
    GFX_0('Entry2', 0)
    sprite('bc601_17', 6)	# 69587-69592
    sprite('bc601_18', 6)	# 69593-69598
    Unknown23018(1)
    label(253)
    sprite('bc000_00', 6)	# 69599-69604
    sprite('bc000_01', 6)	# 69605-69610
    sprite('bc000_02', 6)	# 69611-69616
    sprite('bc000_03', 6)	# 69617-69622
    sprite('bc000_04', 6)	# 69623-69628
    sprite('bc000_05', 6)	# 69629-69634
    sprite('bc000_06', 6)	# 69635-69640
    sprite('bc000_07', 6)	# 69641-69646
    sprite('bc000_08', 6)	# 69647-69652
    sprite('bc000_09', 6)	# 69653-69658
    gotoLabel(253)
    ExitState()
    label(991)
    sprite('bc000_00', 1)	# 69659-69659
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('bc000_00', 6)	# 69660-69665
    sprite('bc000_01', 6)	# 69666-69671
    sprite('bc000_02', 6)	# 69672-69677
    sprite('bc000_03', 6)	# 69678-69683
    sprite('bc000_04', 6)	# 69684-69689
    sprite('bc000_05', 6)	# 69690-69695
    sprite('bc000_06', 6)	# 69696-69701
    sprite('bc000_07', 6)	# 69702-69707
    sprite('bc000_08', 6)	# 69708-69713
    sprite('bc000_09', 6)	# 69714-69719
    gotoLabel(992)
    label(993)
    sprite('bc033_00', 2)	# 69720-69721

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
    sprite('bc033_01', 3)	# 69722-69724
    label(994)
    sprite('bc033_02', 3)	# 69725-69727
    sprite('bc033_01', 3)	# 69728-69730
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 69731-69733
    ExitState()

@State
def CmnActMatchWin():
    if SLOT_169:
        _gotolabel(482)
    if SLOT_122:
        _gotolabel(482)
    if SLOT_123:
        _gotolabel(482)
    if SLOT_59:
        _gotolabel(20)
    sprite('keep', 2)	# 1-2

    def upon_3():
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
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(240)
                    clearUponHandler(3)
            if PartnerChar('biz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(250)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('bc610_00', 6)	# 4-9
    sprite('bc610_01', 6)	# 10-15
    sprite('bc610_02', 6)	# 16-21
    sprite('bc610_03', 6)	# 22-27
    sprite('bc610_04', 6)	# 28-33
    sprite('bc610_05', 6)	# 34-39
    sprite('bc610_06', 6)	# 40-45
    GFX_1('ef_thunder_damage_b', 0)
    sprite('bc610_07', 30)	# 46-75
    GFX_1('bcef_matchwin_01', 0)
    SFX_3('electric_m')
    sprite('bc610_08', 3)	# 76-78
    SFX_3('slash_rapier_fast')
    sprite('bc610_09', 6)	# 79-84
    GFX_1('ef_thunder_damage_b', 0)
    GFX_1('bcef_matchwin_oku_01', 1)
    sprite('bc610_10', 6)	# 85-90
    SFX_3('electric_s')
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 91-96
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pbc524', 100, 895705712, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pbc402_0', 100, 878928496, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pbc520', 100, 895705712, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('bc610_12', 6)	# 97-102
    label(1000)
    sprite('bc610_10', 6)	# 103-108
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 109-114
    sprite('bc610_12', 6)	# 115-120
    loopRest()
    gotoLabel(1000)
    label(10)
    sprite('bc611_00', 6)	# 121-126
    sprite('bc611_01', 6)	# 127-132
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 133-138
    sprite('bc611_03', 6)	# 139-144
    sprite('bc611_04', 6)	# 145-150
    sprite('bc611_05', 6)	# 151-156
    sprite('bc611_06', 6)	# 157-162
    sprite('bc611_07', 6)	# 163-168
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 169-174
    sprite('bc611_09', 6)	# 175-180
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 181-186
    sprite('bc611_11', 6)	# 187-192
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pbc524', 100, 895705712, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pbc402_0', 100, 878928496, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pbc522', 100, 895705712, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(11)
    sprite('bc611_09', 6)	# 193-198
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 199-204
    sprite('bc611_11', 6)	# 205-210
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('bc611_00', 6)	# 211-216
    sprite('bc611_01', 6)	# 217-222
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 223-228
    sprite('bc611_03', 6)	# 229-234
    sprite('bc611_04', 6)	# 235-240
    sprite('bc611_05', 6)	# 241-246
    sprite('bc611_06', 6)	# 247-252
    sprite('bc611_07', 6)	# 253-258
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 259-264
    sprite('bc611_09', 6)	# 265-270
    sprite('bc611_10', 6)	# 271-276
    sprite('bc611_11', 6)	# 277-282
    Unknown7006('pbc293_0', 100, 845374064, 828322617, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(21)
    sprite('bc611_09', 6)	# 283-288
    sprite('bc611_10', 6)	# 289-294
    sprite('bc611_11', 6)	# 295-300
    loopRest()
    gotoLabel(21)
    label(100)
    sprite('bc000_00', 1)	# 301-301

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('bc000_00', 6)	# 302-307
    sprite('bc000_01', 6)	# 308-313
    sprite('bc000_02', 6)	# 314-319
    sprite('bc000_03', 6)	# 320-325
    sprite('bc000_04', 6)	# 326-331
    sprite('bc000_05', 6)	# 332-337
    sprite('bc000_06', 6)	# 338-343
    sprite('bc000_07', 6)	# 344-349
    sprite('bc000_08', 6)	# 350-355
    sprite('bc000_09', 6)	# 356-361
    gotoLabel(101)
    label(102)
    sprite('bc610_00', 6)	# 362-367
    sprite('bc610_01', 6)	# 368-373
    sprite('bc610_02', 6)	# 374-379
    sprite('bc610_03', 6)	# 380-385
    sprite('bc610_04', 6)	# 386-391
    sprite('bc610_05', 6)	# 392-397
    sprite('bc610_06', 6)	# 398-403
    GFX_1('ef_thunder_damage_b', 0)
    sprite('bc610_07', 30)	# 404-433
    GFX_1('bcef_matchwin_01', 0)
    SFX_3('electric_m')
    sprite('bc610_08', 3)	# 434-436
    SFX_3('slash_rapier_fast')
    sprite('bc610_09', 6)	# 437-442
    GFX_1('ef_thunder_damage_b', 0)
    GFX_1('bcef_matchwin_oku_01', 1)
    sprite('bc610_10', 6)	# 443-448
    SFX_3('electric_s')
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 449-454
    SFX_1('pbc701brg')
    sprite('bc610_12', 6)	# 455-460
    label(103)
    sprite('bc610_10', 6)	# 461-466
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 467-472
    sprite('bc610_12', 6)	# 473-478
    loopRest()
    if SLOT_97:
        _gotolabel(103)
    sprite('bc610_10', 1)	# 479-479
    Unknown23018(1)
    label(104)
    sprite('bc610_10', 6)	# 480-485
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 486-491
    sprite('bc610_12', 6)	# 492-497
    loopRest()
    gotoLabel(104)
    label(110)
    sprite('bc610_00', 6)	# 498-503
    sprite('bc610_01', 6)	# 504-509
    sprite('bc610_02', 6)	# 510-515
    sprite('bc610_03', 6)	# 516-521
    sprite('bc610_04', 6)	# 522-527
    sprite('bc610_05', 6)	# 528-533
    sprite('bc610_06', 6)	# 534-539
    GFX_1('ef_thunder_damage_b', 0)
    sprite('bc610_07', 30)	# 540-569
    GFX_1('bcef_matchwin_01', 0)
    SFX_3('electric_m')
    sprite('bc610_08', 3)	# 570-572
    SFX_3('slash_rapier_fast')
    sprite('bc610_09', 6)	# 573-578
    GFX_1('ef_thunder_damage_b', 0)
    GFX_1('bcef_matchwin_oku_01', 1)
    sprite('bc610_10', 6)	# 579-584
    SFX_3('electric_s')
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 585-590
    SFX_1('pbc700bha')
    sprite('bc610_12', 6)	# 591-596
    label(111)
    sprite('bc610_10', 6)	# 597-602
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 603-608
    sprite('bc610_12', 6)	# 609-614
    loopRest()
    if SLOT_97:
        _gotolabel(111)
    sprite('bc610_10', 1)	# 615-615
    Unknown21007(24, 40)
    Unknown21011(240)
    label(112)
    sprite('bc610_10', 6)	# 616-621
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 622-627
    sprite('bc610_12', 6)	# 628-633
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('bc000_00', 1)	# 634-634

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('bc000_00', 6)	# 635-640
    sprite('bc000_01', 6)	# 641-646
    sprite('bc000_02', 6)	# 647-652
    sprite('bc000_03', 6)	# 653-658
    sprite('bc000_04', 6)	# 659-664
    sprite('bc000_05', 6)	# 665-670
    sprite('bc000_06', 6)	# 671-676
    sprite('bc000_07', 6)	# 677-682
    sprite('bc000_08', 6)	# 683-688
    sprite('bc000_09', 6)	# 689-694
    gotoLabel(121)
    label(122)
    sprite('bc611_00', 6)	# 695-700
    sprite('bc611_01', 6)	# 701-706
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 707-712
    sprite('bc611_03', 6)	# 713-718
    sprite('bc611_04', 6)	# 719-724
    sprite('bc611_05', 6)	# 725-730
    sprite('bc611_06', 6)	# 731-736
    sprite('bc611_07', 6)	# 737-742
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 743-748
    sprite('bc611_09', 6)	# 749-754
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 755-760
    sprite('bc611_11', 6)	# 761-766
    SFX_1('pbc701bes')
    label(123)
    sprite('bc611_09', 6)	# 767-772
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 773-778
    sprite('bc611_11', 6)	# 779-784
    loopRest()
    if SLOT_97:
        _gotolabel(123)
    sprite('bc611_09', 1)	# 785-785
    Unknown23018(1)
    label(124)
    sprite('bc611_09', 6)	# 786-791
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 792-797
    sprite('bc611_11', 6)	# 798-803
    loopRest()
    gotoLabel(124)
    label(130)
    sprite('bc000_00', 1)	# 804-804

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('bc000_00', 6)	# 805-810
    sprite('bc000_01', 6)	# 811-816
    sprite('bc000_02', 6)	# 817-822
    sprite('bc000_03', 6)	# 823-828
    sprite('bc000_04', 6)	# 829-834
    sprite('bc000_05', 6)	# 835-840
    sprite('bc000_06', 6)	# 841-846
    sprite('bc000_07', 6)	# 847-852
    sprite('bc000_08', 6)	# 853-858
    sprite('bc000_09', 6)	# 859-864
    gotoLabel(131)
    label(132)
    sprite('bc611_00', 6)	# 865-870
    sprite('bc611_01', 6)	# 871-876
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 877-882
    sprite('bc611_03', 6)	# 883-888
    sprite('bc611_04', 6)	# 889-894
    sprite('bc611_05', 6)	# 895-900
    sprite('bc611_06', 6)	# 901-906
    sprite('bc611_07', 6)	# 907-912
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 913-918
    sprite('bc611_09', 6)	# 919-924
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 925-930
    sprite('bc611_11', 6)	# 931-936
    SFX_1('pbc701pyo')
    label(133)
    sprite('bc611_09', 6)	# 937-942
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 943-948
    sprite('bc611_11', 6)	# 949-954
    loopRest()
    if SLOT_97:
        _gotolabel(133)
    sprite('bc611_09', 1)	# 955-955
    Unknown18008()
    label(134)
    sprite('bc611_09', 6)	# 956-961
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 962-967
    sprite('bc611_11', 6)	# 968-973
    loopRest()
    gotoLabel(134)
    label(140)
    sprite('bc000_00', 1)	# 974-974

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('bc000_00', 6)	# 975-980
    sprite('bc000_01', 6)	# 981-986
    sprite('bc000_02', 6)	# 987-992
    sprite('bc000_03', 6)	# 993-998
    sprite('bc000_04', 6)	# 999-1004
    sprite('bc000_05', 6)	# 1005-1010
    sprite('bc000_06', 6)	# 1011-1016
    sprite('bc000_07', 6)	# 1017-1022
    sprite('bc000_08', 6)	# 1023-1028
    sprite('bc000_09', 6)	# 1029-1034
    gotoLabel(141)
    label(142)
    sprite('bc611_00', 6)	# 1035-1040
    sprite('bc611_01', 6)	# 1041-1046
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 1047-1052
    sprite('bc611_03', 6)	# 1053-1058
    sprite('bc611_04', 6)	# 1059-1064
    sprite('bc611_05', 6)	# 1065-1070
    sprite('bc611_06', 6)	# 1071-1076
    sprite('bc611_07', 6)	# 1077-1082
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 1083-1088
    sprite('bc611_09', 6)	# 1089-1094
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1095-1100
    sprite('bc611_11', 6)	# 1101-1106
    SFX_1('pbc701pyu')
    label(143)
    sprite('bc611_09', 6)	# 1107-1112
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1113-1118
    sprite('bc611_11', 6)	# 1119-1124
    loopRest()
    if SLOT_97:
        _gotolabel(143)
    sprite('bc611_09', 1)	# 1125-1125
    Unknown21011(60)
    label(144)
    sprite('bc611_09', 6)	# 1126-1131
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1132-1137
    sprite('bc611_11', 6)	# 1138-1143
    loopRest()
    gotoLabel(144)
    label(150)
    sprite('bc611_00', 6)	# 1144-1149
    sprite('bc611_01', 6)	# 1150-1155
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 1156-1161
    sprite('bc611_03', 6)	# 1162-1167
    sprite('bc611_04', 6)	# 1168-1173
    sprite('bc611_05', 6)	# 1174-1179
    sprite('bc611_06', 6)	# 1180-1185
    sprite('bc611_07', 6)	# 1186-1191
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 1192-1197
    sprite('bc611_09', 6)	# 1198-1203
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1204-1209
    sprite('bc611_11', 6)	# 1210-1215
    SFX_1('pbc700pce')
    label(151)
    sprite('bc611_09', 6)	# 1216-1221
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1222-1227
    sprite('bc611_11', 6)	# 1228-1233
    loopRest()
    if SLOT_97:
        _gotolabel(151)
    sprite('bc611_09', 6)	# 1234-1239
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1240-1245
    sprite('bc611_11', 6)	# 1246-1251
    sprite('bc611_09', 6)	# 1252-1257
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1258-1263
    sprite('bc611_11', 6)	# 1264-1269
    sprite('bc611_09', 1)	# 1270-1270
    Unknown21011(180)
    Unknown21007(24, 40)
    label(152)
    sprite('bc611_09', 6)	# 1271-1276
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1277-1282
    sprite('bc611_11', 6)	# 1283-1288
    gotoLabel(152)
    label(160)
    sprite('bc000_00', 1)	# 1289-1289

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('bc000_00', 6)	# 1290-1295
    sprite('bc000_01', 6)	# 1296-1301
    sprite('bc000_02', 6)	# 1302-1307
    sprite('bc000_03', 6)	# 1308-1313
    sprite('bc000_04', 6)	# 1314-1319
    sprite('bc000_05', 6)	# 1320-1325
    sprite('bc000_06', 6)	# 1326-1331
    sprite('bc000_07', 6)	# 1332-1337
    sprite('bc000_08', 6)	# 1338-1343
    sprite('bc000_09', 6)	# 1344-1349
    gotoLabel(161)
    label(162)
    sprite('bc611_00', 6)	# 1350-1355
    sprite('bc611_01', 6)	# 1356-1361
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 1362-1367
    sprite('bc611_03', 6)	# 1368-1373
    sprite('bc611_04', 6)	# 1374-1379
    sprite('bc611_05', 6)	# 1380-1385
    sprite('bc611_06', 6)	# 1386-1391
    sprite('bc611_07', 6)	# 1392-1397
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 1398-1403
    sprite('bc611_09', 6)	# 1404-1409
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1410-1415
    sprite('bc611_11', 6)	# 1416-1421
    SFX_1('pbc701pka')
    label(163)
    sprite('bc611_09', 6)	# 1422-1427
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1428-1433
    sprite('bc611_11', 6)	# 1434-1439
    loopRest()
    if SLOT_97:
        _gotolabel(163)
    sprite('bc611_09', 6)	# 1440-1445
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1446-1451
    sprite('bc611_11', 6)	# 1452-1457
    Unknown21007(24, 40)
    Unknown21011(240)
    label(164)
    sprite('bc611_09', 6)	# 1458-1463
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1464-1469
    sprite('bc611_11', 6)	# 1470-1475
    loopRest()
    gotoLabel(164)
    label(170)
    sprite('bc611_00', 6)	# 1476-1481
    sprite('bc611_01', 6)	# 1482-1487
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 1488-1493
    sprite('bc611_03', 6)	# 1494-1499
    sprite('bc611_04', 6)	# 1500-1505
    sprite('bc611_05', 6)	# 1506-1511
    sprite('bc611_06', 6)	# 1512-1517
    sprite('bc611_07', 6)	# 1518-1523
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 1524-1529
    sprite('bc611_09', 6)	# 1530-1535
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1536-1541
    sprite('bc611_11', 6)	# 1542-1547
    SFX_1('pbc700pna')
    label(171)
    sprite('bc611_09', 6)	# 1548-1553
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1554-1559
    sprite('bc611_11', 6)	# 1560-1565
    loopRest()
    if SLOT_97:
        _gotolabel(171)
    sprite('bc611_09', 6)	# 1566-1571
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1572-1577
    sprite('bc611_11', 6)	# 1578-1583
    sprite('bc611_09', 6)	# 1584-1589
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1590-1595
    sprite('bc611_11', 6)	# 1596-1601
    Unknown2034(0)
    Unknown2053(0)
    Unknown21007(24, 40)
    Unknown21011(240)
    label(172)
    sprite('bc611_09', 6)	# 1602-1607
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1608-1613
    sprite('bc611_11', 6)	# 1614-1619
    gotoLabel(172)
    label(180)
    sprite('bc000_00', 1)	# 1620-1620

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('bc000_00', 6)	# 1621-1626
    sprite('bc000_01', 6)	# 1627-1632
    sprite('bc000_02', 6)	# 1633-1638
    sprite('bc000_03', 6)	# 1639-1644
    sprite('bc000_04', 6)	# 1645-1650
    sprite('bc000_05', 6)	# 1651-1656
    sprite('bc000_06', 6)	# 1657-1662
    sprite('bc000_07', 6)	# 1663-1668
    sprite('bc000_08', 6)	# 1669-1674
    sprite('bc000_09', 6)	# 1675-1680
    gotoLabel(181)
    label(182)
    sprite('bc611_00', 6)	# 1681-1686
    sprite('bc611_01', 6)	# 1687-1692
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 1693-1698
    sprite('bc611_03', 6)	# 1699-1704
    sprite('bc611_04', 6)	# 1705-1710
    sprite('bc611_05', 6)	# 1711-1716
    sprite('bc611_06', 6)	# 1717-1722
    sprite('bc611_07', 6)	# 1723-1728
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 1729-1734
    sprite('bc611_09', 6)	# 1735-1740
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1741-1746
    sprite('bc611_11', 6)	# 1747-1752
    SFX_1('pbc701uhy')
    label(183)
    sprite('bc611_09', 6)	# 1753-1758
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1759-1764
    sprite('bc611_11', 6)	# 1765-1770
    loopRest()
    if SLOT_97:
        _gotolabel(183)
    sprite('bc611_09', 1)	# 1771-1771
    Unknown23018(1)
    label(184)
    sprite('bc611_09', 6)	# 1772-1777
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1778-1783
    sprite('bc611_11', 6)	# 1784-1789
    loopRest()
    gotoLabel(184)
    label(190)
    sprite('bc000_00', 1)	# 1790-1790

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('bc000_00', 6)	# 1791-1796
    sprite('bc000_01', 6)	# 1797-1802
    sprite('bc000_02', 6)	# 1803-1808
    sprite('bc000_03', 6)	# 1809-1814
    sprite('bc000_04', 6)	# 1815-1820
    sprite('bc000_05', 6)	# 1821-1826
    sprite('bc000_06', 6)	# 1827-1832
    sprite('bc000_07', 6)	# 1833-1838
    sprite('bc000_08', 6)	# 1839-1844
    sprite('bc000_09', 6)	# 1845-1850
    gotoLabel(191)
    label(192)
    sprite('bc611_00', 6)	# 1851-1856
    sprite('bc611_01', 6)	# 1857-1862
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 1863-1868
    sprite('bc611_03', 6)	# 1869-1874
    sprite('bc611_04', 6)	# 1875-1880
    sprite('bc611_05', 6)	# 1881-1886
    sprite('bc611_06', 6)	# 1887-1892
    sprite('bc611_07', 6)	# 1893-1898
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 1899-1904
    sprite('bc611_09', 6)	# 1905-1910
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1911-1916
    sprite('bc611_11', 6)	# 1917-1922
    SFX_1('pbc701ugo')
    label(193)
    sprite('bc611_09', 6)	# 1923-1928
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1929-1934
    sprite('bc611_11', 6)	# 1935-1940
    loopRest()
    if SLOT_97:
        _gotolabel(193)
    sprite('bc611_09', 1)	# 1941-1941
    Unknown21011(120)
    label(194)
    sprite('bc611_09', 6)	# 1942-1947
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 1948-1953
    sprite('bc611_11', 6)	# 1954-1959
    loopRest()
    gotoLabel(194)
    label(200)
    sprite('bc611_00', 6)	# 1960-1965
    sprite('bc611_01', 6)	# 1966-1971
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 1972-1977
    sprite('bc611_03', 6)	# 1978-1983
    sprite('bc611_04', 6)	# 1984-1989
    sprite('bc611_05', 6)	# 1990-1995
    sprite('bc611_06', 6)	# 1996-2001
    sprite('bc611_07', 6)	# 2002-2007
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 2008-2013
    sprite('bc611_09', 6)	# 2014-2019
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2020-2025
    sprite('bc611_11', 6)	# 2026-2031
    SFX_1('pbc700rrb')
    label(201)
    sprite('bc611_09', 6)	# 2032-2037
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2038-2043
    sprite('bc611_11', 6)	# 2044-2049
    loopRest()
    if SLOT_97:
        _gotolabel(201)
    sprite('bc611_09', 1)	# 2050-2050
    Unknown21011(300)
    Unknown21007(24, 40)
    label(202)
    sprite('bc611_09', 6)	# 2051-2056
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2057-2062
    sprite('bc611_11', 6)	# 2063-2068
    gotoLabel(202)
    label(210)
    sprite('bc000_00', 1)	# 2069-2069

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('bc000_00', 6)	# 2070-2075
    sprite('bc000_01', 6)	# 2076-2081
    sprite('bc000_02', 6)	# 2082-2087
    sprite('bc000_03', 6)	# 2088-2093
    sprite('bc000_04', 6)	# 2094-2099
    sprite('bc000_05', 6)	# 2100-2105
    sprite('bc000_06', 6)	# 2106-2111
    sprite('bc000_07', 6)	# 2112-2117
    sprite('bc000_08', 6)	# 2118-2123
    sprite('bc000_09', 6)	# 2124-2129
    gotoLabel(211)
    label(212)
    sprite('bc611_00', 6)	# 2130-2135
    sprite('bc611_01', 6)	# 2136-2141
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 2142-2147
    sprite('bc611_03', 6)	# 2148-2153
    sprite('bc611_04', 6)	# 2154-2159
    sprite('bc611_05', 6)	# 2160-2165
    sprite('bc611_06', 6)	# 2166-2171
    sprite('bc611_07', 6)	# 2172-2177
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 2178-2183
    sprite('bc611_09', 6)	# 2184-2189
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2190-2195
    sprite('bc611_11', 6)	# 2196-2201
    SFX_1('pbc701rwi')
    label(213)
    sprite('bc611_09', 6)	# 2202-2207
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2208-2213
    sprite('bc611_11', 6)	# 2214-2219
    loopRest()
    if SLOT_97:
        _gotolabel(213)
    sprite('bc611_09', 6)	# 2220-2225
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2226-2231
    sprite('bc611_11', 6)	# 2232-2237
    sprite('bc611_09', 1)	# 2238-2238
    Unknown21007(24, 40)
    Unknown21011(180)
    label(214)
    sprite('bc611_09', 6)	# 2239-2244
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2245-2250
    sprite('bc611_11', 6)	# 2251-2256
    loopRest()
    gotoLabel(214)
    label(220)
    sprite('bc000_00', 1)	# 2257-2257

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('bc000_00', 6)	# 2258-2263
    sprite('bc000_01', 6)	# 2264-2269
    sprite('bc000_02', 6)	# 2270-2275
    sprite('bc000_03', 6)	# 2276-2281
    sprite('bc000_04', 6)	# 2282-2287
    sprite('bc000_05', 6)	# 2288-2293
    sprite('bc000_06', 6)	# 2294-2299
    sprite('bc000_07', 6)	# 2300-2305
    sprite('bc000_08', 6)	# 2306-2311
    sprite('bc000_09', 6)	# 2312-2317
    gotoLabel(221)
    label(222)
    sprite('bc610_00', 6)	# 2318-2323
    sprite('bc610_01', 6)	# 2324-2329
    sprite('bc610_02', 6)	# 2330-2335
    sprite('bc610_03', 6)	# 2336-2341
    sprite('bc610_04', 6)	# 2342-2347
    sprite('bc610_05', 6)	# 2348-2353
    sprite('bc610_06', 6)	# 2354-2359
    GFX_1('ef_thunder_damage_b', 0)
    sprite('bc610_07', 30)	# 2360-2389
    GFX_1('bcef_matchwin_01', 0)
    SFX_3('electric_m')
    sprite('bc610_08', 3)	# 2390-2392
    SFX_3('slash_rapier_fast')
    sprite('bc610_09', 6)	# 2393-2398
    GFX_1('ef_thunder_damage_b', 0)
    GFX_1('bcef_matchwin_oku_01', 1)
    sprite('bc610_10', 6)	# 2399-2404
    SFX_3('electric_s')
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 2405-2410
    SFX_1('pbc701pag')
    sprite('bc610_12', 6)	# 2411-2416
    label(223)
    sprite('bc610_10', 6)	# 2417-2422
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 2423-2428
    sprite('bc610_12', 6)	# 2429-2434
    loopRest()
    if SLOT_97:
        _gotolabel(223)
    sprite('bc610_10', 1)	# 2435-2435
    Unknown21011(120)
    label(224)
    sprite('bc610_10', 6)	# 2436-2441
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 2442-2447
    sprite('bc610_12', 6)	# 2448-2453
    loopRest()
    gotoLabel(224)
    label(230)
    sprite('bc000_00', 1)	# 2454-2454

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('bc000_00', 6)	# 2455-2460
    sprite('bc000_01', 6)	# 2461-2466
    sprite('bc000_02', 6)	# 2467-2472
    sprite('bc000_03', 6)	# 2473-2478
    sprite('bc000_04', 6)	# 2479-2484
    sprite('bc000_05', 6)	# 2485-2490
    sprite('bc000_06', 6)	# 2491-2496
    sprite('bc000_07', 6)	# 2497-2502
    sprite('bc000_08', 6)	# 2503-2508
    sprite('bc000_09', 6)	# 2509-2514
    gotoLabel(231)
    label(232)
    sprite('bc611_00', 6)	# 2515-2520
    sprite('bc611_01', 6)	# 2521-2526
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 2527-2532
    sprite('bc611_03', 6)	# 2533-2538
    sprite('bc611_04', 6)	# 2539-2544
    sprite('bc611_05', 6)	# 2545-2550
    sprite('bc611_06', 6)	# 2551-2556
    sprite('bc611_07', 6)	# 2557-2562
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 2563-2568
    sprite('bc611_09', 6)	# 2569-2574
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2575-2580
    sprite('bc611_11', 6)	# 2581-2586
    SFX_1('pbc701uyu')
    label(233)
    sprite('bc611_09', 6)	# 2587-2592
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2593-2598
    sprite('bc611_11', 6)	# 2599-2604
    loopRest()
    if SLOT_97:
        _gotolabel(233)
    sprite('bc611_09', 6)	# 2605-2610
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2611-2616
    sprite('bc611_11', 6)	# 2617-2622
    Unknown23018(1)
    label(234)
    sprite('bc611_09', 6)	# 2623-2628
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2629-2634
    sprite('bc611_11', 6)	# 2635-2640
    loopRest()
    gotoLabel(234)
    label(240)
    sprite('bc000_00', 1)	# 2641-2641

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    label(241)
    sprite('bc000_00', 6)	# 2642-2647
    sprite('bc000_01', 6)	# 2648-2653
    sprite('bc000_02', 6)	# 2654-2659
    sprite('bc000_03', 6)	# 2660-2665
    sprite('bc000_04', 6)	# 2666-2671
    sprite('bc000_05', 6)	# 2672-2677
    sprite('bc000_06', 6)	# 2678-2683
    sprite('bc000_07', 6)	# 2684-2689
    sprite('bc000_08', 6)	# 2690-2695
    sprite('bc000_09', 6)	# 2696-2701
    gotoLabel(241)
    label(242)
    sprite('bc611_00', 6)	# 2702-2707
    sprite('bc611_01', 6)	# 2708-2713
    SFX_3('slash_knife_slow')
    sprite('bc611_02', 6)	# 2714-2719
    sprite('bc611_03', 6)	# 2720-2725
    sprite('bc611_04', 6)	# 2726-2731
    sprite('bc611_05', 6)	# 2732-2737
    sprite('bc611_06', 6)	# 2738-2743
    sprite('bc611_07', 6)	# 2744-2749
    GFX_1('bcef_matchwin2_02', 0)
    SFX_3('slash_knife_fast')
    sprite('bc611_08', 6)	# 2750-2755
    sprite('bc611_09', 6)	# 2756-2761
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2762-2767
    sprite('bc611_11', 6)	# 2768-2773
    SFX_1('pbc701pla')
    label(243)
    sprite('bc611_09', 6)	# 2774-2779
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2780-2785
    sprite('bc611_11', 6)	# 2786-2791
    loopRest()
    if SLOT_97:
        _gotolabel(243)
    sprite('bc611_09', 6)	# 2792-2797
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2798-2803
    sprite('bc611_11', 6)	# 2804-2809
    Unknown21007(24, 40)
    Unknown21011(300)
    label(244)
    sprite('bc611_09', 6)	# 2810-2815
    SFX_3('cloth_l')
    sprite('bc611_10', 6)	# 2816-2821
    sprite('bc611_11', 6)	# 2822-2827
    loopRest()
    gotoLabel(244)
    label(250)
    sprite('bc000_00', 1)	# 2828-2828

    def upon_40():
        clearUponHandler(40)
        sendToLabel(252)
    label(251)
    sprite('bc000_00', 6)	# 2829-2834
    sprite('bc000_01', 6)	# 2835-2840
    sprite('bc000_02', 6)	# 2841-2846
    sprite('bc000_03', 6)	# 2847-2852
    sprite('bc000_04', 6)	# 2853-2858
    sprite('bc000_05', 6)	# 2859-2864
    sprite('bc000_06', 6)	# 2865-2870
    sprite('bc000_07', 6)	# 2871-2876
    sprite('bc000_08', 6)	# 2877-2882
    sprite('bc000_09', 6)	# 2883-2888
    gotoLabel(251)
    label(252)
    sprite('bc610_00', 6)	# 2889-2894
    sprite('bc610_01', 6)	# 2895-2900
    sprite('bc610_02', 6)	# 2901-2906
    sprite('bc610_03', 6)	# 2907-2912
    sprite('bc610_04', 6)	# 2913-2918
    sprite('bc610_05', 6)	# 2919-2924
    sprite('bc610_06', 6)	# 2925-2930
    GFX_1('ef_thunder_damage_b', 0)
    sprite('bc610_07', 30)	# 2931-2960
    GFX_1('bcef_matchwin_01', 0)
    SFX_3('electric_m')
    sprite('bc610_08', 3)	# 2961-2963
    SFX_3('slash_rapier_fast')
    sprite('bc610_09', 6)	# 2964-2969
    GFX_1('ef_thunder_damage_b', 0)
    GFX_1('bcef_matchwin_oku_01', 1)
    sprite('bc610_10', 6)	# 2970-2975
    SFX_3('electric_s')
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 2976-2981
    SFX_1('pbc701biz')
    sprite('bc610_12', 6)	# 2982-2987
    Unknown23018(1)
    label(253)
    sprite('bc610_10', 6)	# 2988-2993
    SFX_3('cloth_l')
    sprite('bc610_11', 6)	# 2994-2999
    sprite('bc610_12', 6)	# 3000-3005
    loopRest()
    gotoLabel(253)

@State
def CmnActLose():
    sprite('bc070_00', 6)	# 1-6
    if random_(2, 0, 50):
        SFX_1('pbc403_0')
    else:
        SFX_1('pbc403_1')
    Unknown23018(1)
    sprite('bc070_01', 6)	# 7-12
    sprite('bc070_02', 2)	# 13-14
    sprite('bc070_03', 32767)	# 15-32781

@State
def EventDefEntryWait():
    label(0)
    sprite('bn000_00', 7)	# 1-7
    sprite('bn000_01', 7)	# 8-14
    sprite('bn000_02', 7)	# 15-21
    sprite('bn000_03', 7)	# 22-28
    sprite('bn000_04', 7)	# 29-35
    sprite('bn000_05', 7)	# 36-42
    sprite('bn000_06', 7)	# 43-49
    sprite('bn000_07', 7)	# 50-56
    sprite('bn000_08', 7)	# 57-63
    sprite('bn000_09', 7)	# 64-70
    sprite('bn000_11', 7)	# 71-77
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
    sprite('bn620_13', 32767)	# 1-32767

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    loopRest()

@State
def EventStandReaction():
    sprite('bn001_00', 6)	# 1-6
    sprite('bn001_01', 6)	# 7-12
    sprite('bn001_02', 6)	# 13-18
    sprite('bn001_03', 6)	# 19-24
    sprite('bn001_04', 6)	# 25-30
    sprite('bn001_05', 5)	# 31-35
    sprite('bn001_06', 5)	# 36-40
    sprite('bn001_07', 5)	# 41-45
    sprite('bn001_08', 5)	# 46-50
    sprite('bn001_09', 6)	# 51-56
    sprite('bn001_10', 6)	# 57-62
    sprite('bn001_11', 6)	# 63-68
    loopRest()
    enterState('CmnActStand')

@State
def EventEntryFall():
    Unknown1000(-260000)
    teleportRelativeY(600000)
    sendToLabelUpon(2, 1)
    physicsYImpulse(-10000)
    Unknown1043()
    label(0)
    sprite('bn020_06', 3)	# 1-3
    sprite('bn020_07', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    sprite('bn024_00', 4)	# 7-10
    SFX_3('bnse_10')
    sprite('bn024_01', 6)	# 11-16
    sprite('bn024_02', 8)	# 17-24
    sprite('bn024_03', 6)	# 25-30
    sprite('bn024_04', 4)	# 31-34
    loopRest()
    enterState('CmnActStand')

@State
def EventSmokeOut():
    sprite('bn610_00', 3)	# 1-3
    Unknown2017(0)
    Unknown2034(0)
    sprite('bn610_01', 3)	# 4-6
    sprite('bn610_02', 3)	# 7-9
    sprite('bn610_03', 3)	# 10-12
    sprite('bn610_04', 3)	# 13-15
    sprite('bn610_05', 3)	# 16-18
    physicsYImpulse(25000)
    setGravity(1000)
    sprite('bn610_06', 3)	# 19-21
    sprite('bn610_07', 3)	# 22-24
    sprite('bn610_08', 3)	# 25-27
    sprite('bn610_09', 3)	# 28-30
    sprite('bn610_10', 3)	# 31-33
    sprite('bn610_11', 3)	# 34-36
    sprite('bn610_12', 3)	# 37-39
    sprite('bn610_13', 3)	# 40-42
    physicsYImpulse(0)
    setGravity(0)
    sprite('null', 120)	# 43-162
    GFX_0('bn_win', -1)
    SFX_3('bnse_06')
    loopRest()
    enterState('EventNoDisp')

@State
def EventWarp():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown2034(0)
        Unknown3032()
    sprite('keep', 26)	# 1-26
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    GFX_1('story_rc_teni', 103)
    sprite('keep', 1)	# 27-27
    Unknown1000(-500000)
    sprite('null', 32767)	# 28-32794
    loopRest()

@State
def EventYoroke():
    sprite('bn070_00', 6)	# 1-6
    sprite('bn070_01', 6)	# 7-12
    sprite('bn070_02', 6)	# 13-18
    sprite('bn070_03', 32767)	# 19-32785
    loopRest()

@State
def EventYorokeLoop():
    label(0)
    sprite('bn070_02', 6)	# 1-6
    sprite('bn070_03', 6)	# 7-12
    loopRest()
    gotoLabel(0)

@State
def EventYorokeStop():
    sprite('bn070_03', 32767)	# 1-32767

@State
def EventYorokeDown():
    sprite('bn070_02', 6)	# 1-6
    sprite('bn070_03', 6)	# 7-12
    sprite('bn070_04', 6)	# 13-18
    sprite('bn070_05', 6)	# 19-24
    sprite('bn070_06', 6)	# 25-30
    sprite('bn070_07', 6)	# 31-36
    sprite('bn070_08', 6)	# 37-42
    sprite('bn070_09', 6)	# 43-48
    sprite('bn063_11', 32767)	# 49-32815
    teleportRelativeX(140000)

@State
def EventYorokeDownToStand():
    sprite('bn064_00', 6)	# 1-6
    sprite('bn064_01', 6)	# 7-12
    sprite('bn064_02', 6)	# 13-18
    sprite('bn064_03', 6)	# 19-24
    sprite('bn064_04', 6)	# 25-30
    sprite('bn064_05', 6)	# 31-36
    sprite('bn064_06', 6)	# 37-42
    sprite('bn064_07', 6)	# 43-48
    sprite('bn064_08', 6)	# 49-54
    sprite('bn064_09', 6)	# 55-60
    sprite('bn064_10', 6)	# 61-66
    sprite('bn064_11', 6)	# 67-72
    loopRest()
    enterState('CmnActStand')

@State
def EventEntryFDashIn():
    Unknown2017(0)
    Unknown2034(0)
    Unknown1000(-1280000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 400000):
                sendToLabel(1)
        elif (SLOT_22 > (-400000)):
            sendToLabel(1)
    sprite('bn032_00', 1)	# 1-1
    Unknown8006(100, 1, 1)
    SFX_0('000_airdash_0')
    physicsXImpulse(21000)
    Unknown1028(200)
    label(0)
    sprite('bn032_01', 2)	# 2-3
    sprite('bn032_02', 2)	# 4-5
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 2)	# 6-7
    sprite('bn032_04', 2)	# 8-9
    sprite('bn032_05', 2)	# 10-11
    sprite('bn032_06', 2)	# 12-13
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 2)	# 14-15
    sprite('bn032_08', 2)	# 16-17
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('bn032_09', 3)	# 18-20
    Unknown1019(70)
    sprite('bn032_09', 3)	# 21-23
    Unknown1019(70)
    sprite('bn032_09', 3)	# 24-26
    Unknown1019(70)
    sprite('bn032_10', 3)	# 27-29
    Unknown1019(70)
    sprite('bn032_10', 6)	# 30-35
    Unknown1084(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def EventVSAM1():
    sprite('keep', 32767)	# 1-32767
    Unknown1000(-960000)
    Unknown2034(0)
    Unknown3038(1)

@State
def EventVSAM2():
    Unknown2034(0)
    sprite('bn430_00', 23)	# 1-23
    sprite('bn430_01', 4)	# 24-27
    SFX_0('000_airdash_2')
    sprite('bn430_02', 4)	# 28-31
    Unknown4049(2500)
    Unknown4045('626e65665f44445f315f736d6f6b650000000000000000000000000000000000ffffffff')
    sprite('bn430_03', 4)	# 32-35
    physicsXImpulse(29000)
    Unknown4049(2500)
    Unknown4045('626e65665f44445f315f736d6f6b650000000000000000000000000000000000ffffffff')
    sprite('bn430_04', 4)	# 36-39
    Unknown8006(100, 1, 1)
    sprite('bn430_05', 4)	# 40-43
    sprite('bn430_06', 4)	# 44-47
    sprite('bn430_49', 3)	# 48-50
    Unknown8006(100, 1, 0)
    SFX_3('bnse_10')
    Unknown1019(80)
    sprite('bn430_49', 3)	# 51-53
    Unknown8006(100, 1, 0)
    SFX_3('bnse_10')
    Unknown1019(80)
    sprite('bn430_49', 3)	# 54-56
    Unknown8006(100, 1, 0)
    SFX_3('bnse_10')
    Unknown1019(80)
    sprite('bn430_50', 3)	# 57-59
    Unknown1019(80)
    sprite('bn032_09', 2)	# 60-61
    Unknown8006(100, 1, 0)
    Unknown1019(80)
    sprite('bn032_09', 2)	# 62-63
    Unknown1019(60)
    sprite('bn032_10', 2)	# 64-65
    Unknown1019(60)
    sprite('bn000_00', 1)	# 66-66
    physicsXImpulse(0)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def EventPosesStandEntryWait():
    label(0)
    sprite('bn601_00', 5)	# 1-5
    sprite('bn601_01', 5)	# 6-10
    sprite('bn601_02', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def EventPosesStandEntry():
    sprite('bn601_01', 5)	# 1-5
    sprite('bn601_02', 5)	# 6-10
    sprite('bn601_03', 6)	# 11-16
    sprite('bn601_04', 6)	# 17-22
    sprite('bn601_05', 6)	# 23-28
    sprite('bn601_06', 6)	# 29-34
    sprite('bn601_07', 6)	# 35-40
    sprite('bn601_08', 6)	# 41-46
    sprite('bn601_09', 6)	# 47-52
    sprite('bn601_10', 6)	# 53-58
    sprite('bn601_11', 6)	# 59-64
    sprite('bn601_12', 6)	# 65-70
    sprite('bn601_13', 7)	# 71-77
    sprite('bn601_14', 7)	# 78-84
    sprite('bn601_15', 7)	# 85-91
    sprite('bn601_16', 6)	# 92-97
    loopRest()
    enterState('CmnActStand')

@State
def EventAttackVariation():
    sprite('bn200_00', 2)	# 1-2
    sprite('bn200_01', 1)	# 3-3
    sprite('bn200_01', 1)	# 4-4
    SFX_0('004_swing_grap_1_0')
    sprite('bn200_02', 3)	# 5-7
    sprite('bn200_03', 3)	# 8-10
    sprite('bn200_04', 2)	# 11-12
    sprite('bn200_04', 1)	# 13-13
    sprite('bn201_00', 2)	# 14-15
    sprite('bn201_01', 2)	# 16-17
    sprite('bn201_02', 2)	# 18-19
    sprite('bn201_03', 1)	# 20-20
    SFX_0('005_swing_grap_2_1')
    SFX_0('005_swing_grap_2_0')
    sprite('bn201_04', 4)	# 21-24
    sprite('bn201_05', 3)	# 25-27
    sprite('bn201_06', 3)	# 28-30
    sprite('bn201_07', 3)	# 31-33
    sprite('bn201_08', 3)	# 34-36
    sprite('bn201_09', 4)	# 37-40
    sprite('bn202_00', 4)	# 41-44
    sprite('bn202_01', 4)	# 45-48
    sprite('bn202_02', 3)	# 49-51
    sprite('bn202_03', 3)	# 52-54
    sprite('bn202_04', 3)	# 55-57
    sprite('bn202_05', 3)	# 58-60
    sprite('bn202_06', 3)	# 61-63
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_2')
    sprite('bn202_07', 2)	# 64-65
    sprite('bn202_08', 3)	# 66-68
    sprite('bn202_09', 2)	# 69-70
    sprite('bn202_10', 2)	# 71-72
    sprite('bn202_11', 2)	# 73-74
    sprite('bn202_12', 2)	# 75-76
    sprite('bn202_13', 2)	# 77-78
    sprite('bn202_14', 2)	# 79-80
    sprite('bn202_15', 2)	# 81-82
    sprite('bn202_16', 1)	# 83-83
    sprite('bn202_17', 1)	# 84-84
    loopRest()
    enterState('CmnActStand')

@State
def EventAttackVariationStop():
    sprite('bn200_00', 2)	# 1-2
    sprite('bn200_01', 1)	# 3-3
    sprite('bn200_01', 1)	# 4-4
    SFX_0('004_swing_grap_1_0')
    sprite('bn200_02', 3)	# 5-7
    sprite('bn200_03', 3)	# 8-10
    sprite('bn200_04', 2)	# 11-12
    sprite('bn200_04', 1)	# 13-13
    sprite('bn201_00', 2)	# 14-15
    sprite('bn201_01', 2)	# 16-17
    sprite('bn201_02', 2)	# 18-19
    sprite('bn201_03', 1)	# 20-20
    SFX_0('005_swing_grap_2_1')
    SFX_0('005_swing_grap_2_0')
    sprite('bn201_04', 60)	# 21-80
    sprite('bn201_05', 3)	# 81-83
    sprite('bn201_06', 3)	# 84-86
    sprite('bn201_07', 3)	# 87-89
    sprite('bn201_08', 3)	# 90-92
    sprite('bn201_09', 4)	# 93-96
    enterState('CmnActStand')

@State
def EventAttackVariationForLC():
    sprite('bn200_00', 2)	# 1-2
    sprite('bn200_01', 1)	# 3-3
    sprite('bn200_01', 1)	# 4-4
    SFX_0('004_swing_grap_1_0')
    sprite('bn200_02', 3)	# 5-7
    sprite('bn200_03', 3)	# 8-10
    sprite('bn200_04', 2)	# 11-12
    sprite('bn200_04', 1)	# 13-13
    sprite('bn200_00', 2)	# 14-15
    sprite('bn200_01', 1)	# 16-16
    sprite('bn200_01', 1)	# 17-17
    SFX_0('004_swing_grap_1_0')
    sprite('bn200_02', 3)	# 18-20
    sprite('bn200_03', 3)	# 21-23
    sprite('bn200_04', 2)	# 24-25
    sprite('bn200_04', 1)	# 26-26
    sprite('bn201_00', 2)	# 27-28
    sprite('bn201_01', 2)	# 29-30
    sprite('bn201_02', 2)	# 31-32
    sprite('bn201_03', 1)	# 33-33
    SFX_0('005_swing_grap_2_1')
    SFX_0('005_swing_grap_2_0')
    sprite('bn201_04', 4)	# 34-37
    sprite('bn201_05', 3)	# 38-40
    sprite('bn201_06', 3)	# 41-43
    sprite('bn201_07', 3)	# 44-46
    sprite('bn201_08', 3)	# 47-49
    sprite('bn201_09', 4)	# 50-53
    sprite('bn203_00', 2)	# 54-55
    sprite('bn203_01', 3)	# 56-58
    Unknown8000(100, 1, 1)
    sprite('bn203_02', 4)	# 59-62
    sprite('bn203_03', 3)	# 63-65
    sprite('bn203_04', 3)	# 66-68
    sprite('bn203_05', 2)	# 69-70
    physicsXImpulse(50000)
    Unknown8006(100, 1, 1)
    sprite('bn203_06', 2)	# 71-72
    Unknown1019(80)
    sprite('bn203_07', 2)	# 73-74
    Unknown8006(100, 1, 1)
    Unknown1019(80)
    sprite('bn203_08', 2)	# 75-76
    Unknown1019(50)
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_1')
    SFX_0('005_swing_grap_2_1')
    sprite('bn203_09', 4)	# 77-80
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('bn203_10', 3)	# 81-83
    sprite('bn203_11', 3)	# 84-86
    sprite('bn203_12', 2)	# 87-88
    sprite('bn203_13', 2)	# 89-90
    sprite('bn203_14', 2)	# 91-92
    sprite('bn203_15', 2)	# 93-94
    sprite('bn203_16', 3)	# 95-97
    sprite('bn203_17', 3)	# 98-100
    sprite('bn203_18', 2)	# 101-102
    sprite('bn203_19', 2)	# 103-104
    sprite('bn203_20', 1)	# 105-105
    sprite('bn203_21', 1)	# 106-106
    loopRest()
    enterState('CmnActStand')

@State
def EventBackStepForLC():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
    sprite('bn033_00', 2)	# 1-2
    sprite('bn033_01', 2)	# 3-4
    physicsXImpulse(-10000)
    sprite('bn033_02', 2)	# 5-6
    sprite('bn033_03', 2)	# 7-8
    sprite('bn033_04', 1)	# 9-9
    sprite('bn033_04', 1)	# 10-10
    sprite('bn033_05', 2)	# 11-12
    sprite('bn033_06', 3)	# 13-15
    physicsXImpulse(-12000)
    physicsYImpulse(11000)
    setGravity(1650)
    SFX_3('bnse_08')
    sprite('bn033_07', 3)	# 16-18
    sprite('bn033_08', 3)	# 19-21
    sprite('bn033_09', 3)	# 22-24
    sprite('bn033_10', 3)	# 25-27
    label(1)
    clearUponHandler(2)
    sprite('bn033_11', 3)	# 28-30
    Unknown1019(50)
    sprite('bn033_12', 3)	# 31-33
    Unknown1000(-260000)
    physicsXImpulse(0)
    SFX_3('bnse_09')
    Unknown8000(100, 1, 1)
    sprite('bn033_13', 3)	# 34-36
    enterState('CmnActStand')

@State
def EventSmokeEntryWait():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    gotoLabel(0)

@State
def EventSmokeEntry():
    sendToLabelUpon(2, 1)
    sprite('null', 1)	# 1-1
    GFX_0('bn_win', -1)
    SFX_3('bnse_06')
    setGravity(1000)
    teleportRelativeY(200000)
    label(0)
    sprite('bn610_08', 3)	# 2-4
    sprite('bn610_09', 3)	# 5-7
    sprite('bn610_10', 3)	# 8-10
    sprite('bn610_11', 3)	# 11-13
    sprite('bn610_12', 3)	# 14-16
    sprite('bn610_13', 3)	# 17-19
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bn610_07', 3)	# 20-22
    Unknown8000(100, 1, 1)
    sprite('bn610_04', 3)	# 23-25
    sprite('bn610_03', 3)	# 26-28
    sprite('bn610_02', 3)	# 29-31
    sprite('bn610_01', 3)	# 32-34
    sprite('bn610_00', 3)	# 35-37
    loopRest()
    enterState('CmnActStand')

@State
def EventLoseReverse():
    sprite('bn620_13', 6)	# 1-6
    sprite('bn620_12', 6)	# 7-12
    sprite('bn620_11', 6)	# 13-18
    sprite('bn620_10', 6)	# 19-24
    sprite('bn620_09', 6)	# 25-30
    sprite('bn620_08', 6)	# 31-36
    sprite('bn620_07', 6)	# 37-42
    sprite('bn620_06', 6)	# 43-48
    sprite('bn620_05', 6)	# 49-54
    sprite('bn620_04', 6)	# 55-60
    sprite('bn620_03', 6)	# 61-66
    sprite('bn620_02', 6)	# 67-72
    sprite('bn620_01', 6)	# 73-78
    sprite('bn620_00', 6)	# 79-84
    loopRest()
    enterState('CmnActStand')

@State
def EventExcite():
    sprite('bn300_00', 4)	# 1-4
    sprite('bn300_01', 4)	# 5-8
    sprite('bn300_02', 6)	# 9-14
    sprite('bn300_03', 6)	# 15-20
    sprite('bn300_04', 4)	# 21-24
    sprite('bn300_05', 4)	# 25-28
    SFX_0('100_hit_grap_1')
    sprite('bn300_06', 6)	# 29-34
    sprite('bn300_07', 6)	# 35-40
    sprite('bn300_08', 6)	# 41-46
    sprite('bn300_09', 6)	# 47-52
    sprite('bn300_10', 6)	# 53-58
    sprite('bn300_11', 6)	# 59-64
    sprite('bn300_12', 6)	# 65-70
    SFX_0('200_walk_normal_1')
    sprite('bn300_13', 6)	# 71-76
    sprite('bn300_14', 6)	# 77-82
    sprite('bn300_15', 6)	# 83-88
    sprite('bn300_16', 6)	# 89-94
    sprite('bn300_14', 6)	# 95-100
    sprite('bn300_15', 6)	# 101-106
    sprite('bn300_16', 6)	# 107-112
    sprite('bn300_14', 6)	# 113-118
    sprite('bn300_15', 6)	# 119-124
    sprite('bn300_16', 6)	# 125-130
    sprite('bn300_14', 6)	# 131-136
    sprite('bn300_15', 6)	# 137-142
    sprite('bn300_16', 6)	# 143-148
    sprite('bn300_14', 6)	# 149-154
    sprite('bn300_15', 6)	# 155-160
    sprite('bn300_16', 6)	# 161-166
    sprite('bn300_17', 6)	# 167-172
    sprite('bn300_18', 6)	# 173-178
    sprite('bn300_19', 6)	# 179-184
    loopRest()
    enterState('CmnActStand')

@State
def EventGutsPoses():
    sprite('bn615_00', 3)	# 1-3
    sprite('bn615_01', 3)	# 4-6
    sprite('bn615_02', 3)	# 7-9
    sprite('bn615_03', 3)	# 10-12
    sprite('bn615_04', 3)	# 13-15
    sprite('bn615_05', 3)	# 16-18
    sprite('bn615_06', 3)	# 19-21
    sprite('bn615_07', 3)	# 22-24
    sprite('bn615_08', 3)	# 25-27
    sprite('bn615_09', 3)	# 28-30
    sprite('bn615_10', 3)	# 31-33
    sprite('bn615_11', 3)	# 34-36
    sprite('bn615_10', 3)	# 37-39
    sprite('bn615_11', 3)	# 40-42
    sprite('bn615_10', 3)	# 43-45
    sprite('bn615_11', 3)	# 46-48
    sprite('bn615_12', 3)	# 49-51
    sprite('bn615_13', 3)	# 52-54
    sprite('bn615_12', 3)	# 55-57
    sprite('bn615_13', 3)	# 58-60
    sprite('bn615_12', 3)	# 61-63
    sprite('bn615_13', 3)	# 64-66
    sprite('bn615_14', 3)	# 67-69
    sprite('bn615_15', 3)	# 70-72
    sprite('bn615_16', 3)	# 73-75
    label(0)
    sprite('bn615_14', 4)	# 76-79
    sprite('bn615_15', 4)	# 80-83
    sprite('bn615_16', 4)	# 84-87
    loopRest()
    gotoLabel(0)

@State
def EventGutsPosesToStand():
    sprite('bn615_16', 3)	# 1-3
    sprite('bn615_15', 3)	# 4-6
    sprite('bn615_14', 3)	# 7-9
    sprite('bn615_13', 3)	# 10-12
    sprite('bn615_11', 3)	# 13-15
    sprite('bn615_09', 3)	# 16-18
    sprite('bn615_08', 3)	# 19-21
    sprite('bn615_07', 3)	# 22-24
    sprite('bn615_00', 3)	# 25-27
    loopRest()
    enterState('CmnActStand')

@State
def EventWalkScreenOut():
    sprite('bn030_00', 7)	# 1-7
    Unknown2034(0)
    Unknown2017(0)
    physicsXImpulse(10000)
    sprite('bn030_01', 7)	# 8-14
    label(0)
    sprite('bn030_02', 7)	# 15-21
    sprite('bn030_03', 7)	# 22-28
    sprite('bn030_04', 7)	# 29-35
    sprite('bn030_05', 7)	# 36-42
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('bnse_10')
    sprite('bn030_06', 7)	# 43-49
    sprite('bn030_07', 7)	# 50-56
    sprite('bn030_08', 7)	# 57-63
    sprite('bn030_01', 7)	# 64-70
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('bnse_10')
    loopRest()
    gotoLabel(0)

@State
def EventDashScreenRunaway():
    sprite('bn032_08', 1)	# 1-1
    Unknown2005()
    Unknown2034(0)
    Unknown2017(0)
    sprite('bn032_01', 3)	# 2-4
    physicsXImpulse(32000)
    sprite('bn032_02', 3)	# 5-7
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 8-10
    sprite('bn032_04', 3)	# 11-13
    sprite('bn032_05', 3)	# 14-16
    sprite('bn032_06', 3)	# 17-19
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 20-22
    sprite('bn032_08', 3)	# 23-25
    loopRest()
    label(0)
    sprite('bn032_01', 3)	# 26-28
    sprite('bn032_02', 3)	# 29-31
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 32-34
    sprite('bn032_04', 3)	# 35-37
    sprite('bn032_05', 3)	# 38-40
    sprite('bn032_06', 3)	# 41-43
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 44-46
    sprite('bn032_08', 3)	# 47-49
    loopRest()
    gotoLabel(0)

@State
def EventBNVsAZ_EntryWalkIn0():
    Unknown2017(0)
    Unknown2034(0)
    Unknown1000(-2800000)
    sprite('bn030_00', 8)	# 1-8
    physicsXImpulse(4500)
    Unknown20000(1)
    sprite('bn030_01', 7)	# 9-15
    label(0)
    sprite('bn030_02', 7)	# 16-22
    sprite('bn030_03', 7)	# 23-29
    sprite('bn030_04', 7)	# 30-36
    sprite('bn030_05', 7)	# 37-43
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('bnse_10')
    sprite('bn030_06', 7)	# 44-50
    sprite('bn030_07', 7)	# 51-57
    sprite('bn030_08', 7)	# 58-64
    sprite('bn030_01', 7)	# 65-71
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('bnse_10')
    loopRest()
    gotoLabel(0)

@State
def EventBNVsAZ_EntryWalkIn1():
    Unknown1084(1)
    Unknown20000(1)
    Unknown2017(0)
    Unknown2034(0)
    label(0)
    sprite('bn000_00', 7)	# 1-7
    sprite('bn000_01', 7)	# 8-14
    sprite('bn000_02', 7)	# 15-21
    sprite('bn000_03', 7)	# 22-28
    sprite('bn000_04', 7)	# 29-35
    sprite('bn000_05', 7)	# 36-42
    sprite('bn000_06', 7)	# 43-49
    sprite('bn000_07', 7)	# 50-56
    sprite('bn000_08', 7)	# 57-63
    sprite('bn000_09', 7)	# 64-70
    sprite('bn000_11', 7)	# 71-77
    loopRest()
    gotoLabel(0)

@State
def EventBNVsAZ_EntryWalkIn2():
    Unknown20000(1)
    Unknown2017(0)
    Unknown2034(0)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 320000):
                sendToLabel(1)
        elif (SLOT_22 > (-320000)):
            sendToLabel(1)
    sprite('bn032_00', 2)	# 1-2
    SFX_3('bnse_08')
    sprite('bn032_01', 1)	# 3-3
    physicsXImpulse(18000)
    loopRest()
    label(0)
    sprite('bn032_01', 3)	# 4-6
    sprite('bn032_02', 3)	# 7-9
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 10-12
    sprite('bn032_04', 3)	# 13-15
    sprite('bn032_05', 3)	# 16-18
    sprite('bn032_06', 3)	# 19-21
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 22-24
    sprite('bn032_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('bn032_09', 2)	# 28-29
    Unknown1019(50)
    sprite('bn032_10', 2)	# 30-31
    Unknown1019(50)
    Unknown20000(0)
    sprite('bn000_00', 1)	# 32-32
    Unknown1084(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def EventBNVsLC_WeepStart():
    sprite('bn061_10', 3)	# 1-3
    sprite('bn061_09', 3)	# 4-6
    sprite('bn061_08', 3)	# 7-9
    sprite('bn061_07', 3)	# 10-12
    sprite('bn061_06', 3)	# 13-15
    sprite('bn061_05', 3)	# 16-18
    sprite('bn061_04', 3)	# 19-21
    sprite('bn061_03', 3)	# 22-24
    sprite('bn061_02', 32767)	# 25-32791
    loopRest()

@State
def EventBNVsLC_WeepEnd():
    sprite('bn061_03', 4)	# 1-4
    sprite('bn061_04', 4)	# 5-8
    sprite('bn061_05', 4)	# 9-12
    sprite('bn061_06', 4)	# 13-16
    sprite('bn061_07', 4)	# 17-20
    sprite('bn061_08', 4)	# 21-24
    sprite('bn061_09', 4)	# 25-28
    sprite('bn061_10', 4)	# 29-32
    loopRest()
    enterState('CmnActStand')

@State
def EventBNVsLC_FurinkazanStart():
    sprite('bn432_00', 4)	# 1-4
    sprite('bn432_01', 5)	# 5-9
    sprite('bn432_02', 5)	# 10-14
    sprite('bn432_03', 5)	# 15-19
    sprite('bn432_04', 5)	# 20-24
    sprite('bn432_05', 5)	# 25-29
    sprite('bn432_06', 5)	# 30-34
    sprite('bn432_07', 5)	# 35-39
    sprite('bn432_08', 5)	# 40-44
    sprite('bn432_09', 5)	# 45-49
    sprite('bn432_10', 5)	# 50-54
    sprite('bn432_11', 5)	# 55-59
    sprite('bn432_12', 5)	# 60-64
    SFX_3('bnse_04')
    SFX_3('bnse_05')
    sprite('bn432_13', 4)	# 65-68
    sprite('bn432_14', 4)	# 69-72
    sprite('bn432_15', 69)	# 73-141
    sprite('bn432_16', 6)	# 142-147
    sprite('bn432_17', 6)	# 148-153
    sprite('bn432_18', 7)	# 154-160
    sprite('bn432_19', 7)	# 161-167
    sprite('bn432_20', 15)	# 168-182
    sprite('bn432_21', 6)	# 183-188
    GFX_0('bn_DD_3_ray', -1)
    physicsYImpulse(7000)
    sprite('bn432_22', 3)	# 189-191
    sprite('bn432_23', 3)	# 192-194
    sprite('bn432_24', 3)	# 195-197
    sprite('bn432_25', 3)	# 198-200
    sprite('bn432_26', 3)	# 201-203
    sprite('bn432_23', 3)	# 204-206
    physicsYImpulse(0)
    sprite('bn432_24', 3)	# 207-209
    sprite('bn432_25', 3)	# 210-212
    sprite('bn432_26', 3)	# 213-215
    sprite('bn432_23', 3)	# 216-218
    sprite('bn432_24', 3)	# 219-221
    sprite('bn432_25', 3)	# 222-224
    sprite('bn432_26', 3)	# 225-227
    loopRest()
    label(0)
    sprite('bn432_23', 3)	# 228-230
    sprite('bn432_24', 3)	# 231-233
    sprite('bn432_25', 3)	# 234-236
    sprite('bn432_26', 3)	# 237-239
    loopRest()
    gotoLabel(0)

@State
def EventBNVsLC_FurinkazanEnd():
    sprite('bn432_27', 3)	# 1-3
    setGravity(1450)
    sprite('bn432_28', 3)	# 4-6
    sprite('bn432_29', 3)	# 7-9
    sprite('bn432_30', 3)	# 10-12
    sprite('bn432_31', 3)	# 13-15
    sprite('bn432_32', 3)	# 16-18
    SFX_3('bnse_10')
    Unknown8000(100, 1, 1)
    sprite('bn432_33', 3)	# 19-21
    sprite('bn432_34', 3)	# 22-24
    sprite('bn432_35', 3)	# 25-27
    sprite('bn432_36', 6)	# 28-33
    sprite('bn432_37', 5)	# 34-38
    sprite('bn432_38', 4)	# 39-42
    teleportRelativeX(-40000)
    sprite('bn432_39', 4)	# 43-46
    teleportRelativeX(-40000)
    loopRest()
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventBNAppear():
    sprite('bn601_00', 5)	# 1-5
    Unknown3038(0)
    Unknown3001(0)
    SFX_0('000_airdash_0')
    Unknown3004(5)
    sprite('bn601_01', 5)	# 6-10
    sprite('bn601_02', 5)	# 11-15
    label(0)
    sprite('bn601_00', 5)	# 16-20
    sprite('bn601_01', 5)	# 21-25
    sprite('bn601_02', 5)	# 26-30
    loopRest()
    gotoLabel(0)

@State
def EventBNDown():
    sprite('bn063_11', 32767)	# 1-32767

@State
def EventBNDisappear():
    sprite('bn063_11', 30)	# 1-30
    sprite('bn063_11', 32767)	# 31-32797
    Unknown3004(-5)
    SFX_0('000_airdash_2')

@State
def EventCrounch():
    label(0)
    sprite('bn010_02', 6)	# 1-6
    sprite('bn010_03', 6)	# 7-12
    sprite('bn010_04', 6)	# 13-18
    sprite('bn010_05', 6)	# 19-24
    sprite('bn010_06', 6)	# 25-30
    sprite('bn010_07', 6)	# 31-36
    sprite('bn010_08', 6)	# 37-42
    sprite('bn010_09', 6)	# 43-48
    sprite('bn010_10', 6)	# 49-54
    sprite('bn010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def EventCrounchToStand():
    sprite('bn010_01', 4)	# 1-4
    sprite('bn010_00', 4)	# 5-8
    enterState('CmnActStand')

@State
def EventBNvdTB_EntryWait():
    Unknown2017(0)
    Unknown2034(0)
    Unknown20000(1)
    sprite('null', 32767)	# 1-32767
    Unknown1000(-2800000)
    Unknown3038(1)
    loopRest()

@State
def EventBNvdTB_EntryWalkIn01():
    Unknown2017(0)
    Unknown2034(0)
    Unknown1000(-3200000)
    loopRelated(17, 120)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    sprite('bn030_00', 8)	# 1-8
    physicsXImpulse(4500)
    Unknown20000(1)
    sprite('bn030_01', 7)	# 9-15
    sprite('bn030_01', 7)	# 16-22
    label(0)
    sprite('bn030_02', 7)	# 23-29
    sprite('bn030_03', 7)	# 30-36
    sprite('bn030_04', 7)	# 37-43
    sprite('bn030_05', 7)	# 44-50
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('bnse_10')
    sprite('bn030_06', 7)	# 51-57
    sprite('bn030_07', 7)	# 58-64
    sprite('bn030_08', 7)	# 65-71
    sprite('bn030_01', 7)	# 72-78
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('bnse_10')
    loopRest()
    gotoLabel(0)
    label(1)
    enterState('EventBNVsAZ_EntryWalkIn1')

@State
def EventBNvdTBEnemyCamera():

    def upon_IMMEDIATE():
        loopRelated(17, 280)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown20000(1)
        Unknown2017(0)
        Unknown2034(0)
    sprite('bn000_00', 7)	# 1-7
    GFX_0('EventBNvsTBStandLC', -1)
    Unknown36(1)
    Unknown1000(-280000)
    Unknown35()
    label(0)
    sprite('bn000_01', 7)	# 8-14
    sprite('bn000_02', 7)	# 15-21
    sprite('bn000_03', 7)	# 22-28
    sprite('bn000_04', 7)	# 29-35
    sprite('bn000_05', 7)	# 36-42
    sprite('bn000_06', 7)	# 43-49
    sprite('bn000_07', 7)	# 50-56
    sprite('bn000_08', 7)	# 57-63
    sprite('bn000_09', 7)	# 64-70
    sprite('bn000_11', 7)	# 71-77
    sprite('bn000_00', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bn000_01', 3)	# 85-87
    Unknown20000(0)
    loopRest()

@State
def EventRunIn():
    Unknown2034(0)
    Unknown2037(1)
    Unknown2017(0)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            sendToLabel(1)
    sprite('bn032_01', 3)	# 1-3
    physicsXImpulse(25000)
    label(0)
    sprite('bn032_02', 3)	# 4-6
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 7-9
    sprite('bn032_04', 3)	# 10-12
    sprite('bn032_05', 3)	# 13-15
    sprite('bn032_06', 3)	# 16-18
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 19-21
    sprite('bn032_08', 3)	# 22-24
    sprite('bn032_01', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventBNvsTB5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('bn203_00', 4)	# 1-4
    setInvincible(1)
    Unknown1000(-160000)
    sprite('bn203_01', 1)	# 5-5
    sprite('bn203_01', 2)	# 6-7
    GFX_0('bn_D_stand', -1)
    Unknown8000(100, 1, 1)
    sprite('bn203_02', 3)	# 8-10
    sprite('bn203_03', 3)	# 11-13
    sprite('bn203_04', 2)	# 14-15
    sprite('bn203_05', 1)	# 16-16
    physicsXImpulse(80000)
    Unknown8006(100, 1, 1)
    sprite('bn203_06', 1)	# 17-17
    Unknown1019(80)
    sprite('bn203_07', 2)	# 18-19
    Unknown8006(100, 1, 1)
    Unknown1019(40)
    GFX_0('bn_D_stand2', -1)
    sprite('bn203_08', 2)	# 20-21
    Unknown1019(50)
    SFX_0('005_swing_grap_2_2')
    sprite('bn203_09', 3)	# 22-24
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    Unknown21012('4576656e74424e767354425374616e644c43000000000000000000000000000020000000')
    sprite('bn203_10', 3)	# 25-27
    sprite('bn203_11', 3)	# 28-30
    sprite('bn203_12', 3)	# 31-33
    sprite('bn203_13', 3)	# 34-36
    sprite('bn203_14', 3)	# 37-39
    sprite('bn203_15', 3)	# 40-42
    sprite('bn203_16', 3)	# 43-45
    loopRest()
    enterState('EventBackStepForLC')

@State
def EventBGvsTBRunIn():
    Unknown2034(0)
    Unknown2037(1)
    Unknown2017(0)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 160000):
                Unknown2037(0)
                clearUponHandler(3)
                sendToLabel(1)
        elif (SLOT_22 > (-100000)):
            clearUponHandler(3)
            sendToLabel(1)
    sprite('bn032_01', 3)	# 1-3
    physicsXImpulse(25000)
    label(0)
    sprite('bn032_02', 3)	# 4-6
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 7-9
    sprite('bn032_04', 3)	# 10-12
    sprite('bn032_05', 3)	# 13-15
    sprite('bn032_06', 3)	# 16-18
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 19-21
    sprite('bn032_08', 3)	# 22-24
    sprite('bn032_01', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 28-29
    Unknown1084(1)
    loopRest()
    enterState('CmnActStand')

@State
def EventStrike():
    sprite('bn404_00', 3)	# 1-3
    sprite('bn404_01', 3)	# 4-6
    sprite('bn404_02', 3)	# 7-9
    sprite('bn404_03', 2)	# 10-11
    GFX_0('bn_strike', -1)
    sprite('bn404_04', 2)	# 12-13
    sprite('bn404_05', 2)	# 14-15
    Unknown21007(22, 32)
    sprite('bn404_06', 2)	# 16-17
    SFX_0('004_swing_grap_1_1')
    SFX_0('003_swing_grap_0_1')
    sprite('bn404_07', 3)	# 18-20
    sprite('bn404_08', 3)	# 21-23
    sprite('bn404_09', 3)	# 24-26
    sprite('bn404_10', 2)	# 27-28
    sprite('bn404_11', 2)	# 29-30
    sprite('bn404_12', 2)	# 31-32
    sprite('bn404_13', 2)	# 33-34
    sprite('bn404_14', 2)	# 35-36
    sprite('bn404_15', 2)	# 37-38
    loopRest()
    enterState('CmnActStand')

@State
def EventStandTurn():
    sprite('bn003_00', 3)	# 1-3
    Unknown2005()
    sprite('bn003_01', 3)	# 4-6
    sprite('bn003_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('bn000_01', 7)	# 10-16
    sprite('bn000_02', 7)	# 17-23
    sprite('bn000_03', 7)	# 24-30
    sprite('bn000_04', 7)	# 31-37
    sprite('bn000_05', 7)	# 38-44
    sprite('bn000_06', 7)	# 45-51
    sprite('bn000_07', 7)	# 52-58
    sprite('bn000_08', 7)	# 59-65
    sprite('bn000_09', 7)	# 66-72
    sprite('bn000_11', 7)	# 73-79
    sprite('bn000_00', 7)	# 80-86
    loopRest()
    gotoLabel(0)

@State
def EventStandTurnEnd():
    sprite('bn003_00', 3)	# 1-3
    Unknown2005()
    sprite('bn003_01', 3)	# 4-6
    sprite('bn003_02', 3)	# 7-9
    loopRest()
    enterState('CmnActStand')

@State
def EventStandWithLC():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        GFX_0('EventBNvsTBStandLC', -1)
        Unknown36(1)
        Unknown1000(-300000)
        Unknown35()
    label(0)
    sprite('bn000_01', 7)	# 1-7
    sprite('bn000_02', 7)	# 8-14
    sprite('bn000_03', 7)	# 15-21
    sprite('bn000_04', 7)	# 22-28
    sprite('bn000_05', 7)	# 29-35
    sprite('bn000_06', 7)	# 36-42
    sprite('bn000_07', 7)	# 43-49
    sprite('bn000_08', 7)	# 50-56
    sprite('bn000_09', 7)	# 57-63
    sprite('bn000_11', 7)	# 64-70
    sprite('bn000_00', 7)	# 71-77
    loopRest()
    gotoLabel(0)

@State
def EventRunEntry():
    Unknown2034(0)
    Unknown2037(1)
    Unknown2017(0)
    Unknown1000(-900000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            sendToLabel(1)
    sprite('bn032_01', 3)	# 1-3
    physicsXImpulse(32000)
    label(0)
    sprite('bn032_02', 3)	# 4-6
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 7-9
    sprite('bn032_04', 3)	# 10-12
    sprite('bn032_05', 3)	# 13-15
    sprite('bn032_06', 3)	# 16-18
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 19-21
    sprite('bn032_08', 3)	# 22-24
    sprite('bn032_01', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventExciteLoop():
    sprite('bn300_00', 4)	# 1-4
    sprite('bn300_01', 4)	# 5-8
    sprite('bn300_02', 6)	# 9-14
    sprite('bn300_03', 6)	# 15-20
    sprite('bn300_04', 4)	# 21-24
    sprite('bn300_05', 4)	# 25-28
    SFX_0('100_hit_grap_1')
    sprite('bn300_06', 6)	# 29-34
    sprite('bn300_07', 6)	# 35-40
    sprite('bn300_08', 6)	# 41-46
    sprite('bn300_09', 6)	# 47-52
    sprite('bn300_10', 6)	# 53-58
    sprite('bn300_11', 6)	# 59-64
    sprite('bn300_12', 6)	# 65-70
    SFX_0('200_walk_normal_1')
    sprite('bn300_13', 6)	# 71-76
    label(0)
    sprite('bn300_14', 6)	# 77-82
    sprite('bn300_15', 6)	# 83-88
    sprite('bn300_16', 6)	# 89-94
    loopRest()
    gotoLabel(0)

@State
def EventExciteLoopEnd():
    sprite('bn300_17', 6)	# 1-6
    sprite('bn300_18', 6)	# 7-12
    sprite('bn300_19', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Headache():
    sprite('bn620_00', 4)	# 1-4
    sprite('bn620_01', 18)	# 5-22
    GFX_0('Event_Headache', -1)
    ScreenShake(0, 3000)
    sprite('bn620_01', 6)	# 23-28
    sprite('bn620_00', 6)	# 29-34
    sprite('bn001_00', 7)	# 35-41
    sprite('bn001_01', 7)	# 42-48
    sprite('bn001_02', 7)	# 49-55
    sprite('bn001_03', 7)	# 56-62
    sprite('bn001_04', 7)	# 63-69
    sprite('bn001_05', 7)	# 70-76
    sprite('bn001_06', 7)	# 77-83
    sprite('bn001_07', 7)	# 84-90
    sprite('bn001_08', 7)	# 91-97
    sprite('bn001_09', 7)	# 98-104
    sprite('bn001_10', 7)	# 105-111
    sprite('bn001_11', 7)	# 112-118
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventReaction():
    sprite('bn001_00', 6)	# 1-6
    sprite('bn001_01', 6)	# 7-12
    sprite('bn001_02', 6)	# 13-18
    sprite('bn001_03', 6)	# 19-24
    sprite('bn001_04', 6)	# 25-30
    sprite('bn001_05', 5)	# 31-35
    sprite('bn001_06', 5)	# 36-40
    sprite('bn001_07', 5)	# 41-45
    sprite('bn001_08', 5)	# 46-50
    sprite('bn001_09', 6)	# 51-56
    sprite('bn001_10', 6)	# 57-62
    sprite('bn001_11', 6)	# 63-68
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventExcite():
    sprite('bn300_00', 4)	# 1-4
    sprite('bn300_01', 4)	# 5-8
    sprite('bn300_02', 6)	# 9-14
    sprite('bn300_03', 6)	# 15-20
    sprite('bn300_04', 4)	# 21-24
    sprite('bn300_05', 4)	# 25-28
    SFX_0('100_hit_grap_1')
    sprite('bn300_06', 6)	# 29-34
    sprite('bn300_07', 6)	# 35-40
    sprite('bn300_08', 6)	# 41-46
    sprite('bn300_09', 6)	# 47-52
    sprite('bn300_10', 6)	# 53-58
    sprite('bn300_11', 6)	# 59-64
    sprite('bn300_12', 6)	# 65-70
    SFX_0('200_walk_normal_1')
    sprite('bn300_13', 6)	# 71-76
    sprite('bn300_14', 6)	# 77-82
    sprite('bn300_15', 6)	# 83-88
    sprite('bn300_16', 6)	# 89-94
    sprite('bn300_14', 6)	# 95-100
    sprite('bn300_15', 6)	# 101-106
    sprite('bn300_16', 6)	# 107-112
    sprite('bn300_14', 6)	# 113-118
    sprite('bn300_15', 6)	# 119-124
    sprite('bn300_16', 6)	# 125-130
    sprite('bn300_14', 6)	# 131-136
    sprite('bn300_15', 6)	# 137-142
    sprite('bn300_16', 6)	# 143-148
    sprite('bn300_14', 6)	# 149-154
    sprite('bn300_15', 6)	# 155-160
    sprite('bn300_16', 6)	# 161-166
    sprite('bn300_17', 6)	# 167-172
    sprite('bn300_18', 6)	# 173-178
    sprite('bn300_19', 6)	# 179-184
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventLose():
    sprite('bn620_13', 32767)	# 1-32767

@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_LoseToDown():
    sprite('bn063_07', 7)	# 1-7
    sprite('bn063_08', 7)	# 8-14
    sprite('bn063_09', 7)	# 15-21
    sprite('bn063_10', 7)	# 22-28
    GFX_1('ef_grndshock', 104)
    SFX_0('209_down_normal_0')
    sprite('bn063_11', 32767)	# 29-32795
    loopRest()

@State
def Act2EventEntryFDashIn():
    Unknown2017(0)
    Unknown2034(0)
    Unknown1000(-1280000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 400000):
                sendToLabel(1)
        elif (SLOT_22 > (-400000)):
            sendToLabel(1)
    sprite('bn032_00', 1)	# 1-1
    Unknown8006(100, 1, 1)
    SFX_0('000_airdash_0')
    physicsXImpulse(21000)
    Unknown1028(200)
    label(0)
    sprite('bn032_01', 2)	# 2-3
    sprite('bn032_02', 2)	# 4-5
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 2)	# 6-7
    sprite('bn032_04', 2)	# 8-9
    sprite('bn032_05', 2)	# 10-11
    sprite('bn032_06', 2)	# 12-13
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 2)	# 14-15
    sprite('bn032_08', 2)	# 16-17
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('bn032_09', 3)	# 18-20
    Unknown1019(70)
    sprite('bn032_09', 3)	# 21-23
    Unknown1019(70)
    sprite('bn032_09', 3)	# 24-26
    Unknown1019(70)
    sprite('bn032_10', 3)	# 27-29
    Unknown1019(70)
    sprite('bn032_10', 6)	# 30-35
    Unknown1084(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_RoundWin():
    sprite('bn615_00', 3)	# 1-3
    sprite('bn615_01', 3)	# 4-6
    sprite('bn615_02', 3)	# 7-9
    sprite('bn615_03', 3)	# 10-12
    sprite('bn615_04', 3)	# 13-15
    sprite('bn615_05', 3)	# 16-18
    sprite('bn615_06', 3)	# 19-21
    sprite('bn615_07', 3)	# 22-24
    sprite('bn615_08', 3)	# 25-27
    sprite('bn615_09', 3)	# 28-30
    sprite('bn615_10', 3)	# 31-33
    sprite('bn615_12', 3)	# 34-36
    sprite('bn615_14', 3)	# 37-39
    sprite('bn615_15', 3)	# 40-42
    sprite('bn615_16', 3)	# 43-45
    label(0)
    sprite('bn615_14', 4)	# 46-49
    sprite('bn615_15', 4)	# 50-53
    sprite('bn615_16', 4)	# 54-57
    loopRest()
    gotoLabel(0)

@State
def Act2Event_RoundWinLoop():
    label(0)
    sprite('bn615_14', 4)	# 1-4
    sprite('bn615_15', 4)	# 5-8
    sprite('bn615_16', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def Act2Event_RoundWinEnd():
    sprite('keep', 2)	# 1-2
    sprite('bn615_13', 3)	# 3-5
    sprite('bn615_11', 3)	# 6-8
    sprite('bn615_09', 3)	# 9-11
    sprite('bn615_08', 3)	# 12-14
    sprite('bn615_07', 3)	# 15-17
    sprite('bn615_00', 3)	# 18-20
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_bnvstk_00():
    sprite('bn030_00', 7)	# 1-7
    physicsXImpulse(4500)
    sprite('bn030_01', 7)	# 8-14
    sprite('bn030_02', 7)	# 15-21
    sprite('bn030_03', 7)	# 22-28
    sprite('bn030_04', 7)	# 29-35
    sprite('bn030_05', 7)	# 36-42
    sprite('bn010_00', 4)	# 43-46
    Unknown1084(1)
    sprite('bn010_01', 4)	# 47-50
    label(0)
    sprite('bn010_02', 6)	# 51-56
    sprite('bn010_03', 6)	# 57-62
    sprite('bn010_04', 6)	# 63-68
    sprite('bn010_05', 6)	# 69-74
    sprite('bn010_06', 6)	# 75-80
    sprite('bn010_07', 6)	# 81-86
    sprite('bn010_08', 6)	# 87-92
    sprite('bn010_09', 6)	# 93-98
    sprite('bn010_10', 6)	# 99-104
    sprite('bn010_11', 6)	# 105-110
    loopRest()
    gotoLabel(0)

@State
def Act2Event_bnvstk_01():
    sprite('keep', 2)	# 1-2
    sprite('bn010_01', 4)	# 3-6
    sprite('bn010_00', 4)	# 7-10
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_bnvstk_02():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('bn032_00', 3)	# 1-3
    sprite('bn032_01', 3)	# 4-6
    SFX_0('000_airdash_0')
    physicsXImpulse(32000)
    sprite('bn032_02', 3)	# 7-9
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 10-12
    sprite('bn032_04', 3)	# 13-15
    sprite('bn032_05', 3)	# 16-18
    sprite('bn032_06', 3)	# 19-21
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 22-24
    sprite('bn032_08', 3)	# 25-27
    loopRest()
    label(0)
    sprite('bn032_01', 3)	# 28-30
    sprite('bn032_02', 3)	# 31-33
    sprite('bn032_03', 3)	# 34-36
    sprite('bn032_04', 3)	# 37-39
    sprite('bn032_05', 3)	# 40-42
    sprite('bn032_06', 3)	# 43-45
    sprite('bn032_07', 3)	# 46-48
    sprite('bn032_08', 3)	# 49-51
    loopRest()
    gotoLabel(0)

@State
def Act2Event_bnvsjn_00():

    def upon_IMMEDIATE():
        teleportRelativeY(360000)
        Unknown1000(-960000)
        Unknown2017(0)
        Unknown2034(0)
        Unknown20000(1)

        def upon_LANDING():
            Unknown1084(1)
            sendToLabel(0)
    sprite('bn600_03', 4)	# 1-4
    physicsXImpulse(3000)
    physicsYImpulse(12000)
    setGravity(1500)
    sprite('bn600_04', 4)	# 5-8
    sprite('bn600_05', 4)	# 9-12
    SFX_0('019_cloth_c')
    SFX_0('019_cloth_a')
    sprite('bn600_06', 4)	# 13-16
    sprite('bn600_07', 4)	# 17-20
    sprite('bn600_08', 4)	# 21-24
    label(9)
    sprite('bn600_09', 1)	# 25-25
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('bn600_10', 6)	# 26-31
    clearUponHandler(2)
    SFX_3('bnse_10')
    sprite('bn600_11', 6)	# 32-37
    sprite('bn600_12', 6)	# 38-43
    sprite('bn600_13', 6)	# 44-49
    sprite('bn600_14', 6)	# 50-55
    sprite('bn600_15', 6)	# 56-61
    sprite('bn600_16', 6)	# 62-67
    sprite('bn600_17', 6)	# 68-73
    sprite('bn600_18', 6)	# 74-79
    sprite('bn600_19', 6)	# 80-85
    sprite('bn600_20', 6)	# 86-91
    sprite('bn600_21', 7)	# 92-98
    sprite('bn600_22', 7)	# 99-105
    sprite('bn600_23', 7)	# 106-112
    label(1)
    sprite('bn000_00', 7)	# 113-119
    sprite('bn000_01', 7)	# 120-126
    sprite('bn000_02', 7)	# 127-133
    sprite('bn000_03', 7)	# 134-140
    sprite('bn000_04', 7)	# 141-147
    sprite('bn000_05', 7)	# 148-154
    sprite('bn000_06', 7)	# 155-161
    sprite('bn000_07', 7)	# 162-168
    sprite('bn000_08', 7)	# 169-175
    sprite('bn000_09', 7)	# 176-182
    sprite('bn000_11', 7)	# 183-189
    loopRest()
    gotoLabel(1)

@State
def Act2Event_bnvsjn_01():

    def upon_IMMEDIATE():
        Unknown2017(0)
        Unknown2034(0)
    label(0)
    sprite('bn000_00', 7)	# 1-7
    sprite('bn000_01', 7)	# 8-14
    sprite('bn000_02', 7)	# 15-21
    sprite('bn000_03', 7)	# 22-28
    sprite('bn000_04', 7)	# 29-35
    sprite('bn000_05', 7)	# 36-42
    sprite('bn000_06', 7)	# 43-49
    sprite('bn000_07', 7)	# 50-56
    sprite('bn000_08', 7)	# 57-63
    sprite('bn000_09', 7)	# 64-70
    sprite('bn000_11', 7)	# 71-77
    loopRest()
    gotoLabel(0)

@State
def Act2Event_bnvsjn_02():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 360000):
                    clearUponHandler(3)
                    sendToLabel(0)
            elif (SLOT_22 > (-360000)):
                clearUponHandler(3)
                sendToLabel(0)
    sprite('bn032_01', 3)	# 1-3
    physicsXImpulse(32000)
    label(9)
    sprite('bn032_02', 3)	# 4-6
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 7-9
    sprite('bn032_04', 3)	# 10-12
    sprite('bn032_05', 3)	# 13-15
    sprite('bn032_06', 3)	# 16-18
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 19-21
    sprite('bn032_08', 3)	# 22-24
    sprite('bn032_01', 3)	# 25-27
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('bn032_09', 5)	# 28-32
    physicsXImpulse(0)
    Unknown1045(10000)
    sprite('bn032_10', 5)	# 33-37
    loopRest()
    Unknown1084(1)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def Act2Event_bnvsjn_03():
    sprite('bn040_00', 3)	# 1-3
    sprite('bn040_01', 3)	# 4-6
    sprite('bn312_00', 4)	# 7-10
    sprite('bn312_01', 4)	# 11-14
    sprite('bn312_02', 4)	# 15-18
    sprite('bn312_03', 4)	# 19-22
    sprite('bn312_04', 4)	# 23-26
    sprite('bn312_05', 4)	# 27-30
    sprite('bn312_06', 4)	# 31-34
    sprite('bn312_07', 4)	# 35-38
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_bnvsny_00():
    sprite('bn620_00', 4)	# 1-4
    GFX_0('Act2Event_Yure', -1)
    sprite('bn620_01', 4)	# 5-8
    sprite('bn620_02', 4)	# 9-12
    sprite('bn620_05', 4)	# 13-16
    sprite('bn620_06', 4)	# 17-20
    sprite('bn620_07', 4)	# 21-24
    sprite('bn620_08', 4)	# 25-28
    sprite('bn620_09', 32767)	# 29-32795
    loopRest()

@State
def Act2Event_RunIn():

    def upon_IMMEDIATE():
        Unknown1000(-960000)
        Unknown2034(0)
        Unknown2017(0)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 360000):
                    clearUponHandler(3)
                    sendToLabel(0)
            elif (SLOT_22 > (-360000)):
                clearUponHandler(3)
                sendToLabel(0)
    sprite('bn032_01', 3)	# 1-3
    physicsXImpulse(32000)
    label(9)
    sprite('bn032_02', 3)	# 4-6
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 7-9
    sprite('bn032_04', 3)	# 10-12
    sprite('bn032_05', 3)	# 13-15
    sprite('bn032_06', 3)	# 16-18
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 19-21
    sprite('bn032_08', 3)	# 22-24
    sprite('bn032_01', 3)	# 25-27
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('bn032_09', 5)	# 28-32
    physicsXImpulse(0)
    Unknown1045(10000)
    sprite('bn032_10', 5)	# 33-37
    loopRest()
    Unknown1084(1)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def KuginasiSugekae():
    sprite('bn063_11', 128)	# 1-128
    Unknown3004(-2)
    GFX_0('Event_Kuginasi', 100)
    sprite('bn063_11', 32767)	# 129-32895
    Unknown3038(1)
    Unknown21007(22, 32)

@State
def Act2EventNYvsBN00():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    GFX_0('Act2Event_CreatePT', -1)
    Unknown1000(0)
    loopRest()

@State
def Act2EventNYvsBN01():

    def upon_IMMEDIATE():

        def upon_32():
            Unknown21012('416374324576656e745f4372656174655054000000000000000000000000000020000000')
            GFX_0('Act2Event_PTCamera', 0)

        def upon_33():
            Unknown21012('416374324576656e745f4372656174655054000000000000000000000000000021000000')

        def upon_34():
            Unknown21012('416374324576656e745f505443616d657261000000000000000000000000000020000000')
            Unknown21012('416374324576656e745f4372656174655054000000000000000000000000000022000000')
        sendToLabelUpon(35, 3)
        Unknown2037(4)
        teleportRelativeX(-100000)
        sendToLabelUpon(2, 1)
    sprite('null', 1)	# 1-1
    GFX_0('bn_win', -1)
    SFX_3('bnse_06')
    setGravity(1000)
    teleportRelativeY(200000)
    label(0)
    sprite('bn610_08', 3)	# 2-4
    sprite('bn610_09', 3)	# 5-7
    sprite('bn610_10', 3)	# 8-10
    sprite('bn610_11', 3)	# 11-13
    sprite('bn610_12', 3)	# 14-16
    sprite('bn610_13', 3)	# 17-19
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bn610_07', 3)	# 20-22
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('bn610_04', 3)	# 23-25
    sprite('bn610_03', 3)	# 26-28
    sprite('bn610_02', 3)	# 29-31
    sprite('bn610_01', 3)	# 32-34
    sprite('bn610_00', 3)	# 35-37
    loopRest()
    label(2)
    sprite('bn000_00', 7)	# 38-44
    sprite('bn000_01', 7)	# 45-51
    sprite('bn000_02', 7)	# 52-58
    sprite('bn000_03', 7)	# 59-65
    sprite('bn000_04', 7)	# 66-72
    sprite('bn000_05', 7)	# 73-79
    sprite('bn000_06', 7)	# 80-86
    sprite('bn000_07', 7)	# 87-93
    sprite('bn000_08', 7)	# 94-100
    sprite('bn000_09', 7)	# 101-107
    sprite('bn000_11', 7)	# 108-114
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('bn003_00', 3)	# 115-117
    Unknown2005()
    sprite('bn003_01', 3)	# 118-120
    sprite('bn003_02', 3)	# 121-123
    loopRest()
    gotoLabel(2)

@State
def Act2Event_StandTurnToBstep():
    sprite('bn003_00', 3)	# 1-3
    Unknown2005()
    sprite('bn003_01', 3)	# 4-6
    sprite('bn003_02', 3)	# 7-9
    loopRest()
    sprite('bn031_00', 2)	# 10-11
    physicsXImpulse(-28000)
    SFX_3('bnse_08')
    sprite('bn031_01', 2)	# 12-13
    sprite('bn031_02', 2)	# 14-15
    sprite('bn031_01', 2)	# 16-17
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('bn031_00', 2)	# 18-19
    loopRest()
    enterState('Act2EventReaction')

@State
def Act3Event_azvsbn_00():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        teleportRelativeX(25000)
    label(0)
    sprite('bn000_00', 7)	# 1-7
    sprite('bn000_01', 7)	# 8-14
    sprite('bn000_02', 7)	# 15-21
    sprite('bn000_03', 7)	# 22-28
    sprite('bn000_04', 7)	# 29-35
    sprite('bn000_05', 7)	# 36-42
    sprite('bn000_06', 7)	# 43-49
    sprite('bn000_07', 7)	# 50-56
    sprite('bn000_08', 7)	# 57-63
    sprite('bn000_09', 7)	# 64-70
    sprite('bn000_11', 7)	# 71-77
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bn070_00', 10)	# 78-87
    Unknown4049(1500)
    GFX_1('ef_hitmd', 103)
    SFX_0('100_hit_grap_3')
    ScreenShake(3000, 18000)
    sprite('bn070_01', 10)	# 88-97
    Unknown1047(-17000)
    sprite('bn070_02', 8)	# 98-105
    sprite('bn070_03', 8)	# 106-113
    sprite('bn070_02', 5)	# 114-118
    sprite('bn070_03', 5)	# 119-123
    Unknown1084(1)
    label(2)
    sprite('bn070_02', 5)	# 124-128
    sprite('bn070_03', 5)	# 129-133
    loopRest()
    gotoLabel(2)

@State
def Act3Event_YorokeDown():
    sprite('bn070_02', 6)	# 1-6
    sprite('bn070_03', 6)	# 7-12
    sprite('bn070_04', 6)	# 13-18
    sprite('bn070_05', 6)	# 19-24
    sprite('bn070_06', 6)	# 25-30
    sprite('bn070_07', 6)	# 31-36
    sprite('bn070_08', 6)	# 37-42
    sprite('bn070_09', 6)	# 43-48
    GFX_1('ef_grndshock', 104)
    SFX_0('209_down_normal_0')
    sprite('bn063_11', 32767)	# 49-32815
    teleportRelativeX(140000)

@State
def Act3Event_BNvsHB02():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('bn203_00', 4)	# 1-4
    setInvincible(1)
    Unknown1000(-160000)
    sprite('bn203_01', 1)	# 5-5
    sprite('bn203_01', 2)	# 6-7
    GFX_0('bn_D_stand', -1)
    Unknown8000(100, 1, 1)
    sprite('bn203_02', 3)	# 8-10
    sprite('bn203_03', 3)	# 11-13
    sprite('bn203_04', 2)	# 14-15
    sprite('bn203_05', 1)	# 16-16
    physicsXImpulse(80000)
    Unknown8006(100, 1, 1)
    sprite('bn203_06', 1)	# 17-17
    Unknown1019(80)
    sprite('bn203_07', 2)	# 18-19
    Unknown8006(100, 1, 1)
    Unknown1019(40)
    GFX_0('bn_D_stand2', -1)
    sprite('bn203_08', 2)	# 20-21
    Unknown1019(50)
    SFX_0('005_swing_grap_2_2')
    sprite('bn203_09', 15)	# 22-36
    Unknown21007(22, 32)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('bn203_10', 3)	# 37-39
    sprite('bn203_11', 3)	# 40-42
    sprite('bn203_12', 3)	# 43-45
    sprite('bn203_13', 3)	# 46-48
    sprite('bn203_14', 3)	# 49-51
    sprite('bn203_15', 3)	# 52-54
    sprite('bn203_16', 3)	# 55-57
    loopRest()
    enterState('EventBackStepForLC')

@State
def Act3Event_BNvsHB04():
    sprite('bn402_00', 5)	# 1-5
    sprite('bn402_01', 5)	# 6-10
    sprite('bn402_02', 2)	# 11-12
    sprite('bn402_02', 3)	# 13-15
    sprite('bn402_37', 10)	# 16-25
    sprite('bn402_38', 8)	# 26-33
    sprite('bn402_39', 8)	# 34-41
    sprite('bn402_40', 7)	# 42-48
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_bnvshb_05():
    sprite('bn032_01', 3)	# 1-3
    physicsXImpulse(32000)
    sprite('bn032_02', 3)	# 4-6
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 7-9
    sprite('bn032_04', 3)	# 10-12
    loopRest()
    label(0)
    physicsXImpulse(0)
    Unknown1045(10000)
    sprite('bn032_10', 5)	# 13-17
    Unknown1084(1)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsCA00():

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 200000):
                clearUponHandler(3)
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-200000)):
            clearUponHandler(3)
            sendToLabel(1)
    sprite('bn032_01', 3)	# 1-3
    Unknown2034(0)
    Unknown2037(1)
    Unknown2017(0)
    Unknown1000(-960000)
    physicsXImpulse(21000)
    label(0)
    sprite('bn032_02', 3)	# 4-6
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_03', 3)	# 7-9
    sprite('bn032_04', 3)	# 10-12
    sprite('bn032_05', 3)	# 13-15
    sprite('bn032_06', 3)	# 16-18
    SFX_3('bnse_09')
    Unknown8006(100, 1, 1)
    sprite('bn032_07', 3)	# 19-21
    sprite('bn032_08', 3)	# 22-24
    sprite('bn032_01', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bn032_09', 3)	# 28-30
    Unknown1045(5000)
    sprite('bn032_10', 3)	# 31-33
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsCA01():
    sprite('bn031_00', 2)	# 1-2
    physicsXImpulse(-28000)
    SFX_3('bnse_08')
    sprite('bn031_01', 2)	# 3-4
    sprite('bn031_02', 2)	# 5-6
    sprite('bn031_01', 2)	# 7-8
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('bn031_00', 2)	# 9-10
    loopRest()
    enterState('Act2EventReaction')

@State
def Act3Event_bnvslc_00():

    def upon_IMMEDIATE():
        sendToLabelUpon(2, 2)
        sendToLabelUpon(32, 1)
        Unknown2034(0)
    label(0)
    sprite('bn000_00', 7)	# 1-7
    sprite('bn000_01', 7)	# 8-14
    sprite('bn000_02', 7)	# 15-21
    sprite('bn000_03', 7)	# 22-28
    sprite('bn000_04', 7)	# 29-35
    sprite('bn000_05', 7)	# 36-42
    sprite('bn000_06', 7)	# 43-49
    sprite('bn000_07', 7)	# 50-56
    sprite('bn000_08', 7)	# 57-63
    sprite('bn000_09', 7)	# 64-70
    sprite('bn000_11', 7)	# 71-77
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('bn033_00', 2)	# 78-79
    sprite('bn033_01', 2)	# 80-81
    physicsXImpulse(-15000)
    sprite('bn033_02', 2)	# 82-83
    sprite('bn033_03', 2)	# 84-85
    sprite('bn033_04', 1)	# 86-86
    sprite('bn033_04', 1)	# 87-87
    sprite('bn033_05', 2)	# 88-89
    sprite('bn033_06', 3)	# 90-92
    physicsXImpulse(-20000)
    physicsYImpulse(11000)
    setGravity(1650)
    SFX_3('bnse_08')
    sprite('bn033_07', 3)	# 93-95
    sprite('bn033_08', 3)	# 96-98
    sprite('bn033_09', 3)	# 99-101
    sprite('bn033_10', 3)	# 102-104
    label(2)
    clearUponHandler(2)
    sprite('bn033_11', 3)	# 105-107
    Unknown1019(50)
    sprite('bn033_12', 3)	# 108-110
    physicsXImpulse(0)
    SFX_3('bnse_09')
    Unknown8000(100, 1, 1)
    sprite('bn033_13', 3)	# 111-113
    loopRest()
    enterState('Act2Event_bnvsjn_02')

@State
def Act3Event_BNvsLC05():
    sprite('bn040_00', 4)	# 1-4
    GFX_0('Act3Event_TeniObj', -1)
    Unknown3004(-4)
    sprite('bn040_01', 4)	# 5-8
    sprite('bn040_02', 5)	# 9-13
    sprite('bn040_03', 5)	# 14-18
    sprite('bn040_04', 5)	# 19-23
    Unknown3038(1)
    Unknown2035(1)
    label(0)
    sprite('bn040_02', 5)	# 24-28
    sprite('bn040_03', 5)	# 29-33
    sprite('bn040_04', 5)	# 34-38
    loopRest()
    gotoLabel(0)

@State
def Act3Event_BNvsPH00():

    def upon_IMMEDIATE():
        Unknown3001(0)
        loopRelated(17, 120)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)

        def upon_STATE_END():
            Unknown3001(255)
    sprite('bn040_02', 80)	# 1-80
    GFX_0('Act3Event_TeniObj', -1)
    Unknown3004(4)
    label(0)
    sprite('bn040_03', 5)	# 81-85
    sprite('bn040_04', 5)	# 86-90
    loopRest()
    label(1)
    sprite('bn040_02', 5)	# 91-95
    sprite('bn040_03', 5)	# 96-100
    sprite('bn040_04', 5)	# 101-105
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('bn040_01', 5)	# 106-110
    sprite('bn040_00', 5)	# 111-115
    loopRest()
    label(3)
    sprite('bn000_00', 7)	# 116-122
    sprite('bn000_01', 7)	# 123-129
    sprite('bn000_02', 7)	# 130-136
    sprite('bn000_03', 7)	# 137-143
    sprite('bn000_04', 7)	# 144-150
    sprite('bn000_05', 7)	# 151-157
    sprite('bn000_06', 7)	# 158-164
    sprite('bn000_07', 7)	# 165-171
    sprite('bn000_08', 7)	# 172-178
    sprite('bn000_09', 7)	# 179-185
    sprite('bn000_11', 7)	# 186-192
    loopRest()
    gotoLabel(3)