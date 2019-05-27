@Subroutine
def PreInit():
    Unknown12019('70636500000000000000000000000000')

@Subroutine
def MatchInit():
    DashFInitialVelocity(20000)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(1)
    Unknown13039(1)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 150000, -150000, 180000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 150000, -150000, 180000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 150000, -150000, 180000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(2)
    Unknown15014(2000)
    Unknown14015(0, 100000, -150000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 100000, -150000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 100000, -150000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkKokutengeki', 0x7)
    Move_AirGround_(0x3083)
    Unknown14005(1)
    Unknown14015(0, 150000, -150000, 180000, 1000, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 200000, -100000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Move_AirGround_(0x3083)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 450000, -200000, 250000, 1000, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x3083)
    Unknown14015(0, 450000, -200000, 250000, 1000, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(2000)
    Unknown14015(50000, 250000, -100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown14015(0, 350000, -200000, 50000, 300, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(0, 250000, -100000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 250000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 250000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3083)
    Unknown14015(0, 250000, -250000, 150000, 1000, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Move_AirGround_(0x3083)
    Unknown14015(0, 450000, -300000, 450000, 1000, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 150000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 150000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NoutenotoshiA', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15008()
    Unknown14015(0, 150000, -150000, 180000, 500, 50)
    Move_EndRegister()
    Move_Register('NoutenotoshiB', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14013('NoutenotoshiA')
    Unknown15008()
    Unknown14015(0, 150000, -150000, 180000, 500, 50)
    Move_EndRegister()
    Move_Register('NoutenotoshiC', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown14013('NoutenotoshiA')
    Unknown15008()
    Unknown14015(0, 150000, -150000, 180000, 500, 50)
    Move_EndRegister()
    Move_Register('DragonKickLand_NoutenHasei', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14015(0, 150000, -150000, 180000, 500, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('DragonKickLand_NoutenHaseiB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14013('DragonKickLand_NoutenHasei')
    Unknown14015(0, 150000, -150000, 180000, 500, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('DragonKickLand_NoutenHaseiC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown14013('DragonKickLand_NoutenHasei')
    Unknown14015(0, 150000, -150000, 180000, 500, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('AbaremakuriLandA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 500000, -200000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('DragonKickLandB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 1200000, 100000, 300000, 100, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('DragonKickLandB_Hasei', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14013('DragonKickLandB')
    Unknown14015(0, 1200000, 100000, 300000, 100, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('DragonKickLandEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(0, 1400000, 100000, 400000, 100, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('DragonKickLandEX_Hasei', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown14013('DragonKickLandEX')
    Unknown14015(0, 1400000, 100000, 400000, 100, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('100inchPunchA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 700000, -200000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('100inchPunchA_Hasei', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14013('100inchPunchA')
    Unknown14015(0, 700000, -200000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('100inchPunchB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 1200000, -200000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('100inchPunchB_Hasei', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14013('100inchPunchB')
    Unknown14015(0, 1200000, -200000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('100inchPunchEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(0, 1200000, -200000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('100inchPunchEX_Hasei', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown14013('100inchPunchEX')
    Unknown14015(0, 1200000, -200000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('AbaremakuriAirA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 700000, -400000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('DragonKickAirB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 1200000, 100000, 500000, 300, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('DragonKickAirEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(0, 1200000, 100000, 500000, 300, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('DashCancel', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xe5)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown14015(0, 600000, -200000, 250000, 800, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(2000)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown14015(0, 350000, -200000, 250000, 300, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15014(2000)
    Unknown14015(0, 350000, -200000, 250000, 300, 50)
    Move_EndRegister()
    Move_Register('UltimateGodHand', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(0, 350000, -100000, 200000, 200, 0)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('UltimateGodHandOD', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(0, 350000, -100000, 200000, 200, 0)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('UltimateCharge', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 150000, -150000, 180000, 200, 50)
    Move_EndRegister()
    Move_Register('UltimateChargeOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(0, 150000, -150000, 180000, 200, 50)
    Move_EndRegister()
    Move_Register('UltimateAguneyasutora_Far', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(700000, 1500000, -400000, 400000, 200, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('UltimateAguneyasutoraOD_Far', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(700000, 1500000, -400000, 400000, 200, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('UltimateAguneyasutora_Near', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(300000, 1000000, -400000, 400000, 200, 50)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('UltimateAguneyasutoraOD_Near', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(300000, 1000000, -400000, 400000, 200, 50)
    Move_AirGround_(0x300e)
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
    Unknown15024('NmlAtk5A3rd', 'NmlAtkKokutengeki', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtkKokutengeki', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A2nd', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtk2C', 'AbaremakuriLandA', 10000000)
    Unknown15024('AbaremakuriLandA', 'NoutenotoshiA', 10000000)
    Unknown15024('NoutenotoshiA', 'DragonKickLand_NoutenHasei', 10000000)
    Unknown12018(0, 'ce060_00')
    Unknown12018(1, 'ce060_01')
    Unknown12018(2, 'ce060_02')
    Unknown12018(3, 'ce060_03')
    Unknown12018(4, 'ce060_04')
    Unknown12018(5, 'ce060_05')
    Unknown12018(6, 'ce060_06')
    Unknown12018(7, 'ce041_02')
    Unknown12018(8, 'ce040_02')
    Unknown12018(9, 'ce045_02')
    Unknown12018(10, 'ce060_00')
    Unknown12018(11, 'ce060_01')
    Unknown12018(12, 'ce060_03')
    Unknown12018(13, 'ce060_05')
    Unknown12018(14, 'ce060_07')
    Unknown12018(15, 'ce125_00')
    Unknown12018(16, 'ce050_00')
    Unknown12018(17, 'ce052_00')
    Unknown12018(18, 'ce054_00')
    Unknown12018(25, 'ce063_00')
    Unknown12018(26, 'ce063_01')
    Unknown12018(27, 'ce063_02')
    Unknown12018(28, 'ce063_05')
    Unknown12018(29, 'ce060_12')
    Unknown12018(24, 'ce072_03')
    Unknown7010(0, 'pce000')
    Unknown7010(1, 'pce001')
    Unknown7010(2, 'pce002')
    Unknown7010(3, 'pce003')
    Unknown7010(4, 'pce004')
    Unknown7010(5, 'pce005')
    Unknown7010(6, 'pce006')
    Unknown7010(7, 'pce007')
    Unknown7010(8, 'pce008')
    Unknown7010(9, 'pce009')
    Unknown7010(10, 'pce010')
    Unknown7010(15, 'pce015')
    Unknown7010(16, 'pce016')
    Unknown7010(17, 'pce017')
    Unknown7010(18, 'pce018')
    Unknown7010(19, 'pce019')
    Unknown7010(20, 'pce020')
    Unknown7010(21, 'pce021')
    Unknown7010(22, 'pce022')
    Unknown7010(23, 'pce023')
    Unknown7010(24, 'pce024')
    Unknown7010(25, 'pce025')
    Unknown7010(28, 'pce028')
    Unknown7010(29, 'pce029')
    Unknown7010(30, 'pce030')
    Unknown7010(31, 'pce031')
    Unknown7010(32, 'pce032')
    Unknown7010(33, 'pce033')
    Unknown7010(34, 'pce034')
    Unknown7010(35, 'pce035')
    Unknown7010(36, 'pce036')
    Unknown7010(37, 'pce037')
    Unknown7010(39, 'pce039')
    Unknown7010(42, 'pce042')
    Unknown7010(43, 'pce043')
    Unknown7010(44, 'pce044')
    Unknown7010(45, 'pce045')
    Unknown7010(46, 'pce046')
    Unknown7010(47, 'pce047')
    Unknown7010(48, 'pce048')
    Unknown7010(49, 'pce049')
    Unknown7010(50, 'pce050')
    Unknown7010(52, 'pce052')
    Unknown7010(53, 'pce053')
    Unknown7010(54, 'pce100_0')
    Unknown7010(55, 'pce100_1')
    Unknown7010(56, 'pce100_2')
    Unknown7010(63, 'pce101_0')
    Unknown7010(64, 'pce101_1')
    Unknown7010(65, 'pce101_2')
    Unknown7010(57, 'pce102_0')
    Unknown7010(58, 'pce102_1')
    Unknown7010(59, 'pce102_2')
    Unknown7010(66, 'pce103_0')
    Unknown7010(67, 'pce103_1')
    Unknown7010(68, 'pce103_2')
    Unknown7010(60, 'pce104_0')
    Unknown7010(61, 'pce104_1')
    Unknown7010(62, 'pce104_2')
    Unknown7010(69, 'pce105_0')
    Unknown7010(70, 'pce105_1')
    Unknown7010(71, 'pce105_2')
    Unknown7010(72, 'pce156')
    Unknown7010(73, 'pce157')
    Unknown7010(74, 'pce158')
    Unknown7010(85, 'pce159')
    Unknown7010(87, 'pce160')
    Unknown7010(88, 'pce161')
    Unknown7010(96, 'pce167_0')
    Unknown7010(97, 'pce167_1')
    Unknown7010(92, 'pce168_0')
    Unknown7010(93, 'pce168_1')
    Unknown7010(98, 'pce169_0')
    Unknown7010(99, 'pce169_1')
    Unknown7010(100, 'pce170_0')
    Unknown7010(101, 'pce170_1')
    Unknown7010(105, 'pce171_0')
    Unknown7010(106, 'pce171_1')
    Unknown7010(102, 'pce172_0')
    Unknown7010(103, 'pce172_1')
    Unknown7010(90, 'pce173_0')
    Unknown7010(91, 'pce173_1')
    Unknown7010(107, 'pce174_0')
    Unknown7010(108, 'pce175_0')
    Unknown7010(110, 'pce174_1')
    Unknown7010(111, 'pce175_1')
    Unknown7010(94, 'pce402_0')
    Unknown7010(95, 'pce402_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d617465476f6448616e640000000000000000000000000000000000')
    Unknown12059('03000000556c74696d617465476f6448616e644f44000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465436861726765000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174654368617267654f4400000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    Unknown30036('5043455f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown23003(0, 1, 4, 1, 18000, 0, -65536, -65536)

@Subroutine
def OnFrameStep():
    if SLOT_31:
        if (not 
        if (not 
        if (not 
        if (not 
        if (not 
        if (not 
        if (not 
        if (not Unknown23148('UltimateCharge')):
            Unknown23148('UltimateChargeOD')):
            Unknown23148('UltimateGodHand')):
            Unknown23148('UltimateGodHandOD')):
            Unknown23148('UltimateAguneyasutora_Far')):
            Unknown23148('UltimateAguneyasutora_Near')):
            Unknown23148('UltimateAguneyasutoraOD_Far')):
            Unknown23148('UltimateAguneyasutoraOD_Near')):
            if (not SLOT_114):
                if (SLOT_59 == 1):
                    SLOT_31 = (SLOT_31 + (-150))
                if (SLOT_59 == 2):
                    SLOT_31 = (SLOT_31 + (-150))
                if (SLOT_59 == 3):
                    SLOT_31 = (SLOT_31 + (-150))
    if SLOT_91:
        Unknown58('TRI_PCEChargeLv', 2, 67)
        if (SLOT_67 == 1):
            SLOT_31 = 0
        if (SLOT_67 == 2):
            SLOT_31 = 18000
            SLOT_59 = 1
        if (SLOT_67 == 3):
            SLOT_31 = 18000
            SLOT_59 = 2
        if (SLOT_67 == 4):
            SLOT_31 = 18000
            SLOT_59 = 3
    if (not SLOT_31):
        SLOT_59 = 0
    if (not SLOT_75):
        SLOT_31 = 0
    SLOT_60 = (SLOT_60 + 1)
    if (SLOT_60 >= 2):
        SLOT_60 = 0
    if SLOT_59:
        Unknown12030(10)
        Unknown23008(0, 1)
        if (SLOT_59 == 1):
            Unknown23007(0, -11010304)
            Unknown23038(0, -11010304)
            Unknown23006(0, 4)
        if (SLOT_59 == 2):
            Unknown23007(0, -256)
            Unknown23038(0, -256)
            Unknown23006(0, 5)
        if (SLOT_59 == 3):
            Unknown23007(0, -65536)
            Unknown23038(0, -65536)
            Unknown23006(0, 6)
        if SLOT_60:
            if (not SLOT_64):
                GFX_1('ceef_charge_02', 105)
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
        if Unknown23148('CmnActChangeReturnAppeal'):
            SLOT_64 = 1
        if Unknown23148('CmnActCrushAttackAssistChase1st'):
            SLOT_64 = 1
        if Unknown23148('CmnActCrushAttackAssistChase2nd'):
            SLOT_64 = 1
        if Unknown23148('CmnActCrushAttackAssistFinish'):
            SLOT_64 = 1
        if Unknown23148('CmnActChangePartnerDD'):
            SLOT_64 = 1
        if Unknown23148('ChangePartnerDD_Exe'):
            SLOT_64 = 1
        if Unknown23148('ChangePartnerDDOD_Exe'):
            SLOT_64 = 1
    else:
        Unknown12030(20)
        Unknown23008(0, 0)

@Subroutine
def ChargeDamageUp():
    Unknown48('19000000020000004300000003000000020000003b000000')
    if (SLOT_67 == 1):
        Unknown10000(200)
    if (SLOT_67 == 2):
        Unknown10000(300)
    if (SLOT_67 == 3):
        Unknown10000(400)

@Subroutine
def ChargeDamageUp_Kick():
    Unknown48('19000000020000004300000003000000020000003b000000')
    if (SLOT_67 == 1):
        Unknown10000(200)
    if (SLOT_67 == 2):
        Unknown10000(300)
    if (SLOT_67 == 3):
        Unknown10000(400)

@Subroutine
def Charge_Count():
    if SLOT_31:
        pass

@Subroutine
def DoNotBeginCancel():
    if Unknown23145('AbaremakuriLandA'):
        Unknown30068(1)
    if Unknown23145('AbaremakuriAirA'):
        Unknown30068(1)
    if Unknown23145('NoutenotoshiA'):
        Unknown30068(1)
    if Unknown23145('100inchPunchA'):
        Unknown30068(1)
    if Unknown23145('100inchPunchB'):
        Unknown30068(1)
    if Unknown23145('100inchPunchEX'):
        Unknown30068(1)

@Subroutine
def LandSpecialAttack_DeriveInput():
    if (not Unknown23148('NoutenotoshiA')):
        Unknown14070('AbaremakuriLandA')
        Unknown14070('UltimateGodHand')
        Unknown14070('UltimateGodHandOD')
        Unknown14070('UltimateCharge')
        Unknown14070('UltimateChargeOD')
        Unknown14070('AstralHeat')
    Unknown14070('DragonKickLandB')
    Unknown14070('DragonKickLandEX')
    Unknown14070('100inchPunchA')
    Unknown14070('100inchPunchB')
    Unknown14070('100inchPunchEX')

@Subroutine
def LandSpecialAttack_DeriveTiming():
    if (not Unknown23148('NoutenotoshiA')):
        Unknown14072('AbaremakuriLandA')
        Unknown14072('UltimateGodHand')
        Unknown14072('UltimateGodHandOD')
        Unknown14072('UltimateCharge')
        Unknown14072('UltimateChargeOD')
        Unknown14072('AstralHeat')
    Unknown14072('DragonKickLandB')
    Unknown14072('DragonKickLandEX')
    Unknown14072('100inchPunchA')
    Unknown14072('100inchPunchB')
    Unknown14072('100inchPunchEX')

@Subroutine
def LandSpecialAttack_DeriveClear():
    if (not Unknown23148('NoutenotoshiA')):
        Unknown14074('AbaremakuriLandA')
        Unknown14074('UltimateGodHand')
        Unknown14074('UltimateGodHandOD')
        Unknown14074('UltimateCharge')
        Unknown14074('UltimateChargeOD')
        Unknown14074('AstralHeat')
    Unknown14074('DragonKickLandB')
    Unknown14074('DragonKickLandEX')
    Unknown14074('100inchPunchA')
    Unknown14074('100inchPunchB')
    Unknown14074('100inchPunchEX')

@Subroutine
def AirSpecialAttack_DeriveInput():
    Unknown14070('AbaremakuriAirA')
    Unknown14070('DragonKickAirB')
    Unknown14070('DragonKickAirEX')

@Subroutine
def AirSpecialAttack_DeriveTiming():
    Unknown14072('AbaremakuriAirA')
    Unknown14072('DragonKickAirB')
    Unknown14072('DragonKickAirEX')

@Subroutine
def AirSpecialAttack_DeriveClear():
    Unknown14074('AbaremakuriAirA')
    Unknown14074('DragonKickAirB')
    Unknown14074('DragonKickAirEX')

@Subroutine
def Abaremakuri_DeriveInput():
    Unknown14070('DragonKickLandB_Hasei')
    Unknown14070('DragonKickLandEX_Hasei')
    Unknown14070('100inchPunchA_Hasei')
    Unknown14070('100inchPunchB_Hasei')
    Unknown14070('100inchPunchEX_Hasei')

@Subroutine
def Abaremakuri_DeriveTiming():
    Unknown14072('DragonKickLandB_Hasei')
    Unknown14072('DragonKickLandEX_Hasei')
    Unknown14072('100inchPunchA_Hasei')
    Unknown14072('100inchPunchB_Hasei')
    Unknown14072('100inchPunchEX_Hasei')

@Subroutine
def Abaremakuri_DeriveClear():
    Unknown14074('DragonKickLandB_Hasei')
    Unknown14074('DragonKickLandEX_Hasei')
    Unknown14074('100inchPunchA_Hasei')
    Unknown14074('100inchPunchB_Hasei')
    Unknown14074('100inchPunchEX_Hasei')

@Subroutine
def Noutenotoshi_DeriveInput():
    Unknown14070('NoutenotoshiA')
    Unknown14070('NoutenotoshiB')
    Unknown14070('NoutenotoshiC')

@Subroutine
def Noutenotoshi_DeriveTiming():
    Unknown14072('NoutenotoshiA')
    Unknown14072('NoutenotoshiB')
    Unknown14072('NoutenotoshiC')

@Subroutine
def Noutenotoshi_DeriveClear():
    Unknown14074('NoutenotoshiA')
    Unknown14074('NoutenotoshiB')
    Unknown14074('NoutenotoshiC')

@State
def CmnActStand():
    label(0)
    sprite('ce000_00', 6)	# 1-6
    sprite('ce000_01', 6)	# 7-12
    sprite('ce000_02', 6)	# 13-18
    sprite('ce000_03', 6)	# 19-24
    sprite('ce000_04', 6)	# 25-30
    sprite('ce000_05', 6)	# 31-36
    sprite('ce000_06', 6)	# 37-42
    sprite('ce000_07', 6)	# 43-48
    sprite('ce000_08', 6)	# 49-54
    sprite('ce000_09', 6)	# 55-60
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
    sprite('ce001_00', 6)	# 61-66
    SLOT_88 = 960
    SFX_1('pce000')
    sprite('ce001_01', 6)	# 67-72
    sprite('ce001_02', 6)	# 73-78
    sprite('ce001_03', 6)	# 79-84
    sprite('ce001_04', 6)	# 85-90
    sprite('ce001_05', 6)	# 91-96
    sprite('ce001_00', 6)	# 97-102
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ce003_00', 4)	# 1-4
    sprite('ce003_01', 4)	# 5-8
    sprite('ce003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('ce010_00', 4)	# 1-4
    sprite('ce010_01', 4)	# 5-8

@State
def CmnActCrouch():
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
    sprite('ce013_00', 4)	# 1-4
    sprite('ce013_01', 4)	# 5-8
    sprite('ce013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('ce010_01', 4)	# 1-4
    sprite('ce010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ce010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ce020_00', 4)	# 1-4
    sprite('ce020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ce020_02', 3)	# 1-3
    sprite('ce020_03', 3)	# 4-6
    sprite('ce020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ce020_05', 3)	# 1-3
    sprite('ce020_06', 3)	# 4-6
    label(0)
    sprite('ce020_07', 4)	# 7-10
    sprite('ce020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ce010_01', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('ce010_01', 2)	# 1-2
    sprite('ce010_02', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('ce010_02', 2)	# 1-2
    sprite('ce010_03', 2)	# 3-4
    sprite('ce010_04', 2)	# 5-6

@State
def CmnActFWalk():
    sprite('ce030_00', 5)	# 1-5
    sprite('ce030_01', 5)	# 6-10
    label(0)
    sprite('ce030_02', 5)	# 11-15
    sprite('ce030_03', 5)	# 16-20
    sprite('ce030_04', 5)	# 21-25
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce030_05', 5)	# 26-30
    sprite('ce030_06', 5)	# 31-35
    sprite('ce030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('ce031_00', 6)	# 1-6
    sprite('ce031_01', 6)	# 7-12
    label(0)
    sprite('ce031_02', 6)	# 13-18
    sprite('ce031_03', 6)	# 19-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ce031_04', 6)	# 25-30
    sprite('ce031_05', 6)	# 31-36
    sprite('ce031_06', 6)	# 37-42
    sprite('ce031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('ce030_00', 4)	# 1-4
    sprite('ce032_00', 2)	# 5-6
    label(0)
    sprite('ce032_01', 4)	# 7-10
    sprite('ce032_02', 4)	# 11-14
    sprite('ce032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('ce032_04', 4)	# 19-22
    sprite('ce032_05', 4)	# 23-26
    sprite('ce032_06', 4)	# 27-30
    sprite('ce032_07', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('ce032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ce032_09', 7)	# 1-7
    sprite('ce032_10', 5)	# 8-12

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
    sprite('ce033_00', 2)	# 1-2
    sprite('ce033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('ce033_02', 3)	# 6-8
    label(0)
    sprite('ce033_01', 3)	# 9-11
    sprite('ce033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce033_03', 3)	# 15-17
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ce033_04', 3)	# 18-20

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('ce035_00', 3)	# 1-3
    label(0)
    sprite('ce035_01', 3)	# 4-6
    sprite('ce035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ce033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('ce033_02', 3)	# 4-6
    sprite('ce033_01', 3)	# 7-9
    sprite('ce033_02', 3)	# 10-12
    sprite('ce033_01', 3)	# 13-15
    sprite('ce033_02', 3)	# 16-18
    sprite('ce033_01', 3)	# 19-21
    sprite('ce033_02', 3)	# 22-24
    sprite('ce020_05', 3)	# 25-27
    sprite('ce020_06', 3)	# 28-30
    label(0)
    sprite('ce020_07', 4)	# 31-34
    sprite('ce020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ce050_00', 1)	# 1-1
    sprite('ce050_01', 1)	# 2-2
    sprite('ce050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ce050_01', 1)	# 1-1
    sprite('ce050_02', 1)	# 2-2
    sprite('ce050_01', 2)	# 3-4
    sprite('ce050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ce050_02', 1)	# 1-1
    sprite('ce050_03', 1)	# 2-2
    sprite('ce050_02', 2)	# 3-4
    sprite('ce050_01', 2)	# 5-6
    sprite('ce050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ce050_03', 1)	# 1-1
    sprite('ce050_04', 1)	# 2-2
    sprite('ce050_03', 2)	# 3-4
    sprite('ce050_02', 2)	# 5-6
    sprite('ce050_01', 2)	# 7-8
    sprite('ce050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ce050_04', 1)	# 1-1
    sprite('ce050_04', 1)	# 2-2
    sprite('ce050_04', 2)	# 3-4
    sprite('ce050_03', 2)	# 5-6
    sprite('ce050_02', 2)	# 7-8
    sprite('ce050_01', 2)	# 9-10
    sprite('ce050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ce052_00', 1)	# 1-1
    sprite('ce052_01', 1)	# 2-2
    sprite('ce052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ce052_01', 1)	# 1-1
    sprite('ce052_02', 1)	# 2-2
    sprite('ce052_01', 2)	# 3-4
    sprite('ce052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ce052_02', 1)	# 1-1
    sprite('ce052_03', 1)	# 2-2
    sprite('ce052_02', 2)	# 3-4
    sprite('ce052_01', 2)	# 5-6
    sprite('ce052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ce052_03', 1)	# 1-1
    sprite('ce052_04', 1)	# 2-2
    sprite('ce052_03', 2)	# 3-4
    sprite('ce052_02', 2)	# 5-6
    sprite('ce052_01', 2)	# 7-8
    sprite('ce052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ce052_04', 1)	# 1-1
    sprite('ce052_04', 1)	# 2-2
    sprite('ce052_04', 2)	# 3-4
    sprite('ce052_03', 2)	# 5-6
    sprite('ce052_02', 2)	# 7-8
    sprite('ce052_01', 2)	# 9-10
    sprite('ce052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ce054_00', 1)	# 1-1
    sprite('ce054_01', 1)	# 2-2
    sprite('ce054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ce054_01', 1)	# 1-1
    sprite('ce054_02', 1)	# 2-2
    sprite('ce054_01', 2)	# 3-4
    sprite('ce054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ce054_02', 1)	# 1-1
    sprite('ce054_03', 1)	# 2-2
    sprite('ce054_02', 2)	# 3-4
    sprite('ce054_01', 2)	# 5-6
    sprite('ce054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ce054_03', 1)	# 1-1
    sprite('ce054_04', 1)	# 2-2
    sprite('ce054_03', 2)	# 3-4
    sprite('ce054_02', 2)	# 5-6
    sprite('ce054_01', 2)	# 7-8
    sprite('ce054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ce054_04', 1)	# 1-1
    sprite('ce054_04', 1)	# 2-2
    sprite('ce054_04', 2)	# 3-4
    sprite('ce054_03', 2)	# 5-6
    sprite('ce054_02', 2)	# 7-8
    sprite('ce054_01', 2)	# 9-10
    sprite('ce054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ce060_00', 4)	# 1-4
    label(0)
    sprite('ce060_01', 4)	# 5-8
    sprite('ce060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ce060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ce060_04', 8)	# 1-8
    label(0)
    sprite('ce060_05', 4)	# 9-12
    sprite('ce060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ce060_07', 4)	# 1-4

@State
def CmnActBDownBound():
    sprite('ce060_07', 3)	# 1-3

@State
def CmnActBDownLoop():
    sprite('ce060_12', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('nt061_00', 4)	# 1-4
    sprite('nt061_01', 3)	# 5-7
    sprite('nt061_02', 3)	# 8-10
    sprite('nt061_03', 3)	# 11-13
    sprite('nt061_04', 3)	# 14-16
    sprite('nt061_05', 3)	# 17-19
    sprite('nt061_06', 3)	# 20-22
    sprite('nt061_07', 3)	# 23-25
    sprite('nt061_08', 3)	# 26-28

@State
def CmnActFDownUpper():
    sprite('ce063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ce063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ce063_03', 3)	# 1-3
    sprite('ce063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ce063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('ce060_08', 2)	# 1-2
    sprite('ce060_09', 2)	# 3-4
    sprite('ce060_10', 2)	# 5-6
    sprite('ce060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('ce060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ce064_00', 6)	# 1-6
    sprite('ce064_01', 6)	# 7-12
    sprite('ce064_02', 6)	# 13-18
    sprite('ce064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('ce060_00', 4)	# 1-4
    label(0)
    sprite('ce060_01', 4)	# 5-8
    sprite('ce060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ce060_03', 4)	# 1-4
    sprite('ce060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('ce060_04', 8)	# 1-8
    label(0)
    sprite('ce060_05', 4)	# 9-12
    sprite('ce060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ce060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('ce072_00', 3)	# 1-3
    sprite('ce072_01', 3)	# 4-6
    sprite('ce072_02', 3)	# 7-9
    label(0)
    sprite('ce072_01', 3)	# 10-12
    sprite('ce072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ce074_00', 2)	# 1-2
    sprite('ce074_01', 2)	# 3-4
    sprite('ce074_02', 2)	# 5-6
    sprite('ce074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('ce082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('ce052_01', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ce072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('ce063_00', 3)	# 1-3
    label(0)
    sprite('ce063_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ce070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('ce070_01', 4)	# 1-4
    sprite('ce070_02', 4)	# 5-8
    sprite('ce070_03', 4)	# 9-12
    sprite('ce070_04', 4)	# 13-16
    sprite('ce070_05', 4)	# 17-20
    sprite('ce070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ce040_03', 2)	# 1-2
    sprite('ce040_02', 2)	# 3-4
    sprite('ce040_01', 2)	# 5-6
    sprite('ce040_00', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ce020_02', 3)	# 1-3
    sprite('ce020_03', 3)	# 4-6
    sprite('ce020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('ce020_02', 3)	# 1-3
    sprite('ce020_03', 3)	# 4-6
    sprite('ce020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirN():
    sprite('ce020_02', 3)	# 1-3
    sprite('ce020_03', 3)	# 4-6
    sprite('ce020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandF():
    sprite('ce112_00', 3)	# 1-3
    sprite('ce112_01', 3)	# 4-6
    sprite('ce112_02', 3)	# 7-9
    sprite('ce112_03', 3)	# 10-12
    sprite('ce112_04', 3)	# 13-15
    sprite('ce112_05', 3)	# 16-18
    label(0)
    sprite('ce020_07', 4)	# 19-22
    sprite('ce020_08', 4)	# 23-26
    loopRest()
    gotoLabel(0)

@State
def CmnActUkemiLandB():
    sprite('ce112_00', 3)	# 1-3
    sprite('ce112_01', 3)	# 4-6
    sprite('ce112_02', 3)	# 7-9
    sprite('ce112_03', 3)	# 10-12
    sprite('ce112_04', 3)	# 13-15
    sprite('ce112_05', 3)	# 16-18
    label(0)
    sprite('ce020_07', 4)	# 19-22
    sprite('ce020_08', 4)	# 23-26
    loopRest()
    gotoLabel(0)

@State
def CmnActUkemiLandN():
    sprite('ce112_00', 3)	# 1-3
    sprite('ce112_01', 3)	# 4-6
    sprite('ce112_02', 3)	# 7-9
    sprite('ce112_03', 3)	# 10-12
    sprite('ce112_04', 3)	# 13-15
    sprite('ce112_05', 3)	# 16-18
    label(0)
    sprite('ce020_07', 4)	# 19-22
    sprite('ce020_08', 4)	# 23-26
    loopRest()
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('ce010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('ce040_00', 3)	# 1-3
    sprite('ce040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ce040_02', 5)	# 1-5
    sprite('ce040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ce040_01', 3)	# 1-3
    sprite('ce040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ce040_04', 1)	# 1-1
    label(0)
    sprite('ce040_02', 5)	# 2-6
    sprite('ce040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ce040_01', 3)	# 1-3
    sprite('ce040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ce040_00', 3)	# 1-3
    sprite('ce040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('ce040_04', 1)	# 1-1
    label(0)
    sprite('ce040_02', 5)	# 2-6
    sprite('ce040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ce040_01', 3)	# 1-3
    sprite('ce040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ce040_04', 1)	# 1-1
    label(0)
    sprite('ce040_02', 5)	# 2-6
    sprite('ce040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ce040_01', 3)	# 1-3
    sprite('ce040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ce043_00', 3)	# 1-3
    sprite('ce043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ce043_02', 5)	# 1-5
    sprite('ce043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ce043_01', 3)	# 1-3
    sprite('ce043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ce043_04', 1)	# 1-1
    label(0)
    sprite('ce043_02', 5)	# 2-6
    sprite('ce043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ce043_01', 3)	# 1-3
    sprite('ce043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ce045_00', 3)	# 1-3
    sprite('ce045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ce045_02', 5)	# 1-5
    sprite('ce045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ce045_01', 3)	# 1-3
    sprite('ce045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ce045_04', 1)	# 1-1
    label(0)
    sprite('ce045_02', 5)	# 2-6
    sprite('ce045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ce045_01', 3)	# 1-3
    sprite('ce045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ce040_04', 2)	# 1-2
    sprite('ce040_04', 2)	# 3-4
    sprite('ce040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ce040_02', 4)	# 6-9
    sprite('ce040_01', 4)	# 10-13
    sprite('ce040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ce043_04', 2)	# 1-2
    sprite('ce043_04', 2)	# 3-4
    sprite('ce043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ce043_02', 4)	# 6-9
    sprite('ce043_01', 4)	# 10-13
    sprite('ce043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ce045_04', 2)	# 1-2
    sprite('ce045_04', 2)	# 3-4
    sprite('ce045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ce045_02', 4)	# 6-9
    sprite('ce045_01', 4)	# 10-13
    sprite('ce045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('ce025_00', 1)	# 1-1
    sprite('ce025_01', 2)	# 2-3
    sprite('ce025_02', 1)	# 4-4

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('ce203_00', 2)	# 1-2
    Unknown2004(1, 0)
    sprite('ce203_01', 4)	# 3-6
    sprite('ce203_02', 2)	# 7-8	 **attackbox here**
    sprite('ce203_03', 3)	# 9-11	 **attackbox here**
    sprite('ce203_04', 3)	# 12-14
    sprite('ce203_05', 3)	# 15-17
    sprite('ce203_06', 3)	# 18-20
    sprite('ce203_07', 3)	# 21-23
    sprite('ce203_08', 3)	# 24-26
    sprite('ce203_09', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('nt045_02', 1)	# 1-1
    sprite('nt045_01', 3)	# 2-4
    sprite('nt045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ce252_00', 3)	# 1-3
    sprite('ce252_01', 3)	# 4-6
    sprite('ce252_03', 3)	# 7-9	 **attackbox here**
    sprite('ce252_03', 8)	# 10-17	 **attackbox here**
    Unknown23027()
    sprite('ce252_04', 3)	# 18-20
    sprite('ce252_05', 3)	# 21-23
    sprite('ce252_06', 3)	# 24-26
    sprite('ce252_07', 3)	# 27-29
    Unknown2001()

@State
def CmnActLandSpin():
    sprite('ce071_00', 2)	# 1-2
    label(0)
    sprite('ce071_01', 2)	# 3-4
    sprite('ce071_02', 2)	# 5-6
    sprite('ce071_03', 2)	# 7-8
    sprite('ce071_04', 2)	# 9-10
    sprite('ce071_05', 2)	# 11-12
    sprite('ce071_06', 2)	# 13-14
    sprite('ce071_07', 2)	# 15-16
    sprite('ce071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ce040_02', 32767)	# 1-32767
    sprite('ce040_01', 3)	# 32768-32770
    sprite('ce040_00', 3)	# 32771-32773

@State
def CmnActVertSpin():
    sprite('ce071_00', 2)	# 1-2
    label(0)
    sprite('ce071_01', 2)	# 3-4
    sprite('ce071_02', 2)	# 5-6
    sprite('ce071_03', 2)	# 7-8
    sprite('ce071_04', 2)	# 9-10
    sprite('ce071_05', 2)	# 11-12
    sprite('ce071_06', 2)	# 13-14
    sprite('ce071_07', 2)	# 15-16
    sprite('ce071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('ce124_00', 2)	# 1-2
    label(0)
    sprite('ce124_01', 2)	# 3-4
    sprite('ce124_02', 2)	# 5-6
    sprite('ce124_03', 2)	# 7-8
    sprite('ce124_04', 2)	# 9-10
    sprite('ce124_05', 2)	# 11-12
    sprite('ce124_06', 2)	# 13-14
    sprite('ce124_07', 2)	# 15-16
    sprite('ce124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ce077_02', 4)	# 1-4
    label(0)
    sprite('ce077_03', 3)	# 5-7
    sprite('ce077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ce077_05', 5)	# 1-5
    sprite('ce077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('ce077_02', 4)	# 1-4
    label(0)
    sprite('ce077_03', 3)	# 5-7
    sprite('ce077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ce077_05', 5)	# 1-5
    sprite('ce077_06', 4)	# 6-9

@State
def CmnActBurstBegin():
    label(0)
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ce121_03', 3)	# 1-3
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ce121_07', 3)	# 1-3
    sprite('ce121_08', 3)	# 4-6
    sprite('ce020_04', 3)	# 7-9
    sprite('ce020_05', 3)	# 10-12
    sprite('ce020_06', 3)	# 13-15
    label(0)
    sprite('ce020_07', 4)	# 16-19
    sprite('ce020_08', 4)	# 20-23
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstBegin():
    label(0)
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ce121_03', 3)	# 1-3
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ce121_07', 3)	# 1-3
    sprite('ce121_08', 3)	# 4-6
    sprite('ce020_04', 3)	# 7-9
    sprite('ce020_05', 3)	# 10-12
    sprite('ce020_06', 3)	# 13-15
    label(0)
    sprite('ce020_07', 4)	# 16-19
    sprite('ce020_08', 4)	# 20-23
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ce121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ce121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('ce121_07', 4)	# 1-4
    sprite('ce121_08', 4)	# 5-8
    sprite('ce010_00', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ce121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ce121_03', 3)	# 1-3
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ce121_07', 2)	# 1-2
    sprite('ce121_08', 2)	# 3-4
    sprite('ce020_04', 3)	# 5-7
    sprite('ce020_05', 3)	# 8-10
    sprite('ce020_06', 2)	# 11-12
    label(0)
    sprite('ce020_07', 4)	# 13-16
    sprite('ce020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PCE_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ce121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ce121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('ce121_07', 2)	# 1-2
    sprite('ce121_08', 2)	# 3-4
    sprite('ce020_04', 2)	# 5-6
    sprite('ce020_05', 2)	# 7-8
    sprite('ce020_06', 2)	# 9-10
    sprite('ce020_07', 2)	# 11-12

@State
def CmnActAirCrossRushBegin():
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PCE_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ce121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ce121_03', 3)	# 1-3
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ce121_07', 2)	# 1-2
    sprite('ce121_08', 2)	# 3-4
    sprite('ce020_04', 3)	# 5-7
    sprite('ce020_05', 3)	# 8-10
    sprite('ce020_06', 2)	# 11-12
    label(0)
    sprite('ce020_07', 4)	# 13-16
    sprite('ce020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PCE_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ce121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('ce121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ce121_07', 2)	# 1-2
    sprite('ce121_08', 2)	# 3-4
    sprite('ce020_04', 2)	# 5-6
    sprite('ce020_05', 2)	# 7-8
    sprite('ce020_06', 2)	# 9-10
    sprite('ce020_07', 2)	# 11-12

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PCE_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    sprite('ce121_00', 2)	# 1-2
    sprite('ce121_01', 2)	# 3-4
    sprite('ce121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ce121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('ce121_03', 3)	# 1-3
    label(0)
    sprite('ce121_04', 2)	# 4-5
    sprite('ce121_05', 2)	# 6-7
    sprite('ce121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ce121_07', 2)	# 1-2
    sprite('ce121_08', 2)	# 3-4
    sprite('ce020_04', 3)	# 5-7
    sprite('ce020_05', 3)	# 8-10
    sprite('ce020_06', 2)	# 11-12
    label(0)
    sprite('ce020_07', 4)	# 13-16
    sprite('ce020_08', 4)	# 17-20
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
        AttackLevel_(4)
        AirPushbackX(24000)
        AirPushbackY(-75000)
        Unknown11028(24)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(10)
        Unknown11064(2)
        Hitstop(20)
        Unknown2004(1, 0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
        setInvincible(1)
        Unknown11063(1)
    sprite('null', 16)	# 1-16
    sprite('null', 1)	# 17-17
    Unknown23151(22, 104)
    Unknown2017(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown23119(16750300, 8, 2)
    sprite('null', 1)	# 18-18
    teleportRelativeX(-1600000)
    Unknown1007(650000)
    physicsXImpulse(90000)
    physicsYImpulse(-37500)
    sprite('ce600_00ex', 2)	# 19-20	 **attackbox here**
    Unknown23027()
    Unknown2005()
    sprite('ce600_01ex', 2)	# 21-22	 **attackbox here**
    sprite('ce600_00ex', 2)	# 23-24	 **attackbox here**
    sprite('ce600_01ex', 2)	# 25-26	 **attackbox here**
    sprite('ce600_00ex', 2)	# 27-28	 **attackbox here**
    sprite('ce600_01ex', 2)	# 29-30	 **attackbox here**
    sprite('ce600_00ex', 2)	# 31-32	 **attackbox here**
    sprite('ce600_01ex', 2)	# 33-34	 **attackbox here**
    sprite('ce600_00ex', 2)	# 35-36	 **attackbox here**
    Unknown2017(1)
    Unknown2053(1)
    Unknown2034(1)
    label(0)
    sprite('ce600_01ex', 2)	# 37-38	 **attackbox here**
    sprite('ce600_00ex', 2)	# 39-40	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 3)	# 41-43
    RefreshMultihit()
    sprite('ce402_14', 4)	# 44-47
    Unknown1019(30)
    Unknown2005()
    Unknown18009(1)
    teleportRelativeX(150000)
    Unknown8000(0, 1, 1)
    sprite('ce402_15', 4)	# 48-51
    Unknown1019(30)
    teleportRelativeX(-265000)
    sprite('ce402_16', 4)	# 52-55
    Unknown1019(30)
    sprite('ce402_17', 4)	# 56-59
    Unknown1019(30)
    sprite('ce402_18', 3)	# 60-62
    Unknown1019(0)
    sprite('ce010_02', 3)	# 63-65
    teleportRelativeX(140000)

@State
def CmnActChangePartnerQuickIn():
    sprite('ce032_05', 3)	# 1-3
    sprite('ce032_06', 5)	# 4-8
    sprite('ce032_09', 7)	# 9-15
    sprite('ce032_09', 7)	# 16-22
    sprite('ce032_10', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ce033_01', 3)	# 1-3
    sprite('ce033_02', 3)	# 4-6
    sprite('ce033_01', 3)	# 7-9
    sprite('ce033_02', 3)	# 10-12
    sprite('ce033_01', 3)	# 13-15
    sprite('ce033_02', 3)	# 16-18
    sprite('ce033_01', 3)	# 19-21
    sprite('ce033_02', 3)	# 22-24
    sprite('ce033_01', 3)	# 25-27
    sprite('ce033_02', 3)	# 28-30
    sprite('ce033_01', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('ce033_00', 1)	# 1-1
    sprite('ce033_01', 2)	# 2-3
    sprite('ce033_01', 2)	# 4-5
    Unknown8002()
    sprite('ce033_02', 1)	# 6-6
    sprite('ce033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('ce033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce033_03', 3)	# 13-15
    sprite('ce033_04', 3)	# 16-18

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ce600_07', 6)	# 1-6
    sprite('ce600_05', 6)	# 7-12
    sprite('ce600_04', 6)	# 13-18
    sprite('ce600_03', 6)	# 19-24
    sprite('ce600_04', 6)	# 25-30
    sprite('ce600_05', 6)	# 31-36
    sprite('ce600_03', 6)	# 37-42
    sprite('ce600_04', 6)	# 43-48
    sprite('ce600_05', 6)	# 49-54
    sprite('ce600_03', 4)	# 55-58
    sprite('ce600_04', 6)	# 59-64
    sprite('ce600_05', 6)	# 65-70
    sprite('ce600_07', 6)	# 71-76

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
    sprite('ce010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11042(1)
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(70)
        Unknown11056(2)
        Unknown11058('0100000000000000000000000000000000000000')
        AirUntechableTime(60)
        AirPushbackX(70000)
        AirPushbackY(60000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9178(1)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(15)

        def upon_78():
            pass
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        Unknown23001(0, 0)
        Unknown23014()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ce032_00', 2)	# 1-2
    Unknown8006(100, 1, 1)
    Unknown1084(1)
    Unknown1047(12000)
    Unknown7007('7063653231325f300000000000000000640000007063653231325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ce404_00', 3)	# 3-5
    sprite('ce404_01', 2)	# 6-7
    sprite('ce404_01', 1)	# 8-8
    Unknown23029(11, 403, 0)
    sprite('ce404_02', 5)	# 9-13
    sprite('ce404_03', 3)	# 14-16
    sprite('ce404_04', 1)	# 17-17
    Unknown8007(100, 1, 1)
    physicsXImpulse(30000)
    physicsYImpulse(13000)
    setGravity(1000)
    SFX_3('slash_blade_middle')
    sprite('ce404_04', 2)	# 18-19
    Unknown1019(200)
    YAccel(200)
    SFX_3('slash_blade_fast')
    loopRest()
    sprite('ce404_05', 3)	# 20-22
    Unknown1019(96)
    sprite('ce404_06', 3)	# 23-25	 **attackbox here**
    Unknown1019(96)
    Unknown2017(0)
    RefreshMultihit()
    GFX_0('DragonKick', 0)
    GFX_0('DragonKick_Launcher', 0)
    loopRest()
    sprite('ce404_07', 3)	# 26-28	 **attackbox here**
    Unknown1019(96)
    sprite('ce404_06', 3)	# 29-31	 **attackbox here**
    Unknown1019(96)
    sprite('ce404_07', 3)	# 32-34	 **attackbox here**
    Unknown1019(96)
    loopRest()
    sprite('ce404_08', 3)	# 35-37
    sendToLabelUpon(2, 2)
    Unknown2017(1)
    setGravity(1800)
    Unknown1019(80)
    sprite('ce404_09', 3)	# 38-40
    Unknown1019(80)
    sprite('ce404_10', 3)	# 41-43
    Unknown1019(80)
    sprite('ce404_11', 3)	# 44-46
    Unknown1019(80)
    sprite('ce020_04', 3)	# 47-49
    Unknown1019(80)
    sprite('ce020_05', 3)	# 50-52
    Unknown1019(80)
    sprite('ce020_06', 3)	# 53-55
    loopRest()
    label(4)
    sprite('ce020_07', 4)	# 56-59
    sprite('ce020_08', 4)	# 60-63
    loopRest()
    gotoLabel(4)
    label(2)
    sprite('ce010_00', 3)	# 64-66
    Unknown8000(100, 1, 1)
    Unknown2001()
    Unknown1084(1)
    Unknown18009(1)
    sprite('ce010_01', 4)	# 67-70
    sprite('ce010_02', 7)	# 71-77

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2004(1, 0)
        Unknown11042(1)
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ce233_00', 2)	# 1-2
    sprite('ce233_01', 1)	# 3-3
    Unknown7007('7063653132315f320000000000000000640000007063653132325f300000000000000000640000007063653132335f320000000000000000640000007063653132345f31000000000000000064000000')
    Unknown23029(11, 103, 0)
    sprite('ce233_01', 1)	# 4-4
    sprite('ce233_02', 4)	# 5-8
    GFX_1('persona_enter_ply', 0)
    sprite('ce233_03', 4)	# 9-12
    sprite('ce233_04', 4)	# 13-16
    sprite('ce233_05', 4)	# 17-20
    sprite('ce233_03', 4)	# 21-24
    sprite('ce233_04', 4)	# 25-28
    sprite('ce233_05', 4)	# 29-32
    sprite('ce233_03', 4)	# 33-36
    sprite('ce233_04', 4)	# 37-40
    sprite('ce233_05', 4)	# 41-44
    sprite('ce233_03', 4)	# 45-48
    sprite('ce233_04', 4)	# 49-52
    sprite('ce233_06', 4)	# 53-56
    sprite('ce233_07', 4)	# 57-60
    sprite('ce010_01', 4)	# 61-64
    sprite('ce010_00', 4)	# 65-68

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11042(1)
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()
        AttackLevel_(3)
        AttackP1(70)
        AirPushbackX(20000)
        AirPushbackY(18000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(31)
        Unknown11028(19)
        Unknown11056(2)
        sendToLabelUpon(2, 0)
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
            SFX_3('down_steal_m')
            Unknown1019(60)
            Unknown1039(120)
            ScreenShake(4000, 1000)

        def upon_12():
            Unknown2037(1)
            SFX_3('counter_hit_l01')
            ScreenShake(1000, 4000)

        def upon_78():
            SLOT_51 = 1

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ce406_00', 1)	# 1-1
    Unknown1084(1)
    sprite('ce406_01', 2)	# 2-3
    sprite('ce406_02', 1)	# 4-4
    sprite('ce406_04', 1)	# 5-5
    SFX_3('runjump_stone_heavy')
    SFX_3('hit_m_slow')
    Unknown8007(100, 1, 1)
    ScreenShake(0, 6000)
    sprite('ce406_05', 3)	# 6-8
    physicsXImpulse(12000)
    sprite('ce406_06', 4)	# 9-12
    SFX_3('slash_blade_fast')
    SFX_3('airdash_l')
    Unknown1019(300)
    Unknown7007('7063653231355f300000000000000000640000007063653231365f320000000000000000640000007063653231365f300000000000000000640000007063653231365f31000000000000000064000000')
    sprite('ce406_07ex', 2)	# 13-14	 **attackbox here**
    GFX_0('100InchPanch_hand', 0)
    GFX_0('100InchPanch_add', 0)
    GFX_0('100InchPanch_dash', 104)
    Unknown8007(100, 0, 1)
    Unknown1019(200)
    physicsYImpulse(4000)
    setGravity(2400)
    RefreshMultihit()
    sprite('ce406_08ex', 2)	# 15-16	 **attackbox here**
    Unknown26('100InchPanch_add')
    label(1)
    sprite('ce406_07ex', 2)	# 17-18	 **attackbox here**
    Unknown8007(100, 0, 1)
    sprite('ce406_08ex', 2)	# 19-20	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 1)	# 21-21
    Unknown26('100InchPanch_hand')
    Unknown1019(60)
    if (not SLOT_2):
        pass
    sprite('ce406_09', 5)	# 22-26
    SFX_3('brake_normal_light')
    Unknown8000(100, 0, 1)
    Unknown8006(100, 1, 1)
    Unknown1019(50)
    if SLOT_51:
        sendToLabel(2)
    sprite('ce406_10', 5)	# 27-31
    Unknown1019(50)
    sprite('ce406_11', 5)	# 32-36
    Unknown1084(1)
    sprite('ce406_12', 5)	# 37-41
    sprite('ce406_13', 5)	# 42-46
    ExitState()
    label(2)
    sprite('ce405_10', 2)	# 47-48
    Unknown1084(1)
    Unknown1051(0)
    Unknown2004(1, 0)
    sprite('ce405_11', 5)	# 49-53
    Unknown23029(11, 410, 0)
    GFX_0('KokutengekiCEtameC', 0)
    sprite('ce405_12', 3)	# 54-56
    loopRest()
    sprite('ce405_03', 3)	# 57-59
    teleportRelativeX(40000)
    Unknown7007('7063653231335f300000000000000000640000007063653231335f310000000000000000640000007063653231345f300000000000000000640000007063653231345f31000000000000000064000000')
    sprite('ce405_04', 3)	# 60-62
    sprite('ce405_05', 3)	# 63-65
    sprite('ce405_06', 3)	# 66-68
    sprite('ce405_04', 3)	# 69-71
    sprite('ce405_05', 3)	# 72-74
    sprite('ce405_06', 3)	# 75-77
    sprite('ce405_04', 3)	# 78-80
    sprite('ce405_07', 4)	# 81-84
    teleportRelativeX(-43000)
    sprite('ce405_08', 4)	# 85-88
    teleportRelativeX(-8000)
    sprite('ce405_09', 4)	# 89-92
    teleportRelativeX(-8000)

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
    sprite('ce020_07', 4)	# 3-6
    sprite('ce020_08', 4)	# 7-10
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
        setInvincible(1)
    sprite('ce000_00', 5)	# 1-5
    sprite('ce430_00', 3)	# 6-8
    sprite('ce430_01', 3)	# 9-11
    Unknown23029(11, 513, 0)
    sprite('ce430_02', 3)	# 12-14
    sprite('ce430_03', 3)	# 15-17
    sprite('ce430_04', 3)	# 18-20
    sprite('ce430_05', 3)	# 21-23
    sprite('ce430_06', 3)	# 24-26
    sprite('ce430_07', 3)	# 27-29
    sprite('ce430_08', 3)	# 30-32
    sprite('ce430_09', 3)	# 33-35
    sprite('ce430_10', 3)	# 36-38
    sprite('ce430_11', 3)	# 39-41
    sprite('ce430_09', 3)	# 42-44
    sprite('ce430_10', 3)	# 45-47
    sprite('ce430_11', 3)	# 48-50
    sprite('ce430_09', 3)	# 51-53
    sprite('ce430_10', 3)	# 54-56
    sprite('ce430_11', 3)	# 57-59
    sprite('ce430_12', 3)	# 60-62
    sprite('ce430_13', 3)	# 63-65
    sprite('ce430_14', 3)	# 66-68
    sprite('ce430_15', 3)	# 69-71
    sprite('ce430_16', 3)	# 72-74
    sprite('ce430_17', 3)	# 75-77
    SFX_4('pce253_1')
    sprite('ce430_15', 3)	# 78-80
    setInvincible(0)
    sprite('ce430_16', 3)	# 81-83
    sprite('ce430_17', 3)	# 84-86
    sprite('ce430_15', 3)	# 87-89
    sprite('ce430_16', 3)	# 90-92
    sprite('ce430_17', 3)	# 93-95
    sprite('ce430_15', 3)	# 96-98
    sprite('ce430_16', 3)	# 99-101
    sprite('ce430_17', 3)	# 102-104
    sprite('ce430_15', 3)	# 105-107
    sprite('ce430_16', 3)	# 108-110
    sprite('ce430_17', 3)	# 111-113
    sprite('ce430_15', 3)	# 114-116
    sprite('ce430_16', 3)	# 117-119
    sprite('ce430_17', 3)	# 120-122
    sprite('ce430_15', 3)	# 123-125
    sprite('ce430_16', 3)	# 126-128
    sprite('ce430_17', 3)	# 129-131
    sprite('ce430_18', 3)	# 132-134

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        setInvincible(1)
    sprite('ce000_00', 5)	# 1-5
    sprite('ce430_00', 3)	# 6-8
    sprite('ce430_01', 3)	# 9-11
    Unknown23029(11, 514, 0)
    sprite('ce430_02', 3)	# 12-14
    sprite('ce430_03', 3)	# 15-17
    sprite('ce430_04', 3)	# 18-20
    sprite('ce430_05', 3)	# 21-23
    sprite('ce430_06', 3)	# 24-26
    sprite('ce430_07', 3)	# 27-29
    sprite('ce430_08', 3)	# 30-32
    sprite('ce430_09', 3)	# 33-35
    sprite('ce430_10', 3)	# 36-38
    sprite('ce430_11', 3)	# 39-41
    sprite('ce430_09', 3)	# 42-44
    sprite('ce430_10', 3)	# 45-47
    sprite('ce430_11', 3)	# 48-50
    sprite('ce430_09', 3)	# 51-53
    sprite('ce430_10', 3)	# 54-56
    sprite('ce430_11', 3)	# 57-59
    sprite('ce430_12', 3)	# 60-62
    sprite('ce430_13', 3)	# 63-65
    sprite('ce430_14', 3)	# 66-68
    sprite('ce430_15', 3)	# 69-71
    sprite('ce430_16', 3)	# 72-74
    sprite('ce430_17', 3)	# 75-77
    SFX_4('pce253_1')
    sprite('ce430_15', 3)	# 78-80
    setInvincible(0)
    sprite('ce430_16', 3)	# 81-83
    sprite('ce430_17', 3)	# 84-86
    sprite('ce430_15', 3)	# 87-89
    sprite('ce430_16', 3)	# 90-92
    sprite('ce430_17', 3)	# 93-95
    sprite('ce430_15', 3)	# 96-98
    sprite('ce430_16', 3)	# 99-101
    sprite('ce430_17', 3)	# 102-104
    sprite('ce430_15', 3)	# 105-107
    sprite('ce430_16', 3)	# 108-110
    sprite('ce430_17', 3)	# 111-113
    sprite('ce430_15', 3)	# 114-116
    sprite('ce430_16', 3)	# 117-119
    sprite('ce430_17', 3)	# 120-122
    sprite('ce430_15', 3)	# 123-125
    sprite('ce430_16', 3)	# 126-128
    sprite('ce430_17', 3)	# 129-131
    sprite('ce430_15', 3)	# 132-134
    sprite('ce430_16', 3)	# 135-137
    sprite('ce430_17', 3)	# 138-140
    sprite('ce430_15', 3)	# 141-143
    sprite('ce430_16', 3)	# 144-146
    sprite('ce430_17', 3)	# 147-149
    sprite('ce430_15', 3)	# 150-152
    sprite('ce430_16', 3)	# 153-155
    sprite('ce430_17', 3)	# 156-158
    sprite('ce430_15', 3)	# 159-161
    sprite('ce430_16', 3)	# 162-164
    sprite('ce430_17', 3)	# 165-167
    sprite('ce430_15', 3)	# 168-170
    sprite('ce430_16', 3)	# 171-173
    sprite('ce430_18', 3)	# 174-176

@State
def CmnActChangeRequest():
    pass

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown2004(1, 0)

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
    sprite('ce600_00ex', 3)	# 129-131	 **attackbox here**
    Unknown2005()
    sprite('ce600_01ex', 3)	# 132-134	 **attackbox here**
    sprite('ce600_00ex', 3)	# 135-137	 **attackbox here**
    sprite('ce600_01ex', 3)	# 138-140	 **attackbox here**
    sprite('ce600_00ex', 3)	# 141-143	 **attackbox here**
    sprite('ce600_01ex', 3)	# 144-146	 **attackbox here**
    sprite('ce600_00ex', 3)	# 147-149	 **attackbox here**
    Unknown2053(1)
    sprite('ce600_01ex', 3)	# 150-152	 **attackbox here**
    sendToLabelUpon(2, 9)
    label(1)
    sprite('ce600_00ex', 3)	# 153-155	 **attackbox here**
    sprite('ce600_01ex', 3)	# 156-158	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 159-161
    Unknown1019(10)
    sprite('ce402_14', 5)	# 162-166
    Unknown2005()
    teleportRelativeX(150000)
    Unknown1019(50)
    Unknown8000(0, 1, 1)
    sprite('ce402_15', 5)	# 167-171
    teleportRelativeX(-265000)
    sprite('ce402_16', 5)	# 172-176
    sprite('ce402_17', 5)	# 177-181
    sprite('ce402_18', 5)	# 182-186
    Unknown1084(1)
    sprite('ce010_02', 3)	# 187-189
    teleportRelativeX(140000)

@State
def CmnActChangeReturnAppealBurst():
    sprite('ce064_01', 50)	# 1-50
    sprite('ce064_02', 5)	# 51-55
    sprite('ce064_03', 25)	# 56-80

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(12000)
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
        callSubroutine('ChargeDamageUp')
    sprite('ce203_00', 2)	# 1-2
    Unknown1015(20000)
    sprite('ce203_01', 2)	# 3-4
    Unknown1019(80)
    sprite('ce203_01', 1)	# 5-5
    Unknown1019(50)
    Unknown7009(1)
    sprite('ce203_02', 2)	# 6-7	 **attackbox here**
    SFX_3('hit_l_slow')
    Unknown1019(0)
    sprite('ce203_03', 2)	# 8-9	 **attackbox here**
    sprite('ce203_04', 2)	# 10-11
    Recovery()
    Unknown2063()
    sprite('ce203_05', 3)	# 12-14
    sprite('ce203_06', 4)	# 15-18
    sprite('ce203_07', 3)	# 19-21
    sprite('ce203_08', 3)	# 22-24
    sprite('ce203_09', 3)	# 25-27

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(950)
        AirPushbackX(-5000)
        AirPushbackY(10000)
        Unknown11092(1)
        Hitstop(12)
        PushbackX(15000)
        Unknown30055('20bf02005a0000005a000000')
        Unknown9154(20)
        AirUntechableTime(20)
        JumpCancel_(1)
        HitOrBlockJumpCancel(1)
        callSubroutine('ChargeDamageUp_Kick')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_STATE_END():
            Unknown1045(0)
    sprite('ce207_00', 3)	# 1-3
    sprite('ce207_01', 1)	# 4-4
    Unknown1045(12000)
    sprite('ce207_02', 2)	# 5-6	 **attackbox here**
    StartMultihit()
    SFX_3('hit_l_slow')
    sprite('ce207_03', 3)	# 7-9	 **attackbox here**
    Unknown1045(-18000)
    RefreshMultihit()
    sprite('ce207_04', 3)	# 10-12
    Unknown7009(1)
    SFX_3('hit_l_slow')
    sprite('ce207_06', 6)	# 13-18	 **attackbox here**
    Unknown23054('63653230375f303500000000000000000000000000000000000000000000000006000000')
    Hitstop(3)
    PushbackX(-26000)
    RefreshMultihit()
    Unknown30055('000000000000000000000000')
    Unknown14070('NmlAtk5A3rd')

    def upon_ON_HIT_OR_BLOCK():
        Unknown2037(1)
    sprite('ce207_06', 1)	# 19-19	 **attackbox here**
    Unknown23027()
    if SLOT_2:
        Unknown14072('NmlAtk5A3rd')
    Recovery()
    Unknown2063()
    sprite('ce207_06', 3)	# 20-22	 **attackbox here**
    sprite('ce207_07', 3)	# 23-25
    Unknown1019(80)
    sprite('ce207_07', 1)	# 26-26
    Unknown14074('NmlAtk5A3rd')
    sprite('ce207_08', 3)	# 27-29
    Unknown1084(1)

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2004(1, 0)
        AttackLevel_(4)
        Damage(750)
        Unknown11092(1)
        AirPushbackX(26000)
        AirPushbackY(16000)
        Hitstop(9)
        sendToLabelUpon(2, 0)
        callSubroutine('ChargeDamageUp_Kick')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
            Unknown2038(1)
    sprite('ce208_00', 3)	# 1-3
    sprite('ce208_01', 3)	# 4-6
    sprite('ce208_02', 3)	# 7-9
    physicsXImpulse(40000)
    physicsYImpulse(23000)
    Unknown8001(1, 0)
    SFX_3('hit_l_slow')
    sprite('ce208_03', 2)	# 10-11	 **attackbox here**
    Unknown1019(60)
    YAccel(80)
    setGravity(2800)
    RefreshMultihit()
    Unknown7009(2)
    sprite('ce208_04', 3)	# 12-14
    sprite('ce208_05', 3)	# 15-17
    sprite('ce208_06', 3)	# 18-20
    sprite('ce208_07', 3)	# 21-23
    SFX_3('hit_l_slow')
    sprite('ce208_08', 3)	# 24-26	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(18000)
    AirPushbackY(10000)
    sprite('ce208_09', 32767)	# 27-32793
    label(0)
    sprite('ce208_10', 4)	# 32794-32797
    Unknown1084(1)
    Unknown1047(15000)
    Unknown8000(100, 1, 1)
    sprite('ce208_11', 4)	# 32798-32801
    SFX_3('hit_l_slow')
    sprite('ce208_13', 3)	# 32802-32804	 **attackbox here**
    Unknown23054('63653230385f313200000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    GroundedHitstunAnimation(0)
    AirHitstunAnimation(9)
    AirPushbackX(15000)
    AirPushbackY(15000)
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        HitOrBlockCancel('NmlAtkKokutengeki')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('ce208_13', 7)	# 32805-32811	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ce208_14', 3)	# 32812-32814
    sprite('ce208_15', 6)	# 32815-32820
    sprite('ce208_16', 3)	# 32821-32823

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        AirPushbackY(20000)
        WhiffCancel('NmlAtk4A')
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
        callSubroutine('ChargeDamageUp')
    sprite('ce200_00', 2)	# 1-2
    sprite('ce200_01', 1)	# 3-3
    sprite('ce200_01', 1)	# 4-4
    sprite('ce200_03', 3)	# 5-7	 **attackbox here**
    Unknown23054('63653230305f303200000000000000000000000000000000000000000000000003000000')
    Unknown7009(0)
    SFX_3('hit_l_fast')
    sprite('ce200_03', 5)	# 8-12	 **attackbox here**
    WhiffCancelEnable(1)
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ce200_04', 6)	# 13-18
    WhiffCancelEnable(0)

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(400)
        Hitstop(1)
        PushbackX(9000)
        AirPushbackY(4000)
        Unknown11092(1)
        HitOrBlockJumpCancel(1)
        callSubroutine('ChargeDamageUp_Kick')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('ce201_00', 2)	# 1-2
    Unknown1047(15000)
    sprite('ce201_01', 2)	# 3-4
    sprite('ce201_02', 4)	# 5-8
    Unknown7009(1)
    sprite('ce201_03', 2)	# 9-10	 **attackbox here**
    SFX_3('hit_l_fast')
    RefreshMultihit()
    sprite('ce201_04', 2)	# 11-12
    sprite('ce201_05', 2)	# 13-14
    sprite('ce201_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ce201_07', 2)	# 17-18
    sprite('ce201_05', 2)	# 19-20
    sprite('ce201_08', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ce201_09', 2)	# 23-24
    sprite('ce201_02', 2)	# 25-26
    sprite('ce201_03', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ce201_04', 2)	# 29-30
    sprite('ce201_05', 2)	# 31-32
    sprite('ce201_06', 2)	# 33-34	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ce201_07', 2)	# 35-36
    sprite('ce201_05', 2)	# 37-38
    sprite('ce201_08', 2)	# 39-40	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ce201_09', 2)	# 41-42
    Recovery()
    Unknown2063()
    sprite('ce201_02', 6)	# 43-48
    SFX_3('hit_l_fast')
    sprite('ce201_10', 6)	# 49-54
    sprite('ce201_01', 4)	# 55-58
    sprite('ce201_00', 3)	# 59-61

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2004(1, 0)
        AttackLevel_(3)
        Damage(1000)
        PushbackX(-60000)
        AirPushbackX(-6000)
        AirPushbackY(18000)
        Unknown11092(1)
        callSubroutine('ChargeDamageUp_Kick')

        def upon_STATE_END():
            Unknown1084(1)
            Unknown1051(0)
    sprite('ce202_00', 2)	# 1-2
    teleportRelativeX(50000)
    sprite('ce202_01', 3)	# 3-5
    Unknown7009(2)
    sprite('ce202_02', 1)	# 6-6	 **attackbox here**
    SFX_3('hit_l_slow')
    Unknown1047(-20000)
    RefreshMultihit()
    Unknown14070('NmlAtkKokutengeki')
    Unknown14070('CmnActCrushAttack')
    Unknown14070('NmlAtk2C')
    callSubroutine('LandSpecialAttack_DeriveInput')
    sprite('ce202_02', 2)	# 7-8	 **attackbox here**
    sprite('ce202_03', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    PushbackX(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown2037(1)
    sprite('ce202_03', 2)	# 10-11	 **attackbox here**
    HitOrBlockJumpCancel(1)
    if SLOT_2:
        Unknown14072('NmlAtkKokutengeki')
        Unknown14072('CmnActCrushAttack')
        Unknown14072('NmlAtk2C')
        callSubroutine('LandSpecialAttack_DeriveTiming')
    sprite('ce202_04', 1)	# 12-12
    Recovery()
    Unknown2063()
    sprite('ce202_04', 3)	# 13-15
    sprite('ce202_05', 3)	# 16-18
    sprite('ce202_05', 2)	# 19-20
    Unknown14074('NmlAtkKokutengeki')
    Unknown14074('CmnActCrushAttack')
    Unknown14074('NmlAtk2C')
    callSubroutine('LandSpecialAttack_DeriveClear')
    sprite('ce202_06', 6)	# 21-26
    Unknown2001()

@State
def NmlAtkKokutengeki():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2004(1, 0)
        Unknown2006()
        Unknown2017(1)
        Unknown2015(180)
        Unknown2021(1)
        JumpCancel_(0)
    sprite('ce405_00', 4)	# 1-4
    Unknown1084(1)
    Unknown1051(0)
    sprite('ce405_01', 5)	# 5-9
    Unknown23029(11, 407, 0)
    GFX_0('KokutengekiCEtameC', 0)
    sprite('ce405_02', 3)	# 10-12
    teleportRelativeX(58000)
    loopRest()
    sprite('ce405_03', 3)	# 13-15
    teleportRelativeX(40000)
    Unknown7007('7063653231335f300000000000000000640000007063653231335f310000000000000000640000007063653231345f300000000000000000640000007063653231345f31000000000000000064000000')
    sprite('ce405_04', 3)	# 16-18
    sprite('ce405_05', 3)	# 19-21
    sprite('ce405_06', 3)	# 22-24
    sprite('ce405_04', 3)	# 25-27
    Recovery()
    sprite('ce405_05', 3)	# 28-30
    sprite('ce405_06', 3)	# 31-33
    sprite('ce405_04', 3)	# 34-36
    sprite('ce405_07', 4)	# 37-40
    teleportRelativeX(-43000)
    sprite('ce405_08', 4)	# 41-44
    teleportRelativeX(-8000)
    sprite('ce405_09', 4)	# 45-48
    teleportRelativeX(-8000)

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown1112('')
        HitOrBlockCancel('DashCancel')
    sprite('ce204_00', 2)	# 1-2
    sprite('ce204_01', 1)	# 3-3
    sprite('ce204_01', 3)	# 4-6
    Unknown23029(11, 101, 0)
    sprite('ce204_02', 4)	# 7-10
    GFX_1('persona_enter_ply', 0)
    Unknown7007('7063653330355f300000000000000000640000007063653132305f310000000000000000640000007063653132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ce204_03', 2)	# 11-12
    sprite('ce204_03', 2)	# 13-14
    Recovery()
    Unknown2063()
    sprite('ce204_04', 4)	# 15-18
    sprite('ce204_05', 4)	# 19-22
    sprite('ce204_03', 4)	# 23-26
    sprite('ce204_04', 4)	# 27-30
    sprite('ce204_05', 4)	# 31-34
    sprite('ce204_01', 4)	# 35-38
    sprite('ce204_00', 4)	# 39-42

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 1101):
                clearUponHandler(43)
                Unknown14072('CmnActCrushAttack')
                Unknown14072('NmlAtk2C')
                callSubroutine('LandSpecialAttack_DeriveTiming')
                Unknown13024(1)
                HitOrBlockCancel('DashCancel')
    sprite('ce205_00', 3)	# 1-3
    sprite('ce205_01', 4)	# 4-7
    Unknown23029(11, 201, 0)
    sprite('ce205_02', 4)	# 8-11
    Unknown7007('7063653132315f300000000000000000640000007063653132315f310000000000000000640000007063653132335f300000000000000000640000007063653132335f31000000000000000064000000')
    sprite('ce205_03', 3)	# 12-14
    GFX_1('persona_enter_ply', 0)
    sprite('ce205_03', 2)	# 15-16
    Unknown14070('CmnActCrushAttack')
    Unknown14070('NmlAtk2C')
    callSubroutine('LandSpecialAttack_DeriveInput')
    sprite('ce205_04', 4)	# 17-20
    sprite('ce205_05', 4)	# 21-24
    sprite('ce205_06', 4)	# 25-28
    sprite('ce205_04', 2)	# 29-30
    sprite('ce205_04', 2)	# 31-32
    Recovery()
    Unknown2063()
    sprite('ce205_05', 4)	# 33-36
    sprite('ce205_06', 1)	# 37-37
    sprite('ce205_06', 3)	# 38-40
    Unknown14074('CmnActCrushAttack')
    Unknown14074('NmlAtk2C')
    callSubroutine('LandSpecialAttack_DeriveClear')
    sprite('ce205_07', 4)	# 41-44
    sprite('ce205_08', 4)	# 45-48

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2004(1, 0)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 1202):
                clearUponHandler(43)
                Unknown2038(1)
    sprite('ce205_00', 4)	# 1-4
    sprite('ce205_01', 4)	# 5-8
    Unknown7007('7063653132315f320000000000000000640000007063653132325f300000000000000000640000007063653132335f320000000000000000640000007063653132345f31000000000000000064000000')
    Unknown23029(11, 103, 0)
    sprite('ce205_02', 4)	# 9-12
    sprite('ce205_03', 5)	# 13-17
    GFX_1('persona_enter_ply', 0)
    sprite('ce205_04', 4)	# 18-21
    sprite('ce205_05', 4)	# 22-25
    sprite('ce205_06', 4)	# 26-29
    sprite('ce205_04', 4)	# 30-33
    sprite('ce205_05', 4)	# 34-37
    sprite('ce205_06', 4)	# 38-41
    if CheckInput(0xa):
        Unknown23029(11, 1201, 0)
        sendToLabel(99)
    sprite('ce205_04', 4)	# 42-45
    sprite('ce205_05', 4)	# 46-49
    sprite('ce205_06', 4)	# 50-53
    sprite('ce205_04', 4)	# 54-57
    sprite('ce205_05', 4)	# 58-61
    sprite('ce205_06', 4)	# 62-65
    if SLOT_2:
        JumpCancel_(1)
    sprite('ce205_04', 4)	# 66-69
    sprite('ce205_05', 4)	# 70-73
    sprite('ce205_07', 4)	# 74-77
    sprite('ce205_08', 4)	# 78-81
    ExitState()
    label(99)
    sprite('ce205_04', 4)	# 82-85
    sprite('ce205_05', 4)	# 86-89
    sprite('ce205_06', 4)	# 90-93
    sprite('ce205_04', 4)	# 94-97
    sprite('ce205_05', 4)	# 98-101
    sprite('ce205_06', 4)	# 102-105
    sprite('ce205_04', 4)	# 106-109
    sprite('ce205_05', 4)	# 110-113
    sprite('ce205_06', 4)	# 114-117
    sprite('ce205_04', 4)	# 118-121
    if SLOT_2:
        JumpCancel_(1)
    sprite('ce205_05', 4)	# 122-125
    sprite('ce205_06', 4)	# 126-129
    sprite('ce205_07', 4)	# 130-133
    sprite('ce205_08', 4)	# 134-137

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('ChargeDamageUp')
    sprite('ce230_00', 2)	# 1-2
    sprite('ce230_01', 1)	# 3-3
    sprite('ce230_01', 1)	# 4-4
    Unknown1051(80)
    sprite('ce230_02', 1)	# 5-5
    Unknown7009(0)
    sprite('ce230_04', 2)	# 6-7	 **attackbox here**
    Unknown23054('63653233305f303300000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_l_fast')
    RefreshMultihit()
    sprite('ce230_04', 5)	# 8-12	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ce230_01', 4)	# 13-16
    WhiffCancelEnable(1)
    sprite('ce230_00', 3)	# 17-19

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Unknown2004(1, 0)
        AttackLevel_(3)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        callSubroutine('ChargeDamageUp_Kick')
        Unknown28(8, '_NEUTRAL')
        Unknown11058('0000000001000000000000000000000000000000')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce231_00', 3)	# 1-3
    sprite('ce231_00', 1)	# 4-4
    Unknown1015(52500)
    Unknown8007(100, 1, 0)
    Unknown7007('7063653130365f300000000000000000640000007063653130365f310000000000000000640000007063653130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ce231_00', 1)	# 5-5
    Unknown1019(90)
    SFX_3('hit_l_middle')
    sprite('ce231_00', 1)	# 6-6
    Unknown1019(90)
    sprite('ce231_00', 1)	# 7-7
    Unknown1019(80)
    sprite('ce231_01', 2)	# 8-9
    Unknown1019(50)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ce231_03', 2)	# 10-11	 **attackbox here**
    Unknown23054('63653233315f303200000000000000000000000000000000000000000000000003000000')
    Unknown1019(0)
    Unknown18009(0)
    RefreshMultihit()
    Unknown8006(100, 1, 0)
    sprite('ce231_03', 10)	# 12-21	 **attackbox here**
    setInvincible(0)
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ce231_04', 4)	# 22-25
    sprite('ce231_05', 4)	# 26-29
    sprite('ce231_06', 4)	# 30-33
    sprite('ce231_07', 4)	# 34-37
    sprite('ce231_08', 4)	# 38-41

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        Unknown2004(1, 0)
        AttackLevel_(4)
        AttackP1(90)
        AirPushbackY(13000)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(24)
        HitOrBlockJumpCancel(1)
        callSubroutine('ChargeDamageUp_Kick')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')

        def upon_3():
            Unknown1019(90)
    sprite('ce211_00', 2)	# 1-2
    physicsXImpulse(20000)
    sprite('ce211_01', 1)	# 3-3
    sprite('ce211_01', 1)	# 4-4
    SFX_3('hit_l_middle')
    sprite('ce211_02', 2)	# 5-6
    sprite('ce211_03', 2)	# 7-8
    sprite('ce211_05', 3)	# 9-11	 **attackbox here**
    Unknown23054('63653231315f303400000000000000000000000000000000000000000000000002000000')
    Unknown7007('7063653130375f300000000000000000640000007063653130375f310000000000000000640000007063653130375f320000000000000000640000000000000000000000000000000000000000000000')
    RefreshMultihit()
    Unknown1084(1)
    clearUponHandler(3)
    sprite('ce211_05', 8)	# 12-19	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ce211_06', 3)	# 20-22
    sprite('ce211_07', 3)	# 23-25
    sprite('ce211_08', 3)	# 26-28
    sprite('ce211_09', 3)	# 29-31

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackX(6000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        callSubroutine('ChargeDamageUp_Kick')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce251_00', 1)	# 1-1
    sprite('ce251_01', 2)	# 2-3
    sprite('ce251_02', 2)	# 4-5
    Unknown7009(1)
    sprite('ce251_03', 2)	# 6-7
    sprite('ce251_05', 3)	# 8-10	 **attackbox here**
    Unknown23054('63653235315f303400000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_l_slow')
    RefreshMultihit()
    sprite('ce251_05', 1)	# 11-11	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ce251_06', 3)	# 12-14
    sprite('ce251_07', 3)	# 15-17
    sprite('ce251_08', 3)	# 18-20
    sprite('ce251_09', 3)	# 21-23

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        callSubroutine('ChargeDamageUp_Kick')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce252_00', 3)	# 1-3
    SFX_3('hit_l_middle')
    sprite('ce252_01', 3)	# 4-6
    Unknown7009(1)
    sprite('ce252_03', 3)	# 7-9	 **attackbox here**
    Unknown23054('63653235325f303200000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('ce252_03', 2)	# 10-11	 **attackbox here**
    sprite('ce252_03', 2)	# 12-13	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ce252_04', 3)	# 14-16
    sprite('ce252_05', 3)	# 17-19
    sprite('ce252_06', 3)	# 20-22
    sprite('ce252_07', 3)	# 23-25

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_LANDING():
            Unknown23029(11, 3001, 0)

        def upon_STATE_END():
            Unknown23029(11, 3002, 0)
        Unknown4009(11)
    sprite('ce254_00', 5)	# 1-5
    sprite('ce254_01', 3)	# 6-8
    Unknown23029(11, 301, 0)
    sprite('ce254_02', 4)	# 9-12
    Unknown7007('7063653132305f320000000000000000640000007063653132305f310000000000000000640000007063653132305f320000000000000000640000000000000000000000000000000000000064000000')
    sprite('ce254_03', 3)	# 13-15
    GFX_1('persona_enter_ply', 0)
    sprite('ce254_04', 1)	# 16-16
    sprite('ce254_04', 2)	# 17-18
    Recovery()
    Unknown2063()
    sprite('ce254_05', 3)	# 19-21
    sprite('ce254_06', 3)	# 22-24
    sprite('ce254_00', 3)	# 25-27

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown4009(11)

        def upon_STATE_END():
            Unknown4009(0)
    sprite('ce255_00', 4)	# 1-4
    sprite('ce255_01', 4)	# 5-8
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown7007('7063653132325f300000000000000000640000007063653132335f320000000000000000640000007063653132305f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('ce255_02', 4)	# 9-12
    Unknown23029(11, 302, 0)
    GFX_1('persona_enter_ply', 0)
    sprite('ce255_03', 4)	# 13-16
    sprite('ce255_04', 4)	# 17-20
    sprite('ce255_05', 2)	# 21-22
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(70)
    YAccel(70)
    sprite('ce255_05', 2)	# 23-24
    Recovery()
    sprite('ce255_06', 4)	# 25-28

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        sendToLabelUpon(2, 0)
    sprite('ce210_00', 2)	# 1-2
    sprite('ce210_01', 2)	# 3-4
    sprite('ce210_02', 2)	# 5-6
    sprite('ce210_03', 2)	# 7-8
    tag_voice(1, 'pce162_0', 'pce162_1', '', '')
    sprite('ce210_03', 1)	# 9-9
    physicsYImpulse(40000)
    physicsXImpulse(15000)
    setGravity(8000)
    sprite('ce210_03', 2)	# 10-11
    sprite('ce210_04', 2)	# 12-13
    sprite('ce210_05', 4)	# 14-17
    sprite('ce210_06', 32767)	# 18-32784
    loopRest()
    label(0)
    sprite('ce210_08', 3)	# 32785-32787	 **attackbox here**
    Unknown23054('63653231305f303700000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_l_slow')
    ScreenShake(0, 3000)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ce210_08', 7)	# 32788-32794	 **attackbox here**
    Unknown23027()
    sprite('ce210_09', 5)	# 32795-32799
    sprite('ce210_10', 4)	# 32800-32803
    sprite('ce210_11', 4)	# 32804-32807
    sprite('ce210_12', 4)	# 32808-32811

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
    sprite('ce210_08', 6)	# 2-7	 **attackbox here**
    sprite('ce210_09', 4)	# 8-11
    sprite('ce210_10', 3)	# 12-14
    sprite('ce210_11', 3)	# 15-17
    sprite('ce210_12', 3)	# 18-20
    sprite('ce000_00', 3)	# 21-23
    sprite('ce203_00', 2)	# 24-25
    Unknown1015(20000)
    sprite('ce203_01', 2)	# 26-27
    Unknown1019(80)
    sprite('ce203_01', 2)	# 28-29
    Unknown1019(50)
    sprite('ce203_02', 2)	# 30-31	 **attackbox here**
    SFX_3('hit_l_slow')
    Unknown1019(0)
    RefreshMultihit()
    sprite('ce203_03', 2)	# 32-33	 **attackbox here**
    Unknown23027()
    sprite('ce203_04', 3)	# 34-36
    sprite('ce203_08', 3)	# 37-39
    sprite('ce203_09', 13)	# 40-52
    sprite('ce001_00', 6)	# 53-58
    sprite('ce001_01', 6)	# 59-64
    sprite('ce001_02', 6)	# 65-70
    sprite('ce001_03', 6)	# 71-76
    sprite('ce001_04', 6)	# 77-82
    sprite('ce001_05', 6)	# 83-88
    sprite('ce001_00', 6)	# 89-94
    label(0)
    sprite('ce000_00', 6)	# 95-100
    sprite('ce000_01', 6)	# 101-106
    sprite('ce000_02', 6)	# 107-112
    sprite('ce000_03', 6)	# 113-118
    sprite('ce000_04', 6)	# 119-124
    sprite('ce000_05', 6)	# 125-130
    sprite('ce000_06', 6)	# 131-136
    sprite('ce000_07', 6)	# 137-142
    sprite('ce000_08', 6)	# 143-148
    sprite('ce000_09', 6)	# 149-154
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 155-155

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
    sprite('ce204_00', 2)	# 1-2
    sprite('ce204_00', 2)	# 3-4
    tag_voice(0, 'pce163_0', 'pce163_1', '', '')
    sprite('ce204_01', 1)	# 5-5
    sprite('ce204_01', 3)	# 6-8
    Unknown23029(11, 105, 0)
    Unknown4020(11)
    sprite('ce204_01', 1)	# 9-9
    RefreshMultihit()
    sprite('ce204_02', 4)	# 10-13
    GFX_1('persona_enter_ply', 0)
    sprite('ce204_03', 2)	# 14-15
    sprite('ce204_03', 2)	# 16-17
    sprite('ce204_04', 4)	# 18-21
    sprite('ce204_05', 4)	# 22-25
    sprite('ce204_03', 4)	# 26-29
    sprite('ce204_04', 4)	# 30-33
    sprite('ce204_05', 4)	# 34-37
    sprite('ce204_03', 4)	# 38-41
    sprite('ce204_04', 4)	# 42-45
    sprite('ce204_05', 4)	# 46-49
    sprite('ce204_03', 4)	# 50-53
    sprite('ce204_04', 4)	# 54-57
    sprite('ce204_05', 4)	# 58-61
    sprite('ce204_03', 4)	# 62-65
    sprite('ce204_04', 4)	# 66-69
    sprite('ce204_05', 4)	# 70-73
    sprite('ce204_03', 4)	# 74-77
    sprite('ce204_04', 4)	# 78-81
    sprite('ce204_05', 4)	# 82-85
    label(0)
    sprite('ce000_00', 6)	# 86-91
    sprite('ce000_01', 6)	# 92-97
    sprite('ce000_02', 6)	# 98-103
    sprite('ce000_03', 6)	# 104-109
    sprite('ce000_04', 6)	# 110-115
    sprite('ce000_05', 6)	# 116-121
    sprite('ce000_06', 6)	# 122-127
    sprite('ce000_07', 6)	# 128-133
    sprite('ce000_08', 6)	# 134-139
    sprite('ce000_09', 6)	# 140-145
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 146-146

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
        Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
    sprite('ce205_00', 3)	# 1-3
    sprite('ce205_01', 2)	# 4-5
    sprite('ce205_01', 1)	# 6-6
    sprite('ce205_02', 1)	# 7-7
    sprite('ce205_02', 1)	# 8-8
    Unknown23029(11, 106, 0)
    Unknown4020(11)
    sprite('ce205_03', 2)	# 9-10
    GFX_1('persona_enter_ply', 0)
    sprite('ce205_04', 4)	# 11-14
    tag_voice(0, 'pce164_0', 'pce164_1', '', '')
    sprite('ce205_05', 2)	# 15-16
    sprite('ce205_05', 2)	# 17-18
    RefreshMultihit()
    sprite('ce205_06', 4)	# 19-22
    sprite('ce205_04', 4)	# 23-26
    sprite('ce205_05', 4)	# 27-30
    sprite('ce205_06', 4)	# 31-34
    sprite('ce205_04', 4)	# 35-38
    sprite('ce205_05', 4)	# 39-42
    sprite('ce205_06', 4)	# 43-46
    sprite('ce205_04', 4)	# 47-50
    sprite('ce205_07', 5)	# 51-55
    sprite('ce205_08', 4)	# 56-59
    loopRest()

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
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
    sprite('ce020_07', 4)	# 24-27
    physicsXImpulse(35000)
    physicsYImpulse(-25000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('ce020_08', 4)	# 28-31
    sprite('ce020_07', 4)	# 32-35
    sprite('ce252_00', 3)	# 36-38
    SFX_3('hit_l_middle')
    sprite('ce252_01', 3)	# 39-41
    sprite('ce252_03', 3)	# 42-44	 **attackbox here**
    Unknown23054('63653235325f303200000000000000000000000000000000000000000000000003000000')
    sprite('ce252_03', 3)	# 45-47	 **attackbox here**
    sprite('ce252_04', 3)	# 48-50
    sprite('ce252_05', 3)	# 51-53
    sprite('ce252_06', 3)	# 54-56
    sprite('ce252_07', 3)	# 57-59
    sprite('keep', 32767)	# 60-32826
    label(2)
    sprite('ce010_01', 3)	# 32827-32829
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('ce010_00', 4)	# 32830-32833
    sprite('ce000_00', 6)	# 32834-32839
    sprite('ce000_01', 6)	# 32840-32845
    sprite('ce000_02', 6)	# 32846-32851
    sprite('ce000_03', 6)	# 32852-32857
    sprite('ce000_04', 6)	# 32858-32863
    sprite('ce000_05', 6)	# 32864-32869
    sprite('ce000_06', 6)	# 32870-32875
    sprite('ce000_07', 6)	# 32876-32881
    sprite('ce000_08', 6)	# 32882-32887
    sprite('ce000_09', 6)	# 32888-32893

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
        Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
    sprite('keep', 2)	# 1-2
    sprite('ce204_00', 2)	# 3-4
    sprite('ce204_01', 1)	# 5-5
    Unknown23029(11, 104, 0)
    Unknown4020(11)
    sprite('ce204_01', 2)	# 6-7
    sprite('ce204_01', 1)	# 8-8
    RefreshMultihit()
    sprite('ce204_02', 4)	# 9-12
    GFX_1('persona_enter_ply', 0)
    sprite('ce204_03', 2)	# 13-14
    sprite('ce204_03', 2)	# 15-16
    sprite('ce204_04', 4)	# 17-20
    sprite('ce204_05', 4)	# 21-24
    sprite('ce204_03', 4)	# 25-28
    sprite('ce204_04', 4)	# 29-32
    sprite('ce204_05', 4)	# 33-36
    sprite('ce204_03', 4)	# 37-40
    sprite('ce204_04', 4)	# 41-44
    sprite('ce204_05', 4)	# 45-48
    sprite('ce204_03', 4)	# 49-52
    sprite('ce204_04', 4)	# 53-56
    sprite('ce204_05', 4)	# 57-60
    sprite('ce204_03', 4)	# 61-64
    sprite('ce204_04', 4)	# 65-68
    sprite('ce204_05', 4)	# 69-72
    sprite('ce204_03', 4)	# 73-76
    sprite('ce204_04', 4)	# 77-80
    sprite('ce204_05', 4)	# 81-84
    sprite('ce000_00', 6)	# 85-90
    sprite('ce000_01', 6)	# 91-96
    sprite('ce000_02', 6)	# 97-102
    sprite('ce000_03', 6)	# 103-108
    sprite('ce000_04', 6)	# 109-114
    sprite('ce000_05', 6)	# 115-120
    sprite('ce000_06', 6)	# 121-126
    sprite('ce000_07', 6)	# 127-132
    sprite('ce000_08', 6)	# 133-138
    sprite('ce000_09', 6)	# 139-144

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
    sprite('ce205_00', 3)	# 1-3
    sprite('ce205_01', 2)	# 4-5
    sprite('ce205_01', 1)	# 6-6
    sprite('ce205_02', 1)	# 7-7
    sprite('ce205_02', 1)	# 8-8
    Unknown23029(11, 106, 0)
    Unknown4020(11)
    sprite('ce205_03', 2)	# 9-10
    GFX_1('persona_enter_ply', 0)
    sprite('ce205_04', 4)	# 11-14
    sprite('ce205_05', 2)	# 15-16
    sprite('ce205_05', 2)	# 17-18
    RefreshMultihit()
    sprite('ce205_06', 4)	# 19-22
    sprite('ce205_04', 4)	# 23-26
    sprite('ce205_05', 4)	# 27-30
    sprite('ce205_06', 4)	# 31-34
    sprite('ce205_04', 4)	# 35-38
    sprite('ce205_05', 4)	# 39-42
    sprite('ce205_06', 4)	# 43-46
    sprite('ce205_04', 4)	# 47-50
    sprite('ce205_07', 5)	# 51-55
    sprite('ce205_08', 4)	# 56-59
    loopRest()

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ce030_00', 4)	# 1-4
    sprite('ce032_00', 2)	# 5-6
    label(0)
    sprite('ce032_01', 4)	# 7-10
    sprite('ce032_02', 4)	# 11-14
    sprite('ce032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('ce032_04', 4)	# 19-22
    sprite('ce032_05', 4)	# 23-26
    sprite('ce032_06', 4)	# 27-30
    sprite('ce032_07', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('ce032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce310_00', 1)	# 39-39
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ce310_01', 2)	# 40-41
    sprite('ce310_02', 3)	# 42-44	 **attackbox here**
    Unknown1084(1)
    sprite('ce310_03', 3)	# 45-47
    sprite('ce310_04', 12)	# 48-59
    SFX_4('pce160')
    Unknown2015(180)
    sprite('ce310_03', 4)	# 60-63
    Unknown2015(-1)
    sprite('ce310_02', 4)	# 64-67	 **attackbox here**
    StartMultihit()

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-2000)
        AirPushbackY(-10000)
        AirUntechableTime(20)
        Unknown9310(45)
        JumpCancel_(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2004(1, 0)
        Unknown11069('ThrowExe')
        sendToLabelUpon(2, 0)
    sprite('ce310_02', 4)	# 1-4	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    Unknown5003(1)
    sprite('ce311_00', 3)	# 5-7
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce311_01', 3)	# 8-10
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce311_02', 3)	# 11-13
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce311_03', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(2000)
    physicsYImpulse(26000)
    setGravity(2200)
    sprite('ce311_04', 3)	# 17-19
    sprite('ce311_05', 3)	# 20-22
    sprite('ce311_06', 4)	# 23-26
    sprite('ce311_07', 4)	# 27-30
    sprite('ce311_08', 4)	# 31-34
    sprite('ce311_09', 32767)	# 35-32801	 **attackbox here**
    SFX_4('pce159')
    Unknown23027()
    loopRest()
    label(0)
    sprite('ce311_10', 4)	# 32802-32805	 **attackbox here**
    Unknown23054('63653331315f303900000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    AttackP2(50)
    AirPushbackX(10000)
    AirPushbackY(-40000)
    Hitstop(6)
    callSubroutine('ChargeDamageUp')
    Unknown11050('010000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')
    sprite('ce311_10', 3)	# 32806-32808	 **attackbox here**
    Unknown23027()
    physicsXImpulse(-1000)
    physicsYImpulse(18000)
    setGravity(2000)
    sendToLabelUpon(2, 1)
    sprite('ce311_11', 3)	# 32809-32811
    sprite('ce311_12', 32767)	# 32812-65578
    label(1)
    sprite('ce311_13', 4)	# 65579-65582
    Unknown1084(1)
    Unknown2005()
    Unknown23073()
    sprite('ce311_14', 4)	# 65583-65586
    sprite('ce311_15', 4)	# 65587-65590
    sprite('ce311_16', 3)	# 65591-65593
    sprite('ce000_00', 1)	# 65594-65594
    Unknown2005()
    teleportRelativeX(-90000)

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ce030_00', 4)	# 1-4
    sprite('ce032_00', 2)	# 5-6
    label(0)
    sprite('ce032_01', 4)	# 7-10
    sprite('ce032_02', 4)	# 11-14
    sprite('ce032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('ce032_04', 4)	# 19-22
    sprite('ce032_05', 4)	# 23-26
    sprite('ce032_06', 4)	# 27-30
    sprite('ce032_07', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('ce032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce310_00', 1)	# 39-39
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ce310_01', 2)	# 40-41
    sprite('ce310_02', 3)	# 42-44	 **attackbox here**
    Unknown1084(1)
    sprite('ce310_03', 3)	# 45-47
    sprite('ce310_04', 12)	# 48-59
    SFX_4('pce160')
    Unknown2015(180)
    sprite('ce310_03', 4)	# 60-63
    Unknown2015(-1)
    sprite('ce310_02', 4)	# 64-67	 **attackbox here**
    StartMultihit()

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-2000)
        AirPushbackY(-10000)
        AirUntechableTime(20)
        Unknown9310(45)
        JumpCancel_(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2004(1, 0)
        Unknown11069('BackThrowExe')
        sendToLabelUpon(2, 0)
    sprite('ce310_02', 4)	# 1-4	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    Unknown5003(1)
    sprite('ce311_00', 3)	# 5-7
    Unknown2005()
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce311_01', 3)	# 8-10
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce311_02', 3)	# 11-13
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('ce311_03', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(2000)
    physicsYImpulse(26000)
    setGravity(2200)
    sprite('ce311_04', 3)	# 17-19
    sprite('ce311_05', 3)	# 20-22
    sprite('ce311_06', 4)	# 23-26
    sprite('ce311_07', 4)	# 27-30
    sprite('ce311_08', 4)	# 31-34
    sprite('ce311_09', 32767)	# 35-32801	 **attackbox here**
    SFX_4('pce159')
    Unknown23027()
    loopRest()
    label(0)
    sprite('ce311_10', 4)	# 32802-32805	 **attackbox here**
    Unknown23054('63653331315f303900000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    AttackP2(50)
    AirPushbackX(10000)
    AirPushbackY(-40000)
    Hitstop(6)
    callSubroutine('ChargeDamageUp')
    Unknown11050('010000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')
    sprite('ce311_10', 3)	# 32806-32808	 **attackbox here**
    Unknown23027()
    physicsXImpulse(-1000)
    physicsYImpulse(18000)
    setGravity(2000)
    sendToLabelUpon(2, 1)
    sprite('ce311_11', 3)	# 32809-32811
    sprite('ce311_12', 32767)	# 32812-65578
    label(1)
    sprite('ce311_13', 4)	# 65579-65582
    Unknown1084(1)
    Unknown2005()
    Unknown23073()
    sprite('ce311_14', 4)	# 65583-65586
    sprite('ce311_15', 4)	# 65587-65590
    sprite('ce311_16', 3)	# 65591-65593
    sprite('ce000_00', 1)	# 65594-65594
    Unknown2005()
    teleportRelativeX(-90000)

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(2)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(12000)
        AirPushbackY(15000)
        HitLow(2)
        Hitstop(4)
        Unknown11063(1)
        Damage(950)
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce400_00', 3)	# 1-3
    SFX_3('cut_l')
    GFX_0('Hyper_Counter_Barrier_r', 0)
    GFX_0('Hyper_Counter_Barrier', 0)
    Unknown1084(0)
    GuardPoint_(1)
    Unknown22031(-1, 15)
    sendToLabelUpon(42, 0)
    tag_voice(1, 'pce205_0', 'pce205_1', 'pce205_2', 'pce205_1')
    sprite('ce400_01', 3)	# 4-6
    sprite('ce400_02', 3)	# 7-9
    sprite('ce400_00', 3)	# 10-12
    sprite('ce400_01', 3)	# 13-15
    sprite('ce400_02', 3)	# 16-18
    setInvincible(0)
    sprite('ce400_00', 3)	# 19-21
    sprite('ce400_01', 3)	# 22-24
    sprite('ce400_02', 3)	# 25-27
    sprite('ce400_00', 3)	# 28-30
    sprite('ce400_01', 3)	# 31-33
    sprite('ce400_02', 3)	# 34-36
    sprite('ce400_00', 3)	# 37-39
    sprite('ce400_01', 3)	# 40-42
    sprite('ce400_03', 3)	# 43-45
    ExitState()
    label(0)
    sprite('ce401_00', 2)	# 46-47
    clearUponHandler(42)
    GuardPoint_(0)
    sprite('ce401_01', 2)	# 48-49
    sprite('ce401_02', 2)	# 50-51	 **attackbox here**
    SFX_3('bound_marble_m')
    ScreenShake(0, 3000)
    RefreshMultihit()
    Unknown26('Hyper_Counter_Barrier')
    Unknown26('Hyper_Counter_Barrier_r')
    sprite('ce401_03', 2)	# 52-53
    sprite('ce401_04', 2)	# 54-55
    sprite('ce401_05', 1)	# 56-56
    physicsXImpulse(15000)
    physicsYImpulse(14000)
    setGravity(1400)
    loopRest()
    gotoLabel(3)
    label(3)
    sprite('ce401_05', 1)	# 57-57
    sprite('ce401_06', 1)	# 58-58
    Unknown1051(70)
    sprite('ce401_08', 1)	# 59-59	 **attackbox here**
    Unknown23054('63653430315f303700000000000000000000000000000000000000000000000001000000')
    SFX_3('slash_blade_fast')
    GFX_0('Hyper_Counter_kick', 100)
    AttackLevel_(4)
    Hitstop(8)
    AirPushbackX(12000)
    AirPushbackY(20000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    HitLow(0)
    RefreshMultihit()
    sendToLabelUpon(2, 5)

    def upon_LANDING():
        pass
    sprite('ce401_09', 2)	# 60-61
    tag_voice(0, 'pce206_0', 'pce206_0', 'pce206_2', 'pce206_2')
    sprite('ce401_10', 2)	# 62-63
    Unknown1015(1000)
    physicsYImpulse(14000)
    sprite('ce401_11', 2)	# 64-65
    sprite('ce401_13', 2)	# 66-67	 **attackbox here**
    Unknown23054('63653430315f313200000000000000000000000000000000000000000000000002000000')
    GFX_0('Hyper_Counter_kick_oku', 100)
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    sprite('ce401_14', 3)	# 68-70
    sprite('ce401_15', 3)	# 71-73
    Unknown1015(1000)
    physicsYImpulse(14000)
    sprite('ce401_08', 2)	# 74-75	 **attackbox here**
    Unknown23054('63653430315f303700000000000000000000000000000000000000000000000002000000')
    GFX_0('Hyper_Counter_kick', 100)
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ce401_09', 2)	# 76-77
    sprite('ce401_10', 2)	# 78-79
    Unknown1015(1000)
    physicsYImpulse(14000)
    setGravity(2000)
    sprite('ce401_11', 2)	# 80-81
    sprite('ce401_13', 2)	# 82-83	 **attackbox here**
    Unknown23054('63653430315f313200000000000000000000000000000000000000000000000002000000')
    GFX_0('Hyper_Counter_kick_oku', 100)
    RefreshMultihit()
    AirPushbackX(24000)
    AirPushbackY(26000)
    AirUntechableTime(50)
    SFX_3('hit_l_fast')
    YImpluseBeforeWallbounce(3000)
    sprite('ce401_14', 2)	# 84-85
    setInvincible(0)
    Recovery()
    sprite('ce401_16', 3)	# 86-88
    sprite('ce020_04', 3)	# 89-91
    sprite('ce020_05', 3)	# 92-94
    sprite('ce020_06', 3)	# 95-97
    label(4)
    sprite('ce020_07', 4)	# 98-101
    sprite('ce020_08', 4)	# 102-105
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('ce010_00', 2)	# 106-107
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown18009(1)
    sprite('ce010_01', 2)	# 108-109
    sprite('ce010_02', 4)	# 110-113

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown11058('0100000000000000000000000000000000000000')
        AttackLevel_(4)
        Damage(1100)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(12000)
        AirPushbackY(26000)
        Hitstop(8)
        AirUntechableTime(25)
        callSubroutine('ChargeDamageUp')
        clearUponHandler(2)

        def upon_LANDING():
            sendToLabel(5)
    sprite('ce401_05', 1)	# 1-1
    Unknown7007('7063653330325f310000000000000000640000007063653330355f300000000000000000640000007063653330355f310000000000000000640000000000000000000000000000000000000000000000')
    Unknown1084(0)
    physicsXImpulse(15000)
    physicsYImpulse(14000)
    setGravity(1400)
    Unknown11058('0100000000000000000000000000000000000000')
    GuardPoint_(0)
    loopRest()
    sprite('ce401_05', 2)	# 2-3
    sprite('ce401_06', 1)	# 4-4
    sprite('ce401_06', 1)	# 5-5
    Unknown1051(70)
    sprite('ce401_08', 2)	# 6-7	 **attackbox here**
    Unknown23054('63653430315f303700000000000000000000000000000000000000000000000002000000')
    SFX_3('slash_blade_fast')
    GFX_0('Hyper_Counter_kick', 100)
    sprite('ce401_09', 2)	# 8-9
    setInvincible(0)
    sprite('ce401_10', 2)	# 10-11
    Unknown1015(1000)
    physicsYImpulse(14000)
    sprite('ce401_11', 2)	# 12-13
    sprite('ce401_13', 2)	# 14-15	 **attackbox here**
    Unknown23054('63653430315f313200000000000000000000000000000000000000000000000002000000')
    GFX_0('Hyper_Counter_kick_oku', 100)
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    sprite('ce401_14', 3)	# 16-18
    sprite('ce401_15', 3)	# 19-21
    Unknown1015(1000)
    physicsYImpulse(14000)
    sprite('ce401_08', 2)	# 22-23	 **attackbox here**
    Unknown23054('63653430315f303700000000000000000000000000000000000000000000000002000000')
    GFX_0('Hyper_Counter_kick', 100)
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ce401_09', 2)	# 24-25
    sprite('ce401_10', 2)	# 26-27
    Unknown1015(1000)
    physicsYImpulse(14000)
    setGravity(2000)
    sprite('ce401_11', 2)	# 28-29
    sprite('ce401_13', 2)	# 30-31	 **attackbox here**
    Unknown23054('63653430315f313200000000000000000000000000000000000000000000000002000000')
    GFX_0('Hyper_Counter_kick_oku', 100)
    RefreshMultihit()
    AirPushbackX(18000)
    AirPushbackY(26000)
    SFX_3('hit_l_fast')
    sprite('ce401_14', 2)	# 32-33
    sprite('ce401_16', 3)	# 34-36
    sprite('ce020_04', 3)	# 37-39
    sprite('ce020_05', 3)	# 40-42
    sprite('ce020_06', 3)	# 43-45
    label(4)
    sprite('ce020_07', 4)	# 46-49
    sprite('ce020_08', 4)	# 50-53
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('ce010_00', 2)	# 54-55
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown18009(1)
    sprite('ce010_01', 2)	# 56-57
    sprite('ce010_02', 4)	# 58-61

@State
def AbaremakuriLandA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(4)
        AirPushbackY(11000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown1045(0)
        sendToLabelUpon(2, 2)
        Unknown2004(1, 0)
        callSubroutine('ChargeDamageUp')

        def upon_3():
            if SLOT_52:
                if CheckInput(0x37):
                    Unknown1015(-3000)
                    SLOT_52 = 0
                if CheckInput(0x51):
                    Unknown1015(8000)
                    SLOT_52 = 0
                if CheckInput(0x5e):
                    Unknown1015(-3000)
                    SLOT_52 = 0
                if CheckInput(0x78):
                    Unknown1015(8000)
                    SLOT_52 = 0
                if CheckInput(0x85):
                    Unknown1015(-3000)
                    SLOT_52 = 0
                if CheckInput(0x9f):
                    Unknown1015(8000)
                    SLOT_52 = 0
            if SLOT_51:
                if CheckInput(0x37):
                    Unknown1015(-3000)
                    Unknown1021(-4000)
                    SLOT_51 = 0
                if CheckInput(0x44):
                    Unknown1021(-6000)
                    SLOT_51 = 0
                if CheckInput(0x51):
                    Unknown1015(3000)
                    Unknown1021(-4000)
                    SLOT_51 = 0
                if CheckInput(0x5e):
                    Unknown1015(-3000)
                    SLOT_51 = 0
                if CheckInput(0x78):
                    Unknown1015(3000)
                    SLOT_51 = 0
                if CheckInput(0x85):
                    Unknown1015(-3000)
                    Unknown1021(5000)
                    SLOT_51 = 0
                if CheckInput(0x92):
                    Unknown1021(6000)
                    SLOT_51 = 0
                if CheckInput(0x9f):
                    Unknown1015(3000)
                    Unknown1021(5000)
                    SLOT_51 = 0

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce402_00', 1)	# 1-1
    sprite('ce402_01', 1)	# 2-2
    sprite('ce402_02', 1)	# 3-3
    sprite('ce402_03', 1)	# 4-4
    sprite('ce402_04', 1)	# 5-5
    sprite('ce402_05', 2)	# 6-7
    sprite('ce402_06', 2)	# 8-9
    SFX_3('hit_l_fast')
    sprite('ce402_07', 1)	# 10-10
    sprite('ce402_09', 2)	# 11-12	 **attackbox here**
    Unknown23054('63653430325f303800000000000000000000000000000000000000000000000002000000')
    Unknown1047(28000)
    physicsYImpulse(12000)
    setGravity(1250)
    SLOT_52 = 1
    RefreshMultihit()
    Unknown7007('7063653230375f310000000000000000640000007063653230375f320000000000000000640000007063653230385f310000000000000000640000000000000000000000000000000000000000000000')
    loopRest()
    label(1)
    sprite('ce402_09', 3)	# 13-15	 **attackbox here**
    Unknown23027()
    sprite('ce402_10', 3)	# 16-18
    SFX_3('hit_l_fast')
    callSubroutine('Abaremakuri_DeriveInput')
    sprite('ce402_12', 3)	# 19-21	 **attackbox here**
    Unknown23054('63653430325f313100000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    sprite('ce402_12', 3)	# 22-24	 **attackbox here**
    Unknown23027()
    sprite('ce402_13', 3)	# 25-27
    SFX_3('hit_l_fast')
    sprite('ce402_09', 3)	# 28-30	 **attackbox here**
    Unknown23054('63653430325f303800000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    SLOT_51 = 0
    SLOT_52 = 0
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ce402_14', 4)	# 31-34
    physicsXImpulse(0)
    Unknown1051(70)
    callSubroutine('Noutenotoshi_DeriveInput')
    sprite('ce402_15', 4)	# 35-38
    callSubroutine('Abaremakuri_DeriveTiming')
    callSubroutine('Noutenotoshi_DeriveTiming')
    sprite('ce402_16', 3)	# 39-41
    sprite('ce402_17', 3)	# 42-44
    callSubroutine('Abaremakuri_DeriveClear')
    callSubroutine('Noutenotoshi_DeriveClear')
    Unknown2001()
    Recovery()
    Unknown2063()
    sprite('ce402_18', 3)	# 45-47

@State
def DragonKickLandB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Unknown11056(2)
        Unknown23001(0, 0)
        Unknown23014()
        Unknown11058('0100000000000000000000000000000000000000')
        Damage(3000)
        AirUntechableTime(60)
        Hitstop(9)
        AirPushbackX(3000)
        AirPushbackY(50000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown30056('000000001400000000000000')
        callSubroutine('ChargeDamageUp')
        callSubroutine('DoNotBeginCancel')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce032_00', 2)	# 1-2
    Unknown1084(1)
    Unknown1047(12000)
    sprite('ce404_00', 1)	# 3-3
    sprite('ce404_00', 2)	# 4-5
    Unknown23029(11, 401, 0)
    sprite('ce404_01', 3)	# 6-8
    sprite('ce404_02', 3)	# 9-11
    sprite('ce404_03', 3)	# 12-14
    sprite('ce404_04', 1)	# 15-15
    Unknown8007(100, 0, 1)
    SFX_3('slash_blade_middle')
    physicsXImpulse(25000)
    physicsYImpulse(13000)
    setGravity(1000)
    sprite('ce404_04', 1)	# 16-16
    Unknown1019(200)
    YAccel(200)
    SFX_3('slash_blade_fast')
    sprite('ce404_05', 1)	# 17-17
    Unknown1019(95)
    loopRest()
    label(1)
    sprite('ce404_06', 3)	# 18-20	 **attackbox here**
    GFX_0('DragonKick', 0)
    GFX_0('DragonKick_Launcher', 0)
    Unknown1019(95)
    Unknown2017(0)
    RefreshMultihit()
    Unknown7007('7063653231315f300000000000000000640000007063653231315f310000000000000000640000007063653231315f320000000000000000640000007063653231325f32000000000000000064000000')
    loopRest()
    sprite('ce404_07', 3)	# 21-23	 **attackbox here**
    Unknown1019(95)
    sprite('ce404_06', 3)	# 24-26	 **attackbox here**
    Unknown1019(95)
    sprite('ce404_07', 3)	# 27-29	 **attackbox here**
    Unknown1019(95)
    loopRest()
    sprite('ce404_08', 3)	# 30-32
    sendToLabelUpon(2, 2)
    Unknown2017(1)
    setGravity(1800)
    Unknown1019(80)
    sprite('ce404_09', 3)	# 33-35
    Unknown1019(80)
    sprite('ce404_10', 3)	# 36-38
    Unknown1019(80)
    sprite('ce404_11', 3)	# 39-41
    Unknown1019(80)
    sprite('ce020_04', 3)	# 42-44
    Unknown1019(80)
    sprite('ce020_05', 3)	# 45-47
    Unknown1019(80)
    sprite('ce020_06', 3)	# 48-50
    loopRest()
    label(4)
    sprite('ce020_07', 4)	# 51-54
    sprite('ce020_08', 4)	# 55-58
    loopRest()
    gotoLabel(4)
    label(2)
    sprite('ce010_00', 2)	# 59-60
    Unknown8000(100, 1, 1)
    Unknown2001()
    Unknown1084(1)
    Unknown18009(1)
    sprite('ce010_01', 2)	# 61-62
    sprite('ce010_02', 11)	# 63-73

@State
def DragonKickLandEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(4500)
        Unknown11056(2)
        Unknown11058('0100000000000000000000000000000000000000')
        AirUntechableTime(80)
        AirPushbackX(3000)
        AirPushbackY(50000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown30065(0)
        Unknown11091(10)

        def upon_78():
            pass
        Unknown30056('000000001400000000000000')
        callSubroutine('ChargeDamageUp')
        callSubroutine('DoNotBeginCancel')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        Unknown23001(0, 0)
        Unknown23014()
    sprite('ce032_00', 2)	# 1-2
    Unknown8006(100, 1, 1)
    Unknown1084(1)
    Unknown1047(32000)
    sprite('ce032_01', 1)	# 3-3
    sprite('ce032_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ce032_02', 2)	# 5-6
    sprite('ce032_03', 2)	# 7-8
    sprite('ce032_04', 1)	# 9-9
    Unknown7007('7063653231325f300000000000000000640000007063653231325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ce404_00', 3)	# 10-12
    sprite('ce404_01', 2)	# 13-14
    sprite('ce404_01', 1)	# 15-15
    Unknown23029(11, 403, 0)
    sprite('ce404_02', 5)	# 16-20
    sprite('ce404_03', 3)	# 21-23
    sprite('ce404_04', 1)	# 24-24
    Unknown8007(100, 1, 1)
    physicsXImpulse(25000)
    physicsYImpulse(13000)
    setGravity(1000)
    SFX_3('slash_blade_middle')
    sprite('ce404_04', 2)	# 25-26
    Unknown1019(200)
    YAccel(200)
    SFX_3('slash_blade_fast')
    loopRest()
    sprite('ce404_05', 3)	# 27-29
    Unknown1019(96)
    sprite('ce404_06', 3)	# 30-32	 **attackbox here**
    Unknown1019(96)
    Unknown2017(0)
    RefreshMultihit()
    GFX_0('DragonKick', 0)
    GFX_0('DragonKick_Launcher', 0)
    loopRest()
    sprite('ce404_07', 3)	# 33-35	 **attackbox here**
    Unknown1019(96)
    sprite('ce404_06', 3)	# 36-38	 **attackbox here**
    Unknown1019(96)
    sprite('ce404_07', 3)	# 39-41	 **attackbox here**
    Unknown1019(96)
    loopRest()
    sprite('ce404_08', 3)	# 42-44
    sendToLabelUpon(2, 2)
    Unknown2017(1)
    setGravity(1800)
    Unknown1019(80)
    sprite('ce404_09', 3)	# 45-47
    Unknown1019(80)
    sprite('ce404_10', 3)	# 48-50
    Unknown1019(80)
    sprite('ce404_11', 3)	# 51-53
    Unknown1019(80)
    sprite('ce020_04', 3)	# 54-56
    Unknown1019(80)
    sprite('ce020_05', 3)	# 57-59
    Unknown1019(80)
    sprite('ce020_06', 3)	# 60-62
    loopRest()
    label(4)
    sprite('ce020_07', 4)	# 63-66
    sprite('ce020_08', 4)	# 67-70
    loopRest()
    gotoLabel(4)
    label(2)
    sprite('ce010_00', 3)	# 71-73
    Unknown8000(100, 1, 1)
    Unknown2001()
    Unknown1084(1)
    Unknown18009(1)
    sprite('ce010_01', 4)	# 74-77
    sprite('ce010_02', 7)	# 78-84

@State
def __100inchPunchA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(90)
        AirPushbackX(30000)
        AirPushbackY(18000)
        PushbackX(55000)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirUntechableTime(31)
        Unknown11028(19)
        Unknown11056(2)
        sendToLabelUpon(2, 0)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
            SFX_3('down_steal_m')
            Unknown1019(60)
            Unknown1039(120)
            ScreenShake(4000, 1000)

        def upon_12():
            Unknown2037(1)
            SLOT_51 = 1
            SFX_3('counter_hit_l01')
            ScreenShake(1000, 4000)
        callSubroutine('ChargeDamageUp')
        callSubroutine('DoNotBeginCancel')
    sprite('ce406_00', 1)	# 1-1
    Unknown1084(1)
    sprite('ce406_01', 2)	# 2-3
    sprite('ce406_02', 2)	# 4-5
    sprite('ce406_04', 2)	# 6-7
    SFX_3('runjump_stone_heavy')
    SFX_3('hit_m_slow')
    Unknown8007(100, 1, 1)
    ScreenShake(0, 6000)
    sprite('ce406_05', 1)	# 8-8
    physicsXImpulse(10000)
    sprite('ce406_06', 2)	# 9-10
    SFX_3('slash_blade_fast')
    SFX_3('airdash_l')
    Unknown1019(300)
    Unknown7007('7063653231355f300000000000000000640000007063653231365f320000000000000000640000007063653231365f300000000000000000640000007063653231365f31000000000000000064000000')
    sprite('ce406_07', 2)	# 11-12	 **attackbox here**
    GFX_0('100InchPanch_hand', 0)
    GFX_0('100InchPanch_add', 0)
    GFX_0('100InchPanch_dash', 104)
    Unknown8007(100, 0, 1)
    Unknown1019(200)
    physicsYImpulse(4000)
    setGravity(2400)
    RefreshMultihit()
    sprite('ce406_08', 2)	# 13-14	 **attackbox here**
    Unknown26('100InchPanch_add')
    label(1)
    sprite('ce406_07', 2)	# 15-16	 **attackbox here**
    Unknown8007(100, 0, 1)
    sprite('ce406_08', 2)	# 17-18	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 1)	# 19-19
    Unknown26('100InchPanch_hand')
    Unknown1019(60)
    if (not SLOT_2):
        pass
    sprite('ce406_09', 5)	# 20-24
    SFX_3('brake_normal_light')
    Unknown8000(100, 0, 1)
    Unknown8006(100, 1, 1)
    Unknown1019(50)
    if SLOT_51:
        pass
    sprite('ce406_10', 5)	# 25-29
    Unknown1019(50)
    sprite('ce406_11', 4)	# 30-33
    Unknown1084(1)
    sprite('ce406_12', 4)	# 34-37
    sprite('ce406_13', 4)	# 38-41

@State
def __100inchPunchB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP1(80)
        AirUntechableTime(45)
        Unknown11028(23)
        AirPushbackX(93500)
        AirPushbackY(12000)
        PushbackX(60000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirHitstunAfterWallbounce(30)
        WallbounceReboundTime(0)
        Unknown9362(1)
        Unknown9364(20)
        Unknown9215()
        Unknown11056(2)
        sendToLabelUpon(2, 0)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
            SFX_3('down_steal_m')
            Unknown1019(60)
            Unknown1039(120)
            ScreenShake(8000, 1000)

        def upon_12():
            Unknown2037(1)
            SLOT_51 = 1
            SFX_3('counter_hit_l01')
            ScreenShake(1000, 8000)
        callSubroutine('ChargeDamageUp')
        callSubroutine('DoNotBeginCancel')
    sprite('ce406_00', 2)	# 1-2
    setInvincible(1)
    Unknown22019('0000000000000000000000000000000001000000')
    Unknown1084(1)
    sprite('ce406_01', 2)	# 3-4
    physicsXImpulse(-6000)
    sprite('ce406_01', 2)	# 5-6
    Unknown1019(200)
    sprite('ce406_02', 2)	# 7-8
    Unknown1019(200)
    sprite('ce406_02', 2)	# 9-10
    Unknown1019(200)
    sprite('ce406_03', 2)	# 11-12
    SFX_3('runjump_stone_heavy')
    ScreenShake(0, 6000)
    Unknown1019(50)
    sprite('ce406_03', 2)	# 13-14
    Unknown1019(50)
    sprite('ce406_04', 3)	# 15-17
    Unknown1019(50)
    sprite('ce406_04', 3)	# 18-20
    Unknown1019(50)
    Unknown14070('DragonKickLandB_Hasei')
    Unknown14070('DragonKickLandEX_Hasei')
    sprite('ce406_05', 2)	# 21-22
    Unknown8007(100, 1, 1)
    physicsXImpulse(15000)
    setInvincible(0)
    sprite('ce406_06', 2)	# 23-24
    SFX_3('slash_blade_fast')
    SFX_3('airdash_l')
    Unknown1019(300)
    Unknown7007('7063653231355f300000000000000000640000007063653231365f320000000000000000640000007063653231365f300000000000000000640000007063653231365f31000000000000000064000000')
    sprite('ce406_07', 2)	# 25-26	 **attackbox here**
    GFX_0('100InchPanch_hand', 0)
    GFX_0('100InchPanch_add', 0)
    GFX_0('100InchPanch_dash', 104)
    Unknown1019(200)
    physicsYImpulse(8000)
    setGravity(2400)
    RefreshMultihit()
    sprite('ce406_08', 2)	# 27-28	 **attackbox here**
    Unknown26('100InchPanch_add')
    label(1)
    sprite('ce406_07', 2)	# 29-30	 **attackbox here**
    GFX_0('100InchPanch_dash', 104)
    sprite('ce406_08', 2)	# 31-32	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 1)	# 33-33
    Unknown26('100InchPanch_hand')
    Unknown1019(60)
    if (not SLOT_2):
        pass
    sprite('ce406_09', 4)	# 34-37
    SFX_3('brake_normal_light')
    Unknown8000(100, 0, 1)
    Unknown8006(100, 1, 1)
    Unknown1019(50)
    sprite('ce406_10', 4)	# 38-41
    Unknown1019(50)
    if SLOT_51:
        Unknown14072('DragonKickLandB_Hasei')
        Unknown14072('DragonKickLandEX_Hasei')
    sprite('ce406_11', 3)	# 42-44
    Unknown1019(80)
    sprite('ce406_12', 3)	# 45-47
    Unknown1019(80)
    sprite('ce406_13', 3)	# 48-50
    Unknown1019(80)

@State
def __100inchPunchEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(70)
        AirUntechableTime(45)
        Unknown11028(25)
        AirPushbackX(60000)
        AirPushbackY(25000)
        PushbackX(25000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirHitstunAfterWallbounce(40)
        WallbounceReboundTime(10)
        Unknown30065(0)
        Unknown11091(10)
        Unknown9362(1)
        Unknown9364(35)
        Unknown11001(0, 0, 0)
        Unknown9215()
        Unknown11056(2)
        sendToLabelUpon(2, 0)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
            SFX_3('down_steal_m')
            Unknown1019(60)
            Unknown1039(120)
            ScreenShake(8000, 1000)

        def upon_12():
            Unknown2037(1)
            SLOT_51 = 1
            SFX_3('counter_hit_l01')
            ScreenShake(1000, 8000)
        callSubroutine('ChargeDamageUp')
        callSubroutine('DoNotBeginCancel')
    sprite('ce406_00', 2)	# 1-2
    setInvincible(1)
    Unknown22019('0000000000000000000000000000000001000000')
    Unknown1084(1)
    sprite('ce406_01', 1)	# 3-3
    physicsXImpulse(-6000)
    sprite('ce406_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ce406_01', 2)	# 5-6
    Unknown1019(200)
    sprite('ce406_02', 2)	# 7-8
    Unknown1019(200)
    sprite('ce406_02', 2)	# 9-10
    Unknown1019(200)
    sprite('ce406_03', 2)	# 11-12
    SFX_3('runjump_stone_heavy')
    ScreenShake(0, 6000)
    Unknown1019(50)
    sprite('ce406_03', 2)	# 13-14
    Unknown1019(50)
    sprite('ce406_04', 3)	# 15-17
    Unknown1019(50)
    sprite('ce406_04', 3)	# 18-20
    Unknown1019(50)
    Unknown14070('DragonKickLandB_Hasei')
    Unknown14070('DragonKickLandEX_Hasei')
    sprite('ce406_05', 2)	# 21-22
    Unknown8007(100, 1, 1)
    physicsXImpulse(15000)
    setInvincible(0)
    sprite('ce406_06', 2)	# 23-24
    SFX_3('slash_blade_fast')
    SFX_3('airdash_l')
    Unknown1019(300)
    Unknown7007('7063653231355f300000000000000000640000007063653231365f320000000000000000640000007063653231365f300000000000000000640000007063653231365f31000000000000000064000000')
    sprite('ce406_07', 2)	# 25-26	 **attackbox here**
    GFX_0('100InchPanch_hand', 0)
    GFX_0('100InchPanch_add', 0)
    GFX_0('100InchPanch_dash', 104)
    Unknown1019(200)
    physicsYImpulse(8000)
    setGravity(2400)
    RefreshMultihit()
    sprite('ce406_08', 2)	# 27-28	 **attackbox here**
    Unknown26('100InchPanch_add')
    label(1)
    sprite('ce406_07', 2)	# 29-30	 **attackbox here**
    GFX_0('100InchPanch_dash', 104)
    sprite('ce406_08', 2)	# 31-32	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 1)	# 33-33
    Unknown26('100InchPanch_hand')
    Unknown1019(60)
    if (not SLOT_2):
        RefreshMultihit()
    sprite('ce406_09', 4)	# 34-37
    SFX_3('brake_normal_light')
    Unknown8000(100, 0, 1)
    Unknown8006(100, 1, 1)
    Unknown1019(50)
    sprite('ce406_10', 4)	# 38-41
    Unknown1019(50)
    if SLOT_51:
        Unknown14072('DragonKickLandB_Hasei')
        Unknown14072('DragonKickLandEX_Hasei')
    sprite('ce406_11', 3)	# 42-44
    Unknown1019(80)
    sprite('ce406_12', 3)	# 45-47
    Unknown1019(80)
    sprite('ce406_13', 3)	# 48-50
    Unknown1019(80)

@State
def AbaremakuriAirA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(550)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(4)
        AirPushbackX(15000)
        AirPushbackY(6000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown1045(0)
        sendToLabelUpon(2, 2)
        Unknown2004(1, 0)
        callSubroutine('ChargeDamageUp')
        AirUntechableTime(30)

        def upon_3():
            if SLOT_52:
                if CheckInput(0x37):
                    Unknown1015(-3000)
                    SLOT_52 = 0
                if CheckInput(0x51):
                    Unknown1015(3000)
                    SLOT_52 = 0
                if CheckInput(0x5e):
                    Unknown1015(-3000)
                    SLOT_52 = 0
                if CheckInput(0x78):
                    Unknown1015(3000)
                    SLOT_52 = 0
                if CheckInput(0x85):
                    Unknown1015(-3000)
                    SLOT_52 = 0
                if CheckInput(0x9f):
                    Unknown1015(3000)
                    SLOT_52 = 0
            if SLOT_51:
                if CheckInput(0x37):
                    Unknown1015(-3000)
                    Unknown1021(-4000)
                    SLOT_51 = 0
                if CheckInput(0x44):
                    Unknown1021(-6000)
                    SLOT_51 = 0
                if CheckInput(0x51):
                    Unknown1015(3000)
                    Unknown1021(-4000)
                    SLOT_51 = 0
                if CheckInput(0x5e):
                    Unknown1015(-3000)
                    SLOT_51 = 0
                if CheckInput(0x78):
                    Unknown1015(3000)
                    SLOT_51 = 0
                if CheckInput(0x85):
                    Unknown1015(-3000)
                    Unknown1021(5000)
                    SLOT_51 = 0
                if CheckInput(0x92):
                    Unknown1021(6000)
                    SLOT_51 = 0
                if CheckInput(0x9f):
                    Unknown1015(3000)
                    Unknown1021(5000)
                    SLOT_51 = 0

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce402_06', 3)	# 1-3
    teleportRelativeX(-100000)
    Unknown1007(50000)
    YAccel(30)
    sprite('ce402_07', 2)	# 4-5
    SFX_3('hit_l_fast')
    sprite('ce402_09', 2)	# 6-7	 **attackbox here**
    Unknown23054('63653430325f303800000000000000000000000000000000000000000000000002000000')
    Unknown1045(28000)
    physicsXImpulse(0)
    physicsYImpulse(12000)
    setGravity(1250)
    SLOT_51 = 1
    RefreshMultihit()
    Unknown7007('7063653230375f310000000000000000640000007063653230375f320000000000000000640000007063653230385f310000000000000000640000000000000000000000000000000000000000000000')
    loopRest()
    label(1)
    sprite('ce402_09', 3)	# 8-10	 **attackbox here**
    Unknown23027()
    sprite('ce402_10', 3)	# 11-13
    SFX_3('hit_l_fast')
    callSubroutine('Abaremakuri_DeriveInput')
    sprite('ce402_12', 3)	# 14-16	 **attackbox here**
    Unknown23054('63653430325f313100000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    sprite('ce402_12', 3)	# 17-19	 **attackbox here**
    Unknown23027()
    sprite('ce402_13', 3)	# 20-22
    SFX_3('hit_l_fast')
    sprite('ce402_09', 3)	# 23-25	 **attackbox here**
    Unknown23054('63653430325f303800000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    SLOT_51 = 0
    SLOT_52 = 0
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ce402_14', 4)	# 26-29
    physicsXImpulse(0)
    Unknown1051(70)
    callSubroutine('Noutenotoshi_DeriveInput')
    sprite('ce402_15', 4)	# 30-33
    callSubroutine('Abaremakuri_DeriveTiming')
    callSubroutine('Noutenotoshi_DeriveTiming')
    sprite('ce402_16', 3)	# 34-36
    sprite('ce402_17', 3)	# 37-39
    callSubroutine('Abaremakuri_DeriveClear')
    callSubroutine('Noutenotoshi_DeriveClear')
    Unknown2001()
    Recovery()
    Unknown2063()
    sprite('ce402_18', 3)	# 40-42

@State
def DragonKickAirB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Unknown11056(2)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown23014()
        Damage(3000)
        AirUntechableTime(60)
        Hitstop(9)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(50000)
        Unknown30056('000000001400000000000000')
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    label(0)
    sprite('ce404_02ex', 3)	# 1-3
    Unknown1084(1)
    sprite('ce404_02ex', 2)	# 4-5
    Unknown23029(11, 404, 0)
    sprite('ce404_03ex', 5)	# 6-10
    sprite('ce404_04ex', 1)	# 11-11
    SFX_3('slash_blade_middle')
    physicsXImpulse(25000)
    physicsYImpulse(13000)
    sprite('ce404_04ex', 1)	# 12-12
    SFX_3('slash_blade_fast')
    Unknown1019(200)
    YAccel(200)
    setGravity(1000)
    sprite('ce404_05', 1)	# 13-13
    Unknown1019(95)
    loopRest()
    label(1)
    sprite('ce404_06', 3)	# 14-16	 **attackbox here**
    GFX_0('DragonKick', 0)
    GFX_0('DragonKick_Launcher', 0)
    Unknown1019(95)
    Unknown2017(0)
    RefreshMultihit()
    Unknown7007('7063653231315f300000000000000000640000007063653231315f310000000000000000640000007063653231315f320000000000000000640000007063653231325f32000000000000000064000000')
    loopRest()
    sprite('ce404_07', 3)	# 17-19	 **attackbox here**
    Unknown1019(95)
    sprite('ce404_06', 3)	# 20-22	 **attackbox here**
    Unknown1019(95)
    sprite('ce404_07', 3)	# 23-25	 **attackbox here**
    Unknown1019(95)
    loopRest()
    sprite('ce404_08', 3)	# 26-28
    sendToLabelUpon(2, 2)
    Unknown2017(1)
    setGravity(1800)
    Unknown1019(80)
    sprite('ce404_09', 3)	# 29-31
    Unknown1019(80)
    sprite('ce404_10', 3)	# 32-34
    Unknown1019(80)
    sprite('ce404_11', 3)	# 35-37
    Unknown1019(80)
    sprite('ce020_04', 3)	# 38-40
    Unknown1019(80)
    sprite('ce020_05', 3)	# 41-43
    Unknown1019(80)
    sprite('ce020_06', 3)	# 44-46
    loopRest()
    label(4)
    sprite('ce020_07', 4)	# 47-50
    sprite('ce020_08', 4)	# 51-54
    loopRest()
    gotoLabel(4)
    label(2)
    sprite('ce010_00', 2)	# 55-56
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown2001()
    Unknown18009(1)
    sprite('ce010_01', 2)	# 57-58
    sprite('ce010_02', 11)	# 59-69

@State
def DragonKickAirEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(4500)
        Unknown11056(2)
        Unknown11058('0100000000000000000000000000000000000000')
        AirUntechableTime(80)
        AirPushbackX(3000)
        AirPushbackY(50000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown30065(0)
        Unknown11091(10)

        def upon_78():
            Hitstop(20)
        Unknown30056('000000001400000000000000')
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        Unknown23001(0, 0)
        Unknown23014()
    sprite('ce404_02ex', 3)	# 1-3
    Unknown1084(1)
    sprite('ce404_03ex', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    Unknown23029(11, 406, 0)
    sprite('ce404_04ex', 1)	# 7-7
    physicsXImpulse(25000)
    physicsYImpulse(13000)
    SFX_3('slash_blade_middle')
    sprite('ce404_04ex', 2)	# 8-9
    Unknown1019(200)
    YAccel(200)
    setGravity(1000)
    SFX_3('slash_blade_fast')
    loopRest()
    sprite('ce404_05', 3)	# 10-12
    Unknown1019(96)
    sprite('ce404_06', 3)	# 13-15	 **attackbox here**
    Unknown1019(96)
    Unknown2017(0)
    RefreshMultihit()
    GFX_0('DragonKick', 0)
    GFX_0('DragonKick_Launcher', 0)
    Unknown7007('7063653231315f300000000000000000640000007063653231315f310000000000000000640000007063653231315f320000000000000000640000007063653231325f32000000000000000064000000')
    loopRest()
    sprite('ce404_07', 3)	# 16-18	 **attackbox here**
    Unknown1019(96)
    sprite('ce404_06', 3)	# 19-21	 **attackbox here**
    Unknown1019(96)
    sprite('ce404_07', 3)	# 22-24	 **attackbox here**
    Unknown1019(96)
    loopRest()
    sprite('ce404_08', 3)	# 25-27
    sendToLabelUpon(2, 2)
    Unknown2017(1)
    setGravity(1800)
    Unknown1019(80)
    sprite('ce404_09', 3)	# 28-30
    Unknown1019(80)
    sprite('ce404_10', 3)	# 31-33
    Unknown1019(80)
    sprite('ce404_11', 3)	# 34-36
    Unknown1019(80)
    sprite('ce020_04', 3)	# 37-39
    Unknown1019(80)
    sprite('ce020_05', 3)	# 40-42
    Unknown1019(80)
    sprite('ce020_06', 3)	# 43-45
    loopRest()
    label(4)
    sprite('ce020_07', 4)	# 46-49
    sprite('ce020_08', 4)	# 50-53
    loopRest()
    gotoLabel(4)
    label(2)
    sprite('ce010_00', 3)	# 54-56
    Unknown8000(100, 1, 1)
    Unknown2001()
    Unknown1084(1)
    Unknown18009(1)
    sprite('ce010_01', 4)	# 57-60
    sprite('ce010_02', 7)	# 61-67

@State
def NoutenotoshiA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(20000)
        AirPushbackY(-24000)
        Unknown9310(20)
        callSubroutine('ChargeDamageUp')
        HitOverhead(2)
        Unknown2004(1, 0)
        JumpCancel_(0)
        callSubroutine('DoNotBeginCancel')
        Unknown11056(2)
        Unknown11001(0, -4, 1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce403_00', 1)	# 1-1
    GFX_0('ceef_403_kick', 103)
    sprite('ce403_01', 2)	# 2-3
    sprite('ce403_02', 2)	# 4-5
    SFX_3('hit_l_slow')
    sprite('ce403_03', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    Unknown7007('7063653230395f300000000000000000640000007063653230395f310000000000000000640000007063653231305f300000000000000000640000007063653231305f32000000000000000064000000')
    sprite('ce403_03', 1)	# 7-7	 **attackbox here**
    sprite('ce403_04', 3)	# 8-10
    sprite('ce403_05', 3)	# 11-13
    GFX_0('Nouten_stump', 100)
    sprite('ce403_06', 3)	# 14-16
    Unknown14070('100inchPunchA')
    Unknown14070('100inchPunchB')
    Unknown14070('100inchPunchEX')
    Unknown14070('DragonKickLand_NoutenHasei')
    Unknown14070('DragonKickLand_NoutenHaseiB')
    Unknown14070('DragonKickLand_NoutenHaseiC')
    sprite('ce403_07', 3)	# 17-19	 **attackbox here**
    GFX_0('Nouten_stump_hit', 100)
    GFX_1('ceef_noutenotoshi_02', 0)
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown11058('0000000000000000010000000000000000000000')
    ScreenShake(0, 3000)
    AirPushbackX(14000)
    AirPushbackY(32000)
    YImpluseBeforeWallbounce(2500)
    PushbackX(15000)
    AirUntechableTime(36)
    Unknown9310(0)
    HitOverhead(0)
    SFX_3('bound_marble_m')
    Unknown11001(0, 0, 5)
    sprite('ce403_08', 4)	# 20-23
    sprite('ce403_09', 5)	# 24-28
    Unknown14072('100inchPunchA')
    Unknown14072('100inchPunchB')
    Unknown14072('100inchPunchEX')
    Unknown14072('DragonKickLand_NoutenHasei')
    Unknown14072('DragonKickLand_NoutenHaseiB')
    Unknown14072('DragonKickLand_NoutenHaseiC')
    sprite('ce403_09', 5)	# 29-33
    Unknown14074('100inchPunchA')
    Unknown14074('100inchPunchB')
    Unknown14074('100inchPunchEX')
    Unknown14074('DragonKickLand_NoutenHasei')
    Unknown14074('DragonKickLand_NoutenHaseiB')
    Unknown14074('DragonKickLand_NoutenHaseiC')
    sprite('ce403_10', 3)	# 34-36
    sprite('ce403_11', 3)	# 37-39

@State
def DragonKickLand_NoutenHasei():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Unknown11056(2)
        Unknown23001(0, 0)
        Unknown23014()
        Unknown11058('0100000000000000000000000000000000000000')
        Damage(3000)
        AirUntechableTime(60)
        Hitstop(9)
        AirPushbackX(3000)
        AirPushbackY(50000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        callSubroutine('ChargeDamageUp')
        callSubroutine('DoNotBeginCancel')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
    sprite('ce032_00', 2)	# 1-2
    Unknown1084(1)
    Unknown1047(12000)
    sprite('ce404_00', 1)	# 3-3
    sprite('ce404_00', 2)	# 4-5
    Unknown23029(11, 401, 0)
    sprite('ce404_01', 3)	# 6-8
    sprite('ce404_02', 3)	# 9-11
    sprite('ce404_03', 3)	# 12-14
    sprite('ce404_04', 1)	# 15-15
    Unknown8007(100, 0, 1)
    SFX_3('slash_blade_middle')
    physicsXImpulse(25000)
    physicsYImpulse(13000)
    setGravity(1000)
    sprite('ce404_04', 1)	# 16-16
    Unknown1019(200)
    YAccel(200)
    SFX_3('slash_blade_fast')
    sprite('ce404_05', 1)	# 17-17
    Unknown1019(95)
    loopRest()
    label(1)
    sprite('ce404_06', 3)	# 18-20	 **attackbox here**
    GFX_0('DragonKick', 0)
    GFX_0('DragonKick_Launcher', 0)
    Unknown1019(95)
    Unknown2017(0)
    RefreshMultihit()
    Unknown7007('7063653231315f300000000000000000640000007063653231315f310000000000000000640000007063653231315f320000000000000000640000007063653231325f32000000000000000064000000')
    loopRest()
    sprite('ce404_07', 3)	# 21-23	 **attackbox here**
    Unknown1019(95)
    sprite('ce404_06', 3)	# 24-26	 **attackbox here**
    Unknown1019(95)
    sprite('ce404_07', 3)	# 27-29	 **attackbox here**
    Unknown1019(95)
    loopRest()
    sprite('ce404_08', 3)	# 30-32
    sendToLabelUpon(2, 2)
    Unknown2017(1)
    setGravity(1800)
    Unknown1019(80)
    sprite('ce404_09', 3)	# 33-35
    Unknown1019(80)
    sprite('ce404_10', 3)	# 36-38
    Unknown1019(80)
    sprite('ce404_11', 3)	# 39-41
    Unknown1019(80)
    sprite('ce020_04', 3)	# 42-44
    Unknown1019(80)
    sprite('ce020_05', 3)	# 45-47
    Unknown1019(80)
    sprite('ce020_06', 3)	# 48-50
    loopRest()
    label(4)
    sprite('ce020_07', 4)	# 51-54
    sprite('ce020_08', 4)	# 55-58
    loopRest()
    gotoLabel(4)
    label(2)
    sprite('ce010_00', 2)	# 59-60
    Unknown8000(100, 1, 1)
    Unknown2001()
    Unknown1084(1)
    Unknown18009(1)
    sprite('ce010_01', 2)	# 61-62
    sprite('ce010_02', 11)	# 63-73

@State
def DashCancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        physicsXImpulse(8000)
    sprite('ce032_00', 2)	# 1-2
    sprite('ce032_01', 4)	# 3-6
    physicsXImpulse(20440)
    Unknown1045(40880)

    def upon_3():
        Unknown1015(440)
        Unknown1047(440)
    sprite('ce032_02', 4)	# 7-10
    Unknown8006(100, 1, 1)
    sprite('ce032_03', 4)	# 11-14
    sprite('ce032_09', 3)	# 15-17
    physicsXImpulse(0)
    clearUponHandler(3)
    Unknown8010(100, 1, 1)
    sprite('ce032_10', 3)	# 18-20

@State
def UltimateGodHand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)

        def upon_STATE_END():
            if SLOT_31:
                SLOT_31 = 0
    sprite('ce430_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('ce430_01', 3)	# 4-6
    tag_voice(1, 'pce252_0', 'pce252_1', '', '')
    Unknown30080('')
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown23029(11, 501, 0)
    sprite('ce430_02', 3)	# 7-9
    sprite('ce430_03', 3)	# 10-12
    sprite('ce430_04', 3)	# 13-15
    sprite('ce430_05', 3)	# 16-18
    sprite('ce430_06', 3)	# 19-21
    sprite('ce430_07', 3)	# 22-24
    sprite('ce430_08', 3)	# 25-27
    sprite('ce430_09', 3)	# 28-30
    sprite('ce430_10', 3)	# 31-33
    sprite('ce430_11', 3)	# 34-36
    sprite('ce430_09', 3)	# 37-39
    sprite('ce430_10', 3)	# 40-42
    sprite('ce430_11', 3)	# 43-45
    sprite('ce430_09', 3)	# 46-48
    sprite('ce430_10', 3)	# 49-51
    sprite('ce430_11', 3)	# 52-54
    sprite('ce430_12', 3)	# 55-57
    sprite('ce430_13', 3)	# 58-60
    sprite('ce430_14', 3)	# 61-63
    sprite('ce430_15', 3)	# 64-66
    sprite('ce430_16', 3)	# 67-69
    sprite('ce430_17', 3)	# 70-72
    tag_voice(0, 'pce253_0', 'pce253_1', '', '')
    sprite('ce430_15', 3)	# 73-75
    setInvincible(0)
    if SLOT_85:
        _gotolabel(10)
    sprite('ce430_16', 3)	# 76-78
    sprite('ce430_17', 3)	# 79-81
    sprite('ce430_15', 3)	# 82-84
    sprite('ce430_16', 3)	# 85-87
    sprite('ce430_17', 3)	# 88-90
    sprite('ce430_15', 3)	# 91-93
    sprite('ce430_16', 3)	# 94-96
    sprite('ce430_17', 3)	# 97-99
    sprite('ce430_15', 3)	# 100-102
    sprite('ce430_16', 3)	# 103-105
    sprite('ce430_17', 3)	# 106-108
    sprite('ce430_15', 3)	# 109-111
    sprite('ce430_16', 3)	# 112-114
    sprite('ce430_17', 3)	# 115-117
    sprite('ce430_15', 3)	# 118-120
    sprite('ce430_16', 3)	# 121-123
    sprite('ce430_17', 3)	# 124-126
    label(10)
    sprite('ce430_15', 3)	# 127-129
    sprite('ce430_16', 3)	# 130-132
    sprite('ce430_17', 3)	# 133-135
    sprite('ce430_18', 3)	# 136-138

@State
def UltimateGodHandOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)

        def upon_STATE_END():
            if SLOT_31:
                SLOT_31 = 0
    sprite('ce430_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('ce430_01', 3)	# 4-6
    tag_voice(1, 'pce252_0', 'pce252_1', '', '')
    Unknown30080('')
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown23029(11, 502, 0)
    sprite('ce430_02', 3)	# 7-9
    sprite('ce430_03', 3)	# 10-12
    sprite('ce430_04', 3)	# 13-15
    sprite('ce430_05', 3)	# 16-18
    sprite('ce430_06', 3)	# 19-21
    sprite('ce430_07', 3)	# 22-24
    sprite('ce430_08', 3)	# 25-27
    sprite('ce430_09', 3)	# 28-30
    sprite('ce430_10', 3)	# 31-33
    sprite('ce430_11', 3)	# 34-36
    sprite('ce430_09', 3)	# 37-39
    sprite('ce430_10', 3)	# 40-42
    sprite('ce430_11', 3)	# 43-45
    sprite('ce430_09', 3)	# 46-48
    sprite('ce430_10', 3)	# 49-51
    sprite('ce430_11', 3)	# 52-54
    sprite('ce430_12', 3)	# 55-57
    sprite('ce430_13', 3)	# 58-60
    sprite('ce430_14', 3)	# 61-63
    sprite('ce430_15', 3)	# 64-66
    sprite('ce430_16', 3)	# 67-69
    sprite('ce430_17', 3)	# 70-72
    SFX_1('ce311')
    tag_voice(0, 'pce253_0', 'pce253_1', '', '')
    sprite('ce430_15', 3)	# 73-75
    setInvincible(0)
    sprite('ce430_16', 3)	# 76-78
    sprite('ce430_17', 3)	# 79-81
    sprite('ce430_15', 3)	# 82-84
    sprite('ce430_16', 3)	# 85-87
    sprite('ce430_17', 3)	# 88-90
    sprite('ce430_15', 3)	# 91-93
    sprite('ce430_16', 3)	# 94-96
    sprite('ce430_17', 3)	# 97-99
    sprite('ce430_15', 3)	# 100-102
    sprite('ce430_16', 3)	# 103-105
    sprite('ce430_17', 3)	# 106-108
    sprite('ce430_15', 3)	# 109-111
    sprite('ce430_16', 3)	# 112-114
    sprite('ce430_17', 3)	# 115-117
    sprite('ce430_15', 3)	# 118-120
    sprite('ce430_16', 3)	# 121-123
    sprite('ce430_17', 3)	# 124-126
    sprite('ce430_15', 3)	# 127-129
    sprite('ce430_16', 3)	# 130-132
    sprite('ce430_17', 3)	# 133-135
    sprite('ce430_15', 3)	# 136-138
    sprite('ce430_16', 3)	# 139-141
    sprite('ce430_17', 3)	# 142-144
    sprite('ce430_15', 3)	# 145-147
    sprite('ce430_16', 3)	# 148-150
    sprite('ce430_17', 3)	# 151-153
    sprite('ce430_15', 3)	# 154-156
    sprite('ce430_16', 3)	# 157-159
    sprite('ce430_17', 3)	# 160-162
    sprite('ce430_15', 3)	# 163-165
    sprite('ce430_16', 3)	# 166-168
    label(10)
    sprite('ce430_15', 3)	# 169-171
    sprite('ce430_16', 3)	# 172-174
    sprite('ce430_17', 3)	# 175-177
    sprite('ce430_18', 3)	# 178-180

@State
def UltimateCharge():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)

        def upon_3():
            if (not CheckInput(0xa)):
                if (not CheckInput(0x13)):
                    clearUponHandler(3)
                    SLOT_51 = 1
    sprite('ce431_00', 4)	# 1-4
    Unknown1084(1)
    Unknown30080('')
    Unknown2036(43, -1, 0)
    Unknown2058(-10000)
    setInvincible(1)
    sprite('ce431_01', 3)	# 5-7
    GFX_0('Chargestart', 0)
    sprite('ce431_02', 3)	# 8-10
    sprite('ce431_03', 3)	# 11-13
    sprite('ce431_04', 3)	# 14-16
    sprite('ce431_05', 3)	# 17-19
    sprite('ce431_06', 3)	# 20-22
    sprite('ce431_07', 3)	# 23-25
    sprite('ce431_08', 3)	# 26-28
    sprite('ce431_09', 3)	# 29-31
    sprite('ce431_10', 3)	# 32-34
    Unknown7007('7063653235345f310000000000000000640000007063653235355f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ce005')
    SLOT_31 = 18000
    clearUponHandler(3)
    if SLOT_51:
        if (SLOT_59 <= 2):
            SLOT_59 = (SLOT_59 + 1)
    else:
        Unknown23159('UltimateChargeTame')
        if (SLOT_59 <= 0):
            SLOT_59 = 2
        else:
            SLOT_59 = 3
        sendToLabel(0)
    sprite('ce431_11', 3)	# 35-37
    SFX_3('blaze_long')
    GFX_0('ChargeAModel', 0)
    sprite('ce431_12', 3)	# 38-40
    sprite('ce431_11', 3)	# 41-43
    sprite('ce431_12', 1)	# 44-44
    sprite('ce431_12', 2)	# 45-46
    setInvincible(0)
    sprite('ce431_13', 4)	# 47-50
    sprite('ce431_14', 3)	# 51-53
    sprite('ce431_14', 1)	# 54-54
    ExitState()
    label(0)
    sprite('ce431_11', 3)	# 55-57
    SFX_3('blaze_long')
    GFX_0('ChargeAModel', 0)
    sprite('ce431_12', 3)	# 58-60
    sprite('ce431_11', 3)	# 61-63
    sprite('ce431_12', 3)	# 64-66
    sprite('ce431_11', 4)	# 67-70
    setInvincible(0)
    sprite('ce431_12', 4)	# 71-74
    sprite('ce431_11', 4)	# 75-78
    sprite('ce431_12', 4)	# 79-82
    sprite('ce431_11', 4)	# 83-86
    sprite('ce431_12', 4)	# 87-90
    sprite('ce431_11', 4)	# 91-94
    sprite('ce431_12', 4)	# 95-98
    sprite('ce431_11', 4)	# 99-102
    sprite('ce431_12', 4)	# 103-106
    sprite('ce431_11', 4)	# 107-110
    sprite('ce431_12', 4)	# 111-114
    sprite('ce431_13', 4)	# 115-118
    sprite('ce431_14', 3)	# 119-121
    sprite('ce431_14', 1)	# 122-122

@State
def UltimateChargeOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)

        def upon_3():
            if (not CheckInput(0xa)):
                if (not CheckInput(0x13)):
                    clearUponHandler(3)
                    SLOT_51 = 1
    sprite('ce431_00', 4)	# 1-4
    Unknown1084(1)
    Unknown30080('')
    Unknown2036(43, -1, 0)
    Unknown2058(-10000)
    setInvincible(1)
    sprite('ce431_01', 3)	# 5-7
    GFX_0('Chargestart', 0)
    sprite('ce431_02', 3)	# 8-10
    sprite('ce431_03', 3)	# 11-13
    sprite('ce431_04', 3)	# 14-16
    sprite('ce431_05', 3)	# 17-19
    sprite('ce431_06', 3)	# 20-22
    sprite('ce431_07', 3)	# 23-25
    sprite('ce431_08', 3)	# 26-28
    sprite('ce431_09', 3)	# 29-31
    sprite('ce431_10', 3)	# 32-34
    Unknown7007('7063653235345f300000000000000000640000007063653235355f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('ce005')
    SLOT_31 = 18000
    clearUponHandler(3)
    if SLOT_51:
        if (SLOT_59 <= 2):
            SLOT_59 = (SLOT_59 + 1)
        else:
            Unknown23159('UltimateChargeODTame')
            SLOT_59 = 3
    else:
        SLOT_59 = 3
        sendToLabel(0)
    sprite('ce431_11', 3)	# 35-37
    SFX_3('blaze_long')
    GFX_0('ChargeAModel', 0)
    sprite('ce431_12', 3)	# 38-40
    sprite('ce431_11', 3)	# 41-43
    sprite('ce431_12', 1)	# 44-44
    sprite('ce431_12', 2)	# 45-46
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('ce431_13', 4)	# 47-50
    sprite('ce431_14', 3)	# 51-53
    sprite('ce431_14', 1)	# 54-54
    ExitState()
    label(0)
    sprite('ce431_11', 3)	# 55-57
    SFX_3('blaze_long')
    GFX_0('ChargeAModel', 0)
    sprite('ce431_12', 3)	# 58-60
    sprite('ce431_11', 3)	# 61-63
    sprite('ce431_12', 3)	# 64-66
    sprite('ce431_11', 4)	# 67-70
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('ce431_12', 4)	# 71-74
    sprite('ce431_11', 4)	# 75-78
    sprite('ce431_12', 4)	# 79-82
    sprite('ce431_11', 4)	# 83-86
    sprite('ce431_12', 4)	# 87-90
    sprite('ce431_11', 4)	# 91-94
    sprite('ce431_12', 4)	# 95-98
    sprite('ce431_11', 4)	# 99-102
    sprite('ce431_12', 4)	# 103-106
    sprite('ce431_11', 4)	# 107-110
    sprite('ce431_12', 4)	# 111-114
    sprite('ce431_13', 4)	# 115-118
    sprite('ce431_14', 3)	# 119-121
    sprite('ce431_14', 1)	# 122-122

@State
def UltimateAguneyasutora_Far():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        sendToLabelUpon(2, 1)
    sprite('ce432_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('ce432_00', 1)	# 4-4
    Unknown7007('7063653235365f300000000000000000640000007063653235365f310000000000000000640000007063653235375f300000000000000000640000007063653235375f31000000000000000064000000')
    loopRest()
    sprite('ce432_01', 3)	# 5-7
    physicsYImpulse(14000)
    setGravity(800)
    sprite('ce432_02', 3)	# 8-10
    sprite('ce432_03', 2)	# 11-12
    Unknown30080('')
    Unknown2036(41, -1, 0)
    Unknown2058(-10000)
    Unknown23029(11, 503, 0)
    sprite('ce432_04', 2)	# 13-14
    sprite('ce432_05', 2)	# 15-16
    sprite('ce432_03', 2)	# 17-18
    sprite('ce432_04', 2)	# 19-20
    sprite('ce432_05', 2)	# 21-22
    sprite('ce432_03', 2)	# 23-24
    Unknown1022()
    Unknown1084(1)
    sprite('ce432_04', 2)	# 25-26
    sprite('ce432_05', 2)	# 27-28
    sprite('ce432_03', 2)	# 29-30
    sprite('ce432_04', 2)	# 31-32
    sprite('ce432_05', 2)	# 33-34
    sprite('ce432_03', 2)	# 35-36
    sprite('ce432_04', 2)	# 37-38
    sprite('ce432_05', 2)	# 39-40
    sprite('ce432_06', 3)	# 41-43
    Unknown1023()
    sprite('ce432_07', 3)	# 44-46
    sprite('ce432_08', 5)	# 47-51
    sprite('ce432_08', 3)	# 52-54
    setInvincible(0)
    sprite('ce432_09', 3)	# 55-57
    sprite('ce432_10', 3)	# 58-60
    sprite('ce432_11', 3)	# 61-63
    setGravity(2000)
    sprite('ce020_04', 3)	# 64-66
    sprite('ce020_05', 3)	# 67-69
    sprite('ce020_06', 3)	# 70-72
    label(0)
    sprite('ce020_07', 4)	# 73-76
    sprite('ce020_08', 4)	# 77-80
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce010_00', 4)	# 81-84
    Unknown18009(1)
    sprite('ce010_01', 4)	# 85-88
    sprite('ce010_02', 4)	# 89-92

@State
def UltimateAguneyasutoraOD_Far():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        sendToLabelUpon(2, 1)
    sprite('ce432_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('ce432_00', 1)	# 4-4
    Unknown7007('7063653235365f300000000000000000640000007063653235365f310000000000000000640000007063653235375f300000000000000000640000007063653235375f31000000000000000064000000')
    loopRest()
    sprite('ce432_01', 3)	# 5-7
    physicsYImpulse(14000)
    setGravity(800)
    sprite('ce432_02', 3)	# 8-10
    sprite('ce432_03', 2)	# 11-12
    Unknown30080('')
    Unknown2036(41, -1, 0)
    Unknown2058(-10000)
    Unknown23029(11, 505, 0)
    sprite('ce432_04', 2)	# 13-14
    sprite('ce432_05', 2)	# 15-16
    sprite('ce432_03', 2)	# 17-18
    sprite('ce432_04', 2)	# 19-20
    sprite('ce432_05', 2)	# 21-22
    sprite('ce432_03', 2)	# 23-24
    Unknown1022()
    Unknown1084(1)
    sprite('ce432_04', 2)	# 25-26
    sprite('ce432_05', 2)	# 27-28
    sprite('ce432_03', 2)	# 29-30
    sprite('ce432_04', 2)	# 31-32
    sprite('ce432_05', 2)	# 33-34
    sprite('ce432_03', 2)	# 35-36
    sprite('ce432_04', 2)	# 37-38
    sprite('ce432_05', 2)	# 39-40
    sprite('ce432_06', 3)	# 41-43
    Unknown1023()
    sprite('ce432_07', 3)	# 44-46
    sprite('ce432_08', 5)	# 47-51
    sprite('ce432_08', 3)	# 52-54
    setInvincible(0)
    sprite('ce432_09', 3)	# 55-57
    sprite('ce432_10', 3)	# 58-60
    sprite('ce432_11', 3)	# 61-63
    setGravity(2000)
    sprite('ce020_04', 3)	# 64-66
    sprite('ce020_05', 3)	# 67-69
    sprite('ce020_06', 3)	# 70-72
    label(0)
    sprite('ce020_07', 4)	# 73-76
    sprite('ce020_08', 4)	# 77-80
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce010_00', 4)	# 81-84
    Unknown18009(1)
    sprite('ce010_01', 4)	# 85-88
    sprite('ce010_02', 4)	# 89-92

@State
def UltimateAguneyasutora_Near():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        sendToLabelUpon(2, 1)
    sprite('ce432_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('ce432_00', 1)	# 4-4
    Unknown7007('7063653235365f300000000000000000640000007063653235365f310000000000000000640000007063653235375f300000000000000000640000007063653235375f31000000000000000064000000')
    loopRest()
    sprite('ce432_01', 3)	# 5-7
    physicsYImpulse(14000)
    setGravity(800)
    sprite('ce432_02', 3)	# 8-10
    sprite('ce432_03', 2)	# 11-12
    Unknown30080('')
    Unknown2036(41, -1, 0)
    Unknown2058(-10000)
    Unknown23029(11, 504, 0)
    sprite('ce432_04', 2)	# 13-14
    sprite('ce432_05', 2)	# 15-16
    sprite('ce432_03', 2)	# 17-18
    sprite('ce432_04', 2)	# 19-20
    sprite('ce432_05', 2)	# 21-22
    sprite('ce432_03', 2)	# 23-24
    Unknown1022()
    Unknown1084(1)
    sprite('ce432_04', 2)	# 25-26
    sprite('ce432_05', 2)	# 27-28
    sprite('ce432_03', 2)	# 29-30
    sprite('ce432_04', 2)	# 31-32
    sprite('ce432_05', 2)	# 33-34
    sprite('ce432_03', 2)	# 35-36
    sprite('ce432_04', 2)	# 37-38
    sprite('ce432_05', 2)	# 39-40
    sprite('ce432_06', 3)	# 41-43
    Unknown1023()
    sprite('ce432_07', 3)	# 44-46
    sprite('ce432_08', 5)	# 47-51
    sprite('ce432_08', 3)	# 52-54
    setInvincible(0)
    sprite('ce432_09', 3)	# 55-57
    sprite('ce432_10', 3)	# 58-60
    sprite('ce432_11', 3)	# 61-63
    setGravity(2000)
    sprite('ce020_04', 3)	# 64-66
    sprite('ce020_05', 3)	# 67-69
    sprite('ce020_06', 3)	# 70-72
    label(0)
    sprite('ce020_07', 4)	# 73-76
    sprite('ce020_08', 4)	# 77-80
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce010_00', 4)	# 81-84
    Unknown18009(1)
    sprite('ce010_01', 4)	# 85-88
    sprite('ce010_02', 4)	# 89-92

@State
def UltimateAguneyasutoraOD_Near():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        sendToLabelUpon(2, 1)
    sprite('ce432_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('ce432_00', 1)	# 4-4
    Unknown7007('7063653235365f300000000000000000640000007063653235365f310000000000000000640000007063653235375f300000000000000000640000007063653235375f31000000000000000064000000')
    loopRest()
    sprite('ce432_01', 3)	# 5-7
    physicsYImpulse(14000)
    setGravity(800)
    sprite('ce432_02', 3)	# 8-10
    sprite('ce432_03', 2)	# 11-12
    Unknown30080('')
    Unknown2036(41, -1, 0)
    Unknown2058(-10000)
    Unknown23029(11, 506, 0)
    sprite('ce432_04', 2)	# 13-14
    sprite('ce432_05', 2)	# 15-16
    sprite('ce432_03', 2)	# 17-18
    sprite('ce432_04', 2)	# 19-20
    sprite('ce432_05', 2)	# 21-22
    sprite('ce432_03', 2)	# 23-24
    Unknown1022()
    Unknown1084(1)
    sprite('ce432_04', 2)	# 25-26
    sprite('ce432_05', 2)	# 27-28
    sprite('ce432_03', 2)	# 29-30
    sprite('ce432_04', 2)	# 31-32
    sprite('ce432_05', 2)	# 33-34
    sprite('ce432_03', 2)	# 35-36
    sprite('ce432_04', 2)	# 37-38
    sprite('ce432_05', 2)	# 39-40
    sprite('ce432_06', 3)	# 41-43
    Unknown1023()
    sprite('ce432_07', 3)	# 44-46
    sprite('ce432_08', 5)	# 47-51
    sprite('ce432_08', 3)	# 52-54
    setInvincible(0)
    sprite('ce432_09', 3)	# 55-57
    sprite('ce432_10', 3)	# 58-60
    sprite('ce432_11', 3)	# 61-63
    setGravity(2000)
    sprite('ce020_04', 3)	# 64-66
    sprite('ce020_05', 3)	# 67-69
    sprite('ce020_06', 3)	# 70-72
    label(0)
    sprite('ce020_07', 4)	# 73-76
    sprite('ce020_08', 4)	# 77-80
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ce010_00', 4)	# 81-84
    Unknown18009(1)
    sprite('ce010_01', 4)	# 85-88
    sprite('ce010_02', 4)	# 89-92

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(30000)
        AirPushbackX(40000)
        AirPushbackY(50000)
        YImpluseBeforeWallbounce(0)
        Unknown11091(100)
        Unknown11064(3)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown9001(6)

        def upon_32():
            SLOT_51 = 1
            Unknown23088(1, 1)
            Unknown23084(1)
            GFX_0('IchigekiCamera', 100)
            Unknown48('0100000002000000340000000b0000000200000016000000')
            Unknown48('0100000002000000350000000b0000000200000017000000')
            Unknown23157(1)
            Unknown2037(1)

        def upon_STATE_END():
            pass

        def upon_3():
            if SLOT_56:
                op(4, 2, 18, 0, 10)
                if (SLOT_0 == 0):
                    GFX_0('IchigekiCopyZanzoh', 100)
            if SLOT_2:
                SLOT_2 = 0
                Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000020000000')
        Unknown2004(1, 0)
    sprite('ce450_00', 3)	# 1-3
    setInvincible(1)
    sprite('ce450_01', 3)	# 4-6
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(60000)
    physicsYImpulse(-1500)
    Unknown35()
    sprite('ce450_02', 3)	# 7-9
    sprite('ce450_03', 3)	# 10-12
    sprite('ce450_04', 15)	# 13-27
    Unknown2036(60, -1, 2)
    GFX_0('P4U_Cutin_Parent', 100)
    Unknown23147()
    tag_voice(1, 'pce290_0', 'pce290_1', '', '')
    sprite('ce450_04', 4)	# 28-31
    physicsXImpulse(6000)
    physicsYImpulse(8000)
    setGravity(1800)
    sendToLabelUpon(2, 1)
    sprite('ce450_05', 4)	# 32-35
    SFX_3('hit_l_slow')
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('ce450_06', 3)	# 36-38
    Unknown23029(11, 700, 0)
    sprite('ce450_06', 32767)	# 39-32805
    label(1)
    sprite('ce450_07', 3)	# 32806-32808
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeX(50000)
    Unknown1045(5000)
    sprite('ce450_08', 65)	# 32809-32873
    sprite('ce450_08', 50)	# 32874-32923
    clearUponHandler(32)
    if SLOT_51:
        _gotolabel(2)
    setInvincible(0)
    sprite('ce450_09', 4)	# 32924-32927
    sprite('ce450_10', 4)	# 32928-32931
    sprite('ce450_11', 4)	# 32932-32935
    loopRest()
    ExitState()
    label(2)
    sprite('ce450_08', 20)	# 32936-32955
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000021000000')
    sprite('ce450_12', 70)	# 32956-33025
    sprite('ce450_12', 35)	# 33026-33060
    Unknown1000(0)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000022000000')
    sprite('ce450_13', 6)	# 33061-33066
    SFX_3('ce005')
    SFX_3('blaze_long')
    GFX_0('ChargeIchigekiModel', 100)
    sprite('ce450_14', 6)	# 33067-33072
    sprite('ce450_15', 6)	# 33073-33078
    sprite('ce450_16', 6)	# 33079-33084
    sprite('ce450_17', 6)	# 33085-33090
    sprite('ce450_18', 6)	# 33091-33096
    sprite('ce450_17', 6)	# 33097-33102
    sprite('ce450_16', 6)	# 33103-33108
    sprite('ce450_15', 6)	# 33109-33114
    tag_voice(0, 'pce291_0', 'pce291_1', '', '')
    sprite('ce450_14', 6)	# 33115-33120
    sprite('ce450_13', 6)	# 33121-33126
    sprite('ce450_12', 6)	# 33127-33132
    sprite('ce450_13', 6)	# 33133-33138
    SFX_3('ce005')
    SFX_3('blaze_long')
    sprite('ce450_14', 6)	# 33139-33144
    sprite('ce450_15', 6)	# 33145-33150
    sprite('ce450_16', 6)	# 33151-33156
    sprite('ce450_17', 6)	# 33157-33162
    sprite('ce450_18', 16)	# 33163-33178
    sprite('ce450_17', 8)	# 33179-33186
    sprite('ce450_19', 8)	# 33187-33194
    sprite('ce450_20', 8)	# 33195-33202
    SLOT_56 = 1
    sprite('ce450_21', 8)	# 33203-33210
    sprite('ce450_22', 4)	# 33211-33214
    Unknown36(22)
    Unknown1086(22)
    teleportRelativeX(-520000)
    Unknown1007(800000)
    physicsYImpulse(-22000)
    physicsXImpulse(0)
    Unknown35()
    sprite('ce450_23', 4)	# 33215-33218
    physicsXImpulse(10000)
    physicsYImpulse(4000)
    setGravity(100)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000023000000')
    sprite('ce450_24', 4)	# 33219-33222
    sprite('ce450_25', 4)	# 33223-33226
    GFX_0('IchigekiJumpSmoke', 104)
    sprite('ce450_25', 4)	# 33227-33230
    sprite('ce450_25', 4)	# 33231-33234
    sprite('ce450_25', 10)	# 33235-33244
    Unknown23024(2)
    Unknown1019(4)
    YAccel(4)
    setGravity(0)
    Unknown36(22)
    Unknown1019(4)
    YAccel(4)
    setGravity(0)
    Unknown35()
    sprite('ce450_25', 10)	# 33245-33254
    SLOT_56 = 0
    sprite('ce450_25', 17)	# 33255-33271
    sprite('ce450_26', 8)	# 33272-33279
    sprite('ce450_27', 8)	# 33280-33287
    sprite('ce450_28', 11)	# 33288-33298	 **attackbox here**
    Unknown23027()
    sprite('ce450_28', 5)	# 33299-33303	 **attackbox here**
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('ce450_28', 2)	# 33304-33305	 **attackbox here**
    Unknown3038(1)
    Unknown26('SCEF_FadeBlack12In')
    GFX_0('IchigekiPicture', 100)
    GFX_0('IchiHaikei', 100)
    Unknown23024(0)
    Unknown4004('534345465f55737567757261690000000000000000000000000000000000000064000000')
    SFX_3('ce001')
    SFX_3('damage_ichigeki_hit')
    tag_voice(0, 'pce292_0', 'pce292_1', '', '')
    sprite('ce450_28', 2)	# 33306-33307	 **attackbox here**
    sprite('ce450_28', 6)	# 33308-33313	 **attackbox here**
    sprite('ce450_28', 40)	# 33314-33353	 **attackbox here**
    SFX_3('damage_ichigeki_hit')
    Unknown11023(1)
    RefreshMultihit()
    sprite('ce450_28', 30)	# 33354-33383	 **attackbox here**
    sprite('ce450_28', 50)	# 33384-33433	 **attackbox here**
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('ce203_04', 55)	# 33434-33488
    Unknown3038(0)
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000024000000')
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown18010()
    sprite('ce203_05', 3)	# 33489-33491
    sprite('ce203_06', 4)	# 33492-33495
    sprite('ce203_07', 3)	# 33496-33498
    Unknown2001()
    sprite('ce203_08', 3)	# 33499-33501
    sprite('ce203_09', 3)	# 33502-33504
    sprite('ce000_00', 6)	# 33505-33510
    sprite('ce000_01', 6)	# 33511-33516
    GFX_1('ceef_ichigekiwin_rain', 100)
    sprite('ce000_02', 6)	# 33517-33522
    sprite('ce000_03', 6)	# 33523-33528
    sprite('ce000_04', 6)	# 33529-33534
    sprite('ce000_05', 6)	# 33535-33540
    sprite('ce000_06', 6)	# 33541-33546
    sprite('ce000_07', 6)	# 33547-33552
    sprite('ce000_08', 6)	# 33553-33558
    sprite('ce000_09', 6)	# 33559-33564
    sprite('ce000_00', 6)	# 33565-33570
    tag_voice(0, 'pce293_0', '', '', '')
    sprite('ce000_01', 6)	# 33571-33576
    sprite('ce000_02', 6)	# 33577-33582
    sprite('ce000_03', 6)	# 33583-33588
    sprite('ce000_04', 6)	# 33589-33594
    sprite('ce000_05', 6)	# 33595-33600
    sprite('ce000_06', 6)	# 33601-33606
    sprite('ce000_07', 6)	# 33607-33612
    sprite('ce000_08', 6)	# 33613-33618
    sprite('ce000_09', 6)	# 33619-33624
    sprite('ce611_00', 4)	# 33625-33628
    sprite('ce611_01', 4)	# 33629-33632
    sprite('ce611_02', 4)	# 33633-33636
    sprite('ce611_03', 4)	# 33637-33640
    sprite('ce611_04', 4)	# 33641-33644
    tag_voice(0, '', 'pce293_1', '', '')
    sprite('ce611_05', 32767)	# 33645-66411
    GFX_0('IchigekiWinRainbow', 0)
    GFX_1('ceef_ichigekiwinkira_05', 1)
    GFX_1('ceef_ichigekiwinkira_05', 2)
    GFX_1('ceef_ichigekiwinkira_05', 3)
    SFX_3('ce002')
    SFX_3('ce006')
    Unknown23018(1)

@Subroutine
def MouthTableInit():
    Unknown18011('pce000', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce293_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce293_1', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce500', 12643, 13153, 13153, 13923, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce504', 12643, 13665, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce505', 12643, 13665, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce506', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce507', 12643, 13665, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce521', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce522', 12643, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce523', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce524', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce525', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce404_0', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce404_1', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce405_0', 12643, 13665, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce405_1', 12643, 13665, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce601bma', 12643, 14177, 12643, 24882, 25399, 12849, 12641, 25394, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce600pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce600pyo', 12643, 13153, 25392, 24887, 25399, 24887, 13361, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24881, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce600ryn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 12337, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce600umi', 12643, 14177, 14179, 12641, 25394, 24887, 12849, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 13105, 13411, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce601baz', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12849, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce601bmk', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce601bpt', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce601pbc', 12643, 14177, 12643, 24881, 25399, 24887, 12849, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 14129, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce601pyu', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce601uwa', 12643, 12897, 25394, 14131, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 12641, 25394, 12338, 12897, 25394, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce700bma', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24885, 25397, 24885, 25397, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce700bmk', 12643, 12641, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce700pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 13618, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce700umi', 12643, 12897, 25392, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce700uwa', 12643, 14177, 12643, 24880, 25399, 12337, 12641, 25394, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce701baz', 12643, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce701bmk', 12643, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce701bpt', 12643, 12641, 25396, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce701pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 14129, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce701pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce701pyo', 12643, 14177, 14179, 12641, 25396, 14132, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pce701ryn', 12643, 14177, 12643, 24880, 25397, 24885, 25397, 13618, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('baz')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('bma')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('ce601_00', 5)	# 2-6
    Unknown7006('pce502', 100, 895837040, 13104, 0, 0, 100, 895837040, 13872, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ce601_01', 5)	# 7-11
    sprite('ce601_02', 5)	# 12-16
    sprite('ce601_03', 5)	# 17-21
    sprite('ce601_04', 5)	# 22-26
    sprite('ce601_03', 12)	# 27-38
    sprite('ce601_04', 5)	# 39-43
    sprite('ce601_03', 5)	# 44-48
    sprite('ce601_05', 5)	# 49-53
    sprite('ce601_06', 5)	# 54-58
    sprite('ce601_07', 5)	# 59-63
    sprite('ce601_08', 5)	# 64-68
    sprite('ce601_09', 5)	# 69-73
    sprite('ce601_10', 5)	# 74-78
    sprite('ce601_11', 5)	# 79-83
    sprite('ce601_10', 12)	# 84-95
    sprite('ce601_11', 5)	# 96-100
    sprite('ce601_12', 5)	# 101-105
    sprite('ce601_13', 5)	# 106-110
    sprite('ce601_14', 5)	# 111-115
    sprite('ce601_15', 5)	# 116-120
    sprite('ce601_14', 5)	# 121-125
    sprite('ce601_16', 5)	# 126-130
    SFX_3('walk_stone_light')
    sprite('ce601_14', 5)	# 131-135
    sprite('ce601_15', 5)	# 136-140
    sprite('ce601_14', 5)	# 141-145
    sprite('ce601_16', 5)	# 146-150
    sprite('ce601_14', 5)	# 151-155
    sprite('ce601_17', 5)	# 156-160
    sprite('ce601_18', 5)	# 161-165
    sprite('ce001_01', 6)	# 166-171
    sprite('ce001_02', 6)	# 172-177
    sprite('ce001_03', 6)	# 178-183
    sprite('ce001_04', 6)	# 184-189
    sprite('ce001_05', 51)	# 190-240
    sprite('ce001_00', 6)	# 241-246
    Unknown23018(1)
    label(1)
    sprite('ce000_00', 6)	# 247-252
    sprite('ce000_01', 6)	# 253-258
    sprite('ce000_02', 6)	# 259-264
    sprite('ce000_03', 6)	# 265-270
    sprite('ce000_04', 6)	# 271-276
    sprite('ce000_05', 6)	# 277-282
    sprite('ce000_06', 6)	# 283-288
    sprite('ce000_07', 6)	# 289-294
    sprite('ce000_08', 6)	# 295-300
    sprite('ce000_09', 6)	# 301-306
    loopRest()
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('ce600_00', 3)	# 307-309
    Unknown2034(0)
    Unknown2017(0)
    Unknown1000(0)
    teleportRelativeY(600000)
    setGravity(0)
    sprite('ce600_00', 3)	# 310-312
    ScreenShake(3000, 0)
    Unknown1015(-61500)
    physicsYImpulse(-32000)
    sendToLabelUpon(5, 12)
    if random_(2, 0, 50):
        SFX_1('pce500')
    else:
        SLOT_51 = 1
    label(11)
    sprite('ce600_01', 3)	# 313-315
    sprite('ce600_00', 3)	# 316-318
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('ce402_14', 7)	# 319-325
    Unknown1084(1)
    Unknown1019(30)
    Unknown2005()
    teleportRelativeX(-100000)
    Unknown8000(0, 1, 1)
    sprite('ce402_15', 7)	# 326-332
    Unknown1019(30)
    sprite('ce402_16', 7)	# 333-339
    Unknown1019(30)
    sprite('ce402_17', 7)	# 340-346
    Unknown1019(30)
    sprite('ce402_18', 7)	# 347-353
    Unknown1019(0)
    sprite('ce010_02', 3)	# 354-356
    Unknown1000(1230000)
    sprite('ce013_00', 3)	# 357-359
    Unknown2005()
    sprite('ce013_01', 3)	# 360-362
    sprite('ce013_02', 3)	# 363-365
    sprite('ce010_02', 3)	# 366-368
    sprite('ce010_01', 3)	# 369-371
    sprite('ce010_00', 3)	# 372-374
    sprite('ce600_02', 4)	# 375-378
    if SLOT_51:
        SFX_1('pce501')
    Unknown21007(24, 41)
    sprite('ce600_03', 4)	# 379-382
    sprite('ce600_04', 3)	# 383-385
    sprite('ce600_05', 4)	# 386-389
    sprite('ce600_04', 2)	# 390-391
    sprite('ce600_03', 5)	# 392-396
    sprite('ce600_04', 4)	# 397-400
    sprite('ce600_05', 4)	# 401-404
    sprite('ce600_04', 2)	# 405-406
    sprite('ce600_03', 5)	# 407-411
    sprite('ce600_04', 4)	# 412-415
    sprite('ce600_05', 4)	# 416-419
    sprite('ce600_04', 2)	# 420-421
    sprite('ce600_03', 5)	# 422-426
    sprite('ce600_04', 4)	# 427-430
    sprite('ce600_05', 4)	# 431-434
    sprite('ce600_05', 4)	# 435-438
    sprite('ce600_06', 6)	# 439-444
    sprite('ce600_07', 6)	# 445-450
    sprite('ce001_01', 6)	# 451-456
    sprite('ce001_02', 6)	# 457-462
    sprite('ce001_03', 6)	# 463-468
    sprite('ce001_04', 6)	# 469-474
    sprite('ce001_05', 56)	# 475-530
    sprite('ce001_00', 6)	# 531-536
    Unknown23018(1)
    label(13)
    sprite('ce000_00', 6)	# 537-542
    sprite('ce000_01', 6)	# 543-548
    sprite('ce000_02', 6)	# 549-554
    sprite('ce000_03', 6)	# 555-560
    sprite('ce000_04', 6)	# 561-566
    sprite('ce000_05', 6)	# 567-572
    sprite('ce000_06', 6)	# 573-578
    sprite('ce000_07', 6)	# 579-584
    sprite('ce000_08', 6)	# 585-590
    sprite('ce000_09', 6)	# 591-596
    loopRest()
    label(13)
    ExitState()
    label(20)
    sprite('ce000_00', 1)	# 597-597
    SFX_1('pce701ryn')
    label(21)
    sprite('ce000_00', 6)	# 598-603
    sprite('ce000_01', 6)	# 604-609
    sprite('ce000_02', 6)	# 610-615
    sprite('ce000_03', 6)	# 616-621
    sprite('ce000_04', 6)	# 622-627
    sprite('ce000_05', 6)	# 628-633
    sprite('ce000_06', 6)	# 634-639
    sprite('ce000_07', 6)	# 640-645
    sprite('ce000_08', 6)	# 646-651
    sprite('ce000_09', 6)	# 652-657
    gotoLabel(21)
    label(100)
    sprite('ce000_00', 1)	# 658-658
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('ce000_00', 6)	# 659-664
    sprite('ce000_01', 6)	# 665-670
    sprite('ce000_02', 6)	# 671-676
    sprite('ce000_03', 6)	# 677-682
    sprite('ce000_04', 6)	# 683-688
    sprite('ce000_05', 6)	# 689-694
    sprite('ce000_06', 6)	# 695-700
    sprite('ce000_07', 6)	# 701-706
    sprite('ce000_08', 6)	# 707-712
    sprite('ce000_09', 6)	# 713-718
    gotoLabel(101)
    label(102)
    sprite('ce611_00', 4)	# 719-722
    sprite('ce611_01', 4)	# 723-726
    SFX_1('pce601baz')
    sprite('ce611_02', 4)	# 727-730
    sprite('ce611_03', 4)	# 731-734
    sprite('ce611_04', 4)	# 735-738
    SFX_3('hit_l_fast')
    label(103)
    sprite('ce611_05', 1)	# 739-739
    if SLOT_97:
        _gotolabel(103)
    sprite('ce611_05', 32767)	# 740-33506
    Unknown21011(120)
    ExitState()
    label(110)
    sprite('ce000_00', 1)	# 33507-33507
    if SLOT_158:
        Unknown1000(-1115000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ce000_00', 6)	# 33508-33513
    sprite('ce000_01', 6)	# 33514-33519
    sprite('ce000_02', 6)	# 33520-33525
    sprite('ce000_03', 6)	# 33526-33531
    sprite('ce000_04', 6)	# 33532-33537
    sprite('ce000_05', 6)	# 33538-33543
    sprite('ce000_06', 6)	# 33544-33549
    sprite('ce000_07', 6)	# 33550-33555
    sprite('ce000_08', 6)	# 33556-33561
    sprite('ce000_09', 6)	# 33562-33567
    gotoLabel(111)
    label(112)
    sprite('ce610_00', 4)	# 33568-33571
    Unknown2004(1, 0)
    sprite('ce610_01', 4)	# 33572-33575
    sprite('ce610_02', 4)	# 33576-33579
    SFX_1('pce601bpt')
    sprite('ce610_03', 4)	# 33580-33583
    sprite('ce321_08', 4)	# 33584-33587
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(2000)
    sendToLabelUpon(2, 113)
    SFX_3('runjump_stone_light')
    sprite('ce321_09', 4)	# 33588-33591
    sprite('ce321_10', 4)	# 33592-33595
    sprite('ce321_11', 4)	# 33596-33599
    sprite('ce321_12', 4)	# 33600-33603
    sprite('ce321_13', 4)	# 33604-33607
    sprite('ce321_14', 32767)	# 33608-66374
    loopRest()
    label(113)
    sprite('ce321_15', 4)	# 66375-66378
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    SFX_3('walk_stone_light')
    sprite('ce321_16', 9)	# 66379-66387
    sprite('ce321_17', 3)	# 66388-66390
    sprite('ce321_18', 3)	# 66391-66393
    sprite('ce321_19', 3)	# 66394-66396
    sprite('ce610_04', 6)	# 66397-66402
    sprite('ce610_05', 6)	# 66403-66408
    sprite('ce610_06', 6)	# 66409-66414
    sprite('ce610_07', 6)	# 66415-66420
    sprite('ce610_08', 6)	# 66421-66426
    SFX_3('cloth_l')
    label(114)
    sprite('ce610_06', 6)	# 66427-66432
    sprite('ce610_07', 6)	# 66433-66438
    sprite('ce610_08', 6)	# 66439-66444
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(114)
    sprite('ce610_09', 6)	# 66445-66450
    sprite('ce610_10', 6)	# 66451-66456
    Unknown21011(120)
    label(115)
    sprite('ce000_00', 6)	# 66457-66462
    sprite('ce000_01', 6)	# 66463-66468
    sprite('ce000_02', 6)	# 66469-66474
    sprite('ce000_03', 6)	# 66475-66480
    sprite('ce000_04', 6)	# 66481-66486
    sprite('ce000_05', 6)	# 66487-66492
    sprite('ce000_06', 6)	# 66493-66498
    sprite('ce000_07', 6)	# 66499-66504
    sprite('ce000_08', 6)	# 66505-66510
    sprite('ce000_09', 6)	# 66511-66516
    gotoLabel(115)
    ExitState()
    label(120)
    sprite('ce000_00', 1)	# 66517-66517
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ce000_00', 6)	# 66518-66523
    sprite('ce000_01', 6)	# 66524-66529
    sprite('ce000_02', 6)	# 66530-66535
    sprite('ce000_03', 6)	# 66536-66541
    sprite('ce000_04', 6)	# 66542-66547
    sprite('ce000_05', 6)	# 66548-66553
    sprite('ce000_06', 6)	# 66554-66559
    sprite('ce000_07', 6)	# 66560-66565
    sprite('ce000_08', 6)	# 66566-66571
    sprite('ce000_09', 6)	# 66572-66577
    gotoLabel(121)
    label(122)
    sprite('ce001_01', 6)	# 66578-66583
    SFX_1('pce601pbc')
    sprite('ce001_02', 6)	# 66584-66589
    sprite('ce001_03', 6)	# 66590-66595
    sprite('ce001_04', 6)	# 66596-66601
    label(123)
    sprite('ce001_05', 1)	# 66602-66602
    if SLOT_97:
        _gotolabel(123)
    sprite('ce001_05', 20)	# 66603-66622
    sprite('ce001_00', 6)	# 66623-66628
    Unknown21011(60)
    label(124)
    sprite('ce000_00', 6)	# 66629-66634
    sprite('ce000_01', 6)	# 66635-66640
    sprite('ce000_02', 6)	# 66641-66646
    sprite('ce000_03', 6)	# 66647-66652
    sprite('ce000_04', 6)	# 66653-66658
    sprite('ce000_05', 6)	# 66659-66664
    sprite('ce000_06', 6)	# 66665-66670
    sprite('ce000_07', 6)	# 66671-66676
    sprite('ce000_08', 6)	# 66677-66682
    sprite('ce000_09', 6)	# 66683-66688
    gotoLabel(124)
    ExitState()
    label(130)
    sprite('ce611_00', 4)	# 66689-66692
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ce611_01', 4)	# 66693-66696
    SFX_1('pce600pyo')
    sprite('ce611_02', 4)	# 66697-66700
    sprite('ce611_03', 4)	# 66701-66704
    sprite('ce611_04', 4)	# 66705-66708
    SFX_3('hit_l_fast')
    label(131)
    sprite('ce611_05', 1)	# 66709-66709
    if SLOT_97:
        _gotolabel(131)
    sprite('ce611_05', 30)	# 66710-66739
    sprite('ce611_03', 7)	# 66740-66746
    Unknown21011(90)
    Unknown21007(24, 40)
    sprite('ce611_01', 7)	# 66747-66753
    sprite('ce611_00', 7)	# 66754-66760
    label(132)
    sprite('ce000_00', 6)	# 66761-66766
    sprite('ce000_01', 6)	# 66767-66772
    sprite('ce000_02', 6)	# 66773-66778
    sprite('ce000_03', 6)	# 66779-66784
    sprite('ce000_04', 6)	# 66785-66790
    sprite('ce000_05', 6)	# 66791-66796
    sprite('ce000_06', 6)	# 66797-66802
    sprite('ce000_07', 6)	# 66803-66808
    sprite('ce000_08', 6)	# 66809-66814
    sprite('ce000_09', 6)	# 66815-66820
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('ce000_00', 1)	# 66821-66821
    if SLOT_158:
        Unknown1000(-1200000)
        Unknown2019(-500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ce000_00', 6)	# 66822-66827
    sprite('ce000_01', 6)	# 66828-66833
    sprite('ce000_02', 6)	# 66834-66839
    sprite('ce000_03', 6)	# 66840-66845
    sprite('ce000_04', 6)	# 66846-66851
    sprite('ce000_05', 6)	# 66852-66857
    sprite('ce000_06', 6)	# 66858-66863
    sprite('ce000_07', 6)	# 66864-66869
    sprite('ce000_08', 6)	# 66870-66875
    sprite('ce000_09', 6)	# 66876-66881
    gotoLabel(141)
    label(142)
    sprite('ce001_01', 6)	# 66882-66887
    SFX_1('pce601uwa')
    sprite('ce001_02', 6)	# 66888-66893
    sprite('ce001_03', 6)	# 66894-66899
    sprite('ce001_04', 6)	# 66900-66905
    sprite('ce001_05', 160)	# 66906-67065
    sprite('ce001_00', 6)	# 67066-67071
    label(143)
    sprite('ce000_00', 6)	# 67072-67077
    sprite('ce000_01', 6)	# 67078-67083
    sprite('ce000_02', 6)	# 67084-67089
    sprite('ce000_03', 6)	# 67090-67095
    sprite('ce000_04', 6)	# 67096-67101
    sprite('ce000_05', 6)	# 67102-67107
    sprite('ce000_06', 6)	# 67108-67113
    sprite('ce000_07', 6)	# 67114-67119
    sprite('ce000_08', 6)	# 67120-67125
    sprite('ce000_09', 6)	# 67126-67131
    if SLOT_97:
        _gotolabel(143)
    sprite('ce000_00', 1)	# 67132-67132
    Unknown18008()
    label(144)
    sprite('ce000_00', 6)	# 67133-67138
    sprite('ce000_01', 6)	# 67139-67144
    sprite('ce000_02', 6)	# 67145-67150
    sprite('ce000_03', 6)	# 67151-67156
    sprite('ce000_04', 6)	# 67157-67162
    sprite('ce000_05', 6)	# 67163-67168
    sprite('ce000_06', 6)	# 67169-67174
    sprite('ce000_07', 6)	# 67175-67180
    sprite('ce000_08', 6)	# 67181-67186
    sprite('ce000_09', 6)	# 67187-67192
    gotoLabel(144)
    ExitState()
    label(150)
    sprite('ce000_00', 1)	# 67193-67193
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ce000_00', 6)	# 67194-67199
    sprite('ce000_01', 6)	# 67200-67205
    sprite('ce000_02', 6)	# 67206-67211
    sprite('ce000_03', 6)	# 67212-67217
    sprite('ce000_04', 6)	# 67218-67223
    sprite('ce000_05', 6)	# 67224-67229
    sprite('ce000_06', 6)	# 67230-67235
    sprite('ce000_07', 6)	# 67236-67241
    sprite('ce000_08', 6)	# 67242-67247
    sprite('ce000_09', 6)	# 67248-67253
    gotoLabel(151)
    label(152)
    sprite('ce001_01', 6)	# 67254-67259
    SFX_1('pce601bmk')
    sprite('ce001_02', 6)	# 67260-67265
    sprite('ce001_03', 6)	# 67266-67271
    sprite('ce001_04', 6)	# 67272-67277
    sprite('ce001_05', 240)	# 67278-67517
    sprite('ce001_00', 6)	# 67518-67523
    sprite('ce611_00', 4)	# 67524-67527
    sprite('ce611_01', 4)	# 67528-67531
    sprite('ce611_02', 4)	# 67532-67535
    sprite('ce611_03', 4)	# 67536-67539
    sprite('ce611_04', 4)	# 67540-67543
    SFX_3('hit_l_fast')
    Unknown21011(120)
    sprite('ce611_05', 32767)	# 67544-100310
    ExitState()
    label(160)
    sprite('ce641_00', 1)	# 100311-100311
    Unknown2019(100)
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('pce601pyu')
        Unknown23018(1)
    label(161)
    sprite('ce641_00', 6)	# 100312-100317
    sprite('ce641_01', 6)	# 100318-100323
    SFX_3('cloth_l')
    sprite('ce641_02', 6)	# 100324-100329
    sprite('ce641_03', 6)	# 100330-100335
    sprite('ce641_04', 6)	# 100336-100341
    loopRest()
    gotoLabel(161)
    ExitState()
    label(170)
    sprite('ce601_00', 5)	# 100342-100346
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ce601_01', 5)	# 100347-100351
    SFX_1('pce600ryn')
    sprite('ce601_02', 5)	# 100352-100356
    sprite('ce601_03', 5)	# 100357-100361
    sprite('ce601_04', 5)	# 100362-100366
    sprite('ce601_03', 12)	# 100367-100378
    sprite('ce601_04', 5)	# 100379-100383
    sprite('ce601_03', 5)	# 100384-100388
    sprite('ce601_05', 5)	# 100389-100393
    sprite('ce601_06', 5)	# 100394-100398
    sprite('ce601_07', 5)	# 100399-100403
    sprite('ce601_08', 5)	# 100404-100408
    sprite('ce601_09', 5)	# 100409-100413
    sprite('ce601_10', 5)	# 100414-100418
    sprite('ce601_11', 5)	# 100419-100423
    sprite('ce601_10', 12)	# 100424-100435
    sprite('ce601_11', 5)	# 100436-100440
    sprite('ce601_12', 5)	# 100441-100445
    sprite('ce601_13', 5)	# 100446-100450
    sprite('ce601_14', 5)	# 100451-100455
    sprite('ce601_15', 5)	# 100456-100460
    sprite('ce601_14', 5)	# 100461-100465
    sprite('ce601_16', 5)	# 100466-100470
    SFX_3('walk_stone_light')
    sprite('ce601_14', 5)	# 100471-100475
    sprite('ce601_15', 5)	# 100476-100480
    sprite('ce601_14', 5)	# 100481-100485
    sprite('ce601_16', 5)	# 100486-100490
    sprite('ce601_14', 5)	# 100491-100495
    sprite('ce601_17', 5)	# 100496-100500
    sprite('ce601_18', 5)	# 100501-100505
    sprite('ce001_01', 6)	# 100506-100511
    sprite('ce001_02', 6)	# 100512-100517
    sprite('ce001_03', 6)	# 100518-100523
    sprite('ce001_04', 6)	# 100524-100529
    label(171)
    sprite('ce001_05', 1)	# 100530-100530
    if SLOT_97:
        _gotolabel(171)
    sprite('ce001_05', 20)	# 100531-100550
    sprite('ce001_00', 6)	# 100551-100556
    Unknown21007(24, 40)
    Unknown21011(300)
    label(172)
    sprite('ce000_00', 6)	# 100557-100562
    sprite('ce000_01', 6)	# 100563-100568
    sprite('ce000_02', 6)	# 100569-100574
    sprite('ce000_03', 6)	# 100575-100580
    sprite('ce000_04', 6)	# 100581-100586
    sprite('ce000_05', 6)	# 100587-100592
    sprite('ce000_06', 6)	# 100593-100598
    sprite('ce000_07', 6)	# 100599-100604
    sprite('ce000_08', 6)	# 100605-100610
    sprite('ce000_09', 6)	# 100611-100616
    loopRest()
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('ce611_00', 4)	# 100617-100620
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ce611_01', 4)	# 100621-100624
    SFX_1('pce600umi')
    sprite('ce611_02', 4)	# 100625-100628
    sprite('ce611_03', 4)	# 100629-100632
    sprite('ce611_04', 4)	# 100633-100636
    SFX_3('hit_l_fast')
    sprite('ce611_05', 300)	# 100637-100936
    sprite('ce611_03', 7)	# 100937-100943
    Unknown21011(200)
    Unknown21007(24, 40)
    sprite('ce611_01', 7)	# 100944-100950
    sprite('ce611_00', 7)	# 100951-100957
    label(181)
    sprite('ce000_00', 6)	# 100958-100963
    sprite('ce000_01', 6)	# 100964-100969
    sprite('ce000_02', 6)	# 100970-100975
    sprite('ce000_03', 6)	# 100976-100981
    sprite('ce000_04', 6)	# 100982-100987
    sprite('ce000_05', 6)	# 100988-100993
    sprite('ce000_06', 6)	# 100994-100999
    sprite('ce000_07', 6)	# 101000-101005
    sprite('ce000_08', 6)	# 101006-101011
    sprite('ce000_09', 6)	# 101012-101017
    gotoLabel(181)
    ExitState()
    label(190)
    sprite('ce000_00', 1)	# 101018-101018
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ce000_00', 6)	# 101019-101024
    sprite('ce000_01', 6)	# 101025-101030
    sprite('ce000_02', 6)	# 101031-101036
    sprite('ce000_03', 6)	# 101037-101042
    sprite('ce000_04', 6)	# 101043-101048
    sprite('ce000_05', 6)	# 101049-101054
    sprite('ce000_06', 6)	# 101055-101060
    sprite('ce000_07', 6)	# 101061-101066
    sprite('ce000_08', 6)	# 101067-101072
    sprite('ce000_09', 6)	# 101073-101078
    gotoLabel(191)
    label(192)
    sprite('ce611_00', 4)	# 101079-101082
    sprite('ce611_01', 4)	# 101083-101086
    SFX_1('pce601bma')
    sprite('ce611_02', 4)	# 101087-101090
    sprite('ce611_03', 4)	# 101091-101094
    sprite('ce611_04', 4)	# 101095-101098
    SFX_3('hit_l_fast')
    label(193)
    sprite('ce611_05', 1)	# 101099-101099
    if SLOT_97:
        _gotolabel(193)
    sprite('ce611_05', 20)	# 101100-101119
    sprite('ce611_03', 7)	# 101120-101126
    sprite('ce611_01', 7)	# 101127-101133
    sprite('ce611_00', 7)	# 101134-101140
    Unknown23018(1)
    label(194)
    sprite('ce000_00', 6)	# 101141-101146
    sprite('ce000_01', 6)	# 101147-101152
    sprite('ce000_02', 6)	# 101153-101158
    sprite('ce000_03', 6)	# 101159-101164
    sprite('ce000_04', 6)	# 101165-101170
    sprite('ce000_05', 6)	# 101171-101176
    sprite('ce000_06', 6)	# 101177-101182
    sprite('ce000_07', 6)	# 101183-101188
    sprite('ce000_08', 6)	# 101189-101194
    sprite('ce000_09', 6)	# 101195-101200
    gotoLabel(194)
    ExitState()
    label(200)
    sprite('ce642_00', 1)	# 101201-101201
    if SLOT_158:
        Unknown1000(-1350000)
    else:
        Unknown1000(-1350000)
    Unknown2037(14)
    SFX_1('pce600pak')
    Unknown2019(-500)
    label(201)
    sprite('ce642_00', 6)	# 101202-101207
    sprite('ce642_01', 6)	# 101208-101213
    sprite('ce642_02', 6)	# 101214-101219
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(201)
    sprite('ce642_03', 6)	# 101220-101225
    sprite('ce000_00', 6)	# 101226-101231
    sprite('ce000_01', 6)	# 101232-101237
    sprite('ce000_02', 6)	# 101238-101243
    sprite('ce000_03', 6)	# 101244-101249
    sprite('ce000_04', 6)	# 101250-101255
    sprite('ce000_05', 6)	# 101256-101261
    sprite('ce000_06', 6)	# 101262-101267
    sprite('ce000_07', 6)	# 101268-101273
    sprite('ce000_08', 6)	# 101274-101279
    sprite('ce000_09', 6)	# 101280-101285
    Unknown21007(24, 40)
    Unknown21011(360)
    label(202)
    sprite('ce000_00', 6)	# 101286-101291
    sprite('ce000_01', 6)	# 101292-101297
    sprite('ce000_02', 6)	# 101298-101303
    sprite('ce000_03', 6)	# 101304-101309
    sprite('ce000_04', 6)	# 101310-101315
    sprite('ce000_05', 6)	# 101316-101321
    sprite('ce000_06', 6)	# 101322-101327
    sprite('ce000_07', 6)	# 101328-101333
    sprite('ce000_08', 6)	# 101334-101339
    sprite('ce000_09', 6)	# 101340-101345
    gotoLabel(202)
    ExitState()
    label(991)
    sprite('ce000_00', 1)	# 101346-101346
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ce000_00', 6)	# 101347-101352
    sprite('ce000_01', 6)	# 101353-101358
    sprite('ce000_02', 6)	# 101359-101364
    sprite('ce000_03', 6)	# 101365-101370
    sprite('ce000_04', 6)	# 101371-101376
    sprite('ce000_05', 6)	# 101377-101382
    sprite('ce000_06', 6)	# 101383-101388
    sprite('ce000_07', 6)	# 101389-101394
    sprite('ce000_08', 6)	# 101395-101400
    sprite('ce000_09', 6)	# 101401-101406
    gotoLabel(992)
    label(993)
    sprite('ce033_00', 2)	# 101407-101408

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
    sprite('ce033_01', 3)	# 101409-101411
    label(994)
    sprite('ce033_02', 3)	# 101412-101414
    sprite('ce033_01', 3)	# 101415-101417
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 101418-101420
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
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('baz'):
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
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('pak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('ce610_00', 4)	# 4-7
    Unknown36(24)
    Unknown2034(0)
    Unknown2053(0)
    Unknown35()
    Unknown2004(1, 0)
    Unknown2034(0)
    sprite('ce610_01', 4)	# 8-11
    sprite('ce610_02', 4)	# 12-15
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pce524', 100, 895837040, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pce404_0', 100, 879059824, 828322864, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pce520', 100, 895837040, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ce610_03', 4)	# 16-19
    sprite('ce321_08', 4)	# 20-23
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(2000)
    sendToLabelUpon(2, 1)
    SFX_3('runjump_stone_light')
    sprite('ce321_09', 4)	# 24-27
    sprite('ce321_10', 4)	# 28-31
    sprite('ce321_11', 4)	# 32-35
    sprite('ce321_12', 4)	# 36-39
    sprite('ce321_13', 4)	# 40-43
    sprite('ce321_14', 32767)	# 44-32810
    loopRest()
    label(1)
    sprite('ce321_15', 4)	# 32811-32814
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    SFX_3('walk_stone_light')
    sprite('ce321_16', 9)	# 32815-32823
    sprite('ce321_17', 3)	# 32824-32826
    sprite('ce321_18', 3)	# 32827-32829
    sprite('ce321_19', 3)	# 32830-32832
    sprite('ce610_04', 6)	# 32833-32838
    sprite('ce610_05', 6)	# 32839-32844
    sprite('ce610_06', 6)	# 32845-32850
    sprite('ce610_07', 6)	# 32851-32856
    sprite('ce610_08', 6)	# 32857-32862
    SFX_3('cloth_l')
    label(2)
    sprite('ce610_06', 6)	# 32863-32868
    sprite('ce610_07', 6)	# 32869-32874
    sprite('ce610_08', 6)	# 32875-32880
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('ce611_00', 4)	# 32881-32884
    Unknown2019(0)
    sprite('ce611_01', 4)	# 32885-32888
    sprite('ce611_02', 4)	# 32889-32892
    sprite('ce611_03', 4)	# 32893-32896
    sprite('ce611_04', 4)	# 32897-32900
    if SLOT_158:
        if SLOT_52:
            SLOT_51 = 1
        elif SLOT_108:
            SLOT_2 = 1
        elif random_(2, 0, 50):
            SFX_1('pce522')
            Unknown23018(1)
        else:
            SLOT_53 = 1
    SFX_3('hit_l_fast')
    sprite('ce611_05', 30)	# 32901-32930
    sprite('ce611_05', 20)	# 32931-32950
    Unknown23029(11, 600, 0)
    GFX_0('MatchWin2_bikkuri', 0)
    sprite('ce611_05', 16)	# 32951-32966
    sprite('ce611_05', 4)	# 32967-32970
    SFX_3('hit_l_middle')
    sprite('ce611_06', 4)	# 32971-32974
    Unknown26('MatchWin2_bikkuri')
    sprite('ce611_07', 3)	# 32975-32977
    sprite('ce611_08', 4)	# 32978-32981
    sprite('ce611_09', 6)	# 32982-32987
    sprite('ce611_09', 4)	# 32988-32991
    SFX_3('hit_l_middle')
    sprite('ce611_10', 4)	# 32992-32995
    Unknown2019(-1000)
    sprite('ce611_11', 4)	# 32996-32999
    sprite('ce611_12', 4)	# 33000-33003
    if SLOT_51:
        Unknown7006('pce524', 100, 895837040, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        if SLOT_2:
            Unknown7006('pce404_0', 100, 879059824, 828322864, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if SLOT_53:
            SFX_1('pce523')
    Unknown23018(1)
    sprite('ce611_13', 4)	# 33004-33007
    sprite('ce611_14', 4)	# 33008-33011
    SFX_3('cloth_l')
    label(11)
    sprite('ce611_12', 4)	# 33012-33015
    sprite('ce611_13', 4)	# 33016-33019
    sprite('ce611_14', 4)	# 33020-33023
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('ce001_01', 6)	# 33024-33029
    SFX_1('pce700bmk')
    sprite('ce001_02', 6)	# 33030-33035
    sprite('ce001_03', 6)	# 33036-33041
    sprite('ce001_04', 6)	# 33042-33047
    sprite('ce001_05', 90)	# 33048-33137
    sprite('ce001_00', 6)	# 33138-33143
    sprite('ce611_00', 4)	# 33144-33147
    Unknown21007(24, 40)
    sprite('ce611_01', 4)	# 33148-33151
    SFX_1('pce701bmk')
    sprite('ce611_02', 4)	# 33152-33155
    sprite('ce611_03', 4)	# 33156-33159
    sprite('ce611_04', 4)	# 33160-33163
    Unknown21011(120)
    SFX_3('hit_l_fast')
    sprite('ce611_05', 32767)	# 33164-65930
    label(110)
    sprite('ce000_00', 1)	# 65931-65931
    if (not SLOT_53):
        if random_(2, 0, 50):
            sendToLabel(0)
        else:
            sendToLabel(10)
    sprite('ce000_00', 1)	# 65932-65932
    Unknown2053(0)
    Unknown2034(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ce000_00', 6)	# 65933-65938
    sprite('ce000_01', 6)	# 65939-65944
    sprite('ce000_02', 6)	# 65945-65950
    sprite('ce000_03', 6)	# 65951-65956
    sprite('ce000_04', 6)	# 65957-65962
    sprite('ce000_05', 6)	# 65963-65968
    sprite('ce000_06', 6)	# 65969-65974
    sprite('ce000_07', 6)	# 65975-65980
    sprite('ce000_08', 6)	# 65981-65986
    sprite('ce000_09', 6)	# 65987-65992
    gotoLabel(111)
    label(112)
    sprite('ce610_00', 4)	# 65993-65996
    Unknown2004(1, 0)
    sprite('ce610_01', 4)	# 65997-66000
    sprite('ce610_02', 4)	# 66001-66004
    SFX_1('pce701bpt')
    sprite('ce610_03', 4)	# 66005-66008
    sprite('ce321_08', 4)	# 66009-66012
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(2000)
    sendToLabelUpon(2, 113)
    SFX_3('runjump_stone_light')
    sprite('ce321_09', 4)	# 66013-66016
    sprite('ce321_10', 4)	# 66017-66020
    sprite('ce321_11', 4)	# 66021-66024
    sprite('ce321_12', 4)	# 66025-66028
    sprite('ce321_13', 4)	# 66029-66032
    sprite('ce321_14', 32767)	# 66033-98799
    loopRest()
    label(113)
    sprite('ce321_15', 4)	# 98800-98803
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    SFX_3('walk_stone_light')
    sprite('ce321_16', 9)	# 98804-98812
    sprite('ce321_17', 3)	# 98813-98815
    sprite('ce321_18', 3)	# 98816-98818
    sprite('ce321_19', 3)	# 98819-98821
    sprite('ce610_04', 6)	# 98822-98827
    sprite('ce610_05', 6)	# 98828-98833
    sprite('ce610_06', 6)	# 98834-98839
    sprite('ce610_07', 6)	# 98840-98845
    sprite('ce610_08', 6)	# 98846-98851
    SFX_3('cloth_l')
    Unknown23018(1)
    label(114)
    sprite('ce610_06', 6)	# 98852-98857
    sprite('ce610_07', 6)	# 98858-98863
    sprite('ce610_08', 6)	# 98864-98869
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(114)
    label(120)
    sprite('ce000_00', 1)	# 98870-98870

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ce000_00', 6)	# 98871-98876
    sprite('ce000_01', 6)	# 98877-98882
    sprite('ce000_02', 6)	# 98883-98888
    sprite('ce000_03', 6)	# 98889-98894
    sprite('ce000_04', 6)	# 98895-98900
    sprite('ce000_05', 6)	# 98901-98906
    sprite('ce000_06', 6)	# 98907-98912
    sprite('ce000_07', 6)	# 98913-98918
    sprite('ce000_08', 6)	# 98919-98924
    sprite('ce000_09', 6)	# 98925-98930
    gotoLabel(121)
    label(122)
    sprite('ce610_00', 4)	# 98931-98934
    Unknown2004(1, 0)
    sprite('ce610_01', 4)	# 98935-98938
    sprite('ce610_02', 4)	# 98939-98942
    sprite('ce610_03', 4)	# 98943-98946
    sprite('ce321_08', 4)	# 98947-98950
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(2000)
    sendToLabelUpon(2, 123)
    SFX_3('runjump_stone_light')
    sprite('ce321_09', 4)	# 98951-98954
    sprite('ce321_10', 4)	# 98955-98958
    sprite('ce321_11', 4)	# 98959-98962
    sprite('ce321_12', 4)	# 98963-98966
    sprite('ce321_13', 4)	# 98967-98970
    sprite('ce321_14', 32767)	# 98971-131737
    loopRest()
    label(123)
    sprite('ce321_15', 4)	# 131738-131741
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    SFX_3('walk_stone_light')
    sprite('ce321_16', 9)	# 131742-131750
    sprite('ce321_17', 3)	# 131751-131753
    sprite('ce321_18', 3)	# 131754-131756
    sprite('ce321_19', 3)	# 131757-131759
    sprite('ce610_04', 6)	# 131760-131765
    SFX_1('pce701baz')
    sprite('ce610_05', 6)	# 131766-131771
    sprite('ce610_06', 6)	# 131772-131777
    sprite('ce610_07', 6)	# 131778-131783
    sprite('ce610_08', 6)	# 131784-131789
    SFX_3('cloth_l')
    Unknown21011(120)
    label(124)
    sprite('ce610_06', 6)	# 131790-131795
    sprite('ce610_07', 6)	# 131796-131801
    sprite('ce610_08', 6)	# 131802-131807
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(124)
    label(130)
    sprite('ce000_00', 1)	# 131808-131808

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ce000_00', 6)	# 131809-131814
    sprite('ce000_01', 6)	# 131815-131820
    sprite('ce000_02', 6)	# 131821-131826
    sprite('ce000_03', 6)	# 131827-131832
    sprite('ce000_04', 6)	# 131833-131838
    sprite('ce000_05', 6)	# 131839-131844
    sprite('ce000_06', 6)	# 131845-131850
    sprite('ce000_07', 6)	# 131851-131856
    sprite('ce000_08', 6)	# 131857-131862
    sprite('ce000_09', 6)	# 131863-131868
    gotoLabel(131)
    label(132)
    sprite('ce001_01', 6)	# 131869-131874
    SFX_1('pce701pbc')
    sprite('ce001_02', 6)	# 131875-131880
    sprite('ce001_03', 6)	# 131881-131886
    sprite('ce001_04', 6)	# 131887-131892
    sprite('ce001_05', 135)	# 131893-132027
    sprite('ce001_00', 6)	# 132028-132033
    sprite('ce611_00', 4)	# 132034-132037
    sprite('ce611_01', 4)	# 132038-132041
    sprite('ce611_02', 4)	# 132042-132045
    sprite('ce611_03', 4)	# 132046-132049
    sprite('ce611_04', 4)	# 132050-132053
    SFX_3('hit_l_fast')
    sprite('ce611_05', 32767)	# 132054-164820
    Unknown21011(120)
    label(140)
    sprite('ce000_00', 1)	# 164821-164821
    Unknown2034(0)
    Unknown2053(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ce000_00', 6)	# 164822-164827
    sprite('ce000_01', 6)	# 164828-164833
    sprite('ce000_02', 6)	# 164834-164839
    sprite('ce000_03', 6)	# 164840-164845
    sprite('ce000_04', 6)	# 164846-164851
    sprite('ce000_05', 6)	# 164852-164857
    sprite('ce000_06', 6)	# 164858-164863
    sprite('ce000_07', 6)	# 164864-164869
    sprite('ce000_08', 6)	# 164870-164875
    sprite('ce000_09', 6)	# 164876-164881
    gotoLabel(141)
    label(142)
    sprite('ce611_00', 4)	# 164882-164885
    sprite('ce611_01', 4)	# 164886-164889
    SFX_1('pce701pyo')
    sprite('ce611_02', 4)	# 164890-164893
    sprite('ce611_03', 4)	# 164894-164897
    sprite('ce611_04', 4)	# 164898-164901
    SFX_3('hit_l_fast')
    label(143)
    sprite('ce611_05', 1)	# 164902-164902
    if SLOT_97:
        _gotolabel(143)
    sprite('ce611_05', 32767)	# 164903-197669
    Unknown21011(30)
    label(150)
    sprite('ce610_00', 4)	# 197670-197673
    Unknown2004(1, 0)
    sprite('ce610_01', 4)	# 197674-197677
    sprite('ce610_02', 4)	# 197678-197681
    SFX_1('pce700pyu')
    sprite('ce610_03', 4)	# 197682-197685
    sprite('ce321_08', 4)	# 197686-197689
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(2000)
    sendToLabelUpon(2, 153)
    SFX_3('runjump_stone_light')
    sprite('ce321_09', 4)	# 197690-197693
    sprite('ce321_10', 4)	# 197694-197697
    sprite('ce321_11', 4)	# 197698-197701
    sprite('ce321_12', 4)	# 197702-197705
    sprite('ce321_13', 4)	# 197706-197709
    sprite('ce321_14', 32767)	# 197710-230476
    loopRest()
    label(153)
    sprite('ce321_15', 4)	# 230477-230480
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    SFX_3('walk_stone_light')
    sprite('ce321_16', 9)	# 230481-230489
    sprite('ce321_17', 3)	# 230490-230492
    sprite('ce321_18', 3)	# 230493-230495
    sprite('ce321_19', 3)	# 230496-230498
    sprite('ce610_04', 6)	# 230499-230504
    sprite('ce610_05', 6)	# 230505-230510
    sprite('ce610_06', 6)	# 230511-230516
    sprite('ce610_07', 6)	# 230517-230522
    sprite('ce610_08', 6)	# 230523-230528
    SFX_3('cloth_l')
    label(154)
    sprite('ce610_06', 6)	# 230529-230534
    sprite('ce610_07', 6)	# 230535-230540
    sprite('ce610_08', 6)	# 230541-230546
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(154)
    sprite('ce610_06', 1)	# 230547-230547
    Unknown21007(24, 40)
    Unknown21011(280)
    label(155)
    sprite('ce610_06', 6)	# 230548-230553
    sprite('ce610_07', 6)	# 230554-230559
    sprite('ce610_08', 6)	# 230560-230565
    SFX_3('cloth_l')
    gotoLabel(155)
    label(160)
    sprite('ce610_00', 4)	# 230566-230569
    Unknown2004(1, 0)
    sprite('ce610_01', 4)	# 230570-230573
    sprite('ce610_02', 4)	# 230574-230577
    SFX_1('pce700uwa')
    sprite('ce610_03', 4)	# 230578-230581
    sprite('ce321_08', 4)	# 230582-230585
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(2000)
    sendToLabelUpon(2, 163)
    SFX_3('runjump_stone_light')
    sprite('ce321_09', 4)	# 230586-230589
    sprite('ce321_10', 4)	# 230590-230593
    sprite('ce321_11', 4)	# 230594-230597
    sprite('ce321_12', 4)	# 230598-230601
    sprite('ce321_13', 4)	# 230602-230605
    sprite('ce321_14', 32767)	# 230606-263372
    loopRest()
    label(163)
    sprite('ce321_15', 4)	# 263373-263376
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    SFX_3('walk_stone_light')
    sprite('ce321_16', 9)	# 263377-263385
    sprite('ce321_17', 3)	# 263386-263388
    sprite('ce321_18', 3)	# 263389-263391
    sprite('ce321_19', 3)	# 263392-263394
    sprite('ce610_04', 6)	# 263395-263400
    sprite('ce610_05', 6)	# 263401-263406
    sprite('ce610_06', 6)	# 263407-263412
    sprite('ce610_07', 6)	# 263413-263418
    sprite('ce610_08', 6)	# 263419-263424
    SFX_3('cloth_l')
    label(164)
    sprite('ce610_06', 6)	# 263425-263430
    sprite('ce610_07', 6)	# 263431-263436
    sprite('ce610_08', 6)	# 263437-263442
    SFX_3('cloth_l')
    loopRest()
    if SLOT_97:
        _gotolabel(164)
    sprite('ce610_06', 6)	# 263443-263448
    sprite('ce610_07', 6)	# 263449-263454
    sprite('ce610_08', 6)	# 263455-263460
    sprite('ce610_06', 6)	# 263461-263466
    sprite('ce610_07', 6)	# 263467-263472
    sprite('ce610_08', 6)	# 263473-263478
    Unknown21007(24, 40)
    Unknown21011(360)
    label(165)
    sprite('ce610_06', 6)	# 263479-263484
    sprite('ce610_07', 6)	# 263485-263490
    sprite('ce610_08', 6)	# 263491-263496
    SFX_3('cloth_l')
    gotoLabel(165)
    label(170)
    sprite('ce000_00', 1)	# 263497-263497

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ce000_00', 6)	# 263498-263503
    sprite('ce000_01', 6)	# 263504-263509
    sprite('ce000_02', 6)	# 263510-263515
    sprite('ce000_03', 6)	# 263516-263521
    sprite('ce000_04', 6)	# 263522-263527
    sprite('ce000_05', 6)	# 263528-263533
    sprite('ce000_06', 6)	# 263534-263539
    sprite('ce000_07', 6)	# 263540-263545
    sprite('ce000_08', 6)	# 263546-263551
    sprite('ce000_09', 6)	# 263552-263557
    gotoLabel(171)
    label(172)
    sprite('ce610_00', 4)	# 263558-263561
    Unknown2004(1, 0)
    sprite('ce610_01', 4)	# 263562-263565
    sprite('ce610_02', 4)	# 263566-263569
    sprite('ce610_03', 4)	# 263570-263573
    sprite('ce321_08', 4)	# 263574-263577
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(2000)
    sendToLabelUpon(2, 173)
    SFX_3('runjump_stone_light')
    sprite('ce321_09', 4)	# 263578-263581
    sprite('ce321_10', 4)	# 263582-263585
    sprite('ce321_11', 4)	# 263586-263589
    sprite('ce321_12', 4)	# 263590-263593
    sprite('ce321_13', 4)	# 263594-263597
    sprite('ce321_14', 32767)	# 263598-296364
    loopRest()
    label(173)
    sprite('ce321_15', 4)	# 296365-296368
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    SFX_3('walk_stone_light')
    sprite('ce321_16', 9)	# 296369-296377
    sprite('ce321_17', 3)	# 296378-296380
    sprite('ce321_18', 3)	# 296381-296383
    sprite('ce321_19', 3)	# 296384-296386
    sprite('ce610_04', 6)	# 296387-296392
    SFX_1('pce701ryn')
    sprite('ce610_05', 6)	# 296393-296398
    sprite('ce610_06', 6)	# 296399-296404
    sprite('ce610_07', 6)	# 296405-296410
    sprite('ce610_08', 6)	# 296411-296416
    SFX_3('cloth_l')
    Unknown23018(1)
    label(174)
    sprite('ce610_06', 6)	# 296417-296422
    sprite('ce610_07', 6)	# 296423-296428
    sprite('ce610_08', 6)	# 296429-296434
    SFX_3('cloth_l')
    loopRest()
    gotoLabel(174)
    label(180)
    sprite('ce001_01', 6)	# 296435-296440
    SFX_1('pce700umi')
    sprite('ce001_02', 6)	# 296441-296446
    sprite('ce001_03', 6)	# 296447-296452
    sprite('ce001_04', 6)	# 296453-296458
    sprite('ce001_05', 90)	# 296459-296548
    sprite('ce001_00', 6)	# 296549-296554
    sprite('ce611_00', 4)	# 296555-296558
    sprite('ce611_01', 4)	# 296559-296562
    sprite('ce611_02', 4)	# 296563-296566
    sprite('ce611_03', 4)	# 296567-296570
    sprite('ce611_04', 4)	# 296571-296574
    Unknown21011(270)
    SFX_3('hit_l_fast')
    sprite('ce611_05', 60)	# 296575-296634
    sprite('ce611_05', 32767)	# 296635-329401
    Unknown21007(24, 40)
    loopRest()
    label(190)
    sprite('ce001_01', 6)	# 329402-329407
    SFX_1('pce700bma')
    sprite('ce001_02', 6)	# 329408-329413
    sprite('ce001_03', 6)	# 329414-329419
    sprite('ce001_04', 6)	# 329420-329425
    sprite('ce001_05', 200)	# 329426-329625
    sprite('ce001_00', 6)	# 329626-329631
    sprite('ce611_00', 4)	# 329632-329635
    sprite('ce611_01', 4)	# 329636-329639
    sprite('ce611_02', 4)	# 329640-329643
    sprite('ce611_03', 4)	# 329644-329647
    sprite('ce611_04', 4)	# 329648-329651
    SFX_3('hit_l_fast')
    label(191)
    sprite('ce611_05', 1)	# 329652-329652
    if SLOT_97:
        _gotolabel(191)
    sprite('ce611_05', 10)	# 329653-329662
    sprite('ce611_05', 32767)	# 329663-362429
    Unknown21007(24, 40)
    Unknown21011(240)
    label(200)
    sprite('ce000_00', 1)	# 362430-362430

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ce000_00', 6)	# 362431-362436
    sprite('ce000_01', 6)	# 362437-362442
    sprite('ce000_02', 6)	# 362443-362448
    sprite('ce000_03', 6)	# 362449-362454
    sprite('ce000_04', 6)	# 362455-362460
    sprite('ce000_05', 6)	# 362461-362466
    sprite('ce000_06', 6)	# 362467-362472
    sprite('ce000_07', 6)	# 362473-362478
    sprite('ce000_08', 6)	# 362479-362484
    sprite('ce000_09', 6)	# 362485-362490
    gotoLabel(201)
    label(202)
    sprite('ce611_00', 4)	# 362491-362494
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
    sprite('ce611_01', 4)	# 362495-362498
    SFX_1('pce701pak')
    sprite('ce611_02', 4)	# 362499-362502
    sprite('ce611_03', 4)	# 362503-362506
    sprite('ce611_04', 4)	# 362507-362510
    SFX_3('hit_l_fast')
    label(203)
    sprite('ce611_05', 1)	# 362511-362511
    if SLOT_97:
        _gotolabel(203)
    sprite('ce611_05', 25)	# 362512-362536
    sprite('ce611_05', 32767)	# 362537-395303
    Unknown21007(24, 40)
    Unknown21011(180)

@State
def CmnActLose():
    sprite('ce070_00', 6)	# 1-6
    if random_(2, 0, 50):
        SFX_1('pce405_0')
    else:
        SFX_1('pce405_1')
    Unknown23018(1)
    sprite('ce070_01', 6)	# 7-12
    sprite('ce070_02', 2)	# 13-14
    Unknown8000(100, 1, 1)
    sprite('ce070_03', 32767)	# 15-32781
