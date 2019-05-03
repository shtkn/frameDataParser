@Subroutine
def PreInit():
    Unknown12019('756c6900000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFAccel(1000)
    DashFMaxVelocity(32000)
    Unknown12038(23000)
    Unknown12034(33)
    Unknown12036(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
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
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(180000, 300000, -200000, 150000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 430000, -200000, 230000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 800000, -200000, 230000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 180000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk4A_2nd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(4000)
    Unknown14015(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk4A_3rd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(4000)
    Unknown14015(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk4A_4th', 0x6)
    Unknown14013('AN_NmlAtk5A_4th')
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(4000)
    Unknown14015(0, 800000, -200000, 230000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 150000, -100000, 100000, 1200, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown15013(3000)
    Unknown14015(0, 150000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(2000)
    Unknown15006(3000)
    Unknown14015(300000, 500000, 100000, 400000, 1200, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 320000, -100000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(4000)
    Unknown14015(0, 450000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(4000)
    Unknown14015(0, 420000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -200000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(200000, 430000, -100000, 50000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk3C', 0x29)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(-100000, 250000, -300000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-100000, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 350000, -500000, 0, 800, 40)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('ShotDashCancel', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Move_EndRegister()
    Move_Register('Shot_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(1)
    Unknown14015(300000, 700000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('Shot_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown14015(400000, 800000, -200000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('Assault_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15012(1000)
    Unknown14015(0, 300000, -200000, 100000, 10, 0)
    Move_EndRegister()
    Move_Register('Assault_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown14015(0, 600000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AirShot_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(1)
    Unknown14015(300000, 700000, -100000, -500000, 150, 0)
    Move_EndRegister()
    Move_Register('AirShot_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(400000, 800000, 100000, -200000, 150, 0)
    Move_EndRegister()
    Move_Register('Shot_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(1)
    Unknown14015(0, 800000, -200000, 150000, 100, 20)
    Move_EndRegister()
    Move_Register('Assault_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15008()
    Unknown14015(0, 600000, -200000, 200000, 100, 20)
    Move_EndRegister()
    Move_Register('AirShot_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15021(1)
    Unknown14015(300000, 700000, -100000, -500000, 100, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 300000, -100000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 300000, -100000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateRush', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(6000)
    Unknown14015(150000, 500000, -200000, 150000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateRushOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(6000)
    Unknown14015(150000, 500000, -200000, 150000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateRanbu', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(6000)
    Unknown14015(0, 300000, -200000, 300000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateRanbuOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(6000)
    Unknown14015(0, 300000, -200000, 300000, 50, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(8000)
    Unknown14015(0, 450000, -200000, 150000, 250, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk4A', 'AN_NmlAtk4A_2nd', 10000000)
    Unknown15024('AN_NmlAtk4A_2nd', 'AN_NmlAtk4A_3rd', 10000000)
    Unknown15024('AN_NmlAtk4A_3rd', 'AN_NmlAtk4A_4th', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'AN_NmlAtk5B_3rd', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2C', 'Assault_B', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown14048('AntiAir', 0x4, 0xed)
    Unknown14048('Assault_C', 0x4, 0x79)
    Unknown14048('UltimateAssault2', 0x4, 0x5f)
    Unknown14048('UltimateAssault2_OD', 0x4, 0x5f)
    Unknown14048('BunshinAssault_A', 0x4, 0x45)
    Unknown14048('AirAssault', 0x4, 0xed)
    Unknown14049('NmlAtk5A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk5B', 'NmlAtk2C', 12, 0)
    Unknown14049('NmlAtk5D', 'BunshinAssault_A', 0, 0)
    Unknown14049('NmlAtk5D', 'BunshinAssault_B', 1, 600000)
    Unknown14049('NmlAtk5D', 'UltimateAssault', 6, 0)
    Unknown14049('NmlAtk5D', 'UltimateAssault_OD', 6, 0)
    Unknown14049('NmlAtk2A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk2C', 'FHighJump', 12, 0)
    Unknown14049('NmlAtk2C', 'NmlAtk5D', 13, 0)
    Unknown14049('NmlAtk2D', 'BunshinAssault_A', 0, 0)
    Unknown14049('NmlAtk2D', 'BunshinAssault_B', 1, 600000)
    Unknown14049('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    Unknown14049('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    Unknown14049('NmlAtkAIR5C', 'AirAssault', 3, 0)
    Unknown14049('NmlAtkAIR5C', 'FJump', 12, 0)
    Unknown14049('NmlAtkAIR6D', 'AirAssault', 3, 0)
    Unknown12018(0, 'Action_330_01')
    Unknown12018(1, 'Action_330_04')
    Unknown12018(2, 'Action_330_05')
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
    Unknown12018(14, 'Action_351_00')
    Unknown12018(15, 'Action_290_00')
    Unknown12018(16, 'Action_300_00')
    Unknown12018(17, 'Action_304_02')
    Unknown12018(18, 'Action_305_03')
    Unknown12018(19, 'Action_000_00')
    Unknown12018(20, 'Action_000_00')
    Unknown12018(25, 'Action_326_00')
    Unknown12018(26, 'Action_326_02')
    Unknown12018(27, 'Action_326_03')
    Unknown12018(28, 'Action_351_05')
    Unknown12018(29, 'Action_292_00')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'uli000')
    Unknown7010(1, 'uli001')
    Unknown7010(2, 'uli002')
    Unknown7010(3, 'uli003')
    Unknown7010(4, 'uli004')
    Unknown7010(5, 'uli005')
    Unknown7010(6, 'uli006')
    Unknown7010(7, 'uli007')
    Unknown7010(8, 'uli008')
    Unknown7010(9, 'uli009')
    Unknown7010(10, 'uli010')
    Unknown7010(11, 'uli011')
    Unknown7010(12, 'uli012')
    Unknown7010(13, 'uli013')
    Unknown7010(14, 'uli014')
    Unknown7010(15, 'uli015')
    Unknown7010(16, 'uli016')
    Unknown7010(17, 'uli017')
    Unknown7010(18, 'uli018')
    Unknown7010(19, 'uli019')
    Unknown7010(20, 'uli020')
    Unknown7010(21, 'uli021')
    Unknown7010(22, 'uli022')
    Unknown7010(23, 'uli023')
    Unknown7010(24, 'uli024')
    Unknown7010(25, 'uli025')
    Unknown7010(26, 'uli026')
    Unknown7010(27, 'uli027')
    Unknown7010(28, 'uli028')
    Unknown7010(29, 'uli029')
    Unknown7010(30, 'uli030')
    Unknown7010(31, 'uli031')
    Unknown7010(32, 'uli032')
    Unknown7010(33, 'uli033')
    Unknown7010(34, 'uli034')
    Unknown7010(35, 'uli035')
    Unknown7010(36, 'uli036')
    Unknown7010(37, 'uli037')
    Unknown7010(38, 'uli038')
    Unknown7010(39, 'uli039')
    Unknown7010(40, 'Hyd500')
    Unknown7010(41, 'uli041')
    Unknown7010(42, 'uli042')
    Unknown7010(43, 'uli043')
    Unknown7010(44, 'uli044')
    Unknown7010(45, 'uli045')
    Unknown7010(46, 'uli046')
    Unknown7010(47, 'uli047')
    Unknown7010(48, 'uli048')
    Unknown7010(49, 'uli049')
    Unknown7010(50, 'uli050')
    Unknown7010(51, 'uli051')
    Unknown7010(52, 'uli052')
    Unknown7010(53, 'uli053')
    Unknown7010(54, 'uli100_0')
    Unknown7010(55, 'uli100_1')
    Unknown7010(56, 'uli100_2')
    Unknown7010(63, 'uli101_0')
    Unknown7010(64, 'uli101_1')
    Unknown7010(65, 'uli101_2')
    Unknown7010(57, 'uli102_0')
    Unknown7010(58, 'uli102_1')
    Unknown7010(59, 'uli102_2')
    Unknown7010(66, 'uli103_0')
    Unknown7010(67, 'uli103_1')
    Unknown7010(68, 'uli103_2')
    Unknown7010(60, 'uli104_0')
    Unknown7010(61, 'uli104_1')
    Unknown7010(62, 'uli104_2')
    Unknown7010(69, 'uli105_0')
    Unknown7010(70, 'uli105_1')
    Unknown7010(71, 'uli105_2')
    Unknown7010(72, 'uli150')
    Unknown7010(73, 'uli151')
    Unknown7010(74, 'uli152')
    Unknown7010(85, 'uli153')
    Unknown7010(88, 'uli155')
    Unknown7010(94, 'uli400_0')
    Unknown7010(95, 'uli401_0')
    Unknown7010(96, 'uli161_0')
    Unknown7010(97, 'uli161_1')
    Unknown7010(98, 'uli163_0')
    Unknown7010(99, 'uli163_1')
    Unknown7010(100, 'uli164_0')
    Unknown7010(101, 'uli164_1')
    Unknown7010(102, 'uli166_0')
    Unknown7010(103, 'uli166_1')
    Unknown7010(92, 'uli162_0')
    Unknown7010(93, 'uli162_1')
    Unknown7010(90, 'uli167_0')
    Unknown7010(91, 'uli167_1')
    Unknown7010(105, 'uli165_0')
    Unknown7010(106, 'uli165_1')
    Unknown7010(107, 'uli168_0')
    Unknown7010(108, 'uli168_1')
    Unknown7010(110, 'uli169_0')
    Unknown7010(111, 'uli169_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d617465527573680000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d617465527573684f44000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746552616e627500000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746552616e62754f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    GFX_0('Geboku', -1)
    Unknown38(11, 1)

@Subroutine
def OnPreDraw():
    Unknown23030('554c495f4c6967687400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if Unknown23145('CmnActOverDriveEnd'):
        SLOT_47 = 1

@Subroutine
def OnActionBegin():
    if Unknown46(11):
        if Unknown23148('CmnActTagBattleWait'):
            Unknown23029(11, 9901, 0)
        else:
            Unknown23029(11, 9900, 0)

@Subroutine
def ChainRoot():
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk4A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')
    HitJumpCancel(1)

@State
def CmnActStand():
    sprite('Action_000_00', 1)	# 1-1	 **attackbox here**
    label(0)
    sprite('Action_000_00', 7)	# 2-8	 **attackbox here**
    sprite('Action_000_01', 7)	# 9-15	 **attackbox here**
    sprite('Action_000_02', 6)	# 16-21	 **attackbox here**
    sprite('Action_000_03', 6)	# 22-27	 **attackbox here**
    sprite('Action_000_04', 8)	# 28-35	 **attackbox here**
    sprite('Action_000_05', 5)	# 36-40	 **attackbox here**
    sprite('Action_000_06', 5)	# 41-45	 **attackbox here**
    sprite('Action_000_07', 5)	# 46-50	 **attackbox here**
    sprite('Action_000_08', 6)	# 51-56	 **attackbox here**
    sprite('Action_000_09', 5)	# 57-61	 **attackbox here**
    sprite('Action_000_10', 6)	# 62-67	 **attackbox here**
    sprite('Action_000_11', 8)	# 68-75	 **attackbox here**
    sprite('Action_000_12', 5)	# 76-80	 **attackbox here**
    sprite('Action_000_13', 5)	# 81-85	 **attackbox here**
    sprite('Action_000_14', 6)	# 86-91	 **attackbox here**
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
    sprite('Action_000_15', 7)	# 92-98	 **attackbox here**
    SLOT_88 = 960
    sprite('Action_000_16', 4)	# 99-102	 **attackbox here**
    SFX_1('uli000')
    sprite('Action_000_17', 7)	# 103-109	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('Action_000_18', 5)	# 110-114	 **attackbox here**
    sprite('Action_000_19', 8)	# 115-122	 **attackbox here**
    sprite('Action_000_20', 10)	# 123-132	 **attackbox here**
    sprite('Action_000_21', 5)	# 133-137	 **attackbox here**
    sprite('Action_000_22', 7)	# 138-144	 **attackbox here**
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('Action_000_23', 3)	# 145-147	 **attackbox here**
    sprite('Action_000_24', 20)	# 148-167	 **attackbox here**
    sprite('Action_000_25', 240)	# 168-407	 **attackbox here**
    sprite('Action_000_26', 5)	# 408-412	 **attackbox here**
    sprite('Action_000_27', 8)	# 413-420	 **attackbox here**
    sprite('Action_000_28', 6)	# 421-426	 **attackbox here**
    sprite('Action_000_29', 4)	# 427-430	 **attackbox here**
    sprite('Action_000_30', 4)	# 431-434	 **attackbox here**
    SFX_0('008_swing_pole_0')
    sprite('Action_000_31', 6)	# 435-440	 **attackbox here**
    sprite('Action_000_32', 7)	# 441-447
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 2)	# 1-2
    sprite('Action_015_01', 2)	# 3-4
    sprite('Action_015_02', 2)	# 5-6

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 3)	# 1-3
    sprite('Action_012_01', 3)	# 4-6
    sprite('Action_012_02', 2)	# 7-8

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 15)	# 1-15
    sprite('Action_013_01', 7)	# 16-22
    sprite('Action_013_02', 6)	# 23-28
    sprite('Action_013_03', 6)	# 29-34
    sprite('Action_013_04', 7)	# 35-41
    sprite('Action_013_05', 7)	# 42-48
    sprite('Action_013_06', 5)	# 49-53
    sprite('Action_013_07', 5)	# 54-58
    sprite('Action_013_08', 5)	# 59-63
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 2)	# 1-2
    sprite('Action_016_01', 2)	# 3-4
    sprite('Action_016_02', 2)	# 5-6

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 3)	# 1-3
    sprite('Action_014_01', 6)	# 4-9
    sprite('Action_014_02', 4)	# 10-13

@State
def CmnActJumpPre():
    sprite('Action_036_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('Action_036_01', 4)	# 1-4
    sprite('Action_035_02', 3)	# 5-7
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('Action_035_03', 3)	# 1-3
    sprite('Action_035_04', 6)	# 4-9
    sprite('Action_035_05', 6)	# 10-15
    sprite('Action_035_06', 6)	# 16-21

@State
def CmnActJumpDown():
    label(0)
    sprite('Action_022_00', 3)	# 1-3
    sprite('Action_022_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('Action_023_00', 2)	# 1-2
    sprite('Action_023_01', 1)	# 3-3
    sprite('Action_023_02', 2)	# 4-5
    sprite('Action_023_03', 3)	# 6-8

@State
def CmnActLandingStiffLoop():
    sprite('Action_023_00', 2)	# 1-2
    sprite('Action_023_01', 2)	# 3-4
    sprite('Action_023_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('Action_023_02', 3)	# 1-3
    sprite('Action_023_03', 3)	# 4-6

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 5)	# 1-5
    sprite('Action_010_01', 5)	# 6-10
    sprite('Action_010_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_03', 5)	# 16-20
    sprite('Action_010_04', 5)	# 21-25
    sprite('Action_010_05', 5)	# 26-30
    sprite('Action_010_06', 5)	# 31-35
    sprite('Action_010_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_08', 5)	# 41-45
    sprite('Action_010_09', 5)	# 46-50
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('Action_011_00', 2)	# 1-2
    sprite('Action_011_01', 2)	# 3-4
    label(0)
    sprite('Action_011_02', 4)	# 5-8
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_03', 4)	# 9-12
    sprite('Action_011_04', 4)	# 13-16
    sprite('Action_011_05', 4)	# 17-20
    sprite('Action_011_06', 4)	# 21-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_07', 4)	# 25-28
    sprite('Action_011_08', 4)	# 29-32
    sprite('Action_011_09', 4)	# 33-36
    sprite('Action_011_10', 4)	# 37-40
    sprite('Action_011_11', 4)	# 41-44
    sprite('Action_011_12', 4)	# 45-48
    sprite('Action_011_13', 4)	# 49-52
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_045_13', 4)	# 1-4
    sprite('Action_045_00', 3)	# 5-7
    sprite('Action_045_01', 3)	# 8-10
    sprite('Action_045_02', 3)	# 11-13
    label(0)
    sprite('Action_045_03', 3)	# 14-16
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 17-19
    sprite('Action_045_05', 3)	# 20-22
    sprite('Action_045_06', 3)	# 23-25
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 26-28
    sprite('Action_045_08', 3)	# 29-31
    sprite('Action_045_09', 3)	# 32-34
    sprite('Action_045_02', 3)	# 35-37
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_11', 2)	# 1-2
    sprite('Action_045_12', 3)	# 3-5
    sprite('Action_045_13', 4)	# 6-9

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

        def upon_3():
            Unknown1019(90)
    sprite('Action_046_00', 1)	# 1-1
    sprite('Action_046_01', 2)	# 2-3
    physicsXImpulse(-40000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('Action_046_02', 2)	# 4-5
    sprite('Action_046_02', 1)	# 6-6
    sprite('Action_046_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('Action_046_03', 3)	# 10-12
    sprite('Action_046_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_05', 3)	# 16-18
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    clearUponHandler(3)
    sprite('Action_046_06', 3)	# 19-21

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        pass
    sprite('Action_068_01', 3)	# 1-3
    sprite('Action_068_02', 3)	# 4-6
    sprite('Action_068_03', 3)	# 7-9
    sprite('Action_068_04', 3)	# 10-12
    sprite('Action_068_05', 3)	# 13-15
    sprite('Action_068_06', 3)	# 16-18
    sprite('Action_068_07', 3)	# 19-21
    sprite('Action_068_08', 3)	# 22-24
    loopRest()
    enterState('AirFDashRigor')

@State
def AirFDashRigor():

    def upon_IMMEDIATE():
        Unknown13014(1)
        Unknown13015(1)
        Unknown13031(1)
        Unknown13019(1)
        Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_068_09', 3)	# 1-3
    sprite('Action_068_10', 3)	# 4-6
    label(0)
    sprite('Action_068_11', 3)	# 7-9
    sprite('Action_068_12', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('Action_046_03', 4)	# 1-4
    physicsYImpulse(12000)
    sprite('Action_046_04', 4)	# 5-8
    label(0)
    sprite('Action_046_03', 4)	# 9-12
    sprite('Action_046_04', 4)	# 13-16
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
    sprite('Action_330_04', 3)	# 1-3
    sprite('Action_330_05', 3)	# 4-6

@State
def CmnActBDownDown():
    sprite('Action_330_06', 3)	# 1-3
    sprite('Action_330_07', 3)	# 4-6
    label(0)
    sprite('Action_330_08', 4)	# 7-10
    sprite('Action_330_09', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('Action_351_00', 2)	# 1-2
    sprite('Action_331_01', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('Action_350_01', 3)	# 1-3
    sprite('Action_350_02', 3)	# 4-6
    sprite('Action_350_03', 3)	# 7-9
    sprite('Action_350_04', 3)	# 10-12
    sprite('Action_350_05', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('Action_350_06', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('Action_293_11', 4)	# 1-4
    sprite('Action_293_12', 4)	# 5-8
    sprite('Action_293_13', 3)	# 9-11
    sprite('Action_293_14', 3)	# 12-14
    sprite('Action_293_15', 4)	# 15-18
    sprite('Action_293_16', 4)	# 19-22
    sprite('Action_293_17', 4)	# 23-26

@State
def CmnActFDownUpper():
    sprite('Action_326_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('Action_326_02', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('Action_326_03', 4)	# 1-4
    sprite('Action_326_04', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('Action_354_00', 3)	# 1-3

@State
def CmnActFDownBound():
    sprite('Action_354_01', 4)	# 1-4
    sprite('Action_354_02', 4)	# 5-8
    sprite('Action_354_03', 4)	# 9-12

@State
def CmnActFDownLoop():
    sprite('Action_292_00', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('Action_294_11', 3)	# 1-3
    sprite('Action_294_12', 3)	# 4-6
    sprite('Action_294_13', 3)	# 7-9
    sprite('Action_294_14', 3)	# 10-12
    sprite('Action_294_15', 3)	# 13-15
    sprite('Action_294_16', 3)	# 16-18
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
    sprite('Action_330_03', 2)	# 1-2
    sprite('Action_330_04', 2)	# 3-4
    sprite('Action_330_05', 2)	# 5-6

@State
def CmnActVDownDown():
    sprite('Action_330_06', 3)	# 1-3
    sprite('Action_330_06', 3)	# 4-6
    label(0)
    sprite('Action_330_08', 4)	# 7-10
    sprite('Action_330_09', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('Action_351_00', 3)	# 1-3
    sprite('Action_351_01', 3)	# 4-6

@State
def CmnActBlowoff():
    sprite('Action_331_00', 2)	# 1-2
    label(0)
    sprite('Action_331_02', 3)	# 3-5
    sprite('Action_331_03', 3)	# 6-8
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
    label(0)
    sprite('Action_301_00', 2)	# 1-2
    sprite('Action_301_00', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('Action_301_00', 1)	# 1-1

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
    sprite('Action_327_02', 5)	# 1-5
    sprite('Action_327_03', 5)	# 6-10
    sprite('Action_327_04', 4)	# 11-14
    sprite('Action_328_00', 4)	# 15-18
    sprite('Action_328_01', 4)	# 19-22

@State
def CmnActUkemiStagger():
    sprite('Action_327_00', 8)	# 1-8

@State
def CmnActUkemiAirF():
    sprite('Action_032_00', 2)	# 1-2
    sprite('Action_032_01', 2)	# 3-4
    sprite('Action_032_02', 2)	# 5-6
    sprite('Action_032_03', 1)	# 7-7
    sprite('Action_032_04', 1)	# 8-8
    sprite('Action_032_05', 1)	# 9-9

@State
def CmnActUkemiAirB():
    sprite('Action_032_00', 4)	# 1-4
    sprite('Action_032_01', 4)	# 5-8
    sprite('Action_032_02', 4)	# 9-12
    sprite('Action_032_03', 4)	# 13-16
    sprite('Action_032_04', 4)	# 17-20
    sprite('Action_032_05', 3)	# 21-23

@State
def CmnActUkemiAirN():
    sprite('Action_032_00', 4)	# 1-4
    sprite('Action_032_01', 4)	# 5-8
    sprite('Action_032_02', 4)	# 9-12
    sprite('Action_032_03', 4)	# 13-16
    sprite('Action_032_04', 4)	# 17-20
    sprite('Action_032_05', 3)	# 21-23
    sprite('Action_032_06', 3)	# 24-26
    sprite('Action_032_07', 3)	# 27-29

@State
def CmnActUkemiLandF():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14
    sprite('Action_041_07', 2)	# 15-16

@State
def CmnActUkemiLandB():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14
    sprite('Action_041_07', 2)	# 15-16

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14
    sprite('Action_041_07', 2)	# 15-16

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_08', 5)	# 1-5
    sprite('Action_041_09', 5)	# 6-10
    sprite('Action_041_10', 5)	# 11-15

@State
def CmnActMidGuardPre():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

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
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActMidHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('Action_017_00', 3)	# 1-3

@State
def CmnActHighGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('Action_018_00', 3)	# 1-3
    sprite('Action_018_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('Action_018_02', 3)	# 1-3
    sprite('Action_018_03', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('Action_018_01', 3)	# 1-3
    sprite('Action_018_02', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('Action_019_00', 3)	# 1-3
    sprite('Action_019_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('Action_019_02', 3)	# 1-3
    sprite('Action_019_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('Action_019_02', 3)	# 1-3
    sprite('Action_019_03', 3)	# 4-6

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
    sprite('Action_017_05', 6)	# 6-11
    sprite('Action_017_06', 6)	# 12-17

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
    sprite('Action_036_01', 9)	# 1-9

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_003_02', 1)	# 1-1
    sprite('Action_003_03', 1)	# 2-2
    sprite('Action_003_04', 2)	# 3-4	 **attackbox here**
    GFX_0('EffNmlAtk5CBlade', 100)
    sprite('Action_003_05', 4)	# 5-8	 **attackbox here**
    sprite('Action_003_06', 7)	# 9-15
    sprite('Action_003_07', 3)	# 16-18
    sprite('Action_003_08', 3)	# 19-21
    sprite('Action_003_09', 3)	# 22-24
    sprite('Action_003_10', 2)	# 25-26

@State
def CmnActAirLockWait():
    sprite('Action_019_02', 1)	# 1-1
    sprite('Action_019_01', 3)	# 2-4
    sprite('Action_019_00', 3)	# 5-7

@State
def CmnActLandSpin():
    sprite('hb071_00', 4)	# 1-4
    sprite('hb071_01', 4)	# 5-8
    label(0)
    sprite('hb071_02', 2)	# 9-10
    sprite('hb071_03', 2)	# 11-12
    sprite('hb071_04', 2)	# 13-14
    sprite('hb071_05', 2)	# 15-16
    sprite('hb071_06', 2)	# 17-18
    sprite('hb071_07', 2)	# 19-20
    sprite('hb071_08', 2)	# 21-22
    sprite('hb071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('hb071_10', 6)	# 1-6
    sprite('hb071_11', 5)	# 7-11
    sprite('hb071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6
    sprite('Action_333_03', 2)	# 7-8
    sprite('Action_333_04', 2)	# 9-10
    sprite('Action_333_05', 2)	# 11-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6
    sprite('Action_333_03', 2)	# 7-8
    sprite('Action_333_04', 2)	# 9-10
    sprite('Action_333_05', 2)	# 11-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('Action_351_00', 1)	# 1-1
    label(0)
    sprite('Action_351_01', 3)	# 2-4
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('Action_351_02', 3)	# 1-3
    sprite('Action_351_03', 2)	# 4-5
    sprite('Action_351_04', 2)	# 6-7
    sprite('Action_351_05', 2)	# 8-9

@State
def CmnActAomukeSlideKeep():
    sprite('Action_351_04', 1)	# 1-1
    label(0)
    sprite('Action_351_04', 3)	# 2-4
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('Action_351_02', 3)	# 1-3
    sprite('Action_351_03', 2)	# 4-5
    sprite('Action_351_04', 2)	# 6-7
    sprite('Action_351_05', 2)	# 8-9

@State
def CmnActBurstBegin():
    sprite('Action_262_00', 4)	# 1-4
    label(0)
    sprite('Action_262_01', 5)	# 5-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('Action_262_05', 3)	# 1-3
    sprite('Action_262_06', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    label(0)
    sprite('Action_262_07', 4)	# 1-4
    sprite('Action_262_08', 4)	# 5-8
    loopRest()
    gotoLabel(0)

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
    sprite('Action_262_05', 6)	# 1-6
    sprite('Action_262_06', 6)	# 7-12

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
    sprite('Action_262_07', 6)	# 1-6
    sprite('Action_262_08', 6)	# 7-12
    label(0)
    sprite('Action_022_00', 3)	# 13-15
    sprite('Action_022_01', 3)	# 16-18
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
    sprite('Action_262_05', 6)	# 1-6
    sprite('Action_262_06', 6)	# 7-12

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
    sprite('Action_262_07', 6)	# 1-6
    sprite('Action_262_08', 6)	# 7-12
    label(0)
    sprite('Action_022_00', 3)	# 13-15
    sprite('Action_022_01', 3)	# 16-18
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
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
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
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('Action_262_07', 3)	# 1-3
    sprite('Action_262_08', 3)	# 4-6
    label(0)
    sprite('Action_022_00', 3)	# 7-9
    sprite('Action_022_01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_002_00', 3)	# 1-3
    sprite('Action_002_01', 3)	# 4-6
    sprite('Action_002_02', 1)	# 7-7
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    sprite('Action_002_03', 4)	# 8-11	 **attackbox here**
    sprite('Action_002_04', 4)	# 12-15
    Recovery()
    Unknown2063()
    sprite('Action_002_05', 4)	# 16-19
    sprite('Action_002_06', 3)	# 20-22
    sprite('Action_002_07', 3)	# 23-25

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1300)
        AirPushbackY(0)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_145_00', 2)	# 1-2
    sprite('Action_145_01', 4)	# 3-6
    Unknown7009(1)
    SFX_0('010_swing_sword_1')
    sprite('Action_145_02', 2)	# 7-8	 **attackbox here**
    GFX_0('Lin_082', 100)
    sprite('Action_145_03', 3)	# 9-11
    Recovery()
    Unknown2063()
    sprite('Action_145_04', 6)	# 12-17
    sprite('Action_145_05', 5)	# 18-22
    sprite('Action_145_06', 4)	# 23-26

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(950)
        Unknown11092(1)
        Hitstop(7)
        AirPushbackY(20000)
        Unknown9016(1)
        callSubroutine('ChainRoot')
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 3)	# 3-5
    sprite('Action_003_02', 5)	# 6-10
    sprite('Action_003_03', 1)	# 11-11
    Unknown7009(2)
    SFX_0('010_swing_sword_2')
    sprite('Action_003_04', 2)	# 12-13	 **attackbox here**
    GFX_0('EffNmlAtk5CBlade', 100)
    sprite('Action_003_05', 4)	# 14-17	 **attackbox here**
    RefreshMultihit()

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('AN_NmlAtk5A_4th')
    sprite('Action_003_06', 7)	# 18-24
    Recovery()
    Unknown2063()
    HitOrBlockCancel('AN_NmlAtk5A_4th')
    sprite('Action_003_07', 4)	# 25-28
    sprite('Action_003_08', 4)	# 29-32
    sprite('Action_003_09', 3)	# 33-35
    sprite('Action_003_10', 3)	# 36-38

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1100)
        GroundedHitstunAnimation(9)
        AirPushbackY(10000)
        AirPushbackX(30000)
        AirUntechableTime(30)
        Hitstop(4)
        Unknown11001(8, 8, 13)
        Unknown9016(1)
        JumpCancel_(0)
    sprite('Action_441_00', 2)	# 1-2
    sprite('Action_441_01', 2)	# 3-4
    sprite('Action_441_02', 2)	# 5-6
    sprite('Action_441_03', 4)	# 7-10
    sprite('Action_441_04', 2)	# 11-12
    GFX_0('Lin_430', 100)
    Unknown4020(1)
    GFX_0('Lin_433', 100)
    Unknown4020(1)
    SFX_4('uli204_2')
    SFX_0('006_swing_blade_1')
    sprite('Action_441_05', 2)	# 13-14
    sprite('Action_441_06', 2)	# 15-16
    sprite('Action_441_07', 2)	# 17-18
    sprite('Action_145_00', 2)	# 19-20
    Unknown14070('ShotDashCancel')
    sprite('Action_145_01', 2)	# 21-22
    Unknown23027()
    sprite('Action_145_02', 3)	# 23-25	 **attackbox here**
    GFX_0('Lin_432', 100)
    Unknown4020(1)
    GFX_0('Lin_434', 100)
    Unknown4020(1)
    SFX_0('006_swing_blade_2')
    sprite('Action_145_03', 3)	# 26-28
    RefreshMultihit()
    Unknown11001(0, 0, 5)
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        Unknown14072('ShotDashCancel')
    sprite('Action_145_04', 12)	# 29-40
    Unknown4020(0)
    Unknown14072('ShotDashCancel')
    Recovery()
    Unknown2063()
    sprite('Action_145_05', 5)	# 41-45
    Unknown14074('ShotDashCancel')
    sprite('Action_145_06', 4)	# 46-49

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(700)
        Unknown11092(1)
        AirPushbackY(10000)
        PushbackX(8000)
        Hitstop(6)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_249_00', 3)	# 1-3
    sprite('Action_249_01', 2)	# 4-5
    tag_voice(1, 'uli206_0', 'uli206_1', 'uli206_2', '')
    SFX_0('010_swing_sword_1')
    sprite('Action_249_02', 1)	# 6-6	 **attackbox here**
    GFX_0('EffARushSlash00', 100)
    sprite('Action_249_03', 2)	# 7-8
    sprite('Action_249_04', 2)	# 9-10
    sprite('Action_249_05', 2)	# 11-12
    SFX_0('008_swing_pole_1')
    sprite('Action_249_06', 4)	# 13-16	 **attackbox here**
    GFX_0('EffARushSlash01', 100)
    RefreshMultihit()
    Hitstop(10)

    def upon_ON_HIT_OR_BLOCK():
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk4A_2nd')
    sprite('Action_249_07', 6)	# 17-22
    callSubroutine('ChainRoot')
    HitOrBlockCancel('AN_NmlAtk4A_2nd')
    Recovery()
    Unknown2063()
    sprite('Action_249_08', 6)	# 23-28

@State
def AN_NmlAtk4A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(800)
        Unknown11092(1)
        AirPushbackY(10000)
        PushbackX(8000)
        Hitstop(6)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_253_00', 4)	# 1-4
    sprite('Action_253_01', 2)	# 5-6
    SFX_0('010_swing_sword_1')
    sprite('Action_253_02', 1)	# 7-7	 **attackbox here**
    GFX_0('EffARush2ndSlash00', 100)
    sprite('Action_253_03', 2)	# 8-9
    sprite('Action_253_04', 2)	# 10-11
    sprite('Action_253_05', 2)	# 12-13
    tag_voice(0, 'uli207_0', 'uli207_1', 'uli207_2', '')
    SFX_0('008_swing_pole_2')
    sprite('Action_253_06', 1)	# 14-14	 **attackbox here**
    GFX_0('EffARush2ndSlash01', 100)
    RefreshMultihit()
    Hitstop(10)
    PushbackX(-8000)
    AirPushbackX(-5000)
    AirPushbackY(-5000)

    def upon_ON_HIT_OR_BLOCK():
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk4A_3rd')
    sprite('Action_253_06', 3)	# 15-17	 **attackbox here**
    callSubroutine('ChainRoot')
    HitOrBlockCancel('AN_NmlAtk4A_3rd')
    sprite('Action_253_07', 2)	# 18-19
    Recovery()
    Unknown2063()
    sprite('Action_253_08', 8)	# 20-27
    sprite('Action_253_09', 6)	# 28-33

@State
def AN_NmlAtk4A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1000)
        AttackP2(70)
        Unknown11092(1)
        AirPushbackY(15000)
        Hitstop(6)
        Unknown9016(1)
    sprite('Action_255_07', 3)	# 1-3
    sprite('Action_255_08', 3)	# 4-6
    SFX_0('010_swing_sword_1')
    sprite('Action_255_09', 4)	# 7-10	 **attackbox here**
    GFX_0('EffBRush2ndSlash02', 100)
    RefreshMultihit()
    sprite('Action_255_10', 2)	# 11-12
    Unknown2015(125)
    sprite('Action_255_11', 2)	# 13-14
    sprite('Action_255_12', 2)	# 15-16
    sprite('Action_255_13', 2)	# 17-18
    Unknown2015(150)
    teleportRelativeX(55000)
    sprite('Action_255_14', 1)	# 19-19
    Unknown14070('ShotDashCancel')
    tag_voice(0, 'uli208_0', 'uli208_1', 'uli208_2', '')
    teleportRelativeX(65000)
    SFX_0('010_swing_sword_2')
    sprite('Action_255_14', 1)	# 20-20
    sprite('Action_255_15', 2)	# 21-22	 **attackbox here**
    GFX_0('EffEXRushSlash05', 100)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirPushbackX(20000)
    AirUntechableTime(30)
    Hitstop(13)

    def upon_ON_HIT_OR_BLOCK():
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk4A_4th')
        Unknown14072('ShotDashCancel')
    sprite('Action_255_16', 6)	# 23-28
    callSubroutine('ChainRoot')
    HitOrBlockCancel('AN_NmlAtk4A_4th')
    Unknown14072('ShotDashCancel')
    Recovery()
    Unknown2063()
    sprite('Action_255_17', 8)	# 29-36
    sprite('Action_255_18', 5)	# 37-41
    Unknown14074('ShotDashCancel')
    Unknown2015(125)
    teleportRelativeX(-25000)
    sprite('Action_255_19', 2)	# 42-43
    teleportRelativeX(-40000)
    Unknown2015(-1)
    sprite('Action_255_19', 2)	# 44-45

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(20000)
        AirUntechableTime(24)
        Unknown9016(1)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5B_2nd')
    sprite('Action_140_00', 4)	# 1-4
    sprite('Action_140_01', 3)	# 5-7
    tag_voice(1, 'uli109_0', 'uli109_1', 'uli109_2', '')
    sprite('Action_140_02', 3)	# 8-10
    sprite('Action_140_03', 2)	# 11-12
    SFX_0('010_swing_sword_1')
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_140_04', 6)	# 13-18	 **attackbox here**
    GFX_0('EffNmlAtk6CBlade1st', 100)
    sprite('Action_140_04', 13)	# 19-31	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('Action_140_05', 6)	# 32-37
    sprite('Action_140_06', 4)	# 38-41
    sprite('Action_140_07', 3)	# 42-44

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(20000)
        AirUntechableTime(24)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5B_3rd')
    sprite('Action_141_00', 5)	# 1-5
    sprite('Action_141_01', 5)	# 6-10
    sprite('Action_141_02', 2)	# 11-12
    tag_voice(0, 'uli110_0', 'uli110_1', 'uli110_2', '')
    SFX_0('010_swing_sword_2')
    sprite('Action_141_03', 2)	# 13-14	 **attackbox here**
    GFX_0('EffNmlAtk6CBlade2nd', 100)
    sprite('Action_141_03', 2)	# 15-16	 **attackbox here**
    sprite('Action_141_04', 6)	# 17-22
    Recovery()
    Unknown2063()
    sprite('Action_141_05', 4)	# 23-26
    sprite('Action_141_05', 4)	# 27-30
    sprite('Action_141_06', 4)	# 31-34
    sprite('Action_141_07', 4)	# 35-38

@State
def AN_NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(20000)
        AirPushbackY(-60000)
        AirUntechableTime(24)
        Unknown9310(1)
        Unknown9016(1)
        Unknown11056(0)
        Unknown2004(1, 0)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('ShotDashCancel')
    sprite('Action_142_00', 6)	# 1-6
    Unknown2015(125)
    sprite('Action_142_01', 3)	# 7-9
    Unknown2015(150)
    Unknown2016(250)
    sprite('Action_142_01', 2)	# 10-11
    Unknown2015(175)
    Unknown2016(300)
    sprite('Action_142_02', 4)	# 12-15
    Unknown2015(200)
    sprite('Action_142_03', 3)	# 16-18
    sprite('Action_142_04', 1)	# 19-19
    Unknown2015(250)
    tag_voice(0, 'uli111_0', 'uli111_1', 'uli111_2', '')
    SFX_0('006_swing_blade_2')
    sprite('Action_142_04', 1)	# 20-20
    GFX_0('EffNmlAtk6CBlade3rd', 100)
    sprite('Action_142_05', 5)	# 21-25	 **attackbox here**
    Unknown2015(200)
    Unknown2016(-1)
    SFX_0('209_down_normal_1')
    sprite('Action_142_06', 8)	# 26-33
    Recovery()
    Unknown2063()
    Unknown2015(175)
    sprite('Action_142_07', 6)	# 34-39
    Unknown2015(150)
    sprite('Action_142_08', 5)	# 40-44
    Unknown2015(125)
    sprite('Action_142_09', 3)	# 45-47
    Unknown2015(-1)
    sprite('Action_142_10', 3)	# 48-50

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(0)
    SFX_0('010_swing_sword_0')
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    GFX_0('EffNmlAtk2ABlade', 100)
    sprite('Action_004_03', 3)	# 9-11
    Recovery()
    WhiffCancelEnable(1)
    sprite('Action_004_04', 3)	# 12-14
    sprite('Action_004_04', 2)	# 15-16
    WhiffCancelEnable(0)
    sprite('Action_004_05', 5)	# 17-21

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(0)
    SFX_0('010_swing_sword_0')
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    GFX_0('EffNmlAtk2ABlade', 100)
    sprite('Action_004_03', 3)	# 9-11
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('Action_004_04', 5)	# 12-16
    sprite('Action_004_05', 5)	# 17-21

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        Unknown9016(1)
        callSubroutine('ChainRoot')
    sprite('Action_005_00', 4)	# 1-4
    sprite('Action_005_01', 3)	# 5-7
    Unknown7009(1)
    SFX_0('010_swing_sword_1')
    sprite('Action_005_02', 2)	# 8-9	 **attackbox here**
    teleportRelativeX(40000)
    GFX_0('EffNmlAtk2BBlade', 100)
    Recovery()
    sprite('Action_005_03', 5)	# 10-14
    Recovery()
    Unknown2063()
    sprite('Action_005_04', 6)	# 15-20
    sprite('Action_005_05', 5)	# 21-25
    teleportRelativeX(40000)
    sprite('Action_005_06', 4)	# 26-29
    teleportRelativeX(50000)

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        AirPushbackY(20000)
        AirUntechableTime(26)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HitLow(2)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        Unknown14085('CmnActCrushAttack')
    sprite('Action_006_00', 4)	# 1-4
    sprite('Action_006_01', 5)	# 5-9
    teleportRelativeX(50000)
    sprite('Action_006_02', 1)	# 10-10
    teleportRelativeX(43000)
    GFX_0('EffNmlAtk2CBlade', 100)
    tag_voice(1, 'uli107_0', 'uli107_1', 'uli107_2', '')
    SFX_0('010_swing_sword_2')
    sprite('Action_006_02', 1)	# 11-11
    sprite('Action_006_03', 6)	# 12-17	 **attackbox here**
    sprite('Action_006_04', 8)	# 18-25
    Recovery()
    Unknown2063()
    sprite('Action_006_05', 5)	# 26-30
    sprite('Action_006_06', 6)	# 31-36
    sprite('Action_006_07', 5)	# 37-41

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        AirPushbackX(10000)
        AirPushbackY(18000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A_2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_147_08', 6)	# 1-6
    sprite('Action_147_09', 2)	# 7-8
    Unknown7009(3)
    sprite('Action_147_09', 2)	# 9-10
    SFX_0('010_swing_sword_0')
    sprite('Action_147_10', 4)	# 11-14	 **attackbox here**
    GFX_0('EffNmlAtkAir5BBlade', 100)
    sprite('Action_147_11', 5)	# 15-19
    Recovery()
    Unknown2063()
    sprite('Action_147_12', 5)	# 20-24
    sprite('Action_147_13', 5)	# 25-29

@State
def NmlAtkAIR5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1200)
        Unknown9016(1)
        AirPushbackX(10000)
        AirPushbackY(18000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_008_00', 4)	# 1-4
    sprite('Action_008_01', 3)	# 5-7
    Unknown7009(3)
    SFX_0('010_swing_sword_1')
    sprite('Action_008_02', 2)	# 8-9	 **attackbox here**
    GFX_0('EffNmlAtkAir5A2ndBlade', 100)
    sprite('Action_008_03', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('Action_008_03', 4)	# 14-17
    sprite('Action_008_04', 5)	# 18-22
    sprite('Action_008_05', 5)	# 23-27

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1600)
        Unknown9016(1)
        AirPushbackX(10000)
        AirPushbackY(14000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_009_00', 2)	# 1-2
    sprite('Action_009_01', 4)	# 3-6
    sprite('Action_009_02', 2)	# 7-8
    Unknown7009(5)
    sprite('Action_009_02', 3)	# 9-11
    SFX_0('010_swing_sword_2')
    sprite('Action_009_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffNmlAtkAir5CBlade', 100)
    sprite('Action_009_04', 8)	# 16-23
    Recovery()
    Unknown2063()
    sprite('Action_009_05', 5)	# 24-28
    sprite('Action_009_06', 4)	# 29-32

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackX(24000)
        AirPushbackY(-30000)
        PushbackX(10000)
        AirUntechableTime(30)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        HitOverhead(0)
    sprite('Action_146_00', 5)	# 1-5
    physicsXImpulse(10000)
    physicsYImpulse(10000)
    sprite('Action_146_01', 6)	# 6-11
    sprite('Action_146_02', 1)	# 12-12
    Unknown1084(1)
    physicsYImpulse(-30000)
    setGravity(5000)
    physicsXImpulse(30000)
    tag_voice(1, 'uli108_0', 'uli108_1', 'uli108_2', '')
    SFX_0('004_swing_grap_1_1')
    SFX_0('000_airdash_2')
    sprite('Action_146_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_146_04', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_146_03', 3)	# 19-21	 **attackbox here**
    sprite('Action_146_04', 3)	# 22-24	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_146_05', 5)	# 25-29
    Unknown8000(100, 1, 1)
    Unknown1019(10)
    clearUponHandler(2)
    Recovery()
    Unknown2063()
    sprite('Action_146_06', 4)	# 30-33
    sprite('Action_146_07', 3)	# 34-36
    loopRest()

@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_150_00', 5)	# 1-5
    Unknown18009(1)
    Unknown1015(34000)
    sprite('Action_150_01', 4)	# 6-9
    tag_voice(1, 'uli112_0', 'uli112_1', 'uli112_2', '')
    setInvincible(1)
    Unknown2017(0)
    sprite('Action_150_02', 4)	# 10-13
    sprite('Action_150_03', 2)	# 14-15
    sprite('Action_150_05', 4)	# 16-19
    Unknown2006()
    sprite('Action_150_07', 4)	# 20-23
    setInvincible(0)
    Unknown1084(1)
    sprite('Action_150_06', 3)	# 24-26
    sprite('Action_150_08', 3)	# 27-29

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
    sprite('Action_068_00', 4)	# 1-4
    sprite('Action_068_02', 3)	# 5-7
    SLOT_12 = SLOT_19
    Unknown1019(5)
    physicsYImpulse(23000)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    Unknown23087(100000)
    sprite('Action_068_03', 3)	# 8-10
    sprite('Action_068_04', 3)	# 11-13
    tag_voice(1, 'uli156_0', 'uli156_1', '', '')
    sprite('Action_068_05', 3)	# 14-16
    sprite('Action_068_06', 3)	# 17-19
    sprite('Action_147_08', 3)	# 20-22
    sprite('Action_147_09', 3)	# 23-25
    sprite('Action_147_10', 3)	# 26-28	 **attackbox here**
    GFX_0('EffNmlAtkAir5BBlade', 100)
    SFX_0('010_swing_sword_0')
    sprite('Action_147_11', 6)	# 29-34
    sprite('Action_147_12', 6)	# 35-40
    sprite('Action_147_13', 7)	# 41-47
    label(0)
    sprite('Action_068_10', 3)	# 48-50
    sprite('Action_068_11', 2)	# 51-52
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_069_00', 2)	# 53-54
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_069_01', 3)	# 55-57
    sprite('Action_069_02', 5)	# 58-62
    sprite('Action_069_03', 3)	# 63-65
    Unknown18009(0)

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 19)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_147_11', 6)	# 1-6
    sprite('Action_147_12', 6)	# 7-12
    sprite('Action_147_13', 7)	# 13-19
    sprite('Action_068_10', 3)	# 20-22
    sprite('Action_068_11', 2)	# 23-24
    label(1)
    sprite('Action_069_00', 4)	# 25-28
    Unknown8000(100, 1, 1)
    sprite('Action_069_01', 50)	# 29-78
    label(2)
    sprite('Action_145_00', 4)	# 79-82
    clearUponHandler(17)
    teleportRelativeY(0)
    tag_voice(0, 'uli157_0', 'uli157_1', '', '')
    sprite('Action_145_01', 6)	# 83-88
    sprite('Action_145_02', 2)	# 89-90	 **attackbox here**
    GFX_0('EffNmlAtk5BBlade', 100)
    SFX_0('010_swing_sword_1')
    sprite('Action_145_03', 3)	# 91-93
    sprite('Action_145_04', 6)	# 94-99
    sprite('Action_145_05', 5)	# 100-104
    sprite('Action_145_06', 4)	# 105-108
    SFX_FOOTSTEP_(100, 1, 1)
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('Action_000_00', 7)	# 109-115	 **attackbox here**
    sprite('Action_000_01', 7)	# 116-122	 **attackbox here**
    sprite('Action_000_02', 6)	# 123-128	 **attackbox here**
    sprite('Action_000_03', 6)	# 129-134	 **attackbox here**
    sprite('Action_000_04', 8)	# 135-142	 **attackbox here**
    sprite('Action_000_05', 5)	# 143-147	 **attackbox here**
    sprite('Action_000_06', 5)	# 148-152	 **attackbox here**
    sprite('Action_000_07', 5)	# 153-157	 **attackbox here**
    sprite('Action_000_08', 6)	# 158-163	 **attackbox here**
    sprite('Action_000_09', 5)	# 164-168	 **attackbox here**
    sprite('Action_000_10', 6)	# 169-174	 **attackbox here**
    sprite('Action_000_11', 8)	# 175-182	 **attackbox here**
    sprite('Action_000_12', 5)	# 183-187	 **attackbox here**
    sprite('Action_000_13', 5)	# 188-192	 **attackbox here**
    sprite('Action_000_14', 6)	# 193-198	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 199-199

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_251_28', 3)	# 1-3
    sprite('Action_251_29', 3)	# 4-6
    sprite('Action_251_30', 2)	# 7-8
    sprite('Action_251_31', 2)	# 9-10
    sprite('Action_251_32', 2)	# 11-12
    sprite('Action_251_33', 2)	# 13-14
    sprite('Action_251_34', 1)	# 15-15	 **attackbox here**
    GFX_0('EffEXRushSlash05', 100)
    SFX_0('010_swing_sword_2')
    sprite('Action_251_35', 6)	# 16-21
    sprite('Action_251_36', 5)	# 22-26
    sprite('Action_251_37', 5)	# 27-31
    sprite('Action_251_38', 3)	# 32-34
    sprite('Action_000_00', 7)	# 35-41	 **attackbox here**
    sprite('Action_000_01', 7)	# 42-48	 **attackbox here**
    sprite('Action_000_02', 6)	# 49-54	 **attackbox here**
    sprite('Action_000_03', 6)	# 55-60	 **attackbox here**
    sprite('Action_000_04', 8)	# 61-68	 **attackbox here**
    sprite('Action_000_05', 5)	# 69-73	 **attackbox here**
    sprite('Action_000_06', 5)	# 74-78	 **attackbox here**
    sprite('Action_000_07', 5)	# 79-83	 **attackbox here**
    sprite('Action_000_08', 6)	# 84-89	 **attackbox here**
    sprite('Action_000_09', 5)	# 90-94	 **attackbox here**
    sprite('Action_000_10', 6)	# 95-100	 **attackbox here**
    sprite('Action_000_11', 8)	# 101-108	 **attackbox here**
    sprite('Action_000_12', 5)	# 109-113	 **attackbox here**
    sprite('Action_000_13', 5)	# 114-118	 **attackbox here**
    sprite('Action_000_14', 6)	# 119-124	 **attackbox here**
    label(0)
    sprite('Action_000_00', 7)	# 125-131	 **attackbox here**
    sprite('Action_000_01', 7)	# 132-138	 **attackbox here**
    sprite('Action_000_02', 6)	# 139-144	 **attackbox here**
    sprite('Action_000_03', 6)	# 145-150	 **attackbox here**
    sprite('Action_000_04', 8)	# 151-158	 **attackbox here**
    sprite('Action_000_05', 5)	# 159-163	 **attackbox here**
    sprite('Action_000_06', 5)	# 164-168	 **attackbox here**
    sprite('Action_000_07', 5)	# 169-173	 **attackbox here**
    sprite('Action_000_08', 6)	# 174-179	 **attackbox here**
    sprite('Action_000_09', 5)	# 180-184	 **attackbox here**
    sprite('Action_000_10', 6)	# 185-190	 **attackbox here**
    sprite('Action_000_11', 8)	# 191-198	 **attackbox here**
    sprite('Action_000_12', 5)	# 199-203	 **attackbox here**
    sprite('Action_000_13', 5)	# 204-208	 **attackbox here**
    sprite('Action_000_14', 6)	# 209-214	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 215-215

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('Action_140_00', 3)	# 1-3
    sprite('Action_140_01', 6)	# 4-9
    sprite('Action_140_02', 6)	# 10-15
    sprite('Action_140_03', 4)	# 16-19
    tag_voice(0, 'uli158_0', 'uli158_1', '', '')
    sprite('Action_140_04', 6)	# 20-25	 **attackbox here**
    GFX_0('EffNmlAtk6CBlade1st', 100)
    SFX_0('006_swing_blade_0')
    sprite('Action_140_05', 25)	# 26-50
    sprite('Action_140_06', 5)	# 51-55
    sprite('Action_140_07', 5)	# 56-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 20)	# 1-20
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 21-21
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('Action_184_00', 1)	# 22-22
    sprite('Action_184_01', 1)	# 23-23
    physicsXImpulse(38000)
    physicsYImpulse(23000)
    setGravity(3000)
    Unknown8001(0, 100)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('Action_184_02', 1)	# 24-24
    sprite('Action_184_03', 1)	# 25-25
    sprite('Action_184_04', 2)	# 26-27
    sprite('Action_184_05', 2)	# 28-29
    sprite('Action_184_06', 3)	# 30-32
    sprite('Action_184_07', 4)	# 33-36
    Unknown1019(60)
    sprite('Action_184_08', 5)	# 37-41
    sprite('Action_184_09', 5)	# 42-46
    label(1)
    sprite('Action_184_10', 1)	# 47-47	 **attackbox here**
    GFX_0('EffEXAssaultSlash', 100)
    SFX_0('010_swing_sword_1')
    physicsXImpulse(0)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_184_10', 1)	# 48-48	 **attackbox here**
    sprite('Action_184_10', 1)	# 49-49	 **attackbox here**
    sprite('Action_184_11', 1)	# 50-50	 **attackbox here**
    sprite('Action_184_12', 7)	# 51-57
    sprite('Action_184_13', 5)	# 58-62
    sprite('Action_184_14', 4)	# 63-66
    sprite('Action_184_15', 4)	# 67-70
    sprite('Action_000_00', 7)	# 71-77	 **attackbox here**
    sprite('Action_000_01', 7)	# 78-84	 **attackbox here**
    sprite('Action_000_02', 6)	# 85-90	 **attackbox here**
    sprite('Action_000_03', 6)	# 91-96	 **attackbox here**
    sprite('Action_000_04', 8)	# 97-104	 **attackbox here**
    sprite('Action_000_05', 5)	# 105-109	 **attackbox here**
    sprite('Action_000_06', 5)	# 110-114	 **attackbox here**
    sprite('Action_000_07', 5)	# 115-119	 **attackbox here**
    sprite('Action_000_08', 6)	# 120-125	 **attackbox here**
    sprite('Action_000_09', 5)	# 126-130	 **attackbox here**
    sprite('Action_000_10', 6)	# 131-136	 **attackbox here**
    sprite('Action_000_11', 8)	# 137-144	 **attackbox here**
    sprite('Action_000_12', 5)	# 145-149	 **attackbox here**
    sprite('Action_000_13', 5)	# 150-154	 **attackbox here**
    sprite('Action_000_14', 6)	# 155-160	 **attackbox here**

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('Action_142_00', 2)	# 1-2
    sprite('Action_142_01', 2)	# 3-4
    sprite('Action_142_02', 2)	# 5-6
    sprite('Action_142_03', 2)	# 7-8
    teleportRelativeX(-40000)
    sprite('Action_142_04', 3)	# 9-11
    teleportRelativeX(-60000)
    sprite('Action_142_05', 3)	# 12-14	 **attackbox here**
    teleportRelativeX(-80000)
    GFX_0('EffNmlAtk6CBlade3rd', 100)
    SFX_0('010_swing_sword_2')
    Unknown36(1)
    teleportRelativeX(250000)
    Unknown35()
    sprite('Action_142_06', 3)	# 15-17
    sprite('Action_142_07', 3)	# 18-20
    sprite('Action_142_08', 3)	# 21-23
    teleportRelativeX(80000)
    sprite('Action_142_09', 3)	# 24-26
    teleportRelativeX(60000)
    sprite('Action_142_10', 3)	# 27-29
    teleportRelativeX(40000)
    sprite('Action_000_00', 7)	# 30-36	 **attackbox here**
    sprite('Action_000_01', 7)	# 37-43	 **attackbox here**
    sprite('Action_000_02', 6)	# 44-49	 **attackbox here**
    sprite('Action_000_03', 6)	# 50-55	 **attackbox here**
    sprite('Action_000_04', 8)	# 56-63	 **attackbox here**
    sprite('Action_000_05', 5)	# 64-68	 **attackbox here**
    sprite('Action_000_06', 5)	# 69-73	 **attackbox here**
    sprite('Action_000_07', 5)	# 74-78	 **attackbox here**
    sprite('Action_000_08', 6)	# 79-84	 **attackbox here**
    sprite('Action_000_09', 5)	# 85-89	 **attackbox here**
    sprite('Action_000_10', 6)	# 90-95	 **attackbox here**
    sprite('Action_000_11', 8)	# 96-103	 **attackbox here**
    sprite('Action_000_12', 5)	# 104-108	 **attackbox here**
    sprite('Action_000_13', 5)	# 109-113	 **attackbox here**
    sprite('Action_000_14', 6)	# 114-119	 **attackbox here**

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('Action_140_00', 3)	# 1-3
    sprite('Action_140_01', 6)	# 4-9
    sprite('Action_140_02', 6)	# 10-15
    sprite('Action_140_03', 4)	# 16-19
    sprite('Action_140_04', 6)	# 20-25	 **attackbox here**
    GFX_0('EffNmlAtk6CBlade1st', 100)
    SFX_0('006_swing_blade_0')
    sprite('Action_140_05', 25)	# 26-50
    sprite('Action_140_06', 5)	# 51-55
    sprite('Action_140_07', 5)	# 56-60

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
                Unknown1015(1000)
                if (SLOT_12 >= 32000):
                    SLOT_12 = 32000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('Action_045_13', 4)	# 1-4
    sprite('Action_045_00', 3)	# 5-7
    sprite('Action_045_01', 3)	# 8-10
    sprite('Action_045_02', 3)	# 11-13
    label(0)
    sprite('Action_045_03', 3)	# 14-16
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 17-19
    sprite('Action_045_05', 3)	# 20-22
    sprite('Action_045_06', 3)	# 23-25
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 26-28
    sprite('Action_045_08', 3)	# 29-31
    sprite('Action_045_09', 3)	# 32-34
    sprite('Action_045_02', 3)	# 35-37
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 2)	# 38-39
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 1)	# 40-40
    sprite('Action_055_02', 3)	# 41-43	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown1084(1)
    sprite('Action_055_02', 3)	# 44-46	 **attackbox here**
    StartMultihit()
    sprite('Action_055_03', 2)	# 47-48
    sprite('Action_055_04', 7)	# 49-55
    SFX_4('uli154')
    sprite('Action_055_05', 5)	# 56-60
    sprite('Action_055_06', 3)	# 61-63
    sprite('Action_055_07', 3)	# 64-66

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(200)
        AttackP2(50)
        Unknown11092(1)
        Unknown11073(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(1800)
        AirUntechableTime(40)
        Unknown9310(90)
        JumpCancel_(0)
        Unknown13024(0)
        Unknown11064(1)
        Unknown11069('ThrowExe')
    sprite('Action_055_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00', 1)	# 5-5
    SFX_0('003_swing_grap_0_1')
    sprite('Action_057_00', 1)	# 6-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_01', 8)	# 7-14	 **attackbox here**
    tag_voice(1, 'uli153_0', '', '', '')
    sprite('Action_057_02', 4)	# 15-18
    Unknown23027()
    sprite('Action_057_03', 2)	# 19-20
    sprite('Action_057_04', 2)	# 21-22
    sprite('Action_057_05', 3)	# 23-25
    sprite('Action_057_06', 4)	# 26-29
    physicsYImpulse(11000)
    setGravity(2200)
    teleportRelativeX(10000)
    sprite('Action_057_07', 3)	# 30-32
    teleportRelativeX(10000)
    sprite('Action_057_08', 3)	# 33-35
    teleportRelativeX(10000)
    sprite('Action_057_09', 1)	# 36-36	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_057_10', 5)	# 37-41
    sprite('Action_057_11', 3)	# 42-44
    tag_voice(1, 'uli153_1', '', '', '')
    Unknown1084(1)
    sprite('Action_057_12', 1)	# 45-45	 **attackbox here**
    AttackLevel_(4)
    Damage(1800)
    YImpluseBeforeWallbounce(50000)
    Unknown11073(1)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(500)
    AirPushbackY(-40000)
    Unknown9310(40)
    Unknown9016(1)
    RefreshMultihit()
    Unknown11064(0)
    Unknown11069('')
    Unknown11083(1)
    clearUponHandler(78)

    def upon_78():
        Unknown13024(1)
        JumpCancel_(1)
    sprite('Action_057_13', 6)	# 46-51
    sprite('Action_057_14', 3)	# 52-54
    sprite('Action_057_15', 2)	# 55-56
    sprite('Action_057_16', 5)	# 57-61
    physicsXImpulse(-10000)
    physicsYImpulse(12000)
    setGravity(2500)
    label(0)
    sprite('Action_057_17', 5)	# 62-66
    sendToLabelUpon(2, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_057_18', 2)	# 67-68
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_057_19', 2)	# 69-70
    sprite('Action_057_20', 2)	# 71-72
    sprite('Action_057_21', 2)	# 73-74

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
                Unknown1015(1000)
                if (SLOT_12 >= 32000):
                    SLOT_12 = 32000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('Action_045_13', 4)	# 1-4
    sprite('Action_045_00', 3)	# 5-7
    sprite('Action_045_01', 3)	# 8-10
    sprite('Action_045_02', 3)	# 11-13
    label(0)
    sprite('Action_045_03', 3)	# 14-16
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 17-19
    sprite('Action_045_05', 3)	# 20-22
    sprite('Action_045_06', 3)	# 23-25
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 26-28
    sprite('Action_045_08', 3)	# 29-31
    sprite('Action_045_09', 3)	# 32-34
    sprite('Action_045_02', 3)	# 35-37
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 2)	# 38-39
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 1)	# 40-40
    sprite('Action_055_02', 3)	# 41-43	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown1084(1)
    sprite('Action_055_02', 3)	# 44-46	 **attackbox here**
    StartMultihit()
    sprite('Action_055_03', 2)	# 47-48
    sprite('Action_055_04', 7)	# 49-55
    SFX_4('uli154')
    sprite('Action_055_05', 5)	# 56-60
    sprite('Action_055_06', 3)	# 61-63
    sprite('Action_055_07', 3)	# 64-66

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(200)
        AttackP2(50)
        Unknown11092(1)
        Unknown11073(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(1800)
        AirUntechableTime(40)
        Unknown9310(90)
        JumpCancel_(0)
        Unknown13024(0)
        Unknown11064(1)
        Unknown11069('BackThrowExe')
    sprite('Action_055_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00', 1)	# 5-5
    SFX_0('003_swing_grap_0_1')
    Unknown2005()
    sprite('Action_057_00', 1)	# 6-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_01', 8)	# 7-14	 **attackbox here**
    tag_voice(1, 'uli153_0', '', '', '')
    sprite('Action_057_02', 4)	# 15-18
    Unknown23027()
    sprite('Action_057_03', 2)	# 19-20
    sprite('Action_057_04', 2)	# 21-22
    sprite('Action_057_05', 3)	# 23-25
    sprite('Action_057_06', 4)	# 26-29
    physicsYImpulse(11000)
    setGravity(2200)
    teleportRelativeX(10000)
    sprite('Action_057_07', 3)	# 30-32
    teleportRelativeX(10000)
    sprite('Action_057_08', 3)	# 33-35
    teleportRelativeX(10000)
    sprite('Action_057_09', 1)	# 36-36	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_057_10', 5)	# 37-41
    sprite('Action_057_11', 3)	# 42-44
    tag_voice(1, 'uli153_1', '', '', '')
    Unknown1084(1)
    sprite('Action_057_12', 1)	# 45-45	 **attackbox here**
    AttackLevel_(4)
    Damage(1800)
    YImpluseBeforeWallbounce(50000)
    Unknown11073(1)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(500)
    AirPushbackY(-40000)
    Unknown9310(40)
    Unknown9016(1)
    RefreshMultihit()
    Unknown11064(0)
    Unknown11069('')
    Unknown11083(1)
    clearUponHandler(78)

    def upon_78():
        Unknown13024(1)
        JumpCancel_(1)
    sprite('Action_057_13', 6)	# 46-51
    sprite('Action_057_14', 3)	# 52-54
    sprite('Action_057_15', 2)	# 55-56
    sprite('Action_057_16', 5)	# 57-61
    physicsXImpulse(-10000)
    physicsYImpulse(12000)
    setGravity(2500)
    label(0)
    sprite('Action_057_17', 5)	# 62-66
    sendToLabelUpon(2, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_057_18', 2)	# 67-68
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_057_19', 2)	# 69-70
    sprite('Action_057_20', 2)	# 71-72
    sprite('Action_057_21', 2)	# 73-74

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(3)
        Damage(500)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(15000)
        AirPushbackX(6000)
        Unknown9016(1)
        AirUntechableTime(60)
        Unknown1084(0)
        sendToLabelUpon(2, 1)

        def upon_12():
            Unknown2037(1)
    sprite('Action_100_00', 6)	# 1-6
    setInvincible(1)
    sprite('Action_100_01', 3)	# 7-9	 **attackbox here**
    StartMultihit()
    sprite('Action_100_01', 3)	# 10-12	 **attackbox here**
    Hitstop(3)
    physicsXImpulse(11000)
    sprite('Action_101_02', 2)	# 13-14	 **attackbox here**
    Unknown23027()
    sprite('Action_101_03', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    SFX_0('010_swing_sword_0')
    AirPushbackY(35000)
    physicsYImpulse(23000)
    physicsXImpulse(4000)
    setGravity(1800)
    if SLOT_2:
        SFX_4('uli201')
    else:
        tag_voice(1, 'uli200_0', 'uli200_1', '', '')
        Unknown2037(0)
    clearUponHandler(12)
    sprite('Action_101_04', 2)	# 16-17	 **attackbox here**
    GFX_0('EffNmlReversalAction00', 100)
    sprite('Action_101_05', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_101_06', 1)	# 20-20	 **attackbox here**
    sprite('Action_101_07', 1)	# 21-21
    setInvincible(0)
    sprite('Action_101_08', 1)	# 22-22
    sprite('Action_101_09', 1)	# 23-23
    sprite('Action_101_10', 3)	# 24-26
    sprite('Action_101_11', 2)	# 27-28
    sprite('Action_101_12', 1)	# 29-29
    physicsYImpulse(32000)
    physicsXImpulse(7000)
    setGravity(2600)
    sprite('Action_101_13', 1)	# 30-30
    sprite('Action_101_14', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    SFX_0('010_swing_sword_1')
    Hitstop(1)
    GFX_0('EffNmlReversalAction01', 100)
    sprite('Action_101_14', 1)	# 33-33	 **attackbox here**
    if SLOT_2:
        SFX_4('uli202')
    RefreshMultihit()
    sprite('Action_101_15', 3)	# 34-36	 **attackbox here**
    RefreshMultihit()
    Hitstop(10)
    AirPushbackX(12500)
    sprite('Action_101_16', 1)	# 37-37
    sprite('Action_101_17', 1)	# 38-38
    sprite('Action_101_18', 2)	# 39-40
    sprite('Action_101_19', 1)	# 41-41
    sprite('Action_101_20', 3)	# 42-44
    sprite('Action_101_21', 2)	# 45-46
    sprite('Action_101_22', 1)	# 47-47
    physicsYImpulse(38000)
    physicsXImpulse(8000)
    setGravity(2600)
    sprite('Action_101_23', 1)	# 48-48
    sprite('Action_101_24', 1)	# 49-49	 **attackbox here**
    Hitstop(1)
    RefreshMultihit()
    GFX_0('EffNmlReversalAction01', 100)
    SFX_0('010_swing_sword_1')
    sprite('Action_101_24', 1)	# 50-50	 **attackbox here**
    RefreshMultihit()
    sprite('Action_101_25', 7)	# 51-57	 **attackbox here**
    if SLOT_2:
        SFX_4('uli203')
    Hitstop(15)
    RefreshMultihit()
    AirPushbackY(32000)
    AirPushbackX(9500)
    sprite('Action_101_26', 6)	# 58-63
    sprite('Action_101_27', 3)	# 64-66
    sprite('Action_101_28', 4)	# 67-70
    sprite('Action_101_29', 4)	# 71-74
    sprite('Action_101_30', 7)	# 75-81
    sprite('Action_101_31', 3)	# 82-84
    label(0)
    sprite('Action_101_32', 2)	# 85-86
    sprite('Action_101_33', 2)	# 87-88
    gotoLabel(0)
    label(1)
    sprite('Action_101_33', 4)	# 89-92
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_101_34', 4)	# 93-96
    sprite('Action_101_35', 6)	# 97-102
    sprite('Action_101_36', 6)	# 103-108

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(3)
        Damage(550)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(35000)
        AirPushbackX(6000)
        Unknown9016(1)
        AirUntechableTime(39)
        Unknown1084(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('Action_101_03', 9)	# 1-9	 **attackbox here**
    setInvincible(1)
    StartMultihit()
    Hitstop(3)
    physicsYImpulse(26500)
    physicsXImpulse(4000)
    setGravity(1650)
    sprite('Action_101_03', 2)	# 10-11	 **attackbox here**
    RefreshMultihit()
    SFX_0('010_swing_sword_0')
    sprite('Action_101_04', 2)	# 12-13	 **attackbox here**
    tag_voice(1, 'uli200_0', 'uli200_1', '', '')
    GFX_0('EffNmlReversalAction00', 100)
    sprite('Action_101_05', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    Hitstop(3)
    sprite('Action_101_06', 1)	# 16-16	 **attackbox here**
    sprite('Action_101_07', 1)	# 17-17
    setInvincible(0)
    sprite('Action_101_08', 1)	# 18-18
    sprite('Action_101_09', 1)	# 19-19
    sprite('Action_101_10', 3)	# 20-22
    sprite('Action_101_11', 2)	# 23-24
    sprite('Action_101_12', 1)	# 25-25
    physicsYImpulse(27000)
    physicsXImpulse(7000)
    setGravity(2600)
    sprite('Action_101_13', 1)	# 26-26
    sprite('Action_101_14', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    Hitstop(1)
    GFX_0('EffNmlReversalAction01', 100)
    SFX_0('010_swing_sword_1')
    sprite('Action_101_14', 1)	# 29-29	 **attackbox here**
    RefreshMultihit()
    sprite('Action_101_15', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    Hitstop(10)
    AirPushbackX(12500)
    sprite('Action_101_16', 1)	# 33-33
    sprite('Action_101_17', 1)	# 34-34
    sprite('Action_101_18', 2)	# 35-36
    sprite('Action_101_19', 1)	# 37-37
    sprite('Action_101_20', 3)	# 38-40
    sprite('Action_101_21', 2)	# 41-42
    sprite('Action_101_22', 1)	# 43-43
    physicsYImpulse(33500)
    physicsXImpulse(10000)
    setGravity(2600)
    sprite('Action_101_23', 1)	# 44-44
    sprite('Action_101_24', 1)	# 45-45	 **attackbox here**
    Hitstop(1)
    RefreshMultihit()
    GFX_0('EffNmlReversalAction01', 100)
    SFX_0('010_swing_sword_1')
    sprite('Action_101_24', 1)	# 46-46	 **attackbox here**
    RefreshMultihit()
    sprite('Action_101_25', 7)	# 47-53	 **attackbox here**
    Hitstop(15)
    RefreshMultihit()
    AirPushbackY(32000)
    AirPushbackX(10000)
    sprite('Action_101_26', 6)	# 54-59
    sprite('Action_101_27', 3)	# 60-62
    sprite('Action_101_28', 4)	# 63-66
    sprite('Action_101_29', 4)	# 67-70
    sprite('Action_101_30', 7)	# 71-77
    sprite('Action_101_31', 3)	# 78-80
    label(0)
    sprite('Action_101_32', 2)	# 81-82
    sprite('Action_101_33', 2)	# 83-84
    gotoLabel(0)
    label(1)
    sprite('Action_101_33', 2)	# 85-86
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_101_34', 2)	# 87-88
    sprite('Action_101_35', 3)	# 89-91
    sprite('Action_101_36', 3)	# 92-94

@State
def Shot_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
    sprite('Action_440_00', 6)	# 1-6
    sprite('Action_440_01', 4)	# 7-10
    sprite('Action_440_02', 4)	# 11-14
    Unknown14070('ShotDashCancel')
    sprite('Action_440_03', 6)	# 15-20
    SFX_0('010_swing_sword_2')
    sprite('Action_440_04', 2)	# 21-22
    GFX_0('ShotA', 0)
    GFX_0('EffShotSlash', 100)
    tag_voice(1, 'uli204_0', 'uli204_1', 'uli204_2', '')
    sprite('Action_440_05', 6)	# 23-28
    Unknown14072('ShotDashCancel')
    sprite('Action_440_06', 7)	# 29-35
    sprite('Action_440_07', 5)	# 36-40
    sprite('Action_440_08', 5)	# 41-45
    Unknown14074('ShotDashCancel')
    Recovery()
    sprite('Action_440_09', 4)	# 46-49

@State
def Shot_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
    sprite('Action_441_00', 2)	# 1-2
    sprite('Action_441_01', 2)	# 3-4
    sprite('Action_441_02', 3)	# 5-7
    sprite('Action_441_03', 4)	# 8-11
    SFX_0('010_swing_sword_2')
    sprite('Action_441_04', 2)	# 12-13
    Unknown14070('ShotDashCancel')
    GFX_0('ShotB', 0)
    GFX_0('EffShotSlash', 100)
    tag_voice(1, 'uli204_0', 'uli204_1', 'uli204_2', '')
    sprite('Action_441_05', 6)	# 14-19
    sprite('Action_441_06', 14)	# 20-33
    Unknown14072('ShotDashCancel')
    sprite('Action_441_07', 5)	# 34-38
    sprite('Action_441_08', 5)	# 39-43
    Unknown14074('ShotDashCancel')
    Recovery()
    sprite('Action_441_09', 4)	# 44-47

@State
def ShotDashCancel():

    def upon_IMMEDIATE():
        Unknown17013()
        WhiffCancel('Assault_A')
        WhiffCancelEnable(1)
    sprite('Action_045_00', 3)	# 1-3
    sprite('Action_045_01', 3)	# 4-6
    physicsXImpulse(36000)
    sprite('Action_045_02', 3)	# 7-9
    sprite('Action_045_03', 3)	# 10-12
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 13-15
    sprite('Action_045_05', 3)	# 16-18
    Unknown8006(100, 1, 1)
    sprite('Action_045_11', 2)	# 19-20
    Unknown1019(30)
    sprite('Action_045_12', 3)	# 21-23
    Unknown1019(10)
    sprite('Action_045_13', 2)	# 24-25
    physicsXImpulse(0)
    loopRest()

@State
def Assault_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_3():
            if (SLOT_163 <= 0):
                Unknown2037(1)
                clearUponHandler(3)
    sprite('Action_045_00', 2)	# 1-2
    sprite('Action_045_01', 2)	# 3-4
    Unknown8006(100, 1, 1)
    physicsXImpulse(36000)
    sprite('Action_150_00', 5)	# 5-9
    SFX_0('019_cloth_a')
    Unknown18009(1)
    Unknown2017(0)
    setInvincible(1)
    Unknown22019('0100000001000000000000000100000000000000')
    sprite('Action_150_01', 4)	# 10-13
    sprite('Action_150_02', 4)	# 14-17
    Unknown2017(1)
    setInvincible(0)
    sprite('Action_150_03', 2)	# 18-19
    Unknown1019(50)
    sprite('Action_150_05', 3)	# 20-22
    Unknown23183('416374696f6e5f3135305f303700000000000000000000000000000000000000030000000200000002000000')
    if SLOT_2:
        Unknown2005()
    Unknown1019(50)
    sprite('Action_150_06', 3)	# 23-25
    Unknown23183('416374696f6e5f3135305f303800000000000000000000000000000000000000030000000200000002000000')
    Unknown1019(0)
    sprite('Action_014_01', 2)	# 26-27
    Unknown18009(0)
    sprite('Action_014_02', 2)	# 28-29

@State
def Assault_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(18000)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Hitstop(1)
        Unknown9016(1)
        HitOverhead(2)
        sendToLabelUpon(2, 1)
    sprite('Action_182_00', 3)	# 1-3
    sprite('Action_182_01', 2)	# 4-5
    Unknown23087(50000)
    physicsXImpulse(24000)
    physicsYImpulse(16000)
    setGravity(2000)
    Unknown8001(0, 100)
    tag_voice(1, 'uli212_0', 'uli212_1', 'uli212_2', '')
    SFX_0('002_highjump_0')
    sprite('Action_182_02', 2)	# 6-7
    sprite('Action_182_03', 2)	# 8-9
    sprite('Action_182_04', 2)	# 10-11
    sprite('Action_182_05', 2)	# 12-13
    sprite('Action_182_06', 2)	# 14-15
    sprite('Action_182_07', 2)	# 16-17
    sprite('Action_182_08', 3)	# 18-20
    sprite('Action_182_09', 32767)	# 21-32787
    label(1)
    sprite('Action_182_10', 1)	# 32788-32788	 **attackbox here**
    StartMultihit()
    GFX_0('EffAssaultSlash', 100)
    SFX_0('010_swing_sword_2')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown23087(-1)
    sprite('Action_182_10', 1)	# 32789-32789	 **attackbox here**
    sprite('Action_182_10', 1)	# 32790-32790	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    PushbackX(12000)
    sprite('Action_182_11', 4)	# 32791-32794
    Recovery()
    sprite('Action_182_12', 6)	# 32795-32800
    sprite('Action_182_13', 8)	# 32801-32808
    sprite('Action_182_14', 4)	# 32809-32812
    sprite('Action_182_15', 3)	# 32813-32815

@State
def AirShot_A():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('Action_448_00', 2)	# 1-2
    physicsXImpulse(3000)
    physicsYImpulse(16000)
    setGravity(1400)
    sprite('Action_448_01', 3)	# 3-5
    sprite('Action_448_02', 3)	# 6-8
    sprite('Action_448_03', 3)	# 9-11
    sprite('Action_448_04', 5)	# 12-16
    sprite('Action_448_05', 4)	# 17-20
    SFX_0('010_swing_sword_2')
    sprite('Action_448_06', 3)	# 21-23
    GFX_0('EffAirShotSlash', 100)
    GFX_0('AirShotA', 0)
    tag_voice(1, 'uli204_0', 'uli204_1', 'uli204_2', '')
    Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_448_07', 10)	# 24-33
    sprite('Action_448_08', 6)	# 34-39
    sprite('Action_448_09', 4)	# 40-43
    Recovery()
    label(0)
    sprite('Action_448_09', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_023_00', 3)	# 48-50
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_023_01', 3)	# 51-53
    sprite('Action_023_02', 3)	# 54-56
    sprite('Action_023_03', 4)	# 57-60

@State
def AirShot_B():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('Action_448_00', 2)	# 1-2
    physicsXImpulse(3000)
    physicsYImpulse(20000)
    setGravity(1400)
    sprite('Action_448_01', 3)	# 3-5
    sprite('Action_448_02', 3)	# 6-8
    sprite('Action_448_03', 3)	# 9-11
    sprite('Action_448_04', 10)	# 12-21
    sprite('Action_448_05', 4)	# 22-25
    SFX_0('010_swing_sword_2')
    sprite('Action_448_06', 3)	# 26-28
    GFX_0('EffAirShotSlash', 100)
    GFX_0('AirShotB', 0)
    tag_voice(1, 'uli204_0', 'uli204_1', 'uli204_2', '')
    Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_448_07', 10)	# 29-38
    sprite('Action_448_08', 6)	# 39-44
    sprite('Action_448_09', 4)	# 45-48
    Recovery()
    label(0)
    sprite('Action_448_09', 4)	# 49-52
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_023_00', 3)	# 53-55
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_023_01', 3)	# 56-58
    sprite('Action_023_02', 3)	# 59-61
    sprite('Action_023_03', 4)	# 62-65

@State
def Shot_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
    sprite('Action_441_00', 2)	# 1-2
    sprite('Action_441_01', 1)	# 3-3
    sprite('Action_441_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'uli205_0', 'uli205_1', 'uli205_2', '')
    sprite('Action_441_02', 3)	# 5-7
    sprite('Action_441_03', 4)	# 8-11
    Unknown14070('ShotDashCancel')
    SFX_0('010_swing_sword_2')
    sprite('Action_442_04', 2)	# 12-13
    GFX_0('EffShotSlash', 100)
    GFX_0('ShotEX', 0)
    sprite('Action_442_05', 6)	# 14-19
    Unknown14072('ShotDashCancel')
    sprite('Action_442_06', 14)	# 20-33
    sprite('Action_442_07', 5)	# 34-38
    sprite('Action_442_08', 5)	# 39-43
    Unknown14074('ShotDashCancel')
    Recovery()
    sprite('Action_442_09', 4)	# 44-47

@State
def Rush_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(500)
        Unknown30065(0)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        PushbackX(0)
        AirPushbackX(-5000)
        AirPushbackY(20000)
        Unknown9016(1)
        Unknown11001(0, 6, 6)
        Hitstop(6)
    sprite('Action_251_00', 1)	# 1-1
    sprite('Action_251_01', 2)	# 2-3
    physicsXImpulse(80000)
    Unknown8006(100, 1, 0)
    tag_voice(1, 'uli209_0', 'uli209_1', 'uli209_2', '')
    sprite('Action_251_02', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_251_03', 2)	# 6-7
    sprite('Action_251_04', 4)	# 8-11	 **attackbox here**
    GFX_0('EffEXRushSlash00', 100)
    GroundedHitstunAnimation(9)
    AirPushbackX(10000)
    AirPushbackY(12000)
    physicsXImpulse(0)
    sprite('Action_251_05', 4)	# 12-15
    sprite('Action_251_06', 4)	# 16-19
    sprite('Action_251_07', 3)	# 20-22
    sprite('Action_251_08', 1)	# 23-23
    GFX_0('EffEXRushSlash01', 100)
    sprite('Action_251_09', 3)	# 24-26	 **attackbox here**
    Hitstop(5)
    GroundedHitstunAnimation(11)
    AirPushbackX(1000)
    AirPushbackY(10000)
    RefreshMultihit()
    sprite('Action_251_10', 7)	# 27-33
    sprite('Action_251_11', 1)	# 34-34
    GFX_0('EffEXRushSlash02', 100)
    sprite('Action_251_12', 2)	# 35-36	 **attackbox here**
    Hitstop(4)
    GroundedHitstunAnimation(9)
    AirPushbackX(1000)
    RefreshMultihit()
    sprite('Action_251_13', 2)	# 37-38
    sprite('Action_251_14', 4)	# 39-42
    sprite('Action_251_15', 2)	# 43-44
    GFX_0('EffEXRushSlash03', 100)
    tag_voice(0, 'uli210_0', 'uli210_1', 'uli210_2', '')
    sprite('Action_251_16', 2)	# 45-46	 **attackbox here**
    Hitstop(3)
    GroundedHitstunAnimation(11)
    AirPushbackX(1000)
    RefreshMultihit()
    sprite('Action_251_17', 3)	# 47-49
    sprite('Action_251_18', 3)	# 50-52
    sprite('Action_251_19', 1)	# 53-53
    GFX_0('EffEXRushSlash04', 100)
    sprite('Action_251_20', 2)	# 54-55	 **attackbox here**
    GroundedHitstunAnimation(9)
    AirPushbackX(1000)
    RefreshMultihit()
    sprite('Action_251_21', 1)	# 56-56
    sprite('Action_251_22', 2)	# 57-58
    sprite('Action_251_23', 1)	# 59-59
    GFX_0('EffEXRushSlash03', 100)
    sprite('Action_251_24', 3)	# 60-62	 **attackbox here**
    GroundedHitstunAnimation(11)
    AirPushbackX(1000)
    AirPushbackY(8000)
    Hitstop(3)
    RefreshMultihit()
    sprite('Action_251_25', 2)	# 63-64
    sprite('Action_251_26', 2)	# 65-66
    sprite('Action_251_27', 5)	# 67-71	 **attackbox here**
    GFX_0('EffEXRushSlash04', 100)
    Hitstop(12)
    GroundedHitstunAnimation(9)
    AirPushbackX(1000)
    AirPushbackY(8000)
    PushbackX(30000)
    RefreshMultihit()
    sprite('Action_251_28', 3)	# 72-74
    sprite('Action_251_29', 2)	# 75-76
    sprite('Action_251_30', 2)	# 77-78
    sprite('Action_251_31', 1)	# 79-79
    sprite('Action_251_32', 1)	# 80-80
    sprite('Action_251_33', 3)	# 81-83
    tag_voice(0, 'uli211_0', 'uli211_1', 'uli211_2', '')
    sprite('Action_251_34', 1)	# 84-84	 **attackbox here**
    GFX_0('EffEXRushSlash05', 100)
    Damage(1000)
    GroundedHitstunAnimation(18)
    AirPushbackX(52000)
    AirPushbackY(23000)
    Unknown9178(1)
    Hitstop(9)
    PushbackX(35000)
    RefreshMultihit()
    sprite('Action_251_35', 6)	# 85-90
    sprite('Action_251_36', 5)	# 91-95
    sprite('Action_251_37', 5)	# 96-100
    sprite('Action_251_38', 3)	# 101-103

@State
def Assault_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(18000)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Hitstop(1)
        Unknown9016(1)
        HitOverhead(2)
        Unknown30065(0)
        Unknown11091(10)
        sendToLabelUpon(2, 1)
    sprite('Action_184_00', 3)	# 1-3
    sprite('Action_184_01', 2)	# 4-5
    Unknown23087(50000)
    physicsXImpulse(36000)
    physicsYImpulse(16000)
    setGravity(2000)
    Unknown8001(0, 100)
    tag_voice(1, 'uli213_0', 'uli213_1', 'uli213_2', '')
    SFX_0('002_highjump_0')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_184_02', 2)	# 6-7
    sprite('Action_184_03', 2)	# 8-9
    sprite('Action_184_04', 2)	# 10-11
    sprite('Action_184_05', 2)	# 12-13
    sprite('Action_184_06', 2)	# 14-15
    sprite('Action_184_07', 2)	# 16-17
    sprite('Action_184_08', 2)	# 18-19
    sprite('Action_184_09', 32767)	# 20-32786
    label(1)
    sprite('Action_184_10', 1)	# 32787-32787	 **attackbox here**
    StartMultihit()
    GFX_0('EffEXAssaultSlash', 100)
    SFX_0('010_swing_sword_2')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown23087(-1)
    sprite('Action_184_10', 1)	# 32788-32788	 **attackbox here**
    RefreshMultihit()
    sprite('Action_184_10', 1)	# 32789-32789	 **attackbox here**
    RefreshMultihit()
    sprite('Action_184_11', 2)	# 32790-32791	 **attackbox here**
    RefreshMultihit()
    sprite('Action_184_11', 2)	# 32792-32793	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    PushbackX(12000)
    sprite('Action_184_12', 6)	# 32794-32799
    Recovery()
    Unknown2063()
    sprite('Action_184_13', 8)	# 32800-32807
    sprite('Action_184_14', 4)	# 32808-32811
    sprite('Action_184_15', 3)	# 32812-32814

@State
def AirShot_EX():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        clearUponHandler(2)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('Action_450_00', 2)	# 1-2
    physicsXImpulse(3000)
    physicsYImpulse(16000)
    setGravity(1400)
    sprite('Action_450_01', 1)	# 3-3
    sprite('Action_450_01', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_450_02', 3)	# 6-8
    sprite('Action_450_03', 3)	# 9-11
    sprite('Action_450_04', 5)	# 12-16
    sprite('Action_450_05', 4)	# 17-20
    SFX_0('010_swing_sword_2')
    sprite('Action_450_06', 3)	# 21-23
    GFX_0('EffAirShotSlash', 100)
    GFX_0('AirShotEX', 0)
    tag_voice(1, 'uli205_0', 'uli205_1', 'uli205_2', '')
    Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_450_07', 10)	# 24-33
    sprite('Action_448_08', 6)	# 34-39
    sprite('Action_448_09', 4)	# 40-43
    Recovery()
    label(0)
    sprite('Action_448_09', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_023_00', 3)	# 48-50
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_023_01', 3)	# 51-53
    sprite('Action_023_02', 3)	# 54-56
    sprite('Action_023_03', 4)	# 57-60

@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(300)
        Unknown11091(15)
        AttackP2(98)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(6000)
        AirPushbackY(3000)
        Unknown30056('a08601003200000000000000')
        YImpluseBeforeWallbounce(700)
        AirUntechableTime(100)
        Unknown9310(1)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        Unknown11056(2)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11057(800)
        Unknown11064(1)
        Unknown1084(1)
        GFX_0('UltimateRushEff', 100)
    sprite('Action_189_00', 5)	# 1-5
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    setInvincible(1)
    Unknown30080('')
    tag_voice(1, 'uli250_0', 'uli250_1', '', '')
    sprite('Action_189_01', 8)	# 6-13
    SFX_3('SE_ApperLightBlade')
    sprite('Action_189_02', 7)	# 14-20
    sprite('Action_189_03', 6)	# 21-26
    sprite('Action_189_04', 5)	# 27-31
    sprite('Action_189_05', 4)	# 32-35
    sprite('Action_189_06', 4)	# 36-39
    sprite('Action_189_07', 4)	# 40-43
    sprite('Action_189_08', 3)	# 44-46
    sprite('Action_189_09', 3)	# 47-49
    Unknown2015(200)
    sprite('Action_190_00', 5)	# 50-54
    sprite('Action_190_01', 5)	# 55-59
    teleportRelativeX(20000)
    sprite('Action_190_02', 4)	# 60-63
    sprite('Action_190_03', 4)	# 64-67
    physicsXImpulse(5000)
    Unknown1028(-50)
    sprite('Action_190_04', 4)	# 68-71
    SFX_3('SE_SwingLightSword')
    SFX_0('010_swing_sword_2')
    sprite('Action_190_05', 4)	# 72-75	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 3)	# 76-78	 **attackbox here**
    sprite('Action_190_07', 3)	# 79-81	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 4)	# 82-85	 **attackbox here**
    sprite('Action_190_09', 2)	# 86-87
    setInvincible(0)
    sprite('Action_190_10', 2)	# 88-89
    sprite('Action_190_11', 2)	# 90-91
    sprite('Action_190_12', 2)	# 92-93
    SFX_3('SE_SwingLightSword')
    SFX_0('010_swing_sword_2')
    sprite('Action_190_13', 2)	# 94-95	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_14', 2)	# 96-97	 **attackbox here**
    sprite('Action_190_15', 2)	# 98-99	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_16', 2)	# 100-101	 **attackbox here**
    sprite('Action_190_10', 2)	# 102-103
    sprite('Action_190_11', 2)	# 104-105
    sprite('Action_190_12', 2)	# 106-107
    SFX_3('SE_SwingLightSword')
    SFX_0('010_swing_sword_2')
    sprite('Action_190_13', 2)	# 108-109	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_14', 2)	# 110-111	 **attackbox here**
    sprite('Action_190_15', 2)	# 112-113	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_16', 2)	# 114-115	 **attackbox here**
    sprite('Action_190_17', 2)	# 116-117
    Unknown1084(1)
    sprite('Action_190_18', 2)	# 118-119
    teleportRelativeX(20000)
    sprite('Action_190_19', 2)	# 120-121
    teleportRelativeX(20000)
    sprite('Action_190_20', 2)	# 122-123
    SFX_3('SE_SwingLightSword')
    SFX_0('010_swing_sword_2')
    teleportRelativeX(20000)
    sprite('Action_190_21', 3)	# 124-126	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    sprite('Action_190_22', 4)	# 127-130	 **attackbox here**
    Unknown1084(1)
    teleportRelativeX(20000)
    sprite('Action_190_23', 6)	# 131-136	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    AirPushbackX(5000)
    AirPushbackY(28000)
    YImpluseBeforeWallbounce(900)
    sprite('Action_190_24', 6)	# 137-142	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_190_25', 7)	# 143-149
    physicsXImpulse(0)
    sprite('Action_190_26', 10)	# 150-159
    tag_voice(0, 'uli251_0', 'uli251_1', '', '')
    sprite('Action_190_27', 2)	# 160-161
    Unknown11057(1000)
    GFX_0('UltimateSlash', 100)
    Unknown2015(-1)
    SFX_3('SE_BigBomb')
    sprite('Action_190_28', 4)	# 162-165	 **attackbox here**
    Unknown11001(0, 0, 0)
    AirPushbackX(25000)
    AirPushbackY(-45000)
    Unknown30055('305705003200000000000000')
    Hitstop(0)
    RefreshMultihit()
    sprite('Action_190_29', 28)	# 166-193
    GFX_0('UltimateLightwall', 0)
    sprite('Action_190_30', 2)	# 194-195
    sprite('Action_190_31', 6)	# 196-201
    sprite('Action_190_32', 3)	# 202-204
    sprite('Action_190_33', 5)	# 205-209
    sprite('Action_190_34', 3)	# 210-212
    sprite('Action_190_35', 6)	# 213-218
    sprite('Action_190_36', 3)	# 219-221
    sprite('Action_190_37', 4)	# 222-225	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    GFX_0('UltimateAssaultFinish', 100)
    AirPushbackX(1000)
    AirPushbackY(20000)
    sprite('Action_190_38', 31)	# 226-256
    sprite('Action_190_39', 4)	# 257-260
    sprite('Action_190_40', 6)	# 261-266
    sprite('Action_190_41', 3)	# 267-269
    sprite('Action_190_42', 3)	# 270-272
    sprite('Action_190_43', 3)	# 273-275

@State
def UltimateRushOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(300)
        Unknown11091(15)
        AttackP2(98)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(4500)
        Unknown30056('a08601003200000000000000')
        YImpluseBeforeWallbounce(700)
        AirUntechableTime(100)
        Unknown9310(1)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        Unknown11056(2)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11057(800)
        Unknown11064(1)
        Unknown1084(1)
        GFX_0('UltimateRushEffOD', 100)
    sprite('Action_189_00', 5)	# 1-5
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    setInvincible(1)
    Unknown30080('')
    tag_voice(1, 'uli250_0', 'uli250_1', '', '')
    sprite('Action_189_01', 8)	# 6-13
    SFX_3('SE_ApperLightBlade')
    sprite('Action_189_02', 7)	# 14-20
    sprite('Action_189_03', 6)	# 21-26
    sprite('Action_189_04', 5)	# 27-31
    sprite('Action_189_05', 4)	# 32-35
    sprite('Action_189_06', 4)	# 36-39
    sprite('Action_189_07', 4)	# 40-43
    sprite('Action_189_08', 3)	# 44-46
    sprite('Action_189_09', 3)	# 47-49
    Unknown2015(200)
    sprite('Action_190_00', 5)	# 50-54
    sprite('Action_190_01', 5)	# 55-59
    teleportRelativeX(20000)
    sprite('Action_190_02', 4)	# 60-63
    sprite('Action_190_03', 4)	# 64-67
    physicsXImpulse(9000)
    Unknown1028(-50)
    sprite('Action_190_04', 4)	# 68-71
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 4)	# 72-75	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 3)	# 76-78	 **attackbox here**
    sprite('Action_190_07', 3)	# 79-81	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 4)	# 82-85	 **attackbox here**
    sprite('Action_190_00', 2)	# 86-87
    setInvincible(0)
    sprite('Action_190_01', 2)	# 88-89
    sprite('Action_190_02', 2)	# 90-91
    sprite('Action_190_03', 2)	# 92-93
    sprite('Action_190_04', 2)	# 94-95
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 96-97	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 98-99	 **attackbox here**
    sprite('Action_190_07', 2)	# 100-101	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 102-103	 **attackbox here**
    sprite('Action_190_01', 2)	# 104-105
    sprite('Action_190_02', 2)	# 106-107
    sprite('Action_190_03', 2)	# 108-109
    sprite('Action_190_04', 2)	# 110-111
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 112-113	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 114-115	 **attackbox here**
    sprite('Action_190_07', 2)	# 116-117	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 118-119	 **attackbox here**
    sprite('Action_190_01', 2)	# 120-121
    sprite('Action_190_02', 2)	# 122-123
    sprite('Action_190_03', 2)	# 124-125
    sprite('Action_190_04', 2)	# 126-127
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 128-129	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 130-131	 **attackbox here**
    sprite('Action_190_07', 2)	# 132-133	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 134-135	 **attackbox here**
    sprite('Action_190_01', 2)	# 136-137
    sprite('Action_190_02', 2)	# 138-139
    sprite('Action_190_03', 2)	# 140-141
    sprite('Action_190_04', 2)	# 142-143
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 144-145	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 146-147	 **attackbox here**
    sprite('Action_190_07', 2)	# 148-149	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 150-151	 **attackbox here**
    sprite('Action_190_09', 2)	# 152-153
    sprite('Action_190_10', 2)	# 154-155
    sprite('Action_190_11', 2)	# 156-157
    sprite('Action_190_12', 2)	# 158-159
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_13', 2)	# 160-161	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_14', 2)	# 162-163	 **attackbox here**
    sprite('Action_190_15', 2)	# 164-165	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_16', 2)	# 166-167	 **attackbox here**
    sprite('Action_190_17', 2)	# 168-169
    Unknown1084(1)
    sprite('Action_190_18', 2)	# 170-171
    teleportRelativeX(20000)
    sprite('Action_190_19', 2)	# 172-173
    teleportRelativeX(20000)
    sprite('Action_190_20', 2)	# 174-175
    SFX_3('SE_SwingLightSword')
    teleportRelativeX(20000)
    sprite('Action_190_21', 3)	# 176-178	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    sprite('Action_190_22', 4)	# 179-182	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_190_23', 6)	# 183-188	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    AirPushbackX(5000)
    AirPushbackY(28000)
    YImpluseBeforeWallbounce(900)
    sprite('Action_190_24', 6)	# 189-194	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_190_25', 7)	# 195-201
    physicsXImpulse(0)
    sprite('Action_190_26', 10)	# 202-211
    tag_voice(0, 'uli251_0', 'uli251_1', '', '')
    sprite('Action_190_27', 2)	# 212-213
    Unknown11057(1000)
    GFX_0('UltimateSlashOD', 100)
    Unknown2015(-1)
    SFX_3('SE_BigBomb')
    sprite('Action_190_28', 4)	# 214-217	 **attackbox here**
    Unknown11001(0, 0, 0)
    AirPushbackX(25000)
    AirPushbackY(-45000)
    Unknown30055('305705003200000000000000')
    Hitstop(0)
    RefreshMultihit()
    sprite('Action_190_29', 38)	# 218-255
    GFX_0('UltimateLightwallOD', 0)
    sprite('Action_190_30', 2)	# 256-257
    sprite('Action_190_31', 6)	# 258-263
    sprite('Action_190_32', 3)	# 264-266
    sprite('Action_190_33', 5)	# 267-271
    sprite('Action_190_34', 3)	# 272-274
    sprite('Action_190_35', 6)	# 275-280
    sprite('Action_190_36', 3)	# 281-283
    sprite('Action_190_37', 4)	# 284-287	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    GFX_0('UltimateAssaultFinish', 100)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(20000)
    sprite('Action_190_38', 31)	# 288-318
    sprite('Action_190_39', 4)	# 319-322
    sprite('Action_190_40', 6)	# 323-328
    sprite('Action_190_41', 3)	# 329-331
    sprite('Action_190_42', 3)	# 332-334
    sprite('Action_190_43', 3)	# 335-337

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown2003(1)
    sprite('Action_262_00', 5)	# 1-5
    sprite('Action_262_01', 5)	# 6-10
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    setInvincible(1)
    Unknown30080('')
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 3)	# 37-39
    sprite('Action_262_03', 3)	# 40-42
    sprite('Action_262_04', 3)	# 43-45
    sprite('Action_262_05', 5)	# 46-50
    sprite('Action_262_06', 5)	# 51-55
    sprite('Action_441_00', 2)	# 56-57
    sprite('Action_441_01', 2)	# 58-59
    sprite('Action_441_02', 2)	# 60-61
    sprite('Action_441_03', 4)	# 62-65
    sprite('Action_441_04', 2)	# 66-67
    SFX_0('006_swing_blade_1')
    GFX_0('EffShotSlash', 100)
    GFX_0('UltimateShot1', 0)
    sprite('Action_441_05', 2)	# 68-69
    sprite('Action_441_06', 2)	# 70-71
    sprite('Action_441_07', 2)	# 72-73
    sprite('Action_145_00', 2)	# 74-75
    sprite('Action_145_01', 2)	# 76-77
    sprite('Action_145_02', 3)	# 78-80	 **attackbox here**
    GFX_0('Lin_432', 100)
    GFX_0('UltimateShot2', 0)
    sprite('Action_145_03', 3)	# 81-83
    sprite('Action_145_04', 12)	# 84-95
    sprite('Action_145_05', 5)	# 96-100
    sprite('Action_145_06', 4)	# 101-104

@State
def UltimateRanbu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Unknown11091(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11069('UltimateRanbu_Exe')
        Unknown11064(1)

        def upon_78():
            Unknown13024(0)
            enterState('UltimateRanbu_Exe')
        setInvincible(1)
        Unknown1084(1)
    sprite('Action_262_00', 5)	# 1-5
    sprite('Action_262_01', 5)	# 6-10
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_4('uli252')
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 3)	# 37-39
    sprite('Action_262_03', 3)	# 40-42
    sprite('Action_262_04', 3)	# 43-45
    sprite('Action_262_03', 3)	# 46-48
    sprite('Action_262_04', 3)	# 49-51
    sprite('Action_262_05', 5)	# 52-56
    sprite('Action_262_06', 5)	# 57-61
    sprite('Action_154_00', 6)	# 62-67
    sprite('Action_154_01', 4)	# 68-71
    Unknown1045(40000)
    sprite('Action_154_02', 4)	# 72-75	 **attackbox here**
    GFX_0('Lin_157', 0)
    Unknown1084(1)
    SFX_0('007_swing_knife_1')
    sprite('Action_154_03', 8)	# 76-83
    setInvincible(0)
    sprite('Action_154_04', 5)	# 84-88
    sprite('Action_154_05', 4)	# 89-92
    sprite('Action_154_06', 3)	# 93-95

@State
def UltimateRanbu_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(750)
        Unknown11091(15)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Hitstop(4)
        Unknown30048(1)
        Unknown11023(1)
        Unknown11072(1, 150000, 50000)
        Unknown9016(1)
        Unknown11069('UltimateRanbu_Exe')
        Unknown11064(1)
        Unknown23027()
        setInvincible(1)
        Unknown2017(0)
        Unknown2015(40)

        def upon_ON_HIT_OR_BLOCK():
            Unknown3001(200)
            Unknown3004(-40)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        Unknown13024(0)
    sprite('keep', 7)	# 1-7
    GFX_0('Lin_166_1', 0)
    Unknown3004(-40)
    sprite('Action_160_07', 6)	# 8-13
    GFX_0('Lin_160_1', 0)
    teleportRelativeX(100000)
    Unknown1007(360000)
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_08', 2)	# 14-15
    sprite('Action_160_09', 4)	# 16-19	 **attackbox here**
    SFX_4('uli253_0')
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(30000)
    AirPushbackY(-18000)
    GFX_0('Lin_091', 0)
    SFX_0('007_swing_knife_1')
    sprite('null', 5)	# 20-24
    GFX_0('Lin_168_1', 0)
    teleportRelativeX(300000)
    teleportRelativeY(0)
    sprite('Action_154_00', 3)	# 25-27
    GFX_0('Lin_160_2', 0)
    Unknown3001(128)
    Unknown3004(20)
    Unknown8000(100, 1, 1)
    sprite('Action_154_01', 2)	# 28-29
    sprite('Action_154_02', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown9071()
    AirPushbackY(40000)
    GFX_0('Lin_157', 0)
    SFX_0('007_swing_knife_1')
    sprite('null', 1)	# 32-32
    GFX_0('Lin_166_3', 0)
    teleportRelativeX(300000)
    Unknown1007(300000)
    Unknown2005()
    Unknown26('Lin_157')
    sprite('Action_160_03', 6)	# 33-38
    GFX_0('Lin_160_3', 0)
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_04', 2)	# 39-40
    sprite('Action_160_05', 4)	# 41-44	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAir5CBlade', 100)
    SFX_0('010_swing_sword_1')
    sprite('null', 5)	# 45-49
    GFX_0('Lin_168_2', 0)
    sprite('Action_160_07', 6)	# 50-55
    GFX_0('Lin_160_4', 0)
    teleportRelativeX(300000)
    Unknown1007(360000)
    Unknown2005()
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_08', 2)	# 56-57
    sprite('Action_160_09', 4)	# 58-61	 **attackbox here**
    GFX_0('Lin_168_3', 0)
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackY(-28000)
    GFX_0('Lin_091', 0)
    SFX_0('007_swing_knife_1')
    sprite('null', 5)	# 62-66
    teleportRelativeX(500000)
    teleportRelativeY(0)
    Unknown2005()
    sprite('Action_160_12', 4)	# 67-70
    GFX_0('Lin_160_5', 0)
    Unknown3001(128)
    Unknown3004(20)
    Unknown8000(100, 1, 1)
    sprite('Action_160_13', 3)	# 71-73
    sprite('Action_160_14', 2)	# 74-75
    sprite('Action_160_15', 6)	# 76-81	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(10000)
    AirPushbackY(30000)
    Hitstop(1)
    Unknown11001(0, 20, 20)
    Unknown11099(1)
    physicsXImpulse(60000)
    Unknown8007(100, 1, 1)
    GFX_0('Lin_169', 0)
    SFX_0('007_swing_knife_2')
    sprite('Action_160_16', 5)	# 82-86
    Unknown3001(128)
    Unknown3004(20)
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('Action_160_15', 1)	# 87-87	 **attackbox here**
    SFX_4('uli254')
    RefreshMultihit()
    Unknown11001(0, 0, 5)
    Unknown11072(0, 150000, 50000)
    Unknown11099(0)
    Unknown11069('')
    clearUponHandler(10)
    Unknown3001(128)
    Unknown3004(20)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('Action_160_15', 1)	# 88-88	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 1)	# 89-89	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 1)	# 90-90	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 1)	# 91-91	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 6)	# 92-97	 **attackbox here**
    RefreshMultihit()
    Unknown11064(0)
    sprite('Action_160_16', 11)	# 98-108
    Unknown1019(20)
    Unknown13024(1)
    sprite('Action_160_17', 6)	# 109-114
    Unknown1084(1)
    sprite('Action_160_18', 5)	# 115-119
    sprite('Action_160_19', 5)	# 120-124
    sprite('Action_160_20', 4)	# 125-128

@State
def UltimateRanbuOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Unknown11091(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11069('UltimateRanbuOD_Exe')
        Unknown11064(1)

        def upon_78():
            Unknown13024(0)
            enterState('UltimateRanbuOD_Exe')
        setInvincible(1)
        Unknown1084(1)
    sprite('Action_262_00', 5)	# 1-5
    sprite('Action_262_01', 5)	# 6-10
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_4('uli252')
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 3)	# 37-39
    sprite('Action_262_03', 3)	# 40-42
    sprite('Action_262_04', 3)	# 43-45
    sprite('Action_262_03', 3)	# 46-48
    sprite('Action_262_04', 3)	# 49-51
    sprite('Action_262_05', 5)	# 52-56
    sprite('Action_262_06', 5)	# 57-61
    sprite('Action_154_00', 6)	# 62-67
    sprite('Action_154_01', 4)	# 68-71
    Unknown1045(40000)
    sprite('Action_154_02', 4)	# 72-75	 **attackbox here**
    GFX_0('Lin_157', 0)
    Unknown1084(1)
    SFX_0('007_swing_knife_1')
    sprite('Action_154_03', 8)	# 76-83
    setInvincible(0)
    sprite('Action_154_04', 5)	# 84-88
    sprite('Action_154_05', 4)	# 89-92
    sprite('Action_154_06', 3)	# 93-95

@State
def UltimateRanbuOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(850)
        Unknown11091(15)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Hitstop(4)
        Unknown30048(1)
        Unknown11023(1)
        Unknown11072(1, 150000, 50000)
        Unknown9016(1)
        Unknown11069('UltimateRanbuOD_Exe')
        Unknown11064(1)
        Unknown23027()
        setInvincible(1)
        Unknown2017(0)
        Unknown2015(40)

        def upon_ON_HIT_OR_BLOCK():
            Unknown3001(200)
            Unknown3004(-40)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        Unknown13024(0)
    sprite('keep', 7)	# 1-7
    GFX_0('Lin_166_1', 0)
    Unknown3004(-40)
    sprite('null', 1)	# 8-8
    teleportRelativeX(300000)
    Unknown1007(300000)
    Unknown2005()
    Unknown26('Lin_157')
    sprite('Action_160_03', 6)	# 9-14
    GFX_0('Lin_160_3', 0)
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_04', 2)	# 15-16
    sprite('Action_160_05', 4)	# 17-20	 **attackbox here**
    SFX_4('uli253_1')
    RefreshMultihit()
    GFX_0('EffNmlAtkAir5CBlade', 100)
    SFX_0('010_swing_sword_1')
    sprite('null', 5)	# 21-25
    GFX_0('Lin_168_2', 0)
    sprite('Action_160_07', 6)	# 26-31
    GFX_0('Lin_160_4', 0)
    teleportRelativeX(300000)
    Unknown1007(360000)
    Unknown2005()
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_08', 2)	# 32-33
    sprite('Action_160_09', 4)	# 34-37	 **attackbox here**
    GFX_0('Lin_168_3', 0)
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackY(-28000)
    GFX_0('Lin_091', 0)
    SFX_0('007_swing_knife_1')
    sprite('null', 5)	# 38-42
    teleportRelativeX(500000)
    teleportRelativeY(0)
    Unknown2005()
    sprite('Action_154_00', 3)	# 43-45
    GFX_0('Lin_160_5', 0)
    Unknown3001(128)
    Unknown3004(20)
    Unknown8000(100, 1, 1)
    sprite('Action_154_01', 2)	# 46-47
    sprite('Action_154_02', 2)	# 48-49	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown9071()
    AirPushbackY(40000)
    GFX_0('Lin_157', 0)
    SFX_0('007_swing_knife_1')
    sprite('null', 1)	# 50-50
    GFX_0('Lin_166_3', 0)
    teleportRelativeX(300000)
    Unknown1007(300000)
    Unknown2005()
    Unknown26('Lin_157')
    sprite('Action_160_03', 6)	# 51-56
    GFX_0('Lin_160_3', 0)
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_04', 2)	# 57-58
    sprite('Action_160_05', 4)	# 59-62	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAir5CBlade', 100)
    SFX_0('010_swing_sword_1')
    sprite('null', 5)	# 63-67
    GFX_0('Lin_166_1', 0)
    sprite('null', 1)	# 68-68
    teleportRelativeX(300000)
    Unknown1007(300000)
    Unknown2005()
    Unknown26('Lin_157')
    sprite('Action_160_03', 6)	# 69-74
    GFX_0('Lin_160_2', 0)
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_04', 2)	# 75-76
    sprite('Action_160_05', 4)	# 77-80	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAir5CBlade', 100)
    SFX_0('010_swing_sword_1')
    sprite('null', 5)	# 81-85
    GFX_0('Lin_166_1', 0)
    sprite('Action_160_07', 6)	# 86-91
    GFX_0('Lin_160_1', 0)
    teleportRelativeX(300000)
    Unknown1007(360000)
    Unknown2005()
    Unknown3001(128)
    Unknown3004(20)
    sprite('Action_160_08', 2)	# 92-93
    sprite('Action_160_09', 4)	# 94-97	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackY(-42000)
    GFX_0('Lin_091', 0)
    SFX_0('007_swing_knife_1')
    sprite('null', 6)	# 98-103
    GFX_0('Lin_168_3', 0)
    teleportRelativeX(500000)
    teleportRelativeY(0)
    Unknown2005()
    sprite('Action_160_12', 4)	# 104-107
    GFX_0('Lin_160_5', 0)
    Unknown3001(128)
    Unknown3004(20)
    Unknown8000(100, 1, 1)
    sprite('Action_160_13', 3)	# 108-110
    sprite('Action_160_14', 2)	# 111-112
    sprite('Action_160_15', 6)	# 113-118	 **attackbox here**
    SFX_4('uli254')
    RefreshMultihit()
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(10000)
    AirPushbackY(30000)
    Hitstop(1)
    Unknown11001(0, 20, 20)
    Unknown11099(1)
    physicsXImpulse(60000)
    Unknown8007(100, 1, 1)
    GFX_0('Lin_169', 0)
    SFX_0('007_swing_knife_2')
    sprite('Action_160_16', 5)	# 119-123
    Unknown3001(128)
    Unknown3004(20)
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('Action_160_15', 1)	# 124-124	 **attackbox here**
    RefreshMultihit()
    Unknown11001(0, 0, 5)
    Unknown11072(0, 150000, 50000)
    Unknown11099(0)
    Unknown11069('')
    Unknown11064(0)
    clearUponHandler(10)
    Unknown3001(128)
    Unknown3004(20)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('Action_160_15', 1)	# 125-125	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 1)	# 126-126	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 1)	# 127-127	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 1)	# 128-128	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_15', 6)	# 129-134	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_16', 11)	# 135-145
    Unknown1019(20)
    Unknown13024(1)
    sprite('Action_160_17', 6)	# 146-151
    Unknown1084(1)
    sprite('Action_160_18', 5)	# 152-156
    sprite('Action_160_19', 5)	# 157-161
    sprite('Action_160_20', 4)	# 162-165

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(2)
        Unknown11064(1)
        Damage(2000)
        Unknown11091(100)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9154(120)
        Unknown11001(0, 0, 0)
        AirUntechableTime(300)
        Hitstop(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11062(1)
        Unknown9016(1)

        def upon_78():
            clearUponHandler(78)
            PushbackX(20000)
            sendToLabel(2)
            Unknown23157(1)
            Unknown2017(0)
            Unknown2053(0)
            Unknown2034(0)
            Unknown20003(1)
            Unknown20004(1)
            Unknown23084(1)
            Unknown23088(1, 1)
        Unknown11086(1)

        def upon_77():
            Unknown21015('41737472616c5f3238395f310000000000000000000000000000000000000000581b000000000000')
            Unknown21015('41737472616c5f3238395f320000000000000000000000000000000000000000581b000000000000')
    sprite('Action_270_00', 3)	# 1-3	 **attackbox here**
    setInvincible(1)
    sprite('Action_270_00', 5)	# 4-8	 **attackbox here**
    Unknown2036(90, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    SFX_4('uli290')
    GFX_0('Astral_CutIn', 100)
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    sprite('Action_270_01', 3)	# 9-11	 **attackbox here**
    sprite('Action_270_02', 2)	# 12-13	 **attackbox here**
    sprite('Action_270_03', 5)	# 14-18	 **attackbox here**
    sprite('Action_270_06', 3)	# 19-21	 **attackbox here**
    sprite('Action_270_07', 3)	# 22-24	 **attackbox here**
    sprite('Action_270_08', 3)	# 25-27	 **attackbox here**
    sprite('Action_270_06', 3)	# 28-30	 **attackbox here**
    sprite('Action_270_07', 3)	# 31-33	 **attackbox here**
    sprite('Action_270_08', 3)	# 34-36	 **attackbox here**
    sprite('Action_270_06', 3)	# 37-39	 **attackbox here**
    sprite('Action_270_07', 3)	# 40-42	 **attackbox here**
    sprite('Action_270_08', 3)	# 43-45	 **attackbox here**
    sprite('Action_270_06', 3)	# 46-48	 **attackbox here**
    sprite('Action_270_07', 3)	# 49-51	 **attackbox here**
    sprite('Action_270_08', 3)	# 52-54	 **attackbox here**
    sprite('Action_270_06', 3)	# 55-57	 **attackbox here**
    sprite('Action_270_07', 3)	# 58-60	 **attackbox here**
    sprite('Action_270_08', 3)	# 61-63	 **attackbox here**
    sprite('Action_270_06', 3)	# 64-66	 **attackbox here**
    sprite('Action_270_07', 3)	# 67-69	 **attackbox here**
    sprite('Action_270_08', 3)	# 70-72	 **attackbox here**
    sprite('Action_270_06', 3)	# 73-75	 **attackbox here**
    sprite('Action_270_07', 3)	# 76-78	 **attackbox here**
    sprite('Action_270_08', 3)	# 79-81	 **attackbox here**
    sprite('Action_270_06', 3)	# 82-84	 **attackbox here**
    sprite('Action_270_07', 3)	# 85-87	 **attackbox here**
    sprite('Action_270_08', 3)	# 88-90	 **attackbox here**
    sprite('Action_270_06', 3)	# 91-93	 **attackbox here**
    sprite('Action_270_07', 3)	# 94-96	 **attackbox here**
    sprite('Action_270_08', 3)	# 97-99	 **attackbox here**
    sprite('Action_270_09', 3)	# 100-102	 **attackbox here**
    loopRest()
    sprite('Action_270_10', 2)	# 103-104	 **attackbox here**
    physicsXImpulse(30000)

    def upon_3():
        if (SLOT_19 <= 200000):
            clearUponHandler(3)
            sendToLabel(1)
    sprite('Action_270_11', 3)	# 105-107	 **attackbox here**
    GFX_0('Astral_289_1', 100)
    GFX_0('Astral_289_2', 100)
    sprite('Action_270_12', 3)	# 108-110	 **attackbox here**
    sprite('Action_270_13', 2)	# 111-112	 **attackbox here**
    sprite('Action_270_14', 2)	# 113-114	 **attackbox here**
    sprite('Action_270_15', 2)	# 115-116	 **attackbox here**
    sprite('Action_270_16', 2)	# 117-118	 **attackbox here**
    sprite('Action_270_17', 2)	# 119-120	 **attackbox here**
    sprite('Action_270_18', 2)	# 121-122	 **attackbox here**
    label(1)
    sprite('Action_270_11ex', 3)	# 123-125	 **attackbox here**
    Unknown21015('41737472616c5f3238395f310000000000000000000000000000000000000000581b000000000000')
    Unknown21015('41737472616c5f3238395f320000000000000000000000000000000000000000581b000000000000')
    clearUponHandler(3)
    Unknown11072(1, 200000, 0)
    sprite('Action_045_11', 4)	# 126-129
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    setInvincible(0)
    Unknown1019(80)
    sprite('Action_045_12', 5)	# 130-134
    sprite('Action_045_11', 4)	# 135-138
    Unknown1019(50)
    sprite('Action_045_12', 5)	# 139-143
    Unknown1019(0)
    sprite('Action_045_13', 6)	# 144-149
    ExitState()
    label(2)
    sprite('Action_270_19', 4)	# 150-153	 **attackbox here**
    SFX_4('uli291')
    physicsXImpulse(6000)
    clearUponHandler(3)
    clearUponHandler(78)
    sprite('Action_270_20', 2)	# 154-155	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    AttackLevel_(4)
    Hitstop(2)
    sprite('Action_270_20', 2)	# 156-157	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    RefreshMultihit()
    sprite('Action_270_21', 5)	# 158-162	 **attackbox here**
    sprite('Action_270_22', 3)	# 163-165	 **attackbox here**
    GFX_0('Astral_280', 100)
    RefreshMultihit()
    sprite('Action_270_23', 2)	# 166-167	 **attackbox here**
    sprite('Action_270_24', 3)	# 168-170	 **attackbox here**
    sprite('Action_270_25', 4)	# 171-174	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    GFX_0('Astral_281', 100)
    RefreshMultihit()
    sprite('Action_270_26', 5)	# 175-179	 **attackbox here**
    sprite('Action_270_27', 3)	# 180-182	 **attackbox here**
    sprite('Action_270_28', 4)	# 183-186	 **attackbox here**
    sprite('Action_270_29', 4)	# 187-190	 **attackbox here**
    sprite('Action_270_30', 1)	# 191-191	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    GFX_0('Astral_282', 100)
    RefreshMultihit()
    sprite('Action_270_31', 4)	# 192-195	 **attackbox here**
    sprite('Action_270_32', 3)	# 196-198	 **attackbox here**
    sprite('Action_270_33', 2)	# 199-200	 **attackbox here**
    sprite('Action_270_34', 5)	# 201-205	 **attackbox here**
    sprite('Action_270_35', 4)	# 206-209	 **attackbox here**
    sprite('Action_270_36', 2)	# 210-211	 **attackbox here**
    sprite('Action_270_37', 5)	# 212-216	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    GFX_0('Astral_283', 100)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirUntechableTime(600)
    AirPushbackX(0)
    AirPushbackY(80000)
    YImpluseBeforeWallbounce(1600)
    RefreshMultihit()
    sprite('Action_270_38', 22)	# 217-238	 **attackbox here**
    Unknown1084(1)
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('null', 45)	# 239-283
    Unknown20000(1)
    Unknown20003(1)
    Unknown20002(1)
    Unknown1000(0)
    Unknown36(22)
    Unknown3001(0)
    Unknown1000(0)
    physicsYImpulse(1)
    setGravity(0)
    Unknown35()
    sprite('null', 45)	# 284-328
    Unknown4004('6566666563745f32363500000000000000000000000000000000000000000000ffff0000')
    SFX_4('uli292')
    sprite('null', 40)	# 329-368
    SFX_3('SE039')
    GFX_0('Astral_277', 100)
    sprite('null', 20)	# 369-388
    Unknown36(22)
    Unknown3001(255)
    Unknown35()
    GFX_0('Astral_276', 100)
    sprite('null', 1)	# 389-389
    Unknown20000(0)
    Unknown20007(1)
    Unknown20001(1)
    sprite('null', 20)	# 390-409
    GFX_0('Astral_274', -1)
    Unknown1086(22)
    teleportRelativeX(-100000)
    Unknown1007(-30000)
    sprite('Action_271_03', 4)	# 410-413	 **attackbox here**
    Unknown3001(0)
    Unknown3004(42)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    physicsXImpulse(1200)
    physicsYImpulse(10000)
    setGravity(100)
    sprite('Action_271_04', 4)	# 414-417	 **attackbox here**
    sprite('Action_271_05', 4)	# 418-421	 **attackbox here**
    sprite('Action_271_06', 4)	# 422-425	 **attackbox here**
    YAccel(80)
    sprite('Action_271_07', 4)	# 426-429	 **attackbox here**
    SFX_4('uli293')
    sprite('Action_271_08', 11)	# 430-440	 **attackbox here**
    sprite('Action_271_09', 10)	# 441-450	 **attackbox here**
    YAccel(50)
    sprite('Action_271_10', 10)	# 451-460	 **attackbox here**
    sprite('Action_271_11', 5)	# 461-465	 **attackbox here**
    YAccel(20)
    setGravity(0)
    sprite('null', 40)	# 466-505
    SFX_3('SE_SwingGlass')
    GFX_0('Astral_272', 100)
    Unknown36(22)
    Unknown3001(0)
    Unknown35()
    Unknown26('Astral_274')
    sprite('null', 20)	# 506-525
    Unknown20007(1)
    Unknown20001(1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('null', 90)	# 526-615
    GFX_0('Astral_279', -1)
    GFX_0('Astral_274_2', -1)
    GFX_0('Astral_278', 100)
    Unknown36(22)
    Unknown3001(255)
    Unknown23178(11)
    setGravity(0)
    Unknown35()
    sprite('null', 30)	# 616-645
    GFX_0('Astral_275', 100)
    SFX_3('SE_BigBomb')
    sprite('null', 30)	# 646-675
    Unknown11064(3)
    GFX_0('Astral_Atk_dmy', 100)
    Unknown26('Astral_274_2')
    sprite('null', 87)	# 676-762
    Unknown26('Astral_278')
    Unknown20007(0)
    Unknown20000(1)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown23024(0)
    sprite('Action_269_00', 122)	# 763-884
    sprite('Action_269_01', 15)	# 885-899
    Unknown20000(0)
    sprite('Action_269_02', 5)	# 900-904
    sprite('Action_269_03', 4)	# 905-908
    sprite('Action_269_04', 5)	# 909-913
    sprite('Action_269_05', 5)	# 914-918
    sprite('Action_269_06', 2)	# 919-920

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
    sprite('Action_248_00', 3)	# 1-3
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    sprite('Action_248_01', 3)	# 4-6
    sprite('Action_248_02', 3)	# 7-9
    sprite('Action_248_03', 3)	# 10-12
    sprite('Action_248_04', 3)	# 13-15
    sprite('Action_248_05', 3)	# 16-18
    sprite('Action_248_06', 3)	# 19-21
    sprite('Action_248_07', 3)	# 22-24
    sprite('Action_248_08', 3)	# 25-27
    sprite('Action_248_09', 3)	# 28-30
    sprite('Action_248_10', 20)	# 31-50
    sprite('Action_248_06', 3)	# 51-53
    sprite('Action_248_05', 3)	# 54-56
    sprite('Action_248_04', 3)	# 57-59
    sprite('Action_248_03', 3)	# 60-62
    sprite('Action_248_02', 3)	# 63-65
    sprite('Action_248_01', 3)	# 66-68
    sprite('Action_248_00', 3)	# 69-71

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
    sprite('Action_019_03', 2)	# 1-2
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('Action_019_02', 2)	# 3-4
    label(0)
    sprite('Action_019_00', 5)	# 5-9
    sprite('Action_019_01', 5)	# 10-14
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
    sprite('Action_019_00', 6)	# 15-20
    sprite('Action_019_01', 6)	# 21-26

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_046_01', 3)	# 1-3
    sprite('Action_046_02', 3)	# 4-6
    sprite('Action_046_01', 3)	# 7-9
    sprite('Action_046_02', 3)	# 10-12
    sprite('Action_046_01', 3)	# 13-15
    sprite('Action_046_02', 3)	# 16-18
    sprite('Action_046_01', 3)	# 19-21
    sprite('Action_046_02', 3)	# 22-24
    sprite('Action_046_01', 3)	# 25-27
    sprite('Action_046_02', 3)	# 28-30
    sprite('Action_046_01', 30)	# 31-60

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17013()
        Unknown1084(1)
        Unknown2034(0)
        Unknown2017(0)
        Unknown2053(0)
        Unknown2067(2500, 240)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2017(1)
            Unknown2053(1)
    sprite('Action_053_00', 3)	# 1-3
    sprite('Action_053_01', 3)	# 4-6
    sprite('Action_053_02', 4)	# 7-10
    sprite('Action_053_03', 4)	# 11-14
    sprite('Action_053_04', 6)	# 15-20
    sprite('Action_053_05', 20)	# 21-40
    sprite('Action_053_06', 2)	# 41-42
    sprite('Action_053_07', 5)	# 43-47
    sprite('Action_053_08', 5)	# 48-52
    sprite('Action_053_09', 10)	# 53-62
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    sprite('keep', 32767)	# 63-32829
    label(2)
    sprite('Action_053_03', 3)	# 32830-32832
    sprite('Action_053_02', 3)	# 32833-32835
    sprite('Action_053_01', 3)	# 32836-32838
    sprite('Action_053_00', 3)	# 32839-32841

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_000_15', 1)	# 1-1	 **attackbox here**
    sprite('Action_000_16', 4)	# 2-5	 **attackbox here**
    sprite('Action_000_17', 4)	# 6-9	 **attackbox here**
    sprite('Action_000_18', 4)	# 10-13	 **attackbox here**
    sprite('Action_000_19', 4)	# 14-17	 **attackbox here**
    sprite('Action_000_20', 4)	# 18-21	 **attackbox here**
    sprite('Action_000_21', 4)	# 22-25	 **attackbox here**
    sprite('Action_000_22', 4)	# 26-29	 **attackbox here**
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('Action_000_23', 3)	# 30-32	 **attackbox here**
    sprite('Action_000_24', 23)	# 33-55	 **attackbox here**
    sprite('Action_000_26', 4)	# 56-59	 **attackbox here**
    sprite('Action_000_27', 4)	# 60-63	 **attackbox here**
    sprite('Action_000_28', 3)	# 64-66	 **attackbox here**
    sprite('Action_000_29', 3)	# 67-69	 **attackbox here**
    sprite('Action_000_30', 3)	# 70-72	 **attackbox here**
    sprite('Action_000_31', 3)	# 73-75	 **attackbox here**
    sprite('Action_000_32', 30)	# 76-105

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('Action_146_01', 2)	# 26-27
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    sprite('Action_146_02', 2)	# 28-29
    SFX_0('004_swing_grap_1_1')
    SFX_0('000_airdash_2')
    label(1)
    sprite('Action_146_03ex', 3)	# 30-32	 **attackbox here**
    sprite('Action_146_04ex', 3)	# 33-35	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 36-38
    Unknown1084(1)
    sprite('Action_146_05', 4)	# 39-42
    Unknown8000(100, 1, 1)
    sprite('Action_146_06', 14)	# 43-56
    sprite('Action_146_07', 4)	# 57-60

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_03', 2)	# 1-2
    sprite('Action_312_04', 2)	# 3-4
    sprite('Action_312_05', 32)	# 5-36
    sprite('Action_312_06', 4)	# 37-40
    sprite('Action_312_07', 4)	# 41-44
    sprite('Action_312_08', 4)	# 45-48
    sprite('Action_014_00', 4)	# 49-52
    sprite('Action_014_01', 4)	# 53-56
    sprite('Action_014_02', 4)	# 57-60
    sprite('Action_000_00', 30)	# 61-90	 **attackbox here**

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_03', 3)	# 1-3
    sprite('Action_045_04', 5)	# 4-8
    sprite('Action_045_11', 7)	# 9-15
    sprite('Action_045_12', 7)	# 16-22
    sprite('Action_045_13', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('Action_046_00', 1)	# 1-1
    sprite('Action_046_01', 2)	# 2-3
    sprite('Action_046_02', 2)	# 4-5
    sprite('Action_046_02', 1)	# 6-6
    sprite('Action_046_03', 1)	# 7-7
    loopRest()
    label(0)
    sprite('Action_046_03', 3)	# 8-10
    sprite('Action_046_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_05', 3)	# 14-16
    sprite('Action_046_06', 3)	# 17-19

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
    sprite('Action_022_00', 4)	# 3-6
    Unknown1019(95)
    sprite('Action_022_01', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('Action_013_00', 2)	# 11-12
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
        Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_036_00', 4)	# 1-4
    sprite('Action_036_01', 4)	# 5-8
    SLOT_12 = SLOT_19
    Unknown1019(3)
    if (SLOT_12 <= 1000):
        SLOT_12 = 1000
    physicsYImpulse(34000)
    sprite('Action_448_00', 2)	# 9-10
    physicsXImpulse(3000)
    physicsYImpulse(20000)
    setGravity(1400)
    sprite('Action_448_01', 3)	# 11-13
    sprite('Action_448_02', 3)	# 14-16
    sprite('Action_448_03', 3)	# 17-19
    sprite('Action_448_04', 10)	# 20-29
    sprite('Action_448_05', 4)	# 30-33
    SFX_0('010_swing_sword_2')
    sprite('Action_448_06', 3)	# 34-36
    GFX_0('EffAirShotSlash', 100)
    GFX_0('ShotAssist', 0)
    tag_voice(1, 'uli204_0', 'uli204_1', 'uli204_2', '')
    sprite('Action_448_07', 10)	# 37-46
    sprite('Action_448_08', 6)	# 47-52
    sprite('Action_448_09', 4)	# 53-56
    label(0)
    sprite('Action_022_00', 3)	# 57-59
    sprite('Action_022_01', 3)	# 60-62
    loopRest()
    gotoLabel(0)

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AttackP1(70)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(38000)
        AirUntechableTime(60)
        Unknown9016(1)
        Hitstop(7)
        Unknown11042(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_099_00', 6)	# 1-6
    physicsXImpulse(40000)
    sprite('Action_099_01', 3)	# 7-9
    physicsXImpulse(11000)
    Unknown7006('uli200_0', 100, 845769845, 828321840, 0, 0, 100, 845769845, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_099_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_099_03', 1)	# 13-13
    SFX_0('010_swing_sword_0')
    physicsYImpulse(23000)
    physicsXImpulse(4000)
    setGravity(1800)
    sprite('Action_099_04', 2)	# 14-15
    GFX_0('EffNmlReversalAction00', 100)
    sprite('Action_099_05', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    Unknown9071()
    Unknown9083()
    sprite('Action_099_06', 3)	# 18-20
    sprite('Action_099_07', 2)	# 21-22
    sprite('Action_099_08', 2)	# 23-24
    sprite('Action_099_09', 2)	# 25-26
    sprite('Action_099_10', 2)	# 27-28
    sprite('Action_099_11', 3)	# 29-31
    sprite('Action_099_12', 4)	# 32-35
    label(0)
    sprite('Action_099_13', 3)	# 36-38
    sprite('Action_099_14', 3)	# 39-41
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_099_15', 2)	# 42-43
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_099_16', 2)	# 44-45
    sprite('Action_099_17', 3)	# 46-48
    sprite('Action_099_18', 3)	# 49-51

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
        Damage(800)
        AttackP1(70)
        Unknown11092(1)
        Hitstop(2)
        AirPushbackX(12000)
        AirPushbackY(32000)
        AirUntechableTime(50)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        Unknown11042(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_045_00', 2)	# 1-2
    Unknown3029(1)
    sprite('Action_045_01', 3)	# 3-5
    physicsXImpulse(38000)
    Unknown1028(-1000)
    sprite('Action_045_02', 2)	# 6-7

    def upon_3():
        if (SLOT_19 <= 200000):
            sendToLabel(0)
    sprite('Action_045_03', 2)	# 8-9
    Unknown8006(100, 1, 1)
    label(0)
    sprite('Action_403_00', 1)	# 10-10
    clearUponHandler(3)
    Unknown1084(1)
    Unknown1045(28000)
    sprite('Action_403_01', 1)	# 11-11
    sprite('Action_403_02', 2)	# 12-13
    sprite('Action_403_03', 1)	# 14-14
    Unknown7009(2)
    SFX_0('010_swing_sword_2')
    sprite('Action_403_03', 1)	# 15-15
    sprite('Action_403_04', 1)	# 16-16	 **attackbox here**
    GFX_0('EffNmlAtk5CBlade', 100)
    RefreshMultihit()
    Unknown1019(80)
    sprite('Action_403_04', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_05', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    Hitstop(7)
    Unknown1019(80)
    sprite('Action_403_06', 4)	# 20-23
    sprite('Action_403_07', 7)	# 24-30
    sprite('Action_403_08', 4)	# 31-34
    sprite('Action_403_09', 4)	# 35-38
    sprite('Action_403_10', 3)	# 39-41
    sprite('Action_403_11', 1)	# 42-42
    sprite('Action_403_11', 1)	# 43-43
    sprite('Action_403_11', 1)	# 44-44

@State
def CmnActChangePartnerAttackIn():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerDD():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown30063(1)
        if SLOT_162:
            SLOT_58 = 1

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
    sprite('null', 1)	# 1-1
    Unknown2036(96, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('Action_022_00', 3)	# 3-5
    sprite('Action_022_01', 3)	# 6-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 9-18
    if SLOT_58:
        enterState('AN_CmnActChangePartnerDDODExe')
    else:
        enterState('AN_CmnActChangePartnerDDExe')

@State
def AN_CmnActChangePartnerDDExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(150)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(6000)
        AirPushbackY(3000)
        Unknown30056('a08601003200000000000000')
        YImpluseBeforeWallbounce(700)
        AirUntechableTime(100)
        Unknown9310(1)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        Unknown11056(2)
        Unknown11064(1)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11057(800)
        Unknown1084(1)
        Unknown30063(1)
        Unknown30019('0000000001000000')
        GFX_0('UltimateRushEff', 100)
    sprite('Lin392_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_189_01', 8)	# 6-13
    SFX_3('SE_ApperLightBlade')
    sprite('Action_189_02', 7)	# 14-20
    sprite('Action_189_03', 6)	# 21-26
    sprite('Action_189_04', 5)	# 27-31
    sprite('Action_189_05', 4)	# 32-35
    sprite('Action_189_06', 4)	# 36-39
    sprite('Action_189_07', 4)	# 40-43
    sprite('Action_189_08', 3)	# 44-46
    sprite('Action_189_09', 3)	# 47-49
    Unknown2015(200)
    sprite('Action_190_00', 5)	# 50-54
    sprite('Action_190_01', 5)	# 55-59
    teleportRelativeX(20000)
    sprite('Action_190_02', 4)	# 60-63
    sprite('Action_190_03', 4)	# 64-67
    physicsXImpulse(5000)
    Unknown1028(-50)
    sprite('Action_190_04', 4)	# 68-71
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05duo', 4)	# 72-75	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 3)	# 76-78	 **attackbox here**
    sprite('Action_190_07', 3)	# 79-81	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 4)	# 82-85	 **attackbox here**
    sprite('Action_190_09', 2)	# 86-87
    setInvincible(0)
    sprite('Action_190_10', 2)	# 88-89
    sprite('Action_190_11', 2)	# 90-91
    sprite('Action_190_12', 2)	# 92-93
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_13', 2)	# 94-95	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_14', 2)	# 96-97	 **attackbox here**
    sprite('Action_190_15', 2)	# 98-99	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_16', 2)	# 100-101	 **attackbox here**
    sprite('Action_190_10', 2)	# 102-103
    sprite('Action_190_11', 2)	# 104-105
    sprite('Action_190_12', 2)	# 106-107
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_13', 2)	# 108-109	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_14', 2)	# 110-111	 **attackbox here**
    sprite('Action_190_15', 2)	# 112-113	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_16', 2)	# 114-115	 **attackbox here**
    sprite('Action_190_17', 2)	# 116-117
    Unknown1084(1)
    sprite('Action_190_18', 2)	# 118-119
    teleportRelativeX(20000)
    sprite('Action_190_19', 2)	# 120-121
    teleportRelativeX(20000)
    sprite('Action_190_20', 2)	# 122-123
    SFX_3('SE_SwingLightSword')
    teleportRelativeX(20000)
    sprite('Action_190_21', 3)	# 124-126	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    SFX_0('010_swing_sword_2')
    sprite('Action_190_22', 4)	# 127-130	 **attackbox here**
    Unknown1084(1)
    teleportRelativeX(20000)
    sprite('Action_190_23', 6)	# 131-136	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    AirPushbackX(5000)
    AirPushbackY(28000)
    YImpluseBeforeWallbounce(900)
    sprite('Action_190_24', 6)	# 137-142	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_190_25', 7)	# 143-149
    physicsXImpulse(0)
    sprite('Action_190_26', 10)	# 150-159
    tag_voice(0, 'uli251_0', 'uli251_1', '', '')
    sprite('Action_190_27', 2)	# 160-161
    Unknown11057(1000)
    GFX_0('UltimateSlash', 100)
    Unknown2015(-1)
    SFX_3('SE_BigBomb')
    sprite('Action_190_28', 4)	# 162-165	 **attackbox here**
    Unknown11001(0, 0, 0)
    AirPushbackX(25000)
    AirPushbackY(-45000)
    Unknown30055('305705003200000000000000')
    Hitstop(0)
    Damage(170)
    RefreshMultihit()
    sprite('Action_190_29', 28)	# 166-193
    GFX_0('UltimateLightwallDDD', 0)
    sprite('Action_190_30', 2)	# 194-195
    sprite('Action_190_31', 6)	# 196-201
    sprite('Action_190_32', 3)	# 202-204
    sprite('Action_190_33', 5)	# 205-209
    sprite('Action_190_34', 3)	# 210-212
    sprite('Action_190_35', 6)	# 213-218
    Unknown21012('556c74696d6174654c6967687477616c6c45666600000000000000000000000029000000')
    sprite('Action_190_36', 3)	# 219-221
    sprite('Action_190_37', 4)	# 222-225	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    GFX_0('UltimateAssaultFinish', 100)
    AirPushbackX(1000)
    AirPushbackY(20000)
    sprite('Action_190_38', 31)	# 226-256
    sprite('Action_190_39', 4)	# 257-260
    sprite('Action_190_40', 6)	# 261-266
    sprite('Action_190_41', 3)	# 267-269
    sprite('Action_190_42', 3)	# 270-272
    sprite('Action_190_43', 3)	# 273-275

@State
def AN_CmnActChangePartnerDDODExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(100)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(4500)
        Unknown30056('a08601003200000000000000')
        YImpluseBeforeWallbounce(700)
        AirUntechableTime(100)
        Unknown9310(1)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        Unknown11056(2)
        Unknown11064(1)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11057(800)
        Unknown1084(1)
        Unknown30063(1)
        GFX_0('UltimateRushEffOD', 100)
    sprite('Lin392_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_189_01', 8)	# 6-13
    SFX_3('SE_ApperLightBlade')
    sprite('Action_189_02', 7)	# 14-20
    sprite('Action_189_03', 6)	# 21-26
    sprite('Action_189_04', 5)	# 27-31
    sprite('Action_189_05', 4)	# 32-35
    sprite('Action_189_06', 4)	# 36-39
    sprite('Action_189_07', 4)	# 40-43
    sprite('Action_189_08', 3)	# 44-46
    sprite('Action_189_09', 3)	# 47-49
    Unknown2015(200)
    sprite('Action_190_00', 5)	# 50-54
    sprite('Action_190_01', 5)	# 55-59
    teleportRelativeX(20000)
    sprite('Action_190_02', 4)	# 60-63
    sprite('Action_190_03', 4)	# 64-67
    sprite('Action_190_04', 4)	# 68-71
    physicsXImpulse(5000)
    Unknown1028(-50)
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05duo', 4)	# 72-75	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 3)	# 76-78	 **attackbox here**
    sprite('Action_190_07', 3)	# 79-81	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 4)	# 82-85	 **attackbox here**
    sprite('Action_190_00', 2)	# 86-87
    setInvincible(0)
    sprite('Action_190_01', 2)	# 88-89
    sprite('Action_190_02', 2)	# 90-91
    sprite('Action_190_03', 2)	# 92-93
    sprite('Action_190_04', 2)	# 94-95
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 96-97	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 98-99	 **attackbox here**
    sprite('Action_190_07', 2)	# 100-101	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 102-103	 **attackbox here**
    sprite('Action_190_01', 2)	# 104-105
    sprite('Action_190_02', 2)	# 106-107
    sprite('Action_190_03', 2)	# 108-109
    sprite('Action_190_04', 2)	# 110-111
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 112-113	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 114-115	 **attackbox here**
    sprite('Action_190_07', 2)	# 116-117	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 118-119	 **attackbox here**
    sprite('Action_190_01', 2)	# 120-121
    sprite('Action_190_02', 2)	# 122-123
    sprite('Action_190_03', 2)	# 124-125
    sprite('Action_190_04', 2)	# 126-127
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 128-129	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 130-131	 **attackbox here**
    sprite('Action_190_07', 2)	# 132-133	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 134-135	 **attackbox here**
    sprite('Action_190_01', 2)	# 136-137
    sprite('Action_190_02', 2)	# 138-139
    sprite('Action_190_03', 2)	# 140-141
    sprite('Action_190_04', 2)	# 142-143
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_05', 2)	# 144-145	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_06', 2)	# 146-147	 **attackbox here**
    sprite('Action_190_07', 2)	# 148-149	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_08', 2)	# 150-151	 **attackbox here**
    sprite('Action_190_09', 2)	# 152-153
    sprite('Action_190_10', 2)	# 154-155
    sprite('Action_190_11', 2)	# 156-157
    sprite('Action_190_12', 2)	# 158-159
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_13', 2)	# 160-161	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_14', 2)	# 162-163	 **attackbox here**
    sprite('Action_190_15', 2)	# 164-165	 **attackbox here**
    RefreshMultihit()
    sprite('Action_190_16', 2)	# 166-167	 **attackbox here**
    sprite('Action_190_17', 2)	# 168-169
    Unknown1084(1)
    sprite('Action_190_18', 2)	# 170-171
    teleportRelativeX(20000)
    sprite('Action_190_19', 2)	# 172-173
    teleportRelativeX(20000)
    sprite('Action_190_20', 2)	# 174-175
    teleportRelativeX(20000)
    SFX_3('SE_SwingLightSword')
    sprite('Action_190_21', 3)	# 176-178	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    sprite('Action_190_22', 4)	# 179-182	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_190_23', 6)	# 183-188	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    AirPushbackX(5000)
    AirPushbackY(28000)
    YImpluseBeforeWallbounce(900)
    sprite('Action_190_24', 6)	# 189-194	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_190_25', 7)	# 195-201
    physicsXImpulse(0)
    sprite('Action_190_26', 10)	# 202-211
    tag_voice(0, 'uli251_0', 'uli251_1', '', '')
    sprite('Action_190_27', 2)	# 212-213
    Unknown11057(1000)
    GFX_0('UltimateSlashOD', 100)
    SFX_3('SE_BigBomb')
    Unknown2015(-1)
    sprite('Action_190_28', 4)	# 214-217	 **attackbox here**
    Unknown11001(0, 0, 0)
    AirPushbackX(25000)
    AirPushbackY(-45000)
    Unknown30055('305705003200000000000000')
    Hitstop(0)
    RefreshMultihit()
    sprite('Action_190_29', 38)	# 218-255
    GFX_0('UltimateLightwallDDDOD', 0)
    sprite('Action_190_30', 2)	# 256-257
    sprite('Action_190_31', 6)	# 258-263
    sprite('Action_190_32', 3)	# 264-266
    sprite('Action_190_33', 5)	# 267-271
    sprite('Action_190_34', 3)	# 272-274
    sprite('Action_190_35', 6)	# 275-280
    sprite('Action_190_36', 3)	# 281-283
    sprite('Action_190_37', 4)	# 284-287	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    GFX_0('UltimateAssaultFinish', 100)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(20000)
    sprite('Action_190_38', 36)	# 288-323
    Unknown21012('556c74696d6174654c6967687477616c6c4566664f440000000000000000000029000000')
    sprite('Action_190_39', 4)	# 324-327
    sprite('Action_190_40', 6)	# 328-333
    sprite('Action_190_41', 4)	# 334-337
    sprite('Action_190_42', 4)	# 338-341
    sprite('Action_190_43', 3)	# 342-344

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
    sprite('null', 5)	# 121-125
    sprite('Action_146_01', 6)	# 126-131
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-96000)
    setGravity(0)
    Unknown2053(1)
    sprite('Action_146_02', 3)	# 132-134
    SFX_0('004_swing_grap_1_1')
    SFX_0('000_airdash_2')
    label(1)
    sprite('Action_146_03ex', 3)	# 135-137	 **attackbox here**
    sprite('Action_146_04ex', 3)	# 138-140	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 141-143
    Unknown1084(1)
    sprite('Action_146_05', 5)	# 144-148
    Unknown8000(100, 1, 1)
    sprite('Action_146_06', 18)	# 149-166
    sprite('Action_146_07', 5)	# 167-171

@Subroutine
def MouthTableInit():
    Unknown18011('uli000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli500', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli501', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli502', 12643, 14177, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli504', 12643, 14177, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli523', 12643, 14177, 12643, 24880, 25399, 24887, 12337, 14179, 14177, 14179, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli525', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli403_0', 12643, 14177, 14179, 14177, 12643, 24882, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli601bes', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli600bha', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli601bpt', 12643, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli600brc', 12643, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli600pla', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli601pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli601uhy', 12643, 14177, 13411, 24887, 25399, 13105, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli600umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli601uor', 12643, 12641, 25396, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli600uva', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli601uwa', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli701bes', 12643, 12641, 25392, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli701bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli700bpt', 12643, 12641, 25394, 12341, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli701brc', 12643, 12641, 25392, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli700pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli701pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli700uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli700umi', 12643, 14177, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli701uor', 12643, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli700uva', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli701uwa', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uli703pyo', 12643, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uor')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('uva')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    sprite('Action_050_02', 5)	# 2-6	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        if random_(2, 0, 50):
            Unknown7006('uli500', 100, 896101493, 12592, 0, 0, 100, 896101493, 12848, 0, 0, 100, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uli503', 100, 896101493, 13360, 0, 0, 100, 896101493, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_050_03', 5)	# 7-11	 **attackbox here**
    sprite('Action_050_04', 5)	# 12-16	 **attackbox here**
    label(1)
    sprite('Action_050_02', 5)	# 17-21	 **attackbox here**
    sprite('Action_050_03', 5)	# 22-26	 **attackbox here**
    sprite('Action_050_04', 5)	# 27-31	 **attackbox here**
    if SLOT_97:
        _gotolabel(1)
    sprite('Action_050_05', 7)	# 32-38
    sprite('Action_050_06', 9)	# 39-47
    sprite('Action_050_07', 4)	# 48-51
    sprite('Action_050_08', 5)	# 52-56
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 57-64
    sprite('Action_050_10', 7)	# 65-71
    sprite('Action_050_11', 6)	# 72-77	 **attackbox here**
    sprite('Action_050_12', 5)	# 78-82	 **attackbox here**
    sprite('Action_050_13', 5)	# 83-87	 **attackbox here**
    Unknown23018(1)
    sprite('Action_050_14', 20)	# 88-107	 **attackbox here**
    sprite('Action_050_15', 5)	# 108-112
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 113-116
    sprite('Action_050_17', 5)	# 117-121
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 122-126
    sprite('Action_050_19', 2)	# 127-128
    loopRest()
    ExitState()
    label(10)
    sprite('Action_000_25', 32767)	# 129-32895	 **attackbox here**
    SFX_1('uli700umi')
    label(100)
    sprite('Action_000_15', 7)	# 32896-32902	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown23029(11, 9902, 0)
    sprite('Action_000_16', 4)	# 32903-32906	 **attackbox here**
    SFX_1('uli600brc')
    sprite('Action_000_17', 7)	# 32907-32913	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('Action_000_18', 5)	# 32914-32918	 **attackbox here**
    sprite('Action_000_19', 8)	# 32919-32926	 **attackbox here**
    sprite('Action_000_20', 10)	# 32927-32936	 **attackbox here**
    sprite('Action_000_21', 5)	# 32937-32941	 **attackbox here**
    sprite('Action_000_22', 7)	# 32942-32948	 **attackbox here**
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('Action_000_23', 3)	# 32949-32951	 **attackbox here**
    sprite('Action_000_24', 20)	# 32952-32971	 **attackbox here**
    label(101)
    sprite('Action_000_25', 1)	# 32972-32972	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_000_25', 30)	# 32973-33002	 **attackbox here**
    sprite('Action_000_26', 5)	# 33003-33007	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_27', 8)	# 33008-33015	 **attackbox here**
    sprite('Action_000_28', 6)	# 33016-33021	 **attackbox here**
    sprite('Action_000_29', 4)	# 33022-33025	 **attackbox here**
    sprite('Action_000_30', 4)	# 33026-33029	 **attackbox here**
    SFX_0('008_swing_pole_0')
    sprite('Action_000_31', 6)	# 33030-33035	 **attackbox here**
    sprite('Action_000_32', 7)	# 33036-33042
    Unknown21011(240)
    label(102)
    sprite('Action_000_00', 7)	# 33043-33049	 **attackbox here**
    sprite('Action_000_01', 7)	# 33050-33056	 **attackbox here**
    sprite('Action_000_02', 6)	# 33057-33062	 **attackbox here**
    sprite('Action_000_03', 6)	# 33063-33068	 **attackbox here**
    sprite('Action_000_04', 8)	# 33069-33076	 **attackbox here**
    sprite('Action_000_05', 5)	# 33077-33081	 **attackbox here**
    sprite('Action_000_06', 5)	# 33082-33086	 **attackbox here**
    sprite('Action_000_07', 5)	# 33087-33091	 **attackbox here**
    sprite('Action_000_08', 6)	# 33092-33097	 **attackbox here**
    sprite('Action_000_09', 5)	# 33098-33102	 **attackbox here**
    sprite('Action_000_10', 6)	# 33103-33108	 **attackbox here**
    sprite('Action_000_11', 8)	# 33109-33116	 **attackbox here**
    sprite('Action_000_12', 5)	# 33117-33121	 **attackbox here**
    sprite('Action_000_13', 5)	# 33122-33126	 **attackbox here**
    sprite('Action_000_14', 6)	# 33127-33132	 **attackbox here**
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('Action_050_02', 5)	# 33133-33137	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('uli600bha')
    sprite('Action_050_03', 5)	# 33138-33142	 **attackbox here**
    sprite('Action_050_04', 5)	# 33143-33147	 **attackbox here**
    label(111)
    sprite('Action_050_02', 5)	# 33148-33152	 **attackbox here**
    sprite('Action_050_03', 5)	# 33153-33157	 **attackbox here**
    sprite('Action_050_04', 5)	# 33158-33162	 **attackbox here**
    if SLOT_97:
        _gotolabel(111)
    sprite('Action_050_05', 7)	# 33163-33169
    sprite('Action_050_06', 9)	# 33170-33178
    sprite('Action_050_07', 4)	# 33179-33182
    sprite('Action_050_08', 5)	# 33183-33187
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 33188-33195
    sprite('Action_050_10', 7)	# 33196-33202
    sprite('Action_050_11', 6)	# 33203-33208	 **attackbox here**
    sprite('Action_050_12', 5)	# 33209-33213	 **attackbox here**
    sprite('Action_050_13', 5)	# 33214-33218	 **attackbox here**
    sprite('Action_050_14', 20)	# 33219-33238	 **attackbox here**
    sprite('Action_050_15', 5)	# 33239-33243
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 33244-33247
    sprite('Action_050_17', 5)	# 33248-33252
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 33253-33257
    Unknown21007(24, 40)
    sprite('Action_050_19', 2)	# 33258-33259
    Unknown21011(420)
    label(112)
    sprite('Action_000_00', 7)	# 33260-33266	 **attackbox here**
    sprite('Action_000_01', 7)	# 33267-33273	 **attackbox here**
    sprite('Action_000_02', 6)	# 33274-33279	 **attackbox here**
    sprite('Action_000_03', 6)	# 33280-33285	 **attackbox here**
    sprite('Action_000_04', 8)	# 33286-33293	 **attackbox here**
    sprite('Action_000_05', 5)	# 33294-33298	 **attackbox here**
    sprite('Action_000_06', 5)	# 33299-33303	 **attackbox here**
    sprite('Action_000_07', 5)	# 33304-33308	 **attackbox here**
    sprite('Action_000_08', 6)	# 33309-33314	 **attackbox here**
    sprite('Action_000_09', 5)	# 33315-33319	 **attackbox here**
    sprite('Action_000_10', 6)	# 33320-33325	 **attackbox here**
    sprite('Action_000_11', 8)	# 33326-33333	 **attackbox here**
    sprite('Action_000_12', 5)	# 33334-33338	 **attackbox here**
    sprite('Action_000_13', 5)	# 33339-33343	 **attackbox here**
    sprite('Action_000_14', 6)	# 33344-33349	 **attackbox here**
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('Action_050_02', 1)	# 33350-33350	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
        SFX_1('uli601bpt')
    label(121)
    sprite('Action_050_02', 5)	# 33351-33355	 **attackbox here**
    sprite('Action_050_03', 5)	# 33356-33360	 **attackbox here**
    sprite('Action_050_04', 5)	# 33361-33365	 **attackbox here**
    gotoLabel(121)
    label(122)
    sprite('Action_050_02', 5)	# 33366-33370	 **attackbox here**
    sprite('Action_050_03', 5)	# 33371-33375	 **attackbox here**
    sprite('Action_050_04', 5)	# 33376-33380	 **attackbox here**
    if SLOT_97:
        _gotolabel(122)
    sprite('Action_050_05', 7)	# 33381-33387
    sprite('Action_050_06', 9)	# 33388-33396
    sprite('Action_050_07', 4)	# 33397-33400
    sprite('Action_050_08', 5)	# 33401-33405
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 33406-33413
    sprite('Action_050_10', 7)	# 33414-33420
    sprite('Action_050_11', 6)	# 33421-33426	 **attackbox here**
    sprite('Action_050_12', 5)	# 33427-33431	 **attackbox here**
    sprite('Action_050_13', 5)	# 33432-33436	 **attackbox here**
    sprite('Action_050_14', 20)	# 33437-33456	 **attackbox here**
    sprite('Action_050_15', 5)	# 33457-33461
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 33462-33465
    sprite('Action_050_17', 5)	# 33466-33470
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 33471-33475
    sprite('Action_050_19', 2)	# 33476-33477
    Unknown21011(120)
    label(123)
    sprite('Action_000_00', 7)	# 33478-33484	 **attackbox here**
    sprite('Action_000_01', 7)	# 33485-33491	 **attackbox here**
    sprite('Action_000_02', 6)	# 33492-33497	 **attackbox here**
    sprite('Action_000_03', 6)	# 33498-33503	 **attackbox here**
    sprite('Action_000_04', 8)	# 33504-33511	 **attackbox here**
    sprite('Action_000_05', 5)	# 33512-33516	 **attackbox here**
    sprite('Action_000_06', 5)	# 33517-33521	 **attackbox here**
    sprite('Action_000_07', 5)	# 33522-33526	 **attackbox here**
    sprite('Action_000_08', 6)	# 33527-33532	 **attackbox here**
    sprite('Action_000_09', 5)	# 33533-33537	 **attackbox here**
    sprite('Action_000_10', 6)	# 33538-33543	 **attackbox here**
    sprite('Action_000_11', 8)	# 33544-33551	 **attackbox here**
    sprite('Action_000_12', 5)	# 33552-33556	 **attackbox here**
    sprite('Action_000_13', 5)	# 33557-33561	 **attackbox here**
    sprite('Action_000_14', 6)	# 33562-33567	 **attackbox here**
    gotoLabel(123)
    ExitState()
    label(130)
    sprite('Action_000_00', 1)	# 33568-33568	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('Action_000_00', 7)	# 33569-33575	 **attackbox here**
    sprite('Action_000_01', 7)	# 33576-33582	 **attackbox here**
    sprite('Action_000_02', 6)	# 33583-33588	 **attackbox here**
    sprite('Action_000_03', 6)	# 33589-33594	 **attackbox here**
    sprite('Action_000_04', 8)	# 33595-33602	 **attackbox here**
    sprite('Action_000_05', 5)	# 33603-33607	 **attackbox here**
    sprite('Action_000_06', 5)	# 33608-33612	 **attackbox here**
    sprite('Action_000_07', 5)	# 33613-33617	 **attackbox here**
    sprite('Action_000_08', 6)	# 33618-33623	 **attackbox here**
    sprite('Action_000_09', 5)	# 33624-33628	 **attackbox here**
    sprite('Action_000_10', 6)	# 33629-33634	 **attackbox here**
    sprite('Action_000_11', 8)	# 33635-33642	 **attackbox here**
    sprite('Action_000_12', 5)	# 33643-33647	 **attackbox here**
    sprite('Action_000_13', 5)	# 33648-33652	 **attackbox here**
    sprite('Action_000_14', 6)	# 33653-33658	 **attackbox here**
    gotoLabel(131)
    label(132)
    sprite('Action_000_15', 7)	# 33659-33665	 **attackbox here**
    sprite('Action_000_16', 4)	# 33666-33669	 **attackbox here**
    SFX_1('uli601bes')
    sprite('Action_000_17', 7)	# 33670-33676	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('Action_000_18', 5)	# 33677-33681	 **attackbox here**
    sprite('Action_000_19', 8)	# 33682-33689	 **attackbox here**
    sprite('Action_000_20', 10)	# 33690-33699	 **attackbox here**
    sprite('Action_000_21', 5)	# 33700-33704	 **attackbox here**
    sprite('Action_000_22', 7)	# 33705-33711	 **attackbox here**
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('Action_000_23', 3)	# 33712-33714	 **attackbox here**
    sprite('Action_000_24', 20)	# 33715-33734	 **attackbox here**
    label(133)
    sprite('Action_000_25', 1)	# 33735-33735	 **attackbox here**
    if SLOT_97:
        _gotolabel(133)
    sprite('Action_000_25', 30)	# 33736-33765	 **attackbox here**
    sprite('Action_000_26', 5)	# 33766-33770	 **attackbox here**
    sprite('Action_000_27', 8)	# 33771-33778	 **attackbox here**
    sprite('Action_000_28', 6)	# 33779-33784	 **attackbox here**
    sprite('Action_000_29', 4)	# 33785-33788	 **attackbox here**
    sprite('Action_000_30', 4)	# 33789-33792	 **attackbox here**
    SFX_0('008_swing_pole_0')
    sprite('Action_000_31', 6)	# 33793-33798	 **attackbox here**
    sprite('Action_000_32', 7)	# 33799-33805
    Unknown21011(120)
    label(134)
    sprite('Action_000_00', 7)	# 33806-33812	 **attackbox here**
    sprite('Action_000_01', 7)	# 33813-33819	 **attackbox here**
    sprite('Action_000_02', 6)	# 33820-33825	 **attackbox here**
    sprite('Action_000_03', 6)	# 33826-33831	 **attackbox here**
    sprite('Action_000_04', 8)	# 33832-33839	 **attackbox here**
    sprite('Action_000_05', 5)	# 33840-33844	 **attackbox here**
    sprite('Action_000_06', 5)	# 33845-33849	 **attackbox here**
    sprite('Action_000_07', 5)	# 33850-33854	 **attackbox here**
    sprite('Action_000_08', 6)	# 33855-33860	 **attackbox here**
    sprite('Action_000_09', 5)	# 33861-33865	 **attackbox here**
    sprite('Action_000_10', 6)	# 33866-33871	 **attackbox here**
    sprite('Action_000_11', 8)	# 33872-33879	 **attackbox here**
    sprite('Action_000_12', 5)	# 33880-33884	 **attackbox here**
    sprite('Action_000_13', 5)	# 33885-33889	 **attackbox here**
    sprite('Action_000_14', 6)	# 33890-33895	 **attackbox here**
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('Action_050_02', 1)	# 33896-33896	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
        SFX_1('uli601pyo')
    label(141)
    sprite('Action_050_02', 5)	# 33897-33901	 **attackbox here**
    sprite('Action_050_03', 5)	# 33902-33906	 **attackbox here**
    sprite('Action_050_04', 5)	# 33907-33911	 **attackbox here**
    gotoLabel(141)
    label(142)
    sprite('Action_050_02', 5)	# 33912-33916	 **attackbox here**
    sprite('Action_050_03', 5)	# 33917-33921	 **attackbox here**
    sprite('Action_050_04', 5)	# 33922-33926	 **attackbox here**
    if SLOT_97:
        _gotolabel(142)
    sprite('Action_050_05', 7)	# 33927-33933
    sprite('Action_050_06', 9)	# 33934-33942
    sprite('Action_050_07', 4)	# 33943-33946
    sprite('Action_050_08', 5)	# 33947-33951
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 33952-33959
    sprite('Action_050_10', 7)	# 33960-33966
    sprite('Action_050_11', 6)	# 33967-33972	 **attackbox here**
    sprite('Action_050_12', 5)	# 33973-33977	 **attackbox here**
    sprite('Action_050_13', 5)	# 33978-33982	 **attackbox here**
    sprite('Action_050_14', 20)	# 33983-34002	 **attackbox here**
    sprite('Action_050_15', 5)	# 34003-34007
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 34008-34011
    sprite('Action_050_17', 5)	# 34012-34016
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 34017-34021
    sprite('Action_050_19', 2)	# 34022-34023
    Unknown21011(60)
    label(143)
    sprite('Action_000_00', 7)	# 34024-34030	 **attackbox here**
    sprite('Action_000_01', 7)	# 34031-34037	 **attackbox here**
    sprite('Action_000_02', 6)	# 34038-34043	 **attackbox here**
    sprite('Action_000_03', 6)	# 34044-34049	 **attackbox here**
    sprite('Action_000_04', 8)	# 34050-34057	 **attackbox here**
    sprite('Action_000_05', 5)	# 34058-34062	 **attackbox here**
    sprite('Action_000_06', 5)	# 34063-34067	 **attackbox here**
    sprite('Action_000_07', 5)	# 34068-34072	 **attackbox here**
    sprite('Action_000_08', 6)	# 34073-34078	 **attackbox here**
    sprite('Action_000_09', 5)	# 34079-34083	 **attackbox here**
    sprite('Action_000_10', 6)	# 34084-34089	 **attackbox here**
    sprite('Action_000_11', 8)	# 34090-34097	 **attackbox here**
    sprite('Action_000_12', 5)	# 34098-34102	 **attackbox here**
    sprite('Action_000_13', 5)	# 34103-34107	 **attackbox here**
    sprite('Action_000_14', 6)	# 34108-34113	 **attackbox here**
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('Action_050_02', 1)	# 34114-34114	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-1000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
        SFX_1('uli601uhy')
    label(151)
    sprite('Action_050_02', 5)	# 34115-34119	 **attackbox here**
    sprite('Action_050_03', 5)	# 34120-34124	 **attackbox here**
    sprite('Action_050_04', 5)	# 34125-34129	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('Action_050_02', 5)	# 34130-34134	 **attackbox here**
    sprite('Action_050_03', 5)	# 34135-34139	 **attackbox here**
    sprite('Action_050_04', 5)	# 34140-34144	 **attackbox here**
    if SLOT_97:
        _gotolabel(152)
    sprite('Action_050_05', 7)	# 34145-34151
    sprite('Action_050_06', 9)	# 34152-34160
    sprite('Action_050_07', 4)	# 34161-34164
    sprite('Action_050_08', 5)	# 34165-34169
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 34170-34177
    sprite('Action_050_10', 7)	# 34178-34184
    sprite('Action_050_11', 6)	# 34185-34190	 **attackbox here**
    sprite('Action_050_12', 5)	# 34191-34195	 **attackbox here**
    sprite('Action_050_13', 5)	# 34196-34200	 **attackbox here**
    sprite('Action_050_14', 20)	# 34201-34220	 **attackbox here**
    sprite('Action_050_15', 5)	# 34221-34225
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 34226-34229
    sprite('Action_050_17', 5)	# 34230-34234
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 34235-34239
    sprite('Action_050_19', 2)	# 34240-34241
    Unknown21011(120)
    label(153)
    sprite('Action_000_00', 7)	# 34242-34248	 **attackbox here**
    sprite('Action_000_01', 7)	# 34249-34255	 **attackbox here**
    sprite('Action_000_02', 6)	# 34256-34261	 **attackbox here**
    sprite('Action_000_03', 6)	# 34262-34267	 **attackbox here**
    sprite('Action_000_04', 8)	# 34268-34275	 **attackbox here**
    sprite('Action_000_05', 5)	# 34276-34280	 **attackbox here**
    sprite('Action_000_06', 5)	# 34281-34285	 **attackbox here**
    sprite('Action_000_07', 5)	# 34286-34290	 **attackbox here**
    sprite('Action_000_08', 6)	# 34291-34296	 **attackbox here**
    sprite('Action_000_09', 5)	# 34297-34301	 **attackbox here**
    sprite('Action_000_10', 6)	# 34302-34307	 **attackbox here**
    sprite('Action_000_11', 8)	# 34308-34315	 **attackbox here**
    sprite('Action_000_12', 5)	# 34316-34320	 **attackbox here**
    sprite('Action_000_13', 5)	# 34321-34325	 **attackbox here**
    sprite('Action_000_14', 6)	# 34326-34331	 **attackbox here**
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('Lin637_00', 32767)	# 34332-67098	 **attackbox here**
    Unknown23029(11, 9902, 0)
    Unknown1000(-1150000)
    teleportRelativeY(240000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(161)
        SFX_1('uli601uwa')
    label(161)
    sprite('Lin637_00', 1)	# 67099-67099	 **attackbox here**
    if SLOT_97:
        _gotolabel(161)
    sprite('Lin637_01', 6)	# 67100-67105
    sprite('Action_035_05', 6)	# 67106-67111
    physicsYImpulse(-1000)
    setGravity(1000)
    Unknown21007(24, 40)
    sendToLabelUpon(2, 163)
    sprite('Action_035_06', 6)	# 67112-67117
    label(162)
    sprite('Action_022_00', 3)	# 67118-67120
    sprite('Action_022_01', 3)	# 67121-67123
    gotoLabel(162)
    label(163)
    sprite('Action_023_00', 3)	# 67124-67126
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_023_01', 3)	# 67127-67129
    sprite('Action_023_02', 3)	# 67130-67132
    Unknown21011(120)
    label(164)
    sprite('Action_000_00', 7)	# 67133-67139	 **attackbox here**
    sprite('Action_000_01', 7)	# 67140-67146	 **attackbox here**
    sprite('Action_000_02', 6)	# 67147-67152	 **attackbox here**
    sprite('Action_000_03', 6)	# 67153-67158	 **attackbox here**
    sprite('Action_000_04', 8)	# 67159-67166	 **attackbox here**
    sprite('Action_000_05', 5)	# 67167-67171	 **attackbox here**
    sprite('Action_000_06', 5)	# 67172-67176	 **attackbox here**
    sprite('Action_000_07', 5)	# 67177-67181	 **attackbox here**
    sprite('Action_000_08', 6)	# 67182-67187	 **attackbox here**
    sprite('Action_000_09', 5)	# 67188-67192	 **attackbox here**
    sprite('Action_000_10', 6)	# 67193-67198	 **attackbox here**
    sprite('Action_000_11', 8)	# 67199-67206	 **attackbox here**
    sprite('Action_000_12', 5)	# 67207-67211	 **attackbox here**
    sprite('Action_000_13', 5)	# 67212-67216	 **attackbox here**
    sprite('Action_000_14', 6)	# 67217-67222	 **attackbox here**
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('Action_050_02', 1)	# 67223-67223	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
        SFX_1('uli601uor')
    label(171)
    sprite('Action_050_02', 5)	# 67224-67228	 **attackbox here**
    sprite('Action_050_03', 5)	# 67229-67233	 **attackbox here**
    sprite('Action_050_04', 5)	# 67234-67238	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_050_02', 5)	# 67239-67243	 **attackbox here**
    sprite('Action_050_03', 5)	# 67244-67248	 **attackbox here**
    sprite('Action_050_04', 5)	# 67249-67253	 **attackbox here**
    if SLOT_97:
        _gotolabel(172)
    sprite('Action_050_05', 7)	# 67254-67260
    sprite('Action_050_06', 9)	# 67261-67269
    sprite('Action_050_07', 4)	# 67270-67273
    sprite('Action_050_08', 5)	# 67274-67278
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 67279-67286
    sprite('Action_050_10', 7)	# 67287-67293
    sprite('Action_050_11', 6)	# 67294-67299	 **attackbox here**
    sprite('Action_050_12', 5)	# 67300-67304	 **attackbox here**
    sprite('Action_050_13', 5)	# 67305-67309	 **attackbox here**
    sprite('Action_050_14', 20)	# 67310-67329	 **attackbox here**
    sprite('Action_050_15', 5)	# 67330-67334
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 67335-67338
    sprite('Action_050_17', 5)	# 67339-67343
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 67344-67348
    sprite('Action_050_19', 2)	# 67349-67350
    Unknown21011(120)
    label(173)
    sprite('Action_000_00', 7)	# 67351-67357	 **attackbox here**
    sprite('Action_000_01', 7)	# 67358-67364	 **attackbox here**
    sprite('Action_000_02', 6)	# 67365-67370	 **attackbox here**
    sprite('Action_000_03', 6)	# 67371-67376	 **attackbox here**
    sprite('Action_000_04', 8)	# 67377-67384	 **attackbox here**
    sprite('Action_000_05', 5)	# 67385-67389	 **attackbox here**
    sprite('Action_000_06', 5)	# 67390-67394	 **attackbox here**
    sprite('Action_000_07', 5)	# 67395-67399	 **attackbox here**
    sprite('Action_000_08', 6)	# 67400-67405	 **attackbox here**
    sprite('Action_000_09', 5)	# 67406-67410	 **attackbox here**
    sprite('Action_000_10', 6)	# 67411-67416	 **attackbox here**
    sprite('Action_000_11', 8)	# 67417-67424	 **attackbox here**
    sprite('Action_000_12', 5)	# 67425-67429	 **attackbox here**
    sprite('Action_000_13', 5)	# 67430-67434	 **attackbox here**
    sprite('Action_000_14', 6)	# 67435-67440	 **attackbox here**
    gotoLabel(173)
    ExitState()
    label(180)
    sprite('Action_050_02', 5)	# 67441-67445	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_03', 5)	# 67446-67450	 **attackbox here**
    SFX_1('uli600uva')
    sprite('Action_050_04', 5)	# 67451-67455	 **attackbox here**
    label(181)
    sprite('Action_050_02', 5)	# 67456-67460	 **attackbox here**
    sprite('Action_050_03', 5)	# 67461-67465	 **attackbox here**
    sprite('Action_050_04', 5)	# 67466-67470	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_050_05', 7)	# 67471-67477
    sprite('Action_050_06', 9)	# 67478-67486
    sprite('Action_050_07', 4)	# 67487-67490
    sprite('Action_050_08', 5)	# 67491-67495
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 67496-67503
    sprite('Action_050_10', 7)	# 67504-67510
    sprite('Action_050_11', 6)	# 67511-67516	 **attackbox here**
    sprite('Action_050_12', 5)	# 67517-67521	 **attackbox here**
    sprite('Action_050_13', 5)	# 67522-67526	 **attackbox here**
    sprite('Action_050_14', 20)	# 67527-67546	 **attackbox here**
    sprite('Action_050_15', 5)	# 67547-67551
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 67552-67555
    sprite('Action_050_17', 5)	# 67556-67560
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 67561-67565
    Unknown21007(24, 40)
    sprite('Action_050_19', 2)	# 67566-67567
    Unknown21011(300)
    label(182)
    sprite('Action_000_00', 7)	# 67568-67574	 **attackbox here**
    sprite('Action_000_01', 7)	# 67575-67581	 **attackbox here**
    sprite('Action_000_02', 6)	# 67582-67587	 **attackbox here**
    sprite('Action_000_03', 6)	# 67588-67593	 **attackbox here**
    sprite('Action_000_04', 8)	# 67594-67601	 **attackbox here**
    sprite('Action_000_05', 5)	# 67602-67606	 **attackbox here**
    sprite('Action_000_06', 5)	# 67607-67611	 **attackbox here**
    sprite('Action_000_07', 5)	# 67612-67616	 **attackbox here**
    sprite('Action_000_08', 6)	# 67617-67622	 **attackbox here**
    sprite('Action_000_09', 5)	# 67623-67627	 **attackbox here**
    sprite('Action_000_10', 6)	# 67628-67633	 **attackbox here**
    sprite('Action_000_11', 8)	# 67634-67641	 **attackbox here**
    sprite('Action_000_12', 5)	# 67642-67646	 **attackbox here**
    sprite('Action_000_13', 5)	# 67647-67651	 **attackbox here**
    sprite('Action_000_14', 6)	# 67652-67657	 **attackbox here**
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('Action_050_02', 5)	# 67658-67662	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_03', 5)	# 67663-67667	 **attackbox here**
    SFX_1('uli600pla')
    sprite('Action_050_04', 5)	# 67668-67672	 **attackbox here**
    label(191)
    sprite('Action_050_02', 5)	# 67673-67677	 **attackbox here**
    sprite('Action_050_03', 5)	# 67678-67682	 **attackbox here**
    sprite('Action_050_04', 5)	# 67683-67687	 **attackbox here**
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_050_05', 7)	# 67688-67694
    sprite('Action_050_06', 9)	# 67695-67703
    sprite('Action_050_07', 4)	# 67704-67707
    sprite('Action_050_08', 5)	# 67708-67712
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 67713-67720
    Unknown21007(24, 40)
    sprite('Action_050_10', 7)	# 67721-67727
    sprite('Action_050_11', 6)	# 67728-67733	 **attackbox here**
    sprite('Action_050_12', 5)	# 67734-67738	 **attackbox here**
    sprite('Action_050_13', 5)	# 67739-67743	 **attackbox here**
    sprite('Action_050_14', 20)	# 67744-67763	 **attackbox here**
    sprite('Action_050_15', 5)	# 67764-67768
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 67769-67772
    sprite('Action_050_17', 5)	# 67773-67777
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 67778-67782
    sprite('Action_050_19', 2)	# 67783-67784
    Unknown21011(240)
    label(192)
    sprite('Action_000_00', 7)	# 67785-67791	 **attackbox here**
    sprite('Action_000_01', 7)	# 67792-67798	 **attackbox here**
    sprite('Action_000_02', 6)	# 67799-67804	 **attackbox here**
    sprite('Action_000_03', 6)	# 67805-67810	 **attackbox here**
    sprite('Action_000_04', 8)	# 67811-67818	 **attackbox here**
    sprite('Action_000_05', 5)	# 67819-67823	 **attackbox here**
    sprite('Action_000_06', 5)	# 67824-67828	 **attackbox here**
    sprite('Action_000_07', 5)	# 67829-67833	 **attackbox here**
    sprite('Action_000_08', 6)	# 67834-67839	 **attackbox here**
    sprite('Action_000_09', 5)	# 67840-67844	 **attackbox here**
    sprite('Action_000_10', 6)	# 67845-67850	 **attackbox here**
    sprite('Action_000_11', 8)	# 67851-67858	 **attackbox here**
    sprite('Action_000_12', 5)	# 67859-67863	 **attackbox here**
    sprite('Action_000_13', 5)	# 67864-67868	 **attackbox here**
    sprite('Action_000_14', 6)	# 67869-67874	 **attackbox here**
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('Action_050_02', 5)	# 67875-67879	 **attackbox here**
    Unknown23029(11, 9902, 0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_03', 5)	# 67880-67884	 **attackbox here**
    SFX_1('uli600umi')
    sprite('Action_050_04', 5)	# 67885-67889	 **attackbox here**
    label(201)
    sprite('Action_050_02', 5)	# 67890-67894	 **attackbox here**
    sprite('Action_050_03', 5)	# 67895-67899	 **attackbox here**
    sprite('Action_050_04', 5)	# 67900-67904	 **attackbox here**
    if SLOT_97:
        _gotolabel(201)
    sprite('Action_050_05', 7)	# 67905-67911
    sprite('Action_050_06', 9)	# 67912-67920
    sprite('Action_050_07', 4)	# 67921-67924
    sprite('Action_050_08', 5)	# 67925-67929
    SFX_0('019_cloth_a')
    sprite('Action_050_09', 8)	# 67930-67937
    Unknown21007(24, 40)
    Unknown21011(300)
    sprite('Action_050_10', 7)	# 67938-67944
    sprite('Action_050_11', 6)	# 67945-67950	 **attackbox here**
    sprite('Action_050_12', 5)	# 67951-67955	 **attackbox here**
    sprite('Action_050_13', 5)	# 67956-67960	 **attackbox here**
    sprite('Action_050_14', 20)	# 67961-67980	 **attackbox here**
    sprite('Action_050_15', 5)	# 67981-67985
    SFX_0('019_cloth_c')
    sprite('Action_050_16', 4)	# 67986-67989
    sprite('Action_050_17', 5)	# 67990-67994
    SFX_3('SE010')
    sprite('Action_050_18', 5)	# 67995-67999
    sprite('Action_050_19', 2)	# 68000-68001
    label(202)
    sprite('Action_000_00', 7)	# 68002-68008	 **attackbox here**
    sprite('Action_000_01', 7)	# 68009-68015	 **attackbox here**
    sprite('Action_000_02', 6)	# 68016-68021	 **attackbox here**
    sprite('Action_000_03', 6)	# 68022-68027	 **attackbox here**
    sprite('Action_000_04', 8)	# 68028-68035	 **attackbox here**
    sprite('Action_000_05', 5)	# 68036-68040	 **attackbox here**
    sprite('Action_000_06', 5)	# 68041-68045	 **attackbox here**
    sprite('Action_000_07', 5)	# 68046-68050	 **attackbox here**
    sprite('Action_000_08', 6)	# 68051-68056	 **attackbox here**
    sprite('Action_000_09', 5)	# 68057-68061	 **attackbox here**
    sprite('Action_000_10', 6)	# 68062-68067	 **attackbox here**
    sprite('Action_000_11', 8)	# 68068-68075	 **attackbox here**
    sprite('Action_000_12', 5)	# 68076-68080	 **attackbox here**
    sprite('Action_000_13', 5)	# 68081-68085	 **attackbox here**
    sprite('Action_000_14', 6)	# 68086-68091	 **attackbox here**
    gotoLabel(202)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 68092-68092	 **attackbox here**
    Unknown23029(11, 9902, 0)
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 7)	# 68093-68099	 **attackbox here**
    sprite('Action_000_01', 7)	# 68100-68106	 **attackbox here**
    sprite('Action_000_02', 6)	# 68107-68112	 **attackbox here**
    sprite('Action_000_03', 6)	# 68113-68118	 **attackbox here**
    sprite('Action_000_04', 8)	# 68119-68126	 **attackbox here**
    sprite('Action_000_05', 5)	# 68127-68131	 **attackbox here**
    sprite('Action_000_06', 5)	# 68132-68136	 **attackbox here**
    sprite('Action_000_07', 5)	# 68137-68141	 **attackbox here**
    sprite('Action_000_08', 6)	# 68142-68147	 **attackbox here**
    sprite('Action_000_09', 5)	# 68148-68152	 **attackbox here**
    sprite('Action_000_10', 6)	# 68153-68158	 **attackbox here**
    sprite('Action_000_11', 8)	# 68159-68166	 **attackbox here**
    sprite('Action_000_12', 5)	# 68167-68171	 **attackbox here**
    sprite('Action_000_13', 5)	# 68172-68176	 **attackbox here**
    sprite('Action_000_14', 6)	# 68177-68182	 **attackbox here**
    gotoLabel(992)
    label(993)
    sprite('Action_046_00', 2)	# 68183-68184

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
    sprite('Action_046_01', 2)	# 68185-68186
    label(994)
    sprite('Action_046_03', 3)	# 68187-68189
    sprite('Action_046_04', 3)	# 68190-68192
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 68193-68195
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
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    sprite('Action_052_00', 6)	# 4-9
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uli524', 100, 896101493, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uli402_0', 100, 879324277, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uli520', 100, 896101493, 12594, 0, 0, 100, 896101493, 12850, 0, 0, 100, 896101493, 13106, 0, 0, 100)
    sprite('Action_052_01', 6)	# 10-15
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 16-19
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 20-26
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 27-29
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 30-39
    sprite('Action_052_06', 6)	# 40-45
    sprite('Action_052_07', 5)	# 46-50
    Unknown23018(1)
    sprite('Action_052_08', 7)	# 51-57	 **attackbox here**
    label(1000)
    sprite('Action_052_09', 30)	# 58-87	 **attackbox here**
    loopRest()
    gotoLabel(1000)
    label(100)
    sprite('Action_000_00', 1)	# 88-88	 **attackbox here**
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Action_000_00', 7)	# 89-95	 **attackbox here**
    sprite('Action_000_01', 7)	# 96-102	 **attackbox here**
    sprite('Action_000_02', 6)	# 103-108	 **attackbox here**
    sprite('Action_000_03', 6)	# 109-114	 **attackbox here**
    sprite('Action_000_04', 8)	# 115-122	 **attackbox here**
    sprite('Action_000_05', 5)	# 123-127	 **attackbox here**
    sprite('Action_000_06', 5)	# 128-132	 **attackbox here**
    sprite('Action_000_07', 5)	# 133-137	 **attackbox here**
    sprite('Action_000_08', 6)	# 138-143	 **attackbox here**
    sprite('Action_000_09', 5)	# 144-148	 **attackbox here**
    sprite('Action_000_10', 6)	# 149-154	 **attackbox here**
    sprite('Action_000_11', 8)	# 155-162	 **attackbox here**
    sprite('Action_000_12', 5)	# 163-167	 **attackbox here**
    sprite('Action_000_13', 5)	# 168-172	 **attackbox here**
    sprite('Action_000_14', 6)	# 173-178	 **attackbox here**
    gotoLabel(101)
    label(102)
    sprite('Action_052_00', 6)	# 179-184
    SFX_1('uli701brc')
    sprite('Action_052_01', 6)	# 185-190
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 191-194
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 195-201
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 202-204
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 205-214
    sprite('Action_052_06', 6)	# 215-220
    sprite('Action_052_07', 5)	# 221-225
    sprite('Action_052_08', 7)	# 226-232	 **attackbox here**
    label(103)
    sprite('Action_052_09', 1)	# 233-233	 **attackbox here**
    if SLOT_97:
        _gotolabel(103)
    sprite('Action_052_09', 32767)	# 234-33000	 **attackbox here**
    Unknown18008()
    label(110)
    sprite('Action_000_00', 1)	# 33001-33001	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_00', 7)	# 33002-33008	 **attackbox here**
    sprite('Action_000_01', 7)	# 33009-33015	 **attackbox here**
    sprite('Action_000_02', 6)	# 33016-33021	 **attackbox here**
    sprite('Action_000_03', 6)	# 33022-33027	 **attackbox here**
    sprite('Action_000_04', 8)	# 33028-33035	 **attackbox here**
    sprite('Action_000_05', 5)	# 33036-33040	 **attackbox here**
    sprite('Action_000_06', 5)	# 33041-33045	 **attackbox here**
    sprite('Action_000_07', 5)	# 33046-33050	 **attackbox here**
    sprite('Action_000_08', 6)	# 33051-33056	 **attackbox here**
    sprite('Action_000_09', 5)	# 33057-33061	 **attackbox here**
    sprite('Action_000_10', 6)	# 33062-33067	 **attackbox here**
    sprite('Action_000_11', 8)	# 33068-33075	 **attackbox here**
    sprite('Action_000_12', 5)	# 33076-33080	 **attackbox here**
    sprite('Action_000_13', 5)	# 33081-33085	 **attackbox here**
    sprite('Action_000_14', 6)	# 33086-33091	 **attackbox here**
    gotoLabel(111)
    label(112)
    sprite('Action_052_00', 6)	# 33092-33097
    SFX_1('uli701bha')
    sprite('Action_052_01', 6)	# 33098-33103
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 33104-33107
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 33108-33114
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 33115-33117
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 33118-33127
    sprite('Action_052_06', 6)	# 33128-33133
    sprite('Action_052_07', 5)	# 33134-33138
    sprite('Action_052_08', 7)	# 33139-33145	 **attackbox here**
    Unknown23018(1)
    sprite('Action_052_09', 32767)	# 33146-65912	 **attackbox here**
    label(120)
    sprite('Action_052_00', 6)	# 65913-65918
    SFX_1('uli700bpt')
    sprite('Action_052_01', 6)	# 65919-65924
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 65925-65928
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 65929-65935
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 65936-65938
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 65939-65948
    sprite('Action_052_06', 6)	# 65949-65954
    sprite('Action_052_07', 5)	# 65955-65959
    sprite('Action_052_08', 7)	# 65960-65966	 **attackbox here**
    label(121)
    sprite('Action_052_09', 1)	# 65967-65967	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_052_09', 45)	# 65968-66012	 **attackbox here**
    sprite('Action_052_09', 32767)	# 66013-98779	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(280)
    label(130)
    sprite('Action_000_00', 1)	# 98780-98780	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('Action_000_00', 7)	# 98781-98787	 **attackbox here**
    sprite('Action_000_01', 7)	# 98788-98794	 **attackbox here**
    sprite('Action_000_02', 6)	# 98795-98800	 **attackbox here**
    sprite('Action_000_03', 6)	# 98801-98806	 **attackbox here**
    sprite('Action_000_04', 8)	# 98807-98814	 **attackbox here**
    sprite('Action_000_05', 5)	# 98815-98819	 **attackbox here**
    sprite('Action_000_06', 5)	# 98820-98824	 **attackbox here**
    sprite('Action_000_07', 5)	# 98825-98829	 **attackbox here**
    sprite('Action_000_08', 6)	# 98830-98835	 **attackbox here**
    sprite('Action_000_09', 5)	# 98836-98840	 **attackbox here**
    sprite('Action_000_10', 6)	# 98841-98846	 **attackbox here**
    sprite('Action_000_11', 8)	# 98847-98854	 **attackbox here**
    sprite('Action_000_12', 5)	# 98855-98859	 **attackbox here**
    sprite('Action_000_13', 5)	# 98860-98864	 **attackbox here**
    sprite('Action_000_14', 6)	# 98865-98870	 **attackbox here**
    gotoLabel(131)
    label(132)
    sprite('Action_052_00', 6)	# 98871-98876
    SFX_1('uli701bes')
    sprite('Action_052_01', 6)	# 98877-98882
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 98883-98886
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 98887-98893
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 98894-98896
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 98897-98906
    sprite('Action_052_06', 6)	# 98907-98912
    sprite('Action_052_07', 5)	# 98913-98917
    sprite('Action_052_08', 7)	# 98918-98924	 **attackbox here**
    label(133)
    sprite('Action_052_09', 1)	# 98925-98925	 **attackbox here**
    if SLOT_97:
        _gotolabel(133)
    sprite('Action_052_09', 32767)	# 98926-131692	 **attackbox here**
    Unknown21011(120)
    label(140)
    sprite('Action_000_00', 1)	# 131693-131693	 **attackbox here**
    Unknown2034(0)
    Unknown2053(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('Action_000_00', 7)	# 131694-131700	 **attackbox here**
    sprite('Action_000_01', 7)	# 131701-131707	 **attackbox here**
    sprite('Action_000_02', 6)	# 131708-131713	 **attackbox here**
    sprite('Action_000_03', 6)	# 131714-131719	 **attackbox here**
    sprite('Action_000_04', 8)	# 131720-131727	 **attackbox here**
    sprite('Action_000_05', 5)	# 131728-131732	 **attackbox here**
    sprite('Action_000_06', 5)	# 131733-131737	 **attackbox here**
    sprite('Action_000_07', 5)	# 131738-131742	 **attackbox here**
    sprite('Action_000_08', 6)	# 131743-131748	 **attackbox here**
    sprite('Action_000_09', 5)	# 131749-131753	 **attackbox here**
    sprite('Action_000_10', 6)	# 131754-131759	 **attackbox here**
    sprite('Action_000_11', 8)	# 131760-131767	 **attackbox here**
    sprite('Action_000_12', 5)	# 131768-131772	 **attackbox here**
    sprite('Action_000_13', 5)	# 131773-131777	 **attackbox here**
    sprite('Action_000_14', 6)	# 131778-131783	 **attackbox here**
    gotoLabel(141)
    label(142)
    sprite('Action_052_00', 6)	# 131784-131789
    sprite('Action_052_01', 6)	# 131790-131795
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 131796-131799
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 131800-131806
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 131807-131809
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 131810-131819
    sprite('Action_052_06', 6)	# 131820-131825
    sprite('Action_052_07', 5)	# 131826-131830
    sprite('Action_052_08', 7)	# 131831-131837	 **attackbox here**
    SFX_1('uli701pyo')
    label(143)
    sprite('Action_052_09', 1)	# 131838-131838	 **attackbox here**
    if SLOT_97:
        _gotolabel(143)
    sprite('Action_052_09', 30)	# 131839-131868	 **attackbox here**
    sprite('Action_052_09', 32767)	# 131869-164635	 **attackbox here**
    Unknown21007(24, 40)

    def upon_39():
        clearUponHandler(39)
        SFX_1('uli703pyo')
        Unknown21011(80)
    label(150)
    sprite('Action_052_00', 6)	# 164636-164641
    SFX_1('uli700uhy')
    sprite('Action_052_01', 6)	# 164642-164647
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 164648-164651
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 164652-164658
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 164659-164661
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 164662-164671
    sprite('Action_052_06', 6)	# 164672-164677
    sprite('Action_052_07', 5)	# 164678-164682
    sprite('Action_052_08', 7)	# 164683-164689	 **attackbox here**
    label(151)
    sprite('Action_052_09', 1)	# 164690-164690	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('Action_052_09', 30)	# 164691-164720	 **attackbox here**
    sprite('Action_052_09', 32767)	# 164721-197487	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(160)
    sprite('Action_000_00', 1)	# 197488-197488	 **attackbox here**
    Unknown2019(-100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 7)	# 197489-197495	 **attackbox here**
    sprite('Action_000_01', 7)	# 197496-197502	 **attackbox here**
    sprite('Action_000_02', 6)	# 197503-197508	 **attackbox here**
    sprite('Action_000_03', 6)	# 197509-197514	 **attackbox here**
    sprite('Action_000_04', 8)	# 197515-197522	 **attackbox here**
    sprite('Action_000_05', 5)	# 197523-197527	 **attackbox here**
    sprite('Action_000_06', 5)	# 197528-197532	 **attackbox here**
    sprite('Action_000_07', 5)	# 197533-197537	 **attackbox here**
    sprite('Action_000_08', 6)	# 197538-197543	 **attackbox here**
    sprite('Action_000_09', 5)	# 197544-197548	 **attackbox here**
    sprite('Action_000_10', 6)	# 197549-197554	 **attackbox here**
    sprite('Action_000_11', 8)	# 197555-197562	 **attackbox here**
    sprite('Action_000_12', 5)	# 197563-197567	 **attackbox here**
    sprite('Action_000_13', 5)	# 197568-197572	 **attackbox here**
    sprite('Action_000_14', 6)	# 197573-197578	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('Action_052_00', 6)	# 197579-197584
    SFX_1('uli701uwa')
    sprite('Action_052_01', 6)	# 197585-197590
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 197591-197594
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 197595-197601
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 197602-197604
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 197605-197614
    sprite('Action_052_06', 6)	# 197615-197620
    sprite('Action_052_07', 5)	# 197621-197625
    sprite('Action_052_08', 7)	# 197626-197632	 **attackbox here**
    label(163)
    sprite('Action_052_09', 1)	# 197633-197633	 **attackbox here**
    if SLOT_97:
        _gotolabel(163)
    sprite('Action_052_09', 32767)	# 197634-230400	 **attackbox here**
    Unknown21011(120)
    label(170)
    sprite('Action_000_00', 1)	# 230401-230401	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_000_00', 7)	# 230402-230408	 **attackbox here**
    sprite('Action_000_01', 7)	# 230409-230415	 **attackbox here**
    sprite('Action_000_02', 6)	# 230416-230421	 **attackbox here**
    sprite('Action_000_03', 6)	# 230422-230427	 **attackbox here**
    sprite('Action_000_04', 8)	# 230428-230435	 **attackbox here**
    sprite('Action_000_05', 5)	# 230436-230440	 **attackbox here**
    sprite('Action_000_06', 5)	# 230441-230445	 **attackbox here**
    sprite('Action_000_07', 5)	# 230446-230450	 **attackbox here**
    sprite('Action_000_08', 6)	# 230451-230456	 **attackbox here**
    sprite('Action_000_09', 5)	# 230457-230461	 **attackbox here**
    sprite('Action_000_10', 6)	# 230462-230467	 **attackbox here**
    sprite('Action_000_11', 8)	# 230468-230475	 **attackbox here**
    sprite('Action_000_12', 5)	# 230476-230480	 **attackbox here**
    sprite('Action_000_13', 5)	# 230481-230485	 **attackbox here**
    sprite('Action_000_14', 6)	# 230486-230491	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_052_00', 6)	# 230492-230497
    SFX_1('uli701uor')
    sprite('Action_052_01', 6)	# 230498-230503
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 230504-230507
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 230508-230514
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 230515-230517
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 230518-230527
    sprite('Action_052_06', 6)	# 230528-230533
    sprite('Action_052_07', 5)	# 230534-230538
    sprite('Action_052_08', 7)	# 230539-230545	 **attackbox here**
    label(173)
    sprite('Action_052_09', 1)	# 230546-230546	 **attackbox here**
    if SLOT_97:
        _gotolabel(173)
    sprite('Action_052_09', 32767)	# 230547-263313	 **attackbox here**
    Unknown21011(120)
    label(180)
    sprite('Action_052_00', 6)	# 263314-263319
    SFX_1('uli700uva')
    sprite('Action_052_01', 6)	# 263320-263325
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 263326-263329
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 263330-263336
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 263337-263339
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 263340-263349
    sprite('Action_052_06', 6)	# 263350-263355
    sprite('Action_052_07', 5)	# 263356-263360
    sprite('Action_052_08', 7)	# 263361-263367	 **attackbox here**
    label(181)
    sprite('Action_052_09', 1)	# 263368-263368	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_052_09', 32767)	# 263369-296135	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(480)
    label(190)
    sprite('Action_052_00', 6)	# 296136-296141
    SFX_1('uli700pla')
    sprite('Action_052_01', 6)	# 296142-296147
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 296148-296151
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 296152-296158
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 296159-296161
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 296162-296171
    sprite('Action_052_06', 6)	# 296172-296177
    sprite('Action_052_07', 5)	# 296178-296182
    sprite('Action_052_08', 7)	# 296183-296189	 **attackbox here**
    label(191)
    sprite('Action_052_09', 1)	# 296190-296190	 **attackbox here**
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_052_09', 20)	# 296191-296210	 **attackbox here**
    sprite('Action_052_09', 32767)	# 296211-328977	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(360)
    label(200)
    sprite('Action_052_00', 6)	# 328978-328983
    SFX_1('uli700umi')
    sprite('Action_052_01', 6)	# 328984-328989
    teleportRelativeX(-25000)
    SFX_0('003_swing_grap_0_0')
    sprite('Action_052_02', 4)	# 328990-328993
    teleportRelativeX(-5000)
    sprite('Action_052_03', 7)	# 328994-329000
    teleportRelativeX(-20000)
    sprite('Action_052_04', 3)	# 329001-329003
    SFX_3('SE010')
    teleportRelativeX(-20000)
    sprite('Action_052_05', 10)	# 329004-329013
    sprite('Action_052_06', 6)	# 329014-329019
    sprite('Action_052_07', 5)	# 329020-329024
    sprite('Action_052_08', 7)	# 329025-329031	 **attackbox here**
    label(201)
    sprite('Action_052_09', 1)	# 329032-329032	 **attackbox here**
    if SLOT_97:
        _gotolabel(201)
    sprite('Action_052_09', 20)	# 329033-329052	 **attackbox here**
    sprite('Action_052_09', 32767)	# 329053-361819	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(250)

@State
def CmnActLose():
    sprite('Action_248_00', 7)	# 1-7
    sprite('Action_248_01', 4)	# 8-11
    if SLOT_158:
        Unknown7006('uli403_0', 100, 879324277, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_0('003_swing_grap_0_0')
    Unknown23018(1)
    sprite('Action_248_02', 7)	# 12-18
    sprite('Action_248_03', 5)	# 19-23
    sprite('Action_248_04', 8)	# 24-31
    sprite('Action_248_05', 10)	# 32-41
    sprite('Action_248_06', 5)	# 42-46
    sprite('Action_248_07', 7)	# 47-53
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('Action_248_08', 3)	# 54-56
    sprite('Action_248_09', 3)	# 57-59
    sprite('Action_248_10', 32767)	# 60-32826
