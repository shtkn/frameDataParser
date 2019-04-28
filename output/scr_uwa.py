@Subroutine
def PreInit():
    Unknown12019('75776100000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(20000)
    DashFInitialVelocity(9000)
    DashFAccel(0)
    Unknown12038(23000)
    Unknown12034(33)
    Unknown12036(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(4)
    Unknown13039(0)
    Unknown2049(1)
    Unknown12046(35)
    Unknown12029(0)
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 736000, -200000, 380000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 705000, -200000, 505000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(-64000, 700000, -200000, 408000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 786000, -200000, 280000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 448000, -200000, 92000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(1500)
    Unknown14015(0, 672000, -200000, 732000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(2000)
    Unknown14015(0, 872000, -200000, 280000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(4000)
    Unknown14015(-256000, 510000, -200000, 513000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2BB', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(4000)
    Unknown14015(37000, 574000, -123000, 538000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 607000, -200000, 88000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(-254000, 545000, -458000, 412000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(25000, 709000, -167000, 221000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 670000, -92000, 444000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(-104000, 516000, -801000, 160000, 500, 50)
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
    Move_Register('AssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(360000, 1000000, -200000, 436000, 1000, 50)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 841000, -200000, 438000, 1000, 50)
    Move_EndRegister()
    Move_Register('AssaultC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(0, 641000, -200000, 438000, 1000, 50)
    Move_EndRegister()
    Move_Register('CommandThrowA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15010()
    Unknown15013(2000)
    Unknown15021(500)
    Unknown14015(0, 150000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('CommandThrowB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15010()
    Unknown15021(500)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('CommandThrowC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15010()
    Unknown15013(2000)
    Unknown15021(500)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('AirCommandThrowA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15010()
    Unknown15021(4000)
    Unknown14015(0, 400000, -300000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('AirCommandThrowB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15010()
    Unknown15021(4000)
    Unknown14015(0, 400000, -300000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('AirCommandThrowC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15010()
    Unknown15021(4000)
    Unknown14015(0, 400000, -300000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 300000, -200000, 280000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateThrow', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15012(0)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('UltimateRunningThrow', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15012(0)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 800000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('UltimateThrowOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15010()
    Unknown15012(0)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('UltimateRunningThrowOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15010()
    Unknown15012(0)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 800000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('UltimateThrow_TRUE', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(0xcb)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('UltimateThrowOD_TRUE', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(0xcb)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA_Exe2', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA_Exe2', 'CommandThrowB', 10000000)
    Unknown15024('NmlAtk5AAA_Exe2', 'UltimateThrow', 10000000)
    Unknown15024('NmlAtk5AAA_Exe2', 'UltimateThrowOD', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk2BB', 10000000)
    Unknown12018(0, 'Action_330_01')
    Unknown12018(1, 'Action_330_05')
    Unknown12018(2, 'Action_330_04')
    Unknown12018(3, 'Action_330_06')
    Unknown12018(4, 'Action_330_07')
    Unknown12018(5, 'Action_330_07')
    Unknown12018(6, 'Action_330_08')
    Unknown12018(7, 'Action_017_01')
    Unknown12018(8, 'Action_017_01')
    Unknown12018(9, 'Action_019_01')
    Unknown12018(10, 'Action_331_00')
    Unknown12018(11, 'Action_331_00')
    Unknown12018(12, 'Action_320_02')
    Unknown12018(13, 'Action_330_08')
    Unknown12018(14, 'Action_330_09')
    Unknown12018(15, 'Action_290_00')
    Unknown12018(16, 'Action_300_01')
    Unknown12018(17, 'Action_304_02')
    Unknown12018(18, 'Action_305_03')
    Unknown12018(25, 'Action_326_00')
    Unknown12018(26, 'Action_326_02')
    Unknown12018(27, 'Action_326_03')
    Unknown12018(28, 'Action_354_00')
    Unknown12018(29, 'Action_356_04')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'uwa000')
    Unknown7010(1, 'uwa001')
    Unknown7010(2, 'uwa002')
    Unknown7010(3, 'uwa003')
    Unknown7010(4, 'uwa004')
    Unknown7010(5, 'uwa005')
    Unknown7010(6, 'uwa006')
    Unknown7010(7, 'uwa007')
    Unknown7010(8, 'uwa008')
    Unknown7010(9, 'uwa009')
    Unknown7010(10, 'uwa010')
    Unknown7010(15, 'uwa011')
    Unknown7010(16, 'uwa012')
    Unknown7010(17, 'uwa013')
    Unknown7010(18, 'uwa014')
    Unknown7010(19, 'uwa015')
    Unknown7010(20, 'uwa016')
    Unknown7010(21, 'uwa017')
    Unknown7010(22, 'uwa018')
    Unknown7010(23, 'uwa019')
    Unknown7010(24, 'uwa020')
    Unknown7010(25, 'uwa021')
    Unknown7010(28, 'uwa022')
    Unknown7010(29, 'uwa023')
    Unknown7010(30, 'uwa024')
    Unknown7010(31, 'uwa025')
    Unknown7010(32, 'uwa026')
    Unknown7010(33, 'uwa027')
    Unknown7010(34, 'uwa028')
    Unknown7010(35, 'uwa029')
    Unknown7010(36, 'uwa030')
    Unknown7010(37, 'uwa031')
    Unknown7010(39, 'uwa032')
    Unknown7010(42, 'uwa033')
    Unknown7010(43, 'uwa034')
    Unknown7010(44, 'uwa035')
    Unknown7010(45, 'uwa036')
    Unknown7010(46, 'uwa037')
    Unknown7010(47, 'uwa038')
    Unknown7010(48, 'uwa039')
    Unknown7010(49, 'uwa040')
    Unknown7010(50, 'uwa041')
    Unknown7010(52, 'uwa042')
    Unknown7010(53, 'uwa043')
    Unknown7010(54, 'uwa100_0')
    Unknown7010(55, 'uwa100_1')
    Unknown7010(56, 'uwa100_2')
    Unknown7010(63, 'uwa101_0')
    Unknown7010(64, 'uwa101_1')
    Unknown7010(65, 'uwa101_2')
    Unknown7010(57, 'uwa102_0')
    Unknown7010(58, 'uwa102_1')
    Unknown7010(59, 'uwa102_2')
    Unknown7010(66, 'uwa103_0')
    Unknown7010(67, 'uwa103_1')
    Unknown7010(68, 'uwa103_2')
    Unknown7010(60, 'uwa104_0')
    Unknown7010(61, 'uwa104_1')
    Unknown7010(62, 'uwa104_2')
    Unknown7010(69, 'uwa105_0')
    Unknown7010(70, 'uwa105_1')
    Unknown7010(71, 'uwa105_2')
    Unknown7010(72, 'uwa150')
    Unknown7010(73, 'uwa151')
    Unknown7010(74, 'uwa152')
    Unknown7010(85, 'uwa153')
    Unknown7010(87, 'uwa154')
    Unknown7010(88, 'uwa155')
    Unknown7010(96, 'uwa161_0')
    Unknown7010(97, 'uwa161_1')
    Unknown7010(92, 'uwa162_0')
    Unknown7010(93, 'uwa162_1')
    Unknown7010(98, 'uwa163_0')
    Unknown7010(99, 'uwa163_1')
    Unknown7010(100, 'uwa164_0')
    Unknown7010(101, 'uwa164_1')
    Unknown7010(105, 'uwa165_0')
    Unknown7010(106, 'uwa165_1')
    Unknown7010(102, 'uwa166_0')
    Unknown7010(103, 'uwa166_1')
    Unknown7010(90, 'uwa167_0')
    Unknown7010(91, 'uwa167_1')
    Unknown7010(107, 'uwa168_0')
    Unknown7010(108, 'uwa168_1')
    Unknown7010(110, 'uwa169_0')
    Unknown7010(111, 'uwa169_1')
    Unknown7010(94, 'uwa400_0')
    Unknown7010(95, 'uwa400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746552756e6e696e675468726f77000000000000000000000000')
    Unknown12059('03000000556c74696d61746552756e6e696e675468726f774f4400000000000000000000')
    Unknown12059('04000000556c74696d6174655468726f7700000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174655468726f774f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFinalize():
    Unknown12046(35)

@Subroutine
def Throw2Throw():
    Unknown11023(1)
    Unknown11054(1000000)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Unknown11002(-1)
    Unknown11045(0)
    Unknown30061(0)
    Unknown11025(0)
    Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
    Unknown11064(1)
    JumpCancel_(0)
    Unknown14083(0)
    Unknown13024(0)
    Unknown13045(0)
    Unknown30068(1)
    setInvincible(1)

@Subroutine
def LandSlamThrow():
    AttackLevel_(4)
    Damage(500)
    Unknown11091(0)
    AttackP2(100)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackY(-60000)
    Unknown9310(1)
    Unknown11072(1, 600000, -200000)
    Unknown11023(1)
    Unknown11050('020000004566665f4c616e64536c616d5468726f77000000000000000000000000000000')
    Unknown11064(1)
    JumpCancel_(0)
    Unknown14083(0)
    Unknown13045(0)
    Unknown13024(0)
    Unknown30068(1)
    setInvincible(1)

@Subroutine
def GuruX2Throw():
    AttackLevel_(4)
    Unknown11091(0)
    AttackP2(100)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackY(-60000)
    Unknown9310(40)
    Hitstop(20)
    Unknown11072(1, 120000, 0)
    Unknown11023(1)
    Unknown11050('020000004566665f44726568656e4475726368626f6872656e5f426f6d62000000000000')
    Unknown9017(1)
    Unknown23027()
    Unknown13024(0)
    Unknown30068(1)
    setInvincible(1)

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
def UltimateRunningThrow_Atk():
    Unknown23056('')
    AttackLevel_(4)
    Damage(2000)
    Unknown11091(20)
    AttackP2(100)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(100000)
    WallbounceReboundTime(0)
    AirUntechableTime(120)
    Unknown11072(1, 300000, 200000)
    Unknown11023(1)
    Unknown9017(1)
    Unknown11064(1)
    Unknown23027()

    def upon_78():
        Unknown20009(900)
        ScreenShake(20000, 20000)

@Subroutine
def UltimateRunningThrow_Init():
    if (not Unknown23148('UltimateRunningThrow_Exe')):
        if (not Unknown23148('UltimateRunningThrowOD_Exe')):
            Unknown2005()
            Unknown23056('')
    physicsXImpulse(60000)
    Unknown1028(3000)
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(10)
    Unknown20000(1)
    Unknown13024(0)
    Unknown30068(1)

    def upon_3():
        if (SLOT_25 < 200000):
            clearUponHandler(3)
            clearUponHandler(17)
            sendToLabel(1)
    loopRelated(17, 80)

    def upon_17():
        clearUponHandler(3)
        clearUponHandler(17)
        sendToLabel(1)
    Unknown28(8, 'UltimateRunningThrow_End')

@State
def CmnActStand():
    Unknown23145('CmnActFWalk')
    if SLOT_0:
        _gotolabel(1)
    Unknown23145('CmnActBWalk')
    if SLOT_0:
        _gotolabel(1)
    label(0)
    sprite('Action_000_00', 7)	# 1-7	 **attackbox here**
    sprite('Action_000_01', 5)	# 8-12	 **attackbox here**
    sprite('Action_000_02', 12)	# 13-24	 **attackbox here**
    sprite('Action_000_03', 14)	# 25-38	 **attackbox here**
    sprite('Action_000_04', 30)	# 39-68	 **attackbox here**
    sprite('Action_000_05', 9)	# 69-77	 **attackbox here**
    sprite('Action_000_06', 6)	# 78-83	 **attackbox here**
    sprite('Action_000_07', 8)	# 84-91	 **attackbox here**
    sprite('Action_000_08', 14)	# 92-105	 **attackbox here**
    sprite('Action_000_09', 17)	# 106-122	 **attackbox here**
    sprite('Action_000_10', 17)	# 123-139	 **attackbox here**
    sprite('Action_000_11', 12)	# 140-151	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_010_00', 3)	# 152-154
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 4)	# 1-4
    sprite('Action_015_01', 5)	# 5-9

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 3)	# 1-3
    sprite('Action_012_01', 2)	# 4-5
    sprite('Action_012_02', 3)	# 6-8

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 7)	# 1-7
    sprite('Action_013_01', 5)	# 8-12
    sprite('Action_013_02', 14)	# 13-26
    sprite('Action_013_03', 15)	# 27-41
    sprite('Action_013_04', 30)	# 42-71
    sprite('Action_013_05', 14)	# 72-85
    sprite('Action_013_06', 8)	# 86-93
    sprite('Action_013_07', 9)	# 94-102
    sprite('Action_013_08', 15)	# 103-117
    sprite('Action_013_09', 15)	# 118-132
    sprite('Action_013_10', 16)	# 133-148
    sprite('Action_013_11', 12)	# 149-160
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 4)	# 1-4
    sprite('Action_016_01', 5)	# 5-9

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 4)	# 1-4
    sprite('Action_014_01', 3)	# 5-7
    sprite('Action_014_02', 5)	# 8-12

@State
def CmnActJumpPre():
    sprite('Action_035_00', 3)	# 1-3
    sprite('Action_035_01', 3)	# 4-6

@State
def CmnActJumpUpper():
    sprite('Action_035_02', 4)	# 1-4
    label(0)
    sprite('Action_035_03', 3)	# 5-7
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('Action_035_05', 5)	# 1-5
    sprite('Action_035_04', 5)	# 6-10

@State
def CmnActJumpDown():
    sprite('Action_035_06', 3)	# 1-3
    label(0)
    sprite('Action_020_00', 3)	# 4-6	 **attackbox here**
    sprite('Action_020_01', 3)	# 7-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('Action_021_00', 3)	# 1-3
    SFX_3('SE025_BoundBig')
    sprite('Action_021_01', 4)	# 4-7
    sprite('Action_021_02', 4)	# 8-11
    sprite('Action_021_03', 4)	# 12-15

@State
def CmnActLandingStiffLoop():
    sprite('Action_021_00', 4)	# 1-4
    sprite('Action_021_01', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('Action_021_02', 3)	# 1-3
    sprite('Action_021_03', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('Action_010_00', 3)	# 1-3
    Unknown1084(1)
    sprite('Action_010_01', 1)	# 4-4
    physicsXImpulse(44000)
    sprite('Action_010_01', 2)	# 5-6
    Unknown1084(1)
    sprite('Action_010_02', 1)	# 7-7
    physicsXImpulse(44000)
    sprite('Action_010_02', 6)	# 8-13
    Unknown1084(1)
    sprite('Action_010_03', 1)	# 14-14
    physicsXImpulse(8000)
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_010_03', 10)	# 15-24
    Unknown1084(1)
    label(0)
    sprite('Action_010_04', 6)	# 25-30
    sprite('Action_010_05', 1)	# 31-31
    physicsXImpulse(20000)
    sprite('Action_010_05', 4)	# 32-35
    Unknown1084(1)
    sprite('Action_010_06', 4)	# 36-39
    sprite('Action_010_07', 1)	# 40-40
    physicsXImpulse(50000)
    sprite('Action_010_07', 3)	# 41-43
    Unknown1084(1)
    sprite('Action_010_08', 1)	# 44-44
    physicsXImpulse(52000)
    sprite('Action_010_08', 2)	# 45-46
    Unknown1084(1)
    sprite('Action_010_09', 1)	# 47-47
    physicsXImpulse(32000)
    sprite('Action_010_09', 4)	# 48-51
    Unknown1084(1)
    sprite('Action_010_10', 1)	# 52-52
    physicsXImpulse(32000)
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_010_10', 6)	# 53-58
    Unknown1084(1)
    sprite('Action_010_11', 1)	# 59-59
    physicsXImpulse(4000)
    sprite('Action_010_11', 8)	# 60-67
    Unknown1084(1)
    sprite('Action_010_12', 1)	# 68-68
    physicsXImpulse(4000)
    sprite('Action_010_12', 5)	# 69-73
    Unknown1084(1)
    sprite('Action_010_13', 1)	# 74-74
    physicsXImpulse(20000)
    sprite('Action_010_13', 4)	# 75-78
    Unknown1084(1)
    sprite('Action_010_14', 1)	# 79-79
    physicsXImpulse(24000)
    sprite('Action_010_14', 3)	# 80-82
    Unknown1084(1)
    sprite('Action_010_15', 1)	# 83-83
    physicsXImpulse(32000)
    sprite('Action_010_15', 3)	# 84-86
    Unknown1084(1)
    sprite('Action_010_16', 1)	# 87-87
    physicsXImpulse(48000)
    sprite('Action_010_16', 2)	# 88-89
    Unknown1084(1)
    sprite('Action_010_17', 1)	# 90-90
    physicsXImpulse(36000)
    sprite('Action_010_17', 4)	# 91-94
    Unknown1084(1)
    sprite('Action_010_18', 7)	# 95-101
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('Action_011_00', 2)	# 1-2
    Unknown1084(1)
    sprite('Action_011_01', 3)	# 3-5
    sprite('Action_011_02', 1)	# 6-6
    teleportRelativeX(-32000)
    sprite('Action_011_02', 4)	# 7-10
    Unknown1084(1)
    sprite('Action_011_03', 1)	# 11-11
    teleportRelativeX(-32000)
    sprite('Action_011_03', 2)	# 12-13
    Unknown1084(1)
    label(0)
    sprite('Action_011_04', 1)	# 14-14
    teleportRelativeX(-16000)
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_011_04', 8)	# 15-22
    Unknown1084(1)
    sprite('Action_011_05', 1)	# 23-23
    teleportRelativeX(-4000)
    sprite('Action_011_05', 6)	# 24-29
    Unknown1084(1)
    sprite('Action_011_06', 1)	# 30-30
    teleportRelativeX(-8000)
    sprite('Action_011_06', 4)	# 31-34
    Unknown1084(1)
    sprite('Action_011_07', 1)	# 35-35
    teleportRelativeX(-20000)
    sprite('Action_011_07', 2)	# 36-37
    Unknown1084(1)
    sprite('Action_011_08', 1)	# 38-38
    teleportRelativeX(-72000)
    sprite('Action_011_08', 3)	# 39-41
    Unknown1084(1)
    sprite('Action_011_09', 1)	# 42-42
    teleportRelativeX(-8000)
    sprite('Action_011_09', 3)	# 43-45
    Unknown1084(1)
    sprite('Action_011_10', 1)	# 46-46
    teleportRelativeX(-28000)
    sprite('Action_011_10', 4)	# 47-50
    Unknown1084(1)
    sprite('Action_011_11', 1)	# 51-51
    teleportRelativeX(-28000)
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_011_11', 5)	# 52-56
    Unknown1084(1)
    sprite('Action_011_12', 1)	# 57-57
    teleportRelativeX(-4000)
    sprite('Action_011_12', 7)	# 58-64
    Unknown1084(1)
    sprite('Action_011_13', 7)	# 65-71
    sprite('Action_011_14', 5)	# 72-76
    sprite('Action_011_15', 1)	# 77-77
    teleportRelativeX(-36000)
    sprite('Action_011_15', 3)	# 78-80
    Unknown1084(1)
    sprite('Action_011_16', 1)	# 81-81
    teleportRelativeX(-80000)
    sprite('Action_011_16', 3)	# 82-84
    Unknown1084(1)
    sprite('Action_011_17', 1)	# 85-85
    teleportRelativeX(-20000)
    sprite('Action_011_17', 2)	# 86-87
    Unknown1084(1)
    sprite('Action_011_18', 1)	# 88-88
    teleportRelativeX(-20000)
    sprite('Action_011_18', 2)	# 89-90
    Unknown1084(1)
    sprite('Action_011_03', 3)	# 91-93
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown1084(1)
        Unknown13014(1)
        Unknown13015(1)
        Unknown13008(1)
        Unknown13019(1)
    sprite('Action_045_00', 8)	# 1-8
    sprite('Action_045_01', 4)	# 9-12
    physicsXImpulse(25000)
    Unknown1028(-1000)
    Unknown1045(9000)
    teleportRelativeX(50000)
    Unknown8007(100, 1, 1)
    sprite('Action_045_02', 4)	# 13-16
    sprite('Action_045_01', 4)	# 17-20
    Unknown8006(100, 1, 0)
    sprite('Action_045_02', 4)	# 21-24
    sprite('Action_045_04', 4)	# 25-28
    Unknown8010(100, 1, 1)
    Unknown1019(50)
    sprite('Action_045_04', 4)	# 29-32
    Unknown1084(1)

@State
def CmnActFDashStop():
    pass

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
    sprite('Action_046_00', 2)	# 1-2
    sprite('Action_046_01', 4)	# 3-6
    physicsXImpulse(-11500)
    physicsYImpulse(3900)
    setGravity(480)
    Unknown8002()
    label(0)
    sprite('Action_046_02', 6)	# 7-12
    sprite('Action_046_03', 6)	# 13-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_04', 3)	# 19-21
    physicsXImpulse(0)
    SFX_3('SE025_BoundBig')
    sprite('Action_046_05', 2)	# 22-23
    Unknown8000(100, 1, 1)
    sprite('Action_046_06', 2)	# 24-25
    sprite('Action_046_07', 3)	# 26-28

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('Action_068_01', 3)	# 1-3
    sprite('Action_068_02', 3)	# 4-6
    sprite('Action_068_02', 3)	# 7-9
    sprite('Action_068_03', 3)	# 10-12
    sprite('Action_068_03', 3)	# 13-15
    sprite('Action_068_04', 3)	# 16-18
    sprite('Action_068_04', 3)	# 19-21
    sprite('Action_068_05', 3)	# 22-24
    sprite('Action_068_05', 3)	# 25-27
    enterState('AirFDashRigor')

@State
def AirFDashRigor():

    def upon_IMMEDIATE():
        Unknown13014(1)
        Unknown13015(1)
        Unknown13031(1)
        Unknown13019(1)
        Unknown28(2, 'CmnActJumpLanding')
    label(0)
    sprite('Action_068_06', 3)	# 1-3
    sprite('Action_068_07', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('Action_046_02', 4)	# 1-4
    physicsYImpulse(12000)
    sprite('Action_046_03', 4)	# 5-8
    label(0)
    sprite('Action_046_02', 4)	# 9-12
    sprite('Action_046_03', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('Action_300_00', 1)	# 1-1
    sprite('Action_300_00', 1)	# 2-2
    sprite('Action_300_01', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('Action_300_00', 1)	# 1-1
    sprite('Action_300_00', 2)	# 2-3
    sprite('Action_300_01', 3)	# 4-6

@State
def CmnActHitStandLv3():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_00', 2)	# 2-3
    sprite('Action_303_01', 2)	# 4-5
    sprite('Action_303_02', 2)	# 6-7
    sprite('Action_303_03', 2)	# 8-9

@State
def CmnActHitStandLv4():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_00', 1)	# 2-2
    sprite('Action_303_01', 3)	# 3-5
    sprite('Action_303_02', 3)	# 6-8
    sprite('Action_303_03', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_00', 3)	# 2-4
    sprite('Action_303_01', 4)	# 5-8
    sprite('Action_303_02', 4)	# 9-12
    sprite('Action_303_03', 4)	# 13-16

@State
def CmnActHitStandLowLv1():
    sprite('Action_304_02', 1)	# 1-1
    sprite('Action_304_02', 1)	# 2-2
    sprite('Action_304_03', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('Action_304_02', 1)	# 1-1
    sprite('Action_304_02', 2)	# 2-3
    sprite('Action_304_03', 3)	# 4-6

@State
def CmnActHitStandLowLv3():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_00', 1)	# 2-2
    sprite('Action_304_01', 2)	# 3-4
    sprite('Action_304_02', 2)	# 5-6
    sprite('Action_304_03', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_00', 1)	# 2-2
    sprite('Action_304_01', 3)	# 3-5
    sprite('Action_304_02', 3)	# 6-8
    sprite('Action_304_03', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_00', 3)	# 2-4
    sprite('Action_304_01', 4)	# 5-8
    sprite('Action_304_02', 4)	# 9-12
    sprite('Action_304_03', 4)	# 13-16

@State
def CmnActHitCrouchLv1():
    sprite('Action_305_02', 1)	# 1-1
    sprite('Action_305_02', 1)	# 2-2
    sprite('Action_305_03', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('Action_305_02', 1)	# 1-1
    sprite('Action_305_02', 2)	# 2-3
    sprite('Action_305_03', 3)	# 4-6

@State
def CmnActHitCrouchLv3():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_00', 2)	# 2-3
    sprite('Action_305_01', 2)	# 4-5
    sprite('Action_305_02', 2)	# 6-7
    sprite('Action_305_03', 2)	# 8-9

@State
def CmnActHitCrouchLv4():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_00', 1)	# 2-2
    sprite('Action_305_01', 3)	# 3-5
    sprite('Action_305_02', 3)	# 6-8
    sprite('Action_305_03', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_00', 3)	# 2-4
    sprite('Action_305_01', 4)	# 5-8
    sprite('Action_305_02', 4)	# 9-12
    sprite('Action_305_03', 4)	# 13-16

@State
def CmnActBDownUpper():
    sprite('Action_320_00', 4)	# 1-4
    label(0)
    sprite('Action_320_01', 4)	# 5-8
    sprite('Action_320_01', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('Action_320_02', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('Action_320_03', 4)	# 1-4
    label(0)
    sprite('Action_330_08', 4)	# 5-8
    sprite('Action_330_09', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('Action_351_00', 2)	# 1-2
    sprite('Action_331_01', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('Action_351_01', 3)	# 1-3
    sprite('Action_351_02', 3)	# 4-6
    sprite('Action_351_03', 3)	# 7-9
    sprite('Action_351_04', 3)	# 10-12
    sprite('Action_351_05', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('Action_356_04', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('Action_294_10', 4)	# 1-4
    sprite('Action_294_11', 4)	# 5-8
    sprite('Action_294_12', 3)	# 9-11
    sprite('Action_294_13', 3)	# 12-14
    sprite('Action_294_14', 3)	# 15-17
    sprite('Action_294_15', 3)	# 18-20
    sprite('Action_294_16', 3)	# 21-23
    sprite('Action_294_17', 3)	# 24-26

@State
def CmnActFDownUpper():
    sprite('Action_326_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('Action_326_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('Action_326_03', 3)	# 1-3
    sprite('Action_326_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('Action_351_00', 3)	# 1-3
    sprite('Action_351_01', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('Action_353_03', 2)	# 1-2
    sprite('Action_353_04', 2)	# 3-4
    sprite('Action_353_05', 3)	# 5-7
    sprite('Action_354_00', 3)	# 8-10
    sprite('Action_354_01', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('Action_356_04', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('Action_294_10', 3)	# 1-3
    sprite('Action_294_11', 3)	# 4-6
    sprite('Action_294_12', 3)	# 7-9
    sprite('Action_294_13', 3)	# 10-12
    sprite('Action_294_14', 2)	# 13-14
    sprite('Action_294_15', 2)	# 15-16
    sprite('Action_294_16', 2)	# 17-18
    sprite('Action_294_17', 2)	# 19-20

@State
def CmnActVDownUpper():
    sprite('Action_330_00', 3)	# 1-3
    label(0)
    sprite('Action_330_01', 3)	# 4-6
    sprite('Action_330_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('Action_330_04', 3)	# 1-3
    sprite('Action_330_05', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('Action_330_06', 3)	# 1-3
    sprite('Action_330_07', 3)	# 4-6
    label(0)
    sprite('Action_330_08', 3)	# 7-9
    sprite('Action_330_09', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('Action_351_00', 2)	# 1-2
    sprite('Action_351_01', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('Action_331_00', 3)	# 1-3
    sprite('Action_331_02', 3)	# 4-6
    sprite('Action_331_03', 3)	# 7-9
    label(0)
    sprite('Action_331_02', 3)	# 10-12
    sprite('Action_331_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6
    sprite('Action_333_03', 2)	# 7-8
    sprite('Action_333_04', 2)	# 9-10
    sprite('Action_333_05', 2)	# 11-12
    sprite('Action_333_06', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    pass

@State
def CmnActFreeze():
    sprite('Action_327_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('Action_340_00', 2)	# 1-2
    sprite('Action_340_01', 2)	# 3-4
    sprite('Action_340_02', 2)	# 5-6

@State
def CmnActWallBoundDown():
    sprite('Action_340_03', 3)	# 1-3
    sprite('Action_340_04', 3)	# 4-6
    label(0)
    sprite('Action_340_05', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('Action_327_00', 14)	# 1-14

@State
def CmnActStaggerDown():
    sprite('Action_327_01', 4)	# 1-4
    sprite('Action_327_02', 4)	# 5-8
    sprite('Action_327_03', 4)	# 9-12
    sprite('Action_327_04', 4)	# 13-16
    sprite('Action_328_00', 3)	# 17-19
    sprite('Action_328_01', 3)	# 20-22

@State
def CmnActUkemiStagger():
    sprite('Action_327_00', 8)	# 1-8

@State
def CmnActUkemiAirF():
    sprite('Action_032_00', 2)	# 1-2
    sprite('Action_032_01', 2)	# 3-4
    sprite('Action_032_02', 2)	# 5-6
    sprite('Action_032_03', 2)	# 7-8
    sprite('Action_032_04', 1)	# 9-9

@State
def CmnActUkemiAirB():
    sprite('Action_032_00', 2)	# 1-2
    sprite('Action_032_01', 2)	# 3-4
    sprite('Action_032_02', 2)	# 5-6
    sprite('Action_032_03', 2)	# 7-8
    sprite('Action_032_04', 1)	# 9-9

@State
def CmnActUkemiAirN():
    sprite('Action_032_00', 2)	# 1-2
    sprite('Action_032_01', 2)	# 3-4
    sprite('Action_032_02', 2)	# 5-6
    sprite('Action_032_03', 2)	# 7-8
    sprite('Action_032_04', 1)	# 9-9

@State
def CmnActUkemiLandF():
    sprite('Action_041_00', 4)	# 1-4
    sprite('Action_041_01', 4)	# 5-8
    sprite('Action_041_02', 4)	# 9-12
    sprite('Action_041_03', 4)	# 13-16
    sprite('Action_041_04', 4)	# 17-20
    sprite('Action_041_05', 4)	# 21-24	 **attackbox here**
    sprite('Action_041_06', 3)	# 25-27	 **attackbox here**

@State
def CmnActUkemiLandB():
    sprite('Action_041_00', 4)	# 1-4
    sprite('Action_041_01', 4)	# 5-8
    sprite('Action_041_02', 4)	# 9-12
    sprite('Action_041_03', 4)	# 13-16
    sprite('Action_041_04', 4)	# 17-20
    sprite('Action_041_05', 4)	# 21-24	 **attackbox here**
    sprite('Action_041_06', 3)	# 25-27	 **attackbox here**

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 4)	# 1-4
    sprite('Action_041_01', 4)	# 5-8
    sprite('Action_041_02', 4)	# 9-12
    sprite('Action_041_03', 4)	# 13-16
    sprite('Action_041_04', 4)	# 17-20
    sprite('Action_041_05', 4)	# 21-24	 **attackbox here**
    sprite('Action_041_06', 3)	# 25-27	 **attackbox here**

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_07', 2)	# 1-2
    SFX_3('SE025_BoundBig')
    sprite('Action_041_08', 4)	# 3-6
    sprite('Action_041_09', 5)	# 7-11
    sprite('Action_041_10', 3)	# 12-14
    sprite('Action_041_11', 3)	# 15-17

@State
def CmnActMidGuardPre():
    sprite('Action_017_07', 3)	# 1-3
    sprite('Action_017_06', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('Action_017_07', 3)	# 1-3
    sprite('Action_017_06', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('Action_018_07', 3)	# 1-3
    sprite('Action_018_06', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('Action_018_00', 3)	# 1-3
    sprite('Action_018_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('Action_018_00', 3)	# 1-3
    sprite('Action_018_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('Action_019_07', 3)	# 1-3
    sprite('Action_019_06', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('Action_019_00', 3)	# 1-3
    sprite('Action_019_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('Action_019_00', 3)	# 1-3
    sprite('Action_019_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('Action_017_00', 2)	# 1-2
    sprite('Action_017_01', 2)	# 3-4
    sprite('Action_017_01', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_017_06', 6)	# 6-11
    sprite('Action_017_07', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('Action_018_00', 2)	# 1-2
    sprite('Action_018_01', 2)	# 3-4
    sprite('Action_018_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_018_01', 6)	# 6-11
    sprite('Action_018_00', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('Action_019_00', 2)	# 1-2
    sprite('Action_019_01', 2)	# 3-4
    sprite('Action_019_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_019_01', 6)	# 6-11
    sprite('Action_019_00', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('Action_035_03', 3)	# 1-3

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_001_01', 4)	# 1-4
    sprite('Action_001_02', 3)	# 5-7
    sprite('Action_001_03', 2)	# 8-9	 **attackbox here**
    sprite('Action_001_05', 3)	# 10-12
    sprite('Action_001_04', 7)	# 13-19
    sprite('Action_001_05', 4)	# 20-23
    sprite('Action_001_06', 4)	# 24-27

@State
def CmnActAirLockWait():
    sprite('hb045_02', 1)	# 1-1
    sprite('hb045_01', 3)	# 2-4
    sprite('hb045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('hb322_00', 2)	# 1-2
    sprite('hb322_01', 2)	# 3-4
    sprite('hb322_02', 8)	# 5-12
    sprite('hb322_03', 2)	# 13-14
    sprite('hb322_04', 3)	# 15-17
    sprite('hb322_05', 3)	# 18-20
    sprite('hb322_06', 3)	# 21-23
    sprite('hb322_07', 3)	# 24-26
    sprite('hb322_08', 3)	# 27-29

@State
def CmnActLandSpin():
    pass

@State
def CmnActLandSpinDown():
    pass

@State
def CmnActVertSpin():
    pass

@State
def CmnActSlideAir():
    label(0)
    sprite('Action_333_00', 3)	# 1-3
    sprite('Action_333_01', 3)	# 4-6
    sprite('Action_333_02', 3)	# 7-9
    sprite('Action_333_03', 3)	# 10-12
    sprite('Action_333_04', 3)	# 13-15
    sprite('Action_333_05', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('Action_351_00', 4)	# 1-4
    label(0)
    sprite('Action_351_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('Action_351_02', 3)	# 1-3
    sprite('Action_351_03', 2)	# 4-5
    sprite('Action_352_00', 2)	# 6-7
    sprite('Action_352_01', 2)	# 8-9

@State
def CmnActAomukeSlideKeep():
    pass

@State
def CmnActAomukeSlideEnd():
    pass

@State
def CmnActBurstBegin():
    pass

@State
def CmnActBurstLoop():
    pass

@State
def CmnActBurstEnd():
    pass

@State
def CmnActAirBurstBegin():
    pass

@State
def CmnActAirBurstLoop():
    pass

@State
def CmnActAirBurstEnd():
    pass

@State
def CmnActOverDriveBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('Action_262_04', 4)	# 1-4
    sprite('Action_262_05', 4)	# 5-8
    sprite('Action_262_06', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('Action_262_06', 6)	# 1-6
    sprite('Action_262_07', 6)	# 7-12
    label(0)
    sprite('Action_020_00', 3)	# 13-15	 **attackbox here**
    sprite('Action_020_01', 3)	# 16-18	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('Action_262_04', 4)	# 1-4
    sprite('Action_262_05', 4)	# 5-8
    sprite('Action_262_06', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('Action_262_06', 6)	# 1-6
    sprite('Action_262_07', 6)	# 7-12
    label(0)
    sprite('Action_020_00', 3)	# 13-15	 **attackbox here**
    sprite('Action_020_01', 3)	# 16-18	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('Action_262_00', 4)	# 1-4
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 4)	# 5-8
    sprite('Action_262_04', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('Action_262_05', 3)	# 1-3
    sprite('Action_262_06', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('Action_262_00', 4)	# 1-4
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 4)	# 5-8
    sprite('Action_262_04', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('Action_262_06', 3)	# 1-3
    sprite('Action_262_07', 3)	# 4-6
    label(0)
    sprite('Action_020_00', 3)	# 7-9	 **attackbox here**
    sprite('Action_020_01', 3)	# 10-12	 **attackbox here**
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
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('Action_110_02', 3)	# 26-28	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    sprite('Action_110_03', 3)	# 29-31	 **attackbox here**
    label(1)
    sprite('Action_110_02', 3)	# 32-34	 **attackbox here**
    sprite('Action_110_03', 3)	# 35-37	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 38-40
    Unknown1084(1)
    sprite('Action_110_04', 2)	# 41-42
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    SFX_3('SE025_BoundBig')
    sprite('Action_110_05', 2)	# 43-44
    sprite('Action_110_06', 5)	# 45-49
    sprite('Action_110_07', 3)	# 50-52
    sprite('Action_110_08', 3)	# 53-55
    sprite('Action_110_09', 3)	# 56-58
    sprite('Action_110_10', 2)	# 59-60
    sprite('Action_110_11', 2)	# 61-62

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_00', 3)	# 1-3
    sprite('Action_045_01', 5)	# 4-8
    sprite('Action_045_02', 7)	# 9-15
    sprite('Action_045_03', 7)	# 16-22
    sprite('Action_045_04', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_046_01', 3)	# 1-3
    sprite('Action_046_02', 3)	# 4-6
    sprite('Action_046_03', 3)	# 7-9
    sprite('Action_046_02', 3)	# 10-12
    sprite('Action_046_03', 3)	# 13-15
    sprite('Action_046_02', 3)	# 16-18
    sprite('Action_046_03', 3)	# 19-21
    sprite('Action_046_02', 3)	# 22-24
    sprite('Action_046_03', 3)	# 25-27
    sprite('Action_046_02', 3)	# 28-30
    sprite('Action_046_03', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('Action_046_00', 2)	# 1-2
    sprite('Action_046_01', 3)	# 3-5
    loopRest()
    label(0)
    sprite('Action_046_02', 3)	# 6-8
    sprite('Action_046_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_04', 3)	# 12-14
    physicsXImpulse(0)
    sprite('Action_046_05', 3)	# 15-17

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_277_00', 2)	# 1-2
    sprite('Action_277_01', 4)	# 3-6
    sprite('Action_277_02', 12)	# 7-18
    sprite('Action_277_03', 2)	# 19-20
    sprite('Action_277_04', 2)	# 21-22
    sprite('Action_277_05', 2)	# 23-24
    sprite('Action_277_06', 4)	# 25-28
    sprite('Action_277_07', 4)	# 29-32
    sprite('Action_277_06', 4)	# 33-36
    sprite('Action_277_07', 4)	# 37-40
    sprite('Action_277_06', 4)	# 41-44
    sprite('Action_277_07', 4)	# 45-48
    sprite('Action_277_06', 4)	# 49-52
    sprite('Action_277_07', 4)	# 53-56
    sprite('Action_277_06', 4)	# 57-60
    sprite('Action_277_07', 4)	# 61-64
    sprite('Action_277_06', 4)	# 65-68
    sprite('Action_277_07', 30)	# 69-98

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
    sprite('Action_020_00', 4)	# 3-6	 **attackbox here**
    Unknown1019(95)
    sprite('Action_020_01', 4)	# 7-10	 **attackbox here**
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('Action_021_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown11033(2)
        Damage(1200)
        AttackP1(70)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(12000)
        AirUntechableTime(60)
        Unknown9016(1)
        Hitstop(2)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_277_00', 4)	# 1-4
    sprite('Action_277_02', 4)	# 5-8
    sprite('Action_277_03', 6)	# 9-14
    sprite('Action_277_04', 8)	# 15-22
    sprite('Action_275_00', 3)	# 23-25
    sprite('Action_275_01', 3)	# 26-28
    GFX_0('Eff_Wirbelwind01', 100)
    Unknown12046(60)
    Unknown7006('uwa202_0', 100, 845248373, 828322352, 0, 0, 100, 845248373, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_275_02', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(40000)
    SFX_3('SE051')
    sprite('Action_275_03', 5)	# 32-36
    teleportRelativeX(40000)
    sprite('Action_275_04', 2)	# 37-38
    teleportRelativeX(40000)
    sprite('Action_275_05', 2)	# 39-40
    GFX_0('Eff_Wirbelwind02', 100)
    teleportRelativeX(80000)
    sprite('Action_275_06', 4)	# 41-44	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(80000)
    SFX_3('SE051')
    sprite('Action_275_07', 4)	# 45-48
    teleportRelativeX(40000)
    sprite('Action_275_08', 4)	# 49-52
    teleportRelativeX(40000)
    sprite('Action_275_09', 2)	# 53-54
    GFX_0('Eff_Wirbelwind03', 100)
    teleportRelativeX(80000)
    sprite('Action_275_10', 5)	# 55-59	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(20000)
    Unknown9083()
    Hitstop(12)
    ScreenShake(5000, 10000)
    teleportRelativeX(80000)
    SFX_3('SE051')
    sprite('Action_275_11', 12)	# 60-71
    sprite('Action_275_12', 8)	# 72-79
    sprite('Action_275_13', 8)	# 80-87

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown11033(2)
        AttackP1(70)
        AirPushbackX(2000)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Unknown9310(10)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_200_00', 6)	# 1-6
    Unknown7009(1)
    sprite('Action_200_01', 6)	# 7-12
    sprite('Action_200_02', 3)	# 13-15	 **attackbox here**
    GFX_0('Eff_6A_00', 100)
    SFX_3('SE043')
    sprite('Action_200_03', 5)	# 16-20
    sprite('Action_200_04', 6)	# 21-26
    sprite('Action_200_05', 7)	# 27-33
    sprite('Action_200_06', 2)	# 34-35	 **attackbox here**
    Unknown7009(2)
    Unknown23027()
    GFX_0('Eff_6A_01', 100)
    GFX_0('Eff_6A_StoneAtk', 0)
    SFX_3('SE043')
    sprite('Action_200_07', 2)	# 36-37
    sprite('Action_200_08', 4)	# 38-41
    sprite('Action_200_09', 9)	# 42-50
    sprite('Action_200_10', 6)	# 51-56
    sprite('Action_200_11', 5)	# 57-61
    sprite('Action_200_12', 5)	# 62-66

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown11033(2)
        AttackP1(70)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(-40000)
        AirUntechableTime(30)
        Unknown9310(1)
        Unknown11042(1)
    sprite('Action_264_00', 3)	# 1-3
    sprite('Action_264_01', 3)	# 4-6
    teleportRelativeX(60000)
    Unknown12046(60)
    Unknown7006('uwa200_0', 100, 845248373, 828321840, 0, 0, 100, 845248373, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_264_02', 2)	# 7-8
    teleportRelativeX(60000)
    sprite('Action_264_03', 2)	# 9-10
    teleportRelativeX(60000)
    sprite('Action_264_04', 2)	# 11-12	 **attackbox here**
    teleportRelativeX(60000)
    GFX_0('Eff_EisenNagel', 100)
    sprite('Action_264_05', 2)	# 13-14
    teleportRelativeX(60000)
    sprite('Action_264_06', 3)	# 15-17	 **attackbox here**
    teleportRelativeX(60000)
    SFX_3('SE051')
    sprite('Action_264_07', 6)	# 18-23
    Recovery()
    Unknown2063()
    teleportRelativeX(25000)
    sprite('Action_264_08', 6)	# 24-29
    sprite('Action_264_09', 5)	# 30-34
    sprite('Action_264_10', 5)	# 35-39
    sprite('Action_264_11', 5)	# 40-44

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
        SLOT_4 = 1
        SLOT_5 = 0
    sprite('null', 1)	# 1-1
    Unknown2036(79, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('Action_020_00', 4)	# 3-6	 **attackbox here**
    sprite('Action_020_01', 4)	# 7-10	 **attackbox here**
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
        Unknown23056('')
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11069('ChangePartnerDD_Exe2')
        Hitstop(0)
        setInvincible(1)

        def upon_78():
            enterState('ChangePartnerDD_Exe2')
    sprite('Action_277_00', 2)	# 1-2
    sprite('Action_277_01', 5)	# 3-7
    sprite('Action_277_02', 2)	# 8-9
    sprite('Action_277_03', 12)	# 10-21
    sprite('Action_277_04', 4)	# 22-25
    sprite('Action_277_05', 4)	# 26-29
    sprite('Action_277_06', 3)	# 30-32
    sprite('Action_277_07', 3)	# 33-35
    sprite('Action_277_06', 3)	# 36-38
    sprite('Action_277_07', 3)	# 39-41
    sprite('Action_277_00', 1)	# 42-42
    sprite('Action_220_00', 4)	# 43-46
    sprite('Action_220_01', 3)	# 47-49
    sprite('Action_220_02', 5)	# 50-54
    sprite('Action_220_03', 5)	# 55-59	 **attackbox here**
    sprite('Action_451_04', 20)	# 60-79	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Unknown23027()
    sprite('Action_451_05', 2)	# 80-81	 **attackbox here**
    sprite('Action_451_06', 8)	# 82-89	 **attackbox here**
    sprite('Action_451_07', 4)	# 90-93	 **attackbox here**

@State
def ChangePartnerDD_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowExe', 5, 0, 0)
        Unknown23056('')
        callSubroutine('Throw2Throw')
        Unknown11069('UltimateThrowExe')
        Unknown20003(1)
    sprite('keep', 1)	# 1-1

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11069('ChangePartnerDDOD_Exe2')
        Hitstop(0)
        setInvincible(1)

        def upon_78():
            enterState('ChangePartnerDDOD_Exe2')
    sprite('Action_277_00', 2)	# 1-2
    sprite('Action_277_01', 5)	# 3-7
    sprite('Action_277_02', 2)	# 8-9
    sprite('Action_277_03', 12)	# 10-21
    sprite('Action_277_04', 4)	# 22-25
    sprite('Action_277_05', 4)	# 26-29
    sprite('Action_277_06', 3)	# 30-32
    sprite('Action_277_07', 3)	# 33-35
    sprite('Action_277_06', 3)	# 36-38
    sprite('Action_277_07', 3)	# 39-41
    sprite('Action_277_00', 1)	# 42-42
    sprite('Action_220_00', 4)	# 43-46
    sprite('Action_220_01', 3)	# 47-49
    sprite('Action_220_02', 5)	# 50-54
    sprite('Action_220_03', 5)	# 55-59	 **attackbox here**
    sprite('Action_451_04', 20)	# 60-79	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Unknown23027()
    sprite('Action_451_05', 2)	# 80-81	 **attackbox here**
    sprite('Action_451_06', 8)	# 82-89	 **attackbox here**
    sprite('Action_451_07', 4)	# 90-93	 **attackbox here**

@State
def ChangePartnerDDOD_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe', 5, 0, 0)
        Unknown23056('')
        callSubroutine('Throw2Throw')
        Unknown11069('UltimateThrowODExe')
        Unknown20003(1)
    sprite('keep', 1)	# 1-1

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('Action_277_00', 2)	# 1-2
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('Action_277_01', 5)	# 3-7
    sprite('Action_277_02', 2)	# 8-9
    sprite('Action_277_03', 12)	# 10-21
    sprite('Action_277_04', 3)	# 22-24
    sprite('Action_277_05', 3)	# 25-27
    sprite('Action_277_06', 3)	# 28-30
    sprite('Action_277_07', 3)	# 31-33
    sprite('Action_277_06', 3)	# 34-36
    sprite('Action_277_07', 3)	# 37-39
    sprite('Action_277_06', 3)	# 40-42
    sprite('Action_277_07', 3)	# 43-45
    sprite('Action_277_06', 3)	# 46-48
    sprite('Action_277_07', 3)	# 49-51
    sprite('Action_277_06', 3)	# 52-54
    sprite('Action_277_07', 3)	# 55-57
    sprite('Action_277_06', 3)	# 58-60
    sprite('Action_277_07', 3)	# 61-63
    sprite('Action_277_06', 3)	# 64-66
    sprite('Action_277_07', 3)	# 67-69
    sprite('Action_277_06', 3)	# 70-72
    label(1)
    sprite('keep', 1)	# 73-73
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('Action_277_07', 3)	# 74-76
    sprite('Action_277_06', 3)	# 77-79
    sprite('Action_277_07', 3)	# 80-82
    sprite('Action_277_00', 3)	# 83-85

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown23027()

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 1)	# 121-121
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    sprite('Action_110_02', 3)	# 122-124	 **attackbox here**
    sprite('Action_110_03', 3)	# 125-127	 **attackbox here**
    label(1)
    sprite('Action_110_02', 3)	# 128-130	 **attackbox here**
    sprite('Action_110_03', 3)	# 131-133	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 134-136
    Unknown1084(1)
    sprite('Action_110_04', 2)	# 137-138
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    sprite('Action_110_05', 2)	# 139-140
    sprite('Action_110_06', 8)	# 141-148
    sprite('Action_110_07', 4)	# 149-152
    sprite('Action_110_08', 4)	# 153-156
    sprite('Action_110_09', 4)	# 157-160
    sprite('Action_110_10', 2)	# 161-162
    sprite('Action_110_11', 2)	# 163-164

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_02', 3)	# 1-3
    sprite('Action_312_03', 3)	# 4-6
    sprite('Action_312_04', 3)	# 7-9
    sprite('Action_312_05', 27)	# 10-36
    sprite('Action_312_06', 4)	# 37-40
    sprite('Action_312_07', 4)	# 41-44
    sprite('Action_312_08', 4)	# 45-48
    sprite('Action_014_00', 4)	# 49-52
    sprite('Action_014_01', 4)	# 53-56
    sprite('Action_014_02', 4)	# 57-60
    sprite('Action_000_00', 30)	# 61-90	 **attackbox here**

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown11033(2)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_002_00', 4)	# 1-4
    sprite('Action_002_01', 4)	# 5-8
    sprite('Action_002_02', 2)	# 9-10
    Unknown7009(0)
    SFX_3('SE043')
    sprite('Action_002_03', 3)	# 11-13	 **attackbox here**
    GFX_0('Wal_081', 100)
    sprite('Action_002_04', 3)	# 14-16
    Recovery()
    Unknown2063()
    sprite('Action_002_05', 10)	# 17-26
    sprite('Action_002_06', 4)	# 27-30
    sprite('Action_002_07', 4)	# 31-34
    sprite('Action_002_08', 4)	# 35-38

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown11033(2)
        AirUntechableTime(21)
        Unknown9016(1)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_402_00', 7)	# 1-7
    sprite('Action_402_01', 2)	# 8-9
    Unknown7009(1)
    SFX_3('SE043')
    sprite('Action_402_02', 2)	# 10-11	 **attackbox here**
    GFX_0('Wal_082', 100)
    sprite('Action_402_03', 3)	# 12-14
    Recovery()
    Unknown2063()
    sprite('Action_402_04', 10)	# 15-24
    sprite('Action_402_05', 5)	# 25-29
    sprite('Action_402_06', 5)	# 30-34

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1000)
        Unknown11033(2)
        AttackP2(70)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9310(1)
        Hitstop(7)
        AirPushbackY(-100000)

        def upon_78():
            JumpCancel_(0)
            Unknown14077(0)
            enterState('NmlAtk5AAA_Exe')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_106_02', 4)	# 1-4
    sprite('Action_106_03', 4)	# 5-8
    sprite('Action_106_04', 2)	# 9-10
    Unknown7009(0)
    SFX_3('SE043')
    sprite('Action_106_05', 3)	# 11-13	 **attackbox here**
    sprite('Action_106_06', 8)	# 14-21	 **attackbox here**
    GFX_0('Eff_4BShock', 0)
    clearUponHandler(78)
    SFX_3('SE025_BoundBig')
    Unknown11034(0)
    Unknown11033(1)
    ScreenShake(0, 10000)
    sprite('Action_106_07', 4)	# 22-25
    Recovery()
    Unknown2063()
    sprite('Action_106_08', 4)	# 26-29

@State
def NmlAtk5AAA_Exe():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk5AAA_Exe2', 1, 0, 0)
        callSubroutine('Throw2Throw')
    sprite('keep', 1)	# 1-1
    sprite('Action_106_06', 8)	# 2-9	 **attackbox here**
    setInvincible(0)
    Unknown23027()
    GFX_0('Eff_4BShock', 0)
    SFX_3('SE025_BoundBig')
    sprite('Action_106_07', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('Action_106_08', 4)	# 14-17

@State
def NmlAtk5AAA_Exe2():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2500)
        Unknown11091(0)
        AirHitstunAnimation(5)
        GroundedHitstunAnimation(5)
        Unknown11094(1)
        Unknown9154(21)
        AirPushbackX(14000)
        AirPushbackY(-40000)
        Hitstop(15)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('CmnActCrushAttack')
        Unknown2019(500)

        def upon_STATE_END():
            Unknown2019(0)
        Unknown30068(1)
    sprite('Action_107_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(29, 0)
    Unknown5001('0000000004000000040000000400000000000000')
    StartMultihit()
    sprite('Action_107_01', 3)	# 4-6
    Unknown5000(29, 0)
    Unknown5001('0000000004000000040000000400000000000000')
    sprite('Action_107_02', 3)	# 7-9
    Unknown5000(18, 0)
    Unknown5001('0000000004000000040000000400000000000000')
    sprite('Action_107_03', 3)	# 10-12	 **attackbox here**
    Unknown5000(18, 0)
    Unknown5001('0000000004000000040000000400000000000000')
    sprite('Action_107_04', 3)	# 13-15	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000400000000000000')
    sprite('Action_107_05', 6)	# 16-21	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000400000000000000')
    sprite('Action_107_11', 6)	# 22-27	 **attackbox here**
    Unknown7006('uwa165_0', 100, 828471157, 828323126, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000400000000000000')
    sprite('Action_107_12', 6)	# 28-33	 **attackbox here**
    sprite('Action_107_13', 2)	# 34-35	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000400000000000000')
    StartMultihit()
    sprite('Action_107_14', 3)	# 36-38	 **attackbox here**
    ScreenShake(10000, 10000)
    sprite('Action_107_15', 6)	# 39-44
    Recovery()
    Unknown2063()
    sprite('Action_107_16', 3)	# 45-47
    sprite('Action_107_17', 3)	# 48-50

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown11033(2)
        Damage(2000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        JumpCancel_(0)
    sprite('Action_220_00', 6)	# 1-6
    sprite('Action_220_01', 10)	# 7-16
    sprite('Action_220_02', 2)	# 17-18
    GFX_0('Eff_FairdeRuben1', 100)
    GFX_0('Eff_FairdeRuben2', 100)
    Unknown7006('uwa108_0', 100, 828471157, 828323888, 0, 0, 100, 828471157, 845101104, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_220_03', 4)	# 19-22	 **attackbox here**
    GFX_0('Eff_FairdeRuben_Impact', 0)
    SFX_3('SE007')
    sprite('Action_220_04', 4)	# 23-26	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('Action_220_05', 4)	# 27-30	 **attackbox here**
    sprite('Action_220_06', 4)	# 31-34	 **attackbox here**
    sprite('Action_220_07', 4)	# 35-38	 **attackbox here**
    sprite('Action_220_08', 4)	# 39-42	 **attackbox here**
    sprite('Action_220_09', 4)	# 43-46

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown11033(2)
        AirUntechableTime(24)
        Unknown9016(1)
        Unknown1112('')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 4)	# 3-6
    sprite('Action_003_02', 4)	# 7-10
    sprite('Action_003_03', 2)	# 11-12
    Unknown7009(2)
    SFX_3('SE043')
    sprite('Action_003_04', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    GFX_0('Wal_080', 100)
    sprite('Action_003_05', 3)	# 15-17	 **attackbox here**
    sprite('Action_003_05', 3)	# 18-20	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('Action_003_06', 7)	# 21-27
    sprite('Action_003_07', 5)	# 28-32
    sprite('Action_003_08', 4)	# 33-36

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown11033(2)
        Damage(1000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(1800)
        AirUntechableTime(30)
        Unknown9016(1)

        def upon_78():
            JumpCancel_(0)
            Unknown14077(0)
            Unknown13024(0)
            Hitstop(0)
            enterState('NmlAtk5BB_Exe')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_108_00', 4)	# 1-4
    sprite('Action_108_01', 4)	# 5-8
    sprite('Action_108_02', 2)	# 9-10
    Unknown7009(0)
    sprite('Action_108_03', 2)	# 11-12	 **attackbox here**
    GFX_0('Wal_094', 100)
    SFX_3('SE043')
    sprite('Action_108_04', 2)	# 13-14	 **attackbox here**
    physicsXImpulse(-20000)
    Unknown1028(400)
    clearUponHandler(78)
    sprite('Action_108_05', 2)	# 15-16
    sprite('Action_108_06', 2)	# 17-18
    sprite('Action_108_07', 2)	# 19-20
    sprite('Action_108_08', 6)	# 21-26
    Unknown1019(30)
    Unknown1034(30)
    sprite('Action_108_09', 2)	# 27-28
    Unknown1084(1)
    physicsXImpulse(15000)
    sprite('Action_108_10', 2)	# 29-30
    Unknown1019(200)
    sprite('Action_108_11', 2)	# 31-32	 **attackbox here**
    Unknown1019(200)
    GFX_0('Wal_085', 100)
    Unknown7006('uwa106_0', 100, 828471157, 828323376, 0, 0, 100, 828471157, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('SE043')
    sprite('Action_108_12', 8)	# 33-40	 **attackbox here**
    Unknown1019(30)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2000)
    AttackP2(80)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(60000)
    AirPushbackY(12000)
    AirUntechableTime(40)
    WallbounceReboundTime(0)
    sprite('Action_108_13', 7)	# 41-47
    Unknown1084(1)
    Recovery()
    Unknown2063()
    sprite('Action_108_14', 6)	# 48-53

@State
def NmlAtk5BB_Exe():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk5BB_Exe2', 1, 0, 0)
        callSubroutine('Throw2Throw')
    sprite('keep', 1)	# 1-1
    sprite('Action_108_04', 2)	# 2-3	 **attackbox here**
    sprite('Action_108_05', 2)	# 4-5
    sprite('Action_108_06', 2)	# 6-7
    sprite('Action_108_07', 2)	# 8-9
    sprite('Action_108_08', 6)	# 10-15
    sprite('Action_108_09', 2)	# 16-17
    sprite('Action_108_10', 2)	# 18-19
    sprite('Action_108_11', 2)	# 20-21	 **attackbox here**
    GFX_0('Wal_085', 100)
    Unknown7006('uwa106_0', 100, 828471157, 828323376, 0, 0, 100, 828471157, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('SE043')
    sprite('Action_108_12', 8)	# 22-29	 **attackbox here**
    AttackDefaults_StandingNormal()
    AttackLevel_(5)
    Damage(2000)
    AttackP2(80)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(60000)
    AirPushbackY(12000)
    AirUntechableTime(40)
    WallbounceReboundTime(0)
    sprite('Action_108_13', 7)	# 30-36
    Recovery()
    Unknown2063()
    sprite('Action_108_14', 6)	# 37-42

@State
def NmlAtk5BB_Exe2():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        Unknown11091(0)
        Damage(2500)
        AttackP2(80)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(80000)
        AirUntechableTime(44)
        WallbounceReboundTime(20)
        Unknown11001(0, -11, -11)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        Unknown2004(1, 0)
        Unknown20000(1)
        Unknown30068(1)

        def upon_STATE_END():
            Unknown2019(0)
    sprite('Action_109_00', 4)	# 1-4
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_01', 2)	# 5-6
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_02', 4)	# 7-10
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_03', 6)	# 11-16
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_04', 8)	# 17-24
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_05', 4)	# 25-28
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_06', 1)	# 29-29
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_07', 1)	# 30-30
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_08', 1)	# 31-31
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_109_09', 1)	# 32-32	 **attackbox here**
    Unknown5000(29, 0)
    Unknown5001('0000000004000000040000000400000000000000')
    GFX_0('Wal_083', 100)
    StartMultihit()
    Unknown7006('uwa106_0', 100, 828471157, 828323376, 0, 0, 100, 828471157, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('SE043')
    sprite('Action_109_10', 10)	# 33-42	 **attackbox here**
    Unknown20000(0)
    Unknown2019(500)
    sprite('Action_109_11', 6)	# 43-48
    sprite('Action_109_12', 6)	# 49-54

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_112_00', 1)	# 1-1
    sprite('Action_112_01', 2)	# 2-3
    sprite('Action_112_02', 2)	# 4-5
    sprite('Action_112_03', 2)	# 6-7
    Unknown7009(3)
    SFX_3('SE043')
    sprite('Action_112_04', 2)	# 8-9	 **attackbox here**
    sprite('Action_112_05', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('Action_112_06', 6)	# 14-19
    sprite('Action_112_07', 4)	# 20-23

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Unknown11033(2)
        AttackP1(90)
        AttackP2(75)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(32000)
        AirUntechableTime(24)
        Unknown11058('0000000001000000000000000000000000000000')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk2BB')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_006_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_006_01', 4)	# 6-9
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_006_02', 2)	# 10-11
    sprite('Action_006_03', 2)	# 12-13
    Unknown7009(5)
    SFX_3('SE043')
    sprite('Action_006_04', 2)	# 14-15	 **attackbox here**
    GFX_0('Wal_084', 100)
    sprite('Action_006_05', 3)	# 16-18	 **attackbox here**
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('Action_006_06', 6)	# 19-24
    sprite('Action_006_07', 6)	# 25-30
    sprite('Action_006_08', 4)	# 31-34
    sprite('Action_006_09', 4)	# 35-38
    sprite('Action_006_10', 4)	# 39-42
    sprite('Action_006_11', 3)	# 43-45

@State
def NmlAtk2BB():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk2BB_Exe', 1, 0, 0)
        Unknown11054(400000)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11002(-1)
        Unknown11045(0)
        Unknown30061(0)
        Unknown11025(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        HitLow(0)
        HitOverhead(0)
        HitAirUnblockable(0)
        Unknown11033(2)
    sprite('Action_210_00', 4)	# 1-4
    sprite('Action_210_01', 3)	# 5-7
    sprite('Action_210_02', 3)	# 8-10
    Unknown7009(3)
    sprite('Action_210_03', 2)	# 11-12	 **attackbox here**
    GFX_0('Wal_077', 100)
    GFX_0('Wal_078', 100)
    SFX_3('SE043')
    sprite('Action_210_04', 5)	# 13-17	 **attackbox here**
    sprite('Action_210_05', 6)	# 18-23	 **attackbox here**
    sprite('Action_210_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_210_07', 6)	# 28-33	 **attackbox here**
    sprite('Action_210_08', 6)	# 34-39	 **attackbox here**
    sprite('Action_210_09', 5)	# 40-44

@State
def NmlAtk2BB_Exe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        Unknown11091(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11001(20, 20, 20)
        Unknown11072(1, 50000, 510000)
        Unknown11023(1)
        Unknown11064(1)
        JumpCancel_(0)
        Unknown30068(1)
        Unknown28(8, 'NmlAtk2BB_Exe2')
    sprite('Action_211_00', 5)	# 1-5	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_01', 5)	# 6-10	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_02', 5)	# 11-15	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_03', 5)	# 16-20	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_04', 5)	# 21-25	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_05', 5)	# 26-30	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_06', 5)	# 31-35	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_07', 7)	# 36-42	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_08', 2)	# 43-44	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown7009(4)
    sprite('Action_211_09', 1)	# 45-45	 **attackbox here**
    SFX_3('SE007')

@State
def NmlAtk2BB_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk2BB_Exe3', 1, 0, 0)
        callSubroutine('Throw2Throw')
    sprite('keep', 1)	# 1-1

@State
def NmlAtk2BB_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(0)
        AttackP2(75)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(-20000)
        Unknown9310(1)
        AirUntechableTime(60)
        Unknown11001(0, -11, -11)
        Unknown11023(1)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        Unknown30068(1)
    sprite('Action_211_10', 5)	# 1-5	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_11', 7)	# 6-12	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_12', 6)	# 13-18	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_13', 5)	# 19-23	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_14', 5)	# 24-28
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_211_15', 2)	# 29-30
    Unknown5000(27, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown7006('uwa106_0', 100, 828471157, 828323376, 0, 0, 100, 828471157, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_211_16', 1)	# 31-31	 **attackbox here**
    sprite('Action_211_17', 10)	# 32-41
    sprite('Action_211_18', 7)	# 42-48

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Unknown11033(2)
        AttackP1(90)
        AttackP2(75)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(8000)
        AirPushbackY(13000)
        AirUntechableTime(40)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
    sprite('Action_005_00', 5)	# 1-5
    sprite('Action_005_01', 3)	# 6-8
    sprite('Action_005_02', 2)	# 9-10
    Unknown7006('uwa107_0', 100, 828471157, 828323632, 0, 0, 100, 828471157, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('SE043')
    sprite('Action_005_03', 4)	# 11-14	 **attackbox here**
    sprite('Action_005_04', 6)	# 15-20
    Recovery()
    Unknown2063()
    sprite('Action_005_05', 6)	# 21-26
    sprite('Action_005_06', 5)	# 27-31

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown11033(2)
        AirHitstunAnimation(10)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_009_10', 7)	# 1-7	 **attackbox here**
    sprite('Action_009_11', 3)	# 8-10	 **attackbox here**
    sprite('Action_009_12', 2)	# 11-12
    sprite('Action_009_13', 1)	# 13-13	 **attackbox here**
    Unknown7009(1)
    SFX_3('SE043')
    sprite('Action_009_14', 3)	# 14-16	 **attackbox here**
    GFX_0('Wal_076', 100)
    sprite('Action_009_15', 4)	# 17-20	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_009_16', 5)	# 21-25
    sprite('Action_009_17', 5)	# 26-30

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown11033(2)
        AirUntechableTime(20)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_007_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_007_01', 3)	# 4-6
    sprite('Action_007_02', 2)	# 7-8
    Unknown7009(4)
    SFX_3('SE043')
    GFX_0('Wal_088', 100)
    sprite('Action_007_03', 8)	# 9-16	 **attackbox here**
    sprite('Action_007_04', 4)	# 17-20
    Recovery()
    Unknown2063()
    sprite('Action_007_05', 6)	# 21-26
    sprite('Action_007_06', 6)	# 27-32

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Unknown11033(2)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(70000)
        AirPushbackY(36000)
        AirUntechableTime(40)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_111_00', 3)	# 1-3
    sprite('Action_111_01', 3)	# 4-6
    sprite('Action_111_02', 3)	# 7-9
    SFX_3('SE043')
    sprite('Action_111_03', 3)	# 10-12
    Unknown7009(2)
    sprite('Action_111_04', 6)	# 13-18	 **attackbox here**
    sprite('Action_111_05', 6)	# 19-24
    sprite('Action_111_06', 6)	# 25-30
    sprite('Action_111_07', 4)	# 31-34

@Subroutine
def AirAttackBeginCancelDirection():
    SLOT_6 = 1
    loopRelated(17, 4)

    def upon_17():
        clearUponHandler(17)
        SLOT_6 = 0

    def upon_STATE_END():
        if SLOT_6:
            if SLOT_37:
                Unknown2006()
            SLOT_6 = 0

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        Damage(2500)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-60000)
        AirUntechableTime(40)
        Unknown9310(1)
        Unknown23027()
        JumpCancel_(0)
        clearUponHandler(2)
        callSubroutine('AirAttackBeginCancelDirection')
    sprite('Action_110_00', 3)	# 1-3
    sprite('Action_110_01', 3)	# 4-6
    Unknown1015(8000)
    Unknown1019(50)
    physicsYImpulse(35000)
    setGravity(3500)
    Unknown7009(5)
    sendToLabelUpon(2, 9)
    sprite('Action_110_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_110_03', 3)	# 10-12	 **attackbox here**
    sprite('Action_110_02', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_03', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_110_02', 3)	# 19-21	 **attackbox here**
    Unknown1039(110)
    sprite('Action_110_03', 3)	# 22-24	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_110_05', 2)	# 25-26
    Unknown1084(1)
    Unknown4004('6566666563745f32393000000000000000000000000000000000000000000000ffff0000')
    Unknown4004('6566666563745f33373900000000000000000000000000000000000000000000ffff0000')
    Unknown8004(100, 1, 1)
    SFX_3('SE051')
    sprite('Action_110_06', 6)	# 27-32
    sprite('Action_110_07', 4)	# 33-36
    sprite('Action_110_08', 4)	# 37-40
    sprite('Action_110_09', 4)	# 41-44
    sprite('Action_110_10', 2)	# 45-46
    sprite('Action_110_11', 2)	# 47-48

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11033(2)
    sprite('Action_068_00', 3)	# 1-3
    sprite('Action_068_00', 1)	# 4-4
    tag_voice(1, 'uwa156_0', 'uwa156_1', '', '')
    sprite('Action_068_02', 3)	# 5-7
    Unknown1084(1)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    physicsYImpulse(23000)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_068_03', 3)	# 8-10
    tag_voice(1, 'uhy156_0', 'uhy156_1', '', '')
    sprite('Action_068_04', 5)	# 11-15
    sprite('Action_008_00', 5)	# 16-20	 **attackbox here**
    sprite('Action_008_01', 3)	# 21-23
    sprite('Action_008_02', 2)	# 24-25
    SFX_3('SE043')
    sprite('Action_008_03', 3)	# 26-28	 **attackbox here**
    sprite('Action_008_04', 4)	# 29-32	 **attackbox here**
    Unknown23027()
    sprite('Action_008_05', 9)	# 33-41
    sprite('Action_008_06', 4)	# 42-45
    label(0)
    sprite('Action_020_00', 3)	# 46-48	 **attackbox here**
    sprite('Action_020_01', 3)	# 49-51	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 2)	# 52-53
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    SFX_3('SE025_BoundBig')
    sprite('Action_021_01', 6)	# 54-59
    sprite('Action_021_02', 3)	# 60-62
    Unknown18009(0)
    sprite('Action_021_03', 2)	# 63-64

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown23027()
        Unknown9016(1)
        loopRelated(17, 19)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_008_04', 4)	# 1-4	 **attackbox here**
    sprite('Action_008_05', 9)	# 5-13
    sprite('Action_008_06', 4)	# 14-17
    sprite('Action_020_00', 3)	# 18-20	 **attackbox here**
    sprite('Action_020_01', 3)	# 21-23	 **attackbox here**
    label(1)
    sprite('Action_021_00', 2)	# 24-25
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_021_01', 6)	# 26-31
    sprite('Action_021_02', 30)	# 32-61
    label(2)
    sprite('Action_002_00', 4)	# 62-65
    clearUponHandler(17)
    teleportRelativeY(0)
    sprite('Action_002_01', 4)	# 66-69
    sprite('Action_002_02', 2)	# 70-71
    tag_voice(0, 'uwa157_0', 'uwa157_1', '', '')
    SFX_3('SE043')
    sprite('Action_002_03', 3)	# 72-74	 **attackbox here**
    RefreshMultihit()
    GFX_0('Wal_081', 100)
    sprite('Action_002_03', 3)	# 75-77	 **attackbox here**
    Unknown2003(1)
    sprite('Action_002_04', 6)	# 78-83
    sprite('Action_002_03', 4)	# 84-87	 **attackbox here**
    sprite('Action_002_05', 4)	# 88-91
    sprite('Action_002_06', 4)	# 92-95
    sprite('Action_002_07', 4)	# 96-99
    sprite('Action_002_08', 4)	# 100-103
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(0)
    sprite('Action_000_00', 7)	# 104-110	 **attackbox here**
    sprite('Action_000_01', 5)	# 111-115	 **attackbox here**
    sprite('Action_000_02', 12)	# 116-127	 **attackbox here**
    sprite('Action_000_03', 14)	# 128-141	 **attackbox here**
    sprite('Action_000_04', 30)	# 142-171	 **attackbox here**
    sprite('Action_000_05', 9)	# 172-180	 **attackbox here**
    sprite('Action_000_06', 6)	# 181-186	 **attackbox here**
    sprite('Action_000_07', 8)	# 187-194	 **attackbox here**
    sprite('Action_000_08', 14)	# 195-208	 **attackbox here**
    sprite('Action_000_09', 17)	# 209-225	 **attackbox here**
    sprite('Action_000_10', 17)	# 226-242	 **attackbox here**
    sprite('Action_000_11', 12)	# 243-254	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(11)
    sprite('keep', 1)	# 255-255

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 4)	# 3-6
    sprite('Action_003_02', 4)	# 7-10
    sprite('Action_003_03', 2)	# 11-12
    SFX_3('SE043')
    sprite('Action_003_04', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    sprite('Action_003_05', 6)	# 15-20	 **attackbox here**
    sprite('Action_003_06', 7)	# 21-27
    sprite('Action_003_07', 5)	# 28-32
    sprite('Action_003_08', 4)	# 33-36
    label(0)
    sprite('Action_000_00', 7)	# 37-43	 **attackbox here**
    sprite('Action_000_01', 5)	# 44-48	 **attackbox here**
    sprite('Action_000_02', 12)	# 49-60	 **attackbox here**
    sprite('Action_000_03', 14)	# 61-74	 **attackbox here**
    sprite('Action_000_04', 30)	# 75-104	 **attackbox here**
    sprite('Action_000_05', 9)	# 105-113	 **attackbox here**
    sprite('Action_000_06', 6)	# 114-119	 **attackbox here**
    sprite('Action_000_07', 8)	# 120-127	 **attackbox here**
    sprite('Action_000_08', 14)	# 128-141	 **attackbox here**
    sprite('Action_000_09', 17)	# 142-158	 **attackbox here**
    sprite('Action_000_10', 17)	# 159-175	 **attackbox here**
    sprite('Action_000_11', 12)	# 176-187	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 188-188

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('Action_220_00', 6)	# 1-6
    tag_voice(0, 'uwa158_0', 'uwa158_1', '', '')
    sprite('Action_220_01', 11)	# 7-17
    sprite('Action_220_02', 2)	# 18-19
    GFX_0('Eff_FairdeRuben1', 100)
    GFX_0('Eff_FairdeRuben2', 100)
    sprite('Action_220_03', 6)	# 20-25	 **attackbox here**
    GFX_0('Eff_FairdeRuben_Impact', 0)
    SFX_3('SE007')
    sprite('Action_220_04', 4)	# 26-29	 **attackbox here**
    Unknown23027()
    sprite('Action_220_05', 12)	# 30-41	 **attackbox here**
    sprite('Action_220_06', 5)	# 42-46	 **attackbox here**
    sprite('Action_220_07', 5)	# 47-51	 **attackbox here**
    sprite('Action_220_08', 5)	# 52-56	 **attackbox here**
    sprite('Action_220_09', 4)	# 57-60

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
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('Action_068_03', 5)	# 24-28
    physicsXImpulse(28000)
    physicsYImpulse(25000)
    setGravity(2000)
    SFX_0('004_swing_grap_1_2')
    SFX_0('002_highjump_2')

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('Action_009_10', 7)	# 29-35	 **attackbox here**
    sprite('Action_009_11', 3)	# 36-38	 **attackbox here**
    sprite('Action_009_12', 2)	# 39-40
    sprite('Action_009_13', 1)	# 41-41	 **attackbox here**
    SFX_3('SE043')
    sprite('Action_009_14', 3)	# 42-44	 **attackbox here**
    GFX_0('Wal_076', 100)
    sprite('Action_009_15', 4)	# 45-48	 **attackbox here**
    Unknown1019(30)
    sprite('Action_009_16', 5)	# 49-53
    Unknown1019(30)
    sprite('Action_009_17', 5)	# 54-58
    sprite('Action_035_06', 3)	# 59-61
    label(0)
    sprite('Action_020_00', 3)	# 62-64	 **attackbox here**
    sprite('Action_020_01', 3)	# 65-67	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('Action_021_00', 2)	# 68-69
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_021_01', 4)	# 70-73
    sprite('Action_021_02', 3)	# 74-76
    sprite('Action_021_03', 3)	# 77-79
    sprite('Action_000_00', 7)	# 80-86	 **attackbox here**
    sprite('Action_000_01', 5)	# 87-91	 **attackbox here**
    sprite('Action_000_02', 12)	# 92-103	 **attackbox here**
    sprite('Action_000_03', 14)	# 104-117	 **attackbox here**
    sprite('Action_000_04', 30)	# 118-147	 **attackbox here**
    sprite('Action_000_05', 9)	# 148-156	 **attackbox here**
    sprite('Action_000_06', 6)	# 157-162	 **attackbox here**
    sprite('Action_000_07', 8)	# 163-170	 **attackbox here**
    sprite('Action_000_08', 14)	# 171-184	 **attackbox here**
    sprite('Action_000_09', 17)	# 185-201	 **attackbox here**
    sprite('Action_000_10', 17)	# 202-218	 **attackbox here**
    sprite('Action_000_11', 12)	# 219-230	 **attackbox here**

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('Action_001_00', 5)	# 1-5
    sprite('Action_001_01', 4)	# 6-9
    sprite('Action_001_02', 2)	# 10-11
    SFX_3('SE043')
    sprite('Action_001_03', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_001_04', 7)	# 15-21
    sprite('Action_001_05', 8)	# 22-29
    sprite('Action_001_06', 4)	# 30-33
    sprite('Action_000_00', 7)	# 34-40	 **attackbox here**
    sprite('Action_000_01', 5)	# 41-45	 **attackbox here**
    sprite('Action_000_02', 12)	# 46-57	 **attackbox here**
    sprite('Action_000_03', 14)	# 58-71	 **attackbox here**
    sprite('Action_000_04', 30)	# 72-101	 **attackbox here**
    sprite('Action_000_05', 9)	# 102-110	 **attackbox here**
    sprite('Action_000_06', 6)	# 111-116	 **attackbox here**
    sprite('Action_000_07', 8)	# 117-124	 **attackbox here**
    sprite('Action_000_08', 14)	# 125-138	 **attackbox here**
    sprite('Action_000_09', 17)	# 139-155	 **attackbox here**
    sprite('Action_000_10', 17)	# 156-172	 **attackbox here**
    sprite('Action_000_11', 12)	# 173-184	 **attackbox here**

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('Action_220_00', 6)	# 1-6
    sprite('Action_220_01', 11)	# 7-17
    sprite('Action_220_02', 2)	# 18-19
    GFX_0('Eff_FairdeRuben1', 100)
    GFX_0('Eff_FairdeRuben2', 100)
    sprite('Action_220_03', 6)	# 20-25	 **attackbox here**
    GFX_0('Eff_FairdeRuben_Impact', 0)
    SFX_3('SE007')
    sprite('Action_220_04', 4)	# 26-29	 **attackbox here**
    Unknown23027()
    sprite('Action_220_05', 12)	# 30-41	 **attackbox here**
    sprite('Action_220_06', 5)	# 42-46	 **attackbox here**
    sprite('Action_220_07', 5)	# 47-51	 **attackbox here**
    sprite('Action_220_08', 5)	# 52-56	 **attackbox here**
    sprite('Action_220_09', 4)	# 57-60

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('Action_045_00', 8)	# 1-8
    sprite('Action_045_01', 4)	# 9-12
    Unknown8006(100, 0, 1)
    physicsXImpulse(25000)
    Unknown1028(-1000)
    Unknown1045(9000)
    teleportRelativeX(50000)
    Unknown8007(100, 1, 1)
    sprite('Action_045_02', 4)	# 13-16
    sprite('Action_045_01', 4)	# 17-20
    Unknown8006(100, 1, 0)
    sprite('Action_045_02', 4)	# 21-24
    sprite('Action_045_04', 4)	# 25-28
    Unknown8010(100, 1, 1)
    Unknown1019(50)
    sprite('Action_045_04', 4)	# 29-32
    Unknown1084(1)
    label(1)
    sprite('Action_055_00', 3)	# 33-35
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 36-38	 **attackbox here**
    Unknown1084(1)
    sprite('Action_055_02', 4)	# 39-42
    SFX_3('SE043')
    sprite('Action_055_03', 2)	# 43-44
    SFX_1('uwa154')
    sprite('Action_055_04', 2)	# 45-46
    sprite('Action_055_05', 10)	# 47-56
    sprite('Action_055_06', 5)	# 57-61

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        Damage(0)
        AttackP2(50)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(42000)
        AirPushbackY(-26000)
        Unknown9310(15)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11072(1, 400000, 100000)
        Unknown11050('0800000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11080(1)
        JumpCancel_(0)
    sprite('Action_056_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_056_01', 6)	# 4-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_00', 3)	# 10-12
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_057_01', 3)	# 13-15
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_057_02', 7)	# 16-22
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_057_03', 7)	# 23-29
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_057_04', 2)	# 30-31
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_1('uwa153')
    sprite('Action_057_05', 2)	# 32-33	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('Action_057_06', 3)	# 34-36	 **attackbox here**
    sprite('Action_057_06', 4)	# 37-40	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    Unknown9071()
    Unknown9190(1)
    Unknown11072(0, 400000, 100000)
    Unknown11080(0)
    clearUponHandler(78)

    def upon_78():
        JumpCancel_(1)
    sprite('Action_057_07', 6)	# 41-46	 **attackbox here**
    SFX_3('SE051')
    sprite('Action_057_08', 6)	# 47-52
    sprite('Action_057_09', 6)	# 53-58
    sprite('Action_057_10', 6)	# 59-64

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('Action_045_00', 8)	# 1-8
    sprite('Action_045_01', 4)	# 9-12
    Unknown8006(100, 0, 1)
    physicsXImpulse(25000)
    Unknown1028(-1000)
    Unknown1045(9000)
    teleportRelativeX(50000)
    Unknown8007(100, 1, 1)
    sprite('Action_045_02', 4)	# 13-16
    sprite('Action_045_01', 4)	# 17-20
    Unknown8006(100, 1, 0)
    sprite('Action_045_02', 4)	# 21-24
    sprite('Action_045_04', 4)	# 25-28
    Unknown8010(100, 1, 1)
    Unknown1019(50)
    sprite('Action_045_04', 4)	# 29-32
    Unknown1084(1)
    label(1)
    sprite('Action_055_00', 3)	# 33-35
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 36-38	 **attackbox here**
    Unknown1084(1)
    sprite('Action_055_02', 4)	# 39-42
    SFX_3('SE043')
    sprite('Action_055_03', 2)	# 43-44
    SFX_1('uwa154')
    sprite('Action_055_04', 2)	# 45-46
    sprite('Action_055_05', 10)	# 47-56
    sprite('Action_055_06', 5)	# 57-61

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        Damage(0)
        AttackP2(50)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(42000)
        AirPushbackY(-26000)
        Unknown9310(15)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11072(1, 400000, 100000)
        Unknown11050('0800000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11080(1)
        JumpCancel_(0)
    sprite('Action_056_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_056_01', 6)	# 4-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_00', 3)	# 10-12
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000001000000')
    sprite('Action_057_01', 3)	# 13-15
    Unknown2005()
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000001000000')
    sprite('Action_057_02', 7)	# 16-22
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_057_03', 7)	# 23-29
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_057_04', 2)	# 30-31
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_1('uwa153')
    sprite('Action_057_05', 2)	# 32-33	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('Action_057_06', 3)	# 34-36	 **attackbox here**
    sprite('Action_057_06', 4)	# 37-40	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    Unknown9071()
    Unknown9190(1)
    Unknown11072(0, 400000, 100000)
    Unknown11080(0)
    clearUponHandler(78)

    def upon_78():
        JumpCancel_(1)
    sprite('Action_057_07', 6)	# 41-46	 **attackbox here**
    SFX_3('SE051')
    sprite('Action_057_08', 6)	# 47-52
    sprite('Action_057_09', 6)	# 53-58
    sprite('Action_057_10', 6)	# 59-64

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Unknown11033(2)
        Damage(1500)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        PushbackX(19800)

        def upon_78():
            if Unknown48('190000000200000000000000160000000200000025000000'):
                enterState('CmnActInvincibleAttack_Exe')
    sprite('Action_220_00', 8)	# 1-8
    sprite('Action_220_01', 11)	# 9-19
    tag_voice(1, 'uwa210_0', 'uwa210_1', 'uwa210_2', '')
    sprite('Action_220_02', 2)	# 20-21
    GFX_0('Eff_FairdeRuben1', 100)
    GFX_0('Eff_FairdeRuben2', 100)
    sprite('Action_220_03', 4)	# 22-25	 **attackbox here**
    GFX_0('Eff_FairdeRuben_Impact', 0)
    SFX_3('SE007')
    sprite('Action_220_04', 4)	# 26-29	 **attackbox here**
    StartMultihit()
    setInvincible(0)
    sprite('Action_220_05', 15)	# 30-44	 **attackbox here**
    sprite('Action_220_06', 8)	# 45-52	 **attackbox here**
    sprite('Action_220_07', 6)	# 53-58	 **attackbox here**
    sprite('Action_220_08', 6)	# 59-64	 **attackbox here**
    sprite('Action_220_09', 6)	# 65-70

@State
def CmnActInvincibleAttack_Exe():

    def upon_IMMEDIATE():
        Unknown17011('CmnActInvincibleAttack_Exe2', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('CmnActInvincibleAttack_Exe2')
        JumpCancel_(0)
        Unknown14083(0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('keep', 1)	# 1-1
    sprite('Action_220_04', 4)	# 2-5	 **attackbox here**
    sprite('Action_220_05', 12)	# 6-17	 **attackbox here**
    sprite('Action_220_06', 6)	# 18-23	 **attackbox here**
    sprite('Action_220_07', 6)	# 24-29	 **attackbox here**
    sprite('Action_220_08', 6)	# 30-35	 **attackbox here**
    sprite('Action_220_09', 6)	# 36-41

@State
def CmnActInvincibleAttack_Exe2():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Damage(1500)
        Unknown11091(5)
        Unknown30065(100)
        Unknown11069('CmnActInvincibleAttack_Exe3')
        Unknown23027()
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
        Unknown28(8, 'CmnActInvincibleAttack_Exe3')
    sprite('Action_222_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_01', 6)	# 4-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_02', 2)	# 10-11	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_03', 5)	# 12-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_04', 8)	# 17-24	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_05', 5)	# 25-29	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_06', 3)	# 30-32	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_07', 10)	# 33-42	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_08', 7)	# 43-49	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    tag_voice(0, 'uwa211_0', 'uwa211_1', 'uwa211_2', '')
    sprite('Action_222_09', 1)	# 50-50
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_10', 1)	# 51-51
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_11', 1)	# 52-52	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    GFX_0('Wal_074', 0)

@State
def CmnActInvincibleAttack_Exe3():

    def upon_IMMEDIATE():
        Unknown17011('CmnActInvincibleAttack_Exe4', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('CmnActInvincibleAttack_Exe4')
        Unknown14083(0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('keep', 1)	# 1-1

@State
def CmnActInvincibleAttack_Exe4():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Damage(2000)
        Hitstop(20)
        Unknown11072(1, 700000, -200000)
        Unknown11064(0)
        Unknown11091(5)
        Unknown30065(100)
        Unknown23027()
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
        Unknown23072()
    sprite('Action_222_12', 6)	# 1-6	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_13', 8)	# 7-14	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_14', 2)	# 15-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_222_15', 3)	# 17-19	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_150_11', 4)	# 20-23	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_150_12', 3)	# 24-26	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_150_13', 2)	# 27-28
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    tag_voice(0, 'uwa212_0', 'uwa212_1', 'uwa212_2', '')
    sprite('Action_150_14', 5)	# 29-33	 **attackbox here**
    RefreshMultihit()
    Unknown13024(1)
    Unknown2005()
    GFX_0('Wal_074', 0)
    sprite('Action_150_15', 5)	# 34-38	 **attackbox here**
    sprite('Action_150_16', 5)	# 39-43	 **attackbox here**
    sprite('Action_150_17', 5)	# 44-48	 **attackbox here**
    sprite('Action_150_18', 7)	# 49-55
    sprite('Action_150_19', 10)	# 56-65
    sprite('Action_150_20', 5)	# 66-70
    sprite('Action_150_21', 4)	# 71-74
    sprite('Action_150_22', 3)	# 75-77
    sprite('Action_150_23', 2)	# 78-79

@State
def AssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown11033(2)
        Damage(2200)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(-40000)
        AirUntechableTime(30)
        Unknown9310(1)
    sprite('Action_264_00', 3)	# 1-3
    sprite('Action_264_01', 3)	# 4-6
    teleportRelativeX(60000)
    Unknown12046(60)
    Unknown7006('uwa200_0', 100, 845248373, 828321840, 0, 0, 100, 845248373, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_264_02', 2)	# 7-8
    teleportRelativeX(60000)
    sprite('Action_264_03', 2)	# 9-10
    teleportRelativeX(60000)
    sprite('Action_264_04', 2)	# 11-12	 **attackbox here**
    teleportRelativeX(60000)
    GFX_0('Eff_EisenNagel', 100)
    sprite('Action_264_05', 2)	# 13-14
    teleportRelativeX(60000)
    sprite('Action_264_06', 3)	# 15-17	 **attackbox here**
    teleportRelativeX(60000)
    SFX_3('SE051')
    sprite('Action_264_07', 6)	# 18-23
    Recovery()
    Unknown2063()
    teleportRelativeX(25000)
    sprite('Action_264_08', 6)	# 24-29
    sprite('Action_264_09', 5)	# 30-34
    sprite('Action_264_10', 5)	# 35-39
    sprite('Action_264_11', 5)	# 40-44

@State
def AssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown11033(2)
        Damage(1200)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(12000)
        AirUntechableTime(60)
        Unknown9016(1)
        Hitstop(2)
    sprite('Action_277_00', 2)	# 1-2
    sprite('Action_277_02', 2)	# 3-4
    sprite('Action_277_03', 4)	# 5-8
    sprite('Action_277_04', 2)	# 9-10
    sprite('Action_275_00', 2)	# 11-12
    sprite('Action_275_01', 2)	# 13-14
    GFX_0('Eff_Wirbelwind01', 100)
    Unknown12046(60)
    Unknown7006('uwa202_0', 100, 845248373, 828322352, 0, 0, 100, 845248373, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_275_02', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(40000)
    SFX_3('SE051')
    sprite('Action_275_03', 5)	# 18-22
    teleportRelativeX(40000)
    sprite('Action_275_04', 2)	# 23-24
    teleportRelativeX(40000)
    sprite('Action_275_05', 2)	# 25-26
    GFX_0('Eff_Wirbelwind02', 100)
    teleportRelativeX(80000)
    sprite('Action_275_06', 4)	# 27-30	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(80000)
    SFX_3('SE051')
    sprite('Action_275_07', 4)	# 31-34
    teleportRelativeX(40000)
    sprite('Action_275_08', 4)	# 35-38
    teleportRelativeX(40000)
    sprite('Action_275_09', 2)	# 39-40
    GFX_0('Eff_Wirbelwind03', 100)
    teleportRelativeX(80000)
    sprite('Action_275_10', 5)	# 41-45	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(20000)
    Unknown9083()
    Hitstop(12)
    ScreenShake(5000, 10000)
    SFX_3('SE051')
    sprite('Action_275_11', 15)	# 46-60
    sprite('Action_275_12', 6)	# 61-66
    sprite('Action_275_13', 6)	# 67-72

@State
def AssaultC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown11033(2)
        Damage(1200)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(12000)
        AirUntechableTime(60)
        Unknown9016(1)
        Hitstop(2)
        Unknown11091(10)
        Unknown30065(0)
    sprite('Action_277_00', 2)	# 1-2
    sprite('Action_277_02', 1)	# 3-3
    sprite('Action_277_02', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_277_03', 4)	# 5-8
    sprite('Action_277_04', 2)	# 9-10
    sprite('Action_277_12', 2)	# 11-12
    sprite('Action_277_13', 2)	# 13-14
    GFX_0('Eff_Wirbelwind01', 100)
    Unknown12046(60)
    Unknown7006('uwa203_0', 100, 845248373, 828322608, 0, 0, 100, 845248373, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_277_14', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(40000)
    SFX_3('SE051')
    sprite('Action_277_15', 2)	# 17-18
    teleportRelativeX(40000)
    sprite('Action_277_16', 5)	# 19-23
    teleportRelativeX(40000)
    sprite('Action_277_17', 3)	# 24-26
    GFX_0('Eff_Wirbelwind02', 100)
    teleportRelativeX(80000)
    sprite('Action_277_18', 2)	# 27-28
    teleportRelativeX(80000)
    sprite('Action_277_19', 2)	# 29-30	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(40000)
    SFX_3('SE051')
    sprite('Action_277_20', 2)	# 31-32
    teleportRelativeX(40000)
    sprite('Action_277_21', 4)	# 33-36
    teleportRelativeX(80000)
    sprite('Action_277_22', 3)	# 37-39
    sprite('Action_277_23', 2)	# 40-41
    GFX_0('Eff_Wirbelwind03', 100)
    sprite('Action_277_24', 2)	# 42-43	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(20000)
    Unknown9083()
    Hitstop(12)
    SFX_3('SE051')
    sprite('Action_277_25', 2)	# 44-45
    sprite('Action_277_26', 4)	# 46-49
    sprite('Action_277_27', 2)	# 50-51
    GFX_0('Eff_Wirbelwind04', 100)
    Unknown7006('uwa204_0', 100, 845248373, 828322864, 0, 0, 100, 845248373, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_277_28', 4)	# 52-55	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(40000)
    AirPushbackY(-40000)
    Unknown9310(1)
    ScreenShake(5000, 10000)
    SFX_3('SE051')
    sprite('Action_277_29', 8)	# 56-63
    sprite('Action_277_30', 2)	# 64-65
    sprite('Action_277_31', 7)	# 66-72
    sprite('Action_277_32', 5)	# 73-77

@State
def CommandThrowA():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowA_Exe', 2, 0, 0)
        Unknown11054(150000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
    sprite('Action_055_00', 3)	# 1-3
    sprite('Action_055_01', 2)	# 4-5	 **attackbox here**
    StartMultihit()
    sprite('Action_055_02', 2)	# 6-7
    sprite('Action_055_03ex', 2)	# 8-9	 **attackbox here**
    sprite('Action_055_04', 6)	# 10-15
    SFX_1('uwa154')
    SFX_3('SE043')
    sprite('Action_055_05', 11)	# 16-26
    sprite('Action_055_06', 8)	# 27-34
    sprite('Action_055_07', 8)	# 35-42

@State
def CommandThrowA_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Unknown11069('CommandThrowA_Exe2')
        Unknown23027()
        Unknown28(78, 'CommandThrowA_Exe2')
    sprite('Action_056_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_056_01', 6)	# 4-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_455_00', 3)	# 10-12	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown7006('uwa205_0', 100, 845248373, 828323120, 0, 0, 100, 845248373, 845100336, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_455_01', 6)	# 13-18	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_02', 3)	# 19-21	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_05', 3)	# 22-24	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown11091(5)
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    Unknown36(1)
    teleportRelativeY(0)
    Unknown35()

@State
def CommandThrowA_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowA_Exe3', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('CommandThrowA_Exe3')
    sprite('keep', 1)	# 1-1

@State
def CommandThrowA_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('GuruX2Throw')
        Damage(3000)
        Unknown11091(5)
        AttackP2(50)
        Unknown20000(0)
        Unknown20007(0)
    sprite('Action_455_06', 2)	# 1-2	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_07', 2)	# 3-4	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_08', 2)	# 5-6	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_09', 2)	# 7-8	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    physicsXImpulse(10000)
    physicsYImpulse(80000)
    setGravity(3000)
    sprite('Action_455_10', 1)	# 9-9	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_11', 1)	# 10-10
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_12', 3)	# 11-13
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(1)
    sprite('Action_455_13', 3)	# 14-16
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    GFX_0('Eff_DrehenDurchbohren_Spin', 100)
    Unknown20000(1)
    sprite('Action_455_14', 3)	# 17-19
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_15', 3)	# 20-22
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_16', 3)	# 23-25
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 2)	# 26-27
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 2)	# 28-29
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 2)	# 30-31
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 2)	# 32-33
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 1)	# 34-34
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 1)	# 35-35
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 1)	# 36-36
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 1)	# 37-37
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 2)	# 38-39
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 2)	# 40-41
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 2)	# 42-43
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 2)	# 44-45
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 3)	# 46-48
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 3)	# 49-51
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 3)	# 52-54
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    sprite('Action_455_29', 3)	# 55-57	 **attackbox here**
    RefreshMultihit()
    teleportRelativeY(0)
    teleportRelativeX(50000)
    Unknown1084(1)
    Unknown13024(1)
    Unknown3029(0)
    Unknown26('Eff_DrehenDurchbohren_Spin')
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    sprite('Action_455_30', 1)	# 58-58
    Unknown20000(0)
    sprite('Action_455_31', 2)	# 59-60
    sprite('Action_455_32', 4)	# 61-64
    sprite('Action_455_33', 3)	# 65-67
    physicsXImpulse(-12000)
    physicsYImpulse(24000)
    Unknown1043()
    sprite('Action_455_34', 4)	# 68-71
    sprite('Action_455_35', 4)	# 72-75
    label(2)
    sprite('Action_020_00', 3)	# 76-78	 **attackbox here**
    sprite('Action_020_01', 3)	# 79-81	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('Action_455_38', 3)	# 82-84
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_455_39', 3)	# 85-87
    sprite('Action_455_40', 3)	# 88-90
    sprite('Action_455_41', 3)	# 91-93
    sprite('Action_455_42', 3)	# 94-96

@State
def CommandThrowB():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowB_Exe', 2, 0, 0)
        Unknown11054(300000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
    sprite('Action_451_00', 6)	# 1-6
    sprite('Action_451_01', 6)	# 7-12
    sprite('Action_451_02', 2)	# 13-14	 **attackbox here**
    sprite('Action_451_03', 7)	# 15-21	 **attackbox here**
    SFX_1('uwa154')
    SFX_3('SE043')
    sprite('Action_451_04', 7)	# 22-28	 **attackbox here**
    sprite('Action_451_05', 7)	# 29-35	 **attackbox here**
    sprite('Action_451_06', 7)	# 36-42	 **attackbox here**
    sprite('Action_451_07', 4)	# 43-46	 **attackbox here**
    sprite('Action_451_08', 4)	# 47-50

@State
def CommandThrowB_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Unknown11069('CommandThrowB_Exe2')
        Unknown23027()
        Unknown28(78, 'CommandThrowB_Exe2')
    sprite('Action_454_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_01', 6)	# 4-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_02', 2)	# 10-11	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_03', 5)	# 12-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_04', 8)	# 17-24	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_05', 3)	# 25-27	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_455_00', 3)	# 28-30	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown7006('uwa205_0', 100, 845248373, 828323120, 0, 0, 100, 845248373, 845100336, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_455_01', 6)	# 31-36	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_02', 3)	# 37-39	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_05', 3)	# 40-42	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown11091(5)
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    Unknown36(1)
    teleportRelativeY(0)
    Unknown35()

@State
def CommandThrowB_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowB_Exe3', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('CommandThrowB_Exe3')
    sprite('keep', 1)	# 1-1

@State
def CommandThrowB_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('GuruX2Throw')
        Damage(3500)
        Unknown11091(5)
        AttackP2(50)
        Unknown20000(0)
        Unknown20007(0)
    sprite('Action_455_06', 2)	# 1-2	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_07', 2)	# 3-4	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_08', 2)	# 5-6	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_09', 2)	# 7-8	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    physicsXImpulse(20000)
    physicsYImpulse(80000)
    setGravity(3000)
    sprite('Action_455_10', 1)	# 9-9	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_11', 1)	# 10-10
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_12', 3)	# 11-13
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(1)
    sprite('Action_455_13', 3)	# 14-16
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    GFX_0('Eff_DrehenDurchbohren_Spin', 100)
    Unknown20000(1)
    sprite('Action_455_14', 3)	# 17-19
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_15', 3)	# 20-22
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_16', 3)	# 23-25
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 2)	# 26-27
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 2)	# 28-29
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 2)	# 30-31
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 2)	# 32-33
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 1)	# 34-34
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 1)	# 35-35
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 1)	# 36-36
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 1)	# 37-37
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 2)	# 38-39
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 2)	# 40-41
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 2)	# 42-43
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 2)	# 44-45
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 3)	# 46-48
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 3)	# 49-51
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 3)	# 52-54
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    sprite('Action_455_29', 3)	# 55-57	 **attackbox here**
    RefreshMultihit()
    teleportRelativeY(0)
    teleportRelativeX(50000)
    Unknown1084(1)
    Unknown13024(1)
    Unknown3029(0)
    Unknown26('Eff_DrehenDurchbohren_Spin')
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    sprite('Action_455_30', 1)	# 58-58
    Unknown20000(0)
    sprite('Action_455_31', 2)	# 59-60
    sprite('Action_455_32', 4)	# 61-64
    sprite('Action_455_33', 3)	# 65-67
    physicsXImpulse(-12000)
    physicsYImpulse(24000)
    Unknown1043()
    sprite('Action_455_34', 4)	# 68-71
    sprite('Action_455_35', 4)	# 72-75
    label(2)
    sprite('Action_020_00', 3)	# 76-78	 **attackbox here**
    sprite('Action_020_01', 3)	# 79-81	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('Action_455_38', 3)	# 82-84
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_455_39', 3)	# 85-87
    sprite('Action_455_40', 3)	# 88-90
    sprite('Action_455_41', 3)	# 91-93
    sprite('Action_455_42', 3)	# 94-96

@State
def CommandThrowC():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowC_Exe', 2, 0, 0)
        Unknown11054(300000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11025(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11091(10)
    sprite('Action_451_00', 3)	# 1-3
    sprite('Action_451_00', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_451_01', 6)	# 7-12
    sprite('Action_451_02', 2)	# 13-14	 **attackbox here**
    sprite('Action_451_03', 7)	# 15-21	 **attackbox here**
    SFX_1('uwa154')
    SFX_3('SE043')
    sprite('Action_451_04', 7)	# 22-28	 **attackbox here**
    sprite('Action_451_05', 7)	# 29-35	 **attackbox here**
    sprite('Action_451_06', 7)	# 36-42	 **attackbox here**
    sprite('Action_451_07', 4)	# 43-46	 **attackbox here**
    sprite('Action_451_08', 4)	# 47-50

@State
def CommandThrowC_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Damage(500)
        Unknown30065(0)
        Hitstop(0)
        Unknown11069('CommandThrowC_Exe2')
        Unknown23027()
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown28(78, 'CommandThrowC_Exe2')
    sprite('Action_454_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_01', 6)	# 4-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_02', 2)	# 10-11	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_03', 5)	# 12-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_04', 8)	# 17-24	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_05', 3)	# 25-27	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_455_00', 3)	# 28-30	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    tag_voice(1, 'uwa206_0', 'uwa206_1', 'uwa206_2', '')
    sprite('Action_455_01', 6)	# 31-36	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_02', 3)	# 37-39	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_05', 3)	# 40-42	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown11091(10)
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    Unknown36(1)
    teleportRelativeY(0)
    Unknown35()

@State
def CommandThrowC_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowC_Exe3', 2, 0, 0)
        callSubroutine('Throw2Throw')
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown11069('CommandThrowC_Exe3')
        Unknown11091(10)
    sprite('keep', 1)	# 1-1

@State
def CommandThrowC_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Damage(500)
        Unknown30065(0)
        Unknown11069('CommandThrowC_Exe4')
        Unknown23027()
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown28(78, 'CommandThrowC_Exe4')
    sprite('Action_455_06', 2)	# 1-2	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_07', 2)	# 3-4	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_056_01', 6)	# 5-10	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_455_00', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_01', 6)	# 14-19	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_02', 3)	# 20-22	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_05', 3)	# 23-25	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown11091(10)
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    Unknown36(1)
    teleportRelativeY(0)
    Unknown35()

@State
def CommandThrowC_Exe4():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowC_Exe5', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('CommandThrowC_Exe5')
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown11091(10)
    sprite('keep', 1)	# 1-1

@State
def CommandThrowC_Exe5():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('GuruX2Throw')
        Damage(500)
        Hitstop(8)
        Unknown11050('020000004566665f4c616e64536c616d5468726f77000000000000000000000000000000')
        Unknown11064(1)
        Unknown30065(0)
        Unknown11069('CommandThrowC_Exe6')
        JumpCancel_(0)
        Unknown14083(0)
        Unknown20000(1)
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown28(78, 'CommandThrowC_Exe6')
    sprite('Action_455_06', 2)	# 1-2	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_07', 2)	# 3-4	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_08', 2)	# 5-6	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_09', 2)	# 7-8	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    physicsXImpulse(10000)
    physicsYImpulse(50000)
    setGravity(3000)
    sprite('Action_455_10', 1)	# 9-9	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_11', 1)	# 10-10
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_12', 3)	# 11-13
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(1)
    sprite('Action_455_13', 3)	# 14-16
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    GFX_0('Eff_DrehenDurchbohren_Spin', 100)
    sprite('Action_455_14', 3)	# 17-19
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_15', 3)	# 20-22
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_16', 3)	# 23-25
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 1)	# 26-26
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 1)	# 27-27
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 1)	# 28-28
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 1)	# 29-29
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 3)	# 30-32
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 3)	# 33-35
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 3)	# 36-38
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    sprite('Action_458_42', 3)	# 39-41	 **attackbox here**
    RefreshMultihit()
    Unknown11091(10)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown26('Eff_DrehenDurchbohren_Spin')

@State
def CommandThrowC_Exe6():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowC_Exe7', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('CommandThrowC_Exe7')
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown11091(10)
    sprite('keep', 1)	# 1-1

@State
def CommandThrowC_Exe7():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('GuruX2Throw')
        Damage(1000)
        Hitstop(12)
        Unknown11050('020000004566665f4c616e64536c616d5468726f77000000000000000000000000000000')
        Unknown11064(1)
        Unknown30065(0)
        Unknown11069('CommandThrowC_Exe8')
        JumpCancel_(0)
        Unknown14083(0)
        Unknown20000(1)
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown28(78, 'CommandThrowC_Exe8')
    sprite('Action_455_08', 2)	# 1-2	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_09', 2)	# 3-4	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    physicsXImpulse(15000)
    physicsYImpulse(50000)
    setGravity(3000)
    sprite('Action_455_10', 1)	# 5-5	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_11', 1)	# 6-6
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_12', 3)	# 7-9
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(1)
    sprite('Action_455_13', 3)	# 10-12
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    GFX_0('Eff_DrehenDurchbohren_Spin', 100)
    sprite('Action_455_14', 3)	# 13-15
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_15', 3)	# 16-18
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_16', 3)	# 19-21
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 1)	# 22-22
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 1)	# 23-23
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 1)	# 24-24
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 1)	# 25-25
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 3)	# 26-28
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 3)	# 29-31
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 3)	# 32-34
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    sprite('Action_458_42', 3)	# 35-37	 **attackbox here**
    RefreshMultihit()
    Unknown11091(10)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown26('Eff_DrehenDurchbohren_Spin')

@State
def CommandThrowC_Exe8():

    def upon_IMMEDIATE():
        Unknown17011('CommandThrowC_Exe9', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('CommandThrowC_Exe9')
        callSubroutine('Eff_ExSkill_AfterImage')
        Unknown11091(10)
    sprite('keep', 1)	# 1-1

@State
def CommandThrowC_Exe9():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('GuruX2Throw')
        Damage(2500)
        AttackP2(50)
        Unknown11050('020000004566665f44726568656e4475726368626f6872656e5f426967426f6d62000000')
        Unknown30065(0)
        Unknown20000(0)
        Unknown20007(0)
        callSubroutine('Eff_ExSkill_AfterImage')
    sprite('Action_455_08', 2)	# 1-2	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_09', 2)	# 3-4	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    physicsXImpulse(20000)
    physicsYImpulse(80000)
    setGravity(3000)
    sprite('Action_455_10', 1)	# 5-5	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_11', 1)	# 6-6
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_12', 3)	# 7-9
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(1)
    sprite('Action_455_13', 3)	# 10-12
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    GFX_0('Eff_DrehenDurchbohren_Spin', 100)
    Unknown20000(1)
    sprite('Action_455_14', 3)	# 13-15
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_15', 3)	# 16-18
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_16', 3)	# 19-21
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 2)	# 22-23
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 2)	# 24-25
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 2)	# 26-27
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 2)	# 28-29
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 1)	# 30-30
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 1)	# 31-31
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 1)	# 32-32
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 1)	# 33-33
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 2)	# 34-35
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 2)	# 36-37
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 2)	# 38-39
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_20', 2)	# 40-41
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_17', 3)	# 42-44
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_18', 3)	# 45-47
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    SFX_3('SE048_LongSwingC')
    sprite('Action_455_19', 3)	# 48-50
    Unknown5000(11, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    sprite('Action_455_29', 3)	# 51-53	 **attackbox here**
    teleportRelativeY(0)
    teleportRelativeX(50000)
    RefreshMultihit()
    Unknown11091(10)
    Unknown3029(0)
    Unknown1084(1)
    Unknown13024(1)
    Unknown26('Eff_DrehenDurchbohren_Spin')
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    sprite('Action_455_30', 1)	# 54-54
    Unknown20000(0)
    sprite('Action_455_31', 2)	# 55-56
    sprite('Action_455_32', 4)	# 57-60
    sprite('Action_455_33', 3)	# 61-63
    physicsXImpulse(-12000)
    physicsYImpulse(24000)
    Unknown1043()
    sprite('Action_455_34', 4)	# 64-67
    sprite('Action_455_35', 4)	# 68-71
    label(2)
    sprite('Action_020_00', 3)	# 72-74	 **attackbox here**
    sprite('Action_020_01', 3)	# 75-77	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('Action_455_38', 3)	# 78-80
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_455_39', 3)	# 81-83
    sprite('Action_455_40', 3)	# 84-86
    sprite('Action_455_41', 3)	# 87-89
    sprite('Action_455_42', 3)	# 90-92

@State
def AirCommandThrowA():

    def upon_IMMEDIATE():
        Unknown17011('AirCommandThrowA_Exe', 2, 1, 0)
        Unknown11054(300000)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        clearUponHandler(2)
        callSubroutine('AirAttackBeginCancelDirection')
    sprite('Action_144_00', 3)	# 1-3
    sprite('Action_144_00', 3)	# 4-6
    Unknown28(2, 'CmnActJumpLanding')
    Unknown1019(30)
    physicsYImpulse(8000)
    SFX_3('SE043')
    sprite('Action_144_01', 3)	# 7-9	 **attackbox here**
    Unknown22004(10, 1)
    sprite('Action_144_02', 4)	# 10-13	 **attackbox here**
    SFX_1('uwa154')
    sprite('Action_144_03', 2)	# 14-15	 **attackbox here**
    sprite('Action_144_04', 20)	# 16-35	 **attackbox here**
    sprite('Action_144_05', 4)	# 36-39

@State
def AirCommandThrowA_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Damage(2300)
        Unknown11091(5)
        Unknown9287()
        Hitstop(20)
        Unknown11064(0)
        Unknown14083(1)
        Unknown1084(1)
        Unknown20000(1)
        sendToLabelUpon(2, 9)
    sprite('Action_148_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Wal_075', 0)
    SFX_3('SE007')
    sprite('Action_148_01', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_02', 3)	# 7-9	 **attackbox here**
    physicsXImpulse(16000)
    physicsYImpulse(20000)
    Unknown1043()
    Unknown1039(150)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_03', 32767)	# 10-32776	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown7006('uwa209_0', 100, 845248373, 828324144, 0, 0, 100, 845248373, 845101360, 0, 0, 100, 0, 0, 0, 0, 0)
    loopRest()
    label(9)
    sprite('Action_148_04', 1)	# 32777-32777
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown1084(1)
    Unknown20000(0)
    SFX_3('SE025_BoundBig')
    sprite('Action_148_05', 1)	# 32778-32778
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_06', 4)	# 32779-32782	 **attackbox here**
    GFX_0('Wal_074', 0)
    Unknown13024(1)
    SFX_3('SE051')
    sprite('Action_148_07', 4)	# 32783-32786	 **attackbox here**
    sprite('Action_148_08', 20)	# 32787-32806	 **attackbox here**
    sprite('Action_148_09', 4)	# 32807-32810

@State
def AirCommandThrowB():

    def upon_IMMEDIATE():
        Unknown17011('AirCommandThrowB_Exe', 2, 1, 0)
        Unknown11054(300000)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        clearUponHandler(2)
        callSubroutine('AirAttackBeginCancelDirection')
    sprite('Action_144_00', 3)	# 1-3
    sprite('Action_144_00', 6)	# 4-9
    Unknown28(2, 'CmnActJumpLanding')
    physicsXImpulse(6000)
    physicsYImpulse(8000)
    SFX_3('SE043')
    sprite('Action_144_01', 3)	# 10-12	 **attackbox here**
    Unknown22004(10, 1)
    sprite('Action_144_02', 4)	# 13-16	 **attackbox here**
    SFX_1('uwa154')
    sprite('Action_144_03', 2)	# 17-18	 **attackbox here**
    sprite('Action_144_04', 20)	# 19-38	 **attackbox here**
    sprite('Action_144_05', 4)	# 39-42

@State
def AirCommandThrowB_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Damage(2700)
        Unknown11091(5)
        Unknown9287()
        Hitstop(20)
        Unknown11064(0)
        Unknown14083(1)
        Unknown1084(1)
        Unknown20000(1)
        sendToLabelUpon(2, 9)
    sprite('Action_148_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Wal_075', 0)
    SFX_3('SE007')
    sprite('Action_148_01', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_02', 3)	# 7-9	 **attackbox here**
    physicsYImpulse(20000)
    Unknown1043()
    Unknown1039(150)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_03', 32767)	# 10-32776	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown7006('uwa209_0', 100, 845248373, 828324144, 0, 0, 100, 845248373, 845101360, 0, 0, 100, 0, 0, 0, 0, 0)
    loopRest()
    label(9)
    sprite('Action_148_04', 1)	# 32777-32777
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown1084(1)
    Unknown20000(0)
    SFX_3('SE025_BoundBig')
    sprite('Action_148_05', 1)	# 32778-32778
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_06', 4)	# 32779-32782	 **attackbox here**
    GFX_0('Wal_074', 0)
    Unknown13024(1)
    SFX_3('SE051')
    sprite('Action_148_07', 6)	# 32783-32788	 **attackbox here**
    sprite('Action_148_08', 20)	# 32789-32808	 **attackbox here**
    sprite('Action_148_09', 4)	# 32809-32812

@State
def AirCommandThrowC():

    def upon_IMMEDIATE():
        Unknown17011('AirCommandThrowC_Exe', 2, 1, 0)
        Unknown11054(300000)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11091(10)
        clearUponHandler(2)
        callSubroutine('AirAttackBeginCancelDirection')
    sprite('Action_144_00', 3)	# 1-3
    sprite('Action_144_00', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    Unknown28(2, 'CmnActJumpLanding')
    Unknown1019(30)
    physicsYImpulse(8000)
    SFX_3('SE043')
    sprite('Action_144_01', 3)	# 7-9	 **attackbox here**
    Unknown22004(10, 1)
    sprite('Action_144_02', 4)	# 10-13	 **attackbox here**
    SFX_1('uwa154')
    sprite('Action_144_03', 2)	# 14-15	 **attackbox here**
    sprite('Action_144_04', 8)	# 16-23	 **attackbox here**
    sprite('Action_144_05', 4)	# 24-27

@State
def AirCommandThrowC_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Unknown30065(0)
        Unknown11069('AirCommandThrowC_Exe2')
        Unknown23027()
        Unknown1084(1)
        Unknown20000(1)
        callSubroutine('Eff_ExSkill_AfterImage')
        sendToLabelUpon(2, 9)
        Unknown28(78, 'AirCommandThrowC_Exe2')
    sprite('Action_148_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Wal_075', 0)
    SFX_3('SE007')
    sprite('Action_148_01', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_02', 3)	# 7-9	 **attackbox here**
    physicsXImpulse(12000)
    physicsYImpulse(20000)
    Unknown1043()
    Unknown1039(150)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    tag_voice(1, 'uwa210_0', 'uwa210_1', 'uwa210_2', '')
    sprite('Action_148_03', 32767)	# 10-32776	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    label(9)
    sprite('Action_148_04', 1)	# 32777-32777
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown1084(1)
    Unknown20000(0)
    tag_voice(0, 'uwa211_0', 'uwa211_1', 'uwa211_2', '')
    SFX_3('SE025_BoundBig')
    sprite('Action_148_05', 1)	# 32778-32778
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_06', 1)	# 32779-32779	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    RefreshMultihit()
    Unknown11091(10)
    GFX_0('Wal_074', 0)

@State
def AirCommandThrowC_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('AirCommandThrowC_Exe3', 2, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown11069('AirCommandThrowC_Exe3')
        Unknown11091(10)
        Unknown1084(1)
        callSubroutine('Eff_ExSkill_AfterImage')
    sprite('keep', 1)	# 1-1

@State
def AirCommandThrowC_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        callSubroutine('LandSlamThrow')
        Damage(2700)
        Unknown11091(10)
        Unknown9287()
        Unknown9310(20)
        Hitstop(20)
        Unknown11072(1, 700000, -200000)
        Unknown11064(0)
        Unknown30065(0)
        Unknown23027()
        Unknown14083(1)
        Unknown23072()
        callSubroutine('Eff_ExSkill_AfterImage')
    sprite('Action_148_07', 6)	# 1-6	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_08', 8)	# 7-14	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_148_09', 4)	# 15-18
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_150_10', 3)	# 19-21	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_150_11', 4)	# 22-25	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_150_12', 3)	# 26-28	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_150_13', 2)	# 29-30
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    tag_voice(0, 'uwa212_0', 'uwa212_1', 'uwa212_2', '')
    sprite('Action_150_14', 5)	# 31-35	 **attackbox here**
    RefreshMultihit()
    Unknown13024(1)
    Unknown2005()
    GFX_0('Wal_074', 0)
    sprite('Action_150_15', 5)	# 36-40	 **attackbox here**
    sprite('Action_150_16', 5)	# 41-45	 **attackbox here**
    sprite('Action_150_17', 5)	# 46-50	 **attackbox here**
    sprite('Action_150_18', 7)	# 51-57
    sprite('Action_150_19', 10)	# 58-67
    sprite('Action_150_20', 5)	# 68-72
    sprite('Action_150_21', 4)	# 73-76
    sprite('Action_150_22', 3)	# 77-79
    sprite('Action_150_23', 2)	# 80-81

@State
def UltimateThrow():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowExe', 3, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(360000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11025(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        SLOT_4 = 0
        SLOT_5 = 0

        def upon_3():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11045(0)
            else:
                Unknown11045(1)
    sprite('Action_277_00', 3)	# 1-3
    sprite('Action_277_01', 6)	# 4-9
    sprite('Action_277_02', 3)	# 10-12
    sprite('Action_277_03', 12)	# 13-24
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    sprite('Action_277_04', 4)	# 25-28
    sprite('Action_277_05', 4)	# 29-32
    sprite('Action_277_06', 3)	# 33-35
    sprite('Action_277_07', 3)	# 36-38
    sprite('Action_277_06', 3)	# 39-41
    sprite('Action_277_07', 3)	# 42-44
    sprite('Action_277_06', 3)	# 45-47
    sprite('Action_277_07', 3)	# 48-50
    sprite('Action_277_06', 3)	# 51-53
    sprite('Action_277_07', 3)	# 54-56
    sprite('Action_277_06', 3)	# 57-59
    sprite('Action_277_00', 1)	# 60-60
    sprite('Action_451_00', 6)	# 61-66
    sprite('Action_451_01', 6)	# 67-72
    sprite('Action_451_02', 5)	# 73-77	 **attackbox here**
    sprite('Action_451_03', 8)	# 78-85	 **attackbox here**
    setInvincible(0)
    SFX_1('uwa154')
    SFX_3('SE043')
    Unknown23027()
    clearUponHandler(3)
    sprite('Action_451_04', 8)	# 86-93	 **attackbox here**
    sprite('Action_451_05', 8)	# 94-101	 **attackbox here**
    sprite('Action_451_06', 8)	# 102-109	 **attackbox here**
    sprite('Action_451_07', 6)	# 110-115	 **attackbox here**
    sprite('Action_451_08', 6)	# 116-121

@State
def UltimateThrow_TRUE():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowExe', 3, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(360000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11025(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        SLOT_4 = 0
        SLOT_5 = 1

        def upon_3():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11045(0)
            else:
                Unknown11045(1)
    sprite('Action_277_00', 3)	# 1-3
    sprite('Action_277_01', 6)	# 4-9
    sprite('Action_277_02', 3)	# 10-12
    sprite('Action_277_03', 12)	# 13-24
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    sprite('Action_277_04', 4)	# 25-28
    sprite('Action_277_05', 4)	# 29-32
    sprite('Action_277_06', 3)	# 33-35
    sprite('Action_277_07', 3)	# 36-38
    sprite('Action_277_06', 3)	# 39-41
    sprite('Action_277_07', 3)	# 42-44
    sprite('Action_277_06', 3)	# 45-47
    sprite('Action_277_07', 3)	# 48-50
    sprite('Action_277_06', 3)	# 51-53
    sprite('Action_277_07', 3)	# 54-56
    sprite('Action_277_06', 3)	# 57-59
    sprite('Action_277_00', 1)	# 60-60
    sprite('Action_451_00', 6)	# 61-66
    sprite('Action_451_01', 6)	# 67-72
    sprite('Action_451_02', 5)	# 73-77	 **attackbox here**
    sprite('Action_451_03', 8)	# 78-85	 **attackbox here**
    setInvincible(0)
    SFX_1('uwa154')
    SFX_3('SE043')
    Unknown23027()
    clearUponHandler(3)
    sprite('Action_451_04', 8)	# 86-93	 **attackbox here**
    sprite('Action_451_05', 8)	# 94-101	 **attackbox here**
    sprite('Action_451_06', 8)	# 102-109	 **attackbox here**
    sprite('Action_451_07', 6)	# 110-115	 **attackbox here**
    sprite('Action_451_08', 6)	# 116-121

@State
def UltimateThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11001(20, 20, 20)
        Unknown11072(1, 50000, 510000)
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowExe2')
        if SLOT_4:
            Damage(500)
            Unknown11091(100)
        setInvincible(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown13024(0)
        Unknown30068(1)
        Unknown28(8, 'UltimateThrowExe2')
    sprite('Action_173_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_3('SE007')
    sprite('Action_173_01', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_02', 2)	# 7-8	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_03', 5)	# 9-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_04', 3)	# 14-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_05', 3)	# 17-19	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_06', 5)	# 20-24	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_175_00', 3)	# 25-27	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    tag_voice(1, 'uwa250_0', 'uwa250_1', '', '')
    sprite('Action_175_01', 4)	# 28-31	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_02', 5)	# 32-36	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_03', 4)	# 37-40	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('Wal_104', 0)
    SFX_3('SE007')

@State
def UltimateThrowExe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowExe3', 3, 0, 0)
        Unknown23056('')
        callSubroutine('Throw2Throw')
        Unknown11069('UltimateThrowExe3')
        Unknown20000(1)
        Unknown20003(1)
    sprite('keep', 1)	# 1-1

@State
def UltimateThrowExe3():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(10)
        AirPushbackY(-100000)
        AirUntechableTime(999)
        Unknown9310(999)
        Hitstop(0)
        Unknown11072(1, 200000, 1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowExe4')
        if SLOT_4:
            Damage(500)
            Unknown11091(100)
        setInvincible(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown13024(0)
        Unknown30068(1)
        Unknown28(8, 'UltimateThrowExe4')
    sprite('Action_175_04', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_05', 2)	# 4-5	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_06', 4)	# 6-9	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_07', 2)	# 10-11	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_08', 2)	# 12-13
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_09', 19)	# 14-32	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    physicsXImpulse(5000)
    physicsYImpulse(40000)
    sprite('Action_175_10', 23)	# 33-55	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_11', 1)	# 56-56	 **attackbox here**
    RefreshMultihit()

@State
def UltimateThrowExe4():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(5000)
        Unknown11091(20)
        AttackP2(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(120)
        Unknown9190(1)
        AirPushbackY(-70000)
        Unknown9310(30)
        Hitstop(0)
        Unknown11001(30, 30, 30)
        Unknown11023(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown30048(1)
        Unknown23027()
        if SLOT_4:
            Damage(1000)
            AttackP2(100)
            Unknown11091(100)
            SLOT_4 = 0
            Unknown2037(1)
        if SLOT_5:
            Damage(5782)
            SLOT_5 = 0
        setInvincible(1)
        GFX_0('UltimateThrowExe4_Camera', 1)
        Unknown13024(0)
        sendToLabelUpon(2, 1)
        Unknown30068(1)
    sprite('null', 30)	# 1-30
    sprite('Action_110_00', 15)	# 31-45
    teleportRelativeY(2000000)
    Unknown1084(1)
    physicsYImpulse(-30000)
    tag_voice(0, 'uwa251_0', 'uwa251_1', '', '')
    sprite('Action_110_01', 2)	# 46-47
    sprite('Action_110_02', 2)	# 48-49	 **attackbox here**
    GFX_0('Wal_178', 100)
    SFX_3('SE051')
    SFX_3('SE_BigBomb')
    sprite('Action_110_03', 2)	# 50-51	 **attackbox here**
    label(0)
    sprite('Action_110_02', 2)	# 52-53	 **attackbox here**
    sprite('Action_110_03', 2)	# 54-55	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 56-56
    Unknown26('UltimateThrowExe4_Camera')
    Unknown20001(1)
    Unknown20000(1)
    Unknown20003(1)
    RefreshMultihit()
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    Unknown4004('6566666563745f33383200000000000000000000000000000000000000000000ffff0000')
    SFX_3('SE025_BoundBig')
    sprite('Action_110_04', 2)	# 57-58
    Unknown26('Wal_178')
    sprite('Action_110_05', 2)	# 59-60
    sprite('Action_110_06', 30)	# 61-90
    sprite('Action_110_06', 30)	# 91-120
    sprite('Action_277_06', 5)	# 121-125
    sprite('Action_277_07', 5)	# 126-130
    sprite('Action_277_06', 5)	# 131-135
    sprite('Action_277_07', 5)	# 136-140
    sprite('Action_277_06', 5)	# 141-145
    sprite('Action_277_07', 5)	# 146-150
    sprite('Action_277_06', 5)	# 151-155
    if (not SLOT_2):
        Unknown13024(1)
    sprite('Action_277_07', 5)	# 156-160
    sprite('Action_277_06', 5)	# 161-165
    sprite('Action_277_07', 5)	# 166-170
    sprite('Action_277_06', 5)	# 171-175
    sprite('Action_277_07', 5)	# 176-180
    sprite('Action_277_06', 8)	# 181-188
    Unknown20000(0)
    sprite('Action_277_07', 8)	# 189-196
    sprite('Action_051_15', 5)	# 197-201
    sprite('Action_051_16', 5)	# 202-206
    sprite('Action_051_17', 5)	# 207-211

@State
def UltimateThrowOD():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe', 5, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(360000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11025(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        SLOT_4 = 0
        SLOT_5 = 0

        def upon_3():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11045(0)
            else:
                Unknown11045(1)
    sprite('Action_277_00', 3)	# 1-3
    sprite('Action_277_01', 6)	# 4-9
    sprite('Action_277_02', 3)	# 10-12
    sprite('Action_277_03', 12)	# 13-24
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    sprite('Action_277_04', 4)	# 25-28
    sprite('Action_277_05', 4)	# 29-32
    sprite('Action_277_06', 3)	# 33-35
    sprite('Action_277_07', 3)	# 36-38
    sprite('Action_277_06', 3)	# 39-41
    sprite('Action_277_07', 3)	# 42-44
    sprite('Action_277_06', 3)	# 45-47
    sprite('Action_277_07', 3)	# 48-50
    sprite('Action_277_06', 3)	# 51-53
    sprite('Action_277_07', 3)	# 54-56
    sprite('Action_277_06', 3)	# 57-59
    sprite('Action_277_00', 1)	# 60-60
    sprite('Action_451_00', 6)	# 61-66
    sprite('Action_451_01', 6)	# 67-72
    sprite('Action_451_02', 5)	# 73-77	 **attackbox here**
    sprite('Action_451_03', 8)	# 78-85	 **attackbox here**
    setInvincible(0)
    SFX_1('uwa154')
    SFX_3('SE043')
    Unknown23027()
    clearUponHandler(3)
    sprite('Action_451_04', 8)	# 86-93	 **attackbox here**
    sprite('Action_451_05', 8)	# 94-101	 **attackbox here**
    sprite('Action_451_06', 8)	# 102-109	 **attackbox here**
    sprite('Action_451_07', 6)	# 110-115	 **attackbox here**
    sprite('Action_451_08', 6)	# 116-121

@State
def UltimateThrowOD_TRUE():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe', 5, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(360000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11025(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        SLOT_4 = 0
        SLOT_5 = 1

        def upon_3():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11045(0)
            else:
                Unknown11045(1)
    sprite('Action_277_00', 3)	# 1-3
    sprite('Action_277_01', 6)	# 4-9
    sprite('Action_277_02', 3)	# 10-12
    sprite('Action_277_03', 12)	# 13-24
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    sprite('Action_277_04', 4)	# 25-28
    sprite('Action_277_05', 4)	# 29-32
    sprite('Action_277_06', 3)	# 33-35
    sprite('Action_277_07', 3)	# 36-38
    sprite('Action_277_06', 3)	# 39-41
    sprite('Action_277_07', 3)	# 42-44
    sprite('Action_277_06', 3)	# 45-47
    sprite('Action_277_07', 3)	# 48-50
    sprite('Action_277_06', 3)	# 51-53
    sprite('Action_277_07', 3)	# 54-56
    sprite('Action_277_06', 3)	# 57-59
    sprite('Action_277_00', 1)	# 60-60
    sprite('Action_451_00', 6)	# 61-66
    sprite('Action_451_01', 6)	# 67-72
    sprite('Action_451_02', 5)	# 73-77	 **attackbox here**
    sprite('Action_451_03', 8)	# 78-85	 **attackbox here**
    setInvincible(0)
    SFX_1('uwa154')
    SFX_3('SE043')
    Unknown23027()
    clearUponHandler(3)
    sprite('Action_451_04', 8)	# 86-93	 **attackbox here**
    sprite('Action_451_05', 8)	# 94-101	 **attackbox here**
    sprite('Action_451_06', 8)	# 102-109	 **attackbox here**
    sprite('Action_451_07', 6)	# 110-115	 **attackbox here**
    sprite('Action_451_08', 6)	# 116-121

@State
def UltimateThrowODExe():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        Unknown23056('')
        callSubroutine('LandSlamThrow')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(100)
        Hitstop(0)
        Unknown11069('UltimateThrowODExe2')
        Unknown23027()
        if SLOT_4:
            Damage(100)
            Unknown11091(100)
        Unknown20000(1)
        Unknown20003(1)
        Unknown28(78, 'UltimateThrowODExe2')
    sprite('Action_454_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_3('SE007')
    sprite('Action_454_01', 6)	# 4-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_02', 2)	# 10-11	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_03', 5)	# 12-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_04', 8)	# 17-24	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_454_05', 3)	# 25-27	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_455_00', 3)	# 28-30	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_01', 6)	# 31-36	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_02', 3)	# 37-39	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_05', 3)	# 40-42	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Eff_UltimateThrowSlam', 0)
    RefreshMultihit()
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    Unknown36(1)
    teleportRelativeY(0)
    Unknown35()

@State
def UltimateThrowODExe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe3', 5, 0, 0)
        Unknown23056('')
        callSubroutine('Throw2Throw')
        Unknown11069('UltimateThrowODExe3')
        Unknown20003(1)
    sprite('keep', 1)	# 1-1

@State
def UltimateThrowODExe3():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        Unknown23056('')
        callSubroutine('LandSlamThrow')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(100)
        Hitstop(0)
        Unknown11069('UltimateThrowODExe4')
        Unknown23027()
        if SLOT_4:
            Damage(200)
            Unknown11091(100)
        Unknown20000(1)
        Unknown20003(1)
        Unknown28(78, 'UltimateThrowODExe4')
    sprite('Action_455_06', 2)	# 1-2	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_07', 2)	# 3-4	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_056_01', 6)	# 5-10	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_455_00', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_01', 6)	# 14-19	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_02', 3)	# 20-22	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_05', 3)	# 23-25	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Eff_UltimateThrowSlam', 0)
    RefreshMultihit()
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    Unknown36(1)
    teleportRelativeY(0)
    Unknown35()

@State
def UltimateThrowODExe4():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe5', 5, 0, 0)
        Unknown23056('')
        callSubroutine('Throw2Throw')
        Unknown11069('UltimateThrowODExe5')
        Unknown20003(1)
    sprite('keep', 1)	# 1-1

@State
def UltimateThrowODExe5():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        Unknown23056('')
        callSubroutine('LandSlamThrow')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(100)
        Unknown11069('UltimateThrowODExe6')
        Unknown23027()
        if SLOT_4:
            Damage(200)
            Unknown11091(100)
        Unknown20000(1)
        Unknown20003(1)
        Unknown28(78, 'UltimateThrowODExe6')
    sprite('Action_455_06', 2)	# 1-2	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_07', 2)	# 3-4	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_056_01', 6)	# 5-10	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_455_00', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_01', 6)	# 14-19	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    sprite('Action_455_02', 3)	# 20-22	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_455_05', 3)	# 23-25	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('Eff_UltimateThrowSlam', 0)
    RefreshMultihit()
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    Unknown36(1)
    teleportRelativeY(0)
    Unknown35()

@State
def UltimateThrowODExe6():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe7', 5, 0, 0)
        Unknown23056('')
        callSubroutine('Throw2Throw')
        Unknown11069('UltimateThrowODExe7')
        Unknown20003(1)
    sprite('keep', 1)	# 1-1

@State
def UltimateThrowODExe7():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11001(20, 20, 20)
        Unknown11072(1, 50000, 510000)
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowODExe8')
        if SLOT_4:
            Damage(500)
            Unknown11091(100)
        setInvincible(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown13024(0)
        Unknown30068(1)
        Unknown28(8, 'UltimateThrowODExe8')
    sprite('Action_173_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_01', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_02', 2)	# 7-8	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_03', 5)	# 9-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_04', 3)	# 14-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_05', 3)	# 17-19	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_06', 5)	# 20-24	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_175_00', 3)	# 25-27	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    tag_voice(1, 'uwa250_0', 'uwa250_1', '', '')
    sprite('Action_175_01', 4)	# 28-31	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_02', 5)	# 32-36	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_03', 4)	# 37-40	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('Wal_104', 0)
    SFX_3('SE007')

@State
def UltimateThrowODExe8():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe9', 5, 0, 0)
        Unknown23056('')
        callSubroutine('Throw2Throw')
        Unknown11069('UltimateThrowODExe9')
        Unknown20000(1)
        Unknown20003(1)
    sprite('keep', 1)	# 1-1

@State
def UltimateThrowODExe9():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(10)
        AirPushbackY(-100000)
        AirUntechableTime(999)
        Unknown9310(999)
        Hitstop(0)
        Unknown11072(1, 200000, 1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowODExe10')
        if SLOT_4:
            Damage(500)
            Unknown11091(100)
        setInvincible(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown13024(0)
        Unknown30068(1)
        Unknown28(8, 'UltimateThrowODExe10')
    sprite('Action_175_04', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_05', 2)	# 4-5	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_06', 4)	# 6-9	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_07', 2)	# 10-11	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_08', 2)	# 12-13
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_09', 19)	# 14-32	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    physicsXImpulse(5000)
    physicsYImpulse(40000)
    sprite('Action_175_10', 23)	# 33-55	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_175_11', 1)	# 56-56	 **attackbox here**
    RefreshMultihit()

@State
def UltimateThrowODExe10():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(5000)
        Unknown11091(20)
        AttackP2(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(120)
        Unknown9190(1)
        AirPushbackY(-70000)
        Unknown9310(30)
        Hitstop(0)
        Unknown11001(30, 30, 30)
        Unknown11023(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown30048(1)
        Unknown23027()
        if SLOT_4:
            Damage(1000)
            AttackP2(100)
            Unknown11091(100)
            SLOT_4 = 0
            Unknown2037(1)
        if SLOT_5:
            Damage(5782)
            SLOT_5 = 0
        setInvincible(1)
        GFX_0('UltimateThrowExe4_Camera', 1)
        Unknown13024(0)
        sendToLabelUpon(2, 1)
        Unknown30068(1)
    sprite('null', 30)	# 1-30
    sprite('Action_110_00', 15)	# 31-45
    teleportRelativeY(2000000)
    Unknown1084(1)
    physicsYImpulse(-30000)
    tag_voice(0, 'uwa251_0', 'uwa251_1', '', '')
    sprite('Action_110_01', 2)	# 46-47
    sprite('Action_110_02', 2)	# 48-49	 **attackbox here**
    GFX_0('Wal_178', 100)
    SFX_3('SE051')
    SFX_3('SE_BigBomb')
    sprite('Action_110_03', 2)	# 50-51	 **attackbox here**
    label(0)
    sprite('Action_110_02', 2)	# 52-53	 **attackbox here**
    sprite('Action_110_03', 2)	# 54-55	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 56-56
    Unknown26('UltimateThrowExe4_Camera')
    Unknown20001(1)
    Unknown20000(1)
    Unknown20003(1)
    RefreshMultihit()
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    Unknown4004('6566666563745f33383200000000000000000000000000000000000000000000ffff0000')
    SFX_3('SE025_BoundBig')
    sprite('Action_110_04', 2)	# 57-58
    Unknown26('Wal_178')
    sprite('Action_110_05', 2)	# 59-60
    sprite('Action_110_06', 30)	# 61-90
    sprite('Action_110_06', 30)	# 91-120
    sprite('Action_277_06', 5)	# 121-125
    sprite('Action_277_07', 5)	# 126-130
    sprite('Action_277_06', 5)	# 131-135
    sprite('Action_277_07', 5)	# 136-140
    sprite('Action_277_06', 5)	# 141-145
    sprite('Action_277_07', 5)	# 146-150
    sprite('Action_277_06', 5)	# 151-155
    if (not SLOT_2):
        Unknown13024(1)
    sprite('Action_277_07', 5)	# 156-160
    sprite('Action_277_06', 5)	# 161-165
    sprite('Action_277_07', 5)	# 166-170
    sprite('Action_277_06', 5)	# 171-175
    sprite('Action_277_07', 5)	# 176-180
    sprite('Action_277_06', 8)	# 181-188
    Unknown20000(0)
    sprite('Action_277_07', 8)	# 189-196
    sprite('Action_051_15', 5)	# 197-201
    sprite('Action_051_16', 5)	# 202-206
    sprite('Action_051_17', 5)	# 207-211

@State
def UltimateRunningThrow():

    def upon_IMMEDIATE():
        Unknown17011('UltimateRunningThrow_Exe', 3, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(240000)
        Unknown11032('0000000040420f00ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11082(1)
        Unknown11025(0)
        loopRelated(17, 120)

        def upon_17():
            clearUponHandler(3)
            clearUponHandler(17)
            sendToLabel(1)
        Unknown28(8, 'UltimateRunningThrow_End')
    sprite('Action_435_00', 3)	# 1-3
    setInvincible(1)
    sprite('Action_435_01', 3)	# 4-6
    sprite('Action_435_02', 6)	# 7-12
    sprite('Action_435_02', 52)	# 13-64
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    Unknown7006('uwa252_0', 100, 845248373, 828322357, 0, 0, 100, 845248373, 845099573, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_435_03', 3)	# 65-67
    sprite('Action_435_04', 6)	# 68-73
    Unknown8007(100, 1, 1)
    physicsXImpulse(40000)
    Unknown1028(1000)
    SFX_3('SE050_SlideDash')
    label(0)
    sprite('Action_435_05', 3)	# 74-76	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('Action_435_06', 3)	# 77-79	 **attackbox here**
    setInvincible(0)
    Unknown2017(0)

    def upon_3():
        Unknown48('19000000020000003300000016000000020000001e000000')
        if SLOT_51:
            Unknown11045(0)
        else:
            Unknown11045(1)
        if SLOT_38:
            Unknown23045('5a000000')
            if (SLOT_22 < SLOT_0):
                clearUponHandler(3)
                clearUponHandler(17)
                sendToLabel(1)
        else:
            Unknown23045('5a000000')
            if (SLOT_22 > SLOT_0):
                clearUponHandler(3)
                clearUponHandler(17)
                sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_09', 1)	# 80-80
    setInvincible(0)
    Unknown26('AirCatch_Collision_URT')
    Unknown1019(40)
    Unknown2017(1)
    Unknown8007(100, 1, 1)
    sprite('Action_435_10', 3)	# 81-83
    Unknown1019(40)
    GFX_0('Eff_SturmAngriff', 0)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    sprite('Action_435_11', 6)	# 84-89
    Unknown1084(1)

@State
def UltimateRunningThrow_Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        callSubroutine('UltimateRunningThrow_Init')
        callSubroutine('UltimateRunningThrow_Atk')
        Unknown11069('UltimateRunningThrow_Exe2')
        Unknown28(78, 'UltimateRunningThrow_Exe2')
        Unknown26('AirCatch_Collision_URT')
        SFX_3('SE050_SlideDash')
    label(0)
    sprite('Action_435_05', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown8006(100, 1, 0)
    sprite('Action_435_06', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_09', 2)	# 7-8
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(0)
    Unknown1019(80)
    Unknown2017(1)
    Unknown8007(100, 1, 1)
    tag_voice(1, 'uwa253_0', 'uwa253_1', 'uwa253_2', '')
    sprite('Action_435_09', 2)	# 9-10
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown1019(80)
    sprite('Action_435_10ex', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    RefreshMultihit()
    GFX_0('Eff_SturmAngriff', 0)
    Unknown1084(1)
    sprite('Action_435_11', 8)	# 14-21

@State
def UltimateRunningThrow_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateRunningThrow_Exe3', 5, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown20000(1)
        Unknown11069('UltimateRunningThrow_Exe3')
    sprite('keep', 1)	# 1-1

@State
def UltimateRunningThrow_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        callSubroutine('UltimateRunningThrow_Init')
        callSubroutine('UltimateRunningThrow_Atk')
        Damage(5000)
        AttackP2(60)
        Hitstop(30)
        Unknown11064(0)
        Unknown13024(1)
        SFX_3('SE050_SlideDash')
    label(0)
    sprite('Action_435_05', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown8006(100, 1, 0)
    sprite('Action_435_06', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_09', 2)	# 7-8
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(0)
    Unknown1019(80)
    Unknown2017(1)
    Unknown8007(100, 1, 1)
    tag_voice(0, 'uwa254_0', 'uwa254_1', 'uwa254_2', '')
    sprite('Action_435_09', 2)	# 9-10
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown1019(80)
    sprite('Action_435_10ex', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    RefreshMultihit()
    GFX_0('Eff_SturmAngriff', 0)
    Unknown1084(1)
    sprite('Action_435_11', 8)	# 14-21

@State
def UltimateRunningThrow_End():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        sendToLabelUpon(2, 99)
    sprite('Action_435_12', 3)	# 1-3
    sprite('Action_435_13', 4)	# 4-7
    physicsXImpulse(-5500)
    physicsYImpulse(3900)
    setGravity(480)
    label(4)
    sprite('Action_435_14', 6)	# 8-13
    sprite('Action_435_15', 6)	# 14-19
    loopRest()
    gotoLabel(4)
    label(99)
    sprite('Action_435_16', 4)	# 20-23
    Unknown1084(1)
    sprite('Action_435_17', 4)	# 24-27
    Unknown8000(100, 1, 1)
    SFX_3('SE025_BoundBig')
    sprite('Action_435_18', 4)	# 28-31
    sprite('Action_435_19', 4)	# 32-35

@State
def UltimateRunningThrowOD():

    def upon_IMMEDIATE():
        Unknown17011('UltimateRunningThrowOD_Exe', 5, 0, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11054(240000)
        Unknown11032('0000000040420f00ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(0)
        Unknown11082(1)
        Unknown11025(0)
        loopRelated(17, 120)

        def upon_17():
            clearUponHandler(3)
            clearUponHandler(17)
            sendToLabel(1)
        Unknown28(8, 'UltimateRunningThrow_End')
    sprite('Action_435_00', 3)	# 1-3
    setInvincible(1)
    sprite('Action_435_01', 3)	# 4-6
    sprite('Action_435_02', 6)	# 7-12
    sprite('Action_435_02', 52)	# 13-64
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    Unknown7006('uwa252_0', 100, 845248373, 828322357, 0, 0, 100, 845248373, 845099573, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_435_03', 3)	# 65-67
    sprite('Action_435_04', 6)	# 68-73
    Unknown8007(100, 1, 1)
    physicsXImpulse(40000)
    Unknown1028(1000)
    SFX_3('SE050_SlideDash')
    label(0)
    sprite('Action_435_05', 3)	# 74-76	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('Action_435_06', 3)	# 77-79	 **attackbox here**
    setInvincible(0)
    Unknown2017(0)

    def upon_3():
        Unknown48('19000000020000003300000016000000020000001e000000')
        if SLOT_51:
            Unknown11045(0)
        else:
            Unknown11045(1)
        if SLOT_38:
            Unknown23045('5a000000')
            if (SLOT_22 < SLOT_0):
                clearUponHandler(3)
                clearUponHandler(17)
                sendToLabel(1)
        else:
            Unknown23045('5a000000')
            if (SLOT_22 > SLOT_0):
                clearUponHandler(3)
                clearUponHandler(17)
                sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_09', 1)	# 80-80
    setInvincible(0)
    Unknown26('AirCatch_Collision_URTOD')
    Unknown1019(40)
    Unknown2017(1)
    Unknown8007(100, 1, 1)
    sprite('Action_435_10', 3)	# 81-83
    Unknown1019(40)
    GFX_0('Eff_SturmAngriff', 0)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    sprite('Action_435_11', 6)	# 84-89
    Unknown1084(1)

@State
def UltimateRunningThrowOD_Exe():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        callSubroutine('UltimateRunningThrow_Init')
        callSubroutine('UltimateRunningThrow_Atk')
        Unknown11069('UltimateRunningThrowOD_Exe2')
        Unknown28(78, 'UltimateRunningThrowOD_Exe2')
        Unknown26('AirCatch_Collision_URTOD')
        SFX_3('SE050_SlideDash')
    label(0)
    sprite('Action_435_05', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown8006(100, 1, 0)
    sprite('Action_435_06', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_09', 2)	# 7-8
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(0)
    Unknown1019(80)
    Unknown2017(1)
    Unknown8007(100, 1, 1)
    tag_voice(1, 'uwa253_0', 'uwa253_1', 'uwa253_2', '')
    sprite('Action_435_09', 2)	# 9-10
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown1019(80)
    sprite('Action_435_10ex', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    RefreshMultihit()
    GFX_0('Eff_SturmAngriff', 0)
    Unknown1084(1)
    sprite('Action_435_11', 8)	# 14-21

@State
def UltimateRunningThrowOD_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateRunningThrowOD_Exe3', 5, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown20000(1)
        Unknown11069('UltimateRunningThrowOD_Exe3')
    sprite('keep', 1)	# 1-1

@State
def UltimateRunningThrowOD_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        callSubroutine('UltimateRunningThrow_Init')
        callSubroutine('UltimateRunningThrow_Atk')
        Unknown11069('UltimateRunningThrowOD_Exe4')
        Unknown28(78, 'UltimateRunningThrowOD_Exe4')
        SFX_3('SE050_SlideDash')
    label(0)
    sprite('Action_435_05', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown8006(100, 1, 0)
    sprite('Action_435_06', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_09', 2)	# 7-8
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(0)
    Unknown1019(80)
    Unknown2017(1)
    Unknown8007(100, 1, 1)
    tag_voice(0, 'uwa254_0', 'uwa255_1', 'uwa254_2', '')
    sprite('Action_435_09', 2)	# 9-10
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown1019(80)
    sprite('Action_435_10ex', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    RefreshMultihit()
    GFX_0('Eff_SturmAngriff', 0)
    Unknown1084(1)
    sprite('Action_435_11', 8)	# 14-21

@State
def UltimateRunningThrowOD_Exe4():

    def upon_IMMEDIATE():
        Unknown17011('UltimateRunningThrowOD_Exe5', 5, 0, 0)
        callSubroutine('Throw2Throw')
        Unknown20000(1)
        Unknown11069('UltimateRunningThrowOD_Exe5')
    sprite('keep', 1)	# 1-1

@State
def UltimateRunningThrowOD_Exe5():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        callSubroutine('UltimateRunningThrow_Init')
        callSubroutine('UltimateRunningThrow_Atk')
        Damage(5000)
        AttackP2(60)
        Hitstop(30)
        Unknown11064(0)
        Unknown13024(1)
        SFX_3('SE050_SlideDash')
    label(0)
    sprite('Action_435_05', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown8006(100, 1, 0)
    sprite('Action_435_06', 3)	# 4-6	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_09', 2)	# 7-8
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown3029(0)
    Unknown1019(80)
    Unknown2017(1)
    Unknown8007(100, 1, 1)
    tag_voice(0, 'uwa255_2', 'uwa256_2', 'uwa256_1', '')
    sprite('Action_435_09', 2)	# 9-10
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    Unknown1019(80)
    sprite('Action_435_10ex', 3)	# 11-13	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000040000000000000000000000')
    RefreshMultihit()
    GFX_0('Eff_SturmAngriff', 0)
    Unknown1084(1)
    sprite('Action_435_11', 8)	# 14-21

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown17011('AstralHeatExe', 6, 0, 0)
        Unknown11069('AstralHeatExe')
        Unknown11054(360000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(1)
        Unknown11025(0)
        setInvincible(1)
    sprite('Action_277_00', 3)	# 1-3
    sprite('Action_277_01', 6)	# 4-9
    sprite('Action_277_02', 3)	# 10-12
    sprite('Action_277_03', 23)	# 13-35
    Unknown2036(72, -1, 1)
    Unknown23147()
    GFX_0('Wal_999', 100)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    SFX_1('uwa290')
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    sprite('Action_277_04', 4)	# 36-39
    sprite('Action_277_05', 4)	# 40-43
    sprite('Action_277_06', 3)	# 44-46
    sprite('Action_277_07', 3)	# 47-49
    sprite('Action_277_06', 3)	# 50-52
    sprite('Action_277_07', 3)	# 53-55
    sprite('Action_277_06', 3)	# 56-58
    sprite('Action_277_00', 2)	# 59-60
    sprite('Action_220_00', 11)	# 61-71
    sprite('Action_220_01', 8)	# 72-79
    sprite('Action_220_02', 5)	# 80-84
    sprite('Action_220_03', 5)	# 85-89	 **attackbox here**
    sprite('Action_451_04', 20)	# 90-109	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    SFX_3('SE043')
    SFX_1('uwa154')
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_451_05', 5)	# 110-114	 **attackbox here**
    sprite('Action_451_06', 8)	# 115-122	 **attackbox here**
    sprite('Action_451_07', 4)	# 123-126	 **attackbox here**
    sprite('Action_451_08', 4)	# 127-130

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        AttackLevel_(5)
        Damage(20000)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(0)
        AirPushbackY(-100000)
        Unknown9310(999)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown11064(1)
        Unknown30079(1)
        Unknown23027()
        setInvincible(1)
        Unknown13024(0)
        Unknown2034(0)
        Unknown2053(0)
        Unknown30068(1)
        Unknown20000(1)
        Unknown23157(1)
        Unknown23088(1, 1)
        Unknown23084(1)
    sprite('Action_173_00', 8)	# 1-8	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    GFX_0('Wal_188', 0)
    SFX_1('uwa291')
    sprite('Action_173_01', 8)	# 9-16	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_02', 6)	# 17-22	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_173_03', 12)	# 23-34	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    sprite('Action_148_00', 2)	# 35-36	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown8001(1, 0)
    GFX_0('AstralHeatCamera', 100)
    Unknown20000(0)
    sprite('Action_148_01', 9)	# 37-45	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    physicsXImpulse(40000)
    physicsYImpulse(90000)
    Unknown3029(1)
    Unknown3070(5)
    Unknown3071(10)
    sprite('Action_148_01', 30)	# 46-75	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_185_10', 12)	# 76-87
    Unknown3029(0)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown1084(1)
    Unknown1000(0)
    teleportRelativeY(1000000)
    Unknown2018(0, 70)
    GFX_0('Wal_183', 0)
    Unknown21015('41737472616c4865617443616d657261000000000000000000000000000000008503000000000000')
    Unknown4004('6566666563745f32363600000000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    Unknown2019(500)
    Unknown35()

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 >= 180):
            clearUponHandler(3)
            Unknown1084(1)
            teleportRelativeY(0)
            Unknown21015('41737472616c4865617443616d657261000000000000000000000000000000008603000000000000')
            sendToLabel(9)
    label(0)
    sprite('Action_185_11', 4)	# 88-91
    ScreenShake(5000, 10000)
    SFX_3('SE009')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_185_12', 4)	# 92-95
    ScreenShake(10000, 5000)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_185_13ex', 20)	# 96-115	 **attackbox here**
    Unknown26('effect_266')
    RefreshMultihit()
    Unknown5005(0)
    Unknown5000(28, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    ScreenShake(5000, 20000)
    Unknown8004(100, 1, 1)
    SFX_3('SE_Bomb')
    Unknown1096(8000)
    GFX_0('Wal_185ex', 100)
    GFX_0('Wal_187', 100)
    sprite('Action_185_13ex', 3)	# 116-118	 **attackbox here**
    SFX_1('uwa292')
    sprite('Action_185_13ex', 30)	# 119-148	 **attackbox here**
    SFX_3('SE_Bomb')
    ScreenShake(5000, 5000)
    Unknown1059(-16)
    Unknown1067(-16)
    physicsYImpulse(1000)
    sprite('Action_185_13ex', 20)	# 149-168	 **attackbox here**
    physicsYImpulse(3000)
    Unknown1059(-144)
    Unknown1067(-144)
    SFX_3('SE_Bomb')
    ScreenShake(5000, 5000)
    sprite('Action_185_13ex', 10)	# 169-178	 **attackbox here**
    SFX_3('SE_Bomb')
    physicsYImpulse(-4000)
    Unknown1059(-320)
    Unknown1067(-320)
    sprite('Action_185_13ex', 225)	# 179-403	 **attackbox here**
    Unknown1084(1)
    Unknown1059(0)
    Unknown1067(0)
    sprite('Action_185_13ex', 1)	# 404-404	 **attackbox here**
    RefreshMultihit()
    Damage(37000)
    Unknown11072(2, 0, 2000000)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirUntechableTime(9999)
    AirPushbackX(0)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(0)
    Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    Unknown11064(3)
    Unknown30079(0)
    Unknown26('Wal_185ex')
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    label(20)
    sprite('Action_277_06', 5)	# 405-409
    Unknown1096(1000)
    Unknown1099(0)
    teleportRelativeY(0)
    sprite('Action_277_07', 5)	# 410-414
    sprite('Action_277_06', 5)	# 415-419
    sprite('Action_277_07', 5)	# 420-424
    sprite('Action_277_06', 5)	# 425-429
    sprite('Action_277_07', 5)	# 430-434
    sprite('Action_277_06', 5)	# 435-439
    sprite('Action_277_07', 5)	# 440-444
    sprite('Action_277_06', 5)	# 445-449
    sprite('Action_277_07', 5)	# 450-454
    sprite('Action_277_06', 5)	# 455-459
    sprite('Action_277_07', 5)	# 460-464
    sprite('Action_277_06', 5)	# 465-469
    sprite('Action_277_07', 5)	# 470-474
    sprite('Action_277_06', 5)	# 475-479
    sprite('Action_277_07', 5)	# 480-484
    sprite('Action_277_06', 5)	# 485-489
    sprite('Action_277_07', 5)	# 490-494
    sprite('Action_277_06', 5)	# 495-499
    sprite('Action_277_07', 5)	# 500-504
    sprite('Action_277_06', 5)	# 505-509
    sprite('Action_277_07', 5)	# 510-514
    sprite('Action_277_06', 5)	# 515-519
    sprite('Action_277_07', 5)	# 520-524
    sprite('Action_277_06', 5)	# 525-529
    sprite('Action_277_07', 5)	# 530-534
    sprite('Action_277_06', 5)	# 535-539
    sprite('Action_277_07', 5)	# 540-544
    sprite('Action_277_06', 8)	# 545-552
    sprite('Action_277_07', 8)	# 553-560
    sprite('Action_051_15', 5)	# 561-565
    sprite('Action_051_16', 5)	# 566-570
    sprite('Action_051_17', 5)	# 571-575

@Subroutine
def MouthTableInit():
    Unknown18011('uwa500', 12643, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa501', 13155, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa502', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa503', 13155, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa504', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa505', 13155, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa520', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa521', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa522', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa523', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa524', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa525', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa402_0', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa402_1', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa403_0', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa403_1', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600baz', 12643, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 12849, 14435, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600bjb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa601btg', 12899, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa601pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600pce', 12899, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600ryn_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600ryn_2', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600uca', 12899, 12345, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa601ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600uhy', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 12849, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600uli', 12643, 24880, 13361, 14179, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa600umi', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa700baz', 12899, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa701bjb', 12643, 12641, 25396, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa700btg', 12643, 12343, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa701pak', 12643, 14177, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa701pce', 13155, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa700ryn', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa700uca', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa700ugo', 12899, 24880, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa701uhy', 12643, 14177, 12899, 24882, 25399, 24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa700uli', 12899, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uwa700umi', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    label(1)
    sprite('null', 2)	# 2-3
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(1)
    sprite('Action_050_02', 5)	# 4-8
    if SLOT_158:
        if random_(2, 0, 50):
            Unknown7006('uwa501', 100, 895580021, 12336, 0, 0, 100, 895580021, 12848, 0, 0, 100, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uwa503', 100, 895580021, 13360, 0, 0, 100, 895580021, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(2500)
    sendToLabelUpon(2, 3)
    label(2)
    sprite('Action_050_02', 3)	# 9-11
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('Action_050_03', 7)	# 12-18
    SFX_3('SE025_BoundBig')
    ScreenShake(0, 10000)
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    sprite('Action_050_04', 15)	# 19-33
    sprite('Action_050_05', 12)	# 34-45
    sprite('Action_050_06', 7)	# 46-52
    sprite('Action_050_07', 5)	# 53-57
    sprite('Action_050_08', 5)	# 58-62
    sprite('Action_050_09', 5)	# 63-67
    sprite('Action_050_10', 5)	# 68-72
    sprite('Action_050_09', 5)	# 73-77
    sprite('Action_050_10', 5)	# 78-82
    sprite('Action_050_09', 5)	# 83-87
    sprite('Action_050_10', 5)	# 88-92
    sprite('Action_050_09', 5)	# 93-97
    sprite('Action_050_10', 5)	# 98-102
    label(4)
    sprite('Action_050_11', 5)	# 103-107
    sprite('Action_050_12', 5)	# 108-112
    if SLOT_97:
        _gotolabel(4)
    sprite('Action_050_13', 8)	# 113-120
    sprite('Action_050_14', 8)	# 121-128
    Unknown23018(1)
    sprite('Action_050_15', 5)	# 129-133
    sprite('Action_050_16', 5)	# 134-138
    sprite('Action_050_17', 5)	# 139-143
    label(5)
    sprite('Action_000_00', 7)	# 144-150	 **attackbox here**
    sprite('Action_000_01', 5)	# 151-155	 **attackbox here**
    sprite('Action_000_02', 12)	# 156-167	 **attackbox here**
    sprite('Action_000_03', 14)	# 168-181	 **attackbox here**
    sprite('Action_000_04', 30)	# 182-211	 **attackbox here**
    sprite('Action_000_05', 9)	# 212-220	 **attackbox here**
    sprite('Action_000_06', 6)	# 221-226	 **attackbox here**
    sprite('Action_000_07', 8)	# 227-234	 **attackbox here**
    sprite('Action_000_08', 14)	# 235-248	 **attackbox here**
    sprite('Action_000_09', 17)	# 249-265	 **attackbox here**
    sprite('Action_000_10', 17)	# 266-282	 **attackbox here**
    sprite('Action_000_11', 12)	# 283-294	 **attackbox here**
    loopRest()
    gotoLabel(5)
    ExitState()
    label(10)
    sprite('Action_000_00', 1)	# 295-295	 **attackbox here**
    SFX_1('uwa601pak')
    label(11)
    sprite('Action_000_00', 7)	# 296-302	 **attackbox here**
    sprite('Action_000_01', 5)	# 303-307	 **attackbox here**
    sprite('Action_000_02', 12)	# 308-319	 **attackbox here**
    sprite('Action_000_03', 14)	# 320-333	 **attackbox here**
    sprite('Action_000_04', 30)	# 334-363	 **attackbox here**
    sprite('Action_000_05', 9)	# 364-372	 **attackbox here**
    sprite('Action_000_06', 6)	# 373-378	 **attackbox here**
    sprite('Action_000_07', 8)	# 379-386	 **attackbox here**
    sprite('Action_000_08', 14)	# 387-400	 **attackbox here**
    sprite('Action_000_09', 17)	# 401-417	 **attackbox here**
    sprite('Action_000_10', 17)	# 418-434	 **attackbox here**
    sprite('Action_000_11', 12)	# 435-446	 **attackbox here**
    gotoLabel(11)
    label(100)
    sprite('Action_000_00', 1)	# 447-447	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1210000)
    else:
        Unknown1000(-1525000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Action_000_00', 7)	# 448-454	 **attackbox here**
    sprite('Action_000_01', 5)	# 455-459	 **attackbox here**
    sprite('Action_000_02', 12)	# 460-471	 **attackbox here**
    sprite('Action_000_03', 14)	# 472-485	 **attackbox here**
    sprite('Action_000_04', 30)	# 486-515	 **attackbox here**
    sprite('Action_000_05', 9)	# 516-524	 **attackbox here**
    sprite('Action_000_06', 6)	# 525-530	 **attackbox here**
    sprite('Action_000_07', 8)	# 531-538	 **attackbox here**
    sprite('Action_000_08', 14)	# 539-552	 **attackbox here**
    sprite('Action_000_09', 17)	# 553-569	 **attackbox here**
    sprite('Action_000_10', 17)	# 570-586	 **attackbox here**
    sprite('Action_000_11', 12)	# 587-598	 **attackbox here**
    gotoLabel(101)
    label(102)
    sprite('Action_000_00', 7)	# 599-605	 **attackbox here**
    SFX_1('uwa601btg')
    sprite('Action_053_00', 2)	# 606-607
    sprite('Action_053_01', 4)	# 608-611
    sprite('Action_053_02', 12)	# 612-623
    sprite('Action_053_03', 2)	# 624-625
    SFX_3('SE002')
    sprite('Action_053_04', 2)	# 626-627
    sprite('Action_053_05', 2)	# 628-629
    sprite('Action_053_06', 40)	# 630-669
    sprite('Action_053_07', 6)	# 670-675
    sprite('Action_053_01', 4)	# 676-679
    sprite('Action_053_08', 5)	# 680-684
    label(103)
    sprite('Action_053_09', 4)	# 685-688
    sprite('Action_053_10', 4)	# 689-692
    loopRest()
    if SLOT_97:
        _gotolabel(103)
    sprite('Action_050_15', 5)	# 693-697
    sprite('Action_050_16', 5)	# 698-702
    sprite('Action_050_17', 5)	# 703-707
    Unknown21011(120)
    label(104)
    sprite('Action_000_00', 7)	# 708-714	 **attackbox here**
    sprite('Action_000_01', 5)	# 715-719	 **attackbox here**
    sprite('Action_000_02', 12)	# 720-731	 **attackbox here**
    sprite('Action_000_03', 14)	# 732-745	 **attackbox here**
    sprite('Action_000_04', 30)	# 746-775	 **attackbox here**
    sprite('Action_000_05', 9)	# 776-784	 **attackbox here**
    sprite('Action_000_06', 6)	# 785-790	 **attackbox here**
    sprite('Action_000_07', 8)	# 791-798	 **attackbox here**
    sprite('Action_000_08', 14)	# 799-812	 **attackbox here**
    sprite('Action_000_09', 17)	# 813-829	 **attackbox here**
    sprite('Action_000_10', 17)	# 830-846	 **attackbox here**
    sprite('Action_000_11', 12)	# 847-858	 **attackbox here**
    gotoLabel(104)
    ExitState()
    label(110)
    sprite('Action_000_00', 7)	# 859-865	 **attackbox here**
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('uwa600baz')
    sprite('Action_053_00', 2)	# 866-867
    sprite('Action_053_01', 4)	# 868-871
    sprite('Action_053_02', 12)	# 872-883
    sprite('Action_053_03', 2)	# 884-885
    SFX_3('SE002')
    sprite('Action_053_04', 2)	# 886-887
    sprite('Action_053_05', 2)	# 888-889
    sprite('Action_053_06', 80)	# 890-969
    sprite('Action_053_07', 6)	# 970-975
    sprite('Action_053_01', 4)	# 976-979
    sprite('Action_053_08', 5)	# 980-984
    label(111)
    sprite('Action_053_09', 4)	# 985-988
    sprite('Action_053_10', 4)	# 989-992
    if SLOT_97:
        _gotolabel(111)
    sprite('Action_053_09', 4)	# 993-996
    sprite('Action_053_10', 4)	# 997-1000
    sprite('Action_053_09', 4)	# 1001-1004
    sprite('Action_053_10', 4)	# 1005-1008
    sprite('Action_053_09', 4)	# 1009-1012
    sprite('Action_053_10', 4)	# 1013-1016
    sprite('Action_050_15', 5)	# 1017-1021
    sprite('Action_050_16', 5)	# 1022-1026
    sprite('Action_050_17', 5)	# 1027-1031
    Unknown21011(120)
    label(112)
    sprite('Action_000_00', 7)	# 1032-1038	 **attackbox here**
    sprite('Action_000_01', 5)	# 1039-1043	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_02', 12)	# 1044-1055	 **attackbox here**
    sprite('Action_000_03', 14)	# 1056-1069	 **attackbox here**
    sprite('Action_000_04', 30)	# 1070-1099	 **attackbox here**
    sprite('Action_000_05', 9)	# 1100-1108	 **attackbox here**
    sprite('Action_000_06', 6)	# 1109-1114	 **attackbox here**
    sprite('Action_000_07', 8)	# 1115-1122	 **attackbox here**
    sprite('Action_000_08', 14)	# 1123-1136	 **attackbox here**
    sprite('Action_000_09', 17)	# 1137-1153	 **attackbox here**
    sprite('Action_000_10', 17)	# 1154-1170	 **attackbox here**
    sprite('Action_000_11', 12)	# 1171-1182	 **attackbox here**
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('Action_050_02', 5)	# 1183-1187
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(2500)
    sendToLabelUpon(2, 122)
    label(121)
    sprite('Action_050_02', 3)	# 1188-1190
    loopRest()
    gotoLabel(121)
    label(122)
    sprite('Action_050_03', 40)	# 1191-1230
    SFX_1('uwa600bjb')
    SFX_3('SE025_BoundBig')
    ScreenShake(0, 10000)
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    sprite('Action_050_04', 6)	# 1231-1236
    sprite('Action_050_05', 6)	# 1237-1242
    sprite('Action_050_06', 6)	# 1243-1248
    sprite('Action_050_15', 6)	# 1249-1254
    sprite('Action_050_17', 6)	# 1255-1260
    sprite('Action_000_00', 7)	# 1261-1267	 **attackbox here**
    sprite('Action_000_01', 5)	# 1268-1272	 **attackbox here**
    sprite('Action_000_02', 12)	# 1273-1284	 **attackbox here**
    sprite('Action_000_03', 14)	# 1285-1298	 **attackbox here**
    sprite('Action_000_04', 30)	# 1299-1328	 **attackbox here**
    sprite('Action_000_05', 9)	# 1329-1337	 **attackbox here**
    sprite('Action_000_06', 6)	# 1338-1343	 **attackbox here**
    sprite('Action_000_07', 8)	# 1344-1351	 **attackbox here**
    sprite('Action_000_08', 14)	# 1352-1365	 **attackbox here**
    sprite('Action_000_09', 17)	# 1366-1382	 **attackbox here**
    sprite('Action_000_10', 17)	# 1383-1399	 **attackbox here**
    sprite('Action_000_11', 12)	# 1400-1411	 **attackbox here**
    sprite('Action_000_00', 7)	# 1412-1418	 **attackbox here**
    sprite('Action_000_01', 5)	# 1419-1423	 **attackbox here**
    sprite('Action_000_02', 12)	# 1424-1435	 **attackbox here**
    sprite('Action_000_03', 14)	# 1436-1449	 **attackbox here**
    sprite('Action_000_04', 30)	# 1450-1479	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    sprite('Action_000_05', 9)	# 1480-1488	 **attackbox here**
    sprite('Action_000_06', 6)	# 1489-1494	 **attackbox here**
    sprite('Action_000_07', 8)	# 1495-1502	 **attackbox here**
    sprite('Action_000_08', 14)	# 1503-1516	 **attackbox here**
    sprite('Action_000_09', 17)	# 1517-1533	 **attackbox here**
    sprite('Action_000_10', 17)	# 1534-1550	 **attackbox here**
    sprite('Action_000_11', 12)	# 1551-1562	 **attackbox here**
    sprite('Action_000_00', 1)	# 1563-1563	 **attackbox here**
    label(124)
    sprite('Action_000_00', 7)	# 1564-1570	 **attackbox here**
    sprite('Action_000_01', 5)	# 1571-1575	 **attackbox here**
    sprite('Action_000_02', 12)	# 1576-1587	 **attackbox here**
    sprite('Action_000_03', 14)	# 1588-1601	 **attackbox here**
    sprite('Action_000_04', 30)	# 1602-1631	 **attackbox here**
    sprite('Action_000_05', 9)	# 1632-1640	 **attackbox here**
    sprite('Action_000_06', 6)	# 1641-1646	 **attackbox here**
    sprite('Action_000_07', 8)	# 1647-1654	 **attackbox here**
    sprite('Action_000_08', 14)	# 1655-1668	 **attackbox here**
    sprite('Action_000_09', 17)	# 1669-1685	 **attackbox here**
    sprite('Action_000_10', 17)	# 1686-1702	 **attackbox here**
    sprite('Action_000_11', 12)	# 1703-1714	 **attackbox here**
    gotoLabel(124)
    ExitState()
    label(130)
    sprite('Action_050_02', 5)	# 1715-1719
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1495000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(2500)
    sendToLabelUpon(2, 132)
    SFX_1('uwa600pce')
    label(131)
    sprite('Action_050_02', 2)	# 1720-1721
    sprite('Action_050_02', 1)	# 1722-1722
    gotoLabel(131)
    label(132)
    sprite('Action_050_03', 7)	# 1723-1729
    SFX_3('SE025_BoundBig')
    ScreenShake(0, 10000)
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    sprite('Action_050_04', 15)	# 1730-1744
    sprite('Action_050_05', 12)	# 1745-1756
    sprite('Action_050_06', 7)	# 1757-1763
    sprite('Action_050_07', 5)	# 1764-1768
    sprite('Action_050_08', 5)	# 1769-1773
    sprite('Action_050_09', 5)	# 1774-1778
    sprite('Action_050_10', 5)	# 1779-1783
    sprite('Action_050_09', 5)	# 1784-1788
    sprite('Action_050_10', 5)	# 1789-1793
    sprite('Action_050_09', 5)	# 1794-1798
    sprite('Action_050_10', 5)	# 1799-1803
    sprite('Action_050_09', 5)	# 1804-1808
    sprite('Action_050_10', 5)	# 1809-1813
    label(133)
    sprite('Action_050_11', 5)	# 1814-1818
    sprite('Action_050_12', 5)	# 1819-1823
    if SLOT_97:
        _gotolabel(133)
    sprite('Action_050_13', 8)	# 1824-1831
    sprite('Action_050_14', 8)	# 1832-1839
    sprite('Action_050_15', 5)	# 1840-1844
    sprite('Action_050_16', 5)	# 1845-1849
    sprite('Action_050_17', 5)	# 1850-1854
    Unknown21007(24, 40)
    Unknown21011(120)
    label(134)
    sprite('Action_000_00', 7)	# 1855-1861	 **attackbox here**
    sprite('Action_000_01', 5)	# 1862-1866	 **attackbox here**
    sprite('Action_000_02', 12)	# 1867-1878	 **attackbox here**
    sprite('Action_000_03', 14)	# 1879-1892	 **attackbox here**
    sprite('Action_000_04', 30)	# 1893-1922	 **attackbox here**
    sprite('Action_000_05', 9)	# 1923-1931	 **attackbox here**
    sprite('Action_000_06', 6)	# 1932-1937	 **attackbox here**
    sprite('Action_000_07', 8)	# 1938-1945	 **attackbox here**
    sprite('Action_000_08', 14)	# 1946-1959	 **attackbox here**
    sprite('Action_000_09', 17)	# 1960-1976	 **attackbox here**
    sprite('Action_000_10', 17)	# 1977-1993	 **attackbox here**
    sprite('Action_000_11', 12)	# 1994-2005	 **attackbox here**
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('Action_000_00', 7)	# 2006-2012	 **attackbox here**
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('uwa600uhy')
    sprite('Action_000_01', 5)	# 2013-2017	 **attackbox here**
    sprite('Action_000_02', 12)	# 2018-2029	 **attackbox here**
    sprite('Action_000_03', 14)	# 2030-2043	 **attackbox here**
    sprite('Action_000_04', 30)	# 2044-2073	 **attackbox here**
    sprite('Action_053_00', 2)	# 2074-2075
    sprite('Action_053_01', 4)	# 2076-2079
    sprite('Action_053_02', 12)	# 2080-2091
    sprite('Action_053_03', 2)	# 2092-2093
    SFX_3('SE002')
    sprite('Action_053_04', 2)	# 2094-2095
    sprite('Action_053_05', 2)	# 2096-2097
    sprite('Action_053_06', 80)	# 2098-2177
    sprite('Action_053_07', 6)	# 2178-2183
    sprite('Action_053_01', 4)	# 2184-2187
    sprite('Action_053_08', 5)	# 2188-2192
    label(141)
    sprite('Action_053_09', 4)	# 2193-2196
    sprite('Action_053_10', 4)	# 2197-2200
    if SLOT_97:
        _gotolabel(141)
    sprite('Action_053_09', 4)	# 2201-2204
    sprite('Action_053_10', 4)	# 2205-2208
    sprite('Action_053_09', 4)	# 2209-2212
    sprite('Action_053_10', 4)	# 2213-2216
    sprite('Action_053_09', 4)	# 2217-2220
    sprite('Action_053_10', 4)	# 2221-2224
    sprite('Action_050_15', 5)	# 2225-2229
    sprite('Action_050_16', 5)	# 2230-2234
    sprite('Action_050_17', 5)	# 2235-2239
    Unknown21007(24, 40)
    Unknown21011(120)
    label(142)
    sprite('Action_000_00', 7)	# 2240-2246	 **attackbox here**
    sprite('Action_000_01', 5)	# 2247-2251	 **attackbox here**
    sprite('Action_000_02', 12)	# 2252-2263	 **attackbox here**
    sprite('Action_000_03', 14)	# 2264-2277	 **attackbox here**
    sprite('Action_000_04', 30)	# 2278-2307	 **attackbox here**
    sprite('Action_000_05', 9)	# 2308-2316	 **attackbox here**
    sprite('Action_000_06', 6)	# 2317-2322	 **attackbox here**
    sprite('Action_000_07', 8)	# 2323-2330	 **attackbox here**
    sprite('Action_000_08', 14)	# 2331-2344	 **attackbox here**
    sprite('Action_000_09', 17)	# 2345-2361	 **attackbox here**
    sprite('Action_000_10', 17)	# 2362-2378	 **attackbox here**
    sprite('Action_000_11', 12)	# 2379-2390	 **attackbox here**
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('null', 1)	# 2391-2391
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1220000)
    else:
        Unknown1000(-1495000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(151)
    sprite('null', 32767)	# 2392-35158
    label(151)
    sprite('Action_050_02', 5)	# 35159-35163
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(2500)
    sendToLabelUpon(2, 153)
    label(152)
    sprite('Action_050_02', 3)	# 35164-35166
    loopRest()
    gotoLabel(152)
    label(153)
    sprite('Action_050_03', 40)	# 35167-35206
    SFX_1('uwa601ugo')
    SFX_3('SE025_BoundBig')
    ScreenShake(0, 10000)
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    sprite('Action_050_04', 6)	# 35207-35212
    sprite('Action_050_05', 6)	# 35213-35218
    sprite('Action_050_06', 6)	# 35219-35224
    sprite('Action_050_15', 6)	# 35225-35230
    sprite('Action_050_17', 6)	# 35231-35236
    Unknown23018(1)
    label(154)
    sprite('Action_000_00', 7)	# 35237-35243	 **attackbox here**
    sprite('Action_000_01', 5)	# 35244-35248	 **attackbox here**
    sprite('Action_000_02', 12)	# 35249-35260	 **attackbox here**
    sprite('Action_000_03', 14)	# 35261-35274	 **attackbox here**
    sprite('Action_000_04', 30)	# 35275-35304	 **attackbox here**
    sprite('Action_000_05', 9)	# 35305-35313	 **attackbox here**
    sprite('Action_000_06', 6)	# 35314-35319	 **attackbox here**
    sprite('Action_000_07', 8)	# 35320-35327	 **attackbox here**
    sprite('Action_000_08', 14)	# 35328-35341	 **attackbox here**
    sprite('Action_000_09', 17)	# 35342-35358	 **attackbox here**
    sprite('Action_000_10', 17)	# 35359-35375	 **attackbox here**
    sprite('Action_000_11', 12)	# 35376-35387	 **attackbox here**
    if SLOT_97:
        _gotolabel(154)
    sprite('Action_000_00', 1)	# 35388-35388	 **attackbox here**
    label(155)
    sprite('Action_000_00', 7)	# 35389-35395	 **attackbox here**
    sprite('Action_000_01', 5)	# 35396-35400	 **attackbox here**
    sprite('Action_000_02', 12)	# 35401-35412	 **attackbox here**
    sprite('Action_000_03', 14)	# 35413-35426	 **attackbox here**
    sprite('Action_000_04', 30)	# 35427-35456	 **attackbox here**
    sprite('Action_000_05', 9)	# 35457-35465	 **attackbox here**
    sprite('Action_000_06', 6)	# 35466-35471	 **attackbox here**
    sprite('Action_000_07', 8)	# 35472-35479	 **attackbox here**
    sprite('Action_000_08', 14)	# 35480-35493	 **attackbox here**
    sprite('Action_000_09', 17)	# 35494-35510	 **attackbox here**
    sprite('Action_000_10', 17)	# 35511-35527	 **attackbox here**
    sprite('Action_000_11', 12)	# 35528-35539	 **attackbox here**
    gotoLabel(155)
    ExitState()
    label(160)
    sprite('Wal637_00', 1)	# 35540-35540	 **attackbox here**
    Unknown2019(100)
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    SFX_1('uwa600uli')
    label(161)
    sprite('Wal637_00', 1)	# 35541-35541	 **attackbox here**
    if SLOT_97:
        _gotolabel(161)
    sprite('Wal637_00', 30)	# 35542-35571	 **attackbox here**
    sprite('Wal637_00', 32767)	# 35572-68338	 **attackbox here**
    Unknown21007(24, 40)
    label(162)
    sprite('Wal637_01', 6)	# 68339-68344	 **attackbox here**
    sprite('Wal637_02', 6)	# 68345-68350	 **attackbox here**
    sprite('Wal637_03', 6)	# 68351-68356
    Unknown21011(120)
    label(163)
    sprite('Action_000_00', 7)	# 68357-68363	 **attackbox here**
    sprite('Action_000_01', 5)	# 68364-68368	 **attackbox here**
    sprite('Action_000_02', 12)	# 68369-68380	 **attackbox here**
    sprite('Action_000_03', 14)	# 68381-68394	 **attackbox here**
    sprite('Action_000_04', 30)	# 68395-68424	 **attackbox here**
    sprite('Action_000_05', 9)	# 68425-68433	 **attackbox here**
    sprite('Action_000_06', 6)	# 68434-68439	 **attackbox here**
    sprite('Action_000_07', 8)	# 68440-68447	 **attackbox here**
    sprite('Action_000_08', 14)	# 68448-68461	 **attackbox here**
    sprite('Action_000_09', 17)	# 68462-68478	 **attackbox here**
    sprite('Action_000_10', 17)	# 68479-68495	 **attackbox here**
    sprite('Action_000_11', 12)	# 68496-68507	 **attackbox here**
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('Action_050_02', 5)	# 68508-68512
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(2500)
    sendToLabelUpon(2, 172)
    label(171)
    sprite('Action_050_02', 3)	# 68513-68515
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('Action_050_03', 7)	# 68516-68522
    SFX_3('SE025_BoundBig')
    ScreenShake(0, 10000)
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    sprite('Action_050_04', 15)	# 68523-68537
    sprite('Action_050_05', 12)	# 68538-68549
    sprite('Action_050_06', 7)	# 68550-68556
    sprite('Action_050_07', 5)	# 68557-68561
    SFX_1('uwa600uca')
    sprite('Action_050_08', 5)	# 68562-68566
    sprite('Action_050_09', 5)	# 68567-68571
    sprite('Action_050_10', 5)	# 68572-68576
    sprite('Action_050_09', 5)	# 68577-68581
    sprite('Action_050_10', 5)	# 68582-68586
    sprite('Action_050_09', 5)	# 68587-68591
    sprite('Action_050_10', 5)	# 68592-68596
    sprite('Action_050_09', 5)	# 68597-68601
    sprite('Action_050_10', 5)	# 68602-68606
    label(173)
    sprite('Action_050_11', 5)	# 68607-68611
    sprite('Action_050_12', 5)	# 68612-68616
    if SLOT_97:
        _gotolabel(173)
    sprite('Action_050_15', 5)	# 68617-68621
    sprite('Action_050_16', 5)	# 68622-68626
    sprite('Action_050_17', 5)	# 68627-68631
    Unknown21007(24, 40)
    Unknown21011(300)
    label(174)
    sprite('Action_000_00', 7)	# 68632-68638	 **attackbox here**
    sprite('Action_000_01', 5)	# 68639-68643	 **attackbox here**
    sprite('Action_000_02', 12)	# 68644-68655	 **attackbox here**
    sprite('Action_000_03', 14)	# 68656-68669	 **attackbox here**
    sprite('Action_000_04', 30)	# 68670-68699	 **attackbox here**
    sprite('Action_000_05', 9)	# 68700-68708	 **attackbox here**
    sprite('Action_000_06', 6)	# 68709-68714	 **attackbox here**
    sprite('Action_000_07', 8)	# 68715-68722	 **attackbox here**
    sprite('Action_000_08', 14)	# 68723-68736	 **attackbox here**
    sprite('Action_000_09', 17)	# 68737-68753	 **attackbox here**
    sprite('Action_000_10', 17)	# 68754-68770	 **attackbox here**
    sprite('Action_000_11', 12)	# 68771-68782	 **attackbox here**
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('Action_000_00', 1)	# 68783-68783	 **attackbox here**
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1200000)
    else:
        Unknown1000(-1495000)
    SFX_1('uwa600ryn_1')
    label(181)
    sprite('Action_000_00', 7)	# 68784-68790	 **attackbox here**
    sprite('Action_000_01', 5)	# 68791-68795	 **attackbox here**
    sprite('Action_000_02', 12)	# 68796-68807	 **attackbox here**
    sprite('Action_000_03', 14)	# 68808-68821	 **attackbox here**
    sprite('Action_000_04', 30)	# 68822-68851	 **attackbox here**
    sprite('Action_000_05', 9)	# 68852-68860	 **attackbox here**
    sprite('Action_000_06', 6)	# 68861-68866	 **attackbox here**
    sprite('Action_000_07', 8)	# 68867-68874	 **attackbox here**
    sprite('Action_000_08', 14)	# 68875-68888	 **attackbox here**
    sprite('Action_000_09', 17)	# 68889-68905	 **attackbox here**
    sprite('Action_000_10', 17)	# 68906-68922	 **attackbox here**
    sprite('Action_000_11', 12)	# 68923-68934	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_000_00', 1)	# 68935-68935	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    label(182)
    sprite('Action_000_00', 7)	# 68936-68942	 **attackbox here**
    sprite('Action_000_01', 5)	# 68943-68947	 **attackbox here**
    sprite('Action_000_02', 12)	# 68948-68959	 **attackbox here**
    sprite('Action_000_03', 14)	# 68960-68973	 **attackbox here**
    sprite('Action_000_04', 30)	# 68974-69003	 **attackbox here**
    sprite('Action_000_05', 9)	# 69004-69012	 **attackbox here**
    sprite('Action_000_06', 6)	# 69013-69018	 **attackbox here**
    sprite('Action_000_07', 8)	# 69019-69026	 **attackbox here**
    sprite('Action_000_08', 14)	# 69027-69040	 **attackbox here**
    sprite('Action_000_09', 17)	# 69041-69057	 **attackbox here**
    sprite('Action_000_10', 17)	# 69058-69074	 **attackbox here**
    sprite('Action_000_11', 12)	# 69075-69086	 **attackbox here**
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('Action_050_02', 5)	# 69087-69091
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(2500)
    sendToLabelUpon(2, 192)
    SFX_1('uwa600umi')
    label(191)
    sprite('Action_050_02', 2)	# 69092-69093
    sprite('Action_050_02', 1)	# 69094-69094
    gotoLabel(191)
    label(192)
    sprite('Action_050_03', 7)	# 69095-69101
    SFX_3('SE025_BoundBig')
    ScreenShake(0, 10000)
    clearUponHandler(2)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 0)
    Unknown8000(100, 1, 1)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    sprite('Action_050_04', 55)	# 69102-69156
    sprite('Action_050_05', 12)	# 69157-69168
    sprite('Action_050_06', 7)	# 69169-69175
    sprite('Action_050_07', 5)	# 69176-69180
    sprite('Action_050_08', 5)	# 69181-69185
    sprite('Action_050_09', 5)	# 69186-69190
    sprite('Action_050_10', 5)	# 69191-69195
    sprite('Action_050_09', 5)	# 69196-69200
    sprite('Action_050_10', 5)	# 69201-69205
    sprite('Action_050_09', 5)	# 69206-69210
    sprite('Action_050_10', 5)	# 69211-69215
    sprite('Action_050_09', 5)	# 69216-69220
    sprite('Action_050_10', 5)	# 69221-69225
    label(193)
    sprite('Action_050_11', 5)	# 69226-69230
    sprite('Action_050_12', 5)	# 69231-69235
    if SLOT_97:
        _gotolabel(193)
    sprite('Action_050_13', 8)	# 69236-69243
    sprite('Action_050_14', 8)	# 69244-69251
    sprite('Action_050_15', 5)	# 69252-69256
    sprite('Action_050_16', 5)	# 69257-69261
    sprite('Action_050_17', 5)	# 69262-69266
    Unknown21007(24, 40)
    Unknown21011(200)
    label(194)
    sprite('Action_000_00', 7)	# 69267-69273	 **attackbox here**
    sprite('Action_000_01', 5)	# 69274-69278	 **attackbox here**
    sprite('Action_000_02', 12)	# 69279-69290	 **attackbox here**
    sprite('Action_000_03', 14)	# 69291-69304	 **attackbox here**
    sprite('Action_000_04', 30)	# 69305-69334	 **attackbox here**
    sprite('Action_000_05', 9)	# 69335-69343	 **attackbox here**
    sprite('Action_000_06', 6)	# 69344-69349	 **attackbox here**
    sprite('Action_000_07', 8)	# 69350-69357	 **attackbox here**
    sprite('Action_000_08', 14)	# 69358-69371	 **attackbox here**
    sprite('Action_000_09', 17)	# 69372-69388	 **attackbox here**
    sprite('Action_000_10', 17)	# 69389-69405	 **attackbox here**
    sprite('Action_000_11', 12)	# 69406-69417	 **attackbox here**
    gotoLabel(194)
    ExitState()
    label(200)
    sprite('Action_000_00', 1)	# 69418-69418	 **attackbox here**
    Unknown2019(1000)
    if SLOT_158:
        Unknown1000(-1200000)
    else:
        Unknown1000(-1200000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('uwa601pak')
        Unknown23018(1)
    label(201)
    sprite('Action_000_00', 7)	# 69419-69425	 **attackbox here**
    sprite('Action_000_01', 5)	# 69426-69430	 **attackbox here**
    sprite('Action_000_02', 12)	# 69431-69442	 **attackbox here**
    sprite('Action_000_03', 14)	# 69443-69456	 **attackbox here**
    sprite('Action_000_04', 30)	# 69457-69486	 **attackbox here**
    sprite('Action_000_05', 9)	# 69487-69495	 **attackbox here**
    sprite('Action_000_06', 6)	# 69496-69501	 **attackbox here**
    sprite('Action_000_07', 8)	# 69502-69509	 **attackbox here**
    sprite('Action_000_08', 14)	# 69510-69523	 **attackbox here**
    sprite('Action_000_09', 17)	# 69524-69540	 **attackbox here**
    sprite('Action_000_10', 17)	# 69541-69557	 **attackbox here**
    sprite('Action_000_11', 12)	# 69558-69569	 **attackbox here**
    gotoLabel(201)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 69570-69570	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 7)	# 69571-69577	 **attackbox here**
    sprite('Action_000_01', 5)	# 69578-69582	 **attackbox here**
    sprite('Action_000_02', 12)	# 69583-69594	 **attackbox here**
    sprite('Action_000_03', 14)	# 69595-69608	 **attackbox here**
    sprite('Action_000_04', 30)	# 69609-69638	 **attackbox here**
    sprite('Action_000_05', 9)	# 69639-69647	 **attackbox here**
    sprite('Action_000_06', 6)	# 69648-69653	 **attackbox here**
    sprite('Action_000_07', 8)	# 69654-69661	 **attackbox here**
    sprite('Action_000_08', 14)	# 69662-69675	 **attackbox here**
    sprite('Action_000_09', 17)	# 69676-69692	 **attackbox here**
    sprite('Action_000_10', 17)	# 69693-69709	 **attackbox here**
    sprite('Action_000_11', 12)	# 69710-69721	 **attackbox here**
    gotoLabel(992)
    label(993)
    sprite('Action_046_00', 2)	# 69722-69723

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
    label(994)
    sprite('Action_046_01', 2)	# 69724-69725
    sprite('Action_046_02', 1)	# 69726-69726
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 69727-69729
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
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
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
            if PartnerChar('umi'):
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
    sprite('Action_053_00', 2)	# 4-5
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uwa524', 100, 895580021, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uwa402_0', 100, 878802805, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uwa520', 100, 895580021, 12850, 0, 0, 100, 895580021, 13106, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_053_01', 4)	# 6-9
    sprite('Action_053_02', 12)	# 10-21
    sprite('Action_053_03', 2)	# 22-23
    SFX_3('SE002')
    sprite('Action_053_04', 2)	# 24-25
    sprite('Action_053_05', 2)	# 26-27
    sprite('Action_053_06', 13)	# 28-40
    sprite('Action_053_07', 6)	# 41-46
    Unknown23018(1)
    sprite('Action_053_08', 5)	# 47-51
    label(1000)
    sprite('Action_053_09', 4)	# 52-55
    sprite('Action_053_10', 4)	# 56-59
    loopRest()
    gotoLabel(1000)
    label(10)
    sprite('keep', 1)	# 60-60

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        clearUponHandler(3)
        AttackLevel_(0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        Unknown11056(0)
        Unknown2003(0)
        Unknown11025(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown36(22)
        Unknown23022(0)
        Unknown35()
    sprite('Action_010_00', 3)	# 61-63

    def upon_3():
        if (SLOT_29 <= 450000):
            sendToLabel(12)
    sprite('Action_010_01', 3)	# 64-66
    physicsXImpulse(8000)
    sprite('Action_010_02', 7)	# 67-73
    sprite('Action_010_03', 11)	# 74-84
    Unknown1019(0)
    Unknown8000(100, 1, 1)
    label(11)
    sprite('Action_010_04', 6)	# 85-90
    physicsXImpulse(8000)
    sprite('Action_010_05', 5)	# 91-95
    sprite('Action_010_06', 4)	# 96-99
    sprite('Action_010_07', 4)	# 100-103
    sprite('Action_010_08', 3)	# 104-106
    sprite('Action_010_09', 5)	# 107-111
    sprite('Action_010_10', 7)	# 112-118
    sprite('Action_010_11', 9)	# 119-127
    Unknown1019(0)
    Unknown8000(100, 1, 1)
    sprite('Action_010_12', 6)	# 128-133
    physicsXImpulse(8000)
    sprite('Action_010_13', 5)	# 134-138
    sprite('Action_010_14', 4)	# 139-142
    sprite('Action_010_15', 4)	# 143-146
    sprite('Action_010_16', 3)	# 147-149
    sprite('Action_010_17', 5)	# 150-154
    sprite('Action_010_18', 7)	# 155-161
    Unknown1019(0)
    Unknown8000(100, 1, 1)
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('Action_054_00', 8)	# 162-169
    clearUponHandler(3)
    Unknown1084(1)
    sprite('Action_054_01', 8)	# 170-177
    sprite('Action_054_02', 9)	# 178-186	 **attackbox here**
    RefreshMultihit()
    Unknown36(22)
    Unknown2019(500)
    Unknown35()
    Unknown2019(1000)
    sprite('Action_054_03', 13)	# 187-199
    sprite('Action_054_04', 4)	# 200-203	 **attackbox here**
    sprite('Action_054_05', 5)	# 204-208	 **attackbox here**
    sprite('Action_054_06', 3)	# 209-211	 **attackbox here**
    sprite('Action_054_07', 32767)	# 212-32978	 **attackbox here**
    loopRest()
    ExitState()
    label(100)
    sprite('Action_053_00', 2)	# 32979-32980
    Unknown2019(1000)
    sprite('Action_053_01', 4)	# 32981-32984
    SFX_1('uwa700btg')
    sprite('Action_053_02', 12)	# 32985-32996
    sprite('Action_053_03', 2)	# 32997-32998
    sprite('Action_053_04', 2)	# 32999-33000
    sprite('Action_053_05', 2)	# 33001-33002
    sprite('Action_053_06', 13)	# 33003-33015
    sprite('Action_053_07', 6)	# 33016-33021
    sprite('Action_053_08', 5)	# 33022-33026
    label(101)
    sprite('Action_053_09', 4)	# 33027-33030
    sprite('Action_053_10', 4)	# 33031-33034
    loopRest()
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_053_09', 1)	# 33035-33035
    Unknown21007(24, 40)
    Unknown21011(300)
    label(102)
    sprite('Action_053_09', 4)	# 33036-33039
    sprite('Action_053_10', 4)	# 33040-33043
    loopRest()
    gotoLabel(102)
    label(110)
    sprite('Action_053_00', 2)	# 33044-33045
    Unknown2019(1000)
    SFX_1('uwa700baz')
    sprite('Action_053_01', 4)	# 33046-33049
    sprite('Action_053_02', 12)	# 33050-33061
    sprite('Action_053_03', 2)	# 33062-33063
    sprite('Action_053_04', 2)	# 33064-33065
    sprite('Action_053_05', 2)	# 33066-33067
    sprite('Action_053_06', 13)	# 33068-33080
    sprite('Action_053_07', 6)	# 33081-33086
    sprite('Action_053_08', 5)	# 33087-33091
    label(111)
    sprite('Action_053_09', 4)	# 33092-33095
    sprite('Action_053_10', 4)	# 33096-33099
    loopRest()
    if SLOT_97:
        _gotolabel(111)
    sprite('Action_053_09', 1)	# 33100-33100
    Unknown21007(24, 40)
    Unknown21011(360)
    label(112)
    sprite('Action_053_09', 4)	# 33101-33104
    sprite('Action_053_10', 4)	# 33105-33108
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('Action_000_00', 1)	# 33109-33109	 **attackbox here**
    Unknown2034(0)
    Unknown2053(0)
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
        SFX_1('uwa701bjb')
        Unknown21011(400)
    label(121)
    sprite('Action_000_00', 7)	# 33110-33116	 **attackbox here**
    sprite('Action_000_01', 5)	# 33117-33121	 **attackbox here**
    sprite('Action_000_02', 12)	# 33122-33133	 **attackbox here**
    sprite('Action_000_03', 14)	# 33134-33147	 **attackbox here**
    sprite('Action_000_04', 30)	# 33148-33177	 **attackbox here**
    sprite('Action_000_05', 9)	# 33178-33186	 **attackbox here**
    sprite('Action_000_06', 6)	# 33187-33192	 **attackbox here**
    sprite('Action_000_07', 8)	# 33193-33200	 **attackbox here**
    sprite('Action_000_08', 14)	# 33201-33214	 **attackbox here**
    sprite('Action_000_09', 17)	# 33215-33231	 **attackbox here**
    sprite('Action_000_10', 17)	# 33232-33248	 **attackbox here**
    sprite('Action_000_11', 12)	# 33249-33260	 **attackbox here**
    gotoLabel(121)
    label(122)
    sprite('Action_000_00', 7)	# 33261-33267	 **attackbox here**
    sprite('Action_000_01', 5)	# 33268-33272	 **attackbox here**
    sprite('Action_000_02', 12)	# 33273-33284	 **attackbox here**
    sprite('Action_000_03', 14)	# 33285-33298	 **attackbox here**
    sprite('Action_000_04', 30)	# 33299-33328	 **attackbox here**
    sprite('Action_000_05', 9)	# 33329-33337	 **attackbox here**
    sprite('Action_000_06', 6)	# 33338-33343	 **attackbox here**
    sprite('Action_000_07', 8)	# 33344-33351	 **attackbox here**
    sprite('Action_000_08', 14)	# 33352-33365	 **attackbox here**
    sprite('Action_000_09', 17)	# 33366-33382	 **attackbox here**
    sprite('Action_000_10', 17)	# 33383-33399	 **attackbox here**
    sprite('Action_000_11', 12)	# 33400-33411	 **attackbox here**
    gotoLabel(122)
    label(130)
    sprite('Action_000_00', 1)	# 33412-33412	 **attackbox here**
    Unknown2034(0)
    Unknown2053(0)
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('Action_000_00', 7)	# 33413-33419	 **attackbox here**
    sprite('Action_000_01', 5)	# 33420-33424	 **attackbox here**
    sprite('Action_000_02', 12)	# 33425-33436	 **attackbox here**
    sprite('Action_000_03', 14)	# 33437-33450	 **attackbox here**
    sprite('Action_000_04', 30)	# 33451-33480	 **attackbox here**
    sprite('Action_000_05', 9)	# 33481-33489	 **attackbox here**
    sprite('Action_000_06', 6)	# 33490-33495	 **attackbox here**
    sprite('Action_000_07', 8)	# 33496-33503	 **attackbox here**
    sprite('Action_000_08', 14)	# 33504-33517	 **attackbox here**
    sprite('Action_000_09', 17)	# 33518-33534	 **attackbox here**
    sprite('Action_000_10', 17)	# 33535-33551	 **attackbox here**
    sprite('Action_000_11', 12)	# 33552-33563	 **attackbox here**
    gotoLabel(131)
    label(132)
    sprite('Action_053_00', 2)	# 33564-33565
    sprite('Action_053_01', 4)	# 33566-33569
    sprite('Action_053_02', 12)	# 33570-33581
    sprite('Action_053_03', 2)	# 33582-33583
    sprite('Action_053_04', 2)	# 33584-33585
    sprite('Action_053_05', 2)	# 33586-33587
    sprite('Action_053_06', 13)	# 33588-33600
    sprite('Action_053_07', 6)	# 33601-33606
    sprite('Action_053_08', 5)	# 33607-33611
    SFX_1('uwa701pce')
    label(133)
    sprite('Action_053_09', 4)	# 33612-33615
    sprite('Action_053_10', 4)	# 33616-33619
    loopRest()
    if SLOT_97:
        _gotolabel(133)
    sprite('Action_053_09', 1)	# 33620-33620
    Unknown18008()
    label(134)
    sprite('Action_053_09', 4)	# 33621-33624
    sprite('Action_053_10', 4)	# 33625-33628
    loopRest()
    gotoLabel(134)
    label(140)
    sprite('Action_000_00', 1)	# 33629-33629	 **attackbox here**
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
        SFX_1('uwa701uhy')
        Unknown21011(200)
    label(141)
    sprite('Action_000_00', 7)	# 33630-33636	 **attackbox here**
    sprite('Action_000_01', 5)	# 33637-33641	 **attackbox here**
    sprite('Action_000_02', 12)	# 33642-33653	 **attackbox here**
    sprite('Action_000_03', 14)	# 33654-33667	 **attackbox here**
    sprite('Action_000_04', 30)	# 33668-33697	 **attackbox here**
    sprite('Action_000_05', 9)	# 33698-33706	 **attackbox here**
    sprite('Action_000_06', 6)	# 33707-33712	 **attackbox here**
    sprite('Action_000_07', 8)	# 33713-33720	 **attackbox here**
    sprite('Action_000_08', 14)	# 33721-33734	 **attackbox here**
    sprite('Action_000_09', 17)	# 33735-33751	 **attackbox here**
    sprite('Action_000_10', 17)	# 33752-33768	 **attackbox here**
    sprite('Action_000_11', 12)	# 33769-33780	 **attackbox here**
    gotoLabel(141)
    label(142)
    sprite('Action_000_00', 7)	# 33781-33787	 **attackbox here**
    sprite('Action_000_01', 5)	# 33788-33792	 **attackbox here**
    sprite('Action_000_02', 12)	# 33793-33804	 **attackbox here**
    sprite('Action_000_03', 14)	# 33805-33818	 **attackbox here**
    sprite('Action_000_04', 30)	# 33819-33848	 **attackbox here**
    sprite('Action_000_05', 9)	# 33849-33857	 **attackbox here**
    sprite('Action_000_06', 6)	# 33858-33863	 **attackbox here**
    sprite('Action_000_07', 8)	# 33864-33871	 **attackbox here**
    sprite('Action_000_08', 14)	# 33872-33885	 **attackbox here**
    sprite('Action_000_09', 17)	# 33886-33902	 **attackbox here**
    sprite('Action_000_10', 17)	# 33903-33919	 **attackbox here**
    sprite('Action_000_11', 12)	# 33920-33931	 **attackbox here**
    gotoLabel(142)
    label(150)
    sprite('Action_053_00', 2)	# 33932-33933
    Unknown2019(1000)
    sprite('Action_053_01', 4)	# 33934-33937
    sprite('Action_053_02', 12)	# 33938-33949
    sprite('Action_053_03', 2)	# 33950-33951
    sprite('Action_053_04', 2)	# 33952-33953
    sprite('Action_053_05', 2)	# 33954-33955
    sprite('Action_053_06', 13)	# 33956-33968
    sprite('Action_053_07', 6)	# 33969-33974
    sprite('Action_053_08', 5)	# 33975-33979
    SFX_1('uwa700uli')
    label(151)
    sprite('Action_053_09', 4)	# 33980-33983
    sprite('Action_053_10', 4)	# 33984-33987
    loopRest()
    if SLOT_97:
        _gotolabel(151)
    sprite('Action_053_09', 1)	# 33988-33988
    Unknown21007(24, 40)
    Unknown21011(240)
    label(152)
    sprite('Action_053_09', 4)	# 33989-33992
    sprite('Action_053_10', 4)	# 33993-33996
    loopRest()
    gotoLabel(152)
    label(160)
    sprite('Action_053_00', 2)	# 33997-33998
    Unknown2019(1000)
    sprite('Action_053_01', 4)	# 33999-34002
    SFX_1('uwa700ugo')
    sprite('Action_053_02', 12)	# 34003-34014
    sprite('Action_053_03', 2)	# 34015-34016
    sprite('Action_053_04', 2)	# 34017-34018
    sprite('Action_053_05', 2)	# 34019-34020
    sprite('Action_053_06', 13)	# 34021-34033
    sprite('Action_053_07', 6)	# 34034-34039
    sprite('Action_053_08', 5)	# 34040-34044
    label(161)
    sprite('Action_053_09', 4)	# 34045-34048
    sprite('Action_053_10', 4)	# 34049-34052
    loopRest()
    if SLOT_97:
        _gotolabel(161)
    sprite('Action_053_09', 1)	# 34053-34053
    Unknown21007(24, 40)
    Unknown21011(480)
    label(162)
    sprite('Action_053_09', 4)	# 34054-34057
    sprite('Action_053_10', 4)	# 34058-34061
    loopRest()
    gotoLabel(162)
    label(170)
    sprite('Action_000_00', 7)	# 34062-34068	 **attackbox here**
    Unknown2019(1000)
    sprite('Action_000_01', 5)	# 34069-34073	 **attackbox here**
    SFX_1('uwa700uca')
    sprite('Action_000_02', 12)	# 34074-34085	 **attackbox here**
    sprite('Action_000_03', 14)	# 34086-34099	 **attackbox here**
    sprite('Action_000_04', 30)	# 34100-34129	 **attackbox here**
    sprite('Action_000_05', 9)	# 34130-34138	 **attackbox here**
    sprite('Action_000_06', 6)	# 34139-34144	 **attackbox here**
    sprite('Action_000_07', 8)	# 34145-34152	 **attackbox here**
    sprite('Action_000_08', 14)	# 34153-34166	 **attackbox here**
    sprite('Action_000_09', 17)	# 34167-34183	 **attackbox here**
    sprite('Action_000_10', 17)	# 34184-34200	 **attackbox here**
    sprite('Action_000_11', 12)	# 34201-34212	 **attackbox here**
    sprite('Action_000_00', 7)	# 34213-34219	 **attackbox here**
    sprite('Action_000_01', 5)	# 34220-34224	 **attackbox here**
    sprite('Action_000_02', 12)	# 34225-34236	 **attackbox here**
    sprite('Action_000_03', 14)	# 34237-34250	 **attackbox here**
    sprite('Action_000_04', 30)	# 34251-34280	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    sprite('Action_000_05', 9)	# 34281-34289	 **attackbox here**
    sprite('Action_000_06', 6)	# 34290-34295	 **attackbox here**
    sprite('Action_000_07', 8)	# 34296-34303	 **attackbox here**
    sprite('Action_000_08', 14)	# 34304-34317	 **attackbox here**
    sprite('Action_000_09', 17)	# 34318-34334	 **attackbox here**
    sprite('Action_000_10', 17)	# 34335-34351	 **attackbox here**
    sprite('Action_000_11', 12)	# 34352-34363	 **attackbox here**
    label(171)
    sprite('Action_000_00', 7)	# 34364-34370	 **attackbox here**
    sprite('Action_000_01', 5)	# 34371-34375	 **attackbox here**
    sprite('Action_000_02', 12)	# 34376-34387	 **attackbox here**
    sprite('Action_000_03', 14)	# 34388-34401	 **attackbox here**
    sprite('Action_000_04', 30)	# 34402-34431	 **attackbox here**
    sprite('Action_000_05', 9)	# 34432-34440	 **attackbox here**
    sprite('Action_000_06', 6)	# 34441-34446	 **attackbox here**
    sprite('Action_000_07', 8)	# 34447-34454	 **attackbox here**
    sprite('Action_000_08', 14)	# 34455-34468	 **attackbox here**
    sprite('Action_000_09', 17)	# 34469-34485	 **attackbox here**
    sprite('Action_000_10', 17)	# 34486-34502	 **attackbox here**
    sprite('Action_000_11', 12)	# 34503-34514	 **attackbox here**
    gotoLabel(171)
    label(180)
    sprite('Action_053_00', 2)	# 34515-34516
    Unknown2019(1000)
    sprite('Action_053_01', 4)	# 34517-34520
    SFX_1('uwa700ryn')
    sprite('Action_053_02', 12)	# 34521-34532
    sprite('Action_053_03', 2)	# 34533-34534
    sprite('Action_053_04', 2)	# 34535-34536
    sprite('Action_053_05', 2)	# 34537-34538
    sprite('Action_053_06', 13)	# 34539-34551
    sprite('Action_053_07', 6)	# 34552-34557
    sprite('Action_053_08', 5)	# 34558-34562
    label(181)
    sprite('Action_053_09', 4)	# 34563-34566
    sprite('Action_053_10', 4)	# 34567-34570
    loopRest()
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_053_09', 1)	# 34571-34571
    Unknown21007(24, 40)
    Unknown21011(240)
    label(182)
    sprite('Action_053_09', 4)	# 34572-34575
    sprite('Action_053_10', 4)	# 34576-34579
    loopRest()
    gotoLabel(182)
    label(190)
    sprite('Action_053_00', 2)	# 34580-34581
    Unknown2019(1000)
    sprite('Action_053_01', 4)	# 34582-34585
    sprite('Action_053_02', 12)	# 34586-34597
    sprite('Action_053_03', 2)	# 34598-34599
    sprite('Action_053_04', 2)	# 34600-34601
    SFX_1('uwa700umi')
    sprite('Action_053_05', 2)	# 34602-34603
    sprite('Action_053_06', 13)	# 34604-34616
    sprite('Action_053_07', 6)	# 34617-34622
    sprite('Action_053_08', 5)	# 34623-34627
    label(191)
    sprite('Action_053_09', 4)	# 34628-34631
    sprite('Action_053_10', 4)	# 34632-34635
    loopRest()
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_053_09', 1)	# 34636-34636
    Unknown21007(24, 40)
    Unknown21011(200)
    label(192)
    sprite('Action_053_09', 4)	# 34637-34640
    sprite('Action_053_10', 4)	# 34641-34644
    loopRest()
    gotoLabel(192)
    label(200)
    sprite('Action_000_00', 1)	# 34645-34645	 **attackbox here**
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 7)	# 34646-34652	 **attackbox here**
    sprite('Action_000_01', 5)	# 34653-34657	 **attackbox here**
    sprite('Action_000_02', 12)	# 34658-34669	 **attackbox here**
    sprite('Action_000_03', 14)	# 34670-34683	 **attackbox here**
    sprite('Action_000_04', 30)	# 34684-34713	 **attackbox here**
    sprite('Action_000_05', 9)	# 34714-34722	 **attackbox here**
    sprite('Action_000_06', 6)	# 34723-34728	 **attackbox here**
    sprite('Action_000_07', 8)	# 34729-34736	 **attackbox here**
    sprite('Action_000_08', 14)	# 34737-34750	 **attackbox here**
    sprite('Action_000_09', 17)	# 34751-34767	 **attackbox here**
    sprite('Action_000_10', 17)	# 34768-34784	 **attackbox here**
    sprite('Action_000_11', 12)	# 34785-34796	 **attackbox here**
    gotoLabel(201)
    label(202)
    sprite('Action_053_00', 2)	# 34797-34798
    sprite('Action_053_01', 4)	# 34799-34802
    sprite('Action_053_02', 12)	# 34803-34814
    sprite('Action_053_03', 2)	# 34815-34816
    sprite('Action_053_04', 2)	# 34817-34818
    SFX_1('uwa701pak')
    sprite('Action_053_05', 2)	# 34819-34820
    sprite('Action_053_06', 13)	# 34821-34833
    sprite('Action_053_07', 6)	# 34834-34839
    sprite('Action_053_08', 5)	# 34840-34844
    Unknown23018(1)
    label(203)
    sprite('Action_053_09', 4)	# 34845-34848
    sprite('Action_053_10', 4)	# 34849-34852
    loopRest()
    gotoLabel(203)

@State
def CmnActLose():
    sprite('Action_248_00', 7)	# 1-7
    if random_(2, 0, 50):
        SFX_1('uwa403_0')
    else:
        SFX_1('uwa403_1')
    Unknown23018(1)
    sprite('Action_248_01', 4)	# 8-11	 **attackbox here**
    label(1)
    sprite('Action_248_02', 60)	# 12-71	 **attackbox here**
    sprite('Action_248_03', 5)	# 72-76	 **attackbox here**
    gotoLabel(1)

@State
def EventDefEntryWait():
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_05', 7)	# 50-56
    sprite('hb000_04', 7)	# 57-63
    sprite('hb000_03', 7)	# 64-70
    sprite('hb000_02', 7)	# 71-77
    sprite('hb000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryWaitCameraON():

    def upon_IMMEDIATE():
        Unknown20000(1)
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_05', 7)	# 50-56
    sprite('hb000_04', 7)	# 57-63
    sprite('hb000_03', 7)	# 64-70
    sprite('hb000_02', 7)	# 71-77
    sprite('hb000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def EventYoroke():
    sprite('hb070_03', 32767)	# 1-32767

@State
def EventYorokeDown():
    sprite('hb070_04', 4)	# 1-4
    sprite('hb070_05', 4)	# 5-8
    sprite('hb070_06', 4)	# 9-12
    sprite('hb070_07', 4)	# 13-16
    sprite('hb070_08', 4)	# 17-20
    sprite('hb070_09', 4)	# 21-24
    sprite('hb063_11', 32767)	# 25-32791

@State
def EventDefCrouch():
    label(0)
    sprite('hb010_02', 6)	# 1-6
    sprite('hb010_03', 6)	# 7-12
    sprite('hb010_04', 6)	# 13-18
    sprite('hb010_05', 6)	# 19-24
    sprite('hb010_06', 6)	# 25-30
    sprite('hb010_07', 6)	# 31-36
    sprite('hb010_08', 6)	# 37-42
    sprite('hb010_09', 6)	# 43-48
    loopRest()
    gotoLabel(0)

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

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
    sprite('hb030_00', 7)	# 1-7
    physicsXImpulse(4650)
    label(0)
    sprite('hb030_01', 7)	# 8-14
    sprite('hb030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_03', 7)	# 22-28
    sprite('hb030_04', 7)	# 29-35
    sprite('hb030_05', 7)	# 36-42
    sprite('hb030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_07', 7)	# 50-56
    sprite('hb030_08', 7)	# 57-63
    sprite('hb030_09', 7)	# 64-70
    sprite('hb030_10', 10)	# 71-80
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventDefChouhatsu():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 6)	# 19-24
    sprite('hb300_04', 6)	# 25-30
    sprite('hb300_05', 6)	# 31-36
    sprite('hb300_03', 25)	# 37-61
    sprite('hb300_06', 6)	# 62-67
    sprite('hb300_07', 6)	# 68-73
    sprite('hb300_08', 30)	# 74-103
    sprite('hb300_07', 6)	# 104-109
    sprite('hb300_06', 6)	# 110-115
    sprite('hb300_05', 6)	# 116-121
    sprite('hb300_02', 6)	# 122-127
    sprite('hb300_01', 6)	# 128-133
    sprite('hb300_00', 6)	# 134-139
    enterState('CmnActStand')

@State
def EventDefChouhatsu2():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 32767)	# 19-32785

@State
def EventDefChouhatsu2End():
    sprite('hb300_02', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_00', 6)	# 13-18
    enterState('CmnActStand')

@State
def EventNOVSHB():
    sprite('hb000_00', 8)	# 1-8
    sprite('hb000_01', 8)	# 9-16
    sprite('hb000_02', 8)	# 17-24
    sprite('hb000_03', 8)	# 25-32
    sprite('hb000_04', 8)	# 33-40
    sprite('hb000_05', 8)	# 41-48
    sprite('hb000_06', 8)	# 49-56
    sprite('hb000_05', 8)	# 57-64
    sprite('hb000_04', 8)	# 65-72
    sprite('hb000_03', 8)	# 73-80
    sprite('hb000_02', 8)	# 81-88
    sprite('hb000_01', 8)	# 89-96
    sprite('hb300_00', 8)	# 97-104
    sprite('hb300_01', 8)	# 105-112
    sprite('hb300_02', 8)	# 113-120
    sprite('hb300_03', 8)	# 121-128
    sprite('hb300_03', 280)	# 129-408
    sprite('hb300_05', 8)	# 409-416
    sprite('hb300_02', 8)	# 417-424
    sprite('hb300_01', 8)	# 425-432
    sprite('hb300_00', 8)	# 433-440
    loopRest()
    enterState('CmnActStand')

@State
def EventPause1():
    sprite('hb333_00', 6)	# 1-6
    sprite('hb333_01', 6)	# 7-12
    sprite('hb333_02', 6)	# 13-18
    sprite('hb333_03', 6)	# 19-24
    sprite('hb333_04', 6)	# 25-30
    label(0)
    sprite('hb333_05', 8)	# 31-38
    sprite('hb333_06', 8)	# 39-46
    sprite('hb333_07', 8)	# 47-54
    loopRest()
    gotoLabel(0)

@State
def EventPause1End():
    sprite('hb333_08', 8)	# 1-8
    sprite('hb333_09', 8)	# 9-16
    loopRest()
    enterState('CmnActStand')

@State
def EventStandDLoop():
    sprite('hb203_00', 6)	# 1-6
    sprite('hb203_01', 6)	# 7-12
    label(0)
    sprite('hb203_02', 6)	# 13-18
    sprite('hb203_03', 6)	# 19-24
    sprite('hb203_04', 6)	# 25-30
    sprite('hb203_05', 8)	# 31-38
    loopRest()
    gotoLabel(0)

@State
def EventStandDLoopEnd():
    sprite('hb203_01', 6)	# 1-6
    sprite('hb203_00', 6)	# 7-12
    loopRest()
    enterState('CmnActStand')

@State
def EventMemoLoop():
    sprite('hb610_00', 6)	# 1-6
    sprite('hb610_01', 6)	# 7-12
    sprite('hb610_02', 6)	# 13-18
    sprite('hb610_03', 6)	# 19-24
    sprite('hb610_04', 6)	# 25-30
    sprite('hb610_05', 8)	# 31-38
    sprite('hb610_06', 8)	# 39-46
    sprite('hb610_07', 8)	# 47-54
    label(0)
    sprite('hb610_08', 8)	# 55-62
    sprite('hb610_09', 8)	# 63-70
    loopRest()
    gotoLabel(0)

@State
def EventMemoLoopEnd():
    sprite('hb610_07', 8)	# 1-8
    sprite('hb610_06', 6)	# 9-14
    sprite('hb610_05', 6)	# 15-20
    sprite('hb610_04', 6)	# 21-26
    sprite('hb610_03', 6)	# 27-32
    sprite('hb610_02', 6)	# 33-38
    sprite('hb610_01', 8)	# 39-46
    sprite('hb610_00', 8)	# 47-54
    loopRest()
    enterState('CmnActStand')

@State
def EventMemoLoopCameraON():

    def upon_IMMEDIATE():
        Unknown20000(1)
    sprite('hb610_00', 6)	# 1-6
    sprite('hb610_01', 6)	# 7-12
    sprite('hb610_02', 6)	# 13-18
    sprite('hb610_03', 6)	# 19-24
    sprite('hb610_04', 6)	# 25-30
    sprite('hb610_05', 8)	# 31-38
    sprite('hb610_06', 8)	# 39-46
    sprite('hb610_07', 8)	# 47-54
    label(0)
    sprite('hb610_08', 8)	# 55-62
    sprite('hb610_09', 8)	# 63-70
    loopRest()
    gotoLabel(0)

@State
def EventWin01Wait():
    sprite('hb615_08', 32767)	# 1-32767
    loopRest()

@State
def EventWin01WaitToStand():
    sprite('hb615_08', 6)	# 1-6
    sprite('hb615_07', 6)	# 7-12
    sprite('hb615_06', 6)	# 13-18
    sprite('hb615_05', 6)	# 19-24
    sprite('hb615_04', 6)	# 25-30
    sprite('hb615_03', 6)	# 31-36
    sprite('hb615_02', 6)	# 37-42
    sprite('hb615_01', 6)	# 43-48
    sprite('hb615_00', 6)	# 49-54
    loopRest()
    enterState('CmnActStand')

@State
def EventWin02ToStand():
    sprite('hb603_06', 6)	# 1-6
    sprite('hb603_05', 6)	# 7-12
    sprite('hb603_04', 6)	# 13-18
    sprite('hb603_03', 6)	# 19-24
    sprite('hb603_02', 6)	# 25-30
    sprite('hb603_01', 8)	# 31-38
    sprite('hb603_00', 32767)	# 39-32805
    loopRest()

@State
def EventEntry01ToStand():
    sprite('null', 20)	# 1-20
    teleportRelativeX(-105000)
    Unknown3026(-13421773)
    sprite('hb600_00', 32767)	# 21-32787
    physicsYImpulse(-30000)
    setGravity(1800)
    Unknown3038(0)
    sendToLabelUpon(2, 1)
    GFX_0('hbef_600_feather', 100)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3072('7f000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    SFX_0('000_airdash_1')
    label(1)
    sprite('hb600_01', 6)	# 32788-32793
    Unknown26('hbef_600_feather')
    GFX_0('hbef_600_feather2', 100)
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    Unknown3025(-1, 16)
    sprite('hb600_02', 2)	# 32794-32795
    Unknown3029(0)
    sprite('hb600_02', 2)	# 32796-32797
    sprite('hb600_03', 6)	# 32798-32803
    SFX_0('019_cloth_b')
    sprite('hb600_04', 6)	# 32804-32809
    sprite('hb600_05', 6)	# 32810-32815
    sprite('hb600_06', 6)	# 32816-32821
    sprite('hb600_07', 6)	# 32822-32827
    sprite('hb600_08', 6)	# 32828-32833
    sprite('hb600_09', 6)	# 32834-32839
    sprite('hb600_10', 7)	# 32840-32846
    sprite('hb600_11', 7)	# 32847-32853
    sprite('hb600_12', 7)	# 32854-32860
    sprite('hb600_13', 20)	# 32861-32880
    sprite('hb600_14', 6)	# 32881-32886
    teleportRelativeX(10000)
    sprite('hb600_15', 6)	# 32887-32892
    teleportRelativeX(5000)
    sprite('hb600_16', 6)	# 32893-32898
    teleportRelativeX(45000)
    sprite('hb600_17', 6)	# 32899-32904
    teleportRelativeX(25000)
    sprite('hb000_00', 1)	# 32905-32905
    Unknown21011(100)
    teleportRelativeX(20000)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Event2DLoop():
    sprite('hb234_00', 3)	# 1-3
    sprite('hb234_01', 4)	# 4-7
    SFX_0('019_cloth_a')
    Unknown1084(1)
    physicsYImpulse(15000)
    sprite('hb234_02', 5)	# 8-12
    setGravity(3600)
    sprite('hb234_03', 4)	# 13-16
    sprite('hb234_04', 32767)	# 17-32783
    sendToLabelUpon(2, 0)
    label(0)
    sprite('hb234_05', 3)	# 32784-32786
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    GFX_0('hbef_Drive', 103)
    GFX_0('hbef_2D_feather', 103)
    label(10)
    sprite('hb234_06', 6)	# 32787-32792
    sprite('hb234_07', 6)	# 32793-32798
    sprite('hb234_08', 6)	# 32799-32804
    sprite('hb234_09', 6)	# 32805-32810
    loopRest()
    gotoLabel(10)

@State
def Event2DLoopEnd():
    sprite('hb234_10', 4)	# 1-4
    sprite('hb234_11', 4)	# 5-8
    sprite('hb234_12', 4)	# 9-12
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_NoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def Act2EventWalkFrameIn():
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
    sprite('hb030_00', 7)	# 1-7
    physicsXImpulse(4650)
    label(0)
    sprite('hb030_01', 7)	# 8-14
    sprite('hb030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_03', 7)	# 22-28
    sprite('hb030_04', 7)	# 29-35
    sprite('hb030_05', 7)	# 36-42
    sprite('hb030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_07', 7)	# 50-56
    sprite('hb030_08', 7)	# 57-63
    sprite('hb030_09', 7)	# 64-70
    sprite('hb030_10', 10)	# 71-80
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def Act2Event_EntryA():

    def upon_IMMEDIATE():
        sendToLabelUpon(2, 0)
        Unknown3038(1)
        setGravity(0)
        teleportRelativeX(-105000)
    sprite('null', 2)	# 1-2
    teleportRelativeY(600000)
    sprite('null', 20)	# 3-22
    Unknown3026(-13421773)
    sprite('hb600_00', 32767)	# 23-32789
    physicsYImpulse(-30000)
    setGravity(1800)
    Unknown3038(0)
    GFX_0('hbef_600_feather', 100)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3072('7f000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    SFX_0('000_airdash_1')
    label(0)
    sprite('hb600_01', 6)	# 32790-32795
    Unknown26('hbef_600_feather')
    GFX_0('hbef_600_feather2', 100)
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    Unknown3025(-1, 16)
    sprite('hb600_02', 2)	# 32796-32797
    Unknown3029(0)
    sprite('hb600_02', 2)	# 32798-32799
    sprite('hb600_03', 6)	# 32800-32805
    SFX_0('019_cloth_b')
    sprite('hb600_04', 6)	# 32806-32811
    sprite('hb600_05', 6)	# 32812-32817
    sprite('hb600_06', 6)	# 32818-32823
    sprite('hb600_07', 6)	# 32824-32829
    sprite('hb600_08', 6)	# 32830-32835
    sprite('hb600_09', 6)	# 32836-32841
    sprite('hb600_10', 7)	# 32842-32848
    sprite('hb600_11', 7)	# 32849-32855
    sprite('hb600_12', 7)	# 32856-32862
    sprite('hb600_13', 20)	# 32863-32882
    sprite('hb600_14', 6)	# 32883-32888
    teleportRelativeX(10000)
    sprite('hb600_15', 6)	# 32889-32894
    teleportRelativeX(5000)
    sprite('hb600_16', 6)	# 32895-32900
    teleportRelativeX(45000)
    sprite('hb600_17', 6)	# 32901-32906
    teleportRelativeX(25000)
    sprite('hb000_00', 1)	# 32907-32907
    teleportRelativeX(20000)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_EntryB1():
    sprite('hb603_00', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_EntryB2():
    sprite('hb603_00', 7)	# 1-7
    sprite('hb603_01', 7)	# 8-14
    sprite('hb603_02', 7)	# 15-21
    sprite('hb603_03', 10)	# 22-31
    sprite('hb603_04', 7)	# 32-38
    sprite('hb603_05', 6)	# 39-44
    sprite('hb603_06', 6)	# 45-50
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Reaction():
    sprite('hb001_00', 7)	# 1-7
    sprite('hb001_01', 7)	# 8-14
    sprite('hb001_02', 7)	# 15-21
    sprite('hb001_03', 8)	# 22-29
    sprite('hb001_04', 8)	# 30-37
    sprite('hb001_05', 8)	# 38-45
    sprite('hb001_06', 7)	# 46-52
    sprite('hb001_05', 5)	# 53-57
    sprite('hb001_04', 5)	# 58-62
    sprite('hb001_03', 5)	# 63-67
    sprite('hb001_02', 10)	# 68-77
    sprite('hb001_03', 8)	# 78-85
    sprite('hb001_04', 8)	# 86-93
    sprite('hb001_05', 8)	# 94-101
    sprite('hb001_06', 7)	# 102-108
    sprite('hb001_05', 5)	# 109-113
    sprite('hb001_04', 5)	# 114-118
    sprite('hb001_03', 5)	# 119-123
    sprite('hb001_01', 7)	# 124-130
    sprite('hb001_00', 7)	# 131-137
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Win1():
    sprite('hb611_00', 7)	# 1-7
    sprite('hb611_01', 7)	# 8-14
    label(0)
    sprite('hb611_02', 6)	# 15-20
    sprite('hb611_03', 6)	# 21-26
    sprite('hb611_04', 6)	# 27-32
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Win2():
    sprite('keep', 1)	# 1-1
    sprite('hb611_05', 7)	# 2-8
    sprite('hb611_06', 7)	# 9-15
    sprite('hb611_07', 6)	# 16-21
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb611_08', 6)	# 22-27
    sprite('hb611_09', 6)	# 28-33
    sprite('hb611_07', 6)	# 34-39
    Unknown3038(1)
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('hbef_611_shadow_Event', 100)
    sprite('hb611_08', 6)	# 40-45
    Unknown3004(-10)
    sprite('hb611_09', 6)	# 46-51
    sprite('hb611_07', 6)	# 52-57
    Unknown21011(30)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb611_08', 6)	# 58-63
    sprite('hb611_09', 6)	# 64-69
    Unknown3038(1)
    sprite('hb611_07', 6)	# 70-75
    sprite('hb611_08', 6)	# 76-81
    sprite('hb611_09', 6)	# 82-87
    label(9)
    sprite('hb611_07', 6)	# 88-93
    sprite('hb611_08', 6)	# 94-99
    sprite('hb611_09', 6)	# 100-105
    loopRest()
    gotoLabel(9)

@State
def Act2Event_Chouhatsu():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 32767)	# 19-32785
    loopRest()

@State
def Act2Event_ChouhatsuEnd():
    sprite('keep', 2)	# 1-2
    sprite('hb300_02', 6)	# 3-8
    sprite('hb300_01', 6)	# 9-14
    sprite('hb300_00', 6)	# 15-20
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Down():
    sprite('hb060_14', 32767)	# 1-32767
    loopRest()

@State
def Act2EventYorokeDown():
    sprite('hb070_04', 4)	# 1-4
    sprite('hb070_05', 4)	# 5-8
    sprite('hb070_06', 4)	# 9-12
    sprite('hb070_07', 4)	# 13-16
    sprite('hb070_08', 4)	# 17-20
    sprite('hb070_09', 4)	# 21-24
    GFX_1('ef_grndshock', 104)
    SFX_0('209_down_normal_0')
    sprite('hb063_11', 32767)	# 25-32791

@State
def Act2Event_DownEnd():
    sprite('keep', 2)	# 1-2
    sprite('hb061_00', 4)	# 3-6
    sprite('hb061_01', 4)	# 7-10
    sprite('hb061_02', 4)	# 11-14
    sprite('hb061_03', 4)	# 15-18
    sprite('hb061_04', 4)	# 19-22
    sprite('hb061_05', 4)	# 23-26
    sprite('hb061_06', 3)	# 27-29
    sprite('hb061_07', 3)	# 30-32
    sprite('hb061_08', 3)	# 33-35
    sprite('hb061_09', 3)	# 36-38
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_hbvstb_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
    sprite('hb003_00', 3)	# 1-3
    sprite('hb003_01', 3)	# 4-6
    sprite('hb003_00ex01', 3)	# 7-9
    Unknown2005()
    sprite('hb032_00', 2)	# 10-11
    physicsXImpulse(24000)
    sprite('hb032_01', 2)	# 12-13
    sprite('hb032_02', 4)	# 14-17
    sprite('hb032_03', 4)	# 18-21
    Unknown8006(100, 1, 1)
    sprite('hb032_04', 4)	# 22-25
    sprite('hb032_05', 4)	# 26-29
    sprite('hb032_06', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('hb032_07', 4)	# 34-37
    sprite('hb032_08', 4)	# 38-41
    sprite('hb032_02', 4)	# 42-45
    sprite('hb032_03', 4)	# 46-49
    Unknown8006(100, 1, 1)
    sprite('hb032_04', 4)	# 50-53
    sprite('hb032_05', 4)	# 54-57
    sprite('hb032_06', 4)	# 58-61
    Unknown8006(100, 1, 1)
    sprite('hb032_07', 4)	# 62-65
    sprite('hb032_08', 4)	# 66-69
    sprite('null', 32767)	# 70-32836
    Unknown1084(1)
    loopRest()

@State
def Act2Event_hbvsaz_00():

    def upon_IMMEDIATE():
        Unknown1000(-900000)
        Unknown2034(0)
        sendToLabelUpon(2, 1)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 160000):
                sendToLabel(0)
                clearUponHandler(3)
        elif (SLOT_22 > (-160000)):
            sendToLabel(0)
            clearUponHandler(3)
    sprite('hb032_00', 2)	# 1-2
    physicsXImpulse(24000)
    sprite('hb032_01', 2)	# 3-4
    label(9)
    sprite('hb032_02', 4)	# 5-8
    sprite('hb032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('hb032_04', 4)	# 13-16
    sprite('hb032_05', 4)	# 17-20
    sprite('hb032_06', 4)	# 21-24
    Unknown8006(100, 1, 1)
    sprite('hb032_07', 4)	# 25-28
    sprite('hb032_08', 4)	# 29-32
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('hb032_09', 3)	# 33-35
    physicsXImpulse(0)
    Unknown1045(5000)
    sprite('hb032_10', 3)	# 36-38
    sprite('hb032_11', 3)	# 39-41
    sprite('hb032_12', 3)	# 42-44
    sprite('hb033_00', 2)	# 45-46
    Unknown1084(1)
    sprite('hb033_01', 2)	# 47-48
    physicsXImpulse(-24000)
    physicsYImpulse(6800)
    setGravity(2000)
    Unknown8002()
    sprite('hb033_02', 2)	# 49-50
    sprite('hb033_03', 2)	# 51-52
    sprite('hb033_04', 32767)	# 53-32819
    label(1)
    sprite('hb033_05', 2)	# 32820-32821
    Unknown1084(1)
    Unknown1000(-260000)
    Unknown8000(100, 1, 1)
    sprite('hb033_06', 3)	# 32822-32824
    sprite('hb033_07', 3)	# 32825-32827
    sprite('hb033_08', 3)	# 32828-32830
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_hbvsaz_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('hb090_00', 15)	# 1-15
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('hb090_01', 6)	# 16-21
    sprite('hb090_02', 6)	# 22-27
    sprite('hb090_03', 6)	# 28-33
    sprite('hb090_04', 6)	# 34-39
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_hbvsaz_02():
    sprite('hb070_13', 5)	# 1-5
    GFX_0('Act2Event_Yure', -1)
    sprite('hb070_12', 5)	# 6-10
    sprite('hb070_11', 5)	# 11-15
    sprite('hb070_10', 32767)	# 16-32782
    loopRest()

@State
def Act2Event_hzvshb_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
    sprite('hb032_00', 2)	# 1-2
    physicsXImpulse(18000)
    sprite('hb032_01', 2)	# 3-4
    sprite('hb032_02', 4)	# 5-8
    sprite('hb032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    physicsXImpulse(0)
    Unknown1047(10000)
    sprite('hb032_09', 5)	# 13-17
    sprite('hb032_10', 5)	# 18-22
    sprite('hb032_11', 5)	# 23-27
    sprite('hb032_12', 7)	# 28-34
    Unknown1084(1)
    sprite('hb000_00', 7)	# 35-41
    sprite('hb000_01', 7)	# 42-48
    sprite('hb000_02', 7)	# 49-55
    sprite('hb000_03', 7)	# 56-62
    sprite('hb000_04', 7)	# 63-69
    sprite('hb000_05', 7)	# 70-76
    sprite('hb000_06', 7)	# 77-83
    sprite('hb000_07', 7)	# 84-90
    sprite('hb000_08', 7)	# 91-97
    sprite('hb611_00', 6)	# 98-103
    sprite('hb611_01', 6)	# 104-109
    label(0)
    sprite('hb611_02', 6)	# 110-115
    sprite('hb611_03', 6)	# 116-121
    sprite('hb611_04', 6)	# 122-127
    loopRest()
    gotoLabel(0)

@State
def Act2Event_muvshb_00():

    def upon_IMMEDIATE():
        teleportRelativeY(700000)
        clearUponHandler(2)
        sendToLabelUpon(2, 0)
    sprite('null', 1)	# 1-1
    SFX_3('hbse_02')
    SFX_0('007_swing_knife_0')
    teleportRelativeX(-105000)
    GFX_0('Kunai_Event', -1)
    Unknown21007(1, 32)
    sprite('null', 1)	# 2-2
    GFX_0('Kunai_Event', -1)
    Unknown21007(1, 33)
    sprite('null', 1)	# 3-3
    GFX_0('Kunai_Event', -1)
    Unknown21007(1, 34)
    sprite('null', 60)	# 4-63
    sprite('hb600_00', 32767)	# 64-32830
    Unknown3026(-13421773)
    physicsYImpulse(-30000)
    Unknown1043()
    Unknown3038(0)
    GFX_0('hbef_600_feather', 100)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3072('7f000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    SFX_0('000_airdash_1')
    label(0)
    sprite('hb600_01', 6)	# 32831-32836
    Unknown26('hbef_600_feather')
    GFX_0('hbef_600_feather2', 100)
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    Unknown3025(-1, 16)
    sprite('hb600_02', 2)	# 32837-32838
    Unknown3029(0)
    sprite('hb600_02', 2)	# 32839-32840
    sprite('hb600_03', 6)	# 32841-32846
    SFX_0('019_cloth_b')
    sprite('hb600_04', 6)	# 32847-32852
    sprite('hb600_05', 6)	# 32853-32858
    sprite('hb600_06', 6)	# 32859-32864
    sprite('hb600_07', 6)	# 32865-32870
    sprite('hb600_08', 6)	# 32871-32876
    sprite('hb600_09', 6)	# 32877-32882
    sprite('hb600_10', 7)	# 32883-32889
    sprite('hb600_11', 7)	# 32890-32896
    sprite('hb600_12', 7)	# 32897-32903
    sprite('hb600_13', 20)	# 32904-32923
    sprite('hb600_14', 6)	# 32924-32929
    teleportRelativeX(10000)
    sprite('hb600_15', 6)	# 32930-32935
    teleportRelativeX(5000)
    sprite('hb600_16', 6)	# 32936-32941
    teleportRelativeX(45000)
    sprite('hb600_17', 6)	# 32942-32947
    teleportRelativeX(25000)
    sprite('hb000_00', 1)	# 32948-32948
    teleportRelativeX(20000)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_muvshb_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('hb070_00', 15)	# 1-15
    Unknown4052()
    Unknown4045('65665f6869746d7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_1')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('hb070_01', 3)	# 16-18
    sprite('hb070_02', 4)	# 19-22
    sprite('hb070_03', 32767)	# 23-32789
    loopRest()

@State
def Act2Event_muvshb_02():
    sprite('hb070_04', 5)	# 1-5
    sprite('hb070_05', 5)	# 6-10
    sprite('hb070_06', 5)	# 11-15
    sprite('hb070_07', 5)	# 16-20
    sprite('hb070_08', 5)	# 21-25
    sprite('hb070_09', 5)	# 26-30
    sprite('hb063_11', 32767)	# 31-32797
    SFX_0('209_down_normal_0')
    loopRest()

@State
def Act2Event_hbvsmi_00():
    sprite('keep', 32767)	# 1-32767
    GFX_0('Act2Event_Fade', -1)
    SFX_0('022_magiccircle_c')
    Unknown3004(-4)
    Unknown36(22)
    Unknown3004(-4)
    Unknown35()
    loopRest()

@State
def Act3Event_muvshb_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('hb202_00', 3)	# 1-3
    sprite('hb202_01', 4)	# 4-7
    sprite('hb202_02', 2)	# 8-9
    sprite('hb202_03', 3)	# 10-12
    GFX_0('hbef_202_slash', 100)
    SFX_0('009_swing_rapier_1')
    sprite('hb202_04', 5)	# 13-17
    sprite('hb202_05', 5)	# 18-22
    sprite('hb202_06', 5)	# 23-27
    sprite('hb202_07', 5)	# 28-32
    sprite('hb202_08', 4)	# 33-36
    sprite('hb202_09', 4)	# 37-40
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_muvshb_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb070_00', 19)	# 8-26
    Unknown4052()
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_2')
    ScreenShake(1000, 20000)
    sprite('hb070_00', 4)	# 27-30
    Unknown1047(-11000)
    sprite('hb070_01', 4)	# 31-34
    sprite('hb070_02', 4)	# 35-38
    sprite('hb070_03', 32767)	# 39-32805
    loopRest()

@State
def Act3Event_muvshb_02():
    sprite('hb070_04', 5)	# 1-5
    sprite('hb070_05', 5)	# 6-10
    sprite('hb070_06', 5)	# 11-15
    sprite('hb070_07', 5)	# 16-20
    sprite('hb070_08', 5)	# 21-25
    sprite('hb070_09', 5)	# 26-30
    sprite('hb063_11', 32767)	# 31-32797
    Unknown8000(100, 1, 1)
    SFX_0('209_down_normal_0')

@State
def Act3Event_muvshb_03():
    sprite('hb064_00', 3)	# 1-3
    sprite('hb064_01', 3)	# 4-6
    sprite('hb064_02', 3)	# 7-9
    sprite('hb064_03', 3)	# 10-12
    sprite('hb064_04', 3)	# 13-15
    sprite('hb064_05', 3)	# 16-18
    sprite('hb064_06', 3)	# 19-21
    sprite('hb064_07', 3)	# 22-24
    sprite('hb064_08', 3)	# 25-27
    sprite('hb064_09', 3)	# 28-30
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_00():
    sprite('hb001_00', 7)	# 1-7
    sprite('hb001_01', 7)	# 8-14
    sprite('hb001_02', 7)	# 15-21
    label(0)
    sprite('hb001_03', 8)	# 22-29
    sprite('hb001_04', 8)	# 30-37
    sprite('hb001_05', 8)	# 38-45
    sprite('hb001_06', 7)	# 46-52
    sprite('hb001_05', 5)	# 53-57
    sprite('hb001_04', 5)	# 58-62
    sprite('hb001_03', 5)	# 63-67
    sprite('hb001_02', 20)	# 68-87
    loopRest()
    gotoLabel(0)

@State
def Act3Event_hbvstb_01():
    sprite('hb001_01', 7)	# 1-7
    sprite('hb001_00', 7)	# 8-14
    loopRest()
    enterState('CmnActStand')
endState()

@State
def Act3Event_hbvstb_02():
    sprite('hb615_00', 4)	# 1-4
    sprite('hb615_01', 4)	# 5-8
    sprite('hb615_02', 7)	# 9-15
    SFX_3('hbse_07')
    sprite('hb615_03', 7)	# 16-22
    GFX_0('hbef_615_hibana', 0)
    sprite('hb615_04', 7)	# 23-29
    sprite('hb615_05', 7)	# 30-36
    sprite('hb615_06', 7)	# 37-43
    sprite('hb615_07', 7)	# 44-50
    sprite('hb615_08', 32767)	# 51-32817

@State
def Act3Event_hbvstb_03():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            teleportRelativeX(120000)
    sprite('hb211_19', 4)	# 1-4
    teleportRelativeX(-120000)
    SFX_0('011_spin_1')
    sprite('hb211_20', 4)	# 5-8
    sprite('hb211_21', 4)	# 9-12
    sprite('hb211_22', 4)	# 13-16
    sprite('hb211_23', 5)	# 17-21
    sprite('hb211_24', 5)	# 22-26
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_04():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('hb202_00', 2)	# 1-2
    sprite('hb202_01', 3)	# 3-5
    sprite('hb202_02', 2)	# 6-7
    sprite('hb202_03', 16)	# 8-23
    GFX_0('hbef_202_slash', 100)
    SFX_0('009_swing_rapier_1')
    sprite('hb202_04', 5)	# 24-28
    sprite('hb202_05', 5)	# 29-33
    sprite('hb202_06', 5)	# 34-38
    sprite('hb202_07', 5)	# 39-43
    sprite('hb202_08', 4)	# 44-47
    sprite('hb202_09', 4)	# 48-51
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_05():
    sprite('keep', 2)	# 1-2
    sprite('hb611_01', 7)	# 3-9
    sprite('hb611_00', 7)	# 10-16
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_06():
    sprite('hb611_00', 7)	# 1-7
    sprite('hb611_01', 7)	# 8-14
    sprite('hb611_05', 7)	# 15-21
    sprite('hb611_06', 7)	# 22-28
    sprite('hb611_07', 6)	# 29-34
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb611_08', 6)	# 35-40
    sprite('hb611_09', 6)	# 41-46
    sprite('hb611_07', 6)	# 47-52
    Unknown3038(1)
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('hbef_611_shadow_Event', 100)
    sprite('hb611_08', 6)	# 53-58
    Unknown3004(-10)
    sprite('hb611_09', 6)	# 59-64
    sprite('hb611_07', 6)	# 65-70
    Unknown21011(30)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb611_08', 6)	# 71-76
    sprite('hb611_09', 6)	# 77-82
    Unknown3038(1)
    sprite('hb611_07', 6)	# 83-88
    sprite('hb611_08', 6)	# 89-94
    sprite('hb611_09', 6)	# 95-100
    label(9)
    sprite('hb611_07', 6)	# 101-106
    sprite('hb611_08', 6)	# 107-112
    sprite('hb611_09', 6)	# 113-118
    loopRest()
    gotoLabel(9)

@State
def Act3Event_hbvsno_00():
    sprite('hb203_00', 5)	# 1-5
    sprite('hb203_01', 5)	# 6-10
    sprite('hb203_02', 5)	# 11-15
    label(0)
    sprite('hb203_03', 5)	# 16-20
    sprite('hb203_04', 5)	# 21-25
    sprite('hb203_05', 5)	# 26-30
    loopRest()
    gotoLabel(0)

@State
def Act3Event_hbvsno_01():
    sprite('hb203_01', 5)	# 1-5
    sprite('hb203_00', 5)	# 6-10
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvshz_00():
    sprite('hb333_00', 5)	# 1-5
    sprite('hb333_01', 5)	# 6-10
    sprite('hb333_02', 5)	# 11-15
    sprite('hb333_03', 32767)	# 16-32782

@State
def Act3Event_hbvshz_01():
    sprite('keep', 2)	# 1-2
    sprite('hb333_04', 3)	# 3-5
    Unknown4049(1500)
    Unknown4004('4775617264437275736857696e64000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    Unknown1096(1200)
    Unknown35()
    SFX_0('302_spsys_drivemotion')
    SFX_0('302_spsys_burst')
    ScreenShake(3000, 60000)
    Unknown2037(3)
    label(0)
    sprite('hb333_05', 5)	# 6-10
    Unknown2038(-1)
    sprite('hb333_06', 5)	# 11-15
    sprite('hb333_07', 5)	# 16-20
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('hb333_08', 5)	# 21-25
    sprite('hb333_09', 5)	# 26-30
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_5DLoop():
    sprite('hb203_00', 5)	# 1-5
    sprite('hb203_01', 5)	# 6-10
    sprite('hb203_02', 5)	# 11-15
    label(0)
    sprite('hb203_03', 5)	# 16-20
    sprite('hb203_04', 5)	# 21-25
    sprite('hb203_05', 5)	# 26-30
    loopRest()
    gotoLabel(0)

@State
def Act3Event_5DLoopEnd():
    sprite('hb203_01', 5)	# 1-5
    sprite('hb203_00', 5)	# 6-10
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_kgvshb_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_07', 7)	# 50-56
    sprite('hb000_08', 7)	# 57-63
    sprite('hb000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hb052_03', 17)	# 71-87
    Unknown4049(1500)
    Unknown4045('65665f6869746d6400000000000000000000000000000000000000000000000067000000')
    SFX_0('100_hit_grap_3')
    ScreenShake(1000, 20000)
    sprite('hb052_03', 32767)	# 88-32854
    Unknown1047(-11000)
    loopRest()

@State
def Act3Event_kgvshb_01():
    sprite('hb052_03', 6)	# 1-6
    sprite('hb052_02', 6)	# 7-12
    sprite('hb052_01', 6)	# 13-18
    sprite('hb052_00', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_DownWait():
    sprite('hb060_14', 32767)	# 1-32767

@State
def Act3Event_DownToStand():
    sprite('hb061_00', 4)	# 1-4
    sprite('hb061_01', 4)	# 5-8
    sprite('hb061_02', 4)	# 9-12
    sprite('hb061_03', 4)	# 13-16
    sprite('hb061_04', 4)	# 17-20
    sprite('hb061_05', 4)	# 21-24
    sprite('hb061_06', 3)	# 25-27
    sprite('hb061_07', 3)	# 28-30
    sprite('hb061_08', 3)	# 31-33
    sprite('hb061_09', 3)	# 34-36
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Smile():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 6)	# 19-24
    sprite('hb300_04', 6)	# 25-30
    sprite('hb300_05', 6)	# 31-36
    sprite('hb300_06', 6)	# 37-42
    sprite('hb300_07', 6)	# 43-48
    sprite('hb300_08', 32767)	# 49-32815
    loopRest()

@State
def Act3Event_blvshb_00():
    sprite('keep', 2)	# 1-2
    teleportRelativeX(90000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_blvshb_01():
    sprite('keep', 2)	# 1-2
    sendToLabelUpon(32, 1)
    sprite('hb300_02', 6)	# 3-8
    sprite('hb300_01', 6)	# 9-14
    sprite('hb300_00', 6)	# 15-20
    loopRest()
    label(0)
    sprite('hb000_00', 7)	# 21-27
    sprite('hb000_01', 7)	# 28-34
    sprite('hb000_02', 7)	# 35-41
    sprite('hb000_03', 7)	# 42-48
    sprite('hb000_04', 7)	# 49-55
    sprite('hb000_05', 7)	# 56-62
    sprite('hb000_06', 7)	# 63-69
    sprite('hb000_07', 7)	# 70-76
    sprite('hb000_08', 7)	# 77-83
    sprite('hb000_09', 7)	# 84-90
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hb033_00', 2)	# 91-92
    sprite('hb033_01', 2)	# 93-94
    physicsXImpulse(-12000)
    physicsYImpulse(4800)
    setGravity(2000)
    Unknown8002()
    sendToLabelUpon(2, 2)
    sprite('hb033_02', 2)	# 95-96
    setInvincible(0)
    sprite('hb033_03', 2)	# 97-98
    sprite('hb033_04', 32767)	# 99-32865
    label(2)
    sprite('hb033_05', 2)	# 32866-32867
    clearUponHandler(2)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('hb033_06', 3)	# 32868-32870
    sprite('hb033_07', 3)	# 32871-32873
    sprite('hb033_08', 2)	# 32874-32875
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsHB00():

    def upon_IMMEDIATE():
        Unknown3001(0)
        Unknown1000(-50000)
    sprite('hb603_00', 6)	# 1-6
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb603_00', 6)	# 7-12
    sprite('hb603_00', 6)	# 13-18
    sprite('hb603_00', 6)	# 19-24
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('Act3Event_BNvsHB00shadow', 100)
    sprite('hb603_00', 6)	# 25-30
    Unknown3004(10)
    sprite('hb603_00', 6)	# 31-36
    sprite('hb603_00', 6)	# 37-42
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb603_00', 6)	# 43-48
    Unknown13044(0)
    Unknown3026(0)
    Unknown3025(-1, 10)
    GFX_0('hbef_D_feather', 100)
    sprite('hb603_00', 32767)	# 49-32815
    loopRest()

@State
def Act3Event_BNvsHB01():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
    sprite('hb603_00', 32767)	# 1-32767
    loopRest()
    label(0)
    sprite('hb603_00', 6)	# 32768-32773
    SFX_3('hbse_08')
    Unknown3004(-10)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb603_00', 6)	# 32774-32779
    sprite('hb603_00', 6)	# 32780-32785
    sprite('hb603_00', 6)	# 32786-32791
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb603_00', 6)	# 32792-32797
    sprite('hb603_00', 6)	# 32798-32803
    sprite('hb603_00', 6)	# 32804-32809
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb603_00', 6)	# 32810-32815
    Unknown13044(0)
    sprite('null', 32767)	# 32816-65582
    Unknown3038(1)
    Unknown1000(-260000)
    loopRest()

@State
def Act3Event_2DLoopEnd():
    sprite('hb234_10', 6)	# 1-6
    sprite('hb234_11', 6)	# 7-12
    sprite('hb234_12', 6)	# 13-18
    sprite('hb010_01', 4)	# 19-22
    sprite('hb010_00', 4)	# 23-26
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsHB02():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        Unknown1000(-160000)
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_05', 7)	# 50-56
    sprite('hb000_04', 7)	# 57-63
    sprite('hb000_03', 7)	# 64-70
    sprite('hb000_02', 7)	# 71-77
    sprite('hb000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hb090_00', 15)	# 85-99
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('104_guard_grap_2')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('hb090_01', 6)	# 100-105
    sprite('hb090_02', 6)	# 106-111
    sprite('hb090_03', 6)	# 112-117
    sprite('hb090_04', 6)	# 118-123
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsHB03():
    sprite('hb611_00', 7)	# 1-7
    Unknown2004(1, 0)
    sprite('hb611_01', 7)	# 8-14
    sprite('hb611_02', 6)	# 15-20
    sprite('hb611_03', 6)	# 21-26
    sprite('hb611_04', 6)	# 27-32
    sprite('hb611_02', 6)	# 33-38
    sprite('hb611_03', 6)	# 39-44
    sprite('hb611_04', 6)	# 45-50
    sprite('hb611_02', 6)	# 51-56
    sprite('hb611_03', 6)	# 57-62
    sprite('hb611_04', 6)	# 63-68
    sprite('hb611_05', 7)	# 69-75
    sprite('hb611_06', 7)	# 76-82
    sprite('hb611_07', 6)	# 83-88
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb611_08', 6)	# 89-94
    sprite('hb611_09', 6)	# 95-100
    sprite('hb611_07', 6)	# 101-106
    Unknown3038(1)
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('hbef_611_shadow', 100)
    sprite('hb611_08', 6)	# 107-112
    Unknown3004(-10)
    sprite('hb611_09', 6)	# 113-118
    sprite('hb611_07', 6)	# 119-124
    Unknown21011(30)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb611_08', 6)	# 125-130
    sprite('hb611_09', 6)	# 131-136
    Unknown3038(1)
    sprite('hb611_07', 6)	# 137-142
    sprite('hb611_08', 6)	# 143-148
    sprite('hb611_09', 6)	# 149-154
    label(2)
    sprite('hb611_07', 6)	# 155-160
    sprite('hb611_08', 6)	# 161-166
    sprite('hb611_09', 6)	# 167-172
    loopRest()
    gotoLabel(2)

@State
def Act3Event_tbvshb_01():

    def upon_IMMEDIATE():
        Unknown1000(-60000)
        sendToLabelUpon(32, 1)
    sprite('hb312_02', 32767)	# 1-32767
    label(1)
    sprite('hb090_00', 20)	# 32768-32787
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    Unknown1047(-20000)
    ScreenShake(5000, 20000)
    sprite('hb090_01', 6)	# 32788-32793
    sprite('hb090_02', 6)	# 32794-32799
    sprite('hb090_03', 6)	# 32800-32805
    sprite('hb090_04', 6)	# 32806-32811
    loopRest()
    enterState('CmnActStand')