@Subroutine
def PreInit():
    Unknown12019('706d6900000000000000000000000000')

@Subroutine
def MatchInit():
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(2)
    Unknown13039(2)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
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
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5A5th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5A6th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2ARenda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14015(2000, 580000, -117000, 143000, 200, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5B3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown15015(30, 40)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14015(-10000, 323000, -209000, 417000, 200, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B2nd', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 350000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(20000, 430000, -219000, -66000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(10000, 377000, -218000, 131000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(10000, 377000, -218000, 131000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Move_AirGround_(0x3083)
    Unknown14015(210000, 702000, -417000, 209000, 10, 0)
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
    Move_Register('coup_droitA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(400000, 700000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('coup_droitB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(900000, 1200000, -200000, 200000, 3000, 10)
    Move_EndRegister()
    Move_Register('coup_droitEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(900000, 1200000, -200000, 200000, 1500, 10)
    Move_EndRegister()
    Move_Register('MarinKarin', INPUT_SPECIALMOVE)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3083)
    Unknown14015(400000, 700000, -200000, 200000, 10, 0)
    Move_EndRegister()
    Move_Register('Tentarafoo', INPUT_SPECIALMOVE)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3083)
    Unknown15009()
    Unknown14015(900000, 1200000, -200000, 200000, 50, 10)
    Move_EndRegister()
    Move_Register('Bufula', INPUT_SPECIALMOVE)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3083)
    Unknown14015(400000, 700000, -200000, 200000, 10, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(7000, 266000, -123000, 655000, 100, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14015(7000, 266000, -123000, 655000, 100, 0)
    Move_EndRegister()
    Move_Register('Setsuna_Samidare_Uchi', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(2000, 580000, -117000, 143000, 100, 0)
    Move_EndRegister()
    Move_Register('Setsuna_Samidare_UchiSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(2000, 580000, -117000, 143000, 100, 0)
    Move_EndRegister()
    Move_Register('Bufudyne', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(-100000, 350000, 100000, 450000, 100, 0)
    Move_EndRegister()
    Move_Register('BufudyneSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(-100000, 350000, 100000, 450000, 100, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk5A4th', 'NmlAtk5A5th', 10000000)
    Unknown15024('NmlAtk5A5th', 'NmlAtk5A6th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'NmlAtk5B3rd', 10000000)
    Unknown15024('NmlAtk5B3rd', 'coup_droitB', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk2B2nd', 10000000)
    Unknown15024('NmlAtk2B2nd', 'Tentarafoo', 10000000)
    Unknown12018(0, 'mi060_00')
    Unknown12018(1, 'mi060_01')
    Unknown12018(2, 'mi060_02')
    Unknown12018(3, 'mi060_03')
    Unknown12018(4, 'mi060_04')
    Unknown12018(5, 'mi060_05')
    Unknown12018(6, 'mi060_06')
    Unknown12018(7, 'mi041_02')
    Unknown12018(8, 'mi040_02')
    Unknown12018(9, 'mi045_02')
    Unknown12018(10, 'mi060_00')
    Unknown12018(11, 'mi060_01')
    Unknown12018(12, 'mi060_03')
    Unknown12018(13, 'mi060_05')
    Unknown12018(14, 'mi060_07')
    Unknown12018(15, 'mi125_00')
    Unknown12018(16, 'mi050_00')
    Unknown12018(17, 'mi052_00')
    Unknown12018(18, 'mi054_00')
    Unknown12018(19, 'mi000_00')
    Unknown12018(20, 'mi000_00')
    Unknown12018(25, 'mi063_00')
    Unknown12018(26, 'mi063_01')
    Unknown12018(27, 'mi063_02')
    Unknown12018(28, 'mi063_05')
    Unknown12018(29, 'mi060_12')
    Unknown12018(24, 'mi072_03')
    Unknown7010(0, 'pmi000')
    Unknown7010(1, 'pmi001')
    Unknown7010(2, 'pmi002')
    Unknown7010(3, 'pmi003')
    Unknown7010(4, 'pmi004')
    Unknown7010(5, 'pmi005')
    Unknown7010(6, 'pmi006')
    Unknown7010(7, 'pmi007')
    Unknown7010(8, 'pmi008')
    Unknown7010(9, 'pmi009')
    Unknown7010(10, 'pmi010')
    Unknown7010(15, 'pmi011')
    Unknown7010(16, 'pmi012')
    Unknown7010(17, 'pmi013')
    Unknown7010(18, 'pmi014')
    Unknown7010(19, 'pmi015')
    Unknown7010(20, 'pmi016')
    Unknown7010(21, 'pmi017')
    Unknown7010(22, 'pmi018')
    Unknown7010(23, 'pmi019')
    Unknown7010(24, 'pmi020')
    Unknown7010(25, 'pmi021')
    Unknown7010(28, 'pmi022')
    Unknown7010(29, 'pmi023')
    Unknown7010(30, 'pmi024')
    Unknown7010(31, 'pmi025')
    Unknown7010(32, 'pmi026')
    Unknown7010(33, 'pmi027')
    Unknown7010(34, 'pmi028')
    Unknown7010(35, 'pmi029')
    Unknown7010(36, 'pmi030')
    Unknown7010(37, 'pmi031')
    Unknown7010(39, 'pmi032')
    Unknown7010(42, 'pmi033')
    Unknown7010(43, 'pmi034')
    Unknown7010(44, 'pmi035')
    Unknown7010(45, 'pmi036')
    Unknown7010(46, 'pmi037')
    Unknown7010(47, 'pmi038')
    Unknown7010(48, 'pmi039')
    Unknown7010(49, 'pmi040')
    Unknown7010(50, 'pmi041')
    Unknown7010(52, 'pmi042')
    Unknown7010(53, 'pmi043')
    Unknown7010(54, 'pmi100_0')
    Unknown7010(55, 'pmi100_1')
    Unknown7010(56, 'pmi100_2')
    Unknown7010(63, 'pmi101_0')
    Unknown7010(64, 'pmi101_1')
    Unknown7010(65, 'pmi101_2')
    Unknown7010(57, 'pmi102_0')
    Unknown7010(58, 'pmi102_1')
    Unknown7010(59, 'pmi102_2')
    Unknown7010(66, 'pmi103_0')
    Unknown7010(67, 'pmi103_1')
    Unknown7010(68, 'pmi103_2')
    Unknown7010(60, 'pmi104_0')
    Unknown7010(61, 'pmi104_1')
    Unknown7010(62, 'pmi104_2')
    Unknown7010(69, 'pmi105_0')
    Unknown7010(70, 'pmi105_1')
    Unknown7010(71, 'pmi105_2')
    Unknown7010(72, 'pmi150')
    Unknown7010(73, 'pmi151')
    Unknown7010(74, 'pmi152')
    Unknown7010(85, 'pmi153')
    Unknown7010(87, 'pmi154')
    Unknown7010(88, 'pmi155')
    Unknown7010(96, 'pmi161_0')
    Unknown7010(97, 'pmi161_1')
    Unknown7010(92, 'pmi162_0')
    Unknown7010(93, 'pmi162_1')
    Unknown7010(98, 'pmi163_0')
    Unknown7010(99, 'pmi163_1')
    Unknown7010(100, 'pmi164_0')
    Unknown7010(101, 'pmi164_1')
    Unknown7010(105, 'pmi165_0')
    Unknown7010(106, 'pmi165_1')
    Unknown7010(102, 'pmi166_0')
    Unknown7010(103, 'pmi166_1')
    Unknown7010(90, 'pmi167_0')
    Unknown7010(91, 'pmi167_1')
    Unknown7010(107, 'pmi168_0')
    Unknown7010(108, 'pmi168_1')
    Unknown7010(110, 'pmi169_0')
    Unknown7010(111, 'pmi169_1')
    Unknown7010(94, 'pmi400_0')
    Unknown7010(95, 'pmi400_1')
    Unknown30036('504d495f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3541000000000000000000000000000000000000000000000000')
    Unknown12059('0200000053657473756e615f53616d69646172655f556368690000000000000000000000')
    Unknown12059('0300000053657473756e615f53616d69646172655f556368695350000000000000000000')
    Unknown12059('040000004275667564796e65000000000000000000000000000000000000000000000000')
    Unknown12059('050000004275667564796e65535000000000000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnPreDraw():
    Unknown23030('706d695f726170696572656666000000000000000000000000000000000000000000000034000000000000000400000000000000000000000000000000000000')

@State
def CmnActStand():
    label(0)
    sprite('mi000_00', 8)	# 1-8
    sprite('mi000_01', 8)	# 9-16
    sprite('mi000_02', 8)	# 17-24
    sprite('mi000_03', 8)	# 25-32
    sprite('mi000_04', 8)	# 33-40
    sprite('mi000_05', 8)	# 41-48
    sprite('mi000_06', 8)	# 49-56
    sprite('mi000_07', 8)	# 57-64
    sprite('mi000_08', 8)	# 65-72
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('mi001_00', 8)	# 73-80
    SLOT_88 = 960
    SFX_1('pmi000')
    sprite('mi001_01', 8)	# 81-88
    sprite('mi001_02', 8)	# 89-96
    sprite('mi001_03', 6)	# 97-102
    sprite('mi001_04', 6)	# 103-108
    sprite('mi001_05', 6)	# 109-114
    sprite('mi001_06', 6)	# 115-120
    sprite('mi001_07', 6)	# 121-126
    sprite('mi001_08', 6)	# 127-132
    sprite('mi001_09', 6)	# 133-138
    SFX_3('hair')
    sprite('mi001_10', 6)	# 139-144
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('mi003_00', 4)	# 1-4
    sprite('mi003_01', 4)	# 5-8
    sprite('mi003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('mi010_00', 4)	# 1-4
    sprite('mi010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('mi010_02', 8)	# 1-8
    sprite('mi010_03', 8)	# 9-16
    sprite('mi010_04', 8)	# 17-24
    sprite('mi010_05', 8)	# 25-32
    sprite('mi010_06', 8)	# 33-40
    sprite('mi010_07', 8)	# 41-48
    sprite('mi010_08', 8)	# 49-56
    sprite('mi010_09', 8)	# 57-64
    sprite('mi010_10', 8)	# 65-72
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('mi013_00', 4)	# 1-4
    sprite('mi013_01', 4)	# 5-8
    sprite('mi013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('mi010_01', 4)	# 1-4
    sprite('mi010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('mi010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('mi020_00', 4)	# 1-4
    sprite('mi020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('mi020_02', 3)	# 1-3
    sprite('mi020_03', 3)	# 4-6
    sprite('mi020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('mi020_05', 3)	# 1-3
    sprite('mi020_06', 3)	# 4-6
    label(0)
    sprite('mi020_07', 4)	# 7-10
    sprite('mi020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('mi010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('mi230_00', 3)	# 1-3
    sprite('mi230_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('mi230_00', 3)	# 1-3

@State
def CmnActFWalk():
    sprite('mi030_00', 5)	# 1-5
    sprite('mi030_01', 5)	# 6-10
    label(0)
    sprite('mi030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mi030_03', 5)	# 16-20
    sprite('mi030_04', 5)	# 21-25
    sprite('mi030_05', 5)	# 26-30
    sprite('mi030_06', 5)	# 31-35
    sprite('mi030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mi030_08', 5)	# 41-45
    sprite('mi030_09', 5)	# 46-50
    sprite('mi030_10', 5)	# 51-55
    sprite('mi030_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('mi031_00', 6)	# 1-6
    sprite('mi031_01', 6)	# 7-12
    label(0)
    sprite('mi031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mi031_03', 6)	# 19-24
    sprite('mi031_04', 6)	# 25-30
    sprite('mi031_05', 6)	# 31-36
    sprite('mi031_06', 6)	# 37-42
    sprite('mi031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mi031_08', 6)	# 49-54
    sprite('mi031_09', 6)	# 55-60
    sprite('mi031_10', 6)	# 61-66
    sprite('mi031_11', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('mi030_00', 2)	# 1-2
    sprite('mi030_01', 2)	# 3-4
    sprite('mi032_00', 2)	# 5-6
    label(0)
    sprite('mi032_01', 4)	# 7-10
    sprite('mi032_02', 4)	# 11-14
    sprite('mi032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('mi032_04', 4)	# 19-22
    sprite('mi032_05', 4)	# 23-26
    sprite('mi032_06', 4)	# 27-30
    sprite('mi032_07', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('mi032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('mi032_09', 4)	# 1-4
    sprite('mi032_10', 4)	# 5-8

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
    sprite('mi033_00', 2)	# 1-2
    sprite('mi033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('mi033_02', 3)	# 6-8
    label(0)
    sprite('mi033_01', 3)	# 9-11
    sprite('mi033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi033_03', 3)	# 15-17
    setInvincible(0)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('mi033_04', 3)	# 18-20

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirTurn():
    sprite('mi025_00', 1)	# 1-1
    sprite('mi025_01', 2)	# 2-3
    sprite('mi025_02', 1)	# 4-4

@State
def CmnActAirFDash():
    sprite('mi035_00', 3)	# 1-3
    label(0)
    sprite('mi035_01', 2)	# 4-5
    sprite('mi035_02', 2)	# 6-7
    sprite('mi035_03', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('mi033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('mi033_02', 3)	# 4-6
    sprite('mi033_01', 3)	# 7-9
    sprite('mi033_02', 3)	# 10-12
    sprite('mi033_01', 3)	# 13-15
    sprite('mi033_02', 3)	# 16-18
    sprite('mi033_01', 3)	# 19-21
    sprite('mi033_02', 3)	# 22-24
    sprite('mi020_05', 3)	# 25-27
    sprite('mi020_06', 3)	# 28-30
    label(0)
    sprite('mi020_07', 4)	# 31-34
    sprite('mi020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('mi050_00', 1)	# 1-1
    sprite('mi050_01', 1)	# 2-2
    sprite('mi050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('mi050_01', 1)	# 1-1
    sprite('mi050_02', 1)	# 2-2
    sprite('mi050_01', 2)	# 3-4
    sprite('mi050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('mi050_02', 1)	# 1-1
    sprite('mi050_03', 1)	# 2-2
    sprite('mi050_02', 2)	# 3-4
    sprite('mi050_01', 2)	# 5-6
    sprite('mi050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('mi050_03', 1)	# 1-1
    sprite('mi050_04', 1)	# 2-2
    sprite('mi050_03', 2)	# 3-4
    sprite('mi050_02', 2)	# 5-6
    sprite('mi050_01', 2)	# 7-8
    sprite('mi050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('mi050_04', 1)	# 1-1
    sprite('mi050_04', 1)	# 2-2
    sprite('mi050_04', 2)	# 3-4
    sprite('mi050_03', 2)	# 5-6
    sprite('mi050_02', 2)	# 7-8
    sprite('mi050_01', 2)	# 9-10
    sprite('mi050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('mi052_00', 1)	# 1-1
    sprite('mi052_01', 1)	# 2-2
    sprite('mi052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('mi052_01', 1)	# 1-1
    sprite('mi052_02', 1)	# 2-2
    sprite('mi052_01', 2)	# 3-4
    sprite('mi052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('mi052_02', 1)	# 1-1
    sprite('mi052_03', 1)	# 2-2
    sprite('mi052_02', 2)	# 3-4
    sprite('mi052_01', 2)	# 5-6
    sprite('mi052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('mi052_03', 1)	# 1-1
    sprite('mi052_04', 1)	# 2-2
    sprite('mi052_03', 2)	# 3-4
    sprite('mi052_02', 2)	# 5-6
    sprite('mi052_01', 2)	# 7-8
    sprite('mi052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('mi052_04', 1)	# 1-1
    sprite('mi052_04', 1)	# 2-2
    sprite('mi052_04', 2)	# 3-4
    sprite('mi052_03', 2)	# 5-6
    sprite('mi052_02', 2)	# 7-8
    sprite('mi052_01', 2)	# 9-10
    sprite('mi052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('mi054_00', 1)	# 1-1
    sprite('mi054_01', 1)	# 2-2
    sprite('mi054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('mi054_01', 1)	# 1-1
    sprite('mi054_02', 1)	# 2-2
    sprite('mi054_01', 2)	# 3-4
    sprite('mi054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('mi054_02', 1)	# 1-1
    sprite('mi054_03', 1)	# 2-2
    sprite('mi054_02', 2)	# 3-4
    sprite('mi054_01', 2)	# 5-6
    sprite('mi054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('mi054_03', 1)	# 1-1
    sprite('mi054_04', 1)	# 2-2
    sprite('mi054_03', 2)	# 3-4
    sprite('mi054_02', 2)	# 5-6
    sprite('mi054_01', 2)	# 7-8
    sprite('mi054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('mi054_04', 1)	# 1-1
    sprite('mi054_04', 1)	# 2-2
    sprite('mi054_04', 2)	# 3-4
    sprite('mi054_03', 2)	# 5-6
    sprite('mi054_02', 2)	# 7-8
    sprite('mi054_01', 2)	# 9-10
    sprite('mi054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('mi060_00', 4)	# 1-4
    label(0)
    sprite('mi060_01', 4)	# 5-8
    sprite('mi060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('mi060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('mi060_04', 8)	# 1-8
    label(1)
    sprite('mi060_05', 4)	# 9-12
    sprite('mi060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('mi060_07', 4)	# 1-4

@State
def CmnActBDownBound():
    sprite('mi060_08', 2)	# 1-2
    sprite('mi060_09', 2)	# 3-4
    sprite('mi060_10', 2)	# 5-6
    sprite('mi060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('mi060_12', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('mi064_00', 6)	# 1-6
    sprite('mi064_01', 6)	# 7-12
    sprite('mi064_02', 6)	# 13-18
    sprite('mi064_03', 6)	# 19-24

@State
def CmnActFDownUpper():
    sprite('mi063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('mi063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('mi063_03', 3)	# 1-3
    sprite('mi063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('mi063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('mi060_08', 2)	# 1-2
    sprite('mi060_09', 2)	# 3-4
    sprite('mi060_10', 2)	# 5-6
    sprite('mi060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('mi060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('mi064_00', 6)	# 1-6
    sprite('mi064_01', 6)	# 7-12
    sprite('mi064_02', 6)	# 13-18
    sprite('mi064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('mi060_00', 4)	# 1-4
    label(0)
    sprite('mi060_01', 4)	# 5-8
    sprite('mi060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('mi060_03', 4)	# 1-4

@State
def CmnActVDownDown():
    sprite('mi060_04', 8)	# 1-8
    label(0)
    sprite('mi060_05', 4)	# 9-12
    sprite('mi060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('mi060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('mi072_00', 3)	# 1-3
    label(0)
    sprite('mi072_01', 3)	# 4-6
    sprite('mi072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('mi074_00', 2)	# 1-2
    sprite('mi074_01', 2)	# 3-4
    sprite('mi074_02', 2)	# 5-6
    sprite('mi074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('mi072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('mi063_00', 4)	# 1-4
    sprite('mi063_01', 4)	# 5-8
    sprite('mi063_02', 4)	# 9-12
    label(0)
    sprite('mi063_03', 4)	# 13-16
    sprite('mi063_04', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('mi082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('mi050_00', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('mi070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('mi070_01', 4)	# 1-4
    sprite('mi070_02', 4)	# 5-8
    sprite('mi070_03', 4)	# 9-12
    sprite('mi070_04', 4)	# 13-16
    sprite('mi070_05', 4)	# 17-20
    sprite('mi070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('mi040_03', 2)	# 1-2
    sprite('mi040_02', 2)	# 3-4
    sprite('mi040_01', 2)	# 5-6
    sprite('mi040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('mi020_02', 3)	# 1-3
    sprite('mi020_03', 3)	# 4-6
    sprite('mi020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('mi020_02', 3)	# 1-3
    sprite('mi020_03', 3)	# 4-6
    sprite('mi020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('mi020_02', 3)	# 1-3
    sprite('mi020_03', 3)	# 4-6
    sprite('mi020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('mi112_00', 3)	# 1-3
    sprite('mi112_01', 3)	# 4-6
    sprite('mi112_02', 3)	# 7-9
    sprite('mi112_03', 3)	# 10-12
    sprite('mi112_04', 3)	# 13-15
    sprite('mi112_05', 3)	# 16-18
    sprite('mi020_07', 4)	# 19-22
    sprite('mi020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandF():
    sprite('mi112_00', 3)	# 1-3
    sprite('mi112_01', 3)	# 4-6
    sprite('mi112_02', 3)	# 7-9
    sprite('mi112_03', 3)	# 10-12
    sprite('mi112_04', 3)	# 13-15
    sprite('mi112_05', 3)	# 16-18
    sprite('mi020_07', 4)	# 19-22
    sprite('mi020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('mi112_00', 3)	# 1-3
    sprite('mi112_01', 3)	# 4-6
    sprite('mi112_02', 3)	# 7-9
    sprite('mi112_03', 3)	# 10-12
    sprite('mi112_04', 3)	# 13-15
    sprite('mi112_05', 3)	# 16-18
    sprite('mi020_07', 4)	# 19-22
    sprite('mi020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('mi010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('mi040_00', 3)	# 1-3
    sprite('mi040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('mi040_02', 3)	# 1-3
    sprite('mi040_03', 3)	# 4-6
    sprite('mi040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('mi040_01', 3)	# 1-3
    sprite('mi040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('mi040_05', 1)	# 1-1
    label(0)
    sprite('mi040_02', 3)	# 2-4
    sprite('mi040_03', 3)	# 5-7
    sprite('mi040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('mi040_01', 3)	# 1-3
    sprite('mi040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('mi040_00', 3)	# 1-3
    sprite('mi040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('mi040_02', 3)	# 1-3
    sprite('mi040_03', 3)	# 4-6
    sprite('mi040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('mi040_01', 3)	# 1-3
    sprite('mi040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('mi040_05', 1)	# 1-1
    label(0)
    sprite('mi040_02', 3)	# 2-4
    sprite('mi040_03', 3)	# 5-7
    sprite('mi040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('mi040_01', 3)	# 1-3
    sprite('mi040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('mi043_00', 3)	# 1-3
    sprite('mi043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('mi043_02', 3)	# 1-3
    sprite('mi043_03', 3)	# 4-6
    sprite('mi043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('mi043_01', 3)	# 1-3
    sprite('mi043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('mi043_05', 1)	# 1-1
    label(0)
    sprite('mi043_02', 3)	# 2-4
    sprite('mi043_03', 3)	# 5-7
    sprite('mi043_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('mi043_01', 3)	# 1-3
    sprite('mi043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('mi045_00', 3)	# 1-3
    sprite('mi045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('mi045_02', 3)	# 1-3
    sprite('mi045_03', 3)	# 4-6
    sprite('mi045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('mi045_01', 3)	# 1-3
    sprite('mi045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('mi045_05', 1)	# 1-1
    label(0)
    sprite('mi045_02', 3)	# 2-4
    sprite('mi045_03', 3)	# 5-7
    sprite('mi045_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('mi045_01', 3)	# 1-3
    sprite('mi045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('mi040_05', 2)	# 1-2
    sprite('mi040_05', 2)	# 3-4
    sprite('mi040_05', 1)	# 5-5
    Unknown2042(1)
    sprite('mi040_02', 4)	# 6-9
    sprite('mi040_01', 4)	# 10-13
    sprite('mi040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('mi043_05', 2)	# 1-2
    sprite('mi043_05', 2)	# 3-4
    sprite('mi043_05', 1)	# 5-5
    Unknown2042(1)
    sprite('mi043_02', 4)	# 6-9
    sprite('mi043_01', 4)	# 10-13
    sprite('mi043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('mi045_05', 2)	# 1-2
    sprite('mi045_05', 2)	# 3-4
    sprite('mi045_05', 1)	# 5-5
    Unknown2042(1)
    sprite('mi045_02', 4)	# 6-9
    sprite('mi045_01', 4)	# 10-13
    sprite('mi045_00', 4)	# 14-17

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('mi430_17', 3)	# 1-3
    sprite('mi430_18', 5)	# 4-8
    sprite('mi430_19', 3)	# 9-11
    sprite('mi430_20', 3)	# 12-14
    sprite('mi430_21', 3)	# 15-17	 **attackbox here**
    sprite('mi430_22', 3)	# 18-20
    sprite('mi430_25', 3)	# 21-23
    sprite('mi430_26', 3)	# 24-26
    sprite('mi430_27', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('mi045_02', 1)	# 1-1
    sprite('mi045_01', 3)	# 2-4
    sprite('mi045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('mi210_02', 2)	# 1-2
    sprite('mi210_03', 2)	# 3-4
    sprite('mi210_04', 2)	# 5-6
    sprite('mi210_05', 2)	# 7-8
    sprite('mi210_06', 2)	# 9-10
    sprite('mi210_07', 2)	# 11-12
    sprite('mi210_08', 2)	# 13-14
    sprite('mi210_09', 3)	# 15-17	 **attackbox here**
    sprite('mi210_10', 5)	# 18-22
    sprite('mi210_11', 7)	# 23-29

@State
def CmnActLandSpin():
    sprite('mi071_00', 2)	# 1-2
    label(0)
    sprite('mi071_01', 2)	# 3-4
    sprite('mi071_02', 2)	# 5-6
    sprite('mi071_03', 2)	# 7-8
    sprite('mi071_04', 2)	# 9-10
    sprite('mi071_05', 2)	# 11-12
    sprite('mi071_06', 2)	# 13-14
    sprite('mi071_07', 2)	# 15-16
    sprite('mi071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('mi040_02', 3)	# 1-3
    sprite('mi040_01', 3)	# 4-6
    sprite('mi040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('mi071_00', 2)	# 1-2
    label(0)
    sprite('mi071_01', 2)	# 3-4
    sprite('mi071_02', 2)	# 5-6
    sprite('mi071_03', 2)	# 7-8
    sprite('mi071_04', 2)	# 9-10
    sprite('mi071_05', 2)	# 11-12
    sprite('mi071_06', 2)	# 13-14
    sprite('mi071_07', 2)	# 15-16
    sprite('mi071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('mi124_00', 2)	# 1-2
    label(0)
    sprite('mi124_01', 2)	# 3-4
    sprite('mi124_02', 2)	# 5-6
    sprite('mi124_03', 2)	# 7-8
    sprite('mi124_04', 2)	# 9-10
    sprite('mi124_05', 2)	# 11-12
    sprite('mi124_06', 2)	# 13-14
    sprite('mi124_07', 2)	# 15-16
    sprite('mi124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('mi077_02', 4)	# 1-4
    label(0)
    sprite('mi077_03', 3)	# 5-7
    sprite('mi077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('mi077_05', 5)	# 1-5
    sprite('mi077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('mi077_02', 4)	# 1-4
    label(0)
    sprite('mi077_03', 3)	# 5-7
    sprite('mi077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('mi077_05', 5)	# 1-5
    sprite('mi077_06', 4)	# 6-9

@State
def CmnActBurstBegin():
    label(0)
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('mi121_03', 3)	# 1-3
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('mi121_07', 3)	# 1-3
    sprite('mi020_04', 3)	# 4-6
    sprite('mi020_05', 3)	# 7-9
    sprite('mi020_06', 3)	# 10-12
    label(0)
    sprite('mi020_07', 4)	# 13-16
    sprite('mi020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstBegin():
    label(0)
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('mi121_03', 3)	# 1-3
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('mi121_07', 3)	# 1-3
    sprite('mi020_04', 3)	# 4-6
    sprite('mi020_05', 3)	# 7-9
    sprite('mi020_06', 3)	# 10-12
    label(0)
    sprite('mi020_07', 4)	# 13-16
    sprite('mi020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('mi121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('mi121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('mi121_07', 6)	# 1-6
    sprite('mi010_00', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('mi121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('mi121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('mi121_07', 4)	# 1-4
    sprite('mi020_04', 3)	# 5-7
    sprite('mi020_05', 3)	# 8-10
    sprite('mi020_06', 2)	# 11-12
    label(0)
    sprite('mi020_07', 4)	# 13-16
    sprite('mi020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PMI_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
        Unknown21015('547375726172615f53686f740000000000000000000000000000000000000000e610000000000000')
    sprite('mi121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('mi121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('mi121_07', 6)	# 1-6
    sprite('mi010_00', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PMI_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
        Unknown21015('547375726172615f53686f740000000000000000000000000000000000000000e610000000000000')
    sprite('mi121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('mi121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('mi121_07', 4)	# 1-4
    sprite('mi020_04', 3)	# 5-7
    sprite('mi020_05', 3)	# 8-10
    sprite('mi020_06', 2)	# 11-12
    label(0)
    sprite('mi020_07', 4)	# 13-16
    sprite('mi020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PMI_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
            Unknown21015('547375726172615f53686f740000000000000000000000000000000000000000e610000000000000')
    label(0)
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('mi121_03', 3)	# 1-3
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('mi121_07', 6)	# 1-6
    sprite('mi010_00', 6)	# 7-12

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PMI_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
            Unknown21015('547375726172615f53686f740000000000000000000000000000000000000000e610000000000000')
    label(0)
    sprite('mi121_00', 2)	# 1-2
    sprite('mi121_01', 2)	# 3-4
    sprite('mi121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('mi121_03', 3)	# 1-3
    label(0)
    sprite('mi121_04', 2)	# 4-5
    sprite('mi121_05', 2)	# 6-7
    sprite('mi121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('mi121_07', 4)	# 1-4
    sprite('mi020_04', 3)	# 5-7
    sprite('mi020_05', 3)	# 8-10
    sprite('mi020_06', 2)	# 11-12
    label(0)
    sprite('mi020_07', 4)	# 13-16
    sprite('mi020_08', 4)	# 17-20
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
    sprite('mi251_01', 5)	# 26-30
    Unknown1086(22)
    teleportRelativeX(-240000)
    teleportRelativeY(2000000)
    physicsYImpulse(-166666)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('mi251_02', 1)	# 31-31
    sprite('mi251_03', 2)	# 32-33
    SFX_3('slash_pole_middle')
    sprite('mi251_04', 32767)	# 34-32800	 **attackbox here**
    label(9)
    sprite('mi230_00', 14)	# 32801-32814
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('mi010_01', 4)	# 32815-32818
    sprite('mi010_00', 4)	# 32819-32822

@State
def CmnActChangePartnerQuickIn():
    sprite('mi032_03', 3)	# 1-3
    sprite('mi032_04', 5)	# 4-8
    sprite('mi032_05', 5)	# 9-13
    sprite('mi032_09', 2)	# 14-15
    sprite('mi032_09', 6)	# 16-21
    sprite('mi032_10', 8)	# 22-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('mi033_00', 3)	# 1-3
    sprite('mi033_01', 3)	# 4-6
    sprite('mi033_02', 3)	# 7-9
    sprite('mi033_01', 3)	# 10-12
    sprite('mi033_02', 3)	# 13-15
    sprite('mi033_01', 3)	# 16-18
    sprite('mi033_02', 3)	# 19-21
    sprite('mi033_01', 3)	# 22-24
    sprite('mi033_02', 3)	# 25-27
    sprite('mi033_01', 3)	# 28-30
    sprite('mi033_02', 3)	# 31-33
    sprite('mi033_01', 27)	# 34-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('mi033_00', 2)	# 1-2
    label(0)
    sprite('mi033_01', 3)	# 3-5
    sprite('mi033_02', 3)	# 6-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi033_03', 3)	# 9-11
    sprite('mi033_04', 3)	# 12-14

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('mi000_00', 2)	# 1-2
    sprite('mi001_00', 8)	# 3-10
    sprite('mi001_01', 8)	# 11-18
    sprite('mi001_02', 8)	# 19-26
    sprite('mi001_03', 6)	# 27-32
    sprite('mi001_04', 6)	# 33-38
    sprite('mi001_05', 6)	# 39-44
    sprite('mi001_06', 6)	# 45-50
    sprite('mi001_07', 6)	# 51-56
    sprite('mi001_08', 6)	# 57-62
    sprite('mi001_09', 6)	# 63-68
    SFX_3('hair')
    sprite('mi001_10', 6)	# 69-74
    sprite('mi000_00', 22)	# 75-96

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
    sprite('mi020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('mi020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('mi010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
        Unknown21015('547375726172615f53686f740000000000000000000000000000000000000000e610000000000000')
    sprite('mi205_00', 3)	# 1-3
    sprite('mi205_01', 3)	# 4-6
    sprite('mi205_02', 3)	# 7-9
    sprite('mi205_03', 3)	# 10-12
    SFX_3('cloth_h')
    sprite('mi205_04', 4)	# 13-16
    Unknown7007('706d693231305f30000000000000000064000000706d693231305f31000000000000000064000000706d693231325f300000000000000000640000000000000000000000000000000000000000000000')
    GFX_1('persona_enter_ply', 0)
    sprite('mi205_05', 4)	# 17-20
    Unknown23029(11, 4320, 0)
    sprite('mi205_06', 4)	# 21-24
    sprite('mi205_04', 4)	# 25-28
    SFX_3('cloth_h')
    sprite('mi205_05', 4)	# 29-32
    sprite('mi205_06', 4)	# 33-36
    sprite('mi205_04', 4)	# 37-40
    SFX_3('cloth_h')
    sprite('mi205_05', 4)	# 41-44
    sprite('mi205_06', 4)	# 45-48
    sprite('mi205_04', 4)	# 49-52
    SFX_3('cloth_h')
    sprite('mi205_05', 4)	# 53-56
    sprite('mi205_06', 4)	# 57-60
    sprite('mi205_04', 4)	# 61-64
    SFX_3('cloth_h')
    sprite('mi205_05', 4)	# 65-68
    sprite('mi205_06', 4)	# 69-72
    sprite('mi205_04', 4)	# 73-76
    SFX_3('cloth_h')
    sprite('mi205_05', 4)	# 77-80
    sprite('mi205_06', 4)	# 81-84
    sprite('mi205_04', 4)	# 85-88
    SFX_3('cloth_h')
    sprite('mi205_05', 4)	# 89-92
    sprite('mi205_06', 4)	# 93-96
    sprite('mi205_04', 4)	# 97-100
    SFX_3('cloth_h')
    sprite('mi205_05', 4)	# 101-104
    sprite('mi205_06', 4)	# 105-108
    sprite('mi205_02', 4)	# 109-112
    sprite('mi205_01', 4)	# 113-116
    sprite('mi205_00', 4)	# 117-120

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)

        def upon_43():
            if (SLOT_48 == 7000):
                Recovery()
    sprite('mi204_00', 4)	# 1-4
    sprite('mi204_01', 4)	# 5-8
    sprite('mi204_02', 4)	# 9-12
    Unknown23029(11, 9980, 0)
    Unknown7007('706d693132305f30000000000000000064000000706d693132305f32000000000000000064000000706d693132315f30000000000000000064000000706d693132335f30000000000000000064000000')
    sprite('mi204_03', 4)	# 13-16
    sprite('mi204_04', 6)	# 17-22
    sprite('mi204_05', 6)	# 23-28
    sprite('mi204_01', 6)	# 29-34
    sprite('mi204_00', 6)	# 35-40
    sprite('mi204_06', 6)	# 41-46

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirUntechableTime(40)
        AirHitstunAfterWallbounce(40)
        PushbackX(30400)
        AirPushbackX(80000)
        AirPushbackY(10000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown9016(1)
        Unknown11056(2)
        Unknown9178(1)
        WallbounceReboundTime(20)

        def upon_12():
            PushbackX(39520)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
            Unknown2015(-1)
    sprite('mi401_00', 3)	# 1-3
    sprite('mi401_01', 2)	# 4-5
    sprite('mi401_02', 2)	# 6-7
    sprite('mi401_03', 3)	# 8-10
    Unknown7007('706d693230315f30000000000000000064000000706d693230315f32000000000000000064000000706d693230325f31000000000000000064000000706d693230325f32000000000000000064000000')
    sprite('mi401_04', 1)	# 11-11
    Unknown3029(1)
    sprite('mi401_04', 1)	# 12-12
    sprite('mi401_05ex', 2)	# 13-14	 **attackbox here**
    GFX_1('mief_401smoke_04', 0)
    GFX_0('mief_401', 1)
    RefreshMultihit()
    physicsXImpulse(50000)
    Unknown2015(220)
    SFX_3('airdash_m')
    sprite('mi401_06ex', 2)	# 15-16	 **attackbox here**
    SFX_3('slash_blade_fast')
    sprite('mi401_05ex', 2)	# 17-18	 **attackbox here**
    SFX_3('slash_rapier_fast')
    sprite('mi401_06', 2)	# 19-20	 **attackbox here**
    sprite('mi401_05', 2)	# 21-22	 **attackbox here**
    sprite('mi401_07', 3)	# 23-25
    Recovery()
    Unknown1019(30)
    Unknown3029(0)
    sprite('mi401_08', 3)	# 26-28
    Unknown1019(60)
    Unknown2015(-1)
    sprite('mi401_09', 3)	# 29-31
    GFX_1('mief_401stopsmoke_03', 0)
    Unknown1019(60)
    sprite('mi401_10', 4)	# 32-35
    sprite('mi401_11', 4)	# 36-39
    Unknown1019(0)
    sprite('mi401_12', 4)	# 40-43

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
    teleportRelativeX(-260000)
    Unknown1019(4)
    label(0)
    sprite('mi020_07', 4)	# 3-6
    sprite('mi020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    Unknown1084(1)
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
        setInvincible(1)
    sprite('mi431_00', 4)	# 1-4
    sprite('mi431_01', 4)	# 5-8
    sprite('mi431_02', 6)	# 9-14
    sprite('mi431_03', 6)	# 15-20
    sprite('mi431_04', 6)	# 21-26
    sprite('mi431_02', 6)	# 27-32
    sprite('mi431_03', 6)	# 33-38
    sprite('mi431_04', 6)	# 39-44
    Unknown23029(11, 4312, 0)
    sprite('mi431_02', 6)	# 45-50
    GFX_1('persona_enter_ply', 0)
    sprite('mi431_03', 6)	# 51-56
    sprite('mi431_04', 6)	# 57-62
    sprite('mi431_05', 4)	# 63-66
    SFX_3('cloth_m')
    Unknown7007('706d693235345f30000000000000000064000000706d693235345f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('mi431_06', 4)	# 67-70
    sprite('mi431_07', 6)	# 71-76
    sprite('mi431_08', 6)	# 77-82
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 83-88
    setInvincible(0)
    sprite('mi431_10', 6)	# 89-94
    sprite('mi431_08', 6)	# 95-100
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 101-106
    sprite('mi431_10', 6)	# 107-112
    sprite('mi431_08', 6)	# 113-118
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 119-124
    sprite('mi431_10', 6)	# 125-130
    sprite('mi431_08', 6)	# 131-136
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 137-142
    sprite('mi431_10', 6)	# 143-148
    sprite('mi431_02', 6)	# 149-154
    sprite('mi431_01', 6)	# 155-160
    sprite('mi431_00', 4)	# 161-164

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)
    sprite('mi431_00', 4)	# 1-4
    sprite('mi431_01', 4)	# 5-8
    sprite('mi431_02', 6)	# 9-14
    Unknown2021(1)
    sprite('mi431_03', 6)	# 15-20
    sprite('mi431_04', 6)	# 21-26
    sprite('mi431_03', 6)	# 27-32
    ScreenShake(8000, 8000)
    sprite('mi431_02', 6)	# 33-38
    ScreenShake(12000, 12000)
    SFX_3('quake_s')
    sprite('mi431_03', 6)	# 39-44
    ScreenShake(12000, 12000)
    Unknown23029(11, 4313, 0)
    sprite('mi431_02', 6)	# 45-50
    ScreenShake(12000, 12000)
    GFX_1('persona_enter_ply', 0)
    sprite('mi431_03', 6)	# 51-56
    ScreenShake(16000, 16000)
    SFX_3('quake_s')
    sprite('mi431_04', 6)	# 57-62
    ScreenShake(16000, 16000)
    sprite('mi431_05', 4)	# 63-66
    ScreenShake(16000, 16000)
    SFX_3('cloth_m')
    Unknown7007('706d693235345f30000000000000000064000000706d693235345f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('mi431_06', 4)	# 67-70
    sprite('mi431_07', 6)	# 71-76
    sprite('mi431_08', 6)	# 77-82
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 83-88
    setInvincible(0)
    sprite('mi431_10', 6)	# 89-94
    sprite('mi431_08', 6)	# 95-100
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 101-106
    sprite('mi431_10', 6)	# 107-112
    sprite('mi431_08', 6)	# 113-118
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 119-124
    sprite('mi431_10', 6)	# 125-130
    sprite('mi431_08', 6)	# 131-136
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 137-142
    sprite('mi431_10', 6)	# 143-148
    sprite('mi431_02', 6)	# 149-154
    Unknown2021(0)
    sprite('mi431_01', 6)	# 155-160
    sprite('mi431_00', 4)	# 161-164

@State
def CmnActChangeRequest():
    pass

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
    sprite('mi251_01', 4)	# 121-124
    Unknown1086(22)
    teleportRelativeX(-180000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    sprite('mi251_02', 1)	# 125-125
    sprite('mi251_03', 2)	# 126-127
    SFX_3('slash_pole_middle')
    sprite('mi251_04', 32767)	# 128-32894	 **attackbox here**
    label(9)
    sprite('mi230_00', 23)	# 32895-32917
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('mi010_01', 4)	# 32918-32921
    sprite('mi010_00', 4)	# 32922-32925

@State
def CmnActChangeReturnAppealBurst():
    sprite('mi064_01', 45)	# 1-45
    sprite('mi064_02', 3)	# 46-48
    sprite('mi064_03', 3)	# 49-51
    sprite('mi010_01', 3)	# 52-54
    sprite('mi010_00', 3)	# 55-57
    sprite('mi000_00', 23)	# 58-80

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Hitstop(7)
        AirPushbackY(16000)
        PushbackX(15300)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown1112('')
    sprite('mi200_00', 3)	# 1-3
    physicsXImpulse(5000)
    sprite('mi200_01', 3)	# 4-6
    Unknown1051(80)
    sprite('mi200_02', 1)	# 7-7	 **attackbox here**
    StartMultihit()
    Unknown7009(0)
    sprite('mi200_03', 1)	# 8-8	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('mi200_04', 2)	# 9-10	 **attackbox here**
    sprite('mi200_05', 1)	# 11-11
    Recovery()
    Unknown2063()
    physicsXImpulse(0)
    sprite('mi200_06', 1)	# 12-12
    sprite('mi200_06', 5)	# 13-17
    sprite('mi200_07', 1)	# 18-18
    sprite('mi200_07', 5)	# 19-23
    sprite('mi200_08', 6)	# 24-29

@Subroutine
def __5ASmartComboInit():
    AttackLevel_(3)
    AttackP2(85)
    Unknown9016(1)
    AirPushbackX(12000)
    AirPushbackY(12000)
    Unknown11028(13)
    PushbackX(15300)
    Hitstop(7)
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('CmnActCrushAttack')
    HitOrBlockCancel('NmlAtk2C')

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('5ASmartComboInit')
        Damage(1100)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_ON_HIT_OR_BLOCK():
            Unknown14070('NmlAtk5A3rd')
            Unknown2037(1)
    sprite('mi200_09', 1)	# 1-1
    sprite('mi201_00', 1)	# 2-2
    physicsXImpulse(7500)
    sprite('mi201_01', 1)	# 3-3
    physicsXImpulse(15000)
    sprite('mi201_02', 1)	# 4-4
    physicsXImpulse(30000)
    sprite('mi201_03', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    GFX_0('mief201_Zanzoh', 100)
    Unknown1019(80)
    Unknown7009(1)
    sprite('mi201_04', 1)	# 6-6	 **attackbox here**
    Unknown1019(60)
    sprite('mi201_05', 1)	# 7-7
    Recovery()
    Unknown2063()
    Unknown1019(30)
    sprite('mi201_06', 1)	# 8-8
    physicsXImpulse(0)
    sprite('mi201_07', 1)	# 9-9
    if SLOT_2:
        Unknown14072('NmlAtk5A3rd')
    sprite('mi201_07', 3)	# 10-12
    sprite('mi201_08', 1)	# 13-13
    sprite('mi201_08', 1)	# 14-14
    Unknown14074('NmlAtk5A3rd')
    sprite('mi201_08', 4)	# 15-18
    sprite('mi201_09', 5)	# 19-23
    sprite('mi201_10', 5)	# 24-28

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('5ASmartComboInit')
        Damage(1200)
        HitJumpCancel(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown14070('NmlAtk5A4th')
            Unknown2037(1)
    sprite('mi201_11', 2)	# 1-2
    physicsXImpulse(5000)
    sprite('mi202_01', 1)	# 3-3
    sprite('mi202_02', 1)	# 4-4
    GFX_0('mief202_Zanzoh', 100)
    sprite('mi202_03', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    SFX_3('slash_knife_slow')
    Unknown7009(0)
    sprite('mi202_04', 1)	# 6-6	 **attackbox here**
    sprite('mi202_05', 1)	# 7-7
    Recovery()
    Unknown2063()
    sprite('mi202_05', 4)	# 8-11
    if SLOT_2:
        Unknown14072('NmlAtk5A4th')
    sprite('mi202_06', 1)	# 12-12
    sprite('mi202_06', 1)	# 13-13
    Unknown14074('NmlAtk5A4th')
    sprite('mi202_06', 1)	# 14-14
    sprite('mi201_07', 5)	# 15-19
    sprite('mi201_08', 5)	# 20-24
    sprite('mi201_09', 4)	# 25-28
    sprite('mi201_10', 4)	# 29-32

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('5ASmartComboInit')
        Damage(1300)

        def upon_ON_HIT_OR_BLOCK():
            Unknown14070('NmlAtk5A5th')
            Unknown2037(1)
    sprite('mi202_11', 1)	# 1-1
    sprite('mi201_00', 1)	# 2-2
    physicsXImpulse(7500)
    sprite('mi201_01', 1)	# 3-3
    physicsXImpulse(15000)
    sprite('mi201_02', 1)	# 4-4
    physicsXImpulse(30000)
    sprite('mi201_03', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    GFX_0('mief201_Zanzoh', 100)
    Unknown1019(80)
    Unknown7009(1)
    sprite('mi201_04', 1)	# 6-6	 **attackbox here**
    Unknown1019(60)
    sprite('mi201_05', 1)	# 7-7
    Recovery()
    Unknown2063()
    Unknown1019(30)
    sprite('mi201_06', 1)	# 8-8
    physicsXImpulse(0)
    sprite('mi201_07', 1)	# 9-9
    if SLOT_2:
        Unknown14072('NmlAtk5A5th')
    sprite('mi201_07', 3)	# 10-12
    sprite('mi201_08', 1)	# 13-13
    sprite('mi201_08', 1)	# 14-14
    Unknown14074('NmlAtk5A5th')
    sprite('mi201_08', 4)	# 15-18
    sprite('mi201_09', 5)	# 19-23
    sprite('mi201_10', 5)	# 24-28

@State
def NmlAtk5A5th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('5ASmartComboInit')
        Damage(1400)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A6th')
    sprite('mi201_11', 2)	# 1-2
    physicsXImpulse(5000)
    sprite('mi202_01', 1)	# 3-3
    sprite('mi202_02', 1)	# 4-4
    GFX_0('mief202_Zanzoh', 100)
    sprite('mi202_03', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    SFX_3('slash_knife_slow')
    Unknown7009(1)
    sprite('mi202_04', 1)	# 6-6	 **attackbox here**
    sprite('mi202_05', 5)	# 7-11
    Recovery()
    Unknown2063()
    sprite('mi202_06', 3)	# 12-14
    sprite('mi201_07', 5)	# 15-19
    sprite('mi201_08', 5)	# 20-24
    sprite('mi201_09', 4)	# 25-28
    sprite('mi201_10', 4)	# 29-32

@State
def NmlAtk5A6th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 7000):
                Recovery()
    sprite('mi204_00', 4)	# 1-4
    sprite('mi204_01', 4)	# 5-8
    sprite('mi204_02', 4)	# 9-12
    Unknown23029(11, 9990, 0)
    sprite('mi204_03', 4)	# 13-16
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706d693132305f32000000000000000064000000706d693132315f32000000000000000064000000706d693132335f30000000000000000064000000706d693132335f31000000000000000064000000')
    sprite('mi204_04', 4)	# 17-20
    sprite('mi204_05', 4)	# 21-24
    sprite('mi204_03', 5)	# 25-29
    SFX_3('cloth_h')
    sprite('mi204_04', 5)	# 30-34
    sprite('mi204_05', 5)	# 35-39
    sprite('mi204_03', 6)	# 40-45
    sprite('mi204_04', 6)	# 46-51
    sprite('mi204_05', 6)	# 52-57
    sprite('mi204_01', 5)	# 58-62
    sprite('mi204_00', 5)	# 63-67
    sprite('mi204_06', 4)	# 68-71

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirUntechableTime(40)
        Unknown9016(1)
        AirPushbackX(8000)
        AirPushbackY(4000)
        Unknown11001(0, 4, 9)
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        sendToLabelUpon(2, 1)
        physicsXImpulse(0)
        if CheckInput(0x5f):
            Unknown1015(-9000)
        if CheckInput(0x79):
            Unknown1015(12000)
    sprite('mi203_00', 3)	# 1-3
    sprite('mi203_01', 2)	# 4-5
    SFX_3('cloth_m')
    physicsYImpulse(7500)
    setGravity(2500)
    sprite('mi203_01', 1)	# 6-6
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000000000000')
    sprite('mi203_02', 3)	# 7-9
    sprite('mi203_03', 3)	# 10-12
    sprite('mi203_02', 3)	# 13-15
    sprite('mi203_03', 3)	# 16-18
    label(0)
    sprite('mi203_02', 3)	# 19-21
    sprite('mi203_03', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('mi203_04', 1)	# 25-25
    Unknown1084(1)
    clearUponHandler(3)
    Unknown20(2, 2, 51)
    sprite('mi203_05', 1)	# 26-26
    GFX_0('mief203_Zanzoh', 100)
    SFX_3('slash_rapier_middle')
    Unknown7009(5)
    sprite('mi203_06', 3)	# 27-29	 **attackbox here**
    RefreshMultihit()
    sprite('mi203_07', 3)	# 30-32
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('mi203_08', 8)	# 33-40
    sprite('mi203_09', 4)	# 41-44
    sprite('mi203_10', 4)	# 45-48
    sprite('mi203_11', 4)	# 49-52

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        AirPushbackX(16000)
        AirUntechableTime(21)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B3rd')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
    sprite('mi207_00', 2)	# 1-2
    sprite('mi207_01', 1)	# 3-3
    sprite('mi207_02', 3)	# 4-6
    physicsXImpulse(15000)
    sprite('mi207_02', 3)	# 7-9
    Unknown1019(350)
    SFX_3('slash_rapier_middle')
    Unknown7009(4)
    sprite('mi207_03', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    GFX_0('mief207_Zanzoh', 100)
    sprite('mi207_04', 3)	# 13-15	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('mi207_05', 3)	# 16-18
    sprite('mi207_06', 3)	# 19-21
    sprite('mi207_07', 3)	# 22-24
    sprite('mi207_08', 3)	# 25-27
    sprite('mi207_09', 3)	# 28-30

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1000)
        AttackP2(90)
        AirUntechableTime(30)
        AirPushbackX(20000)
        AirPushbackY(15000)
        Unknown9016(1)
        Hitstop(1)
        PushbackX(30400)
        Unknown30055('20a107001e0000000a000000')
        Unknown30056('f04902001e00000000000000')
        Unknown11057(700)
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('mi208_00', 3)	# 1-3
    sprite('mi208_01', 3)	# 4-6
    sprite('mi208_02', 3)	# 7-9
    Unknown7009(2)
    sprite('mi208_03', 4)	# 10-13	 **attackbox here**
    Unknown8007(100, 1, 1)
    RefreshMultihit()
    physicsXImpulse(15000)
    SFX_3('slash_rapier_fast')
    sprite('mi208_04', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    Unknown1019(150)
    SFX_3('slash_rapier_fast')
    sprite('mi208_05', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    Unknown1019(150)
    SFX_3('slash_rapier_fast')
    sprite('mi208_06', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    Unknown1019(80)
    Unknown8010(100, 1, 1)
    SFX_3('slash_rapier_fast')
    sprite('mi208_03', 3)	# 23-25	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    SFX_3('slash_rapier_fast')
    sprite('mi208_07', 3)	# 26-28
    Recovery()
    Unknown2063()
    Unknown1019(60)
    Unknown8010(100, 1, 1)
    sprite('mi208_08', 3)	# 29-31
    Unknown1019(50)
    sprite('mi208_09', 3)	# 32-34
    sprite('mi208_10', 3)	# 35-37
    Unknown1019(0)
    sprite('mi203_09', 3)	# 38-40
    sprite('mi203_10', 3)	# 41-43
    sprite('mi203_11', 3)	# 44-46

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        Hitstop(7)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2ARenda')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('mi230_00', 2)	# 1-2
    sprite('mi230_01', 1)	# 3-3
    sprite('mi230_01', 3)	# 4-6
    Unknown1051(80)
    sprite('mi230_02', 2)	# 7-8
    Unknown7009(3)
    sprite('mi230_03', 3)	# 9-11	 **attackbox here**
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('mi230_04', 6)	# 12-17
    Recovery()
    Unknown2063()
    sprite('mi230_02', 3)	# 18-20
    sprite('mi230_01', 3)	# 21-23
    sprite('mi230_00', 3)	# 24-26

@State
def NmlAtk2ARenda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        Hitstop(7)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2ARenda')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('mi230_01', 5)	# 1-5
    sprite('mi230_02', 3)	# 6-8
    Unknown7009(3)
    sprite('mi230_03', 3)	# 9-11	 **attackbox here**
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('mi230_04', 6)	# 12-17
    Recovery()
    Unknown2063()
    sprite('mi230_02', 3)	# 18-20
    sprite('mi230_01', 3)	# 21-23
    sprite('mi230_00', 3)	# 24-26

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        Unknown9016(1)
        AirUntechableTime(25)
        AirPushbackX(10000)
        AirPushbackY(30000)
        GroundedHitstunAnimation(1)
        Unknown11058('0000000001000000000000000000000000000000')
        HitCancel('NmlAtk2B2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
    sprite('mi231_00', 4)	# 1-4
    sprite('mi231_01', 2)	# 5-6
    sprite('mi231_01', 1)	# 7-7
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('mi231_01', 1)	# 8-8
    sprite('mi231_02', 2)	# 9-10
    SFX_3('slash_pole_middle')
    Unknown7007('706d693130365f30000000000000000064000000706d693130365f31000000000000000064000000706d693130355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('mi231_03', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    sprite('mi231_04', 5)	# 14-18
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('mi231_05', 5)	# 19-23
    sprite('mi231_06', 5)	# 24-28
    sprite('mi231_03', 4)	# 29-32	 **attackbox here**
    StartMultihit()
    sprite('mi231_02', 4)	# 33-36
    sprite('mi231_01', 4)	# 37-40
    sprite('mi231_00', 4)	# 41-44

@State
def NmlAtk2B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Unknown11063(1)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 2331):
                HitOrBlockCancel('NmlAtk5B')
                HitOrBlockCancel('CmnActCrushAttack')
                HitOrBlockCancel('NmlAtk2C')
                Unknown14082(1)
            if (SLOT_48 == 7000):
                Recovery()
    sprite('mi233_00', 4)	# 1-4
    sprite('mi233_01', 4)	# 5-8
    sprite('mi233_02', 4)	# 9-12
    sprite('mi233_03', 4)	# 13-16
    Unknown23029(11, 2330, 0)
    sprite('mi233_04', 4)	# 17-20
    SFX_3('cloth_h')
    Unknown7007('706d693132305f31000000000000000064000000706d693132315f30000000000000000064000000706d693132325f30000000000000000064000000706d693132345f30000000000000000064000000')
    GFX_1('persona_enter_ply', 0)
    sprite('mi233_05', 4)	# 21-24
    sprite('mi233_06', 4)	# 25-28
    sprite('mi233_04', 4)	# 29-32
    SFX_3('cloth_h')
    sprite('mi233_05', 4)	# 33-36
    sprite('mi233_06', 4)	# 37-40
    sprite('mi233_04', 4)	# 41-44
    SFX_3('cloth_h')
    sprite('mi233_05', 4)	# 45-48
    sprite('mi233_06', 4)	# 49-52
    sprite('mi233_04', 4)	# 53-56
    SFX_3('cloth_h')
    sprite('mi233_05', 4)	# 57-60
    sprite('mi233_06', 4)	# 61-64
    sprite('mi233_02', 4)	# 65-68
    sprite('mi233_01', 4)	# 69-72
    sprite('mi233_00', 4)	# 73-76

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(5000)
        AirPushbackY(20000)
        AirUntechableTime(40)
        Unknown9016(1)
    sprite('mi211_00ex', 5)	# 1-5
    sprite('mi211_01', 3)	# 6-8
    physicsXImpulse(30000)
    Unknown8007(100, 1, 0)
    sprite('mi211_02', 3)	# 9-11
    Unknown8007(100, 1, 0)
    sprite('mi211_03', 3)	# 12-14
    Unknown1019(50)
    sprite('mi211_04', 2)	# 15-16
    sprite('mi211_05', 2)	# 17-18
    Unknown1019(50)
    GFX_0('mief211_Zanzoh', 100)
    SFX_3('slash_rapier_middle')
    Unknown7007('706d693130375f30000000000000000064000000706d693130375f31000000000000000064000000706d693130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('mi211_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('mi211_06', 3)	# 21-23	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    setInvincible(0)
    Unknown8010(100, 1, 1)
    sprite('mi211_07', 6)	# 24-29
    Unknown1019(0)
    sprite('mi211_08', 3)	# 30-32
    sprite('mi211_09', 3)	# 33-35
    sprite('mi211_10', 3)	# 36-38
    sprite('mi211_11', 2)	# 39-40

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('mi250_00', 3)	# 1-3
    sprite('mi250_01', 3)	# 4-6
    SFX_3('slash_rapier_fast')
    Unknown7009(0)
    sprite('mi250_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('mi250_03', 2)	# 9-10	 **attackbox here**
    sprite('mi250_04', 2)	# 11-12	 **attackbox here**
    sprite('mi250_02', 2)	# 13-14	 **attackbox here**
    sprite('mi250_03', 2)	# 15-16	 **attackbox here**
    sprite('mi250_04', 2)	# 17-18	 **attackbox here**
    sprite('mi250_05', 4)	# 19-22
    Recovery()
    Unknown2063()
    sprite('mi250_06', 4)	# 23-26
    sprite('mi250_07', 4)	# 27-30
    sprite('mi250_08', 4)	# 31-34

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Unknown4009(11)
    sprite('mi255_00', 2)	# 1-2
    sprite('mi255_01', 2)	# 3-4
    sprite('mi255_02', 3)	# 5-7
    Unknown23029(11, 2540, 0)
    Unknown7007('706d693132305f30000000000000000064000000706d693132315f30000000000000000064000000706d693132335f30000000000000000064000000706d693132335f31000000000000000064000000')

    def upon_LANDING():
        Unknown23029(11, 9999, 0)
    sprite('mi255_03', 3)	# 8-10
    SFX_3('cloth_h')
    sprite('mi255_04', 1)	# 11-11
    GFX_1('persona_enter_ply', 0)
    sprite('mi255_04', 4)	# 12-15
    sprite('mi255_05', 4)	# 16-19
    sprite('mi255_05', 1)	# 20-20
    Recovery()
    Unknown2063()
    sprite('mi255_06', 5)	# 21-25
    sprite('mi255_02', 4)	# 26-29
    sprite('mi255_01', 4)	# 30-33
    sprite('mi255_00', 4)	# 34-37

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(50)
        AirPushbackX(24000)
        AirPushbackY(-36000)
        Unknown9016(1)
        HitJumpCancel(1)
        HitCancel('NmlAtkAIR5A')
        HitCancel('NmlAtkAIR5C')
    sprite('mi251_00', 2)	# 1-2
    sprite('mi251_01', 5)	# 3-7
    sprite('mi251_02', 1)	# 8-8
    sprite('mi251_03', 2)	# 9-10
    SFX_3('slash_pole_middle')
    Unknown7009(2)
    sprite('mi251_04', 6)	# 11-16	 **attackbox here**
    RefreshMultihit()
    sprite('mi251_05', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('mi251_06', 4)	# 20-23
    sprite('mi251_07', 4)	# 24-27
    sprite('mi251_08', 4)	# 28-31
    sprite('mi251_09', 4)	# 32-35
    sprite('mi251_10', 6)	# 36-41

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)

        def upon_STATE_END():
            if (not SLOT_2):
                Unknown1018()
                Unknown1038()
                Unknown1019(85)
                YAccel(85)

        def upon_43():
            if (SLOT_48 == 7000):
                Recovery()
            if (SLOT_48 == 2551):
                HitOrBlockCancel('NmlAtkAIR5A')
                HitOrBlockCancel('NmlAtkAIR5B')
    sprite('mi254_00', 4)	# 1-4
    sprite('mi254_01', 4)	# 5-8
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown23029(11, 2550, 0)
    Unknown7007('706d693132335f30000000000000000064000000706d693132335f32000000000000000064000000706d693132345f31000000000000000064000000706d693132345f32000000000000000064000000')
    sprite('mi254_02', 4)	# 9-12
    sprite('mi254_03', 4)	# 13-16
    GFX_1('persona_enter_ply', 0)
    SFX_3('cloth_h')
    sprite('mi254_04', 4)	# 17-20
    Unknown22004(5, 5)
    sprite('mi254_05', 4)	# 21-24
    sprite('mi254_03', 4)	# 25-28
    sprite('mi254_04', 4)	# 29-32
    sprite('mi254_05', 4)	# 33-36
    sprite('mi254_03', 4)	# 37-40
    sprite('mi254_04', 4)	# 41-44
    Unknown1018()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    Unknown2037(1)
    sprite('mi254_05', 4)	# 45-48
    sprite('mi254_03', 4)	# 49-52
    sprite('mi254_04', 4)	# 53-56
    sprite('mi254_05', 4)	# 57-60
    sprite('mi254_00', 4)	# 61-64

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('mi210_00', 3)	# 1-3
    sprite('mi210_01', 3)	# 4-6
    sprite('mi210_02', 3)	# 7-9
    Unknown1084(1)
    SFX_3('highjump_l')
    physicsYImpulse(20000)
    setGravity(1500)
    physicsXImpulse(9000)
    tag_voice(1, 'pmi156_0', 'pmi156_1', '', '')
    sprite('mi210_03', 3)	# 10-12
    sprite('mi210_04', 3)	# 13-15
    sprite('mi210_05', 3)	# 16-18
    sprite('mi210_06', 3)	# 19-21
    sprite('mi210_07', 2)	# 22-23
    sprite('mi210_08', 2)	# 24-25
    SFX_3('slash_rapier_middle')
    GFX_0('mief210_Zanzoh', 100)
    sprite('mi210_09', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    sprite('mi210_10', 3)	# 29-31
    sprite('mi210_11', 3)	# 32-34
    sprite('mi020_04', 3)	# 35-37
    sprite('mi020_05', 3)	# 38-40
    sprite('mi020_06', 3)	# 41-43
    label(0)
    sprite('mi020_07', 3)	# 44-46
    sprite('mi020_08', 3)	# 47-49
    gotoLabel(0)
    label(1)
    sprite('mi230_00', 10)	# 50-59
    Unknown1084(1)
    Unknown18009(1)
    Unknown8000(100, 1, 1)

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        Unknown23027()
        physicsXImpulse(5000)
        setGravity(3000)
        sendToLabelUpon(2, 2)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('mi210_10', 3)	# 2-4
    sprite('mi210_11', 3)	# 5-7
    sprite('mi020_04', 3)	# 8-10
    sprite('mi020_05', 3)	# 11-13
    sprite('mi020_06', 3)	# 14-16
    label(0)
    sprite('mi020_07', 3)	# 17-19
    sprite('mi020_08', 3)	# 20-22
    gotoLabel(0)
    label(2)
    sprite('mi230_00', 3)	# 23-25
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('mi010_01', 3)	# 26-28
    sprite('mi010_00', 3)	# 29-31
    sprite('mi207_00', 2)	# 32-33
    sprite('mi207_01', 1)	# 34-34
    sprite('mi207_02', 3)	# 35-37
    sprite('mi207_02', 3)	# 38-40
    SFX_3('slash_rapier_middle')
    sprite('mi207_03', 3)	# 41-43	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief207_Zanzoh', 100)
    sprite('mi207_04', 3)	# 44-46	 **attackbox here**
    sprite('mi207_05', 3)	# 47-49
    tag_voice(0, 'pmi157_0', 'pmi157_1', '', '')
    sprite('mi207_06', 3)	# 50-52
    sprite('mi207_07', 3)	# 53-55
    sprite('mi207_08', 3)	# 56-58
    sprite('mi207_09', 3)	# 59-61
    sprite('mi001_00', 8)	# 62-69
    sprite('mi001_01', 8)	# 70-77
    sprite('mi001_02', 8)	# 78-85
    sprite('mi001_03', 6)	# 86-91
    sprite('mi001_04', 6)	# 92-97
    sprite('mi001_05', 6)	# 98-103
    sprite('mi001_06', 6)	# 104-109
    sprite('mi001_07', 6)	# 110-115
    sprite('mi001_08', 6)	# 116-121
    sprite('mi001_09', 6)	# 122-127
    SFX_3('hair')
    sprite('mi001_10', 6)	# 128-133
    label(0)
    sprite('mi000_00', 8)	# 134-141
    sprite('mi000_01', 8)	# 142-149
    sprite('mi000_02', 8)	# 150-157
    sprite('mi000_03', 8)	# 158-165
    sprite('mi000_04', 8)	# 166-173
    sprite('mi000_05', 8)	# 174-181
    sprite('mi000_06', 8)	# 182-189
    sprite('mi000_07', 8)	# 190-197
    sprite('mi000_08', 8)	# 198-205
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 206-206

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('mi010_01', 2)	# 1-2
    sprite('mi211_00', 2)	# 3-4
    sprite('mi211_01', 2)	# 5-6
    sprite('mi211_02', 2)	# 7-8
    sprite('mi211_03', 2)	# 9-10
    sprite('mi211_04', 2)	# 11-12
    sprite('mi211_05', 2)	# 13-14
    GFX_0('mief211_Zanzoh_CA', 100)
    SFX_3('slash_rapier_middle')
    sprite('mi211_06', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('mi211_07', 3)	# 18-20
    sprite('mi211_08', 3)	# 21-23
    sprite('mi211_09', 3)	# 24-26
    sprite('mi211_10', 3)	# 27-29
    sprite('mi211_11', 3)	# 30-32
    sprite('mi010_00', 3)	# 33-35
    sprite('mi000_00', 3)	# 36-38
    sprite('mi430_17', 3)	# 39-41
    teleportRelativeX(20000)
    sprite('mi430_18', 200)	# 42-241
    sprite('mi001_00', 8)	# 242-249
    sprite('mi001_01', 8)	# 250-257
    sprite('mi001_02', 8)	# 258-265
    sprite('mi001_03', 6)	# 266-271
    sprite('mi001_04', 6)	# 272-277
    sprite('mi001_05', 6)	# 278-283
    sprite('mi001_06', 6)	# 284-289
    sprite('mi001_07', 6)	# 290-295
    sprite('mi001_08', 6)	# 296-301
    sprite('mi001_09', 6)	# 302-307
    SFX_3('hair')
    sprite('mi001_10', 6)	# 308-313
    label(0)
    sprite('mi000_00', 8)	# 314-321
    sprite('mi000_01', 8)	# 322-329
    sprite('mi000_02', 8)	# 330-337
    sprite('mi000_03', 8)	# 338-345
    sprite('mi000_04', 8)	# 346-353
    sprite('mi000_05', 8)	# 354-361
    sprite('mi000_06', 8)	# 362-369
    sprite('mi000_07', 8)	# 370-377
    sprite('mi000_08', 8)	# 378-385
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 386-386

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)

        def upon_STATE_END():
            teleportRelativeX(-30000)
    sprite('mi430_19', 15)	# 1-15
    sprite('mi430_20', 4)	# 16-19
    tag_voice(0, 'pmi158_0', 'pmi158_1', '', '')
    sprite('mi430_21', 5)	# 20-24	 **attackbox here**
    RefreshMultihit()
    Unknown8007(100, 1, 1)
    SFX_3('grip_hugs')
    sprite('mi430_21', 11)	# 25-35	 **attackbox here**
    sprite('mi430_22', 5)	# 36-40
    sprite('mi430_23', 5)	# 41-45
    sprite('mi430_24', 5)	# 46-50
    sprite('mi430_25', 5)	# 51-55
    sprite('mi430_26', 5)	# 56-60
    sprite('mi430_27', 5)	# 61-65

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 8)	# 26-33
    sprite('mi401_00', 2)	# 34-35
    teleportRelativeX(-1000000)
    SLOT_12 = SLOT_19
    Unknown1019(7)
    sprite('mi401_01', 2)	# 36-37
    sprite('mi401_02', 2)	# 38-39
    sprite('mi401_04', 1)	# 40-40
    SFX_3('airdash_m')
    sprite('mi401_04', 1)	# 41-41
    SFX_3('slash_blade_fast')
    sprite('mi401_05', 2)	# 42-43	 **attackbox here**
    GFX_1('mief_401smoke_04', 0)
    GFX_0('mief_401', 1)
    RefreshMultihit()
    Unknown2015(220)
    SFX_3('slash_rapier_fast')
    sprite('mi401_06', 2)	# 44-45	 **attackbox here**
    Unknown1019(8)
    sprite('mi401_07', 3)	# 46-48
    Unknown1019(8)
    sprite('mi401_08', 3)	# 49-51
    Unknown1019(8)
    Unknown2015(-1)
    sprite('mi401_09', 2)	# 52-53
    GFX_1('mief_401stopsmoke_03', 0)
    Unknown1019(8)
    sprite('mi401_10', 2)	# 54-55
    sprite('mi401_11', 2)	# 56-57
    Unknown1019(0)
    sprite('mi401_12', 3)	# 58-60
    sprite('mi000_00', 8)	# 61-68
    sprite('mi000_01', 8)	# 69-76
    sprite('mi000_02', 8)	# 77-84
    sprite('mi000_03', 8)	# 85-92
    sprite('mi000_04', 8)	# 93-100
    sprite('mi000_05', 8)	# 101-108
    sprite('mi000_06', 8)	# 109-116
    sprite('mi000_07', 8)	# 117-124
    sprite('mi000_08', 8)	# 125-132

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('mi203_00', 2)	# 1-2
    sprite('mi203_01', 2)	# 3-4
    SFX_3('cloth_m')
    physicsYImpulse(20000)
    setGravity(18000)
    sprite('mi203_02', 2)	# 5-6
    sprite('mi203_03', 2)	# 7-8
    sprite('mi203_02', 2)	# 9-10
    sprite('mi203_03', 2)	# 11-12
    label(0)
    sprite('mi203_02', 2)	# 13-14
    sprite('mi203_03', 2)	# 15-16
    gotoLabel(0)
    label(1)
    sprite('mi203_04', 2)	# 17-18
    Unknown1084(1)
    clearUponHandler(3)
    sprite('mi203_05', 2)	# 19-20
    GFX_0('mief203_Zanzoh', 100)
    SFX_3('slash_rapier_middle')
    sprite('mi203_06', 3)	# 21-23	 **attackbox here**
    RefreshMultihit()
    sprite('mi203_07', 3)	# 24-26
    sprite('mi203_08', 3)	# 27-29
    sprite('mi203_09', 3)	# 30-32
    sprite('mi203_10', 3)	# 33-35
    sprite('mi000_00', 3)	# 36-38
    sprite('mi430_17', 3)	# 39-41
    teleportRelativeX(20000)
    sprite('mi430_18', 200)	# 42-241
    sprite('mi001_00', 8)	# 242-249
    sprite('mi001_01', 8)	# 250-257
    sprite('mi001_02', 8)	# 258-265
    sprite('mi001_03', 6)	# 266-271
    sprite('mi001_04', 6)	# 272-277
    sprite('mi001_05', 6)	# 278-283
    sprite('mi001_06', 6)	# 284-289
    sprite('mi001_07', 6)	# 290-295
    sprite('mi001_08', 6)	# 296-301
    sprite('mi001_09', 6)	# 302-307
    SFX_3('hair')
    sprite('mi001_10', 6)	# 308-313
    sprite('mi000_00', 8)	# 314-321
    sprite('mi000_01', 8)	# 322-329
    sprite('mi000_02', 8)	# 330-337
    sprite('mi000_03', 8)	# 338-345
    sprite('mi000_04', 8)	# 346-353
    sprite('mi000_05', 8)	# 354-361
    sprite('mi000_06', 8)	# 362-369
    sprite('mi000_07', 8)	# 370-377
    sprite('mi000_08', 8)	# 378-385

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)

        def upon_STATE_END():
            teleportRelativeX(-30000)
    sprite('mi430_19', 15)	# 1-15
    sprite('mi430_20', 4)	# 16-19
    sprite('mi430_21', 5)	# 20-24	 **attackbox here**
    RefreshMultihit()
    Unknown8007(100, 1, 1)
    SFX_3('grip_hugs')
    sprite('mi430_21', 11)	# 25-35	 **attackbox here**
    sprite('mi430_22', 5)	# 36-40
    sprite('mi430_23', 5)	# 41-45
    sprite('mi430_24', 5)	# 46-50
    sprite('mi430_25', 5)	# 51-55
    sprite('mi430_26', 5)	# 56-60
    sprite('mi430_27', 5)	# 61-65

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
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('mi032_00', 2)	# 1-2
    label(0)
    sprite('mi032_01', 4)	# 3-6
    sprite('mi032_02', 4)	# 7-10
    sprite('mi032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('mi032_04', 4)	# 15-18
    sprite('mi032_05', 4)	# 19-22
    sprite('mi032_06', 4)	# 23-26
    sprite('mi032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('mi032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi310_00', 3)	# 35-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('mi310_01', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('mi310_02', 3)	# 41-43
    sprite('mi310_03', 10)	# 44-53
    SFX_4('pmi154')
    sprite('mi310_04', 5)	# 54-58
    sprite('mi310_00', 5)	# 59-63

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(150)
        PushbackX(0)
        AttackP2(100)
        Unknown9154(60)
        Hitstop(0)
        Unknown9016(1)
        Unknown11057(500)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        JumpCancel_(0)
        Unknown11069('ThrowExe')
        Unknown11064(1)
    sprite('mi310_01', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(1, 80)
    sprite('mi311_00', 4)	# 4-7
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mi311_01', 4)	# 8-11
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mi311_02', 1)	# 12-12	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mi311_02', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    Unknown30079(1)
    GFX_0('mief_311', 100)
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_03', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_04', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_05', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_06', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_02', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311', 100)
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_03', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_04', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_05', 2)	# 29-30	 **attackbox here**
    RefreshMultihit()
    SFX_4('pmi153')
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_06', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    Unknown30079(0)
    sprite('mi311_07', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    Damage(350)
    AttackP2(50)
    AirUntechableTime(60)
    AirPushbackX(12000)
    AirPushbackY(32000)
    GroundedHitstunAnimation(10)
    Unknown11064(0)
    GFX_0('mief_311_HitEff', 100)

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
    Unknown11069('')
    sprite('mi311_08', 4)	# 36-39
    GFX_0('mief_311_finish', 100)
    sprite('mi311_09', 3)	# 40-42
    sprite('mi311_10', 3)	# 43-45
    sprite('mi311_11', 2)	# 46-47

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
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('mi032_00', 2)	# 1-2
    label(0)
    sprite('mi032_01', 4)	# 3-6
    sprite('mi032_02', 4)	# 7-10
    sprite('mi032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('mi032_04', 4)	# 15-18
    sprite('mi032_05', 4)	# 19-22
    sprite('mi032_06', 4)	# 23-26
    sprite('mi032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('mi032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi310_00', 3)	# 35-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('mi310_01', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('mi310_02', 3)	# 41-43
    sprite('mi310_03', 10)	# 44-53
    SFX_4('pmi154')
    sprite('mi310_04', 5)	# 54-58
    sprite('mi310_00', 5)	# 59-63

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(150)
        PushbackX(0)
        AttackP2(100)
        Unknown9154(60)
        Hitstop(0)
        Unknown9016(1)
        Unknown11057(500)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        JumpCancel_(0)
        Unknown11069('BackThrowExe')
        Unknown11064(1)
    sprite('mi310_01', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(1, 80)
    sprite('mi311_00', 4)	# 4-7
    Unknown2005()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mi311_01', 4)	# 8-11
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mi311_02', 1)	# 12-12	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mi311_02', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    Unknown30079(1)
    GFX_0('mief_311', 100)
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_03', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_04', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_05', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_06', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_02', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311', 100)
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_03', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_04', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_05', 2)	# 29-30	 **attackbox here**
    RefreshMultihit()
    SFX_4('pmi153')
    GFX_0('mief_311_HitEff', 100)
    sprite('mi311_06', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('mief_311_HitEff', 100)
    Unknown30079(0)
    sprite('mi311_07', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    Damage(350)
    AttackP2(50)
    AirUntechableTime(60)
    AirPushbackX(12000)
    AirPushbackY(32000)
    GroundedHitstunAnimation(10)
    Unknown11064(0)
    GFX_0('mief_311_HitEff', 100)

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
    Unknown11069('')
    sprite('mi311_08', 4)	# 36-39
    GFX_0('mief_311_finish', 100)
    sprite('mi311_09', 3)	# 40-42
    sprite('mi311_10', 3)	# 43-45
    sprite('mi311_11', 2)	# 46-47

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2400)
        Hitstop(16)
        AirPushbackX(15000)
        AirPushbackY(32000)
        GroundedHitstunAnimation(1)
        Unknown9016(1)
        AirUntechableTime(80)
        sendToLabelUpon(2, 1)
    sprite('mi400_00', 3)	# 1-3
    sprite('mi400_01', 3)	# 4-6
    SFX_3('highjump_l')
    sprite('mi400_02', 5)	# 7-11
    physicsXImpulse(15000)
    physicsYImpulse(32000)
    setGravity(1700)
    GFX_0('mief_400', 0)
    GFX_0('mief_400_2', 0)
    SFX_3('slash_pole_middle')
    sprite('mi400_03ex', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(90)
    Unknown7007('706d693230305f30000000000000000064000000706d693230305f31000000000000000064000000706d693230305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('mi400_03ex2', 1)	# 13-13	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    SFX_3('slash_rapier_middle')
    sprite('mi400_03ex3', 1)	# 14-14	 **attackbox here**
    sprite('mi400_03', 1)	# 15-15	 **attackbox here**
    setInvincible(0)
    StartMultihit()
    sprite('mi400_03', 2)	# 16-17	 **attackbox here**
    StartMultihit()
    Unknown1019(80)
    YAccel(80)
    sprite('mi400_04', 3)	# 18-20
    sprite('mi400_05', 3)	# 21-23
    sprite('mi400_07', 3)	# 24-26
    sprite('mi400_08', 3)	# 27-29
    sprite('mi400_09', 3)	# 30-32
    label(0)
    sprite('mi020_07', 3)	# 33-35
    sprite('mi020_08', 3)	# 36-38
    gotoLabel(0)
    label(1)
    sprite('mi230_00', 5)	# 39-43
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown18009(1)
    sprite('mi230_01', 10)	# 44-53
    sprite('mi230_00', 5)	# 54-58

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(2400)
        Hitstop(16)
        AirPushbackX(15000)
        AirPushbackY(32000)
        GroundedHitstunAnimation(1)
        Unknown9016(1)
        AirUntechableTime(80)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('mi400_00', 2)	# 1-2
    Unknown1084(1)
    sprite('mi400_01', 2)	# 3-4
    SFX_3('highjump_l')
    sprite('mi400_02', 5)	# 5-9
    physicsXImpulse(15000)
    physicsYImpulse(32000)
    setGravity(1700)
    GFX_0('mief_400', 0)
    GFX_0('mief_400_2', 0)
    SFX_3('slash_pole_middle')
    sprite('mi400_03', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(90)
    Unknown7007('706d693230305f30000000000000000064000000706d693230305f31000000000000000064000000706d693230305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('mi400_03', 3)	# 11-13	 **attackbox here**
    StartMultihit()
    setInvincible(0)
    Unknown1019(80)
    YAccel(80)
    SFX_3('slash_rapier_middle')
    sprite('mi400_03', 2)	# 14-15	 **attackbox here**
    StartMultihit()
    Unknown1019(80)
    YAccel(80)
    sprite('mi400_04', 3)	# 16-18
    sprite('mi400_05', 3)	# 19-21
    sprite('mi400_07', 3)	# 22-24
    sprite('mi400_08', 3)	# 25-27
    sprite('mi400_09', 3)	# 28-30
    label(0)
    sprite('mi020_07', 3)	# 31-33
    sprite('mi020_08', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('mi230_00', 5)	# 37-41
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown18009(1)
    sprite('mi230_01', 10)	# 42-51
    sprite('mi230_00', 5)	# 52-56

@State
def coup_droitA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1700)
        AttackP1(80)
        AttackP2(85)
        PushbackX(30400)
        AirPushbackX(38000)
        AirPushbackY(10000)
        AirHitstunAnimation(18)
        Unknown9154(25)
        AirUntechableTime(27)
        Unknown9202(15)
        Unknown9016(1)

        def upon_12():
            PushbackX(39520)
    sprite('mi401_00', 2)	# 1-2
    sprite('mi401_01', 2)	# 3-4
    sprite('mi401_02', 2)	# 5-6
    Unknown7007('706d693230315f30000000000000000064000000706d693230315f31000000000000000064000000706d693230325f31000000000000000064000000706d693330345f31000000000000000064000000')
    sprite('mi401_04', 1)	# 7-7
    Unknown3029(1)
    sprite('mi401_04', 1)	# 8-8
    sprite('mi401_05', 2)	# 9-10	 **attackbox here**
    GFX_1('mief_401smoke_04', 0)
    GFX_0('mief_401', 1)
    RefreshMultihit()
    physicsXImpulse(50000)
    Unknown2015(220)
    SFX_3('airdash_m')
    Unknown1028(2500)
    sprite('mi401_06', 4)	# 11-14	 **attackbox here**
    SFX_3('slash_blade_fast')
    sprite('mi401_07', 3)	# 15-17
    Recovery()
    Unknown3029(0)
    SFX_3('slash_rapier_fast')
    Unknown1028(0)
    sprite('mi401_08', 3)	# 18-20
    Unknown1019(60)
    Unknown2015(-1)
    sprite('mi401_09', 3)	# 21-23
    GFX_1('mief_401stopsmoke_03', 0)
    Unknown1019(60)
    sprite('mi401_10', 2)	# 24-25
    sprite('mi401_10', 1)	# 26-26
    Unknown1019(0)
    sprite('mi401_11', 3)	# 27-29
    sprite('mi401_12', 3)	# 30-32

@State
def coup_droitB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(90)
        PushbackX(45000)
        AirPushbackX(60000)
        AirPushbackY(10000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        Unknown11028(20)
        AirUntechableTime(30)
        Unknown9202(18)
        Unknown9016(1)
    sprite('mi401_00', 4)	# 1-4
    sprite('mi401_01', 4)	# 5-8
    sprite('mi401_02', 4)	# 9-12
    sprite('mi401_03', 4)	# 13-16
    sprite('mi401_01', 1)	# 17-17
    Unknown7007('706d693230315f30000000000000000064000000706d693230315f31000000000000000064000000706d693230325f31000000000000000064000000706d693330345f31000000000000000064000000')
    sprite('mi401_04', 3)	# 18-20
    Unknown3029(1)
    sprite('mi401_05', 2)	# 21-22	 **attackbox here**
    GFX_1('mief_401smoke_04', 0)
    GFX_0('mief_401', 1)
    Unknown23029(1, 4011, 0)
    RefreshMultihit()
    physicsXImpulse(65000)
    Unknown2015(220)
    SFX_3('airdash_m')
    Unknown1028(2500)
    sprite('mi401_06', 2)	# 23-24	 **attackbox here**
    SFX_3('slash_blade_fast')
    sprite('mi401_05', 2)	# 25-26	 **attackbox here**
    SFX_3('slash_rapier_fast')
    sprite('mi401_06', 2)	# 27-28	 **attackbox here**
    sprite('mi401_05', 2)	# 29-30	 **attackbox here**
    sprite('mi401_06', 2)	# 31-32	 **attackbox here**
    sprite('mi401_07', 2)	# 33-34
    Recovery()
    Unknown1019(30)
    Unknown3029(0)
    Unknown1028(0)
    sprite('mi401_08', 2)	# 35-36
    Unknown1019(60)
    Unknown2015(-1)
    sprite('mi401_09', 2)	# 37-38
    GFX_1('mief_401stopsmoke_03', 0)
    Unknown1019(60)
    sprite('mi401_10', 2)	# 39-40
    sprite('mi401_11', 2)	# 41-42
    Unknown1019(0)
    sprite('mi401_12', 2)	# 43-44

@State
def coup_droitEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(90)
        PushbackX(45000)
        AirPushbackX(60000)
        AirPushbackY(10000)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        Unknown9154(27)
        AirUntechableTime(29)
        Unknown9202(17)
        Unknown9016(1)
        Unknown11091(10)
        Unknown30065(0)
    sprite('mi401_00', 2)	# 1-2
    sprite('mi401_01', 1)	# 3-3
    sprite('mi401_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('mi401_04', 1)	# 5-5
    sprite('mi401_04', 1)	# 6-6
    Unknown7007('706d693230315f30000000000000000064000000706d693230315f31000000000000000064000000706d693230325f31000000000000000064000000706d693330345f31000000000000000064000000')
    sprite('mi401_05', 2)	# 7-8	 **attackbox here**
    GFX_1('mief_401smoke_04', 0)
    GFX_0('mief_401', 1)
    Unknown23029(1, 4012, 0)
    RefreshMultihit()
    physicsXImpulse(75000)
    Unknown2015(220)
    Unknown1028(3000)
    SFX_3('airdash_m')
    sprite('mi401_06', 2)	# 9-10	 **attackbox here**
    SFX_3('slash_blade_fast')
    sprite('mi401_05', 2)	# 11-12	 **attackbox here**
    SFX_3('slash_rapier_fast')
    sprite('mi401_07', 3)	# 13-15
    Recovery()
    Unknown1019(60)
    Unknown1028(0)
    sprite('mi401_08', 3)	# 16-18
    Unknown1019(80)
    Unknown2015(-1)
    sprite('mi401_09', 2)	# 19-20
    Unknown1019(80)
    GFX_1('mief_401stopsmoke_03', 0)
    sprite('mi401_10', 3)	# 21-23
    sprite('mi401_11', 3)	# 24-26
    Unknown1019(0)
    sprite('mi401_12', 3)	# 27-29

@State
def MarinKarin():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
    sprite('mi205_00', 3)	# 1-3
    sprite('mi205_01', 3)	# 4-6
    sprite('mi205_02', 3)	# 7-9
    sprite('mi205_03', 3)	# 10-12
    Unknown23029(11, 2320, 0)
    Unknown21015('4d6172696e4b6172696e5f73686f7400000000000000000000000000000000001109000000000000')
    SFX_3('cloth_h')
    sprite('mi205_04', 4)	# 13-16
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706d693230335f30000000000000000064000000706d693230335f31000000000000000064000000706d693230335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('mi205_05', 4)	# 17-20
    sprite('mi205_06', 4)	# 21-24
    sprite('mi205_02', 3)	# 25-27
    sprite('mi205_01', 3)	# 28-30
    sprite('mi205_00', 3)	# 31-33

@State
def Tentarafoo():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 4031):
                Unknown13045(0)
                sendToLabel(1)
    sprite('mi403_00', 3)	# 1-3
    sprite('mi403_01', 4)	# 4-7
    tag_voice(1, 'pmi208_0', 'pmi208_1', 'pmi208_2', '')
    sprite('mi403_01', 1)	# 8-8
    Unknown23029(11, 4030, 0)
    sprite('mi403_02', 3)	# 9-11
    sprite('mi403_03', 3)	# 12-14
    sprite('mi403_04', 3)	# 15-17
    sprite('mi403_05', 5)	# 18-22
    sprite('mi403_06', 5)	# 23-27
    sprite('mi403_07', 5)	# 28-32
    sprite('mi403_05', 5)	# 33-37
    sprite('mi403_06', 5)	# 38-42
    sprite('mi403_02', 4)	# 43-46
    sprite('mi403_01', 4)	# 47-50
    sprite('mi403_00', 4)	# 51-54
    ExitState()
    label(1)
    sprite('mi403_05', 3)	# 55-57
    clearUponHandler(43)
    setInvincible(1)
    Unknown14083(0)

    def upon_43():
        if (SLOT_48 == 4033):
            clearUponHandler(43)
            setInvincible(0)
            Unknown14083(1)
            Unknown13045(1)
    sprite('mi403_06', 3)	# 58-60
    sprite('mi403_07', 3)	# 61-63
    sprite('mi403_05', 3)	# 64-66
    sprite('mi403_06', 3)	# 67-69
    sprite('mi403_07', 3)	# 70-72
    sprite('mi403_05', 3)	# 73-75
    sprite('mi403_06', 3)	# 76-78
    sprite('mi403_07', 3)	# 79-81
    sprite('mi403_05', 3)	# 82-84
    sprite('mi403_06', 3)	# 85-87
    sprite('mi403_07', 3)	# 88-90
    sprite('mi403_05', 3)	# 91-93
    tag_voice(0, 'pmi209_0', 'pmi209_1', 'pmi209_2', '')
    sprite('mi403_06', 3)	# 94-96
    sprite('mi403_07', 3)	# 97-99
    sprite('mi403_05', 3)	# 100-102
    sprite('mi403_06', 3)	# 103-105
    sprite('mi403_07', 3)	# 106-108
    sprite('mi403_05', 3)	# 109-111
    sprite('mi403_06', 3)	# 112-114
    sprite('mi403_07', 3)	# 115-117
    sprite('mi403_02', 5)	# 118-122
    sprite('mi403_01', 5)	# 123-127
    sprite('mi403_00', 5)	# 128-132

@State
def Bufula():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('mi402_00', 3)	# 1-3
    sprite('mi402_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    sprite('mi402_02', 3)	# 7-9
    sprite('mi402_03', 3)	# 10-12
    Unknown23029(11, 4020, 0)
    Unknown21015('4963654d696c6c65725f53686f74000000000000000000000000000000000000b50f000000000000')
    SFX_3('slash_knife_slow')
    sprite('mi402_04', 5)	# 13-17
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706d693230345f31000000000000000064000000706d693230365f30000000000000000064000000706d693230365f32000000000000000064000000706d693230375f30000000000000000064000000')
    sprite('mi402_05', 5)	# 18-22
    SFX_3('cloth_h')
    sprite('mi402_06', 5)	# 23-27
    sprite('mi402_07', 5)	# 28-32
    sprite('mi402_05', 5)	# 33-37
    sprite('mi402_06', 5)	# 38-42
    sprite('mi402_07', 5)	# 43-47

@State
def Setsuna_Samidare_Uchi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(3)
        Damage(500)
        AttackP2(98)
        Unknown11091(19)
        Hitstop(0)
        PushbackX(2000)
        Unknown9016(1)
        Unknown11057(400)
        Unknown11064(1)
        setInvincible(1)
        Unknown30055('e09304001e0000000a000000')

        def upon_78():
            Unknown9154(50)
            AirUntechableTime(120)
            AirHitstunAnimation(4)
            if (not SLOT_2):
                Unknown13024(0)
                Unknown2037(1)
            setInvincible(0)
            Unknown22008(45)

        def upon_82():
            clearUponHandler(82)
            Unknown9154(20)
            AirUntechableTime(10)
            AirHitstunAnimation(10)
            Unknown30048(1)
    sprite('mi430_00', 3)	# 1-3
    sprite('mi430_01', 15)	# 4-18
    Unknown2036(58, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pmi250_0', 'pmi250_1', '', '')
    sprite('mi430_02', 6)	# 19-24
    sprite('mi430_03', 6)	# 25-30
    sprite('mi430_04', 6)	# 31-36
    sprite('mi430_05', 6)	# 37-42
    sprite('mi430_06', 10)	# 43-52
    sprite('mi430_06', 9)	# 53-61
    tag_voice(0, 'pmi251_0', 'pmi251_1', '', '')
    sprite('mi430_06', 1)	# 62-62
    sprite('mi430_07', 2)	# 63-64
    label(0)
    sprite('mi430_08', 2)	# 65-66	 **attackbox here**
    GFX_0('RenzokuSlash', 100)
    GFX_0('RenzokuTsukiA', 0)
    RefreshMultihit()
    SLOT_51 = (SLOT_51 + 1)
    SFX_3('slash_rapier_fast')
    sprite('mi430_09', 2)	# 67-68	 **attackbox here**
    GFX_0('RenzokuTsukiB', 0)
    if (not SLOT_2):
        setInvincible(0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_10', 2)	# 69-70	 **attackbox here**
    GFX_0('RenzokuTsukiC', 0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_11', 2)	# 71-72	 **attackbox here**
    GFX_0('RenzokuTsukiD', 0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_12', 2)	# 73-74	 **attackbox here**
    GFX_0('RenzokuTsukiE', 0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_13', 2)	# 75-76	 **attackbox here**
    RefreshMultihit()
    (SLOT_51 == 2)
    if SLOT_0:
        _gotolabel(1)
    SFX_3('slash_rapier_fast')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi430_14', 2)	# 77-78
    sprite('mi430_15', 2)	# 79-80	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    GroundedHitstunAnimation(2)
    Unknown9130(17)
    Unknown9142(999)
    Unknown30055('20a107006400000000000000')
    PushbackX(-24000)
    sprite('mi430_16', 2)	# 81-82
    clearUponHandler(78)
    clearUponHandler(82)
    if SLOT_2:
        setInvincible(1)
    sprite('mi430_17', 2)	# 83-84
    sprite('mi430_18', 5)	# 85-89
    ScreenShake(5000, 5000)
    Unknown8000(100, 1, 1)
    sprite('mi430_18', 1)	# 90-90
    AttackLevel_(5)
    Damage(3000)
    AttackP2(80)
    Hitstop(25)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(3000)
    PushbackX(10000)
    Unknown9178(1)
    Unknown9346(0)
    WallbounceReboundTime(5)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown11057(1200)
    sprite('mi430_18', 1)	# 91-91
    sprite('mi430_18', 4)	# 92-95
    Unknown23183('6d693433305f3138000000000000000000000000000000000000000000000000240000000200000002000000')
    tag_voice(0, 'pmi252_0', 'pmi252_1', '', '')
    if SLOT_2:
        Unknown2036(32, -1, 0)
    sprite('mi430_18', 4)	# 96-99
    sprite('mi430_19', 3)	# 100-102
    sprite('mi430_20', 3)	# 103-105
    physicsXImpulse(30000)
    sprite('mi430_21', 5)	# 106-110	 **attackbox here**
    physicsXImpulse(0)
    Unknown11064(0)
    RefreshMultihit()
    Unknown9015(1)
    Unknown9016(0)
    ScreenShake(20000, 10000)
    Unknown8007(100, 1, 1)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('grip_hugs')
        ScreenShake(40000, 20000)
        Unknown13024(1)
    SFX_3('slash_blade_fast')
    sprite('mi430_21', 10)	# 111-120	 **attackbox here**
    StartMultihit()
    sprite('mi430_22', 6)	# 121-126
    sprite('mi430_23', 6)	# 127-132
    sprite('mi430_24', 6)	# 133-138
    sprite('mi430_25', 6)	# 139-144
    sprite('mi430_26', 6)	# 145-150
    sprite('mi430_27', 6)	# 151-156

@State
def Setsuna_Samidare_UchiSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(3)
        Damage(300)
        AttackP2(99)
        Unknown11091(18)
        Hitstop(0)
        PushbackX(2000)
        Unknown9016(1)
        Unknown11057(400)
        Unknown11064(1)
        setInvincible(1)
        Unknown30055('e09304000a0000000a000000')

        def upon_78():
            Unknown9154(50)
            AirUntechableTime(120)
            AirHitstunAnimation(4)
            if (not SLOT_2):
                Unknown13024(0)
                Unknown2037(1)
            setInvincible(0)
            Unknown22008(45)

        def upon_82():
            clearUponHandler(82)
            Unknown9154(20)
            AirUntechableTime(10)
            AirHitstunAnimation(10)
            Unknown30048(1)
    sprite('mi430_00', 3)	# 1-3
    sprite('mi430_01', 15)	# 4-18
    Unknown2036(58, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pmi250_0', 'pmi250_1', '', '')
    sprite('mi430_02', 6)	# 19-24
    sprite('mi430_03', 6)	# 25-30
    sprite('mi430_04', 6)	# 31-36
    sprite('mi430_05', 6)	# 37-42
    sprite('mi430_06', 19)	# 43-61
    sprite('mi430_06', 1)	# 62-62
    sprite('mi430_07', 2)	# 63-64
    tag_voice(0, 'pmi251_0', 'pmi251_1', '', '')
    label(0)
    sprite('mi430_08', 2)	# 65-66	 **attackbox here**
    GFX_0('RenzokuSlash', 100)
    GFX_0('RenzokuTsukiA', 0)
    RefreshMultihit()
    SLOT_51 = (SLOT_51 + 1)
    SFX_3('slash_rapier_fast')
    sprite('mi430_09', 2)	# 67-68	 **attackbox here**
    GFX_0('RenzokuTsukiB', 0)
    if (not SLOT_2):
        setInvincible(0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_10', 2)	# 69-70	 **attackbox here**
    GFX_0('RenzokuTsukiC', 0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_11', 2)	# 71-72	 **attackbox here**
    GFX_0('RenzokuTsukiD', 0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_12', 2)	# 73-74	 **attackbox here**
    GFX_0('RenzokuTsukiE', 0)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    sprite('mi430_13', 2)	# 75-76	 **attackbox here**
    RefreshMultihit()
    (SLOT_51 == 4)
    if SLOT_0:
        _gotolabel(1)
    SFX_3('slash_rapier_fast')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi430_14', 2)	# 77-78
    sprite('mi430_15', 2)	# 79-80	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    GroundedHitstunAnimation(2)
    Unknown9130(17)
    Unknown9142(999)
    Unknown30055('20a107006400000000000000')
    PushbackX(-24000)
    sprite('mi430_16', 2)	# 81-82
    clearUponHandler(78)
    clearUponHandler(82)
    if SLOT_2:
        setInvincible(1)
    sprite('mi430_17', 2)	# 83-84
    sprite('mi430_18', 5)	# 85-89
    ScreenShake(5000, 5000)
    Unknown8000(100, 1, 1)
    sprite('mi430_18', 1)	# 90-90
    AttackLevel_(5)
    Damage(4000)
    AttackP2(80)
    Hitstop(25)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(100000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(3000)
    PushbackX(10000)
    Unknown9178(1)
    Unknown9346(0)
    WallbounceReboundTime(5)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown11057(1200)
    sprite('mi430_18', 1)	# 91-91
    sprite('mi430_18', 4)	# 92-95
    Unknown23183('6d693433305f3138000000000000000000000000000000000000000000000000240000000200000002000000')
    tag_voice(0, 'pmi252_0', 'pmi252_1', '', '')
    if SLOT_2:
        Unknown2036(32, -1, 0)
    sprite('mi430_18', 4)	# 96-99
    sprite('mi430_19', 3)	# 100-102
    sprite('mi430_20', 3)	# 103-105
    physicsXImpulse(30000)
    sprite('mi430_21', 5)	# 106-110	 **attackbox here**
    physicsXImpulse(0)
    Unknown11064(0)
    RefreshMultihit()
    Unknown9015(1)
    Unknown9016(0)
    ScreenShake(20000, 10000)
    Unknown8007(100, 1, 1)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('grip_hugs')
        ScreenShake(40000, 20000)
        Unknown13024(1)
    SFX_3('slash_blade_fast')
    sprite('mi430_21', 10)	# 111-120	 **attackbox here**
    StartMultihit()
    sprite('mi430_22', 6)	# 121-126
    sprite('mi430_23', 6)	# 127-132
    sprite('mi430_24', 6)	# 133-138
    sprite('mi430_25', 6)	# 139-144
    sprite('mi430_26', 6)	# 145-150
    sprite('mi430_27', 6)	# 151-156

@State
def Bufudyne():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
    sprite('mi431_00', 4)	# 1-4
    sprite('mi431_01', 4)	# 5-8
    sprite('mi431_02', 6)	# 9-14
    Unknown2036(54, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pmi253_0', 'pmi253_1', '', '')
    sprite('mi431_03', 6)	# 15-20
    sprite('mi431_04', 6)	# 21-26
    sprite('mi431_02', 6)	# 27-32
    sprite('mi431_03', 6)	# 33-38
    sprite('mi431_04', 6)	# 39-44
    Unknown23029(11, 4310, 0)
    sprite('mi431_02', 6)	# 45-50
    GFX_1('persona_enter_ply', 0)
    sprite('mi431_03', 6)	# 51-56
    sprite('mi431_04', 6)	# 57-62
    sprite('mi431_05', 4)	# 63-66
    SFX_3('cloth_m')
    tag_voice(0, 'pmi254_0', 'pmi254_1', '', '')
    sprite('mi431_06', 4)	# 67-70
    sprite('mi431_07', 6)	# 71-76
    sprite('mi431_08', 6)	# 77-82
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 83-88
    setInvincible(0)
    sprite('mi431_10', 6)	# 89-94
    sprite('mi431_08', 6)	# 95-100
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 101-106
    sprite('mi431_10', 6)	# 107-112
    sprite('mi431_08', 6)	# 113-118
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 119-124
    sprite('mi431_10', 6)	# 125-130
    sprite('mi431_08', 6)	# 131-136
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 137-142
    sprite('mi431_10', 6)	# 143-148
    sprite('mi431_02', 6)	# 149-154
    sprite('mi431_01', 6)	# 155-160
    sprite('mi431_00', 4)	# 161-164

@State
def BufudyneSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
    sprite('mi431_00', 4)	# 1-4
    sprite('mi431_01', 4)	# 5-8
    sprite('mi431_02', 6)	# 9-14
    Unknown2036(84, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pmi253_0', 'pmi253_1', '', '')
    Unknown2021(1)
    sprite('mi431_03', 6)	# 15-20
    sprite('mi431_04', 6)	# 21-26
    sprite('mi431_02', 6)	# 27-32
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('mi431_03', 6)	# 33-38
    ScreenShake(6000, 6000)
    sprite('mi431_04', 6)	# 39-44
    ScreenShake(6000, 6000)
    sprite('mi431_02', 6)	# 45-50
    ScreenShake(8000, 8000)
    SFX_3('quake_s')
    sprite('mi431_03', 6)	# 51-56
    ScreenShake(8000, 8000)
    sprite('mi431_04', 6)	# 57-62
    ScreenShake(8000, 8000)
    sprite('mi431_02', 6)	# 63-68
    ScreenShake(12000, 12000)
    SFX_3('quake_s')
    sprite('mi431_03', 6)	# 69-74
    ScreenShake(12000, 12000)
    Unknown23029(11, 4311, 0)
    sprite('mi431_02', 6)	# 75-80
    ScreenShake(12000, 12000)
    GFX_1('persona_enter_ply', 0)
    sprite('mi431_03', 6)	# 81-86
    ScreenShake(16000, 16000)
    SFX_3('quake_s')
    sprite('mi431_04', 6)	# 87-92
    ScreenShake(16000, 16000)
    sprite('mi431_05', 4)	# 93-96
    ScreenShake(16000, 16000)
    SFX_3('cloth_m')
    tag_voice(0, 'pmi254_0', 'pmi254_1', '', '')
    sprite('mi431_06', 4)	# 97-100
    sprite('mi431_07', 6)	# 101-106
    sprite('mi431_08', 6)	# 107-112
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 113-118
    setInvincible(0)
    sprite('mi431_10', 6)	# 119-124
    sprite('mi431_08', 6)	# 125-130
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 131-136
    sprite('mi431_10', 6)	# 137-142
    sprite('mi431_08', 6)	# 143-148
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 149-154
    sprite('mi431_10', 6)	# 155-160
    sprite('mi431_08', 6)	# 161-166
    SFX_3('cloth_m')
    sprite('mi431_09', 6)	# 167-172
    sprite('mi431_10', 6)	# 173-178
    sprite('mi431_02', 6)	# 179-184
    Unknown2021(0)
    sprite('mi431_01', 6)	# 185-190
    sprite('mi431_00', 4)	# 191-194

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(100000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(800)
        AirPushbackY(33000)
        YImpluseBeforeWallbounce(600)
        Unknown11023(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown23083(1)
                Unknown23084(1)
                setInvincible(1)
                Unknown23088(1, 1)
                Unknown23157(1)
                GFX_0('IchigekiCamera', 100)
                Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000009313000000000000')
                sendToLabel(1)
            if (SLOT_48 == 5003):
                Unknown23029(11, 4501, 0)
                Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000009513000000000000')
                Unknown36(22)
                Unknown1000(-635000)
                teleportRelativeY(192000)
                physicsXImpulse(4550)
                physicsYImpulse(18400)
                setGravity(0)
                Unknown35()
            if (SLOT_48 == 5004):
                Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000009713000000000000')
                Unknown21015('4963686967656b695f52616e6275534500000000000000000000000000000000a013000000000000')
                Unknown1000(-260000)
                sendToLabel(2)
            if (SLOT_48 == 5002):
                sendToLabel(9)
    sprite('mi450_00', 5)	# 1-5
    setInvincible(1)
    sprite('mi450_01', 5)	# 6-10
    Unknown2036(73, -1, 2)
    GFX_0('P4U_Cutin_Parent', 100)
    Unknown23147()
    sprite('mi450_02', 8)	# 11-18
    sprite('mi450_03', 6)	# 19-24
    sprite('mi450_04', 6)	# 25-30
    sprite('mi450_05', 5)	# 31-35
    tag_voice(1, 'pmi290_0', 'pmi290_1', '', '')
    sprite('mi450_06', 5)	# 36-40
    Unknown23029(11, 4500, 0)
    sprite('mi450_07', 5)	# 41-45
    sprite('mi450_08', 5)	# 46-50
    sprite('mi450_09', 5)	# 51-55
    sprite('mi450_10', 30)	# 56-85
    SFX_3('mi050')
    sprite('mi450_11', 2)	# 86-87
    SFX_3('mi051')
    Unknown4048(-45000)
    Unknown4054(11)
    Unknown4045('706572736f6e615f656e7465725f70330000000000000000000000000000000000000000')
    sprite('mi450_11', 4)	# 88-91
    SFX_0('persona_destroy')
    sprite('mi450_12', 6)	# 92-97
    GFX_0('Ichigeki_Whip', -1)
    label(0)
    sprite('mi450_13', 6)	# 98-103
    sprite('mi450_14', 6)	# 104-109
    sprite('mi450_15', 6)	# 110-115
    gotoLabel(0)
    label(1)
    sprite('mi450_13', 2)	# 116-117
    tag_voice(0, 'pmi291_0', 'pmi291_1', '', '')
    sprite('mi450_14', 2)	# 118-119
    sprite('mi450_15', 2)	# 120-121
    sprite('mi450_13', 2)	# 122-123
    sprite('mi450_14', 2)	# 124-125
    sprite('mi450_15', 2)	# 126-127
    sprite('keep', 70)	# 128-197
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(4000000)
    physicsXImpulse(0)
    physicsYImpulse(40000)
    setGravity(0)
    Unknown35()
    Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000009413000000000000')
    sprite('keep', 32767)	# 198-32964
    Unknown36(22)
    physicsYImpulse(37700)
    physicsXImpulse(9800)
    setGravity(0)
    Unknown35()
    label(2)
    GFX_1('mief_450bg', 100)
    GFX_0('450cutinbg', 100)
    Unknown23024(3)
    sprite('mi450_16', 26)	# 32965-32990
    GFX_0('450icebreak', 100)
    sprite('keep', 20)	# 32991-33010
    GFX_0('IchigekiPicture', 100)
    sprite('keep', 90)	# 33011-33100
    tag_voice(0, 'pmi293_0', 'pmi293_1', '', '')
    sprite('keep', 5)	# 33101-33105
    sprite('mi450_17', 6)	# 33106-33111
    tag_voice(0, 'pmi292_0', 'pmi292_1', '', '')
    sprite('mi450_18', 6)	# 33112-33117
    sprite('mi450_16', 6)	# 33118-33123
    sprite('mi450_17', 6)	# 33124-33129
    sprite('mi450_18', 6)	# 33130-33135
    sprite('mi450_19', 4)	# 33136-33139
    sprite('mi450_20', 4)	# 33140-33143	 **attackbox here**
    ScreenShake(22000, 22000)
    Unknown21015('343530696365627265616b000000000000000000000000000000000000000000a713000000000000')
    GFX_1('mief_450issen', 0)
    GFX_0('Issen', 100)
    sprite('mi450_21', 6)	# 33144-33149	 **attackbox here**
    SFX_3('damage_ichigeki_hit')
    SFX_0('persona_destroy')
    SFX_3('quake_l')
    SFX_3('mi052')
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33150-33155	 **attackbox here**
    GFX_0('450KObg', 100)
    SFX_3('slash_knife_slow')
    sprite('mi450_20', 6)	# 33156-33161	 **attackbox here**
    RefreshMultihit()
    Unknown11064(3)
    sprite('mi450_21', 6)	# 33162-33167	 **attackbox here**
    SFX_3('mi052')
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33168-33173	 **attackbox here**
    sprite('mi450_20', 6)	# 33174-33179	 **attackbox here**
    sprite('mi450_21', 6)	# 33180-33185	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33186-33191	 **attackbox here**
    sprite('mi450_20', 6)	# 33192-33197	 **attackbox here**
    sprite('mi450_21', 6)	# 33198-33203	 **attackbox here**
    SFX_3('mi052')
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33204-33209	 **attackbox here**
    sprite('mi450_20', 6)	# 33210-33215	 **attackbox here**
    sprite('mi450_21', 6)	# 33216-33221	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33222-33227	 **attackbox here**
    sprite('mi450_20', 6)	# 33228-33233	 **attackbox here**
    sprite('mi450_21', 6)	# 33234-33239	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33240-33245	 **attackbox here**
    sprite('mi450_20', 6)	# 33246-33251	 **attackbox here**
    sprite('mi450_21', 6)	# 33252-33257	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33258-33263	 **attackbox here**
    sprite('mi450_20', 6)	# 33264-33269	 **attackbox here**
    sprite('mi450_21', 6)	# 33270-33275	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33276-33281	 **attackbox here**
    sprite('mi450_20', 6)	# 33282-33287	 **attackbox here**
    sprite('mi450_21', 6)	# 33288-33293	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33294-33299	 **attackbox here**
    sprite('mi450_20', 6)	# 33300-33305	 **attackbox here**
    sprite('mi450_21', 6)	# 33306-33311	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33312-33317	 **attackbox here**
    sprite('mi450_20', 6)	# 33318-33323	 **attackbox here**
    sprite('mi450_21', 6)	# 33324-33329	 **attackbox here**
    SFX_3('cloth_m')
    sprite('mi450_22', 6)	# 33330-33335	 **attackbox here**
    sprite('mi450_23', 8)	# 33336-33343
    sprite('mi450_24', 8)	# 33344-33351
    sprite('mi450_25', 8)	# 33352-33359
    sprite('mi450_26', 8)	# 33360-33367
    sprite('mi450_27', 8)	# 33368-33375
    SFX_3('cloth_l')
    Unknown18010()
    Unknown20000(1)
    sprite('mi450_28', 8)	# 33376-33383
    sprite('mi450_29', 8)	# 33384-33391
    sprite('mi450_27', 8)	# 33392-33399
    SFX_3('cloth_l')
    sprite('mi450_28', 8)	# 33400-33407
    sprite('mi450_29', 8)	# 33408-33415
    Unknown18008()
    sprite('mi450_27', 8)	# 33416-33423
    SFX_3('cloth_l')
    sprite('mi450_28', 8)	# 33424-33431
    sprite('mi450_29', 8)	# 33432-33439
    sprite('mi450_27', 8)	# 33440-33447
    SFX_3('cloth_l')
    sprite('mi450_28', 8)	# 33448-33455
    sprite('mi450_29', 8)	# 33456-33463
    sprite('mi450_27', 8)	# 33464-33471
    SFX_3('cloth_l')
    sprite('mi450_28', 8)	# 33472-33479
    sprite('mi450_29', 8)	# 33480-33487
    sprite('mi450_27', 8)	# 33488-33495
    SFX_3('cloth_l')
    sprite('mi450_28', 8)	# 33496-33503
    sprite('mi450_29', 8)	# 33504-33511
    Unknown23018(1)
    label(3)
    sprite('mi450_27', 8)	# 33512-33519
    SFX_3('cloth_l')
    sprite('mi450_28', 8)	# 33520-33527
    sprite('mi450_29', 8)	# 33528-33535
    gotoLabel(3)
    label(9)
    sprite('mi450_10', 14)	# 33536-33549
    setInvincible(0)
    sprite('mi450_07', 8)	# 33550-33557
    sprite('mi450_04', 8)	# 33558-33565
    SFX_4('pmi294')
    sprite('mi600_18', 8)	# 33566-33573
    sprite('mi600_19', 8)	# 33574-33581
    sprite('mi600_20', 8)	# 33582-33589
    SFX_3('slash_knife_fast')
    sprite('mi600_21', 8)	# 33590-33597
    sprite('mi600_22', 6)	# 33598-33603

@Subroutine
def MouthTableInit():
    Unknown18011('pmi000', 12643, 14177, 12643, 24882, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi500', 12643, 14177, 14179, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi502', 12643, 14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi506', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi507', 12643, 14177, 14179, 14177, 14179, 13921, 13923, 13921, 13923, 14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi520', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24886, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi521', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 12849, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 24887, 25399, 24887, 25399, 14131, 12641, 25392, 13621, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi402', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi402_1', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi403', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi403_1', 12643, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi600pak', 12643, 24880, 25399, 12344, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi600pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601bjn', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601bma', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601bny', 12643, 14177, 14435, 24880, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601brc', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13620, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601pag', 12643, 12641, 25392, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601pak', 12643, 12641, 25392, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601rbl', 12643, 13921, 13923, 13921, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601rwi', 12643, 12641, 25392, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi601uor', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi700bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi700brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi700pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi700rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi701bma', 12643, 12641, 25392, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi701bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi701pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi701pna', 12643, 24880, 25399, 13622, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi701rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24884, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pmi701uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('pna')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bjn')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bny')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('brc')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pag')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uor')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('bma')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('mi600_00', 2)	# 2-3
    sprite('mi600_01', 6)	# 4-9
    Unknown7006('pmi500', 100, 896101744, 13360, 0, 0, 100, 896101744, 13616, 0, 0, 100, 896101744, 13872, 0, 0, 100)
    sprite('mi600_02', 6)	# 10-15
    sprite('mi600_03', 6)	# 16-21
    SFX_3('hair')
    sprite('mi600_04', 18)	# 22-39
    sprite('mi600_05', 6)	# 40-45
    sprite('mi600_06', 6)	# 46-51
    sprite('mi600_07', 6)	# 52-57
    sprite('mi600_09', 6)	# 58-63
    sprite('mi600_10', 6)	# 64-69
    SFX_3('cloth_h')
    sprite('mi600_12', 8)	# 70-77
    sprite('mi600_13', 8)	# 78-85
    sprite('mi600_14', 6)	# 86-91
    sprite('mi600_15', 18)	# 92-109
    SFX_3('hair')
    SFX_3('cloth_l')
    sprite('mi600_16', 6)	# 110-115
    sprite('mi600_17', 6)	# 116-121
    sprite('mi600_18', 10)	# 122-131
    sprite('mi600_19', 6)	# 132-137
    sprite('mi600_20', 6)	# 138-143
    SFX_3('slash_knife_fast')
    sprite('mi600_21', 6)	# 144-149
    sprite('mi600_22', 6)	# 150-155
    sprite('mi000_00', 6)	# 156-161
    Unknown23018(1)
    label(1)
    sprite('mi000_00', 8)	# 162-169
    sprite('mi000_01', 8)	# 170-177
    sprite('mi000_02', 8)	# 178-185
    sprite('mi000_03', 8)	# 186-193
    sprite('mi000_04', 8)	# 194-201
    sprite('mi000_05', 8)	# 202-209
    sprite('mi000_06', 8)	# 210-217
    sprite('mi000_07', 8)	# 218-225
    sprite('mi000_08', 8)	# 226-233
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('mi601_00', 75)	# 234-308
    teleportRelativeY(1)
    Unknown3001(0)
    GFX_0('rimzineHontaiA', 100)
    Unknown36(24)
    Unknown2019(-1000)
    Unknown35()
    sprite('mi601_00', 75)	# 309-383
    sprite('mi601_00', 26)	# 384-409
    Unknown3001(255)
    Unknown2019(999)
    sprite('mi601_01', 6)	# 410-415
    sprite('mi601_02', 12)	# 416-427
    sprite('mi601_03', 6)	# 428-433
    sprite('mi601_04', 6)	# 434-439
    sprite('mi601_05', 6)	# 440-445
    sprite('mi601_06', 6)	# 446-451
    teleportRelativeY(0)
    sprite('mi601_07', 6)	# 452-457
    sprite('mi601_08', 6)	# 458-463
    Unknown8000(100, 0, 1)
    Unknown2019(0)
    sprite('mi601_09', 6)	# 464-469
    sprite('mi601_10', 16)	# 470-485
    Unknown7006('pmi501', 100, 896101744, 12848, 0, 0, 100, 896101744, 13104, 0, 0, 100, 896101744, 14128, 0, 0, 100)
    sprite('mi601_11', 6)	# 486-491
    sprite('mi601_12', 6)	# 492-497
    SFX_3('cloth_h')
    sprite('mi601_13', 6)	# 498-503
    sprite('mi601_14', 11)	# 504-514
    SFX_3('hair')
    sprite('mi601_15', 6)	# 515-520
    sprite('mi601_16', 6)	# 521-526
    sprite('mi601_17', 6)	# 527-532
    sprite('mi601_18', 6)	# 533-538
    sprite('mi600_18', 10)	# 539-548
    sprite('mi600_19', 6)	# 549-554
    sprite('mi600_20', 6)	# 555-560
    SFX_3('slash_knife_fast')
    sprite('mi600_21', 6)	# 561-566
    sprite('mi600_22', 5)	# 567-571
    sprite('mi600_22', 1)	# 572-572
    Unknown26('rimzineHontaiA')
    Unknown26('rimzinetaiya2')
    Unknown26('rimzineDoor2')
    Unknown23018(1)
    label(11)
    sprite('mi000_00', 8)	# 573-580
    sprite('mi000_01', 8)	# 581-588
    sprite('mi000_02', 8)	# 589-596
    sprite('mi000_03', 8)	# 597-604
    sprite('mi000_04', 8)	# 605-612
    sprite('mi000_05', 8)	# 613-620
    sprite('mi000_06', 8)	# 621-628
    sprite('mi000_07', 8)	# 629-636
    sprite('mi000_08', 8)	# 637-644
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('mi000_00', 8)	# 645-652
    sprite('mi602_10', 6)	# 653-658
    SFX_1('pmi601brc')
    sprite('mi602_11', 6)	# 659-664
    sprite('mi602_12', 6)	# 665-670
    sprite('mi602_13', 6)	# 671-676
    sprite('mi602_14', 6)	# 677-682
    sprite('mi602_12', 6)	# 683-688
    sprite('mi602_13', 6)	# 689-694
    sprite('mi602_14', 6)	# 695-700
    sprite('mi602_12', 6)	# 701-706
    sprite('mi602_13', 6)	# 707-712
    sprite('mi602_14', 6)	# 713-718
    sprite('mi602_12', 6)	# 719-724
    sprite('mi602_13', 6)	# 725-730
    sprite('mi602_14', 6)	# 731-736
    label(21)
    sprite('mi602_12', 6)	# 737-742
    sprite('mi602_13', 6)	# 743-748
    sprite('mi602_14', 6)	# 749-754
    gotoLabel(21)
    sprite('mi602_15', 6)	# 755-760
    ExitState()
    label(991)
    sprite('mi000_00', 1)	# 761-761
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('mi000_00', 8)	# 762-769
    sprite('mi000_01', 8)	# 770-777
    sprite('mi000_02', 8)	# 778-785
    sprite('mi000_03', 8)	# 786-793
    sprite('mi000_04', 8)	# 794-801
    sprite('mi000_05', 8)	# 802-809
    sprite('mi000_06', 8)	# 810-817
    sprite('mi000_07', 8)	# 818-825
    sprite('mi000_08', 8)	# 826-833
    gotoLabel(992)
    ExitState()
    label(100)
    sprite('mi600_00', 2)	# 834-835
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('mi600_01', 6)	# 836-841
    SFX_1('pmi600pna')
    sprite('mi600_02', 6)	# 842-847
    sprite('mi600_03', 6)	# 848-853
    SFX_3('hair')
    sprite('mi600_04', 18)	# 854-871
    sprite('mi600_05', 6)	# 872-877
    sprite('mi600_06', 6)	# 878-883
    sprite('mi600_07', 6)	# 884-889
    sprite('mi600_09', 6)	# 890-895
    sprite('mi600_10', 6)	# 896-901
    SFX_3('cloth_h')
    sprite('mi600_12', 8)	# 902-909
    sprite('mi600_13', 8)	# 910-917
    sprite('mi600_14', 6)	# 918-923
    sprite('mi600_15', 18)	# 924-941
    SFX_3('hair')
    SFX_3('cloth_l')
    sprite('mi600_16', 6)	# 942-947
    sprite('mi600_17', 6)	# 948-953
    sprite('mi600_18', 10)	# 954-963
    sprite('mi600_19', 6)	# 964-969
    sprite('mi600_20', 6)	# 970-975
    SFX_3('slash_knife_fast')
    sprite('mi600_21', 6)	# 976-981
    sprite('mi600_22', 6)	# 982-987
    sprite('mi000_00', 6)	# 988-993
    Unknown2037(1)
    Unknown21011(380)
    label(101)
    sprite('mi000_00', 8)	# 994-1001
    sprite('mi000_01', 8)	# 1002-1009
    sprite('mi000_02', 8)	# 1010-1017
    sprite('mi000_03', 8)	# 1018-1025
    sprite('mi000_04', 8)	# 1026-1033
    if (not SLOT_2):
        Unknown21007(24, 40)
    sprite('mi000_05', 8)	# 1034-1041
    sprite('mi000_06', 8)	# 1042-1049
    sprite('mi000_07', 8)	# 1050-1057
    sprite('mi000_08', 8)	# 1058-1065
    Unknown2038(-1)
    gotoLabel(101)
    ExitState()
    label(110)
    sprite('mi000_00', 1)	# 1066-1066
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('mi000_00', 8)	# 1067-1074
    sprite('mi000_01', 8)	# 1075-1082
    sprite('mi000_02', 8)	# 1083-1090
    sprite('mi000_03', 8)	# 1091-1098
    sprite('mi000_04', 8)	# 1099-1106
    sprite('mi000_05', 8)	# 1107-1114
    sprite('mi000_06', 8)	# 1115-1122
    sprite('mi000_07', 8)	# 1123-1130
    sprite('mi000_08', 8)	# 1131-1138
    gotoLabel(111)
    label(112)
    sprite('mi001_00', 8)	# 1139-1146
    SFX_1('pmi601bjn')
    sprite('mi001_01', 8)	# 1147-1154
    sprite('mi001_02', 8)	# 1155-1162
    sprite('mi001_03', 6)	# 1163-1168
    sprite('mi001_04', 6)	# 1169-1174
    sprite('mi001_05', 6)	# 1175-1180
    sprite('mi001_06', 6)	# 1181-1186
    sprite('mi001_07', 6)	# 1187-1192
    sprite('mi001_08', 6)	# 1193-1198
    sprite('mi001_09', 6)	# 1199-1204
    SFX_3('hair')
    sprite('mi001_10', 6)	# 1205-1210
    Unknown23018(1)
    label(113)
    sprite('mi000_00', 8)	# 1211-1218
    sprite('mi000_01', 8)	# 1219-1226
    sprite('mi000_02', 8)	# 1227-1234
    sprite('mi000_03', 8)	# 1235-1242
    sprite('mi000_04', 8)	# 1243-1250
    sprite('mi000_05', 8)	# 1251-1258
    sprite('mi000_06', 8)	# 1259-1266
    sprite('mi000_07', 8)	# 1267-1274
    sprite('mi000_08', 8)	# 1275-1282
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('mi000_00', 1)	# 1283-1283
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('mi000_00', 8)	# 1284-1291
    sprite('mi000_01', 8)	# 1292-1299
    sprite('mi000_02', 8)	# 1300-1307
    sprite('mi000_03', 8)	# 1308-1315
    sprite('mi000_04', 8)	# 1316-1323
    sprite('mi000_05', 8)	# 1324-1331
    sprite('mi000_06', 8)	# 1332-1339
    sprite('mi000_07', 8)	# 1340-1347
    sprite('mi000_08', 8)	# 1348-1355
    gotoLabel(121)
    label(122)
    sprite('mi001_00', 8)	# 1356-1363
    SFX_1('pmi601bny')
    sprite('mi001_01', 8)	# 1364-1371
    sprite('mi001_02', 8)	# 1372-1379
    sprite('mi001_03', 6)	# 1380-1385
    sprite('mi001_04', 6)	# 1386-1391
    sprite('mi001_05', 6)	# 1392-1397
    sprite('mi001_06', 6)	# 1398-1403
    sprite('mi001_07', 6)	# 1404-1409
    sprite('mi001_08', 6)	# 1410-1415
    sprite('mi001_09', 6)	# 1416-1421
    SFX_3('hair')
    sprite('mi001_10', 6)	# 1422-1427
    Unknown23018(1)
    label(123)
    sprite('mi000_00', 8)	# 1428-1435
    sprite('mi000_01', 8)	# 1436-1443
    sprite('mi000_02', 8)	# 1444-1451
    sprite('mi000_03', 8)	# 1452-1459
    sprite('mi000_04', 8)	# 1460-1467
    sprite('mi000_05', 8)	# 1468-1475
    sprite('mi000_06', 8)	# 1476-1483
    sprite('mi000_07', 8)	# 1484-1491
    sprite('mi000_08', 8)	# 1492-1499
    gotoLabel(123)
    ExitState()
    label(130)
    sprite('mi000_00', 1)	# 1500-1500
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('mi000_00', 8)	# 1501-1508
    sprite('mi000_01', 8)	# 1509-1516
    sprite('mi000_02', 8)	# 1517-1524
    sprite('mi000_03', 8)	# 1525-1532
    sprite('mi000_04', 8)	# 1533-1540
    sprite('mi000_05', 8)	# 1541-1548
    sprite('mi000_06', 8)	# 1549-1556
    sprite('mi000_07', 8)	# 1557-1564
    sprite('mi000_08', 8)	# 1565-1572
    gotoLabel(131)
    label(132)
    sprite('mi001_00', 8)	# 1573-1580
    SFX_1('pmi601brc')
    sprite('mi001_01', 8)	# 1581-1588
    sprite('mi001_02', 8)	# 1589-1596
    sprite('mi001_03', 6)	# 1597-1602
    sprite('mi001_04', 6)	# 1603-1608
    sprite('mi001_05', 6)	# 1609-1614
    sprite('mi001_06', 6)	# 1615-1620
    sprite('mi001_07', 6)	# 1621-1626
    sprite('mi001_08', 6)	# 1627-1632
    sprite('mi001_09', 6)	# 1633-1638
    SFX_3('hair')
    sprite('mi001_10', 6)	# 1639-1644
    Unknown23018(1)
    label(133)
    sprite('mi000_00', 8)	# 1645-1652
    sprite('mi000_01', 8)	# 1653-1660
    sprite('mi000_02', 8)	# 1661-1668
    sprite('mi000_03', 8)	# 1669-1676
    sprite('mi000_04', 8)	# 1677-1684
    sprite('mi000_05', 8)	# 1685-1692
    sprite('mi000_06', 8)	# 1693-1700
    sprite('mi000_07', 8)	# 1701-1708
    sprite('mi000_08', 8)	# 1709-1716
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('mi000_00', 1)	# 1717-1717
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('mi000_00', 8)	# 1718-1725
    sprite('mi000_01', 8)	# 1726-1733
    sprite('mi000_02', 8)	# 1734-1741
    sprite('mi000_03', 8)	# 1742-1749
    sprite('mi000_04', 8)	# 1750-1757
    sprite('mi000_05', 8)	# 1758-1765
    sprite('mi000_06', 8)	# 1766-1773
    sprite('mi000_07', 8)	# 1774-1781
    sprite('mi000_08', 8)	# 1782-1789
    gotoLabel(141)
    label(142)
    sprite('mi001_00', 8)	# 1790-1797
    SFX_1('pmi601pag')
    sprite('mi001_01', 8)	# 1798-1805
    sprite('mi001_02', 8)	# 1806-1813
    sprite('mi001_03', 6)	# 1814-1819
    sprite('mi001_04', 6)	# 1820-1825
    sprite('mi001_05', 6)	# 1826-1831
    sprite('mi001_06', 6)	# 1832-1837
    sprite('mi001_07', 6)	# 1838-1843
    sprite('mi001_08', 6)	# 1844-1849
    sprite('mi001_09', 6)	# 1850-1855
    SFX_3('hair')
    sprite('mi001_10', 6)	# 1856-1861
    Unknown23018(1)
    label(143)
    sprite('mi000_00', 8)	# 1862-1869
    sprite('mi000_01', 8)	# 1870-1877
    sprite('mi000_02', 8)	# 1878-1885
    sprite('mi000_03', 8)	# 1886-1893
    sprite('mi000_04', 8)	# 1894-1901
    sprite('mi000_05', 8)	# 1902-1909
    sprite('mi000_06', 8)	# 1910-1917
    sprite('mi000_07', 8)	# 1918-1925
    sprite('mi000_08', 8)	# 1926-1933
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('mi000_00', 1)	# 1934-1934
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('mi000_00', 8)	# 1935-1942
    sprite('mi000_01', 8)	# 1943-1950
    sprite('mi000_02', 8)	# 1951-1958
    sprite('mi000_03', 8)	# 1959-1966
    sprite('mi000_04', 8)	# 1967-1974
    sprite('mi000_05', 8)	# 1975-1982
    sprite('mi000_06', 8)	# 1983-1990
    sprite('mi000_07', 8)	# 1991-1998
    sprite('mi000_08', 8)	# 1999-2006
    gotoLabel(151)
    label(152)
    sprite('mi001_00', 8)	# 2007-2014
    SFX_1('pmi601rbl')
    sprite('mi001_01', 8)	# 2015-2022
    sprite('mi001_02', 8)	# 2023-2030
    sprite('mi001_03', 6)	# 2031-2036
    sprite('mi001_04', 6)	# 2037-2042
    sprite('mi001_05', 6)	# 2043-2048
    sprite('mi001_06', 6)	# 2049-2054
    sprite('mi001_07', 6)	# 2055-2060
    sprite('mi001_08', 6)	# 2061-2066
    sprite('mi001_09', 6)	# 2067-2072
    SFX_3('hair')
    sprite('mi001_10', 6)	# 2073-2078
    Unknown23018(1)
    label(153)
    sprite('mi000_00', 8)	# 2079-2086
    sprite('mi000_01', 8)	# 2087-2094
    sprite('mi000_02', 8)	# 2095-2102
    sprite('mi000_03', 8)	# 2103-2110
    sprite('mi000_04', 8)	# 2111-2118
    sprite('mi000_05', 8)	# 2119-2126
    sprite('mi000_06', 8)	# 2127-2134
    sprite('mi000_07', 8)	# 2135-2142
    sprite('mi000_08', 8)	# 2143-2150
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('mi000_00', 1)	# 2151-2151
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('mi000_00', 8)	# 2152-2159
    sprite('mi000_01', 8)	# 2160-2167
    sprite('mi000_02', 8)	# 2168-2175
    sprite('mi000_03', 8)	# 2176-2183
    sprite('mi000_04', 8)	# 2184-2191
    sprite('mi000_05', 8)	# 2192-2199
    sprite('mi000_06', 8)	# 2200-2207
    sprite('mi000_07', 8)	# 2208-2215
    sprite('mi000_08', 8)	# 2216-2223
    gotoLabel(161)
    label(162)
    sprite('mi001_00', 8)	# 2224-2231
    SFX_1('pmi601rwi')
    sprite('mi001_01', 8)	# 2232-2239
    sprite('mi001_02', 8)	# 2240-2247
    sprite('mi001_03', 6)	# 2248-2253
    sprite('mi001_04', 6)	# 2254-2259
    sprite('mi001_05', 6)	# 2260-2265
    sprite('mi001_06', 6)	# 2266-2271
    sprite('mi001_07', 6)	# 2272-2277
    sprite('mi001_08', 6)	# 2278-2283
    sprite('mi001_09', 6)	# 2284-2289
    SFX_3('hair')
    sprite('mi001_10', 6)	# 2290-2295
    Unknown23018(1)
    label(163)
    sprite('mi000_00', 8)	# 2296-2303
    sprite('mi000_01', 8)	# 2304-2311
    sprite('mi000_02', 8)	# 2312-2319
    sprite('mi000_03', 8)	# 2320-2327
    sprite('mi000_04', 8)	# 2328-2335
    sprite('mi000_05', 8)	# 2336-2343
    sprite('mi000_06', 8)	# 2344-2351
    sprite('mi000_07', 8)	# 2352-2359
    sprite('mi000_08', 8)	# 2360-2367
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('mi000_00', 1)	# 2368-2368
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('mi000_00', 8)	# 2369-2376
    sprite('mi000_01', 8)	# 2377-2384
    sprite('mi000_02', 8)	# 2385-2392
    sprite('mi000_03', 8)	# 2393-2400
    sprite('mi000_04', 8)	# 2401-2408
    sprite('mi000_05', 8)	# 2409-2416
    sprite('mi000_06', 8)	# 2417-2424
    sprite('mi000_07', 8)	# 2425-2432
    sprite('mi000_08', 8)	# 2433-2440
    gotoLabel(171)
    label(172)
    sprite('mi602_10', 6)	# 2441-2446
    SFX_1('pmi601uor')
    sprite('mi602_11', 6)	# 2447-2452
    sprite('mi602_12', 6)	# 2453-2458
    sprite('mi602_13', 6)	# 2459-2464
    sprite('mi602_14', 6)	# 2465-2470
    sprite('mi602_12', 6)	# 2471-2476
    sprite('mi602_13', 6)	# 2477-2482
    sprite('mi602_14', 6)	# 2483-2488
    label(173)
    sprite('mi602_12', 6)	# 2489-2494
    sprite('mi602_13', 6)	# 2495-2500
    sprite('mi602_14', 6)	# 2501-2506
    if SLOT_97:
        _gotolabel(173)
    sprite('mi602_12', 6)	# 2507-2512
    sprite('mi602_13', 6)	# 2513-2518
    sprite('mi602_14', 6)	# 2519-2524
    sprite('mi602_15', 6)	# 2525-2530
    Unknown23018(1)
    label(174)
    sprite('mi000_00', 8)	# 2531-2538
    sprite('mi000_01', 8)	# 2539-2546
    sprite('mi000_02', 8)	# 2547-2554
    sprite('mi000_03', 8)	# 2555-2562
    sprite('mi000_04', 8)	# 2563-2570
    sprite('mi000_05', 8)	# 2571-2578
    sprite('mi000_06', 8)	# 2579-2586
    sprite('mi000_07', 8)	# 2587-2594
    sprite('mi000_08', 8)	# 2595-2602
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('mi000_00', 1)	# 2603-2603
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('mi000_00', 8)	# 2604-2611
    sprite('mi000_01', 8)	# 2612-2619
    sprite('mi000_02', 8)	# 2620-2627
    sprite('mi000_03', 8)	# 2628-2635
    sprite('mi000_04', 8)	# 2636-2643
    sprite('mi000_05', 8)	# 2644-2651
    sprite('mi000_06', 8)	# 2652-2659
    sprite('mi000_07', 8)	# 2660-2667
    sprite('mi000_08', 8)	# 2668-2675
    gotoLabel(181)
    label(182)
    sprite('mi001_00', 8)	# 2676-2683
    SFX_1('pmi601bma')
    sprite('mi001_01', 8)	# 2684-2691
    sprite('mi001_02', 8)	# 2692-2699
    sprite('mi001_03', 6)	# 2700-2705
    sprite('mi001_04', 6)	# 2706-2711
    sprite('mi001_05', 6)	# 2712-2717
    sprite('mi001_06', 6)	# 2718-2723
    sprite('mi001_07', 6)	# 2724-2729
    sprite('mi001_08', 6)	# 2730-2735
    sprite('mi001_09', 6)	# 2736-2741
    SFX_3('hair')
    sprite('mi001_10', 6)	# 2742-2747
    Unknown23018(1)
    label(183)
    sprite('mi000_00', 8)	# 2748-2755
    sprite('mi000_01', 8)	# 2756-2763
    sprite('mi000_02', 8)	# 2764-2771
    sprite('mi000_03', 8)	# 2772-2779
    sprite('mi000_04', 8)	# 2780-2787
    sprite('mi000_05', 8)	# 2788-2795
    sprite('mi000_06', 8)	# 2796-2803
    sprite('mi000_07', 8)	# 2804-2811
    sprite('mi000_08', 8)	# 2812-2819
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('mi000_00', 1)	# 2820-2820
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('mi000_00', 8)	# 2821-2828
    sprite('mi000_01', 8)	# 2829-2836
    sprite('mi000_02', 8)	# 2837-2844
    sprite('mi000_03', 8)	# 2845-2852
    sprite('mi000_04', 8)	# 2853-2860
    sprite('mi000_05', 8)	# 2861-2868
    sprite('mi000_06', 8)	# 2869-2876
    sprite('mi000_07', 8)	# 2877-2884
    sprite('mi000_08', 8)	# 2885-2892
    gotoLabel(191)
    label(192)
    sprite('mi001_00', 8)	# 2893-2900
    SFX_1('pmi601pak')
    sprite('mi001_01', 8)	# 2901-2908
    sprite('mi001_02', 8)	# 2909-2916
    sprite('mi001_03', 6)	# 2917-2922
    sprite('mi001_04', 6)	# 2923-2928
    sprite('mi001_05', 6)	# 2929-2934
    sprite('mi001_06', 6)	# 2935-2940
    sprite('mi001_07', 6)	# 2941-2946
    sprite('mi001_08', 6)	# 2947-2952
    sprite('mi001_09', 6)	# 2953-2958
    SFX_3('hair')
    sprite('mi001_10', 6)	# 2959-2964
    Unknown23018(1)
    label(193)
    sprite('mi000_00', 8)	# 2965-2972
    sprite('mi000_01', 8)	# 2973-2980
    sprite('mi000_02', 8)	# 2981-2988
    sprite('mi000_03', 8)	# 2989-2996
    sprite('mi000_04', 8)	# 2997-3004
    sprite('mi000_05', 8)	# 3005-3012
    sprite('mi000_06', 8)	# 3013-3020
    sprite('mi000_07', 8)	# 3021-3028
    sprite('mi000_08', 8)	# 3029-3036
    gotoLabel(193)
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
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('pak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    sprite('keep', 1)	# 4-4
    if SLOT_158:
        if (not SLOT_52):
            if (not SLOT_108):
                if (SLOT_19 <= 900000):
                    if (SLOT_19 >= 300000):
                        if random_(2, 0, 50):
                            sendToLabel(0)
                        else:
                            sendToLabel(10)
            else:
                sendToLabel(0)
        else:
            sendToLabel(0)
    label(0)
    sprite('mi000_00', 6)	# 5-10
    sprite('mi600_22', 6)	# 11-16
    sprite('mi600_21', 6)	# 17-22
    sprite('mi600_20', 6)	# 23-28
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 29-34
    sprite('mi600_18', 18)	# 35-52
    Unknown23029(11, 6100, 0)
    sprite('mi610_01', 6)	# 53-58
    sprite('mi610_02', 6)	# 59-64
    sprite('mi610_03', 6)	# 65-70
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pmi524', 100, 896101744, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pmi402', 100, 879324528, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pmi520', 100, 896101744, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(1)
    sprite('mi610_04', 8)	# 71-78
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 79-86
    sprite('mi610_06', 8)	# 87-94
    gotoLabel(1)
    label(10)
    sprite('mi000_00', 8)	# 95-102
    Unknown2006()
    Unknown20000(1)

    def upon_3():
        if (SLOT_19 <= 300000):
            clearUponHandler(3)
            sendToLabel(12)
    sprite('mi030_00', 5)	# 103-107
    physicsXImpulse(7500)
    sprite('mi030_01', 5)	# 108-112
    label(11)
    sprite('mi030_02', 5)	# 113-117
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mi030_03', 5)	# 118-122
    sprite('mi030_04', 5)	# 123-127
    sprite('mi030_05', 5)	# 128-132
    sprite('mi030_06', 5)	# 133-137
    sprite('mi030_07', 5)	# 138-142
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mi030_08', 5)	# 143-147
    sprite('mi030_09', 5)	# 148-152
    sprite('mi030_10', 5)	# 153-157
    sprite('mi030_11', 5)	# 158-162
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('mi000_00', 8)	# 163-170
    physicsXImpulse(0)
    sprite('mi600_22', 6)	# 171-176
    sprite('mi600_21', 6)	# 177-182
    sprite('mi600_20', 6)	# 183-188
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 189-194
    sprite('mi600_18', 12)	# 195-206
    sprite('mi611_00', 6)	# 207-212
    sprite('mi611_01', 6)	# 213-218
    sprite('mi611_02', 6)	# 219-224
    SFX_3('cloth_m')
    sprite('mi611_03', 6)	# 225-230
    sprite('mi611_04', 6)	# 231-236
    sprite('mi611_05', 6)	# 237-242
    sprite('mi611_06', 6)	# 243-248
    sprite('mi611_07', 6)	# 249-254
    SFX_3('cloth_h')
    sprite('mi611_08', 6)	# 255-260
    sprite('mi611_09', 6)	# 261-266
    Unknown8000(100, 0, 1)
    sprite('mi611_10', 6)	# 267-272
    sprite('mi611_11', 6)	# 273-278
    sprite('mi611_12', 6)	# 279-284
    sprite('mi611_13', 6)	# 285-290
    sprite('mi611_14', 6)	# 291-296
    SFX_3('cloth_m')
    sprite('mi611_15', 6)	# 297-302
    sprite('mi611_16', 6)	# 303-308
    sprite('mi611_17', 6)	# 309-314
    sprite('mi611_18', 6)	# 315-320
    SFX_3('hair')
    sprite('mi611_19', 6)	# 321-326
    sprite('mi611_20', 8)	# 327-334
    Unknown7006('pmi521', 100, 896101744, 12850, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_3('cloth_l')
    sprite('mi611_21', 8)	# 335-342
    sprite('mi611_22', 8)	# 343-350
    Unknown23018(1)
    label(13)
    sprite('mi611_20', 8)	# 351-358
    SFX_3('cloth_l')
    sprite('mi611_21', 8)	# 359-366
    sprite('mi611_22', 8)	# 367-374
    gotoLabel(13)
    label(100)
    sprite('mi000_00', 6)	# 375-380
    sprite('mi600_22', 6)	# 381-386
    sprite('mi600_21', 6)	# 387-392
    sprite('mi600_20', 6)	# 393-398
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 399-404
    sprite('mi600_18', 18)	# 405-422
    Unknown23029(11, 6100, 0)
    sprite('mi610_01', 6)	# 423-428
    sprite('mi610_02', 6)	# 429-434
    sprite('mi610_03', 6)	# 435-440
    SFX_1('pmi700bjn')
    label(101)
    sprite('mi610_04', 8)	# 441-448
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 449-456
    sprite('mi610_06', 8)	# 457-464
    if SLOT_97:
        _gotolabel(101)
    sprite('mi610_04', 8)	# 465-472
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 473-480
    sprite('mi610_06', 8)	# 481-488
    Unknown21007(24, 40)
    Unknown21011(420)
    label(102)
    sprite('mi610_04', 8)	# 489-496
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 497-504
    sprite('mi610_06', 8)	# 505-512
    gotoLabel(102)
    label(110)
    sprite('mi402_00', 2)	# 513-514
    SFX_1('pmi700brc')
    sprite('mi402_01', 2)	# 515-516
    sprite('mi402_02', 2)	# 517-518
    sprite('mi402_03', 3)	# 519-521
    SFX_3('slash_knife_slow')
    sprite('mi402_04', 6)	# 522-527
    label(111)
    sprite('mi402_05', 6)	# 528-533
    sprite('mi402_06', 6)	# 534-539
    sprite('mi402_07', 6)	# 540-545
    loopRest()
    if SLOT_97:
        _gotolabel(111)
    sprite('mi402_05', 1)	# 546-546
    Unknown21007(24, 40)
    Unknown21011(240)
    label(112)
    sprite('mi402_05', 6)	# 547-552
    sprite('mi402_06', 6)	# 553-558
    sprite('mi402_07', 6)	# 559-564
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('mi402_00', 2)	# 565-566
    SFX_1('pmi700rwi')
    sprite('mi402_01', 2)	# 567-568
    sprite('mi402_02', 2)	# 569-570
    sprite('mi402_03', 3)	# 571-573
    SFX_3('slash_knife_slow')
    sprite('mi402_04', 6)	# 574-579
    label(121)
    sprite('mi402_05', 6)	# 580-585
    sprite('mi402_06', 6)	# 586-591
    sprite('mi402_07', 6)	# 592-597
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('mi402_05', 1)	# 598-598
    Unknown21007(24, 40)
    Unknown21011(220)
    label(122)
    sprite('mi402_05', 6)	# 599-604
    sprite('mi402_06', 6)	# 605-610
    sprite('mi402_07', 6)	# 611-616
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('mi000_00', 1)	# 617-617

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('mi000_00', 8)	# 618-625
    sprite('mi000_01', 8)	# 626-633
    sprite('mi000_02', 8)	# 634-641
    sprite('mi000_03', 8)	# 642-649
    sprite('mi000_04', 8)	# 650-657
    sprite('mi000_05', 8)	# 658-665
    sprite('mi000_06', 8)	# 666-673
    sprite('mi000_07', 8)	# 674-681
    sprite('mi000_08', 8)	# 682-689
    gotoLabel(131)
    label(132)
    sprite('mi600_22', 6)	# 690-695
    sprite('mi600_21', 6)	# 696-701
    sprite('mi600_20', 6)	# 702-707
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 708-713
    sprite('mi600_18', 18)	# 714-731
    Unknown23029(11, 6100, 0)
    sprite('mi610_01', 6)	# 732-737
    sprite('mi610_02', 6)	# 738-743
    sprite('mi610_03', 6)	# 744-749
    SFX_1('pmi701bny')
    Unknown23018(1)
    label(133)
    sprite('mi610_04', 8)	# 750-757
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 758-765
    sprite('mi610_06', 8)	# 766-773
    gotoLabel(133)
    label(140)
    sprite('mi000_00', 1)	# 774-774

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('mi000_00', 8)	# 775-782
    sprite('mi000_01', 8)	# 783-790
    sprite('mi000_02', 8)	# 791-798
    sprite('mi000_03', 8)	# 799-806
    sprite('mi000_04', 8)	# 807-814
    sprite('mi000_05', 8)	# 815-822
    sprite('mi000_06', 8)	# 823-830
    sprite('mi000_07', 8)	# 831-838
    sprite('mi000_08', 8)	# 839-846
    gotoLabel(141)
    label(142)
    sprite('mi600_22', 6)	# 847-852
    sprite('mi600_21', 6)	# 853-858
    sprite('mi600_20', 6)	# 859-864
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 865-870
    sprite('mi600_18', 18)	# 871-888
    sprite('mi610_01', 6)	# 889-894
    sprite('mi610_02', 6)	# 895-900
    sprite('mi610_03', 6)	# 901-906
    SFX_1('pmi701pag')
    Unknown23018(1)
    label(143)
    sprite('mi610_04', 8)	# 907-914
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 915-922
    sprite('mi610_06', 8)	# 923-930
    gotoLabel(143)
    label(150)
    sprite('mi000_00', 1)	# 931-931

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('mi000_00', 8)	# 932-939
    sprite('mi000_01', 8)	# 940-947
    sprite('mi000_02', 8)	# 948-955
    sprite('mi000_03', 8)	# 956-963
    sprite('mi000_04', 8)	# 964-971
    sprite('mi000_05', 8)	# 972-979
    sprite('mi000_06', 8)	# 980-987
    sprite('mi000_07', 8)	# 988-995
    sprite('mi000_08', 8)	# 996-1003
    gotoLabel(151)
    label(152)
    sprite('mi600_22', 6)	# 1004-1009
    sprite('mi600_21', 6)	# 1010-1015
    sprite('mi600_20', 6)	# 1016-1021
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 1022-1027
    sprite('mi600_18', 18)	# 1028-1045
    Unknown23029(11, 6100, 0)
    sprite('mi610_01', 6)	# 1046-1051
    sprite('mi610_02', 6)	# 1052-1057
    sprite('mi610_03', 6)	# 1058-1063
    SFX_1('pmi701pna')
    Unknown23018(1)
    label(153)
    sprite('mi610_04', 8)	# 1064-1071
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 1072-1079
    sprite('mi610_06', 8)	# 1080-1087
    gotoLabel(153)
    label(160)
    sprite('mi000_00', 1)	# 1088-1088

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('mi000_00', 8)	# 1089-1096
    sprite('mi000_01', 8)	# 1097-1104
    sprite('mi000_02', 8)	# 1105-1112
    sprite('mi000_03', 8)	# 1113-1120
    sprite('mi000_04', 8)	# 1121-1128
    sprite('mi000_05', 8)	# 1129-1136
    sprite('mi000_06', 8)	# 1137-1144
    sprite('mi000_07', 8)	# 1145-1152
    sprite('mi000_08', 8)	# 1153-1160
    gotoLabel(161)
    label(162)
    sprite('mi402_00', 2)	# 1161-1162
    SFX_1('pmi701rbl')
    sprite('mi402_01', 2)	# 1163-1164
    sprite('mi402_02', 2)	# 1165-1166
    sprite('mi402_03', 3)	# 1167-1169
    SFX_3('slash_knife_slow')
    sprite('mi402_04', 6)	# 1170-1175
    Unknown23018(1)
    label(163)
    sprite('mi402_05', 6)	# 1176-1181
    sprite('mi402_06', 6)	# 1182-1187
    sprite('mi402_07', 6)	# 1188-1193
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('mi000_00', 1)	# 1194-1194

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('mi000_00', 8)	# 1195-1202
    sprite('mi000_01', 8)	# 1203-1210
    sprite('mi000_02', 8)	# 1211-1218
    sprite('mi000_03', 8)	# 1219-1226
    sprite('mi000_04', 8)	# 1227-1234
    sprite('mi000_05', 8)	# 1235-1242
    sprite('mi000_06', 8)	# 1243-1250
    sprite('mi000_07', 8)	# 1251-1258
    sprite('mi000_08', 8)	# 1259-1266
    gotoLabel(171)
    label(172)
    sprite('mi600_22', 6)	# 1267-1272
    sprite('mi600_21', 6)	# 1273-1278
    sprite('mi600_20', 6)	# 1279-1284
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 1285-1290
    sprite('mi600_18', 18)	# 1291-1308
    Unknown23029(11, 6100, 0)
    sprite('mi610_01', 6)	# 1309-1314
    sprite('mi610_02', 6)	# 1315-1320
    sprite('mi610_03', 6)	# 1321-1326
    SFX_1('pmi701uor')
    Unknown23018(1)
    label(173)
    sprite('mi610_04', 8)	# 1327-1334
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 1335-1342
    sprite('mi610_06', 8)	# 1343-1350
    gotoLabel(173)
    label(180)
    sprite('mi000_00', 1)	# 1351-1351

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('mi000_00', 8)	# 1352-1359
    sprite('mi000_01', 8)	# 1360-1367
    sprite('mi000_02', 8)	# 1368-1375
    sprite('mi000_03', 8)	# 1376-1383
    sprite('mi000_04', 8)	# 1384-1391
    sprite('mi000_05', 8)	# 1392-1399
    sprite('mi000_06', 8)	# 1400-1407
    sprite('mi000_07', 8)	# 1408-1415
    sprite('mi000_08', 8)	# 1416-1423
    gotoLabel(181)
    label(182)
    sprite('mi600_22', 6)	# 1424-1429
    sprite('mi600_21', 6)	# 1430-1435
    sprite('mi600_20', 6)	# 1436-1441
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 1442-1447
    sprite('mi600_18', 18)	# 1448-1465
    Unknown23029(11, 6100, 0)
    sprite('mi610_01', 6)	# 1466-1471
    sprite('mi610_02', 6)	# 1472-1477
    sprite('mi610_03', 6)	# 1478-1483
    SFX_1('pmi701bma')
    Unknown23018(1)
    label(183)
    sprite('mi610_04', 8)	# 1484-1491
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 1492-1499
    sprite('mi610_06', 8)	# 1500-1507
    gotoLabel(183)
    label(190)
    sprite('mi000_00', 6)	# 1508-1513
    sprite('mi600_22', 6)	# 1514-1519
    sprite('mi600_21', 6)	# 1520-1525
    sprite('mi600_20', 6)	# 1526-1531
    SFX_3('slash_knife_slow')
    sprite('mi600_19', 6)	# 1532-1537
    sprite('mi600_18', 18)	# 1538-1555
    Unknown23029(11, 6100, 0)
    sprite('mi610_01', 6)	# 1556-1561
    sprite('mi610_02', 6)	# 1562-1567
    sprite('mi610_03', 6)	# 1568-1573
    SFX_1('pmi700pak')
    label(191)
    sprite('mi610_04', 8)	# 1574-1581
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 1582-1589
    sprite('mi610_06', 8)	# 1590-1597
    if SLOT_97:
        _gotolabel(191)
    sprite('mi610_04', 1)	# 1598-1598
    Unknown21007(24, 40)
    Unknown21011(300)
    label(192)
    sprite('mi610_04', 8)	# 1599-1606
    SFX_3('cloth_l')
    sprite('mi610_05', 8)	# 1607-1614
    sprite('mi610_06', 8)	# 1615-1622
    gotoLabel(192)

@State
def CmnActLose():
    sprite('mi070_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('pmi403', 100, 879324528, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('mi070_01', 6)	# 7-12
    sprite('mi070_02', 2)	# 13-14
    Unknown23018(1)
    sprite('mi070_03', 32767)	# 15-32781
