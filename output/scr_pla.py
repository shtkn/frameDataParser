@Subroutine
def PreInit():
    Unknown12019('706c6100000000000000000000000000')

@Subroutine
def MatchInit():
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(2)
    Unknown13039(1)
    Unknown2049(1)
    Unknown23003(0, 1, 14, 1, 25000, 10000, -11010304, -65536)
    Unknown23003(1, 0, 0, 1, 180, 0, -1, -1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    Unknown14015(0, 450000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14013('NmlAtk5A4th')
    Unknown14015(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    Unknown15009()
    Unknown14015(0, 300000, -250000, 50000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    MoveMaxChainRepeat(1)
    Unknown14015(124000, 852000, -223000, 238000, 300, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(124000, 852000, -223000, 238000, 300, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B3rd', 0x19)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(124000, 852000, -223000, 238000, 300, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(4000)
    Unknown14015(-50000, 500000, -200000, 700000, 400, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown15021(1)
    Unknown15014(1)
    Unknown14015(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 500000, -200000, 0, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 200000, -250000, 50000, 1000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown14015(0, 300000, -250000, 300000, 1000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 300000, -350000, 300000, 2000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B2nd', 0x22)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5A2nd')
    Unknown14015(0, 300000, -250000, 300000, 1000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(0, 300000, -250000, 300000, 1000, 20)
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
    Move_Register('RocketPunchA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RocketPunchB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RocketPunchAB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RokepanDash', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RokepanDashB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('RokepanDash')
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RokepanDashC', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('RokepanDash')
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RokepanDash6', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('RokepanDash')
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RokepanHaseiA', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RokepanHaseiB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xa)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('RokepanHaseiAB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x13)
    Unknown14015(14000, 1800000, -27000, 95000, 50, 50)
    Move_EndRegister()
    Move_Register('AxeAttackA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15008()
    Unknown14015(0, 400000, -200000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('AxeAttackB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown14015(0, 400000, -200000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('AxeAttackAB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15008()
    Unknown14015(0, 400000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('AxeAttackAirA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 350000, -600000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('AxeAttackAirB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 350000, -600000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('AxeAttackAirAB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(0, 350000, -600000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(3000)
    Unknown14015(-50000, 300000, -100000, 350000, 400, 0)
    Move_EndRegister()
    Move_Register('UltimateTackle', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 649000, -113000, 92000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateTackleOD', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 649000, -113000, 92000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateFullswing', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 649000, -113000, 92000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateFullswingOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
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
    Unknown15024('NmlAtk5A3rd', 'RocketPunchA', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtk4A4th', 10000000)
    Unknown15024('NmlAtk4A3rd', 'RocketPunchB', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'RocketPunchB', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5B', 'AxeAttackAirA', 10000000)
    Unknown15024('NmlAtkAIR5B', 'AxeAttackAirAB', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AxeAttackAirB', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'NmlAtkAIR5B2nd', 10000000)
    Unknown15024('NmlAtkAIR5B2nd', 'NmlAtkAIR5B2nd', 10000000)
    Unknown15024('RocketPunchB', 'RokepanDash', 10000000)
    Unknown15024('RocketPunchAB', 'RokepanDash', 10000000)
    Unknown15024('RokepanDash', 'RokepanHaseiA', 10000000)
    Unknown15024('RokepanDash', 'RokepanHaseiB', 10000000)
    Unknown15024('RokepanDash', 'RokepanHaseiAB', 10000000)
    Unknown7010(0, 'pla000')
    Unknown7010(1, 'pla001')
    Unknown7010(2, 'pla002')
    Unknown7010(3, 'pla003')
    Unknown7010(4, 'pla004')
    Unknown7010(5, 'pla005')
    Unknown7010(6, 'pla006')
    Unknown7010(7, 'pla007')
    Unknown7010(8, 'pla008')
    Unknown7010(9, 'pla009')
    Unknown7010(10, 'pla010')
    Unknown7010(15, 'pla011')
    Unknown7010(16, 'pla012')
    Unknown7010(17, 'pla013')
    Unknown7010(18, 'pla014')
    Unknown7010(19, 'pla015')
    Unknown7010(20, 'pla016')
    Unknown7010(21, 'pla017')
    Unknown7010(22, 'pla018')
    Unknown7010(23, 'pla019')
    Unknown7010(24, 'pla020')
    Unknown7010(25, 'pla021')
    Unknown7010(28, 'pla022')
    Unknown7010(29, 'pla023')
    Unknown7010(30, 'pla024')
    Unknown7010(31, 'pla025')
    Unknown7010(32, 'pla026')
    Unknown7010(33, 'pla027')
    Unknown7010(34, 'pla028')
    Unknown7010(35, 'pla029')
    Unknown7010(36, 'pla030')
    Unknown7010(37, 'pla031')
    Unknown7010(39, 'pla032')
    Unknown7010(42, 'pla033')
    Unknown7010(43, 'pla034')
    Unknown7010(44, 'pla035')
    Unknown7010(45, 'pla036')
    Unknown7010(46, 'pla037')
    Unknown7010(47, 'pla038')
    Unknown7010(48, 'pla039')
    Unknown7010(49, 'pla040')
    Unknown7010(50, 'pla041')
    Unknown7010(52, 'pla042')
    Unknown7010(53, 'pla043')
    Unknown7010(54, 'pla100_0')
    Unknown7010(55, 'pla100_1')
    Unknown7010(56, 'pla100_2')
    Unknown7010(63, 'pla101_0')
    Unknown7010(64, 'pla101_1')
    Unknown7010(65, 'pla101_2')
    Unknown7010(57, 'pla102_0')
    Unknown7010(58, 'pla102_1')
    Unknown7010(59, 'pla102_2')
    Unknown7010(66, 'pla103_0')
    Unknown7010(67, 'pla103_1')
    Unknown7010(68, 'pla103_2')
    Unknown7010(60, 'pla104_0')
    Unknown7010(61, 'pla104_1')
    Unknown7010(62, 'pla104_2')
    Unknown7010(69, 'pla105_0')
    Unknown7010(70, 'pla105_1')
    Unknown7010(71, 'pla105_2')
    Unknown7010(72, 'pla150')
    Unknown7010(73, 'pla151')
    Unknown7010(74, 'pla152')
    Unknown7010(85, 'pla153')
    Unknown7010(87, 'pla154')
    Unknown7010(88, 'pla155')
    Unknown7010(96, 'pla161_0')
    Unknown7010(97, 'pla161_1')
    Unknown7010(92, 'pla162_0')
    Unknown7010(93, 'pla162_1')
    Unknown7010(98, 'pla163_0')
    Unknown7010(99, 'pla163_1')
    Unknown7010(100, 'pla164_0')
    Unknown7010(101, 'pla164_1')
    Unknown7010(105, 'pla165_0')
    Unknown7010(106, 'pla165_1')
    Unknown7010(102, 'pla166_0')
    Unknown7010(103, 'pla166_1')
    Unknown7010(90, 'pla167_0')
    Unknown7010(91, 'pla167_1')
    Unknown7010(107, 'pla168_0')
    Unknown7010(108, 'pla168_1')
    Unknown7010(110, 'pla169_0')
    Unknown7010(111, 'pla169_1')
    Unknown7010(94, 'pla400_0')
    Unknown7010(95, 'pla400_1')
    Unknown12018(0, 'la060_00')
    Unknown12018(1, 'la060_01')
    Unknown12018(2, 'la060_02')
    Unknown12018(3, 'la060_03')
    Unknown12018(4, 'la060_04')
    Unknown12018(5, 'la060_05')
    Unknown12018(6, 'la060_06')
    Unknown12018(7, 'la041_02')
    Unknown12018(8, 'la040_02')
    Unknown12018(9, 'la045_02')
    Unknown12018(10, 'la060_00')
    Unknown12018(11, 'la060_01')
    Unknown12018(12, 'la060_03')
    Unknown12018(13, 'la060_05')
    Unknown12018(14, 'la060_07')
    Unknown12018(15, 'la125_00')
    Unknown12018(16, 'la050_00')
    Unknown12018(17, 'la052_00')
    Unknown12018(18, 'la054_00')
    Unknown12018(19, 'la000_00')
    Unknown12018(20, 'la000_00')
    Unknown12018(25, 'la063_00')
    Unknown12018(26, 'la063_01')
    Unknown12018(27, 'la063_02')
    Unknown12018(28, 'la063_05')
    Unknown12018(29, 'la060_12')
    Unknown12018(24, 'la072_03')
    Unknown30036('504c415f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174655461636b6c65000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d6174655461636b6c654f4400000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746546756c6c7377696e67000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746546756c6c7377696e674f4400000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if SLOT_21:
        if (not SLOT_81):
            if (not SLOT_32):
                if (SLOT_31 >= 25000):
                    SLOT_32 = (SLOT_32 + 180)
                if (SLOT_31 >= 15000):
                    if (SLOT_6 == 3):
                        SLOT_32 = (SLOT_32 + 120)
                if (SLOT_31 >= 20000):
                    if (SLOT_6 == 4):
                        SLOT_32 = (SLOT_32 + 120)
            SLOT_32 = (SLOT_32 + (-1))
            if (SLOT_31 == 10000):
                SLOT_31 = (SLOT_31 + 0)
            if (SLOT_31 > 20000):
                if (not SLOT_32):
                    if SLOT_158:
                        SLOT_31 = (SLOT_31 + (-30))
                    else:
                        SLOT_31 = (SLOT_31 + (-20))
            elif (SLOT_31 > 15000):
                if (not SLOT_32):
                    if SLOT_158:
                        SLOT_31 = (SLOT_31 + (-20))
                    else:
                        SLOT_31 = (SLOT_31 + (-10))
            elif (SLOT_31 > 10000):
                if (not SLOT_32):
                    if SLOT_158:
                        SLOT_31 = (SLOT_31 + (-10))
                    else:
                        SLOT_31 = (SLOT_31 + (-10))
            if SLOT_30:
                if SLOT_158:
                    SLOT_31 = (SLOT_31 + (-20))
                else:
                    SLOT_31 = (SLOT_31 + (-10))
                SLOT_32 = (SLOT_32 + 0)
            elif (SLOT_31 < 10000):
                if SLOT_158:
                    SLOT_31 = (SLOT_31 + 50)
                else:
                    SLOT_31 = (SLOT_31 + 10)
            if SLOT_90:
                Unknown58('TRI_PLAAxeLv', 2, 67)
                if (SLOT_67 == 1):
                    SLOT_5 = 0
                    SLOT_31 = 0
                if (SLOT_67 == 2):
                    SLOT_5 = 1
                    SLOT_31 = 5000
                if (SLOT_67 == 3):
                    SLOT_5 = 2
                    SLOT_31 = 10000
                if (SLOT_67 == 4):
                    SLOT_5 = 3
                    SLOT_31 = 15000
                if (SLOT_67 == 5):
                    SLOT_5 = 4
                    SLOT_31 = 20000
            if (SLOT_31 >= 20000):
                SLOT_5 = 4
                Unknown23006(0, 16)
                Unknown23007(0, -65536)
                GFX_0('axe_level5', 0)
                Unknown26('axe_level4')
                Unknown26('axe_level3')
                Unknown26('axe_level2')
            elif (SLOT_31 >= 15000):
                SLOT_5 = 3
                Unknown23006(0, 15)
                Unknown23007(0, -256)
                GFX_0('axe_level4', 0)
                Unknown26('axe_level5')
                Unknown26('axe_level3')
                Unknown26('axe_level2')
            elif (SLOT_31 >= 10000):
                SLOT_5 = 2
                Unknown23006(0, 14)
                Unknown23007(0, -11010304)
                GFX_0('axe_level3', 0)
                Unknown26('axe_level5')
                Unknown26('axe_level4')
                Unknown26('axe_level2')
            elif (SLOT_31 >= 5000):
                SLOT_5 = 1
                Unknown23006(0, 13)
                Unknown23007(0, -16776961)
                GFX_0('axe_level2', 0)
                Unknown26('axe_level5')
                Unknown26('axe_level4')
                Unknown26('axe_level3')
            elif (SLOT_31 >= 0):
                SLOT_5 = 0
                Unknown23006(0, 12)
                Unknown23007(0, -5197648)
                Unknown26('axe_level5')
                Unknown26('axe_level4')
                Unknown26('axe_level3')
                Unknown26('axe_level2')
            if SLOT_42:
                Unknown26('axe_level5')
                Unknown26('axe_level4')
                Unknown26('axe_level3')
                Unknown26('axe_level2')
            if Unknown23148('CmnActTagBattleWait'):
                Unknown26('axe_level5')
                Unknown26('axe_level4')
                Unknown26('axe_level3')
                Unknown26('axe_level2')
            if Unknown23148('CmnActChangePartnerOut'):
                Unknown26('axe_level5')
                Unknown26('axe_level4')
                Unknown26('axe_level3')
                Unknown26('axe_level2')
            if Unknown23148('CmnActChangePartnerQuickOut'):
                Unknown26('axe_level5')
                Unknown26('axe_level4')
                Unknown26('axe_level3')
                Unknown26('axe_level2')
    else:
        Unknown26('axe_level5')
        Unknown26('axe_level4')
        Unknown26('axe_level3')
        Unknown26('axe_level2')
    if SLOT_170:
        Unknown23008(0, 0)

@Subroutine
def OnGuard():
    Unknown26('axe_level5')
    Unknown26('axe_level4')
    Unknown26('axe_level3')
    Unknown26('axe_level2')

@Subroutine
def OnDamage():
    SLOT_32 = 0
    SLOT_31 = (SLOT_31 + (-500))
    Unknown26('axe_level5')
    Unknown26('axe_level4')
    Unknown26('axe_level3')
    Unknown26('axe_level2')

@Subroutine
def AxeLvExp_Normal():

    def upon_45():
        if (not SLOT_81):
            if (SLOT_18 == 3):
                SLOT_31 = (SLOT_31 + 200)
            if (SLOT_18 >= 3):
                pass

    def upon_ON_HIT_OR_BLOCK():
        SLOT_31 = (SLOT_31 + 400)

    def upon_12():
        SLOT_31 = (SLOT_31 + 400)

    def upon_STATE_END():
        pass

@Subroutine
def AxeLvExp_Special():

    def upon_45():
        if (not SLOT_81):
            if (SLOT_18 == 3):
                SLOT_31 = (SLOT_31 + 300)
            if (SLOT_18 >= 3):
                pass

    def upon_ON_HIT_OR_BLOCK():
        SLOT_31 = (SLOT_31 + 600)

    def upon_12():
        SLOT_31 = (SLOT_31 + 600)

    def upon_STATE_END():
        pass

@Subroutine
def AxeLvExp_Ex():

    def upon_45():
        if (not SLOT_81):
            if (SLOT_18 == 3):
                SLOT_31 = (SLOT_31 + 400)
            if (SLOT_18 >= 3):
                pass

    def upon_ON_HIT_OR_BLOCK():
        SLOT_31 = (SLOT_31 + 800)

    def upon_12():
        SLOT_31 = (SLOT_31 + 800)

    def upon_STATE_END():
        pass

@Subroutine
def AxeLv_Powerup():
    if (SLOT_5 == 0):
        Unknown10000(90)
    if (SLOT_5 == 1):
        Unknown10000(95)
    if (SLOT_5 == 2):
        Unknown10000(100)
    if (SLOT_5 == 3):
        Unknown10000(120)
    if (SLOT_5 == 4):
        Unknown10000(150)

@Subroutine
def SkillDeriveInput():
    Unknown14070('RocketPunchA')
    Unknown14070('RocketPunchB')
    Unknown14070('RocketPunchAB')
    Unknown14070('AxeAttackA')
    Unknown14070('AxeAttackB')
    Unknown14070('AxeAttackAB')
    Unknown14070('UltimateTackle')
    Unknown14070('UltimateTackleOD')
    Unknown14070('UltimateFullswing')
    Unknown14070('UltimateFullswingOD')

@Subroutine
def SkillDeriveTiming():
    Unknown14072('RocketPunchA')
    Unknown14072('RocketPunchB')
    Unknown14072('RocketPunchAB')
    Unknown14072('AxeAttackA')
    Unknown14072('AxeAttackB')
    Unknown14072('AxeAttackAB')
    Unknown14072('UltimateTackle')
    Unknown14072('UltimateTackleOD')
    Unknown14072('UltimateFullswing')
    Unknown14072('UltimateFullswingOD')

@Subroutine
def SkillDeriveClear():
    Unknown14074('RocketPunchA')
    Unknown14074('RocketPunchB')
    Unknown14074('RocketPunchAB')
    Unknown14074('AxeAttackA')
    Unknown14074('AxeAttackB')
    Unknown14074('AxeAttackAB')
    Unknown14074('UltimateTackle')
    Unknown14074('UltimateTackleOD')
    Unknown14074('UltimateFullswing')
    Unknown14074('UltimateFullswingOD')

@Subroutine
def RocketPunch_Eff():
    GFX_0('laef401punch', 4)
    GFX_0('laef401punch_b', 4)
    GFX_1('laef_401_punch', 4)

@Subroutine
def RocketPunch_EffDel():
    Unknown26('laef401punch')
    Unknown26('laef401punch_b')
    Recovery()

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 == 3):
            Unknown14085('RokepanDash6')

@Subroutine
def RocketPunch_Atk():
    AttackLevel_(3)
    Unknown11033(1)
    AttackP1(80)
    GroundedHitstunAnimation(5)
    Unknown11001(0, 0, 0)
    Unknown9154(27)
    Unknown9156(27)
    AirUntechableTime(30)
    AirPushbackY(15000)
    AirPushbackX(10000)

@Subroutine
def RocketPunch_Bunki():

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        Unknown23086(1)
        if (not Unknown23148('RocketPunchA')):
            HitOrBlockCancel('RokepanDash6')
        if (SLOT_62 == 0):
            sendToLabel(0)
        if (SLOT_62 == 1):
            sendToLabel(1)
        if (SLOT_62 == 2):
            sendToLabel(2)
        if (SLOT_62 == 3):
            sendToLabel(3)
        if (SLOT_62 == 4):
            sendToLabel(4)
        if (SLOT_62 == 5):
            sendToLabel(5)
        if (SLOT_62 == 6):
            sendToLabel(6)

@State
def CmnActStand():
    label(0)
    sprite('la000_00', 6)	# 1-6
    sprite('la000_01', 6)	# 7-12
    sprite('la000_02', 6)	# 13-18
    sprite('la000_03', 6)	# 19-24
    sprite('la000_04', 6)	# 25-30
    sprite('la000_05', 6)	# 31-36
    sprite('la000_06', 6)	# 37-42
    sprite('la000_07', 6)	# 43-48
    sprite('la000_08', 6)	# 49-54
    sprite('la000_09', 6)	# 55-60
    sprite('la000_10', 6)	# 61-66
    sprite('la000_11', 6)	# 67-72
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
    sprite('la001_00', 6)	# 73-78
    SLOT_88 = 960
    sprite('la001_01', 6)	# 79-84
    sprite('la001_02', 6)	# 85-90
    sprite('la001_03', 6)	# 91-96
    sprite('la001_04', 6)	# 97-102
    sprite('la001_05', 6)	# 103-108
    GFX_0('laef001burner', 4)
    GFX_0('laef001burner_add', 4)
    GFX_0('laef001burner2', 5)
    GFX_0('laef001burner2_add', 5)
    GFX_0('laef001burner3', 6)
    GFX_0('laef001burner3_add', 6)
    GFX_0('laef001burner4', 7)
    GFX_0('laef001burner4_add', 7)
    GFX_0('laef001burner5', 8)
    GFX_0('laef001burner5_add', 8)
    GFX_0('laef001burner6', 9)
    GFX_0('laef001burner6_add', 9)
    SFX_3('la001')
    sprite('la001_06', 6)	# 109-114
    sprite('la001_07', 6)	# 115-120
    sprite('la001_08', 6)	# 121-126
    SFX_1('pla000')
    sprite('la001_05', 6)	# 127-132
    sprite('la001_06', 6)	# 133-138
    sprite('la001_07', 6)	# 139-144
    SFX_3('cloth_l')
    sprite('la001_08', 6)	# 145-150
    sprite('la001_05', 6)	# 151-156
    sprite('la001_06', 6)	# 157-162
    Unknown26('laef001burner')
    Unknown26('laef001burner_add')
    Unknown26('laef001burner2')
    Unknown26('laef001burner2_add')
    Unknown26('laef001burner3')
    Unknown26('laef001burner3_add')
    Unknown26('laef001burner4')
    Unknown26('laef001burner4_add')
    Unknown26('laef001burner5')
    Unknown26('laef001burner5_add')
    Unknown26('laef001burner6')
    Unknown26('laef001burner6_add')
    sprite('la001_07', 6)	# 163-168
    sprite('la001_08', 6)	# 169-174
    sprite('la001_04', 6)	# 175-180
    sprite('la001_03', 6)	# 181-186
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('la003_00', 4)	# 1-4
    sprite('la003_01', 4)	# 5-8
    sprite('la003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('la010_00', 4)	# 1-4
    sprite('la010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('la010_02', 6)	# 1-6
    sprite('la010_03', 6)	# 7-12
    sprite('la010_04', 6)	# 13-18
    sprite('la010_05', 6)	# 19-24
    sprite('la010_06', 6)	# 25-30
    sprite('la010_07', 6)	# 31-36
    sprite('la010_08', 6)	# 37-42
    sprite('la010_09', 6)	# 43-48
    sprite('la010_10', 6)	# 49-54
    sprite('la010_11', 6)	# 55-60
    sprite('la010_12', 6)	# 61-66
    sprite('la010_13', 6)	# 67-72
    loopRest()
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('la013_00', 4)	# 1-4
    sprite('la013_01', 4)	# 5-8
    sprite('la013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('la010_01', 4)	# 1-4
    sprite('la010_00', 4)	# 5-8

@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        SLOT_4 = 0
    sprite('la010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('la020_00', 4)	# 1-4
    sprite('la020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpper():
    label(0)
    sprite('la020_00', 4)	# 1-4
    sprite('la020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('la020_02', 3)	# 1-3
    sprite('la020_03', 3)	# 4-6
    sprite('la020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('la020_05', 3)	# 1-3
    sprite('la020_06', 3)	# 4-6
    label(0)
    sprite('la020_07', 4)	# 7-10
    sprite('la020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('la010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('la230_01', 2)	# 1-2
    sprite('la230_05', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('la230_05', 2)	# 1-2
    sprite('la230_01', 2)	# 3-4
    sprite('la230_00', 2)	# 5-6

@State
def CmnActFWalk():
    sprite('la030_00', 5)	# 1-5
    sprite('la030_01', 5)	# 6-10
    label(0)
    sprite('la030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('la030_03', 5)	# 16-20
    sprite('la030_04', 5)	# 21-25
    sprite('la030_05', 5)	# 26-30
    sprite('la030_06', 5)	# 31-35
    sprite('la030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('la030_08', 5)	# 41-45
    sprite('la030_09', 5)	# 46-50
    loopRest()
    gotoLabel(0)
    sprite('la030_00', 3)	# 51-53

@State
def CmnActBWalk():
    sprite('la031_00', 6)	# 1-6
    sprite('la031_01', 6)	# 7-12
    label(0)
    sprite('la031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('la031_03', 6)	# 19-24
    sprite('la031_04', 6)	# 25-30
    sprite('la031_05', 6)	# 31-36
    sprite('la031_06', 6)	# 37-42
    sprite('la031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('la031_08', 6)	# 49-54
    sprite('la031_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)
    sprite('la031_00', 3)	# 61-63

@State
def CmnActFDash():
    sprite('la032_00', 2)	# 1-2
    label(0)
    sprite('la032_01', 4)	# 3-6
    sprite('la032_02', 4)	# 7-10
    sprite('la032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('la032_04', 4)	# 15-18
    sprite('la032_05', 4)	# 19-22
    sprite('la032_06', 4)	# 23-26
    sprite('la032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('la032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('la032_09', 6)	# 1-6
    sprite('la032_10', 6)	# 7-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('la033_00', 2)	# 1-2
    sprite('la033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('la033_02', 3)	# 6-8
    sprite('la033_01', 3)	# 9-11
    sprite('la033_02', 3)	# 12-14
    label(0)
    sprite('la033_01', 3)	# 15-17
    sprite('la033_02', 3)	# 18-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('la033_03', 3)	# 21-23
    setInvincible(0)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('la033_04', 3)	# 24-26

@State
def CmnActAirTurn():
    sprite('la025_02', 1)	# 1-1
    sprite('la025_01', 2)	# 2-3
    sprite('la025_02', 1)	# 4-4

@State
def CmnActAirFDash():
    sprite('la035_00', 3)	# 1-3
    label(0)
    sprite('la035_01', 3)	# 4-6
    sprite('la035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    sprite('la035_00', 4)	# 10-13

@State
def CmnActAirBDash():
    sprite('la033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('la033_02', 3)	# 4-6
    sprite('la033_01', 3)	# 7-9
    sprite('la033_02', 3)	# 10-12
    sprite('la033_01', 3)	# 13-15
    sprite('la033_02', 3)	# 16-18
    sprite('la033_01', 3)	# 19-21
    sprite('la033_02', 3)	# 22-24
    sprite('la020_05', 3)	# 25-27
    sprite('la020_06', 3)	# 28-30
    label(0)
    sprite('la020_07', 4)	# 31-34
    sprite('la020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('la050_00', 1)	# 1-1
    sprite('la050_01', 1)	# 2-2
    sprite('la050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('la050_01', 1)	# 1-1
    sprite('la050_02', 1)	# 2-2
    sprite('la050_01', 2)	# 3-4
    sprite('la050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('la050_02', 1)	# 1-1
    sprite('la050_03', 1)	# 2-2
    sprite('la050_02', 2)	# 3-4
    sprite('la050_01', 2)	# 5-6
    sprite('la050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('la050_03', 1)	# 1-1
    sprite('la050_04', 1)	# 2-2
    sprite('la050_03', 2)	# 3-4
    sprite('la050_02', 2)	# 5-6
    sprite('la050_01', 2)	# 7-8
    sprite('la050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('la050_04', 1)	# 1-1
    sprite('la050_04', 1)	# 2-2
    sprite('la050_04', 2)	# 3-4
    sprite('la050_03', 2)	# 5-6
    sprite('la050_02', 2)	# 7-8
    sprite('la050_01', 2)	# 9-10
    sprite('la050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('la052_00', 1)	# 1-1
    sprite('la052_01', 1)	# 2-2
    sprite('la052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('la052_01', 1)	# 1-1
    sprite('la052_02', 1)	# 2-2
    sprite('la052_01', 2)	# 3-4
    sprite('la052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('la052_02', 1)	# 1-1
    sprite('la052_03', 1)	# 2-2
    sprite('la052_02', 2)	# 3-4
    sprite('la052_01', 2)	# 5-6
    sprite('la052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('la052_03', 1)	# 1-1
    sprite('la052_04', 1)	# 2-2
    sprite('la052_03', 2)	# 3-4
    sprite('la052_02', 2)	# 5-6
    sprite('la052_01', 2)	# 7-8
    sprite('la052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('la052_04', 1)	# 1-1
    sprite('la052_04', 1)	# 2-2
    sprite('la052_04', 2)	# 3-4
    sprite('la052_03', 2)	# 5-6
    sprite('la052_02', 2)	# 7-8
    sprite('la052_01', 2)	# 9-10
    sprite('la052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('la054_00', 1)	# 1-1
    sprite('la054_01', 1)	# 2-2
    sprite('la054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('la054_01', 1)	# 1-1
    sprite('la054_02', 1)	# 2-2
    sprite('la054_01', 2)	# 3-4
    sprite('la054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('la054_02', 1)	# 1-1
    sprite('la054_03', 1)	# 2-2
    sprite('la054_02', 2)	# 3-4
    sprite('la054_01', 2)	# 5-6
    sprite('la054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('la054_03', 1)	# 1-1
    sprite('la054_04', 1)	# 2-2
    sprite('la054_03', 2)	# 3-4
    sprite('la054_02', 2)	# 5-6
    sprite('la054_01', 2)	# 7-8
    sprite('la054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('la054_04', 1)	# 1-1
    sprite('la054_04', 1)	# 2-2
    sprite('la054_04', 2)	# 3-4
    sprite('la054_03', 2)	# 5-6
    sprite('la054_02', 2)	# 7-8
    sprite('la054_01', 2)	# 9-10
    sprite('la054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('la060_00', 4)	# 1-4
    label(0)
    sprite('la060_01', 4)	# 5-8
    sprite('la060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('la060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('la060_04', 8)	# 1-8
    label(1)
    sprite('la060_05', 4)	# 9-12
    sprite('la060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('la060_07', 6)	# 1-6

@State
def CmnActBDownLoop():
    sprite('la060_12', 3)	# 1-3

@State
def CmnActFDownUpper():
    sprite('la063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('la063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('la063_03', 4)	# 1-4
    sprite('la063_04', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('la063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('la060_08', 2)	# 1-2
    sprite('la060_09', 2)	# 3-4
    sprite('la060_10', 2)	# 5-6
    sprite('la060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('la060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('la064_00', 6)	# 1-6
    sprite('la064_01', 6)	# 7-12
    sprite('la064_02', 6)	# 13-18
    sprite('la064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('la060_00', 4)	# 1-4
    label(0)
    sprite('la060_01', 4)	# 5-8
    sprite('la060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('la060_03', 4)	# 1-4
    sprite('la060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('la060_04', 8)	# 1-8
    label(1)
    sprite('la060_05', 4)	# 9-12
    sprite('la060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActVDownCrash():
    sprite('la060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('la072_00', 3)	# 1-3
    sprite('la072_01', 3)	# 4-6
    sprite('la072_02', 3)	# 7-9
    label(0)
    sprite('la072_01', 3)	# 10-12
    sprite('la072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('la074_00', 2)	# 1-2
    sprite('la074_01', 2)	# 3-4
    sprite('la074_02', 2)	# 5-6
    sprite('la074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('la072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('la063_00', 3)	# 1-3
    label(0)
    sprite('la063_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('la082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('la052_01', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('la070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('la070_01', 8)	# 1-8
    sprite('la070_02', 2)	# 9-10
    sprite('la070_03', 28)	# 11-38
    sprite('la070_04', 6)	# 39-44
    sprite('la070_05', 6)	# 45-50
    sprite('la070_06', 6)	# 51-56

@State
def CmnActUkemiStagger():
    sprite('la040_03', 2)	# 1-2
    sprite('la040_02', 2)	# 3-4
    sprite('la040_01', 2)	# 5-6
    sprite('la040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('la020_02', 3)	# 1-3
    sprite('la020_03', 3)	# 4-6
    sprite('la020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('la020_02', 3)	# 1-3
    sprite('la020_03', 3)	# 4-6
    sprite('la020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('la020_02', 3)	# 1-3
    sprite('la020_03', 3)	# 4-6
    sprite('la020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('la112_00', 3)	# 1-3
    sprite('la112_01', 3)	# 4-6
    sprite('la112_02', 3)	# 7-9
    sprite('la112_03', 3)	# 10-12
    sprite('la112_04', 3)	# 13-15
    sprite('la112_05', 3)	# 16-18
    sprite('la020_07', 4)	# 19-22
    sprite('la020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandF():
    sprite('la112_00', 3)	# 1-3
    sprite('la112_01', 3)	# 4-6
    sprite('la112_02', 3)	# 7-9
    sprite('la112_03', 3)	# 10-12
    sprite('la112_04', 3)	# 13-15
    sprite('la112_05', 3)	# 16-18
    sprite('la020_07', 4)	# 19-22
    sprite('la020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('la112_00', 3)	# 1-3
    sprite('la112_01', 3)	# 4-6
    sprite('la112_02', 3)	# 7-9
    sprite('la112_03', 3)	# 10-12
    sprite('la112_04', 3)	# 13-15
    sprite('la112_05', 3)	# 16-18
    sprite('la020_07', 4)	# 19-22
    sprite('la020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('la010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('la040_00', 3)	# 1-3
    sprite('la040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('la040_02', 3)	# 1-3
    sprite('la040_03', 3)	# 4-6
    sprite('la040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('la040_01', 3)	# 1-3
    sprite('la040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('la040_05', 1)	# 1-1
    label(0)
    sprite('la040_02', 3)	# 2-4
    sprite('la040_03', 3)	# 5-7
    sprite('la040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('la040_01', 3)	# 1-3
    sprite('la040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('la040_00', 3)	# 1-3
    sprite('la040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('la040_05', 1)	# 1-1
    label(0)
    sprite('la040_02', 3)	# 2-4
    sprite('la040_03', 3)	# 5-7
    sprite('la040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('la040_01', 3)	# 1-3
    sprite('la040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('la040_05', 1)	# 1-1
    label(0)
    sprite('la040_02', 3)	# 2-4
    sprite('la040_03', 3)	# 5-7
    sprite('la040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('la040_01', 3)	# 1-3
    sprite('la040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('la043_00', 3)	# 1-3
    sprite('la043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('la043_02', 3)	# 1-3
    sprite('la043_03', 3)	# 4-6
    sprite('la043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('la043_01', 3)	# 1-3
    sprite('la043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('la043_05', 1)	# 1-1
    label(0)
    sprite('la043_02', 3)	# 2-4
    sprite('la043_03', 3)	# 5-7
    sprite('la043_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('la043_01', 3)	# 1-3
    sprite('la043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('la045_00', 3)	# 1-3
    sprite('la045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('la045_02', 3)	# 1-3
    sprite('la045_03', 3)	# 4-6
    sprite('la045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('la045_01', 3)	# 1-3
    sprite('la045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('la045_05', 1)	# 1-1
    label(0)
    sprite('la045_02', 3)	# 2-4
    sprite('la045_03', 3)	# 5-7
    sprite('la045_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('la045_01', 3)	# 1-3
    sprite('la045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('la040_04', 2)	# 1-2
    sprite('la040_04', 2)	# 3-4
    sprite('la040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('la040_02', 4)	# 6-9
    sprite('la040_01', 4)	# 10-13
    sprite('la040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('la043_04', 2)	# 1-2
    sprite('la043_04', 2)	# 3-4
    sprite('la043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('la043_02', 4)	# 6-9
    sprite('la043_01', 4)	# 10-13
    sprite('la043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('la045_04', 2)	# 1-2
    sprite('la045_04', 2)	# 3-4
    sprite('la045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('la045_02', 4)	# 6-9
    sprite('la045_01', 4)	# 10-13
    sprite('la045_00', 4)	# 14-17

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('la201_00', 4)	# 1-4
    sprite('la201_01', 2)	# 5-6
    sprite('la201_02', 2)	# 7-8
    sprite('la201_04', 3)	# 9-11	 **attackbox here**
    Unknown23054('6c613230315f303300000000000000000000000000000000000000000000000005000000')
    sprite('la201_05', 3)	# 12-14
    sprite('la201_06', 4)	# 15-18
    sprite('la201_07', 4)	# 19-22
    sprite('la201_08', 4)	# 23-26
    sprite('la201_09', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('la045_02', 1)	# 1-1
    sprite('la045_01', 3)	# 2-4
    sprite('la045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('la250_00', 5)	# 1-5
    sprite('la250_01', 8)	# 6-13
    sprite('la250_02', 2)	# 14-15
    sprite('la250_03', 4)	# 16-19	 **attackbox here**
    sprite('la250_04', 4)	# 20-23	 **attackbox here**
    sprite('la250_05', 6)	# 24-29
    Unknown2001()

@State
def CmnActLandSpin():
    sprite('la071_00', 2)	# 1-2
    label(0)
    sprite('la071_01', 2)	# 3-4
    sprite('la071_02', 2)	# 5-6
    sprite('la071_03', 2)	# 7-8
    sprite('la071_04', 2)	# 9-10
    sprite('la071_05', 2)	# 11-12
    sprite('la071_06', 2)	# 13-14
    sprite('la071_07', 2)	# 15-16
    sprite('la071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('la040_02', 3)	# 1-3
    sprite('la040_01', 3)	# 4-6
    sprite('la040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('la071_00', 2)	# 1-2
    label(0)
    sprite('la071_01', 2)	# 3-4
    sprite('la071_02', 2)	# 5-6
    sprite('la071_03', 2)	# 7-8
    sprite('la071_04', 2)	# 9-10
    sprite('la071_05', 2)	# 11-12
    sprite('la071_06', 2)	# 13-14
    sprite('la071_07', 2)	# 15-16
    sprite('la071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('la124_00', 2)	# 1-2
    label(0)
    sprite('la124_01', 2)	# 3-4
    sprite('la124_02', 2)	# 5-6
    sprite('la124_03', 2)	# 7-8
    sprite('la124_04', 2)	# 9-10
    sprite('la124_05', 2)	# 11-12
    sprite('la124_06', 2)	# 13-14
    sprite('la124_07', 2)	# 15-16
    sprite('la124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('la077_02', 4)	# 1-4
    label(0)
    sprite('la077_03', 3)	# 5-7
    sprite('la077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('la077_05', 5)	# 1-5
    sprite('la077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('la077_02', 4)	# 1-4
    label(0)
    sprite('la077_03', 3)	# 5-7
    sprite('la077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('la077_05', 5)	# 1-5
    sprite('la077_06', 4)	# 6-9

@State
def CmnActOverDriveBegin():
    sprite('la121_00', 2)	# 1-2
    sprite('la121_01', 2)	# 3-4
    sprite('la121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('la121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('la121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('la121_04', 2)	# 4-5
    sprite('la121_05', 2)	# 6-7
    sprite('la121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActOverDriveEnd():
    sprite('la121_07', 6)	# 1-6
    sprite('la010_00', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('la121_00', 2)	# 1-2
    sprite('la121_01', 2)	# 3-4
    sprite('la121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('la121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('la121_03', 3)	# 1-3
    label(1)
    sprite('la121_04', 2)	# 4-5
    sprite('la121_05', 2)	# 6-7
    sprite('la121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirOverDriveEnd():
    sprite('la121_07', 2)	# 1-2
    sprite('la121_08', 2)	# 3-4
    sprite('la020_04', 3)	# 5-7
    sprite('la020_05', 3)	# 8-10
    sprite('la020_06', 2)	# 11-12
    label(0)
    sprite('la020_07', 4)	# 13-16
    sprite('la020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('la121_00', 2)	# 1-2
    sprite('la121_01', 2)	# 3-4
    sprite('la121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PLA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 121, 0)
    sprite('la121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('la121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('la121_04', 2)	# 4-5
    sprite('la121_05', 2)	# 6-7
    sprite('la121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossRushEnd():
    sprite('la121_07', 2)	# 1-2
    sprite('la121_08', 2)	# 3-4
    sprite('la020_04', 2)	# 5-6
    sprite('la020_05', 2)	# 7-8
    sprite('la020_06', 2)	# 9-10
    sprite('la020_07', 2)	# 11-12

@State
def CmnActAirCrossRushBegin():
    sprite('la121_00', 2)	# 1-2
    sprite('la121_01', 2)	# 3-4
    sprite('la121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PLA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 121, 0)
    sprite('la121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('la121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('la121_04', 2)	# 4-5
    sprite('la121_05', 2)	# 6-7
    sprite('la121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossRushEnd():
    sprite('la121_07', 2)	# 1-2
    sprite('la121_08', 2)	# 3-4
    sprite('la020_04', 3)	# 5-7
    sprite('la020_05', 3)	# 8-10
    sprite('la020_06', 2)	# 11-12
    label(0)
    sprite('la020_07', 4)	# 13-16
    sprite('la020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    label(0)
    sprite('la121_00', 2)	# 1-2
    sprite('la121_01', 2)	# 3-4
    sprite('la121_02', 2)	# 5-6
    Unknown36(28)
    Unknown23148('PLA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 121, 0)
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('la121_03', 3)	# 1-3
    label(1)
    sprite('la121_04', 2)	# 4-5
    sprite('la121_05', 2)	# 6-7
    sprite('la121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossChangeEnd():
    sprite('la121_07', 3)	# 1-3
    sprite('la121_08', 3)	# 4-6
    sprite('la020_04', 3)	# 7-9
    sprite('la020_05', 3)	# 10-12
    sprite('la020_06', 3)	# 13-15
    sprite('la020_07', 4)	# 16-19
    sprite('la020_08', 4)	# 20-23
    loopRest()

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    label(0)
    sprite('la121_00', 2)	# 1-2
    sprite('la121_01', 2)	# 3-4
    sprite('la121_02', 2)	# 5-6
    Unknown36(28)
    Unknown23148('PLA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 121, 0)
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('la121_03', 3)	# 1-3
    label(1)
    sprite('la121_04', 2)	# 4-5
    sprite('la121_05', 2)	# 6-7
    sprite('la121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossChangeEnd():
    sprite('la121_07', 3)	# 1-3
    sprite('la121_08', 3)	# 4-6
    sprite('la020_04', 3)	# 7-9
    sprite('la020_05', 3)	# 10-12
    sprite('la020_06', 3)	# 13-15
    label(0)
    sprite('la020_07', 4)	# 16-19
    sprite('la020_08', 4)	# 20-23
    loopRest()
    gotoLabel(2)

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
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('la033_01', 3)	# 1-3
    sprite('la033_02', 3)	# 4-6
    sprite('la033_01', 3)	# 7-9
    sprite('la033_02', 3)	# 10-12
    sprite('la033_01', 3)	# 13-15
    sprite('la033_02', 3)	# 16-18
    sprite('la033_01', 3)	# 19-21
    sprite('la033_02', 3)	# 22-24
    sprite('la033_01', 3)	# 25-27
    sprite('la033_02', 3)	# 28-30
    sprite('la033_01', 30)	# 31-60

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
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('la000_00', 20)	# 1-20

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        Unknown17015()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('la000_00', 20)	# 1-20

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17015()
    sprite('la001_00', 7)	# 1-7
    sprite('la001_01', 7)	# 8-14
    sprite('la001_02', 7)	# 15-21
    sprite('la001_03', 9)	# 22-30
    sprite('la001_04', 5)	# 31-35
    sprite('la001_05', 5)	# 36-40
    sprite('la001_06', 10)	# 41-50
    sprite('la001_01', 5)	# 51-55
    sprite('la001_00', 5)	# 56-60
    loopRest()
    label(1)
    sprite('la600_12', 1)	# 61-61
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('la600_13', 3)	# 62-64
    sprite('la600_14', 3)	# 65-67
    sprite('la600_15', 3)	# 68-70
    sprite('la600_16', 3)	# 71-73

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('la450_01', 5)	# 1-5
    sprite('la450_02', 5)	# 6-10
    sprite('la450_03', 5)	# 11-15
    sprite('la450_04', 5)	# 16-20
    sprite('la450_05', 5)	# 21-25
    sprite('la450_06', 6)	# 26-31
    sprite('la450_07', 6)	# 32-37
    sprite('la450_08', 6)	# 38-43
    sprite('la450_06', 6)	# 44-49
    sprite('la450_07', 6)	# 50-55
    sprite('la450_08', 6)	# 56-61
    sprite('la450_09', 5)	# 62-66
    sprite('la450_10', 5)	# 67-71
    sprite('la450_11', 5)	# 72-76
    sprite('la000_00', 30)	# 77-106

@State
def CmnActChangePartnerQuickIn():
    sprite('la032_05', 3)	# 1-3
    sprite('la032_06', 5)	# 4-8
    sprite('la032_09', 7)	# 9-15
    sprite('la032_09', 7)	# 16-22
    sprite('la032_10', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('la033_00', 1)	# 1-1
    sprite('la033_01', 2)	# 2-3
    sprite('la033_01', 2)	# 4-5
    sprite('la033_02', 1)	# 6-6
    sprite('la033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('la033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('la033_03', 3)	# 13-15
    sprite('la033_04', 3)	# 16-18

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
    sprite('la405_08', 3)	# 121-123	 **attackbox here**
    SLOT_58 = 1
    Unknown1086(22)
    teleportRelativeX(-200000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    GFX_0('laef405burner', 4)
    GFX_0('laef405burner_add', 4)
    GFX_0('laef405burner2', 5)
    GFX_0('laef405burner2_add', 5)
    GFX_0('laef405burner3', 6)
    GFX_0('laef405burner3_add', 6)
    SFX_3('la001')
    SFX_3('airdash_m')
    label(1)
    sprite('la405_08', 3)	# 124-126	 **attackbox here**
    sprite('la405_09', 3)	# 127-129	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('la405_10', 3)	# 130-132
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    sprite('la405_11', 3)	# 133-135
    Unknown26('laef405burner')
    Unknown26('laef405burner2')
    Unknown26('laef405burner3')
    Unknown26('laef405burner_add')
    Unknown26('laef405burner2_add')
    Unknown26('laef405burner3_add')
    SFX_3('guard_hit_l')
    sprite('la405_12', 3)	# 136-138
    sprite('la405_13', 3)	# 139-141
    sprite('la405_14', 3)	# 142-144
    sprite('la405_15', 3)	# 145-147
    sprite('la405_16', 3)	# 148-150
    sprite('la405_17', 3)	# 151-153
    sprite('la405_18', 3)	# 154-156
    sprite('la405_19', 2)	# 157-158
    sprite('la405_20', 2)	# 159-160

@State
def CmnActChangeReturnAppealBurst():
    sprite('la064_02', 35)	# 1-35
    sprite('la064_03', 5)	# 36-40
    sprite('la010_02', 5)	# 41-45
    sprite('la010_01', 5)	# 46-50
    sprite('la010_00', 5)	# 51-55
    sprite('la000_00', 5)	# 56-60

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('la405_08', 3)	# 26-28	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-200000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    GFX_0('laef405burner', 4)
    GFX_0('laef405burner_add', 4)
    GFX_0('laef405burner2', 5)
    GFX_0('laef405burner2_add', 5)
    GFX_0('laef405burner3', 6)
    GFX_0('laef405burner3_add', 6)
    SFX_3('la001')
    SFX_3('airdash_m')
    label(1)
    sprite('la405_08', 3)	# 29-31	 **attackbox here**
    sprite('la405_09', 3)	# 32-34	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('la405_09', 3)	# 35-37	 **attackbox here**
    sprite('la405_10', 2)	# 38-39
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    sprite('la405_11', 2)	# 40-41
    Unknown26('laef405burner')
    Unknown26('laef405burner2')
    Unknown26('laef405burner3')
    Unknown26('laef405burner_add')
    Unknown26('laef405burner2_add')
    Unknown26('laef405burner3_add')
    SFX_3('guard_hit_l')
    sprite('la405_12', 3)	# 42-44
    sprite('la405_13', 3)	# 45-47
    sprite('la405_14', 3)	# 48-50
    sprite('la405_17', 3)	# 51-53
    sprite('la405_18', 2)	# 54-55
    sprite('la405_19', 2)	# 56-57
    sprite('la405_20', 2)	# 58-59

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
    sprite('la020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('la020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('la010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
        SLOT_58 = 1
        Unknown11063(1)
    sprite('la407_00', 3)	# 1-3
    sprite('la407_01', 5)	# 4-8
    Unknown21015('34303753686f745f5342000000000000000000000000000000000000000000003001000000000000')
    Unknown23029(11, 300, 0)
    Unknown7007('706c613231365f30000000000000000064000000706c613231365f31000000000000000064000000706c613231375f30000000000000000064000000706c613231375f31000000000000000064000000')
    sprite('la407_02', 5)	# 9-13
    sprite('la407_03', 5)	# 14-18
    GFX_1('persona_enter_ply', 1)
    sprite('la407_04', 4)	# 19-22
    sprite('la407_05', 4)	# 23-26
    sprite('la407_03', 5)	# 27-31
    sprite('la407_04', 4)	# 32-35
    sprite('la407_05', 4)	# 36-39
    sprite('la407_03', 5)	# 40-44
    sprite('la407_04', 4)	# 45-48
    sprite('la407_05', 4)	# 49-52
    sprite('la407_03', 5)	# 53-57
    sprite('la407_04', 4)	# 58-61
    sprite('la407_05', 4)	# 62-65
    sprite('la407_03', 5)	# 66-70
    sprite('la407_04', 4)	# 71-74
    sprite('la407_05', 4)	# 75-78
    sprite('la407_03', 5)	# 79-83
    sprite('la407_04', 4)	# 84-87
    sprite('la407_05', 4)	# 88-91
    sprite('la407_03', 5)	# 92-96
    sprite('la407_04', 4)	# 97-100
    sprite('la407_05', 4)	# 101-104
    sprite('la407_03', 4)	# 105-108
    sprite('la407_04', 3)	# 109-111
    sprite('la407_06', 2)	# 112-113

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirUntechableTime(60)
        AirPushbackX(3000)
        AirPushbackY(40000)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown11042(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
        SLOT_58 = 1
    sprite('la202_00', 3)	# 1-3
    sprite('la202_01', 4)	# 4-7
    sprite('la202_02', 4)	# 8-11
    sprite('la202_03', 3)	# 12-14
    Unknown7007('706c613331325f30000000000000000064000000706c613331325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la202_04', 3)	# 15-17	 **attackbox here**
    SFX_3('slash_blade_slow')
    RefreshMultihit()
    sprite('la202_05', 3)	# 18-20	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('la202_06', 4)	# 21-24
    sprite('la202_07', 8)	# 25-32
    sprite('la202_08', 6)	# 33-38
    sprite('la202_09', 6)	# 39-44

@State
def CmnActChangePartnerAssistAtk_C():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
        AttackLevel_(4)
        AttackP1(70)
        AirUntechableTime(60)
        AirPushbackX(7000)
        AirPushbackY(35000)
        GroundedHitstunAnimation(9)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11042(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
        SLOT_58 = 1
        Unknown11063(1)

        def upon_3():
            if (SLOT_19 < 200000):
                sendToLabel(0)
                clearUponHandler(3)
    sprite('la032_00', 3)	# 1-3
    sprite('la032_01', 2)	# 4-5
    physicsXImpulse(40000)
    sprite('la032_02', 3)	# 6-8
    Unknown8010(100, 1, 1)
    label(0)
    sprite('la203_00', 2)	# 9-10
    physicsXImpulse(30000)
    clearUponHandler(3)
    Unknown1019(90)
    Unknown11063(0)
    sprite('la203_01', 2)	# 11-12
    Unknown1019(90)
    SFX_3('cloth_l')
    sprite('la203_02', 2)	# 13-14
    sprite('la203_03', 2)	# 15-16
    sprite('la203_04', 2)	# 17-18
    sprite('la203_05', 2)	# 19-20
    Unknown1019(60)
    SFX_3('slash_blade_middle')
    sprite('la203_07', 2)	# 21-22	 **attackbox here**
    Unknown1019(80)
    Unknown23054('6c613230335f303600000000000000000000000000000000000000000000000004000000')
    RefreshMultihit()
    Unknown7007('706c613130355f32000000000000000064000000706c613130345f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown8010(100, 1, 1)
    sprite('la203_08', 6)	# 23-28
    Recovery()
    Unknown1084(1)
    sprite('la203_08', 6)	# 29-34
    sprite('la201_05', 4)	# 35-38
    sprite('la201_06', 4)	# 39-42
    sprite('la201_07', 4)	# 43-46
    sprite('la201_08', 4)	# 47-50
    sprite('la201_09', 5)	# 51-55

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
    Unknown2036(90, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-290000)
    Unknown1019(4)
    label(0)
    sprite('la020_07', 4)	# 3-6
    sprite('la020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateFullswingDDDOD')
    else:
        enterState('UltimateFullswingDDD')

@State
def UltimateFullswingDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2000)
        Hitstop(30)
        AirUntechableTime(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackX(50000)
        AirPushbackY(50000)
        Unknown11056(0)
        Unknown11068(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown30063(1)
        SLOT_58 = 1
        setInvincible(1)
    sprite('la432_00', 3)	# 1-3
    sprite('la432_00', 3)	# 4-6
    sprite('la432_01', 6)	# 7-12
    sprite('la432_02', 6)	# 13-18
    sprite('la432_03', 6)	# 19-24
    SFX_3('cloth_m')
    GFX_0('laef432_charge', 0)
    sprite('la432_04', 6)	# 25-30
    sprite('la432_05', 6)	# 31-36
    sprite('la432_03', 5)	# 37-41
    sprite('la432_04', 5)	# 42-46
    sprite('la432_05', 5)	# 47-51
    sprite('la432_06', 4)	# 52-55
    Unknown26('laef432_charge')
    sprite('la432_07', 1)	# 56-56
    physicsXImpulse(80000)
    SFX_3('airdash_m')
    SFX_3('slash_beam_slow')
    sprite('la432_08', 1)	# 57-57
    SFX_3('airdash_m')
    sprite('la432_09', 4)	# 58-61
    Unknown1019(30)
    SFX_3('la001')
    sprite('la432_10', 4)	# 62-65
    Unknown1019(50)
    SFX_3('slash_blade_slow')
    GFX_0('laef432_10_burner4', 7)
    GFX_0('laef432_10_burner5', 8)
    GFX_0('laef432_10_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_11', 3)	# 66-68	 **attackbox here**
    Unknown8006(100, 1, 1)
    Unknown1019(10)
    RefreshMultihit()
    Unknown7007('706c613236315f31000000000000000064000000706c613236315f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('laef432_10_burner4')
    Unknown26('laef432_10_burner5')
    Unknown26('laef432_10_burner6')
    GFX_0('laef432_11_burner', 4)
    GFX_0('laef432_11_burner2', 5)
    GFX_0('laef432_11_burner3', 6)
    GFX_0('laef432_11_burner4', 7)
    GFX_0('laef432_11_burner5', 8)
    GFX_0('laef432_11_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    GFX_0('laef432_fire', 8)
    GFX_1('laef_432_smoke', 100)
    SFX_3('la001')
    sprite('la432_12', 3)	# 69-71	 **attackbox here**
    physicsXImpulse(0)
    Unknown8006(100, 1, 1)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_13', 6)	# 72-77
    setInvincible(0)
    sprite('la432_14', 6)	# 78-83
    sprite('la432_15', 4)	# 84-87
    sprite('la432_16', 6)	# 88-93
    sprite('la432_17', 6)	# 94-99
    sprite('la201_05', 6)	# 100-105
    sprite('la201_06', 6)	# 106-111
    sprite('la201_07', 6)	# 112-117
    sprite('la201_08', 6)	# 118-123
    sprite('la432_18', 6)	# 124-129

@State
def UltimateFullswingDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2500)
        Hitstop(50)
        AirUntechableTime(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackX(50000)
        AirPushbackY(50000)
        Unknown11056(0)
        Unknown11068(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown30063(1)
        SLOT_58 = 1
        setInvincible(1)
    sprite('la432_00', 3)	# 1-3
    sprite('la432_00', 3)	# 4-6
    sprite('la432_01', 6)	# 7-12
    sprite('la432_02', 6)	# 13-18
    sprite('la432_03', 6)	# 19-24
    SFX_3('cloth_m')
    GFX_0('laef432_charge', 0)
    sprite('la432_04', 6)	# 25-30
    sprite('la432_05', 6)	# 31-36
    sprite('la432_03', 5)	# 37-41
    sprite('la432_04', 5)	# 42-46
    sprite('la432_05', 5)	# 47-51
    sprite('la432_06', 4)	# 52-55
    Unknown26('laef432_charge')
    sprite('la432_07', 1)	# 56-56
    physicsXImpulse(80000)
    SFX_3('airdash_m')
    SFX_3('slash_beam_slow')
    sprite('la432_08', 1)	# 57-57
    SFX_3('airdash_m')
    sprite('la432_09', 4)	# 58-61
    Unknown1019(30)
    SFX_3('la001')
    sprite('la432_10', 4)	# 62-65
    Unknown1019(50)
    SFX_3('slash_blade_slow')
    GFX_0('laef432_10_burner4', 7)
    GFX_0('laef432_10_burner5', 8)
    GFX_0('laef432_10_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_11', 3)	# 66-68	 **attackbox here**
    Unknown8006(100, 1, 1)
    Unknown1019(10)
    Unknown7007('706c613236315f31000000000000000064000000706c613236315f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    RefreshMultihit()
    Unknown26('laef432_10_burner4')
    Unknown26('laef432_10_burner5')
    Unknown26('laef432_10_burner6')
    GFX_0('laef432_11_burner', 4)
    GFX_0('laef432_11_burner2', 5)
    GFX_0('laef432_11_burner3', 6)
    GFX_0('laef432_11_burner4', 7)
    GFX_0('laef432_11_burner5', 8)
    GFX_0('laef432_11_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    GFX_0('laef432_fire', 8)
    GFX_1('laef_432_smoke', 100)
    SFX_3('la001')
    sprite('la432_12', 3)	# 69-71	 **attackbox here**
    physicsXImpulse(0)
    Unknown8006(100, 1, 1)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_13', 6)	# 72-77
    setInvincible(0)
    sprite('la432_14', 6)	# 78-83
    sprite('la432_15', 4)	# 84-87
    sprite('la432_16', 6)	# 88-93
    sprite('la432_17', 6)	# 94-99
    sprite('la201_05', 6)	# 100-105
    sprite('la201_06', 6)	# 106-111
    sprite('la201_07', 6)	# 112-117
    sprite('la201_08', 6)	# 118-123
    sprite('la432_18', 6)	# 124-129

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(12000)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('la203_00', 2)	# 1-2
    sprite('la203_01', 3)	# 3-5
    SFX_3('cloth_l')
    sprite('la203_04', 2)	# 6-7
    sprite('la203_05', 2)	# 8-9
    Unknown7007('706c613130325f32000000000000000064000000706c613130355f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_middle')
    sprite('la203_07', 2)	# 10-11	 **attackbox here**
    Unknown23054('6c613230335f303600000000000000000000000000000000000000000000000004000000')
    RefreshMultihit()
    sprite('la203_08', 2)	# 12-13
    sprite('la203_08', 2)	# 14-15
    Recovery()
    Unknown2063()
    sprite('la201_05', 4)	# 16-19
    sprite('la201_06', 4)	# 20-23
    sprite('la201_07', 4)	# 24-27
    sprite('la201_08', 4)	# 28-31
    sprite('la201_09', 3)	# 32-34

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(10000)
        PushbackX(19800)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('la207_00', 3)	# 1-3
    sprite('la207_01', 3)	# 4-6
    physicsXImpulse(8000)
    sprite('la207_01', 3)	# 7-9
    Unknown1019(500)
    sprite('la207_03', 3)	# 10-12	 **attackbox here**
    Unknown23054('6c613230375f303200000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Unknown1019(0)
    SFX_3('slash_blade_fast')
    Unknown7007('706c613130335f30000000000000000064000000706c613130335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la207_03', 3)	# 13-15	 **attackbox here**
    sprite('la207_04', 4)	# 16-19
    Recovery()
    Unknown2063()
    sprite('la207_05', 4)	# 20-23
    sprite('la207_06', 4)	# 24-27
    sprite('la207_07', 4)	# 28-31

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(13)
        AirPushbackX(12000)
        AirPushbackY(24000)
        AirUntechableTime(30)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        Unknown28(8, 'CmnActCrouch')
    sprite('la231_00', 1)	# 1-1
    sprite('la231_01', 2)	# 2-3
    sprite('la231_02', 3)	# 4-6
    SFX_3('cloth_l')
    sprite('la231_03', 2)	# 7-8
    sprite('la231_04', 2)	# 9-10
    sprite('la231_05', 2)	# 11-12
    physicsXImpulse(40000)
    sprite('la231_06', 1)	# 13-13
    Unknown1019(60)
    Unknown7009(2)
    sprite('la231_07', 2)	# 14-15
    Unknown1019(0)
    SFX_3('slash_blade_middle')
    sprite('la231_09', 4)	# 16-19	 **attackbox here**
    Unknown23054('6c613233315f303800000000000000000000000000000000000000000000000004000000')
    RefreshMultihit()
    sprite('la231_09', 6)	# 20-25	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('la231_10', 7)	# 26-32
    sprite('la231_11', 5)	# 33-37
    sprite('la211_12', 5)	# 38-42

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1000)
        AirPushbackY(-40000)
        PushbackX(12000)
        Hitstop(7)
        Unknown9016(1)
        Unknown9310(1)
        AirHitstunAnimation(9)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        Unknown11058('0100000000000000000000000000000000000000')
        JumpCancel_(0)
        sendToLabelUpon(2, 3)
    sprite('la208_00', 2)	# 1-2
    Unknown3029(1)
    sprite('la208_01', 2)	# 3-4
    sprite('la208_02', 4)	# 5-8
    Unknown8007(100, 1, 1)
    physicsYImpulse(15000)
    physicsXImpulse(12000)
    setGravity(1000)
    sprite('la208_03', 3)	# 9-11
    sprite('la208_04', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    sprite('la208_05', 3)	# 15-17
    sprite('la208_03', 3)	# 18-20
    sprite('la208_04', 3)	# 21-23	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    sprite('la208_05', 3)	# 24-26
    setGravity(2800)
    sprite('la208_06', 32767)	# 27-32793
    label(3)
    sprite('la208_08', 6)	# 32794-32799	 **attackbox here**
    Unknown23054('6c613230385f303700000000000000000000000000000000000000000000000006000000')
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    Hitstop(12)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    GFX_0('laef_405clash_l', 1)
    ScreenShake(0, 5000)
    Unknown7009(2)
    SFX_3('slash_blade_fast')
    SFX_3('guard_hit_l')
    sprite('la208_09', 4)	# 32800-32803
    Recovery()
    Unknown2063()
    Unknown3029(0)
    sprite('la208_10', 4)	# 32804-32807
    sprite('la208_11', 4)	# 32808-32811
    sprite('la208_12', 4)	# 32812-32815
    sprite('la208_13', 4)	# 32816-32819
    sprite('la208_14', 4)	# 32820-32823

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(1200)
        AirPushbackY(12000)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
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
    sprite('la200_00', 3)	# 1-3
    sprite('la200_01', 3)	# 4-6
    Unknown1051(80)
    Unknown7009(1)
    sprite('la200_03', 6)	# 7-12	 **attackbox here**
    Unknown23054('6c613230305f303200000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    sprite('la200_04', 6)	# 13-18
    Recovery()
    Unknown2063()
    sprite('la200_05', 6)	# 19-24
    sprite('la200_06', 4)	# 25-28

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('la201_00', 6)	# 1-6
    sprite('la201_01', 2)	# 7-8
    physicsXImpulse(20000)
    sprite('la201_02', 2)	# 9-10
    Unknown7009(1)
    sprite('la201_04', 3)	# 11-13	 **attackbox here**
    Unknown23054('6c613230315f303300000000000000000000000000000000000000000000000005000000')
    RefreshMultihit()
    Unknown1019(0)
    SFX_3('slash_blade_fast')
    sprite('la201_05', 4)	# 14-17
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('la201_06', 4)	# 18-21
    sprite('la201_07', 4)	# 22-25
    sprite('la201_08', 5)	# 26-30
    sprite('la201_09', 5)	# 31-35

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP2(75)
        GroundedHitstunAnimation(9)
        AirPushbackX(8000)
        AirUntechableTime(30)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        HitOrBlockCancel('NmlAtk4A4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('la202_00', 3)	# 1-3
    sprite('la202_01', 3)	# 4-6
    sprite('la202_02', 3)	# 7-9
    sprite('la202_03', 2)	# 10-11
    Unknown7009(2)
    sprite('la202_04', 4)	# 12-15	 **attackbox here**
    SFX_3('slash_blade_slow')
    RefreshMultihit()
    sprite('la202_05', 3)	# 16-18	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('la202_06', 4)	# 19-22
    sprite('la202_07', 8)	# 23-30
    sprite('la202_08', 6)	# 31-36
    sprite('la202_09', 4)	# 37-40

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('la230_00', 3)	# 1-3
    sprite('la230_01', 2)	# 4-5
    sprite('la230_02', 2)	# 6-7
    sprite('la230_03', 2)	# 8-9	 **attackbox here**
    RefreshMultihit()
    Unknown7009(0)
    SFX_3('hit_l_fast')
    sprite('la230_04', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('la230_05', 3)	# 13-15
    sprite('la230_01', 5)	# 16-20
    sprite('la230_00', 3)	# 21-23

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')

        def upon_43():
            if (SLOT_48 == 204):
                clearUponHandler(43)
                Unknown14070('NmlAtk5A')
                Unknown14070('NmlAtk5B2nd')
                Unknown14070('NmlAtk2B')
                Unknown14070('NmlAtk2C')
                Unknown14070('CmnActCrushAttack')
                callSubroutine('SkillDeriveInput')
        Unknown2063()
    sprite('la204_00', 4)	# 1-4
    sprite('la204_01', 4)	# 5-8
    Unknown23029(11, 202, 0)
    Unknown7007('706c613132305f30000000000000000064000000706c613132305f31000000000000000064000000706c613132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('la204_02', 4)	# 9-12
    GFX_1('persona_enter_ply', 0)
    sprite('la204_03', 4)	# 13-16
    sprite('la204_04', 4)	# 17-20
    sprite('la204_05', 4)	# 21-24
    sprite('la204_03', 4)	# 25-28
    SFX_3('cloth_m')
    sprite('la204_04', 4)	# 29-32
    sprite('la204_05', 4)	# 33-36
    sprite('la204_03', 4)	# 37-40
    sprite('la204_04', 4)	# 41-44
    Unknown14072('NmlAtk5A')
    Unknown14072('NmlAtk5B2nd')
    Unknown14072('NmlAtk2B')
    Unknown14072('NmlAtk2C')
    Unknown14072('CmnActCrushAttack')
    callSubroutine('SkillDeriveTiming')
    sprite('la204_05', 4)	# 45-48
    Recovery()
    sprite('la204_03', 4)	# 49-52
    Unknown14074('NmlAtk5A')
    Unknown14074('NmlAtk5B2nd')
    Unknown14074('NmlAtk2B')
    Unknown14074('NmlAtk2C')
    Unknown14074('CmnActCrushAttack')
    sprite('la204_04', 4)	# 53-56
    sprite('la204_05', 4)	# 57-60
    sprite('la204_03', 4)	# 61-64
    sprite('la204_04', 4)	# 65-68
    sprite('la204_06', 4)	# 69-72

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_43():
            if (SLOT_48 == 206):
                clearUponHandler(43)
                Unknown14070('NmlAtk5A')
                Unknown14070('NmlAtk2B')
                Unknown14070('NmlAtk2C')
                Unknown14070('CmnActCrushAttack')
                callSubroutine('SkillDeriveInput')
    sprite('la205_00', 3)	# 1-3
    Unknown23029(11, 205, 0)
    sprite('la205_01', 4)	# 4-7
    sprite('la205_02', 4)	# 8-11
    Unknown7007('706c613132345f30000000000000000064000000706c613132345f31000000000000000064000000706c613132305f32000000000000000064000000706c613132325f30000000000000000064000000')
    sprite('la205_03', 4)	# 12-15
    sprite('la205_04', 4)	# 16-19
    sprite('la205_05', 4)	# 20-23
    SFX_3('cloth_m')
    sprite('la205_03', 4)	# 24-27
    sprite('la205_04', 4)	# 28-31
    sprite('la205_05', 4)	# 32-35
    sprite('la205_03', 4)	# 36-39
    sprite('la205_04', 4)	# 40-43
    sprite('la205_05', 4)	# 44-47
    sprite('la205_03', 4)	# 48-51
    sprite('la205_04', 4)	# 52-55
    sprite('la205_05', 4)	# 56-59
    Unknown14072('NmlAtk5A')
    Unknown14072('NmlAtk2B')
    Unknown14072('NmlAtk2C')
    Unknown14072('CmnActCrushAttack')
    callSubroutine('SkillDeriveTiming')
    sprite('la205_03', 4)	# 60-63
    sprite('la205_04', 1)	# 64-64
    sprite('la205_04', 3)	# 65-67
    Recovery()
    sprite('la205_05', 4)	# 68-71
    sprite('la205_03', 4)	# 72-75
    Unknown14074('NmlAtk5A')
    Unknown14074('NmlAtk2B')
    Unknown14074('NmlAtk2C')
    Unknown14074('CmnActCrushAttack')
    sprite('la205_04', 4)	# 76-79
    sprite('la205_05', 4)	# 80-83
    sprite('la205_03', 4)	# 84-87
    sprite('la205_04', 4)	# 88-91
    sprite('la205_05', 4)	# 92-95
    sprite('la205_06', 6)	# 96-101
    sprite('la205_07', 6)	# 102-107

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_43():
            if (SLOT_48 == 206):
                clearUponHandler(43)
                WhiffCancelEnable(1)
                WhiffCancel('NmlAtk2C')
    sprite('la407_00', 3)	# 1-3
    sprite('la407_01', 5)	# 4-8
    Unknown23029(11, 205, 0)
    sprite('la407_02', 5)	# 9-13
    sprite('la407_03', 5)	# 14-18
    sprite('la407_04', 4)	# 19-22
    sprite('la407_05', 4)	# 23-26
    sprite('la407_03', 4)	# 27-30
    sprite('la407_04', 4)	# 31-34
    sprite('la407_05', 4)	# 35-38
    sprite('la407_03', 4)	# 39-42
    sprite('la407_04', 4)	# 43-46
    sprite('la407_05', 4)	# 47-50
    sprite('la407_03', 4)	# 51-54
    sprite('la407_04', 4)	# 55-58
    sprite('la407_05', 4)	# 59-62
    sprite('la407_03', 4)	# 63-66
    Recovery()
    sprite('la407_04', 4)	# 67-70
    sprite('la407_05', 4)	# 71-74
    WhiffCancelEnable(0)
    sprite('la407_03', 4)	# 75-78
    sprite('la407_04', 4)	# 79-82
    sprite('la407_05', 4)	# 83-86
    sprite('la407_03', 4)	# 87-90
    sprite('la407_04', 4)	# 91-94
    sprite('la407_06', 4)	# 95-98

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_43():
            if (SLOT_48 == 203):
                Unknown14070('NmlAtk5A')
                Unknown14070('NmlAtk5B')
                Unknown14070('NmlAtk2C')
                Unknown14070('CmnActCrushAttack')
                callSubroutine('SkillDeriveInput')
            if (SLOT_48 == 6001):
                Recovery()
                SLOT_51 = 256
    sprite('la232_00', 3)	# 1-3
    sprite('la232_01', 4)	# 4-7
    Unknown23029(11, 201, 0)
    Unknown7007('706c613331305f31000000000000000064000000706c613132315f31000000000000000064000000706c613132315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('la232_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('la232_03', 4)	# 12-15
    sprite('la232_04', 4)	# 16-19
    sprite('la232_05', 4)	# 20-23
    SFX_0('cloth_m')
    sprite('la232_03', 4)	# 24-27
    sprite('la232_04', 2)	# 28-29
    sprite('la232_04', 2)	# 30-31
    sprite('la232_05', 4)	# 32-35
    setInvincible(0)
    SFX_3('cloth_m')
    HitJumpCancel(1)
    Unknown14072('NmlAtk5A')
    Unknown14072('NmlAtk5B')
    Unknown14072('NmlAtk2C')
    Unknown14072('CmnActCrushAttack')
    callSubroutine('SkillDeriveTiming')
    sprite('la232_03', 5)	# 36-40
    sprite('la232_04', 5)	# 41-45
    Unknown14074('NmlAtk5A')
    Unknown14074('NmlAtk5B')
    Unknown14074('NmlAtk2C')
    Unknown14074('CmnActCrushAttack')
    sprite('la232_05', 5)	# 46-50
    sprite('la232_01', 5)	# 51-55
    sprite('la232_00', 4)	# 56-59

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirPushbackX(8000)
        AirPushbackY(18000)
        AirUntechableTime(30)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HitLow(2)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
    sprite('la211_00', 3)	# 1-3
    sprite('la211_01', 5)	# 4-8
    sprite('la211_02', 3)	# 9-11
    physicsXImpulse(20000)
    Unknown1045(20000)
    GFX_0('hibana2AB', 100)
    SFX_3('slash_blade_fast')
    sprite('la211_03', 3)	# 12-14
    SFX_3('la002')
    sprite('la211_04', 3)	# 15-17	 **attackbox here**
    Unknown1019(80)
    RefreshMultihit()
    Unknown7007('706c613130375f30000000000000000064000000706c613130375f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la211_05', 3)	# 18-20
    Unknown1019(80)
    Recovery()
    sprite('la211_06', 3)	# 21-23
    Unknown1019(80)
    sprite('la211_07', 3)	# 24-26
    Unknown1019(80)
    sprite('la211_08', 3)	# 27-29
    Unknown1019(80)
    sprite('la211_09', 3)	# 30-32
    Unknown1019(0)
    sprite('la211_10', 3)	# 33-35
    sprite('la211_11', 3)	# 36-38
    sprite('la211_12', 3)	# 39-41

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(1200)
        AirUntechableTime(17)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('la250_00', 3)	# 1-3
    sprite('la250_01', 3)	# 4-6
    sprite('la250_02', 2)	# 7-8
    SFX_3('hit_l_middle')
    Unknown7009(0)
    sprite('la250_04', 6)	# 9-14	 **attackbox here**
    Unknown23054('6c613235305f303300000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('la250_04', 4)	# 15-18	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('la250_05', 8)	# 19-26
    sprite('la020_05', 4)	# 27-30

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackX(8000)
        AirPushbackY(20000)
        AirUntechableTime(19)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('la251_00', 3)	# 1-3
    sprite('la251_01', 2)	# 4-5
    SFX_3('cloth_l')
    sprite('la251_05', 1)	# 6-6
    Unknown7009(2)
    sprite('la251_06', 1)	# 7-7
    sprite('la251_07', 1)	# 8-8
    SFX_3('slash_blade_middle')
    sprite('la251_08', 5)	# 9-13	 **attackbox here**
    RefreshMultihit()
    sprite('la251_09', 4)	# 14-17
    Recovery()
    Unknown2063()
    sprite('la251_10', 4)	# 18-21
    sprite('la251_11', 4)	# 22-25
    sprite('la251_12', 5)	# 26-30
    sprite('la251_13', 5)	# 31-35

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Normal')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B2nd')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('la252_00', 1)	# 1-1
    sprite('la252_01', 2)	# 2-3
    SFX_3('cloth_l')
    sprite('la252_02', 2)	# 4-5
    sprite('la252_03', 2)	# 6-7
    Unknown7009(1)
    SFX_3('slash_blade_slow')
    sprite('la252_04', 2)	# 8-9
    sprite('la252_05', 2)	# 10-11
    sprite('la252_06', 2)	# 12-13
    sprite('la252_07', 2)	# 14-15
    sprite('la252_09', 2)	# 16-17	 **attackbox here**
    Unknown23054('6c613235325f303800000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    sprite('la252_09ex', 2)	# 18-19	 **attackbox here**
    sprite('la252_10', 4)	# 20-23
    Recovery()
    Unknown2063()
    sprite('la252_11', 4)	# 24-27
    sprite('la252_12', 3)	# 28-30
    sprite('la252_13', 3)	# 31-33

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 221):
                JumpCancel_(1)
    sprite('la254_00', 6)	# 1-6
    sprite('la254_01', 4)	# 7-10
    Unknown23029(11, 207, 0)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown7007('706c613132335f30000000000000000064000000706c613132335f31000000000000000064000000706c613132335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('la254_02', 4)	# 11-14
    GFX_1('persona_enter_ply', 0)
    sprite('la254_03', 4)	# 15-18
    sprite('la254_04', 4)	# 19-22
    sprite('la254_05', 4)	# 23-26
    sprite('la254_03', 5)	# 27-31
    sprite('la254_04', 5)	# 32-36
    sprite('la254_05', 5)	# 37-41
    SFX_3('cloth_m')
    sprite('la254_03', 6)	# 42-47
    sprite('la254_04', 2)	# 48-49
    sprite('la254_04', 4)	# 50-53
    Recovery()
    sprite('la254_05', 6)	# 54-59
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(60)
    YAccel(60)
    Unknown1039(60)
    sprite('la254_06', 4)	# 60-63

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
        callSubroutine('AxeLvExp_Normal')
    sprite('la210_00', 3)	# 1-3
    sprite('la210_01', 3)	# 4-6
    sprite('la210_02', 3)	# 7-9
    sprite('la210_03', 3)	# 10-12
    sprite('la210_03', 3)	# 13-15
    sprite('la210_04', 2)	# 16-17
    sprite('la210_05', 2)	# 18-19
    sprite('la210_06', 2)	# 20-21
    Unknown7007('706c613135365f30000000000000000064000000706c613135365f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('la210_08', 3)	# 22-24	 **attackbox here**
    Unknown23054('6c613231305f303700000000000000000000000000000000000000000000000003000000')
    SFX_3('la003')
    sprite('la210_08', 5)	# 25-29	 **attackbox here**
    Unknown23027()
    sprite('la210_09', 5)	# 30-34
    sprite('la210_10', 5)	# 35-39
    sprite('la210_11', 5)	# 40-44
    sprite('la210_12', 4)	# 45-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        callSubroutine('AxeLvExp_Normal')
        Unknown23027()
        setGravity(3000)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('la210_08', 3)	# 1-3	 **attackbox here**
    sprite('la210_09', 6)	# 4-9
    sprite('la210_10', 4)	# 10-13
    sprite('la210_11', 4)	# 14-17
    sprite('la210_12', 4)	# 18-21
    sprite('la203_00', 2)	# 22-23
    sprite('la203_01', 2)	# 24-25
    SFX_3('cloth_l')
    sprite('la203_02', 2)	# 26-27
    sprite('la203_03', 1)	# 28-28
    sprite('la203_05', 1)	# 29-29
    tag_voice(1, 'pla157_0', 'pla157_1', '', '')
    SFX_3('slash_blade_middle')
    sprite('la203_07', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    Unknown23054('6c613230335f303600000000000000000000000000000000000000000000000004000000')
    sprite('la203_08', 3)	# 32-34
    sprite('la201_05', 3)	# 35-37
    sprite('la201_06', 3)	# 38-40
    sprite('la201_07', 3)	# 41-43
    sprite('la201_08', 3)	# 44-46
    sprite('la201_09', 3)	# 47-49
    sprite('la000_00', 6)	# 50-55
    sprite('la000_01', 6)	# 56-61
    sprite('la000_02', 6)	# 62-67
    sprite('la000_03', 6)	# 68-73
    sprite('la000_04', 6)	# 74-79
    sprite('la000_05', 6)	# 80-85
    sprite('la000_06', 6)	# 86-91
    sprite('la000_07', 6)	# 92-97
    sprite('la000_08', 6)	# 98-103
    sprite('la000_09', 6)	# 104-109
    sprite('la000_10', 6)	# 110-115
    sprite('la000_11', 6)	# 116-121
    label(10)
    sprite('la000_00', 6)	# 122-127
    sprite('la000_01', 6)	# 128-133
    sprite('la000_02', 6)	# 134-139
    sprite('la000_03', 6)	# 140-145
    sprite('la000_04', 6)	# 146-151
    sprite('la000_05', 6)	# 152-157
    sprite('la000_06', 6)	# 158-163
    sprite('la000_07', 6)	# 164-169
    sprite('la000_08', 6)	# 170-175
    sprite('la000_09', 6)	# 176-181
    sprite('la000_10', 6)	# 182-187
    sprite('la000_11', 6)	# 188-193
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 194-194

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        callSubroutine('AxeLvExp_Normal')
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('la202_00', 4)	# 1-4
    sprite('la202_01', 4)	# 5-8
    sprite('la202_02', 3)	# 9-11
    sprite('la202_03', 3)	# 12-14
    sprite('la202_04', 3)	# 15-17	 **attackbox here**
    SFX_3('slash_blade_slow')
    sprite('la202_05', 3)	# 18-20	 **attackbox here**
    sprite('la202_06', 2)	# 21-22
    sprite('la202_07', 5)	# 23-27
    sprite('la202_08', 4)	# 28-31
    sprite('la202_09', 4)	# 32-35
    sprite('la000_00', 6)	# 36-41
    sprite('la000_01', 6)	# 42-47
    sprite('la000_02', 6)	# 48-53
    sprite('la000_03', 6)	# 54-59
    sprite('la000_04', 6)	# 60-65
    sprite('la000_05', 6)	# 66-71
    sprite('la000_06', 6)	# 72-77
    sprite('la000_07', 6)	# 78-83
    sprite('la000_08', 6)	# 84-89
    sprite('la000_09', 6)	# 90-95
    sprite('la000_10', 6)	# 96-101
    sprite('la000_11', 6)	# 102-107
    label(0)
    sprite('la000_00', 6)	# 108-113
    sprite('la000_01', 6)	# 114-119
    sprite('la000_02', 6)	# 120-125
    sprite('la000_03', 6)	# 126-131
    sprite('la000_04', 6)	# 132-137
    sprite('la000_05', 6)	# 138-143
    sprite('la000_06', 6)	# 144-149
    sprite('la000_07', 6)	# 150-155
    sprite('la000_08', 6)	# 156-161
    sprite('la000_09', 6)	# 162-167
    sprite('la000_10', 6)	# 168-173
    sprite('la000_11', 6)	# 174-179
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 180-180

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
        callSubroutine('AxeLvExp_Normal')
    sprite('la400_00', 2)	# 1-2
    sprite('la400_01', 2)	# 3-4
    sprite('la400_02', 3)	# 5-7
    sprite('la400_03', 4)	# 8-11
    SFX_3('slash_blade_slow')
    sprite('la400_04', 2)	# 12-13
    tag_voice(0, 'pla158_0', 'pla158_1', '', '')
    SFX_3('slash_blade_fast')
    sprite('la400_05', 2)	# 14-15
    physicsXImpulse(40000)
    sprite('la400_06', 2)	# 16-17
    GFX_0('laef_swing', 1)
    SFX_3('la004')
    sprite('la400_07', 2)	# 18-19
    Unknown1019(50)
    sprite('la400_09', 1)	# 20-20	 **attackbox here**
    Unknown23054('6c613430305f303800000000000000000000000000000000000000000000000005000000')
    physicsXImpulse(0)
    SFX_3('la004')
    sprite('la400_09', 3)	# 21-23	 **attackbox here**
    sprite('la400_10', 3)	# 24-26
    sprite('la400_11', 3)	# 27-29
    sprite('la400_09', 4)	# 30-33	 **attackbox here**
    SFX_3('cloth_l')
    sprite('la400_10', 4)	# 34-37
    sprite('la400_11', 4)	# 38-41
    sprite('la400_09', 4)	# 42-45	 **attackbox here**
    sprite('la400_10', 4)	# 46-49
    sprite('la400_11', 4)	# 50-53
    sprite('la400_12', 4)	# 54-57
    sprite('la400_13', 4)	# 58-61
    sprite('la400_14', 4)	# 62-65

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
        callSubroutine('AxeLvExp_Normal')
    sprite('null', 27)	# 1-27
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 28-28
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1100000)
    Unknown1007(450000)
    SLOT_58 = 1
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('la020_05', 3)	# 29-31
    physicsXImpulse(40000)
    physicsYImpulse(-25000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('la020_06', 1)	# 32-32
    sprite('la252_00', 1)	# 33-33
    sprite('la252_01', 1)	# 34-34
    SFX_3('cloth_l')
    sprite('la252_02', 1)	# 35-35
    sprite('la252_03', 1)	# 36-36
    SFX_3('slash_blade_slow')
    sprite('la252_04', 1)	# 37-37
    sprite('la252_05', 1)	# 38-38
    sprite('la252_06', 1)	# 39-39
    sprite('la252_07', 2)	# 40-41
    sprite('la252_09', 2)	# 42-43	 **attackbox here**
    Unknown23054('6c613235325f303800000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    sprite('la252_09ex', 2)	# 44-45	 **attackbox here**
    sprite('la252_10', 4)	# 46-49
    sprite('la252_11', 4)	# 50-53
    sprite('la252_12', 3)	# 54-56
    sprite('la252_13', 3)	# 57-59
    label(2)
    sprite('la010_00', 3)	# 60-62
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('la000_00', 6)	# 63-68
    sprite('la000_01', 6)	# 69-74
    sprite('la000_02', 6)	# 75-80
    sprite('la000_03', 6)	# 81-86
    sprite('la000_04', 6)	# 87-92
    sprite('la000_05', 6)	# 93-98
    sprite('la000_06', 6)	# 99-104
    sprite('la000_07', 6)	# 105-110
    sprite('la000_08', 6)	# 111-116
    sprite('la000_09', 6)	# 117-122
    sprite('la000_10', 6)	# 123-128
    sprite('la000_11', 6)	# 129-134

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown23027()
        Unknown9016(1)
        callSubroutine('AxeLvExp_Normal')
        SLOT_58 = 1
    sprite('la404_01', 3)	# 1-3
    sprite('la404_02', 1)	# 4-4
    SFX_3('cloth_l')
    sprite('la404_05', 1)	# 5-5
    SFX_3('slash_blade_fast')
    sprite('la404_06', 1)	# 6-6
    sprite('la404_07', 1)	# 7-7	 **attackbox here**
    SFX_3('slash_blade_middle')
    sprite('la404_08', 1)	# 8-8	 **attackbox here**
    sprite('la404_09', 1)	# 9-9
    sprite('la404_10', 2)	# 10-11
    sprite('la404_12', 1)	# 12-12	 **attackbox here**
    Unknown23054('6c613430345f313100000000000000000000000000000000000000000000000006000000')
    RefreshMultihit()
    GFX_0('laef404clash', 7)
    GFX_0('laef404clash_r', 7)
    GFX_0('laef404burner', 4)
    GFX_0('laef404burner_add', 4)
    GFX_0('laef404burner2', 5)
    GFX_0('laef404burner2_add', 5)
    GFX_0('laef404burner3', 6)
    GFX_0('laef404burner3_add', 6)
    SFX_3('la001')
    SFX_3('la003')
    sprite('la404_12', 11)	# 13-23	 **attackbox here**
    sprite('la404_13', 4)	# 24-27
    Unknown26('laef404burner_add')
    Unknown26('laef404burner2_add')
    Unknown26('laef404burner3_add')
    Unknown26('laef404burner')
    Unknown26('laef404burner2')
    Unknown26('laef404burner3')
    sprite('la404_14', 4)	# 28-31
    Unknown2001()
    sprite('la404_15', 3)	# 32-34
    sprite('la404_16', 3)	# 35-37
    sprite('la404_17', 3)	# 38-40
    sprite('la000_00', 6)	# 41-46
    sprite('la000_01', 6)	# 47-52
    sprite('la000_02', 6)	# 53-58
    sprite('la000_03', 6)	# 59-64
    sprite('la000_04', 6)	# 65-70
    sprite('la000_05', 6)	# 71-76
    sprite('la000_06', 6)	# 77-82
    sprite('la000_07', 6)	# 83-88
    sprite('la000_08', 6)	# 89-94
    sprite('la000_09', 6)	# 95-100
    sprite('la000_10', 6)	# 101-106
    sprite('la000_11', 6)	# 107-112

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        callSubroutine('AxeLvExp_Normal')
        SLOT_58 = 1
    sprite('la400_00', 2)	# 1-2
    sprite('la400_01', 2)	# 3-4
    sprite('la400_02', 3)	# 5-7
    sprite('la400_03', 4)	# 8-11
    SFX_3('slash_blade_slow')
    sprite('la400_04', 2)	# 12-13
    SFX_3('slash_blade_fast')
    sprite('la400_05', 2)	# 14-15
    physicsXImpulse(40000)
    sprite('la400_06', 2)	# 16-17
    GFX_0('laef_swing', 1)
    SFX_3('la004')
    sprite('la400_07', 2)	# 18-19
    Unknown1019(50)
    sprite('la400_09', 1)	# 20-20	 **attackbox here**
    Unknown23054('6c613430305f303800000000000000000000000000000000000000000000000005000000')
    physicsXImpulse(0)
    SFX_3('la004')
    sprite('la400_09', 3)	# 21-23	 **attackbox here**
    sprite('la400_10', 3)	# 24-26
    sprite('la400_11', 3)	# 27-29
    sprite('la400_09', 4)	# 30-33	 **attackbox here**
    SFX_3('cloth_l')
    sprite('la400_10', 4)	# 34-37
    sprite('la400_11', 4)	# 38-41
    sprite('la400_09', 4)	# 42-45	 **attackbox here**
    sprite('la400_10', 4)	# 46-49
    sprite('la400_11', 4)	# 50-53
    sprite('la400_12', 4)	# 54-57
    sprite('la400_13', 4)	# 58-61
    sprite('la400_14', 4)	# 62-65

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
    sprite('la032_00', 2)	# 1-2
    label(0)
    sprite('la032_01', 4)	# 3-6
    sprite('la032_02', 4)	# 7-10
    sprite('la032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('la032_04', 4)	# 15-18
    sprite('la032_05', 4)	# 19-22
    sprite('la032_06', 4)	# 23-26
    sprite('la032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('la032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('la310_00', 3)	# 35-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('la310_01', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('la310_02', 5)	# 41-45
    SFX_4('pla154')
    sprite('la310_03', 9)	# 46-54
    sprite('la310_04', 5)	# 55-59
    sprite('la310_00', 4)	# 60-63

@State
def NmlAtkThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AirUntechableTime(50)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AttackP2(50)
        Unknown9310(45)
    sprite('la310_01', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('la311_00', 6)	# 4-9
    Unknown5000(25, 0)
    Unknown5001('0200000001000000010000000000000000000000')
    SFX_1('pla153')
    sprite('la311_01', 3)	# 10-12
    Unknown5000(25, 0)
    Unknown5001('0200000001000000010000000000000000000000')
    sprite('la311_02', 6)	# 13-18
    Unknown5000(29, 0)
    Unknown5001('0100000001000000010000000000000000000000')
    sprite('la311_03', 3)	# 19-21
    Unknown2018(1, 80)
    sprite('la311_04', 3)	# 22-24
    sprite('la311_05', 3)	# 25-27
    sprite('la311_06', 3)	# 28-30
    sprite('la311_07', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    AirPushbackY(-10000)
    Unknown9310(30)
    callSubroutine('AxeLvExp_Normal')
    ScreenShake(0, 25000)
    SFX_3('bound_marble_m')
    sprite('la311_08', 4)	# 34-37
    physicsXImpulse(-8000)
    physicsYImpulse(6000)
    setGravity(1000)
    sprite('la311_09', 4)	# 38-41
    sprite('la311_10', 4)	# 42-45
    sprite('la311_11', 4)	# 46-49
    sprite('la311_12', 4)	# 50-53
    Unknown1084(1)
    sprite('la311_13', 4)	# 54-57

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
    sprite('la032_00', 2)	# 1-2
    label(0)
    sprite('la032_01', 4)	# 3-6
    sprite('la032_02', 4)	# 7-10
    sprite('la032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('la032_04', 4)	# 15-18
    sprite('la032_05', 4)	# 19-22
    sprite('la032_06', 4)	# 23-26
    sprite('la032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('la032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('la310_00', 3)	# 35-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('la310_01', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('la310_02', 5)	# 41-45
    SFX_4('pla154')
    sprite('la310_03', 9)	# 46-54
    sprite('la310_04', 5)	# 55-59
    sprite('la310_00', 4)	# 60-63

@State
def NmlAtkBackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AirUntechableTime(50)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AttackP2(50)
        Unknown9310(45)
    sprite('la310_01', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('la311_00', 6)	# 4-9
    Unknown2005()
    Unknown5000(25, 0)
    Unknown5001('0200000001000000010000000000000000000000')
    SFX_1('pla153')
    sprite('la311_01', 3)	# 10-12
    Unknown5000(25, 0)
    Unknown5001('0200000001000000010000000000000000000000')
    sprite('la311_02', 6)	# 13-18
    Unknown5000(29, 0)
    Unknown5001('0100000001000000010000000000000000000000')
    sprite('la311_03', 3)	# 19-21
    Unknown2018(1, 80)
    sprite('la311_04', 3)	# 22-24
    sprite('la311_05', 3)	# 25-27
    sprite('la311_06', 3)	# 28-30
    sprite('la311_07', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    AirPushbackY(-10000)
    Unknown9310(30)
    callSubroutine('AxeLvExp_Normal')
    ScreenShake(0, 25000)
    SFX_3('bound_marble_m')
    sprite('la311_08', 4)	# 34-37
    physicsXImpulse(-8000)
    physicsYImpulse(6000)
    setGravity(1000)
    sprite('la311_09', 4)	# 38-41
    sprite('la311_10', 4)	# 42-45
    sprite('la311_11', 4)	# 46-49
    sprite('la311_12', 4)	# 50-53
    Unknown1084(1)
    sprite('la311_13', 4)	# 54-57

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2500)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackY(35000)
        AirPushbackX(10000)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')
        setInvincible(1)
        GuardPoint_(1)
    sprite('la400_00', 3)	# 1-3
    sprite('la400_01', 3)	# 4-6
    sprite('la400_02', 6)	# 7-12
    sprite('la400_03', 3)	# 13-15
    SFX_3('slash_blade_slow')
    sprite('la400_04', 2)	# 16-17
    Unknown7007('706c613230305f30000000000000000064000000706c613230305f31000000000000000064000000706c613230305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('la400_05', 2)	# 18-19
    physicsXImpulse(40000)
    sprite('la400_06', 2)	# 20-21
    GFX_0('laef_swing', 1)
    SFX_3('la004')
    sprite('la400_07', 2)	# 22-23
    Unknown1019(50)
    sprite('la400_09', 4)	# 24-27	 **attackbox here**
    Unknown23054('6c613430305f303800000000000000000000000000000000000000000000000005000000')
    RefreshMultihit()
    physicsXImpulse(0)
    ScreenShake(5000, 9000)
    SFX_3('la004')
    sprite('la400_10', 3)	# 28-30
    setInvincible(0)
    Unknown23027()
    sprite('la400_11', 3)	# 31-33
    sprite('la400_09', 4)	# 34-37	 **attackbox here**
    SFX_3('cloth_l')
    sprite('la400_10', 4)	# 38-41
    sprite('la400_11', 4)	# 42-45
    sprite('la400_09', 4)	# 46-49	 **attackbox here**
    sprite('la400_10', 4)	# 50-53
    sprite('la400_11', 4)	# 54-57
    sprite('la400_12', 6)	# 58-63
    sprite('la400_13', 6)	# 64-69
    sprite('la400_14', 6)	# 70-75

@State
def RocketPunchA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('RocketPunch_Atk')
        callSubroutine('RocketPunch_Bunki')

        def upon_STATE_END():
            Unknown7015()
    sprite('la401_00', 2)	# 1-2
    sprite('la401_01', 2)	# 3-4
    sprite('la401_02', 2)	# 5-6
    sprite('la401_03', 2)	# 7-8
    sprite('la401_04', 2)	# 9-10
    sprite('la401_06', 2)	# 11-12
    sprite('la401_07', 2)	# 13-14
    Unknown7007('706c613230315f30000000000000000064000000706c613230315f31000000000000000064000000706c613230315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('bomb_m')
    sprite('la401_08', 2)	# 15-16
    Unknown7014('la010')
    callSubroutine('RocketPunch_Eff')
    GFX_1('laef_401_launcher', 5)
    GFX_0('laef401smoke', 100)
    sprite('la401_09', 1)	# 17-17	 **attackbox here**
    SLOT_62 = 0
    callSubroutine('RocketPunch_Eff')
    GFX_0('laef401smoke_b', 100)
    sprite('la401_091', 1)	# 18-18	 **attackbox here**
    SLOT_62 = 1
    callSubroutine('RocketPunch_Eff')
    sprite('la401_114', 1)	# 19-19	 **attackbox here**
    SLOT_62 = 2
    callSubroutine('RocketPunch_Eff')
    sprite('la401_126', 1)	# 20-20	 **attackbox here**
    SLOT_62 = 3
    callSubroutine('RocketPunch_Eff')
    sprite('la401_108', 1)	# 21-21	 **attackbox here**
    SLOT_62 = 4
    callSubroutine('RocketPunch_Eff')
    sprite('la401_138', 3)	# 22-24
    Recovery()
    SFX_3('chain_snap')
    GFX_0('laef401punch', 4)
    GFX_0('laef401punch_b', 4)
    sprite('la401_156', 1)	# 25-25
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_164', 1)	# 26-26
    sprite('la401_142', 1)	# 27-27
    sprite('la401_140', 1)	# 28-28
    loopRest()
    gotoLabel(99)
    label(0)
    sprite('la401_13', 3)	# 29-31
    callSubroutine('RocketPunch_EffDel')
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('la401_130', 3)	# 32-34
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_140', 1)	# 35-35
    loopRest()
    gotoLabel(99)
    label(2)
    sprite('la401_133', 3)	# 36-38
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_142', 1)	# 39-39
    sprite('la401_140', 1)	# 40-40
    loopRest()
    gotoLabel(99)
    label(3)
    sprite('la401_135', 3)	# 41-43
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_144', 1)	# 44-44
    sprite('la401_142', 1)	# 45-45
    sprite('la401_140', 1)	# 46-46
    loopRest()
    gotoLabel(99)
    label(4)
    sprite('la401_137', 3)	# 47-49
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_146', 1)	# 50-50
    sprite('la401_144', 1)	# 51-51
    sprite('la401_142', 1)	# 52-52
    sprite('la401_140', 1)	# 53-53
    label(99)
    sprite('la401_16', 2)	# 54-55
    sprite('la401_17', 2)	# 56-57
    GFX_1('laef_401_attachment', 4)
    Unknown7015()
    sprite('la401_18', 2)	# 58-59
    sprite('la401_19', 2)	# 60-61
    sprite('la401_04', 2)	# 62-63
    sprite('la401_03', 2)	# 64-65
    sprite('la401_02', 2)	# 66-67
    sprite('la401_01', 2)	# 68-69
    sprite('la401_00', 2)	# 70-71

@State
def RocketPunchB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('RocketPunch_Atk')
        callSubroutine('RocketPunch_Bunki')

        def upon_STATE_END():
            Unknown7015()
    sprite('la401_00', 3)	# 1-3
    sprite('la401_01', 3)	# 4-6
    sprite('la401_02', 3)	# 7-9
    sprite('la401_03', 3)	# 10-12
    sprite('la401_04', 3)	# 13-15
    sprite('la401_05', 3)	# 16-18
    sprite('la401_06', 2)	# 19-20
    sprite('la401_07', 2)	# 21-22
    Unknown7007('706c613230365f30000000000000000064000000706c613230365f31000000000000000064000000706c613230365f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('bomb_m')
    sprite('la401_08', 2)	# 23-24
    Unknown7014('la010')
    callSubroutine('RocketPunch_Eff')
    GFX_1('laef_401_launcher', 5)
    GFX_0('laef401smoke', 100)
    sprite('la401_09', 1)	# 25-25	 **attackbox here**
    RefreshMultihit()
    SLOT_62 = 0
    callSubroutine('RocketPunch_Eff')
    GFX_0('laef401smoke_b', 100)
    sprite('la401_091', 1)	# 26-26	 **attackbox here**
    SLOT_62 = 1
    callSubroutine('RocketPunch_Eff')
    sprite('la401_114', 1)	# 27-27	 **attackbox here**
    SLOT_62 = 2
    callSubroutine('RocketPunch_Eff')
    sprite('la401_126', 1)	# 28-28	 **attackbox here**
    SLOT_62 = 3
    callSubroutine('RocketPunch_Eff')
    sprite('la401_108', 1)	# 29-29	 **attackbox here**
    SLOT_62 = 4
    callSubroutine('RocketPunch_Eff')
    sprite('la401_11a', 1)	# 30-30	 **attackbox here**
    SLOT_62 = 5
    callSubroutine('RocketPunch_Eff')
    sprite('la401_12c', 1)	# 31-31	 **attackbox here**
    SLOT_62 = 6
    callSubroutine('RocketPunch_Eff')
    sprite('la401_13c', 3)	# 32-34
    Recovery()
    SFX_3('chain_snap')
    GFX_0('laef401punch', 4)
    GFX_0('laef401punch_b', 4)
    sprite('la401_14a', 1)	# 35-35
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_148', 1)	# 36-36
    sprite('la401_146', 1)	# 37-37
    sprite('la401_144', 1)	# 38-38
    sprite('la401_142', 1)	# 39-39
    sprite('la401_140', 1)	# 40-40
    loopRest()
    gotoLabel(99)
    label(0)
    sprite('la401_13', 3)	# 41-43
    callSubroutine('RocketPunch_EffDel')
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('la401_131', 3)	# 44-46
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_140', 1)	# 47-47
    loopRest()
    gotoLabel(99)
    label(2)
    sprite('la401_133', 3)	# 48-50
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_142', 1)	# 51-51
    sprite('la401_140', 1)	# 52-52
    loopRest()
    gotoLabel(99)
    label(3)
    sprite('la401_135', 3)	# 53-55
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_144', 1)	# 56-56
    sprite('la401_142', 1)	# 57-57
    sprite('la401_140', 1)	# 58-58
    loopRest()
    gotoLabel(99)
    label(4)
    sprite('la401_137', 3)	# 59-61
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_146', 1)	# 62-62
    sprite('la401_144', 1)	# 63-63
    sprite('la401_142', 1)	# 64-64
    sprite('la401_140', 1)	# 65-65
    loopRest()
    gotoLabel(99)
    label(5)
    sprite('la401_139', 3)	# 66-68
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_148', 1)	# 69-69
    sprite('la401_146', 1)	# 70-70
    sprite('la401_144', 1)	# 71-71
    sprite('la401_142', 1)	# 72-72
    sprite('la401_140', 1)	# 73-73
    loopRest()
    gotoLabel(99)
    label(6)
    sprite('la401_13b', 3)	# 74-76
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_14a', 1)	# 77-77
    sprite('la401_148', 1)	# 78-78
    sprite('la401_146', 1)	# 79-79
    sprite('la401_144', 1)	# 80-80
    sprite('la401_142', 1)	# 81-81
    sprite('la401_140', 1)	# 82-82
    label(99)
    sprite('la401_16', 2)	# 83-84
    sprite('la401_17', 2)	# 85-86
    GFX_1('laef_401_attachment', 4)
    Unknown7015()
    sprite('la401_18', 2)	# 87-88
    sprite('la401_19', 2)	# 89-90
    sprite('la401_04', 2)	# 91-92
    sprite('la401_03', 2)	# 93-94
    sprite('la401_02', 2)	# 95-96
    sprite('la401_01', 2)	# 97-98
    sprite('la401_00', 2)	# 99-100

@State
def RocketPunchAB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('RocketPunch_Atk')
        AirPushbackY(20000)
        Unknown11091(10)
        Unknown30065(0)
        callSubroutine('RocketPunch_Bunki')

        def upon_STATE_END():
            Unknown7015()
    sprite('la401_00', 2)	# 1-2
    sprite('la401_01', 1)	# 3-3
    sprite('la401_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('la401_02', 2)	# 5-6
    sprite('la401_03', 2)	# 7-8
    sprite('la401_04', 2)	# 9-10
    sprite('la401_06', 2)	# 11-12
    sprite('la401_07', 2)	# 13-14
    Unknown7007('706c613230365f30000000000000000064000000706c613230365f31000000000000000064000000706c613230365f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('bomb_m')
    sprite('la401_08', 2)	# 15-16
    Unknown7014('la010')
    callSubroutine('RocketPunch_Eff')
    GFX_1('laef_401_launcher', 5)
    GFX_0('laef401smoke', 100)
    sprite('la401_09', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    SLOT_62 = 0
    callSubroutine('RocketPunch_Eff')
    GFX_0('laef401smoke_b', 100)
    sprite('la401_091', 1)	# 18-18	 **attackbox here**
    SLOT_62 = 1
    callSubroutine('RocketPunch_Eff')
    sprite('la401_114', 1)	# 19-19	 **attackbox here**
    SLOT_62 = 2
    callSubroutine('RocketPunch_Eff')
    sprite('la401_126', 1)	# 20-20	 **attackbox here**
    SLOT_62 = 3
    callSubroutine('RocketPunch_Eff')
    sprite('la401_108', 1)	# 21-21	 **attackbox here**
    SLOT_62 = 4
    callSubroutine('RocketPunch_Eff')
    sprite('la401_11a', 1)	# 22-22	 **attackbox here**
    SLOT_62 = 5
    callSubroutine('RocketPunch_Eff')
    sprite('la401_12c', 1)	# 23-23	 **attackbox here**
    SLOT_62 = 6
    callSubroutine('RocketPunch_Eff')
    sprite('la401_13c', 3)	# 24-26
    Recovery()
    SFX_3('chain_snap')
    GFX_0('laef401punch', 4)
    GFX_0('laef401punch_b', 4)
    sprite('la401_14a', 1)	# 27-27
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_148', 1)	# 28-28
    sprite('la401_146', 1)	# 29-29
    sprite('la401_144', 1)	# 30-30
    sprite('la401_142', 1)	# 31-31
    sprite('la401_140', 1)	# 32-32
    loopRest()
    gotoLabel(99)
    label(0)
    sprite('la401_13', 3)	# 33-35
    callSubroutine('RocketPunch_EffDel')
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('la401_131', 3)	# 36-38
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_140', 1)	# 39-39
    loopRest()
    gotoLabel(99)
    label(2)
    sprite('la401_133', 3)	# 40-42
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_142', 1)	# 43-43
    sprite('la401_140', 1)	# 44-44
    loopRest()
    gotoLabel(99)
    label(3)
    sprite('la401_135', 3)	# 45-47
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_144', 1)	# 48-48
    sprite('la401_142', 1)	# 49-49
    sprite('la401_140', 1)	# 50-50
    loopRest()
    gotoLabel(99)
    label(4)
    sprite('la401_137', 3)	# 51-53
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_146', 1)	# 54-54
    sprite('la401_144', 1)	# 55-55
    sprite('la401_142', 1)	# 56-56
    sprite('la401_140', 1)	# 57-57
    loopRest()
    gotoLabel(99)
    label(5)
    sprite('la401_139', 3)	# 58-60
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_148', 1)	# 61-61
    sprite('la401_146', 1)	# 62-62
    sprite('la401_144', 1)	# 63-63
    sprite('la401_142', 1)	# 64-64
    sprite('la401_140', 1)	# 65-65
    loopRest()
    gotoLabel(99)
    label(6)
    sprite('la401_13b', 3)	# 66-68
    callSubroutine('RocketPunch_EffDel')
    sprite('la401_14a', 1)	# 69-69
    sprite('la401_148', 1)	# 70-70
    sprite('la401_146', 1)	# 71-71
    sprite('la401_144', 1)	# 72-72
    sprite('la401_142', 1)	# 73-73
    sprite('la401_140', 1)	# 74-74
    label(99)
    sprite('la401_16', 2)	# 75-76
    sprite('la401_17', 2)	# 77-78
    GFX_1('laef_401_attachment', 4)
    Unknown7015()
    sprite('la401_18', 2)	# 79-80
    sprite('la401_19', 2)	# 81-82
    sprite('la401_04', 2)	# 83-84
    sprite('la401_03', 2)	# 85-86
    sprite('la401_02', 2)	# 87-88
    sprite('la401_01', 2)	# 89-90
    sprite('la401_00', 2)	# 91-92

@State
def RokepanDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        Unknown23086(1)
        WhiffCancel('RokepanHaseiA')
        WhiffCancel('RokepanHaseiB')
        WhiffCancel('RokepanHaseiAB')

        def upon_3():
            if (SLOT_18 == 5):
                SFX_3('airdash_m')
                Unknown8009(1)
                WhiffCancelEnable(1)
                Unknown3029(1)
            if (SLOT_18 == 7):
                Unknown8009(1)
            if (SLOT_18 == 9):
                Unknown8009(1)
            if (SLOT_18 == 11):
                Unknown8009(1)
            if (SLOT_18 >= 5):
                if CheckInput(0x5f):
                    clearUponHandler(3)
                    Unknown7007('706c613230395f30000000000000000064000000706c613230395f31000000000000000064000000706c613230395f320000000000000000640000000000000000000000000000000000000000000000')
                    sendToLabel(99)
        Unknown26('laef401punch')
        Unknown26('laef401punch_b')
        Unknown8009(1)
        SFX_3('chain_snap')
        if Unknown23145('RocketPunchAB'):
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)
    (SLOT_62 == 6)
    if SLOT_0:
        _gotolabel(6)
    (SLOT_62 == 5)
    if SLOT_0:
        _gotolabel(5)
    (SLOT_62 == 4)
    if SLOT_0:
        _gotolabel(4)
    (SLOT_62 == 3)
    if SLOT_0:
        _gotolabel(3)
    (SLOT_62 == 2)
    if SLOT_0:
        _gotolabel(2)
    (SLOT_62 == 1)
    if SLOT_0:
        _gotolabel(1)
    Unknown19(0, 2, 62)
    label(6)
    sprite('la402_00l', 2)	# 1-2
    Unknown7007('706c613230375f30000000000000000064000000706c613230375f31000000000000000064000000706c613230385f30000000000000000064000000706c613230385f31000000000000000064000000')
    sprite('la402_01l', 2)	# 3-4
    sprite('la402_01k', 1)	# 5-5
    physicsXImpulse(60000)
    sprite('la402_02j', 1)	# 6-6
    sprite('la402_03h', 1)	# 7-7
    physicsXImpulse(160000)
    sprite('la402_02f', 1)	# 8-8
    sprite('la402_03d', 1)	# 9-9
    sprite('la402_02b', 1)	# 10-10
    sprite('la402_03', 1)	# 11-11
    loopRest()
    gotoLabel(99)
    label(5)
    sprite('la402_00j', 2)	# 12-13
    Unknown7007('706c613230375f30000000000000000064000000706c613230375f31000000000000000064000000706c613230385f30000000000000000064000000706c613230385f31000000000000000064000000')
    sprite('la402_01j', 2)	# 14-15
    sprite('la402_03i', 1)	# 16-16
    physicsXImpulse(40000)
    sprite('la402_03g', 1)	# 17-17
    Unknown1019(400)
    sprite('la402_02e', 1)	# 18-18
    sprite('la402_03c', 1)	# 19-19
    sprite('la402_03a', 1)	# 20-20
    sprite('la402_03', 1)	# 21-21
    Unknown1019(50)
    loopRest()
    gotoLabel(99)
    label(4)
    sprite('la402_00h', 2)	# 22-23
    Unknown7007('706c613230375f30000000000000000064000000706c613230375f31000000000000000064000000706c613230385f30000000000000000064000000706c613230385f31000000000000000064000000')
    sprite('la402_01h', 2)	# 24-25
    sprite('la402_02g', 1)	# 26-26
    physicsXImpulse(40000)
    sprite('la402_02e', 1)	# 27-27
    Unknown1019(400)
    sprite('la402_03c', 1)	# 28-28
    sprite('la402_03a', 1)	# 29-29
    sprite('la402_03', 1)	# 30-30
    Unknown1019(50)
    loopRest()
    gotoLabel(99)
    label(3)
    sprite('la402_00g', 2)	# 31-32
    Unknown7007('706c613230375f30000000000000000064000000706c613230375f31000000000000000064000000706c613230385f30000000000000000064000000706c613230385f31000000000000000064000000')
    sprite('la402_01g', 2)	# 33-34
    sprite('la402_02f', 1)	# 35-35
    physicsXImpulse(40000)
    sprite('la402_03d', 1)	# 36-36
    Unknown1019(400)
    sprite('la402_02b', 1)	# 37-37
    sprite('la402_03', 1)	# 38-38
    loopRest()
    gotoLabel(99)
    label(2)
    sprite('la402_00e', 2)	# 39-40
    Unknown7007('706c613230375f30000000000000000064000000706c613230375f31000000000000000064000000706c613230385f30000000000000000064000000706c613230385f31000000000000000064000000')
    sprite('la402_01e', 2)	# 41-42
    sprite('la402_02d', 1)	# 43-43
    physicsXImpulse(40000)
    sprite('la402_02b', 1)	# 44-44
    Unknown1019(400)
    sprite('la402_03', 1)	# 45-45
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('la402_00b', 2)	# 46-47
    Unknown7007('706c613230375f30000000000000000064000000706c613230375f31000000000000000064000000706c613230385f30000000000000000064000000706c613230385f31000000000000000064000000')
    sprite('la402_01b', 2)	# 48-49
    sprite('la402_03a', 1)	# 50-50
    physicsXImpulse(40000)
    sprite('la402_03', 1)	# 51-51
    Unknown1019(200)
    loopRest()
    gotoLabel(99)
    label(0)
    sprite('la402_00', 2)	# 52-53
    Unknown7007('706c613230375f30000000000000000064000000706c613230375f31000000000000000064000000706c613230385f30000000000000000064000000706c613230385f31000000000000000064000000')
    sprite('la402_01', 2)	# 54-55
    sprite('la402_02', 1)	# 56-56
    loopRest()
    label(99)
    sprite('la402_04', 2)	# 57-58
    Unknown1084(1)
    Unknown1045(40000)
    Unknown8010(100, 1, 1)
    clearUponHandler(3)
    sprite('la402_05', 2)	# 59-60
    sprite('la402_06', 2)	# 61-62
    Unknown8010(100, 1, 1)
    WhiffCancelEnable(0)
    sprite('la402_07', 2)	# 63-64
    Unknown8010(100, 1, 1)
    sprite('la402_08', 2)	# 65-66
    Unknown8010(100, 1, 1)
    sprite('la402_09', 2)	# 67-68
    Unknown8010(100, 1, 1)
    sprite('la402_10', 2)	# 69-70
    sprite('la402_11', 2)	# 71-72
    Unknown1084(1)

@State
def RokepanHaseiA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(1000)
        AirPushbackY(-70000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown9118(50)
        Unknown11058('0100000000000000000000000000000000000000')
        HitOverhead(2)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')
        Unknown30068(1)
        sendToLabelUpon(2, 9)
    sprite('la402_05', 2)	# 1-2
    Unknown8009(1)
    Unknown3029(1)
    SLOT_12 = (SLOT_12 + SLOT_19)
    Unknown1019(10)
    sprite('la402_06', 2)	# 3-4
    sprite('la208_01', 2)	# 5-6
    Unknown1019(50)
    sprite('la208_02', 6)	# 7-12
    Unknown8007(100, 1, 1)
    physicsXImpulse(40000)
    physicsYImpulse(22000)
    setGravity(4500)
    Unknown7009(1)
    sprite('la208_06', 32767)	# 13-32779
    Unknown1019(50)
    label(9)
    sprite('la208_08', 6)	# 32780-32785	 **attackbox here**
    Unknown23054('6c613230385f303700000000000000000000000000000000000000000000000006000000')
    RefreshMultihit()
    Unknown7007('706c613130365f31000000000000000064000000706c613331305f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    SFX_3('guard_hit_l')
    Unknown8000(100, 1, 1)
    GFX_0('laef_405clash_l', 1)
    ScreenShake(0, 5000)
    Unknown1084(1)
    sprite('la208_08', 4)	# 32786-32789	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown3029(0)
    sprite('la208_09', 5)	# 32790-32794
    sprite('la208_10', 5)	# 32795-32799
    sprite('la208_11', 5)	# 32800-32804
    sprite('la208_12', 5)	# 32805-32809
    sprite('la208_13', 5)	# 32810-32814
    sprite('la208_14', 5)	# 32815-32819

@State
def RokepanHaseiB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(15000)
        AirPushbackY(22000)
        AirUntechableTime(40)
        HitLow(2)
        Unknown9016(1)
        Unknown11058('0000000000000000010000000000000000000000')
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')
        Unknown30068(1)
    sprite('la402_05', 2)	# 1-2
    Unknown8009(1)
    Unknown3029(1)
    SLOT_12 = (SLOT_12 + SLOT_19)
    Unknown1019(10)
    sprite('la402_06', 2)	# 3-4
    sprite('la211_00', 1)	# 5-5
    Unknown1019(50)
    sprite('la211_01', 2)	# 6-7
    sprite('la211_02', 2)	# 8-9
    physicsXImpulse(40000)
    GFX_0('hibana2AB', 100)
    SFX_3('slash_blade_fast')
    sprite('la211_03', 2)	# 10-11
    SFX_3('la002')
    sprite('la211_04', 3)	# 12-14	 **attackbox here**
    Unknown1019(80)
    RefreshMultihit()
    Unknown7007('706c613331315f30000000000000000064000000706c613331315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la211_05', 3)	# 15-17
    Unknown3029(0)
    Unknown1019(80)
    Recovery()
    sprite('la211_06', 3)	# 18-20
    Unknown1019(80)
    sprite('la211_07', 3)	# 21-23
    Unknown1019(80)
    sprite('la211_08', 2)	# 24-25
    Unknown1019(80)
    Unknown8010(100, 1, 1)
    sprite('la211_09', 2)	# 26-27
    Unknown8010(100, 1, 1)
    Unknown1019(0)
    sprite('la211_10', 2)	# 28-29
    sprite('la211_11', 2)	# 30-31
    sprite('la211_12', 3)	# 32-34

@State
def RokepanHaseiAB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        AttackP2(80)
        GroundedHitstunAnimation(9)
        AirPushbackX(7000)
        AirPushbackY(35000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11091(10)
        Unknown30065(0)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Ex')
        Unknown30068(1)
    sprite('la402_05', 2)	# 1-2
    Unknown8009(1)
    Unknown3029(1)
    SLOT_12 = (SLOT_12 + SLOT_19)
    Unknown1019(10)
    sprite('la402_06', 1)	# 3-3
    sprite('la402_06', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('la203_00', 2)	# 5-6
    Unknown1019(50)
    sprite('la203_04', 2)	# 7-8
    sprite('la203_05', 2)	# 9-10
    SFX_3('slash_blade_middle')
    sprite('la203_07a', 4)	# 11-14	 **attackbox here**
    RefreshMultihit()
    SFX_1('pla106_0')
    sprite('la203_08', 1)	# 15-15
    Unknown1019(30)
    Recovery()
    sprite('la203_08', 1)	# 16-16
    Unknown1019(30)
    sprite('la203_08', 1)	# 17-17
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('la203_08', 1)	# 18-18
    Unknown1019(50)
    sprite('la203_08', 1)	# 19-19
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('la201_05', 4)	# 20-23
    Unknown8010(100, 1, 1)
    Unknown1019(0)
    sprite('la201_06', 4)	# 24-27
    sprite('la201_07', 4)	# 28-31
    sprite('la201_08', 4)	# 32-35
    loopRest()

@State
def AxeAttackA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        AttackP2(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(2000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)
        Unknown9310(1)
        Hitstop(15)
        PushbackX(12000)
        HitOverhead(2)
        Unknown9016(1)
        Unknown23027()
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')
        Unknown2004(1, 0)
    sprite('la404_00', 2)	# 1-2
    sprite('la404_01', 2)	# 3-4
    sprite('la404_02', 2)	# 5-6
    SFX_3('cloth_l')
    sprite('la404_05', 2)	# 7-8
    SFX_3('slash_blade_fast')
    sprite('la404_06', 2)	# 9-10
    sprite('la404_07', 2)	# 11-12	 **attackbox here**
    Unknown7007('706c613231305f30000000000000000064000000706c613231305f31000000000000000064000000706c613231305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_middle')
    sprite('la404_08', 2)	# 13-14	 **attackbox here**
    sprite('la404_09', 2)	# 15-16
    sprite('la404_10', 6)	# 17-22
    sprite('la404_12', 5)	# 23-27	 **attackbox here**
    Unknown23054('6c613430345f313100000000000000000000000000000000000000000000000005000000')
    ScreenShake(20000, 40000)
    RefreshMultihit()
    GFX_0('laef404clash', 7)
    GFX_0('laef404clash_r', 7)
    GFX_0('laef404burner', 4)
    GFX_0('laef404burner_add', 4)
    GFX_0('laef404burner2', 5)
    GFX_0('laef404burner2_add', 5)
    GFX_0('laef404burner3', 6)
    GFX_0('laef404burner3_add', 6)
    SFX_3('la001')
    SFX_3('la003')
    sprite('la404_12', 8)	# 28-35	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('la404_13', 4)	# 36-39
    Unknown26('laef404burner_add')
    Unknown26('laef404burner2_add')
    Unknown26('laef404burner3_add')
    Unknown26('laef404burner')
    Unknown26('laef404burner2')
    Unknown26('laef404burner3')
    sprite('la404_14', 4)	# 40-43
    sprite('la404_15', 4)	# 44-47
    sprite('la404_16', 3)	# 48-50
    sprite('la404_17', 3)	# 51-53

@State
def AxeAttackB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2400)
        AttackP1(80)
        AttackP2(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(2000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown9118(30)
        Unknown9310(1)
        Unknown11028(24)
        Hitstop(15)
        PushbackX(12000)
        HitOverhead(2)
        Unknown9016(1)
        Unknown23027()
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')
        Unknown2004(1, 0)
    sprite('la404_00', 2)	# 1-2
    sprite('la404_01', 3)	# 3-5
    sprite('la404_02', 3)	# 6-8
    SFX_3('cloth_l')
    sprite('la404_03', 3)	# 9-11
    sprite('la404_04', 3)	# 12-14
    sprite('la404_05', 3)	# 15-17
    SFX_3('slash_blade_fast')
    sprite('la404_06', 3)	# 18-20
    sprite('la404_07', 3)	# 21-23	 **attackbox here**
    Unknown7007('706c613231315f30000000000000000064000000706c613231315f31000000000000000064000000706c613231315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_middle')
    sprite('la404_08', 3)	# 24-26	 **attackbox here**
    sprite('la404_09', 3)	# 27-29
    sprite('la404_10', 6)	# 30-35
    sprite('la404_12', 5)	# 36-40	 **attackbox here**
    Unknown23054('6c613430345f313100000000000000000000000000000000000000000000000005000000')
    ScreenShake(20000, 40000)
    RefreshMultihit()
    GFX_0('laef404clash', 7)
    GFX_0('laef404clash_r', 7)
    GFX_0('laef404burner', 4)
    GFX_0('laef404burner_add', 4)
    GFX_0('laef404burner2', 5)
    GFX_0('laef404burner2_add', 5)
    GFX_0('laef404burner3', 6)
    GFX_0('laef404burner3_add', 6)
    SFX_3('la001')
    SFX_3('la003')
    sprite('la404_12', 8)	# 41-48	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('la404_13', 4)	# 49-52
    Unknown26('laef404burner_add')
    Unknown26('laef404burner2_add')
    Unknown26('laef404burner3_add')
    Unknown26('laef404burner')
    Unknown26('laef404burner2')
    Unknown26('laef404burner3')
    sprite('la404_14', 4)	# 53-56
    sprite('la404_15', 4)	# 57-60
    sprite('la404_16', 3)	# 61-63
    sprite('la404_17', 3)	# 64-66

@State
def AxeAttackAB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(500)
        AirPushbackX(2000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        Unknown11028(24)
        Hitstop(7)
        PushbackX(12000)
        HitOverhead(0)
        Unknown9016(1)
        Unknown11091(10)
        Unknown30065(0)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Ex')
        Unknown2004(1, 0)
    sprite('la404_00', 2)	# 1-2
    sprite('la404_01', 1)	# 3-3
    sprite('la404_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('la404_02', 2)	# 5-6
    SFX_3('cloth_l')
    sprite('la404_05', 2)	# 7-8
    SFX_3('slash_blade_fast')
    sprite('la404_06', 2)	# 9-10
    sprite('la404_07', 2)	# 11-12	 **attackbox here**
    Unknown7007('706c613231315f30000000000000000064000000706c613231315f31000000000000000064000000706c613231315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_middle')
    sprite('la404_08', 2)	# 13-14	 **attackbox here**
    sprite('la404_09', 2)	# 15-16
    sprite('la404_10', 6)	# 17-22
    sprite('la404_12', 5)	# 23-27	 **attackbox here**
    Unknown23054('6c613430345f313100000000000000000000000000000000000000000000000005000000')
    ScreenShake(20000, 40000)
    RefreshMultihit()
    AttackP1(80)
    Damage(3000)
    GroundedHitstunAnimation(1)
    AirPushbackX(2000)
    AirPushbackY(-80000)
    YImpluseBeforeWallbounce(0)
    AirUntechableTime(60)
    Unknown9310(1)
    Hitstop(15)
    PushbackX(12000)
    HitOverhead(2)
    Unknown9016(1)
    callSubroutine('AxeLv_Powerup')
    GFX_0('laef404clash', 7)
    GFX_0('laef404clash_r', 7)
    GFX_0('laef404burner', 4)
    GFX_0('laef404burner_add', 4)
    GFX_0('laef404burner2', 5)
    GFX_0('laef404burner2_add', 5)
    GFX_0('laef404burner3', 6)
    GFX_0('laef404burner3_add', 6)
    SFX_3('la001')
    SFX_3('la003')
    sprite('la404_12', 8)	# 28-35	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('la404_13', 4)	# 36-39
    Unknown26('laef404burner_add')
    Unknown26('laef404burner2_add')
    Unknown26('laef404burner3_add')
    Unknown26('laef404burner')
    Unknown26('laef404burner2')
    Unknown26('laef404burner3')
    sprite('la404_14', 4)	# 40-43
    sprite('la404_15', 4)	# 44-47
    sprite('la404_16', 3)	# 48-50
    sprite('la404_17', 3)	# 51-53

@State
def AxeAttackAirA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(40)
        Hitstop(6)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        Unknown9310(1)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('la405_00', 3)	# 1-3
    Unknown1019(50)
    YAccel(0)
    Unknown1039(0)
    sprite('la405_01', 2)	# 4-5
    sprite('la405_02', 2)	# 6-7
    Unknown7007('706c613231325f30000000000000000064000000706c613231325f31000000000000000064000000706c613231325f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1019(80)
    SFX_3('slash_blade_fast')
    sprite('la405_03', 2)	# 8-9
    sprite('la405_04', 2)	# 10-11
    Unknown1019(80)
    sprite('la405_05', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    sprite('la405_06', 2)	# 14-15
    Unknown1019(80)
    sprite('la405_07', 2)	# 16-17
    sprite('la405_08', 3)	# 18-20	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(-30000)
    setGravity(5000)
    RefreshMultihit()
    AirPushbackY(-50000)
    YImpluseBeforeWallbounce(5000)
    GFX_0('laef405burner', 4)
    GFX_0('laef405burner_add', 4)
    GFX_0('laef405burner2', 5)
    GFX_0('laef405burner2_add', 5)
    GFX_0('laef405burner3', 6)
    GFX_0('laef405burner3_add', 6)
    SFX_3('la001')
    SFX_3('airdash_m')
    sprite('la405_09', 3)	# 21-23	 **attackbox here**
    SFX_3('slash_blade_fast')
    label(0)
    sprite('la405_08', 3)	# 24-26	 **attackbox here**
    sprite('la405_09', 3)	# 27-29	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('la405_10', 2)	# 30-31
    Unknown3029(0)
    Unknown1084(1)
    SFX_3('la003')
    GFX_0('LandingImpactA', 104)
    GFX_0('laef_405clash_l', 7)
    GFX_0('laef_405clash_r', 7)
    sprite('la405_11', 2)	# 32-33
    Unknown26('laef405burner')
    Unknown26('laef405burner2')
    Unknown26('laef405burner3')
    Unknown26('laef405burner_add')
    Unknown26('laef405burner2_add')
    Unknown26('laef405burner3_add')
    SFX_3('guard_hit_l')
    sprite('la405_12', 2)	# 34-35
    sprite('la405_13', 3)	# 36-38
    Recovery()
    sprite('la405_14', 3)	# 39-41
    sprite('la405_15', 3)	# 42-44
    sprite('la405_16', 3)	# 45-47
    sprite('la405_17', 4)	# 48-51
    sprite('la405_18', 4)	# 52-55
    sprite('la405_19', 4)	# 56-59
    sprite('la405_20', 4)	# 60-63

@State
def AxeAttackAirB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(40)
        Hitstop(6)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        Unknown9310(1)
        Unknown9016(1)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Special')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('la405_00', 6)	# 1-6
    Unknown1019(50)
    YAccel(0)
    Unknown1039(0)
    sprite('la405_01', 4)	# 7-10
    Unknown1019(0)
    Unknown1051(0)
    sprite('la405_02', 4)	# 11-14
    Unknown7007('706c613231335f30000000000000000064000000706c613231335f31000000000000000064000000706c613231335f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('la405_03', 4)	# 15-18
    sprite('la405_04', 4)	# 19-22
    sprite('la405_05', 3)	# 23-25	 **attackbox here**
    RefreshMultihit()
    sprite('la405_06', 3)	# 26-28
    sprite('la405_07', 3)	# 29-31
    sprite('la405_08', 3)	# 32-34	 **attackbox here**
    physicsYImpulse(-40000)
    setGravity(5000)
    RefreshMultihit()
    AirPushbackY(-50000)
    YImpluseBeforeWallbounce(5000)
    GFX_0('laef405burner', 4)
    GFX_0('laef405burner_add', 4)
    GFX_0('laef405burner2', 5)
    GFX_0('laef405burner2_add', 5)
    GFX_0('laef405burner3', 6)
    GFX_0('laef405burner3_add', 6)
    SFX_3('la001')
    SFX_3('airdash_m')
    sprite('la405_09', 3)	# 35-37	 **attackbox here**
    SFX_3('slash_blade_fast')
    label(0)
    sprite('la405_08', 3)	# 38-40	 **attackbox here**
    sprite('la405_09', 3)	# 41-43	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('la405_10', 2)	# 44-45
    Unknown3029(0)
    Unknown1084(1)
    SFX_3('la003')
    GFX_0('LandingImpactB', 104)
    GFX_0('laef_405clash_l', 7)
    GFX_0('laef_405clash_r', 7)
    sprite('la405_11', 2)	# 46-47
    Unknown26('laef405burner')
    Unknown26('laef405burner2')
    Unknown26('laef405burner3')
    Unknown26('laef405burner_add')
    Unknown26('laef405burner2_add')
    Unknown26('laef405burner3_add')
    SFX_3('guard_hit_l')
    sprite('la405_12', 2)	# 48-49
    sprite('la405_13', 3)	# 50-52
    Recovery()
    sprite('la405_14', 3)	# 53-55
    sprite('la405_15', 3)	# 56-58
    sprite('la405_16', 3)	# 59-61
    sprite('la405_17', 4)	# 62-65
    sprite('la405_18', 4)	# 66-69
    sprite('la405_19', 4)	# 70-73
    sprite('la405_20', 4)	# 74-77

@State
def AxeAttackAirAB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(5)
        Damage(1200)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(40)
        Hitstop(6)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        Unknown9310(1)
        Unknown9016(1)
        Unknown11091(10)
        Unknown30065(0)
        callSubroutine('AxeLv_Powerup')
        callSubroutine('AxeLvExp_Ex')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('la405_00', 3)	# 1-3
    Unknown1019(80)
    YAccel(0)
    Unknown1039(0)
    sprite('la405_01', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    sprite('la405_02', 2)	# 6-7
    Unknown7007('706c613231335f30000000000000000064000000706c613231335f31000000000000000064000000706c613231335f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1019(80)
    SFX_3('slash_blade_fast')
    sprite('la405_03', 2)	# 8-9
    sprite('la405_04', 2)	# 10-11
    Unknown1019(80)
    sprite('la405_05', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    sprite('la405_06', 2)	# 14-15
    Unknown1019(80)
    sprite('la405_07', 2)	# 16-17
    sprite('la405_08', 3)	# 18-20	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(-30000)
    setGravity(5000)
    RefreshMultihit()
    AirPushbackY(-50000)
    YImpluseBeforeWallbounce(5000)
    GFX_0('laef405burner', 4)
    GFX_0('laef405burner_add', 4)
    GFX_0('laef405burner2', 5)
    GFX_0('laef405burner2_add', 5)
    GFX_0('laef405burner3', 6)
    GFX_0('laef405burner3_add', 6)
    SFX_3('la001')
    SFX_3('airdash_m')
    sprite('la405_09', 3)	# 21-23	 **attackbox here**
    SFX_3('slash_blade_fast')
    label(0)
    sprite('la405_08', 3)	# 24-26	 **attackbox here**
    sprite('la405_09', 3)	# 27-29	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('la405_10', 2)	# 30-31
    Unknown3029(0)
    Unknown1084(1)
    SFX_3('la003')
    GFX_0('LandingImpactAB', 104)
    GFX_0('laef_405clash_l', 7)
    GFX_0('laef_405clash_r', 7)
    sprite('la405_11', 2)	# 32-33
    Unknown26('laef405burner')
    Unknown26('laef405burner2')
    Unknown26('laef405burner3')
    Unknown26('laef405burner_add')
    Unknown26('laef405burner2_add')
    Unknown26('laef405burner3_add')
    SFX_3('guard_hit_l')
    sprite('la405_12', 2)	# 34-35
    sprite('la405_13', 3)	# 36-38
    Recovery()
    sprite('la405_14', 3)	# 39-41
    sprite('la405_15', 3)	# 42-44
    sprite('la405_16', 3)	# 45-47
    sprite('la405_17', 4)	# 48-51
    sprite('la405_18', 4)	# 52-55
    sprite('la405_19', 4)	# 56-59
    sprite('la405_20', 4)	# 60-63

@State
def UltimateTackle():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(2500)
        AttackP2(60)
        Unknown11091(10)
        Unknown11092(1)
        AirUntechableTime(100)
        Unknown9310(45)
        Hitstop(20)
        AirPushbackX(0)
        AirPushbackY(80000)
        Unknown30055('c0d401002800000028000000')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11068(1)
        Unknown9016(1)

        def upon_45():
            if (SLOT_18 >= 3):
                pass

        def upon_STATE_END():
            Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009401000000000000')

        def upon_78():
            clearUponHandler(78)
            Unknown2037(1)

        def upon_43():
            if (SLOT_48 == 405):
                sendToLabel(0)
                Damage(4700)
            if (SLOT_48 == 408):
                Unknown2017(0)

        def upon_LANDING():
            clearUponHandler(2)
            if SLOT_2:
                sendToLabel(10)
            else:
                sendToLabel(11)
    sprite('la430_00', 3)	# 1-3
    setInvincible(1)
    sprite('la430_00', 3)	# 4-6
    Unknown30080('')
    Unknown2036(55, -1, 0)
    Unknown2058(-10000)
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706c613235305f30000000000000000064000000706c613235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la430_01', 4)	# 7-10
    sprite('la430_02', 4)	# 11-14
    sprite('la430_03', 4)	# 15-18
    sprite('la430_01', 1)	# 19-19
    Unknown23029(11, 400, 0)
    sprite('la430_01', 3)	# 20-22
    sprite('la430_02', 4)	# 23-26
    sprite('la430_03', 4)	# 27-30
    sprite('la430_01', 4)	# 31-34
    sprite('la430_02', 4)	# 35-38
    sprite('la430_03', 4)	# 39-42
    sprite('la430_01', 4)	# 43-46
    sprite('la430_02', 4)	# 47-50
    sprite('la430_03', 4)	# 51-54
    sprite('la430_01', 4)	# 55-58
    sprite('la430_02', 4)	# 59-62
    sprite('la430_04', 4)	# 63-66
    Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009101000000000000')
    sprite('la430_05', 4)	# 67-70
    sprite('la430_06', 4)	# 71-74
    sprite('la430_07', 3)	# 75-77
    Unknown7007('706c613235315f30000000000000000064000000706c613235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    physicsXImpulse(60000)
    Unknown8007(100, 1, 1)
    SFX_3('airdash_m')
    GFX_0('laef430slasher', 100)
    GFX_0('laef430slasher_b', 100)
    SFX_3('la002')
    sprite('la430_08', 3)	# 78-80
    SFX_3('la002')
    sprite('la430_07', 3)	# 81-83
    SFX_3('la002')
    sprite('la430_08', 3)	# 84-86
    SFX_3('la002')
    label(0)
    sprite('la430_09', 5)	# 87-91
    sprite('la430_10', 3)	# 92-94
    SFX_3('la002')
    Unknown1019(60)
    Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009201000000000000')
    Unknown2017(1)
    sprite('la430_11', 3)	# 95-97	 **attackbox here**
    GFX_0('430upperaura', 100)
    RefreshMultihit()
    if (SLOT_5 == 0):
        Unknown10000(90)
    if (SLOT_5 == 1):
        Unknown10000(95)
    if (SLOT_5 == 2):
        Unknown10000(100)
    if (SLOT_5 == 3):
        Unknown10000(144)
    if (SLOT_5 == 4):
        Unknown10000(225)
    Unknown1019(60)
    physicsYImpulse(50000)
    setGravity(1800)
    Unknown26('laef430slasher')
    Unknown26('laef430slasher_b')
    GFX_1('laef_430_upper', 100)
    GFX_1('laef_430_upper_b', 100)
    GFX_0('laef430burner_start', 4)
    GFX_0('laef430burner2_start', 5)
    GFX_0('laef430burner3_start', 6)
    GFX_0('laef430burner_start_add', 4)
    GFX_0('laef430burner2_start_add', 5)
    GFX_0('laef430burner3_start_add', 6)
    SFX_3('la001')
    sprite('la430_12', 3)	# 98-100	 **attackbox here**
    Unknown26('laef430burner_start')
    Unknown26('laef430burner2_start')
    Unknown26('laef430burner3_start')
    Unknown26('laef430burner_start_add')
    Unknown26('laef430burner2_start_add')
    Unknown26('laef430burner3_start_add')
    GFX_0('laef430burner', 4)
    GFX_0('laef430burner_add', 4)
    GFX_0('laef430burner2', 5)
    GFX_0('laef430burner2_add', 5)
    GFX_0('laef430burner3', 6)
    GFX_0('laef430burner3_add', 6)
    SFX_3('la001')
    sprite('la430_13', 3)	# 101-103	 **attackbox here**
    Unknown7007('6c613331340000000000000000000000640000006c6133313600000000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    RefreshMultihit()
    AirPushbackY(60000)
    Unknown1019(0)
    sendToLabelUpon(4, 8)
    Unknown26('laef430burner')
    Unknown26('laef430burner2')
    Unknown26('laef430burner3')
    Unknown26('laef430burner_add')
    Unknown26('laef430burner2_add')
    Unknown26('laef430burner3_add')
    GFX_0('laef430burner', 4)
    GFX_0('laef430burner_add', 4)
    GFX_0('laef430burner2', 5)
    GFX_0('laef430burner2_add', 5)
    GFX_0('laef430burner3', 6)
    GFX_0('laef430burner3_add', 6)
    SFX_3('la001')
    label(9)
    sprite('la430_14', 3)	# 104-106	 **attackbox here**
    sprite('la430_13', 3)	# 107-109	 **attackbox here**
    loopRest()
    gotoLabel(9)
    label(8)
    clearUponHandler(4)
    sprite('la430_15', 4)	# 110-113
    setInvincible(0)
    Unknown26('laef430burner')
    Unknown26('laef430burner2')
    Unknown26('laef430burner3')
    Unknown26('laef430burner_add')
    Unknown26('laef430burner2_add')
    Unknown26('laef430burner3_add')
    sprite('la430_16', 4)	# 114-117
    loopRest()
    label(7)
    sprite('la020_07', 4)	# 118-121
    sprite('la020_08', 4)	# 122-125
    loopRest()
    gotoLabel(7)
    label(10)
    sprite('la001_00', 6)	# 126-131
    sprite('la001_01', 6)	# 132-137
    sprite('la001_02', 6)	# 138-143
    sprite('la001_03', 6)	# 144-149
    sprite('la001_04', 6)	# 150-155
    SFX_1('pla301_1')
    sprite('la001_05', 6)	# 156-161
    GFX_0('laef001burner', 4)
    GFX_0('laef001burner_add', 4)
    GFX_0('laef001burner2', 5)
    GFX_0('laef001burner2_add', 5)
    GFX_0('laef001burner3', 6)
    GFX_0('laef001burner3_add', 6)
    GFX_0('laef001burner4', 7)
    GFX_0('laef001burner4_add', 7)
    GFX_0('laef001burner5', 8)
    GFX_0('laef001burner5_add', 8)
    GFX_0('laef001burner6', 9)
    GFX_0('laef001burner6_add', 9)
    SFX_3('la001')
    SLOT_51 = (SLOT_51 + SLOT_31)
    SLOT_51 = (SLOT_51 / 50)
    SLOT_51 = (SLOT_51 * (-1))

    def upon_3():
        SLOT_31 = (SLOT_31 + SLOT_51)

    def upon_STATE_END():
        Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009401000000000000')
        SLOT_31 = 0
        SLOT_32 = 0
    sprite('la001_06', 6)	# 162-167
    sprite('la001_07', 6)	# 168-173
    sprite('la001_08', 6)	# 174-179
    sprite('la001_05', 6)	# 180-185
    sprite('la001_06', 6)	# 186-191
    sprite('la001_07', 6)	# 192-197
    SFX_3('cloth_l')
    sprite('la001_08', 6)	# 198-203
    sprite('la001_05', 6)	# 204-209
    sprite('la001_04', 6)	# 210-215
    sprite('la001_03', 6)	# 216-221
    ExitState()
    label(11)
    sprite('la010_00', 3)	# 222-224
    sprite('la230_05', 15)	# 225-239
    sprite('la230_01', 2)	# 240-241
    sprite('la230_00', 2)	# 242-243
    sprite('la010_01', 4)	# 244-247
    sprite('la010_00', 4)	# 248-251

@State
def UltimateTackleOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1150)
        AttackP2(60)
        Unknown11091(10)
        Unknown11092(1)
        Hitstop(6)
        AirUntechableTime(300)
        Unknown9310(36)
        AirPushbackX(0)
        AirPushbackY(45000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11068(1)
        Unknown9016(1)

        def upon_45():
            if (SLOT_18 >= 3):
                pass

        def upon_STATE_END():
            Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009401000000000000')

        def upon_78():
            clearUponHandler(78)
            Unknown2037(1)

        def upon_43():
            if (SLOT_48 == 405):
                sendToLabel(0)
                Damage(1550)
            if (SLOT_48 == 408):
                Unknown2017(0)

        def upon_LANDING():
            clearUponHandler(2)
            if SLOT_2:
                sendToLabel(10)
            else:
                sendToLabel(11)
    sprite('la430_00', 3)	# 1-3
    setInvincible(1)
    sprite('la430_00', 3)	# 4-6
    Unknown30080('')
    Unknown2036(55, -1, 0)
    Unknown2058(-10000)
    GFX_1('persona_enter_ply', 0)
    Unknown7007('706c613235325f30000000000000000064000000706c613235325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la430_01', 4)	# 7-10
    sprite('la430_02', 4)	# 11-14
    sprite('la430_03', 4)	# 15-18
    sprite('la430_01', 1)	# 19-19
    Unknown23029(11, 400, 0)
    sprite('la430_01', 3)	# 20-22
    Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009601000000000000')
    sprite('la430_02', 4)	# 23-26
    sprite('la430_03', 4)	# 27-30
    sprite('la430_01', 4)	# 31-34
    sprite('la430_02', 4)	# 35-38
    sprite('la430_03', 4)	# 39-42
    sprite('la430_01', 4)	# 43-46
    sprite('la430_02', 4)	# 47-50
    sprite('la430_03', 4)	# 51-54
    sprite('la430_01', 4)	# 55-58
    sprite('la430_04', 4)	# 59-62
    Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009101000000000000')
    sprite('la430_05', 4)	# 63-66
    sprite('la430_06', 4)	# 67-70
    sprite('la430_07', 3)	# 71-73
    Unknown7007('706c613235315f30000000000000000064000000706c613235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    physicsXImpulse(60000)
    Unknown8007(100, 1, 1)
    SFX_3('airdash_m')
    GFX_0('laef430slasher', 100)
    GFX_0('laef430slasher_b', 100)
    SFX_3('la002')
    sprite('la430_08', 3)	# 74-76
    SFX_3('la002')
    sprite('la430_07', 3)	# 77-79
    SFX_3('la002')
    sprite('la430_08', 3)	# 80-82
    SFX_3('la002')
    label(0)
    sprite('la430_09', 5)	# 83-87
    sprite('la430_10', 3)	# 88-90
    SFX_3('la002')
    Unknown1019(60)
    Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009201000000000000')
    Unknown2017(1)
    sprite('la430_11', 3)	# 91-93	 **attackbox here**
    GFX_0('430upperaura', 100)
    RefreshMultihit()
    if (SLOT_5 == 0):
        Unknown10000(90)
    if (SLOT_5 == 1):
        Unknown10000(95)
    if (SLOT_5 == 2):
        Unknown10000(100)
    if (SLOT_5 == 3):
        Unknown10000(144)
    if (SLOT_5 == 4):
        Unknown10000(225)
    Unknown1019(60)
    physicsYImpulse(50000)
    setGravity(1800)
    Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009301000000000000')
    Unknown26('laef430slasher')
    Unknown26('laef430slasher_b')
    GFX_1('laef_430_upper', 100)
    GFX_1('laef_430_upper_b', 100)
    GFX_0('laef430burner_start', 4)
    GFX_0('laef430burner2_start', 5)
    GFX_0('laef430burner3_start', 6)
    GFX_0('laef430burner_start_add', 4)
    GFX_0('laef430burner2_start_add', 5)
    GFX_0('laef430burner3_start_add', 6)
    SFX_3('la001')
    sprite('la430_12', 3)	# 94-96	 **attackbox here**
    Unknown26('laef430burner_start')
    Unknown26('laef430burner2_start')
    Unknown26('laef430burner3_start')
    Unknown26('laef430burner_start_add')
    Unknown26('laef430burner2_start_add')
    Unknown26('laef430burner3_start_add')
    GFX_0('laef430burner', 4)
    GFX_0('laef430burner_add', 4)
    GFX_0('laef430burner2', 5)
    GFX_0('laef430burner2_add', 5)
    GFX_0('laef430burner3', 6)
    GFX_0('laef430burner3_add', 6)
    SFX_3('la001')
    sprite('la430_13', 3)	# 97-99	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(40000)
    Hitstop(3)
    Unknown1019(0)
    sendToLabelUpon(4, 8)
    if SLOT_2:
        Unknown7007('706c613235335f30000000000000000064000000706c613235335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('laef430burner')
    Unknown26('laef430burner2')
    Unknown26('laef430burner3')
    Unknown26('laef430burner_add')
    Unknown26('laef430burner2_add')
    Unknown26('laef430burner3_add')
    GFX_0('laef430burner', 4)
    GFX_0('laef430burner_add', 4)
    GFX_0('laef430burner2', 5)
    GFX_0('laef430burner2_add', 5)
    GFX_0('laef430burner3', 6)
    GFX_0('laef430burner3_add', 6)
    SFX_3('la001')
    label(9)
    sprite('la430_14', 3)	# 100-102	 **attackbox here**
    RefreshMultihit()
    sprite('la430_13', 3)	# 103-105	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(8)
    clearUponHandler(4)
    sprite('la430_15', 4)	# 106-109
    setInvincible(0)
    Unknown26('laef430burner')
    Unknown26('laef430burner2')
    Unknown26('laef430burner3')
    Unknown26('laef430burner_add')
    Unknown26('laef430burner2_add')
    Unknown26('laef430burner3_add')
    sprite('la430_16', 4)	# 110-113
    loopRest()
    label(7)
    sprite('la020_07', 4)	# 114-117
    sprite('la020_08', 4)	# 118-121
    loopRest()
    gotoLabel(7)
    label(10)
    sprite('la001_00', 6)	# 122-127
    sprite('la001_01', 6)	# 128-133
    sprite('la001_02', 6)	# 134-139
    sprite('la001_03', 6)	# 140-145
    sprite('la001_04', 6)	# 146-151
    SFX_1('pla301_1')
    sprite('la001_05', 6)	# 152-157
    GFX_0('laef001burner', 4)
    GFX_0('laef001burner_add', 4)
    GFX_0('laef001burner2', 5)
    GFX_0('laef001burner2_add', 5)
    GFX_0('laef001burner3', 6)
    GFX_0('laef001burner3_add', 6)
    GFX_0('laef001burner4', 7)
    GFX_0('laef001burner4_add', 7)
    GFX_0('laef001burner5', 8)
    GFX_0('laef001burner5_add', 8)
    GFX_0('laef001burner6', 9)
    GFX_0('laef001burner6_add', 9)
    SFX_3('la001')
    SLOT_51 = (SLOT_51 + SLOT_31)
    SLOT_51 = (SLOT_51 / 50)
    SLOT_51 = (SLOT_51 * (-1))

    def upon_3():
        SLOT_31 = (SLOT_31 + SLOT_51)

    def upon_STATE_END():
        Unknown21015('504c415f506572736f6e615461636b6c650000000000000000000000000000009401000000000000')
        SLOT_31 = 0
        SLOT_32 = 0
    sprite('la001_06', 6)	# 158-163
    sprite('la001_07', 6)	# 164-169
    sprite('la001_08', 6)	# 170-175
    SFX_1('la128')
    sprite('la001_05', 6)	# 176-181
    sprite('la001_06', 6)	# 182-187
    sprite('la001_07', 6)	# 188-193
    SFX_3('cloth_l')
    sprite('la001_08', 6)	# 194-199
    sprite('la001_05', 6)	# 200-205
    sprite('la001_04', 6)	# 206-211
    sprite('la001_03', 6)	# 212-217
    ExitState()
    label(11)
    sprite('la010_00', 3)	# 218-220
    sprite('la230_05', 15)	# 221-235
    sprite('la230_01', 2)	# 236-237
    sprite('la230_00', 2)	# 238-239
    sprite('la010_01', 4)	# 240-243
    sprite('la010_00', 4)	# 244-247

@State
def UltimateFullswing():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(5)
        Damage(6000)
        Unknown11091(20)
        Hitstop(30)
        AirUntechableTime(100)
        AirPushbackX(120000)
        AirPushbackY(50000)
        Unknown23086(1)
        Unknown9310(1)
        Unknown11068(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown11056(0)
        if (SLOT_5 == 0):
            Unknown10000(90)
        if (SLOT_5 == 1):
            Unknown10000(95)
        if (SLOT_5 == 2):
            Unknown10000(100)
        if (SLOT_5 == 3):
            Unknown10000(130)
        if (SLOT_5 == 4):
            Unknown10000(200)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0100000001000000010000000100000000000000')

        def upon_3():
            if (not CheckInput(0xa)):
                if (not CheckInput(0x13)):
                    clearUponHandler(3)
                    SLOT_51 = 1

        def upon_45():
            if (not SLOT_81):
                if (SLOT_18 >= 3):
                    pass

        def upon_78():
            Unknown2037(1)
    sprite('la432_00', 3)	# 1-3
    sprite('la432_00', 6)	# 4-9
    sprite('la432_01', 6)	# 10-15
    Unknown7007('706c613235345f30000000000000000064000000706c613235345f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la432_02', 6)	# 16-21
    sprite('la432_03', 6)	# 22-27
    Unknown2058(-10000)
    Unknown30080('')
    Unknown2036(58, -1, 0)
    SFX_3('cloth_m')
    GFX_0('laef432_charge', 0)
    sprite('la432_04', 6)	# 28-33
    sprite('la432_05', 6)	# 34-39
    sprite('la432_03', 5)	# 40-44
    sprite('la432_04', 5)	# 45-49
    sprite('la432_05', 4)	# 50-53
    sprite('la432_05', 1)	# 54-54
    if (not SLOT_51):
        sendToLabel(10)
        SLOT_52 = 9
    sprite('la432_03', 4)	# 55-58
    SFX_3('cloth_l')
    sprite('la432_04', 4)	# 59-62
    sprite('la432_05', 3)	# 63-65
    sprite('la432_05', 1)	# 66-66
    label(1)
    sprite('la432_06', 4)	# 67-70
    Unknown26('laef432_charge')
    sprite('la432_07', 2)	# 71-72
    physicsXImpulse(80000)
    SFX_3('airdash_m')
    SFX_3('slash_beam_slow')
    sprite('la432_08', 2)	# 73-74
    SFX_3('airdash_m')
    sprite('la432_09', 4)	# 75-78
    Unknown1019(30)
    SFX_3('la001')
    sprite('la432_10', 4)	# 79-82
    Unknown1019(50)
    SFX_3('slash_blade_slow')
    GFX_0('laef432_10_burner4', 7)
    GFX_0('laef432_10_burner5', 8)
    GFX_0('laef432_10_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_11', 3)	# 83-85	 **attackbox here**
    Unknown8006(100, 1, 1)
    Unknown1019(10)
    Unknown7007('706c613235355f30000000000000000064000000706c613235355f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    RefreshMultihit()
    Unknown26('laef432_10_burner4')
    Unknown26('laef432_10_burner5')
    Unknown26('laef432_10_burner6')
    GFX_0('laef432_11_burner', 4)
    GFX_0('laef432_11_burner2', 5)
    GFX_0('laef432_11_burner3', 6)
    GFX_0('laef432_11_burner4', 7)
    GFX_0('laef432_11_burner5', 8)
    GFX_0('laef432_11_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    GFX_0('laef432_fire', 8)
    GFX_1('laef_432_smoke', 100)
    SFX_3('la001')
    sprite('la432_12', 3)	# 86-88	 **attackbox here**
    physicsXImpulse(0)
    Unknown8006(100, 1, 1)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_13', 6)	# 89-94
    setInvincible(0)
    if SLOT_2:
        SLOT_54 = (SLOT_54 + SLOT_31)
        SLOT_54 = (SLOT_54 / 50)
        SLOT_54 = (SLOT_54 * (-1))

        def upon_3():
            SLOT_31 = (SLOT_31 + SLOT_54)
        clearUponHandler(45)
        SLOT_32 = 0
    sprite('la432_14', 6)	# 95-100
    sprite('la432_13', 5)	# 101-105
    sprite('la432_14', 5)	# 106-110
    sprite('la432_13', 4)	# 111-114
    sprite('la432_14', 4)	# 115-118
    sprite('la432_15', 4)	# 119-122
    sprite('la432_16', 6)	# 123-128
    sprite('la432_17', 6)	# 129-134
    sprite('la201_05', 6)	# 135-140
    sprite('la201_06', 6)	# 141-146
    sprite('la201_07', 6)	# 147-152
    sprite('la201_08', 6)	# 153-158
    sprite('la432_18', 6)	# 159-164
    ExitState()
    label(10)
    sprite('la432_03', 4)	# 165-168

    def upon_3():
        if (not CheckInput(0xa)):
            if (not CheckInput(0x13)):
                clearUponHandler(3)
                SLOT_53 = 1
    SFX_0('cloth_l')
    sprite('la432_04', 4)	# 169-172
    sprite('la432_05', 3)	# 173-175
    sprite('la432_05', 1)	# 176-176
    if (SLOT_52 == 6):
        tag_voice(1, 'pla256_0', 'pla256_1', '', '')
    SLOT_52 = (SLOT_52 + (-1))
    if (not SLOT_52):
        sendToLabel(11)
    if SLOT_53:
        sendToLabel(1)
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('la432_06', 4)	# 177-180
    Unknown26('laef432_charge')
    sprite('la432_07', 2)	# 181-182
    physicsXImpulse(100000)
    SFX_3('airdash_m')
    SFX_3('slash_beam_slow')
    sprite('la432_08', 2)	# 183-184
    SFX_3('airdash_m')
    sprite('la432_07', 2)	# 185-186
    sprite('la432_08', 2)	# 187-188
    sprite('la432_07', 2)	# 189-190
    SFX_3('slash_beam_slow')
    sprite('la432_08', 2)	# 191-192
    sprite('la432_09', 4)	# 193-196
    Unknown1019(30)
    SFX_3('la001')
    sprite('la432_10', 4)	# 197-200
    Unknown1019(50)
    SFX_3('slash_blade_slow')
    GFX_0('laef432_10_burner4', 7)
    GFX_0('laef432_10_burner5', 8)
    GFX_0('laef432_10_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_11', 3)	# 201-203	 **attackbox here**
    Unknown8006(100, 1, 1)
    Unknown1019(10)
    tag_voice(0, 'pla257_0', 'pla257_1', '', '')
    RefreshMultihit()
    Damage(10000)
    if (SLOT_5 == 0):
        Unknown10000(90)
    if (SLOT_5 == 1):
        Unknown10000(95)
    if (SLOT_5 == 2):
        Unknown10000(100)
    if (SLOT_5 == 3):
        Unknown10000(130)
    if (SLOT_5 == 4):
        Unknown10000(200)
    Unknown26('laef432_10_burner4')
    Unknown26('laef432_10_burner5')
    Unknown26('laef432_10_burner6')
    GFX_0('laef432_11_burner', 4)
    GFX_0('laef432_11_burner2', 5)
    GFX_0('laef432_11_burner3', 6)
    GFX_0('laef432_11_burner4', 7)
    GFX_0('laef432_11_burner5', 8)
    GFX_0('laef432_11_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    GFX_0('laef432_fire', 8)
    GFX_1('laef_432_smoke', 100)
    SFX_3('la001')
    sprite('la432_12', 3)	# 204-206	 **attackbox here**
    physicsXImpulse(0)
    Unknown8006(100, 1, 1)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_13', 6)	# 207-212
    setInvincible(0)
    if SLOT_2:
        SLOT_54 = (SLOT_54 + SLOT_31)
        SLOT_54 = (SLOT_54 / 50)
        SLOT_54 = (SLOT_54 * (-1))

        def upon_3():
            SLOT_31 = (SLOT_31 + SLOT_54)
    sprite('la432_14', 6)	# 213-218
    sprite('la432_13', 5)	# 219-223
    sprite('la432_14', 5)	# 224-228
    sprite('la432_13', 4)	# 229-232
    sprite('la432_14', 4)	# 233-236
    sprite('la432_15', 4)	# 237-240
    sprite('la432_16', 6)	# 241-246
    sprite('la432_17', 6)	# 247-252
    sprite('la201_05', 6)	# 253-258
    sprite('la201_06', 6)	# 259-264
    sprite('la201_07', 6)	# 265-270
    sprite('la201_08', 6)	# 271-276
    sprite('la432_18', 6)	# 277-282

@State
def UltimateFullswingOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(7000)
        Unknown11091(20)
        Hitstop(50)
        AirUntechableTime(100)
        Unknown9310(1)
        AirPushbackX(180000)
        AirPushbackY(50000)
        Unknown23086(1)
        Unknown11068(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown11056(0)
        if (SLOT_5 == 0):
            Unknown10000(90)
        if (SLOT_5 == 1):
            Unknown10000(95)
        if (SLOT_5 == 2):
            Unknown10000(100)
        if (SLOT_5 == 3):
            Unknown10000(130)
        if (SLOT_5 == 4):
            Unknown10000(200)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0100000001000000010000000100000000000000')

        def upon_3():
            if (not CheckInput(0xa)):
                if (not CheckInput(0x13)):
                    clearUponHandler(3)
                    SLOT_51 = 1

        def upon_45():
            if (not SLOT_81):
                if (SLOT_18 >= 3):
                    pass

        def upon_78():
            Unknown2037(1)
    sprite('la432_00', 3)	# 1-3
    sprite('la432_00', 6)	# 4-9
    sprite('la432_01', 6)	# 10-15
    Unknown7007('706c613235345f30000000000000000064000000706c613235345f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('la432_02', 6)	# 16-21
    sprite('la432_03', 6)	# 22-27
    Unknown2058(-10000)
    Unknown30080('')
    Unknown2036(82, -1, 0)
    SFX_3('cloth_m')
    GFX_0('laef432_charge', 0)
    sprite('la432_04', 6)	# 28-33
    sprite('la432_05', 6)	# 34-39
    sprite('la432_03', 5)	# 40-44
    sprite('la432_04', 5)	# 45-49
    sprite('la432_05', 5)	# 50-54
    sprite('la432_03', 4)	# 55-58
    SFX_3('cloth_l')
    sprite('la432_04', 4)	# 59-62
    sprite('la432_05', 3)	# 63-65
    sprite('la432_05', 1)	# 66-66
    sprite('la432_03', 4)	# 67-70
    sprite('la432_04', 4)	# 71-74
    sprite('la432_05', 4)	# 75-78
    sprite('la432_03', 4)	# 79-82
    sprite('la432_04', 4)	# 83-86
    sprite('la432_05', 3)	# 87-89
    sprite('la432_05', 1)	# 90-90
    if (not SLOT_51):
        sendToLabel(10)
        SLOT_52 = 7
    label(1)
    sprite('la432_06', 4)	# 91-94
    Unknown26('laef432_charge')
    sprite('la432_07', 2)	# 95-96
    physicsXImpulse(80000)
    SFX_3('airdash_m')
    sprite('la432_08', 2)	# 97-98
    SFX_3('airdash_m')
    sprite('la432_09', 4)	# 99-102
    Unknown1019(30)
    SFX_3('la001')
    sprite('la432_10', 4)	# 103-106
    Unknown1019(50)
    SFX_3('slash_blade_slow')
    GFX_0('laef432_10_burner4', 7)
    GFX_0('laef432_10_burner5', 8)
    GFX_0('laef432_10_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_11', 3)	# 107-109	 **attackbox here**
    Unknown1019(10)
    Unknown7007('706c613235355f30000000000000000064000000706c613235355f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    RefreshMultihit()
    Unknown8006(100, 1, 1)
    Unknown26('laef432_10_burner4')
    Unknown26('laef432_10_burner5')
    Unknown26('laef432_10_burner6')
    GFX_0('laef432_11_burner', 4)
    GFX_0('laef432_11_burner2', 5)
    GFX_0('laef432_11_burner3', 6)
    GFX_0('laef432_11_burner4', 7)
    GFX_0('laef432_11_burner5', 8)
    GFX_0('laef432_11_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    GFX_0('laef432_fire', 8)
    GFX_1('laef_432_smoke', 100)
    SFX_3('la001')
    sprite('la432_12', 3)	# 110-112	 **attackbox here**
    physicsXImpulse(0)
    Unknown8006(100, 1, 1)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_13', 6)	# 113-118
    setInvincible(0)
    if SLOT_2:
        SLOT_54 = (SLOT_54 + SLOT_31)
        SLOT_54 = (SLOT_54 / 50)
        SLOT_54 = (SLOT_54 * (-1))

        def upon_3():
            SLOT_31 = (SLOT_31 + SLOT_54)
    sprite('la432_14', 6)	# 119-124
    sprite('la432_13', 5)	# 125-129
    sprite('la432_14', 5)	# 130-134
    sprite('la432_13', 4)	# 135-138
    sprite('la432_14', 4)	# 139-142
    sprite('la432_15', 4)	# 143-146
    sprite('la432_16', 6)	# 147-152
    sprite('la432_17', 6)	# 153-158
    sprite('la201_05', 6)	# 159-164
    sprite('la201_06', 6)	# 165-170
    sprite('la201_07', 6)	# 171-176
    sprite('la201_08', 6)	# 177-182
    sprite('la432_18', 6)	# 183-188
    ExitState()
    label(10)
    sprite('la432_03', 4)	# 189-192

    def upon_3():
        if (not CheckInput(0xa)):
            if (not CheckInput(0x13)):
                clearUponHandler(3)
                SLOT_53 = 1
    SFX_0('cloth_l')
    sprite('la432_04', 4)	# 193-196
    sprite('la432_05', 3)	# 197-199
    sprite('la432_05', 1)	# 200-200
    if (SLOT_52 == 6):
        tag_voice(1, 'pla256_0', 'pla256_1', '', '')
    SLOT_52 = (SLOT_52 + (-1))
    if (not SLOT_52):
        sendToLabel(11)
    if SLOT_53:
        sendToLabel(1)
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('la432_03', 4)	# 201-204
    sprite('la432_04', 4)	# 205-208
    sprite('la432_06', 2)	# 209-210
    Unknown26('laef432_charge')
    sprite('la432_07', 2)	# 211-212
    physicsXImpulse(100000)
    SFX_3('airdash_m')
    SFX_3('slash_beam_slow')
    sprite('la432_08', 2)	# 213-214
    SFX_3('airdash_m')
    sprite('la432_07', 2)	# 215-216
    sprite('la432_08', 2)	# 217-218
    sprite('la432_07', 2)	# 219-220
    SFX_3('slash_beam_slow')
    sprite('la432_08', 2)	# 221-222
    sprite('la432_09', 4)	# 223-226
    Unknown1019(30)
    SFX_3('la001')
    sprite('la432_10', 4)	# 227-230
    Unknown1019(50)
    SFX_3('slash_blade_slow')
    GFX_0('laef432_10_burner4', 7)
    GFX_0('laef432_10_burner5', 8)
    GFX_0('laef432_10_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_11', 3)	# 231-233	 **attackbox here**
    Unknown8006(100, 1, 1)
    Unknown1019(10)
    tag_voice(0, 'pla257_0', 'pla257_1', '', '')
    RefreshMultihit()
    Damage(15000)
    if (SLOT_5 == 0):
        Unknown10000(90)
    if (SLOT_5 == 1):
        Unknown10000(95)
    if (SLOT_5 == 2):
        Unknown10000(100)
    if (SLOT_5 == 3):
        Unknown10000(130)
    if (SLOT_5 == 4):
        Unknown10000(200)
    Unknown26('laef432_10_burner4')
    Unknown26('laef432_10_burner5')
    Unknown26('laef432_10_burner6')
    GFX_0('laef432_11_burner', 4)
    GFX_0('laef432_11_burner2', 5)
    GFX_0('laef432_11_burner3', 6)
    GFX_0('laef432_11_burner4', 7)
    GFX_0('laef432_11_burner5', 8)
    GFX_0('laef432_11_burner6', 9)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    GFX_0('laef432_fire', 8)
    GFX_1('laef_432_smoke', 100)
    SFX_3('la001')
    sprite('la432_12', 3)	# 234-236	 **attackbox here**
    physicsXImpulse(0)
    Unknown8006(100, 1, 1)
    GFX_1('laef_432_fire', 10)
    GFX_1('laef_432_fire', 11)
    SFX_3('la001')
    sprite('la432_13', 6)	# 237-242
    setInvincible(0)
    if SLOT_2:
        SLOT_54 = (SLOT_54 + SLOT_31)
        SLOT_54 = (SLOT_54 / 50)
        SLOT_54 = (SLOT_54 * (-1))

        def upon_3():
            SLOT_31 = (SLOT_31 + SLOT_54)
        clearUponHandler(45)
        SLOT_32 = 0
    sprite('la432_14', 6)	# 243-248
    sprite('la432_13', 5)	# 249-253
    sprite('la432_14', 5)	# 254-258
    sprite('la432_13', 4)	# 259-262
    sprite('la432_14', 4)	# 263-266
    sprite('la432_15', 4)	# 267-270
    sprite('la432_16', 6)	# 271-276
    sprite('la432_17', 6)	# 277-282
    sprite('la201_05', 6)	# 283-288
    sprite('la201_06', 6)	# 289-294
    sprite('la201_07', 6)	# 295-300
    sprite('la201_08', 6)	# 301-306
    sprite('la432_18', 6)	# 307-312

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(500)
        Unknown11091(100)
        Hitstop(0)
        Unknown11064(1)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(10000)
        Unknown9310(60)
        PushbackX(0)
        Unknown11023(1)
        Unknown9016(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11072(1, 850000, 80000)
        Unknown23027()

        def upon_43():
            if (SLOT_48 == 5001):
                clearUponHandler(43)
                Unknown23088(1, 1)
                Unknown23084(1)
                Unknown23083(1)
                setInvincible(1)
                Unknown23024(3)
                GFX_0('IchigekiCamera', 100)
                Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000008c13000000000000')

                def upon_3():
                    SLOT_5 = 0
                    SLOT_31 = 0
                    SLOT_32 = 0
                    SLOT_33 = 0
                Unknown23157(1)
                sendToLabel(0)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown21015('506572736f6e614963686967656b6900000000000000000000000000000000008a13000000000000')
            setInvincible(0)

        def upon_78():
            SFX_0('101_hit_slash_3')
    sprite('la450_00', 6)	# 1-6
    Unknown1084(1)
    Unknown23029(11, 950, 0)
    setInvincible(1)
    tag_voice(1, 'pla294_0', 'pla294_1', '', '')
    sprite('la450_01', 6)	# 7-12
    Unknown2036(68, -1, 2)
    Unknown23147()
    GFX_0('P4U_Cutin_Parent', 100)
    sprite('la450_02', 6)	# 13-18
    sprite('la450_03', 6)	# 19-24
    sprite('la450_04', 6)	# 25-30
    sprite('la450_05', 6)	# 31-36
    sprite('la450_06', 6)	# 37-42
    sprite('la450_07', 6)	# 43-48
    sprite('la450_08', 6)	# 49-54
    sprite('la450_06', 6)	# 55-60
    sprite('la450_07', 6)	# 61-66
    sprite('la450_08', 6)	# 67-72
    sprite('la450_06', 6)	# 73-78
    sprite('la450_07', 6)	# 79-84
    sprite('la450_08', 6)	# 85-90
    sprite('la450_06', 6)	# 91-96
    sprite('la450_07', 6)	# 97-102
    sprite('la450_08', 6)	# 103-108
    sprite('la450_06', 6)	# 109-114
    setInvincible(0)
    sprite('la450_07', 6)	# 115-120
    sprite('la450_08', 6)	# 121-126
    sprite('la450_06', 6)	# 127-132
    sprite('la450_07', 6)	# 133-138
    sprite('la450_08', 6)	# 139-144
    sprite('la450_06', 6)	# 145-150
    sprite('la450_07', 6)	# 151-156
    sprite('la450_08', 6)	# 157-162
    sprite('la450_09', 6)	# 163-168
    sprite('la450_10', 6)	# 169-174
    sprite('la450_11', 6)	# 175-180
    loopRest()
    ExitState()
    label(0)
    sprite('la450_08', 6)	# 181-186
    GFX_0('450kumonosu', 100)
    sprite('la450_12', 6)	# 187-192
    sprite('la450_13', 6)	# 193-198
    sprite('la432_00', 6)	# 199-204
    sprite('la432_01', 6)	# 205-210
    sprite('la432_02', 6)	# 211-216
    sprite('la432_06', 6)	# 217-222
    sprite('la432_09', 6)	# 223-228
    sprite('la432_10', 6)	# 229-234
    tag_voice(0, 'pla291_0', 'pla291_1', '', '')
    sprite('la450_50', 6)	# 235-240	 **attackbox here**
    GFX_0('450bukinage', 0)
    SFX_3('slash_blade_slow')
    sprite('la450_51', 6)	# 241-246
    sprite('la450_50', 3)	# 247-249	 **attackbox here**
    RefreshMultihit()
    GFX_0('450zanhit', 100)
    sprite('la450_51', 3)	# 250-252
    sprite('la450_52', 6)	# 253-258
    sprite('la450_53', 6)	# 259-264
    sprite('la450_54', 1)	# 265-265
    sprite('la450_55', 1)	# 266-266
    sprite('la450_56', 1)	# 267-267
    sprite('la450_57', 1)	# 268-268
    sprite('la450_57a', 1)	# 269-269
    sprite('la450_58b', 1)	# 270-270
    sprite('la450_58c', 1)	# 271-271
    sprite('la450_59d', 1)	# 272-272
    sprite('la450_59e', 1)	# 273-273
    sprite('la450_60', 2)	# 274-275
    GFX_1('laef450_catch', 4)
    SFX_3('damage_hit_m')
    sprite('la450_61', 10)	# 276-285
    sprite('la450_14', 8)	# 286-293
    sprite('la450_15', 4)	# 294-297
    sprite('la450_16', 4)	# 298-301	 **attackbox here**
    GFX_0('450zan', 100)
    GFX_0('450speedline', 100)
    GFX_0('laef450_zanhit', 100)
    RefreshMultihit()
    AirHitstunAnimation(12)
    SLOT_51 = 2
    tag_voice(0, 'pla292_0', 'pla292_1', '', '')
    label(1)
    sprite('la450_17', 4)	# 302-305
    sprite('la450_18', 4)	# 306-309
    SFX_3('slash_sword_slow')
    sprite('la450_19', 4)	# 310-313
    sprite('la450_20', 4)	# 314-317	 **attackbox here**
    ScreenShake(6000, 6000)
    RefreshMultihit()
    AirHitstunAnimation(12)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_21', 4)	# 318-321
    SFX_3('slash_sword_slow')
    sprite('la450_22', 4)	# 322-325
    sprite('la450_23', 4)	# 326-329	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_24', 4)	# 330-333
    sprite('la450_25', 4)	# 334-337
    SFX_3('slash_sword_slow')
    sprite('la450_26', 4)	# 338-341
    sprite('la450_27', 3)	# 342-344	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_27', 1)	# 345-345	 **attackbox here**
    SLOT_51 = (SLOT_51 + (-1))
    if (not SLOT_51):
        sendToLabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    SLOT_51 = 1
    label(3)
    sprite('la450_14', 3)	# 346-348
    SFX_3('slash_sword_middle')
    sprite('la450_15', 3)	# 349-351
    sprite('la450_16', 3)	# 352-354	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GFX_0('laef450_zanhit', 100)
    ScreenShake(9000, 9000)
    sprite('la450_17', 3)	# 355-357
    sprite('la450_18', 3)	# 358-360
    SFX_3('slash_sword_middle')
    sprite('la450_19', 3)	# 361-363
    sprite('la450_20', 3)	# 364-366	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_21', 3)	# 367-369
    SFX_3('slash_sword_middle')
    sprite('la450_22', 3)	# 370-372
    sprite('la450_23', 3)	# 373-375	 **attackbox here**
    ScreenShake(8000, 8000)
    RefreshMultihit()
    AirHitstunAnimation(13)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_24', 3)	# 376-378
    sprite('la450_25', 3)	# 379-381
    SFX_3('slash_sword_middle')
    sprite('la450_26', 3)	# 382-384
    sprite('la450_27', 2)	# 385-386	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_27', 1)	# 387-387	 **attackbox here**
    SLOT_51 = (SLOT_51 + (-1))
    if (not SLOT_51):
        sendToLabel(4)
    loopRest()
    gotoLabel(3)
    label(4)
    SLOT_51 = 4
    label(5)
    sprite('la450_14', 2)	# 388-389
    SFX_3('slash_sword_fast')
    sprite('la450_15', 2)	# 390-391
    sprite('la450_16', 2)	# 392-393	 **attackbox here**
    ScreenShake(12000, 10000)
    RefreshMultihit()
    AirHitstunAnimation(12)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_17', 2)	# 394-395
    sprite('la450_18', 2)	# 396-397
    SFX_3('slash_sword_fast')
    sprite('la450_19', 2)	# 398-399
    sprite('la450_20', 2)	# 400-401	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_21', 2)	# 402-403
    SFX_3('slash_sword_fast')
    sprite('la450_22', 2)	# 404-405
    sprite('la450_23', 2)	# 406-407	 **attackbox here**
    ScreenShake(12000, 10000)
    RefreshMultihit()
    AirHitstunAnimation(13)
    GFX_0('laef450_zanhit', 100)
    sprite('la450_24', 2)	# 408-409
    sprite('la450_25', 2)	# 410-411
    SFX_3('slash_sword_fast')
    sprite('la450_26', 2)	# 412-413
    sprite('la450_27', 1)	# 414-414	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    sprite('la450_27', 1)	# 415-415	 **attackbox here**
    SLOT_51 = (SLOT_51 + (-1))
    if (not SLOT_51):
        sendToLabel(6)
    loopRest()
    gotoLabel(5)
    label(6)
    sprite('la450_14', 4)	# 416-419
    GFX_0('IchigekiBlack', 100)
    sprite('la450_15', 4)	# 420-423
    sprite('la450_16', 6)	# 424-429	 **attackbox here**
    RefreshMultihit()
    GFX_0('laef450_zanhit', 100)
    Unknown9016(1)
    sprite('la450_27', 30)	# 430-459	 **attackbox here**
    clearUponHandler(78)
    Unknown23119(0, 1, 1)
    Unknown36(22)
    Unknown1000(1000000)
    Unknown35()
    Unknown36(3)
    Unknown3004(-10)
    Unknown35()
    GFX_0('IchigekiPicture', 100)
    GFX_0('450cutinbg', 100)
    Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000008d13000000000000')
    RefreshMultihit()
    AttackLevel_(5)
    Damage(500)
    Hitstop(0)
    Unknown11064(1)
    AirPushbackX(0)
    AirPushbackY(-20000)
    YImpluseBeforeWallbounce(20000)
    AirUntechableTime(10000)
    Unknown9310(1000)
    Unknown11023(1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11051('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11072(0, -1, -1)
    sprite('la450_27', 145)	# 460-604	 **attackbox here**
    Unknown21015('4963686967656b69426c61636b000000000000000000000000000000000000008e13000000000000')
    tag_voice(0, 'pla290_0', 'pla290_1', '', '')
    sprite('la450_28', 10)	# 605-614
    GFX_0('IchigekiBlack', 100)
    sprite('la450_28', 10)	# 615-624
    Unknown1000(0)
    teleportRelativeY(100000)
    setGravity(0)
    Unknown2017(0)
    Unknown2018(0, 500)
    sprite('la450_28', 1)	# 625-625
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(-100000)
    setGravity(-1000000)
    Unknown2017(0)
    Unknown3004(1)
    Unknown35()
    Unknown36(3)
    Unknown3004(1)
    Unknown35()
    sprite('la450_28', 3)	# 626-628
    Unknown26('IchigekiPicture')
    Unknown7014('la010')
    sprite('la450_29', 5)	# 629-633
    Unknown21015('4963686967656b69426c61636b000000000000000000000000000000000000008e13000000000000')
    sprite('la450_30', 5)	# 634-638
    SLOT_51 = 5
    label(7)
    sprite('la450_28', 3)	# 639-641
    sprite('la450_29', 3)	# 642-644
    sprite('la450_30', 2)	# 645-646
    sprite('la450_30', 1)	# 647-647
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(8, 2, 51)
    loopRest()
    gotoLabel(7)
    label(8)
    sprite('la450_28', 3)	# 648-650
    sprite('la450_29', 3)	# 651-653
    sprite('la450_30', 3)	# 654-656
    sprite('la450_31', 2)	# 657-658
    sprite('la450_32', 2)	# 659-660
    SFX_3('slash_blade_slow')
    tag_voice(0, 'pla293_0', 'pla293_1', '', '')
    sprite('la450_33', 2)	# 661-662
    sprite('la450_34', 2)	# 663-664
    sprite('la450_35', 2)	# 665-666
    sprite('la450_33', 2)	# 667-668
    sprite('la450_34', 2)	# 669-670
    sprite('la450_35', 2)	# 671-672
    sprite('la450_33', 2)	# 673-674
    sprite('la450_34', 2)	# 675-676
    sprite('la450_35', 2)	# 677-678
    sprite('la450_33', 2)	# 679-680
    sprite('la450_34', 2)	# 681-682
    sprite('la450_35', 2)	# 683-684
    sprite('la450_33', 2)	# 685-686
    sprite('la450_34', 2)	# 687-688
    sprite('la450_35', 2)	# 689-690
    sprite('la450_33', 6)	# 691-696
    sprite('la450_34', 6)	# 697-702
    Unknown7015()
    GFX_0('450todome', 100)
    sprite('la450_35', 6)	# 703-708
    ScreenShake(30000, 30000)
    Unknown36(3)
    Unknown3004(-50)
    Unknown35()
    Unknown36(22)
    Unknown1000(3000000)
    teleportRelativeY(0)
    setGravity(0)
    Unknown35()
    sprite('la000_00', 1)	# 709-709
    teleportRelativeY(0)
    sprite('keep', 1)	# 710-710
    GFX_0('450tvbreak', 100)
    ScreenShake(50000, 50000)
    SFX_3('damage_hit_mh')
    sprite('keep', 1)	# 711-711
    SFX_3('bomb_l')
    sprite('keep', 3)	# 712-714
    SFX_3('bomb_l')
    sprite('keep', 5)	# 715-719
    ScreenShake(50000, 50000)
    sprite('keep', 5)	# 720-724
    ScreenShake(50000, 50000)
    sprite('keep', 12)	# 725-736
    sprite('keep', 116)	# 737-852
    GFX_0('Ichigeki_todome', 100)
    sprite('keep', 65)	# 853-917
    GFX_0('450TVnoise', 100)
    sprite('keep', 35)	# 918-952
    Unknown36(3)
    Unknown3004(10)
    Unknown35()
    Unknown23024(0)
    sprite('keep', 6)	# 953-958

@Subroutine
def MouthTableInit():
    Unknown18011('pla000', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 13364, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla501', 12643, 13921, 14179, 13921, 14179, 13921, 14179, 13921, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla502', 12643, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 13363, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla506', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla507', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla520', 12643, 13665, 13667, 13665, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla521', 12643, 12641, 25399, 24887, 25399, 12337, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla522', 12643, 14177, 14179, 12641, 25397, 24887, 25399, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla523', 12643, 12641, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla524', 12643, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla525', 12643, 12641, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla402_0', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla402_1', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla403_0', 12643, 13921, 25392, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla600bes', 12643, 13665, 13667, 13665, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla600pag', 12643, 13665, 13667, 13665, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla600rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24885, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla600uyu', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601bno', 12643, 13665, 13667, 13665, 13411, 24885, 13361, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601bny', 12643, 24880, 25399, 12337, 14177, 12643, 24887, 25399, 24887, 12338, 13411, 24887, 13361, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601bpt', 12643, 13153, 25397, 14131, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 13411, 24887, 25397, 24885, 25397, 24885, 25399, 12849, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601pag', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601pyu', 12643, 24880, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601ryn', 12643, 24880, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla601uli', 12643, 14177, 13155, 24887, 25397, 24885, 25397, 12337, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla602bes', 12643, 13665, 12643, 24880, 25397, 12337, 13665, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla700bno', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 13108, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla700pbc', 12643, 14177, 12643, 24880, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla700pyu', 12643, 12641, 25394, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 12849, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla700rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla701bes', 12643, 14177, 12643, 24880, 25397, 24885, 25397, 13619, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla701bny', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla701bpt', 12643, 13665, 13667, 13665, 13667, 13665, 13411, 24885, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla701pag', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla701ryn', 12643, 14177, 12899, 24880, 25399, 13620, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 14133, 14177, 13155, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla701uli', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 14132, 14177, 14179, 12641, 25392, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla701uyu', 12643, 14177, 14179, 14177, 14179, 12641, 25392, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pla702pbc', 12643, 14177, 13411, 24885, 13617, 12643, 24885, 25399, 24887, 25399, 24887, 13617, 12899, 24887, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('pag')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('uyu')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('bno')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('bny')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('la600_00', 5)	# 2-6
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(-1959900)
    teleportRelativeY(300000)
    physicsXImpulse(40000)
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 7-11
    sprite('la600_00', 5)	# 12-16
    sprite('la600_01', 5)	# 17-21
    sprite('la600_00', 5)	# 22-26
    sprite('la600_01', 5)	# 27-31
    sprite('la600_00', 5)	# 32-36
    sprite('la600_01', 5)	# 37-41
    sprite('la600_00', 5)	# 42-46
    sprite('la600_01', 5)	# 47-51
    sprite('la600_00', 20)	# 52-71
    physicsXImpulse(0)
    Unknown2005()
    sprite('la600_00', 1)	# 72-72
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    Unknown26('laef600burner_add')
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 73-77
    physicsXImpulse(40000)
    sprite('la600_00', 5)	# 78-82
    sprite('la600_01', 5)	# 83-87
    sprite('la600_00', 5)	# 88-92
    physicsXImpulse(20000)
    sprite('la600_01', 5)	# 93-97
    sprite('la600_00', 5)	# 98-102
    physicsXImpulse(10000)
    sprite('la600_01', 5)	# 103-107
    sprite('la600_00', 5)	# 108-112
    sprite('la600_01', 2)	# 113-114
    sprite('la600_02', 4)	# 115-118
    Unknown2005()
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner_b', 0)
    GFX_0('laef600burner2_b', 1)
    GFX_0('laef600burner3_b', 2)
    GFX_0('laef600burner4_b', 3)
    Unknown26('laef600burner_add')
    SFX_3('down_steal_m')
    sprite('la600_03', 4)	# 119-122
    physicsYImpulse(-10000)
    Unknown26('laef600burner_b')
    Unknown26('laef600burner2_b')
    Unknown26('laef600burner3_b')
    Unknown26('laef600burner4_b')
    GFX_0('laef600burner_c', 0)
    GFX_0('laef600burner2_c', 1)
    GFX_0('laef600burner3_c', 2)
    GFX_0('laef600burner4_c', 3)
    sprite('la600_04', 4)	# 123-126
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner_c')
    Unknown26('laef600burner2_c')
    Unknown26('laef600burner3_c')
    Unknown26('laef600burner4_c')
    GFX_0('laef600_wing', 100)
    SFX_3('airdash_m')
    sprite('la600_05', 4)	# 127-130
    sendToLabelUpon(2, 2)
    label(1)
    sprite('la600_04', 4)	# 131-134
    sprite('la600_05', 4)	# 135-138
    loopRest()
    gotoLabel(1)
    label(2)
    clearUponHandler(2)
    sprite('la600_06', 4)	# 139-142
    Unknown8000(-1, 1, 1)
    physicsXImpulse(0)
    teleportRelativeX(-100)
    sprite('la600_07', 4)	# 143-146
    sprite('la600_08', 4)	# 147-150
    sprite('la600_09', 4)	# 151-154
    sprite('la600_10', 24)	# 155-178
    Unknown26('laef600_wing')
    GFX_0('laef600_axe', 100)
    sprite('la600_10', 10)	# 179-188
    SFX_3('highjump_m')
    sprite('la600_10', 10)	# 189-198
    SFX_3('attack_offset_shot')
    SFX_3('down_steal_m')
    sprite('la600_11', 4)	# 199-202
    Unknown7006('pla500', 100, 895577200, 12592, 0, 0, 100, 895577200, 12848, 0, 0, 100, 895577200, 14128, 0, 0, 100)
    SFX_3('damage_hit_m')
    sprite('la600_12', 4)	# 203-206
    sprite('la600_13', 4)	# 207-210
    sprite('la600_14', 4)	# 211-214
    sprite('la600_15', 4)	# 215-218
    SFX_3('slash_sword_middle')
    sprite('la600_16', 6)	# 219-224
    sprite('la600_17', 6)	# 225-230
    sprite('la600_18', 6)	# 231-236
    sprite('la600_19', 6)	# 237-242
    sprite('la600_20', 6)	# 243-248
    sprite('la201_08', 6)	# 249-254
    sprite('la432_18', 6)	# 255-260
    Unknown23018(1)
    label(3)
    sprite('la000_00', 6)	# 261-266
    sprite('la000_01', 6)	# 267-272
    sprite('la000_02', 6)	# 273-278
    sprite('la000_03', 6)	# 279-284
    sprite('la000_04', 6)	# 285-290
    sprite('la000_05', 6)	# 291-296
    sprite('la000_06', 6)	# 297-302
    sprite('la000_07', 6)	# 303-308
    sprite('la000_08', 6)	# 309-314
    sprite('la000_09', 6)	# 315-320
    sprite('la000_10', 6)	# 321-326
    sprite('la000_11', 6)	# 327-332
    loopRest()
    gotoLabel(3)
    ExitState()
    label(10)
    sprite('la601_00', 6)	# 333-338
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 339-344
    sprite('la601_02', 6)	# 345-350
    sprite('la601_00', 6)	# 351-356
    if random_(2, 0, 50):
        Unknown7006('pla503', 100, 895577200, 13360, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown2037(1)
    sprite('la601_01', 6)	# 357-362
    sprite('la601_02', 6)	# 363-368
    label(11)
    sprite('la601_00', 6)	# 369-374
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 375-380
    sprite('la601_02', 6)	# 381-386
    if SLOT_97:
        _gotolabel(11)
    sprite('la601_00', 6)	# 387-392
    sprite('la601_01', 6)	# 393-398
    sprite('la601_02', 6)	# 399-404
    sprite('la601_03', 6)	# 405-410
    sprite('la601_04', 6)	# 411-416
    if SLOT_2:
        Unknown7006('pla505', 100, 895577200, 13872, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('la601_05', 6)	# 417-422
    sprite('la601_06', 6)	# 423-428
    sprite('la601_07', 6)	# 429-434
    sprite('la450_01', 5)	# 435-439
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 440-444
    sprite('la450_03', 5)	# 445-449
    sprite('la450_01', 5)	# 450-454
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 455-459
    sprite('la601_08', 6)	# 460-465
    sprite('la601_09', 6)	# 466-471
    sprite('la601_10', 6)	# 472-477
    sprite('la601_11', 8)	# 478-485
    sprite('la601_12', 6)	# 486-491
    Unknown23018(1)
    label(12)
    sprite('la000_00', 6)	# 492-497
    sprite('la000_01', 6)	# 498-503
    sprite('la000_02', 6)	# 504-509
    sprite('la000_03', 6)	# 510-515
    sprite('la000_04', 6)	# 516-521
    sprite('la000_05', 6)	# 522-527
    sprite('la000_06', 6)	# 528-533
    sprite('la000_07', 6)	# 534-539
    sprite('la000_08', 6)	# 540-545
    sprite('la000_09', 6)	# 546-551
    sprite('la000_10', 6)	# 552-557
    sprite('la000_11', 6)	# 558-563
    loopRest()
    gotoLabel(12)
    ExitState()
    label(20)
    sprite('la610_09', 32767)	# 564-33330
    SFX_1('pla702pbc')
    ExitState()
    label(991)
    sprite('la000_00', 1)	# 33331-33331
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('la000_00', 6)	# 33332-33337
    sprite('la000_01', 6)	# 33338-33343
    sprite('la000_02', 6)	# 33344-33349
    sprite('la000_03', 6)	# 33350-33355
    sprite('la000_04', 6)	# 33356-33361
    sprite('la000_05', 6)	# 33362-33367
    sprite('la000_06', 6)	# 33368-33373
    sprite('la000_07', 6)	# 33374-33379
    sprite('la000_08', 6)	# 33380-33385
    sprite('la000_09', 6)	# 33386-33391
    sprite('la000_10', 6)	# 33392-33397
    sprite('la000_11', 6)	# 33398-33403
    loopRest()
    gotoLabel(992)
    label(100)
    sprite('la600_00', 5)	# 33404-33408
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-1959900)
        Unknown2019(500)
    else:
        Unknown1000(-2194900)
    teleportRelativeY(300000)
    physicsXImpulse(40000)
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 33409-33413
    sprite('la600_00', 5)	# 33414-33418
    sprite('la600_01', 5)	# 33419-33423
    sprite('la600_00', 5)	# 33424-33428
    sprite('la600_01', 5)	# 33429-33433
    sprite('la600_00', 5)	# 33434-33438
    sprite('la600_01', 5)	# 33439-33443
    sprite('la600_00', 5)	# 33444-33448
    sprite('la600_01', 5)	# 33449-33453
    sprite('la600_00', 20)	# 33454-33473
    physicsXImpulse(0)
    Unknown2005()
    sprite('la600_00', 1)	# 33474-33474
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    Unknown26('laef600burner_add')
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 33475-33479
    physicsXImpulse(40000)
    sprite('la600_00', 5)	# 33480-33484
    sprite('la600_01', 5)	# 33485-33489
    sprite('la600_00', 5)	# 33490-33494
    physicsXImpulse(20000)
    sprite('la600_01', 5)	# 33495-33499
    sprite('la600_00', 5)	# 33500-33504
    physicsXImpulse(10000)
    sprite('la600_01', 5)	# 33505-33509
    sprite('la600_00', 5)	# 33510-33514
    sprite('la600_01', 2)	# 33515-33516
    sprite('la600_02', 4)	# 33517-33520
    Unknown2005()
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner_b', 0)
    GFX_0('laef600burner2_b', 1)
    GFX_0('laef600burner3_b', 2)
    GFX_0('laef600burner4_b', 3)
    Unknown26('laef600burner_add')
    SFX_3('down_steal_m')
    sprite('la600_03', 4)	# 33521-33524
    physicsYImpulse(-10000)
    Unknown26('laef600burner_b')
    Unknown26('laef600burner2_b')
    Unknown26('laef600burner3_b')
    Unknown26('laef600burner4_b')
    GFX_0('laef600burner_c', 0)
    GFX_0('laef600burner2_c', 1)
    GFX_0('laef600burner3_c', 2)
    GFX_0('laef600burner4_c', 3)
    sprite('la600_04', 4)	# 33525-33528
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner_c')
    Unknown26('laef600burner2_c')
    Unknown26('laef600burner3_c')
    Unknown26('laef600burner4_c')
    GFX_0('laef600_wing', 100)
    SFX_3('airdash_m')
    sprite('la600_05', 4)	# 33529-33532
    sendToLabelUpon(2, 102)
    label(101)
    sprite('la600_04', 4)	# 33533-33536
    sprite('la600_05', 4)	# 33537-33540
    loopRest()
    gotoLabel(101)
    label(102)
    clearUponHandler(2)
    sprite('la600_06', 4)	# 33541-33544
    Unknown8000(-1, 1, 1)
    physicsXImpulse(0)
    teleportRelativeX(-100)
    sprite('la600_07', 4)	# 33545-33548
    sprite('la600_08', 4)	# 33549-33552
    sprite('la600_09', 4)	# 33553-33556
    sprite('la600_10', 24)	# 33557-33580
    Unknown26('laef600_wing')
    GFX_0('laef600_axe', 100)
    sprite('la600_10', 10)	# 33581-33590
    SFX_3('highjump_m')
    sprite('la600_10', 10)	# 33591-33600
    SFX_3('attack_offset_shot')
    SFX_3('down_steal_m')
    sprite('la600_11', 4)	# 33601-33604
    SFX_1('pla600bes')
    SFX_3('damage_hit_m')
    sprite('la600_12', 4)	# 33605-33608
    sprite('la600_13', 4)	# 33609-33612
    sprite('la600_14', 4)	# 33613-33616
    sprite('la600_15', 4)	# 33617-33620
    SFX_3('slash_sword_middle')
    sprite('la600_16', 6)	# 33621-33626
    sprite('la600_17', 6)	# 33627-33632
    sprite('la600_18', 6)	# 33633-33638
    sprite('la600_19', 6)	# 33639-33644
    sprite('la600_20', 6)	# 33645-33650
    sprite('la201_08', 6)	# 33651-33656
    sprite('la432_18', 6)	# 33657-33662

    def upon_40():
        clearUponHandler(40)
        sendToLabel(105)
    label(103)
    sprite('la000_00', 6)	# 33663-33668
    sprite('la000_01', 6)	# 33669-33674
    sprite('la000_02', 6)	# 33675-33680
    sprite('la000_03', 6)	# 33681-33686
    sprite('la000_04', 6)	# 33687-33692
    sprite('la000_05', 6)	# 33693-33698
    sprite('la000_06', 6)	# 33699-33704
    sprite('la000_07', 6)	# 33705-33710
    sprite('la000_08', 6)	# 33711-33716
    sprite('la000_09', 6)	# 33717-33722
    sprite('la000_10', 6)	# 33723-33728
    sprite('la000_11', 6)	# 33729-33734
    loopRest()
    if SLOT_97:
        _gotolabel(103)
    sprite('la000_00', 1)	# 33735-33735
    Unknown21007(24, 40)
    label(104)
    sprite('la000_00', 6)	# 33736-33741
    sprite('la000_01', 6)	# 33742-33747
    sprite('la000_02', 6)	# 33748-33753
    sprite('la000_03', 6)	# 33754-33759
    sprite('la000_04', 6)	# 33760-33765
    sprite('la000_05', 6)	# 33766-33771
    sprite('la000_06', 6)	# 33772-33777
    sprite('la000_07', 6)	# 33778-33783
    sprite('la000_08', 6)	# 33784-33789
    sprite('la000_09', 6)	# 33790-33795
    sprite('la000_10', 6)	# 33796-33801
    sprite('la000_11', 6)	# 33802-33807
    loopRest()
    gotoLabel(104)
    label(105)
    sprite('la001_00', 6)	# 33808-33813
    SFX_1('pla602bes')
    sprite('la001_01', 6)	# 33814-33819
    sprite('la001_02', 6)	# 33820-33825
    sprite('la001_03', 6)	# 33826-33831
    sprite('la001_04', 6)	# 33832-33837
    sprite('la001_05', 6)	# 33838-33843
    sprite('la001_06', 6)	# 33844-33849
    sprite('la001_07', 6)	# 33850-33855
    sprite('la001_08', 6)	# 33856-33861
    sprite('la001_05', 6)	# 33862-33867
    sprite('la001_06', 6)	# 33868-33873
    sprite('la001_07', 6)	# 33874-33879
    SFX_3('cloth_l')
    sprite('la001_08', 6)	# 33880-33885
    sprite('la001_05', 6)	# 33886-33891
    sprite('la001_06', 6)	# 33892-33897
    sprite('la001_07', 6)	# 33898-33903
    sprite('la001_08', 6)	# 33904-33909
    sprite('la001_04', 6)	# 33910-33915
    sprite('la001_03', 6)	# 33916-33921
    Unknown23018(1)
    label(106)
    sprite('la000_00', 6)	# 33922-33927
    sprite('la000_01', 6)	# 33928-33933
    sprite('la000_02', 6)	# 33934-33939
    sprite('la000_03', 6)	# 33940-33945
    sprite('la000_04', 6)	# 33946-33951
    sprite('la000_05', 6)	# 33952-33957
    sprite('la000_06', 6)	# 33958-33963
    sprite('la000_07', 6)	# 33964-33969
    sprite('la000_08', 6)	# 33970-33975
    sprite('la000_09', 6)	# 33976-33981
    sprite('la000_10', 6)	# 33982-33987
    sprite('la000_11', 6)	# 33988-33993
    loopRest()
    gotoLabel(106)
    ExitState()
    label(110)
    sprite('la601_00', 6)	# 33994-33999
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 34000-34005
    sprite('la601_02', 6)	# 34006-34011
    sprite('la601_00', 6)	# 34012-34017
    sprite('la601_01', 6)	# 34018-34023
    sprite('la601_02', 6)	# 34024-34029
    sprite('la601_00', 6)	# 34030-34035
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 34036-34041
    sprite('la601_02', 6)	# 34042-34047
    sprite('la601_00', 6)	# 34048-34053
    sprite('la601_01', 6)	# 34054-34059
    sprite('la601_02', 6)	# 34060-34065
    sprite('la601_03', 6)	# 34066-34071
    sprite('la601_04', 6)	# 34072-34077
    SFX_1('pla600pag')
    sprite('la601_05', 6)	# 34078-34083
    sprite('la601_06', 6)	# 34084-34089
    sprite('la601_07', 6)	# 34090-34095
    sprite('la450_01', 5)	# 34096-34100
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 34101-34105
    sprite('la450_03', 5)	# 34106-34110
    sprite('la450_01', 5)	# 34111-34115
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 34116-34120
    sprite('la601_08', 6)	# 34121-34126
    sprite('la601_09', 6)	# 34127-34132
    sprite('la601_10', 6)	# 34133-34138
    sprite('la601_11', 8)	# 34139-34146
    sprite('la601_12', 6)	# 34147-34152
    Unknown2037(2)
    label(111)
    sprite('la000_00', 6)	# 34153-34158
    sprite('la000_01', 6)	# 34159-34164
    sprite('la000_02', 6)	# 34165-34170
    sprite('la000_03', 6)	# 34171-34176
    sprite('la000_04', 6)	# 34177-34182
    sprite('la000_05', 6)	# 34183-34188
    if (not SLOT_2):
        Unknown21007(24, 40)
        Unknown21011(240)
    sprite('la000_06', 6)	# 34189-34194
    sprite('la000_07', 6)	# 34195-34200
    sprite('la000_08', 6)	# 34201-34206
    sprite('la000_09', 6)	# 34207-34212
    sprite('la000_10', 6)	# 34213-34218
    sprite('la000_11', 6)	# 34219-34224
    Unknown2038(-1)
    loopRest()
    gotoLabel(111)
    ExitState()
    label(120)
    sprite('la601_00', 6)	# 34225-34230
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 34231-34236
    sprite('la601_02', 6)	# 34237-34242
    sprite('la601_00', 6)	# 34243-34248
    sprite('la601_01', 6)	# 34249-34254
    sprite('la601_02', 6)	# 34255-34260
    sprite('la601_00', 6)	# 34261-34266
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 34267-34272
    sprite('la601_02', 6)	# 34273-34278
    sprite('la601_00', 6)	# 34279-34284
    sprite('la601_01', 6)	# 34285-34290
    sprite('la601_02', 6)	# 34291-34296
    sprite('la601_03', 6)	# 34297-34302
    sprite('la601_04', 6)	# 34303-34308
    SFX_1('pla600rrb')
    sprite('la601_05', 6)	# 34309-34314
    sprite('la601_06', 6)	# 34315-34320
    sprite('la601_07', 6)	# 34321-34326
    sprite('la450_01', 5)	# 34327-34331
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 34332-34336
    sprite('la450_03', 5)	# 34337-34341
    sprite('la450_01', 5)	# 34342-34346
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 34347-34351
    sprite('la601_08', 6)	# 34352-34357
    sprite('la601_09', 6)	# 34358-34363
    sprite('la601_10', 6)	# 34364-34369
    sprite('la601_11', 8)	# 34370-34377
    sprite('la601_12', 6)	# 34378-34383
    label(121)
    sprite('la000_00', 6)	# 34384-34389
    sprite('la000_01', 6)	# 34390-34395
    sprite('la000_02', 6)	# 34396-34401
    sprite('la000_03', 6)	# 34402-34407
    sprite('la000_04', 6)	# 34408-34413
    sprite('la000_05', 6)	# 34414-34419
    sprite('la000_06', 6)	# 34420-34425
    sprite('la000_07', 6)	# 34426-34431
    sprite('la000_08', 6)	# 34432-34437
    sprite('la000_09', 6)	# 34438-34443
    sprite('la000_10', 6)	# 34444-34449
    sprite('la000_11', 6)	# 34450-34455
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('la000_00', 6)	# 34456-34461
    sprite('la000_01', 6)	# 34462-34467
    sprite('la000_02', 6)	# 34468-34473
    sprite('la000_03', 6)	# 34474-34479
    Unknown21007(24, 40)
    Unknown21011(270)
    sprite('la000_04', 6)	# 34480-34485
    sprite('la000_05', 6)	# 34486-34491
    sprite('la000_06', 6)	# 34492-34497
    sprite('la000_07', 6)	# 34498-34503
    sprite('la000_08', 6)	# 34504-34509
    sprite('la000_09', 6)	# 34510-34515
    sprite('la000_10', 6)	# 34516-34521
    sprite('la000_11', 6)	# 34522-34527
    label(122)
    sprite('la000_00', 6)	# 34528-34533
    sprite('la000_01', 6)	# 34534-34539
    sprite('la000_02', 6)	# 34540-34545
    sprite('la000_03', 6)	# 34546-34551
    sprite('la000_04', 6)	# 34552-34557
    sprite('la000_05', 6)	# 34558-34563
    sprite('la000_06', 6)	# 34564-34569
    sprite('la000_07', 6)	# 34570-34575
    sprite('la000_08', 6)	# 34576-34581
    sprite('la000_09', 6)	# 34582-34587
    sprite('la000_10', 6)	# 34588-34593
    sprite('la000_11', 6)	# 34594-34599
    loopRest()
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('la601_00', 6)	# 34600-34605
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 34606-34611
    sprite('la601_02', 6)	# 34612-34617
    sprite('la601_00', 6)	# 34618-34623
    SFX_1('pla600uyu')
    sprite('la601_01', 6)	# 34624-34629
    sprite('la601_02', 6)	# 34630-34635
    sprite('la601_00', 6)	# 34636-34641
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 34642-34647
    sprite('la601_02', 6)	# 34648-34653
    sprite('la601_00', 6)	# 34654-34659
    sprite('la601_01', 6)	# 34660-34665
    sprite('la601_02', 6)	# 34666-34671
    sprite('la601_03', 6)	# 34672-34677
    sprite('la601_04', 6)	# 34678-34683
    sprite('la601_05', 6)	# 34684-34689
    sprite('la601_06', 6)	# 34690-34695
    sprite('la601_07', 6)	# 34696-34701
    sprite('la450_01', 5)	# 34702-34706
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 34707-34711
    sprite('la450_03', 5)	# 34712-34716
    sprite('la450_01', 5)	# 34717-34721
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 34722-34726
    sprite('la601_08', 6)	# 34727-34732
    sprite('la601_09', 6)	# 34733-34738
    sprite('la601_10', 6)	# 34739-34744
    sprite('la601_11', 8)	# 34745-34752
    sprite('la601_12', 6)	# 34753-34758
    Unknown21011(400)
    label(131)
    sprite('la000_00', 6)	# 34759-34764
    sprite('la000_01', 6)	# 34765-34770
    sprite('la000_02', 6)	# 34771-34776
    sprite('la000_03', 6)	# 34777-34782
    sprite('la000_04', 6)	# 34783-34788
    sprite('la000_05', 6)	# 34789-34794
    sprite('la000_06', 6)	# 34795-34800
    Unknown21007(24, 40)
    sprite('la000_07', 6)	# 34801-34806
    sprite('la000_08', 6)	# 34807-34812
    sprite('la000_09', 6)	# 34813-34818
    sprite('la000_10', 6)	# 34819-34824
    sprite('la000_11', 6)	# 34825-34830
    loopRest()
    gotoLabel(131)
    ExitState()
    label(140)
    sprite('la000_00', 1)	# 34831-34831
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('la000_00', 6)	# 34832-34837
    sprite('la000_01', 6)	# 34838-34843
    sprite('la000_02', 6)	# 34844-34849
    sprite('la000_03', 6)	# 34850-34855
    sprite('la000_04', 6)	# 34856-34861
    sprite('la000_05', 6)	# 34862-34867
    sprite('la000_06', 6)	# 34868-34873
    sprite('la000_07', 6)	# 34874-34879
    sprite('la000_08', 6)	# 34880-34885
    sprite('la000_09', 6)	# 34886-34891
    sprite('la000_10', 6)	# 34892-34897
    sprite('la000_11', 6)	# 34898-34903
    loopRest()
    gotoLabel(141)
    label(142)
    sprite('la001_00', 6)	# 34904-34909
    SFX_1('pla601bno')
    sprite('la001_01', 6)	# 34910-34915
    sprite('la001_02', 6)	# 34916-34921
    sprite('la001_03', 6)	# 34922-34927
    sprite('la001_04', 6)	# 34928-34933
    sprite('la001_05', 6)	# 34934-34939
    sprite('la001_06', 6)	# 34940-34945
    sprite('la001_07', 6)	# 34946-34951
    sprite('la001_08', 6)	# 34952-34957
    label(143)
    sprite('la001_05', 6)	# 34958-34963
    sprite('la001_06', 6)	# 34964-34969
    sprite('la001_07', 6)	# 34970-34975
    sprite('la001_08', 6)	# 34976-34981
    if SLOT_97:
        _gotolabel(143)
    sprite('la001_05', 6)	# 34982-34987
    sprite('la001_06', 6)	# 34988-34993
    sprite('la001_07', 6)	# 34994-34999
    sprite('la001_08', 6)	# 35000-35005
    sprite('la001_04', 6)	# 35006-35011
    sprite('la001_03', 6)	# 35012-35017
    Unknown23018(1)
    label(144)
    sprite('la000_00', 6)	# 35018-35023
    sprite('la000_01', 6)	# 35024-35029
    sprite('la000_02', 6)	# 35030-35035
    sprite('la000_03', 6)	# 35036-35041
    sprite('la000_04', 6)	# 35042-35047
    sprite('la000_05', 6)	# 35048-35053
    sprite('la000_06', 6)	# 35054-35059
    sprite('la000_07', 6)	# 35060-35065
    sprite('la000_08', 6)	# 35066-35071
    sprite('la000_09', 6)	# 35072-35077
    sprite('la000_10', 6)	# 35078-35083
    sprite('la000_11', 6)	# 35084-35089
    loopRest()
    gotoLabel(144)
    ExitState()
    label(150)
    sprite('la601_00', 6)	# 35090-35095
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 35096-35101
    sprite('la601_02', 6)	# 35102-35107
    label(151)
    sprite('la601_00', 6)	# 35108-35113
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 35114-35119
    sprite('la601_02', 6)	# 35120-35125
    sprite('la601_00', 6)	# 35126-35131
    sprite('la601_01', 6)	# 35132-35137
    sprite('la601_02', 6)	# 35138-35143
    gotoLabel(151)
    label(152)
    sprite('la601_03', 6)	# 35144-35149
    sprite('la601_04', 6)	# 35150-35155
    SFX_1('pla601bny')
    sprite('la601_05', 6)	# 35156-35161
    sprite('la601_06', 6)	# 35162-35167
    sprite('la601_07', 6)	# 35168-35173
    sprite('la450_01', 5)	# 35174-35178
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 35179-35183
    sprite('la450_03', 5)	# 35184-35188
    sprite('la450_01', 5)	# 35189-35193
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 35194-35198
    sprite('la601_08', 6)	# 35199-35204
    sprite('la601_09', 6)	# 35205-35210
    sprite('la601_10', 6)	# 35211-35216
    sprite('la601_11', 8)	# 35217-35224
    sprite('la601_12', 6)	# 35225-35230
    Unknown23018(1)
    label(153)
    sprite('la000_00', 6)	# 35231-35236
    sprite('la000_01', 6)	# 35237-35242
    sprite('la000_02', 6)	# 35243-35248
    sprite('la000_03', 6)	# 35249-35254
    sprite('la000_04', 6)	# 35255-35260
    sprite('la000_05', 6)	# 35261-35266
    sprite('la000_06', 6)	# 35267-35272
    sprite('la000_07', 6)	# 35273-35278
    sprite('la000_08', 6)	# 35279-35284
    sprite('la000_09', 6)	# 35285-35290
    sprite('la000_10', 6)	# 35291-35296
    sprite('la000_11', 6)	# 35297-35302
    loopRest()
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('la601_00', 6)	# 35303-35308
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 35309-35314
    sprite('la601_02', 6)	# 35315-35320
    label(161)
    sprite('la601_00', 6)	# 35321-35326
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 35327-35332
    sprite('la601_02', 6)	# 35333-35338
    sprite('la601_00', 6)	# 35339-35344
    sprite('la601_01', 6)	# 35345-35350
    sprite('la601_02', 6)	# 35351-35356
    gotoLabel(161)
    label(162)
    sprite('la601_00', 6)	# 35357-35362
    SFX_1('pla601bpt')
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 35363-35368
    sprite('la601_02', 6)	# 35369-35374
    Unknown2037(5)
    label(163)
    sprite('la601_00', 6)	# 35375-35380
    sprite('la601_01', 6)	# 35381-35386
    sprite('la601_02', 6)	# 35387-35392
    sprite('la601_00', 6)	# 35393-35398
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 35399-35404
    sprite('la601_02', 6)	# 35405-35410
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(163)
    sprite('la601_00', 6)	# 35411-35416
    sprite('la601_01', 6)	# 35417-35422
    sprite('la601_02', 6)	# 35423-35428
    sprite('la601_03', 6)	# 35429-35434
    sprite('la601_04', 6)	# 35435-35440
    sprite('la601_05', 6)	# 35441-35446
    sprite('la601_06', 6)	# 35447-35452
    sprite('la601_07', 6)	# 35453-35458
    sprite('la450_01', 5)	# 35459-35463
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 35464-35468
    sprite('la450_03', 5)	# 35469-35473
    sprite('la450_01', 5)	# 35474-35478
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 35479-35483
    sprite('la601_08', 6)	# 35484-35489
    sprite('la601_09', 6)	# 35490-35495
    sprite('la601_10', 6)	# 35496-35501
    sprite('la601_11', 8)	# 35502-35509
    sprite('la601_12', 6)	# 35510-35515
    Unknown23018(1)
    label(164)
    sprite('la000_00', 6)	# 35516-35521
    sprite('la000_01', 6)	# 35522-35527
    sprite('la000_02', 6)	# 35528-35533
    sprite('la000_03', 6)	# 35534-35539
    sprite('la000_04', 6)	# 35540-35545
    sprite('la000_05', 6)	# 35546-35551
    sprite('la000_06', 6)	# 35552-35557
    sprite('la000_07', 6)	# 35558-35563
    sprite('la000_08', 6)	# 35564-35569
    sprite('la000_09', 6)	# 35570-35575
    sprite('la000_10', 6)	# 35576-35581
    sprite('la000_11', 6)	# 35582-35587
    loopRest()
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('la600_00', 32767)	# 35588-68354
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-1959900)
        Unknown2019(500)
    else:
        Unknown1000(-2194900)
    teleportRelativeY(300000)
    Unknown3038(1)

    def upon_40():
        clearUponHandler(40)
        Unknown3038(0)
        sendToLabel(171)
    label(171)
    sprite('la600_00', 5)	# 68355-68359
    physicsXImpulse(40000)
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 68360-68364
    sprite('la600_00', 5)	# 68365-68369
    sprite('la600_01', 5)	# 68370-68374
    sprite('la600_00', 5)	# 68375-68379
    sprite('la600_01', 5)	# 68380-68384
    sprite('la600_00', 5)	# 68385-68389
    sprite('la600_01', 5)	# 68390-68394
    sprite('la600_00', 5)	# 68395-68399
    sprite('la600_01', 5)	# 68400-68404
    sprite('la600_00', 20)	# 68405-68424
    physicsXImpulse(0)
    Unknown2005()
    sprite('la600_00', 1)	# 68425-68425
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    Unknown26('laef600burner_add')
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 68426-68430
    physicsXImpulse(40000)
    sprite('la600_00', 5)	# 68431-68435
    sprite('la600_01', 5)	# 68436-68440
    sprite('la600_00', 5)	# 68441-68445
    physicsXImpulse(20000)
    sprite('la600_01', 5)	# 68446-68450
    sprite('la600_00', 5)	# 68451-68455
    physicsXImpulse(10000)
    sprite('la600_01', 5)	# 68456-68460
    sprite('la600_00', 5)	# 68461-68465
    sprite('la600_01', 2)	# 68466-68467
    sprite('la600_02', 4)	# 68468-68471
    Unknown2005()
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner_b', 0)
    GFX_0('laef600burner2_b', 1)
    GFX_0('laef600burner3_b', 2)
    GFX_0('laef600burner4_b', 3)
    Unknown26('laef600burner_add')
    SFX_3('down_steal_m')
    sprite('la600_03', 4)	# 68472-68475
    physicsYImpulse(-10000)
    Unknown26('laef600burner_b')
    Unknown26('laef600burner2_b')
    Unknown26('laef600burner3_b')
    Unknown26('laef600burner4_b')
    GFX_0('laef600burner_c', 0)
    GFX_0('laef600burner2_c', 1)
    GFX_0('laef600burner3_c', 2)
    GFX_0('laef600burner4_c', 3)
    sprite('la600_04', 4)	# 68476-68479
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner_c')
    Unknown26('laef600burner2_c')
    Unknown26('laef600burner3_c')
    Unknown26('laef600burner4_c')
    GFX_0('laef600_wing', 100)
    SFX_3('airdash_m')
    sprite('la600_05', 4)	# 68480-68483
    sendToLabelUpon(2, 173)
    label(172)
    sprite('la600_04', 4)	# 68484-68487
    sprite('la600_05', 4)	# 68488-68491
    loopRest()
    gotoLabel(172)
    label(173)
    clearUponHandler(2)
    sprite('la600_06', 4)	# 68492-68495
    Unknown8000(-1, 1, 1)
    physicsXImpulse(0)
    teleportRelativeX(-100)
    sprite('la600_07', 4)	# 68496-68499
    sprite('la600_08', 4)	# 68500-68503
    sprite('la600_09', 4)	# 68504-68507
    sprite('la600_10', 24)	# 68508-68531
    Unknown26('laef600_wing')
    GFX_0('laef600_axe', 100)
    sprite('la600_10', 10)	# 68532-68541
    SFX_3('highjump_m')
    sprite('la600_10', 10)	# 68542-68551
    SFX_3('attack_offset_shot')
    SFX_3('down_steal_m')
    sprite('la600_11', 4)	# 68552-68555
    SFX_1('pla601pbc')
    SFX_3('damage_hit_m')
    sprite('la600_12', 4)	# 68556-68559
    sprite('la600_13', 4)	# 68560-68563
    sprite('la600_14', 4)	# 68564-68567
    sprite('la600_15', 4)	# 68568-68571
    SFX_3('slash_sword_middle')
    sprite('la600_16', 6)	# 68572-68577
    sprite('la600_17', 6)	# 68578-68583
    sprite('la600_18', 6)	# 68584-68589
    sprite('la600_19', 6)	# 68590-68595
    sprite('la600_20', 6)	# 68596-68601
    sprite('la201_08', 6)	# 68602-68607
    sprite('la432_18', 6)	# 68608-68613
    Unknown23018(1)
    label(174)
    sprite('la000_00', 6)	# 68614-68619
    sprite('la000_01', 6)	# 68620-68625
    sprite('la000_02', 6)	# 68626-68631
    sprite('la000_03', 6)	# 68632-68637
    sprite('la000_04', 6)	# 68638-68643
    sprite('la000_05', 6)	# 68644-68649
    sprite('la000_06', 6)	# 68650-68655
    sprite('la000_07', 6)	# 68656-68661
    sprite('la000_08', 6)	# 68662-68667
    sprite('la000_09', 6)	# 68668-68673
    sprite('la000_10', 6)	# 68674-68679
    sprite('la000_11', 6)	# 68680-68685
    loopRest()
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('la000_00', 1)	# 68686-68686
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('la000_00', 6)	# 68687-68692
    sprite('la000_01', 6)	# 68693-68698
    sprite('la000_02', 6)	# 68699-68704
    sprite('la000_03', 6)	# 68705-68710
    sprite('la000_04', 6)	# 68711-68716
    sprite('la000_05', 6)	# 68717-68722
    sprite('la000_06', 6)	# 68723-68728
    sprite('la000_07', 6)	# 68729-68734
    sprite('la000_08', 6)	# 68735-68740
    sprite('la000_09', 6)	# 68741-68746
    sprite('la000_10', 6)	# 68747-68752
    sprite('la000_11', 6)	# 68753-68758
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('la001_00', 6)	# 68759-68764
    SFX_1('pla601pyu')
    sprite('la001_01', 6)	# 68765-68770
    sprite('la001_02', 6)	# 68771-68776
    sprite('la001_03', 6)	# 68777-68782
    sprite('la001_04', 6)	# 68783-68788
    sprite('la001_05', 6)	# 68789-68794
    sprite('la001_06', 6)	# 68795-68800
    sprite('la001_07', 6)	# 68801-68806
    sprite('la001_08', 6)	# 68807-68812
    label(183)
    sprite('la001_05', 6)	# 68813-68818
    sprite('la001_06', 6)	# 68819-68824
    sprite('la001_07', 6)	# 68825-68830
    sprite('la001_08', 6)	# 68831-68836
    if SLOT_97:
        _gotolabel(183)
    sprite('la001_05', 6)	# 68837-68842
    sprite('la001_06', 6)	# 68843-68848
    sprite('la001_07', 6)	# 68849-68854
    sprite('la001_08', 6)	# 68855-68860
    sprite('la001_04', 6)	# 68861-68866
    sprite('la001_03', 6)	# 68867-68872
    Unknown23018(1)
    label(184)
    sprite('la000_00', 6)	# 68873-68878
    sprite('la000_01', 6)	# 68879-68884
    sprite('la000_02', 6)	# 68885-68890
    sprite('la000_03', 6)	# 68891-68896
    sprite('la000_04', 6)	# 68897-68902
    sprite('la000_05', 6)	# 68903-68908
    sprite('la000_06', 6)	# 68909-68914
    sprite('la000_07', 6)	# 68915-68920
    sprite('la000_08', 6)	# 68921-68926
    sprite('la000_09', 6)	# 68927-68932
    sprite('la000_10', 6)	# 68933-68938
    sprite('la000_11', 6)	# 68939-68944
    loopRest()
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('la600_00', 32767)	# 68945-101711
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-1959900)
    else:
        Unknown1000(-2194900)
    teleportRelativeY(300000)
    Unknown3038(1)

    def upon_40():
        clearUponHandler(40)
        Unknown3038(0)
        sendToLabel(191)
    label(191)
    sprite('la600_00', 5)	# 101712-101716
    physicsXImpulse(40000)
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 101717-101721
    sprite('la600_00', 5)	# 101722-101726
    sprite('la600_01', 5)	# 101727-101731
    sprite('la600_00', 5)	# 101732-101736
    sprite('la600_01', 5)	# 101737-101741
    sprite('la600_00', 5)	# 101742-101746
    sprite('la600_01', 5)	# 101747-101751
    sprite('la600_00', 5)	# 101752-101756
    sprite('la600_01', 5)	# 101757-101761
    sprite('la600_00', 20)	# 101762-101781
    physicsXImpulse(0)
    Unknown2005()
    sprite('la600_00', 1)	# 101782-101782
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner', 0)
    GFX_0('laef600burner2', 1)
    GFX_0('laef600burner3', 2)
    GFX_0('laef600burner4', 3)
    Unknown26('laef600burner_add')
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    SFX_3('la001')
    sprite('la600_01', 5)	# 101783-101787
    physicsXImpulse(40000)
    sprite('la600_00', 5)	# 101788-101792
    sprite('la600_01', 5)	# 101793-101797
    sprite('la600_00', 5)	# 101798-101802
    physicsXImpulse(20000)
    sprite('la600_01', 5)	# 101803-101807
    sprite('la600_00', 5)	# 101808-101812
    physicsXImpulse(10000)
    sprite('la600_01', 5)	# 101813-101817
    sprite('la600_00', 5)	# 101818-101822
    sprite('la600_01', 2)	# 101823-101824
    sprite('la600_02', 4)	# 101825-101828
    Unknown2005()
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner')
    Unknown26('laef600burner2')
    Unknown26('laef600burner3')
    Unknown26('laef600burner4')
    GFX_0('laef600burner_b', 0)
    GFX_0('laef600burner2_b', 1)
    GFX_0('laef600burner3_b', 2)
    GFX_0('laef600burner4_b', 3)
    Unknown26('laef600burner_add')
    SFX_3('down_steal_m')
    sprite('la600_03', 4)	# 101829-101832
    physicsYImpulse(-10000)
    Unknown26('laef600burner_b')
    Unknown26('laef600burner2_b')
    Unknown26('laef600burner3_b')
    Unknown26('laef600burner4_b')
    GFX_0('laef600burner_c', 0)
    GFX_0('laef600burner2_c', 1)
    GFX_0('laef600burner3_c', 2)
    GFX_0('laef600burner4_c', 3)
    sprite('la600_04', 4)	# 101833-101836
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    Unknown26('laef600burner_c')
    Unknown26('laef600burner2_c')
    Unknown26('laef600burner3_c')
    Unknown26('laef600burner4_c')
    GFX_0('laef600_wing', 100)
    SFX_3('airdash_m')
    sprite('la600_05', 4)	# 101837-101840
    sendToLabelUpon(2, 193)
    label(192)
    sprite('la600_04', 4)	# 101841-101844
    sprite('la600_05', 4)	# 101845-101848
    loopRest()
    gotoLabel(192)
    label(193)
    clearUponHandler(2)
    sprite('la600_06', 4)	# 101849-101852
    Unknown8000(-1, 1, 1)
    physicsXImpulse(0)
    teleportRelativeX(-100)
    sprite('la600_07', 4)	# 101853-101856
    sprite('la600_08', 4)	# 101857-101860
    sprite('la600_09', 4)	# 101861-101864
    sprite('la600_10', 24)	# 101865-101888
    Unknown26('laef600_wing')
    GFX_0('laef600_axe', 100)
    sprite('la600_10', 10)	# 101889-101898
    SFX_3('highjump_m')
    sprite('la600_10', 10)	# 101899-101908
    SFX_3('attack_offset_shot')
    SFX_3('down_steal_m')
    sprite('la600_11', 4)	# 101909-101912
    SFX_1('pla601ryn')
    SFX_3('damage_hit_m')
    sprite('la600_12', 4)	# 101913-101916
    sprite('la600_13', 4)	# 101917-101920
    sprite('la600_14', 4)	# 101921-101924
    sprite('la600_15', 4)	# 101925-101928
    SFX_3('slash_sword_middle')
    sprite('la600_16', 6)	# 101929-101934
    sprite('la600_17', 6)	# 101935-101940
    sprite('la600_18', 6)	# 101941-101946
    sprite('la600_19', 6)	# 101947-101952
    sprite('la600_20', 6)	# 101953-101958
    sprite('la201_08', 6)	# 101959-101964
    sprite('la432_18', 6)	# 101965-101970
    Unknown23018(1)
    label(194)
    sprite('la000_00', 6)	# 101971-101976
    sprite('la000_01', 6)	# 101977-101982
    sprite('la000_02', 6)	# 101983-101988
    sprite('la000_03', 6)	# 101989-101994
    sprite('la000_04', 6)	# 101995-102000
    sprite('la000_05', 6)	# 102001-102006
    sprite('la000_06', 6)	# 102007-102012
    sprite('la000_07', 6)	# 102013-102018
    sprite('la000_08', 6)	# 102019-102024
    sprite('la000_09', 6)	# 102025-102030
    sprite('la000_10', 6)	# 102031-102036
    sprite('la000_11', 6)	# 102037-102042
    loopRest()
    gotoLabel(194)
    ExitState()
    label(200)
    sprite('la601_00', 6)	# 102043-102048
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 102049-102054
    sprite('la601_02', 6)	# 102055-102060
    label(201)
    sprite('la601_00', 6)	# 102061-102066
    SFX_3('cloth_l')
    sprite('la601_01', 6)	# 102067-102072
    sprite('la601_02', 6)	# 102073-102078
    sprite('la601_00', 6)	# 102079-102084
    sprite('la601_01', 6)	# 102085-102090
    sprite('la601_02', 6)	# 102091-102096
    gotoLabel(201)
    label(202)
    sprite('la601_03', 6)	# 102097-102102
    sprite('la601_04', 6)	# 102103-102108
    SFX_1('pla601uli')
    sprite('la601_05', 6)	# 102109-102114
    sprite('la601_06', 6)	# 102115-102120
    sprite('la601_07', 6)	# 102121-102126
    sprite('la450_01', 5)	# 102127-102131
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 102132-102136
    sprite('la450_03', 5)	# 102137-102141
    sprite('la450_01', 5)	# 102142-102146
    SFX_3('slash_blade_middle')
    sprite('la450_02', 5)	# 102147-102151
    sprite('la601_08', 6)	# 102152-102157
    sprite('la601_09', 6)	# 102158-102163
    sprite('la601_10', 6)	# 102164-102169
    sprite('la601_11', 8)	# 102170-102177
    sprite('la601_12', 6)	# 102178-102183
    Unknown23018(1)
    label(203)
    sprite('la000_00', 6)	# 102184-102189
    sprite('la000_01', 6)	# 102190-102195
    sprite('la000_02', 6)	# 102196-102201
    sprite('la000_03', 6)	# 102202-102207
    sprite('la000_04', 6)	# 102208-102213
    sprite('la000_05', 6)	# 102214-102219
    sprite('la000_06', 6)	# 102220-102225
    sprite('la000_07', 6)	# 102226-102231
    sprite('la000_08', 6)	# 102232-102237
    sprite('la000_09', 6)	# 102238-102243
    sprite('la000_10', 6)	# 102244-102249
    sprite('la000_11', 6)	# 102250-102255
    loopRest()
    gotoLabel(203)
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
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    sprite('keep', 1)	# 4-4
    if SLOT_158:
        if (not SLOT_52):
            if random_(2, 0, 33):
                sendToLabel(10)
            if random_(2, 0, 50):
                sendToLabel(20)
        elif random_(2, 0, 50):
            sendToLabel(20)
    elif random_(2, 0, 50):
        sendToLabel(20)
    label(0)
    sprite('la610_00', 4)	# 5-8
    sprite('la610_01', 4)	# 9-12
    Unknown23029(11, 1001, 0)
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 13-16
    sprite('la610_03', 4)	# 17-20
    sprite('la610_04', 4)	# 21-24
    sprite('la610_05', 4)	# 25-28
    sprite('la610_06', 10)	# 29-38
    sprite('la610_07', 6)	# 39-44
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 45-54
    sprite('la610_09', 6)	# 55-60
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pla525', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pla402_0', 100, 878799984, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('', 0, 895577200, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('la610_10', 6)	# 61-66
    SFX_3('cloth_h')
    Unknown23018(1)
    label(1)
    sprite('la610_11', 8)	# 67-74
    sprite('la610_12', 8)	# 75-82
    sprite('la610_13', 8)	# 83-90
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('la611_00', 6)	# 91-96
    GFX_0('WinCamera', 100)
    if SLOT_158:
        if SLOT_108:
            Unknown7006('pla402_0', 100, 878799984, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pla520', 100, 895577200, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('la611_01', 6)	# 97-102
    sprite('la611_02', 6)	# 103-108
    sprite('la611_03', 6)	# 109-114
    sprite('la611_04', 6)	# 115-120
    sprite('la611_05', 6)	# 121-126
    SFX_3('slash_blade_middle')
    sprite('la611_06', 6)	# 127-132
    sprite('la611_07', 6)	# 133-138
    sprite('la611_08', 6)	# 139-144
    sprite('la611_09', 6)	# 145-150
    sprite('la611_10', 6)	# 151-156
    sprite('la611_11', 6)	# 157-162
    sprite('la611_12', 6)	# 163-168
    sprite('la611_13', 6)	# 169-174
    sprite('la611_14', 8)	# 175-182
    GFX_1('laef_win2_attach', 0)
    SFX_3('damage_hit_m')
    sprite('la611_15', 8)	# 183-190
    sprite('la611_16', 6)	# 191-196
    GFX_0('laef_win2_burner', 0)
    GFX_0('laef_win2_burner2', 1)
    GFX_0('laef_win2_burner3', 2)
    sprite('la611_17', 6)	# 197-202
    physicsYImpulse(10000)
    setGravity(-100)
    SFX_3('la012')
    Unknown26('laef_win2_burner')
    Unknown26('laef_win2_burner2')
    Unknown26('laef_win2_burner3')
    GFX_0('laef_win2_burner_b', 0)
    GFX_0('laef_win2_burner_b2', 1)
    GFX_0('laef_win2_burner_b3', 2)
    GFX_0('laef600burner_add', 0)
    GFX_0('laef600burner_add', 1)
    GFX_0('laef600burner_add', 2)
    GFX_1('laef_win2_smoke', 100)
    SFX_3('la001')
    sprite('la611_18', 6)	# 203-208
    sprite('la611_17', 6)	# 209-214
    setGravity(-500)
    SFX_3('la012')
    sprite('la611_18', 6)	# 215-220
    sprite('la611_17', 6)	# 221-226
    setGravity(-900)
    SFX_3('la012')
    sprite('la611_18', 6)	# 227-232
    SFX_3('la001')
    Unknown23018(1)
    label(11)
    sprite('la611_17', 6)	# 233-238
    sprite('la611_18', 6)	# 239-244
    gotoLabel(11)
    label(20)
    sprite('la610_00', 4)	# 245-248
    sprite('la610_01', 4)	# 249-252
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 253-256
    sprite('la610_03', 4)	# 257-260
    sprite('la610_04', 4)	# 261-264
    sprite('la610_05', 4)	# 265-268
    sprite('la610_06', 10)	# 269-278
    sprite('la610_07', 6)	# 279-284
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 285-294
    sprite('la651_00', 6)	# 295-300
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pla525', 100, 895577200, 13362, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pla402_0', 100, 878799984, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('', 0, 895577200, 12850, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('la651_01', 32767)	# 301-33067
    Unknown23018(1)
    label(100)
    sprite('la610_00', 4)	# 33068-33071
    sprite('la610_01', 4)	# 33072-33075
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 33076-33079
    sprite('la610_03', 4)	# 33080-33083
    sprite('la610_04', 4)	# 33084-33087
    sprite('la610_05', 4)	# 33088-33091
    sprite('la610_06', 10)	# 33092-33101
    sprite('la610_07', 6)	# 33102-33107
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 33108-33117
    sprite('la651_00', 6)	# 33118-33123
    SFX_1('pla700bno')
    label(101)
    sprite('la651_01', 1)	# 33124-33124
    if SLOT_97:
        _gotolabel(101)
    sprite('la651_01', 20)	# 33125-33144
    sprite('la651_01', 32767)	# 33145-65911
    Unknown21007(24, 40)
    Unknown21011(360)
    label(110)
    sprite('la205_00', 4)	# 65912-65915

    def upon_40():
        clearUponHandler(40)
        sendToLabel(113)
    sprite('la205_01', 5)	# 65916-65920
    sprite('la205_02', 5)	# 65921-65925
    sprite('la205_03', 5)	# 65926-65930
    SFX_1('pla700pbc')
    sprite('la205_04', 5)	# 65931-65935
    sprite('la205_05', 5)	# 65936-65940
    SFX_3('cloth_m')
    label(111)
    sprite('la205_03', 5)	# 65941-65945
    sprite('la205_04', 5)	# 65946-65950
    sprite('la205_05', 5)	# 65951-65955
    if SLOT_97:
        _gotolabel(111)
    sprite('la205_03', 1)	# 65956-65956
    Unknown21007(24, 40)
    label(112)
    sprite('la205_03', 5)	# 65957-65961
    sprite('la205_04', 5)	# 65962-65966
    sprite('la205_05', 5)	# 65967-65971
    gotoLabel(112)
    label(113)
    sprite('la205_06', 4)	# 65972-65975
    sprite('la205_07', 4)	# 65976-65979
    sprite('la610_00', 4)	# 65980-65983
    SFX_1('pla702pbc')
    sprite('la610_01', 4)	# 65984-65987
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 65988-65991
    sprite('la610_03', 4)	# 65992-65995
    sprite('la610_04', 4)	# 65996-65999
    sprite('la610_05', 4)	# 66000-66003
    sprite('la610_06', 10)	# 66004-66013
    sprite('la610_07', 6)	# 66014-66019
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 66020-66029
    sprite('la610_09', 6)	# 66030-66035
    sprite('la610_10', 6)	# 66036-66041
    SFX_3('cloth_h')
    Unknown23018(1)
    label(114)
    sprite('la610_11', 8)	# 66042-66049
    sprite('la610_12', 8)	# 66050-66057
    sprite('la610_13', 8)	# 66058-66065
    loopRest()
    gotoLabel(114)
    label(120)
    sprite('la610_00', 4)	# 66066-66069
    sprite('la610_01', 4)	# 66070-66073
    SFX_1('pla700pyu')
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 66074-66077
    sprite('la610_03', 4)	# 66078-66081
    sprite('la610_04', 4)	# 66082-66085
    sprite('la610_05', 4)	# 66086-66089
    sprite('la610_06', 10)	# 66090-66099
    sprite('la610_07', 6)	# 66100-66105
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 66106-66115
    sprite('la651_00', 6)	# 66116-66121
    label(121)
    sprite('la651_01', 1)	# 66122-66122
    if SLOT_97:
        _gotolabel(121)
    sprite('la651_01', 32767)	# 66123-98889
    Unknown21007(24, 40)
    Unknown21011(200)
    label(130)
    sprite('la610_00', 4)	# 98890-98893
    sprite('la610_01', 4)	# 98894-98897
    Unknown23029(11, 1001, 0)
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 98898-98901
    sprite('la610_03', 4)	# 98902-98905
    sprite('la610_04', 4)	# 98906-98909
    sprite('la610_05', 4)	# 98910-98913
    sprite('la610_06', 10)	# 98914-98923
    sprite('la610_07', 6)	# 98924-98929
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 98930-98939
    sprite('la610_09', 6)	# 98940-98945
    SFX_1('pla700rrb')
    sprite('la610_10', 6)	# 98946-98951
    SFX_3('cloth_h')
    label(131)
    sprite('la610_11', 8)	# 98952-98959
    sprite('la610_12', 8)	# 98960-98967
    sprite('la610_13', 8)	# 98968-98975
    loopRest()
    if SLOT_97:
        _gotolabel(131)
    sprite('la610_11', 1)	# 98976-98976
    Unknown21007(24, 40)
    Unknown21011(180)
    label(132)
    sprite('la610_11', 8)	# 98977-98984
    sprite('la610_12', 8)	# 98985-98992
    sprite('la610_13', 8)	# 98993-99000
    loopRest()
    gotoLabel(132)
    label(140)
    sprite('la000_00', 1)	# 99001-99001

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('la000_00', 6)	# 99002-99007
    sprite('la000_01', 6)	# 99008-99013
    sprite('la000_02', 6)	# 99014-99019
    sprite('la000_03', 6)	# 99020-99025
    sprite('la000_04', 6)	# 99026-99031
    sprite('la000_05', 6)	# 99032-99037
    sprite('la000_06', 6)	# 99038-99043
    sprite('la000_07', 6)	# 99044-99049
    sprite('la000_08', 6)	# 99050-99055
    sprite('la000_09', 6)	# 99056-99061
    sprite('la000_10', 6)	# 99062-99067
    sprite('la000_11', 6)	# 99068-99073
    loopRest()
    gotoLabel(141)
    label(142)
    sprite('keep', 1)	# 99074-99074
    if SLOT_2:
        sendToLabel(143)
    sprite('la003_00', 4)	# 99075-99078
    Unknown2005()
    sprite('la003_01', 4)	# 99079-99082
    sprite('la003_02', 4)	# 99083-99086
    label(143)
    sprite('la610_00', 4)	# 99087-99090
    sprite('la610_01', 4)	# 99091-99094
    SFX_1('pla701bes')
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 99095-99098
    sprite('la610_03', 4)	# 99099-99102
    sprite('la610_04', 4)	# 99103-99106
    sprite('la610_05', 4)	# 99107-99110
    sprite('la610_06', 10)	# 99111-99120
    sprite('la610_07', 6)	# 99121-99126
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 99127-99136
    sprite('la651_00', 6)	# 99137-99142
    sprite('la651_01', 32767)	# 99143-131909
    Unknown23018(1)
    label(150)
    sprite('la000_00', 1)	# 131910-131910

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('la000_00', 6)	# 131911-131916
    sprite('la000_01', 6)	# 131917-131922
    sprite('la000_02', 6)	# 131923-131928
    sprite('la000_03', 6)	# 131929-131934
    sprite('la000_04', 6)	# 131935-131940
    sprite('la000_05', 6)	# 131941-131946
    sprite('la000_06', 6)	# 131947-131952
    sprite('la000_07', 6)	# 131953-131958
    sprite('la000_08', 6)	# 131959-131964
    sprite('la000_09', 6)	# 131965-131970
    sprite('la000_10', 6)	# 131971-131976
    sprite('la000_11', 6)	# 131977-131982
    loopRest()
    gotoLabel(151)
    label(152)
    sprite('la610_00', 4)	# 131983-131986
    sprite('la610_01', 4)	# 131987-131990
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 131991-131994
    SFX_1('pla701bny')
    sprite('la610_03', 4)	# 131995-131998
    sprite('la610_04', 4)	# 131999-132002
    sprite('la610_05', 4)	# 132003-132006
    sprite('la610_06', 10)	# 132007-132016
    sprite('la610_07', 6)	# 132017-132022
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 132023-132032
    sprite('la610_09', 6)	# 132033-132038
    sprite('la610_10', 6)	# 132039-132044
    SFX_3('cloth_h')
    Unknown23018(1)
    label(153)
    sprite('la610_11', 8)	# 132045-132052
    sprite('la610_12', 8)	# 132053-132060
    sprite('la610_13', 8)	# 132061-132068
    loopRest()
    gotoLabel(153)
    label(160)
    sprite('la000_00', 1)	# 132069-132069

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('la000_00', 6)	# 132070-132075
    sprite('la000_01', 6)	# 132076-132081
    sprite('la000_02', 6)	# 132082-132087
    sprite('la000_03', 6)	# 132088-132093
    sprite('la000_04', 6)	# 132094-132099
    sprite('la000_05', 6)	# 132100-132105
    sprite('la000_06', 6)	# 132106-132111
    sprite('la000_07', 6)	# 132112-132117
    sprite('la000_08', 6)	# 132118-132123
    sprite('la000_09', 6)	# 132124-132129
    sprite('la000_10', 6)	# 132130-132135
    sprite('la000_11', 6)	# 132136-132141
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('keep', 1)	# 132142-132142
    if SLOT_2:
        sendToLabel(163)
    sprite('la003_00', 4)	# 132143-132146
    Unknown2005()
    sprite('la003_01', 4)	# 132147-132150
    sprite('la003_02', 4)	# 132151-132154
    label(163)
    sprite('la610_00', 4)	# 132155-132158
    sprite('la610_01', 4)	# 132159-132162
    SFX_1('pla701bpt')
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 132163-132166
    sprite('la610_03', 4)	# 132167-132170
    sprite('la610_04', 4)	# 132171-132174
    sprite('la610_05', 4)	# 132175-132178
    sprite('la610_06', 10)	# 132179-132188
    sprite('la610_07', 6)	# 132189-132194
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 132195-132204
    sprite('la651_00', 6)	# 132205-132210
    sprite('la651_01', 32767)	# 132211-164977
    Unknown23018(1)
    label(170)
    sprite('la000_00', 1)	# 164978-164978

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('la000_00', 6)	# 164979-164984
    sprite('la000_01', 6)	# 164985-164990
    sprite('la000_02', 6)	# 164991-164996
    sprite('la000_03', 6)	# 164997-165002
    sprite('la000_04', 6)	# 165003-165008
    sprite('la000_05', 6)	# 165009-165014
    sprite('la000_06', 6)	# 165015-165020
    sprite('la000_07', 6)	# 165021-165026
    sprite('la000_08', 6)	# 165027-165032
    sprite('la000_09', 6)	# 165033-165038
    sprite('la000_10', 6)	# 165039-165044
    sprite('la000_11', 6)	# 165045-165050
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('keep', 1)	# 165051-165051
    if (SLOT_38 == 1):
        if (SLOT_152 == 1):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                Unknown2037(1)
    if (SLOT_38 == 0):
        if (SLOT_152 == 0):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                Unknown2037(1)
    if (not SLOT_2):
        sendToLabel(173)
    sprite('la003_00', 4)	# 165052-165055
    Unknown2005()
    sprite('la003_01', 4)	# 165056-165059
    sprite('la003_02', 4)	# 165060-165063
    label(173)
    sprite('la610_00', 4)	# 165064-165067
    sprite('la610_01', 4)	# 165068-165071
    SFX_1('pla701pag')
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 165072-165075
    sprite('la610_03', 4)	# 165076-165079
    sprite('la610_04', 4)	# 165080-165083
    sprite('la610_05', 4)	# 165084-165087
    sprite('la610_06', 10)	# 165088-165097
    sprite('la610_07', 6)	# 165098-165103
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 165104-165113
    sprite('la651_00', 6)	# 165114-165119
    sprite('la651_01', 32767)	# 165120-197886
    Unknown23018(1)
    label(180)
    sprite('la000_00', 1)	# 197887-197887

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('la000_00', 6)	# 197888-197893
    sprite('la000_01', 6)	# 197894-197899
    sprite('la000_02', 6)	# 197900-197905
    sprite('la000_03', 6)	# 197906-197911
    sprite('la000_04', 6)	# 197912-197917
    sprite('la000_05', 6)	# 197918-197923
    sprite('la000_06', 6)	# 197924-197929
    sprite('la000_07', 6)	# 197930-197935
    sprite('la000_08', 6)	# 197936-197941
    sprite('la000_09', 6)	# 197942-197947
    sprite('la000_10', 6)	# 197948-197953
    sprite('la000_11', 6)	# 197954-197959
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('la610_00', 4)	# 197960-197963
    sprite('la610_01', 4)	# 197964-197967
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 197968-197971
    sprite('la610_03', 4)	# 197972-197975
    sprite('la610_04', 4)	# 197976-197979
    sprite('la610_05', 4)	# 197980-197983
    sprite('la610_06', 10)	# 197984-197993
    sprite('la610_07', 6)	# 197994-197999
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 198000-198009
    sprite('la651_00', 6)	# 198010-198015
    SFX_1('pla701ryn')
    sprite('la651_01', 32767)	# 198016-230782
    Unknown23018(1)
    label(190)
    sprite('la000_00', 1)	# 230783-230783

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('la000_00', 6)	# 230784-230789
    sprite('la000_01', 6)	# 230790-230795
    sprite('la000_02', 6)	# 230796-230801
    sprite('la000_03', 6)	# 230802-230807
    sprite('la000_04', 6)	# 230808-230813
    sprite('la000_05', 6)	# 230814-230819
    sprite('la000_06', 6)	# 230820-230825
    sprite('la000_07', 6)	# 230826-230831
    sprite('la000_08', 6)	# 230832-230837
    sprite('la000_09', 6)	# 230838-230843
    sprite('la000_10', 6)	# 230844-230849
    sprite('la000_11', 6)	# 230850-230855
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('la610_00', 4)	# 230856-230859
    sprite('la610_01', 4)	# 230860-230863
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 230864-230867
    sprite('la610_03', 4)	# 230868-230871
    sprite('la610_04', 4)	# 230872-230875
    sprite('la610_05', 4)	# 230876-230879
    sprite('la610_06', 10)	# 230880-230889
    sprite('la610_07', 6)	# 230890-230895
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 230896-230905
    sprite('la610_09', 6)	# 230906-230911
    SFX_1('pla701uli')
    sprite('la610_10', 6)	# 230912-230917
    SFX_3('cloth_h')
    Unknown23018(1)
    label(193)
    sprite('la610_11', 8)	# 230918-230925
    sprite('la610_12', 8)	# 230926-230933
    sprite('la610_13', 8)	# 230934-230941
    loopRest()
    gotoLabel(193)
    label(200)
    sprite('la000_00', 1)	# 230942-230942

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('la000_00', 6)	# 230943-230948
    sprite('la000_01', 6)	# 230949-230954
    sprite('la000_02', 6)	# 230955-230960
    sprite('la000_03', 6)	# 230961-230966
    sprite('la000_04', 6)	# 230967-230972
    sprite('la000_05', 6)	# 230973-230978
    sprite('la000_06', 6)	# 230979-230984
    sprite('la000_07', 6)	# 230985-230990
    sprite('la000_08', 6)	# 230991-230996
    sprite('la000_09', 6)	# 230997-231002
    sprite('la000_10', 6)	# 231003-231008
    sprite('la000_11', 6)	# 231009-231014
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('la610_00', 4)	# 231015-231018
    sprite('la610_01', 4)	# 231019-231022
    SFX_3('slash_sword_fast')
    sprite('la610_02', 4)	# 231023-231026
    sprite('la610_03', 4)	# 231027-231030
    sprite('la610_04', 4)	# 231031-231034
    sprite('la610_05', 4)	# 231035-231038
    sprite('la610_06', 10)	# 231039-231048
    sprite('la610_07', 6)	# 231049-231054
    Unknown8003(0, 1, 1)
    ScreenShake(0, 10000)
    GFX_1('laef_610_smoke', 0)
    sprite('la610_08', 10)	# 231055-231064
    sprite('la651_00', 6)	# 231065-231070
    SFX_1('pla701uyu')
    sprite('la651_01', 32767)	# 231071-263837
    Unknown23018(1)

@State
def CmnActLose():
    sprite('la070_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('pla403_0', 100, 878799984, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('la070_01', 6)	# 7-12
    sprite('la070_02', 2)	# 13-14
    Unknown23018(1)
    sprite('la070_03', 32767	# 15-32781
