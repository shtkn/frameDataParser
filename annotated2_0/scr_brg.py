@Subroutine
def PreInit():
    Unknown12019('62726700000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Unknown12045(100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
    Unknown12024(2)
    Unknown13039(0)
    Unknown2049(1)
    Unknown23003(0, 1, 4, 1, 600, 0, -65536, -65536)
    Unknown23004(0, 1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 450000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 300000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown15009()
    Unknown14015(200000, 400000, -80000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(200000, 400000, -80000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown15013(1)
    Unknown14015(100000, 400000, 50000, 400000, 3000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown15015(47, 50)
    Unknown15021(2000)
    Unknown15012(1)
    Unknown14015(-50000, 500000, -200000, 700000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x19)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('Oiuchi', 0x19)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14027('NmlAtk5B')
    Unknown15009()
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15021(1)
    Unknown15012(1500)
    Unknown14015(150000, 500000, -100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 450000, -300000, 300000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(0, 450000, -300000, 300000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(0, 300000, 0, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown14015(0, 350000, -500000, 80000, 500, 1)
    Move_EndRegister()
    Move_Register('ShortDash', 0x1)
    Move_Input_(0xda)
    Unknown14005(1)
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
    Unknown15011(10000)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(4000)
    Unknown14015(250000, 750000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15011(10000)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(4000)
    Unknown14015(250000, 750000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('ShotC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15011(10000)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(4000)
    Unknown14015(250000, 750000, -200000, 100000, 100, 0)
    Move_EndRegister()
    Move_Register('ShotC_2nd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15006(10000)
    Move_EndRegister()
    Move_Register('ShotC_3rd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15006(10000)
    Move_EndRegister()
    Move_Register('AntiAir2nd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15006(10000)
    Move_EndRegister()
    Move_Register('AntiAir3rdTate', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15006(10000)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15015(29, 30)
    Unknown15014(1)
    Unknown15013(500)
    Unknown14015(0, 700000, -200000, 250000, 150, 0)
    Move_EndRegister()
    Move_Register('Assault2nd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15013(10000)
    Unknown15012(1)
    Move_EndRegister()
    Move_Register('MidAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown15005(1)
    Unknown15015(45, 46)
    Unknown14015(300000, 600000, -100000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('Air_MidAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown15005(1)
    Unknown15015(30, 35)
    Unknown14015(300000, 600000, -100000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('MidAssault2nd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15006(10000)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown14015(0, 350000, -500000, 80000, 500, 1)
    Move_EndRegister()
    Move_Register('AirAssault2nd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15013(10000)
    Unknown14015(0, 350000, -200000, 200000, 1000, 1)
    Move_EndRegister()
    Move_Register('JumpAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(450000, 850000, -200000, 400000, 100, 1)
    Move_EndRegister()
    Move_Register('AirJumpAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(250000, 700000, -400000, 100000, 100, 1)
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
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 500000, -200000, 400000, 500, 50)
    Move_EndRegister()
    Move_Register('BloodWeaponFinish', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(3000)
    Unknown14015(50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('BloodWeaponFinish_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(3000)
    Unknown14015(50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('DebugSkill', 0x1)
    Move_Input_(0x26)
    Move_AirGround_(0x306f)
    Move_EndRegister()
    Move_Register('DS_Niku_Head', 0x1)
    Move_Input_(0x6b)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_NH')
    Move_EndRegister()
    Move_Register('DS_Niku_Body', 0x1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_NB')
    Move_EndRegister()
    Move_Register('DS_Niku_Leg', 0x1)
    Move_Input_(0x44)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_NL')
    Move_EndRegister()
    Move_Register('DS_Niku_Approach', 0x1)
    Move_Input_(0x78)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_NA')
    Move_EndRegister()
    Move_Register('DS_Niku_Throw', 0x1)
    Move_Input_(0x92)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_NT')
    Move_EndRegister()
    Move_Register('DS_Shot_Head', 0x1)
    Move_Input_(0x6b)
    Move_Input_(INPUT_RELEASE_B)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_SH')
    Move_EndRegister()
    Move_Register('DS_Shot_Body', 0x1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_RELEASE_B)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_SB')
    Move_EndRegister()
    Move_Register('DS_Shot_Leg', 0x1)
    Move_Input_(0x44)
    Move_Input_(INPUT_RELEASE_B)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_SL')
    Move_EndRegister()
    Move_Register('DS_Shot_Approach', 0x1)
    Move_Input_(0x78)
    Move_Input_(INPUT_RELEASE_B)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_SA')
    Move_EndRegister()
    Move_Register('DS_Shot_Throw', 0x1)
    Move_Input_(0x92)
    Move_Input_(INPUT_RELEASE_B)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_ST')
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BBB', 'Oiuchi', 10000000)
    Unknown15024('Oiuchi', 'Assault', 10000000)
    Unknown15024('OiuchiExe', 'Assault', 10000000)
    Unknown12018(0, 'rg062_01')
    Unknown12018(1, 'rg062_03')
    Unknown12018(2, 'rg062_04')
    Unknown12018(3, 'rg062_05')
    Unknown12018(4, 'rg062_05')
    Unknown12018(5, 'rg062_06')
    Unknown12018(6, 'rg062_07')
    Unknown12018(7, 'rg041_02')
    Unknown12018(8, 'rg040_02')
    Unknown12018(9, 'rg045_02')
    Unknown12018(10, 'rg060_00')
    Unknown12018(11, 'rg060_01')
    Unknown12018(12, 'rg060_03')
    Unknown12018(13, 'rg060_05')
    Unknown12018(14, 'rg060_07')
    Unknown12018(15, 'rg060_14')
    Unknown12018(16, 'rg050_00')
    Unknown12018(17, 'rg052_00')
    Unknown12018(18, 'rg054_00')
    Unknown12018(19, 'rg000_00')
    Unknown12018(20, 'rg000_00')
    Unknown12018(25, 'rg063_00')
    Unknown12018(26, 'rg063_01')
    Unknown12018(27, 'rg063_02')
    Unknown12018(28, 'rg063_04')
    Unknown12018(29, 'rg063_10')
    Unknown12018(24, 'rg073_01')
    Unknown7010(0, 'brg000')
    Unknown7010(1, 'brg001')
    Unknown7010(2, 'brg002')
    Unknown7010(3, 'brg003')
    Unknown7010(4, 'brg004')
    Unknown7010(5, 'brg005')
    Unknown7010(6, 'brg006')
    Unknown7010(7, 'brg007')
    Unknown7010(8, 'brg008')
    Unknown7010(9, 'brg009')
    Unknown7010(10, 'brg010')
    Unknown7010(15, 'brg011')
    Unknown7010(16, 'brg012')
    Unknown7010(17, 'brg013')
    Unknown7010(18, 'brg014')
    Unknown7010(19, 'brg015')
    Unknown7010(20, 'brg016')
    Unknown7010(21, 'brg017')
    Unknown7010(22, 'brg018')
    Unknown7010(23, 'brg019')
    Unknown7010(24, 'brg020')
    Unknown7010(25, 'brg021')
    Unknown7010(28, 'brg022')
    Unknown7010(29, 'brg023')
    Unknown7010(30, 'brg024')
    Unknown7010(31, 'brg025')
    Unknown7010(32, 'brg026')
    Unknown7010(33, 'brg027')
    Unknown7010(34, 'brg028')
    Unknown7010(35, 'brg029')
    Unknown7010(36, 'brg030')
    Unknown7010(37, 'brg031')
    Unknown7010(39, 'brg032')
    Unknown7010(42, 'brg033')
    Unknown7010(43, 'brg034')
    Unknown7010(44, 'brg035')
    Unknown7010(45, 'brg036')
    Unknown7010(46, 'brg037')
    Unknown7010(47, 'brg038')
    Unknown7010(48, 'brg039')
    Unknown7010(49, 'brg040')
    Unknown7010(50, 'brg041')
    Unknown7010(52, 'brg042')
    Unknown7010(53, 'brg043')
    Unknown7010(54, 'brg100_0')
    Unknown7010(55, 'brg100_1')
    Unknown7010(56, 'brg100_2')
    Unknown7010(63, 'brg101_0')
    Unknown7010(64, 'brg101_1')
    Unknown7010(65, 'brg101_2')
    Unknown7010(57, 'brg102_0')
    Unknown7010(58, 'brg102_1')
    Unknown7010(59, 'brg102_2')
    Unknown7010(66, 'brg103_0')
    Unknown7010(67, 'brg103_1')
    Unknown7010(68, 'brg103_2')
    Unknown7010(60, 'brg104_0')
    Unknown7010(61, 'brg104_1')
    Unknown7010(62, 'brg104_2')
    Unknown7010(69, 'brg105_0')
    Unknown7010(70, 'brg105_1')
    Unknown7010(71, 'brg105_2')
    Unknown7010(72, 'brg150')
    Unknown7010(73, 'brg151')
    Unknown7010(74, 'brg152')
    Unknown7010(85, 'brg153')
    Unknown7010(87, 'brg154')
    Unknown7010(88, 'brg155')
    Unknown7010(96, 'brg161_0')
    Unknown7010(97, 'brg161_1')
    Unknown7010(92, 'brg162_0')
    Unknown7010(93, 'brg162_1')
    Unknown7010(98, 'brg163_0')
    Unknown7010(99, 'brg163_1')
    Unknown7010(100, 'brg164_0')
    Unknown7010(101, 'brg164_1')
    Unknown7010(105, 'brg165_0')
    Unknown7010(106, 'brg165_1')
    Unknown7010(102, 'brg166_0')
    Unknown7010(103, 'brg166_1')
    Unknown7010(90, 'brg167_0')
    Unknown7010(91, 'brg167_1')
    Unknown7010(107, 'brg168_0')
    Unknown7010(108, 'brg168_1')
    Unknown7010(110, 'brg169_0')
    Unknown7010(111, 'brg169_1')
    Unknown7010(112, 'brg159_0')
    Unknown7010(113, 'brg159_1')
    Unknown7010(94, 'brg400_0')
    Unknown7010(95, 'brg400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('04000000426c6f6f64576561706f6e46696e697368000000000000000000000000000000')
    Unknown12059('05000000426c6f6f64576561706f6e46696e6973685f4f44000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if Unknown23145('CmnActOverDriveEnd'):
        SLOT_47 = 1

@Subroutine
def OnFrameStep():
    if SLOT_115:
        pass
    if (not SLOT_81):
        if SLOT_31:
            if SLOT_85:
                Unknown3029(1)
                Unknown3069(4)
                Unknown3071(6)
                Unknown3072('64000000500000005000000050000000')
                Unknown3073('32000000500000005000000050000000')
                Unknown3074('0000000064000000c8000000c8000000')
                Unknown3075('0000000000000000c8000000c8000000')
                Unknown3076(1020)
                Unknown3077(1050)
                Unknown3078(1)
            else:
                Unknown3029(1)
                Unknown3069(4)
                Unknown3071(6)
                Unknown3074('00000000ff000000ff000000ff000000')
                Unknown3075('0000000000000000ff000000ff000000')
                Unknown3076(1000)
                Unknown3077(1150)
            if SLOT_21:
                SLOT_31 = (SLOT_31 + (-1))
            if (SLOT_31 == 0):
                Unknown3029(0)
                Unknown3030(0)
            if SLOT_85:
                if (not SLOT_62):
                    SLOT_31 = 600
                if SLOT_21:
                    ConsumeSuperMeter(3)
                    SLOT_78 = 125
                    SLOT_82 = 125
            Unknown58('TRI_RagnasPowerUp', 2, 67)
            if SLOT_67:
                SLOT_31 = 600
        if Unknown23148('RlAstralDamage'):
            Unknown3029(0)
            Unknown3030(0)
        if SLOT_37:
            SLOT_66 = 2

@Subroutine
def OnActionBegin():
    pass

@Subroutine
def OnFinalize():
    pass

@Subroutine
def OnPreDraw():
    Unknown23030('52475f45796553776974636800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def VSta_Check():
    SLOT_47 = 0
    if Unknown42('ta'):
        SLOT_47 = 1

@Subroutine
def MatchInit2():
    SLOT_66 = 2

@Subroutine
def CheckAirAntiAirActive():
    (SLOT_66 >= 1)
    SLOT_47 = SLOT_0

@Subroutine
def Func_DS_NH():
    GFX_0('DS_Niku_Head', -1)

@Subroutine
def Func_DS_NB():
    GFX_0('DS_Niku_Body', -1)

@Subroutine
def Func_DS_NL():
    GFX_0('DS_Niku_Leg', -1)

@Subroutine
def Func_DS_NA():
    GFX_0('DS_Niku_Approach', -1)

@Subroutine
def Func_DS_NT():
    GFX_0('DS_Niku_Throw', -1)

@Subroutine
def Func_DS_SH():
    GFX_0('DS_Shot_Head', -1)

@Subroutine
def Func_DS_SB():
    GFX_0('DS_Shot_Body', -1)

@Subroutine
def Func_DS_SL():
    GFX_0('DS_Shot_Leg', -1)

@Subroutine
def Func_DS_SA():
    GFX_0('DS_Shot_Approach', -1)

@Subroutine
def Func_DS_ST():
    GFX_0('DS_Shot_Throw', -1)

@State
def CmnActStand():
    label(0)
    sprite('rg000_00', 7)	# 1-7
    sprite('rg000_01', 7)	# 8-14
    sprite('rg000_02', 7)	# 15-21
    sprite('rg000_03', 7)	# 22-28
    sprite('rg000_04', 7)	# 29-35
    sprite('rg000_05', 7)	# 36-42
    sprite('rg000_06', 7)	# 43-49
    sprite('rg000_05', 7)	# 50-56
    sprite('rg000_04', 7)	# 57-63
    sprite('rg000_03', 7)	# 64-70
    sprite('rg000_02', 7)	# 71-77
    sprite('rg000_01', 7)	# 78-84
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('rg001_00', 6)	# 85-90
    SLOT_88 = 960
    SFX_1('brg000')
    sprite('rg001_01', 6)	# 91-96
    sprite('rg001_02', 6)	# 97-102
    sprite('rg001_03', 6)	# 103-108
    sprite('rg001_04', 6)	# 109-114
    sprite('rg001_05', 6)	# 115-120
    sprite('rg001_06', 6)	# 121-126
    sprite('rg001_07', 6)	# 127-132
    sprite('rg001_08', 6)	# 133-138
    sprite('rg001_09', 6)	# 139-144
    sprite('rg001_10', 6)	# 145-150
    sprite('rg001_11', 6)	# 151-156
    sprite('rg001_12', 6)	# 157-162
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 163-168
    sprite('rg001_14', 6)	# 169-174
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 175-180
    sprite('rg001_16', 6)	# 181-186
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('rg003_00', 3)	# 1-3
    sprite('rg003_01', 3)	# 4-6
    sprite('rg003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('rg010_00', 4)	# 1-4
    SFX_3('rgse_00')
    sprite('rg010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('rg010_02', 6)	# 1-6
    sprite('rg010_03', 6)	# 7-12
    sprite('rg010_04', 6)	# 13-18
    sprite('rg010_05', 6)	# 19-24
    sprite('rg010_06', 6)	# 25-30
    sprite('rg010_07', 6)	# 31-36
    sprite('rg010_08', 6)	# 37-42
    sprite('rg010_07', 6)	# 43-48
    sprite('rg010_06', 6)	# 49-54
    sprite('rg010_05', 6)	# 55-60
    sprite('rg010_04', 6)	# 61-66
    sprite('rg010_03', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('rg013_00', 3)	# 1-3
    sprite('rg013_01', 3)	# 4-6
    sprite('rg013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('rg010_01', 4)	# 1-4
    sprite('rg010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('rg023_00', 2)	# 1-2
    SFX_3('rgse_00')
    sprite('rg023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('rg020_00', 4)	# 1-4
    sprite('rg020_01', 4)	# 5-8
    SFX_4('rg002')
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('rg020_02', 3)	# 1-3
    sprite('rg020_03', 3)	# 4-6
    sprite('rg020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('rg020_05', 3)	# 1-3
    sprite('rg020_06', 3)	# 4-6
    label(0)
    sprite('rg020_07', 4)	# 7-10
    sprite('rg020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('rg024_00', 3)	# 1-3
    sprite('rg024_01', 3)	# 4-6
    sprite('rg024_02', 3)	# 7-9
    sprite('rg024_03', 3)	# 10-12
    sprite('rg024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('rg024_00', 2)	# 1-2
    sprite('rg024_01', 2)	# 3-4
    sprite('rg024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('rg024_03', 3)	# 1-3
    sprite('rg024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('rg030_00', 2)	# 1-2
    sprite('rg030_00', 5)	# 3-7
    label(0)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_03', 7)	# 22-28
    sprite('rg030_04', 7)	# 29-35
    sprite('rg030_05', 7)	# 36-42
    sprite('rg030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_07', 7)	# 50-56
    SFX_3('rgse_00')
    sprite('rg030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('rg031_00', 7)	# 1-7
    label(0)
    sprite('rg031_01', 7)	# 8-14
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg031_02', 7)	# 15-21
    sprite('rg031_03', 7)	# 22-28
    sprite('rg031_04', 7)	# 29-35
    sprite('rg031_05', 7)	# 36-42
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg031_06', 7)	# 43-49
    sprite('rg031_07', 7)	# 50-56
    SFX_3('rgse_00')
    sprite('rg031_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('rg032_11', 3)	# 1-3
    sprite('rg032_00', 4)	# 4-7
    sprite('rg032_01', 4)	# 8-11
    label(0)
    sprite('rg032_02', 4)	# 12-15
    sprite('rg032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 20-23
    sprite('rg032_04', 4)	# 24-27
    sprite('rg032_05', 4)	# 28-31
    sprite('rg032_06', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('rg032_06add', 4)	# 36-39
    sprite('rg032_07', 4)	# 40-43
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('rg032_08', 3)	# 1-3
    sprite('rg032_09', 3)	# 4-6
    sprite('rg032_10', 3)	# 7-9
    sprite('rg032_11', 3)	# 10-12

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
    sprite('rg033_00', 1)	# 1-1
    sprite('rg033_01', 2)	# 2-3
    SFX_3('rgse_00')
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rg033_02', 2)	# 4-5
    sprite('rg033_02', 1)	# 6-6
    sprite('rg033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('rg033_02', 3)	# 10-12
    sprite('rg033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg033_04', 3)	# 16-18
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('rg033_05', 3)	# 19-21

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('rg035_00', 3)	# 1-3
    label(0)
    sprite('rg035_01', 3)	# 4-6
    sprite('rg035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('rg036_00', 3)	# 1-3
    label(0)
    sprite('rg036_01', 3)	# 4-6
    sprite('rg036_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('rg050_00', 1)	# 1-1
    sprite('rg050_01', 1)	# 2-2
    sprite('rg050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('rg050_01', 1)	# 1-1
    sprite('rg050_02', 1)	# 2-2
    sprite('rg050_01', 2)	# 3-4
    sprite('rg050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('rg050_02', 1)	# 1-1
    sprite('rg050_03', 1)	# 2-2
    sprite('rg050_02', 2)	# 3-4
    sprite('rg050_01', 2)	# 5-6
    sprite('rg050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('rg050_03', 1)	# 1-1
    sprite('rg050_04', 1)	# 2-2
    sprite('rg050_03', 2)	# 3-4
    sprite('rg050_02', 2)	# 5-6
    sprite('rg050_01', 2)	# 7-8
    sprite('rg050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('rg050_04', 1)	# 1-1
    sprite('rg050_04', 1)	# 2-2
    sprite('rg050_04', 2)	# 3-4
    sprite('rg050_03', 2)	# 5-6
    sprite('rg050_02', 2)	# 7-8
    sprite('rg050_01', 2)	# 9-10
    sprite('rg050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('rg052_00', 1)	# 1-1
    sprite('rg052_01', 1)	# 2-2
    sprite('rg052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('rg052_01', 1)	# 1-1
    sprite('rg052_02', 1)	# 2-2
    sprite('rg052_01', 2)	# 3-4
    sprite('rg052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('rg052_02', 1)	# 1-1
    sprite('rg052_03', 1)	# 2-2
    sprite('rg052_02', 2)	# 3-4
    sprite('rg052_01', 2)	# 5-6
    sprite('rg052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('rg052_03', 1)	# 1-1
    sprite('rg052_04', 1)	# 2-2
    sprite('rg052_03', 2)	# 3-4
    sprite('rg052_02', 2)	# 5-6
    sprite('rg052_01', 2)	# 7-8
    sprite('rg052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('rg052_04', 1)	# 1-1
    sprite('rg052_04', 1)	# 2-2
    sprite('rg052_04', 2)	# 3-4
    sprite('rg052_03', 2)	# 5-6
    sprite('rg052_02', 2)	# 7-8
    sprite('rg052_01', 2)	# 9-10
    sprite('rg052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('rg054_00', 1)	# 1-1
    sprite('rg054_01', 1)	# 2-2
    sprite('rg054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('rg054_01', 1)	# 1-1
    sprite('rg054_02', 1)	# 2-2
    sprite('rg054_01', 2)	# 3-4
    sprite('rg054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('rg054_02', 1)	# 1-1
    sprite('rg054_03', 1)	# 2-2
    sprite('rg054_02', 2)	# 3-4
    sprite('rg054_01', 2)	# 5-6
    sprite('rg054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('rg054_03', 1)	# 1-1
    sprite('rg054_04', 1)	# 2-2
    sprite('rg054_03', 2)	# 3-4
    sprite('rg054_02', 2)	# 5-6
    sprite('rg054_01', 2)	# 7-8
    sprite('rg054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('rg054_04', 1)	# 1-1
    sprite('rg054_04', 1)	# 2-2
    sprite('rg054_04', 2)	# 3-4
    sprite('rg054_03', 2)	# 5-6
    sprite('rg054_02', 2)	# 7-8
    sprite('rg054_01', 2)	# 9-10
    sprite('rg054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('rg060_00', 4)	# 1-4
    label(0)
    sprite('rg060_01', 4)	# 5-8
    sprite('rg060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('rg062_05', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('rg062_06', 4)	# 1-4
    label(0)
    sprite('rg062_07', 3)	# 5-7
    sprite('rg062_08', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('rg063_04', 3)	# 1-3
    sprite('rg063_05', 3)	# 4-6

@State
def CmnActBDownBound():
    sprite('rg063_06', 2)	# 1-2
    sprite('rg063_07', 2)	# 3-4
    sprite('rg063_08', 3)	# 5-7
    sprite('rg063_09', 3)	# 8-10
    sprite('rg063_10', 3)	# 11-13

@State
def CmnActBDownLoop():
    sprite('rg063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('rg064_00', 2)	# 1-2
    sprite('rg064_01', 2)	# 3-4
    sprite('rg064_02', 2)	# 5-6
    sprite('rg064_03', 2)	# 7-8
    sprite('rg064_04', 2)	# 9-10
    sprite('rg064_05', 2)	# 11-12
    SFX_3('rgse_00')
    sprite('rg064_06', 2)	# 13-14
    sprite('rg064_07', 2)	# 15-16
    sprite('rg064_08', 2)	# 17-18
    sprite('rg064_09', 2)	# 19-20
    sprite('rg064_10', 2)	# 21-22

@State
def CmnActFDownUpper():
    sprite('rg063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('rg063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('rg063_02', 3)	# 1-3
    sprite('rg063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('rg063_04', 3)	# 1-3
    sprite('rg063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('rg063_06', 2)	# 1-2
    sprite('rg063_07', 2)	# 3-4
    sprite('rg063_08', 3)	# 5-7
    sprite('rg063_09', 3)	# 8-10
    sprite('rg063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('rg063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('rg064_00', 2)	# 1-2
    sprite('rg064_01', 2)	# 3-4
    sprite('rg064_02', 2)	# 5-6
    sprite('rg064_03', 2)	# 7-8
    sprite('rg064_04', 2)	# 9-10
    sprite('rg064_05', 2)	# 11-12
    SFX_3('rgse_00')
    sprite('rg064_06', 2)	# 13-14
    sprite('rg064_07', 2)	# 15-16
    sprite('rg064_08', 2)	# 17-18
    sprite('rg064_09', 2)	# 19-20
    sprite('rg064_10', 2)	# 21-22

@State
def CmnActVDownUpper():
    sprite('rg062_00', 3)	# 1-3
    label(0)
    sprite('rg062_01', 3)	# 4-6
    sprite('rg062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('rg062_03', 3)	# 1-3
    sprite('rg062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('rg062_05', 3)	# 1-3
    sprite('rg062_06', 3)	# 4-6
    label(0)
    sprite('rg062_07', 3)	# 7-9
    sprite('rg062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('rg062_09', 2)	# 1-2
    sprite('rg062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('rg072_00', 3)	# 1-3
    sprite('rg072_01', 3)	# 4-6
    sprite('rg072_02', 3)	# 7-9
    label(0)
    sprite('rg072_01', 3)	# 10-12
    sprite('rg072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('rg074_00', 3)	# 1-3
    sprite('rg074_01', 3)	# 4-6
    sprite('rg074_02', 3)	# 7-9
    sprite('rg074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('rg082_00', 2)	# 1-2
    sprite('rg082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('rg071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('rg073_00', 3)	# 1-3
    sprite('rg073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('rg073_02', 3)	# 1-3
    label(0)
    sprite('rg073_03', 3)	# 4-6
    sprite('rg073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('rg070_00', 2)	# 1-2
    sprite('rg070_01', 2)	# 3-4
    sprite('rg070_02', 2)	# 5-6
    sprite('rg070_03', 2)	# 7-8
    sprite('rg070_04', 2)	# 9-10
    sprite('rg070_05', 2)	# 11-12
    sprite('rg070_06', 2)	# 13-14

@State
def CmnActStaggerDown():
    sprite('rg070_07', 7)	# 1-7
    sprite('rg070_08', 7)	# 8-14
    sprite('rg070_09', 5)	# 15-19
    sprite('rg070_10', 5)	# 20-24

@State
def CmnActUkemiStagger():
    sprite('rg070_11', 2)	# 1-2
    sprite('rg070_12', 3)	# 3-5
    sprite('rg070_13', 3)	# 6-8

@State
def CmnActUkemiAirF():
    sprite('rg113_00', 3)	# 1-3
    sprite('rg113_01', 3)	# 4-6
    SFX_3('rgse_00')
    sprite('rg113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('rg113_00', 3)	# 1-3
    sprite('rg113_01', 3)	# 4-6
    SFX_3('rgse_00')
    sprite('rg113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('rg113_00', 3)	# 1-3
    sprite('rg113_01', 3)	# 4-6
    SFX_3('rgse_00')
    sprite('rg113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('rg112_00', 2)	# 1-2
    EnableCollision(0)
    sprite('rg112_01', 2)	# 3-4
    sprite('rg112_02', 2)	# 5-6
    sprite('rg112_03', 2)	# 7-8
    sprite('rg112_04', 2)	# 9-10
    sprite('rg112_05', 2)	# 11-12
    SFX_3('rgse_00')
    sprite('rg112_06', 2)	# 13-14
    sprite('rg112_07', 2)	# 15-16
    sprite('rg112_08', 2)	# 17-18
    sprite('rg112_09', 2)	# 19-20

@State
def CmnActUkemiLandB():
    sprite('rg112_00', 2)	# 1-2
    sprite('rg112_01', 2)	# 3-4
    sprite('rg112_02', 2)	# 5-6
    sprite('rg112_03', 2)	# 7-8
    sprite('rg112_04', 2)	# 9-10
    sprite('rg112_05', 2)	# 11-12
    SFX_3('rgse_00')
    sprite('rg112_06', 2)	# 13-14
    sprite('rg112_07', 2)	# 15-16
    sprite('rg112_08', 2)	# 17-18
    sprite('rg112_09', 2)	# 19-20

@State
def CmnActUkemiLandN():
    sprite('rg112_00', 2)	# 1-2
    sprite('rg112_01', 2)	# 3-4
    sprite('rg112_02', 2)	# 5-6
    sprite('rg112_03', 2)	# 7-8
    sprite('rg112_04', 2)	# 9-10
    sprite('rg112_05', 2)	# 11-12
    SFX_3('rgse_00')
    sprite('rg112_06', 2)	# 13-14
    sprite('rg112_07', 2)	# 15-16
    sprite('rg112_08', 2)	# 17-18
    sprite('rg112_09', 2)	# 19-20

@State
def CmnActUkemiLandNLanding():
    sprite('rg024_00', 3)	# 1-3
    sprite('rg024_01', 3)	# 4-6
    sprite('rg024_02', 3)	# 7-9
    sprite('rg024_03', 3)	# 10-12
    sprite('rg024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('rg040_00', 3)	# 1-3
    sprite('rg040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('rg040_02', 5)	# 1-5
    sprite('rg040_02ex', 5)	# 6-10
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('rg040_01', 3)	# 1-3
    sprite('rg040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('rg040_03', 3)	# 1-3
    label(0)
    sprite('rg040_02', 5)	# 4-8
    sprite('rg040_02ex', 5)	# 9-13
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('rg040_01', 3)	# 1-3
    sprite('rg040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('rg041_00', 3)	# 1-3
    sprite('rg041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('rg041_02', 3)	# 1-3

@State
def CmnActHighGuardEnd():
    sprite('rg041_01', 3)	# 1-3
    sprite('rg041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('rg041_03', 3)	# 1-3
    sprite('rg041_02', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('rg041_01', 3)	# 1-3
    sprite('rg041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('rg043_00', 3)	# 1-3
    sprite('rg043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('rg043_02', 5)	# 1-5
    sprite('rg043_02ex', 5)	# 6-10
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('rg043_01', 3)	# 1-3
    sprite('rg043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('rg043_03', 3)	# 1-3
    label(0)
    sprite('rg043_02', 5)	# 4-8
    sprite('rg043_02ex', 5)	# 9-13
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('rg043_01', 3)	# 1-3
    sprite('rg043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('rg045_00', 3)	# 1-3
    sprite('rg045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('rg045_02', 5)	# 1-5
    sprite('rg045_02ex', 5)	# 6-10
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('rg045_01', 3)	# 1-3
    sprite('rg045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('rg045_03', 3)	# 1-3
    label(0)
    sprite('rg045_02', 5)	# 4-8
    sprite('rg045_02ex', 5)	# 9-13
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('rg045_01', 3)	# 1-3
    sprite('rg045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('rg090_00', 2)	# 1-2
    sprite('rg090_01', 2)	# 3-4
    sprite('rg090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('rg090_03', 6)	# 6-11
    sprite('rg090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('rg091_00', 2)	# 1-2
    sprite('rg091_01', 2)	# 3-4
    sprite('rg091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('rg091_03', 6)	# 6-11
    sprite('rg091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('rg092_00', 2)	# 1-2
    sprite('rg092_01', 2)	# 3-4
    sprite('rg092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('rg092_03', 6)	# 6-11
    sprite('rg092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('rg025_00', 4)	# 1-4
    sprite('rg025_01', 4)	# 5-8
    sprite('rg025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('rg040_02', 1)	# 1-1
    sprite('rg040_01', 3)	# 2-4
    sprite('rg040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('rg312_00', 2)	# 1-2
    sprite('rg312_01', 2)	# 3-4
    sprite('rg312_02', 2)	# 5-6
    sprite('rg312_03', 8)	# 7-14
    sprite('rg312_04', 4)	# 15-18	 **attackbox here**
    sprite('rg312_05', 3)	# 19-21
    sprite('rg312_06', 2)	# 22-23
    sprite('rg312_07', 2)	# 24-25

@State
def CmnActAirLockWait():
    sprite('rg045_02', 1)	# 1-1
    sprite('rg045_01', 3)	# 2-4
    sprite('rg045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('rg322_00', 2)	# 1-2
    sprite('rg322_01', 2)	# 3-4
    sprite('rg322_02', 8)	# 5-12
    sprite('rg322_03', 2)	# 13-14	 **attackbox here**
    sprite('rg322_04', 3)	# 15-17
    sprite('rg322_05', 3)	# 18-20
    sprite('rg322_05', 3)	# 21-23

@State
def CmnActLandSpin():
    sprite('rg071_00', 4)	# 1-4
    sprite('rg071_01', 4)	# 5-8
    label(0)
    sprite('rg071_02', 2)	# 9-10
    sprite('rg071_03', 2)	# 11-12
    sprite('rg071_04', 2)	# 13-14
    sprite('rg071_05', 2)	# 15-16
    sprite('rg071_06', 2)	# 17-18
    sprite('rg071_07', 2)	# 19-20
    sprite('rg071_08', 2)	# 21-22
    sprite('rg071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('rg071_10', 6)	# 1-6
    sprite('rg071_11', 5)	# 7-11
    sprite('rg071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('rg071_02', 2)	# 1-2
    sprite('rg071_03', 2)	# 3-4
    sprite('rg071_04', 2)	# 5-6
    sprite('rg071_05', 2)	# 7-8
    sprite('rg071_06', 2)	# 9-10
    sprite('rg071_07', 2)	# 11-12
    sprite('rg071_08', 2)	# 13-14
    sprite('rg071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('rg077_00', 2)	# 1-2
    sprite('rg077_01', 2)	# 3-4
    sprite('rg077_00ex01', 2)	# 5-6
    sprite('rg077_01ex01', 2)	# 7-8
    sprite('rg077_00ex02', 2)	# 9-10
    sprite('rg077_01ex02', 2)	# 11-12
    sprite('rg077_00ex03', 2)	# 13-14
    sprite('rg077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('rg077_02', 4)	# 1-4
    label(0)
    sprite('rg077_03', 3)	# 5-7
    sprite('rg077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('rg077_05', 5)	# 1-5
    sprite('rg077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('rg060_07', 3)	# 1-3
    sprite('rg060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('rg060_11', 4)	# 1-4
    sprite('rg060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('rg331_00', 2)	# 1-2
    sprite('rg331_01', 2)	# 3-4
    label(0)
    sprite('rg331_02', 3)	# 5-7
    sprite('rg331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('rg331_04', 2)	# 1-2
    sprite('rg331_05', 2)	# 3-4
    label(0)
    sprite('rg331_06', 3)	# 5-7
    sprite('rg331_07', 3)	# 8-10
    sprite('rg331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('rg331_09', 3)	# 1-3
    sprite('rg331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('rg332_00', 2)	# 1-2
    sprite('rg332_01', 2)	# 3-4
    label(0)
    sprite('rg332_02', 3)	# 5-7
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('rg332_03', 2)	# 1-2
    sprite('rg332_04', 2)	# 3-4
    label(0)
    sprite('rg332_05', 2)	# 5-6
    sprite('rg332_06', 2)	# 7-8
    sprite('rg332_07', 2)	# 9-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('rg332_08', 4)	# 1-4
    sprite('rg020_05', 3)	# 5-7
    sprite('rg020_06', 3)	# 8-10
    label(0)
    sprite('rg020_07', 4)	# 11-14
    sprite('rg020_08', 4)	# 15-18
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('rg431_00', 3)	# 1-3
    sprite('rg431_01', 3)	# 4-6
    sprite('rg431_02', 3)	# 7-9
    sprite('rg431_03', 3)	# 10-12
    GFX_0('EMB_OD', -1)
    sprite('rg431_04', 3)	# 13-15
    Unknown4047(224, 224, 224)
    Unknown4049(1500)
    Unknown4045('7267656634333168616e64706f7700000000000000000000000000000000000001000000')
    sprite('rg431_05', 3)	# 16-18
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    sprite('rg431_06', 32767)	# 19-32785
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('rg431_07', 3)	# 1-3
    SFX_3('rgse_01')
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    sprite('rg431_08', 3)	# 4-6
    GFX_0('rgef431_Start', 1)
    sprite('rg431_09', 3)	# 7-9
    sprite('rg431_08', 3)	# 10-12
    sprite('rg431_09', 3)	# 13-15
    Unknown3068('00000000ff000000ff000000ff000000ff000000')
    sprite('rg431_08', 3)	# 16-18
    Unknown3068('00000000c8000000ff000000ff000000ff000000')
    sprite('rg431_09', 3)	# 19-21
    Unknown3068('0000000096000000ff000000ff000000ff000000')
    sprite('rg431_08', 3)	# 22-24
    Unknown3068('0000000064000000ff000000ff000000ff000000')
    sprite('rg431_09', 32767)	# 25-32791
    Unknown3068('0000000028000000ff000000ff000000ff000000')

@State
def CmnActOverDriveEnd():
    sprite('rg431_10', 4)	# 1-4
    sprite('rg431_13', 4)	# 5-8
    Unknown3060('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rg431_15', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('rg333_00', 3)	# 1-3
    sprite('rg333_01', 3)	# 4-6
    sprite('rg333_02', 3)	# 7-9
    Unknown4047(224, 224, 224)
    Unknown4049(1500)
    Unknown4045('7267656634333168616e64706f7700000000000000000000000000000000000001000000')
    sprite('rg333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('rg333_04', 3)	# 1-3
    SFX_3('rgse_01')
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    sprite('rg333_05', 3)	# 4-6
    GFX_0('rgef431_Start', 1)
    sprite('rg333_06', 3)	# 7-9
    sprite('rg333_07', 3)	# 10-12
    sprite('rg333_05', 3)	# 13-15
    Unknown3068('00000000ff000000ff000000ff000000ff000000')
    sprite('rg333_06', 3)	# 16-18
    Unknown3068('00000000c8000000ff000000ff000000ff000000')
    sprite('rg333_07', 3)	# 19-21
    Unknown3068('0000000096000000ff000000ff000000ff000000')
    sprite('rg333_05', 3)	# 22-24
    Unknown3068('0000000064000000ff000000ff000000ff000000')
    sprite('rg333_06', 32767)	# 25-32791
    Unknown3068('0000000028000000ff000000ff000000ff000000')

@State
def CmnActAirOverDriveEnd():
    sprite('rg333_08', 2)	# 1-2
    sprite('rg333_09', 2)	# 3-4
    sprite('rg333_10', 2)	# 5-6
    sprite('rg020_05', 3)	# 7-9
    sprite('rg020_06', 3)	# 10-12
    label(0)
    sprite('rg020_07', 4)	# 13-16
    sprite('rg020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('rg431_00', 3)	# 1-3
    sprite('rg431_01', 3)	# 4-6
    sprite('rg431_02', 3)	# 7-9
    sprite('rg431_03', 3)	# 10-12
    GFX_0('EMB_OD', -1)
    sprite('rg431_04', 3)	# 13-15
    Unknown4047(224, 224, 224)
    Unknown4049(1500)
    Unknown4045('7267656634333168616e64706f7700000000000000000000000000000000000001000000')
    sprite('rg431_05', 3)	# 16-18
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    sprite('rg431_06', 32767)	# 19-32785
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('rg431_07', 3)	# 1-3
    SFX_3('rgse_01')
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    sprite('rg431_08', 3)	# 4-6
    GFX_0('rgef431_Start', 1)
    sprite('rg431_09', 3)	# 7-9
    sprite('rg431_08', 3)	# 10-12
    sprite('rg431_09', 3)	# 13-15
    Unknown3068('00000000ff000000ff000000ff000000ff000000')
    sprite('rg431_08', 3)	# 16-18
    Unknown3068('00000000c8000000ff000000ff000000ff000000')
    sprite('rg431_09', 3)	# 19-21
    Unknown3068('0000000096000000ff000000ff000000ff000000')
    sprite('rg431_08', 3)	# 22-24
    Unknown3068('0000000064000000ff000000ff000000ff000000')
    sprite('rg431_09', 32767)	# 25-32791
    Unknown3068('0000000028000000ff000000ff000000ff000000')

@State
def CmnActCrossRushEnd():
    sprite('rg431_10', 4)	# 1-4
    sprite('rg431_13', 4)	# 5-8
    Unknown3060('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rg431_15', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('rg333_00', 3)	# 1-3
    sprite('rg333_01', 3)	# 4-6
    sprite('rg333_02', 3)	# 7-9
    Unknown4047(224, 224, 224)
    Unknown4049(1500)
    Unknown4045('7267656634333168616e64706f7700000000000000000000000000000000000001000000')
    sprite('rg333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('rg333_04', 3)	# 1-3
    SFX_3('rgse_01')
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    sprite('rg333_05', 3)	# 4-6
    GFX_0('rgef431_Start', 1)
    sprite('rg333_06', 3)	# 7-9
    sprite('rg333_07', 3)	# 10-12
    sprite('rg333_05', 3)	# 13-15
    Unknown3068('00000000ff000000ff000000ff000000ff000000')
    sprite('rg333_06', 3)	# 16-18
    Unknown3068('00000000c8000000ff000000ff000000ff000000')
    sprite('rg333_07', 3)	# 19-21
    Unknown3068('0000000096000000ff000000ff000000ff000000')
    sprite('rg333_05', 3)	# 22-24
    Unknown3068('0000000064000000ff000000ff000000ff000000')
    sprite('rg333_06', 32767)	# 25-32791
    Unknown3068('0000000028000000ff000000ff000000ff000000')

@State
def CmnActAirCrossRushEnd():
    sprite('rg333_08', 2)	# 1-2
    sprite('rg333_09', 2)	# 3-4
    sprite('rg333_10', 2)	# 5-6
    sprite('rg020_05', 3)	# 7-9
    sprite('rg020_06', 3)	# 10-12
    label(0)
    sprite('rg020_07', 4)	# 13-16
    sprite('rg020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('rg331_00', 2)	# 1-2
    sprite('rg331_01', 2)	# 3-4
    label(0)
    sprite('rg331_02', 3)	# 5-7
    sprite('rg331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('rg331_04', 2)	# 1-2
    sprite('rg331_05', 2)	# 3-4
    label(0)
    sprite('rg331_06', 3)	# 5-7
    sprite('rg331_07', 3)	# 8-10
    sprite('rg331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('rg331_09', 3)	# 1-3
    sprite('rg331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('rg332_00', 2)	# 1-2
    sprite('rg332_01', 2)	# 3-4
    label(0)
    sprite('rg332_02', 3)	# 5-7
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('rg332_03', 2)	# 1-2
    sprite('rg332_04', 2)	# 3-4
    label(0)
    sprite('rg332_05', 2)	# 5-6
    sprite('rg332_06', 2)	# 7-8
    sprite('rg332_07', 2)	# 9-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('keep', 3)	# 1-3
    sprite('rg332_08', 3)	# 4-6
    sprite('rg020_05', 3)	# 7-9
    sprite('rg020_06', 3)	# 10-12
    label(0)
    sprite('rg020_07', 4)	# 13-16
    sprite('rg020_08', 4)	# 17-20
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

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_CLEAR_OR_EXIT():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('rg300_00', 4)	# 1-4
    loopRest()
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    SFX_0('301_overdrive_end')
    sprite('rg300_01', 4)	# 5-8
    if random_(2, 0, 50):
        SFX_1('rg404')
    else:
        SFX_1('rg405')
    sprite('rg300_02', 4)	# 9-12
    sprite('rg300_03', 4)	# 13-16
    sprite('rg300_05', 27)	# 17-43
    sprite('rg300_03', 4)	# 44-47
    sprite('rg300_06', 5)	# 48-52
    sprite('rg300_07', 5)	# 53-57
    sprite('rg300_08', 5)	# 58-62

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_CLEAR_OR_EXIT():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('rg045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('rg045_00', 3)	# 2-4
    sprite('rg045_01', 4)	# 5-8
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    SFX_0('301_overdrive_end')
    label(0)
    sprite('rg045_02', 5)	# 9-13
    sprite('rg045_02ex', 5)	# 14-18
    loopRest()
    Unknown2038(1)
    if (SLOT_2 == 5):
        Unknown1018()
        Unknown1023()
        Unknown1038()
        Unknown1019(40)
        YAccel(40)
    (SLOT_2 >= 6)
    if SLOT_ReturnVal:
        _gotolabel(1)
    gotoLabel(0)
    label(1)
    sprite('rg045_01', 6)	# 19-24
    sprite('rg045_00', 6)	# 25-30

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

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
    sprite('rg414_06ex', 3)	# 631-633	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(2000000)
    physicsYImpulse(-400000)
    setGravity(0)
    Unknown2053(1)
    EnableCollision(1)
    label(1)
    sprite('rg414_06ex', 3)	# 634-636	 **attackbox here**
    Unknown4048(90000)
    Unknown4049(1500)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000002000000')
    sprite('rg414_06ex', 3)	# 637-639	 **attackbox here**
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('rg414_07', 3)	# 640-642	 **attackbox here**
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    sprite('rg414_08', 5)	# 643-647
    sprite('rg414_09', 5)	# 648-652
    sprite('rg414_10', 3)	# 653-655
    sprite('rg414_11', 3)	# 656-658
    sprite('rg414_12', 3)	# 659-661
    sprite('rg414_13', 3)	# 662-664

@State
def CmnActChangePartnerQuickIn():
    sprite('rg032_08', 3)	# 1-3
    sprite('rg032_08', 5)	# 4-8
    sprite('rg032_09', 7)	# 9-15
    sprite('rg032_10', 7)	# 16-22
    sprite('rg032_11', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rg033_02', 3)	# 1-3
    sprite('rg033_03', 3)	# 4-6
    sprite('rg033_02', 3)	# 7-9
    sprite('rg033_03', 3)	# 10-12
    sprite('rg033_02', 3)	# 13-15
    sprite('rg033_03', 3)	# 16-18
    sprite('rg033_02', 3)	# 19-21
    sprite('rg033_03', 3)	# 22-24
    sprite('rg033_02', 3)	# 25-27
    sprite('rg033_03', 3)	# 28-30
    sprite('rg033_02', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('rg033_00', 1)	# 1-1
    sprite('rg033_01', 2)	# 2-3
    SFX_3('rgse_00')
    sprite('rg033_02', 2)	# 4-5
    sprite('rg033_02', 1)	# 6-6
    sprite('rg033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('rg033_02', 3)	# 10-12
    sprite('rg033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg033_04', 3)	# 16-18
    sprite('rg033_05', 3)	# 19-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rg300_00', 4)	# 1-4
    sprite('rg300_01', 4)	# 5-8
    sprite('rg300_02', 4)	# 9-12
    sprite('rg300_03', 6)	# 13-18
    sprite('rg300_04', 6)	# 19-24
    sprite('rg300_05', 6)	# 25-30
    sprite('rg300_03', 6)	# 31-36
    sprite('rg300_04', 6)	# 37-42
    sprite('rg300_05', 6)	# 43-48
    sprite('rg300_03', 10)	# 49-58
    sprite('rg300_06', 6)	# 59-64
    sprite('rg300_07', 6)	# 65-70
    sprite('rg300_08', 30)	# 71-100

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
    sprite('rg020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('rg020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('rg010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(5)
        AttackP1(70)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(10000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(40)
        AirUntechableTime(60)
        Hitstop(16)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11042(1)
        Unknown9016(1)
        Unknown30040(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(2)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
        Unknown2006()
    sprite('rg412_00', 4)	# 1-4
    sprite('rg412_01', 3)	# 5-7
    Unknown7007('6272673230395f300000000000000000640000006272673230395f310000000000000000640000006272673230395f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown8001(3, 100)
    physicsYImpulse(42000)
    setGravity(2200)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    SLOT_12 = SLOT_19
    Unknown1019(3)
    if (SLOT_12 <= 10000):
        SLOT_12 = 10000
    sprite('rg412_02', 3)	# 8-10
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3074('00000000ff000000000000007f000000')
    Unknown3075('000000007f00000000000000ff000000')
    Unknown3076(1010)
    Unknown3077(1100)
    Unknown2004(1, 1)
    sprite('rg412_03', 3)	# 11-13
    sprite('rg412_04', 3)	# 14-16
    SLOT_12 = SLOT_19
    Unknown1019(3)
    if (SLOT_12 <= 10000):
        SLOT_12 = 10000
    sprite('rg412_05', 8)	# 17-24
    Unknown2015(150)
    sprite('rg412_06', 4)	# 25-28
    Unknown23087(120000)
    GFX_0('rgef412effpos', -1)
    Unknown1019(80)
    sprite('rg412_07', 4)	# 29-32
    Unknown1019(80)
    SFX_0('010_swing_sword_2')
    sprite('rg412_08', 4)	# 33-36
    Unknown1019(80)
    sprite('rg412_09', 3)	# 37-39	 **attackbox here**
    sprite('rg412_10', 2)	# 40-41
    Recovery()
    sprite('rg412_11', 2)	# 42-43
    sprite('rg412_12', 2)	# 44-45
    sprite('rg412_13', 32767)	# 46-32812
    Unknown2015(-1)
    label(2)
    sprite('rg412_14', 2)	# 32813-32814
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('rg024_02', 2)	# 32815-32816
    sprite('rg024_03', 2)	# 32817-32818
    sprite('rg024_04', 2)	# 32819-32820

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        AttackP1(70)
        AirPushbackX(4800)
        AirPushbackY(45000)
        AirUntechableTime(75)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown11042(1)
    sprite('rg213_02', 1)	# 1-1
    sprite('rg213_03', 2)	# 2-3
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    Unknown7007('6272673130365f310000000000000000640000006272673130365f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rg213_04', 2)	# 4-5
    sprite('rg213_05', 2)	# 6-7
    teleportRelativeX(50000)
    physicsXImpulse(9500)
    physicsYImpulse(18000)
    Unknown1043()
    sendToLabelUpon(2, 9)
    sprite('rg213_06', 2)	# 8-9
    GFX_0('rgef213atk', -1)
    sprite('rg213_07', 2)	# 10-11
    sprite('rg213_08', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('rg213_09', 2)	# 15-16
    Recovery()
    sprite('rg213_10', 2)	# 17-18
    Unknown1019(60)
    sprite('rg213_11', 2)	# 19-20
    sprite('rg213_12', 2)	# 21-22
    sprite('rg213_13', 2)	# 23-24
    sprite('rg213_14', 32767)	# 25-32791
    label(9)
    sprite('rg213_15', 5)	# 32792-32796
    Recovery()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rg213_16', 5)	# 32797-32801
    sprite('rg213_17', 4)	# 32802-32805
    sprite('rg213_18', 4)	# 32806-32809
    sprite('rg213_19', 4)	# 32810-32813

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(4)
        AttackP1(70)
        hitstun(27)
        AirUntechableTime(40)
        AirPushbackX(16000)
        AirPushbackY(20000)
        PushbackX(18000)
        Unknown11042(1)
        Unknown30039(24)
        Unknown30040(1)

        def upon_CLEAR_OR_EXIT():
            (SLOT_19 < 200000)
            if op(5, 2, 0, 2, 51):
                if SLOT_2:
                    sendToLabel(0)

        def upon_12():
            sendToLabel(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
        Unknown2006()
    sprite('rg402_00', 2)	# 1-2
    Unknown8000(100, 1, 1)
    EnableCollision(1)
    Unknown2053(1)
    Unknown2034(1)
    tag_voice(1, 'brg200_0', 'brg200_1', 'brg200_2', '')
    Unknown1084(1)
    sprite('rg400_01', 2)	# 3-4
    sprite('rg400_02', 3)	# 5-7
    sprite('rg400_03', 2)	# 8-9
    sprite('rg400_04', 3)	# 10-12
    GFX_0('rgef400loop', -1)
    Unknown38(4, 1)
    physicsXImpulse(43000)
    Unknown8006(100, 1, 0)
    sprite('rg400_05ex1', 2)	# 13-14	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06ex1', 3)	# 15-17	 **attackbox here**
    Unknown2015(250)
    Unknown8006(100, 1, 0)
    sprite('rg400_07', 2)	# 18-19	 **attackbox here**
    SLOT_51 = 1
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 2)	# 20-21	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_07', 2)	# 22-23	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 2)	# 24-25	 **attackbox here**
    Unknown8006(100, 1, 0)
    label(0)
    sprite('rg400_08', 2)	# 26-27
    clearUponHandler(3)
    clearUponHandler(12)
    Unknown13(4)
    Unknown2015(-1)
    GFX_0('rgef400end', -1)
    Unknown1019(70)
    Unknown1028(-1000)
    Recovery()
    sprite('rg400_09', 2)	# 28-29
    sprite('rg400_10', 2)	# 30-31
    Unknown8006(100, 1, 0)
    sprite('rg400_11', 2)	# 32-33
    Unknown8006(100, 1, 0)
    sprite('rg400_12', 2)	# 34-35
    Unknown8006(100, 1, 0)
    sprite('rg400_13', 2)	# 36-37
    Unknown8006(100, 1, 0)
    sprite('rg400_14', 4)	# 38-41
    sprite('rg400_15', 4)	# 42-45
    SFX_0('208_brake_normal')
    sprite('rg400_16', 4)	# 46-49
    SFX_0('208_brake_normal')
    Unknown1028(0)
    physicsXImpulse(0)
    sprite('rg400_17', 4)	# 50-53
    sprite('rg400_18', 4)	# 54-57
    sprite('rg400_19', 5)	# 58-62
    loopRest()
    ExitState()
    label(1)
    sprite('rg401_00', 2)	# 63-64
    clearUponHandler(3)
    clearUponHandler(12)
    Unknown13(4)
    Unknown11097(300, 300)
    ChipDamagePct(0)
    Unknown9015(1)
    Unknown11097(100, 100)
    Unknown1019(70)
    sprite('rg401_01', 3)	# 65-67
    Unknown1019(70)
    sprite('rg401_02', 3)	# 68-70
    Unknown1019(70)
    sprite('rg401_03', 3)	# 71-73
    Unknown1019(70)
    sprite('rg401_04', 2)	# 74-75
    Unknown1019(70)
    tag_voice(0, 'brg201_0', 'brg201_1', 'brg201_2', '')
    sprite('rg401_05', 2)	# 76-77
    Unknown1019(0)
    GFX_0('rgef401atk', -1)
    sprite('rg401_06', 1)	# 78-78
    sprite('rg401_07', 1)	# 79-79
    sprite('rg401_08', 1)	# 80-80
    SFX_0('004_swing_grap_1_0')
    SFX_0('004_swing_grap_1_1')
    SFX_3('rgse_20')
    SFX_3('rgse_20')
    sprite('rg401_09ex', 6)	# 81-86	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    WallbounceReboundTime(5)
    Unknown9215()
    AirPushbackX(80000)
    AirPushbackY(20000)
    AirUntechableTime(60)
    sprite('rg401_10', 2)	# 87-88
    Recovery()
    sprite('rg401_11', 2)	# 89-90
    sprite('rg401_12', 9)	# 91-99
    sprite('rg401_13', 2)	# 100-101
    sprite('rg401_14', 2)	# 102-103
    sprite('rg401_15', 2)	# 104-105
    sprite('rg401_16', 2)	# 106-107
    sprite('rg401_17', 2)	# 108-109
    sprite('rg401_18', 2)	# 110-111

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
    Unknown2036(69, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('rg020_07', 4)	# 3-6
    sprite('rg020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('BloodWeaponFinishDDDOD')
    else:
        enterState('BloodWeaponFinishDDD')

@State
def BloodWeaponFinishDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(35)
        Unknown9142(60)
        Unknown9310(12)
        PushbackX(100)
        Unknown11072(1, 300000, 0)
        Unknown30048(1)
        Unknown30063(1)
        Unknown11032('801a060050c30000801a0600ffffffff')
        Unknown11062(1)
        Hitstop(10)
        Unknown11068(1)
        Unknown2004(1, 0)
        Unknown11067(1)
        Unknown11069('BloodWeaponFinishDDD_2nd')

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
            enterState('BloodWeaponFinishDDD_2nd')
            tag_voice(1, 'brg253_0', 'brg253_1', '', '')
            EnableCollision(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_52:
                SLOT_51 = (SLOT_51 + 1)
                if (SLOT_51 == 5):
                    SLOT_51 = 0
                    ScreenShake(1000, 8000)
    sprite('rg432_00', 4)	# 1-4
    SFX_3('rgse_04')
    setInvincible(1)
    sprite('rg432_01', 4)	# 5-8
    sprite('rg432_02', 4)	# 9-12
    sprite('rg432_03', 5)	# 13-17
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    SFX_0('019_quake_0')
    SLOT_52 = 1
    sprite('rg432_03', 5)	# 18-22
    sprite('rg432_03', 5)	# 23-27
    sprite('rg432_03', 5)	# 28-32
    SFX_0('019_quake_0')
    sprite('rg432_03', 4)	# 33-36
    sprite('rg432_04', 4)	# 37-40
    SLOT_52 = 0
    SFX_3('rgse_22')
    SFX_3('rgse_22')
    sprite('rg432_04ex01', 4)	# 41-44
    sprite('rg432_05', 3)	# 45-47	 **attackbox here**
    sprite('rg432_23', 5)	# 48-52
    GFX_0('rgef432lock', 1)
    teleportRelativeX(-130000)
    setInvincible(0)
    sprite('rg432_24', 5)	# 53-57
    sprite('rg432_25', 5)	# 58-62
    sprite('rg432_26', 5)	# 63-67
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg432_27', 5)	# 68-72
    sprite('rg432_28', 5)	# 73-77
    sprite('rg432_29', 10)	# 78-87
    sprite('rg432_30', 5)	# 88-92
    sprite('rg432_31', 5)	# 93-97
    sprite('rg432_32', 5)	# 98-102

@State
def BloodWeaponFinishDDD_2nd():

    def upon_IMMEDIATE():
        Unknown17011('BloodWeaponFinishDDD_3rd', 3, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP2(100)
        setInvincible(1)
        Unknown3029(1)
        Unknown3070(2)
        Unknown3071(5)
        Unknown3074('00000000800000000000000000000000')
        Unknown3075('00000000000000000000000000000000')
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown30063(1)
        Unknown30068(1)
        Unknown11069('BloodWeaponFinishDDD_3rd')
        Unknown11023(1)
        EnableCollision(0)
        Unknown11108('03000000')
    sprite('rg432_05ex01', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown4047(220, 220, 220)
    Unknown4045('726765663433326c6f636b00000000000000000000000000000000000000000001000000')
    GFX_0('rgef432lock', 1)
    sprite('rg432_06', 5)	# 4-8
    sprite('rg432_07', 5)	# 9-13
    sprite('rg432_08', 5)	# 14-18
    SFX_0('022_magiccircle_a')
    sprite('rg432_09', 5)	# 19-23
    sprite('rg432_10', 5)	# 24-28
    Unknown2006()
    sprite('rg432_11', 5)	# 29-33
    sprite('rg432_12', 5)	# 34-38	 **attackbox here**
    sprite('rg432_23', 5)	# 39-43
    sprite('rg432_24', 5)	# 44-48
    sprite('rg432_25', 5)	# 49-53
    sprite('rg432_26', 5)	# 54-58
    sprite('rg432_27', 5)	# 59-63
    sprite('rg432_28', 5)	# 64-68
    sprite('rg432_29', 10)	# 69-78
    sprite('rg432_30', 5)	# 79-83
    sprite('rg432_31', 5)	# 84-88
    sprite('rg432_32', 5)	# 89-93

@State
def BloodWeaponFinishDDD_3rd():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        Damage(2500)
        AttackP2(100)
        AttackP1(100)
        MinimumDamagePct(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        AirPushbackX(8000)
        AirPushbackY(33333)
        YImpluseBeforeWallbounce(1500)
        Hitstop(14)
        Unknown9016(1)
        StarterRating(0)
        Unknown11002(-1)
        Unknown11097(500, 500)
        Unknown11108('03000000')
        Unknown30063(1)
        Unknown30061(0)
        setInvincible(1)
    sprite('rg432_14', 3)	# 1-3
    GFX_0('rgef432loop', 2)
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg432_15', 3)	# 4-6
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_16', 3)	# 7-9
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 10-12
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_18', 3)	# 13-15
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 16-18
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_20', 3)	# 19-21
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 22-24
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_15', 3)	# 25-27
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_16', 3)	# 28-30
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_17', 3)	# 31-33
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 34-36
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 37-39
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 40-42
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_22', 13)	# 43-55	 **attackbox here**
    SFX_0('101_hit_slash_3')
    SFX_0('103_hit_counter_slash_2')
    RefreshMultihit()
    tag_voice(0, 'brg254_0', 'brg254_1', '', '')
    Unknown4049(3000)
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000000000000')
    Unknown4047(215, 215, 209)
    Unknown4045('72676566343332627265616b000000000000000000000000000000000000000000000000')
    GFX_0('rgef432fall', -1)
    sprite('rg432_23', 5)	# 56-60
    sprite('rg432_24', 5)	# 61-65
    sprite('rg432_25', 5)	# 66-70
    sprite('rg432_26', 5)	# 71-75
    sprite('rg432_27', 5)	# 76-80
    sprite('rg432_28', 5)	# 81-85
    sprite('rg432_29', 10)	# 86-95
    sprite('rg432_30', 5)	# 96-100
    sprite('rg432_31', 5)	# 101-105
    sprite('rg432_32', 5)	# 106-110

@State
def BloodWeaponFinishDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(4)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(35)
        Unknown9142(60)
        Unknown9310(12)
        PushbackX(100)
        Unknown11072(1, 300000, 0)
        Unknown30048(1)
        Unknown11032('801a060050c30000801a0600ffffffff')
        Unknown11062(1)
        Hitstop(10)
        Unknown11068(1)
        Unknown2004(1, 0)
        Unknown11067(1)
        Unknown11069('BloodWeaponFinishDDDOD_2nd')

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
            enterState('BloodWeaponFinishDDDOD_2nd')
            tag_voice(1, 'brg253_0', 'brg253_1', '', '')
            EnableCollision(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_52:
                SLOT_51 = (SLOT_51 + 1)
                if (SLOT_51 == 5):
                    SLOT_51 = 0
                    ScreenShake(1000, 8000)
    sprite('rg432_00', 4)	# 1-4
    SFX_3('rgse_04')
    setInvincible(1)
    sprite('rg432_01', 4)	# 5-8
    sprite('rg432_02', 4)	# 9-12
    sprite('rg432_03', 5)	# 13-17
    SFX_0('019_quake_0')
    SLOT_52 = 1
    sprite('rg432_03', 5)	# 18-22
    sprite('rg432_03', 5)	# 23-27
    sprite('rg432_03', 5)	# 28-32
    SFX_0('019_quake_0')
    sprite('rg432_03', 4)	# 33-36
    sprite('rg432_04', 4)	# 37-40
    SLOT_52 = 0
    SFX_3('rgse_22')
    SFX_3('rgse_22')
    sprite('rg432_04ex01', 4)	# 41-44
    sprite('rg432_05', 3)	# 45-47	 **attackbox here**
    sprite('rg432_23', 5)	# 48-52
    GFX_0('rgef432lock', 1)
    teleportRelativeX(-130000)
    setInvincible(0)
    sprite('rg432_24', 5)	# 53-57
    sprite('rg432_25', 5)	# 58-62
    sprite('rg432_26', 5)	# 63-67
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg432_27', 5)	# 68-72
    sprite('rg432_28', 5)	# 73-77
    setInvincible(0)
    sprite('rg432_29', 10)	# 78-87
    sprite('rg432_30', 5)	# 88-92
    sprite('rg432_31', 5)	# 93-97
    sprite('rg432_32', 5)	# 98-102

@State
def BloodWeaponFinishDDDOD_2nd():

    def upon_IMMEDIATE():
        Unknown17011('BloodWeaponFinishDDDOD_3rd', 3, 0, 0)
        Unknown30063(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP2(100)
        setInvincible(1)
        Unknown3029(1)
        Unknown3070(2)
        Unknown3071(5)
        Unknown3074('00000000800000000000000000000000')
        Unknown3075('00000000000000000000000000000000')
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown30061(0)
        Unknown30063(1)
        Unknown30068(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11023(1)
        EnableCollision(0)
        Unknown11108('03000000')
        Unknown11069('BloodWeaponFinishDDDOD_3rd')
    sprite('rg432_05ex01', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown4047(220, 220, 220)
    Unknown4045('726765663433326c6f636b00000000000000000000000000000000000000000001000000')
    GFX_0('rgef432lock', 1)
    sprite('rg432_06', 5)	# 4-8
    sprite('rg432_07', 5)	# 9-13
    sprite('rg432_08', 5)	# 14-18
    SFX_0('022_magiccircle_a')
    sprite('rg432_09', 5)	# 19-23
    sprite('rg432_10', 5)	# 24-28
    Unknown2006()
    sprite('rg432_11', 5)	# 29-33
    sprite('rg432_12', 5)	# 34-38	 **attackbox here**
    sprite('rg432_23', 5)	# 39-43
    sprite('rg432_24', 5)	# 44-48
    sprite('rg432_25', 5)	# 49-53
    sprite('rg432_26', 5)	# 54-58
    sprite('rg432_27', 5)	# 59-63
    sprite('rg432_28', 5)	# 64-68
    sprite('rg432_29', 10)	# 69-78
    sprite('rg432_30', 5)	# 79-83
    sprite('rg432_31', 5)	# 84-88
    sprite('rg432_32', 5)	# 89-93

@State
def BloodWeaponFinishDDDOD_3rd():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown30063(1)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        Damage(3000)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        AirPushbackX(8000)
        AirPushbackY(33333)
        YImpluseBeforeWallbounce(1500)
        Hitstop(20)
        Unknown9016(1)
        StarterRating(0)
        Unknown11002(-1)
        Unknown11097(1000, 1000)
        Unknown11108('03000000')
        Unknown30063(1)
        Unknown30061(0)
        setInvincible(1)
    sprite('rg432_14', 3)	# 1-3
    GFX_0('rgef432loop_SP', 2)
    Unknown4047(211, 210, 209)
    Unknown4045('726765663433325f6e646c303000000000000000000000000000000000000000ffffffff')
    Unknown4047(209, 216, 209)
    Unknown4045('726765663433325f6e646c000000000000000000000000000000000000000000ffffffff')
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg432_15', 3)	# 4-6
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_16', 3)	# 7-9
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 10-12
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_18', 3)	# 13-15
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 16-18
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_20', 3)	# 19-21
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 22-24
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_15', 3)	# 25-27
    Unknown4047(209, 216, 209)
    Unknown4045('726765663433325f6e646c000000000000000000000000000000000000000000ffffffff')
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_16', 3)	# 28-30
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_17', 3)	# 31-33
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 34-36
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 37-39
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 40-42
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_15', 3)	# 43-45
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_16', 3)	# 46-48
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 49-51
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 52-54
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_19', 3)	# 55-57
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_20', 3)	# 58-60
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_21', 3)	# 61-63
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_15', 3)	# 64-66
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_16', 3)	# 67-69
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 70-72
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 73-75
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_19', 3)	# 76-78
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_20', 3)	# 79-81
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_21', 3)	# 82-84
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_15', 3)	# 85-87
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(4)
    sprite('rg432_16', 3)	# 88-90
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(4)
    sprite('rg432_17', 3)	# 91-93
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(5)
    sprite('rg432_18', 3)	# 94-96
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(5)
    sprite('rg432_19', 3)	# 97-99
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(6)
    sprite('rg432_20', 3)	# 100-102
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(6)
    sprite('rg432_21', 3)	# 103-105
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(7)
    label(0)
    sprite('rg432_22', 13)	# 106-118	 **attackbox here**
    SFX_0('101_hit_slash_3')
    SFX_0('103_hit_counter_slash_2')
    RefreshMultihit()
    tag_voice(0, 'brg254_0', 'brg254_1', '', '')
    Unknown4049(3000)
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000000000000')
    Unknown4047(215, 215, 209)
    Unknown4045('72676566343332627265616b000000000000000000000000000000000000000000000000')
    GFX_0('rgef432fall', -1)
    sprite('rg432_23', 5)	# 119-123
    sprite('rg432_24', 5)	# 124-128
    sprite('rg432_25', 5)	# 129-133
    sprite('rg432_26', 5)	# 134-138
    sprite('rg432_27', 5)	# 139-143
    sprite('rg432_28', 5)	# 144-148
    sprite('rg432_29', 10)	# 149-158
    sprite('rg432_30', 5)	# 159-163
    sprite('rg432_31', 5)	# 164-168
    sprite('rg432_32', 5)	# 169-173

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
    SFX_3('rgse_00')
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
        Unknown9016(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('rg414_06ex', 3)	# 121-123	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('rg414_06ex', 3)	# 124-126	 **attackbox here**
    Unknown4048(90000)
    Unknown4049(1500)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000002000000')
    sprite('rg414_06ex', 3)	# 127-129	 **attackbox here**
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('rg414_07', 3)	# 130-132	 **attackbox here**
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    sprite('rg414_07', 5)	# 133-137	 **attackbox here**
    sprite('rg414_08', 6)	# 138-143
    sprite('rg414_09', 5)	# 144-148
    sprite('rg414_10', 3)	# 149-151
    sprite('rg414_11', 3)	# 152-154
    sprite('rg414_12', 3)	# 155-157
    sprite('rg414_13', 3)	# 158-160

@State
def CmnActChangeReturnAppealBurst():
    sprite('rg111_07', 50)	# 1-50
    sprite('rg111_08', 5)	# 51-55
    sprite('rg111_09', 30)	# 56-85

@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
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
    sprite('rg414_06ex', 3)	# 32-34	 **attackbox here**
    Unknown4048(90000)
    Unknown4049(1500)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000002000000')
    sprite('rg414_06ex', 3)	# 35-37	 **attackbox here**
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 38-38
    sprite('rg414_07', 3)	# 39-41	 **attackbox here**
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    sprite('rg414_07', 5)	# 42-46	 **attackbox here**
    Unknown23022(0)
    sprite('rg414_08', 6)	# 47-52
    sprite('rg414_09', 5)	# 53-57
    sprite('rg414_10', 3)	# 58-60
    sprite('rg414_11', 3)	# 61-63
    sprite('rg414_12', 3)	# 64-66
    sprite('rg414_13', 3)	# 67-69

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('rg414_07', 2)	# 2-3	 **attackbox here**
    StartMultihit()
    sprite('rg414_08', 2)	# 4-5
    sprite('rg414_09', 2)	# 6-7
    sprite('rg414_10', 2)	# 8-9
    sprite('rg414_11', 3)	# 10-12
    sprite('rg414_12', 3)	# 13-15
    sprite('rg440_02', 3)	# 16-18
    sprite('rg440_03', 3)	# 19-21
    teleportRelativeX(-30000)
    sprite('rg440_04', 3)	# 22-24
    teleportRelativeX(-30000)
    sprite('rg440_05', 2)	# 25-26
    Unknown7009(2)
    GFX_0('rgef440StartEff', -1)
    sprite('rg440_06', 2)	# 27-28
    sprite('rg440_07', 2)	# 29-30
    SFX_3('rgse_26')
    sprite('rg440_08', 2)	# 31-32
    sprite('rg440_09', 2)	# 33-34
    sprite('rg440_10', 4)	# 35-38	 **attackbox here**
    GFX_0('rgef440', -1)
    sprite('rg440_11', 4)	# 39-42
    sprite('rg440_12', 15)	# 43-57
    sprite('rg440_13', 6)	# 58-63
    sprite('rg440_14', 6)	# 64-69
    sprite('rg440_15', 6)	# 70-75

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        WhiffCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('rg200_00', 2)	# 1-2
    Unknown1051(60)
    sprite('rg200_01', 1)	# 3-3
    sprite('rg200_01', 1)	# 4-4
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    sprite('rg200_02', 3)	# 5-7	 **attackbox here**
    sprite('rg200_03', 3)	# 8-10
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('rg200_04', 3)	# 11-13
    sprite('rg200_05', 3)	# 14-16

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(15000)
        Unknown2004(1, 0)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('rg211_00', 1)	# 1-1
    sprite('rg211_03', 1)	# 2-2
    sprite('rg211_04', 1)	# 3-3
    sprite('rg211_05', 1)	# 4-4
    sprite('rg211_06', 1)	# 5-5
    SFX_0('004_swing_grap_1_2')
    Unknown7009(0)
    sprite('rg211_07', 1)	# 6-6
    sprite('rg211_08', 1)	# 7-7
    sprite('rg211_09', 2)	# 8-9	 **attackbox here**
    sprite('rg211_10', 3)	# 10-12	 **attackbox here**
    sprite('rg211_11', 3)	# 13-15	 **attackbox here**
    sprite('rg211_12', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('rg211_13', 3)	# 19-21
    sprite('rg211_14', 4)	# 22-25
    sprite('rg211_15', 3)	# 26-28
    sprite('rg211_16', 2)	# 29-30
    sprite('rg211_16', 1)	# 31-31
    SFX_FOOTSTEP_(100, 1, 1)

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(20000)
        PushbackX(20000)
        Unknown9016(1)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('rg202_00', 1)	# 1-1
    sprite('rg202_01', 1)	# 2-2
    sprite('rg202_02', 2)	# 3-4
    sprite('rg202_05', 2)	# 5-6
    SFX_0('008_swing_pole_2')
    Unknown7009(1)
    sprite('rg202_06', 2)	# 7-8
    sprite('rg202_07', 2)	# 9-10
    sprite('rg202_08', 1)	# 11-11	 **attackbox here**
    StartMultihit()
    sprite('rg202_09', 4)	# 12-15	 **attackbox here**
    sprite('rg202_10', 2)	# 16-17
    Recovery()
    Unknown2063()
    sprite('rg202_11', 2)	# 18-19
    sprite('rg202_12', 2)	# 20-21
    sprite('rg202_13', 2)	# 22-23
    sprite('rg202_14', 2)	# 24-25
    sprite('rg202_15', 2)	# 26-27
    sprite('rg202_16', 3)	# 28-30
    sprite('rg202_17', 3)	# 31-33
    sprite('rg202_18', 2)	# 34-35

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(90)
        Unknown11092(1)
        AirUntechableTime(40)
        AirPushbackY(16000)
        PushbackX(12000)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown9016(1)
        HitLow(2)
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('rg212_00', 2)	# 1-2
    sprite('rg212_01', 2)	# 3-4
    Unknown7009(2)
    sprite('rg212_02', 2)	# 5-6
    sprite('rg212_03', 2)	# 7-8
    sprite('rg212_04', 2)	# 9-10
    SFX_0('006_swing_blade_2')
    sprite('rg212_05', 2)	# 11-12
    sprite('rg212_06', 1)	# 13-13	 **attackbox here**
    sprite('rg212_07', 1)	# 14-14
    sprite('rg212_08', 1)	# 15-15
    sprite('rg212_09', 1)	# 16-16
    sprite('rg212_10', 1)	# 17-17
    SFX_0('006_swing_blade_2')
    sprite('rg212_11', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    AttackP1(100)
    AirPushbackX(0)
    AirPushbackY(30000)
    HitLow(0)
    Unknown11058('0000000001000000000000000000000000000000')

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockJumpCancel(1)
    sprite('rg212_12', 7)	# 20-26
    Recovery()
    Unknown2063()
    sprite('rg212_13', 4)	# 27-30
    sprite('rg212_14', 4)	# 31-34
    sprite('rg212_15', 3)	# 35-37
    sprite('rg212_16', 3)	# 38-40
    sprite('rg212_17', 3)	# 41-43
    sprite('rg212_18', 3)	# 44-46
    sprite('rg212_19', 3)	# 47-49
    sprite('rg212_20', 3)	# 50-52

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(5)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(40)
        AirPushbackX(30000)
        AirPushbackY(18000)
        Unknown9016(1)
        Unknown11044(1)
        JumpCancel_(0)
        DisableAttackRestOfMove()
    sprite('rg450_00', 3)	# 1-3
    sprite('rg450_01', 4)	# 4-7
    sprite('rg450_02', 4)	# 8-11
    GFX_0('NmlAtk5AAAA_Eff', -1)
    Unknown4020(1)
    SFX_3('rgse_02')
    SFX_0('005_swing_grap_2_2')
    Unknown7009(2)
    sprite('rg450_05', 4)	# 12-15
    sprite('rg450_06', 2)	# 16-17
    sprite('rg450_07ex01', 4)	# 18-21	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 15000)
    Unknown30088(1)
    sprite('rg450_08', 4)	# 22-25
    Unknown4020(0)
    Recovery()
    Unknown2063()
    sprite('rg450_09', 4)	# 26-29
    sprite('rg450_10', 4)	# 30-33
    sprite('rg450_11', 4)	# 34-37
    sprite('rg450_12', 3)	# 38-40
    sprite('rg450_13', 3)	# 41-43
    sprite('rg450_14', 3)	# 44-46
    sprite('rg450_15', 3)	# 47-49
    sprite('rg450_16', 3)	# 50-52

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(70)
        AirUntechableTime(26)
        AirPushbackX(1000)
        AirPushbackY(30000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown2004(1, 0)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('rg210_00', 2)	# 1-2
    sprite('rg210_01', 1)	# 3-3
    sprite('rg210_01', 1)	# 4-4
    Unknown7009(1)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('rg210_02', 2)	# 5-6
    sprite('rg210_03', 2)	# 7-8
    sprite('rg210_04', 2)	# 9-10
    SFX_0('004_swing_grap_1_1')
    sprite('rg210_05', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('rg210_06', 3)	# 12-14	 **attackbox here**
    setInvincible(0)
    sprite('rg210_07', 4)	# 15-18
    Recovery()
    Unknown2063()
    sprite('rg210_08', 4)	# 19-22
    sprite('rg210_09', 4)	# 23-26
    sprite('rg210_10', 4)	# 27-30
    sprite('rg210_11', 4)	# 31-34
    sprite('rg210_12', 4)	# 35-38

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(1000)
        Unknown11092(1)
        AirUntechableTime(24)
        Hitstop(6)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(18000)
        PushbackX(19800)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
    sprite('rg203_00', 2)	# 1-2
    sprite('rg203_01', 2)	# 3-4
    sprite('rg203_02', 3)	# 5-7
    SFX_0('005_swing_grap_2_1')
    sprite('rg203_03', 5)	# 8-12
    sprite('rg203_04', 1)	# 13-13
    Unknown7007('6272673130365f300000000000000000640000006272673130365f310000000000000000640000006272673130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg203_05', 1)	# 14-14	 **attackbox here**
    StartMultihit()
    sprite('rg203_05', 2)	# 15-16	 **attackbox here**
    GFX_0('rgef203atk', -1)
    sprite('rg203_06', 3)	# 17-19	 **attackbox here**
    sprite('rg203_07', 5)	# 20-24
    sprite('rg203_08', 4)	# 25-28
    sprite('rg203_09', 3)	# 29-31
    SFX_3('rgse_02')
    SFX_0('005_swing_grap_2_2')
    sprite('rg203_10', 3)	# 32-34	 **attackbox here**
    Unknown23183('72673230335f313065783031000000000000000000000000000000000000000003000000020000003a000000')
    RefreshMultihit()
    Unknown11097(300, 300)
    ChipDamagePct(0)
    Damage(2000)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(8500)
    AirPushbackY(-100000)
    YImpluseBeforeWallbounce(0)
    Unknown9310(1)
    Hitstop(13)
    PushbackX(39900)
    blockstun(25)

    def upon_77():
        HitOrBlockCancel('NmlAtk5BBB')
    sprite('rg203_11', 3)	# 35-37
    Recovery()
    Unknown2063()
    sprite('rg203_12', 4)	# 38-41
    sprite('rg203_13', 4)	# 42-45
    sprite('rg203_14', 4)	# 46-49
    sprite('rg203_15', 4)	# 50-53
    sprite('rg203_16', 4)	# 54-57
    sprite('rg203_17', 3)	# 58-60
    sprite('rg203_18', 3)	# 61-63

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        WhiffCancel('Oiuchi')
    sprite('rg032_00', 3)	# 1-3
    sprite('rg032_01', 4)	# 4-7
    sprite('rg032_02', 4)	# 8-11
    Unknown8009(0)
    physicsXImpulse(30000)
    Unknown1047(50000)
    sprite('rg032_03', 4)	# 12-15
    WhiffCancelEnable(1)
    sprite('rg032_04', 4)	# 16-19
    sprite('rg032_05', 4)	# 20-23
    sprite('rg032_10', 3)	# 24-26
    WhiffCancelEnable(0)
    Unknown1019(50)
    sprite('rg032_11', 3)	# 27-29

@State
def Oiuchi():

    def upon_IMMEDIATE():
        Unknown17011('OiuchiExe', 1, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(400000)
        Unknown11002(-1)
        Unknown11025(0)
        Unknown11045(0)
        Unknown11046(1)
        Unknown30061(0)
        DisableAttackRestOfMove()
    sprite('rg330_00', 4)	# 1-4
    sprite('rg330_01', 3)	# 5-7
    sprite('rg330_02', 3)	# 8-10	 **attackbox here**
    sprite('rg330_02', 8)	# 11-18	 **attackbox here**
    RefreshMultihit()
    sprite('rg330_02', 5)	# 19-23	 **attackbox here**
    Recovery()
    sprite('rg330_03', 3)	# 24-26
    sprite('rg330_04', 3)	# 27-29

@State
def OiuchiExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown1084(1)
        AttackLevel_(5)
        PushbackX(19800)
        Hitstop(18)
        MinimumDamagePct(0)
        Unknown11068(0)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirUntechableTime(60)
        AirPushbackX(36000)
        AirPushbackY(2000)
        Unknown9202(10)
        JumpCancel_(1)
    sprite('rg330_03', 3)	# 1-3
    Unknown5000(18, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown5003(1)
    sprite('rg330_04', 3)	# 4-6
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_05', 3)	# 7-9
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_06', 3)	# 10-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_07', 10)	# 13-22
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_08', 3)	# 23-25
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_09', 3)	# 26-28
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_10', 6)	# 29-34
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_11', 2)	# 35-36
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg330_12', 8)	# 37-44	 **attackbox here**
    Unknown7007('6272673130385f300000000000000000640000006272673130385f310000000000000000640000006272673130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg330_13', 4)	# 45-48
    sprite('rg330_14', 4)	# 49-52
    sprite('rg330_15', 4)	# 53-56
    sprite('rg330_16', 4)	# 57-60
    sprite('rg330_17', 4)	# 61-64
    sprite('rg330_18', 4)	# 65-68

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('rg231_00', 2)	# 1-2
    sprite('rg231_01', 1)	# 3-3
    sprite('rg231_01', 1)	# 4-4
    Unknown7009(0)
    SFX_0('003_swing_grap_0_2')
    sprite('rg231_02', 1)	# 5-5
    sprite('rg231_03', 1)	# 6-6
    sprite('rg231_04', 2)	# 7-8	 **attackbox here**
    sprite('rg231_05', 3)	# 9-11
    Recovery()
    Unknown2063()
    sprite('rg231_06', 3)	# 12-14
    sprite('rg231_07', 2)	# 15-16
    sprite('rg231_08', 2)	# 17-18
    sprite('rg231_09', 2)	# 19-20

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(9)
        AirUntechableTime(26)
        Unknown2004(1, 0)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rg213_00', 3)	# 1-3
    sprite('rg213_01', 3)	# 4-6
    Unknown7009(2)
    sprite('rg213_02', 3)	# 7-9
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000000000000')
    Unknown1051(125)
    sprite('rg213_03', 3)	# 10-12
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    sprite('rg213_04', 2)	# 13-14
    sprite('rg213_05', 2)	# 15-16
    teleportRelativeX(50000)
    physicsYImpulse(18000)
    physicsXImpulse(5000)
    Unknown1043()
    sendToLabelUpon(2, 1)
    sprite('rg213_06', 2)	# 17-18
    GFX_0('rgef213atk', -1)
    sprite('rg213_07', 2)	# 19-20
    sprite('rg213_08', 3)	# 21-23	 **attackbox here**
    setInvincible(0)
    sprite('rg213_09', 2)	# 24-25
    Recovery()
    Unknown2063()
    sprite('rg213_10', 2)	# 26-27
    sprite('rg213_11', 2)	# 28-29
    sprite('rg213_12', 2)	# 30-31
    sprite('rg213_13', 2)	# 32-33
    sprite('rg213_14', 30)	# 34-63
    label(1)
    sprite('rg213_15', 3)	# 64-66
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rg213_16', 3)	# 67-69
    Unknown18009(0)
    sprite('rg213_17', 3)	# 70-72
    sprite('rg213_18', 3)	# 73-75
    sprite('rg213_19', 4)	# 76-79

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(5)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9016(1)
        HitLow(2)
        AirPushbackX(4500)
        AirPushbackY(17000)
        AirUntechableTime(30)
    sprite('rg233_00', 2)	# 1-2
    sprite('rg233_01', 2)	# 3-4
    sprite('rg233_02', 3)	# 5-7
    SFX_0('019_cloth_a')
    GFX_0('rgef233atk', -1)
    Unknown7007('6272673130375f300000000000000000640000006272673130375f310000000000000000640000006272673130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg233_03', 3)	# 8-10
    sprite('rg233_04', 6)	# 11-16
    SFX_0('006_swing_blade_2')
    sprite('rg233_05', 1)	# 17-17	 **attackbox here**
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    ScreenShake(0, 5000)
    SFX_0('209_down_normal_0')
    sprite('rg233_06', 1)	# 18-18	 **attackbox here**
    sprite('rg233_07', 8)	# 19-26
    Recovery()
    Unknown2063()
    sprite('rg233_08', 4)	# 27-30
    sprite('rg233_09', 3)	# 31-33
    sprite('rg233_10', 3)	# 34-36
    sprite('rg233_11', 2)	# 37-38
    sprite('rg233_12', 3)	# 39-41

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rg252_00', 2)	# 1-2
    sprite('rg252_01', 2)	# 3-4
    sprite('rg252_01', 2)	# 5-6
    sprite('rg252_02', 2)	# 7-8
    SFX_0('008_swing_pole_2')
    Unknown7009(4)
    sprite('rg252_03', 2)	# 9-10
    sprite('rg252_04', 4)	# 11-14	 **attackbox here**
    sprite('rg252_05', 4)	# 15-18
    SFX_0('019_cloth_a')
    Recovery()
    Unknown2063()
    sprite('rg252_06', 4)	# 19-22
    sprite('rg252_07', 4)	# 23-26
    sprite('rg252_08', 4)	# 27-30
    sprite('rg252_09', 4)	# 31-34
    sprite('rg252_10', 4)	# 35-38
    sprite('rg252_11', 4)	# 39-42
    sprite('rg252_12', 4)	# 43-46

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        AirPushbackX(8000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rg321_13', 2)	# 1-2
    sprite('rg321_12', 2)	# 3-4
    sprite('rg321_11', 2)	# 5-6
    SFX_0('004_swing_grap_1_1')
    sprite('rg321_10', 2)	# 7-8
    sprite('rg321_09', 2)	# 9-10
    sprite('rg321_05', 6)	# 11-16	 **attackbox here**
    sprite('rg321_06', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('rg321_07', 3)	# 20-22
    sprite('rg321_08', 3)	# 23-25
    sprite('rg321_09', 3)	# 26-28
    sprite('rg321_10', 3)	# 29-31
    sprite('rg321_11', 3)	# 32-34
    sprite('rg321_12', 3)	# 35-37
    sprite('rg321_13', 3)	# 38-40

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        AirUntechableTime(22)
        AirPushbackX(8000)
        AirPushbackY(28000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rg253_00', 2)	# 1-2
    sprite('rg253_01', 2)	# 3-4
    Unknown7009(5)
    sprite('rg253_02', 3)	# 5-7
    GFX_0('rgef253atk', -1)
    sprite('rg253_03', 3)	# 8-10
    SFX_3('rgse_03')
    SFX_0('008_swing_pole_2')
    sprite('rg253_04', 2)	# 11-12	 **attackbox here**
    sprite('rg253_04', 2)	# 13-14	 **attackbox here**
    sprite('rg253_05', 2)	# 15-16
    Recovery()
    Unknown2063()
    sprite('rg253_06', 2)	# 17-18
    sprite('rg253_07', 2)	# 19-20
    sprite('rg253_08', 3)	# 21-23
    sprite('rg253_09', 3)	# 24-26
    sprite('rg253_10', 3)	# 27-29
    sprite('rg253_11', 3)	# 30-32
    sprite('rg253_12', 2)	# 33-34

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(800)
        AirHitstunAnimation(10)
        AirUntechableTime(25)
        PushbackX(15000)
        Unknown9016(1)
        AirPushbackX(26000)
        AirPushbackY(-60000)
        YImpluseBeforeWallbounce(0)
        HitOverhead(0)
        JumpCancel_(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        DisableAttackRestOfMove()
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            Unknown1028(1900)
            setGravity(3800)
    sprite('rg411_00', 2)	# 1-2
    physicsXImpulse(9500)
    physicsYImpulse(25000)
    sprite('rg411_01', 2)	# 3-4
    Unknown1019(80)
    YAccel(80)
    sprite('rg411_02', 2)	# 5-6	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    SFX_0('019_cloth_b')
    sprite('rg411_03', 6)	# 7-12
    Unknown1019(80)
    YAccel(80)
    sprite('rg411_04', 2)	# 13-14	 **attackbox here**
    Unknown7007('6272673230385f300000000000000000640000006272673230385f310000000000000000640000006272673230385f320000000000000000640000000000000000000000000000000000000000000000')
    RefreshMultihit()
    SFX_3('rgse_24')
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    GFX_1('rgef00', 3)
    Unknown1084(1)
    sprite('rg411_04', 2)	# 15-16	 **attackbox here**
    Unknown3029(1)
    physicsXImpulse(27550)
    physicsYImpulse(-55100)
    loopRest()
    AttackLevel_(4)
    Hitstop(2)
    Unknown11001(-1, -1, -1)
    label(0)
    sprite('rg411_05', 2)	# 17-18	 **attackbox here**
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    RefreshMultihit()
    sprite('rg411_06', 1)	# 19-19	 **attackbox here**
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    GFX_1('rgef02', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    Unknown3029(0)
    sprite('rg411_07', 1)	# 20-20
    GFX_1('rgef00', 0)
    sprite('rg411_08', 1)	# 21-21	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    AirPushbackX(2000)
    AirPushbackY(20000)
    YImpluseBeforeWallbounce(2000)
    AirUntechableTime(35)
    Hitstop(3)
    Unknown11001(0, 0, 5)
    Unknown11025(1)

    def upon_11():
        JumpCancel_(1)
    sprite('rg411_08', 3)	# 22-24	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('rg411_09', 5)	# 25-29
    sprite('rg411_10', 5)	# 30-34
    sprite('rg411_11', 5)	# 35-39
    sprite('rg411_12', 5)	# 40-44

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('rg413_00', 2)	# 1-2
    sprite('rg413_01', 1)	# 3-3
    sprite('rg413_01', 1)	# 4-4
    tag_voice(1, 'brg156_0', 'brg156_1', '', '')
    sprite('rg413_02', 2)	# 5-6
    Unknown4047(224, 224, 224)
    Unknown4045('726765665f3431335f68656e73696e303100000000000000000000000000000000000000')
    sprite('rg413_03', 3)	# 7-9
    sprite('rg413_04', 3)	# 10-12
    sprite('rg413_05', 3)	# 13-15
    sprite('rg413_06', 3)	# 16-18
    sprite('rg413_07', 3)	# 19-21
    SFX_3('rgse_22')
    sprite('rg413_08', 3)	# 22-24	 **attackbox here**
    sprite('rg413_09', 4)	# 25-28
    sprite('rg413_10', 4)	# 29-32
    sprite('rg413_11', 4)	# 33-36
    sprite('rg413_12', 4)	# 37-40
    sprite('rg413_13', 3)	# 41-43
    sprite('rg413_14', 3)	# 44-46
    sprite('rg413_15', 2)	# 47-48

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
    sprite('rg413_08', 2)	# 2-3	 **attackbox here**
    sprite('rg413_09', 2)	# 4-5
    sprite('rg413_10', 2)	# 6-7
    sprite('rg413_11', 2)	# 8-9
    sprite('rg413_12', 2)	# 10-11
    sprite('rg413_13', 2)	# 12-13
    sprite('rg413_14', 1)	# 14-14
    sprite('rg413_15', 1)	# 15-15
    sprite('rg201_00', 1)	# 16-16
    sprite('rg201_01', 1)	# 17-17
    sprite('rg201_02', 2)	# 18-19
    sprite('rg201_03', 2)	# 20-21
    sprite('rg201_04', 2)	# 22-23
    tag_voice(1, 'brg157_0', 'brg157_1', '', '')
    sprite('rg201_05', 2)	# 24-25
    sprite('rg201_06', 2)	# 26-27
    sprite('rg201_07', 2)	# 28-29
    sprite('rg201_08', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    sprite('rg201_09', 2)	# 32-33	 **attackbox here**
    sprite('rg201_10', 4)	# 34-37
    sprite('rg201_11', 3)	# 38-40
    sprite('rg201_12', 3)	# 41-43
    sprite('rg201_13', 3)	# 44-46
    sprite('rg201_14', 3)	# 47-49
    sprite('rg201_15', 3)	# 50-52
    sprite('rg001_00', 7)	# 53-59
    sprite('rg001_01', 7)	# 60-66
    sprite('rg001_02', 7)	# 67-73
    sprite('rg001_03', 7)	# 74-80
    sprite('rg001_04', 7)	# 81-87
    sprite('rg001_05', 7)	# 88-94
    sprite('rg001_06', 7)	# 95-101
    sprite('rg001_07', 7)	# 102-108
    sprite('rg001_08', 6)	# 109-114
    sprite('rg001_09', 6)	# 115-120
    sprite('rg001_10', 6)	# 121-126
    sprite('rg001_11', 6)	# 127-132
    sprite('rg001_12', 6)	# 133-138
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 139-144
    sprite('rg001_14', 6)	# 145-150
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 151-156
    sprite('rg001_16', 6)	# 157-162
    label(0)
    sprite('rg000_00', 7)	# 163-169
    sprite('rg000_01', 7)	# 170-176
    sprite('rg000_02', 7)	# 177-183
    sprite('rg000_03', 7)	# 184-190
    sprite('rg000_04', 7)	# 191-197
    sprite('rg000_05', 7)	# 198-204
    sprite('rg000_06', 7)	# 205-211
    sprite('rg000_05', 7)	# 212-218
    sprite('rg000_04', 7)	# 219-225
    sprite('rg000_03', 7)	# 226-232
    sprite('rg000_02', 7)	# 233-239
    sprite('rg000_01', 7)	# 240-246
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 247-247

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('rg213_00', 1)	# 1-1
    sprite('rg213_01', 1)	# 2-2
    sprite('rg213_02', 1)	# 3-3
    sprite('rg213_03', 2)	# 4-5
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    sprite('rg213_04', 3)	# 6-8
    sprite('rg213_05', 2)	# 9-10
    teleportRelativeX(50000)
    physicsYImpulse(15000)
    Unknown1043()
    sendToLabelUpon(2, 9)
    sprite('rg213_06', 2)	# 11-12
    GFX_0('rgef213atk', -1)
    sprite('rg213_07', 2)	# 13-14
    sprite('rg213_08', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('rg213_09', 2)	# 18-19
    sprite('rg213_10', 2)	# 20-21
    sprite('rg213_11', 2)	# 22-23
    sprite('rg213_12', 2)	# 24-25
    sprite('rg213_13', 2)	# 26-27
    sprite('rg213_14', 32767)	# 28-32794
    label(9)
    sprite('rg213_15', 2)	# 32795-32796
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rg213_16', 2)	# 32797-32798
    sprite('rg213_17', 2)	# 32799-32800
    sprite('rg213_18', 2)	# 32801-32802
    sprite('rg213_19', 2)	# 32803-32804
    sprite('rg001_00', 7)	# 32805-32811
    sprite('rg001_01', 7)	# 32812-32818
    sprite('rg001_02', 7)	# 32819-32825
    sprite('rg001_03', 7)	# 32826-32832
    sprite('rg001_04', 7)	# 32833-32839
    sprite('rg001_05', 7)	# 32840-32846
    sprite('rg001_06', 7)	# 32847-32853
    sprite('rg001_07', 7)	# 32854-32860
    sprite('rg001_08', 6)	# 32861-32866
    sprite('rg001_09', 6)	# 32867-32872
    sprite('rg001_10', 6)	# 32873-32878
    sprite('rg001_11', 6)	# 32879-32884
    sprite('rg001_12', 6)	# 32885-32890
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 32891-32896
    sprite('rg001_14', 6)	# 32897-32902
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 32903-32908
    sprite('rg001_16', 6)	# 32909-32914
    label(0)
    sprite('rg000_00', 7)	# 32915-32921
    sprite('rg000_01', 7)	# 32922-32928
    sprite('rg000_02', 7)	# 32929-32935
    sprite('rg000_03', 7)	# 32936-32942
    sprite('rg000_04', 7)	# 32943-32949
    sprite('rg000_05', 7)	# 32950-32956
    sprite('rg000_06', 7)	# 32957-32963
    sprite('rg000_05', 7)	# 32964-32970
    sprite('rg000_04', 7)	# 32971-32977
    sprite('rg000_03', 7)	# 32978-32984
    sprite('rg000_02', 7)	# 32985-32991
    sprite('rg000_01', 7)	# 32992-32998
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 32999-32999

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('rg440_02', 3)	# 1-3
    sprite('rg440_03', 3)	# 4-6
    teleportRelativeX(-30000)
    sprite('rg440_04', 3)	# 7-9
    teleportRelativeX(-30000)
    sprite('rg440_05', 2)	# 10-11
    tag_voice(0, 'brg158_0', 'brg158_1', '', '')
    GFX_0('rgef440StartEff', -1)
    sprite('rg440_06', 2)	# 12-13
    sprite('rg440_07', 2)	# 14-15
    SFX_3('rgse_26')
    sprite('rg440_08', 2)	# 16-17
    sprite('rg440_09', 2)	# 18-19
    sprite('rg440_10', 4)	# 20-23	 **attackbox here**
    GFX_0('rgef440', -1)
    sprite('rg440_11', 4)	# 24-27
    sprite('rg440_12', 15)	# 28-42
    sprite('rg440_13', 6)	# 43-48
    sprite('rg440_14', 6)	# 49-54
    sprite('rg440_15', 6)	# 55-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('rg000_00', 7)	# 1-7
    sprite('rg000_01', 7)	# 8-14
    sprite('rg000_02', 7)	# 15-21
    sprite('rg000_03', 7)	# 22-28
    sprite('rg000_04', 7)	# 29-35
    sprite('rg000_05', 7)	# 36-42
    sprite('rg000_06', 7)	# 43-49
    sprite('rg000_05', 7)	# 50-56
    sprite('rg000_04', 7)	# 57-63
    sprite('rg000_03', 7)	# 64-70
    sprite('rg000_02', 7)	# 71-77
    sprite('rg000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg440_02', 3)	# 85-87
    sprite('rg440_03', 3)	# 88-90
    teleportRelativeX(-30000)
    sprite('rg440_04', 3)	# 91-93
    teleportRelativeX(-30000)
    sprite('rg440_05', 2)	# 94-95
    tag_voice(0, 'brg158_0', 'brg158_1', '', '')
    GFX_0('rgef440StartEff', -1)
    sprite('rg440_06', 2)	# 96-97
    sprite('rg440_07', 2)	# 98-99
    SFX_3('rgse_26')
    sprite('rg440_08', 2)	# 100-101
    sprite('rg440_09', 2)	# 102-103
    sprite('rg440_10', 4)	# 104-107	 **attackbox here**
    GFX_0('rgef440', -1)
    sprite('rg440_11', 4)	# 108-111
    sprite('rg440_12', 15)	# 112-126
    sprite('rg440_13', 6)	# 127-132
    sprite('rg440_14', 6)	# 133-138
    sprite('rg440_15', 6)	# 139-144

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown30081('')
    sprite('rg450_03', 2)	# 26-27
    Unknown1086(22)
    teleportRelativeX(-1000000)
    SLOT_12 = SLOT_19
    Unknown1019(7)
    sprite('rg450_04', 2)	# 28-29
    Unknown8006(100, 1, 0)
    sprite('rg450_03', 2)	# 30-31
    Unknown8006(100, 1, 0)
    sprite('rg450_04', 2)	# 32-33
    Unknown8006(100, 1, 0)
    sprite('rg450_03', 2)	# 34-35
    Unknown8006(100, 1, 0)
    sprite('rg450_05', 3)	# 36-38
    Unknown1019(10)
    sprite('rg450_06', 3)	# 39-41
    SFX_0('011_spin_0')
    SFX_0('010_swing_sword_2')
    SFX_0('016_explode_1')
    Unknown1019(30)
    Unknown8010(100, 1, 0)
    sprite('rg450_07', 2)	# 42-43	 **attackbox here**
    GFX_0('rgef450', -1)
    Unknown1084(1)
    sprite('rg450_08', 3)	# 44-46
    sprite('rg450_09', 3)	# 47-49
    SFX_3('rgse_05')
    sprite('rg450_13', 3)	# 50-52
    sprite('rg450_14', 3)	# 53-55
    sprite('rg450_15', 3)	# 56-58
    sprite('rg450_16', 3)	# 59-61
    sprite('rg000_00', 7)	# 62-68
    sprite('rg000_01', 7)	# 69-75
    sprite('rg000_02', 7)	# 76-82
    sprite('rg000_03', 7)	# 83-89
    sprite('rg000_04', 7)	# 90-96
    sprite('rg000_05', 7)	# 97-103
    sprite('rg000_06', 7)	# 104-110
    sprite('rg000_05', 7)	# 111-117
    sprite('rg000_04', 7)	# 118-124
    sprite('rg000_03', 7)	# 125-131
    sprite('rg000_02', 7)	# 132-138
    sprite('rg000_01', 7)	# 139-145

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('rg440_00', 2)	# 1-2
    sprite('rg440_01', 3)	# 3-5
    sprite('rg203_08ex01', 3)	# 6-8
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    sprite('rg203_09ex01', 3)	# 9-11
    sprite('rg203_10ex02', 3)	# 12-14	 **attackbox here**
    sprite('rg203_11ex01', 3)	# 15-17
    sprite('rg203_12ex01', 3)	# 18-20
    sprite('rg203_13ex01', 3)	# 21-23
    sprite('rg203_14ex01', 3)	# 24-26
    sprite('rg203_15ex01', 3)	# 27-29
    sprite('rg203_16ex01', 3)	# 30-32
    sprite('rg203_17ex01', 3)	# 33-35
    sprite('rg203_18ex01', 3)	# 36-38
    sprite('rg000_00', 7)	# 39-45
    sprite('rg000_01', 7)	# 46-52
    sprite('rg000_02', 7)	# 53-59
    sprite('rg000_03', 7)	# 60-66
    sprite('rg000_04', 7)	# 67-73
    sprite('rg000_05', 7)	# 74-80
    sprite('rg000_06', 7)	# 81-87
    sprite('rg000_05', 7)	# 88-94
    sprite('rg000_04', 7)	# 95-101
    sprite('rg000_03', 7)	# 102-108
    sprite('rg000_02', 7)	# 109-115
    sprite('rg000_01', 7)	# 116-122

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('rg440_02', 3)	# 1-3
    sprite('rg440_03', 3)	# 4-6
    teleportRelativeX(-30000)
    sprite('rg440_04', 3)	# 7-9
    teleportRelativeX(-30000)
    sprite('rg440_05', 2)	# 10-11
    GFX_0('rgef440StartEff', -1)
    sprite('rg440_06', 2)	# 12-13
    sprite('rg440_07', 2)	# 14-15
    SFX_3('rgse_26')
    sprite('rg440_08', 2)	# 16-17
    sprite('rg440_09', 2)	# 18-19
    sprite('rg440_10', 4)	# 20-23	 **attackbox here**
    GFX_0('rgef440', -1)
    sprite('rg440_11', 4)	# 24-27
    sprite('rg440_12', 15)	# 28-42
    sprite('rg440_13', 6)	# 43-48
    sprite('rg440_14', 6)	# 49-54
    sprite('rg440_15', 6)	# 55-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('rg000_00', 7)	# 1-7
    sprite('rg000_01', 7)	# 8-14
    sprite('rg000_02', 7)	# 15-21
    sprite('rg000_03', 7)	# 22-28
    sprite('rg000_04', 7)	# 29-35
    sprite('rg000_05', 7)	# 36-42
    sprite('rg000_06', 7)	# 43-49
    sprite('rg000_05', 7)	# 50-56
    sprite('rg000_04', 7)	# 57-63
    sprite('rg000_03', 7)	# 64-70
    sprite('rg000_02', 7)	# 71-77
    sprite('rg000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg440_02', 3)	# 85-87
    sprite('rg440_03', 3)	# 88-90
    teleportRelativeX(-30000)
    sprite('rg440_04', 3)	# 91-93
    teleportRelativeX(-30000)
    sprite('rg440_05', 2)	# 94-95
    GFX_0('rgef440StartEff', -1)
    sprite('rg440_06', 2)	# 96-97
    sprite('rg440_07', 2)	# 98-99
    SFX_3('rgse_26')
    sprite('rg440_08', 2)	# 100-101
    sprite('rg440_09', 2)	# 102-103
    sprite('rg440_10', 4)	# 104-107	 **attackbox here**
    GFX_0('rgef440', -1)
    sprite('rg440_11', 4)	# 108-111
    sprite('rg440_12', 15)	# 112-126
    sprite('rg440_13', 6)	# 127-132
    sprite('rg440_14', 6)	# 133-138
    sprite('rg440_15', 6)	# 139-144

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
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
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rg032_11', 3)	# 1-3
    sprite('rg032_00', 4)	# 4-7
    sprite('rg032_01', 4)	# 8-11
    label(0)
    sprite('rg032_02', 4)	# 12-15
    sprite('rg032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 20-23
    sprite('rg032_04', 4)	# 24-27
    sprite('rg032_05', 4)	# 28-31
    sprite('rg032_06', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('rg032_06add', 4)	# 36-39
    sprite('rg032_07', 4)	# 40-43
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg310_00', 1)	# 44-44
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rg310_01', 2)	# 45-46
    SFX_0('010_swing_sword_0')
    sprite('rg310_02', 3)	# 47-49	 **attackbox here**
    Unknown1084(1)
    sprite('rg310_03', 12)	# 50-61
    SFX_4('brg154')
    sprite('rg310_02', 4)	# 62-65	 **attackbox here**
    StartMultihit()
    sprite('rg310_01', 4)	# 66-69
    sprite('rg310_00', 3)	# 70-72

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(40000)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown11001(0, 8, 13)
    sprite('rg310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rg311_00', 3)	# 4-6
    SFX_1('brg153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_01', 4)	# 7-10
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_02', 4)	# 11-14
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_03', 5)	# 15-19
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_04', 5)	# 20-24
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_05', 6)	# 25-30
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_06', 6)	# 31-36
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_07', 20)	# 37-56
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_08', 3)	# 57-59	 **attackbox here**
    GFX_0('ThrowMazzle', 1)
    SFX_0('016_explode_1')
    SFX_3('rgse_06')
    Unknown8004(100, 1, 1)
    sprite('rg311_09', 6)	# 60-65
    sprite('rg311_11', 3)	# 66-68
    SFX_3('rgse_05')
    sprite('rg311_12', 3)	# 69-71
    sprite('rg311_13', 3)	# 72-74
    sprite('rg311_14', 3)	# 75-77
    sprite('rg311_15', 3)	# 78-80
    sprite('rg311_16', 3)	# 81-83
    sprite('rg311_17', 3)	# 84-86
    sprite('rg311_18', 3)	# 87-89
    sprite('rg311_19', 3)	# 90-92
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
    sprite('rg032_11', 3)	# 1-3
    sprite('rg032_00', 4)	# 4-7
    sprite('rg032_01', 4)	# 8-11
    label(0)
    sprite('rg032_02', 4)	# 12-15
    sprite('rg032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 20-23
    sprite('rg032_04', 4)	# 24-27
    sprite('rg032_05', 4)	# 28-31
    sprite('rg032_06', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('rg032_06add', 4)	# 36-39
    sprite('rg032_07', 4)	# 40-43
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg310_00', 1)	# 44-44
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rg310_01', 2)	# 45-46
    SFX_0('010_swing_sword_0')
    sprite('rg310_02', 3)	# 47-49	 **attackbox here**
    Unknown1084(1)
    sprite('rg310_03', 12)	# 50-61
    SFX_4('brg154')
    sprite('rg310_02', 4)	# 62-65	 **attackbox here**
    StartMultihit()
    sprite('rg310_01', 4)	# 66-69
    sprite('rg310_00', 3)	# 70-72

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(45000)
        Unknown11099(1)
        Hitstop(0)
        AirUntechableTime(60)
        Unknown13021(1)
        Unknown21005(1)
    sprite('rg310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rg311_00', 3)	# 4-6
    SFX_1('brg153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_01', 4)	# 7-10
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg311_02', 4)	# 11-14
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_00', 3)	# 15-17
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_01', 3)	# 18-20
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_02', 3)	# 21-23
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_1('ef_hitmd', 0)
    SFX_0('100_hit_grap_0')
    Unknown8004(100, 1, 1)
    sprite('rg313_03', 3)	# 24-26
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_04', 6)	# 27-32
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_05', 3)	# 33-35
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_06', 3)	# 36-38
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_07', 3)	# 39-41
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('rg313_08', 3)	# 42-44
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    sprite('rg313_09', 1)	# 45-45	 **attackbox here**
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg313_09', 12)	# 46-57	 **attackbox here**
    SFX_0('100_hit_grap_3')
    sprite('rg313_10', 6)	# 58-63
    sprite('rg313_11', 4)	# 64-67
    sprite('rg313_12', 4)	# 68-71
    sprite('rg313_13', 4)	# 72-75
    sprite('rg313_14', 4)	# 76-79

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('rg408_00', 2)	# 1-2
    sprite('rg408_01', 2)	# 3-4
    sprite('rg408_02', 2)	# 5-6
    Unknown7007('6272673230375f300000000000000000640000006272673230375f310000000000000000640000006272673230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg408_03', 2)	# 7-8
    sprite('rg408_04', 2)	# 9-10
    sprite('rg408_05', 1)	# 11-11
    sprite('rg408_06', 1)	# 12-12
    sprite('rg408_07', 1)	# 13-13
    sprite('rg408_08', 2)	# 14-15
    GFX_0('rgef408Shot', -1)
    SFX_3('rgse_06')
    sprite('rg408_09', 6)	# 16-21
    sprite('rg408_10', 5)	# 22-26
    SFX_3('rgse_21')
    sprite('rg408_11', 5)	# 27-31
    Recovery()
    sprite('rg408_12', 5)	# 32-36
    sprite('rg408_13', 2)	# 37-38
    sprite('rg408_14', 2)	# 39-40
    sprite('rg408_15', 2)	# 41-42
    sprite('rg408_16', 2)	# 43-44
    sprite('rg408_17', 2)	# 45-46
    sprite('rg408_18', 2)	# 47-48
    sprite('rg408_19', 2)	# 49-50
    sprite('rg408_20', 1)	# 51-51

@State
def ShortDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
    sprite('rg032_00', 3)	# 1-3
    sprite('rg032_01', 3)	# 4-6
    sprite('rg032_02', 4)	# 7-10
    Unknown8009(0)
    physicsXImpulse(30000)
    Unknown1047(50000)
    sprite('rg032_03', 4)	# 11-14
    sprite('rg032_04', 4)	# 15-18
    sprite('rg032_10', 4)	# 19-22
    Unknown1019(50)
    sprite('rg032_11', 4)	# 23-26
    Unknown1019(10)

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('rg408_00', 2)	# 1-2
    sprite('rg408_01', 2)	# 3-4
    sprite('rg408_02', 2)	# 5-6
    Unknown7007('6272673230375f300000000000000000640000006272673230375f310000000000000000640000006272673230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg408_03', 3)	# 7-9
    sprite('rg408_04', 3)	# 10-12
    sprite('rg408_05', 3)	# 13-15
    Unknown14070('ShortDash')
    sprite('rg408_06', 2)	# 16-17
    sprite('rg408_07', 2)	# 18-19
    sprite('rg408_08', 2)	# 20-21
    GFX_0('408_dog', -1)
    SFX_3('rgse_06')
    sprite('rg408_09', 6)	# 22-27
    sprite('rg408_10', 5)	# 28-32
    SFX_3('rgse_21')
    sprite('rg408_11', 5)	# 33-37
    Recovery()
    Unknown14072('ShortDash')
    sprite('rg408_12', 5)	# 38-42
    sprite('rg408_13', 2)	# 43-44
    sprite('rg408_14', 2)	# 45-46
    sprite('rg408_15', 2)	# 47-48
    sprite('rg408_16', 2)	# 49-50
    sprite('rg408_17', 2)	# 51-52
    Unknown14074('ShortDash')
    sprite('rg408_18', 2)	# 53-54
    sprite('rg408_19', 2)	# 55-56
    sprite('rg408_20', 1)	# 57-57

@State
def ShotC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('rg408_00', 2)	# 1-2
    sprite('rg408_01', 2)	# 3-4
    sprite('rg408_02', 2)	# 5-6
    Unknown7007('6272673230375f300000000000000000640000006272673230375f310000000000000000640000006272673230375f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('rg408_03', 2)	# 7-8
    sprite('rg408_04', 2)	# 9-10
    sprite('rg408_05', 1)	# 11-11
    sprite('rg408_06', 1)	# 12-12
    sprite('rg408_07', 1)	# 13-13
    sprite('rg408_08', 2)	# 14-15
    GFX_0('rgef408Shotsp', -1)
    SFX_3('rgse_06')
    sprite('rg408_09', 6)	# 16-21
    sprite('rg408_10', 5)	# 22-26
    SFX_3('rgse_21')
    Unknown14070('ShotC_2nd')
    sprite('rg408_11', 5)	# 27-31
    Recovery()
    sprite('rg408_12', 5)	# 32-36
    Unknown14072('ShotC_2nd')
    sprite('rg408_13', 2)	# 37-38
    sprite('rg408_14', 2)	# 39-40
    Unknown14074('ShotC_2nd')
    sprite('rg408_15', 2)	# 41-42
    sprite('rg408_16', 2)	# 43-44
    sprite('rg408_17', 2)	# 45-46
    sprite('rg408_18', 2)	# 47-48
    sprite('rg408_19', 2)	# 49-50
    sprite('rg408_20', 1)	# 51-51

@State
def ShotC_2nd():

    def upon_IMMEDIATE():
        Unknown1017()
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('rg401_00', 2)	# 1-2
    sprite('rg401_01', 2)	# 3-4
    sprite('rg401_02', 2)	# 5-6
    sprite('rg401_03', 2)	# 7-8
    sprite('rg401_04', 2)	# 9-10
    Unknown14070('ShotC_3rd')
    sprite('rg401_05', 2)	# 11-12
    GFX_0('rgef401atk2nd', -1)
    sprite('rg401_06', 2)	# 13-14
    sprite('rg401_07', 2)	# 15-16
    sprite('rg401_08', 2)	# 17-18
    SFX_0('hit_m_fast')
    SFX_0('hit_m_middle')
    SFX_3('rgse_20')
    SFX_3('rgse_20')
    sprite('rg401_09', 3)	# 19-21	 **attackbox here**
    StartMultihit()
    sprite('rg401_10', 4)	# 22-25
    sprite('rg401_11', 4)	# 26-29
    sprite('rg401_12', 12)	# 30-41
    sprite('rg401_13', 4)	# 42-45
    sprite('rg401_14', 4)	# 46-49
    Unknown14072('ShotC_3rd')
    sprite('rg401_15', 3)	# 50-52
    sprite('rg401_16', 3)	# 53-55
    Unknown14073('ShotC_3rd')
    Recovery()
    sprite('rg401_17', 3)	# 56-58
    sprite('rg401_18', 3)	# 59-61

@State
def ShotC_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(4200)
        AttackP1(50)
        AttackP2(100)
        Unknown30065(0)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(40000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Hitstop(20)
        ChipDamagePct(0)
        MinimumDamagePct(10)
        Unknown11068(1)
        Unknown11001(0, 8, 13)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('rg440_04', 3)	# 1-3
    sprite('rg440_05', 3)	# 4-6
    Unknown2004(1, 0)
    GFX_0('rgef440StartEff', -1)
    sprite('rg440_06', 3)	# 7-9
    sprite('rg440_07', 3)	# 10-12
    SFX_3('rgse_26')
    sprite('rg440_08', 3)	# 13-15
    sprite('rg440_09', 2)	# 16-17
    Unknown7007('6272673230345f300000000000000000640000006272673230345f310000000000000000640000006272673230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg440_10ex00', 6)	# 18-23	 **attackbox here**
    GFX_0('rgef440', -1)
    SFX_0('025_cleanhit_slash')
    sprite('rg440_11', 2)	# 24-25
    Recovery()
    sprite('rg440_12', 2)	# 26-27
    sprite('rg440_13', 2)	# 28-29
    sprite('rg440_14', 2)	# 30-31
    sprite('rg440_15', 2)	# 32-33
    sprite('rg601_15ex01', 3)	# 34-36
    sprite('rg601_16ex01', 3)	# 37-39
    sprite('rg601_17ex01', 4)	# 40-43
    sprite('rg601_18ex01', 4)	# 44-47
    sprite('rg601_19ex01', 3)	# 48-50
    sprite('rg601_20ex01', 4)	# 51-54
    sprite('rg601_21ex01', 4)	# 55-58
    sprite('rg601_22ex01', 4)	# 59-62
    sprite('rg601_23ex01', 4)	# 63-66

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        Damage(1000)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(42)
        AirPushbackY(40000)
        AirPushbackX(8000)
        Unknown11001(0, 0, 0)
        Unknown9015(1)
        Unknown11097(150, 150)
        Unknown1084(1)
        sendToLabelUpon(2, 1)
    sprite('rg402_00', 1)	# 1-1
    tag_voice(1, 'brg202_0', 'brg202_1', 'brg202_2', '')
    physicsXImpulse(24000)
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    sprite('rg402_01', 1)	# 2-2
    sprite('rg402_02', 1)	# 3-3
    sprite('rg402_03', 2)	# 4-5
    SFX_0('006_swing_blade_2')
    SFX_0('011_spin_0')
    Unknown1019(50)
    sprite('rg402_04', 2)	# 6-7
    sprite('rg402_05', 2)	# 8-9
    sprite('rg402_06', 1)	# 10-10	 **attackbox here**
    GFX_0('rgef402atk', -1)
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    physicsXImpulse(0)
    sprite('rg402_07', 1)	# 11-11	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('011_spin_0')
    sprite('rg402_08', 1)	# 12-12	 **attackbox here**
    Unknown8001(3, 100)
    sprite('rg402_09', 2)	# 13-14	 **attackbox here**
    physicsYImpulse(40000)
    physicsXImpulse(6000)
    setGravity(2100)
    sprite('rg402_10', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    Unknown9015(0)
    Unknown9016(1)

    def upon_78():
        HitCancel('AntiAir2nd')
    sprite('rg402_11', 2)	# 17-18	 **attackbox here**
    setInvincible(0)
    sprite('rg402_12', 2)	# 19-20	 **attackbox here**
    sprite('rg402_13', 2)	# 21-22	 **attackbox here**
    sprite('rg402_14', 3)	# 23-25
    setGravity(2400)
    sprite('rg402_15', 3)	# 26-28
    sprite('rg402_16', 3)	# 29-31
    sprite('rg402_17', 3)	# 32-34
    sprite('rg402_18', 3)	# 35-37
    Unknown14086('416e7469416972326e6400000000000000000000000000000000000000000000')
    sprite('rg402_19', 3)	# 38-40
    sprite('rg402_20', 3)	# 41-43
    sprite('rg402_21', 3)	# 44-46
    sprite('rg020_05', 3)	# 47-49
    sprite('rg020_06', 3)	# 50-52
    label(0)
    sprite('rg020_07', 4)	# 53-56
    sprite('rg020_08', 4)	# 57-60
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg024_00', 4)	# 61-64
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rg024_01', 4)	# 65-68
    sprite('rg024_02', 5)	# 69-73
    sprite('rg024_03', 3)	# 74-76
    sprite('rg024_04', 3)	# 77-79

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        Damage(1000)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(42)
        AirPushbackY(40000)
        AirPushbackX(8000)
        Unknown11001(0, 0, 0)
        Unknown9015(1)
        Unknown11097(150, 150)
        Unknown13024(0)
        Unknown13045(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('rg402_00', 1)	# 1-1
    Unknown1051(70)
    tag_voice(1, 'brg202_0', 'brg202_1', 'brg202_2', '')
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    sprite('rg402_01', 1)	# 2-2
    sprite('rg402_02', 1)	# 3-3
    sprite('rg402_03', 1)	# 4-4
    SFX_0('006_swing_blade_2')
    SFX_0('011_spin_0')
    sprite('rg402_04', 1)	# 5-5
    sprite('rg402_05', 1)	# 6-6
    sprite('rg402_06', 1)	# 7-7	 **attackbox here**
    GFX_0('rgef402atk', -1)
    sprite('rg402_07', 1)	# 8-8	 **attackbox here**
    sprite('rg402_08', 1)	# 9-9	 **attackbox here**
    sprite('rg402_09', 2)	# 10-11	 **attackbox here**
    physicsYImpulse(40000)
    physicsXImpulse(6000)
    setGravity(2100)
    sprite('rg402_10', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    Unknown9015(0)
    Unknown9016(1)

    def upon_78():
        HitCancel('AntiAir2nd')
    sprite('rg402_11', 2)	# 14-15	 **attackbox here**
    setInvincible(0)
    sprite('rg402_12', 2)	# 16-17	 **attackbox here**
    sprite('rg402_13', 2)	# 18-19	 **attackbox here**
    sprite('rg402_14', 3)	# 20-22
    sprite('rg402_15', 3)	# 23-25
    sprite('rg402_16', 3)	# 26-28
    sprite('rg402_17', 3)	# 29-31
    sprite('rg402_18', 3)	# 32-34
    Unknown14086('416e7469416972326e6400000000000000000000000000000000000000000000')
    sprite('rg402_19', 3)	# 35-37
    sprite('rg402_20', 3)	# 38-40
    sprite('rg402_21', 3)	# 41-43
    sprite('rg020_05', 3)	# 44-46
    sprite('rg020_06', 3)	# 47-49
    label(0)
    sprite('rg020_07', 4)	# 50-53
    sprite('rg020_08', 4)	# 54-57
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg024_00', 4)	# 58-61
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rg024_01', 4)	# 62-65
    sprite('rg024_02', 5)	# 66-70
    sprite('rg024_03', 3)	# 71-73
    sprite('rg024_04', 3)	# 74-76

@State
def AntiAir2nd():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        AttackLevel_(4)
        Damage(1000)
        AttackP1(48)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(11000)
        YImpluseBeforeWallbounce(1200)
        AirUntechableTime(42)
        Unknown9015(1)
        Unknown30068(1)

        def upon_78():
            HitCancel('AntiAir3rdTate')
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('rg403_00', 3)	# 1-3
    setGravity(900)
    physicsYImpulse(26000)
    physicsXImpulse(12000)
    Unknown1051(60)
    sprite('rg403_01', 3)	# 4-6
    sprite('rg403_02', 3)	# 7-9
    sprite('rg403_03', 2)	# 10-11
    sprite('rg403_04', 1)	# 12-12
    sprite('rg403_05', 1)	# 13-13
    SFX_0('004_swing_grap_1_1')
    sprite('rg403_06', 3)	# 14-16	 **attackbox here**
    sprite('rg403_07', 4)	# 17-20
    Recovery()
    sprite('rg403_08', 5)	# 21-25
    setGravity(1400)
    sprite('rg403_09', 3)	# 26-28
    Unknown14077(0)
    sprite('rg403_10', 3)	# 29-31
    setGravity(1600)
    sprite('rg403_11', 3)	# 32-34
    setGravity(1800)
    sprite('rg020_05', 3)	# 35-37
    setGravity(2000)
    sprite('rg020_06', 3)	# 38-40
    setGravity(2200)
    label(0)
    sprite('rg020_07', 4)	# 41-44
    sprite('rg020_08', 4)	# 45-48
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg024_00', 4)	# 49-52
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rg024_01', 4)	# 53-56
    sprite('rg024_02', 5)	# 57-61
    sprite('rg024_03', 3)	# 62-64
    sprite('rg024_04', 3)	# 65-67

@State
def AntiAir3rdTate():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        AttackP1(48)
        AttackP2(100)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(-64000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)
        Unknown9015(1)
        Unknown11097(150, 150)
        Unknown30068(1)
        Unknown22004(4, 1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('rg404_00', 4)	# 1-4
    physicsXImpulse(5000)
    physicsYImpulse(22000)
    setGravity(900)
    sprite('rg404_01', 4)	# 5-8
    sprite('rg404_02', 4)	# 9-12
    tag_voice(0, 'brg203_0', 'brg203_1', 'brg203_2', '')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000003000000')
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    sprite('rg404_03', 3)	# 13-15
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000003000000')
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    sprite('rg404_04', 3)	# 16-18
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000003000000')
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    SFX_0('004_swing_grap_1_2')
    sprite('rg404_06', 2)	# 19-20	 **attackbox here**
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000003000000')
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    sprite('rg404_06', 2)	# 21-22	 **attackbox here**
    setGravity(2200)
    sprite('rg404_07', 2)	# 23-24	 **attackbox here**
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000003000000')
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    sprite('rg404_08', 5)	# 25-29
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000003000000')
    GFX_0('rgef_drains', 0)
    GFX_0('rgef_drains', 1)
    GFX_0('rgef_drains', 2)
    GFX_0('rgef_drains', 3)
    Recovery()
    Unknown1019(90)
    sprite('rg404_09', 6)	# 30-35
    Unknown1019(90)
    sprite('rg404_10', 3)	# 36-38
    sprite('rg020_05', 3)	# 39-41
    sprite('rg020_06', 3)	# 42-44
    label(0)
    sprite('rg020_07', 4)	# 45-48
    sprite('rg020_08', 4)	# 49-52
    loopRest()
    gotoLabel(0)

@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(4)
        AttackP1(80)
        blockstun(22)
        hitstun(27)
        AirUntechableTime(40)
        AirPushbackX(16000)
        AirPushbackY(20000)
        PushbackX(18000)
        sendToLabelUpon(10, 0)

        def upon_CLEAR_OR_EXIT():
            (SLOT_19 < 300000)
            if op(5, 2, 0, 2, 51):
                sendToLabel(0)
    sprite('rg400_00', 2)	# 1-2
    sprite('rg400_01', 2)	# 3-4
    sprite('rg400_02', 5)	# 5-9
    tag_voice(1, 'brg200_0', 'brg200_1', 'brg200_2', '')
    GFX_0('rgef400nokori', -1)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    sprite('rg400_03', 2)	# 10-11
    sprite('rg400_04', 3)	# 12-14
    GFX_0('rgef400loop', -1)
    Unknown38(4, 1)
    physicsXImpulse(40000)
    Unknown8006(100, 1, 0)
    Unknown14070('Assault2nd')
    sprite('rg400_05', 2)	# 15-16	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 3)	# 17-19	 **attackbox here**
    Unknown2015(250)
    Unknown8006(100, 1, 0)
    sprite('rg400_07', 2)	# 20-21	 **attackbox here**
    SLOT_51 = 1
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 2)	# 22-23	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_07', 2)	# 24-25	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 2)	# 26-27	 **attackbox here**
    Unknown8006(100, 1, 0)
    label(0)
    sprite('rg400_08', 2)	# 28-29
    clearUponHandler(3)
    clearUponHandler(10)
    Unknown13(4)
    Unknown2015(-1)
    GFX_0('rgef400end', -1)
    Unknown1019(70)
    Unknown1028(-1000)
    Unknown14072('Assault2nd')
    Recovery()
    sprite('rg400_09', 2)	# 30-31
    sprite('rg400_10', 2)	# 32-33
    Unknown8006(100, 1, 0)
    sprite('rg400_11', 2)	# 34-35
    Unknown8006(100, 1, 0)
    sprite('rg400_12', 2)	# 36-37
    Unknown8006(100, 1, 0)
    sprite('rg400_13', 2)	# 38-39
    Unknown8006(100, 1, 0)
    sprite('rg400_14', 4)	# 40-43
    sprite('rg400_15', 2)	# 44-45
    SFX_0('208_brake_normal')
    sprite('rg400_16', 2)	# 46-47
    SFX_0('208_brake_normal')
    Unknown14074('Assault2nd')
    Unknown1028(0)
    physicsXImpulse(0)
    sprite('rg400_17', 2)	# 48-49
    sprite('rg400_18', 2)	# 50-51
    sprite('rg400_19', 2)	# 52-53

@State
def Assault2nd():

    def upon_IMMEDIATE():
        Unknown1017()
        AttackDefaults_StandingSpecial()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(56)
        AirPushbackX(22000)
        Unknown9015(1)
        PushbackX(12000)
        Unknown11097(600, 600)
        Unknown30068(1)
    sprite('rg401_00', 2)	# 1-2
    Unknown1018()
    Unknown1019(70)
    sprite('rg401_01', 3)	# 3-5
    sprite('rg401_02', 3)	# 6-8
    Unknown1019(70)
    sprite('rg401_03', 3)	# 9-11
    sprite('rg401_04', 2)	# 12-13
    Unknown1019(70)
    sprite('rg401_05', 2)	# 14-15
    Unknown1019(0)
    GFX_0('rgef401atk', -1)
    sprite('rg401_06', 1)	# 16-16
    sprite('rg401_07', 1)	# 17-17
    tag_voice(0, 'brg201_0', 'brg201_1', 'brg201_2', '')
    sprite('rg401_08', 1)	# 18-18
    SFX_0('004_swing_grap_1_0')
    SFX_0('004_swing_grap_1_1')
    SFX_3('rgse_20')
    SFX_3('rgse_20')
    sprite('rg401_09', 3)	# 19-21	 **attackbox here**
    sprite('rg401_10', 4)	# 22-25
    Recovery()
    sprite('rg401_11', 4)	# 26-29
    sprite('rg401_12', 9)	# 30-38
    sprite('rg401_13', 3)	# 39-41
    sprite('rg401_14', 3)	# 42-44
    sprite('rg401_15', 3)	# 45-47
    sprite('rg401_16', 3)	# 48-50
    sprite('rg401_17', 3)	# 51-53
    sprite('rg401_18', 3)	# 54-56

@State
def MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(4)
        AttackP1(80)
        GroundedHitstunAnimation(2)
        AirUntechableTime(28)
        AirPushbackX(15000)
        AirPushbackY(15000)
        PushbackX(19800)
        HitOverhead(2)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
        sendToLabelUpon(2, 1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1019(50)
    sprite('rg406_00', 3)	# 1-3
    sprite('rg406_01', 2)	# 4-5
    tag_voice(1, 'brg205_0', 'brg205_1', 'brg205_2', '')
    sprite('rg406_02', 2)	# 6-7
    Unknown14070('MidAssault2nd')
    sprite('rg406_03', 2)	# 8-9
    sprite('rg406_04', 6)	# 10-15
    physicsXImpulse(20000)
    physicsYImpulse(21500)
    setGravity(1700)
    Unknown8001(3, 100)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(-90000)
    Unknown35()
    sprite('rg406_05', 2)	# 16-17
    Unknown23087(20000)
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(-60000)
    Unknown35()
    sprite('rg406_06', 2)	# 18-19	 **attackbox here**
    Unknown23087(30000)
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(-30000)
    Unknown35()
    sprite('rg406_07', 2)	# 20-21	 **attackbox here**
    Unknown23087(50000)
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(30000)
    Unknown35()
    sprite('rg406_08', 3)	# 22-24	 **attackbox here**
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown3001(255)
    Unknown3004(-20)
    Unknown1096(1000)
    Unknown1099(-50)
    Unknown1072(60000)
    Unknown35()
    sprite('rg406_09', 3)	# 25-27
    Recovery()
    sprite('rg406_10', 3)	# 28-30
    Unknown23087(30000)
    Unknown14072('MidAssault2nd')
    sprite('rg406_15', 3)	# 31-33
    Unknown23087(20000)
    sprite('rg406_16', 32767)	# 34-32800
    Unknown23087(0)
    label(1)
    sprite('rg406_17', 4)	# 32801-32804
    Unknown14074('MidAssault2nd')
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('rg406_18', 4)	# 32805-32808
    sprite('rg406_19', 3)	# 32809-32811
    sprite('rg406_20', 3)	# 32812-32814

@State
def Air_MidAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(28)
        AirPushbackX(15000)
        AirPushbackY(15000)
        PushbackX(19800)
        HitOverhead(2)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
        Unknown1084(0)
        sendToLabelUpon(2, 1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1019(50)
            YAccel(50)
        if SLOT_136:
            Unknown10000(80)
    sprite('rg406_04', 8)	# 1-8
    physicsXImpulse(20000)
    physicsYImpulse(21500)
    setGravity(1700)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(-90000)
    Unknown35()
    sprite('rg406_05', 3)	# 9-11
    tag_voice(1, 'brg205_0', 'brg205_1', 'brg205_2', '')
    Unknown23087(20000)
    Unknown14070('MidAssault2nd')
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(-60000)
    Unknown35()
    sprite('rg406_06', 3)	# 12-14	 **attackbox here**
    Unknown23087(30000)
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(-30000)
    Unknown35()
    sprite('rg406_07', 3)	# 15-17	 **attackbox here**
    Unknown23087(50000)
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown1072(30000)
    Unknown35()
    sprite('rg406_08', 3)	# 18-20	 **attackbox here**
    GFX_0('rgef406atk', 0)
    Unknown36(1)
    Unknown3001(255)
    Unknown3004(-20)
    Unknown1096(1000)
    Unknown1099(-50)
    Unknown1072(60000)
    Unknown35()
    sprite('rg406_09', 3)	# 21-23
    Recovery()
    sprite('rg406_10', 3)	# 24-26
    Unknown23087(30000)
    Unknown14072('MidAssault2nd')
    sprite('rg406_15', 3)	# 27-29
    Unknown23087(20000)
    sprite('rg406_16', 32767)	# 30-32796
    Unknown23087(0)
    label(1)
    sprite('rg406_17', 3)	# 32797-32799
    Unknown14074('MidAssault2nd')
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('rg406_18', 5)	# 32800-32804
    sprite('rg406_19', 4)	# 32805-32808
    sprite('rg406_20', 3)	# 32809-32811

@State
def MidAssault2nd():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(75)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(18000)
        AirPushbackY(40000)
        Unknown11001(0, 2, 7)
        AirUntechableTime(45)
        Unknown11061(1)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        Unknown30068(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('rg406_10', 2)	# 1-2
    if SLOT_58:
        GFX_0('rgef406batkD', 0)
    else:
        GFX_0('rgef406batk', 0)
    physicsXImpulse(14000)
    physicsYImpulse(10000)
    setGravity(1200)
    sprite('rg406_11', 6)	# 3-8
    SFX_0('005_swing_grap_2_0')
    SFX_0('005_swing_grap_2_2')
    SFX_3('rgse_01')
    sprite('rg406_12', 4)	# 9-12	 **attackbox here**
    tag_voice(0, 'brg206_0', 'brg206_1', 'brg206_2', '')
    sprite('rg406_13', 3)	# 13-15
    Recovery()
    sprite('rg406_14', 3)	# 16-18
    sprite('rg406_15', 3)	# 19-21
    sprite('rg406_16', 32767)	# 22-32788
    label(1)
    sprite('rg406_17', 5)	# 32789-32793
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    HitOrBlockJumpCancel(0)
    sprite('rg406_18', 5)	# 32794-32798
    sprite('rg406_19', 4)	# 32799-32802
    sprite('rg406_20', 4)	# 32803-32806

@State
def AirAssault():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(-60000)
        AirUntechableTime(60)
        Unknown9310(20)
        PushbackX(12000)
        Unknown9016(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown11001(0, -1, 2)
    sprite('rg414_00', 4)	# 1-4
    Unknown1084(1)
    physicsXImpulse(6000)
    physicsYImpulse(18000)
    Unknown1043()
    sprite('rg414_01', 4)	# 5-8
    tag_voice(1, 'brg210_0', 'brg210_1', 'brg210_2', '')
    sprite('rg414_02', 4)	# 9-12
    SFX_0('019_cloth_b')
    sprite('rg414_03', 4)	# 13-16
    SFX_3('rgse_24')
    sprite('rg414_04', 3)	# 17-19	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(-46000)
    Unknown14070('AirAssault2nd')
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    Unknown3029(1)
    sprite('rg414_05', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    GFX_0('rgef_414_fall', -1)
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    sprite('rg414_06', 2)	# 22-23	 **attackbox here**
    Unknown4048(90000)
    Unknown4049(1500)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000002000000')
    label(0)
    sprite('rg414_05', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000000000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000001000000')
    Unknown4049(1500)
    Unknown4048(90000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    sprite('rg414_06', 2)	# 26-27	 **attackbox here**
    Unknown4048(90000)
    Unknown4049(1500)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    Unknown4048(90000)
    Unknown4045('726765663032000000000000000000000000000000000000000000000000000002000000')
    loopRest()
    gotoLabel(0)
    label(1)
    Unknown26('rgef_414_fall')
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    Unknown3029(0)
    Unknown26('rgef_414_fall')
    Unknown3029(0)
    sprite('rg414_07', 2)	# 28-29	 **attackbox here**
    StartMultihit()
    sprite('rg414_07', 2)	# 30-31	 **attackbox here**
    GFX_0('rgef_414', -1)
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    Unknown9190(0)
    Unknown9118(30)
    Unknown9310(1)
    Hitstop(11)
    Unknown11001(0, -7, 2)
    AirPushbackX(6000)
    sprite('rg414_08', 4)	# 32-35
    Recovery()
    Unknown14072('AirAssault2nd')
    sprite('rg414_09', 4)	# 36-39
    sprite('rg414_10', 3)	# 40-42
    sprite('rg414_11', 3)	# 43-45
    sprite('rg414_12', 3)	# 46-48
    Unknown14074('AirAssault2nd')
    sprite('rg414_13', 3)	# 49-51

@State
def AirAssault2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(1)
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackX(30000)
        AirPushbackY(30000)
        Hitstop(16)
        Unknown11097(600, 600)
        PushbackX(19800)
        Unknown30068(1)
    sprite('rg414_14', 1)	# 1-1
    GFX_0('rgef414atk', -1)
    sprite('rg414_15', 2)	# 2-3
    sprite('rg414_16', 2)	# 4-5
    SFX_3('rgse_06')
    tag_voice(0, 'brg211_0', 'brg211_1', 'brg211_2', '')
    sprite('rg414_17', 2)	# 6-7
    sprite('rg414_18', 2)	# 8-9
    sprite('rg414_19', 1)	# 10-10
    SFX_3('rgse_22')
    SFX_3('rgse_22')
    sprite('rg414_20', 1)	# 11-11
    sprite('rg414_21', 3)	# 12-14	 **attackbox here**
    sprite('rg414_22', 5)	# 15-19
    Recovery()
    SFX_3('rgse_22')
    sprite('rg414_23', 8)	# 20-27
    sprite('rg414_24', 4)	# 28-31
    sprite('rg414_25', 4)	# 32-35
    sprite('rg450_14', 4)	# 36-39
    sprite('rg450_15', 4)	# 40-43
    sprite('rg450_16', 4)	# 44-47

@State
def JumpAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(5)
        Damage(2500)
        AttackP1(80)
        AttackP2(80)
        Unknown30065(0)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(10000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(40)
        AirUntechableTime(60)
        Hitstop(16)
        blockstun(23)
        ChipDamagePct(0)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        MinimumDamagePct(10)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1019(30)

        def upon_LANDING():
            sendToLabel(2)
    sprite('rg412_00', 3)	# 1-3
    sprite('rg412_01', 2)	# 4-5
    Unknown23087(50000)
    physicsXImpulse(28000)
    Unknown1007(50000)
    physicsYImpulse(19600)
    setGravity(1400)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown7007('6272673230395f300000000000000000640000006272673230395f310000000000000000640000006272673230395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg412_02', 2)	# 6-7
    sprite('rg412_03', 2)	# 8-9
    sprite('rg412_04', 2)	# 10-11
    Unknown2015(200)
    sprite('rg412_05', 3)	# 12-14
    sprite('rg412_06', 2)	# 15-16
    GFX_0('rgef412effpos', -1)
    sprite('rg412_07', 2)	# 17-18
    SFX_0('010_swing_sword_2')
    SFX_3('rgse_03')
    sprite('rg412_08', 2)	# 19-20
    sprite('rg412_09ex', 4)	# 21-24	 **attackbox here**
    Unknown2015(-1)
    sprite('rg412_10', 2)	# 25-26
    Unknown1019(50)
    Recovery()
    sprite('rg412_11', 2)	# 27-28
    sprite('rg412_12', 2)	# 29-30
    sprite('rg412_13', 32767)	# 31-32797
    label(2)
    sprite('rg412_14', 4)	# 32798-32801
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown23087(-1)
    sprite('rg024_02', 4)	# 32802-32805
    sprite('rg024_03', 3)	# 32806-32808
    sprite('rg024_04', 3)	# 32809-32811

@State
def AirJumpAssault():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(5)
        Damage(2500)
        AttackP1(80)
        AttackP2(80)
        Unknown30065(0)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(10000)
        AirPushbackY(-80000)
        AirUntechableTime(60)
        Hitstop(16)
        ChipDamagePct(0)
        Unknown9016(1)
        MinimumDamagePct(10)
        Unknown9118(40)
        Unknown9190(1)
        YImpluseBeforeWallbounce(0)
        clearUponHandler(2)

        def upon_LANDING():
            sendToLabel(2)
    sprite('rg412_01', 2)	# 1-2
    physicsXImpulse(22000)
    physicsYImpulse(28000)
    setGravity(2000)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    sprite('rg412_02', 1)	# 3-3
    sprite('rg412_02', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown7007('6272673230395f300000000000000000640000006272673230395f310000000000000000640000006272673230395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rg412_03', 2)	# 5-6
    sprite('rg412_04', 2)	# 7-8
    Unknown2015(200)
    sprite('rg412_05', 4)	# 9-12
    sprite('rg412_06', 2)	# 13-14
    GFX_0('rgef412effpos', -1)
    Unknown1019(90)
    sprite('rg412_07', 2)	# 15-16
    Unknown1019(90)
    SFX_0('010_swing_sword_2')
    SFX_3('rgse_03')
    sprite('rg412_08', 2)	# 17-18
    Unknown1019(90)
    sprite('rg412_09ex', 4)	# 19-22	 **attackbox here**
    Unknown1019(90)
    Unknown2015(-1)
    sprite('rg412_10', 4)	# 23-26
    Unknown1019(50)
    Recovery()
    sprite('rg412_11', 4)	# 27-30
    sprite('rg412_12', 4)	# 31-34
    sprite('rg412_13', 32767)	# 35-32801
    label(2)
    sprite('rg412_14', 3)	# 32802-32804
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('rg024_02', 3)	# 32805-32807
    sprite('rg024_03', 2)	# 32808-32809
    sprite('rg024_04', 2)	# 32810-32811

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(0)
        AttackLevel_(4)
        Damage(3000)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        Unknown9130(60)
        Unknown9142(42)
        PushbackX(12000)
        AirPushbackY(-85000)
        AirPushbackX(12000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(90)
        Unknown9190(1)
        Unknown9118(40)
        Unknown9016(1)
        Unknown11056(0)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1

        def upon_CLEAR_OR_EXIT():
            (SLOT_19 < 600000)
            if op(5, 2, 0, 2, 52):
                SLOT_52 = 0
                sendToLabel(99)
        Unknown2004(1, 0)
        setInvincible(1)
    sprite('rg450_00', 2)	# 1-2
    sprite('rg450_01', 3)	# 3-5
    sprite('rg450_02', 3)	# 6-8
    sprite('rg450_02ex01', 35)	# 9-43
    Unknown2036(42, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'brg250_0', 'brg250_1', '', '')
    Unknown30080('')
    sprite('rg450_03', 3)	# 44-46
    Unknown3029(1)
    physicsXImpulse(30000)
    Unknown1028(12000)
    Unknown8006(100, 1, 0)
    SFX_0('000_airdash_0')
    sprite('rg450_04', 3)	# 47-49
    SLOT_52 = 1
    Unknown8006(100, 1, 0)
    sprite('rg450_03', 3)	# 50-52
    Unknown8006(100, 1, 0)
    sprite('rg450_04', 3)	# 53-55
    Unknown8006(100, 1, 0)
    label(99)
    sprite('rg450_05', 3)	# 56-58
    SLOT_52 = 0
    Unknown1019(30)
    Unknown1028(0)
    sprite('rg450_06', 2)	# 59-60
    SFX_0('011_spin_0')
    SFX_0('010_swing_sword_2')
    SFX_0('016_explode_1')
    Unknown1019(30)
    sprite('rg450_07', 2)	# 61-62	 **attackbox here**
    GFX_0('rgef450', -1)
    Unknown1019(30)
    sprite('rg450_08', 2)	# 63-64
    Unknown1019(30)
    sprite('rg450_09', 3)	# 65-67
    SFX_3('rgse_05')
    Unknown1019(30)
    sprite('rg450_10', 5)	# 68-72
    setInvincible(0)
    Unknown1019(0)
    sprite('rg450_11', 6)	# 73-78
    sprite('rg450_12', 4)	# 79-82
    loopRest()
    if SLOT_51:
        _gotolabel(88)
    sprite('rg450_13', 4)	# 83-86
    sprite('rg450_14', 4)	# 87-90
    sprite('rg450_15', 4)	# 91-94
    sprite('rg450_16', 4)	# 95-98
    loopRest()
    ExitState()
    label(88)
    sprite('rg451_00', 3)	# 99-101
    teleportRelativeX(100000)
    Unknown1019(0)
    sprite('rg451_01', 3)	# 102-104
    Unknown2015(200)
    sprite('rg451_02', 3)	# 105-107
    sprite('rg451_03', 2)	# 108-109
    tag_voice(0, 'brg251_0', 'brg251_1', '', '')
    sprite('rg451_04', 2)	# 110-111
    GFX_0('rgef451atk', -1)
    sprite('rg451_05', 2)	# 112-113
    sprite('rg451_06', 3)	# 114-116
    SFX_3('rgse_23')
    SFX_3('rgse_23')
    sprite('rg451_07', 4)	# 117-120	 **attackbox here**
    RefreshMultihit()
    Unknown11097(300, 300)
    ChipDamagePct(0)
    Damage(5800)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    PushbackX(30400)
    AirPushbackX(60000)
    AirPushbackY(36000)
    Hitstop(6)
    Unknown9190(0)
    YImpluseBeforeWallbounce(1300)
    Unknown11097(1000, 1000)
    MinimumDamagePct(18)
    SFX_0('209_down_normal_0')
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    SFX_0('013_thunder_1')
    SFX_3('rgse_01')
    sprite('rg451_08', 3)	# 121-123
    Unknown2015(-1)
    sprite('rg451_09', 3)	# 124-126
    sprite('rg451_08', 3)	# 127-129
    sprite('rg451_09', 3)	# 130-132
    sprite('rg451_08', 4)	# 133-136
    setInvincible(0)
    sprite('rg451_09', 4)	# 137-140
    sprite('rg451_08', 5)	# 141-145
    sprite('rg451_09', 5)	# 146-150
    sprite('rg451_10', 4)	# 151-154
    sprite('rg451_11', 4)	# 155-158
    sprite('rg451_12', 4)	# 159-162
    sprite('rg451_13', 4)	# 163-166
    sprite('rg451_14', 4)	# 167-170
    sprite('rg451_15', 4)	# 171-174
    sprite('rg451_16', 4)	# 175-178
    SFX_FOOTSTEP_(100, 1, 1)

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(0)
        AttackLevel_(4)
        Damage(3000)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        Unknown9130(60)
        Unknown9142(42)
        PushbackX(12000)
        AirPushbackY(-85000)
        AirPushbackX(12000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(90)
        Unknown9190(1)
        Unknown9118(40)
        Unknown9016(1)
        Unknown11056(0)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1

        def upon_CLEAR_OR_EXIT():
            (SLOT_19 < 600000)
            if op(5, 2, 0, 2, 52):
                SLOT_52 = 0
                sendToLabel(99)
        Unknown2004(1, 0)
        setInvincible(1)
    sprite('rg450_00', 2)	# 1-2
    sprite('rg450_01', 3)	# 3-5
    sprite('rg450_02', 3)	# 6-8
    sprite('rg450_02ex01', 35)	# 9-43
    Unknown2036(42, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'brg250_0', 'brg250_1', '', '')
    Unknown30080('')
    sprite('rg450_03', 3)	# 44-46
    Unknown3029(1)
    physicsXImpulse(30000)
    Unknown1028(12000)
    Unknown8006(100, 1, 0)
    SFX_0('000_airdash_0')
    sprite('rg450_04', 3)	# 47-49
    SLOT_52 = 1
    Unknown8006(100, 1, 0)
    sprite('rg450_03', 3)	# 50-52
    Unknown8006(100, 1, 0)
    sprite('rg450_04', 3)	# 53-55
    Unknown8006(100, 1, 0)
    label(99)
    sprite('rg450_05', 3)	# 56-58
    SLOT_52 = 0
    Unknown1019(30)
    Unknown1028(0)
    sprite('rg450_06', 2)	# 59-60
    SFX_0('011_spin_0')
    SFX_0('010_swing_sword_2')
    SFX_0('016_explode_1')
    Unknown1019(30)
    sprite('rg450_07', 2)	# 61-62	 **attackbox here**
    GFX_0('rgef450', -1)
    Unknown1019(30)
    sprite('rg450_08', 2)	# 63-64
    Unknown1019(30)
    sprite('rg450_09', 3)	# 65-67
    SFX_3('rgse_05')
    Unknown1019(30)
    sprite('rg450_10', 5)	# 68-72
    setInvincible(0)
    Unknown1019(0)
    sprite('rg450_11', 6)	# 73-78
    sprite('rg450_12', 4)	# 79-82
    loopRest()
    if SLOT_51:
        _gotolabel(88)
    sprite('rg450_13', 4)	# 83-86
    setInvincible(0)
    sprite('rg450_14', 4)	# 87-90
    sprite('rg450_15', 4)	# 91-94
    sprite('rg450_16', 4)	# 95-98
    loopRest()
    ExitState()
    label(88)
    sprite('rg451_00', 3)	# 99-101
    teleportRelativeX(100000)
    Unknown1019(0)
    sprite('rg451_01', 3)	# 102-104
    Unknown2015(200)
    sprite('rg451_02', 3)	# 105-107
    sprite('rg451_03', 2)	# 108-109
    tag_voice(0, 'brg251_0', 'brg251_1', '', '')
    sprite('rg451_04', 2)	# 110-111
    GFX_0('rgef451atkOD', -1)
    sprite('rg451_05', 2)	# 112-113
    sprite('rg451_06', 3)	# 114-116
    SFX_3('rgse_23')
    SFX_3('rgse_23')
    sprite('rg451_07', 4)	# 117-120	 **attackbox here**
    RefreshMultihit()
    Unknown11097(300, 300)
    ChipDamagePct(0)
    Damage(5600)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    PushbackX(30400)
    AirPushbackX(60000)
    AirPushbackY(36000)
    Hitstop(6)
    Unknown9190(0)
    YImpluseBeforeWallbounce(1300)
    Unknown11097(800, 800)
    MinimumDamagePct(15)
    SFX_0('209_down_normal_0')
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    SFX_0('013_thunder_1')
    SFX_3('rgse_01')
    sprite('rg451_07', 1)	# 121-121	 **attackbox here**
    RefreshMultihit()
    Unknown11097(300, 300)
    Damage(700)
    Hitstop(5)
    sprite('rg451_07', 1)	# 122-122	 **attackbox here**
    RefreshMultihit()
    sprite('rg451_07', 1)	# 123-123	 **attackbox here**
    RefreshMultihit()
    sprite('rg451_07', 1)	# 124-124	 **attackbox here**
    RefreshMultihit()
    sprite('rg451_08', 3)	# 125-127
    Unknown2015(-1)
    sprite('rg451_09', 3)	# 128-130
    sprite('rg451_08', 3)	# 131-133
    sprite('rg451_09', 3)	# 134-136
    sprite('rg451_08', 4)	# 137-140
    setInvincible(0)
    sprite('rg451_09', 4)	# 141-144
    sprite('rg451_08', 5)	# 145-149
    sprite('rg451_09', 5)	# 150-154
    sprite('rg451_10', 4)	# 155-158
    sprite('rg451_11', 4)	# 159-162
    sprite('rg451_12', 4)	# 163-166
    sprite('rg451_13', 4)	# 167-170
    sprite('rg451_14', 4)	# 171-174
    sprite('rg451_15', 4)	# 175-178
    sprite('rg451_16', 4)	# 179-182
    SFX_FOOTSTEP_(100, 1, 1)

@State
def BloodWeaponFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(35)
        Unknown9142(60)
        Unknown9310(12)
        PushbackX(100)
        Unknown11072(1, 300000, 0)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11032('801a060050c30000801a0600ffffffff')
        Unknown11062(1)
        Hitstop(10)
        Unknown11068(1)
        setInvincible(1)
        Unknown2004(1, 0)
        Unknown11067(1)
        Unknown11069('BloodWeaponFinish2nd')

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
            enterState('BloodWeaponFinish2nd')
            EnableCollision(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_52:
                SLOT_51 = (SLOT_51 + 1)
                if (SLOT_51 == 5):
                    SLOT_51 = 0
                    ScreenShake(1000, 8000)
    sprite('rg432_00', 4)	# 1-4
    SFX_3('rgse_04')
    sprite('rg432_01', 4)	# 5-8
    sprite('rg432_02', 4)	# 9-12
    sprite('rg432_03', 5)	# 13-17
    Unknown2036(30, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    tag_voice(1, 'brg253_0', 'brg253_1', '', '')
    SFX_0('019_quake_0')
    SLOT_52 = 1
    Unknown30080('')
    sprite('rg432_03', 5)	# 18-22
    sprite('rg432_03', 5)	# 23-27
    sprite('rg432_03', 5)	# 28-32
    SFX_0('019_quake_0')
    sprite('rg432_03', 5)	# 33-37
    sprite('rg432_03', 5)	# 38-42
    sprite('rg432_03', 4)	# 43-46
    sprite('rg432_04', 4)	# 47-50
    SLOT_52 = 0
    SFX_3('rgse_22')
    SFX_3('rgse_22')
    sprite('rg432_04ex01', 4)	# 51-54
    sprite('rg432_05', 3)	# 55-57	 **attackbox here**
    sprite('rg432_23', 5)	# 58-62
    GFX_0('rgef432lock', 1)
    teleportRelativeX(-130000)
    setInvincible(0)
    sprite('rg432_24', 5)	# 63-67
    sprite('rg432_25', 5)	# 68-72
    sprite('rg432_26', 5)	# 73-77
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg432_27', 5)	# 78-82
    sprite('rg432_28', 5)	# 83-87
    sprite('rg432_29', 10)	# 88-97
    sprite('rg432_30', 5)	# 98-102
    sprite('rg432_31', 5)	# 103-107
    sprite('rg432_32', 5)	# 108-112

@State
def BloodWeaponFinish2nd():

    def upon_IMMEDIATE():
        Unknown17011('BloodWeaponFinish3rd', 3, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(100)
        setInvincible(1)
        Unknown3029(1)
        Unknown3070(2)
        Unknown3071(5)
        Unknown3074('00000000800000000000000000000000')
        Unknown3075('00000000000000000000000000000000')
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11069('BloodWeaponFinish3rd')
        Unknown11023(1)
        EnableCollision(0)
        Unknown11108('03000000')
    sprite('rg432_05ex01', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown4047(220, 220, 220)
    Unknown4045('726765663433326c6f636b00000000000000000000000000000000000000000001000000')
    GFX_0('rgef432lock', 1)
    sprite('rg432_06', 5)	# 4-8
    sprite('rg432_07', 5)	# 9-13
    sprite('rg432_08', 5)	# 14-18
    SFX_0('022_magiccircle_a')
    sprite('rg432_09', 5)	# 19-23
    sprite('rg432_10', 5)	# 24-28
    Unknown2006()
    sprite('rg432_11', 5)	# 29-33
    sprite('rg432_12', 5)	# 34-38	 **attackbox here**
    sprite('rg432_23', 5)	# 39-43
    sprite('rg432_24', 5)	# 44-48
    sprite('rg432_25', 5)	# 49-53
    sprite('rg432_26', 5)	# 54-58
    sprite('rg432_27', 5)	# 59-63
    sprite('rg432_28', 5)	# 64-68
    sprite('rg432_29', 10)	# 69-78
    sprite('rg432_30', 5)	# 79-83
    sprite('rg432_31', 5)	# 84-88
    sprite('rg432_32', 5)	# 89-93

@State
def BloodWeaponFinish3rd():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(4)
        Damage(6000)
        AttackP2(60)
        MinimumDamagePct(29)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        AirPushbackX(8000)
        AirPushbackY(33333)
        YImpluseBeforeWallbounce(1500)
        Hitstop(14)
        Unknown9016(1)
        StarterRating(0)
        Unknown11002(-1)
        Unknown11097(2000, 2000)
        Unknown11108('03000000')
        Unknown30061(0)
        setInvincible(1)
    sprite('rg432_14', 3)	# 1-3
    GFX_0('rgef432loop', 2)
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg432_15', 3)	# 4-6
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_16', 3)	# 7-9
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 10-12
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_18', 3)	# 13-15
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 16-18
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_20', 3)	# 19-21
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 22-24
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_15', 3)	# 25-27
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_16', 3)	# 28-30
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_17', 3)	# 31-33
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 34-36
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 37-39
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 40-42
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_22', 13)	# 43-55	 **attackbox here**
    SFX_0('101_hit_slash_3')
    SFX_0('103_hit_counter_slash_2')
    RefreshMultihit()
    tag_voice(0, 'brg254_0', 'brg254_1', '', '')
    Unknown4049(3000)
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000000000000')
    Unknown4047(215, 215, 209)
    Unknown4045('72676566343332627265616b000000000000000000000000000000000000000000000000')
    sprite('rg432_23', 5)	# 56-60
    sprite('rg432_24', 5)	# 61-65
    sprite('rg432_25', 5)	# 66-70
    sprite('rg432_26', 5)	# 71-75
    sprite('rg432_27', 5)	# 76-80
    sprite('rg432_28', 5)	# 81-85
    sprite('rg432_29', 10)	# 86-95
    sprite('rg432_30', 5)	# 96-100
    sprite('rg432_31', 5)	# 101-105
    sprite('rg432_32', 5)	# 106-110

@State
def BloodWeaponFinish_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(35)
        Unknown9142(60)
        Unknown9310(12)
        PushbackX(100)
        Unknown11072(1, 300000, 0)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11032('801a060050c30000801a0600ffffffff')
        Unknown11062(1)
        Hitstop(10)
        Unknown11068(1)
        setInvincible(1)
        Unknown2004(1, 0)
        Unknown11067(1)
        Unknown11069('BloodWeaponFinish2nd_OD')

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
            enterState('BloodWeaponFinish2nd_OD')
            EnableCollision(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_52:
                SLOT_51 = (SLOT_51 + 1)
                if (SLOT_51 == 5):
                    SLOT_51 = 0
                    ScreenShake(1000, 8000)
    sprite('rg432_00', 4)	# 1-4
    SFX_3('rgse_04')
    sprite('rg432_01', 4)	# 5-8
    sprite('rg432_02', 4)	# 9-12
    sprite('rg432_03', 5)	# 13-17
    Unknown2036(30, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    tag_voice(1, 'brg253_0', 'brg253_1', '', '')
    SFX_0('019_quake_0')
    SLOT_52 = 1
    Unknown30080('')
    sprite('rg432_03', 5)	# 18-22
    sprite('rg432_03', 5)	# 23-27
    sprite('rg432_03', 5)	# 28-32
    SFX_0('019_quake_0')
    sprite('rg432_03', 5)	# 33-37
    sprite('rg432_03', 5)	# 38-42
    sprite('rg432_03', 4)	# 43-46
    sprite('rg432_04', 4)	# 47-50
    SLOT_52 = 0
    SFX_3('rgse_22')
    SFX_3('rgse_22')
    sprite('rg432_04ex01', 4)	# 51-54
    sprite('rg432_05', 3)	# 55-57	 **attackbox here**
    sprite('rg432_23', 5)	# 58-62
    GFX_0('rgef432lock', 1)
    teleportRelativeX(-130000)
    setInvincible(0)
    sprite('rg432_24', 5)	# 63-67
    sprite('rg432_25', 5)	# 68-72
    sprite('rg432_26', 5)	# 73-77
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg432_27', 5)	# 78-82
    sprite('rg432_28', 5)	# 83-87
    sprite('rg432_29', 10)	# 88-97
    sprite('rg432_30', 5)	# 98-102
    sprite('rg432_31', 5)	# 103-107
    sprite('rg432_32', 5)	# 108-112

@State
def BloodWeaponFinish2nd_OD():

    def upon_IMMEDIATE():
        Unknown17011('BloodWeaponFinish3rd_OD', 3, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(100)
        setInvincible(1)
        Unknown3029(1)
        Unknown3070(2)
        Unknown3071(5)
        Unknown3074('00000000800000000000000000000000')
        Unknown3075('00000000000000000000000000000000')
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown30061(0)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11023(1)
        EnableCollision(0)
        Unknown11108('03000000')
    sprite('rg432_05ex01', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown4047(220, 220, 220)
    Unknown4045('726765663433326c6f636b00000000000000000000000000000000000000000001000000')
    GFX_0('rgef432lock', 1)
    sprite('rg432_06', 5)	# 4-8
    sprite('rg432_07', 5)	# 9-13
    sprite('rg432_08', 5)	# 14-18
    SFX_0('022_magiccircle_a')
    sprite('rg432_09', 5)	# 19-23
    sprite('rg432_10', 5)	# 24-28
    Unknown2006()
    sprite('rg432_11', 5)	# 29-33
    sprite('rg432_12', 5)	# 34-38	 **attackbox here**
    sprite('rg432_23', 5)	# 39-43
    sprite('rg432_24', 5)	# 44-48
    sprite('rg432_25', 5)	# 49-53
    sprite('rg432_26', 5)	# 54-58
    sprite('rg432_27', 5)	# 59-63
    sprite('rg432_28', 5)	# 64-68
    sprite('rg432_29', 10)	# 69-78
    sprite('rg432_30', 5)	# 79-83
    sprite('rg432_31', 5)	# 84-88
    sprite('rg432_32', 5)	# 89-93

@State
def BloodWeaponFinish3rd_OD():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(7500)
        AttackP2(60)
        MinimumDamagePct(26)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        AirPushbackX(8000)
        AirPushbackY(33333)
        YImpluseBeforeWallbounce(1500)
        Hitstop(20)
        Unknown9016(1)
        StarterRating(0)
        Unknown11002(-1)
        Unknown11097(3000, 3000)
        Unknown11108('03000000')
        Unknown30061(0)
        setInvincible(1)
    sprite('rg432_14', 3)	# 1-3
    GFX_0('rgef432loop_SP', 2)
    Unknown4047(211, 210, 209)
    Unknown4045('726765663433325f6e646c303000000000000000000000000000000000000000ffffffff')
    Unknown4047(209, 216, 209)
    Unknown4045('726765663433325f6e646c000000000000000000000000000000000000000000ffffffff')
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rg432_15', 3)	# 4-6
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_16', 3)	# 7-9
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 10-12
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_18', 3)	# 13-15
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 16-18
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_20', 3)	# 19-21
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 22-24
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_15', 3)	# 25-27
    Unknown4047(209, 216, 209)
    Unknown4045('726765663433325f6e646c000000000000000000000000000000000000000000ffffffff')
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_16', 3)	# 28-30
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_17', 3)	# 31-33
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 34-36
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_19', 3)	# 37-39
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_21', 3)	# 40-42
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_15', 3)	# 43-45
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_16', 3)	# 46-48
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 49-51
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 52-54
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_19', 3)	# 55-57
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_20', 3)	# 58-60
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_21', 3)	# 61-63
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_15', 3)	# 64-66
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_16', 3)	# 67-69
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_17', 3)	# 70-72
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_18', 3)	# 73-75
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_19', 3)	# 76-78
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(2)
    sprite('rg432_20', 3)	# 79-81
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    sprite('rg432_21', 3)	# 82-84
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(3)
    sprite('rg432_15', 3)	# 85-87
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_03')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(4)
    sprite('rg432_16', 3)	# 88-90
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(4)
    sprite('rg432_17', 3)	# 91-93
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(5)
    sprite('rg432_18', 3)	# 94-96
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(5)
    sprite('rg432_19', 3)	# 97-99
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_01')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(6)
    sprite('rg432_20', 3)	# 100-102
    SFX_0('101_hit_slash_2')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(6)
    sprite('rg432_21', 3)	# 103-105
    SFX_0('101_hit_slash_2')
    SFX_3('rgse_02')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(7)
    label(0)
    sprite('rg432_22', 13)	# 106-118	 **attackbox here**
    SFX_0('101_hit_slash_3')
    SFX_0('103_hit_counter_slash_2')
    RefreshMultihit()
    tag_voice(0, 'brg254_0', 'brg254_1', '', '')
    Unknown4049(3000)
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000000000000')
    Unknown4047(215, 215, 209)
    Unknown4045('72676566343332627265616b000000000000000000000000000000000000000000000000')
    sprite('rg432_23', 5)	# 119-123
    sprite('rg432_24', 5)	# 124-128
    sprite('rg432_25', 5)	# 129-133
    sprite('rg432_26', 5)	# 134-138
    sprite('rg432_27', 5)	# 139-143
    sprite('rg432_28', 5)	# 144-148
    sprite('rg432_29', 10)	# 149-158
    sprite('rg432_30', 5)	# 159-163
    sprite('rg432_31', 5)	# 164-168
    sprite('rg432_32', 5)	# 169-173

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        sendToLabelUpon(12, 1)
        Unknown11069('AstralHeat')
        AttackLevel_(5)
        Hitstop(60)
        Unknown11064(1)
        Damage(0)
        hitstun(20)
        Unknown9016(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(220)
        Unknown9142(200)
        PushbackX(15000)
        Unknown11001(-6, 0, 0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(4)
        Unknown3074('00000000ff0000000000000080000000')
        Unknown3075('000000008000000000000000ff000000')
        Unknown3076(1010)
        Unknown3077(1100)
        Unknown2004(1, 0)
        Unknown11068(1)
        Unknown11078(1)
        MinimumDamagePct(100)
        setInvincible(1)
    sprite('rg460_00', 2)	# 1-2
    Unknown1084(1)
    sprite('rg460_01', 3)	# 3-5
    Unknown2036(75, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_RG_AH', -1)
    GFX_1('rgef_ASTstart', -1)
    SFX_0('019_quake_0')
    Unknown8000(100, 1, 0)
    tag_voice(1, 'brg290_0', 'brg290_1', '', '')
    sprite('rg460_02', 3)	# 6-8
    sprite('rg460_03', 3)	# 9-11
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 12-14
    sprite('rg460_02', 3)	# 15-17
    sprite('rg460_03', 3)	# 18-20
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 21-23
    sprite('rg460_02', 3)	# 24-26
    sprite('rg460_03', 3)	# 27-29
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 30-32
    sprite('rg460_02', 3)	# 33-35
    sprite('rg460_03', 3)	# 36-38
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 39-41
    sprite('rg460_02', 3)	# 42-44
    sprite('rg460_03', 3)	# 45-47
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 48-50
    sprite('rg460_02', 3)	# 51-53
    sprite('rg460_03', 3)	# 54-56
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 57-59
    sprite('rg460_02', 3)	# 60-62
    sprite('rg460_03', 3)	# 63-65
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 66-68
    sprite('rg460_02', 3)	# 69-71
    sprite('rg460_03', 3)	# 72-74
    SFX_3('rgse_04')
    sprite('rg460_01', 3)	# 75-77
    sprite('rg460_02', 3)	# 78-80
    sprite('rg460_03', 3)	# 81-83
    SFX_3('rgse_04')
    sprite('rg460_04', 2)	# 84-85
    physicsXImpulse(12000)
    sprite('rg460_04', 2)	# 86-87
    Unknown1019(80)
    sprite('rg460_05', 2)	# 88-89
    Unknown1019(80)
    sprite('rg460_05', 2)	# 90-91
    Unknown1019(80)
    sprite('rg460_51ex01', 2)	# 92-93
    Unknown1019(80)
    SFX_0('005_swing_grap_2_2')
    sprite('rg460_06', 2)	# 94-95	 **attackbox here**
    Unknown1019(50)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('rgse_01')
    SFX_3('rgse_04')
    sprite('rg460_07', 2)	# 96-97
    Unknown1019(50)
    setInvincible(0)
    sprite('rg460_07', 5)	# 98-102
    physicsXImpulse(0)
    sprite('rg460_53', 5)	# 103-107
    sprite('rg460_54', 4)	# 108-111
    sprite('rg460_51ex01', 4)	# 112-115
    sprite('rg460_52ex01', 4)	# 116-119
    loopRest()
    ExitState()
    label(1)
    clearUponHandler(12)
    Unknown11097(70, 70)
    Unknown23088(1, 1)
    Unknown23157(1)
    Unknown11067(1)
    EnableCollision(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown20000(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown1028(0)
    physicsXImpulse(0)
    Unknown23084(1)
    sprite('rg460_07', 3)	# 120-122
    Unknown2006()
    sprite('rg460_08', 3)	# 123-125	 **attackbox here**
    sprite('rg460_09', 3)	# 126-128	 **attackbox here**
    sprite('rg460_10', 3)	# 129-131	 **attackbox here**
    sprite('rg460_11', 3)	# 132-134	 **attackbox here**
    sprite('rg460_12', 3)	# 135-137
    GFX_1('rgef_ASTBG', -1)
    GFX_1('rgef_asthandpow', 1)
    GFX_0('ChangeToDeathscythe', 0)
    SFX_0('019_quake_1')
    tag_voice(0, 'brg291_0', 'brg291_1', '', '')
    sprite('rg460_13', 3)	# 138-140
    sprite('rg460_14', 3)	# 141-143
    sprite('rg460_12', 3)	# 144-146
    SFX_0('019_quake_1')
    sprite('rg460_13', 3)	# 147-149
    sprite('rg460_14', 3)	# 150-152
    sprite('rg460_12', 3)	# 153-155
    SFX_0('019_quake_1')
    sprite('rg460_13', 3)	# 156-158
    sprite('rg460_14', 3)	# 159-161
    sprite('rg460_12', 3)	# 162-164
    SFX_0('019_quake_1')
    sprite('rg460_13', 3)	# 165-167
    sprite('rg460_14', 3)	# 168-170
    sprite('rg460_12', 3)	# 171-173
    SFX_0('019_quake_1')
    sprite('rg460_13', 3)	# 174-176
    sprite('rg460_14', 3)	# 177-179
    sprite('rg460_12', 3)	# 180-182
    SFX_0('019_quake_1')
    sprite('rg460_15', 4)	# 183-186
    GFX_1('rgef_astcircle', 0)
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('rg460_16', 4)	# 187-190
    sprite('rg460_17', 4)	# 191-194
    sprite('rg460_18', 4)	# 195-198
    sprite('rg460_19', 4)	# 199-202
    sprite('rg460_20', 6)	# 203-208
    sprite('rg460_21', 4)	# 209-212
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('rg460_22', 1)	# 213-213	 **attackbox here**
    Unknown11023(1)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    Unknown11048(20)
    PushbackX(2500)
    hitstun(300)
    Hitstop(1)
    RefreshMultihit()
    Damage(2100)
    SFX_0('103_hit_counter_slash_1')
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    GFX_1('rgef_astbkburst', 0)
    GFX_1('rgef_astbkburst', 1)
    GFX_1('rgef_astbkburst', 2)
    sprite('rg460_22', 5)	# 214-218	 **attackbox here**
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000065000000')
    sprite('rg460_23', 4)	# 219-222
    sprite('rg460_24', 4)	# 223-226
    sprite('rg460_25', 4)	# 227-230
    sprite('rg460_26', 6)	# 231-236
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('rg460_27', 4)	# 237-240
    SFX_3('rgse_02')
    sprite('rg460_28', 1)	# 241-241	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    GFX_1('rgef_astbkburst', 0)
    GFX_1('rgef_astbkburst', 1)
    GFX_1('rgef_astbkburst', 2)
    sprite('rg460_28', 5)	# 242-246	 **attackbox here**
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000065000000')
    sprite('rg460_29', 4)	# 247-250
    sprite('rg460_30', 4)	# 251-254
    sprite('rg460_31', 4)	# 255-258
    sprite('rg460_32', 4)	# 259-262
    SFX_0('006_swing_blade_2')
    sprite('rg460_33', 4)	# 263-266
    SFX_0('010_swing_sword_2')
    sprite('rg460_34', 1)	# 267-267	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(12000)
    RefreshMultihit()
    ScreenShake(0, 5000)
    SFX_0('103_hit_counter_slash_1')
    SFX_3('rgse_02')
    GFX_1('rgef_astbkburst', 0)
    GFX_1('rgef_astbkburst', 1)
    GFX_1('rgef_astbkburst', 2)
    sprite('rg460_34', 2)	# 268-269	 **attackbox here**
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000065000000')
    sprite('rg460_35', 3)	# 270-272	 **attackbox here**
    GFX_1('rgef_astbkburst', 3)
    GFX_1('rgef_astbkburst', 4)
    GFX_1('rgef_astbkburst', 5)
    sprite('rg460_36', 3)	# 273-275	 **attackbox here**
    GFX_1('rgef_astbkburst', 6)
    GFX_1('rgef_astbkburst', 7)
    tag_voice(0, 'brg292_0', 'brg292_1', '', '')
    sprite('rg460_17', 4)	# 276-279
    sprite('rg460_18', 4)	# 280-283
    sprite('rg460_19', 4)	# 284-287
    sprite('rg460_20', 6)	# 288-293
    sprite('rg460_21', 4)	# 294-297
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('rg460_22', 1)	# 298-298	 **attackbox here**
    Unknown11023(1)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    Unknown11048(20)
    PushbackX(2500)
    hitstun(300)
    Hitstop(1)
    RefreshMultihit()
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    GFX_1('rgef_astbkburst', 0)
    GFX_1('rgef_astbkburst', 1)
    GFX_1('rgef_astbkburst', 2)
    sprite('rg460_22', 5)	# 299-303	 **attackbox here**
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000065000000')
    sprite('rg460_23', 4)	# 304-307
    sprite('rg460_24', 4)	# 308-311
    sprite('rg460_25', 4)	# 312-315
    sprite('rg460_26', 6)	# 316-321
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('rg460_27', 4)	# 322-325
    SFX_0('103_hit_counter_slash_1')
    SFX_3('rgse_02')
    sprite('rg460_28', 1)	# 326-326	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(5000)
    RefreshMultihit()
    GFX_1('rgef_astbkburst', 0)
    GFX_1('rgef_astbkburst', 1)
    GFX_1('rgef_astbkburst', 2)
    sprite('rg460_28', 5)	# 327-331	 **attackbox here**
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000065000000')
    sprite('rg460_29', 4)	# 332-335
    sprite('rg460_30', 4)	# 336-339
    sprite('rg460_31', 4)	# 340-343
    sprite('rg460_32', 4)	# 344-347
    SFX_0('006_swing_blade_2')
    sprite('rg460_33', 4)	# 348-351
    SFX_0('010_swing_sword_2')
    sprite('rg460_34', 1)	# 352-352	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(40000)
    RefreshMultihit()
    ScreenShake(0, 5000)
    SFX_3('rgse_02')
    Unknown3026(-1)
    Unknown3025(-14675952, 10)
    GFX_1('rgef_astbkburst', 0)
    GFX_1('rgef_astbkburst', 1)
    GFX_1('rgef_astbkburst', 2)
    sprite('rg460_34', 2)	# 353-354	 **attackbox here**
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000065000000')
    sprite('rg460_35', 3)	# 355-357	 **attackbox here**
    GFX_1('rgef_astbkburst', 3)
    GFX_1('rgef_astbkburst', 4)
    GFX_1('rgef_astbkburst', 5)
    sprite('rg460_36', 3)	# 358-360	 **attackbox here**
    GFX_1('rgef_astbkburst', 6)
    GFX_1('rgef_astbkburst', 7)
    sprite('rg460_37', 3)	# 361-363	 **attackbox here**
    PushbackX(0)
    Unknown11072(1, 490000, 0)
    Damage(1000)
    RefreshMultihit()
    Unknown4049(500)
    Unknown4045('726765665f41480000000000000000000000000000000000000000000000000007000000')
    GFX_1('rgef_astmc', 0)
    GFX_1('rgef_astbkburst', 0)
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('rg460_37', 2)	# 364-365	 **attackbox here**
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('rg460_38', 1)	# 366-366	 **attackbox here**
    sprite('rg460_38', 3)	# 367-369	 **attackbox here**
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('rg460_39', 3)	# 370-372	 **attackbox here**
    GFX_1('rgef_astmc', 0)
    GFX_1('rgef_astbkburst', 0)
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('rg460_40', 3)	# 373-375	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41', 3)	# 376-378	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41add01', 3)	# 379-381	 **attackbox here**
    Unknown11097(70, 70)
    RefreshMultihit()
    GFX_1('rgef_astlight', 1)
    GFX_1('rgef_astaura', 1)
    GFX_1('rgef_astmc', 0)
    GFX_1('rgef_astbkburst', 0)
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('rg460_41add02', 3)	# 382-384	 **attackbox here**
    Unknown4045('726765665f647261696e6869743031000000000000000000000000000000000065000000')
    GFX_1('ef_hitlz', 101)
    SFX_0('019_quake_0')
    sprite('rg460_41add03', 3)	# 385-387	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41add01', 3)	# 388-390	 **attackbox here**
    RefreshMultihit()
    ScreenShake(0, 8000)
    SFX_0('019_quake_0')
    sprite('rg460_41add02', 3)	# 391-393	 **attackbox here**
    Unknown4045('726765665f647261696e6869743031000000000000000000000000000000000065000000')
    GFX_1('ef_hitlz', 101)
    SFX_0('019_quake_0')
    sprite('rg460_41add03', 3)	# 394-396	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41add01', 3)	# 397-399	 **attackbox here**
    RefreshMultihit()
    GFX_1('rgef_astmc', 0)
    GFX_1('rgef_astbkburst', 0)
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    sprite('rg460_41add02', 3)	# 400-402	 **attackbox here**
    Unknown4045('726765665f647261696e6869743031000000000000000000000000000000000065000000')
    GFX_1('ef_hitlz', 101)
    SFX_0('019_quake_0')
    sprite('rg460_41add03', 3)	# 403-405	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41add01', 3)	# 406-408	 **attackbox here**
    RefreshMultihit()
    ScreenShake(0, 12000)
    SFX_0('019_quake_0')
    sprite('rg460_41add02', 3)	# 409-411	 **attackbox here**
    Unknown4045('726765665f647261696e6869743031000000000000000000000000000000000065000000')
    GFX_1('ef_hitlz', 101)
    SFX_0('019_quake_0')
    sprite('rg460_41add03', 3)	# 412-414	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41add01', 3)	# 415-417	 **attackbox here**
    Unknown11048(0)
    RefreshMultihit()
    GFX_1('rgef_astmc', 0)
    GFX_1('rgef_astbkburst', 0)
    ScreenShake(0, 14000)
    SFX_0('019_quake_0')
    sprite('rg460_41add02', 3)	# 418-420	 **attackbox here**
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000065000000')
    SFX_0('019_quake_0')
    sprite('rg460_41add03', 3)	# 421-423	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41add01', 3)	# 424-426	 **attackbox here**
    RefreshMultihit()
    ScreenShake(0, 16000)
    SFX_0('019_quake_0')
    sprite('rg460_41add02', 3)	# 427-429	 **attackbox here**
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000065000000')
    SFX_0('019_quake_0')
    sprite('rg460_41add03', 3)	# 430-432	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_41add01', 3)	# 433-435	 **attackbox here**
    RefreshMultihit()
    GFX_1('rgef_astmc', 0)
    GFX_1('rgef_astbkburst', 0)
    ScreenShake(0, 20000)
    SFX_0('019_quake_0')
    sprite('rg460_41add02', 3)	# 436-438	 **attackbox here**
    Unknown4045('726765665f647261696e7374617274000000000000000000000000000000000065000000')
    SFX_0('019_quake_0')
    sprite('rg460_41add03', 3)	# 439-441	 **attackbox here**
    SFX_0('019_quake_0')
    sprite('rg460_42', 4)	# 442-445	 **attackbox here**
    GFX_1('rgef_astlock', 2)
    sprite('rg460_43', 4)	# 446-449	 **attackbox here**
    sprite('rg460_44', 4)	# 450-453	 **attackbox here**
    sprite('rg460_45', 4)	# 454-457	 **attackbox here**
    sprite('rg460_46', 4)	# 458-461	 **attackbox here**
    tag_voice(0, 'brg293_0', 'brg293_1', '', '')
    SFX_0('010_swing_sword_2')
    sprite('rg460_47', 1)	# 462-462	 **attackbox here**
    Unknown11097(0, 0)
    Unknown11064(3)
    AirPushbackY(30000)
    AirPushbackX(100000)
    Unknown11072(0, 0, 0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Hitstop(0)
    RefreshMultihit()
    Damage(21400)
    Unknown21013('647261696e5f747375627500000000000000000000000000000000000000000021000000')
    GFX_1('rgef_astenemydel', 0)
    GFX_1('rgef_astfinish', 0)
    GFX_1('rgef_asttodome', 0)
    GFX_1('rgef_asttodomehit', 0)
    SFX_0('015_blaze_2')
    SFX_0('010_swing_sword_2')
    sprite('rg460_47', 1)	# 463-463	 **attackbox here**
    Unknown21013('647261696e5f747375627500000000000000000000000000000000000000000021000000')
    SFX_0('005_swing_grap_2_2')
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('rg460_47', 1)	# 464-464	 **attackbox here**
    SFX_3('rgse_01')
    SFX_3('rgse_02')
    sprite('rg460_47', 1)	# 465-465	 **attackbox here**
    Unknown21013('647261696e5f747375627500000000000000000000000000000000000000000021000000')
    SFX_3('rgse_03')
    SFX_3('rgse_04')
    SFX_3('rgse_04')
    SFX_3('rgse_04')
    sprite('rg460_48', 4)	# 466-469	 **attackbox here**
    Unknown3029(0)
    Unknown3026(-14675952)
    Unknown3025(-1, 20)
    sprite('rg460_49', 4)	# 470-473	 **attackbox here**
    sprite('rg460_47add01', 4)	# 474-477	 **attackbox here**
    sprite('rg460_48', 4)	# 478-481	 **attackbox here**
    sprite('rg460_49', 4)	# 482-485	 **attackbox here**
    sprite('rg460_47add01', 4)	# 486-489	 **attackbox here**
    sprite('rg460_48', 4)	# 490-493	 **attackbox here**
    sprite('rg460_49', 4)	# 494-497	 **attackbox here**
    sprite('rg460_47add01', 4)	# 498-501	 **attackbox here**
    sprite('rg460_48', 4)	# 502-505	 **attackbox here**
    sprite('rg460_49', 4)	# 506-509	 **attackbox here**
    sprite('rg460_47add01', 4)	# 510-513	 **attackbox here**
    sprite('rg460_48', 4)	# 514-517	 **attackbox here**
    sprite('rg460_49', 4)	# 518-521	 **attackbox here**
    sprite('rg460_47add01', 4)	# 522-525	 **attackbox here**
    sprite('rg460_48', 4)	# 526-529	 **attackbox here**
    sprite('rg460_49', 4)	# 530-533	 **attackbox here**
    sprite('rg460_47add01', 4)	# 534-537	 **attackbox here**
    sprite('rg460_48', 4)	# 538-541	 **attackbox here**
    sprite('rg460_49', 4)	# 542-545	 **attackbox here**
    sprite('rg460_47add01', 4)	# 546-549	 **attackbox here**
    sprite('rg460_48', 4)	# 550-553	 **attackbox here**
    sprite('rg460_49', 4)	# 554-557	 **attackbox here**
    sprite('rg460_47add01', 4)	# 558-561	 **attackbox here**
    sprite('rg460_48', 4)	# 562-565	 **attackbox here**
    Unknown1000(260000)
    sprite('rg460_49', 4)	# 566-569	 **attackbox here**
    sprite('rg460_47add01', 4)	# 570-573	 **attackbox here**
    sprite('rg460_48', 4)	# 574-577	 **attackbox here**
    sprite('rg460_49', 4)	# 578-581	 **attackbox here**
    sprite('rg460_47add01', 4)	# 582-585	 **attackbox here**
    sprite('rg460_48', 4)	# 586-589	 **attackbox here**
    sprite('rg460_49', 4)	# 590-593	 **attackbox here**
    sprite('rg460_47add01', 4)	# 594-597	 **attackbox here**
    sprite('rg460_48', 4)	# 598-601	 **attackbox here**
    sprite('rg460_49', 4)	# 602-605	 **attackbox here**
    sprite('rg460_47add01', 4)	# 606-609	 **attackbox here**
    sprite('rg460_48', 4)	# 610-613	 **attackbox here**
    sprite('rg460_49', 4)	# 614-617	 **attackbox here**
    loopRest()
    sprite('rg460_47add01', 4)	# 618-621	 **attackbox here**
    sprite('rg460_48', 4)	# 622-625	 **attackbox here**
    sprite('rg460_49', 4)	# 626-629	 **attackbox here**
    sprite('rg460_47add01', 4)	# 630-633	 **attackbox here**
    sprite('rg460_48', 4)	# 634-637	 **attackbox here**
    sprite('rg460_49', 4)	# 638-641	 **attackbox here**
    sprite('rg460_47add01', 4)	# 642-645	 **attackbox here**
    sprite('rg460_48', 4)	# 646-649	 **attackbox here**
    sprite('rg460_49', 4)	# 650-653	 **attackbox here**
    sprite('rg460_47add01', 4)	# 654-657	 **attackbox here**
    sprite('rg460_48', 4)	# 658-661	 **attackbox here**
    sprite('rg460_49', 4)	# 662-665	 **attackbox here**
    sprite('rg460_50', 6)	# 666-671
    SLOT_61 = 1
    sprite('rg460_51', 5)	# 672-676
    sprite('rg460_52', 5)	# 677-681

@State
def DebugSkill():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown1084(1)
    sprite('rg000_00', 480)	# 1-480
    Unknown1096(15000)
    EnableCollision(0)

@Subroutine
def MouthTableInit():
    Unknown18011('brg000', 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg500', '001')
    Unknown18011('brg501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg501', '002')
    Unknown18011('brg502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg502', '003')
    Unknown18011('brg503', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg503', '004')
    Unknown18011('brg504', 12643, 12641, 25397, 13617, 12641, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 14130, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg504', '005')
    Unknown18011('brg505', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg505', '006')
    Unknown18011('brg520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg520', '007')
    Unknown18011('brg521', 12643, 12641, 25397, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg521', '008')
    Unknown18011('brg522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg522', '009')
    Unknown18011('brg523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg523', '010')
    Unknown18011('brg524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg524', '011')
    Unknown18011('brg525', 12643, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg525', '012')
    Unknown18011('brg402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg403_0', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg403_1', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25393, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601bha', 12643, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601bjb', 12643, 14177, 14179, 14177, 14179, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12594, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601bno', 12643, 12641, 25394, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601bpt', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601brc', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601pag', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601pbc', 12643, 24880, 25396, 24884, 25396, 13363, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg600rbl', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14691, 13665, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg600uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601uor', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg603pbc', 12643, 12643, 14177, 14179, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg605pbc', 12643, 12643, 14177, 13411, 12899, 14177, 14179, 14177, 12643, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg600bce', 12899, 12897, 25392, 24886, 13873, 13411, 12641, 25394, 13364, 14177, 14179, 14177, 13155, 24882, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601', 12643, 14433, 13411, 24884, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601ahe', 12899, 24885, 25399, 24887, 25397, 24885, 12849, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601bnt', 14689, 13923, 24882, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg602bsu', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14386, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg600uak', 13155, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 24886, 25397, 24885, 25397, 24885, 25397, 24885, 25397, 24885, 25397, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg601kym', 13155, 12897, 25394, 12593, 12641, 25396, 12851, 12641, 25392, 12337, 12641, 25392, 13105, 14689, 14691, 14689, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg600rbl', '017')
    Unknown30092('brg600uhy', '018')
    Unknown30092('brg601baz', '019')
    Unknown30092('brg601bha', '020')
    Unknown30092('brg601bjb', '021')
    Unknown30092('brg601bjn', '022')
    Unknown30092('brg601bno', '023')
    Unknown30092('brg601bny', '024')
    Unknown30092('brg601bpt', '025')
    Unknown30092('brg601brc', '026')
    Unknown30092('brg601pag', '027')
    Unknown30092('brg601pbc', '028')
    Unknown30092('brg601rrb', '029')
    Unknown30092('brg601uor', '030')
    Unknown30092('brg603pbc', '031')
    Unknown30092('brg605pbc', '032')
    Unknown30092('brg600bce', '033')
    Unknown30092('brg601', '034')
    Unknown30092('brg601ahe', '035')
    Unknown30092('brg601bnt', '036')
    Unknown30092('brg602bsu', '037')
    Unknown30092('brg600uak', '038')
    Unknown30092('brg601kym', '039')
    Unknown18011('brg701baz', 13667, 13409, 13411, 13409, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701bha', 12643, 13409, 13411, 14177, 14691, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701bjb', 12643, 14177, 14179, 14177, 14179, 12641, 24880, 25399, 24887, 12337, 14179, 14177, 13155, 24880, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg700bjn', 12643, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701bno', 13667, 13409, 13411, 14177, 13411, 24880, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701bpt', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701brc', 12643, 12897, 25393, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701pag', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 13665, 13667, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg700pbc', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 12337, 13155, 24887, 25401, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg700rbl', 13667, 13409, 13411, 13409, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701rrb', 12643, 14177, 14691, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701uhy', 12643, 13409, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 13617, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701uor', 12643, 12641, 25392, 24887, 12337, 14179, 14177, 13411, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701bce', 13155, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg700ahe', 13155, 14177, 13923, 13665, 13667, 14689, 13667, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg702ahe', 12643, 14433, 12899, 24885, 25399, 24886, 25399, 24886, 25399, 24886, 12338, 12899, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701bnt', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg700bsu', 13155, 14177, 14179, 14177, 14179, 14177, 13155, 24885, 25397, 24885, 25397, 24885, 25397, 12849, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg700uak', 12899, 14177, 12899, 24880, 25398, 24886, 25398, 24886, 25398, 13362, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 12643, 24888, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brg701kym', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24881, 25397, 13617, 14689, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('brg700pbc', '041')
    Unknown30092('brg700rbl', '042')
    Unknown30092('brg701baz', '043')
    Unknown30092('brg701bha', '044')
    Unknown30092('brg701bjb', '045')
    Unknown30092('brg701bno', '046')
    Unknown30092('brg701bny', '047')
    Unknown30092('brg701bpt', '048')
    Unknown30092('brg701brc', '049')
    Unknown30092('brg701pag', '050')
    Unknown30092('brg701rrb', '051')
    Unknown30092('brg701uhy', '052')
    Unknown30092('brg701uor', '053')
    Unknown30092('brg701bce', '054')
    Unknown30092('brg700ahe', '055')
    Unknown30092('brg702ahe', '056')
    Unknown30092('brg701bnt', '057')
    Unknown30092('brg700bsu', '058')
    Unknown30092('brg700uak', '059')
    Unknown30092('brg701kym', '060')
    if SLOT_172:
        Unknown18011('brg000', 12643, 12899, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 14179, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg502', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg504', 14177, 14179, 14177, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg505', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg521', 12643, 12641, 25397, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg523', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg525', 12643, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg402_0', 12643, 12643, 14177, 14179, 12641, 25392, 25399, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg402_1', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 14177, 14179, 14689, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg403_0', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg403_1', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25393, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601bha', 12643, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601bjb', 12643, 14177, 14179, 14177, 14179, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601bno', 12643, 12641, 25394, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601bpt', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601pag', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601pbc', 12643, 12643, 14177, 14179, 13921, 13667, 14177, 14179, 14177, 13411, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg600rbl', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14691, 13665, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg600uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 24885, 25399, 24887, 25394, 12849, 14177, 14179, 13665, 12643, 14177, 14179, 14177, 14179, 13921, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg603pbc', 12643, 12643, 14177, 14179, 14433, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg605pbc', 12643, 12643, 14177, 13923, 14177, 14179, 14177, 13411, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg600bce', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601', 12643, 12643, 12641, 25392, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601ahe', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25393, 25399, 25397, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601bnt', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13923, 14177, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 13155, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg602bsu', 12643, 14177, 14179, 14177, 14179, 14433, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg600uak', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12643, 24886, 25400, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg601kym', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24889, 25399, 24887, 25399, 25398, 24881, 25399, 24887, 12337, 14179, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701baz', 13667, 13409, 13411, 13409, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701bha', 12643, 13409, 13411, 14177, 14691, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701bjb', 12643, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg700bjn', 12643, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701bno', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701bpt', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701pag', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg700pbc', 12643, 12643, 14433, 14435, 14177, 14179, 14177, 14179, 13409, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg700rbl', 13667, 13409, 13411, 13409, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701rrb', 12643, 14177, 14179, 14177, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 25394, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701uhy', 12643, 13409, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701uor', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 24881, 25399, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24881, 25396, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701bce', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg700ahe', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24886, 25399, 24887, 25399, 24887, 25399, 25399, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg702ahe', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 25399, 25400, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701bnt', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14179, 12899, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg700bsu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 14433, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg700uak', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 14177, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 24881, 25399, 24887, 25399, 24887, 25399, 25397, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('brg701kym', 12643, 12643, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('6263650000000000000000000000000062726700000000000000000000000000626a6e00000000000000000000000000626e6f00000000000000000000000000'):
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
    PartnerChar('bny')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('brc')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('uhy')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('pbc')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('bno')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('bha')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('bjb')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('baz')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('bpt')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('rbl')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('bjn')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('uor')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('pag')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('rrb')
    if SLOT_ReturnVal:
        _gotolabel(230)
    PartnerChar('bce')
    if SLOT_ReturnVal:
        _gotolabel(240)
    PartnerChar('bnt')
    if SLOT_ReturnVal:
        _gotolabel(250)
    PartnerChar('ahe')
    if SLOT_ReturnVal:
        _gotolabel(260)
    PartnerChar('bsu')
    if SLOT_ReturnVal:
        _gotolabel(270)
    PartnerChar('uak')
    if SLOT_ReturnVal:
        _gotolabel(280)
    PartnerChar('kym')
    if SLOT_ReturnVal:
        _gotolabel(290)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('rg600_00', 6)	# 2-7
    sprite('rg600_00ex01', 6)	# 8-13
    sprite('rg600_00ex02', 6)	# 14-19
    if SLOT_158:
        Unknown7006('brg500', 100, 895971938, 12592, 0, 0, 100, 895971938, 13616, 0, 0, 100, 895971938, 13360, 0, 0, 100)
    sprite('rg600_01', 6)	# 20-25
    sprite('rg600_01ex01', 6)	# 26-31
    sprite('rg600_00', 6)	# 32-37
    sprite('rg600_00ex01', 6)	# 38-43
    sprite('rg600_00ex02', 6)	# 44-49
    sprite('rg600_01', 6)	# 50-55
    sprite('rg600_01ex01', 6)	# 56-61
    sprite('rg600_02', 6)	# 62-67
    sprite('rg600_03', 6)	# 68-73
    sprite('rg600_04', 6)	# 74-79
    sprite('rg600_05', 6)	# 80-85
    sprite('rg600_06', 24)	# 86-109
    sprite('rg600_07', 4)	# 110-113
    sprite('rg600_08', 4)	# 114-117
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 118-123
    sprite('rg600_10', 6)	# 124-129
    sprite('rg600_11', 6)	# 130-135
    sprite('rg600_12', 15)	# 136-150
    SFX_3('rgse_00')
    label(1)
    sprite('rg600_12', 1)	# 151-151
    if SLOT_97:
        _gotolabel(1)
    sprite('rg600_13', 6)	# 152-157
    Unknown21007(24, 41)
    sprite('rg600_14', 6)	# 158-163
    sprite('rg600_15', 6)	# 164-169
    sprite('rg600_16', 6)	# 170-175
    ExitState()
    label(10)
    sprite('rg601_00', 60)	# 176-235
    if SLOT_158:
        Unknown7006('brg502', 100, 895971938, 13104, 0, 0, 100, 895971938, 13616, 0, 0, 100, 895971938, 13360, 0, 0, 100)
    sprite('rg601_01', 6)	# 236-241
    sprite('rg601_02', 6)	# 242-247
    sprite('rg601_03', 6)	# 248-253
    sprite('rg601_04', 6)	# 254-259
    sprite('rg601_05', 6)	# 260-265
    sprite('rg601_06', 6)	# 266-271
    SFX_1('rg413')
    sprite('rg601_07', 6)	# 272-277
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 278-283
    sprite('rg601_09', 6)	# 284-289
    sprite('rg601_10', 6)	# 290-295
    sprite('rg601_11', 4)	# 296-299
    sprite('rg601_12', 4)	# 300-303
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 304-307
    sprite('rg601_14', 4)	# 308-311
    sprite('rg601_15', 4)	# 312-315
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 316-319
    sprite('rg601_17', 6)	# 320-325
    sprite('rg601_18', 6)	# 326-331
    sprite('rg601_19', 3)	# 332-334
    sprite('rg601_20', 6)	# 335-340
    Unknown21007(24, 41)
    sprite('rg601_21', 6)	# 341-346
    SFX_3('rgse_00')
    Unknown23018(1)
    sprite('rg601_22', 6)	# 347-352
    sprite('rg601_23', 6)	# 353-358
    label(11)
    sprite('rg000_00', 7)	# 359-365
    sprite('rg000_01', 7)	# 366-372
    sprite('rg000_02', 7)	# 373-379
    sprite('rg000_03', 7)	# 380-386
    sprite('rg000_04', 7)	# 387-393
    sprite('rg000_05', 7)	# 394-400
    sprite('rg000_06', 7)	# 401-407
    sprite('rg000_05', 7)	# 408-414
    sprite('rg000_04', 7)	# 415-421
    sprite('rg000_03', 7)	# 422-428
    sprite('rg000_02', 7)	# 429-435
    sprite('rg000_01', 7)	# 436-442
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('rg000_00', 1)	# 443-443
    SFX_1('brg701uor')
    label(21)
    sprite('rg000_00', 7)	# 444-450
    sprite('rg000_01', 7)	# 451-457
    sprite('rg000_02', 7)	# 458-464
    sprite('rg000_03', 7)	# 465-471
    sprite('rg000_04', 7)	# 472-478
    sprite('rg000_05', 7)	# 479-485
    sprite('rg000_06', 7)	# 486-492
    sprite('rg000_05', 7)	# 493-499
    sprite('rg000_04', 7)	# 500-506
    sprite('rg000_03', 7)	# 507-513
    sprite('rg000_02', 7)	# 514-520
    sprite('rg000_01', 7)	# 521-527
    gotoLabel(21)
    label(100)
    sprite('rg000_00', 1)	# 528-528
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('rg000_00', 7)	# 529-535
    sprite('rg000_01', 7)	# 536-542
    sprite('rg000_02', 7)	# 543-549
    sprite('rg000_03', 7)	# 550-556
    sprite('rg000_04', 7)	# 557-563
    sprite('rg000_05', 7)	# 564-570
    sprite('rg000_06', 7)	# 571-577
    sprite('rg000_05', 7)	# 578-584
    sprite('rg000_04', 7)	# 585-591
    sprite('rg000_03', 7)	# 592-598
    sprite('rg000_02', 7)	# 599-605
    sprite('rg000_01', 7)	# 606-612
    gotoLabel(101)
    label(102)
    sprite('rg300_00', 4)	# 613-616
    SFX_1('brg601bny')
    sprite('rg300_01', 4)	# 617-620
    sprite('rg300_02', 4)	# 621-624
    sprite('rg300_03', 6)	# 625-630
    sprite('rg300_04', 6)	# 631-636
    sprite('rg300_05', 37)	# 637-673
    sprite('rg300_04', 6)	# 674-679
    sprite('rg300_05', 7)	# 680-686
    sprite('rg300_03', 9)	# 687-695
    sprite('rg300_06', 6)	# 696-701
    sprite('rg300_07', 6)	# 702-707
    sprite('rg300_08', 6)	# 708-713
    Unknown23018(1)
    label(103)
    sprite('rg000_00', 7)	# 714-720
    sprite('rg000_01', 7)	# 721-727
    sprite('rg000_02', 7)	# 728-734
    sprite('rg000_03', 7)	# 735-741
    sprite('rg000_04', 7)	# 742-748
    sprite('rg000_05', 7)	# 749-755
    sprite('rg000_06', 7)	# 756-762
    sprite('rg000_05', 7)	# 763-769
    sprite('rg000_04', 7)	# 770-776
    sprite('rg000_03', 7)	# 777-783
    sprite('rg000_02', 7)	# 784-790
    sprite('rg000_01', 7)	# 791-797
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('rg000_00', 1)	# 798-798
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    sprite('rg000_00', 7)	# 799-805
    sprite('rg000_01', 7)	# 806-812
    sprite('rg000_02', 7)	# 813-819
    sprite('rg000_03', 7)	# 820-826
    sprite('rg000_04', 7)	# 827-833
    sprite('rg000_05', 7)	# 834-840
    sprite('rg000_06', 7)	# 841-847
    sprite('rg000_05', 7)	# 848-854
    sprite('rg000_04', 7)	# 855-861
    sprite('rg000_03', 7)	# 862-868
    sprite('rg000_02', 7)	# 869-875
    sprite('rg000_01', 7)	# 876-882
    sprite('rg001_00', 6)	# 883-888
    sprite('rg001_01', 6)	# 889-894
    sprite('rg001_02', 6)	# 895-900
    sprite('rg001_03', 6)	# 901-906
    sprite('rg001_04', 6)	# 907-912
    sprite('rg001_05', 6)	# 913-918
    sprite('rg001_06', 6)	# 919-924
    sprite('rg001_07', 6)	# 925-930
    sprite('rg001_08', 6)	# 931-936
    sprite('rg001_09', 6)	# 937-942
    sprite('rg001_10', 6)	# 943-948
    sprite('rg001_11', 6)	# 949-954
    sprite('rg001_12', 6)	# 955-960
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 961-966
    sprite('rg001_14', 6)	# 967-972
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 973-978
    sprite('rg001_16', 6)	# 979-984
    label(111)
    sprite('rg000_00', 7)	# 985-991
    sprite('rg000_01', 7)	# 992-998
    sprite('rg000_02', 7)	# 999-1005
    sprite('rg000_03', 7)	# 1006-1012
    sprite('rg000_04', 7)	# 1013-1019
    sprite('rg000_05', 7)	# 1020-1026
    sprite('rg000_06', 7)	# 1027-1033
    sprite('rg000_05', 7)	# 1034-1040
    sprite('rg000_04', 7)	# 1041-1047
    sprite('rg000_03', 7)	# 1048-1054
    sprite('rg000_02', 7)	# 1055-1061
    sprite('rg000_01', 7)	# 1062-1068
    gotoLabel(111)
    label(112)
    sprite('rg300_00', 4)	# 1069-1072
    SFX_1('brg601brc')
    sprite('rg300_01', 4)	# 1073-1076
    sprite('rg300_02', 4)	# 1077-1080
    sprite('rg300_03', 6)	# 1081-1086
    sprite('rg300_04', 6)	# 1087-1092
    sprite('rg300_05', 67)	# 1093-1159
    sprite('rg300_04', 6)	# 1160-1165
    sprite('rg300_05', 7)	# 1166-1172
    sprite('rg300_03', 9)	# 1173-1181
    sprite('rg300_06', 6)	# 1182-1187
    sprite('rg300_07', 6)	# 1188-1193
    sprite('rg300_08', 6)	# 1194-1199
    Unknown23018(1)
    label(113)
    sprite('rg000_00', 7)	# 1200-1206
    sprite('rg000_01', 7)	# 1207-1213
    sprite('rg000_02', 7)	# 1214-1220
    sprite('rg000_03', 7)	# 1221-1227
    sprite('rg000_04', 7)	# 1228-1234
    sprite('rg000_05', 7)	# 1235-1241
    sprite('rg000_06', 7)	# 1242-1248
    sprite('rg000_05', 7)	# 1249-1255
    sprite('rg000_04', 7)	# 1256-1262
    sprite('rg000_03', 7)	# 1263-1269
    sprite('rg000_02', 7)	# 1270-1276
    sprite('rg000_01', 7)	# 1277-1283
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('rg600_00', 6)	# 1284-1289
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rg600_00ex01', 6)	# 1290-1295
    sprite('rg600_00ex02', 6)	# 1296-1301
    sprite('rg600_01', 6)	# 1302-1307
    SFX_1('brg600uhy')
    sprite('rg600_01ex01', 6)	# 1308-1313
    sprite('rg600_00', 6)	# 1314-1319
    sprite('rg600_00ex01', 6)	# 1320-1325
    sprite('rg600_00ex02', 6)	# 1326-1331
    sprite('rg600_01', 6)	# 1332-1337
    sprite('rg600_01ex01', 6)	# 1338-1343
    sprite('rg600_00', 6)	# 1344-1349
    sprite('rg600_00ex01', 6)	# 1350-1355
    sprite('rg600_00ex02', 6)	# 1356-1361
    sprite('rg600_01', 6)	# 1362-1367
    sprite('rg600_01ex01', 6)	# 1368-1373
    sprite('rg600_00', 6)	# 1374-1379
    sprite('rg600_00ex01', 6)	# 1380-1385
    sprite('rg600_00ex02', 6)	# 1386-1391
    sprite('rg600_01', 6)	# 1392-1397
    sprite('rg600_01ex01', 6)	# 1398-1403
    sprite('rg600_02', 6)	# 1404-1409
    sprite('rg600_03', 6)	# 1410-1415
    sprite('rg600_04', 6)	# 1416-1421
    sprite('rg600_05', 6)	# 1422-1427
    sprite('rg600_06', 24)	# 1428-1451
    sprite('rg600_07', 4)	# 1452-1455
    sprite('rg600_08', 4)	# 1456-1459
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 1460-1465
    sprite('rg600_10', 6)	# 1466-1471
    sprite('rg600_11', 6)	# 1472-1477
    sprite('rg600_12', 45)	# 1478-1522
    SFX_3('rgse_00')
    label(121)
    sprite('rg600_12', 1)	# 1523-1523
    if SLOT_97:
        _gotolabel(121)
    sprite('rg600_13', 6)	# 1524-1529
    Unknown21007(24, 40)
    sprite('rg600_14', 6)	# 1530-1535
    sprite('rg600_15', 6)	# 1536-1541
    sprite('rg600_16', 6)	# 1542-1547
    Unknown21011(240)
    label(122)
    sprite('rg000_00', 7)	# 1548-1554
    sprite('rg000_01', 7)	# 1555-1561
    sprite('rg000_02', 7)	# 1562-1568
    sprite('rg000_03', 7)	# 1569-1575
    sprite('rg000_04', 7)	# 1576-1582
    sprite('rg000_05', 7)	# 1583-1589
    sprite('rg000_06', 7)	# 1590-1596
    sprite('rg000_05', 7)	# 1597-1603
    sprite('rg000_04', 7)	# 1604-1610
    sprite('rg000_03', 7)	# 1611-1617
    sprite('rg000_02', 7)	# 1618-1624
    sprite('rg000_01', 7)	# 1625-1631
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('rg000_00', 1)	# 1632-1632
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('rg000_00', 7)	# 1633-1639
    sprite('rg000_01', 7)	# 1640-1646
    sprite('rg000_02', 7)	# 1647-1653
    sprite('rg000_03', 7)	# 1654-1660
    sprite('rg000_04', 7)	# 1661-1667
    sprite('rg000_05', 7)	# 1668-1674
    sprite('rg000_06', 7)	# 1675-1681
    sprite('rg000_05', 7)	# 1682-1688
    sprite('rg000_04', 7)	# 1689-1695
    sprite('rg000_03', 7)	# 1696-1702
    sprite('rg000_02', 7)	# 1703-1709
    sprite('rg000_01', 7)	# 1710-1716
    gotoLabel(131)
    label(132)
    sprite('rg001_00', 6)	# 1717-1722
    SFX_1('brg601pbc')
    sprite('rg001_01', 6)	# 1723-1728
    sprite('rg001_02', 6)	# 1729-1734
    sprite('rg001_03', 6)	# 1735-1740
    sprite('rg001_04', 6)	# 1741-1746
    sprite('rg001_05', 6)	# 1747-1752
    sprite('rg001_06', 6)	# 1753-1758
    sprite('rg001_07', 6)	# 1759-1764
    sprite('rg001_08', 6)	# 1765-1770
    sprite('rg001_09', 6)	# 1771-1776
    sprite('rg001_10', 6)	# 1777-1782
    sprite('rg001_11', 6)	# 1783-1788
    sprite('rg001_12', 6)	# 1789-1794
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 1795-1800
    sprite('rg001_14', 6)	# 1801-1806
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 1807-1812
    sprite('rg001_16', 6)	# 1813-1818
    sprite('rg000_00', 1)	# 1819-1819

    def upon_39():
        clearUponHandler(39)
        sendToLabel(134)
    label(133)
    sprite('rg000_00', 7)	# 1820-1826
    sprite('rg000_01', 7)	# 1827-1833
    sprite('rg000_02', 7)	# 1834-1840
    sprite('rg000_03', 7)	# 1841-1847
    sprite('rg000_04', 7)	# 1848-1854
    sprite('rg000_05', 7)	# 1855-1861
    sprite('rg000_06', 7)	# 1862-1868
    sprite('rg000_05', 7)	# 1869-1875
    sprite('rg000_04', 7)	# 1876-1882
    sprite('rg000_03', 7)	# 1883-1889
    Unknown21007(24, 39)
    sprite('rg000_02', 7)	# 1890-1896
    sprite('rg000_01', 7)	# 1897-1903
    gotoLabel(133)
    label(134)
    sprite('rg300_00', 4)	# 1904-1907

    def upon_38():
        clearUponHandler(38)
        sendToLabel(136)
    SFX_1('brg603pbc')
    sprite('rg300_01', 4)	# 1908-1911
    sprite('rg300_02', 4)	# 1912-1915
    sprite('rg300_03', 6)	# 1916-1921
    sprite('rg300_04', 6)	# 1922-1927
    sprite('rg300_05', 67)	# 1928-1994
    sprite('rg300_04', 6)	# 1995-2000
    sprite('rg300_05', 7)	# 2001-2007
    sprite('rg300_03', 9)	# 2008-2016
    sprite('rg300_06', 6)	# 2017-2022
    sprite('rg300_07', 6)	# 2023-2028
    sprite('rg300_08', 6)	# 2029-2034
    label(135)
    sprite('rg000_00', 7)	# 2035-2041
    sprite('rg000_01', 7)	# 2042-2048
    sprite('rg000_02', 7)	# 2049-2055
    sprite('rg000_03', 7)	# 2056-2062
    sprite('rg000_04', 7)	# 2063-2069
    sprite('rg000_05', 7)	# 2070-2076
    sprite('rg000_06', 7)	# 2077-2083
    sprite('rg000_05', 7)	# 2084-2090
    sprite('rg000_04', 7)	# 2091-2097
    sprite('rg000_03', 7)	# 2098-2104
    sprite('rg000_02', 7)	# 2105-2111
    Unknown21007(24, 38)
    sprite('rg000_01', 7)	# 2112-2118
    gotoLabel(135)
    label(136)
    sprite('rg600_15', 5)	# 2119-2123
    sprite('rg600_14', 5)	# 2124-2128
    sprite('rg600_04', 5)	# 2129-2133
    sprite('rg600_05', 5)	# 2134-2138
    sprite('rg600_06', 32)	# 2139-2170
    sprite('rg600_07', 4)	# 2171-2174
    sprite('rg600_08', 4)	# 2175-2178
    SFX_1('brg605pbc')
    sprite('rg600_09', 5)	# 2179-2183
    sprite('rg600_10', 4)	# 2184-2187
    sprite('rg600_11', 5)	# 2188-2192
    sprite('rg600_12', 32767)	# 2193-34959
    SFX_3('rgse_00')
    Unknown23018(1)
    label(137)
    sprite('rg000_00', 7)	# 34960-34966
    sprite('rg000_01', 7)	# 34967-34973
    sprite('rg000_02', 7)	# 34974-34980
    sprite('rg000_03', 7)	# 34981-34987
    sprite('rg000_04', 7)	# 34988-34994
    sprite('rg000_05', 7)	# 34995-35001
    sprite('rg000_06', 7)	# 35002-35008
    sprite('rg000_05', 7)	# 35009-35015
    sprite('rg000_04', 7)	# 35016-35022
    sprite('rg000_03', 7)	# 35023-35029
    sprite('rg000_02', 7)	# 35030-35036
    sprite('rg000_01', 7)	# 35037-35043
    gotoLabel(137)
    ExitState()
    label(140)
    sprite('rg600_00', 1)	# 35044-35044
    if SLOT_158:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
        SFX_1('brg601bno')
    label(141)
    sprite('rg600_00', 6)	# 35045-35050
    sprite('rg600_00ex01', 6)	# 35051-35056
    sprite('rg600_00ex02', 6)	# 35057-35062
    sprite('rg600_01', 6)	# 35063-35068
    sprite('rg600_01ex01', 6)	# 35069-35074
    sprite('rg600_00', 6)	# 35075-35080
    sprite('rg600_00ex01', 6)	# 35081-35086
    sprite('rg600_00ex02', 6)	# 35087-35092
    sprite('rg600_01', 6)	# 35093-35098
    sprite('rg600_01ex01', 6)	# 35099-35104
    sprite('rg600_00', 6)	# 35105-35110
    sprite('rg600_00ex01', 6)	# 35111-35116
    sprite('rg600_00ex02', 6)	# 35117-35122
    sprite('rg600_01', 6)	# 35123-35128
    sprite('rg600_01ex01', 6)	# 35129-35134
    sprite('rg600_00', 6)	# 35135-35140
    sprite('rg600_00ex01', 6)	# 35141-35146
    sprite('rg600_00ex02', 6)	# 35147-35152
    sprite('rg600_01', 6)	# 35153-35158
    sprite('rg600_01ex01', 6)	# 35159-35164
    gotoLabel(141)
    label(142)
    sprite('rg600_02', 6)	# 35165-35170
    sprite('rg600_03', 6)	# 35171-35176
    sprite('rg600_04', 6)	# 35177-35182
    sprite('rg600_05', 6)	# 35183-35188
    sprite('rg600_06', 24)	# 35189-35212
    sprite('rg600_07', 4)	# 35213-35216
    sprite('rg600_08', 4)	# 35217-35220
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 35221-35226
    sprite('rg600_10', 6)	# 35227-35232
    sprite('rg600_11', 6)	# 35233-35238
    sprite('rg600_12', 45)	# 35239-35283
    SFX_3('rgse_00')
    label(143)
    sprite('rg600_12', 1)	# 35284-35284
    if SLOT_97:
        _gotolabel(143)
    sprite('rg600_13', 6)	# 35285-35290
    sprite('rg600_14', 6)	# 35291-35296
    sprite('rg600_15', 6)	# 35297-35302
    sprite('rg600_16', 6)	# 35303-35308
    Unknown23018(1)
    label(144)
    sprite('rg000_00', 7)	# 35309-35315
    sprite('rg000_01', 7)	# 35316-35322
    sprite('rg000_02', 7)	# 35323-35329
    sprite('rg000_03', 7)	# 35330-35336
    sprite('rg000_04', 7)	# 35337-35343
    sprite('rg000_05', 7)	# 35344-35350
    sprite('rg000_06', 7)	# 35351-35357
    sprite('rg000_05', 7)	# 35358-35364
    sprite('rg000_04', 7)	# 35365-35371
    sprite('rg000_03', 7)	# 35372-35378
    sprite('rg000_02', 7)	# 35379-35385
    sprite('rg000_01', 7)	# 35386-35392
    gotoLabel(144)
    ExitState()
    label(150)
    sprite('rg000_00', 1)	# 35393-35393
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('rg000_00', 7)	# 35394-35400
    sprite('rg000_01', 7)	# 35401-35407
    sprite('rg000_02', 7)	# 35408-35414
    sprite('rg000_03', 7)	# 35415-35421
    sprite('rg000_04', 7)	# 35422-35428
    sprite('rg000_05', 7)	# 35429-35435
    sprite('rg000_06', 7)	# 35436-35442
    sprite('rg000_05', 7)	# 35443-35449
    sprite('rg000_04', 7)	# 35450-35456
    sprite('rg000_03', 7)	# 35457-35463
    sprite('rg000_02', 7)	# 35464-35470
    sprite('rg000_01', 7)	# 35471-35477
    gotoLabel(151)
    label(152)
    sprite('rg300_00', 4)	# 35478-35481
    SFX_1('brg601bha')
    sprite('rg300_01', 4)	# 35482-35485
    sprite('rg300_02', 4)	# 35486-35489
    sprite('rg300_03', 6)	# 35490-35495
    sprite('rg300_04', 6)	# 35496-35501
    sprite('rg300_05', 67)	# 35502-35568
    sprite('rg300_04', 6)	# 35569-35574
    sprite('rg300_05', 7)	# 35575-35581
    sprite('rg300_03', 9)	# 35582-35590
    sprite('rg300_06', 6)	# 35591-35596
    sprite('rg300_07', 6)	# 35597-35602
    sprite('rg300_08', 6)	# 35603-35608
    Unknown23018(1)
    label(153)
    sprite('rg000_00', 7)	# 35609-35615
    sprite('rg000_01', 7)	# 35616-35622
    sprite('rg000_02', 7)	# 35623-35629
    sprite('rg000_03', 7)	# 35630-35636
    sprite('rg000_04', 7)	# 35637-35643
    sprite('rg000_05', 7)	# 35644-35650
    sprite('rg000_06', 7)	# 35651-35657
    sprite('rg000_05', 7)	# 35658-35664
    sprite('rg000_04', 7)	# 35665-35671
    sprite('rg000_03', 7)	# 35672-35678
    sprite('rg000_02', 7)	# 35679-35685
    sprite('rg000_01', 7)	# 35686-35692
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('rg000_00', 1)	# 35693-35693
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
        SFX_1('brg601bjb')
    label(161)
    sprite('rg000_00', 7)	# 35694-35700
    sprite('rg000_01', 7)	# 35701-35707
    sprite('rg000_02', 7)	# 35708-35714
    sprite('rg000_03', 7)	# 35715-35721
    sprite('rg000_04', 7)	# 35722-35728
    sprite('rg000_05', 7)	# 35729-35735
    sprite('rg000_06', 7)	# 35736-35742
    sprite('rg000_05', 7)	# 35743-35749
    sprite('rg000_04', 7)	# 35750-35756
    sprite('rg000_03', 7)	# 35757-35763
    sprite('rg000_02', 7)	# 35764-35770
    sprite('rg000_01', 7)	# 35771-35777
    gotoLabel(161)
    label(162)
    sprite('rg001_00', 6)	# 35778-35783
    sprite('rg001_01', 6)	# 35784-35789
    sprite('rg001_02', 6)	# 35790-35795
    sprite('rg001_03', 6)	# 35796-35801
    sprite('rg001_04', 6)	# 35802-35807
    sprite('rg001_05', 6)	# 35808-35813
    sprite('rg001_06', 6)	# 35814-35819
    sprite('rg001_07', 6)	# 35820-35825
    sprite('rg001_08', 6)	# 35826-35831
    sprite('rg001_09', 6)	# 35832-35837
    sprite('rg001_10', 6)	# 35838-35843
    sprite('rg001_11', 6)	# 35844-35849
    sprite('rg001_12', 6)	# 35850-35855
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 35856-35861
    sprite('rg001_14', 6)	# 35862-35867
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 35868-35873
    sprite('rg001_16', 6)	# 35874-35879
    Unknown23018(1)
    label(163)
    sprite('rg000_00', 7)	# 35880-35886
    sprite('rg000_01', 7)	# 35887-35893
    sprite('rg000_02', 7)	# 35894-35900
    sprite('rg000_03', 7)	# 35901-35907
    sprite('rg000_04', 7)	# 35908-35914
    sprite('rg000_05', 7)	# 35915-35921
    sprite('rg000_06', 7)	# 35922-35928
    sprite('rg000_05', 7)	# 35929-35935
    sprite('rg000_04', 7)	# 35936-35942
    sprite('rg000_03', 7)	# 35943-35949
    sprite('rg000_02', 7)	# 35950-35956
    sprite('rg000_01', 7)	# 35957-35963
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('rg600_00', 1)	# 35964-35964
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1495000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
        SFX_1('brg601baz')
    label(171)
    sprite('rg600_00', 6)	# 35965-35970
    sprite('rg600_00ex01', 6)	# 35971-35976
    sprite('rg600_00ex02', 6)	# 35977-35982
    sprite('rg600_01', 6)	# 35983-35988
    sprite('rg600_01ex01', 6)	# 35989-35994
    gotoLabel(171)
    label(172)
    sprite('rg600_02', 6)	# 35995-36000
    sprite('rg600_03', 6)	# 36001-36006
    sprite('rg600_04', 6)	# 36007-36012
    sprite('rg600_05', 6)	# 36013-36018
    sprite('rg600_06', 24)	# 36019-36042
    sprite('rg600_07', 4)	# 36043-36046
    sprite('rg600_08', 4)	# 36047-36050
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 36051-36056
    sprite('rg600_10', 6)	# 36057-36062
    sprite('rg600_11', 6)	# 36063-36068
    sprite('rg600_12', 15)	# 36069-36083
    SFX_3('rgse_00')
    label(173)
    sprite('rg600_12', 1)	# 36084-36084
    if SLOT_97:
        _gotolabel(173)
    sprite('rg600_13', 6)	# 36085-36090
    Unknown21007(24, 41)
    sprite('rg600_14', 6)	# 36091-36096
    sprite('rg600_15', 6)	# 36097-36102
    sprite('rg600_16', 6)	# 36103-36108
    Unknown23018(1)
    label(174)
    sprite('rg000_00', 7)	# 36109-36115
    sprite('rg000_01', 7)	# 36116-36122
    sprite('rg000_02', 7)	# 36123-36129
    sprite('rg000_03', 7)	# 36130-36136
    sprite('rg000_04', 7)	# 36137-36143
    sprite('rg000_05', 7)	# 36144-36150
    sprite('rg000_06', 7)	# 36151-36157
    sprite('rg000_05', 7)	# 36158-36164
    sprite('rg000_04', 7)	# 36165-36171
    sprite('rg000_03', 7)	# 36172-36178
    sprite('rg000_02', 7)	# 36179-36185
    sprite('rg000_01', 7)	# 36186-36192
    gotoLabel(174)
    label(180)
    sprite('rg000_00', 1)	# 36193-36193
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('rg000_00', 7)	# 36194-36200
    sprite('rg000_01', 7)	# 36201-36207
    sprite('rg000_02', 7)	# 36208-36214
    sprite('rg000_03', 7)	# 36215-36221
    sprite('rg000_04', 7)	# 36222-36228
    sprite('rg000_05', 7)	# 36229-36235
    sprite('rg000_06', 7)	# 36236-36242
    sprite('rg000_05', 7)	# 36243-36249
    sprite('rg000_04', 7)	# 36250-36256
    sprite('rg000_03', 7)	# 36257-36263
    sprite('rg000_02', 7)	# 36264-36270
    sprite('rg000_01', 7)	# 36271-36277
    gotoLabel(181)
    label(182)
    sprite('rg300_00', 4)	# 36278-36281
    SFX_1('brg601bpt')
    sprite('rg300_01', 4)	# 36282-36285
    sprite('rg300_02', 4)	# 36286-36289
    sprite('rg300_03', 6)	# 36290-36295
    sprite('rg300_04', 6)	# 36296-36301
    sprite('rg300_05', 37)	# 36302-36338
    sprite('rg300_04', 6)	# 36339-36344
    sprite('rg300_05', 7)	# 36345-36351
    sprite('rg300_03', 9)	# 36352-36360
    sprite('rg300_06', 6)	# 36361-36366
    sprite('rg300_07', 6)	# 36367-36372
    sprite('rg300_08', 6)	# 36373-36378
    Unknown21011(120)
    label(183)
    sprite('rg000_00', 7)	# 36379-36385
    sprite('rg000_01', 7)	# 36386-36392
    sprite('rg000_02', 7)	# 36393-36399
    sprite('rg000_03', 7)	# 36400-36406
    sprite('rg000_04', 7)	# 36407-36413
    sprite('rg000_05', 7)	# 36414-36420
    sprite('rg000_06', 7)	# 36421-36427
    sprite('rg000_05', 7)	# 36428-36434
    sprite('rg000_04', 7)	# 36435-36441
    sprite('rg000_03', 7)	# 36442-36448
    sprite('rg000_02', 7)	# 36449-36455
    sprite('rg000_01', 7)	# 36456-36462
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('rg601_00', 20)	# 36463-36482
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rg601_01', 6)	# 36483-36488
    sprite('rg601_02', 6)	# 36489-36494
    sprite('rg601_03', 6)	# 36495-36500
    sprite('rg601_04', 6)	# 36501-36506
    sprite('rg601_05', 6)	# 36507-36512
    sprite('rg601_06', 6)	# 36513-36518
    SFX_1('brg600rbl')
    sprite('rg601_07', 6)	# 36519-36524
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 36525-36530
    sprite('rg601_09', 6)	# 36531-36536
    sprite('rg601_10', 6)	# 36537-36542
    sprite('rg601_11', 4)	# 36543-36546
    sprite('rg601_12', 4)	# 36547-36550
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 36551-36554
    sprite('rg601_14', 4)	# 36555-36558
    sprite('rg601_15', 4)	# 36559-36562
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 36563-36566
    sprite('rg601_17', 6)	# 36567-36572
    sprite('rg601_18', 6)	# 36573-36578
    sprite('rg601_19', 3)	# 36579-36581
    sprite('rg601_20', 6)	# 36582-36587
    sprite('rg601_21', 6)	# 36588-36593
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 36594-36599
    sprite('rg601_23', 6)	# 36600-36605
    label(191)
    sprite('rg000_00', 7)	# 36606-36612
    sprite('rg000_01', 7)	# 36613-36619
    sprite('rg000_02', 7)	# 36620-36626
    sprite('rg000_03', 7)	# 36627-36633
    sprite('rg000_04', 7)	# 36634-36640
    sprite('rg000_05', 7)	# 36641-36647
    sprite('rg000_06', 7)	# 36648-36654
    sprite('rg000_05', 7)	# 36655-36661
    sprite('rg000_04', 7)	# 36662-36668
    sprite('rg000_03', 7)	# 36669-36675
    sprite('rg000_02', 7)	# 36676-36682
    sprite('rg000_01', 7)	# 36683-36689
    if SLOT_97:
        _gotolabel(191)
    sprite('rg000_00', 1)	# 36690-36690
    Unknown21007(24, 40)
    Unknown21011(180)
    label(192)
    sprite('rg000_00', 7)	# 36691-36697
    sprite('rg000_01', 7)	# 36698-36704
    sprite('rg000_02', 7)	# 36705-36711
    sprite('rg000_03', 7)	# 36712-36718
    sprite('rg000_04', 7)	# 36719-36725
    sprite('rg000_05', 7)	# 36726-36732
    sprite('rg000_06', 7)	# 36733-36739
    sprite('rg000_05', 7)	# 36740-36746
    sprite('rg000_04', 7)	# 36747-36753
    sprite('rg000_03', 7)	# 36754-36760
    sprite('rg000_02', 7)	# 36761-36767
    sprite('rg000_01', 7)	# 36768-36774
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('rg630_00', 32767)	# 36775-69541
    Unknown2019(-100)
    if SLOT_158:
        Unknown1000(-1330000)
        Unknown2005()
    else:
        Unknown1000(-1330000)
        Unknown2005()

    def upon_40():
        clearUponHandler(40)
        sendToLabel(201)
    label(201)
    sprite('rg033_00', 1)	# 69542-69542
    sprite('rg033_01', 2)	# 69543-69544
    SFX_3('rgse_00')
    physicsXImpulse(-12500)
    physicsYImpulse(13000)
    setGravity(1550)
    Unknown8002()
    sprite('rg033_02', 2)	# 69545-69546
    sprite('rg033_02', 1)	# 69547-69547
    sprite('rg033_03', 3)	# 69548-69550
    loopRest()
    sprite('rg033_02', 3)	# 69551-69553
    sprite('rg033_03', 3)	# 69554-69556
    sprite('rg033_02', 3)	# 69557-69559
    sprite('rg033_03', 2)	# 69560-69561
    sprite('rg010_01', 2)	# 69562-69563
    Unknown1044()
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    teleportRelativeY(0)
    sprite('rg010_02', 2)	# 69564-69565
    sprite('rg010_01', 6)	# 69566-69571
    sprite('rg010_00', 6)	# 69572-69577
    SFX_1('brg601bjn')

    def upon_39():
        clearUponHandler(39)
        sendToLabel(203)
    label(202)
    sprite('rg000_00', 7)	# 69578-69584
    sprite('rg000_01', 7)	# 69585-69591
    sprite('rg000_02', 7)	# 69592-69598
    sprite('rg000_03', 7)	# 69599-69605
    sprite('rg000_04', 7)	# 69606-69612
    sprite('rg000_05', 7)	# 69613-69619
    sprite('rg000_06', 7)	# 69620-69626
    sprite('rg000_05', 7)	# 69627-69633
    sprite('rg000_04', 7)	# 69634-69640
    sprite('rg000_03', 7)	# 69641-69647
    sprite('rg000_02', 7)	# 69648-69654
    sprite('rg000_01', 7)	# 69655-69661
    gotoLabel(202)
    label(203)
    sprite('rg003_00', 5)	# 69662-69666
    Unknown2005()
    sprite('rg003_01', 5)	# 69667-69671
    sprite('rg003_02', 5)	# 69672-69676
    sprite('rg001_01', 6)	# 69677-69682
    sprite('rg001_02', 6)	# 69683-69688
    sprite('rg001_03', 6)	# 69689-69694
    sprite('rg001_04', 6)	# 69695-69700
    sprite('rg001_05', 6)	# 69701-69706
    sprite('rg001_06', 6)	# 69707-69712
    sprite('rg001_07', 6)	# 69713-69718
    sprite('rg001_08', 6)	# 69719-69724
    sprite('rg001_09', 6)	# 69725-69730
    sprite('rg001_10', 6)	# 69731-69736
    sprite('rg001_11', 6)	# 69737-69742
    sprite('rg001_12', 6)	# 69743-69748
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 69749-69754
    sprite('rg001_14', 6)	# 69755-69760
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 69761-69766
    sprite('rg001_16', 6)	# 69767-69772
    Unknown21011(120)
    label(204)
    sprite('rg000_00', 7)	# 69773-69779
    sprite('rg000_01', 7)	# 69780-69786
    sprite('rg000_02', 7)	# 69787-69793
    sprite('rg000_03', 7)	# 69794-69800
    sprite('rg000_04', 7)	# 69801-69807
    sprite('rg000_05', 7)	# 69808-69814
    sprite('rg000_06', 7)	# 69815-69821
    sprite('rg000_05', 7)	# 69822-69828
    sprite('rg000_04', 7)	# 69829-69835
    sprite('rg000_03', 7)	# 69836-69842
    sprite('rg000_02', 7)	# 69843-69849
    sprite('rg000_01', 7)	# 69850-69856
    gotoLabel(204)
    ExitState()
    label(210)
    sprite('rg000_00', 1)	# 69857-69857
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('rg000_00', 7)	# 69858-69864
    sprite('rg000_01', 7)	# 69865-69871
    sprite('rg000_02', 7)	# 69872-69878
    sprite('rg000_03', 7)	# 69879-69885
    sprite('rg000_04', 7)	# 69886-69892
    sprite('rg000_05', 7)	# 69893-69899
    sprite('rg000_06', 7)	# 69900-69906
    sprite('rg000_05', 7)	# 69907-69913
    sprite('rg000_04', 7)	# 69914-69920
    sprite('rg000_03', 7)	# 69921-69927
    sprite('rg000_02', 7)	# 69928-69934
    sprite('rg000_01', 7)	# 69935-69941
    gotoLabel(211)
    label(212)
    sprite('rg001_00', 6)	# 69942-69947
    SFX_1('brg601uor')
    sprite('rg001_01', 6)	# 69948-69953
    sprite('rg001_02', 6)	# 69954-69959
    sprite('rg001_03', 6)	# 69960-69965
    sprite('rg001_04', 6)	# 69966-69971
    sprite('rg001_05', 6)	# 69972-69977
    sprite('rg001_06', 6)	# 69978-69983
    sprite('rg001_07', 6)	# 69984-69989
    sprite('rg001_08', 6)	# 69990-69995
    sprite('rg001_09', 6)	# 69996-70001
    sprite('rg001_10', 6)	# 70002-70007
    sprite('rg001_11', 6)	# 70008-70013
    sprite('rg001_12', 6)	# 70014-70019
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 70020-70025
    sprite('rg001_14', 6)	# 70026-70031
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 70032-70037
    sprite('rg001_16', 6)	# 70038-70043
    Unknown23018(1)
    label(213)
    sprite('rg000_00', 7)	# 70044-70050
    sprite('rg000_01', 7)	# 70051-70057
    sprite('rg000_02', 7)	# 70058-70064
    sprite('rg000_03', 7)	# 70065-70071
    sprite('rg000_04', 7)	# 70072-70078
    sprite('rg000_05', 7)	# 70079-70085
    sprite('rg000_06', 7)	# 70086-70092
    sprite('rg000_05', 7)	# 70093-70099
    sprite('rg000_04', 7)	# 70100-70106
    sprite('rg000_03', 7)	# 70107-70113
    sprite('rg000_02', 7)	# 70114-70120
    sprite('rg000_01', 7)	# 70121-70127
    gotoLabel(213)
    ExitState()
    label(220)
    sprite('rg000_00', 1)	# 70128-70128
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('rg000_00', 7)	# 70129-70135
    sprite('rg000_01', 7)	# 70136-70142
    sprite('rg000_02', 7)	# 70143-70149
    sprite('rg000_03', 7)	# 70150-70156
    sprite('rg000_04', 7)	# 70157-70163
    sprite('rg000_05', 7)	# 70164-70170
    sprite('rg000_06', 7)	# 70171-70177
    sprite('rg000_05', 7)	# 70178-70184
    sprite('rg000_04', 7)	# 70185-70191
    sprite('rg000_03', 7)	# 70192-70198
    sprite('rg000_02', 7)	# 70199-70205
    sprite('rg000_01', 7)	# 70206-70212
    gotoLabel(221)
    label(222)
    sprite('rg001_00', 6)	# 70213-70218
    SFX_1('brg601pag')
    sprite('rg001_01', 6)	# 70219-70224
    sprite('rg001_02', 6)	# 70225-70230
    sprite('rg001_03', 6)	# 70231-70236
    sprite('rg001_04', 6)	# 70237-70242
    sprite('rg001_05', 6)	# 70243-70248
    sprite('rg001_06', 6)	# 70249-70254
    sprite('rg001_07', 6)	# 70255-70260
    sprite('rg001_08', 6)	# 70261-70266
    sprite('rg001_09', 6)	# 70267-70272
    sprite('rg001_10', 6)	# 70273-70278
    sprite('rg001_11', 6)	# 70279-70284
    sprite('rg001_12', 6)	# 70285-70290
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 70291-70296
    sprite('rg001_14', 6)	# 70297-70302
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 70303-70308
    sprite('rg001_16', 6)	# 70309-70314
    Unknown23018(1)
    label(223)
    sprite('rg000_00', 7)	# 70315-70321
    sprite('rg000_01', 7)	# 70322-70328
    sprite('rg000_02', 7)	# 70329-70335
    sprite('rg000_03', 7)	# 70336-70342
    sprite('rg000_04', 7)	# 70343-70349
    sprite('rg000_05', 7)	# 70350-70356
    sprite('rg000_06', 7)	# 70357-70363
    sprite('rg000_05', 7)	# 70364-70370
    sprite('rg000_04', 7)	# 70371-70377
    sprite('rg000_03', 7)	# 70378-70384
    sprite('rg000_02', 7)	# 70385-70391
    sprite('rg000_01', 7)	# 70392-70398
    gotoLabel(223)
    ExitState()
    label(230)
    sprite('rg631_00', 32767)	# 70399-103165
    Unknown2019(-100)
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(231)
    label(231)
    sprite('rg631_01', 6)	# 103166-103171
    SFX_1('brg601rrb')
    Unknown21007(24, 40)
    sprite('rg631_02', 6)	# 103172-103177
    sprite('rg631_03', 6)	# 103178-103183
    sprite('rg631_04', 32767)	# 103184-135950
    Unknown23018(1)
    ExitState()
    label(240)
    sprite('rg601_00', 6)	# 135951-135956
    if (not SLOT_158):
        Unknown1000(-1230000)
    sprite('rg601_00', 1)	# 135957-135957
    SFX_1('brg600bce')
    label(241)
    sprite('rg601_00', 1)	# 135958-135958
    if SLOT_97:
        _gotolabel(241)
    sprite('rg601_01', 6)	# 135959-135964
    sprite('rg601_02', 6)	# 135965-135970
    sprite('rg601_03', 6)	# 135971-135976
    sprite('rg601_04', 6)	# 135977-135982
    sprite('rg601_05', 6)	# 135983-135988
    sprite('rg601_06', 6)	# 135989-135994
    sprite('rg601_07', 6)	# 135995-136000
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 136001-136006
    sprite('rg601_09', 6)	# 136007-136012
    sprite('rg601_10', 6)	# 136013-136018
    sprite('rg601_11', 4)	# 136019-136022
    sprite('rg601_12', 4)	# 136023-136026
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 136027-136030
    sprite('rg601_14', 4)	# 136031-136034
    sprite('rg601_15', 4)	# 136035-136038
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 136039-136042
    sprite('rg601_17', 6)	# 136043-136048
    sprite('rg601_18', 6)	# 136049-136054
    sprite('rg601_19', 3)	# 136055-136057
    sprite('rg601_20', 6)	# 136058-136063
    sprite('rg601_21', 6)	# 136064-136069
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 136070-136075
    Unknown21007(24, 40)
    Unknown21011(120)
    sprite('rg601_23', 6)	# 136076-136081
    loopRest()
    label(242)
    sprite('rg000_00', 7)	# 136082-136088
    sprite('rg000_01', 7)	# 136089-136095
    sprite('rg000_02', 7)	# 136096-136102
    sprite('rg000_03', 7)	# 136103-136109
    sprite('rg000_04', 7)	# 136110-136116
    sprite('rg000_05', 7)	# 136117-136123
    sprite('rg000_06', 7)	# 136124-136130
    sprite('rg000_05', 7)	# 136131-136137
    sprite('rg000_04', 7)	# 136138-136144
    sprite('rg000_03', 7)	# 136145-136151
    sprite('rg000_02', 7)	# 136152-136158
    sprite('rg000_01', 7)	# 136159-136165
    gotoLabel(242)
    ExitState()
    label(250)
    sprite('rg602_00', 1)	# 136166-136166
    Unknown1000(-1260000)
    Unknown2005()
    Unknown2019(100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(251)
    sprite('rg602_00', 32767)	# 136167-168933
    label(251)
    sprite('rg602_00', 1)	# 168934-168934
    SFX_1('brg601bnt')
    label(252)
    sprite('rg602_00', 1)	# 168935-168935
    if SLOT_97:
        _gotolabel(252)
    sprite('rg602_00', 10)	# 168936-168945
    sprite('rg003_00', 4)	# 168946-168949
    Unknown21007(24, 40)
    Unknown2005()
    sprite('rg003_01', 4)	# 168950-168953
    sprite('rg003_02', 4)	# 168954-168957
    sprite('rg001_00', 7)	# 168958-168964
    sprite('rg001_01', 7)	# 168965-168971
    sprite('rg001_02', 7)	# 168972-168978
    sprite('rg001_03', 7)	# 168979-168985
    sprite('rg001_04', 7)	# 168986-168992
    sprite('rg001_05', 7)	# 168993-168999
    sprite('rg001_06', 7)	# 169000-169006
    sprite('rg001_07', 7)	# 169007-169013
    sprite('rg001_08', 6)	# 169014-169019
    sprite('rg001_09', 6)	# 169020-169025
    sprite('rg001_10', 6)	# 169026-169031
    sprite('rg001_11', 6)	# 169032-169037
    sprite('rg001_12', 6)	# 169038-169043
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 169044-169049
    sprite('rg001_14', 6)	# 169050-169055
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 169056-169061
    sprite('rg001_16', 6)	# 169062-169067
    Unknown21011(30)
    label(253)
    sprite('rg000_00', 7)	# 169068-169074
    sprite('rg000_01', 7)	# 169075-169081
    sprite('rg000_02', 7)	# 169082-169088
    sprite('rg000_03', 7)	# 169089-169095
    sprite('rg000_04', 7)	# 169096-169102
    sprite('rg000_05', 7)	# 169103-169109
    sprite('rg000_06', 7)	# 169110-169116
    sprite('rg000_05', 7)	# 169117-169123
    sprite('rg000_04', 7)	# 169124-169130
    sprite('rg000_03', 7)	# 169131-169137
    sprite('rg000_02', 7)	# 169138-169144
    sprite('rg000_01', 7)	# 169145-169151
    loopRest()
    gotoLabel(253)
    label(260)
    sprite('rg000_00', 1)	# 169152-169152

    def upon_40():
        clearUponHandler(40)
        sendToLabel(262)
    label(261)
    sprite('rg000_00', 7)	# 169153-169159
    sprite('rg000_01', 7)	# 169160-169166
    sprite('rg000_02', 7)	# 169167-169173
    sprite('rg000_03', 7)	# 169174-169180
    sprite('rg000_04', 7)	# 169181-169187
    sprite('rg000_05', 7)	# 169188-169194
    sprite('rg000_06', 7)	# 169195-169201
    sprite('rg000_05', 7)	# 169202-169208
    sprite('rg000_04', 7)	# 169209-169215
    sprite('rg000_03', 7)	# 169216-169222
    sprite('rg000_02', 7)	# 169223-169229
    sprite('rg000_01', 7)	# 169230-169236
    gotoLabel(261)
    label(262)
    sprite('rg300_00', 6)	# 169237-169242
    sprite('rg300_01', 6)	# 169243-169248
    sprite('rg300_02', 6)	# 169249-169254
    sprite('rg300_03', 8)	# 169255-169262
    SFX_1('brg601ahe')
    sprite('rg300_04', 8)	# 169263-169270
    sprite('rg300_05', 20)	# 169271-169290
    label(263)
    sprite('rg300_05', 1)	# 169291-169291
    if SLOT_97:
        _gotolabel(263)
    sprite('rg300_05', 32767)	# 169292-202058
    Unknown21011(30)
    loopRest()
    label(270)
    sprite('rg601_00', 32767)	# 202059-234825

    def upon_40():
        clearUponHandler(40)
        SFX_1('brg602bsu')
        sendToLabel(271)
    label(271)
    sprite('rg601_00', 1)	# 234826-234826
    if SLOT_97:
        _gotolabel(271)
    sprite('rg601_00', 60)	# 234827-234886
    sprite('rg601_01', 6)	# 234887-234892
    sprite('rg601_02', 6)	# 234893-234898
    sprite('rg601_03', 6)	# 234899-234904
    sprite('rg601_04', 6)	# 234905-234910
    sprite('rg601_05', 6)	# 234911-234916
    sprite('rg601_06', 6)	# 234917-234922
    sprite('rg601_07', 6)	# 234923-234928
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 234929-234934
    sprite('rg601_09', 6)	# 234935-234940
    sprite('rg601_10', 6)	# 234941-234946
    sprite('rg601_11', 4)	# 234947-234950
    sprite('rg601_12', 4)	# 234951-234954
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 234955-234958
    sprite('rg601_14', 4)	# 234959-234962
    sprite('rg601_15', 4)	# 234963-234966
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 234967-234970
    sprite('rg601_17', 6)	# 234971-234976
    sprite('rg601_18', 6)	# 234977-234982
    sprite('rg601_19', 3)	# 234983-234985
    sprite('rg601_20', 6)	# 234986-234991
    sprite('rg601_21', 6)	# 234992-234997
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 234998-235003
    sprite('rg601_23', 6)	# 235004-235009
    Unknown21011(30)
    label(272)
    sprite('rg000_00', 7)	# 235010-235016
    sprite('rg000_01', 7)	# 235017-235023
    sprite('rg000_02', 7)	# 235024-235030
    sprite('rg000_03', 7)	# 235031-235037
    sprite('rg000_04', 7)	# 235038-235044
    sprite('rg000_05', 7)	# 235045-235051
    sprite('rg000_06', 7)	# 235052-235058
    sprite('rg000_05', 7)	# 235059-235065
    sprite('rg000_04', 7)	# 235066-235072
    sprite('rg000_03', 7)	# 235073-235079
    sprite('rg000_02', 7)	# 235080-235086
    sprite('rg000_01', 7)	# 235087-235093
    gotoLabel(272)
    label(280)
    sprite('rg601_00', 6)	# 235094-235099
    Unknown1000(-1230000)
    sprite('rg601_00', 1)	# 235100-235100
    SFX_1('brg600uak')
    label(281)
    sprite('rg601_00', 1)	# 235101-235101
    if SLOT_97:
        _gotolabel(281)
    sprite('rg601_01', 6)	# 235102-235107
    sprite('rg601_02', 6)	# 235108-235113
    sprite('rg601_03', 6)	# 235114-235119
    sprite('rg601_04', 6)	# 235120-235125
    sprite('rg601_05', 6)	# 235126-235131
    sprite('rg601_06', 6)	# 235132-235137
    sprite('rg601_07', 6)	# 235138-235143
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 235144-235149
    sprite('rg601_09', 6)	# 235150-235155
    sprite('rg601_10', 6)	# 235156-235161
    sprite('rg601_11', 4)	# 235162-235165
    sprite('rg601_12', 4)	# 235166-235169
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 235170-235173
    sprite('rg601_14', 4)	# 235174-235177
    sprite('rg601_15', 4)	# 235178-235181
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 235182-235185
    sprite('rg601_17', 6)	# 235186-235191
    sprite('rg601_18', 6)	# 235192-235197
    sprite('rg601_19', 3)	# 235198-235200
    sprite('rg601_20', 6)	# 235201-235206
    sprite('rg601_21', 6)	# 235207-235212
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 235213-235218
    Unknown21007(24, 40)
    Unknown21011(30)
    sprite('rg601_23', 6)	# 235219-235224
    loopRest()
    label(282)
    sprite('rg000_00', 7)	# 235225-235231
    sprite('rg000_01', 7)	# 235232-235238
    sprite('rg000_02', 7)	# 235239-235245
    sprite('rg000_03', 7)	# 235246-235252
    sprite('rg000_04', 7)	# 235253-235259
    sprite('rg000_05', 7)	# 235260-235266
    sprite('rg000_06', 7)	# 235267-235273
    sprite('rg000_05', 7)	# 235274-235280
    sprite('rg000_04', 7)	# 235281-235287
    sprite('rg000_03', 7)	# 235288-235294
    sprite('rg000_02', 7)	# 235295-235301
    sprite('rg000_01', 7)	# 235302-235308
    gotoLabel(282)
    ExitState()
    label(290)
    sprite('rg601_00', 32767)	# 235309-268075

    def upon_40():
        clearUponHandler(40)
        sendToLabel(291)
    label(291)
    sprite('rg601_00', 1)	# 268076-268076
    SFX_1('brg601kym')
    label(292)
    sprite('rg601_00', 1)	# 268077-268077
    if SLOT_97:
        _gotolabel(292)
    sprite('rg601_00', 30)	# 268078-268107
    sprite('rg601_01', 6)	# 268108-268113
    sprite('rg601_02', 6)	# 268114-268119
    sprite('rg601_03', 6)	# 268120-268125
    sprite('rg601_04', 6)	# 268126-268131
    sprite('rg601_05', 6)	# 268132-268137
    sprite('rg601_06', 6)	# 268138-268143
    sprite('rg601_07', 6)	# 268144-268149
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 268150-268155
    sprite('rg601_09', 6)	# 268156-268161
    sprite('rg601_10', 6)	# 268162-268167
    sprite('rg601_11', 4)	# 268168-268171
    sprite('rg601_12', 4)	# 268172-268175
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 268176-268179
    sprite('rg601_14', 4)	# 268180-268183
    sprite('rg601_15', 4)	# 268184-268187
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 268188-268191
    sprite('rg601_17', 6)	# 268192-268197
    sprite('rg601_18', 6)	# 268198-268203
    sprite('rg601_19', 3)	# 268204-268206
    sprite('rg601_20', 6)	# 268207-268212
    sprite('rg601_21', 6)	# 268213-268218
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 268219-268224
    sprite('rg601_23', 6)	# 268225-268230
    Unknown21011(30)
    label(293)
    sprite('rg000_00', 7)	# 268231-268237
    sprite('rg000_01', 7)	# 268238-268244
    sprite('rg000_02', 7)	# 268245-268251
    sprite('rg000_03', 7)	# 268252-268258
    sprite('rg000_04', 7)	# 268259-268265
    sprite('rg000_05', 7)	# 268266-268272
    sprite('rg000_06', 7)	# 268273-268279
    sprite('rg000_05', 7)	# 268280-268286
    sprite('rg000_04', 7)	# 268287-268293
    sprite('rg000_03', 7)	# 268294-268300
    sprite('rg000_02', 7)	# 268301-268307
    sprite('rg000_01', 7)	# 268308-268314
    gotoLabel(293)
    label(1000)
    sprite('rg601_00', 32767)	# 268315-301081
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 10001):
            SFX_1('brg601')

            def upon_CLEAR_OR_EXIT():
                if (not SLOT_97):
                    clearUponHandler(3)
                    Unknown23029(24, 10005, 0)
                    Unknown23029(22, 10005, 0)
                    Unknown23029(23, 10005, 0)
                    sendToLabel(1001)
        if (SLOT_48 == 10004):
            clearUponHandler(43)
            Unknown18008()
    label(1001)
    sprite('rg601_01', 6)	# 301082-301087
    sprite('rg601_02', 6)	# 301088-301093
    sprite('rg601_03', 6)	# 301094-301099
    sprite('rg601_04', 6)	# 301100-301105
    sprite('rg601_05', 6)	# 301106-301111
    sprite('rg601_06', 6)	# 301112-301117
    sprite('rg601_07', 6)	# 301118-301123
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 301124-301129
    sprite('rg601_09', 6)	# 301130-301135
    sprite('rg601_10', 6)	# 301136-301141
    sprite('rg601_11', 4)	# 301142-301145
    sprite('rg601_12', 4)	# 301146-301149
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 301150-301153
    sprite('rg601_14', 4)	# 301154-301157
    sprite('rg601_15', 4)	# 301158-301161
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 301162-301165
    sprite('rg601_17', 6)	# 301166-301171
    sprite('rg601_18', 6)	# 301172-301177
    sprite('rg601_19', 3)	# 301178-301180
    sprite('rg601_20', 6)	# 301181-301186
    sprite('rg601_21', 6)	# 301187-301192
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 301193-301198
    sprite('rg601_23', 6)	# 301199-301204
    Unknown23029(24, 10002, 0)
    Unknown23029(22, 10002, 0)
    Unknown23029(23, 10002, 0)
    label(1002)
    sprite('rg000_00', 7)	# 301205-301211
    sprite('rg000_01', 7)	# 301212-301218
    sprite('rg000_02', 7)	# 301219-301225
    sprite('rg000_03', 7)	# 301226-301232
    sprite('rg000_04', 7)	# 301233-301239
    sprite('rg000_05', 7)	# 301240-301246
    sprite('rg000_06', 7)	# 301247-301253
    sprite('rg000_05', 7)	# 301254-301260
    sprite('rg000_04', 7)	# 301261-301267
    sprite('rg000_03', 7)	# 301268-301274
    sprite('rg000_02', 7)	# 301275-301281
    sprite('rg000_01', 7)	# 301282-301288
    gotoLabel(1002)
    label(991)
    sprite('rg000_00', 1)	# 301289-301289
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('rg000_00', 7)	# 301290-301296
    sprite('rg000_01', 7)	# 301297-301303
    sprite('rg000_02', 7)	# 301304-301310
    sprite('rg000_03', 7)	# 301311-301317
    sprite('rg000_04', 7)	# 301318-301324
    sprite('rg000_05', 7)	# 301325-301331
    sprite('rg000_06', 7)	# 301332-301338
    sprite('rg000_05', 7)	# 301339-301345
    sprite('rg000_04', 7)	# 301346-301352
    sprite('rg000_03', 7)	# 301353-301359
    sprite('rg000_02', 7)	# 301360-301366
    sprite('rg000_01', 7)	# 301367-301373
    gotoLabel(992)
    label(993)
    sprite('rg033_00', 1)	# 301374-301374

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
    SFX_3('rgse_00')
    sprite('rg033_01', 2)	# 301375-301376
    label(994)
    sprite('rg033_02', 3)	# 301377-301379
    sprite('rg033_03', 3)	# 301380-301382
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 301383-301385
    ExitState()

@State
def CmnActRoundWin():
    sprite('rg300_00', 6)	# 1-6
    sprite('rg300_01', 6)	# 7-12
    sprite('rg300_02', 6)	# 13-18
    sprite('rg300_03', 8)	# 19-26
    if random_(2, 0, 50):
        SFX_1('rg400')
    else:
        SFX_1('rg401')
    Unknown23018(1)
    sprite('rg300_04', 8)	# 27-34
    sprite('rg300_05', 20)	# 35-54
    label(1)
    sprite('rg300_05', 1)	# 55-55
    if SLOT_97:
        _gotolabel(1)
    sprite('rg300_05', 32767)	# 56-32822
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
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('bjb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
            if PartnerChar('bce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(240)
                    clearUponHandler(3)
            if PartnerChar('bnt'):
                if (SLOT_145 <= 500000):
                    sendToLabel(250)
                    clearUponHandler(3)
            if PartnerChar('ahe'):
                if (SLOT_145 <= 500000):
                    sendToLabel(260)
                    clearUponHandler(3)
            if PartnerChar('bsu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(270)
                    clearUponHandler(3)
            if PartnerChar('uak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(280)
                    clearUponHandler(3)
            if PartnerChar('kym'):
                if (SLOT_145 <= 500000):
                    sendToLabel(290)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    if SLOT_61:
        _gotolabel(0)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('rg610_00', 1)	# 4-4
    sprite('rg610_00', 3)	# 5-7
    sprite('rg610_01', 3)	# 8-10
    sprite('rg610_02', 3)	# 11-13
    if (not SLOT_61):
        if SLOT_158:
            if SLOT_52:
                Unknown7006('brg524', 100, 895971938, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            elif SLOT_108:
                Unknown7006('brg402_0', 100, 879194722, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown7006('brg520', 100, 895971938, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_0('007_swing_knife_1')
    GFX_0('rgef610wingmake', -1)
    sprite('rg610_03', 3)	# 14-16
    sprite('rg610_04', 3)	# 17-19
    sprite('rg610_05', 3)	# 20-22
    sprite('rg610_06', 6)	# 23-28
    sprite('rg610_07', 2)	# 29-30
    GFX_0('rgef610wingbreak', -1)
    SFX_0('019_cloth_c')
    loopRest()
    sprite('rg610_08', 6)	# 31-36
    SFX_0('210_down_garden_1')
    Unknown23018(1)
    sprite('rg610_09', 6)	# 37-42
    sprite('rg610_10', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg610_11', 32767)	# 49-32815
    label(10)
    sprite('rg611_00', 5)	# 32816-32820
    sprite('rg611_01', 4)	# 32821-32824
    sprite('rg611_02', 10)	# 32825-32834
    sprite('rg611_03', 3)	# 32835-32837
    sprite('rg611_04', 8)	# 32838-32845	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 32846-32849	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 32850-32853	 **attackbox here**
    sprite('rg611_07', 6)	# 32854-32859	 **attackbox here**
    sprite('rg611_08', 6)	# 32860-32865	 **attackbox here**
    sprite('rg611_09', 6)	# 32866-32871	 **attackbox here**
    sprite('rg611_10', 6)	# 32872-32877	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 32878-32883	 **attackbox here**
    sprite('rg611_12', 6)	# 32884-32889	 **attackbox here**
    sprite('rg611_13', 6)	# 32890-32895	 **attackbox here**
    sprite('rg611_14', 6)	# 32896-32901	 **attackbox here**
    sprite('rg611_15', 6)	# 32902-32907	 **attackbox here**
    sprite('rg611_16', 6)	# 32908-32913	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('brg524', 100, 895971938, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('brg402_0', 100, 879194722, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('', 0, 0, 0, 0, 0, 0, 895971938, 12850, 0, 0, 100, 895971938, 13106, 0, 0, 100)
    Unknown23018(1)
    sprite('rg611_17', 6)	# 32914-32919	 **attackbox here**
    sprite('rg611_14', 6)	# 32920-32925	 **attackbox here**
    sprite('rg611_15', 6)	# 32926-32931	 **attackbox here**
    sprite('rg611_16', 6)	# 32932-32937	 **attackbox here**
    sprite('rg611_17', 6)	# 32938-32943	 **attackbox here**
    sprite('rg611_14', 6)	# 32944-32949	 **attackbox here**
    sprite('rg611_15', 6)	# 32950-32955	 **attackbox here**
    sprite('rg611_16', 6)	# 32956-32961	 **attackbox here**
    sprite('rg611_17', 6)	# 32962-32967	 **attackbox here**
    sprite('rg611_14', 6)	# 32968-32973	 **attackbox here**
    sprite('rg611_15', 6)	# 32974-32979	 **attackbox here**
    sprite('rg611_16', 6)	# 32980-32985	 **attackbox here**
    sprite('rg611_17', 6)	# 32986-32991	 **attackbox here**
    label(2)
    sprite('rg611_14', 6)	# 32992-32997	 **attackbox here**
    sprite('rg611_15', 6)	# 32998-33003	 **attackbox here**
    sprite('rg611_16', 6)	# 33004-33009	 **attackbox here**
    sprite('rg611_17', 6)	# 33010-33015	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(100)
    sprite('rg000_00', 7)	# 33016-33022
    sprite('rg000_01', 7)	# 33023-33029
    sprite('rg000_02', 7)	# 33030-33036
    sprite('rg000_03', 7)	# 33037-33043
    sprite('rg000_04', 7)	# 33044-33050
    sprite('rg000_05', 7)	# 33051-33057
    sprite('rg000_06', 7)	# 33058-33064
    sprite('rg000_05', 7)	# 33065-33071
    sprite('rg000_04', 7)	# 33072-33078
    sprite('rg000_03', 7)	# 33079-33085
    sprite('rg000_02', 7)	# 33086-33092
    sprite('rg000_01', 7)	# 33093-33099
    sprite('rg032_11', 3)	# 33100-33102
    physicsXImpulse(8000)
    Unknown2053(0)
    Unknown2034(0)
    sprite('rg032_00', 4)	# 33103-33106
    SFX_1('brg700bjn')
    sprite('rg032_01', 4)	# 33107-33110
    physicsXImpulse(28000)
    label(101)
    sprite('rg032_02', 4)	# 33111-33114
    if (SLOT_145 >= 3000000):
        Unknown1084(1)
        sendToLabel(102)
        Unknown21011(420)
    sprite('rg032_03', 4)	# 33115-33118
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 33119-33122
    sprite('rg032_04', 4)	# 33123-33126
    sprite('rg032_05', 4)	# 33127-33130
    sprite('rg032_06', 4)	# 33131-33134
    Unknown8006(100, 1, 1)
    sprite('rg032_06add', 4)	# 33135-33138
    sprite('rg032_07', 4)	# 33139-33142
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('rg000_00', 7)	# 33143-33149
    sprite('rg000_01', 7)	# 33150-33156
    sprite('rg000_02', 7)	# 33157-33163
    sprite('rg000_03', 7)	# 33164-33170
    sprite('rg000_04', 7)	# 33171-33177
    sprite('rg000_05', 7)	# 33178-33184
    sprite('rg000_06', 7)	# 33185-33191
    sprite('rg000_05', 7)	# 33192-33198
    sprite('rg000_04', 7)	# 33199-33205
    sprite('rg000_03', 7)	# 33206-33212
    sprite('rg000_02', 7)	# 33213-33219
    sprite('rg000_01', 7)	# 33220-33226
    gotoLabel(102)
    label(110)
    sprite('rg000_00', 1)	# 33227-33227

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('rg000_00', 7)	# 33228-33234
    sprite('rg000_01', 7)	# 33235-33241
    sprite('rg000_02', 7)	# 33242-33248
    sprite('rg000_03', 7)	# 33249-33255
    sprite('rg000_04', 7)	# 33256-33262
    sprite('rg000_05', 7)	# 33263-33269
    sprite('rg000_06', 7)	# 33270-33276
    sprite('rg000_05', 7)	# 33277-33283
    sprite('rg000_04', 7)	# 33284-33290
    sprite('rg000_03', 7)	# 33291-33297
    sprite('rg000_02', 7)	# 33298-33304
    sprite('rg000_01', 7)	# 33305-33311
    gotoLabel(111)
    label(112)
    sprite('rg300_00', 6)	# 33312-33317
    SFX_1('brg701rrb')
    sprite('rg300_01', 6)	# 33318-33323
    sprite('rg300_02', 6)	# 33324-33329
    sprite('rg300_03', 8)	# 33330-33337
    sprite('rg300_04', 8)	# 33338-33345
    sprite('rg300_05', 20)	# 33346-33365
    sprite('rg300_05', 32767)	# 33366-66132
    Unknown23018(1)
    label(120)
    sprite('rg000_00', 1)	# 66133-66133

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('rg000_00', 7)	# 66134-66140
    sprite('rg000_01', 7)	# 66141-66147
    sprite('rg000_02', 7)	# 66148-66154
    sprite('rg000_03', 7)	# 66155-66161
    sprite('rg000_04', 7)	# 66162-66168
    sprite('rg000_05', 7)	# 66169-66175
    sprite('rg000_06', 7)	# 66176-66182
    sprite('rg000_05', 7)	# 66183-66189
    sprite('rg000_04', 7)	# 66190-66196
    sprite('rg000_03', 7)	# 66197-66203
    sprite('rg000_02', 7)	# 66204-66210
    sprite('rg000_01', 7)	# 66211-66217
    gotoLabel(121)
    label(122)
    sprite('rg300_00', 6)	# 66218-66223
    SFX_1('brg701bny')
    sprite('rg300_01', 6)	# 66224-66229
    sprite('rg300_02', 6)	# 66230-66235
    sprite('rg300_03', 8)	# 66236-66243
    sprite('rg300_04', 8)	# 66244-66251
    sprite('rg300_05', 20)	# 66252-66271
    sprite('rg300_05', 32767)	# 66272-99038
    Unknown23018(1)
    label(130)
    sprite('rg000_00', 1)	# 99039-99039
    if (not SLOT_158):
        Unknown2019(-1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('rg000_00', 7)	# 99040-99046
    sprite('rg000_01', 7)	# 99047-99053
    sprite('rg000_02', 7)	# 99054-99060
    sprite('rg000_03', 7)	# 99061-99067
    sprite('rg000_04', 7)	# 99068-99074
    sprite('rg000_05', 7)	# 99075-99081
    sprite('rg000_06', 7)	# 99082-99088
    sprite('rg000_05', 7)	# 99089-99095
    sprite('rg000_04', 7)	# 99096-99102
    sprite('rg000_03', 7)	# 99103-99109
    sprite('rg000_02', 7)	# 99110-99116
    sprite('rg000_01', 7)	# 99117-99123
    gotoLabel(131)
    label(132)
    sprite('rg611_00', 5)	# 99124-99128
    sprite('rg611_01', 4)	# 99129-99132
    sprite('rg611_02', 10)	# 99133-99142
    sprite('rg611_03', 3)	# 99143-99145
    sprite('rg611_04', 8)	# 99146-99153	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 99154-99157	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 99158-99161	 **attackbox here**
    sprite('rg611_07', 6)	# 99162-99167	 **attackbox here**
    sprite('rg611_08', 6)	# 99168-99173	 **attackbox here**
    sprite('rg611_09', 6)	# 99174-99179	 **attackbox here**
    sprite('rg611_10', 6)	# 99180-99185	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 99186-99191	 **attackbox here**
    sprite('rg611_12', 6)	# 99192-99197	 **attackbox here**
    sprite('rg611_13', 6)	# 99198-99203	 **attackbox here**
    sprite('rg611_14', 6)	# 99204-99209	 **attackbox here**
    sprite('rg611_15', 6)	# 99210-99215	 **attackbox here**
    sprite('rg611_16', 6)	# 99216-99221	 **attackbox here**
    SFX_1('brg701brc')
    sprite('rg611_17', 6)	# 99222-99227	 **attackbox here**
    sprite('rg611_14', 6)	# 99228-99233	 **attackbox here**
    sprite('rg611_15', 6)	# 99234-99239	 **attackbox here**
    sprite('rg611_16', 6)	# 99240-99245	 **attackbox here**
    sprite('rg611_17', 6)	# 99246-99251	 **attackbox here**
    sprite('rg611_14', 6)	# 99252-99257	 **attackbox here**
    sprite('rg611_15', 6)	# 99258-99263	 **attackbox here**
    sprite('rg611_16', 6)	# 99264-99269	 **attackbox here**
    sprite('rg611_17', 6)	# 99270-99275	 **attackbox here**
    sprite('rg611_14', 6)	# 99276-99281	 **attackbox here**
    sprite('rg611_15', 6)	# 99282-99287	 **attackbox here**
    sprite('rg611_16', 6)	# 99288-99293	 **attackbox here**
    sprite('rg611_17', 6)	# 99294-99299	 **attackbox here**
    Unknown23018(1)
    label(133)
    sprite('rg611_14', 6)	# 99300-99305	 **attackbox here**
    sprite('rg611_15', 6)	# 99306-99311	 **attackbox here**
    sprite('rg611_16', 6)	# 99312-99317	 **attackbox here**
    sprite('rg611_17', 6)	# 99318-99323	 **attackbox here**
    loopRest()
    gotoLabel(133)
    label(140)
    sprite('rg000_00', 1)	# 99324-99324

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('rg000_00', 7)	# 99325-99331
    sprite('rg000_01', 7)	# 99332-99338
    sprite('rg000_02', 7)	# 99339-99345
    sprite('rg000_03', 7)	# 99346-99352
    sprite('rg000_04', 7)	# 99353-99359
    sprite('rg000_05', 7)	# 99360-99366
    sprite('rg000_06', 7)	# 99367-99373
    sprite('rg000_05', 7)	# 99374-99380
    sprite('rg000_04', 7)	# 99381-99387
    sprite('rg000_03', 7)	# 99388-99394
    sprite('rg000_02', 7)	# 99395-99401
    sprite('rg000_01', 7)	# 99402-99408
    gotoLabel(141)
    label(142)
    sprite('rg611_00', 5)	# 99409-99413
    sprite('rg611_01', 4)	# 99414-99417
    sprite('rg611_02', 10)	# 99418-99427
    sprite('rg611_03', 3)	# 99428-99430
    sprite('rg611_04', 8)	# 99431-99438	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 99439-99442	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 99443-99446	 **attackbox here**
    sprite('rg611_07', 6)	# 99447-99452	 **attackbox here**
    sprite('rg611_08', 6)	# 99453-99458	 **attackbox here**
    sprite('rg611_09', 6)	# 99459-99464	 **attackbox here**
    sprite('rg611_10', 6)	# 99465-99470	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 99471-99476	 **attackbox here**
    sprite('rg611_12', 6)	# 99477-99482	 **attackbox here**
    sprite('rg611_13', 6)	# 99483-99488	 **attackbox here**
    sprite('rg611_14', 6)	# 99489-99494	 **attackbox here**
    sprite('rg611_15', 6)	# 99495-99500	 **attackbox here**
    sprite('rg611_16', 6)	# 99501-99506	 **attackbox here**
    SFX_1('brg701uhy')
    sprite('rg611_17', 6)	# 99507-99512	 **attackbox here**
    sprite('rg611_14', 6)	# 99513-99518	 **attackbox here**
    sprite('rg611_15', 6)	# 99519-99524	 **attackbox here**
    sprite('rg611_16', 6)	# 99525-99530	 **attackbox here**
    sprite('rg611_17', 6)	# 99531-99536	 **attackbox here**
    sprite('rg611_14', 6)	# 99537-99542	 **attackbox here**
    sprite('rg611_15', 6)	# 99543-99548	 **attackbox here**
    sprite('rg611_16', 6)	# 99549-99554	 **attackbox here**
    sprite('rg611_17', 6)	# 99555-99560	 **attackbox here**
    sprite('rg611_14', 6)	# 99561-99566	 **attackbox here**
    sprite('rg611_15', 6)	# 99567-99572	 **attackbox here**
    sprite('rg611_16', 6)	# 99573-99578	 **attackbox here**
    sprite('rg611_17', 6)	# 99579-99584	 **attackbox here**
    Unknown23018(1)
    label(143)
    sprite('rg611_14', 6)	# 99585-99590	 **attackbox here**
    sprite('rg611_15', 6)	# 99591-99596	 **attackbox here**
    sprite('rg611_16', 6)	# 99597-99602	 **attackbox here**
    sprite('rg611_17', 6)	# 99603-99608	 **attackbox here**
    loopRest()
    gotoLabel(143)
    label(150)
    sprite('rg611_00', 5)	# 99609-99613
    sprite('rg611_01', 4)	# 99614-99617
    sprite('rg611_02', 10)	# 99618-99627
    sprite('rg611_03', 3)	# 99628-99630
    sprite('rg611_04', 8)	# 99631-99638	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 99639-99642	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 99643-99646	 **attackbox here**
    sprite('rg611_07', 6)	# 99647-99652	 **attackbox here**
    sprite('rg611_08', 6)	# 99653-99658	 **attackbox here**
    sprite('rg611_09', 6)	# 99659-99664	 **attackbox here**
    sprite('rg611_10', 6)	# 99665-99670	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 99671-99676	 **attackbox here**
    sprite('rg611_12', 6)	# 99677-99682	 **attackbox here**
    sprite('rg611_13', 6)	# 99683-99688	 **attackbox here**
    sprite('rg611_14', 6)	# 99689-99694	 **attackbox here**
    sprite('rg611_15', 6)	# 99695-99700	 **attackbox here**
    sprite('rg611_16', 6)	# 99701-99706	 **attackbox here**
    SFX_1('brg700pbc')
    sprite('rg611_17', 6)	# 99707-99712	 **attackbox here**
    sprite('rg611_14', 6)	# 99713-99718	 **attackbox here**
    sprite('rg611_15', 6)	# 99719-99724	 **attackbox here**
    sprite('rg611_16', 6)	# 99725-99730	 **attackbox here**
    sprite('rg611_17', 6)	# 99731-99736	 **attackbox here**
    sprite('rg611_14', 6)	# 99737-99742	 **attackbox here**
    sprite('rg611_15', 6)	# 99743-99748	 **attackbox here**
    sprite('rg611_16', 6)	# 99749-99754	 **attackbox here**
    sprite('rg611_17', 6)	# 99755-99760	 **attackbox here**
    sprite('rg611_14', 6)	# 99761-99766	 **attackbox here**
    sprite('rg611_15', 6)	# 99767-99772	 **attackbox here**
    sprite('rg611_16', 6)	# 99773-99778	 **attackbox here**
    sprite('rg611_17', 6)	# 99779-99784	 **attackbox here**
    label(151)
    sprite('rg611_14', 6)	# 99785-99790	 **attackbox here**
    sprite('rg611_15', 6)	# 99791-99796	 **attackbox here**
    sprite('rg611_16', 6)	# 99797-99802	 **attackbox here**
    sprite('rg611_17', 6)	# 99803-99808	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('rg611_14', 1)	# 99809-99809	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(152)
    sprite('rg611_14', 6)	# 99810-99815	 **attackbox here**
    sprite('rg611_15', 6)	# 99816-99821	 **attackbox here**
    sprite('rg611_16', 6)	# 99822-99827	 **attackbox here**
    sprite('rg611_17', 6)	# 99828-99833	 **attackbox here**
    gotoLabel(152)
    label(160)
    sprite('rg000_00', 1)	# 99834-99834

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('rg000_00', 7)	# 99835-99841
    sprite('rg000_01', 7)	# 99842-99848
    sprite('rg000_02', 7)	# 99849-99855
    sprite('rg000_03', 7)	# 99856-99862
    sprite('rg000_04', 7)	# 99863-99869
    sprite('rg000_05', 7)	# 99870-99876
    sprite('rg000_06', 7)	# 99877-99883
    sprite('rg000_05', 7)	# 99884-99890
    sprite('rg000_04', 7)	# 99891-99897
    sprite('rg000_03', 7)	# 99898-99904
    sprite('rg000_02', 7)	# 99905-99911
    sprite('rg000_01', 7)	# 99912-99918
    gotoLabel(161)
    label(162)
    sprite('rg611_00', 5)	# 99919-99923
    sprite('rg611_01', 4)	# 99924-99927
    sprite('rg611_02', 10)	# 99928-99937
    sprite('rg611_03', 3)	# 99938-99940
    sprite('rg611_04', 8)	# 99941-99948	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 99949-99952	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 99953-99956	 **attackbox here**
    sprite('rg611_07', 6)	# 99957-99962	 **attackbox here**
    sprite('rg611_08', 6)	# 99963-99968	 **attackbox here**
    sprite('rg611_09', 6)	# 99969-99974	 **attackbox here**
    sprite('rg611_10', 6)	# 99975-99980	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 99981-99986	 **attackbox here**
    sprite('rg611_12', 6)	# 99987-99992	 **attackbox here**
    sprite('rg611_13', 6)	# 99993-99998	 **attackbox here**
    sprite('rg611_14', 6)	# 99999-100004	 **attackbox here**
    sprite('rg611_15', 6)	# 100005-100010	 **attackbox here**
    sprite('rg611_16', 6)	# 100011-100016	 **attackbox here**
    SFX_1('brg701bno')
    sprite('rg611_17', 6)	# 100017-100022	 **attackbox here**
    sprite('rg611_14', 6)	# 100023-100028	 **attackbox here**
    sprite('rg611_15', 6)	# 100029-100034	 **attackbox here**
    sprite('rg611_16', 6)	# 100035-100040	 **attackbox here**
    sprite('rg611_17', 6)	# 100041-100046	 **attackbox here**
    sprite('rg611_14', 6)	# 100047-100052	 **attackbox here**
    sprite('rg611_15', 6)	# 100053-100058	 **attackbox here**
    sprite('rg611_16', 6)	# 100059-100064	 **attackbox here**
    sprite('rg611_17', 6)	# 100065-100070	 **attackbox here**
    sprite('rg611_14', 6)	# 100071-100076	 **attackbox here**
    sprite('rg611_15', 6)	# 100077-100082	 **attackbox here**
    sprite('rg611_16', 6)	# 100083-100088	 **attackbox here**
    sprite('rg611_17', 6)	# 100089-100094	 **attackbox here**
    Unknown23018(1)
    label(163)
    sprite('rg611_14', 6)	# 100095-100100	 **attackbox here**
    sprite('rg611_15', 6)	# 100101-100106	 **attackbox here**
    sprite('rg611_16', 6)	# 100107-100112	 **attackbox here**
    sprite('rg611_17', 6)	# 100113-100118	 **attackbox here**
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('rg000_00', 1)	# 100119-100119

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('rg000_00', 7)	# 100120-100126
    sprite('rg000_01', 7)	# 100127-100133
    sprite('rg000_02', 7)	# 100134-100140
    sprite('rg000_03', 7)	# 100141-100147
    sprite('rg000_04', 7)	# 100148-100154
    sprite('rg000_05', 7)	# 100155-100161
    sprite('rg000_06', 7)	# 100162-100168
    sprite('rg000_05', 7)	# 100169-100175
    sprite('rg000_04', 7)	# 100176-100182
    sprite('rg000_03', 7)	# 100183-100189
    sprite('rg000_02', 7)	# 100190-100196
    sprite('rg000_01', 7)	# 100197-100203
    gotoLabel(171)
    label(172)
    sprite('rg300_00', 6)	# 100204-100209
    SFX_1('brg701bha')
    sprite('rg300_01', 6)	# 100210-100215
    sprite('rg300_02', 6)	# 100216-100221
    sprite('rg300_03', 8)	# 100222-100229
    sprite('rg300_04', 8)	# 100230-100237
    sprite('rg300_05', 20)	# 100238-100257
    sprite('rg300_05', 32767)	# 100258-133024
    Unknown23018(1)
    label(180)
    sprite('rg610_00', 1)	# 133025-133025
    sprite('rg610_00', 3)	# 133026-133028
    sprite('rg610_01', 3)	# 133029-133031
    sprite('rg610_02', 3)	# 133032-133034
    SFX_1('brg700rbl')
    SFX_0('007_swing_knife_1')
    GFX_0('rgef610wingmake', -1)
    sprite('rg610_03', 3)	# 133035-133037
    sprite('rg610_04', 3)	# 133038-133040
    sprite('rg610_05', 3)	# 133041-133043
    sprite('rg610_06', 6)	# 133044-133049
    sprite('rg610_07', 2)	# 133050-133051
    GFX_0('rgef610wingbreak', -1)
    SFX_0('019_cloth_c')
    sprite('rg610_08', 6)	# 133052-133057
    SFX_0('210_down_garden_1')
    sprite('rg610_09', 6)	# 133058-133063
    sprite('rg610_10', 6)	# 133064-133069
    SFX_FOOTSTEP_(100, 1, 1)
    label(181)
    sprite('rg610_11', 1)	# 133070-133070
    if SLOT_97:
        _gotolabel(181)
    sprite('rg610_11', 15)	# 133071-133085
    sprite('rg610_11', 32767)	# 133086-165852
    Unknown21007(24, 40)
    Unknown21011(240)
    label(190)
    sprite('rg000_00', 1)	# 165853-165853

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('rg000_00', 7)	# 165854-165860
    sprite('rg000_01', 7)	# 165861-165867
    sprite('rg000_02', 7)	# 165868-165874
    sprite('rg000_03', 7)	# 165875-165881
    sprite('rg000_04', 7)	# 165882-165888
    sprite('rg000_05', 7)	# 165889-165895
    sprite('rg000_06', 7)	# 165896-165902
    sprite('rg000_05', 7)	# 165903-165909
    sprite('rg000_04', 7)	# 165910-165916
    sprite('rg000_03', 7)	# 165917-165923
    sprite('rg000_02', 7)	# 165924-165930
    sprite('rg000_01', 7)	# 165931-165937
    gotoLabel(191)
    label(192)
    sprite('rg611_00', 5)	# 165938-165942
    sprite('rg611_01', 4)	# 165943-165946
    sprite('rg611_02', 10)	# 165947-165956
    sprite('rg611_03', 3)	# 165957-165959
    sprite('rg611_04', 8)	# 165960-165967	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 165968-165971	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 165972-165975	 **attackbox here**
    sprite('rg611_07', 6)	# 165976-165981	 **attackbox here**
    sprite('rg611_08', 6)	# 165982-165987	 **attackbox here**
    sprite('rg611_09', 6)	# 165988-165993	 **attackbox here**
    sprite('rg611_10', 6)	# 165994-165999	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 166000-166005	 **attackbox here**
    sprite('rg611_12', 6)	# 166006-166011	 **attackbox here**
    sprite('rg611_13', 6)	# 166012-166017	 **attackbox here**
    sprite('rg611_14', 6)	# 166018-166023	 **attackbox here**
    sprite('rg611_15', 6)	# 166024-166029	 **attackbox here**
    sprite('rg611_16', 6)	# 166030-166035	 **attackbox here**
    SFX_1('brg701bjb')
    sprite('rg611_17', 6)	# 166036-166041	 **attackbox here**
    sprite('rg611_14', 6)	# 166042-166047	 **attackbox here**
    sprite('rg611_15', 6)	# 166048-166053	 **attackbox here**
    sprite('rg611_16', 6)	# 166054-166059	 **attackbox here**
    sprite('rg611_17', 6)	# 166060-166065	 **attackbox here**
    sprite('rg611_14', 6)	# 166066-166071	 **attackbox here**
    sprite('rg611_15', 6)	# 166072-166077	 **attackbox here**
    sprite('rg611_16', 6)	# 166078-166083	 **attackbox here**
    sprite('rg611_17', 6)	# 166084-166089	 **attackbox here**
    sprite('rg611_14', 6)	# 166090-166095	 **attackbox here**
    sprite('rg611_15', 6)	# 166096-166101	 **attackbox here**
    sprite('rg611_16', 6)	# 166102-166107	 **attackbox here**
    sprite('rg611_17', 6)	# 166108-166113	 **attackbox here**
    Unknown23018(1)
    label(193)
    sprite('rg611_14', 6)	# 166114-166119	 **attackbox here**
    sprite('rg611_15', 6)	# 166120-166125	 **attackbox here**
    sprite('rg611_16', 6)	# 166126-166131	 **attackbox here**
    sprite('rg611_17', 6)	# 166132-166137	 **attackbox here**
    loopRest()
    gotoLabel(193)
    label(200)
    sprite('rg000_00', 1)	# 166138-166138

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('rg000_00', 7)	# 166139-166145
    sprite('rg000_01', 7)	# 166146-166152
    sprite('rg000_02', 7)	# 166153-166159
    sprite('rg000_03', 7)	# 166160-166166
    sprite('rg000_04', 7)	# 166167-166173
    sprite('rg000_05', 7)	# 166174-166180
    sprite('rg000_06', 7)	# 166181-166187
    sprite('rg000_05', 7)	# 166188-166194
    sprite('rg000_04', 7)	# 166195-166201
    sprite('rg000_03', 7)	# 166202-166208
    sprite('rg000_02', 7)	# 166209-166215
    sprite('rg000_01', 7)	# 166216-166222
    gotoLabel(201)
    label(202)
    sprite('rg611_00', 5)	# 166223-166227
    sprite('rg611_01', 4)	# 166228-166231
    sprite('rg611_02', 10)	# 166232-166241
    sprite('rg611_03', 3)	# 166242-166244
    sprite('rg611_04', 8)	# 166245-166252	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 166253-166256	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 166257-166260	 **attackbox here**
    sprite('rg611_07', 6)	# 166261-166266	 **attackbox here**
    sprite('rg611_08', 6)	# 166267-166272	 **attackbox here**
    sprite('rg611_09', 6)	# 166273-166278	 **attackbox here**
    sprite('rg611_10', 6)	# 166279-166284	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 166285-166290	 **attackbox here**
    sprite('rg611_12', 6)	# 166291-166296	 **attackbox here**
    sprite('rg611_13', 6)	# 166297-166302	 **attackbox here**
    sprite('rg611_14', 6)	# 166303-166308	 **attackbox here**
    sprite('rg611_15', 6)	# 166309-166314	 **attackbox here**
    sprite('rg611_16', 6)	# 166315-166320	 **attackbox here**
    SFX_1('brg701baz')
    sprite('rg611_17', 6)	# 166321-166326	 **attackbox here**
    sprite('rg611_14', 6)	# 166327-166332	 **attackbox here**
    sprite('rg611_15', 6)	# 166333-166338	 **attackbox here**
    sprite('rg611_16', 6)	# 166339-166344	 **attackbox here**
    sprite('rg611_17', 6)	# 166345-166350	 **attackbox here**
    sprite('rg611_14', 6)	# 166351-166356	 **attackbox here**
    sprite('rg611_15', 6)	# 166357-166362	 **attackbox here**
    sprite('rg611_16', 6)	# 166363-166368	 **attackbox here**
    sprite('rg611_17', 6)	# 166369-166374	 **attackbox here**
    sprite('rg611_14', 6)	# 166375-166380	 **attackbox here**
    sprite('rg611_15', 6)	# 166381-166386	 **attackbox here**
    sprite('rg611_16', 6)	# 166387-166392	 **attackbox here**
    sprite('rg611_17', 6)	# 166393-166398	 **attackbox here**
    Unknown23018(1)
    label(203)
    sprite('rg611_14', 6)	# 166399-166404	 **attackbox here**
    sprite('rg611_15', 6)	# 166405-166410	 **attackbox here**
    sprite('rg611_16', 6)	# 166411-166416	 **attackbox here**
    sprite('rg611_17', 6)	# 166417-166422	 **attackbox here**
    loopRest()
    gotoLabel(203)
    label(210)
    sprite('rg000_00', 1)	# 166423-166423

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('rg000_00', 7)	# 166424-166430
    sprite('rg000_01', 7)	# 166431-166437
    sprite('rg000_02', 7)	# 166438-166444
    sprite('rg000_03', 7)	# 166445-166451
    sprite('rg000_04', 7)	# 166452-166458
    sprite('rg000_05', 7)	# 166459-166465
    sprite('rg000_06', 7)	# 166466-166472
    sprite('rg000_05', 7)	# 166473-166479
    sprite('rg000_04', 7)	# 166480-166486
    sprite('rg000_03', 7)	# 166487-166493
    sprite('rg000_02', 7)	# 166494-166500
    sprite('rg000_01', 7)	# 166501-166507
    gotoLabel(211)
    label(212)
    sprite('rg300_00', 6)	# 166508-166513
    SFX_1('brg701bpt')
    sprite('rg300_01', 6)	# 166514-166519
    sprite('rg300_02', 6)	# 166520-166525
    sprite('rg300_03', 8)	# 166526-166533
    sprite('rg300_04', 8)	# 166534-166541
    sprite('rg300_05', 32767)	# 166542-199308
    Unknown23018(1)
    label(220)
    sprite('rg000_00', 1)	# 199309-199309

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('rg000_00', 7)	# 199310-199316
    sprite('rg000_01', 7)	# 199317-199323
    sprite('rg000_02', 7)	# 199324-199330
    sprite('rg000_03', 7)	# 199331-199337
    sprite('rg000_04', 7)	# 199338-199344
    sprite('rg000_05', 7)	# 199345-199351
    sprite('rg000_06', 7)	# 199352-199358
    sprite('rg000_05', 7)	# 199359-199365
    sprite('rg000_04', 7)	# 199366-199372
    sprite('rg000_03', 7)	# 199373-199379
    sprite('rg000_02', 7)	# 199380-199386
    sprite('rg000_01', 7)	# 199387-199393
    gotoLabel(221)
    label(222)
    sprite('rg611_00', 5)	# 199394-199398
    sprite('rg611_01', 4)	# 199399-199402
    sprite('rg611_02', 10)	# 199403-199412
    sprite('rg611_03', 3)	# 199413-199415
    sprite('rg611_04', 8)	# 199416-199423	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 199424-199427	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 199428-199431	 **attackbox here**
    sprite('rg611_07', 6)	# 199432-199437	 **attackbox here**
    sprite('rg611_08', 6)	# 199438-199443	 **attackbox here**
    sprite('rg611_09', 6)	# 199444-199449	 **attackbox here**
    sprite('rg611_10', 6)	# 199450-199455	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 199456-199461	 **attackbox here**
    sprite('rg611_12', 6)	# 199462-199467	 **attackbox here**
    sprite('rg611_13', 6)	# 199468-199473	 **attackbox here**
    sprite('rg611_14', 6)	# 199474-199479	 **attackbox here**
    sprite('rg611_15', 6)	# 199480-199485	 **attackbox here**
    sprite('rg611_16', 6)	# 199486-199491	 **attackbox here**
    SFX_1('brg701uor')
    sprite('rg611_17', 6)	# 199492-199497	 **attackbox here**
    sprite('rg611_14', 6)	# 199498-199503	 **attackbox here**
    sprite('rg611_15', 6)	# 199504-199509	 **attackbox here**
    sprite('rg611_16', 6)	# 199510-199515	 **attackbox here**
    sprite('rg611_17', 6)	# 199516-199521	 **attackbox here**
    sprite('rg611_14', 6)	# 199522-199527	 **attackbox here**
    sprite('rg611_15', 6)	# 199528-199533	 **attackbox here**
    sprite('rg611_16', 6)	# 199534-199539	 **attackbox here**
    sprite('rg611_17', 6)	# 199540-199545	 **attackbox here**
    sprite('rg611_14', 6)	# 199546-199551	 **attackbox here**
    sprite('rg611_15', 6)	# 199552-199557	 **attackbox here**
    sprite('rg611_16', 6)	# 199558-199563	 **attackbox here**
    sprite('rg611_17', 6)	# 199564-199569	 **attackbox here**
    Unknown23018(1)
    label(223)
    sprite('rg611_14', 6)	# 199570-199575	 **attackbox here**
    sprite('rg611_15', 6)	# 199576-199581	 **attackbox here**
    sprite('rg611_16', 6)	# 199582-199587	 **attackbox here**
    sprite('rg611_17', 6)	# 199588-199593	 **attackbox here**
    loopRest()
    gotoLabel(223)
    label(230)
    sprite('rg000_00', 1)	# 199594-199594

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('rg000_00', 7)	# 199595-199601
    sprite('rg000_01', 7)	# 199602-199608
    sprite('rg000_02', 7)	# 199609-199615
    sprite('rg000_03', 7)	# 199616-199622
    sprite('rg000_04', 7)	# 199623-199629
    sprite('rg000_05', 7)	# 199630-199636
    sprite('rg000_06', 7)	# 199637-199643
    sprite('rg000_05', 7)	# 199644-199650
    sprite('rg000_04', 7)	# 199651-199657
    sprite('rg000_03', 7)	# 199658-199664
    sprite('rg000_02', 7)	# 199665-199671
    sprite('rg000_01', 7)	# 199672-199678
    gotoLabel(231)
    label(232)
    sprite('rg611_00', 5)	# 199679-199683
    sprite('rg611_01', 4)	# 199684-199687
    sprite('rg611_02', 10)	# 199688-199697
    sprite('rg611_03', 3)	# 199698-199700
    sprite('rg611_04', 8)	# 199701-199708	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 199709-199712	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 199713-199716	 **attackbox here**
    sprite('rg611_07', 6)	# 199717-199722	 **attackbox here**
    sprite('rg611_08', 6)	# 199723-199728	 **attackbox here**
    sprite('rg611_09', 6)	# 199729-199734	 **attackbox here**
    sprite('rg611_10', 6)	# 199735-199740	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 199741-199746	 **attackbox here**
    sprite('rg611_12', 6)	# 199747-199752	 **attackbox here**
    sprite('rg611_13', 6)	# 199753-199758	 **attackbox here**
    sprite('rg611_14', 6)	# 199759-199764	 **attackbox here**
    sprite('rg611_15', 6)	# 199765-199770	 **attackbox here**
    sprite('rg611_16', 6)	# 199771-199776	 **attackbox here**
    SFX_1('brg701pag')
    sprite('rg611_17', 6)	# 199777-199782	 **attackbox here**
    sprite('rg611_14', 6)	# 199783-199788	 **attackbox here**
    sprite('rg611_15', 6)	# 199789-199794	 **attackbox here**
    sprite('rg611_16', 6)	# 199795-199800	 **attackbox here**
    sprite('rg611_17', 6)	# 199801-199806	 **attackbox here**
    sprite('rg611_14', 6)	# 199807-199812	 **attackbox here**
    sprite('rg611_15', 6)	# 199813-199818	 **attackbox here**
    sprite('rg611_16', 6)	# 199819-199824	 **attackbox here**
    sprite('rg611_17', 6)	# 199825-199830	 **attackbox here**
    sprite('rg611_14', 6)	# 199831-199836	 **attackbox here**
    sprite('rg611_15', 6)	# 199837-199842	 **attackbox here**
    sprite('rg611_16', 6)	# 199843-199848	 **attackbox here**
    sprite('rg611_17', 6)	# 199849-199854	 **attackbox here**
    Unknown23018(1)
    label(233)
    sprite('rg611_14', 6)	# 199855-199860	 **attackbox here**
    sprite('rg611_15', 6)	# 199861-199866	 **attackbox here**
    sprite('rg611_16', 6)	# 199867-199872	 **attackbox here**
    sprite('rg611_17', 6)	# 199873-199878	 **attackbox here**
    loopRest()
    gotoLabel(233)
    label(240)
    sprite('rg000_00', 1)	# 199879-199879

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    label(241)
    sprite('rg000_00', 7)	# 199880-199886
    sprite('rg000_01', 7)	# 199887-199893
    sprite('rg000_02', 7)	# 199894-199900
    sprite('rg000_03', 7)	# 199901-199907
    sprite('rg000_04', 7)	# 199908-199914
    sprite('rg000_05', 7)	# 199915-199921
    sprite('rg000_06', 7)	# 199922-199928
    sprite('rg000_05', 7)	# 199929-199935
    sprite('rg000_04', 7)	# 199936-199942
    sprite('rg000_03', 7)	# 199943-199949
    sprite('rg000_02', 7)	# 199950-199956
    sprite('rg000_01', 7)	# 199957-199963
    gotoLabel(241)
    label(242)
    sprite('rg611_00', 5)	# 199964-199968
    Unknown20000(1)
    sprite('rg611_01', 4)	# 199969-199972
    sprite('rg611_02', 10)	# 199973-199982
    sprite('rg611_03', 3)	# 199983-199985
    sprite('rg611_04', 8)	# 199986-199993	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 199994-199997	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 199998-200001	 **attackbox here**
    sprite('rg611_07', 6)	# 200002-200007	 **attackbox here**
    sprite('rg611_08', 6)	# 200008-200013	 **attackbox here**
    sprite('rg611_09', 6)	# 200014-200019	 **attackbox here**
    sprite('rg611_10', 6)	# 200020-200025	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 200026-200031	 **attackbox here**
    sprite('rg611_12', 6)	# 200032-200037	 **attackbox here**
    sprite('rg611_13', 6)	# 200038-200043	 **attackbox here**
    sprite('rg611_14', 6)	# 200044-200049	 **attackbox here**
    sprite('rg611_15', 6)	# 200050-200055	 **attackbox here**
    sprite('rg611_16', 6)	# 200056-200061	 **attackbox here**
    SFX_1('brg701bce')
    sprite('rg611_17', 6)	# 200062-200067	 **attackbox here**
    sprite('rg611_14', 6)	# 200068-200073	 **attackbox here**
    sprite('rg611_15', 6)	# 200074-200079	 **attackbox here**
    sprite('rg611_16', 6)	# 200080-200085	 **attackbox here**
    sprite('rg611_17', 6)	# 200086-200091	 **attackbox here**
    Unknown23018(1)
    label(243)
    sprite('rg611_14', 6)	# 200092-200097	 **attackbox here**
    sprite('rg611_15', 6)	# 200098-200103	 **attackbox here**
    sprite('rg611_16', 6)	# 200104-200109	 **attackbox here**
    sprite('rg611_17', 6)	# 200110-200115	 **attackbox here**
    gotoLabel(243)
    label(250)
    sprite('rg300_00', 1)	# 200116-200116

    def upon_40():
        clearUponHandler(40)
        sendToLabel(252)
    label(251)
    sprite('rg300_00', 1)	# 200117-200117
    sprite('rg300_01', 3)	# 200118-200120
    sprite('rg300_02', 3)	# 200121-200123
    sprite('rg300_03', 32767)	# 200124-232890
    label(252)
    sprite('rg300_03', 1)	# 232891-232891
    SFX_1('brg701bnt')
    label(253)
    sprite('rg300_03', 1)	# 232892-232892
    if SLOT_97:
        _gotolabel(253)
    sprite('rg300_06', 6)	# 232893-232898
    sprite('rg300_07', 6)	# 232899-232904
    sprite('rg300_08', 2)	# 232905-232906
    Unknown21007(24, 40)
    sprite('rg300_08', 1)	# 232907-232907
    sprite('rg610_01', 1)	# 232908-232908
    SFX_0('007_swing_knife_1')
    GFX_0('rgef610wingmake', -1)
    sprite('rg610_03', 3)	# 232909-232911
    sprite('rg610_04', 3)	# 232912-232914
    sprite('rg610_05', 3)	# 232915-232917
    sprite('rg610_06', 6)	# 232918-232923
    sprite('rg610_07', 2)	# 232924-232925
    GFX_0('rgef610wingbreak', -1)
    SFX_0('019_cloth_c')
    sprite('rg610_08', 6)	# 232926-232931
    SFX_0('210_down_garden_1')
    sprite('rg610_09', 6)	# 232932-232937
    sprite('rg610_10', 6)	# 232938-232943
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg610_11', 15)	# 232944-232958
    Unknown21011(30)
    sprite('rg610_11', 32767)	# 232959-265725
    ExitState()
    label(260)
    sprite('rg431_00', 3)	# 265726-265728

    def upon_40():
        clearUponHandler(40)
        sendToLabel(262)
    sprite('rg431_01', 3)	# 265729-265731
    sprite('rg431_02', 3)	# 265732-265734
    sprite('rg431_03', 3)	# 265735-265737
    sprite('rg431_04', 3)	# 265738-265740
    sprite('rg431_05', 3)	# 265741-265743
    SFX_1('brg700ahe')
    label(261)
    sprite('rg431_06', 1)	# 265744-265744
    if SLOT_97:
        _gotolabel(261)
    sprite('rg431_06', 60)	# 265745-265804
    sprite('rg431_06', 32767)	# 265805-298571
    Unknown21007(24, 40)
    label(262)
    sprite('rg431_05', 2)	# 298572-298573
    sprite('rg431_04', 2)	# 298574-298575
    sprite('rg431_03', 2)	# 298576-298577
    sprite('rg431_02', 3)	# 298578-298580
    sprite('rg431_01', 3)	# 298581-298583
    sprite('rg431_00', 3)	# 298584-298586
    sprite('rg000_00', 2)	# 298587-298588
    sprite('rg300_00', 6)	# 298589-298594
    SFX_1('brg702ahe')
    sprite('rg300_01', 6)	# 298595-298600
    sprite('rg300_02', 6)	# 298601-298606
    sprite('rg300_03', 8)	# 298607-298614
    sprite('rg300_04', 8)	# 298615-298622
    sprite('rg300_05', 32767)	# 298623-331389
    Unknown23018(1)
    label(270)
    sprite('rg610_00', 2)	# 331390-331391
    sprite('rg610_00', 3)	# 331392-331394
    sprite('rg610_01', 3)	# 331395-331397
    sprite('rg610_02', 3)	# 331398-331400
    SFX_1('brg700bsu')
    SFX_0('007_swing_knife_1')
    GFX_0('rgef610wingmake', -1)
    sprite('rg610_03', 3)	# 331401-331403
    sprite('rg610_04', 3)	# 331404-331406
    sprite('rg610_05', 3)	# 331407-331409
    sprite('rg610_06', 6)	# 331410-331415
    sprite('rg610_07', 2)	# 331416-331417
    GFX_0('rgef610wingbreak', -1)
    SFX_0('019_cloth_c')
    sprite('rg610_08', 6)	# 331418-331423
    SFX_0('210_down_garden_1')
    sprite('rg610_09', 6)	# 331424-331429
    sprite('rg610_10', 6)	# 331430-331435
    SFX_FOOTSTEP_(100, 1, 1)
    label(271)
    sprite('rg610_11', 1)	# 331436-331436
    if SLOT_97:
        _gotolabel(271)
    sprite('rg610_11', 15)	# 331437-331451
    sprite('rg610_11', 32767)	# 331452-364218
    Unknown21007(24, 40)
    Unknown21011(180)
    label(280)
    sprite('rg611_00', 5)	# 364219-364223
    sprite('rg611_01', 4)	# 364224-364227
    sprite('rg611_02', 10)	# 364228-364237
    sprite('rg611_03', 3)	# 364238-364240
    sprite('rg611_04', 8)	# 364241-364248	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 364249-364252	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 364253-364256	 **attackbox here**
    sprite('rg611_07', 6)	# 364257-364262	 **attackbox here**
    sprite('rg611_08', 6)	# 364263-364268	 **attackbox here**
    sprite('rg611_09', 6)	# 364269-364274	 **attackbox here**
    sprite('rg611_10', 6)	# 364275-364280	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 364281-364286	 **attackbox here**
    sprite('rg611_12', 6)	# 364287-364292	 **attackbox here**
    sprite('rg611_13', 6)	# 364293-364298	 **attackbox here**
    sprite('rg611_14', 6)	# 364299-364304	 **attackbox here**
    sprite('rg611_15', 6)	# 364305-364310	 **attackbox here**
    sprite('rg611_16', 6)	# 364311-364316	 **attackbox here**
    SFX_1('brg700uak')
    sprite('rg611_17', 6)	# 364317-364322	 **attackbox here**
    sprite('rg611_14', 6)	# 364323-364328	 **attackbox here**
    sprite('rg611_15', 6)	# 364329-364334	 **attackbox here**
    sprite('rg611_16', 6)	# 364335-364340	 **attackbox here**
    sprite('rg611_17', 6)	# 364341-364346	 **attackbox here**
    sprite('rg611_14', 6)	# 364347-364352	 **attackbox here**
    sprite('rg611_15', 6)	# 364353-364358	 **attackbox here**
    sprite('rg611_16', 6)	# 364359-364364	 **attackbox here**
    sprite('rg611_17', 6)	# 364365-364370	 **attackbox here**
    sprite('rg611_14', 6)	# 364371-364376	 **attackbox here**
    sprite('rg611_15', 6)	# 364377-364382	 **attackbox here**
    sprite('rg611_16', 6)	# 364383-364388	 **attackbox here**
    sprite('rg611_17', 6)	# 364389-364394	 **attackbox here**
    label(281)
    sprite('rg611_14', 6)	# 364395-364400	 **attackbox here**
    sprite('rg611_15', 6)	# 364401-364406	 **attackbox here**
    sprite('rg611_16', 6)	# 364407-364412	 **attackbox here**
    sprite('rg611_17', 6)	# 364413-364418	 **attackbox here**
    if SLOT_97:
        _gotolabel(281)
    sprite('rg611_14', 1)	# 364419-364419	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(180)
    label(282)
    sprite('rg611_14', 6)	# 364420-364425	 **attackbox here**
    sprite('rg611_15', 6)	# 364426-364431	 **attackbox here**
    sprite('rg611_16', 6)	# 364432-364437	 **attackbox here**
    sprite('rg611_17', 6)	# 364438-364443	 **attackbox here**
    gotoLabel(282)
    label(290)
    sprite('rg000_00', 1)	# 364444-364444

    def upon_40():
        clearUponHandler(40)
        sendToLabel(292)
    label(291)
    sprite('rg000_00', 7)	# 364445-364451
    sprite('rg000_01', 7)	# 364452-364458
    sprite('rg000_02', 7)	# 364459-364465
    sprite('rg000_03', 7)	# 364466-364472
    sprite('rg000_04', 7)	# 364473-364479
    sprite('rg000_05', 7)	# 364480-364486
    sprite('rg000_06', 7)	# 364487-364493
    sprite('rg000_05', 7)	# 364494-364500
    sprite('rg000_04', 7)	# 364501-364507
    sprite('rg000_03', 7)	# 364508-364514
    sprite('rg000_02', 7)	# 364515-364521
    sprite('rg000_01', 7)	# 364522-364528
    gotoLabel(291)
    label(292)
    sprite('rg611_00', 5)	# 364529-364533
    sprite('rg611_01', 4)	# 364534-364537
    sprite('rg611_02', 10)	# 364538-364547
    sprite('rg611_03', 3)	# 364548-364550
    sprite('rg611_04', 8)	# 364551-364558	 **attackbox here**
    SFX_3('rgse_25')
    sprite('rg611_05', 4)	# 364559-364562	 **attackbox here**
    SFX_3('rgse_00')
    sprite('rg611_06', 4)	# 364563-364566	 **attackbox here**
    sprite('rg611_07', 6)	# 364567-364572	 **attackbox here**
    sprite('rg611_08', 6)	# 364573-364578	 **attackbox here**
    sprite('rg611_09', 6)	# 364579-364584	 **attackbox here**
    sprite('rg611_10', 6)	# 364585-364590	 **attackbox here**
    SFX_3('rgse_05')
    sprite('rg611_11', 6)	# 364591-364596	 **attackbox here**
    sprite('rg611_12', 6)	# 364597-364602	 **attackbox here**
    sprite('rg611_13', 6)	# 364603-364608	 **attackbox here**
    sprite('rg611_14', 6)	# 364609-364614	 **attackbox here**
    sprite('rg611_15', 6)	# 364615-364620	 **attackbox here**
    sprite('rg611_16', 6)	# 364621-364626	 **attackbox here**
    SFX_1('brg701kym')
    sprite('rg611_17', 6)	# 364627-364632	 **attackbox here**
    sprite('rg611_14', 6)	# 364633-364638	 **attackbox here**
    sprite('rg611_15', 6)	# 364639-364644	 **attackbox here**
    sprite('rg611_16', 6)	# 364645-364650	 **attackbox here**
    sprite('rg611_17', 6)	# 364651-364656	 **attackbox here**
    Unknown23018(1)
    label(243)
    sprite('rg611_14', 6)	# 364657-364662	 **attackbox here**
    sprite('rg611_15', 6)	# 364663-364668	 **attackbox here**
    sprite('rg611_16', 6)	# 364669-364674	 **attackbox here**
    sprite('rg611_17', 6)	# 364675-364680	 **attackbox here**
    gotoLabel(243)

@State
def CmnActLose():
    sprite('rg620_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('brg403_0', 100, 879194722, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('rg620_01', 6)	# 7-12
    sprite('rg620_02', 6)	# 13-18
    sprite('rg620_03', 6)	# 19-24
    sprite('rg620_04', 6)	# 25-30
    SFX_3('rgse_00')
    sprite('rg620_05', 32767)	# 31-32797

@State
def EventDefEntryWait():
    label(0)
    sprite('rg000_00', 7)	# 1-7
    sprite('rg000_01', 7)	# 8-14
    sprite('rg000_02', 7)	# 15-21
    sprite('rg000_03', 7)	# 22-28
    sprite('rg000_04', 7)	# 29-35
    sprite('rg000_05', 7)	# 36-42
    sprite('rg000_06', 7)	# 43-49
    sprite('rg000_05', 7)	# 50-56
    sprite('rg000_04', 7)	# 57-63
    sprite('rg000_03', 7)	# 64-70
    sprite('rg000_02', 7)	# 71-77
    sprite('rg000_01', 7)	# 78-84
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
    sprite('rg620_05', 32767)	# 1-32767

@State
def EventDefChouhatsu():
    sprite('rg300_00', 4)	# 1-4
    sprite('rg300_01', 4)	# 5-8
    sprite('rg300_02', 4)	# 9-12
    sprite('rg300_03', 6)	# 13-18
    sprite('rg300_04', 6)	# 19-24
    sprite('rg300_05', 7)	# 25-31
    sprite('rg300_04', 6)	# 32-37
    sprite('rg300_05', 7)	# 38-44
    sprite('rg300_03', 9)	# 45-53
    sprite('rg300_06', 6)	# 54-59
    sprite('rg300_07', 6)	# 60-65
    sprite('rg300_08', 6)	# 66-71
    loopRest()
    enterState('CmnActStand')

@State
def EventDefChouhatsu2():
    sprite('rg300_00', 4)	# 1-4
    sprite('rg300_01', 4)	# 5-8
    sprite('rg300_02', 4)	# 9-12
    sprite('rg300_03', 6)	# 13-18
    sprite('rg300_04', 6)	# 19-24
    sprite('rg300_05', 32767)	# 25-32791

@State
def EventDefChouhatsuEnd():
    sprite('rg300_03', 6)	# 1-6
    sprite('rg300_06', 6)	# 7-12
    sprite('rg300_07', 6)	# 13-18
    sprite('rg300_08', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventYoroke():
    sprite('rg070_07', 32767)	# 1-32767
    loopRest()

@State
def EventEntry0_WaitGazingEnemy():
    sprite('rg601_00', 32767)	# 1-32767
    loopRest()

@State
def EventEntry0_PrepareForBattle():
    sprite('rg601_00', 6)	# 1-6
    sprite('rg601_01', 6)	# 7-12
    sprite('rg601_02', 6)	# 13-18
    sprite('rg601_03', 6)	# 19-24
    sprite('rg601_04', 6)	# 25-30
    sprite('rg601_05', 6)	# 31-36
    sprite('rg601_06', 6)	# 37-42
    sprite('rg601_07', 6)	# 43-48
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 49-54
    sprite('rg601_09', 6)	# 55-60
    sprite('rg601_10', 6)	# 61-66
    sprite('rg601_11', 4)	# 67-70
    sprite('rg601_12', 4)	# 71-74
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 75-78
    sprite('rg601_14', 4)	# 79-82
    sprite('rg601_15', 4)	# 83-86
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 87-90
    sprite('rg601_17', 6)	# 91-96
    sprite('rg601_18', 6)	# 97-102
    sprite('rg601_19', 3)	# 103-105
    sprite('rg601_20', 6)	# 106-111
    sprite('rg601_21', 6)	# 112-117
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 118-123
    sprite('rg601_23', 6)	# 124-129
    loopRest()
    enterState('CmnActStand')

@State
def EventWarpIn():
    Unknown3001(0)
    sprite('rg000_00', 6)	# 1-6
    Unknown3004(10)
    SFX_0('001_airbackdash_0')
    sprite('keep', 20)	# 7-26
    SFX_0('000_airdash_2')
    sprite('keep', 1)	# 27-27
    Unknown3004(0)
    Unknown3001(255)
    loopRest()
    enterState('CmnActStand')

@State
def EventWarpOut():
    sprite('keep', 6)	# 1-6
    Unknown3004(-10)
    SFX_0('001_airbackdash_0')
    sprite('keep', 20)	# 7-26
    SFX_0('000_airdash_2')
    sprite('null', 32767)	# 27-32793
    Unknown3004(0)
    Unknown3001(0)
    loopRest()

@State
def EventVSJN1():
    sprite('keep', 2)	# 1-2
    Unknown1000(-200000)
    loopRest()
    enterState('CmnActStand')

@State
def EventVSJN2():
    sprite('rg040_00', 4)	# 1-4
    setInvincible(1)
    sprite('rg040_01', 4)	# 5-8
    sprite('rg040_02', 4)	# 9-12
    sprite('rg040_03', 4)	# 13-16
    SFX_0('105_guard_slash_2')
    physicsXImpulse(-6000)
    sprite('rg041_01', 2)	# 17-18
    sprite('rg041_02', 2)	# 19-20
    Unknown1019(50)
    sprite('rg041_03', 15)	# 21-35
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('rg040_02', 2)	# 36-37
    sprite('rg040_01', 2)	# 38-39
    sprite('rg040_00', 2)	# 40-41
    setInvincible(0)
    loopRest()
    enterState('CmnActStand')

@State
def EventRGAttackCStart():
    sprite('rg202_00', 3)	# 1-3
    sprite('rg202_01', 3)	# 4-6
    sprite('rg202_02', 5)	# 7-11
    sprite('rg202_05', 5)	# 12-16
    SFX_0('008_swing_pole_2')
    sprite('rg202_06', 4)	# 17-20
    sprite('rg202_07', 3)	# 21-23
    sprite('rg202_08', 3)	# 24-26	 **attackbox here**
    sprite('rg202_09', 4)	# 27-30	 **attackbox here**
    ScreenShake(18000, 6000)
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_2')
    SFX_0('108_attack_offset')
    sprite('rg202_10', 2)	# 31-32
    sprite('rg202_11', 2)	# 33-34
    sprite('rg202_12', 32767)	# 35-32801
    GFX_0('EventEffectRGVsTB_Hakumen', 0)
    loopRest()

@State
def EventRGAttackCEnd():
    sprite('rg202_13', 4)	# 1-4
    sprite('rg202_14', 3)	# 5-7
    sprite('rg202_15', 3)	# 8-10
    sprite('rg202_16', 3)	# 11-13
    sprite('rg202_17', 4)	# 14-17
    sprite('rg202_18', 4)	# 18-21
    loopRest()
    enterState('CmnActStand')

@State
def EventRGVsNY_Attack():
    Unknown1000(-260000)
    AttackDefaults_StandingDD()
    AttackLevel_(4)
    setInvincible(1)
    DisableAttackRestOfMove()
    sprite('rg023_00', 2)	# 1-2
    SFX_3('rgse_00')
    sprite('rg023_01', 2)	# 3-4
    sprite('rg020_00', 1)	# 5-5
    physicsXImpulse(12600)
    physicsYImpulse(42000)
    Unknown1043()
    sprite('rg020_00', 2)	# 6-7
    sprite('rg020_01', 2)	# 8-9
    sprite('rg020_02', 2)	# 10-11
    sprite('rg020_03', 2)	# 12-13
    sprite('rg020_04', 2)	# 14-15
    sprite('rg411_00', 2)	# 16-17
    sendToLabelUpon(2, 1)
    Unknown1084(1)
    physicsXImpulse(-4750)
    physicsYImpulse(9500)
    setGravity(0)
    sprite('rg411_01', 2)	# 18-19
    Unknown1019(90)
    YAccel(90)
    sprite('rg411_02', 2)	# 20-21	 **attackbox here**
    Unknown21007(22, 32)
    Unknown1019(90)
    YAccel(90)
    SFX_0('019_cloth_b')
    sprite('rg411_03', 8)	# 22-29
    Unknown1019(90)
    YAccel(90)
    sprite('rg411_04', 2)	# 30-31	 **attackbox here**
    SFX_3('rgse_24')
    GFX_1('rgef00', 1)
    GFX_1('rgef00', 2)
    GFX_1('rgef00', 3)
    physicsXImpulse(5700)
    physicsYImpulse(-11400)
    setGravity(0)
    sprite('rg411_04', 2)	# 32-33	 **attackbox here**
    physicsXImpulse(28500)
    physicsYImpulse(-57000)
    setGravity(0)
    loopRest()
    Unknown3029(1)
    AttackLevel_(4)
    Hitstop(2)
    Unknown9016(1)
    AirHitstunAnimation(9)
    AirPushbackX(28500)
    AirPushbackY(-57000)
    YImpluseBeforeWallbounce(0)
    Unknown11001(-1, -1, 6)
    AirUntechableTime(25)
    sendToLabelUpon(10, 1)
    sprite('rg411_05', 1)	# 34-34	 **attackbox here**
    RefreshMultihit()
    loopRest()
    label(0)
    sprite('rg411_05', 2)	# 35-36	 **attackbox here**
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000000000000')
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000002000000')
    GFX_1('rgef02', 0)
    GFX_1('rgef02', 1)
    sprite('rg411_06', 1)	# 37-37	 **attackbox here**
    Unknown4049(2000)
    Unknown4045('726765663030000000000000000000000000000000000000000000000000000001000000')
    GFX_1('rgef02', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(10)
    sprite('rg411_04', 2)	# 38-39	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(-10000)
    physicsYImpulse(8000)
    Unknown1043()
    sprite('rg411_03', 2)	# 40-41
    sprite('rg411_02', 2)	# 42-43	 **attackbox here**
    sprite('rg411_01', 2)	# 44-45
    sprite('rg411_00', 2)	# 46-47
    sprite('rg020_05', 3)	# 48-50
    sprite('rg020_06', 3)	# 51-53
    sendToLabelUpon(2, 3)
    label(2)
    sprite('rg020_07', 4)	# 54-57
    sprite('rg020_08', 4)	# 58-61
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(2)
    sprite('rg024_00', 5)	# 62-66
    Unknown1084(1)
    Unknown1047(-8000)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    Unknown3029(0)
    sprite('rg024_01', 5)	# 67-71
    sprite('rg024_02', 4)	# 72-75
    sprite('rg024_03', 4)	# 76-79
    Unknown21007(22, 32)
    sprite('rg024_04', 3)	# 80-82
    loopRest()
    sprite('rg213_00', 2)	# 83-84
    sprite('rg213_01', 2)	# 85-86
    sprite('rg213_02', 2)	# 87-88
    Unknown1045(5000)
    sprite('rg213_02', 2)	# 89-90
    sprite('rg213_03', 3)	# 91-93
    SFX_0('006_swing_blade_2')
    SFX_3('rgse_03')
    sprite('rg213_04', 2)	# 94-95
    sprite('rg213_05', 2)	# 96-97
    teleportRelativeX(50000)
    physicsYImpulse(18000)
    physicsXImpulse(1000)
    Unknown1043()
    sendToLabelUpon(2, 4)
    sprite('rg213_06', 2)	# 98-99
    GFX_0('rgef213atk', -1)
    sprite('rg213_07', 2)	# 100-101
    sprite('rg213_08', 3)	# 102-104	 **attackbox here**
    RefreshMultihit()
    sprite('rg213_09', 2)	# 105-106
    sprite('rg213_10', 2)	# 107-108
    sprite('rg213_11', 2)	# 109-110
    sprite('rg213_12', 2)	# 111-112
    sprite('rg213_13', 2)	# 113-114
    sprite('rg213_14', 32767)	# 115-32881
    label(4)
    sprite('rg213_15', 3)	# 32882-32884
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rg213_16', 3)	# 32885-32887
    sprite('rg213_17', 3)	# 32888-32890
    sprite('rg213_18', 3)	# 32891-32893
    sprite('rg213_19', 4)	# 32894-32897
    loopRest()
    enterState('CmnActStand')

@State
def EventRGVsNY_BootBlazblueStart():
    sprite('rg431_00', 3)	# 1-3
    sprite('rg431_01', 3)	# 4-6
    sprite('rg431_02', 3)	# 7-9
    sprite('rg431_03', 3)	# 10-12
    sprite('rg431_04', 3)	# 13-15
    sprite('rg431_05', 3)	# 16-18
    sprite('rg431_06', 32767)	# 19-32785

@State
def EventRGVsNY_BootBlazblueLoop():
    sprite('rg431_07', 3)	# 1-3
    sprite('rg431_08', 3)	# 4-6
    sprite('rg431_09', 3)	# 7-9
    sprite('rg431_08', 3)	# 10-12
    sprite('rg431_09', 3)	# 13-15
    sprite('rg431_08', 3)	# 16-18
    sprite('rg431_09', 3)	# 19-21
    sprite('rg431_08', 3)	# 22-24
    sprite('rg431_09', 3)	# 25-27
    loopRest()
    sprite('keep', 4)	# 28-31
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 32-35
    sprite('keep', 4)	# 36-39
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 40-43
    sprite('keep', 4)	# 44-47
    ScreenShake(5000, 10000)
    GFX_0('NOISE', -1)
    SFX_0('023_noize')
    sprite('keep', 4)	# 48-51
    sprite('keep', 4)	# 52-55
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 56-59
    sprite('keep', 4)	# 60-63
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 64-67
    sprite('keep', 4)	# 68-71
    ScreenShake(5000, 10000)
    sprite('keep', 32767)	# 72-32838
    loopRest()

@State
def EventRGVsNY_BootBlazblueEnd():
    sprite('rg431_10', 4)	# 1-4
    sprite('rg431_12', 4)	# 5-8
    sprite('rg431_13', 4)	# 9-12
    sprite('rg431_14', 8)	# 13-20
    sprite('rg431_15', 4)	# 21-24
    sprite('rg431_16', 3)	# 25-27
    loopRest()
    enterState('CmnActStand')

@State
def EventRGAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(4)
        AttackP2(70)
        setInvincible(1)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(0)
        SLOT_60 = 0

        def upon_CLEAR_OR_EXIT():
            (SLOT_19 < 300000)
            if op(5, 2, 0, 2, 60):
                SLOT_60 = 0
                sendToLabel(0)
    sprite('rg400_00', 2)	# 1-2
    SFX_1('rg200')
    sprite('rg400_01', 2)	# 3-4
    sprite('rg400_02', 5)	# 5-9
    GFX_0('rgef400nokori', -1)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    sprite('rg400_03', 2)	# 10-11
    sprite('rg400_04', 3)	# 12-14
    GFX_0('rgef400loop', -1)
    Unknown38(4, 1)
    physicsXImpulse(40000)
    Unknown8006(100, 1, 0)
    sprite('rg400_05', 2)	# 15-16	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 3)	# 17-19	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_07', 2)	# 20-21	 **attackbox here**
    SLOT_60 = 1
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 2)	# 22-23	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_07', 2)	# 24-25	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06', 2)	# 26-27	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_09', 2)	# 28-29
    sprite('rg400_10', 2)	# 30-31
    Unknown8006(100, 1, 0)
    sprite('rg400_11', 2)	# 32-33
    Unknown8006(100, 1, 0)
    sprite('rg400_12', 2)	# 34-35
    Unknown8006(100, 1, 0)
    label(0)
    sprite('rg400_08', 2)	# 36-37
    SLOT_60 = 0
    Unknown13(4)
    GFX_0('rgef400end', -1)
    clearUponHandler(10)
    Unknown1019(70)
    Unknown1028(-1000)
    sprite('rg400_08', 2)	# 38-39
    sprite('rg400_09', 2)	# 40-41
    sprite('rg400_10', 2)	# 42-43
    Unknown8006(100, 1, 0)
    sprite('rg400_11', 2)	# 44-45
    Unknown8006(100, 1, 0)
    sprite('rg400_12', 2)	# 46-47
    Unknown8006(100, 1, 0)
    sprite('rg400_13', 3)	# 48-50
    Unknown8006(100, 1, 0)
    sprite('rg400_14', 3)	# 51-53
    sprite('rg400_15', 3)	# 54-56
    SFX_0('208_brake_normal')
    sprite('rg400_16', 3)	# 57-59
    SFX_0('208_brake_normal')
    Unknown1028(0)
    physicsXImpulse(0)
    Unknown2001()

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown23001(100, 0)
    sprite('rg033_00', 1)	# 60-60
    sprite('rg033_01', 2)	# 61-62
    SFX_3('rgse_00')
    physicsXImpulse(-25000)
    physicsYImpulse(13000)
    setGravity(1550)
    Unknown8002()
    sprite('rg033_02', 2)	# 63-64
    sprite('rg033_02', 1)	# 65-65
    sprite('rg033_03', 3)	# 66-68
    loopRest()
    sprite('rg033_02', 3)	# 69-71
    sprite('rg033_03', 3)	# 72-74
    sprite('rg033_02', 3)	# 75-77
    sprite('rg033_03', 2)	# 78-79
    sprite('rg010_01', 2)	# 80-81
    Unknown1044()
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown1000(-260000)
    teleportRelativeY(0)
    sprite('rg010_02', 32767)	# 82-32848

@State
def EventRGCrouch2Stand():
    sprite('rg010_01', 6)	# 1-6
    sprite('rg010_00', 6)	# 7-12
    enterState('CmnActStand')

@State
def EventRGReaction():
    sprite('rg001_01', 6)	# 1-6
    sprite('rg001_02', 6)	# 7-12
    sprite('rg001_03', 6)	# 13-18
    sprite('rg001_04', 6)	# 19-24
    sprite('rg001_05', 6)	# 25-30
    sprite('rg001_06', 6)	# 31-36
    sprite('rg001_07', 6)	# 37-42
    sprite('rg001_08', 6)	# 43-48
    sprite('rg001_09', 6)	# 49-54
    sprite('rg001_10', 6)	# 55-60
    sprite('rg001_11', 6)	# 61-66
    sprite('rg001_12', 6)	# 67-72
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 73-78
    sprite('rg001_14', 6)	# 79-84
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 85-90
    sprite('rg001_16', 6)	# 91-96
    loopRest()
    enterState('CmnActStand')

@State
def EventRGWin1():
    sprite('rg610_00', 1)	# 1-1
    sprite('rg610_00', 3)	# 2-4
    sprite('rg610_01', 3)	# 5-7
    sprite('rg610_02', 3)	# 8-10
    sprite('rg610_03', 3)	# 11-13
    sprite('rg610_04', 3)	# 14-16
    sprite('rg610_05', 3)	# 17-19
    sprite('rg610_06', 6)	# 20-25
    sprite('rg610_07', 2)	# 26-27
    SFX_0('019_cloth_c')
    sprite('rg610_08', 6)	# 28-33
    sprite('rg610_09', 6)	# 34-39
    sprite('rg610_10', 6)	# 40-45
    sprite('rg610_11', 32767)	# 46-32812

@State
def EventRGPowerUp():
    sprite('rg431_00', 3)	# 1-3
    GFX_0('ModelMagicCircle1', 0)
    sprite('rg431_01', 3)	# 4-6
    sprite('rg431_02', 3)	# 7-9
    sprite('rg431_03', 3)	# 10-12
    sprite('rg431_04', 3)	# 13-15
    Unknown4047(224, 224, 224)
    Unknown4049(1500)
    Unknown4045('7267656634333168616e64706f7700000000000000000000000000000000000001000000')
    sprite('rg431_05', 3)	# 16-18
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    sprite('rg431_06', 2)	# 19-20
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown4047(224, 208, 192)
    Unknown4045('726765663433310000000000000000000000000000000000000000000000000001000000')
    Unknown2036(1, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    SLOT_31 = 600
    sprite('rg431_06', 2)	# 21-22
    SFX_3('rgse_04')
    sprite('rg431_06', 2)	# 23-24
    sprite('rg431_06', 3)	# 25-27
    sprite('rg431_06', 3)	# 28-30
    sprite('rg431_06', 260)	# 31-290
    sprite('rg431_07', 3)	# 291-293
    SFX_3('rgse_01')
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    sprite('rg431_08', 3)	# 294-296
    GFX_1('rgef_bkkakusan', -1)
    GFX_0('rgef431_Start', 1)
    sprite('rg431_09', 3)	# 297-299
    sprite('rg431_08', 3)	# 300-302
    sprite('rg431_09', 3)	# 303-305
    Unknown3068('00000000ff000000ff000000ff000000ff000000')
    sprite('rg431_08', 3)	# 306-308
    Unknown3068('00000000c8000000ff000000ff000000ff000000')
    sprite('rg431_09', 3)	# 309-311
    Unknown3068('0000000096000000ff000000ff000000ff000000')
    sprite('rg431_08', 3)	# 312-314
    Unknown3068('0000000064000000ff000000ff000000ff000000')
    sprite('rg431_09', 3)	# 315-317
    Unknown3068('0000000028000000ff000000ff000000ff000000')
    sprite('rg431_10', 5)	# 318-322
    Unknown3068('0000000015000000ff000000ff000000ff000000')
    sprite('rg431_02', 5)	# 323-327
    sprite('rg431_01', 5)	# 328-332
    sprite('rg431_00', 5)	# 333-337
    Unknown3060('000000000000000000000000000000000000000000000000000000000000000000000000')
    loopRest()
    enterState('CmnActStand')

@State
def EventRGPowerDown():
    sprite('rg000_00', 1)	# 1-1
    SLOT_31 = (SLOT_31 + (-600))
    Unknown3029(0)
    Unknown3030(0)
    SLOT_62 = 1
    loopRest()
    enterState('CmnActStand')

@State
def EventRGEntryOutWindow():
    label(0)
    sprite('rg000_00', 1)	# 1-1
    Unknown1000(-1200000)
    Unknown2034(0)
    loopRest()
    gotoLabel(0)

@State
def EventHZvsRGEntry00():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Hitstop(8)
        Unknown2004(1, 0)
        setInvincible(1)
    sprite('rg450_03', 3)	# 1-3
    setInvincible(1)
    Unknown2034(0)
    SFX_1('rg211')
    physicsXImpulse(15000)
    Unknown1028(7000)
    Unknown8006(100, 1, 0)
    SFX_0('000_airdash_0')
    sprite('rg450_04', 3)	# 4-6
    Unknown8006(100, 1, 0)
    sprite('rg450_03', 3)	# 7-9
    Unknown8006(100, 1, 0)
    sprite('rg450_04', 3)	# 10-12
    Unknown8006(100, 1, 0)
    sprite('rg450_05', 2)	# 13-14
    Unknown1019(30)
    Unknown1028(0)
    sprite('rg450_06', 2)	# 15-16
    Unknown1019(30)
    SFX_0('011_spin_0')
    SFX_0('010_swing_sword_2')
    SFX_0('016_explode_1')
    sprite('rg450_07', 1)	# 17-17	 **attackbox here**
    StartMultihit()
    Unknown1019(30)
    GFX_0('rgef450', -1)
    sprite('rg450_08', 2)	# 18-19
    Unknown1019(0)
    sprite('rg450_09', 3)	# 20-22
    SFX_3('rgse_05')
    sprite('rg450_10', 5)	# 23-27
    sprite('rg450_11', 6)	# 28-33
    sprite('rg450_12', 6)	# 34-39
    sprite('rg451_00', 5)	# 40-44
    teleportRelativeX(100000)
    sprite('rg451_01', 4)	# 45-48
    sprite('rg451_02', 4)	# 49-52
    sprite('rg451_03', 3)	# 53-55
    sprite('rg451_04', 2)	# 56-57
    GFX_0('rgef451atk', -1)
    sprite('rg451_05', 2)	# 58-59
    sprite('rg451_06', 3)	# 60-62
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_0('005_swing_grap_2_2')
    SFX_0('004_swing_grap_1_2')
    SFX_3('rgse_03')
    sprite('rg451_07ex', 4)	# 63-66	 **attackbox here**
    RefreshMultihit()
    SFX_0('209_down_normal_0')
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    SFX_0('013_thunder_1')
    SFX_3('rgse_01')
    sprite('rg451_08', 2)	# 67-68
    sprite('rg451_09', 2)	# 69-70
    sprite('rg451_10', 2)	# 71-72
    sprite('rg451_11', 3)	# 73-75
    Unknown1000(-175000)
    sprite('rg451_12', 3)	# 76-78
    Unknown1000(-175000)
    sprite('rg451_13', 3)	# 79-81
    Unknown1000(-175000)
    sprite('rg451_14', 3)	# 82-84
    Unknown1000(-225000)
    sprite('rg451_15', 3)	# 85-87
    Unknown1000(-250000)
    sprite('rg451_16', 3)	# 88-90
    Unknown1000(-260000)

@State
def EventRGWalkFrameIn():
    Unknown2034(0)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(4650)
    label(0)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_03', 7)	# 22-28
    sprite('rg030_04', 7)	# 29-35
    sprite('rg030_05', 7)	# 36-42
    sprite('rg030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_07', 7)	# 50-56
    sprite('rg030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventRGChouhatu():
    sprite('rg300_00', 4)	# 1-4
    sprite('rg300_01', 4)	# 5-8
    sprite('rg300_02', 4)	# 9-12
    sprite('rg300_03', 6)	# 13-18
    sprite('rg300_04', 6)	# 19-24
    sprite('rg300_05', 7)	# 25-31
    sprite('rg300_04', 6)	# 32-37
    sprite('rg300_05', 7)	# 38-44
    sprite('rg300_03', 9)	# 45-53
    sprite('rg300_06', 6)	# 54-59
    sprite('rg300_07', 6)	# 60-65
    sprite('rg300_08', 6)	# 66-71
    loopRest()
    enterState('CmnActStand')

@State
def EventDefLoseScreenShake():
    sprite('rg620_05', 1)	# 1-1
    ScreenShake(0, 3000)
    sprite('rg620_05', 1)	# 2-2
    ScreenShake(0, 3000)
    sprite('rg620_05', 1)	# 3-3
    ScreenShake(0, 3000)
    loopRest()
    enterState('EventDefLose')

@State
def EventYorokeDown():
    sprite('rg070_07', 1)	# 1-1
    teleportRelativeX(3000)
    sprite('rg070_07', 1)	# 2-2
    teleportRelativeX(3000)
    sprite('rg070_07', 1)	# 3-3
    teleportRelativeX(-3000)
    sprite('rg070_07', 1)	# 4-4
    teleportRelativeX(3000)
    sprite('rg070_07', 1)	# 5-5
    teleportRelativeX(-3000)
    sprite('rg070_07', 1)	# 6-6
    teleportRelativeX(3000)
    sprite('rg070_07', 1)	# 7-7
    teleportRelativeX(-3000)
    sprite('rg070_07', 1)	# 8-8
    teleportRelativeX(3000)
    sprite('rg070_07', 1)	# 9-9
    teleportRelativeX(-3000)
    sprite('rg070_07', 1)	# 10-10
    teleportRelativeX(3000)
    sprite('rg070_07', 1)	# 11-11
    teleportRelativeX(-3000)
    sprite('rg070_07', 1)	# 12-12
    teleportRelativeX(3000)
    sprite('rg070_07', 1)	# 13-13
    teleportRelativeX(-3000)
    sprite('rg070_07', 1)	# 14-14
    teleportRelativeX(3000)
    sprite('rg070_07', 2)	# 15-16
    sprite('rg070_08', 7)	# 17-23
    sprite('rg070_09', 5)	# 24-28
    sprite('rg070_10', 5)	# 29-33
    sprite('rg063_11', 1)	# 34-34
    SFX_0('209_down_normal_0')
    Unknown8000(100, 1, 1)
    teleportRelativeX(100000)
    label(0)
    sprite('rg063_11', 1)	# 35-35
    loopRest()
    gotoLabel(0)

@State
def EventHAvsRGEntryWait():
    sprite('null', 32767)	# 1-32767
    Unknown2034(0)
    EnableCollision(0)
    Unknown1000(-12800000)

@State
def EventHAvsRGEntry():
    sprite('rg400_00', 2)	# 1-2
    Unknown2034(0)
    EnableCollision(0)
    AttackDefaults_StandingSpecial()
    AttackLevel_(4)
    Unknown23022(1)
    sprite('rg400_01', 2)	# 3-4
    sprite('rg400_02', 5)	# 5-9
    GFX_0('rgef400nokori', -1)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    sprite('rg400_03', 2)	# 10-11
    sprite('rg400_04', 2)	# 12-13
    physicsXImpulse(80000)
    Unknown8006(100, 1, 0)
    sprite('rg400_05', 2)	# 14-15	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06ex', 3)	# 16-18	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_07ex', 2)	# 19-20	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06ex', 2)	# 21-22	 **attackbox here**
    GFX_0('rgef400loop', -1)
    Unknown38(4, 1)
    Unknown8006(100, 1, 0)
    sprite('rg400_07ex', 2)	# 23-24	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06ex', 2)	# 25-26	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_07ex', 2)	# 27-28	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_06ex', 2)	# 29-30	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('rg400_08', 1)	# 31-31
    Unknown13(4)
    GFX_0('rgef400end', -1)
    Unknown1019(10)
    Unknown1028(-1000)
    sprite('rg400_08', 1)	# 32-32
    sprite('rg400_09', 1)	# 33-33
    sprite('rg400_10', 1)	# 34-34
    Unknown8006(100, 1, 0)
    sprite('rg400_11', 1)	# 35-35
    Unknown8006(100, 1, 0)
    sprite('rg400_12', 1)	# 36-36
    Unknown8006(100, 1, 0)
    sprite('rg401_00', 1)	# 37-37
    Unknown1028(0)
    RefreshMultihit()
    sprite('rg401_01', 1)	# 38-38
    sprite('rg401_02', 1)	# 39-39
    Unknown1019(2)
    sprite('rg401_03', 1)	# 40-40
    Unknown1019(0)
    sprite('rg401_04', 1)	# 41-41
    sprite('rg401_05', 1)	# 42-42
    Unknown1000(-260000)
    GFX_0('rgef401atk', -1)
    sprite('rg401_06', 2)	# 43-44
    sprite('rg401_07', 2)	# 45-46
    sprite('rg401_08', 3)	# 47-49
    SFX_0('004_swing_grap_1_0')
    SFX_0('004_swing_grap_1_1')
    SFX_3('rgse_02')
    SFX_3('rgse_02')
    sprite('rg401_09', 3)	# 50-52	 **attackbox here**
    sprite('rg401_10', 4)	# 53-56
    sprite('rg401_11', 4)	# 57-60
    sprite('rg401_12', 12)	# 61-72
    sprite('rg401_13', 4)	# 73-76
    sprite('rg401_14', 4)	# 77-80
    sprite('rg401_15', 3)	# 81-83
    sprite('rg401_16', 3)	# 84-86
    sprite('rg401_17', 3)	# 87-89
    sprite('rg401_18', 3)	# 90-92
    loopRest()
    enterState('CmnActStand')

@State
def EventRGStandAway():
    Unknown2005()
    label(0)
    sprite('rg000_00', 7)	# 1-7
    sprite('rg000_01', 7)	# 8-14
    sprite('rg000_02', 7)	# 15-21
    sprite('rg000_03', 7)	# 22-28
    sprite('rg000_04', 7)	# 29-35
    sprite('rg000_05', 7)	# 36-42
    sprite('rg000_06', 7)	# 43-49
    sprite('rg000_05', 7)	# 50-56
    sprite('rg000_04', 7)	# 57-63
    sprite('rg000_03', 7)	# 64-70
    sprite('rg000_02', 7)	# 71-77
    sprite('rg000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def EventRGStandTurn():
    Unknown2005()
    sprite('rg003_00', 3)	# 1-3
    sprite('rg003_01', 3)	# 4-6
    sprite('rg003_02', 3)	# 7-9
    label(0)
    sprite('rg000_00', 7)	# 10-16
    sprite('rg000_01', 7)	# 17-23
    sprite('rg000_02', 7)	# 24-30
    sprite('rg000_03', 7)	# 31-37
    sprite('rg000_04', 7)	# 38-44
    sprite('rg000_05', 7)	# 45-51
    sprite('rg000_06', 7)	# 52-58
    sprite('rg000_05', 7)	# 59-65
    sprite('rg000_04', 7)	# 66-72
    sprite('rg000_03', 7)	# 73-79
    sprite('rg000_02', 7)	# 80-86
    sprite('rg000_01', 7)	# 87-93
    gotoLabel(0)

@State
def EventRGvsPTReaction():
    sprite('rg001_01', 6)	# 1-6
    sprite('rg001_02', 6)	# 7-12
    sprite('rg001_03', 6)	# 13-18
    sprite('rg001_04', 6)	# 19-24
    sprite('rg001_05', 6)	# 25-30
    sprite('rg001_06', 6)	# 31-36
    sprite('rg001_07', 6)	# 37-42
    sprite('rg001_08', 6)	# 43-48
    sprite('rg001_09', 6)	# 49-54
    sprite('rg001_10', 6)	# 55-60
    sprite('rg001_11', 6)	# 61-66
    sprite('rg001_12', 6)	# 67-72
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 73-78
    sprite('rg001_14', 6)	# 79-84
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 85-90
    sprite('rg001_16', 6)	# 91-96
    sprite('rg000_00', 1)	# 97-97
    loopRest()
    enterState('CmnActStand')

@State
def EventLosePunch():
    sprite('rg620_05', 6)	# 1-6
    sprite('rg620_04', 8)	# 7-14
    sprite('rg620_05', 32767)	# 15-32781
    Unknown8000(100, 1, 0)
    SFX_0('100_hit_grap_1')

@State
def EventMUVsRG_FallDown():
    teleportRelativeY(1000000)
    physicsYImpulse(-20000)
    Unknown1043()
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_2')
    label(0)
    sprite('rg060_05', 4)	# 1-4
    sprite('rg060_06', 4)	# 5-8
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    sprite('rg060_07', 2)	# 9-10
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    SFX_0('209_down_normal_0')
    GFX_1('ef_smokedwn', -1)
    GFX_1('ef_hitmd', 104)
    sprite('rg060_08', 2)	# 11-12
    physicsYImpulse(30000)
    setGravity(15000)
    sprite('rg060_09', 1)	# 13-13
    physicsYImpulse(0)
    Unknown1043()
    sprite('rg060_09', 2)	# 14-15
    sprite('rg060_10', 3)	# 16-18
    sprite('rg060_11', 2)	# 19-20
    sprite('rg060_11', 1)	# 21-21
    physicsYImpulse(20000)
    setGravity(10000)
    sprite('rg060_12', 1)	# 22-22
    sprite('rg060_12', 3)	# 23-25
    physicsYImpulse(0)
    Unknown1043()
    sprite('rg060_13', 3)	# 26-28
    sprite('rg060_14', 32767)	# 29-32795
    Unknown1084(1)
    teleportRelativeY(0)
    loopRest()

@State
def EventMUVsRG_StandUp():
    sprite('rg061_00', 6)	# 1-6
    sprite('rg061_01', 6)	# 7-12
    sprite('rg061_00', 6)	# 13-18
    sprite('rg061_01', 6)	# 19-24
    sprite('rg061_02', 6)	# 25-30
    sprite('rg061_03', 6)	# 31-36
    sprite('rg061_02', 6)	# 37-42
    sprite('rg061_03', 12)	# 43-54
    sprite('rg061_04', 6)	# 55-60
    sprite('rg061_05', 6)	# 61-66
    SFX_3('rgse_00')
    sprite('rg061_06', 20)	# 67-86
    sprite('rg061_07', 10)	# 87-96
    sprite('rg061_08', 8)	# 97-104
    sprite('rg061_09', 8)	# 105-112
    sprite('rg061_10', 8)	# 113-120
    loopRest()
    enterState('CmnActStand')

@State
def EventMUVsRG_Stop():
    sprite('keep', 4)	# 1-4
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 5-8
    sprite('keep', 4)	# 9-12
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 13-16
    sprite('keep', 4)	# 17-20
    ScreenShake(5000, 10000)
    GFX_0('NOISE', -1)
    SFX_0('023_noize')
    sprite('keep', 4)	# 21-24
    sprite('keep', 4)	# 25-28
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 29-32
    sprite('keep', 4)	# 33-36
    ScreenShake(5000, 10000)
    sprite('keep', 4)	# 37-40
    sprite('keep', 4)	# 41-44
    ScreenShake(5000, 10000)
    sprite('keep', 32767)	# 45-32811
    loopRest()
    sprite('keep', 32767)	# 32812-65578
    loopRest()

@State
def EventHZVsRG_Kerare():
    Unknown1000(-40000)
    EnableCollision(0)
    sendToLabelUpon(32, 1)
    sendToLabelUpon(33, 2)
    label(0)
    sprite('rg063_11', 1)	# 1-1
    loopRest()
    gotoLabel(0)
    label(1)
    GFX_1('ef_hitmd', 104)
    sprite('rg063_11', 4)	# 2-5
    sprite('rg063_06', 2)	# 6-7
    sprite('rg063_09', 3)	# 8-10
    sprite('rg063_10', 3)	# 11-13
    loopRest()
    gotoLabel(0)
    label(2)
    GFX_1('ef_exhit_sub', 104)
    sprite('rg063_11', 4)	# 14-17
    sprite('rg063_06', 2)	# 18-19
    sprite('rg063_07', 2)	# 20-21
    sprite('rg063_08', 3)	# 22-24
    sprite('rg063_09', 3)	# 25-27
    sprite('rg063_10', 3)	# 28-30
    loopRest()
    gotoLabel(0)

@State
def EventRGAppear():
    sprite('rg600_00', 6)	# 1-6
    Unknown3001(0)
    Unknown3004(5)
    SFX_0('000_airdash_0')
    sprite('rg600_00ex01', 6)	# 7-12
    sprite('rg600_00ex02', 6)	# 13-18
    sprite('rg600_01', 6)	# 19-24
    sprite('rg600_01ex01', 6)	# 25-30
    sprite('rg600_00', 6)	# 31-36
    sprite('rg600_00ex01', 6)	# 37-42
    sprite('rg600_00ex02', 6)	# 43-48
    sprite('rg600_01', 6)	# 49-54
    sprite('rg600_01ex01', 6)	# 55-60
    loopRest()
    label(0)
    sprite('rg600_00', 6)	# 61-66
    sprite('rg600_00ex01', 6)	# 67-72
    sprite('rg600_00ex02', 6)	# 73-78
    sprite('rg600_01', 6)	# 79-84
    sprite('rg600_01ex01', 6)	# 85-90
    sprite('rg600_00', 6)	# 91-96
    sprite('rg600_00ex01', 6)	# 97-102
    sprite('rg600_00ex02', 6)	# 103-108
    sprite('rg600_01', 6)	# 109-114
    sprite('rg600_01ex01', 6)	# 115-120
    loopRest()
    gotoLabel(0)

@State
def EventRGAppearToStand():
    sprite('rg600_00', 6)	# 1-6
    sprite('rg600_00ex01', 6)	# 7-12
    sprite('rg600_00ex02', 6)	# 13-18
    sprite('rg600_01', 6)	# 19-24
    sprite('rg600_01ex01', 6)	# 25-30
    sprite('rg600_02', 6)	# 31-36
    sprite('rg600_03', 6)	# 37-42
    sprite('rg600_04', 6)	# 43-48
    sprite('rg600_05', 6)	# 49-54
    sprite('rg600_06', 10)	# 55-64
    sprite('rg600_07', 4)	# 65-68
    sprite('rg600_08', 4)	# 69-72
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 73-78
    sprite('rg600_10', 6)	# 79-84
    sprite('rg600_11', 6)	# 85-90
    sprite('rg600_12', 35)	# 91-125
    SFX_3('rgse_00')
    sprite('rg600_13', 6)	# 126-131
    sprite('rg600_14', 6)	# 132-137
    sprite('rg600_15', 6)	# 138-143
    sprite('rg600_16', 6)	# 144-149
    loopRest()
    enterState('CmnActStand')

@State
def EventRGDown():
    sprite('rg060_14', 32767)	# 1-32767

@State
def EventRGDisappear():
    sprite('rg620_05', 30)	# 1-30
    sprite('rg620_05', 32767)	# 31-32797
    Unknown3004(-5)
    SFX_0('000_airdash_2')

@State
def EventRGWalkIn():
    Unknown2034(0)
    Unknown1000(-900000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(4650)
    label(0)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_03', 7)	# 22-28
    sprite('rg030_04', 7)	# 29-35
    sprite('rg030_05', 7)	# 36-42
    sprite('rg030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_07', 7)	# 50-56
    sprite('rg030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventRGDashScreenOut():
    sprite('rg032_00', 2)	# 1-2
    Unknown2034(0)
    EnableCollision(0)
    sprite('rg032_01', 2)	# 3-4
    physicsXImpulse(27000)
    SFX_3('rgse_00')
    label(0)
    sprite('rg032_02', 4)	# 5-8
    sprite('rg032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 13-16
    sprite('rg032_04', 4)	# 17-20
    sprite('rg032_05', 4)	# 21-24
    sprite('rg032_06', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('rg032_06add', 4)	# 29-32
    sprite('rg032_07', 4)	# 33-36
    gotoLabel(0)

@State
def EventRGReaction2():
    sprite('rg310_00', 6)	# 1-6
    sprite('rg310_01', 6)	# 7-12
    sprite('rg310_02', 6)	# 13-18	 **attackbox here**
    sprite('rg311_00', 6)	# 19-24
    sprite('rg311_01', 6)	# 25-30
    sprite('rg311_02', 40)	# 31-70
    sprite('rg311_01', 6)	# 71-76
    sprite('rg311_00', 6)	# 77-82
    sprite('rg310_02', 6)	# 83-88	 **attackbox here**
    sprite('rg310_01', 6)	# 89-94
    enterState('CmnActStand')

@State
def EventRGDog():
    sprite('rg408_00', 2)	# 1-2
    sprite('rg408_01', 2)	# 3-4
    sprite('rg408_02', 2)	# 5-6
    SFX_1('rg207')
    sprite('rg408_03', 3)	# 7-9
    sprite('rg408_04', 3)	# 10-12
    sprite('rg408_05', 3)	# 13-15
    sprite('rg408_06', 2)	# 16-17
    sprite('rg408_07', 2)	# 18-19
    sprite('rg408_08', 2)	# 20-21
    GFX_0('EventDogD', -1)
    SFX_3('rgse_06')
    sprite('rg408_09', 6)	# 22-27
    sprite('rg408_10', 5)	# 28-32
    SFX_3('rgse_21')
    sprite('rg408_11', 5)	# 33-37
    sprite('rg408_12', 5)	# 38-42
    sprite('rg408_13', 2)	# 43-44
    sprite('rg408_14', 2)	# 45-46
    sprite('rg408_15', 2)	# 47-48
    sprite('rg408_16', 2)	# 49-50
    sprite('rg408_17', 2)	# 51-52
    sprite('rg408_18', 2)	# 53-54
    sprite('rg408_19', 2)	# 55-56
    sprite('rg408_20', 1)	# 57-57

@State
def EventRGDashIn():
    Unknown2034(0)
    Unknown1000(-900000)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('rg032_00', 2)	# 1-2
    Unknown2034(0)
    EnableCollision(0)
    sprite('rg032_01', 2)	# 3-4
    physicsXImpulse(18000)
    SFX_3('rgse_00')
    label(0)
    sprite('rg032_02', 4)	# 5-8
    sprite('rg032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 13-16
    sprite('rg032_04', 4)	# 17-20
    sprite('rg032_05', 4)	# 21-24
    sprite('rg032_06', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('rg032_06add', 4)	# 29-32
    sprite('rg032_07', 4)	# 33-36
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventRGThinkng():
    sprite('rg431_16', 6)	# 1-6
    sprite('rg431_15', 6)	# 7-12
    sprite('rg431_14', 6)	# 13-18
    sprite('rg431_13', 32767)	# 19-32785

@State
def EventRGThinkngEnd():
    sprite('rg431_14', 8)	# 1-8
    sprite('rg431_15', 8)	# 9-16
    sprite('rg431_16', 8)	# 17-24
    enterState('CmnActStand')

@State
def EventRGThinkng2():
    sprite('rg460_00', 6)	# 1-6
    label(0)
    sprite('rg460_01', 6)	# 7-12
    sprite('rg460_02', 6)	# 13-18
    sprite('rg460_03', 6)	# 19-24
    gotoLabel(0)

@State
def EventRGThinkng2End():
    sprite('rg460_00', 12)	# 1-12
    enterState('CmnActStand')

@State
def EventRGDefLose():
    sprite('rg620_00', 6)	# 1-6
    sprite('rg620_01', 6)	# 7-12
    sprite('rg620_02', 6)	# 13-18
    sprite('rg620_03', 6)	# 19-24
    sprite('rg620_04', 6)	# 25-30
    SFX_3('rgse_00')
    sprite('rg620_05', 32767)	# 31-32797

@State
def EventRGDefLoseEnd():
    sprite('rg620_05', 6)	# 1-6
    sprite('rg620_04', 6)	# 7-12
    sprite('rg620_03', 6)	# 13-18
    sprite('rg620_02', 6)	# 19-24
    sprite('rg620_01', 6)	# 25-30
    sprite('rg620_00', 6)	# 31-36
    enterState('CmnActStand')

@State
def EventRGWin2ReverseWait():
    sprite('rg600_12', 32767)	# 1-32767

@State
def EventRGWin2Reverse():
    sprite('rg600_16', 6)	# 1-6
    SFX_0('006_swing_blade_2')
    sprite('rg600_15', 6)	# 7-12
    sprite('rg600_14', 6)	# 13-18
    sprite('rg600_13', 6)	# 19-24
    sprite('rg600_12', 6)	# 25-30
    SFX_3('rgse_00')
    sprite('rg600_11', 6)	# 31-36
    sprite('rg600_10', 6)	# 37-42
    sprite('rg600_09', 6)	# 43-48
    sprite('rg600_10', 6)	# 49-54
    sprite('rg600_11', 6)	# 55-60
    sprite('rg600_12', 32767)	# 61-32827

@State
def EventRGWin2ReverseEnd():
    sprite('rg600_13', 6)	# 1-6
    sprite('rg600_14', 6)	# 7-12
    sprite('rg600_15', 6)	# 13-18
    sprite('rg600_16', 6)	# 19-24
    enterState('CmnActStand')

@State
def EventRGWin2():
    label(0)
    sprite('rg600_00', 6)	# 1-6
    sprite('rg600_00ex01', 6)	# 7-12
    sprite('rg600_00ex02', 6)	# 13-18
    sprite('rg600_01', 6)	# 19-24
    sprite('rg600_01ex01', 6)	# 25-30
    gotoLabel(0)

@State
def EventRGWin2End():
    sprite('rg600_00', 6)	# 1-6
    sprite('rg600_01', 6)	# 7-12
    sprite('rg600_02', 6)	# 13-18
    sprite('rg600_03', 6)	# 19-24
    sprite('rg600_04', 6)	# 25-30
    sprite('rg600_05', 6)	# 31-36
    sprite('rg600_06', 6)	# 37-42
    sprite('rg600_07', 6)	# 43-48
    sprite('rg600_08', 6)	# 49-54
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 55-60
    sprite('rg600_10', 6)	# 61-66
    sprite('rg600_11', 6)	# 67-72
    sprite('rg600_12', 6)	# 73-78
    SFX_3('rgse_00')
    sprite('rg600_13', 6)	# 79-84
    sprite('rg600_14', 6)	# 85-90
    sprite('rg600_15', 6)	# 91-96
    sprite('rg600_16', 6)	# 97-102
    enterState('CmnActStand')

@State
def EventRGCrouch():
    label(0)
    sprite('rg010_02', 6)	# 1-6
    sprite('rg010_03', 6)	# 7-12
    sprite('rg010_04', 6)	# 13-18
    sprite('rg010_05', 6)	# 19-24
    sprite('rg010_06', 6)	# 25-30
    sprite('rg010_07', 6)	# 31-36
    sprite('rg010_08', 6)	# 37-42
    sprite('rg010_07', 6)	# 43-48
    sprite('rg010_06', 6)	# 49-54
    sprite('rg010_05', 6)	# 55-60
    sprite('rg010_04', 6)	# 61-66
    sprite('rg010_03', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def EventWalkFrameIn():
    Unknown2034(0)
    Unknown2037(1)
    Unknown1000(-900000)

    def upon_CLEAR_OR_EXIT():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            sendToLabel(1)
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(4650)
    label(0)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_03', 7)	# 22-28
    sprite('rg030_04', 7)	# 29-35
    sprite('rg030_05', 7)	# 36-42
    sprite('rg030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_07', 7)	# 50-56
    SFX_3('rgse_00')
    sprite('rg030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventRGvsTBActionStart():

    def upon_IMMEDIATE():
        setInvincible(1)
        sendToLabelUpon(32, 10)
        Unknown1084(1)
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(4300)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_03', 7)	# 22-28
    sprite('rg030_04', 7)	# 29-35
    loopRest()
    label(5)
    sprite('rg000_00', 7)	# 36-42
    Unknown1084(1)
    sprite('rg000_01', 7)	# 43-49
    sprite('rg000_02', 7)	# 50-56
    sprite('rg000_03', 7)	# 57-63
    sprite('rg000_04', 7)	# 64-70
    sprite('rg000_05', 7)	# 71-77
    sprite('rg000_06', 7)	# 78-84
    sprite('rg000_05', 7)	# 85-91
    sprite('rg000_04', 7)	# 92-98
    sprite('rg000_03', 7)	# 99-105
    sprite('rg000_02', 7)	# 106-112
    sprite('rg000_01', 7)	# 113-119
    gotoLabel(5)
    label(10)
    sprite('rg033_00', 1)	# 120-120
    sprite('rg033_01', 2)	# 121-122
    SFX_3('rgse_00')
    physicsXImpulse(-12000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rg033_02', 2)	# 123-124
    sendToLabelUpon(2, 1)
    sprite('rg033_02', 1)	# 125-125
    setInvincible(0)
    sprite('rg033_03', 3)	# 126-128
    loopRest()
    label(0)
    sprite('rg033_02', 3)	# 129-131
    sprite('rg033_03', 3)	# 132-134
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg033_04', 2)	# 135-136
    setInvincible(1)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('rg033_05', 2)	# 137-138
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventVHvsRGDash():
    Unknown2034(0)
    sprite('rg032_00', 2)	# 1-2
    sprite('rg032_01', 2)	# 3-4
    physicsXImpulse(18000)
    sprite('rg032_02', 4)	# 5-8
    sprite('rg032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 13-16
    sprite('rg032_04', 4)	# 17-20
    physicsXImpulse(0)
    loopRest()
    enterState('CmnActStand')

@State
def EventRGThinkng2():
    sprite('rg460_00', 6)	# 1-6
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3074('00000000ff000000000000007f000000')
    Unknown3075('000000007f00000000000000ff000000')
    Unknown3076(1010)
    Unknown3077(1100)
    Unknown2004(1, 1)
    label(0)
    sprite('rg460_01', 6)	# 7-12
    sprite('rg460_02', 6)	# 13-18
    sprite('rg460_03', 6)	# 19-24
    gotoLabel(0)

@State
def EventRGVsCEAction01():

    def upon_IMMEDIATE():
        Unknown21007(22, 32)
    sprite('rg331_00', 6)	# 1-6
    sprite('rg331_01', 6)	# 7-12
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3074('00000000ff000000000000007f000000')
    Unknown3075('000000007f00000000000000ff000000')
    Unknown3076(1010)
    Unknown3077(1100)
    Unknown2004(1, 1)
    label(0)
    sprite('rg331_02', 6)	# 13-18
    ScreenShake(500, 3000)
    SFX_0('019_quake_0')
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    GFX_0('Eventrgef_drains2', -1)
    sprite('rg331_03', 6)	# 19-24
    ScreenShake(500, 3000)
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    gotoLabel(0)

@State
def EventRGVsCEAction02():
    loopRelated(17, 300)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('rg331_02', 6)	# 1-6
    ScreenShake(500, 8000)
    SFX_0('019_quake_1')
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    GFX_0('Eventrgef_drains2', -1)
    sprite('rg331_03', 6)	# 7-12
    ScreenShake(500, 8000)
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    gotoLabel(0)
    sprite('rg331_04', 2)	# 13-14
    SFX_0('019_quake_1')
    sprite('rg331_05', 2)	# 15-16
    label(1)
    sprite('rg331_06', 6)	# 17-22
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    GFX_0('Eventrgef_drains3', -1)
    SFX_3('rgse_01')
    SFX_3('rgse_02')
    SFX_3('rgse_03')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('rg331_07', 6)	# 23-28
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    sprite('rg331_08', 6)	# 29-34
    GFX_0('Eventrgef_drains', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    label(2)
    sprite('rg331_06', 6)	# 35-40
    GFX_0('Eventrgef_drains', -1)
    ScreenShake(500, 4000)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('rg331_07', 6)	# 41-46
    GFX_0('Eventrgef_drains', -1)
    ScreenShake(500, 4000)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    sprite('rg331_08', 6)	# 47-52
    GFX_0('Eventrgef_drains', -1)
    ScreenShake(500, 4000)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    gotoLabel(2)
    sprite('rg331_09', 6)	# 53-58
    sprite('rg331_10', 6)	# 59-64
    loopRest()
    enterState('CmnActStand')

@State
def EventRGVsCEAction03():
    sprite('rg331_06', 6)	# 1-6
    sprite('rg331_07', 6)	# 7-12
    sprite('rg331_08', 6)	# 13-18
    sprite('rg331_09', 8)	# 19-26
    sprite('rg331_10', 8)	# 27-34
    loopRest()
    enterState('CmnActStand')

@State
def EventBDash():
    label(10)
    sprite('rg033_00', 1)	# 1-1
    sprite('rg033_01', 2)	# 2-3
    SFX_3('rgse_00')
    physicsXImpulse(-17000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rg033_02', 2)	# 4-5
    sendToLabelUpon(2, 1)
    sprite('rg033_02', 1)	# 6-6
    setInvincible(0)
    sprite('rg033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('rg033_02', 3)	# 10-12
    sprite('rg033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg033_04', 2)	# 16-17
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('rg033_05', 2)	# 18-19
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventVsCEStandWait():

    def upon_IMMEDIATE():
        Unknown1000(0)
    sprite('rg460_00', 6)	# 1-6
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3074('00000000ff000000000000007f000000')
    Unknown3075('000000007f00000000000000ff000000')
    Unknown3076(1010)
    Unknown3077(1100)
    Unknown2004(1, 1)
    label(0)
    sprite('rg460_01', 6)	# 7-12
    sprite('rg460_02', 6)	# 13-18
    sprite('rg460_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def EventVsCEBWalk():
    Unknown2034(0)
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(-1650)
    sprite('rg031_00', 7)	# 8-14
    label(0)
    sprite('rg031_01', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg031_02', 7)	# 22-28
    sprite('rg031_03', 7)	# 29-35
    sprite('rg031_04', 7)	# 36-42
    sprite('rg031_05', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg031_06', 7)	# 50-56
    sprite('rg031_07', 7)	# 57-63
    SFX_3('rgse_00')
    sprite('rg031_08', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def HAKUMEN_NOUNAI():
    sprite('keep', 2)	# 1-2
    GFX_0('HAKUMEN_NOUNAI', -1)
    loopRest()
    enterState('CmnActStand')

@State
def HAKUMEN_NOUNAI_OWARI():
    sprite('keep', 2)	# 1-2
    Unknown21012('48414b554d454e5f4e4f554e414900000000000000000000000000000000000020000000')
    loopRest()
    enterState('CmnActStand')

@State
def EventVSAZ01():
    sprite('keep', 32767)	# 1-32767
    GFX_0('EventRC', -1)
    enterState('CmnActStand')

@State
def EventVSAZ02():
    sprite('keep', 1)	# 1-1
    Unknown21012('4576656e7452430000000000000000000000000000000000000000000000000020000000')
    enterState('CmnActStand')

@State
def EventJumpAssaultToBDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11097(300, 300)
        ChipDamagePct(0)
        AttackLevel_(5)
        Unknown1000(-400000)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(2)
    sprite('rg412_00', 4)	# 1-4
    setInvincible(1)
    sprite('rg412_01', 3)	# 5-7
    Unknown8001(3, 100)
    physicsXImpulse(15000)
    physicsYImpulse(42000)
    setGravity(2200)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    sprite('rg412_02', 3)	# 8-10
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3074('00000000ff000000000000007f000000')
    Unknown3075('000000007f00000000000000ff000000')
    Unknown3076(1010)
    Unknown3077(1100)
    Unknown2004(1, 1)
    sprite('rg412_03', 3)	# 11-13
    sprite('rg412_04', 3)	# 14-16
    sprite('rg412_05', 8)	# 17-24
    Unknown2015(150)
    sprite('rg412_06', 4)	# 25-28
    Unknown23087(120000)
    GFX_0('rgef412effpos', -1)
    Unknown1019(80)
    sprite('rg412_07', 4)	# 29-32
    Unknown1019(80)
    SFX_0('010_swing_sword_2')
    sprite('rg412_08', 4)	# 33-36
    Unknown1019(80)
    sprite('rg412_09', 3)	# 37-39	 **attackbox here**
    sprite('rg412_10', 2)	# 40-41
    Recovery()
    sprite('rg412_11', 2)	# 42-43
    sprite('rg412_12', 2)	# 44-45
    sprite('rg412_13', 32767)	# 46-32812
    Unknown2015(-1)
    label(2)
    sprite('rg412_14', 2)	# 32813-32814
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    setInvincible(0)
    sprite('rg024_02', 2)	# 32815-32816
    sprite('rg024_03', 2)	# 32817-32818
    sprite('rg024_04', 2)	# 32819-32820
    sprite('rg033_00', 1)	# 32821-32821
    sprite('rg033_01', 2)	# 32822-32823
    SFX_3('rgse_00')
    physicsXImpulse(-25000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rg033_02', 2)	# 32824-32825
    clearUponHandler(2)
    sendToLabelUpon(2, 4)
    sprite('rg033_02', 1)	# 32826-32826
    setInvincible(0)
    sprite('rg033_03', 3)	# 32827-32829
    loopRest()
    label(3)
    sprite('rg033_02', 3)	# 32830-32832
    sprite('rg033_03', 3)	# 32833-32835
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('rg033_04', 2)	# 32836-32837
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('rg033_05', 2)	# 32838-32839
    sprite('rg300_00', 4)	# 32840-32843
    sprite('rg300_01', 4)	# 32844-32847
    sprite('rg300_02', 4)	# 32848-32851
    sprite('rg300_03', 6)	# 32852-32857
    sprite('rg300_04', 6)	# 32858-32863
    sprite('rg300_05', 7)	# 32864-32870
    sprite('rg300_04', 6)	# 32871-32876
    sprite('rg300_05', 7)	# 32877-32883
    sprite('rg300_03', 9)	# 32884-32892
    sprite('rg300_06', 6)	# 32893-32898
    sprite('rg300_07', 6)	# 32899-32904
    sprite('rg300_08', 6)	# 32905-32910
    loopRest()
    enterState('CmnActStand')

@State
def EventDashWhiteout():
    sprite('rg032_00', 2)	# 1-2
    Unknown2034(0)
    EnableCollision(0)
    sprite('rg032_01', 2)	# 3-4
    physicsXImpulse(27000)
    SFX_3('rgse_00')
    GFX_0('EventWhiteOut', -1)
    label(0)
    sprite('rg032_02', 4)	# 5-8
    sprite('rg032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 13-16
    sprite('rg032_04', 4)	# 17-20
    sprite('rg032_05', 4)	# 21-24
    sprite('rg032_06', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('rg032_06add', 4)	# 29-32
    sprite('rg032_07', 4)	# 33-36
    gotoLabel(0)

@State
def Act2Event_ntvsrg_00():
    sprite('null', 32767)	# 1-32767
    Unknown1000(-360000)
    loopRest()

@State
def Act2Event_ntvsrg_01():
    label(0)
    sprite('rg000_00', 7)	# 1-7
    sprite('rg000_01', 7)	# 8-14
    sprite('rg000_02', 7)	# 15-21
    sprite('rg000_03', 7)	# 22-28
    sprite('rg000_04', 7)	# 29-35
    sprite('rg000_05', 7)	# 36-42
    sprite('rg000_06', 7)	# 43-49
    sprite('rg000_05', 7)	# 50-56
    sprite('rg000_04', 7)	# 57-63
    sprite('rg000_03', 7)	# 64-70
    sprite('rg000_02', 7)	# 71-77
    sprite('rg000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def Act2Event_ntvsrg_02():
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(4000)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg600_16', 5)	# 22-26
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('rg600_15', 5)	# 27-31
    sprite('rg600_14', 5)	# 32-36
    sprite('rg600_04', 5)	# 37-41
    sprite('rg600_05', 5)	# 42-46
    sprite('rg600_06', 24)	# 47-70
    sprite('rg600_07', 4)	# 71-74
    sprite('rg600_08', 4)	# 75-78
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 79-84
    sprite('rg600_10', 6)	# 85-90
    sprite('rg600_11', 6)	# 91-96
    sprite('rg600_12', 15)	# 97-111
    SFX_3('rgse_00')
    sprite('rg600_13', 6)	# 112-117
    sprite('rg600_14', 6)	# 118-123
    sprite('rg600_15', 6)	# 124-129
    sprite('rg600_16', 6)	# 130-135
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ntvsrg_03():
    sprite('rg300_05', 1)	# 1-1
    sendToLabelUpon(32, 1)
    sprite('rg300_05', 32767)	# 2-32768
    label(1)
    sprite('rg300_05', 60)	# 32769-32828
    Unknown3004(-4)
    sprite('null', 32767)	# 32829-65595
    Unknown3001(0)
    loopRest()

@State
def Act2Event_phvsrg_00():

    def upon_IMMEDIATE():

        def upon_32():
            sendToLabel(0)
            GFX_1('ef_exhit_sub', 104)
            SFX_0('100_hit_grap_3')
            SFX_0('209_down_normal_0')

        def upon_33():
            sendToLabel(1)
    label(9)
    sprite('rg063_11', 32767)	# 1-32767
    Unknown1084(1)
    loopRest()
    label(0)
    sprite('rg063_11', 4)	# 32768-32771
    sprite('rg063_06', 2)	# 32772-32773
    physicsYImpulse(8000)
    setGravity(2000)
    sprite('rg063_07', 2)	# 32774-32775
    sprite('rg063_08', 3)	# 32776-32778
    sprite('rg063_09', 3)	# 32779-32781
    sprite('rg063_10', 3)	# 32782-32784
    GFX_1('ef_grndshock', 104)
    SFX_0('209_down_normal_0')
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('rg064_00', 4)	# 32785-32788
    sprite('rg064_01', 4)	# 32789-32792
    sprite('rg064_02', 5)	# 32793-32797
    sprite('rg064_03', 5)	# 32798-32802
    sprite('rg064_04', 5)	# 32803-32807
    sprite('rg063_05', 12)	# 32808-32819
    GFX_1('ef_exhit_sub', 104)
    SFX_0('100_hit_grap_3')
    ScreenShake(3000, 18000)
    sprite('rg063_06', 2)	# 32820-32821
    physicsYImpulse(6000)
    setGravity(2000)
    sprite('rg063_07', 2)	# 32822-32823
    sprite('rg063_08', 3)	# 32824-32826
    sprite('rg063_09', 3)	# 32827-32829
    sprite('rg063_10', 3)	# 32830-32832
    GFX_1('ef_grndshock', 104)
    SFX_0('209_down_normal_0')
    loopRest()
    gotoLabel(9)

@State
def Act2Event_phvsrg_01():
    sprite('keep', 1)	# 1-1
    GFX_0('Act2Event_Yure', -1)
    sprite('keep', 32767)	# 2-32768
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
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(5000)
    label(9)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_03', 7)	# 22-28
    sprite('rg030_04', 7)	# 29-35
    sprite('rg030_05', 7)	# 36-42
    sprite('rg030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_07', 7)	# 50-56
    SFX_3('rgse_00')
    sprite('rg030_08', 7)	# 57-63
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('rg000_00', 1)	# 64-64
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Reaction():
    sprite('rg001_00', 6)	# 1-6
    sprite('rg001_01', 6)	# 7-12
    sprite('rg001_02', 6)	# 13-18
    sprite('rg001_03', 6)	# 19-24
    sprite('rg001_04', 6)	# 25-30
    sprite('rg001_05', 6)	# 31-36
    sprite('rg001_06', 6)	# 37-42
    sprite('rg001_07', 6)	# 43-48
    sprite('rg001_08', 6)	# 49-54
    sprite('rg001_09', 6)	# 55-60
    sprite('rg001_10', 6)	# 61-66
    sprite('rg001_11', 6)	# 67-72
    sprite('rg001_12', 6)	# 73-78
    SFX_0('019_cloth_a')
    sprite('rg001_13', 6)	# 79-84
    sprite('rg001_14', 6)	# 85-90
    SFX_3('rgse_00')
    sprite('rg001_15', 6)	# 91-96
    sprite('rg001_16', 6)	# 97-102
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Chouhatsu():
    sprite('rg300_00', 4)	# 1-4
    sprite('rg300_01', 4)	# 5-8
    sprite('rg300_02', 4)	# 9-12
    sprite('rg300_03', 6)	# 13-18
    sprite('rg300_04', 6)	# 19-24
    sprite('rg300_05', 7)	# 25-31
    sprite('rg300_04', 6)	# 32-37
    sprite('rg300_05', 7)	# 38-44
    sprite('rg300_03', 6)	# 45-50
    sprite('rg300_06', 6)	# 51-56
    sprite('rg300_07', 6)	# 57-62
    sprite('rg300_08', 6)	# 63-68
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ChouhatsuLoop():
    sprite('rg300_00', 4)	# 1-4
    sprite('rg300_01', 4)	# 5-8
    sprite('rg300_02', 4)	# 9-12
    sprite('rg300_03', 6)	# 13-18
    sprite('rg300_04', 6)	# 19-24
    sprite('rg300_05', 32767)	# 25-32791

@State
def Act2Event_ChouhatsuEnd():
    sprite('rg300_03', 6)	# 1-6
    sprite('rg300_06', 6)	# 7-12
    sprite('rg300_07', 6)	# 13-18
    sprite('rg300_08', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Hiza():
    sprite('rg061_06', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_HizaEnd():
    sprite('rg061_07', 5)	# 1-5
    Unknown21007(22, 32)
    sprite('rg061_08', 5)	# 6-10
    sprite('rg061_09', 5)	# 11-15
    sprite('rg061_10', 5)	# 16-20
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ptvsrg_00():

    def upon_IMMEDIATE():
        EnableCollision(0)
    sprite('rg071_00', 4)	# 1-4
    SFX_1('rg028')
    sprite('rg071_01', 4)	# 5-8
    Unknown1047(-5000)
    Unknown2037(2)
    label(0)
    sprite('rg071_02', 2)	# 9-10
    Unknown2038(-1)
    sprite('rg071_03', 2)	# 11-12
    sprite('rg071_04', 2)	# 13-14
    sprite('rg071_05', 2)	# 15-16
    sprite('rg071_06', 2)	# 17-18
    sprite('rg071_07', 2)	# 19-20
    sprite('rg071_08', 2)	# 21-22
    sprite('rg071_09', 2)	# 23-24
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('rg071_10', 6)	# 25-30
    sprite('rg071_11', 5)	# 31-35
    sprite('rg071_12', 5)	# 36-40
    sprite('rg060_07', 3)	# 41-43
    teleportRelativeX(-120000)
    sprite('rg060_08', 3)	# 44-46
    SFX_0('209_down_normal_0')
    sprite('rg060_09', 3)	# 47-49
    physicsXImpulse(-2000)
    physicsYImpulse(12000)
    Unknown1043()
    sprite('rg060_10', 3)	# 50-52
    sprite('rg060_11', 3)	# 53-55
    sprite('rg060_12', 3)	# 56-58
    sprite('rg060_13', 3)	# 59-61
    sprite('rg060_14', 32767)	# 62-32828
    Unknown1084(1)
    loopRest()

@State
def Act2Event_Kaze():
    sprite('rg040_00', 4)	# 1-4
    sprite('rg040_01', 4)	# 5-8
    label(0)
    sprite('rg040_02', 5)	# 9-13
    sprite('rg040_02ex', 5)	# 14-18
    loopRest()
    gotoLabel(0)

@State
def Act2Event_KazeEnd():
    sprite('keep', 2)	# 1-2
    sprite('rg040_01', 4)	# 3-6
    sprite('rg040_00', 4)	# 7-10
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvsmk_00():
    sprite('rg600_16', 5)	# 1-5
    sprite('rg600_15', 5)	# 6-10
    sprite('rg600_14', 5)	# 11-15
    sprite('rg600_04', 5)	# 16-20
    sprite('rg600_05', 5)	# 21-25
    sprite('rg600_06', 24)	# 26-49
    sprite('rg600_07', 4)	# 50-53
    sprite('rg600_08', 4)	# 54-57
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 58-63
    sprite('rg600_10', 6)	# 64-69
    sprite('rg600_11', 6)	# 70-75
    sprite('rg600_12', 15)	# 76-90
    SFX_3('rgse_00')
    sprite('rg600_13', 6)	# 91-96
    sprite('rg600_14', 6)	# 97-102
    sprite('rg600_15', 6)	# 103-108
    sprite('rg600_16', 6)	# 109-114
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvsmk_01():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('rg211_07', 2)	# 1-2
    SFX_0('004_swing_grap_1_2')
    sprite('rg211_08', 2)	# 3-4
    sprite('rg211_09', 11)	# 5-15	 **attackbox here**
    sprite('rg211_10', 4)	# 16-19	 **attackbox here**
    sprite('rg211_11', 4)	# 20-23	 **attackbox here**
    sprite('rg211_12', 4)	# 24-27
    sprite('rg211_13', 4)	# 28-31
    sprite('rg211_14', 5)	# 32-36
    sprite('rg211_15', 5)	# 37-41
    sprite('rg211_16', 5)	# 42-46
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvsmk_02():
    sprite('rg610_00', 1)	# 1-1
    sprite('rg610_00', 3)	# 2-4
    sprite('rg610_01', 3)	# 5-7
    sprite('rg610_02', 3)	# 8-10
    SFX_0('007_swing_knife_1')
    GFX_0('rgef610wingmake', -1)
    sprite('rg610_03', 3)	# 11-13
    sprite('rg610_04', 3)	# 14-16
    sprite('rg610_05', 3)	# 17-19
    sprite('rg610_06', 6)	# 20-25
    sprite('rg610_07', 2)	# 26-27
    GFX_0('rgef610wingbreak', -1)
    SFX_0('019_cloth_c')
    sprite('rg610_08', 6)	# 28-33
    SFX_0('210_down_garden_1')
    sprite('rg610_09', 6)	# 34-39
    sprite('rg610_10', 6)	# 40-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg610_11', 32767)	# 46-32812
    loopRest()

@State
def Act3Event_rgvstb_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('rg202_05', 2)	# 1-2
    SFX_0('008_swing_pole_2')
    sprite('rg202_06', 2)	# 3-4
    sprite('rg202_07', 2)	# 5-6
    sprite('rg202_08', 1)	# 7-7	 **attackbox here**
    sprite('rg202_09', 16)	# 8-23	 **attackbox here**
    sprite('rg202_10', 4)	# 24-27
    sprite('rg202_11', 4)	# 28-31
    sprite('rg202_12', 4)	# 32-35
    sprite('rg202_13', 4)	# 36-39
    sprite('rg202_14', 4)	# 40-43
    sprite('rg202_15', 4)	# 44-47
    sprite('rg202_16', 5)	# 48-52
    sprite('rg202_17', 5)	# 53-57
    sprite('rg202_18', 4)	# 58-61
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvskg_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('rg040_02ex', 5)	# 1-5
    sprite('rg090_00', 12)	# 6-17
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('rg090_01', 7)	# 18-24
    Unknown1047(-11000)
    sprite('rg090_02', 7)	# 25-31
    sprite('rg090_03', 7)	# 32-38
    sprite('rg090_04', 7)	# 39-45
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvskg_01():
    sprite('rg040_00', 4)	# 1-4
    GFX_0('Noise_Long', 0)
    Unknown38(4, 1)
    sprite('rg040_01', 4)	# 5-8
    sprite('rg040_02', 5)	# 9-13
    sprite('rg040_02ex', 5)	# 14-18
    sprite('rg040_01', 4)	# 19-22
    sprite('rg040_00', 4)	# 23-26
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvskg_02():
    sprite('rg040_00', 4)	# 1-4
    Unknown21007(4, 32)
    GFX_1('story_teni', 103)
    SFX_0('000_airdash_2')
    SFX_0('022_magiccircle_b')
    Unknown3004(-4)
    sprite('rg040_01', 4)	# 5-8
    sprite('rg040_02', 5)	# 9-13
    sprite('rg040_02ex', 5)	# 14-18
    sprite('rg040_02', 5)	# 19-23
    sprite('rg040_02ex', 5)	# 24-28
    sprite('rg040_02', 5)	# 29-33
    sprite('rg040_02ex', 5)	# 34-38
    sprite('rg040_02', 5)	# 39-43
    sprite('rg040_02ex', 5)	# 44-48
    sprite('rg040_02', 5)	# 49-53
    sprite('rg040_02ex', 5)	# 54-58
    sprite('rg040_02', 5)	# 59-63
    sprite('rg040_02ex', 5)	# 64-68
    GFX_1('haef_event_lose_end', 103)
    sprite('keep', 1)	# 69-69
    Unknown3038(1)
    Unknown2035(1)
    label(0)
    sprite('rg040_02', 5)	# 70-74
    sprite('rg040_02ex', 5)	# 75-79
    sprite('rg040_02', 5)	# 80-84
    sprite('rg040_02ex', 5)	# 85-89
    loopRest()
    gotoLabel(0)

@State
def Act3Event_rgvsam_00():

    def upon_IMMEDIATE():
        Unknown3001(0)

        def upon_STATE_END():
            Unknown3001(255)
    sprite('rg620_05', 60)	# 1-60
    GFX_1('story_teni', 100)
    SFX_0('000_airdash_2')
    SFX_0('022_magiccircle_b')
    Unknown3004(4)
    sprite('rg620_05', 20)	# 61-80
    GFX_1('haef_event_lose_end', 103)
    sprite('rg620_04', 6)	# 81-86
    sprite('rg620_03', 6)	# 87-92
    sprite('rg620_02', 6)	# 93-98
    sprite('rg620_01', 6)	# 99-104
    sprite('rg620_00', 6)	# 105-110
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_KimePause():
    sprite('rg600_16', 5)	# 1-5
    sprite('rg600_15', 5)	# 6-10
    sprite('rg600_14', 5)	# 11-15
    sprite('rg600_04', 5)	# 16-20
    sprite('rg600_05', 5)	# 21-25
    sprite('rg600_06', 24)	# 26-49
    sprite('rg600_07', 4)	# 50-53
    sprite('rg600_08', 4)	# 54-57
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 58-63
    sprite('rg600_10', 6)	# 64-69
    sprite('rg600_11', 6)	# 70-75
    sprite('rg600_12', 32767)	# 76-32842
    SFX_3('rgse_00')
    loopRest()

@State
def Act3Event_KimePauseEnd():
    sprite('rg600_13', 6)	# 1-6
    sprite('rg600_14', 6)	# 7-12
    sprite('rg600_15', 6)	# 13-18
    sprite('rg600_16', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Entry1():
    sprite('rg601_00', 32767)	# 1-32767
    loopRest()

@State
def Act3Event_Entry1End():
    sprite('rg601_01', 6)	# 1-6
    sprite('rg601_02', 6)	# 7-12
    sprite('rg601_03', 6)	# 13-18
    sprite('rg601_04', 6)	# 19-24
    sprite('rg601_05', 6)	# 25-30
    sprite('rg601_06', 6)	# 31-36
    sprite('rg601_07', 6)	# 37-42
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 43-48
    sprite('rg601_09', 6)	# 49-54
    sprite('rg601_10', 6)	# 55-60
    sprite('rg601_11', 4)	# 61-64
    sprite('rg601_12', 4)	# 65-68
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 69-72
    sprite('rg601_14', 4)	# 73-76
    sprite('rg601_15', 4)	# 77-80
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 81-84
    sprite('rg601_17', 6)	# 85-90
    sprite('rg601_18', 6)	# 91-96
    sprite('rg601_19', 3)	# 97-99
    sprite('rg601_20', 6)	# 100-105
    sprite('rg601_21', 6)	# 106-111
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 112-117
    sprite('rg601_23', 6)	# 118-123
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rcvsrg_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('rg211_00', 1)	# 1-1
    sprite('rg211_03', 1)	# 2-2
    sprite('rg211_04', 1)	# 3-3
    sprite('rg211_05', 1)	# 4-4
    sprite('rg211_06', 1)	# 5-5
    SFX_0('004_swing_grap_1_2')
    sprite('rg211_07', 1)	# 6-6
    sprite('rg211_08', 1)	# 7-7
    Unknown21007(22, 32)
    sprite('rg211_09', 2)	# 8-9	 **attackbox here**
    sprite('rg211_10', 3)	# 10-12	 **attackbox here**
    sprite('rg211_11', 3)	# 13-15	 **attackbox here**
    sprite('rg211_12', 3)	# 16-18
    sprite('rg211_13', 3)	# 19-21
    sprite('rg211_14', 4)	# 22-25
    sprite('rg211_15', 3)	# 26-28
    sprite('rg211_16', 2)	# 29-30
    sprite('rg211_16', 1)	# 31-31
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_arvsrg_00():

    def upon_IMMEDIATE():
        teleportRelativeX(180000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('rg000_00', 7)	# 1-7
    sprite('rg000_01', 7)	# 8-14
    sprite('rg000_02', 7)	# 15-21
    sprite('rg000_03', 7)	# 22-28
    sprite('rg000_04', 7)	# 29-35
    sprite('rg000_05', 7)	# 36-42
    sprite('rg000_06', 7)	# 43-49
    sprite('rg000_05', 7)	# 50-56
    sprite('rg000_04', 7)	# 57-63
    sprite('rg000_03', 7)	# 64-70
    sprite('rg000_02', 7)	# 71-77
    sprite('rg000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rg070_00', 4)	# 85-88
    sprite('rg070_00', 8)	# 89-96
    GFX_1('ef_hitmd', 103)
    SFX_0('100_hit_grap_2')
    ScreenShake(3000, 18000)
    sprite('rg070_01', 8)	# 97-104
    Unknown1047(-27000)
    sprite('rg070_02', 5)	# 105-109
    sprite('rg070_03', 5)	# 110-114
    sprite('rg070_04', 5)	# 115-119
    sprite('rg070_05', 5)	# 120-124
    sprite('rg070_06', 32767)	# 125-32891
    Unknown1084(1)
    loopRest()

@State
def Act3Event_arvsrg_01():
    sprite('rg070_07', 7)	# 1-7
    sprite('rg070_08', 5)	# 8-12
    sprite('rg070_09', 5)	# 13-17
    sprite('rg070_10', 5)	# 18-22
    sprite('rg063_11', 1)	# 23-23
    Unknown8003(100, 0, 1)
    teleportRelativeX(100000)
    sprite('rg063_11', 32767)	# 24-32790
    loopRest()

@State
def Act3Event_kgvsrg_00():

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
    sprite('rg030_00', 7)	# 1-7
    physicsXImpulse(5000)
    label(9)
    sprite('rg030_01', 7)	# 8-14
    sprite('rg030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_03', 7)	# 22-28
    sprite('rg030_04', 7)	# 29-35
    sprite('rg030_05', 7)	# 36-42
    sprite('rg030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rg030_07', 7)	# 50-56
    SFX_3('rgse_00')
    sprite('rg030_08', 7)	# 57-63
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 2)	# 64-65
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_kgvsrg_01():
    sprite('keep', 1)	# 1-1
    Unknown21007(22, 32)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_kgvsrg_02():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('rg211_00', 1)	# 1-1
    sprite('rg211_03', 1)	# 2-2
    sprite('rg211_04', 1)	# 3-3
    sprite('rg211_05', 1)	# 4-4
    sprite('rg211_06', 1)	# 5-5
    SFX_0('004_swing_grap_1_2')
    sprite('rg211_07', 1)	# 6-6
    sprite('rg211_08', 1)	# 7-7
    Unknown21007(22, 32)
    sprite('rg211_09', 12)	# 8-19	 **attackbox here**
    sprite('rg211_10', 3)	# 20-22	 **attackbox here**
    sprite('rg211_11', 3)	# 23-25	 **attackbox here**
    sprite('rg211_12', 3)	# 26-28
    sprite('rg211_13', 3)	# 29-31
    sprite('rg211_14', 4)	# 32-35
    sprite('rg211_15', 3)	# 36-38
    sprite('rg211_16', 2)	# 39-40
    sprite('rg211_16', 1)	# 41-41
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_kgvsrg_03():

    def upon_IMMEDIATE():
        teleportRelativeX(35000)
        Unknown2004(1, 0)
    label(0)
    sprite('rg202_00', 1)	# 1-1
    sprite('rg202_01', 1)	# 2-2
    sprite('rg202_02', 2)	# 3-4
    sprite('rg202_05', 3)	# 5-7
    SFX_0('008_swing_pole_2')
    sprite('rg202_06', 2)	# 8-9
    sprite('rg202_07', 2)	# 10-11
    sprite('rg202_08', 1)	# 12-12	 **attackbox here**
    StartMultihit()
    sprite('rg202_09', 12)	# 13-24	 **attackbox here**
    label(1)
    sprite('rg090_01', 4)	# 25-28
    ScreenShake(5000, 20000)
    sprite('rg090_01', 4)	# 29-32
    Unknown1047(-14000)
    sprite('rg090_02', 4)	# 33-36
    sprite('rg090_03', 4)	# 37-40
    sprite('rg090_04', 5)	# 41-45
    sprite('rg090_04', 1)	# 46-46
    sprite('rg090_04', 1)	# 47-47
    Unknown1084(1)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_kgvsrg_04():
    sprite('rg032_00', 2)	# 1-2
    sprite('rg032_01', 2)	# 3-4
    physicsXImpulse(26000)
    SFX_3('rgse_00')
    sprite('rg032_02', 4)	# 5-8
    sprite('rg032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('rg032_03add', 4)	# 13-16
    sprite('rg032_04', 4)	# 17-20
    sprite('rg032_08', 2)	# 21-22
    Unknown1084(1)
    Unknown1047(3500)
    sprite('rg310_00', 5)	# 23-27
    sprite('rg310_01', 5)	# 28-32
    sprite('rg310_02', 12)	# 33-44	 **attackbox here**
    sprite('rg310_01', 5)	# 45-49
    sprite('rg310_00', 5)	# 50-54
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rmvsrg_00():
    sprite('rg431_00', 3)	# 1-3
    sprite('rg431_01', 3)	# 4-6
    sprite('rg431_02', 3)	# 7-9
    sprite('rg431_03', 3)	# 10-12
    sprite('rg431_04', 3)	# 13-15
    sprite('rg431_05', 3)	# 16-18
    sprite('rg431_06', 32767)	# 19-32785
    loopRest()

@State
def Act3Event_rmvsrg_01():
    sprite('rg431_07', 3)	# 1-3
    SFX_0('302_spsys_burst')
    Unknown4004('4775617264437275736857696e64000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    Unknown1096(1400)
    Unknown35()
    label(0)
    sprite('rg431_08', 3)	# 4-6
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    sprite('rg431_09', 3)	# 7-9
    sprite('rg431_08', 3)	# 10-12
    sprite('rg431_09', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def Act3Event_rmvsrg_02():

    def upon_IMMEDIATE():
        EnableCollision(0)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 <= 3):
                Unknown2038(1)
            else:
                SLOT_2 = 0
                SFX_0('014_electric_s')
                GFX_1('haef_event_lose', 103)
    sprite('rg431_09', 3)	# 1-3
    sprite('rg431_10', 5)	# 4-8
    sprite('rg431_02', 5)	# 9-13
    sprite('rg431_01', 5)	# 14-18
    sprite('rg431_00', 5)	# 19-23
    label(0)
    sprite('rg000_00', 7)	# 24-30
    sprite('rg000_01', 7)	# 31-37
    sprite('rg000_02', 7)	# 38-44
    sprite('rg000_03', 7)	# 45-51
    sprite('rg000_04', 7)	# 52-58
    sprite('rg000_05', 7)	# 59-65
    sprite('rg000_06', 7)	# 66-72
    sprite('rg000_05', 7)	# 73-79
    sprite('rg000_04', 7)	# 80-86
    sprite('rg000_03', 7)	# 87-93
    sprite('rg000_02', 7)	# 94-100
    sprite('rg000_01', 7)	# 101-107
    loopRest()
    gotoLabel(0)

@State
def Act3Event_rmvsrg_03():
    sprite('keep', 3)	# 1-3
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-7)
    sprite('keep', 3)	# 4-6
    sprite('keep', 30)	# 7-36
    SFX_0('014_electric_sl')
    GFX_1('haef_event_lose_end', 103)

    def upon_CLEAR_OR_EXIT():
        SLOT_7 = 1
    sprite('keep', 1)	# 37-37
    sprite('keep', 32767)	# 38-32804
    loopRest()

@State
def Act3Event_esvsrg_00():

    def upon_IMMEDIATE():
        Unknown3001(0)

        def upon_STATE_END():
            Unknown3001(255)
    sprite('rg620_05', 60)	# 1-60
    GFX_1('story_teni', 100)
    SFX_0('000_airdash_2')
    SFX_0('022_magiccircle_b')
    Unknown3004(4)
    sprite('rg620_05', 20)	# 61-80
    GFX_1('haef_event_lose_end', 103)
    sprite('rg620_04', 6)	# 81-86
    sprite('rg620_03', 6)	# 87-92
    sprite('rg620_02', 6)	# 93-98
    sprite('rg620_01', 6)	# 99-104
    sprite('rg620_00', 6)	# 105-110
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_esvsrg_01():
    sprite('rg600_16', 5)	# 1-5
    sprite('rg600_15', 5)	# 6-10
    sprite('rg600_14', 5)	# 11-15
    sprite('rg600_04', 5)	# 16-20
    sprite('rg600_05', 5)	# 21-25
    sprite('rg600_06', 24)	# 26-49
    sprite('rg600_07', 4)	# 50-53
    sprite('rg600_08', 4)	# 54-57
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 58-63
    sprite('rg600_10', 6)	# 64-69
    sprite('rg600_11', 6)	# 70-75
    sprite('rg600_12', 15)	# 76-90
    SFX_3('rgse_00')
    sprite('rg600_13', 6)	# 91-96
    sprite('rg600_14', 6)	# 97-102
    sprite('rg600_15', 6)	# 103-108
    sprite('rg600_16', 6)	# 109-114
    loopRest()
    enterState('CmnActStand')