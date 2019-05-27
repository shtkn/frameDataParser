@Subroutine
def PreInit():
    Unknown12019('626a6e00000000000000000000000000')

@Subroutine
def MatchInit():
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
    Unknown15013(1)
    Unknown14015(0, 300000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown15013(1)
    Unknown14015(0, 230000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown14015(50000, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown15013(1)
    Unknown14015(0, 250000, -100000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown14015(200000, 450000, -150000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown14015(0, 450000, -150000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x19)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14027('NmlAtk5B')
    Unknown15021(4000)
    Unknown14015(50000, 400000, 250000, 700000, 800, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5C', 0x2b)
    Unknown15000(0)
    Unknown15003(0)
    Unknown14015(-50000, 450000, -150000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown15012(1)
    Unknown14015(0, 450000, -100000, 100000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 300000, -300000, 0, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(100000, 550000, -100000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-100000, 250000, -400000, -100000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5BB', 0x22)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5AA')
    Unknown14015(100000, 550000, -100000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15005(1)
    Unknown14015(-300000, 300000, -300000, 300000, 1000, 10)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1200, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1200, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(500000, 1000000, -100000, 200000, 500, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('Shot_D1', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(1000000, 2000000, -100000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('Shot_D2', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(50000, 500000, -150000, 180000, 250, 0)
    Move_EndRegister()
    Move_Register('AirShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(500000, 1000000, -200000, 300000, 250, 50)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('AirShot_D1', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(700000, 1300000, -200000, 300000, 200, 50)
    Move_EndRegister()
    Move_Register('AirShot_D2', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(0)
    Unknown15012(10000)
    Unknown14015(50000, 450000, -150000, 150000, 100, 1)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15009()
    Unknown15005(1)
    Unknown15006(1)
    Unknown15012(1)
    Unknown15013(1500)
    Unknown14015(0, 700000, -200000, 100000, 500, 50)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('Assault_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15009()
    Unknown15005(1)
    Unknown15006(1)
    Unknown15012(1)
    Unknown15013(1500)
    Unknown14015(400000, 900000, -200000, 100000, 500, 50)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('Assault_2nd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(50000)
    Unknown14015(0, 300000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('Assault_D', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15009()
    Unknown15005(1)
    Unknown15012(1)
    Unknown15021(1)
    Unknown15013(2000)
    Unknown14015(0, 1000000, -150000, 150000, 250, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('Assault_D_2nd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(2000)
    Unknown14015(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1200)
    Unknown14015(100000, 450000, -500000, 100000, 250, 1)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('AirAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(2000)
    Unknown14015(100000, 450000, -500000, 100000, 100, 1)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('AirAssault_D', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(2000)
    Unknown14015(0, 300000, -350000, 300000, 50, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('RushAssaultFinish', 0x7)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 800000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-150000, 250000, -100000, 600000, 250, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAtemi', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Unknown15003(0)
    Unknown15014(2000)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-100000, 350000, -100000, 500000, 200, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAtemi_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Unknown15003(0)
    Unknown15014(2000)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-100000, 350000, -100000, 500000, 200, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3072)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(500000, 1500000, -200000, 200000, 250, 1)
    Move_EndRegister()
    Move_Register('UltimateShot_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3072)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(500000, 1500000, -200000, 200000, 250, 1)
    Move_EndRegister()
    Move_Register('UltimateAntiAirShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown14015(0, 500000, 100000, 500000, 500, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAntiAirShot_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown14015(0, 500000, 100000, 500000, 500, 0)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAirShot', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 350000, -600000, -100000, 500, 1)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('UltimateAirShot_OD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 350000, -600000, -100000, 500, 1)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Move_Register('astral', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Move_AirGround_(0x3072)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'RushAssaultFinish', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BBB', 'Assault', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown14048('AntiAir_Slow', 0x4, 0xed)
    Unknown14048('Assault', 0x4, 0x79)
    Unknown14048('Assault_D', 0x4, 0x79)
    Unknown14048('UltimateShot', 0x4, 0x5f)
    Unknown14048('UltimateShot_OD', 0x4, 0x5f)
    Unknown14048('Shot', 0x4, 0x45)
    Unknown14048('AirAssault', 0x4, 0xed)
    Unknown14048('AirAssault_D', 0x4, 0xed)
    Unknown14048('UltimateAirShot', 0x4, 0x5f)
    Unknown14048('UltimateAirShot_OD', 0x4, 0x5f)
    Unknown14048('AirShot', 0x4, 0x45)
    Unknown14048('RushAssaultFinish', 0x4, 0xed)
    Unknown14048('Assault_D_2nd', 0x4, 0xed)
    Unknown14048('Assault_2nd', 0x4, 0xed)
    Unknown14049('NmlAtk5A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk5B', 'NmlAtk5C', 0, 0)
    Unknown14049('NmlAtk5C', 'NmlAtk2C', 1, 300000)
    Unknown14049('NmlAtk5C', 'NmlAtk2C', 3, 0)
    Unknown14049('NmlAtk5D', 'UltimateShot', 6, 50)
    Unknown14049('NmlAtk5D', 'UltimateShot_OD', 6, 50)
    Unknown14049('NmlAtk5D', 'Shot', 13, 0)
    Unknown14049('Assault', 'Assault_2nd', 0, 0)
    Unknown14049('Assault_D', 'Assault_D_2nd', 0, 0)
    Unknown14049('ThrowExe', 'astral', 6, 0)
    Unknown14049('BackThrowExe', 'astral', 6, 0)
    Unknown14049('NmlAtk2A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk2B', 'NmlAtk5C', 0, 0)
    Unknown14049('NmlAtk2B', 'NmlAtk5B', 1, 200000)
    Unknown14049('NmlAtk2B', 'NmlAtk5C', 12, 0)
    Unknown14049('NmlAtk2C', 'FHighJump', 3, 0)
    Unknown14049('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    Unknown14049('NmlAtkAIR5B', 'NmlAtkAIR5A', 0, 0)
    Unknown14049('NmlAtkAIR5B', 'NmlAtkAIR5C', 3, 0)
    Unknown14049('NmlAtkAIR5C', 'AirAssault', 0, 0)
    Unknown14049('NmlAtkAIR5C', 'AirAssault_D', 0, 0)
    Unknown14049('NmlAtkAIR5C', 'FJump', 0, 0)
    Unknown14049('NmlAtkAIR5C', 'NmlAtkAIR2C', 2, 100000)
    Unknown14049('NmlAtkAIR5C', 'NmlAtkAIR2C', 13, 0)
    Unknown14049('NmlAtkAIR2C', 'NmlAtkAIR5C', 0, 0)
    Unknown14049('NmlAtkAIR2C', 'AirAssault', 3, 0)
    Unknown14049('NmlAtkAIR2C', 'AirAssault_D', 3, 0)
    Unknown12018(0, 'jn062_01')
    Unknown12018(1, 'jn062_03')
    Unknown12018(2, 'jn062_04')
    Unknown12018(3, 'jn062_05')
    Unknown12018(4, 'jn062_06')
    Unknown12018(5, 'jn062_06')
    Unknown12018(6, 'jn062_07')
    Unknown12018(7, 'jn041_02')
    Unknown12018(8, 'jn040_02')
    Unknown12018(9, 'jn045_02')
    Unknown12018(10, 'jn060_00')
    Unknown12018(11, 'jn060_01')
    Unknown12018(12, 'jn060_02')
    Unknown12018(13, 'jn060_03')
    Unknown12018(14, 'jn060_04')
    Unknown12018(15, 'jn060_12')
    Unknown12018(16, 'jn050_00')
    Unknown12018(17, 'jn052_00')
    Unknown12018(18, 'jn054_00')
    Unknown12018(19, 'jn000_00')
    Unknown12018(20, 'jn000_00')
    Unknown12018(25, 'jn063_00')
    Unknown12018(26, 'jn063_01')
    Unknown12018(27, 'jn063_02')
    Unknown12018(28, 'jn063_03')
    Unknown12018(29, 'jn063_09')
    Unknown12018(24, 'jn073_01')
    Unknown7010(0, 'bjn000')
    Unknown7010(1, 'bjn001')
    Unknown7010(2, 'bjn002')
    Unknown7010(3, 'bjn003')
    Unknown7010(4, 'bjn004')
    Unknown7010(5, 'bjn005')
    Unknown7010(6, 'bjn006')
    Unknown7010(7, 'bjn007')
    Unknown7010(8, 'bjn008')
    Unknown7010(9, 'bjn009')
    Unknown7010(10, 'bjn010')
    Unknown7010(15, 'bjn011')
    Unknown7010(16, 'bjn012')
    Unknown7010(17, 'bjn013')
    Unknown7010(18, 'bjn014')
    Unknown7010(19, 'bjn015')
    Unknown7010(20, 'bjn016')
    Unknown7010(21, 'bjn017')
    Unknown7010(22, 'bjn018')
    Unknown7010(23, 'bjn019')
    Unknown7010(24, 'bjn020')
    Unknown7010(25, 'bjn021')
    Unknown7010(28, 'bjn022')
    Unknown7010(29, 'bjn023')
    Unknown7010(30, 'bjn024')
    Unknown7010(31, 'bjn025')
    Unknown7010(32, 'bjn026')
    Unknown7010(33, 'bjn027')
    Unknown7010(34, 'bjn028')
    Unknown7010(35, 'bjn029')
    Unknown7010(36, 'bjn030')
    Unknown7010(37, 'bjn031')
    Unknown7010(39, 'bjn032')
    Unknown7010(42, 'bjn033')
    Unknown7010(43, 'bjn034')
    Unknown7010(44, 'bjn035')
    Unknown7010(45, 'bjn036')
    Unknown7010(46, 'bjn037')
    Unknown7010(47, 'bjn038')
    Unknown7010(48, 'bjn039')
    Unknown7010(49, 'bjn040')
    Unknown7010(50, 'bjn041')
    Unknown7010(52, 'bjn042')
    Unknown7010(53, 'bjn043')
    Unknown7010(54, 'bjn100_0')
    Unknown7010(55, 'bjn100_1')
    Unknown7010(56, 'bjn100_2')
    Unknown7010(63, 'bjn101_0')
    Unknown7010(64, 'bjn101_1')
    Unknown7010(65, 'bjn101_2')
    Unknown7010(57, 'bjn102_0')
    Unknown7010(58, 'bjn102_1')
    Unknown7010(59, 'bjn102_2')
    Unknown7010(66, 'bjn103_0')
    Unknown7010(67, 'bjn103_1')
    Unknown7010(68, 'bjn103_2')
    Unknown7010(60, 'bjn104_0')
    Unknown7010(61, 'bjn104_1')
    Unknown7010(62, 'bjn104_2')
    Unknown7010(69, 'bjn105_0')
    Unknown7010(70, 'bjn105_1')
    Unknown7010(71, 'bjn105_2')
    Unknown7010(72, 'bjn150')
    Unknown7010(73, 'bjn151')
    Unknown7010(74, 'bjn152')
    Unknown7010(85, 'bjn153')
    Unknown7010(87, 'bjn154')
    Unknown7010(88, 'bjn155')
    Unknown7010(96, 'bjn161_0')
    Unknown7010(97, 'bjn161_1')
    Unknown7010(92, 'bjn162_0')
    Unknown7010(93, 'bjn162_1')
    Unknown7010(98, 'bjn163_0')
    Unknown7010(99, 'bjn163_1')
    Unknown7010(100, 'bjn164_0')
    Unknown7010(101, 'bjn164_1')
    Unknown7010(105, 'bjn165_0')
    Unknown7010(106, 'bjn165_1')
    Unknown7010(102, 'bjn166_0')
    Unknown7010(103, 'bjn166_1')
    Unknown7010(90, 'bjn167_0')
    Unknown7010(91, 'bjn167_1')
    Unknown7010(107, 'bjn168_0')
    Unknown7010(108, 'bjn168_1')
    Unknown7010(110, 'bjn169_0')
    Unknown7010(111, 'bjn169_1')
    Unknown7010(94, 'bjn400_0')
    Unknown7010(95, 'bjn400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745f4f440000000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465416e746941697253686f7400000000000000000000000000')
    Unknown12059('05000000556c74696d617465416e746941697253686f745f4f4400000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if Unknown23145('CmnActOverDriveEnd'):
        SLOT_47 = 1

@Subroutine
def CheckDriveFlash():

    def upon_16():
        if SLOT_56:
            SLOT_56 = (SLOT_56 + 1)

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_21:
            if SLOT_115:
                SLOT_78 = 110
                Unknown2058(3)

@State
def CmnActStand():
    label(0)
    sprite('jn000_00', 7)	# 1-7
    sprite('jn000_01', 7)	# 8-14
    sprite('jn000_02', 7)	# 15-21
    sprite('jn000_03', 7)	# 22-28
    sprite('jn000_04', 7)	# 29-35
    sprite('jn000_05', 7)	# 36-42
    sprite('jn000_06', 7)	# 43-49
    sprite('jn000_07', 7)	# 50-56
    sprite('jn000_08', 7)	# 57-63
    sprite('jn000_09', 7)	# 64-70
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    if random_(2, 0, 80):
        gotoLabel(0)
    sprite('jn001_00', 8)	# 71-78
    sprite('jn001_01', 8)	# 79-86
    sprite('jn001_02', 10)	# 87-96
    SLOT_88 = 960
    SFX_1('bjn000')
    sprite('jn001_03', 8)	# 97-104
    sprite('jn001_04', 8)	# 105-112
    sprite('jn001_05', 8)	# 113-120
    sprite('jn001_06', 10)	# 121-130
    sprite('jn001_07', 8)	# 131-138
    sprite('jn001_08', 8)	# 139-146
    sprite('jn001_09', 8)	# 147-154
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('jn003_01', 4)	# 1-4
    sprite('jn003_00', 4)	# 5-8

@State
def CmnActStand2Crouch():
    sprite('jn010_00', 3)	# 1-3
    sprite('jn010_01', 3)	# 4-6

@State
def CmnActCrouch():
    label(0)
    sprite('jn010_02', 8)	# 1-8
    sprite('jn010_03', 8)	# 9-16
    sprite('jn010_04', 8)	# 17-24
    sprite('jn010_05', 8)	# 25-32
    sprite('jn010_06', 8)	# 33-40
    sprite('jn010_07', 8)	# 41-48
    sprite('jn010_08', 8)	# 49-56
    sprite('jn010_09', 8)	# 57-64
    sprite('jn010_10', 8)	# 65-72
    sprite('jn010_11', 8)	# 73-80
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('jn013_01', 4)	# 1-4
    sprite('jn013_00', 4)	# 5-8

@State
def CmnActCrouch2Stand():
    sprite('jn010_01', 4)	# 1-4
    sprite('jn010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('jn020_00', 2)	# 1-2
    sprite('jn020_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('jn020_02', 3)	# 1-3
    sprite('jn020_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('jn020_04', 3)	# 1-3
    sprite('jn020_05', 3)	# 4-6

@State
def CmnActJumpDown():
    sprite('jn020_05', 3)	# 1-3
    sprite('jn020_06', 3)	# 4-6
    sprite('jn020_07', 3)	# 7-9
    label(0)
    sprite('jn020_08', 3)	# 10-12
    sprite('jn020_09', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('jn020_10', 3)	# 1-3
    sprite('jn020_11', 3)	# 4-6
    sprite('jn020_12', 3)	# 7-9
    sprite('jn020_13', 3)	# 10-12
    sprite('jn020_14', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('jn020_10', 2)	# 1-2
    sprite('jn020_11', 2)	# 3-4
    sprite('jn020_12', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('jn020_13', 3)	# 1-3
    sprite('jn020_14', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('jn030_00', 6)	# 1-6
    label(0)
    sprite('jn030_01', 6)	# 7-12
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)	# 13-18
    sprite('jn030_03', 6)	# 19-24
    sprite('jn030_04', 6)	# 25-30
    sprite('jn030_05', 6)	# 31-36
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)	# 37-42
    sprite('jn030_07', 6)	# 43-48
    sprite('jn030_08', 6)	# 49-54
    sprite('jn030_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('jn031_00', 6)	# 1-6
    label(0)
    sprite('jn031_01', 6)	# 7-12
    sprite('jn031_02', 6)	# 13-18
    sprite('jn031_03', 6)	# 19-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn031_04', 6)	# 25-30
    sprite('jn031_05', 6)	# 31-36
    sprite('jn031_06', 6)	# 37-42
    sprite('jn031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn031_08', 6)	# 49-54
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('jn032_12', 3)	# 1-3
    sprite('jn032_00', 4)	# 4-7
    sprite('jn032_01', 4)	# 8-11
    label(0)
    sprite('jn032_02', 4)	# 12-15
    sprite('jn032_03', 4)	# 16-19
    sprite('jn032_04', 4)	# 20-23
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 24-27
    sprite('jn032_06', 4)	# 28-31
    sprite('jn032_07', 4)	# 32-35
    sprite('jn032_08', 4)	# 36-39
    sprite('jn032_09', 4)	# 40-43
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 44-47
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('jn032_11', 6)	# 1-6
    sprite('jn032_12', 6)	# 7-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('jn033_00', 2)	# 1-2
    sprite('jn033_01', 3)	# 3-5
    physicsXImpulse(-24000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('jn033_02', 3)	# 6-8
    sprite('jn033_03', 3)	# 9-11
    sprite('jn033_04', 32767)	# 12-32778
    loopRest()
    label(1)
    sprite('jn033_05', 2)	# 32779-32780
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('jn033_06', 1)	# 32781-32781
    sprite('jn033_07', 1)	# 32782-32782
    sprite('jn033_08', 1)	# 32783-32783

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('jn035_00', 5)	# 1-5
    label(0)
    sprite('jn035_01', 3)	# 6-8
    sprite('jn035_02', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('jn036_00', 5)	# 1-5
    label(0)
    sprite('jn036_01', 3)	# 6-8
    sprite('jn036_02', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('jn050_00', 1)	# 1-1
    sprite('jn050_01', 1)	# 2-2
    sprite('jn050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('jn050_01', 1)	# 1-1
    sprite('jn050_02', 1)	# 2-2
    sprite('jn050_01', 2)	# 3-4
    sprite('jn050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('jn050_02', 1)	# 1-1
    sprite('jn050_03', 1)	# 2-2
    sprite('jn050_02', 2)	# 3-4
    sprite('jn050_01', 2)	# 5-6
    sprite('jn050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('jn050_03', 1)	# 1-1
    sprite('jn050_04', 1)	# 2-2
    sprite('jn050_03', 2)	# 3-4
    sprite('jn050_02', 2)	# 5-6
    sprite('jn050_01', 2)	# 7-8
    sprite('jn050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('jn050_04', 1)	# 1-1
    sprite('jn050_05', 1)	# 2-2
    sprite('jn050_04', 2)	# 3-4
    sprite('jn050_03', 2)	# 5-6
    sprite('jn050_02', 2)	# 7-8
    sprite('jn050_01', 2)	# 9-10
    sprite('jn050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('jn052_00', 1)	# 1-1
    sprite('jn052_01', 1)	# 2-2
    sprite('jn052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('jn052_01', 1)	# 1-1
    sprite('jn052_02', 1)	# 2-2
    sprite('jn052_01', 2)	# 3-4
    sprite('jn052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('jn052_02', 1)	# 1-1
    sprite('jn052_03', 1)	# 2-2
    sprite('jn052_02', 2)	# 3-4
    sprite('jn052_01', 2)	# 5-6
    sprite('jn052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('jn052_03', 1)	# 1-1
    sprite('jn052_04', 1)	# 2-2
    sprite('jn052_03', 2)	# 3-4
    sprite('jn052_02', 2)	# 5-6
    sprite('jn052_01', 2)	# 7-8
    sprite('jn052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('jn052_04', 1)	# 1-1
    sprite('jn052_05', 1)	# 2-2
    sprite('jn052_04', 2)	# 3-4
    sprite('jn052_03', 2)	# 5-6
    sprite('jn052_02', 2)	# 7-8
    sprite('jn052_01', 2)	# 9-10
    sprite('jn052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('jn054_00', 1)	# 1-1
    sprite('jn054_01', 1)	# 2-2
    sprite('jn054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('jn054_01', 1)	# 1-1
    sprite('jn054_02', 1)	# 2-2
    sprite('jn054_01', 2)	# 3-4
    sprite('jn054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('jn054_02', 1)	# 1-1
    sprite('jn054_03', 1)	# 2-2
    sprite('jn054_02', 2)	# 3-4
    sprite('jn054_01', 2)	# 5-6
    sprite('jn054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('jn054_03', 1)	# 1-1
    sprite('jn054_04', 1)	# 2-2
    sprite('jn054_03', 2)	# 3-4
    sprite('jn054_02', 2)	# 5-6
    sprite('jn054_01', 2)	# 7-8
    sprite('jn054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('jn054_04', 1)	# 1-1
    sprite('jn054_05', 1)	# 2-2
    sprite('jn054_04', 2)	# 3-4
    sprite('jn054_03', 2)	# 5-6
    sprite('jn054_02', 2)	# 7-8
    sprite('jn054_01', 2)	# 9-10
    sprite('jn054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('jn060_00', 6)	# 1-6
    label(0)
    sprite('jn060_01', 4)	# 7-10
    sprite('jn060_01add', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('jn062_04', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('jn062_05', 2)	# 1-2
    sprite('jn062_06', 2)	# 3-4
    label(0)
    sprite('jn062_07', 4)	# 5-8
    sprite('jn062_08', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('jn062_09', 2)	# 1-2
    sprite('jn062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('jn063_04', 3)	# 1-3
    sprite('jn063_05', 3)	# 4-6
    sprite('jn063_06', 3)	# 7-9
    sprite('jn063_07', 3)	# 10-12
    sprite('jn063_08', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('jn063_09', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('jn064_00', 3)	# 1-3
    sprite('jn064_01', 3)	# 4-6
    sprite('jn064_02', 3)	# 7-9
    sprite('jn064_03', 3)	# 10-12
    sprite('jn064_04', 3)	# 13-15
    sprite('jn064_05', 3)	# 16-18
    sprite('jn064_06', 3)	# 19-21
    sprite('jn064_07', 3)	# 22-24
    sprite('jn064_08', 3)	# 25-27
    sprite('jn064_09', 3)	# 28-30
    sprite('jn064_10', 3)	# 31-33
    sprite('jn064_11', 3)	# 34-36
    sprite('jn064_12', 3)	# 37-39

@State
def CmnActFDownUpper():
    sprite('jn063_00', 3)	# 1-3
    sprite('jn063_01', 3)	# 4-6

@State
def CmnActFDownUpperEnd():
    sprite('jn063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    sprite('jn063_01', 3)	# 1-3
    label(0)
    sprite('jn063_02', 3)	# 4-6
    sprite('jn063_02add', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('jn063_03', 3)	# 1-3

@State
def CmnActFDownBound():
    sprite('jn063_04', 3)	# 1-3
    sprite('jn063_05', 3)	# 4-6
    sprite('jn063_06', 3)	# 7-9
    sprite('jn063_07', 3)	# 10-12
    sprite('jn063_08', 3)	# 13-15

@State
def CmnActFDownLoop():
    sprite('jn063_09', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('jn064_00', 3)	# 1-3
    sprite('jn064_01', 3)	# 4-6
    sprite('jn064_02', 3)	# 7-9
    sprite('jn064_03', 3)	# 10-12
    sprite('jn064_04', 3)	# 13-15
    sprite('jn064_05', 3)	# 16-18
    sprite('jn064_06', 3)	# 19-21
    sprite('jn064_07', 3)	# 22-24
    sprite('jn064_08', 3)	# 25-27
    sprite('jn064_09', 3)	# 28-30
    sprite('jn064_10', 3)	# 31-33
    sprite('jn064_11', 3)	# 34-36
    sprite('jn064_12', 3)	# 37-39

@State
def CmnActVDownUpper():
    sprite('jn062_00', 4)	# 1-4
    label(0)
    sprite('jn062_01', 4)	# 5-8
    sprite('jn062_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('jn062_03', 3)	# 1-3
    sprite('jn062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('jn062_05', 4)	# 1-4
    sprite('jn062_06', 4)	# 5-8
    label(0)
    sprite('jn062_07', 4)	# 9-12
    sprite('jn062_08', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('jn062_09', 2)	# 1-2
    sprite('jn062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('jn072_00', 3)	# 1-3
    label(0)
    sprite('jn072_01', 3)	# 4-6
    sprite('jn072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('jn074_00', 3)	# 1-3
    sprite('jn074_01', 3)	# 4-6
    sprite('jn074_02', 3)	# 7-9
    sprite('jn074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('jn082_00', 2)	# 1-2
    sprite('jn082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('jn071_03', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('jn073_00', 3)	# 1-3
    sprite('jn073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('jn073_02', 3)	# 1-3
    label(0)
    sprite('jn073_03', 3)	# 4-6
    sprite('jn073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('jn070_00', 2)	# 1-2
    sprite('jn070_01', 2)	# 3-4
    sprite('jn070_02', 2)	# 5-6
    sprite('jn070_03', 2)	# 7-8

@State
def CmnActStaggerDown():
    sprite('jn070_08', 6)	# 1-6
    sprite('jn070_09', 6)	# 7-12
    sprite('jn070_10', 6)	# 13-18
    sprite('jn070_11', 6)	# 19-24

@State
def CmnActUkemiStagger():
    sprite('jn070_12', 2)	# 1-2
    sprite('jn070_13', 3)	# 3-5
    sprite('jn070_14', 3)	# 6-8

@State
def CmnActUkemiAirF():
    sprite('jn113_00', 2)	# 1-2
    sprite('jn113_01', 2)	# 3-4
    sprite('jn113_02', 2)	# 5-6

@State
def CmnActUkemiAirB():
    sprite('jn113_00', 2)	# 1-2
    sprite('jn113_01', 2)	# 3-4
    sprite('jn113_02', 2)	# 5-6

@State
def CmnActUkemiAirN():
    sprite('jn113_00', 2)	# 1-2
    sprite('jn113_01', 2)	# 3-4
    sprite('jn113_02', 2)	# 5-6

@State
def CmnActUkemiLandF():
    sprite('jn110_00', 3)	# 1-3
    sprite('jn110_01', 3)	# 4-6
    sprite('jn110_02', 3)	# 7-9
    sprite('jn110_03', 3)	# 10-12
    sprite('jn110_04', 3)	# 13-15
    sprite('jn110_05', 3)	# 16-18
    sprite('jn110_06', 3)	# 19-21
    sprite('jn110_07', 200)	# 22-221
    sprite('jn110_08', 6)	# 222-227

@State
def CmnActUkemiLandB():
    sprite('jn111_00', 3)	# 1-3
    sprite('jn111_01', 3)	# 4-6
    sprite('jn111_02', 3)	# 7-9
    sprite('jn111_03', 3)	# 10-12
    sprite('jn111_04', 3)	# 13-15
    sprite('jn111_05', 3)	# 16-18
    sprite('jn111_06', 200)	# 19-218
    sprite('jn111_07', 6)	# 219-224

@State
def CmnActUkemiLandN():
    sprite('jn112_00', 3)	# 1-3
    sprite('jn112_01', 3)	# 4-6
    sprite('jn112_02', 3)	# 7-9
    sprite('jn112_03', 3)	# 10-12
    sprite('jn112_04', 3)	# 13-15
    sprite('jn112_05', 3)	# 16-18
    sprite('jn112_06', 3)	# 19-21
    sprite('jn112_07', 3)	# 22-24
    sprite('jn112_08', 3)	# 25-27

@State
def CmnActUkemiLandNLanding():
    sprite('jn020_11', 3)	# 1-3
    sprite('jn020_12', 3)	# 4-6
    sprite('jn020_13', 3)	# 7-9
    sprite('jn020_14', 3)	# 10-12

@State
def CmnActMidGuardPre():
    sprite('jn040_00', 3)	# 1-3
    sprite('jn040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('jn040_02', 5)	# 1-5
    sprite('jn040_03', 5)	# 6-10
    sprite('jn040_04', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('jn040_01', 3)	# 1-3
    sprite('jn040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('jn040_05', 3)	# 1-3
    label(0)
    sprite('jn040_02', 5)	# 4-8
    sprite('jn040_03', 5)	# 9-13
    sprite('jn040_04', 5)	# 14-18
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('jn040_01', 3)	# 1-3
    sprite('jn040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('jn041_00', 3)	# 1-3
    sprite('jn041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('jn041_02', 5)	# 1-5
    sprite('jn041_03', 5)	# 6-10
    sprite('jn041_04', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('jn041_01', 3)	# 1-3
    sprite('jn041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('jn041_05', 3)	# 1-3
    label(0)
    sprite('jn041_02', 5)	# 4-8
    sprite('jn041_03', 5)	# 9-13
    sprite('jn041_04', 5)	# 14-18
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('jn041_01', 3)	# 1-3
    sprite('jn041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('jn043_00', 3)	# 1-3
    sprite('jn043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('jn043_02', 5)	# 1-5
    sprite('jn043_03', 5)	# 6-10
    sprite('jn043_04', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('jn043_01', 3)	# 1-3
    sprite('jn043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('jn043_05', 3)	# 1-3
    label(0)
    sprite('jn043_02', 5)	# 4-8
    sprite('jn043_03', 5)	# 9-13
    sprite('jn043_04', 5)	# 14-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('jn043_01', 3)	# 1-3
    sprite('jn043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('jn045_00', 3)	# 1-3
    sprite('jn045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('jn045_02', 5)	# 1-5
    sprite('jn045_03', 5)	# 6-10
    sprite('jn045_04', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('jn045_01', 3)	# 1-3
    sprite('jn045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('jn045_05', 3)	# 1-3
    label(0)
    sprite('jn045_02', 5)	# 4-8
    sprite('jn045_03', 5)	# 9-13
    sprite('jn045_04', 5)	# 14-18
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('jn045_01', 3)	# 1-3
    sprite('jn045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('jn090_00', 2)	# 1-2
    sprite('jn090_01', 2)	# 3-4
    sprite('jn090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('jn090_03', 6)	# 6-11
    sprite('jn090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('jn091_00', 2)	# 1-2
    sprite('jn091_01', 2)	# 3-4
    sprite('jn091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('jn091_03', 6)	# 6-11
    sprite('jn091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('jn092_00', 2)	# 1-2
    sprite('jn092_01', 2)	# 3-4
    sprite('jn092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('jn092_03', 6)	# 6-11
    sprite('jn092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('jn025_00', 4)	# 1-4
    sprite('jn025_01', 4)	# 5-8
    sprite('jn025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('________', 10)	# 1-10
    sprite('________', 10)	# 11-20
    sprite('jn040_01', 3)	# 21-23
    sprite('jn040_00', 3)	# 24-26

@State
def CmnActLockReject():
    sprite('jn312_00', 4)	# 1-4
    sprite('jn312_01', 4)	# 5-8
    sprite('jn312_02', 2)	# 9-10
    sprite('jn312_03', 3)	# 11-13	 **attackbox here**
    sprite('jn312_04', 5)	# 14-18
    sprite('jn312_05', 5)	# 19-23
    sprite('jn312_06', 5)	# 24-28
    sprite('jn312_07', 5)	# 29-33
    sprite('jn312_08', 5)	# 34-38
    sprite('jn312_09', 5)	# 39-43
    sprite('jn312_10', 5)	# 44-48

@State
def CmnActAirLockWait():
    sprite('jn045_02', 1)	# 1-1
    sprite('jn045_01', 3)	# 2-4
    sprite('jn045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('jn322_00', 5)	# 1-5
    sprite('jn322_01', 2)	# 6-7
    sprite('jn322_02', 1)	# 8-8
    sprite('jn322_03', 3)	# 9-11	 **attackbox here**
    sprite('jn322_04', 4)	# 12-15
    sprite('jn322_05', 4)	# 16-19
    sprite('jn322_06', 4)	# 20-23
    sprite('jn322_07', 4)	# 24-27
    sprite('jn322_08', 4)	# 28-31
    sprite('jn322_09', 4)	# 32-35

@State
def CmnActLandSpin():
    sprite('jn071_00', 4)	# 1-4
    sprite('jn071_01', 4)	# 5-8
    label(0)
    sprite('jn071_02', 4)	# 9-12
    sprite('jn071_03', 4)	# 13-16
    sprite('jn071_04', 4)	# 17-20
    sprite('jn071_05', 4)	# 21-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('jn071_06', 6)	# 1-6
    sprite('jn071_07', 6)	# 7-12
    sprite('jn071_08', 4)	# 13-16

@State
def CmnActVertSpin():
    label(0)
    sprite('jn071_02', 4)	# 1-4
    sprite('jn071_03', 4)	# 5-8
    sprite('jn071_04', 4)	# 9-12
    sprite('jn071_05', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('jn077_90', 2)	# 1-2
    sprite('jn077_91', 2)	# 3-4
    sprite('jn077_90ex01', 2)	# 5-6
    sprite('jn077_91ex01', 2)	# 7-8
    sprite('jn077_90ex02', 2)	# 9-10
    sprite('jn077_91ex02', 2)	# 11-12
    sprite('jn077_90ex03', 2)	# 13-14
    sprite('jn077_91ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('jn077_00', 3)	# 1-3
    label(0)
    sprite('jn077_01', 3)	# 4-6
    sprite('jn077_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('jn077_03', 3)	# 1-3
    sprite('jn077_04', 3)	# 4-6
    sprite('jn077_05', 3)	# 7-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('jn060_04', 4)	# 1-4
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('jn060_10', 5)	# 1-5
    sprite('jn060_11', 4)	# 6-9

@State
def CmnActBurstBegin():
    sprite('jn331_00', 2)	# 1-2
    label(0)
    sprite('jn331_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('jn331_02', 3)	# 1-3
    label(0)
    sprite('jn331_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('jn331_04', 2)	# 1-2
    sprite('jn331_05', 2)	# 3-4
    sprite('jn331_06', 2)	# 5-6

@State
def CmnActAirBurstBegin():
    sprite('jn332_00', 2)	# 1-2
    label(0)
    sprite('jn332_01', 3)	# 3-5
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('jn332_02', 3)	# 1-3
    sprite('jn332_03', 3)	# 4-6
    label(0)
    sprite('jn332_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('jn332_05', 3)	# 1-3
    sprite('jn332_06', 3)	# 4-6
    sprite('jn020_05', 3)	# 7-9
    sprite('jn020_06', 3)	# 10-12
    sprite('jn020_07', 3)	# 13-15
    label(0)
    sprite('jn020_08', 3)	# 16-18
    sprite('jn020_09', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('jn333_00', 3)	# 1-3
    sprite('jn333_01', 3)	# 4-6
    sprite('jn333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('jn333_03', 32767)	# 10-32776
    GFX_0('EMB_JN_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('jn333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('jn333_05', 3)	# 4-6
    sprite('jn333_06', 3)	# 7-9
    sprite('jn333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('jn333_08', 4)	# 1-4
    sprite('jn333_09', 4)	# 5-8
    sprite('jn333_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('jn333_11', 3)	# 1-3
    sprite('jn333_12', 3)	# 4-6
    sprite('jn333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('jn333_14', 32767)	# 10-32776
    GFX_0('EMB_JN_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('jn333_15', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('jn333_05', 3)	# 4-6
    sprite('jn333_06', 3)	# 7-9
    sprite('jn333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('jn333_16', 4)	# 1-4
    sprite('jn333_17', 4)	# 5-8
    sprite('jn333_18', 4)	# 9-12
    label(0)
    sprite('jn020_08', 3)	# 13-15
    sprite('jn020_09', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('jn333_00', 3)	# 1-3
    sprite('jn333_01', 3)	# 4-6
    sprite('jn333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('jn333_03', 32767)	# 10-32776
    GFX_0('EMB_JN_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('jn333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('jn333_05', 3)	# 4-6
    sprite('jn333_06', 3)	# 7-9
    sprite('jn333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('jn333_08', 4)	# 1-4
    sprite('jn333_09', 4)	# 5-8
    sprite('jn333_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('jn333_11', 3)	# 1-3
    sprite('jn333_12', 3)	# 4-6
    sprite('jn333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('jn333_14', 32767)	# 10-32776
    GFX_0('EMB_JN_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('jn333_15', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('jn333_05', 3)	# 4-6
    sprite('jn333_06', 3)	# 7-9
    sprite('jn333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('jn333_16', 4)	# 1-4
    sprite('jn333_17', 4)	# 5-8
    sprite('jn333_18', 4)	# 9-12
    label(0)
    sprite('jn020_08', 3)	# 13-15
    sprite('jn020_09', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('jn331_00', 2)	# 1-2
    sprite('jn331_01', 32767)	# 3-32769

@State
def CmnActCrossChangeLoop():
    sprite('jn331_02', 3)	# 1-3
    sprite('jn331_03', 32767)	# 4-32770

@State
def CmnActCrossChangeEnd():
    sprite('jn331_04', 2)	# 1-2
    sprite('jn331_05', 2)	# 3-4
    sprite('jn331_06', 2)	# 5-6

@State
def CmnActAirCrossChangeBegin():
    sprite('jn332_00', 2)	# 1-2
    sprite('jn332_01', 32767)	# 3-32769

@State
def CmnActAirCrossChangeLoop():
    sprite('jn332_02', 3)	# 1-3
    sprite('jn332_03', 3)	# 4-6
    sprite('jn332_04', 32767)	# 7-32773

@State
def CmnActAirCrossChangeEnd():
    sprite('jn332_05', 2)	# 1-2
    sprite('jn332_06', 2)	# 3-4
    sprite('jn020_05', 2)	# 5-6
    sprite('jn020_06', 2)	# 7-8
    sprite('jn020_07', 2)	# 9-10
    label(0)
    sprite('jn020_08', 3)	# 11-13
    sprite('jn020_09', 3)	# 14-16
    loopRest()
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
    label(0)
    sprite('null', 1)	# 1-1
    Unknown2017(0)
    Unknown2034(0)
    teleportRelativeY(0)
    gotoLabel(0)

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('jn610_00', 5)	# 1-5
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    sprite('jn610_01', 5)	# 6-10
    sprite('jn610_02', 12)	# 11-22
    sprite('jn610_03', 5)	# 23-27
    sprite('jn610_04', 5)	# 28-32
    sprite('jn610_05', 6)	# 33-38
    sprite('jn610_06', 6)	# 39-44
    sprite('jn610_07', 6)	# 45-50
    sprite('jn610_08', 12)	# 51-62
    sprite('jn610_00', 6)	# 63-68

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('jn045_00', 2)	# 1-2
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('jn045_01', 2)	# 3-4
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    label(0)
    sprite('jn045_02', 5)	# 5-9
    sprite('jn045_03', 5)	# 10-14
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
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jn045_04', 6)	# 15-20
    sprite('jn045_05', 6)	# 21-26

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('jn033_01', 3)	# 1-3
    sprite('jn033_02', 3)	# 4-6
    sprite('jn033_03', 3)	# 7-9
    sprite('jn033_04', 3)	# 10-12
    sprite('jn033_04', 48)	# 13-60

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('jn611_00', 2)	# 1-2
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('jn611_01', 3)	# 3-5
    sprite('jn611_02', 3)	# 6-8
    sprite('jn611_03', 4)	# 9-12
    sprite('jn611_04', 4)	# 13-16
    sprite('jn611_05', 4)	# 17-20
    sprite('jn611_06', 4)	# 21-24
    sprite('jn611_07', 4)	# 25-28
    sprite('jn611_08', 4)	# 29-32
    sprite('jn611_09', 4)	# 33-36
    sprite('jn611_10', 4)	# 37-40
    sprite('jn611_11', 4)	# 41-44
    sprite('jn611_12', 4)	# 45-48
    label(1)
    sprite('jn611_10', 4)	# 49-52
    sprite('jn611_11', 4)	# 53-56
    sprite('jn611_12', 4)	# 57-60
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('jn611_10', 3)	# 61-63
    sprite('jn611_11', 3)	# 64-66
    sprite('jn611_12', 2)	# 67-68
    sprite('jn611_13', 4)	# 69-72

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('jn610_00', 5)	# 1-5
    sprite('jn610_01', 5)	# 6-10
    sprite('jn610_02', 12)	# 11-22
    sprite('jn610_03', 5)	# 23-27
    sprite('jn610_04', 5)	# 28-32
    sprite('jn610_05', 6)	# 33-38
    sprite('jn610_06', 6)	# 39-44
    sprite('jn610_07', 6)	# 45-50
    sprite('jn610_08', 20)	# 51-70
    sprite('jn610_00', 30)	# 71-100

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)
    sprite('null', 22)	# 1-22
    sprite('jn413_00', 3)	# 23-25
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    physicsXImpulse(150000)
    physicsYImpulse(-100000)
    sprite('jn413_01', 3)	# 26-28
    sprite('jn413_02', 2)	# 29-30
    sprite('jn413_05', 2)	# 31-32
    sprite('jn413_06', 3)	# 33-35
    Unknown1084(1)
    physicsXImpulse(-9000)
    physicsYImpulse(20000)
    setGravity(2000)
    SFX_0('009_swing_rapier_2')
    SFX_3('jnse_21')
    GFX_0('EFF413C', -1)
    Unknown2053(1)
    Unknown2017(1)
    sendToLabelUpon(2, 9)
    sprite('jn413_07', 3)	# 36-38	 **attackbox here**
    sprite('jn413_08', 3)	# 39-41
    Unknown1019(50)
    sprite('jn413_09', 3)	# 42-44
    sprite('jn413_10', 6)	# 45-50
    GFX_0('EffNoutou', 0)
    Unknown1019(50)
    sprite('jn413_11', 5)	# 51-55
    Unknown1019(50)
    sprite('jn413_12', 5)	# 56-60
    sprite('jn020_05', 3)	# 61-63
    sprite('jn020_06', 3)	# 64-66
    sprite('jn020_07', 3)	# 67-69
    label(1)
    sprite('jn020_08', 3)	# 70-72
    sprite('jn020_09', 3)	# 73-75
    gotoLabel(1)
    label(9)
    sprite('jn211_12', 2)	# 76-77
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('jn020_13', 2)	# 78-79
    sprite('jn020_14', 1)	# 80-80

@State
def CmnActChangeReturnAppealBurst():
    sprite('jn061_03', 35)	# 1-35
    sprite('jn061_04', 5)	# 36-40
    sprite('jn061_05', 5)	# 41-45
    sprite('jn061_06', 5)	# 46-50
    sprite('jn061_07', 5)	# 51-55
    sprite('jn061_08', 30)	# 56-85

@State
def CmnActChangePartnerQuickIn():

    def upon_IMMEDIATE():
        Unknown28(8, '_NEUTRAL')
        Unknown3001(0)
        Unknown3004(42)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('jn032_11', 3)	# 1-3
    sprite('jn032_11', 5)	# 4-8
    setInvincible(0)
    sprite('jn032_11', 7)	# 9-15
    sprite('jn032_12', 7)	# 16-22
    Unknown1084(1)
    sprite('jn031_07', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('jn033_00', 1)	# 1-1
    sprite('jn033_01', 2)	# 2-3
    sprite('jn033_02', 2)	# 4-5
    sprite('jn033_02', 1)	# 6-6
    sprite('jn033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('jn033_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jn033_05', 3)	# 13-15
    sprite('jn033_06', 3)	# 16-18

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
    sprite('jn020_04', 4)	# 3-6
    Unknown1019(95)
    sprite('jn020_05', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('jn020_12', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckDriveFlash')
        Unknown1084(1)
        Unknown21015('6963655f73686f745f65780000000000000000000000000000000000000000006810000000000000')
        Unknown21015('6169725f6963655f73686f745f657800000000000000000000000000000000006810000000000000')
        Unknown21015('6963655f73686f745f65785f41737369737400000000000000000000000000006810000000000000')
    sprite('jn400_00', 3)	# 1-3
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn400_01', 3)	# 4-6
    SFX_3('jnse_22')
    GFX_0('jnef_25percent', -1)
    Unknown7007('626a6e3230315f30000000000000000064000000626a6e3230315f31000000000000000064000000626a6e3230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn400_02', 19)	# 7-25
    Unknown38(7, 1)
    sprite('jn400_03', 4)	# 26-29
    GFX_0('ice_shot_ex_Assist', 0)
    sprite('jn400_04', 4)	# 30-33
    SFX_0('003_swing_grap_0_1')
    sprite('jn400_05', 4)	# 34-37
    sprite('jn400_06', 4)	# 38-41
    sprite('jn400_07', 4)	# 42-45
    sprite('jn400_08', 4)	# 46-49
    sprite('jn400_09', 4)	# 50-53
    sprite('jn400_10', 4)	# 54-57
    sprite('jn400_11', 4)	# 58-61
    sprite('jn400_12', 4)	# 62-65
    Recovery()
    sprite('jn400_13', 3)	# 66-68
    sprite('jn400_14', 2)	# 69-70
    sprite('jn400_15', 2)	# 71-72
    Unknown3029(0)

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(43000)
        AirUntechableTime(60)
        PushbackX(12000)
        Hitstop(16)
        Unknown9016(1)
        Unknown11042(1)
        callSubroutine('CheckDriveFlash')
    sprite('jn405_00', 3)	# 1-3
    sprite('jn405_01', 3)	# 4-6
    sprite('jn405_02', 2)	# 7-8
    sprite('jn405_03', 1)	# 9-9
    GFX_0('EFF28AtkA', 0)
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    SFX_1('jn206')
    sprite('jn405_04', 3)	# 10-12	 **attackbox here**
    SFX_3('jnse_21')
    sprite('jn405_04', 5)	# 13-17	 **attackbox here**
    StartMultihit()
    sprite('jn405_05', 3)	# 18-20
    Recovery()
    sprite('jn405_06', 3)	# 21-23
    sprite('jn405_07', 2)	# 24-25
    sprite('jn405_07ex', 2)	# 26-27
    sprite('jn405_08', 2)	# 28-29
    sprite('jn405_08ex', 2)	# 30-31
    sprite('jn405_09', 2)	# 32-33
    sprite('jn405_09ex', 2)	# 34-35
    sprite('jn405_10', 2)	# 36-37
    sprite('jn405_11', 3)	# 38-40
    GFX_0('EffNoutou', 0)
    sprite('jn405_12', 2)	# 41-42
    sprite('jn405_13', 2)	# 43-44
    sprite('jn405_14', 2)	# 45-46
    sprite('jn405_15', 2)	# 47-48
    sprite('jn405_16', 2)	# 49-50

@State
def CmnActChangePartnerAssistAtk_C():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AttackP1(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        AirUntechableTime(26)
        Unknown9016(1)
        Unknown11042(1)

        def upon_STATE_END():
            GFX_0('IceBoard_koware', -1)
        Unknown2006()
        Unknown30040(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('jn020_12', 2)	# 1-2
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('jn020_13', 2)	# 3-4
    sprite('jn020_14', 1)	# 5-5
    sprite('jn408_00', 1)	# 6-6
    Unknown2017(1)
    Unknown2053(1)
    Unknown2034(1)
    Unknown1019(10)
    sprite('jn408_01', 1)	# 7-7
    physicsXImpulse(-3000)
    physicsYImpulse(16000)
    Unknown1043()
    sprite('jn408_01', 2)	# 8-9
    sprite('jn408_02', 1)	# 10-10
    GFX_0('IceBoardASS', -1)
    Unknown38(4, 1)
    tag_voice(1, 'bjn210_0', 'bjn210_1', 'bjn210_2', '')
    sprite('jn408_03', 1)	# 11-11
    sprite('jn408_04', 1)	# 12-12
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)	# 13-15
    SFX_0('000_airdash_0')

    def upon_78():
        sendToLabel(110)
    sprite('jn408_06ex02', 2)	# 16-17	 **attackbox here**
    physicsXImpulse(60000)
    Unknown2016(60)
    Unknown2015(150)
    Unknown23029(4, 4001, 0)
    sprite('jn408_07ex02', 2)	# 18-19	 **attackbox here**
    sprite('jn408_06ex02', 2)	# 20-21	 **attackbox here**
    sprite('jn408_07ex02', 2)	# 22-23	 **attackbox here**
    sprite('jn408_06ex02', 2)	# 24-25	 **attackbox here**
    sprite('jn408_07ex02', 2)	# 26-27	 **attackbox here**
    if SLOT_2:
        _gotolabel(110)
    label(0)
    sprite('jn408_08', 5)	# 28-32
    clearUponHandler(78)
    clearUponHandler(1)
    sendToLabelUpon(2, 100)
    Unknown13(4)
    GFX_0('IceBoard_koware', -1)
    Recovery()
    Unknown2016(-1)
    Unknown2015(-1)
    Unknown1019(10)
    Unknown1034(0)
    physicsYImpulse(14000)
    Unknown1043()
    label(9)
    sprite('jn408_09', 3)	# 33-35
    sprite('jn408_10', 3)	# 36-38
    loopRest()
    gotoLabel(9)
    label(100)
    Unknown1084(1)
    sprite('jn020_10', 5)	# 39-43
    sprite('jn020_11', 5)	# 44-48
    sprite('jn020_13', 6)	# 49-54
    ExitState()
    label(110)
    sprite('jn408_11', 1)	# 55-55
    RefreshMultihit()
    Unknown13(4)
    GFX_0('IceBoard_koware', -1)
    clearUponHandler(78)
    AttackLevel_(3)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirUntechableTime(30)
    AirPushbackY(-28000)
    YImpluseBeforeWallbounce(1000)
    Unknown9310(1)
    Hitstop(8)
    Unknown11108('03000000')
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown9016(1)
    if SLOT_109:
        Unknown9250(5)
        Unknown9262(45)
    Unknown23087(120000)
    sendToLabelUpon(2, 11)
    sprite('jn408_11', 1)	# 56-56
    physicsXImpulse(20000)
    physicsYImpulse(25000)
    setGravity(2500)
    sprite('jn408_12', 2)	# 57-58
    sprite('jn408_13', 3)	# 59-61
    sprite('jn408_14', 3)	# 62-64
    tag_voice(0, 'bjn211_0', 'bjn211_1', 'bjn211_2', '')
    sprite('jn408_15', 3)	# 65-67
    Unknown1019(80)
    sprite('jn408_16ex01', 2)	# 68-69	 **attackbox here**
    GFX_0('zan408', 0)
    SFX_0('009_swing_rapier_1')
    Unknown1019(80)
    sprite('jn408_17', 2)	# 70-71	 **attackbox here**
    sprite('jn408_18', 2)	# 72-73
    Recovery()
    sprite('jn408_19', 32767)	# 74-32840
    label(11)
    sprite('jn408_20', 3)	# 32841-32843
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown23087(-1)
    sprite('jn408_21', 3)	# 32844-32846
    sprite('jn408_22', 2)	# 32847-32848
    sprite('jn408_23', 2)	# 32849-32850
    sprite('jn408_24', 2)	# 32851-32852
    sprite('jn408_25', 2)	# 32853-32854
    sprite('jn408_26', 2)	# 32855-32856
    GFX_0('EffNoutou', 0)
    sprite('jn408_27', 2)	# 32857-32858
    sprite('jn408_28', 2)	# 32859-32860

@State
def CmnActChangePartnerAttackIn():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('keep', 180)	# 1-180

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
    Unknown2036(79, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-245000)
    Unknown1019(4)
    label(0)
    sprite('jn020_08', 4)	# 3-6
    sprite('jn020_09', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateAntiAirShotDDDOD')
    else:
        enterState('UltimateAntiAirShotDDD')

@State
def UltimateAntiAirShotDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown11063(1)
        Unknown9016(1)
        AttackLevel_(4)
        Damage(500)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(-10000)
        AirUntechableTime(80)
        Unknown11064(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9250(60)
        Unknown9262(180)
        Unknown9019(1)
        Unknown11084(1)
        Unknown11066(1)
        Unknown30063(1)
        Unknown11069('Yukikazedmy')
        Unknown2018(0, 80)

        def upon_78():
            Unknown23027()
            Unknown2037(1)
        setInvincible(1)
    sprite('jn433_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_01', 4)	# 3-6
    sprite('jn433_02', 4)	# 7-10
    sprite('jn433_03', 4)	# 11-14
    sprite('jn433_04', 4)	# 15-18
    sprite('jn433_05', 4)	# 19-22
    sprite('jn433_06', 4)	# 23-26
    sprite('jn433_07', 4)	# 27-30
    sprite('jn433_08', 4)	# 31-34
    sprite('jn433_09', 4)	# 35-38
    sprite('jn433_10', 4)	# 39-42
    sprite('jn433_11', 4)	# 43-46
    sprite('jn433_12', 4)	# 47-50
    sprite('jn433_13', 4)	# 51-54
    sprite('jn433_14', 3)	# 55-57	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_DD', 0)
    ScreenShake(0, 16000)
    teleportRelativeX(565333)
    sprite('jn433_15', 3)	# 58-60	 **attackbox here**
    sprite('jn433_16', 3)	# 61-63	 **attackbox here**
    sprite('jn433_15', 3)	# 64-66	 **attackbox here**
    sprite('jn433_16', 3)	# 67-69	 **attackbox here**
    loopRest()
    if SLOT_2:
        _gotolabel(444)
    sprite('jn433_17', 4)	# 70-73
    setInvincible(0)
    sprite('jn433_18', 4)	# 74-77
    sprite('jn433_19', 4)	# 78-81
    sprite('jn433_20', 4)	# 82-85
    sprite('jn433_21', 4)	# 86-89
    sprite('jn433_22', 4)	# 90-93
    sprite('jn433_23', 4)	# 94-97
    sprite('jn433_24', 4)	# 98-101
    sprite('jn433_25', 4)	# 102-105
    sprite('jn433_26', 4)	# 106-109
    sprite('jn433_27', 4)	# 110-113
    sprite('jn433_28', 4)	# 114-117
    sprite('jn433_30', 4)	# 118-121
    sprite('jn433_31', 4)	# 122-125
    sprite('jn433_32', 4)	# 126-129
    sprite('jn433_33', 4)	# 130-133
    sprite('jn433_34', 4)	# 134-137
    sprite('jn433_35', 4)	# 138-141
    sprite('jn433_36', 4)	# 142-145
    sprite('jn000_00', 1)	# 146-146
    Unknown2005()
    loopRest()
    ExitState()
    label(444)
    sprite('jn433_17', 4)	# 147-150
    sprite('jn433_18', 4)	# 151-154
    sprite('jn433_19', 4)	# 155-158
    sprite('jn433_20', 4)	# 159-162
    tag_voice(0, 'bjn254_0', 'bjn254_0', '', '')
    sprite('jn433_21', 4)	# 163-166
    sprite('jn433_22', 4)	# 167-170
    sprite('jn433_23', 4)	# 171-174
    sprite('jn433_24', 4)	# 175-178
    sprite('jn433_25', 4)	# 179-182
    sprite('jn433_26', 4)	# 183-186
    sprite('jn433_27', 30)	# 187-216
    sprite('jn433_28', 4)	# 217-220
    GFX_0('EffNoutou', 0)
    sprite('jn433_29', 5)	# 221-225
    ScreenShake(26000, 0)
    GFX_0('Yukikazedmy', -1)
    GFX_0('DDD_Snow', -1)
    sprite('jn433_30', 5)	# 226-230
    sprite('jn433_31', 5)	# 231-235
    sprite('jn433_32', 5)	# 236-240
    sprite('jn433_33', 5)	# 241-245
    sprite('jn433_28', 34)	# 246-279
    sprite('jn433_34', 5)	# 280-284
    sprite('jn433_35', 5)	# 285-289
    sprite('jn433_36', 5)	# 290-294
    sprite('jn000_00', 1)	# 295-295
    Unknown2005()

@State
def UltimateAntiAirShotDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown11063(1)
        Unknown9016(1)
        AttackLevel_(4)
        Damage(200)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(-10000)
        AirUntechableTime(80)
        Unknown11064(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9250(60)
        Unknown9262(180)
        Unknown9019(1)
        Unknown11084(1)
        Unknown11066(1)
        Unknown30063(1)
        Unknown11069('UltimateAntiAirShotDDDOD')
        Unknown2018(0, 80)

        def upon_78():
            Unknown23027()
            Unknown2037(1)
        setInvincible(1)
    sprite('jn433_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_01', 4)	# 3-6
    sprite('jn433_02', 4)	# 7-10
    sprite('jn433_03', 4)	# 11-14
    sprite('jn433_04', 4)	# 15-18
    sprite('jn433_05', 4)	# 19-22
    sprite('jn433_06', 4)	# 23-26
    sprite('jn433_07', 4)	# 27-30
    sprite('jn433_08', 4)	# 31-34
    sprite('jn433_09', 4)	# 35-38
    sprite('jn433_10', 4)	# 39-42
    sprite('jn433_11', 4)	# 43-46
    sprite('jn433_12', 4)	# 47-50
    sprite('jn433_13', 4)	# 51-54
    sprite('jn433_14', 3)	# 55-57	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_DD', 0)
    ScreenShake(0, 16000)
    teleportRelativeX(565333)
    sprite('jn433_15', 3)	# 58-60	 **attackbox here**
    sprite('jn433_16', 3)	# 61-63	 **attackbox here**
    sprite('jn433_15', 3)	# 64-66	 **attackbox here**
    sprite('jn433_16', 3)	# 67-69	 **attackbox here**
    loopRest()
    if SLOT_2:
        _gotolabel(444)
    sprite('jn433_17', 4)	# 70-73
    setInvincible(0)
    sprite('jn433_18', 4)	# 74-77
    sprite('jn433_19', 4)	# 78-81
    sprite('jn433_20', 4)	# 82-85
    sprite('jn433_21', 4)	# 86-89
    sprite('jn433_22', 4)	# 90-93
    sprite('jn433_23', 4)	# 94-97
    sprite('jn433_24', 4)	# 98-101
    sprite('jn433_25', 4)	# 102-105
    sprite('jn433_26', 4)	# 106-109
    sprite('jn433_27', 4)	# 110-113
    sprite('jn433_28', 4)	# 114-117
    sprite('jn433_30', 4)	# 118-121
    sprite('jn433_31', 4)	# 122-125
    sprite('jn433_32', 4)	# 126-129
    sprite('jn433_33', 4)	# 130-133
    sprite('jn433_34', 4)	# 134-137
    sprite('jn433_35', 4)	# 138-141
    sprite('jn433_36', 4)	# 142-145
    sprite('jn000_00', 1)	# 146-146
    Unknown2005()
    loopRest()
    ExitState()
    label(444)
    sprite('jn433_01', 4)	# 147-150
    Unknown2006()
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('jn433_02', 4)	# 151-154
    sprite('jn433_03', 4)	# 155-158
    sprite('jn433_04', 4)	# 159-162
    sprite('jn433_05', 4)	# 163-166
    sprite('jn433_07', 1)	# 167-167
    sprite('jn433_09', 1)	# 168-168
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_14', 3)	# 169-171	 **attackbox here**
    RefreshMultihit()
    Hitstop(1)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(500000)
    teleportRelativeY(0)
    Unknown2015(20)
    GFX_0('AstralStartPtc', -1)
    sprite('jn433_15', 3)	# 172-174	 **attackbox here**
    Unknown2015(-1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn433_16', 3)	# 175-177	 **attackbox here**
    loopRest()
    sprite('jn433_01', 1)	# 178-178
    Unknown2006()
    sprite('jn433_02', 1)	# 179-179
    sprite('jn433_03', 1)	# 180-180
    sprite('jn433_04', 1)	# 181-181
    sprite('jn433_05', 1)	# 182-182
    sprite('jn433_07', 1)	# 183-183
    sprite('jn433_09', 1)	# 184-184
    sprite('jn433_14', 2)	# 185-186	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(400000)
    teleportRelativeY(0)
    Unknown2015(20)
    sprite('jn433_15', 1)	# 187-187	 **attackbox here**
    Unknown2015(-1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn433_16', 1)	# 188-188	 **attackbox here**
    loopRest()
    sprite('jn433_01', 1)	# 189-189
    Unknown2006()
    sprite('jn433_02', 1)	# 190-190
    sprite('jn433_03', 1)	# 191-191
    sprite('jn433_04', 1)	# 192-192
    sprite('jn433_05', 1)	# 193-193
    sprite('jn433_07', 1)	# 194-194
    sprite('jn433_09', 1)	# 195-195
    sprite('jn433_14', 1)	# 196-196	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(300000)
    teleportRelativeY(0)
    Unknown2015(20)
    sprite('jn433_15', 1)	# 197-197	 **attackbox here**
    Unknown2015(-1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn433_16', 1)	# 198-198	 **attackbox here**
    loopRest()
    sprite('jn433_01', 1)	# 199-199
    Unknown2006()
    sprite('jn433_02', 1)	# 200-200
    sprite('jn433_03', 1)	# 201-201
    sprite('jn433_04', 1)	# 202-202
    sprite('jn433_05', 1)	# 203-203
    sprite('jn433_07', 1)	# 204-204
    sprite('jn433_09', 1)	# 205-205
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_14', 3)	# 206-208	 **attackbox here**
    RefreshMultihit()
    Unknown11069('YukikazedmyOD')
    Unknown3038(1)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(275000)
    teleportRelativeY(0)
    Unknown2015(20)
    sprite('jn414_09', 1)	# 209-209	 **attackbox here**
    Unknown2005()
    Unknown3038(0)
    Unknown1045(-10000)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn414_09', 2)	# 210-211	 **attackbox here**
    StartMultihit()
    sprite('jn414_10', 20)	# 212-231
    sprite('jn414_10', 20)	# 232-251
    tag_voice(0, 'bjn254_0', 'bjn254_0', '', '')
    sprite('jn414_11', 6)	# 252-257
    GFX_0('EffNoutou', 0)
    sprite('jn414_12', 70)	# 258-327
    ScreenShake(40000, 40000)
    GFX_0('YukikazedmyOD', -1)
    GFX_0('DDD_Snow', -1)
    sprite('jn414_13', 5)	# 328-332
    sprite('jn414_14', 5)	# 333-337

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
    sprite('null', 1)	# 121-121
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    Unknown1007(1000000)
    physicsXImpulse(60000)
    physicsYImpulse(-40000)
    sprite('jn413_00', 6)	# 122-127
    sprite('jn413_01', 6)	# 128-133
    sprite('jn413_02', 6)	# 134-139
    sprite('jn413_05', 6)	# 140-145
    sprite('jn413_06', 3)	# 146-148
    Unknown1084(1)
    physicsXImpulse(-9000)
    physicsYImpulse(20000)
    setGravity(1800)
    SFX_0('009_swing_rapier_2')
    SFX_3('jnse_21')
    GFX_0('EFF413C', -1)
    Unknown2053(1)
    sendToLabelUpon(2, 9)
    sprite('jn413_07', 3)	# 149-151	 **attackbox here**
    sprite('jn413_08', 3)	# 152-154
    Unknown1019(50)
    sprite('jn413_09', 3)	# 155-157
    sprite('jn413_10', 6)	# 158-163
    GFX_0('EffNoutou', 0)
    Unknown1019(50)
    sprite('jn413_11', 5)	# 164-168
    Unknown1019(50)
    sprite('jn413_12', 5)	# 169-173
    sprite('jn020_05', 3)	# 174-176
    sprite('jn020_06', 3)	# 177-179
    sprite('jn020_07', 3)	# 180-182
    label(1)
    sprite('jn020_08', 3)	# 183-185
    sprite('jn020_09', 3)	# 186-188
    gotoLabel(1)
    label(9)
    sprite('jn211_12', 3)	# 189-191
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('jn020_13', 4)	# 192-195
    sprite('jn020_14', 3)	# 196-198

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(800)
        Unknown11092(1)
        PushbackX(-5000)
        AirPushbackY(12000)
        AirPushbackX(-3000)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('jn201_00', 2)	# 1-2
    sprite('jn201_01', 2)	# 3-4
    sprite('jn201_02', 2)	# 5-6
    Unknown7009(0)
    sprite('jn201_03', 2)	# 7-8	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    sprite('jn201_04', 2)	# 9-10	 **attackbox here**
    sprite('jn201_05', 1)	# 11-11
    sprite('jn201_06', 1)	# 12-12
    sprite('jn201_07', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    PushbackX(-10000)
    AirPushbackX(-2600)
    AirPushbackY(8000)
    sprite('jn201_08', 4)	# 14-17
    Recovery()
    Unknown2063()
    sprite('jn201_09', 5)	# 18-22
    sprite('jn201_10', 5)	# 23-27
    sprite('jn201_11', 5)	# 28-32

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
    sprite('jn200_00', 1)	# 1-1
    Unknown1051(60)
    sprite('jn200_01', 3)	# 2-4
    sprite('jn200_02', 1)	# 5-5
    Unknown7009(0)
    SFX_0('003_swing_grap_0_0')
    sprite('jn200_03', 3)	# 6-8	 **attackbox here**
    sprite('jn200_03', 3)	# 9-11	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('jn200_04', 4)	# 12-15
    sprite('jn200_05', 4)	# 16-19

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('jn213_00', 2)	# 1-2
    sprite('jn213_01', 2)	# 3-4
    sprite('jn213_02', 2)	# 5-6
    Unknown2015(120)
    sprite('jn213_03', 2)	# 7-8
    GFX_0('ModelMagicCircle2', 1)
    Unknown8004(100, 0, 1)
    ScreenShake(0, 5000)
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('jn213_04', 3)	# 9-11
    GFX_0('EffAtk6D', 0)
    Unknown2015(150)
    sprite('jn213_05', 3)	# 12-14
    sprite('jn213_06', 3)	# 15-17
    sprite('jn213_07', 3)	# 18-20
    sprite('jn213_08', 6)	# 21-26
    sprite('jn213_09', 3)	# 27-29	 **attackbox here**
    Unknown2015(120)
    Recovery()
    Unknown2063()
    sprite('jn213_10', 3)	# 30-32
    Unknown2015(-1)
    sprite('jn213_11', 3)	# 33-35
    sprite('jn213_12', 3)	# 36-38
    sprite('jn213_13', 3)	# 39-41
    sprite('jn213_14', 3)	# 42-44
    sprite('jn213_15', 3)	# 45-47
    sprite('jn213_16', 3)	# 48-50

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(650)
        AttackP2(85)
        Unknown11092(1)
        GroundedHitstunAnimation(4)
        Unknown11001(9, 0, 2)
        AirPushbackX(2500)
        AirPushbackY(2500)
        PushbackX(3000)
        Hitstop(0)
        Unknown9016(1)
        JumpCancel_(0)

        def upon_STATE_END():
            Unknown3001(255)
        callSubroutine('CheckDriveFlash')
    sprite('jn410_00', 5)	# 1-5
    sprite('jn410_01', 1)	# 6-6
    sprite('jn410_02', 1)	# 7-7
    tag_voice(1, 'bjn213_0', 'bjn213_1', 'bjn213_2', '')
    sprite('jn410_03ex01', 2)	# 8-9	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    RefreshMultihit()
    sprite('jn410_04', 1)	# 10-10
    sprite('jn410_05', 1)	# 11-11
    Unknown3001(0)
    sprite('jn410_06', 1)	# 12-12
    Unknown8000(100, 1, 1)
    sprite('jn410_07ex01', 2)	# 13-14	 **attackbox here**
    Unknown3001(255)
    SFX_0('009_swing_rapier_0')
    RefreshMultihit()
    sprite('jn410_08', 1)	# 15-15
    sprite('jn410_09', 1)	# 16-16
    Unknown3001(0)
    sprite('jn410_10', 1)	# 17-17
    Unknown3001(255)
    Unknown8000(100, 1, 1)
    sprite('jn410_11ex01', 2)	# 18-19	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    RefreshMultihit()
    sprite('jn410_12', 1)	# 20-20
    sprite('jn410_13', 1)	# 21-21
    Unknown3001(0)
    sprite('jn410_14', 1)	# 22-22
    Unknown3001(255)
    Unknown8000(100, 1, 1)
    sprite('jn410_15ex01', 2)	# 23-24	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    RefreshMultihit()

    def upon_ON_HIT_OR_BLOCK():
        AirPushbackY(20000)
        AirPushbackX(15000)
        AirUntechableTime(40)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(2)
        Unknown9130(39)
        Unknown9142(29)
        PushbackX(19800)
        Unknown14070('RushAssaultFinish')
        JumpCancel_(1)
    sprite('jn410_16', 2)	# 25-26
    Unknown14072('RushAssaultFinish')
    Recovery()
    Unknown2063()
    sprite('jn410_17', 2)	# 27-28
    sprite('jn410_18', 4)	# 29-32
    sprite('jn410_19', 5)	# 33-37
    GFX_0('EffNoutou', 0)
    Unknown14074('RushAssaultFinish')
    sprite('jn410_19', 10)	# 38-47
    sprite('jn410_20', 5)	# 48-52

@State
def RushAssaultFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(60)
        Unknown9142(50)
        AirPushbackY(10000)
        AirPushbackX(-5000)
        AirUntechableTime(40)
        PushbackX(-19800)
        Unknown9250(10)
        Unknown9262(70)
        Hitstop(0)
        Unknown9016(1)
        Unknown11068(1)
        Unknown11056(0)
        JumpCancel_(0)
        Unknown9019(1)

        def upon_78():
            clearUponHandler(78)
            Unknown2037(1)
            Unknown1086(22)
            teleportRelativeX(200000)
            teleportRelativeY(0)
            Unknown2015(20)
            sendToLabel(0)
        SLOT_6 = 0

        def upon_82():
            SLOT_6 = 1

        def upon_STATE_END():
            Unknown3038(0)
    sprite('jn433_01', 3)	# 1-3
    SFX_3('jnse_21')
    sprite('jn433_01', 1)	# 4-4
    sprite('jn433_02', 2)	# 5-6
    sprite('jn433_03', 2)	# 7-8
    sprite('jn433_04', 2)	# 9-10
    sprite('jn433_05', 2)	# 11-12
    sprite('jn433_07', 1)	# 13-13
    sprite('jn433_09', 1)	# 14-14
    sprite('jn433_11', 1)	# 15-15
    sprite('jn433_13', 1)	# 16-16
    sprite('jn433_14ex01', 10)	# 17-26	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown3038(1)
    physicsXImpulse(60000)
    Unknown2017(0)
    Unknown11069('RushAssaultFinishAtkObj')
    label(0)
    sprite('jn433_14ex01', 2)	# 27-28	 **attackbox here**
    Unknown23027()
    Unknown1084(1)
    Unknown1045(20000)
    Unknown3038(0)
    tag_voice(0, 'bjn214_0', 'bjn214_1', 'bjn214_2', '')
    sprite('jn433_15', 3)	# 29-31	 **attackbox here**
    Unknown2015(-1)
    Unknown2017(1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn433_16', 3)	# 32-34	 **attackbox here**
    sprite('jn433_17', 4)	# 35-38
    Recovery()
    Unknown2063()
    sprite('jn433_18', 4)	# 39-42
    sprite('jn433_19', 4)	# 43-46
    Unknown1045(0)
    sprite('jn433_20', 4)	# 47-50
    sprite('jn433_21', 4)	# 51-54
    sprite('jn433_22', 4)	# 55-58
    sprite('jn433_23', 4)	# 59-62
    sprite('jn433_24', 4)	# 63-66
    sprite('jn433_25', 3)	# 67-69
    sprite('jn433_27', 2)	# 70-71
    sprite('jn433_28', 1)	# 72-72
    GFX_0('EffNoutou', 0)
    SFX_1('jn214')
    sprite('jn433_28', 1)	# 73-73
    if (not Unknown23166('CmnActFreeze')):
        if (not SLOT_2):
            sendToLabel(9)
    sprite('jn433_30', 4)	# 74-77
    GFX_0('RushAssaultFinishAtkObj', -1)
    sprite('jn433_31', 4)	# 78-81
    sprite('jn433_32', 4)	# 82-85
    sprite('jn433_33', 4)	# 86-89
    label(9)
    sprite('jn433_34', 4)	# 90-93
    Recovery()
    Unknown2063()
    sprite('jn433_35', 4)	# 94-97
    sprite('jn433_36', 4)	# 98-101
    sprite('jn000_00', 1)	# 102-102
    Unknown2005()

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('jn202_00', 2)	# 1-2
    sprite('jn202_01', 2)	# 3-4
    sprite('jn202_02', 2)	# 5-6
    Unknown7009(2)
    sprite('jn202_03', 3)	# 7-9
    sprite('jn202_04', 2)	# 10-11	 **attackbox here**
    GFX_0('zan_b0', -1)
    SFX_0('009_swing_rapier_1')
    sprite('jn202_05', 2)	# 12-13	 **attackbox here**
    sprite('jn202_05', 5)	# 14-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('jn202_06', 2)	# 19-20
    sprite('jn202_08', 3)	# 21-23
    sprite('jn202_09', 3)	# 24-26
    sprite('jn202_10', 2)	# 27-28
    sprite('jn202_11', 1)	# 29-29
    sprite('jn202_12', 1)	# 30-30
    sprite('jn202_14', 1)	# 31-31
    GFX_0('EffNoutou', 0)
    sprite('jn202_16', 1)	# 32-32

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(10)
        AirPushbackY(16000)
        AirPushbackX(10000)
        AirUntechableTime(20)
        PushbackX(19800)
        Unknown9016(1)
        Unknown9019(1)
        HitOrBlockCancel('NmlAtk5BBB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('45666641746b35440000000000000000000000000000000000000000000000007117000000000000')
    sprite('jn203_00', 1)	# 1-1
    sprite('jn203_01', 1)	# 2-2
    sprite('jn203_02', 1)	# 3-3
    Unknown7007('626a6e3130385f30000000000000000064000000626a6e3130385f31000000000000000064000000626a6e3130385f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('ModelMagicCircle1', 0)
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('jn203_03', 2)	# 4-5
    sprite('jn203_04', 2)	# 6-7
    sprite('jn203_05', 2)	# 8-9
    sprite('jn203_06', 2)	# 10-11
    sprite('jn203_07', 3)	# 12-14
    GFX_0('EffAtk5D', 0)
    ScreenShake(0, 5000)
    sprite('jn203_08', 8)	# 15-22	 **attackbox here**
    sprite('jn203_09', 3)	# 23-25
    Recovery()
    Unknown2063()
    sprite('jn203_10', 3)	# 26-28
    sprite('jn203_11', 3)	# 29-31
    sprite('jn203_12', 3)	# 32-34
    sprite('jn203_13', 3)	# 35-37

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP2(75)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackY(32000)
        AirUntechableTime(28)
        Unknown9016(1)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        Unknown2004(1, 0)
        Unknown2015(120)
    sprite('jn212_00', 2)	# 1-2
    sprite('jn212_01', 2)	# 3-4
    sprite('jn212_02', 2)	# 5-6
    sprite('jn212_03', 2)	# 7-8
    Unknown7007('626a6e3130395f30000000000000000064000000626a6e3130395f31000000000000000064000000626a6e3130395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn212_04', 2)	# 9-10
    sprite('jn212_05', 2)	# 11-12
    sprite('jn212_06', 2)	# 13-14
    sprite('jn212_07', 3)	# 15-17	 **attackbox here**
    GFX_0('zan_a0', -1)
    SFX_0('009_swing_rapier_2')
    sprite('jn212_08', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('jn212_09', 3)	# 21-23
    sprite('jn212_10', 3)	# 24-26
    sprite('jn212_11', 3)	# 27-29
    sprite('jn212_12', 3)	# 30-32
    sprite('jn212_13', 3)	# 33-35
    sprite('jn212_14', 3)	# 36-38
    GFX_0('EffNoutou', 0)
    sprite('jn212_15', 5)	# 39-43
    sprite('jn212_16', 5)	# 44-48

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
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('jn231_00', 2)	# 1-2
    sprite('jn231_01', 2)	# 3-4
    sprite('jn231_02', 1)	# 5-5
    sprite('jn231_03', 1)	# 6-6
    Unknown7009(0)
    sprite('jn231_04', 1)	# 7-7
    sprite('jn231_05', 1)	# 8-8
    SFX_0('003_swing_grap_0_1')
    sprite('jn231_06', 2)	# 9-10	 **attackbox here**
    sprite('jn231_07', 2)	# 11-12
    Recovery()
    Unknown2063()
    sprite('jn231_08', 2)	# 13-14
    sprite('jn231_09', 2)	# 15-16
    sprite('jn231_10', 2)	# 17-18
    sprite('jn231_11', 2)	# 19-20
    sprite('jn231_12', 2)	# 21-22
    sprite('jn231_13', 2)	# 23-24
    sprite('jn231_14', 1)	# 25-25

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        Unknown9016(1)
        AirUntechableTime(24)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('jn232_00', 4)	# 1-4
    sprite('jn232_01', 3)	# 5-7
    sprite('jn232_02', 3)	# 8-10
    Unknown7007('626a6e3130365f30000000000000000064000000626a6e3130365f31000000000000000064000000626a6e3130365f320000000000000000640000000000000000000000000000000000000000000000')
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('jn232_03', 1)	# 11-11
    SFX_0('009_swing_rapier_2')
    sprite('jn232_04', 1)	# 12-12
    GFX_0('zan_d0', -1)
    sprite('jn232_06', 1)	# 13-13
    sprite('jn232_07', 3)	# 14-16	 **attackbox here**
    sprite('jn232_07', 6)	# 17-22	 **attackbox here**
    setInvincible(0)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('jn232_09', 3)	# 23-25
    sprite('jn232_11', 3)	# 26-28
    sprite('jn232_13', 3)	# 29-31
    sprite('jn232_14', 3)	# 32-34
    sprite('jn232_15', 3)	# 35-37
    WhiffCancelEnable(1)
    sprite('jn232_16', 5)	# 38-42
    GFX_0('EffNoutou', 0)
    sprite('jn232_17', 5)	# 43-47

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(16000)
        AirUntechableTime(26)
        Unknown9016(1)
        Unknown2004(1, 0)
    sprite('jn235_00', 2)	# 1-2
    sprite('jn235_01', 2)	# 3-4
    sprite('jn235_02', 2)	# 5-6
    SFX_0('009_swing_rapier_1')
    Unknown7007('626a6e3130375f30000000000000000064000000626a6e3130375f31000000000000000064000000626a6e3130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn235_03', 4)	# 7-10
    sprite('jn235_04', 2)	# 11-12
    Unknown2015(150)
    sprite('jn235_05', 4)	# 13-16	 **attackbox here**
    GFX_0('zan235', -1)
    sprite('jn235_06', 4)	# 17-20
    Recovery()
    Unknown2063()
    Unknown2015(-1)
    sprite('jn235_07', 4)	# 21-24
    sprite('jn235_08', 4)	# 25-28
    sprite('jn235_09', 4)	# 29-32
    sprite('jn235_10', 4)	# 33-36
    GFX_0('EffNoutou', 0)
    sprite('jn235_11', 4)	# 37-40
    sprite('jn235_12', 4)	# 41-44

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackX(3000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
    sprite('jn251_00', 2)	# 1-2
    sprite('jn251_01', 3)	# 3-5
    sprite('jn251_02', 3)	# 6-8
    Unknown7009(3)
    sprite('jn251_03', 3)	# 9-11	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    sprite('jn251_04', 3)	# 12-14	 **attackbox here**
    sprite('jn251_05', 3)	# 15-17	 **attackbox here**
    sprite('jn251_06', 4)	# 18-21
    Recovery()
    Unknown2063()
    sprite('jn251_07', 4)	# 22-25
    sprite('jn251_08', 4)	# 26-29
    sprite('jn251_09', 4)	# 30-33
    sprite('jn251_10', 4)	# 34-37
    sprite('jn251_11', 4)	# 38-41
    sprite('jn251_12', 4)	# 42-45

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirPushbackX(8000)
        AirPushbackY(23000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('jn412_00', 5)	# 1-5
    sprite('jn412_01', 2)	# 6-7
    Unknown7009(4)
    sprite('jn412_02', 2)	# 8-9
    GFX_0('zan412', 0)
    sprite('jn412_03', 6)	# 10-15	 **attackbox here**
    SFX_0('009_swing_rapier_1')
    sprite('jn412_04', 6)	# 16-21
    Recovery()
    Unknown2063()
    sprite('jn412_05', 2)	# 22-23
    sprite('jn412_06', 2)	# 24-25
    sprite('jn412_07', 4)	# 26-29
    GFX_0('EffNoutou', 0)
    sprite('jn412_08', 3)	# 30-32
    sprite('jn412_09', 3)	# 33-35

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirPushbackX(8000)
        AirPushbackY(23000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5BB')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('jn252_00', 2)	# 1-2
    sprite('jn252_01', 2)	# 3-4
    sprite('jn252_01', 2)	# 5-6
    Unknown7009(5)
    sprite('jn252_02', 4)	# 7-10
    sprite('jn252_03', 2)	# 11-12
    sprite('jn252_04', 2)	# 13-14	 **attackbox here**
    GFX_0('zan_e0', -1)
    SFX_0('009_swing_rapier_1')
    sprite('jn252_05', 3)	# 15-17	 **attackbox here**
    sprite('jn252_06', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('jn252_07', 3)	# 21-23
    sprite('jn252_08', 3)	# 24-26
    sprite('jn252_09', 3)	# 27-29
    sprite('jn252_10', 3)	# 30-32
    GFX_0('EffNoutou', 0)
    sprite('jn252_11', 3)	# 33-35
    sprite('jn252_12', 3)	# 36-38
    sprite('jn252_13', 3)	# 39-41

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        Unknown9016(1)
        HitOverhead(0)
        AirPushbackX(3000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(28)
        Unknown11034(1)
        Unknown11033(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9019(1)
        callSubroutine('CheckDriveFlash')
    sprite('jn253_00', 2)	# 1-2
    sprite('jn253_01', 2)	# 3-4
    Unknown7007('626a6e3130385f30000000000000000064000000626a6e3130385f31000000000000000064000000626a6e3130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn253_02', 3)	# 5-7
    sprite('jn253_03', 3)	# 8-10
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    GFX_0('ModelMagicCircle3', 1)
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown22004(6, 1)
    sprite('jn253_04', 3)	# 11-13
    GFX_0('EffAtk8D', 0)
    sprite('jn253_05', 3)	# 14-16	 **attackbox here**
    GFX_0('EffNoutou', 1)
    sprite('jn253_06', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('jn253_07', 3)	# 20-22
    sprite('jn253_08', 3)	# 23-25
    sprite('jn253_09', 5)	# 26-30
    Unknown1018()
    Unknown1023()
    Unknown1019(60)
    YAccel(30)
    Unknown1043()
    sprite('jn253_10', 5)	# 31-35
    sprite('jn253_11', 5)	# 36-40
    sprite('jn253_12', 5)	# 41-45

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('jn414_00', 3)	# 1-3
    sprite('jn414_01', 3)	# 4-6
    tag_voice(1, 'bjn156_0', 'bjn156_1', '', '')
    sprite('jn414_02', 3)	# 7-9
    sprite('jn414_03', 4)	# 10-13
    sprite('jn414_06', 2)	# 14-15
    SFX_0('009_swing_rapier_1')
    sprite('jn414_07', 2)	# 16-17
    sprite('jn414_08', 2)	# 18-19
    SFX_0('009_swing_rapier_2')
    GFX_0('zan414', -1)
    sprite('jn414_09', 2)	# 20-21	 **attackbox here**
    StartMultihit()
    sprite('jn414_09', 3)	# 22-24	 **attackbox here**
    sprite('jn414_10', 6)	# 25-30
    Unknown3029(0)
    sprite('jn414_11', 6)	# 31-36
    GFX_0('EffNoutou', 0)
    sprite('jn414_12', 6)	# 37-42
    sprite('jn414_13', 3)	# 43-45
    sprite('jn414_14', 3)	# 46-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)
    sprite('jn414_10', 4)	# 1-4
    Unknown3029(0)
    sprite('jn414_11', 4)	# 5-8
    GFX_0('EffNoutou', 0)
    sprite('jn414_12', 5)	# 9-13
    sprite('jn414_13', 4)	# 14-17
    sprite('jn414_14', 3)	# 18-20
    sprite('jn202_00', 2)	# 21-22
    sprite('jn202_01', 2)	# 23-24
    sprite('jn202_02', 2)	# 25-26
    sprite('jn202_03', 3)	# 27-29
    sprite('jn202_04', 2)	# 30-31	 **attackbox here**
    GFX_0('zan_b0', -1)
    SFX_0('009_swing_rapier_1')
    tag_voice(1, 'bjn157_0', 'bjn157_1', '', '')
    sprite('jn202_05', 2)	# 32-33	 **attackbox here**
    sprite('jn202_05', 5)	# 34-38	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('jn202_06', 2)	# 39-40
    sprite('jn202_08', 3)	# 41-43
    sprite('jn202_09', 3)	# 44-46
    sprite('jn202_10', 2)	# 47-48
    sprite('jn202_11', 1)	# 49-49
    sprite('jn202_12', 1)	# 50-50
    sprite('jn202_14', 1)	# 51-51
    GFX_0('EffNoutou', 0)
    sprite('jn202_16', 1)	# 52-52
    sprite('jn000_00', 7)	# 53-59
    sprite('jn000_01', 7)	# 60-66
    sprite('jn000_02', 7)	# 67-73
    sprite('jn000_03', 7)	# 74-80
    sprite('jn000_04', 7)	# 81-87
    sprite('jn000_05', 7)	# 88-94
    sprite('jn000_06', 7)	# 95-101
    sprite('jn000_07', 7)	# 102-108
    sprite('jn000_08', 7)	# 109-115
    sprite('jn000_09', 7)	# 116-122
    label(10)
    sprite('jn000_00', 7)	# 123-129
    sprite('jn000_01', 7)	# 130-136
    sprite('jn000_02', 7)	# 137-143
    sprite('jn000_03', 7)	# 144-150
    sprite('jn000_04', 7)	# 151-157
    sprite('jn000_05', 7)	# 158-164
    sprite('jn000_06', 7)	# 165-171
    sprite('jn000_07', 7)	# 172-178
    sprite('jn000_08', 7)	# 179-185
    sprite('jn000_09', 7)	# 186-192
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 193-193

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('jn405_00', 5)	# 1-5
    sprite('jn405_01', 6)	# 6-11
    sprite('jn405_02', 2)	# 12-13
    sprite('jn405_03', 1)	# 14-14
    GFX_0('EFF28AtkA', 0)
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('jn405_04', 3)	# 15-17	 **attackbox here**
    SFX_3('jnse_21')
    sprite('jn405_05', 3)	# 18-20
    sprite('jn405_06', 3)	# 21-23
    sprite('jn405_07', 2)	# 24-25
    sprite('jn405_07ex', 2)	# 26-27
    sprite('jn405_08', 2)	# 28-29
    sprite('jn405_08ex', 2)	# 30-31
    sprite('jn405_09', 2)	# 32-33
    sprite('jn405_09ex', 2)	# 34-35
    sprite('jn405_10', 2)	# 36-37
    sprite('jn405_11', 3)	# 38-40
    GFX_0('EffNoutou', 0)
    sprite('jn405_12', 2)	# 41-42
    sprite('jn405_13', 2)	# 43-44
    sprite('jn405_14', 2)	# 45-46
    sprite('jn405_15', 2)	# 47-48
    sprite('jn405_16', 2)	# 49-50
    sprite('jn000_00', 7)	# 51-57
    sprite('jn000_01', 7)	# 58-64
    sprite('jn000_02', 7)	# 65-71
    sprite('jn000_03', 7)	# 72-78
    sprite('jn000_04', 7)	# 79-85
    sprite('jn000_05', 7)	# 86-92
    sprite('jn000_06', 7)	# 93-99
    sprite('jn000_07', 7)	# 100-106
    sprite('jn000_08', 7)	# 107-113
    sprite('jn000_09', 7)	# 114-120
    label(0)
    sprite('jn000_00', 7)	# 121-127
    sprite('jn000_01', 7)	# 128-134
    sprite('jn000_02', 7)	# 135-141
    sprite('jn000_03', 7)	# 142-148
    sprite('jn000_04', 7)	# 149-155
    sprite('jn000_05', 7)	# 156-162
    sprite('jn000_06', 7)	# 163-169
    sprite('jn000_07', 7)	# 170-176
    sprite('jn000_08', 7)	# 177-183
    sprite('jn000_09', 7)	# 184-190
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 191-191

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('jn407_05', 3)	# 1-3
    sprite('jn407_06', 3)	# 4-6
    sprite('jn407_07', 3)	# 7-9
    sprite('jn407_08', 3)	# 10-12
    sprite('jn407_09', 3)	# 13-15
    sprite('jn407_10', 2)	# 16-17
    sprite('jn407_11', 2)	# 18-19
    SFX_3('jnse_21')
    GFX_0('EFF28AtkD', 0)
    sprite('jn407_12ex2', 3)	# 20-22	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    tag_voice(0, 'bjn158_0', 'bjn158_1', '', '')
    sprite('jn407_13', 3)	# 23-25
    sprite('jn407_14', 3)	# 26-28
    sprite('jn407_15', 3)	# 29-31
    sprite('jn407_16', 3)	# 32-34
    sprite('jn407_17', 3)	# 35-37
    sprite('jn407_18', 3)	# 38-40
    sprite('jn407_19', 3)	# 41-43
    sprite('jn407_20', 3)	# 44-46
    sprite('jn407_21', 3)	# 47-49
    sprite('jn407_22', 3)	# 50-52
    sprite('jn407_23', 3)	# 53-55
    sprite('jn407_24', 3)	# 56-58
    GFX_0('EffNoutou', 0)
    sprite('jn407_25', 2)	# 59-60
    ExitState()
    label(1)
    sprite('jn433_00', 2)	# 61-62
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_01', 2)	# 63-64
    sprite('jn433_02', 2)	# 65-66
    sprite('jn433_03', 3)	# 67-69
    sprite('jn433_04', 3)	# 70-72
    sprite('jn433_05', 1)	# 73-73
    sprite('jn433_06', 1)	# 74-74
    sprite('jn433_07', 1)	# 75-75
    sprite('jn433_08', 1)	# 76-76
    sprite('jn433_09', 1)	# 77-77
    sprite('jn433_10', 1)	# 78-78
    sprite('jn433_13', 1)	# 79-79
    tag_voice(0, 'bjn158_0', 'bjn158_1', '', '')
    sprite('jn433_14', 3)	# 80-82	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_DD', 0)
    teleportRelativeX(600000)
    sprite('jn433_15', 3)	# 83-85	 **attackbox here**
    sprite('jn433_16', 3)	# 86-88	 **attackbox here**
    sprite('jn433_15', 3)	# 89-91	 **attackbox here**
    sprite('jn433_19', 2)	# 92-93
    sprite('jn433_20', 2)	# 94-95
    sprite('jn433_21', 2)	# 96-97
    sprite('jn433_22', 2)	# 98-99
    sprite('jn433_23', 2)	# 100-101
    sprite('jn433_24', 2)	# 102-103
    sprite('jn433_25', 2)	# 104-105
    sprite('jn433_26', 2)	# 106-107
    sprite('jn433_27', 2)	# 108-109
    sprite('jn433_28', 2)	# 110-111
    sprite('jn433_33', 2)	# 112-113
    sprite('jn433_34', 2)	# 114-115
    sprite('jn433_35', 2)	# 116-117
    sprite('jn433_36', 2)	# 118-119
    sprite('jn000_00', 1)	# 120-120

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
    sprite('jn408_11', 1)	# 29-29
    physicsXImpulse(46000)
    physicsYImpulse(-15000)
    setGravity(2500)
    Unknown8001(0, 100)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('jn408_12', 3)	# 30-32
    sprite('jn408_13', 3)	# 33-35
    sprite('jn408_14', 3)	# 36-38
    sprite('jn408_15', 3)	# 39-41
    Unknown1019(80)
    sprite('jn408_16ex01', 2)	# 42-43	 **attackbox here**
    GFX_0('zan408', 0)
    SFX_0('009_swing_rapier_1')
    sprite('jn408_17', 2)	# 44-45	 **attackbox here**
    sprite('jn408_18', 2)	# 46-47
    sprite('jn408_19', 20)	# 48-67
    label(1)
    sprite('jn408_20', 3)	# 68-70
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown23087(-1)
    sprite('jn408_21', 3)	# 71-73
    sprite('jn408_22', 2)	# 74-75
    sprite('jn408_23', 2)	# 76-77
    sprite('jn408_24', 2)	# 78-79
    sprite('jn408_25', 2)	# 80-81
    sprite('jn408_26', 2)	# 82-83
    GFX_0('EffNoutou', 0)
    sprite('jn408_27', 2)	# 84-85
    sprite('jn408_28', 2)	# 86-87
    sprite('jn000_00', 7)	# 88-94
    sprite('jn000_01', 7)	# 95-101
    sprite('jn000_02', 7)	# 102-108
    sprite('jn000_03', 7)	# 109-115
    sprite('jn000_04', 7)	# 116-122
    sprite('jn000_05', 7)	# 123-129
    sprite('jn000_06', 7)	# 130-136
    sprite('jn000_07', 7)	# 137-143
    sprite('jn000_08', 7)	# 144-150
    sprite('jn000_09', 7)	# 151-157

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('jn413_00', 2)	# 1-2
    sprite('jn413_01', 2)	# 3-4
    sprite('jn413_02', 2)	# 5-6
    sprite('jn413_05', 2)	# 7-8
    sprite('jn413_06', 3)	# 9-11
    SFX_0('009_swing_rapier_2')
    SFX_3('jnse_21')
    GFX_0('EFF413C', -1)
    sprite('jn413_07', 3)	# 12-14	 **attackbox here**
    sprite('jn413_08', 2)	# 15-16
    sprite('jn413_09', 2)	# 17-18
    sprite('jn413_10', 2)	# 19-20
    GFX_0('EffNoutou', 0)
    sprite('jn413_11', 2)	# 21-22
    sprite('jn413_12', 2)	# 23-24
    sprite('jn020_10', 3)	# 25-27
    clearUponHandler(2)
    sprite('jn020_11', 3)	# 28-30
    sprite('jn020_12', 3)	# 31-33
    sprite('jn020_13', 3)	# 34-36
    sprite('jn020_14', 3)	# 37-39
    loopRest()
    sprite('jn000_00', 7)	# 40-46
    sprite('jn000_01', 7)	# 47-53
    sprite('jn000_02', 7)	# 54-60
    sprite('jn000_03', 7)	# 61-67
    sprite('jn000_04', 7)	# 68-74
    sprite('jn000_05', 7)	# 75-81
    sprite('jn000_06', 7)	# 82-88
    sprite('jn000_07', 7)	# 89-95
    sprite('jn000_08', 7)	# 96-102
    sprite('jn000_09', 7)	# 103-109

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('jn407_05', 3)	# 1-3
    sprite('jn407_06', 3)	# 4-6
    sprite('jn407_07', 3)	# 7-9
    sprite('jn407_08', 3)	# 10-12
    sprite('jn407_09', 3)	# 13-15
    sprite('jn407_10', 2)	# 16-17
    sprite('jn407_11', 2)	# 18-19
    SFX_3('jnse_21')
    GFX_0('EFF28AtkD', 0)
    sprite('jn407_12ex2', 3)	# 20-22	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('jn407_13', 3)	# 23-25
    sprite('jn407_14', 3)	# 26-28
    sprite('jn407_15', 3)	# 29-31
    sprite('jn407_16', 3)	# 32-34
    sprite('jn407_17', 3)	# 35-37
    sprite('jn407_18', 3)	# 38-40
    sprite('jn407_19', 3)	# 41-43
    sprite('jn407_20', 3)	# 44-46
    sprite('jn407_21', 3)	# 47-49
    sprite('jn407_22', 3)	# 50-52
    sprite('jn407_23', 3)	# 53-55
    sprite('jn407_24', 3)	# 56-58
    GFX_0('EffNoutou', 0)
    sprite('jn407_25', 2)	# 59-60
    ExitState()
    label(1)
    sprite('jn433_00', 2)	# 61-62
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_01', 2)	# 63-64
    sprite('jn433_02', 2)	# 65-66
    sprite('jn433_03', 3)	# 67-69
    sprite('jn433_04', 3)	# 70-72
    sprite('jn433_05', 1)	# 73-73
    sprite('jn433_06', 1)	# 74-74
    sprite('jn433_07', 1)	# 75-75
    sprite('jn433_08', 1)	# 76-76
    sprite('jn433_09', 1)	# 77-77
    sprite('jn433_10', 1)	# 78-78
    sprite('jn433_13', 1)	# 79-79
    sprite('jn433_14', 3)	# 80-82	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_DD', 0)
    teleportRelativeX(600000)
    sprite('jn433_15', 3)	# 83-85	 **attackbox here**
    sprite('jn433_16', 3)	# 86-88	 **attackbox here**
    sprite('jn433_15', 3)	# 89-91	 **attackbox here**
    sprite('jn433_19', 2)	# 92-93
    sprite('jn433_20', 2)	# 94-95
    sprite('jn433_21', 2)	# 96-97
    sprite('jn433_22', 2)	# 98-99
    sprite('jn433_23', 2)	# 100-101
    sprite('jn433_24', 2)	# 102-103
    sprite('jn433_25', 2)	# 104-105
    sprite('jn433_26', 2)	# 106-107
    sprite('jn433_27', 2)	# 108-109
    sprite('jn433_28', 2)	# 110-111
    sprite('jn433_33', 2)	# 112-113
    sprite('jn433_34', 2)	# 114-115
    sprite('jn433_35', 2)	# 116-117
    sprite('jn433_36', 2)	# 118-119
    sprite('jn000_00', 1)	# 120-120

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
    sprite('jn032_12', 3)	# 1-3
    sprite('jn032_00', 4)	# 4-7
    sprite('jn032_01', 4)	# 8-11
    label(0)
    sprite('jn032_02', 4)	# 12-15
    sprite('jn032_03', 4)	# 16-19
    sprite('jn032_04', 4)	# 20-23
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 24-27
    sprite('jn032_06', 4)	# 28-31
    sprite('jn032_07', 4)	# 32-35
    sprite('jn032_08', 4)	# 36-39
    sprite('jn032_09', 4)	# 40-43
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jn310_00', 1)	# 48-48
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('jn310_01', 2)	# 49-50
    SFX_0('010_swing_sword_0')
    sprite('jn310_02', 3)	# 51-53	 **attackbox here**
    Unknown1084(1)
    sprite('jn310_02', 3)	# 54-56	 **attackbox here**
    Unknown23027()
    sprite('jn310_03', 6)	# 57-62
    SFX_4('bjn154')
    sprite('jn310_04', 8)	# 63-70
    sprite('jn310_05', 6)	# 71-76

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2018(0, 80)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9142(28)
        Unknown9130(28)
        PushbackX(6000)
        Hitstop(0)
        JumpCancel_(0)
    sprite('jn310_02', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('jn311_00', 5)	# 3-7
    GFX_0('jnef311', 1)
    GFX_0('ModelMagicCircle2', 1)
    SFX_1('bjn153')
    sprite('jn311_01', 4)	# 8-11	 **attackbox here**
    Unknown11069('ThrowExe')
    sprite('jn311_02', 4)	# 12-15
    sprite('jn311_03', 4)	# 16-19
    sprite('jn311_04', 4)	# 20-23
    sprite('jn311_05', 4)	# 24-27
    sprite('jn311_06', 4)	# 28-31
    sprite('jn311_07', 5)	# 32-36	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    AttackP2(50)
    Hitstop(0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(30000)
    AirUntechableTime(40)
    Unknown9019(1)
    Unknown9250(10)
    Unknown9262(54)
    Unknown11069('')

    def upon_12():
        JumpCancel_(1)
    sprite('jn311_08', 5)	# 37-41
    sprite('jn311_09', 5)	# 42-46
    sprite('jn311_10', 5)	# 47-51
    sprite('jn311_11', 5)	# 52-56
    sprite('jn311_12', 5)	# 57-61
    sprite('jn311_13', 5)	# 62-66
    sprite('jn311_14', 5)	# 67-71
    sprite('jn311_15', 5)	# 72-76

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
    sprite('jn032_12', 3)	# 1-3
    sprite('jn032_00', 4)	# 4-7
    sprite('jn032_01', 4)	# 8-11
    label(0)
    sprite('jn032_02', 4)	# 12-15
    sprite('jn032_03', 4)	# 16-19
    sprite('jn032_04', 4)	# 20-23
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 24-27
    sprite('jn032_06', 4)	# 28-31
    sprite('jn032_07', 4)	# 32-35
    sprite('jn032_08', 4)	# 36-39
    sprite('jn032_09', 4)	# 40-43
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jn310_00', 1)	# 48-48
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('jn310_01', 2)	# 49-50
    SFX_0('010_swing_sword_0')
    sprite('jn310_02', 3)	# 51-53	 **attackbox here**
    Unknown1084(1)
    sprite('jn310_02', 3)	# 54-56	 **attackbox here**
    Unknown23027()
    sprite('jn310_03', 6)	# 57-62
    SFX_4('bjn154')
    sprite('jn310_04', 8)	# 63-70
    sprite('jn310_05', 6)	# 71-76

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(40)
        Unknown9019(1)
        Unknown9250(10)
        Unknown9262(54)
        AirPushbackX(5500)
        AirPushbackY(30000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown2004(1, 0)
        Unknown2018(0, 80)
        Unknown13021(1)
        Unknown21005(1)
        Unknown11056(1)
    sprite('jn310_02', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('jn313_00', 5)	# 3-7
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('jn313_01', 5)	# 8-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('jn313_02', 5)	# 13-17
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('jn313_03', 5)	# 18-22
    SFX_4('bjn153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('jn313_04', 5)	# 23-27
    GFX_0('jnef311', 1)
    GFX_0('ModelMagicCircle2', 1)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('jn313_05', 30)	# 28-57
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('jn313_06', 5)	# 58-62	 **attackbox here**
    sprite('jn313_07', 5)	# 63-67
    sprite('jn313_08', 5)	# 68-72
    sprite('jn313_09', 5)	# 73-77
    sprite('jn313_10', 5)	# 78-82
    sprite('jn313_11', 5)	# 83-87
    sprite('jn313_12', 5)	# 88-92
    sprite('jn313_13', 5)	# 93-97
    sprite('jn313_14', 5)	# 98-102

@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckDriveFlash')
        Unknown1084(1)
        Unknown21015('6963655f73686f74000000000000000000000000000000000000000000000000cc10000000000000')
        Unknown21015('6169725f6963655f73686f740000000000000000000000000000000000000000cc10000000000000')
    sprite('jn400_00', 1)	# 1-1
    sprite('jn400_01', 1)	# 2-2
    sprite('jn400_02', 1)	# 3-3
    sprite('jn400_02', 4)	# 4-7
    Unknown7007('626a6e3230305f30000000000000000064000000626a6e3230305f31000000000000000064000000626a6e3230305f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('ice_shot', 0)
    sprite('jn400_03', 3)	# 8-10
    sprite('jn400_04', 3)	# 11-13
    SFX_0('003_swing_grap_0_1')
    sprite('jn400_05', 3)	# 14-16
    sprite('jn400_06', 3)	# 17-19
    sprite('jn400_07', 4)	# 20-23
    sprite('jn400_08', 4)	# 24-27
    sprite('jn400_09', 4)	# 28-31
    sprite('jn400_10', 4)	# 32-35
    sprite('jn400_11', 4)	# 36-39
    sprite('jn400_12', 4)	# 40-43
    Recovery()
    sprite('jn400_13', 3)	# 44-46
    sprite('jn400_14', 2)	# 47-48
    sprite('jn400_15', 2)	# 49-50

@State
def Shot_D1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('CheckDriveFlash')
        Unknown1084(1)
        Unknown21015('6963655f73686f745f65780000000000000000000000000000000000000000006810000000000000')
        Unknown21015('6169725f6963655f73686f745f657800000000000000000000000000000000006810000000000000')
        Unknown21015('6963655f73686f745f65785f41737369737400000000000000000000000000006810000000000000')
    sprite('jn400_00', 3)	# 1-3
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn400_01', 3)	# 4-6
    SFX_3('jnse_22')
    GFX_0('jnef_25percent', -1)
    Unknown7007('626a6e3230315f30000000000000000064000000626a6e3230315f31000000000000000064000000626a6e3230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn400_02', 19)	# 7-25
    Unknown38(7, 1)
    sprite('jn400_03', 4)	# 26-29
    GFX_0('ice_shot_ex', 0)
    sprite('jn400_04', 4)	# 30-33
    SFX_0('003_swing_grap_0_1')
    sprite('jn400_05', 4)	# 34-37
    sprite('jn400_06', 4)	# 38-41
    sprite('jn400_07', 4)	# 42-45
    sprite('jn400_08', 4)	# 46-49
    sprite('jn400_09', 4)	# 50-53
    sprite('jn400_10', 4)	# 54-57
    sprite('jn400_11', 4)	# 58-61
    sprite('jn400_12', 4)	# 62-65
    Recovery()
    sprite('jn400_13', 3)	# 66-68
    sprite('jn400_14', 2)	# 69-70
    sprite('jn400_15', 2)	# 71-72
    Unknown3029(0)

@State
def Shot_D2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(1)
        Unknown21015('6963655f73686f745f65783200000000000000000000000000000000000000000610000000000000')
        Unknown21015('6169725f6963655f73686f745f657832000000000000000000000000000000000610000000000000')
    sprite('jn400_00', 3)	# 1-3
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn400_01', 3)	# 4-6
    SFX_3('jnse_22')
    Unknown7007('626a6e3230325f30000000000000000064000000626a6e3230325f31000000000000000064000000626a6e3230325f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('jn400_02', 9)	# 7-15
    sprite('jn400_03', 3)	# 16-18
    GFX_0('ice_shot_ex2', 0)
    Unknown38(7, 1)
    sprite('jn400_04', 3)	# 19-21
    SFX_0('003_swing_grap_0_1')
    sprite('jn400_05', 3)	# 22-24
    sprite('jn400_06', 3)	# 25-27
    sprite('jn400_07', 3)	# 28-30
    sprite('jn400_08', 3)	# 31-33
    sprite('jn400_09', 3)	# 34-36
    sprite('jn400_10', 3)	# 37-39
    sprite('jn400_11', 3)	# 40-42
    sprite('jn400_12', 3)	# 43-45
    Recovery()
    sprite('jn400_13', 3)	# 46-48
    sprite('jn400_14', 2)	# 49-50
    sprite('jn400_15', 2)	# 51-52
    Unknown3029(0)

@State
def AirShot():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        Unknown22004(12, 1)
        callSubroutine('CheckDriveFlash')
        Unknown1045(0)
        Unknown21015('6963655f73686f74000000000000000000000000000000000000000000000000cc10000000000000')
        Unknown21015('6169725f6963655f73686f740000000000000000000000000000000000000000cc10000000000000')
    sprite('jn402_00', 1)	# 1-1
    physicsXImpulse(-8000)
    Unknown1028(100)
    physicsYImpulse(17000)
    setGravity(700)
    sprite('jn402_00', 2)	# 2-3
    sprite('jn402_01', 3)	# 4-6
    Unknown7007('626a6e3230335f30000000000000000064000000626a6e3230335f31000000000000000064000000626a6e3230335f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('air_ice_shot', 1)
    sprite('jn402_02', 3)	# 7-9
    sprite('jn402_03', 3)	# 10-12
    sprite('jn402_04', 3)	# 13-15
    SFX_0('003_swing_grap_0_1')
    sprite('jn402_05', 2)	# 16-17
    sprite('jn402_06', 15)	# 18-32
    Unknown1043()
    sprite('jn402_07', 6)	# 33-38
    sprite('jn402_08', 6)	# 39-44

@State
def AirShot_D1():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        callSubroutine('CheckDriveFlash')
        Unknown1045(0)
        Unknown21015('6963655f73686f745f65780000000000000000000000000000000000000000006810000000000000')
        Unknown21015('6169725f6963655f73686f745f657800000000000000000000000000000000006810000000000000')
        Unknown21015('6963655f73686f745f65785f41737369737400000000000000000000000000006810000000000000')
    sprite('jn402_00', 4)	# 1-4
    Unknown1019(50)
    YAccel(0)
    setGravity(0)
    sprite('jn402_00', 4)	# 5-8
    GFX_0('jnef_25percent', -1)
    physicsXImpulse(-8000)
    Unknown1028(100)
    physicsYImpulse(27000)
    setGravity(1500)
    Unknown3029(1)
    Unknown3069(0)
    SFX_3('jnse_22')
    sprite('jn402_01', 3)	# 9-11
    Unknown7007('626a6e3230345f30000000000000000064000000626a6e3230345f31000000000000000064000000626a6e3230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn402_02', 3)	# 12-14
    sprite('jn402_03', 3)	# 15-17
    GFX_0('air_ice_shot_ex', 1)
    Unknown38(7, 1)
    sprite('jn402_04', 3)	# 18-20
    SFX_0('003_swing_grap_0_1')
    sprite('jn402_05', 2)	# 21-22
    sprite('jn402_06', 20)	# 23-42
    Unknown1019(70)
    label(0)
    sprite('jn402_07', 4)	# 43-46
    Unknown3029(0)
    sprite('jn402_08', 4)	# 47-50
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    sprite('jn020_10', 4)	# 51-54
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('jn020_11', 4)	# 55-58
    sprite('jn020_12', 4)	# 59-62
    sprite('jn020_13', 4)	# 63-66
    sprite('jn020_14', 4)	# 67-70
    ExitState()

@State
def AirShot_D2():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1045(0)
        Unknown21015('6963655f73686f745f65783200000000000000000000000000000000000000000610000000000000')
        Unknown21015('6169725f6963655f73686f745f657832000000000000000000000000000000000610000000000000')
    sprite('jn402_00', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(-2000)
    physicsYImpulse(2000)
    sprite('jn402_00', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    SFX_3('jnse_22')
    Unknown22004(9, 1)
    sprite('jn402_01', 3)	# 7-9
    Unknown7007('626a6e3230355f30000000000000000064000000626a6e3230355f31000000000000000064000000626a6e3230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn402_02', 3)	# 10-12
    sprite('jn402_03', 3)	# 13-15
    GFX_0('air_ice_shot_ex2', 1)
    Unknown38(7, 1)
    sprite('jn402_04', 3)	# 16-18
    SFX_0('003_swing_grap_0_1')
    sprite('jn402_05', 2)	# 19-20
    sprite('jn402_06', 12)	# 21-32
    physicsXImpulse(-2000)
    physicsYImpulse(12000)
    Unknown1043()
    sprite('jn402_07', 4)	# 33-36
    sprite('jn402_08', 4)	# 37-40

@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        AirUntechableTime(26)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown9016(1)
        Unknown12051(2)
        HitOrBlockCancel('Assault_2nd')
        WhiffCancel('Assault_2nd')
        callSubroutine('CheckDriveFlash')
        sendToLabelUpon(10, 0)
    sprite('jn408_00', 3)	# 1-3
    sprite('jn408_01', 3)	# 4-6
    physicsXImpulse(-3000)
    physicsYImpulse(4000)
    Unknown1043()
    GFX_0('IceBoard', -1)
    Unknown38(4, 1)
    tag_voice(1, 'bjn210_0', 'bjn210_1', 'bjn210_2', '')

    def upon_STATE_END():
        GFX_0('IceBoard_koware', -1)
    sprite('jn408_02', 3)	# 7-9
    sprite('jn408_03', 2)	# 10-11
    sprite('jn408_04', 2)	# 12-13
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)	# 14-16
    SFX_0('000_airdash_0')
    physicsXImpulse(35000)
    Unknown1028(1500)
    Unknown2016(60)
    Unknown2015(150)
    Unknown23029(4, 4001, 0)
    sprite('jn408_06ex', 1)	# 17-17	 **attackbox here**
    sprite('jn408_06ex', 1)	# 18-18	 **attackbox here**
    WhiffCancelEnable(1)
    sprite('jn408_07ex', 2)	# 19-20	 **attackbox here**
    sprite('jn408_06ex', 2)	# 21-22	 **attackbox here**
    sprite('jn408_07ex', 2)	# 23-24	 **attackbox here**
    label(0)
    sprite('jn408_08', 5)	# 25-29
    clearUponHandler(10)
    clearUponHandler(1)
    sendToLabelUpon(2, 100)
    Unknown13(4)
    GFX_0('IceBoard_koware', -1)
    Recovery()
    Unknown2016(-1)
    Unknown2015(-1)
    Unknown1019(10)
    Unknown1034(0)
    physicsYImpulse(10000)
    Unknown1043()
    Unknown14077(0)
    WhiffCancelEnable(0)
    label(9)
    sprite('jn408_09', 3)	# 30-32
    sprite('jn408_10', 3)	# 33-35
    loopRest()
    gotoLabel(9)
    label(100)
    Unknown1084(1)
    sprite('jn020_10', 2)	# 36-37
    sprite('jn020_11', 2)	# 38-39
    sprite('jn020_13', 2)	# 40-41

@State
def Assault_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1600)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        AirUntechableTime(26)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown9016(1)
        HitOrBlockCancel('Assault_2nd')
        WhiffCancel('Assault_2nd')
        callSubroutine('CheckDriveFlash')
        sendToLabelUpon(10, 0)
    sprite('jn408_00', 3)	# 1-3
    sprite('jn408_01', 3)	# 4-6
    physicsXImpulse(-3000)
    physicsYImpulse(4000)
    Unknown1043()
    GFX_0('IceBoard', -1)
    Unknown38(4, 1)
    tag_voice(1, 'bjn210_0', 'bjn210_1', 'bjn210_2', '')

    def upon_STATE_END():
        GFX_0('IceBoard_koware', -1)
    sprite('jn408_02', 3)	# 7-9
    sprite('jn408_03', 2)	# 10-11
    sprite('jn408_04', 2)	# 12-13
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)	# 14-16
    SFX_0('000_airdash_0')
    physicsXImpulse(50000)
    Unknown1028(3000)
    Unknown2016(60)
    Unknown2015(150)
    Unknown23029(4, 4001, 0)
    sprite('jn408_06ex', 1)	# 17-17	 **attackbox here**
    sprite('jn408_06ex', 1)	# 18-18	 **attackbox here**
    WhiffCancelEnable(1)
    sprite('jn408_07ex', 2)	# 19-20	 **attackbox here**
    sprite('jn408_06ex', 2)	# 21-22	 **attackbox here**
    sprite('jn408_07ex', 2)	# 23-24	 **attackbox here**
    sprite('jn408_06ex', 2)	# 25-26	 **attackbox here**
    label(0)
    sprite('jn408_08', 5)	# 27-31
    clearUponHandler(10)
    clearUponHandler(1)
    sendToLabelUpon(2, 100)
    Unknown13(4)
    GFX_0('IceBoard_koware', -1)
    Recovery()
    Unknown2016(-1)
    Unknown2015(-1)
    Unknown1019(10)
    Unknown1034(0)
    physicsYImpulse(14000)
    Unknown1043()
    Unknown14077(0)
    WhiffCancelEnable(0)
    label(9)
    sprite('jn408_09', 3)	# 32-34
    sprite('jn408_10', 3)	# 35-37
    loopRest()
    gotoLabel(9)
    label(100)
    Unknown1084(1)
    sprite('jn020_10', 2)	# 38-39
    sprite('jn020_11', 2)	# 40-41
    sprite('jn020_13', 3)	# 42-44

@State
def Assault_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(30)
        AirPushbackY(-28000)
        YImpluseBeforeWallbounce(1000)
        Unknown9310(1)
        Hitstop(8)
        Unknown11108('03000000')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        if Unknown23145('Assault_B'):
            Damage(1600)
        Unknown30068(1)
        Unknown23087(120000)
        sendToLabelUpon(2, 3)
    sprite('jn408_11', 1)	# 1-1
    physicsXImpulse(20000)
    physicsYImpulse(25000)
    setGravity(2500)
    sprite('jn408_12', 3)	# 2-4
    sprite('jn408_13', 3)	# 5-7
    sprite('jn408_14', 3)	# 8-10
    tag_voice(0, 'bjn211_0', 'bjn211_1', 'bjn211_2', '')
    sprite('jn408_15', 3)	# 11-13
    Unknown1019(80)
    sprite('jn408_16ex01', 2)	# 14-15	 **attackbox here**
    GFX_0('zan408', 0)
    SFX_0('009_swing_rapier_1')
    Unknown1019(80)
    sprite('jn408_17', 2)	# 16-17	 **attackbox here**
    sprite('jn408_18', 2)	# 18-19
    Recovery()
    sprite('jn408_19', 32767)	# 20-32786
    label(3)
    sprite('jn408_20', 3)	# 32787-32789
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown23087(-1)
    sprite('jn408_21', 3)	# 32790-32792
    sprite('jn408_22', 2)	# 32793-32794
    sprite('jn408_23', 2)	# 32795-32796
    sprite('jn408_24', 2)	# 32797-32798
    sprite('jn408_25', 2)	# 32799-32800
    sprite('jn408_26', 2)	# 32801-32802
    GFX_0('EffNoutou', 0)
    sprite('jn408_27', 2)	# 32803-32804
    sprite('jn408_28', 2)	# 32805-32806

@State
def Assault_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        Unknown9154(26)
        AirUntechableTime(25)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown9016(1)
        Unknown9019(1)
        Unknown30065(0)
        Unknown11091(10)
        HitOrBlockCancel('Assault_D_2nd')
        WhiffCancel('Assault_D_2nd')
        sendToLabelUpon(10, 0)
    sprite('jn408_00', 3)	# 1-3
    sprite('jn408_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'bjn210_0', 'bjn210_1', 'bjn210_2', '')
    physicsXImpulse(-5000)
    physicsYImpulse(4000)
    Unknown1043()
    GFX_0('IceBoard', -1)
    Unknown38(4, 1)
    SFX_3('jnse_22')

    def upon_STATE_END():
        GFX_0('IceBoard_koware', -1)
    sprite('jn408_02', 3)	# 7-9
    sprite('jn408_03', 2)	# 10-11
    sprite('jn408_04', 2)	# 12-13
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)	# 14-16
    SFX_0('000_airdash_0')
    physicsXImpulse(50000)
    Unknown1028(3000)
    Unknown2016(60)
    Unknown2015(150)
    Unknown23029(4, 4001, 0)
    sprite('jn408_06ex', 1)	# 17-17	 **attackbox here**
    sprite('jn408_06ex', 1)	# 18-18	 **attackbox here**
    WhiffCancelEnable(1)
    sprite('jn408_07ex', 2)	# 19-20	 **attackbox here**
    sprite('jn408_06ex', 2)	# 21-22	 **attackbox here**
    sprite('jn408_07ex', 2)	# 23-24	 **attackbox here**
    sprite('jn408_06ex', 2)	# 25-26	 **attackbox here**
    sprite('jn408_07ex', 2)	# 27-28	 **attackbox here**
    label(0)
    sprite('jn408_08', 5)	# 29-33
    clearUponHandler(10)
    clearUponHandler(1)
    sendToLabelUpon(2, 100)
    Unknown13(4)
    GFX_0('IceBoard_koware', -1)
    Unknown3029(1)
    Recovery()
    Unknown2016(-1)
    Unknown2015(-1)
    Unknown1019(10)
    Unknown1034(0)
    physicsYImpulse(10000)
    Unknown1043()
    loopRest()
    Unknown14077(0)
    WhiffCancelEnable(0)
    label(9)
    sprite('jn408_09', 3)	# 34-36
    sprite('jn408_10', 3)	# 37-39
    loopRest()
    gotoLabel(9)
    label(100)
    Unknown1084(1)
    sprite('jn020_10', 2)	# 40-41
    sprite('jn020_11', 2)	# 42-43
    sprite('jn020_13', 2)	# 44-45

@State
def Assault_D_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackY(6000)
        AirPushbackX(96000)
        WallbounceReboundTime(5)
        YImpluseBeforeWallbounce(800)
        Unknown9202(15)
        AirUntechableTime(50)
        Unknown11108('03000000')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        Unknown30065(0)
        Unknown11091(10)
        Unknown3029(1)
        Unknown23087(120000)
        sendToLabelUpon(2, 3)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('jn409_00', 1)	# 1-1
    physicsXImpulse(24000)
    sprite('jn409_00', 1)	# 2-2
    sprite('jn409_01', 2)	# 3-4
    physicsYImpulse(15000)
    setGravity(1500)
    sprite('jn409_02', 2)	# 5-6
    tag_voice(0, 'bjn212_0', 'bjn212_1', 'bjn212_2', '')
    sprite('jn409_03', 3)	# 7-9
    sprite('jn409_04', 2)	# 10-11
    sprite('jn409_05', 2)	# 12-13
    sprite('jn409_06ex01', 3)	# 14-16	 **attackbox here**
    GFX_0('zan409', 0)
    SFX_0('009_swing_rapier_0')
    Unknown1019(70)
    sprite('jn409_07', 3)	# 17-19
    Recovery()
    sprite('jn409_08', 3)	# 20-22
    sprite('jn409_09', 32767)	# 23-32789
    label(3)
    sprite('jn409_10', 2)	# 32790-32791
    GFX_0('EffNoutou', 0)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown23087(-1)
    Unknown3029(0)
    sprite('jn409_11', 2)	# 32792-32793
    sprite('jn409_12', 2)	# 32794-32795
    sprite('jn409_13', 2)	# 32796-32797
    sprite('jn409_14', 2)	# 32798-32799
    sprite('jn409_15', 1)	# 32800-32800

@State
def AirAssault():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(24000)
        AirPushbackY(-48000)
        Unknown11058('0100000000000000000000000000000000000000')
        AirUntechableTime(36)
        Unknown9310(1)
        Unknown9016(1)
        callSubroutine('CheckDriveFlash')
    sprite('jn413_00', 2)	# 1-2
    Unknown1019(20)
    Unknown1051(0)
    YAccel(0)
    Unknown1039(-20)
    sprite('jn413_01', 2)	# 3-4
    sprite('jn413_02', 2)	# 5-6
    sprite('jn413_05', 3)	# 7-9
    Unknown7007('626a6e3231355f30000000000000000064000000626a6e3231355f31000000000000000064000000626a6e3231355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn413_06', 3)	# 10-12
    Unknown1084(1)
    physicsXImpulse(-9000)
    physicsYImpulse(20000)
    setGravity(1800)
    SFX_0('009_swing_rapier_2')
    SFX_3('jnse_21')
    GFX_0('EFF413C', -1)
    sprite('jn413_07', 3)	# 13-15	 **attackbox here**
    Unknown22004(8, 1)
    sprite('jn413_08', 3)	# 16-18
    Recovery()
    Unknown1019(50)
    sprite('jn413_09', 3)	# 19-21
    sprite('jn413_10', 6)	# 22-27
    GFX_0('EffNoutou', 0)
    Unknown1019(50)
    sprite('jn413_11', 5)	# 28-32
    Unknown1019(50)
    sprite('jn413_12', 5)	# 33-37
    sprite('jn020_05', 3)	# 38-40
    sprite('jn020_06', 3)	# 41-43
    sprite('jn020_07', 3)	# 44-46
    label(0)
    sprite('jn020_08', 3)	# 47-49
    sprite('jn020_09', 3)	# 50-52
    gotoLabel(0)

@State
def AirAssaultB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(10000)
        AirPushbackX(-3000)
        Unknown11058('0100000000000000000000000000000000000000')
        AirUntechableTime(80)
        Hitstop(6)
        Unknown11046(1)
        Unknown9016(1)
        Unknown9019(1)
    sprite('jn413_00', 4)	# 1-4
    Unknown1019(20)
    Unknown1051(0)
    YAccel(0)
    Unknown1039(-20)
    sprite('jn413_01', 4)	# 5-8
    Unknown7007('626a6e3231365f30000000000000000064000000626a6e3231365f31000000000000000064000000626a6e3231365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn413_02', 4)	# 9-12
    SFX_0('009_swing_rapier_1')
    sprite('jn413_03', 2)	# 13-14	 **attackbox here**
    GFX_0('EFF413D', -1)
    StartMultihit()
    sprite('jn413_03', 1)	# 15-15	 **attackbox here**
    Unknown1084(1)
    sprite('jn413_04', 3)	# 16-18
    sprite('jn413_05', 3)	# 19-21
    sprite('jn413_06', 3)	# 22-24
    Unknown1084(1)
    physicsXImpulse(-9000)
    physicsYImpulse(20000)
    setGravity(1800)
    SFX_0('009_swing_rapier_2')
    SFX_3('jnse_21')
    GFX_0('EFF413C', -1)
    sprite('jn413_07', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1800)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(24000)
    AirPushbackY(-48000)
    AirUntechableTime(42)
    Unknown9310(1)
    Unknown11058('0100000000000000000000000000000000000000')
    AirUntechableTime(36)
    PushbackX(19800)
    Unknown9251()
    HitOverhead(2)
    Hitstop(12)
    Unknown11046(0)
    Unknown22004(8, 1)
    sprite('jn413_08', 3)	# 28-30
    Recovery()
    Unknown1019(50)
    sprite('jn413_09', 3)	# 31-33
    sprite('jn413_10', 6)	# 34-39
    GFX_0('EffNoutou', 0)
    Unknown1019(50)
    sprite('jn413_11', 5)	# 40-44
    Unknown1019(50)
    sprite('jn413_12', 5)	# 45-49
    sprite('jn020_05', 3)	# 50-52
    sprite('jn020_06', 3)	# 53-55
    sprite('jn020_07', 3)	# 56-58
    label(0)
    sprite('jn020_08', 3)	# 59-61
    sprite('jn020_09', 3)	# 62-64
    gotoLabel(0)

@State
def AirAssault_D():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(10000)
        AirPushbackX(-3000)
        Unknown11058('0100000000000000000000000000000000000000')
        AirUntechableTime(80)
        Hitstop(6)
        Unknown11046(1)
        Unknown9016(1)
        Unknown9019(1)
        Unknown30065(0)
        Unknown11091(10)
    sprite('jn413_00', 2)	# 1-2
    Unknown1019(20)
    Unknown1051(0)
    YAccel(0)
    Unknown1039(-20)
    sprite('jn413_01', 1)	# 3-3
    sprite('jn413_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    SFX_3('jnse_22')
    Unknown7007('626a6e3231365f30000000000000000064000000626a6e3231365f31000000000000000064000000626a6e3231365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn413_02', 2)	# 5-6
    SFX_0('009_swing_rapier_1')
    sprite('jn413_03', 2)	# 7-8	 **attackbox here**
    GFX_0('EFF413D', -1)
    StartMultihit()
    sprite('jn413_03', 1)	# 9-9	 **attackbox here**
    Unknown1084(1)
    sprite('jn413_04', 2)	# 10-11
    sprite('jn413_05', 2)	# 12-13
    sprite('jn413_06', 3)	# 14-16
    Unknown1084(1)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    setGravity(2000)
    SFX_0('009_swing_rapier_2')
    SFX_3('jnse_21')
    GFX_0('EFF413C', -1)
    sprite('jn413_07', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(24000)
    AirPushbackY(-48000)
    AirUntechableTime(42)
    Unknown9310(14)
    Unknown9251()
    Unknown9287()
    HitOverhead(2)
    Hitstop(12)
    Unknown11046(0)
    Unknown22004(6, 1)
    sprite('jn413_08', 3)	# 20-22
    Unknown1019(80)
    Recovery()
    sprite('jn413_09', 3)	# 23-25
    sprite('jn413_10', 6)	# 26-31
    Unknown1019(80)
    GFX_0('EffNoutou', 0)
    sprite('jn413_11', 5)	# 32-36
    Unknown1019(80)
    sprite('jn413_12', 5)	# 37-41

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2300)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(37000)
        AirUntechableTime(55)
        Unknown9016(1)
        Unknown2004(1, 0)
        callSubroutine('CheckDriveFlash')
    sprite('jn406_00', 2)	# 1-2
    sprite('jn406_01', 2)	# 3-4
    sprite('jn406_02', 2)	# 5-6
    sprite('jn406_03', 2)	# 7-8
    Unknown18009(1)
    sprite('jn406_04', 2)	# 9-10
    sprite('jn406_05', 1)	# 11-11
    sprite('jn406_06', 1)	# 12-12
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a6e3230375f30000000000000000064000000626a6e3230375f31000000000000000064000000626a6e3230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jn406_07', 3)	# 13-15	 **attackbox here**
    SFX_3('jnse_21')
    GFX_0('EFF28AtkC', 0)
    sprite('jn406_08', 3)	# 16-18
    setInvincible(0)
    sprite('jn406_09', 3)	# 19-21
    sprite('jn406_10', 3)	# 22-24
    sprite('jn406_11', 3)	# 25-27
    sprite('jn406_12', 3)	# 28-30
    sprite('jn406_13', 4)	# 31-34
    sprite('jn406_14', 4)	# 35-38
    sprite('jn406_15', 4)	# 39-42
    sprite('jn406_16', 4)	# 43-46
    sprite('jn406_17', 4)	# 47-50
    GFX_0('EffNoutou', 1)
    sprite('jn406_18', 4)	# 51-54
    sprite('jn406_19', 4)	# 55-58
    sprite('jn406_20', 3)	# 59-61
    sprite('jn406_21', 3)	# 62-64
    Unknown18009(0)

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Unknown2003(1)
        setInvincible(1)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('jn430_00', 1)	# 1-1
    Unknown2036(30, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown7006('bjn250_0', 100, 846096994, 828321845, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    sprite('jn430_00', 1)	# 2-2
    sprite('jn430_01', 2)	# 3-4
    sprite('jn430_02', 2)	# 5-6
    sprite('jn430_03', 2)	# 7-8
    sprite('jn430_04', 2)	# 9-10
    sprite('jn430_05', 2)	# 11-12
    sprite('jn430_06', 2)	# 13-14
    sprite('jn430_07', 3)	# 15-17
    sprite('jn430_08', 3)	# 18-20
    sprite('jn430_09', 3)	# 21-23
    Unknown12046(50)
    sprite('jn430_10', 3)	# 24-26
    SFX_0('009_swing_rapier_1')
    sprite('jn430_11', 3)	# 27-29
    sprite('jn430_12', 3)	# 30-32
    sprite('jn430_13', 3)	# 33-35
    sprite('jn430_14', 3)	# 36-38
    SFX_0('006_swing_blade_1')
    sprite('jn430_15', 3)	# 39-41
    Unknown12046(100)
    setInvincible(0)
    GFX_0('UltimateSlashShotObj', 0)
    SFX_0('000_airdash_0')
    sprite('jn430_16', 3)	# 42-44
    sprite('jn430_17', 3)	# 45-47
    Unknown12046(50)
    sprite('jn430_18', 3)	# 48-50
    sprite('jn430_19', 3)	# 51-53
    Unknown12046(0)
    sprite('jn430_20', 3)	# 54-56
    sprite('jn430_21', 3)	# 57-59
    sprite('jn430_22', 3)	# 60-62
    sprite('jn430_23', 3)	# 63-65
    GFX_0('EffNoutou', 0)
    sprite('jn430_24', 3)	# 66-68
    sprite('jn430_25', 3)	# 69-71
    sprite('jn430_26', 3)	# 72-74

@State
def UltimateShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 5101):
                Unknown2037(1)
            if (SLOT_48 == 5102):
                Unknown2064(1)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('jn430_00', 1)	# 1-1
    Unknown2036(30, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown7006('bjn250_0', 100, 846096994, 828321845, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    sprite('jn430_00', 1)	# 2-2
    sprite('jn430_01', 2)	# 3-4
    sprite('jn430_02', 2)	# 5-6
    sprite('jn430_03', 2)	# 7-8
    sprite('jn430_04', 2)	# 9-10
    sprite('jn430_05', 2)	# 11-12
    sprite('jn430_06', 2)	# 13-14
    sprite('jn430_07', 3)	# 15-17
    sprite('jn430_08', 3)	# 18-20
    sprite('jn430_09', 3)	# 21-23
    Unknown12046(50)
    sprite('jn430_10', 3)	# 24-26
    SFX_0('009_swing_rapier_1')
    sprite('jn430_11', 3)	# 27-29
    sprite('jn430_12', 3)	# 30-32
    sprite('jn430_13', 3)	# 33-35
    sprite('jn430_14', 3)	# 36-38
    SFX_0('006_swing_blade_1')
    sprite('jn430_15', 3)	# 39-41
    Unknown12046(100)
    setInvincible(0)
    GFX_0('OverDriveSlashShotObj', 0)
    SFX_0('000_airdash_0')
    sprite('jn430_16', 3)	# 42-44
    sprite('jn430_17', 3)	# 45-47
    Unknown12046(50)
    sprite('jn430_18', 3)	# 48-50
    sprite('jn430_19', 3)	# 51-53
    Unknown12046(0)
    sprite('jn430_20', 3)	# 54-56
    sprite('jn430_21', 3)	# 57-59
    if SLOT_2:
        enterState('UltimateShotAddAttack')
    clearUponHandler(43)
    sprite('jn430_22', 3)	# 60-62
    sprite('jn430_23', 3)	# 63-65
    GFX_0('EffNoutou', 0)
    sprite('jn430_24', 3)	# 66-68
    sprite('jn430_25', 3)	# 69-71
    sprite('jn430_26', 3)	# 72-74

@State
def UltimateShotAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2004(1, 0)
        setInvincible(1)
        Unknown23027()
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 5108):
                Unknown2038(1)
    sprite('jn330_03', 4)	# 1-4
    SFX_0('008_swing_pole_0')
    sprite('jn330_04', 4)	# 5-8
    SFX_0('008_swing_pole_0')
    sprite('jn330_05', 3)	# 9-11
    tag_voice(1, 'bjn251_0', 'bjn251_1', 'bjn251_2', '')
    sprite('jn330_06', 12)	# 12-23
    sprite('jn330_06', 12)	# 24-35
    Unknown23024(2)
    sprite('jn330_07', 3)	# 36-38
    SFX_0('019_cloth_c')
    SFX_0('019_cloth_a')
    sprite('jn330_08', 5)	# 39-43	 **attackbox here**
    GFX_1('jnef_ast_attack', 0)
    GFX_0('AstralStartPtc', -1)
    SFX_3('jnse_22')
    GFX_0('UltimateShotOverDrive', -1)
    Unknown23029(1, 5104, 0)
    sprite('jn330_09', 5)	# 44-48
    sprite('jn330_10', 5)	# 49-53
    sprite('jn330_11', 5)	# 54-58
    GFX_0('UltimateShotOverDrive', -1)
    Unknown23029(1, 5105, 0)
    sprite('jn330_11', 15)	# 59-73
    sprite('jn330_11', 10)	# 74-83
    GFX_0('UltimateShotOverDrive', -1)
    Unknown23029(1, 5106, 0)
    sprite('jn330_11', 20)	# 84-103
    sprite('jn330_12', 5)	# 104-108
    sprite('jn330_13', 5)	# 109-113
    sprite('jn330_14', 5)	# 114-118
    sprite('jn330_15', 4)	# 119-122	 **attackbox here**
    SFX_0('008_swing_pole_0')
    sprite('jn330_16', 4)	# 123-126	 **attackbox here**
    SFX_0('008_swing_pole_0')
    sprite('jn330_17', 4)	# 127-130	 **attackbox here**
    SFX_0('008_swing_pole_0')
    sprite('jn330_18', 4)	# 131-134	 **attackbox here**
    SFX_0('008_swing_pole_0')
    sprite('jn330_19', 4)	# 135-138
    sprite('jn330_20', 4)	# 139-142
    sprite('jn330_21', 4)	# 143-146
    GFX_0('EffNoutou', 0)
    sprite('jn330_22', 4)	# 147-150
    if SLOT_2:
        GFX_0('OverDriveSlashShotFinish', -1)
        ScreenShake(40000, 40000)
        Unknown21015('556c74696d61746553686f744f76657244726976650000000000000000000000f313000000000000')
    sprite('jn330_23', 4)	# 151-154
    Unknown13024(1)
    sprite('jn330_24', 55)	# 155-209
    sprite('jn330_25', 8)	# 210-217
    sprite('jn330_26', 8)	# 218-225

@State
def UltimateAntiAirShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Unknown2003(1)
        setInvincible(1)
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 5003):
                clearUponHandler(43)
                SLOT_51 = 1
                setInvincible(1)
                Unknown2037(1)
            if (SLOT_48 == 5005):
                clearUponHandler(43)
                Unknown13024(1)
        callSubroutine('CheckDriveFlash')

        def upon_STATE_END():
            Unknown12046(0)
    sprite('jn431_00', 2)	# 1-2
    sprite('jn431_01', 2)	# 3-4
    sprite('jn431_02', 2)	# 5-6
    Unknown2036(45, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown7006('bjn252_0', 100, 846096994, 828322357, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown12046(50)
    sprite('jn431_03', 2)	# 7-8
    sprite('jn431_04', 2)	# 9-10
    sprite('jn431_05', 2)	# 11-12
    sprite('jn431_06', 2)	# 13-14
    sprite('jn431_07', 3)	# 15-17
    sprite('jn431_08', 3)	# 18-20
    Unknown12046(100)
    sprite('jn431_09', 3)	# 21-23
    GFX_0('IceBow', 0)
    GFX_0('IceArrow', 1)
    Unknown23029(1, 5001, 0)
    SFX_0('018_ice_break_0')
    SFX_0('008_swing_pole_0')
    sprite('jn431_10', 3)	# 24-26
    sprite('jn431_11', 3)	# 27-29
    sprite('jn431_12', 3)	# 30-32
    sprite('jn431_09', 3)	# 33-35
    sprite('jn431_10', 3)	# 36-38
    sprite('jn431_11', 3)	# 39-41
    sprite('jn431_12', 3)	# 42-44
    sprite('jn431_09', 3)	# 45-47
    sprite('jn431_10', 3)	# 48-50
    sprite('jn431_11', 3)	# 51-53
    sprite('jn431_12', 3)	# 54-56
    sprite('jn431_13', 1)	# 57-57
    if SLOT_2:
        setInvincible(1)
    else:
        setInvincible(0)
    GFX_0('IceCircleA', 2)
    sprite('jn431_13', 1)	# 58-58
    GFX_0('IceCircleB', 3)
    sprite('jn431_13', 1)	# 59-59
    GFX_0('IceCircleC', 3)
    sprite('jn431_14', 3)	# 60-62
    SFX_0('009_swing_rapier_2')
    sprite('jn431_15', 3)	# 63-65
    sprite('jn431_16', 3)	# 66-68
    sprite('jn431_13', 3)	# 69-71
    sprite('jn431_14', 3)	# 72-74
    sprite('jn431_15', 3)	# 75-77
    sprite('jn431_16', 3)	# 78-80
    sprite('jn431_13', 3)	# 81-83
    Unknown1084(1)
    sprite('jn431_14', 3)	# 84-86
    sprite('jn431_15', 3)	# 87-89
    sprite('jn431_16', 3)	# 90-92
    if (not SLOT_51):
        sendToLabel(1)
    sprite('jn431_13', 3)	# 93-95

    def upon_43():
        if (SLOT_48 == 5004):
            Unknown13024(1)
            setInvincible(0)
    sprite('jn431_14', 3)	# 96-98
    sprite('jn431_15', 3)	# 99-101
    sprite('jn431_16', 3)	# 102-104
    sprite('jn431_13', 3)	# 105-107
    sprite('jn431_14', 3)	# 108-110
    sprite('jn431_15', 3)	# 111-113
    sprite('jn431_16', 3)	# 114-116
    sprite('jn431_13', 3)	# 117-119
    sprite('jn431_14', 3)	# 120-122
    sprite('jn431_15', 3)	# 123-125
    sprite('jn431_16', 3)	# 126-128
    label(1)
    sprite('jn431_17', 3)	# 129-131
    Unknown13024(1)
    sprite('jn431_18', 3)	# 132-134
    sprite('jn431_19', 3)	# 135-137
    sprite('jn431_20', 3)	# 138-140
    Unknown12046(50)
    sprite('jn431_21', 3)	# 141-143
    Unknown12046(0)
    sprite('jn431_22', 3)	# 144-146

@State
def UltimateAntiAirShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Unknown2003(1)
        setInvincible(1)
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 5003):
                clearUponHandler(43)
                SLOT_51 = 1
                setInvincible(1)
                Unknown2037(1)
            if (SLOT_48 == 5005):
                clearUponHandler(43)
                Unknown13024(1)
        callSubroutine('CheckDriveFlash')

        def upon_STATE_END():
            Unknown12046(0)
    sprite('jn431_00', 2)	# 1-2
    sprite('jn431_01', 2)	# 3-4
    sprite('jn431_02', 2)	# 5-6
    Unknown2036(45, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown7006('bjn252_0', 100, 846096994, 828322357, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown12046(50)
    sprite('jn431_03', 2)	# 7-8
    sprite('jn431_04', 2)	# 9-10
    sprite('jn431_05', 2)	# 11-12
    sprite('jn431_06', 2)	# 13-14
    sprite('jn431_07', 3)	# 15-17
    sprite('jn431_08', 3)	# 18-20
    Unknown12046(100)
    sprite('jn431_09', 3)	# 21-23
    GFX_0('IceBow', 0)
    GFX_0('IceArrow_OD', 1)
    Unknown23029(1, 5001, 0)
    SFX_0('018_ice_break_0')
    SFX_0('008_swing_pole_0')
    SFX_3('jnse_22')
    sprite('jn431_10', 3)	# 24-26
    sprite('jn431_11', 3)	# 27-29
    sprite('jn431_12', 3)	# 30-32
    sprite('jn431_09', 3)	# 33-35
    sprite('jn431_10', 3)	# 36-38
    sprite('jn431_11', 3)	# 39-41
    sprite('jn431_12', 3)	# 42-44
    sprite('jn431_09', 3)	# 45-47
    sprite('jn431_10', 3)	# 48-50
    sprite('jn431_11', 3)	# 51-53
    sprite('jn431_12', 3)	# 54-56
    sprite('jn431_13', 1)	# 57-57
    if SLOT_2:
        setInvincible(1)
    else:
        setInvincible(0)
    GFX_0('IceCircleA', 2)
    sprite('jn431_13', 1)	# 58-58
    GFX_0('IceCircleB', 3)
    sprite('jn431_13', 1)	# 59-59
    GFX_0('IceCircleC', 3)
    sprite('jn431_14', 3)	# 60-62
    SFX_0('009_swing_rapier_2')
    sprite('jn431_15', 3)	# 63-65
    sprite('jn431_16', 3)	# 66-68
    sprite('jn431_13', 3)	# 69-71
    sprite('jn431_14', 3)	# 72-74
    sprite('jn431_15', 3)	# 75-77
    sprite('jn431_16', 3)	# 78-80
    loopRest()
    if (not SLOT_51):
        sendToLabel(1)
    sprite('jn431_13', 3)	# 81-83

    def upon_43():
        if (SLOT_48 == 5004):
            Unknown13024(1)
            setInvincible(0)
    sprite('jn431_14', 3)	# 84-86
    sprite('jn431_15', 3)	# 87-89
    sprite('jn431_16', 3)	# 90-92
    sprite('jn431_13', 3)	# 93-95
    sprite('jn431_14', 3)	# 96-98
    sprite('jn431_15', 3)	# 99-101
    sprite('jn431_16', 3)	# 102-104
    sprite('jn431_13', 3)	# 105-107
    sprite('jn431_14', 3)	# 108-110
    sprite('jn431_15', 3)	# 111-113
    sprite('jn431_16', 3)	# 114-116
    sprite('jn431_13', 3)	# 117-119
    sprite('jn431_14', 3)	# 120-122
    sprite('jn431_15', 3)	# 123-125
    sprite('jn431_16', 3)	# 126-128
    sprite('jn431_13', 3)	# 129-131
    sprite('jn431_14', 3)	# 132-134
    sprite('jn431_15', 3)	# 135-137
    sprite('jn431_16', 3)	# 138-140
    label(1)
    sprite('jn431_17', 3)	# 141-143
    Unknown13024(1)
    sprite('jn431_18', 3)	# 144-146
    sprite('jn431_19', 3)	# 147-149
    sprite('jn431_20', 3)	# 150-152
    Unknown12046(50)
    sprite('jn431_21', 3)	# 153-155
    Unknown12046(0)
    sprite('jn431_22', 3)	# 156-158

@State
def UltimateAirShot():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        setInvincible(1)
        Unknown1084(1)
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 5003):
                clearUponHandler(43)
                Unknown1019(80)
                Unknown1039(50)
            if (SLOT_48 == 5005):
                clearUponHandler(43)
                Unknown13024(1)
        callSubroutine('CheckDriveFlash')
    sprite('jn253_00', 2)	# 1-2
    sprite('jn253_01', 2)	# 3-4
    sprite('jn253_01', 3)	# 5-7
    Unknown2036(32, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown7006('bjn252_0', 100, 846096994, 828322357, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('jn253_02', 18)	# 8-25
    GFX_0('IceBow', 0)
    Unknown23029(1, 5002, 0)
    GFX_0('IceArrow', 1)
    Unknown23029(1, 5002, 0)
    sprite('jn253_03', 3)	# 26-28
    sprite('jn402_00', 1)	# 29-29
    sprite('jn402_00', 2)	# 30-31
    sprite('jn402_01', 3)	# 32-34
    sprite('jn402_02', 3)	# 35-37
    Unknown1045(0)
    physicsXImpulse(-10000)
    physicsYImpulse(36000)
    Unknown1043()

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(10)
    sprite('jn402_03', 3)	# 38-40
    sprite('jn402_04', 3)	# 41-43
    SFX_0('003_swing_grap_0_1')
    sprite('jn402_05', 2)	# 44-45
    sprite('jn402_06', 16)	# 46-61
    setInvincible(0)
    GFX_0('IceCircleA', -1)
    Unknown23029(1, 5002, 0)
    GFX_0('IceCircleB', -1)
    Unknown23029(1, 5002, 0)
    GFX_0('IceCircleC', -1)
    Unknown23029(1, 5002, 0)
    sprite('jn402_07', 4)	# 62-65

    def upon_43():
        if (SLOT_48 == 5004):
            clearUponHandler(43)
            Unknown13024(1)
    sprite('jn402_08', 4)	# 66-69
    sprite('jn020_05', 3)	# 70-72
    sprite('jn020_06', 3)	# 73-75
    sprite('jn020_07', 3)	# 76-78
    label(0)
    sprite('jn020_08', 3)	# 79-81
    sprite('jn020_09', 3)	# 82-84
    gotoLabel(0)
    label(10)
    sprite('jn020_10', 3)	# 85-87
    clearUponHandler(2)
    Unknown1084(1)
    sprite('jn020_11', 3)	# 88-90
    sprite('jn020_12', 3)	# 91-93
    sprite('jn020_13', 3)	# 94-96
    sprite('jn020_14', 4)	# 97-100

@State
def UltimateAirShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        setInvincible(1)
        callSubroutine('CheckDriveFlash')
        setGravity(0)
        Unknown1084(1)
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 5003):
                clearUponHandler(43)
                Unknown1019(80)
                Unknown1039(50)
            if (SLOT_48 == 5005):
                clearUponHandler(43)
                Unknown13024(1)
    sprite('jn253_00', 2)	# 1-2
    sprite('jn253_01', 2)	# 3-4
    sprite('jn253_01', 3)	# 5-7
    Unknown2036(32, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown7006('bjn252_0', 100, 846096994, 828322357, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('jn253_02', 18)	# 8-25
    GFX_0('IceBow', 0)
    Unknown23029(1, 5002, 0)
    GFX_0('IceArrow_OD', 1)
    Unknown23029(1, 5002, 0)
    sprite('jn253_03', 3)	# 26-28
    sprite('jn402_00', 1)	# 29-29
    sprite('jn402_00', 2)	# 30-31
    sprite('jn402_01', 3)	# 32-34
    sprite('jn402_02', 3)	# 35-37
    Unknown1045(0)
    physicsXImpulse(-10000)
    physicsYImpulse(36000)
    Unknown1043()

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(10)
    sprite('jn402_03', 3)	# 38-40
    sprite('jn402_04', 3)	# 41-43
    SFX_0('003_swing_grap_0_1')
    SFX_3('jnse_22')
    sprite('jn402_05', 2)	# 44-45
    sprite('jn402_06', 16)	# 46-61
    setInvincible(0)
    GFX_0('IceCircleA', -1)
    Unknown23029(1, 5002, 0)
    GFX_0('IceCircleB', -1)
    Unknown23029(1, 5002, 0)
    GFX_0('IceCircleC', -1)
    Unknown23029(1, 5002, 0)
    sprite('jn402_07', 4)	# 62-65

    def upon_43():
        if (SLOT_48 == 5004):
            Unknown13024(1)
    sprite('jn402_08', 4)	# 66-69
    sprite('jn020_05', 3)	# 70-72
    sprite('jn020_06', 3)	# 73-75
    sprite('jn020_07', 3)	# 76-78
    label(0)
    sprite('jn020_08', 3)	# 79-81
    sprite('jn020_09', 3)	# 82-84
    gotoLabel(0)
    label(10)
    sprite('jn020_10', 2)	# 85-86
    clearUponHandler(2)
    Unknown1084(1)
    sprite('jn020_11', 2)	# 87-88
    sprite('jn020_12', 2)	# 89-90
    sprite('jn020_13', 2)	# 91-92
    sprite('jn020_14', 3)	# 93-95

@State
def UltimateAtemi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)
        Unknown9016(1)
        AttackLevel_(4)
        Damage(500)
        AirPushbackX(0)
        AirPushbackY(-10000)
        AirUntechableTime(80)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11058('0000000001000000000000000000000000000000')
        AirUntechableTime(180)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        Unknown11084(1)
        AttackP2(100)
        Unknown11066(1)
        Unknown12051(2)
        Unknown2018(0, 80)

        def upon_12():
            Unknown23027()
            Unknown2037(1)

        def upon_42():
            clearUponHandler(42)
            Unknown23022(1)
            sendToLabel(111)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0100000001000000010000000100000000000000')
        Unknown22030(0)
        Unknown22026(1)
        Unknown22031(5, 73)
    sprite('jn432_00', 1)	# 1-1
    Unknown2036(36, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_JN', -1)
    SFX_1('jn253')
    GFX_0('jn_DD_2_ex', -1)
    Unknown2058(-10000)
    sprite('jn432_01', 40)	# 2-41
    sprite('jn432_02', 9)	# 42-50
    sprite('jn432_03', 4)	# 51-54
    setInvincible(0)
    sprite('jn432_04', 4)	# 55-58
    sprite('jn432_05', 4)	# 59-62
    sprite('jn432_06', 4)	# 63-66
    sprite('jn432_07', 4)	# 67-70
    loopRest()
    ExitState()
    label(111)
    sprite('jn433_00', 4)	# 71-74
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_01', 4)	# 75-78
    sprite('jn433_02', 4)	# 79-82
    sprite('jn433_03', 4)	# 83-86
    sprite('jn433_04', 4)	# 87-90
    sprite('jn433_05', 4)	# 91-94
    sprite('jn433_06', 4)	# 95-98
    sprite('jn433_07', 4)	# 99-102
    sprite('jn433_08', 4)	# 103-106
    sprite('jn433_09', 4)	# 107-110
    sprite('jn433_10', 4)	# 111-114
    sprite('jn433_11', 4)	# 115-118
    sprite('jn433_12', 4)	# 119-122
    sprite('jn433_13', 4)	# 123-126
    sprite('jn433_14', 3)	# 127-129	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_DD', 0)
    ScreenShake(0, 16000)
    teleportRelativeX(1696000)
    sprite('jn433_15', 3)	# 130-132	 **attackbox here**
    sprite('jn433_16', 3)	# 133-135	 **attackbox here**
    sprite('jn433_15', 3)	# 136-138	 **attackbox here**
    sprite('jn433_16', 3)	# 139-141	 **attackbox here**
    loopRest()
    if SLOT_2:
        _gotolabel(444)
    sprite('jn433_17', 4)	# 142-145
    sprite('jn433_18', 4)	# 146-149
    sprite('jn433_19', 4)	# 150-153
    sprite('jn433_20', 4)	# 154-157
    sprite('jn433_21', 4)	# 158-161
    sprite('jn433_22', 4)	# 162-165
    sprite('jn433_23', 4)	# 166-169
    sprite('jn433_24', 4)	# 170-173
    sprite('jn433_25', 4)	# 174-177
    sprite('jn433_26', 4)	# 178-181
    sprite('jn433_27', 4)	# 182-185
    sprite('jn433_28', 4)	# 186-189
    sprite('jn433_30', 4)	# 190-193
    sprite('jn433_31', 4)	# 194-197
    sprite('jn433_32', 4)	# 198-201
    sprite('jn433_33', 4)	# 202-205
    sprite('jn433_34', 4)	# 206-209
    sprite('jn433_35', 4)	# 210-213
    sprite('jn433_36', 4)	# 214-217
    sprite('jn000_00', 1)	# 218-218
    Unknown2005()
    loopRest()
    ExitState()
    label(444)
    sprite('jn433_17', 4)	# 219-222
    sprite('jn433_18', 4)	# 223-226
    sprite('jn433_19', 4)	# 227-230
    sprite('jn433_20', 4)	# 231-234
    SFX_1('jn254')
    sprite('jn433_21', 4)	# 235-238
    sprite('jn433_22', 4)	# 239-242
    sprite('jn433_23', 4)	# 243-246
    sprite('jn433_24', 4)	# 247-250
    sprite('jn433_25', 4)	# 251-254
    sprite('jn433_26', 4)	# 255-258
    sprite('jn433_27', 30)	# 259-288
    sprite('jn433_28', 40)	# 289-328
    GFX_0('EffNoutou', 0)
    sprite('jn433_29', 5)	# 329-333
    ScreenShake(26000, 0)
    GFX_0('Yukikazedmy', -1)
    sprite('jn433_30', 5)	# 334-338
    sprite('jn433_31', 5)	# 339-343
    sprite('jn433_32', 5)	# 344-348
    sprite('jn433_33', 5)	# 349-353
    sprite('jn433_28', 34)	# 354-387
    sprite('jn433_34', 5)	# 388-392
    sprite('jn433_35', 5)	# 393-397
    sprite('jn433_36', 5)	# 398-402
    sprite('jn000_00', 1)	# 403-403
    Unknown2005()
    loopRest()
    ExitState()

@State
def UltimateAtemi_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)
        Unknown9016(1)
        AttackLevel_(4)
        Damage(500)
        AirPushbackX(0)
        AirPushbackY(-10000)
        AirUntechableTime(80)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11058('0000000001000000000000000000000000000000')
        AirUntechableTime(180)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        Unknown11084(1)
        AttackP2(100)
        Unknown11066(1)
        Hitstop(1)
        Unknown12051(2)
        Unknown2018(0, 80)

        def upon_12():
            Unknown2001()
            Unknown2037(1)

        def upon_42():
            clearUponHandler(42)
            Unknown23022(1)
            sendToLabel(111)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0100000001000000010000000100000000000000')
        Unknown22030(0)
        Unknown22026(1)
        Unknown22031(5, 73)
    sprite('jn432_00', 1)	# 1-1
    Unknown2036(36, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_JN', -1)
    SFX_1('jn253')
    GFX_0('jn_DD_2_ex', -1)
    Unknown2058(-10000)
    sprite('jn432_01', 40)	# 2-41
    sprite('jn432_02', 9)	# 42-50
    sprite('jn432_03', 4)	# 51-54
    setInvincible(0)
    sprite('jn432_04', 4)	# 55-58
    sprite('jn432_05', 4)	# 59-62
    sprite('jn432_06', 4)	# 63-66
    sprite('jn432_07', 4)	# 67-70
    loopRest()
    ExitState()
    label(111)
    sprite('jn433_00', 4)	# 71-74
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_01', 4)	# 75-78
    sprite('jn433_02', 4)	# 79-82
    sprite('jn433_03', 4)	# 83-86
    sprite('jn433_04', 4)	# 87-90
    sprite('jn433_05', 4)	# 91-94
    sprite('jn433_06', 4)	# 95-98
    sprite('jn433_07', 4)	# 99-102
    sprite('jn433_08', 4)	# 103-106
    sprite('jn433_09', 4)	# 107-110
    sprite('jn433_10', 4)	# 111-114
    sprite('jn433_11', 4)	# 115-118
    sprite('jn433_12', 4)	# 119-122
    sprite('jn433_13', 4)	# 123-126
    sprite('jn433_14', 3)	# 127-129	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_DD', 0)
    ScreenShake(0, 16000)
    teleportRelativeX(1696000)
    sprite('jn433_15', 3)	# 130-132	 **attackbox here**
    RefreshMultihit()
    sprite('jn433_16', 3)	# 133-135	 **attackbox here**
    RefreshMultihit()
    sprite('jn433_15', 3)	# 136-138	 **attackbox here**
    RefreshMultihit()
    sprite('jn433_16', 3)	# 139-141	 **attackbox here**
    RefreshMultihit()
    loopRest()
    if SLOT_2:
        enterState('UltimateAtemiAddAttack')
    sprite('jn433_17', 4)	# 142-145
    sprite('jn433_18', 4)	# 146-149
    sprite('jn433_19', 4)	# 150-153
    sprite('jn433_20', 4)	# 154-157
    sprite('jn433_21', 4)	# 158-161
    sprite('jn433_22', 4)	# 162-165
    sprite('jn433_23', 4)	# 166-169
    sprite('jn433_24', 4)	# 170-173
    sprite('jn433_25', 4)	# 174-177
    sprite('jn433_26', 4)	# 178-181
    sprite('jn433_27', 4)	# 182-185
    sprite('jn433_28', 4)	# 186-189
    sprite('jn433_30', 4)	# 190-193
    sprite('jn433_31', 4)	# 194-197
    sprite('jn433_32', 4)	# 198-201
    sprite('jn433_33', 4)	# 202-205
    sprite('jn433_34', 4)	# 206-209
    sprite('jn433_35', 4)	# 210-213
    sprite('jn433_36', 4)	# 214-217
    sprite('jn000_00', 1)	# 218-218
    Unknown2005()

@State
def UltimateAtemiAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(0)
        Unknown11064(1)
        Hitstop(1)
        AttackLevel_(4)
        Damage(500)
        AirPushbackY(-10000)
        AirUntechableTime(100)
        Unknown9016(1)
        Unknown11108('03000000')
        setInvincible(1)
        Unknown23024(2)
        Unknown30068(1)
    sprite('jn433_01', 4)	# 1-4
    Unknown2006()
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('jn433_02', 4)	# 5-8
    sprite('jn433_03', 4)	# 9-12
    sprite('jn433_04', 4)	# 13-16
    sprite('jn433_05', 4)	# 17-20
    sprite('jn433_07', 1)	# 21-21
    sprite('jn433_09', 1)	# 22-22
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_14', 3)	# 23-25	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(500000)
    teleportRelativeY(0)
    Unknown2015(20)
    GFX_0('AstralStartPtc', -1)
    sprite('jn433_15', 3)	# 26-28	 **attackbox here**
    Unknown2015(-1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn433_16', 3)	# 29-31	 **attackbox here**
    loopRest()
    sprite('jn433_01', 1)	# 32-32
    Unknown2006()
    sprite('jn433_02', 1)	# 33-33
    sprite('jn433_03', 1)	# 34-34
    sprite('jn433_04', 1)	# 35-35
    sprite('jn433_05', 1)	# 36-36
    sprite('jn433_07', 1)	# 37-37
    sprite('jn433_09', 1)	# 38-38
    sprite('jn433_14', 2)	# 39-40	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(400000)
    teleportRelativeY(0)
    Unknown2015(20)
    sprite('jn433_15', 1)	# 41-41	 **attackbox here**
    Unknown2015(-1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn433_16', 1)	# 42-42	 **attackbox here**
    loopRest()
    sprite('jn433_01', 1)	# 43-43
    Unknown2006()
    sprite('jn433_02', 1)	# 44-44
    sprite('jn433_03', 1)	# 45-45
    sprite('jn433_04', 1)	# 46-46
    sprite('jn433_05', 1)	# 47-47
    sprite('jn433_07', 1)	# 48-48
    sprite('jn433_09', 1)	# 49-49
    sprite('jn433_14', 1)	# 50-50	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(300000)
    teleportRelativeY(0)
    Unknown2015(20)
    sprite('jn433_15', 1)	# 51-51	 **attackbox here**
    Unknown2015(-1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn433_16', 1)	# 52-52	 **attackbox here**
    loopRest()
    sprite('jn433_01', 1)	# 53-53
    Unknown2006()
    sprite('jn433_02', 1)	# 54-54
    sprite('jn433_03', 1)	# 55-55
    sprite('jn433_04', 1)	# 56-56
    sprite('jn433_05', 1)	# 57-57
    sprite('jn433_07', 1)	# 58-58
    sprite('jn433_09', 1)	# 59-59
    Unknown3029(1)
    Unknown3069(0)
    sprite('jn433_14', 3)	# 60-62	 **attackbox here**
    RefreshMultihit()
    Unknown3038(1)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    GFX_1('jnef_finishatc', 0)
    ScreenShake(0, 16000)
    Unknown1086(22)
    teleportRelativeX(275000)
    teleportRelativeY(0)
    Unknown2015(20)
    sprite('jn414_09', 1)	# 63-63	 **attackbox here**
    Unknown2005()
    Unknown3038(0)
    Unknown1045(-10000)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('jn414_09', 2)	# 64-65	 **attackbox here**
    StartMultihit()
    sprite('jn414_10', 20)	# 66-85
    sprite('jn414_10', 20)	# 86-105
    SFX_1('jn254')
    sprite('jn414_11', 6)	# 106-111
    GFX_0('EffNoutou', 0)
    sprite('jn414_12', 70)	# 112-181
    ScreenShake(40000, 40000)
    GFX_0('YukikazedmyOD', -1)
    sprite('jn414_13', 5)	# 182-186
    sprite('jn414_14', 5)	# 187-191
    ExitState()

@State
def astral():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Hitstop(0)
        PushbackX(0)
        AirUntechableTime(200)
        Damage(0)
        Unknown11091(100)
        AirPushbackX(0)
        AirPushbackY(-100000)
        Unknown11084(1)
        Unknown9250(360)
        Unknown9262(380)
        HitLow(2)
        Unknown11033(3)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown2004(1, 0)
        Unknown28(12, 'astral2')
        setInvincible(1)
    sprite('jn450_00', 5)	# 1-5
    sprite('jn450_01', 5)	# 6-10
    Unknown2036(71, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_JN_AH', -1)
    SFX_4('bjn290')
    sprite('jn450_02', 5)	# 11-15
    sprite('jn450_03', 5)	# 16-20
    sprite('jn450_04', 5)	# 21-25
    sprite('jn450_05', 5)	# 26-30
    sprite('jn450_06', 5)	# 31-35
    sprite('jn450_07', 5)	# 36-40
    sprite('jn450_08', 5)	# 41-45
    sprite('jn450_09', 5)	# 46-50
    sprite('jn450_10', 5)	# 51-55
    SFX_0('019_cloth_c')
    SFX_0('019_cloth_a')
    sprite('jn450_11', 5)	# 56-60
    sprite('jn450_12', 5)	# 61-65
    sprite('jn450_13', 5)	# 66-70
    sprite('jn450_14', 5)	# 71-75
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('jn450_15', 5)	# 76-80
    sprite('jn450_16', 5)	# 81-85
    sprite('jn450_17', 5)	# 86-90
    sprite('jn450_18', 10)	# 91-100	 **attackbox here**
    GFX_0('JNEF_ast_attack', 0)
    SFX_3('jnse_22')
    setInvincible(0)
    sprite('jn450_19', 5)	# 101-105
    sprite('jn450_20', 5)	# 106-110
    sprite('jn450_21', 5)	# 111-115
    sprite('jn450_22', 5)	# 116-120
    sprite('jn450_23', 5)	# 121-125
    sprite('jn450_24', 5)	# 126-130
    sprite('jn450_25', 5)	# 131-135
    sprite('jn450_26', 5)	# 136-140
    sprite('jn450_27', 5)	# 141-145
    sprite('jn450_28', 5)	# 146-150
    Unknown2003(1)
    sprite('jn450_29', 5)	# 151-155	 **attackbox here**
    GFX_0('EffNoutou', 0)
    Unknown23024(0)
    sprite('jn450_30', 5)	# 156-160
    sprite('jn450_31', 5)	# 161-165
    sprite('jn450_32', 5)	# 166-170
    sprite('jn450_33', 5)	# 171-175
    sprite('jn450_34', 5)	# 176-180
    sprite('jn450_35', 5)	# 181-185
    sprite('jn450_36', 5)	# 186-190
    sprite('jn450_37', 5)	# 191-195

@State
def astral2():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Unknown2004(1, 0)
        Unknown23024(3)
        setInvincible(1)
        Unknown23084(1)
        Unknown2003(1)
        Unknown23088(1, 1)
        Unknown23157(1)
        GFX_0('LookAtMe', -1)
        Unknown38(8, 1)
        Unknown23025(1)
        Unknown11067(1)
        Unknown2017(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown20004(1)
    sprite('jn450_19', 3)	# 1-3
    GFX_0('AstralStartPtc', -1)
    GFX_0('ef_jnah_A', 101)
    GFX_0('ef_jnah_B', 101)
    GFX_1('jnef_ast_icewind', 101)
    sprite('jn450_20', 3)	# 4-6
    sprite('jn450_21', 3)	# 7-9
    sprite('jn450_19', 3)	# 10-12
    sprite('jn450_20', 3)	# 13-15
    sprite('jn450_21', 3)	# 16-18
    sprite('jn450_19', 3)	# 19-21
    sprite('jn450_20', 3)	# 22-24
    sprite('jn450_21', 3)	# 25-27
    sprite('jn450_19', 3)	# 28-30
    sprite('jn450_20', 3)	# 31-33
    sprite('jn450_21', 3)	# 34-36
    sprite('jn450_19', 3)	# 37-39
    sprite('jn450_20', 3)	# 40-42
    sprite('jn450_21', 3)	# 43-45
    sprite('jn450_19', 3)	# 46-48
    sprite('jn450_20', 3)	# 49-51
    sprite('jn450_21', 3)	# 52-54
    sprite('jn450_19', 3)	# 55-57
    sprite('jn450_20', 3)	# 58-60
    sprite('jn450_21', 3)	# 61-63
    sprite('jn450_19', 3)	# 64-66
    sprite('jn450_20', 3)	# 67-69
    sprite('jn450_21', 3)	# 70-72
    sprite('jn450_19', 3)	# 73-75
    sprite('jn450_20', 3)	# 76-78
    sprite('jn450_21', 3)	# 79-81
    sprite('jn450_19', 3)	# 82-84
    sprite('jn450_20', 3)	# 85-87
    sprite('jn450_21', 3)	# 88-90
    sprite('jn450_19', 3)	# 91-93
    sprite('jn450_20', 3)	# 94-96
    sprite('jn450_21', 3)	# 97-99
    sprite('jn450_19', 3)	# 100-102
    sprite('jn450_20', 3)	# 103-105
    sprite('jn450_21', 3)	# 106-108
    sprite('jn450_19', 3)	# 109-111
    sprite('jn450_20', 3)	# 112-114
    sprite('jn450_21', 3)	# 115-117
    sprite('jn450_19', 3)	# 118-120
    sprite('jn450_20', 3)	# 121-123
    sprite('jn450_21', 3)	# 124-126
    sprite('jn450_19', 3)	# 127-129
    sprite('jn450_20', 3)	# 130-132
    sprite('jn450_21', 3)	# 133-135
    sprite('jn450_19', 3)	# 136-138
    sprite('jn450_20', 3)	# 139-141
    sprite('jn450_21', 3)	# 142-144
    sprite('jn450_19', 3)	# 145-147
    sprite('jn450_20', 3)	# 148-150
    sprite('jn450_21', 3)	# 151-153
    sprite('jn450_19', 3)	# 154-156
    sprite('jn450_20', 3)	# 157-159
    sprite('jn450_21', 3)	# 160-162
    sprite('jn450_19', 3)	# 163-165
    sprite('jn450_20', 3)	# 166-168
    sprite('jn450_21', 3)	# 169-171
    sprite('jn450_19', 3)	# 172-174
    sprite('jn450_20', 3)	# 175-177
    sprite('jn450_21', 3)	# 178-180
    sprite('jn450_19', 3)	# 181-183
    sprite('jn450_20', 3)	# 184-186
    sprite('jn450_21', 3)	# 187-189
    sprite('jn450_19', 3)	# 190-192
    sprite('jn450_20', 3)	# 193-195
    sprite('jn450_21', 3)	# 196-198
    sprite('jn450_19', 3)	# 199-201
    sprite('jn450_20', 3)	# 202-204
    sprite('jn450_21', 3)	# 205-207
    sprite('jn450_19', 3)	# 208-210
    sprite('jn450_20', 3)	# 211-213
    sprite('jn450_21', 3)	# 214-216
    sprite('jn450_19', 3)	# 217-219
    sprite('jn450_20', 3)	# 220-222
    sprite('jn450_21', 3)	# 223-225
    sprite('jn450_22', 5)	# 226-230
    sprite('jn450_23', 5)	# 231-235
    sprite('jn450_24', 5)	# 236-240
    sprite('jn450_25', 5)	# 241-245
    sprite('jn450_26', 5)	# 246-250
    SFX_4('bjn291')
    sprite('jn450_27', 5)	# 251-255
    sprite('jn450_28', 5)	# 256-260
    GFX_0('AstralFinishPtc', -1)
    GFX_0('EffNoutou', 0)
    sprite('jn450_29', 5)	# 261-265	 **attackbox here**
    Unknown2003(0)
    Unknown11023(1)
    Unknown11064(4)
    Unknown9016(1)
    Unknown11091(100)
    Damage(27315)
    Hitstop(0)
    RefreshMultihit()
    SFX_0('018_ice_break_1')
    Unknown23024(2)
    sprite('jn450_29add01', 7)	# 266-272	 **attackbox here**
    sprite('jn450_29add02', 7)	# 273-279	 **attackbox here**
    sprite('jn450_29add03', 7)	# 280-286	 **attackbox here**
    sprite('jn450_29add04', 70)	# 287-356	 **attackbox here**
    sprite('jn450_29add04', 70)	# 357-426	 **attackbox here**
    Unknown20000(1)
    Unknown20006(1)
    Unknown13(8)
    sprite('jn450_30', 7)	# 427-433
    sprite('jn450_31', 7)	# 434-440
    sprite('jn450_32', 7)	# 441-447
    sprite('jn450_33', 7)	# 448-454
    sprite('jn450_34', 7)	# 455-461
    sprite('jn450_35', 7)	# 462-468
    Unknown2001()
    sprite('jn450_36', 7)	# 469-475
    sprite('jn450_37', 7)	# 476-482
    sprite('jn000_00', 7)	# 483-489
    teleportRelativeX(128000)
    sprite('jn000_01', 7)	# 490-496
    sprite('jn000_02', 7)	# 497-503
    sprite('jn000_03', 7)	# 504-510
    sprite('jn000_04', 7)	# 511-517
    Unknown18010()
    sprite('jn000_05', 7)	# 518-524
    sprite('jn000_06', 7)	# 525-531
    sprite('jn000_07', 7)	# 532-538
    sprite('jn000_08', 7)	# 539-545
    sprite('jn000_09', 7)	# 546-552
    sprite('jn611_00', 5)	# 553-557
    sprite('jn611_01', 5)	# 558-562
    SFX_4('bjn521')
    sprite('jn611_02', 5)	# 563-567
    sprite('jn611_03', 5)	# 568-572
    sprite('jn611_04', 5)	# 573-577
    sprite('jn611_05', 5)	# 578-582
    GFX_0('jnef611icewing', 0)
    sprite('jn611_06', 5)	# 583-587
    sprite('jn611_07', 5)	# 588-592
    sprite('jn611_08', 5)	# 593-597
    sprite('jn611_09', 5)	# 598-602
    sprite('jn611_10', 5)	# 603-607
    sprite('jn611_11', 5)	# 608-612
    sprite('jn611_12', 5)	# 613-617
    sprite('jn611_13', 150)	# 618-767
    sprite('jn611_13', 5)	# 768-772
    sprite('jn611_13', 32767)	# 773-33539
    Unknown18008()
    loopRest()
    ExitState()

@State
def NanDato():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('jn430_26', 3)	# 1-3
    sprite('jn430_25', 4)	# 4-7
    sprite('jn430_24', 10)	# 8-17
    sprite('jn430_23', 1)	# 18-18
    GFX_0('EffNoutou', 0)
    sprite('jn430_24', 1)	# 19-19
    sprite('jn430_23', 1)	# 20-20
    sprite('jn430_24', 10)	# 21-30
    SFX_0('014_electric_m')
    ScreenShake(12000, 0)
    sprite('jn430_24', 30)	# 31-60
    SFX_1('jn039')
    sprite('jn430_25', 5)	# 61-65
    sprite('jn430_26', 4)	# 66-69

@State
def StoryYowai5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AttackP1(100)
        AttackP2(80)
        AirPushbackY(10000)
        AirPushbackX(24000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        JumpCancel_(0)
        Unknown23027()
    sprite('jn203_00', 2)	# 1-2
    Unknown1019(25)
    sprite('jn203_01', 2)	# 3-4
    Unknown7009(1)
    sprite('jn203_02', 2)	# 5-6
    sprite('jn203_03', 2)	# 7-8
    Unknown1047(8333)
    sprite('jn203_04', 2)	# 9-10
    sprite('jn203_05', 1)	# 11-11
    sprite('jn203_06', 1)	# 12-12
    sprite('jn203_07ex01', 4)	# 13-16	 **attackbox here**
    RefreshMultihit()
    ScreenShake(0, 5000)
    sprite('jn203_08', 8)	# 17-24	 **attackbox here**
    Unknown23027()
    sprite('jn203_09', 4)	# 25-28
    sprite('jn203_10', 4)	# 29-32
    sprite('jn203_11', 4)	# 33-36
    sprite('jn203_12', 4)	# 37-40
    sprite('jn203_13', 4)	# 41-44

@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBOunce_()
        Unknown2017(0)

        def upon_14():
            SFX_1('jn054')
    sprite('jn900_00', 32767)	# 1-32767	 **attackbox here**
    Unknown2017(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown20001(1)
    Unknown20000(1)
    Unknown20004(1)
    Unknown2007()
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown1084(1)
    loopRest()

@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBOunce_()
        Unknown2017(0)
        teleportRelativeY(200000)
    sprite('jn901_00', 50)	# 1-50
    physicsYImpulse(-150)
    sprite('jn901_00', 50)	# 51-100
    physicsYImpulse(150)
    SFX_1('jn055')
    label(0)
    sprite('jn901_00', 50)	# 101-150
    physicsYImpulse(-150)
    sprite('jn901_00', 50)	# 151-200
    physicsYImpulse(150)
    gotoLabel(0)

@Subroutine
def MouthTableInit():
    Unknown18011('bjn000', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn500', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn501', 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 24882, 25398, 24886, 12337, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn502', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn503', 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn504', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn505', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn520', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24888, 25397, 24885, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn521', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn522', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 12643, 12848, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn523', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 24888, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn524', 12643, 24881, 25399, 12345, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn525', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn402_0', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn402_1', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn403_0', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn403_1', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn600biz', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 12343, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn601bjb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 12853, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn601bma', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn600bno', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn600brg', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 14133, 12641, 25392, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn600pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 13665, 13667, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24885, 25397, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn601pyo', 13155, 24881, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn600rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn600uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn601uyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn700biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn701bjb', 12643, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn700bma', 12643, 14177, 14179, 14177, 14179, 14177, 14435, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn701bno', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn701brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 24880, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 12337, 24882, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn701pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn700pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn700rbl', 12643, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn701uor', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn701uyu', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjn702pyo', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bno')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bjb')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('brg')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uor')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uyu')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('bma')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('biz')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('jn600_00', 6)	# 2-7
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    sprite('jn600_01', 6)	# 8-13
    if SLOT_158:
        Unknown7006('bjn501', 100, 896428642, 13104, 0, 0, 100, 896428642, 13360, 0, 0, 100, 896428642, 13616, 0, 0, 100)
    sprite('jn600_02', 6)	# 14-19
    sprite('jn600_03', 6)	# 20-25
    label(1)
    sprite('jn600_00', 6)	# 26-31
    sprite('jn600_01', 6)	# 32-37
    sprite('jn600_02', 6)	# 38-43
    sprite('jn600_03', 6)	# 44-49
    if SLOT_97:
        _gotolabel(1)
    sprite('jn600_04', 6)	# 50-55
    sprite('jn600_05', 6)	# 56-61
    sprite('jn600_06', 6)	# 62-67
    sprite('jn600_07', 6)	# 68-73
    sprite('jn600_08', 6)	# 74-79
    Unknown21007(24, 41)
    sprite('jn600_09', 6)	# 80-85
    sprite('jn600_10', 6)	# 86-91
    sprite('jn600_11', 6)	# 92-97
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 98-103
    sprite('jn600_13', 6)	# 104-109
    sprite('jn600_14', 6)	# 110-115
    sprite('jn600_15', 6)	# 116-121
    sprite('jn600_16', 6)	# 122-127
    sprite('jn600_17', 6)	# 128-133
    sprite('jn600_18', 6)	# 134-139
    loopRest()
    ExitState()
    label(10)
    sprite('jn601_00', 6)	# 140-145
    GFX_0('jnef601makeSword', 0)
    Unknown38(6, 1)
    SFX_3('jnse_22')
    sprite('jn601_01', 6)	# 146-151
    sprite('jn601_02', 6)	# 152-157
    sprite('jn601_03', 6)	# 158-163
    Unknown36(6)
    sendToLabel(1)
    Unknown35()
    sprite('jn601_04', 6)	# 164-169
    sprite('jn601_05', 6)	# 170-175
    sprite('jn601_06', 6)	# 176-181
    SFX_0('008_swing_pole_1')
    sprite('jn601_07', 6)	# 182-187
    sprite('jn601_08', 6)	# 188-193
    SFX_0('008_swing_pole_1')
    sprite('jn601_09', 6)	# 194-199
    sprite('jn601_10', 6)	# 200-205
    SFX_0('008_swing_pole_1')
    sprite('jn601_11', 6)	# 206-211
    sprite('jn601_12', 140)	# 212-351
    if SLOT_158:
        Unknown7006('bjn500', 100, 896428642, 12848, 0, 0, 100, 896428642, 13360, 0, 0, 100, 896428642, 13616, 0, 0, 100)
    Unknown21007(24, 41)
    Unknown23018(1)
    sprite('jn601_12', 30)	# 352-381
    sprite('jn601_12', 30)	# 382-411
    sprite('jn601_13', 6)	# 412-417
    sprite('jn601_14', 6)	# 418-423
    loopRest()
    ExitState()
    label(20)
    sprite('jn601_00', 3)	# 424-426
    GFX_0('ptPhantom_NoSound', -1)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(-100000)
    Unknown2019(-500)
    Unknown35()
    label(4)
    sprite('jn601_00', 3)	# 427-429
    loopRest()
    if SLOT_17:
        _gotolabel(4)
    sprite('jn601_00', 6)	# 430-435
    GFX_0('jnef601makeSword', 0)
    Unknown38(6, 1)
    SFX_3('jnse_22')
    sprite('jn601_01', 6)	# 436-441
    sprite('jn601_02', 6)	# 442-447
    sprite('jn601_03', 6)	# 448-453
    Unknown36(6)
    sendToLabel(1)
    Unknown35()
    sprite('jn601_04', 6)	# 454-459
    sprite('jn601_05', 6)	# 460-465
    if SLOT_43:
        SFX_1('jn416')
    sprite('jn601_06', 6)	# 466-471
    SFX_0('008_swing_pole_1')
    sprite('jn601_07', 6)	# 472-477
    sprite('jn601_08', 6)	# 478-483
    SFX_0('008_swing_pole_1')
    sprite('jn601_09', 6)	# 484-489
    sprite('jn601_10', 6)	# 490-495
    SFX_0('008_swing_pole_1')
    sprite('jn601_11', 6)	# 496-501
    sprite('jn601_12', 125)	# 502-626
    Unknown21007(24, 41)
    if SLOT_44:
        SFX_1('jn416')
    sprite('jn601_12', 30)	# 627-656
    if SLOT_44:
        SFX_1('jn417')
    sprite('jn601_12', 30)	# 657-686
    if SLOT_43:
        SFX_1('jn417')
    sprite('jn601_13', 6)	# 687-692
    Unknown21007(4, 32)
    sprite('jn601_14', 6)	# 693-698
    Unknown21011(50)
    loopRest()
    ExitState()
    label(30)
    sprite('jn631_00', 6)	# 699-704
    SFX_1('bjn600biz')
    sprite('jn631_01', 6)	# 705-710
    sprite('jn631_02', 6)	# 711-716
    sprite('jn631_03', 100)	# 717-816
    sprite('jn631_04', 3)	# 817-819
    sprite('jn631_05', 3)	# 820-822
    sprite('jn631_06', 3)	# 823-825
    sprite('jn631_07', 3)	# 826-828
    SFX_0('009_swing_rapier_1')
    sprite('jn631_08', 32767)	# 829-33595
    label(100)
    sprite('jn600_00', 6)	# 33596-33601
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    SFX_1('bjn600bno')
    label(101)
    sprite('jn600_01', 6)	# 33602-33607
    sprite('jn600_02', 6)	# 33608-33613
    sprite('jn600_03', 6)	# 33614-33619
    if SLOT_97:
        _gotolabel(101)
    sprite('jn600_04', 6)	# 33620-33625
    sprite('jn600_05', 6)	# 33626-33631
    sprite('jn600_06', 6)	# 33632-33637
    sprite('jn600_07', 6)	# 33638-33643
    sprite('jn600_08', 6)	# 33644-33649
    sprite('jn600_09', 6)	# 33650-33655
    sprite('jn600_10', 6)	# 33656-33661
    sprite('jn600_11', 6)	# 33662-33667
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 33668-33673
    sprite('jn600_13', 6)	# 33674-33679
    sprite('jn600_14', 6)	# 33680-33685
    sprite('jn600_15', 6)	# 33686-33691
    sprite('jn600_16', 6)	# 33692-33697
    sprite('jn600_17', 6)	# 33698-33703
    sprite('jn600_18', 6)	# 33704-33709
    Unknown21007(24, 40)
    Unknown21011(120)
    label(102)
    sprite('jn000_00', 7)	# 33710-33716
    sprite('jn000_01', 7)	# 33717-33723
    sprite('jn000_02', 7)	# 33724-33730
    sprite('jn000_03', 7)	# 33731-33737
    sprite('jn000_04', 7)	# 33738-33744
    sprite('jn000_05', 7)	# 33745-33751
    sprite('jn000_06', 7)	# 33752-33758
    sprite('jn000_07', 7)	# 33759-33765
    sprite('jn000_08', 7)	# 33766-33772
    sprite('jn000_09', 7)	# 33773-33779
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('jn600_00', 6)	# 33780-33785
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
        SFX_1('bjn601pyo')
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    label(111)
    sprite('jn600_01', 6)	# 33786-33791
    sprite('jn600_02', 6)	# 33792-33797
    sprite('jn600_03', 6)	# 33798-33803
    gotoLabel(111)
    label(112)
    sprite('jn600_01', 6)	# 33804-33809
    sprite('jn600_02', 6)	# 33810-33815
    sprite('jn600_03', 6)	# 33816-33821
    if SLOT_97:
        _gotolabel(112)
    sprite('jn600_04', 6)	# 33822-33827
    sprite('jn600_05', 6)	# 33828-33833
    sprite('jn600_06', 6)	# 33834-33839
    sprite('jn600_07', 6)	# 33840-33845
    sprite('jn600_08', 6)	# 33846-33851
    sprite('jn600_09', 6)	# 33852-33857
    sprite('jn600_10', 6)	# 33858-33863
    sprite('jn600_11', 6)	# 33864-33869
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 33870-33875
    sprite('jn600_13', 6)	# 33876-33881
    sprite('jn600_14', 6)	# 33882-33887
    sprite('jn600_15', 6)	# 33888-33893
    sprite('jn600_16', 6)	# 33894-33899
    sprite('jn600_17', 6)	# 33900-33905
    sprite('jn600_18', 6)	# 33906-33911
    Unknown21011(120)
    label(113)
    sprite('jn000_00', 7)	# 33912-33918
    sprite('jn000_01', 7)	# 33919-33925
    sprite('jn000_02', 7)	# 33926-33932
    sprite('jn000_03', 7)	# 33933-33939
    sprite('jn000_04', 7)	# 33940-33946
    sprite('jn000_05', 7)	# 33947-33953
    sprite('jn000_06', 7)	# 33954-33960
    sprite('jn000_07', 7)	# 33961-33967
    sprite('jn000_08', 7)	# 33968-33974
    sprite('jn000_09', 7)	# 33975-33981
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('jn000_00', 1)	# 33982-33982
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('jn000_00', 7)	# 33983-33989
    sprite('jn000_01', 7)	# 33990-33996
    sprite('jn000_02', 7)	# 33997-34003
    sprite('jn000_03', 7)	# 34004-34010
    sprite('jn000_04', 7)	# 34011-34017
    sprite('jn000_05', 7)	# 34018-34024
    sprite('jn000_06', 7)	# 34025-34031
    sprite('jn000_07', 7)	# 34032-34038
    sprite('jn000_08', 7)	# 34039-34045
    sprite('jn000_09', 7)	# 34046-34052
    gotoLabel(121)
    label(122)
    sprite('jn001_00', 8)	# 34053-34060
    SFX_1('bjn601bjb')
    sprite('jn001_01', 8)	# 34061-34068
    sprite('jn001_02', 10)	# 34069-34078
    sprite('jn001_03', 8)	# 34079-34086
    sprite('jn001_04', 8)	# 34087-34094
    sprite('jn001_05', 8)	# 34095-34102
    sprite('jn001_06', 10)	# 34103-34112
    sprite('jn001_07', 8)	# 34113-34120
    sprite('jn001_08', 8)	# 34121-34128
    sprite('jn001_09', 8)	# 34129-34136
    sprite('jn000_00', 7)	# 34137-34143
    sprite('jn430_00', 3)	# 34144-34146
    SFX_0('009_swing_rapier_2')
    sprite('jn430_04', 4)	# 34147-34150
    sprite('jn430_03', 4)	# 34151-34154
    sprite('jn430_02', 4)	# 34155-34158
    sprite('jn430_01', 80)	# 34159-34238
    sprite('jn410_14', 2)	# 34239-34240
    SFX_0('009_swing_rapier_1')
    sprite('jn410_15', 3)	# 34241-34243	 **attackbox here**
    sprite('jn410_16', 4)	# 34244-34247
    sprite('jn410_17', 4)	# 34248-34251
    sprite('jn410_18', 4)	# 34252-34255
    sprite('jn410_19', 80)	# 34256-34335
    GFX_0('EffNoutou', 0)
    sprite('jn410_20', 7)	# 34336-34342
    Unknown23018(1)
    label(123)
    sprite('jn000_00', 7)	# 34343-34349
    sprite('jn000_01', 7)	# 34350-34356
    sprite('jn000_02', 7)	# 34357-34363
    sprite('jn000_03', 7)	# 34364-34370
    sprite('jn000_04', 7)	# 34371-34377
    sprite('jn000_05', 7)	# 34378-34384
    sprite('jn000_06', 7)	# 34385-34391
    sprite('jn000_07', 7)	# 34392-34398
    sprite('jn000_08', 7)	# 34399-34405
    sprite('jn000_09', 7)	# 34406-34412
    gotoLabel(123)
    ExitState()
    label(130)
    sprite('jn600_00', 6)	# 34413-34418
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    sprite('jn600_01', 6)	# 34419-34424
    sprite('jn600_02', 6)	# 34425-34430
    SFX_1('bjn600rbl')
    sprite('jn600_03', 6)	# 34431-34436
    label(131)
    sprite('jn600_00', 6)	# 34437-34442
    sprite('jn600_01', 6)	# 34443-34448
    sprite('jn600_02', 6)	# 34449-34454
    sprite('jn600_03', 6)	# 34455-34460
    if SLOT_97:
        _gotolabel(131)
    sprite('jn600_04', 6)	# 34461-34466
    sprite('jn600_05', 6)	# 34467-34472
    sprite('jn600_06', 6)	# 34473-34478
    sprite('jn600_07', 6)	# 34479-34484
    sprite('jn600_08', 6)	# 34485-34490
    sprite('jn600_09', 6)	# 34491-34496
    sprite('jn600_10', 6)	# 34497-34502
    sprite('jn600_11', 6)	# 34503-34508
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 34509-34514
    sprite('jn600_13', 6)	# 34515-34520
    sprite('jn600_14', 6)	# 34521-34526
    sprite('jn600_15', 6)	# 34527-34532
    sprite('jn600_16', 6)	# 34533-34538
    sprite('jn600_17', 6)	# 34539-34544
    sprite('jn600_18', 6)	# 34545-34550
    Unknown21007(24, 40)
    Unknown21011(120)
    label(132)
    sprite('jn000_00', 7)	# 34551-34557
    sprite('jn000_01', 7)	# 34558-34564
    sprite('jn000_02', 7)	# 34565-34571
    sprite('jn000_03', 7)	# 34572-34578
    sprite('jn000_04', 7)	# 34579-34585
    sprite('jn000_05', 7)	# 34586-34592
    sprite('jn000_06', 7)	# 34593-34599
    sprite('jn000_07', 7)	# 34600-34606
    sprite('jn000_08', 7)	# 34607-34613
    sprite('jn000_09', 7)	# 34614-34620
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('jn630_00', 1)	# 34621-34621
    Unknown2019(100)
    if SLOT_158:
        Unknown1000(-1450000)
    else:
        Unknown1000(-1450000)
    SFX_1('bjn600brg')
    sprite('jn630_00', 240)	# 34622-34861
    sprite('jn630_01', 6)	# 34862-34867
    sprite('jn202_00', 2)	# 34868-34869
    sprite('jn202_01', 2)	# 34870-34871
    sprite('jn202_02', 2)	# 34872-34873
    sprite('jn202_03', 3)	# 34874-34876
    Unknown21007(24, 40)
    sprite('jn202_04', 2)	# 34877-34878	 **attackbox here**
    StartMultihit()
    GFX_0('zan_b0', -1)
    SFX_0('009_swing_rapier_1')
    sprite('jn202_05', 2)	# 34879-34880	 **attackbox here**
    StartMultihit()
    sprite('jn202_05', 5)	# 34881-34885	 **attackbox here**
    StartMultihit()
    sprite('jn202_06', 2)	# 34886-34887
    sprite('jn202_08', 3)	# 34888-34890
    sprite('jn202_09', 3)	# 34891-34893
    sprite('jn202_10', 2)	# 34894-34895
    sprite('jn202_11', 1)	# 34896-34896
    sprite('jn202_12', 1)	# 34897-34897
    sprite('jn202_14', 1)	# 34898-34898
    GFX_0('EffNoutou', 0)
    sprite('jn202_16', 1)	# 34899-34899
    sprite('jn000_00', 7)	# 34900-34906
    sprite('jn000_01', 7)	# 34907-34913
    sprite('jn000_02', 7)	# 34914-34920
    sprite('jn000_03', 7)	# 34921-34927
    sprite('jn000_04', 7)	# 34928-34934
    sprite('jn000_05', 7)	# 34935-34941
    sprite('jn000_06', 7)	# 34942-34948
    sprite('jn000_07', 7)	# 34949-34955
    sprite('jn000_08', 7)	# 34956-34962
    sprite('jn000_09', 7)	# 34963-34969
    sprite('jn000_00', 7)	# 34970-34976
    sprite('jn000_01', 7)	# 34977-34983
    sprite('jn000_02', 7)	# 34984-34990
    sprite('jn000_03', 7)	# 34991-34997
    sprite('jn000_04', 7)	# 34998-35004
    sprite('jn000_05', 7)	# 35005-35011
    sprite('jn000_06', 7)	# 35012-35018
    sprite('jn000_07', 7)	# 35019-35025
    sprite('jn000_08', 7)	# 35026-35032
    sprite('jn000_09', 7)	# 35033-35039
    Unknown21011(120)
    Unknown21007(24, 39)
    label(141)
    sprite('jn000_00', 7)	# 35040-35046
    sprite('jn000_01', 7)	# 35047-35053
    sprite('jn000_02', 7)	# 35054-35060
    sprite('jn000_03', 7)	# 35061-35067
    sprite('jn000_04', 7)	# 35068-35074
    sprite('jn000_05', 7)	# 35075-35081
    sprite('jn000_06', 7)	# 35082-35088
    sprite('jn000_07', 7)	# 35089-35095
    sprite('jn000_08', 7)	# 35096-35102
    sprite('jn000_09', 7)	# 35103-35109
    gotoLabel(141)
    ExitState()
    label(150)
    sprite('jn600_00', 6)	# 35110-35115
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    SFX_1('bjn600uor')
    sprite('jn600_01', 6)	# 35116-35121
    sprite('jn600_02', 6)	# 35122-35127
    sprite('jn600_03', 6)	# 35128-35133
    Unknown2037(3)
    label(151)
    sprite('jn600_00', 6)	# 35134-35139
    sprite('jn600_01', 6)	# 35140-35145
    sprite('jn600_02', 6)	# 35146-35151
    sprite('jn600_03', 6)	# 35152-35157
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(151)
    sprite('jn600_04', 6)	# 35158-35163
    sprite('jn600_05', 6)	# 35164-35169
    sprite('jn600_06', 6)	# 35170-35175
    sprite('jn600_07', 6)	# 35176-35181
    sprite('jn600_08', 6)	# 35182-35187
    sprite('jn600_09', 6)	# 35188-35193
    sprite('jn600_10', 6)	# 35194-35199
    sprite('jn600_11', 6)	# 35200-35205
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 35206-35211
    Unknown21007(24, 40)
    sprite('jn600_13', 6)	# 35212-35217
    sprite('jn600_14', 6)	# 35218-35223
    sprite('jn600_15', 6)	# 35224-35229
    sprite('jn600_16', 6)	# 35230-35235
    sprite('jn600_17', 6)	# 35236-35241
    sprite('jn600_18', 6)	# 35242-35247
    Unknown21011(200)
    label(152)
    sprite('jn000_00', 7)	# 35248-35254
    sprite('jn000_01', 7)	# 35255-35261
    sprite('jn000_02', 7)	# 35262-35268
    sprite('jn000_03', 7)	# 35269-35275
    sprite('jn000_04', 7)	# 35276-35282
    sprite('jn000_05', 7)	# 35283-35289
    sprite('jn000_06', 7)	# 35290-35296
    sprite('jn000_07', 7)	# 35297-35303
    sprite('jn000_08', 7)	# 35304-35310
    sprite('jn000_09', 7)	# 35311-35317
    gotoLabel(152)
    label(160)
    sprite('jn600_00', 1)	# 35318-35318
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
        SFX_1('bjn601uyu')
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    label(161)
    sprite('jn600_01', 6)	# 35319-35324
    sprite('jn600_02', 6)	# 35325-35330
    sprite('jn600_03', 6)	# 35331-35336
    gotoLabel(161)
    label(162)
    sprite('jn600_01', 6)	# 35337-35342
    sprite('jn600_02', 6)	# 35343-35348
    sprite('jn600_03', 6)	# 35349-35354
    if SLOT_97:
        _gotolabel(162)
    sprite('jn600_04', 6)	# 35355-35360
    sprite('jn600_05', 6)	# 35361-35366
    sprite('jn600_06', 6)	# 35367-35372
    sprite('jn600_07', 6)	# 35373-35378
    sprite('jn600_08', 6)	# 35379-35384
    sprite('jn600_09', 6)	# 35385-35390
    sprite('jn600_10', 6)	# 35391-35396
    sprite('jn600_11', 6)	# 35397-35402
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 35403-35408
    sprite('jn600_13', 6)	# 35409-35414
    sprite('jn600_14', 6)	# 35415-35420
    sprite('jn600_15', 6)	# 35421-35426
    sprite('jn600_16', 6)	# 35427-35432
    sprite('jn600_17', 6)	# 35433-35438
    sprite('jn600_18', 6)	# 35439-35444
    Unknown23018(1)
    label(163)
    sprite('jn000_00', 7)	# 35445-35451
    sprite('jn000_01', 7)	# 35452-35458
    sprite('jn000_02', 7)	# 35459-35465
    sprite('jn000_03', 7)	# 35466-35472
    sprite('jn000_04', 7)	# 35473-35479
    sprite('jn000_05', 7)	# 35480-35486
    sprite('jn000_06', 7)	# 35487-35493
    sprite('jn000_07', 7)	# 35494-35500
    sprite('jn000_08', 7)	# 35501-35507
    sprite('jn000_09', 7)	# 35508-35514
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('jn600_00', 6)	# 35515-35520
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    SFX_1('bjn600pmi')
    sprite('jn600_01', 6)	# 35521-35526
    sprite('jn600_02', 6)	# 35527-35532
    sprite('jn600_03', 6)	# 35533-35538
    Unknown2037(3)
    label(171)
    sprite('jn600_00', 6)	# 35539-35544
    sprite('jn600_01', 6)	# 35545-35550
    sprite('jn600_02', 6)	# 35551-35556
    sprite('jn600_03', 6)	# 35557-35562
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(171)
    sprite('jn600_04', 6)	# 35563-35568
    sprite('jn600_05', 6)	# 35569-35574
    sprite('jn600_06', 6)	# 35575-35580
    sprite('jn600_07', 6)	# 35581-35586
    sprite('jn600_08', 6)	# 35587-35592
    sprite('jn600_09', 6)	# 35593-35598
    sprite('jn600_10', 6)	# 35599-35604
    sprite('jn600_11', 6)	# 35605-35610
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 35611-35616
    sprite('jn600_13', 6)	# 35617-35622
    sprite('jn600_14', 6)	# 35623-35628
    sprite('jn600_15', 6)	# 35629-35634
    sprite('jn600_16', 6)	# 35635-35640
    sprite('jn600_17', 6)	# 35641-35646
    sprite('jn600_18', 6)	# 35647-35652
    label(172)
    sprite('jn000_00', 7)	# 35653-35659
    sprite('jn000_01', 7)	# 35660-35666
    sprite('jn000_02', 7)	# 35667-35673
    sprite('jn000_03', 7)	# 35674-35680
    sprite('jn000_04', 7)	# 35681-35687
    sprite('jn000_05', 7)	# 35688-35694
    sprite('jn000_06', 7)	# 35695-35701
    sprite('jn000_07', 7)	# 35702-35708
    sprite('jn000_08', 7)	# 35709-35715
    sprite('jn000_09', 7)	# 35716-35722
    if SLOT_97:
        _gotolabel(172)
    sprite('jn000_00', 1)	# 35723-35723
    Unknown21007(24, 40)
    Unknown21011(240)
    label(173)
    sprite('jn000_00', 7)	# 35724-35730
    sprite('jn000_01', 7)	# 35731-35737
    sprite('jn000_02', 7)	# 35738-35744
    sprite('jn000_03', 7)	# 35745-35751
    sprite('jn000_04', 7)	# 35752-35758
    sprite('jn000_05', 7)	# 35759-35765
    sprite('jn000_06', 7)	# 35766-35772
    sprite('jn000_07', 7)	# 35773-35779
    sprite('jn000_08', 7)	# 35780-35786
    sprite('jn000_09', 7)	# 35787-35793
    gotoLabel(173)
    ExitState()
    label(180)
    sprite('jn600_00', 1)	# 35794-35794
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
        SFX_1('bjn601bma')
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    label(181)
    sprite('jn600_01', 6)	# 35795-35800
    sprite('jn600_02', 6)	# 35801-35806
    sprite('jn600_03', 6)	# 35807-35812
    gotoLabel(181)
    label(182)
    sprite('jn600_01', 6)	# 35813-35818
    sprite('jn600_02', 6)	# 35819-35824
    sprite('jn600_03', 6)	# 35825-35830
    if SLOT_97:
        _gotolabel(182)
    sprite('jn600_04', 6)	# 35831-35836
    sprite('jn600_05', 6)	# 35837-35842
    sprite('jn600_06', 6)	# 35843-35848
    sprite('jn600_07', 6)	# 35849-35854
    sprite('jn600_08', 6)	# 35855-35860
    sprite('jn600_09', 6)	# 35861-35866
    sprite('jn600_10', 6)	# 35867-35872
    sprite('jn600_11', 6)	# 35873-35878
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 35879-35884
    sprite('jn600_13', 6)	# 35885-35890
    sprite('jn600_14', 6)	# 35891-35896
    sprite('jn600_15', 6)	# 35897-35902
    sprite('jn600_16', 6)	# 35903-35908
    sprite('jn600_17', 6)	# 35909-35914
    sprite('jn600_18', 6)	# 35915-35920
    Unknown23018(1)
    label(183)
    sprite('jn000_00', 7)	# 35921-35927
    sprite('jn000_01', 7)	# 35928-35934
    sprite('jn000_02', 7)	# 35935-35941
    sprite('jn000_03', 7)	# 35942-35948
    sprite('jn000_04', 7)	# 35949-35955
    sprite('jn000_05', 7)	# 35956-35962
    sprite('jn000_06', 7)	# 35963-35969
    sprite('jn000_07', 7)	# 35970-35976
    sprite('jn000_08', 7)	# 35977-35983
    sprite('jn000_09', 7)	# 35984-35990
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('jn631_00', 6)	# 35991-35996
    Unknown2019(100)
    Unknown1000(-1300000)
    sprite('jn631_01', 6)	# 35997-36002
    sprite('jn631_02', 6)	# 36003-36008
    sprite('jn631_03', 120)	# 36009-36128
    SFX_1('bjn600biz')
    sprite('jn631_04', 3)	# 36129-36131
    sprite('jn631_05', 3)	# 36132-36134
    sprite('jn631_06', 3)	# 36135-36137
    sprite('jn631_07', 3)	# 36138-36140
    SFX_0('009_swing_rapier_1')
    label(191)
    sprite('jn631_08', 1)	# 36141-36141
    if SLOT_97:
        _gotolabel(191)
    sprite('jn631_08', 15)	# 36142-36156
    sprite('jn631_08', 32767)	# 36157-68923
    Unknown21007(24, 40)
    Unknown21011(260)
    ExitState()
    label(991)
    sprite('jn000_00', 1)	# 68924-68924
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('jn000_00', 7)	# 68925-68931
    sprite('jn000_01', 7)	# 68932-68938
    sprite('jn000_02', 7)	# 68939-68945
    sprite('jn000_03', 7)	# 68946-68952
    sprite('jn000_04', 7)	# 68953-68959
    sprite('jn000_05', 7)	# 68960-68966
    sprite('jn000_06', 7)	# 68967-68973
    sprite('jn000_07', 7)	# 68974-68980
    sprite('jn000_08', 7)	# 68981-68987
    sprite('jn000_09', 7)	# 68988-68994
    gotoLabel(992)
    label(993)
    sprite('jn033_00', 2)	# 68995-68996
    sprite('jn033_01', 3)	# 68997-68999

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
    sprite('jn033_02', 3)	# 69000-69002
    sprite('jn033_03', 3)	# 69003-69005
    sprite('jn033_04', 32767)	# 69006-101772
    label(995)
    sprite('null', 3)	# 101773-101775
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
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bjb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('biz'):
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
    sprite('jn611_00', 5)	# 4-8
    sprite('jn611_01', 5)	# 9-13
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bjn524', 100, 896428642, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bjn402_0', 100, 879651426, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bjn520', 100, 896428642, 12850, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn611_02', 5)	# 14-18
    sprite('jn611_03', 5)	# 19-23
    sprite('jn611_04', 5)	# 24-28
    sprite('jn611_05', 5)	# 29-33
    GFX_0('jnef611icewing', 0)
    SFX_3('jnse_02')
    sprite('jn611_06', 5)	# 34-38
    sprite('jn611_07', 5)	# 39-43
    sprite('jn611_08', 5)	# 44-48
    sprite('jn611_09', 5)	# 49-53
    sprite('jn611_10', 5)	# 54-58
    sprite('jn611_11', 5)	# 59-63
    sprite('jn611_12', 5)	# 64-68
    sprite('jn611_13', 60)	# 69-128
    sprite('jn611_13', 5)	# 129-133
    sprite('jn611_13', 32767)	# 134-32900
    Unknown23018(1)
    loopRest()
    ExitState()
    label(10)
    sprite('jn610_00', 5)	# 32901-32905
    sprite('jn610_01', 5)	# 32906-32910
    sprite('jn610_02', 5)	# 32911-32915
    sprite('jn610_03', 5)	# 32916-32920
    sprite('jn610_04', 5)	# 32921-32925
    sprite('jn610_05', 5)	# 32926-32930
    sprite('jn610_06', 5)	# 32931-32935
    sprite('jn610_07', 5)	# 32936-32940
    sprite('jn610_08', 140)	# 32941-33080
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bjn524', 100, 896428642, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bjn402_0', 100, 879651426, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bjn521', 100, 896428642, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('jn610_08', 32767)	# 33081-65847
    loopRest()
    ExitState()
    label(100)
    sprite('keep', 1)	# 65848-65848
    Unknown2053(0)
    Unknown2034(0)
    sprite('jn300_00', 6)	# 65849-65854
    SFX_1('bjn701brg')
    sprite('jn300_01', 6)	# 65855-65860
    sprite('jn300_02', 6)	# 65861-65866
    sprite('jn300_03', 6)	# 65867-65872
    sprite('jn300_04', 30)	# 65873-65902
    sprite('jn300_05', 8)	# 65903-65910
    sprite('jn300_06', 8)	# 65911-65918
    sprite('jn300_07', 8)	# 65919-65926
    sprite('jn300_08', 300)	# 65927-66226
    sprite('jn300_09', 6)	# 66227-66232
    sprite('jn300_10', 6)	# 66233-66238
    sprite('jn000_00', 7)	# 66239-66245
    sprite('jn000_01', 7)	# 66246-66252
    sprite('jn000_02', 7)	# 66253-66259
    sprite('jn000_03', 7)	# 66260-66266
    sprite('jn000_04', 7)	# 66267-66273
    sprite('jn000_05', 7)	# 66274-66280
    sprite('jn000_06', 7)	# 66281-66287
    sprite('jn000_07', 7)	# 66288-66294
    sprite('jn000_08', 7)	# 66295-66301
    sprite('jn000_09', 7)	# 66302-66308
    sprite('jn001_00', 8)	# 66309-66316
    if (SLOT_38 == 1):
        if (SLOT_152 == 1):
            Unknown2005()
            Unknown2037(1)
    if (SLOT_38 == 0):
        if (SLOT_152 == 0):
            Unknown2005()
            Unknown2037(1)
    sprite('jn001_01', 8)	# 66317-66324
    sprite('jn001_02', 10)	# 66325-66334
    sprite('jn001_03', 8)	# 66335-66342
    sprite('jn001_04', 8)	# 66343-66350
    sprite('jn001_05', 8)	# 66351-66358
    sprite('jn001_06', 10)	# 66359-66368
    sprite('jn001_07', 8)	# 66369-66376
    sprite('jn001_08', 8)	# 66377-66384
    sprite('jn001_09', 8)	# 66385-66392
    sprite('jn032_12', 3)	# 66393-66395
    Unknown2005()
    physicsXImpulse(8000)
    Unknown2053(0)
    Unknown2034(0)
    sprite('jn032_00', 4)	# 66396-66399
    sprite('jn032_01', 4)	# 66400-66403
    physicsXImpulse(28000)
    Unknown21011(180)
    label(101)
    sprite('jn032_02', 4)	# 66404-66407

    def upon_3():
        if (SLOT_145 <= 500000):
            clearUponHandler(3)
            Unknown1084(1)
            sendToLabel(102)
    sprite('jn032_03', 4)	# 66408-66411
    sprite('jn032_04', 4)	# 66412-66415
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 66416-66419
    sprite('jn032_06', 4)	# 66420-66423
    sprite('jn032_07', 4)	# 66424-66427
    sprite('jn032_08', 4)	# 66428-66431
    sprite('jn032_09', 4)	# 66432-66435
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 66436-66439
    gotoLabel(101)
    label(102)
    sprite('jn000_00', 7)	# 66440-66446
    sprite('jn000_01', 7)	# 66447-66453
    sprite('jn000_02', 7)	# 66454-66460
    sprite('jn000_03', 7)	# 66461-66467
    sprite('jn000_04', 7)	# 66468-66474
    sprite('jn000_05', 7)	# 66475-66481
    sprite('jn000_06', 7)	# 66482-66488
    sprite('jn000_07', 7)	# 66489-66495
    sprite('jn000_08', 7)	# 66496-66502
    sprite('jn000_09', 7)	# 66503-66509
    gotoLabel(102)
    label(110)
    sprite('jn000_00', 1)	# 66510-66510

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('jn000_00', 7)	# 66511-66517
    sprite('jn000_01', 7)	# 66518-66524
    sprite('jn000_02', 7)	# 66525-66531
    sprite('jn000_03', 7)	# 66532-66538
    sprite('jn000_04', 7)	# 66539-66545
    sprite('jn000_05', 7)	# 66546-66552
    sprite('jn000_06', 7)	# 66553-66559
    sprite('jn000_07', 7)	# 66560-66566
    sprite('jn000_08', 7)	# 66567-66573
    sprite('jn000_09', 7)	# 66574-66580
    gotoLabel(111)
    label(112)
    sprite('jn610_00', 5)	# 66581-66585
    sprite('jn610_01', 5)	# 66586-66590
    sprite('jn610_02', 5)	# 66591-66595
    sprite('jn610_03', 5)	# 66596-66600
    sprite('jn610_04', 5)	# 66601-66605
    sprite('jn610_05', 5)	# 66606-66610
    sprite('jn610_06', 5)	# 66611-66615
    sprite('jn610_07', 5)	# 66616-66620
    sprite('jn610_08', 1)	# 66621-66621
    SFX_1('bjn701bno')
    label(113)
    sprite('jn610_08', 1)	# 66622-66622
    if SLOT_97:
        _gotolabel(113)
    sprite('jn610_08', 20)	# 66623-66642
    sprite('jn610_08', 32767)	# 66643-99409
    Unknown21007(24, 40)
    Unknown21011(180)
    label(120)
    sprite('jn610_00', 5)	# 99410-99414
    sprite('jn610_01', 5)	# 99415-99419
    sprite('jn610_02', 5)	# 99420-99424
    sprite('jn610_03', 5)	# 99425-99429
    sprite('jn610_04', 5)	# 99430-99434
    sprite('jn610_05', 5)	# 99435-99439
    sprite('jn610_06', 5)	# 99440-99444
    sprite('jn610_07', 5)	# 99445-99449
    sprite('jn610_08', 1)	# 99450-99450
    SFX_1('bjn700pyo')
    label(121)
    sprite('jn610_08', 1)	# 99451-99451
    if SLOT_97:
        _gotolabel(121)
    sprite('jn610_08', 32767)	# 99452-132218
    Unknown21007(24, 40)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bjn702pyo')
        Unknown23018(1)
    label(130)
    sprite('jn000_00', 1)	# 132219-132219

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('jn000_00', 7)	# 132220-132226
    sprite('jn000_01', 7)	# 132227-132233
    sprite('jn000_02', 7)	# 132234-132240
    sprite('jn000_03', 7)	# 132241-132247
    sprite('jn000_04', 7)	# 132248-132254
    sprite('jn000_05', 7)	# 132255-132261
    sprite('jn000_06', 7)	# 132262-132268
    sprite('jn000_07', 7)	# 132269-132275
    sprite('jn000_08', 7)	# 132276-132282
    sprite('jn000_09', 7)	# 132283-132289
    gotoLabel(131)
    label(132)
    sprite('jn611_00', 5)	# 132290-132294
    sprite('jn611_01', 5)	# 132295-132299
    SFX_1('bjn701bjb')
    sprite('jn611_02', 5)	# 132300-132304
    sprite('jn611_03', 5)	# 132305-132309
    sprite('jn611_04', 5)	# 132310-132314
    sprite('jn611_05', 5)	# 132315-132319
    GFX_0('jnef611icewing', 0)
    SFX_3('jnse_02')
    sprite('jn611_06', 5)	# 132320-132324
    sprite('jn611_07', 5)	# 132325-132329
    sprite('jn611_08', 5)	# 132330-132334
    sprite('jn611_09', 5)	# 132335-132339
    sprite('jn611_10', 5)	# 132340-132344
    sprite('jn611_11', 5)	# 132345-132349
    sprite('jn611_12', 5)	# 132350-132354
    Unknown23018(1)
    sprite('jn611_13', 32767)	# 132355-165121
    label(140)
    sprite('jn611_00', 5)	# 165122-165126
    sprite('jn611_01', 5)	# 165127-165131
    SFX_1('bjn700rbl')
    sprite('jn611_02', 5)	# 165132-165136
    sprite('jn611_03', 5)	# 165137-165141
    sprite('jn611_04', 5)	# 165142-165146
    sprite('jn611_05', 5)	# 165147-165151
    GFX_0('jnef611icewing', 0)
    SFX_3('jnse_02')
    sprite('jn611_06', 5)	# 165152-165156
    sprite('jn611_07', 5)	# 165157-165161
    sprite('jn611_08', 5)	# 165162-165166
    sprite('jn611_09', 5)	# 165167-165171
    sprite('jn611_10', 5)	# 165172-165176
    sprite('jn611_11', 5)	# 165177-165181
    sprite('jn611_12', 5)	# 165182-165186
    label(141)
    sprite('jn611_13', 1)	# 165187-165187
    if SLOT_97:
        _gotolabel(141)
    sprite('jn611_13', 30)	# 165188-165217
    sprite('jn611_13', 32767)	# 165218-197984
    Unknown21007(24, 40)
    Unknown21011(200)
    label(150)
    sprite('jn000_00', 1)	# 197985-197985

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('jn000_00', 7)	# 197986-197992
    sprite('jn000_01', 7)	# 197993-197999
    sprite('jn000_02', 7)	# 198000-198006
    sprite('jn000_03', 7)	# 198007-198013
    sprite('jn000_04', 7)	# 198014-198020
    sprite('jn000_05', 7)	# 198021-198027
    sprite('jn000_06', 7)	# 198028-198034
    sprite('jn000_07', 7)	# 198035-198041
    sprite('jn000_08', 7)	# 198042-198048
    sprite('jn000_09', 7)	# 198049-198055
    gotoLabel(151)
    label(152)
    sprite('jn610_00', 5)	# 198056-198060
    sprite('jn610_01', 5)	# 198061-198065
    sprite('jn610_02', 5)	# 198066-198070
    sprite('jn610_03', 5)	# 198071-198075
    sprite('jn610_04', 5)	# 198076-198080
    sprite('jn610_05', 5)	# 198081-198085
    sprite('jn610_06', 5)	# 198086-198090
    sprite('jn610_07', 5)	# 198091-198095
    sprite('jn610_08', 1)	# 198096-198096
    SFX_1('bjn701uor')
    label(153)
    sprite('jn610_08', 1)	# 198097-198097
    if SLOT_97:
        _gotolabel(153)
    sprite('jn610_08', 32767)	# 198098-230864
    Unknown23018(1)
    label(160)
    sprite('jn000_00', 1)	# 230865-230865

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('jn000_00', 7)	# 230866-230872
    sprite('jn000_01', 7)	# 230873-230879
    sprite('jn000_02', 7)	# 230880-230886
    sprite('jn000_03', 7)	# 230887-230893
    sprite('jn000_04', 7)	# 230894-230900
    sprite('jn000_05', 7)	# 230901-230907
    sprite('jn000_06', 7)	# 230908-230914
    sprite('jn000_07', 7)	# 230915-230921
    sprite('jn000_08', 7)	# 230922-230928
    sprite('jn000_09', 7)	# 230929-230935
    gotoLabel(161)
    label(162)
    sprite('jn611_00', 5)	# 230936-230940
    sprite('jn611_01', 5)	# 230941-230945
    SFX_1('bjn701uyu')
    sprite('jn611_02', 5)	# 230946-230950
    sprite('jn611_03', 5)	# 230951-230955
    sprite('jn611_04', 5)	# 230956-230960
    sprite('jn611_05', 5)	# 230961-230965
    GFX_0('jnef611icewing', 0)
    SFX_3('jnse_02')
    sprite('jn611_06', 5)	# 230966-230970
    sprite('jn611_07', 5)	# 230971-230975
    sprite('jn611_08', 5)	# 230976-230980
    sprite('jn611_09', 5)	# 230981-230985
    sprite('jn611_10', 5)	# 230986-230990
    sprite('jn611_11', 5)	# 230991-230995
    sprite('jn611_12', 5)	# 230996-231000
    Unknown23018(1)
    sprite('jn611_13', 32767)	# 231001-263767
    label(170)
    sprite('jn000_00', 1)	# 263768-263768

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('jn000_00', 7)	# 263769-263775
    sprite('jn000_01', 7)	# 263776-263782
    sprite('jn000_02', 7)	# 263783-263789
    sprite('jn000_03', 7)	# 263790-263796
    sprite('jn000_04', 7)	# 263797-263803
    sprite('jn000_05', 7)	# 263804-263810
    sprite('jn000_06', 7)	# 263811-263817
    sprite('jn000_07', 7)	# 263818-263824
    sprite('jn000_08', 7)	# 263825-263831
    sprite('jn000_09', 7)	# 263832-263838
    gotoLabel(171)
    label(172)
    sprite('jn611_00', 5)	# 263839-263843
    sprite('jn611_01', 5)	# 263844-263848
    SFX_1('bjn701pmi')
    sprite('jn611_02', 5)	# 263849-263853
    sprite('jn611_03', 5)	# 263854-263858
    sprite('jn611_04', 5)	# 263859-263863
    sprite('jn611_05', 5)	# 263864-263868
    GFX_0('jnef611icewing', 0)
    SFX_3('jnse_02')
    sprite('jn611_06', 5)	# 263869-263873
    sprite('jn611_07', 5)	# 263874-263878
    sprite('jn611_08', 5)	# 263879-263883
    sprite('jn611_09', 5)	# 263884-263888
    sprite('jn611_10', 5)	# 263889-263893
    sprite('jn611_11', 5)	# 263894-263898
    sprite('jn611_12', 5)	# 263899-263903
    Unknown23018(1)
    sprite('jn611_13', 32767)	# 263904-296670
    label(180)
    sprite('jn610_00', 5)	# 296671-296675
    sprite('jn610_01', 5)	# 296676-296680
    sprite('jn610_02', 5)	# 296681-296685
    sprite('jn610_03', 5)	# 296686-296690
    sprite('jn610_04', 5)	# 296691-296695
    sprite('jn610_05', 5)	# 296696-296700
    sprite('jn610_06', 5)	# 296701-296705
    sprite('jn610_07', 5)	# 296706-296710
    sprite('jn610_08', 1)	# 296711-296711
    SFX_1('bjn700bma')
    label(181)
    sprite('jn610_08', 1)	# 296712-296712
    if SLOT_97:
        _gotolabel(181)
    sprite('jn610_08', 32767)	# 296713-329479
    Unknown21007(24, 40)
    Unknown21011(260)
    label(190)
    sprite('jn610_00', 5)	# 329480-329484
    sprite('jn610_01', 5)	# 329485-329489
    sprite('jn610_02', 5)	# 329490-329494
    sprite('jn610_03', 5)	# 329495-329499
    sprite('jn610_04', 5)	# 329500-329504
    sprite('jn610_05', 5)	# 329505-329509
    sprite('jn610_06', 5)	# 329510-329514
    sprite('jn610_07', 5)	# 329515-329519
    sprite('jn610_08', 1)	# 329520-329520
    SFX_1('bjn700biz')
    label(191)
    sprite('jn610_08', 1)	# 329521-329521
    if SLOT_97:
        _gotolabel(191)
    sprite('jn610_08', 32767)	# 329522-362288
    Unknown21007(24, 40)
    Unknown21011(120)

@State
def CmnActLose():
    sprite('jn620_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('bjn403_0', 100, 879651426, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jn620_01', 6)	# 7-12
    sprite('jn620_02', 6)	# 13-18
    sprite('jn620_03', 6)	# 19-24
    sprite('jn620_04', 6)	# 25-30
    sprite('jn620_05', 6)	# 31-36
    sprite('jn620_06', 6)	# 37-42
    sprite('jn620_07', 6)	# 43-48
    sprite('jn620_08', 32767)	# 49-32815
    Unknown23018(1)
    loopRest()

@State
def EventDefEntryWait():
    label(0)
    sprite('jn000_00', 7)	# 1-7
    sprite('jn000_01', 7)	# 8-14
    sprite('jn000_02', 7)	# 15-21
    sprite('jn000_03', 7)	# 22-28
    sprite('jn000_04', 7)	# 29-35
    sprite('jn000_05', 7)	# 36-42
    sprite('jn000_06', 7)	# 43-49
    sprite('jn000_07', 7)	# 50-56
    sprite('jn000_08', 7)	# 57-63
    sprite('jn000_09', 7)	# 64-70
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
    sprite('jn620_08', 32767)	# 1-32767

@State
def EventDefLose01():
    sprite('jn620_08', 7)	# 1-7
    sprite('jn064_03', 7)	# 8-14
    sprite('jn064_02', 7)	# 15-21
    sprite('jn064_01', 7)	# 22-28
    sprite('jn064_00', 7)	# 29-35
    sprite('jn063_09', 32767)	# 36-32802

@State
def EventEntryRunWait():
    sprite('null', 32767)	# 1-32767
    teleportRelativeX(-700000)
    Unknown2034(0)

@State
def EventEntryRun():
    sprite('jn032_00', 4)	# 1-4
    Unknown2034(0)
    Unknown8006(100, 1, 1)
    physicsXImpulse(15000)
    sprite('jn032_01', 4)	# 5-8
    sprite('jn032_02', 4)	# 9-12
    sprite('jn032_03', 4)	# 13-16
    sprite('jn032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 21-24
    sprite('jn032_06', 4)	# 25-28
    sprite('jn032_07', 4)	# 29-32
    sprite('jn032_08', 4)	# 33-36
    sprite('jn032_09', 4)	# 37-40
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 41-44
    Unknown1019(90)
    sprite('jn032_11', 4)	# 45-48
    sprite('jn032_12', 4)	# 49-52
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('jn000_00', 1)	# 53-53
    enterState('CmnActStand')

@State
def EventChouhatsu():
    sprite('jn300_00', 6)	# 1-6
    sprite('jn300_01', 6)	# 7-12
    sprite('jn300_02', 6)	# 13-18
    sprite('jn300_03', 6)	# 19-24
    sprite('jn300_04', 32767)	# 25-32791

@State
def EventChouhatsuEnd():
    sprite('jn300_04', 6)	# 1-6
    sprite('jn300_05', 6)	# 7-12
    sprite('jn300_06', 6)	# 13-18
    sprite('jn300_07', 6)	# 19-24
    sprite('jn300_08', 6)	# 25-30
    sprite('jn300_09', 6)	# 31-36
    sprite('jn300_10', 6)	# 37-42
    sprite('jn000_00', 1)	# 43-43
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    loopRest()

@State
def EventYoroke():
    sprite('jn070_00', 4)	# 1-4
    sprite('jn070_01', 4)	# 5-8
    sprite('jn070_02', 4)	# 9-12
    sprite('jn070_03', 32767)	# 13-32779
    loopRest()

@State
def EventAZYorokeLoop():
    sprite('jn070_03', 32767)	# 1-32767

@State
def EventAZYoroke2Down():
    sprite('jn070_03', 2)	# 1-2
    sprite('jn070_08', 6)	# 3-8
    sprite('jn070_09', 6)	# 9-14
    sprite('jn070_10', 6)	# 15-20
    sprite('jn070_11', 6)	# 21-26
    sprite('jn064_03', 6)	# 27-32
    sprite('jn064_02', 6)	# 33-38
    sprite('jn064_01', 6)	# 39-44
    sprite('jn063_09', 32767)	# 45-32811
    loopRest()

@State
def EventAZDown():
    sprite('jn061_00', 32767)	# 1-32767

@State
def EventAZDownToStand():
    sprite('jn061_00', 6)	# 1-6
    sprite('jn061_01', 6)	# 7-12
    sprite('jn061_02', 6)	# 13-18
    sprite('jn061_03', 6)	# 19-24
    sprite('jn061_04', 6)	# 25-30
    sprite('jn061_05', 6)	# 31-36
    sprite('jn061_06', 6)	# 37-42
    sprite('jn061_07', 6)	# 43-48
    sprite('jn061_08', 6)	# 49-54
    Unknown2005()
    sprite('jn620_00', 6)	# 55-60
    sprite('jn620_01', 6)	# 61-66
    sprite('jn620_02', 6)	# 67-72
    sprite('jn620_03', 6)	# 73-78
    sprite('jn620_04', 6)	# 79-84
    sprite('jn620_05', 6)	# 85-90
    sprite('jn620_06', 6)	# 91-96
    sprite('jn620_07', 6)	# 97-102
    sprite('jn620_08', 32767)	# 103-32869

@State
def EventVSAM1():
    sprite('jn430_26', 4)	# 1-4
    sprite('jn430_25', 4)	# 5-8
    sprite('jn430_24', 5)	# 9-13
    sprite('jn430_23', 32767)	# 14-32780
    GFX_0('EffNoutou', 0)

@State
def EventVSAM2():
    sprite('jn430_23', 5)	# 1-5
    sprite('jn430_24', 6)	# 6-11
    sprite('jn430_25', 6)	# 12-17
    sprite('jn430_26', 6)	# 18-23
    sprite('jn000_00', 1)	# 24-24
    enterState('CmnActStand')

@State
def EventVSRG1():
    setInvincible(1)
    AttackDefaults_StandingNormal()
    sprite('jn202_00', 2)	# 1-2
    sprite('jn202_01', 2)	# 3-4
    sprite('jn202_02', 2)	# 5-6
    sprite('jn202_03', 3)	# 7-9
    sprite('jn202_04', 2)	# 10-11	 **attackbox here**
    GFX_0('zan_b0', -1)
    SFX_0('009_swing_rapier_1')
    sprite('jn202_05', 2)	# 12-13	 **attackbox here**
    sprite('jn202_05', 12)	# 14-25	 **attackbox here**
    StartMultihit()
    sprite('jn202_06', 2)	# 26-27
    sprite('jn202_08', 3)	# 28-30
    sprite('jn202_09', 3)	# 31-33
    sprite('jn202_10', 2)	# 34-35
    sprite('jn202_11', 1)	# 36-36
    sprite('jn202_12', 1)	# 37-37
    sprite('jn202_14', 1)	# 38-38
    GFX_0('EffNoutou', 0)
    sprite('jn202_16', 1)	# 39-39
    sprite('jn000_00', 1)	# 40-40
    enterState('CmnActStand')

@State
def EventVSTB1():
    sprite('jn300_04', 32767)	# 1-32767

@State
def EventVSTB2():
    sprite('jn300_04', 8)	# 1-8
    sprite('jn300_05', 6)	# 9-14
    sprite('jn300_06', 6)	# 15-20
    sprite('jn300_07', 6)	# 21-26
    sprite('jn300_08', 6)	# 27-32
    sprite('jn300_09', 6)	# 33-38
    sprite('jn300_10', 6)	# 39-44
    sprite('jn000_00', 1)	# 45-45
    enterState('CmnActStand')

@State
def EventJNDamage():
    sprite('jn620_00', 5)	# 1-5
    sprite('jn620_01', 5)	# 6-10
    sprite('jn620_02', 15)	# 11-25
    sprite('jn620_01', 7)	# 26-32
    sprite('jn620_00', 7)	# 33-39
    loopRest()
    enterState('CmnActStand')

@State
def EventJNDamage2():
    sprite('jn620_00', 5)	# 1-5
    sprite('jn620_01', 5)	# 6-10
    sprite('jn620_02', 30)	# 11-40
    sprite('jn300_00', 6)	# 41-46
    sprite('jn300_01', 6)	# 47-52
    sprite('jn300_02', 6)	# 53-58
    sprite('jn300_03', 6)	# 59-64
    sprite('jn300_04', 100)	# 65-164
    sprite('jn300_05', 8)	# 165-172
    sprite('jn300_06', 8)	# 173-180
    sprite('jn300_07', 6)	# 181-186
    sprite('jn300_08', 6)	# 187-192
    sprite('jn300_09', 8)	# 193-200
    sprite('jn300_10', 8)	# 201-208
    loopRest()
    enterState('CmnActStand')

@State
def EventJNvsHZWin():
    sprite('jn033_00', 2)	# 1-2
    Unknown2034(0)
    sprite('jn033_01', 3)	# 3-5
    physicsXImpulse(-48000)
    physicsYImpulse(30000)
    setGravity(1550)
    Unknown8002()
    SFX_0('000_airdash_2')
    sprite('jn033_02', 3)	# 6-8
    sprite('jn033_03', 3)	# 9-11
    sprite('jn033_04', 3)	# 12-14
    sprite('jn033_05', 2)	# 15-16
    sprite('jn033_06', 1)	# 17-17
    sprite('jn033_07', 1)	# 18-18
    sprite('jn033_08', 1)	# 19-19
    sprite('null', 1)	# 20-20

@State
def EventJNYoroke():
    sprite('jn620_00', 5)	# 1-5
    sprite('jn620_01', 5)	# 6-10
    sprite('jn620_02', 5)	# 11-15
    sprite('jn620_03', 5)	# 16-20
    sprite('jn620_04', 5)	# 21-25
    sprite('jn620_05', 5)	# 26-30
    sprite('jn620_06', 5)	# 31-35
    sprite('jn620_07', 5)	# 36-40
    sprite('jn620_08', 32767)	# 41-32807

@State
def EventJNYorokeReverse():
    sprite('jn620_08', 8)	# 1-8
    sprite('jn620_07', 8)	# 9-16
    sprite('jn620_06', 8)	# 17-24
    sprite('jn620_05', 8)	# 25-32
    sprite('jn620_04', 12)	# 33-44
    sprite('jn620_03', 4)	# 45-48
    sprite('jn620_02', 4)	# 49-52
    sprite('jn620_01', 4)	# 53-56
    sprite('jn620_00', 3)	# 57-59
    enterState('CmnActStand')

@State
def EventJNvsNOEntry02():
    label(0)
    sprite('jn000_00', 7)	# 1-7
    sprite('jn000_01', 7)	# 8-14
    sprite('jn000_02', 7)	# 15-21
    sprite('jn000_03', 7)	# 22-28
    sprite('jn000_04', 7)	# 29-35
    sprite('jn000_05', 7)	# 36-42
    sprite('jn000_06', 7)	# 43-49
    sprite('jn000_07', 7)	# 50-56
    sprite('jn000_08', 7)	# 57-63
    sprite('jn000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def EventJNTimeupLoop():
    sprite('jn620_08', 32767)	# 1-32767

@State
def EventJNvsNOWin01():
    Unknown2017(0)
    Unknown2034(0)
    sprite('jn620_08', 6)	# 1-6
    sprite('jn620_07', 6)	# 7-12
    sprite('jn620_06', 6)	# 13-18
    sprite('jn620_05', 6)	# 19-24
    sprite('jn620_04', 6)	# 25-30
    sprite('jn620_03', 6)	# 31-36
    sprite('jn620_02', 6)	# 37-42
    sprite('jn620_01', 6)	# 43-48
    sprite('jn620_00', 6)	# 49-54
    loopRest()
    sprite('jn032_00', 4)	# 55-58
    physicsXImpulse(24000)
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 59-62
    sprite('jn032_02', 4)	# 63-66
    sprite('jn032_03', 4)	# 67-70
    sprite('jn032_04', 4)	# 71-74
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 75-78
    sprite('jn032_06', 4)	# 79-82
    sprite('jn032_07', 4)	# 83-86
    sprite('jn032_08', 4)	# 87-90
    sprite('jn032_09', 4)	# 91-94
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 95-98
    sprite('jn032_00', 4)	# 99-102
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 103-106
    sprite('jn032_02', 4)	# 107-110
    sprite('jn032_03', 4)	# 111-114
    sprite('jn032_04', 4)	# 115-118
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 119-122
    sprite('jn032_06', 4)	# 123-126
    sprite('jn032_07', 4)	# 127-130
    sprite('jn032_08', 4)	# 131-134
    sprite('jn032_09', 4)	# 135-138
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 139-142

@State
def EventKubifuri():
    sprite('jn300_00', 6)	# 1-6
    sprite('jn300_01', 6)	# 7-12
    sprite('jn300_02', 6)	# 13-18
    sprite('jn300_03', 6)	# 19-24
    sprite('jn300_04', 60)	# 25-84
    sprite('jn300_05', 6)	# 85-90
    sprite('jn300_06', 6)	# 91-96
    sprite('jn300_07', 6)	# 97-102
    sprite('jn300_08', 6)	# 103-108
    sprite('jn300_09', 6)	# 109-114
    sprite('jn300_10', 6)	# 115-120
    enterState('CmnActStand')

@State
def EventKubifuriShort():
    sprite('jn300_00', 6)	# 1-6
    sprite('jn300_01', 6)	# 7-12
    sprite('jn300_02', 6)	# 13-18
    sprite('jn300_03', 6)	# 19-24
    sprite('jn300_04', 10)	# 25-34
    sprite('jn300_05', 6)	# 35-40
    sprite('jn300_06', 6)	# 41-46
    sprite('jn300_07', 6)	# 47-52
    sprite('jn300_08', 6)	# 53-58
    sprite('jn300_09', 6)	# 59-64
    sprite('jn300_10', 6)	# 65-70
    enterState('CmnActStand')

@State
def EventJNYorokeSummon():
    sprite('jn620_08', 32767)	# 1-32767
    GFX_0('jnef600iceSword', -1)
    Unknown38(5, 1)

@State
def EventJNYorokeDelObj():
    sprite('jn620_08', 32767)	# 1-32767
    Unknown13(5)

@State
def EventHazamaAttack():
    sprite('jn000_00', 7)	# 1-7
    GFX_0('EventEffSpKensei', -1)
    sprite('jn000_01', 5)	# 8-12
    sprite('jn000_01ex01', 2)	# 13-14
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a0000000000000000000000000000000000000000000000006c000000')
    SFX_0('101_hit_slash_2')
    sprite('jn000_02', 7)	# 15-21
    sprite('jn000_03', 7)	# 22-28
    sprite('jn000_04', 7)	# 29-35
    sprite('jn000_05', 7)	# 36-42
    sprite('jn000_06', 7)	# 43-49
    sprite('jn000_07', 7)	# 50-56
    sprite('jn000_08', 7)	# 57-63
    sprite('jn000_09', 7)	# 64-70
    loopRest()
    enterState('CmnActStand')

@State
def EventRGAntiAirEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Hitstop(8)
        Unknown9016(1)
        setInvincible(1)
    sprite('jn000_00', 7)	# 1-7
    sprite('jn407_00', 3)	# 8-10
    sprite('jn407_01', 3)	# 11-13
    sprite('jn407_02', 3)	# 14-16
    sprite('jn407_03', 3)	# 17-19
    sprite('jn407_04', 3)	# 20-22	 **attackbox here**
    SFX_3('jnse_21')
    GFX_0('zan407', 0)
    SFX_0('009_swing_rapier_0')
    sprite('jn407_05', 3)	# 23-25
    sprite('jn407_06', 3)	# 26-28
    sprite('jn407_07', 3)	# 29-31
    sprite('jn407_08', 3)	# 32-34
    sprite('jn407_26', 10)	# 35-44
    sprite('jn407_09', 2)	# 45-46
    sprite('jn407_10', 3)	# 47-49
    sprite('jn407_11', 3)	# 50-52
    SFX_3('jnse_21')
    GFX_0('EFF28AtkD', 0)
    sprite('jn407_12ex', 3)	# 53-55	 **attackbox here**
    RefreshMultihit()
    Hitstop(20)
    SFX_0('010_swing_sword_0')
    sprite('jn407_13ex', 3)	# 56-58
    sprite('jn407_14', 3)	# 59-61
    sprite('jn407_15', 3)	# 62-64
    sprite('jn407_16', 3)	# 65-67
    sprite('jn407_17', 3)	# 68-70
    sprite('jn407_18', 3)	# 71-73
    sprite('jn407_19', 3)	# 74-76
    sprite('jn407_20', 3)	# 77-79
    sprite('jn407_21', 5)	# 80-84
    sprite('jn407_22', 4)	# 85-88
    sprite('jn407_23', 3)	# 89-91
    sprite('jn407_24', 3)	# 92-94
    GFX_0('EffNoutou', 0)
    sprite('jn407_25', 3)	# 95-97
    Unknown1000(-260000)
    loopRest()

@State
def EventRGWin1():
    sprite('jn610_00', 5)	# 1-5
    sprite('jn610_01', 5)	# 6-10
    sprite('jn610_02', 5)	# 11-15
    sprite('jn610_03', 5)	# 16-20
    sprite('jn610_04', 5)	# 21-25
    sprite('jn610_05', 5)	# 26-30
    sprite('jn610_06', 5)	# 31-35
    sprite('jn610_07', 5)	# 36-40
    sprite('jn610_08', 5)	# 41-45
    loopRest()

@State
def EventRGYorokeLoop():
    sprite('jn070_02', 32767)	# 1-32767

@State
def EventRGYoroke2Down():
    sprite('jn070_03', 2)	# 1-2
    sprite('jn070_08', 6)	# 3-8
    sprite('jn070_09', 6)	# 9-14
    sprite('jn070_10', 6)	# 15-20
    sprite('jn070_11', 6)	# 21-26
    sprite('jn064_03', 6)	# 27-32
    sprite('jn064_02', 6)	# 33-38
    sprite('jn064_01', 6)	# 39-44
    sprite('jn063_09', 32767)	# 45-32811
    loopRest()

@State
def EventJNReAction():
    sprite('jn001_00', 8)	# 1-8
    sprite('jn001_01', 8)	# 9-16
    sprite('jn001_02', 10)	# 17-26
    sprite('jn001_03', 8)	# 27-34
    sprite('jn001_04', 8)	# 35-42
    sprite('jn001_05', 8)	# 43-50
    sprite('jn001_06', 10)	# 51-60
    sprite('jn001_07', 8)	# 61-68
    sprite('jn001_08', 8)	# 69-76
    sprite('jn001_09', 8)	# 77-84
    enterState('CmnActStand')

@State
def EventJNVsRCDownLoop():
    sprite('jn063_09', 32767)	# 1-32767
    Unknown1000(-40000)
    loopRest()

@State
def EventTBDown01():
    sprite('jn061_00', 32767)	# 1-32767
    Unknown1000(-50000)

@State
def EventMUYoroke():
    sprite('jn620_00', 5)	# 1-5
    sprite('jn620_01', 5)	# 6-10
    sprite('jn620_02', 5)	# 11-15
    sprite('jn620_03', 5)	# 16-20
    sprite('jn620_04', 5)	# 21-25
    sprite('jn620_05', 5)	# 26-30
    sprite('jn620_06', 5)	# 31-35
    sprite('jn620_07', 5)	# 36-40
    sprite('jn620_08', 32767)	# 41-32807

@State
def EventMUUdekumiloop():
    label(0)
    sprite('jn600_00', 6)	# 1-6
    sprite('jn600_01', 6)	# 7-12
    sprite('jn600_02', 6)	# 13-18
    sprite('jn600_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def EventMUSummonSword():
    sprite('jn600_00', 6)	# 1-6
    GFX_0('jnef600iceSword', -1)
    Unknown38(4, 1)
    sprite('jn600_01', 6)	# 7-12
    sprite('jn600_02', 6)	# 13-18
    sprite('jn600_03', 6)	# 19-24
    sprite('jn600_00', 6)	# 25-30
    sprite('jn600_01', 6)	# 31-36
    sprite('jn600_02', 6)	# 37-42
    sprite('jn600_03', 6)	# 43-48
    sprite('jn600_00', 6)	# 49-54
    sprite('jn600_01', 6)	# 55-60
    sprite('jn600_02', 6)	# 61-66
    sprite('jn600_03', 6)	# 67-72
    sprite('jn600_04', 6)	# 73-78
    sprite('jn600_05', 6)	# 79-84
    sprite('jn600_06', 6)	# 85-90
    sprite('jn600_07', 6)	# 91-96
    sprite('jn600_08', 6)	# 97-102
    sprite('jn600_09', 6)	# 103-108
    sprite('jn600_10', 6)	# 109-114
    sprite('jn600_11', 6)	# 115-120
    Unknown36(4)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 121-126
    sprite('jn600_13', 6)	# 127-132
    sprite('jn600_14', 6)	# 133-138
    sprite('jn600_15', 6)	# 139-144
    sprite('jn600_16', 6)	# 145-150
    sprite('jn600_17', 6)	# 151-156
    sprite('jn600_18', 6)	# 157-162
    sprite('jn000_00', 1)	# 163-163
    enterState('CmnActStand')

@State
def EventHZVsJN_Dash5C():
    Unknown2034(0)
    Unknown1000(-1350000)
    Unknown3038(0)

    def upon_3():
        if (SLOT_29 < 700000):
            sendToLabel(1)
    sprite('jn032_00', 4)	# 1-4
    SFX_0('000_airdash_0')
    physicsXImpulse(10000)
    Unknown1028(1000)
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 5-8
    label(0)
    sprite('jn032_02', 4)	# 9-12
    sprite('jn032_03', 4)	# 13-16
    sprite('jn032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 21-24
    sprite('jn032_06', 4)	# 25-28
    sprite('jn032_07', 4)	# 29-32
    sprite('jn032_08', 4)	# 33-36
    sprite('jn032_09', 4)	# 37-40
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 41-44
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('jn032_11', 2)	# 45-46
    Unknown21007(22, 32)
    Unknown1028(0)
    Unknown1019(60)
    sprite('jn032_11', 2)	# 47-48
    sprite('jn032_12', 2)	# 49-50
    Unknown1019(60)
    sprite('jn202_03', 3)	# 51-53
    sprite('jn202_04', 2)	# 54-55	 **attackbox here**
    GFX_0('zan_b0', -1)
    SFX_0('009_swing_rapier_1')
    Unknown1019(60)
    sprite('jn202_05', 2)	# 56-57	 **attackbox here**
    sprite('jn202_05', 5)	# 58-62	 **attackbox here**
    StartMultihit()
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('jn202_06', 4)	# 63-66
    sprite('jn202_07', 3)	# 67-69
    sprite('jn202_08', 4)	# 70-73
    sprite('jn202_09', 4)	# 74-77
    sprite('jn202_10', 3)	# 78-80
    sprite('jn202_11', 3)	# 81-83
    sprite('jn202_12', 3)	# 84-86
    sprite('jn202_13', 2)	# 87-88
    sprite('jn202_14', 2)	# 89-90
    GFX_0('EffNoutou', 0)
    sprite('jn202_15', 2)	# 91-92
    sprite('jn202_16', 2)	# 93-94
    enterState('CmnActStand')

@State
def EventGuardUe():
    sprite('jn040_00', 6)	# 1-6
    sprite('jn040_01', 6)	# 7-12
    label(0)
    sprite('jn040_02', 6)	# 13-18
    sprite('jn040_03', 6)	# 19-24
    sprite('jn040_04', 6)	# 25-30
    gotoLabel(0)

@State
def EventGuardUeEnd():
    sprite('jn040_00', 6)	# 1-6
    sprite('jn040_01', 6)	# 7-12
    enterState('CmnActStand')

@State
def EventWin2():
    sprite('jn611_00', 5)	# 1-5
    sprite('jn611_01', 5)	# 6-10
    sprite('jn611_02', 5)	# 11-15
    sprite('jn611_03', 5)	# 16-20
    sprite('jn611_04', 5)	# 21-25
    sprite('jn611_05', 5)	# 26-30
    GFX_0('jnef611icewing', 0)
    SFX_3('jnse_02')
    sprite('jn611_06', 5)	# 31-35
    sprite('jn611_07', 5)	# 36-40
    sprite('jn611_08', 5)	# 41-45
    sprite('jn611_09', 5)	# 46-50
    sprite('jn611_10', 5)	# 51-55
    sprite('jn611_11', 5)	# 56-60
    sprite('jn611_12', 5)	# 61-65
    sprite('jn611_13', 60)	# 66-125
    sprite('jn611_13', 5)	# 126-130
    sprite('jn611_13', 32767)	# 131-32897
    loopRest()

@State
def EventTBDown02():
    sprite('jn620_08', 30)	# 1-30
    Unknown4049(1200)
    GFX_0('EventTBHitEff', 0)
    Unknown38(4, 1)
    Unknown36(4)
    Unknown2019(-4000)
    Unknown35()
    sprite('jn620_08', 32767)	# 31-32797

@State
def EventJNYorokeEnd():
    sprite('jn620_08', 5)	# 1-5
    sprite('jn620_07', 5)	# 6-10
    sprite('jn620_06', 5)	# 11-15
    sprite('jn620_05', 5)	# 16-20
    sprite('jn620_04', 5)	# 21-25
    sprite('jn620_03', 5)	# 26-30
    loopRest()
    enterState('CmnActStand')

@State
def EventDashLeaveOpposite():
    sprite('jn032_00', 4)	# 1-4
    Unknown2034(0)
    Unknown2017(0)
    physicsXImpulse(24000)
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 5-8
    sprite('jn032_02', 4)	# 9-12
    sprite('jn032_03', 4)	# 13-16
    sprite('jn032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 21-24
    Unknown21007(22, 32)
    sprite('jn032_06', 4)	# 25-28
    sprite('jn032_07', 4)	# 29-32
    sprite('jn032_08', 4)	# 33-36
    sprite('jn032_09', 4)	# 37-40
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 41-44
    sprite('jn032_00', 4)	# 45-48
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 49-52
    sprite('jn032_02', 4)	# 53-56
    sprite('jn032_03', 4)	# 57-60
    sprite('jn032_04', 4)	# 61-64
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 65-68
    sprite('jn032_06', 4)	# 69-72
    sprite('jn032_07', 4)	# 73-76
    sprite('jn032_08', 4)	# 77-80
    sprite('jn032_09', 4)	# 81-84
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 85-88

@State
def EventJNvsTBAction01():

    def upon_IMMEDIATE():
        Unknown1000(-100000)
    label(0)
    sprite('jn000_00', 7)	# 1-7
    sprite('jn000_01', 7)	# 8-14
    sprite('jn000_02', 7)	# 15-21
    sprite('jn000_03', 7)	# 22-28
    sprite('jn000_04', 7)	# 29-35
    sprite('jn000_05', 7)	# 36-42
    sprite('jn000_06', 7)	# 43-49
    sprite('jn000_07', 7)	# 50-56
    sprite('jn000_08', 7)	# 57-63
    sprite('jn000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def EventJNvsTBAction02():
    sprite('jn003_00', 3)	# 1-3
    sprite('jn003_01', 3)	# 4-6
    Unknown2005()
    label(1)
    sprite('jn000_00', 7)	# 7-13
    physicsXImpulse(0)
    sprite('jn000_01', 7)	# 14-20
    sprite('jn000_02', 7)	# 21-27
    sprite('jn000_03', 7)	# 28-34
    sprite('jn000_04', 7)	# 35-41
    sprite('jn000_05', 7)	# 42-48
    sprite('jn000_06', 7)	# 49-55
    sprite('jn000_07', 7)	# 56-62
    sprite('jn000_08', 7)	# 63-69
    sprite('jn000_09', 7)	# 70-76
    loopRest()
    gotoLabel(1)

@State
def EventCrouch():
    label(0)
    sprite('jn010_02', 6)	# 1-6
    sprite('jn010_03', 6)	# 7-12
    sprite('jn010_04', 6)	# 13-18
    sprite('jn010_05', 6)	# 19-24
    sprite('jn010_06', 6)	# 25-30
    sprite('jn010_07', 6)	# 31-36
    sprite('jn010_08', 6)	# 37-42
    sprite('jn010_09', 6)	# 43-48
    sprite('jn010_10', 6)	# 49-54
    sprite('jn010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def EventCrouchToStand():
    sprite('jn010_01', 4)	# 1-4
    sprite('jn010_00', 4)	# 5-8
    loopRest()
    enterState('CmnActStand')

@State
def EventSummonPtPhantom():
    sprite('keep', 2)	# 1-2
    GFX_0('ptPhantom', -1)
    Unknown36(1)
    teleportRelativeX(-50000)
    Unknown2019(-500)
    Unknown35()
    loopRest()
    enterState('CmnActStand')

@State
def EventSummonPtPhantomEnd():
    sprite('keep', 2)	# 1-2
    Unknown21012('70745068616e746f6d000000000000000000000000000000000000000000000020000000')
    enterState('CmnActStand')

@State
def EventShake():
    sprite('keep', 2)	# 1-2
    GFX_0('EventShakeObj', -1)
    loopRest()
    enterState('CmnActStand')

@State
def EventWalkFrameIn():
    Unknown2034(0)
    Unknown2037(1)
    Unknown1000(-900000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            sendToLabel(1)
    sprite('jn030_00', 6)	# 1-6
    physicsXImpulse(4650)
    label(0)
    sprite('jn030_01', 6)	# 7-12
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)	# 13-18
    sprite('jn030_03', 6)	# 19-24
    sprite('jn030_04', 6)	# 25-30
    sprite('jn030_05', 6)	# 31-36
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)	# 37-42
    sprite('jn030_07', 6)	# 43-48
    sprite('jn030_08', 6)	# 49-54
    sprite('jn030_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventUltimateShot():
    sprite('jn430_00', 1)	# 1-1
    Unknown2036(30, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    GFX_0('EMB_JN', -1)
    sprite('jn430_00', 1)	# 2-2
    sprite('jn430_01', 2)	# 3-4
    sprite('jn430_02', 2)	# 5-6
    sprite('jn430_03', 2)	# 7-8
    sprite('jn430_04', 2)	# 9-10
    sprite('jn430_05', 2)	# 11-12
    sprite('jn430_06', 2)	# 13-14
    sprite('jn430_07', 3)	# 15-17
    sprite('jn430_08', 3)	# 18-20
    sprite('jn430_09', 3)	# 21-23
    sprite('jn430_10', 3)	# 24-26
    SFX_0('009_swing_rapier_1')
    sprite('jn430_11', 3)	# 27-29
    sprite('jn430_12', 3)	# 30-32
    sprite('jn430_13', 3)	# 33-35
    sprite('jn430_14', 3)	# 36-38
    SFX_0('006_swing_blade_1')
    sprite('jn430_15', 3)	# 39-41
    GFX_0('Event_UltimateSlashShotObj', 0)
    SFX_0('000_airdash_0')
    Unknown21007(22, 32)
    sprite('jn430_16', 3)	# 42-44
    sprite('jn430_17', 3)	# 45-47
    sprite('jn430_18', 3)	# 48-50
    sprite('jn430_19', 3)	# 51-53
    sprite('jn430_20', 3)	# 54-56
    sprite('jn430_21', 3)	# 57-59
    sprite('jn430_22', 3)	# 60-62
    sprite('jn430_23', 3)	# 63-65
    GFX_0('EffNoutou', 0)
    sprite('jn430_24', 3)	# 66-68
    sprite('jn430_25', 3)	# 69-71
    sprite('jn430_26', 3)	# 72-74
    loopRest()
    enterState('CmnActStand')

@State
def EventDashLeaveOppositeReverse():
    sprite('jn032_00', 4)	# 1-4
    Unknown2034(0)
    Unknown2017(0)
    physicsXImpulse(-24000)
    Unknown8006(100, 1, 1)
    Unknown2005()
    sprite('jn032_01', 4)	# 5-8
    sprite('jn032_02', 4)	# 9-12
    sprite('jn032_03', 4)	# 13-16
    sprite('jn032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 21-24
    Unknown21007(22, 32)
    sprite('jn032_06', 4)	# 25-28
    sprite('jn032_07', 4)	# 29-32
    sprite('jn032_08', 4)	# 33-36
    sprite('jn032_09', 4)	# 37-40
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 41-44
    sprite('jn032_00', 4)	# 45-48
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 49-52
    sprite('jn032_02', 4)	# 53-56
    sprite('jn032_03', 4)	# 57-60
    sprite('jn032_04', 4)	# 61-64
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 65-68
    sprite('jn032_06', 4)	# 69-72
    sprite('jn032_07', 4)	# 73-76
    sprite('jn032_08', 4)	# 77-80
    sprite('jn032_09', 4)	# 81-84
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 85-88

@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_Entry1():
    label(0)
    sprite('jn600_00', 6)	# 1-6
    sprite('jn600_01', 6)	# 7-12
    sprite('jn600_02', 6)	# 13-18
    sprite('jn600_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Entry1End():
    sprite('keep', 2)	# 1-2
    sprite('jn600_04', 6)	# 3-8
    GFX_0('jnef600iceSword', -1)
    Unknown38(5, 1)
    sprite('jn600_05', 6)	# 9-14
    sprite('jn600_06', 6)	# 15-20
    sprite('jn600_07', 6)	# 21-26
    sprite('jn600_08', 6)	# 27-32
    sprite('jn600_09', 6)	# 33-38
    sprite('jn600_10', 6)	# 39-44
    sprite('jn600_11', 6)	# 45-50
    Unknown36(5)
    sendToLabel(1)
    Unknown35()
    sprite('jn600_12', 6)	# 51-56
    sprite('jn600_13', 6)	# 57-62
    sprite('jn600_14', 6)	# 63-68
    sprite('jn600_15', 6)	# 69-74
    sprite('jn600_16', 6)	# 75-80
    sprite('jn600_17', 6)	# 81-86
    sprite('jn600_18', 6)	# 87-92
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Kenchira():
    sprite('jn430_26', 4)	# 1-4
    sprite('jn430_25', 4)	# 5-8
    sprite('jn430_24', 5)	# 9-13
    sprite('jn430_23', 5)	# 14-18
    GFX_0('EffNoutou', 0)
    sprite('jn430_23', 32767)	# 19-32785
    loopRest()

@State
def Act2Event_KenchiraEnd():
    sprite('jn430_23', 5)	# 1-5
    sprite('jn430_24', 6)	# 6-11
    sprite('jn430_25', 6)	# 12-17
    sprite('jn430_26', 6)	# 18-23
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_SummonTrinity():
    sprite('keep', 2)	# 1-2
    GFX_0('ptPhantom', -1)
    Unknown36(1)
    teleportRelativeX(-50000)
    Unknown2019(-500)
    Unknown35()
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_bnvsjn_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('jn003_01', 4)	# 1-4
    Unknown2005()
    sprite('jn003_00', 4)	# 5-8
    sprite('jn030_00', 6)	# 9-14
    physicsXImpulse(4650)
    sprite('jn030_01', 6)	# 15-20
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)	# 21-26
    sprite('jn030_03', 6)	# 27-32
    sprite('jn030_04', 6)	# 33-38
    sprite('jn030_05', 6)	# 39-44
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)	# 45-50
    sprite('jn030_07', 6)	# 51-56
    sprite('jn030_08', 6)	# 57-62
    sprite('jn030_09', 6)	# 63-68
    sprite('jn030_01', 6)	# 69-74
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_02', 6)	# 75-80
    sprite('jn030_03', 6)	# 81-86
    sprite('jn030_04', 6)	# 87-92
    sprite('jn030_05', 6)	# 93-98
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jn030_06', 6)	# 99-104
    sprite('jn030_07', 6)	# 105-110
    sprite('jn030_08', 6)	# 111-116
    sprite('jn030_09', 6)	# 117-122
    sprite('null', 32767)	# 123-32889
    Unknown1084(1)

@State
def Act2Event_cevsjn_00():
    sprite('jn620_00', 5)	# 1-5
    sprite('jn620_01', 5)	# 6-10
    sprite('jn620_01', 7)	# 11-17
    sprite('jn620_00', 7)	# 18-24
    sprite('jn000_00', 7)	# 25-31
    sprite('jn001_00', 8)	# 32-39
    sprite('jn001_01', 8)	# 40-47
    sprite('jn001_02', 10)	# 48-57
    sprite('jn001_03', 8)	# 58-65
    sprite('jn001_04', 8)	# 66-73
    sprite('jn001_05', 8)	# 74-81
    sprite('jn001_06', 10)	# 82-91
    sprite('jn001_07', 8)	# 92-99
    sprite('jn001_08', 8)	# 100-107
    sprite('jn001_09', 8)	# 108-115
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvstb_00():
    sprite('jn300_00', 6)	# 1-6
    sprite('jn300_01', 6)	# 7-12
    sprite('jn300_02', 6)	# 13-18
    sprite('jn300_03', 6)	# 19-24
    sprite('jn300_04', 32767)	# 25-32791
    loopRest()

@State
def Act3Event_jnvstb_01():
    sprite('jn300_05', 7)	# 1-7
    sprite('jn300_06', 7)	# 8-14
    sprite('jn300_07', 7)	# 15-21
    sprite('jn300_08', 7)	# 22-28
    sprite('jn300_09', 7)	# 29-35
    sprite('jn300_10', 7)	# 36-42
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvstb_02():
    sprite('jn001_00', 8)	# 1-8
    sprite('jn001_01', 8)	# 9-16
    sprite('jn001_02', 10)	# 17-26
    sprite('jn001_03', 8)	# 27-34
    sprite('jn001_04', 8)	# 35-42
    sprite('jn001_05', 8)	# 43-50
    sprite('jn001_06', 10)	# 51-60
    sprite('jn001_07', 8)	# 61-68
    sprite('jn001_08', 8)	# 69-76
    sprite('jn001_09', 8)	# 77-84
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvstb_03():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('jn414_06', 1)	# 1-1
    SFX_0('009_swing_rapier_1')
    sprite('jn414_07', 2)	# 2-3
    sprite('jn414_08', 2)	# 4-5
    SFX_0('009_swing_rapier_2')
    GFX_0('zan414', -1)
    sprite('jn414_09', 2)	# 6-7	 **attackbox here**
    sprite('jn414_09', 16)	# 8-23	 **attackbox here**
    sprite('jn414_10', 6)	# 24-29
    sprite('jn414_11', 6)	# 30-35
    GFX_0('EffNoutou', 0)
    sprite('jn414_12', 24)	# 36-59
    sprite('jn414_13', 5)	# 60-64
    sprite('jn414_14', 5)	# 65-69
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvstb_04():
    sprite('jn601_14', 6)	# 1-6
    sprite('jn600_18', 6)	# 7-12
    sprite('jn601_09', 6)	# 13-18
    sprite('jn601_10', 6)	# 19-24
    sprite('jn601_11', 6)	# 25-30
    sprite('jn601_12', 32767)	# 31-32797
    loopRest()

@State
def Act3Event_jnvstb_05():
    sprite('keep', 30)	# 1-30
    Unknown20000(1)
    Unknown20004(1)
    sprite('keep', 10)	# 31-40
    GFX_0('Act3Event_ptPhantom_Renew', -1)
    sprite('keep', 32767)	# 41-32807
    loopRest()

@State
def Act3Event_jnvstb_06():
    sprite('keep', 2)	# 1-2
    sprite('jn601_13', 6)	# 3-8
    sprite('jn601_14', 6)	# 9-14
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvsrc_00():
    sprite('jn610_00', 5)	# 1-5
    sprite('jn610_01', 5)	# 6-10
    sprite('jn610_02', 5)	# 11-15
    sprite('jn610_03', 5)	# 16-20
    sprite('jn610_04', 5)	# 21-25
    sprite('jn610_05', 5)	# 26-30
    sprite('jn610_06', 5)	# 31-35
    sprite('jn610_07', 5)	# 36-40
    sprite('jn610_08', 32767)	# 41-32807
    loopRest()

@State
def Act3Event_jnvsrc_01():
    sprite('keep', 2)	# 1-2
    sprite('jn610_00', 7)	# 3-9
    loopRest()
    enterState('Act3Event_jnvstb_00')

@State
def Act3Event_jnvsrc_02():
    sprite('keep', 2)	# 1-2
    GFX_0('Act3Event_ptPhantom_Renew', -1)
    sprite('keep', 32767)	# 3-32769
    loopRest()

@State
def Act3Event_jnvsno_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1000(-960000)
        Unknown2003(1)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 300000):
                    clearUponHandler(3)
                    Unknown21007(22, 32)
                    sendToLabelUpon(2, 100)
                    sendToLabel(0)
            elif (SLOT_22 > (-300000)):
                clearUponHandler(3)
                Unknown21007(22, 32)
                sendToLabelUpon(2, 100)
                sendToLabel(0)
    sprite('jn408_00', 3)	# 1-3
    GFX_0('Act3Event_IceBoard', -1)
    Unknown38(4, 1)
    sprite('jn408_01', 3)	# 4-6
    physicsXImpulse(-3000)
    physicsYImpulse(15000)
    Unknown1043()
    sprite('jn408_02', 3)	# 7-9
    sprite('jn408_03', 2)	# 10-11
    sprite('jn408_04', 2)	# 12-13
    physicsYImpulse(0)
    setGravity(0)
    sprite('jn408_05', 3)	# 14-16
    SFX_0('000_airdash_0')
    physicsXImpulse(42000)
    Unknown1028(1000)
    Unknown21007(4, 32)
    label(1)
    sprite('jn408_06ex', 2)	# 17-18	 **attackbox here**
    sprite('jn408_07ex', 2)	# 19-20	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 3)	# 21-23
    sprite('keep', 7)	# 24-30
    Unknown1028(0)
    Unknown1019(0)
    sprite('jn408_08', 5)	# 31-35
    Unknown13(4)
    GFX_0('Act3Event_IceBoard_koware', -1)
    physicsXImpulse(-10000)
    physicsYImpulse(14000)
    Unknown1043()
    label(9)
    sprite('jn408_09', 3)	# 36-38
    sprite('jn408_10', 3)	# 39-41
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('jn020_10', 4)	# 42-45
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('jn020_11', 5)	# 46-50
    sprite('jn020_12', 6)	# 51-56
    sprite('jn020_13', 5)	# 57-61
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvsno_01():
    sprite('jn430_00', 3)	# 1-3
    SFX_0('009_swing_rapier_2')
    sprite('jn430_04', 4)	# 4-7
    sprite('jn430_03', 4)	# 8-11
    sprite('jn430_02', 4)	# 12-15
    sprite('jn430_01', 32767)	# 16-32782
    loopRest()

@State
def Act3Event_jnvsno_02():
    sprite('jn410_14', 2)	# 1-2
    SFX_0('009_swing_rapier_1')
    sprite('jn410_15', 3)	# 3-5	 **attackbox here**
    sprite('jn410_16', 4)	# 6-9
    sprite('jn410_17', 4)	# 10-13
    sprite('jn410_18', 4)	# 14-17
    sprite('jn410_19', 15)	# 18-32
    GFX_0('EffNoutou', 0)
    sprite('jn410_20', 7)	# 33-39
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvsno_03():

    def upon_IMMEDIATE():
        Unknown1000(-900000)
        Unknown2034(0)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 360000):
                sendToLabel(0)
                clearUponHandler(3)
        elif (SLOT_22 > (-360000)):
            sendToLabel(0)
            clearUponHandler(3)
    sprite('jn032_00', 4)	# 1-4
    Unknown8006(100, 1, 1)
    physicsXImpulse(24000)
    sprite('jn032_01', 4)	# 5-8
    label(9)
    sprite('jn032_02', 4)	# 9-12
    sprite('jn032_03', 4)	# 13-16
    sprite('jn032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 21-24
    sprite('jn032_06', 4)	# 25-28
    sprite('jn032_07', 4)	# 29-32
    sprite('jn032_08', 4)	# 33-36
    sprite('jn032_09', 4)	# 37-40
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 41-44
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('jn032_11', 6)	# 45-50
    physicsXImpulse(0)
    Unknown1045(10000)
    sprite('jn032_12', 6)	# 51-56
    loopRest()
    Unknown1084(1)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def Act3Event_jnvskg_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('jn407_09', 1)	# 1-1
    sprite('jn407_10', 2)	# 2-3
    sprite('jn407_11', 2)	# 4-5
    SFX_3('jnse_21')
    GFX_0('EFF28AtkD', 0)
    sprite('jn407_12', 24)	# 6-29	 **attackbox here**
    GFX_0('Act3Event_Offset', 0)
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('jn407_13', 3)	# 30-32
    sprite('jn407_14', 3)	# 33-35
    sprite('jn407_15', 3)	# 36-38
    sprite('jn407_16', 3)	# 39-41
    sprite('jn407_17', 3)	# 42-44
    sprite('jn407_18', 3)	# 45-47
    sprite('jn407_19', 3)	# 48-50
    sprite('jn407_20', 3)	# 51-53
    sprite('jn407_21', 5)	# 54-58
    sprite('jn407_22', 4)	# 59-62
    sprite('jn407_23', 3)	# 63-65
    sprite('jn407_24', 3)	# 66-68
    GFX_0('EffNoutou', 0)
    sprite('jn407_25', 3)	# 69-71
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_arvsjn_00():

    def upon_IMMEDIATE():
        teleportRelativeX(180000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('jn000_00', 7)	# 1-7
    sprite('jn000_01', 7)	# 8-14
    sprite('jn000_02', 7)	# 15-21
    sprite('jn000_03', 7)	# 22-28
    sprite('jn000_04', 7)	# 29-35
    sprite('jn000_05', 7)	# 36-42
    sprite('jn000_06', 7)	# 43-49
    sprite('jn000_07', 7)	# 50-56
    sprite('jn000_08', 7)	# 57-63
    sprite('jn000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jn620_00', 2)	# 71-72
    clearUponHandler(32)
    SFX_0('100_hit_grap_2')
    ScreenShake(3000, 18000)
    Unknown4045('65665f6869746d6400000000000000000000000000000000000000000000000067000000')
    sprite('jn620_01', 2)	# 73-74
    sprite('jn620_02', 2)	# 75-76
    sprite('jn620_03', 2)	# 77-78
    sprite('jn620_04', 2)	# 79-80
    sprite('jn620_05', 16)	# 81-96
    Unknown1047(-29000)
    sprite('jn620_06', 5)	# 97-101
    sprite('jn620_07', 5)	# 102-106
    sprite('jn620_08', 32767)	# 107-32873
    Unknown1084(1)
    loopRest()

@State
def Act3Event_arvsjn_01():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('jn620_08', 3)	# 1-3
    sprite('jn620_07', 3)	# 4-6
    sprite('jn620_06', 3)	# 7-9
    sprite('jn620_05', 3)	# 10-12
    sprite('jn620_04', 5)	# 13-17
    sprite('jn620_03', 2)	# 18-19
    sprite('jn620_02', 2)	# 20-21
    sprite('jn620_01', 2)	# 22-23
    sprite('jn620_00', 2)	# 24-25
    sprite('jn000_00', 5)	# 26-30
    sprite('jn405_00', 2)	# 31-32
    sprite('jn405_01', 2)	# 33-34
    sprite('jn405_02', 2)	# 35-36
    sprite('jn405_03', 1)	# 37-37
    GFX_0('EFF28AtkA', 0)
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    sprite('jn405_04', 16)	# 38-53	 **attackbox here**
    SFX_3('jnse_21')
    Unknown21007(22, 32)
    sprite('jn405_05', 3)	# 54-56
    sprite('jn405_06', 3)	# 57-59
    sprite('jn405_07', 2)	# 60-61
    sprite('jn405_07ex', 2)	# 62-63
    sprite('jn405_08', 2)	# 64-65
    sprite('jn405_08ex', 2)	# 66-67
    sprite('jn405_09', 2)	# 68-69
    sprite('jn405_09ex', 2)	# 70-71
    sprite('jn405_10', 2)	# 72-73
    sprite('jn405_11', 3)	# 74-76
    GFX_0('EffNoutou', 0)
    sprite('jn405_12', 2)	# 77-78
    sprite('jn405_13', 2)	# 79-80
    sprite('jn405_14', 2)	# 81-82
    sprite('jn405_15', 2)	# 83-84
    sprite('jn405_16', 2)	# 85-86
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_DashOut():
    sprite('jn003_01', 4)	# 1-4
    Unknown2005()
    sprite('jn003_00', 4)	# 5-8
    sprite('jn032_00', 4)	# 9-12
    Unknown2034(0)
    Unknown2017(0)
    physicsXImpulse(24000)
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 13-16
    sprite('jn032_02', 4)	# 17-20
    sprite('jn032_03', 4)	# 21-24
    sprite('jn032_04', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 29-32
    Unknown21007(22, 32)
    sprite('jn032_06', 4)	# 33-36
    sprite('jn032_07', 4)	# 37-40
    sprite('jn032_08', 4)	# 41-44
    sprite('jn032_09', 4)	# 45-48
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 49-52
    sprite('jn032_00', 4)	# 53-56
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 57-60
    sprite('jn032_02', 4)	# 61-64
    sprite('jn032_03', 4)	# 65-68
    sprite('jn032_04', 4)	# 69-72
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 73-76
    sprite('jn032_06', 4)	# 77-80
    sprite('jn032_07', 4)	# 81-84
    sprite('jn032_08', 4)	# 85-88
    sprite('jn032_09', 4)	# 89-92
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 93-96
    sprite('null', 32767)	# 97-32863

@State
def Act3Event_ptvsjn_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('jn414_06', 1)	# 1-1
    SFX_0('009_swing_rapier_1')
    sprite('jn414_07', 2)	# 2-3
    sprite('jn414_08', 2)	# 4-5
    SFX_0('009_swing_rapier_2')
    GFX_0('zan414', -1)
    sprite('jn414_09', 2)	# 6-7	 **attackbox here**
    sprite('jn414_09', 16)	# 8-23	 **attackbox here**
    Unknown21007(22, 32)
    sprite('jn414_10', 6)	# 24-29
    sprite('jn414_11', 6)	# 30-35
    GFX_0('EffNoutou', 0)
    sprite('jn414_12', 24)	# 36-59
    sprite('jn414_13', 5)	# 60-64
    sprite('jn414_14', 5)	# 65-69
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_izvsjn_00():
    sprite('jn110_05', 3)	# 1-3
    teleportRelativeX(230000)
    sprite('jn110_06', 8)	# 4-11
    GFX_1('caef_guardcrash', 0)
    ScreenShake(10000, 50000)
    sprite('jn110_06', 4)	# 12-15
    Unknown1047(-50000)
    sprite('jn110_07', 10)	# 16-25
    Unknown1051(30)
    Unknown8003(100, 1, 1)
    sprite('jn110_07', 5)	# 26-30
    Unknown8003(100, 1, 0)
    Unknown1084(1)
    sprite('jn110_08', 7)	# 31-37
    sprite('jn010_00', 6)	# 38-43
    sprite('jn000_00', 6)	# 44-49
    sprite('jn000_00', 6)	# 50-55
    sprite('jn610_00', 5)	# 56-60
    sprite('jn610_01', 5)	# 61-65
    sprite('jn610_02', 5)	# 66-70
    sprite('jn610_03', 5)	# 71-75
    sprite('jn610_04', 5)	# 76-80
    sprite('jn610_05', 5)	# 81-85
    sprite('jn610_06', 5)	# 86-90
    sprite('jn610_07', 5)	# 91-95
    sprite('jn610_08', 5)	# 96-100
    sprite('jn610_00', 7)	# 101-107
    loopRest()
    enterState('CmnActStand')
    loopRest()

@State
def Act3Event_tmvsjn_00():
    sprite('jn300_00', 6)	# 1-6
    sprite('jn300_01', 6)	# 7-12
    sprite('jn300_02', 6)	# 13-18
    sprite('jn300_03', 6)	# 19-24
    sprite('jn300_04', 32767)	# 25-32791
    loopRest()

@State
def Act3Event_tmvsjn_01():
    sprite('jn300_05', 7)	# 1-7
    Unknown21012('416374334576656e745f70745068616e746f6d5f52656e65770000000000000020000000')
    sprite('jn300_06', 7)	# 8-14
    sprite('jn300_07', 7)	# 15-21
    sprite('jn300_08', 7)	# 22-28
    sprite('jn300_09', 7)	# 29-35
    sprite('jn300_10', 7)	# 36-42
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tmvsjn_02():
    sprite('jn110_05', 3)	# 1-3
    teleportRelativeX(230000)
    sprite('jn110_06', 8)	# 4-11
    Unknown4045('65665f67697264627265616b000000000000000000000000000000000000000067000000')
    SFX_0('106_guard_crush')
    SFX_0('101_hit_slash_3')
    ScreenShake(10000, 50000)
    sprite('jn110_06', 4)	# 12-15
    Unknown1047(-50000)
    sprite('jn110_07', 10)	# 16-25
    Unknown1051(30)
    Unknown8003(100, 1, 1)
    sprite('jn110_07', 5)	# 26-30
    Unknown8003(100, 1, 0)
    Unknown1084(1)
    sprite('jn110_08', 7)	# 31-37
    sprite('jn000_00', 6)	# 38-43

    def upon_3():
        SLOT_51 = (SLOT_51 + 1)
        if (SLOT_51 == 3):
            if op(4, 2, 52, 0, 2):
                teleportRelativeX(1000)
            else:
                teleportRelativeX(-1000)
            SLOT_51 = 0
            SLOT_52 = (SLOT_52 + 1)
    sprite('jn620_00', 5)	# 44-48
    sprite('jn620_01', 5)	# 49-53
    sprite('jn620_02', 5)	# 54-58
    sprite('jn620_03', 5)	# 59-63
    sprite('jn620_04', 5)	# 64-68
    sprite('jn620_05', 5)	# 69-73
    sprite('jn620_06', 5)	# 74-78
    sprite('jn620_07', 5)	# 79-83
    sprite('jn620_08', 32767)	# 84-32850
    clearUponHandler(3)
    loopRest()

@State
def Act3Event_tmvsjn_03():
    sprite('keep', 2)	# 1-2
    GFX_0('Act3Event_ptPhantom_Renew', -1)
    sprite('keep', 32767)	# 3-32769
    loopRest()

@State
def Act3Event_tmvsjn_04():
    sprite('jn430_23', 5)	# 1-5
    GFX_0('Act3Event_ptPhantom_Renew', -1)
    sprite('jn430_24', 6)	# 6-11
    sprite('jn430_25', 6)	# 12-17
    sprite('jn430_26', 6)	# 18-23
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tmvsjn_05():
    sprite('jn620_08', 6)	# 1-6
    Unknown21012('416374334576656e745f70745068616e746f6d5f52656e65770000000000000020000000')
    sprite('jn620_07', 6)	# 7-12
    sprite('jn620_06', 6)	# 13-18
    sprite('jn620_05', 6)	# 19-24
    sprite('jn620_04', 5)	# 25-29
    sprite('jn620_03', 2)	# 30-31
    sprite('jn620_02', 2)	# 32-33
    sprite('jn620_01', 2)	# 34-35
    sprite('jn620_00', 2)	# 36-37
    sprite('jn000_00', 4)	# 38-41
    sprite('jn003_01', 4)	# 42-45
    Unknown2005()
    sprite('jn003_00', 4)	# 46-49
    sprite('jn032_00', 4)	# 50-53
    Unknown2034(0)
    Unknown2017(0)
    physicsXImpulse(24000)
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 54-57
    sprite('jn032_02', 4)	# 58-61
    sprite('jn032_03', 4)	# 62-65
    sprite('jn032_04', 4)	# 66-69
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 70-73
    Unknown21007(22, 32)
    sprite('jn032_06', 4)	# 74-77
    sprite('jn032_07', 4)	# 78-81
    sprite('jn032_08', 4)	# 82-85
    sprite('jn032_09', 4)	# 86-89
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 90-93
    sprite('jn032_00', 4)	# 94-97
    Unknown8006(100, 1, 1)
    sprite('jn032_01', 4)	# 98-101
    sprite('jn032_02', 4)	# 102-105
    sprite('jn032_03', 4)	# 106-109
    sprite('jn032_04', 4)	# 110-113
    Unknown8006(100, 1, 1)
    sprite('jn032_05', 4)	# 114-117
    sprite('jn032_06', 4)	# 118-121
    sprite('jn032_07', 4)	# 122-125
    sprite('jn032_08', 4)	# 126-129
    sprite('jn032_09', 4)	# 130-133
    Unknown8006(100, 1, 1)
    sprite('jn032_10', 4)	# 134-137
    sprite('null', 32767)	# 138-32904

@State
def Act3Event_phvsjn_00():
    sprite('jn110_05', 3)	# 1-3
    teleportRelativeX(230000)
    sprite('jn110_06', 8)	# 4-11
    Unknown4045('65665f67697264627265616b000000000000000000000000000000000000000067000000')
    SFX_0('106_guard_crush')
    SFX_0('101_hit_slash_3')
    ScreenShake(10000, 50000)
    sprite('jn110_06', 4)	# 12-15
    Unknown1047(-50000)
    sprite('jn110_07', 10)	# 16-25
    Unknown1051(30)
    Unknown8003(100, 1, 1)
    sprite('jn110_07', 5)	# 26-30
    Unknown8003(100, 1, 0)
    Unknown1084(1)
    sprite('jn110_08', 7)	# 31-37
    sprite('jn000_00', 6)	# 38-43
    loopRest()
    sprite('jn300_00', 6)	# 44-49
    sprite('jn300_01', 6)	# 50-55
    sprite('jn300_02', 6)	# 56-61
    sprite('jn300_03', 6)	# 62-67
    sprite('jn300_04', 30)	# 68-97
    sprite('jn300_05', 7)	# 98-104
    sprite('jn300_06', 7)	# 105-111
    sprite('jn300_07', 7)	# 112-118
    sprite('jn300_08', 7)	# 119-125
    sprite('jn300_09', 7)	# 126-132
    sprite('jn300_10', 7)	# 133-139
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_phvsjn_01():
    sprite('jn033_00', 2)	# 1-2
    Unknown2034(0)
    sprite('jn033_01', 3)	# 3-5
    physicsXImpulse(-48000)
    physicsYImpulse(30000)
    setGravity(1550)
    Unknown8002()
    SFX_0('000_airdash_2')
    sprite('jn033_02', 3)	# 6-8
    sprite('jn033_03', 3)	# 9-11
    sprite('jn033_04', 3)	# 12-14
    sprite('jn033_05', 2)	# 15-16
    sprite('jn033_06', 1)	# 17-17
    sprite('jn033_07', 1)	# 18-18
    sprite('jn033_08', 1)	# 19-19
    sprite('null', 32767)	# 20-32786
    loopRest()

@State
def Act3Event_phvsjn_02():
    sprite('keep', 2)	# 1-2
    GFX_0('Act3Event_ptPhantom_Renew', -1)
    loopRest()
    enterState('CmnActStand')