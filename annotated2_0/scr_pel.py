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
    Unknown12019('70656c00000000000000000000000000')

@Subroutine
def MatchInit():
    Health(16000)
    WalkFSpeed(7200)
    WalkBSpeed(5400)
    DashFInitialVelocity(16000)
    DashFAccel(100)
    DashFMaxVelocity(20000)
    Unknown12011(1650)
    Unknown12038(28000)
    AirDashBSpeed(22000)
    AirBDashDuration(13)
    Unknown12037(-1650)
    Unknown12024(1)
    Unknown13039(1)
    Unknown2049(1)
    Unknown15018(2000)
    Unknown15019(1500)
    Unknown30093(1, 5, 36, 0, 0)
    Unknown3060('0000000076725f6c61796572310000000000000000000000000000000000000000000000')
    Unknown3061(0, 5)
    Unknown3063(0, 65000)
    Unknown3062(0, 100000)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown15015(28, 30)
    Unknown14015(0, 450000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 500000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 500000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 500000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4AA', 0x6)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 400000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4AAA', 0x6)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 400000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk4AAAA', 0x6)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 400000, -200000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    MoveMaxChainRepeat(3)
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(0, 350000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown15013(2000)
    Unknown14015(0, 450000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x19)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('NmlAtk5BC', 0x2b)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown15023(28)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B2C', 0x28)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown15023(28)
    Unknown15009()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 350000, 150000, 550000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 450000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(0, 450000, -100000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15015(28, 30)
    Unknown14015(0, 600000, -300000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown15013(1)
    Unknown14015(0, 350000, -400000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 350000, -200000, 200000, 1000, 0)
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
    Move_Register('LandAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-50000, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('LandShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(650000, 1200000, -200000, 400000, 250, 0)
    Move_EndRegister()
    Move_Register('LandSetTrapEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(600000, 1500000, -500000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('AirShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(800000, 2000000, -200000, 400000, 250, 0)
    Move_EndRegister()
    Move_Register('AirSetTrapEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AntiAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 450000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('ChargeShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(2000)
    Unknown15012(2000)
    Unknown14015(450000, 1200000, -200000, 400000, 150, 0)
    Move_EndRegister()
    Move_Register('SpecialHeal', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(1)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(1200000, 1500000, -200000, 300000, 500, 0)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateThrow', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3083)
    Unknown15021(1)
    Unknown15012(1)
    Unknown15014(4000)
    Unknown14015(0, 500000, -200000, 200000, 150, 5)
    Move_EndRegister()
    Move_Register('UltimateThrowSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3083)
    Unknown15021(1)
    Unknown15012(1)
    Unknown15014(4000)
    Unknown14015(0, 500000, -200000, 200000, 150, 5)
    Move_EndRegister()
    Move_Register('UltimateCharge', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('UltimateChargeSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(-350000, 850000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4AA', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk4AAA', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk4AAA', 'NmlAtk4AAAA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BBB', 'LandShot', 10000000)
    Unknown15024('NmlAtk5BBB', 'AntiAir', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown15024('NmlAtk2C', 'LandAssault', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtk5BC', 'LandShot', 10000000)
    Unknown15024('NmlAtkAIR5C', 'LandShot', 10000000)
    Unknown15024('NmlAtk5B2C', 'AntiAir', 10000000)
    Unknown12018(0, 'el060_00')
    Unknown12018(1, 'el060_01')
    Unknown12018(2, 'el060_02')
    Unknown12018(3, 'el060_03')
    Unknown12018(4, 'el060_04')
    Unknown12018(5, 'el060_05')
    Unknown12018(6, 'el060_06')
    Unknown12018(7, 'el040_02')
    Unknown12018(8, 'el040_02')
    Unknown12018(9, 'el045_02')
    Unknown12018(10, 'el060_00')
    Unknown12018(11, 'el060_01')
    Unknown12018(12, 'el060_03')
    Unknown12018(13, 'el060_05')
    Unknown12018(14, 'el060_07')
    Unknown12018(15, 'el125_00')
    Unknown12018(16, 'el050_00')
    Unknown12018(17, 'el052_00')
    Unknown12018(18, 'el054_00')
    Unknown12018(19, 'el000_00')
    Unknown12018(20, 'el000_00')
    Unknown12018(25, 'el063_00')
    Unknown12018(26, 'el063_01')
    Unknown12018(27, 'el063_02')
    Unknown12018(28, 'el063_05')
    Unknown12018(29, 'el060_12')
    Unknown12018(24, 'el072_03')
    Unknown7010(0, 'pel000')
    Unknown7010(1, 'pel001')
    Unknown7010(2, 'pel002')
    Unknown7010(3, 'pel003')
    Unknown7010(4, 'pel004')
    Unknown7010(5, 'pel005')
    Unknown7010(6, 'pel006')
    Unknown7010(7, 'pel007')
    Unknown7010(8, 'pel008')
    Unknown7010(9, 'pel009')
    Unknown7010(10, 'pel010')
    Unknown7010(15, 'pel015')
    Unknown7010(16, 'pel016')
    Unknown7010(17, 'pel017')
    Unknown7010(18, 'pel018')
    Unknown7010(19, 'pel019')
    Unknown7010(20, 'pel020')
    Unknown7010(21, 'pel021')
    Unknown7010(22, 'pel022')
    Unknown7010(23, 'pel023')
    Unknown7010(24, 'pel024')
    Unknown7010(25, 'pel025')
    Unknown7010(28, 'pel028')
    Unknown7010(29, 'pel029')
    Unknown7010(30, 'pel030')
    Unknown7010(31, 'pel031')
    Unknown7010(32, 'pel032')
    Unknown7010(33, 'pel033')
    Unknown7010(34, 'pel034')
    Unknown7010(35, 'pel035')
    Unknown7010(36, 'pel036')
    Unknown7010(37, 'pel037')
    Unknown7010(39, 'pel039')
    Unknown7010(42, 'pel042')
    Unknown7010(43, 'pel043')
    Unknown7010(44, 'pel044')
    Unknown7010(45, 'pel045')
    Unknown7010(46, 'pel046')
    Unknown7010(47, 'pel047')
    Unknown7010(48, 'pel048')
    Unknown7010(49, 'pel049')
    Unknown7010(50, 'pel050')
    Unknown7010(52, 'pel052')
    Unknown7010(53, 'pel053')
    Unknown7010(54, 'pel100_0')
    Unknown7010(55, 'pel100_1')
    Unknown7010(56, 'pel100_2')
    Unknown7010(63, 'pel101_0')
    Unknown7010(64, 'pel101_1')
    Unknown7010(65, 'pel101_2')
    Unknown7010(57, 'pel102_0')
    Unknown7010(58, 'pel102_1')
    Unknown7010(59, 'pel102_2')
    Unknown7010(66, 'pel103_0')
    Unknown7010(67, 'pel103_1')
    Unknown7010(68, 'pel103_2')
    Unknown7010(60, 'pel104_0')
    Unknown7010(61, 'pel104_1')
    Unknown7010(62, 'pel104_2')
    Unknown7010(69, 'pel105_0')
    Unknown7010(70, 'pel105_1')
    Unknown7010(71, 'pel105_2')
    Unknown7010(72, 'pel150')
    Unknown7010(73, 'pel151')
    Unknown7010(74, 'pel152')
    Unknown7010(85, 'pel153')
    Unknown7010(87, 'pel154')
    Unknown7010(88, 'pel155')
    Unknown7010(96, 'pel161_0')
    Unknown7010(97, 'pel161_1')
    Unknown7010(92, 'pel162_0')
    Unknown7010(93, 'pel162_1')
    Unknown7010(98, 'pel163_0')
    Unknown7010(99, 'pel163_1')
    Unknown7010(100, 'pel164_0')
    Unknown7010(101, 'pel164_1')
    Unknown7010(105, 'pel165_0')
    Unknown7010(106, 'pel165_1')
    Unknown7010(102, 'pel166_0')
    Unknown7010(103, 'pel166_1')
    Unknown7010(90, 'pel167_0')
    Unknown7010(91, 'pel167_1')
    Unknown7010(107, 'pel168_0')
    Unknown7010(108, 'pel168_1')
    Unknown7010(110, 'pel169_0')
    Unknown7010(111, 'pel169_1')
    Unknown7010(112, 'pel159_0')
    Unknown7010(113, 'pel159_1')
    Unknown7010(94, 'pel402_0')
    Unknown7010(95, 'pel402_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174655468726f7700000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d6174655468726f7753500000000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465436861726765000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465436861726765535000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    Unknown30036('50454c5f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown23003(0, 1, 32, 1, 1, 0, -1, -1)
    Unknown23044(0, 1)
    Unknown23008(0, 0)

@Subroutine
def MatchInit2():
    callSubroutine('CheckKakusei')
    callSubroutine('CheckKakuseiTraining')

@Subroutine
def CheckKakusei():
    if SLOT_158:
        if (not SLOT_42):
            if (not SLOT_4):
                if (SLOT_124 < 3000):
                    if SLOT_IsPlayer2:
                        Unknown58('TRI_PELPowerUp', 2, 67)
                        if (SLOT_67 == 0):
                            SLOT_4 = 1
                            Unknown23008(0, 1)
                            GFX_0('P4U_Cutin_Parent', 100)
                    else:
                        SLOT_4 = 1
                        Unknown23008(0, 1)
                        GFX_0('P4U_Cutin_Parent', 100)
            if SLOT_170:
                Unknown23008(0, 0)

@Subroutine
def CheckKakuseiTraining():
    if SLOT_IsPlayer2:
        Unknown58('TRI_PELPowerUp', 2, 67)
        if (SLOT_67 == 1):
            SLOT_4 = 1
            Unknown23008(0, 1)

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_90:
            Unknown58('TRI_PELPowerUp', 2, 67)
            if (SLOT_67 == 1):
                SLOT_4 = 1
                Unknown23008(0, 1)
            if (SLOT_67 == 2):
                SLOT_4 = 0
                Unknown23008(0, 0)

@Subroutine
def OnActionBegin():
    callSubroutine('CheckKakusei')
    if Unknown23148('CmnActTagBattleWait'):
        if SLOT_170:
            Unknown23008(0, 0)

@State
def CmnActStand():
    label(0)
    sprite('el000_00', 6)	# 1-6
    sprite('el000_01', 6)	# 7-12
    sprite('el000_02', 6)	# 13-18
    sprite('el000_03', 6)	# 19-24
    sprite('el000_04', 6)	# 25-30
    sprite('el000_05', 6)	# 31-36
    sprite('el000_06', 6)	# 37-42
    sprite('el000_07', 6)	# 43-48
    sprite('el000_08', 6)	# 49-54
    sprite('el000_09', 6)	# 55-60
    sprite('el000_10', 6)	# 61-66
    sprite('el000_11', 6)	# 67-72
    sprite('el000_12', 6)	# 73-78
    sprite('el000_13', 6)	# 79-84
    sprite('el000_14', 6)	# 85-90
    sprite('el000_15', 6)	# 91-96
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('el001_00', 6)	# 97-102
    SFX_1('pel000')
    SLOT_88 = 960
    sprite('el001_01', 40)	# 103-142
    sprite('el001_02', 6)	# 143-148
    sprite('el001_03', 6)	# 149-154
    sprite('el001_04', 6)	# 155-160
    sprite('el001_05', 6)	# 161-166
    sprite('el001_06', 6)	# 167-172
    sprite('el001_07', 6)	# 173-178
    sprite('el001_01', 40)	# 179-218
    sprite('el001_02', 6)	# 219-224
    sprite('el001_03', 6)	# 225-230
    sprite('el001_04', 6)	# 231-236
    sprite('el001_05', 6)	# 237-242
    sprite('el001_06', 6)	# 243-248
    sprite('el001_07', 6)	# 249-254
    sprite('el001_01', 40)	# 255-294
    sprite('el001_00', 7)	# 295-301
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('el003_00', 4)	# 1-4
    sprite('el003_01', 4)	# 5-8
    sprite('el003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('el010_00', 4)	# 1-4
    sprite('el010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('el010_02', 6)	# 1-6
    sprite('el010_03', 6)	# 7-12
    sprite('el010_04', 6)	# 13-18
    sprite('el010_05', 6)	# 19-24
    sprite('el010_06', 6)	# 25-30
    sprite('el010_07', 6)	# 31-36
    sprite('el010_08', 6)	# 37-42
    sprite('el010_11', 6)	# 43-48
    sprite('el010_12', 6)	# 49-54
    sprite('el010_13', 6)	# 55-60
    sprite('el010_14', 6)	# 61-66
    sprite('el010_15', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('el013_00', 4)	# 1-4
    sprite('el013_01', 4)	# 5-8
    sprite('el013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('el010_01', 4)	# 1-4
    sprite('el010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('el010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('el020_00', 4)	# 1-4
    sprite('el020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('el020_02', 3)	# 1-3
    sprite('el020_03', 3)	# 4-6
    sprite('el020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('el020_05', 3)	# 1-3
    sprite('el020_06', 3)	# 4-6
    label(0)
    sprite('el020_07', 4)	# 7-10
    sprite('el020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('el010_01', 3)	# 1-3
    sprite('el010_00', 3)	# 4-6

@State
def CmnActLandingStiffLoop():
    sprite('el010_01', 2)	# 1-2
    sprite('el010_02', 32767)	# 3-32769

@State
def CmnActLandingStiffEnd():
    sprite('el010_01', 3)	# 1-3
    sprite('el010_00', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('null', 60)	# 1-60

@State
def CmnActBWalk():
    sprite('el031_00', 5)	# 1-5
    sprite('el031_01', 5)	# 6-10
    label(0)
    sprite('el031_02', 5)	# 11-15
    sprite('el031_03', 5)	# 16-20
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('el031_04', 5)	# 21-25
    sprite('el031_05', 5)	# 26-30
    sprite('el031_06', 5)	# 31-35
    sprite('el031_07', 5)	# 36-40
    sprite('el031_08', 5)	# 41-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('el031_09', 5)	# 46-50
    sprite('el031_10', 5)	# 51-55
    sprite('el031_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('el032_00', 4)	# 1-4
    label(0)
    sprite('el032_01', 4)	# 5-8
    sprite('el032_02', 4)	# 9-12
    sprite('el032_03', 4)	# 13-16
    Unknown8006(100, 1, 1)
    sprite('el032_04', 4)	# 17-20
    sprite('el032_05', 4)	# 21-24
    sprite('el032_06', 4)	# 25-28
    sprite('el032_07', 4)	# 29-32
    Unknown8006(100, 1, 1)
    sprite('el032_08', 4)	# 33-36
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('el032_09', 4)	# 1-4
    sprite('el032_10', 4)	# 5-8

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        setInvincibleFor(7)
        Unknown1084(1)
        Unknown23001(100, 0)
        Unknown23076()
        sendToLabelUpon(2, 1)
        Unknown28(8, '_NEUTRAL')
    sprite('el033_00', 2)	# 1-2
    sprite('el033_01', 3)	# 3-5
    physicsXImpulse(-16000)
    physicsYImpulse(10000)
    setGravity(1150)
    Unknown8002()
    sprite('el033_02', 3)	# 6-8
    label(0)
    sprite('el033_01', 3)	# 9-11
    sprite('el033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el033_03', 3)	# 15-17
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('el033_04', 3)	# 18-20

@State
def CmnActBDashLanding():
    sprite('null', 60)	# 1-60

@State
def CmnActAirFDash():
    sprite('el035_00', 3)	# 1-3
    label(0)
    sprite('el035_01', 3)	# 4-6
    sprite('el035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('el033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('el033_02', 3)	# 4-6
    sprite('el033_01', 3)	# 7-9
    sprite('el033_02', 3)	# 10-12
    sprite('el033_01', 3)	# 13-15
    sprite('el033_02', 3)	# 16-18
    sprite('el033_01', 3)	# 19-21
    sprite('el033_02', 3)	# 22-24
    sprite('el020_05', 3)	# 25-27
    sprite('el020_06', 3)	# 28-30
    label(0)
    sprite('el020_07', 4)	# 31-34
    sprite('el020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('el050_00', 1)	# 1-1
    sprite('el050_01', 1)	# 2-2
    sprite('el050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('el050_01', 1)	# 1-1
    sprite('el050_02', 1)	# 2-2
    sprite('el050_01', 2)	# 3-4
    sprite('el050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('el050_02', 1)	# 1-1
    sprite('el050_03', 1)	# 2-2
    sprite('el050_02', 2)	# 3-4
    sprite('el050_01', 2)	# 5-6
    sprite('el050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('el050_03', 1)	# 1-1
    sprite('el050_04', 1)	# 2-2
    sprite('el050_03', 2)	# 3-4
    sprite('el050_02', 2)	# 5-6
    sprite('el050_01', 2)	# 7-8
    sprite('el050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('el050_04', 1)	# 1-1
    sprite('el050_04', 1)	# 2-2
    sprite('el050_04', 2)	# 3-4
    sprite('el050_03', 2)	# 5-6
    sprite('el050_02', 2)	# 7-8
    sprite('el050_01', 2)	# 9-10
    sprite('el050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('el052_00', 1)	# 1-1
    sprite('el052_01', 1)	# 2-2
    sprite('el052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('el052_01', 1)	# 1-1
    sprite('el052_02', 1)	# 2-2
    sprite('el052_01', 2)	# 3-4
    sprite('el052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('el052_02', 1)	# 1-1
    sprite('el052_03', 1)	# 2-2
    sprite('el052_02', 2)	# 3-4
    sprite('el052_01', 2)	# 5-6
    sprite('el052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('el052_03', 1)	# 1-1
    sprite('el052_04', 1)	# 2-2
    sprite('el052_03', 2)	# 3-4
    sprite('el052_02', 2)	# 5-6
    sprite('el052_01', 2)	# 7-8
    sprite('el052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('el052_04', 1)	# 1-1
    sprite('el052_04', 1)	# 2-2
    sprite('el052_04', 2)	# 3-4
    sprite('el052_03', 2)	# 5-6
    sprite('el052_02', 2)	# 7-8
    sprite('el052_01', 2)	# 9-10
    sprite('el052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('el054_00', 1)	# 1-1
    sprite('el054_01', 1)	# 2-2
    sprite('el054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('el054_01', 1)	# 1-1
    sprite('el054_02', 1)	# 2-2
    sprite('el054_01', 2)	# 3-4
    sprite('el054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('el054_02', 1)	# 1-1
    sprite('el054_03', 1)	# 2-2
    sprite('el054_02', 2)	# 3-4
    sprite('el054_01', 2)	# 5-6
    sprite('el054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('el054_03', 1)	# 1-1
    sprite('el054_04', 1)	# 2-2
    sprite('el054_03', 2)	# 3-4
    sprite('el054_02', 2)	# 5-6
    sprite('el054_01', 2)	# 7-8
    sprite('el054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('el054_04', 1)	# 1-1
    sprite('el054_04', 1)	# 2-2
    sprite('el054_04', 2)	# 3-4
    sprite('el054_03', 2)	# 5-6
    sprite('el054_02', 2)	# 7-8
    sprite('el054_01', 2)	# 9-10
    sprite('el054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('el060_00', 4)	# 1-4
    label(0)
    sprite('el060_01', 4)	# 5-8
    sprite('el060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('el060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('el060_04', 8)	# 1-8
    label(0)
    sprite('el060_05', 4)	# 9-12
    sprite('el060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('el063_05', 6)	# 1-6

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
    sprite('el063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('el063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    sprite('el063_02', 3)	# 1-3
    label(0)
    sprite('el063_03', 4)	# 4-7
    sprite('el063_04', 4)	# 8-11
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('el063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('el060_08', 2)	# 1-2
    sprite('el060_09', 2)	# 3-4
    sprite('el060_10', 2)	# 5-6
    sprite('el060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('el060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('el064_00', 4)	# 1-4
    sprite('el064_01', 4)	# 5-8
    sprite('el064_02', 4)	# 9-12
    sprite('el064_03', 4)	# 13-16

@State
def CmnActVDownUpper():
    sprite('el060_00', 4)	# 1-4
    label(0)
    sprite('el060_01', 4)	# 5-8
    sprite('el060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('el060_03', 4)	# 1-4

@State
def CmnActVDownDown():
    sprite('el060_04', 8)	# 1-8
    label(0)
    sprite('el060_05', 4)	# 9-12
    sprite('el060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('el063_05', 6)	# 1-6

@State
def CmnActBlowoff():
    sprite('el072_00', 3)	# 1-3
    label(0)
    sprite('el072_01', 3)	# 4-6
    sprite('el072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('el074_00', 3)	# 1-3
    sprite('el074_01', 3)	# 4-6
    sprite('el074_02', 3)	# 7-9
    sprite('el074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('null', 60)	# 1-60

@State
def CmnActFreeze():
    sprite('el052_01', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('el072_03', 6)	# 1-6

@State
def CmnActWallBoundDown():
    sprite('el063_00', 3)	# 1-3
    sprite('el063_01', 3)	# 4-6
    sprite('el063_02', 3)	# 7-9
    label(0)
    sprite('el063_03', 3)	# 10-12
    sprite('el063_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('el070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('el070_01', 4)	# 1-4
    sprite('el070_02', 4)	# 5-8
    sprite('el070_03', 4)	# 9-12
    sprite('el070_04', 4)	# 13-16
    sprite('el070_05', 4)	# 17-20
    sprite('el070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('el040_03', 2)	# 1-2
    sprite('el040_02', 2)	# 3-4
    sprite('el040_01', 2)	# 5-6
    sprite('el040_00', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('el020_02', 3)	# 1-3
    sprite('el020_03', 3)	# 4-6
    sprite('el020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('el020_02', 3)	# 1-3
    sprite('el020_03', 3)	# 4-6
    sprite('el020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirN():
    sprite('el020_02', 3)	# 1-3
    sprite('el020_03', 3)	# 4-6
    sprite('el020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandF():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandB():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandN():
    sprite('el112_00', 3)	# 1-3
    sprite('el112_01', 3)	# 4-6
    sprite('el112_02', 3)	# 7-9
    sprite('el112_03', 3)	# 10-12
    sprite('el112_04', 3)	# 13-15
    sprite('el112_05', 3)	# 16-18
    label(0)
    sprite('el020_07', 4)	# 19-22
    sprite('el020_08', 4)	# 23-26
    loopRest()
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('el010_01', 3)	# 1-3
    sprite('el010_00', 3)	# 4-6

@State
def CmnActMidGuardPre():
    sprite('el040_00', 3)	# 1-3
    sprite('el040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('el040_02', 5)	# 1-5
    sprite('el040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('el040_01', 3)	# 1-3
    sprite('el040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('el040_04', 1)	# 1-1
    label(0)
    sprite('el040_02', 5)	# 2-6
    sprite('el040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('el040_01', 3)	# 1-3
    sprite('el040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('el040_00', 3)	# 1-3
    sprite('el040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('el040_02', 5)	# 1-5
    sprite('el040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('el040_01', 3)	# 1-3
    sprite('el040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('el040_04', 1)	# 1-1
    label(0)
    sprite('el040_02', 5)	# 2-6
    sprite('el040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('el040_01', 3)	# 1-3
    sprite('el040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('el043_00', 3)	# 1-3
    sprite('el043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('el043_02', 5)	# 1-5
    sprite('el043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('el043_01', 3)	# 1-3
    sprite('el043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('el043_04', 1)	# 1-1
    label(0)
    sprite('el043_02', 5)	# 2-6
    sprite('el043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('el043_01', 3)	# 1-3
    sprite('el043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('el045_00', 3)	# 1-3
    sprite('el045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('el045_02', 5)	# 1-5
    sprite('el045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('el045_01', 3)	# 1-3
    sprite('el045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('el045_04', 1)	# 1-1
    label(0)
    sprite('el045_02', 5)	# 2-6
    sprite('el045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('el045_01', 3)	# 1-3
    sprite('el045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('el040_04', 2)	# 1-2
    sprite('el040_04', 2)	# 3-4
    sprite('el040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('el040_02', 4)	# 6-9
    sprite('el040_01', 4)	# 10-13
    sprite('el040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('el043_04', 2)	# 1-2
    sprite('el043_04', 2)	# 3-4
    sprite('el043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('el043_02', 4)	# 6-9
    sprite('el043_01', 4)	# 10-13
    sprite('el043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('el045_04', 2)	# 1-2
    sprite('el045_04', 2)	# 3-4
    sprite('el045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('el045_02', 4)	# 6-9
    sprite('el045_01', 4)	# 10-13
    sprite('el045_00', 4)	# 14-17

@State
def CmnActGuardBreakStand():
    sprite('null', 60)	# 1-60

@State
def CmnActGuardBreakCrouch():
    sprite('null', 60)	# 1-60

@State
def CmnActGuardBreakAir():
    sprite('null', 60)	# 1-60

@State
def CmnActAirTurn():
    sprite('el025_02', 1)	# 1-1
    Unknown2005()
    sprite('el025_01', 2)	# 2-3
    sprite('el025_02', 1)	# 4-4
    Unknown2005()

@State
def CmnActLockWait():
    sprite('el040_02', 1)	# 1-1
    sprite('el040_01', 3)	# 2-4
    sprite('el040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('el200_00', 3)	# 1-3
    sprite('el200_01', 3)	# 4-6
    sprite('el200_02', 11)	# 7-17	 **attackbox here**
    GFX_0('elef200_Zanzoh', 100)
    sprite('el200_03', 3)	# 18-20
    sprite('el200_04', 3)	# 21-23
    sprite('el200_05', 3)	# 24-26
    sprite('el200_06', 3)	# 27-29

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
    sprite('null', 60)	# 1-60

@State
def CmnActSlideAir():
    label(0)
    sprite('el077_00', 2)	# 1-2
    sprite('el077_01', 2)	# 3-4
    sprite('el077_10', 2)	# 5-6
    sprite('el077_11', 2)	# 7-8
    sprite('el077_12', 2)	# 9-10
    sprite('el077_13', 2)	# 11-12
    sprite('el077_14', 2)	# 13-14
    sprite('el077_15', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('el077_02', 4)	# 1-4
    label(0)
    sprite('el077_03', 3)	# 5-7
    sprite('el077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('el077_05', 5)	# 1-5
    sprite('el077_06', 4)	# 6-9

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
    label(0)
    sprite('el121_00', 3)	# 1-3
    sprite('el121_01', 3)	# 4-6
    sprite('el121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveLoop():
    sprite('el121_03', 3)	# 1-3
    GFX_0('elef121_Burst', 0)
    label(0)
    sprite('el121_04', 2)	# 4-5
    sprite('el121_05', 2)	# 6-7
    sprite('el121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('el121_07', 4)	# 1-4
    sprite('el033_03', 4)	# 5-8
    sprite('el033_04', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    label(0)
    sprite('el121_00', 3)	# 1-3
    sprite('el121_01', 3)	# 4-6
    sprite('el121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveLoop():
    sprite('el121_03', 3)	# 1-3
    GFX_0('elef121_Burst', 0)
    label(0)
    sprite('el121_04', 2)	# 4-5
    sprite('el121_05', 2)	# 6-7
    sprite('el121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('el121_07', 3)	# 1-3
    sprite('el121_08', 3)	# 4-6
    sprite('el020_05', 3)	# 7-9
    sprite('el020_06', 3)	# 10-12
    label(0)
    sprite('el020_07', 4)	# 13-16
    sprite('el020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PEL_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 1008, 0)
    label(0)
    sprite('el121_00', 3)	# 1-3
    sprite('el121_01', 3)	# 4-6
    sprite('el121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushLoop():
    sprite('el121_03', 3)	# 1-3
    GFX_0('elef121_Burst', 0)
    label(0)
    sprite('el121_04', 2)	# 4-5
    sprite('el121_05', 2)	# 6-7
    sprite('el121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('el121_07', 4)	# 1-4
    sprite('el033_03', 4)	# 5-8
    sprite('el033_04', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PEL_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 1008, 0)
    label(0)
    sprite('el121_00', 3)	# 1-3
    sprite('el121_01', 3)	# 4-6
    sprite('el121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushLoop():
    sprite('el121_03', 3)	# 1-3
    GFX_0('elef121_Burst', 0)
    label(0)
    sprite('el121_04', 2)	# 4-5
    sprite('el121_05', 2)	# 6-7
    sprite('el121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('el121_07', 3)	# 1-3
    sprite('el121_08', 3)	# 4-6
    sprite('el020_05', 3)	# 7-9
    sprite('el020_06', 3)	# 10-12
    label(0)
    sprite('el020_07', 4)	# 13-16
    sprite('el020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PEL_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 1008, 0)
    label(0)
    sprite('el121_00', 3)	# 1-3
    sprite('el121_01', 3)	# 4-6
    sprite('el121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('el121_03', 3)	# 1-3
    label(0)
    sprite('el121_04', 2)	# 4-5
    sprite('el121_05', 2)	# 6-7
    sprite('el121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('el121_07', 2)	# 1-2
    sprite('el033_03', 2)	# 3-4
    sprite('el033_04', 2)	# 5-6

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PEL_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 1008, 0)
    label(0)
    sprite('el121_00', 3)	# 1-3
    sprite('el121_01', 3)	# 4-6
    sprite('el121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('el121_03', 3)	# 1-3
    label(0)
    sprite('el121_04', 2)	# 4-5
    sprite('el121_05', 2)	# 6-7
    sprite('el121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('el121_07', 3)	# 1-3
    sprite('el121_08', 3)	# 4-6
    sprite('el020_05', 3)	# 7-9
    sprite('el020_06', 3)	# 10-12
    label(0)
    sprite('el020_07', 4)	# 13-16
    sprite('el020_08', 4)	# 17-20
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

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 28)	# 603-630
    sprite('null', 1)	# 631-631
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(1200000)
    physicsYImpulse(-240000)
    Unknown2053(1)
    EnableCollision(1)
    sprite('el321_06', 32767)	# 632-33398	 **attackbox here**
    label(1)
    sprite('keep', 3)	# 33399-33401
    sprite('el010_01', 4)	# 33402-33405
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('el010_02', 6)	# 33406-33411
    sprite('el010_03', 4)	# 33412-33415
    sprite('el010_01', 4)	# 33416-33419
    sprite('el010_00', 4)	# 33420-33423

@State
def CmnActChangePartnerQuickIn():
    sprite('el032_07', 4)	# 1-4
    sprite('el032_07', 4)	# 5-8
    sprite('el032_09', 7)	# 9-15
    sprite('el032_09', 7)	# 16-22
    sprite('el032_10', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('el033_01', 3)	# 1-3
    sprite('el033_02', 3)	# 4-6
    sprite('el033_01', 3)	# 7-9
    sprite('el033_02', 3)	# 10-12
    sprite('el033_01', 3)	# 13-15
    sprite('el033_02', 3)	# 16-18
    sprite('el033_01', 3)	# 19-21
    sprite('el033_02', 3)	# 22-24
    sprite('el033_01', 3)	# 25-27
    sprite('el033_02', 3)	# 28-30
    sprite('el033_01', 3)	# 31-33
    sprite('keep', 30)	# 34-63

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('el033_00', 3)	# 1-3
    sprite('el033_01', 3)	# 4-6
    sprite('el033_02', 3)	# 7-9
    label(0)
    sprite('el033_01', 3)	# 10-12
    sprite('el033_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el033_03', 3)	# 16-18
    sprite('el033_04', 3)	# 19-21

@State
def CmnActChangeReturnAppeal():
    sprite('el001_00', 7)	# 1-7
    sprite('el001_01', 10)	# 8-17
    sprite('el001_02', 7)	# 18-24
    sprite('el001_03', 7)	# 25-31
    sprite('el001_04', 7)	# 32-38
    sprite('el001_05', 7)	# 39-45
    sprite('el001_06', 7)	# 46-52
    sprite('el001_07', 7)	# 53-59
    sprite('el001_01', 10)	# 60-69
    sprite('el001_00', 7)	# 70-76

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
    sprite('el020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('el020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('el010_01', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        loopRelated(17, 100)

        def upon_17():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 3013):
                Recovery()
                Unknown2063()
    sprite('el402_00', 4)	# 1-4
    sprite('el402_01', 4)	# 5-8
    if SLOT_4:
        Unknown23029(11, 2503, 0)
        Unknown7007('70656c3230365f3100000000000000006400000070656c3230365f3200000000000000006400000070656c3230375f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown23029(11, 2502, 0)
        Unknown7007('70656c3230365f3000000000000000006400000070656c3230375f3000000000000000006400000070656c3230375f310000000000000000640000000000000000000000000000000000000000000000')
    sprite('el402_02', 4)	# 9-12
    GFX_0('elef402_ply_jio', 0)
    Unknown38(7, 1)
    sprite('el402_02', 2)	# 13-14
    sprite('el402_02', 2)	# 15-16
    sprite('el402_03', 4)	# 17-20
    Unknown13(7)
    label(0)
    sprite('el402_04', 4)	# 21-24
    sprite('el402_05', 4)	# 25-28
    sprite('el402_06', 4)	# 29-32
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el402_07', 4)	# 33-36
    sprite('el402_08', 4)	# 37-40
    sprite('el402_09', 4)	# 41-44

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        loopRelated(17, 65)

        def upon_17():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 3015):
                Recovery()
                Unknown2063()
    sprite('el403_00', 3)	# 1-3
    sprite('el403_01', 4)	# 4-7
    sprite('el403_02', 4)	# 8-11
    if SLOT_4:
        Unknown23029(11, 2505, 0)
        Unknown7007('70656c3230385f3100000000000000006400000070656c3230385f3200000000000000006400000070656c3230395f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown23029(11, 2504, 0)
        Unknown7007('70656c3230385f3000000000000000006400000070656c3230395f3000000000000000006400000070656c3230395f310000000000000000640000000000000000000000000000000000000000000000')
    sprite('el403_03', 4)	# 12-15
    sprite('el403_04', 4)	# 16-19
    GFX_0('elef403_ply_bufu', 0)
    Unknown38(7, 1)
    label(0)
    sprite('el403_05', 4)	# 20-23
    sprite('el403_06', 4)	# 24-27
    sprite('el403_07', 4)	# 28-31
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 32-33
    Unknown13(7)
    sprite('el403_00', 4)	# 34-37

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        loopRelated(17, 85)

        def upon_17():
            sendToLabel(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 1004):
                HitOrBlockCancel('NmlAtk5BB')
                HitOrBlockJumpCancel(1)
            if (SLOT_48 == 2011):
                Recovery()
                Unknown2063()
    sprite('el204_00', 4)	# 1-4
    sprite('el204_01', 4)	# 5-8
    Unknown7007('70656c3132315f3000000000000000006400000070656c3132315f3100000000000000006400000070656c3132305f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23029(11, 2501, 0)
    sprite('el204_02', 4)	# 9-12
    sprite('el204_03', 4)	# 13-16
    callSubroutine('PersonaCard_ON')
    sprite('el204_04', 4)	# 17-20
    callSubroutine('PersonaCard_STOP')
    sprite('el204_05', 4)	# 21-24
    label(0)
    sprite('el204_03', 4)	# 25-28
    sprite('el204_04', 4)	# 29-32
    sprite('el204_05', 4)	# 33-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el204_01', 4)	# 37-40
    callSubroutine('PersonaCard_OFF')
    sprite('el204_00', 4)	# 41-44

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
    Unknown2036(99, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-200000)
    Unknown1019(4)
    label(0)
    sprite('el020_07', 4)	# 3-6
    sprite('el020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateDUOSP')
    else:
        enterState('UltimateDUO')

@State
def UltimateDUO():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 5023):
                enterState('UltimateDUOExe')
    sprite('el433_00', 3)	# 1-3
    sprite('el433_01', 4)	# 4-7
    callSubroutine('PersonaCard_ON')
    Unknown23029(11, 5003, 0)
    sprite('el433_02', 4)	# 8-11
    sprite('el433_00', 4)	# 12-15
    sprite('el433_01', 4)	# 16-19
    sprite('el433_02', 4)	# 20-23
    sprite('el433_00', 4)	# 24-27
    sprite('el433_01', 4)	# 28-31
    sprite('el433_02', 4)	# 32-35
    sprite('el433_00', 4)	# 36-39
    sprite('el433_01', 4)	# 40-43
    sprite('el433_02', 4)	# 44-47
    sprite('el433_03', 4)	# 48-51
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 52-55
    sprite('el433_05', 4)	# 56-59
    sprite('el433_06', 4)	# 60-63
    sprite('el433_07', 4)	# 64-67
    sprite('el433_08', 4)	# 68-71
    sprite('el433_09', 4)	# 72-75
    sprite('el433_10', 4)	# 76-79
    sprite('el433_11', 4)	# 80-83
    setInvincible(0)
    sprite('el433_09', 4)	# 84-87
    sprite('el433_10', 4)	# 88-91
    sprite('el433_11', 4)	# 92-95
    sprite('el433_09', 4)	# 96-99
    sprite('el433_10', 4)	# 100-103
    sprite('el433_12', 4)	# 104-107
    sprite('el433_13', 4)	# 108-111

@State
def UltimateDUOExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)
        loopRelated(17, 157)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('el433_09', 4)	# 1-4
    sprite('el433_10', 4)	# 5-8
    sprite('el433_11', 4)	# 9-12
    sprite('el433_09', 4)	# 13-16
    sprite('el433_10', 4)	# 17-20
    sprite('el433_11', 4)	# 21-24
    sprite('el433_09', 4)	# 25-28
    sprite('el433_10', 4)	# 29-32
    sprite('el433_11', 4)	# 33-36
    sprite('el433_09', 4)	# 37-40
    tag_voice(1, 'pel259_0', 'pel259_1', '', '')
    sprite('el433_10', 4)	# 41-44
    sprite('el433_11', 4)	# 45-48
    label(0)
    sprite('el433_09', 4)	# 49-52
    sprite('el433_10', 4)	# 53-56
    sprite('el433_11', 4)	# 57-60
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 61-62
    sprite('el433_12', 4)	# 63-66
    sprite('el433_13', 4)	# 67-70

@State
def UltimateDUOSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 5024):
                enterState('UltimateDUOSPExe')
    sprite('el433_00', 3)	# 1-3
    sprite('el433_01', 4)	# 4-7
    callSubroutine('PersonaCard_ON')
    Unknown23029(11, 5004, 0)
    sprite('el433_02', 4)	# 8-11
    sprite('el433_00', 4)	# 12-15
    sprite('el433_01', 4)	# 16-19
    sprite('el433_02', 4)	# 20-23
    sprite('el433_00', 4)	# 24-27
    sprite('el433_01', 4)	# 28-31
    sprite('el433_02', 4)	# 32-35
    sprite('el433_00', 4)	# 36-39
    sprite('el433_01', 4)	# 40-43
    sprite('el433_02', 4)	# 44-47
    sprite('el433_03', 4)	# 48-51
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 52-55
    sprite('el433_05', 4)	# 56-59
    sprite('el433_06', 4)	# 60-63
    sprite('el433_07', 4)	# 64-67
    sprite('el433_08', 4)	# 68-71
    sprite('el433_09', 4)	# 72-75
    sprite('el433_10', 4)	# 76-79
    sprite('el433_11', 4)	# 80-83
    setInvincible(0)
    sprite('el433_09', 4)	# 84-87
    sprite('el433_10', 4)	# 88-91
    sprite('el433_11', 4)	# 92-95
    sprite('el433_09', 4)	# 96-99
    sprite('el433_10', 4)	# 100-103
    sprite('el433_12', 4)	# 104-107
    sprite('el433_13', 4)	# 108-111

@State
def UltimateDUOSPExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)
        loopRelated(17, 278)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('el433_09', 4)	# 1-4
    sprite('el433_10', 4)	# 5-8
    sprite('el433_11', 4)	# 9-12
    sprite('el433_09', 4)	# 13-16
    sprite('el433_10', 4)	# 17-20
    sprite('el433_11', 4)	# 21-24
    sprite('el433_09', 4)	# 25-28
    sprite('el433_10', 4)	# 29-32
    sprite('el433_11', 4)	# 33-36
    sprite('el433_09', 4)	# 37-40
    tag_voice(1, 'pel261_0', 'pel261_1', '', '')
    sprite('el433_10', 4)	# 41-44
    sprite('el433_11', 4)	# 45-48
    label(0)
    sprite('el433_09', 4)	# 49-52
    sprite('el433_10', 4)	# 53-56
    sprite('el433_11', 4)	# 57-60
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 61-62
    sprite('el433_12', 4)	# 63-66
    sprite('el433_13', 4)	# 67-70

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
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 8)	# 121-128
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-580000)
    Unknown1007(2900000)
    physicsXImpulse(20000)
    physicsYImpulse(-100000)
    sprite('el320_02', 3)	# 129-131	 **attackbox here**
    sprite('el321_00', 3)	# 132-134
    sprite('el321_01', 3)	# 135-137
    sprite('el321_02', 3)	# 138-140
    sprite('el321_03', 5)	# 141-145
    sprite('el321_04', 3)	# 146-148
    sprite('el321_06', 3)	# 149-151	 **attackbox here**
    sendToLabelUpon(2, 9)
    sprite('el321_06', 32767)	# 152-32918	 **attackbox here**
    sprite('el321_07', 6)	# 32919-32924
    sprite('el321_08', 6)	# 32925-32930
    label(9)
    sprite('keep', 2)	# 32931-32932
    Unknown1019(5)
    sprite('el010_01', 2)	# 32933-32934
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('el010_02', 8)	# 32935-32942
    sprite('el010_03', 8)	# 32943-32950
    sprite('el010_01', 6)	# 32951-32956
    sprite('el010_00', 6)	# 32957-32962

@State
def CmnActChangeReturnAppealBurst():
    sprite('el070_03', 30)	# 1-30
    sprite('el064_02', 5)	# 31-35
    sprite('el064_03', 5)	# 36-40
    sprite('el010_02', 5)	# 41-45
    sprite('el010_01', 5)	# 46-50
    sprite('el010_00', 5)	# 51-55
    sprite('el000_00', 30)	# 56-85

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
    sprite('el321_06', 32767)	# 32-32798	 **attackbox here**
    label(1)
    sprite('keep', 1)	# 32799-32799
    sprite('keep', 1)	# 32800-32800
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    sprite('el010_01', 6)	# 32801-32806
    Unknown8000(100, 1, 1)
    sprite('el010_02', 8)	# 32807-32814
    sprite('el010_03', 5)	# 32815-32819
    sprite('el010_01', 5)	# 32820-32824
    sprite('el010_00', 5)	# 32825-32829

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
        DisableAttackRestOfMove()
    sprite('keep', 1)	# 1-1
    StartMultihit()
    Unknown1084(1)
    sprite('el010_01', 4)	# 2-5
    Unknown8000(100, 1, 1)
    sprite('el010_02', 2)	# 6-7
    sprite('el010_03', 2)	# 8-9
    sprite('el010_01', 3)	# 10-12
    sprite('el010_00', 3)	# 13-15
    sprite('el202_00', 5)	# 16-20
    sprite('el202_01', 5)	# 21-25
    sprite('el202_02', 5)	# 26-30
    sprite('el202_03', 4)	# 31-34	 **attackbox here**
    GFX_0('CardTornade', 0)
    SFX_3('slash_pole_slow')
    sprite('el202_04', 4)	# 35-38	 **attackbox here**
    RefreshMultihit()
    sprite('el202_05', 4)	# 39-42	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el202_06', 4)	# 43-46	 **attackbox here**
    sprite('el202_04', 4)	# 47-50	 **attackbox here**
    sprite('el202_05', 5)	# 51-55	 **attackbox here**
    sprite('el202_06', 5)	# 56-60	 **attackbox here**
    sprite('el202_04', 5)	# 61-65	 **attackbox here**
    sprite('el202_07', 5)	# 66-70
    sprite('el202_08', 4)	# 71-74
    loopRest()

@Subroutine
def PersonaCard_ON():
    GFX_0('elef_cardlight', 0)
    GFX_0('elef_cardlight_add', 0)
    GFX_1('elef_cardlight_add2', 0)

@Subroutine
def PersonaCard_STOP():
    Unknown26('elef_cardlight_add')

@Subroutine
def PersonaCard_OFF():
    Unknown26('elef_cardlight')

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(500)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        Unknown1112('')
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 1003):
                clearUponHandler(43)
                Unknown2037(1)
    sprite('el203_00', 1)	# 1-1
    sprite('el203_01', 3)	# 2-4
    sprite('el203_02', 2)	# 5-6
    sprite('el203_03', 2)	# 7-8
    sprite('el203_04', 2)	# 9-10
    Unknown7009(3)
    sprite('el203_05', 2)	# 11-12
    GFX_0('elef203_CardShot', 0)
    Unknown14070('NmlAtk5AA')
    sprite('el203_06', 3)	# 13-15
    sprite('el203_07', 3)	# 16-18
    sprite('el203_08', 3)	# 19-21
    sprite('el203_06', 3)	# 22-24
    sprite('el203_07', 3)	# 25-27
    sprite('el203_09', 3)	# 28-30
    sprite('el203_10', 2)	# 31-32
    sprite('el203_10', 2)	# 33-34
    Recovery()
    Unknown2063()
    sprite('el203_11', 4)	# 35-38
    sprite('el203_12', 1)	# 39-39
    sprite('el203_12', 3)	# 40-42
    if SLOT_2:
        Unknown14072('NmlAtk5AA')
    sprite('el203_10', 3)	# 43-45
    Unknown23183('656c3230335f3130000000000000000000000000000000000000000000000000040000000200000002000000')
    sprite('el203_11', 3)	# 46-48
    Unknown23183('656c3230335f3131000000000000000000000000000000000000000000000000040000000200000002000000')
    sprite('el203_13', 5)	# 49-53

@Subroutine
def DeriveInput5AA():
    Unknown14070('NmlAtk5AAA')
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk2B')
    Unknown14070('CmnActCrushAttack')
    Unknown14070('NmlAtk2C')
    Unknown14070('NmlAtkThrow')
    Unknown14070('NmlAtkBackThrow')

@Subroutine
def DeriveTiming5AA():
    if SLOT_2:
        Unknown14072('NmlAtk5AAA')
        Unknown14072('NmlAtk5B')
        Unknown14072('NmlAtk2B')
        Unknown14072('CmnActCrushAttack')
        Unknown14072('NmlAtk2C')
        Unknown14072('NmlAtkThrow')
        Unknown14072('NmlAtkBackThrow')

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(200)
        Unknown11092(1)
        AirUntechableTime(22)
        AirPushbackY(10000)
        Hitstop(1)
        PushbackX(7000)
        Unknown9016(1)
        Unknown2037(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2037(1)
    sprite('el201_00', 4)	# 1-4
    sprite('el201_01', 1)	# 5-5	 **attackbox here**
    SFX_3('el002')
    sprite('el201_01', 1)	# 6-6	 **attackbox here**
    sprite('el201_01', 1)	# 7-7	 **attackbox here**
    SFX_3('el002')
    sprite('el201_02', 1)	# 8-8	 **attackbox here**
    sprite('el201_02', 1)	# 9-9	 **attackbox here**
    SFX_3('el002')
    sprite('el201_02', 1)	# 10-10	 **attackbox here**
    sprite('el201_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    SFX_3('el002')
    sprite('el201_03', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('el201_03', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    SFX_3('el002')
    sprite('el201_04', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('el201_04', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    SFX_3('el002')
    callSubroutine('DeriveInput5AA')
    sprite('el201_04', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('el201_05', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    SFX_3('el003')
    sprite('el201_05', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('el201_05', 1)	# 19-19	 **attackbox here**
    RefreshMultihit()
    SFX_3('el003')
    sprite('el201_06', 1)	# 20-20	 **attackbox here**
    callSubroutine('DeriveTiming5AA')
    Recovery()
    Unknown2063()
    sprite('el201_06', 1)	# 21-21	 **attackbox here**
    SFX_3('el003')
    sprite('el201_06', 1)	# 22-22	 **attackbox here**
    sprite('el201_07', 1)	# 23-23	 **attackbox here**
    HitOrBlockJumpCancel(1)
    SFX_3('el003')
    sprite('el201_07', 1)	# 24-24	 **attackbox here**
    sprite('el201_07', 1)	# 25-25	 **attackbox here**
    SFX_3('el003')
    sprite('el201_08', 3)	# 26-28
    sprite('el201_09', 4)	# 29-32
    Unknown2001()
    sprite('el201_10', 4)	# 33-36

@Subroutine
def NmlAtk5AAAInput():
    Unknown14070('NmlAtk5AAAA')
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk2B')
    Unknown14070('CmnActCrushAttack')
    Unknown14070('NmlAtk2C')

@Subroutine
def NmlAtk5AAATiming():
    if SLOT_2:
        Unknown14072('NmlAtk5AAAA')
        Unknown14072('NmlAtk5B')
        Unknown14072('NmlAtk2B')
        Unknown14072('CmnActCrushAttack')
        Unknown14072('NmlAtk2C')

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(250)
        Unknown11092(1)
        AirHitstunAnimation(9)
        AirUntechableTime(27)
        AirPushbackX(0)
        AirPushbackY(10000)
        Unknown30055('f04902006400000064000000')
        PushbackX(12000)
        Hitstop(1)
        Unknown11057(750)
        Unknown9016(1)
        Unknown2037(0)

        def upon_11():
            Unknown2037(1)
        HitOrBlockJumpCancel(1)
    sprite('el202_00', 4)	# 1-4
    sprite('el202_01', 2)	# 5-6
    sprite('el202_02', 2)	# 7-8
    Unknown7009(4)
    sprite('el202_03', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    GFX_0('CardTornade', 0)
    sprite('el202_03', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_slow')
    sprite('el202_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('el202_04', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('el202_04', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    sprite('el202_04', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('el202_05', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('el202_05', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    callSubroutine('NmlAtk5AAAInput')
    sprite('el202_05', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('el202_06', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('el202_06', 1)	# 19-19	 **attackbox here**
    RefreshMultihit()
    sprite('el202_06', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    sprite('el202_04', 1)	# 21-21	 **attackbox here**
    callSubroutine('NmlAtk5AAATiming')
    sprite('el202_04', 2)	# 22-23	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('el202_05', 3)	# 24-26	 **attackbox here**
    sprite('el202_06', 3)	# 27-29	 **attackbox here**
    sprite('el202_04', 3)	# 30-32	 **attackbox here**
    sprite('el202_07', 6)	# 33-38
    Unknown2001()
    sprite('el202_08', 6)	# 39-44

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                SLOT_67 = SLOT_40
                if (SLOT_40 > 100):
                    SLOT_67 = (SLOT_67 / 400)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
                if (SLOT_40 < (-100)):
                    SLOT_67 = (SLOT_67 / 400)
                    if SLOT_38:
                        SLOT_67 = (SLOT_67 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_67)
        Unknown23001(0, 0)
        Unknown23014()
    sprite('el402_00', 3)	# 1-3
    sprite('el402_01', 4)	# 4-7
    Unknown7007('70656c3132335f3100000000000000006400000070656c3132345f3100000000000000006400000070656c3132305f310000000000000000640000000000000000000000000000000000000000000000')
    sprite('el402_01', 1)	# 8-8
    Unknown1084(1)
    Unknown22004(1, 1)
    Unknown23029(11, 3001, 0)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('el402_01', 2)	# 9-10
    sprite('el402_02', 4)	# 11-14
    GFX_0('elef402_ply_garu', 0)
    Unknown38(7, 1)
    sprite('el402_03', 3)	# 15-17
    Unknown13(7)
    setGravity(0)
    physicsYImpulse(1800)
    sprite('el402_03', 3)	# 18-20
    YAccel(200)
    sprite('el402_07', 3)	# 21-23
    YAccel(200)
    sprite('el402_08', 3)	# 24-26
    YAccel(200)
    sprite('el402_09', 3)	# 27-29
    YAccel(105)
    sprite('el402_11', 3)	# 30-32
    sprite('el020_04', 30)	# 33-62
    Unknown2037(1)
    Unknown21007(11, 32)
    YAccel(0)
    sprite('el020_04', 3)	# 63-65
    Unknown1019(50)
    YAccel(50)
    sprite('el020_04', 3)	# 66-68
    clearUponHandler(3)
    Unknown28(2, 'CmnActJumpLanding')
    Recovery()
    Unknown2063()
    sprite('el020_05', 4)	# 69-72
    sprite('el020_06', 4)	# 73-76
    physicsYImpulse(5000)
    Unknown1043()
    label(0)
    sprite('el020_07', 4)	# 77-80
    sprite('el020_08', 4)	# 81-84
    loopRest()
    gotoLabel(0)

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirUntechableTime(18)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk4AA')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('el200_00', 3)	# 1-3
    sprite('el200_00', 1)	# 4-4
    sprite('el200_01', 3)	# 5-7
    SFX_3('slash_knife_fast')
    Unknown7009(0)
    sprite('el200_02', 2)	# 8-9	 **attackbox here**
    GFX_0('elef200_Zanzoh', 100)
    sprite('el200_03', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('el200_04', 3)	# 13-15
    sprite('el200_05', 4)	# 16-19
    sprite('el200_06', 4)	# 20-23

@State
def NmlAtk4AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(300)
        AirUntechableTime(19)
        Hitstop(1)
        Unknown11092(1)
        Unknown9016(1)
        Unknown11057(750)
        AirPushbackY(4000)
        PushbackX(12000)
        Unknown30055('90d003001e0000001e000000')
        Unknown14077(0)
        HitOrBlockCancel('NmlAtk4AAA')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown2037(3)

        def upon_STATE_END():
            if Unknown46(4):
                Unknown13(4)
    sprite('el207_00', 1)	# 1-1
    sprite('el207_01', 1)	# 2-2
    sprite('el207_02', 1)	# 3-3
    sprite('el207_03', 2)	# 4-5
    sprite('el207_04', 2)	# 6-7
    sprite('el207_05', 2)	# 8-9
    sprite('el207_06', 2)	# 10-11	 **attackbox here**
    Unknown7009(4)
    StartMultihit()
    GFX_0('elef207_all', 0)
    Unknown38(4, 1)
    label(0)
    sprite('el207_07', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    SFX_3('el002')
    SFX_3('slash_knife_slow')
    sprite('el207_08', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    SLOT_2 = (SLOT_2 + (-1))
    if (SLOT_2 <= 0):
        Unknown14077(1)
        HitOrBlockJumpCancel(1)
        SLOT_2 = 0
    sprite('keep', 1)	# 15-15
    if SLOT_2:
        _gotolabel(0)
    label(1)
    sprite('el207_09', 3)	# 16-18
    Unknown13(4)
    Recovery()
    Unknown2063()
    sprite('el207_10', 3)	# 19-21
    sprite('el207_11', 3)	# 22-24
    sprite('el207_12', 3)	# 25-27
    sprite('el207_13', 3)	# 28-30
    sprite('el207_14', 3)	# 31-33
    sprite('el207_15', 5)	# 34-38

@State
def NmlAtk4AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        DisableAttackRestOfMove()
        Unknown9016(1)

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(2)
            if (SLOT_48 == 1002):
                JumpCancel_(1)
                HitOrBlockCancel('NmlAtk4AAAA')
    sprite('el208_00', 1)	# 1-1
    sprite('el208_01', 1)	# 2-2
    sprite('el208_02', 1)	# 3-3
    sprite('el208_03', 2)	# 4-5
    sprite('el208_04', 2)	# 6-7
    sprite('el208_05', 2)	# 8-9
    Unknown7009(2)
    sprite('el208_06', 3)	# 10-12	 **attackbox here**
    GFX_0('dmy_el208', 0)
    sprite('el208_07', 3)	# 13-15	 **attackbox here**
    sprite('el208_07ex', 3)	# 16-18	 **attackbox here**
    sprite('el208_06', 3)	# 19-21	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('el208_07', 3)	# 22-24	 **attackbox here**
    sprite('el208_06', 3)	# 25-27	 **attackbox here**
    sprite('el208_07', 3)	# 28-30	 **attackbox here**
    sprite('el208_07ex', 3)	# 31-33	 **attackbox here**
    sprite('el208_08', 5)	# 34-38
    sprite('el208_09', 5)	# 39-43
    ExitState()
    label(2)
    sprite('el208_06', 3)	# 44-46	 **attackbox here**
    sprite('el208_07', 3)	# 47-49	 **attackbox here**
    sprite('el208_07ex', 3)	# 50-52	 **attackbox here**
    sprite('el208_06', 3)	# 53-55	 **attackbox here**
    sprite('el208_07', 3)	# 56-58	 **attackbox here**
    sprite('el208_07ex', 3)	# 59-61	 **attackbox here**
    sprite('el208_06', 3)	# 62-64	 **attackbox here**
    sprite('el208_07', 3)	# 65-67	 **attackbox here**
    sprite('el208_07ex', 3)	# 68-70	 **attackbox here**
    sprite('el208_06', 3)	# 71-73	 **attackbox here**
    sprite('el208_07', 3)	# 74-76	 **attackbox here**
    sprite('el208_07ex', 3)	# 77-79	 **attackbox here**
    sprite('el208_06', 3)	# 80-82	 **attackbox here**
    sprite('el208_07', 3)	# 83-85	 **attackbox here**
    sprite('el208_07ex', 3)	# 86-88	 **attackbox here**
    sprite('el208_06', 3)	# 89-91	 **attackbox here**
    sprite('el208_07', 3)	# 92-94	 **attackbox here**
    sprite('el208_07ex', 3)	# 95-97	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('el208_06', 3)	# 98-100	 **attackbox here**
    sprite('el208_07', 3)	# 101-103	 **attackbox here**
    sprite('el208_07ex', 3)	# 104-106	 **attackbox here**
    sprite('el208_06', 3)	# 107-109	 **attackbox here**
    sprite('el208_07', 3)	# 110-112	 **attackbox here**
    sprite('el208_07ex', 3)	# 113-115	 **attackbox here**
    sprite('el208_06', 3)	# 116-118	 **attackbox here**
    sprite('el208_08', 5)	# 119-123
    sprite('el208_09', 5)	# 124-128

@State
def NmlAtk4AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
        loopRelated(17, 65)

        def upon_17():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 3015):
                Recovery()
                Unknown2063()
    sprite('el403_00', 3)	# 1-3
    sprite('el403_01', 4)	# 4-7
    Unknown7007('70656c3132335f3100000000000000006400000070656c3132345f3100000000000000006400000070656c3132305f310000000000000000640000000000000000000000000000000000000000000000')
    sprite('el403_02', 4)	# 8-11
    if SLOT_4:
        Unknown23029(11, 3006, 0)
    else:
        Unknown23029(11, 3005, 0)
    sprite('el403_03', 4)	# 12-15
    sprite('el403_04', 4)	# 16-19
    GFX_0('elef403_ply_bufu', 0)
    Unknown38(7, 1)
    label(0)
    sprite('el403_05', 4)	# 20-23
    sprite('el403_06', 4)	# 24-27
    sprite('el403_07', 4)	# 28-31
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 32-33
    Unknown13(7)
    sprite('el403_00', 4)	# 34-37

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5BC')
        HitOrBlockCancel('NmlAtk5B2C')
        Unknown1112('')
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 1004):
                HitOrBlockCancel('NmlAtk5BB')
                HitOrBlockCancel('NmlAtk5A')
                HitOrBlockCancel('NmlAtk2B')
                HitOrBlockJumpCancel(1)
            if (SLOT_48 == 2011):
                Recovery()
                Unknown2063()
    sprite('el204_00', 4)	# 1-4
    sprite('el204_01', 4)	# 5-8
    Unknown23029(11, 2001, 0)
    Unknown7007('70656c3132315f3000000000000000006400000070656c3132315f3100000000000000006400000070656c3132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('el204_02', 4)	# 9-12
    sprite('el204_03', 4)	# 13-16
    callSubroutine('PersonaCard_ON')
    sprite('el204_04', 4)	# 17-20
    callSubroutine('PersonaCard_STOP')
    sprite('el204_05', 4)	# 21-24
    sprite('el204_03', 4)	# 25-28
    sprite('el204_04', 4)	# 29-32
    sprite('el204_05', 4)	# 33-36
    sprite('el204_03', 4)	# 37-40
    sprite('el204_04', 4)	# 41-44
    sprite('el204_05', 4)	# 45-48
    sprite('el204_01', 4)	# 49-52
    callSubroutine('PersonaCard_OFF')
    sprite('el204_00', 4)	# 53-56

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5BBB')
        HitOrBlockCancel('NmlAtk5BC')
        HitOrBlockCancel('NmlAtk5B2C')

        def upon_43():
            if (SLOT_48 == 2012):
                Recovery()
                Unknown2063()
    sprite('el232_00', 4)	# 1-4
    sprite('el232_01', 4)	# 5-8
    Unknown23029(11, 2002, 0)
    sprite('el232_02', 4)	# 9-12
    sprite('el232_03', 4)	# 13-16
    callSubroutine('PersonaCard_ON')
    sprite('el232_04', 4)	# 17-20
    callSubroutine('PersonaCard_STOP')
    sprite('el232_05', 4)	# 21-24
    sprite('el232_03', 4)	# 25-28
    sprite('el232_04', 4)	# 29-32
    sprite('el232_05', 4)	# 33-36
    sprite('el232_03', 4)	# 37-40
    sprite('el232_04', 4)	# 41-44
    sprite('el232_05', 4)	# 45-48
    sprite('el232_01', 4)	# 49-52
    callSubroutine('PersonaCard_OFF')
    sprite('el232_00', 4)	# 53-56

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_43():
            if (SLOT_48 == 3013):
                Recovery()
                Unknown2063()
    sprite('el402_00', 4)	# 1-4
    sprite('el402_01', 4)	# 5-8
    Unknown7007('70656c3132335f3000000000000000006400000070656c3132345f3200000000000000006400000070656c3132325f320000000000000000640000000000000000000000000000000000000000000000')
    if SLOT_4:
        Unknown23029(11, 3004, 0)
    else:
        Unknown23029(11, 3003, 0)
    sprite('el402_02', 4)	# 9-12
    GFX_0('elef402_ply_jio', 0)
    Unknown38(7, 1)
    sprite('el402_02', 2)	# 13-14
    sprite('el402_02', 2)	# 15-16
    sprite('el402_03', 4)	# 17-20
    Unknown13(7)
    sprite('el402_04', 4)	# 21-24
    sprite('el402_05', 4)	# 25-28
    sprite('el402_06', 4)	# 29-32
    sprite('el402_04', 4)	# 33-36
    sprite('el402_05', 4)	# 37-40
    sprite('el402_06', 4)	# 41-44
    sprite('el402_04', 4)	# 45-48
    sprite('el402_05', 4)	# 49-52
    sprite('el402_07', 4)	# 53-56
    sprite('el402_08', 4)	# 57-60
    sprite('el402_09', 4)	# 61-64

@State
def NmlAtk5BC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 2013):
                Recovery()
                Unknown2063()
            if (SLOT_48 == 2022):
                Unknown13045(0)
                Unknown23022(1)
                sendToLabel(1)
            if (SLOT_48 == 2029):
                JumpCancel_(1)
    sprite('el205_00', 4)	# 1-4
    sprite('el205_01', 4)	# 5-8
    Unknown23029(11, 2003, 0)
    Unknown7007('70656c3132335f3000000000000000006400000070656c3132345f3000000000000000006400000070656c3132345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('el205_02', 4)	# 9-12
    sprite('el205_03', 4)	# 13-16
    callSubroutine('PersonaCard_ON')
    sprite('el205_04', 4)	# 17-20
    sprite('el205_05', 4)	# 21-24
    sprite('el205_03', 4)	# 25-28
    sprite('el205_04', 4)	# 29-32
    callSubroutine('PersonaCard_STOP')
    sprite('el205_05', 4)	# 33-36
    sprite('el205_03', 4)	# 37-40
    sprite('el205_04', 4)	# 41-44
    sprite('el205_06', 4)	# 45-48
    callSubroutine('PersonaCard_OFF')
    ExitState()
    label(1)
    sprite('el205_04', 6)	# 49-54
    sprite('el205_05', 6)	# 55-60
    sprite('el205_06', 6)	# 61-66
    callSubroutine('PersonaCard_OFF')
    sprite('el001_00', 5)	# 67-71
    sprite('el001_01', 26)	# 72-97
    sprite('el001_02', 5)	# 98-102
    sprite('el001_03', 5)	# 103-107
    sprite('el001_04', 5)	# 108-112
    sprite('el001_05', 5)	# 113-117
    sprite('el001_06', 5)	# 118-122
    sprite('el001_07', 5)	# 123-127
    sprite('el001_01', 26)	# 128-153
    sprite('el001_00', 5)	# 154-158

@State
def NmlAtk5B2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()

        def upon_43():
            if (SLOT_48 == 2014):
                Recovery()
                Unknown2063()
    sprite('el233_00', 4)	# 1-4
    sprite('el233_01', 4)	# 5-8
    Unknown23029(11, 2004, 0)
    Unknown7009(5)
    sprite('el233_02', 4)	# 9-12
    sprite('el233_03', 4)	# 13-16
    callSubroutine('PersonaCard_ON')
    sprite('el233_04', 4)	# 17-20
    sprite('el233_05', 4)	# 21-24
    callSubroutine('PersonaCard_STOP')
    sprite('el233_03', 4)	# 25-28
    sprite('el233_04', 4)	# 29-32
    sprite('el233_05', 4)	# 33-36
    sprite('el233_03', 4)	# 37-40
    sprite('el233_04', 4)	# 41-44
    sprite('el233_05', 4)	# 45-48
    sprite('el233_03', 4)	# 49-52
    sprite('el233_04', 4)	# 53-56
    sprite('el233_00', 4)	# 57-60
    callSubroutine('PersonaCard_OFF')

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(0)
    sprite('el210_00', 2)	# 1-2
    sprite('el210_01', 3)	# 3-5
    sprite('el210_00', 2)	# 6-7
    tag_voice(1, 'pel156_0', 'pel156_1', '', '')
    SFX_3('walk_stone_heavy')
    sprite('el210_00', 3)	# 8-10
    sprite('el210_01', 1)	# 11-11
    sprite('el210_03', 1)	# 12-12
    sprite('el210_04', 2)	# 13-14
    sprite('el210_05', 3)	# 15-17
    physicsXImpulse(20000)
    physicsYImpulse(12000)
    setGravity(3000)
    sprite('el210_06', 3)	# 18-20
    sprite('el210_07', 32767)	# 21-32787
    SFX_3('hit_m_slow')
    label(0)
    sprite('el210_09', 3)	# 32788-32790	 **attackbox here**
    Unknown23054('656c3231305f303800000000000000000000000000000000000000000000000002000000')
    sprite('el210_09', 2)	# 32791-32792	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el210_10', 4)	# 32793-32796
    sprite('el210_11', 4)	# 32797-32800
    sprite('el210_12', 4)	# 32801-32804
    sprite('el210_13', 4)	# 32805-32808

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('el210_09', 6)	# 1-6	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el210_10', 4)	# 7-10
    sprite('el210_11', 4)	# 11-14
    sprite('el210_12', 4)	# 15-18
    sprite('el210_13', 4)	# 19-22
    sprite('el200_00', 3)	# 23-25
    sprite('el200_00', 1)	# 26-26
    sprite('el200_01', 3)	# 27-29
    SFX_3('slash_knife_fast')
    sprite('el200_02', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    GFX_0('elef200_Zanzoh', 100)
    tag_voice(0, 'pel157_0', 'pel157_1', '', '')
    sprite('el200_03', 3)	# 32-34
    sprite('el200_04', 3)	# 35-37
    sprite('el200_05', 3)	# 38-40
    sprite('el200_06', 3)	# 41-43
    sprite('el000_00', 6)	# 44-49
    sprite('el000_01', 6)	# 50-55
    sprite('el000_02', 6)	# 56-61
    sprite('el000_03', 6)	# 62-67
    sprite('el000_04', 6)	# 68-73
    sprite('el000_05', 6)	# 74-79
    sprite('el000_06', 6)	# 80-85
    sprite('el000_07', 6)	# 86-91
    sprite('el000_08', 6)	# 92-97
    sprite('el000_09', 6)	# 98-103
    sprite('el000_10', 6)	# 104-109
    sprite('el000_11', 6)	# 110-115
    sprite('el000_12', 6)	# 116-121
    sprite('el000_13', 6)	# 122-127
    sprite('el000_14', 6)	# 128-133
    sprite('el000_15', 6)	# 134-139
    label(0)
    sprite('el000_00', 6)	# 140-145
    sprite('el000_01', 6)	# 146-151
    sprite('el000_02', 6)	# 152-157
    sprite('el000_03', 6)	# 158-163
    sprite('el000_04', 6)	# 164-169
    sprite('el000_05', 6)	# 170-175
    sprite('el000_06', 6)	# 176-181
    sprite('el000_07', 6)	# 182-187
    sprite('el000_08', 6)	# 188-193
    sprite('el000_09', 6)	# 194-199
    sprite('el000_10', 6)	# 200-205
    sprite('el000_11', 6)	# 206-211
    sprite('el000_12', 6)	# 212-217
    sprite('el000_13', 6)	# 218-223
    sprite('el000_14', 6)	# 224-229
    sprite('el000_15', 6)	# 230-235
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 236-236

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('el231_00', 3)	# 1-3
    sprite('el231_01', 2)	# 4-5
    physicsYImpulse(7500)
    sprite('el231_02', 3)	# 6-8	 **attackbox here**
    SFX_3('hit_l_slow')
    sprite('el231_03', 3)	# 9-11	 **attackbox here**
    setGravity(600)
    sprite('el231_04', 3)	# 12-14	 **attackbox here**
    sprite('el231_05', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('el231_06', 3)	# 18-20	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el231_07', 3)	# 21-23	 **attackbox here**
    sprite('el231_08', 3)	# 24-26	 **attackbox here**
    sprite('el231_09', 3)	# 27-29	 **attackbox here**
    sprite('el231_09add01', 3)	# 30-32
    sprite('el231_10', 7)	# 33-39
    sprite('el010_00', 3)	# 40-42
    sprite('el010_01', 3)	# 43-45
    sprite('el010_00', 3)	# 46-48
    sprite('el000_00', 6)	# 49-54
    sprite('el000_01', 6)	# 55-60
    sprite('el000_02', 6)	# 61-66
    sprite('el000_03', 6)	# 67-72
    sprite('el000_04', 6)	# 73-78
    sprite('el000_05', 6)	# 79-84
    sprite('el000_06', 6)	# 85-90
    sprite('el000_07', 6)	# 91-96
    sprite('el000_08', 6)	# 97-102
    sprite('el000_09', 6)	# 103-108
    sprite('el000_10', 6)	# 109-114
    sprite('el000_11', 6)	# 115-120
    sprite('el000_12', 6)	# 121-126
    sprite('el000_13', 6)	# 127-132
    sprite('el000_14', 6)	# 133-138
    sprite('el000_15', 6)	# 139-144
    label(0)
    sprite('el000_00', 6)	# 145-150
    sprite('el000_01', 6)	# 151-156
    sprite('el000_02', 6)	# 157-162
    sprite('el000_03', 6)	# 163-168
    sprite('el000_04', 6)	# 169-174
    sprite('el000_05', 6)	# 175-180
    sprite('el000_06', 6)	# 181-186
    sprite('el000_07', 6)	# 187-192
    sprite('el000_08', 6)	# 193-198
    sprite('el000_09', 6)	# 199-204
    sprite('el000_10', 6)	# 205-210
    sprite('el000_11', 6)	# 211-216
    sprite('el000_12', 6)	# 217-222
    sprite('el000_13', 6)	# 223-228
    sprite('el000_14', 6)	# 229-234
    sprite('el000_15', 6)	# 235-240
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 241-241

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        DisableAttackRestOfMove()
    sprite('el202_00', 5)	# 1-5
    sprite('el202_01', 5)	# 6-10
    sprite('el202_02', 5)	# 11-15
    tag_voice(0, 'pel158_0', 'pel158_1', '', '')
    sprite('el202_03', 4)	# 16-19	 **attackbox here**
    GFX_0('CardTornade', 0)
    SFX_3('slash_pole_slow')
    sprite('el202_04', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('el202_05', 4)	# 24-27	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el202_06', 4)	# 28-31	 **attackbox here**
    sprite('el202_04', 4)	# 32-35	 **attackbox here**
    sprite('el202_05', 5)	# 36-40	 **attackbox here**
    sprite('el202_06', 5)	# 41-45	 **attackbox here**
    sprite('el202_04', 5)	# 46-50	 **attackbox here**
    sprite('el202_07', 5)	# 51-55
    sprite('el202_08', 5)	# 56-60
    loopRest()

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        DisableAttackRestOfMove()
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('el000_00', 6)	# 1-6
    sprite('el000_01', 6)	# 7-12
    sprite('el000_02', 6)	# 13-18
    sprite('el000_03', 6)	# 19-24
    sprite('el000_04', 6)	# 25-30
    sprite('el000_05', 6)	# 31-36
    sprite('el000_06', 6)	# 37-42
    sprite('el000_07', 6)	# 43-48
    sprite('el000_08', 6)	# 49-54
    sprite('el000_09', 6)	# 55-60
    sprite('el000_10', 6)	# 61-66
    sprite('el000_11', 6)	# 67-72
    sprite('el000_12', 6)	# 73-78
    sprite('el000_13', 6)	# 79-84
    sprite('el000_14', 6)	# 85-90
    sprite('el000_15', 6)	# 91-96
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el202_00', 5)	# 97-101
    sprite('el202_01', 5)	# 102-106
    sprite('el202_02', 5)	# 107-111
    tag_voice(0, 'pel158_0', 'pel158_1', '', '')
    sprite('el202_03', 4)	# 112-115	 **attackbox here**
    GFX_0('CardTornade', 0)
    SFX_3('slash_pole_slow')
    sprite('el202_04', 4)	# 116-119	 **attackbox here**
    RefreshMultihit()
    sprite('el202_05', 4)	# 120-123	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el202_06', 4)	# 124-127	 **attackbox here**
    sprite('el202_04', 4)	# 128-131	 **attackbox here**
    sprite('el202_05', 5)	# 132-136	 **attackbox here**
    sprite('el202_06', 5)	# 137-141	 **attackbox here**
    sprite('el202_04', 5)	# 142-146	 **attackbox here**
    sprite('el202_07', 5)	# 147-151
    sprite('el202_08', 5)	# 152-156
    loopRest()

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        DisableAttackRestOfMove()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown2003(1)
            Unknown1084(1)
            sendToLabel(100)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown30081('')
    sprite('el321_00', 1)	# 26-26
    Unknown1086(22)
    teleportRelativeX(-400000)
    Unknown1007(1100000)
    Unknown1084(1)
    physicsXImpulse(7500)
    physicsYImpulse(-45000)
    Unknown1043()
    sprite('el321_01', 3)	# 27-29
    sprite('el321_02', 3)	# 30-32
    sprite('el321_03', 3)	# 33-35
    sprite('el321_04', 3)	# 36-38
    sprite('el321_04', 3)	# 39-41
    sprite('el321_06', 3)	# 42-44	 **attackbox here**
    RefreshMultihit()
    sprite('el321_06', 32767)	# 45-32811	 **attackbox here**
    DisableAttackRestOfMove()
    label(100)
    sprite('el010_00', 3)	# 32812-32814
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('el010_01', 3)	# 32815-32817
    sprite('el010_00', 3)	# 32818-32820
    sprite('el000_00', 6)	# 32821-32826
    sprite('el000_01', 6)	# 32827-32832
    sprite('el000_02', 6)	# 32833-32838
    sprite('el000_03', 6)	# 32839-32844
    sprite('el000_04', 6)	# 32845-32850
    sprite('el000_05', 6)	# 32851-32856
    sprite('el000_06', 6)	# 32857-32862
    sprite('el000_07', 6)	# 32863-32868
    sprite('el000_08', 6)	# 32869-32874
    sprite('el000_09', 6)	# 32875-32880
    sprite('el000_10', 6)	# 32881-32886
    sprite('el000_11', 6)	# 32887-32892
    sprite('el000_12', 6)	# 32893-32898
    sprite('el000_13', 6)	# 32899-32904
    sprite('el000_14', 6)	# 32905-32910
    sprite('el000_15', 6)	# 32911-32916
    label(0)
    sprite('el000_00', 6)	# 32917-32922
    sprite('el000_01', 6)	# 32923-32928
    sprite('el000_02', 6)	# 32929-32934
    sprite('el000_03', 6)	# 32935-32940
    sprite('el000_04', 6)	# 32941-32946
    sprite('el000_05', 6)	# 32947-32952
    sprite('el000_06', 6)	# 32953-32958
    sprite('el000_07', 6)	# 32959-32964
    sprite('el000_08', 6)	# 32965-32970
    sprite('el000_09', 6)	# 32971-32976
    sprite('el000_10', 6)	# 32977-32982
    sprite('el000_11', 6)	# 32983-32988
    sprite('el000_12', 6)	# 32989-32994
    sprite('el000_13', 6)	# 32995-33000
    sprite('el000_14', 6)	# 33001-33006
    sprite('el000_15', 6)	# 33007-33012
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 33013-33013

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('el211_00', 3)	# 1-3
    sprite('el211_01', 2)	# 4-5
    sprite('el211_02', 2)	# 6-7	 **attackbox here**
    sprite('el211_03', 2)	# 8-9	 **attackbox here**
    sprite('el211_04', 2)	# 10-11	 **attackbox here**
    SFX_3('slash_knife_middle')
    sprite('el211_05', 3)	# 12-14	 **attackbox here**
    sprite('el211_06', 4)	# 15-18	 **attackbox here**
    sprite('el211_07', 4)	# 19-22	 **attackbox here**
    sprite('el211_08', 4)	# 23-26	 **attackbox here**
    sprite('el211_09', 1)	# 27-27	 **attackbox here**
    SFX_3('el003')
    sprite('el211_09', 1)	# 28-28	 **attackbox here**
    sprite('el211_09', 1)	# 29-29	 **attackbox here**
    SFX_3('el003')
    sprite('el211_10', 1)	# 30-30	 **attackbox here**
    sprite('el211_10', 1)	# 31-31	 **attackbox here**
    SFX_3('el003')
    sprite('el211_10', 1)	# 32-32	 **attackbox here**
    sprite('el211_10', 1)	# 33-33	 **attackbox here**
    SFX_3('el003')
    sprite('el000_00', 6)	# 34-39
    sprite('el000_01', 6)	# 40-45
    sprite('el000_02', 6)	# 46-51
    sprite('el000_03', 6)	# 52-57
    sprite('el000_04', 6)	# 58-63
    sprite('el000_05', 6)	# 64-69
    sprite('el000_06', 6)	# 70-75
    sprite('el000_07', 6)	# 76-81
    sprite('el000_08', 6)	# 82-87
    sprite('el000_09', 6)	# 88-93
    sprite('el000_10', 6)	# 94-99
    sprite('el000_11', 6)	# 100-105
    sprite('el000_12', 6)	# 106-111
    sprite('el000_13', 6)	# 112-117
    sprite('el000_14', 6)	# 118-123
    sprite('el000_15', 6)	# 124-129
    label(0)
    sprite('el000_00', 6)	# 130-135
    sprite('el000_01', 6)	# 136-141
    sprite('el000_02', 6)	# 142-147
    sprite('el000_03', 6)	# 148-153
    sprite('el000_04', 6)	# 154-159
    sprite('el000_05', 6)	# 160-165
    sprite('el000_06', 6)	# 166-171
    sprite('el000_07', 6)	# 172-177
    sprite('el000_08', 6)	# 178-183
    sprite('el000_09', 6)	# 184-189
    sprite('el000_10', 6)	# 190-195
    sprite('el000_11', 6)	# 196-201
    sprite('el000_12', 6)	# 202-207
    sprite('el000_13', 6)	# 208-213
    sprite('el000_14', 6)	# 214-219
    sprite('el000_15', 6)	# 220-225
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 226-226

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        DisableAttackRestOfMove()
    sprite('el202_00', 5)	# 1-5
    sprite('el202_01', 5)	# 6-10
    sprite('el202_02', 5)	# 11-15
    sprite('el202_03', 4)	# 16-19	 **attackbox here**
    GFX_0('CardTornade', 0)
    SFX_3('slash_pole_slow')
    sprite('el202_04', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('el202_05', 4)	# 24-27	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el202_06', 4)	# 28-31	 **attackbox here**
    sprite('el202_04', 4)	# 32-35	 **attackbox here**
    sprite('el202_05', 5)	# 36-40	 **attackbox here**
    sprite('el202_06', 5)	# 41-45	 **attackbox here**
    sprite('el202_04', 5)	# 46-50	 **attackbox here**
    sprite('el202_07', 5)	# 51-55
    sprite('el202_08', 5)	# 56-60
    loopRest()

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        DisableAttackRestOfMove()
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('el000_00', 6)	# 1-6
    sprite('el000_01', 6)	# 7-12
    sprite('el000_02', 6)	# 13-18
    sprite('el000_03', 6)	# 19-24
    sprite('el000_04', 6)	# 25-30
    sprite('el000_05', 6)	# 31-36
    sprite('el000_06', 6)	# 37-42
    sprite('el000_07', 6)	# 43-48
    sprite('el000_08', 6)	# 49-54
    sprite('el000_09', 6)	# 55-60
    sprite('el000_10', 6)	# 61-66
    sprite('el000_11', 6)	# 67-72
    sprite('el000_12', 6)	# 73-78
    sprite('el000_13', 6)	# 79-84
    sprite('el000_14', 6)	# 85-90
    sprite('el000_15', 6)	# 91-96
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el202_00', 5)	# 97-101
    sprite('el202_01', 5)	# 102-106
    sprite('el202_02', 5)	# 107-111
    sprite('el202_03', 4)	# 112-115	 **attackbox here**
    GFX_0('CardTornade', 0)
    SFX_3('slash_pole_slow')
    sprite('el202_04', 4)	# 116-119	 **attackbox here**
    RefreshMultihit()
    sprite('el202_05', 4)	# 120-123	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('el202_06', 4)	# 124-127	 **attackbox here**
    sprite('el202_04', 4)	# 128-131	 **attackbox here**
    sprite('el202_05', 5)	# 132-136	 **attackbox here**
    sprite('el202_06', 5)	# 137-141	 **attackbox here**
    sprite('el202_04', 5)	# 142-146	 **attackbox here**
    sprite('el202_07', 5)	# 147-151
    sprite('el202_08', 5)	# 152-156
    loopRest()

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AirUntechableTime(18)
        AttackP1(90)
        Unknown9016(1)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('el230_00', 2)	# 1-2
    sprite('el230_01', 2)	# 3-4
    sprite('el230_02', 2)	# 5-6
    SFX_3('slash_knife_fast')
    sprite('el230_03', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    Unknown7009(0)
    sprite('el230_04', 6)	# 9-14
    Recovery()
    Unknown2063()
    sprite('el230_02', 4)	# 15-18
    sprite('el230_01', 4)	# 19-22

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(70)
        AirUntechableTime(23)
        Hitstop(7)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(0)
    sprite('el231_00', 3)	# 1-3
    sprite('el231_01', 2)	# 4-5
    physicsYImpulse(7500)
    Unknown7007('70656c3130365f3000000000000000006400000070656c3130365f3100000000000000006400000070656c3130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('el231_02', 3)	# 6-8	 **attackbox here**
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    SFX_3('hit_l_slow')
    sprite('el231_03', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    setGravity(600)
    sprite('el231_04', 3)	# 12-14	 **attackbox here**
    sprite('el231_05', 3)	# 15-17	 **attackbox here**
    sprite('el231_06', 3)	# 18-20	 **attackbox here**
    sprite('el231_07', 3)	# 21-23	 **attackbox here**
    sprite('el231_08', 3)	# 24-26	 **attackbox here**
    sprite('el231_09', 3)	# 27-29	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('el231_09add01', 4)	# 30-33
    setInvincible(0)
    sprite('el231_10', 8)	# 34-41
    label(0)
    sprite('el232_00', 5)	# 42-46
    sprite('el232_00', 5)	# 47-51

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(40)
        Unknown9016(1)
        AirPushbackY(20000)
    sprite('el211_00', 2)	# 1-2
    sprite('el211_01', 1)	# 3-3
    sprite('el211_01', 1)	# 4-4
    sprite('el211_02', 1)	# 5-5	 **attackbox here**
    Unknown7007('70656c3130375f3000000000000000006400000070656c3130375f3100000000000000006400000070656c3130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('el211_02', 1)	# 6-6	 **attackbox here**
    sprite('el211_03', 1)	# 7-7	 **attackbox here**
    sprite('el211_03', 1)	# 8-8	 **attackbox here**
    sprite('el211_04', 1)	# 9-9	 **attackbox here**
    SFX_3('slash_knife_middle')
    sprite('el211_04', 1)	# 10-10	 **attackbox here**
    sprite('el211_05', 3)	# 11-13	 **attackbox here**
    sprite('el211_06', 4)	# 14-17	 **attackbox here**
    sprite('el211_07', 4)	# 18-21	 **attackbox here**
    sprite('el211_08', 4)	# 22-25	 **attackbox here**
    sprite('el211_09', 2)	# 26-27	 **attackbox here**
    SFX_3('el003')
    Recovery()
    Unknown2063()
    sprite('el211_09', 2)	# 28-29	 **attackbox here**
    SFX_3('el003')
    sprite('el211_10', 2)	# 30-31	 **attackbox here**
    SFX_3('el003')
    sprite('el211_10', 2)	# 32-33	 **attackbox here**
    SFX_3('el003')

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_STATE_END():
            Unknown1043()
    sprite('el251_00', 2)	# 1-2
    sprite('el251_01', 2)	# 3-4
    sprite('el251_02', 3)	# 5-7
    Unknown7009(1)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('el251_03', 2)	# 8-9
    sprite('el251_04', 2)	# 10-11
    GFX_0('elef251_CardShotAir', 0)
    sprite('el251_05', 2)	# 12-13
    sprite('el251_06', 2)	# 14-15
    sprite('el251_07', 2)	# 16-17
    sprite('el251_08', 2)	# 18-19
    Unknown1018()
    Unknown1023()
    Unknown1038()
    sprite('el251_06', 2)	# 20-21
    sprite('el251_09', 4)	# 22-25
    sprite('el251_10', 4)	# 26-29
    sprite('el251_11', 2)	# 30-31
    Recovery()
    Unknown2063()
    sprite('el251_11', 2)	# 32-33
    sprite('el251_09', 4)	# 34-37
    sprite('el251_12', 5)	# 38-42

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('el250_00', 2)	# 1-2
    sprite('el250_01', 2)	# 3-4
    sprite('el250_02', 2)	# 5-6
    SFX_3('slash_knife_fast')
    sprite('el250_03', 3)	# 7-9	 **attackbox here**
    RefreshMultihit()
    sprite('el250_04', 2)	# 10-11
    Recovery()
    Unknown2063()
    sprite('el250_05', 3)	# 12-14
    sprite('el250_01', 3)	# 15-17
    sprite('el250_00', 3)	# 18-20

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_43():
            if (SLOT_48 == 2015):
                Recovery()
                Unknown2063()
    sprite('el254_00', 3)	# 1-3
    sprite('el254_01', 4)	# 4-7
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown23029(11, 2005, 0)
    Unknown7007('70656c3132315f3100000000000000006400000070656c3132315f3200000000000000006400000070656c3132325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('el254_02', 4)	# 8-11
    sprite('el254_03', 4)	# 12-15
    callSubroutine('PersonaCard_ON')
    sprite('el254_04', 4)	# 16-19
    callSubroutine('PersonaCard_STOP')
    sprite('el254_05', 4)	# 20-23
    sprite('el254_03', 4)	# 24-27
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(40)
    YAccel(40)
    sprite('el254_04', 4)	# 28-31
    sprite('el254_05', 4)	# 32-35
    sprite('el254_01', 4)	# 36-39
    callSubroutine('PersonaCard_OFF')
    sprite('el254_00', 4)	# 40-43

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 2016):
                Recovery()
                Unknown2063()
            if (SLOT_48 == 2025):

                def upon_LANDING():
                    clearUponHandler(2)
                    Unknown1084(1)
                    sendToLabel(20)
                Unknown13045(0)
                Unknown23022(1)
                sendToLabel(1)
            if (SLOT_48 == 2029):
                JumpCancel_(1)
    sprite('el255_00', 3)	# 1-3
    sprite('el255_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown22004(10, 1)
    sprite('el255_02', 3)	# 7-9
    Unknown7007('70656c3132335f3000000000000000006400000070656c3132345f3000000000000000006400000070656c3132345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('el255_03', 4)	# 10-13
    callSubroutine('PersonaCard_ON')
    sprite('el255_04', 4)	# 14-17
    Unknown23029(11, 2006, 0)
    sprite('el255_05', 4)	# 18-21
    sprite('el255_03', 4)	# 22-25
    callSubroutine('PersonaCard_STOP')
    sprite('el255_04', 4)	# 26-29
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    sprite('el255_05', 4)	# 30-33
    sprite('el255_03', 4)	# 34-37
    sprite('el255_00', 4)	# 38-41
    callSubroutine('PersonaCard_OFF')
    sprite('el020_05', 3)	# 42-44
    sprite('el020_06', 3)	# 45-47
    label(0)
    sprite('el020_07', 3)	# 48-50
    sprite('el020_08', 3)	# 51-53
    gotoLabel(0)
    ExitState()
    label(1)
    sprite('keep', 2)	# 54-55
    callSubroutine('PersonaCard_STOP')
    sprite('el255_00', 4)	# 56-59
    callSubroutine('PersonaCard_OFF')
    Unknown1018()
    Unknown1019(85)
    physicsYImpulse(15000)
    Unknown1043()
    sprite('el020_05', 3)	# 60-62
    sprite('el020_06', 3)	# 63-65
    label(11)
    sprite('el020_07', 4)	# 66-69
    sprite('el020_08', 4)	# 70-73
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('el010_01', 3)	# 74-76
    sprite('el010_00', 3)	# 77-79
    sprite('el001_00', 5)	# 80-84
    sprite('el001_01', 26)	# 85-110
    sprite('el001_02', 5)	# 111-115
    sprite('el001_03', 5)	# 116-120
    sprite('el001_04', 5)	# 121-125
    sprite('el001_05', 5)	# 126-130
    sprite('el001_06', 5)	# 131-135
    sprite('el001_07', 5)	# 136-140
    sprite('el001_01', 26)	# 141-166
    sprite('el001_00', 5)	# 167-171
    ExitState()

@Subroutine
def ThrowApproachInit():
    physicsXImpulse(7200)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_18 == 7):
            Unknown8007(100, 1, 1)
            physicsXImpulse(16000)
        if (SLOT_18 >= 7):
            Unknown1015(100)
            if (SLOT_12 >= 20000):
                SLOT_12 = 20000
        if (SLOT_18 >= 25):
            sendToLabel(1)
        if (SLOT_18 >= 3):
            if (SLOT_19 < 180000):
                sendToLabel(1)

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('el032_00', 3)	# 1-3
    label(0)
    sprite('el032_01', 4)	# 4-7
    sprite('el032_02', 4)	# 8-11
    sprite('el032_03', 4)	# 12-15
    Unknown8006(100, 1, 1)
    sprite('el032_04', 4)	# 16-19
    sprite('el032_05', 4)	# 20-23
    sprite('el032_06', 4)	# 24-27
    sprite('el032_07', 4)	# 28-31
    Unknown8006(100, 1, 1)
    sprite('el032_08', 4)	# 32-35
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el310_00', 2)	# 36-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('el310_01', 1)	# 38-38
    sprite('el310_02', 3)	# 39-41	 **attackbox here**
    Unknown1084(1)
    sprite('el310_03', 3)	# 42-44
    SFX_1('pel154')
    sprite('el310_04', 8)	# 45-52
    sprite('el310_03', 4)	# 53-56
    sprite('el310_01', 4)	# 57-60
    sprite('el310_00', 4)	# 61-64

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirPushbackX(45000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        YImpluseBeforeWallbounce(1400)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9178(1)
        WallbounceReboundTime(25)
        Unknown9366(9)
    sprite('el310_02', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('el400_07', 1)	# 4-4	 **attackbox here**
    StartMultihit()
    GFX_0('elef400_HandAuraSuccess', 0)
    GFX_0('elef400_Soul', 2)
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('magiccircle_a')
    Unknown7007('70656c3230305f3000000000000000006400000070656c3230305f3100000000000000006400000070656c3230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('el401_00', 4)	# 5-8
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_01', 36)	# 9-44
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_02', 4)	# 45-48
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_03', 18)	# 49-66
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown26('elef400_Soul')
    sprite('el401_04', 4)	# 67-70
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_05', 4)	# 71-74
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_06', 4)	# 75-78
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_07', 4)	# 79-82
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_3('hit_l_fast')
    sprite('el401_08', 4)	# 83-86
    if random_(2, 0, 25):
        GFX_0('elef400_EnemyCard_LOVERS', 1)
    elif random_(2, 0, 33):
        GFX_0('elef400_EnemyCard_DEATH', 1)
    elif random_(2, 0, 50):
        GFX_0('elef400_EnemyCard_DEVIL', 1)
    else:
        GFX_0('elef400_EnemyCard_TOWER', 1)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_09', 4)	# 87-90
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_10', 4)	# 91-94
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_11', 4)	# 95-98
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_09', 4)	# 99-102
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_10', 4)	# 103-106
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_11', 4)	# 107-110
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el401_09', 4)	# 111-114
    sprite('el401_10', 4)	# 115-118
    sprite('el401_11', 4)	# 119-122
    sprite('el401_09', 4)	# 123-126
    sprite('el401_10', 4)	# 127-130
    sprite('el401_11', 4)	# 131-134
    sprite('el311_12', 4)	# 135-138	 **attackbox here**
    RefreshMultihit()
    Unknown5005(1)
    Unknown36(22)
    Unknown3038(0)
    Unknown3001(255)
    Unknown35()
    sprite('el311_12', 21)	# 139-159	 **attackbox here**

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('el032_00', 3)	# 1-3
    label(0)
    sprite('el032_01', 4)	# 4-7
    sprite('el032_02', 4)	# 8-11
    sprite('el032_03', 4)	# 12-15
    Unknown8006(100, 1, 1)
    sprite('el032_04', 4)	# 16-19
    sprite('el032_05', 4)	# 20-23
    sprite('el032_06', 4)	# 24-27
    sprite('el032_07', 4)	# 28-31
    Unknown8006(100, 1, 1)
    sprite('el032_08', 4)	# 32-35
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el310_00', 2)	# 36-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('el310_01', 1)	# 38-38
    sprite('el310_02', 3)	# 39-41	 **attackbox here**
    Unknown1084(1)
    sprite('el310_03', 3)	# 42-44
    SFX_1('pel154')
    sprite('el310_04', 8)	# 45-52
    sprite('el310_03', 4)	# 53-56
    sprite('el310_01', 4)	# 57-60
    sprite('el310_00', 4)	# 61-64

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        Damage(2000)
        AttackP2(50)
        AirPushbackX(45000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        YImpluseBeforeWallbounce(1400)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9178(1)
        WallbounceReboundTime(25)
        Unknown9366(9)
        Unknown13021(1)
        Unknown21005(1)
    sprite('el310_02', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('el311_00', 3)	# 4-6
    Unknown2005()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000008000000')
    GFX_0('elef311_GuruGuru', 0)
    SFX_3('magiccircle_b')
    SFX_1('pel153')
    sprite('el311_01', 4)	# 7-10
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_02', 4)	# 11-14
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_03', 4)	# 15-18
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_04', 4)	# 19-22
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_05', 4)	# 23-26
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_01', 4)	# 27-30
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_3('magiccircle_b')
    sprite('el311_02', 4)	# 31-34
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_03', 4)	# 35-38
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_04', 4)	# 39-42
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_05', 4)	# 43-46
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_06', 4)	# 47-50
    sprite('el311_07', 20)	# 51-70
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('el311_09', 7)	# 71-77	 **attackbox here**
    RefreshMultihit()
    Unknown21012('656c65663331315f47757275477572750000000000000000000000000000000020000000')
    sprite('el311_09', 4)	# 78-81	 **attackbox here**
    sprite('el311_10', 4)	# 82-85
    sprite('el311_11', 4)	# 86-89
    sprite('el311_10', 4)	# 90-93
    sprite('el311_11', 4)	# 94-97
    sprite('el311_12', 4)	# 98-101	 **attackbox here**

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11063(1)
        Unknown1051(30)
        GuardPoint_(1)
        Unknown22031(-1, 17)

        def upon_42():
            Unknown23022(1)
            ScreenShake(8000, 2000)
            enterState('CmnActInvincibleAttackGrip')
    sprite('el406_00', 3)	# 1-3
    GFX_0('elef406', 103)
    Unknown38(6, 1)
    Unknown8000(100, 1, 1)
    sprite('el406_01', 3)	# 4-6
    Unknown1084(1)
    SFX_3('el001')
    sprite('el406_02', 3)	# 7-9
    sprite('el406_01', 3)	# 10-12
    sprite('el406_02', 3)	# 13-15
    sprite('el406_01', 3)	# 16-18
    sprite('el406_02', 3)	# 19-21
    sprite('el406_01', 3)	# 22-24
    sprite('el406_02', 1)	# 25-25
    Unknown23029(6, 1007, 0)
    sprite('el406_03', 2)	# 26-27
    setInvincible(0)
    tag_voice(1, 'pel264_0', 'pel264_1', '', '')
    sprite('el406_04', 2)	# 28-29
    SFX_3('walk_marble_heavy')
    sprite('el406_05', 2)	# 30-31
    GFX_1('elef_cardshotcrash05', 0)
    Unknown13(6)
    sprite('el406_06', 2)	# 32-33
    sprite('el406_07', 3)	# 34-36
    sprite('el406_08', 3)	# 37-39
    clearUponHandler(42)
    Unknown8000(100, 1, 1)
    sprite('el406_10', 3)	# 40-42
    sprite('el406_11', 3)	# 43-45

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11063(1)
        Unknown1051(30)
        GuardPoint_(1)
        Unknown22031(-1, 17)

        def upon_42():
            Unknown23022(1)
            ScreenShake(8000, 2000)
            enterState('CmnActInvincibleAttackGrip')

        def upon_LANDING():
            clearUponHandler(2)
            clearUponHandler(42)
            Unknown8000(100, 1, 1)
            sendToLabel(0)
    sprite('el406_00', 3)	# 1-3
    GFX_0('elef406', 103)
    Unknown38(6, 1)
    physicsYImpulse(6000)
    setGravity(0)
    sprite('el406_01', 3)	# 4-6
    Unknown1084(1)
    SFX_3('el001')
    sprite('el406_02', 3)	# 7-9
    sprite('el406_01', 3)	# 10-12
    sprite('el406_02', 3)	# 13-15
    sprite('el406_01', 3)	# 16-18
    sprite('el406_02', 3)	# 19-21
    sprite('el406_01', 3)	# 22-24
    sprite('el406_02', 1)	# 25-25
    Unknown23029(6, 1007, 0)
    sprite('el406_03', 2)	# 26-27
    setInvincible(0)
    tag_voice(1, 'pel264_0', 'pel264_1', '', '')
    sprite('el406_04', 2)	# 28-29
    SFX_3('walk_marble_heavy')
    sprite('el406_05', 2)	# 30-31
    GFX_1('elef_cardshotcrash05', 0)
    Unknown13(6)
    sprite('el406_06', 3)	# 32-34
    sprite('el406_07', 3)	# 35-37
    setGravity(1800)
    sprite('el406_08', 32767)	# 38-32804
    label(0)
    sprite('el406_10', 3)	# 32805-32807
    sprite('el406_11', 3)	# 32808-32810

@Subroutine
def InvincibleAfterImage():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3072('60000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    Unknown3074('00000000dc0000002000000000000000')
    Unknown3075('00000000800000000000000020000000')
    Unknown3076(1010)
    Unknown3077(1000)

@State
def CmnActInvincibleAttackGrip():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11063(1)
        Unknown23022(1)
        EnableCollision(0)
        Unknown23014()
        Unknown23001(0, 0)
        callSubroutine('InvincibleAfterImage')

        def upon_LANDING():
            clearUponHandler(2)
            clearUponHandler(43)
            Unknown8000(100, 1, 1)
            sendToLabel(0)

        def upon_STATE_END():
            EnableCollision(1)

        def upon_43():
            if (SLOT_48 == 1006):
                clearUponHandler(43)
                enterState('CmnActInvincibleAttackExe')
    sprite('el406_01', 10)	# 1-10
    sprite('el406_01', 3)	# 11-13
    GFX_0('Randomizer_col', 0)
    Unknown21007(1, 32)
    SFX_3('cloth_m')
    physicsYImpulse(12000)
    sprite('el406_02', 3)	# 14-16
    Unknown1084(1)
    sprite('el406_03', 3)	# 17-19
    clearUponHandler(43)
    sprite('el406_04', 3)	# 20-22
    SFX_3('walk_marble_heavy')
    sprite('el406_05', 4)	# 23-26
    sprite('el406_06', 6)	# 27-32
    sprite('el406_07', 3)	# 33-35
    EnableCollision(1)
    Unknown1043()
    Unknown23022(0)
    sprite('el406_08', 20)	# 36-55
    label(0)
    sprite('el406_09', 3)	# 56-58
    sprite('el406_10', 3)	# 59-61
    sprite('el406_11', 3)	# 62-64

@State
def CmnActInvincibleAttackExe():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown23022(1)
        Unknown1084(1)
        Unknown23014()
        Unknown23001(0, 0)
        EnableCollision(0)
        callSubroutine('InvincibleAfterImage')

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sendToLabel(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown36(22)
                Unknown2071('16000000b08f06005052feff0a00000000000000')
                Unknown35()

        def upon_STATE_END():
            EnableCollision(1)
    sprite('el407_00', 3)	# 1-3
    physicsXImpulse(-9000)
    physicsYImpulse(9500)
    setGravity(400)
    SFX_3('el001')
    sprite('el407_01', 3)	# 4-6
    SFX_3('magiccircle_a')
    GFX_0('elef407_card_top', -1)
    GFX_0('elef407_card_under', -1)
    GFX_0('elef407_pillar', -1)
    sprite('el407_02', 3)	# 7-9
    sprite('el407_03', 3)	# 10-12
    SFX_3('magiccircle_b')
    sprite('el407_01', 3)	# 13-15
    tag_voice(1, 'pel262_0', 'pel262_1', 'pel263_1', '')
    sprite('el407_02', 3)	# 16-18
    sprite('el407_03', 3)	# 19-21
    sprite('el407_01', 3)	# 22-24
    sprite('el407_02', 3)	# 25-27
    sprite('el407_03', 3)	# 28-30
    sprite('el407_01', 3)	# 31-33
    sprite('el407_02', 3)	# 34-36
    sprite('el407_03', 3)	# 37-39
    SFX_3('magiccircle_b')
    GFX_0('RandomizerCamera', -1)
    Unknown38(5, 1)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    sprite('el407_04', 3)	# 40-42
    Unknown1084(1)
    setGravity(0)
    Unknown2037(1)
    sprite('el407_05', 3)	# 43-45
    sprite('el407_06', 3)	# 46-48
    sprite('el407_07', 3)	# 49-51
    SFX_3('el001')
    sprite('el407_05', 3)	# 52-54
    sprite('el407_06', 3)	# 55-57
    sprite('el407_07', 3)	# 58-60
    sprite('el407_05', 3)	# 61-63
    sprite('el407_06', 3)	# 64-66
    GFX_0('elef407_card_return', 100)
    sprite('el407_07', 3)	# 67-69
    sprite('el407_05', 3)	# 70-72
    SFX_3('el001')
    sprite('el407_06', 3)	# 73-75
    sprite('el407_07', 3)	# 76-78
    sprite('el407_05', 3)	# 79-81
    sprite('el407_06', 3)	# 82-84
    sprite('el407_07', 3)	# 85-87
    sprite('el407_05', 3)	# 88-90
    sprite('el407_06', 3)	# 91-93
    sprite('el407_07', 3)	# 94-96
    sprite('el407_05', 3)	# 97-99
    sprite('el407_06', 3)	# 100-102
    Unknown2037(0)
    clearUponHandler(3)
    sprite('el407_07', 3)	# 103-105
    sprite('el407_08', 3)	# 106-108
    sprite('el407_09', 3)	# 109-111
    SFX_3('walk_marble_heavy')
    sprite('el407_10', 3)	# 112-114
    sprite('el407_11', 3)	# 115-117
    sprite('el407_09', 3)	# 118-120
    Unknown36(22)
    Unknown3038(0)
    Unknown3001(255)
    Unknown35()
    sprite('el407_10', 3)	# 121-123
    sprite('el407_11', 3)	# 124-126
    sprite('el407_12', 3)	# 127-129
    EnableCollision(1)
    sprite('el407_13', 32767)	# 130-32896
    Unknown23029(5, 1005, 0)
    Unknown1043()
    label(0)
    sprite('el407_14', 3)	# 32897-32899
    sprite('el407_15', 3)	# 32900-32902
    sprite('el407_16', 3)	# 32903-32905

@State
def LandAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                SLOT_55 = SLOT_40
                if (SLOT_40 > 100):
                    SLOT_55 = (SLOT_55 / 400)
                    if SLOT_38:
                        SLOT_55 = (SLOT_55 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_55)
                if (SLOT_40 < (-100)):
                    SLOT_55 = (SLOT_55 / 400)
                    if SLOT_38:
                        SLOT_55 = (SLOT_55 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_55)
                if (SLOT_12 > 35000):
                    SLOT_12 = 35000

        def upon_43():
            if (SLOT_48 == 7005):
                sendToLabel(10)
            if (SLOT_48 == 7006):
                Unknown21007(11, 32)
                sendToLabel(100)
        Unknown23001(0, 0)
        Unknown23014()
    sprite('el402_00', 3)	# 1-3
    sprite('el402_01', 4)	# 4-7
    sprite('el402_01', 1)	# 8-8
    Unknown1084(1)
    Unknown22004(1, 1)
    Unknown23029(11, 4001, 0)
    if SLOT_4:
        Unknown7007('70656c3231305f3100000000000000006400000070656c3231305f3200000000000000006400000070656c3231315f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown7007('70656c3231305f3000000000000000006400000070656c3231315f3000000000000000006400000070656c3231315f310000000000000000640000000000000000000000000000000000000000000000')
    Unknown28(2, 'CmnActJumpLanding')
    sprite('el402_01', 2)	# 9-10
    sprite('el402_02', 4)	# 11-14
    GFX_0('elef402_ply_garu', 0)
    Unknown38(7, 1)
    sprite('el402_03', 3)	# 15-17
    Unknown13(7)
    setGravity(0)
    physicsYImpulse(1800)
    sprite('el402_03', 3)	# 18-20
    YAccel(200)
    sprite('el402_07', 3)	# 21-23
    YAccel(200)
    sprite('el402_08', 3)	# 24-26
    YAccel(200)
    sprite('el402_09', 3)	# 27-29
    YAccel(105)
    sprite('el402_11', 3)	# 30-32
    sprite('el020_04', 35)	# 33-67
    Unknown2037(1)
    Unknown21007(11, 32)
    YAccel(0)
    Unknown2006()
    label(100)
    sprite('el020_04', 3)	# 68-70
    Unknown1019(50)
    physicsYImpulse(0)
    sprite('el020_04', 3)	# 71-73
    Unknown1043()
    clearUponHandler(3)
    Unknown28(2, 'CmnActJumpLanding')
    Recovery()
    sprite('el020_05', 3)	# 74-76
    sprite('el020_06', 3)	# 77-79
    label(101)
    sprite('el020_07', 4)	# 80-83
    sprite('el020_08', 4)	# 84-87
    loopRest()
    gotoLabel(101)
    ExitState()
    label(10)
    sprite('el020_04', 300)	# 88-387
    Unknown1019(60)
    YAccel(60)
    label(11)
    sprite('el020_04', 1)	# 388-388
    sprite('el020_04', 2)	# 389-390
    setGravity(2000)
    sprite('el020_05', 4)	# 391-394
    Unknown1019(50)
    YAccel(50)
    sprite('el020_06', 2)	# 395-396
    label(2)
    sprite('el020_07', 4)	# 397-400
    setGravity(2000)
    sprite('el020_08', 4)	# 401-404
    loopRest()
    gotoLabel(2)

@State
def LandShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 4013):
                Recovery()
    sprite('el402_00', 3)	# 1-3
    sprite('el402_01', 4)	# 4-7
    if SLOT_4:
        Unknown23029(11, 4004, 0)
        Unknown7007('70656c3230365f3100000000000000006400000070656c3230365f3200000000000000006400000070656c3230375f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown23029(11, 4003, 0)
        Unknown7007('70656c3230365f3000000000000000006400000070656c3230375f3000000000000000006400000070656c3230375f310000000000000000640000000000000000000000000000000000000000000000')
    sprite('el402_02', 8)	# 8-15
    GFX_0('elef402_ply_jio', 0)
    Unknown38(7, 1)
    sprite('el402_03', 4)	# 16-19
    Unknown13(7)
    sprite('el402_04', 4)	# 20-23
    sprite('el402_05', 4)	# 24-27
    sprite('el402_06', 4)	# 28-31
    sprite('el402_04', 4)	# 32-35
    sprite('el402_05', 4)	# 36-39
    sprite('el402_06', 4)	# 40-43
    sprite('el402_04', 4)	# 44-47
    sprite('el402_05', 4)	# 48-51
    sprite('el402_06', 4)	# 52-55
    sprite('el402_04', 4)	# 56-59
    sprite('el402_05', 4)	# 60-63
    sprite('el402_06', 4)	# 64-67
    sprite('el402_04', 4)	# 68-71
    sprite('el402_05', 4)	# 72-75
    sprite('el402_06', 4)	# 76-79
    sprite('el402_04', 4)	# 80-83
    sprite('el402_07', 4)	# 84-87
    sprite('el402_08', 4)	# 88-91
    sprite('el402_09', 4)	# 92-95

@State
def LandSetTrapEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown1084(1)
    sprite('el431_00', 3)	# 1-3
    sprite('el431_00', 4)	# 4-7
    Unknown7007('70656c3235325f3000000000000000006400000070656c3235325f3100000000000000006400000070656c3235335f3000000000000000006400000070656c3235335f31000000000000000064000000')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    SFX_3('el001')
    GFX_0('elef431_CardPickUp', 0)
    Unknown38(7, 1)
    sprite('el431_01', 4)	# 8-11
    sprite('el431_02', 4)	# 12-15
    sprite('el431_03', 4)	# 16-19
    sprite('el431_04', 4)	# 20-23
    sprite('el431_05', 4)	# 24-27
    sprite('el431_06', 4)	# 28-31
    sprite('el431_07', 4)	# 32-35
    sprite('el431_08', 4)	# 36-39
    Unknown23029(7, 4504, 0)
    Unknown23118(-1)
    Unknown23119(-16777216, 16, 1)
    sprite('el431_09', 4)	# 40-43
    Unknown23029(11, 4501, 0)
    GFX_0('elef431_WhitePick', 100)
    sprite('el431_10', 4)	# 44-47
    sprite('el431_11', 4)	# 48-51
    sprite('el431_09z', 4)	# 52-55
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    Unknown26('elef431_WhitePick')
    sprite('el431_08z', 5)	# 56-60
    sprite('el431_07', 5)	# 61-65
    sprite('el431_01', 5)	# 66-70

@State
def AirAssault():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                SLOT_55 = SLOT_40
                if (SLOT_40 > 100):
                    SLOT_55 = (SLOT_55 / 400)
                    if SLOT_38:
                        SLOT_55 = (SLOT_55 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_55)
                if (SLOT_40 < (-100)):
                    SLOT_55 = (SLOT_55 / 400)
                    if SLOT_38:
                        SLOT_55 = (SLOT_55 / (-1))
                    SLOT_12 = (SLOT_12 + SLOT_55)
                if (SLOT_12 > 35000):
                    SLOT_12 = 35000
                SLOT_56 = SLOT_41
                if (SLOT_41 > 100):
                    SLOT_56 = (SLOT_56 / 400)
                    SLOT_13 = (SLOT_13 + SLOT_56)
                if (SLOT_41 < (-100)):
                    SLOT_56 = (SLOT_56 / 400)
                    SLOT_13 = (SLOT_13 + SLOT_56)
                if (SLOT_23 < 170000):
                    teleportRelativeY(170000)

        def upon_43():
            if (SLOT_48 == 7005):
                sendToLabel(10)
            if (SLOT_48 == 7006):
                Unknown21007(11, 32)
                sendToLabel(100)
        Unknown23001(0, 0)
        Unknown23014()
    sprite('el402_10', 3)	# 1-3
    sprite('el402_00', 4)	# 4-7
    Unknown1084(1)
    sprite('el402_01', 1)	# 8-8
    Unknown1084(1)
    Unknown22004(1, 1)
    Unknown23029(11, 4001, 0)
    if SLOT_4:
        Unknown7007('70656c3231305f3100000000000000006400000070656c3231305f3200000000000000006400000070656c3231315f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown7007('70656c3231305f3000000000000000006400000070656c3231315f3000000000000000006400000070656c3231315f310000000000000000640000000000000000000000000000000000000000000000')
    Unknown28(2, 'CmnActJumpLanding')
    sprite('el402_01', 2)	# 9-10
    sprite('el402_02', 4)	# 11-14
    GFX_0('elef402_ply_garu', 0)
    Unknown38(7, 1)
    sprite('el402_03', 3)	# 15-17
    Unknown13(7)
    setGravity(0)
    physicsYImpulse(1800)
    sprite('el402_03', 3)	# 18-20
    YAccel(200)
    sprite('el402_07', 3)	# 21-23
    YAccel(200)
    sprite('el402_08', 3)	# 24-26
    YAccel(200)
    sprite('el402_09', 3)	# 27-29
    YAccel(105)
    sprite('el402_11', 3)	# 30-32
    sprite('el020_04', 35)	# 33-67
    Unknown2037(1)
    Unknown21007(11, 32)
    YAccel(0)
    Unknown2006()
    label(100)
    sprite('el020_04', 3)	# 68-70
    Unknown1019(50)
    physicsYImpulse(0)
    sprite('el020_04', 3)	# 71-73
    Unknown1043()
    clearUponHandler(3)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('el020_05', 3)	# 74-76
    sprite('el020_06', 3)	# 77-79
    label(101)
    sprite('el020_07', 4)	# 80-83
    sprite('el020_08', 4)	# 84-87
    loopRest()
    gotoLabel(101)
    ExitState()
    label(10)
    sprite('el020_04', 300)	# 88-387
    Unknown1019(60)
    YAccel(60)
    label(11)
    sprite('el020_04', 1)	# 388-388
    sprite('el020_04', 2)	# 389-390
    setGravity(2000)
    sprite('el020_05', 4)	# 391-394
    Unknown1019(50)
    YAccel(50)
    sprite('el020_06', 2)	# 395-396
    gotoLabel(2)
    label(2)
    sprite('el020_07', 4)	# 397-400
    setGravity(2000)
    sprite('el020_08', 4)	# 401-404
    loopRest()
    gotoLabel(2)

@State
def AirShot():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
    sprite('el402_10', 3)	# 1-3
    sprite('el402_00', 4)	# 4-7
    if SLOT_4:
        Unknown23029(11, 4004, 0)
        Unknown7007('70656c3230365f3100000000000000006400000070656c3230365f3200000000000000006400000070656c3230375f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown23029(11, 4003, 0)
        Unknown7007('70656c3230365f3000000000000000006400000070656c3230375f3000000000000000006400000070656c3230375f310000000000000000640000000000000000000000000000000000000000000000')
    Unknown1084(1)
    Unknown22004(6, 6)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('el402_01', 4)	# 8-11
    sprite('el402_02', 8)	# 12-19
    GFX_0('elef402_ply_jio', 0)
    Unknown38(7, 1)
    sprite('el402_03', 4)	# 20-23
    sprite('el402_04', 4)	# 24-27
    Unknown13(7)
    sprite('el402_05', 4)	# 28-31
    sprite('el402_06', 4)	# 32-35
    sprite('el402_04', 4)	# 36-39
    sprite('el402_05', 4)	# 40-43
    sprite('el402_06', 4)	# 44-47
    sprite('el402_04', 4)	# 48-51
    sprite('el402_05', 4)	# 52-55
    sprite('el402_04', 4)	# 56-59
    sprite('el402_05', 4)	# 60-63
    sprite('el402_06', 4)	# 64-67
    sprite('el402_04', 4)	# 68-71
    setGravity(1700)
    sprite('el402_07', 4)	# 72-75
    sprite('el402_08', 3)	# 76-78
    sprite('el402_09', 3)	# 79-81
    sprite('el402_11', 3)	# 82-84

@State
def AirSetTrapEx():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown1084(1)
    sprite('el431_00', 3)	# 1-3
    sprite('el431_00', 4)	# 4-7
    Unknown7007('70656c3235345f3000000000000000006400000070656c3235345f3100000000000000006400000070656c3235355f3000000000000000006400000070656c3235355f31000000000000000064000000')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    SFX_3('el001')
    GFX_0('elef431_CardPickUp', 0)
    Unknown38(7, 1)
    sprite('el431_01', 4)	# 8-11
    sprite('el431_02', 4)	# 12-15
    sprite('el431_03', 4)	# 16-19
    sprite('el431_04', 4)	# 20-23
    sprite('el431_05', 4)	# 24-27
    sprite('el431_06', 4)	# 28-31
    sprite('el431_07', 4)	# 32-35
    sprite('el431_08', 4)	# 36-39
    Unknown23029(7, 4505, 0)
    Unknown3026(-13158601)
    Unknown23130(-1, 16, 1)
    sprite('el431_09', 4)	# 40-43
    Unknown23029(11, 4502, 0)
    GFX_0('elef431_BlackPick', 100)
    sprite('el431_10', 4)	# 44-47
    sprite('el431_11', 4)	# 48-51
    sprite('el431_09z', 4)	# 52-55
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    Unknown26('elef431_BlackPick')
    sprite('el431_10z', 4)	# 56-59
    sprite('el431_11z', 3)	# 60-62
    sprite('el431_08z', 2)	# 63-64
    sprite('el431_07', 2)	# 65-66
    sprite('el431_01', 2)	# 67-68
    Unknown1043()
    sprite('el020_02', 2)	# 69-70

@State
def AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        loopRelated(17, 45)

        def upon_17():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 4025):
                loopRelated(17, 95)
            if (SLOT_48 == 3015):
                Recovery()
    sprite('el403_00', 3)	# 1-3
    sprite('el403_01', 4)	# 4-7
    sprite('el403_02', 4)	# 8-11
    if SLOT_4:
        Unknown23029(11, 4006, 0)
        Unknown7007('70656c3230385f3100000000000000006400000070656c3230385f3200000000000000006400000070656c3230395f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown23029(11, 4005, 0)
        Unknown7007('70656c3230385f3000000000000000006400000070656c3230395f3000000000000000006400000070656c3230395f310000000000000000640000000000000000000000000000000000000000000000')
    sprite('el403_03', 4)	# 12-15
    sprite('el403_04', 4)	# 16-19
    GFX_0('elef403_ply_bufu', 0)
    Unknown38(7, 1)
    label(0)
    sprite('el403_05', 4)	# 20-23
    sprite('el403_06', 4)	# 24-27
    sprite('el403_07', 4)	# 28-31
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 32-33
    Unknown13(7)
    sprite('el403_00', 4)	# 34-37

@State
def ChargeShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('el403_00', 4)	# 1-4
    sprite('el403_01', 4)	# 5-8
    if SLOT_4:
        Unknown23029(11, 4008, 0)
        Unknown7007('70656c3231325f3100000000000000006400000070656c3231325f3200000000000000006400000070656c3231335f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown23029(11, 4007, 0)
        Unknown7007('70656c3231325f3000000000000000006400000070656c3231335f3000000000000000006400000070656c3231335f310000000000000000640000000000000000000000000000000000000000000000')
    sprite('el403_02', 4)	# 9-12
    sprite('el403_03', 4)	# 13-16
    sprite('el403_04', 4)	# 17-20
    GFX_0('elef403_ply_ragi', 0)
    sprite('el403_05', 4)	# 21-24
    sprite('el403_06', 4)	# 25-28
    sprite('el403_07', 4)	# 29-32
    Unknown26('elef403_ply_ragi')
    sprite('el403_05', 4)	# 33-36
    sprite('el403_06', 4)	# 37-40
    sprite('el403_07', 4)	# 41-44
    sprite('el403_05', 4)	# 45-48
    sprite('el403_06', 4)	# 49-52
    sprite('el403_07', 4)	# 53-56
    sprite('el403_05', 4)	# 57-60
    sprite('el403_06', 4)	# 61-64
    sprite('el403_07', 4)	# 65-68
    sprite('el403_05', 4)	# 69-72
    sprite('el403_06', 4)	# 73-76
    sprite('el403_07', 4)	# 77-80
    sprite('el403_05', 4)	# 81-84
    sprite('el403_06', 4)	# 85-88
    sprite('el403_00', 4)	# 89-92

@State
def SpecialHeal():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2021(1)
        Unknown1084(1)
        Unknown23014()
        Unknown23001(0, 0)
        loopRelated(17, 240)

        def upon_17():
            SLOT_54 = 1
        Unknown2037(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown21000(25)
            if (not SLOT_IsInOverdrive2):
                if (not CheckInput(0x13)):
                    SLOT_54 = 1

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(2)
    sprite('el432_00', 4)	# 1-4
    sprite('el432_01', 4)	# 5-8
    sprite('el432_02', 4)	# 9-12
    sprite('el432_03', 4)	# 13-16
    physicsYImpulse(700)
    SFX_3('el007')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 4503, 0)
    sprite('el432_04', 4)	# 17-20
    sprite('el432_05', 4)	# 21-24
    Unknown7007('70656c3235365f3000000000000000006400000070656c3235365f3100000000000000006400000070656c3235375f3000000000000000006400000070656c3235375f31000000000000000064000000')
    sprite('el432_06', 4)	# 25-28
    SFX_3('el001')
    sprite('el432_07', 4)	# 29-32
    Unknown21000(500)
    Unknown2037(1)
    sprite('el432_08', 4)	# 33-36
    Unknown21000(500)
    sprite('el432_09', 4)	# 37-40
    Unknown21000(500)
    sprite('el432_10', 4)	# 41-44
    Unknown21000(500)
    sprite('el432_11', 4)	# 45-48
    Unknown21000(500)
    sprite('el432_09', 4)	# 49-52
    sprite('el432_10', 4)	# 53-56
    sprite('el432_11', 4)	# 57-60
    sprite('el432_09', 4)	# 61-64
    GFX_0('elHikari', 100)
    SFX_3('el053')
    sprite('el432_10', 4)	# 65-68
    sprite('el432_11', 4)	# 69-72
    sprite('el432_09', 4)	# 73-76
    sprite('el432_10', 4)	# 77-80
    sprite('el432_11', 4)	# 81-84
    YAccel(0)
    loopRest()
    if SLOT_IsInOverdrive2:
        _gotolabel(1)
    label(0)
    sprite('el432_09', 4)	# 85-88
    sprite('el432_10', 4)	# 89-92
    sprite('el432_11', 4)	# 93-96
    sprite('el432_09', 4)	# 97-100
    sprite('el432_10', 4)	# 101-104
    sprite('el432_11', 4)	# 105-108
    sprite('el432_09', 4)	# 109-112
    sprite('el432_10', 4)	# 113-116
    sprite('el432_11', 4)	# 117-120
    sprite('el432_09', 4)	# 121-124
    sprite('el432_10', 4)	# 125-128
    sprite('el432_11', 4)	# 129-132
    sprite('el432_09', 4)	# 133-136
    sprite('el432_10', 4)	# 137-140
    sprite('el432_11', 4)	# 141-144
    sprite('el432_09', 4)	# 145-148
    sprite('el432_10', 4)	# 149-152
    sprite('el432_11', 4)	# 153-156
    sprite('el432_09', 4)	# 157-160
    sprite('el432_10', 4)	# 161-164
    sprite('el432_11', 4)	# 165-168
    loopRest()
    Unknown19(0, 2, 54)
    label(1)
    sprite('el432_07', 4)	# 169-172
    clearUponHandler(3)
    clearUponHandler(17)
    Unknown21007(11, 33)
    Unknown21012('656c48696b61726900000000000000000000000000000000000000000000000021000000')
    Unknown2037(0)
    setGravity(300)
    sprite('el432_06', 4)	# 173-176
    sprite('el432_03', 2)	# 177-178
    sprite('el432_03', 10)	# 179-188
    sprite('el432_02', 32767)	# 189-32955
    label(2)
    sprite('el432_01', 3)	# 32956-32958
    sprite('el432_00', 3)	# 32959-32961

@State
def UltimateCharge():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
        Unknown1084(1)
    sprite('el430_00', 3)	# 1-3
    sprite('el430_01', 3)	# 4-6
    sprite('el430_01', 3)	# 7-9
    Unknown7007('70656c3235305f3000000000000000006400000070656c3235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30080('')
    Unknown2036(88, -1, 0)
    ConsumeSuperMeter(-10000)
    setInvincible(1)
    Unknown23119(-16776961, 12, 1)
    SFX_3('el001')
    physicsYImpulse(4000)
    setGravity(0)
    sprite('el430_01', 3)	# 10-12
    sprite('el430_02', 5)	# 13-17
    Unknown3029(1)
    Unknown3071(4)
    YAccel(50)
    Unknown23119(-16744193, 30, 1)
    GFX_0('elef430_Concentraite', 100)
    SFX_3('el052')
    sprite('el430_03', 5)	# 18-22
    YAccel(50)
    sprite('el430_04', 5)	# 23-27
    YAccel(50)
    SFX_3('el001')
    sprite('el430_02', 4)	# 28-31
    Unknown23119(-1, 24, 1)
    sprite('el430_03', 4)	# 32-35
    sprite('el430_04', 4)	# 36-39
    sprite('el430_02', 3)	# 40-42
    Unknown23119(-65536, 18, 1)
    sprite('el430_03', 3)	# 43-45
    sprite('el430_04', 3)	# 46-48
    op(3, 2, 76, 0, 100)
    SLOT_52 = SLOT_0
    op(2, 2, 52, 0, 35)
    SLOT_53 = SLOT_0
    Unknown48('1900000002000000360000001600000002000000aa000000')
    if (not SLOT_IsInOverdrive2):

        def upon_45():
            if (SLOT_75 >= SLOT_53):
                Unknown21001(-230)
                Unknown30029(115)
                Unknown2068(632)
    sprite('el430_02', 2)	# 49-50
    sprite('el430_03', 2)	# 51-52
    sprite('el430_04', 2)	# 53-54
    sprite('el430_02', 2)	# 55-56
    sprite('el430_03', 2)	# 57-58
    sprite('el430_04', 2)	# 59-60
    sprite('el430_02', 2)	# 61-62
    sprite('el430_03', 2)	# 63-64
    sprite('el430_04', 2)	# 65-66
    sprite('el430_02', 2)	# 67-68
    Unknown23119(-16777216, 30, 1)
    sprite('el430_03', 2)	# 69-70
    sprite('el430_04', 2)	# 71-72
    loopRest()
    setGravity(400)
    physicsYImpulse(0)
    sprite('el430_02', 2)	# 73-74
    sprite('el430_03', 2)	# 75-76
    label(0)
    sprite('el430_02', 2)	# 77-78
    sprite('el430_03', 2)	# 79-80
    sprite('el430_04', 2)	# 81-82
    sprite('el430_02', 2)	# 83-84
    sprite('el430_03', 2)	# 85-86
    sprite('el430_04', 2)	# 87-88
    loopRest()
    gotoLabel(0)
    label(10)
    clearUponHandler(3)
    clearUponHandler(2)
    sprite('el430_05', 1)	# 89-89
    setInvincible(0)
    sprite('el430_06', 1)	# 90-90
    sprite('el430_07', 1)	# 91-91
    sprite('el430_08', 1)	# 92-92

@State
def UltimateChargeSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
        Unknown1084(1)
    sprite('el430_00', 3)	# 1-3
    sprite('el430_01', 3)	# 4-6
    sprite('el430_01', 3)	# 7-9
    Unknown7007('70656c3235305f3000000000000000006400000070656c3235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30080('')
    Unknown2036(88, -1, 0)
    ConsumeSuperMeter(-10000)
    setInvincible(1)
    Unknown23119(-16776961, 12, 1)
    SFX_3('el001')
    physicsYImpulse(4000)
    setGravity(0)
    sprite('el430_01', 3)	# 10-12
    sprite('el430_02', 5)	# 13-17
    Unknown3029(1)
    Unknown3071(4)
    YAccel(50)
    Unknown23119(-16744193, 30, 1)
    GFX_0('elef430_Concentraite', 100)
    SFX_3('el052')
    sprite('el430_03', 5)	# 18-22
    YAccel(50)
    sprite('el430_04', 5)	# 23-27
    YAccel(50)
    SFX_3('el001')
    sprite('el430_02', 4)	# 28-31
    Unknown23119(-1, 24, 1)
    sprite('el430_03', 4)	# 32-35
    sprite('el430_04', 4)	# 36-39
    sprite('el430_02', 3)	# 40-42
    Unknown23119(-65536, 18, 1)
    sprite('el430_03', 3)	# 43-45
    sprite('el430_04', 3)	# 46-48
    op(3, 2, 76, 0, 100)
    SLOT_52 = SLOT_0
    op(2, 2, 52, 0, 35)
    SLOT_53 = SLOT_0
    Unknown48('1900000002000000360000001600000002000000aa000000')
    if (not SLOT_IsInOverdrive2):

        def upon_45():
            if (SLOT_75 >= SLOT_53):
                Unknown21001(-230)
                Unknown30029(172)
                Unknown2068(632)
    sprite('el430_02', 2)	# 49-50
    sprite('el430_03', 2)	# 51-52
    sprite('el430_04', 2)	# 53-54
    sprite('el430_02', 2)	# 55-56
    sprite('el430_03', 2)	# 57-58
    sprite('el430_04', 2)	# 59-60
    sprite('el430_02', 2)	# 61-62
    sprite('el430_03', 2)	# 63-64
    sprite('el430_04', 2)	# 65-66
    sprite('el430_02', 2)	# 67-68
    Unknown23119(-16777216, 30, 1)
    sprite('el430_03', 2)	# 69-70
    sprite('el430_04', 2)	# 71-72
    loopRest()
    setGravity(400)
    physicsYImpulse(0)
    sprite('el430_02', 2)	# 73-74
    sprite('el430_03', 2)	# 75-76
    label(0)
    sprite('el430_02', 2)	# 77-78
    sprite('el430_03', 2)	# 79-80
    sprite('el430_04', 2)	# 81-82
    sprite('el430_02', 2)	# 83-84
    sprite('el430_03', 2)	# 85-86
    sprite('el430_04', 2)	# 87-88
    loopRest()
    gotoLabel(0)
    label(10)
    clearUponHandler(3)
    clearUponHandler(2)
    sprite('el430_05', 1)	# 89-89
    setInvincible(0)
    sprite('el430_06', 1)	# 90-90
    sprite('el430_07', 1)	# 91-91
    sprite('el430_08', 1)	# 92-92

@State
def UltimateThrow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        Unknown1084(1)
        loopRelated(17, 104)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 5021):
                enterState('UltimateThrowExe')
    sprite('el433_00', 4)	# 1-4
    sprite('el433_01', 4)	# 5-8
    callSubroutine('PersonaCard_ON')
    sprite('el433_02', 4)	# 9-12
    tag_voice(1, 'pel258_0', 'pel258_1', '', '')
    sprite('el433_00', 4)	# 13-16
    Unknown30080('')
    Unknown2036(63, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown23029(11, 5001, 0)
    sprite('el433_01', 4)	# 17-20
    sprite('el433_02', 4)	# 21-24
    sprite('el433_00', 4)	# 25-28
    sprite('el433_01', 4)	# 29-32
    sprite('el433_02', 4)	# 33-36
    sprite('el433_00', 4)	# 37-40
    sprite('el433_01', 4)	# 41-44
    sprite('el433_02', 4)	# 45-48
    sprite('el433_03', 4)	# 49-52
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 53-56
    sprite('el433_05', 4)	# 57-60
    sprite('el433_06', 4)	# 61-64
    sprite('el433_07', 4)	# 65-68
    sprite('el433_08', 4)	# 69-72
    sprite('el433_09', 4)	# 73-76
    sprite('el433_10', 4)	# 77-80
    sprite('el433_11', 4)	# 81-84
    setInvincible(0)
    label(0)
    sprite('el433_09', 4)	# 85-88
    sprite('el433_10', 4)	# 89-92
    sprite('el433_11', 4)	# 93-96
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el433_12', 4)	# 97-100
    sprite('el433_13', 4)	# 101-104

@State
def UltimateThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        setInvincible(1)
        Unknown1084(1)
        loopRelated(17, 157)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('el433_09', 4)	# 1-4
    sprite('el433_10', 4)	# 5-8
    sprite('el433_11', 4)	# 9-12
    sprite('el433_09', 4)	# 13-16
    sprite('el433_10', 4)	# 17-20
    sprite('el433_11', 4)	# 21-24
    sprite('el433_09', 4)	# 25-28
    sprite('el433_10', 4)	# 29-32
    sprite('el433_11', 4)	# 33-36
    sprite('el433_09', 4)	# 37-40
    tag_voice(0, 'pel259_0', 'pel259_1', '', '')
    sprite('el433_10', 4)	# 41-44
    sprite('el433_11', 4)	# 45-48
    label(0)
    sprite('el433_09', 4)	# 49-52
    sprite('el433_10', 4)	# 53-56
    sprite('el433_11', 4)	# 57-60
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 61-62
    sprite('el433_12', 4)	# 63-66
    sprite('el433_13', 4)	# 67-70

@State
def UltimateThrowSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        Unknown1084(1)
        loopRelated(17, 104)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 5022):
                enterState('UltimateThrowSPExe')
    sprite('el433_00', 4)	# 1-4
    sprite('el433_01', 4)	# 5-8
    callSubroutine('PersonaCard_ON')
    sprite('el433_02', 4)	# 9-12
    tag_voice(1, 'pel260_0', 'pel260_1', '', '')
    sprite('el433_00', 4)	# 13-16
    Unknown30080('')
    Unknown2036(63, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown23029(11, 5002, 0)
    sprite('el433_01', 4)	# 17-20
    sprite('el433_02', 4)	# 21-24
    sprite('el433_00', 4)	# 25-28
    sprite('el433_01', 4)	# 29-32
    sprite('el433_02', 4)	# 33-36
    sprite('el433_00', 4)	# 37-40
    sprite('el433_01', 4)	# 41-44
    sprite('el433_02', 4)	# 45-48
    sprite('el433_03', 4)	# 49-52
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 53-56
    sprite('el433_05', 4)	# 57-60
    sprite('el433_06', 4)	# 61-64
    sprite('el433_07', 4)	# 65-68
    sprite('el433_08', 4)	# 69-72
    sprite('el433_09', 4)	# 73-76
    sprite('el433_10', 4)	# 77-80
    sprite('el433_11', 4)	# 81-84
    setInvincible(0)
    label(0)
    sprite('el433_09', 4)	# 85-88
    sprite('el433_10', 4)	# 89-92
    sprite('el433_11', 4)	# 93-96
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('el433_12', 4)	# 97-100
    sprite('el433_13', 4)	# 101-104

@State
def UltimateThrowSPExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        setInvincible(1)
        Unknown1084(1)
        loopRelated(17, 278)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('el433_09', 4)	# 1-4
    sprite('el433_10', 4)	# 5-8
    sprite('el433_11', 4)	# 9-12
    sprite('el433_09', 4)	# 13-16
    sprite('el433_10', 4)	# 17-20
    sprite('el433_11', 4)	# 21-24
    sprite('el433_09', 4)	# 25-28
    sprite('el433_10', 4)	# 29-32
    sprite('el433_11', 4)	# 33-36
    sprite('el433_09', 4)	# 37-40
    sprite('el433_10', 4)	# 41-44
    sprite('el433_11', 4)	# 45-48
    sprite('el433_09', 4)	# 49-52
    sprite('el433_10', 4)	# 53-56
    sprite('el433_11', 4)	# 57-60
    sprite('el433_09', 4)	# 61-64
    sprite('el433_10', 4)	# 65-68
    sprite('el433_11', 4)	# 69-72
    sprite('el433_09', 4)	# 73-76
    sprite('el433_10', 4)	# 77-80
    sprite('el433_11', 4)	# 81-84
    sprite('el433_09', 4)	# 85-88
    tag_voice(0, 'pel261_0', 'pel261_1', '', '')
    sprite('el433_10', 4)	# 89-92
    sprite('el433_11', 4)	# 93-96
    label(0)
    sprite('el433_09', 4)	# 97-100
    sprite('el433_10', 4)	# 101-104
    sprite('el433_11', 4)	# 105-108
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 2)	# 109-110
    sprite('el433_12', 4)	# 111-114
    sprite('el433_13', 4)	# 115-118

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown2003(1)
        Unknown11063(1)
        Unknown48('19000000020000003900000016000000020000001e000000')
        GuardPoint_(1)
        Unknown22031(-1, 1)
        SLOT_5 = 0

        def upon_42():
            tag_voice(1, 'pel290_0', 'pel290_1', '', '')
            Unknown23022(1)
            SLOT_5 = 1
            ScreenShake(15000, 10000)
            Unknown2036(60, -1, 2)
            Unknown23029(8, 6002, 0)
            sendToLabel(0)

        def upon_STATE_END():
            Unknown23029(8, 6003, 0)
    sprite('el450_00', 4)	# 1-4
    setInvincible(1)
    Unknown2036(50, -1, 2)
    Unknown23147()
    GFX_0('P4U_Cutin_Parent', 100)
    GFX_0('elef450_AtemiCard', 100)
    Unknown38(8, 1)
    sprite('el450_01', 4)	# 5-8	 **attackbox here**
    sprite('el450_02', 4)	# 9-12	 **attackbox here**
    sprite('el450_03', 4)	# 13-16	 **attackbox here**
    if SLOT_57:
        Unknown23029(8, 6002, 0)
        sendToLabel(0)
    sprite('el450_01', 4)	# 17-20	 **attackbox here**
    sprite('el450_02', 4)	# 21-24	 **attackbox here**
    sprite('el450_03', 4)	# 25-28	 **attackbox here**
    sprite('el450_01', 4)	# 29-32	 **attackbox here**
    sprite('el450_02', 4)	# 33-36	 **attackbox here**
    sprite('el450_03', 4)	# 37-40	 **attackbox here**
    sprite('el450_01', 4)	# 41-44	 **attackbox here**
    sprite('el450_02', 4)	# 45-48	 **attackbox here**
    sprite('el450_03', 4)	# 49-52	 **attackbox here**
    sprite('el450_01', 4)	# 53-56	 **attackbox here**
    sprite('el450_02', 4)	# 57-60	 **attackbox here**
    sprite('el450_03', 4)	# 61-64	 **attackbox here**
    sprite('el450_01', 4)	# 65-68	 **attackbox here**
    sprite('el450_02', 4)	# 69-72	 **attackbox here**
    sprite('el450_03', 4)	# 73-76	 **attackbox here**
    sprite('el450_01', 4)	# 77-80	 **attackbox here**
    sprite('el450_02', 4)	# 81-84	 **attackbox here**
    sprite('el450_03', 4)	# 85-88	 **attackbox here**
    sprite('el450_01', 4)	# 89-92	 **attackbox here**
    Unknown23029(8, 6003, 0)
    setInvincible(0)
    sprite('el450_02', 4)	# 93-96	 **attackbox here**
    sprite('el450_03ex01', 4)	# 97-100	 **attackbox here**
    sprite('el450_01ex01', 4)	# 101-104	 **attackbox here**
    sprite('el450_02ex01', 4)	# 105-108	 **attackbox here**
    sprite('el450_03ex01', 4)	# 109-112	 **attackbox here**
    sprite('el450_00', 4)	# 113-116
    ExitState()
    label(0)
    sprite('el450_01', 4)	# 117-120	 **attackbox here**
    sprite('el450_02', 4)	# 121-124	 **attackbox here**
    sprite('el450_03', 4)	# 125-128	 **attackbox here**
    sprite('el450_01', 4)	# 129-132	 **attackbox here**
    sprite('el450_02', 4)	# 133-136	 **attackbox here**
    sprite('el450_03', 4)	# 137-140	 **attackbox here**
    sprite('el450_01', 4)	# 141-144	 **attackbox here**
    sprite('el450_02', 4)	# 145-148	 **attackbox here**
    sprite('el450_03', 4)	# 149-152	 **attackbox here**
    label(1)
    sprite('keep', 4)	# 153-156
    enterState('AstralHeatCounter')

@State
def AstralHeatCounter():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown2003(1)
        setInvincible(1)
        loopRelated(17, 46)

        def upon_17():
            clearUponHandler(17)
            setInvincible(0)
        if SLOT_5:
            Unknown23022(1)
            SLOT_5 = 0

        def upon_43():
            if (SLOT_48 == 6004):
                clearUponHandler(43)
                Unknown23022(1)
                sendToLabel(0)
    sprite('el204_00', 4)	# 1-4
    sprite('el204_01', 4)	# 5-8
    sprite('el204_02', 4)	# 9-12
    sprite('el204_03', 4)	# 13-16
    GFX_0('elef450_CounterCard', 100)
    callSubroutine('PersonaCard_ON')
    sprite('el204_04', 4)	# 17-20
    callSubroutine('PersonaCard_STOP')
    sprite('el204_05', 4)	# 21-24
    sprite('el204_03', 4)	# 25-28
    sprite('el204_04', 4)	# 29-32
    sprite('el204_05', 4)	# 33-36
    sprite('el204_03', 4)	# 37-40
    sprite('el204_04', 4)	# 41-44
    sprite('el204_05', 4)	# 45-48
    sprite('el204_03', 4)	# 49-52
    sprite('el204_04', 4)	# 53-56
    sprite('el204_05', 4)	# 57-60
    sprite('el204_03', 4)	# 61-64
    sprite('el204_04', 4)	# 65-68
    sprite('el204_05', 4)	# 69-72
    sprite('el204_01', 4)	# 73-76
    callSubroutine('PersonaCard_OFF')
    sprite('el204_00', 4)	# 77-80
    ExitState()
    label(0)
    sprite('keep', 2)	# 81-82
    sprite('el204_03', 4)	# 83-86
    sprite('el204_04', 4)	# 87-90
    sprite('el204_05', 4)	# 91-94
    sprite('el204_01', 4)	# 95-98
    callSubroutine('PersonaCard_OFF')
    sprite('el204_00', 4)	# 99-102
    sprite('keep', 4)	# 103-106
    enterState('AstralHeatExe')
    ExitState()

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        DisableAttackRestOfMove()
        Unknown2006()
        Unknown23022(1)
        Unknown23084(1)
        Unknown23157(1)
        Unknown23088(1, 1)

        def upon_CLEAR_OR_EXIT():
            Unknown1019(98)
            YAccel(98)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)
        Unknown21012('4d6168616e6d616f6e5f7365617263680000000000000000000000000000000027000000')
        Unknown21012('4d6168616d75646f5f6f6e5f736561726368000000000000000000000000000027000000')
    sprite('keep', 3)	# 1-3
    GFX_0('CameraDammy', 100)
    sprite('el000_00', 6)	# 4-9
    sprite('el000_01', 6)	# 10-15
    sprite('el000_02', 6)	# 16-21
    sprite('el450_04', 4)	# 22-25	 **attackbox here**
    physicsXImpulse(-1500)
    physicsYImpulse(4000)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3076(900)
    Unknown3077(900)
    Unknown23024(3)
    sprite('el450_05', 4)	# 26-29
    sprite('el450_06', 4)	# 30-33
    sprite('el450_07', 4)	# 34-37
    sprite('el450_08', 4)	# 38-41
    GFX_0('elef450_CardLayParent', 103)
    SFX_3('el002')
    sprite('el450_09', 4)	# 42-45
    SFX_3('el002')
    sprite('el450_10', 4)	# 46-49
    SFX_3('el002')
    sprite('el450_08', 4)	# 50-53
    SFX_3('el002')
    sprite('el450_09', 4)	# 54-57
    SFX_3('el002')
    sprite('el450_10', 4)	# 58-61
    SFX_3('el002')
    sprite('el450_08', 4)	# 62-65
    SFX_3('el002')
    sprite('el450_09', 4)	# 66-69
    SFX_3('el002')
    sprite('el450_10', 4)	# 70-73
    SFX_3('el002')
    sprite('el450_08', 4)	# 74-77
    SFX_3('el002')
    sprite('el450_09', 4)	# 78-81
    SFX_3('el002')
    sprite('el450_10', 4)	# 82-85
    SFX_3('el002')
    sprite('el450_08', 4)	# 86-89
    SFX_3('el002')
    sprite('el450_09', 4)	# 90-93
    SFX_3('el002')
    sprite('el450_10', 4)	# 94-97
    SFX_3('el002')
    sprite('el450_08', 4)	# 98-101
    SFX_3('el002')
    sprite('el450_09', 4)	# 102-105
    SFX_3('el002')
    sprite('el450_10', 4)	# 106-109
    sprite('el450_08', 4)	# 110-113
    sprite('el450_09', 4)	# 114-117
    sprite('el450_10', 4)	# 118-121
    sprite('el450_08', 4)	# 122-125
    sprite('el450_09', 4)	# 126-129
    sprite('el450_10', 4)	# 130-133
    sprite('el450_08', 4)	# 134-137
    sprite('el450_09', 4)	# 138-141
    sprite('el450_10', 4)	# 142-145
    sprite('el450_11', 4)	# 146-149
    SFX_3('magiccircle_b')
    sprite('el450_12', 4)	# 150-153
    sprite('el450_13', 4)	# 154-157	 **attackbox here**
    sprite('el450_14', 4)	# 158-161	 **attackbox here**
    sprite('el450_15', 4)	# 162-165	 **attackbox here**
    Unknown3029(0)
    sprite('el450_13', 4)	# 166-169	 **attackbox here**
    sprite('el450_14', 4)	# 170-173	 **attackbox here**
    sprite('el450_15', 4)	# 174-177	 **attackbox here**
    sprite('el450_13', 4)	# 178-181	 **attackbox here**
    sprite('el450_14', 4)	# 182-185	 **attackbox here**
    sprite('el450_15', 4)	# 186-189	 **attackbox here**
    sprite('el450_13', 4)	# 190-193	 **attackbox here**
    sprite('el450_14', 4)	# 194-197	 **attackbox here**
    sprite('el450_15', 4)	# 198-201	 **attackbox here**
    sprite('el450_13', 4)	# 202-205	 **attackbox here**
    Unknown21012('656c65663435305f4c6f636b436172640000000000000000000000000000000020000000')
    sprite('el450_14', 4)	# 206-209	 **attackbox here**
    sprite('el450_15', 4)	# 210-213	 **attackbox here**
    sprite('el450_13', 4)	# 214-217	 **attackbox here**
    sprite('el450_14', 4)	# 218-221	 **attackbox here**
    sprite('el450_15', 4)	# 222-225	 **attackbox here**
    sprite('el450_13', 4)	# 226-229	 **attackbox here**
    sprite('el450_14', 4)	# 230-233	 **attackbox here**
    sprite('el450_15', 4)	# 234-237	 **attackbox here**
    sprite('el450_13', 4)	# 238-241	 **attackbox here**
    sprite('el450_14', 4)	# 242-245	 **attackbox here**
    sprite('el450_15', 4)	# 246-249	 **attackbox here**
    sprite('el450_13', 4)	# 250-253	 **attackbox here**
    sprite('el450_14', 4)	# 254-257	 **attackbox here**
    sprite('el450_15', 4)	# 258-261	 **attackbox here**
    sprite('el450_13', 4)	# 262-265	 **attackbox here**
    sprite('el450_14', 4)	# 266-269	 **attackbox here**
    sprite('el450_15', 4)	# 270-273	 **attackbox here**
    sprite('el450_13', 4)	# 274-277	 **attackbox here**
    sprite('el450_14', 4)	# 278-281	 **attackbox here**
    sprite('el450_15', 4)	# 282-285	 **attackbox here**
    sprite('el450_13', 4)	# 286-289	 **attackbox here**
    sprite('el450_14', 4)	# 290-293	 **attackbox here**
    sprite('el450_15', 4)	# 294-297	 **attackbox here**
    sprite('el450_13', 4)	# 298-301	 **attackbox here**
    sprite('el450_14', 4)	# 302-305	 **attackbox here**
    sprite('el450_15', 4)	# 306-309	 **attackbox here**
    sprite('el450_13', 4)	# 310-313	 **attackbox here**
    sprite('el450_14', 4)	# 314-317	 **attackbox here**
    sprite('el450_15', 4)	# 318-321	 **attackbox here**
    sprite('el450_13', 4)	# 322-325	 **attackbox here**
    sprite('el450_14', 4)	# 326-329	 **attackbox here**
    sprite('el450_15', 4)	# 330-333	 **attackbox here**
    sprite('el450_13', 4)	# 334-337	 **attackbox here**
    sprite('el450_14', 4)	# 338-341	 **attackbox here**
    sprite('el450_15', 4)	# 342-345	 **attackbox here**
    sprite('el450_13', 4)	# 346-349	 **attackbox here**
    sprite('el450_14', 4)	# 350-353	 **attackbox here**
    sprite('el450_15', 4)	# 354-357	 **attackbox here**
    Unknown4004('534345465f536861736861496e0000000000000000000000000000000000000064000000')
    sprite('el450_13', 4)	# 358-361	 **attackbox here**
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    Unknown3029(0)
    sprite('el450_14', 4)	# 362-365	 **attackbox here**
    sprite('el450_15', 4)	# 366-369	 **attackbox here**
    sprite('el450_13', 4)	# 370-373	 **attackbox here**
    Unknown26('CameraDammy')
    Unknown20000(3)
    Unknown1086(22)
    Unknown1000(0)
    Unknown1007(1024000)
    physicsYImpulse(0)
    physicsXImpulse(0)
    Unknown23024(2)
    sprite('el450_14', 4)	# 374-377	 **attackbox here**
    sprite('el450_15', 4)	# 378-381	 **attackbox here**
    sprite('el450_15', 60)	# 382-441	 **attackbox here**
    sprite('el450_16', 4)	# 442-445
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown26('SCEF_ShashaIn')
    GFX_0('Cutinbg', 100)
    sprite('el450_17', 4)	# 446-449
    sprite('el450_18', 4)	# 450-453
    sprite('el450_16', 4)	# 454-457
    sprite('el450_17', 4)	# 458-461
    sprite('el450_18', 4)	# 462-465
    sprite('el450_16', 4)	# 466-469
    sprite('el450_17', 4)	# 470-473
    sprite('el450_18', 4)	# 474-477
    sprite('el450_16', 4)	# 478-481
    sprite('el450_17', 4)	# 482-485
    sprite('el450_18', 4)	# 486-489
    sprite('el450_19', 6)	# 490-495
    sprite('el450_20', 7)	# 496-502
    sprite('el450_21', 1)	# 503-503
    GFX_0('elef450_cardA', 0)
    GFX_0('elef_cardlight', 0)
    GFX_0('elef_cardlight_add', 0)
    SFX_3('cloth_l')
    sprite('el450_21', 9)	# 504-512
    SFX_3('cloth_l')
    sprite('el450_22', 10)	# 513-522
    sprite('el450_23', 1)	# 523-523
    Unknown26('elef450_cardA')
    GFX_0('elef450_cardB', 0)
    SFX_3('cloth_l')
    sprite('el450_23', 5)	# 524-528
    SFX_3('cloth_l')
    sprite('el450_24', 6)	# 529-534
    tag_voice(1, 'pel291_0', 'pel291_1', '', '')
    sprite('el450_25', 75)	# 535-609
    GFX_0('IchigekiPicture', 100)
    sprite('el450_25', 60)	# 610-669
    sprite('el450_26', 15)	# 670-684
    Unknown21012('4963686967656b6950696374757265000000000000000000000000000000000020000000')
    sprite('el450_27', 6)	# 685-690
    Unknown26('elef_cardlight')
    Unknown26('elef_cardlight_add')
    Unknown26('elef450_cardB')
    GFX_1('elef_card_ply', 0)
    SFX_3('persona_destroy')
    sprite('el450_28', 4)	# 691-694
    Unknown23029(11, 6001, 0)
    GFX_0('elef450_MegidoraJon', 100)
    sprite('el450_29', 4)	# 695-698
    sprite('el450_30', 4)	# 699-702
    sprite('el450_28', 4)	# 703-706
    sprite('el450_29', 4)	# 707-710
    sprite('el450_30', 4)	# 711-714
    sprite('el450_28', 4)	# 715-718
    tag_voice(0, 'pel292_0', 'pel292_1', '', '')
    sprite('el450_29', 4)	# 719-722
    sprite('el450_30', 4)	# 723-726
    sprite('el450_28', 4)	# 727-730
    sprite('el450_29', 4)	# 731-734
    sprite('el450_30', 4)	# 735-738
    sprite('el450_28', 4)	# 739-742
    sprite('el450_29', 4)	# 743-746
    sprite('el450_30', 4)	# 747-750
    sprite('el450_28', 4)	# 751-754
    sprite('el450_29', 4)	# 755-758
    sprite('el450_30', 4)	# 759-762
    sprite('el450_28', 4)	# 763-766
    sprite('el450_29', 4)	# 767-770
    sprite('el450_30', 4)	# 771-774
    sprite('el450_28', 4)	# 775-778
    sprite('el450_29', 4)	# 779-782
    sprite('el450_30', 4)	# 783-786
    sprite('el450_28', 4)	# 787-790
    sprite('el450_29', 4)	# 791-794
    sprite('el450_30', 4)	# 795-798
    sprite('el450_28', 4)	# 799-802
    sprite('el450_29', 4)	# 803-806
    sprite('el450_30', 4)	# 807-810
    sprite('el450_28', 4)	# 811-814
    sprite('el450_29', 4)	# 815-818
    sprite('el450_30', 4)	# 819-822
    sprite('el450_28', 4)	# 823-826
    sprite('el450_29', 4)	# 827-830
    sprite('el450_30', 4)	# 831-834
    sprite('el450_28', 4)	# 835-838
    sprite('el450_29', 4)	# 839-842
    sprite('el450_30', 4)	# 843-846
    sprite('el450_28', 4)	# 847-850
    sprite('el450_29', 4)	# 851-854
    sprite('el450_30', 4)	# 855-858
    sprite('el450_28', 4)	# 859-862
    sprite('el450_29', 4)	# 863-866
    sprite('el450_30', 4)	# 867-870
    sprite('el450_28', 4)	# 871-874
    sprite('el450_29', 4)	# 875-878
    sprite('el450_30', 4)	# 879-882
    sprite('el450_28', 4)	# 883-886
    sprite('el450_29', 4)	# 887-890
    sprite('el450_30', 4)	# 891-894
    sprite('el450_28', 4)	# 895-898
    sprite('el450_29', 4)	# 899-902
    sprite('el450_30', 4)	# 903-906
    sprite('el450_31', 4)	# 907-910
    SFX_3('el004')
    sprite('el450_32', 4)	# 911-914
    tag_voice(0, 'pel293_0', 'pel293_1', '', '')
    sprite('el450_33', 4)	# 915-918
    sprite('el450_34', 4)	# 919-922
    Unknown4004('534345465f536861736861496e0000000000000000000000000000000000000064000000')
    sprite('el450_35', 4)	# 923-926	 **attackbox here**
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    Unknown21007(11, 32)
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown35()
    sprite('el450_35', 20)	# 927-946	 **attackbox here**
    SFX_3('el004')
    Unknown3038(1)
    teleportRelativeY(240000)
    Unknown36(22)
    Unknown23119(-1, 500, 1)
    Unknown35()
    Unknown20009(3000)
    Unknown20002(1)
    Unknown20003(1)
    Unknown21012('656c65663435305f4d656769646f72614a6f6e0000000000000000000000000020000000')
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown4004('534345465f5368617368614f757400000000000000000000000000000000000064000000')
    Unknown26('SCEF_ShashaIn')
    sprite('el450_35', 20)	# 947-966	 **attackbox here**
    SFX_3('el004')
    sprite('el450_35', 20)	# 967-986	 **attackbox here**
    SFX_3('el004')
    sprite('el450_35', 20)	# 987-1006	 **attackbox here**
    SFX_3('el004')
    sprite('el450_35', 20)	# 1007-1026	 **attackbox here**
    SFX_3('el004')
    label(2)
    sprite('el450_35', 100)	# 1027-1126	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(100)
    sprite('el450_35', 8)	# 1127-1134	 **attackbox here**
    GFX_0('elef450_DamageNum', 100)
    ScreenShake(15000, 15000)
    SFX_3('el005')
    Unknown36(22)
    Unknown3038(1)
    Unknown35()
    sprite('el450_35', 2)	# 1135-1136	 **attackbox here**
    SFX_3('el054')
    sprite('el450_35', 2)	# 1137-1138	 **attackbox here**
    SFX_3('el054')
    sprite('el450_35', 2)	# 1139-1140	 **attackbox here**
    SFX_3('blaze_long')
    sprite('el450_35', 16)	# 1141-1156	 **attackbox here**
    SFX_3('blaze_long')
    sprite('el450_35', 30)	# 1157-1186	 **attackbox here**
    RefreshMultihit()
    Unknown11023(1)
    AttackLevel_(5)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Damage(99999)
    MinimumDamagePct(100)
    Unknown11064(4)
    AirPushbackY(64000)
    YImpluseBeforeWallbounce(1500)
    Unknown36(22)
    Unknown3038(0)
    Unknown23119(-16777216, 120, 1)
    Unknown35()
    Unknown21012('437574696e62670000000000000000000000000000000000000000000000000020000000')
    sprite('el450_35', 30)	# 1187-1216	 **attackbox here**
    Unknown20009(1000)
    Unknown20002(0)
    Unknown20003(0)
    sprite('el000_00', 20)	# 1217-1236
    Unknown23024(0)
    teleportRelativeY(0)
    Unknown3038(0)
    Unknown20000(1)
    Unknown20004(1)
    Unknown20006(1)
    Unknown20003(1)
    sprite('el000_00', 6)	# 1237-1242
    sprite('el000_01', 6)	# 1243-1248
    sprite('el000_02', 6)	# 1249-1254
    sprite('el000_03', 6)	# 1255-1260
    sprite('el000_04', 6)	# 1261-1266
    sprite('el000_05', 6)	# 1267-1272
    sprite('el000_06', 6)	# 1273-1278
    sprite('el000_07', 6)	# 1279-1284
    sprite('el000_08', 6)	# 1285-1290
    sprite('el000_09', 6)	# 1291-1296
    sprite('el000_10', 6)	# 1297-1302
    sprite('el000_11', 6)	# 1303-1308
    sprite('el000_12', 6)	# 1309-1314
    sprite('el000_13', 6)	# 1315-1320
    sprite('el000_14', 6)	# 1321-1326
    sprite('el000_15', 6)	# 1327-1332

@Subroutine
def MouthTableInit():
    Unknown18011('pel000', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pel600def', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel600def', '001')
    Unknown18011('pel601def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601def', '002')
    Unknown18011('pel602def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel602def', '003')
    Unknown18011('pel603def', 12899, 13921, 13923, 13921, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13361, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel603def', '004')
    Unknown18011('pel604def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24888, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel604def', '005')
    Unknown18011('pel605def', 12899, 14689, 14691, 13153, 25392, 12338, 13153, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel605def', '006')
    Unknown18011('pel700def', 12643, 14689, 14691, 14689, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel700def', '007')
    Unknown18011('pel701def', 13411, 14689, 14179, 14689, 14179, 14177, 14179, 14689, 14179, 14177, 14179, 14177, 14179, 14689, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701def', '008')
    Unknown18011('pel702def', 12643, 13409, 25392, 12337, 12641, 25401, 24888, 14385, 12643, 24880, 14641, 14435, 12641, 25392, 14385, 13153, 25392, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel702def', '009')
    Unknown18011('pel703def', 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13155, 24884, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel703def', '010')
    Unknown18011('pel704def', 13155, 12641, 25392, 24887, 12337, 14179, 13921, 13923, 13921, 13155, 24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 14641, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel704def', '011')
    Unknown18011('pel705def', 13155, 12641, 25392, 12337, 14689, 13155, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14388, 12641, 25393, 12593, 12897, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel705def', '012')
    Unknown18011('pel402_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pel402_1', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 12643, 24888, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pel403_0', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pel403_1', 12899, 14433, 14435, 13921, 13923, 13921, 13923, 13921, 12643, 24888, 25400, 14385, 14433, 14435, 14433, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pel601brc', 12899, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13155, 24887, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601brc', '017')
    Unknown18011('pel601bny', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24886, 25400, 24888, 25400, 24888, 25400, 12850, 12641, 25394, 12849, 12641, 25394, 12849, 12641, 25394, 12849, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601bny', '018 ')
    Unknown18011('pel601baz', 13155, 13665, 13667, 13665, 13155, 24882, 25398, 13875, 14689, 14691, 14689, 14691, 14689, 14691, 14689, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601baz', '019')
    Unknown18011('pel601bph', 12641, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12897, 25399, 24889, 25401, 24889, 25401, 24889, 25401, 24889, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601bph', '020')
    Unknown18011('pel601pbc', 13153, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12341, 12899, 24880, 13873, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601pbc', '021')
    Unknown18011('pel603pbc', 13411, 14177, 14179, 14177, 14179, 14177, 13411, 12641, 25392, 24887, 13621, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel603pbc', '022')
    Unknown18011('pel601pmi', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24889, 12337, 12643, 24881, 25400, 24889, 25398, 24886, 25398, 24886, 12849, 14179, 14177, 13155, 24884, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601pmi', '023')
    Unknown18011('pel601pag', 13411, 14433, 14435, 14433, 14435, 14433, 12899, 24887, 25400, 24888, 25400, 24888, 25400, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601pag', '024')
    Unknown18011('pel601uli', 12897, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 13153, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601uli', '025')
    Unknown18011('pel601uor', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601uor', '026')
    Unknown18011('pel601uva', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25397, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 12337, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601uva', '027')
    Unknown18011('pel601rwi', 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24889, 14386, 12643, 24882, 12339, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 13361, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601rwi', '028')
    Unknown18011('pel601uhi', 14177, 14179, 14177, 14179, 14177, 14691, 12643, 24888, 13361, 12643, 24886, 14129, 12643, 24887, 12849, 12643, 24883, 14129, 12899, 24880, 12337, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13873, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601uhi', '029')
    Unknown18011('pel601bce', 13923, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13667, 24887, 25398, 24886, 25398, 24886, 25398, 14386, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel601bce', '030')
    Unknown18011('pel701brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25398, 14385, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 12643, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701brc', '031')
    Unknown18011('pel701bny', 12899, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25400, 24888, 25400, 24888, 25400, 13873, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701bny', '032')
    Unknown18011('pel701baz', 12899, 14177, 14179, 14177, 14179, 14177, 13155, 24884, 14385, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701baz', '033')
    Unknown18011('pel701bph', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701bph', '034')
    Unknown18011('pel700pbc', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 13105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel700pbc', '035')
    Unknown18011('pel701pmi', 12899, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25393, 12851, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701pmi', '036')
    Unknown18011('pel701pag', 12643, 14433, 14435, 14433, 14435, 14433, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701pag', '037')
    Unknown18011('pel701uli', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701uli', '038')
    Unknown18011('pel701uor', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25401, 24889, 25401, 24889, 25401, 13361, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701uor', '039')
    Unknown18011('pel701uva', 12899, 14433, 14435, 14433, 14435, 14433, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25401, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701uva', '040')
    Unknown18011('pel700rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24883, 25401, 24889, 25401, 24889, 25401, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12850, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel700rwi', '041')
    Unknown18011('pel701uhi', 13411, 14177, 14179, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12849, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel701uhi', '042')
    Unknown18011('pel700bce', 12897, 14179, 14177, 14179, 14433, 12641, 25395, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pel700bce', '043')
    if SLOT_172:
        Unknown18011('pel000', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 14177, 14179, 14177, 14179, 12897, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel600def', 12643, 12643, 14177, 14179, 14177, 13667, 14435, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 24882, 25399, 25398, 24882, 25399, 25398, 24881, 25399, 24887, 25399, 24887, 25397, 24881, 25399, 25399, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13411, 14177, 14179, 13921, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel602def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 13155, 14177, 13155, 13155, 14177, 14179, 12641, 12643, 14177, 12899, 13923, 13921, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel603def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 24884, 25399, 24887, 25399, 25396, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 24886, 25399, 24887, 25396, 24881, 25399, 24887, 25399, 25393, 24887, 25393, 24884, 25395, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel604def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 13409, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel605def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel700def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13667, 14177, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13155, 14177, 12643, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel702def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 12641, 12643, 14177, 14179, 13153, 13411, 13409, 12643, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 12337, 14177, 13667, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel703def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 24880, 25399, 24887, 25398, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel704def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 14177, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel705def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 14177, 14179, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 25394, 24883, 25399, 24887, 25399, 24887, 25399, 25394, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24881, 25399, 24887, 25393, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 51, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel402_0', 12643, 12643, 14177, 14179, 14177, 13411, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel402_1', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel403_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14177, 12899, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 14177, 14179, 13153, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel403_1', 12643, 12643, 13921, 12643, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 14177, 12899, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601brc', 12643, 12643, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24883, 25399, 24887, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24881, 25399, 24887, 25399, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601baz', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 14177, 14179, 12641, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 13665, 12643, 14177, 14179, 13665, 14179, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601pbc', 12643, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 25398, 24881, 25399, 25398, 24886, 25399, 24887, 25394, 24881, 25396, 24881, 25399, 25398, 24884, 25399, 24887, 25399, 24887, 25397, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel603pbc', 12643, 14177, 14179, 14177, 14179, 13665, 13155, 14177, 14179, 14177, 14179, 14177, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601pmi', 12643, 12643, 14177, 13923, 13155, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 13665, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 13155, 12643, 14177, 14179, 13665, 12643, 14177, 13155, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13411, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601uli', 12643, 12643, 14177, 14179, 14177, 14179, 13153, 12899, 12897, 12899, 14177, 14179, 14177, 13411, 13411, 14177, 14179, 14177, 12643, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 14177, 14179, 14177, 14179, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 14177, 14179, 14177, 14179, 14177, 13923, 13155, 14177, 14179, 14177, 13923, 13923, 14177, 14179, 13665, 12643, 14177, 14179, 14177, 13667, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601uva', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 14177, 14179, 14177, 12643, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 13665, 12643, 14177, 14179, 14177, 13667, 12899, 14177, 14179, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601rwi', 12643, 12643, 14177, 14179, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14691, 14177, 14179, 14177, 14179, 12897, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601uhi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel601bce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13155, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 24885, 25399, 25397, 24881, 25393, 24885, 25399, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701brc', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 14177, 14179, 14177, 12643, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701bny', 12643, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 13153, 13411, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701baz', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel700pbc', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 12641, 12899, 14177, 12899, 12899, 14177, 14179, 13665, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701pmi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 24886, 25399, 24887, 25399, 25396, 24884, 25399, 25397, 24884, 25399, 24881, 25399, 24887, 25399, 24887, 25393, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701pag', 12643, 12643, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 24883, 25399, 24887, 25399, 24887, 25394, 24884, 25399, 25393, 24883, 25399, 24887, 25399, 24887, 25393, 24883, 25399, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701uli', 12643, 12643, 14177, 14179, 14177, 14179, 13153, 12643, 24882, 25399, 25396, 24881, 25399, 24887, 25399, 25393, 24882, 25399, 25396, 24886, 25395, 24881, 25399, 24887, 25399, 24887, 25399, 25396, 24883, 25393, 24887, 25399, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701uor', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 14179, 14177, 14179, 13921, 13155, 14177, 14179, 14177, 14179, 14177, 12899, 14435, 14177, 14179, 12897, 12643, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701uva', 12643, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel700rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 14177, 13667, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel701uhi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12643, 14177, 14179, 12641, 13411, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pel700bce', 12643, 14177, 14179, 14177, 12899, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13667, 14177, 14179, 12641, 13155, 14177, 14179, 12641, 13411, 14177, 12899, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bny')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('baz')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bph')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('pbc')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('pmi')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('pag')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('uli')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('uor')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uva')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('rwi')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('uhi')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('bce')
    if SLOT_ReturnVal:
        _gotolabel(220)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('el600_00', 4)	# 2-5
    sprite('el600_01', 4)	# 6-9
    sprite('el600_02', 4)	# 10-13
    sprite('el600_03', 4)	# 14-17
    sprite('el600_04', 4)	# 18-21
    GFX_0('elef600_card', 0)
    if random_(2, 0, 50):
        Unknown7006('pel600def', 100, 913073520, 1701065008, 102, 0, 100, 913073520, 1701065264, 102, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown7006('pel603def', 100, 913073520, 1701065776, 102, 0, 100, 913073520, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0)
    sprite('el600_05', 4)	# 22-25
    sprite('el600_06', 4)	# 26-29
    sprite('el600_07', 4)	# 30-33
    sprite('el600_08', 4)	# 34-37
    Unknown2037(3)
    label(1)
    sprite('el600_09', 4)	# 38-41
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 42-45
    sprite('el600_11', 4)	# 46-49
    if SLOT_2:
        _gotolabel(1)
    sprite('el600_09', 4)	# 50-53
    Unknown23029(11, 9001, 0)
    sprite('el600_10', 4)	# 54-57
    sprite('el600_11', 4)	# 58-61
    Unknown2037(10)
    label(2)
    sprite('el600_09', 4)	# 62-65
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 66-69
    sprite('el600_11', 4)	# 70-73
    if SLOT_2:
        _gotolabel(2)
    sprite('el600_12', 6)	# 74-79
    Unknown23018(1)
    label(3)
    sprite('el000_00', 6)	# 80-85
    sprite('el000_01', 6)	# 86-91
    sprite('el000_02', 6)	# 92-97
    sprite('el000_03', 6)	# 98-103
    sprite('el000_04', 6)	# 104-109
    sprite('el000_05', 6)	# 110-115
    sprite('el000_06', 6)	# 116-121
    sprite('el000_07', 6)	# 122-127
    sprite('el000_08', 6)	# 128-133
    sprite('el000_09', 6)	# 134-139
    sprite('el000_10', 6)	# 140-145
    sprite('el000_11', 6)	# 146-151
    sprite('el000_12', 6)	# 152-157
    sprite('el000_13', 6)	# 158-163
    sprite('el000_14', 6)	# 164-169
    sprite('el000_15', 6)	# 170-175
    gotoLabel(3)
    ExitState()
    label(10)
    sprite('el601_00', 1)	# 176-176
    sendToLabelUpon(2, 11)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    setGravity(0)
    teleportRelativeY(600000)
    physicsYImpulse(-13000)
    Unknown23118(-128)
    Unknown23119(-16777216, 80, 1)
    GFX_0('elef601_EntryLight', 100)
    sprite('el601_00', 4)	# 177-180
    SFX_3('el051')
    sprite('el601_01', 4)	# 181-184
    sprite('el601_02', 4)	# 185-188
    sprite('el601_00', 4)	# 189-192
    sprite('el601_01', 4)	# 193-196
    sprite('el601_02', 4)	# 197-200
    sprite('el601_00', 4)	# 201-204
    sprite('el601_01', 4)	# 205-208
    sprite('el601_02', 4)	# 209-212
    SFX_3('el051')
    sprite('el601_00', 4)	# 213-216
    sprite('el601_01', 4)	# 217-220
    sprite('el601_02', 4)	# 221-224
    sprite('el601_00', 4)	# 225-228
    sprite('el601_01', 4)	# 229-232
    sprite('el601_02', 4)	# 233-236
    sprite('el601_00', 4)	# 237-240
    sprite('el601_01', 4)	# 241-244
    SFX_3('el051')
    sprite('el601_02', 4)	# 245-248
    sprite('el601_00', 4)	# 249-252
    sprite('el601_01', 4)	# 253-256
    sprite('el601_02', 4)	# 257-260
    sprite('el601_00', 4)	# 261-264
    sprite('el601_01', 4)	# 265-268
    sprite('el601_02', 4)	# 269-272
    sprite('el601_00', 4)	# 273-276
    SFX_3('el051')
    sprite('el601_01', 4)	# 277-280
    sprite('el601_02', 4)	# 281-284
    sprite('el601_00', 4)	# 285-288
    sprite('el601_01', 4)	# 289-292
    sprite('el601_02', 4)	# 293-296
    sprite('el601_00', 4)	# 297-300
    sprite('el601_01', 4)	# 301-304
    sprite('el601_02', 4)	# 305-308
    SFX_3('el051')
    sprite('el601_00', 4)	# 309-312
    sprite('el601_01', 4)	# 313-316
    sprite('el601_02', 4)	# 317-320
    label(11)
    sprite('el601_03', 1)	# 321-321
    clearUponHandler(3)
    Unknown21012('656c65663630315f456e7472794c69676874000000000000000000000000000020000000')
    if random_(2, 0, 50):
        Unknown7006('pel600def', 100, 913073520, 1701065008, 102, 0, 100, 913073520, 1701065264, 102, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown7006('pel603def', 100, 913073520, 1701065776, 102, 0, 100, 913073520, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0)
    sprite('el601_03', 9)	# 322-330
    SFX_3('walk_stone_light')
    sprite('el601_04', 4)	# 331-334
    sprite('el601_05', 4)	# 335-338
    sprite('el601_06', 4)	# 339-342
    sprite('el601_07', 6)	# 343-348
    sprite('el601_08', 4)	# 349-352
    GFX_0('elef601_EntryBookEff', 0)
    GFX_0('elef601_EntryBook', 0)
    SFX_3('distortion_a')
    sprite('el601_09', 4)	# 353-356
    sprite('el601_10', 4)	# 357-360
    sprite('el601_08', 4)	# 361-364
    sprite('el601_09', 4)	# 365-368
    sprite('el601_10', 4)	# 369-372
    sprite('el601_08', 4)	# 373-376
    sprite('el601_09', 4)	# 377-380
    sprite('el601_10', 4)	# 381-384
    sprite('el601_08', 4)	# 385-388
    sprite('el601_09', 4)	# 389-392
    sprite('el601_10', 4)	# 393-396
    sprite('el601_11', 4)	# 397-400
    Unknown26('elef601_EntryBook')
    SFX_3('walk_stone_heavy')
    sprite('el601_12', 10)	# 401-410
    sprite('el601_13', 7)	# 411-417
    Unknown23018(1)
    label(12)
    sprite('el000_00', 6)	# 418-423
    sprite('el000_01', 6)	# 424-429
    sprite('el000_02', 6)	# 430-435
    sprite('el000_03', 6)	# 436-441
    sprite('el000_04', 6)	# 442-447
    sprite('el000_05', 6)	# 448-453
    sprite('el000_06', 6)	# 454-459
    sprite('el000_07', 6)	# 460-465
    sprite('el000_08', 6)	# 466-471
    sprite('el000_09', 6)	# 472-477
    sprite('el000_10', 6)	# 478-483
    sprite('el000_11', 6)	# 484-489
    sprite('el000_12', 6)	# 490-495
    sprite('el000_13', 6)	# 496-501
    sprite('el000_14', 6)	# 502-507
    sprite('el000_15', 6)	# 508-513
    gotoLabel(12)
    label(100)
    sprite('el600_00', 1)	# 514-514
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('el600_00', 4)	# 515-518
    sprite('el600_01', 4)	# 519-522
    sprite('el600_02', 4)	# 523-526
    gotoLabel(101)
    label(102)
    sprite('el600_03', 4)	# 527-530
    sprite('el600_04', 4)	# 531-534
    GFX_0('elef600_card', 0)
    SFX_1('pel601brc')
    sprite('el600_05', 4)	# 535-538
    sprite('el600_06', 4)	# 539-542
    sprite('el600_07', 4)	# 543-546
    sprite('el600_08', 4)	# 547-550
    Unknown2037(3)
    label(103)
    sprite('el600_09', 4)	# 551-554
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 555-558
    sprite('el600_11', 4)	# 559-562
    if SLOT_2:
        _gotolabel(103)
    sprite('el600_09', 4)	# 563-566
    Unknown23029(11, 9001, 0)
    sprite('el600_10', 4)	# 567-570
    sprite('el600_11', 4)	# 571-574
    Unknown2037(10)
    label(104)
    sprite('el600_09', 4)	# 575-578
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 579-582
    sprite('el600_11', 4)	# 583-586
    if SLOT_2:
        _gotolabel(104)
    sprite('el600_12', 6)	# 587-592
    Unknown23018(1)
    label(105)
    sprite('el000_00', 6)	# 593-598
    sprite('el000_01', 6)	# 599-604
    sprite('el000_02', 6)	# 605-610
    sprite('el000_03', 6)	# 611-616
    sprite('el000_04', 6)	# 617-622
    sprite('el000_05', 6)	# 623-628
    sprite('el000_06', 6)	# 629-634
    sprite('el000_07', 6)	# 635-640
    sprite('el000_08', 6)	# 641-646
    sprite('el000_09', 6)	# 647-652
    sprite('el000_10', 6)	# 653-658
    sprite('el000_11', 6)	# 659-664
    sprite('el000_12', 6)	# 665-670
    sprite('el000_13', 6)	# 671-676
    sprite('el000_14', 6)	# 677-682
    sprite('el000_15', 6)	# 683-688
    gotoLabel(105)
    label(110)
    sprite('el600_00', 1)	# 689-689
    Unknown2037(75)

    def upon_40():
        clearUponHandler(40)
        SFX_1('pel601bny')

        def upon_CLEAR_OR_EXIT():
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                sendToLabel(112)
    label(111)
    sprite('el600_00', 4)	# 690-693
    sprite('el600_01', 4)	# 694-697
    sprite('el600_02', 4)	# 698-701
    gotoLabel(111)
    label(112)
    sprite('el600_03', 4)	# 702-705
    sprite('el600_04', 4)	# 706-709
    GFX_0('elef600_card', 0)
    sprite('el600_05', 4)	# 710-713
    sprite('el600_06', 4)	# 714-717
    sprite('el600_07', 4)	# 718-721
    sprite('el600_08', 4)	# 722-725
    Unknown2037(3)
    label(113)
    sprite('el600_09', 4)	# 726-729
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 730-733
    sprite('el600_11', 4)	# 734-737
    if SLOT_2:
        _gotolabel(113)
    sprite('el600_09', 4)	# 738-741
    Unknown23029(11, 9001, 0)
    sprite('el600_10', 4)	# 742-745
    sprite('el600_11', 4)	# 746-749
    Unknown2037(10)
    label(114)
    sprite('el600_09', 4)	# 750-753
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 754-757
    sprite('el600_11', 4)	# 758-761
    if SLOT_2:
        _gotolabel(114)
    sprite('el600_12', 6)	# 762-767
    Unknown21011(30)
    label(115)
    sprite('el000_00', 6)	# 768-773
    sprite('el000_01', 6)	# 774-779
    sprite('el000_02', 6)	# 780-785
    sprite('el000_03', 6)	# 786-791
    sprite('el000_04', 6)	# 792-797
    sprite('el000_05', 6)	# 798-803
    sprite('el000_06', 6)	# 804-809
    sprite('el000_07', 6)	# 810-815
    sprite('el000_08', 6)	# 816-821
    sprite('el000_09', 6)	# 822-827
    sprite('el000_10', 6)	# 828-833
    sprite('el000_11', 6)	# 834-839
    sprite('el000_12', 6)	# 840-845
    sprite('el000_13', 6)	# 846-851
    sprite('el000_14', 6)	# 852-857
    sprite('el000_15', 6)	# 858-863
    gotoLabel(115)
    label(120)
    sprite('el000_00', 6)	# 864-869
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('el000_01', 6)	# 870-875
    sprite('el000_02', 6)	# 876-881
    sprite('el000_03', 6)	# 882-887
    sprite('el000_04', 6)	# 888-893
    sprite('el000_05', 6)	# 894-899
    sprite('el000_06', 6)	# 900-905
    sprite('el000_07', 6)	# 906-911
    sprite('el000_08', 6)	# 912-917
    sprite('el000_09', 6)	# 918-923
    sprite('el000_10', 6)	# 924-929
    sprite('el000_11', 6)	# 930-935
    sprite('el000_12', 6)	# 936-941
    sprite('el000_13', 6)	# 942-947
    sprite('el000_14', 6)	# 948-953
    sprite('el000_15', 6)	# 954-959
    sprite('el000_00', 6)	# 960-965
    gotoLabel(121)
    label(122)
    sprite('el610_00', 35)	# 966-1000
    SFX_1('pel601baz')
    sprite('el610_01', 6)	# 1001-1006
    sprite('el610_02', 25)	# 1007-1031
    sprite('el610_03', 6)	# 1032-1037
    sprite('el610_04', 6)	# 1038-1043
    sprite('el610_05', 60)	# 1044-1103
    label(123)
    sprite('el610_05', 1)	# 1104-1104
    if SLOT_97:
        _gotolabel(123)
    sprite('el610_04', 6)	# 1105-1110
    sprite('el610_03', 6)	# 1111-1116
    sprite('el610_02', 6)	# 1117-1122
    sprite('el610_01', 6)	# 1123-1128
    Unknown23018(1)
    label(124)
    sprite('el000_00', 6)	# 1129-1134
    sprite('el000_01', 6)	# 1135-1140
    sprite('el000_02', 6)	# 1141-1146
    sprite('el000_03', 6)	# 1147-1152
    sprite('el000_04', 6)	# 1153-1158
    sprite('el000_05', 6)	# 1159-1164
    sprite('el000_06', 6)	# 1165-1170
    sprite('el000_07', 6)	# 1171-1176
    sprite('el000_08', 6)	# 1177-1182
    sprite('el000_09', 6)	# 1183-1188
    sprite('el000_10', 6)	# 1189-1194
    sprite('el000_11', 6)	# 1195-1200
    sprite('el000_12', 6)	# 1201-1206
    sprite('el000_13', 6)	# 1207-1212
    sprite('el000_14', 6)	# 1213-1218
    sprite('el000_15', 6)	# 1219-1224
    gotoLabel(124)
    label(130)
    sprite('el000_00', 6)	# 1225-1230

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('el000_01', 6)	# 1231-1236
    sprite('el000_02', 6)	# 1237-1242
    sprite('el000_03', 6)	# 1243-1248
    sprite('el000_04', 6)	# 1249-1254
    sprite('el000_05', 6)	# 1255-1260
    sprite('el000_06', 6)	# 1261-1266
    sprite('el000_07', 6)	# 1267-1272
    sprite('el000_08', 6)	# 1273-1278
    sprite('el000_09', 6)	# 1279-1284
    sprite('el000_10', 6)	# 1285-1290
    sprite('el000_11', 6)	# 1291-1296
    sprite('el000_12', 6)	# 1297-1302
    sprite('el000_13', 6)	# 1303-1308
    sprite('el000_14', 6)	# 1309-1314
    sprite('el000_15', 6)	# 1315-1320
    sprite('el000_00', 6)	# 1321-1326
    gotoLabel(131)
    label(132)
    sprite('el433_00', 3)	# 1327-1329
    sprite('el433_01', 4)	# 1330-1333
    callSubroutine('PersonaCard_ON')
    sprite('el433_02', 4)	# 1334-1337
    sprite('el433_00', 4)	# 1338-1341
    sprite('el433_01', 4)	# 1342-1345
    sprite('el433_02', 4)	# 1346-1349
    sprite('el433_00', 4)	# 1350-1353
    sprite('el433_01', 4)	# 1354-1357
    sprite('el433_02', 4)	# 1358-1361
    sprite('el433_00', 4)	# 1362-1365
    sprite('el433_01', 4)	# 1366-1369
    sprite('el433_02', 4)	# 1370-1373
    sprite('el433_03', 4)	# 1374-1377
    Unknown23029(11, 9002, 0)
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 1378-1381
    sprite('el433_05', 4)	# 1382-1385
    sprite('el433_06', 4)	# 1386-1389
    sprite('el433_07', 4)	# 1390-1393
    sprite('el433_08', 4)	# 1394-1397
    sprite('el433_09', 4)	# 1398-1401
    SFX_1('pel601bph')
    sprite('el433_10', 4)	# 1402-1405
    sprite('el433_11', 4)	# 1406-1409
    sprite('el433_09', 4)	# 1410-1413
    Unknown23018(1)
    label(133)
    sprite('el433_10', 4)	# 1414-1417
    sprite('el433_11', 4)	# 1418-1421
    sprite('el433_09', 4)	# 1422-1425
    gotoLabel(133)
    label(140)
    sprite('el433_00', 3)	# 1426-1428

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    sprite('el433_01', 4)	# 1429-1432
    callSubroutine('PersonaCard_ON')
    sprite('el433_02', 4)	# 1433-1436
    label(141)
    sprite('el433_00', 4)	# 1437-1440
    sprite('el433_01', 4)	# 1441-1444
    sprite('el433_02', 4)	# 1445-1448
    gotoLabel(141)
    label(142)
    sprite('el433_03', 4)	# 1449-1452
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 1453-1456
    sprite('el433_05', 4)	# 1457-1460
    sprite('el433_06', 4)	# 1461-1464
    sprite('el433_07', 4)	# 1465-1468
    sprite('el433_08', 4)	# 1469-1472
    SFX_1('pel601pbc')
    label(143)
    sprite('el433_09', 4)	# 1473-1476
    sprite('el433_10', 4)	# 1477-1480
    sprite('el433_11', 4)	# 1481-1484
    if SLOT_97:
        _gotolabel(143)
    sprite('el433_09', 4)	# 1485-1488
    sprite('el433_10', 4)	# 1489-1492
    sprite('el433_11', 4)	# 1493-1496
    sprite('el433_09', 4)	# 1497-1500
    sprite('el433_12', 4)	# 1501-1504
    sprite('el433_13', 4)	# 1505-1508
    Unknown21007(24, 40)
    sprite('el431_00', 4)	# 1509-1512
    sprite('el431_00', 4)	# 1513-1516
    SFX_3('el001')
    sprite('el431_01', 4)	# 1517-1520
    sprite('el431_02', 4)	# 1521-1524
    sprite('el431_03', 4)	# 1525-1528
    GFX_0('elef431_CardPickUp', 0)
    Unknown38(7, 1)
    sprite('el431_04', 4)	# 1529-1532
    sprite('el431_05', 4)	# 1533-1536
    sprite('el431_03', 4)	# 1537-1540
    sprite('el431_04', 4)	# 1541-1544
    sprite('el431_05', 4)	# 1545-1548
    sprite('el431_03', 4)	# 1549-1552
    sprite('el431_04', 4)	# 1553-1556
    sprite('el431_05', 4)	# 1557-1560
    sprite('el431_03', 4)	# 1561-1564
    sprite('el431_04', 4)	# 1565-1568
    sprite('el431_05', 4)	# 1569-1572
    sprite('el431_03', 4)	# 1573-1576
    sprite('el431_04', 4)	# 1577-1580
    sprite('el431_05', 4)	# 1581-1584
    sprite('el431_03', 4)	# 1585-1588
    sprite('el431_04', 4)	# 1589-1592
    sprite('el431_05', 4)	# 1593-1596
    sprite('el431_06', 4)	# 1597-1600
    Unknown23029(11, 9003, 0)
    sprite('el431_07', 4)	# 1601-1604
    sprite('el431_08', 4)	# 1605-1608
    Unknown21007(7, 32)
    Unknown23118(-1)
    Unknown23119(-16777216, 16, 1)
    sprite('el431_09', 4)	# 1609-1612
    SFX_1('pel603pbc')
    sprite('el431_10', 4)	# 1613-1616
    sprite('el431_11', 4)	# 1617-1620
    sprite('el431_09', 4)	# 1621-1624
    sprite('el431_10', 4)	# 1625-1628
    sprite('el431_11', 4)	# 1629-1632
    sprite('el431_09', 2)	# 1633-1634
    sprite('el431_09', 2)	# 1635-1636
    sprite('el431_10', 4)	# 1637-1640
    sprite('el431_11', 4)	# 1641-1644
    sprite('el431_09', 4)	# 1645-1648
    sprite('el431_10', 4)	# 1649-1652
    sprite('el431_11', 4)	# 1653-1656
    sprite('el431_09', 4)	# 1657-1660
    sprite('el431_10', 4)	# 1661-1664
    sprite('el431_11', 4)	# 1665-1668
    sprite('el431_09', 4)	# 1669-1672
    sprite('el431_10', 4)	# 1673-1676
    sprite('el431_11', 4)	# 1677-1680
    Unknown21011(60)
    label(144)
    sprite('el431_09', 4)	# 1681-1684
    sprite('el431_10', 4)	# 1685-1688
    sprite('el431_11', 4)	# 1689-1692
    gotoLabel(144)
    label(150)
    sprite('el600_00', 1)	# 1693-1693

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('el600_00', 4)	# 1694-1697
    sprite('el600_01', 4)	# 1698-1701
    sprite('el600_02', 4)	# 1702-1705
    gotoLabel(151)
    label(152)
    sprite('el600_03', 4)	# 1706-1709
    sprite('el600_04', 4)	# 1710-1713
    GFX_0('elef600_card', 0)
    SFX_1('pel601pmi')
    sprite('el600_05', 4)	# 1714-1717
    sprite('el600_06', 4)	# 1718-1721
    sprite('el600_07', 4)	# 1722-1725
    sprite('el600_08', 4)	# 1726-1729
    Unknown2037(3)
    label(153)
    sprite('el600_09', 4)	# 1730-1733
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 1734-1737
    sprite('el600_11', 4)	# 1738-1741
    if SLOT_2:
        _gotolabel(153)
    sprite('el600_09', 4)	# 1742-1745
    Unknown23029(11, 9001, 0)
    sprite('el600_10', 4)	# 1746-1749
    sprite('el600_11', 4)	# 1750-1753
    Unknown2037(10)
    label(154)
    sprite('el600_09', 4)	# 1754-1757
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 1758-1761
    sprite('el600_11', 4)	# 1762-1765
    if SLOT_2:
        _gotolabel(154)
    sprite('el600_12', 6)	# 1766-1771
    Unknown23018(1)
    label(155)
    sprite('el000_00', 6)	# 1772-1777
    sprite('el000_01', 6)	# 1778-1783
    sprite('el000_02', 6)	# 1784-1789
    sprite('el000_03', 6)	# 1790-1795
    sprite('el000_04', 6)	# 1796-1801
    sprite('el000_05', 6)	# 1802-1807
    sprite('el000_06', 6)	# 1808-1813
    sprite('el000_07', 6)	# 1814-1819
    sprite('el000_08', 6)	# 1820-1825
    sprite('el000_09', 6)	# 1826-1831
    sprite('el000_10', 6)	# 1832-1837
    sprite('el000_11', 6)	# 1838-1843
    sprite('el000_12', 6)	# 1844-1849
    sprite('el000_13', 6)	# 1850-1855
    sprite('el000_14', 6)	# 1856-1861
    sprite('el000_15', 6)	# 1862-1867
    gotoLabel(155)
    label(160)
    sprite('el000_00', 6)	# 1868-1873

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('el000_01', 6)	# 1874-1879
    sprite('el000_02', 6)	# 1880-1885
    sprite('el000_03', 6)	# 1886-1891
    sprite('el000_04', 6)	# 1892-1897
    sprite('el000_05', 6)	# 1898-1903
    sprite('el000_06', 6)	# 1904-1909
    sprite('el000_07', 6)	# 1910-1915
    sprite('el000_08', 6)	# 1916-1921
    sprite('el000_09', 6)	# 1922-1927
    sprite('el000_10', 6)	# 1928-1933
    sprite('el000_11', 6)	# 1934-1939
    sprite('el000_12', 6)	# 1940-1945
    sprite('el000_13', 6)	# 1946-1951
    sprite('el000_14', 6)	# 1952-1957
    sprite('el000_15', 6)	# 1958-1963
    sprite('el000_00', 6)	# 1964-1969
    gotoLabel(161)
    label(162)
    sprite('el610_00', 35)	# 1970-2004
    SFX_1('pel601pag')
    sprite('el610_01', 6)	# 2005-2010
    sprite('el610_02', 25)	# 2011-2035
    sprite('el610_03', 6)	# 2036-2041
    sprite('el610_04', 6)	# 2042-2047
    sprite('el610_05', 60)	# 2048-2107
    label(163)
    sprite('el610_05', 1)	# 2108-2108
    if SLOT_97:
        _gotolabel(163)
    sprite('el610_05', 10)	# 2109-2118
    sprite('el610_04', 6)	# 2119-2124
    sprite('el610_03', 6)	# 2125-2130
    sprite('el610_02', 6)	# 2131-2136
    sprite('el610_01', 6)	# 2137-2142
    Unknown23018(1)
    label(164)
    sprite('el000_00', 6)	# 2143-2148
    sprite('el000_01', 6)	# 2149-2154
    sprite('el000_02', 6)	# 2155-2160
    sprite('el000_03', 6)	# 2161-2166
    sprite('el000_04', 6)	# 2167-2172
    sprite('el000_05', 6)	# 2173-2178
    sprite('el000_06', 6)	# 2179-2184
    sprite('el000_07', 6)	# 2185-2190
    sprite('el000_08', 6)	# 2191-2196
    sprite('el000_09', 6)	# 2197-2202
    sprite('el000_10', 6)	# 2203-2208
    sprite('el000_11', 6)	# 2209-2214
    sprite('el000_12', 6)	# 2215-2220
    sprite('el000_13', 6)	# 2221-2226
    sprite('el000_14', 6)	# 2227-2232
    sprite('el000_15', 6)	# 2233-2238
    gotoLabel(164)
    label(170)
    sprite('el000_00', 6)	# 2239-2244

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('el000_01', 6)	# 2245-2250
    sprite('el000_02', 6)	# 2251-2256
    sprite('el000_03', 6)	# 2257-2262
    sprite('el000_04', 6)	# 2263-2268
    sprite('el000_05', 6)	# 2269-2274
    sprite('el000_06', 6)	# 2275-2280
    sprite('el000_07', 6)	# 2281-2286
    sprite('el000_08', 6)	# 2287-2292
    sprite('el000_09', 6)	# 2293-2298
    sprite('el000_10', 6)	# 2299-2304
    sprite('el000_11', 6)	# 2305-2310
    sprite('el000_12', 6)	# 2311-2316
    sprite('el000_13', 6)	# 2317-2322
    sprite('el000_14', 6)	# 2323-2328
    sprite('el000_15', 6)	# 2329-2334
    sprite('el000_00', 6)	# 2335-2340
    gotoLabel(171)
    label(172)
    sprite('el433_00', 3)	# 2341-2343
    sprite('el433_01', 4)	# 2344-2347
    callSubroutine('PersonaCard_ON')
    sprite('el433_02', 4)	# 2348-2351
    sprite('el433_00', 4)	# 2352-2355
    sprite('el433_01', 4)	# 2356-2359
    sprite('el433_02', 4)	# 2360-2363
    sprite('el433_00', 4)	# 2364-2367
    sprite('el433_01', 4)	# 2368-2371
    sprite('el433_02', 4)	# 2372-2375
    sprite('el433_00', 4)	# 2376-2379
    sprite('el433_01', 4)	# 2380-2383
    sprite('el433_02', 4)	# 2384-2387
    sprite('el433_03', 4)	# 2388-2391
    Unknown23029(11, 9002, 0)
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 2392-2395
    sprite('el433_05', 4)	# 2396-2399
    sprite('el433_06', 4)	# 2400-2403
    sprite('el433_07', 4)	# 2404-2407
    sprite('el433_08', 4)	# 2408-2411
    sprite('el433_09', 4)	# 2412-2415
    SFX_1('pel601uli')
    sprite('el433_10', 4)	# 2416-2419
    sprite('el433_11', 4)	# 2420-2423
    sprite('el433_09', 4)	# 2424-2427
    Unknown23018(1)
    label(173)
    sprite('el433_10', 4)	# 2428-2431
    sprite('el433_11', 4)	# 2432-2435
    sprite('el433_09', 4)	# 2436-2439
    gotoLabel(173)
    label(180)
    sprite('el000_00', 6)	# 2440-2445
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('el000_01', 6)	# 2446-2451
    sprite('el000_02', 6)	# 2452-2457
    sprite('el000_03', 6)	# 2458-2463
    sprite('el000_04', 6)	# 2464-2469
    sprite('el000_05', 6)	# 2470-2475
    sprite('el000_06', 6)	# 2476-2481
    sprite('el000_07', 6)	# 2482-2487
    sprite('el000_08', 6)	# 2488-2493
    sprite('el000_09', 6)	# 2494-2499
    sprite('el000_10', 6)	# 2500-2505
    sprite('el000_11', 6)	# 2506-2511
    sprite('el000_12', 6)	# 2512-2517
    sprite('el000_13', 6)	# 2518-2523
    sprite('el000_14', 6)	# 2524-2529
    sprite('el000_15', 6)	# 2530-2535
    sprite('el000_00', 6)	# 2536-2541
    gotoLabel(181)
    label(182)
    sprite('el610_00', 35)	# 2542-2576
    SFX_1('pel601uor')
    sprite('el610_01', 6)	# 2577-2582
    sprite('el610_02', 25)	# 2583-2607
    sprite('el610_03', 6)	# 2608-2613
    sprite('el610_04', 6)	# 2614-2619
    sprite('el610_05', 60)	# 2620-2679
    label(183)
    sprite('el610_05', 1)	# 2680-2680
    if SLOT_97:
        _gotolabel(183)
    sprite('el610_05', 10)	# 2681-2690
    sprite('el610_04', 6)	# 2691-2696
    sprite('el610_03', 6)	# 2697-2702
    sprite('el610_02', 6)	# 2703-2708
    sprite('el610_01', 6)	# 2709-2714
    Unknown23018(1)
    label(184)
    sprite('el000_00', 6)	# 2715-2720
    sprite('el000_01', 6)	# 2721-2726
    sprite('el000_02', 6)	# 2727-2732
    sprite('el000_03', 6)	# 2733-2738
    sprite('el000_04', 6)	# 2739-2744
    sprite('el000_05', 6)	# 2745-2750
    sprite('el000_06', 6)	# 2751-2756
    sprite('el000_07', 6)	# 2757-2762
    sprite('el000_08', 6)	# 2763-2768
    sprite('el000_09', 6)	# 2769-2774
    sprite('el000_10', 6)	# 2775-2780
    sprite('el000_11', 6)	# 2781-2786
    sprite('el000_12', 6)	# 2787-2792
    sprite('el000_13', 6)	# 2793-2798
    sprite('el000_14', 6)	# 2799-2804
    sprite('el000_15', 6)	# 2805-2810
    gotoLabel(184)
    label(190)
    sprite('el000_00', 6)	# 2811-2816

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('el000_01', 6)	# 2817-2822
    sprite('el000_02', 6)	# 2823-2828
    sprite('el000_03', 6)	# 2829-2834
    sprite('el000_04', 6)	# 2835-2840
    sprite('el000_05', 6)	# 2841-2846
    sprite('el000_06', 6)	# 2847-2852
    sprite('el000_07', 6)	# 2853-2858
    sprite('el000_08', 6)	# 2859-2864
    sprite('el000_09', 6)	# 2865-2870
    sprite('el000_10', 6)	# 2871-2876
    sprite('el000_11', 6)	# 2877-2882
    sprite('el000_12', 6)	# 2883-2888
    sprite('el000_13', 6)	# 2889-2894
    sprite('el000_14', 6)	# 2895-2900
    sprite('el000_15', 6)	# 2901-2906
    sprite('el000_00', 6)	# 2907-2912
    gotoLabel(191)
    label(192)
    sprite('el433_00', 3)	# 2913-2915
    sprite('el433_01', 4)	# 2916-2919
    callSubroutine('PersonaCard_ON')
    sprite('el433_02', 4)	# 2920-2923
    sprite('el433_00', 4)	# 2924-2927
    sprite('el433_01', 4)	# 2928-2931
    sprite('el433_02', 4)	# 2932-2935
    sprite('el433_00', 4)	# 2936-2939
    sprite('el433_01', 4)	# 2940-2943
    sprite('el433_02', 4)	# 2944-2947
    sprite('el433_00', 4)	# 2948-2951
    sprite('el433_01', 4)	# 2952-2955
    sprite('el433_02', 4)	# 2956-2959
    sprite('el433_03', 4)	# 2960-2963
    Unknown23029(11, 9002, 0)
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 2964-2967
    sprite('el433_05', 4)	# 2968-2971
    sprite('el433_06', 4)	# 2972-2975
    sprite('el433_07', 4)	# 2976-2979
    sprite('el433_08', 4)	# 2980-2983
    sprite('el433_09', 4)	# 2984-2987
    SFX_1('pel601uva')
    sprite('el433_10', 4)	# 2988-2991
    sprite('el433_11', 4)	# 2992-2995
    sprite('el433_09', 4)	# 2996-2999
    Unknown23018(1)
    label(193)
    sprite('el433_10', 4)	# 3000-3003
    sprite('el433_11', 4)	# 3004-3007
    sprite('el433_09', 4)	# 3008-3011
    gotoLabel(193)
    label(200)
    sprite('el600_00', 1)	# 3012-3012

    def upon_40():
        clearUponHandler(40)
        SFX_1('pel601rwi')
        sendToLabel(202)
    label(201)
    sprite('el600_00', 4)	# 3013-3016
    sprite('el600_01', 4)	# 3017-3020
    sprite('el600_02', 4)	# 3021-3024
    gotoLabel(201)
    label(202)
    sprite('el600_00', 4)	# 3025-3028
    sprite('el600_01', 4)	# 3029-3032
    sprite('el600_02', 4)	# 3033-3036
    if SLOT_97:
        _gotolabel(202)
    sprite('el600_00', 4)	# 3037-3040
    sprite('el600_01', 4)	# 3041-3044
    sprite('el600_02', 4)	# 3045-3048
    sprite('el600_03', 4)	# 3049-3052
    sprite('el600_04', 4)	# 3053-3056
    GFX_0('elef600_card', 0)
    sprite('el600_05', 4)	# 3057-3060
    sprite('el600_06', 4)	# 3061-3064
    sprite('el600_07', 4)	# 3065-3068
    sprite('el600_08', 4)	# 3069-3072
    Unknown2037(3)
    label(203)
    sprite('el600_09', 4)	# 3073-3076
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 3077-3080
    sprite('el600_11', 4)	# 3081-3084
    if SLOT_2:
        _gotolabel(203)
    sprite('el600_09', 4)	# 3085-3088
    Unknown23029(11, 9001, 0)
    sprite('el600_10', 4)	# 3089-3092
    sprite('el600_11', 4)	# 3093-3096
    Unknown2037(10)
    label(204)
    sprite('el600_09', 4)	# 3097-3100
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 3101-3104
    sprite('el600_11', 4)	# 3105-3108
    if SLOT_2:
        _gotolabel(204)
    sprite('el600_12', 6)	# 3109-3114
    Unknown23018(1)
    label(205)
    sprite('el000_00', 6)	# 3115-3120
    sprite('el000_01', 6)	# 3121-3126
    sprite('el000_02', 6)	# 3127-3132
    sprite('el000_03', 6)	# 3133-3138
    sprite('el000_04', 6)	# 3139-3144
    sprite('el000_05', 6)	# 3145-3150
    sprite('el000_06', 6)	# 3151-3156
    sprite('el000_07', 6)	# 3157-3162
    sprite('el000_08', 6)	# 3163-3168
    sprite('el000_09', 6)	# 3169-3174
    sprite('el000_10', 6)	# 3175-3180
    sprite('el000_11', 6)	# 3181-3186
    sprite('el000_12', 6)	# 3187-3192
    sprite('el000_13', 6)	# 3193-3198
    sprite('el000_14', 6)	# 3199-3204
    sprite('el000_15', 6)	# 3205-3210
    gotoLabel(205)
    label(210)
    sprite('el601_00', 1)	# 3211-3211
    sendToLabelUpon(2, 211)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    setGravity(0)
    teleportRelativeY(600000)
    physicsYImpulse(-13000)
    Unknown23118(-128)
    Unknown23119(-16777216, 80, 1)
    GFX_0('elef601_EntryLight', 100)
    sprite('el601_00', 4)	# 3212-3215
    SFX_3('el051')
    sprite('el601_01', 4)	# 3216-3219
    sprite('el601_02', 4)	# 3220-3223
    sprite('el601_00', 4)	# 3224-3227
    sprite('el601_01', 4)	# 3228-3231
    sprite('el601_02', 4)	# 3232-3235
    sprite('el601_00', 4)	# 3236-3239
    sprite('el601_01', 4)	# 3240-3243
    sprite('el601_02', 4)	# 3244-3247
    SFX_3('el051')
    sprite('el601_00', 4)	# 3248-3251
    sprite('el601_01', 4)	# 3252-3255
    sprite('el601_02', 4)	# 3256-3259
    sprite('el601_00', 4)	# 3260-3263
    sprite('el601_01', 4)	# 3264-3267
    sprite('el601_02', 4)	# 3268-3271
    sprite('el601_00', 4)	# 3272-3275
    sprite('el601_01', 4)	# 3276-3279
    SFX_3('el051')
    sprite('el601_02', 4)	# 3280-3283
    sprite('el601_00', 4)	# 3284-3287
    sprite('el601_01', 4)	# 3288-3291
    sprite('el601_02', 4)	# 3292-3295
    sprite('el601_00', 4)	# 3296-3299
    sprite('el601_01', 4)	# 3300-3303
    sprite('el601_02', 4)	# 3304-3307
    sprite('el601_00', 4)	# 3308-3311
    SFX_3('el051')
    sprite('el601_01', 4)	# 3312-3315
    sprite('el601_02', 4)	# 3316-3319
    sprite('el601_00', 4)	# 3320-3323
    sprite('el601_01', 4)	# 3324-3327
    sprite('el601_02', 4)	# 3328-3331
    sprite('el601_00', 4)	# 3332-3335
    sprite('el601_01', 4)	# 3336-3339
    sprite('el601_02', 4)	# 3340-3343
    SFX_3('el051')
    sprite('el601_00', 4)	# 3344-3347
    sprite('el601_01', 4)	# 3348-3351
    sprite('el601_02', 4)	# 3352-3355
    label(211)
    sprite('el601_03', 1)	# 3356-3356
    clearUponHandler(3)
    Unknown21012('656c65663630315f456e7472794c69676874000000000000000000000000000020000000')
    sprite('el601_03', 9)	# 3357-3365
    SFX_3('walk_stone_light')
    sprite('el601_04', 4)	# 3366-3369
    sprite('el601_05', 4)	# 3370-3373
    sprite('el601_06', 4)	# 3374-3377
    sprite('el601_07', 6)	# 3378-3383
    sprite('el601_08', 4)	# 3384-3387
    GFX_0('elef601_EntryBookEff', 0)
    GFX_0('elef601_EntryBook', 0)
    SFX_3('distortion_a')
    sprite('el601_09', 4)	# 3388-3391
    sprite('el601_10', 4)	# 3392-3395
    sprite('el601_08', 4)	# 3396-3399
    sprite('el601_09', 4)	# 3400-3403
    sprite('el601_10', 4)	# 3404-3407
    sprite('el601_08', 4)	# 3408-3411
    sprite('el601_09', 4)	# 3412-3415
    sprite('el601_10', 4)	# 3416-3419
    sprite('el601_08', 4)	# 3420-3423
    sprite('el601_09', 4)	# 3424-3427
    sprite('el601_10', 4)	# 3428-3431
    sprite('el601_11', 4)	# 3432-3435
    Unknown26('elef601_EntryBook')
    SFX_3('walk_stone_heavy')
    sprite('el601_12', 10)	# 3436-3445
    sprite('el601_13', 7)	# 3446-3452
    sprite('el001_00', 6)	# 3453-3458

    def upon_40():
        clearUponHandler(40)
        sendToLabel(213)
    label(212)
    sprite('el000_00', 6)	# 3459-3464
    sprite('el000_01', 6)	# 3465-3470
    sprite('el000_02', 6)	# 3471-3476
    sprite('el000_03', 6)	# 3477-3482
    sprite('el000_04', 6)	# 3483-3488
    sprite('el000_05', 6)	# 3489-3494
    sprite('el000_06', 6)	# 3495-3500
    sprite('el000_07', 6)	# 3501-3506
    sprite('el000_08', 6)	# 3507-3512
    sprite('el000_09', 6)	# 3513-3518
    sprite('el000_10', 6)	# 3519-3524
    sprite('el000_11', 6)	# 3525-3530
    sprite('el000_12', 6)	# 3531-3536
    sprite('el000_13', 6)	# 3537-3542
    sprite('el000_14', 6)	# 3543-3548
    sprite('el000_15', 6)	# 3549-3554
    gotoLabel(212)
    label(213)
    sprite('el610_00', 35)	# 3555-3589
    SFX_1('pel601uhi')
    sprite('el610_01', 6)	# 3590-3595
    sprite('el610_02', 25)	# 3596-3620
    sprite('el610_03', 6)	# 3621-3626
    sprite('el610_04', 6)	# 3627-3632
    sprite('el610_05', 60)	# 3633-3692
    label(214)
    sprite('el610_05', 1)	# 3693-3693
    if SLOT_97:
        _gotolabel(214)
    sprite('el610_04', 6)	# 3694-3699
    sprite('el610_03', 6)	# 3700-3705
    sprite('el610_02', 6)	# 3706-3711
    sprite('el610_01', 6)	# 3712-3717
    Unknown23018(1)
    gotoLabel(212)
    label(220)
    sprite('el600_00', 1)	# 3718-3718
    Unknown1000(-1565000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('el600_00', 4)	# 3719-3722
    sprite('el600_01', 4)	# 3723-3726
    sprite('el600_02', 4)	# 3727-3730
    gotoLabel(221)
    label(222)
    sprite('el600_00', 4)	# 3731-3734
    sprite('el600_01', 4)	# 3735-3738
    SFX_1('pel601bce')
    sprite('el600_02', 4)	# 3739-3742
    sprite('el600_00', 4)	# 3743-3746
    sprite('el600_01', 4)	# 3747-3750
    sprite('el600_02', 4)	# 3751-3754
    sprite('el600_00', 4)	# 3755-3758
    sprite('el600_01', 4)	# 3759-3762
    sprite('el600_02', 4)	# 3763-3766
    sprite('el600_00', 4)	# 3767-3770
    sprite('el600_01', 4)	# 3771-3774
    sprite('el600_02', 4)	# 3775-3778
    sprite('el600_00', 4)	# 3779-3782
    sprite('el600_01', 4)	# 3783-3786
    sprite('el600_02', 4)	# 3787-3790
    sprite('el600_00', 4)	# 3791-3794
    sprite('el600_01', 4)	# 3795-3798
    sprite('el600_02', 4)	# 3799-3802
    sprite('el600_00', 4)	# 3803-3806
    sprite('el600_01', 4)	# 3807-3810
    sprite('el600_02', 4)	# 3811-3814
    sprite('el600_03', 4)	# 3815-3818
    sprite('el600_04', 4)	# 3819-3822
    GFX_0('elef600_card', 0)
    sprite('el600_05', 4)	# 3823-3826
    sprite('el600_06', 4)	# 3827-3830
    sprite('el600_07', 4)	# 3831-3834
    sprite('el600_08', 4)	# 3835-3838
    Unknown2037(3)
    label(223)
    sprite('el600_09', 4)	# 3839-3842
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 3843-3846
    sprite('el600_11', 4)	# 3847-3850
    if SLOT_2:
        _gotolabel(223)
    sprite('el600_09', 4)	# 3851-3854
    Unknown23029(11, 9001, 0)
    sprite('el600_10', 4)	# 3855-3858
    sprite('el600_11', 4)	# 3859-3862
    Unknown2037(10)
    label(224)
    sprite('el600_09', 4)	# 3863-3866
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 3867-3870
    sprite('el600_11', 4)	# 3871-3874
    if SLOT_2:
        _gotolabel(224)
    sprite('el600_12', 6)	# 3875-3880
    Unknown23018(1)
    label(225)
    sprite('el000_00', 6)	# 3881-3886
    sprite('el000_01', 6)	# 3887-3892
    sprite('el000_02', 6)	# 3893-3898
    sprite('el000_03', 6)	# 3899-3904
    sprite('el000_04', 6)	# 3905-3910
    sprite('el000_05', 6)	# 3911-3916
    sprite('el000_06', 6)	# 3917-3922
    sprite('el000_07', 6)	# 3923-3928
    sprite('el000_08', 6)	# 3929-3934
    sprite('el000_09', 6)	# 3935-3940
    sprite('el000_10', 6)	# 3941-3946
    sprite('el000_11', 6)	# 3947-3952
    sprite('el000_12', 6)	# 3953-3958
    sprite('el000_13', 6)	# 3959-3964
    sprite('el000_14', 6)	# 3965-3970
    sprite('el000_15', 6)	# 3971-3976
    gotoLabel(225)
    label(991)
    sprite('el000_00', 1)	# 3977-3977
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('el000_00', 6)	# 3978-3983
    sprite('el000_01', 6)	# 3984-3989
    sprite('el000_02', 6)	# 3990-3995
    sprite('el000_03', 6)	# 3996-4001
    sprite('el000_04', 6)	# 4002-4007
    sprite('el000_05', 6)	# 4008-4013
    sprite('el000_06', 6)	# 4014-4019
    sprite('el000_07', 6)	# 4020-4025
    sprite('el000_08', 6)	# 4026-4031
    sprite('el000_09', 6)	# 4032-4037
    sprite('el000_10', 6)	# 4038-4043
    sprite('el000_11', 6)	# 4044-4049
    sprite('el000_12', 6)	# 4050-4055
    sprite('el000_13', 6)	# 4056-4061
    sprite('el000_14', 6)	# 4062-4067
    sprite('el000_15', 6)	# 4068-4073
    gotoLabel(992)
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

    def upon_CLEAR_OR_EXIT():
        SLOT_58 = 1
        Unknown48('19000000020000003400000018000000020000003a000000')
        if SLOT_52:
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bph'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('uhi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('bce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('el610_00', 35)	# 4-38
    Unknown2034(0)
    GFX_0('elef610_door', 100)
    GFX_0('elef610_door_add', 100)
    sprite('el610_01', 6)	# 39-44
    sprite('el610_02', 25)	# 45-69
    sprite('el610_03', 6)	# 70-75
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pel704def', 100, 929850736, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pel402_0', 100, 879519088, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pel700def', 100, 929850736, 1701065008, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('el610_04', 6)	# 76-81
    sprite('el610_05', 75)	# 82-156
    sprite('el610_06', 5)	# 157-161
    sprite('el610_07', 5)	# 162-166
    sprite('el610_08', 5)	# 167-171
    sprite('el610_09', 10)	# 172-181
    physicsXImpulse(-2800)
    sprite('el610_10', 8)	# 182-189
    SFX_3('walk_stone_light')
    sprite('el610_11', 10)	# 190-199
    sprite('el610_12', 8)	# 200-207
    sprite('el610_09', 8)	# 208-215
    SFX_3('walk_stone_light')
    sprite('el610_09', 2)	# 216-217
    Unknown3032()
    Unknown3004(-19)
    sprite('el610_10', 8)	# 218-225
    sprite('el610_11', 10)	# 226-235
    sprite('el610_12', 8)	# 236-243
    physicsXImpulse(0)
    Unknown2035(1)
    sprite('el610_09', 10)	# 244-253
    Unknown23018(1)
    sprite('null', 32767)	# 254-33020
    ExitState()
    label(10)
    sprite('el611_00', 4)	# 33021-33024
    sprite('el611_01', 4)	# 33025-33028
    GFX_0('elef611_WinCard', 0)
    GFX_0('elef611_Book', 0)
    SFX_3('hair')
    sprite('el611_02', 4)	# 33029-33032
    SFX_3('hair')
    sprite('el611_03', 4)	# 33033-33036
    SFX_3('hair')
    sprite('el611_01', 4)	# 33037-33040
    sprite('el611_02', 4)	# 33041-33044
    sprite('el611_03', 4)	# 33045-33048
    sprite('el611_01', 4)	# 33049-33052
    sprite('el611_02', 4)	# 33053-33056
    sprite('el611_03', 4)	# 33057-33060
    sprite('el611_01', 4)	# 33061-33064
    GFX_0('elef611_DelBook', 0)
    SFX_3('distortion_a')
    sprite('el611_02', 4)	# 33065-33068
    sprite('el611_03', 4)	# 33069-33072
    sprite('el611_01', 4)	# 33073-33076
    sprite('el611_02', 4)	# 33077-33080
    sprite('el611_03', 4)	# 33081-33084
    sprite('el611_04', 4)	# 33085-33088
    sprite('el611_05', 4)	# 33089-33092
    sprite('el611_06', 4)	# 33093-33096
    sprite('el611_07', 4)	# 33097-33100
    Unknown23029(11, 9002, 0)
    sprite('el611_08', 4)	# 33101-33104
    sprite('el611_09', 4)	# 33105-33108
    sprite('el611_10', 4)	# 33109-33112
    sprite('el611_11', 4)	# 33113-33116
    sprite('el611_12', 4)	# 33117-33120
    sprite('el611_13', 4)	# 33121-33124
    sprite('el611_14', 4)	# 33125-33128
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pel704def', 100, 929850736, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pel402_0', 100, 879519088, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pel700def', 100, 929850736, 1701065008, 102, 0, 100, 929850736, 1701065264, 102, 0, 100, 929850736, 1701065520, 102, 0, 100)
    Unknown23018(1)
    setGravity(0)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    label(11)
    sprite('el611_15', 4)	# 33129-33132
    physicsYImpulse(500)
    sprite('el611_16', 4)	# 33133-33136
    sprite('el611_17', 4)	# 33137-33140
    sprite('el611_15', 4)	# 33141-33144
    sprite('el611_16', 4)	# 33145-33148
    sprite('el611_17', 4)	# 33149-33152
    sprite('el611_15', 4)	# 33153-33156
    sprite('el611_16', 4)	# 33157-33160
    sprite('el611_17', 4)	# 33161-33164
    sprite('el611_15', 4)	# 33165-33168
    sprite('el611_16', 4)	# 33169-33172
    sprite('el611_17', 4)	# 33173-33176
    sprite('el611_15', 4)	# 33177-33180
    sprite('el611_16', 4)	# 33181-33184
    sprite('el611_17', 4)	# 33185-33188
    sprite('el611_15', 4)	# 33189-33192
    sprite('el611_16', 4)	# 33193-33196
    sprite('el611_17', 4)	# 33197-33200
    sprite('el611_15', 4)	# 33201-33204
    physicsYImpulse(-500)
    sprite('el611_16', 4)	# 33205-33208
    sprite('el611_17', 4)	# 33209-33212
    sprite('el611_15', 4)	# 33213-33216
    sprite('el611_16', 4)	# 33217-33220
    sprite('el611_17', 4)	# 33221-33224
    sprite('el611_15', 4)	# 33225-33228
    sprite('el611_16', 4)	# 33229-33232
    sprite('el611_17', 4)	# 33233-33236
    sprite('el611_15', 4)	# 33237-33240
    sprite('el611_16', 4)	# 33241-33244
    sprite('el611_17', 4)	# 33245-33248
    sprite('el611_15', 4)	# 33249-33252
    sprite('el611_16', 4)	# 33253-33256
    sprite('el611_17', 4)	# 33257-33260
    sprite('el611_15', 4)	# 33261-33264
    sprite('el611_16', 4)	# 33265-33268
    sprite('el611_17', 4)	# 33269-33272
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('el000_00', 6)	# 33273-33278

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('el000_01', 6)	# 33279-33284
    sprite('el000_02', 6)	# 33285-33290
    sprite('el000_03', 6)	# 33291-33296
    sprite('el000_04', 6)	# 33297-33302
    sprite('el000_05', 6)	# 33303-33308
    sprite('el000_06', 6)	# 33309-33314
    sprite('el000_07', 6)	# 33315-33320
    sprite('el000_08', 6)	# 33321-33326
    sprite('el000_09', 6)	# 33327-33332
    sprite('el000_10', 6)	# 33333-33338
    sprite('el000_11', 6)	# 33339-33344
    sprite('el000_12', 6)	# 33345-33350
    sprite('el000_13', 6)	# 33351-33356
    sprite('el000_14', 6)	# 33357-33362
    sprite('el000_15', 6)	# 33363-33368
    sprite('el000_00', 6)	# 33369-33374
    gotoLabel(101)
    label(102)
    sprite('el611_00', 4)	# 33375-33378
    sprite('el611_01', 4)	# 33379-33382
    GFX_0('elef611_WinCard', 0)
    GFX_0('elef611_Book', 0)
    SFX_3('hair')
    sprite('el611_02', 4)	# 33383-33386
    SFX_3('hair')
    sprite('el611_03', 4)	# 33387-33390
    SFX_3('hair')
    sprite('el611_01', 4)	# 33391-33394
    sprite('el611_02', 4)	# 33395-33398
    sprite('el611_03', 4)	# 33399-33402
    sprite('el611_01', 4)	# 33403-33406
    sprite('el611_02', 4)	# 33407-33410
    sprite('el611_03', 4)	# 33411-33414
    sprite('el611_01', 4)	# 33415-33418
    GFX_0('elef611_DelBook', 0)
    SFX_3('distortion_a')
    sprite('el611_02', 4)	# 33419-33422
    sprite('el611_03', 4)	# 33423-33426
    sprite('el611_01', 4)	# 33427-33430
    sprite('el611_02', 4)	# 33431-33434
    sprite('el611_03', 4)	# 33435-33438
    sprite('el611_04', 4)	# 33439-33442
    SFX_1('pel701brc')
    sprite('el611_05', 4)	# 33443-33446
    sprite('el611_06', 4)	# 33447-33450
    sprite('el611_07', 4)	# 33451-33454
    Unknown23029(11, 9002, 0)
    sprite('el611_08', 4)	# 33455-33458
    sprite('el611_09', 4)	# 33459-33462
    sprite('el611_10', 4)	# 33463-33466
    sprite('el611_11', 4)	# 33467-33470
    sprite('el611_12', 4)	# 33471-33474
    sprite('el611_13', 4)	# 33475-33478
    sprite('el611_14', 4)	# 33479-33482
    setGravity(0)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    Unknown23018(1)
    label(103)
    sprite('el611_15', 4)	# 33483-33486
    physicsYImpulse(500)
    sprite('el611_16', 4)	# 33487-33490
    sprite('el611_17', 4)	# 33491-33494
    sprite('el611_15', 4)	# 33495-33498
    sprite('el611_16', 4)	# 33499-33502
    sprite('el611_17', 4)	# 33503-33506
    sprite('el611_15', 4)	# 33507-33510
    sprite('el611_16', 4)	# 33511-33514
    sprite('el611_17', 4)	# 33515-33518
    sprite('el611_15', 4)	# 33519-33522
    sprite('el611_16', 4)	# 33523-33526
    sprite('el611_17', 4)	# 33527-33530
    sprite('el611_15', 4)	# 33531-33534
    sprite('el611_16', 4)	# 33535-33538
    sprite('el611_17', 4)	# 33539-33542
    sprite('el611_15', 4)	# 33543-33546
    sprite('el611_16', 4)	# 33547-33550
    sprite('el611_17', 4)	# 33551-33554
    sprite('el611_15', 4)	# 33555-33558
    physicsYImpulse(-500)
    sprite('el611_16', 4)	# 33559-33562
    sprite('el611_17', 4)	# 33563-33566
    sprite('el611_15', 4)	# 33567-33570
    sprite('el611_16', 4)	# 33571-33574
    sprite('el611_17', 4)	# 33575-33578
    sprite('el611_15', 4)	# 33579-33582
    sprite('el611_16', 4)	# 33583-33586
    sprite('el611_17', 4)	# 33587-33590
    sprite('el611_15', 4)	# 33591-33594
    sprite('el611_16', 4)	# 33595-33598
    sprite('el611_17', 4)	# 33599-33602
    sprite('el611_15', 4)	# 33603-33606
    sprite('el611_16', 4)	# 33607-33610
    sprite('el611_17', 4)	# 33611-33614
    sprite('el611_15', 4)	# 33615-33618
    sprite('el611_16', 4)	# 33619-33622
    sprite('el611_17', 4)	# 33623-33626
    loopRest()
    gotoLabel(103)
    label(110)
    sprite('el000_00', 6)	# 33627-33632

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('el000_01', 6)	# 33633-33638
    sprite('el000_02', 6)	# 33639-33644
    sprite('el000_03', 6)	# 33645-33650
    sprite('el000_04', 6)	# 33651-33656
    sprite('el000_05', 6)	# 33657-33662
    sprite('el000_06', 6)	# 33663-33668
    sprite('el000_07', 6)	# 33669-33674
    sprite('el000_08', 6)	# 33675-33680
    sprite('el000_09', 6)	# 33681-33686
    sprite('el000_10', 6)	# 33687-33692
    sprite('el000_11', 6)	# 33693-33698
    sprite('el000_12', 6)	# 33699-33704
    sprite('el000_13', 6)	# 33705-33710
    sprite('el000_14', 6)	# 33711-33716
    sprite('el000_15', 6)	# 33717-33722
    sprite('el000_00', 6)	# 33723-33728
    gotoLabel(111)
    label(112)
    sprite('el610_00', 35)	# 33729-33763
    Unknown2034(0)
    SFX_1('pel701bny')
    sprite('el610_01', 6)	# 33764-33769
    sprite('el610_02', 25)	# 33770-33794
    sprite('el610_03', 6)	# 33795-33800
    sprite('el610_04', 6)	# 33801-33806
    sprite('el610_05', 32767)	# 33807-66573
    Unknown23018(1)
    label(120)
    sprite('keep', 1)	# 66574-66574
    Unknown2053(0)
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(128)
        elif (SLOT_38 == 1):
            sendToLabel(128)

    def upon_40():
        clearUponHandler(40)
        SFX_1('pel701baz')
        sendToLabel(125)
    label(121)
    sprite('keep', 1)	# 66575-66575
    if (not (SLOT_145 <= 160000)):
        sendToLabel(124)
    if (SLOT_26 <= 160000):
        sendToLabel(124)
    sprite('el033_00', 2)	# 66576-66577
    sendToLabelUpon(2, 123)
    sprite('el033_01', 3)	# 66578-66580
    physicsXImpulse(-20000)
    physicsYImpulse(9000)
    setGravity(1550)
    Unknown8002()
    sprite('el033_02', 3)	# 66581-66583
    label(122)
    sprite('el033_01', 3)	# 66584-66586
    sprite('el033_02', 3)	# 66587-66589
    loopRest()
    gotoLabel(122)
    label(123)
    sprite('el033_03', 3)	# 66590-66592
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('el033_04', 3)	# 66593-66595
    label(124)
    sprite('el600_00', 4)	# 66596-66599
    sprite('el600_01', 4)	# 66600-66603
    sprite('el600_02', 4)	# 66604-66607
    gotoLabel(124)
    label(125)
    sprite('el600_00', 4)	# 66608-66611
    sprite('el600_01', 4)	# 66612-66615
    sprite('el600_02', 4)	# 66616-66619
    if SLOT_97:
        _gotolabel(125)
    sprite('el600_03', 4)	# 66620-66623
    sprite('el600_04', 4)	# 66624-66627
    GFX_0('elef600_card', 0)
    sprite('el600_05', 4)	# 66628-66631
    sprite('el600_06', 4)	# 66632-66635
    sprite('el600_07', 4)	# 66636-66639
    sprite('el600_08', 4)	# 66640-66643
    Unknown2037(3)
    label(126)
    sprite('el600_09', 4)	# 66644-66647
    SLOT_2 = (SLOT_2 + (-1))
    sprite('el600_10', 4)	# 66648-66651
    sprite('el600_11', 4)	# 66652-66655
    if SLOT_2:
        _gotolabel(126)
    sprite('el600_09', 4)	# 66656-66659
    Unknown23029(11, 9003, 0)
    sprite('el600_10', 4)	# 66660-66663
    sprite('el600_11', 4)	# 66664-66667
    Unknown21011(30)
    label(127)
    sprite('el600_09', 4)	# 66668-66671
    sprite('el600_10', 4)	# 66672-66675
    sprite('el600_11', 4)	# 66676-66679
    gotoLabel(127)
    label(128)
    sprite('el003_00', 4)	# 66680-66683
    Unknown2005()
    sprite('el003_01', 4)	# 66684-66687
    sprite('el003_02', 4)	# 66688-66691
    gotoLabel(121)
    label(130)
    sprite('el000_00', 6)	# 66692-66697

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('el000_01', 6)	# 66698-66703
    sprite('el000_02', 6)	# 66704-66709
    sprite('el000_03', 6)	# 66710-66715
    sprite('el000_04', 6)	# 66716-66721
    sprite('el000_05', 6)	# 66722-66727
    sprite('el000_06', 6)	# 66728-66733
    sprite('el000_07', 6)	# 66734-66739
    sprite('el000_08', 6)	# 66740-66745
    sprite('el000_09', 6)	# 66746-66751
    sprite('el000_10', 6)	# 66752-66757
    sprite('el000_11', 6)	# 66758-66763
    sprite('el000_12', 6)	# 66764-66769
    sprite('el000_13', 6)	# 66770-66775
    sprite('el000_14', 6)	# 66776-66781
    sprite('el000_15', 6)	# 66782-66787
    sprite('el000_00', 6)	# 66788-66793
    gotoLabel(131)
    label(132)
    sprite('el610_00', 35)	# 66794-66828
    Unknown2034(0)
    SFX_1('pel701bph')
    sprite('el610_01', 6)	# 66829-66834
    sprite('el610_02', 25)	# 66835-66859
    sprite('el610_03', 6)	# 66860-66865
    sprite('el610_04', 6)	# 66866-66871
    sprite('el610_05', 32767)	# 66872-99638
    Unknown23018(1)
    label(140)
    sprite('keep', 1)	# 99639-99639
    Unknown2053(0)
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(143)
        elif (SLOT_38 == 1):
            sendToLabel(143)
    label(141)
    sprite('el610_00', 35)	# 99640-99674
    SFX_1('pel700pbc')
    sprite('el610_01', 6)	# 99675-99680
    sprite('el610_02', 25)	# 99681-99705
    sprite('el610_03', 6)	# 99706-99711
    sprite('el610_04', 6)	# 99712-99717
    label(142)
    sprite('el610_05', 1)	# 99718-99718
    if SLOT_97:
        _gotolabel(142)
    sprite('el610_05', 60)	# 99719-99778
    sprite('el610_05', 32767)	# 99779-132545
    Unknown21007(24, 40)
    Unknown21011(210)
    label(143)
    sprite('el003_00', 4)	# 132546-132549
    Unknown2005()
    sprite('el003_01', 4)	# 132550-132553
    sprite('el003_02', 4)	# 132554-132557
    gotoLabel(141)
    label(150)
    sprite('el000_00', 6)	# 132558-132563

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('el000_01', 6)	# 132564-132569
    sprite('el000_02', 6)	# 132570-132575
    sprite('el000_03', 6)	# 132576-132581
    sprite('el000_04', 6)	# 132582-132587
    sprite('el000_05', 6)	# 132588-132593
    sprite('el000_06', 6)	# 132594-132599
    sprite('el000_07', 6)	# 132600-132605
    sprite('el000_08', 6)	# 132606-132611
    sprite('el000_09', 6)	# 132612-132617
    sprite('el000_10', 6)	# 132618-132623
    sprite('el000_11', 6)	# 132624-132629
    sprite('el000_12', 6)	# 132630-132635
    sprite('el000_13', 6)	# 132636-132641
    sprite('el000_14', 6)	# 132642-132647
    sprite('el000_15', 6)	# 132648-132653
    sprite('el000_00', 6)	# 132654-132659
    gotoLabel(151)
    label(152)
    sprite('el610_00', 35)	# 132660-132694
    Unknown2034(0)
    SFX_1('pel701pmi')
    sprite('el610_01', 6)	# 132695-132700
    sprite('el610_02', 25)	# 132701-132725
    sprite('el610_03', 6)	# 132726-132731
    sprite('el610_04', 6)	# 132732-132737
    sprite('el610_05', 32767)	# 132738-165504
    Unknown23018(1)
    label(160)
    sprite('el000_00', 6)	# 165505-165510

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('el000_01', 6)	# 165511-165516
    sprite('el000_02', 6)	# 165517-165522
    sprite('el000_03', 6)	# 165523-165528
    sprite('el000_04', 6)	# 165529-165534
    sprite('el000_05', 6)	# 165535-165540
    sprite('el000_06', 6)	# 165541-165546
    sprite('el000_07', 6)	# 165547-165552
    sprite('el000_08', 6)	# 165553-165558
    sprite('el000_09', 6)	# 165559-165564
    sprite('el000_10', 6)	# 165565-165570
    sprite('el000_11', 6)	# 165571-165576
    sprite('el000_12', 6)	# 165577-165582
    sprite('el000_13', 6)	# 165583-165588
    sprite('el000_14', 6)	# 165589-165594
    sprite('el000_15', 6)	# 165595-165600
    sprite('el000_00', 6)	# 165601-165606
    gotoLabel(161)
    label(162)
    sprite('el611_00', 4)	# 165607-165610
    sprite('el611_01', 4)	# 165611-165614
    GFX_0('elef611_WinCard', 0)
    GFX_0('elef611_Book', 0)
    SFX_3('hair')
    sprite('el611_02', 4)	# 165615-165618
    SFX_3('hair')
    sprite('el611_03', 4)	# 165619-165622
    SFX_3('hair')
    sprite('el611_01', 4)	# 165623-165626
    sprite('el611_02', 4)	# 165627-165630
    sprite('el611_03', 4)	# 165631-165634
    sprite('el611_01', 4)	# 165635-165638
    sprite('el611_02', 4)	# 165639-165642
    sprite('el611_03', 4)	# 165643-165646
    sprite('el611_01', 4)	# 165647-165650
    GFX_0('elef611_DelBook', 0)
    SFX_3('distortion_a')
    sprite('el611_02', 4)	# 165651-165654
    sprite('el611_03', 4)	# 165655-165658
    sprite('el611_01', 4)	# 165659-165662
    sprite('el611_02', 4)	# 165663-165666
    sprite('el611_03', 4)	# 165667-165670
    sprite('el611_04', 4)	# 165671-165674
    SFX_1('pel701pag')
    sprite('el611_05', 4)	# 165675-165678
    sprite('el611_06', 4)	# 165679-165682
    sprite('el611_07', 4)	# 165683-165686
    Unknown23029(11, 9002, 0)
    sprite('el611_08', 4)	# 165687-165690
    sprite('el611_09', 4)	# 165691-165694
    sprite('el611_10', 4)	# 165695-165698
    sprite('el611_11', 4)	# 165699-165702
    sprite('el611_12', 4)	# 165703-165706
    sprite('el611_13', 4)	# 165707-165710
    sprite('el611_14', 4)	# 165711-165714
    setGravity(0)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    Unknown23018(1)
    label(163)
    sprite('el611_15', 4)	# 165715-165718
    physicsYImpulse(500)
    sprite('el611_16', 4)	# 165719-165722
    sprite('el611_17', 4)	# 165723-165726
    sprite('el611_15', 4)	# 165727-165730
    sprite('el611_16', 4)	# 165731-165734
    sprite('el611_17', 4)	# 165735-165738
    sprite('el611_15', 4)	# 165739-165742
    sprite('el611_16', 4)	# 165743-165746
    sprite('el611_17', 4)	# 165747-165750
    sprite('el611_15', 4)	# 165751-165754
    sprite('el611_16', 4)	# 165755-165758
    sprite('el611_17', 4)	# 165759-165762
    sprite('el611_15', 4)	# 165763-165766
    sprite('el611_16', 4)	# 165767-165770
    sprite('el611_17', 4)	# 165771-165774
    sprite('el611_15', 4)	# 165775-165778
    sprite('el611_16', 4)	# 165779-165782
    sprite('el611_17', 4)	# 165783-165786
    sprite('el611_15', 4)	# 165787-165790
    physicsYImpulse(-500)
    sprite('el611_16', 4)	# 165791-165794
    sprite('el611_17', 4)	# 165795-165798
    sprite('el611_15', 4)	# 165799-165802
    sprite('el611_16', 4)	# 165803-165806
    sprite('el611_17', 4)	# 165807-165810
    sprite('el611_15', 4)	# 165811-165814
    sprite('el611_16', 4)	# 165815-165818
    sprite('el611_17', 4)	# 165819-165822
    sprite('el611_15', 4)	# 165823-165826
    sprite('el611_16', 4)	# 165827-165830
    sprite('el611_17', 4)	# 165831-165834
    sprite('el611_15', 4)	# 165835-165838
    sprite('el611_16', 4)	# 165839-165842
    sprite('el611_17', 4)	# 165843-165846
    sprite('el611_15', 4)	# 165847-165850
    sprite('el611_16', 4)	# 165851-165854
    sprite('el611_17', 4)	# 165855-165858
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('el000_00', 6)	# 165859-165864

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('el000_01', 6)	# 165865-165870
    sprite('el000_02', 6)	# 165871-165876
    sprite('el000_03', 6)	# 165877-165882
    sprite('el000_04', 6)	# 165883-165888
    sprite('el000_05', 6)	# 165889-165894
    sprite('el000_06', 6)	# 165895-165900
    sprite('el000_07', 6)	# 165901-165906
    sprite('el000_08', 6)	# 165907-165912
    sprite('el000_09', 6)	# 165913-165918
    sprite('el000_10', 6)	# 165919-165924
    sprite('el000_11', 6)	# 165925-165930
    sprite('el000_12', 6)	# 165931-165936
    sprite('el000_13', 6)	# 165937-165942
    sprite('el000_14', 6)	# 165943-165948
    sprite('el000_15', 6)	# 165949-165954
    sprite('el000_00', 6)	# 165955-165960
    gotoLabel(171)
    label(172)
    sprite('el610_00', 35)	# 165961-165995
    Unknown2034(0)
    SFX_1('pel701uli')
    sprite('el610_01', 6)	# 165996-166001
    sprite('el610_02', 25)	# 166002-166026
    sprite('el610_03', 6)	# 166027-166032
    sprite('el610_04', 6)	# 166033-166038
    sprite('el610_05', 32767)	# 166039-198805
    Unknown23018(1)
    label(180)
    sprite('el000_00', 6)	# 198806-198811

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('el000_01', 6)	# 198812-198817
    sprite('el000_02', 6)	# 198818-198823
    sprite('el000_03', 6)	# 198824-198829
    sprite('el000_04', 6)	# 198830-198835
    sprite('el000_05', 6)	# 198836-198841
    sprite('el000_06', 6)	# 198842-198847
    sprite('el000_07', 6)	# 198848-198853
    sprite('el000_08', 6)	# 198854-198859
    sprite('el000_09', 6)	# 198860-198865
    sprite('el000_10', 6)	# 198866-198871
    sprite('el000_11', 6)	# 198872-198877
    sprite('el000_12', 6)	# 198878-198883
    sprite('el000_13', 6)	# 198884-198889
    sprite('el000_14', 6)	# 198890-198895
    sprite('el000_15', 6)	# 198896-198901
    sprite('el000_00', 6)	# 198902-198907
    gotoLabel(181)
    label(182)
    sprite('el610_00', 35)	# 198908-198942
    Unknown2034(0)
    SFX_1('pel701uor')
    sprite('el610_01', 6)	# 198943-198948
    sprite('el610_02', 25)	# 198949-198973
    sprite('el610_03', 6)	# 198974-198979
    sprite('el610_04', 6)	# 198980-198985
    sprite('el610_05', 32767)	# 198986-231752
    Unknown23018(1)
    label(190)
    sprite('el000_00', 6)	# 231753-231758

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('el000_01', 6)	# 231759-231764
    sprite('el000_02', 6)	# 231765-231770
    sprite('el000_03', 6)	# 231771-231776
    sprite('el000_04', 6)	# 231777-231782
    sprite('el000_05', 6)	# 231783-231788
    sprite('el000_06', 6)	# 231789-231794
    sprite('el000_07', 6)	# 231795-231800
    sprite('el000_08', 6)	# 231801-231806
    sprite('el000_09', 6)	# 231807-231812
    sprite('el000_10', 6)	# 231813-231818
    sprite('el000_11', 6)	# 231819-231824
    sprite('el000_12', 6)	# 231825-231830
    sprite('el000_13', 6)	# 231831-231836
    sprite('el000_14', 6)	# 231837-231842
    sprite('el000_15', 6)	# 231843-231848
    sprite('el000_00', 6)	# 231849-231854
    gotoLabel(191)
    label(192)
    sprite('el611_00', 4)	# 231855-231858
    sprite('el611_01', 4)	# 231859-231862
    GFX_0('elef611_WinCard', 0)
    GFX_0('elef611_Book', 0)
    SFX_3('hair')
    sprite('el611_02', 4)	# 231863-231866
    SFX_3('hair')
    sprite('el611_03', 4)	# 231867-231870
    SFX_3('hair')
    sprite('el611_01', 4)	# 231871-231874
    sprite('el611_02', 4)	# 231875-231878
    sprite('el611_03', 4)	# 231879-231882
    sprite('el611_01', 4)	# 231883-231886
    sprite('el611_02', 4)	# 231887-231890
    sprite('el611_03', 4)	# 231891-231894
    sprite('el611_01', 4)	# 231895-231898
    GFX_0('elef611_DelBook', 0)
    SFX_3('distortion_a')
    sprite('el611_02', 4)	# 231899-231902
    sprite('el611_03', 4)	# 231903-231906
    sprite('el611_01', 4)	# 231907-231910
    sprite('el611_02', 4)	# 231911-231914
    sprite('el611_03', 4)	# 231915-231918
    sprite('el611_04', 4)	# 231919-231922
    SFX_1('pel701uva')
    sprite('el611_05', 4)	# 231923-231926
    sprite('el611_06', 4)	# 231927-231930
    sprite('el611_07', 4)	# 231931-231934
    Unknown23029(11, 9002, 0)
    sprite('el611_08', 4)	# 231935-231938
    sprite('el611_09', 4)	# 231939-231942
    sprite('el611_10', 4)	# 231943-231946
    sprite('el611_11', 4)	# 231947-231950
    sprite('el611_12', 4)	# 231951-231954
    sprite('el611_13', 4)	# 231955-231958
    sprite('el611_14', 4)	# 231959-231962
    setGravity(0)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    Unknown23018(1)
    label(193)
    sprite('el611_15', 4)	# 231963-231966
    physicsYImpulse(500)
    sprite('el611_16', 4)	# 231967-231970
    sprite('el611_17', 4)	# 231971-231974
    sprite('el611_15', 4)	# 231975-231978
    sprite('el611_16', 4)	# 231979-231982
    sprite('el611_17', 4)	# 231983-231986
    sprite('el611_15', 4)	# 231987-231990
    sprite('el611_16', 4)	# 231991-231994
    sprite('el611_17', 4)	# 231995-231998
    sprite('el611_15', 4)	# 231999-232002
    sprite('el611_16', 4)	# 232003-232006
    sprite('el611_17', 4)	# 232007-232010
    sprite('el611_15', 4)	# 232011-232014
    sprite('el611_16', 4)	# 232015-232018
    sprite('el611_17', 4)	# 232019-232022
    sprite('el611_15', 4)	# 232023-232026
    sprite('el611_16', 4)	# 232027-232030
    sprite('el611_17', 4)	# 232031-232034
    sprite('el611_15', 4)	# 232035-232038
    physicsYImpulse(-500)
    sprite('el611_16', 4)	# 232039-232042
    sprite('el611_17', 4)	# 232043-232046
    sprite('el611_15', 4)	# 232047-232050
    sprite('el611_16', 4)	# 232051-232054
    sprite('el611_17', 4)	# 232055-232058
    sprite('el611_15', 4)	# 232059-232062
    sprite('el611_16', 4)	# 232063-232066
    sprite('el611_17', 4)	# 232067-232070
    sprite('el611_15', 4)	# 232071-232074
    sprite('el611_16', 4)	# 232075-232078
    sprite('el611_17', 4)	# 232079-232082
    sprite('el611_15', 4)	# 232083-232086
    sprite('el611_16', 4)	# 232087-232090
    sprite('el611_17', 4)	# 232091-232094
    sprite('el611_15', 4)	# 232095-232098
    sprite('el611_16', 4)	# 232099-232102
    sprite('el611_17', 4)	# 232103-232106
    loopRest()
    gotoLabel(193)
    label(200)
    sprite('el611_00', 4)	# 232107-232110
    sprite('el611_01', 4)	# 232111-232114
    GFX_0('elef611_WinCard', 0)
    GFX_0('elef611_Book', 0)
    SFX_3('hair')
    sprite('el611_02', 4)	# 232115-232118
    SFX_3('hair')
    sprite('el611_03', 4)	# 232119-232122
    SFX_3('hair')
    sprite('el611_01', 4)	# 232123-232126
    sprite('el611_02', 4)	# 232127-232130
    sprite('el611_03', 4)	# 232131-232134
    sprite('el611_01', 4)	# 232135-232138
    sprite('el611_02', 4)	# 232139-232142
    sprite('el611_03', 4)	# 232143-232146
    sprite('el611_01', 4)	# 232147-232150
    GFX_0('elef611_DelBook', 0)
    SFX_3('distortion_a')
    sprite('el611_02', 4)	# 232151-232154
    sprite('el611_03', 4)	# 232155-232158
    sprite('el611_01', 4)	# 232159-232162
    sprite('el611_02', 4)	# 232163-232166
    sprite('el611_03', 4)	# 232167-232170
    sprite('el611_04', 4)	# 232171-232174
    SFX_1('pel700rwi')
    sprite('el611_05', 4)	# 232175-232178
    sprite('el611_06', 4)	# 232179-232182
    sprite('el611_07', 4)	# 232183-232186
    Unknown23029(11, 9002, 0)
    sprite('el611_08', 4)	# 232187-232190
    sprite('el611_09', 4)	# 232191-232194
    sprite('el611_10', 4)	# 232195-232198
    sprite('el611_11', 4)	# 232199-232202
    sprite('el611_12', 4)	# 232203-232206
    sprite('el611_13', 4)	# 232207-232210
    sprite('el611_14', 4)	# 232211-232214
    setGravity(0)
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(210)

                def upon_CLEAR_OR_EXIT():
                    YAccel(98)
    label(201)
    sprite('el611_15', 4)	# 232215-232218
    physicsYImpulse(500)
    sprite('el611_16', 4)	# 232219-232222
    sprite('el611_17', 4)	# 232223-232226
    sprite('el611_15', 4)	# 232227-232230
    sprite('el611_16', 4)	# 232231-232234
    sprite('el611_17', 4)	# 232235-232238
    sprite('el611_15', 4)	# 232239-232242
    sprite('el611_16', 4)	# 232243-232246
    sprite('el611_17', 4)	# 232247-232250
    sprite('el611_15', 4)	# 232251-232254
    sprite('el611_16', 4)	# 232255-232258
    sprite('el611_17', 4)	# 232259-232262
    sprite('el611_15', 4)	# 232263-232266
    sprite('el611_16', 4)	# 232267-232270
    sprite('el611_17', 4)	# 232271-232274
    sprite('el611_15', 4)	# 232275-232278
    sprite('el611_16', 4)	# 232279-232282
    sprite('el611_17', 4)	# 232283-232286
    sprite('el611_15', 4)	# 232287-232290
    physicsYImpulse(-500)
    sprite('el611_16', 4)	# 232291-232294
    sprite('el611_17', 4)	# 232295-232298
    sprite('el611_15', 4)	# 232299-232302
    sprite('el611_16', 4)	# 232303-232306
    sprite('el611_17', 4)	# 232307-232310
    sprite('el611_15', 4)	# 232311-232314
    sprite('el611_16', 4)	# 232315-232318
    sprite('el611_17', 4)	# 232319-232322
    sprite('el611_15', 4)	# 232323-232326
    sprite('el611_16', 4)	# 232327-232330
    sprite('el611_17', 4)	# 232331-232334
    sprite('el611_15', 4)	# 232335-232338
    sprite('el611_16', 4)	# 232339-232342
    sprite('el611_17', 4)	# 232343-232346
    sprite('el611_15', 4)	# 232347-232350
    sprite('el611_16', 4)	# 232351-232354
    sprite('el611_17', 4)	# 232355-232358
    loopRest()
    gotoLabel(201)
    label(210)
    sprite('el000_00', 6)	# 232359-232364

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('el000_01', 6)	# 232365-232370
    sprite('el000_02', 6)	# 232371-232376
    sprite('el000_03', 6)	# 232377-232382
    sprite('el000_04', 6)	# 232383-232388
    sprite('el000_05', 6)	# 232389-232394
    sprite('el000_06', 6)	# 232395-232400
    sprite('el000_07', 6)	# 232401-232406
    sprite('el000_08', 6)	# 232407-232412
    sprite('el000_09', 6)	# 232413-232418
    sprite('el000_10', 6)	# 232419-232424
    sprite('el000_11', 6)	# 232425-232430
    sprite('el000_12', 6)	# 232431-232436
    sprite('el000_13', 6)	# 232437-232442
    sprite('el000_14', 6)	# 232443-232448
    sprite('el000_15', 6)	# 232449-232454
    sprite('el000_00', 6)	# 232455-232460
    gotoLabel(211)
    label(212)
    sprite('el610_00', 35)	# 232461-232495
    Unknown2034(0)
    SFX_1('pel701uhi')
    sprite('el610_01', 6)	# 232496-232501
    sprite('el610_02', 25)	# 232502-232526
    sprite('el610_03', 6)	# 232527-232532
    sprite('el610_04', 6)	# 232533-232538
    sprite('el610_05', 32767)	# 232539-265305
    Unknown23018(1)
    label(220)
    sprite('el433_00', 3)	# 265306-265308
    sprite('el433_01', 4)	# 265309-265312
    callSubroutine('PersonaCard_ON')
    sprite('el433_02', 4)	# 265313-265316
    sprite('el433_00', 4)	# 265317-265320
    sprite('el433_01', 4)	# 265321-265324
    sprite('el433_02', 4)	# 265325-265328
    sprite('el433_00', 4)	# 265329-265332
    sprite('el433_01', 4)	# 265333-265336
    sprite('el433_02', 4)	# 265337-265340
    sprite('el433_00', 4)	# 265341-265344
    sprite('el433_01', 4)	# 265345-265348
    sprite('el433_02', 4)	# 265349-265352
    sprite('el433_03', 4)	# 265353-265356
    Unknown23029(11, 9002, 0)
    callSubroutine('PersonaCard_STOP')
    callSubroutine('PersonaCard_OFF')
    sprite('el433_04', 4)	# 265357-265360
    sprite('el433_05', 4)	# 265361-265364
    sprite('el433_06', 4)	# 265365-265368
    sprite('el433_07', 4)	# 265369-265372
    sprite('el433_08', 4)	# 265373-265376
    sprite('el433_09', 4)	# 265377-265380
    SFX_1('pel700bce')
    sprite('el433_10', 4)	# 265381-265384
    sprite('el433_11', 4)	# 265385-265388
    label(221)
    sprite('el433_09', 4)	# 265389-265392
    sprite('el433_10', 4)	# 265393-265396
    sprite('el433_11', 4)	# 265397-265400
    if SLOT_97:
        _gotolabel(221)
    sprite('el433_09', 4)	# 265401-265404
    Unknown21007(24, 40)
    Unknown21011(150)
    label(222)
    sprite('el433_10', 4)	# 265405-265408
    sprite('el433_11', 4)	# 265409-265412
    sprite('el433_09', 4)	# 265413-265416
    gotoLabel(222)

@State
def CmnActLose():
    sprite('el070_00', 6)	# 1-6
    Unknown7006('pel403_0', 100, 879519088, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('el070_01', 6)	# 7-12
    sprite('el070_02', 2)	# 13-14
    sprite('el070_03', 32767)	# 15-32781
    Unknown23018(1)