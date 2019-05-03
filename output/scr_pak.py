@Subroutine
def PreInit():
    Unknown12019('70616b00000000000000000000000000')

@Subroutine
def MatchInit():
    Health(18000)
    JumpYVelocity(30000)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(3)
    Unknown13039(0)
    Unknown2049(1)
    Move_Register('66Ducking', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Unknown14020(1)
    Unknown14004(1)
    Unknown14013('Ducking')
    Move_EndRegister()
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x1)
    Move_Input_(INPUT_PRESS_A)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14013('NmlAtk5A3rd')
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk2ARenda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 250000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14015(-3000, 550000, -150000, 50000, 1500, 80)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14015(-3000, 250000, 5000, 350000, 500, 80)
    Unknown15021(4000)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(20000, 430000, -219000, -66000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(0, 280000, -100000, 150000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(20000, 250000, -50000, 100000, 200, 80)
    Unknown15021(4000)
    Move_EndRegister()
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5B')
    Unknown14015(20000, 250000, -100000, 100000, 1500, 80)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3083)
    Unknown14015(20000, 250000, -100000, 100000, 1500, 80)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B2nd', 0x22)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5A')
    Unknown14015(20000, 250000, -50000, 100000, 200, 80)
    Unknown15021(4000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(150000, 550000, -500000, 100000, 750, 80)
    Unknown15021(800)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('BoomerangHookA', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-3000, 550000, -150000, 50000, 1500, 80)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('SonicPunchA', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-3000, 550000, -150000, 50000, 1500, 80)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('BoomerangHookB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-3000, 550000, -150000, 50000, 1500, 80)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('SonicPunchB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-3000, 550000, -150000, 50000, 1500, 80)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('Ducking', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Unknown14015(-3000, 550000, -150000, 50000, 50, 50)
    Move_EndRegister()
    Move_Register('RushLegSweep', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_C)
    Unknown15009()
    Unknown14015(0, 280000, -100000, 150000, 1100, 30)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('BoomerangHookA_Air', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('BoomerangHookA')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('SonicPunchB_Air', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('SonicPunchB')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('Ducking_Air', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xda)
    Unknown14013('Ducking')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('RushCrushAttack_Air', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('CmnActCrushAttack')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('RushLegSweep_Air', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('RushLegSweep')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('CycloneThrow', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('CycloneBackThrow', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('CorkScrewA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 550000, -100000, 150000, 300, 10)
    Move_EndRegister()
    Move_Register('CorkScrewB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(2000)
    Unknown14015(0, 550000, -100000, 150000, 200, 10)
    Move_EndRegister()
    Move_Register('CorkScrewEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(2000)
    Unknown14015(0, 550000, -100000, 150000, 150, 10)
    Move_EndRegister()
    Move_Register('AssaultDiveLandA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(200)
    Unknown14015(0, 400000, -250000, 10000, 150, 10)
    Move_EndRegister()
    Move_Register('AssaultDiveLandB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(200)
    Unknown14015(0, 400000, -250000, 10000, 150, 10)
    Move_EndRegister()
    Move_Register('AssaultDiveLandEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(200)
    Unknown14015(0, 400000, -250000, 10000, 150, 10)
    Move_EndRegister()
    Move_Register('AssaultDiveAirA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(200)
    Unknown14015(0, 400000, -500000, 10000, 100, 10)
    Move_EndRegister()
    Move_Register('AssaultDiveAirB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(200)
    Unknown14015(0, 400000, -500000, 10000, 100, 10)
    Move_EndRegister()
    Move_Register('AssaultDiveAirEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(200)
    Unknown14015(0, 400000, -500000, 10000, 100, 10)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 210000, -123000, 285000, 250, 0)
    Move_EndRegister()
    Move_Register('CycloneUpper', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 210000, -113000, 92000, 500, 0)
    Move_EndRegister()
    Move_Register('CycloneUpperSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 210000, -113000, 92000, 500, 0)
    Move_EndRegister()
    Move_Register('Mahajiodain', 0x68)
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
    Unknown14015(279000, 1879000, -91000, 280000, 50, 50)
    Move_EndRegister()
    Move_Register('MahajiodainSP', 0x68)
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
    Unknown14015(279000, 1879000, -91000, 280000, 50, 50)
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
    Unknown15024('NmlAtk2A', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5B', 'BoomerangHookA', 10000000)
    Unknown15024('BoomerangHookA', 'SonicPunchA', 10000000)
    Unknown15024('BoomerangHookA', 'RushLegSweep', 10000000)
    Unknown15024('BoomerangHookA', 'CorkScrewA', 10000000)
    Unknown15024('BoomerangHookA', 'CorkScrewB', 10000000)
    Unknown15024('BoomerangHookA', 'CorkScrewEX', 10000000)
    Unknown15024('NmlAtk5B', 'SonicPunchB', 10000000)
    Unknown15024('SonicPunchB', 'BoomerangHookB', 10000000)
    Unknown15024('BoomerangHookB', 'SonicPunchA', 10000000)
    Unknown15024('RushLegSweep', 'CorkScrewA', 10000000)
    Unknown15024('RushLegSweep', 'CycloneUpper', 10000000)
    Unknown15024('RushLegSweep', 'CycloneUpperSP', 10000000)
    Unknown15024('ThrowExe', 'SonicPunchB', 10000000)
    Unknown15024('ThrowExe', 'BoomerangHookA', 10000000)
    Unknown12018(0, 'ak060_00')
    Unknown12018(1, 'ak060_01')
    Unknown12018(2, 'ak060_02')
    Unknown12018(3, 'ak060_03')
    Unknown12018(4, 'ak060_04')
    Unknown12018(5, 'ak060_05')
    Unknown12018(6, 'ak060_06')
    Unknown12018(7, 'ak041_02')
    Unknown12018(8, 'ak040_02')
    Unknown12018(9, 'ak045_02')
    Unknown12018(10, 'ak060_00')
    Unknown12018(11, 'ak060_01')
    Unknown12018(12, 'ak060_03')
    Unknown12018(13, 'ak060_05')
    Unknown12018(14, 'ak060_07')
    Unknown12018(15, 'ak125_00')
    Unknown12018(16, 'ak050_00')
    Unknown12018(17, 'ak052_00')
    Unknown12018(18, 'ak054_00')
    Unknown12018(19, 'ak000_00')
    Unknown12018(20, 'ak000_00')
    Unknown12018(25, 'ak063_00')
    Unknown12018(26, 'ak063_01')
    Unknown12018(27, 'ak063_02')
    Unknown12018(28, 'ak063_05')
    Unknown12018(29, 'ak060_12')
    Unknown12018(24, 'ak072_03')
    Unknown7010(0, 'pak000')
    Unknown7010(1, 'pak001')
    Unknown7010(2, 'pak002')
    Unknown7010(3, 'pak003')
    Unknown7010(4, 'pak004')
    Unknown7010(5, 'pak005')
    Unknown7010(6, 'pak006')
    Unknown7010(7, 'pak007')
    Unknown7010(8, 'pak008')
    Unknown7010(9, 'pak009')
    Unknown7010(10, 'pak010')
    Unknown7010(15, 'pak011')
    Unknown7010(16, 'pak012')
    Unknown7010(17, 'pak013')
    Unknown7010(18, 'pak014')
    Unknown7010(19, 'pak015')
    Unknown7010(20, 'pak016')
    Unknown7010(21, 'pak017')
    Unknown7010(22, 'pak018')
    Unknown7010(23, 'pak019')
    Unknown7010(24, 'pak020')
    Unknown7010(25, 'pak021')
    Unknown7010(28, 'pak022')
    Unknown7010(29, 'pak023')
    Unknown7010(30, 'pak024')
    Unknown7010(31, 'pak025')
    Unknown7010(32, 'pak026')
    Unknown7010(33, 'pak027')
    Unknown7010(34, 'pak028')
    Unknown7010(35, 'pak029')
    Unknown7010(36, 'pak030')
    Unknown7010(37, 'pak031')
    Unknown7010(39, 'pak032')
    Unknown7010(42, 'pak033')
    Unknown7010(43, 'pak034')
    Unknown7010(44, 'pak035')
    Unknown7010(45, 'pak036')
    Unknown7010(46, 'pak037')
    Unknown7010(47, 'pak038')
    Unknown7010(48, 'pak039')
    Unknown7010(49, 'pak040')
    Unknown7010(50, 'pak041')
    Unknown7010(52, 'pak042')
    Unknown7010(53, 'pak043')
    Unknown7010(54, 'pak100_0')
    Unknown7010(55, 'pak100_1')
    Unknown7010(56, 'pak100_2')
    Unknown7010(63, 'pak101_0')
    Unknown7010(64, 'pak101_1')
    Unknown7010(65, 'pak101_2')
    Unknown7010(57, 'pak102_0')
    Unknown7010(58, 'pak102_1')
    Unknown7010(59, 'pak102_2')
    Unknown7010(66, 'pak103_0')
    Unknown7010(67, 'pak103_1')
    Unknown7010(68, 'pak103_2')
    Unknown7010(60, 'pak104_0')
    Unknown7010(61, 'pak104_1')
    Unknown7010(62, 'pak104_2')
    Unknown7010(69, 'pak105_0')
    Unknown7010(70, 'pak105_1')
    Unknown7010(71, 'pak105_2')
    Unknown7010(72, 'pak150')
    Unknown7010(73, 'pak151')
    Unknown7010(74, 'pak152')
    Unknown7010(85, 'pak153')
    Unknown7010(87, 'pak154')
    Unknown7010(88, 'pak155')
    Unknown7010(96, 'pak161_0')
    Unknown7010(97, 'pak161_1')
    Unknown7010(92, 'pak162_0')
    Unknown7010(93, 'pak162_1')
    Unknown7010(98, 'pak163_0')
    Unknown7010(99, 'pak163_1')
    Unknown7010(100, 'pak164_0')
    Unknown7010(101, 'pak164_1')
    Unknown7010(105, 'pak165_0')
    Unknown7010(106, 'pak165_1')
    Unknown7010(102, 'pak166_0')
    Unknown7010(103, 'pak166_1')
    Unknown7010(90, 'pak167_0')
    Unknown7010(91, 'pak167_1')
    Unknown7010(107, 'pak168_0')
    Unknown7010(108, 'pak168_1')
    Unknown7010(110, 'pak169_0')
    Unknown7010(111, 'pak169_1')
    Unknown7010(94, 'pak400_0')
    Unknown7010(95, 'pak400_1')
    Unknown30036('50414b5f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown23003(0, 1, 11, 1, 5, 0, 0, 0)
    Unknown23005(0, 1)
    Unknown23004(0, 1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('020000004379636c6f6e6555707065720000000000000000000000000000000000000000')
    Unknown12059('030000004379636c6f6e6555707065725350000000000000000000000000000000000000')
    Unknown12059('040000004d6168616a696f6461696e000000000000000000000000000000000000000000')
    Unknown12059('050000004d6168616a696f6461696e535000000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if (SLOT_59 >= 5):
            if SLOT_7:
                if SLOT_5:
                    SLOT_5 = (SLOT_5 + (-1))
                else:
                    Unknown3031()
                    SLOT_5 = (SLOT_5 + 10)
                    Unknown3032()
                    Unknown23118(6291456)
                    Unknown23119(8388608, 8, -1)

@Subroutine
def OnActionBegin():
    if (SLOT_59 >= 5):
        Unknown23118(6291456)
        Unknown23119(8388608, 8, -1)
        SLOT_7 = 1
    else:
        SLOT_7 = 0

@Subroutine
def OnFinalize():
    SLOT_60 = SLOT_59
    SLOT_59 = 0
    SLOT_31 = 0
    Unknown23004(0, 1)

@Subroutine
def CycloneLvIcon():
    Unknown23004(0, 0)
    if (not SLOT_93):
        SLOT_59 = SLOT_60
        SLOT_60 = 0
    if (SLOT_59 == 1):
        SLOT_31 = 1
        Unknown3029(1)
        Unknown3069(1)
        Unknown3071(3)
        Unknown3070(3)
        Unknown3072('46000000320000003200000032000000')
        Unknown3073('1e000000320000003200000032000000')
        Unknown3074('00000000000000004000000080000000')
        Unknown3075('00000000000000002000000040000000')
        Unknown3076(1000)
        Unknown3077(1000)
    if (SLOT_59 == 2):
        SLOT_31 = 2
        Unknown3029(1)
        Unknown3069(1)
        Unknown3071(4)
        Unknown3070(3)
        Unknown3072('46000000320000003200000032000000')
        Unknown3073('1e000000320000003200000032000000')
        Unknown3074('00000000400000000000000080000000')
        Unknown3075('00000000200000000000000040000000')
        Unknown3076(1000)
        Unknown3077(1000)
    if (SLOT_59 == 3):
        SLOT_31 = 3
        Unknown3029(1)
        Unknown3069(1)
        Unknown3071(4)
        Unknown3070(2)
        Unknown3072('46000000320000003200000032000000')
        Unknown3073('1e000000320000003200000032000000')
        Unknown3074('00000000800000000000000080000000')
        Unknown3075('00000000400000000000000080000000')
        Unknown3076(1000)
        Unknown3077(1000)
    if (SLOT_59 >= 4):
        SLOT_31 = 4
        Unknown3029(1)
        Unknown3069(1)
        Unknown3071(6)
        Unknown3070(2)
        Unknown3072('46000000320000003200000032000000')
        Unknown3073('1e000000320000003200000032000000')
        Unknown3074('00000000b80000000000000000000000')
        Unknown3075('00000000400000000000000040000000')
        Unknown3076(1000)
        Unknown3077(1000)
    if (SLOT_59 >= 5):
        SLOT_31 = 5
        Unknown3029(1)
        Unknown3069(1)
        Unknown3071(8)
        Unknown3070(1)
        Unknown3072('46000000320000003200000032000000')
        Unknown3073('1e000000320000003200000032000000')
        Unknown3074('00000000ff0000000000000000000000')
        Unknown3075('00000000400000000000000000000000')
        Unknown3076(1000)
        Unknown3077(1000)

@Subroutine
def CycloneSkillDeriveInput():
    Unknown14070('CmnActCrushAttack')
    Unknown14070('BoomerangHookA')
    Unknown14070('SonicPunchB')
    Unknown14070('Ducking')
    Unknown14070('RushLegSweep')
    Unknown14070('CycloneThrow')
    Unknown14070('CycloneBackThrow')

@Subroutine
def CycloneSkillDeriveTiming():
    Unknown14072('CmnActCrushAttack')
    Unknown14072('BoomerangHookA')
    Unknown14072('SonicPunchB')
    Unknown14072('Ducking')
    Unknown14072('RushLegSweep')
    Unknown14072('CycloneThrow')
    Unknown14072('CycloneBackThrow')

@Subroutine
def CycloneSkillDeriveClear():
    Unknown14074('CmnActCrushAttack')
    Unknown14074('BoomerangHookA')
    Unknown14074('SonicPunchB')
    Unknown14074('Ducking')
    Unknown14074('RushLegSweep')
    Unknown14074('CycloneThrow')
    Unknown14074('CycloneBackThrow')

@Subroutine
def CycloneSkillDeriveInput_Air():
    Unknown14070('BoomerangHookA_Air')
    Unknown14070('SonicPunchB_Air')
    Unknown14070('Ducking_Air')
    Unknown14070('RushLegSweep_Air')
    Unknown14070('RushCrushAttack_Air')

@Subroutine
def CycloneSkillDeriveTiming_Air():
    Unknown14072('BoomerangHookA_Air')
    Unknown14072('SonicPunchB_Air')
    Unknown14072('Ducking_Air')
    Unknown14072('RushLegSweep_Air')
    Unknown14072('RushCrushAttack_Air')

@Subroutine
def CycloneSkillDeriveClear_Air():
    Unknown14074('BoomerangHookA_Air')
    Unknown14074('SonicPunchB_Air')
    Unknown14074('Ducking_Air')
    Unknown14074('RushLegSweep_Air')
    Unknown14074('RushCrushAttack_Air')

@Subroutine
def CycloneSkillFlexChain():
    WhiffCancel('CmnActCrushAttack')
    WhiffCancel('BoomerangHookA')
    WhiffCancel('SonicPunchB')
    WhiffCancel('Ducking')
    WhiffCancel('RushLegSweep')
    WhiffCancel('CycloneThrow')
    WhiffCancel('CycloneBackThrow')

@Subroutine
def SpecialSkillDeriveInput():
    Unknown14070('CmnActInvincibleAttack')
    Unknown14070('CorkScrewA')
    Unknown14070('CorkScrewB')
    Unknown14070('CorkScrewEX')
    Unknown14070('AssaultDiveLandA')
    Unknown14070('AssaultDiveLandB')
    Unknown14070('AssaultDiveLandEX')

@Subroutine
def SpecialSkillDeriveTiming():
    Unknown14072('CmnActInvincibleAttack')
    Unknown14072('CorkScrewA')
    Unknown14072('CorkScrewB')
    Unknown14072('CorkScrewEX')
    Unknown14072('AssaultDiveLandA')
    Unknown14072('AssaultDiveLandB')
    Unknown14072('AssaultDiveLandEX')

@Subroutine
def SpecialSkillDeriveClear():
    Unknown14074('CmnActInvincibleAttack')
    Unknown14074('CorkScrewA')
    Unknown14074('CorkScrewB')
    Unknown14074('CorkScrewEX')
    Unknown14074('AssaultDiveLandA')
    Unknown14074('AssaultDiveLandB')
    Unknown14074('AssaultDiveLandEX')

@Subroutine
def SpecialSkillFlexChain():
    WhiffCancel('CmnActInvincibleAttack')
    WhiffCancel('CorkScrewA')
    WhiffCancel('CorkScrewB')
    WhiffCancel('CorkScrewEX')
    WhiffCancel('AssaultDiveLandA')
    WhiffCancel('AssaultDiveLandB')
    WhiffCancel('AssaultDiveLandEX')

@Subroutine
def DistortionSkillDeriveInput():
    Unknown14070('CycloneUpper')
    Unknown14070('CycloneUpperSP')
    Unknown14070('Mahajiodain')
    Unknown14070('MahajiodainSP')
    Unknown14070('AstralHeat')

@Subroutine
def DistortionSkillDeriveTiming():
    Unknown14072('CycloneUpper')
    Unknown14072('CycloneUpperSP')
    Unknown14072('Mahajiodain')
    Unknown14072('MahajiodainSP')
    Unknown14072('AstralHeat')

@Subroutine
def DistortionSkillDeriveClear():
    Unknown14074('CycloneUpper')
    Unknown14074('CycloneUpperSP')
    Unknown14074('Mahajiodain')
    Unknown14074('MahajiodainSP')
    Unknown14074('AstralHeat')

@Subroutine
def DistortionSkillFlexChain():
    WhiffCancel('CycloneUpper')
    WhiffCancel('CycloneUpperSP')
    WhiffCancel('Mahajiodain')
    WhiffCancel('MahajiodainSP')
    WhiffCancel('AstralHeat')

@Subroutine
def DuckDoNotBeginCancel():
    if Unknown23145('Ducking'):
        Unknown30068(1)

@Subroutine
def DiveDoNotBeginCancel():
    if 
    if (not 
    if (not 
    if (not 
    if (not 
    if (not Unknown23145('AssaultDiveLandA')):
        Unknown23145('AssaultDiveLandB')):
        Unknown23145('AssaultDiveLandEX')):
        Unknown23145('AssaultDiveAirA')):
        Unknown23145('AssaultDiveAirB')):
        Unknown23145('AssaultDiveAirEX'):
        Unknown30068(1)

@State
def CmnActStand():
    label(0)
    sprite('ak000_00', 6)	# 1-6
    sprite('ak000_01', 6)	# 7-12
    sprite('ak000_02', 6)	# 13-18
    sprite('ak000_03', 6)	# 19-24
    sprite('ak000_04', 6)	# 25-30
    sprite('ak000_05', 6)	# 31-36
    sprite('ak000_06', 6)	# 37-42
    sprite('ak000_07', 6)	# 43-48
    sprite('ak000_08', 6)	# 49-54
    sprite('ak000_09', 6)	# 55-60
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('ak001_00', 6)	# 61-66
    SLOT_88 = 960
    SFX_1('pak000')
    sprite('ak001_01', 6)	# 67-72
    sprite('ak001_02', 6)	# 73-78
    sprite('ak001_03', 4)	# 79-82
    sprite('ak001_04', 4)	# 83-86
    sprite('ak001_06', 6)	# 87-92
    sprite('ak001_04', 6)	# 93-98
    sprite('ak001_06', 8)	# 99-106
    sprite('ak001_01', 8)	# 107-114
    sprite('ak001_00', 8)	# 115-122
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ak003_00', 4)	# 1-4
    sprite('ak003_01', 4)	# 5-8
    sprite('ak003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('ak010_00', 4)	# 1-4
    sprite('ak010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ak010_02', 6)	# 1-6
    sprite('ak010_03', 6)	# 7-12
    sprite('ak010_04', 6)	# 13-18
    sprite('ak010_05', 6)	# 19-24
    sprite('ak010_06', 6)	# 25-30
    sprite('ak010_07', 6)	# 31-36
    sprite('ak010_08', 6)	# 37-42
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ak013_00', 4)	# 1-4
    sprite('ak013_01', 4)	# 5-8
    sprite('ak013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('ak010_01', 4)	# 1-4
    sprite('ak010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ak010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ak020_00', 4)	# 1-4
    sprite('ak020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ak020_02', 3)	# 1-3
    sprite('ak020_03', 3)	# 4-6
    sprite('ak020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ak020_05', 3)	# 1-3
    sprite('ak020_06', 3)	# 4-6
    label(0)
    sprite('ak020_07', 4)	# 7-10
    sprite('ak020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ak010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('ak408_07', 3)	# 1-3
    sprite('ak408_08', 3)	# 4-6
    sprite('ak408_09', 32767)	# 7-32773
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('ak408_08', 3)	# 1-3
    sprite('ak408_07', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('ak030_00', 5)	# 1-5
    sprite('ak030_01', 5)	# 6-10
    label(0)
    sprite('ak030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ak030_03', 5)	# 16-20
    sprite('ak030_04', 5)	# 21-25
    sprite('ak030_05', 5)	# 26-30
    sprite('ak030_06', 5)	# 31-35
    sprite('ak030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ak030_08', 5)	# 41-45
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('ak031_00', 6)	# 1-6
    sprite('ak031_01', 6)	# 7-12
    label(0)
    sprite('ak031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ak031_03', 6)	# 19-24
    sprite('ak031_04', 6)	# 25-30
    sprite('ak031_05', 6)	# 31-36
    sprite('ak031_06', 6)	# 37-42
    sprite('ak031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ak031_08', 6)	# 49-54
    sprite('ak031_09', 6)	# 55-60
    sprite('ak031_10', 6)	# 61-66
    sprite('ak031_11', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('ak030_00', 3)	# 1-3
    sprite('ak030_01', 2)	# 4-5
    sprite('ak032_00', 2)	# 6-7
    label(0)
    sprite('ak032_01', 4)	# 8-11
    sprite('ak032_02', 4)	# 12-15
    sprite('ak032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('ak032_04', 4)	# 20-23
    sprite('ak032_05', 4)	# 24-27
    sprite('ak032_06', 4)	# 28-31
    sprite('ak032_07', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('ak032_08', 4)	# 36-39
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ak032_09', 4)	# 1-4
    sprite('ak032_10', 4)	# 5-8

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
    sprite('ak033_00', 2)	# 1-2
    sprite('ak033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('ak033_02', 3)	# 6-8
    label(0)
    sprite('ak033_01', 3)	# 9-11
    sprite('ak033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak033_03', 3)	# 15-17
    setInvincible(0)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 18-20

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirTurn():
    sprite('ak025_00', 1)	# 1-1
    sprite('ak025_01', 2)	# 2-3
    sprite('ak025_02', 1)	# 4-4

@State
def CmnActAirFDash():
    sprite('ak035_00', 3)	# 1-3
    label(0)
    sprite('ak035_01', 3)	# 4-6
    sprite('ak035_02', 3)	# 7-9
    sprite('ak035_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ak033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('ak033_02', 3)	# 4-6
    sprite('ak033_01', 3)	# 7-9
    sprite('ak033_02', 3)	# 10-12
    sprite('ak033_01', 3)	# 13-15
    sprite('ak033_02', 3)	# 16-18
    sprite('ak033_01', 3)	# 19-21
    sprite('ak033_02', 3)	# 22-24
    sprite('ak020_05', 3)	# 25-27
    sprite('ak020_06', 3)	# 28-30
    label(0)
    sprite('ak020_07', 4)	# 31-34
    sprite('ak020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ak050_00', 1)	# 1-1
    sprite('ak050_01', 1)	# 2-2
    sprite('ak050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ak050_01', 1)	# 1-1
    sprite('ak050_02', 1)	# 2-2
    sprite('ak050_01', 2)	# 3-4
    sprite('ak050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ak050_02', 1)	# 1-1
    sprite('ak050_03', 1)	# 2-2
    sprite('ak050_02', 2)	# 3-4
    sprite('ak050_01', 2)	# 5-6
    sprite('ak050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ak050_03', 1)	# 1-1
    sprite('ak050_04', 1)	# 2-2
    sprite('ak050_03', 2)	# 3-4
    sprite('ak050_02', 2)	# 5-6
    sprite('ak050_01', 2)	# 7-8
    sprite('ak050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ak050_04', 1)	# 1-1
    sprite('ak050_04', 1)	# 2-2
    sprite('ak050_04', 2)	# 3-4
    sprite('ak050_03', 2)	# 5-6
    sprite('ak050_02', 2)	# 7-8
    sprite('ak050_01', 2)	# 9-10
    sprite('ak050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ak052_00', 1)	# 1-1
    sprite('ak052_01', 1)	# 2-2
    sprite('ak052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ak052_01', 1)	# 1-1
    sprite('ak052_02', 1)	# 2-2
    sprite('ak052_01', 2)	# 3-4
    sprite('ak052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ak052_02', 1)	# 1-1
    sprite('ak052_03', 1)	# 2-2
    sprite('ak052_02', 2)	# 3-4
    sprite('ak052_01', 2)	# 5-6
    sprite('ak052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ak052_03', 1)	# 1-1
    sprite('ak052_04', 1)	# 2-2
    sprite('ak052_03', 2)	# 3-4
    sprite('ak052_02', 2)	# 5-6
    sprite('ak052_01', 2)	# 7-8
    sprite('ak052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ak052_04', 1)	# 1-1
    sprite('ak052_04', 1)	# 2-2
    sprite('ak052_04', 2)	# 3-4
    sprite('ak052_03', 2)	# 5-6
    sprite('ak052_02', 2)	# 7-8
    sprite('ak052_01', 2)	# 9-10
    sprite('ak052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ak054_00', 1)	# 1-1
    sprite('ak054_01', 1)	# 2-2
    sprite('ak054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ak054_01', 1)	# 1-1
    sprite('ak054_02', 1)	# 2-2
    sprite('ak054_01', 2)	# 3-4
    sprite('ak054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ak054_02', 1)	# 1-1
    sprite('ak054_03', 1)	# 2-2
    sprite('ak054_02', 2)	# 3-4
    sprite('ak054_01', 2)	# 5-6
    sprite('ak054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ak054_03', 1)	# 1-1
    sprite('ak054_04', 1)	# 2-2
    sprite('ak054_03', 2)	# 3-4
    sprite('ak054_02', 2)	# 5-6
    sprite('ak054_01', 2)	# 7-8
    sprite('ak054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ak054_04', 1)	# 1-1
    sprite('ak054_04', 1)	# 2-2
    sprite('ak054_04', 2)	# 3-4
    sprite('ak054_03', 2)	# 5-6
    sprite('ak054_02', 2)	# 7-8
    sprite('ak054_01', 2)	# 9-10
    sprite('ak054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ak060_00', 4)	# 1-4
    label(0)
    sprite('ak060_01', 4)	# 5-8
    sprite('ak060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ak060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ak060_04', 8)	# 1-8
    label(1)
    sprite('ak060_05', 4)	# 9-12
    sprite('ak060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('ak060_07', 4)	# 1-4

@State
def CmnActBDownBound():
    sprite('ak060_08', 2)	# 1-2
    sprite('ak060_09', 2)	# 3-4
    sprite('ak060_10', 2)	# 5-6
    sprite('ak060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('ak060_12', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('ak064_00', 6)	# 1-6
    sprite('ak064_01', 6)	# 7-12
    sprite('ak064_02', 6)	# 13-18
    sprite('ak064_03', 6)	# 19-24

@State
def CmnActFDownUpper():
    sprite('ak063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ak063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ak063_03', 3)	# 1-3
    sprite('ak063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ak063_05', 4)	# 1-4

@State
def CmnActFDownBound():
    sprite('ak060_08', 2)	# 1-2
    sprite('ak060_09', 2)	# 3-4
    sprite('ak060_10', 2)	# 5-6
    sprite('ak060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('ak060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ak064_00', 6)	# 1-6
    sprite('ak064_01', 6)	# 7-12
    sprite('ak064_02', 6)	# 13-18
    sprite('ak064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('ak060_00', 4)	# 1-4
    label(0)
    sprite('ak060_01', 4)	# 5-8
    sprite('ak060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ak060_03', 4)	# 1-4

@State
def CmnActVDownDown():
    sprite('ak060_04', 8)	# 1-8
    label(0)
    sprite('ak060_05', 4)	# 9-12
    sprite('ak060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ak060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('ak072_00', 3)	# 1-3
    label(0)
    sprite('ak072_01', 3)	# 4-6
    sprite('ak072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ak074_00', 2)	# 1-2
    sprite('ak074_01', 2)	# 3-4
    sprite('ak074_02', 2)	# 5-6
    sprite('ak074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('ak072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('ak063_00', 4)	# 1-4
    sprite('ak063_01', 4)	# 5-8
    sprite('ak063_02', 4)	# 9-12
    label(0)
    sprite('ak063_03', 4)	# 13-16
    sprite('ak063_04', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('ak082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('ak052_01', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('ak070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('ak070_01', 4)	# 1-4
    sprite('ak070_02', 4)	# 5-8
    sprite('ak070_03', 4)	# 9-12
    sprite('ak070_04', 4)	# 13-16
    sprite('ak070_05', 4)	# 17-20
    sprite('ak070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ak040_03', 2)	# 1-2
    sprite('ak040_02', 2)	# 3-4
    sprite('ak040_01', 2)	# 5-6
    sprite('ak040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('ak020_02', 3)	# 1-3
    sprite('ak020_03', 3)	# 4-6
    sprite('ak020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('ak020_02', 3)	# 1-3
    sprite('ak020_03', 3)	# 4-6
    sprite('ak020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('ak020_02', 3)	# 1-3
    sprite('ak020_03', 3)	# 4-6
    sprite('ak020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('ak112_00', 3)	# 1-3
    sprite('ak112_01', 3)	# 4-6
    sprite('ak112_02', 3)	# 7-9
    sprite('ak112_03', 3)	# 10-12
    sprite('ak112_04', 3)	# 13-15
    sprite('ak112_05', 3)	# 16-18
    sprite('ak020_07', 4)	# 19-22
    sprite('ak020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandF():
    sprite('ak112_00', 3)	# 1-3
    sprite('ak112_01', 3)	# 4-6
    sprite('ak112_02', 3)	# 7-9
    sprite('ak112_03', 3)	# 10-12
    sprite('ak112_04', 3)	# 13-15
    sprite('ak112_05', 3)	# 16-18
    sprite('ak020_07', 4)	# 19-22
    sprite('ak020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('ak112_00', 3)	# 1-3
    sprite('ak112_01', 3)	# 4-6
    sprite('ak112_02', 3)	# 7-9
    sprite('ak112_03', 3)	# 10-12
    sprite('ak112_04', 3)	# 13-15
    sprite('ak112_05', 3)	# 16-18
    sprite('ak020_07', 4)	# 19-22
    sprite('ak020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('ak010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('ak040_00', 3)	# 1-3
    sprite('ak040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ak040_02', 3)	# 1-3
    sprite('ak040_03', 3)	# 4-6
    sprite('ak040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ak040_01', 3)	# 1-3
    sprite('ak040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ak040_05', 1)	# 1-1
    label(0)
    sprite('ak040_02', 3)	# 2-4
    sprite('ak040_03', 3)	# 5-7
    sprite('ak040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ak040_01', 3)	# 1-3
    sprite('ak040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ak040_00', 3)	# 1-3
    sprite('ak040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ak040_02', 3)	# 1-3
    sprite('ak040_03', 3)	# 4-6
    sprite('ak040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ak040_01', 3)	# 1-3
    sprite('ak040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ak040_05', 1)	# 1-1
    label(0)
    sprite('ak040_02', 3)	# 2-4
    sprite('ak040_03', 3)	# 5-7
    sprite('ak040_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ak040_01', 3)	# 1-3
    sprite('ak040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ak043_00', 3)	# 1-3
    sprite('ak043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ak043_02', 3)	# 1-3
    sprite('ak043_03', 3)	# 4-6
    sprite('ak043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ak043_01', 3)	# 1-3
    sprite('ak043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ak043_05', 1)	# 1-1
    label(0)
    sprite('ak043_02', 3)	# 2-4
    sprite('ak043_03', 3)	# 5-7
    sprite('ak043_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ak043_01', 3)	# 1-3
    sprite('ak043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ak045_00', 3)	# 1-3
    sprite('ak045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ak045_02', 3)	# 1-3
    sprite('ak045_03', 3)	# 4-6
    sprite('ak045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ak045_01', 3)	# 1-3
    sprite('ak045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ak045_05', 1)	# 1-1
    label(0)
    sprite('ak045_02', 3)	# 2-4
    sprite('ak045_03', 3)	# 5-7
    sprite('ak045_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ak045_01', 3)	# 1-3
    sprite('ak045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ak040_05', 2)	# 1-2
    sprite('ak040_05', 2)	# 3-4
    sprite('ak040_05', 1)	# 5-5
    Unknown2042(1)
    sprite('ak040_02', 4)	# 6-9
    sprite('ak040_01', 4)	# 10-13
    sprite('ak040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ak043_05', 2)	# 1-2
    sprite('ak043_05', 2)	# 3-4
    sprite('ak043_05', 1)	# 5-5
    Unknown2042(1)
    sprite('ak043_02', 4)	# 6-9
    sprite('ak043_01', 4)	# 10-13
    sprite('ak043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ak045_05', 2)	# 1-2
    sprite('ak045_05', 2)	# 3-4
    sprite('ak045_05', 1)	# 5-5
    Unknown2042(1)
    sprite('ak045_02', 4)	# 6-9
    sprite('ak045_01', 4)	# 10-13
    sprite('ak045_00', 4)	# 14-17

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('ak201_00', 2)	# 1-2
    sprite('ak201_01', 4)	# 3-6
    sprite('ak201_02', 2)	# 7-8
    sprite('ak201_03', 2)	# 9-10	 **attackbox here**
    sprite('ak201_04', 3)	# 11-13
    sprite('ak201_05', 3)	# 14-16
    sprite('ak201_07', 5)	# 17-21
    sprite('ak201_08', 4)	# 22-25
    sprite('ak201_09', 4)	# 26-29

@State
def CmnActAirLockWait():
    sprite('ak045_02', 1)	# 1-1
    sprite('ak045_01', 3)	# 2-4
    sprite('ak045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ak251_04', 8)	# 1-8
    sprite('ak251_05', 4)	# 9-12	 **attackbox here**
    sprite('ak251_06', 6)	# 13-18	 **attackbox here**
    sprite('ak251_07', 4)	# 19-22
    sprite('ak251_08', 4)	# 23-26
    sprite('ak251_09', 3)	# 27-29

@State
def CmnActLandSpin():
    sprite('ak071_00', 2)	# 1-2
    label(0)
    sprite('ak071_01', 2)	# 3-4
    sprite('ak071_02', 2)	# 5-6
    sprite('ak071_03', 2)	# 7-8
    sprite('ak071_04', 2)	# 9-10
    sprite('ak071_05', 2)	# 11-12
    sprite('ak071_06', 2)	# 13-14
    sprite('ak071_07', 2)	# 15-16
    sprite('ak071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ak040_02', 3)	# 1-3
    sprite('ak040_01', 3)	# 4-6
    sprite('ak040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('ak071_00', 2)	# 1-2
    label(0)
    sprite('ak071_01', 2)	# 3-4
    sprite('ak071_02', 2)	# 5-6
    sprite('ak071_03', 2)	# 7-8
    sprite('ak071_04', 2)	# 9-10
    sprite('ak071_05', 2)	# 11-12
    sprite('ak071_06', 2)	# 13-14
    sprite('ak071_07', 2)	# 15-16
    sprite('ak071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('ak124_00', 2)	# 1-2
    label(0)
    sprite('ak124_01', 2)	# 3-4
    sprite('ak124_02', 2)	# 5-6
    sprite('ak124_03', 2)	# 7-8
    sprite('ak124_04', 2)	# 9-10
    sprite('ak124_05', 2)	# 11-12
    sprite('ak124_06', 2)	# 13-14
    sprite('ak124_07', 2)	# 15-16
    sprite('ak124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ak077_02', 4)	# 1-4
    label(0)
    sprite('ak077_03', 3)	# 5-7
    sprite('ak077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ak077_05', 5)	# 1-5
    sprite('ak077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('ak077_02', 4)	# 1-4
    label(0)
    sprite('ak077_03', 3)	# 5-7
    sprite('ak077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ak077_05', 5)	# 1-5
    sprite('ak077_06', 4)	# 6-9

@State
def CmnActBurstBegin():
    label(0)
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ak121_03', 3)	# 1-3
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ak121_07', 3)	# 1-3
    sprite('ak020_04', 3)	# 4-6
    sprite('ak020_05', 3)	# 7-9
    sprite('ak020_06', 3)	# 10-12
    label(0)
    sprite('ak020_07', 4)	# 13-16
    sprite('ak020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstBegin():
    label(0)
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ak121_03', 3)	# 1-3
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ak121_07', 3)	# 1-3
    sprite('ak020_04', 3)	# 4-6
    sprite('ak020_05', 3)	# 7-9
    sprite('ak020_06', 3)	# 10-12
    label(0)
    sprite('ak020_07', 4)	# 13-16
    sprite('ak020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ak121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ak121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('ak121_07', 6)	# 1-6
    sprite('ak010_00', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ak121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ak121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ak121_07', 4)	# 1-4
    sprite('ak020_04', 3)	# 5-7
    sprite('ak020_05', 3)	# 8-10
    sprite('ak020_06', 2)	# 11-12
    label(0)
    sprite('ak020_07', 4)	# 13-16
    sprite('ak020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PAK_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ak121_02', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ak121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('ak121_07', 6)	# 1-6
    sprite('ak010_00', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(28)
    Unknown23148('PAK_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ak121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ak121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ak121_07', 4)	# 1-4
    sprite('ak020_04', 3)	# 5-7
    sprite('ak020_05', 3)	# 8-10
    sprite('ak020_06', 2)	# 11-12
    label(0)
    sprite('ak020_07', 4)	# 13-16
    sprite('ak020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PAK_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('ak121_03', 3)	# 1-3
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ak121_07', 6)	# 1-6
    sprite('ak010_00', 6)	# 7-12

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PAK_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('ak121_00', 2)	# 1-2
    sprite('ak121_01', 2)	# 3-4
    sprite('ak121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('ak121_03', 3)	# 1-3
    label(0)
    sprite('ak121_04', 2)	# 4-5
    sprite('ak121_05', 2)	# 6-7
    sprite('ak121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ak121_07', 4)	# 1-4
    sprite('ak020_04', 3)	# 5-7
    sprite('ak020_05', 3)	# 8-10
    sprite('ak020_06', 2)	# 11-12
    label(0)
    sprite('ak020_07', 4)	# 13-16
    sprite('ak020_08', 4)	# 17-20
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

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
    sprite('null', 25)	# 1-25
    sprite('ak408_00', 4)	# 26-29
    Unknown1086(22)
    teleportRelativeX(-200000)
    teleportRelativeY(2000000)
    physicsYImpulse(-166666)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('ak408_01', 2)	# 30-31
    sprite('ak408_02', 2)	# 32-33
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 34-35
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 36-37	 **attackbox here**
    GFX_0('SpecialAirFistAura', 0)
    loopRest()
    label(0)
    sprite('ak408_05', 2)	# 38-39	 **attackbox here**
    sprite('ak408_04', 2)	# 40-41	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ak408_06', 4)	# 42-45	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    clearUponHandler(2)
    sprite('ak408_06', 2)	# 46-47	 **attackbox here**
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    sprite('ak408_07', 3)	# 48-50
    sprite('ak408_08', 3)	# 51-53
    sprite('ak408_09', 6)	# 54-59
    sprite('ak408_10', 4)	# 60-63

@State
def CmnActChangePartnerQuickIn():
    sprite('ak032_03', 3)	# 1-3
    sprite('ak032_04', 5)	# 4-8
    sprite('ak032_05', 5)	# 9-13
    sprite('ak032_09', 2)	# 14-15
    sprite('ak032_09', 6)	# 16-21
    sprite('ak032_10', 8)	# 22-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ak033_00', 3)	# 1-3
    sprite('ak033_01', 3)	# 4-6
    sprite('ak033_02', 3)	# 7-9
    sprite('ak033_01', 3)	# 10-12
    sprite('ak033_02', 3)	# 13-15
    sprite('ak033_01', 3)	# 16-18
    sprite('ak033_02', 3)	# 19-21
    sprite('ak033_01', 3)	# 22-24
    sprite('ak033_02', 3)	# 25-27
    sprite('ak033_01', 3)	# 28-30
    sprite('ak033_02', 3)	# 31-33
    sprite('ak033_01', 27)	# 34-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('ak033_00', 3)	# 1-3
    label(0)
    sprite('ak033_01', 3)	# 4-6
    sprite('ak033_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak033_03', 3)	# 10-12
    sprite('ak033_04', 3)	# 13-15

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ak000_00', 2)	# 1-2
    sprite('ak001_00', 5)	# 3-7
    sprite('ak001_01', 5)	# 8-12
    sprite('ak001_02', 5)	# 13-17
    sprite('ak001_03', 4)	# 18-21
    sprite('ak001_04', 4)	# 22-25
    sprite('ak001_06', 6)	# 26-31
    sprite('ak001_04', 6)	# 32-37
    sprite('ak001_06', 7)	# 38-44
    sprite('ak001_01', 5)	# 45-49
    sprite('ak001_00', 5)	# 50-54
    sprite('ak403_06', 2)	# 55-56
    sprite('ak403_07', 2)	# 57-58
    sprite('ak403_08', 2)	# 59-60
    sprite('ak403_09', 10)	# 61-70
    GFX_0('SpecialAtemiGood', 0)
    sprite('ak403_10', 4)	# 71-74
    sprite('ak000_00', 22)	# 75-96

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
    sprite('ak020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ak020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ak010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(70)
        Hitstop(9)
        AirUntechableTime(50)
        PushbackX(20000)
        AirPushbackX(60000)
        AirPushbackY(20000)
        Unknown11056(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9178(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(50)

        def upon_11():
            clearUponHandler(11)
            SFX_3('down_steal_m')
            ScreenShake(10000, 5000)
            sendToLabel(1)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ak406_00', 4)	# 1-4
    sprite('ak406_01', 4)	# 5-8
    physicsXImpulse(10000)
    Unknown3029(1)
    sprite('ak406_02', 2)	# 9-10
    Unknown1019(300)
    SFX_3('airbackdash_m')
    sprite('ak406_03', 2)	# 11-12
    Unknown1019(300)
    sprite('ak406_02', 2)	# 13-14
    sprite('ak406_03', 2)	# 15-16
    Unknown1019(60)
    sprite('ak406_04', 3)	# 17-19
    Unknown1019(50)
    sprite('ak404_00', 2)	# 20-21
    sprite('ak404_01', 2)	# 22-23
    sprite('ak404_02', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(80000)
    Unknown8007(100, 1, 1)
    SFX_3('slash_blade_fast')
    GFX_0('SpecialScrewWind', 0)
    GFX_0('SpecialScrewFistAura', 0)
    GFX_0('UltimateUpperSmoke', 100)
    Unknown7007('70616b3230375f3000000000000000006400000070616b3230375f3100000000000000006400000070616b3230375f3200000000000000006400000070616b3230385f30000000000000000064000000')
    sprite('ak404_03', 1)	# 26-26	 **attackbox here**
    sprite('ak404_03', 1)	# 27-27	 **attackbox here**
    label(1)
    sprite('ak404_04', 2)	# 28-29	 **attackbox here**
    sprite('ak404_05', 3)	# 30-32
    Recovery()
    Unknown1019(80)
    Unknown8006(100, 1, 1)
    sprite('ak404_06', 3)	# 33-35
    Unknown1019(0)
    Unknown8006(100, 1, 1)
    sprite('ak404_07', 3)	# 36-38
    Unknown8006(100, 1, 1)
    sprite('ak404_08', 4)	# 39-42
    sprite('ak404_09', 4)	# 43-46
    sprite('ak404_10', 3)	# 47-49
    sprite('ak404_11', 5)	# 50-54
    sprite('ak404_12', 5)	# 55-59
    SFX_3('ak002')
    sprite('ak404_13', 8)	# 60-67
    sprite('ak000_00', 3)	# 68-70

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AttackP1(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(35000)
        AirUntechableTime(60)

        def upon_11():
            clearUponHandler(11)
            SFX_3('grip_hugs')
        Unknown2004(1, 0)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ak409_00', 3)	# 1-3
    sprite('ak409_01', 2)	# 4-5
    physicsXImpulse(40000)
    GFX_0('SpecialQuakeSmoke', 100)
    Unknown8007(100, 1, 1)
    SFX_3('airbackdash_m')
    SFX_3('cloth_m')
    sprite('ak409_03', 2)	# 6-7
    Unknown1019(80)
    sprite('ak409_04ex', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    Unknown1019(50)
    SFX_3('hit_h_middle')
    GFX_0('akef_dashupper', 100)
    Unknown7007('70616b3231365f3000000000000000006400000070616b3231365f3200000000000000006400000070616b3231375f3100000000000000006400000070616b3231375f32000000000000000064000000')
    sprite('ak409_04ex', 4)	# 10-13	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_1('akef_dashupper_smoke', 100)
    sprite('ak409_05', 6)	# 14-19
    Recovery()
    sprite('ak409_06', 5)	# 20-24
    sprite('ak409_07', 5)	# 25-29
    sprite('ak409_08', 4)	# 30-33
    sprite('ak000_00', 3)	# 34-36
    teleportRelativeX(-30000)

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(500)
        AttackP1(70)
        Unknown11092(1)
        Hitstop(1)
        PushbackX(1000)
        AirPushbackX(1000)
        AirPushbackY(4000)
        YImpluseBeforeWallbounce(1000)
        Unknown30055('c0d401001e0000001e000000')
        Unknown11057(500)
        AirUntechableTime(50)

        def upon_12():
            SFX_3('damage_hit_h')

        def upon_3():
            if SLOT_51:
                if (SLOT_19 < 350000):
                    clearUponHandler(3)
                    sendToLabel(0)
                    SLOT_51 = 0
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
            Unknown2015(-1)
    sprite('ak032_00', 4)	# 1-4
    Unknown3029(1)
    sprite('ak032_01', 4)	# 5-8
    Unknown7007('70616b3231325f3000000000000000006400000070616b3231325f3200000000000000006400000070616b3231335f3100000000000000006400000070616b3231335f32000000000000000064000000')
    physicsXImpulse(60000)
    SFX_3('airbackdash_m')
    Unknown8007(100, 1, 1)
    sprite('ak032_02', 2)	# 9-10
    SLOT_51 = 1
    sprite('ak032_02', 1)	# 11-11
    sprite('ak032_03', 3)	# 12-14
    label(0)
    sprite('ak400_00', 1)	# 15-15
    clearUponHandler(3)
    Unknown1019(70)
    Unknown3029(0)
    SLOT_52 = 2
    label(1)
    sprite('ak400_00', 1)	# 16-16
    sprite('ak400_01', 1)	# 17-17
    sprite('ak400_02aex', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    GFX_0('SpecialRash00', 100)
    Unknown8006(100, 1, 1)
    sprite('ak203_01', 1)	# 19-19
    GFX_0('SpecialRash01', 100)
    Unknown8006(100, 1, 1)
    sprite('ak203_02', 1)	# 20-20
    GFX_0('SpecialRash02', 100)
    Unknown8006(100, 1, 1)
    sprite('ak203_03aex', 1)	# 21-21	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(0)
    SLOT_52 = (SLOT_52 + (-1))
    Unknown19(2, 2, 52)
    GFX_0('SpecialRash03', 100)
    Unknown8006(100, 1, 1)
    loopRest()
    gotoLabel(1)
    label(2)
    clearUponHandler(10)
    sprite('ak203_04', 3)	# 22-24
    sprite('ak203_06a', 3)	# 25-27	 **attackbox here**
    Unknown23054('616b3230335f303500000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    SFX_3('hit_m_middle')
    Unknown9154(25)
    Hitstop(7)
    PushbackX(15200)
    AirPushbackX(10000)
    AirPushbackY(30000)
    Unknown9095()
    Unknown30055('000000000000000000000000')
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    Unknown11057(1000)
    GFX_0('SpecialRash04', 100)
    GFX_0('SpecialRash05', 100)
    Unknown8006(100, 1, 1)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        SFX_3('down_marble_m')
    sprite('ak203_06a', 7)	# 28-34	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('ak203_06a', 8)	# 35-42	 **attackbox here**
    StartMultihit()
    sprite('ak203_07', 5)	# 43-47
    sprite('ak203_08', 5)	# 48-52
    sprite('ak203_09', 5)	# 53-57
    sprite('ak000_00', 3)	# 58-60

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
    Unknown2036(85, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-260000)
    Unknown1019(4)
    label(0)
    sprite('ak020_07', 4)	# 3-6
    sprite('ak020_08', 4)	# 7-10
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

        def upon_43():
            if (SLOT_48 == 4401):
                setInvincible(0)
    sprite('ak432_00', 3)	# 1-3
    sprite('ak432_00', 1)	# 4-4
    sprite('ak432_01', 4)	# 5-8
    sprite('ak432_02', 4)	# 9-12
    sprite('ak432_03', 4)	# 13-16
    sprite('ak432_04', 4)	# 17-20
    sprite('ak432_05', 4)	# 21-24
    Unknown23029(11, 4322, 0)
    sprite('ak432_06', 36)	# 25-60
    SFX_3('ak050')
    sprite('ak432_07', 4)	# 61-64
    Unknown23118(-6921066)
    Unknown23119(-13495246, 4, -1)
    Unknown4048(45000)
    Unknown4045('706572736f6e615f656e7465725f70330000000000000000000000000000000000000000')
    SFX_3('ak051')
    sprite('ak432_08', 4)	# 65-68
    SFX_0('persona_destroy')
    sprite('ak432_09', 5)	# 69-73
    Unknown7007('70616b3235375f3000000000000000006400000070616b3235375f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 74-78
    sprite('ak432_11', 5)	# 79-83
    sprite('ak432_09', 5)	# 84-88
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 89-93
    sprite('ak432_11', 5)	# 94-98
    sprite('ak432_09', 5)	# 99-103
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 104-108
    sprite('ak432_11', 5)	# 109-113
    sprite('ak432_09', 5)	# 114-118
    SFX_3('cloth_m')
    Unknown23119(-16777216, 8, 1)
    sprite('ak432_10', 5)	# 119-123
    sprite('ak432_11', 5)	# 124-128
    sprite('ak432_09', 5)	# 129-133
    SFX_3('cloth_m')
    sprite('ak432_01', 5)	# 134-138
    sprite('ak432_00', 5)	# 139-143

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4401):
                setInvincible(0)
    sprite('ak432_00', 3)	# 1-3
    sprite('ak432_00', 1)	# 4-4
    sprite('ak432_01', 4)	# 5-8
    sprite('ak432_02', 4)	# 9-12
    sprite('ak432_03', 4)	# 13-16
    sprite('ak432_04', 4)	# 17-20
    sprite('ak432_05', 4)	# 21-24
    Unknown23029(11, 4323, 0)
    sprite('ak432_06', 36)	# 25-60
    SFX_3('ak050')
    sprite('ak432_07', 4)	# 61-64
    Unknown23118(-6921066)
    Unknown23119(-13495246, 4, -1)
    Unknown4048(45000)
    Unknown4045('706572736f6e615f656e7465725f70330000000000000000000000000000000000000000')
    SFX_3('ak051')
    sprite('ak432_08', 4)	# 65-68
    SFX_0('persona_destroy')
    sprite('ak432_09', 5)	# 69-73
    Unknown7007('70616b3235385f3000000000000000006400000070616b3235385f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 74-78
    sprite('ak432_11', 5)	# 79-83
    sprite('ak432_09', 5)	# 84-88
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 89-93
    sprite('ak432_11', 5)	# 94-98
    sprite('ak432_09', 5)	# 99-103
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 104-108
    sprite('ak432_11', 5)	# 109-113
    sprite('ak432_09', 5)	# 114-118
    SFX_3('cloth_m')
    Unknown23119(-16777216, 8, 1)
    sprite('ak432_10', 5)	# 119-123
    sprite('ak432_11', 5)	# 124-128
    sprite('ak432_09', 5)	# 129-133
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 134-138
    sprite('ak432_11', 5)	# 139-143
    sprite('ak432_12', 5)	# 144-148
    sprite('ak432_01', 5)	# 149-153
    sprite('ak432_00', 5)	# 154-158

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

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('ak408_00', 4)	# 121-124
    Unknown1086(22)
    teleportRelativeX(-200000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('ak408_01', 2)	# 125-126
    sprite('ak408_02', 2)	# 127-128
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 129-130
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 131-132	 **attackbox here**
    GFX_0('SpecialAirFistAura', 0)
    loopRest()
    label(1)
    sprite('ak408_05', 2)	# 133-134	 **attackbox here**
    sprite('ak408_04', 2)	# 135-136	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ak408_06', 4)	# 137-140	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    clearUponHandler(2)
    sprite('ak408_06', 2)	# 141-142	 **attackbox here**
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    sprite('ak408_07', 5)	# 143-147
    sprite('ak408_08', 6)	# 148-153
    sprite('ak408_09', 8)	# 154-161
    sprite('ak408_10', 6)	# 162-167

@State
def CmnActChangeReturnAppealBurst():
    sprite('ak064_02', 48)	# 1-48
    sprite('ak064_03', 3)	# 49-51
    sprite('ak010_01', 3)	# 52-54
    sprite('ak010_00', 3)	# 55-57
    sprite('ak000_00', 23)	# 58-80

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(950)
        Unknown11092(1)
        Hitstop(5)
        AirPushbackY(13000)
        PushbackX(5000)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
    sprite('ak203_00', 2)	# 1-2
    sprite('ak203_01', 2)	# 3-4
    sprite('ak203_02', 3)	# 5-7
    sprite('ak203_03', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    Unknown7009(2)
    sprite('ak203_04', 3)	# 11-13
    sprite('ak203_06', 3)	# 14-16	 **attackbox here**
    Unknown23054('616b3230335f303500000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Hitstop(13)
    SFX_3('hit_m_middle')

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5A2nd')
    sprite('ak203_06', 2)	# 17-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ak203_07', 5)	# 19-23
    sprite('ak203_07', 1)	# 24-24
    sprite('ak203_08', 6)	# 25-30
    sprite('ak203_09', 6)	# 31-36

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(950)
        Unknown11092(1)
        AirPushbackY(10000)
        PushbackX(5000)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ak400_03', 4)	# 1-4
    sprite('ak400_04', 3)	# 5-7
    SFX_3('blaze_normal')
    physicsXImpulse(30000)
    sprite('ak400_06ex01', 5)	# 8-12	 **attackbox here**
    Unknown23054('616b3430305f303500000000000000000000000000000000000000000000000003000000')
    Unknown7009(5)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('ak201_02', 3)	# 13-15
    sprite('ak201_03', 2)	# 16-17	 **attackbox here**
    SFX_3('hit_m_fast')
    RefreshMultihit()
    PushbackX(-12000)
    AirPushbackX(-4000)
    AirPushbackY(0)
    Hitstop(9)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5A3rd')
    sprite('ak201_04', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('ak201_05', 3)	# 21-23
    sprite('ak201_07', 5)	# 24-28
    sprite('ak201_08', 4)	# 29-32
    sprite('ak201_09', 4)	# 33-36

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP2(80)
        Unknown11092(1)
        PushbackX(10000)
        YImpluseBeforeWallbounce(1500)
        Hitstop(5)
        JumpCancel_(0)
    sprite('ak202_00', 3)	# 1-3
    sprite('ak202_01', 2)	# 4-5
    physicsXImpulse(80000)
    GFX_1('akef_AAAcombo', 103)
    Unknown8006(100, 1, 1)
    SFX_3('hit_h_fast')
    sprite('ak202_01', 2)	# 6-7
    Unknown2017(0)
    sprite('ak202_02', 2)	# 8-9
    Unknown1019(70)
    Unknown2005()
    Unknown8006(100, 1, 1)
    sprite('ak202_04', 2)	# 10-11	 **attackbox here**
    Unknown23054('616b3230325f303300000000000000000000000000000000000000000000000002000000')
    tag_voice(1, 'pak201_0', 'pak201_2', '', '')
    RefreshMultihit()
    AirPushbackY(4000)
    Unknown1019(0)
    Unknown2017(1)
    sprite('ak202_05', 6)	# 12-17
    physicsXImpulse(60000)
    Unknown2017(0)
    Unknown2018(0, 80)
    GFX_1('akef_AAAcombo', 103)
    Unknown8006(100, 1, 1)
    SFX_3('hit_h_fast')
    sprite('ak202_06', 4)	# 18-21
    Unknown1019(15)
    Unknown2005()
    Unknown8006(100, 1, 1)
    sprite('ak202_08', 2)	# 22-23	 **attackbox here**
    Unknown23054('616b3230325f303700000000000000000000000000000000000000000000000002000000')
    Unknown2018(1, 80)
    tag_voice(0, 'pak202_0', 'pak202_2', '', '')
    RefreshMultihit()
    AirPushbackY(8000)
    Unknown1019(0)
    Unknown2017(1)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        sendToLabel(1)
    loopRest()
    label(0)
    sprite('ak202_09', 4)	# 24-27
    Recovery()
    Unknown2063()
    sprite('ak202_10', 4)	# 28-31
    sprite('ak202_11', 4)	# 32-35
    sprite('ak202_13', 4)	# 36-39
    sprite('ak202_14', 4)	# 40-43
    ExitState()
    label(1)
    sprite('ak202_01', 6)	# 44-49
    physicsXImpulse(60000)
    Unknown2017(0)
    GFX_1('akef_AAAcombo', 103)
    Unknown8006(100, 1, 1)
    SFX_3('hit_h_fast')
    sprite('ak202_02', 4)	# 50-53
    Unknown1019(15)
    Unknown2005()
    Unknown8006(100, 1, 1)
    sprite('ak202_04', 2)	# 54-55	 **attackbox here**
    Unknown23054('616b3230325f303300000000000000000000000000000000000000000000000002000000')
    tag_voice(0, 'pak203_0', 'pak203_2', '', '')
    RefreshMultihit()
    AirPushbackY(4000)
    Unknown1019(0)
    Unknown2017(1)
    sprite('ak202_05', 6)	# 56-61
    physicsXImpulse(60000)
    Unknown2017(0)
    Unknown2018(0, 80)
    GFX_1('akef_AAAcombo', 103)
    Unknown8006(100, 1, 1)
    SFX_3('hit_h_fast')
    sprite('ak202_06', 4)	# 62-65
    Unknown1019(15)
    Unknown2005()
    Unknown8006(100, 1, 1)
    sprite('ak202_08', 2)	# 66-67	 **attackbox here**
    Unknown23054('616b3230325f303700000000000000000000000000000000000000000000000002000000')
    Unknown2018(1, 80)
    tag_voice(0, 'pak204_0', 'pak204_2', '', '')
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirPushbackX(8000)
    AirPushbackY(15000)
    AirUntechableTime(30)
    Unknown1019(0)
    Unknown2017(1)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        HitOrBlockCancel('NmlAtk5A4th')
        JumpCancel_(1)
    loopRest()
    gotoLabel(0)

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 2051):
                sendToLabel(0)
                Unknown13045(0)
                setInvincible(1)
            if (SLOT_48 == 2052):
                Unknown13045(1)
                setInvincible(0)
    sprite('ak205_00', 3)	# 1-3
    sprite('ak205_01', 3)	# 4-6
    Unknown23029(11, 2050, 0)
    sprite('ak205_02', 2)	# 7-8
    GFX_1('persona_enter_ply', 0)
    sprite('ak205_02', 1)	# 9-9
    sprite('ak205_03', 4)	# 10-13
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 14-17
    sprite('ak205_05', 4)	# 18-21
    sprite('ak205_03', 4)	# 22-25
    SFX_3('cloth_l')
    Recovery()
    Unknown2063()
    sprite('ak205_04', 4)	# 26-29
    sprite('ak205_05', 4)	# 30-33
    sprite('ak205_01', 4)	# 34-37
    sprite('ak205_00', 4)	# 38-41
    ExitState()
    label(0)
    sprite('ak205_05', 4)	# 42-45
    Unknown7007('70616b3132335f3100000000000000006400000070616b3132345f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak205_03', 4)	# 46-49
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 50-53
    sprite('ak205_05', 4)	# 54-57
    sprite('ak205_03', 4)	# 58-61
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 62-65
    sprite('ak205_05', 4)	# 66-69
    sprite('ak205_03', 4)	# 70-73
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 74-77
    sprite('ak205_05', 4)	# 78-81
    sprite('ak205_03', 4)	# 82-85
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 86-89
    sprite('ak205_05', 4)	# 90-93
    sprite('ak205_03', 4)	# 94-97
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 98-101
    sprite('ak205_05', 4)	# 102-105
    sprite('ak205_03', 4)	# 106-109
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 110-113
    sprite('ak205_05', 4)	# 114-117
    sprite('ak205_03', 4)	# 118-121
    SFX_3('cloth_l')
    sprite('ak205_04', 4)	# 122-125
    sprite('ak205_05', 4)	# 126-129
    sprite('ak205_01', 4)	# 130-133
    sprite('ak205_00', 4)	# 134-137

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Hitstop(8)
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
    sprite('ak200_02', 3)	# 1-3
    sprite('ak200_02', 2)	# 4-5
    Unknown1051(80)
    sprite('ak200_01', 2)	# 6-7	 **attackbox here**
    Unknown23054('616b3230305f303000000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    SFX_3('hit_l_fast')
    Unknown7009(0)
    sprite('ak200_01', 3)	# 8-10	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ak200_02', 8)	# 11-18

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        PushbackX(-12000)
        AirPushbackX(-4000)
        AirPushbackY(0)
        Hitstop(9)
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ak201_00', 2)	# 1-2
    sprite('ak201_01', 4)	# 3-6
    sprite('ak201_02', 2)	# 7-8
    sprite('ak201_03', 2)	# 9-10	 **attackbox here**
    SFX_3('hit_m_fast')
    RefreshMultihit()
    Unknown7009(1)
    sprite('ak201_04', 3)	# 11-13
    Recovery()
    Unknown2063()
    sprite('ak201_05', 3)	# 14-16
    sprite('ak201_07', 5)	# 17-21
    sprite('ak201_08', 4)	# 22-25
    sprite('ak201_09', 4)	# 26-29

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(500)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(1)
        PushbackX(1000)
        AirPushbackX(1000)
        AirPushbackY(4000)
        YImpluseBeforeWallbounce(1000)
        Unknown30055('c0d401001e0000001e000000')
        Unknown11057(500)
        Unknown9154(23)
        AirUntechableTime(27)
        JumpCancel_(0)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        callSubroutine('CycloneSkillFlexChain')

        def upon_12():
            SFX_3('damage_hit_h')

        def upon_3():
            if SLOT_51:
                if (SLOT_19 < 350000):
                    clearUponHandler(3)
                    sendToLabel(0)
                    SLOT_51 = 0
    sprite('ak032_00', 3)	# 1-3
    sprite('ak032_01', 2)	# 4-5
    Unknown3029(1)
    Unknown7007('70616b3231325f3000000000000000006400000070616b3231325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    physicsXImpulse(60000)
    SFX_3('airbackdash_m')
    Unknown8007(100, 1, 1)
    Unknown23004(0, 0)
    sprite('ak032_02', 2)	# 6-7
    SLOT_51 = 1
    sprite('ak032_03', 2)	# 8-9
    label(0)
    sprite('ak400_00', 1)	# 10-10
    clearUponHandler(3)
    Unknown1019(70)
    Unknown3029(0)
    SLOT_52 = 1

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        SLOT_52 = (SLOT_52 + 1)
        SLOT_59 = (SLOT_59 + 1)
        Unknown2037(1)
    label(1)
    sprite('ak400_00', 1)	# 11-11
    sprite('ak400_01', 1)	# 12-12
    sprite('ak400_02a', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    GFX_0('SpecialRash00', 100)
    Unknown8006(100, 1, 1)
    sprite('ak400_02a', 1)	# 14-14	 **attackbox here**
    if (not SLOT_2):
        sendToLabel(3)
    sprite('ak203_01', 1)	# 15-15
    GFX_0('SpecialRash01', 100)
    Unknown8006(100, 1, 1)
    sprite('ak203_02', 1)	# 16-16
    GFX_0('SpecialRash02', 100)
    Unknown8006(100, 1, 1)
    sprite('ak203_03a', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(0)
    SLOT_52 = (SLOT_52 + (-1))
    GFX_0('SpecialRash03', 100)
    Unknown8006(100, 1, 1)
    loopRest()
    Unknown19(2, 2, 52)
    gotoLabel(1)
    label(2)
    clearUponHandler(10)
    sprite('ak203_04', 3)	# 18-20
    label(3)
    sprite('ak203_06a', 3)	# 21-23	 **attackbox here**
    Unknown23054('616b3230335f303500000000000000000000000000000000000000000000000003000000')
    if SLOT_2:
        RefreshMultihit()
    else:
        StartMultihit()
    SFX_3('hit_m_middle')
    Unknown9154(21)
    Hitstop(7)
    PushbackX(15200)
    AirPushbackX(8000)
    AirPushbackY(17000)
    Unknown9095()
    Unknown30055('000000000000000000000000')
    AirHitstunAnimation(9)
    Unknown11057(1000)
    GFX_0('SpecialRash04', 100)
    GFX_0('SpecialRash05', 100)
    Unknown8006(100, 1, 1)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        SLOT_58 = 1
        SFX_3('down_marble_m')
        JumpCancel_(1)
        callSubroutine('CycloneSkillDeriveInput')
    sprite('ak203_06a', 1)	# 24-24	 **attackbox here**
    Unknown23183('616b3230335f3036610000000000000000000000000000000000000000000000030000000200000002000000')
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ak203_06a', 8)	# 25-32	 **attackbox here**
    StartMultihit()
    if SLOT_58:
        callSubroutine('CycloneSkillDeriveTiming')
    if SLOT_2:
        WhiffCancelEnable(1)
        JumpCancel_(1)
    sprite('ak203_07', 3)	# 33-35
    callSubroutine('CycloneSkillDeriveClear')
    WhiffCancelEnable(0)
    sprite('ak203_08', 5)	# 36-40
    sprite('ak203_09', 6)	# 41-46

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Hitstop(7)
        HitOrBlockCancel('NmlAtk2ARenda')
        WhiffCancel('NmlAtk2ARenda')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ak230_03', 2)	# 1-2
    sprite('ak230_00', 2)	# 3-4	 **attackbox here**
    StartMultihit()
    sprite('ak230_00', 1)	# 5-5	 **attackbox here**
    StartMultihit()
    Unknown1051(80)
    sprite('ak230_01', 2)	# 6-7	 **attackbox here**
    Unknown23054('616b3233305f303000000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    SFX_3('hit_l_fast')
    Unknown7009(3)
    sprite('ak230_01', 3)	# 8-10	 **attackbox here**
    StartMultihit()
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ak230_02', 4)	# 11-14
    sprite('ak230_03', 4)	# 15-18

@State
def NmlAtk2ARenda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Hitstop(7)
        HitOrBlockCancel('NmlAtk2ARenda')
        WhiffCancel('NmlAtk2ARenda')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ak230_03', 2)	# 1-2
    sprite('ak230_00', 2)	# 3-4	 **attackbox here**
    StartMultihit()
    sprite('ak230_00', 1)	# 5-5	 **attackbox here**
    StartMultihit()
    Unknown1051(80)
    sprite('ak230_01', 2)	# 6-7	 **attackbox here**
    Unknown23054('616b3233305f303000000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    SFX_3('hit_l_fast')
    Unknown7009(3)
    sprite('ak230_01', 3)	# 8-10	 **attackbox here**
    StartMultihit()
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('ak230_02', 4)	# 11-14
    sprite('ak230_03', 4)	# 15-18

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        Hitstop(15)
        AirUntechableTime(21)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        Unknown28(8, 'CmnActStand')
    sprite('ak231_00', 4)	# 1-4
    sprite('ak231_01', 1)	# 5-5
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ak231_02', 1)	# 6-6
    SFX_3('hit_h_middle')
    sprite('ak231_04', 3)	# 7-9	 **attackbox here**
    Unknown23054('616b3233315f303300000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Unknown18009(0)
    Unknown7007('70616b3130365f3000000000000000006400000070616b3130365f3100000000000000006400000070616b3130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak231_04', 3)	# 10-12	 **attackbox here**
    StartMultihit()
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ak231_05', 3)	# 13-15
    SFX_3('cloth_m')
    sprite('ak231_06', 3)	# 16-18
    sprite('ak231_04', 3)	# 19-21	 **attackbox here**
    StartMultihit()
    sprite('ak231_05', 3)	# 22-24
    sprite('ak231_06', 3)	# 25-27
    sprite('ak231_07', 3)	# 28-30
    sprite('ak231_08', 3)	# 31-33
    sprite('ak231_10', 3)	# 34-36

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirUntechableTime(40)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        PushbackX(15000)
        AirPushbackX(-1000)
        AirPushbackY(12000)
    sprite('ak211_00', 2)	# 1-2
    sprite('ak211_00', 1)	# 3-3
    sprite('ak211_01', 4)	# 4-7
    sprite('ak211_02', 1)	# 8-8
    sprite('ak211_02', 2)	# 9-10
    sprite('ak211_03', 2)	# 11-12
    SFX_3('hit_m_fast')
    sprite('ak211_05', 5)	# 13-17	 **attackbox here**
    Unknown23054('616b3231315f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    physicsXImpulse(0)
    Unknown7007('70616b3130375f3000000000000000006400000070616b3130375f3100000000000000006400000070616b3130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak211_05', 5)	# 18-22	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ak211_07', 5)	# 23-27
    sprite('ak211_08', 5)	# 28-32
    sprite('ak211_09', 5)	# 33-37

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Hitstop(8)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ak250_02', 3)	# 1-3
    sprite('ak250_00', 3)	# 4-6	 **attackbox here**
    Unknown23027()
    sprite('ak250_01', 2)	# 7-8	 **attackbox here**
    Unknown23054('616b3235305f303000000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    SFX_3('hit_l_fast')
    Unknown7009(3)
    sprite('ak250_01', 5)	# 9-13	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ak250_02', 6)	# 14-19

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(900)
        AirPushbackY(2000)
        AttackP2(90)
        AirUntechableTime(24)
        Hitstop(9)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B2nd')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ak251_00', 3)	# 1-3
    sprite('ak251_01', 3)	# 4-6
    sprite('ak251_02', 2)	# 7-8
    sprite('ak251_03', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    Unknown7009(5)
    sprite('ak251_04', 3)	# 12-14
    sprite('ak251_05', 3)	# 15-17	 **attackbox here**
    AttackLevel_(2)
    RefreshMultihit()
    AirPushbackX(10000)
    Unknown9083()
    SFX_3('hit_m_middle')
    sprite('ak251_06', 3)	# 18-20	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ak251_07', 3)	# 21-23
    sprite('ak251_08', 3)	# 24-26
    sprite('ak251_09', 3)	# 27-29
    sprite('ak251_10', 3)	# 30-32

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_STATE_END():
            if (not SLOT_2):
                Unknown1018()
                Unknown1038()
                setGravity(2500)
        JumpCancel_(0)
        Unknown14082(1)
    sprite('ak254_00', 3)	# 1-3
    sprite('ak254_01', 1)	# 4-4
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown23029(11, 2540, 0)
    Unknown7007('70616b3132305f3000000000000000003200000070616b3132305f3200000000000000003200000070616b3132315f3000000000000000003200000070616b3132345f30000000000000000064000000')
    sprite('ak254_01', 3)	# 5-7
    sprite('ak254_02', 4)	# 8-11
    GFX_1('persona_enter_ply', 0)
    Unknown22004(5, 5)
    sprite('ak254_03', 4)	# 12-15
    SFX_3('cloth_m')
    sprite('ak254_04', 4)	# 16-19
    sprite('ak254_05', 4)	# 20-23
    sprite('ak254_03', 4)	# 24-27
    sprite('ak254_04', 4)	# 28-31
    Recovery()
    Unknown2063()
    sprite('ak254_05', 4)	# 32-35
    sprite('ak254_03', 4)	# 36-39
    Unknown2037(1)
    Unknown1018()
    Unknown1038()
    setGravity(2500)
    sprite('ak254_04', 4)	# 40-43
    sprite('ak254_05', 4)	# 44-47
    sprite('ak254_06', 4)	# 48-51
    sprite('ak254_04', 4)	# 52-55
    sprite('ak254_05', 4)	# 56-59

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('ak204_00', 4)	# 1-4
    sprite('ak204_01', 1)	# 5-5
    Unknown23029(11, 2040, 0)
    tag_voice(1, 'pak156_0', 'pak156_1', 'pak124_0', 'pak124_0')
    sprite('ak204_01', 3)	# 6-8
    sprite('ak204_02', 4)	# 9-12
    GFX_1('persona_enter_ply', 0)
    sprite('ak204_03', 5)	# 13-17
    SFX_3('cloth_m')
    sprite('ak204_04', 4)	# 18-21
    sprite('ak204_04ex01', 1)	# 22-22	 **attackbox here**
    sprite('ak204_05ex01', 2)	# 23-24	 **attackbox here**
    sprite('ak204_05', 3)	# 25-27
    sprite('ak204_03', 5)	# 28-32
    sprite('ak204_04', 5)	# 33-37
    sprite('ak204_05', 5)	# 38-42
    sprite('ak204_06', 6)	# 43-48

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
    sprite('ak406_00', 3)	# 2-4
    sprite('ak406_01', 4)	# 5-8
    physicsXImpulse(1500)
    Unknown3029(1)
    sprite('ak406_02', 2)	# 9-10
    Unknown1019(300)
    SFX_3('airbackdash_m')
    sprite('ak406_03', 2)	# 11-12
    Unknown1019(300)
    sprite('ak406_02', 2)	# 13-14
    sprite('ak406_03', 2)	# 15-16
    Unknown1019(60)
    sprite('ak406_04', 3)	# 17-19
    Unknown1019(50)
    sprite('ak405_00', 1)	# 20-20
    sprite('ak405_01', 2)	# 21-22
    sprite('ak405_02', 3)	# 23-25
    sprite('ak405_03', 2)	# 26-27
    physicsXImpulse(0)
    SFX_3('slash_sword_middle')
    GFX_0('SpecialQuakeSmoke', 100)
    ScreenShake(0, 5000)
    sprite('ak405_04', 2)	# 28-29
    GFX_0('SpecialBodyBlowFirst', 100)
    sprite('ak405_05', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialBodyBlowMain', 100)
    tag_voice(0, 'pak157_0', 'pak157_1', 'pak157_0', 'pak157_1')
    sprite('ak405_06', 2)	# 33-34
    sprite('ak405_07', 2)	# 35-36
    sprite('ak405_08', 2)	# 37-38
    sprite('ak405_06', 2)	# 39-40
    sprite('ak405_07', 2)	# 41-42
    sprite('ak405_09', 2)	# 43-44
    sprite('ak405_11', 3)	# 45-47
    sprite('ak405_12', 3)	# 48-50
    sprite('ak001_00', 6)	# 51-56
    sprite('ak001_01', 6)	# 57-62
    sprite('ak001_02', 6)	# 63-68
    sprite('ak001_03', 4)	# 69-72
    sprite('ak001_04', 4)	# 73-76
    sprite('ak001_06', 6)	# 77-82
    sprite('ak001_04', 6)	# 83-88
    sprite('ak001_06', 8)	# 89-96
    sprite('ak001_01', 8)	# 97-104
    sprite('ak001_00', 8)	# 105-112
    label(0)
    sprite('ak000_00', 6)	# 113-118
    sprite('ak000_01', 6)	# 119-124
    sprite('ak000_02', 6)	# 125-130
    sprite('ak000_03', 6)	# 131-136
    sprite('ak000_04', 6)	# 137-142
    sprite('ak000_05', 6)	# 143-148
    sprite('ak000_06', 6)	# 149-154
    sprite('ak000_07', 6)	# 155-160
    sprite('ak000_08', 6)	# 161-166
    sprite('ak000_09', 6)	# 167-172
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 173-173

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        Unknown2004(1, 0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ak409_00', 4)	# 1-4
    sprite('ak409_01', 4)	# 5-8
    GFX_0('SpecialQuakeSmoke', 100)
    Unknown8007(100, 1, 1)
    SFX_3('airbackdash_m')
    SFX_3('cloth_m')
    sprite('ak409_03', 2)	# 9-10
    Unknown1019(20)
    sprite('ak409_03', 2)	# 11-12
    Unknown1019(50)
    sprite('ak409_04', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    Unknown1019(50)
    SFX_3('hit_h_middle')
    GFX_0('akef_dashupper', 100)
    sprite('ak409_04', 4)	# 15-18	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_1('akef_dashupper_smoke', 100)
    sprite('ak407_00', 4)	# 19-22
    label(0)
    sprite('ak407_01', 4)	# 23-26
    Unknown3029(1)
    sprite('ak407_02', 2)	# 27-28
    sprite('ak407_02', 2)	# 29-30
    sprite('ak407_03', 3)	# 31-33
    SFX_3('cloth_m')
    sprite('ak407_04', 4)	# 34-37
    sprite('ak407_05', 4)	# 38-41
    sprite('ak407_06', 4)	# 42-45
    sprite('ak407_08', 4)	# 46-49
    sprite('ak407_09', 4)	# 50-53
    sprite('ak407_10', 4)	# 54-57
    sprite('ak407_11', 4)	# 58-61
    sprite('ak407_12', 4)	# 62-65
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 66-66

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('ak407_00', 4)	# 1-4
    Unknown3029(1)
    sprite('ak407_04', 3)	# 5-7
    Unknown3032()
    Unknown3001(150)
    Unknown3004(-20)
    SFX_3('cloth_m')
    physicsXImpulse(-10000)
    sprite('ak407_05', 1)	# 8-8
    Unknown1019(200)
    sprite('ak407_05', 3)	# 9-11
    sprite('ak404_00', 3)	# 12-14
    sprite('ak404_00', 3)	# 15-17
    Unknown3004(30)
    Unknown3029(0)
    sprite('ak404_01', 2)	# 18-19
    sprite('ak404_02', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(250000)
    Unknown8006(100, 1, 1)
    SFX_3('slash_blade_fast')
    GFX_0('SpecialScrewWind', 0)
    GFX_0('SpecialScrewFistAura', 0)
    GFX_0('UltimateUpperSmoke', 100)
    tag_voice(0, 'pak158_0', 'pak158_1', 'pak158_0', 'pak158_1')
    sprite('ak404_02', 1)	# 21-21	 **attackbox here**
    Unknown1019(30)
    sprite('ak404_03', 2)	# 22-23	 **attackbox here**
    Unknown1019(30)
    sprite('ak404_04', 2)	# 24-25	 **attackbox here**
    Unknown1019(30)
    sprite('ak404_05', 3)	# 26-28
    Unknown1019(30)
    Unknown8006(100, 1, 1)
    sprite('ak404_06', 3)	# 29-31
    Unknown1019(0)
    Unknown8006(100, 1, 1)
    sprite('ak404_07', 3)	# 32-34
    Unknown8006(100, 1, 1)
    sprite('ak404_08', 5)	# 35-39
    sprite('ak404_09', 5)	# 40-44
    sprite('ak404_10', 3)	# 45-47
    sprite('ak404_11', 4)	# 48-51
    sprite('ak404_12', 4)	# 52-55
    SFX_3('ak002')
    sprite('ak404_13', 5)	# 56-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown23027()
        sendToLabelUpon(2, 1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 26-26
    Unknown1086(22)
    teleportRelativeX(-500000)
    Unknown1007(1000000)
    Unknown1084(1)
    setGravity(0)
    sprite('ak408_00', 3)	# 27-29
    SLOT_13 = SLOT_20
    SLOT_13 = (SLOT_13 * (-1))
    YAccel(8)
    sprite('ak408_01', 2)	# 30-31
    sprite('ak408_02', 2)	# 32-33
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 34-35
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    physicsXImpulse(50000)
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 36-37	 **attackbox here**
    GFX_0('SpecialAirFistAura', 0)
    loopRest()
    label(0)
    sprite('ak408_05', 2)	# 38-39	 **attackbox here**
    sprite('ak408_04', 2)	# 40-41	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak408_06', 2)	# 42-43	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    sprite('ak408_06', 2)	# 44-45	 **attackbox here**
    RefreshMultihit()
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    sprite('ak408_07', 2)	# 46-47
    sprite('ak408_07', 2)	# 48-49
    sprite('ak408_08', 2)	# 50-51
    sprite('ak408_09', 3)	# 52-54
    sprite('ak408_10', 3)	# 55-57
    sprite('ak010_00', 2)	# 58-59
    sprite('ak000_00', 6)	# 60-65
    sprite('ak000_01', 6)	# 66-71
    sprite('ak000_02', 6)	# 72-77
    sprite('ak000_03', 6)	# 78-83
    sprite('ak000_04', 6)	# 84-89
    sprite('ak000_05', 6)	# 90-95
    sprite('ak000_06', 6)	# 96-101
    sprite('ak000_07', 6)	# 102-107
    sprite('ak000_08', 6)	# 108-113
    sprite('ak000_09', 6)	# 114-119

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('ak405_00', 2)	# 1-2
    sprite('ak405_01', 2)	# 3-4
    sprite('ak405_02', 3)	# 5-7
    sprite('ak405_03', 2)	# 8-9
    SFX_3('slash_sword_middle')
    GFX_0('SpecialQuakeSmoke', 100)
    ScreenShake(0, 5000)
    sprite('ak405_04', 2)	# 10-11
    GFX_0('SpecialBodyBlowFirst', 100)
    sprite('ak405_05', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialBodyBlowMain', 100)
    sprite('ak405_06', 2)	# 15-16
    sprite('ak405_07', 2)	# 17-18
    sprite('ak405_08', 2)	# 19-20
    sprite('ak405_09', 2)	# 21-22
    sprite('ak405_11', 3)	# 23-25
    sprite('ak405_12', 3)	# 26-28
    sprite('ak407_00', 3)	# 29-31
    sprite('ak407_00', 1)	# 32-32
    label(0)
    sprite('ak407_01', 4)	# 33-36
    Unknown3029(1)
    sprite('ak407_02', 2)	# 37-38
    sprite('ak407_02', 2)	# 39-40
    sprite('ak407_03', 3)	# 41-43
    SFX_3('cloth_m')
    sprite('ak407_04', 4)	# 44-47
    sprite('ak407_05', 4)	# 48-51
    sprite('ak407_06', 4)	# 52-55
    sprite('ak407_08', 4)	# 56-59
    sprite('ak407_09', 4)	# 60-63
    sprite('ak407_10', 4)	# 64-67
    sprite('ak407_11', 4)	# 68-71
    sprite('ak407_12', 4)	# 72-75
    loopRest()
    gotoLabel(0)

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ak407_00', 4)	# 1-4
    Unknown3029(1)
    sprite('ak407_04', 3)	# 5-7
    Unknown3032()
    Unknown3001(150)
    Unknown3004(-20)
    SFX_3('cloth_m')
    physicsXImpulse(-10000)
    sprite('ak407_05', 1)	# 8-8
    Unknown1019(200)
    sprite('ak407_05', 3)	# 9-11
    sprite('ak404_00', 3)	# 12-14
    sprite('ak404_00', 3)	# 15-17
    Unknown3004(30)
    Unknown3029(0)
    sprite('ak404_01', 2)	# 18-19
    sprite('ak404_02', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(250000)
    Unknown8006(100, 1, 1)
    SFX_3('slash_blade_fast')
    GFX_0('SpecialScrewWind', 0)
    GFX_0('SpecialScrewFistAura', 0)
    GFX_0('UltimateUpperSmoke', 100)
    sprite('ak404_02', 1)	# 21-21	 **attackbox here**
    Unknown1019(30)
    sprite('ak404_03', 2)	# 22-23	 **attackbox here**
    Unknown1019(30)
    sprite('ak404_04', 2)	# 24-25	 **attackbox here**
    Unknown1019(30)
    sprite('ak404_05', 3)	# 26-28
    Unknown1019(30)
    Unknown8006(100, 1, 1)
    sprite('ak404_06', 3)	# 29-31
    Unknown1019(0)
    Unknown8006(100, 1, 1)
    sprite('ak404_07', 3)	# 32-34
    Unknown8006(100, 1, 1)
    sprite('ak404_08', 5)	# 35-39
    sprite('ak404_09', 5)	# 40-44
    sprite('ak404_10', 3)	# 45-47
    sprite('ak404_11', 4)	# 48-51
    sprite('ak404_12', 4)	# 52-55
    SFX_3('ak002')
    sprite('ak404_13', 5)	# 56-60

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
    sprite('ak032_00', 2)	# 1-2
    label(0)
    sprite('ak032_01', 4)	# 3-6
    sprite('ak032_02', 4)	# 7-10
    sprite('ak032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('ak032_04', 4)	# 15-18
    sprite('ak032_05', 4)	# 19-22
    sprite('ak032_06', 4)	# 23-26
    sprite('ak032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('ak032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak310_00', 2)	# 35-36
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ak310_01', 1)	# 37-37
    sprite('ak310_02', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('ak310_03', 3)	# 41-43
    sprite('ak310_04', 10)	# 44-53
    SFX_4('pak154')
    sprite('ak310_01', 5)	# 54-58
    sprite('ak310_00', 5)	# 59-63

@State
def CycloneThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('CycloneLvIcon')
    sprite('keep', 1)	# 1-1
    if Unknown23145('Ducking'):
        sendToLabel(0)
    sprite('ak406_00', 4)	# 2-5
    sprite('ak406_01', 4)	# 6-9
    physicsXImpulse(5000)
    Unknown3029(1)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('ak406_02', 2)	# 10-11
    Unknown1019(300)
    SFX_3('airbackdash_m')
    Unknown7007('70616b3231305f3000000000000000006400000070616b3231305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak406_03', 2)	# 12-13
    Unknown1019(300)
    sprite('ak406_02', 2)	# 14-15
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak406_03', 2)	# 16-17
    setInvincible(0)
    Unknown1019(60)
    sprite('ak406_04', 3)	# 18-20
    Unknown1019(50)
    label(0)
    sprite('ak310_00', 2)	# 21-22
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ak310_01', 1)	# 23-23
    sprite('ak310_02', 3)	# 24-26	 **attackbox here**
    Unknown1084(1)
    sprite('ak310_03', 3)	# 27-29
    sprite('ak310_04', 10)	# 30-39
    SFX_4('pak154')
    sprite('ak310_01', 5)	# 40-44
    sprite('ak310_00', 5)	# 45-49

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(500)
        AttackP2(100)
        AirPushbackX(12000)
        AirPushbackY(30000)
        Unknown11072(1, 200000, 60000)
        AirUntechableTime(30)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11056(0)
        JumpCancel_(0)
        Unknown11069('ThrowExe')
        Unknown11064(1)
        sendToLabelUpon(2, 0)
        callSubroutine('CycloneLvIcon')
    sprite('ak310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(1, 80)
    sprite('ak207_02', 3)	# 4-6
    Unknown5000(17, 0)
    sprite('ak207_02', 3)	# 7-9
    physicsXImpulse(20000)
    SFX_3('hit_h_fast')
    sprite('ak207_03', 1)	# 10-10	 **attackbox here**
    StartMultihit()
    physicsXImpulse(10)
    Unknown8000(100, 1, 1)
    sprite('ak207_04', 3)	# 11-13	 **attackbox here**
    Unknown23054('616b3230375f303300000000000000000000000000000000000000000000000003000000')
    tag_voice(1, 'pak201_0', 'pak201_2', '', '')
    Unknown1084(1)
    RefreshMultihit()
    Unknown30079(0)
    sprite('ak207_05', 2)	# 14-15
    sprite('ak207_06', 3)	# 16-18
    Unknown3032()
    Unknown3004(-30)
    sprite('ak207_07', 5)	# 19-23
    Unknown2015(40)
    Unknown2017(0)
    Unknown3001(0)
    ScreenShake(0, 4000)
    Unknown8001(1, 0)
    SLOT_12 = (SLOT_12 + SLOT_19)
    SLOT_13 = (SLOT_13 + SLOT_20)
    Unknown1019(14)
    YAccel(14)
    Unknown1019(140)
    YAccel(130)
    setGravity(1500)
    sprite('ak207_07', 2)	# 24-25
    Unknown3001(150)
    Unknown3004(10)
    sprite('ak207_07', 2)	# 26-27
    Unknown1019(80)
    YAccel(80)
    sprite('ak207_08', 2)	# 28-29
    Unknown2005()
    Unknown3001(255)
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak207_09', 2)	# 30-31
    SFX_3('hit_h_fast')
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak207_11', 3)	# 32-34	 **attackbox here**
    Unknown23054('616b3230375f313000000000000000000000000000000000000000000000000003000000')
    tag_voice(0, 'pak202_0', 'pak202_2', '', '')
    RefreshMultihit()
    AttackLevel_(3)
    AirPushbackX(10000)
    AirPushbackY(-15000)
    Unknown11072(1, 200000, -50000)
    Hitstop(4)
    Unknown11001(5, 5, 5)
    AirUntechableTime(35)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown11056(0)
    Unknown1019(20)
    YAccel(20)
    sprite('ak207_12', 4)	# 35-38
    physicsYImpulse(-10000)
    Unknown3001(128)
    Unknown3004(-20)
    sprite('ak207_00', 3)	# 39-41
    Unknown1084(1)
    teleportRelativeY(0)
    ScreenShake(0, 4000)
    Unknown3001(150)
    Unknown3004(20)
    Unknown8003(100, 1, 0)
    sprite('ak207_01', 3)	# 42-44
    Unknown3001(255)
    Unknown3004(0)
    sprite('ak207_02', 3)	# 45-47
    physicsXImpulse(40000)
    SFX_3('hit_h_fast')
    sprite('ak207_03', 1)	# 48-48	 **attackbox here**
    StartMultihit()
    physicsXImpulse(10)
    Unknown8000(100, 1, 1)
    sprite('ak207_04', 3)	# 49-51	 **attackbox here**
    Unknown23054('616b3230375f303300000000000000000000000000000000000000000000000003000000')
    tag_voice(0, 'pak203_0', 'pak203_2', '', '')
    physicsXImpulse(0)
    RefreshMultihit()
    AttackLevel_(3)
    AirPushbackX(15000)
    AirPushbackY(30000)
    Unknown11072(1, 200000, 60000)
    Hitstop(8)
    AirUntechableTime(35)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown11056(0)
    sprite('ak207_05', 2)	# 52-53
    sprite('ak207_06', 3)	# 54-56
    Unknown3032()
    Unknown3004(-30)
    sprite('ak207_07', 5)	# 57-61
    Unknown2015(40)
    Unknown2017(0)
    Unknown3001(0)
    ScreenShake(0, 4000)
    Unknown8001(1, 0)
    SLOT_12 = (SLOT_12 + SLOT_19)
    SLOT_13 = (SLOT_13 + SLOT_20)
    Unknown1019(14)
    YAccel(14)
    Unknown1019(160)
    YAccel(300)
    setGravity(1500)
    sprite('ak207_07', 2)	# 62-63
    Unknown3001(150)
    Unknown3004(10)
    sprite('ak207_07', 2)	# 64-65
    Unknown1019(80)
    YAccel(80)
    sprite('ak207_08', 2)	# 66-67
    Unknown2005()
    Unknown3001(255)
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak207_09', 2)	# 68-69
    SFX_3('hit_h_fast')
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak210_08', 2)	# 70-71	 **attackbox here**
    Unknown23054('616b3231305f303700000000000000000000000000000000000000000000000002000000')
    tag_voice(0, 'pak204_0', 'pak204_2', '', '')
    Unknown1084(1)
    RefreshMultihit()
    AttackP2(50)
    Unknown11072(1, 200000, -50000)
    GroundedHitstunAnimation(11)
    AirPushbackX(12000)
    AirPushbackY(-150000)
    Unknown9190(1)
    Unknown9118(15)
    Unknown9095()
    Unknown23086(1)
    Unknown11069('')
    Unknown11064(0)

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
        SLOT_59 = (SLOT_59 + 1)
        callSubroutine('CycloneSkillDeriveInput_Air')
    sprite('ak210_08', 32767)	# 72-32838	 **attackbox here**
    StartMultihit()
    physicsXImpulse(10000)
    physicsYImpulse(-50000)
    label(0)
    sprite('ak210_09', 4)	# 32839-32842
    Unknown1084(1)
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    sprite('ak210_10', 4)	# 32843-32846
    callSubroutine('CycloneSkillDeriveTiming_Air')
    sprite('ak210_10', 4)	# 32847-32850
    sprite('ak210_11', 4)	# 32851-32854
    callSubroutine('CycloneSkillDeriveClear_Air')
    Unknown18009(0)
    sprite('ak210_12', 4)	# 32855-32858
    sprite('ak210_13', 4)	# 32859-32862

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
    sprite('ak032_00', 2)	# 1-2
    label(0)
    sprite('ak032_01', 4)	# 3-6
    sprite('ak032_02', 4)	# 7-10
    sprite('ak032_03', 4)	# 11-14
    Unknown8006(100, 1, 1)
    sprite('ak032_04', 4)	# 15-18
    sprite('ak032_05', 4)	# 19-22
    sprite('ak032_06', 4)	# 23-26
    sprite('ak032_07', 4)	# 27-30
    Unknown8006(100, 1, 1)
    sprite('ak032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak310_00', 2)	# 35-36
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ak310_01', 1)	# 37-37
    sprite('ak310_02', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('ak310_03', 3)	# 41-43
    sprite('ak310_04', 10)	# 44-53
    SFX_4('pak154')
    sprite('ak310_01', 5)	# 54-58
    sprite('ak310_00', 5)	# 59-63

@State
def CycloneBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('CycloneLvIcon')
    sprite('keep', 1)	# 1-1
    if Unknown23145('Ducking'):
        sendToLabel(0)
    sprite('ak406_00', 4)	# 2-5
    sprite('ak406_01', 4)	# 6-9
    physicsXImpulse(5000)
    Unknown3029(1)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('ak406_02', 2)	# 10-11
    Unknown1019(300)
    SFX_3('airbackdash_m')
    Unknown7007('70616b3231305f3000000000000000006400000070616b3231305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak406_03', 2)	# 12-13
    Unknown1019(300)
    sprite('ak406_02', 2)	# 14-15
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak406_03', 2)	# 16-17
    setInvincible(0)
    Unknown1019(60)
    sprite('ak406_04', 3)	# 18-20
    Unknown1019(50)
    label(0)
    sprite('ak310_00', 2)	# 21-22
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ak310_01', 1)	# 23-23
    sprite('ak310_02', 3)	# 24-26	 **attackbox here**
    Unknown1084(1)
    sprite('ak310_03', 3)	# 27-29
    sprite('ak310_04', 10)	# 30-39
    SFX_4('pak154')
    sprite('ak310_01', 5)	# 40-44
    sprite('ak310_00', 5)	# 45-49

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(500)
        AttackP2(100)
        AirPushbackX(12000)
        AirPushbackY(30000)
        Unknown11072(1, 200000, 60000)
        AirUntechableTime(30)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11056(0)
        JumpCancel_(0)
        Unknown11069('BackThrowExe')
        Unknown11064(1)
        sendToLabelUpon(2, 0)
        callSubroutine('CycloneLvIcon')
    sprite('ak310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(1, 80)
    sprite('ak310_02', 1)	# 4-4	 **attackbox here**
    Unknown2005()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    sprite('ak207_02', 3)	# 5-7
    Unknown5000(17, 0)
    sprite('ak207_02', 3)	# 8-10
    physicsXImpulse(20000)
    SFX_3('hit_h_fast')
    sprite('ak207_03', 1)	# 11-11	 **attackbox here**
    StartMultihit()
    physicsXImpulse(10)
    Unknown8000(100, 1, 1)
    sprite('ak207_04', 3)	# 12-14	 **attackbox here**
    Unknown23054('616b3230375f303300000000000000000000000000000000000000000000000003000000')
    tag_voice(1, 'pak201_0', 'pak201_2', '', '')
    Unknown1084(1)
    RefreshMultihit()
    Unknown30079(0)
    sprite('ak207_05', 2)	# 15-16
    sprite('ak207_06', 3)	# 17-19
    Unknown3032()
    Unknown3004(-30)
    sprite('ak207_07', 5)	# 20-24
    Unknown2015(40)
    Unknown2017(0)
    Unknown3001(0)
    ScreenShake(0, 4000)
    Unknown8001(1, 0)
    SLOT_12 = (SLOT_12 + SLOT_19)
    SLOT_13 = (SLOT_13 + SLOT_20)
    Unknown1019(14)
    YAccel(14)
    Unknown1019(140)
    YAccel(130)
    setGravity(1500)
    sprite('ak207_07', 2)	# 25-26
    Unknown3001(150)
    Unknown3004(10)
    sprite('ak207_07', 2)	# 27-28
    Unknown1019(80)
    YAccel(80)
    sprite('ak207_08', 2)	# 29-30
    Unknown2005()
    Unknown3001(255)
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak207_09', 2)	# 31-32
    SFX_3('hit_h_fast')
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak207_11', 3)	# 33-35	 **attackbox here**
    Unknown23054('616b3230375f313000000000000000000000000000000000000000000000000003000000')
    tag_voice(0, 'pak202_0', 'pak202_2', '', '')
    RefreshMultihit()
    AttackLevel_(3)
    AirPushbackX(10000)
    AirPushbackY(-15000)
    Unknown11072(1, 200000, -50000)
    Hitstop(4)
    Unknown11001(5, 5, 5)
    AirUntechableTime(35)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown11056(0)
    Unknown1019(20)
    YAccel(20)
    sprite('ak207_12', 4)	# 36-39
    physicsYImpulse(-10000)
    Unknown3001(128)
    Unknown3004(-20)
    sprite('ak207_00', 3)	# 40-42
    Unknown1084(1)
    teleportRelativeY(0)
    ScreenShake(0, 4000)
    Unknown3001(150)
    Unknown3004(20)
    Unknown8003(100, 1, 0)
    sprite('ak207_01', 3)	# 43-45
    Unknown3001(255)
    Unknown3004(0)
    sprite('ak207_02', 3)	# 46-48
    physicsXImpulse(40000)
    SFX_3('hit_h_fast')
    sprite('ak207_03', 1)	# 49-49	 **attackbox here**
    StartMultihit()
    physicsXImpulse(10)
    Unknown8000(100, 1, 1)
    sprite('ak207_04', 3)	# 50-52	 **attackbox here**
    Unknown23054('616b3230375f303300000000000000000000000000000000000000000000000003000000')
    tag_voice(0, 'pak203_0', 'pak203_2', '', '')
    physicsXImpulse(0)
    RefreshMultihit()
    AttackLevel_(3)
    AirPushbackX(15000)
    AirPushbackY(30000)
    Unknown11072(1, 200000, 60000)
    Hitstop(8)
    AirUntechableTime(35)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown11056(0)
    sprite('ak207_05', 2)	# 53-54
    sprite('ak207_06', 3)	# 55-57
    Unknown3032()
    Unknown3004(-30)
    sprite('ak207_07', 5)	# 58-62
    Unknown2015(40)
    Unknown2017(0)
    Unknown3001(0)
    ScreenShake(0, 4000)
    Unknown8001(1, 0)
    SLOT_12 = (SLOT_12 + SLOT_19)
    SLOT_13 = (SLOT_13 + SLOT_20)
    Unknown1019(14)
    YAccel(14)
    Unknown1019(160)
    YAccel(300)
    setGravity(1500)
    sprite('ak207_07', 2)	# 63-64
    Unknown3001(150)
    Unknown3004(10)
    sprite('ak207_07', 2)	# 65-66
    Unknown1019(80)
    YAccel(80)
    sprite('ak207_08', 2)	# 67-68
    Unknown2005()
    Unknown3001(255)
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak207_09', 2)	# 69-70
    SFX_3('hit_h_fast')
    Unknown1019(50)
    YAccel(50)
    Unknown1039(50)
    sprite('ak210_08', 2)	# 71-72	 **attackbox here**
    Unknown23054('616b3231305f303700000000000000000000000000000000000000000000000002000000')
    tag_voice(0, 'pak204_0', 'pak204_2', '', '')
    Unknown1084(1)
    RefreshMultihit()
    AttackP2(50)
    Unknown11072(1, 200000, -50000)
    GroundedHitstunAnimation(11)
    AirPushbackX(12000)
    AirPushbackY(-150000)
    Unknown9190(1)
    Unknown9118(15)
    Unknown9095()
    Unknown23086(1)
    Unknown11069('')
    Unknown11064(0)

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
        SLOT_59 = (SLOT_59 + 1)
        callSubroutine('CycloneSkillDeriveInput_Air')
    sprite('ak210_08', 32767)	# 73-32839	 **attackbox here**
    StartMultihit()
    physicsXImpulse(10000)
    physicsYImpulse(-50000)
    label(0)
    sprite('ak210_09', 4)	# 32840-32843
    Unknown1084(1)
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    sprite('ak210_10', 4)	# 32844-32847
    callSubroutine('CycloneSkillDeriveTiming_Air')
    sprite('ak210_10', 4)	# 32848-32851
    sprite('ak210_11', 4)	# 32852-32855
    callSubroutine('CycloneSkillDeriveClear_Air')
    Unknown18009(0)
    sprite('ak210_12', 4)	# 32856-32859
    sprite('ak210_13', 4)	# 32860-32863

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        PushbackX(24800)
        AirPushbackX(0)
        AirPushbackY(16000)
        YImpluseBeforeWallbounce(2200)
        Unknown30055('c0d401002800000000000000')
        Unknown11001(0, 0, 0)
        AirUntechableTime(60)
        Unknown11092(1)
        Unknown11031(5)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(1500)
        if (SLOT_59 == 1):
            Damage(1700)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1900)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(2100)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2300)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2500)
            Unknown11031(10)
    sprite('ak400_00', 5)	# 1-5
    Unknown1051(60)
    Unknown26('SpecialDashSmoke')
    Unknown26('SpecialDoubleUpperFirst')
    sprite('ak400_01', 4)	# 6-9
    Unknown7007('70616b3230305f3000000000000000006400000070616b3230305f3100000000000000006400000070616b3230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak400_02', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    GFX_0('SpecialDoubleUpperFirst', 1)
    GFX_0('SpecialDashSmoke', 100)
    sprite('ak400_03', 2)	# 13-14
    physicsXImpulse(16000)
    sprite('ak400_04', 2)	# 15-16
    SFX_3('blaze_normal')
    physicsXImpulse(32000)
    sprite('ak400_05', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(1000)
    AirPushbackY(35000)
    Unknown30055('000000000000000000000000')
    Hitstop(12)
    physicsXImpulse(0)
    GFX_0('SpecialDoubleUpperSecond', 100)
    sprite('ak400_06', 3)	# 20-22
    setInvincible(0)
    SFX_3('cloth_m')
    sprite('ak400_07', 3)	# 23-25
    sprite('ak400_08', 3)	# 26-28
    sprite('ak400_06', 3)	# 29-31
    sprite('ak400_07', 3)	# 32-34
    sprite('ak400_08', 3)	# 35-37
    sprite('ak400_09', 4)	# 38-41
    sprite('ak400_10', 4)	# 42-45
    sprite('ak404_11', 5)	# 46-50
    sprite('ak404_12', 5)	# 51-55
    SFX_3('ak002')
    sprite('ak404_13', 7)	# 56-62

@State
def BoomerangHookA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9154(19)
        AirUntechableTime(19)
        Unknown11028(13)
        AirPushbackX(15000)
        AirPushbackY(16000)
        PushbackX(15300)
        Unknown11031(5)
        callSubroutine('CycloneSkillFlexChain')
        WhiffCancel('SonicPunchA')
        WhiffCancel('SonicPunchB')
        callSubroutine('CycloneLvIcon')
        if (SLOT_59 == 0):
            Damage(1200)
        if (SLOT_59 == 1):
            Damage(1500)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1650)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1800)
            AttackP2(85)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(1950)
            AttackP2(85)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2100)
            AttackP2(90)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            WhiffCancelEnable(1)
            SFX_3('grip_hugs')
            SLOT_59 = (SLOT_59 + 1)
    sprite('ak405_00', 1)	# 1-1
    sprite('ak405_01', 2)	# 2-3
    sprite('ak405_02', 5)	# 4-8
    sprite('ak405_03', 2)	# 9-10
    physicsXImpulse(20000)
    SFX_3('slash_sword_middle')
    GFX_0('SpecialQuakeSmoke', 100)
    ScreenShake(0, 5000)
    sprite('ak405_04', 2)	# 11-12
    Unknown1019(40)
    GFX_0('SpecialBodyBlowFirst', 100)
    sprite('ak405_05', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    GFX_0('SpecialBodyBlowMain', 100)
    Unknown7007('70616b3230395f3000000000000000006400000070616b3230395f3100000000000000006400000070616b3230395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak405_06', 2)	# 16-17
    Recovery()
    sprite('ak405_07', 2)	# 18-19
    sprite('ak405_08', 2)	# 20-21
    sprite('ak405_06', 2)	# 22-23
    sprite('ak405_07', 2)	# 24-25
    sprite('ak405_09', 2)	# 26-27
    sprite('ak405_11', 3)	# 28-30
    sprite('ak405_12', 3)	# 31-33
    WhiffCancelEnable(0)

@State
def SonicPunchA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9154(19)
        AirUntechableTime(19)
        Unknown11028(13)
        AirPushbackX(2000)
        AirPushbackY(20000)
        PushbackX(39900)
        Unknown11031(5)
        callSubroutine('CycloneSkillFlexChain')
        Unknown14084('SonicPunchB')
        WhiffCancel('BoomerangHookB')
        callSubroutine('CycloneLvIcon')
        if (SLOT_59 == 0):
            Damage(1200)
        if (SLOT_59 == 1):
            Damage(1500)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1700)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1900)
            AttackP2(85)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2100)
            AttackP2(85)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2300)
            AttackP2(90)
            AirUntechableTime(24)
            Unknown11031(10)

        def upon_11():
            clearUponHandler(11)
            WhiffCancelEnable(1)
            SFX_3('grip_hugs')
            SLOT_59 = (SLOT_59 + 1)
        Unknown2004(1, 0)
    sprite('ak409_00', 3)	# 1-3
    sprite('ak409_01', 3)	# 4-6
    physicsXImpulse(40000)
    GFX_0('SpecialQuakeSmoke', 100)
    Unknown8007(100, 1, 1)
    SFX_3('airbackdash_m')
    SFX_3('cloth_m')
    sprite('ak409_03', 2)	# 7-8
    Unknown1019(20)
    sprite('ak409_03', 2)	# 9-10
    Unknown1019(50)
    sprite('ak409_04', 2)	# 11-12	 **attackbox here**
    StartMultihit()
    Unknown1019(50)
    SFX_3('hit_h_middle')
    GFX_0('akef_dashupper', 100)
    Unknown7007('70616b3231365f3200000000000000006400000070616b3231365f3000000000000000006400000070616b3231375f3000000000000000006400000070616b3231375f32000000000000000064000000')
    sprite('ak409_04', 4)	# 13-16	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_1('akef_dashupper_smoke', 100)
    sprite('ak409_05', 6)	# 17-22
    Recovery()
    sprite('ak409_06', 4)	# 23-26
    sprite('ak409_07', 4)	# 27-30
    sprite('ak409_08', 4)	# 31-34
    WhiffCancelEnable(0)

@State
def BoomerangHookB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9154(19)
        AirUntechableTime(19)
        Unknown11028(13)
        AirPushbackX(15000)
        AirPushbackY(16000)
        PushbackX(3000)
        Unknown11031(5)
        callSubroutine('CycloneSkillFlexChain')
        WhiffCancel('SonicPunchA')
        WhiffCancel('SonicPunchB')
        callSubroutine('CycloneLvIcon')
        if (SLOT_59 == 0):
            Damage(1500)
        if (SLOT_59 == 1):
            Damage(1700)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1850)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(2000)
            AttackP2(85)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2150)
            AttackP2(85)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2300)
            AttackP2(90)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            WhiffCancelEnable(1)
            SFX_3('grip_hugs')
            SLOT_59 = (SLOT_59 + 1)
    sprite('ak405_00', 3)	# 1-3
    sprite('ak405_01', 3)	# 4-6
    sprite('ak405_02', 9)	# 7-15
    sprite('ak405_03', 3)	# 16-18
    physicsXImpulse(40000)
    SFX_3('slash_sword_middle')
    GFX_0('SpecialQuakeSmoke', 100)
    ScreenShake(0, 5000)
    sprite('ak405_04', 2)	# 19-20
    GFX_0('SpecialBodyBlowFirst', 100)
    sprite('ak405_05', 3)	# 21-23	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    GFX_0('SpecialBodyBlowMain', 100)
    Unknown7007('70616b3230395f3000000000000000006400000070616b3230395f3100000000000000006400000070616b3230395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak405_06', 2)	# 24-25
    Recovery()
    sprite('ak405_07', 2)	# 26-27
    sprite('ak405_08', 2)	# 28-29
    sprite('ak405_06', 2)	# 30-31
    sprite('ak405_07', 2)	# 32-33
    sprite('ak405_09', 2)	# 34-35
    sprite('ak405_11', 3)	# 36-38
    sprite('ak405_12', 3)	# 39-41
    WhiffCancelEnable(0)

@State
def SonicPunchB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9154(21)
        AirUntechableTime(21)
        Unknown11028(13)
        AirPushbackX(4000)
        AirPushbackY(20000)
        Unknown11031(5)
        callSubroutine('CycloneSkillFlexChain')
        Unknown14084('SonicPunchB')
        WhiffCancel('BoomerangHookB')
        callSubroutine('CycloneLvIcon')
        if (SLOT_59 == 0):
            Damage(1500)
        if (SLOT_59 == 1):
            Damage(1700)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1900)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(2100)
            AttackP2(85)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2300)
            AttackP2(85)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2500)
            AttackP2(90)
            AirUntechableTime(24)
            Unknown11031(10)

        def upon_11():
            clearUponHandler(11)
            WhiffCancelEnable(1)
            SFX_3('grip_hugs')
            SLOT_59 = (SLOT_59 + 1)
        Unknown2004(1, 0)
    sprite('ak409_00', 3)	# 1-3
    sprite('ak409_01', 3)	# 4-6
    physicsXImpulse(4500)
    GFX_0('SpecialQuakeSmoke', 100)
    SFX_0('airbackdash_m')
    SFX_0('cloth_m')
    sprite('ak409_02', 3)	# 7-9
    Unknown8007(100, 1, 1)
    Unknown1019(500)
    sprite('ak409_01', 3)	# 10-12
    Unknown8009(0)
    Unknown1019(500)
    sprite('ak409_03', 2)	# 13-14
    Unknown1019(30)
    sprite('ak409_03', 4)	# 15-18
    Unknown1019(50)
    sprite('ak409_04', 2)	# 19-20	 **attackbox here**
    StartMultihit()
    Unknown1019(50)
    SFX_0('hit_h_middle')
    GFX_0('akef_dashupper', 100)
    Unknown7007('70616b3231365f3200000000000000006400000070616b3231365f3000000000000000006400000070616b3231365f3100000000000000006400000070616b3231375f31000000000000000064000000')
    sprite('ak409_04', 4)	# 21-24	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_1('akef_dashupper_smoke', 100)
    sprite('ak409_05', 5)	# 25-29
    Recovery()
    sprite('ak409_06', 5)	# 30-34
    sprite('ak409_07', 4)	# 35-38
    sprite('ak409_08', 4)	# 39-42
    WhiffCancelEnable(0)

@State
def Ducking():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
    sprite('ak406_00', 3)	# 1-3
    sprite('ak406_00', 1)	# 4-4
    callSubroutine('CycloneSkillDeriveInput')
    Unknown14074('Ducking')
    callSubroutine('SpecialSkillDeriveInput')
    callSubroutine('DistortionSkillDeriveInput')
    Unknown23004(0, 0)
    sprite('ak406_01', 2)	# 5-6
    physicsXImpulse(40000)
    Unknown3029(1)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('ak406_02', 2)	# 7-8
    SFX_3('airbackdash_m')
    Unknown7007('70616b3231305f3000000000000000006400000070616b3231305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak406_03', 2)	# 9-10
    sprite('ak406_04', 2)	# 11-12
    Unknown1019(50)
    sprite('ak406_05', 2)	# 13-14
    SLOT_59 = (SLOT_59 + 1)
    Unknown1019(50)
    callSubroutine('CycloneSkillDeriveTiming')
    callSubroutine('SpecialSkillDeriveTiming')
    callSubroutine('DistortionSkillDeriveTiming')
    sprite('ak406_06', 3)	# 15-17
    Unknown1019(50)
    setInvincible(0)
    sprite('ak406_07', 3)	# 18-20
    Unknown1019(50)
    sprite('ak406_08', 5)	# 21-25
    Unknown1019(0)
    callSubroutine('CycloneSkillDeriveClear')
    callSubroutine('SpecialSkillDeriveClear')
    callSubroutine('DistortionSkillDeriveClear')

@State
def RushLegSweep():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirUntechableTime(40)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        PushbackX(15000)
        AirPushbackX(-1000)
        AirPushbackY(12000)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11031(5)
        callSubroutine('DiveDoNotBeginCancel')
        callSubroutine('CycloneLvIcon')
        if (SLOT_59 == 0):
            Damage(1500)
        if (SLOT_59 == 1):
            Damage(1700)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1850)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(2000)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2150)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2300)
            Unknown11031(10)
    sprite('ak211_00', 2)	# 1-2
    sprite('ak211_01', 2)	# 3-4
    sprite('ak211_02', 2)	# 5-6
    sprite('ak211_03', 2)	# 7-8
    SFX_3('hit_m_fast')
    sprite('ak211_05ex01', 5)	# 9-13	 **attackbox here**
    Unknown23054('616b3231315f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    SLOT_59 = (SLOT_59 + 1)
    physicsXImpulse(0)
    Unknown7007('70616b3130375f3000000000000000006400000070616b3130375f3100000000000000006400000070616b3130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak211_05', 5)	# 14-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ak211_07', 5)	# 19-23
    sprite('ak211_08', 5)	# 24-28
    sprite('ak211_09', 5)	# 29-33

@State
def CorkScrewA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        Hitstop(9)
        AirUntechableTime(70)
        PushbackX(-3000)
        AirPushbackX(80000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(2200)
        WallbounceReboundTime(20)
        Unknown11001(0, -4, -4)
        Unknown11056(0)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown11031(5)
        callSubroutine('DiveDoNotBeginCancel')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(2000)
        if (SLOT_59 == 1):
            Damage(2200)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(2400)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(2600)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2800)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(3000)
            Unknown11031(10)

        def upon_11():
            clearUponHandler(11)
            SFX_3('down_steal_m')
            ScreenShake(10000, 5000)
            sendToLabel(1)
    sprite('ak404_00', 4)	# 1-4
    sprite('ak404_01', 4)	# 5-8
    sprite('ak404_02', 2)	# 9-10	 **attackbox here**
    SLOT_59 = (SLOT_59 + 1)
    RefreshMultihit()
    physicsXImpulse(80000)
    Unknown8007(100, 1, 1)
    SFX_3('slash_blade_fast')
    GFX_0('SpecialScrewWind', 0)
    GFX_0('SpecialScrewFistAura', 0)
    GFX_0('SpecialDashSmoke', 100)
    Unknown7007('70616b3230375f3000000000000000006400000070616b3230375f3100000000000000006400000070616b3230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak404_03', 2)	# 11-12	 **attackbox here**
    label(1)
    sprite('ak404_04', 2)	# 13-14	 **attackbox here**
    sprite('ak404_05', 3)	# 15-17
    Unknown1019(80)
    Unknown8006(100, 1, 1)
    Recovery()
    sprite('ak404_06', 3)	# 18-20
    Unknown1019(0)
    Unknown8006(100, 1, 1)
    sprite('ak404_07', 3)	# 21-23
    Unknown8006(100, 1, 1)
    sprite('ak404_08', 4)	# 24-27
    sprite('ak404_09', 4)	# 28-31
    sprite('ak404_10', 3)	# 32-34
    sprite('ak404_11', 5)	# 35-39
    sprite('ak404_12', 5)	# 40-44
    SFX_3('ak002')
    sprite('ak404_13', 7)	# 45-51

@State
def CorkScrewB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        Hitstop(9)
        AirUntechableTime(70)
        PushbackX(20000)
        AirPushbackX(80000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(2200)
        WallbounceReboundTime(20)
        Unknown11001(0, -4, -4)
        Unknown11056(0)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown11031(5)
        callSubroutine('DiveDoNotBeginCancel')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(2000)
        if (SLOT_59 == 1):
            Damage(2200)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(2400)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(2600)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2800)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(3000)
            Unknown11031(10)
        loopRelated(17, 47)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(3)

        def upon_11():
            clearUponHandler(11)
            SFX_3('down_steal_m')
            ScreenShake(10000, 5000)
            sendToLabel(2)
    sprite('ak407_00', 4)	# 1-4
    sprite('ak407_04', 3)	# 5-7
    Unknown3029(1)
    physicsXImpulse(-20000)
    SFX_3('cloth_m')
    Unknown7007('70616b3231315f3000000000000000006400000070616b3231315f3100000000000000006400000070616b3231315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak407_05', 1)	# 8-8
    Unknown1019(125)
    sprite('ak407_05', 2)	# 9-10
    sprite('ak407_06', 3)	# 11-13
    sendToLabelUpon(24, 1)
    setInvincible(1)
    Unknown22019('0000000001000000000000000000000000000000')
    sprite('ak407_08', 3)	# 14-16
    physicsXImpulse(-10000)
    sprite('ak407_09', 4)	# 17-20
    SFX_0('cloth_m')
    physicsXImpulse(0)
    sprite('ak407_10', 4)	# 21-24
    sprite('ak407_11', 4)	# 25-28
    sprite('ak407_12', 4)	# 29-32
    label(0)
    sprite('ak407_01', 4)	# 33-36
    sprite('ak407_02', 4)	# 37-40
    sprite('ak407_03', 3)	# 41-43
    SFX_0('cloth_m')
    sprite('ak407_04', 4)	# 44-47
    sprite('ak407_05', 4)	# 48-51
    sprite('ak407_06', 4)	# 52-55
    sprite('ak407_08', 4)	# 56-59
    sprite('ak407_09', 4)	# 60-63
    sprite('ak407_10', 4)	# 64-67
    sprite('ak407_11', 4)	# 68-71
    sprite('ak407_12', 4)	# 72-75
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak404_00', 2)	# 76-77
    clearUponHandler(24)
    clearUponHandler(17)
    setInvincible(0)
    Unknown1019(30)
    sprite('ak404_01', 2)	# 78-79
    sprite('ak404_02', 2)	# 80-81	 **attackbox here**
    SLOT_59 = (SLOT_59 + 1)
    RefreshMultihit()
    physicsXImpulse(80000)
    Unknown8007(100, 1, 1)
    SFX_3('slash_blade_fast')
    GFX_0('SpecialScrewWind', 0)
    GFX_0('SpecialScrewFistAura', 0)
    GFX_0('UltimateUpperSmoke', 100)
    Unknown7007('70616b3230385f3000000000000000006400000070616b3230385f3100000000000000006400000070616b3230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak404_03', 1)	# 82-82	 **attackbox here**
    sprite('ak404_03', 1)	# 83-83	 **attackbox here**
    label(2)
    sprite('ak404_04', 2)	# 84-85	 **attackbox here**
    sprite('ak404_05', 3)	# 86-88
    Unknown1019(80)
    Unknown8006(100, 1, 1)
    Recovery()
    sprite('ak404_06', 3)	# 89-91
    Unknown1019(0)
    Unknown8006(100, 1, 1)
    sprite('ak404_07', 3)	# 92-94
    Unknown8006(100, 1, 1)
    sprite('ak404_08', 4)	# 95-98
    sprite('ak404_09', 4)	# 99-102
    sprite('ak404_10', 3)	# 103-105
    sprite('ak404_11', 5)	# 106-110
    sprite('ak404_12', 5)	# 111-115
    SFX_3('ak002')
    sprite('ak404_13', 7)	# 116-122
    ExitState()
    label(3)
    sprite('ak404_13', 6)	# 123-128
    clearUponHandler(24)
    clearUponHandler(17)
    Unknown3029(0)
    setInvincible(0)

@State
def CorkScrewEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        Hitstop(9)
        AirUntechableTime(70)
        PushbackX(20000)
        AirPushbackX(80000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(2200)
        WallbounceReboundTime(20)
        Unknown11001(0, -4, -4)
        Unknown11056(0)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown11091(10)
        Unknown30065(0)
        Unknown11031(5)
        callSubroutine('DiveDoNotBeginCancel')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(2200)
        if (SLOT_59 == 1):
            Damage(2400)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(2600)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(2800)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(3000)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(3200)
            Unknown11031(10)

        def upon_11():
            clearUponHandler(11)
            SFX_3('down_steal_m')
            ScreenShake(30000, 15000)
            sendToLabel(1)
    sprite('ak406_00', 3)	# 1-3
    sprite('ak406_01', 2)	# 4-5
    physicsXImpulse(50000)
    Unknown3029(1)
    Unknown2017(0)
    Unknown23125('')
    Unknown2058(-5000)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('ak406_02', 2)	# 6-7
    SFX_3('airbackdash_m')
    sprite('ak406_03', 2)	# 8-9
    sprite('ak406_04', 2)	# 10-11
    Unknown1019(80)
    Unknown2017(1)
    sprite('ak404_00', 2)	# 12-13
    Unknown2006()
    setInvincible(0)
    sprite('ak404_01', 2)	# 14-15
    sprite('ak404_02', 2)	# 16-17	 **attackbox here**
    SLOT_59 = (SLOT_59 + 1)
    RefreshMultihit()
    physicsXImpulse(80000)
    Unknown8007(100, 1, 1)
    SFX_3('slash_blade_fast')
    GFX_0('SpecialScrewWind', 0)
    GFX_0('SpecialScrewFistAura', 0)
    GFX_0('UltimateUpperSmoke', 100)
    Unknown7007('70616b3230385f3000000000000000006400000070616b3230385f3100000000000000006400000070616b3230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ak404_03', 1)	# 18-18	 **attackbox here**
    sprite('ak404_03', 1)	# 19-19	 **attackbox here**
    label(1)
    sprite('ak404_04', 2)	# 20-21	 **attackbox here**
    sprite('ak404_05', 3)	# 22-24
    Unknown1019(80)
    Unknown8006(100, 1, 1)
    Recovery()
    sprite('ak404_06', 3)	# 25-27
    Unknown1019(0)
    Unknown8006(100, 1, 1)
    sprite('ak404_07', 3)	# 28-30
    Unknown8006(100, 1, 1)
    sprite('ak404_08', 4)	# 31-34
    sprite('ak404_09', 4)	# 35-38
    sprite('ak404_10', 3)	# 39-41
    sprite('ak404_11', 5)	# 42-46
    sprite('ak404_12', 5)	# 47-51
    SFX_3('ak002')
    sprite('ak404_13', 7)	# 52-58

@State
def AssaultDiveLandA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(40)
        Unknown9310(10)
        PushbackX(0)
        AirPushbackX(22500)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(3000)
        Unknown30056('6079feff6400000000000000')
        Unknown11031(5)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('DiveDoNotBeginCancel')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(900)
        if (SLOT_59 == 1):
            Damage(1100)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1300)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1500)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(1700)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(1900)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
            callSubroutine('CycloneSkillFlexChain')
            callSubroutine('SpecialSkillFlexChain')
    sprite('ak210_00', 3)	# 1-3
    sprite('ak210_01', 3)	# 4-6
    Unknown23004(0, 0)
    sprite('ak210_02', 3)	# 7-9
    sprite('ak210_03', 3)	# 10-12
    physicsXImpulse(8000)
    physicsYImpulse(25000)
    setGravity(2200)
    sprite('ak210_04', 3)	# 13-15
    sprite('ak210_05', 3)	# 16-18
    SFX_3('hit_h_slow')
    sprite('ak210_06', 3)	# 19-21
    sprite('ak408_01', 6)	# 22-27
    Unknown1084(1)
    sendToLabelUpon(2, 1)
    sprite('ak408_02', 6)	# 28-33
    Unknown7007('70616b3231345f3000000000000000006400000070616b3231345f3100000000000000006400000070616b3231355f310000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 34-35
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    physicsXImpulse(40000)
    physicsYImpulse(-35000)
    setGravity(3000)
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 36-37	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialAirFistAura', 0)
    loopRest()
    label(0)
    sprite('ak408_05', 2)	# 38-39	 **attackbox here**
    sprite('ak408_04', 2)	# 40-41	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak408_06', 4)	# 42-45	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak408_06', 2)	# 46-47	 **attackbox here**
    RefreshMultihit()
    PushbackX(9800)
    AirPushbackX(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown9310(0)
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('down_marble_m')
        ScreenShake(0, 15000)
        callSubroutine('CycloneSkillFlexChain')
        callSubroutine('SpecialSkillFlexChain')
        callSubroutine('CycloneSkillDeriveInput')
        callSubroutine('SpecialSkillDeriveInput')
        Unknown2037(1)
    sprite('ak408_07', 2)	# 48-49
    Recovery()
    sprite('ak408_07', 2)	# 50-51
    WhiffCancelEnable(1)
    if SLOT_2:
        callSubroutine('CycloneSkillDeriveTiming')
        callSubroutine('SpecialSkillDeriveTiming')
    sprite('ak408_08', 5)	# 52-56
    sprite('ak408_09', 8)	# 57-64
    WhiffCancelEnable(0)
    callSubroutine('CycloneSkillDeriveClear')
    callSubroutine('SpecialSkillDeriveClear')
    sprite('ak408_10', 5)	# 65-69

@State
def AssaultDiveLandB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(95)
        AirUntechableTime(40)
        Unknown9310(10)
        PushbackX(0)
        AirPushbackX(30000)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(4000)
        Unknown11031(5)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('DiveDoNotBeginCancel')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(900)
        if (SLOT_59 == 1):
            Damage(1100)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1300)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1500)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(1700)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(1900)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
            callSubroutine('CycloneSkillFlexChain')
            callSubroutine('SpecialSkillFlexChain')
    sprite('ak210_00', 3)	# 1-3
    sprite('ak210_01', 3)	# 4-6
    Unknown23004(0, 0)
    sprite('ak210_02', 3)	# 7-9
    sprite('ak210_03', 4)	# 10-13
    physicsXImpulse(15000)
    physicsYImpulse(30000)
    setGravity(1500)
    sprite('ak210_04', 4)	# 14-17
    sprite('ak210_05', 4)	# 18-21
    SFX_3('hit_h_slow')
    sprite('ak210_06', 4)	# 22-25
    sprite('ak408_01', 6)	# 26-31
    Unknown1084(1)
    sendToLabelUpon(2, 1)
    sprite('ak408_02', 6)	# 32-37
    Unknown7007('70616b3231345f3200000000000000006400000070616b3231355f3000000000000000006400000070616b3231355f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 38-39
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    physicsXImpulse(60000)
    physicsYImpulse(-40000)
    setGravity(3000)
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 40-41	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialAirFistAura', 0)
    label(0)
    sprite('ak408_05', 2)	# 42-43	 **attackbox here**
    sprite('ak408_04', 2)	# 44-45	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak408_06', 4)	# 46-49	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak408_06', 2)	# 50-51	 **attackbox here**
    RefreshMultihit()
    PushbackX(9800)
    Unknown11001(0, 0, 0)
    Unknown11058('0000000001000000000000000000000000000000')
    AirHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(-23000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown11065(1)
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('down_marble_m')
        ScreenShake(0, 15000)
        callSubroutine('CycloneSkillFlexChain')
        callSubroutine('SpecialSkillFlexChain')
        callSubroutine('CycloneSkillDeriveInput')
        callSubroutine('SpecialSkillDeriveInput')
        Unknown2037(1)
    sprite('ak408_07', 2)	# 52-53
    Recovery()
    sprite('ak408_07', 2)	# 54-55
    WhiffCancelEnable(1)
    if SLOT_2:
        callSubroutine('CycloneSkillDeriveTiming')
        callSubroutine('SpecialSkillDeriveTiming')
    sprite('ak408_08', 5)	# 56-60
    sprite('ak408_09', 8)	# 61-68
    WhiffCancelEnable(0)
    callSubroutine('CycloneSkillDeriveClear')
    callSubroutine('SpecialSkillDeriveClear')
    sprite('ak408_10', 5)	# 69-73

@State
def AssaultDiveLandEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(40)
        Unknown9310(10)
        PushbackX(0)
        AirPushbackX(27000)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(4000)
        Unknown11091(10)
        Unknown30065(0)
        Unknown11031(5)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('DiveDoNotBeginCancel')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(900)
        if (SLOT_59 == 1):
            Damage(1100)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1300)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1500)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(1700)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(1900)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
            callSubroutine('CycloneSkillFlexChain')
            callSubroutine('SpecialSkillFlexChain')
    sprite('ak210_01', 3)	# 1-3
    sprite('ak210_02', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    Unknown23004(0, 0)
    sprite('ak210_03', 3)	# 7-9
    physicsXImpulse(15000)
    physicsYImpulse(30000)
    setGravity(1500)
    sprite('ak210_04', 2)	# 10-11
    sprite('ak210_05', 2)	# 12-13
    SFX_3('hit_h_slow')
    sprite('ak210_06', 2)	# 14-15
    sprite('ak408_01', 3)	# 16-18
    Unknown1084(1)
    sendToLabelUpon(2, 1)
    sprite('ak408_02', 3)	# 19-21
    Unknown7007('70616b3231345f3000000000000000006400000070616b3231345f3100000000000000006400000070616b3231355f310000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 22-23
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    physicsXImpulse(50000)
    physicsYImpulse(-40000)
    setGravity(3000)
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialAirFistAura', 0)
    label(0)
    sprite('ak408_05', 2)	# 26-27	 **attackbox here**
    sprite('ak408_04', 2)	# 28-29	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak408_06', 4)	# 30-33	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak408_06', 2)	# 34-35	 **attackbox here**
    RefreshMultihit()
    PushbackX(9800)
    Unknown11001(0, 0, 0)
    Unknown11058('0000000001000000000000000000000000000000')
    AirHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(-23000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown11065(1)
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('down_marble_m')
        ScreenShake(0, 15000)
        callSubroutine('CycloneSkillFlexChain')
        callSubroutine('SpecialSkillFlexChain')
        callSubroutine('CycloneSkillDeriveInput')
        callSubroutine('SpecialSkillDeriveInput')
        Unknown2037(1)
    sprite('ak408_07', 2)	# 36-37
    Recovery()
    sprite('ak408_07', 2)	# 38-39
    WhiffCancelEnable(1)
    if SLOT_2:
        callSubroutine('CycloneSkillDeriveTiming')
        callSubroutine('SpecialSkillDeriveTiming')
    sprite('ak408_08', 5)	# 40-44
    sprite('ak408_09', 8)	# 45-52
    WhiffCancelEnable(0)
    callSubroutine('CycloneSkillDeriveClear')
    callSubroutine('SpecialSkillDeriveClear')
    sprite('ak408_10', 5)	# 53-57

@State
def AssaultDiveAirA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(40)
        Unknown9310(10)
        PushbackX(0)
        AirPushbackX(22500)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(3000)
        Unknown30056('6079feff6400000000000000')
        Unknown11031(5)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(1100)
        if (SLOT_59 == 1):
            Damage(1300)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1500)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1700)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(1900)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2100)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
            callSubroutine('CycloneSkillFlexChain')
            callSubroutine('SpecialSkillFlexChain')
    sprite('ak408_00', 3)	# 1-3
    if 
    if (not Unknown23145('ThrowExe')):
        Unknown23145('BackThrowExe'):
        clearUponHandler(2)
    sprite('ak408_01', 2)	# 4-5
    Unknown1084(1)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    Unknown23004(0, 0)
    sprite('ak408_02', 2)	# 6-7
    Unknown7007('70616b3231345f3000000000000000006400000070616b3231345f3100000000000000006400000070616b3231355f310000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 8-9
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    physicsXImpulse(22500)
    physicsYImpulse(-30000)
    setGravity(3000)
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 10-11	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialAirFistAura', 0)
    loopRest()
    label(0)
    sprite('ak408_05', 2)	# 12-13	 **attackbox here**
    sprite('ak408_04', 2)	# 14-15	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak408_06', 4)	# 16-19	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak408_06', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(1)
    PushbackX(9800)
    AirPushbackX(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown9310(0)
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('down_marble_m')
        ScreenShake(0, 15000)
        callSubroutine('CycloneSkillFlexChain')
        callSubroutine('SpecialSkillFlexChain')
        callSubroutine('CycloneSkillDeriveInput')
        callSubroutine('SpecialSkillDeriveInput')
        Unknown2037(1)
    sprite('ak408_07', 2)	# 22-23
    Recovery()
    sprite('ak408_07', 2)	# 24-25
    WhiffCancelEnable(1)
    if SLOT_2:
        callSubroutine('CycloneSkillDeriveTiming')
        callSubroutine('SpecialSkillDeriveTiming')
    sprite('ak408_08', 5)	# 26-30
    sprite('ak408_09', 8)	# 31-38
    WhiffCancelEnable(0)
    callSubroutine('CycloneSkillDeriveClear')
    callSubroutine('SpecialSkillDeriveClear')
    sprite('ak408_10', 5)	# 39-43

@State
def AssaultDiveAirB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(40)
        Unknown9310(10)
        PushbackX(0)
        AirPushbackX(30000)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(3000)
        Unknown30056('6079feff6400000000000000')
        Unknown11031(5)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(1300)
        if (SLOT_59 == 1):
            Damage(1500)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1700)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1900)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2100)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2300)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
            callSubroutine('CycloneSkillFlexChain')
            callSubroutine('SpecialSkillFlexChain')
    sprite('ak408_00', 3)	# 1-3
    if 
    if (not Unknown23145('ThrowExe')):
        Unknown23145('BackThrowExe'):
        clearUponHandler(2)
    sprite('ak408_00', 4)	# 4-7
    Unknown1084(1)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    Unknown23004(0, 0)
    sprite('ak408_01', 7)	# 8-14
    sprite('ak408_02', 7)	# 15-21
    Unknown7007('70616b3231345f3200000000000000006400000070616b3231355f3000000000000000006400000070616b3231355f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 3)	# 22-24
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    physicsXImpulse(30000)
    physicsYImpulse(-30000)
    setGravity(3000)
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialAirFistAura', 0)
    label(0)
    sprite('ak408_05', 2)	# 27-28	 **attackbox here**
    sprite('ak408_04', 2)	# 29-30	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak408_06', 4)	# 31-34	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak408_06', 1)	# 35-35	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(1)
    PushbackX(9800)
    AirPushbackX(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown9310(0)
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown23119(-16777216, 18, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('down_marble_m')
        ScreenShake(0, 15000)
        callSubroutine('CycloneSkillFlexChain')
        callSubroutine('SpecialSkillFlexChain')
        callSubroutine('CycloneSkillDeriveInput')
        callSubroutine('SpecialSkillDeriveInput')
        Unknown2037(1)
    sprite('ak408_06', 1)	# 36-36	 **attackbox here**
    sprite('ak408_07', 2)	# 37-38
    Recovery()
    sprite('ak408_07', 2)	# 39-40
    WhiffCancelEnable(1)
    if SLOT_2:
        callSubroutine('CycloneSkillDeriveTiming')
        callSubroutine('SpecialSkillDeriveTiming')
    sprite('ak408_08', 5)	# 41-45
    sprite('ak408_09', 8)	# 46-53
    WhiffCancelEnable(0)
    callSubroutine('CycloneSkillDeriveClear')
    callSubroutine('SpecialSkillDeriveClear')
    sprite('ak408_10', 5)	# 54-58

@State
def AssaultDiveAirEX():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(40)
        Unknown9310(10)
        PushbackX(0)
        AirPushbackX(27000)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(4000)
        Unknown11091(10)
        Unknown30065(0)
        Unknown11031(5)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            Damage(1300)
        if (SLOT_59 == 1):
            Damage(1500)
            Unknown11031(6)
        if (SLOT_59 == 2):
            Damage(1700)
            Unknown11031(7)
        if (SLOT_59 == 3):
            Damage(1900)
            Unknown11031(8)
        if (SLOT_59 == 4):
            Damage(2100)
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Damage(2300)
            Unknown11031(10)

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('down_marble_m')
            ScreenShake(0, 15000)
            callSubroutine('CycloneSkillFlexChain')
            callSubroutine('SpecialSkillFlexChain')
    sprite('ak408_00', 3)	# 1-3
    if 
    if (not Unknown23145('ThrowExe')):
        Unknown23145('BackThrowExe'):
        clearUponHandler(2)
    sprite('ak408_01', 2)	# 4-5
    Unknown1084(1)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    Unknown23004(0, 0)
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ak408_02', 2)	# 6-7
    Unknown7007('70616b3231345f3000000000000000006400000070616b3231345f3100000000000000006400000070616b3231355f310000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('slash_blade_fast')
    sprite('ak408_03', 2)	# 8-9
    SFX_3('airdash_m')
    SFX_3('slash_blade_slow')
    physicsXImpulse(30000)
    physicsYImpulse(-30000)
    setGravity(4000)
    Unknown23118(-10198016)
    GFX_0('SpecialAirBodyAura', 100)
    sprite('ak408_04', 2)	# 10-11	 **attackbox here**
    RefreshMultihit()
    GFX_0('SpecialAirFistAura', 0)
    label(0)
    sprite('ak408_05', 2)	# 12-13	 **attackbox here**
    sprite('ak408_04', 2)	# 14-15	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ak408_06', 4)	# 16-19	 **attackbox here**
    Unknown1084(1)
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('damage_hit_h')
    SLOT_59 = (SLOT_59 + 1)
    sprite('ak408_06', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    PushbackX(9800)
    Unknown11001(0, 0, 0)
    Unknown11058('0000000001000000000000000000000000000000')
    AirHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(-23000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown11065(1)
    Unknown18009(1)
    Unknown8004(100, 1, 1)
    Unknown26('SpecialAirBodyAura')
    Unknown26('SpecialAirFistAura')
    SFX_3('bomb_m')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('down_marble_m')
        ScreenShake(0, 15000)
        callSubroutine('CycloneSkillFlexChain')
        callSubroutine('SpecialSkillFlexChain')
        callSubroutine('CycloneSkillDeriveInput')
        callSubroutine('SpecialSkillDeriveInput')
        Unknown2037(1)
    sprite('ak408_07', 2)	# 22-23
    Recovery()
    sprite('ak408_07', 2)	# 24-25
    WhiffCancelEnable(1)
    if SLOT_2:
        callSubroutine('CycloneSkillDeriveTiming')
        callSubroutine('SpecialSkillDeriveTiming')
    sprite('ak408_08', 5)	# 26-30
    sprite('ak408_09', 8)	# 31-38
    WhiffCancelEnable(0)
    callSubroutine('CycloneSkillDeriveClear')
    callSubroutine('SpecialSkillDeriveClear')
    sprite('ak408_10', 5)	# 39-43

@State
def CycloneUpper():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(3000)
        AttackP2(80)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(0)
        Unknown30055('c0d401003c00000000000000')
        Hitstop(25)
        Unknown11056(0)
        Unknown11068(1)
        Unknown11062(1)
        Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
        Unknown2006()
        Unknown11064(1)
        Unknown11031(5)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            pass
        if (SLOT_59 == 1):
            SLOT_51 = 1
            Unknown11031(6)
        if (SLOT_59 == 2):
            SLOT_51 = 1
            Unknown11031(7)
        if (SLOT_59 == 3):
            SLOT_52 = 1
            Unknown11031(8)
        if (SLOT_59 == 4):
            SLOT_52 = 1
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Hitstop(40)
            SLOT_53 = 1
            Unknown11031(10)

        def upon_78():
            if (not SLOT_57):
                Unknown11069('CycloneUpper')
                Unknown13024(0)
            else:
                Unknown11069('')
                Unknown13024(1)
                if (SLOT_59 >= 5):
                    Unknown13024(0)
            if SLOT_53:
                Unknown20000(1)
                Unknown20009(900)
            if SLOT_2:
                clearUponHandler(78)
                physicsYImpulse(120000)
                Unknown1019(80)
                setInvincible(1)
        setInvincible(1)
        sendToLabelUpon(2, 99)
    sprite('ak430_00', 1)	# 1-1
    Unknown3029(1)
    physicsXImpulse(4000)
    sprite('ak430_00', 2)	# 2-3
    Unknown1019(500)
    Unknown8007(100, 1, 0)
    sprite('ak430_01', 2)	# 4-5
    Unknown1019(10)
    Unknown8007(100, 1, 0)
    if (SLOT_59 >= 5):
        SLOT_58 = 1
        tag_voice(1, 'pak252_0', 'pak252_1', '', '')
    else:
        tag_voice(1, 'pak250_0', 'pak250_1', '', '')
    sprite('ak430_01', 2)	# 6-7
    Unknown8006(100, 1, 0)
    Unknown30080('')
    if (not (SLOT_59 >= 1)):
        Unknown2036(30, -1, 0)
    else:
        Unknown2036(35, -1, 0)
    Unknown2058(-10000)
    sprite('ak430_03', 30)	# 8-37
    Unknown1019(0)
    sprite('ak430_04', 2)	# 38-39
    physicsXImpulse(3000)
    sprite('ak430_05', 2)	# 40-41
    Unknown1019(200)
    sprite('ak430_06', 3)	# 42-44	 **attackbox here**
    Unknown1019(200)
    RefreshMultihit()
    Unknown11072(1, 150000, 30000)
    Unknown8003(100, 1, 1)
    GFX_0('UltimateFirstPunch', 0)
    sprite('ak430_06', 3)	# 45-47	 **attackbox here**
    Unknown23027()
    Unknown11057(500)
    sprite('ak430_07', 1)	# 48-48	 **attackbox here**
    Unknown1019(40)
    ScreenShake(1000, 8000)
    Unknown8001(1, 0)
    sprite('ak430_07', 1)	# 49-49	 **attackbox here**
    if SLOT_58:
        tag_voice(0, 'pak253_0', 'pak253_1', '', '')
    else:
        tag_voice(0, 'pak251_0', 'pak251_1', '', '')
    if SLOT_51:
        sendToLabel(1)
    elif SLOT_52:
        sendToLabel(2)
    elif SLOT_53:
        sendToLabel(3)
    loopRest()
    label(0)
    sprite('ak430_08', 1)	# 50-50	 **attackbox here**
    SFX_0('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(42000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 51-52	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    Damage(1500)
    AttackP2(91)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(10000)
    AirPushbackY(38000)
    sprite('ak430_08', 2)	# 53-54	 **attackbox here**
    setInvincible(0)
    SFX_0('slash_blade_fast')
    sprite('ak430_09', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 3)	# 57-59	 **attackbox here**
    RefreshMultihit()
    SLOT_57 = 1
    Unknown11064(0)
    sprite('ak430_10', 3)	# 60-62	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('ak430_08', 1)	# 63-63	 **attackbox here**
    SFX_0('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(48000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 64-65	 **attackbox here**
    RefreshMultihit()
    Damage(1050)
    Unknown11091(19)
    if (SLOT_59 == 2):
        Damage(1200)
        Unknown11091(18)
    AttackP2(95)
    Hitstop(3)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(40000)
    sprite('ak430_08', 2)	# 66-67	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    SFX_0('slash_blade_fast')
    sprite('ak430_09', 2)	# 68-69	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 3)	# 70-72	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_10', 3)	# 73-75	 **attackbox here**
    RefreshMultihit()
    SLOT_57 = 1
    Unknown11064(0)
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('ak430_08', 1)	# 76-76	 **attackbox here**
    SFX_0('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(60000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 77-78	 **attackbox here**
    RefreshMultihit()
    Damage(1000)
    Unknown11091(17)
    if (SLOT_59 == 4):
        Damage(1150)
        Unknown11091(16)
    AttackP2(96)
    Hitstop(2)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(14000)
    AirPushbackY(48000)
    sprite('ak430_08', 2)	# 79-80	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    SFX_0('slash_blade_fast')
    sprite('ak430_09', 2)	# 81-82	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 83-83	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 84-84	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 85-85	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_10', 3)	# 86-88	 **attackbox here**
    RefreshMultihit()
    SLOT_57 = 1
    Unknown11064(0)
    loopRest()
    gotoLabel(10)
    label(3)
    SLOT_53 = 0
    clearUponHandler(2)
    sendToLabelUpon(2, 5)
    sprite('ak430_08', 1)	# 89-89	 **attackbox here**
    SFX_0('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(72000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 90-91	 **attackbox here**
    RefreshMultihit()
    Damage(600)
    Unknown11091(15)
    AttackP2(98)
    Hitstop(12)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(1000)
    AirPushbackY(66000)
    HitAirUnblockable(0)
    Unknown30056('20a107005000000000000000')
    sprite('ak430_08', 2)	# 92-93	 **attackbox here**
    Hitstop(6)
    RefreshMultihit()
    setInvincible(0)
    SFX_0('slash_blade_fast')
    sprite('ak430_09', 2)	# 94-95	 **attackbox here**
    RefreshMultihit()
    Hitstop(3)
    sprite('ak430_09', 2)	# 96-97	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_10', 2)	# 98-99	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 2)	# 100-101	 **attackbox here**
    RefreshMultihit()
    Hitstop(1)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak430_10', 2)	# 102-103	 **attackbox here**
    RefreshMultihit()
    Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
    sprite('ak430_09', 2)	# 104-105	 **attackbox here**
    RefreshMultihit()
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak430_10', 1)	# 106-106	 **attackbox here**
    RefreshMultihit()
    Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
    sprite('ak430_10', 1)	# 107-107	 **attackbox here**
    RefreshMultihit()
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak430_09', 1)	# 108-108	 **attackbox here**
    RefreshMultihit()
    Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
    sprite('ak430_09', 1)	# 109-109	 **attackbox here**
    RefreshMultihit()
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak430_10', 1)	# 110-110	 **attackbox here**
    RefreshMultihit()
    Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
    sprite('ak430_10', 1)	# 111-111	 **attackbox here**
    RefreshMultihit()
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ak430_10', 1)	# 112-112	 **attackbox here**
    Unknown2037(1)
    RefreshMultihit()
    AirUntechableTime(100)
    Unknown9310(35)
    AirPushbackX(-1000)
    AirPushbackY(40000)
    YImpluseBeforeWallbounce(1200)
    Unknown30056('400d03006400000000000000')
    Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
    SLOT_57 = 1
    Unknown11064(0)
    loopRest()
    sprite('ak430_12', 3)	# 113-115
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 3)	# 116-118
    sprite('ak430_14', 3)	# 119-121
    sprite('ak430_15', 3)	# 122-124
    sprite('ak020_04', 3)	# 125-127
    sprite('ak020_05', 3)	# 128-130
    sprite('ak020_06', 3)	# 131-133
    label(4)
    Unknown1039(110)
    Unknown1019(90)
    sprite('ak020_07', 4)	# 134-137
    sprite('ak020_08', 4)	# 138-141
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('ak210_09', 12)	# 142-153
    Unknown1084(1)
    Unknown20001(1)
    ScreenShake(5000, 30000)
    Unknown8000(100, 1, 1)
    Unknown8003(100, 1, 1)
    sprite('ak210_10', 20)	# 154-173
    Unknown13024(1)

    def upon_3():
        if (not SLOT_158):
            clearUponHandler(3)
            Unknown20000(0)
    sprite('ak210_11', 7)	# 174-180
    sprite('ak210_12', 5)	# 181-185
    sprite('ak210_13', 5)	# 186-190
    ExitState()
    label(10)
    sprite('ak430_12', 2)	# 191-192
    YAccel(60)
    Unknown1019(80)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 2)	# 193-194
    sprite('ak430_14', 2)	# 195-196
    sprite('ak430_15', 2)	# 197-198
    sprite('ak020_04', 3)	# 199-201
    sprite('ak020_05', 3)	# 202-204
    sprite('ak020_06', 3)	# 205-207
    label(11)
    sprite('ak020_07', 4)	# 208-211
    sprite('ak020_08', 4)	# 212-215
    loopRest()
    gotoLabel(11)
    label(99)
    sprite('ak408_07', 6)	# 216-221
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown8003(100, 1, 1)
    Unknown18009(1)
    sprite('ak408_08', 6)	# 222-227
    sprite('ak408_09', 8)	# 228-235
    sprite('ak408_10', 4)	# 236-239

@State
def CycloneUpperSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2500)
        AttackP2(90)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(0)
        Unknown30055('c0d401003c00000000000000')
        YImpluseBeforeWallbounce(2200)
        Hitstop(20)
        Unknown11056(0)
        Unknown11068(1)
        Unknown11062(1)
        Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
        Unknown2006()
        Unknown11064(1)
        Unknown11031(5)
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        if (SLOT_59 == 0):
            pass
        if (SLOT_59 == 1):
            SLOT_51 = 1
            Unknown11031(6)
        if (SLOT_59 == 2):
            SLOT_51 = 2
            Unknown11031(7)
        if (SLOT_59 == 3):
            SLOT_52 = 1
            Unknown11031(8)
        if (SLOT_59 == 4):
            SLOT_52 = 2
            Unknown11031(9)
        if (SLOT_59 >= 5):
            Hitstop(40)
            SLOT_53 = 1
            Unknown11031(10)

        def upon_78():
            if (not SLOT_57):
                Unknown11069('CycloneUpperSP')
                Unknown13024(0)
            else:
                Unknown11069('')
                Unknown13024(1)
                if (SLOT_59 >= 5):
                    Unknown13024(0)
                    physicsYImpulse(150000)
                    Unknown1019(45)
                    setGravity(2450)
            if SLOT_53:
                Unknown20000(1)
                Unknown20009(1000)
                ScreenShake(5000, 20000)
            if SLOT_56:
                Unknown20009(900)
        setInvincible(1)
    sprite('ak430_00', 2)	# 1-2
    tag_voice(1, 'pak252_0', 'pak252_1', '', '')
    sprite('ak430_01', 3)	# 3-5
    Unknown30080('')
    Unknown2036(33, -1, 0)
    Unknown2058(-10000)
    sprite('ak430_03', 30)	# 6-35
    sprite('ak430_04', 2)	# 36-37
    sprite('ak430_05', 2)	# 38-39
    sprite('ak430_06', 3)	# 40-42	 **attackbox here**
    physicsXImpulse(10000)
    RefreshMultihit()
    Unknown11072(1, 150000, 30000)
    Unknown8003(100, 1, 1)
    GFX_0('UltimateFirstPunch', 0)
    sprite('ak430_06', 3)	# 43-45	 **attackbox here**
    Unknown23027()
    sprite('ak430_07', 1)	# 46-46	 **attackbox here**
    Unknown1019(40)
    ScreenShake(1000, 8000)
    Unknown8001(1, 0)
    sprite('ak430_07', 1)	# 47-47	 **attackbox here**
    clearUponHandler(2)
    tag_voice(0, 'pak253_0', 'pak253_1', '', '')
    if SLOT_51:
        sendToLabel(1)
    elif SLOT_52:
        sendToLabel(2)
    elif SLOT_53:
        sendToLabel(3)
    loopRest()
    label(0)
    sprite('ak430_08', 1)	# 48-48	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(36000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 49-50	 **attackbox here**
    RefreshMultihit()
    Hitstop(10)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(6000)
    AirPushbackY(44000)
    setInvincible(0)
    SFX_3('slash_blade_fast')
    sprite('ak430_09', 5)	# 51-55	 **attackbox here**
    Unknown23027()
    sprite('ak430_10', 3)	# 56-58	 **attackbox here**
    sprite('ak430_12', 2)	# 59-60
    sendToLabelUpon(2, 9)
    YAccel(60)
    Unknown1019(80)
    Unknown1039(150)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 2)	# 61-62
    sprite('ak430_14', 2)	# 63-64
    sprite('ak430_15', 2)	# 65-66
    sprite('ak020_04', 3)	# 67-69
    sprite('ak020_05', 3)	# 70-72
    sprite('ak020_06', 3)	# 73-75
    label(8)
    Unknown1019(80)
    sprite('ak020_07', 4)	# 76-79
    sprite('ak020_08', 4)	# 80-83
    loopRest()
    gotoLabel(8)
    label(9)
    sprite('ak430_00', 2)	# 84-85
    Unknown1084(1)
    sprite('ak430_01', 2)	# 86-87
    sprite('ak430_03', 2)	# 88-89
    sprite('ak430_04', 2)	# 90-91
    sprite('ak430_05', 2)	# 92-93
    sprite('ak430_06', 2)	# 94-95	 **attackbox here**
    physicsXImpulse(15000)
    Unknown8003(100, 1, 1)
    GFX_0('UltimateFirstPunch', 0)
    sprite('ak430_07', 2)	# 96-97	 **attackbox here**
    Unknown1019(40)
    ScreenShake(1000, 8000)
    Unknown8001(1, 0)
    sprite('ak430_08', 1)	# 98-98	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(42000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 99-100	 **attackbox here**
    RefreshMultihit()
    Damage(3500)
    AttackP2(75)
    Unknown11091(18)
    AirPushbackY(52000)
    setInvincible(0)
    SFX_3('slash_blade_fast')
    SLOT_57 = 1
    Unknown11064(0)
    sprite('ak430_09', 5)	# 101-105	 **attackbox here**
    Unknown23027()
    sprite('ak430_10', 3)	# 106-108	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('ak430_08', 1)	# 109-109	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(36000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 110-111	 **attackbox here**
    RefreshMultihit()
    Hitstop(10)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(6000)
    AirPushbackY(36000)
    setInvincible(0)
    SFX_3('slash_blade_fast')
    sprite('ak430_09', 5)	# 112-116	 **attackbox here**
    Unknown23027()
    sprite('ak430_10', 3)	# 117-119	 **attackbox here**
    sprite('ak430_12', 2)	# 120-121
    sendToLabelUpon(2, 19)
    YAccel(60)
    Unknown1019(80)
    Unknown1039(150)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 2)	# 122-123
    sprite('ak430_14', 2)	# 124-125
    sprite('ak430_15', 2)	# 126-127
    sprite('ak020_04', 3)	# 128-130
    sprite('ak020_05', 3)	# 131-133
    sprite('ak020_06', 3)	# 134-136
    label(18)
    Unknown1019(80)
    sprite('ak020_07', 4)	# 137-140
    sprite('ak020_08', 4)	# 141-144
    loopRest()
    gotoLabel(18)
    label(19)
    sprite('ak430_00', 2)	# 145-146
    Unknown1084(1)
    sprite('ak430_01', 2)	# 147-148
    sprite('ak430_03', 2)	# 149-150
    sprite('ak430_04', 2)	# 151-152
    sprite('ak430_05', 2)	# 153-154
    sprite('ak430_06', 3)	# 155-157	 **attackbox here**
    physicsXImpulse(15000)
    RefreshMultihit()
    Damage(1500)
    Unknown11091(17)
    if (SLOT_59 == 2):
        Damage(1700)
    Unknown8003(100, 1, 1)
    GFX_0('UltimateFirstPunch', 0)
    sprite('ak430_07', 2)	# 158-159	 **attackbox here**
    Unknown1019(40)
    ScreenShake(1000, 8000)
    Unknown8001(1, 0)
    sprite('ak430_08', 1)	# 160-160	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(42000)
    setGravity(2000)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 161-162	 **attackbox here**
    RefreshMultihit()
    Hitstop(8)
    AirPushbackY(52000)
    sprite('ak430_08', 2)	# 163-164	 **attackbox here**
    SFX_3('slash_blade_fast')
    sprite('ak430_09', 5)	# 165-169	 **attackbox here**
    RefreshMultihit()
    SLOT_57 = 1
    Unknown11064(0)
    sprite('ak430_10', 3)	# 170-172	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('ak430_08', 1)	# 173-173	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(36000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 174-175	 **attackbox here**
    RefreshMultihit()
    Hitstop(10)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(6000)
    AirPushbackY(40000)
    setInvincible(0)
    SFX_3('slash_blade_fast')
    sprite('ak430_09', 5)	# 176-180	 **attackbox here**
    Unknown23027()
    sprite('ak430_10', 3)	# 181-183	 **attackbox here**
    sprite('ak430_12', 2)	# 184-185
    sendToLabelUpon(2, 29)
    YAccel(60)
    Unknown1019(80)
    Unknown1039(150)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 2)	# 186-187
    sprite('ak430_14', 2)	# 188-189
    sprite('ak430_15', 2)	# 190-191
    sprite('ak020_04', 3)	# 192-194
    sprite('ak020_05', 3)	# 195-197
    sprite('ak020_06', 3)	# 198-200
    label(28)
    Unknown1019(80)
    sprite('ak020_07', 4)	# 201-204
    sprite('ak020_08', 4)	# 205-208
    loopRest()
    gotoLabel(28)
    label(29)
    sprite('ak430_00', 2)	# 209-210
    Unknown1084(1)
    sprite('ak430_01', 2)	# 211-212
    sprite('ak430_03', 2)	# 213-214
    sprite('ak430_04', 2)	# 215-216
    sprite('ak430_05', 2)	# 217-218
    sprite('ak430_06', 3)	# 219-221	 **attackbox here**
    physicsXImpulse(15000)
    RefreshMultihit()
    Damage(600)
    AttackP2(97)
    if (SLOT_59 == 4):
        Damage(670)
    Unknown8003(100, 1, 1)
    GFX_0('UltimateFirstPunch', 0)
    sprite('ak430_07', 2)	# 222-223	 **attackbox here**
    Unknown1019(40)
    ScreenShake(1000, 8000)
    Unknown8001(1, 0)
    sprite('ak430_08', 1)	# 224-224	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(60000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 225-226	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    AirPushbackY(40000)
    sprite('ak430_08', 1)	# 227-227	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    sprite('ak430_08', 1)	# 228-228	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 229-229	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 230-230	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 231-231	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 232-232	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 1)	# 233-233	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_10', 3)	# 234-236	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(52000)
    SLOT_57 = 1
    Unknown11064(0)
    loopRest()
    gotoLabel(10)
    label(3)
    sprite('ak430_08', 1)	# 237-237	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(36000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 238-239	 **attackbox here**
    RefreshMultihit()
    Hitstop(10)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(6000)
    AirPushbackY(42000)
    setInvincible(0)
    SFX_3('slash_blade_fast')
    sprite('ak430_09', 5)	# 240-244	 **attackbox here**
    Unknown23027()
    sprite('ak430_10', 3)	# 245-247	 **attackbox here**
    sprite('ak430_12', 2)	# 248-249
    sendToLabelUpon(2, 36)
    YAccel(60)
    Unknown1019(80)
    Unknown1039(150)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 2)	# 250-251
    sprite('ak430_14', 2)	# 252-253
    sprite('ak430_15', 2)	# 254-255
    sprite('ak020_04', 3)	# 256-258
    sprite('ak020_05', 3)	# 259-261
    sprite('ak020_06', 3)	# 262-264
    label(35)
    Unknown1019(80)
    sprite('ak020_07', 4)	# 265-268
    sprite('ak020_08', 4)	# 269-272
    loopRest()
    gotoLabel(35)
    label(36)
    sprite('ak430_00', 2)	# 273-274
    Unknown1084(1)
    sprite('ak430_01', 2)	# 275-276
    sprite('ak430_03', 2)	# 277-278
    sprite('ak430_04', 2)	# 279-280
    sprite('ak430_05', 2)	# 281-282
    sprite('ak430_06', 3)	# 283-285	 **attackbox here**
    physicsXImpulse(15000)
    RefreshMultihit()
    Damage(500)
    AttackP2(97)
    Unknown8003(100, 1, 1)
    GFX_0('UltimateFirstPunch', 0)
    sprite('ak430_07', 2)	# 286-287	 **attackbox here**
    Unknown1019(40)
    ScreenShake(1000, 8000)
    Unknown8001(1, 0)
    sprite('ak430_08', 1)	# 288-288	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(48000)
    setGravity(2400)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 289-290	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    AirPushbackY(40000)
    sprite('ak430_08', 2)	# 291-292	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    sprite('ak430_09', 2)	# 293-294	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_09', 3)	# 295-297	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_10', 3)	# 298-300	 **attackbox here**
    RefreshMultihit()
    sprite('ak430_12', 2)	# 301-302
    sendToLabelUpon(2, 39)
    YAccel(60)
    Unknown1019(80)
    Unknown1039(150)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 2)	# 303-304
    sprite('ak430_14', 2)	# 305-306
    sprite('ak430_15', 2)	# 307-308
    sprite('ak020_04', 3)	# 309-311
    sprite('ak020_05', 3)	# 312-314
    sprite('ak020_06', 3)	# 315-317
    label(38)
    Unknown1019(80)
    sprite('ak020_07', 4)	# 318-321
    sprite('ak020_08', 4)	# 322-325
    loopRest()
    gotoLabel(38)
    label(39)
    sprite('ak408_07', 2)	# 326-327
    Unknown1084(1)
    Unknown8004(100, 1, 1)
    Unknown8003(100, 1, 1)
    SLOT_56 = 1
    sprite('ak408_08', 2)	# 328-329
    sprite('ak408_09', 4)	# 330-333
    sprite('ak408_10', 2)	# 334-335
    sprite('ak430_00', 2)	# 336-337
    sprite('ak430_01', 2)	# 338-339
    sprite('ak430_03', 6)	# 340-345
    sprite('ak430_04', 2)	# 346-347
    sprite('ak430_05', 2)	# 348-349
    sprite('ak430_06', 6)	# 350-355	 **attackbox here**
    physicsXImpulse(15000)
    RefreshMultihit()
    Damage(2200)
    AttackP2(95)
    Unknown11091(23)
    AirUntechableTime(200)
    Hitstop(25)
    AirPushbackY(74000)
    Unknown8003(100, 1, 1)
    GFX_0('UltimateFirstPunch', 0)
    sprite('ak430_07', 2)	# 356-357	 **attackbox here**
    Unknown1019(40)
    ScreenShake(1000, 8000)
    Unknown8001(1, 0)
    tag_voice(0, 'pak251_0', 'pak251_1', '', '')
    sprite('ak430_08', 1)	# 358-358	 **attackbox here**
    SFX_3('slash_blade_middle')
    Unknown1019(200)
    physicsYImpulse(84000)
    setGravity(2000)
    GFX_0('UltimateUpperFistAura', 0)
    GFX_0('UltimateUpperWind', 100)
    GFX_0('UltimateUpperSmoke', 104)
    GFX_0('UltimateTodomeUpper', 100)
    sprite('ak430_08', 2)	# 359-360	 **attackbox here**
    Unknown2037(1)
    RefreshMultihit()
    AirUntechableTime(200)
    Unknown9310(35)
    AirPushbackX(-1000)
    AirPushbackY(62000)
    YImpluseBeforeWallbounce(1200)
    Unknown30056('400d03006400000000000000')
    Unknown11050('02000000556c74696d61746550756e636853756363657373000000000000000000000000')
    SLOT_57 = 1
    Unknown11064(0)
    sprite('ak430_08', 2)	# 361-362	 **attackbox here**
    SFX_3('slash_blade_fast')
    SLOT_56 = 0
    sprite('ak430_09', 5)	# 363-367	 **attackbox here**
    YAccel(80)
    sprite('ak430_10', 3)	# 368-370	 **attackbox here**
    sprite('ak430_12', 3)	# 371-373
    sendToLabelUpon(2, 5)
    Unknown1019(80)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 3)	# 374-376
    sprite('ak430_14', 3)	# 377-379
    sprite('ak430_15', 3)	# 380-382
    sprite('ak020_04', 3)	# 383-385
    sprite('ak020_05', 3)	# 386-388
    sprite('ak020_06', 3)	# 389-391
    label(4)
    sprite('ak020_07', 4)	# 392-395
    sprite('ak020_08', 4)	# 396-399
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('ak210_09', 12)	# 400-411
    Unknown1084(1)
    Unknown20001(1)
    ScreenShake(5000, 30000)
    Unknown8000(100, 1, 1)
    Unknown8003(100, 1, 1)
    sprite('ak210_10', 22)	# 412-433
    Unknown13024(1)

    def upon_3():
        if (not SLOT_158):
            clearUponHandler(3)
            Unknown20000(0)
    sprite('ak210_11', 8)	# 434-441
    sprite('ak210_12', 6)	# 442-447
    sprite('ak210_13', 6)	# 448-453
    ExitState()
    label(10)
    sprite('ak430_12', 2)	# 454-455
    sendToLabelUpon(2, 99)
    YAccel(60)
    Unknown1019(80)
    Unknown26('UltimateUpperFistAura')
    GFX_1('akef_431_fistaura_end', 0)
    Unknown21015('556c74696d617465546f646f6d65557070657200000000000000000000000000cd10000000000000')
    sprite('ak430_13', 2)	# 456-457
    sprite('ak430_14', 2)	# 458-459
    sprite('ak430_15', 2)	# 460-461
    sprite('ak020_04', 3)	# 462-464
    sprite('ak020_05', 3)	# 465-467
    sprite('ak020_06', 3)	# 468-470
    label(11)
    Unknown1019(80)
    sprite('ak020_07', 4)	# 471-474
    sprite('ak020_08', 4)	# 475-478
    loopRest()
    gotoLabel(11)
    label(99)
    sprite('ak408_07', 6)	# 479-484
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown8003(100, 1, 1)
    Unknown18009(1)
    sprite('ak408_08', 6)	# 485-490
    sprite('ak408_09', 8)	# 491-498
    sprite('ak408_10', 4)	# 499-502

@State
def Mahajiodain():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        Unknown48('0b000000020000000600000019000000020000001f000000')

        def upon_43():
            if (SLOT_48 == 4401):
                setInvincible(0)
        setInvincible(1)
    sprite('ak432_00', 3)	# 1-3
    sprite('ak432_00', 1)	# 4-4
    Unknown30080('')
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    tag_voice(1, 'pak256_0', 'pak256_1', '', '')
    sprite('ak432_01', 4)	# 5-8
    sprite('ak432_02', 4)	# 9-12
    sprite('ak432_03', 4)	# 13-16
    sprite('ak432_04', 4)	# 17-20
    sprite('ak432_05', 4)	# 21-24
    Unknown23029(11, 4320, 0)
    sprite('ak432_06', 36)	# 25-60
    SFX_3('ak050')
    sprite('ak432_07', 4)	# 61-64
    Unknown23118(-6921066)
    Unknown23119(-13495246, 4, -1)
    Unknown4048(45000)
    Unknown4045('706572736f6e615f656e7465725f70330000000000000000000000000000000000000000')
    SFX_3('ak051')
    sprite('ak432_08', 4)	# 65-68
    SFX_0('persona_destroy')
    sprite('ak432_09', 5)	# 69-73
    tag_voice(0, '', 'pak257_1', '', '')
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 74-78
    sprite('ak432_11', 5)	# 79-83
    sprite('ak432_09', 5)	# 84-88
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 89-93
    sprite('ak432_11', 5)	# 94-98
    sprite('ak432_09', 5)	# 99-103
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 104-108
    sprite('ak432_11', 5)	# 109-113
    sprite('ak432_09', 5)	# 114-118
    tag_voice(0, 'pak257_0', '', '', '')
    SFX_3('cloth_m')
    Unknown23119(-16777216, 8, 1)
    sprite('ak432_10', 5)	# 119-123
    sprite('ak432_11', 5)	# 124-128
    sprite('ak432_12', 5)	# 129-133
    sprite('ak432_01', 5)	# 134-138
    sprite('ak432_00', 5)	# 139-143

@State
def MahajiodainSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        callSubroutine('CycloneLvIcon')
        if (not SLOT_59):
            Unknown23004(0, 1)
        Unknown48('0b000000020000000600000019000000020000001f000000')
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4401):
                setInvincible(0)
    sprite('ak432_00', 3)	# 1-3
    sprite('ak432_00', 1)	# 4-4
    Unknown30080('')
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    tag_voice(1, 'pak256_0', 'pak256_1', '', '')
    sprite('ak432_01', 4)	# 5-8
    sprite('ak432_02', 4)	# 9-12
    sprite('ak432_03', 4)	# 13-16
    sprite('ak432_04', 4)	# 17-20
    sprite('ak432_05', 4)	# 21-24
    Unknown23029(11, 4321, 0)
    sprite('ak432_06', 36)	# 25-60
    SFX_3('ak050')
    sprite('ak432_07', 4)	# 61-64
    Unknown23118(-6921066)
    Unknown23119(-13495246, 4, -1)
    Unknown4048(45000)
    Unknown4045('706572736f6e615f656e7465725f70330000000000000000000000000000000000000000')
    SFX_3('ak051')
    sprite('ak432_08', 4)	# 65-68
    SFX_0('persona_destroy')
    sprite('ak432_09', 5)	# 69-73
    tag_voice(0, '', 'pak258_1', '', '')
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 74-78
    sprite('ak432_11', 5)	# 79-83
    sprite('ak432_09', 5)	# 84-88
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 89-93
    sprite('ak432_11', 5)	# 94-98
    sprite('ak432_09', 5)	# 99-103
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 104-108
    sprite('ak432_11', 5)	# 109-113
    sprite('ak432_09', 5)	# 114-118
    tag_voice(0, 'pak258_0', '', '', '')
    SFX_3('cloth_m')
    Unknown23119(-16777216, 8, 1)
    sprite('ak432_10', 5)	# 119-123
    sprite('ak432_11', 5)	# 124-128
    sprite('ak432_09', 5)	# 129-133
    SFX_3('cloth_m')
    sprite('ak432_10', 5)	# 134-138
    sprite('ak432_11', 5)	# 139-143
    sprite('ak432_12', 5)	# 144-148
    sprite('ak432_01', 5)	# 149-153
    sprite('ak432_00', 5)	# 154-158

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(5000)
        Unknown11091(100)
        Hitstop(20)
        Unknown11064(1)
        AirUntechableTime(10000)
        Unknown9310(10000)
        AirPushbackX(0)
        AirPushbackY(-100000)

        def upon_43():
            if (SLOT_48 == 4501):
                setInvincible(1)
                Unknown23083(1)
                Unknown23084(1)
                Unknown23088(1, 1)
                GFX_0('IchigekiCamera', 100)
                Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000a911000000000000')
                Unknown21015('506572736f6e614963686967656b6900000000000000000000000000000000009f11000000000000')
                Unknown23157(1)
                tag_voice(0, 'pak291_0', 'pak291_1', '', '')
                sendToLabel(0)
            if (SLOT_48 == 4502):
                sendToLabel(1)
            if (SLOT_48 == 4503):
                sendToLabel(2)
            if (SLOT_48 == 4504):
                sendToLabel(3)
            if (SLOT_48 == 4505):
                sendToLabel(4)
        clearUponHandler(2)
        sendToLabelUpon(2, 8)
    sprite('ak450_00', 4)	# 1-4
    setInvincible(1)
    Unknown2036(92, -1, 2)
    Unknown23147()
    tag_voice(1, 'pak290_0', 'pak290_1', '', '')
    Unknown2017(0)
    GFX_0('P4U_Cutin_Parent', 100)
    sprite('ak450_01', 4)	# 5-8
    sprite('ak450_02', 4)	# 9-12
    sprite('ak450_03', 4)	# 13-16
    sprite('ak450_04', 6)	# 17-22
    sprite('ak450_05', 6)	# 23-28
    Unknown23029(11, 4500, 0)
    sprite('ak450_06', 6)	# 29-34
    SFX_3('ak050')
    sprite('ak450_07', 6)	# 35-40
    sprite('ak450_08', 6)	# 41-46
    sprite('ak450_11', 6)	# 47-52
    sprite('ak450_12', 6)	# 53-58
    sprite('ak450_08', 6)	# 59-64
    sprite('ak450_11', 6)	# 65-70
    sprite('ak450_09', 2)	# 71-72
    SFX_3('ak051')
    Unknown4048(65000)
    Unknown4054(11)
    Unknown4045('706572736f6e615f656e7465725f70330000000000000000000000000000000000000000')
    sprite('ak450_09', 6)	# 73-78
    SFX_0('persona_destroy')
    sprite('ak450_10', 4)	# 79-82
    sprite('ak450_11', 6)	# 83-88
    sprite('ak450_12', 6)	# 89-94
    sprite('ak450_08', 6)	# 95-100
    sprite('ak450_11', 6)	# 101-106
    sprite('ak450_12', 6)	# 107-112
    sprite('ak450_08', 6)	# 113-118
    sprite('ak450_11', 6)	# 119-124
    sprite('ak450_12', 6)	# 125-130
    sprite('ak450_08', 6)	# 131-136
    sprite('ak450_11', 6)	# 137-142
    setInvincible(0)
    sprite('ak450_12', 6)	# 143-148
    sprite('ak450_08', 6)	# 149-154
    sprite('ak450_11', 6)	# 155-160
    sprite('ak450_12', 6)	# 161-166
    sprite('ak450_08', 6)	# 167-172
    sprite('ak450_11', 6)	# 173-178
    sprite('ak450_12', 6)	# 179-184
    sprite('ak450_08', 6)	# 185-190
    sprite('ak450_06', 6)	# 191-196
    sprite('ak450_05', 6)	# 197-202
    sprite('ak450_04', 6)	# 203-208
    sprite('ak450_03', 6)	# 209-214
    sprite('ak450_02', 6)	# 215-220
    sprite('ak450_01', 6)	# 221-226
    sprite('ak450_00', 6)	# 227-232
    ExitState()
    label(0)
    sprite('keep', 32767)	# 233-32999
    label(1)
    sprite('keep', 32767)	# 33000-65766
    GFX_0('Groundglobe', 103)
    Unknown1000(0)
    teleportRelativeY(3600000)
    physicsXImpulse(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(1800000)
    physicsXImpulse(0)
    physicsYImpulse(-60000)
    setGravity(2000)
    Unknown35()
    Unknown21015('50414b5f506572736f6e614963686967656b6900000000000000000000000000a011000000000000')
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000aa11000000000000')
    label(2)
    sprite('ak450_13', 40)	# 65767-65806
    GFX_0('Ichigekibeam', 100)
    teleportRelativeY(3600000)
    sprite('ak450_13', 3)	# 65807-65809
    physicsYImpulse(-10000)
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000ab11000000000000')
    label(9)
    sprite('ak450_14', 3)	# 65810-65812
    sprite('ak450_13', 3)	# 65813-65815
    loopRest()
    gotoLabel(9)
    label(3)
    sprite('ak450_13', 3)	# 65816-65818
    Unknown2017(0)
    teleportRelativeY(3000000)
    physicsYImpulse(-100000)
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000ac11000000000000')
    tag_voice(0, 'pak292_0', 'pak292_1', '', '')
    sprite('ak450_14', 3)	# 65819-65821
    sprite('ak450_13', 3)	# 65822-65824
    sprite('ak450_14', 3)	# 65825-65827
    sprite('ak450_13', 3)	# 65828-65830
    sprite('ak450_14', 3)	# 65831-65833
    sprite('ak450_13', 3)	# 65834-65836
    sprite('ak450_14', 3)	# 65837-65839
    sprite('ak450_13', 3)	# 65840-65842
    sprite('ak450_14', 3)	# 65843-65845
    sprite('ak450_13', 3)	# 65846-65848
    label(8)
    sprite('ak450_16', 7)	# 65849-65855	 **attackbox here**
    GFX_0('Ichigekiimpact', 100)
    RefreshMultihit()
    Damage(15000)
    ScreenShake(20000, 20000)
    SFX_3('ak001')
    sprite('ak450_16', 4)	# 65856-65859	 **attackbox here**
    ScreenShake(10000, 10000)
    sprite('ak450_16', 4)	# 65860-65863	 **attackbox here**
    ScreenShake(10000, 10000)
    sprite('ak450_17', 4)	# 65864-65867
    ScreenShake(10000, 20000)
    sprite('ak450_17', 4)	# 65868-65871
    ScreenShake(10000, 20000)
    sprite('ak450_18', 4)	# 65872-65875
    ScreenShake(15000, 30000)
    sprite('ak450_18', 4)	# 65876-65879
    ScreenShake(15000, 30000)
    sprite('ak450_19', 3)	# 65880-65882
    ScreenShake(15000, 40000)
    sprite('ak450_19', 3)	# 65883-65885
    ScreenShake(15000, 40000)
    sprite('ak450_20', 3)	# 65886-65888
    ScreenShake(20000, 50000)
    sprite('ak450_20', 3)	# 65889-65891
    ScreenShake(20000, 50000)
    sprite('ak450_21', 3)	# 65892-65894
    ScreenShake(20000, 60000)
    Unknown26('Ichigekibeam')
    sprite('ak450_21', 3)	# 65895-65897
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000ad11000000000000')
    Unknown3038(1)
    Unknown36(22)
    Unknown3038(1)
    Unknown35()
    sprite('ak450_21', 10)	# 65898-65907
    GFX_0('IchigekiPicture', 100)
    sprite('ak450_21', 10)	# 65908-65917
    SFX_3('blaze_normal')
    sprite('ak450_21', 8)	# 65918-65925
    SFX_3('blaze_normal')
    sprite('ak450_21', 8)	# 65926-65933
    SFX_3('blaze_normal')
    sprite('ak450_21', 8)	# 65934-65941
    SFX_3('blaze_normal')
    sprite('ak450_21', 6)	# 65942-65947
    SFX_3('blaze_normal')
    sprite('ak450_21', 8)	# 65948-65955
    SFX_3('blaze_normal')
    sprite('ak450_21', 8)	# 65956-65963
    SFX_3('blaze_normal')
    sprite('ak450_21', 8)	# 65964-65971
    SFX_3('blaze_normal')
    sprite('ak450_21', 8)	# 65972-65979
    SFX_3('blaze_long')
    sprite('ak450_21', 8)	# 65980-65987
    SFX_3('blaze_long')
    sprite('ak450_21', 8)	# 65988-65995
    SFX_3('blaze_long')
    sprite('ak450_21', 8)	# 65996-66003
    SFX_3('blaze_long')
    sprite('ak450_21', 4)	# 66004-66007
    SFX_3('blaze_long')
    sprite('ak450_21', 10)	# 66008-66017
    Unknown21015('47726f756e64676c6f6265000000000000000000000000000000000000000000b311000000000000')
    sprite('ak450_16', 45)	# 66018-66062	 **attackbox here**
    GFX_0('450burst', 100)
    sprite('ak450_16', 80)	# 66063-66142	 **attackbox here**
    RefreshMultihit()
    Damage(17240)
    Unknown11064(3)
    SFX_3('blaze_long')
    SFX_3('bomb_m')
    SFX_3('bomb_l')
    SFX_3('ak001')
    sprite('ak450_16', 32767)	# 66143-98909	 **attackbox here**
    Unknown36(22)
    Unknown1000(1500000)
    teleportRelativeY(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown35()
    Unknown21015('50414b5f506572736f6e614963686967656b6900000000000000000000000000a111000000000000')
    label(4)
    sprite('keep', 10)	# 98910-98919
    sprite('keep', 1)	# 98920-98920
    Unknown3038(0)
    Unknown23024(0)
    sprite('ak450_22', 60)	# 98921-98980
    Unknown18010()
    sprite('ak450_22', 30)	# 98981-99010
    sprite('ak450_22', 30)	# 99011-99040
    tag_voice(0, 'pak293_0', 'pak293_1', '', '')
    sprite('ak450_23', 6)	# 99041-99046
    sprite('ak450_23', 6)	# 99047-99052
    sprite('ak450_24', 6)	# 99053-99058
    sprite('ak450_25', 6)	# 99059-99064
    sprite('ak450_26', 6)	# 99065-99070
    sprite('ak450_27', 6)	# 99071-99076
    sprite('ak450_29', 6)	# 99077-99082
    sprite('ak450_30', 32767)	# 99083-131849
    Unknown18008()

@Subroutine
def MouthTableInit():
    Unknown18011('pak000', 12643, 12641, 25396, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak500', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak501', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak502', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak503', 12643, 13665, 13667, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak504', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak506', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak507', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak520', 12643, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak521', 12643, 14177, 14179, 14177, 13923, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak522', 14179, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak524', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak403_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak403_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak600baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak600bmk', 12643, 14177, 14435, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak600btg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak600pag', 12643, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak600pmi', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak600uwa', 12643, 12641, 25397, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak601bha', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak601pce', 12643, 14177, 13155, 24885, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak601ryn', 12643, 14177, 14179, 14177, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13618, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak601uca', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak601umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak602pag', 12643, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak603umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak604umi', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak700baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak700bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak700pce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak700ryn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak700umi', 12643, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak700uwa', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak701bmk', 12643, 12897, 25392, 12849, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak701btg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak701pag', 12643, 12641, 25394, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak701pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak701uca', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak702pce', 12643, 12641, 25397, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pak702ryn', 12643, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('baz')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('btg')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pag')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('ak601_00', 6)	# 2-7
    teleportRelativeY(0)
    Unknown1000(-1155000)
    sprite('ak601_01', 6)	# 8-13
    if random_(2, 0, 50):
        Unknown2037(1)
        Unknown7006('pak501', 100, 896229744, 12848, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown7006('pak500', 100, 896229744, 14128, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ak601_02', 5)	# 14-18
    sprite('ak601_02', 1)	# 19-19
    if SLOT_2:
        sendToLabel(2)
    label(1)
    sprite('ak601_00', 6)	# 20-25
    sprite('ak601_01', 6)	# 26-31
    sprite('ak601_02', 6)	# 32-37
    if SLOT_97:
        _gotolabel(1)
    label(2)
    sprite('ak601_03', 6)	# 38-43
    sprite('ak601_04', 6)	# 44-49
    sprite('ak601_05', 8)	# 50-57
    sprite('ak601_06', 4)	# 58-61
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak601_07', 8)	# 62-69
    sprite('ak601_08', 6)	# 70-75
    sprite('ak601_09', 2)	# 76-77
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 78-79
    sprite('ak033_01', 1)	# 80-80
    sprite('ak033_01', 2)	# 81-82
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 83-85
    sprite('ak033_03', 3)	# 86-88
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    Unknown1000(-1230000)
    sprite('ak033_04', 3)	# 89-91
    sprite('ak033_00', 3)	# 92-94
    Unknown23018(1)
    label(3)
    sprite('ak000_00', 6)	# 95-100
    sprite('ak000_01', 6)	# 101-106
    sprite('ak000_02', 6)	# 107-112
    sprite('ak000_03', 6)	# 113-118
    sprite('ak000_04', 6)	# 119-124
    sprite('ak000_05', 6)	# 125-130
    sprite('ak000_06', 6)	# 131-136
    sprite('ak000_07', 6)	# 137-142
    sprite('ak000_08', 6)	# 143-148
    sprite('ak000_09', 6)	# 149-154
    loopRest()
    gotoLabel(3)
    ExitState()
    label(10)
    sprite('ak600_00', 6)	# 155-160
    teleportRelativeY(150000)
    GFX_0('akef_entry_shadows', 100)
    sprite('ak600_01', 6)	# 161-166
    Unknown7006('pak503', 100, 896229744, 13360, 0, 0, 100, 896229744, 13616, 0, 0, 100, 896229744, 13872, 0, 0, 100)
    sprite('ak600_02', 6)	# 167-172
    label(11)
    sprite('ak600_00', 6)	# 173-178
    sprite('ak600_01', 6)	# 179-184
    sprite('ak600_02', 6)	# 185-190
    if SLOT_97:
        _gotolabel(11)
    sprite('ak600_03', 4)	# 191-194
    sprite('ak600_04', 8)	# 195-202
    sendToLabelUpon(2, 13)
    label(12)
    sprite('ak600_05', 6)	# 203-208
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)
    setGravity(0)
    sprite('ak600_06', 6)	# 209-214
    gotoLabel(12)
    label(13)
    sprite('ak600_07', 6)	# 215-220
    Unknown1084(1)
    Unknown8000(0, 1, 1)
    sprite('ak600_08', 20)	# 221-240
    sprite('ak600_09', 6)	# 241-246
    sprite('ak600_10', 6)	# 247-252
    sprite('ak600_11', 6)	# 253-258
    SFX_3('hit_m_fast')
    sprite('ak600_12', 6)	# 259-264
    sprite('ak600_13', 6)	# 265-270
    SFX_3('damage_hit_mh')
    Unknown26('akef_entry_shadows')
    GFX_0('akef_entry_shadows_clash', 100)
    GFX_1('ef_hit_blowm', 0)
    physicsXImpulse(10000)
    sprite('ak600_14', 6)	# 271-276
    sprite('ak600_15', 3)	# 277-279
    sprite('ak600_15', 3)	# 280-282
    Unknown1019(0)
    sprite('ak600_16', 6)	# 283-288
    sprite('ak600_17', 6)	# 289-294
    sprite('ak600_18', 6)	# 295-300
    sprite('ak600_19', 6)	# 301-306
    sprite('ak600_20', 6)	# 307-312
    sprite('ak600_21', 6)	# 313-318
    sprite('ak600_22', 6)	# 319-324
    sprite('ak600_21', 6)	# 325-330
    sprite('ak600_22', 6)	# 331-336
    sprite('ak404_11', 8)	# 337-344
    sprite('ak404_12', 6)	# 345-350
    SFX_3('ak002')
    sprite('ak404_13', 8)	# 351-358
    Unknown23018(1)
    label(14)
    sprite('ak000_00', 6)	# 359-364
    sprite('ak000_01', 6)	# 365-370
    sprite('ak000_02', 6)	# 371-376
    sprite('ak000_03', 6)	# 377-382
    sprite('ak000_04', 6)	# 383-388
    sprite('ak000_05', 6)	# 389-394
    sprite('ak000_06', 6)	# 395-400
    sprite('ak000_07', 6)	# 401-406
    sprite('ak000_08', 6)	# 407-412
    sprite('ak000_09', 6)	# 413-418
    loopRest()
    gotoLabel(14)
    ExitState()
    label(20)
    sprite('ak601_00', 1)	# 419-419
    SFX_1('pak702ryn')
    label(21)
    sprite('ak601_00', 6)	# 420-425
    sprite('ak601_01', 6)	# 426-431
    sprite('ak601_02', 6)	# 432-437
    loopRest()
    gotoLabel(21)
    ExitState()
    label(991)
    sprite('ak000_00', 1)	# 438-438
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ak000_00', 6)	# 439-444
    sprite('ak000_01', 6)	# 445-450
    sprite('ak000_02', 6)	# 451-456
    sprite('ak000_03', 6)	# 457-462
    sprite('ak000_04', 6)	# 463-468
    sprite('ak000_05', 6)	# 469-474
    sprite('ak000_06', 6)	# 475-480
    sprite('ak000_07', 6)	# 481-486
    sprite('ak000_08', 6)	# 487-492
    sprite('ak000_09', 6)	# 493-498
    loopRest()
    gotoLabel(992)
    label(100)
    sprite('ak642_00', 6)	# 499-504
    if SLOT_158:
        Unknown1000(-1155000)
    else:
        Unknown1000(-1155000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('pak601pce')
        sendToLabel(102)
    Unknown2019(500)
    sprite('ak642_01', 6)	# 505-510
    sprite('ak642_02', 6)	# 511-516
    label(101)
    sprite('ak642_00', 6)	# 517-522
    sprite('ak642_01', 6)	# 523-528
    sprite('ak642_02', 6)	# 529-534
    gotoLabel(101)
    label(102)
    sprite('ak642_00', 6)	# 535-540
    sprite('ak642_01', 6)	# 541-546
    sprite('ak642_02', 6)	# 547-552
    if SLOT_97:
        _gotolabel(102)
    sprite('ak642_03', 6)	# 553-558
    sprite('ak642_04', 6)	# 559-564
    sprite('ak642_05', 8)	# 565-572
    sprite('ak642_06', 4)	# 573-576
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak642_07', 8)	# 577-584
    sprite('ak642_08', 6)	# 585-590
    sprite('ak601_09', 2)	# 591-592
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 593-594
    sprite('ak033_01', 1)	# 595-595
    sprite('ak033_01', 2)	# 596-597
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 598-600
    sprite('ak033_03', 3)	# 601-603
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 604-606
    sprite('ak033_00', 3)	# 607-609
    Unknown23018(1)
    label(103)
    sprite('ak000_00', 6)	# 610-615
    sprite('ak000_01', 6)	# 616-621
    sprite('ak000_02', 6)	# 622-627
    sprite('ak000_03', 6)	# 628-633
    sprite('ak000_04', 6)	# 634-639
    sprite('ak000_05', 6)	# 640-645
    sprite('ak000_06', 6)	# 646-651
    sprite('ak000_07', 6)	# 652-657
    sprite('ak000_08', 6)	# 658-663
    sprite('ak000_09', 6)	# 664-669
    loopRest()
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('ak644_00', 32767)	# 670-33436
    if SLOT_158:
        Unknown1000(-1500000)
    else:
        Unknown1000(-1500000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('pak601umi')
        sendToLabel(111)
    Unknown2019(-500)
    label(111)
    sprite('ak644_00', 1)	# 33437-33437
    if SLOT_97:
        _gotolabel(111)
    sprite('ak644_00', 20)	# 33438-33457
    sprite('ak644_00', 20)	# 33458-33477
    SFX_1('pak603umi')
    Unknown21007(24, 40)
    sprite('ak644_01', 6)	# 33478-33483
    sprite('ak644_02', 6)	# 33484-33489
    sprite('ak644_03', 6)	# 33490-33495
    sprite('ak644_04', 6)	# 33496-33501
    sprite('ak644_05', 6)	# 33502-33507
    SFX_0('100_hit_grap_3')
    GFX_0('pak644_wind_3D', 0)
    GFX_0('pak644_wind', 1)
    label(112)
    sprite('ak644_06', 6)	# 33508-33513
    sprite('ak644_07', 6)	# 33514-33519
    sprite('ak644_08', 6)	# 33520-33525
    sprite('ak644_09', 6)	# 33526-33531
    if SLOT_97:
        _gotolabel(112)
    sprite('ak644_06', 6)	# 33532-33537
    sprite('ak644_07', 6)	# 33538-33543
    sprite('ak644_08', 6)	# 33544-33549
    sprite('ak644_09', 6)	# 33550-33555
    sprite('ak644_06', 6)	# 33556-33561
    sprite('ak644_07', 6)	# 33562-33567
    sprite('ak644_08', 6)	# 33568-33573
    SFX_1('pak604umi')
    Unknown23018(1)
    sprite('ak644_09', 6)	# 33574-33579
    label(113)
    sprite('ak644_06', 6)	# 33580-33585
    sprite('ak644_07', 6)	# 33586-33591
    sprite('ak644_08', 6)	# 33592-33597
    sprite('ak644_09', 6)	# 33598-33603
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('ak601_00', 6)	# 33604-33609
    if SLOT_158:
        Unknown1000(-1155000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(0)
    sprite('ak601_01', 6)	# 33610-33615
    SFX_1('pak600baz')
    sprite('ak601_02', 6)	# 33616-33621
    label(121)
    sprite('ak601_00', 6)	# 33622-33627
    sprite('ak601_01', 6)	# 33628-33633
    sprite('ak601_02', 6)	# 33634-33639
    if SLOT_97:
        _gotolabel(121)
    sprite('ak601_03', 6)	# 33640-33645
    sprite('ak601_04', 6)	# 33646-33651
    sprite('ak601_05', 8)	# 33652-33659
    sprite('ak601_06', 4)	# 33660-33663
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak601_07', 8)	# 33664-33671
    sprite('ak601_08', 6)	# 33672-33677
    sprite('ak601_09', 2)	# 33678-33679
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 33680-33681
    sprite('ak033_01', 1)	# 33682-33682
    sprite('ak033_01', 2)	# 33683-33684
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 33685-33687
    sprite('ak033_03', 3)	# 33688-33690
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 33691-33693
    sprite('ak033_00', 3)	# 33694-33696
    Unknown21007(24, 40)
    Unknown21011(270)
    label(122)
    sprite('ak000_00', 6)	# 33697-33702
    sprite('ak000_01', 6)	# 33703-33708
    sprite('ak000_02', 6)	# 33709-33714
    sprite('ak000_03', 6)	# 33715-33720
    sprite('ak000_04', 6)	# 33721-33726
    sprite('ak000_05', 6)	# 33727-33732
    sprite('ak000_06', 6)	# 33733-33738
    sprite('ak000_07', 6)	# 33739-33744
    sprite('ak000_08', 6)	# 33745-33750
    sprite('ak000_09', 6)	# 33751-33756
    loopRest()
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('ak601_00', 6)	# 33757-33762
    if SLOT_158:
        Unknown1000(-1155000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(0)
    sprite('ak601_01', 6)	# 33763-33768
    SFX_1('pak600bmk')
    sprite('ak601_02', 6)	# 33769-33774
    label(131)
    sprite('ak601_00', 6)	# 33775-33780
    sprite('ak601_01', 6)	# 33781-33786
    sprite('ak601_02', 6)	# 33787-33792
    if SLOT_97:
        _gotolabel(131)
    sprite('ak601_03', 6)	# 33793-33798
    sprite('ak601_04', 6)	# 33799-33804
    sprite('ak601_05', 8)	# 33805-33812
    sprite('ak601_06', 4)	# 33813-33816
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak601_07', 8)	# 33817-33824
    sprite('ak601_08', 6)	# 33825-33830
    sprite('ak601_09', 2)	# 33831-33832
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 33833-33834
    sprite('ak033_01', 1)	# 33835-33835
    sprite('ak033_01', 2)	# 33836-33837
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 33838-33840
    sprite('ak033_03', 3)	# 33841-33843
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 33844-33846
    sprite('ak033_00', 3)	# 33847-33849
    Unknown21007(24, 40)
    Unknown21011(230)
    label(132)
    sprite('ak000_00', 6)	# 33850-33855
    sprite('ak000_01', 6)	# 33856-33861
    sprite('ak000_02', 6)	# 33862-33867
    sprite('ak000_03', 6)	# 33868-33873
    sprite('ak000_04', 6)	# 33874-33879
    sprite('ak000_05', 6)	# 33880-33885
    sprite('ak000_06', 6)	# 33886-33891
    sprite('ak000_07', 6)	# 33892-33897
    sprite('ak000_08', 6)	# 33898-33903
    sprite('ak000_09', 6)	# 33904-33909
    loopRest()
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('ak601_00', 6)	# 33910-33915
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(0)
    sprite('ak601_01', 6)	# 33916-33921
    SFX_1('pak600btg')
    sprite('ak601_02', 6)	# 33922-33927
    label(141)
    sprite('ak601_00', 6)	# 33928-33933
    sprite('ak601_01', 6)	# 33934-33939
    sprite('ak601_02', 6)	# 33940-33945
    if SLOT_97:
        _gotolabel(141)
    sprite('ak601_03', 6)	# 33946-33951
    sprite('ak601_04', 6)	# 33952-33957
    sprite('ak601_05', 8)	# 33958-33965
    sprite('ak601_06', 4)	# 33966-33969
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak601_07', 8)	# 33970-33977
    sprite('ak601_08', 6)	# 33978-33983
    sprite('ak601_09', 2)	# 33984-33985
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 33986-33987
    sprite('ak033_01', 1)	# 33988-33988
    sprite('ak033_01', 2)	# 33989-33990
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 33991-33993
    sprite('ak033_03', 3)	# 33994-33996
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 33997-33999
    sprite('ak033_00', 3)	# 34000-34002
    Unknown21007(24, 40)
    Unknown21011(240)
    label(142)
    sprite('ak000_00', 6)	# 34003-34008
    sprite('ak000_01', 6)	# 34009-34014
    sprite('ak000_02', 6)	# 34015-34020
    sprite('ak000_03', 6)	# 34021-34026
    sprite('ak000_04', 6)	# 34027-34032
    sprite('ak000_05', 6)	# 34033-34038
    sprite('ak000_06', 6)	# 34039-34044
    sprite('ak000_07', 6)	# 34045-34050
    sprite('ak000_08', 6)	# 34051-34056
    sprite('ak000_09', 6)	# 34057-34062
    loopRest()
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('ak601_00', 6)	# 34063-34068
    if SLOT_158:
        Unknown1000(-1155000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(153)
    sprite('ak601_01', 6)	# 34069-34074
    SFX_1('pak600pag')
    sprite('ak601_02', 6)	# 34075-34080
    label(151)
    sprite('ak601_00', 6)	# 34081-34086
    sprite('ak601_01', 6)	# 34087-34092
    sprite('ak601_02', 6)	# 34093-34098
    if SLOT_97:
        _gotolabel(151)
    sprite('ak601_00', 6)	# 34099-34104
    sprite('ak601_01', 6)	# 34105-34110
    sprite('ak601_02', 6)	# 34111-34116
    sprite('ak601_00', 6)	# 34117-34122
    Unknown21007(24, 40)
    sprite('ak601_01', 6)	# 34123-34128
    sprite('ak601_02', 6)	# 34129-34134
    label(152)
    sprite('ak601_00', 6)	# 34135-34140
    sprite('ak601_01', 6)	# 34141-34146
    sprite('ak601_02', 6)	# 34147-34152
    gotoLabel(152)
    label(153)
    sprite('ak601_03', 6)	# 34153-34158
    SFX_1('pak602pag')
    sprite('ak601_04', 6)	# 34159-34164
    sprite('ak601_05', 8)	# 34165-34172
    sprite('ak601_06', 4)	# 34173-34176
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak601_07', 8)	# 34177-34184
    sprite('ak601_08', 6)	# 34185-34190
    sprite('ak601_09', 2)	# 34191-34192
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 34193-34194
    sprite('ak033_01', 1)	# 34195-34195
    sprite('ak033_01', 2)	# 34196-34197
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 34198-34200
    sprite('ak033_03', 3)	# 34201-34203
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 34204-34206
    sprite('ak033_00', 3)	# 34207-34209
    Unknown23018(1)
    label(154)
    sprite('ak000_00', 6)	# 34210-34215
    sprite('ak000_01', 6)	# 34216-34221
    sprite('ak000_02', 6)	# 34222-34227
    sprite('ak000_03', 6)	# 34228-34233
    sprite('ak000_04', 6)	# 34234-34239
    sprite('ak000_05', 6)	# 34240-34245
    sprite('ak000_06', 6)	# 34246-34251
    sprite('ak000_07', 6)	# 34252-34257
    sprite('ak000_08', 6)	# 34258-34263
    sprite('ak000_09', 6)	# 34264-34269
    loopRest()
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('ak601_00', 6)	# 34270-34275
    if SLOT_158:
        Unknown1000(-1155000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(0)
    sprite('ak601_01', 6)	# 34276-34281
    SFX_1('pak600pmi')
    sprite('ak601_02', 6)	# 34282-34287
    label(161)
    sprite('ak601_00', 6)	# 34288-34293
    sprite('ak601_01', 6)	# 34294-34299
    sprite('ak601_02', 6)	# 34300-34305
    if SLOT_97:
        _gotolabel(161)
    sprite('ak601_03', 6)	# 34306-34311
    sprite('ak601_04', 6)	# 34312-34317
    sprite('ak601_05', 8)	# 34318-34325
    sprite('ak601_06', 4)	# 34326-34329
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak601_07', 8)	# 34330-34337
    sprite('ak601_08', 6)	# 34338-34343
    sprite('ak601_09', 2)	# 34344-34345
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 34346-34347
    sprite('ak033_01', 1)	# 34348-34348
    sprite('ak033_01', 2)	# 34349-34350
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 34351-34353
    sprite('ak033_03', 3)	# 34354-34356
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 34357-34359
    sprite('ak033_00', 3)	# 34360-34362
    Unknown21007(24, 40)
    Unknown21011(180)
    label(162)
    sprite('ak000_00', 6)	# 34363-34368
    sprite('ak000_01', 6)	# 34369-34374
    sprite('ak000_02', 6)	# 34375-34380
    sprite('ak000_03', 6)	# 34381-34386
    sprite('ak000_04', 6)	# 34387-34392
    sprite('ak000_05', 6)	# 34393-34398
    sprite('ak000_06', 6)	# 34399-34404
    sprite('ak000_07', 6)	# 34405-34410
    sprite('ak000_08', 6)	# 34411-34416
    sprite('ak000_09', 6)	# 34417-34422
    loopRest()
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('ak601_00', 6)	# 34423-34428
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(0)
    sprite('ak601_01', 6)	# 34429-34434
    SFX_1('pak600uwa')
    sprite('ak601_02', 6)	# 34435-34440
    label(171)
    sprite('ak601_00', 6)	# 34441-34446
    sprite('ak601_01', 6)	# 34447-34452
    sprite('ak601_02', 6)	# 34453-34458
    if SLOT_97:
        _gotolabel(171)
    sprite('ak601_03', 6)	# 34459-34464
    sprite('ak601_04', 6)	# 34465-34470
    sprite('ak601_05', 8)	# 34471-34478
    sprite('ak601_06', 4)	# 34479-34482
    GFX_1('akef_entry2', 0)
    SFX_3('grip_fast')
    sprite('ak601_07', 8)	# 34483-34490
    sprite('ak601_08', 6)	# 34491-34496
    sprite('ak601_09', 2)	# 34497-34498
    physicsXImpulse(-7500)
    physicsYImpulse(3000)
    sprite('ak033_00', 2)	# 34499-34500
    sprite('ak033_01', 1)	# 34501-34501
    sprite('ak033_01', 2)	# 34502-34503
    physicsYImpulse(-3000)
    sprite('ak033_02', 3)	# 34504-34506
    sprite('ak033_03', 3)	# 34507-34509
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ak033_04', 3)	# 34510-34512
    sprite('ak033_00', 3)	# 34513-34515
    Unknown21007(24, 40)
    Unknown21011(180)
    label(172)
    sprite('ak000_00', 6)	# 34516-34521
    sprite('ak000_01', 6)	# 34522-34527
    sprite('ak000_02', 6)	# 34528-34533
    sprite('ak000_03', 6)	# 34534-34539
    sprite('ak000_04', 6)	# 34540-34545
    sprite('ak000_05', 6)	# 34546-34551
    sprite('ak000_06', 6)	# 34552-34557
    sprite('ak000_07', 6)	# 34558-34563
    sprite('ak000_08', 6)	# 34564-34569
    sprite('ak000_09', 6)	# 34570-34575
    loopRest()
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('ak000_00', 1)	# 34576-34576
    if SLOT_158:
        Unknown1000(-1180000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('ak000_00', 6)	# 34577-34582
    sprite('ak000_01', 6)	# 34583-34588
    sprite('ak000_02', 6)	# 34589-34594
    sprite('ak000_03', 6)	# 34595-34600
    sprite('ak000_04', 6)	# 34601-34606
    sprite('ak000_05', 6)	# 34607-34612
    sprite('ak000_06', 6)	# 34613-34618
    sprite('ak000_07', 6)	# 34619-34624
    sprite('ak000_08', 6)	# 34625-34630
    sprite('ak000_09', 6)	# 34631-34636
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('ak001_00', 6)	# 34637-34642
    SFX_1('pak601bha')
    sprite('ak001_01', 6)	# 34643-34648
    sprite('ak001_02', 6)	# 34649-34654
    sprite('ak001_03', 4)	# 34655-34658
    sprite('ak001_04', 4)	# 34659-34662
    sprite('ak001_06', 6)	# 34663-34668
    sprite('ak001_04', 6)	# 34669-34674
    label(183)
    sprite('ak001_06', 1)	# 34675-34675
    if SLOT_97:
        _gotolabel(183)
    sprite('ak001_01', 8)	# 34676-34683
    sprite('ak001_00', 8)	# 34684-34691
    Unknown23018(1)
    label(184)
    sprite('ak000_00', 6)	# 34692-34697
    sprite('ak000_01', 6)	# 34698-34703
    sprite('ak000_02', 6)	# 34704-34709
    sprite('ak000_03', 6)	# 34710-34715
    sprite('ak000_04', 6)	# 34716-34721
    sprite('ak000_05', 6)	# 34722-34727
    sprite('ak000_06', 6)	# 34728-34733
    sprite('ak000_07', 6)	# 34734-34739
    sprite('ak000_08', 6)	# 34740-34745
    sprite('ak000_09', 6)	# 34746-34751
    loopRest()
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('ak000_00', 1)	# 34752-34752
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        Unknown2037(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ak000_00', 6)	# 34753-34758
    sprite('ak000_01', 6)	# 34759-34764
    sprite('ak000_02', 6)	# 34765-34770
    sprite('ak000_03', 6)	# 34771-34776
    sprite('ak000_04', 6)	# 34777-34782
    sprite('ak000_05', 6)	# 34783-34788
    sprite('ak000_06', 6)	# 34789-34794
    sprite('ak000_07', 6)	# 34795-34800
    sprite('ak000_08', 6)	# 34801-34806
    sprite('ak000_09', 6)	# 34807-34812
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('keep', 1)	# 34813-34813
    if SLOT_2:
        sendToLabel(193)
    sprite('ak003_00', 4)	# 34814-34817
    Unknown2005()
    sprite('ak003_01', 4)	# 34818-34821
    sprite('ak003_02', 4)	# 34822-34825
    label(193)
    sprite('ak000_00', 6)	# 34826-34831
    SFX_1('pak601ryn')
    sprite('ak000_01', 6)	# 34832-34837
    sprite('ak000_02', 6)	# 34838-34843
    sprite('ak000_03', 6)	# 34844-34849
    sprite('ak000_04', 6)	# 34850-34855
    sprite('ak000_05', 6)	# 34856-34861
    sprite('ak000_06', 6)	# 34862-34867
    sprite('ak000_07', 6)	# 34868-34873
    sprite('ak000_08', 6)	# 34874-34879
    sprite('ak000_09', 6)	# 34880-34885
    Unknown23018(1)
    label(194)
    sprite('ak000_00', 6)	# 34886-34891
    sprite('ak000_01', 6)	# 34892-34897
    sprite('ak000_02', 6)	# 34898-34903
    sprite('ak000_03', 6)	# 34904-34909
    sprite('ak000_04', 6)	# 34910-34915
    sprite('ak000_05', 6)	# 34916-34921
    sprite('ak000_06', 6)	# 34922-34927
    sprite('ak000_07', 6)	# 34928-34933
    sprite('ak000_08', 6)	# 34934-34939
    sprite('ak000_09', 6)	# 34940-34945
    gotoLabel(194)
    ExitState()
    label(200)
    sprite('ak000_00', 1)	# 34946-34946
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ak000_00', 6)	# 34947-34952
    sprite('ak000_01', 6)	# 34953-34958
    sprite('ak000_02', 6)	# 34959-34964
    sprite('ak000_03', 6)	# 34965-34970
    sprite('ak000_04', 6)	# 34971-34976
    sprite('ak000_05', 6)	# 34977-34982
    sprite('ak000_06', 6)	# 34983-34988
    sprite('ak000_07', 6)	# 34989-34994
    sprite('ak000_08', 6)	# 34995-35000
    sprite('ak000_09', 6)	# 35001-35006
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('ak001_00', 6)	# 35007-35012
    SFX_1('pak601uca')
    sprite('ak001_01', 6)	# 35013-35018
    sprite('ak001_02', 6)	# 35019-35024
    sprite('ak001_03', 4)	# 35025-35028
    sprite('ak001_04', 4)	# 35029-35032
    sprite('ak001_06', 6)	# 35033-35038
    sprite('ak001_04', 6)	# 35039-35044
    label(203)
    sprite('ak001_06', 1)	# 35045-35045
    if SLOT_97:
        _gotolabel(203)
    sprite('ak001_01', 8)	# 35046-35053
    sprite('ak001_00', 8)	# 35054-35061
    Unknown23018(1)
    label(204)
    sprite('ak000_00', 6)	# 35062-35067
    sprite('ak000_01', 6)	# 35068-35073
    sprite('ak000_02', 6)	# 35074-35079
    sprite('ak000_03', 6)	# 35080-35085
    sprite('ak000_04', 6)	# 35086-35091
    sprite('ak000_05', 6)	# 35092-35097
    sprite('ak000_06', 6)	# 35098-35103
    sprite('ak000_07', 6)	# 35104-35109
    sprite('ak000_08', 6)	# 35110-35115
    sprite('ak000_09', 6)	# 35116-35121
    loopRest()
    gotoLabel(204)
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
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('uca'):
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
            if random_(2, 0, 50):
                sendToLabel(0)
            else:
                sendToLabel(10)
        else:
            sendToLabel(0)
    else:
        sendToLabel(0)
    label(0)
    sprite('ak610_00', 6)	# 5-10
    sprite('ak610_01', 6)	# 11-16
    sprite('ak610_02', 6)	# 17-22
    sprite('ak610_03', 6)	# 23-28
    SFX_3('bonecleak_l')
    sprite('ak610_04', 6)	# 29-34
    sprite('ak610_05', 6)	# 35-40
    sprite('ak610_06', 6)	# 41-46
    sprite('ak610_05', 6)	# 47-52
    sprite('ak610_04', 6)	# 53-58
    sprite('ak610_03', 6)	# 59-64
    SFX_3('bonecleak_l')
    sprite('ak610_02', 6)	# 65-70
    sprite('ak610_07', 8)	# 71-78
    sprite('ak610_08', 8)	# 79-86
    Unknown23029(11, 6100, 0)
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pak524', 100, 896229744, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pak402_0', 100, 879452528, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pak520', 100, 896229744, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ak610_09', 8)	# 87-94
    sprite('ak610_10', 6)	# 95-100
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 101-106
    sprite('ak610_12', 6)	# 107-112
    Unknown23018(1)
    label(1)
    sprite('ak610_10', 6)	# 113-118
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 119-124
    sprite('ak610_12', 6)	# 125-130
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ak611_00', 6)	# 131-136
    Unknown2053(0)
    Unknown2034(0)
    GFX_0('WinCamera', 100)
    Unknown36(24)
    Unknown2053(0)
    Unknown2034(0)
    Unknown35()
    Unknown36(22)
    Unknown2053(0)
    Unknown2034(0)
    Unknown35()
    sprite('ak611_01', 6)	# 137-142
    if SLOT_158:
        if SLOT_108:
            Unknown7006('pak402_0', 100, 879452528, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pak522', 100, 896229744, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ak611_02', 6)	# 143-148
    sprite('ak611_03', 6)	# 149-154
    sprite('ak611_04', 6)	# 155-160
    sprite('ak611_05', 6)	# 161-166
    sprite('ak611_06', 6)	# 167-172
    sprite('ak611_07', 6)	# 173-178
    sprite('ak611_08', 6)	# 179-184
    SFX_3('cloth_h')
    sprite('ak611_09', 8)	# 185-192
    sprite('ak611_10', 8)	# 193-200
    sprite('ak611_11', 8)	# 201-208
    label(11)
    sprite('ak611_12', 1)	# 209-209
    if SLOT_97:
        _gotolabel(11)
    sprite('ak611_13', 6)	# 210-215
    sprite('ak611_14', 8)	# 216-223
    sprite('ak611_15', 4)	# 224-227
    sprite('ak611_16', 4)	# 228-231
    sprite('ak611_17', 6)	# 232-237
    physicsXImpulse(-36000)
    physicsYImpulse(40000)
    Unknown8001(1, 0)
    sprite('ak611_18', 6)	# 238-243
    Unknown23018(1)
    sprite('ak611_17', 6)	# 244-249
    sprite('ak611_18', 6)	# 250-255
    sprite('ak611_17', 6)	# 256-261
    Unknown1084(1)
    sprite('ak611_18', 6)	# 262-267
    label(12)
    sprite('ak611_17', 6)	# 268-273
    sprite('ak611_18', 6)	# 274-279
    gotoLabel(12)
    label(100)
    sprite('ak033_00', 2)	# 280-281

    def upon_40():
        clearUponHandler(40)
        SFX_1('pak702pce')
        Unknown23018(1)
    sprite('ak601_09', 6)	# 282-287
    sprite('ak601_03', 6)	# 288-293
    SFX_1('pak700pce')
    label(101)
    sprite('ak601_00', 6)	# 294-299
    SFX_3('cloth_h')
    sprite('ak601_01', 6)	# 300-305
    sprite('ak601_02', 6)	# 306-311
    sprite('ak601_00', 6)	# 312-317
    sprite('ak601_01', 6)	# 318-323
    sprite('ak601_02', 6)	# 324-329
    loopRest()
    if SLOT_97:
        _gotolabel(101)
    sprite('ak601_00', 1)	# 330-330
    Unknown21007(24, 40)
    label(102)
    sprite('ak601_00', 6)	# 331-336
    SFX_3('cloth_h')
    sprite('ak601_01', 6)	# 337-342
    sprite('ak601_02', 6)	# 343-348
    sprite('ak601_00', 6)	# 349-354
    sprite('ak601_01', 6)	# 355-360
    sprite('ak601_02', 6)	# 361-366
    loopRest()
    gotoLabel(102)
    label(110)
    sprite('ak200_02', 4)	# 367-370
    sprite('ak200_00', 2)	# 371-372	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 373-375	 **attackbox here**
    sprite('ak200_02', 4)	# 376-379
    sprite('ak200_00', 2)	# 380-381	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 382-384	 **attackbox here**
    sprite('ak203_00', 1)	# 385-385
    sprite('ak203_01', 2)	# 386-387
    sprite('ak203_02', 2)	# 388-389
    sprite('ak203_03', 3)	# 390-392	 **attackbox here**
    SFX_3('hit_m_fast')
    SFX_1('pak700umi')
    sprite('ak203_04', 3)	# 393-395
    sprite('ak203_05', 3)	# 396-398	 **attackbox here**
    SFX_3('hit_m_middle')
    label(111)
    sprite('ak203_06', 1)	# 399-399	 **attackbox here**
    if SLOT_97:
        _gotolabel(111)
    sprite('ak203_06', 25)	# 400-424	 **attackbox here**
    sprite('ak203_06', 32767)	# 425-33191	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(180)
    label(120)
    sprite('ak610_00', 6)	# 33192-33197
    sprite('ak610_01', 6)	# 33198-33203
    sprite('ak610_02', 6)	# 33204-33209
    sprite('ak610_03', 6)	# 33210-33215
    SFX_3('bonecleak_l')
    sprite('ak610_04', 6)	# 33216-33221
    sprite('ak610_05', 6)	# 33222-33227
    sprite('ak610_06', 6)	# 33228-33233
    sprite('ak610_05', 6)	# 33234-33239
    sprite('ak610_04', 6)	# 33240-33245
    sprite('ak610_03', 6)	# 33246-33251
    SFX_3('bonecleak_l')
    sprite('ak610_02', 6)	# 33252-33257
    sprite('ak610_07', 8)	# 33258-33265
    sprite('ak610_08', 8)	# 33266-33273
    Unknown23029(11, 6100, 0)
    SFX_1('pak700baz')
    sprite('ak610_09', 8)	# 33274-33281
    sprite('ak610_10', 6)	# 33282-33287
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33288-33293
    sprite('ak610_12', 6)	# 33294-33299
    label(121)
    sprite('ak610_10', 6)	# 33300-33305
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33306-33311
    sprite('ak610_12', 6)	# 33312-33317
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('ak610_10', 1)	# 33318-33318
    Unknown21007(24, 40)
    Unknown21011(300)
    label(122)
    sprite('ak610_10', 6)	# 33319-33324
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33325-33330
    sprite('ak610_12', 6)	# 33331-33336
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('ak610_00', 6)	# 33337-33342
    sprite('ak610_01', 6)	# 33343-33348
    sprite('ak610_02', 6)	# 33349-33354
    sprite('ak610_03', 6)	# 33355-33360
    SFX_3('bonecleak_l')
    sprite('ak610_04', 6)	# 33361-33366
    sprite('ak610_05', 6)	# 33367-33372
    sprite('ak610_06', 6)	# 33373-33378
    sprite('ak610_05', 6)	# 33379-33384
    sprite('ak610_04', 6)	# 33385-33390
    sprite('ak610_03', 6)	# 33391-33396
    SFX_3('bonecleak_l')
    sprite('ak610_02', 6)	# 33397-33402
    sprite('ak610_07', 8)	# 33403-33410
    sprite('ak610_08', 8)	# 33411-33418
    Unknown23029(11, 6100, 0)
    SFX_1('pak700bha')
    sprite('ak610_09', 8)	# 33419-33426
    sprite('ak610_10', 6)	# 33427-33432
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33433-33438
    sprite('ak610_12', 6)	# 33439-33444
    label(131)
    sprite('ak610_10', 6)	# 33445-33450
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33451-33456
    sprite('ak610_12', 6)	# 33457-33462
    loopRest()
    if SLOT_97:
        _gotolabel(131)
    sprite('ak610_10', 1)	# 33463-33463
    Unknown21007(24, 40)
    Unknown21011(300)
    label(132)
    sprite('ak610_10', 6)	# 33464-33469
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33470-33475
    sprite('ak610_12', 6)	# 33476-33481
    loopRest()
    gotoLabel(132)
    label(140)
    sprite('ak610_00', 6)	# 33482-33487

    def upon_40():
        clearUponHandler(40)
        SFX_1('pak702ryn')
        Unknown23018(1)
    sprite('ak610_01', 6)	# 33488-33493
    sprite('ak610_02', 6)	# 33494-33499
    sprite('ak610_03', 6)	# 33500-33505
    SFX_3('bonecleak_l')
    sprite('ak610_04', 6)	# 33506-33511
    sprite('ak610_05', 6)	# 33512-33517
    sprite('ak610_06', 6)	# 33518-33523
    sprite('ak610_05', 6)	# 33524-33529
    sprite('ak610_04', 6)	# 33530-33535
    sprite('ak610_03', 6)	# 33536-33541
    SFX_3('bonecleak_l')
    sprite('ak610_02', 6)	# 33542-33547
    sprite('ak610_07', 8)	# 33548-33555
    sprite('ak610_08', 8)	# 33556-33563
    Unknown23029(11, 6100, 0)
    SFX_1('pak700ryn')
    sprite('ak610_09', 8)	# 33564-33571
    sprite('ak610_10', 6)	# 33572-33577
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33578-33583
    sprite('ak610_12', 6)	# 33584-33589
    label(141)
    sprite('ak610_10', 6)	# 33590-33595
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33596-33601
    sprite('ak610_12', 6)	# 33602-33607
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('ak610_10', 1)	# 33608-33608
    Unknown21007(24, 40)
    label(142)
    sprite('ak610_10', 6)	# 33609-33614
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 33615-33620
    sprite('ak610_12', 6)	# 33621-33626
    loopRest()
    gotoLabel(142)
    label(150)
    sprite('ak200_02', 4)	# 33627-33630
    sprite('ak200_00', 2)	# 33631-33632	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 33633-33635	 **attackbox here**
    sprite('ak200_02', 4)	# 33636-33639
    sprite('ak200_00', 2)	# 33640-33641	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 33642-33644	 **attackbox here**
    sprite('ak203_00', 1)	# 33645-33645
    sprite('ak203_01', 2)	# 33646-33647
    sprite('ak203_02', 2)	# 33648-33649
    sprite('ak203_03', 3)	# 33650-33652	 **attackbox here**
    SFX_3('hit_m_fast')
    SFX_1('pak700uwa')
    sprite('ak203_04', 3)	# 33653-33655
    sprite('ak203_05', 3)	# 33656-33658	 **attackbox here**
    SFX_3('hit_m_middle')
    label(151)
    sprite('ak203_06', 1)	# 33659-33659	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('ak203_06', 32767)	# 33660-66426	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(320)
    label(160)
    sprite('ak000_00', 1)	# 66427-66427

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ak000_00', 6)	# 66428-66433
    sprite('ak000_01', 6)	# 66434-66439
    sprite('ak000_02', 6)	# 66440-66445
    sprite('ak000_03', 6)	# 66446-66451
    sprite('ak000_04', 6)	# 66452-66457
    sprite('ak000_05', 6)	# 66458-66463
    sprite('ak000_06', 6)	# 66464-66469
    sprite('ak000_07', 6)	# 66470-66475
    sprite('ak000_08', 6)	# 66476-66481
    sprite('ak000_09', 6)	# 66482-66487
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('ak200_02', 4)	# 66488-66491
    sprite('ak200_00', 2)	# 66492-66493	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 66494-66496	 **attackbox here**
    sprite('ak200_02', 4)	# 66497-66500
    sprite('ak200_00', 2)	# 66501-66502	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 66503-66505	 **attackbox here**
    sprite('ak203_00', 1)	# 66506-66506
    sprite('ak203_01', 2)	# 66507-66508
    sprite('ak203_02', 2)	# 66509-66510
    sprite('ak203_03', 3)	# 66511-66513	 **attackbox here**
    SFX_3('hit_m_fast')
    SFX_1('pak701bmk')
    sprite('ak203_04', 3)	# 66514-66516
    sprite('ak203_05', 3)	# 66517-66519	 **attackbox here**
    SFX_3('hit_m_middle')
    Unknown23018(1)
    sprite('ak203_06', 32767)	# 66520-99286	 **attackbox here**
    label(170)
    sprite('ak000_00', 1)	# 99287-99287

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ak000_00', 6)	# 99288-99293
    sprite('ak000_01', 6)	# 99294-99299
    sprite('ak000_02', 6)	# 99300-99305
    sprite('ak000_03', 6)	# 99306-99311
    sprite('ak000_04', 6)	# 99312-99317
    sprite('ak000_05', 6)	# 99318-99323
    sprite('ak000_06', 6)	# 99324-99329
    sprite('ak000_07', 6)	# 99330-99335
    sprite('ak000_08', 6)	# 99336-99341
    sprite('ak000_09', 6)	# 99342-99347
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('ak610_00', 6)	# 99348-99353
    sprite('ak610_01', 6)	# 99354-99359
    sprite('ak610_02', 6)	# 99360-99365
    sprite('ak610_03', 6)	# 99366-99371
    SFX_3('bonecleak_l')
    sprite('ak610_04', 6)	# 99372-99377
    sprite('ak610_05', 6)	# 99378-99383
    sprite('ak610_06', 6)	# 99384-99389
    sprite('ak610_05', 6)	# 99390-99395
    sprite('ak610_04', 6)	# 99396-99401
    sprite('ak610_03', 6)	# 99402-99407
    SFX_3('bonecleak_l')
    sprite('ak610_02', 6)	# 99408-99413
    sprite('ak610_07', 8)	# 99414-99421
    sprite('ak610_08', 8)	# 99422-99429
    Unknown23029(11, 6100, 0)
    SFX_1('pak701btg')
    sprite('ak610_09', 8)	# 99430-99437
    sprite('ak610_10', 6)	# 99438-99443
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 99444-99449
    sprite('ak610_12', 6)	# 99450-99455
    Unknown23018(1)
    label(173)
    sprite('ak610_10', 6)	# 99456-99461
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 99462-99467
    sprite('ak610_12', 6)	# 99468-99473
    loopRest()
    gotoLabel(173)
    label(180)
    sprite('ak000_00', 1)	# 99474-99474

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('ak000_00', 6)	# 99475-99480
    sprite('ak000_01', 6)	# 99481-99486
    sprite('ak000_02', 6)	# 99487-99492
    sprite('ak000_03', 6)	# 99493-99498
    sprite('ak000_04', 6)	# 99499-99504
    sprite('ak000_05', 6)	# 99505-99510
    sprite('ak000_06', 6)	# 99511-99516
    sprite('ak000_07', 6)	# 99517-99522
    sprite('ak000_08', 6)	# 99523-99528
    sprite('ak000_09', 6)	# 99529-99534
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('ak610_00', 6)	# 99535-99540
    sprite('ak610_01', 6)	# 99541-99546
    sprite('ak610_02', 6)	# 99547-99552
    sprite('ak610_03', 6)	# 99553-99558
    SFX_3('bonecleak_l')
    sprite('ak610_04', 6)	# 99559-99564
    sprite('ak610_05', 6)	# 99565-99570
    sprite('ak610_06', 6)	# 99571-99576
    sprite('ak610_05', 6)	# 99577-99582
    sprite('ak610_04', 6)	# 99583-99588
    sprite('ak610_03', 6)	# 99589-99594
    SFX_3('bonecleak_l')
    sprite('ak610_02', 6)	# 99595-99600
    sprite('ak610_07', 8)	# 99601-99608
    sprite('ak610_08', 8)	# 99609-99616
    SFX_1('pak701pag')
    sprite('ak610_09', 8)	# 99617-99624
    sprite('ak610_10', 6)	# 99625-99630
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 99631-99636
    sprite('ak610_12', 6)	# 99637-99642
    Unknown23018(1)
    label(183)
    sprite('ak610_10', 6)	# 99643-99648
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 99649-99654
    sprite('ak610_12', 6)	# 99655-99660
    loopRest()
    gotoLabel(183)
    label(190)
    sprite('ak000_00', 1)	# 99661-99661

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ak000_00', 6)	# 99662-99667
    sprite('ak000_01', 6)	# 99668-99673
    sprite('ak000_02', 6)	# 99674-99679
    sprite('ak000_03', 6)	# 99680-99685
    sprite('ak000_04', 6)	# 99686-99691
    sprite('ak000_05', 6)	# 99692-99697
    sprite('ak000_06', 6)	# 99698-99703
    sprite('ak000_07', 6)	# 99704-99709
    sprite('ak000_08', 6)	# 99710-99715
    sprite('ak000_09', 6)	# 99716-99721
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('ak610_00', 6)	# 99722-99727
    sprite('ak610_01', 6)	# 99728-99733
    sprite('ak610_02', 6)	# 99734-99739
    sprite('ak610_03', 6)	# 99740-99745
    SFX_3('bonecleak_l')
    sprite('ak610_04', 6)	# 99746-99751
    sprite('ak610_05', 6)	# 99752-99757
    sprite('ak610_06', 6)	# 99758-99763
    sprite('ak610_05', 6)	# 99764-99769
    sprite('ak610_04', 6)	# 99770-99775
    sprite('ak610_03', 6)	# 99776-99781
    SFX_3('bonecleak_l')
    sprite('ak610_02', 6)	# 99782-99787
    sprite('ak610_07', 8)	# 99788-99795
    sprite('ak610_08', 8)	# 99796-99803
    SFX_1('pak701pmi')
    sprite('ak610_09', 8)	# 99804-99811
    sprite('ak610_10', 6)	# 99812-99817
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 99818-99823
    sprite('ak610_12', 6)	# 99824-99829
    Unknown23018(1)
    label(193)
    sprite('ak610_10', 6)	# 99830-99835
    SFX_3('cloth_l')
    sprite('ak610_11', 6)	# 99836-99841
    sprite('ak610_12', 6)	# 99842-99847
    loopRest()
    gotoLabel(193)
    label(200)
    sprite('ak000_00', 1)	# 99848-99848

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ak000_00', 6)	# 99849-99854
    sprite('ak000_01', 6)	# 99855-99860
    sprite('ak000_02', 6)	# 99861-99866
    sprite('ak000_03', 6)	# 99867-99872
    sprite('ak000_04', 6)	# 99873-99878
    sprite('ak000_05', 6)	# 99879-99884
    sprite('ak000_06', 6)	# 99885-99890
    sprite('ak000_07', 6)	# 99891-99896
    sprite('ak000_08', 6)	# 99897-99902
    sprite('ak000_09', 6)	# 99903-99908
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('ak200_02', 4)	# 99909-99912
    sprite('ak200_00', 2)	# 99913-99914	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 99915-99917	 **attackbox here**
    sprite('ak200_02', 4)	# 99918-99921
    sprite('ak200_00', 2)	# 99922-99923	 **attackbox here**
    SFX_3('hit_l_fast')
    sprite('ak200_01', 3)	# 99924-99926	 **attackbox here**
    sprite('ak203_00', 1)	# 99927-99927
    sprite('ak203_01', 2)	# 99928-99929
    sprite('ak203_02', 2)	# 99930-99931
    sprite('ak203_03', 3)	# 99932-99934	 **attackbox here**
    SFX_3('hit_m_fast')
    sprite('ak203_04', 3)	# 99935-99937
    sprite('ak203_05', 3)	# 99938-99940	 **attackbox here**
    SFX_3('hit_m_middle')
    SFX_1('pak701uca')
    Unknown23018(1)
    sprite('ak203_06', 32767)	# 99941-132707	 **attackbox here**

@State
def CmnActLose():
    sprite('ak070_00', 6)	# 1-6
    Unknown7006('pak403_0', 100, 879452528, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ak070_01', 6)	# 7-12
    sprite('ak070_02', 2)	# 13-14
    Unknown23018(1)
    sprite('ak070_03', 32767)	# 15-32781
