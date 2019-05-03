@Subroutine
def PreInit():
    Unknown12019('706b6100000000000000000000000000')

@Subroutine
def MatchInit():
    Health(18000)
    DashFInitialVelocity(6000)
    DashFAccel(70)
    DashFMaxVelocity(19000)
    Unknown12038(18000)
    Unknown12034(16)
    AirDashBSpeed(18000)
    AirBDashDuration(13)
    Unknown12037(-1500)
    Unknown12024(3)
    Unknown13039(0)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14015(-324000, 315000, -200000, 80000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(-322000, 322000, -170000, 152000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(29000, 422000, -225000, 316000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(29000, 422000, -225000, 316000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(2)
    Unknown14015(15000, 260000, -155000, 105000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(-322000, 322000, -170000, 152000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(29000, 422000, -225000, 316000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th', 0xf)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(29000, 422000, -225000, 316000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th_Land', 0x6)
    Unknown14005(1)
    Unknown14013('NmlAtk5A4th')
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    Unknown15009()
    Unknown14015(2000, 255000, -213000, -103000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Move_AirGround_(0x3083)
    MoveMaxChainRepeat(1)
    Unknown14015(60000, 660000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Move_AirGround_(0x3083)
    Unknown14005(1)
    Unknown15012(4000)
    Unknown15013(4000)
    Unknown14015(0, 520000, -218000, 32000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(2000)
    Unknown14015(-261000, 358000, -199000, 378000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(29000, 422000, -225000, 316000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(29000, 481000, -205000, -7000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(106000, 240000, 75000, 230000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown14015(106000, 240000, 75000, 230000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(53000, 448000, -329000, 218000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-60000, 340000, -304000, 20000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 370000, -141000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 370000, -141000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('BusterAttackA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(140000, 490000, -190000, 180000, 500, 50)
    Move_EndRegister()
    Move_Register('BusterAttackB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(360000, 610000, -200000, 300000, 500, 50)
    Move_EndRegister()
    Move_Register('BusterAttackEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(200000, 720000, -190000, 180000, 500, 50)
    Move_EndRegister()
    Move_Register('AirBusterAttackA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(140000, 490000, -190000, 180000, 500, 50)
    Move_EndRegister()
    Move_Register('AirBusterAttackB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(360000, 610000, -200000, 300000, 500, 50)
    Move_EndRegister()
    Move_Register('AirBusterAttackEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(200000, 720000, -190000, 180000, 500, 50)
    Move_EndRegister()
    Move_Register('Oiuchi', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('KushizashiA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x300a)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 256000, -202000, 126000, 500, 0)
    Move_EndRegister()
    Move_Register('TsukameB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(2000)
    Unknown14015(65000, 608000, 117000, 704000, 500, 50)
    Move_EndRegister()
    Move_Register('KushizashiEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x300a)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 256000, -202000, 126000, 500, 0)
    Move_EndRegister()
    Move_Register('TaetemiyagareA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(188000, 420000, -700000, 0, 250, 50)
    Move_EndRegister()
    Move_Register('TaetemiyagareB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(668000, 900000, -700000, 0, 250, 50)
    Move_EndRegister()
    Move_Register('TaetemiyagareEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(450000, 780000, -700000, 0, 250, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Move_AirGround_(0x3083)
    Unknown14015(-229000, 158000, -216000, 186000, 250, 0)
    Move_EndRegister()
    Move_Register('KenkaSappou', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(0, 200000, -60000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('KenkaSappou_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(0, 200000, -60000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('Kurokoge', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 206000, -202000, 126000, 500, 0)
    Move_EndRegister()
    Move_Register('Kurokoge_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 206000, -202000, 126000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15005(10)
    Unknown15014(3000)
    Unknown14015(0, 580000, -95000, 124000, 1000, 50)
    Unknown15000(0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtk4A4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A2nd', 10000000)
    Unknown15024('NmlAtkAIR5B', 'AirBusterAttackA', 10000000)
    Unknown12018(0, 'ka060_00')
    Unknown12018(1, 'ka060_01')
    Unknown12018(2, 'ka060_02')
    Unknown12018(3, 'ka060_03')
    Unknown12018(4, 'ka060_04')
    Unknown12018(5, 'ka060_05')
    Unknown12018(6, 'ka060_06')
    Unknown12018(7, 'ka040_02')
    Unknown12018(8, 'ka040_02')
    Unknown12018(9, 'ka045_02')
    Unknown12018(10, 'ka060_00')
    Unknown12018(11, 'ka060_01')
    Unknown12018(12, 'ka060_03')
    Unknown12018(13, 'ka060_05')
    Unknown12018(14, 'ka060_07')
    Unknown12018(15, 'ka125_00')
    Unknown12018(16, 'ka050_00')
    Unknown12018(17, 'ka052_00')
    Unknown12018(18, 'ka054_00')
    Unknown12018(25, 'ka063_00')
    Unknown12018(26, 'ka063_02')
    Unknown12018(27, 'ka063_03')
    Unknown12018(28, 'ka063_05')
    Unknown12018(29, 'ka060_12')
    Unknown12018(24, 'ka072_03')
    Unknown7010(0, 'pka000')
    Unknown7010(1, 'pka001')
    Unknown7010(2, 'pka002')
    Unknown7010(3, 'pka003')
    Unknown7010(4, 'pka004')
    Unknown7010(5, 'pka005')
    Unknown7010(6, 'pka006')
    Unknown7010(7, 'pka007')
    Unknown7010(8, 'pka008')
    Unknown7010(9, 'pka009')
    Unknown7010(10, 'pka010')
    Unknown7010(15, 'pka011')
    Unknown7010(16, 'pka012')
    Unknown7010(17, 'pka013')
    Unknown7010(18, 'pka014')
    Unknown7010(19, 'pka015')
    Unknown7010(20, 'pka016')
    Unknown7010(21, 'pka017')
    Unknown7010(22, 'pka018')
    Unknown7010(23, 'pka019')
    Unknown7010(24, 'pka020')
    Unknown7010(25, 'pka021')
    Unknown7010(28, 'pka022')
    Unknown7010(29, 'pka023')
    Unknown7010(30, 'pka024')
    Unknown7010(31, 'pka025')
    Unknown7010(32, 'pka026')
    Unknown7010(33, 'pka027')
    Unknown7010(34, 'pka028')
    Unknown7010(35, 'pka029')
    Unknown7010(36, 'pka030')
    Unknown7010(37, 'pka031')
    Unknown7010(39, 'pka032')
    Unknown7010(42, 'pka033')
    Unknown7010(43, 'pka034')
    Unknown7010(44, 'pka035')
    Unknown7010(45, 'pka036')
    Unknown7010(46, 'pka037')
    Unknown7010(47, 'pka038')
    Unknown7010(48, 'pka039')
    Unknown7010(49, 'pka040')
    Unknown7010(50, 'pka041')
    Unknown7010(52, 'pka042')
    Unknown7010(53, 'pka043')
    Unknown7010(54, 'pka100_0')
    Unknown7010(55, 'pka100_1')
    Unknown7010(56, 'pka100_2')
    Unknown7010(63, 'pka101_0')
    Unknown7010(64, 'pka101_1')
    Unknown7010(65, 'pka101_2')
    Unknown7010(57, 'pka102_0')
    Unknown7010(58, 'pka102_1')
    Unknown7010(59, 'pka102_2')
    Unknown7010(66, 'pka103_0')
    Unknown7010(67, 'pka103_1')
    Unknown7010(68, 'pka103_2')
    Unknown7010(60, 'pka104_0')
    Unknown7010(61, 'pka104_1')
    Unknown7010(62, 'pka104_2')
    Unknown7010(69, 'pka105_0')
    Unknown7010(70, 'pka105_1')
    Unknown7010(71, 'pka105_2')
    Unknown7010(72, 'pka150')
    Unknown7010(73, 'pka151')
    Unknown7010(74, 'pka152')
    Unknown7010(85, 'pka153')
    Unknown7010(87, 'pka154')
    Unknown7010(88, 'pka155')
    Unknown7010(96, 'pka161_0')
    Unknown7010(97, 'pka161_1')
    Unknown7010(92, 'pka162_0')
    Unknown7010(93, 'pka162_1')
    Unknown7010(98, 'pka163_0')
    Unknown7010(99, 'pka163_1')
    Unknown7010(100, 'pka164_0')
    Unknown7010(101, 'pka164_1')
    Unknown7010(105, 'pka165_0')
    Unknown7010(106, 'pka165_1')
    Unknown7010(102, 'pka166_0')
    Unknown7010(103, 'pka166_1')
    Unknown7010(90, 'pka167_0')
    Unknown7010(91, 'pka167_1')
    Unknown7010(107, 'pka168_0')
    Unknown7010(108, 'pka168_1')
    Unknown7010(110, 'pka169_0')
    Unknown7010(111, 'pka169_1')
    Unknown7010(94, 'pka400_0')
    Unknown7010(95, 'pka400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('020000004b656e6b61536170706f75000000000000000000000000000000000000000000')
    Unknown12059('030000004b656e6b61536170706f755f4f44000000000000000000000000000000000000')
    Unknown12059('040000004b75726f6b6f6765000000000000000000000000000000000000000000000000')
    Unknown12059('050000004b75726f6b6f67655f4f44000000000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    Unknown30036('504b415f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        pass

@Subroutine
def OnDamage():
    if SLOT_64:
        SLOT_64 = 0

@Subroutine
def Eff_ExSkill_AfterImage():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3072('80000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    Unknown3074('000000000400000032000000a0000000')
    Unknown3075('00000000000000000000000010000000')
    Unknown3076(1010)
    Unknown3077(900)

@Subroutine
def Taete_Input():
    Unknown14070('TaetemiyagareA')
    Unknown14070('TaetemiyagareB')
    Unknown14070('TaetemiyagareEX')

@Subroutine
def Taete_Timing():
    Unknown14072('TaetemiyagareA')
    Unknown14072('TaetemiyagareB')
    Unknown14072('TaetemiyagareEX')

@Subroutine
def Taete_Clear():
    Unknown14074('TaetemiyagareA')
    Unknown14074('TaetemiyagareB')
    Unknown14074('TaetemiyagareEX')

@State
def CmnActStand():
    (SLOT_64 == 1)
    if SLOT_0:
        _gotolabel(1)
    (SLOT_64 == 2)
    if SLOT_0:
        _gotolabel(2)
    label(0)
    sprite('ka000_00', 6)	# 1-6
    sprite('ka000_01', 6)	# 7-12
    sprite('ka000_02', 6)	# 13-18
    sprite('ka000_03', 6)	# 19-24
    sprite('ka000_04', 6)	# 25-30
    sprite('ka000_05', 6)	# 31-36
    sprite('ka000_06', 6)	# 37-42
    sprite('ka000_07', 6)	# 43-48
    sprite('ka000_08', 6)	# 49-54
    sprite('ka000_09', 6)	# 55-60
    sprite('ka000_10', 6)	# 61-66
    sprite('ka000_11', 6)	# 67-72
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
    sprite('ka001_00', 7)	# 73-79
    SLOT_88 = 960
    SFX_1('pka000')
    sprite('ka001_01', 7)	# 80-86
    sprite('ka001_02', 7)	# 87-93
    sprite('ka001_03', 7)	# 94-100
    sprite('ka001_04', 7)	# 101-107
    SFX_3('ka000')
    sprite('ka001_05', 7)	# 108-114
    sprite('ka001_06', 7)	# 115-121
    sprite('ka001_07', 7)	# 122-128
    SFX_3('ka000')
    sprite('ka001_08', 7)	# 129-135
    sprite('ka001_09', 7)	# 136-142
    sprite('ka001_10', 7)	# 143-149
    sprite('ka001_00', 7)	# 150-156
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka401_13', 6)	# 157-162
    SLOT_64 = 0
    sprite('ka401_14', 4)	# 163-166
    SFX_3('ka003')
    sprite('ka401_15', 3)	# 167-169
    sprite('ka401_16', 3)	# 170-172
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('ka401_11', 3)	# 173-175
    SLOT_64 = 0
    sprite('ka401_12', 4)	# 176-179
    sprite('ka401_13', 6)	# 180-185
    sprite('ka401_14', 4)	# 186-189
    SFX_3('ka003')
    sprite('ka401_15', 3)	# 190-192
    sprite('ka401_16', 3)	# 193-195
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ka003_00', 4)	# 1-4
    sprite('ka003_01', 4)	# 5-8
    sprite('ka003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('ka010_00', 4)	# 1-4
    sprite('ka010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ka010_02', 6)	# 1-6
    sprite('ka010_03', 6)	# 7-12
    sprite('ka010_04', 6)	# 13-18
    sprite('ka010_05', 6)	# 19-24
    sprite('ka010_06', 6)	# 25-30
    sprite('ka010_07', 6)	# 31-36
    sprite('ka010_08', 6)	# 37-42
    sprite('ka010_09', 6)	# 43-48
    sprite('ka010_10', 6)	# 49-54
    sprite('ka010_11', 6)	# 55-60
    sprite('ka010_12', 6)	# 61-66
    sprite('ka010_13', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ka013_00', 4)	# 1-4
    sprite('ka013_01', 4)	# 5-8
    sprite('ka013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('ka010_01', 4)	# 1-4
    sprite('ka010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ka010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ka020_00', 4)	# 1-4
    sprite('ka020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ka020_02', 3)	# 1-3
    sprite('ka020_03', 3)	# 4-6
    sprite('ka020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ka020_05', 3)	# 1-3
    sprite('ka020_06', 3)	# 4-6
    label(0)
    sprite('ka020_07', 4)	# 7-10
    sprite('ka020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ka010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('ka064_02', 32767)	# 1-32767
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('ka064_03', 6)	# 1-6

@State
def CmnActFWalk():
    sprite('ka030_00', 3)	# 1-3
    sprite('ka030_01', 5)	# 4-8
    label(0)
    sprite('ka030_02', 5)	# 9-13
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ka030_03', 5)	# 14-18
    sprite('ka030_04', 5)	# 19-23
    sprite('ka030_05', 5)	# 24-28
    sprite('ka030_06', 5)	# 29-33
    sprite('ka030_07', 5)	# 34-38
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('ka003')
    sprite('ka030_08', 5)	# 39-43
    sprite('ka030_09', 5)	# 44-48
    sprite('ka030_10', 5)	# 49-53
    sprite('ka030_11', 5)	# 54-58
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('ka031_00', 6)	# 1-6
    sprite('ka031_01', 6)	# 7-12
    label(0)
    sprite('ka031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ka031_03', 6)	# 19-24
    sprite('ka031_04', 6)	# 25-30
    sprite('ka031_05', 6)	# 31-36
    sprite('ka031_06', 6)	# 37-42
    sprite('ka031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('ka003')
    sprite('ka031_08', 6)	# 49-54
    sprite('ka031_09', 6)	# 55-60
    sprite('ka031_10', 6)	# 61-66
    sprite('ka031_11', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('ka032_00', 4)	# 1-4
    sprite('ka032_01', 8)	# 5-12
    sprite('ka032_02', 4)	# 13-16
    sprite('ka032_02', 1)	# 17-17
    Unknown1015(12000)
    label(0)
    sprite('ka032_03', 4)	# 18-21
    sprite('ka032_04', 4)	# 22-25
    Unknown8006(100, 1, 1)
    sprite('ka032_05', 4)	# 26-29
    sprite('ka032_06', 4)	# 30-33
    sprite('ka032_07', 4)	# 34-37
    sprite('ka032_08', 4)	# 38-41
    Unknown8006(100, 1, 1)
    SFX_3('ka003')
    sprite('ka032_09', 4)	# 42-45
    sprite('ka032_10', 4)	# 46-49
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ka032_11', 4)	# 1-4
    sprite('ka032_12', 4)	# 5-8

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
    sprite('ka033_00', 2)	# 1-2
    SFX_3('ka003')
    sprite('ka033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('ka033_02', 1)	# 6-6
    sprite('ka033_02', 2)	# 7-8
    label(0)
    sprite('ka033_01', 3)	# 9-11
    sprite('ka033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka033_03', 3)	# 15-17
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ka033_04', 3)	# 18-20

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('ka035_00', 3)	# 1-3
    label(0)
    sprite('ka035_01', 3)	# 4-6
    sprite('ka035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ka033_01', 3)	# 1-3
    SFX_3('ka003')
    physicsYImpulse(13000)
    sprite('ka033_02', 3)	# 4-6
    sprite('ka033_01', 3)	# 7-9
    sprite('ka033_02', 3)	# 10-12
    sprite('ka033_01', 3)	# 13-15
    sprite('ka033_02', 3)	# 16-18
    sprite('ka033_01', 3)	# 19-21
    sprite('ka033_02', 3)	# 22-24
    sprite('ka020_05', 3)	# 25-27
    sprite('ka020_06', 3)	# 28-30
    label(0)
    sprite('ka020_07', 4)	# 31-34
    sprite('ka020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ka050_00', 1)	# 1-1
    sprite('ka050_01', 1)	# 2-2
    sprite('ka050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ka050_01', 1)	# 1-1
    sprite('ka050_02', 1)	# 2-2
    sprite('ka050_01', 2)	# 3-4
    sprite('ka050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ka050_02', 1)	# 1-1
    sprite('ka050_03', 1)	# 2-2
    sprite('ka050_02', 2)	# 3-4
    sprite('ka050_01', 2)	# 5-6
    sprite('ka050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ka050_03', 1)	# 1-1
    sprite('ka050_04', 1)	# 2-2
    sprite('ka050_03', 2)	# 3-4
    sprite('ka050_02', 2)	# 5-6
    sprite('ka050_01', 2)	# 7-8
    sprite('ka050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ka050_04', 1)	# 1-1
    sprite('ka050_04', 1)	# 2-2
    sprite('ka050_04', 2)	# 3-4
    sprite('ka050_03', 2)	# 5-6
    sprite('ka050_02', 2)	# 7-8
    sprite('ka050_01', 2)	# 9-10
    sprite('ka050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ka052_00', 1)	# 1-1
    sprite('ka052_01', 1)	# 2-2
    sprite('ka052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ka052_01', 1)	# 1-1
    sprite('ka052_02', 1)	# 2-2
    sprite('ka052_01', 2)	# 3-4
    sprite('ka052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ka052_02', 1)	# 1-1
    sprite('ka052_03', 1)	# 2-2
    sprite('ka052_02', 2)	# 3-4
    sprite('ka052_01', 2)	# 5-6
    sprite('ka052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ka052_03', 1)	# 1-1
    sprite('ka052_04', 1)	# 2-2
    sprite('ka052_03', 2)	# 3-4
    sprite('ka052_02', 2)	# 5-6
    sprite('ka052_01', 2)	# 7-8
    sprite('ka052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ka052_04', 1)	# 1-1
    sprite('ka052_04', 1)	# 2-2
    sprite('ka052_04', 2)	# 3-4
    sprite('ka052_03', 2)	# 5-6
    sprite('ka052_02', 2)	# 7-8
    sprite('ka052_01', 2)	# 9-10
    sprite('ka052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ka054_00', 1)	# 1-1
    sprite('ka054_01', 1)	# 2-2
    sprite('ka054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ka054_01', 1)	# 1-1
    sprite('ka054_02', 1)	# 2-2
    sprite('ka054_01', 2)	# 3-4
    sprite('ka054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ka054_02', 1)	# 1-1
    sprite('ka054_03', 1)	# 2-2
    sprite('ka054_02', 2)	# 3-4
    sprite('ka054_01', 2)	# 5-6
    sprite('ka054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ka054_03', 1)	# 1-1
    sprite('ka054_04', 1)	# 2-2
    sprite('ka054_03', 2)	# 3-4
    sprite('ka054_02', 2)	# 5-6
    sprite('ka054_01', 2)	# 7-8
    sprite('ka054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ka054_04', 1)	# 1-1
    sprite('ka054_04', 1)	# 2-2
    sprite('ka054_04', 2)	# 3-4
    sprite('ka054_03', 2)	# 5-6
    sprite('ka054_02', 2)	# 7-8
    sprite('ka054_01', 2)	# 9-10
    sprite('ka054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ka060_00', 4)	# 1-4
    label(0)
    sprite('ka060_01', 4)	# 5-8
    sprite('ka060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ka060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ka060_04', 8)	# 1-8
    label(0)
    sprite('ka060_05', 4)	# 9-12
    sprite('ka060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ka063_05', 6)	# 1-6

@State
def CmnActBDownBound():
    sprite('ka060_08', 2)	# 1-2
    sprite('ka060_09', 2)	# 3-4
    sprite('ka060_10', 2)	# 5-6
    sprite('ka060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('ka060_12', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('ka064_00', 6)	# 1-6
    sprite('ka064_01', 6)	# 7-12
    sprite('ka064_02', 6)	# 13-18
    sprite('ka064_03', 6)	# 19-24

@State
def CmnActFDownUpper():
    sprite('ka063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ka063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ka063_03', 3)	# 1-3
    sprite('ka063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ka063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('ka060_08', 2)	# 1-2
    SFX_3('ka003')
    sprite('ka060_09', 2)	# 3-4
    sprite('ka060_10', 2)	# 5-6
    sprite('ka060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('ka060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ka064_00', 6)	# 1-6
    sprite('ka064_01', 6)	# 7-12
    sprite('ka064_02', 6)	# 13-18
    sprite('ka064_03', 6)	# 19-24
    SFX_3('ka003')

@State
def CmnActVDownUpper():
    sprite('ka060_00', 4)	# 1-4
    label(0)
    sprite('ka060_01', 4)	# 5-8
    sprite('ka060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ka060_03', 4)	# 1-4
    sprite('ka060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('ka060_04', 8)	# 1-8
    label(0)
    sprite('ka060_05', 4)	# 9-12
    sprite('ka060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ka060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('ka072_00', 3)	# 1-3
    label(0)
    sprite('ka072_01', 3)	# 4-6
    sprite('ka072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ka074_00', 2)	# 1-2
    sprite('ka074_01', 2)	# 3-4
    sprite('ka074_02', 2)	# 5-6
    sprite('ka074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('ka082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('ka050_01', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ka072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('ka063_00', 3)	# 1-3
    sprite('ka063_01', 3)	# 4-6
    sprite('ka063_02', 3)	# 7-9
    label(0)
    sprite('ka063_03', 3)	# 10-12
    sprite('ka063_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ka070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('ka070_01', 4)	# 1-4
    sprite('ka070_02', 4)	# 5-8
    sprite('ka070_03', 4)	# 9-12
    sprite('ka070_04', 4)	# 13-16
    sprite('ka070_05', 4)	# 17-20
    sprite('ka070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ka040_03', 2)	# 1-2
    sprite('ka040_02', 2)	# 3-4
    sprite('ka040_01', 2)	# 5-6
    sprite('ka040_00', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ka020_02', 3)	# 1-3
    sprite('ka020_03', 3)	# 4-6
    sprite('ka020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('ka020_02', 3)	# 1-3
    sprite('ka020_03', 3)	# 4-6
    sprite('ka020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirN():
    sprite('ka020_02', 3)	# 1-3
    sprite('ka020_03', 3)	# 4-6
    sprite('ka020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandF():
    sprite('ka112_00', 3)	# 1-3
    sprite('ka112_01', 3)	# 4-6
    sprite('ka112_02', 3)	# 7-9
    sprite('ka112_03', 3)	# 10-12
    sprite('ka112_04', 3)	# 13-15
    sprite('ka112_05', 3)	# 16-18
    sprite('ka020_07', 4)	# 19-22
    sprite('ka020_08', 4)	# 23-26

@State
def CmnActUkemiLandB():
    sprite('ka112_00', 3)	# 1-3
    sprite('ka112_01', 3)	# 4-6
    sprite('ka112_02', 3)	# 7-9
    sprite('ka112_03', 3)	# 10-12
    sprite('ka112_04', 3)	# 13-15
    sprite('ka112_05', 3)	# 16-18
    sprite('ka020_07', 4)	# 19-22
    sprite('ka020_08', 4)	# 23-26

@State
def CmnActUkemiLandN():
    sprite('ka112_00', 3)	# 1-3
    sprite('ka112_01', 3)	# 4-6
    sprite('ka112_02', 3)	# 7-9
    sprite('ka112_03', 3)	# 10-12
    sprite('ka112_04', 3)	# 13-15
    sprite('ka112_05', 3)	# 16-18
    sprite('ka020_07', 4)	# 19-22
    sprite('ka020_08', 4)	# 23-26

@State
def CmnActUkemiLandNLanding():
    sprite('ka010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('ka040_00', 3)	# 1-3
    sprite('ka040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ka040_02', 3)	# 1-3
    sprite('ka040_03', 4)	# 4-7
    sprite('ka040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ka040_01', 3)	# 1-3
    sprite('ka040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ka040_05', 1)	# 1-1
    label(0)
    sprite('ka040_02', 3)	# 2-4
    sprite('ka040_03', 4)	# 5-8
    sprite('ka040_04', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ka040_01', 3)	# 1-3
    sprite('ka040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ka040_00', 3)	# 1-3
    sprite('ka040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('ka040_05', 1)	# 1-1
    label(0)
    sprite('ka040_02', 3)	# 2-4
    sprite('ka040_03', 4)	# 5-8
    sprite('ka040_04', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ka040_01', 3)	# 1-3
    sprite('ka040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ka040_05', 1)	# 1-1
    label(0)
    sprite('ka040_02', 3)	# 2-4
    sprite('ka040_03', 4)	# 5-8
    sprite('ka040_04', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ka040_01', 3)	# 1-3
    sprite('ka040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ka043_00', 3)	# 1-3
    sprite('ka043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ka043_02', 3)	# 1-3
    sprite('ka043_03', 4)	# 4-7
    sprite('ka043_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ka043_01', 3)	# 1-3
    sprite('ka043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ka043_05', 1)	# 1-1
    label(0)
    sprite('ka043_02', 3)	# 2-4
    sprite('ka043_03', 4)	# 5-8
    sprite('ka043_04', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ka043_01', 3)	# 1-3
    sprite('ka043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ka045_00', 3)	# 1-3
    sprite('ka045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ka045_02', 3)	# 1-3
    sprite('ka045_03', 4)	# 4-7
    sprite('ka045_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ka045_01', 3)	# 1-3
    sprite('ka045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ka045_05', 1)	# 1-1
    label(0)
    sprite('ka045_02', 3)	# 2-4
    sprite('ka045_03', 4)	# 5-8
    sprite('ka045_04', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ka045_01', 3)	# 1-3
    sprite('ka045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ka040_04', 2)	# 1-2
    sprite('ka040_04', 2)	# 3-4
    sprite('ka040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ka040_02', 4)	# 6-9
    sprite('ka040_01', 4)	# 10-13
    sprite('ka040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ka043_04', 2)	# 1-2
    sprite('ka043_04', 2)	# 3-4
    sprite('ka043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ka043_02', 4)	# 6-9
    sprite('ka043_01', 4)	# 10-13
    sprite('ka043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ka045_04', 2)	# 1-2
    sprite('ka045_04', 2)	# 3-4
    sprite('ka045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ka045_02', 4)	# 6-9
    sprite('ka045_01', 4)	# 10-13
    sprite('ka045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('ka025_01', 2)	# 1-2
    sprite('ka025_02', 2)	# 3-4

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('ka200_00', 3)	# 1-3
    sprite('ka200_01', 3)	# 4-6
    sprite('ka200_02', 11)	# 7-17	 **attackbox here**
    sprite('ka200_03', 3)	# 18-20	 **attackbox here**
    sprite('ka200_04', 3)	# 21-23
    sprite('ka200_05', 3)	# 24-26
    sprite('ka200_06', 3)	# 27-29
    sprite('ka200_07', 3)	# 30-32

@State
def CmnActAirLockWait():
    sprite('ka045_02', 1)	# 1-1
    sprite('ka045_01', 3)	# 2-4
    sprite('ka045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ka250_00', 3)	# 1-3
    sprite('ka250_01', 3)	# 4-6
    sprite('ka250_02', 11)	# 7-17	 **attackbox here**
    sprite('ka250_03', 3)	# 18-20	 **attackbox here**
    sprite('ka250_04', 3)	# 21-23
    sprite('ka250_05', 3)	# 24-26
    sprite('ka250_06', 3)	# 27-29

@State
def CmnActLandSpin():
    sprite('ka071_00', 2)	# 1-2
    label(0)
    sprite('ka071_01', 2)	# 3-4
    sprite('ka071_02', 2)	# 5-6
    sprite('ka071_03', 2)	# 7-8
    sprite('ka071_04', 2)	# 9-10
    sprite('ka071_05', 2)	# 11-12
    sprite('ka071_06', 2)	# 13-14
    sprite('ka071_07', 2)	# 15-16
    sprite('ka071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ka040_02', 3)	# 1-3
    sprite('ka040_01', 3)	# 4-6
    sprite('ka040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('ka071_00', 2)	# 1-2
    label(0)
    sprite('ka071_01', 2)	# 3-4
    sprite('ka071_02', 2)	# 5-6
    sprite('ka071_03', 2)	# 7-8
    sprite('ka071_04', 2)	# 9-10
    sprite('ka071_05', 2)	# 11-12
    sprite('ka071_06', 2)	# 13-14
    sprite('ka071_07', 2)	# 15-16
    sprite('ka071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('ka124_00', 2)	# 1-2
    label(0)
    sprite('ka124_01', 2)	# 3-4
    sprite('ka124_02', 2)	# 5-6
    sprite('ka124_03', 2)	# 7-8
    sprite('ka124_04', 2)	# 9-10
    sprite('ka124_05', 2)	# 11-12
    sprite('ka124_06', 2)	# 13-14
    sprite('ka124_07', 2)	# 15-16
    sprite('ka124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ka077_02', 4)	# 1-4
    label(0)
    sprite('ka077_03', 3)	# 5-7
    sprite('ka077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ka077_05', 5)	# 1-5
    sprite('ka077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('ka077_02', 4)	# 1-4
    label(0)
    sprite('ka077_03', 3)	# 5-7
    sprite('ka077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ka077_05', 5)	# 1-5
    sprite('ka077_06', 4)	# 6-9

@State
def CmnActBurstBegin():
    label(0)
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ka121_03', 3)	# 1-3
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ka121_07', 3)	# 1-3
    sprite('ka121_08', 3)	# 4-6
    sprite('ka020_04', 3)	# 7-9
    sprite('ka020_05', 3)	# 10-12
    sprite('ka020_06', 3)	# 13-15
    label(0)
    sprite('ka020_07', 4)	# 16-19
    sprite('ka020_08', 4)	# 20-23
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstBegin():
    label(0)
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ka121_03', 3)	# 1-3
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ka121_07', 3)	# 1-3
    sprite('ka121_08', 3)	# 4-6
    sprite('ka020_04', 3)	# 7-9
    sprite('ka020_05', 3)	# 10-12
    sprite('ka020_06', 3)	# 13-15
    label(0)
    sprite('ka020_07', 4)	# 16-19
    sprite('ka020_08', 4)	# 20-23
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ka121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ka121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('ka121_07', 4)	# 1-4
    sprite('ka121_08', 4)	# 5-8
    sprite('ka010_00', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ka121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ka121_03', 3)	# 1-3
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ka121_07', 2)	# 1-2
    sprite('ka121_08', 2)	# 3-4
    sprite('ka020_04', 2)	# 5-6
    sprite('ka020_05', 2)	# 7-8
    sprite('ka020_06', 2)	# 9-10
    sprite('ka020_07', 2)	# 11-12
    label(0)
    sprite('ka020_07', 4)	# 13-16
    sprite('ka020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PKA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ka121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ka121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('ka121_07', 4)	# 1-4
    sprite('ka121_08', 4)	# 5-8
    sprite('ka010_00', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PKA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ka121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ka121_03', 3)	# 1-3
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ka121_07', 2)	# 1-2
    sprite('ka121_08', 2)	# 3-4
    sprite('ka020_04', 3)	# 5-7
    sprite('ka020_05', 3)	# 8-10
    sprite('ka020_06', 2)	# 11-12
    label(0)
    sprite('ka020_07', 4)	# 13-16
    sprite('ka020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PKA_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ka121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('ka121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ka121_07', 3)	# 1-3
    sprite('ka121_08', 3)	# 4-6
    sprite('ka020_04', 2)	# 7-8
    sprite('ka020_05', 2)	# 9-10
    sprite('ka020_06', 2)	# 11-12
    sprite('ka020_07', 2)	# 13-14

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PKA_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    sprite('ka121_00', 2)	# 1-2
    sprite('ka121_01', 2)	# 3-4
    sprite('ka121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ka121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('ka121_03', 3)	# 1-3
    label(0)
    sprite('ka121_04', 2)	# 4-5
    sprite('ka121_05', 2)	# 6-7
    sprite('ka121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ka121_07', 2)	# 1-2
    sprite('ka121_08', 2)	# 3-4
    sprite('ka020_04', 3)	# 5-7
    sprite('ka020_05', 3)	# 8-10
    sprite('ka020_06', 2)	# 11-12
    label(0)
    sprite('ka020_07', 4)	# 13-16
    sprite('ka020_08', 4)	# 17-20
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
    sprite('null', 27)	# 1-27
    sprite('ka401_05', 2)	# 28-29
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(1500000)
    physicsYImpulse(-150000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    SFX_3('ka003')
    sprite('ka401_06ex00', 32767)	# 30-32796	 **attackbox here**
    loopRest()
    label(9)
    sprite('ka401_06ex00', 1)	# 32797-32797	 **attackbox here**
    sprite('ka401_08', 4)	# 32798-32801	 **attackbox here**
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    Unknown1084(1)
    ScreenShake(10000, 10000)
    StartMultihit()
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    sprite('ka401_50', 3)	# 32802-32804
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    sprite('ka401_09', 2)	# 32805-32806
    sprite('ka401_10', 2)	# 32807-32808
    sprite('ka401_11', 2)	# 32809-32810
    sprite('ka401_12', 2)	# 32811-32812
    sprite('ka401_13', 2)	# 32813-32814
    sprite('ka401_14', 2)	# 32815-32816
    SFX_3('ka003')
    sprite('ka401_15', 2)	# 32817-32818
    sprite('ka401_16', 1)	# 32819-32819

@State
def CmnActChangePartnerQuickIn():
    sprite('ka032_06', 3)	# 1-3
    sprite('ka032_07', 5)	# 4-8
    sprite('ka032_08', 7)	# 9-15
    sprite('ka032_11', 7)	# 16-22
    sprite('ka032_12', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ka033_01', 3)	# 1-3
    sprite('ka033_02', 3)	# 4-6
    sprite('ka033_01', 3)	# 7-9
    sprite('ka033_02', 3)	# 10-12
    sprite('ka033_01', 3)	# 13-15
    sprite('ka033_02', 3)	# 16-18
    sprite('ka033_01', 3)	# 19-21
    sprite('ka033_02', 3)	# 22-24
    sprite('ka033_01', 3)	# 25-27
    sprite('ka033_02', 3)	# 28-30
    sprite('ka033_01', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('ka033_00', 3)	# 1-3
    sprite('ka033_01', 3)	# 4-6
    SFX_3('ka003')
    sprite('ka033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('ka033_01', 3)	# 10-12
    sprite('ka033_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka033_03', 3)	# 16-18
    sprite('ka033_04', 3)	# 19-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ka000_00', 2)	# 1-2
    sprite('ka001_00', 6)	# 3-8
    sprite('ka001_01', 6)	# 9-14
    sprite('ka001_02', 6)	# 15-20
    sprite('ka001_03', 6)	# 21-26
    sprite('ka001_04', 6)	# 27-32
    SFX_3('ka000')
    sprite('ka001_05', 6)	# 33-38
    sprite('ka001_06', 6)	# 39-44
    sprite('ka001_07', 6)	# 45-50
    SFX_3('ka000')
    sprite('ka001_08', 6)	# 51-56
    sprite('ka001_09', 6)	# 57-62
    sprite('ka001_10', 6)	# 63-68
    sprite('ka001_00', 6)	# 69-74
    sprite('ka000_00', 2)	# 75-76

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
    sprite('ka020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ka020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ka010_02', 2)	# 11-12
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
    sprite('ka430_00', 3)	# 1-3
    sprite('ka430_01', 4)	# 4-7
    Unknown7007('706b613330365f30000000000000000064000000706b613330365f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ka430_02', 5)	# 8-12
    sprite('ka430_03', 5)	# 13-17
    sprite('ka430_04', 3)	# 18-20
    sprite('ka430_05', 3)	# 21-23
    sprite('ka430_06', 3)	# 24-26
    GFX_1('kaef_chairthrow_smoke', 100)
    sprite('ka430_07', 3)	# 27-29
    GFX_0('kaef430_atkline1', 100)
    SFX_3('slash_blade_slow')
    sprite('ka430_08', 3)	# 30-32	 **attackbox here**
    GFX_0('kaef430_atk1', 100)
    SFX_1('ka317')
    StartMultihit()
    sprite('ka430_09', 3)	# 33-35
    GFX_0('ka_isuyoko_assist', 0)
    Unknown23029(1, 4303, 0)
    sprite('ka430_10', 3)	# 36-38
    sprite('ka430_11', 3)	# 39-41
    sprite('ka430_12', 3)	# 42-44
    sprite('ka430_13', 4)	# 45-48
    sprite('ka430_14', 4)	# 49-52
    sprite('ka430_15', 4)	# 53-56
    sprite('ka401_11', 5)	# 57-61
    sprite('ka401_12', 5)	# 62-66
    sprite('ka401_13', 7)	# 67-73
    sprite('ka401_14', 6)	# 74-79
    sprite('ka401_15', 5)	# 80-84
    sprite('ka401_16', 5)	# 85-89

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
    sprite('ka408_00', 2)	# 1-2
    sprite('ka408_01', 2)	# 3-4
    sprite('ka408_02', 3)	# 5-7
    Unknown23029(11, 4080, 0)
    sprite('ka408_03', 3)	# 8-10
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706b613132325f30000000000000000064000000706b613132345f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ka002')
    sprite('ka408_04', 4)	# 11-14
    sprite('ka408_05', 4)	# 15-18
    sprite('ka408_06', 4)	# 19-22
    sprite('ka408_04', 4)	# 23-26
    sprite('ka408_05', 4)	# 27-30
    sprite('ka408_06', 4)	# 31-34
    sprite('ka408_04', 4)	# 35-38
    sprite('ka408_05', 4)	# 39-42
    sprite('ka408_06', 4)	# 43-46
    sprite('ka408_04', 4)	# 47-50
    sprite('ka408_05', 4)	# 51-54
    sprite('ka408_06', 4)	# 55-58
    sprite('ka408_07', 6)	# 59-64
    sprite('ka408_08', 6)	# 65-70
    sprite('ka408_09', 6)	# 71-76

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP1(70)
        AirPushbackX(80000)
        AirPushbackY(20000)
        PushbackX(60000)
        AirUntechableTime(50)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        YImpluseBeforeWallbounce(2200)
        Unknown9178(1)
        Unknown9346(0)
        WallbounceReboundTime(15)
        Unknown11042(1)
        Unknown11056(0)
        sendToLabelUpon(2, 0)
        Unknown2004(1, 0)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ka211_00', 2)	# 1-2
    sprite('ka211_01', 2)	# 3-4
    sprite('ka211_02', 2)	# 5-6
    SFX_3('hit_h_middle')
    physicsXImpulse(40000)
    physicsYImpulse(17000)
    setGravity(2800)
    Unknown7007('706b613130375f30000000000000000064000000706b613130375f31000000000000000064000000706b613130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ka211_03', 6)	# 7-12
    sprite('ka211_05', 10)	# 13-22	 **attackbox here**
    Unknown23054('6b613231315f303400000000000000000000000000000000000000000000000004000000')
    Unknown2017(0)
    label(0)
    sprite('ka211_06', 6)	# 23-28
    Unknown1084(1)
    SFX_3('ka004')
    sprite('ka211_07', 5)	# 29-33
    sprite('ka211_08', 4)	# 34-37
    sprite('ka211_09', 4)	# 38-41
    sprite('ka211_10', 4)	# 42-45
    sprite('ka211_11', 5)	# 46-50
    sprite('ka211_12', 8)	# 51-58
    sprite('ka010_02', 3)	# 59-61
    teleportRelativeX(170000)
    sprite('ka010_01', 3)	# 62-64
    sprite('ka010_00', 3)	# 65-67
    sprite('ka000_00', 2)	# 68-69

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
    Unknown2036(93, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('ka020_07', 4)	# 3-6
    sprite('ka020_08', 4)	# 7-10
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
        Unknown30063(1)
        Unknown23055('')
        AttackLevel_(5)
        Damage(500)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(80)
        Unknown9142(80)
        AirPushbackY(26000)
        YImpluseBeforeWallbounce(1000)
        Hitstop(25)
        Unknown11032('305705000000000000000000400d0300')
        Unknown9154(41)
        AirUntechableTime(81)
        Unknown30055('a08601003200000000000000')
        Unknown11068(1)
        Unknown11064(1)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1

        def upon_78():
            clearUponHandler(78)
            Unknown23029(1, 4302, 0)
            Unknown11069('ChangePartnerDD_Exe')
            Unknown2017(0)
            ScreenShake(40000, 0)
            sendToLabel(0)
    sprite('ka430_00', 3)	# 1-3
    setInvincible(1)
    sprite('ka430_01', 4)	# 4-7
    sprite('ka430_02', 5)	# 8-12
    sprite('ka430_03', 5)	# 13-17
    sprite('ka430_01', 5)	# 18-22
    sprite('ka430_02', 5)	# 23-27
    sprite('ka430_03', 5)	# 28-32
    sprite('ka430_01', 4)	# 33-36
    sprite('ka430_02', 4)	# 37-40
    sprite('ka430_03', 4)	# 41-44
    sprite('ka430_01', 4)	# 45-48
    sprite('ka430_02', 4)	# 49-52
    sprite('ka430_03', 4)	# 53-56
    sprite('ka430_04', 3)	# 57-59
    sprite('ka430_05', 3)	# 60-62
    sprite('ka430_06', 3)	# 63-65
    GFX_1('kaef_chairthrow_smoke', 100)
    sprite('ka430_07', 3)	# 66-68
    GFX_0('kaef430_atkline1', 100)
    SFX_3('slash_blade_slow')
    sprite('ka430_08', 3)	# 69-71	 **attackbox here**
    GFX_0('kaef430_atk1', 100)
    tag_voice(1, 'pka251_0', 'pka251_1', '', '')
    RefreshMultihit()
    sprite('ka430_09', 3)	# 72-74
    if SLOT_51:
        GFX_0('ka_isuyamanari', 0)
        Unknown23029(1, 4307, 0)
    else:
        GFX_0('ka_isuyoko', 0)
        Unknown23029(1, 4303, 0)
    setInvincible(0)
    sprite('ka430_10', 3)	# 75-77
    sprite('ka430_11', 3)	# 78-80
    sprite('ka430_12', 3)	# 81-83
    sprite('ka430_13', 4)	# 84-87
    sprite('ka430_14', 4)	# 88-91
    sprite('ka430_15', 4)	# 92-95
    sprite('ka401_11', 4)	# 96-99
    sprite('ka401_12', 4)	# 100-103
    sprite('ka401_13', 6)	# 104-109
    sprite('ka401_14', 4)	# 110-113
    sprite('ka401_15', 3)	# 114-116
    sprite('ka401_16', 3)	# 117-119
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(78)
    sprite('ka430_09', 3)	# 120-122
    GFX_0('ka_isuokiseme', 0)
    Unknown23029(1, 4307, 0)
    Unknown23029(1, 4306, 0)
    sprite('ka430_10', 3)	# 123-125
    sprite('ka430_11', 3)	# 126-128
    sprite('ka430_10', 3)	# 129-131
    sprite('ka430_11', 3)	# 132-134
    sprite('ka430_16', 4)	# 135-138
    sprite('ka430_17', 5)	# 139-143
    sprite('ka430_18', 5)	# 144-148
    physicsXImpulse(26000)
    physicsYImpulse(15000)
    setGravity(2200)
    SFX_3('highjump_l')
    sprite('ka430_19', 5)	# 149-153
    tag_voice(0, 'pka252_0', 'pka252_1', '', '')
    SFX_3('hit_h_middle')
    sprite('ka430_20', 3)	# 154-156	 **attackbox here**
    GFX_1('kaef_430atk2', 0)
    Unknown1019(80)
    YAccel(80)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(600)
    AirUntechableTime(51)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(0)
    AirPushbackX(12000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(1500)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Hitstop(30)
    PushbackX(70000)
    Unknown30048(1)

    def upon_78():
        ScreenShake(50000, 0)
        clearUponHandler(78)
    sprite('ka430_22', 2)	# 157-158
    sprite('ka430_23', 32767)	# 159-32925
    sendToLabelUpon(2, 2)
    loopRest()
    label(2)
    sprite('ka430_24', 3)	# 32926-32928
    Unknown1084(1)
    sprite('ka430_25', 4)	# 32929-32932
    sprite('ka430_26', 4)	# 32933-32936
    sprite('ka430_27', 8)	# 32937-32944
    SFX_3('highjump_m')
    physicsXImpulse(31000)
    physicsYImpulse(32000)
    setGravity(3000)
    sprite('ka430_28', 7)	# 32945-32951
    Unknown1019(80)
    tag_voice(0, 'pka253_0', 'pka253_1', '', '')
    sprite('ka430_29', 2)	# 32952-32953
    GFX_0('kaef430_atkline3', 100)
    SFX_3('hit_h_slow')
    Unknown1019(80)
    sprite('ka430_31', 5)	# 32954-32958	 **attackbox here**
    Unknown23054('6b613433305f333000000000000000000000000000000000000000000000000004000000')
    GFX_0('kaef430_atk3', 100)
    Unknown1019(80)
    RefreshMultihit()
    Damage(700)
    Hitstop(30)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(10000)
    AirPushbackY(-100000)
    YImpluseBeforeWallbounce(4500)
    Unknown9190(1)
    Unknown11073(1)
    Unknown11064(0)
    Unknown11069('ka_isuokiseme_DSD')

    def upon_78():
        SFX_3('quake_s')
        SFX_3('blaze_normal')
        SFX_3('bound_steal_m')
        ScreenShake(80000, 0)
        clearUponHandler(78)
    sprite('ka430_31', 32767)	# 32959-65725	 **attackbox here**
    sendToLabelUpon(2, 4)
    loopRest()
    label(4)
    sprite('ka430_32', 3)	# 65726-65728
    Unknown20000(1)
    Unknown1019(30)
    YAccel(30)
    ScreenShake(0, 20000)
    sprite('ka430_33', 3)	# 65729-65731
    Unknown1019(0)
    YAccel(0)
    sprite('ka430_32', 3)	# 65732-65734
    sprite('ka430_33', 3)	# 65735-65737
    sprite('ka430_32', 3)	# 65738-65740
    sprite('ka430_33', 3)	# 65741-65743
    sprite('ka430_32', 3)	# 65744-65746
    sprite('ka430_33', 3)	# 65747-65749
    sprite('ka430_32', 3)	# 65750-65752
    sprite('ka430_33', 3)	# 65753-65755
    sprite('ka430_32', 3)	# 65756-65758
    sprite('ka430_32', 2)	# 65759-65760
    sprite('ka430_34', 4)	# 65761-65764
    sprite('ka430_35', 3)	# 65765-65767
    sprite('ka401_11', 3)	# 65768-65770
    setInvincible(0)
    Unknown2017(1)
    sprite('ka401_12', 4)	# 65771-65774
    sprite('ka401_13', 6)	# 65775-65780
    sprite('ka401_14', 4)	# 65781-65784
    sprite('ka401_15', 3)	# 65785-65787
    sprite('ka401_16', 3)	# 65788-65790
    loopRest()

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(5)
        Damage(500)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(80)
        Unknown9142(80)
        AirPushbackY(26000)
        YImpluseBeforeWallbounce(1000)
        Hitstop(25)
        Unknown11032('305705000000000000000000400d0300')
        Unknown9154(41)
        AirUntechableTime(81)
        Unknown30055('a08601003200000000000000')
        Unknown11068(1)
        Unknown11064(1)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1

        def upon_78():
            clearUponHandler(78)
            Unknown21015('6b615f6973756f6b6973656d6500000000000000000000000000000000000000ce10000000000000')
            Unknown11069('ChangePartnerDDOD_Exe')
            Unknown2017(0)
            ScreenShake(40000, 0)
            sendToLabel(0)
    sprite('ka430_00', 3)	# 1-3
    setInvincible(1)
    sprite('ka430_01', 4)	# 4-7
    sprite('ka430_02', 5)	# 8-12
    sprite('ka430_03', 5)	# 13-17
    sprite('ka430_01', 5)	# 18-22
    sprite('ka430_02', 5)	# 23-27
    sprite('ka430_03', 5)	# 28-32
    sprite('ka430_01', 4)	# 33-36
    sprite('ka430_02', 4)	# 37-40
    sprite('ka430_03', 4)	# 41-44
    sprite('ka430_01', 4)	# 45-48
    sprite('ka430_02', 4)	# 49-52
    sprite('ka430_03', 4)	# 53-56
    sprite('ka430_04', 3)	# 57-59
    sprite('ka430_05', 3)	# 60-62
    sprite('ka430_06', 3)	# 63-65
    GFX_1('kaef_chairthrow_smoke', 100)
    sprite('ka430_07', 3)	# 66-68
    GFX_0('kaef430_atkline1', 100)
    SFX_3('slash_blade_slow')
    sprite('ka430_08', 3)	# 69-71	 **attackbox here**
    GFX_0('kaef430_atk1', 100)
    tag_voice(1, 'pka251_0', 'pka251_1', '', '')
    RefreshMultihit()
    sprite('ka430_09', 3)	# 72-74
    if SLOT_51:
        GFX_0('ka_isuyamanari', 0)
        Unknown23029(1, 4307, 0)
    else:
        GFX_0('ka_isuyoko', 0)
        Unknown23029(1, 4303, 0)
    setInvincible(0)
    sprite('ka430_10', 3)	# 75-77
    sprite('ka430_11', 3)	# 78-80
    sprite('ka430_12', 3)	# 81-83
    sprite('ka430_13', 4)	# 84-87
    sprite('ka430_14', 4)	# 88-91
    sprite('ka430_15', 4)	# 92-95
    sprite('ka401_11', 4)	# 96-99
    sprite('ka401_12', 4)	# 100-103
    sprite('ka401_13', 6)	# 104-109
    sprite('ka401_14', 4)	# 110-113
    sprite('ka401_15', 3)	# 114-116
    sprite('ka401_16', 3)	# 117-119
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(78)
    sprite('ka430_09', 3)	# 120-122
    GFX_0('ka_isuokiseme', 0)
    Unknown23029(1, 4305, 0)
    Unknown23029(1, 4306, 0)
    sprite('ka430_10', 3)	# 123-125
    sprite('ka430_11', 3)	# 126-128
    sprite('ka430_10', 3)	# 129-131
    sprite('ka430_11', 3)	# 132-134
    sprite('ka430_16', 4)	# 135-138
    sprite('ka430_17', 5)	# 139-143
    sprite('ka430_18', 5)	# 144-148
    physicsXImpulse(26000)
    physicsYImpulse(15000)
    setGravity(2200)
    SFX_3('highjump_l')
    sprite('ka430_19', 5)	# 149-153
    tag_voice(0, 'pka252_0', 'pka252_1', '', '')
    SFX_3('hit_h_middle')
    sprite('ka430_20', 3)	# 154-156	 **attackbox here**
    GFX_1('kaef_430atk2', 0)
    Unknown1019(80)
    YAccel(80)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(600)
    AirUntechableTime(51)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(0)
    AirPushbackX(12000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(1500)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Hitstop(30)
    PushbackX(70000)
    Unknown30048(1)

    def upon_78():
        ScreenShake(50000, 0)
        clearUponHandler(78)
    sprite('ka430_22', 2)	# 157-158
    sprite('ka430_23', 32767)	# 159-32925
    sendToLabelUpon(2, 2)
    loopRest()
    label(2)
    sprite('ka430_24', 3)	# 32926-32928
    Unknown1084(1)
    sprite('ka430_25', 4)	# 32929-32932
    sprite('ka430_26', 4)	# 32933-32936
    sprite('ka430_27', 8)	# 32937-32944
    SFX_3('highjump_m')
    physicsXImpulse(31000)
    physicsYImpulse(32000)
    setGravity(3000)
    sprite('ka430_28', 7)	# 32945-32951
    Unknown1019(80)
    tag_voice(0, 'pka253_0', 'pka253_1', '', '')
    sprite('ka430_29', 2)	# 32952-32953
    GFX_0('kaef430_atkline3', 100)
    SFX_3('hit_h_slow')
    Unknown1019(80)
    sprite('ka430_31', 5)	# 32954-32958	 **attackbox here**
    Unknown23054('6b613433305f333000000000000000000000000000000000000000000000000004000000')
    GFX_0('kaef430_atk3', 100)
    Unknown1019(80)
    RefreshMultihit()
    Damage(700)
    Hitstop(30)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(7000)
    AirPushbackY(-30000)
    YImpluseBeforeWallbounce(1500)
    Unknown9310(100)
    Unknown9190(1)
    Unknown11073(1)
    Unknown11069('PKA_PersonaKenkaOD_DUO')

    def upon_78():
        SFX_3('quake_s')
        SFX_3('blaze_normal')
        SFX_3('bound_steal_m')
        ScreenShake(80000, 0)
        clearUponHandler(78)
    sprite('ka430_31', 32767)	# 32959-65725	 **attackbox here**
    Unknown2015(500)
    sendToLabelUpon(2, 4)
    loopRest()
    label(4)
    sprite('ka430_32', 3)	# 65726-65728
    Unknown20000(1)
    Unknown1019(30)
    YAccel(30)
    ScreenShake(0, 20000)
    sprite('ka430_33', 3)	# 65729-65731
    Unknown1019(0)
    YAccel(0)
    sprite('ka430_32', 3)	# 65732-65734
    sprite('ka430_33', 3)	# 65735-65737
    sprite('ka430_32', 3)	# 65738-65740
    sprite('ka430_33', 3)	# 65741-65743
    Unknown23029(11, 4301, 0)
    sprite('ka430_32', 3)	# 65744-65746
    sprite('ka430_34', 6)	# 65747-65752
    sprite('ka430_35', 6)	# 65753-65758
    sprite('ka000_00', 6)	# 65759-65764
    sprite('ka432_00', 3)	# 65765-65767
    sprite('ka432_01', 3)	# 65768-65770
    sprite('ka432_02', 3)	# 65771-65773	 **attackbox here**
    Unknown7007('706b613330395f31000000000000000064000000706b613331305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ka432_03', 3)	# 65774-65776
    sprite('ka432_04', 6)	# 65777-65782
    sprite('ka432_05', 6)	# 65783-65788
    sprite('ka432_06', 6)	# 65789-65794
    sprite('ka432_07', 6)	# 65795-65800
    sprite('ka432_08', 6)	# 65801-65806
    sprite('ka432_09', 3)	# 65807-65809
    sprite('ka432_10', 3)	# 65810-65812
    sprite('ka432_11', 3)	# 65813-65815
    Unknown2015(-1)
    sprite('ka432_09', 3)	# 65816-65818
    sprite('ka432_10', 3)	# 65819-65821
    sprite('ka432_11', 3)	# 65822-65824
    sprite('ka432_09', 3)	# 65825-65827
    sprite('ka432_10', 3)	# 65828-65830
    sprite('ka432_11', 3)	# 65831-65833
    Unknown20000(0)
    sprite('ka432_09', 3)	# 65834-65836
    sprite('ka432_10', 3)	# 65837-65839
    sprite('ka432_11', 3)	# 65840-65842
    sprite('ka432_09', 3)	# 65843-65845
    sprite('ka432_10', 3)	# 65846-65848
    sprite('ka432_11', 3)	# 65849-65851
    sprite('ka432_09', 3)	# 65852-65854
    sprite('ka432_10', 3)	# 65855-65857
    sprite('ka432_11', 3)	# 65858-65860
    sprite('ka432_09', 3)	# 65861-65863
    sprite('ka432_10', 3)	# 65864-65866
    sprite('ka432_11', 3)	# 65867-65869
    sprite('ka432_09', 3)	# 65870-65872
    sprite('ka432_10', 3)	# 65873-65875
    sprite('ka432_11', 3)	# 65876-65878
    sprite('ka432_09', 3)	# 65879-65881
    sprite('ka432_10', 3)	# 65882-65884
    sprite('ka432_11', 3)	# 65885-65887
    sprite('ka432_09', 3)	# 65888-65890
    sprite('ka432_10', 3)	# 65891-65893
    sprite('ka432_11', 3)	# 65894-65896
    sprite('ka432_09', 3)	# 65897-65899
    sprite('ka432_10', 3)	# 65900-65902
    sprite('ka432_11', 3)	# 65903-65905
    sprite('ka432_12', 6)	# 65906-65911
    sprite('ka000_00', 6)	# 65912-65917
    sprite('ka401_11', 3)	# 65918-65920
    setInvincible(0)
    Unknown2017(1)
    sprite('ka401_12', 4)	# 65921-65924
    sprite('ka401_13', 6)	# 65925-65930
    sprite('ka401_14', 4)	# 65931-65934
    sprite('ka401_15', 3)	# 65935-65937
    sprite('ka401_16', 3)	# 65938-65940
    loopRest()

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
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('ka401_05', 2)	# 121-122
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    SFX_3('ka003')
    sprite('ka401_06ex00', 32767)	# 123-32889	 **attackbox here**
    loopRest()
    label(9)
    sprite('ka401_08', 5)	# 32890-32894	 **attackbox here**
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    Unknown1084(1)
    ScreenShake(10000, 10000)
    StartMultihit()
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    sprite('ka401_50', 5)	# 32895-32899
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    sprite('ka401_09', 3)	# 32900-32902
    sprite('ka401_10', 3)	# 32903-32905
    sprite('ka401_11', 2)	# 32906-32907
    sprite('ka401_12', 3)	# 32908-32910
    sprite('ka401_13', 3)	# 32911-32913
    sprite('ka401_14', 3)	# 32914-32916
    SFX_3('ka003')
    sprite('ka401_15', 2)	# 32917-32918
    sprite('ka401_16', 2)	# 32919-32920

@State
def CmnActChangeReturnAppealBurst():
    sprite('ka064_01', 30)	# 1-30
    sprite('ka064_02', 5)	# 31-35
    sprite('ka064_03', 5)	# 36-40
    sprite('ka010_02', 5)	# 41-45
    sprite('ka010_01', 5)	# 46-50
    sprite('ka010_00', 5)	# 51-55
    sprite('ka000_00', 30)	# 56-85

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown1112('')
    sprite('ka203_00', 2)	# 1-2
    sprite('ka203_01', 2)	# 3-4
    sprite('ka203_02', 2)	# 5-6
    sprite('ka203_03', 3)	# 7-9
    sprite('ka203_03', 1)	# 10-10
    label(1)
    sprite('ka203_04', 2)	# 11-12
    Unknown7007('706b613230315f30000000000000000064000000706b613230315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('fukidashi', 100)
    sprite('ka203_05', 3)	# 13-15
    sprite('ka203_05', 1)	# 16-16
    Recovery()
    Unknown2063()
    sprite('ka203_06', 3)	# 17-19
    sprite('ka203_07', 3)	# 20-22
    sprite('ka203_06', 2)	# 23-24
    sprite('ka203_07', 2)	# 25-26
    sprite('ka203_08', 2)	# 27-28

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        PushbackX(11000)
        AirPushbackY(20000)
        AirUntechableTime(19)
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ka201_00', 2)	# 1-2
    sprite('ka201_01', 2)	# 3-4
    sprite('ka201_02', 2)	# 5-6
    Unknown7009(1)
    sprite('ka201_03', 3)	# 7-9	 **attackbox here**
    SFX_3('hit_m_middle')
    StartMultihit()
    sprite('ka201_04', 3)	# 10-12	 **attackbox here**
    sprite('ka201_05', 2)	# 13-14	 **attackbox here**
    sprite('ka201_06', 4)	# 15-18
    SFX_3('ka003')
    Recovery()
    Unknown2063()
    sprite('ka201_07', 4)	# 19-22
    sprite('ka201_08', 4)	# 23-26

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(-30000)
        PushbackX(19800)
        Unknown9310(1)
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('ka202_00', 3)	# 1-3
    sprite('ka202_01', 6)	# 4-9
    sprite('ka202_02', 5)	# 10-14
    Unknown7009(2)
    sprite('ka202_03', 2)	# 15-16
    SFX_3('hit_h_middle')
    sprite('ka202_05', 6)	# 17-22	 **attackbox here**
    Unknown23054('6b613230325f303400000000000000000000000000000000000000000000000006000000')
    SFX_3('ka004')
    sprite('ka202_05', 7)	# 23-29	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ka202_06', 8)	# 30-37
    sprite('ka202_07', 4)	# 38-41
    sprite('ka202_08', 4)	# 42-45
    sprite('ka202_09', 3)	# 46-48

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('ka408_00', 2)	# 1-2
    sprite('ka408_01', 2)	# 3-4
    sprite('ka408_02', 3)	# 5-7
    Unknown23029(11, 2540, 0)
    sprite('ka408_03', 3)	# 8-10
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706b613231355f30000000000000000064000000706b613231355f31000000000000000064000000706b613231355f32000000000000000064000000706b613231365f32000000000000000064000000')
    SFX_3('ka002')
    sprite('ka408_04', 4)	# 11-14
    sprite('ka408_05', 4)	# 15-18
    sprite('ka408_06', 4)	# 19-22
    sprite('ka408_04', 4)	# 23-26
    sprite('ka408_05', 4)	# 27-30
    sprite('ka408_06', 4)	# 31-34
    sprite('ka408_07', 6)	# 35-40
    Recovery()
    Unknown2063()
    sprite('ka408_08', 6)	# 41-46
    sprite('ka408_09', 6)	# 47-52

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(12000)
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ka200_00', 2)	# 1-2
    sprite('ka200_01', 1)	# 3-3
    sprite('ka200_01', 2)	# 4-5
    Unknown1051(80)
    sprite('ka200_03', 3)	# 6-8	 **attackbox here**
    Unknown23054('6b613230305f303200000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_m_fast')
    Unknown7009(0)
    sprite('ka200_03', 2)	# 9-10	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ka200_04', 4)	# 11-14
    sprite('ka200_05', 4)	# 15-18
    sprite('ka200_06', 4)	# 19-22
    sprite('ka200_07', 3)	# 23-25

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        PushbackX(15000)
        AirPushbackY(20000)
        Hitstop(14)
        AirUntechableTime(19)
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ka207_00', 2)	# 1-2
    sprite('ka207_01', 3)	# 3-5
    sprite('ka207_02', 4)	# 6-9
    physicsXImpulse(25000)
    Unknown7009(4)
    SFX_3('hit_m_middle')
    sprite('ka207_04', 3)	# 10-12	 **attackbox here**
    Unknown23054('6b613230375f303300000000000000000000000000000000000000000000000003000000')
    Unknown1019(0)
    SFX_3('ka003')
    RefreshMultihit()
    sprite('ka207_05', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('ka207_06', 3)	# 16-18
    sprite('ka207_07', 3)	# 19-21
    sprite('ka207_08', 4)	# 22-25
    sprite('ka207_09', 4)	# 26-29

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(100)
        AttackP2(85)
        HitOrBlockCancel('NmlAtk4A4th_Land')
        Unknown11044(1)

        def upon_78():
            Hitstop(0)
            enterState('NmlAtk4A3rd_Plus')
    sprite('ka208_00', 5)	# 1-5
    sprite('ka208_01', 5)	# 6-10
    sprite('ka208_02', 4)	# 11-14
    physicsXImpulse(20000)
    Unknown7009(2)
    SFX_3('hit_h_middle')
    sprite('ka208_03', 3)	# 15-17	 **attackbox here**
    Unknown1019(0)
    sprite('ka208_04', 5)	# 18-22
    Recovery()
    Unknown2063()
    sprite('ka208_05', 5)	# 23-27
    sprite('ka208_06', 5)	# 28-32
    sprite('ka208_07', 5)	# 33-37
    sprite('ka208_08', 5)	# 38-42

@State
def NmlAtk4A3rd_Plus():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk4A3rd_Exe', 1, 0, 0)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(0)
        Hitstop(16)
        Unknown11045(0)
        Unknown30061(1)
        setInvincible(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)

        def upon_78():
            Hitstop(0)
    sprite('keep', 1)	# 1-1
    sprite('ka208_04', 4)	# 2-5
    setInvincible(0)
    Recovery()
    sprite('ka208_05', 4)	# 6-9
    sprite('ka208_06', 4)	# 10-13
    sprite('ka208_07', 4)	# 14-17
    sprite('ka208_08', 4)	# 18-21

@State
def NmlAtk4A3rd_Exe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        AirUntechableTime(30)
        Hitstop(0)
        PushbackX(0)
        AirPushbackX(-1000)
        AirPushbackY(-3000)
        Unknown11068(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11091(0)
        Unknown2004(0, 1)
        sendToLabelUpon(2, 1)
        if Unknown48('1900000002000000000000001b00000002000000aa000000'):
            YImpluseBeforeWallbounce(800)
        else:
            YImpluseBeforeWallbounce(-100)
    sprite('ka208_03', 6)	# 1-6	 **attackbox here**
    StartMultihit()
    Unknown5000(10, 0)
    Unknown5001('0100000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('ka209_00', 3)	# 7-9
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka209_01', 3)	# 10-12
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka209_02', 3)	# 13-15
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka209_03', 3)	# 16-18
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    physicsYImpulse(60000)
    setGravity(2200)
    sprite('ka209_04', 3)	# 19-21
    YAccel(50)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka209_05', 3)	# 22-24
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 50)
    sprite('ka209_06', 5)	# 25-29	 **attackbox here**
    RefreshMultihit()
    JumpCancel_(0)
    Unknown11069('NmlAtk4A3rd_Exe')
    sprite('ka209_07', 3)	# 30-32
    Unknown1039(25)
    sprite('ka209_08', 9)	# 33-41
    sprite('ka209_09', 9)	# 42-50
    Unknown1039(200)
    sprite('ka209_11', 8)	# 51-58	 **attackbox here**
    Unknown23054('6b613230395f313000000000000000000000000000000000000000000000000003000000')

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
        Unknown14070('NmlAtk4A4th')
        Unknown11069('')
    RefreshMultihit()
    Unknown11068(1)
    Unknown2018(1, 50)
    AttackLevel_(4)
    Damage(1500)
    Unknown9287()
    AirPushbackX(10000)
    AirPushbackY(-46000)
    YImpluseBeforeWallbounce(0)
    Hitstop(20)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    ScreenShake(15000, 15000)
    Unknown9190(1)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1039(200)
    sprite('ka209_12', 1)	# 59-59
    Unknown14072('NmlAtk4A4th')
    sprite('ka209_12', 2)	# 60-61
    Unknown14074('NmlAtk4A4th')
    sprite('ka209_13', 3)	# 62-64
    sprite('ka209_14', 3)	# 65-67
    sprite('ka020_04', 3)	# 68-70
    sprite('ka020_05', 3)	# 71-73
    sprite('ka020_06', 3)	# 74-76
    label(0)
    sprite('ka020_07', 3)	# 77-79
    sprite('ka020_08', 3)	# 80-82
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka064_02', 8)	# 83-90
    sprite('ka064_03', 6)	# 91-96

@State
def NmlAtk4A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
        sendToLabelUpon(2, 1)
    sprite('ka254_00', 3)	# 1-3
    sprite('ka254_01', 5)	# 4-8
    Unknown23029(11, 2540, 0)
    Unknown1084(1)
    sprite('ka254_02', 5)	# 9-13
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706b613231355f31000000000000000064000000706b613231355f32000000000000000064000000706b613231365f31000000000000000064000000706b613231365f32000000000000000064000000')
    SFX_3('ka002')
    sprite('ka254_03', 3)	# 14-16
    sprite('ka254_04', 3)	# 17-19
    sprite('ka254_05', 3)	# 20-22
    sprite('ka254_03', 3)	# 23-25
    sprite('ka254_04', 3)	# 26-28
    sprite('ka254_05', 3)	# 29-31
    sprite('ka254_03', 3)	# 32-34
    Recovery()
    Unknown2063()
    Unknown1044()
    sprite('ka254_01', 3)	# 35-37
    sprite('ka254_00', 3)	# 38-40
    sprite('ka020_04', 3)	# 41-43
    sprite('ka020_05', 3)	# 44-46
    sprite('ka020_06', 3)	# 47-49
    label(0)
    sprite('ka020_07', 3)	# 50-52
    sprite('ka020_08', 3)	# 53-55
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka064_02', 3)	# 56-58
    sprite('ka064_03', 3)	# 59-61

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')

        def upon_24():
            SLOT_52 = 1
            clearUponHandler(24)
    sprite('ka204_00', 4)	# 1-4
    sprite('ka204_01', 3)	# 5-7
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 2040, 0)
    SFX_3('hit_h_fast')
    sprite('ka204_02', 3)	# 8-10
    sprite('ka204_03', 3)	# 11-13
    sprite('ka204_04', 3)	# 14-16
    if (not SLOT_52):
        clearUponHandler(24)
        sendToLabel(0)
    sprite('ka204_02', 4)	# 17-20
    Unknown21015('504b415f506572736f6e61354200000000000000000000000000000000000000f907000000000000')
    Unknown7007('706b613132305f30000000000000000064000000706b613132305f31000000000000000064000000706b613132335f32000000000000000064000000706b613132345f32000000000000000064000000')
    sprite('ka204_03', 2)	# 21-22
    sprite('ka204_03', 2)	# 23-24
    Recovery()
    Unknown2063()
    sprite('ka204_04', 4)	# 25-28
    sprite('ka204_02', 4)	# 29-32
    sprite('ka204_03', 4)	# 33-36
    sprite('ka204_04', 4)	# 37-40
    sprite('ka204_02', 3)	# 41-43
    sprite('ka204_03', 3)	# 44-46
    sprite('ka204_04', 3)	# 47-49
    sprite('ka204_05', 2)	# 50-51
    loopRest()
    ExitState()
    label(0)
    sprite('ka204_02', 3)	# 52-54
    SFX_3('electric_m')

    def upon_3():
        sendToLabelUpon(24, 1)
    sprite('ka204_03', 3)	# 55-57
    sprite('ka204_04', 3)	# 58-60
    SLOT_51 = (SLOT_51 + 1)
    if (SLOT_51 == 3):
        sendToLabel(2)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    clearUponHandler(24)
    sprite('ka204_02', 4)	# 61-64
    Unknown7007('706b613132305f30000000000000000064000000706b613132305f31000000000000000064000000706b613132335f32000000000000000064000000706b613132345f32000000000000000064000000')
    if (SLOT_51 == 3):
        Unknown21015('504b415f506572736f6e61354200000000000000000000000000000000000000fb07000000000000')
    else:
        Unknown21015('504b415f506572736f6e61354200000000000000000000000000000000000000fa07000000000000')
    sprite('ka204_03', 4)	# 65-68
    sprite('ka204_04', 4)	# 69-72
    sprite('ka204_02', 3)	# 73-75
    sprite('ka204_02', 1)	# 76-76
    Recovery()
    Unknown2063()
    sprite('ka204_03', 4)	# 77-80
    sprite('ka204_04', 4)	# 81-84
    sprite('ka204_02', 3)	# 85-87
    sprite('ka204_03', 3)	# 88-90
    sprite('ka204_04', 3)	# 91-93
    sprite('ka204_02', 3)	# 94-96
    sprite('ka204_03', 3)	# 97-99
    sprite('ka204_04', 3)	# 100-102
    sprite('ka204_05', 2)	# 103-104
    loopRest()
    ExitState()
    label(2)
    clearUponHandler(3)
    clearUponHandler(24)
    sprite('ka204_04', 3)	# 105-107
    Unknown23090(11)
    sprite('ka204_05', 2)	# 108-109
    loopRest()

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')

        def upon_24():
            SLOT_52 = 1
            clearUponHandler(24)
    sprite('ka205_00', 2)	# 1-2
    sprite('ka205_01', 2)	# 3-4
    sprite('ka205_02', 3)	# 5-7
    sprite('ka205_03', 3)	# 8-10
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 2050, 0)
    SFX_3('hit_h_fast')
    sprite('ka205_04', 2)	# 11-12
    sprite('ka205_05', 2)	# 13-14
    sprite('ka205_06', 1)	# 15-15
    if SLOT_52:
        sendToLabel(1)
    clearUponHandler(24)
    sendToLabelUpon(24, 1)
    label(0)
    sprite('ka205_06', 4)	# 16-19
    SFX_3('electric_m')
    sprite('ka205_04', 4)	# 20-23
    sprite('ka205_05', 4)	# 24-27
    SLOT_51 = (SLOT_51 + 1)
    if (SLOT_51 == 2):
        sendToLabel(2)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(24)
    sprite('ka205_06', 4)	# 28-31
    Unknown7007('706b613132315f30000000000000000064000000706b613132325f30000000000000000064000000706b613132335f30000000000000000064000000706b613132345f30000000000000000064000000')
    if (SLOT_51 == 2):
        Unknown23029(11, 2052, 0)
    else:
        Unknown23029(11, 2051, 0)
    sprite('ka205_04', 2)	# 32-33
    sprite('ka205_04', 3)	# 34-36
    Recovery()
    Unknown2063()
    sprite('ka205_05', 4)	# 37-40
    sprite('ka205_02', 4)	# 41-44
    sprite('ka205_01', 4)	# 45-48
    sprite('ka205_00', 4)	# 49-52
    loopRest()
    ExitState()
    label(2)
    clearUponHandler(24)
    sprite('ka205_02', 3)	# 53-55
    Unknown23090(11)
    sprite('ka205_01', 3)	# 56-58
    sprite('ka205_00', 3)	# 59-61
    loopRest()

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackY(22000)
        HitLow(2)
        Unknown11028(14)
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ka230_00', 2)	# 1-2
    sprite('ka230_01', 1)	# 3-3
    sprite('ka230_01', 2)	# 4-5
    Unknown1051(80)
    sprite('ka230_02', 2)	# 6-7
    sprite('ka230_04', 3)	# 8-10	 **attackbox here**
    Unknown23054('6b613233305f303300000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_h_fast')
    Unknown7009(3)
    sprite('ka230_04', 4)	# 11-14	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ka230_01', 4)	# 15-18
    sprite('ka230_00', 4)	# 19-22

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(24)
        AirPushbackX(3000)
        AirPushbackY(40000)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('ka231_00', 4)	# 1-4
    sprite('ka231_01', 4)	# 5-8
    sprite('ka231_02', 4)	# 9-12
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ka231_03', 5)	# 13-17
    Unknown7007('706b613130365f30000000000000000064000000706b613130365f31000000000000000064000000706b613130365f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_slow')
    sprite('ka231_04', 3)	# 18-20	 **attackbox here**
    sprite('ka231_05', 4)	# 21-24
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ka231_06', 4)	# 25-28
    sprite('ka231_05', 5)	# 29-33
    sprite('ka231_06', 5)	# 34-38
    sprite('ka231_07', 5)	# 39-43
    SFX_3('ka003')
    sprite('ka231_08', 5)	# 44-48
    sprite('ka231_09', 3)	# 49-51

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(12000)
        AirPushbackY(12000)
        PushbackX(60000)
        Unknown9310(12)
        Unknown2004(1, 0)
        JumpCancel_(0)
        sendToLabelUpon(2, 0)

        def upon_78():
            Unknown2037(1)
    sprite('ka211_00', 2)	# 1-2
    sprite('ka211_01', 2)	# 3-4
    sprite('ka211_02', 2)	# 5-6
    SFX_3('hit_h_middle')
    physicsXImpulse(25000)
    physicsYImpulse(15000)
    setGravity(4000)
    Unknown7007('706b613130375f30000000000000000064000000706b613130375f31000000000000000064000000706b613130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ka211_03', 6)	# 7-12
    sprite('ka211_05', 10)	# 13-22	 **attackbox here**
    Unknown23054('6b613231315f303400000000000000000000000000000000000000000000000004000000')
    Unknown14070('Oiuchi')
    label(0)
    sprite('ka211_06', 1)	# 23-23
    Unknown1084(1)
    SFX_3('ka004')
    sprite('ka211_06', 5)	# 24-28
    Recovery()
    Unknown2063()
    if SLOT_2:
        Unknown14072('Oiuchi')
    sprite('ka211_07', 5)	# 29-33
    Unknown14074('Oiuchi')
    sprite('ka211_08', 4)	# 34-37
    sprite('ka211_09', 4)	# 38-41
    sprite('ka211_10', 4)	# 42-45
    sprite('ka211_11', 5)	# 46-50
    sprite('ka211_12', 8)	# 51-58

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        HitOrBlockJumpCancel(1)
        WhiffCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('ka250_00', 3)	# 1-3
    sprite('ka250_01', 6)	# 4-9
    sprite('ka250_03', 3)	# 10-12	 **attackbox here**
    Unknown23054('6b613235305f303200000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_m_fast')
    Unknown7009(3)
    sprite('ka250_03', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ka250_04', 3)	# 15-17
    sprite('ka250_05', 3)	# 18-20
    WhiffCancelEnable(1)
    sprite('ka250_06', 3)	# 21-23

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirPushbackY(18000)
        AirUntechableTime(22)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('ka321_02', 2)	# 1-2
    sprite('ka321_03', 2)	# 3-4
    sprite('ka321_04', 2)	# 5-6
    sprite('ka321_05', 2)	# 7-8
    sprite('ka321_06', 2)	# 9-10
    SFX_3('slash_sword_middle')
    sprite('ka321_07', 2)	# 11-12
    sprite('ka321_09ex00', 4)	# 13-16	 **attackbox here**
    Unknown23054('6b613332315f303800000000000000000000000000000000000000000000000004000000')
    RefreshMultihit()
    Unknown7009(4)
    SFX_3('ka004')
    sprite('ka321_09', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('ka321_10', 3)	# 20-22
    sprite('ka321_11', 3)	# 23-25

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirPushbackY(20000)
        AirUntechableTime(22)
        HitOrBlockJumpCancel(1)
        PushbackX(40000)
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('ka251_00', 4)	# 1-4
    sprite('ka251_01', 8)	# 5-12
    sprite('ka251_02', 3)	# 13-15
    SFX_3('slash_blade_slow')
    sprite('ka251_04', 3)	# 16-18	 **attackbox here**
    Unknown23054('6b613235315f303300000000000000000000000000000000000000000000000003000000')
    Unknown7009(2)
    sprite('ka251_04', 2)	# 19-20	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ka251_05', 6)	# 21-26
    sprite('ka251_06', 3)	# 27-29
    SFX_3('ka003')
    sprite('ka251_07', 3)	# 30-32
    sprite('ka251_08', 3)	# 33-35
    sprite('ka251_09', 2)	# 36-37

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)
    sprite('ka253_00', 3)	# 1-3
    sprite('ka253_01', 4)	# 4-7
    Unknown23029(11, 2530, 0)
    GFX_1('persona_enter_ply', 0)
    sprite('ka253_02', 4)	# 8-11
    sprite('ka253_02', 1)	# 12-12
    sendToLabelUpon(25, 1)
    label(0)
    sprite('ka253_01', 3)	# 13-15
    sprite('ka253_02', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(25)
    sprite('ka253_03', 2)	# 19-20
    setInvincible(1)
    Unknown22019('0000000001000000000000000000000000000000')
    Unknown1084(1)
    physicsXImpulse(-15000)
    physicsYImpulse(30000)
    Unknown22004(9, 9)
    sprite('ka253_04', 2)	# 21-22
    Unknown23029(11, 2531, 0)
    Unknown1019(80)
    YAccel(80)
    sprite('ka253_05', 5)	# 23-27
    Unknown1019(80)
    YAccel(80)
    Unknown7007('706b613132305f30000000000000000064000000706b613132335f32000000000000000064000000706b613132345f30000000000000000064000000706b613132345f32000000000000000064000000')
    SFX_3('hit_m_fast')
    sprite('ka253_06', 1)	# 28-28
    Unknown1019(50)
    YAccel(50)
    sprite('ka253_06', 4)	# 29-32
    setInvincible(0)
    sprite('ka253_07', 5)	# 33-37
    Recovery()
    Unknown2063()
    Unknown1019(50)
    YAccel(50)
    sprite('ka253_06', 5)	# 38-42
    YAccel(0)
    setGravity(4000)
    sprite('ka253_07', 5)	# 43-47
    sprite('ka253_09', 5)	# 48-52
    sprite('ka020_04', 3)	# 53-55
    sprite('ka020_05', 3)	# 56-58
    sprite('ka020_06', 3)	# 59-61
    label(2)
    sprite('ka020_07', 3)	# 62-64
    sprite('ka020_08', 3)	# 65-67
    gotoLabel(2)

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('ka210_00', 3)	# 1-3
    sprite('ka210_01', 1)	# 4-4
    tag_voice(1, 'pka156_0', 'pka156_1', '', '')
    sprite('ka210_01', 2)	# 5-6
    sprite('ka210_02', 3)	# 7-9
    sprite('ka210_03', 2)	# 10-11
    sprite('ka210_03', 2)	# 12-13
    sprite('ka210_04', 4)	# 14-17
    sprite('ka210_05', 1)	# 18-18
    physicsXImpulse(40000)
    sprite('ka210_05', 2)	# 19-20
    sprite('ka210_05', 1)	# 21-21
    SFX_3('hit_h_fast')
    sprite('ka210_06', 1)	# 22-22	 **attackbox here**
    Unknown1019(80)
    sprite('ka210_06', 2)	# 23-24	 **attackbox here**
    Unknown1019(50)
    sprite('ka210_07', 4)	# 25-28
    Unknown1019(0)
    sprite('ka210_08', 6)	# 29-34
    sprite('ka210_09', 7)	# 35-41
    sprite('ka210_10', 7)	# 42-48

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
    physicsXImpulse(10000)
    sprite('ka210_06', 3)	# 2-4	 **attackbox here**
    sprite('ka210_07', 3)	# 5-7
    Unknown1019(80)
    sprite('ka210_08', 2)	# 8-9
    Unknown1019(50)
    sprite('ka210_09', 2)	# 10-11
    Unknown1019(20)
    sprite('ka210_10', 2)	# 12-13
    Unknown1019(0)
    sprite('ka010_00', 2)	# 14-15
    sprite('ka010_01', 2)	# 16-17
    sprite('ka232_00', 3)	# 18-20
    sprite('ka232_01', 3)	# 21-23
    Unknown23029(11, 2053, 0)
    Unknown4020(11)
    GFX_1('persona_enter_ply', 0)
    SFX_3('hit_h_fast')
    sprite('ka232_02', 4)	# 24-27
    sprite('ka232_03', 2)	# 28-29
    tag_voice(0, 'pka157_0', 'pka157_1', '', '')
    sprite('ka232_03', 2)	# 30-31
    RefreshMultihit()
    sprite('ka232_04', 4)	# 32-35
    sprite('ka232_02', 4)	# 36-39
    sprite('ka232_03', 4)	# 40-43
    sprite('ka232_04', 4)	# 44-47
    sprite('ka232_02', 3)	# 48-50
    sprite('ka232_03', 3)	# 51-53
    sprite('ka232_04', 3)	# 54-56
    loopRest()
    sprite('ka001_00', 7)	# 57-63
    sprite('ka001_01', 7)	# 64-70
    sprite('ka001_02', 7)	# 71-77
    sprite('ka001_03', 7)	# 78-84
    sprite('ka001_04', 7)	# 85-91
    SFX_3('ka000')
    sprite('ka001_05', 7)	# 92-98
    sprite('ka001_06', 7)	# 99-105
    sprite('ka001_07', 7)	# 106-112
    SFX_3('ka000')
    sprite('ka001_08', 7)	# 113-119
    sprite('ka001_09', 7)	# 120-126
    sprite('ka001_10', 7)	# 127-133
    sprite('ka001_00', 7)	# 134-140
    label(0)
    sprite('ka000_00', 6)	# 141-146
    sprite('ka000_01', 6)	# 147-152
    sprite('ka000_02', 6)	# 153-158
    sprite('ka000_03', 6)	# 159-164
    sprite('ka000_04', 6)	# 165-170
    sprite('ka000_05', 6)	# 171-176
    sprite('ka000_06', 6)	# 177-182
    sprite('ka000_07', 6)	# 183-188
    sprite('ka000_08', 6)	# 189-194
    sprite('ka000_09', 6)	# 195-200
    sprite('ka000_10', 6)	# 201-206
    sprite('ka000_11', 6)	# 207-212
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 213-213

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ka231_00', 3)	# 1-3
    sprite('ka231_01', 3)	# 4-6
    sprite('ka231_02', 4)	# 7-10
    sprite('ka231_03', 4)	# 11-14
    SFX_3('slash_blade_slow')
    sprite('ka231_04', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('ka231_05', 4)	# 18-21
    sprite('ka231_06', 4)	# 22-25
    sprite('ka231_05', 5)	# 26-30
    sprite('ka231_06', 5)	# 31-35
    sprite('ka231_07', 5)	# 36-40
    SFX_3('ka003')
    sprite('ka231_08', 5)	# 41-45
    sprite('ka231_09', 3)	# 46-48
    sprite('ka001_00', 7)	# 49-55
    sprite('ka001_01', 7)	# 56-62
    sprite('ka001_02', 7)	# 63-69
    sprite('ka001_03', 7)	# 70-76
    sprite('ka001_04', 7)	# 77-83
    SFX_3('ka000')
    sprite('ka001_05', 7)	# 84-90
    sprite('ka001_06', 7)	# 91-97
    sprite('ka001_07', 7)	# 98-104
    SFX_3('ka000')
    sprite('ka001_08', 7)	# 105-111
    sprite('ka001_09', 7)	# 112-118
    sprite('ka001_10', 7)	# 119-125
    sprite('ka001_00', 7)	# 126-132
    label(0)
    sprite('ka000_00', 6)	# 133-138
    sprite('ka000_01', 6)	# 139-144
    sprite('ka000_02', 6)	# 145-150
    sprite('ka000_03', 6)	# 151-156
    sprite('ka000_04', 6)	# 157-162
    sprite('ka000_05', 6)	# 163-168
    sprite('ka000_06', 6)	# 169-174
    sprite('ka000_07', 6)	# 175-180
    sprite('ka000_08', 6)	# 181-186
    sprite('ka000_09', 6)	# 187-192
    sprite('ka000_10', 6)	# 193-198
    sprite('ka000_11', 6)	# 199-204
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 205-205

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('ka430_00', 2)	# 1-2
    sprite('ka430_01', 2)	# 3-4
    sprite('ka430_02', 2)	# 5-6
    sprite('ka430_03', 2)	# 7-8
    sprite('ka430_04', 2)	# 9-10
    sprite('ka430_05', 3)	# 11-13
    sprite('ka430_06', 3)	# 14-16
    GFX_1('kaef_chairthrow_smoke', 100)
    sprite('ka430_07', 3)	# 17-19
    GFX_0('kaef430_atkline1', 100)
    SFX_3('slash_blade_slow')
    tag_voice(0, 'pka158_0', 'pka158_1', '', '')
    sprite('ka430_08', 3)	# 20-22	 **attackbox here**
    GFX_0('kaef430_atk1', 100)
    RefreshMultihit()
    sprite('ka430_09', 3)	# 23-25
    sprite('ka430_10', 3)	# 26-28
    sprite('ka430_11', 3)	# 29-31
    sprite('ka430_12', 3)	# 32-34
    sprite('ka430_13', 3)	# 35-37
    sprite('ka430_14', 3)	# 38-40
    sprite('ka430_15', 3)	# 41-43
    sprite('ka401_11', 3)	# 44-46
    sprite('ka401_12', 3)	# 47-49
    sprite('ka401_13', 3)	# 50-52
    sprite('ka401_14', 3)	# 53-55
    sprite('ka401_15', 2)	# 56-57
    sprite('ka401_16', 2)	# 58-59
    sprite('ka000_00', 1)	# 60-60
    loopRest()

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 25)	# 1-25
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 26-26
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('ka251_00', 4)	# 27-30
    physicsXImpulse(35000)
    physicsYImpulse(-25000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('ka251_01', 8)	# 31-38
    sprite('ka251_02', 3)	# 39-41
    SFX_3('slash_blade_slow')
    sprite('ka251_04', 3)	# 42-44	 **attackbox here**
    Unknown23054('6b613235315f303300000000000000000000000000000000000000000000000003000000')
    sprite('ka251_04', 2)	# 45-46	 **attackbox here**
    sprite('ka251_05', 6)	# 47-52
    sprite('ka251_06', 3)	# 53-55
    SFX_3('ka003')
    sprite('ka251_07', 3)	# 56-58
    sprite('ka251_08', 3)	# 59-61
    sprite('ka251_09', 2)	# 62-63
    label(2)
    sprite('ka010_00', 3)	# 64-66
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('ka000_00', 6)	# 67-72
    sprite('ka000_01', 6)	# 73-78
    sprite('ka000_02', 6)	# 79-84
    sprite('ka000_03', 6)	# 85-90
    sprite('ka000_04', 6)	# 91-96
    sprite('ka000_05', 6)	# 97-102
    sprite('ka000_06', 6)	# 103-108
    sprite('ka000_07', 6)	# 109-114
    sprite('ka000_08', 6)	# 115-120
    sprite('ka000_09', 6)	# 121-126
    sprite('ka000_10', 6)	# 127-132
    sprite('ka000_11', 6)	# 133-138

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('ka204_00', 3)	# 1-3
    sprite('ka204_01', 3)	# 4-6
    Unknown23029(11, 2044, 0)
    Unknown4020(11)
    GFX_1('persona_enter_ply', 0)
    SFX_3('hit_h_fast')
    sprite('ka204_02', 4)	# 7-10
    sprite('ka204_03', 1)	# 11-11
    sprite('ka204_03', 3)	# 12-14
    RefreshMultihit()
    sprite('ka204_04', 4)	# 15-18
    sprite('ka204_02', 4)	# 19-22
    sprite('ka204_03', 2)	# 23-24
    sprite('ka204_03', 2)	# 25-26
    sprite('ka204_04', 4)	# 27-30
    sprite('ka204_02', 4)	# 31-34
    sprite('ka204_03', 4)	# 35-38
    sprite('ka204_04', 4)	# 39-42
    sprite('ka204_02', 3)	# 43-45
    sprite('ka204_03', 3)	# 46-48
    sprite('ka204_04', 3)	# 49-51
    sprite('ka204_05', 2)	# 52-53
    loopRest()
    sprite('ka001_00', 7)	# 54-60
    sprite('ka001_01', 7)	# 61-67
    sprite('ka001_02', 7)	# 68-74
    sprite('ka001_03', 7)	# 75-81
    sprite('ka001_04', 7)	# 82-88
    SFX_3('ka000')
    sprite('ka001_05', 7)	# 89-95
    sprite('ka001_06', 7)	# 96-102
    sprite('ka001_07', 7)	# 103-109
    SFX_3('ka000')
    sprite('ka001_08', 7)	# 110-116
    sprite('ka001_09', 7)	# 117-123
    sprite('ka001_10', 7)	# 124-130
    sprite('ka001_00', 7)	# 131-137
    sprite('ka000_00', 6)	# 138-143
    sprite('ka000_01', 6)	# 144-149
    sprite('ka000_02', 6)	# 150-155
    sprite('ka000_03', 6)	# 156-161
    sprite('ka000_04', 6)	# 162-167
    sprite('ka000_05', 6)	# 168-173
    sprite('ka000_06', 6)	# 174-179
    sprite('ka000_07', 6)	# 180-185
    sprite('ka000_08', 6)	# 186-191
    sprite('ka000_09', 6)	# 192-197
    sprite('ka000_10', 6)	# 198-203
    sprite('ka000_11', 6)	# 204-209

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ka430_00', 2)	# 1-2
    sprite('ka430_01', 2)	# 3-4
    sprite('ka430_02', 2)	# 5-6
    sprite('ka430_03', 2)	# 7-8
    sprite('ka430_04', 2)	# 9-10
    sprite('ka430_05', 3)	# 11-13
    sprite('ka430_06', 3)	# 14-16
    GFX_1('kaef_chairthrow_smoke', 100)
    sprite('ka430_07', 3)	# 17-19
    GFX_0('kaef430_atkline1', 100)
    SFX_3('slash_blade_slow')
    sprite('ka430_08', 3)	# 20-22	 **attackbox here**
    GFX_0('kaef430_atk1', 100)
    RefreshMultihit()
    sprite('ka430_09', 3)	# 23-25
    sprite('ka430_10', 3)	# 26-28
    sprite('ka430_11', 3)	# 29-31
    sprite('ka430_12', 3)	# 32-34
    sprite('ka430_13', 3)	# 35-37
    sprite('ka430_14', 3)	# 38-40
    sprite('ka430_15', 3)	# 41-43
    sprite('ka401_11', 3)	# 44-46
    sprite('ka401_12', 3)	# 47-49
    sprite('ka401_13', 3)	# 50-52
    sprite('ka401_14', 3)	# 53-55
    sprite('ka401_15', 2)	# 56-57
    sprite('ka401_16', 2)	# 58-59
    sprite('ka000_00', 1)	# 60-60
    loopRest()

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
    sprite('ka310_00', 7)	# 1-7
    sprite('ka310_01', 3)	# 8-10
    Unknown1051(150)
    physicsXImpulse(32000)
    Unknown8007(100, 1, 1)
    sprite('ka310_01', 2)	# 11-12
    Unknown1019(80)
    sprite('ka310_01', 2)	# 13-14
    Unknown1019(80)
    sprite('ka310_01', 2)	# 15-16
    Unknown1019(80)
    sprite('ka310_02', 3)	# 17-19
    sprite('ka310_03', 3)	# 20-22	 **attackbox here**
    Unknown1019(50)
    sprite('ka310_04', 6)	# 23-28
    Unknown1019(50)
    SFX_4('pka154')
    SFX_3('ka003')
    Unknown8010(100, 1, 1)
    sprite('ka310_05', 11)	# 29-39
    Unknown1019(0)
    sprite('ka310_06', 6)	# 40-45

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2004(1, 0)
        AttackLevel_(5)
        Damage(2000)
        AttackP2(50)
        Hitstop(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(500)
        Unknown9178(1)
        WallbounceReboundTime(25)
        Unknown9346(0)
        AirUntechableTime(120)
        Unknown9310(12)
        Unknown23086(1)
        Unknown21015('6b615f6973756f6b6973656d6500000000000000000000000000000000000000ce10000000000000')
    sprite('ka310_03', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('ka403_00', 3)	# 4-6
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka403_01', 3)	# 7-9
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka403_02', 10)	# 10-19
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka403_03', 3)	# 20-22
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_4('pka153')
    sprite('ka403_04', 3)	# 23-25
    Unknown5000(25, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ka403_05', 3)	# 26-28
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ka403_06', 3)	# 29-31	 **attackbox here**
    Unknown11072(1, 0, 70000)
    sprite('ka403_07', 4)	# 32-35
    Unknown2017(1)
    Unknown2016(200)
    sprite('ka403_08', 6)	# 36-41
    sprite('ka403_09', 6)	# 42-47
    sprite('ka403_10', 6)	# 48-53
    sprite('ka403_08', 6)	# 54-59
    sprite('ka403_09', 1)	# 60-60
    sprite('ka403_09', 3)	# 61-63
    sprite('ka403_10', 4)	# 64-67
    sprite('ka403_11', 3)	# 68-70
    sprite('ka403_12', 3)	# 71-73

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
    sprite('ka310_00', 7)	# 1-7
    sprite('ka310_01', 3)	# 8-10
    Unknown1051(150)
    physicsXImpulse(32000)
    Unknown8007(100, 1, 1)
    sprite('ka310_01', 2)	# 11-12
    Unknown1019(80)
    sprite('ka310_01', 2)	# 13-14
    Unknown1019(80)
    sprite('ka310_01', 2)	# 15-16
    Unknown1019(80)
    sprite('ka310_02', 3)	# 17-19
    sprite('ka310_03', 3)	# 20-22	 **attackbox here**
    Unknown1019(50)
    sprite('ka310_04', 6)	# 23-28
    Unknown1019(50)
    SFX_4('pka154')
    SFX_3('ka003')
    Unknown8010(100, 1, 1)
    sprite('ka310_05', 11)	# 29-39
    Unknown1019(0)
    sprite('ka310_06', 6)	# 40-45

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2017(0)
        Unknown2004(1, 0)
        AttackLevel_(5)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(30)
        Unknown9202(1)
        Unknown9310(1)
        AirPushbackX(20000)
        AirPushbackY(20000)
        YImpluseBeforeWallbounce(2200)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        JumpCancel_(0)
        Unknown21015('6b615f6973756f6b6973656d6500000000000000000000000000000000000000ce10000000000000')
    sprite('ka310_03', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('ka311_00', 4)	# 4-7	 **attackbox here**
    Unknown2005()
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    sprite('ka311_01', 4)	# 8-11	 **attackbox here**
    Unknown5001('0000000004000000040000000000000000000000')
    RefreshMultihit()
    SFX_4('pka153')
    sprite('ka311_02', 3)	# 12-14
    sprite('ka311_03', 3)	# 15-17
    sprite('ka311_04', 3)	# 18-20
    SFX_3('hit_h_fast')
    sprite('ka311_05', 3)	# 21-23
    sprite('ka311_06', 6)	# 24-29	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    AttackP2(50)
    Hitstop(13)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(80000)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(500)
    Unknown9178(1)
    WallbounceReboundTime(25)
    Unknown9346(0)
    AirUntechableTime(120)
    Unknown9310(12)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
    sprite('ka311_07', 7)	# 30-36
    Unknown2017(1)
    Unknown2016(200)
    sprite('ka311_08', 1)	# 37-37
    sprite('ka311_08', 6)	# 38-43
    sprite('ka311_09', 7)	# 44-50
    sprite('ka311_10', 7)	# 51-57
    sprite('ka311_11', 6)	# 58-63
    sprite('ka311_12', 6)	# 64-69

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(60)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(44)
        Unknown9021(1)
        Unknown9266(7)
        Unknown11084(1)
        Unknown11032('400d0300c0f2fcff90d0030000000000')

        def upon_52():
            Unknown36(26)
            Unknown48('16000000020000003300000019000000020000009e000000')
            Unknown35()
            if SLOT_51:
                if Unknown23036():
                    Unknown22031(14, 26)

        def upon_42():
            Unknown36(26)
            Unknown48('16000000020000003300000019000000020000009e000000')
            Unknown35()
            if SLOT_51:
                if Unknown23036():
                    Unknown23022(1)
                    Unknown23027()
                    GFX_0('KandenAtkObj', 100)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(42)
    sprite('ka400_00', 2)	# 1-2
    Unknown1084(0)
    setInvincible(1)
    GuardPoint_(1)
    GFX_1('kaef_spark_01', 0)
    GFX_1('kaef_spark_01', 1)
    GFX_1('kaef_spark_01', 2)
    sprite('ka400_01', 4)	# 3-6
    sprite('ka400_02', 2)	# 7-8
    Unknown7007('706b613230305f30000000000000000064000000706b613230305f31000000000000000064000000706b613230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ka400_03', 2)	# 9-10
    Unknown23029(11, 4000, 0)
    sprite('ka400_04', 2)	# 11-12
    sprite('ka400_05', 1)	# 13-13	 **attackbox here**
    sprite('ka400_06', 2)	# 14-15	 **attackbox here**
    GFX_0('taiden', 100)
    GFX_1('kaef_thunder_00', 100)
    GFX_1('kaef_spark_01', 0)
    GFX_1('kaef_spark_01', 1)
    GFX_1('kaef_spark_01', 2)
    SFX_3('electric_m')
    sprite('ka400_07', 2)	# 16-17	 **attackbox here**
    SFX_3('electric_m')
    sprite('ka400_06', 2)	# 18-19	 **attackbox here**
    GFX_1('kaef_thunder_00', 100)
    SFX_3('bomb_m')
    sprite('ka400_07', 2)	# 20-21	 **attackbox here**
    sprite('ka400_06', 3)	# 22-24	 **attackbox here**
    GFX_1('kaef_thunder_00', 100)
    GFX_1('kaef_spark_01', 0)
    GFX_1('kaef_spark_01', 1)
    GFX_1('kaef_spark_01', 2)
    SFX_3('electric_m')
    sprite('ka400_07', 3)	# 25-27	 **attackbox here**
    sprite('ka400_06', 4)	# 28-31	 **attackbox here**
    GFX_1('kaef_thunder_00', 100)
    GFX_1('kaef_spark_01', 0)
    GFX_1('kaef_spark_01', 1)
    GFX_1('kaef_spark_01', 2)
    SFX_3('electric_m')
    sprite('ka400_07', 4)	# 32-35	 **attackbox here**
    setInvincible(0)
    Unknown23027()
    sprite('ka400_06', 5)	# 36-40	 **attackbox here**
    SFX_3('electric_m')
    sprite('ka400_07', 5)	# 41-45	 **attackbox here**
    sprite('ka400_06', 5)	# 46-50	 **attackbox here**
    sprite('ka400_08', 5)	# 51-55
    sprite('ka400_09', 5)	# 56-60
    sprite('ka400_10', 5)	# 61-65

@State
def BusterAttackA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(7)
        Damage(1300)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(18000)
        AirPushbackY(-20000)
        AirHitstunAnimation(10)
        PushbackX(15000)
        Unknown9154(24)
        Unknown11028(23)
        Unknown9310(1)
        Unknown9202(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown1084(1)
        sendToLabelUpon(2, 1)
    sprite('ka401_00', 4)	# 1-4
    sprite('ka401_01', 2)	# 5-6
    sprite('ka401_02', 2)	# 7-8
    physicsXImpulse(22000)
    physicsYImpulse(20000)
    setGravity(4000)
    SFX_3('highjump_l')
    sprite('ka401_03', 2)	# 9-10
    sprite('ka401_04', 32767)	# 11-32777
    sendToLabelUpon(4, 0)
    loopRest()
    label(0)
    clearUponHandler(4)
    sprite('ka401_05', 2)	# 32778-32779
    Unknown7007('706b613230325f30000000000000000064000000706b613230335f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka401_06', 32767)	# 32780-65546	 **attackbox here**
    RefreshMultihit()
    loopRest()
    label(1)
    sprite('ka401_08', 6)	# 65547-65552	 **attackbox here**
    Unknown1084(1)
    ScreenShake(10000, 10000)
    RefreshMultihit()
    GroundedHitstunAnimation(0)
    Unknown11058('0000000001000000000000000000000000000000')
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    sprite('ka401_50', 6)	# 65553-65558
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    Recovery()
    sprite('ka401_09', 3)	# 65559-65561
    sprite('ka401_10', 3)	# 65562-65564
    sprite('ka401_11', 3)	# 65565-65567
    sprite('ka401_12', 3)	# 65568-65570
    sprite('ka401_12', 1)	# 65571-65571
    SLOT_64 = 1

@State
def BusterAttackB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(9)
        Damage(1500)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(-20000)
        PushbackX(15000)
        Unknown9310(1)
        Unknown9202(1)
        Unknown11058('0100000000000000000000000000000000000000')
        sendToLabelUpon(2, 1)

        def upon_14():
            SLOT_62 = 0
    sprite('ka401_00', 6)	# 1-6
    sprite('ka401_01', 3)	# 7-9
    sprite('ka401_02', 2)	# 10-11
    physicsXImpulse(16500)
    physicsYImpulse(50000)
    setGravity(5000)
    SLOT_62 = 1
    callSubroutine('Taete_Input')
    SFX_3('highjump_l')
    sprite('ka401_03', 2)	# 12-13
    sprite('ka401_04', 32767)	# 14-32780
    callSubroutine('Taete_Timing')
    sendToLabelUpon(4, 0)
    loopRest()
    label(0)
    clearUponHandler(4)
    sprite('ka401_05', 4)	# 32781-32784
    Unknown7007('706b613230325f31000000000000000064000000706b613230335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka401_06', 32767)	# 32785-65551	 **attackbox here**
    RefreshMultihit()
    callSubroutine('Taete_Clear')
    SLOT_62 = 0
    loopRest()
    label(1)
    sprite('ka401_08', 6)	# 65552-65557	 **attackbox here**
    Unknown1084(1)
    ScreenShake(20000, 20000)
    RefreshMultihit()
    AirUntechableTime(25)
    GroundedHitstunAnimation(1)
    Unknown11058('0000000001000000000000000000000000000000')
    AirPushbackY(-50000)
    setGravity(0)
    Unknown9190(1)
    Unknown9118(15)
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    sprite('ka401_50', 4)	# 65558-65561
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    Recovery()
    sprite('ka401_09', 1)	# 65562-65562
    sprite('ka401_10', 1)	# 65563-65563
    sprite('ka401_10', 1)	# 65564-65564
    SLOT_64 = 2

@State
def BusterAttackEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(9)
        Damage(1700)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(18000)
        AirPushbackY(-20000)
        AirHitstunAnimation(10)
        PushbackX(15000)
        Unknown9310(1)
        Unknown9202(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown30065(0)
        Unknown11091(10)

        def upon_14():
            SLOT_62 = 0
        sendToLabelUpon(2, 1)
    sprite('ka401_00', 3)	# 1-3
    sprite('ka401_00', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ka401_01', 3)	# 7-9
    sprite('ka401_02', 2)	# 10-11
    physicsXImpulse(35000)
    physicsYImpulse(30000)
    setGravity(3000)
    SLOT_62 = 1
    callSubroutine('Taete_Input')
    SFX_3('highjump_l')
    sprite('ka401_03', 2)	# 12-13
    sprite('ka401_04', 32767)	# 14-32780
    callSubroutine('Taete_Timing')
    sendToLabelUpon(4, 0)
    loopRest()
    label(0)
    clearUponHandler(4)
    sprite('ka401_05', 4)	# 32781-32784
    Unknown7007('706b613230325f32000000000000000064000000706b613230335f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka401_06', 32767)	# 32785-65551	 **attackbox here**
    RefreshMultihit()
    callSubroutine('Taete_Clear')
    SLOT_62 = 0
    loopRest()
    label(1)
    sprite('ka401_08', 6)	# 65552-65557	 **attackbox here**
    Unknown1084(1)
    ScreenShake(20000, 20000)
    RefreshMultihit()
    AirUntechableTime(25)
    GroundedHitstunAnimation(1)
    Unknown11058('0000000001000000000000000000000000000000')
    AirPushbackY(-50000)
    setGravity(0)
    Unknown9190(1)
    Unknown9118(15)
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    sprite('ka401_50', 4)	# 65558-65561
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    Recovery()
    sprite('ka401_09', 1)	# 65562-65562
    sprite('ka401_10', 1)	# 65563-65563
    sprite('ka401_10', 1)	# 65564-65564
    SLOT_64 = 2

@State
def AirBusterAttackA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(7)
        Damage(1300)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(8000)
        AirPushbackY(-25000)
        PushbackX(10000)
        Unknown11028(24)
        Unknown9310(1)
        Unknown9202(1)
        Unknown11058('0100000000000000000000000000000000000000')
        sendToLabelUpon(2, 1)
    sprite('ka401_02', 4)	# 1-4
    Unknown1084(1)
    physicsXImpulse(8800)
    physicsYImpulse(55000)
    setGravity(5000)
    SFX_3('highjump_l')
    sprite('ka401_03', 4)	# 5-8
    sprite('ka401_04', 5)	# 9-13
    sprite('ka401_04', 32767)	# 14-32780
    sendToLabelUpon(4, 0)
    loopRest()
    label(0)
    clearUponHandler(4)
    sprite('ka401_05', 2)	# 32781-32782
    Unknown7007('706b613230325f30000000000000000064000000706b613230335f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka401_06', 32767)	# 32783-65549	 **attackbox here**
    RefreshMultihit()
    loopRest()
    label(1)
    sprite('ka401_08', 6)	# 65550-65555	 **attackbox here**
    Unknown1084(1)
    ScreenShake(10000, 10000)
    RefreshMultihit()
    GroundedHitstunAnimation(1)
    Unknown11058('0000000001000000000000000000000000000000')
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    sprite('ka401_50', 4)	# 65556-65559
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    Recovery()
    sprite('ka401_09', 3)	# 65560-65562
    sprite('ka401_10', 3)	# 65563-65565
    sprite('ka401_11', 3)	# 65566-65568
    sprite('ka401_12', 3)	# 65569-65571
    sprite('ka401_12', 1)	# 65572-65572
    SLOT_64 = 1

@State
def AirBusterAttackB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(7)
        Damage(1500)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(16000)
        AirPushbackY(-30000)
        PushbackX(10000)
        Unknown9310(16)
        Unknown9202(1)
        Unknown11028(24)
        Unknown11058('0100000000000000000000000000000000000000')
        sendToLabelUpon(2, 1)
    sprite('ka401_02', 5)	# 1-5
    Unknown1084(1)
    physicsXImpulse(17600)
    physicsYImpulse(60000)
    setGravity(5000)
    SFX_3('highjump_l')
    sprite('ka401_03', 6)	# 6-11
    sprite('ka401_04', 7)	# 12-18
    sprite('ka401_04', 32767)	# 19-32785
    sendToLabelUpon(4, 0)
    loopRest()
    label(0)
    clearUponHandler(4)
    sprite('ka401_05', 4)	# 32786-32789
    Unknown7007('706b613230325f31000000000000000064000000706b613230335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka401_06', 32767)	# 32790-65556	 **attackbox here**
    RefreshMultihit()
    loopRest()
    label(1)
    sprite('ka401_08', 6)	# 65557-65562	 **attackbox here**
    Unknown1084(1)
    ScreenShake(20000, 20000)
    RefreshMultihit()
    AirUntechableTime(25)
    GroundedHitstunAnimation(1)
    Unknown11058('0000000001000000000000000000000000000000')
    AirPushbackY(-50000)
    setGravity(0)
    Unknown9190(1)
    Unknown9118(15)
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    sprite('ka401_50', 5)	# 65563-65567
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    Recovery()
    sprite('ka401_09', 2)	# 65568-65569
    sprite('ka401_10', 2)	# 65570-65571
    sprite('ka401_11', 1)	# 65572-65572
    sprite('ka401_12', 2)	# 65573-65574
    sprite('ka401_12', 1)	# 65575-65575
    SLOT_64 = 1

@State
def AirBusterAttackEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(7)
        Damage(1700)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(16000)
        AirPushbackY(-30000)
        PushbackX(10000)
        Unknown9310(16)
        Unknown9202(1)
        Unknown11028(24)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown30065(0)
        Unknown11091(10)
        sendToLabelUpon(2, 1)
    sprite('ka401_02', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(30000)
    physicsYImpulse(60000)
    setGravity(5000)
    SFX_3('highjump_l')
    sprite('ka401_02', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ka401_03', 6)	# 6-11
    sprite('ka401_04', 7)	# 12-18
    sprite('ka401_04', 32767)	# 19-32785
    sendToLabelUpon(4, 0)
    loopRest()
    label(0)
    clearUponHandler(4)
    sprite('ka401_05', 4)	# 32786-32789
    Unknown7007('706b613230325f32000000000000000064000000706b613230335f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka401_06', 32767)	# 32790-65556	 **attackbox here**
    RefreshMultihit()
    loopRest()
    label(1)
    sprite('ka401_08', 6)	# 65557-65562	 **attackbox here**
    Unknown1084(1)
    ScreenShake(20000, 20000)
    RefreshMultihit()
    AirUntechableTime(25)
    GroundedHitstunAnimation(1)
    Unknown11058('0000000001000000000000000000000000000000')
    AirPushbackY(-50000)
    setGravity(0)
    Unknown9190(1)
    Unknown9118(15)
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    sprite('ka401_50', 5)	# 65563-65567
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    Recovery()
    sprite('ka401_09', 2)	# 65568-65569
    sprite('ka401_10', 2)	# 65570-65571
    sprite('ka401_11', 1)	# 65572-65572
    sprite('ka401_12', 2)	# 65573-65574
    sprite('ka401_12', 1)	# 65575-65575
    SLOT_64 = 1

@State
def Oiuchi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(80)
        Hitstop(7)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(32)
        AirPushbackX(3000)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(0)
        Unknown9118(50)
        Unknown9190(1)
        Unknown11068(1)
        sendToLabelUpon(2, 1)
        Unknown30068(1)
        if (not Unknown23145('NmlAtk2C')):
            Unknown13045(0)
    sprite('ka401_00', 2)	# 1-2
    Unknown23087(80000)
    sprite('ka401_01', 6)	# 3-8
    sprite('ka401_02', 3)	# 9-11
    SLOT_67 = SLOT_19
    SLOT_12 = SLOT_67
    Unknown1019(6)
    physicsYImpulse(40000)
    setGravity(5500)
    SFX_3('highjump_l')
    sprite('ka401_03', 2)	# 12-13
    sprite('ka401_04', 32767)	# 14-32780
    sendToLabelUpon(4, 0)
    loopRest()
    label(0)
    clearUponHandler(4)
    sprite('ka401_05', 2)	# 32781-32782
    Unknown7007('706b613230345f30000000000000000064000000706b613230345f31000000000000000064000000706b613230345f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka401_06', 32767)	# 32783-65549	 **attackbox here**
    StartMultihit()
    loopRest()
    label(1)
    sprite('ka401_08', 6)	# 65550-65555	 **attackbox here**
    Unknown1084(1)
    ScreenShake(15000, 15000)
    RefreshMultihit()
    SFX_3('ka005')
    GFX_1('kaef_busterattack', 0)
    Unknown23054('6b613430315f303700000000000000000000000000000000000000000000000003000000')
    Unknown23087(-1)
    sprite('ka401_50', 5)	# 65556-65560
    GFX_0('IsuBreakParts1ex', 1)
    GFX_0('IsuBreakParts2ex', 1)
    GFX_0('IsuBreakParts3ex', 1)
    sprite('ka401_09', 4)	# 65561-65564
    sprite('ka401_10', 3)	# 65565-65567
    sprite('ka401_10', 1)	# 65568-65568
    SLOT_64 = 2

@State
def KushizashiA():

    def upon_IMMEDIATE():
        Unknown17011('Kushizashi_Exe', 2, 0, 0)
        Unknown11054(220000)
        Unknown11032('30570500000000000000000000000000')

        def upon_14():
            SLOT_59 = 0
    sprite('ka402_00', 3)	# 1-3
    sprite('ka402_04', 3)	# 4-6
    sprite('ka402_05', 1)	# 7-7	 **attackbox here**
    SLOT_59 = 1
    sprite('ka402_05', 3)	# 8-10	 **attackbox here**
    sprite('ka402_06', 3)	# 11-13
    SLOT_59 = 0
    sprite('ka402_07', 4)	# 14-17
    sprite('ka402_08', 8)	# 18-25
    Unknown7007('706b613230355f30000000000000000064000000706b613230355f31000000000000000064000000706b613230355f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka402_09', 4)	# 26-29
    sprite('ka402_10', 3)	# 30-32
    sprite('ka402_11', 3)	# 33-35
    sprite('ka402_12', 3)	# 36-38
    sprite('ka402_13', 3)	# 39-41

@State
def KushizashiEX():

    def upon_IMMEDIATE():
        Unknown17011('Kushizashi_Exe', 2, 0, 0)
        Unknown11054(220000)
        Unknown11032('30570500000000000000000000000000')

        def upon_14():
            SLOT_61 = 0
    sprite('ka402_00', 1)	# 1-1
    sprite('ka402_00', 1)	# 2-2
    sprite('ka402_01', 1)	# 3-3
    sprite('ka402_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ka402_02', 2)	# 5-6
    sprite('ka402_03', 2)	# 7-8
    sprite('ka402_04', 3)	# 9-11
    physicsXImpulse(15000)
    sprite('ka402_05', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    SLOT_61 = 1
    sprite('ka402_05', 3)	# 13-15	 **attackbox here**
    setInvincible(0)
    sprite('ka402_06', 3)	# 16-18
    Unknown1084(1)
    SLOT_61 = 0
    sprite('ka402_07', 4)	# 19-22
    sprite('ka402_08', 8)	# 23-30
    Unknown7007('706b613230355f30000000000000000064000000706b613230355f31000000000000000064000000706b613230355f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ka003')
    sprite('ka402_09', 4)	# 31-34
    sprite('ka402_10', 3)	# 35-37
    sprite('ka402_11', 3)	# 38-40
    sprite('ka402_12', 3)	# 41-43
    sprite('ka402_13', 3)	# 44-46

@State
def Kushizashi_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(5)
        Damage(500)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(500)
        Unknown9178(1)
        WallbounceReboundTime(3)
        Unknown9346(0)
        AirUntechableTime(120)
        Unknown9310(120)
        Unknown11064(1)
        Unknown2037(2)
        Unknown14083(0)
        Unknown2004(1, 0)
        Unknown23086(1)
        Unknown23027()

        def upon_43():
            if (SLOT_48 == 4022):
                sendToLabel(1)
        Unknown21015('6b615f6973756f6b6973656d6500000000000000000000000000000000000000ce10000000000000')
    sprite('ka402_05', 15)	# 1-15	 **attackbox here**
    Unknown11069('PKA_PersonaKushizashiA')
    if Unknown23145('KushizashiEX'):
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown11069('PKA_PersonaKushizashiEX')
        Unknown30065(0)
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    sprite('ka403_00', 3)	# 16-18
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka403_01', 3)	# 19-21
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka403_02', 10)	# 22-31
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka403_03', 3)	# 32-34
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown14070('Oiuchi')
    tag_voice(1, 'pka206_0', 'pka206_1', 'pka206_2', '')
    sprite('ka403_04', 3)	# 35-37
    Unknown5000(25, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ka403_05', 3)	# 38-40
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ka403_06', 3)	# 41-43	 **attackbox here**
    RefreshMultihit()
    sprite('ka403_07', 4)	# 44-47
    sprite('ka403_08', 6)	# 48-53
    sprite('ka403_09', 6)	# 54-59
    sprite('ka403_10', 6)	# 60-65
    sprite('ka403_08', 6)	# 66-71
    sprite('ka403_09', 6)	# 72-77
    sprite('ka403_10', 5)	# 78-82
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    if SLOT_59:
        Unknown23029(11, 4020, 0)
        SLOT_59 = 0
    if SLOT_61:
        Unknown23029(11, 4021, 0)
        SLOT_61 = 0
    sprite('ka403_10', 1)	# 83-83
    tag_voice(0, 'pka207_0', 'pka207_1', '', '')
    sprite('ka001_00', 7)	# 84-90
    sprite('ka001_01', 7)	# 91-97
    sprite('ka001_02', 7)	# 98-104
    label(0)
    sprite('ka001_03', 7)	# 105-111
    sprite('ka001_04', 7)	# 112-118
    SFX_3('ka000')
    sprite('ka001_05', 7)	# 119-125
    sprite('ka001_06', 7)	# 126-132
    sprite('ka001_07', 7)	# 133-139
    SFX_3('ka000')
    if SLOT_2:
        Unknown2038(-1)
        gotoLabel(0)
    loopRest()
    label(1)
    sprite('ka001_06', 7)	# 140-146
    Unknown2037(0)
    tag_voice(0, '', '', 'pka207_2', '')
    sprite('ka001_07', 7)	# 147-153
    SFX_3('ka000')
    sprite('ka001_03', 7)	# 154-160
    sprite('ka001_04', 7)	# 161-167
    SFX_3('ka000')
    sprite('ka001_05', 7)	# 168-174
    sprite('ka001_06', 4)	# 175-178
    sprite('ka001_06', 1)	# 179-179
    Unknown14083(1)
    sprite('ka001_06', 2)	# 180-181
    Unknown14072('Oiuchi')
    sprite('ka001_07', 6)	# 182-187
    SFX_3('ka000')
    Unknown14074('Oiuchi')
    sprite('ka001_08', 3)	# 188-190
    sprite('ka001_09', 3)	# 191-193
    sprite('ka001_10', 3)	# 194-196
    sprite('ka001_00', 2)	# 197-198

@State
def TsukameB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown14083(0)

        def upon_43():
            if (SLOT_48 == 4041):
                Unknown13045(0)
                sendToLabel(0)

        def upon_STATE_END():
            Unknown20007(0)
            setInvincible(0)
    sprite('ka404_00', 2)	# 1-2
    sprite('ka404_01', 3)	# 3-5
    sprite('ka404_02', 3)	# 6-8
    Unknown23029(11, 4040, 0)
    GFX_1('persona_enter_ply', 0)
    sprite('ka404_03', 2)	# 9-10
    sprite('ka404_04', 3)	# 11-13
    tag_voice(1, 'pka208_0', 'pka208_1', 'pka208_2', '')
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 14-16
    sprite('ka404_06', 3)	# 17-19
    sprite('ka404_04', 3)	# 20-22
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 23-25
    sprite('ka404_06', 3)	# 26-28
    sprite('ka404_04', 4)	# 29-32
    SFX_3('cloth_l')
    sprite('ka404_05', 5)	# 33-37
    sprite('ka404_06', 6)	# 38-43
    sprite('ka404_07', 6)	# 44-49
    loopRest()
    ExitState()
    label(0)
    sprite('ka404_04', 3)	# 50-52
    setInvincible(1)
    SFX_3('cloth_l')
    Unknown2006()
    sprite('ka404_05', 3)	# 53-55
    Unknown20007(1)
    sprite('ka404_06', 3)	# 56-58
    sprite('ka404_04', 3)	# 59-61
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 62-64
    sprite('ka404_06', 3)	# 65-67
    sprite('ka404_04', 3)	# 68-70
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 71-73
    sprite('ka404_06', 3)	# 74-76
    sprite('ka404_04', 3)	# 77-79
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 80-82
    sprite('ka404_06', 3)	# 83-85
    sprite('ka404_04', 3)	# 86-88
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 89-91
    sprite('ka404_06', 3)	# 92-94
    sprite('ka404_04', 3)	# 95-97
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 98-100
    sprite('ka404_06', 3)	# 101-103
    sprite('ka404_04', 3)	# 104-106
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 107-109
    sprite('ka404_06', 3)	# 110-112
    Unknown14070('Oiuchi')
    tag_voice(0, 'pka209_0', 'pka209_1', 'pka209_2', '')
    sprite('ka404_04', 3)	# 113-115
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 116-118
    sprite('ka404_06', 3)	# 119-121
    Unknown20007(0)
    sprite('ka404_04', 3)	# 122-124
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 125-127
    sprite('ka404_06', 3)	# 128-130
    sprite('ka404_04', 3)	# 131-133
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 134-136
    sprite('ka404_06', 3)	# 137-139
    sprite('ka404_04', 3)	# 140-142
    SFX_3('cloth_l')
    sprite('ka404_05', 2)	# 143-144
    sprite('ka404_05', 1)	# 145-145
    Unknown14083(1)
    sprite('ka404_06', 3)	# 146-148
    Unknown14072('Oiuchi')
    sprite('ka404_04', 3)	# 149-151
    SFX_3('cloth_l')
    sprite('ka404_05', 3)	# 152-154
    Unknown14074('Oiuchi')
    sprite('ka404_06', 3)	# 155-157
    sprite('ka404_04', 5)	# 158-162
    SFX_3('cloth_l')
    sprite('ka404_05', 5)	# 163-167
    sprite('ka404_06', 6)	# 168-173
    sprite('ka404_07', 6)	# 174-179

@State
def TaetemiyagareA():

    def upon_IMMEDIATE():
        Unknown17011('TaetemiyagareA_Exe', 2, 1, 0)
        AttackLevel_(5)
        Unknown11046(0)
        Unknown11061(1)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11032('e093040000000000400d0300c0f2fcff')
        Unknown23027()
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    if SLOT_62:
        _gotolabel(3)
    sprite('ka406_00', 6)	# 1-6
    Unknown1019(15)
    YAccel(15)
    setGravity(0)
    sprite('ka406_00', 3)	# 7-9
    tag_voice(1, 'pka210_0', 'pka210_1', 'pka210_2', '')
    SFX_3('airdash_m')
    physicsXImpulse(10000)
    physicsYImpulse(40000)
    setGravity(3500)
    sendToLabelUpon(4, 0)
    sprite('ka406_01', 3)	# 10-12	 **attackbox here**
    GFX_0('406isumove', 100)
    label(2)
    sprite('ka406_02', 3)	# 13-15	 **attackbox here**
    sprite('ka406_01', 3)	# 16-18	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(0)
    clearUponHandler(4)
    sprite('ka406_01', 3)	# 19-21	 **attackbox here**
    sprite('ka406_02', 3)	# 22-24	 **attackbox here**
    sprite('ka406_01', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    SLOT_5 = SLOT_12
    sprite('ka406_02', 3)	# 28-30	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka406_03', 3)	# 31-33
    Unknown1084(1)
    SFX_3('bound_stone_m')
    SLOT_62 = 0
    sprite('ka406_04', 3)	# 34-36
    sprite('ka406_05', 5)	# 37-41
    sprite('ka406_06', 5)	# 42-46
    sprite('ka401_09', 2)	# 47-48
    sprite('ka401_10', 1)	# 49-49
    sprite('ka401_10', 1)	# 50-50
    tag_voice(0, 'pka211_0', 'pka211_1', 'pka211_2', '')
    SLOT_64 = 2
    ExitState()
    label(3)
    clearUponHandler(4)
    SLOT_62 = 0
    sprite('ka406_01', 4)	# 51-54	 **attackbox here**
    GFX_0('406isumove', 100)
    tag_voice(1, 'pka210_0', 'pka210_1', 'pka210_2', '')
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('ka406_02', 3)	# 55-57	 **attackbox here**
    sprite('ka406_01', 3)	# 58-60	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(40)
    Unknown1039(80)
    RefreshMultihit()
    label(4)
    sprite('ka406_02', 3)	# 61-63	 **attackbox here**
    SLOT_5 = SLOT_12
    sprite('ka406_01', 3)	# 64-66	 **attackbox here**
    loopRest()
    gotoLabel(4)

@State
def TaetemiyagareA_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(400)
        AttackP2(100)
        Unknown11091(5)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(30000)
        AirUntechableTime(80)
        Unknown9310(1)
        Unknown11064(1)
        Hitstop(0)
        Unknown2004(1, 0)
        sendToLabelUpon(2, 1)
        SLOT_62 = 0
        Unknown14083(0)
    sprite('ka407_00', 9)	# 1-9
    SFX_3('grip_middle')
    Unknown5000(4, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SLOT_12 = SLOT_5
    Unknown1084(1)
    ScreenShake(7000, 10000)
    sprite('ka407_00', 5)	# 10-14
    setGravity(100)
    physicsXImpulse(28000)
    physicsYImpulse(-50000)
    label(0)
    sprite('ka407_01', 5)	# 15-19
    sprite('ka407_00', 5)	# 20-24
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka407_00', 4)	# 25-28
    Unknown5000(15, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1084(1)
    Unknown1047(30000)
    SFX_3('damage_hit_mh')
    SFX_3('bound_stone_m')
    ScreenShake(7000, 25000)
    sprite('ka407_01', 4)	# 29-32
    ScreenShake(7000, 15000)
    sprite('ka407_00', 4)	# 33-36
    ScreenShake(7000, 15000)
    sprite('ka407_02', 4)	# 37-40
    Unknown5000(15, 0)
    Unknown5001('0100000000000000000000000000000000000000')
    sprite('ka407_08', 4)	# 41-44
    sprite('ka407_11', 4)	# 45-48
    sprite('ka407_03', 10)	# 49-58
    sprite('ka407_04', 8)	# 59-66
    tag_voice(1, 'pka213_0', 'pka213_1', 'pka213_2', '')
    sprite('ka407_05', 1)	# 67-67
    sprite('ka407_05', 1)	# 68-68
    GFX_0('kaef407_atk1', 100)
    sprite('ka407_06', 8)	# 69-76	 **attackbox here**
    GFX_1('kaef_407atk1', 1)
    RefreshMultihit()
    Unknown30079(1)
    ScreenShake(20000, 10000)
    sprite('ka407_07', 3)	# 77-79
    sprite('ka407_08', 2)	# 80-81
    GFX_0('kaef407_atk2', 100)
    sprite('ka407_09', 8)	# 82-89	 **attackbox here**
    GFX_1('kaef_407atk2', 1)
    RefreshMultihit()
    ScreenShake(20000, 10000)
    sprite('ka407_10', 5)	# 90-94
    sprite('ka407_11', 5)	# 95-99
    sprite('ka407_12', 5)	# 100-104
    sprite('ka407_13', 5)	# 105-109
    sprite('ka407_14', 6)	# 110-115
    sprite('ka407_15', 10)	# 116-125
    sprite('ka407_16', 5)	# 126-130	 **attackbox here**
    GFX_0('kaef407_atk3', 100)
    GFX_1('kaef_407atk3', 0)
    tag_voice(0, 'pka214_0', 'pka214_1', 'pka214_2', '')
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1600)
    AttackP2(50)
    Hitstop(13)
    Unknown11064(0)
    ScreenShake(20000, 20000)
    Unknown30079(0)
    Unknown14070('Oiuchi')
    Unknown14083(1)
    Unknown11072(1, 100000, 0)
    sprite('ka407_17', 5)	# 131-135
    sprite('ka406_06', 5)	# 136-140
    sprite('ka401_09', 7)	# 141-147
    sprite('ka401_10', 7)	# 148-154
    Unknown14072('Oiuchi')
    sprite('ka401_11', 5)	# 155-159
    sprite('ka401_12', 6)	# 160-165
    sprite('ka401_13', 6)	# 166-171
    sprite('ka401_14', 4)	# 172-175
    Unknown14074('Oiuchi')
    SFX_3('ka003')
    sprite('ka401_15', 3)	# 176-178
    sprite('ka401_16', 3)	# 179-181

@State
def TaetemiyagareB():

    def upon_IMMEDIATE():
        Unknown17011('TaetemiyagareB_Exe', 2, 1, 0)
        AttackLevel_(5)
        Unknown11046(0)
        Unknown11061(1)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11032('e093040000000000400d0300c0f2fcff')
        Unknown23027()
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    if SLOT_62:
        _gotolabel(3)
    sprite('ka406_00', 7)	# 1-7
    Unknown1019(15)
    YAccel(15)
    setGravity(0)
    sprite('ka406_00', 3)	# 8-10
    SFX_3('airdash_m')
    tag_voice(1, 'pka210_0', 'pka210_1', 'pka210_2', '')
    physicsXImpulse(25000)
    physicsYImpulse(40000)
    setGravity(3500)
    sendToLabelUpon(4, 0)
    sprite('ka406_01', 3)	# 11-13	 **attackbox here**
    GFX_0('406isumove', 100)
    label(2)
    sprite('ka406_02', 3)	# 14-16	 **attackbox here**
    sprite('ka406_01', 3)	# 17-19	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(0)
    clearUponHandler(4)
    sprite('ka406_01', 3)	# 20-22	 **attackbox here**
    sprite('ka406_02', 3)	# 23-25	 **attackbox here**
    sprite('ka406_01', 1)	# 26-26	 **attackbox here**
    RefreshMultihit()
    SLOT_5 = SLOT_12
    sprite('ka406_01', 2)	# 27-28	 **attackbox here**
    sprite('ka406_02', 3)	# 29-31	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka406_03', 3)	# 32-34
    Unknown1084(1)
    SFX_3('bound_stone_m')
    SLOT_62 = 0
    sprite('ka406_04', 3)	# 35-37
    sprite('ka406_05', 5)	# 38-42
    sprite('ka406_06', 5)	# 43-47
    sprite('ka401_09', 2)	# 48-49
    sprite('ka401_10', 1)	# 50-50
    sprite('ka401_10', 1)	# 51-51
    tag_voice(0, 'pka211_0', 'pka211_1', 'pka211_2', '')
    SLOT_64 = 2
    ExitState()
    label(3)
    clearUponHandler(4)
    SLOT_62 = 0
    sprite('ka406_01', 4)	# 52-55	 **attackbox here**
    GFX_0('406isumove', 100)
    tag_voice(1, 'pka210_0', 'pka210_1', 'pka210_2', '')
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('ka406_02', 3)	# 56-58	 **attackbox here**
    sprite('ka406_01', 3)	# 59-61	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(80)
    Unknown1039(80)
    RefreshMultihit()
    label(4)
    sprite('ka406_02', 3)	# 62-64	 **attackbox here**
    SLOT_5 = SLOT_12
    sprite('ka406_01', 3)	# 65-67	 **attackbox here**
    loopRest()
    gotoLabel(4)

@State
def TaetemiyagareB_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(400)
        AttackP2(100)
        Unknown11091(5)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(30000)
        AirUntechableTime(80)
        Unknown9310(1)
        Unknown11064(1)
        Hitstop(0)
        Unknown2004(1, 0)
        sendToLabelUpon(2, 1)
        SLOT_62 = 0
        Unknown14083(0)
    sprite('ka407_00', 9)	# 1-9
    SFX_3('grip_middle')
    Unknown5000(4, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SLOT_12 = SLOT_5
    Unknown1084(1)
    ScreenShake(7000, 10000)
    sprite('ka407_00', 5)	# 10-14
    setGravity(100)
    physicsXImpulse(32000)
    physicsYImpulse(-50000)
    label(0)
    sprite('ka407_01', 5)	# 15-19
    sprite('ka407_00', 5)	# 20-24
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka407_00', 4)	# 25-28
    Unknown5000(15, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1084(1)
    Unknown1047(36000)
    SFX_3('damage_hit_mh')
    SFX_3('bound_stone_m')
    ScreenShake(7000, 25000)
    sprite('ka407_01', 4)	# 29-32
    ScreenShake(7000, 15000)
    sprite('ka407_00', 4)	# 33-36
    ScreenShake(7000, 15000)
    sprite('ka407_02', 4)	# 37-40
    Unknown5000(15, 0)
    Unknown5001('0100000000000000000000000000000000000000')
    sprite('ka407_08', 4)	# 41-44
    sprite('ka407_11', 4)	# 45-48
    sprite('ka407_03', 10)	# 49-58
    sprite('ka407_04', 8)	# 59-66
    tag_voice(1, 'pka213_0', 'pka213_1', 'pka213_2', '')
    sprite('ka407_05', 1)	# 67-67
    sprite('ka407_05', 1)	# 68-68
    GFX_0('kaef407_atk1', 100)
    sprite('ka407_06', 8)	# 69-76	 **attackbox here**
    GFX_1('kaef_407atk1', 1)
    RefreshMultihit()
    Unknown30079(1)
    ScreenShake(20000, 10000)
    sprite('ka407_07', 3)	# 77-79
    sprite('ka407_08', 2)	# 80-81
    GFX_0('kaef407_atk2', 100)
    sprite('ka407_09', 8)	# 82-89	 **attackbox here**
    GFX_1('kaef_407atk2', 1)
    RefreshMultihit()
    ScreenShake(20000, 10000)
    sprite('ka407_10', 5)	# 90-94
    sprite('ka407_08', 2)	# 95-96
    sprite('ka407_05', 1)	# 97-97
    GFX_0('kaef407_atk1', 100)
    sprite('ka407_06', 8)	# 98-105	 **attackbox here**
    GFX_1('kaef_407atk1', 1)
    RefreshMultihit()
    ScreenShake(20000, 10000)
    sprite('ka407_07', 3)	# 106-108
    sprite('ka407_08', 2)	# 109-110
    GFX_0('kaef407_atk2', 100)
    sprite('ka407_09', 8)	# 111-118	 **attackbox here**
    GFX_1('kaef_407atk2', 1)
    RefreshMultihit()
    ScreenShake(20000, 10000)
    sprite('ka407_10', 5)	# 119-123
    sprite('ka407_11', 5)	# 124-128
    sprite('ka407_12', 5)	# 129-133
    sprite('ka407_13', 5)	# 134-138
    sprite('ka407_14', 6)	# 139-144
    sprite('ka407_15', 10)	# 145-154
    sprite('ka407_16', 5)	# 155-159	 **attackbox here**
    GFX_0('kaef407_atk3', 100)
    GFX_1('kaef_407atk3', 0)
    tag_voice(0, 'pka214_0', 'pka214_1', 'pka214_2', '')
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1600)
    AttackP2(50)
    Hitstop(13)
    Unknown11064(0)
    ScreenShake(20000, 20000)
    Unknown30079(0)
    Unknown14070('Oiuchi')
    Unknown14083(1)
    Unknown11072(1, 100000, 0)
    sprite('ka407_17', 5)	# 160-164
    sprite('ka406_06', 5)	# 165-169
    sprite('ka401_09', 7)	# 170-176
    sprite('ka401_10', 7)	# 177-183
    Unknown14072('Oiuchi')
    sprite('ka401_11', 5)	# 184-188
    sprite('ka401_12', 6)	# 189-194
    sprite('ka401_13', 6)	# 195-200
    sprite('ka401_14', 4)	# 201-204
    Unknown14074('Oiuchi')
    SFX_3('ka003')
    sprite('ka401_15', 3)	# 205-207
    sprite('ka401_16', 3)	# 208-210

@State
def TaetemiyagareEX():

    def upon_IMMEDIATE():
        Unknown17011('TaetemiyagareEX_Exe', 2, 1, 0)
        AttackLevel_(5)
        Unknown11046(0)
        Unknown11061(1)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11032('e093040000000000400d0300c0f2fcff')
        Unknown23027()
        Unknown11091(10)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    if SLOT_62:
        _gotolabel(3)
    sprite('ka406_00', 3)	# 1-3
    Unknown1019(15)
    YAccel(15)
    setGravity(0)
    sprite('ka406_00', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ka406_00', 2)	# 6-7
    SFX_3('airdash_m')
    tag_voice(1, 'pka210_0', 'pka210_1', 'pka210_2', '')
    SLOT_12 = SLOT_19
    Unknown1019(5)

    def upon_3():
        if (SLOT_12 <= 1000):
            SLOT_12 = 1000
    physicsYImpulse(25000)
    setGravity(2200)
    sendToLabelUpon(4, 0)
    sprite('ka406_01', 1)	# 8-8	 **attackbox here**
    GFX_0('406isumove', 100)
    label(2)
    sprite('ka406_01', 3)	# 9-11	 **attackbox here**
    Unknown1019(60)
    SLOT_5 = SLOT_12
    sprite('ka406_02', 3)	# 12-14	 **attackbox here**
    SLOT_12 = SLOT_19
    Unknown1019(5)
    loopRest()
    gotoLabel(2)
    label(0)
    clearUponHandler(4)
    sprite('ka406_01', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    SLOT_5 = SLOT_12
    setGravity(2500)
    sprite('ka406_02', 3)	# 18-20	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka406_03', 3)	# 21-23
    clearUponHandler(3)
    Unknown1084(1)
    SFX_3('bound_stone_m')
    SLOT_62 = 0
    sprite('ka406_04', 3)	# 24-26
    sprite('ka406_05', 5)	# 27-31
    sprite('ka406_06', 5)	# 32-36
    sprite('ka401_09', 2)	# 37-38
    sprite('ka401_10', 1)	# 39-39
    sprite('ka401_10', 1)	# 40-40
    tag_voice(0, 'pka211_0', 'pka211_1', 'pka211_2', '')
    SLOT_64 = 2
    ExitState()
    label(3)
    clearUponHandler(4)
    SLOT_62 = 0
    sprite('ka406_01', 1)	# 41-41	 **attackbox here**
    Unknown1084(1)
    sprite('ka406_01', 3)	# 42-44	 **attackbox here**
    GFX_0('406isumove', 100)
    tag_voice(1, 'pka210_0', 'pka210_1', 'pka210_2', '')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ka406_02', 3)	# 45-47	 **attackbox here**
    sprite('ka406_01', 3)	# 48-50	 **attackbox here**
    SLOT_12 = SLOT_19
    Unknown1019(4)

    def upon_3():
        if (SLOT_12 <= 1000):
            SLOT_12 = 1000
    physicsYImpulse(25000)
    setGravity(5000)
    RefreshMultihit()
    label(4)
    sprite('ka406_02', 3)	# 51-53	 **attackbox here**
    SLOT_5 = SLOT_12
    Unknown1039(90)
    sprite('ka406_01', 3)	# 54-56	 **attackbox here**
    loopRest()
    gotoLabel(4)

@State
def TaetemiyagareEX_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(500)
        AttackP2(50)
        Hitstop(5)
        Unknown11092(1)
        Unknown11091(0)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(30000)
        AirUntechableTime(80)
        Unknown9310(20)
        Unknown11064(1)
        Hitstop(0)
        Unknown2004(1, 0)
        Unknown30065(0)
        Unknown11091(10)
        callSubroutine('Eff_ExSkill_AfterImage')
        sendToLabelUpon(2, 1)
        SLOT_62 = 0
        Unknown14083(0)
    sprite('ka407_00', 9)	# 1-9
    SFX_3('grip_middle')
    Unknown5000(4, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SLOT_12 = SLOT_5
    Unknown1084(1)
    ScreenShake(7000, 10000)
    sprite('ka407_00', 5)	# 10-14
    setGravity(100)
    physicsXImpulse(32000)
    physicsYImpulse(-50000)
    label(0)
    sprite('ka407_01', 5)	# 15-19
    sprite('ka407_00', 5)	# 20-24
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ka407_00', 4)	# 25-28
    Unknown5000(15, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1084(1)
    Unknown1047(36000)
    SFX_3('damage_hit_mh')
    SFX_3('bound_stone_m')
    ScreenShake(7000, 25000)
    sprite('ka407_01', 4)	# 29-32
    ScreenShake(7000, 15000)
    sprite('ka407_00', 4)	# 33-36
    ScreenShake(7000, 15000)
    sprite('ka407_02', 4)	# 37-40
    Unknown5000(15, 0)
    Unknown5001('0100000000000000000000000000000000000000')
    sprite('ka407_08', 4)	# 41-44
    sprite('ka407_11', 4)	# 45-48
    sprite('ka407_12', 8)	# 49-56
    sprite('ka407_13', 8)	# 57-64
    sprite('ka407_14', 9)	# 65-73
    Unknown7007('706b613231325f30000000000000000064000000706b613231325f31000000000000000064000000706b613231325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ka407_15', 18)	# 74-91
    sprite('ka407_16', 13)	# 92-104	 **attackbox here**
    GFX_0('kaef407_atk3', 100)
    GFX_1('kaef_407atk3', 0)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(3600)
    Hitstop(13)
    Unknown11064(0)
    ScreenShake(20000, 20000)
    Unknown30079(0)
    Unknown14070('Oiuchi')
    Unknown14083(1)
    Unknown11072(1, 100000, 0)
    sprite('ka407_17', 5)	# 105-109
    sprite('ka406_06', 5)	# 110-114
    sprite('ka401_09', 7)	# 115-121
    Unknown14072('Oiuchi')
    sprite('ka401_10', 7)	# 122-128
    sprite('ka401_11', 5)	# 129-133
    sprite('ka401_12', 6)	# 134-139
    sprite('ka401_13', 6)	# 140-145
    sprite('ka401_14', 4)	# 146-149
    Unknown14074('Oiuchi')
    SFX_3('ka003')
    sprite('ka401_15', 3)	# 150-152
    sprite('ka401_16', 3)	# 153-155

@State
def KenkaSappou():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1500)
        Unknown11091(25)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(80)
        Unknown9142(80)
        AirPushbackY(26000)
        YImpluseBeforeWallbounce(1000)
        Hitstop(25)
        Unknown11032('305705000000000000000000400d0300')
        Unknown9154(41)
        AirUntechableTime(81)
        Unknown30055('a08601003200000000000000')
        Unknown11068(1)
        Unknown11064(1)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1

        def upon_78():
            clearUponHandler(78)
            Unknown21015('6b615f6973756f6b6973656d6500000000000000000000000000000000000000ce10000000000000')
            ScreenShake(40000, 0)
            Unknown11069('KenkaSappou')
            Unknown2017(0)
            Unknown13024(0)
            sendToLabel(0)
    sprite('ka430_00', 3)	# 1-3
    setInvincible(1)
    tag_voice(1, 'pka250_0', 'pka250_1', '', '')
    sprite('ka430_01', 4)	# 4-7
    Unknown2036(59, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('ka430_02', 5)	# 8-12
    sprite('ka430_03', 5)	# 13-17
    sprite('ka430_01', 5)	# 18-22
    sprite('ka430_02', 5)	# 23-27
    sprite('ka430_03', 5)	# 28-32
    sprite('ka430_01', 4)	# 33-36
    sprite('ka430_02', 4)	# 37-40
    sprite('ka430_03', 4)	# 41-44
    sprite('ka430_01', 4)	# 45-48
    sprite('ka430_02', 4)	# 49-52
    sprite('ka430_03', 4)	# 53-56
    sprite('ka430_04', 3)	# 57-59
    sprite('ka430_05', 3)	# 60-62
    sprite('ka430_06', 3)	# 63-65
    GFX_1('kaef_chairthrow_smoke', 100)
    sprite('ka430_07', 3)	# 66-68
    GFX_0('kaef430_atkline1', 100)
    SFX_3('slash_blade_slow')
    sprite('ka430_08', 3)	# 69-71	 **attackbox here**
    GFX_0('kaef430_atk1', 100)
    tag_voice(0, 'pka251_0', 'pka251_1', '', '')
    RefreshMultihit()
    sprite('ka430_09', 3)	# 72-74
    if SLOT_51:
        GFX_0('ka_isuyamanari', 0)
        Unknown23029(1, 4303, 0)
    else:
        GFX_0('ka_isuyoko', 0)
        Unknown23029(1, 4303, 0)
    setInvincible(0)
    sprite('ka430_10', 3)	# 75-77
    sprite('ka430_11', 3)	# 78-80
    sprite('ka430_12', 3)	# 81-83
    sprite('ka430_13', 4)	# 84-87
    sprite('ka430_14', 4)	# 88-91
    sprite('ka430_15', 4)	# 92-95
    sprite('ka401_11', 4)	# 96-99
    sprite('ka401_12', 4)	# 100-103
    sprite('ka401_13', 6)	# 104-109
    sprite('ka401_14', 4)	# 110-113
    sprite('ka401_15', 3)	# 114-116
    sprite('ka401_16', 3)	# 117-119
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(78)
    sprite('ka430_09', 3)	# 120-122
    GFX_0('ka_isuokiseme', 0)
    Unknown23029(1, 4303, 0)
    sprite('ka430_10', 3)	# 123-125
    sprite('ka430_11', 3)	# 126-128
    sprite('ka430_10', 3)	# 129-131
    sprite('ka430_11', 3)	# 132-134
    sprite('ka430_16', 4)	# 135-138
    sprite('ka430_17', 5)	# 139-143
    sprite('ka430_18', 5)	# 144-148
    physicsXImpulse(26000)
    physicsYImpulse(15000)
    setGravity(2200)
    SFX_3('highjump_l')
    sprite('ka430_19', 5)	# 149-153
    tag_voice(0, 'pka252_0', 'pka252_1', '', '')
    SFX_3('hit_h_middle')
    sprite('ka430_20', 3)	# 154-156	 **attackbox here**
    GFX_1('kaef_430atk2', 0)
    Unknown1019(80)
    YAccel(80)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2000)
    AirUntechableTime(51)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(0)
    AirPushbackX(12000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(1500)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Hitstop(30)
    PushbackX(70000)
    Unknown30048(1)

    def upon_78():
        ScreenShake(50000, 0)
        clearUponHandler(78)
    sprite('ka430_22', 2)	# 157-158
    sprite('ka430_23', 32767)	# 159-32925
    sendToLabelUpon(2, 2)
    loopRest()
    label(2)
    sprite('ka430_24', 3)	# 32926-32928
    Unknown1084(1)
    sprite('ka430_25', 4)	# 32929-32932
    sprite('ka430_26', 4)	# 32933-32936
    sprite('ka430_27', 8)	# 32937-32944
    SFX_3('highjump_m')
    physicsXImpulse(31000)
    physicsYImpulse(32000)
    setGravity(3000)
    sprite('ka430_28', 7)	# 32945-32951
    Unknown1019(80)
    tag_voice(0, 'pka253_0', 'pka253_1', '', '')
    sprite('ka430_29', 2)	# 32952-32953
    GFX_0('kaef430_atkline3', 100)
    SFX_3('hit_h_slow')
    Unknown1019(80)
    sprite('ka430_31', 5)	# 32954-32958	 **attackbox here**
    Unknown23054('6b613433305f333000000000000000000000000000000000000000000000000004000000')
    GFX_0('kaef430_atk3', 100)
    Unknown1019(80)
    RefreshMultihit()
    Damage(3000)
    Hitstop(30)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(10000)
    AirPushbackY(-100000)
    YImpluseBeforeWallbounce(4500)
    Unknown9190(1)
    Unknown11073(1)
    Unknown11064(0)
    Unknown11069('ka_isuokiseme')

    def upon_78():
        SFX_3('quake_s')
        SFX_3('blaze_normal')
        SFX_3('bound_steal_m')
        ScreenShake(80000, 0)
        clearUponHandler(78)
    sprite('ka430_31', 32767)	# 32959-65725	 **attackbox here**
    sendToLabelUpon(2, 4)
    loopRest()
    label(4)
    sprite('ka430_32', 3)	# 65726-65728
    Unknown20000(1)
    Unknown1019(30)
    YAccel(30)
    ScreenShake(0, 20000)
    sprite('ka430_33', 3)	# 65729-65731
    Unknown1019(0)
    YAccel(0)
    sprite('ka430_32', 3)	# 65732-65734
    sprite('ka430_33', 3)	# 65735-65737
    sprite('ka430_32', 3)	# 65738-65740
    sprite('ka430_33', 3)	# 65741-65743
    sprite('ka430_32', 3)	# 65744-65746
    sprite('ka430_33', 3)	# 65747-65749
    sprite('ka430_32', 3)	# 65750-65752
    sprite('ka430_33', 3)	# 65753-65755
    sprite('ka430_32', 3)	# 65756-65758
    sprite('ka430_32', 2)	# 65759-65760
    sprite('ka430_34', 4)	# 65761-65764
    sprite('ka430_35', 3)	# 65765-65767
    Unknown13024(1)
    sprite('ka401_11', 3)	# 65768-65770
    setInvincible(0)
    Unknown2017(1)
    sprite('ka401_12', 4)	# 65771-65774
    sprite('ka401_13', 6)	# 65775-65780
    sprite('ka401_14', 4)	# 65781-65784
    sprite('ka401_15', 3)	# 65785-65787
    sprite('ka401_16', 3)	# 65788-65790
    loopRest()

@State
def KenkaSappou_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1500)
        Unknown11091(25)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(80)
        Unknown9142(80)
        AirPushbackY(26000)
        YImpluseBeforeWallbounce(1000)
        Hitstop(25)
        Unknown11032('305705000000000000000000400d0300')
        Unknown9154(41)
        AirUntechableTime(81)
        Unknown30055('a08601003200000000000000')
        Unknown11068(1)
        Unknown11064(1)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1

        def upon_78():
            clearUponHandler(78)
            Unknown21015('6b615f6973756f6b6973656d6500000000000000000000000000000000000000ce10000000000000')
            Unknown11069('KenkaSappou_OD')
            ScreenShake(40000, 0)
            Unknown13024(0)
            Unknown2017(0)
            sendToLabel(0)
    sprite('ka430_00', 3)	# 1-3
    setInvincible(1)
    tag_voice(1, 'pka250_0', 'pka250_1', '', '')
    sprite('ka430_01', 4)	# 4-7
    Unknown2036(59, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('ka430_02', 5)	# 8-12
    sprite('ka430_03', 5)	# 13-17
    sprite('ka430_01', 5)	# 18-22
    sprite('ka430_02', 5)	# 23-27
    sprite('ka430_03', 5)	# 28-32
    sprite('ka430_01', 4)	# 33-36
    sprite('ka430_02', 4)	# 37-40
    sprite('ka430_03', 4)	# 41-44
    sprite('ka430_01', 4)	# 45-48
    sprite('ka430_02', 4)	# 49-52
    sprite('ka430_03', 4)	# 53-56
    sprite('ka430_04', 3)	# 57-59
    sprite('ka430_05', 3)	# 60-62
    sprite('ka430_06', 3)	# 63-65
    GFX_1('kaef_chairthrow_smoke', 100)
    sprite('ka430_07', 3)	# 66-68
    GFX_0('kaef430_atkline1', 100)
    SFX_3('slash_blade_slow')
    sprite('ka430_08', 3)	# 69-71	 **attackbox here**
    GFX_0('kaef430_atk1', 100)
    tag_voice(0, 'pka251_0', 'pka251_1', '', '')
    RefreshMultihit()
    sprite('ka430_09', 3)	# 72-74
    if SLOT_51:
        GFX_0('ka_isuyamanari', 0)
        Unknown23029(1, 4304, 0)
    else:
        GFX_0('ka_isuyoko', 0)
        Unknown23029(1, 4303, 0)
    setInvincible(0)
    sprite('ka430_10', 3)	# 75-77
    sprite('ka430_11', 3)	# 78-80
    sprite('ka430_12', 3)	# 81-83
    sprite('ka430_13', 4)	# 84-87
    sprite('ka430_14', 4)	# 88-91
    sprite('ka430_15', 4)	# 92-95
    sprite('ka401_11', 4)	# 96-99
    sprite('ka401_12', 4)	# 100-103
    sprite('ka401_13', 6)	# 104-109
    sprite('ka401_14', 4)	# 110-113
    sprite('ka401_15', 3)	# 114-116
    sprite('ka401_16', 3)	# 117-119
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(78)
    sprite('ka430_09', 3)	# 120-122
    GFX_0('ka_isuokiseme', 0)
    Unknown23029(1, 4305, 0)
    sprite('ka430_10', 3)	# 123-125
    sprite('ka430_11', 3)	# 126-128
    sprite('ka430_10', 3)	# 129-131
    sprite('ka430_11', 3)	# 132-134
    sprite('ka430_16', 4)	# 135-138
    sprite('ka430_17', 5)	# 139-143
    sprite('ka430_18', 5)	# 144-148
    physicsXImpulse(26000)
    physicsYImpulse(15000)
    setGravity(2200)
    SFX_3('highjump_l')
    sprite('ka430_19', 5)	# 149-153
    tag_voice(0, 'pka252_0', 'pka252_1', '', '')
    SFX_3('hit_h_middle')
    sprite('ka430_20', 3)	# 154-156	 **attackbox here**
    GFX_1('kaef_430atk2', 0)
    Unknown1019(80)
    YAccel(80)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2000)
    AirUntechableTime(51)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(0)
    AirPushbackX(12000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(1500)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Hitstop(30)
    PushbackX(70000)
    Unknown30048(1)

    def upon_78():
        ScreenShake(50000, 0)
        clearUponHandler(78)
    sprite('ka430_22', 2)	# 157-158
    sprite('ka430_23', 32767)	# 159-32925
    sendToLabelUpon(2, 2)
    loopRest()
    label(2)
    sprite('ka430_24', 3)	# 32926-32928
    Unknown1084(1)
    sprite('ka430_25', 4)	# 32929-32932
    sprite('ka430_26', 4)	# 32933-32936
    sprite('ka430_27', 8)	# 32937-32944
    SFX_3('highjump_m')
    physicsXImpulse(31000)
    physicsYImpulse(32000)
    setGravity(3000)
    sprite('ka430_28', 7)	# 32945-32951
    Unknown1019(80)
    tag_voice(0, 'pka253_0', 'pka253_1', '', '')
    sprite('ka430_29', 2)	# 32952-32953
    GFX_0('kaef430_atkline3', 100)
    SFX_3('hit_h_slow')
    Unknown1019(80)
    sprite('ka430_31', 5)	# 32954-32958	 **attackbox here**
    Unknown23054('6b613433305f333000000000000000000000000000000000000000000000000004000000')
    GFX_0('kaef430_atk3', 100)
    Unknown1019(80)
    RefreshMultihit()
    Damage(3000)
    AttackP2(100)
    Hitstop(30)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(7000)
    AirPushbackY(-30000)
    YImpluseBeforeWallbounce(1500)
    Unknown9310(100)
    Unknown9190(1)
    Unknown11073(1)
    Unknown11069('PKA_PersonaKenkaOD')

    def upon_78():
        SFX_3('quake_s')
        SFX_3('blaze_normal')
        SFX_3('bound_steal_m')
        ScreenShake(80000, 0)
        clearUponHandler(78)
    sprite('ka430_31', 32767)	# 32959-65725	 **attackbox here**
    Unknown2015(500)
    sendToLabelUpon(2, 4)
    loopRest()
    label(4)
    sprite('ka430_32', 3)	# 65726-65728
    Unknown20000(1)
    Unknown1019(30)
    YAccel(30)
    ScreenShake(0, 20000)
    sprite('ka430_33', 3)	# 65729-65731
    Unknown1019(0)
    YAccel(0)
    sprite('ka430_34', 3)	# 65732-65734
    sprite('ka430_35', 3)	# 65735-65737
    sprite('ka401_11', 3)	# 65738-65740
    Unknown2015(-1)
    sprite('ka401_12', 4)	# 65741-65744
    sprite('ka401_13', 3)	# 65745-65747
    sprite('ka401_13', 3)	# 65748-65750
    Unknown23029(11, 4300, 0)
    sprite('ka401_14', 5)	# 65751-65755
    sprite('ka401_15', 5)	# 65756-65760
    sprite('ka401_16', 5)	# 65761-65765
    sprite('ka000_00', 3)	# 65766-65768
    sprite('ka000_01', 3)	# 65769-65771
    sprite('ka432_00', 3)	# 65772-65774
    sprite('ka432_01', 3)	# 65775-65777
    sprite('ka432_02', 3)	# 65778-65780	 **attackbox here**
    Unknown7007('706b613330395f31000000000000000064000000706b613331305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ka432_03', 3)	# 65781-65783
    sprite('ka432_04', 6)	# 65784-65789
    sprite('ka432_05', 6)	# 65790-65795
    sprite('ka432_06', 6)	# 65796-65801
    sprite('ka432_07', 6)	# 65802-65807
    sprite('ka432_08', 6)	# 65808-65813
    sprite('ka432_09', 3)	# 65814-65816
    sprite('ka432_10', 3)	# 65817-65819
    sprite('ka432_11', 3)	# 65820-65822
    sprite('ka432_09', 3)	# 65823-65825
    sprite('ka432_10', 3)	# 65826-65828
    sprite('ka432_11', 3)	# 65829-65831
    sprite('ka432_09', 3)	# 65832-65834
    sprite('ka432_10', 3)	# 65835-65837
    sprite('ka432_11', 3)	# 65838-65840
    Unknown20000(0)
    sprite('ka432_09', 3)	# 65841-65843
    sprite('ka432_10', 3)	# 65844-65846
    sprite('ka432_11', 3)	# 65847-65849
    sprite('ka432_09', 3)	# 65850-65852
    sprite('ka432_10', 3)	# 65853-65855
    sprite('ka432_11', 3)	# 65856-65858
    sprite('ka432_09', 3)	# 65859-65861
    sprite('ka432_10', 3)	# 65862-65864
    sprite('ka432_11', 3)	# 65865-65867
    sprite('ka432_09', 3)	# 65868-65870
    sprite('ka432_10', 3)	# 65871-65873
    sprite('ka432_11', 3)	# 65874-65876
    sprite('ka432_09', 3)	# 65877-65879
    sprite('ka432_10', 3)	# 65880-65882
    sprite('ka432_11', 3)	# 65883-65885
    Unknown13024(1)
    setInvincible(0)
    Unknown2017(1)
    sprite('ka432_09', 3)	# 65886-65888
    sprite('ka432_10', 3)	# 65889-65891
    sprite('ka432_11', 3)	# 65892-65894
    sprite('ka432_09', 3)	# 65895-65897
    sprite('ka432_10', 3)	# 65898-65900
    sprite('ka432_11', 3)	# 65901-65903
    sprite('ka432_09', 3)	# 65904-65906
    sprite('ka432_10', 3)	# 65907-65909
    sprite('ka432_11', 3)	# 65910-65912
    sprite('ka432_09', 3)	# 65913-65915
    sprite('ka432_10', 3)	# 65916-65918
    sprite('ka432_12', 6)	# 65919-65924
    loopRest()

@State
def Kurokoge():

    def upon_IMMEDIATE():
        Unknown17011('Kurokoge_Exe', 3, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(180000)
        Unknown11032('30570500000000000000000000000000')
        Unknown13024(0)
    sprite('ka431_00', 3)	# 1-3
    setInvincible(1)
    sprite('ka431_01', 2)	# 4-5
    SFX_3('cloth_l')
    sprite('ka431_01', 2)	# 6-7
    Unknown2036(102, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pka256_0', 'pka256_1', '', '')
    sprite('ka431_02', 4)	# 8-11
    sprite('ka431_03', 4)	# 12-15
    sprite('ka431_01', 4)	# 16-19
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 20-23
    sprite('ka431_03', 4)	# 24-27
    sprite('ka431_01', 4)	# 28-31
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 32-35
    sprite('ka431_03', 4)	# 36-39
    sprite('ka431_01', 4)	# 40-43
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 44-47
    sprite('ka431_03', 4)	# 48-51
    sprite('ka431_01', 4)	# 52-55
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 56-59
    sprite('ka431_03', 4)	# 60-63
    sprite('ka431_01', 3)	# 64-66
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 67-69
    sprite('ka431_03', 3)	# 70-72
    sprite('ka431_01', 3)	# 73-75
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 76-78
    sprite('ka431_03', 3)	# 79-81
    sprite('ka431_01', 3)	# 82-84
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 85-87
    sprite('ka431_03', 3)	# 88-90
    sprite('ka431_01', 3)	# 91-93
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 94-96
    sprite('ka431_03', 3)	# 97-99
    sprite('ka431_04', 3)	# 100-102
    sprite('ka431_05', 3)	# 103-105
    sprite('ka431_06', 5)	# 106-110	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(20000)
    sprite('ka431_06', 5)	# 111-115	 **attackbox here**
    setInvincible(0)
    sprite('ka402_04', 3)	# 116-118
    sprite('ka402_05', 3)	# 119-121	 **attackbox here**
    Unknown23027()
    Unknown1019(50)
    SLOT_59 = 0
    sprite('ka402_06', 5)	# 122-126
    Unknown1019(50)
    sprite('ka402_07', 4)	# 127-130
    Unknown1019(50)
    sprite('ka402_08', 8)	# 131-138
    tag_voice(0, 'pka257_0', 'pka257_1', '', '')
    Unknown1019(0)
    SFX_3('ka003')
    sprite('ka402_09', 5)	# 139-143
    sprite('ka402_10', 4)	# 144-147
    sprite('ka402_11', 4)	# 148-151
    sprite('ka402_12', 4)	# 152-155
    sprite('ka402_13', 4)	# 156-159

@State
def Kurokoge_OD():

    def upon_IMMEDIATE():
        Unknown17011('Kurokoge_Exe', 3, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(180000)
        Unknown11032('30570500000000000000000000000000')
        Unknown13024(0)

        def upon_14():
            SLOT_61 = 0
    sprite('ka431_00', 3)	# 1-3
    setInvincible(1)
    sprite('ka431_01', 2)	# 4-5
    SFX_3('cloth_l')
    sprite('ka431_01', 2)	# 6-7
    Unknown2036(102, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pka256_0', 'pka256_1', '', '')
    sprite('ka431_02', 4)	# 8-11
    sprite('ka431_03', 4)	# 12-15
    sprite('ka431_01', 4)	# 16-19
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 20-23
    sprite('ka431_03', 4)	# 24-27
    sprite('ka431_01', 4)	# 28-31
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 32-35
    sprite('ka431_03', 4)	# 36-39
    sprite('ka431_01', 4)	# 40-43
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 44-47
    sprite('ka431_03', 4)	# 48-51
    sprite('ka431_01', 4)	# 52-55
    SFX_3('cloth_l')
    sprite('ka431_02', 4)	# 56-59
    sprite('ka431_03', 4)	# 60-63
    sprite('ka431_01', 3)	# 64-66
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 67-69
    sprite('ka431_03', 3)	# 70-72
    sprite('ka431_01', 3)	# 73-75
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 76-78
    sprite('ka431_03', 3)	# 79-81
    sprite('ka431_01', 3)	# 82-84
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 85-87
    sprite('ka431_03', 3)	# 88-90
    sprite('ka431_01', 3)	# 91-93
    SFX_3('cloth_l')
    sprite('ka431_02', 3)	# 94-96
    sprite('ka431_03', 3)	# 97-99
    sprite('ka431_04', 3)	# 100-102
    sprite('ka431_05', 3)	# 103-105
    sprite('ka431_06', 5)	# 106-110	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(20000)
    SLOT_61 = 1
    sprite('ka431_06', 5)	# 111-115	 **attackbox here**
    setInvincible(0)
    sprite('ka402_04', 3)	# 116-118
    sprite('ka402_05', 3)	# 119-121	 **attackbox here**
    Unknown23027()
    Unknown1019(50)
    SLOT_61 = 0
    sprite('ka402_06', 5)	# 122-126
    Unknown1019(50)
    sprite('ka402_07', 4)	# 127-130
    Unknown1019(50)
    sprite('ka402_08', 8)	# 131-138
    tag_voice(0, 'pka257_0', 'pka257_1', '', '')
    Unknown1019(0)
    SFX_3('ka003')
    sprite('ka402_09', 5)	# 139-143
    sprite('ka402_10', 4)	# 144-147
    sprite('ka402_11', 4)	# 148-151
    sprite('ka402_12', 4)	# 152-155
    sprite('ka402_13', 4)	# 156-159

@State
def Kurokoge_Exe():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown2017(0)
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(1)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(1000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(200)
        Hitstop(0)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23027()
        Unknown13024(0)
        Unknown2004(1, 0)

        def upon_3():
            if SLOT_51:
                if (SLOT_25 < 1000000):
                    sendToLabel(321)
                    SLOT_51 = 0

        def upon_14():
            SLOT_59 = 0
            SLOT_60 = 0
            SLOT_61 = 0
        Unknown21015('6b615f6973756f6b6973656d6500000000000000000000000000000000000000ce10000000000000')

        def upon_43():
            if (SLOT_48 == 4313):
                tag_voice(0, 'pka260_0', 'pka260_1', '', '')
            if (SLOT_48 == 4314):
                Unknown20007(0)
            if (SLOT_48 == 4315):
                Unknown13024(1)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown20003(0)
            SLOT_7 = 0
        Unknown2034(0)
        Unknown20003(1)
    sprite('ka402_05', 15)	# 1-15	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    GFX_0('KurokogeCamera1', 100)
    Unknown21015('4b75726f6b6f676543616d657261310000000000000000000000000000000000d710000000000000')
    Unknown23084(1)
    sprite('ka432_00', 4)	# 16-19
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka432_01', 4)	# 20-23
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka432_02', 4)	# 24-27	 **attackbox here**
    tag_voice(1, 'pka258_0', 'pka258_1', '', '')
    RefreshMultihit()
    Unknown11069('PKA_PersonaKurokoge')
    SFX_3('spin_m')
    Unknown21015('4b75726f6b6f676543616d657261310000000000000000000000000000000000d810000000000000')
    sprite('ka432_03', 10)	# 28-37
    sprite('ka432_03', 50)	# 38-87
    if (SLOT_25 < 865000):
        Unknown1000(1000000)
    if (SLOT_25 < 700000):
        Unknown2037(1)
    sprite('ka432_03', 10)	# 88-97
    Unknown20000(1)
    Unknown20001(1)
    sprite('ka432_04', 6)	# 98-103
    sprite('ka432_05', 4)	# 104-107
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('ka432_06', 35)	# 108-142
    sprite('ka432_07', 6)	# 143-148
    tag_voice(0, 'pka259_0', 'pka259_1', '', '')
    sprite('ka432_08', 6)	# 149-154
    sprite('ka432_09', 6)	# 155-160
    sprite('ka432_10', 6)	# 161-166
    Unknown23029(11, 4310, 0)
    if SLOT_61:
        SLOT_7 = 1
        SLOT_61 = 0
    sprite('ka432_11', 6)	# 167-172
    sprite('ka432_09', 6)	# 173-178
    sprite('ka432_10', 6)	# 179-184
    sprite('ka432_11', 6)	# 185-190
    Unknown23084(0)
    if SLOT_38:
        Unknown47('00000000020000001600000000000000e487f8ff0200000036000000')
    else:
        Unknown47('000000000200000016000000000000001c7807000200000036000000')
        SLOT_54 = (SLOT_54 * (-1))
    Unknown48('160000000200000016000000190000000200000036000000')
    Unknown36(22)
    teleportRelativeY(700000)
    physicsYImpulse(-20000)
    setGravity(0)
    Unknown35()
    sprite('ka432_09', 6)	# 191-196
    sprite('ka432_10', 6)	# 197-202
    sprite('ka432_11', 6)	# 203-208
    sprite('ka432_09', 6)	# 209-214
    Unknown20000(0)
    if (not SLOT_2):
        Unknown20007(1)
    sprite('ka432_10', 6)	# 215-220
    sprite('ka432_11', 6)	# 221-226
    sprite('ka432_09', 6)	# 227-232
    sprite('ka432_10', 6)	# 233-238
    sprite('ka432_11', 6)	# 239-244
    sprite('ka432_09', 6)	# 245-250
    sprite('ka432_10', 6)	# 251-256
    sprite('ka432_11', 6)	# 257-262
    sprite('ka432_09', 6)	# 263-268
    sprite('ka432_10', 6)	# 269-274
    sprite('ka432_11', 6)	# 275-280
    sprite('ka432_09', 6)	# 281-286
    sprite('ka432_10', 6)	# 287-292
    sprite('ka432_11', 6)	# 293-298
    sprite('ka432_09', 6)	# 299-304
    sprite('ka432_10', 6)	# 305-310
    sprite('ka432_11', 6)	# 311-316
    loopRest()
    Unknown48('19000000020000003a0000000b000000020000003a000000')
    Unknown48('1900000002000000390000000b0000000200000039000000')
    if (SLOT_25 > 1565000):
        Unknown1000(500000)
    (SLOT_25 < 1000000)
    if SLOT_0:
        _gotolabel(34)
    sprite('ka432_12', 6)	# 317-322
    SLOT_51 = 1
    sprite('ka432_12', 6)	# 323-328
    sprite('ka000_00', 3)	# 329-331
    sprite('ka032_00', 3)	# 332-334
    sprite('ka032_01', 3)	# 335-337
    sprite('ka032_02', 3)	# 338-340
    Unknown48('1900000002000000390000000b0000000200000039000000')
    if (SLOT_57 < 120):
        Unknown47('0100000002000000190000000000000040420f000200000038000000')
        op(1, 0, 120, 2, 57)
        Unknown47('03000000020000003800000002000000000000000200000037000000')
        if (SLOT_55 > 45000):
            physicsXImpulse(45000)
        else:
            SLOT_12 = SLOT_55
    else:
        physicsXImpulse(20000)
    label(0)
    sprite('ka032_03', 4)	# 341-344
    sprite('ka032_04', 4)	# 345-348
    Unknown8006(100, 1, 1)
    sprite('ka032_05', 4)	# 349-352
    sprite('ka032_06', 4)	# 353-356
    sprite('ka032_07', 4)	# 357-360
    sprite('ka032_08', 4)	# 361-364
    Unknown8006(100, 1, 1)
    sprite('ka032_09', 4)	# 365-368
    sprite('ka032_10', 4)	# 369-372
    loopRest()
    gotoLabel(0)
    label(321)
    sprite('ka032_11', 4)	# 373-376
    physicsXImpulse(13000)
    sprite('ka032_11', 4)	# 377-380
    sprite('ka032_11', 4)	# 381-384
    physicsXImpulse(8000)
    sprite('ka032_12', 4)	# 385-388
    sprite('ka032_12', 6)	# 389-394
    Unknown1019(0)
    loopRest()
    ExitState()
    label(34)
    sprite('ka432_09', 9)	# 395-403
    sprite('ka432_10', 9)	# 404-412
    sprite('ka432_11', 9)	# 413-421
    sprite('ka432_12', 8)	# 422-429

@State
def AstralHeat():

    def upon_IMMEDIATE():
        Unknown17011('IchigekiExe', 6, 0, 0)
        Unknown11054(160000)
        Unknown11032('e093040000000000400d030000000000')
        Unknown2004(1, 0)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11082(1)
        Unknown11025(0)
    sprite('ka450_00', 3)	# 1-3
    setInvincible(1)
    sprite('ka450_01', 6)	# 4-9
    physicsXImpulse(6000)
    tag_voice(1, 'pka290_0', 'pka290_1', '', '')
    sprite('ka450_02', 6)	# 10-15
    Unknown2036(50, -1, 2)
    GFX_0('P4U_Cutin_Parent', 100)
    Unknown23147()

    def upon_3():
        Unknown48('19000000020000003300000016000000020000001e000000')
        if SLOT_51:
            Unknown11045(0)
        else:
            Unknown11045(1)
    sprite('ka450_03', 6)	# 16-21
    sprite('ka450_04', 6)	# 22-27
    sprite('ka450_05', 6)	# 28-33
    sprite('ka450_06', 6)	# 34-39
    sprite('ka450_07', 6)	# 40-45
    SFX_3('ka003')
    sprite('ka450_08', 6)	# 46-51
    sprite('ka450_09', 6)	# 52-57
    sprite('ka450_10', 6)	# 58-63
    sprite('ka450_11', 6)	# 64-69
    physicsXImpulse(0)
    sprite('ka450_12', 3)	# 70-72	 **attackbox here**
    RefreshMultihit()
    sprite('ka450_12', 5)	# 73-77	 **attackbox here**
    Unknown23027()
    clearUponHandler(3)
    sprite('ka450_13', 6)	# 78-83
    setInvincible(0)
    sprite('ka450_14', 10)	# 84-93
    tag_voice(0, 'pka291_0', 'pka291_1', '', '')
    SFX_3('ka003')
    sprite('ka450_15', 8)	# 94-101
    sprite('ka450_16', 8)	# 102-109
    sprite('ka450_17', 8)	# 110-117

@State
def IchigekiExe():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        AttackLevel_(5)
        Damage(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(150000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(10000)
        Unknown11064(1)
        Unknown23083(1)
        Unknown2004(1, 0)
        Unknown23084(1)
        Unknown23157(1)
        Unknown23088(1, 1)

        def upon_STATE_END():
            pass
        sendToLabelUpon(40, 8)
        sendToLabelUpon(41, 9)
    sprite('ka450_12', 10)	# 1-10	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    GFX_0('IchigekiCamera', 100)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000020000000')
    Unknown23027()
    sprite('ka451_00', 3)	# 11-13
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka451_01', 3)	# 14-16
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    tag_voice(1, 'pka292_0', 'pka292_1', '', '')
    sprite('ka451_02', 20)	# 17-36
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka451_03', 3)	# 37-39
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000021000000')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka451_04', 3)	# 40-42
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka451_05', 3)	# 43-45
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka451_06', 3)	# 46-48
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ka451_07', 3)	# 49-51	 **attackbox here**
    SFX_3('ka004')
    RefreshMultihit()
    sprite('ka451_08', 5)	# 52-56
    sprite('ka451_08', 15)	# 57-71
    sprite('ka451_08', 32767)	# 72-32838
    loopRest()
    label(8)
    sprite('keep', 180)	# 32839-33018
    Unknown23024(2)
    Unknown23029(11, 4500, 0)
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(2000000)
    Unknown1084(1)
    Unknown35()
    sprite('keep', 25)	# 33019-33043
    GFX_0('IchigekiPicture1', 100)
    GFX_0('IchigekiPicture2', 100)
    GFX_0('IchigekiPicture4', 100)
    sprite('keep', 80)	# 33044-33123
    sprite('keep', 10)	# 33124-33133
    Unknown21007(3, 41)
    tag_voice(0, 'pka293_0', 'pka293_1', '', '')
    label(9)
    sprite('ka451_09', 6)	# 33134-33139
    Unknown1000(-300000)
    Unknown23024(3)
    GFX_0('kaef_450smoke', 100)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000023000000')
    Unknown21012('504b415f506572736f6e614963686967656b690000000000000000000000000027000000')
    sprite('ka451_10', 6)	# 33140-33145
    Unknown26('SCEF_RyuhaiYoko')
    Unknown26('IchigekiPicture1')
    Unknown26('IchigekiPicture2')
    sprite('ka451_11', 6)	# 33146-33151
    sprite('ka451_09', 6)	# 33152-33157
    sprite('ka451_10', 6)	# 33158-33163
    sprite('ka451_11', 6)	# 33164-33169
    sprite('ka451_09', 6)	# 33170-33175
    sprite('ka451_10', 6)	# 33176-33181
    sprite('ka451_11', 6)	# 33182-33187
    sprite('ka451_09', 6)	# 33188-33193
    sprite('ka451_10', 6)	# 33194-33199
    sprite('ka451_11', 6)	# 33200-33205
    sprite('ka451_09', 6)	# 33206-33211
    sprite('ka451_10', 6)	# 33212-33217
    sprite('ka451_11', 6)	# 33218-33223
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(2000000)
    physicsYImpulse(-40000)
    setGravity(0)
    Unknown35()
    sprite('ka451_09', 6)	# 33224-33229
    sprite('ka451_10', 6)	# 33230-33235
    sprite('ka451_11', 6)	# 33236-33241
    sprite('ka451_09', 6)	# 33242-33247
    sprite('ka451_10', 6)	# 33248-33253
    sprite('ka451_11', 6)	# 33254-33259
    tag_voice(0, 'pka294_0', 'pka294_1', '', '')
    sprite('ka451_12', 6)	# 33260-33265
    GFX_0('ka450_PunchAura', 0)
    sprite('ka451_13', 5)	# 33266-33270	 **attackbox here**
    ScreenShake(8000, 4000)
    SFX_3('damage_ichigeki_hit')
    SFX_3('quake_l')
    RefreshMultihit()
    Damage(30350)
    Unknown11001(120, 120, 120)
    Hitstop(0)
    AirPushbackX(0)
    AirPushbackY(-10000)
    Unknown11064(3)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23024(0)
    Unknown26('kaef_450smoke')
    GFX_0('ka450_PunchBom', 0)
    sprite('ka451_13', 60)	# 33271-33330	 **attackbox here**
    ScreenShake(8000, 4000)
    Unknown36(22)
    Unknown23130(0, 15, 1)
    Unknown23132(1)
    Unknown35()
    Unknown23130(0, 15, 1)
    SFX_3('bomb_l')
    SFX_3('quake_l')
    sprite('ka451_14', 5)	# 33331-33335
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_15', 5)	# 33336-33340
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_13', 5)	# 33341-33345	 **attackbox here**
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_14', 5)	# 33346-33350
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_15', 5)	# 33351-33355
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_13', 5)	# 33356-33360	 **attackbox here**
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_14', 5)	# 33361-33365
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_15', 5)	# 33366-33370
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_13', 5)	# 33371-33375	 **attackbox here**
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_14', 5)	# 33376-33380
    SFX_3('quake_l')
    ScreenShake(3000, 3000)
    sprite('ka451_15', 5)	# 33381-33385
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000024000000')
    sprite('ka451_16', 30)	# 33386-33415
    Unknown3026(-1)
    Unknown1084(1)
    sprite('ka451_17', 3)	# 33416-33418
    sprite('ka451_18', 3)	# 33419-33421
    sprite('ka451_19', 3)	# 33422-33424
    Unknown18010()
    tag_voice(0, 'pka295_0', 'pka295_1', '', '')
    sprite('ka451_20', 3)	# 33425-33427
    sprite('ka451_21', 3)	# 33428-33430
    sprite('ka451_22', 3)	# 33431-33433
    sprite('ka451_23', 6)	# 33434-33439
    sprite('ka451_24', 6)	# 33440-33445
    sprite('ka451_25', 6)	# 33446-33451
    sprite('ka451_23', 6)	# 33452-33457
    sprite('ka451_24', 6)	# 33458-33463
    sprite('ka451_25', 6)	# 33464-33469
    Unknown21011(120)
    label(99)
    sprite('ka451_23', 6)	# 33470-33475
    sprite('ka451_24', 6)	# 33476-33481
    sprite('ka451_25', 6)	# 33482-33487
    gotoLabel(99)

@Subroutine
def MouthTableInit():
    Unknown18011('pka000', 12643, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka295_0', 13667, 13409, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka295_1', 12643, 13665, 13667, 13665, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka500', 12643, 14177, 14179, 12641, 25397, 14135, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka501', 12643, 14177, 14179, 12641, 25397, 12854, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka502', 12643, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 12641, 25397, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 13923, 24881, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka506', 12643, 24880, 13617, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka507', 12643, 14177, 14179, 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka522', 12643, 12641, 25394, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka523', 12643, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka524', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka525', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 12643, 24880, 25397, 24885, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24885, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka402_0', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka402_1', 12643, 13665, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka403_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka403_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka600baz', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka600bjb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka600pbc', 12643, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka600pna', 12643, 12641, 25397, 24887, 25399, 14131, 14177, 14691, 14177, 14179, 14177, 14691, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka600pyu', 12643, 14177, 12643, 24880, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka600ryn', 12643, 14177, 14179, 14177, 12643, 24880, 13617, 14179, 14177, 13155, 24880, 25397, 24885, 25397, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka600uca', 12643, 12641, 25397, 24887, 25399, 24887, 12849, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka601btg', 12643, 14177, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka601pyo', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 12641, 25397, 24889, 25399, 14132, 13665, 13667, 14177, 14691, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka700pbc', 12643, 12641, 25394, 24887, 25399, 24887, 25399, 14134, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 13623, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka700pna', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka700pyo', 12643, 13665, 13667, 12641, 25392, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka700ryn', 12643, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 13364, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka700uca', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka701baz', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka701bjb', 12643, 13153, 25392, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 12341, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka701btg', 12643, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka701pyu', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 12593, 13665, 13667, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pka702pbc', 12643, 12641, 25394, 24887, 25399, 24887, 12849, 14179, 12641, 25392, 12851, 12641, 25394, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('btg')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('baz')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bjb')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pna')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(180)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('ka600_00', 6)	# 2-7
    sprite('ka600_01', 6)	# 8-13
    sprite('ka600_02', 6)	# 14-19
    sprite('ka600_00', 6)	# 20-25
    Unknown7006('pka502', 100, 895576944, 13104, 0, 0, 100, 895576944, 13616, 0, 0, 100, 895576944, 13872, 0, 0, 100)
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 26-31
    sprite('ka600_02', 6)	# 32-37
    sprite('ka600_00', 6)	# 38-43
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 44-49
    sprite('ka600_02', 6)	# 50-55
    sprite('ka600_03', 6)	# 56-61
    sprite('ka600_04', 6)	# 62-67
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 68-73
    sprite('ka600_06', 6)	# 74-79
    sprite('ka600_04', 6)	# 80-85
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 86-91
    sprite('ka600_06', 6)	# 92-97
    sprite('ka600_04', 6)	# 98-103
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 104-109
    sprite('ka600_06', 6)	# 110-115
    sprite('ka600_07', 6)	# 116-121
    sprite('ka600_08', 6)	# 122-127
    sprite('ka600_09', 6)	# 128-133
    sprite('ka600_10', 6)	# 134-139
    sprite('ka600_11', 6)	# 140-145
    sprite('ka600_12', 6)	# 146-151
    SFX_3('slash_sword_middle')
    sprite('ka600_13', 6)	# 152-157
    sprite('ka600_14', 6)	# 158-163
    sprite('ka600_15', 10)	# 164-173
    sprite('ka600_16', 6)	# 174-179
    SFX_3('ka003')
    Unknown23018(1)
    label(1)
    sprite('ka000_00', 6)	# 180-185
    sprite('ka000_01', 6)	# 186-191
    sprite('ka000_02', 6)	# 192-197
    sprite('ka000_03', 6)	# 198-203
    sprite('ka000_04', 6)	# 204-209
    sprite('ka000_05', 6)	# 210-215
    sprite('ka000_06', 6)	# 216-221
    sprite('ka000_07', 6)	# 222-227
    sprite('ka000_08', 6)	# 228-233
    sprite('ka000_09', 6)	# 234-239
    sprite('ka000_10', 6)	# 240-245
    sprite('ka000_11', 6)	# 246-251
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('ka601_00', 30)	# 252-281
    if random_(2, 0, 50):
        Unknown7006('pka500', 100, 895576944, 12592, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown2037(1)
    SFX_3('damage_hit_h')
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(-2000000)
    ScreenShake(10000, 10000)
    GFX_1('ef_hit_blowm', 0)
    GFX_0('Entry_2', 0)
    sprite('ka601_50', 3)	# 282-284
    sprite('ka601_01', 3)	# 285-287
    sprite('ka030_07', 5)	# 288-292
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(7000)
    sprite('ka030_08', 5)	# 293-297
    sprite('ka030_09', 5)	# 298-302
    sprite('ka030_10', 5)	# 303-307
    sprite('ka030_11', 5)	# 308-312
    sprite('ka030_02', 5)	# 313-317
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ka030_03', 5)	# 318-322
    sprite('ka030_04', 5)	# 323-327
    sprite('ka030_05', 5)	# 328-332
    sprite('ka030_06', 5)	# 333-337
    sprite('ka030_07', 5)	# 338-342
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ka030_08', 5)	# 343-347
    sprite('ka030_09', 5)	# 348-352
    sprite('ka030_10', 5)	# 353-357
    sprite('ka030_11', 5)	# 358-362
    sprite('ka030_02', 5)	# 363-367
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ka030_03', 5)	# 368-372
    sprite('ka030_04', 5)	# 373-377
    sprite('ka030_05', 5)	# 378-382
    sprite('ka030_06', 5)	# 383-387
    sprite('ka030_07', 5)	# 388-392
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ka030_08', 5)	# 393-397
    sprite('ka030_00', 6)	# 398-403
    Unknown1084(1)
    sprite('ka010_00', 6)	# 404-409
    Unknown1000(-1230000)
    sprite('ka601_10', 6)	# 410-415
    sprite('ka601_11', 6)	# 416-421
    if SLOT_2:
        Unknown7006('pka504', 100, 895576944, 14128, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ka601_12', 6)	# 422-427
    SFX_3('cloth_l')
    label(11)
    sprite('ka601_13', 6)	# 428-433
    sprite('ka601_14', 6)	# 434-439
    sprite('ka601_12', 6)	# 440-445
    SFX_3('cloth_l')
    if SLOT_97:
        _gotolabel(11)
    sprite('ka601_13', 6)	# 446-451
    sprite('ka601_14', 6)	# 452-457
    sprite('ka601_12', 6)	# 458-463
    SFX_3('cloth_l')
    sprite('ka601_13', 6)	# 464-469
    sprite('ka601_14', 6)	# 470-475
    sprite('ka601_15', 6)	# 476-481
    sprite('ka601_16', 6)	# 482-487
    Unknown23018(1)
    label(12)
    sprite('ka000_00', 6)	# 488-493
    sprite('ka000_01', 6)	# 494-499
    sprite('ka000_02', 6)	# 500-505
    sprite('ka000_03', 6)	# 506-511
    sprite('ka000_04', 6)	# 512-517
    sprite('ka000_05', 6)	# 518-523
    sprite('ka000_06', 6)	# 524-529
    sprite('ka000_07', 6)	# 530-535
    sprite('ka000_08', 6)	# 536-541
    sprite('ka000_09', 6)	# 542-547
    sprite('ka000_10', 6)	# 548-553
    sprite('ka000_11', 6)	# 554-559
    gotoLabel(12)
    ExitState()
    label(20)
    sprite('ka000_00', 1)	# 560-560
    SFX_1('pka700ryn')
    label(21)
    sprite('ka000_00', 6)	# 561-566
    sprite('ka000_01', 6)	# 567-572
    sprite('ka000_02', 6)	# 573-578
    sprite('ka000_03', 6)	# 579-584
    sprite('ka000_04', 6)	# 585-590
    sprite('ka000_05', 6)	# 591-596
    sprite('ka000_06', 6)	# 597-602
    sprite('ka000_07', 6)	# 603-608
    sprite('ka000_08', 6)	# 609-614
    sprite('ka000_09', 6)	# 615-620
    sprite('ka000_10', 6)	# 621-626
    sprite('ka000_11', 6)	# 627-632
    gotoLabel(21)
    ExitState()
    label(100)
    sprite('ka600_00', 1)	# 633-633
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
        SFX_1('pka601btg')
    label(101)
    sprite('ka600_00', 6)	# 634-639
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 640-645
    sprite('ka600_02', 6)	# 646-651
    gotoLabel(101)
    label(102)
    sprite('ka600_03', 6)	# 652-657
    sprite('ka600_04', 6)	# 658-663
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 664-669
    sprite('ka600_06', 6)	# 670-675
    sprite('ka600_04', 6)	# 676-681
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 682-687
    sprite('ka600_06', 6)	# 688-693
    sprite('ka600_04', 6)	# 694-699
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 700-705
    sprite('ka600_06', 6)	# 706-711
    sprite('ka600_07', 6)	# 712-717
    sprite('ka600_08', 6)	# 718-723
    sprite('ka600_09', 6)	# 724-729
    sprite('ka600_10', 6)	# 730-735
    sprite('ka600_11', 6)	# 736-741
    sprite('ka600_12', 6)	# 742-747
    SFX_3('slash_sword_middle')
    sprite('ka600_13', 6)	# 748-753
    sprite('ka600_14', 6)	# 754-759
    sprite('ka600_15', 10)	# 760-769
    sprite('ka600_16', 6)	# 770-775
    SFX_3('ka003')
    Unknown23018(1)
    label(103)
    sprite('ka000_00', 6)	# 776-781
    sprite('ka000_01', 6)	# 782-787
    sprite('ka000_02', 6)	# 788-793
    sprite('ka000_03', 6)	# 794-799
    sprite('ka000_04', 6)	# 800-805
    sprite('ka000_05', 6)	# 806-811
    sprite('ka000_06', 6)	# 812-817
    sprite('ka000_07', 6)	# 818-823
    sprite('ka000_08', 6)	# 824-829
    sprite('ka000_09', 6)	# 830-835
    sprite('ka000_10', 6)	# 836-841
    sprite('ka000_11', 6)	# 842-847
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('ka001_00', 7)	# 848-854
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ka001_01', 7)	# 855-861
    SFX_1('pka600baz')
    sprite('ka001_02', 7)	# 862-868
    sprite('ka001_03', 7)	# 869-875
    sprite('ka001_04', 8)	# 876-883
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 884-891
    sprite('ka001_06', 8)	# 892-899
    sprite('ka001_07', 8)	# 900-907
    SFX_3('ka000')
    sprite('ka001_06', 8)	# 908-915
    sprite('ka001_05', 8)	# 916-923
    sprite('ka001_04', 8)	# 924-931
    sprite('ka001_05', 8)	# 932-939
    SFX_3('ka000')
    sprite('ka001_06', 8)	# 940-947
    sprite('ka001_07', 8)	# 948-955
    sprite('ka001_06', 8)	# 956-963
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 964-971
    sprite('ka001_04', 8)	# 972-979
    sprite('ka001_05', 8)	# 980-987
    SFX_3('ka000')
    sprite('ka001_06', 8)	# 988-995
    label(111)
    sprite('ka001_07', 1)	# 996-996
    if SLOT_97:
        _gotolabel(111)
    sprite('ka001_07', 20)	# 997-1016
    sprite('ka001_08', 7)	# 1017-1023
    sprite('ka001_09', 7)	# 1024-1030
    sprite('ka001_10', 7)	# 1031-1037
    sprite('ka001_00', 7)	# 1038-1044
    Unknown21007(24, 40)
    Unknown21011(240)
    label(112)
    sprite('ka000_00', 6)	# 1045-1050
    sprite('ka000_01', 6)	# 1051-1056
    sprite('ka000_02', 6)	# 1057-1062
    sprite('ka000_03', 6)	# 1063-1068
    sprite('ka000_04', 6)	# 1069-1074
    sprite('ka000_05', 6)	# 1075-1080
    sprite('ka000_06', 6)	# 1081-1086
    sprite('ka000_07', 6)	# 1087-1092
    sprite('ka000_08', 6)	# 1093-1098
    sprite('ka000_09', 6)	# 1099-1104
    sprite('ka000_10', 6)	# 1105-1110
    sprite('ka000_11', 6)	# 1111-1116
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('ka600_00', 6)	# 1117-1122
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ka600_01', 6)	# 1123-1128
    SFX_1('pka600bjb')
    sprite('ka600_02', 6)	# 1129-1134
    sprite('ka600_00', 6)	# 1135-1140
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 1141-1146
    sprite('ka600_02', 6)	# 1147-1152
    sprite('ka600_00', 6)	# 1153-1158
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 1159-1164
    sprite('ka600_02', 6)	# 1165-1170
    sprite('ka600_03', 6)	# 1171-1176
    sprite('ka600_04', 6)	# 1177-1182
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 1183-1188
    sprite('ka600_06', 6)	# 1189-1194
    sprite('ka600_04', 6)	# 1195-1200
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 1201-1206
    sprite('ka600_06', 6)	# 1207-1212
    sprite('ka600_04', 6)	# 1213-1218
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 1219-1224
    sprite('ka600_06', 6)	# 1225-1230
    sprite('ka600_07', 6)	# 1231-1236
    sprite('ka600_08', 6)	# 1237-1242
    sprite('ka600_09', 6)	# 1243-1248
    sprite('ka600_10', 6)	# 1249-1254
    sprite('ka600_11', 6)	# 1255-1260
    sprite('ka600_12', 6)	# 1261-1266
    SFX_3('slash_sword_middle')
    sprite('ka600_13', 6)	# 1267-1272
    sprite('ka600_14', 6)	# 1273-1278
    sprite('ka600_15', 10)	# 1279-1288
    sprite('ka600_16', 6)	# 1289-1294
    SFX_3('ka003')
    label(121)
    sprite('ka000_00', 6)	# 1295-1300
    sprite('ka000_01', 6)	# 1301-1306
    sprite('ka000_02', 6)	# 1307-1312
    sprite('ka000_03', 6)	# 1313-1318
    sprite('ka000_04', 6)	# 1319-1324
    sprite('ka000_05', 6)	# 1325-1330
    sprite('ka000_06', 6)	# 1331-1336
    sprite('ka000_07', 6)	# 1337-1342
    sprite('ka000_08', 6)	# 1343-1348
    sprite('ka000_09', 6)	# 1349-1354
    sprite('ka000_10', 6)	# 1355-1360
    sprite('ka000_11', 6)	# 1361-1366
    if SLOT_97:
        _gotolabel(121)
    sprite('ka000_00', 1)	# 1367-1367
    Unknown21007(24, 40)
    Unknown21011(240)
    label(122)
    sprite('ka000_00', 6)	# 1368-1373
    sprite('ka000_01', 6)	# 1374-1379
    sprite('ka000_02', 6)	# 1380-1385
    sprite('ka000_03', 6)	# 1386-1391
    sprite('ka000_04', 6)	# 1392-1397
    sprite('ka000_05', 6)	# 1398-1403
    sprite('ka000_06', 6)	# 1404-1409
    sprite('ka000_07', 6)	# 1410-1415
    sprite('ka000_08', 6)	# 1416-1421
    sprite('ka000_09', 6)	# 1422-1427
    sprite('ka000_10', 6)	# 1428-1433
    sprite('ka000_11', 6)	# 1434-1439
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('ka001_00', 7)	# 1440-1446
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ka001_01', 7)	# 1447-1453
    SFX_1('pka600pbc')
    sprite('ka001_02', 7)	# 1454-1460
    sprite('ka001_03', 7)	# 1461-1467
    sprite('ka001_04', 8)	# 1468-1475
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 1476-1483
    sprite('ka001_06', 8)	# 1484-1491
    sprite('ka001_07', 8)	# 1492-1499
    SFX_3('ka000')
    sprite('ka001_06', 8)	# 1500-1507
    sprite('ka001_05', 8)	# 1508-1515
    sprite('ka001_04', 8)	# 1516-1523
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 1524-1531
    sprite('ka001_06', 8)	# 1532-1539
    sprite('ka001_07', 8)	# 1540-1547
    SFX_3('ka000')
    sprite('ka001_06', 8)	# 1548-1555
    sprite('ka001_05', 8)	# 1556-1563
    sprite('ka001_04', 8)	# 1564-1571
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 1572-1579
    sprite('ka001_06', 8)	# 1580-1587
    label(131)
    sprite('ka001_07', 1)	# 1588-1588
    if SLOT_97:
        _gotolabel(131)
    sprite('ka001_07', 20)	# 1589-1608
    sprite('ka001_08', 7)	# 1609-1615
    sprite('ka001_09', 7)	# 1616-1622
    sprite('ka001_10', 7)	# 1623-1629
    sprite('ka001_00', 7)	# 1630-1636
    Unknown21007(24, 40)
    Unknown21011(140)
    label(132)
    sprite('ka000_00', 6)	# 1637-1642
    sprite('ka000_01', 6)	# 1643-1648
    sprite('ka000_02', 6)	# 1649-1654
    sprite('ka000_03', 6)	# 1655-1660
    sprite('ka000_04', 6)	# 1661-1666
    sprite('ka000_05', 6)	# 1667-1672
    sprite('ka000_06', 6)	# 1673-1678
    sprite('ka000_07', 6)	# 1679-1684
    sprite('ka000_08', 6)	# 1685-1690
    sprite('ka000_09', 6)	# 1691-1696
    sprite('ka000_10', 6)	# 1697-1702
    sprite('ka000_11', 6)	# 1703-1708
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('ka600_00', 1)	# 1709-1709
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
        SFX_1('pka601pyo')
    label(141)
    sprite('ka600_00', 6)	# 1710-1715
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 1716-1721
    sprite('ka600_02', 6)	# 1722-1727
    gotoLabel(141)
    label(142)
    sprite('ka600_03', 6)	# 1728-1733
    sprite('ka600_04', 6)	# 1734-1739
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 1740-1745
    sprite('ka600_06', 6)	# 1746-1751
    sprite('ka600_04', 6)	# 1752-1757
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 1758-1763
    sprite('ka600_06', 6)	# 1764-1769
    sprite('ka600_04', 6)	# 1770-1775
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 1776-1781
    sprite('ka600_06', 6)	# 1782-1787
    sprite('ka600_07', 6)	# 1788-1793
    sprite('ka600_08', 6)	# 1794-1799
    sprite('ka600_09', 6)	# 1800-1805
    sprite('ka600_10', 6)	# 1806-1811
    sprite('ka600_11', 6)	# 1812-1817
    sprite('ka600_12', 6)	# 1818-1823
    SFX_3('slash_sword_middle')
    sprite('ka600_13', 6)	# 1824-1829
    sprite('ka600_14', 6)	# 1830-1835
    sprite('ka600_15', 10)	# 1836-1845
    sprite('ka600_16', 6)	# 1846-1851
    SFX_3('ka003')
    Unknown23018(1)
    label(143)
    sprite('ka000_00', 6)	# 1852-1857
    sprite('ka000_01', 6)	# 1858-1863
    sprite('ka000_02', 6)	# 1864-1869
    sprite('ka000_03', 6)	# 1870-1875
    sprite('ka000_04', 6)	# 1876-1881
    sprite('ka000_05', 6)	# 1882-1887
    sprite('ka000_06', 6)	# 1888-1893
    sprite('ka000_07', 6)	# 1894-1899
    sprite('ka000_08', 6)	# 1900-1905
    sprite('ka000_09', 6)	# 1906-1911
    sprite('ka000_10', 6)	# 1912-1917
    sprite('ka000_11', 6)	# 1918-1923
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('ka600_00', 6)	# 1924-1929
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)
    sprite('ka600_01', 6)	# 1930-1935
    SFX_1('pka600pyu')
    sprite('ka600_02', 6)	# 1936-1941
    sprite('ka600_00', 6)	# 1942-1947
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 1948-1953
    sprite('ka600_02', 6)	# 1954-1959
    sprite('ka600_00', 6)	# 1960-1965
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 1966-1971
    sprite('ka600_02', 6)	# 1972-1977
    sprite('ka600_03', 6)	# 1978-1983
    sprite('ka600_04', 6)	# 1984-1989
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 1990-1995
    sprite('ka600_06', 6)	# 1996-2001
    sprite('ka600_04', 6)	# 2002-2007
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 2008-2013
    sprite('ka600_06', 6)	# 2014-2019
    sprite('ka600_04', 6)	# 2020-2025
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 2026-2031
    sprite('ka600_06', 6)	# 2032-2037
    sprite('ka600_07', 6)	# 2038-2043
    sprite('ka600_08', 6)	# 2044-2049
    sprite('ka600_09', 6)	# 2050-2055
    sprite('ka600_10', 6)	# 2056-2061
    sprite('ka600_11', 6)	# 2062-2067
    sprite('ka600_12', 6)	# 2068-2073
    SFX_3('slash_sword_middle')
    sprite('ka600_13', 6)	# 2074-2079
    sprite('ka600_14', 6)	# 2080-2085
    sprite('ka600_15', 10)	# 2086-2095
    sprite('ka600_16', 6)	# 2096-2101
    SFX_3('ka003')
    Unknown2037(2)
    label(151)
    sprite('ka000_00', 6)	# 2102-2107
    sprite('ka000_01', 6)	# 2108-2113
    sprite('ka000_02', 6)	# 2114-2119
    sprite('ka000_03', 6)	# 2120-2125
    sprite('ka000_04', 6)	# 2126-2131
    sprite('ka000_05', 6)	# 2132-2137
    if (not SLOT_2):
        Unknown21007(24, 40)
        Unknown21011(240)
    sprite('ka000_06', 6)	# 2138-2143
    sprite('ka000_07', 6)	# 2144-2149
    sprite('ka000_08', 6)	# 2150-2155
    sprite('ka000_09', 6)	# 2156-2161
    sprite('ka000_10', 6)	# 2162-2167
    sprite('ka000_11', 6)	# 2168-2173
    Unknown2038(-1)
    gotoLabel(151)
    ExitState()
    label(160)
    sprite('ka010_00', 6)	# 2174-2179
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ka601_10', 6)	# 2180-2185
    SFX_1('pka600pna')
    sprite('ka601_11', 6)	# 2186-2191
    label(161)
    sprite('ka601_12', 6)	# 2192-2197
    SFX_3('cloth_l')
    sprite('ka601_13', 6)	# 2198-2203
    sprite('ka601_14', 6)	# 2204-2209
    if SLOT_97:
        _gotolabel(161)
    sprite('ka601_12', 6)	# 2210-2215
    SFX_3('cloth_l')
    sprite('ka601_13', 6)	# 2216-2221
    sprite('ka601_14', 6)	# 2222-2227
    sprite('ka601_15', 6)	# 2228-2233
    sprite('ka601_16', 6)	# 2234-2239
    Unknown21007(24, 40)
    Unknown21011(240)
    label(162)
    sprite('ka000_00', 6)	# 2240-2245
    sprite('ka000_01', 6)	# 2246-2251
    sprite('ka000_02', 6)	# 2252-2257
    sprite('ka000_03', 6)	# 2258-2263
    sprite('ka000_04', 6)	# 2264-2269
    sprite('ka000_05', 6)	# 2270-2275
    sprite('ka000_06', 6)	# 2276-2281
    sprite('ka000_07', 6)	# 2282-2287
    sprite('ka000_08', 6)	# 2288-2293
    sprite('ka000_09', 6)	# 2294-2299
    sprite('ka000_10', 6)	# 2300-2305
    sprite('ka000_11', 6)	# 2306-2311
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('ka001_00', 7)	# 2312-2318
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1230000)
        Unknown2005()
    sprite('ka001_01', 7)	# 2319-2325
    SFX_1('pka600uca')
    sprite('ka001_02', 7)	# 2326-2332
    sprite('ka001_03', 7)	# 2333-2339
    sprite('ka001_04', 8)	# 2340-2347
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 2348-2355
    sprite('ka001_06', 8)	# 2356-2363
    sprite('ka001_07', 8)	# 2364-2371
    SFX_3('ka000')
    sprite('ka001_06', 8)	# 2372-2379
    sprite('ka001_05', 8)	# 2380-2387
    sprite('ka001_04', 8)	# 2388-2395
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 2396-2403
    sprite('ka001_06', 8)	# 2404-2411
    sprite('ka001_07', 8)	# 2412-2419
    SFX_3('ka000')
    sprite('ka001_06', 8)	# 2420-2427
    sprite('ka001_05', 8)	# 2428-2435
    sprite('ka001_04', 8)	# 2436-2443
    SFX_3('ka000')
    sprite('ka001_05', 8)	# 2444-2451
    sprite('ka001_06', 8)	# 2452-2459
    label(171)
    sprite('ka001_07', 1)	# 2460-2460
    if SLOT_97:
        _gotolabel(171)
    sprite('ka001_07', 10)	# 2461-2470
    sprite('ka001_07', 32767)	# 2471-35237
    Unknown21007(24, 40)
    Unknown21011(240)
    ExitState()
    label(180)
    sprite('ka600_00', 6)	# 35238-35243
    if SLOT_158:
        Unknown1000(-1210000)
    else:
        Unknown1000(-1465000)
    sprite('ka600_01', 6)	# 35244-35249
    SFX_1('pka600ryn')
    sprite('ka600_02', 6)	# 35250-35255
    sprite('ka600_00', 6)	# 35256-35261
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 35262-35267
    sprite('ka600_02', 6)	# 35268-35273
    sprite('ka600_00', 6)	# 35274-35279
    SFX_3('cloth_l')
    sprite('ka600_01', 6)	# 35280-35285
    sprite('ka600_02', 6)	# 35286-35291
    sprite('ka600_03', 6)	# 35292-35297
    sprite('ka600_04', 6)	# 35298-35303
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 35304-35309
    sprite('ka600_06', 6)	# 35310-35315
    sprite('ka600_04', 6)	# 35316-35321
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 35322-35327
    sprite('ka600_06', 6)	# 35328-35333
    sprite('ka600_04', 6)	# 35334-35339
    SFX_3('cloth_l')
    sprite('ka600_05', 6)	# 35340-35345
    sprite('ka600_06', 6)	# 35346-35351
    sprite('ka600_07', 6)	# 35352-35357
    sprite('ka600_08', 6)	# 35358-35363
    sprite('ka600_09', 6)	# 35364-35369
    sprite('ka600_10', 6)	# 35370-35375
    sprite('ka600_11', 6)	# 35376-35381
    sprite('ka600_12', 6)	# 35382-35387
    SFX_3('slash_sword_middle')
    sprite('ka600_13', 6)	# 35388-35393
    sprite('ka600_14', 6)	# 35394-35399
    sprite('ka600_15', 10)	# 35400-35409
    sprite('ka600_16', 6)	# 35410-35415
    SFX_3('ka003')
    label(181)
    sprite('ka000_00', 6)	# 35416-35421
    sprite('ka000_01', 6)	# 35422-35427
    sprite('ka000_02', 6)	# 35428-35433
    sprite('ka000_03', 6)	# 35434-35439
    sprite('ka000_04', 6)	# 35440-35445
    sprite('ka000_05', 6)	# 35446-35451
    sprite('ka000_06', 6)	# 35452-35457
    sprite('ka000_07', 6)	# 35458-35463
    sprite('ka000_08', 6)	# 35464-35469
    sprite('ka000_09', 6)	# 35470-35475
    sprite('ka000_10', 6)	# 35476-35481
    sprite('ka000_11', 6)	# 35482-35487
    if SLOT_97:
        _gotolabel(181)
    sprite('ka000_00', 1)	# 35488-35488
    Unknown21007(24, 40)
    Unknown21011(300)
    label(182)
    sprite('ka000_00', 6)	# 35489-35494
    sprite('ka000_01', 6)	# 35495-35500
    sprite('ka000_02', 6)	# 35501-35506
    sprite('ka000_03', 6)	# 35507-35512
    sprite('ka000_04', 6)	# 35513-35518
    sprite('ka000_05', 6)	# 35519-35524
    sprite('ka000_06', 6)	# 35525-35530
    sprite('ka000_07', 6)	# 35531-35536
    sprite('ka000_08', 6)	# 35537-35542
    sprite('ka000_09', 6)	# 35543-35548
    sprite('ka000_10', 6)	# 35549-35554
    sprite('ka000_11', 6)	# 35555-35560
    gotoLabel(182)
    ExitState()
    label(991)
    sprite('ka000_00', 1)	# 35561-35561
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ka000_00', 6)	# 35562-35567
    sprite('ka000_01', 6)	# 35568-35573
    sprite('ka000_02', 6)	# 35574-35579
    sprite('ka000_03', 6)	# 35580-35585
    sprite('ka000_04', 6)	# 35586-35591
    sprite('ka000_05', 6)	# 35592-35597
    sprite('ka000_06', 6)	# 35598-35603
    sprite('ka000_07', 6)	# 35604-35609
    sprite('ka000_08', 6)	# 35610-35615
    sprite('ka000_09', 6)	# 35616-35621
    sprite('ka000_10', 6)	# 35622-35627
    sprite('ka000_11', 6)	# 35628-35633
    gotoLabel(992)
    label(993)
    sprite('ka033_00', 2)	# 35634-35635

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
    sprite('ka033_01', 3)	# 35636-35638
    label(994)
    sprite('ka033_01', 3)	# 35639-35641
    sprite('ka033_02', 3)	# 35642-35644
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 35645-35647
    ExitState()

@State
def CmnActRoundWin():
    sprite('keep', 32767)	# 1-32767

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
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bjb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    sprite('keep', 1)	# 4-4
    if (not SLOT_158):
        sendToLabel(20)
    if SLOT_108:
        if SLOT_52:
            if (SLOT_25 >= 300000):
                if (SLOT_26 >= 300000):
                    if random_(2, 0, 50):
                        sendToLabel(0)
                    else:
                        sendToLabel(20)
                else:
                    sendToLabel(20)
            else:
                sendToLabel(20)
        elif (SLOT_25 >= 300000):
            if (SLOT_26 >= 300000):
                if random_(2, 0, 33):
                    gotoLabel(10)
                if random_(2, 0, 50):
                    gotoLabel(20)
            elif random_(2, 0, 50):
                sendToLabel(10)
            else:
                sendToLabel(20)
        elif random_(2, 0, 50):
            sendToLabel(10)
        else:
            sendToLabel(20)
    elif SLOT_52:
        if (SLOT_25 >= 300000):
            if (SLOT_26 >= 300000):
                if random_(2, 0, 50):
                    sendToLabel(0)
                else:
                    sendToLabel(20)
            else:
                sendToLabel(20)
        else:
            sendToLabel(20)
    elif (SLOT_25 >= 300000):
        if (SLOT_26 >= 300000):
            if random_(2, 0, 33):
                gotoLabel(10)
            if random_(2, 0, 50):
                gotoLabel(20)
        elif random_(2, 0, 50):
            sendToLabel(10)
        else:
            sendToLabel(20)
    elif random_(2, 0, 50):
        sendToLabel(10)
    else:
        sendToLabel(20)
    label(0)
    sprite('ka610_00', 6)	# 5-10
    sprite('ka610_01', 6)	# 11-16
    sprite('ka610_02', 6)	# 17-22
    sprite('ka610_03', 6)	# 23-28
    sprite('ka610_04', 6)	# 29-34
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 35-40
    sprite('ka610_06', 6)	# 41-46
    sprite('ka610_07', 6)	# 47-52
    sprite('ka610_08', 6)	# 53-58
    sprite('ka610_09', 6)	# 59-64
    sprite('ka610_10', 6)	# 65-70
    sprite('ka610_11', 6)	# 71-76
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 77-82
    sprite('ka610_13', 6)	# 83-88
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pka524', 100, 895576944, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pka402_0', 100, 878799728, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('', 0, 895576944, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(1)
    sprite('ka610_14', 6)	# 89-94
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ka000_00', 5)	# 95-99
    Unknown20000(1)
    if (SLOT_38 == 0):
        if (SLOT_22 > 1300000):
            sendToLabel(5)
        if (SLOT_22 < (-1300000)):
            sendToLabel(6)
    else:
        if (SLOT_22 < (-1300000)):
            sendToLabel(5)
        if (SLOT_22 > 1300000):
            sendToLabel(6)
    label(3)
    sprite('ka611_00', 20)	# 100-119
    GFX_1('ef_font_exclaim', 0)
    sprite('ka611_01', 6)	# 120-125
    if SLOT_108:
        Unknown7006('', 0, 878799728, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('pka522', 100, 895576944, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ka611_02', 6)	# 126-131
    sprite('ka611_03', 6)	# 132-137
    sprite('ka611_04', 6)	# 138-143
    sprite('ka611_05', 9)	# 144-152
    SFX_3('ka003')
    sprite('ka611_06', 9)	# 153-161
    sprite('ka611_07', 9)	# 162-170
    sprite('ka611_05', 6)	# 171-176
    SFX_3('ka003')
    sprite('ka611_06', 6)	# 177-182
    sprite('ka611_07', 6)	# 183-188
    sprite('ka611_05', 9)	# 189-197
    SFX_3('ka003')
    sprite('ka611_06', 9)	# 198-206
    sprite('ka611_07', 9)	# 207-215
    sprite('ka611_05', 6)	# 216-221
    SFX_3('ka003')
    sprite('ka611_06', 6)	# 222-227
    sprite('ka611_07', 6)	# 228-233
    sprite('ka611_08', 6)	# 234-239
    sprite('ka611_09', 6)	# 240-245
    SFX_3('hit_m_fast')
    sprite('ka611_10', 6)	# 246-251
    GFX_0('win2', 100)
    sprite('ka611_11', 6)	# 252-257
    sprite('ka611_12', 15)	# 258-272
    Unknown23018(1)
    label(4)
    sprite('ka611_13', 12)	# 273-284
    sprite('ka611_14', 8)	# 285-292
    sprite('ka611_15', 8)	# 293-300
    sprite('ka611_14', 8)	# 301-308
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('ka003_00', 4)	# 309-312
    Unknown2005()
    sprite('ka003_01', 4)	# 313-316
    sprite('ka003_02', 4)	# 317-320
    label(6)
    sprite('ka030_00', 3)	# 321-323
    physicsXImpulse(5000)
    sprite('ka030_01', 5)	# 324-328
    label(7)
    sprite('ka030_02', 5)	# 329-333
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ka030_03', 5)	# 334-338
    sprite('ka030_04', 5)	# 339-343
    sprite('ka030_05', 5)	# 344-348
    sprite('ka030_06', 5)	# 349-353
    sprite('ka030_07', 5)	# 354-358
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('ka003')
    sprite('ka030_08', 5)	# 359-363
    sprite('ka030_09', 5)	# 364-368
    sprite('ka030_10', 5)	# 369-373
    sprite('ka030_11', 5)	# 374-378
    if (SLOT_22 < 1300000):
        if (SLOT_22 > (-1300000)):
            sendToLabel(8)
    loopRest()
    gotoLabel(7)
    label(8)
    sprite('ka030_00', 3)	# 379-381
    clearUponHandler(3)
    physicsXImpulse(0)
    loopRest()
    gotoLabel(3)
    label(20)
    sprite('ka205_00', 3)	# 382-384
    if SLOT_158:
        if SLOT_52:
            if random_(2, 0, 50):
                SFX_1('pka524')
            else:
                SFX_1('pka525')
        elif SLOT_108:
            SFX_1('pka402_0')
        else:
            SFX_1('pka520')
    sprite('ka205_01', 3)	# 385-387
    sprite('ka205_02', 5)	# 388-392
    Unknown23018(1)
    sprite('ka205_03', 3)	# 393-395
    SFX_3('ka002')
    label(21)
    sprite('ka205_04', 6)	# 396-401
    sprite('ka205_05', 6)	# 402-407
    loopRest()
    gotoLabel(21)
    label(100)
    sprite('ka000_00', 1)	# 408-408
    if (not SLOT_158):
        Unknown2019(-1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('ka000_00', 6)	# 409-414
    sprite('ka000_01', 6)	# 415-420
    sprite('ka000_02', 6)	# 421-426
    sprite('ka000_03', 6)	# 427-432
    sprite('ka000_04', 6)	# 433-438
    sprite('ka000_05', 6)	# 439-444
    sprite('ka000_06', 6)	# 445-450
    sprite('ka000_07', 6)	# 451-456
    sprite('ka000_08', 6)	# 457-462
    sprite('ka000_09', 6)	# 463-468
    sprite('ka000_10', 6)	# 469-474
    sprite('ka000_11', 6)	# 475-480
    gotoLabel(101)
    label(102)
    sprite('ka610_00', 6)	# 481-486
    sprite('ka610_01', 6)	# 487-492
    sprite('ka610_02', 6)	# 493-498
    sprite('ka610_03', 6)	# 499-504
    sprite('ka610_04', 6)	# 505-510
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 511-516
    sprite('ka610_06', 6)	# 517-522
    sprite('ka610_07', 6)	# 523-528
    sprite('ka610_08', 6)	# 529-534
    sprite('ka610_09', 6)	# 535-540
    sprite('ka610_10', 6)	# 541-546
    sprite('ka610_11', 6)	# 547-552
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 553-558
    sprite('ka610_13', 6)	# 559-564
    SFX_1('pka701btg')
    Unknown23018(1)
    label(103)
    sprite('ka610_14', 6)	# 565-570
    loopRest()
    gotoLabel(103)
    label(110)
    sprite('ka000_00', 1)	# 571-571

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ka000_00', 6)	# 572-577
    sprite('ka000_01', 6)	# 578-583
    sprite('ka000_02', 6)	# 584-589
    sprite('ka000_03', 6)	# 590-595
    sprite('ka000_04', 6)	# 596-601
    sprite('ka000_05', 6)	# 602-607
    sprite('ka000_06', 6)	# 608-613
    sprite('ka000_07', 6)	# 614-619
    sprite('ka000_08', 6)	# 620-625
    sprite('ka000_09', 6)	# 626-631
    sprite('ka000_10', 6)	# 632-637
    sprite('ka000_11', 6)	# 638-643
    gotoLabel(111)
    label(112)
    sprite('ka610_00', 6)	# 644-649
    sprite('ka610_01', 6)	# 650-655
    sprite('ka610_02', 6)	# 656-661
    sprite('ka610_03', 6)	# 662-667
    sprite('ka610_04', 6)	# 668-673
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 674-679
    sprite('ka610_06', 6)	# 680-685
    sprite('ka610_07', 6)	# 686-691
    sprite('ka610_08', 6)	# 692-697
    sprite('ka610_09', 6)	# 698-703
    sprite('ka610_10', 6)	# 704-709
    sprite('ka610_11', 6)	# 710-715
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 716-721
    sprite('ka610_13', 6)	# 722-727
    SFX_1('pka701baz')
    Unknown23018(1)
    label(113)
    sprite('ka610_14', 6)	# 728-733
    loopRest()
    gotoLabel(113)
    label(120)
    sprite('ka000_00', 1)	# 734-734
    Unknown2034(0)
    Unknown2053(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ka000_00', 6)	# 735-740
    sprite('ka000_01', 6)	# 741-746
    sprite('ka000_02', 6)	# 747-752
    sprite('ka000_03', 6)	# 753-758
    sprite('ka000_04', 6)	# 759-764
    sprite('ka000_05', 6)	# 765-770
    sprite('ka000_06', 6)	# 771-776
    sprite('ka000_07', 6)	# 777-782
    sprite('ka000_08', 6)	# 783-788
    sprite('ka000_09', 6)	# 789-794
    sprite('ka000_10', 6)	# 795-800
    sprite('ka000_11', 6)	# 801-806
    gotoLabel(121)
    label(122)
    sprite('ka601_10', 6)	# 807-812
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
    SFX_1('pka701bjb')
    Unknown23018(1)
    sprite('ka601_11', 6)	# 813-818
    sprite('ka601_12', 6)	# 819-824
    SFX_3('cloth_l')
    sprite('ka601_13', 6)	# 825-830
    sprite('ka601_14', 6)	# 831-836
    SFX_3('ka002')
    label(123)
    sprite('ka601_12', 6)	# 837-842
    SFX_3('cloth_l')
    sprite('ka601_13', 6)	# 843-848
    sprite('ka601_14', 6)	# 849-854
    loopRest()
    gotoLabel(123)
    label(130)
    sprite('ka001_01', 7)	# 855-861

    def upon_40():
        clearUponHandler(40)
        SFX_1('pka702pbc')
        Unknown23018(1)
    SFX_1('pka700pbc')
    sprite('ka001_02', 7)	# 862-868
    sprite('ka001_03', 7)	# 869-875
    sprite('ka001_04', 7)	# 876-882
    sprite('ka001_05', 7)	# 883-889
    sprite('ka001_06', 7)	# 890-896
    label(131)
    sprite('ka001_07', 1)	# 897-897
    if SLOT_97:
        _gotolabel(131)
    sprite('ka001_07', 32767)	# 898-33664
    Unknown21007(24, 40)
    label(140)
    sprite('ka610_00', 6)	# 33665-33670
    sprite('ka610_01', 6)	# 33671-33676
    sprite('ka610_02', 6)	# 33677-33682
    sprite('ka610_03', 6)	# 33683-33688
    sprite('ka610_04', 6)	# 33689-33694
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 33695-33700
    sprite('ka610_06', 6)	# 33701-33706
    sprite('ka610_07', 6)	# 33707-33712
    sprite('ka610_08', 6)	# 33713-33718
    sprite('ka610_09', 6)	# 33719-33724
    sprite('ka610_10', 6)	# 33725-33730
    sprite('ka610_11', 6)	# 33731-33736
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 33737-33742
    sprite('ka610_13', 6)	# 33743-33748
    SFX_1('pka700pyo')
    label(141)
    sprite('ka610_14', 1)	# 33749-33749
    if SLOT_97:
        _gotolabel(141)
    sprite('ka610_14', 20)	# 33750-33769
    sprite('ka610_14', 1)	# 33770-33770
    Unknown21007(24, 40)
    Unknown21011(300)
    label(142)
    sprite('ka610_14', 6)	# 33771-33776
    gotoLabel(142)
    label(150)
    sprite('ka000_00', 1)	# 33777-33777

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ka000_00', 6)	# 33778-33783
    sprite('ka000_01', 6)	# 33784-33789
    sprite('ka000_02', 6)	# 33790-33795
    sprite('ka000_03', 6)	# 33796-33801
    sprite('ka000_04', 6)	# 33802-33807
    sprite('ka000_05', 6)	# 33808-33813
    sprite('ka000_06', 6)	# 33814-33819
    sprite('ka000_07', 6)	# 33820-33825
    sprite('ka000_08', 6)	# 33826-33831
    sprite('ka000_09', 6)	# 33832-33837
    sprite('ka000_10', 6)	# 33838-33843
    sprite('ka000_11', 6)	# 33844-33849
    gotoLabel(151)
    label(152)
    sprite('ka610_00', 6)	# 33850-33855
    sprite('ka610_01', 6)	# 33856-33861
    sprite('ka610_02', 6)	# 33862-33867
    sprite('ka610_03', 6)	# 33868-33873
    sprite('ka610_04', 6)	# 33874-33879
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 33880-33885
    sprite('ka610_06', 6)	# 33886-33891
    sprite('ka610_07', 6)	# 33892-33897
    sprite('ka610_08', 6)	# 33898-33903
    sprite('ka610_09', 6)	# 33904-33909
    sprite('ka610_10', 6)	# 33910-33915
    sprite('ka610_11', 6)	# 33916-33921
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 33922-33927
    sprite('ka610_13', 6)	# 33928-33933
    SFX_1('pka701pyu')
    Unknown23018(1)
    label(153)
    sprite('ka610_14', 6)	# 33934-33939
    loopRest()
    gotoLabel(153)
    label(160)
    sprite('ka610_00', 6)	# 33940-33945
    sprite('ka610_01', 6)	# 33946-33951
    sprite('ka610_02', 6)	# 33952-33957
    sprite('ka610_03', 6)	# 33958-33963
    sprite('ka610_04', 6)	# 33964-33969
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 33970-33975
    sprite('ka610_06', 6)	# 33976-33981
    sprite('ka610_07', 6)	# 33982-33987
    sprite('ka610_08', 6)	# 33988-33993
    sprite('ka610_09', 6)	# 33994-33999
    sprite('ka610_10', 6)	# 34000-34005
    sprite('ka610_11', 6)	# 34006-34011
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 34012-34017
    sprite('ka610_13', 6)	# 34018-34023
    SFX_1('pka700pna')
    label(161)
    sprite('ka610_14', 1)	# 34024-34024
    if SLOT_97:
        _gotolabel(161)
    sprite('ka610_14', 1)	# 34025-34025
    Unknown21007(24, 40)
    Unknown21011(200)
    label(162)
    sprite('ka610_14', 6)	# 34026-34031
    gotoLabel(162)
    label(170)
    sprite('ka610_00', 6)	# 34032-34037
    sprite('ka610_01', 6)	# 34038-34043
    sprite('ka610_02', 6)	# 34044-34049
    sprite('ka610_03', 6)	# 34050-34055
    sprite('ka610_04', 6)	# 34056-34061
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 34062-34067
    sprite('ka610_06', 6)	# 34068-34073
    sprite('ka610_07', 6)	# 34074-34079
    sprite('ka610_08', 6)	# 34080-34085
    sprite('ka610_09', 6)	# 34086-34091
    sprite('ka610_10', 6)	# 34092-34097
    sprite('ka610_11', 6)	# 34098-34103
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 34104-34109
    sprite('ka610_13', 6)	# 34110-34115
    SFX_1('pka700uca')
    label(171)
    sprite('ka610_14', 1)	# 34116-34116
    if SLOT_97:
        _gotolabel(171)
    sprite('ka610_14', 20)	# 34117-34136
    sprite('ka610_14', 1)	# 34137-34137
    Unknown21007(24, 40)
    Unknown21011(240)
    label(172)
    sprite('ka610_14', 6)	# 34138-34143
    gotoLabel(172)
    label(180)
    sprite('ka610_00', 6)	# 34144-34149
    sprite('ka610_01', 6)	# 34150-34155
    sprite('ka610_02', 6)	# 34156-34161
    sprite('ka610_03', 6)	# 34162-34167
    sprite('ka610_04', 6)	# 34168-34173
    SFX_3('ka003')
    sprite('ka610_05', 6)	# 34174-34179
    sprite('ka610_06', 6)	# 34180-34185
    sprite('ka610_07', 6)	# 34186-34191
    sprite('ka610_08', 6)	# 34192-34197
    sprite('ka610_09', 6)	# 34198-34203
    sprite('ka610_10', 6)	# 34204-34209
    sprite('ka610_11', 6)	# 34210-34215
    SFX_3('chain_move')
    SFX_3('cloth_m')
    sprite('ka610_12', 6)	# 34216-34221
    sprite('ka610_13', 6)	# 34222-34227
    SFX_1('pka700ryn')
    label(181)
    sprite('ka610_14', 1)	# 34228-34228
    if SLOT_97:
        _gotolabel(181)
    sprite('ka610_14', 32767)	# 34229-66995
    Unknown21007(24, 40)
    Unknown21011(180)

@State
def CmnActLose():
    sprite('ka070_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('pka403_0', 100, 878799728, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ka070_01', 6)	# 7-12
    sprite('ka070_02', 2)	# 13-14
    sprite('ka070_03', 32767)	# 15-32781
