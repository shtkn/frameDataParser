@Subroutine
def PreInit():
    Unknown12019('70797500000000000000000000000000')

@Subroutine
def MatchInit():
    Health(14000)
    DashFInitialVelocity(16000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(38000)
    Unknown12011(1650)
    AirBDashDuration(13)
    Unknown12037(-1650)
    Unknown12024(1)
    Unknown13039(1)
    Unknown2049(1)
    Unknown23003(0, 1, 7, 1, 9, 0, -1, -1)
    Unknown23005(0, 1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    Move_AirGround_(0x3083)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x300e)
    Unknown14015(0, 1000000, -200000, 150000, 3000, 50)
    Unknown15015(18, 55)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Unknown15015(21, 30)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Unknown15015(17, 25)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown14015(0, 450000, -200000, 200000, 3000, 50)
    Unknown14027('NmlAtk2A')
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A3nd', 0x6)
    Unknown14015(0, 350000, -200000, 150000, 1000, 50)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th', 0x6)
    Unknown14005(1)
    Unknown14013('NmlAtk5A4th')
    Unknown14015(0, 350000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 250000, -200000, 150000, 1000, 50)
    Unknown15009()
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', 0x1a)
    Move_Input_(0x79)
    Unknown14027('NmlAtk5B')
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4B', 0x18)
    Move_Input_(0x5f)
    Unknown14027('NmlAtk5B')
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd_Front', 0x1a)
    Unknown14005(1)
    Unknown14027('NmlAtk5B2nd')
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd_Back', 0x18)
    Unknown14005(1)
    Unknown14027('NmlAtk5B2nd')
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 500000, -200000, 500000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk3B', 0x17)
    Unknown14027('NmlAtk2B')
    Unknown14015(0, 500000, -200000, 500000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk1B', 0x15)
    Unknown14027('NmlAtk2B')
    Unknown14015(0, 500000, -200000, 500000, 1000, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown14015(0, 300000, -200000, 150000, 0, 0)
    Unknown15008()
    Unknown15012(1000)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown14015(0, 450000, -200000, 150000, 1000, 50)
    Unknown15009()
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(-100000, 300000, -300000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown14015(-100000, 300000, -300000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 1000000, -500000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR6B', 0x23)
    Unknown14027('NmlAtkAIR5B')
    Unknown14015(0, 1000000, -500000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR4B', 0x21)
    Unknown14027('NmlAtkAIR5B')
    Unknown14015(0, 1000000, -500000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 400000, -500000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('AgiA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x300e)
    Unknown14015(0, 550000, -200000, 150000, 1000, 50)
    Unknown15016(0, 1, 43)
    Move_EndRegister()
    Move_Register('AgiB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x300e)
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Unknown15016(1, 1, 20)
    Move_EndRegister()
    Move_Register('AgiEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x300e)
    Unknown14015(0, 750000, -200000, 150000, 500, 50)
    Unknown15025('000000000000000005000000f401000020030000')
    Unknown15016(2, 1, 20)
    Move_EndRegister()
    Move_Register('AgiAirA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x300e)
    Unknown14015(0, 550000, -200000, 150000, 1000, 50)
    Unknown15016(0, 1, 20)
    Move_EndRegister()
    Move_Register('AgiAirB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x300e)
    Unknown14015(0, 1000000, -200000, 150000, 1000, 50)
    Unknown15016(1, 1, 20)
    Move_EndRegister()
    Move_Register('AgiAirEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x300e)
    Unknown14015(0, 750000, -200000, 150000, 500, 50)
    Unknown15025('000000000000000005000000f401000020030000')
    Unknown15016(2, 1, 20)
    Move_EndRegister()
    Move_Register('MaharagiA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3009)
    Unknown14015(0, 600000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('MaharagiB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3009)
    Unknown14015(0, 800000, -200000, 400000, 1000, 50)
    Unknown15016(1, 38, 54)
    Move_EndRegister()
    Move_Register('MaharagiEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3009)
    Unknown14015(0, 800000, -200000, 400000, 500, 50)
    Unknown15016(2, 38, 80)
    Unknown15012(2000)
    Unknown15025('000000000000000005000000f401000020030000')
    Move_EndRegister()
    Move_Register('FireBoosterA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(700000, 1500000, -200000, 1500000, 0, 0)
    Move_EndRegister()
    Move_Register('FireBoosterB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(700000, 1500000, -200000, 1500000, 0, 0)
    Move_EndRegister()
    Move_Register('FireBoosterC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(700000, 1500000, -200000, 1500000, 0, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Move_AirGround_(0x3083)
    Unknown14015(0, 200000, -200000, 150000, 300, 0)
    Unknown15014(1000)
    Unknown15020(800, 1000, 500, 1000)
    Move_EndRegister()
    Move_Register('UltimateAgidine', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(0, 500000, -200000, 150000, 200, 0)
    Unknown15014(1000)
    Unknown15020(800, 1000, 500, 1000)
    Move_EndRegister()
    Move_Register('UltimateAgidine_OD', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(0, 500000, -200000, 150000, 200, 0)
    Unknown15014(1000)
    Unknown15020(800, 1000, 500, 1000)
    Move_EndRegister()
    Move_Register('UltimateMaharagidine', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 700000, -200000, 300000, 200, 0)
    Unknown15020(800, 1000, 500, 1000)
    Move_EndRegister()
    Move_Register('UltimateMaharagidineOD', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(0, 700000, -200000, 300000, 200, 0)
    Unknown15020(800, 1000, 500, 1000)
    Move_EndRegister()
    Move_Register('DebugSkill', 0x1)
    Move_Input_(0x26)
    Move_AirGround_(0x306f)
    Move_EndRegister()
    Move_Register('DS_YarareCHECK1', 0x1)
    Move_Input_(0x6b)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_Yarare1')
    Move_EndRegister()
    Move_Register('DS_YarareCHECK2', 0x1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_Yarare2')
    Move_EndRegister()
    Move_Register('DS_YarareCHECK3', 0x1)
    Move_Input_(0x44)
    Move_Input_(INPUT_RELEASE_A)
    Unknown14018(1, 1, 1)
    Move_AirGround_(0x306f)
    Unknown14019('Func_DS_Yarare3')
    Move_EndRegister()
    Move_Register('Ichigeki', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk2C', 3000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk2C', 3000000)
    Unknown15024('NmlAtk4A3nd', 'NmlAtk4A4th', 10000000)
    Unknown15024('NmlAtk4A3nd', 'NmlAtk2C', 3000000)
    Unknown15024('NmlAtk2A', 'NmlAtk4A', 10000000)
    Unknown15024('NmlAtk2C', 'AgiA', 10000000)
    Unknown15024('NmlAtk2C', 'AgiEX', 10000000)
    Unknown12018(0, 'yu060_00')
    Unknown12018(1, 'yu060_01')
    Unknown12018(2, 'yu060_02')
    Unknown12018(3, 'yu060_03')
    Unknown12018(4, 'yu060_04')
    Unknown12018(5, 'yu060_05')
    Unknown12018(6, 'yu060_06')
    Unknown12018(7, 'yu041_02')
    Unknown12018(8, 'yu040_02')
    Unknown12018(9, 'yu045_02')
    Unknown12018(10, 'yu060_00')
    Unknown12018(11, 'yu060_01')
    Unknown12018(12, 'yu060_03')
    Unknown12018(13, 'yu060_05')
    Unknown12018(14, 'yu060_07')
    Unknown12018(15, 'yu125_00')
    Unknown12018(16, 'yu050_00')
    Unknown12018(17, 'yu052_00')
    Unknown12018(18, 'yu054_00')
    Unknown12018(25, 'yu063_00')
    Unknown12018(26, 'yu063_01')
    Unknown12018(27, 'yu063_02')
    Unknown12018(28, 'yu063_05')
    Unknown12018(29, 'yu060_12')
    Unknown12018(24, 'yu072_03')
    Unknown7010(0, 'pyu000')
    Unknown7010(1, 'pyu001')
    Unknown7010(2, 'pyu002')
    Unknown7010(3, 'pyu003')
    Unknown7010(4, 'pyu004')
    Unknown7010(5, 'pyu005')
    Unknown7010(6, 'pyu006')
    Unknown7010(7, 'pyu007')
    Unknown7010(8, 'pyu008')
    Unknown7010(9, 'pyu009')
    Unknown7010(10, 'pyu010')
    Unknown7010(15, 'pyu015')
    Unknown7010(16, 'pyu016')
    Unknown7010(17, 'pyu017')
    Unknown7010(18, 'pyu018')
    Unknown7010(19, 'pyu019')
    Unknown7010(20, 'pyu020')
    Unknown7010(21, 'pyu021')
    Unknown7010(22, 'pyu022')
    Unknown7010(23, 'pyu023')
    Unknown7010(24, 'pyu024')
    Unknown7010(25, 'pyu025')
    Unknown7010(28, 'pyu028')
    Unknown7010(29, 'pyu029')
    Unknown7010(30, 'pyu030')
    Unknown7010(31, 'pyu031')
    Unknown7010(32, 'pyu025')
    Unknown7010(33, 'pyu033')
    Unknown7010(34, 'pyu034')
    Unknown7010(35, 'pyu035')
    Unknown7010(36, 'pyu036')
    Unknown7010(37, 'pyu037')
    Unknown7010(39, 'pyu039')
    Unknown7010(42, 'pyu042')
    Unknown7010(43, 'pyu043')
    Unknown7010(44, 'pyu044')
    Unknown7010(45, 'pyu045')
    Unknown7010(46, 'pyu046')
    Unknown7010(47, 'pyu301_0')
    Unknown7010(48, 'pyu048')
    Unknown7010(49, 'pyu049')
    Unknown7010(50, 'pyu050')
    Unknown7010(52, 'pyu052')
    Unknown7010(53, 'pyu053')
    Unknown7010(54, 'pyu100_0')
    Unknown7010(55, 'pyu100_1')
    Unknown7010(56, 'pyu100_2')
    Unknown7010(63, 'pyu101_0')
    Unknown7010(64, 'pyu101_1')
    Unknown7010(65, 'pyu101_2')
    Unknown7010(57, 'pyu102_0')
    Unknown7010(58, 'pyu102_1')
    Unknown7010(59, 'pyu102_2')
    Unknown7010(66, 'pyu103_0')
    Unknown7010(67, 'pyu103_1')
    Unknown7010(68, 'pyu103_2')
    Unknown7010(60, 'pyu104_0')
    Unknown7010(61, 'pyu104_1')
    Unknown7010(62, 'pyu104_2')
    Unknown7010(69, 'pyu105_0')
    Unknown7010(70, 'pyu105_1')
    Unknown7010(71, 'pyu105_2')
    Unknown7010(72, 'pyu150')
    Unknown7010(73, 'pyu151')
    Unknown7010(74, 'pyu152')
    Unknown7010(85, 'pyu153')
    Unknown7010(87, 'pyu154')
    Unknown7010(88, 'pyu155')
    Unknown7010(96, 'pyu161_0')
    Unknown7010(97, 'pyu161_1')
    Unknown7010(92, 'pyu162_0')
    Unknown7010(93, 'pyu162_1')
    Unknown7010(98, 'pyu163_0')
    Unknown7010(99, 'pyu163_1')
    Unknown7010(100, 'pyu164_0')
    Unknown7010(101, 'pyu164_1')
    Unknown7010(105, 'pyu165_0')
    Unknown7010(106, 'pyu165_1')
    Unknown7010(102, 'pyu166_0')
    Unknown7010(103, 'pyu166_1')
    Unknown7010(90, 'pyu167_0')
    Unknown7010(91, 'pyu167_1')
    Unknown7010(107, 'pyu168_0')
    Unknown7010(108, 'pyu168_1')
    Unknown7010(110, 'pyu169_0')
    Unknown7010(111, 'pyu169_1')
    Unknown7010(94, 'pyu400_0')
    Unknown7010(95, 'pyu400_1')
    Unknown30036('5059555f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541676964696e650000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541676964696e655f4f440000000000000000000000000000')
    Unknown12059('04000000556c74696d6174654d6168617261676964696e65000000000000000000000000')
    Unknown12059('05000000556c74696d6174654d6168617261676964696e654f4400000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def Func_DS_Yarare1():
    Unknown1000(-600000)
    teleportRelativeY(0)
    Unknown36(22)
    Unknown1000(-600000)
    teleportRelativeY(0)
    Unknown35()
    GFX_0('Func_DS_Yarare1', -1)

@Subroutine
def Func_DS_Yarare2():
    Unknown1000(-600000)
    teleportRelativeY(0)
    Unknown36(22)
    Unknown1000(-600000)
    teleportRelativeY(0)
    Unknown35()
    GFX_0('Func_DS_Yarare2', -1)

@Subroutine
def Func_DS_Yarare3():
    Unknown1000(-600000)
    teleportRelativeY(0)
    Unknown36(22)
    Unknown1000(-600000)
    teleportRelativeY(0)
    Unknown35()
    GFX_0('Func_DS_Yarare3', -1)

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_90:
            Unknown58('TRI_PYUFireLv', 2, 67)
            if SLOT_67:
                SLOT_31 = SLOT_67
    if SLOT_170:
        Unknown23008(0, 0)
    if (SLOT_31 == 9):
        if (not SLOT_81):
            if (not SLOT_31):
                SLOT_60 = 0
            SLOT_61 = (SLOT_61 + 1)
            if (SLOT_61 >= 2):
                SLOT_61 = 0
            if SLOT_61:
                if (not SLOT_64):
                    GFX_1('yuef_403jizokuaura', 105)
            SLOT_64 = 1
            if (not SLOT_30):
                if SLOT_21:
                    SLOT_64 = 0
            if Unknown23148('CmnActTagBattleWait'):
                SLOT_64 = 1
            if Unknown23148('CmnActChangePartnerOut'):
                SLOT_64 = 1
            if Unknown23148('CmnActChangePartnerQuickOut'):
                SLOT_64 = 1
            if Unknown23148('CmnActFDownLoop'):
                SLOT_64 = 1
            if Unknown23148('Ichigeki'):
                SLOT_64 = 1

@State
def CmnActStand():
    label(0)
    sprite('yu000_00', 6)	# 1-6
    sprite('yu000_01', 6)	# 7-12
    sprite('yu000_02', 6)	# 13-18
    sprite('yu000_03', 6)	# 19-24
    sprite('yu000_04', 6)	# 25-30
    sprite('yu000_05', 6)	# 31-36
    sprite('yu000_06', 6)	# 37-42
    sprite('yu000_07', 6)	# 43-48
    sprite('yu000_08', 6)	# 49-54
    sprite('yu000_09', 6)	# 55-60
    sprite('yu000_10', 6)	# 61-66
    sprite('yu000_11', 6)	# 67-72
    sprite('yu000_12', 6)	# 73-78
    sprite('yu000_13', 6)	# 79-84
    sprite('yu000_14', 6)	# 85-90
    sprite('yu000_15', 6)	# 91-96
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 123)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('yu001_00', 8)	# 97-104
    SLOT_88 = 960
    sprite('yu001_01', 8)	# 105-112
    SFX_1('pyu000')
    sprite('yu001_02', 8)	# 113-120
    sprite('yu001_03', 8)	# 121-128
    sprite('yu001_04', 8)	# 129-136
    GFX_0('reaction_sakura', 0)
    sprite('yu001_05', 8)	# 137-144
    GFX_0('reaction_sakura', 0)
    sprite('yu001_06', 8)	# 145-152
    GFX_0('reaction_sakura', 0)
    sprite('yu001_07', 8)	# 153-160
    sprite('yu001_08', 8)	# 161-168
    sprite('yu001_00', 8)	# 169-176
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('yu003_00', 4)	# 1-4
    sprite('yu003_01', 4)	# 5-8
    sprite('yu003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('yu010_00', 4)	# 1-4
    sprite('yu010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('yu010_02', 6)	# 1-6
    sprite('yu010_03', 6)	# 7-12
    sprite('yu010_04', 6)	# 13-18
    sprite('yu010_05', 6)	# 19-24
    sprite('yu010_06', 6)	# 25-30
    sprite('yu010_07', 6)	# 31-36
    sprite('yu010_08', 6)	# 37-42
    sprite('yu010_09', 6)	# 43-48
    sprite('yu010_10', 6)	# 49-54
    sprite('yu010_11', 6)	# 55-60
    sprite('yu010_12', 6)	# 61-66
    sprite('yu010_13', 6)	# 67-72
    sprite('yu010_14', 6)	# 73-78
    sprite('yu010_15', 6)	# 79-84
    sprite('yu010_16', 6)	# 85-90
    sprite('yu010_17', 6)	# 91-96
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('yu013_00', 4)	# 1-4
    sprite('yu013_01', 4)	# 5-8
    sprite('yu013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('yu010_01', 4)	# 1-4
    sprite('yu010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    if SLOT_37:
        if SLOT_93:
            if SLOT_16:
                Unknown1045(15000)
    sprite('yu010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('yu020_00', 4)	# 1-4
    sprite('yu020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('yu020_02', 4)	# 1-4
    sprite('yu020_03', 5)	# 5-9

@State
def CmnActJumpDown():
    sprite('yu020_05', 3)	# 1-3
    sprite('yu020_06', 3)	# 4-6
    label(0)
    sprite('yu020_07', 4)	# 7-10
    sprite('yu020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('yu010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('yu232_02', 2)	# 1-2
    sprite('yu232_03', 2)	# 3-4
    sprite('yu232_04', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('yu010_01', 4)	# 1-4
    sprite('yu010_00', 4)	# 5-8

@State
def CmnActFWalk():
    sprite('yu030_00', 5)	# 1-5
    sprite('yu030_01', 5)	# 6-10
    label(0)
    sprite('yu030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yu030_03', 5)	# 16-20
    sprite('yu030_04', 5)	# 21-25
    sprite('yu030_05', 5)	# 26-30
    sprite('yu030_06', 5)	# 31-35
    sprite('yu030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yu030_08', 5)	# 41-45
    sprite('yu030_09', 5)	# 46-50
    sprite('yu030_10', 5)	# 51-55
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('yu031_00', 6)	# 1-6
    sprite('yu031_01', 6)	# 7-12
    label(0)
    sprite('yu031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yu031_03', 6)	# 19-24
    sprite('yu031_04', 6)	# 25-30
    sprite('yu031_05', 6)	# 31-36
    sprite('yu031_06', 6)	# 37-42
    sprite('yu031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('yu031_08', 6)	# 49-54
    sprite('yu031_09', 6)	# 55-60
    sprite('yu031_10', 6)	# 61-66
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('yu030_00', 3)	# 1-3
    sprite('yu032_00', 2)	# 4-5
    label(0)
    sprite('yu032_01', 4)	# 6-9
    sprite('yu032_02', 4)	# 10-13
    sprite('yu032_03', 4)	# 14-17
    Unknown8006(100, 1, 1)
    sprite('yu032_04', 4)	# 18-21
    sprite('yu032_05', 4)	# 22-25
    sprite('yu032_06', 4)	# 26-29
    sprite('yu032_07', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('yu032_08', 4)	# 34-37
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('yu032_09', 4)	# 1-4
    sprite('yu032_10', 4)	# 5-8

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
    sprite('yu033_00', 2)	# 1-2
    sprite('yu033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('yu033_02', 1)	# 6-6
    sprite('yu033_02', 2)	# 7-8
    sprite('yu033_03', 3)	# 9-11
    label(0)
    sprite('yu033_04', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yu033_05', 3)	# 15-17
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('yu033_06', 1)	# 18-18
    sprite('yu033_06', 2)	# 19-20
    sprite('yu033_07', 3)	# 21-23
    sprite('yu033_08', 3)	# 24-26

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('yu035_00', 2)	# 1-2
    sprite('yu035_01', 3)	# 3-5
    sprite('yu035_02', 3)	# 6-8
    sprite('yu035_01', 3)	# 9-11
    sprite('yu035_02', 3)	# 12-14
    sprite('yu035_01', 3)	# 15-17
    sprite('yu035_00', 3)	# 18-20

@State
def CmnActAirBDash():
    sprite('yu036_00', 1)	# 1-1
    physicsYImpulse(12000)
    sprite('yu036_00', 4)	# 2-5
    sprite('yu036_01', 4)	# 6-9
    sprite('yu036_02', 4)	# 10-13
    sprite('yu036_00', 4)	# 14-17
    sprite('yu020_06', 4)	# 18-21
    label(0)
    sprite('yu020_07', 4)	# 22-25
    sprite('yu020_08', 4)	# 26-29
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('yu050_00', 1)	# 1-1
    sprite('yu050_01', 7)	# 2-8
    sprite('yu050_00', 2)	# 9-10

@State
def CmnActHitStandLv2():
    sprite('yu050_01', 1)	# 1-1
    sprite('yu050_02', 7)	# 2-8
    sprite('yu050_01', 2)	# 9-10
    sprite('yu050_00', 2)	# 11-12

@State
def CmnActHitStandLv3():
    sprite('yu050_02', 1)	# 1-1
    sprite('yu050_03', 7)	# 2-8
    sprite('yu050_02', 2)	# 9-10
    sprite('yu050_01', 2)	# 11-12
    sprite('yu050_00', 2)	# 13-14

@State
def CmnActHitStandLv4():
    sprite('yu050_03', 1)	# 1-1
    sprite('yu050_04', 8)	# 2-9
    sprite('yu050_03', 2)	# 10-11
    sprite('yu050_02', 2)	# 12-13
    sprite('yu050_01', 2)	# 14-15
    sprite('yu050_00', 2)	# 16-17

@State
def CmnActHitStandLv5():
    sprite('yu050_04', 1)	# 1-1
    sprite('yu050_04', 8)	# 2-9
    sprite('yu050_04', 2)	# 10-11
    sprite('yu050_03', 2)	# 12-13
    sprite('yu050_02', 2)	# 14-15
    sprite('yu050_01', 2)	# 16-17
    sprite('yu050_00', 2)	# 18-19

@State
def CmnActHitStandLowLv1():
    sprite('yu052_00', 1)	# 1-1
    sprite('yu052_01', 7)	# 2-8
    sprite('yu052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv2():
    sprite('yu052_01', 1)	# 1-1
    sprite('yu052_02', 7)	# 2-8
    sprite('yu052_01', 2)	# 9-10
    sprite('yu052_00', 2)	# 11-12

@State
def CmnActHitStandLowLv3():
    sprite('yu052_02', 1)	# 1-1
    sprite('yu052_03', 7)	# 2-8
    sprite('yu052_02', 2)	# 9-10
    sprite('yu052_01', 2)	# 11-12
    sprite('yu052_00', 2)	# 13-14

@State
def CmnActHitStandLowLv4():
    sprite('yu052_03', 1)	# 1-1
    sprite('yu052_04', 8)	# 2-9
    sprite('yu052_03', 2)	# 10-11
    sprite('yu052_02', 2)	# 12-13
    sprite('yu052_01', 2)	# 14-15
    sprite('yu052_00', 2)	# 16-17

@State
def CmnActHitStandLowLv5():
    sprite('yu052_04', 1)	# 1-1
    sprite('yu052_04', 8)	# 2-9
    sprite('yu052_04', 2)	# 10-11
    sprite('yu052_03', 2)	# 12-13
    sprite('yu052_02', 2)	# 14-15
    sprite('yu052_01', 2)	# 16-17
    sprite('yu052_00', 2)	# 18-19

@State
def CmnActHitCrouchLv1():
    sprite('yu054_00', 1)	# 1-1
    sprite('yu054_01', 9)	# 2-10
    sprite('yu054_00', 2)	# 11-12

@State
def CmnActHitCrouchLv2():
    sprite('yu054_01', 1)	# 1-1
    sprite('yu054_02', 11)	# 2-12
    sprite('yu054_01', 2)	# 13-14
    sprite('yu054_00', 2)	# 15-16

@State
def CmnActHitCrouchLv3():
    sprite('yu054_02', 1)	# 1-1
    sprite('yu054_03', 12)	# 2-13
    sprite('yu054_02', 2)	# 14-15
    sprite('yu054_01', 2)	# 16-17
    sprite('yu054_00', 2)	# 18-19

@State
def CmnActHitCrouchLv4():
    sprite('yu054_03', 1)	# 1-1
    sprite('yu054_04', 12)	# 2-13
    sprite('yu054_03', 2)	# 14-15
    sprite('yu054_02', 2)	# 16-17
    sprite('yu054_01', 2)	# 18-19
    sprite('yu054_00', 2)	# 20-21

@State
def CmnActHitCrouchLv5():
    sprite('yu054_04', 1)	# 1-1
    sprite('yu054_04', 25)	# 2-26
    sprite('yu054_04', 2)	# 27-28
    sprite('yu054_03', 2)	# 29-30
    sprite('yu054_02', 2)	# 31-32
    sprite('yu054_01', 2)	# 33-34
    sprite('yu054_00', 2)	# 35-36

@State
def CmnActBDownUpper():
    sprite('yu060_00', 4)	# 1-4
    label(0)
    sprite('yu060_01', 4)	# 5-8
    sprite('yu060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('yu060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('yu060_04', 8)	# 1-8
    label(1)
    sprite('yu060_05', 4)	# 9-12
    sprite('yu060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('yu060_07', 4)	# 1-4

@State
def CmnActBDownBound():
    sprite('yu060_08', 2)	# 1-2
    sprite('yu060_09', 2)	# 3-4
    sprite('yu060_10', 2)	# 5-6
    sprite('yu060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('yu060_12', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('yu064_00', 4)	# 1-4
    sprite('yu064_01', 4)	# 5-8
    sprite('yu064_02', 4)	# 9-12
    sprite('yu064_03', 4)	# 13-16

@State
def CmnActFDownUpper():
    sprite('yu063_00', 4)	# 1-4

@State
def CmnActFDownUpperEnd():
    sprite('yu063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(1)
    sprite('yu063_03', 4)	# 1-4
    sprite('yu063_04', 4)	# 5-8
    loopRest()
    gotoLabel(1)

@State
def CmnActFDownCrash():
    sprite('yu063_05', 4)	# 1-4

@State
def CmnActFDownBound():
    sprite('yu060_08', 2)	# 1-2
    sprite('yu060_09', 2)	# 3-4
    sprite('yu060_10', 2)	# 5-6
    sprite('yu060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('yu060_12', 1)	# 1-1

@State
def CmnActFDown2Stand():
    sprite('yu064_00', 4)	# 1-4
    sprite('yu064_01', 4)	# 5-8
    sprite('yu064_02', 4)	# 9-12
    sprite('yu064_03', 4)	# 13-16

@State
def CmnActVDownUpper():
    sprite('yu060_00', 4)	# 1-4
    label(0)
    sprite('yu060_01', 4)	# 5-8
    sprite('yu060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('yu060_03', 8)	# 1-8

@State
def CmnActVDownDown():
    sprite('yu060_04', 8)	# 1-8
    label(0)
    sprite('yu060_05', 4)	# 9-12
    sprite('yu060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('yu060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('yu072_00', 3)	# 1-3
    label(0)
    sprite('yu072_01', 3)	# 4-6
    sprite('yu072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('yu074_00', 2)	# 1-2
    sprite('yu074_01', 2)	# 3-4
    sprite('yu074_02', 2)	# 5-6
    sprite('yu074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('yu082_00', 2)	# 1-2
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('yu052_01', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('yu072_03', 32767)	# 1-32767

@State
def CmnActWallBoundDown():
    sprite('yu063_00', 4)	# 1-4
    sprite('yu063_01', 32767)	# 5-32771

@State
def CmnActStaggerLoop():
    sprite('yu070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('yu070_01', 4)	# 1-4
    sprite('yu070_02', 4)	# 5-8
    sprite('yu070_03', 4)	# 9-12
    sprite('yu070_04', 4)	# 13-16
    sprite('yu070_05', 4)	# 17-20
    sprite('yu070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('yu040_03', 2)	# 1-2
    sprite('yu040_02', 2)	# 3-4
    sprite('yu040_01', 2)	# 5-6
    sprite('yu040_00', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('yu020_02', 3)	# 1-3
    sprite('yu020_03', 3)	# 4-6
    sprite('yu020_04', 9)	# 7-15

@State
def CmnActUkemiAirB():
    sprite('yu020_02', 3)	# 1-3
    sprite('yu020_03', 3)	# 4-6
    sprite('yu020_04', 9)	# 7-15

@State
def CmnActUkemiAirN():
    sprite('yu020_02', 3)	# 1-3
    sprite('yu020_03', 3)	# 4-6
    sprite('yu020_04', 9)	# 7-15

@State
def CmnActUkemiLandF():
    sprite('yu112_00', 3)	# 1-3
    sprite('yu112_01', 3)	# 4-6
    sprite('yu112_02', 3)	# 7-9
    sprite('yu112_03', 3)	# 10-12
    sprite('yu112_04', 3)	# 13-15
    sprite('yu112_05', 3)	# 16-18
    sprite('yu020_07', 4)	# 19-22
    sprite('yu020_08', 4)	# 23-26

@State
def CmnActUkemiLandB():
    sprite('yu112_00', 3)	# 1-3
    sprite('yu112_01', 3)	# 4-6
    sprite('yu112_02', 3)	# 7-9
    sprite('yu112_03', 3)	# 10-12
    sprite('yu112_04', 3)	# 13-15
    sprite('yu112_05', 3)	# 16-18
    sprite('yu020_07', 4)	# 19-22
    sprite('yu020_08', 4)	# 23-26

@State
def CmnActUkemiLandN():
    sprite('yu112_00', 3)	# 1-3
    sprite('yu112_01', 3)	# 4-6
    sprite('yu112_02', 3)	# 7-9
    sprite('yu112_03', 3)	# 10-12
    sprite('yu112_04', 3)	# 13-15
    sprite('yu112_05', 3)	# 16-18
    sprite('yu020_07', 4)	# 19-22
    sprite('yu020_08', 4)	# 23-26

@State
def CmnActUkemiLandNLanding():
    sprite('yu010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('yu040_00', 3)	# 1-3
    sprite('yu040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('yu040_02', 5)	# 1-5
    sprite('yu040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('yu040_01', 3)	# 1-3
    sprite('yu040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('yu040_04', 1)	# 1-1
    label(0)
    sprite('yu040_02', 5)	# 2-6
    sprite('yu040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('yu040_01', 3)	# 1-3
    sprite('yu040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('yu040_00', 3)	# 1-3
    sprite('yu040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('yu040_04', 1)	# 1-1
    label(0)
    sprite('yu040_02', 5)	# 2-6
    sprite('yu040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('yu040_01', 3)	# 1-3
    sprite('yu040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('yu040_04', 1)	# 1-1
    label(0)
    sprite('yu040_02', 5)	# 2-6
    sprite('yu040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('yu040_01', 3)	# 1-3
    sprite('yu040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('yu043_00', 3)	# 1-3
    sprite('yu043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('yu043_02', 5)	# 1-5
    sprite('yu043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('yu043_01', 3)	# 1-3
    sprite('yu043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('yu043_04', 1)	# 1-1
    label(0)
    sprite('yu043_02', 5)	# 2-6
    sprite('yu043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('yu043_01', 3)	# 1-3
    sprite('yu043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('yu045_00', 3)	# 1-3
    sprite('yu045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('yu045_02', 5)	# 1-5
    sprite('yu045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('yu045_01', 3)	# 1-3
    sprite('yu045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('yu045_04', 1)	# 1-1
    label(0)
    sprite('yu045_02', 5)	# 2-6
    sprite('yu045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('yu045_01', 3)	# 1-3
    sprite('yu045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('yu040_04', 2)	# 1-2
    sprite('yu040_04', 2)	# 3-4
    sprite('yu040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('yu040_02', 4)	# 6-9
    sprite('yu040_01', 4)	# 10-13
    sprite('yu040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('yu043_04', 2)	# 1-2
    sprite('yu043_04', 2)	# 3-4
    sprite('yu043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('yu043_02', 4)	# 6-9
    sprite('yu043_01', 4)	# 10-13
    sprite('yu043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('yu045_04', 2)	# 1-2
    sprite('yu045_04', 2)	# 3-4
    sprite('yu045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('yu045_02', 4)	# 6-9
    sprite('yu045_01', 4)	# 10-13
    sprite('yu045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('yu025_02', 1)	# 1-1
    sprite('yu025_01', 2)	# 2-3
    sprite('yu025_00', 1)	# 4-4

@State
def CmnActLockWait():
    sprite('yu040_02', 1)	# 1-1
    sprite('yu040_01', 3)	# 2-4
    sprite('yu040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('yu200_00', 5)	# 1-5
    sprite('yu200_01', 3)	# 6-8
    sprite('yu200_02', 3)	# 9-11	 **attackbox here**
    sprite('yu200_03', 5)	# 12-16
    sprite('yu200_04', 4)	# 17-20
    sprite('yu200_05', 3)	# 21-23
    sprite('yu200_06', 3)	# 24-26
    sprite('yu200_07', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('yu045_02', 1)	# 1-1
    sprite('yu045_01', 3)	# 2-4
    sprite('yu045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('yu250_00', 3)	# 1-3
    sprite('yu250_01', 3)	# 4-6
    sprite('yu250_02', 3)	# 7-9
    sprite('yu250_03', 5)	# 10-14	 **attackbox here**
    sprite('yu250_04', 6)	# 15-20
    sprite('yu250_05', 6)	# 21-26
    sprite('yu250_06', 3)	# 27-29

@State
def CmnActLandSpin():
    sprite('yu071_00', 2)	# 1-2
    label(0)
    sprite('yu071_01', 2)	# 3-4
    sprite('yu071_02', 2)	# 5-6
    sprite('yu071_03', 2)	# 7-8
    sprite('yu071_04', 2)	# 9-10
    sprite('yu071_05', 2)	# 11-12
    sprite('yu071_06', 2)	# 13-14
    sprite('yu071_07', 2)	# 15-16
    sprite('yu071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('yu040_02', 6)	# 1-6
    sprite('yu040_01', 5)	# 7-11
    sprite('yu040_00', 5)	# 12-16

@State
def CmnActVertSpin():
    sprite('yu071_00', 2)	# 1-2
    label(0)
    sprite('yu071_01', 2)	# 3-4
    sprite('yu071_02', 2)	# 5-6
    sprite('yu071_03', 2)	# 7-8
    sprite('yu071_04', 2)	# 9-10
    sprite('yu071_05', 2)	# 11-12
    sprite('yu071_06', 2)	# 13-14
    sprite('yu071_07', 2)	# 15-16
    sprite('yu071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('yu124_00', 2)	# 1-2
    label(0)
    sprite('yu124_01', 2)	# 3-4
    sprite('yu124_02', 2)	# 5-6
    sprite('yu124_03', 2)	# 7-8
    sprite('yu124_04', 2)	# 9-10
    sprite('yu124_05', 2)	# 11-12
    sprite('yu124_06', 2)	# 13-14
    sprite('yu124_07', 2)	# 15-16
    sprite('yu124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('yu077_02', 4)	# 1-4
    label(0)
    sprite('yu077_03', 3)	# 5-7
    sprite('yu077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('yu077_05', 5)	# 1-5
    sprite('yu077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('yu077_02', 4)	# 1-4
    label(0)
    sprite('yu077_03', 3)	# 5-7
    sprite('yu077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('yu077_05', 5)	# 1-5
    sprite('yu077_06', 4)	# 6-9

@State
def CmnActBurstBegin():
    label(0)
    sprite('yu121_00', 2)	# 1-2
    sprite('yu121_01', 2)	# 3-4
    sprite('yu121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('yu121_07', 3)	# 1-3
    sprite('yu121_08', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    label(0)
    sprite('yu121_00', 2)	# 1-2
    sprite('yu121_01', 2)	# 3-4
    sprite('yu121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('yu121_07', 3)	# 1-3
    sprite('yu121_08', 3)	# 4-6

@State
def CmnActOverDriveBegin():
    sprite('yu121_00', 3)	# 1-3
    sprite('yu121_01', 3)	# 4-6
    sprite('yu121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('yu121_02', 32767)	# 10-32776
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('yu121_07', 4)	# 1-4
    sprite('yu121_08', 4)	# 5-8
    sprite('yu010_00', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('yu121_00', 3)	# 1-3
    sprite('yu121_01', 3)	# 4-6
    sprite('yu121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('yu121_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('yu121_07', 6)	# 1-6
    sprite('yu121_08', 6)	# 7-12
    sprite('yu020_04', 3)	# 13-15
    sprite('yu020_05', 3)	# 16-18
    sprite('yu020_06', 3)	# 19-21
    label(0)
    sprite('yu020_07', 4)	# 22-25
    sprite('yu020_08', 4)	# 26-29
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('yu121_00', 2)	# 1-2
    sprite('yu121_01', 2)	# 3-4
    sprite('yu121_02', 2)	# 5-6
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PYU_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 13, 0)
    sprite('yu121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('yu121_07', 6)	# 1-6
    sprite('yu121_08', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('yu121_00', 3)	# 1-3
    sprite('yu121_01', 3)	# 4-6
    sprite('yu121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PYU_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 13, 0)
    sprite('yu121_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('yu121_07', 6)	# 1-6
    sprite('yu121_08', 6)	# 7-12
    sprite('yu020_04', 3)	# 13-15
    sprite('yu020_05', 3)	# 16-18
    sprite('yu020_06', 3)	# 19-21
    label(0)
    sprite('yu020_07', 4)	# 22-25
    sprite('yu020_08', 4)	# 26-29
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('yu121_00', 3)	# 1-3
    sprite('yu121_01', 3)	# 4-6
    sprite('yu121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PYU_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 13, 0)
    sprite('yu121_02', 32767)	# 10-32776
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('yu121_07', 6)	# 1-6
    sprite('yu121_08', 6)	# 7-12

@State
def CmnActAirCrossChangeBegin():
    sprite('yu121_00', 3)	# 1-3
    sprite('yu121_01', 3)	# 4-6
    sprite('yu121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PYU_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 13, 0)
    sprite('yu121_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('yu121_03', 3)	# 1-3
    label(0)
    sprite('yu121_04', 2)	# 4-5
    sprite('yu121_05', 2)	# 6-7
    sprite('yu121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('yu121_07', 6)	# 1-6
    sprite('yu121_08', 6)	# 7-12
    sprite('yu020_04', 3)	# 13-15
    sprite('yu020_05', 3)	# 16-18
    sprite('yu020_06', 3)	# 19-21
    label(0)
    sprite('yu020_07', 4)	# 22-25
    sprite('yu020_08', 4)	# 26-29
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
        AttackLevel_(4)
        Unknown11028(24)
        Hitstop(20)
        Unknown23027()
        Unknown11063(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 7)	# 1-7
    sprite('null', 10)	# 8-17
    sprite('null', 1)	# 18-18
    Unknown23151(22, 104)
    Unknown2017(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown23119(16750300, 8, 2)
    sprite('null', 1)	# 19-19
    teleportRelativeX(-1600000)
    Unknown1007(650000)
    physicsXImpulse(90000)
    physicsYImpulse(-37500)
    sprite('yu250_03', 2)	# 20-21	 **attackbox here**
    Unknown23027()
    sprite('yu250_03', 2)	# 22-23	 **attackbox here**
    sprite('yu250_03', 2)	# 24-25	 **attackbox here**
    sprite('yu250_03', 2)	# 26-27	 **attackbox here**
    sprite('yu250_03', 2)	# 28-29	 **attackbox here**
    sprite('yu250_03', 2)	# 30-31	 **attackbox here**
    sprite('yu250_03', 2)	# 32-33	 **attackbox here**
    sprite('yu250_03', 2)	# 34-35	 **attackbox here**
    sprite('yu250_03', 2)	# 36-37	 **attackbox here**
    RefreshMultihit()
    Unknown2017(1)
    Unknown2053(1)
    Unknown2034(1)
    label(1)
    sprite('yu250_03', 2)	# 38-39	 **attackbox here**
    gotoLabel(1)
    label(9)
    sprite('yu250_03', 2)	# 40-41	 **attackbox here**
    Unknown1084(1)
    sprite('yu232_02', 6)	# 42-47
    Unknown8000(-1, 1, 1)
    sprite('yu232_03', 4)	# 48-51
    sprite('yu232_04', 4)	# 52-55
    sprite('yu010_01', 4)	# 56-59
    sprite('yu010_00', 4)	# 60-63

@State
def CmnActChangePartnerQuickIn():
    sprite('yu032_05', 3)	# 1-3
    sprite('yu032_06', 5)	# 4-8
    sprite('yu032_09', 7)	# 9-15
    sprite('yu032_09', 7)	# 16-22
    sprite('yu032_10', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('yu033_00', 3)	# 1-3
    sprite('yu033_01', 3)	# 4-6
    sprite('yu033_02', 3)	# 7-9
    sprite('yu033_03', 3)	# 10-12
    sprite('yu033_04', 3)	# 13-15
    sprite('yu033_00', 3)	# 16-18
    sprite('yu033_01', 3)	# 19-21
    sprite('yu033_02', 3)	# 22-24
    sprite('yu033_03', 3)	# 25-27
    sprite('yu033_04', 3)	# 28-30
    sprite('yu033_00', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('yu033_00', 1)	# 1-1
    sprite('yu033_01', 4)	# 2-5
    sprite('yu033_02', 4)	# 6-9
    loopRest()
    label(0)
    sprite('yu033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yu033_03', 3)	# 13-15
    sprite('yu033_04', 3)	# 16-18

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('yu611_00', 5)	# 1-5
    sprite('yu611_01', 5)	# 6-10
    sprite('yu611_02', 7)	# 11-17
    sprite('yu611_03', 7)	# 18-24
    sprite('yu611_04', 7)	# 25-31
    sprite('yu611_03', 7)	# 32-38
    sprite('yu611_02', 7)	# 39-45
    sprite('yu611_03', 7)	# 46-52
    sprite('yu611_04', 7)	# 53-59
    sprite('yu611_03', 7)	# 60-66
    sprite('yu611_01', 4)	# 67-70
    sprite('yu611_00', 4)	# 71-74
    sprite('yu000_03', 2)	# 75-76

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
    sprite('yu020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('yu020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('yu010_00', 2)	# 11-12
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
    sprite('yu403_00', 3)	# 1-3
    sprite('yu403_07', 3)	# 4-6
    Unknown23029(11, 4080, 0)
    sprite('yu403_08', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    GFX_0('fire_booster', 100)
    sprite('yu403_09', 3)	# 10-12
    sprite('yu403_11', 3)	# 13-15
    if (SLOT_31 < 9):
        selfDamage(500)
        SLOT_31 = (SLOT_31 + 1)
    SFX_3('distortion_b')
    Recovery()
    sprite('yu403_12', 3)	# 16-18
    sprite('yu450_00', 3)	# 19-21
    Unknown2006()
    sprite('yu450_01', 3)	# 22-24
    Unknown7007('7079753231325f300000000000000000640000007079753231325f310000000000000000640000007079753231325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu450_02', 3)	# 25-27
    GFX_1('persona_enter_ply', 0)
    sprite('yu450_03', 3)	# 28-30
    sprite('yu450_04', 3)	# 31-33
    sprite('yu450_05', 3)	# 34-36
    sprite('yu450_06', 3)	# 37-39
    sprite('yu450_07', 3)	# 40-42
    Unknown23029(11, 5030, 0)
    sprite('yu450_08', 1)	# 43-43
    sprite('yu450_09', 1)	# 44-44
    sprite('yu450_10', 3)	# 45-47
    sprite('yu450_11', 3)	# 48-50
    sprite('yu450_12', 4)	# 51-54
    sprite('yu450_13', 4)	# 55-58
    sprite('yu450_14', 4)	# 59-62
    sprite('yu450_12', 4)	# 63-66
    sprite('yu450_13', 4)	# 67-70
    sprite('yu450_14', 4)	# 71-74
    sprite('yu450_12', 4)	# 75-78
    sprite('yu450_13', 4)	# 79-82
    sprite('yu450_14', 4)	# 83-86
    sprite('yu450_12', 4)	# 87-90
    sprite('yu450_13', 4)	# 91-94
    sprite('yu450_14', 4)	# 95-98
    sprite('yu450_15', 4)	# 99-102
    sprite('yu010_02', 4)	# 103-106
    sprite('yu010_01', 4)	# 107-110
    sprite('yu010_00', 3)	# 111-113

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(40000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1000)
        AirUntechableTime(35)
        Unknown11042(1)
        Unknown2003(1)
        Unknown11063(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('yu400_01', 3)	# 1-3
    Unknown7007('7079753230305f300000000000000000640000007079753230305f310000000000000000640000007079753230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu400_02', 3)	# 4-6
    sprite('yu400_03', 3)	# 7-9
    sprite('yu400_04', 3)	# 10-12
    setInvincible(1)
    Unknown22022(0)
    Unknown22038(0)
    Unknown22019('0000000000000000000000000100000000000000')
    GFX_0('rinkakuaura_Assist', 100)
    Unknown38(5, 1)
    Unknown23029(5, 56, 0)
    Unknown23029(11, 4010, 0)
    GFX_0('rinkakuaura2', 100)
    Unknown23029(1, 57, 0)
    sprite('yu400_05', 3)	# 13-15
    sprite('yu400_06', 3)	# 16-18
    Unknown1084(1)
    physicsYImpulse(2000)
    sprite('yu400_07', 4)	# 19-22	 **attackbox here**
    RefreshMultihit()
    sprite('yu400_08', 4)	# 23-26	 **attackbox here**
    GFX_0('diacharge', 104)
    Unknown38(6, 1)
    Unknown23029(6, 58, 0)
    GFX_0('diacharge_floor', 0)
    Unknown38(7, 1)
    Unknown23029(7, 59, 0)
    sprite('yu400_09', 4)	# 27-30	 **attackbox here**
    sprite('yu400_10', 4)	# 31-34	 **attackbox here**
    Unknown23027()
    SFX_3('yu004')

    def upon_3():
        Unknown47('090000000200000033000000000000003c0000000200000034000000')
        if SLOT_52:
            SFX_3('yu004')
            SLOT_51 = 0
        if (SLOT_145 <= 300000):
            Unknown48('19000000020000003500000018000000020000004b000000')
            if SLOT_53:
                Unknown21000(10)
                SLOT_51 = (SLOT_51 + 1)
                Unknown36(24)
                Unknown21000(20)
                Unknown35()
        else:
            Unknown21000(20)
    physicsYImpulse(-600)
    SFX_3('yu002')
    sprite('yu400_07', 3)	# 35-37	 **attackbox here**
    sprite('yu400_08', 3)	# 38-40	 **attackbox here**
    sprite('yu400_09', 3)	# 41-43	 **attackbox here**
    sprite('yu400_10', 3)	# 44-46	 **attackbox here**
    sprite('yu400_07', 3)	# 47-49	 **attackbox here**
    sprite('yu400_08', 3)	# 50-52	 **attackbox here**
    sprite('yu400_09', 3)	# 53-55	 **attackbox here**
    sprite('yu400_10', 3)	# 56-58	 **attackbox here**
    sprite('yu400_07', 3)	# 59-61	 **attackbox here**
    sprite('yu400_08', 3)	# 62-64	 **attackbox here**
    sprite('yu400_09', 3)	# 65-67	 **attackbox here**
    sprite('yu400_10', 3)	# 68-70	 **attackbox here**
    sprite('yu400_07', 3)	# 71-73	 **attackbox here**
    sprite('yu400_08', 3)	# 74-76	 **attackbox here**
    sprite('yu400_09', 3)	# 77-79	 **attackbox here**
    sprite('yu400_10', 3)	# 80-82	 **attackbox here**
    sprite('yu400_07', 3)	# 83-85	 **attackbox here**
    sprite('yu400_08', 3)	# 86-88	 **attackbox here**
    sprite('yu400_09', 3)	# 89-91	 **attackbox here**
    sprite('yu400_10', 3)	# 92-94	 **attackbox here**
    sprite('yu400_07', 3)	# 95-97	 **attackbox here**
    sprite('yu400_08', 3)	# 98-100	 **attackbox here**
    sprite('yu400_09', 3)	# 101-103	 **attackbox here**
    sprite('yu400_10', 3)	# 104-106	 **attackbox here**
    sprite('yu400_07', 3)	# 107-109	 **attackbox here**
    sprite('yu400_08', 3)	# 110-112	 **attackbox here**
    sprite('yu400_09', 3)	# 113-115	 **attackbox here**
    sprite('yu400_10', 3)	# 116-118	 **attackbox here**
    sprite('yu400_07', 3)	# 119-121	 **attackbox here**
    setGravity(500)
    setInvincible(0)
    Unknown23029(5, 52, 0)
    Unknown23029(6, 53, 0)
    Unknown23029(7, 54, 0)
    Unknown23029(11, 11, 0)
    sprite('yu400_08', 3)	# 122-124	 **attackbox here**
    sprite('yu400_09', 3)	# 125-127	 **attackbox here**
    sprite('yu400_10', 3)	# 128-130	 **attackbox here**
    loopRest()
    label(1)
    sprite('yu400_11', 4)	# 131-134
    sprite('yu400_12', 4)	# 135-138
    sprite('yu400_13', 4)	# 139-142

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('yu404_00', 3)	# 1-3
    Unknown1084(1)
    sprite('yu404_01', 4)	# 4-7
    Unknown23029(11, 4074, 0)
    Unknown7007('7079753231305f300000000000000000640000007079753231305f310000000000000000640000007079753231305f320000000000000000640000007079753231315f32000000000000000064000000')
    sprite('yu404_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    sprite('yu404_03', 4)	# 12-15
    physicsXImpulse(-3000)
    sprite('yu404_03', 4)	# 16-19
    Unknown1019(120)
    sprite('yu404_04', 4)	# 20-23
    Unknown1019(110)
    sprite('yu404_04', 4)	# 24-27
    Unknown1019(100)
    sprite('yu404_05', 4)	# 28-31
    Unknown1019(50)
    sprite('yu404_05', 4)	# 32-35
    Unknown1019(50)
    sprite('yu404_06', 4)	# 36-39
    Unknown1019(50)
    Recovery()
    sprite('yu404_06', 5)	# 40-44
    sprite('yu404_07', 5)	# 45-49
    Unknown1084(1)
    sprite('yu404_08', 9)	# 50-58

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
    Unknown2036(104, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-10434)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('yu020_07', 4)	# 3-6
    sprite('yu020_08', 4)	# 7-10
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
        setInvincible(1)
        Unknown13024(0)
        Unknown30063(1)
    sprite('yu430_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('yu430_00', 3)	# 4-6
    SFX_1('yu310')
    sprite('yu430_01', 4)	# 7-10
    sprite('yu430_02', 4)	# 11-14
    sprite('yu430_03', 4)	# 15-18
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(5, 1)
    sprite('yu430_04', 4)	# 19-22
    sprite('yu430_05', 4)	# 23-26
    sprite('yu430_06', 4)	# 27-30
    sprite('yu430_07', 4)	# 31-34
    sprite('yu430_08', 4)	# 35-38
    sprite('yu430_09', 4)	# 39-42
    sprite('yu430_10', 4)	# 43-46
    sprite('yu430_11', 4)	# 47-50
    sprite('yu430_12', 3)	# 51-53
    sprite('yu430_13', 3)	# 54-56
    sprite('yu430_14', 3)	# 57-59
    sprite('yu430_15', 3)	# 60-62
    sprite('yu430_16', 3)	# 63-65
    sprite('yu430_17', 3)	# 66-68
    sprite('yu430_18', 4)	# 69-72
    Unknown21007(5, 32)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('yu430_19', 4)	# 73-76
    Unknown23029(11, 10060, 0)
    sprite('yu430_20', 4)	# 77-80
    sprite('yu430_21', 4)	# 81-84
    sprite('yu430_19', 4)	# 85-88
    sprite('yu430_20', 4)	# 89-92
    setInvincible(0)
    sprite('yu430_21', 4)	# 93-96
    sprite('yu430_19', 4)	# 97-100
    Unknown7007('7079753235315f300000000000000000640000007079753235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu430_20', 4)	# 101-104
    sprite('yu430_21', 4)	# 105-108
    sprite('yu430_19', 5)	# 109-113
    sprite('yu430_20', 5)	# 114-118
    sprite('yu430_21', 5)	# 119-123
    sprite('yu430_19', 5)	# 124-128
    sprite('yu430_20', 5)	# 129-133
    sprite('yu430_21', 5)	# 134-138
    sprite('yu430_19', 5)	# 139-143
    sprite('yu430_20', 5)	# 144-148
    sprite('yu430_21', 5)	# 149-153
    sprite('yu430_22', 4)	# 154-157
    sprite('yu430_23', 4)	# 158-161
    Recovery()

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        Unknown13024(0)
        Unknown30063(1)
    sprite('yu430_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('yu430_00', 3)	# 4-6
    SFX_1('yu310')
    sprite('yu430_01', 4)	# 7-10
    sprite('yu430_02', 4)	# 11-14
    sprite('yu430_03', 4)	# 15-18
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(5, 1)
    sprite('yu430_04', 4)	# 19-22
    sprite('yu430_05', 4)	# 23-26
    sprite('yu430_06', 4)	# 27-30
    sprite('yu430_07', 4)	# 31-34
    sprite('yu430_08', 4)	# 35-38
    sprite('yu430_09', 4)	# 39-42
    sprite('yu430_10', 4)	# 43-46
    sprite('yu430_11', 4)	# 47-50
    sprite('yu430_12', 3)	# 51-53
    sprite('yu430_13', 3)	# 54-56
    sprite('yu430_14', 3)	# 57-59
    sprite('yu430_15', 3)	# 60-62
    sprite('yu430_16', 3)	# 63-65
    sprite('yu430_17', 3)	# 66-68
    sprite('yu430_18', 4)	# 69-72
    Unknown21007(5, 32)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('yu430_19', 4)	# 73-76
    Unknown23029(11, 10061, 0)
    sprite('yu430_20', 4)	# 77-80
    sprite('yu430_21', 4)	# 81-84
    sprite('yu430_19', 4)	# 85-88
    sprite('yu430_20', 4)	# 89-92
    setInvincible(0)
    sprite('yu430_21', 4)	# 93-96
    sprite('yu430_19', 4)	# 97-100
    Unknown7007('7079753235315f300000000000000000640000007079753235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu430_20', 4)	# 101-104
    sprite('yu430_21', 4)	# 105-108
    sprite('yu430_19', 5)	# 109-113
    sprite('yu430_20', 5)	# 114-118
    sprite('yu430_21', 5)	# 119-123
    sprite('yu430_19', 5)	# 124-128
    sprite('yu430_20', 5)	# 129-133
    sprite('yu430_21', 5)	# 134-138
    sprite('yu430_19', 5)	# 139-143
    sprite('yu430_20', 5)	# 144-148
    sprite('yu430_21', 5)	# 149-153
    sprite('yu430_22', 4)	# 154-157
    sprite('yu430_23', 4)	# 158-161
    Recovery()

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
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 8)	# 121-128
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-580000)
    Unknown1007(2900000)
    physicsXImpulse(20000)
    physicsYImpulse(-100000)
    sprite('yu250_03', 3)	# 129-131	 **attackbox here**
    sprite('yu250_03', 3)	# 132-134	 **attackbox here**
    sprite('yu250_03', 3)	# 135-137	 **attackbox here**
    sprite('yu250_03', 3)	# 138-140	 **attackbox here**
    sprite('yu250_03', 3)	# 141-143	 **attackbox here**
    sprite('yu250_03', 3)	# 144-146	 **attackbox here**
    sprite('yu250_03', 3)	# 147-149	 **attackbox here**
    Unknown2053(1)
    sprite('yu250_03', 3)	# 150-152	 **attackbox here**
    sendToLabelUpon(2, 9)
    label(1)
    sprite('yu250_03', 3)	# 153-155	 **attackbox here**
    sprite('yu250_03', 3)	# 156-158	 **attackbox here**
    gotoLabel(1)
    label(9)
    sprite('yu232_02', 6)	# 159-164
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('yu232_03', 6)	# 165-170
    sprite('yu232_04', 6)	# 171-176
    sprite('yu010_01', 6)	# 177-182
    sprite('yu010_00', 7)	# 183-189
endState()

@State
def CmnActChangeReturnAppealBurst():
    sprite('yu064_02', 35)	# 1-35
    sprite('yu064_03', 5)	# 36-40
    sprite('yu010_02', 5)	# 41-45
    sprite('yu010_01', 5)	# 46-50
    sprite('yu010_00', 5)	# 51-55
    sprite('yu000_00', 5)	# 56-60
    loopRest()

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2006()
        Unknown1112('')
        Unknown14077(0)

        def upon_43():
            if (SLOT_48 == 106):
                Unknown14077(1)
                HitOrBlockCancel('NmlAtk5A2nd')
                HitOrBlockCancel('NmlAtk5B')
                HitOrBlockCancel('NmlAtk6B')
                HitOrBlockCancel('NmlAtk4B')
                HitOrBlockCancel('NmlAtk2B')
                HitOrBlockCancel('NmlAtk3B')
                HitOrBlockCancel('NmlAtk1B')
                HitOrBlockCancel('NmlAtk2C')
                HitOrBlockCancel('CmnActCrushAttack')
                HitOrBlockCancel('NmlAtkThrow')
                HitOrBlockCancel('NmlAtkBackThrow')
            if (SLOT_48 == 107):
                sendToLabel(1)
            if (SLOT_48 == 109):
                Unknown2063()
    sprite('yu205_00', 2)	# 1-2
    Unknown1051(70)
    sprite('yu205_01', 2)	# 3-4
    sprite('yu205_02', 3)	# 5-7
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 102, 0)
    Unknown7007('7079753132305f300000000000000000640000007079753132305f310000000000000000640000007079753132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu205_03', 5)	# 8-12
    sprite('yu205_04', 1)	# 13-13
    sprite('yu205_04', 3)	# 14-16
    sprite('yu205_02', 4)	# 17-20
    sprite('yu205_03', 1)	# 21-21
    sprite('yu205_03', 3)	# 22-24
    Recovery()
    sprite('yu205_04', 4)	# 25-28
    sprite('yu205_02', 4)	# 29-32
    sprite('yu205_03', 4)	# 33-36
    sprite('yu205_04', 4)	# 37-40
    label(0)
    sprite('yu205_02', 4)	# 41-44
    if (SLOT_51 >= 1):
        gotoLabel(1)
    SLOT_51 = (SLOT_51 + 1)
    sprite('yu205_03', 4)	# 45-48
    sprite('yu205_04', 4)	# 49-52
    gotoLabel(0)
    label(1)
    sprite('yu205_05', 5)	# 53-57
    sprite('yu205_06', 6)	# 58-63

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_43():
            if (SLOT_48 == 105):
                Unknown14072('NmlAtk5A3rd')
                Unknown14072('NmlAtk5B')
                Unknown14072('NmlAtk6B')
                Unknown14072('NmlAtk4B')
                Unknown14072('NmlAtk3B')
                Unknown14072('NmlAtk1B')
                Unknown14072('NmlAtk2B')
                Unknown14072('NmlAtk2C')
                Unknown14072('AgiA')
                Unknown14072('AgiB')
                Unknown14072('AgiEX')
                Unknown14072('MaharagiA')
                Unknown14072('MaharagiB')
                Unknown14072('MaharagiEX')
                Unknown14072('FireBoosterA')
                Unknown14072('FireBoosterB')
                Unknown14072('FireBoosterC')
                Unknown14072('UltimateAgidine')
                Unknown14072('UltimateAgidine_OD')
                Unknown14072('UltimateMaharagidine')
                Unknown14072('UltimateMaharagidineOD')
                Unknown14072('CmnActCrushAttack')
                Unknown14072('CmnActInvincibleAttack')
    sprite('yu206_00', 3)	# 1-3
    sprite('yu206_01', 3)	# 4-6
    Unknown23029(11, 101, 0)
    SFX_1('pyu123_2')
    sprite('yu206_02', 3)	# 7-9
    sprite('yu206_03', 3)	# 10-12
    GFX_1('persona_enter_ply', 0)
    sprite('yu206_04', 3)	# 13-15
    sprite('yu206_05', 3)	# 16-18
    sprite('yu206_03', 3)	# 19-21
    Unknown14070('NmlAtk5A3rd')
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk6B')
    Unknown14070('NmlAtk4B')
    Unknown14070('NmlAtk3B')
    Unknown14070('NmlAtk1B')
    Unknown14070('NmlAtk2B')
    Unknown14070('NmlAtk2C')
    Unknown14070('AgiA')
    Unknown14070('AgiB')
    Unknown14070('AgiEX')
    Unknown14070('MaharagiA')
    Unknown14070('MaharagiB')
    Unknown14070('MaharagiEX')
    Unknown14070('FireBoosterA')
    Unknown14070('FireBoosterB')
    Unknown14070('FireBoosterC')
    Unknown14070('UltimateAgidine')
    Unknown14070('UltimateAgidine_OD')
    Unknown14070('UltimateMaharagidine')
    Unknown14070('UltimateMaharagidineOD')
    Unknown14070('CmnActCrushAttack')
    Unknown14070('CmnActInvincibleAttack')
    HitOrBlockCancel('NmlAtkThrow')
    HitOrBlockCancel('NmlAtkBackThrow')
    sprite('yu206_04', 3)	# 22-24
    Recovery()
    sprite('yu206_05', 3)	# 25-27
    sprite('yu206_03', 2)	# 28-29
    sprite('yu206_03', 1)	# 30-30
    Unknown14074('NmlAtk5A3rd')
    Unknown14074('NmlAtk5B')
    Unknown14074('NmlAtk6B')
    Unknown14074('NmlAtk4B')
    Unknown14074('NmlAtk3B')
    Unknown14074('NmlAtk1B')
    Unknown14074('NmlAtk2B')
    Unknown14074('NmlAtk2C')
    Unknown14074('NmlAtk5A2nd')
    Unknown14074('NmlAtk5B')
    Unknown14074('NmlAtk2B')
    Unknown14074('AgiA')
    Unknown14074('AgiB')
    Unknown14074('AgiEX')
    Unknown14074('MaharagiA')
    Unknown14074('MaharagiB')
    Unknown14074('MaharagiEX')
    Unknown14074('FireBoosterA')
    Unknown14074('FireBoosterB')
    Unknown14074('FireBoosterC')
    Unknown14074('UltimateAgidine')
    Unknown14074('UltimateAgidine_OD')
    Unknown14074('UltimateMaharagidine')
    Unknown14074('UltimateMaharagidineOD')
    Unknown14074('CmnActCrushAttack')
    Unknown14074('CmnActInvincibleAttack')
    sprite('yu206_04', 3)	# 31-33
    sprite('yu206_05', 3)	# 34-36
    sprite('yu206_03', 3)	# 37-39
    sprite('yu206_04', 3)	# 40-42
    sprite('yu206_06', 3)	# 43-45
    sprite('yu206_07', 3)	# 46-48
    sprite('yu206_08', 3)	# 49-51
    sprite('yu206_09', 3)	# 52-54

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_43():
            if (SLOT_48 == 202):
                Unknown14072('NmlAtk5A4th')
                Unknown14072('NmlAtk5B')
                Unknown14072('NmlAtk6B')
                Unknown14072('NmlAtk4B')
                Unknown14072('NmlAtk3B')
                Unknown14072('NmlAtk1B')
                Unknown14072('NmlAtk2B')
                Unknown14072('NmlAtk2C')
                Unknown14072('AgiA')
                Unknown14072('AgiB')
                Unknown14072('AgiEX')
                Unknown14072('MaharagiA')
                Unknown14072('MaharagiB')
                Unknown14072('MaharagiEX')
                Unknown14072('FireBoosterA')
                Unknown14072('FireBoosterB')
                Unknown14072('FireBoosterC')
                Unknown14072('UltimateAgidine')
                Unknown14072('UltimateAgidine_OD')
                Unknown14072('UltimateMaharagidine')
                Unknown14072('UltimateMaharagidineOD')
                Unknown14072('CmnActCrushAttack')
                Unknown14072('CmnActInvincibleAttack')
            if (SLOT_48 == 210):
                Unknown14074('NmlAtk5A4th')
                Unknown14074('NmlAtk5B')
                Unknown14074('NmlAtk6B')
                Unknown14074('NmlAtk4B')
                Unknown14074('NmlAtk3B')
                Unknown14074('NmlAtk1B')
                Unknown14074('NmlAtk2B')
                Unknown14074('NmlAtk2C')
                Unknown14074('NmlAtk5A2nd')
                Unknown14074('NmlAtk5B')
                Unknown14074('NmlAtk2B')
                Unknown14074('AgiA')
                Unknown14074('AgiB')
                Unknown14074('AgiEX')
                Unknown14074('MaharagiA')
                Unknown14074('MaharagiB')
                Unknown14074('MaharagiEX')
                Unknown14074('FireBoosterA')
                Unknown14074('FireBoosterB')
                Unknown14074('FireBoosterC')
                Unknown14074('UltimateAgidine')
                Unknown14074('UltimateAgidine_OD')
                Unknown14074('UltimateMaharagidine')
                Unknown14074('UltimateMaharagidineOD')
                Unknown14074('CmnActCrushAttack')
                Unknown14074('CmnActInvincibleAttack')
    sprite('yu401_00', 2)	# 1-2
    sprite('yu401_01', 1)	# 3-3
    Unknown23029(11, 201, 0)
    sprite('yu401_01', 1)	# 4-4
    sprite('yu401_02', 2)	# 5-6
    sprite('yu401_03', 1)	# 7-7
    sprite('yu401_03', 1)	# 8-8
    sprite('yu401_04', 3)	# 9-11
    Unknown7007('7079753132335f31000000000000000064000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu401_05', 3)	# 12-14
    Unknown14070('NmlAtk5A4th')
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk6B')
    Unknown14070('NmlAtk4B')
    Unknown14070('NmlAtk3B')
    Unknown14070('NmlAtk1B')
    Unknown14070('NmlAtk2B')
    Unknown14070('NmlAtk2C')
    Unknown14070('AgiA')
    Unknown14070('AgiB')
    Unknown14070('AgiEX')
    Unknown14070('MaharagiA')
    Unknown14070('MaharagiB')
    Unknown14070('MaharagiEX')
    Unknown14070('FireBoosterA')
    Unknown14070('FireBoosterB')
    Unknown14070('FireBoosterC')
    Unknown14070('UltimateAgidine')
    Unknown14070('UltimateAgidine_OD')
    Unknown14070('UltimateMaharagidine')
    Unknown14070('UltimateMaharagidineOD')
    Unknown14070('CmnActCrushAttack')
    Unknown14070('CmnActInvincibleAttack')
    sprite('yu401_06', 3)	# 15-17
    sprite('yu401_05', 1)	# 18-18
    Recovery()
    sprite('yu401_05', 1)	# 19-19
    sprite('yu401_04', 3)	# 20-22
    sprite('yu401_05', 3)	# 23-25
    sprite('yu401_06', 1)	# 26-26
    sprite('yu401_06', 2)	# 27-28
    sprite('yu401_05', 3)	# 29-31
    sprite('yu401_04', 3)	# 32-34
    sprite('yu401_05', 3)	# 35-37
    sprite('yu401_03', 3)	# 38-40
    sprite('yu401_02', 3)	# 41-43
    sprite('yu401_01', 3)	# 44-46
    sprite('yu401_00', 3)	# 47-49

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('yu404_00', 3)	# 1-3
    Unknown1084(1)
    sprite('yu404_01', 4)	# 4-7
    Unknown23029(11, 5020, 0)
    Unknown7007('7079753231305f300000000000000000640000007079753231305f310000000000000000640000007079753231305f320000000000000000640000007079753231315f32000000000000000064000000')
    sprite('yu404_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    sprite('yu404_03', 3)	# 12-14
    physicsXImpulse(-10000)
    sprite('yu404_03', 3)	# 15-17
    Unknown1019(120)
    sprite('yu404_04', 3)	# 18-20
    Unknown1019(110)
    sprite('yu404_04', 3)	# 21-23
    Unknown1019(100)
    sprite('yu404_05', 2)	# 24-25
    Unknown1019(50)
    sprite('yu404_05', 1)	# 26-26
    Recovery()
    sprite('yu404_05', 3)	# 27-29
    Unknown1019(50)
    sprite('yu404_06', 3)	# 30-32
    Unknown1019(50)
    sprite('yu404_06', 5)	# 33-37
    sprite('yu404_07', 9)	# 38-46
    Unknown1084(1)
    sprite('yu404_08', 9)	# 47-55

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1000)
        PushbackX(9000)
        AirPushbackY(10000)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk3B')
        HitOrBlockCancel('NmlAtk1B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('yu200_00', 3)	# 1-3
    sprite('yu200_00', 1)	# 4-4
    Unknown1051(80)
    sprite('yu200_01', 5)	# 5-9
    physicsXImpulse(8000)
    sprite('yu200_02', 4)	# 10-13	 **attackbox here**
    Unknown1019(0)
    SFX_3('slash_rapier_fast')
    RefreshMultihit()
    Unknown7007('7079753130305f300000000000000000640000007079753130305f310000000000000000640000007079753130305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu200_03', 3)	# 14-16
    Recovery()
    Unknown2063()
    sprite('yu200_04', 3)	# 17-19
    sprite('yu200_05', 3)	# 20-22
    sprite('yu200_06', 3)	# 23-25
    sprite('yu200_07', 3)	# 26-28

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1000)
        AirPushbackY(15000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk4A3nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk3B')
        HitOrBlockCancel('NmlAtk1B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('yu201_00', 3)	# 1-3
    physicsXImpulse(5000)
    sprite('yu201_01', 3)	# 4-6
    sprite('yu201_02', 3)	# 7-9
    sprite('yu201_03', 3)	# 10-12	 **attackbox here**
    Unknown1084(1)
    RefreshMultihit()
    SFX_3('slash_rapier_fast')
    Unknown7007('7079753130315f300000000000000000640000007079753130315f310000000000000000640000007079753130315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu201_04', 2)	# 13-14	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('yu201_05', 2)	# 15-16
    sprite('yu201_06', 4)	# 17-20
    sprite('yu201_07', 3)	# 21-23
    sprite('yu201_08', 3)	# 24-26
endState()

@State
def NmlAtk4A3nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1200)
        AirPushbackX(10000)
        AirPushbackY(-20000)
        PushbackX(20000)
        AirUntechableTime(30)
        Unknown9310(1)
        AirHitstunAnimation(9)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A4th')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
    sprite('yu202_00', 5)	# 1-5
    physicsXImpulse(8000)
    sprite('yu202_01', 3)	# 6-8
    sprite('yu202_02', 3)	# 9-11
    Unknown7007('7079753130325f300000000000000000640000007079753130325f310000000000000000640000007079753130325f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1019(90)
    sprite('yu202_03', 3)	# 12-14	 **attackbox here**
    Unknown1019(90)
    sprite('yu202_04', 3)	# 15-17	 **attackbox here**
    Unknown1019(0)
    SFX_3('slash_rapier_middle')
    sprite('yu202_05', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('yu202_06', 3)	# 21-23
    sprite('yu202_07', 3)	# 24-26
    sprite('yu202_08', 5)	# 27-31
    sprite('yu202_09', 3)	# 32-34
    sprite('yu202_10', 3)	# 35-37
    sprite('yu202_11', 3)	# 38-40

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk3B')
        HitOrBlockCancel('NmlAtk1B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('yu230_00', 4)	# 1-4
    sprite('yu230_01', 3)	# 5-7
    Unknown1051(80)
    sprite('yu230_02', 2)	# 8-9	 **attackbox here**
    SFX_3('hit_l_fast')
    RefreshMultihit()
    Unknown7009(0)
    sprite('yu230_03', 3)	# 10-12
    Recovery()
    WhiffCancelEnable(1)
    sprite('yu230_05', 4)	# 13-16
    sprite('yu230_04', 4)	# 17-20
    sprite('yu230_00', 3)	# 21-23

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk3B')
        HitOrBlockCancel('NmlAtk1B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu203_00', 3)	# 1-3
    sprite('yu203_01', 3)	# 4-6
    sprite('yu203_01', 1)	# 7-7
    sprite('yu203_02', 4)	# 8-11
    Unknown14070('NmlAtk5B2nd')
    Unknown14070('NmlAtk5B2nd_Front')
    Unknown14070('NmlAtk5B2nd_Back')
    sprite('yu203_03', 2)	# 12-13
    Unknown7007('7079753130325f310000000000000000640000007079753330325f300000000000000000640000007079753330365f310000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Sensu_Stand_A', 0)
    sprite('yu203_04', 2)	# 14-15
    sprite('yu203_05', 2)	# 16-17
    Unknown14072('NmlAtk5B2nd')
    Unknown14072('NmlAtk5B2nd_Front')
    Unknown14072('NmlAtk5B2nd_Back')
    sprite('yu203_06', 3)	# 18-20
    sprite('yu203_07', 3)	# 21-23
    sprite('yu203_08', 3)	# 24-26
    Recovery()
    Unknown2063()
    sprite('yu203_09', 5)	# 27-31
    sprite('yu203_10', 7)	# 32-38
    Unknown14074('NmlAtk5B2nd')
    Unknown14074('NmlAtk5B2nd_Front')
    Unknown14074('NmlAtk5B2nd_Back')
    sprite('yu203_11', 5)	# 39-43
    SFX_3('yu000')
    sprite('yu203_12', 5)	# 44-48

@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk3B')
        HitOrBlockCancel('NmlAtk1B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu203_00', 3)	# 1-3
    sprite('yu203_01', 3)	# 4-6
    sprite('yu203_01', 1)	# 7-7
    sprite('yu203_02', 4)	# 8-11
    Unknown14070('NmlAtk5B2nd')
    Unknown14070('NmlAtk5B2nd_Front')
    Unknown14070('NmlAtk5B2nd_Back')
    sprite('yu203_03', 2)	# 12-13
    Unknown7007('7079753130325f310000000000000000640000007079753330325f300000000000000000640000007079753330365f310000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Sensu_Stand_A', 0)
    Unknown23029(1, 1011, 0)
    sprite('yu203_04', 3)	# 14-16
    sprite('yu203_05', 3)	# 17-19
    Unknown14072('NmlAtk5B2nd')
    Unknown14072('NmlAtk5B2nd_Front')
    Unknown14072('NmlAtk5B2nd_Back')
    sprite('yu203_06', 3)	# 20-22
    sprite('yu203_07', 3)	# 23-25
    sprite('yu203_08', 3)	# 26-28
    Recovery()
    Unknown2063()
    sprite('yu203_09', 4)	# 29-32
    sprite('yu203_10', 6)	# 33-38
    Unknown14074('NmlAtk5B2nd')
    Unknown14074('NmlAtk5B2nd_Front')
    Unknown14074('NmlAtk5B2nd_Back')
    sprite('yu203_11', 5)	# 39-43
    SFX_3('yu000')
    sprite('yu203_12', 5)	# 44-48

@State
def NmlAtk4B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk3B')
        HitOrBlockCancel('NmlAtk1B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu203_00', 3)	# 1-3
    sprite('yu203_01', 3)	# 4-6
    sprite('yu203_01', 1)	# 7-7
    sprite('yu203_02', 4)	# 8-11
    Unknown14070('NmlAtk5B2nd')
    Unknown14070('NmlAtk5B2nd_Front')
    Unknown14070('NmlAtk5B2nd_Back')
    sprite('yu203_03', 2)	# 12-13
    Unknown7007('7079753130325f310000000000000000640000007079753330325f300000000000000000640000007079753330365f310000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Sensu_Stand_A', 0)
    Unknown23029(1, 1012, 0)
    sprite('yu203_04', 3)	# 14-16
    sprite('yu203_05', 3)	# 17-19
    Unknown14072('NmlAtk5B2nd')
    Unknown14072('NmlAtk5B2nd_Front')
    Unknown14072('NmlAtk5B2nd_Back')
    sprite('yu203_06', 3)	# 20-22
    sprite('yu203_07', 3)	# 23-25
    sprite('yu203_08', 3)	# 26-28
    Recovery()
    Unknown2063()
    sprite('yu203_09', 4)	# 29-32
    sprite('yu203_10', 6)	# 33-38
    Unknown14074('NmlAtk5B2nd')
    Unknown14074('NmlAtk5B2nd_Front')
    Unknown14074('NmlAtk5B2nd_Back')
    sprite('yu203_11', 5)	# 39-43
    SFX_3('yu000')
    sprite('yu203_12', 5)	# 44-48

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu204_00', 2)	# 1-2
    sprite('yu204_01', 1)	# 3-3
    sprite('yu204_01', 2)	# 4-5
    sprite('yu204_02', 3)	# 6-8
    sprite('yu204_03', 3)	# 9-11
    Unknown7007('7079753130325f310000000000000000640000007079753330325f300000000000000000640000007079753330365f310000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Sensu_Stand_A_2nd', 0)
    sprite('yu204_04', 4)	# 12-15
    sprite('yu204_05', 4)	# 16-19
    sprite('yu204_06', 4)	# 20-23
    sprite('yu204_07', 4)	# 24-27
    sprite('yu204_08', 4)	# 28-31
    sprite('yu204_09', 4)	# 32-35
    Recovery()
    Unknown2063()
    sprite('yu203_10', 3)	# 36-38
    sprite('yu203_10', 1)	# 39-39
    sprite('yu203_11', 2)	# 40-41
    SFX_3('yu000')
    sprite('yu203_11', 3)	# 42-44
    sprite('yu203_12', 4)	# 45-48

@State
def NmlAtk5B2nd_Front():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu204_00', 2)	# 1-2
    sprite('yu204_01', 1)	# 3-3
    sprite('yu204_01', 2)	# 4-5
    sprite('yu204_02', 3)	# 6-8
    sprite('yu204_03', 3)	# 9-11
    Unknown7007('7079753130325f310000000000000000640000007079753330325f300000000000000000640000007079753330365f310000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Sensu_Stand_A_2nd', 0)
    Unknown23029(1, 1011, 0)
    sprite('yu204_04', 4)	# 12-15
    sprite('yu204_05', 4)	# 16-19
    sprite('yu204_06', 4)	# 20-23
    sprite('yu204_07', 4)	# 24-27
    sprite('yu204_08', 4)	# 28-31
    sprite('yu204_09', 4)	# 32-35
    Recovery()
    Unknown2063()
    sprite('yu203_10', 3)	# 36-38
    sprite('yu203_10', 1)	# 39-39
    sprite('yu203_11', 2)	# 40-41
    SFX_3('yu000')
    sprite('yu203_11', 3)	# 42-44
    sprite('yu203_12', 5)	# 45-49

@State
def NmlAtk5B2nd_Back():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu204_00', 2)	# 1-2
    sprite('yu204_01', 1)	# 3-3
    sprite('yu204_01', 2)	# 4-5
    sprite('yu204_02', 3)	# 6-8
    sprite('yu204_03', 3)	# 9-11
    Unknown7007('7079753130325f310000000000000000640000007079753330325f300000000000000000640000007079753330365f310000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Sensu_Stand_A_2nd', 0)
    Unknown23029(1, 1012, 0)
    sprite('yu204_04', 4)	# 12-15
    sprite('yu204_05', 4)	# 16-19
    sprite('yu204_06', 4)	# 20-23
    sprite('yu204_07', 4)	# 24-27
    sprite('yu204_08', 4)	# 28-31
    sprite('yu204_09', 4)	# 32-35
    Recovery()
    Unknown2063()
    sprite('yu203_10', 3)	# 36-38
    sprite('yu203_10', 2)	# 39-40
    sprite('yu203_11', 2)	# 41-42
    SFX_3('yu000')
    sprite('yu203_11', 4)	# 43-46
    sprite('yu203_12', 6)	# 47-52

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu231_00', 4)	# 1-4
    sprite('yu231_01', 5)	# 5-9
    sprite('yu231_02', 4)	# 10-13
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('yu231_03', 1)	# 14-14
    Unknown7007('7079753330335f300000000000000000640000007079753330335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('Sensu_2A', 0)
    sprite('yu231_03', 2)	# 15-16
    sprite('yu231_04', 4)	# 17-20
    setInvincible(0)
    sprite('yu231_05', 4)	# 21-24
    sprite('yu231_06', 3)	# 25-27
    Recovery()
    Unknown2063()
    sprite('yu231_07', 3)	# 28-30
    sprite('yu231_08', 2)	# 31-32
    sprite('yu231_09', 5)	# 33-37
    SFX_3('yu000')
    sprite('yu231_10', 5)	# 38-42

@State
def NmlAtk3B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu231_00', 4)	# 1-4
    sprite('yu231_01', 5)	# 5-9
    sprite('yu231_02', 4)	# 10-13
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('yu231_03', 1)	# 14-14
    Unknown7007('7079753330335f300000000000000000640000007079753330335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('Sensu_2A', 0)
    Unknown23029(1, 1021, 0)
    sprite('yu231_03', 2)	# 15-16
    sprite('yu231_04', 4)	# 17-20
    setInvincible(0)
    sprite('yu231_05', 4)	# 21-24
    sprite('yu231_06', 3)	# 25-27
    Recovery()
    Unknown2063()
    sprite('yu231_07', 3)	# 28-30
    sprite('yu231_08', 2)	# 31-32
    sprite('yu231_09', 5)	# 33-37
    SFX_3('yu000')
    sprite('yu231_10', 5)	# 38-42

@State
def NmlAtk1B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('yu231_00', 4)	# 1-4
    sprite('yu231_01', 5)	# 5-9
    sprite('yu231_02', 4)	# 10-13
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('yu231_03', 1)	# 14-14
    Unknown7007('7079753330335f300000000000000000640000007079753330335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('Sensu_2A', 0)
    Unknown23029(1, 1022, 0)
    sprite('yu231_03', 2)	# 15-16
    sprite('yu231_04', 4)	# 17-20
    setInvincible(0)
    sprite('yu231_05', 4)	# 21-24
    sprite('yu231_06', 3)	# 25-27
    Recovery()
    Unknown2063()
    sprite('yu231_07', 3)	# 28-30
    sprite('yu231_08', 2)	# 31-32
    sprite('yu231_09', 5)	# 33-37
    SFX_3('yu000')
    sprite('yu231_10', 5)	# 38-42

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        HitLow(2)
        AirPushbackX(6000)
        AirPushbackY(13500)
        AirUntechableTime(30)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9016(1)
        HitJumpCancel(1)
    sprite('yu211_00', 3)	# 1-3
    sprite('yu211_01', 2)	# 4-5
    sprite('yu211_02', 2)	# 6-7
    sprite('yu211_04', 2)	# 8-9
    sprite('yu211_06', 3)	# 10-12	 **attackbox here**
    Unknown23054('79753231315f303500000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Unknown7007('7079753130375f300000000000000000640000007079753130375f310000000000000000640000007079753130375f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_rapier_fast')
    sprite('yu211_06', 2)	# 13-14	 **attackbox here**
    sprite('yu211_07', 4)	# 15-18
    Recovery()
    sprite('yu211_08', 4)	# 19-22
    sprite('yu211_09', 4)	# 23-26
    sprite('yu211_10', 3)	# 27-29

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1000)
        AirUntechableTime(19)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR6B')
        HitOrBlockCancel('NmlAtkAIR4B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('yu250_00', 3)	# 1-3
    sprite('yu250_01', 3)	# 4-6
    sprite('yu250_02', 3)	# 7-9
    SFX_3('slash_rapier_fast')
    sprite('yu250_03', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    Unknown7007('7079753130305f300000000000000000640000007079753130305f310000000000000000640000007079753130305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu250_04', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('yu250_05', 5)	# 16-20
    sprite('yu250_06', 5)	# 21-25

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1000)
        AirUntechableTime(19)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR6B')
        HitOrBlockCancel('NmlAtkAIR4B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('yu250_01', 3)	# 1-3
    sprite('yu250_02', 3)	# 4-6
    SFX_3('slash_rapier_fast')
    sprite('yu250_03', 3)	# 7-9	 **attackbox here**
    RefreshMultihit()
    Unknown7009(0)
    sprite('yu250_04', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('yu250_05', 5)	# 13-17
    sprite('yu250_06', 5)	# 18-22

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
    sprite('yu251_00', 4)	# 1-4
    sprite('yu251_01', 3)	# 5-7
    Unknown1039(80)
    sprite('yu251_02', 2)	# 8-9
    sprite('yu251_03', 2)	# 10-11
    Unknown1019(50)
    sprite('yu251_04', 3)	# 12-14
    Unknown22004(6, 1)
    Unknown1019(50)
    Unknown7007('7079753330345f300000000000000000640000007079753330345f310000000000000000640000007079753330325f300000000000000000640000007079753330365f31000000000000000064000000')
    GFX_0('Sensu_Air', 0)
    sprite('yu251_05', 2)	# 15-16
    Unknown1019(50)
    sprite('yu251_06', 2)	# 17-18
    sprite('yu251_07', 2)	# 19-20
    sprite('yu251_08', 2)	# 21-22
    Recovery()
    Unknown2063()
    sprite('yu251_09', 3)	# 23-25
    sprite('yu251_10', 3)	# 26-28
    sprite('yu251_11', 3)	# 29-31
    SFX_3('yu000')
    sprite('yu251_12', 3)	# 32-34

@State
def NmlAtkAIR6B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
    HitOrBlockCancel('NmlAtkAIR5C')
    HitJumpCancel(1)
    sprite('yu251_00', 4)	# 1-4
    sprite('yu251_01', 3)	# 5-7
    Unknown1039(80)
    sprite('yu251_02', 2)	# 8-9
    sprite('yu251_03', 2)	# 10-11
    Unknown1019(50)
    sprite('yu251_04', 3)	# 12-14
    Unknown22004(8, 1)
    Unknown1019(50)
    Unknown7007('7079753330345f300000000000000000640000007079753330345f310000000000000000640000007079753330325f300000000000000000640000007079753330365f31000000000000000064000000')
    GFX_0('Sensu_Air', 0)
    Unknown23029(1, 1031, 0)
    sprite('yu251_05', 2)	# 15-16
    Unknown1019(50)
    sprite('yu251_06', 2)	# 17-18
    sprite('yu251_07', 2)	# 19-20
    sprite('yu251_08', 2)	# 21-22
    Recovery()
    Unknown2063()
    sprite('yu251_09', 3)	# 23-25
    sprite('yu251_10', 1)	# 26-26
    sprite('yu251_10', 2)	# 27-28
    sprite('yu251_11', 3)	# 29-31
    SFX_3('yu000')
    sprite('yu251_12', 3)	# 32-34

@State
def NmlAtkAIR4B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
    sprite('yu251_00', 4)	# 1-4
    sprite('yu251_01', 3)	# 5-7
    Unknown1039(80)
    sprite('yu251_02', 2)	# 8-9
    sprite('yu251_03', 2)	# 10-11
    Unknown1019(50)
    sprite('yu251_04', 3)	# 12-14
    Unknown1019(50)
    Unknown7007('7079753330345f300000000000000000640000007079753330345f310000000000000000640000007079753330325f300000000000000000640000007079753330365f31000000000000000064000000')
    GFX_0('Sensu_Air', 0)
    Unknown23029(1, 1032, 0)
    sprite('yu251_05', 2)	# 15-16
    Unknown1019(50)
    sprite('yu251_06', 2)	# 17-18
    sprite('yu251_07', 2)	# 19-20
    sprite('yu251_08', 2)	# 21-22
    Recovery()
    Unknown2063()
    sprite('yu251_09', 3)	# 23-25
    sprite('yu251_10', 1)	# 26-26
    sprite('yu251_10', 2)	# 27-28
    sprite('yu251_11', 3)	# 29-31
    SFX_3('yu000')
    sprite('yu251_12', 3)	# 32-34

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_43():
            if (SLOT_48 == 5031):
                JumpCancel_(1)

        def upon_LANDING():
            sendToLabel(1)
    sprite('yu254_00', 3)	# 1-3
    sprite('yu254_01', 2)	# 4-5
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    GFX_1('persona_enter_ply', 0)
    sprite('yu254_02', 3)	# 6-8
    Unknown7007('7079753132345f300000000000000000640000007079753132345f310000000000000000640000007079753132345f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23029(11, 302, 0)
    sprite('yu254_03', 3)	# 9-11
    sprite('yu254_01', 3)	# 12-14
    sprite('yu254_02', 3)	# 15-17
    sprite('yu254_03', 3)	# 18-20
    sprite('yu254_01', 3)	# 21-23
    sprite('yu254_02', 3)	# 24-26
    sprite('yu254_03', 3)	# 27-29
    sprite('yu254_01', 3)	# 30-32
    sprite('yu254_02', 3)	# 33-35
    sprite('yu254_04', 3)	# 36-38
    Recovery()
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(40)
    YAccel(85)
    sprite('yu254_05', 3)	# 39-41
    sprite('yu254_06', 3)	# 42-44
    sprite('yu020_05', 3)	# 45-47
    sprite('yu020_06', 3)	# 48-50
    label(0)
    sprite('yu020_07', 4)	# 51-54
    sprite('yu020_08', 4)	# 55-58
    gotoLabel(0)
    label(1)

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('yu210_00', 2)	# 1-2
    sprite('yu210_01', 3)	# 3-5
    sprite('yu210_02', 3)	# 6-8
    sprite('yu210_03', 2)	# 9-10
    sprite('yu210_03', 2)	# 11-12
    Unknown7007('7079753130355f300000000000000000640000007079753130355f310000000000000000640000007079753130355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu210_04', 2)	# 13-14
    physicsXImpulse(15000)
    GFX_0('sensu_sakura', 0)
    sprite('yu210_04', 3)	# 15-17
    GFX_0('sensu_sakura', 0)
    sprite('yu210_05', 4)	# 18-21
    GFX_0('sensu_sakura', 0)
    sprite('yu210_06', 4)	# 22-25
    Unknown1019(80)
    GFX_0('sensu_sakura', 0)
    sprite('yu210_07', 3)	# 26-28	 **attackbox here**
    Unknown1019(80)
    GFX_0('sensu_sakura', 0)
    SFX_3('slash_rapier_middle')
    sprite('yu210_08', 1)	# 29-29	 **attackbox here**
    Unknown2003(1)
    physicsXImpulse(0)
    GFX_0('sensu_sakura', 0)
    sprite('yu210_08', 3)	# 30-32	 **attackbox here**
    sprite('yu210_09', 3)	# 33-35
    GFX_0('sensu_sakura', 0)
    sprite('yu210_10', 3)	# 36-38
    sprite('yu210_11', 4)	# 39-42
    SFX_3('yu001')
    sprite('yu210_12', 4)	# 43-46

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown23027()
        Unknown9016(1)
        Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('yu205_00', 7)	# 2-8
    sprite('yu205_01', 7)	# 9-15
    sprite('yu205_02', 2)	# 16-17
    Unknown23029(11, 501, 0)
    Unknown4020(11)
    GFX_1('persona_enter_ply', 0)
    tag_voice(1, 'pyu208_2', 'pyu302_1', '', '')
    sprite('yu205_02', 4)	# 18-21
    sprite('yu205_02', 3)	# 22-24
    sprite('yu205_03', 3)	# 25-27
    sprite('yu205_04', 2)	# 28-29
    sprite('yu205_04', 1)	# 30-30
    RefreshMultihit()
    sprite('yu205_04', 1)	# 31-31
    sprite('yu205_04', 1)	# 32-32
    sprite('yu205_02', 3)	# 33-35
    sprite('yu205_03', 3)	# 36-38
    sprite('yu205_04', 3)	# 39-41
    sprite('yu205_05', 4)	# 42-45
    sprite('yu205_06', 5)	# 46-50
    sprite('yu000_00', 6)	# 51-56
    sprite('yu000_01', 6)	# 57-62
    sprite('yu000_02', 6)	# 63-68
    sprite('yu000_03', 6)	# 69-74
    sprite('yu000_04', 6)	# 75-80
    sprite('yu000_05', 6)	# 81-86
    sprite('yu000_06', 6)	# 87-92
    sprite('yu000_07', 6)	# 93-98
    sprite('yu000_08', 6)	# 99-104
    sprite('yu000_09', 6)	# 105-110
    sprite('yu000_10', 6)	# 111-116
    sprite('yu000_11', 6)	# 117-122
    sprite('yu000_12', 6)	# 123-128
    sprite('yu000_13', 6)	# 129-134
    sprite('yu000_14', 6)	# 135-140
    sprite('yu000_15', 6)	# 141-146
    Unknown4020(0)
    label(0)
    sprite('yu000_00', 6)	# 147-152
    sprite('yu000_01', 6)	# 153-158
    sprite('yu000_02', 6)	# 159-164
    sprite('yu000_03', 6)	# 165-170
    sprite('yu000_04', 6)	# 171-176
    sprite('yu000_05', 6)	# 177-182
    sprite('yu000_06', 6)	# 183-188
    sprite('yu000_07', 6)	# 189-194
    sprite('yu000_08', 6)	# 195-200
    sprite('yu000_09', 6)	# 201-206
    sprite('yu000_10', 6)	# 207-212
    sprite('yu000_11', 6)	# 213-218
    sprite('yu000_12', 6)	# 219-224
    sprite('yu000_13', 6)	# 225-230
    sprite('yu000_14', 6)	# 231-236
    sprite('yu000_15', 6)	# 237-242
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 243-243

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        Unknown9016(1)
        Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('yu206_00', 3)	# 1-3
    sprite('yu206_01', 2)	# 4-5
    sprite('yu206_01', 3)	# 6-8
    sprite('yu206_02', 3)	# 9-11
    sprite('yu206_03', 3)	# 12-14
    Unknown23029(11, 503, 0)
    Unknown4020(11)
    GFX_1('persona_enter_ply', 0)
    sprite('yu206_04', 3)	# 15-17
    RefreshMultihit()
    sprite('yu206_05', 3)	# 18-20
    sprite('yu206_03', 3)	# 21-23
    sprite('yu206_04', 3)	# 24-26
    Recovery()
    sprite('yu206_05', 3)	# 27-29
    sprite('yu206_03', 3)	# 30-32
    sprite('yu206_04', 3)	# 33-35
    sprite('yu206_05', 3)	# 36-38
    sprite('yu206_03', 3)	# 39-41
    sprite('yu206_04', 3)	# 42-44
    sprite('yu206_06', 3)	# 45-47
    sprite('yu206_07', 3)	# 48-50
    sprite('yu206_08', 3)	# 51-53
    sprite('yu206_09', 3)	# 54-56
    sprite('yu000_00', 6)	# 57-62
    sprite('yu000_01', 6)	# 63-68
    sprite('yu000_02', 6)	# 69-74
    sprite('yu000_03', 6)	# 75-80
    sprite('yu000_04', 6)	# 81-86
    sprite('yu000_05', 6)	# 87-92
    sprite('yu000_06', 6)	# 93-98
    sprite('yu000_07', 6)	# 99-104
    sprite('yu000_08', 6)	# 105-110
    sprite('yu000_09', 6)	# 111-116
    sprite('yu000_10', 6)	# 117-122
    sprite('yu000_11', 6)	# 123-128
    sprite('yu000_12', 6)	# 129-134
    sprite('yu000_13', 6)	# 135-140
    sprite('yu000_14', 6)	# 141-146
    sprite('yu000_15', 6)	# 147-152
    Unknown4020(0)
    label(0)
    sprite('yu000_00', 6)	# 153-158
    sprite('yu000_01', 6)	# 159-164
    sprite('yu000_02', 6)	# 165-170
    sprite('yu000_03', 6)	# 171-176
    sprite('yu000_04', 6)	# 177-182
    sprite('yu000_05', 6)	# 183-188
    sprite('yu000_06', 6)	# 189-194
    sprite('yu000_07', 6)	# 195-200
    sprite('yu000_08', 6)	# 201-206
    sprite('yu000_09', 6)	# 207-212
    sprite('yu000_10', 6)	# 213-218
    sprite('yu000_11', 6)	# 219-224
    sprite('yu000_12', 6)	# 225-230
    sprite('yu000_13', 6)	# 231-236
    sprite('yu000_14', 6)	# 237-242
    sprite('yu000_15', 6)	# 243-248
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 249-249

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown2017(0)
        Unknown23027()
    sprite('yu450_00', 3)	# 1-3
    sprite('yu450_01', 2)	# 4-5
    Unknown23029(11, 502, 0)
    Unknown4020(11)
    sprite('yu450_02', 2)	# 6-7
    GFX_1('persona_enter_ply', 0)
    sprite('yu450_03', 2)	# 8-9
    sprite('yu450_04', 2)	# 10-11
    sprite('yu450_05', 2)	# 12-13
    sprite('yu450_06', 2)	# 14-15
    sprite('yu450_07', 2)	# 16-17
    tag_voice(0, 'pyu106_1', 'pyu106_0', '', '')
    sprite('yu450_08', 1)	# 18-18
    sprite('yu450_09', 1)	# 19-19
    sprite('yu450_10', 3)	# 20-22
    RefreshMultihit()
    sprite('yu450_11', 3)	# 23-25
    sprite('yu450_12', 3)	# 26-28
    sprite('yu450_13', 3)	# 29-31
    sprite('yu450_14', 3)	# 32-34
    sprite('yu450_12', 3)	# 35-37
    sprite('yu450_13', 3)	# 38-40
    sprite('yu450_14', 3)	# 41-43
    Unknown2017(1)
    sprite('yu450_12', 3)	# 44-46
    sprite('yu450_13', 3)	# 47-49
    sprite('yu450_14', 3)	# 50-52
    sprite('yu450_15', 3)	# 53-55
    sprite('yu010_02', 1)	# 56-56
    sprite('yu010_01', 2)	# 57-58
    sprite('yu010_00', 2)	# 59-60
    Unknown4020(0)

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
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('yu020_05', 3)	# 24-26
    physicsXImpulse(35000)
    physicsYImpulse(-25000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('yu020_06', 3)	# 27-29
    sprite('yu020_07', 3)	# 30-32
    sprite('yu250_00', 3)	# 33-35
    sprite('yu250_01', 3)	# 36-38
    sprite('yu250_02', 3)	# 39-41
    SFX_3('slash_rapier_fast')
    sprite('yu250_03', 3)	# 42-44	 **attackbox here**
    sprite('yu250_04', 3)	# 45-47
    sprite('yu250_05', 5)	# 48-52
    sprite('yu250_06', 5)	# 53-57
    label(2)
    sprite('yu010_01', 3)	# 58-60
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('yu010_01', 3)	# 61-63
    sprite('yu010_02', 3)	# 64-66
    sprite('yu010_03', 3)	# 67-69
    sprite('yu000_00', 6)	# 70-75
    sprite('yu000_01', 6)	# 76-81
    sprite('yu000_02', 6)	# 82-87
    sprite('yu000_03', 6)	# 88-93
    sprite('yu000_04', 6)	# 94-99
    sprite('yu000_05', 6)	# 100-105
    sprite('yu000_06', 6)	# 106-111
    sprite('yu000_07', 6)	# 112-117
    sprite('yu000_08', 6)	# 118-123
    sprite('yu000_09', 6)	# 124-129
    sprite('yu000_10', 6)	# 130-135
    sprite('yu000_11', 6)	# 136-141
    sprite('yu000_12', 6)	# 142-147
    sprite('yu000_13', 6)	# 148-153
    sprite('yu000_14', 6)	# 154-159
    sprite('yu000_15', 6)	# 160-165

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('keep', 3)	# 1-3
    sprite('yu207_00', 2)	# 4-5
    Unknown1019(150)
    sprite('yu207_01', 2)	# 6-7
    Unknown1019(150)
    sprite('yu207_02', 2)	# 8-9
    Unknown1019(50)
    sprite('yu207_03', 2)	# 10-11
    Unknown1019(50)
    sprite('yu207_05', 3)	# 12-14	 **attackbox here**
    Unknown23054('79753230375f303400000000000000000000000000000000000000000000000003000000')
    SFX_3('slash_rapier_fast')
    RefreshMultihit()
    Unknown1019(0)
    sprite('yu207_06', 3)	# 15-17
    sprite('yu207_07', 3)	# 18-20
    Unknown2001()
    sprite('yu207_08', 3)	# 21-23
    sprite('yu207_09', 3)	# 24-26
    sprite('yu207_10', 3)	# 27-29
    sprite('yu000_00', 6)	# 30-35
    sprite('yu000_01', 6)	# 36-41
    sprite('yu000_02', 6)	# 42-47
    sprite('yu000_03', 6)	# 48-53
    sprite('yu000_04', 6)	# 54-59
    sprite('yu000_05', 6)	# 60-65
    sprite('yu000_06', 6)	# 66-71
    sprite('yu000_07', 6)	# 72-77
    sprite('yu000_08', 6)	# 78-83
    sprite('yu000_09', 6)	# 84-89
    sprite('yu000_10', 6)	# 90-95
    sprite('yu000_11', 6)	# 96-101
    sprite('yu000_12', 6)	# 102-107
    sprite('yu000_13', 6)	# 108-113

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('yu450_00', 3)	# 1-3
    sprite('yu450_01', 2)	# 4-5
    Unknown23029(11, 502, 0)
    Unknown4020(11)
    sprite('yu450_02', 2)	# 6-7
    GFX_1('persona_enter_ply', 0)
    sprite('yu450_03', 2)	# 8-9
    sprite('yu450_04', 2)	# 10-11
    sprite('yu450_05', 2)	# 12-13
    sprite('yu450_06', 2)	# 14-15
    sprite('yu450_07', 2)	# 16-17
    sprite('yu450_08', 1)	# 18-18
    sprite('yu450_09', 1)	# 19-19
    sprite('yu450_10', 3)	# 20-22
    sprite('yu450_11', 3)	# 23-25
    sprite('yu450_12', 3)	# 26-28
    sprite('yu450_13', 3)	# 29-31
    sprite('yu450_14', 3)	# 32-34
    sprite('yu450_12', 3)	# 35-37
    sprite('yu450_13', 3)	# 38-40
    sprite('yu450_14', 3)	# 41-43
    sprite('yu450_12', 3)	# 44-46
    sprite('yu450_13', 3)	# 47-49
    sprite('yu450_14', 3)	# 50-52
    sprite('yu450_15', 3)	# 53-55
    sprite('yu010_02', 1)	# 56-56
    sprite('yu010_01', 2)	# 57-58
    sprite('yu010_00', 2)	# 59-60
    Unknown4020(0)

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(16000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('yu030_00', 3)	# 1-3
    sprite('yu032_00', 2)	# 4-5
    label(0)
    sprite('yu032_01', 4)	# 6-9
    sprite('yu032_02', 4)	# 10-13
    sprite('yu032_03', 4)	# 14-17
    Unknown8006(100, 1, 1)
    sprite('yu032_04', 4)	# 18-21
    sprite('yu032_05', 4)	# 22-25
    sprite('yu032_06', 4)	# 26-29
    sprite('yu032_07', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('yu032_08', 4)	# 34-37
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yu310_00', 1)	# 38-38
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    SFX_3('yu001')
    sprite('yu310_01', 2)	# 39-40
    sprite('yu310_02', 3)	# 41-43	 **attackbox here**
    Unknown1084(1)
    sprite('yu310_03', 3)	# 44-46
    sprite('yu310_04', 5)	# 47-51
    SFX_4('pyu154')
    sprite('yu310_05', 9)	# 52-60
    sprite('yu310_06', 3)	# 61-63
    SFX_3('yu000')
    sprite('yu310_07', 3)	# 64-66

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        Unknown9154(25)
        Unknown9130(16)
        Unknown9142(100)
        PushbackX(20000)
        Hitstop(7)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown2004(1, 0)
    sprite('yu310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    Unknown2018(1, 80)
    StartMultihit()
    SFX_3('grip_fast')
    sprite('yu311_00', 4)	# 5-8
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('yu311_01', 6)	# 9-14
    sprite('yu311_02', 3)	# 15-17
    Unknown2018(0, 80)
    SFX_3('hit_l_fast')
    sprite('yu311_03', 3)	# 18-20	 **attackbox here**
    Unknown2018(1, 80)
    RefreshMultihit()
    SFX_3('slap_large')
    SFX_4('pyu153')
    sprite('yu311_04', 12)	# 21-32
    sprite('yu311_05', 3)	# 33-35
    sprite('yu311_06', 6)	# 36-41
    sprite('yu311_07', 5)	# 42-46
    SFX_3('yu000')

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(16000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('yu030_00', 3)	# 1-3
    sprite('yu032_00', 2)	# 4-5
    label(0)
    sprite('yu032_01', 4)	# 6-9
    sprite('yu032_02', 4)	# 10-13
    sprite('yu032_03', 4)	# 14-17
    Unknown8006(100, 1, 1)
    sprite('yu032_04', 4)	# 18-21
    sprite('yu032_05', 4)	# 22-25
    sprite('yu032_06', 4)	# 26-29
    sprite('yu032_07', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('yu032_08', 4)	# 34-37
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yu310_00', 1)	# 38-38
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    SFX_3('yu001')
    sprite('yu310_01', 2)	# 39-40
    sprite('yu310_02', 3)	# 41-43	 **attackbox here**
    Unknown1084(1)
    sprite('yu310_03', 3)	# 44-46
    sprite('yu310_04', 5)	# 47-51
    SFX_4('pyu154')
    sprite('yu310_05', 9)	# 52-60
    sprite('yu310_06', 3)	# 61-63
    SFX_3('yu000')
    sprite('yu310_07', 3)	# 64-66

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        Unknown9154(25)
        Unknown9130(16)
        Unknown9142(100)
        PushbackX(20000)
        Hitstop(7)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
    sprite('yu310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    Unknown2018(1, 80)
    StartMultihit()
    SFX_3('grip_fast')
    sprite('yu311_00ex', 4)	# 5-8
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('yu311_01', 6)	# 9-14
    Unknown2005()
    sprite('yu311_02', 3)	# 15-17
    Unknown2018(0, 80)
    SFX_3('hit_l_fast')
    sprite('yu311_03', 3)	# 18-20	 **attackbox here**
    Unknown2018(1, 80)
    RefreshMultihit()
    SFX_3('slap_large')
    SFX_4('pyu153')
    sprite('yu311_04', 12)	# 21-32
    sprite('yu311_05', 3)	# 33-35
    sprite('yu311_06', 6)	# 36-41
    sprite('yu311_07', 5)	# 42-46
    SFX_3('yu000')

@State
def AgiA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
        Unknown21015('41676973686f7441000000000000000000000000000000000000000000000000cb0f000000000000')
    sprite('yu401_00', 2)	# 1-2
    sprite('yu401_01', 1)	# 3-3
    sprite('yu401_01', 1)	# 4-4
    sprite('yu401_02', 2)	# 5-6
    sprite('yu401_03', 1)	# 7-7
    Unknown23029(11, 4020, 0)
    sprite('yu401_03', 1)	# 8-8
    sprite('yu401_04', 3)	# 9-11
    GFX_1('persona_enter_ply', 0)
    Unknown7007('7079753230315f300000000000000000640000007079753230315f310000000000000000640000007079753230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu401_05', 3)	# 12-14
    sprite('yu401_06', 3)	# 15-17
    sprite('yu401_05', 3)	# 18-20
    sprite('yu401_04', 3)	# 21-23
    sprite('yu401_05', 3)	# 24-26
    sprite('yu401_06', 3)	# 27-29
    sprite('yu401_05', 3)	# 30-32
    sprite('yu401_04', 3)	# 33-35
    sprite('yu401_05', 3)	# 36-38
    sprite('yu401_03', 4)	# 39-42
    Recovery()
    sprite('yu401_02', 4)	# 43-46
    sprite('yu401_01', 4)	# 47-50
    sprite('yu401_00', 4)	# 51-54

@State
def AgiB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
        Unknown21015('41676973686f7442000000000000000000000000000000000000000000000000cc0f000000000000')
    sprite('yu401_00', 2)	# 1-2
    sprite('yu401_01', 1)	# 3-3
    sprite('yu401_01', 1)	# 4-4
    sprite('yu401_02', 2)	# 5-6
    sprite('yu401_03', 1)	# 7-7
    Unknown23029(11, 4030, 0)
    sprite('yu401_03', 1)	# 8-8
    sprite('yu401_04', 3)	# 9-11
    GFX_1('persona_enter_ply', 0)
    Unknown7007('7079753230315f300000000000000000640000007079753230315f310000000000000000640000007079753230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu401_05', 3)	# 12-14
    sprite('yu401_06', 3)	# 15-17
    sprite('yu401_05', 3)	# 18-20
    sprite('yu401_04', 3)	# 21-23
    sprite('yu401_05', 3)	# 24-26
    sprite('yu401_06', 3)	# 27-29
    sprite('yu401_05', 3)	# 30-32
    sprite('yu401_04', 3)	# 33-35
    sprite('yu401_05', 3)	# 36-38
    sprite('yu401_03', 4)	# 39-42
    Recovery()
    sprite('yu401_02', 4)	# 43-46
    sprite('yu401_01', 4)	# 47-50
    sprite('yu401_00', 4)	# 51-54

@State
def AgiEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
        Unknown21015('41676973686f7441420000000000000000000000000000000000000000000000cd0f000000000000')
    sprite('yu401_00', 3)	# 1-3
    sprite('yu401_01', 1)	# 4-4
    sprite('yu401_01', 2)	# 5-6
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('7079753230335f300000000000000000640000007079753230335f310000000000000000640000007079753230335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu401_02', 2)	# 7-8
    sprite('yu401_03', 1)	# 9-9
    sprite('yu401_03', 1)	# 10-10
    Unknown23029(11, 4040, 0)
    sprite('yu401_04', 3)	# 11-13
    GFX_1('persona_enter_ply', 0)
    sprite('yu401_05', 3)	# 14-16
    sprite('yu401_06', 3)	# 17-19
    sprite('yu401_04', 3)	# 20-22
    sprite('yu401_05', 3)	# 23-25
    sprite('yu401_06', 3)	# 26-28
    sprite('yu401_04', 3)	# 29-31
    sprite('yu401_05', 3)	# 32-34
    sprite('yu401_06', 3)	# 35-37
    sprite('yu401_05', 3)	# 38-40
    sprite('yu401_04', 3)	# 41-43
    Recovery()
    sprite('yu401_02', 3)	# 44-46
    sprite('yu401_01', 3)	# 47-49
    sprite('yu401_00', 2)	# 50-51

@State
def AgiAirA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown21015('41676973686f7441000000000000000000000000000000000000000000000000cb0f000000000000')
    sprite('yu255_00', 3)	# 1-3
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('yu255_01', 1)	# 4-4
    sprite('yu255_01', 2)	# 5-6
    Unknown22004(6, 6)
    sprite('yu255_02', 1)	# 7-7
    Unknown23029(11, 5032, 0)
    sprite('yu255_02', 2)	# 8-9
    sprite('yu255_03', 3)	# 10-12
    GFX_1('persona_enter_ply', 0)
    Unknown7007('7079753230325f300000000000000000640000007079753230325f310000000000000000640000007079753230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu255_04', 1)	# 13-13
    sprite('yu255_04', 2)	# 14-15
    sprite('yu255_05', 3)	# 16-18
    sprite('yu255_03', 4)	# 19-22
    sprite('yu255_04', 4)	# 23-26
    sprite('yu255_05', 4)	# 27-30
    sprite('yu255_03', 4)	# 31-34
    sprite('yu255_04', 4)	# 35-38
    sprite('yu255_05', 4)	# 39-42
    sprite('yu255_06', 4)	# 43-46
    Unknown1018()
    Unknown1038()
    Unknown1019(85)
    setGravity(2400)
    Recovery()
    sprite('yu255_07', 4)	# 47-50
    sprite('yu255_08', 4)	# 51-54

@State
def AgiAirB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown21015('41676973686f7442000000000000000000000000000000000000000000000000cc0f000000000000')
    sprite('yu255_00', 3)	# 1-3
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('yu255_01', 1)	# 4-4
    sprite('yu255_01', 2)	# 5-6
    Unknown22004(6, 6)
    sprite('yu255_02', 1)	# 7-7
    Unknown23029(11, 5033, 0)
    sprite('yu255_02', 2)	# 8-9
    sprite('yu255_03', 3)	# 10-12
    GFX_1('persona_enter_ply', 0)
    Unknown7007('7079753230325f300000000000000000640000007079753230325f310000000000000000640000007079753230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu255_04', 3)	# 13-15
    sprite('yu255_05', 3)	# 16-18
    sprite('yu255_03', 4)	# 19-22
    sprite('yu255_04', 4)	# 23-26
    sprite('yu255_05', 4)	# 27-30
    sprite('yu255_03', 4)	# 31-34
    sprite('yu255_04', 4)	# 35-38
    sprite('yu255_05', 4)	# 39-42
    sprite('yu255_06', 4)	# 43-46
    Unknown1018()
    Unknown1038()
    Unknown1019(85)
    setGravity(2400)
    Recovery()
    sprite('yu255_07', 4)	# 47-50
    sprite('yu255_08', 4)	# 51-54

@State
def AgiAirEX():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown21015('41676973686f7441420000000000000000000000000000000000000000000000cd0f000000000000')
    sprite('yu255_00', 2)	# 1-2
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('yu255_01', 1)	# 3-3
    sprite('yu255_01', 1)	# 4-4
    Unknown22004(6, 6)
    sprite('yu255_02', 3)	# 5-7
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('7079753230335f300000000000000000640000007079753230335f310000000000000000640000007079753230335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu255_03', 1)	# 8-8
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 5034, 0)
    sprite('yu255_03', 3)	# 9-11
    sprite('yu255_04', 4)	# 12-15
    sprite('yu255_05', 4)	# 16-19
    sprite('yu255_03', 4)	# 20-23
    sprite('yu255_04', 4)	# 24-27
    sprite('yu255_05', 4)	# 28-31
    sprite('yu255_03', 4)	# 32-35
    sprite('yu255_04', 4)	# 36-39
    Unknown1018()
    Unknown1038()
    Unknown1019(85)
    setGravity(2400)
    sprite('yu255_05', 4)	# 40-43
    sprite('yu255_06', 4)	# 44-47
    Recovery()
    sprite('yu255_07', 4)	# 48-51
    sprite('yu255_08', 4)	# 52-55

@State
def MaharagiA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
    sprite('yu402_00', 3)	# 1-3
    sprite('yu402_01', 3)	# 4-6
    sprite('yu402_02', 3)	# 7-9
    sprite('yu402_03', 3)	# 10-12
    sprite('yu402_04', 3)	# 13-15
    GFX_1('persona_enter_ply', 0)
    sprite('yu402_05', 4)	# 16-19
    Unknown23029(11, 4060, 0)
    Unknown7007('7079753230355f300000000000000000640000007079753230355f310000000000000000640000007079753230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu402_06', 4)	# 20-23
    sprite('yu402_07', 4)	# 24-27
    sprite('yu402_05', 4)	# 28-31
    sprite('yu402_06', 4)	# 32-35
    sprite('yu402_07', 4)	# 36-39
    sprite('yu402_05', 4)	# 40-43
    sprite('yu402_06', 4)	# 44-47
    sprite('yu402_07', 4)	# 48-51
    sprite('yu402_05', 4)	# 52-55
    sprite('yu402_08', 4)	# 56-59

@State
def MaharagiB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
    sprite('yu402_00', 3)	# 1-3
    sprite('yu402_01', 3)	# 4-6
    sprite('yu402_02', 3)	# 7-9
    sprite('yu402_03', 3)	# 10-12
    sprite('yu402_04', 3)	# 13-15
    GFX_1('persona_enter_ply', 0)
    sprite('yu402_05', 4)	# 16-19
    Unknown7007('7079753230345f300000000000000000640000007079753230345f310000000000000000640000007079753230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu402_06', 4)	# 20-23
    sprite('yu402_07', 4)	# 24-27
    sprite('yu402_05', 4)	# 28-31
    Unknown23029(11, 4050, 0)
    sprite('yu402_06', 4)	# 32-35
    sprite('yu402_07', 4)	# 36-39
    sprite('yu402_05', 4)	# 40-43
    sprite('yu402_06', 4)	# 44-47
    sprite('yu402_07', 4)	# 48-51
    sprite('yu402_05', 4)	# 52-55
    sprite('yu402_08', 4)	# 56-59

@State
def MaharagiEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
    sprite('yu402_00', 3)	# 1-3
    sprite('yu402_01', 1)	# 4-4
    sprite('yu402_01', 3)	# 5-7
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('7079753230365f300000000000000000640000007079753230365f310000000000000000640000007079753230365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu402_02', 3)	# 8-10
    sprite('yu402_03', 3)	# 11-13
    sprite('yu402_04', 4)	# 14-17
    GFX_1('persona_enter_ply', 0)
    sprite('yu402_05', 4)	# 18-21
    Unknown23029(11, 4071, 0)
    sprite('yu402_06', 4)	# 22-25
    sprite('yu402_07', 4)	# 26-29
    sprite('yu402_05', 4)	# 30-33
    sprite('yu402_06', 4)	# 34-37
    sprite('yu402_07', 4)	# 38-41
    sprite('yu402_05', 4)	# 42-45
    sprite('yu402_06', 4)	# 46-49
    sprite('yu402_08', 3)	# 50-52
    Recovery()

@State
def FireBoosterA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('yu403_00', 3)	# 1-3
    sprite('yu403_07', 3)	# 4-6
    Unknown7007('7079753230375f300000000000000000640000007079753230375f310000000000000000640000007079753230375f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23029(11, 4080, 0)
    sprite('yu403_08', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    GFX_0('fire_booster', 100)
    sprite('yu403_09', 3)	# 10-12
    sprite('yu403_10', 3)	# 13-15
    sprite('yu403_08', 3)	# 16-18
    sprite('yu403_09', 3)	# 19-21
    if (SLOT_31 < 9):
        selfDamage(500)
        SLOT_31 = (SLOT_31 + 1)
    SFX_3('distortion_b')
    Recovery()
    sprite('yu403_10', 3)	# 22-24
    sprite('yu403_08', 3)	# 25-27
    sprite('yu403_09', 3)	# 28-30
    sprite('yu403_11', 3)	# 31-33
    sprite('yu403_12', 3)	# 34-36

@State
def FireBoosterB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('yu403_00', 3)	# 1-3
    sprite('yu403_01', 3)	# 4-6
    sprite('yu403_02', 3)	# 7-9
    sprite('yu403_03', 3)	# 10-12
    sprite('yu403_04', 3)	# 13-15
    sprite('yu403_05', 3)	# 16-18
    Unknown7007('7079753230385f300000000000000000640000007079753230385f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu403_06', 3)	# 19-21
    sprite('yu403_07', 3)	# 22-24
    Unknown23029(11, 4080, 0)
    sprite('yu403_08', 3)	# 25-27
    GFX_1('persona_enter_ply', 0)
    GFX_0('fire_booster', 100)
    sprite('yu403_09', 3)	# 28-30
    sprite('yu403_10', 3)	# 31-33
    if (SLOT_31 < 9):
        selfDamage(500)
        SLOT_31 = (SLOT_31 + 1)
    SFX_3('distortion_b')
    sprite('yu403_08', 3)	# 34-36
    sprite('yu403_09', 3)	# 37-39
    sprite('yu403_10', 3)	# 40-42
    if (SLOT_31 < 9):
        SLOT_31 = (SLOT_31 + 1)
    SFX_3('distortion_b')
    Recovery()
    sprite('yu403_08', 3)	# 43-45
    sprite('yu403_09', 3)	# 46-48
    sprite('yu403_10', 3)	# 49-51
    sprite('yu403_11', 3)	# 52-54
    sprite('yu403_12', 3)	# 55-57

@State
def FireBoosterC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        GuardPoint_(1)
    sprite('yu403_00', 3)	# 1-3
    sprite('yu403_07', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    setInvincible(1)
    Unknown22022(0)
    Unknown22038(0)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown7007('7079753230395f300000000000000000640000007079753230395f310000000000000000640000007079753230395f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23029(11, 4080, 0)
    sprite('yu403_08', 2)	# 6-7
    GFX_1('persona_enter_ply', 0)
    GFX_0('fire_booster', 100)
    sprite('yu403_09', 2)	# 8-9
    sprite('yu403_10', 2)	# 10-11
    sprite('yu403_08', 2)	# 12-13
    if (SLOT_31 < 9):
        selfDamage(500)
        SLOT_31 = (SLOT_31 + 2)
    SFX_3('distortion_b')
    Recovery()
    sprite('yu403_11', 4)	# 14-17
    sprite('yu403_12', 5)	# 18-22

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        sendToLabelUpon(2, 1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(20000)
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(60)
        Damage(1200)
        Unknown9021(1)
        GuardPoint_(1)
    sprite('yu400_01', 3)	# 1-3
    Unknown7007('7079753230305f300000000000000000640000007079753230305f310000000000000000640000007079753230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('yu400_02', 3)	# 4-6
    sprite('yu400_03', 3)	# 7-9
    sprite('yu400_04', 3)	# 10-12
    GFX_0('rinkakuaura', 100)
    Unknown38(5, 1)
    Unknown23029(11, 4010, 0)
    GFX_0('rinkakuaura2', 100)
    sprite('yu400_05', 3)	# 13-15
    sprite('yu400_06', 3)	# 16-18
    Unknown1084(1)
    physicsYImpulse(2000)
    sprite('yu400_07', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    sprite('yu400_08', 3)	# 22-24	 **attackbox here**
    GFX_0('diacharge', 104)
    Unknown38(6, 1)
    GFX_0('diacharge_floor', 0)
    Unknown38(7, 1)

    def upon_3():
        Unknown21000(60)
    sprite('yu400_09', 3)	# 25-27	 **attackbox here**
    sprite('yu400_10', 3)	# 28-30	 **attackbox here**
    Unknown23027()
    SFX_3('yu004')
    Unknown22022(0)
    Unknown22038(0)
    Unknown22019('0000000000000000000000000100000000000000')
    physicsYImpulse(-600)
    sprite('yu400_07', 3)	# 31-33	 **attackbox here**
    sprite('yu400_08', 3)	# 34-36	 **attackbox here**
    sprite('yu400_09', 3)	# 37-39	 **attackbox here**
    label(2)
    sprite('yu400_07', 3)	# 40-42	 **attackbox here**
    Unknown11063(1)

    def upon_3():
        if (not CheckInput(0x1)):
            if (not CheckInput(0x1c)):
                clearUponHandler(3)
                sendToLabel(0)
        Unknown47('090000000200000033000000000000003c0000000200000034000000')
        if 
        if SLOT_52:
            SFX_3('yu004')
            SLOT_51 = 0:
            Unknown21000(30)
            SLOT_51 = (SLOT_51 + 1)
        else:
            clearUponHandler(3)
            sendToLabel(0)
    SFX_3('yu002')
    YAccel(-100)
    sprite('yu400_08', 3)	# 43-45	 **attackbox here**
    sprite('yu400_09', 3)	# 46-48	 **attackbox here**
    sprite('yu400_10', 3)	# 49-51	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(0)
    sprite('yu400_07', 3)	# 52-54	 **attackbox here**
    setGravity(350)
    setInvincible(0)
    Unknown23029(5, 52, 0)
    Unknown23029(6, 53, 0)
    Unknown23029(7, 54, 0)
    Unknown23029(11, 11, 0)
    sprite('yu400_08', 3)	# 55-57	 **attackbox here**
    sprite('yu400_09', 3)	# 58-60	 **attackbox here**
    sprite('yu400_10', 3)	# 61-63	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('yu400_11', 4)	# 64-67
    sprite('yu400_12', 4)	# 68-71
    sprite('yu400_13', 4)	# 72-75

@State
def UltimateAgidine():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown2021(1)
        Unknown2006()
        Unknown23055('')
    sprite('yu430_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('yu430_00', 3)	# 4-6
    Unknown2036(78, -1, 0)
    Unknown2058(-10000)
    Unknown7007('7079753235305f300000000000000000640000007079753235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30080('')
    sprite('yu430_01', 4)	# 7-10
    sprite('yu430_02', 4)	# 11-14
    sprite('yu430_03', 4)	# 15-18
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(5, 1)
    sprite('yu430_04', 4)	# 19-22
    sprite('yu430_05', 4)	# 23-26
    sprite('yu430_06', 4)	# 27-30
    sprite('yu430_07', 4)	# 31-34
    sprite('yu430_08', 4)	# 35-38
    sprite('yu430_09', 4)	# 39-42
    sprite('yu430_10', 4)	# 43-46
    sprite('yu430_11', 4)	# 47-50
    sprite('yu430_12', 3)	# 51-53
    sprite('yu430_13', 3)	# 54-56
    sprite('yu430_14', 3)	# 57-59
    sprite('yu430_15', 3)	# 60-62
    sprite('yu430_16', 3)	# 63-65
    sprite('yu430_17', 3)	# 66-68
    sprite('yu430_18', 4)	# 69-72
    Unknown21007(5, 32)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('yu430_19', 4)	# 73-76
    Unknown23029(11, 10010, 0)
    sprite('yu430_20', 4)	# 77-80
    sprite('yu430_21', 4)	# 81-84
    label(0)
    sprite('yu430_19', 4)	# 85-88
    sprite('yu430_20', 4)	# 89-92
    if (SLOT_51 >= 1):
        setInvincible(0)
    if (SLOT_2 >= 7):
        sendToLabel(1)
    sprite('yu430_21', 4)	# 93-96
    Unknown2038(1)
    SLOT_51 = (SLOT_51 + 1)
    gotoLabel(0)
    label(1)
    sprite('yu430_19', 4)	# 97-100
    Unknown7007('7079753235315f300000000000000000640000007079753235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu430_20', 4)	# 101-104
    sprite('yu430_21', 4)	# 105-108
    sprite('yu430_19', 5)	# 109-113
    sprite('yu430_20', 5)	# 114-118
    sprite('yu430_21', 5)	# 119-123
    sprite('yu430_19', 5)	# 124-128
    sprite('yu430_20', 5)	# 129-133
    sprite('yu430_21', 5)	# 134-138
    sprite('yu430_19', 5)	# 139-143
    sprite('yu430_20', 5)	# 144-148
    sprite('yu430_21', 5)	# 149-153
    sprite('yu430_22', 4)	# 154-157
    sprite('yu430_23', 4)	# 158-161
    Recovery()

@State
def UltimateMaharagidine():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown2006()
        Unknown23055('')

        def upon_43():
            if (SLOT_48 == 10055):
                Unknown23159('UltimateMaharagidine_Front')
                SLOT_51 = 1

        def upon_3():
            if SLOT_51:
                sendToLabel(0)
    sprite('yu431_00', 4)	# 1-4
    Unknown1084(1)
    setInvincible(1)
    sprite('yu431_01', 4)	# 5-8
    sprite('yu431_02', 1)	# 9-9
    sprite('yu431_02', 4)	# 10-13
    Unknown2036(77, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(5, 1)
    Unknown36(1)
    physicsYImpulse(-2200)
    Unknown4007(2)
    Unknown35()
    sprite('yu431_03', 5)	# 14-18
    sprite('yu431_04', 5)	# 19-23
    Unknown7007('7079753235325f300000000000000000640000007079753235325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu431_02', 5)	# 24-28
    sprite('yu431_03', 5)	# 29-33
    Unknown23024(1)
    sprite('yu431_04', 5)	# 34-38
    sprite('yu431_05', 4)	# 39-42
    sprite('yu431_06', 4)	# 43-46
    sprite('yu431_07', 4)	# 47-50
    sprite('yu431_08', 4)	# 51-54
    Unknown21007(5, 32)
    Unknown23029(11, 10030, 0)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('yu431_09', 4)	# 55-58
    sprite('yu431_10', 4)	# 59-62
    sprite('yu431_08', 4)	# 63-66
    sprite('yu431_09', 4)	# 67-70
    sprite('yu431_10', 4)	# 71-74
    sprite('yu431_08', 4)	# 75-78
    Unknown7007('7079753235335f300000000000000000640000007079753235335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu431_09', 4)	# 79-82
    sprite('yu431_10', 4)	# 83-86
    sprite('yu431_08', 4)	# 87-90
    sprite('yu431_09', 4)	# 91-94
    sprite('yu431_10', 4)	# 95-98
    sprite('yu431_08', 4)	# 99-102
    sprite('yu431_09', 4)	# 103-106
    sprite('yu431_10', 4)	# 107-110
    setInvincible(0)
    sprite('yu431_08', 4)	# 111-114
    sprite('yu431_09', 4)	# 115-118
    sprite('yu431_10', 4)	# 119-122
    sprite('yu431_08', 4)	# 123-126
    sprite('yu431_09', 4)	# 127-130
    sprite('yu431_10', 4)	# 131-134
    sprite('yu431_08', 4)	# 135-138
    sprite('yu431_09', 4)	# 139-142
    label(0)
    sprite('yu431_10', 4)	# 143-146
    clearUponHandler(3)
    clearUponHandler(43)
    sprite('yu431_08', 4)	# 147-150
    sprite('yu431_09', 4)	# 151-154
    setInvincible(0)
    sprite('yu431_10', 4)	# 155-158
    sprite('yu431_08', 4)	# 159-162
    sprite('yu431_09', 4)	# 163-166
    sprite('yu431_10', 4)	# 167-170
    sprite('yu431_08', 4)	# 171-174
    sprite('yu431_09', 4)	# 175-178
    sprite('yu431_10', 4)	# 179-182
    sprite('yu431_08', 4)	# 183-186
    sprite('yu431_09', 4)	# 187-190
    sprite('yu431_10', 4)	# 191-194
    sprite('yu431_08', 4)	# 195-198
    sprite('yu431_11', 5)	# 199-203
    sprite('yu431_12', 6)	# 204-209
    sprite('yu431_13', 6)	# 210-215

@State
def UltimateAgidine_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown2021(1)
        Unknown23055('')
        Unknown2006()
    sprite('yu430_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('yu430_00', 3)	# 4-6
    Unknown2036(78, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    Unknown7007('7079753235305f300000000000000000640000007079753235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_1('yu310')
    sprite('yu430_01', 4)	# 7-10
    sprite('yu430_02', 4)	# 11-14
    sprite('yu430_03', 4)	# 15-18
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(5, 1)
    sprite('yu430_04', 4)	# 19-22
    sprite('yu430_05', 4)	# 23-26
    sprite('yu430_06', 4)	# 27-30
    sprite('yu430_07', 4)	# 31-34
    sprite('yu430_08', 4)	# 35-38
    sprite('yu430_09', 4)	# 39-42
    sprite('yu430_10', 4)	# 43-46
    sprite('yu430_11', 4)	# 47-50
    sprite('yu430_12', 3)	# 51-53
    sprite('yu430_13', 3)	# 54-56
    sprite('yu430_14', 3)	# 57-59
    sprite('yu430_15', 3)	# 60-62
    sprite('yu430_16', 3)	# 63-65
    sprite('yu430_17', 3)	# 66-68
    sprite('yu430_18', 4)	# 69-72
    Unknown21007(5, 32)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('yu430_19', 4)	# 73-76
    Unknown23029(11, 10020, 0)
    sprite('yu430_20', 4)	# 77-80
    sprite('yu430_21', 4)	# 81-84
    sprite('yu430_19', 4)	# 85-88
    sprite('yu430_20', 4)	# 89-92
    sprite('yu430_21', 4)	# 93-96
    label(0)
    sprite('yu430_19', 4)	# 97-100
    if (SLOT_2 >= 7):
        sendToLabel(1)
    sprite('yu430_20', 4)	# 101-104
    setInvincible(0)
    sprite('yu430_21', 4)	# 105-108
    Unknown2038(1)
    SLOT_51 = (SLOT_51 + 1)
    gotoLabel(0)
    label(1)
    sprite('yu430_19', 4)	# 109-112
    Unknown7007('7079753235315f300000000000000000640000007079753235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu430_20', 4)	# 113-116
    sprite('yu430_21', 4)	# 117-120
    sprite('yu430_19', 5)	# 121-125
    sprite('yu430_20', 5)	# 126-130
    sprite('yu430_21', 5)	# 131-135
    sprite('yu430_19', 5)	# 136-140
    sprite('yu430_20', 5)	# 141-145
    sprite('yu430_21', 5)	# 146-150
    sprite('yu430_19', 5)	# 151-155
    sprite('yu430_20', 5)	# 156-160
    sprite('yu430_21', 5)	# 161-165
    sprite('yu430_22', 4)	# 166-169
    sprite('yu430_23', 4)	# 170-173
    Recovery()

@State
def UltimateMaharagidineOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown2006()

        def upon_43():
            if (SLOT_48 == 10055):
                Unknown23159('UltimateMaharagidineOD_Front')
                SLOT_51 = 1

        def upon_3():
            if SLOT_51:
                sendToLabel(0)
    sprite('yu431_00', 4)	# 1-4
    Unknown1084(1)
    setInvincible(1)
    sprite('yu431_01', 4)	# 5-8
    sprite('yu431_02', 1)	# 9-9
    sprite('yu431_02', 4)	# 10-13
    Unknown2036(77, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(5, 1)
    Unknown36(1)
    physicsYImpulse(-2200)
    Unknown35()
    sprite('yu431_03', 5)	# 14-18
    sprite('yu431_04', 5)	# 19-23
    Unknown7007('7079753235325f300000000000000000640000007079753235325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu431_02', 5)	# 24-28
    sprite('yu431_03', 5)	# 29-33
    Unknown23024(1)
    sprite('yu431_04', 5)	# 34-38
    sprite('yu431_05', 4)	# 39-42
    sprite('yu431_06', 4)	# 43-46
    sprite('yu431_07', 4)	# 47-50
    sprite('yu431_08', 4)	# 51-54
    Unknown21007(5, 32)
    Unknown23029(11, 10053, 0)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    SFX_1('yu312')
    sprite('yu431_09', 4)	# 55-58
    sprite('yu431_10', 4)	# 59-62
    sprite('yu431_08', 4)	# 63-66
    sprite('yu431_09', 4)	# 67-70
    sprite('yu431_10', 4)	# 71-74
    sprite('yu431_08', 4)	# 75-78
    Unknown7007('7079753235335f300000000000000000640000007079753235335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('yu431_09', 4)	# 79-82
    sprite('yu431_10', 4)	# 83-86
    sprite('yu431_08', 4)	# 87-90
    sprite('yu431_09', 4)	# 91-94
    sprite('yu431_10', 4)	# 95-98
    sprite('yu431_08', 4)	# 99-102
    sprite('yu431_09', 4)	# 103-106
    sprite('yu431_10', 4)	# 107-110
    setInvincible(0)
    sprite('yu431_08', 4)	# 111-114
    sprite('yu431_09', 4)	# 115-118
    sprite('yu431_10', 4)	# 119-122
    sprite('yu431_08', 4)	# 123-126
    sprite('yu431_09', 4)	# 127-130
    sprite('yu431_10', 4)	# 131-134
    sprite('yu431_08', 4)	# 135-138
    sprite('yu431_09', 4)	# 139-142
    label(0)
    sprite('yu431_10', 4)	# 143-146
    clearUponHandler(3)
    clearUponHandler(43)
    sprite('yu431_08', 4)	# 147-150
    sprite('yu431_09', 4)	# 151-154
    setInvincible(0)
    sprite('yu431_10', 4)	# 155-158
    sprite('yu431_08', 4)	# 159-162
    sprite('yu431_09', 4)	# 163-166
    sprite('yu431_10', 4)	# 167-170
    sprite('yu431_08', 4)	# 171-174
    sprite('yu431_09', 4)	# 175-178
    sprite('yu431_10', 4)	# 179-182
    sprite('yu431_08', 4)	# 183-186
    sprite('yu431_09', 4)	# 187-190
    sprite('yu431_10', 4)	# 191-194
    sprite('yu431_08', 4)	# 195-198
    sprite('yu431_11', 5)	# 199-203
    sprite('yu431_12', 6)	# 204-209
    sprite('yu431_13', 6)	# 210-215

@State
def Ichigeki():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Hitstop(0)
        Damage(100000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        Unknown11064(3)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown23083(1)

        def upon_32():
            SLOT_51 = 1
            setInvincible(1)
            Unknown23083(1)
            Unknown2017(0)
            Unknown23084(1)
            Unknown23157(1)
            Unknown23088(1, 1)

            def upon_3():
                Unknown48('19000000020000003400000016000000020000000c000000')
                if (SLOT_52 > 0):
                    clearUponHandler(3)
                    Unknown23024(3)
                sendToLabel(2)

        def upon_STATE_END():
            Unknown20000(0)
            setInvincible(0)
    sprite('yu450_00', 3)	# 1-3
    setInvincible(1)
    sprite('yu450_01', 3)	# 4-6
    sprite('yu450_02', 3)	# 7-9
    sprite('yu450_03', 3)	# 10-12
    sprite('yu450_04', 3)	# 13-15
    Unknown2036(86, -1, 2)
    Unknown23147()
    GFX_0('P4U_Cutin_Parent', 100)
    tag_voice(1, 'pyu290_0', 'pyu290_1', '', '')
    sprite('yu450_05', 3)	# 16-18
    sprite('yu450_06', 3)	# 19-21
    sprite('yu450_07', 3)	# 22-24
    sprite('yu450_08', 3)	# 25-27
    sprite('yu450_09', 3)	# 28-30
    sprite('yu450_10', 3)	# 31-33
    Unknown23029(11, 10070, 0)
    Unknown18009(1)
    sprite('yu450_11', 4)	# 34-37
    sprite('yu450_12', 4)	# 38-41
    sprite('yu450_13', 4)	# 42-45
    sprite('yu450_14', 4)	# 46-49
    sprite('yu450_12', 4)	# 50-53
    sprite('yu450_13', 4)	# 54-57
    sprite('yu450_14', 4)	# 58-61
    sprite('yu450_12', 4)	# 62-65
    sprite('yu450_13', 4)	# 66-69
    sprite('yu450_14', 4)	# 70-73
    sprite('yu450_12', 4)	# 74-77
    sprite('yu450_13', 4)	# 78-81
    sprite('yu450_14', 4)	# 82-85
    sprite('yu450_12', 4)	# 86-89
    sprite('yu450_13', 4)	# 90-93
    sprite('yu450_14', 4)	# 94-97
    sprite('yu450_12', 4)	# 98-101
    sprite('yu450_13', 4)	# 102-105
    sprite('yu450_14', 4)	# 106-109
    sprite('yu450_12', 4)	# 110-113
    sprite('yu450_13', 4)	# 114-117
    sprite('yu450_14', 4)	# 118-121
    sprite('yu450_12', 4)	# 122-125
    loopRest()
    Unknown19(0, 2, 51)
    label(1)
    sprite('yu450_12', 4)	# 126-129
    sprite('yu450_13', 4)	# 130-133
    sprite('yu450_14', 4)	# 134-137
    gotoLabel(1)
    label(2)
    sprite('yu450_12', 3)	# 138-140
    sprite('yu450_13', 3)	# 141-143
    sprite('yu450_14', 120)	# 144-263
    sprite('yu450_14', 20)	# 264-283
    Unknown36(22)
    Unknown3004(-30)
    Unknown35()
    Unknown36(3)
    Unknown3004(-30)
    Unknown35()
    GFX_0('450flash', 100)
    sprite('keep', 50)	# 284-333
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(0)
    Unknown36(22)
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(-500000)
    Unknown35()
    Unknown1084(1)
    GFX_0('IchigekiCamera', 100)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000022000000')
    GFX_0('IchigekiPicture', 100)
    GFX_0('Sakurafubuki_slow', 100)
    GFX_0('SakuraSE', 100)
    sprite('null', 30)	# 334-363
    tag_voice(0, 'pyu291_0', 'pyu291_1', '', '')
    sprite('null', 70)	# 364-433
    sprite('null', 20)	# 434-453
    GFX_0('BG_sakura', 100)
    sprite('null', 40)	# 454-493
    Unknown36(22)
    Unknown3004(30)
    Unknown35()
    Unknown36(3)
    Unknown3004(30)
    Unknown35()
    GFX_0('IchigekiBlack', 100)
    tag_voice(0, 'pyu292_0', 'pyu292_1', '', '')
    sprite('null', 10)	# 494-503
    Unknown21012('53616b757261534500000000000000000000000000000000000000000000000020000000')
    SFX_3('yu003')
    GFX_0('Ichigeki_HitEff', 100)
    label(3)
    sprite('null', 5)	# 504-508
    SFX_3('yu003')
    SLOT_53 = (SLOT_53 + 1)
    if (SLOT_53 == 32):
        sendToLabel(4)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('null', 20)	# 509-528
    sprite('null', 120)	# 529-648
    Unknown21012('4963686967656b69426c61636b0000000000000000000000000000000000000020000000')
    Unknown21012('42475f73616b757261000000000000000000000000000000000000000000000020000000')
    GFX_0('IchigekiCamera', 100)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000021000000')
    Unknown18009(0)
    GFX_0('IchigekiWhite', 100)
    Unknown23024(0)
    sprite('yu450_16', 30)	# 649-678	 **attackbox here**
    Unknown21012('53616b757261667562756b695f736c6f7700000000000000000000000000000020000000')
    GFX_0('Sakuraend', 100)
    sprite('yu450_16', 2)	# 679-680	 **attackbox here**
    sprite('yu450_16', 4)	# 681-684	 **attackbox here**
    Unknown20000(1)
    sprite('yu450_17', 6)	# 685-690	 **attackbox here**
    sprite('yu450_18', 6)	# 691-696	 **attackbox here**
    sprite('yu450_19', 6)	# 697-702	 **attackbox here**
    sprite('yu450_20', 6)	# 703-708	 **attackbox here**
    SFX_3('cloth_m')
    sprite('yu450_16', 6)	# 709-714	 **attackbox here**
    sprite('yu450_17', 6)	# 715-720	 **attackbox here**
    sprite('yu450_18', 6)	# 721-726	 **attackbox here**
    sprite('yu450_19', 6)	# 727-732	 **attackbox here**
    sprite('yu450_20', 6)	# 733-738	 **attackbox here**
    SFX_3('cloth_m')
    sprite('yu450_16', 6)	# 739-744	 **attackbox here**
    Unknown18010()
    tag_voice(0, 'pyu293_0', 'pyu293_1', '', '')
    Unknown23018(1)
    sprite('yu450_17', 6)	# 745-750	 **attackbox here**
    sprite('yu450_18', 6)	# 751-756	 **attackbox here**
    sprite('yu450_19', 6)	# 757-762	 **attackbox here**
    sprite('yu450_20', 6)	# 763-768	 **attackbox here**
    SFX_3('cloth_l')
    label(99)
    sprite('yu450_16', 6)	# 769-774	 **attackbox here**
    sprite('yu450_17', 6)	# 775-780	 **attackbox here**
    sprite('yu450_18', 6)	# 781-786	 **attackbox here**
    sprite('yu450_19', 6)	# 787-792	 **attackbox here**
    sprite('yu450_20', 6)	# 793-798	 **attackbox here**
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(99)
    ExitState()
    label(0)
    sprite('yu450_12', 4)	# 799-802
    setInvincible(0)
    sprite('yu450_13', 4)	# 803-806
    sprite('yu450_14', 4)	# 807-810
    sprite('yu450_12', 4)	# 811-814
    sprite('yu450_13', 4)	# 815-818
    sprite('yu450_14', 4)	# 819-822
    sprite('yu450_12', 5)	# 823-827
    sprite('yu450_13', 5)	# 828-832
    sprite('yu450_14', 5)	# 833-837
    sprite('yu450_12', 6)	# 838-843
    sprite('yu450_13', 6)	# 844-849
    sprite('yu450_14', 6)	# 850-855
    sprite('yu450_15', 4)	# 856-859

@Subroutine
def MouthTableInit():
    Unknown18011('pyu000', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu293_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu293_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu500', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu502', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu503', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu504', 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu505', 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu506', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu507', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu520', 12643, 14177, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu525', 12643, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu403_0', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu403_1', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu600pce', 12643, 13665, 13667, 13665, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu600pla', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu600rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu600uca', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu601bjb', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu601bph', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu601brc', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu601pbc', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu601pka', 12643, 12897, 25392, 14134, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu601ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu700bjb', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu700bph', 12643, 14177, 12643, 24880, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu700pka', 12643, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu700rwi', 12643, 13665, 13667, 13665, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu700uca', 12643, 13665, 13667, 13665, 13411, 24887, 25399, 14131, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu701brc', 12643, 13665, 13667, 13665, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu700pbc', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu701pce_1', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu701pce_2', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu701pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25397, 24885, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pyu701ugo', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13107, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bjb')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('yu600_00', 6)	# 2-7
    if SLOT_158:
        Unknown7006('pyu500', 100, 896891248, 12592, 0, 0, 100, 896891248, 12848, 0, 0, 100, 896891248, 13872, 0, 0, 100)
    sprite('yu600_01', 6)	# 8-13
    sprite('yu600_02', 6)	# 14-19
    sprite('yu600_03', 6)	# 20-25
    sprite('yu600_04', 30)	# 26-55
    sprite('yu600_03', 6)	# 56-61
    sprite('yu600_02', 6)	# 62-67
    sprite('yu600_01', 6)	# 68-73
    sprite('yu600_05', 6)	# 74-79
    sprite('yu600_06', 6)	# 80-85
    sprite('yu600_07', 6)	# 86-91
    sprite('yu600_08', 6)	# 92-97
    sprite('yu600_09', 6)	# 98-103
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_10', 6)	# 104-109
    SFX_3('yu000')
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_11', 10)	# 110-119
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_12', 6)	# 120-125
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_13', 6)	# 126-131
    GFX_1('yuef_hinoko', 0)
    Unknown23018(1)
    label(1)
    sprite('yu000_00', 6)	# 132-137
    sprite('yu000_01', 6)	# 138-143
    sprite('yu000_02', 6)	# 144-149
    sprite('yu000_03', 6)	# 150-155
    sprite('yu000_04', 6)	# 156-161
    sprite('yu000_05', 6)	# 162-167
    sprite('yu000_06', 6)	# 168-173
    sprite('yu000_07', 6)	# 174-179
    sprite('yu000_08', 6)	# 180-185
    sprite('yu000_09', 6)	# 186-191
    sprite('yu000_10', 6)	# 192-197
    sprite('yu000_11', 6)	# 198-203
    sprite('yu000_12', 6)	# 204-209
    sprite('yu000_13', 6)	# 210-215
    sprite('yu000_14', 6)	# 216-221
    sprite('yu000_15', 6)	# 222-227
    loopRest()
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('yu601_00', 32767)	# 228-32994
    Unknown36(24)
    teleportRelativeX(-200000)
    Unknown35()
    Unknown23029(11, 50, 0)
    sendToLabelUpon(32, 11)
    loopRest()
    label(11)
    sprite('yu601_01', 6)	# 32995-33000
    if random_(2, 0, 50):
        Unknown7006('pyu503', 100, 896891248, 13616, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_2 = 1
    else:
        SLOT_51 = 1
    sprite('yu601_02', 6)	# 33001-33006
    if SLOT_51:
        if random_(2, 0, 50):
            SFX_1('pyu504')
            SLOT_2 = 1
        else:
            SFX_1('pyu507')
    Unknown23018(1)
    sprite('yu601_01', 6)	# 33007-33012
    sprite('yu601_02', 6)	# 33013-33018
    sprite('yu601_01', 6)	# 33019-33024
    sprite('yu601_02', 6)	# 33025-33030
    sprite('yu601_01', 6)	# 33031-33036
    sprite('yu601_02', 6)	# 33037-33042
    sprite('yu601_01', 6)	# 33043-33048
    sprite('yu601_02', 6)	# 33049-33054
    sprite('yu601_01', 6)	# 33055-33060
    sprite('yu601_02', 6)	# 33061-33066
    sprite('yu601_01', 6)	# 33067-33072
    sprite('yu601_02', 6)	# 33073-33078
    sprite('yu601_01', 6)	# 33079-33084
    sprite('yu601_02', 6)	# 33085-33090
    sprite('yu601_01', 6)	# 33091-33096
    sprite('yu601_02', 6)	# 33097-33102
    if SLOT_2:
        sendToLabel(12)
    sprite('yu601_01', 6)	# 33103-33108
    sprite('yu601_02', 6)	# 33109-33114
    sprite('yu601_01', 6)	# 33115-33120
    sprite('yu601_02', 6)	# 33121-33126
    label(12)
    sprite('yu601_03', 6)	# 33127-33132
    sprite('yu601_04', 6)	# 33133-33138
    sprite('yu601_05', 6)	# 33139-33144
    SFX_3('cloth_m')
    sprite('yu601_06', 6)	# 33145-33150
    sprite('yu601_07', 6)	# 33151-33156
    sprite('yu601_08', 6)	# 33157-33162
    sprite('yu601_09', 6)	# 33163-33168
    SFX_3('hair')
    sprite('yu601_10', 6)	# 33169-33174
    sprite('yu601_11', 6)	# 33175-33180
    sprite('yu601_12', 6)	# 33181-33186
    label(13)
    sprite('yu000_00', 6)	# 33187-33192
    sprite('yu000_01', 6)	# 33193-33198
    sprite('yu000_02', 6)	# 33199-33204
    sprite('yu000_03', 6)	# 33205-33210
    sprite('yu000_04', 6)	# 33211-33216
    sprite('yu000_05', 6)	# 33217-33222
    sprite('yu000_06', 6)	# 33223-33228
    sprite('yu000_07', 6)	# 33229-33234
    sprite('yu000_08', 6)	# 33235-33240
    sprite('yu000_09', 6)	# 33241-33246
    sprite('yu000_10', 6)	# 33247-33252
    sprite('yu000_11', 6)	# 33253-33258
    sprite('yu000_12', 6)	# 33259-33264
    sprite('yu000_13', 6)	# 33265-33270
    sprite('yu000_14', 6)	# 33271-33276
    sprite('yu000_15', 6)	# 33277-33282
    loopRest()
    gotoLabel(13)
    ExitState()
    label(20)
    sprite('yu000_00', 1)	# 33283-33283
    SFX_1('pyu701pla')
    label(21)
    sprite('yu000_00', 6)	# 33284-33289
    sprite('yu000_01', 6)	# 33290-33295
    sprite('yu000_02', 6)	# 33296-33301
    sprite('yu000_03', 6)	# 33302-33307
    sprite('yu000_04', 6)	# 33308-33313
    sprite('yu000_05', 6)	# 33314-33319
    sprite('yu000_06', 6)	# 33320-33325
    sprite('yu000_07', 6)	# 33326-33331
    sprite('yu000_08', 6)	# 33332-33337
    sprite('yu000_09', 6)	# 33338-33343
    sprite('yu000_10', 6)	# 33344-33349
    sprite('yu000_11', 6)	# 33350-33355
    sprite('yu000_12', 6)	# 33356-33361
    sprite('yu000_13', 6)	# 33362-33367
    sprite('yu000_14', 6)	# 33368-33373
    sprite('yu000_15', 6)	# 33374-33379
    gotoLabel(21)
    label(100)
    sprite('yu000_00', 1)	# 33380-33380
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('yu000_00', 6)	# 33381-33386
    sprite('yu000_01', 6)	# 33387-33392
    sprite('yu000_02', 6)	# 33393-33398
    sprite('yu000_03', 6)	# 33399-33404
    sprite('yu000_04', 6)	# 33405-33410
    sprite('yu000_05', 6)	# 33411-33416
    sprite('yu000_06', 6)	# 33417-33422
    sprite('yu000_07', 6)	# 33423-33428
    sprite('yu000_08', 6)	# 33429-33434
    sprite('yu000_09', 6)	# 33435-33440
    sprite('yu000_10', 6)	# 33441-33446
    sprite('yu000_11', 6)	# 33447-33452
    sprite('yu000_12', 6)	# 33453-33458
    sprite('yu000_13', 6)	# 33459-33464
    sprite('yu000_14', 6)	# 33465-33470
    sprite('yu000_15', 6)	# 33471-33476
    gotoLabel(101)
    label(102)
    sprite('yu001_00', 8)	# 33477-33484
    sprite('yu001_01', 8)	# 33485-33492
    SFX_1('pyu601brc')
    sprite('yu001_02', 8)	# 33493-33500
    sprite('yu001_03', 8)	# 33501-33508
    sprite('yu001_04', 8)	# 33509-33516
    GFX_0('reaction_sakura', 0)
    sprite('yu001_05', 8)	# 33517-33524
    GFX_0('reaction_sakura', 0)
    sprite('yu001_06', 8)	# 33525-33532
    GFX_0('reaction_sakura', 0)
    sprite('yu001_07', 8)	# 33533-33540
    sprite('yu001_08', 8)	# 33541-33548
    sprite('yu001_00', 8)	# 33549-33556
    Unknown21011(120)
    label(103)
    sprite('yu000_00', 6)	# 33557-33562
    sprite('yu000_01', 6)	# 33563-33568
    sprite('yu000_02', 6)	# 33569-33574
    sprite('yu000_03', 6)	# 33575-33580
    sprite('yu000_04', 6)	# 33581-33586
    sprite('yu000_05', 6)	# 33587-33592
    sprite('yu000_06', 6)	# 33593-33598
    sprite('yu000_07', 6)	# 33599-33604
    sprite('yu000_08', 6)	# 33605-33610
    sprite('yu000_09', 6)	# 33611-33616
    sprite('yu000_10', 6)	# 33617-33622
    sprite('yu000_11', 6)	# 33623-33628
    sprite('yu000_12', 6)	# 33629-33634
    sprite('yu000_13', 6)	# 33635-33640
    sprite('yu000_14', 6)	# 33641-33646
    sprite('yu000_15', 6)	# 33647-33652
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('yu000_00', 1)	# 33653-33653
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('yu000_00', 6)	# 33654-33659
    sprite('yu000_01', 6)	# 33660-33665
    sprite('yu000_02', 6)	# 33666-33671
    sprite('yu000_03', 6)	# 33672-33677
    sprite('yu000_04', 6)	# 33678-33683
    sprite('yu000_05', 6)	# 33684-33689
    sprite('yu000_06', 6)	# 33690-33695
    sprite('yu000_07', 6)	# 33696-33701
    sprite('yu000_08', 6)	# 33702-33707
    sprite('yu000_09', 6)	# 33708-33713
    sprite('yu000_10', 6)	# 33714-33719
    sprite('yu000_11', 6)	# 33720-33725
    sprite('yu000_12', 6)	# 33726-33731
    sprite('yu000_13', 6)	# 33732-33737
    sprite('yu000_14', 6)	# 33738-33743
    sprite('yu000_15', 6)	# 33744-33749
    gotoLabel(111)
    label(112)
    sprite('yu001_00', 8)	# 33750-33757
    sprite('yu001_01', 8)	# 33758-33765
    SFX_1('pyu601bjb')
    sprite('yu001_02', 8)	# 33766-33773
    sprite('yu001_03', 8)	# 33774-33781
    sprite('yu001_04', 8)	# 33782-33789
    GFX_0('reaction_sakura', 0)
    sprite('yu001_05', 8)	# 33790-33797
    GFX_0('reaction_sakura', 0)
    sprite('yu001_06', 8)	# 33798-33805
    GFX_0('reaction_sakura', 0)
    sprite('yu001_07', 8)	# 33806-33813
    sprite('yu001_08', 8)	# 33814-33821
    sprite('yu001_00', 8)	# 33822-33829
    Unknown23018(1)
    label(113)
    sprite('yu000_00', 6)	# 33830-33835
    sprite('yu000_01', 6)	# 33836-33841
    sprite('yu000_02', 6)	# 33842-33847
    sprite('yu000_03', 6)	# 33848-33853
    sprite('yu000_04', 6)	# 33854-33859
    sprite('yu000_05', 6)	# 33860-33865
    sprite('yu000_06', 6)	# 33866-33871
    sprite('yu000_07', 6)	# 33872-33877
    sprite('yu000_08', 6)	# 33878-33883
    sprite('yu000_09', 6)	# 33884-33889
    sprite('yu000_10', 6)	# 33890-33895
    sprite('yu000_11', 6)	# 33896-33901
    sprite('yu000_12', 6)	# 33902-33907
    sprite('yu000_13', 6)	# 33908-33913
    sprite('yu000_14', 6)	# 33914-33919
    sprite('yu000_15', 6)	# 33920-33925
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('yu601_00', 32767)	# 33926-66692
    if SLOT_158:
        Unknown1000(-1665000)
    else:
        Unknown1000(-1665000)

    def upon_40():
        clearUponHandler(40)
        Unknown21007(11, 32)
    Unknown23029(11, 55, 0)
    sendToLabelUpon(32, 121)
    loopRest()
    label(121)
    sprite('yu601_01', 6)	# 66693-66698
    SFX_1('pyu601pbc')
    sprite('yu601_02', 6)	# 66699-66704
    sprite('yu601_01', 6)	# 66705-66710
    sprite('yu601_02', 6)	# 66711-66716
    sprite('yu601_01', 6)	# 66717-66722
    sprite('yu601_02', 6)	# 66723-66728
    sprite('yu601_01', 6)	# 66729-66734
    sprite('yu601_02', 6)	# 66735-66740
    sprite('yu601_01', 6)	# 66741-66746
    sprite('yu601_02', 6)	# 66747-66752
    sprite('yu601_01', 6)	# 66753-66758
    sprite('yu601_02', 6)	# 66759-66764
    sprite('yu601_01', 6)	# 66765-66770
    sprite('yu601_02', 6)	# 66771-66776
    sprite('yu601_01', 6)	# 66777-66782
    sprite('yu601_02', 6)	# 66783-66788
    sprite('yu601_01', 6)	# 66789-66794
    sprite('yu601_02', 6)	# 66795-66800
    sprite('yu601_03', 6)	# 66801-66806
    sprite('yu601_04', 6)	# 66807-66812
    sprite('yu601_05', 6)	# 66813-66818
    SFX_3('cloth_m')
    sprite('yu601_06', 6)	# 66819-66824
    sprite('yu601_07', 6)	# 66825-66830
    sprite('yu601_08', 6)	# 66831-66836
    sprite('yu601_09', 6)	# 66837-66842
    SFX_3('hair')
    sprite('yu601_10', 6)	# 66843-66848
    sprite('yu601_11', 6)	# 66849-66854
    sprite('yu601_12', 6)	# 66855-66860
    Unknown21011(120)
    label(122)
    sprite('yu000_00', 6)	# 66861-66866
    sprite('yu000_01', 6)	# 66867-66872
    sprite('yu000_02', 6)	# 66873-66878
    sprite('yu000_03', 6)	# 66879-66884
    sprite('yu000_04', 6)	# 66885-66890
    sprite('yu000_05', 6)	# 66891-66896
    sprite('yu000_06', 6)	# 66897-66902
    sprite('yu000_07', 6)	# 66903-66908
    sprite('yu000_08', 6)	# 66909-66914
    sprite('yu000_09', 6)	# 66915-66920
    sprite('yu000_10', 6)	# 66921-66926
    sprite('yu000_11', 6)	# 66927-66932
    sprite('yu000_12', 6)	# 66933-66938
    sprite('yu000_13', 6)	# 66939-66944
    sprite('yu000_14', 6)	# 66945-66950
    sprite('yu000_15', 6)	# 66951-66956
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('yu601_00', 32767)	# 66957-99723
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1665000)

    def upon_40():
        clearUponHandler(40)
        Unknown21007(11, 32)
    Unknown23029(11, 55, 0)
    sendToLabelUpon(32, 131)
    loopRest()
    label(131)
    sprite('yu601_01', 6)	# 99724-99729
    SFX_1('pyu601ugo')
    sprite('yu601_02', 6)	# 99730-99735
    sprite('yu601_01', 6)	# 99736-99741
    sprite('yu601_02', 6)	# 99742-99747
    sprite('yu601_01', 6)	# 99748-99753
    sprite('yu601_02', 6)	# 99754-99759
    sprite('yu601_01', 6)	# 99760-99765
    sprite('yu601_02', 6)	# 99766-99771
    sprite('yu601_01', 6)	# 99772-99777
    sprite('yu601_02', 6)	# 99778-99783
    sprite('yu601_01', 6)	# 99784-99789
    sprite('yu601_02', 6)	# 99790-99795
    sprite('yu601_01', 6)	# 99796-99801
    sprite('yu601_02', 6)	# 99802-99807
    sprite('yu601_01', 6)	# 99808-99813
    sprite('yu601_02', 6)	# 99814-99819
    sprite('yu601_01', 6)	# 99820-99825
    sprite('yu601_02', 6)	# 99826-99831
    sprite('yu601_03', 6)	# 99832-99837
    sprite('yu601_04', 6)	# 99838-99843
    sprite('yu601_05', 6)	# 99844-99849
    SFX_3('cloth_m')
    sprite('yu601_06', 6)	# 99850-99855
    sprite('yu601_07', 6)	# 99856-99861
    sprite('yu601_08', 6)	# 99862-99867
    sprite('yu601_09', 6)	# 99868-99873
    SFX_3('hair')
    sprite('yu601_10', 6)	# 99874-99879
    sprite('yu601_11', 6)	# 99880-99885
    sprite('yu601_12', 6)	# 99886-99891
    Unknown21011(120)
    label(132)
    sprite('yu000_00', 6)	# 99892-99897
    sprite('yu000_01', 6)	# 99898-99903
    sprite('yu000_02', 6)	# 99904-99909
    sprite('yu000_03', 6)	# 99910-99915
    sprite('yu000_04', 6)	# 99916-99921
    sprite('yu000_05', 6)	# 99922-99927
    sprite('yu000_06', 6)	# 99928-99933
    sprite('yu000_07', 6)	# 99934-99939
    sprite('yu000_08', 6)	# 99940-99945
    sprite('yu000_09', 6)	# 99946-99951
    sprite('yu000_10', 6)	# 99952-99957
    sprite('yu000_11', 6)	# 99958-99963
    sprite('yu000_12', 6)	# 99964-99969
    sprite('yu000_13', 6)	# 99970-99975
    sprite('yu000_14', 6)	# 99976-99981
    sprite('yu000_15', 6)	# 99982-99987
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('yu601_00', 32767)	# 99988-132754
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown23029(11, 50, 0)
    sendToLabelUpon(32, 141)
    loopRest()
    label(141)
    sprite('yu601_01', 6)	# 132755-132760
    SFX_1('pyu600rwi')
    sprite('yu601_02', 6)	# 132761-132766
    sprite('yu601_01', 6)	# 132767-132772
    sprite('yu601_02', 6)	# 132773-132778
    sprite('yu601_01', 6)	# 132779-132784
    sprite('yu601_02', 6)	# 132785-132790
    sprite('yu601_01', 6)	# 132791-132796
    sprite('yu601_02', 6)	# 132797-132802
    sprite('yu601_01', 6)	# 132803-132808
    sprite('yu601_02', 6)	# 132809-132814
    sprite('yu601_01', 6)	# 132815-132820
    sprite('yu601_02', 6)	# 132821-132826
    sprite('yu601_01', 6)	# 132827-132832
    sprite('yu601_02', 6)	# 132833-132838
    sprite('yu601_01', 6)	# 132839-132844
    sprite('yu601_02', 6)	# 132845-132850
    sprite('yu601_01', 6)	# 132851-132856
    sprite('yu601_02', 6)	# 132857-132862
    sprite('yu601_03', 6)	# 132863-132868
    sprite('yu601_04', 6)	# 132869-132874
    sprite('yu601_05', 6)	# 132875-132880
    SFX_3('cloth_m')
    sprite('yu601_06', 6)	# 132881-132886
    sprite('yu601_07', 6)	# 132887-132892
    sprite('yu601_08', 6)	# 132893-132898
    sprite('yu601_09', 6)	# 132899-132904
    SFX_3('hair')
    sprite('yu601_10', 6)	# 132905-132910
    sprite('yu601_11', 6)	# 132911-132916
    sprite('yu601_12', 6)	# 132917-132922
    sprite('yu000_00', 6)	# 132923-132928
    sprite('yu000_01', 6)	# 132929-132934
    sprite('yu000_02', 6)	# 132935-132940
    sprite('yu000_03', 6)	# 132941-132946
    sprite('yu000_04', 6)	# 132947-132952
    sprite('yu000_05', 6)	# 132953-132958
    sprite('yu000_06', 6)	# 132959-132964
    sprite('yu000_07', 6)	# 132965-132970
    sprite('yu000_08', 6)	# 132971-132976
    sprite('yu000_09', 6)	# 132977-132982
    sprite('yu000_10', 6)	# 132983-132988
    sprite('yu000_11', 6)	# 132989-132994
    sprite('yu000_12', 6)	# 132995-133000
    sprite('yu000_13', 6)	# 133001-133006
    sprite('yu000_14', 6)	# 133007-133012
    sprite('yu000_15', 6)	# 133013-133018
    sprite('yu000_00', 6)	# 133019-133024
    sprite('yu000_01', 6)	# 133025-133030
    sprite('yu000_02', 6)	# 133031-133036
    sprite('yu000_03', 6)	# 133037-133042
    sprite('yu000_04', 6)	# 133043-133048
    sprite('yu000_05', 6)	# 133049-133054
    Unknown21007(24, 40)
    Unknown21011(400)
    sprite('yu000_06', 6)	# 133055-133060
    sprite('yu000_07', 6)	# 133061-133066
    sprite('yu000_08', 6)	# 133067-133072
    sprite('yu000_09', 6)	# 133073-133078
    sprite('yu000_10', 6)	# 133079-133084
    sprite('yu000_11', 6)	# 133085-133090
    sprite('yu000_12', 6)	# 133091-133096
    sprite('yu000_13', 6)	# 133097-133102
    sprite('yu000_14', 6)	# 133103-133108
    sprite('yu000_15', 6)	# 133109-133114
    label(142)
    sprite('yu000_00', 6)	# 133115-133120
    sprite('yu000_01', 6)	# 133121-133126
    sprite('yu000_02', 6)	# 133127-133132
    sprite('yu000_03', 6)	# 133133-133138
    sprite('yu000_04', 6)	# 133139-133144
    sprite('yu000_05', 6)	# 133145-133150
    sprite('yu000_06', 6)	# 133151-133156
    sprite('yu000_07', 6)	# 133157-133162
    sprite('yu000_08', 6)	# 133163-133168
    sprite('yu000_09', 6)	# 133169-133174
    sprite('yu000_10', 6)	# 133175-133180
    sprite('yu000_11', 6)	# 133181-133186
    sprite('yu000_12', 6)	# 133187-133192
    sprite('yu000_13', 6)	# 133193-133198
    sprite('yu000_14', 6)	# 133199-133204
    sprite('yu000_15', 6)	# 133205-133210
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('yu000_00', 1)	# 133211-133211
    if (not SLOT_158):
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('yu000_00', 6)	# 133212-133217
    sprite('yu000_01', 6)	# 133218-133223
    sprite('yu000_02', 6)	# 133224-133229
    sprite('yu000_03', 6)	# 133230-133235
    sprite('yu000_04', 6)	# 133236-133241
    sprite('yu000_05', 6)	# 133242-133247
    sprite('yu000_06', 6)	# 133248-133253
    sprite('yu000_07', 6)	# 133254-133259
    sprite('yu000_08', 6)	# 133260-133265
    sprite('yu000_09', 6)	# 133266-133271
    sprite('yu000_10', 6)	# 133272-133277
    sprite('yu000_11', 6)	# 133278-133283
    sprite('yu000_12', 6)	# 133284-133289
    sprite('yu000_13', 6)	# 133290-133295
    sprite('yu000_14', 6)	# 133296-133301
    sprite('yu000_15', 6)	# 133302-133307
    gotoLabel(151)
    label(152)
    sprite('yu001_00', 8)	# 133308-133315
    sprite('yu001_01', 8)	# 133316-133323
    SFX_1('pyu601pka')
    sprite('yu001_02', 8)	# 133324-133331
    sprite('yu001_03', 8)	# 133332-133339
    sprite('yu001_04', 8)	# 133340-133347
    GFX_0('reaction_sakura', 0)
    sprite('yu001_05', 8)	# 133348-133355
    GFX_0('reaction_sakura', 0)
    sprite('yu001_06', 8)	# 133356-133363
    GFX_0('reaction_sakura', 0)
    sprite('yu001_07', 8)	# 133364-133371
    sprite('yu001_08', 8)	# 133372-133379
    sprite('yu001_00', 8)	# 133380-133387
    Unknown23018(1)
    label(153)
    sprite('yu000_00', 6)	# 133388-133393
    sprite('yu000_01', 6)	# 133394-133399
    sprite('yu000_02', 6)	# 133400-133405
    sprite('yu000_03', 6)	# 133406-133411
    sprite('yu000_04', 6)	# 133412-133417
    sprite('yu000_05', 6)	# 133418-133423
    sprite('yu000_06', 6)	# 133424-133429
    sprite('yu000_07', 6)	# 133430-133435
    sprite('yu000_08', 6)	# 133436-133441
    sprite('yu000_09', 6)	# 133442-133447
    sprite('yu000_10', 6)	# 133448-133453
    sprite('yu000_11', 6)	# 133454-133459
    sprite('yu000_12', 6)	# 133460-133465
    sprite('yu000_13', 6)	# 133466-133471
    sprite('yu000_14', 6)	# 133472-133477
    sprite('yu000_15', 6)	# 133478-133483
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('yu641_00', 1)	# 133484-133484
    Unknown2019(-100)
    Unknown1000(-1290000)
    sprite('yu641_00', 6)	# 133485-133490
    sprite('yu641_01', 6)	# 133491-133496
    sprite('yu641_02', 6)	# 133497-133502
    SFX_1('pyu600pce')
    sprite('yu641_03', 6)	# 133503-133508
    sprite('yu641_04', 6)	# 133509-133514
    label(161)
    sprite('yu641_00', 6)	# 133515-133520
    sprite('yu641_01', 6)	# 133521-133526
    sprite('yu641_02', 6)	# 133527-133532
    sprite('yu641_03', 6)	# 133533-133538
    sprite('yu641_04', 6)	# 133539-133544
    if SLOT_97:
        _gotolabel(161)
    sprite('yu641_00', 1)	# 133545-133545
    Unknown21007(24, 40)
    Unknown21011(240)
    label(162)
    sprite('yu641_00', 6)	# 133546-133551
    sprite('yu641_01', 6)	# 133552-133557
    sprite('yu641_02', 6)	# 133558-133563
    sprite('yu641_03', 6)	# 133564-133569
    sprite('yu641_04', 6)	# 133570-133575
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('yu600_00', 6)	# 133576-133581
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)
    SFX_1('pyu600uca')
    sprite('yu600_01', 6)	# 133582-133587
    sprite('yu600_02', 6)	# 133588-133593
    sprite('yu600_03', 6)	# 133594-133599
    sprite('yu600_04', 30)	# 133600-133629
    sprite('yu600_03', 6)	# 133630-133635
    sprite('yu600_02', 6)	# 133636-133641
    sprite('yu600_01', 6)	# 133642-133647
    sprite('yu600_05', 6)	# 133648-133653
    sprite('yu600_06', 6)	# 133654-133659
    sprite('yu600_07', 6)	# 133660-133665
    sprite('yu600_08', 6)	# 133666-133671
    sprite('yu600_09', 6)	# 133672-133677
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_10', 6)	# 133678-133683
    SFX_3('yu000')
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_11', 10)	# 133684-133693
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_12', 6)	# 133694-133699
    GFX_1('yuef_hinoko', 0)
    sprite('yu600_13', 6)	# 133700-133705
    GFX_1('yuef_hinoko', 0)
    Unknown21011(380)
    label(171)
    sprite('yu000_00', 6)	# 133706-133711
    sprite('yu000_01', 6)	# 133712-133717
    sprite('yu000_02', 6)	# 133718-133723
    sprite('yu000_03', 6)	# 133724-133729
    sprite('yu000_04', 6)	# 133730-133735
    sprite('yu000_05', 6)	# 133736-133741
    sprite('yu000_06', 6)	# 133742-133747
    sprite('yu000_07', 6)	# 133748-133753
    sprite('yu000_08', 6)	# 133754-133759
    Unknown21007(24, 40)
    sprite('yu000_09', 6)	# 133760-133765
    sprite('yu000_10', 6)	# 133766-133771
    sprite('yu000_11', 6)	# 133772-133777
    sprite('yu000_12', 6)	# 133778-133783
    sprite('yu000_13', 6)	# 133784-133789
    sprite('yu000_14', 6)	# 133790-133795
    sprite('yu000_15', 6)	# 133796-133801
    gotoLabel(171)
    ExitState()
    label(180)
    sprite('yu000_00', 1)	# 133802-133802
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('yu000_00', 6)	# 133803-133808
    sprite('yu000_01', 6)	# 133809-133814
    sprite('yu001_00', 8)	# 133815-133822
    sprite('yu001_01', 8)	# 133823-133830
    SFX_1('pyu600pla')
    sprite('yu001_02', 8)	# 133831-133838
    sprite('yu001_03', 8)	# 133839-133846
    sprite('yu001_04', 8)	# 133847-133854
    GFX_0('reaction_sakura', 0)
    sprite('yu001_05', 8)	# 133855-133862
    GFX_0('reaction_sakura', 0)
    sprite('yu001_06', 8)	# 133863-133870
    GFX_0('reaction_sakura', 0)
    sprite('yu001_07', 8)	# 133871-133878
    sprite('yu001_08', 8)	# 133879-133886
    sprite('yu001_00', 8)	# 133887-133894
    label(181)
    sprite('yu000_00', 6)	# 133895-133900
    sprite('yu000_01', 6)	# 133901-133906
    sprite('yu000_02', 6)	# 133907-133912
    sprite('yu000_03', 6)	# 133913-133918
    sprite('yu000_04', 6)	# 133919-133924
    sprite('yu000_05', 6)	# 133925-133930
    sprite('yu000_06', 6)	# 133931-133936
    sprite('yu000_07', 6)	# 133937-133942
    sprite('yu000_08', 6)	# 133943-133948
    sprite('yu000_09', 6)	# 133949-133954
    sprite('yu000_10', 6)	# 133955-133960
    sprite('yu000_11', 6)	# 133961-133966
    sprite('yu000_12', 6)	# 133967-133972
    sprite('yu000_13', 6)	# 133973-133978
    sprite('yu000_14', 6)	# 133979-133984
    sprite('yu000_15', 6)	# 133985-133990
    if SLOT_97:
        _gotolabel(181)
    sprite('yu000_00', 1)	# 133991-133991
    Unknown21007(24, 40)
    Unknown21011(270)
    label(182)
    sprite('yu000_00', 6)	# 133992-133997
    sprite('yu000_01', 6)	# 133998-134003
    sprite('yu000_02', 6)	# 134004-134009
    sprite('yu000_03', 6)	# 134010-134015
    sprite('yu000_04', 6)	# 134016-134021
    sprite('yu000_05', 6)	# 134022-134027
    sprite('yu000_06', 6)	# 134028-134033
    sprite('yu000_07', 6)	# 134034-134039
    sprite('yu000_08', 6)	# 134040-134045
    sprite('yu000_09', 6)	# 134046-134051
    sprite('yu000_10', 6)	# 134052-134057
    sprite('yu000_11', 6)	# 134058-134063
    sprite('yu000_12', 6)	# 134064-134069
    sprite('yu000_13', 6)	# 134070-134075
    sprite('yu000_14', 6)	# 134076-134081
    sprite('yu000_15', 6)	# 134082-134087
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('yu000_00', 1)	# 134088-134088
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('yu000_00', 6)	# 134089-134094
    sprite('yu000_01', 6)	# 134095-134100
    sprite('yu000_02', 6)	# 134101-134106
    sprite('yu000_03', 6)	# 134107-134112
    sprite('yu000_04', 6)	# 134113-134118
    sprite('yu000_05', 6)	# 134119-134124
    sprite('yu000_06', 6)	# 134125-134130
    sprite('yu000_07', 6)	# 134131-134136
    sprite('yu000_08', 6)	# 134137-134142
    sprite('yu000_09', 6)	# 134143-134148
    sprite('yu000_10', 6)	# 134149-134154
    sprite('yu000_11', 6)	# 134155-134160
    sprite('yu000_12', 6)	# 134161-134166
    sprite('yu000_13', 6)	# 134167-134172
    sprite('yu000_14', 6)	# 134173-134178
    sprite('yu000_15', 6)	# 134179-134184
    gotoLabel(191)
    label(192)
    sprite('yu001_00', 8)	# 134185-134192
    sprite('yu001_01', 8)	# 134193-134200
    SFX_1('pyu601bph')
    sprite('yu001_02', 8)	# 134201-134208
    sprite('yu001_03', 8)	# 134209-134216
    sprite('yu001_04', 8)	# 134217-134224
    GFX_0('reaction_sakura', 0)
    sprite('yu001_05', 8)	# 134225-134232
    GFX_0('reaction_sakura', 0)
    sprite('yu001_06', 8)	# 134233-134240
    GFX_0('reaction_sakura', 0)
    sprite('yu001_07', 8)	# 134241-134248
    sprite('yu001_08', 8)	# 134249-134256
    sprite('yu001_00', 8)	# 134257-134264
    Unknown23018(1)
    label(193)
    sprite('yu000_00', 6)	# 134265-134270
    sprite('yu000_01', 6)	# 134271-134276
    sprite('yu000_02', 6)	# 134277-134282
    sprite('yu000_03', 6)	# 134283-134288
    sprite('yu000_04', 6)	# 134289-134294
    sprite('yu000_05', 6)	# 134295-134300
    sprite('yu000_06', 6)	# 134301-134306
    sprite('yu000_07', 6)	# 134307-134312
    sprite('yu000_08', 6)	# 134313-134318
    sprite('yu000_09', 6)	# 134319-134324
    sprite('yu000_10', 6)	# 134325-134330
    sprite('yu000_11', 6)	# 134331-134336
    sprite('yu000_12', 6)	# 134337-134342
    sprite('yu000_13', 6)	# 134343-134348
    sprite('yu000_14', 6)	# 134349-134354
    sprite('yu000_15', 6)	# 134355-134360
    gotoLabel(193)
    ExitState()
    label(991)
    sprite('yu000_00', 1)	# 134361-134361
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('yu000_00', 6)	# 134362-134367
    sprite('yu000_01', 6)	# 134368-134373
    sprite('yu000_02', 6)	# 134374-134379
    sprite('yu000_03', 6)	# 134380-134385
    sprite('yu000_04', 6)	# 134386-134391
    sprite('yu000_05', 6)	# 134392-134397
    sprite('yu000_06', 6)	# 134398-134403
    sprite('yu000_07', 6)	# 134404-134409
    sprite('yu000_08', 6)	# 134410-134415
    sprite('yu000_09', 6)	# 134416-134421
    sprite('yu000_10', 6)	# 134422-134427
    sprite('yu000_11', 6)	# 134428-134433
    sprite('yu000_12', 6)	# 134434-134439
    sprite('yu000_13', 6)	# 134440-134445
    sprite('yu000_14', 6)	# 134446-134451
    sprite('yu000_15', 6)	# 134452-134457
    gotoLabel(992)
    label(993)
    sprite('yu033_00', 2)	# 134458-134459

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
    sprite('yu033_01', 2)	# 134460-134461
    label(994)
    sprite('yu033_02', 3)	# 134462-134464
    sprite('yu033_01', 3)	# 134465-134467
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 134468-134470
    ExitState()
endState()

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
            if PartnerChar('bjb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('bph'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('yu610_00', 6)	# 4-9
    sprite('yu610_01', 6)	# 10-15
    sprite('yu610_02', 6)	# 16-21
    sprite('yu610_03', 10)	# 22-31
    sprite('yu610_04', 4)	# 32-35
    sprite('yu610_05', 4)	# 36-39
    SFX_3('hair')
    sprite('yu610_06', 8)	# 40-47
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pyu524', 100, 896891248, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pyu402_0', 100, 880114032, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pyu520', 100, 896891248, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('yu610_07', 6)	# 48-53
    sprite('yu610_08', 6)	# 54-59
    sprite('yu610_09', 6)	# 60-65
    label(0)
    sprite('yu610_10', 8)	# 66-73
    SFX_3('cloth_l')
    sprite('yu610_11', 8)	# 74-81
    sprite('yu610_12', 8)	# 82-89
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('yu611_00', 6)	# 90-95
    sprite('yu611_01', 6)	# 96-101
    sprite('yu611_02', 13)	# 102-114
    if (not SLOT_158):
        Unknown4054(2)
    Unknown4045('797565665f77696e66697265000000000000000000000000000000000000000000000000')
    SFX_3('blaze_short')
    sprite('yu611_03', 8)	# 115-122
    sprite('yu611_04', 13)	# 123-135
    sprite('yu611_05', 6)	# 136-141
    sprite('yu611_06', 6)	# 142-147
    SFX_3('yu001')
    sprite('yu611_07', 6)	# 148-153
    Unknown23029(11, 51, 0)
    sprite('yu611_08', 6)	# 154-159
    sprite('yu611_09', 6)	# 160-165
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pyu524', 100, 896891248, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pyu402_0', 100, 880114032, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pyu522', 100, 896891248, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(11)
    sprite('yu611_10', 8)	# 166-173
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 174-181
    sprite('yu611_12', 8)	# 182-189
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('yu000_00', 1)	# 190-190
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('yu000_00', 6)	# 191-196
    sprite('yu000_01', 6)	# 197-202
    sprite('yu000_02', 6)	# 203-208
    sprite('yu000_03', 6)	# 209-214
    sprite('yu000_04', 6)	# 215-220
    sprite('yu000_05', 6)	# 221-226
    sprite('yu000_06', 6)	# 227-232
    sprite('yu000_07', 6)	# 233-238
    sprite('yu000_08', 6)	# 239-244
    sprite('yu000_09', 6)	# 245-250
    sprite('yu000_10', 6)	# 251-256
    sprite('yu000_11', 6)	# 257-262
    sprite('yu000_12', 6)	# 263-268
    sprite('yu000_13', 6)	# 269-274
    sprite('yu000_14', 6)	# 275-280
    sprite('yu000_15', 6)	# 281-286
    gotoLabel(101)
    label(102)
    sprite('yu610_00', 6)	# 287-292
    sprite('yu610_01', 6)	# 293-298
    sprite('yu610_02', 6)	# 299-304
    sprite('yu610_03', 10)	# 305-314
    sprite('yu610_04', 4)	# 315-318
    sprite('yu610_05', 4)	# 319-322
    SFX_3('hair')
    sprite('yu610_06', 8)	# 323-330
    SFX_1('pyu701brc')
    sprite('yu610_07', 6)	# 331-336
    sprite('yu610_08', 6)	# 337-342
    sprite('yu610_09', 6)	# 343-348
    Unknown21011(120)
    label(103)
    sprite('yu610_10', 8)	# 349-356
    SFX_3('cloth_l')
    sprite('yu610_11', 8)	# 357-364
    sprite('yu610_12', 8)	# 365-372
    loopRest()
    gotoLabel(103)
    label(110)
    sprite('yu611_00', 6)	# 373-378
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
    sprite('yu611_01', 6)	# 379-384
    sprite('yu611_02', 13)	# 385-397
    if (not SLOT_158):
        Unknown4054(2)
    Unknown4045('797565665f77696e66697265000000000000000000000000000000000000000000000000')
    SFX_3('blaze_short')
    sprite('yu611_03', 8)	# 398-405
    sprite('yu611_04', 13)	# 406-418
    sprite('yu611_05', 6)	# 419-424
    sprite('yu611_06', 6)	# 425-430
    SFX_3('yu001')
    sprite('yu611_07', 6)	# 431-436
    Unknown23029(11, 51, 0)
    sprite('yu611_08', 6)	# 437-442
    sprite('yu611_09', 6)	# 443-448
    SFX_1('pyu700bjb')
    label(111)
    sprite('yu611_10', 8)	# 449-456
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 457-464
    sprite('yu611_12', 8)	# 465-472
    loopRest()
    if SLOT_97:
        _gotolabel(111)
    sprite('yu611_10', 8)	# 473-480
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 481-488
    sprite('yu611_12', 8)	# 489-496
    sprite('yu611_10', 1)	# 497-497
    Unknown21007(24, 40)
    Unknown21011(240)
    label(112)
    sprite('yu611_10', 8)	# 498-505
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 506-513
    sprite('yu611_12', 8)	# 514-521
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('yu611_00', 6)	# 522-527
    sprite('yu611_01', 6)	# 528-533
    sprite('yu611_02', 13)	# 534-546
    if (not SLOT_158):
        Unknown4054(2)
    Unknown4045('797565665f77696e66697265000000000000000000000000000000000000000000000000')
    SFX_3('blaze_short')
    sprite('yu611_03', 8)	# 547-554
    sprite('yu611_04', 13)	# 555-567
    sprite('yu611_05', 6)	# 568-573
    sprite('yu611_06', 6)	# 574-579
    SFX_3('yu001')
    sprite('yu611_07', 6)	# 580-585
    Unknown23029(11, 51, 0)
    sprite('yu611_08', 6)	# 586-591
    sprite('yu611_09', 6)	# 592-597
    SFX_1('pyu700pbc')
    label(121)
    sprite('yu611_10', 8)	# 598-605
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 606-613
    sprite('yu611_12', 8)	# 614-621
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('yu611_10', 8)	# 622-629
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 630-637
    sprite('yu611_12', 8)	# 638-645
    sprite('yu611_10', 1)	# 646-646
    Unknown21007(24, 40)
    Unknown21011(180)
    label(122)
    sprite('yu611_10', 8)	# 647-654
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 655-662
    sprite('yu611_12', 8)	# 663-670
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('yu000_00', 1)	# 671-671
    Unknown2034(0)
    Unknown2053(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('yu000_00', 6)	# 672-677
    sprite('yu000_01', 6)	# 678-683
    sprite('yu000_02', 6)	# 684-689
    sprite('yu000_03', 6)	# 690-695
    sprite('yu000_04', 6)	# 696-701
    sprite('yu000_05', 6)	# 702-707
    sprite('yu000_06', 6)	# 708-713
    sprite('yu000_07', 6)	# 714-719
    sprite('yu000_08', 6)	# 720-725
    sprite('yu000_09', 6)	# 726-731
    sprite('yu000_10', 6)	# 732-737
    sprite('yu000_11', 6)	# 738-743
    sprite('yu000_12', 6)	# 744-749
    sprite('yu000_13', 6)	# 750-755
    sprite('yu000_14', 6)	# 756-761
    sprite('yu000_15', 6)	# 762-767
    gotoLabel(131)
    label(132)
    sprite('yu611_00', 6)	# 768-773
    sprite('yu611_01', 6)	# 774-779
    sprite('yu611_02', 13)	# 780-792
    if (not SLOT_158):
        Unknown4054(2)
    Unknown4045('797565665f77696e66697265000000000000000000000000000000000000000000000000')
    SFX_3('blaze_short')
    sprite('yu611_03', 8)	# 793-800
    sprite('yu611_04', 13)	# 801-813
    sprite('yu611_05', 6)	# 814-819
    sprite('yu611_06', 6)	# 820-825
    SFX_3('yu001')
    sprite('yu611_07', 6)	# 826-831
    Unknown23029(11, 51, 0)
    sprite('yu611_08', 6)	# 832-837
    sprite('yu611_09', 6)	# 838-843
    SFX_1('pyu701pce_1')
    Unknown23018(1)
    label(133)
    sprite('yu611_10', 8)	# 844-851
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 852-859
    sprite('yu611_12', 8)	# 860-867
    loopRest()
    gotoLabel(133)
    label(140)
    sprite('yu611_00', 6)	# 868-873
    sprite('yu611_01', 6)	# 874-879
    sprite('yu611_02', 13)	# 880-892
    if (not SLOT_158):
        Unknown4054(2)
    Unknown4045('797565665f77696e66697265000000000000000000000000000000000000000000000000')
    SFX_3('blaze_short')
    sprite('yu611_03', 8)	# 893-900
    sprite('yu611_04', 13)	# 901-913
    sprite('yu611_05', 6)	# 914-919
    sprite('yu611_06', 6)	# 920-925
    SFX_3('yu001')
    sprite('yu611_07', 6)	# 926-931
    Unknown23029(11, 51, 0)
    sprite('yu611_08', 6)	# 932-937
    sprite('yu611_09', 6)	# 938-943
    SFX_1('pyu700pka')
    label(141)
    sprite('yu611_10', 8)	# 944-951
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 952-959
    sprite('yu611_12', 8)	# 960-967
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('yu611_10', 1)	# 968-968
    Unknown21007(24, 40)
    Unknown21011(200)
    label(142)
    sprite('yu611_10', 8)	# 969-976
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 977-984
    sprite('yu611_12', 8)	# 985-992
    loopRest()
    gotoLabel(142)
    label(150)
    sprite('yu000_00', 1)	# 993-993

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('yu000_00', 6)	# 994-999
    sprite('yu000_01', 6)	# 1000-1005
    sprite('yu000_02', 6)	# 1006-1011
    sprite('yu000_03', 6)	# 1012-1017
    sprite('yu000_04', 6)	# 1018-1023
    sprite('yu000_05', 6)	# 1024-1029
    sprite('yu000_06', 6)	# 1030-1035
    sprite('yu000_07', 6)	# 1036-1041
    sprite('yu000_08', 6)	# 1042-1047
    sprite('yu000_09', 6)	# 1048-1053
    sprite('yu000_10', 6)	# 1054-1059
    sprite('yu000_11', 6)	# 1060-1065
    sprite('yu000_12', 6)	# 1066-1071
    sprite('yu000_13', 6)	# 1072-1077
    sprite('yu000_14', 6)	# 1078-1083
    sprite('yu000_15', 6)	# 1084-1089
    gotoLabel(151)
    label(152)
    sprite('yu611_00', 6)	# 1090-1095
    sprite('yu611_01', 6)	# 1096-1101
    sprite('yu611_02', 13)	# 1102-1114
    if (not SLOT_158):
        Unknown4054(2)
    Unknown4045('797565665f77696e66697265000000000000000000000000000000000000000000000000')
    SFX_3('blaze_short')
    sprite('yu611_03', 8)	# 1115-1122
    sprite('yu611_04', 13)	# 1123-1135
    sprite('yu611_05', 6)	# 1136-1141
    sprite('yu611_06', 6)	# 1142-1147
    SFX_3('yu001')
    sprite('yu611_07', 6)	# 1148-1153
    Unknown23029(11, 51, 0)
    sprite('yu611_08', 6)	# 1154-1159
    sprite('yu611_09', 6)	# 1160-1165
    SFX_1('pyu701ugo')
    Unknown21011(180)
    label(153)
    sprite('yu611_10', 8)	# 1166-1173
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 1174-1181
    sprite('yu611_12', 8)	# 1182-1189
    loopRest()
    gotoLabel(153)
    label(160)
    sprite('yu610_00', 6)	# 1190-1195
    sprite('yu610_01', 6)	# 1196-1201
    sprite('yu610_02', 6)	# 1202-1207
    sprite('yu610_03', 10)	# 1208-1217
    sprite('yu610_04', 4)	# 1218-1221
    sprite('yu610_05', 4)	# 1222-1225
    SFX_3('hair')
    sprite('yu610_06', 8)	# 1226-1233
    SFX_1('pyu700rwi')
    sprite('yu610_07', 6)	# 1234-1239
    sprite('yu610_08', 6)	# 1240-1245
    sprite('yu610_09', 6)	# 1246-1251
    label(161)
    sprite('yu610_10', 8)	# 1252-1259
    SFX_3('cloth_l')
    sprite('yu610_11', 8)	# 1260-1267
    sprite('yu610_12', 8)	# 1268-1275
    loopRest()
    if SLOT_97:
        _gotolabel(161)
    sprite('yu610_10', 1)	# 1276-1276
    Unknown21007(24, 40)
    Unknown21011(120)
    label(162)
    sprite('yu610_10', 8)	# 1277-1284
    SFX_3('cloth_l')
    sprite('yu610_11', 8)	# 1285-1292
    sprite('yu610_12', 8)	# 1293-1300
    loopRest()
    gotoLabel(162)
    label(170)
    sprite('yu611_00', 6)	# 1301-1306
    sprite('yu611_01', 6)	# 1307-1312
    sprite('yu611_02', 13)	# 1313-1325
    if (not SLOT_158):
        Unknown4054(2)
    Unknown4045('797565665f77696e66697265000000000000000000000000000000000000000000000000')
    SFX_3('blaze_short')
    sprite('yu611_03', 8)	# 1326-1333
    sprite('yu611_04', 13)	# 1334-1346
    sprite('yu611_05', 6)	# 1347-1352
    sprite('yu611_06', 6)	# 1353-1358
    SFX_3('yu001')
    sprite('yu611_07', 6)	# 1359-1364
    Unknown23029(11, 51, 0)
    sprite('yu611_08', 6)	# 1365-1370
    sprite('yu611_09', 6)	# 1371-1376
    SFX_1('pyu700uca')
    label(171)
    sprite('yu611_10', 8)	# 1377-1384
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 1385-1392
    sprite('yu611_12', 8)	# 1393-1400
    loopRest()
    if SLOT_97:
        _gotolabel(171)
    sprite('yu611_10', 8)	# 1401-1408
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 1409-1416
    sprite('yu611_12', 8)	# 1417-1424
    Unknown21007(24, 40)
    Unknown21011(120)
    label(172)
    sprite('yu611_10', 8)	# 1425-1432
    SFX_3('cloth_l')
    sprite('yu611_11', 8)	# 1433-1440
    sprite('yu611_12', 8)	# 1441-1448
    loopRest()
    gotoLabel(172)
    label(180)
    sprite('yu000_00', 1)	# 1449-1449

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('yu000_00', 6)	# 1450-1455
    sprite('yu000_01', 6)	# 1456-1461
    sprite('yu000_02', 6)	# 1462-1467
    sprite('yu000_03', 6)	# 1468-1473
    sprite('yu000_04', 6)	# 1474-1479
    sprite('yu000_05', 6)	# 1480-1485
    sprite('yu000_06', 6)	# 1486-1491
    sprite('yu000_07', 6)	# 1492-1497
    sprite('yu000_08', 6)	# 1498-1503
    sprite('yu000_09', 6)	# 1504-1509
    sprite('yu000_10', 6)	# 1510-1515
    sprite('yu000_11', 6)	# 1516-1521
    sprite('yu000_12', 6)	# 1522-1527
    sprite('yu000_13', 6)	# 1528-1533
    sprite('yu000_14', 6)	# 1534-1539
    sprite('yu000_15', 6)	# 1540-1545
    gotoLabel(181)
    label(182)
    sprite('yu610_00', 6)	# 1546-1551
    sprite('yu610_01', 6)	# 1552-1557
    sprite('yu610_02', 6)	# 1558-1563
    sprite('yu610_03', 10)	# 1564-1573
    sprite('yu610_04', 4)	# 1574-1577
    sprite('yu610_05', 4)	# 1578-1581
    SFX_3('hair')
    sprite('yu610_06', 8)	# 1582-1589
    SFX_1('pyu701pla')
    sprite('yu610_07', 6)	# 1590-1595
    sprite('yu610_08', 6)	# 1596-1601
    sprite('yu610_09', 6)	# 1602-1607
    Unknown23018(1)
    label(183)
    sprite('yu610_10', 8)	# 1608-1615
    SFX_3('cloth_l')
    sprite('yu610_11', 8)	# 1616-1623
    sprite('yu610_12', 8)	# 1624-1631
    loopRest()
    gotoLabel(183)
    label(190)
    sprite('yu610_00', 6)	# 1632-1637
    sprite('yu610_01', 6)	# 1638-1643
    sprite('yu610_02', 6)	# 1644-1649
    sprite('yu610_03', 10)	# 1650-1659
    sprite('yu610_04', 4)	# 1660-1663
    sprite('yu610_05', 4)	# 1664-1667
    SFX_3('hair')
    sprite('yu610_06', 8)	# 1668-1675
    SFX_1('pyu700bph')
    sprite('yu610_07', 6)	# 1676-1681
    sprite('yu610_08', 6)	# 1682-1687
    sprite('yu610_09', 6)	# 1688-1693
    label(191)
    sprite('yu610_10', 8)	# 1694-1701
    SFX_3('cloth_l')
    sprite('yu610_11', 8)	# 1702-1709
    sprite('yu610_12', 8)	# 1710-1717
    loopRest()
    if SLOT_97:
        _gotolabel(191)
    sprite('yu610_10', 1)	# 1718-1718
    Unknown21007(24, 40)
    Unknown21011(240)
    label(192)
    sprite('yu610_10', 8)	# 1719-1726
    SFX_3('cloth_l')
    sprite('yu610_11', 8)	# 1727-1734
    sprite('yu610_12', 8)	# 1735-1742
    loopRest()
    gotoLabel(192)

@State
def CmnActLose():
    sprite('yu070_00', 6)	# 1-6
    if SLOT_158:
        if random_(2, 0, 50):
            SFX_1('pyu403_0')
        else:
            SFX_1('pyu403_1')
    Unknown23018(1)
    sprite('yu070_01', 6)	# 7-12
    sprite('yu070_02', 2)	# 13-14
    sprite('yu070_03', 32767)	# 15-32781
