@Subroutine
def PreInit():
    Unknown12019('62617a00000000000000000000000000')

@Subroutine
def MatchInit():
    Health(18000)
    DashFInitialVelocity(9000)
    DashFAccel(0)
    Unknown12038(28000)
    Unknown12034(14)
    AirBDashDuration(14)
    Unknown12024(3)
    Unknown13039(0)
    Unknown2049(1)
    Unknown23003(0, 0, 0, 1, 100000, 0, -65536, -65536)
    Unknown23004(0, 1)
    Unknown23003(1, 0, 0, 1, 100000, 0, -256, -256)
    Unknown23004(1, 1)
    Unknown23003(2, 0, 0, 1, 100000, 0, -65281, -65281)
    Unknown23004(2, 1)
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 350000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown14015(0, 250000, -100000, 300000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Unknown15008()
    Unknown15026(0, 19, 21)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown15009()
    Unknown15012(2500)
    Unknown15026(0, 14, 16)
    Unknown14015(0, 350000, -100000, 200000, 400, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown14015(0, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    Unknown15009()
    Unknown15026(1, 14, 20)
    Unknown14015(0, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown15021(3000)
    Unknown14015(-100000, 450000, -200000, 550000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15014(1)
    Unknown15012(2500)
    Unknown14015(150000, 450000, -200000, 650000, 400, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15014(1)
    Unknown15012(2500)
    Unknown15026(2, 23, 25)
    Unknown14015(0, 350000, -100000, 200000, 400, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(-300000, 300000, -250000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown14015(0, 350000, -50000, 550000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15026(1, 18, 20)
    Unknown14015(0, 400000, -250000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(50000, 200000, -450000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(500000, 850000, -100000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Derive', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('Assault')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('AZcombo1', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1500)
    Unknown14015(0, 400000, -250000, 300000, 100, 0)
    Move_EndRegister()
    Move_Register('AZcombo1_Derive', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('AZcombo1')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('AZcombo2', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15012(1)
    Unknown15015(24, 25)
    Unknown14015(0, 400000, -250000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('AZcombo3', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown14015(0, 400000, -250000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('ShotAtemi', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(2000)
    Unknown15013(1)
    Unknown14015(600000, 1000000, -200000, 200000, 250, 1)
    Move_EndRegister()
    Move_Register('ShotAtemi_Derive', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('ShotAtemi')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('Shinkyaku', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15006(1)
    Unknown14015(0, 250000, -200000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('Shinkyaku_Derive', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('Shinkyaku')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('DustAttack', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15009()
    Unknown15013(1)
    Unknown15012(1500)
    Unknown15026(2, 23, 25)
    Unknown14015(0, 400000, -100000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('DustAttack_Derive', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('DustAttack')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('HomingJump', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x93)
    Move_EndRegister()
    Move_Register('VanishingAttack', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15008()
    Unknown15013(1)
    Unknown15012(1500)
    Unknown15026(2, 23, 25)
    Unknown14015(0, 400000, -100000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('VanishingAttack_Derive', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('VanishingAttack')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('BoostDashStart', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0x7b)
    Move_EndRegister()
    Move_Register('BoostDash', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0x7b)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(3000)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(0, 350000, -200000, 350000, 250, 10)
    Move_EndRegister()
    Move_Register('InvincibleAttack_Derive', INPUT_SPECIALMOVE)
    Unknown14013('CmnActInvincibleAttack')
    Move_Input_(0xdf)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('Spartan', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown14015(0, 400000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('Spartan_Derive', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14013('Spartan')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('Spartan_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15014(3000)
    Unknown14015(0, 400000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('Spartan_OD_Derive', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14013('Spartan_OD')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('SuperPunch', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(50000)
    Unknown14015(650000, 1500000, -200000, 0, 400, 1)
    Move_EndRegister()
    Move_Register('SuperPunch_Derive', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14013('SuperPunch')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('SuperPunch_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15013(50000)
    Unknown14015(650000, 1500000, -200000, 0, 400, 1)
    Move_EndRegister()
    Move_Register('SuperPunch_OD_Derive', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14013('SuperPunch_OD')
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Unknown15024('NmlAtk4A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A2nd', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'NmlAtkAIR5C', 10000000)
    Unknown15024('AZcombo1', 'AZcombo2', 10000000)
    Unknown15024('AZcombo2', 'AZcombo3', 10000000)
    Unknown15024('DustAttack', 'HomingJump', 10000000)
    Unknown15024('VanishingAttack', 'BoostDashStart', 10000000)
    Unknown12018(0, 'az062_01')
    Unknown12018(1, 'az062_03')
    Unknown12018(2, 'az062_04')
    Unknown12018(3, 'az062_05')
    Unknown12018(4, 'az062_05')
    Unknown12018(5, 'az062_06')
    Unknown12018(6, 'az062_07')
    Unknown12018(7, 'az041_02')
    Unknown12018(8, 'az040_02')
    Unknown12018(9, 'az045_02')
    Unknown12018(10, 'az060_00')
    Unknown12018(11, 'az060_01')
    Unknown12018(12, 'az060_03')
    Unknown12018(13, 'az060_05')
    Unknown12018(14, 'az060_07')
    Unknown12018(15, 'az060_14')
    Unknown12018(16, 'az050_00')
    Unknown12018(17, 'az052_00')
    Unknown12018(18, 'az054_00')
    Unknown12018(25, 'az063_00')
    Unknown12018(26, 'az063_01')
    Unknown12018(27, 'az063_02')
    Unknown12018(28, 'az063_04')
    Unknown12018(29, 'az063_10')
    Unknown12018(24, 'az073_01')
    Unknown7010(0, 'baz000')
    Unknown7010(1, 'baz001')
    Unknown7010(2, 'baz002')
    Unknown7010(3, 'baz003')
    Unknown7010(4, 'baz004')
    Unknown7010(5, 'baz005')
    Unknown7010(6, 'baz006')
    Unknown7010(7, 'baz007')
    Unknown7010(8, 'baz008')
    Unknown7010(9, 'baz009')
    Unknown7010(10, 'baz010')
    Unknown7010(15, 'baz015')
    Unknown7010(16, 'baz016')
    Unknown7010(17, 'baz017')
    Unknown7010(18, 'baz018')
    Unknown7010(19, 'baz019')
    Unknown7010(20, 'baz020')
    Unknown7010(21, 'baz021')
    Unknown7010(22, 'baz022')
    Unknown7010(23, 'baz023')
    Unknown7010(24, 'baz024')
    Unknown7010(25, 'baz025')
    Unknown7010(28, 'baz028')
    Unknown7010(29, 'baz029')
    Unknown7010(30, 'baz030')
    Unknown7010(31, 'baz031')
    Unknown7010(32, 'baz032')
    Unknown7010(33, 'baz033')
    Unknown7010(34, 'baz034')
    Unknown7010(35, 'baz035')
    Unknown7010(36, 'baz036')
    Unknown7010(37, 'baz037')
    Unknown7010(39, 'baz039')
    Unknown7010(42, 'baz042')
    Unknown7010(43, 'baz043')
    Unknown7010(44, 'baz044')
    Unknown7010(45, 'baz045')
    Unknown7010(46, 'baz046')
    Unknown7010(47, 'baz047')
    Unknown7010(48, 'baz048')
    Unknown7010(49, 'baz049')
    Unknown7010(50, 'baz050')
    Unknown7010(52, 'baz052')
    Unknown7010(53, 'baz053')
    Unknown7010(54, 'baz100_0')
    Unknown7010(55, 'baz100_1')
    Unknown7010(56, 'baz100_2')
    Unknown7010(63, 'baz101_0')
    Unknown7010(64, 'baz101_1')
    Unknown7010(65, 'baz101_2')
    Unknown7010(57, 'baz102_0')
    Unknown7010(58, 'baz102_1')
    Unknown7010(59, 'baz102_2')
    Unknown7010(66, 'baz103_0')
    Unknown7010(67, 'baz103_1')
    Unknown7010(68, 'baz103_2')
    Unknown7010(60, 'baz104_0')
    Unknown7010(61, 'baz104_1')
    Unknown7010(62, 'baz104_2')
    Unknown7010(69, 'baz105_0')
    Unknown7010(70, 'baz105_1')
    Unknown7010(71, 'baz105_2')
    Unknown7010(72, 'baz150')
    Unknown7010(73, 'baz151')
    Unknown7010(74, 'baz152')
    Unknown7010(85, 'baz153')
    Unknown7010(87, 'baz154')
    Unknown7010(88, 'baz155')
    Unknown7010(96, 'baz161_0')
    Unknown7010(97, 'baz161_1')
    Unknown7010(92, 'baz162_0')
    Unknown7010(93, 'baz162_1')
    Unknown7010(98, 'baz163_0')
    Unknown7010(99, 'baz163_1')
    Unknown7010(100, 'baz164_0')
    Unknown7010(101, 'baz164_1')
    Unknown7010(105, 'baz165_0')
    Unknown7010(106, 'baz165_1')
    Unknown7010(102, 'baz166_0')
    Unknown7010(103, 'baz166_1')
    Unknown7010(90, 'baz167_0')
    Unknown7010(91, 'baz167_1')
    Unknown7010(107, 'baz168_0')
    Unknown7010(108, 'baz168_1')
    Unknown7010(110, 'baz169_0')
    Unknown7010(111, 'baz169_1')
    Unknown7010(94, 'baz325_0')
    Unknown7010(95, 'baz325_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000537570657250756e636800000000000000000000000000000000000000000000')
    Unknown12059('03000000537570657250756e63685f4f4400000000000000000000000000000000000000')
    Unknown12059('040000005370617274616e00000000000000000000000000000000000000000000000000')
    Unknown12059('050000005370617274616e5f4f4400000000000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_21:
            if SLOT_4:
                SLOT_4 = (SLOT_4 + (-1))
                if (not SLOT_4):
                    if SLOT_60:
                        SLOT_4 = 1
                if SLOT_30:
                    SLOT_4 = 0
                Unknown3029(1)
                Unknown3070(2)
                Unknown3071(6)
                Unknown3072('ff000000ff0000000000000000000000')
                Unknown3073('64000000640000000000000000000000')
                Unknown3076(1000)
                Unknown3077(1000)
                if (SLOT_4 < 80):
                    Unknown3072('f0000000ff0000000000000000000000')
                    Unknown3073('50000000640000000000000000000000')
                if (SLOT_4 < 70):
                    Unknown3072('d2000000ff0000000000000000000000')
                    Unknown3073('46000000640000000000000000000000')
                if (SLOT_4 < 60):
                    Unknown3072('b4000000ff0000000000000000000000')
                    Unknown3073('3c000000640000000000000000000000')
                if (SLOT_4 < 50):
                    Unknown3072('96000000ff0000000000000000000000')
                    Unknown3073('32000000640000000000000000000000')
                if (SLOT_4 < 40):
                    Unknown3072('78000000ff0000000000000000000000')
                    Unknown3073('28000000640000000000000000000000')
                if (SLOT_4 < 30):
                    Unknown3072('5a000000ff0000000000000000000000')
                    Unknown3073('1e000000640000000000000000000000')
                if (SLOT_4 < 20):
                    Unknown3072('3c000000ff0000000000000000000000')
                    Unknown3073('14000000640000000000000000000000')
                if (SLOT_4 < 10):
                    Unknown3072('1e000000ff0000000000000000000000')
                    Unknown3073('0a000000640000000000000000000000')
                if (SLOT_4 == 1):
                    Unknown3029(0)
                    Unknown3030(0)
            if SLOT_5:
                SLOT_5 = (SLOT_5 + (-1))
                if SLOT_30:
                    SLOT_5 = 0
                Unknown3029(1)
                Unknown3070(2)
                Unknown3071(6)
                Unknown3072('ff000000ff000000ff00000000000000')
                Unknown3073('64000000ff000000ff00000000000000')
                Unknown3076(1000)
                Unknown3077(1000)
                if (SLOT_5 < 40):
                    Unknown3072('f0000000ff000000ff00000000000000')
                    Unknown3073('50000000640000006400000000000000')
                if (SLOT_5 < 35):
                    Unknown3072('d2000000ff000000ff00000000000000')
                    Unknown3073('46000000640000006400000000000000')
                if (SLOT_5 < 30):
                    Unknown3072('b4000000ff000000ff00000000000000')
                    Unknown3073('3c000000640000006400000000000000')
                if (SLOT_5 < 25):
                    Unknown3072('96000000ff000000ff00000000000000')
                    Unknown3073('32000000640000006400000000000000')
                if (SLOT_5 < 20):
                    Unknown3072('78000000ff000000ff00000000000000')
                    Unknown3073('28000000640000006400000000000000')
                if (SLOT_5 < 15):
                    Unknown3072('5a000000ff000000ff00000000000000')
                    Unknown3073('1e000000640000006400000000000000')
                if (SLOT_5 < 10):
                    Unknown3072('3c000000ff000000ff00000000000000')
                    Unknown3073('14000000640000006400000000000000')
                if (SLOT_5 < 5):
                    Unknown3072('1e000000ff000000ff00000000000000')
                    Unknown3073('0a000000640000006400000000000000')
                if (SLOT_5 == 0):
                    Unknown3029(0)
                    Unknown3030(0)
        else:
            SLOT_4 = 0
            SLOT_5 = 0
            SLOT_31 = 0
            SLOT_32 = 0
            SLOT_33 = 0
        if SLOT_31:
            SLOT_31 = (SLOT_31 + (-100))
            if (not SLOT_31):
                if SLOT_109:
                    SLOT_31 = 1
        if SLOT_32:
            SLOT_32 = (SLOT_32 + (-100))
            if (not SLOT_32):
                if SLOT_109:
                    SLOT_32 = 1
        if SLOT_31:
            if (not Unknown46(4)):
                GFX_0('weakpoint01', -1)
                Unknown38(4, 1)
        elif Unknown46(4):
            Unknown23029(4, 100, 0)
        if SLOT_32:
            if (not Unknown46(5)):
                GFX_0('weakpoint00', -1)
                Unknown38(5, 1)
        elif Unknown46(5):
            Unknown23029(5, 101, 0)
        if SLOT_33:
            SLOT_33 = (SLOT_33 + (-100))
            if (not SLOT_4):
                if (not SLOT_5):
                    Unknown3029(1)
                    Unknown3069(1)
                    Unknown3071(4)
                    Unknown3070(4)
                    Unknown3072('c8000000ff0000000000000000000000')
                    Unknown3073('00000000ff0000000000000000000000')
                    if (SLOT_33 == 0):
                        Unknown3029(0)
                        Unknown3030(0)
        if (not SLOT_158):
            if SLOT_31:
                SLOT_31 = 0
                Unknown23029(4, 100, 0)
            if SLOT_32:
                SLOT_32 = 0
                Unknown23029(5, 101, 0)
        Unknown58('TRI_AzraelWeakPoint', 2, 67)
        if (SLOT_67 == 1):
            if SLOT_90:
                if (not SLOT_33):
                    SLOT_31 = 100000
                    SLOT_32 = 0
        if (SLOT_67 == 2):
            if SLOT_90:
                if (not SLOT_33):
                    SLOT_31 = 0
                    SLOT_32 = 100000
        if (SLOT_67 == 3):
            if SLOT_90:
                if (not SLOT_33):
                    SLOT_31 = 100000
                    SLOT_32 = 100000
        if (SLOT_67 == 4):
            if SLOT_90:
                SLOT_31 = 100000
                SLOT_32 = 100000
                SLOT_33 = 100000
        Unknown58('TRI_AzraelShotStock', 2, 67)
        if (SLOT_67 == 1):
            if SLOT_90:
                SLOT_59 = 3
        Unknown48('1900000002000000070000001600000002000000aa000000')
        if SLOT_7:
            SLOT_4 = 0
            SLOT_5 = 0
            SLOT_7 = 0

@Subroutine
def OnEnemyComboBreak():
    if SLOT_33:
        callSubroutine('SpecialWeakPointSet')
    SLOT_4 = 0
    SLOT_60 = 0
    SLOT_6 = 8

@Subroutine
def SpecialWeakPointSet():
    SLOT_31 = 0
    SLOT_32 = 0
    SLOT_31 = (SLOT_31 + SLOT_33)
    SLOT_32 = (SLOT_32 + SLOT_33)

@Subroutine
def MidWeakPoint():
    GFX_0('weakhit00', -1)
    if (not SLOT_31):
        if (not SLOT_33):
            SLOT_31 = 100000
            ScreenShake(4000, 4000)
            SFX_1('az210')
            SFX_3('azse_01')
            SFX_3('azse_01')
    else:
        if (not SLOT_109):
            SLOT_31 = 0
        ScreenShake(32000, 32000)
        Unknown23029(4, 100, 0)
        SFX_1('az212')
        SFX_3('azse_02')

@Subroutine
def MidWeakPointOverDrive():

    def upon_11():
        if SLOT_109:
            if (not SLOT_31):
                if (not SLOT_33):
                    GFX_0('weakhit00', -1)
                    SFX_3('azse_01')
                    SFX_3('azse_01')
                    SLOT_31 = 100000

@Subroutine
def LowWeakPoint():
    GFX_0('weakhit01', -1)
    if (not SLOT_32):
        if (not SLOT_33):
            SLOT_32 = 100000
            ScreenShake(8000, 8000)
            SFX_1('az211')
            SFX_3('azse_01')
            SFX_3('azse_01')
    else:
        if (not SLOT_109):
            SLOT_32 = 0
        ScreenShake(32000, 32000)
        Unknown23029(5, 101, 0)
        SFX_1('az212')
        SFX_3('azse_02')

@Subroutine
def LowWeakPointOverDrive():

    def upon_11():
        if SLOT_109:
            if (not SLOT_32):
                if (not SLOT_33):
                    GFX_0('weakhit01', -1)
                    SFX_3('azse_01')
                    SFX_3('azse_01')
                    SLOT_32 = 100000

@Subroutine
def HomingCancel():
    if SLOT_5:
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Unknown13011(1)
        Unknown13012(1)
        Unknown3029(1)
        Unknown3070(1)
        Unknown3071(4)
        Unknown3072('96000000ff000000ff000000ff000000')
        Unknown3073('64000000c8000000c8000000c8000000')
        Unknown3076(1000)
        Unknown3077(1000)
        AirUntechableTime(50)
        AirHitstunAnimation(13)
        AirPushbackX(5000)
        AirPushbackY(26000)

@Subroutine
def BoostCancel():
    if SLOT_4:
        Unknown1018()

        def upon_3():
            Unknown1019(98)

        def upon_12():
            if SLOT_4:
                Unknown1045(0)
                Unknown1019(10)
                AirPushbackX(35000)
                AirPushbackY(1000)
                YImpluseBeforeWallbounce(20)
                Unknown9346(1)
                Unknown9178(1)
                Unknown9362(1)
                Unknown9364(30)
                AirHitstunAfterWallbounce(-1)
                if (SLOT_25 < 200000):
                    if (SLOT_4 == 1):
                        Unknown9218(1)
                        Unknown11056(2)
                    else:
                        pass
                if (SLOT_4 > 1):
                    HitOrBlockCancel('BoostDash')
                    AirUntechableTime(30)
                    AirHitstunAfterWallbounce(30)
                    GroundedHitstunAnimation(1)
                    AirHitstunAnimation(1)
                    Unknown1017()

@Subroutine
def CheckShotCatch():
    Unknown23030('417a53686f7443617463680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def CheckBaigaeshiAvailable():
    SLOT_47 = SLOT_59

@Subroutine
def CheckCrouchGuardCrash():
    if Unknown23166('CmnActCrouchGuardPre'):
        SLOT_57 = 1
    if Unknown23166('CmnActCrouchGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActCrouchHeavyGuardLoop'):
        SLOT_57 = 1

@Subroutine
def CheckStandGuardCrash():
    if Unknown23166('CmnActMidGuardPre'):
        SLOT_57 = 1
    if Unknown23166('CmnActMidGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActMidHeavyGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActHighGuardPre'):
        SLOT_57 = 1
    if Unknown23166('CmnActHighGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActHighHeavyGuardLoop'):
        SLOT_57 = 1

@Subroutine
def WeakPointAttack_Pre():
    if (not SLOT_6):
        SLOT_6 = 8

    def upon_3():
        if 
        if (not Unknown23148('NmlAtk5A4th')):
            Unknown23148('NmlAtk2A'):
            if CheckInput(0x2):
                SLOT_51 = SLOT_18
        if 
        if (not Unknown23148('NmlAtkAIR5B')):
            Unknown23148('NmlAtk5B2nd'):
            if CheckInput(0xb):
                SLOT_51 = SLOT_18
        if 
        if (not 
        if (not Unknown23148('NmlAtk2C')):
            Unknown23148('VanishingAttack')):
            Unknown23148('DustAttack'):
            if CheckInput(0x14):
                SLOT_51 = SLOT_18

@Subroutine
def WeakPointAttack_Judge():
    clearUponHandler(3)
    Unknown47('01000000020000001200000002000000330000000200000034000000')
    op(1, 2, 6, 2, 52)
    (SLOT_0 > 0)

@Subroutine
def WeakPointAttack_Success():
    if (SLOT_6 == 8):
        SLOT_6 = 4
    elif (SLOT_6 == 4):
        SLOT_6 = (SLOT_6 - 2)

@State
def CmnActStand():
    label(0)
    sprite('az000_00', 7)	# 1-7
    sprite('az000_01', 7)	# 8-14
    sprite('az000_02', 7)	# 15-21
    sprite('az000_03', 7)	# 22-28
    sprite('az000_04', 7)	# 29-35
    sprite('az000_05', 7)	# 36-42
    sprite('az000_06', 7)	# 43-49
    sprite('az000_07', 7)	# 50-56
    sprite('az000_08', 7)	# 57-63
    sprite('az000_09', 7)	# 64-70
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
    sprite('az001_00', 6)	# 71-76
    SLOT_88 = 960
    SFX_1('baz000')
    sprite('az001_01', 6)	# 77-82
    sprite('az001_02', 6)	# 83-88
    sprite('az001_03', 6)	# 89-94
    sprite('az001_04', 6)	# 95-100
    sprite('az001_05', 6)	# 101-106
    sprite('az001_06', 6)	# 107-112
    sprite('az001_03', 6)	# 113-118
    sprite('az001_04', 6)	# 119-124
    sprite('az001_05', 6)	# 125-130
    sprite('az001_06', 6)	# 131-136
    sprite('az001_01', 6)	# 137-142
    sprite('az001_00', 6)	# 143-148
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('az003_00ex', 3)	# 1-3
    SFX_4('baz001')
    sprite('az003_01', 3)	# 4-6
    sprite('az003_00', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('az010_00', 4)	# 1-4
    sprite('az010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('az010_02', 6)	# 1-6
    sprite('az010_03', 6)	# 7-12
    sprite('az010_04', 6)	# 13-18
    sprite('az010_05', 6)	# 19-24
    sprite('az010_06', 6)	# 25-30
    sprite('az010_07', 6)	# 31-36
    sprite('az010_08', 6)	# 37-42
    sprite('az010_09', 6)	# 43-48
    sprite('az010_10', 6)	# 49-54
    sprite('az010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('az013_00ex', 3)	# 1-3
    sprite('az013_01', 3)	# 4-6
    sprite('az013_00', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('az010_01', 4)	# 1-4
    sprite('az010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('az023_00', 2)	# 1-2
    sprite('az023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    sprite('az020_00', 3)	# 1-3
    sprite('az020_01', 3)	# 4-6
    label(0)
    sprite('az020_00', 3)	# 7-9
    sprite('az020_01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('az020_02', 3)	# 1-3
    sprite('az020_03', 3)	# 4-6
    sprite('az020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('az020_05', 3)	# 1-3
    sprite('az020_06', 3)	# 4-6
    label(0)
    sprite('az020_07', 3)	# 7-9
    sprite('az020_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('az024_00', 3)	# 1-3
    sprite('az024_01', 3)	# 4-6
    sprite('az024_02', 3)	# 7-9
    sprite('az024_03', 3)	# 10-12
    sprite('az024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('az024_00', 2)	# 1-2
    sprite('az024_01', 2)	# 3-4
    sprite('az024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('az024_03', 3)	# 1-3
    sprite('az024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('az030_00', 8)	# 1-8
    label(0)
    sprite('az030_01', 8)	# 9-16
    sprite('az030_02', 8)	# 17-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 8)	# 25-32
    sprite('az030_04', 8)	# 33-40
    sprite('az030_05', 8)	# 41-48
    sprite('az030_06', 8)	# 49-56
    sprite('az030_07', 8)	# 57-64
    sprite('az030_08', 8)	# 65-72
    sprite('az030_09', 8)	# 73-80
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 8)	# 81-88
    sprite('az030_11', 8)	# 89-96
    sprite('az030_12', 8)	# 97-104
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('az031_00', 7)	# 1-7
    label(0)
    sprite('az031_01', 7)	# 8-14
    sprite('az031_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az031_03', 7)	# 22-28
    sprite('az031_04', 7)	# 29-35
    sprite('az031_05', 7)	# 36-42
    sprite('az031_06', 7)	# 43-49
    sprite('az031_07', 7)	# 50-56
    sprite('az031_08', 7)	# 57-63
    sprite('az031_09', 7)	# 64-70
    sprite('az031_10', 7)	# 71-77
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az031_11', 7)	# 78-84
    sprite('az031_12', 7)	# 85-91
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown1084(1)
        Unknown13008(1)
        Unknown13026(1)
        Unknown13031(1)

        def upon_STATE_END():
            Unknown1051(50)
    sprite('az032_00', 2)	# 1-2
    Unknown1047(4000)
    sprite('az032_01', 2)	# 3-4
    sprite('az032_02', 2)	# 5-6
    SFX_4('baz004')
    sprite('az032_03', 2)	# 7-8
    Unknown1047(25000)
    GFX_0('032rock', -1)
    GFX_0('dashEff', -1)
    SFX_0('000_airdash_0')
    setInvincible(1)
    Unknown2017(0)
    Unknown2015(40)
    Unknown13014(0)
    Unknown13015(0)
    Unknown13031(0)
    sprite('az032_03', 1)	# 9-9
    physicsXImpulse(60000)
    sprite('az032_03', 1)	# 10-10
    Unknown3038(1)
    physicsXImpulse(70000)
    sprite('az032_03', 5)	# 11-15
    physicsXImpulse(50000)
    sprite('az032_03', 1)	# 16-16
    Unknown3038(0)
    setInvincible(0)
    physicsXImpulse(70000)
    sprite('az032_03', 1)	# 17-17
    physicsXImpulse(60000)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('az032_04', 2)	# 18-19
    physicsXImpulse(0)
    sprite('az032_05', 2)	# 20-21
    Unknown1045(0)
    sprite('az032_06', 2)	# 22-23
    sprite('az032_07', 2)	# 24-25

@State
def CmnActFDashStop():
    pass

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincible(1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('az033_00', 2)	# 1-2
    sprite('az033_01', 2)	# 3-4
    sprite('az033_02', 2)	# 5-6
    physicsXImpulse(-28000)
    Unknown8002()
    sprite('az033_02', 2)	# 7-8
    GFX_0('dashEff2', -1)
    SFX_0('001_airbackdash_0')
    SFX_4('baz005')
    loopRest()
    sprite('az033_02', 2)	# 9-10
    Unknown3038(1)
    Unknown3029(1)
    Unknown2017(0)
    Unknown13014(0)
    Unknown13015(0)
    Unknown13026(0)
    Unknown13031(0)
    sprite('az033_03', 2)	# 11-12
    sprite('az033_02', 2)	# 13-14
    sprite('az033_02', 2)	# 15-16
    sprite('az033_03', 2)	# 17-18
    physicsXImpulse(0)
    Unknown3038(0)
    sprite('az033_04', 2)	# 19-20
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('az033_05', 2)	# 21-22
    setInvincible(0)
    Unknown3029(0)
    Unknown2017(1)
    sprite('az033_06', 3)	# 23-25
    sprite('az033_07', 3)	# 26-28

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('az035_00', 3)	# 1-3
    sprite('az035_01', 3)	# 4-6
    sprite('az035_02', 3)	# 7-9
    sprite('az035_03', 3)	# 10-12
    label(0)
    sprite('az035_01', 3)	# 13-15
    sprite('az035_02', 3)	# 16-18
    sprite('az035_03', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('az036_00', 3)	# 1-3
    sprite('az036_01', 3)	# 4-6
    sprite('az036_02', 3)	# 7-9
    sprite('az036_03', 3)	# 10-12
    label(0)
    sprite('az036_01', 3)	# 13-15
    sprite('az036_02', 3)	# 16-18
    sprite('az036_03', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('az050_00', 1)	# 1-1
    sprite('az050_01', 1)	# 2-2
    sprite('az050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('az050_01', 1)	# 1-1
    sprite('az050_02', 1)	# 2-2
    sprite('az050_01', 2)	# 3-4
    sprite('az050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('az050_02', 1)	# 1-1
    sprite('az050_03', 1)	# 2-2
    sprite('az050_02', 2)	# 3-4
    sprite('az050_01', 2)	# 5-6
    sprite('az050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('az050_03', 1)	# 1-1
    sprite('az050_04', 1)	# 2-2
    sprite('az050_03', 2)	# 3-4
    sprite('az050_02', 2)	# 5-6
    sprite('az050_01', 2)	# 7-8
    sprite('az050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('az050_04', 1)	# 1-1
    sprite('az050_04', 1)	# 2-2
    sprite('az050_04', 2)	# 3-4
    sprite('az050_03', 2)	# 5-6
    sprite('az050_02', 2)	# 7-8
    sprite('az050_01', 2)	# 9-10
    sprite('az050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('az052_00', 1)	# 1-1
    sprite('az052_01', 1)	# 2-2
    sprite('az052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('az052_01', 1)	# 1-1
    sprite('az052_02', 1)	# 2-2
    sprite('az052_01', 2)	# 3-4
    sprite('az052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('az052_02', 1)	# 1-1
    sprite('az052_03', 1)	# 2-2
    sprite('az052_02', 2)	# 3-4
    sprite('az052_01', 2)	# 5-6
    sprite('az052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('az052_03', 1)	# 1-1
    sprite('az052_04', 1)	# 2-2
    sprite('az052_03', 2)	# 3-4
    sprite('az052_02', 2)	# 5-6
    sprite('az052_01', 2)	# 7-8
    sprite('az052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('az052_04', 1)	# 1-1
    sprite('az052_04', 1)	# 2-2
    sprite('az052_04', 2)	# 3-4
    sprite('az052_03', 2)	# 5-6
    sprite('az052_02', 2)	# 7-8
    sprite('az052_01', 2)	# 9-10
    sprite('az052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('az054_00', 1)	# 1-1
    sprite('az054_01', 1)	# 2-2
    sprite('az054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('az054_01', 1)	# 1-1
    sprite('az054_02', 1)	# 2-2
    sprite('az054_01', 2)	# 3-4
    sprite('az054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('az054_02', 1)	# 1-1
    sprite('az054_03', 1)	# 2-2
    sprite('az054_02', 2)	# 3-4
    sprite('az054_01', 2)	# 5-6
    sprite('az054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('az054_03', 1)	# 1-1
    sprite('az054_04', 1)	# 2-2
    sprite('az054_03', 2)	# 3-4
    sprite('az054_02', 2)	# 5-6
    sprite('az054_01', 2)	# 7-8
    sprite('az054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('az054_04', 1)	# 1-1
    sprite('az054_04', 1)	# 2-2
    sprite('az054_04', 2)	# 3-4
    sprite('az054_03', 2)	# 5-6
    sprite('az054_02', 2)	# 7-8
    sprite('az054_01', 2)	# 9-10
    sprite('az054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('az060_00', 4)	# 1-4
    label(0)
    sprite('az060_01', 4)	# 5-8
    sprite('az060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('az060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('az062_05', 3)	# 1-3
    sprite('az062_06', 3)	# 4-6
    label(0)
    sprite('az062_07', 3)	# 7-9
    sprite('az062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('az060_07', 2)	# 1-2
    sprite('az060_08', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('az060_09', 3)	# 1-3
    sprite('az060_10', 3)	# 4-6
    sprite('az060_11', 3)	# 7-9
    sprite('az060_12', 3)	# 10-12
    sprite('az060_13', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('az060_14', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('az061_00', 3)	# 1-3
    sprite('az061_01', 3)	# 4-6
    sprite('az061_02', 3)	# 7-9
    sprite('az061_03', 3)	# 10-12
    sprite('az061_04', 3)	# 13-15
    sprite('az061_05', 3)	# 16-18
    sprite('az061_06', 2)	# 19-20
    sprite('az061_07', 2)	# 21-22
    sprite('az061_08', 2)	# 23-24
    sprite('az061_09', 2)	# 25-26

@State
def CmnActFDownUpper():
    sprite('az063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('az063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('az063_02', 3)	# 1-3
    sprite('az063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('az063_04', 3)	# 1-3
    sprite('az063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('az063_06', 2)	# 1-2
    sprite('az063_07', 2)	# 3-4
    sprite('az063_08', 3)	# 5-7
    sprite('az063_09', 3)	# 8-10
    sprite('az063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('az063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('az064_00', 2)	# 1-2
    sprite('az064_01', 2)	# 3-4
    sprite('az064_02', 2)	# 5-6
    sprite('az064_03', 2)	# 7-8
    sprite('az064_04', 2)	# 9-10
    sprite('az064_05', 2)	# 11-12
    sprite('az064_06', 2)	# 13-14
    sprite('az064_07', 2)	# 15-16
    sprite('az064_08', 2)	# 17-18
    sprite('az064_09', 2)	# 19-20
    sprite('az064_10', 2)	# 21-22

@State
def CmnActVDownUpper():
    sprite('az062_00', 3)	# 1-3
    label(0)
    sprite('az062_01', 3)	# 4-6
    sprite('az062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('az062_03', 3)	# 1-3
    sprite('az062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('az062_05', 3)	# 1-3
    sprite('az062_06', 3)	# 4-6
    label(0)
    sprite('az062_07', 3)	# 7-9
    sprite('az062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('az062_09', 2)	# 1-2
    sprite('az062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('az072_00', 3)	# 1-3
    sprite('az072_01', 3)	# 4-6
    sprite('az072_02', 3)	# 7-9
    label(0)
    sprite('az072_01', 3)	# 10-12
    sprite('az072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('az074_00', 3)	# 1-3
    sprite('az074_01', 3)	# 4-6
    sprite('az074_02', 3)	# 7-9
    sprite('az074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('az082_00', 2)	# 1-2
    sprite('az082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('az071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('az073_00', 3)	# 1-3
    sprite('az073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('az073_02', 3)	# 1-3
    label(0)
    sprite('az073_03', 3)	# 4-6
    sprite('az073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('az070_00', 3)	# 1-3
    sprite('az070_01', 3)	# 4-6
    sprite('az070_02', 4)	# 7-10
    sprite('az070_03', 4)	# 11-14

@State
def CmnActStaggerDown():
    sprite('az070_04', 4)	# 1-4
    sprite('az070_05', 4)	# 5-8
    sprite('az070_06', 4)	# 9-12
    sprite('az070_07', 4)	# 13-16
    sprite('az070_08', 4)	# 17-20
    sprite('az070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('az070_10', 2)	# 1-2
    sprite('az070_11', 2)	# 3-4
    sprite('az070_12', 2)	# 5-6
    sprite('az070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('az113_00', 3)	# 1-3
    sprite('az113_01', 3)	# 4-6
    sprite('az113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('az113_00', 3)	# 1-3
    sprite('az113_01', 3)	# 4-6
    sprite('az113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('az113_00', 3)	# 1-3
    sprite('az113_01', 3)	# 4-6
    sprite('az113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('az110_00', 2)	# 1-2
    sprite('az110_01', 2)	# 3-4
    sprite('az110_02', 2)	# 5-6
    sprite('az110_03', 2)	# 7-8
    sprite('az110_04', 2)	# 9-10
    sprite('az110_05', 2)	# 11-12
    sprite('az110_06', 2)	# 13-14
    sprite('az110_07', 2)	# 15-16
    sprite('az110_08', 200)	# 17-216
    sprite('az110_09', 2)	# 217-218
    sprite('az110_10', 2)	# 219-220
    sprite('az110_11', 2)	# 221-222

@State
def CmnActUkemiLandB():
    sprite('az111_00', 2)	# 1-2
    sprite('az111_01', 2)	# 3-4
    sprite('az111_02', 2)	# 5-6
    sprite('az111_03', 2)	# 7-8
    sprite('az111_04', 2)	# 9-10
    sprite('az111_05', 2)	# 11-12
    sprite('az111_06', 2)	# 13-14
    sprite('az111_07', 2)	# 15-16
    sprite('az111_08', 200)	# 17-216
    sprite('az111_09', 2)	# 217-218
    sprite('az111_10', 2)	# 219-220
    sprite('az111_11', 2)	# 221-222

@State
def CmnActUkemiLandN():
    sprite('az112_00', 2)	# 1-2
    sprite('az112_01', 2)	# 3-4
    sprite('az112_02', 2)	# 5-6
    sprite('az112_03', 2)	# 7-8
    sprite('az112_04', 2)	# 9-10
    sprite('az112_05', 2)	# 11-12
    sprite('az112_06', 2)	# 13-14
    sprite('az112_07', 2)	# 15-16
    sprite('az112_08', 2)	# 17-18
    sprite('az112_09', 2)	# 19-20

@State
def CmnActUkemiLandNLanding():
    sprite('az024_00', 3)	# 1-3
    sprite('az024_01', 3)	# 4-6
    sprite('az024_02', 3)	# 7-9
    sprite('az024_03', 3)	# 10-12
    sprite('az024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('az040_00', 3)	# 1-3
    sprite('az040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('az040_02', 3)	# 1-3
    sprite('az040_03', 3)	# 4-6
    sprite('az040_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('az040_01', 3)	# 1-3
    sprite('az040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('az040_03', 3)	# 1-3
    sprite('az040_02', 3)	# 4-6

@State
def CmnActMidHeavyGuardEnd():
    sprite('az040_01', 3)	# 1-3
    sprite('az040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('az041_00', 3)	# 1-3
    sprite('az041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('az041_02', 3)	# 1-3

@State
def CmnActHighGuardEnd():
    sprite('az041_01', 3)	# 1-3
    sprite('az041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('az041_03', 3)	# 1-3
    sprite('az041_02', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('az041_01', 3)	# 1-3
    sprite('az041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('az043_00', 3)	# 1-3
    sprite('az043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('az043_02', 3)	# 1-3
    sprite('az043_03', 3)	# 4-6
    sprite('az043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('az043_01', 3)	# 1-3
    sprite('az043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('az043_03', 3)	# 1-3
    sprite('az043_02', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('az043_01', 3)	# 1-3
    sprite('az043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('az045_00', 3)	# 1-3
    sprite('az045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('az045_02', 3)	# 1-3
    sprite('az045_03', 3)	# 4-6
    sprite('az045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('az045_01', 3)	# 1-3
    sprite('az045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('az045_03', 3)	# 1-3
    sprite('az045_02', 3)	# 4-6

@State
def CmnActAirHeavyGuardEnd():
    sprite('az045_01', 3)	# 1-3
    sprite('az045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('az090_00', 2)	# 1-2
    sprite('az090_01', 2)	# 3-4
    sprite('az090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('az090_03', 6)	# 6-11
    sprite('az090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('az091_00', 2)	# 1-2
    sprite('az091_01', 2)	# 3-4
    sprite('az091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('az091_03', 6)	# 6-11
    sprite('az091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('az092_00', 2)	# 1-2
    sprite('az092_01', 2)	# 3-4
    sprite('az092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('az092_03', 6)	# 6-11
    sprite('az092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('az025_00ex', 4)	# 1-4
    sprite('az025_01', 4)	# 5-8
    sprite('az025_00', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('az040_02', 1)	# 1-1
    sprite('az040_01', 3)	# 2-4
    sprite('az040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('az312_00', 3)	# 1-3
    sprite('az312_01', 3)	# 4-6
    sprite('az312_02', 3)	# 7-9
    sprite('az312_03', 8)	# 10-17	 **attackbox here**
    sprite('az312_04', 3)	# 18-20
    sprite('az312_05', 3)	# 21-23
    sprite('az312_06', 2)	# 24-25
    sprite('az312_07', 2)	# 26-27
    sprite('az312_08', 2)	# 28-29

@State
def CmnActAirLockWait():
    sprite('az045_02', 1)	# 1-1
    sprite('az045_01', 3)	# 2-4
    sprite('az045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('az322_00', 3)	# 1-3
    sprite('az322_01', 3)	# 4-6
    sprite('az322_02', 3)	# 7-9
    sprite('az322_03', 8)	# 10-17	 **attackbox here**
    sprite('az322_04', 3)	# 18-20
    sprite('az322_05', 3)	# 21-23
    sprite('az322_06', 2)	# 24-25
    sprite('az322_07', 2)	# 26-27
    sprite('az322_08', 2)	# 28-29

@State
def CmnActLandSpin():
    sprite('az071_00', 4)	# 1-4
    sprite('az071_01', 4)	# 5-8
    label(0)
    sprite('az071_02', 2)	# 9-10
    sprite('az071_03', 2)	# 11-12
    sprite('az071_04', 2)	# 13-14
    sprite('az071_05', 2)	# 15-16
    sprite('az071_06', 2)	# 17-18
    sprite('az071_07', 2)	# 19-20
    sprite('az071_08', 2)	# 21-22
    sprite('az071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('az071_10', 6)	# 1-6
    sprite('az071_11', 5)	# 7-11
    sprite('az071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('az071_02', 2)	# 1-2
    sprite('az071_03', 2)	# 3-4
    sprite('az071_04', 2)	# 5-6
    sprite('az071_05', 2)	# 7-8
    sprite('az071_06', 2)	# 9-10
    sprite('az071_07', 2)	# 11-12
    sprite('az071_08', 2)	# 13-14
    sprite('az071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('az077_00', 2)	# 1-2
    sprite('az077_01', 2)	# 3-4
    sprite('az077_00ex01', 2)	# 5-6
    sprite('az077_01ex01', 2)	# 7-8
    sprite('az077_00ex02', 2)	# 9-10
    sprite('az077_01ex02', 2)	# 11-12
    sprite('az077_00ex03', 2)	# 13-14
    sprite('az077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('az077_02', 4)	# 1-4
    label(0)
    sprite('az077_03', 3)	# 5-7
    sprite('az077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('az077_05', 5)	# 1-5
    sprite('az077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('az060_07', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('az060_11', 4)	# 1-4
    sprite('az060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('az331_00', 2)	# 1-2
    sprite('az331_01', 2)	# 3-4
    label(0)
    sprite('az331_02', 3)	# 5-7
    sprite('az331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('az331_04', 2)	# 1-2
    sprite('az331_05', 2)	# 3-4
    label(0)
    sprite('az331_06', 3)	# 5-7
    sprite('az331_07', 3)	# 8-10
    sprite('az331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('az331_09', 3)	# 1-3
    sprite('az331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('az331_11', 2)	# 1-2
    sprite('az331_12', 2)	# 3-4
    label(0)
    sprite('az331_02', 3)	# 5-7
    sprite('az331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('az331_04', 2)	# 1-2
    sprite('az331_05', 2)	# 3-4
    label(0)
    sprite('az331_06', 3)	# 5-7
    sprite('az331_07', 3)	# 8-10
    sprite('az331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('az331_13', 3)	# 1-3
    sprite('az331_14', 3)	# 4-6
    sprite('az020_05', 3)	# 7-9
    sprite('az020_06', 3)	# 10-12
    label(0)
    sprite('az020_07', 4)	# 13-16
    sprite('az020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('az333_00', 3)	# 1-3
    sprite('az333_01', 3)	# 4-6
    sprite('az333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('az333_03', 32767)	# 10-32776
    GFX_0('EMB_AZ_OD', -1)

@State
def CmnActOverDriveLoop():
    sprite('az333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('az333_05', 3)	# 4-6
    sprite('az333_06', 3)	# 7-9
    sprite('az333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('az333_08', 4)	# 1-4
    sprite('az333_09', 4)	# 5-8
    sprite('az333_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('az333_11', 3)	# 1-3
    sprite('az333_12', 3)	# 4-6
    sprite('az333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('az333_14', 32767)	# 10-32776
    GFX_0('EMB_AZ_OD', -1)

@State
def CmnActAirOverDriveLoop():
    sprite('az333_15', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('az333_05', 3)	# 4-6
    sprite('az333_06', 3)	# 7-9
    sprite('az333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('az333_16', 4)	# 1-4
    sprite('az333_17', 4)	# 5-8
    sprite('az333_18', 4)	# 9-12
    sprite('az020_05', 3)	# 13-15
    sprite('az020_06', 3)	# 16-18
    label(0)
    sprite('az020_07', 4)	# 19-22
    sprite('az020_08', 4)	# 23-26
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('az333_00', 3)	# 1-3
    sprite('az333_01', 3)	# 4-6
    sprite('az333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('az333_03', 32767)	# 10-32776
    GFX_0('EMB_AZ_OD', -1)

@State
def CmnActCrossRushLoop():
    sprite('az333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('az333_05', 3)	# 4-6
    sprite('az333_06', 3)	# 7-9
    sprite('az333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('az333_08', 4)	# 1-4
    sprite('az333_09', 4)	# 5-8
    sprite('az333_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('az333_11', 3)	# 1-3
    sprite('az333_12', 3)	# 4-6
    sprite('az333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('az333_14', 32767)	# 10-32776
    GFX_0('EMB_AZ_OD', -1)

@State
def CmnActAirCrossRushLoop():
    sprite('az333_15', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('az333_05', 3)	# 4-6
    sprite('az333_06', 3)	# 7-9
    sprite('az333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('az333_16', 4)	# 1-4
    sprite('az333_17', 4)	# 5-8
    sprite('az333_18', 4)	# 9-12
    sprite('az020_05', 3)	# 13-15
    sprite('az020_06', 3)	# 16-18
    label(0)
    sprite('az020_07', 4)	# 19-22
    sprite('az020_08', 4)	# 23-26
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('az331_00', 2)	# 1-2
    sprite('az331_01', 2)	# 3-4
    label(0)
    sprite('az331_02', 3)	# 5-7
    sprite('az331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('az331_04', 2)	# 1-2
    sprite('az331_05', 2)	# 3-4
    label(0)
    sprite('az331_06', 3)	# 5-7
    sprite('az331_07', 3)	# 8-10
    sprite('az331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('az331_09', 3)	# 1-3
    sprite('az331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('az331_11', 2)	# 1-2
    sprite('az331_12', 2)	# 3-4
    label(0)
    sprite('az331_02', 3)	# 5-7
    sprite('az331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('az331_04', 2)	# 1-2
    sprite('az331_05', 2)	# 3-4
    label(0)
    sprite('az331_06', 3)	# 5-7
    sprite('az331_07', 3)	# 8-10
    sprite('az331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('az331_13', 3)	# 1-3
    sprite('az331_14', 3)	# 4-6
    sprite('az020_05', 3)	# 7-9
    sprite('az020_06', 3)	# 10-12
    label(0)
    sprite('az020_07', 4)	# 13-16
    sprite('az020_08', 4)	# 17-20
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
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 25)	# 1-25
    sprite('az409_14', 3)	# 26-28	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('az409_15', 3)	# 29-31	 **attackbox here**
    GFX_0('azef_409_fall', 0)
    label(2)
    sprite('az409_14', 3)	# 32-34	 **attackbox here**
    sprite('az409_15', 3)	# 35-37	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('az409_16', 4)	# 38-41	 **attackbox here**
    SFX_3('azse_07')
    Unknown26('azef_409_fall')
    GFX_0('azef_409_rock', -1)
    Unknown1084(1)
    ScreenShake(10000, 20000)
    sprite('az409_17', 3)	# 42-44
    sprite('az409_18', 3)	# 45-47
    sprite('az409_19', 3)	# 48-50
    sprite('az409_17', 3)	# 51-53
    sprite('az409_18', 3)	# 54-56
    sprite('az409_19', 2)	# 57-58
    sprite('az409_20', 2)	# 59-60
    sprite('az409_21', 2)	# 61-62

@State
def CmnActChangePartnerQuickIn():
    sprite('az030_03', 3)	# 1-3
    sprite('az030_04', 5)	# 4-8
    sprite('az030_05', 7)	# 9-15
    sprite('az030_06', 7)	# 16-22
    sprite('az030_07', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('az031_00', 2)	# 1-2
    Unknown1019(15)
    physicsYImpulse(0)
    setGravity(0)
    sprite('az031_04', 5)	# 3-7
    sprite('az031_05', 5)	# 8-12
    sprite('az031_06', 5)	# 13-17
    sprite('az031_07', 5)	# 18-22
    sprite('az031_08', 5)	# 23-27
    sprite('az031_09', 30)	# 28-57

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('az033_00', 1)	# 1-1
    sprite('az033_01', 2)	# 2-3
    sprite('az033_02', 2)	# 4-5
    sprite('az033_02', 1)	# 6-6
    sprite('az033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('az033_02', 3)	# 10-12
    sprite('az033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az033_04', 3)	# 16-18
    sprite('az033_05', 3)	# 19-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('az000_00', 2)	# 1-2
    sprite('az300_00', 6)	# 3-8
    sprite('az300_01', 6)	# 9-14
    sprite('az300_02', 7)	# 15-21
    sprite('az300_03', 4)	# 22-25
    SFX_3('azse_12')
    sprite('az300_04', 4)	# 26-29	 **attackbox here**
    sprite('az300_05', 4)	# 30-33
    sprite('az300_06', 4)	# 34-37
    sprite('az300_07', 7)	# 38-44
    sprite('az300_08', 6)	# 45-50
    sprite('az300_14', 6)	# 51-56
    sprite('az300_15', 6)	# 57-62
    sprite('az300_16', 6)	# 63-68
    sprite('az300_00', 6)	# 69-74
    sprite('az000_00', 2)	# 75-76

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
    sprite('az020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('az020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('az010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(70)
        Unknown11050('04000000617a65665f343032696d706163746869745f706f730000000000000000000000')
        Hitstop(20)
        Unknown11028(35)
        AirPushbackX(2500)
        AirPushbackY(40000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown11056(0)
        Unknown30040(1)
        Unknown2006()
        Unknown11042(1)

        def upon_78():
            clearUponHandler(78)
            Unknown2017(0)

        def upon_80():
            clearUponHandler(80)
            physicsXImpulse(20000)

        def upon_12():
            SFX_0('025_cleanhit_grap')

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('az406_01', 3)	# 1-3
    sprite('az406_02', 3)	# 4-6
    sprite('az406_03', 3)	# 7-9
    sprite('az406_01', 3)	# 10-12
    sprite('az406_02', 3)	# 13-15
    sprite('az406_03', 3)	# 16-18
    sprite('az401_11', 3)	# 19-21
    sprite('az401_03', 3)	# 22-24	 **attackbox here**
    StartMultihit()
    sprite('az402_16', 3)	# 25-27
    sprite('az402_17', 3)	# 28-30
    sprite('az402_02', 6)	# 31-36
    sprite('az402_03', 2)	# 37-38
    physicsXImpulse(100000)
    Unknown2016(350)
    sprite('az402_04', 2)	# 39-40
    Unknown1019(120)
    SFX_3('azse_07')
    SFX_1('baz203_0')
    sprite('az402_05', 3)	# 41-43	 **attackbox here**
    physicsXImpulse(150000)
    RefreshMultihit()
    GFX_0('402swing', -1)
    GFX_0('402rock1', -1)
    sprite('az402_06', 3)	# 44-46
    Unknown8006(100, 1, 1)
    sprite('az402_07', 3)	# 47-49
    Unknown1019(30)
    Unknown8006(100, 1, 1)
    sprite('az402_08', 3)	# 50-52
    Unknown1019(80)
    Unknown8006(100, 1, 1)
    sprite('az402_09', 3)	# 53-55
    Unknown1019(80)
    sprite('az402_10', 3)	# 56-58
    Unknown1019(80)
    sprite('az402_11', 3)	# 59-61
    Unknown1019(0)
    sprite('az402_12', 3)	# 62-64
    sprite('az402_13', 4)	# 65-68
    sprite('az402_14', 4)	# 69-72
    sprite('az402_15', 4)	# 73-76
    Unknown2016(-1)

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(70)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(15000)
        AirPushbackY(36000)
        AirUntechableTime(45)
        Unknown30040(1)
        Unknown2006()
        Unknown11042(1)

        def upon_42():
            if Unknown23037():
                SLOT_59 = (SLOT_59 + 1)
                if (SLOT_59 >= 3):
                    SLOT_59 = 3
                sendToLabel(0)
                SFX_3('azse_04')
                Unknown7015()
                Unknown22019('0100000001000000010000000100000001000000')
                Unknown22036(1)
                if (not Unknown46(7)):
                    GFX_0('407Kyushu', -1)
                    Unknown38(7, 1)
            else:
                pass

        def upon_3():
            if SLOT_59:
                callSubroutine('CheckShotCatch')
            if (not SLOT_2):
                if (SLOT_19 <= 150000):
                    Unknown2037(1)
            if (SLOT_2 == 1):
                sendToLabel(3)

        def upon_STATE_END():
            Unknown7015()
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('az030_00', 8)	# 1-8
    physicsXImpulse(8000)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('az030_01', 8)	# 9-16
    sprite('az030_02', 8)	# 17-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 8)	# 25-32
    sprite('az030_04', 8)	# 33-40
    label(3)
    sprite('az407_00', 1)	# 41-41
    Unknown1084(1)
    GuardPoint_(1)
    Unknown1084(1)
    Unknown2037(2)
    sprite('az407_01', 2)	# 42-43
    tag_voice(1, 'baz207_0', 'baz207_1', 'baz207_2', '')
    sprite('az407_02', 2)	# 44-45
    sprite('az407_03', 1)	# 46-46	 **attackbox here**
    StartMultihit()
    GFX_0('407aura', -1)
    SFX_3('azse_03')
    sprite('az407_03', 2)	# 47-48	 **attackbox here**
    StartMultihit()
    sprite('az407_03', 1)	# 49-49	 **attackbox here**
    RefreshMultihit()
    sprite('az407_04', 4)	# 50-53	 **attackbox here**
    sprite('az407_05', 4)	# 54-57	 **attackbox here**
    Unknown23027()
    sprite('az407_02', 4)	# 58-61
    Unknown7014('azse_03_loop')
    sprite('az407_03', 4)	# 62-65	 **attackbox here**
    sprite('az407_04', 4)	# 66-69	 **attackbox here**
    sprite('az407_05', 4)	# 70-73	 **attackbox here**
    sprite('az407_02', 4)	# 74-77
    sprite('az407_03', 4)	# 78-81	 **attackbox here**
    sprite('az407_04', 4)	# 82-85	 **attackbox here**
    sprite('az407_05', 3)	# 86-88	 **attackbox here**
    sprite('az407_05', 1)	# 89-89	 **attackbox here**
    sprite('az407_02', 4)	# 90-93
    sprite('az407_03', 4)	# 94-97	 **attackbox here**
    sprite('az407_04', 4)	# 98-101	 **attackbox here**
    sprite('az407_05', 4)	# 102-105	 **attackbox here**
    sprite('az407_02', 4)	# 106-109
    sprite('az407_03', 4)	# 110-113	 **attackbox here**
    sprite('az407_04', 4)	# 114-117	 **attackbox here**
    sprite('az407_05', 4)	# 118-121	 **attackbox here**
    gotoLabel(1)
    label(0)
    sprite('az407_06', 5)	# 122-126
    sprite('az407_07', 5)	# 127-131
    sprite('az407_08', 5)	# 132-136
    sprite('az407_09', 5)	# 137-141
    tag_voice(0, 'baz208_0', 'baz208_1', 'baz208_2', '')
    GuardPoint_(0)
    sprite('az408_00', 2)	# 142-143
    sprite('az408_01', 2)	# 144-145
    sprite('az408_02', 3)	# 146-148
    SFX_3('azse_04')
    tag_voice(0, 'baz209_0', 'baz209_1', 'baz209_2', '')
    GFX_0('408sphereStart', -1)
    GFX_0('408sphere', -1)
    if (SLOT_59 >= 1):
        Unknown38(6, 1)
        Unknown23029(6, 4081, 0)
        Unknown23029(6, 4082, 0)
        SLOT_59 = (SLOT_59 + (-1))
    sprite('az408_03', 3)	# 149-151
    sprite('az408_04', 3)	# 152-154
    sprite('az408_05', 3)	# 155-157
    sprite('az408_06', 3)	# 158-160
    sprite('az408_07', 3)	# 161-163
    sprite('az408_08', 2)	# 164-165
    sprite('az408_09', 2)	# 166-167
    ExitState()
    label(1)
    sprite('az407_02', 4)	# 168-171
    setInvincible(0)
    Unknown7015()
    sprite('az407_01', 3)	# 172-174
    sprite('az407_01', 1)	# 175-175
    gotoLabel(2)
    label(2)
    sprite('az407_00', 3)	# 176-178

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2400)
        AttackP1(70)
        AirPushbackX(10000)
        AirPushbackY(-300000)
        AirUntechableTime(60)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9118(10)
        Unknown9190(1)
        Unknown11058('0100000000000000000000000000000000000000')
        sendToLabelUpon(2, 9)
        Unknown30040(1)
        Unknown2006()
        Unknown11042(1)
        Unknown11056(0)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('az212_00', 2)	# 1-2
    sprite('az212_01', 2)	# 3-4
    sprite('az212_02', 3)	# 5-7
    physicsXImpulse(40000)
    physicsYImpulse(20000)
    setGravity(2000)
    Unknown23087(50000)
    sprite('az212_03', 3)	# 8-10
    Unknown7007('62617a3130385f3100000000000000006400000062617a3130385f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('az212_04', 4)	# 11-14
    SFX_0('005_swing_grap_2_2')
    Unknown2016(300)
    sprite('az212_05', 2)	# 15-16	 **attackbox here**
    Unknown1019(80)
    sprite('az212_06', 2)	# 17-18	 **attackbox here**
    sprite('az212_07', 2)	# 19-20	 **attackbox here**
    sprite('az212_08', 2)	# 21-22	 **attackbox here**
    Unknown1019(30)
    sprite('az212_09', 32767)	# 23-32789
    label(9)
    sprite('az212_10', 5)	# 32790-32794
    Unknown2016(-1)
    physicsXImpulse(0)
    sprite('az212_11', 8)	# 32795-32802
    sprite('az212_12', 8)	# 32803-32810

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
    Unknown2036(157, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-320000)
    Unknown1019(4)
    label(0)
    sprite('az020_07', 4)	# 3-6
    sprite('az020_08', 4)	# 7-10
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
        Unknown30063(1)
        AttackLevel_(4)
        Damage(2000)
        Hitstop(20)
        AirPushbackX(54000)
        AirPushbackY(22000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        PushbackX(60800)
        Unknown11050('04000000617a65665f3433316869745f6c696e6500000000000000000000000000000000')
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown11056(0)
        setInvincible(1)

        def upon_12():
            HitAirUnblockable(4)
            HitOverhead(4)
            HitLow(4)
            if SLOT_31:
                GFX_0('weakhit00', -1)
            if SLOT_32:
                GFX_0('weakhit01', -1)
        if SLOT_31:
            HitAirUnblockable(3)
            HitLow(2)
        if SLOT_32:
            HitAirUnblockable(3)
            HitOverhead(2)
    sprite('az431_00', 3)	# 1-3
    sprite('az431_00', 3)	# 4-6
    sprite('az431_01', 6)	# 7-12
    teleportRelativeX(-70000)
    Unknown3029(1)
    sprite('az431_02', 6)	# 13-18
    teleportRelativeX(-40000)
    sprite('az431_03', 6)	# 19-24
    teleportRelativeX(-40000)
    sprite('az431_04', 6)	# 25-30
    teleportRelativeX(-70000)
    sprite('az431_05', 6)	# 31-36
    teleportRelativeX(-70000)
    sprite('az431_06', 5)	# 37-41
    sprite('az431_07', 5)	# 42-46
    sprite('az431_08', 5)	# 47-51
    sprite('az431_09', 5)	# 52-56
    sprite('az431_10', 3)	# 57-59
    sprite('az431_11', 3)	# 60-62
    sprite('az431_12', 3)	# 63-65
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 66-68
    sprite('az431_11', 3)	# 69-71
    sprite('az431_12', 3)	# 72-74
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 75-77
    sprite('az431_11', 3)	# 78-80
    sprite('az431_12', 3)	# 81-83
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 84-86
    sprite('az431_11', 3)	# 87-89
    sprite('az431_12', 3)	# 90-92
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 93-95
    sprite('az431_11', 3)	# 96-98
    sprite('az431_12', 3)	# 99-101
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 102-104
    sprite('az431_11', 3)	# 105-107
    sprite('az431_12', 3)	# 108-110
    sprite('az431_13', 4)	# 111-114
    sprite('az431_14', 4)	# 115-118
    sprite('az431_15', 4)	# 119-122
    GFX_0('402rock1', -1)
    GFX_0('405smoke', -1)
    teleportRelativeX(10000)
    sprite('az431_16', 4)	# 123-126
    teleportRelativeX(10000)
    SFX_3('azse_06')
    sprite('az431_17', 3)	# 127-129
    SFX_4('baz251_0')
    teleportRelativeX(80000)
    SLOT_12 = SLOT_19
    Unknown1019(9)
    if (SLOT_12 <= 10000):
        SLOT_12 = 10000
    sprite('az431_18', 3)	# 130-132
    teleportRelativeX(20000)
    sprite('az431_19', 3)	# 133-135	 **attackbox here**
    Unknown26('405smoke')
    GFX_0('431swing', -1)
    Unknown1019(70)

    def upon_12():
        SFX_0('025_cleanhit_grap')
        SFX_0('025_cleanhit_grap')
    sprite('az431_20', 6)	# 136-141
    setInvincible(0)
    Unknown1019(20)
    sprite('az431_21', 6)	# 142-147
    physicsXImpulse(0)
    sprite('az431_22', 6)	# 148-153
    sprite('az431_23', 6)	# 154-159
    sprite('az431_24', 6)	# 160-165
    sprite('az431_25', 6)	# 166-171
    sprite('az431_26', 6)	# 172-177
    sprite('az431_27', 6)	# 178-183
    sprite('az431_28', 6)	# 184-189

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2500)
        Hitstop(20)
        AirPushbackX(80000)
        AirPushbackY(22000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        Unknown9168(60)
        PushbackX(60800)
        Unknown9202(40)
        Unknown11050('04000000617a65665f3433316869745f6c696e6500000000000000000000000000000000')
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown11056(0)
        setInvincible(1)

        def upon_12():
            HitAirUnblockable(4)
            HitOverhead(4)
            HitLow(4)
            if SLOT_31:
                GFX_0('weakhit00', -1)
            if SLOT_32:
                GFX_0('weakhit01', -1)
        if SLOT_31:
            HitAirUnblockable(3)
            HitLow(2)
        if SLOT_32:
            HitAirUnblockable(3)
            HitOverhead(2)
    sprite('az431_00', 3)	# 1-3
    sprite('az431_00', 3)	# 4-6
    sprite('az431_01', 6)	# 7-12
    teleportRelativeX(-70000)
    Unknown3029(1)
    sprite('az431_02', 6)	# 13-18
    teleportRelativeX(-40000)
    sprite('az431_03', 6)	# 19-24
    teleportRelativeX(-40000)
    sprite('az431_04', 6)	# 25-30
    teleportRelativeX(-70000)
    sprite('az431_05', 6)	# 31-36
    teleportRelativeX(-70000)
    sprite('az431_06', 5)	# 37-41
    sprite('az431_07', 5)	# 42-46
    sprite('az431_08', 5)	# 47-51
    sprite('az431_09', 5)	# 52-56
    GFX_0('431ODAura', -1)
    Unknown23119(-922799616, 54, 2)
    sprite('az431_10', 3)	# 57-59
    sprite('az431_11', 3)	# 60-62
    sprite('az431_12', 3)	# 63-65
    ScreenShake(12000, 0)
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 66-68
    sprite('az431_11', 3)	# 69-71
    sprite('az431_12', 3)	# 72-74
    ScreenShake(12000, 0)
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 75-77
    sprite('az431_11', 3)	# 78-80
    sprite('az431_12', 3)	# 81-83
    ScreenShake(15000, 0)
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 84-86
    sprite('az431_11', 3)	# 87-89
    sprite('az431_12', 3)	# 90-92
    ScreenShake(18000, 0)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 93-95
    sprite('az431_11', 3)	# 96-98
    sprite('az431_12', 3)	# 99-101
    ScreenShake(21000, 0)
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 102-104
    sprite('az431_11', 3)	# 105-107
    sprite('az431_12', 3)	# 108-110
    ScreenShake(25000, 0)
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    Unknown21015('3433314f44417572610000000000000000000000000000000000000000000000d710000000000000')
    sprite('az431_13', 4)	# 111-114
    sprite('az431_14', 4)	# 115-118
    sprite('az431_15', 4)	# 119-122
    GFX_0('402rock1', -1)
    GFX_0('405smoke', -1)
    teleportRelativeX(10000)
    sprite('az431_16', 4)	# 123-126
    teleportRelativeX(10000)
    SFX_3('azse_06')
    sprite('az431_17', 3)	# 127-129
    SFX_4('baz251_0')
    teleportRelativeX(80000)
    SLOT_12 = SLOT_19
    Unknown1019(9)
    if (SLOT_12 <= 10000):
        SLOT_12 = 10000
    sprite('az431_18', 3)	# 130-132
    teleportRelativeX(20000)
    sprite('az431_19', 3)	# 133-135	 **attackbox here**
    Unknown26('405smoke')
    GFX_0('431swing', -1)
    Unknown1019(70)

    def upon_12():
        SFX_0('025_cleanhit_grap')
        SFX_0('025_cleanhit_grap')
    sprite('az431_20', 6)	# 136-141
    setInvincible(0)
    Unknown1019(20)
    sprite('az431_21', 6)	# 142-147
    physicsXImpulse(0)
    sprite('az431_22', 6)	# 148-153
    sprite('az431_23', 6)	# 154-159
    sprite('az431_24', 6)	# 160-165
    sprite('az431_25', 6)	# 166-171
    sprite('az431_26', 6)	# 172-177
    sprite('az431_27', 6)	# 178-183
    sprite('az431_28', 6)	# 184-189

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
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('az409_14', 3)	# 121-123	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    GFX_0('azef_409_fall', 0)
    sprite('az409_15', 3)	# 124-126	 **attackbox here**
    label(2)
    sprite('az409_14', 3)	# 127-129	 **attackbox here**
    sprite('az409_15', 3)	# 130-132	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('az409_16', 4)	# 133-136	 **attackbox here**
    SFX_3('azse_07')
    Unknown26('azef_409_fall')
    GFX_0('azef_409_rock', -1)
    Unknown1084(1)
    ScreenShake(10000, 20000)
    StartMultihit()
    sprite('az409_17', 4)	# 137-140
    sprite('az409_18', 4)	# 141-144
    sprite('az409_19', 4)	# 145-148
    sprite('az409_17', 3)	# 149-151
    sprite('az409_18', 3)	# 152-154
    sprite('az409_19', 3)	# 155-157
    sprite('az409_20', 3)	# 158-160
    sprite('az409_21', 3)	# 161-163

@State
def CmnActChangeReturnAppealBurst():
    sprite('az061_03', 27)	# 1-27
    sprite('az061_04', 5)	# 28-32
    sprite('az061_05', 5)	# 33-37
    sprite('az061_06', 5)	# 38-42
    sprite('az061_07', 5)	# 43-47
    sprite('az061_08', 5)	# 48-52
    sprite('az061_09', 5)	# 53-57
    sprite('az000_00', 23)	# 58-80

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9154(22)
        AirUntechableTime(19)
        AirPushbackY(20000)
        Unknown11028(17)
        PushbackX(15000)
        HitOrBlockJumpCancel(1)
        callSubroutine('BoostCancel')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_58 = 10

            def upon_45():
                if SLOT_58:
                    SLOT_58 = (SLOT_58 + (-1))
                else:
                    Unknown14070('NmlAtk2A')
                    Unknown14070('NmlAtk5B')
                    Unknown14070('NmlAtk2B')
                    Unknown14070('CmnActCrushAttack')
                    Unknown14070('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('az201_00', 2)	# 1-2
    sprite('az201_01', 2)	# 3-4
    sprite('az201_02', 2)	# 5-6
    Unknown7009(1)
    sprite('az201_03', 4)	# 7-10	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    Unknown14070('NmlAtk5A2nd')
    sprite('az201_04', 3)	# 11-13	 **attackbox here**
    sprite('az201_05', 2)	# 14-15
    Unknown14072('NmlAtk5A2nd')
    Unknown14072('NmlAtk2A')
    Unknown14072('NmlAtk5B')
    Unknown14072('NmlAtk2B')
    Unknown14072('CmnActCrushAttack')
    Unknown14072('NmlAtk2C')
    Recovery()
    Unknown2063()
    sprite('az201_06', 4)	# 16-19
    sprite('az201_07', 4)	# 20-23
    Unknown14074('NmlAtk5A2nd')

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(-10000)
        Unknown11028(17)
        PushbackX(15000)
        Unknown9154(23)
        AirUntechableTime(22)
        Unknown9190(1)
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('BoostCancel')
    sprite('az201_08', 3)	# 1-3
    sprite('az201_09', 3)	# 4-6
    sprite('az201_10', 4)	# 7-10
    Unknown7009(4)
    physicsXImpulse(25000)
    sprite('az201_11', 3)	# 11-13	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    physicsXImpulse(0)
    sprite('az201_12', 5)	# 14-18
    Recovery()
    Unknown2063()
    sprite('az201_13', 5)	# 19-23
    sprite('az201_14', 5)	# 24-28

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown9154(23)
        AirUntechableTime(23)
        PushbackX(19800)
        AirPushbackX(12000)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2C')
        callSubroutine('BoostCancel')
    sprite('az210_00', 2)	# 1-2
    sprite('az210_01', 2)	# 3-4
    sprite('az210_02', 2)	# 5-6
    sprite('az210_02', 1)	# 7-7
    sprite('az210_03', 3)	# 8-10
    sprite('az210_04', 4)	# 11-14
    SFX_0('005_swing_grap_2_2')
    Unknown7009(4)
    sprite('az210_05', 3)	# 15-17	 **attackbox here**
    physicsXImpulse(45000)
    Unknown1047(15000)
    sprite('az210_05', 3)	# 18-20	 **attackbox here**
    Unknown1019(80)
    sprite('az210_05', 3)	# 21-23	 **attackbox here**
    Unknown1019(50)
    sprite('az210_06', 3)	# 24-26
    Recovery()
    Unknown2063()
    Unknown1019(30)
    sprite('az210_07', 3)	# 27-29
    Unknown1019(50)
    sprite('az210_08', 2)	# 30-31
    Unknown1019(50)
    sprite('az210_09', 2)	# 32-33
    physicsXImpulse(0)
    sprite('az210_10', 2)	# 34-35
    sprite('az210_11', 2)	# 36-37

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(80)
        AirPushbackY(-20000)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9154(23)
        PushbackX(19800)
        Unknown9310(1)
        HitOverhead(2)
        JumpCancel_(0)
        callSubroutine('WeakPointAttack_Pre')

        def upon_78():
            clearUponHandler(78)
            if 
            if (not op(6, 2, 4, 2, 5)):
                callSubroutine('WeakPointAttack_Judge'):
                AttackLevel_(5)
                Unknown11001(0, 0, 5)
                Hitstop(15)
                GroundedHitstunAnimation(11)
                AirUntechableTime(60)
                Unknown9310(0)
                AirPushbackY(-20000)
                if SLOT_125:
                    AirPushbackY(-30000)
                Unknown9190(1)
                ScreenShake(32000, 32000)
                GFX_0('weakhit00', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                callSubroutine('WeakPointAttack_Success')
                Unknown23159('NmlAtk5A4th_True')
            else:
                ScreenShake(4000, 4000)
                Unknown7009(2)
                SFX_3('azse_01')
    sprite('az203_00', 2)	# 1-2
    sprite('az203_01', 4)	# 3-6
    sprite('az203_02', 3)	# 7-9
    physicsXImpulse(8000)
    physicsYImpulse(16000)
    setGravity(3250)
    sprite('az203_03', 3)	# 10-12
    sprite('az203_04', 3)	# 13-15
    GFX_1('ef_smokej', 0)
    Unknown1019(80)
    sprite('az203_05', 3)	# 16-18
    sprite('az203_06', 2)	# 19-20
    SFX_0('005_swing_grap_2_2')
    teleportRelativeX(30000)
    physicsXImpulse(0)
    sprite('az203_07', 3)	# 21-23	 **attackbox here**
    Unknown7009(2)
    GFX_1('azef_206smoke_01', 3)
    GFX_0('203swing', -1)
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    SFX_0('209_down_normal_0')
    Unknown1084(1)
    sprite('az203_08', 3)	# 24-26
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    Recovery()
    Unknown2063()
    sprite('az203_09', 3)	# 27-29
    sprite('az203_10', 3)	# 30-32
    sprite('az203_11', 3)	# 33-35
    sprite('az203_12', 2)	# 36-37
    sprite('az203_13', 2)	# 38-39
    sprite('az203_14', 2)	# 40-41
    sprite('az203_15', 2)	# 42-43

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Unknown9154(17)
        AirUntechableTime(17)
        PushbackX(12000)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('BoostCancel')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_58 = 9

            def upon_45():
                if SLOT_58:
                    SLOT_58 = (SLOT_58 + (-1))
                else:
                    Unknown14070('NmlAtk5A')
                    Unknown14070('NmlAtk5B')
                    Unknown14070('NmlAtk2A')
                    Unknown14070('NmlAtk2B')
                    Unknown14070('CmnActCrushAttack')
                    Unknown14070('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('az200_00', 3)	# 1-3
    Unknown1051(60)
    sprite('az200_01', 2)	# 4-5
    Unknown7009(0)
    sprite('az200_02', 3)	# 6-8	 **attackbox here**
    SFX_0('005_swing_grap_2_0')
    sprite('az200_03', 3)	# 9-11	 **attackbox here**
    sprite('az200_04', 3)	# 12-14
    Recovery()
    Unknown2063()
    Unknown14072('NmlAtk5A')
    Unknown14072('NmlAtk5B')
    Unknown14072('NmlAtk2A')
    Unknown14072('NmlAtk2B')
    Unknown14072('CmnActCrushAttack')
    Unknown14072('NmlAtk2C')
    sprite('az200_05', 3)	# 15-17
    sprite('az200_06', 3)	# 18-20

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(18000)
        PushbackX(19800)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        callSubroutine('BoostCancel')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_58 = 11

            def upon_45():
                if SLOT_58:
                    SLOT_58 = (SLOT_58 + (-1))
                else:
                    Unknown14070('NmlAtk2A')
                    Unknown14070('NmlAtk2B')
    sprite('az202_00', 3)	# 1-3
    sprite('az202_01', 3)	# 4-6
    teleportRelativeX(-43000)
    sprite('az202_02', 2)	# 7-8
    teleportRelativeX(-37000)
    sprite('az202_03', 2)	# 9-10
    sprite('az202_04', 2)	# 11-12
    Unknown7009(5)
    SFX_0('005_swing_grap_2_2')
    sprite('az202_05', 3)	# 13-15	 **attackbox here**
    teleportRelativeX(75000)
    sprite('az202_06', 3)	# 16-18	 **attackbox here**
    sprite('az202_07', 2)	# 19-20
    teleportRelativeX(-50000)
    Recovery()
    Unknown2063()
    sprite('az202_08', 2)	# 21-22
    Unknown14072('NmlAtk2A')
    Unknown14072('NmlAtk2B')
    sprite('az202_09', 3)	# 23-25
    teleportRelativeX(-20000)
    sprite('az202_10', 3)	# 26-28
    teleportRelativeX(20000)
    sprite('az202_11', 2)	# 29-30
    teleportRelativeX(40000)
    sprite('az202_11', 1)	# 31-31
    Unknown14074('NmlAtk2A')
    Unknown14074('NmlAtk2B')
    sprite('az202_12', 3)	# 32-34

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(16200)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(2500)
        PushbackX(42000)
        AirUntechableTime(42)
        Unknown9310(1)
        sendToLabelUpon(2, 9)
        callSubroutine('BoostCancel')
        SLOT_61 = 0
        callSubroutine('WeakPointAttack_Pre')

        def upon_77():
            clearUponHandler(77)
            SLOT_61 = 1

        def upon_78():
            clearUponHandler(78)
            if 
            if (not op(6, 2, 4, 2, 5)):
                callSubroutine('WeakPointAttack_Judge'):
                AttackLevel_(5)
                Unknown9310(30)
                JumpCancel_(1)
                Unknown2037(1)
                ScreenShake(32000, 32000)
                GFX_0('weakhit01', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                callSubroutine('WeakPointAttack_Success')
                Unknown23159('NmlAtk5B2nd_True')
            else:
                Unknown7007('62617a3231315f3000000000000000006400000062617a3231315f3100000000000000006400000062617a3231315f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')

        def upon_STATE_END():
            if SLOT_61:
                SLOT_61 = SLOT_19
    sprite('az235_00', 2)	# 1-2
    sprite('az235_01', 3)	# 3-5
    sprite('az235_02', 5)	# 6-10
    sprite('az235_03', 2)	# 11-12
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000000000000')
    sprite('az235_04', 2)	# 13-14
    SFX_0('005_swing_grap_2_2')
    Unknown7009(2)
    sprite('az235_05', 2)	# 15-16	 **attackbox here**
    physicsXImpulse(43000)
    physicsYImpulse(16000)
    setGravity(5000)
    label(0)
    sprite('az235_06', 2)	# 17-18	 **attackbox here**
    Unknown1019(95)
    sprite('az235_07', 2)	# 19-20	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('az235_08', 1)	# 21-21
    setInvincible(0)
    physicsXImpulse(0)
    Recovery()
    Unknown2063()
    sprite('az235_09', 4)	# 22-25
    sprite('az235_10', 6)	# 26-31
    if SLOT_2:
        enterState('NmlAtk5B3rd')
    sprite('az235_11', 4)	# 32-35
    sprite('az235_12', 4)	# 36-39
    sprite('az235_13', 4)	# 40-43

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        if (SLOT_4 > 1):
            HitCancel('BoostDash')

        def upon_STATE_END():
            SLOT_61 = 0
    sprite('az406_00', 1)	# 1-1
    sprite('az406_01', 2)	# 2-3
    sprite('az406_04', 2)	# 4-5
    sprite('az406_05', 32767)	# 6-32772
    Unknown8001(1, 0)
    if SLOT_61:
        SLOT_12 = SLOT_61
        Unknown1019(5)
    else:
        physicsXImpulse(20000)
    physicsYImpulse(35000)
    setGravity(5000)

    def upon_4():
        clearUponHandler(4)
        sendToLabel(0)
    loopRest()
    label(0)
    sprite('az406_06', 2)	# 32773-32774
    Unknown7007('62617a3230365f3000000000000000006400000062617a3230365f3100000000000000006400000062617a3230365f320000000000000000640000000000000000000000000000000000000000000000')

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(9)
    Unknown23087(80000)
    sprite('az406_07', 2)	# 32775-32776
    sprite('az406_08', 2)	# 32777-32778
    sprite('az406_09', 32767)	# 32779-65545
    Unknown1039(400)
    loopRest()
    label(9)
    sprite('az406_10', 2)	# 65546-65547
    SFX_3('azse_07')
    Unknown1084(1)
    GFX_0('az406_dummy_5B3rd', -1)
    GFX_0('rocktest', -1)
    Unknown23087(-1)
    sprite('az406_11', 3)	# 65548-65550
    sprite('az406_12', 3)	# 65551-65553
    sprite('az406_13', 6)	# 65554-65559
    sprite('az406_14', 6)	# 65560-65565
    sprite('az010_01', 4)	# 65566-65569
    sprite('az010_00', 4)	# 65570-65573

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        AirPushbackX(-2000)
        AirPushbackY(15000)
        AirUntechableTime(25)
        PushbackX(15300)
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('WeakPointAttack_Pre')

        def upon_78():
            clearUponHandler(78)
            if 
            if (not op(6, 2, 4, 2, 5)):
                callSubroutine('WeakPointAttack_Judge'):
                AttackLevel_(5)
                Hitstop(15)
                AirPushbackY(23000)
                Unknown9154(25)
                AirUntechableTime(40)
                GFX_0('weakhit01', -1)
                ScreenShake(32000, 32000)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                callSubroutine('WeakPointAttack_Success')
            else:
                ScreenShake(8000, 8000)
                Unknown7009(2)
                SFX_3('azse_01')
    sprite('az233_00', 3)	# 1-3
    sprite('az233_01', 5)	# 4-8
    sprite('az233_02', 6)	# 9-14
    SFX_0('005_swing_grap_2_1')
    sprite('az233_03', 3)	# 15-17	 **attackbox here**
    Unknown7009(2)
    sprite('az233_04', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('az233_05', 3)	# 21-23
    sprite('az233_06', 3)	# 24-26
    sprite('az233_07', 3)	# 27-29
    sprite('az233_08', 3)	# 30-32

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(70)
        Unknown11033(1)
        Unknown11034(1)
        Unknown9154(22)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        AirPushbackX(8800)
        AirPushbackY(35000)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockJumpCancel(1)
        JumpCancel_(1)
        if (SLOT_4 > 1):
            HitCancel('BoostDash')
        Unknown2037(0)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Unknown9178(1)
            Unknown9362(1)
            Unknown9364(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                Unknown1017()

        def upon_ON_HIT_OR_BLOCK():
            Unknown14070('CmnActCrushAttack')
            Unknown14070('NmlAtk2C')
    sprite('az232_00', 2)	# 1-2
    sprite('az232_02', 3)	# 3-5
    sprite('az232_03', 1)	# 6-6
    GFX_0('232rock', -1)
    sprite('az232_03', 2)	# 7-8
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('az232_04', 2)	# 9-10
    Unknown7007('62617a3130365f3000000000000000006400000062617a3130365f3100000000000000006400000062617a3130365f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_1('azef_232smk_stone', 0)
    GFX_1('azef_232smk_stone', 1)
    sprite('az232_05', 2)	# 11-12
    SFX_3('azse_07')
    GFX_1('azef_232smk_stone', 0)
    GFX_1('azef_232smk_stone', 1)
    sprite('az232_06', 2)	# 13-14	 **attackbox here**
    GFX_1('azef_232smk_stone', 0)
    GFX_1('azef_232smk_stone', 1)
    GFX_1('azef_232smk_stone', 2)
    sprite('az232_07', 2)	# 15-16	 **attackbox here**
    sprite('az232_07', 2)	# 17-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    setInvincible(0)
    Unknown14072('CmnActCrushAttack')
    Unknown14072('NmlAtk2C')
    sprite('az232_08', 6)	# 19-24
    sprite('az232_09', 6)	# 25-30
    sprite('az232_10', 6)	# 31-36
    sprite('az232_11', 2)	# 37-38
    sprite('az232_11', 4)	# 39-42
    Unknown18009(1)
    Unknown14074('CmnActCrushAttack')
    Unknown14074('NmlAtk2C')
    sprite('az232_12', 6)	# 43-48

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirPushbackX(8000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(8000)
        AirUntechableTime(40)
        HitLow(2)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown11058('0000000000000000010000000000000000000000')
        JumpCancel_(0)
        Unknown9202(1)
        Unknown9310(1)
        callSubroutine('WeakPointAttack_Pre')

        def upon_78():
            clearUponHandler(78)
            if 
            if (not op(6, 2, 4, 2, 5)):
                callSubroutine('WeakPointAttack_Judge'):
                AttackLevel_(5)
                AirPushbackY(-36000)
                if SLOT_125:
                    AirPushbackY(-28000)
                Unknown9095()
                Hitstop(15)
                AirUntechableTime(60)
                Unknown9190(1)
                ScreenShake(32000, 32000)
                GFX_0('weakhit01', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                Unknown9202(0)
                Unknown9310(0)
                callSubroutine('WeakPointAttack_Success')
                Unknown23159('NmlAtk2C_True')
            else:
                Unknown7007('62617a3130375f3000000000000000006400000062617a3130375f3100000000000000006400000062617a3130375f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
    sprite('az213_00', 3)	# 1-3
    sprite('az213_01', 3)	# 4-6
    Unknown2015(230)
    physicsXImpulse(35000)
    sprite('az213_02', 3)	# 7-9
    Unknown1019(50)
    sprite('az234_00', 2)	# 10-11
    Unknown2015(-1)
    Unknown2016(370)
    Unknown1019(50)
    sprite('az234_00', 2)	# 12-13
    Unknown1019(50)
    sprite('az234_01', 4)	# 14-17
    Unknown1019(80)
    sprite('az234_01', 3)	# 18-20
    Unknown1019(80)
    SFX_0('005_swing_grap_2_2')
    sprite('az234_02', 3)	# 21-23
    SFX_3('azse_07')
    Unknown1019(80)
    sprite('az234_03', 3)	# 24-26	 **attackbox here**
    GFX_0('213rock', 0)
    Unknown36(1)
    Unknown2005()
    teleportRelativeX(-15000)
    Unknown35()
    ScreenShake(10000, 10000)
    Unknown7007('62617a3130375f3000000000000000006400000062617a3130375f3100000000000000006400000062617a3130375f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(0)
    Unknown2015(230)
    Unknown2016(320)
    sprite('az234_04', 3)	# 27-29	 **attackbox here**
    Unknown2016(-1)
    sprite('az234_05', 3)	# 30-32
    Recovery()
    Unknown2063()
    sprite('az234_06', 3)	# 33-35
    sprite('az234_07', 3)	# 36-38
    sprite('az234_08', 3)	# 39-41
    sprite('az234_09', 3)	# 42-44

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOverhead(2)
        AirUntechableTime(19)
        AirPushbackY(20000)
        PushbackX(8000)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        callSubroutine('BoostCancel')
        callSubroutine('HomingCancel')
    sprite('az251_00', 2)	# 1-2
    sprite('az251_01', 2)	# 3-4
    sprite('az251_02', 2)	# 5-6
    Unknown7009(3)
    sprite('az251_03', 2)	# 7-8
    SFX_0('005_swing_grap_2_1')
    sprite('az251_04', 3)	# 9-11	 **attackbox here**
    sprite('az251_05', 2)	# 12-13
    sprite('az251_06', 3)	# 14-16	 **attackbox here**
    sprite('az251_07', 2)	# 17-18
    Recovery()
    Unknown2063()
    sprite('az251_08', 2)	# 19-20
    sprite('az251_09', 3)	# 21-23
    sprite('az251_10', 3)	# 24-26
    sprite('az251_11', 2)	# 27-28

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOverhead(2)
        AirUntechableTime(25)
        PushbackX(15000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        callSubroutine('BoostCancel')
        callSubroutine('HomingCancel')
    sprite('az252_00', 2)	# 1-2
    sprite('az252_01', 2)	# 3-4
    sprite('az252_02', 2)	# 5-6
    Unknown7009(4)
    sprite('az252_03', 3)	# 7-9
    SFX_0('005_swing_grap_2_2')
    sprite('az252_04', 3)	# 10-12	 **attackbox here**
    sprite('az252_05', 3)	# 13-15	 **attackbox here**
    sprite('az252_06', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('az252_07', 3)	# 19-21
    sprite('az252_08', 3)	# 22-24
    sprite('az252_09', 3)	# 25-27
    sprite('az252_10', 3)	# 28-30

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(30)
        AirPushbackX(36000)
        AirPushbackY(-36000)
        PushbackX(15000)
        HitOverhead(2)
        callSubroutine('WeakPointAttack_Pre')

        def upon_78():
            clearUponHandler(78)
            if 
            if (not op(6, 2, 4, 2, 5)):
                callSubroutine('WeakPointAttack_Judge'):
                AttackLevel_(5)
                Hitstop(15)
                AirUntechableTime(60)
                AirHitstunAnimation(9)
                Unknown9190(1)
                Unknown9118(50)
                AirPushbackX(10000)
                AirPushbackY(-36000)
                ScreenShake(32000, 32000)
                GFX_0('weakhit00', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                callSubroutine('WeakPointAttack_Success')
            else:
                ScreenShake(4000, 4000)
                Unknown7009(4)
                SFX_3('azse_01')
    sprite('az253_00', 2)	# 1-2
    sprite('az253_01', 2)	# 3-4
    sprite('az253_02', 2)	# 5-6
    sprite('az253_03', 2)	# 7-8
    sprite('az253_04', 2)	# 9-10
    sprite('az253_05', 3)	# 11-13
    sprite('az253_06', 3)	# 14-16
    SFX_0('005_swing_grap_2_2')
    Unknown7009(4)
    sprite('az253_07', 2)	# 17-18
    sprite('az253_08', 5)	# 19-23	 **attackbox here**
    GFX_0('253swing', -1)
    sprite('az253_09', 4)	# 24-27
    Recovery()
    Unknown2063()
    sprite('az253_10', 3)	# 28-30
    sprite('az253_11', 3)	# 31-33
    sprite('az253_12', 3)	# 34-36
    sprite('az253_13', 3)	# 37-39

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1800)
        HitOverhead(0)
        AirPushbackX(12000)
        AirPushbackY(-58000)
        callSubroutine('HomingCancel')
        callSubroutine('BoostCancel')
    sprite('az254_00', 3)	# 1-3
    sprite('az254_01', 2)	# 4-5
    Unknown1084(1)
    physicsYImpulse(20000)
    physicsXImpulse(10000)
    Unknown1019(20)
    setGravity(1500)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('az254_02', 2)	# 6-7
    sprite('az254_03', 2)	# 8-9
    sprite('az254_01', 2)	# 10-11
    sprite('az254_02', 2)	# 12-13
    sprite('az254_03', 2)	# 14-15
    sprite('az254_01', 2)	# 16-17
    sprite('az254_02', 2)	# 18-19
    Unknown7009(2)
    sprite('az254_03', 2)	# 20-21
    SFX_0('005_swing_grap_2_2')
    sprite('az254_04', 2)	# 22-23	 **attackbox here**
    physicsXImpulse(10000)
    physicsYImpulse(-48000)
    label(0)
    sprite('az254_05', 2)	# 24-25	 **attackbox here**
    sprite('az254_06', 2)	# 26-27	 **attackbox here**
    sprite('az254_07', 2)	# 28-29	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az024_00', 2)	# 30-31
    Unknown1084(1)
    sprite('az024_01', 2)	# 32-33
    sprite('az024_02', 2)	# 34-35
    sprite('az024_03', 2)	# 36-37
    sprite('az024_04', 2)	# 38-39

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown2004(1, 0)
    sprite('az213_00', 2)	# 1-2
    sprite('az213_01', 3)	# 3-5
    physicsXImpulse(35000)
    sprite('az213_02', 3)	# 6-8
    Unknown1019(50)
    sprite('az213_03', 2)	# 9-10
    Unknown1019(50)
    sprite('az213_03', 2)	# 11-12
    Unknown1019(50)
    sprite('az213_04', 3)	# 13-15
    Unknown2016(350)
    Unknown1019(70)
    sprite('az213_05', 4)	# 16-19
    Unknown1019(80)
    sprite('az213_05', 4)	# 20-23
    Unknown1019(80)
    SFX_0('005_swing_grap_2_2')
    sprite('az213_06', 2)	# 24-25
    Unknown1019(80)
    sprite('az213_07', 3)	# 26-28	 **attackbox here**
    SFX_3('azse_07')
    tag_voice(1, 'baz156_0', 'baz156_1', '', '')
    GFX_0('213swing', -1)
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    physicsXImpulse(0)
    sprite('az213_08', 4)	# 29-32	 **attackbox here**
    StartMultihit()
    GFX_1('azef_406_smoke', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    GFX_0('213rock', 3)
    Unknown36(1)
    Unknown2005()
    Unknown1072(10000)
    Unknown35()
    GFX_0('213rock', 4)
    Unknown36(1)
    Unknown1072(10000)
    Unknown35()
    ScreenShake(6000, 6000)
    sprite('az213_09', 4)	# 33-36
    Unknown2016(-1)
    sprite('az213_10', 4)	# 37-40
    sprite('az213_11', 4)	# 41-44
    sprite('az213_12', 2)	# 45-46

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown2004(1, 0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('az213_07', 2)	# 2-3	 **attackbox here**
    StartMultihit()
    physicsXImpulse(-20000)
    sprite('az213_08', 4)	# 4-7	 **attackbox here**
    StartMultihit()
    sprite('az213_09', 4)	# 8-11
    Unknown1019(70)
    sprite('az213_10', 4)	# 12-15
    sprite('az213_11', 4)	# 16-19
    Unknown1019(50)
    sprite('az213_12', 2)	# 20-21
    Unknown1019(0)
    loopRest()
    teleportRelativeX(260000)
    sprite('az401_00ex01', 4)	# 22-25
    sprite('az401_01ex01', 2)	# 26-27
    SFX_0('005_swing_grap_2_2')
    sprite('az401_02ex01', 2)	# 28-29
    tag_voice(0, 'baz157_0', 'baz157_1', '', '')
    sprite('az401_03ex01', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('BrustDD_SlashEff', -1)
    sprite('az401_04ex01', 4)	# 33-36
    sprite('az401_05ex01', 4)	# 37-40
    sprite('az401_06ex01', 4)	# 41-44
    sprite('az401_07ex01', 4)	# 45-48
    sprite('az401_08ex01', 4)	# 49-52
    sprite('az000_00', 7)	# 53-59
    sprite('az000_01', 7)	# 60-66
    sprite('az000_02', 7)	# 67-73
    sprite('az000_03', 7)	# 74-80
    sprite('az000_04', 7)	# 81-87
    sprite('az000_05', 7)	# 88-94
    sprite('az000_06', 7)	# 95-101
    sprite('az000_07', 7)	# 102-108
    sprite('az000_08', 7)	# 109-115
    sprite('az000_09', 7)	# 116-122
    sprite('az001_00', 6)	# 123-128
    sprite('az001_01', 6)	# 129-134
    sprite('az001_02', 6)	# 135-140
    sprite('az001_03', 6)	# 141-146
    sprite('az001_04', 6)	# 147-152
    sprite('az001_05', 6)	# 153-158
    sprite('az001_06', 6)	# 159-164
    sprite('az001_03', 6)	# 165-170
    sprite('az001_04', 6)	# 171-176
    sprite('az001_05', 6)	# 177-182
    sprite('az001_06', 6)	# 183-188
    sprite('az001_01', 6)	# 189-194
    sprite('az001_00', 6)	# 195-200
    label(0)
    sprite('az000_00', 7)	# 201-207
    sprite('az000_01', 7)	# 208-214
    sprite('az000_02', 7)	# 215-221
    sprite('az000_03', 7)	# 222-228
    sprite('az000_04', 7)	# 229-235
    sprite('az000_05', 7)	# 236-242
    sprite('az000_06', 7)	# 243-249
    sprite('az000_07', 7)	# 250-256
    sprite('az000_08', 7)	# 257-263
    sprite('az000_09', 7)	# 264-270
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 271-271

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('az400_01ex01', 5)	# 1-5
    sprite('az400_02ex01', 4)	# 6-9
    sprite('az400_02ex01', 2)	# 10-11
    GFX_0('BrustDD_SlashEff2', -1)
    sprite('az400_03ex01', 3)	# 12-14
    sprite('az400_04ex01', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    SFX_3('azse_02')
    sprite('az400_05ex01', 3)	# 18-20
    sprite('az400_06ex01', 3)	# 21-23
    sprite('az400_07ex01', 3)	# 24-26
    sprite('az001_00', 6)	# 27-32
    sprite('az001_01', 6)	# 33-38
    sprite('az001_02', 6)	# 39-44
    sprite('az001_03', 6)	# 45-50
    sprite('az001_04', 6)	# 51-56
    sprite('az001_05', 6)	# 57-62
    sprite('az001_06', 6)	# 63-68
    sprite('az001_03', 6)	# 69-74
    sprite('az001_04', 6)	# 75-80
    sprite('az001_05', 6)	# 81-86
    sprite('az001_06', 6)	# 87-92
    sprite('az001_01', 6)	# 93-98
    sprite('az001_00', 6)	# 99-104
    label(0)
    sprite('az000_00', 7)	# 105-111
    sprite('az000_01', 7)	# 112-118
    sprite('az000_02', 7)	# 119-125
    sprite('az000_03', 7)	# 126-132
    sprite('az000_04', 7)	# 133-139
    sprite('az000_05', 7)	# 140-146
    sprite('az000_06', 7)	# 147-153
    sprite('az000_07', 7)	# 154-160
    sprite('az000_08', 7)	# 161-167
    sprite('az000_09', 7)	# 168-174
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 175-175

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('az404_00', 4)	# 1-4
    GFX_0('404tame', -1)
    SFX_3('azse_11')
    sprite('az404_01', 3)	# 5-7
    sprite('az404_02', 3)	# 8-10
    sprite('az404_03', 3)	# 11-13
    sprite('az404_04', 3)	# 14-16
    Unknown21015('34303474616d6500000000000000000000000000000000000000000000000000c90f000000000000')
    sprite('az404_05', 3)	# 17-19
    SFX_3('azse_14')
    GFX_0('404swing', -1)
    GFX_0('404nigiyakasi', -1)
    tag_voice(0, 'baz158_0', 'baz158_1', '', '')
    sprite('az404_06', 3)	# 20-22	 **attackbox here**
    sprite('az404_07', 3)	# 23-25	 **attackbox here**
    sprite('az404_08', 3)	# 26-28	 **attackbox here**
    sprite('az404_09', 4)	# 29-32
    sprite('az404_10', 4)	# 33-36
    sprite('az404_11', 4)	# 37-40
    sprite('az404_12', 4)	# 41-44
    sprite('az404_13', 4)	# 45-48
    sprite('az404_14', 3)	# 49-51
    sprite('az404_15', 3)	# 52-54
    sprite('az404_16', 3)	# 55-57
    sprite('az404_17', 3)	# 58-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown23027()
    sprite('null', 33)	# 1-33
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 34-34
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-250000)
    Unknown1007(600000)
    physicsYImpulse(-75000)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    label(0)
    sprite('az409_14', 3)	# 35-37	 **attackbox here**
    GFX_0('azef_409_fall', 0)
    sprite('az409_15', 3)	# 38-40	 **attackbox here**
    label(2)
    sprite('az409_14', 3)	# 41-43	 **attackbox here**
    sprite('az409_15', 3)	# 44-46	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('az409_16', 4)	# 47-50	 **attackbox here**
    RefreshMultihit()
    SFX_3('azse_07')
    Unknown26('azef_409_fall')
    GFX_0('azef_409_rock', -1)
    Unknown1084(1)
    ScreenShake(10000, 20000)
    sprite('az409_19', 4)	# 51-54
    sprite('az409_20', 3)	# 55-57
    sprite('az409_21', 3)	# 58-60
    sprite('az000_00', 7)	# 61-67
    sprite('az000_01', 7)	# 68-74
    sprite('az000_02', 7)	# 75-81
    sprite('az000_03', 7)	# 82-88
    sprite('az000_04', 7)	# 89-95
    sprite('az000_05', 7)	# 96-102
    sprite('az000_06', 7)	# 103-109
    sprite('az000_07', 7)	# 110-116
    sprite('az000_08', 7)	# 117-123
    sprite('az000_09', 7)	# 124-130
    sprite('az000_00', 7)	# 131-137
    sprite('az000_01', 7)	# 138-144

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('az201_08', 3)	# 1-3
    sprite('az201_09', 4)	# 4-7
    sprite('az201_10', 4)	# 8-11
    sprite('az201_11', 3)	# 12-14	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('az201_12', 3)	# 15-17
    sprite('az201_13', 3)	# 18-20
    sprite('az201_14', 3)	# 21-23
    sprite('az001_00', 6)	# 24-29
    sprite('az001_01', 6)	# 30-35
    sprite('az001_02', 6)	# 36-41
    sprite('az001_03', 6)	# 42-47
    sprite('az001_04', 6)	# 48-53
    sprite('az001_05', 6)	# 54-59
    sprite('az001_06', 6)	# 60-65
    sprite('az001_03', 6)	# 66-71
    sprite('az001_04', 6)	# 72-77
    sprite('az001_05', 6)	# 78-83
    sprite('az001_06', 6)	# 84-89
    sprite('az001_01', 6)	# 90-95
    sprite('az001_00', 6)	# 96-101
    sprite('az000_00', 7)	# 102-108
    sprite('az000_01', 7)	# 109-115
    sprite('az000_02', 7)	# 116-122
    sprite('az000_03', 7)	# 123-129
    sprite('az000_04', 7)	# 130-136
    sprite('az000_05', 7)	# 137-143
    sprite('az000_06', 7)	# 144-150
    sprite('az000_07', 7)	# 151-157
    sprite('az000_08', 7)	# 158-164
    sprite('az000_09', 7)	# 165-171
    sprite('az000_00', 7)	# 172-178
    sprite('az000_01', 7)	# 179-185

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('az404_00', 4)	# 1-4
    GFX_0('404tame', -1)
    SFX_3('azse_11')
    sprite('az404_01', 3)	# 5-7
    sprite('az404_02', 3)	# 8-10
    sprite('az404_03', 3)	# 11-13
    sprite('az404_04', 3)	# 14-16
    Unknown21015('34303474616d6500000000000000000000000000000000000000000000000000c90f000000000000')
    sprite('az404_05', 3)	# 17-19
    SFX_3('azse_14')
    GFX_0('404swing', -1)
    GFX_0('404nigiyakasi', -1)
    sprite('az404_06', 3)	# 20-22	 **attackbox here**
    sprite('az404_07', 3)	# 23-25	 **attackbox here**
    sprite('az404_08', 3)	# 26-28	 **attackbox here**
    sprite('az404_09', 4)	# 29-32
    sprite('az404_10', 4)	# 33-36
    sprite('az404_11', 4)	# 37-40
    sprite('az404_12', 4)	# 41-44
    sprite('az404_13', 4)	# 45-48
    sprite('az404_14', 3)	# 49-51
    sprite('az404_15', 3)	# 52-54
    sprite('az404_16', 3)	# 55-57
    sprite('az404_17', 3)	# 58-60

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(9000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('az030_00', 8)	# 1-8
    label(0)
    sprite('az030_01', 8)	# 9-16
    sprite('az030_02', 8)	# 17-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 8)	# 25-32
    sprite('az030_04', 8)	# 33-40
    sprite('az030_05', 8)	# 41-48
    sprite('az030_06', 8)	# 49-56
    sprite('az030_07', 8)	# 57-64
    sprite('az030_08', 8)	# 65-72
    sprite('az030_09', 8)	# 73-80
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 8)	# 81-88
    sprite('az030_11', 8)	# 89-96
    sprite('az030_12', 8)	# 97-104
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az310_00', 2)	# 105-106
    clearUponHandler(3)
    Unknown1019(10)
    sprite('az310_01', 1)	# 107-107
    SFX_0('005_swing_grap_2_2')
    sprite('az310_02', 3)	# 108-110	 **attackbox here**
    Unknown1084(1)
    sprite('az310_03', 4)	# 111-114
    SFX_4('baz154')
    sprite('az310_04', 9)	# 115-123
    sprite('az310_05', 5)	# 124-128
    sprite('az310_06', 5)	# 129-133

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(2200)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown11072(1, 150000, 250000)
    sprite('az310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('az311_00', 3)	# 4-6
    SFX_4('baz153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_01', 3)	# 7-9
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_02', 3)	# 10-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_03', 5)	# 13-17
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_04', 4)	# 18-21
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_05', 4)	# 22-25
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_06', 3)	# 26-28	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    StartMultihit()
    Unknown5000(25, 0)
    Unknown5001('0000000005000000010000000000000000000000')
    sprite('az311_08', 3)	# 29-31
    Unknown5000(25, 0)
    Unknown5001('0000000005000000010000000000000000000000')
    sprite('az311_09', 10)	# 32-41	 **attackbox here**
    RefreshMultihit()
    sprite('az311_10', 3)	# 42-44
    sprite('az311_11', 3)	# 45-47
    sprite('az311_12', 3)	# 48-50
    sprite('az311_13', 3)	# 51-53
    sprite('az311_14', 3)	# 54-56

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(9000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('az030_00', 8)	# 1-8
    label(0)
    sprite('az030_01', 8)	# 9-16
    sprite('az030_02', 8)	# 17-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 8)	# 25-32
    sprite('az030_04', 8)	# 33-40
    sprite('az030_05', 8)	# 41-48
    sprite('az030_06', 8)	# 49-56
    sprite('az030_07', 8)	# 57-64
    sprite('az030_08', 8)	# 65-72
    sprite('az030_09', 8)	# 73-80
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 8)	# 81-88
    sprite('az030_11', 8)	# 89-96
    sprite('az030_12', 8)	# 97-104
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az310_00', 2)	# 105-106
    clearUponHandler(3)
    Unknown1019(10)
    sprite('az310_01', 1)	# 107-107
    SFX_0('005_swing_grap_2_2')
    sprite('az310_02', 3)	# 108-110	 **attackbox here**
    Unknown1084(1)
    sprite('az310_03', 4)	# 111-114
    SFX_4('baz154')
    sprite('az310_04', 9)	# 115-123
    sprite('az310_05', 5)	# 124-128
    sprite('az310_06', 5)	# 129-133

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirPushbackX(-10000)
        AirPushbackY(-54000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        Unknown9118(45)
        AirUntechableTime(40)
        Unknown9310(1)
        Unknown2004(1, 0)
        Unknown13021(1)
        Unknown21005(1)
    sprite('az310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('az311_00', 3)	# 4-6
    SFX_4('baz153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_01', 3)	# 7-9
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_02', 3)	# 10-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_03', 5)	# 13-17
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_04', 5)	# 18-22
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_05', 5)	# 23-27
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('az311_06', 15)	# 28-42	 **attackbox here**
    SFX_0('100_hit_grap_2')
    Unknown5000(25, 0)
    Unknown5001('0000000005000000010000000000000000000000')
    StartMultihit()
    Unknown23011(1)
    GFX_1('ef_hitmd', 0)
    sprite('az311_07', 3)	# 43-45
    Unknown5000(25, 0)
    Unknown5001('0000000005000000010000000000000000000000')
    sprite('az313_00', 3)	# 46-48
    Unknown5000(26, 0)
    Unknown5001('0000000005000000010000000000000000000000')
    Unknown2018(0, 80)
    sprite('az313_01', 3)	# 49-51
    Unknown5000(26, 0)
    Unknown5001('0000000005000000010000000000000000000000')
    sprite('az313_02', 3)	# 52-54
    Unknown5000(6, 0)
    Unknown5001('0000000005000000010000000000000000000000')
    sprite('az313_03', 3)	# 55-57	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('az313_04', 3)	# 58-60
    sprite('az313_05', 3)	# 61-63
    sprite('az313_06', 3)	# 64-66
    sprite('az313_07', 3)	# 67-69
    sprite('az313_08', 3)	# 70-72
    sprite('az313_09', 3)	# 73-75
    sprite('az313_10', 3)	# 76-78

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1800)
        Unknown11092(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackX(10000)
        AirPushbackY(36000)
        Unknown11001(0, 0, 0)
        Hitstop(14)

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(60)

        def upon_12():
            ScreenShake(2000, 12000)

        def upon_LANDING():
            sendToLabel(9)
        callSubroutine('BoostCancel')
    sprite('az409_00', 3)	# 1-3
    sprite('az409_01', 3)	# 4-6
    sprite('az409_02', 3)	# 7-9
    sprite('az409_03', 5)	# 10-14
    sprite('az409_04', 3)	# 15-17
    Unknown7007('62617a3231335f3000000000000000006400000062617a3231335f3100000000000000006400000062617a3231335f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(20000)
    sprite('az409_05', 3)	# 18-20	 **attackbox here**
    Unknown8001(1, 0)
    physicsXImpulse(48000)
    physicsYImpulse(50000)
    setGravity(2000)
    GFX_1('azef_409jump_a', -1)
    sprite('az409_06', 3)	# 21-23	 **attackbox here**
    GFX_1('azef_409jump_b', -1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('az409_05', 3)	# 24-26	 **attackbox here**
    GFX_1('azef_409jump_b', -1)
    sprite('az409_06', 3)	# 27-29	 **attackbox here**
    GFX_1('azef_409jump_b', -1)
    sprite('az409_07', 2)	# 30-31
    setInvincible(0)
    Unknown1019(20)
    setGravity(3000)

    def upon_3():
        if CheckInput(0x79):
            Unknown1015(200)
    sprite('az409_08', 2)	# 32-33
    sprite('az409_09', 2)	# 34-35
    sprite('az409_10', 3)	# 36-38
    sprite('az409_11', 3)	# 39-41
    sprite('az409_12', 2)	# 42-43
    sprite('az409_13', 2)	# 44-45
    sprite('az409_14', 3)	# 46-48	 **attackbox here**
    GFX_0('azef_409_fall', 0)
    physicsYImpulse(-38000)
    clearUponHandler(3)
    RefreshMultihit()
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(3000)
    AirPushbackY(-80000)
    PushbackX(12000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown9118(35)
    HitAirUnblockable(2)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('az409_15', 3)	# 49-51	 **attackbox here**
    label(2)
    sprite('az409_14', 3)	# 52-54	 **attackbox here**
    sprite('az409_15', 3)	# 55-57	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('az409_16', 4)	# 58-61	 **attackbox here**
    SFX_3('azse_07')
    Unknown26('azef_409_fall')
    GFX_0('azef_409_rock', -1)
    Unknown1084(1)
    ScreenShake(10000, 20000)
    AirPushbackY(-80000)
    Unknown11032('40420f0000000000ffffffffffffffff')
    sprite('az409_17', 4)	# 62-65
    sprite('az409_18', 4)	# 66-69
    sprite('az409_19', 4)	# 70-73
    sprite('az409_17', 4)	# 74-77
    sprite('az409_18', 4)	# 78-81
    sprite('az409_19', 4)	# 82-85
    sprite('az409_20', 3)	# 86-88
    sprite('az409_21', 3)	# 89-91

@State
def Assault():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(80)
        Unknown9154(33)
        AirUntechableTime(24)
        Unknown11028(30)
        AirPushbackX(16200)
        AirPushbackY(13000)
        PushbackX(19800)
        Unknown11056(0)

        def upon_3():
            if SLOT_51:
                if (SLOT_19 < 550000):
                    sendToLabel(0)
                    SLOT_51 = 0

        def upon_12():
            SFX_0('025_cleanhit_grap')

        def upon_11():
            if (SLOT_19 < 200000):
                PushbackX(39800)
            else:
                Unknown1045(10000)
        callSubroutine('BoostCancel')
    sprite('az405_00', 2)	# 1-2
    sprite('az405_01', 2)	# 3-4
    Unknown7007('62617a3230305f3000000000000000006400000062617a3230305f3100000000000000006400000062617a3230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('az405_02', 2)	# 5-6
    sprite('az405_03', 2)	# 7-8
    sprite('az405_04', 1)	# 9-9
    physicsXImpulse(52000)
    SLOT_51 = 1
    GFX_0('405smoke', -1)
    GFX_0('213rock', -1)
    sprite('az405_04', 1)	# 10-10
    Unknown1028(2000)
    sprite('az405_05', 2)	# 11-12
    sprite('az405_06', 2)	# 13-14
    PushbackX(19800)
    sprite('az405_04', 2)	# 15-16
    sprite('az405_05', 2)	# 17-18
    Unknown1019(80)
    sprite('az405_06', 1)	# 19-19
    label(0)
    Unknown26('405smoke')
    clearUponHandler(3)
    sprite('az405_07', 1)	# 20-20
    SFX_0('005_swing_grap_2_2')
    SFX_3('azse_05')
    Unknown1019(90)
    GFX_1('azef_blood_01', 0)
    sprite('az405_08', 1)	# 21-21	 **attackbox here**
    StartMultihit()
    Unknown1019(80)
    GFX_0('405punch', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    GFX_1('azef_blood_01', 3)
    sprite('az405_09', 6)	# 22-27	 **attackbox here**
    Unknown1019(20)
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    sprite('az405_10', 4)	# 28-31
    Recovery()
    Unknown1019(0)
    Unknown1084(1)
    sprite('az405_11', 4)	# 32-35
    sprite('az405_12', 3)	# 36-38
    sprite('az405_13', 4)	# 39-42
    sprite('az405_14', 4)	# 43-46
    sprite('az405_15', 4)	# 47-50
    sprite('az405_16', 3)	# 51-53

@State
def AZcombo1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        Unknown11050('04000000617a65665f343030696d706163746869745f636972636c650000000000000000')
        AirPushbackX(8000)
        HitOrBlockCancel('AZcombo2')
        WhiffCancel('AZcombo2')
        callSubroutine('BoostCancel')
    sprite('az400_00', 4)	# 1-4
    sprite('az400_01', 4)	# 5-8
    GFX_0('405smoke', -1)
    tag_voice(1, 'baz201_0', 'baz201_1', 'baz201_2', '')
    physicsXImpulse(28000)
    sprite('az400_02', 3)	# 9-11
    Unknown1019(80)
    sprite('az400_03', 3)	# 12-14
    Unknown1019(50)
    SFX_0('005_swing_grap_2_2')
    sprite('az400_04', 3)	# 15-17	 **attackbox here**
    GFX_0('400impact', -1)
    physicsXImpulse(0)
    Unknown26('405smoke')
    sprite('az400_05', 3)	# 18-20
    Recovery()
    WhiffCancelEnable(1)
    sprite('az400_06', 3)	# 21-23
    sprite('az400_07', 3)	# 24-26
    sprite('az400_08', 3)	# 27-29
    Unknown14077(0)
    WhiffCancelEnable(0)
    sprite('az400_09', 2)	# 30-31
    sprite('az400_10', 2)	# 32-33
    sprite('az400_11', 2)	# 34-35

@State
def AZcombo2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        Unknown11050('04000000617a65665f343031696d706163746869745f6c696e6500000000000000000000')
        AirPushbackX(13200)
        Unknown9154(23)
        AirUntechableTime(36)
        AirPushbackY(10000)
        AirHitstunAnimation(13)
        YImpluseBeforeWallbounce(1800)
        HitOrBlockCancel('AZcombo3')
        WhiffCancel('AZcombo3')
        Unknown30068(1)
    sprite('az401_10', 3)	# 1-3
    Unknown2016(350)
    physicsXImpulse(30000)
    sprite('az401_10', 3)	# 4-6
    Unknown1019(30)
    sprite('az401_11', 3)	# 7-9
    SFX_3('azse_05')
    SFX_0('005_swing_grap_2_2')
    Unknown1019(30)
    sprite('az401_03', 5)	# 10-14	 **attackbox here**
    tag_voice(0, 'baz202_0', 'baz202_1', 'baz202_2', '')
    GFX_1('azef_206smoke_01', 0)
    GFX_0('401swing', -1)
    physicsXImpulse(0)
    sprite('az401_04', 6)	# 15-20
    Recovery()
    WhiffCancelEnable(1)
    sprite('az401_05', 2)	# 21-22
    Unknown14077(0)
    WhiffCancelEnable(0)
    sprite('az401_06', 2)	# 23-24
    sprite('az401_07', 2)	# 25-26
    sprite('az401_08', 3)	# 27-29
    sprite('az401_09', 3)	# 30-32
    Unknown2016(-1)

@State
def AZcombo3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2100)
        Unknown11050('04000000617a65665f343032696d706163746869745f706f730000000000000000000000')
        Hitstop(20)
        AirPushbackX(40000)
        AirPushbackY(20000)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirUntechableTime(60)
        Unknown11056(0)

        def upon_12():
            SFX_0('025_cleanhit_grap')
        callSubroutine('BoostCancel')
        Unknown30068(1)
    sprite('az402_16', 3)	# 1-3
    sprite('az402_17', 3)	# 4-6
    sprite('az402_02', 5)	# 7-11
    sprite('az402_03', 2)	# 12-13
    physicsXImpulse(50000)
    Unknown2016(350)
    sprite('az402_04', 2)	# 14-15
    SFX_3('azse_07')
    tag_voice(0, 'baz203_0', 'baz203_1', 'baz203_2', '')
    sprite('az402_05', 3)	# 16-18	 **attackbox here**
    GFX_0('402swing', -1)
    GFX_0('402rock1', -1)
    sprite('az402_06', 3)	# 19-21
    sprite('az402_07', 3)	# 22-24
    Unknown1019(30)
    sprite('az402_08', 3)	# 25-27
    Unknown1019(80)
    sprite('az402_09', 3)	# 28-30
    Unknown1019(80)
    sprite('az402_10', 3)	# 31-33
    Unknown1019(80)
    sprite('az402_11', 3)	# 34-36
    Unknown1019(0)
    sprite('az402_12', 3)	# 37-39
    sprite('az402_13', 3)	# 40-42
    sprite('az402_14', 3)	# 43-45
    sprite('az402_15', 3)	# 46-48
    Unknown2016(-1)

@State
def ShotAtemi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(90)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(15000)
        AirPushbackY(36000)
        AirUntechableTime(45)

        def upon_42():
            if Unknown23037():
                SLOT_59 = (SLOT_59 + 1)
                if (SLOT_59 >= 3):
                    SLOT_59 = 3
                sendToLabel(0)
                SFX_3('azse_04')
                Unknown7015()
                Unknown22019('0100000001000000010000000100000001000000')
                Unknown22036(1)
                if (not Unknown46(7)):
                    GFX_0('407Kyushu', -1)
                    Unknown38(7, 1)
            else:
                pass

        def upon_3():
            if SLOT_59:
                callSubroutine('CheckShotCatch')

        def upon_STATE_END():
            Unknown7015()
        callSubroutine('BoostCancel')
    sprite('az407_00', 1)	# 1-1
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    GuardPoint_(1)
    Unknown1084(1)
    sprite('az407_01', 1)	# 2-2
    sprite('az407_02', 1)	# 3-3
    sprite('az407_03', 1)	# 4-4	 **attackbox here**
    StartMultihit()
    GFX_0('407aura', -1)
    SFX_3('azse_03')
    tag_voice(1, 'baz207_0', 'baz207_1', 'baz207_2', '')
    sprite('az407_03', 2)	# 5-6	 **attackbox here**
    StartMultihit()
    sprite('az407_03', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    sprite('az407_04', 4)	# 8-11	 **attackbox here**
    sprite('az407_05', 4)	# 12-15	 **attackbox here**
    Unknown23027()
    sprite('az407_02', 4)	# 16-19
    Unknown7014('azse_03_loop')
    sprite('az407_03', 4)	# 20-23	 **attackbox here**
    sprite('az407_04', 4)	# 24-27	 **attackbox here**
    sprite('az407_05', 4)	# 28-31	 **attackbox here**
    sprite('az407_02', 4)	# 32-35
    sprite('az407_03', 4)	# 36-39	 **attackbox here**
    sendToLabelUpon(23, 1)
    sprite('az407_04', 4)	# 40-43	 **attackbox here**
    sprite('az407_05', 3)	# 44-46	 **attackbox here**
    sprite('az407_05', 1)	# 47-47	 **attackbox here**
    sprite('az407_02', 4)	# 48-51
    sprite('az407_03', 4)	# 52-55	 **attackbox here**
    sprite('az407_04', 4)	# 56-59	 **attackbox here**
    sprite('az407_05', 4)	# 60-63	 **attackbox here**
    sprite('az407_02', 4)	# 64-67
    sprite('az407_03', 4)	# 68-71	 **attackbox here**
    sprite('az407_04', 4)	# 72-75	 **attackbox here**
    sprite('az407_05', 4)	# 76-79	 **attackbox here**
    sprite('az407_02', 4)	# 80-83
    sprite('az407_03', 4)	# 84-87	 **attackbox here**
    sprite('az407_04', 4)	# 88-91	 **attackbox here**
    sprite('az407_05', 4)	# 92-95	 **attackbox here**
    sprite('az407_02', 4)	# 96-99
    sprite('az407_03', 4)	# 100-103	 **attackbox here**
    sprite('az407_04', 4)	# 104-107	 **attackbox here**
    sprite('az407_05', 4)	# 108-111	 **attackbox here**
    gotoLabel(1)
    label(0)
    clearUponHandler(23)
    sprite('az407_06', 5)	# 112-116
    sprite('az407_07', 5)	# 117-121
    sprite('az407_08', 5)	# 122-126
    sprite('az407_09', 5)	# 127-131
    tag_voice(0, 'baz208_0', 'baz208_1', 'baz208_2', '')
    GuardPoint_(0)
    if (not CheckInput(0x1)):
        enterState('Baigaeshi')
    sprite('az407_10', 5)	# 132-136
    sprite('az407_02', 3)	# 137-139
    sprite('az407_01', 3)	# 140-142
    gotoLabel(2)
    label(1)
    clearUponHandler(23)
    sprite('az407_02', 4)	# 143-146
    setInvincible(0)
    Unknown7015()
    sprite('az407_01', 3)	# 147-149
    sprite('az407_01', 1)	# 150-150
    gotoLabel(2)
    label(2)
    sprite('az407_00', 3)	# 151-153

@State
def Baigaeshi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        (SLOT_4 > 1)
        if Unknown30068(1):
            HitCancel('BoostDash')
        setInvincible(1)
        Unknown22019('0100000001000000010000000100000001000000')
    sprite('az408_00', 2)	# 1-2
    sprite('az408_01', 2)	# 3-4
    sprite('az408_02', 3)	# 5-7
    SFX_3('azse_04')
    tag_voice(0, 'baz209_0', 'baz209_1', 'baz209_2', '')
    GFX_0('408sphereStart', -1)
    GFX_0('408sphere', -1)
    if (SLOT_59 >= 1):
        Unknown38(6, 1)
        Unknown23029(6, 4081, 0)
        SLOT_59 = (SLOT_59 + (-1))
    if Unknown23145('ShotAtemi'):
        Unknown23029(6, 4089, 0)
    if Unknown23145('CmnActChangePartnerAssistAtk_B'):
        Unknown23029(6, 4082, 0)
    sprite('az408_03', 3)	# 8-10
    sprite('az408_04', 3)	# 11-13
    sprite('az408_05', 3)	# 14-16
    sprite('az408_06', 3)	# 17-19
    sprite('az408_07', 3)	# 20-22
    sprite('az408_08', 2)	# 23-24
    sprite('az408_09', 2)	# 25-26

@State
def Shinkyaku():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(600)
        if (SLOT_4 > 1):
            HitCancel('BoostDash')
    sprite('az406_00', 4)	# 1-4
    sprite('az406_01', 2)	# 5-6
    sprite('az406_02', 2)	# 7-8
    sprite('az406_03', 2)	# 9-10
    sprite('az406_04', 4)	# 11-14
    sprite('az406_05', 32767)	# 15-32781
    Unknown8001(1, 0)
    physicsXImpulse(12000)
    physicsYImpulse(30000)
    setGravity(2800)

    def upon_4():
        clearUponHandler(4)
        sendToLabel(0)
    loopRest()
    label(0)
    sprite('az406_06', 2)	# 32782-32783
    Unknown1039(200)
    Unknown7007('62617a3230365f3000000000000000006400000062617a3230365f3100000000000000006400000062617a3230365f320000000000000000640000000000000000000000000000000000000000000000')

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(9)
    sprite('az406_07', 2)	# 32784-32785
    sprite('az406_08', 2)	# 32786-32787
    sprite('az406_09', 32767)	# 32788-65554
    Unknown1039(400)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(9)
    loopRest()
    label(9)
    sprite('az406_10', 2)	# 65555-65556
    SFX_3('azse_07')
    Unknown1084(1)
    Unknown18009(1)
    GFX_0('az406_dummy', -1)
    GFX_0('rocktest', -1)
    sprite('az406_11', 2)	# 65557-65558
    sprite('az406_12', 4)	# 65559-65562
    sprite('az406_13', 4)	# 65563-65566
    sprite('az406_14', 2)	# 65567-65568

@State
def VanishingAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1900)
        AttackP1(80)
        AirPushbackX(60000)
        AirPushbackY(15000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(60)
        HitOverhead(2)
        Unknown30065(0)
        Unknown11091(10)
        callSubroutine('WeakPointAttack_Pre')
        SLOT_53 = SLOT_6
        SLOT_6 = 8

        def upon_78():
            clearUponHandler(78)
            SFX_0('025_cleanhit_grap')
            if 
            if (not (SLOT_2 == 1)):
                if (not op(6, 2, 4, 2, 5)):
                    callSubroutine('WeakPointAttack_Judge'):
                AttackLevel_(5)
                Damage(2090)
                AirHitstunAnimation(12)
                GroundedHitstunAnimation(12)
                Unknown9178(1)
                Unknown9346(1)
                Unknown9362(1)
                Unknown9364(30)
                AirHitstunAfterWallbounce(30)
                AirPushbackX(35000)
                AirPushbackY(1000)
                YImpluseBeforeWallbounce(20)
                HitCancel('BoostDashStart')
                SFX_3('azse_05')
                Hitstop(20)
                ScreenShake(32000, 32000)
                GFX_0('weakhit00', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                SLOT_60 = 1
                SLOT_6 = SLOT_53
                callSubroutine('WeakPointAttack_Success')
            else:
                ScreenShake(4000, 4000)
                SFX_3('azse_01')
                SLOT_6 = SLOT_53

        def upon_25():
            clearUponHandler(25)
            SLOT_58 = 1
    sprite('az404_00', 3)	# 1-3
    sprite('az404_00', 1)	# 4-4
    Unknown7007('62617a3230355f3000000000000000006400000062617a3230355f3100000000000000006400000062617a3230355f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('404tame', -1)
    SFX_3('azse_11')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('az404_01', 3)	# 5-7
    sprite('az404_02', 3)	# 8-10
    sprite('az404_03', 3)	# 11-13
    setInvincible(1)
    Unknown22019('0100000001000000010000000100000000000000')
    GuardPoint_(1)
    Unknown22030(0)
    Unknown22031(-2, -1)
    sprite('az404_01', 2)	# 14-15
    sprite('az404_01', 1)	# 16-16
    if SLOT_58:
        sendToLabel(0)
    clearUponHandler(25)
    sendToLabelUpon(25, 0)
    loopRest()
    sprite('az404_03', 3)	# 17-19
    sprite('az404_01', 3)	# 20-22
    SFX_3('azse_11')
    sprite('az404_02', 3)	# 23-25
    sprite('az404_03', 3)	# 26-28
    sprite('az404_01', 3)	# 29-31
    sprite('az404_02', 3)	# 32-34
    sprite('az404_03', 3)	# 35-37
    sprite('az404_01', 3)	# 38-40
    sprite('az404_02', 3)	# 41-43
    SFX_3('azse_11')
    sprite('az404_03', 2)	# 44-45
    sprite('az404_03', 1)	# 46-46
    Unknown2037(1)
    Unknown23159('VanishingAttack_Tame')
    label(0)
    sprite('az404_01', 1)	# 47-47
    clearUponHandler(25)
    sprite('az404_04', 3)	# 48-50
    Unknown21015('34303474616d6500000000000000000000000000000000000000000000000000c90f000000000000')
    sprite('az404_05', 3)	# 51-53
    SFX_3('azse_14')
    GFX_0('404swing', -1)
    GFX_0('404nigiyakasi', -1)
    setInvincible(0)
    sprite('az404_06', 1)	# 54-54	 **attackbox here**
    physicsXImpulse(60000)
    sprite('az404_06', 2)	# 55-56	 **attackbox here**
    sprite('az404_07', 3)	# 57-59	 **attackbox here**
    Unknown1019(80)
    sprite('az404_08', 3)	# 60-62	 **attackbox here**
    Unknown1019(60)
    sprite('az404_09', 5)	# 63-67
    Unknown1019(40)
    sprite('az404_10', 5)	# 68-72
    Unknown1019(30)
    sprite('az404_11', 4)	# 73-76
    Unknown1019(30)
    sprite('az404_12', 4)	# 77-80
    physicsXImpulse(0)
    sprite('az404_13', 4)	# 81-84
    sprite('az404_14', 4)	# 85-88
    sprite('az404_15', 4)	# 89-92
    sprite('az404_16', 4)	# 93-96
    sprite('az404_17', 4)	# 97-100

@State
def BoostDashStart():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown23027()
        if (not SLOT_4):
            if SLOT_60:
                SLOT_4 = 90
    sprite('az035_00', 1)	# 1-1
    enterState('BoostDash')

@State
def BoostDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown23027()
        Unknown1045(75000)
        setGravity(300)

        def upon_55():
            SLOT_51 = (SLOT_51 + 1)

        def upon_3():
            if (SLOT_51 >= 30):
                clearUponHandler(55)
                clearUponHandler(3)
                sendToLabel(0)
    sprite('az035_00', 1)	# 1-1
    Unknown23123(16711935, 10)
    sprite('az035_01', 2)	# 2-3
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')
    Unknown8007(100, 1, 1)
    sprite('az035_02', 2)	# 4-5
    physicsXImpulse(38000)
    Unknown8009(0)
    Unknown8006(100, 1, 0)
    Unknown1017()
    Unknown13014(1)
    Unknown13015(1)
    sprite('az035_01', 2)	# 6-7
    sprite('az035_02', 2)	# 8-9
    sprite('az035_03', 2)	# 10-11
    sprite('az035_01', 2)	# 12-13
    sprite('az035_02', 2)	# 14-15
    sprite('az035_03', 2)	# 16-17
    sprite('az035_01', 2)	# 18-19
    sprite('az035_02', 2)	# 20-21
    sprite('az035_03', 2)	# 22-23
    sprite('az035_01', 2)	# 24-25
    sprite('az035_02', 2)	# 26-27
    sprite('az035_03', 2)	# 28-29
    sprite('az035_01', 2)	# 30-31
    sprite('az035_02', 2)	# 32-33
    sprite('az035_03', 2)	# 34-35
    sprite('az035_01', 2)	# 36-37
    sprite('az035_02', 2)	# 38-39
    sprite('az035_03', 2)	# 40-41
    sprite('az035_01', 2)	# 42-43
    sprite('az035_02', 2)	# 44-45
    sprite('az035_03', 2)	# 46-47
    sprite('az035_01', 2)	# 48-49
    sprite('az035_02', 2)	# 50-51
    sprite('az035_03', 2)	# 52-53
    sprite('az035_01', 2)	# 54-55
    sprite('az035_02', 2)	# 56-57
    sprite('az035_03', 2)	# 58-59
    sprite('az035_01', 2)	# 60-61
    sprite('az035_02', 2)	# 62-63
    sprite('az035_03', 2)	# 64-65
    sprite('az035_01', 2)	# 66-67
    sprite('az035_02', 2)	# 68-69
    sprite('az035_03', 2)	# 70-71
    sprite('az035_01', 2)	# 72-73
    sprite('az035_02', 2)	# 74-75
    sprite('az035_03', 2)	# 76-77
    sprite('az035_01', 2)	# 78-79
    sprite('az035_02', 2)	# 80-81
    sprite('az035_03', 2)	# 82-83
    sprite('az035_01', 2)	# 84-85
    sprite('az035_02', 2)	# 86-87
    sprite('az035_03', 2)	# 88-89
    sprite('az035_01', 2)	# 90-91
    sprite('az035_02', 2)	# 92-93
    sprite('az035_03', 2)	# 94-95
    sprite('az035_01', 2)	# 96-97
    Unknown1019(70)
    sprite('az035_02', 2)	# 98-99
    sprite('az035_03', 2)	# 100-101
    label(0)

@State
def DustAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1900)
        AttackP1(90)
        AirPushbackX(6000)
        AirPushbackY(27000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown30065(0)
        Unknown11091(10)
        callSubroutine('WeakPointAttack_Pre')
        SLOT_53 = SLOT_6
        SLOT_6 = 8

        def upon_78():
            SFX_0('025_cleanhit_grap')
            clearUponHandler(78)
            if 
            if (not (SLOT_2 == 1)):
                if (not op(6, 2, 4, 2, 5)):
                    callSubroutine('WeakPointAttack_Judge'):
                AttackLevel_(5)
                Damage(2090)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(65)
                AirPushbackX(5000)
                AirPushbackY(40000)
                YImpluseBeforeWallbounce(750)
                SFX_3('azse_05')
                HitCancel('HomingJump')
                Hitstop(20)
                ScreenShake(32000, 32000)
                GFX_0('weakhit01', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                SLOT_6 = SLOT_53
                callSubroutine('WeakPointAttack_Success')
            else:
                ScreenShake(8000, 8000)
                SFX_3('azse_01')
                SLOT_6 = SLOT_53

        def upon_25():
            clearUponHandler(25)
            SLOT_58 = 1
    sprite('az403_00', 3)	# 1-3
    sprite('az403_01', 3)	# 4-6
    Unknown7007('62617a3230345f3000000000000000006400000062617a3230345f3100000000000000006400000062617a3230345f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    Unknown2058(-5000)
    GFX_0('azef_dustattack_hold', -1)
    sprite('az403_02', 2)	# 7-8
    SFX_3('azse_03_loop')
    sprite('az403_03', 2)	# 9-10
    setInvincible(1)
    Unknown22019('0100000001000000010000000100000000000000')
    Unknown22030(0)
    GuardPoint_(1)
    Unknown22031(-2, -1)
    sprite('az403_04', 1)	# 11-11
    sprite('az403_04', 1)	# 12-12
    if SLOT_58:
        sendToLabel(0)
    clearUponHandler(25)
    sendToLabelUpon(25, 0)
    sprite('az403_02', 3)	# 13-15
    sprite('az403_03', 3)	# 16-18
    sprite('az403_04', 3)	# 19-21
    sprite('az403_02', 3)	# 22-24
    sprite('az403_03', 3)	# 25-27
    sprite('az403_04', 3)	# 28-30
    sprite('az403_02', 3)	# 31-33
    sprite('az403_03', 3)	# 34-36
    SFX_3('azse_03_loop')
    sprite('az403_04', 3)	# 37-39
    sprite('az403_02', 2)	# 40-41
    sprite('az403_02', 1)	# 42-42
    Unknown2037(1)
    label(0)
    clearUponHandler(25)
    sprite('az403_05', 3)	# 43-45
    Unknown26('azef_dustattack_hold')
    sprite('az403_06', 3)	# 46-48
    setInvincible(0)
    sprite('az403_07', 3)	# 49-51
    physicsXImpulse(40000)
    sprite('az403_08', 2)	# 52-53	 **attackbox here**
    StartMultihit()
    GFX_0('403swing', -1)
    SFX_3('azse_14')
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    sprite('az403_09', 1)	# 54-54	 **attackbox here**
    Unknown1019(20)
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    sprite('az403_09', 4)	# 55-58	 **attackbox here**
    sprite('az403_10', 3)	# 59-61	 **attackbox here**
    physicsXImpulse(0)
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    sprite('az403_11', 3)	# 62-64
    sprite('az403_12', 3)	# 65-67
    sprite('az403_11', 3)	# 68-70
    sprite('az403_12', 3)	# 71-73
    sprite('az403_13', 3)	# 74-76
    sprite('az403_14', 3)	# 77-79
    sprite('az403_15', 3)	# 80-82
    sprite('az403_16', 3)	# 83-85

@State
def HomingJump():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown23027()
        Unknown28(2, 'CmnActJumpLanding')
        callSubroutine('HomingCancel')
        SLOT_5 = 60

        def upon_49():
            SLOT_5 = 0
    sprite('az023_00', 2)	# 1-2
    Unknown23123(16711935, 10)
    Unknown13019(1)
    sprite('az023_01', 4)	# 3-6
    sprite('az020_00', 2)	# 7-8
    sprite('az020_01', 1)	# 9-9
    physicsXImpulse(10000)
    physicsYImpulse(40000)
    setGravity(850)
    SLOT_67 = SLOT_20
    if (SLOT_67 > 420000):
        physicsYImpulse(44000)
    SLOT_67 = SLOT_20
    if (SLOT_67 > 450000):
        physicsYImpulse(48000)
    SLOT_68 = SLOT_19
    if (SLOT_68 > 380000):
        physicsXImpulse(12000)
    WhiffCancel('NmlAtkAIR5A')
    WhiffCancel('NmlAtkAIR5B')
    WhiffCancel('NmlAtkAIR5C')
    WhiffCancelEnable(1)
    Unknown8001(100, 1)
    sprite('az020_01', 1)	# 10-10
    Unknown13014(1)
    Unknown13015(1)
    Unknown13026(1)
    Unknown13010(1)
    Unknown13011(1)
    Unknown13012(1)
    sprite('az020_02', 4)	# 11-14
    sprite('az020_03', 4)	# 15-18
    sprite('az020_04', 20)	# 19-38
    sprite('az020_05', 4)	# 39-42
    sprite('az020_06', 4)	# 43-46
    sprite('az020_07', 3)	# 47-49
    sprite('az020_08', 3)	# 50-52
    sprite('az020_07', 3)	# 53-55
    sprite('az020_08', 3)	# 56-58
    sprite('az020_07', 3)	# 59-61
    sprite('az020_08', 3)	# 62-64
    sprite('az020_07', 3)	# 65-67
    sprite('az020_08', 3)	# 68-70
    sprite('az020_07', 3)	# 71-73
    sprite('az020_08', 3)	# 74-76
    sprite('az020_07', 3)	# 77-79
    sprite('az020_08', 3)	# 80-82
    sprite('az020_07', 3)	# 83-85
    sprite('az020_08', 3)	# 86-88
    sprite('az020_07', 3)	# 89-91
    sprite('az020_08', 3)	# 92-94
    sprite('az020_07', 3)	# 95-97
    sprite('az020_08', 3)	# 98-100
    sprite('az020_07', 3)	# 101-103
    sprite('az020_08', 3)	# 104-106
    sprite('az020_07', 3)	# 107-109
    sprite('az020_08', 3)	# 110-112
    sprite('az020_07', 3)	# 113-115
    sprite('az020_08', 3)	# 116-118
    sprite('az020_07', 3)	# 119-121
    sprite('az020_08', 3)	# 122-124
    sprite('az020_07', 3)	# 125-127
    sprite('az020_08', 3)	# 128-130
    sprite('az020_07', 3)	# 131-133
    sprite('az020_08', 3)	# 134-136
    sprite('az020_07', 3)	# 137-139
    sprite('az020_08', 3)	# 140-142

@State
def SuperPunch():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(5500)
        Hitstop(20)
        AirPushbackX(54000)
        AirPushbackY(22000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        PushbackX(60800)
        Unknown11050('04000000617a65665f3433316869745f6c696e6500000000000000000000000000000000')
        Unknown11091(33)
        Unknown11056(0)

        def upon_12():
            HitAirUnblockable(4)
            HitOverhead(4)
            HitLow(4)
            if SLOT_31:
                GFX_0('weakhit00', -1)
            if SLOT_32:
                GFX_0('weakhit01', -1)
        if SLOT_31:
            HitAirUnblockable(3)
            HitLow(2)
        if SLOT_32:
            HitAirUnblockable(3)
            HitOverhead(2)
    sprite('az431_00', 3)	# 1-3
    setInvincible(1)
    GuardPoint_(1)
    tag_voice(1, 'baz250_0', 'baz250_1', '', '')
    sprite('az431_00', 3)	# 4-6
    sprite('az431_01', 6)	# 7-12
    Unknown2036(122, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    teleportRelativeX(-70000)
    Unknown3029(1)
    sprite('az431_02', 6)	# 13-18
    teleportRelativeX(-40000)
    sprite('az431_03', 6)	# 19-24
    teleportRelativeX(-40000)
    sprite('az431_04', 6)	# 25-30
    teleportRelativeX(-70000)
    sprite('az431_05', 6)	# 31-36
    teleportRelativeX(-70000)
    sprite('az431_06', 5)	# 37-41
    sprite('az431_07', 5)	# 42-46
    sprite('az431_08', 5)	# 47-51
    sprite('az431_09', 5)	# 52-56
    sprite('az431_10', 3)	# 57-59
    sprite('az431_11', 3)	# 60-62
    sprite('az431_12', 3)	# 63-65
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 66-68
    sprite('az431_11', 3)	# 69-71
    sprite('az431_12', 3)	# 72-74
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 75-77
    sprite('az431_11', 3)	# 78-80
    sprite('az431_12', 3)	# 81-83
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 84-86
    sprite('az431_11', 3)	# 87-89
    sprite('az431_12', 3)	# 90-92
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 93-95
    sprite('az431_11', 3)	# 96-98
    sprite('az431_12', 3)	# 99-101
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 102-104
    sprite('az431_11', 3)	# 105-107
    sprite('az431_12', 3)	# 108-110
    sprite('az431_13', 4)	# 111-114
    sprite('az431_14', 4)	# 115-118
    sprite('az431_15', 4)	# 119-122
    GFX_0('402rock1', -1)
    GFX_0('405smoke', -1)
    teleportRelativeX(10000)
    sprite('az431_16', 4)	# 123-126
    teleportRelativeX(10000)
    SFX_3('azse_06')
    sprite('az431_17', 3)	# 127-129
    tag_voice(0, 'baz251_0', 'baz251_1', '', '')
    teleportRelativeX(80000)
    SLOT_12 = SLOT_19
    Unknown1019(9)
    if (SLOT_12 <= 10000):
        SLOT_12 = 10000
    sprite('az431_18', 3)	# 130-132
    teleportRelativeX(20000)
    sprite('az431_19', 3)	# 133-135	 **attackbox here**
    Unknown26('405smoke')
    GFX_0('431swing', -1)
    Unknown1019(70)

    def upon_12():
        SFX_0('025_cleanhit_grap')
        SFX_0('025_cleanhit_grap')
    sprite('az431_20', 6)	# 136-141
    setInvincible(0)
    Unknown1019(20)
    sprite('az431_21', 6)	# 142-147
    physicsXImpulse(0)
    sprite('az431_22', 6)	# 148-153
    sprite('az431_23', 6)	# 154-159
    sprite('az431_24', 6)	# 160-165
    sprite('az431_25', 6)	# 166-171
    sprite('az431_26', 6)	# 172-177
    sprite('az431_27', 6)	# 178-183
    sprite('az431_28', 6)	# 184-189

@State
def SuperPunch_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(6500)
        Hitstop(20)
        AirPushbackX(80000)
        AirPushbackY(22000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        PushbackX(60800)
        Unknown9202(40)
        Unknown11050('04000000617a65665f3433316869745f6c696e6500000000000000000000000000000000')
        Unknown11091(31)
        Unknown11056(0)

        def upon_12():
            HitAirUnblockable(4)
            HitOverhead(4)
            HitLow(4)
            if SLOT_31:
                GFX_0('weakhit00', -1)
            if SLOT_32:
                GFX_0('weakhit01', -1)
        if SLOT_31:
            HitAirUnblockable(3)
            HitLow(2)
        if SLOT_32:
            HitAirUnblockable(3)
            HitOverhead(2)
    sprite('az431_00', 3)	# 1-3
    tag_voice(1, 'baz250_0', 'baz250_1', '', '')
    setInvincible(1)
    GuardPoint_(1)
    sprite('az431_00', 3)	# 4-6
    sprite('az431_01', 6)	# 7-12
    Unknown2036(149, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    teleportRelativeX(-70000)
    Unknown3029(1)
    sprite('az431_02', 6)	# 13-18
    teleportRelativeX(-40000)
    sprite('az431_03', 6)	# 19-24
    teleportRelativeX(-40000)
    sprite('az431_04', 6)	# 25-30
    teleportRelativeX(-70000)
    sprite('az431_05', 6)	# 31-36
    teleportRelativeX(-70000)
    sprite('az431_06', 5)	# 37-41
    sprite('az431_07', 5)	# 42-46
    sprite('az431_08', 5)	# 47-51
    sprite('az431_09', 5)	# 52-56
    GFX_0('431ODAura', -1)
    Unknown23119(-922799616, 54, 2)
    sprite('az431_10', 3)	# 57-59
    sprite('az431_11', 3)	# 60-62
    sprite('az431_12', 3)	# 63-65
    ScreenShake(4000, 0)
    SFX_0('019_quake_1')
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 66-68
    sprite('az431_11', 3)	# 69-71
    sprite('az431_12', 3)	# 72-74
    ScreenShake(6000, 0)
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 75-77
    sprite('az431_11', 3)	# 78-80
    sprite('az431_12', 3)	# 81-83
    ScreenShake(8000, 0)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 84-86
    sprite('az431_11', 3)	# 87-89
    sprite('az431_12', 3)	# 90-92
    ScreenShake(12000, 0)
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 93-95
    sprite('az431_11', 3)	# 96-98
    sprite('az431_12', 3)	# 99-101
    ScreenShake(12000, 0)
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 102-104
    sprite('az431_11', 3)	# 105-107
    sprite('az431_12', 3)	# 108-110
    ScreenShake(15000, 0)
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 111-113
    sprite('az431_11', 3)	# 114-116
    sprite('az431_12', 3)	# 117-119
    ScreenShake(18000, 0)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('az431_10', 3)	# 120-122
    sprite('az431_11', 3)	# 123-125
    sprite('az431_12', 3)	# 126-128
    ScreenShake(21000, 0)
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 129-131
    sprite('az431_11', 3)	# 132-134
    sprite('az431_12', 3)	# 135-137
    ScreenShake(25000, 0)
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    Unknown21015('3433314f44417572610000000000000000000000000000000000000000000000d710000000000000')
    sprite('az431_13', 4)	# 138-141
    sprite('az431_14', 4)	# 142-145
    sprite('az431_15', 4)	# 146-149
    GFX_0('402rock1', -1)
    GFX_0('405smoke', -1)
    teleportRelativeX(10000)
    sprite('az431_16', 4)	# 150-153
    teleportRelativeX(10000)
    SFX_3('azse_06')
    sprite('az431_17', 3)	# 154-156
    tag_voice(0, 'baz251_0', 'baz251_1', '', '')
    teleportRelativeX(80000)
    SLOT_12 = SLOT_19
    Unknown1019(9)
    if (SLOT_12 <= 10000):
        SLOT_12 = 10000
    sprite('az431_18', 3)	# 157-159
    teleportRelativeX(20000)
    sprite('az431_19', 3)	# 160-162	 **attackbox here**
    Unknown26('405smoke')
    GFX_0('431swing', -1)
    Unknown1019(70)

    def upon_12():
        SFX_0('025_cleanhit_grap')
        SFX_0('025_cleanhit_grap')
    sprite('az431_20', 6)	# 163-168
    setInvincible(0)
    Unknown1019(20)
    sprite('az431_21', 6)	# 169-174
    physicsXImpulse(0)
    sprite('az431_22', 6)	# 175-180
    sprite('az431_23', 6)	# 181-186
    sprite('az431_24', 6)	# 187-192
    sprite('az431_25', 6)	# 193-198
    sprite('az431_26', 6)	# 199-204
    sprite('az431_27', 6)	# 205-210
    sprite('az431_28', 6)	# 211-216

@State
def Spartan():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1500)
        AttackP2(95)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(60)
        Unknown9142(60)
        Unknown11072(1, 250000, 0)
        Unknown11028(26)
        Hitstop(20)
        Unknown11091(15)
        setInvincible(1)
        Unknown1084(1)
        Unknown13024(0)
        Unknown11064(1)
        Unknown11069('SpartanExe')
        Unknown2073(1)

        def upon_78():
            enterState('SpartanExe')

        def upon_61():
            PushbackX(39900)

        def upon_11():
            ScreenShake(10000, 50000)
    sprite('az300_01', 6)	# 1-6
    sprite('az300_02', 7)	# 7-13
    Unknown2036(77, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('az300_03', 4)	# 14-17
    SFX_3('azse_12')
    sprite('az300_04', 4)	# 18-21	 **attackbox here**
    StartMultihit()
    sprite('az300_05', 4)	# 22-25
    sprite('az300_06', 4)	# 26-29
    sprite('az300_07', 26)	# 30-55
    sprite('az300_03', 7)	# 56-62
    sprite('az300_02', 7)	# 63-69
    tag_voice(1, 'baz280_0', 'baz280_1', '', '')
    sprite('az440_01', 6)	# 70-75
    sprite('az440_02', 6)	# 76-81
    sprite('az440_03', 3)	# 82-84
    SFX_0('005_swing_grap_2_2')
    SFX_0('005_swing_grap_2_2')
    sprite('az440_04', 5)	# 85-89	 **attackbox here**
    sprite('az440_04', 3)	# 90-92	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Unknown13024(1)
    sprite('az440_05', 7)	# 93-99
    sprite('az440_06', 7)	# 100-106
    sprite('az440_07', 7)	# 107-113
    sprite('az440_08', 5)	# 114-118
    sprite('az440_09', 5)	# 119-123
    sprite('az313_09ex01', 5)	# 124-128
    sprite('az313_10ex01', 5)	# 129-133

@State
def SpartanExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(1800)
        AttackP2(95)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(5000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown9178(1)
        WallbounceReboundTime(5)
        Unknown9310(10)
        Unknown11023(1)
        Unknown11091(16)
        Unknown13024(0)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11108('03000000')
        setInvincible(1)
        Unknown11069('SpartanExe')
        Unknown2004(1, 0)
        Unknown2015(300)
    sprite('az440_04', 2)	# 1-2	 **attackbox here**
    Unknown3029(1)
    Unknown20000(1)
    Unknown20003(1)
    StartMultihit()
    sprite('az440_05', 3)	# 3-5
    sprite('az440_06', 3)	# 6-8
    sprite('az440_07', 3)	# 9-11
    sprite('az440_08', 3)	# 12-14
    sprite('az440_09', 3)	# 15-17
    sprite('az401_00ex01', 6)	# 18-23
    physicsXImpulse(25000)
    sprite('az401_01ex01', 2)	# 24-25
    Unknown1019(30)
    SFX_0('005_swing_grap_2_2')
    sprite('az401_02ex01', 2)	# 26-27
    Unknown1019(30)
    tag_voice(0, 'baz281_0', 'baz281_1', '', '')
    sprite('az401_03ex01', 3)	# 28-30	 **attackbox here**
    GFX_0('BrustDD_SlashEff', -1)
    physicsXImpulse(0)

    def upon_11():
        ScreenShake(5000, 50000)
    sprite('az401_04ex01', 4)	# 31-34
    sprite('az401_05ex01', 4)	# 35-38
    sprite('az401_06ex01', 4)	# 39-42
    sprite('az401_07ex01', 4)	# 43-46
    sprite('az401_08ex01', 4)	# 47-50
    sprite('az400_01ex01', 3)	# 51-53
    physicsXImpulse(20000)
    GFX_0('BrustDD_SlashEff2', -1)
    sprite('az400_02ex01', 4)	# 54-57
    Unknown1019(80)
    sprite('az400_03ex01', 2)	# 58-59
    Unknown1019(50)
    sprite('az400_04ex01', 3)	# 60-62	 **attackbox here**
    physicsXImpulse(0)
    RefreshMultihit()
    AttackLevel_(5)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(20000)
    AirPushbackY(60000)
    Unknown20000(0)
    Unknown20007(1)
    Unknown2015(1)
    SFX_3('azse_02')
    sprite('az400_05ex01', 3)	# 63-65
    sprite('az400_06ex01', 3)	# 66-68
    sprite('az400_07ex01', 3)	# 69-71
    sprite('az440_10', 5)	# 72-76
    Unknown3004(-51)
    sprite('az440_11', 5)	# 77-81
    Unknown3029(0)
    Unknown20007(0)
    Unknown20000(1)
    Unknown1086(22)
    teleportRelativeX(800000)
    Unknown3004(51)
    setGravity(100)
    sprite('az440_11', 3)	# 82-84
    Unknown3029(1)
    Unknown3001(255)
    Unknown3004(0)
    sprite('az440_12', 3)	# 85-87
    sprite('az440_13', 10)	# 88-97
    sprite('az440_14', 2)	# 98-99
    GFX_0('BrustDD_SlashEff3', -1)
    SFX_0('016_explode_2')
    sprite('az440_15', 2)	# 100-101
    physicsXImpulse(-30000)
    sprite('az440_16', 1)	# 102-102
    Unknown1019(25)
    sprite('az440_17', 3)	# 103-105	 **attackbox here**
    Unknown1084(1)
    Unknown20000(0)
    Unknown20003(0)
    Unknown2015(-1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(4000)
    AttackP2(70)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(100000)
    AirPushbackY(1000)
    YImpluseBeforeWallbounce(10)
    Hitstop(30)
    WallbounceReboundTime(1)
    AirUntechableTime(360)
    Unknown9310(1)
    Unknown11064(0)
    Unknown11069('')
    Unknown11091(33)
    Unknown13024(1)

    def upon_11():
        ScreenShake(10000, 100000)
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    sprite('az440_18', 3)	# 106-108
    Unknown2034(1)
    Unknown2053(1)
    physicsYImpulse(1000)
    sprite('az440_19', 3)	# 109-111
    sprite('az440_18', 3)	# 112-114
    sprite('az440_19', 3)	# 115-117
    sprite('az440_18', 3)	# 118-120
    sprite('az440_19', 3)	# 121-123
    sprite('az440_18', 3)	# 124-126
    sprite('az440_19', 3)	# 127-129
    sprite('az440_20', 3)	# 130-132
    sprite('az440_21', 3)	# 133-135
    loopRest()
    sprite('az020_00', 3)	# 136-138
    Unknown2006()
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    if (SLOT_23 <= 10000):
        SLOT_23 = 10000
    physicsYImpulse(20000)
    Unknown1043()
    Unknown1039(150)
    sprite('az020_01', 3)	# 139-141
    sprite('az020_02', 3)	# 142-144
    sprite('az020_03', 3)	# 145-147
    sprite('az020_04', 4)	# 148-151
    sprite('az020_05', 4)	# 152-155
    sprite('az020_06', 4)	# 156-159
    sprite('az020_07', 3)	# 160-162
    sprite('az020_08', 3)	# 163-165
    loopRest()
    label(101)
    sprite('az020_07', 3)	# 166-168
    sprite('az020_08', 3)	# 169-171
    loopRest()
    gotoLabel(101)
    label(9)
    sprite('az024_00', 4)	# 172-175
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('az024_01', 3)	# 176-178
    sprite('az024_02', 3)	# 179-181
    sprite('az024_03', 3)	# 182-184
    sprite('az024_04', 3)	# 185-187

@State
def Spartan_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1500)
        AttackP2(95)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(60)
        Unknown9142(60)
        Unknown11072(1, 250000, 0)
        Unknown11028(26)
        Hitstop(20)
        Unknown11091(15)
        setInvincible(1)
        Unknown1084(1)
        Unknown13024(0)
        Unknown11064(1)
        Unknown11069('SpartanExe_OD')
        Unknown2073(1)

        def upon_78():
            enterState('SpartanExe_OD')

        def upon_61():
            PushbackX(39900)

        def upon_11():
            ScreenShake(10000, 50000)
    sprite('az300_01', 6)	# 1-6
    sprite('az300_02', 7)	# 7-13
    Unknown2036(77, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('az300_03', 4)	# 14-17
    SFX_3('azse_12')
    sprite('az300_04', 4)	# 18-21	 **attackbox here**
    StartMultihit()
    sprite('az300_05', 4)	# 22-25
    sprite('az300_06', 4)	# 26-29
    sprite('az300_07', 26)	# 30-55
    sprite('az300_03', 7)	# 56-62
    sprite('az300_02', 7)	# 63-69
    tag_voice(1, 'baz280_0', 'baz280_1', '', '')
    sprite('az440_01', 6)	# 70-75
    sprite('az440_02', 6)	# 76-81
    sprite('az440_03', 3)	# 82-84
    SFX_0('005_swing_grap_2_2')
    SFX_0('005_swing_grap_2_2')
    sprite('az440_04', 5)	# 85-89	 **attackbox here**
    sprite('az440_04', 3)	# 90-92	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Unknown13024(1)
    sprite('az440_05', 7)	# 93-99
    sprite('az440_06', 7)	# 100-106
    sprite('az440_07', 7)	# 107-113
    sprite('az440_08', 5)	# 114-118
    sprite('az440_09', 5)	# 119-123
    sprite('az313_09ex01', 5)	# 124-128
    sprite('az313_10ex01', 5)	# 129-133

@State
def SpartanExe_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(1800)
        AttackP2(95)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(5000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown9178(1)
        WallbounceReboundTime(5)
        Unknown9310(10)
        Unknown11023(1)
        Unknown11091(13)
        Unknown13024(0)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11064(1)
        setInvincible(1)
        Unknown11069('SpartanExe_OD')
        Unknown2004(1, 0)
        Unknown2015(300)
    sprite('az440_04', 2)	# 1-2	 **attackbox here**
    Unknown3029(1)
    Unknown20000(1)
    Unknown20003(1)
    StartMultihit()
    sprite('az440_05', 3)	# 3-5
    sprite('az440_06', 3)	# 6-8
    sprite('az440_07', 3)	# 9-11
    sprite('az440_08', 3)	# 12-14
    sprite('az440_09', 3)	# 15-17
    sprite('az401_00ex01', 6)	# 18-23
    physicsXImpulse(25000)
    Unknown23119(-922799616, 12, 1)
    GFX_0('440Aura', -1)
    sprite('az401_01ex01', 2)	# 24-25
    Unknown1019(30)
    SFX_0('005_swing_grap_2_2')
    sprite('az401_02ex01', 2)	# 26-27
    tag_voice(0, 'baz282_0', 'baz282_1', '', '')
    Unknown1019(30)
    sprite('az401_03ex01', 3)	# 28-30	 **attackbox here**
    GFX_0('BrustDD_SlashEffEx', -1)
    physicsXImpulse(0)
    SFX_3('azse_02')
    SFX_3('azse_07')

    def upon_11():
        ScreenShake(5000, 50000)
    sprite('az401_04ex01', 4)	# 31-34
    sprite('az401_05ex01', 4)	# 35-38
    sprite('az401_06ex01', 4)	# 39-42
    sprite('az401_07ex01', 4)	# 43-46
    sprite('az401_08ex01', 4)	# 47-50
    sprite('az400_01ex01', 3)	# 51-53
    physicsXImpulse(20000)
    GFX_0('BrustDD_SlashEff2Ex', -1)
    sprite('az400_02ex01', 4)	# 54-57
    Unknown1019(80)
    sprite('az400_03ex01', 2)	# 58-59
    Unknown1019(50)
    sprite('az400_04ex01', 3)	# 60-62	 **attackbox here**
    physicsXImpulse(0)
    RefreshMultihit()
    AttackLevel_(5)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(15000)
    AirPushbackY(68000)
    Unknown20000(0)
    Unknown20007(1)
    Unknown2015(1)
    SFX_3('azse_02')
    SFX_3('azse_07')
    sprite('az400_05ex01', 3)	# 63-65
    sprite('az400_06ex01', 3)	# 66-68
    sprite('az400_07ex01', 3)	# 69-71
    sprite('az440_10', 5)	# 72-76
    Unknown3004(-51)
    sprite('az440_11', 5)	# 77-81
    Unknown3029(0)
    Unknown20007(0)
    Unknown20000(1)
    Unknown1086(22)
    teleportRelativeX(800000)
    Unknown3004(51)
    setGravity(100)
    Unknown20009(900)
    sprite('az440_11', 3)	# 82-84
    Unknown3029(1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown23119(-922799616, 12, 1)
    Unknown20009(900)
    sprite('az440_12', 3)	# 85-87
    ScreenShake(1000, 5000)
    SFX_0('019_quake_1')
    sprite('az440_13', 3)	# 88-90
    ScreenShake(1000, 5000)
    sprite('az440_13', 3)	# 91-93
    ScreenShake(1000, 5000)
    sprite('az440_13', 3)	# 94-96
    ScreenShake(1000, 5000)
    sprite('az440_13', 3)	# 97-99
    ScreenShake(1000, 5000)
    sprite('az440_13', 3)	# 100-102
    ScreenShake(1000, 5000)
    sprite('az440_13', 3)	# 103-105
    ScreenShake(1000, 5000)
    sprite('az440_13', 4)	# 106-109
    ScreenShake(1000, 5000)
    sprite('az440_14', 2)	# 110-111
    GFX_0('BrustDD_SlashEff3Ex', -1)
    SFX_0('016_explode_2')
    sprite('az440_15', 2)	# 112-113
    physicsXImpulse(-30000)
    sprite('az440_16', 1)	# 114-114
    Unknown1019(25)
    sprite('az440_17', 3)	# 115-117	 **attackbox here**
    Unknown20000(0)
    Unknown20003(0)
    Unknown2015(-1)
    Unknown1084(1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(5800)
    AttackP2(70)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(100000)
    AirPushbackY(3000)
    YImpluseBeforeWallbounce(10)
    Hitstop(40)
    WallbounceReboundTime(1)
    AirUntechableTime(360)
    Unknown9310(1)
    Unknown11064(0)
    Unknown11091(28)
    Unknown11069('')
    Unknown13024(1)

    def upon_11():
        ScreenShake(10000, 100000)
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    sprite('az440_18', 3)	# 118-120
    Unknown2034(1)
    Unknown2053(1)
    Unknown21012('343430417572610000000000000000000000000000000000000000000000000020000000')
    Unknown20009(1000)
    physicsYImpulse(1000)
    sprite('az440_19', 3)	# 121-123
    sprite('az440_18', 3)	# 124-126
    sprite('az440_19', 3)	# 127-129
    Unknown23119(-16777216, 12, 1)
    sprite('az440_18', 3)	# 130-132
    sprite('az440_19', 3)	# 133-135
    sprite('az440_18', 3)	# 136-138
    sprite('az440_19', 3)	# 139-141
    sprite('az440_20', 3)	# 142-144
    sprite('az440_21', 3)	# 145-147
    sprite('az020_00', 3)	# 148-150
    Unknown2006()
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    if (SLOT_23 <= 10000):
        SLOT_23 = 10000
    physicsYImpulse(20000)
    Unknown1043()
    Unknown1039(150)
    sprite('az020_01', 3)	# 151-153
    sprite('az020_02', 3)	# 154-156
    sprite('az020_03', 3)	# 157-159
    sprite('az020_04', 4)	# 160-163
    sprite('az020_05', 4)	# 164-167
    sprite('az020_06', 4)	# 168-171
    sprite('az020_07', 3)	# 172-174
    sprite('az020_08', 3)	# 175-177
    loopRest()
    label(101)
    sprite('az020_07', 3)	# 178-180
    sprite('az020_08', 3)	# 181-183
    loopRest()
    gotoLabel(101)
    label(9)
    sprite('az024_00', 4)	# 184-187
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('az024_01', 3)	# 188-190
    sprite('az024_02', 3)	# 191-193
    sprite('az024_03', 3)	# 194-196
    sprite('az024_04', 3)	# 197-199

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Hitstop(3)
        Unknown11064(1)
        Damage(0)
        Unknown11091(100)
        Unknown9154(1000)
        AirUntechableTime(1000)
        Unknown9310(1000)
        Unknown11072(1, 80000, 0)
        AirPushbackX(3000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(3000)
        Unknown9015(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9130(30)
        Unknown9142(30)
        Unknown11056(0)
        Unknown2004(1, 0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown2054(1)
        Unknown11091(100)
        setInvincible(1)

        def upon_12():
            enterState('AstralHeatExe')
            Unknown23088(1, 1)
sprite('az450_00', 3)	# 1-3
GFX_0('AHaura', -1)
SFX_4('baz270')
sprite('az450_01', 3)	# 4-6
GFX_0('IrezumiRay', -1)
sprite('az450_01_a', 45)	# 7-51
Unknown2036(55, -1, 2)
Unknown23147()
Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
GFX_0('EMB_AZ_AH', -1)
sprite('az450_02', 3)	# 52-54
sprite('az450_03', 3)	# 55-57
Unknown21012('414861757261000000000000000000000000000000000000000000000000000020000000')
sprite('az450_04', 3)	# 58-60
sprite('az450_05', 3)	# 61-63
sprite('az450_06', 3)	# 64-66
sprite('az450_07', 4)	# 67-70	 **attackbox here**
SFX_3('azse_07')
SFX_3('azse_07')
SFX_3('azse_05')
GFX_0('nepparock', -1)
GFX_0('450swing', -1)
ScreenShake(25000, 0)
StartMultihit()
sprite('az450_08', 5)	# 71-75	 **attackbox here**
SFX_4('baz271')
GFX_0('450neppaMatome', -1)
ScreenShake(25000, 0)
sprite('az450_09', 5)	# 76-80	 **attackbox here**
ScreenShake(25000, 0)
sprite('az450_10', 5)	# 81-85	 **attackbox here**
ScreenShake(25000, 0)
sprite('az450_11', 5)	# 86-90	 **attackbox here**
Unknown23027()
setInvincible(0)
sprite('az450_08', 5)	# 91-95	 **attackbox here**
sprite('az450_09', 5)	# 96-100	 **attackbox here**
sprite('az450_10', 5)	# 101-105	 **attackbox here**
sprite('az450_11', 5)	# 106-110	 **attackbox here**
sprite('az450_08', 5)	# 111-115	 **attackbox here**
Unknown23027()
sprite('az450_09', 5)	# 116-120	 **attackbox here**
sprite('az450_10', 5)	# 121-125	 **attackbox here**
sprite('az450_11', 5)	# 126-130	 **attackbox here**
sprite('az450_36', 7)	# 131-137
Recovery()
sprite('az450_37', 7)	# 138-144
sprite('az450_38', 7)	# 145-151
sprite('az450_39', 6)	# 152-157
sprite('az450_40', 7)	# 158-164
sprite('az450_41', 7)	# 165-171
sprite('az450_42', 6)	# 172-177
SFX_0('004_swing_grap_1_0')
sprite('az450_43', 6)	# 178-183
sprite('az450_44', 6)	# 184-189
sprite('az450_42', 6)	# 190-195
sprite('az450_43', 6)	# 196-201
SFX_0('004_swing_grap_1_0')
sprite('az450_44', 6)	# 202-207
sprite('az450_45', 6)	# 208-213
teleportRelativeX(-68000)
endState()

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        Unknown11069('AstralHeatExe')
        Unknown23024(3)
        Unknown23088(1, 1)
        Unknown23157(1)
        SLOT_33 = 0
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)
        Unknown2017(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown23084(1)
        Unknown23027()
    sprite('az450_08', 5)	# 1-5	 **attackbox here**
    Unknown36(22)
    Unknown23015(1)
    Unknown35()
    sprite('az450_09', 5)	# 6-10	 **attackbox here**
    sprite('az450_10', 5)	# 11-15	 **attackbox here**
    sprite('az450_11', 5)	# 16-20	 **attackbox here**
    sprite('az450_08', 5)	# 21-25	 **attackbox here**
    sprite('az450_09', 5)	# 26-30	 **attackbox here**
    sprite('az450_10', 5)	# 31-35	 **attackbox here**
    sprite('az450_11', 5)	# 36-40	 **attackbox here**
    sprite('az450_12', 5)	# 41-45
    sprite('az450_13', 8)	# 46-53
    sprite('az450_14', 10)	# 54-63
    ScreenShake(25000, 0)
    Unknown36(22)
    Unknown1007(-15000)
    Unknown35()
    SFX_3('azse_08')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('az450_14', 10)	# 64-73
    sprite('az450_14', 10)	# 74-83
    sprite('az450_14', 5)	# 84-88
    sprite('az450_14', 5)	# 89-93
    ScreenShake(2000, 0)
    SFX_0('019_quake_1')
    sprite('az450_14', 5)	# 94-98
    sprite('az450_14', 5)	# 99-103
    ScreenShake(2000, 0)
    SFX_0('019_quake_1')
    sprite('az450_14', 5)	# 104-108
    sprite('az450_14', 5)	# 109-113
    SFX_4('baz272')
    ScreenShake(2000, 0)
    sprite('az450_15', 6)	# 114-119
    GFX_0('450rock', -1)
    ScreenShake(2000, 0)
    SFX_3('azse_08')
    sprite('az450_16', 5)	# 120-124
    sprite('az450_16', 5)	# 125-129
    ScreenShake(4000, 0)
    SFX_0('019_quake_1')
    SFX_0('019_quake_1')
    sprite('az450_16', 5)	# 130-134
    sprite('az450_16', 5)	# 135-139
    ScreenShake(4000, 0)
    SFX_0('019_quake_1')
    sprite('az450_16', 5)	# 140-144
    sprite('az450_16', 5)	# 145-149
    ScreenShake(4000, 0)
    SFX_0('019_quake_0')
    sprite('az450_16', 5)	# 150-154
    sprite('az450_16', 5)	# 155-159
    ScreenShake(4000, 0)
    SFX_0('019_quake_1')
    sprite('az450_16', 5)	# 160-164
    sprite('az450_16', 5)	# 165-169
    ScreenShake(4000, 0)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('az450_17', 5)	# 170-174
    sprite('az450_17', 5)	# 175-179
    ScreenShake(6000, 0)
    SFX_0('019_quake_1')
    sprite('az450_17', 5)	# 180-184
    sprite('az450_17', 5)	# 185-189
    ScreenShake(6000, 0)
    SFX_0('019_quake_1')
    sprite('az450_17', 5)	# 190-194
    sprite('az450_17', 5)	# 195-199
    ScreenShake(6000, 0)
    SFX_0('019_quake_1')
    sprite('az450_17', 5)	# 200-204
    sprite('az450_17', 5)	# 205-209
    ScreenShake(6000, 0)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('az450_18', 5)	# 210-214
    sprite('az450_18', 5)	# 215-219
    ScreenShake(8000, 0)
    SFX_0('019_quake_1')
    sprite('az450_18', 5)	# 220-224
    sprite('az450_18', 5)	# 225-229
    ScreenShake(8000, 0)
    SFX_0('019_quake_1')
    SFX_4('baz273')
    sprite('az450_18', 5)	# 230-234
    sprite('az450_18', 5)	# 235-239
    ScreenShake(10000, 0)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('az450_18', 5)	# 240-244
    sprite('az450_18', 5)	# 245-249
    ScreenShake(10000, 0)
    SFX_0('019_quake_1')
    sprite('az450_19', 5)	# 250-254
    sprite('az450_19', 5)	# 255-259
    ScreenShake(13000, 0)
    SFX_0('019_quake_1')
    sprite('az450_19', 5)	# 260-264
    sprite('az450_19', 5)	# 265-269
    ScreenShake(15000, 0)
    SFX_0('019_quake_1')
    sprite('az450_19', 5)	# 270-274
    sprite('az450_19', 5)	# 275-279
    ScreenShake(18000, 0)
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('az450_19', 5)	# 280-284
    sprite('az450_19', 5)	# 285-289
    ScreenShake(21000, 0)
    SFX_0('019_quake_1')
    sprite('az450_19', 5)	# 290-294
    sprite('az450_19', 5)	# 295-299
    ScreenShake(25000, 0)
    SFX_0('019_quake_1')
    sprite('az450_20', 8)	# 300-307
    sprite('az450_21', 8)	# 308-315
    GFX_0('450smokec', -1)
    SFX_3('azse_07')
    SFX_3('azse_07')
    sprite('az450_22', 8)	# 316-323
    Unknown36(22)
    Unknown3038(1)
    teleportRelativeY(40000000)
    setGravity(0)
    Unknown35()
    sprite('az450_23', 7)	# 324-330
    sprite('az450_24', 7)	# 331-337
    sprite('az450_25', 7)	# 338-344
    sprite('az450_26', 7)	# 345-351
    GFX_0('AHanten00', -1)
    sprite('az450_27', 15)	# 352-366
    sprite('null', 22)	# 367-388
    sprite('az450_28', 6)	# 389-394
    Unknown20010(-4075, -50, 0)
    Unknown1000(0)
    Unknown36(22)
    teleportRelativeY(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown35()
    sprite('az450_29', 6)	# 395-400
    sprite('az450_30', 6)	# 401-406
    sprite('az450_31', 6)	# 407-412
    Unknown20000(0)
    GFX_0('450Cam', -1)
    SFX_0('019_quake_1')
    sprite('az450_32', 6)	# 413-418
    GFX_0('AHshadow', -1)
    SFX_0('019_quake_0')
    Unknown2017(0)
    SFX_4('baz274')
    sprite('az450_29', 6)	# 419-424
    SFX_0('019_quake_0')
    sprite('az450_30', 6)	# 425-430
    SFX_0('019_quake_1')
    sprite('az450_31', 6)	# 431-436
    sprite('az450_32', 6)	# 437-442
    SFX_0('019_quake_1')
    sprite('az450_29', 6)	# 443-448
    SFX_0('019_quake_0')
    sprite('az450_30', 6)	# 449-454
    sprite('az450_31', 6)	# 455-460
    SFX_0('019_quake_0')
    sprite('az450_32', 6)	# 461-466
    SFX_0('019_quake_1')
    sprite('az450_29', 6)	# 467-472
    sprite('az450_30', 6)	# 473-478
    SFX_0('019_quake_1')
    sprite('az450_31', 6)	# 479-484
    SFX_0('019_quake_0')
    sprite('az450_32', 6)	# 485-490
    sprite('az450_29', 6)	# 491-496
    SFX_0('019_quake_1')
    sprite('az450_30', 6)	# 497-502
    sprite('az450_31', 6)	# 503-508
    SFX_0('019_quake_1')
    sprite('az450_32', 6)	# 509-514
    sprite('az450_29', 6)	# 515-520
    SFX_0('019_quake_1')
    sprite('az450_30', 6)	# 521-526
    sprite('az450_31', 6)	# 527-532
    SFX_0('019_quake_1')
    sprite('az450_32', 6)	# 533-538
    sprite('az450_29', 6)	# 539-544
    SFX_0('019_quake_1')
    sprite('az450_30', 6)	# 545-550
    SFX_0('019_quake_0')
    sprite('az450_31', 6)	# 551-556
    SFX_0('019_quake_1')
    sprite('az450_32', 6)	# 557-562
    sprite('az450_33', 5)	# 563-567
    sprite('az450_34', 5)	# 568-572
    sprite('az450_35', 5)	# 573-577
    sprite('az450cutin_00', 20)	# 578-597	 **attackbox here**
    ScreenShake(30000, 30000)
    Unknown20001(1)
    GFX_1('azef_cutbg', -1)
    Unknown20000(1)
    GFX_0('AHanten01', 0)
    sprite('az450cutin_00', 10)	# 598-607	 **attackbox here**
    sprite('az450cutin_00', 10)	# 608-617	 **attackbox here**
    sprite('null', 65)	# 618-682
    Unknown20010(-8000, 0, 0)
    sprite('null', 10)	# 683-692
    SFX_3('azse_09')
    SFX_3('azse_06')
    sprite('null', 100)	# 693-792
    GFX_0('az450_dummy', -1)
    sprite('null', 30)	# 793-822
    Unknown18010()
    GFX_0('AHanten02', -1)
    sprite('az450cutin_01', 32767)	# 823-33589	 **attackbox here**
    SFX_4('baz275')
    Unknown23018(1)
    GFX_0('AHSmoke', 0)
    Unknown20010(-16000, 0, 0)
    loopRest()

@Subroutine
def MouthTableInit():
    Unknown18011('baz000', 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 12337, 14179, 12641, 25392, 24887, 12337, 14179, 12641, 25392, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz501', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz505', 12643, 13875, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz521', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 12853, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz525', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz403_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz404_0', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz404_1', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz600bhz', 12643, 14177, 14179, 14177, 14179, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12593, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz600bma', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz600brg', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 12343, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 12849, 12899, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz601pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz600pce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz601pka', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz601ryn', 12643, 12641, 25392, 12854, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz600uca', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz600umi', 12643, 14689, 14691, 14689, 13923, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz601uwa', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz700bhz', 13667, 13409, 14435, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz700bma', 12643, 14177, 14179, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz700brg', 12643, 14177, 14179, 14177, 14435, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz701pak', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz700pce', 13667, 13409, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 13367, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz700pka', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz700ryn', 12643, 13665, 13667, 12641, 25392, 12853, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz701uca', 13667, 13409, 14691, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14135, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz701umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('baz701uwa', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bhz')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('umi')
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
    sprite('az600_01', 7)	# 2-8
    sprite('az600_02', 7)	# 9-15
    sprite('az600_03', 7)	# 16-22
    sprite('az600_04', 7)	# 23-29
    sprite('az600_05', 7)	# 30-36
    sprite('az600_06', 7)	# 37-43
    sprite('az600_07', 7)	# 44-50
    Unknown7006('baz500', 100, 897212770, 12592, 0, 0, 100, 897212770, 12848, 0, 0, 100, 897212770, 13360, 0, 0, 100)
    sprite('az600_08', 7)	# 51-57
    sprite('az600_09', 7)	# 58-64
    label(1)
    sprite('az600_10', 1)	# 65-65
    if SLOT_97:
        _gotolabel(1)
    sprite('az600_11', 7)	# 66-72
    GFX_1('azef_entry1', 0)
    SFX_3('azse_13')
    SFX_0('100_hit_grap_1')
    sprite('az600_12', 7)	# 73-79
    sprite('az600_12ex01', 7)	# 80-86
    sprite('az600_12ex02', 7)	# 87-93
    sprite('az600_13', 7)	# 94-100
    Unknown23018(1)
    label(2)
    sprite('az000_00', 7)	# 101-107
    sprite('az000_01', 7)	# 108-114
    sprite('az000_02', 7)	# 115-121
    sprite('az000_03', 7)	# 122-128
    sprite('az000_04', 7)	# 129-135
    sprite('az000_05', 7)	# 136-142
    sprite('az000_06', 7)	# 143-149
    sprite('az000_07', 7)	# 150-156
    sprite('az000_08', 7)	# 157-163
    sprite('az000_09', 7)	# 164-170
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('az601_00', 110)	# 171-280	 **attackbox here**
    Unknown7006('baz500', 100, 897212770, 12592, 0, 0, 100, 897212770, 13616, 0, 0, 100, 897212770, 13104, 0, 0, 100)
    sprite('az601_01', 7)	# 281-287	 **attackbox here**
    sprite('az601_02', 7)	# 288-294	 **attackbox here**
    sprite('az601_03', 7)	# 295-301	 **attackbox here**
    sprite('az601_04', 7)	# 302-308	 **attackbox here**
    sprite('az601_05', 7)	# 309-315	 **attackbox here**
    sprite('az601_06', 7)	# 316-322	 **attackbox here**
    sprite('az601_07', 7)	# 323-329	 **attackbox here**
    GFX_1('ef_exhit_sub', 0)
    SFX_0('100_hit_grap_3')
    sprite('az601_08', 7)	# 330-336	 **attackbox here**
    sprite('az601_09', 7)	# 337-343	 **attackbox here**
    sprite('az601_10', 9)	# 344-352	 **attackbox here**
    sprite('az601_11', 7)	# 353-359
    Unknown23018(1)
    sprite('az601_12', 7)	# 360-366
    sprite('az601_13', 7)	# 367-373
    label(11)
    sprite('az000_00', 7)	# 374-380
    sprite('az000_01', 7)	# 381-387
    sprite('az000_02', 7)	# 388-394
    sprite('az000_03', 7)	# 395-401
    sprite('az000_04', 7)	# 402-408
    sprite('az000_05', 7)	# 409-415
    sprite('az000_06', 7)	# 416-422
    sprite('az000_07', 7)	# 423-429
    sprite('az000_08', 7)	# 430-436
    sprite('az000_09', 7)	# 437-443
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('az000_00', 1)	# 444-444
    SFX_1('baz701umi')
    label(21)
    sprite('az000_00', 7)	# 445-451
    sprite('az000_01', 7)	# 452-458
    sprite('az000_02', 7)	# 459-465
    sprite('az000_03', 7)	# 466-472
    sprite('az000_04', 7)	# 473-479
    sprite('az000_05', 7)	# 480-486
    sprite('az000_06', 7)	# 487-493
    sprite('az000_07', 7)	# 494-500
    sprite('az000_08', 7)	# 501-507
    sprite('az000_09', 7)	# 508-514
    gotoLabel(21)
    label(100)
    sprite('az300_00', 6)	# 515-520
    if SLOT_158:
        Unknown1000(-1210000)
    else:
        Unknown1000(-1465000)
    sprite('az300_01', 6)	# 521-526
    SFX_1('baz600brg')
    sprite('az300_02', 7)	# 527-533
    sprite('az300_03', 4)	# 534-537
    SFX_3('azse_02')
    sprite('az300_04', 4)	# 538-541	 **attackbox here**
    sprite('az300_05', 4)	# 542-545
    sprite('az300_06', 4)	# 546-549
    sprite('az300_07', 8)	# 550-557
    sprite('az300_08', 6)	# 558-563
    sprite('az300_09', 6)	# 564-569
    sprite('az300_10', 6)	# 570-575
    sprite('az300_11', 6)	# 576-581
    sprite('az300_12', 6)	# 582-587
    sprite('az300_13', 6)	# 588-593
    sprite('az300_08', 8)	# 594-601
    sprite('az300_13', 6)	# 602-607
    sprite('az300_12', 6)	# 608-613
    sprite('az300_11', 6)	# 614-619
    sprite('az300_10', 6)	# 620-625
    sprite('az300_09', 6)	# 626-631
    sprite('az300_14', 6)	# 632-637
    sprite('az300_15', 6)	# 638-643
    sprite('az300_16', 6)	# 644-649
    sprite('az300_00', 6)	# 650-655
    label(101)
    sprite('az000_00', 7)	# 656-662
    sprite('az000_01', 7)	# 663-669
    sprite('az000_02', 7)	# 670-676
    sprite('az000_03', 7)	# 677-683
    sprite('az000_04', 7)	# 684-690
    sprite('az000_05', 7)	# 691-697
    sprite('az000_06', 7)	# 698-704
    sprite('az000_07', 7)	# 705-711
    sprite('az000_08', 7)	# 712-718
    sprite('az000_09', 7)	# 719-725
    if SLOT_97:
        _gotolabel(101)
    sprite('az000_00', 1)	# 726-726
    Unknown21007(24, 40)
    Unknown21011(360)
    label(102)
    sprite('az000_00', 7)	# 727-733
    sprite('az000_01', 7)	# 734-740
    sprite('az000_02', 7)	# 741-747
    sprite('az000_03', 7)	# 748-754
    sprite('az000_04', 7)	# 755-761
    sprite('az000_05', 7)	# 762-768
    sprite('az000_06', 7)	# 769-775
    sprite('az000_07', 7)	# 776-782
    sprite('az000_08', 7)	# 783-789
    sprite('az000_09', 7)	# 790-796
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('az600_01', 7)	# 797-803
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('az600_02', 7)	# 804-810
    sprite('az600_03', 7)	# 811-817
    sprite('az600_04', 7)	# 818-824
    sprite('az600_05', 7)	# 825-831
    sprite('az600_06', 7)	# 832-838
    sprite('az600_07', 7)	# 839-845
    SFX_1('baz600bhz')
    sprite('az600_08', 7)	# 846-852
    sprite('az600_09', 7)	# 853-859
    label(111)
    sprite('az600_10', 1)	# 860-860
    if SLOT_97:
        _gotolabel(111)
    sprite('az600_10', 30)	# 861-890
    sprite('az600_11', 7)	# 891-897
    GFX_1('azef_entry1', 0)
    SFX_3('azse_13')
    SFX_0('100_hit_grap_1')
    sprite('az600_12', 7)	# 898-904
    sprite('az600_12ex01', 7)	# 905-911
    sprite('az600_12ex02', 7)	# 912-918
    sprite('az600_13', 7)	# 919-925
    Unknown21011(120)
    Unknown21007(24, 40)
    label(112)
    sprite('az000_00', 7)	# 926-932
    sprite('az000_01', 7)	# 933-939
    sprite('az000_02', 7)	# 940-946
    sprite('az000_03', 7)	# 947-953
    sprite('az000_04', 7)	# 954-960
    sprite('az000_05', 7)	# 961-967
    sprite('az000_06', 7)	# 968-974
    sprite('az000_07', 7)	# 975-981
    sprite('az000_08', 7)	# 982-988
    sprite('az000_09', 7)	# 989-995
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('az615_00', 6)	# 996-1001
    sprite('az615_01', 6)	# 1002-1007
    sprite('az615_02', 6)	# 1008-1013
    sprite('az615_03', 6)	# 1014-1019
    SFX_1('baz600pce')
    sprite('az615_04', 6)	# 1020-1025
    sprite('az615_05', 6)	# 1026-1031
    sprite('az615_06', 6)	# 1032-1037
    sprite('az615_07', 6)	# 1038-1043
    sprite('az615_08', 6)	# 1044-1049
    sprite('az615_09', 6)	# 1050-1055
    sprite('az615_10', 6)	# 1056-1061
    sprite('az615_11', 6)	# 1062-1067
    label(121)
    sprite('az615_12', 1)	# 1068-1068
    if SLOT_97:
        _gotolabel(121)
    sprite('az615_12', 30)	# 1069-1098
    sprite('az615_12', 32767)	# 1099-33865
    Unknown21007(24, 40)
    Unknown21011(240)
    ExitState()
    label(130)
    sprite('az000_00', 1)	# 33866-33866
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-1000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('az000_00', 7)	# 33867-33873
    sprite('az000_01', 7)	# 33874-33880
    sprite('az000_02', 7)	# 33881-33887
    sprite('az000_03', 7)	# 33888-33894
    sprite('az000_04', 7)	# 33895-33901
    sprite('az000_05', 7)	# 33902-33908
    sprite('az000_06', 7)	# 33909-33915
    sprite('az000_07', 7)	# 33916-33922
    sprite('az000_08', 7)	# 33923-33929
    sprite('az000_09', 7)	# 33930-33936
    gotoLabel(131)
    label(132)
    sprite('az300_00', 6)	# 33937-33942
    sprite('az300_01', 6)	# 33943-33948
    SFX_1('baz601uwa')
    sprite('az300_02', 7)	# 33949-33955
    sprite('az300_03', 4)	# 33956-33959
    SFX_3('azse_02')
    sprite('az300_04', 4)	# 33960-33963	 **attackbox here**
    sprite('az300_05', 4)	# 33964-33967
    sprite('az300_06', 4)	# 33968-33971
    sprite('az300_07', 8)	# 33972-33979
    sprite('az300_08', 6)	# 33980-33985
    sprite('az300_09', 6)	# 33986-33991
    sprite('az300_10', 6)	# 33992-33997
    sprite('az300_11', 6)	# 33998-34003
    sprite('az300_12', 6)	# 34004-34009
    sprite('az300_13', 6)	# 34010-34015
    sprite('az300_08', 8)	# 34016-34023
    sprite('az300_13', 6)	# 34024-34029
    sprite('az300_12', 6)	# 34030-34035
    sprite('az300_11', 6)	# 34036-34041
    sprite('az300_10', 6)	# 34042-34047
    sprite('az300_09', 6)	# 34048-34053
    sprite('az300_14', 6)	# 34054-34059
    sprite('az300_15', 6)	# 34060-34065
    sprite('az300_16', 6)	# 34066-34071
    sprite('az300_00', 6)	# 34072-34077
    Unknown23018(1)
    label(133)
    sprite('az000_00', 7)	# 34078-34084
    sprite('az000_01', 7)	# 34085-34091
    sprite('az000_02', 7)	# 34092-34098
    sprite('az000_03', 7)	# 34099-34105
    sprite('az000_04', 7)	# 34106-34112
    sprite('az000_05', 7)	# 34113-34119
    sprite('az000_06', 7)	# 34120-34126
    sprite('az000_07', 7)	# 34127-34133
    sprite('az000_08', 7)	# 34134-34140
    sprite('az000_09', 7)	# 34141-34147
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('az000_00', 1)	# 34148-34148
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('az000_00', 7)	# 34149-34155
    sprite('az000_01', 7)	# 34156-34162
    sprite('az000_02', 7)	# 34163-34169
    sprite('az000_03', 7)	# 34170-34176
    sprite('az000_04', 7)	# 34177-34183
    sprite('az000_05', 7)	# 34184-34190
    sprite('az000_06', 7)	# 34191-34197
    sprite('az000_07', 7)	# 34198-34204
    sprite('az000_08', 7)	# 34205-34211
    sprite('az000_09', 7)	# 34212-34218
    gotoLabel(141)
    label(142)
    sprite('az300_00', 6)	# 34219-34224
    sprite('az300_01', 6)	# 34225-34230
    SFX_1('baz601pka')
    sprite('az300_02', 7)	# 34231-34237
    sprite('az300_03', 4)	# 34238-34241
    SFX_3('azse_02')
    sprite('az300_04', 4)	# 34242-34245	 **attackbox here**
    sprite('az300_05', 4)	# 34246-34249
    sprite('az300_06', 4)	# 34250-34253
    sprite('az300_07', 8)	# 34254-34261
    sprite('az300_08', 6)	# 34262-34267
    sprite('az300_09', 6)	# 34268-34273
    sprite('az300_10', 6)	# 34274-34279
    sprite('az300_11', 6)	# 34280-34285
    sprite('az300_12', 6)	# 34286-34291
    sprite('az300_13', 6)	# 34292-34297
    sprite('az300_08', 8)	# 34298-34305
    sprite('az300_13', 6)	# 34306-34311
    sprite('az300_12', 6)	# 34312-34317
    sprite('az300_11', 6)	# 34318-34323
    sprite('az300_10', 6)	# 34324-34329
    sprite('az300_09', 6)	# 34330-34335
    sprite('az300_14', 6)	# 34336-34341
    sprite('az300_15', 6)	# 34342-34347
    sprite('az300_16', 6)	# 34348-34353
    sprite('az300_00', 6)	# 34354-34359
    Unknown23018(1)
    label(143)
    sprite('az000_00', 7)	# 34360-34366
    sprite('az000_01', 7)	# 34367-34373
    sprite('az000_02', 7)	# 34374-34380
    sprite('az000_03', 7)	# 34381-34387
    sprite('az000_04', 7)	# 34388-34394
    sprite('az000_05', 7)	# 34395-34401
    sprite('az000_06', 7)	# 34402-34408
    sprite('az000_07', 7)	# 34409-34415
    sprite('az000_08', 7)	# 34416-34422
    sprite('az000_09', 7)	# 34423-34429
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('az600_01', 7)	# 34430-34436
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('az600_02', 7)	# 34437-34443
    sprite('az600_03', 7)	# 34444-34450
    sprite('az600_04', 7)	# 34451-34457
    sprite('az600_05', 7)	# 34458-34464
    sprite('az600_06', 7)	# 34465-34471
    sprite('az600_07', 7)	# 34472-34478
    SFX_1('baz600uca')
    sprite('az600_08', 7)	# 34479-34485
    sprite('az600_09', 7)	# 34486-34492
    label(151)
    sprite('az600_10', 1)	# 34493-34493
    if SLOT_97:
        _gotolabel(151)
    sprite('az600_10', 30)	# 34494-34523
    sprite('az600_11', 7)	# 34524-34530
    GFX_1('azef_entry1', 0)
    SFX_3('azse_13')
    SFX_0('100_hit_grap_1')
    sprite('az600_12', 7)	# 34531-34537
    sprite('az600_12ex01', 7)	# 34538-34544
    sprite('az600_12ex02', 7)	# 34545-34551
    sprite('az600_13', 7)	# 34552-34558
    Unknown21011(300)
    Unknown21007(24, 40)
    label(152)
    sprite('az000_00', 7)	# 34559-34565
    sprite('az000_01', 7)	# 34566-34572
    sprite('az000_02', 7)	# 34573-34579
    sprite('az000_03', 7)	# 34580-34586
    sprite('az000_04', 7)	# 34587-34593
    sprite('az000_05', 7)	# 34594-34600
    sprite('az000_06', 7)	# 34601-34607
    sprite('az000_07', 7)	# 34608-34614
    sprite('az000_08', 7)	# 34615-34621
    sprite('az000_09', 7)	# 34622-34628
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('az000_00', 1)	# 34629-34629
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('az000_00', 7)	# 34630-34636
    sprite('az000_01', 7)	# 34637-34643
    sprite('az000_02', 7)	# 34644-34650
    sprite('az000_03', 7)	# 34651-34657
    sprite('az000_04', 7)	# 34658-34664
    sprite('az000_05', 7)	# 34665-34671
    sprite('az000_06', 7)	# 34672-34678
    sprite('az000_07', 7)	# 34679-34685
    sprite('az000_08', 7)	# 34686-34692
    sprite('az000_09', 7)	# 34693-34699
    gotoLabel(161)
    label(162)
    sprite('az300_00', 6)	# 34700-34705
    sprite('az300_01', 6)	# 34706-34711
    SFX_1('baz601ryn')
    sprite('az300_02', 7)	# 34712-34718
    sprite('az300_03', 4)	# 34719-34722
    SFX_3('azse_02')
    sprite('az300_04', 4)	# 34723-34726	 **attackbox here**
    sprite('az300_05', 4)	# 34727-34730
    sprite('az300_06', 4)	# 34731-34734
    sprite('az300_07', 8)	# 34735-34742
    sprite('az300_08', 6)	# 34743-34748
    sprite('az300_09', 6)	# 34749-34754
    sprite('az300_10', 6)	# 34755-34760
    sprite('az300_11', 6)	# 34761-34766
    sprite('az300_12', 6)	# 34767-34772
    sprite('az300_13', 6)	# 34773-34778
    sprite('az300_08', 8)	# 34779-34786
    sprite('az300_13', 6)	# 34787-34792
    sprite('az300_12', 6)	# 34793-34798
    sprite('az300_11', 6)	# 34799-34804
    sprite('az300_10', 6)	# 34805-34810
    sprite('az300_09', 6)	# 34811-34816
    sprite('az300_14', 6)	# 34817-34822
    sprite('az300_15', 6)	# 34823-34828
    sprite('az300_16', 6)	# 34829-34834
    sprite('az300_00', 6)	# 34835-34840
    Unknown23018(1)
    label(163)
    sprite('az000_00', 7)	# 34841-34847
    sprite('az000_01', 7)	# 34848-34854
    sprite('az000_02', 7)	# 34855-34861
    sprite('az000_03', 7)	# 34862-34868
    sprite('az000_04', 7)	# 34869-34875
    sprite('az000_05', 7)	# 34876-34882
    sprite('az000_06', 7)	# 34883-34889
    sprite('az000_07', 7)	# 34890-34896
    sprite('az000_08', 7)	# 34897-34903
    sprite('az000_09', 7)	# 34904-34910
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('az300_00', 6)	# 34911-34916
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('az300_01', 6)	# 34917-34922
    SFX_1('baz600umi')
    sprite('az300_02', 7)	# 34923-34929
    sprite('az300_03', 4)	# 34930-34933
    SFX_3('azse_02')
    sprite('az300_04', 4)	# 34934-34937	 **attackbox here**
    sprite('az300_05', 4)	# 34938-34941
    sprite('az300_06', 4)	# 34942-34945
    sprite('az300_07', 8)	# 34946-34953
    sprite('az300_08', 6)	# 34954-34959
    sprite('az300_09', 6)	# 34960-34965
    sprite('az300_10', 6)	# 34966-34971
    sprite('az300_11', 6)	# 34972-34977
    sprite('az300_12', 6)	# 34978-34983
    sprite('az300_13', 6)	# 34984-34989
    sprite('az300_08', 8)	# 34990-34997
    sprite('az300_13', 6)	# 34998-35003
    sprite('az300_12', 6)	# 35004-35009
    sprite('az300_11', 6)	# 35010-35015
    sprite('az300_10', 6)	# 35016-35021
    sprite('az300_09', 6)	# 35022-35027
    sprite('az300_14', 6)	# 35028-35033
    sprite('az300_15', 6)	# 35034-35039
    sprite('az300_16', 6)	# 35040-35045
    sprite('az300_00', 6)	# 35046-35051
    label(171)
    sprite('az000_00', 7)	# 35052-35058
    sprite('az000_01', 7)	# 35059-35065
    sprite('az000_02', 7)	# 35066-35072
    sprite('az000_03', 7)	# 35073-35079
    sprite('az000_04', 7)	# 35080-35086
    sprite('az000_05', 7)	# 35087-35093
    sprite('az000_06', 7)	# 35094-35100
    sprite('az000_07', 7)	# 35101-35107
    sprite('az000_08', 7)	# 35108-35114
    sprite('az000_09', 7)	# 35115-35121
    if SLOT_97:
        _gotolabel(171)
    sprite('az000_00', 1)	# 35122-35122
    Unknown21007(24, 40)
    Unknown21011(120)
    label(172)
    sprite('az000_00', 7)	# 35123-35129
    sprite('az000_01', 7)	# 35130-35136
    sprite('az000_02', 7)	# 35137-35143
    sprite('az000_03', 7)	# 35144-35150
    sprite('az000_04', 7)	# 35151-35157
    sprite('az000_05', 7)	# 35158-35164
    sprite('az000_06', 7)	# 35165-35171
    sprite('az000_07', 7)	# 35172-35178
    sprite('az000_08', 7)	# 35179-35185
    sprite('az000_09', 7)	# 35186-35192
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('az600_01', 7)	# 35193-35199
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('az600_02', 7)	# 35200-35206
    sprite('az600_03', 7)	# 35207-35213
    sprite('az600_04', 7)	# 35214-35220
    sprite('az600_05', 7)	# 35221-35227
    sprite('az600_06', 7)	# 35228-35234
    sprite('az600_07', 7)	# 35235-35241
    SFX_1('baz600bma')
    sprite('az600_08', 7)	# 35242-35248
    sprite('az600_09', 7)	# 35249-35255
    label(181)
    sprite('az600_10', 1)	# 35256-35256
    if SLOT_97:
        _gotolabel(181)
    sprite('az600_10', 30)	# 35257-35286
    sprite('az600_11', 7)	# 35287-35293
    GFX_1('azef_entry1', 0)
    SFX_3('azse_13')
    SFX_0('100_hit_grap_1')
    sprite('az600_12', 7)	# 35294-35300
    sprite('az600_12ex01', 7)	# 35301-35307
    sprite('az600_12ex02', 7)	# 35308-35314
    sprite('az600_13', 7)	# 35315-35321
    Unknown21011(300)
    Unknown21007(24, 40)
    label(182)
    sprite('az000_00', 7)	# 35322-35328
    sprite('az000_01', 7)	# 35329-35335
    sprite('az000_02', 7)	# 35336-35342
    sprite('az000_03', 7)	# 35343-35349
    sprite('az000_04', 7)	# 35350-35356
    sprite('az000_05', 7)	# 35357-35363
    sprite('az000_06', 7)	# 35364-35370
    sprite('az000_07', 7)	# 35371-35377
    sprite('az000_08', 7)	# 35378-35384
    sprite('az000_09', 7)	# 35385-35391
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('az000_00', 1)	# 35392-35392
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('az000_00', 7)	# 35393-35399
    sprite('az000_01', 7)	# 35400-35406
    sprite('az000_02', 7)	# 35407-35413
    sprite('az000_03', 7)	# 35414-35420
    sprite('az000_04', 7)	# 35421-35427
    sprite('az000_05', 7)	# 35428-35434
    sprite('az000_06', 7)	# 35435-35441
    sprite('az000_07', 7)	# 35442-35448
    sprite('az000_08', 7)	# 35449-35455
    sprite('az000_09', 7)	# 35456-35462
    gotoLabel(191)
    label(192)
    sprite('az300_00', 6)	# 35463-35468
    sprite('az300_01', 6)	# 35469-35474
    SFX_1('baz601pak')
    sprite('az300_02', 7)	# 35475-35481
    sprite('az300_03', 4)	# 35482-35485
    SFX_3('azse_02')
    sprite('az300_04', 4)	# 35486-35489	 **attackbox here**
    sprite('az300_05', 4)	# 35490-35493
    sprite('az300_06', 4)	# 35494-35497
    sprite('az300_07', 8)	# 35498-35505
    sprite('az300_08', 6)	# 35506-35511
    sprite('az300_09', 6)	# 35512-35517
    sprite('az300_10', 6)	# 35518-35523
    sprite('az300_11', 6)	# 35524-35529
    sprite('az300_12', 6)	# 35530-35535
    sprite('az300_13', 6)	# 35536-35541
    sprite('az300_08', 8)	# 35542-35549
    sprite('az300_13', 6)	# 35550-35555
    sprite('az300_12', 6)	# 35556-35561
    sprite('az300_11', 6)	# 35562-35567
    sprite('az300_10', 6)	# 35568-35573
    sprite('az300_09', 6)	# 35574-35579
    sprite('az300_14', 6)	# 35580-35585
    sprite('az300_15', 6)	# 35586-35591
    sprite('az300_16', 6)	# 35592-35597
    sprite('az300_00', 6)	# 35598-35603
    Unknown23018(1)
    label(193)
    sprite('az000_00', 7)	# 35604-35610
    sprite('az000_01', 7)	# 35611-35617
    sprite('az000_02', 7)	# 35618-35624
    sprite('az000_03', 7)	# 35625-35631
    sprite('az000_04', 7)	# 35632-35638
    sprite('az000_05', 7)	# 35639-35645
    sprite('az000_06', 7)	# 35646-35652
    sprite('az000_07', 7)	# 35653-35659
    sprite('az000_08', 7)	# 35660-35666
    sprite('az000_09', 7)	# 35667-35673
    gotoLabel(193)
    ExitState()
    label(991)
    sprite('az000_00', 1)	# 35674-35674
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('az000_00', 7)	# 35675-35681
    sprite('az000_01', 7)	# 35682-35688
    sprite('az000_02', 7)	# 35689-35695
    sprite('az000_03', 7)	# 35696-35702
    sprite('az000_04', 7)	# 35703-35709
    sprite('az000_05', 7)	# 35710-35716
    sprite('az000_06', 7)	# 35717-35723
    sprite('az000_07', 7)	# 35724-35730
    sprite('az000_08', 7)	# 35731-35737
    sprite('az000_09', 7)	# 35738-35744
    gotoLabel(992)
    label(993)
    sprite('az000_00', 4)	# 35745-35748
    sprite('az620_04ex01', 5)	# 35749-35753
    sprite('az620_05ex01', 5)	# 35754-35758
    Unknown3004(-12)
    sprite('az620_06ex01', 5)	# 35759-35763
    sprite('az620_07ex01', 5)	# 35764-35768
    sprite('az620_08ex01', 4)	# 35769-35772
    sprite('az620_09ex01', 4)	# 35773-35776
    sprite('az620_10ex03', 4)	# 35777-35780
    loopRest()
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
            if PartnerChar('brg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('umi'):
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
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('az610_00', 6)	# 4-9
    sprite('az610_01', 6)	# 10-15
    sprite('az610_02', 6)	# 16-21
    sprite('az610_03', 9)	# 22-30
    sprite('az610_04', 5)	# 31-35
    sprite('az610_05', 7)	# 36-42
    sprite('az610_06', 7)	# 43-49
    GFX_0('610aura', -1)
    sprite('az610_07', 7)	# 50-56
    if SLOT_158:
        if SLOT_52:
            Unknown7006('baz524', 100, 897212770, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('baz403_0', 100, 880435554, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('baz520', 100, 897212770, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown3029(1)
    Unknown3069(0)
    SFX_3('azse_15')
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_08', 7)	# 57-63
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_09', 7)	# 64-70
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_10', 7)	# 71-77
    SFX_3('azse_15')
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_11', 7)	# 78-84
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_12', 7)	# 85-91
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    Unknown23018(1)
    label(1)
    sprite('az610_07', 7)	# 92-98
    SFX_3('azse_15')
    ScreenShake(0, 4000)
    SFX_0('019_quake_1')
    sprite('az610_08', 7)	# 99-105
    ScreenShake(0, 4000)
    sprite('az610_09', 7)	# 106-112
    ScreenShake(0, 4000)
    sprite('az610_10', 7)	# 113-119
    SFX_3('azse_15')
    ScreenShake(0, 4000)
    sprite('az610_11', 7)	# 120-126
    ScreenShake(0, 4000)
    sprite('az610_12', 7)	# 127-133
    ScreenShake(0, 4000)
    gotoLabel(1)
    loopRest()
    label(10)
    sprite('az611_00', 8)	# 134-141
    if SLOT_158:
        if SLOT_52:
            Unknown7006('baz524', 100, 897212770, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('baz403_0', 100, 880435554, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('baz522', 100, 897212770, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('az611_01', 8)	# 142-149
    sprite('az611_02', 7)	# 150-156
    sprite('az611_03', 7)	# 157-163
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 164-169
    sprite('az611_05', 6)	# 170-175
    sprite('az611_06', 6)	# 176-181
    sprite('az611_07', 6)	# 182-187
    sprite('az611_08', 6)	# 188-193
    Unknown23018(1)
    sprite('az611_09', 55)	# 194-248
    sprite('az611_10', 6)	# 249-254
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    sprite('az611_11', 32767)	# 255-33021
    loopRest()
    label(100)
    sprite('az611_00', 8)	# 33022-33029
    sprite('az611_01', 8)	# 33030-33037
    sprite('az611_02', 7)	# 33038-33044
    sprite('az611_03', 7)	# 33045-33051
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 33052-33057
    sprite('az611_05', 6)	# 33058-33063
    sprite('az611_06', 6)	# 33064-33069
    sprite('az611_07', 6)	# 33070-33075
    SFX_1('baz700brg')
    sprite('az611_08', 6)	# 33076-33081
    sprite('az611_09', 55)	# 33082-33136
    sprite('az611_10', 6)	# 33137-33142
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    label(101)
    sprite('az611_11', 1)	# 33143-33143
    if SLOT_97:
        _gotolabel(101)
    sprite('az611_11', 32767)	# 33144-65910
    Unknown21007(24, 40)
    Unknown21011(240)
    label(110)
    sprite('az611_00', 8)	# 65911-65918
    sprite('az611_01', 8)	# 65919-65926
    sprite('az611_02', 7)	# 65927-65933
    sprite('az611_03', 7)	# 65934-65940
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 65941-65946
    sprite('az611_05', 6)	# 65947-65952
    sprite('az611_06', 6)	# 65953-65958
    SFX_1('baz700bhz')
    sprite('az611_07', 6)	# 65959-65964
    sprite('az611_08', 6)	# 65965-65970
    sprite('az611_09', 55)	# 65971-66025
    sprite('az611_10', 6)	# 66026-66031
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    label(111)
    sprite('az611_11', 1)	# 66032-66032
    if SLOT_97:
        _gotolabel(111)
    sprite('az611_11', 50)	# 66033-66082
    sprite('az611_11', 32767)	# 66083-98849
    Unknown21007(24, 40)
    Unknown21011(240)
    label(120)
    sprite('az611_00', 8)	# 98850-98857
    sprite('az611_01', 8)	# 98858-98865
    sprite('az611_02', 7)	# 98866-98872
    sprite('az611_03', 7)	# 98873-98879
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 98880-98885
    sprite('az611_05', 6)	# 98886-98891
    sprite('az611_06', 6)	# 98892-98897
    SFX_1('baz700pce')
    sprite('az611_07', 6)	# 98898-98903
    sprite('az611_08', 6)	# 98904-98909
    sprite('az611_09', 55)	# 98910-98964
    sprite('az611_10', 6)	# 98965-98970
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    label(121)
    sprite('az611_11', 1)	# 98971-98971
    if SLOT_97:
        _gotolabel(121)
    sprite('az611_11', 32767)	# 98972-131738
    Unknown21007(24, 40)
    Unknown21011(240)
    label(130)
    sprite('az611_00', 8)	# 131739-131746
    sprite('az611_01', 8)	# 131747-131754
    sprite('az611_02', 7)	# 131755-131761
    sprite('az611_03', 7)	# 131762-131768
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 131769-131774
    sprite('az611_05', 6)	# 131775-131780
    sprite('az611_06', 6)	# 131781-131786
    sprite('az611_07', 6)	# 131787-131792
    SFX_1('baz700pka')
    sprite('az611_08', 6)	# 131793-131798
    sprite('az611_09', 55)	# 131799-131853
    sprite('az611_10', 6)	# 131854-131859
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    label(131)
    sprite('az611_11', 1)	# 131860-131860
    if SLOT_97:
        _gotolabel(131)
    sprite('az611_11', 32767)	# 131861-164627
    Unknown21007(24, 40)
    Unknown21011(320)
    label(140)
    sprite('az000_00', 1)	# 164628-164628
    if (not SLOT_158):
        Unknown2019(-1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('az000_00', 7)	# 164629-164635
    sprite('az000_01', 7)	# 164636-164642
    sprite('az000_02', 7)	# 164643-164649
    sprite('az000_03', 7)	# 164650-164656
    sprite('az000_04', 7)	# 164657-164663
    sprite('az000_05', 7)	# 164664-164670
    sprite('az000_06', 7)	# 164671-164677
    sprite('az000_07', 7)	# 164678-164684
    sprite('az000_08', 7)	# 164685-164691
    sprite('az000_09', 7)	# 164692-164698
    gotoLabel(141)
    label(142)
    sprite('az001_00', 6)	# 164699-164704
    SFX_1('baz701uwa')
    sprite('az001_01', 6)	# 164705-164710
    sprite('az001_02', 6)	# 164711-164716
    sprite('az001_03', 6)	# 164717-164722
    sprite('az001_04', 6)	# 164723-164728
    sprite('az001_05', 6)	# 164729-164734
    sprite('az001_06', 6)	# 164735-164740
    sprite('az001_03', 6)	# 164741-164746
    sprite('az001_04', 6)	# 164747-164752
    sprite('az001_05', 6)	# 164753-164758
    sprite('az001_06', 6)	# 164759-164764
    sprite('az001_01', 6)	# 164765-164770
    sprite('az001_00', 6)	# 164771-164776
    Unknown23018(1)
    label(143)
    sprite('az000_00', 7)	# 164777-164783
    sprite('az000_01', 7)	# 164784-164790
    sprite('az000_02', 7)	# 164791-164797
    sprite('az000_03', 7)	# 164798-164804
    sprite('az000_04', 7)	# 164805-164811
    sprite('az000_05', 7)	# 164812-164818
    sprite('az000_06', 7)	# 164819-164825
    sprite('az000_07', 7)	# 164826-164832
    sprite('az000_08', 7)	# 164833-164839
    sprite('az000_09', 7)	# 164840-164846
    gotoLabel(143)
    label(150)
    sprite('az000_00', 1)	# 164847-164847

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('az000_00', 7)	# 164848-164854
    sprite('az000_01', 7)	# 164855-164861
    sprite('az000_02', 7)	# 164862-164868
    sprite('az000_03', 7)	# 164869-164875
    sprite('az000_04', 7)	# 164876-164882
    sprite('az000_05', 7)	# 164883-164889
    sprite('az000_06', 7)	# 164890-164896
    sprite('az000_07', 7)	# 164897-164903
    sprite('az000_08', 7)	# 164904-164910
    sprite('az000_09', 7)	# 164911-164917
    gotoLabel(151)
    label(152)
    Unknown2004(1, 0)
    sprite('az620_00', 6)	# 164918-164923
    sprite('az620_01', 6)	# 164924-164929
    sprite('az620_02', 6)	# 164930-164935
    sprite('az620_03', 6)	# 164936-164941
    SFX_1('baz701uca')
    sprite('az620_04', 6)	# 164942-164947
    sprite('az620_05', 6)	# 164948-164953
    sprite('az620_06', 6)	# 164954-164959
    sprite('az620_07', 6)	# 164960-164965
    sprite('az620_08', 6)	# 164966-164971
    sprite('az620_09', 6)	# 164972-164977
    sprite('az620_10', 6)	# 164978-164983
    sprite('az620_10ex1', 6)	# 164984-164989
    sprite('az620_10ex2', 6)	# 164990-164995
    sprite('az620_11', 32767)	# 164996-197762
    Unknown23018(1)
    label(160)
    sprite('az611_00', 8)	# 197763-197770
    sprite('az611_01', 8)	# 197771-197778
    sprite('az611_02', 7)	# 197779-197785
    sprite('az611_03', 7)	# 197786-197792
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 197793-197798
    sprite('az611_05', 6)	# 197799-197804
    sprite('az611_06', 6)	# 197805-197810
    sprite('az611_07', 6)	# 197811-197816
    SFX_1('baz700ryn')
    sprite('az611_08', 6)	# 197817-197822
    sprite('az611_09', 55)	# 197823-197877
    sprite('az611_10', 6)	# 197878-197883
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    label(161)
    sprite('az611_11', 1)	# 197884-197884
    if SLOT_97:
        _gotolabel(161)
    sprite('az611_11', 30)	# 197885-197914
    sprite('az611_11', 32767)	# 197915-230681
    Unknown21007(24, 40)
    Unknown21011(180)
    label(170)
    sprite('az000_00', 1)	# 230682-230682

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    Unknown2019(1000)
    label(171)
    sprite('az000_00', 7)	# 230683-230689
    sprite('az000_01', 7)	# 230690-230696
    sprite('az000_02', 7)	# 230697-230703
    sprite('az000_03', 7)	# 230704-230710
    sprite('az000_04', 7)	# 230711-230717
    sprite('az000_05', 7)	# 230718-230724
    sprite('az000_06', 7)	# 230725-230731
    sprite('az000_07', 7)	# 230732-230738
    sprite('az000_08', 7)	# 230739-230745
    sprite('az000_09', 7)	# 230746-230752
    gotoLabel(171)
    label(172)
    sprite('az620_00', 6)	# 230753-230758
    Unknown2004(1, 0)
    sprite('az620_01', 6)	# 230759-230764
    sprite('az620_02', 6)	# 230765-230770
    sprite('az620_03', 6)	# 230771-230776
    SFX_1('baz701umi')
    Unknown23018(1)
    sprite('az620_04', 6)	# 230777-230782
    sprite('az620_05', 6)	# 230783-230788
    sprite('az620_06', 6)	# 230789-230794
    sprite('az620_07', 6)	# 230795-230800
    sprite('az620_08', 6)	# 230801-230806
    sprite('az620_09', 6)	# 230807-230812
    sprite('az620_10', 6)	# 230813-230818
    sprite('az620_10ex1', 6)	# 230819-230824
    sprite('az620_10ex2', 6)	# 230825-230830
    sprite('az620_11', 32767)	# 230831-263597
    label(180)
    sprite('az611_00', 8)	# 263598-263605
    sprite('az611_01', 8)	# 263606-263613
    sprite('az611_02', 7)	# 263614-263620
    sprite('az611_03', 7)	# 263621-263627
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 263628-263633
    sprite('az611_05', 6)	# 263634-263639
    sprite('az611_06', 6)	# 263640-263645
    sprite('az611_07', 6)	# 263646-263651
    SFX_1('baz700bma')
    sprite('az611_08', 6)	# 263652-263657
    sprite('az611_09', 55)	# 263658-263712
    sprite('az611_10', 6)	# 263713-263718
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    label(181)
    sprite('az611_11', 1)	# 263719-263719
    if SLOT_97:
        _gotolabel(181)
    sprite('az611_11', 30)	# 263720-263749
    sprite('az611_11', 32767)	# 263750-296516
    Unknown21007(24, 40)
    Unknown21011(240)
    label(190)
    sprite('az000_00', 1)	# 296517-296517

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('az000_00', 7)	# 296518-296524
    sprite('az000_01', 7)	# 296525-296531
    sprite('az000_02', 7)	# 296532-296538
    sprite('az000_03', 7)	# 296539-296545
    sprite('az000_04', 7)	# 296546-296552
    sprite('az000_05', 7)	# 296553-296559
    sprite('az000_06', 7)	# 296560-296566
    sprite('az000_07', 7)	# 296567-296573
    sprite('az000_08', 7)	# 296574-296580
    sprite('az000_09', 7)	# 296581-296587
    gotoLabel(191)
    label(192)
    sprite('az611_00', 8)	# 296588-296595
    sprite('az611_01', 8)	# 296596-296603
    sprite('az611_02', 7)	# 296604-296610
    sprite('az611_03', 7)	# 296611-296617
    SFX_0('019_cloth_c')
    sprite('az611_04', 6)	# 296618-296623
    sprite('az611_05', 6)	# 296624-296629
    sprite('az611_06', 6)	# 296630-296635
    SFX_1('baz701pak')
    sprite('az611_07', 6)	# 296636-296641
    sprite('az611_08', 6)	# 296642-296647
    sprite('az611_09', 55)	# 296648-296702
    sprite('az611_10', 6)	# 296703-296708
    ScreenShake(0, 10000)
    SFX_0('100_hit_grap_1')
    Unknown23018(1)
    sprite('az611_11', 32767)	# 296709-329475

@State
def CmnActLose():
    Unknown2004(1, 0)
    sprite('az620_00', 6)	# 1-6
    Unknown36(24)
    Unknown2034(0)
    Unknown2053(0)
    Unknown35()
    sprite('az620_01', 6)	# 7-12
    sprite('az620_02', 6)	# 13-18
    sprite('az620_03', 6)	# 19-24
    sprite('az620_04', 6)	# 25-30
    sprite('az620_05', 6)	# 31-36
    sprite('az620_06', 6)	# 37-42
    Unknown7006('baz404_0', 100, 0, 0, 0, 0, 0, 880435554, 828322864, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('az620_07', 6)	# 43-48
    sprite('az620_08', 6)	# 49-54
    sprite('az620_09', 6)	# 55-60
    sprite('az620_10', 6)	# 61-66
    Unknown23018(1)
    sprite('az620_10ex1', 6)	# 67-72
    sprite('az620_10ex2', 6)	# 73-78
    sprite('az620_11', 32767)	# 79-32845
    loopRest()

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
def EventEntry():
    sprite('az601_00', 32767)	# 1-32767	 **attackbox here**

@State
def EventEntryStart():
    sprite('az601_00', 7)	# 1-7	 **attackbox here**
    sprite('az601_01', 7)	# 8-14	 **attackbox here**
    sprite('az601_02', 7)	# 15-21	 **attackbox here**
    sprite('az601_03', 7)	# 22-28	 **attackbox here**
    sprite('az601_04', 7)	# 29-35	 **attackbox here**
    sprite('az601_05', 7)	# 36-42	 **attackbox here**
    sprite('az601_06', 7)	# 43-49	 **attackbox here**
    sprite('az601_07', 7)	# 50-56	 **attackbox here**
    GFX_1('ef_exhit_sub', 0)
    SFX_0('100_hit_grap_3')
    sprite('az601_08', 7)	# 57-63	 **attackbox here**
    sprite('az601_09', 7)	# 64-70	 **attackbox here**
    sprite('az601_10', 9)	# 71-79	 **attackbox here**
    sprite('az601_11', 7)	# 80-86
    sprite('az601_12', 7)	# 87-93
    sprite('az601_13', 7)	# 94-100
    loopRest()
    enterState('CmnActStand')

@State
def EventChouhatsu():
    sprite('az300_00', 6)	# 1-6
    sprite('az300_01', 6)	# 7-12
    sprite('az300_02', 7)	# 13-19
    sprite('az300_03', 4)	# 20-23
    SFX_3('azse_02')
    sprite('az300_04', 4)	# 24-27	 **attackbox here**
    sprite('az300_05', 4)	# 28-31
    sprite('az300_06', 4)	# 32-35
    sprite('az300_07', 8)	# 36-43
    sprite('az300_08', 6)	# 44-49
    sprite('az300_09', 6)	# 50-55
    sprite('az300_10', 6)	# 56-61
    sprite('az300_11', 6)	# 62-67
    sprite('az300_12', 6)	# 68-73
    sprite('az300_13', 6)	# 74-79
    sprite('az300_08', 8)	# 80-87
    sprite('az300_13', 6)	# 88-93
    sprite('az300_12', 6)	# 94-99
    sprite('az300_11', 6)	# 100-105
    sprite('az300_10', 6)	# 106-111
    sprite('az300_09', 6)	# 112-117
    sprite('az300_14', 6)	# 118-123
    sprite('az300_15', 6)	# 124-129
    sprite('az300_16', 6)	# 130-135
    sprite('az300_00', 6)	# 136-141
    loopRest()
    enterState('CmnActStand')

@State
def EventRound():
    sprite('az615_00', 6)	# 1-6
    sprite('az615_01', 6)	# 7-12
    sprite('az615_02', 6)	# 13-18
    sprite('az615_03', 6)	# 19-24
    sprite('az615_04', 6)	# 25-30
    sprite('az615_05', 6)	# 31-36
    sprite('az615_06', 6)	# 37-42
    sprite('az615_07', 6)	# 43-48
    sprite('az615_08', 6)	# 49-54
    sprite('az615_09', 6)	# 55-60
    sprite('az615_10', 6)	# 61-66
    sprite('az615_11', 6)	# 67-72
    sprite('az615_12', 32767)	# 73-32839

@State
def EventRoundToStand():
    sprite('az615_12', 7)	# 1-7
    sprite('az615_03', 7)	# 8-14
    sprite('az615_02', 7)	# 15-21
    sprite('az615_01', 7)	# 22-28
    sprite('az615_00', 7)	# 29-35
    loopRest()
    enterState('CmnActStand')

@State
def EventWarp():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown2034(0)
        Unknown3032()
    sprite('az000_00', 26)	# 1-26
    GFX_1('story_rc_teni', 103)
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    sprite('az000_00', 1)	# 27-27
    Unknown1000(-500000)
    sprite('null', 32767)	# 28-32794
    loopRest()

@State
def EventWalkOutOpposite():
    Unknown2034(0)
    Unknown2017(0)
    sprite('az003_00ex', 6)	# 1-6
    Unknown2006()
    Unknown2005()
    sprite('az003_01', 6)	# 7-12
    sprite('az003_00', 6)	# 13-18
    sprite('az030_00', 7)	# 19-25
    sprite('az030_01', 7)	# 26-32
    physicsXImpulse(4500)
    sprite('az030_02', 7)	# 33-39
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 7)	# 40-46
    sprite('az030_04', 7)	# 47-53
    sprite('az030_05', 7)	# 54-60
    sprite('az030_06', 7)	# 61-67
    sprite('az030_07', 7)	# 68-74
    sprite('az030_08', 7)	# 75-81
    sprite('az030_09', 7)	# 82-88
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 7)	# 89-95
    sprite('az030_11', 7)	# 96-102
    sprite('az030_12', 7)	# 103-109
    sprite('az030_01', 7)	# 110-116
    sprite('az030_02', 7)	# 117-123
    sprite('az030_03', 7)	# 124-130
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_04', 7)	# 131-137
    sprite('az030_05', 7)	# 138-144
    sprite('az030_06', 7)	# 145-151
    sprite('az030_07', 7)	# 152-158
    sprite('az030_08', 7)	# 159-165
    sprite('az030_09', 7)	# 166-172
    sprite('az030_10', 7)	# 173-179
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_11', 7)	# 180-186
    sprite('az030_12', 7)	# 187-193
    loopRest()

@State
def EventVSHA1():
    sprite('null', 32767)	# 1-32767
    teleportRelativeX(-700000)
    Unknown2034(0)
    Unknown2017(0)
    loopRest()

@State
def EventVSHA2():
    Unknown2034(0)
    sprite('az030_00', 7)	# 1-7
    physicsXImpulse(4500)
    sprite('az030_01', 7)	# 8-14
    sprite('az030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 7)	# 22-28
    sprite('az030_04', 7)	# 29-35
    sprite('az030_05', 7)	# 36-42
    sprite('az030_06', 7)	# 43-49
    sprite('az030_07', 7)	# 50-56
    sprite('az030_08', 7)	# 57-63
    sprite('az030_09', 7)	# 64-70
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 7)	# 71-77
    sprite('az030_11', 7)	# 78-84
    sprite('az030_12', 7)	# 85-91
    sprite('az030_01', 7)	# 92-98
    sprite('az030_02', 7)	# 99-105
    sprite('az030_03', 7)	# 106-112
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_04', 7)	# 113-119
    sprite('az030_05', 7)	# 120-126
    sprite('az030_06', 7)	# 127-133
    sprite('az030_07', 7)	# 134-140
    sprite('az030_08', 7)	# 141-147
    sprite('az030_09', 7)	# 148-154
    sprite('az030_10', 7)	# 155-161
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    sprite('az000_00', 1)	# 162-162
    enterState('CmnActStand')

@State
def EventVSHA3():
    sprite('az602_12', 32767)	# 1-32767
    loopRest()

@State
def EventVSHA4():
    sprite('az601_12', 7)	# 1-7
    sprite('az601_13', 7)	# 8-14
    loopRest()

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventAZTGEntry():
    label(0)
    sprite('az602_00', 1)	# 1-1
    Unknown3038(1)
    teleportRelativeY(500000)
    teleportRelativeY(500000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        gotoLabel(0)
    sprite('az602_00', 2)	# 2-3
    sendToLabelUpon(2, 1)
    Unknown3038(0)
    physicsYImpulse(-40000)
    sprite('az602_00', 6)	# 4-9
    sprite('az602_01', 6)	# 10-15
    label(1)
    sprite('az602_02', 6)	# 16-21
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    Unknown1043()
    ScreenShake(0, 20000)
    GFX_0('rocktest', -1)
    Unknown1084(1)
    SFX_0('019_quake_0')
    sprite('az602_03', 8)	# 22-29
    ScreenShake(0, 20000)
    SFX_0('019_quake_0')
    sprite('az602_04', 8)	# 30-37
    ScreenShake(0, 20000)
    SFX_0('019_quake_0')
    sprite('az602_05', 60)	# 38-97
    ScreenShake(0, 20000)
    SFX_0('019_quake_0')
    sprite('az602_06', 7)	# 98-104
    sprite('az602_07', 7)	# 105-111
    sprite('az602_08', 7)	# 112-118
    sprite('az602_09', 7)	# 119-125
    sprite('az602_10', 7)	# 126-132
    sprite('az602_11', 7)	# 133-139
    sprite('az602_12', 8)	# 140-147
    sprite('az602_13', 8)	# 148-155
    loopRest()
    enterState('CmnActStand')

@State
def EventvsJN1():
    sprite('keep', 32767)	# 1-32767
    Unknown1000(-960000)
    Unknown2034(0)
    Unknown3038(1)

@State
def EventvsJN2():
    Unknown2034(0)
    sprite('az030_00', 7)	# 1-7
    physicsXImpulse(4500)
    sprite('az030_01', 7)	# 8-14
    sprite('az030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 7)	# 22-28
    sprite('az030_04', 7)	# 29-35
    sprite('az030_05', 7)	# 36-42
    sprite('az030_06', 7)	# 43-49
    sprite('az030_07', 7)	# 50-56
    sprite('az030_08', 7)	# 57-63
    sprite('az030_09', 7)	# 64-70
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 7)	# 71-77
    sprite('az030_11', 7)	# 78-84
    sprite('az030_12', 7)	# 85-91
    sprite('az030_01', 7)	# 92-98
    sprite('az030_02', 7)	# 99-105
    sprite('az030_03', 7)	# 106-112
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_04', 7)	# 113-119
    sprite('az030_05', 7)	# 120-126
    sprite('az030_06', 7)	# 127-133
    sprite('az030_07', 7)	# 134-140
    sprite('az030_08', 7)	# 141-147
    sprite('az030_09', 7)	# 148-154
    sprite('az030_10', 7)	# 155-161
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    sprite('az000_00', 1)	# 162-162
    loopRest()
    enterState('CmnActStand')

@State
def EventvsJN3():
    Unknown2034(0)
    Unknown2017(0)
    sprite('az030_00', 7)	# 1-7
    physicsXImpulse(4500)
    sprite('az030_01', 7)	# 8-14
    sprite('az030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 7)	# 22-28
    sprite('az030_04', 7)	# 29-35
    sprite('az030_05', 7)	# 36-42
    sprite('az030_06', 7)	# 43-49
    sprite('az030_07', 7)	# 50-56
    sprite('az030_08', 7)	# 57-63
    sprite('az030_09', 7)	# 64-70
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 7)	# 71-77
    sprite('az030_11', 7)	# 78-84
    sprite('az030_12', 7)	# 85-91
    sprite('az030_01', 7)	# 92-98
    sprite('az030_02', 7)	# 99-105
    sprite('az030_03', 7)	# 106-112
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_04', 7)	# 113-119
    sprite('az030_05', 7)	# 120-126
    sprite('az030_06', 7)	# 127-133
    sprite('az030_07', 7)	# 134-140
    sprite('az030_08', 7)	# 141-147
    sprite('az030_09', 7)	# 148-154
    sprite('az030_10', 7)	# 155-161
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_11', 7)	# 162-168
    sprite('az030_12', 7)	# 169-175
    sprite('az030_01', 7)	# 176-182
    sprite('az030_02', 7)	# 183-189
    sprite('az030_03', 7)	# 190-196
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_04', 7)	# 197-203
    sprite('az030_05', 7)	# 204-210
    sprite('az030_06', 7)	# 211-217
    sprite('az030_07', 7)	# 218-224
    sprite('az030_08', 7)	# 225-231
    sprite('az030_09', 7)	# 232-238
    sprite('az030_10', 7)	# 239-245
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()

@State
def EventBNVsAZ_EntryDrink0():
    Unknown2006()
    Unknown2005()
    label(0)
    sprite('az600_00', 30)	# 1-30
    sprite('az600_01', 9)	# 31-39
    sprite('az600_02', 6)	# 40-45
    sprite('az600_01', 5)	# 46-50
    gotoLabel(0)

@State
def EventBNVsAZ_EntryDrink1():
    sprite('az600_03', 7)	# 1-7
    sprite('az600_04', 7)	# 8-14
    sprite('az600_05', 7)	# 15-21
    sprite('az600_06', 7)	# 22-28
    sprite('az600_07', 7)	# 29-35
    sprite('az600_08', 7)	# 36-42
    sprite('az600_09', 7)	# 43-49
    sprite('az600_10', 40)	# 50-89
    sprite('az600_11', 7)	# 90-96
    GFX_1('azef_entry1', 0)
    SFX_3('azse_13')
    SFX_0('100_hit_grap_1')
    sprite('az600_12', 7)	# 97-103
    sprite('az600_12ex01', 7)	# 104-110
    sprite('az600_12ex02', 7)	# 111-117
    sprite('az600_13', 7)	# 118-124
    sprite('az003_00ex', 6)	# 125-130
    Unknown2006()
    sprite('az003_01', 6)	# 131-136
    sprite('az003_00', 6)	# 137-142
    loopRest()
    enterState('CmnActStand')

@State
def EventTGVSAZTeni():
    sprite('az610_07', 7)	# 1-7
    Unknown3001(0)
    Unknown1043()
    sprite('az610_08', 7)	# 8-14
    Unknown3004(7)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('az610_09', 7)	# 15-21
    sprite('az610_10', 7)	# 22-28
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('az610_11', 7)	# 29-35
    sprite('az610_12', 7)	# 36-42
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    loopRelated(17, 120)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('az610_07', 7)	# 43-49
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('az610_08', 7)	# 50-56
    sprite('az610_09', 7)	# 57-63
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_sl')
    sprite('az610_10', 7)	# 64-70
    sprite('az610_11', 7)	# 71-77
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    sprite('az610_12', 7)	# 78-84
    gotoLabel(0)
    label(1)
    sprite('az610_06', 6)	# 85-90
    sprite('az610_05', 6)	# 91-96
    sprite('az610_04', 6)	# 97-102
    sprite('az610_03', 9)	# 103-111
    sprite('az610_02', 5)	# 112-116
    sprite('az610_01', 7)	# 117-123
    sprite('az610_00', 7)	# 124-130
    enterState('CmnActStand')

@State
def EventBLvsAZWait():

    def upon_IMMEDIATE():
        Unknown1000(-420000)
    label(0)
    sprite('az000_00', 7)	# 1-7
    sprite('az000_01', 7)	# 8-14
    sprite('az000_02', 7)	# 15-21
    sprite('az000_03', 7)	# 22-28
    sprite('az000_04', 7)	# 29-35
    sprite('az000_05', 7)	# 36-42
    sprite('az000_06', 7)	# 43-49
    sprite('az000_07', 7)	# 50-56
    sprite('az000_08', 7)	# 57-63
    sprite('az000_09', 7)	# 64-70
    gotoLabel(0)

@State
def EventBLvsAZAction01():
    sprite('az404_00', 4)	# 1-4
    GFX_0('404tame', -1)
    SFX_3('azse_11')
    sprite('az404_01', 3)	# 5-7
    sprite('az404_02', 3)	# 8-10
    sprite('az404_03', 3)	# 11-13
    sprite('az404_01', 2)	# 14-15
    sprite('az404_02', 2)	# 16-17
    sprite('az404_03', 1)	# 18-18
    sprite('az404_03', 1)	# 19-19
    sprite('az404_01', 3)	# 20-22
    SFX_3('azse_11')
    sprite('az404_02', 3)	# 23-25
    sprite('az404_03', 3)	# 26-28
    sprite('az404_04', 3)	# 29-31
    setInvincible(0)
    Unknown21012('34303474616d650000000000000000000000000000000000000000000000000020000000')
    sprite('az404_05', 3)	# 32-34
    SFX_3('azse_14')
    GFX_0('404swing', -1)
    GFX_0('404nigiyakasi', -1)
    sprite('az404_06', 14)	# 35-48	 **attackbox here**
    Unknown1084(1)
    Unknown21007(22, 32)
    sprite('az404_06', 3)	# 49-51	 **attackbox here**
    physicsXImpulse(20000)
    sprite('az404_07', 3)	# 52-54	 **attackbox here**
    Unknown1019(80)
    sprite('az404_08', 3)	# 55-57	 **attackbox here**
    Unknown1019(60)
    sprite('az404_09', 5)	# 58-62
    Unknown1019(40)
    sprite('az404_10', 5)	# 63-67
    Unknown1019(30)
    sprite('az404_11', 4)	# 68-71
    Unknown1019(30)
    sprite('az404_12', 4)	# 72-75
    physicsXImpulse(0)
    sprite('az404_13', 4)	# 76-79
    sprite('az404_14', 4)	# 80-83
    sprite('az404_15', 4)	# 84-87
    sprite('az404_16', 4)	# 88-91
    sprite('az404_17', 4)	# 92-95
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def EventvsAZvsARFlameOut1():

    def upon_IMMEDIATE():
        Unknown2034(0)
    sprite('az003_00ex', 2)	# 1-2
    Unknown2005()
    sprite('az003_01', 2)	# 3-4
    sprite('az003_00', 2)	# 5-6
    sprite('az030_00', 7)	# 7-13
    physicsXImpulse(2300)
    sprite('az030_01', 7)	# 14-20
    sprite('az030_02', 7)	# 21-27
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 7)	# 28-34
    sprite('az030_04', 7)	# 35-41
    sprite('az030_05', 7)	# 42-48
    sprite('az030_06', 7)	# 49-55
    physicsXImpulse(0)
    label(0)
    sprite('az000_00', 7)	# 56-62
    sprite('az000_01', 7)	# 63-69
    sprite('az000_02', 7)	# 70-76
    sprite('az000_03', 7)	# 77-83
    sprite('az000_04', 7)	# 84-90
    sprite('az000_05', 7)	# 91-97
    sprite('az000_06', 7)	# 98-104
    sprite('az000_07', 7)	# 105-111
    sprite('az000_08', 7)	# 112-118
    sprite('az000_09', 7)	# 119-125
    loopRest()
    gotoLabel(0)

@State
def EventvsAZvsARFlameOut2():

    def upon_IMMEDIATE():
        Unknown2034(0)
    sprite('az030_00', 7)	# 1-7
    physicsXImpulse(2300)
    label(0)
    sprite('az030_01', 7)	# 8-14
    sprite('az030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 7)	# 22-28
    sprite('az030_04', 7)	# 29-35
    sprite('az030_05', 7)	# 36-42
    sprite('az030_06', 7)	# 43-49
    sprite('az030_07', 7)	# 50-56
    sprite('az030_08', 7)	# 57-63
    sprite('az030_09', 7)	# 64-70
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 7)	# 71-77
    sprite('az030_11', 7)	# 78-84
    sprite('az030_12', 7)	# 85-91
    sprite('az030_00', 7)	# 92-98
    gotoLabel(0)
    loopRest()

@State
def EventAZGrowerLoop():
    label(0)
    sprite('az407_02', 6)	# 1-6
    sprite('az407_03', 6)	# 7-12	 **attackbox here**
    sprite('az407_04', 6)	# 13-18	 **attackbox here**
    sprite('az407_05', 6)	# 19-24	 **attackbox here**
    gotoLabel(0)

@State
def EventAZGrowerLoopEnd():
    sprite('az407_02', 4)	# 1-4
    sprite('az407_01', 4)	# 5-8
    sprite('az407_00', 3)	# 9-11
    loopRest()
    enterState('CmnActStand')

@State
def EventvsAZvsKKAction01():

    def upon_IMMEDIATE():
        Unknown2034(0)
    Unknown2037(1)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 0):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > 0):
            sendToLabel(1)
    sprite('az030_00', 7)	# 1-7
    physicsXImpulse(2300)
    label(0)
    sprite('az030_01', 7)	# 8-14
    sprite('az030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 7)	# 22-28
    sprite('az030_04', 7)	# 29-35
    sprite('az030_05', 7)	# 36-42
    sprite('az030_06', 7)	# 43-49
    sprite('az030_07', 7)	# 50-56
    sprite('az030_08', 7)	# 57-63
    sprite('az030_09', 7)	# 64-70
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 7)	# 71-77
    sprite('az030_11', 7)	# 78-84
    sprite('az030_12', 7)	# 85-91
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az030_00', 2)	# 92-93
    physicsXImpulse(0)
    Unknown1000(0)
    loopRest()
    enterState('CmnActStand')

@State
def EventDustAttackLoop():
    sprite('az403_00', 6)	# 1-6
    sprite('az403_01', 6)	# 7-12
    GFX_0('azef_dustattack_hold', -1)
    sprite('az403_02', 6)	# 13-18
    SFX_3('azse_03_loop')
    sprite('az403_03', 4)	# 19-22
    sprite('az403_04', 4)	# 23-26
    sprite('az403_04', 4)	# 27-30
    sprite('az403_02', 4)	# 31-34
    sprite('az403_03', 4)	# 35-38
    sprite('az403_04', 4)	# 39-42
    sprite('az403_02', 4)	# 43-46
    sprite('az403_03', 4)	# 47-50
    sprite('az403_04', 4)	# 51-54
    label(0)
    sprite('az403_02', 4)	# 55-58
    sprite('az403_03', 4)	# 59-62
    SFX_3('azse_03_loop')
    sprite('az403_04', 4)	# 63-66
    sprite('az403_02', 4)	# 67-70
    sprite('az403_03', 4)	# 71-74
    sprite('az403_04', 4)	# 75-78
    sprite('az403_02', 4)	# 79-82
    sprite('az403_03', 4)	# 83-86
    sprite('az403_04', 4)	# 87-90
    loopRest()
    gotoLabel(0)

@State
def EventSuperPunchLoop():
    sprite('az431_00', 3)	# 1-3
    sprite('az431_00', 3)	# 4-6
    sprite('az431_01', 6)	# 7-12
    Unknown2036(122, -1, 0)
    GFX_0('EMB', 0)
    teleportRelativeX(-70000)
    Unknown3029(1)
    sprite('az431_02', 6)	# 13-18
    teleportRelativeX(-40000)
    sprite('az431_03', 6)	# 19-24
    teleportRelativeX(-40000)
    sprite('az431_04', 6)	# 25-30
    teleportRelativeX(-70000)
    sprite('az431_05', 6)	# 31-36
    teleportRelativeX(-70000)
    sprite('az431_06', 5)	# 37-41
    sprite('az431_07', 5)	# 42-46
    sprite('az431_08', 5)	# 47-51
    sprite('az431_09', 5)	# 52-56
    label(0)
    sprite('az431_10', 3)	# 57-59
    sprite('az431_11', 3)	# 60-62
    sprite('az431_12', 3)	# 63-65
    SFX_0('019_quake_1')
    SFX_0('019_quake_1')
    sprite('az431_10', 3)	# 66-68
    sprite('az431_11', 3)	# 69-71
    sprite('az431_12', 3)	# 72-74
    SFX_0('019_quake_1')
    loopRest()
    gotoLabel(0)

@State
def EventSuperPunchLoopEnd():
    sprite('az431_13', 6)	# 1-6
    sprite('az431_14', 6)	# 7-12
    sprite('az431_15', 6)	# 13-18
    GFX_0('402rock1', -1)
    GFX_0('405smoke', -1)
    teleportRelativeX(10000)
    sprite('az431_16', 6)	# 19-24
    teleportRelativeX(10000)
    sprite('az431_17', 4)	# 25-28
    teleportRelativeX(80000)
    Unknown1015(90000)
    sprite('az431_18', 4)	# 29-32
    teleportRelativeX(20000)
    sprite('az431_19', 4)	# 33-36	 **attackbox here**
    Unknown26('405smoke')
    GFX_0('431swing', -1)
    Unknown1019(70)

    def upon_12():
        SFX_0('025_cleanhit_grap')
        SFX_0('025_cleanhit_grap')
    sprite('az431_20', 6)	# 37-42
    Unknown1019(20)
    sprite('az431_21', 6)	# 43-48
    physicsXImpulse(0)
    sprite('az431_22', 6)	# 49-54
    sprite('az431_23', 6)	# 55-60
    sprite('az431_24', 6)	# 61-66
    sprite('az431_25', 6)	# 67-72
    sprite('az431_26', 6)	# 73-78
    sprite('az431_27', 6)	# 79-84
    sprite('az431_28', 6)	# 85-90
    loopRest()
    enterState('CmnActStand')

@State
def EventGrower():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(15000)
        AirPushbackY(36000)
        AirUntechableTime(45)
        Unknown12051(2)
    sprite('az407_00', 1)	# 1-1
    setInvincible(1)
    sprite('az407_01', 1)	# 2-2
    sprite('az407_02', 1)	# 3-3
    sprite('az407_03', 1)	# 4-4	 **attackbox here**
    StartMultihit()
    GFX_0('407aura', -1)
    SFX_3('azse_03')
    sprite('az407_03', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    sprite('az407_03', 2)	# 6-7	 **attackbox here**
    sprite('az407_04', 4)	# 8-11	 **attackbox here**
    sprite('az407_05', 4)	# 12-15	 **attackbox here**
    sprite('az407_02', 4)	# 16-19
    sprite('az407_03', 4)	# 20-23	 **attackbox here**
    sprite('az407_04', 4)	# 24-27	 **attackbox here**
    sprite('az407_05', 4)	# 28-31	 **attackbox here**
    sprite('az407_02', 4)	# 32-35
    sprite('az407_03', 4)	# 36-39	 **attackbox here**
    sprite('az407_04', 4)	# 40-43	 **attackbox here**
    sprite('az407_05', 3)	# 44-46	 **attackbox here**
    sprite('az407_05', 1)	# 47-47	 **attackbox here**
    sprite('az407_02', 4)	# 48-51
    sprite('az407_03', 4)	# 52-55	 **attackbox here**
    sprite('az407_04', 4)	# 56-59	 **attackbox here**
    sprite('az407_05', 4)	# 60-63	 **attackbox here**
    sprite('az407_02', 4)	# 64-67
    sprite('az407_03', 4)	# 68-71	 **attackbox here**
    sprite('az407_04', 4)	# 72-75	 **attackbox here**
    sprite('az407_05', 4)	# 76-79	 **attackbox here**
    sprite('az407_02', 4)	# 80-83
    sprite('az407_03', 4)	# 84-87	 **attackbox here**
    sprite('az407_04', 4)	# 88-91	 **attackbox here**
    sprite('az407_05', 4)	# 92-95	 **attackbox here**
    sprite('az407_02', 4)	# 96-99
    sprite('az407_03', 4)	# 100-103	 **attackbox here**
    sprite('az407_02', 4)	# 104-107
    sprite('az407_03', 4)	# 108-111	 **attackbox here**
    sprite('az407_04', 4)	# 112-115	 **attackbox here**
    sprite('az407_05', 4)	# 116-119	 **attackbox here**
    sprite('az407_02', 4)	# 120-123
    sprite('az407_03', 4)	# 124-127	 **attackbox here**
    sprite('az407_04', 4)	# 128-131	 **attackbox here**
    sprite('az407_05', 4)	# 132-135	 **attackbox here**
    sprite('az407_02', 4)	# 136-139
    sprite('az407_03', 4)	# 140-143	 **attackbox here**
    sprite('az407_04', 4)	# 144-147	 **attackbox here**
    sprite('az407_05', 4)	# 148-151	 **attackbox here**
    Unknown23027()
    sprite('az407_04', 4)	# 152-155	 **attackbox here**
    Unknown21012('343037617572610000000000000000000000000000000000000000000000000020000000')
    sprite('az407_05', 4)	# 156-159	 **attackbox here**
    clearUponHandler(24)
    sprite('az407_02', 4)	# 160-163
    Unknown21012('343037617572610000000000000000000000000000000000000000000000000020000000')
    setInvincible(0)
    Unknown7015()
    sprite('az407_01', 3)	# 164-166
    sprite('az407_01', 1)	# 167-167
    sprite('az407_00', 3)	# 168-170

@State
def EventReaction():
    sprite('az001_00', 6)	# 1-6
    sprite('az001_01', 6)	# 7-12
    sprite('az001_02', 6)	# 13-18
    sprite('az001_03', 6)	# 19-24
    sprite('az001_04', 6)	# 25-30
    sprite('az001_05', 6)	# 31-36
    sprite('az001_06', 6)	# 37-42
    sprite('az001_03', 6)	# 43-48
    sprite('az001_04', 6)	# 49-54
    sprite('az001_05', 6)	# 55-60
    sprite('az001_06', 6)	# 61-66
    sprite('az001_01', 6)	# 67-72
    sprite('az001_00', 6)	# 73-78
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_grow2Start():
    sprite('az610_00', 6)	# 1-6
    sprite('az610_01', 6)	# 7-12
    sprite('az610_02', 6)	# 13-18
    sprite('az610_03', 9)	# 19-27
    sprite('az610_04', 5)	# 28-32
    sprite('az610_05', 7)	# 33-39
    sprite('az610_06', 7)	# 40-46
    GFX_0('610aura', -1)
    sprite('az610_07', 7)	# 47-53
    Unknown3029(1)
    Unknown3069(0)
    SFX_3('azse_15')
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_08', 7)	# 54-60
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_09', 7)	# 61-67
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_10', 7)	# 68-74
    SFX_3('azse_15')
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_11', 7)	# 75-81
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('az610_12', 7)	# 82-88
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    label(0)
    sprite('az610_07', 7)	# 89-95
    SFX_3('azse_15')
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('az610_08', 7)	# 96-102
    ScreenShake(0, 4000)
    sprite('az610_09', 7)	# 103-109
    ScreenShake(0, 4000)
    sprite('az610_10', 7)	# 110-116
    SFX_3('azse_15')
    ScreenShake(0, 4000)
    sprite('az610_11', 7)	# 117-123
    ScreenShake(0, 4000)
    sprite('az610_12', 7)	# 124-130
    ScreenShake(0, 4000)
    loopRest()
    gotoLabel(0)

@State
def Act2Event_grow2End():
    sprite('az610_06', 6)	# 1-6
    Unknown3029(0)
    Unknown21012('363130617572610000000000000000000000000000000000000000000000000020000000')
    sprite('az610_05', 6)	# 7-12
    Unknown8000(100, 1, 1)
    sprite('az602_07', 6)	# 13-18
    sprite('az602_08', 6)	# 19-24
    sprite('az602_09', 6)	# 25-30
    sprite('az602_10', 6)	# 31-36
    sprite('az602_11', 6)	# 37-42
    sprite('az602_12', 6)	# 43-48
    sprite('az602_13', 6)	# 49-54
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_NoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    loopRest()

@State
def Act2Event_tyakuti():
    sprite('az602_00', 2)	# 1-2
    Unknown1000(-260000)
    teleportRelativeY(700000)
    Unknown3038(0)
    sendToLabelUpon(2, 1)
    physicsYImpulse(-60000)
    setGravity(2500)
    label(0)
    sprite('az602_00', 6)	# 3-8
    sprite('az602_01', 6)	# 9-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az602_02', 7)	# 15-21
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    ScreenShake(0, 20000)
    GFX_0('rocktest', -1)
    SFX_3('azse_07')
    Unknown1084(1)
    sprite('az602_03', 7)	# 22-28
    sprite('az602_04', 7)	# 29-35
    sprite('az602_05', 7)	# 36-42
    sprite('az602_06', 7)	# 43-49
    sprite('az602_07', 7)	# 50-56
    sprite('az602_08', 7)	# 57-63
    sprite('az602_09', 7)	# 64-70
    sprite('az602_10', 7)	# 71-77
    sprite('az602_11', 7)	# 78-84
    sprite('az602_12', 7)	# 85-91
    sprite('az602_13', 7)	# 92-98
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Chouhatsu():
    sprite('az300_00', 7)	# 1-7
    sprite('az300_01', 7)	# 8-14
    sprite('az300_02', 7)	# 15-21
    sprite('az300_03', 7)	# 22-28
    SFX_3('azse_02')
    sprite('az300_04', 7)	# 29-35	 **attackbox here**
    sprite('az300_05', 7)	# 36-42
    sprite('az300_06', 7)	# 43-49
    sprite('az300_07', 7)	# 50-56
    sprite('az300_08', 7)	# 57-63
    sprite('az300_09', 7)	# 64-70
    sprite('az300_10', 7)	# 71-77
    sprite('az300_11', 7)	# 78-84
    sprite('az300_12', 7)	# 85-91
    sprite('az300_13', 7)	# 92-98
    sprite('az300_14', 7)	# 99-105
    sprite('az300_15', 7)	# 106-112
    sprite('az300_16', 7)	# 113-119
    sprite('az300_00', 7)	# 120-126
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_RoundWin1():
    sprite('az615_00', 6)	# 1-6
    sprite('az615_01', 6)	# 7-12
    sprite('az615_02', 6)	# 13-18
    sprite('az615_03', 6)	# 19-24
    sprite('az615_04', 6)	# 25-30
    sprite('az615_05', 6)	# 31-36
    sprite('az615_06', 6)	# 37-42
    sprite('az615_07', 6)	# 43-48
    sprite('az615_08', 6)	# 49-54
    sprite('az615_09', 6)	# 55-60
    sprite('az615_10', 6)	# 61-66
    sprite('az615_11', 6)	# 67-72
    sprite('az615_12', 32767)	# 73-32839

@State
def Act2Event_RoundWin2():
    sprite('az615_12', 7)	# 1-7
    sprite('az615_03', 7)	# 8-14
    sprite('az615_02', 7)	# 15-21
    sprite('az615_01', 7)	# 22-28
    sprite('az615_00', 7)	# 29-35
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_TimeUp():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        Unknown2004(1, 0)
    sprite('az620_00', 6)	# 1-6
    sprite('az620_01', 6)	# 7-12
    sprite('az620_02', 6)	# 13-18
    sprite('az620_03', 6)	# 19-24
    sprite('az620_04', 6)	# 25-30
    sprite('az620_05', 6)	# 31-36
    sprite('az620_06', 6)	# 37-42
    sprite('az620_07', 6)	# 43-48
    sprite('az620_08', 6)	# 49-54
    sprite('az620_09', 6)	# 55-60
    sprite('az620_10', 6)	# 61-66
    sprite('az620_10ex1', 6)	# 67-72
    sprite('az620_10ex2', 6)	# 73-78
    sprite('az620_11', 32767)	# 79-32845
    loopRest()

@State
def Act2Event_vhvsaz_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('az070_00', 15)	# 1-15
    Unknown4052()
    Unknown4045('65665f6869746d7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_1')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('az070_01', 4)	# 16-19
    sprite('az070_02', 4)	# 20-23
    sprite('az070_03', 32767)	# 24-32790
    loopRest()

@State
def Act2Event_vhvsaz_01():
    sprite('az070_10', 5)	# 1-5
    sprite('az070_11', 5)	# 6-10
    sprite('az070_12', 5)	# 11-15
    sprite('az070_13', 5)	# 16-20
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ptvsaz_00():

    def upon_IMMEDIATE():
        teleportRelativeX(160000)
        Unknown2004(1, 0)
    sprite('keep', 1)	# 1-1
    GFX_0('Act2Event_Yure', -1)
    sprite('keep', 32767)	# 2-32768
    loopRest()

@State
def Act2Event_kgvsaz_00():
    sprite('az404_08', 10)	# 1-10	 **attackbox here**
    sprite('az404_09', 5)	# 11-15
    sprite('az404_10', 5)	# 16-20
    sprite('az404_11', 4)	# 21-24
    sprite('az404_12', 4)	# 25-28
    sprite('az404_13', 4)	# 29-32
    sprite('az404_14', 4)	# 33-36
    sprite('az404_15', 4)	# 37-40
    sprite('az404_16', 4)	# 41-44
    sprite('az404_17', 4)	# 45-48
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_kgvsaz_01():
    sprite('keep', 2)	# 1-2
    sprite('az003_00ex', 5)	# 3-7
    Unknown2005()
    sprite('az003_01', 5)	# 8-12
    sprite('az003_00', 5)	# 13-17
    label(0)
    sprite('az000_00', 7)	# 18-24
    sprite('az000_01', 7)	# 25-31
    sprite('az000_02', 7)	# 32-38
    sprite('az000_03', 7)	# 39-45
    sprite('az000_04', 7)	# 46-52
    sprite('az000_05', 7)	# 53-59
    sprite('az000_06', 7)	# 60-66
    sprite('az000_07', 7)	# 67-73
    sprite('az000_08', 7)	# 74-80
    sprite('az000_09', 7)	# 81-87
    loopRest()
    gotoLabel(0)

@State
def Act2Event_kgvsaz_02():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('az030_00', 8)	# 1-8
    physicsXImpulse(5000)
    Unknown2037(2)
    label(0)
    sprite('az030_01', 8)	# 9-16
    Unknown2038(-1)
    sprite('az030_02', 8)	# 17-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 8)	# 25-32
    sprite('az030_04', 8)	# 33-40
    sprite('az030_05', 8)	# 41-48
    sprite('az030_06', 8)	# 49-56
    sprite('az030_07', 8)	# 57-64
    sprite('az030_08', 8)	# 65-72
    sprite('az030_09', 8)	# 73-80
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 8)	# 81-88
    sprite('az030_11', 8)	# 89-96
    sprite('az030_12', 8)	# 97-104
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('null', 32767)	# 105-32871
    Unknown1084(1)
    Unknown3038(1)
    loopRest()

@State
def Act2Event_kgvsaz_03():

    def upon_IMMEDIATE():
        Unknown3038(1)
    sprite('null', 1)	# 1-1
    GFX_0('Act2Event_Yure', -1)
    sprite('null', 32767)	# 2-32768
    loopRest()

@State
def Act2Event_hbvsaz_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        Unknown2004(1, 0)
    sprite('az404_08', 10)	# 1-10	 **attackbox here**
    sprite('az404_09', 5)	# 11-15
    sprite('az404_10', 5)	# 16-20
    sprite('az404_11', 4)	# 21-24
    sprite('az404_12', 4)	# 25-28
    sprite('az404_13', 4)	# 29-32
    sprite('az404_14', 4)	# 33-36
    sprite('az404_15', 4)	# 37-40
    sprite('az404_16', 4)	# 41-44
    sprite('az404_17', 4)	# 45-48
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_hbvsaz_01():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
    sprite('az620_00', 6)	# 1-6
    sprite('az620_01', 6)	# 7-12
    sprite('az620_02', 6)	# 13-18
    sprite('az620_03', 6)	# 19-24
    sprite('az620_04', 6)	# 25-30
    sprite('az620_05', 6)	# 31-36
    sprite('az620_06', 6)	# 37-42
    sprite('az620_07', 6)	# 43-48
    sprite('az620_08', 6)	# 49-54
    sprite('az620_09', 6)	# 55-60
    sprite('az620_10', 6)	# 61-66
    sprite('az620_10ex1', 6)	# 67-72
    sprite('az620_10ex2', 6)	# 73-78
    sprite('az620_11', 32767)	# 79-32845
    loopRest()

@State
def Act2Event_azvsny_00():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_0('Act2Event_Bang', -1)
        Unknown38(11, 1)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_azvsny_01():

    def upon_IMMEDIATE():
        Unknown3038(1)
    sprite('null', 2)	# 1-2
    Unknown21007(11, 32)
    sprite('null', 32767)	# 3-32769
    loopRest()

@State
def Act2Event_azvsny_02():

    def upon_IMMEDIATE():
        Unknown1000(-200000)
        teleportRelativeY(700000)
        Unknown3038(0)
        sendToLabelUpon(2, 1)

        def upon_33():
            Unknown21007(11, 33)

        def upon_34():
            Unknown21007(11, 34)
    sprite('az602_00', 2)	# 1-2
    physicsYImpulse(-60000)
    setGravity(2500)
    label(0)
    sprite('az602_00', 6)	# 3-8
    sprite('az602_01', 6)	# 9-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az602_02', 7)	# 15-21
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    ScreenShake(0, 20000)
    GFX_0('rocktest', -1)
    SFX_3('azse_07')
    Unknown1084(1)
    sprite('az602_03', 7)	# 22-28
    sprite('az602_04', 7)	# 29-35
    sprite('az602_05', 7)	# 36-42
    sprite('az602_06', 7)	# 43-49
    sprite('az602_07', 7)	# 50-56
    sprite('az602_08', 7)	# 57-63
    sprite('az602_09', 7)	# 64-70
    sprite('az602_10', 7)	# 71-77
    sprite('az602_11', 7)	# 78-84
    sprite('az602_12', 7)	# 85-91
    sprite('az602_13', 7)	# 92-98
    loopRest()
    label(9)
    sprite('az000_00', 7)	# 99-105
    sprite('az000_01', 7)	# 106-112
    sprite('az000_02', 7)	# 113-119
    sprite('az000_03', 7)	# 120-126
    sprite('az000_04', 7)	# 127-133
    sprite('az000_05', 7)	# 134-140
    sprite('az000_06', 7)	# 141-147
    sprite('az000_07', 7)	# 148-154
    sprite('az000_08', 7)	# 155-161
    sprite('az000_09', 7)	# 162-168
    loopRest()
    gotoLabel(9)

@State
def Act2Event_azvsny_03():
    sprite('az041_00', 4)	# 1-4
    Unknown2019(500)
    sprite('az041_01', 4)	# 5-8
    sprite('az041_02', 4)	# 9-12
    sprite('az041_03', 18)	# 13-30
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    Unknown1047(-6500)
    ScreenShake(5000, 20000)
    sprite('az041_02', 21)	# 31-51
    sprite('az041_01', 3)	# 52-54
    sprite('az041_00', 3)	# 55-57
    Unknown1084(1)
    Unknown1000(-260000)
    Unknown2019(0)
    loopRest()
    enterState('CmnActStand')

@State
def EventAct2TKVSAZ01():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2034(0)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        Unknown1000(-50000)
        setInvincible(1)
    label(0)
    sprite('az000_00', 7)	# 1-7
    sprite('az000_01', 7)	# 8-14
    sprite('az000_02', 7)	# 15-21
    sprite('az000_03', 7)	# 22-28
    sprite('az000_04', 7)	# 29-35
    sprite('az000_05', 7)	# 36-42
    sprite('az000_06', 7)	# 43-49
    sprite('az000_07', 7)	# 50-56
    sprite('az000_08', 7)	# 57-63
    sprite('az000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az211_00', 2)	# 71-72
    Unknown21007(22, 32)
    sprite('az211_01', 2)	# 73-74
    sprite('az211_02', 2)	# 75-76
    sprite('az211_03', 2)	# 77-78
    SFX_0('005_swing_grap_2_2')
    sprite('az211_04', 2)	# 79-80	 **attackbox here**
    sprite('az211_05', 4)	# 81-84	 **attackbox here**
    sprite('az211_06', 2)	# 85-86
    sprite('az211_07', 4)	# 87-90
    physicsXImpulse(-1000)
    teleportRelativeX(-24000)
    sprite('az211_08', 4)	# 91-94
    sprite('az211_09', 1)	# 95-95
    sprite('az211_09', 3)	# 96-98
    physicsXImpulse(0)
    sprite('az211_10', 4)	# 99-102
    sprite('az211_11', 4)	# 103-106
    sprite('az211_12', 4)	# 107-110
    sprite('az211_13', 4)	# 111-114
    sprite('az211_14', 4)	# 115-118
    sprite('az211_15', 3)	# 119-121
    setInvincible(0)
    Unknown1084(1)
    sprite('az000_00', 1)	# 122-122
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('az000_00', 6)	# 123-128
    sprite('az000_01', 7)	# 129-135
    SFX_1('az546')
    Unknown23018(1)
    sprite('az000_02', 7)	# 136-142
    sprite('az000_03', 7)	# 143-149
    sprite('az000_04', 7)	# 150-156
    loopRest()
    enterState('CmnActStand')

@State
def EventAct2TKVSAZ02():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2034(0)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        Unknown1000(-100000)
        setInvincible(1)
    label(0)
    sprite('az000_00', 7)	# 1-7
    sprite('az000_01', 7)	# 8-14
    sprite('az000_02', 7)	# 15-21
    sprite('az000_03', 7)	# 22-28
    sprite('az000_04', 7)	# 29-35
    sprite('az000_05', 7)	# 36-42
    sprite('az000_06', 7)	# 43-49
    sprite('az000_07', 7)	# 50-56
    sprite('az000_08', 7)	# 57-63
    sprite('az000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az211_00', 2)	# 71-72
    Unknown21007(22, 32)
    sprite('az211_01', 2)	# 73-74
    sprite('az211_02', 2)	# 75-76
    sprite('az211_03', 2)	# 77-78
    SFX_0('005_swing_grap_2_2')
    sprite('az211_04', 2)	# 79-80	 **attackbox here**
    sprite('az211_05', 4)	# 81-84	 **attackbox here**
    sprite('az211_06', 2)	# 85-86
    sprite('az211_07', 4)	# 87-90
    physicsXImpulse(-4000)
    teleportRelativeX(-28000)
    sprite('az211_08', 4)	# 91-94
    sprite('az211_09', 3)	# 95-97
    physicsXImpulse(0)
    sprite('az211_10', 3)	# 98-100
    sprite('az211_11', 3)	# 101-103
    sprite('az211_12', 3)	# 104-106
    sprite('az211_13', 3)	# 107-109
    sprite('az211_14', 3)	# 110-112
    sprite('az211_15', 3)	# 113-115
    setInvincible(0)
    Unknown1084(1)
    enterState('EventVanishingAttack')

@State
def EventVanishingAttack():
    sprite('az404_00', 4)	# 1-4
    teleportRelativeX(-100000)
    SFX_3('azse_11')
    sprite('az404_01', 3)	# 5-7
    SFX_3('azse_11')
    sprite('az404_02', 3)	# 8-10
    sprite('az404_03', 3)	# 11-13
    sprite('az404_04', 3)	# 14-16
    sprite('az404_05', 3)	# 17-19
    SFX_3('azse_14')
    GFX_0('404swing', -1)
    GFX_0('404nigiyakasi', -1)
    sprite('az404_06', 3)	# 20-22	 **attackbox here**
    physicsXImpulse(52000)
    sprite('az404_07', 3)	# 23-25	 **attackbox here**
    Unknown1019(80)
    sprite('az404_08', 3)	# 26-28	 **attackbox here**
    Unknown1019(60)
    sprite('az404_09', 5)	# 29-33
    Unknown1019(40)
    sprite('az404_10', 5)	# 34-38
    Unknown1019(30)
    sprite('az404_11', 4)	# 39-42
    Unknown1019(30)
    sprite('az404_12', 4)	# 43-46
    physicsXImpulse(0)
    sprite('az404_13', 4)	# 47-50
    sprite('az404_14', 4)	# 51-54
    sprite('az404_15', 4)	# 55-58
    sprite('az404_16', 4)	# 59-62
    sprite('az404_17', 4)	# 63-66
    loopRest()
    sprite('az003_00ex', 6)	# 67-72
    Unknown2006()
    sprite('az003_01', 6)	# 73-78
    sprite('az003_00', 6)	# 79-84
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_2mkuraiWalk():
    sprite('az030_00', 5)	# 1-5
    physicsXImpulse(2300)
    sprite('az030_01', 5)	# 6-10
    sprite('az030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 5)	# 16-20
    sprite('az030_04', 5)	# 21-25
    sprite('az030_05', 5)	# 26-30
    sprite('az030_06', 5)	# 31-35
    sprite('az030_07', 5)	# 36-40
    sprite('az030_08', 5)	# 41-45
    sprite('az030_09', 5)	# 46-50
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 5)	# 51-55
    sprite('az030_11', 5)	# 56-60
    sprite('az030_12', 5)	# 61-65
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventWalkLoop():
    sprite('az030_00', 8)	# 1-8
    physicsXImpulse(5000)
    Unknown2017(0)
    Unknown2034(0)
    label(0)
    sprite('az030_01', 8)	# 9-16
    sprite('az030_02', 8)	# 17-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_03', 8)	# 25-32
    sprite('az030_04', 8)	# 33-40
    sprite('az030_05', 8)	# 41-48
    sprite('az030_06', 8)	# 49-56
    sprite('az030_07', 8)	# 57-64
    sprite('az030_08', 8)	# 65-72
    sprite('az030_09', 8)	# 73-80
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('az030_10', 8)	# 81-88
    sprite('az030_11', 8)	# 89-96
    sprite('az030_12', 8)	# 97-104
    loopRest()
    gotoLabel(0)

@State
def Act2EventGrow():
    label(1)
    sprite('az407_00', 1)	# 1-1
    setInvincible(1)
    sendToLabelUpon(32, 3)

    def upon_STATE_END():
        Unknown7015()
    sprite('az407_01', 1)	# 2-2
    sprite('az407_02', 1)	# 3-3
    sprite('az407_03', 1)	# 4-4	 **attackbox here**
    GFX_0('407aura', -1)
    SFX_3('azse_03')
    sprite('az407_03', 1)	# 5-5	 **attackbox here**
    sprite('az407_03', 2)	# 6-7	 **attackbox here**
    sprite('az407_04', 4)	# 8-11	 **attackbox here**
    sprite('az407_05', 4)	# 12-15	 **attackbox here**
    loopRest()
    label(2)
    sprite('az407_02', 4)	# 16-19
    GFX_0('407Kyushu', -1)
    sprite('az407_03', 4)	# 20-23	 **attackbox here**
    sprite('az407_04', 4)	# 24-27	 **attackbox here**
    sprite('az407_05', 4)	# 28-31	 **attackbox here**
    sprite('az407_02', 4)	# 32-35
    sprite('az407_03', 4)	# 36-39	 **attackbox here**
    sprite('az407_04', 4)	# 40-43	 **attackbox here**
    sprite('az407_05', 4)	# 44-47	 **attackbox here**
    sprite('az407_02', 4)	# 48-51
    GFX_0('407Kyushu', -1)
    sprite('az407_03', 4)	# 52-55	 **attackbox here**
    sprite('az407_04', 4)	# 56-59	 **attackbox here**
    sprite('az407_05', 4)	# 60-63	 **attackbox here**
    sprite('az407_02', 4)	# 64-67
    sprite('az407_03', 4)	# 68-71	 **attackbox here**
    sprite('az407_04', 4)	# 72-75	 **attackbox here**
    sprite('az407_05', 4)	# 76-79	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('az407_02', 4)	# 80-83
    sprite('az407_03', 4)	# 84-87	 **attackbox here**
    sprite('az407_04', 4)	# 88-91	 **attackbox here**
    sprite('az407_05', 4)	# 92-95	 **attackbox here**
    Unknown21012('343037617572610000000000000000000000000000000000000000000000000020000000')
    sprite('az407_01', 3)	# 96-98
    sprite('az407_00', 3)	# 99-101
    loopRest()
    enterState('CmnActStand')

@State
def Act2_azvsrl_DustAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown23022(1)
    sprite('az403_00', 3)	# 1-3
    sprite('az403_01', 3)	# 4-6
    sprite('az403_02', 3)	# 7-9
    SFX_3('azse_03_loop')
    sprite('az403_03', 3)	# 10-12
    sprite('az403_04', 3)	# 13-15
    sprite('az403_02', 3)	# 16-18
    sprite('az403_03', 3)	# 19-21
    sprite('az403_04', 3)	# 22-24
    sprite('az403_02', 3)	# 25-27
    sprite('az403_03', 3)	# 28-30
    sprite('az403_04', 3)	# 31-33
    sprite('az403_02', 3)	# 34-36
    sprite('az403_03', 3)	# 37-39
    sprite('az403_04', 3)	# 40-42
    sprite('az403_02', 3)	# 43-45
    sprite('az403_05', 3)	# 46-48
    setInvincible(0)
    Unknown26('azef_dustattack_hold')
    sprite('az403_06', 3)	# 49-51
    sprite('az403_07', 3)	# 52-54
    physicsXImpulse(6500)
    sprite('az403_08', 2)	# 55-56	 **attackbox here**
    StartMultihit()
    GFX_0('403swing', -1)
    SFX_3('azse_14')
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    sprite('az403_09', 5)	# 57-61	 **attackbox here**
    GFX_0('Eventoffset_Sosai', 0)
    Unknown1019(20)
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    sprite('az403_10', 3)	# 62-64	 **attackbox here**
    physicsXImpulse(0)
    sprite('az403_11', 3)	# 65-67
    sprite('az403_12', 3)	# 68-70
    sprite('az403_11', 3)	# 71-73
    sprite('az403_12', 3)	# 74-76
    sprite('az403_11', 3)	# 77-79
    sprite('az403_12', 3)	# 80-82
    sprite('az403_11', 3)	# 83-85
    sprite('az403_12', 3)	# 86-88
    sprite('az403_13', 3)	# 89-91
    sprite('az403_14', 3)	# 92-94
    sprite('az403_15', 3)	# 95-97
    sprite('az403_16', 3)	# 98-100

@State
def Act2Event_tyakuti_azvsrl():
    sprite('az602_00', 2)	# 1-2
    Unknown1000(-299000)
    teleportRelativeY(700000)
    Unknown3038(0)
    sendToLabelUpon(2, 1)
    physicsYImpulse(-60000)
    setGravity(2500)
    label(0)
    sprite('az602_00', 6)	# 3-8
    sprite('az602_01', 6)	# 9-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az602_02', 7)	# 15-21
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    ScreenShake(0, 20000)
    GFX_0('rocktest', -1)
    SFX_3('azse_07')
    Unknown1084(1)
    sprite('az602_03', 7)	# 22-28
    sprite('az602_04', 7)	# 29-35
    sprite('az602_05', 7)	# 36-42
    sprite('az602_06', 7)	# 43-49
    sprite('az602_07', 7)	# 50-56
    sprite('az602_08', 7)	# 57-63
    sprite('az602_09', 7)	# 64-70
    sprite('az602_10', 7)	# 71-77
    sprite('az602_11', 7)	# 78-84
    sprite('az602_12', 7)	# 85-91
    sprite('az602_13', 7)	# 92-98
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsar_00():
    sprite('az602_00', 2)	# 1-2
    Unknown1000(-260000)
    teleportRelativeY(700000)
    Unknown3038(0)
    sendToLabelUpon(2, 1)
    physicsYImpulse(-60000)
    setGravity(2500)
    label(0)
    sprite('az602_00', 6)	# 3-8
    sprite('az602_01', 6)	# 9-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('az602_02', 17)	# 15-31
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown8001(3, 0)
    ScreenShake(0, 20000)
    GFX_0('rocktest', -1)
    SFX_3('azse_07')
    Unknown1084(1)
    Unknown21007(22, 32)
    sprite('az602_03', 7)	# 32-38
    sprite('az602_04', 7)	# 39-45
    sprite('az602_05', 7)	# 46-52
    sprite('az602_06', 7)	# 53-59
    sprite('az602_07', 7)	# 60-66
    sprite('az602_08', 7)	# 67-73
    sprite('az602_09', 7)	# 74-80
    sprite('az602_10', 7)	# 81-87
    sprite('az602_11', 7)	# 88-94
    sprite('az602_12', 7)	# 95-101
    sprite('az602_13', 7)	# 102-108
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsar_01():
    sprite('az202_00', 3)	# 1-3
    sprite('az202_01', 3)	# 4-6
    teleportRelativeX(-43000)
    sprite('az202_02', 3)	# 7-9
    teleportRelativeX(-37000)
    sprite('az202_03', 3)	# 10-12
    sprite('az202_04', 2)	# 13-14
    SFX_0('005_swing_grap_2_2')
    sprite('az202_05', 13)	# 15-27	 **attackbox here**
    teleportRelativeX(75000)
    Unknown21007(22, 32)
    sprite('az202_06', 3)	# 28-30	 **attackbox here**
    sprite('az202_07', 2)	# 31-32
    teleportRelativeX(-50000)
    sprite('az202_08', 2)	# 33-34
    sprite('az202_09', 3)	# 35-37
    teleportRelativeX(-20000)
    sprite('az202_10', 3)	# 38-40
    teleportRelativeX(20000)
    sprite('az202_11', 2)	# 41-42
    teleportRelativeX(40000)
    sprite('az202_11', 1)	# 43-43
    sprite('az202_12', 3)	# 44-46
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsar_02():

    def upon_IMMEDIATE():

        def upon_32():

            def upon_3():
                if (SLOT_19 < 350000):
                    clearUponHandler(3)
                    sendToLabel(1)
    sprite('az615_12', 32767)	# 1-32767
    label(1)
    sprite('az615_12', 2)	# 32768-32769
    sprite('az615_02', 2)	# 32770-32771
    sprite('az615_01', 2)	# 32772-32773
    sprite('az615_00', 2)	# 32774-32775
    sprite('az203_00', 2)	# 32776-32777
    sprite('az203_01', 2)	# 32778-32779
    sprite('az203_02', 2)	# 32780-32781
    physicsXImpulse(6000)
    physicsYImpulse(16000)
    setGravity(3250)
    sprite('az203_03', 2)	# 32782-32783
    sprite('az203_04', 2)	# 32784-32785
    GFX_1('ef_smokej', 0)
    Unknown1019(80)
    sprite('az203_05', 2)	# 32786-32787
    sprite('az203_06', 2)	# 32788-32789
    SFX_0('005_swing_grap_2_2')
    teleportRelativeX(30000)
    physicsXImpulse(0)
    sprite('az203_07', 3)	# 32790-32792	 **attackbox here**
    GFX_1('azef_206smoke_01', 3)
    GFX_0('203swing', -1)
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    SFX_0('209_down_normal_0')
    Unknown21007(22, 32)
    SFX_3('azse_01')
    SFX_3('azse_01')
    GFX_0('weakhit00', -1)
    Unknown36(1)
    Unknown1086(22)
    Unknown35()
    sprite('az203_08', 3)	# 32793-32795
    GFX_1('azef_blood_01', 0)
    GFX_1('azef_blood_01', 1)
    GFX_1('azef_blood_01', 2)
    sprite('az203_09', 3)	# 32796-32798
    sprite('az203_10', 3)	# 32799-32801
    sprite('az203_11', 3)	# 32802-32804
    sprite('az203_12', 2)	# 32805-32806
    sprite('az203_13', 2)	# 32807-32808
    sprite('az203_14', 2)	# 32809-32810
    sprite('az203_15', 2)	# 32811-32812
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsar_03():

    def upon_IMMEDIATE():
        physicsXImpulse(5000)
        Unknown2019(500)

        def upon_3():
            if (SLOT_19 < 150000):
                clearUponHandler(3)
                sendToLabel(1)
label(0)
sprite('az030_01', 8)	# 1-8
sprite('az030_02', 8)	# 9-16
SFX_FOOTSTEP_(100, 1, 1)
sprite('az030_03', 8)	# 17-24
sprite('az030_04', 8)	# 25-32
sprite('az030_05', 8)	# 33-40
sprite('az030_06', 8)	# 41-48
sprite('az030_07', 8)	# 49-56
sprite('az030_08', 8)	# 57-64
sprite('az030_09', 8)	# 65-72
SFX_FOOTSTEP_(100, 1, 1)
sprite('az030_10', 8)	# 73-80
sprite('az030_11', 8)	# 81-88
sprite('az030_12', 8)	# 89-96
loopRest()
gotoLabel(0)
label(1)
sprite('az310_00', 3)	# 97-99
Unknown1084(1)
sprite('az310_01', 2)	# 100-101
SFX_0('005_swing_grap_2_2')
sprite('az310_01', 1)	# 102-102
Unknown21007(22, 32)
Unknown2019(-1000)
sprite('az310_02', 2)	# 103-104	 **attackbox here**
sprite('az310_02', 1)	# 105-105	 **attackbox here**
Unknown21007(22, 33)
sprite('az311_00', 2)	# 106-107
SFX_0('107_throw_catch')
sprite('az311_00', 1)	# 108-108
Unknown21007(22, 34)
sprite('az311_01', 32767)	# 109-32875
loopRest()
endState()

@State
def Act3Event_azvsbn_00():

    def upon_IMMEDIATE():
        GFX_0('Act3Event_ar', 100)
        Unknown38(11, 1)
        teleportRelativeX(120000)
    sprite('keep', 1)	# 1-1
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsbn_01():
    sprite('az003_00ex', 3)	# 1-3
    Unknown2005()
    sprite('az003_01', 3)	# 4-6
    sprite('az003_00', 3)	# 7-9
    sprite('az406_00', 3)	# 10-12
    sprite('az406_01', 3)	# 13-15
    sprite('az406_02', 3)	# 16-18
    sprite('az406_03', 3)	# 19-21
    sprite('az401_00', 2)	# 22-23
    teleportRelativeX(10000)
    sprite('az401_01', 3)	# 24-26
    physicsXImpulse(15000)
    sprite('az401_02', 2)	# 27-28
    SFX_0('005_swing_grap_2_2')
    SFX_0('005_swing_grap_2_2')
    Unknown1019(70)
    sprite('az401_03ex', 13)	# 29-41	 **attackbox here**
    GFX_0('401swing', -1)
    Unknown1019(30)
    Unknown21007(11, 32)
    sprite('az401_04', 6)	# 42-47
    physicsXImpulse(0)
    sprite('az401_05', 4)	# 48-51
    sprite('az401_06', 4)	# 52-55
    sprite('az401_07', 3)	# 56-58
    sprite('az401_08', 3)	# 59-61
    sprite('az401_09', 2)	# 62-63
    sprite('az401_09', 1)	# 64-64
    loopRest()
    label(0)
    sprite('az000_00', 7)	# 65-71
    sprite('az000_01', 7)	# 72-78
    sprite('az000_02', 7)	# 79-85
    sprite('az000_03', 7)	# 86-92
    sprite('az000_04', 7)	# 93-99
    sprite('az000_05', 7)	# 100-106
    sprite('az000_06', 7)	# 107-113
    sprite('az000_07', 7)	# 114-120
    sprite('az000_08', 7)	# 121-127
    sprite('az000_09', 7)	# 128-134
    gotoLabel(0)

@State
def Act3Event_azvsbn_02():
    sprite('az003_00ex', 3)	# 1-3
    Unknown2005()
    sprite('az003_01', 3)	# 4-6
    sprite('az003_00', 3)	# 7-9
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsbn_03():
    sprite('az003_00ex', 3)	# 1-3
    Unknown2005()
    sprite('az003_01', 3)	# 4-6
    sprite('az003_00', 3)	# 7-9
    loopRest()
    label(0)
    sprite('az000_00', 7)	# 10-16
    sprite('az000_01', 7)	# 17-23
    sprite('az000_02', 7)	# 24-30
    sprite('az000_03', 7)	# 31-37
    sprite('az000_04', 7)	# 38-44
    sprite('az000_05', 7)	# 45-51
    sprite('az000_06', 7)	# 52-58
    sprite('az000_07', 7)	# 59-65
    sprite('az000_08', 7)	# 66-72
    sprite('az000_09', 7)	# 73-79
    gotoLabel(0)

@State
def Act3Event_azvsbn_04():

    def upon_IMMEDIATE():
        GFX_0('Act3Event_ar_01', -1)
        Unknown21007(1, 32)
    label(0)
    sprite('az000_00', 7)	# 1-7
    sprite('az000_01', 7)	# 8-14
    sprite('az000_02', 7)	# 15-21
    sprite('az000_03', 7)	# 22-28
    sprite('az000_04', 7)	# 29-35
    sprite('az000_05', 7)	# 36-42
    sprite('az000_06', 7)	# 43-49
    sprite('az000_07', 7)	# 50-56
    sprite('az000_08', 7)	# 57-63
    sprite('az000_09', 7)	# 64-70
    gotoLabel(0)

@State
def Act3Event_azvsbn_05():

    def upon_IMMEDIATE():
        teleportRelativeX(95000)
    sprite('az202_00', 3)	# 1-3
    sprite('az202_01', 3)	# 4-6
    teleportRelativeX(-43000)
    sprite('az202_02', 3)	# 7-9
    teleportRelativeX(-37000)
    sprite('az202_03', 3)	# 10-12
    sprite('az202_04', 2)	# 13-14
    SFX_0('005_swing_grap_2_2')
    sprite('az202_05', 2)	# 15-16	 **attackbox here**
    teleportRelativeX(75000)
    sprite('az202_05', 11)	# 17-27	 **attackbox here**
    Unknown21007(22, 32)
    sprite('az202_06', 3)	# 28-30	 **attackbox here**
    sprite('az202_07', 2)	# 31-32
    teleportRelativeX(-50000)
    sprite('az202_08', 2)	# 33-34
    sprite('az202_09', 3)	# 35-37
    teleportRelativeX(-20000)
    sprite('az202_10', 3)	# 38-40
    teleportRelativeX(20000)
    sprite('az202_11', 2)	# 41-42
    teleportRelativeX(40000)
    sprite('az202_11', 1)	# 43-43
    sprite('az202_12', 3)	# 44-46
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsbn_06():
    sprite('az000_00', 7)	# 1-7
    Unknown21012('416374334576656e745f61725f3031000000000000000000000000000000000021000000')
    sprite('az000_01', 7)	# 8-14
    sprite('az000_02', 7)	# 15-21
    sprite('az000_03', 7)	# 22-28
    sprite('az000_04', 7)	# 29-35
    sprite('az000_05', 7)	# 36-42
    sprite('az003_00ex', 3)	# 43-45
    Unknown2005()
    sprite('az003_01', 3)	# 46-48
    sprite('az003_00', 3)	# 49-51
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsbn_07():
    sprite('keep', 25)	# 1-25
    Unknown21012('416374334576656e745f61725f3031000000000000000000000000000000000024000000')
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    sprite('keep', 25)	# 26-50
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    sprite('keep', 25)	# 51-75
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    sprite('keep', 25)	# 76-100
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_azvsny_00():
    sprite('keep', 25)	# 1-25
    GFX_0('Act3Event_ar_02', 100)
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    sprite('keep', 25)	# 26-50
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    sprite('keep', 25)	# 51-75
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    sprite('keep', 25)	# 76-100
    Unknown8004(100, 1, 1)
    SFX_0('012_stab_middle')
    SFX_0('006_swing_blade_2')
    loopRest()
    enterState('CmnActStand')

@State
def Act3_Event_azvstm_00():
    sprite('az601_00ex00', 32767)	# 1-32767
    GFX_0('Act3Event_ar_03', 100)
    teleportRelativeX(120000)
    loopRest()

@State
def Act3_Event_azvstm_01():
    sprite('az601_00ex00', 7)	# 1-7
    sprite('az601_01ex00', 7)	# 8-14
    sprite('az601_02ex00', 7)	# 15-21
    sprite('az601_03ex00', 7)	# 22-28
    sprite('az601_04ex00', 7)	# 29-35
    sprite('az601_05ex00', 7)	# 36-42
    sprite('az601_06ex00', 7)	# 43-49
    Unknown21012('416374334576656e745f61725f3033000000000000000000000000000000000020000000')
    sprite('az601_07ex00', 11)	# 50-60
    sprite('az601_08ex00', 7)	# 61-67
    sprite('az601_09ex00', 7)	# 68-74
    sprite('az601_10ex00', 8)	# 75-82	 **attackbox here**
    teleportRelativeX(-60000)
    sprite('az601_11', 7)	# 83-89
    teleportRelativeX(-60000)
    sprite('az601_12', 7)	# 90-96
    sprite('az601_13', 7)	# 97-103
    loopRest()
    enterState('CmnActStand')