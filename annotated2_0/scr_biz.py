@Subroutine
def PreInit():
    Unknown12019('62697a00000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Unknown13039(2)
    Unknown2049(1)
    Unknown15018(100)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('SpDashF_Land', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Unknown14004(1)
    Unknown14015(-2000, 464000, -248000, 114000, 200, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 300000, -100000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 519000, -200000, 160000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 902000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    MoveMaxChainRepeat(3)
    Unknown15009()
    Unknown14015(0, 350000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14027('NmlAtk5B')
    Unknown14015(0, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(1)
    Unknown15009()
    Unknown14015(0, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(-10000, 350000, -300000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-250000, 250000, -320000, 120000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(-150000, 250000, -350000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
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
    Move_Register('Shot_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(700000, 1000000, -100000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Shot_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(700000, 1000000, -100000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('Iai_Slash', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15012(1200)
    Unknown14015(0, 550000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('Iai_Slash_Next', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15013(5000)
    Unknown14015(250000, 1000000, -200000, 30000, 1500, 0)
    Move_EndRegister()
    Move_Register('Iai_AntiAirA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(2000)
    Unknown14015(250000, 600000, 250000, 500000, 250, 0)
    Move_EndRegister()
    Move_Register('Iai_AntiAir_Next', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown15005(1500)
    Unknown15013(10000)
    Unknown15012(0)
    Move_EndRegister()
    Move_Register('AirShot_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15012(1)
    Unknown14015(200000, 600000, -1000000, -200000, 250, 0)
    Move_EndRegister()
    Move_Register('AirShot_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15012(1)
    Unknown15014(2000)
    Unknown14015(200000, 600000, -1000000, -200000, 50, 0)
    Move_EndRegister()
    Move_Register('Iai_SlashAir_Low', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(100000, 500000, -400000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('Iai_SlashAir_High', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(100000, 500000, -100000, 500000, 250, 0)
    Move_EndRegister()
    Move_Register('Warp_A_Air', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15027(0)
    Unknown15012(250)
    Unknown14015(0, 500000, -200000, 500000, 20, 0)
    Unknown15003(0)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('Warp_B_Air', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14024('EnableAirWarp')
    Unknown15014(1)
    Unknown15027(0)
    Unknown15012(250)
    Unknown14015(0, 500000, -200000, 500000, 20, 0)
    Unknown15003(0)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('Warp_A_Air_HASEI', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 500000, 20, 0)
    Move_EndRegister()
    Move_Register('Warp_B_Air_HASEI', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14024('EnableAirWarp')
    Unknown14015(0, 500000, -200000, 500000, 20, 0)
    Move_EndRegister()
    Move_Register('Shot_D', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(300000, 800000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('Warp_D_Land', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(0)
    Unknown15012(2000)
    Unknown14015(0, 400000, -300000, 100000, 250, 100)
    Move_EndRegister()
    Move_Register('Iai_Slash_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15009()
    Unknown15021(500)
    Unknown15013(2000)
    Unknown15012(1200)
    Unknown15015(20, 25)
    Unknown14015(100000, 550000, -200000, 100000, 250, 0)
    Unknown15003(0)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AirShot_D', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(200000, 600000, -1000000, -200000, 250, 0)
    Move_EndRegister()
    Move_Register('Warp_D_Air', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(0)
    Unknown15012(2000)
    Unknown14015(0, 400000, -300000, 100000, 250, 100)
    Move_EndRegister()
    Move_Register('Warp_D_Air_HASEI', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown14013('Warp_D_Air')
    Unknown14015(0, 400000, -300000, 100000, 250, 100)
    Move_EndRegister()
    Move_Register('Warp_D_LandHitOnly', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(0)
    Unknown15012(2000)
    Unknown14015(0, 400000, -300000, 100000, 250, 100)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-250000, 250000, -200000, 600000, 250, 5)
    Move_EndRegister()
    Move_Register('AN_CmnActInvincibleAttack_Next', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(0, 400000, -150000, 250000, 250, 5)
    Move_EndRegister()
    Move_Register('AN_CmnActInvincibleAttackAir_Ne', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(50000, 700000, 50000, 500000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(50000, 700000, 50000, 500000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateStrike', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 600000, -200000, 150000, 250, 10)
    Move_EndRegister()
    Move_Register('UltimateStrike_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 300000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 650000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'Iai_AntiAirA', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'Iai_Slash', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'Iai_AntiAirA', 10000000)
    Unknown15024('Iai_Slash', 'Iai_Slash_Next', 10000000)
    Unknown15024('Iai_AntiAirA', 'Iai_AntiAir_Next', 10000000)
    Unknown15024('Iai_AntiAirA', 'Warp_D_LandHitOnly', 10000000)
    Unknown15024('Iai_Slash_Next', 'Warp_D_LandHitOnly', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2C', 'Iai_Slash', 10000000)
    Unknown15024('NmlAtk2C', 'Iai_AntiAirA', 10000000)
    Unknown12018(0, 'iz062_01')
    Unknown12018(1, 'iz062_03')
    Unknown12018(2, 'iz062_04')
    Unknown12018(3, 'iz062_05')
    Unknown12018(4, 'iz062_05')
    Unknown12018(5, 'iz062_06')
    Unknown12018(6, 'iz062_07')
    Unknown12018(7, 'iz041_02')
    Unknown12018(8, 'iz040_02')
    Unknown12018(9, 'iz045_02')
    Unknown12018(10, 'iz060_00')
    Unknown12018(11, 'iz060_01')
    Unknown12018(12, 'iz060_03')
    Unknown12018(13, 'iz060_05')
    Unknown12018(14, 'iz060_07')
    Unknown12018(15, 'iz060_14')
    Unknown12018(16, 'iz050_00')
    Unknown12018(17, 'iz052_00')
    Unknown12018(18, 'iz054_00')
    Unknown12018(19, 'iz000_00')
    Unknown12018(20, 'iz000_00')
    Unknown12018(25, 'iz063_00')
    Unknown12018(26, 'iz063_01')
    Unknown12018(27, 'iz063_02')
    Unknown12018(28, 'iz063_04')
    Unknown12018(29, 'iz063_10')
    Unknown12018(24, 'iz073_01')
    Unknown7010(0, 'biz000')
    Unknown7010(1, 'biz001')
    Unknown7010(2, 'biz002')
    Unknown7010(3, 'biz003')
    Unknown7010(4, 'biz004')
    Unknown7010(5, 'biz005')
    Unknown7010(6, 'biz006')
    Unknown7010(7, 'biz007')
    Unknown7010(8, 'biz008')
    Unknown7010(9, 'biz009')
    Unknown7010(10, 'biz010')
    Unknown7010(15, 'biz011')
    Unknown7010(16, 'biz012')
    Unknown7010(17, 'biz013')
    Unknown7010(18, 'biz014')
    Unknown7010(19, 'biz015')
    Unknown7010(20, 'biz016')
    Unknown7010(21, 'biz017')
    Unknown7010(22, 'biz018')
    Unknown7010(23, 'biz019')
    Unknown7010(24, 'biz020')
    Unknown7010(25, 'biz021')
    Unknown7010(28, 'biz022')
    Unknown7010(29, 'biz023')
    Unknown7010(30, 'biz024')
    Unknown7010(31, 'biz025')
    Unknown7010(32, 'biz026')
    Unknown7010(33, 'biz027')
    Unknown7010(34, 'biz028')
    Unknown7010(35, 'biz029')
    Unknown7010(36, 'biz030')
    Unknown7010(37, 'biz031')
    Unknown7010(39, 'biz032')
    Unknown7010(42, 'biz033')
    Unknown7010(43, 'biz034')
    Unknown7010(44, 'biz035')
    Unknown7010(45, 'biz036')
    Unknown7010(46, 'biz037')
    Unknown7010(47, 'biz038')
    Unknown7010(48, 'biz039')
    Unknown7010(49, 'biz040')
    Unknown7010(50, 'biz041')
    Unknown7010(52, 'biz042')
    Unknown7010(53, 'biz043')
    Unknown7010(54, 'biz100_0')
    Unknown7010(55, 'biz100_1')
    Unknown7010(56, 'biz100_2')
    Unknown7010(63, 'biz101_0')
    Unknown7010(64, 'biz101_1')
    Unknown7010(65, 'biz101_2')
    Unknown7010(57, 'biz102_0')
    Unknown7010(58, 'biz102_1')
    Unknown7010(59, 'biz102_2')
    Unknown7010(66, 'biz103_0')
    Unknown7010(67, 'biz103_1')
    Unknown7010(68, 'biz103_2')
    Unknown7010(60, 'biz104_0')
    Unknown7010(61, 'biz104_1')
    Unknown7010(62, 'biz104_2')
    Unknown7010(69, 'biz105_0')
    Unknown7010(70, 'biz105_1')
    Unknown7010(71, 'biz105_2')
    Unknown7010(72, 'biz150')
    Unknown7010(73, 'biz151')
    Unknown7010(74, 'biz152')
    Unknown7010(85, 'biz153')
    Unknown7010(87, 'biz154')
    Unknown7010(88, 'biz155')
    Unknown7010(96, 'biz161_0')
    Unknown7010(97, 'biz161_1')
    Unknown7010(92, 'biz162_0')
    Unknown7010(93, 'biz162_1')
    Unknown7010(98, 'biz163_0')
    Unknown7010(99, 'biz163_1')
    Unknown7010(100, 'biz164_0')
    Unknown7010(101, 'biz164_1')
    Unknown7010(105, 'biz165_0')
    Unknown7010(106, 'biz165_1')
    Unknown7010(102, 'biz166_0')
    Unknown7010(103, 'biz166_1')
    Unknown7010(90, 'biz167_0')
    Unknown7010(91, 'biz167_1')
    Unknown7010(107, 'biz168_0')
    Unknown7010(108, 'biz168_1')
    Unknown7010(110, 'biz169_0')
    Unknown7010(111, 'biz169_1')
    Unknown7010(112, 'biz159_0')
    Unknown7010(113, 'biz159_1')
    Unknown7010(94, 'biz400_0')
    Unknown7010(95, 'biz400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('04000000556c74696d617465537472696b65000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465537472696b655f4f44000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    GFX_0('Twindrive0', -1)
    GFX_0('Twindrive1', -1)

@Subroutine
def EnableAirWarp():
    SLOT_47 = 0
    if (not SLOT_11):
        SLOT_47 = 1

@Subroutine
def OnFrameStep():
    if SLOT_37:
        SLOT_11 = 0
        SLOT_4 = 0

@Subroutine
def OnPreDraw():
    Unknown23030('497a4c69676874536162657253776974636800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def CmnActStand():
    label(0)
    sprite('iz000_00', 7)	# 1-7	 **attackbox here**
    sprite('iz000_01', 7)	# 8-14	 **attackbox here**
    sprite('iz000_02', 7)	# 15-21	 **attackbox here**
    sprite('iz000_03', 7)	# 22-28	 **attackbox here**
    sprite('iz000_04', 7)	# 29-35	 **attackbox here**
    sprite('iz000_05', 7)	# 36-42	 **attackbox here**
    sprite('iz000_06', 7)	# 43-49	 **attackbox here**
    sprite('iz000_07', 7)	# 50-56	 **attackbox here**
    sprite('iz000_08', 7)	# 57-63	 **attackbox here**
    sprite('iz000_09', 7)	# 64-70	 **attackbox here**
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    if random_(2, 0, 40):
        gotoLabel(30)
    if random_(2, 0, 30):
        gotoLabel(31)
    if random_(2, 0, 50):
        gotoLabel(32)
    label(30)
    sprite('iz002_00', 6)	# 71-76
    SLOT_88 = 960
    SFX_4('biz000')
    sprite('iz002_01', 6)	# 77-82
    sprite('iz002_02', 6)	# 83-88
    sprite('iz002_03', 6)	# 89-94
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz002_04', 6)	# 95-100
    sprite('iz002_05', 6)	# 101-106
    sprite('iz002_06', 6)	# 107-112
    sprite('iz002_07', 6)	# 113-118
    sprite('iz002_08', 6)	# 119-124
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz002_09', 6)	# 125-130
    sprite('iz002_10', 6)	# 131-136
    loopRest()
    gotoLabel(0)
    label(31)
    sprite('iz002_11', 4)	# 137-140
    SLOT_88 = 960
    SFX_4('biz000')
    SFX_3('izse_01')
    sprite('iz002_12', 4)	# 141-144
    sprite('iz002_13', 4)	# 145-148
    sprite('iz002_14', 4)	# 149-152
    sprite('iz002_15', 5)	# 153-157
    sprite('iz002_16', 5)	# 158-162
    sprite('iz002_17', 5)	# 163-167
    sprite('iz002_18', 5)	# 168-172
    sprite('iz002_19', 5)	# 173-177
    loopRest()
    gotoLabel(0)
    label(32)
    sprite('iz002_20', 7)	# 178-184
    SLOT_88 = 960
    SFX_4('biz000')
    sprite('iz002_21', 7)	# 185-191
    sprite('iz002_22', 7)	# 192-198
    sprite('iz002_23', 7)	# 199-205
    sprite('iz002_24', 7)	# 206-212
    sprite('iz002_25', 7)	# 213-219
    sprite('iz002_26', 7)	# 220-226
    sprite('iz002_27', 7)	# 227-233
    sprite('iz002_28', 7)	# 234-240
    sprite('iz002_29', 7)	# 241-247
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('iz003_00', 3)	# 1-3
    SFX_4('biz001')
    sprite('iz003_01', 3)	# 4-6
    sprite('iz003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('iz010_00', 4)	# 1-4
    sprite('iz010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('iz010_02', 7)	# 1-7
    sprite('iz010_03', 7)	# 8-14
    sprite('iz010_04', 7)	# 15-21
    sprite('iz010_05', 7)	# 22-28
    sprite('iz010_06', 7)	# 29-35
    sprite('iz010_07', 7)	# 36-42
    sprite('iz010_08', 7)	# 43-49
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('iz013_00', 3)	# 1-3
    sprite('iz013_01', 3)	# 4-6
    sprite('iz013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('iz010_01', 4)	# 1-4
    sprite('iz010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('iz023_00', 2)	# 1-2
    sprite('iz023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    sprite('iz020_00', 3)	# 1-3
    sprite('iz020_01', 3)	# 4-6
    SFX_4('biz002')
    label(10)
    sprite('iz020_00', 3)	# 7-9
    sprite('iz020_01', 3)	# 10-12
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('iz020_00', 3)	# 13-15
    sprite('iz020_01', 3)	# 16-18
    SFX_4('biz002')
    label(11)
    sprite('iz020_00', 3)	# 19-21
    sprite('iz020_01', 3)	# 22-24
    loopRest()
    gotoLabel(11)
    label(2)
    sprite('iz020_00', 3)	# 25-27
    sprite('iz020_01', 3)	# 28-30
    SFX_4('biz003')
    label(22)
    sprite('iz020_00', 3)	# 31-33
    sprite('iz020_01', 3)	# 34-36
    loopRest()
    gotoLabel(22)

@State
def CmnActJumpUpperEnd():
    sprite('iz020_02', 3)	# 1-3
    sprite('iz020_03', 3)	# 4-6
    sprite('iz020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('iz020_05', 3)	# 1-3
    sprite('iz020_06', 3)	# 4-6
    label(0)
    sprite('iz020_07', 4)	# 7-10
    sprite('iz020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('iz024_00', 3)	# 1-3
    sprite('iz024_01', 3)	# 4-6
    sprite('iz024_02', 3)	# 7-9
    sprite('iz024_03', 3)	# 10-12
    sprite('iz024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('iz024_00', 2)	# 1-2
    sprite('iz024_01', 2)	# 3-4
    sprite('iz024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('iz024_03', 3)	# 1-3
    sprite('iz024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('iz030_00', 7)	# 1-7
    label(0)
    sprite('iz030_01', 7)	# 8-14
    sprite('iz030_02', 7)	# 15-21
    sprite('iz030_03', 7)	# 22-28
    sprite('iz030_04', 7)	# 29-35
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz030_05', 7)	# 36-42
    sprite('iz030_06', 7)	# 43-49
    sprite('iz030_07', 7)	# 50-56
    sprite('iz030_08', 7)	# 57-63
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('iz031_00', 7)	# 1-7
    label(0)
    sprite('iz031_01', 7)	# 8-14
    sprite('iz031_02', 7)	# 15-21
    sprite('iz031_03', 7)	# 22-28
    sprite('iz031_04', 7)	# 29-35
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz031_05', 7)	# 36-42
    sprite('iz031_06', 7)	# 43-49
    sprite('iz031_07', 7)	# 50-56
    sprite('iz031_08', 7)	# 57-63
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('iz032_00', 2)	# 1-2
    sprite('iz032_01', 4)	# 3-6	 **attackbox here**
    sprite('iz032_02', 4)	# 7-10	 **attackbox here**
    sprite('iz032_03', 4)	# 11-14	 **attackbox here**
    sprite('iz032_04', 4)	# 15-18	 **attackbox here**
    sprite('iz032_05', 4)	# 19-22	 **attackbox here**
    Unknown8006(100, 1, 1)
    sprite('iz032_06', 4)	# 23-26	 **attackbox here**
    sprite('iz032_07', 4)	# 27-30	 **attackbox here**
    sprite('iz032_08', 4)	# 31-34	 **attackbox here**
    loopRest()
    label(0)
    sprite('iz032_01', 4)	# 35-38	 **attackbox here**
    Unknown8006(100, 1, 1)
    sprite('iz032_02', 4)	# 39-42	 **attackbox here**
    sprite('iz032_03', 4)	# 43-46	 **attackbox here**
    sprite('iz032_04', 4)	# 47-50	 **attackbox here**
    sprite('iz032_05', 4)	# 51-54	 **attackbox here**
    Unknown8006(100, 1, 1)
    sprite('iz032_06', 4)	# 55-58	 **attackbox here**
    sprite('iz032_07', 4)	# 59-62	 **attackbox here**
    sprite('iz032_08', 4)	# 63-66	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('iz032_09', 3)	# 1-3
    sprite('iz032_10', 3)	# 4-6
    sprite('iz032_11', 3)	# 7-9
    loopRest()
    ExitState()

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown1084(1)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
        setInvincibleFor(7)
    sprite('iz033_00', 1)	# 1-1
    sprite('iz033_01', 2)	# 2-3
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('iz033_02', 3)	# 4-6
    sprite('iz033_03', 1)	# 7-7
    sprite('iz033_03', 2)	# 8-9
    loopRest()
    label(0)
    sprite('iz033_02', 3)	# 10-12
    sprite('iz033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz033_04', 3)	# 16-18
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('iz033_05', 3)	# 19-21
    ExitState()

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        if Unknown23145('CmnActJumpDown'):
            SLOT_10 = 100
        enterState('SpDashF_Air')
    sprite('iz035_00', 3)	# 1-3
    SFX_4('biz004')
    label(0)
    sprite('iz035_01', 3)	# 4-6
    sprite('iz035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():

    def upon_IMMEDIATE():
        pass
    sprite('iz036_00', 3)	# 1-3
    SFX_4('biz006')
    label(0)
    sprite('iz036_01', 3)	# 4-6
    sprite('iz036_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('iz050_00', 1)	# 1-1
    sprite('iz050_01', 1)	# 2-2
    sprite('iz050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('iz050_01', 1)	# 1-1
    sprite('iz050_02', 1)	# 2-2
    sprite('iz050_01', 2)	# 3-4
    sprite('iz050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('iz050_02', 1)	# 1-1
    sprite('iz050_03', 1)	# 2-2
    sprite('iz050_02', 2)	# 3-4
    sprite('iz050_01', 2)	# 5-6
    sprite('iz050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('iz050_03', 1)	# 1-1
    sprite('iz050_04', 1)	# 2-2
    sprite('iz050_03', 2)	# 3-4
    sprite('iz050_02', 2)	# 5-6
    sprite('iz050_01', 2)	# 7-8
    sprite('iz050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('iz050_04', 1)	# 1-1
    sprite('iz050_04', 1)	# 2-2
    sprite('iz050_04', 2)	# 3-4
    sprite('iz050_03', 2)	# 5-6
    sprite('iz050_02', 2)	# 7-8
    sprite('iz050_01', 2)	# 9-10
    sprite('iz050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('iz052_00', 1)	# 1-1
    sprite('iz052_01', 1)	# 2-2
    sprite('iz052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('iz052_01', 1)	# 1-1
    sprite('iz052_02', 1)	# 2-2
    sprite('iz052_01', 2)	# 3-4
    sprite('iz052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('iz052_02', 1)	# 1-1
    sprite('iz052_03', 1)	# 2-2
    sprite('iz052_02', 2)	# 3-4
    sprite('iz052_01', 2)	# 5-6
    sprite('iz052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('iz052_03', 1)	# 1-1
    sprite('iz052_04', 1)	# 2-2
    sprite('iz052_03', 2)	# 3-4
    sprite('iz052_02', 2)	# 5-6
    sprite('iz052_01', 2)	# 7-8
    sprite('iz052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('iz052_04', 1)	# 1-1
    sprite('iz052_04', 1)	# 2-2
    sprite('iz052_04', 2)	# 3-4
    sprite('iz052_03', 2)	# 5-6
    sprite('iz052_02', 2)	# 7-8
    sprite('iz052_01', 2)	# 9-10
    sprite('iz052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('iz054_00', 1)	# 1-1
    sprite('iz054_01', 1)	# 2-2
    sprite('iz054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('iz054_01', 1)	# 1-1
    sprite('iz054_02', 1)	# 2-2
    sprite('iz054_01', 2)	# 3-4
    sprite('iz054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('iz054_02', 1)	# 1-1
    sprite('iz054_03', 1)	# 2-2
    sprite('iz054_02', 2)	# 3-4
    sprite('iz054_01', 2)	# 5-6
    sprite('iz054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('iz054_03', 1)	# 1-1
    sprite('iz054_04', 1)	# 2-2
    sprite('iz054_03', 2)	# 3-4
    sprite('iz054_02', 2)	# 5-6
    sprite('iz054_01', 2)	# 7-8
    sprite('iz054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('iz054_04', 1)	# 1-1
    sprite('iz054_04', 1)	# 2-2
    sprite('iz054_04', 2)	# 3-4
    sprite('iz054_03', 2)	# 5-6
    sprite('iz054_02', 2)	# 7-8
    sprite('iz054_01', 2)	# 9-10
    sprite('iz054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('iz060_00', 4)	# 1-4
    label(0)
    sprite('iz060_01', 4)	# 5-8
    sprite('iz060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('iz060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('iz060_04', 4)	# 1-4
    label(0)
    sprite('iz060_05', 4)	# 5-8
    sprite('iz060_06', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('iz060_07', 2)	# 1-2
    sprite('iz060_08', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('iz060_09', 3)	# 1-3
    sprite('iz060_10', 3)	# 4-6
    sprite('iz060_11', 3)	# 7-9
    sprite('iz060_12', 3)	# 10-12
    sprite('iz060_13', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('iz060_14', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('iz061_00', 3)	# 1-3
    sprite('iz061_01', 3)	# 4-6
    sprite('iz061_02', 3)	# 7-9
    sprite('iz061_03', 3)	# 10-12
    sprite('iz061_04', 3)	# 13-15
    sprite('iz061_05', 3)	# 16-18
    sprite('iz061_06', 2)	# 19-20
    sprite('iz061_07', 2)	# 21-22
    sprite('iz061_08', 2)	# 23-24
    sprite('iz061_09', 2)	# 25-26
    sprite('iz061_10', 2)	# 27-28

@State
def CmnActFDownUpper():
    sprite('iz063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('iz063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('iz063_02', 3)	# 1-3
    sprite('iz063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('iz063_04', 3)	# 1-3
    sprite('iz063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('iz063_06', 2)	# 1-2
    sprite('iz063_07', 2)	# 3-4
    sprite('iz063_08', 3)	# 5-7
    sprite('iz063_09', 3)	# 8-10
    sprite('iz063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('iz063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('iz064_00', 2)	# 1-2
    sprite('iz064_01', 2)	# 3-4
    sprite('iz064_02', 2)	# 5-6
    sprite('iz064_03', 2)	# 7-8
    sprite('iz064_04', 2)	# 9-10
    sprite('iz064_05', 2)	# 11-12
    sprite('iz064_06', 2)	# 13-14
    sprite('iz064_07', 2)	# 15-16
    sprite('iz064_08', 2)	# 17-18
    sprite('iz064_09', 2)	# 19-20

@State
def CmnActVDownUpper():
    sprite('iz062_00', 3)	# 1-3
    label(0)
    sprite('iz062_01', 3)	# 4-6
    sprite('iz062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('iz062_03', 3)	# 1-3
    sprite('iz062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('iz062_05', 3)	# 1-3
    sprite('iz062_06', 3)	# 4-6
    label(0)
    sprite('iz062_07', 3)	# 7-9
    sprite('iz062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('iz062_09', 2)	# 1-2
    sprite('iz062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('iz072_00', 3)	# 1-3
    sprite('iz072_01', 3)	# 4-6
    sprite('iz072_02', 3)	# 7-9
    label(0)
    sprite('iz072_01', 3)	# 10-12
    sprite('iz072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('iz074_00', 3)	# 1-3
    sprite('iz074_01', 3)	# 4-6
    sprite('iz074_02', 3)	# 7-9
    sprite('iz074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('iz082_00', 2)	# 1-2
    sprite('iz082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('iz071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('iz073_00', 3)	# 1-3
    sprite('iz073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('iz073_02', 3)	# 1-3
    label(0)
    sprite('iz073_03', 3)	# 4-6
    sprite('iz073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('iz070_00', 3)	# 1-3
    sprite('iz070_01', 3)	# 4-6
    sprite('iz070_02', 3)	# 7-9
    sprite('iz070_03', 3)	# 10-12
    sprite('iz070_02', 4)	# 13-16
    sprite('iz070_03', 4)	# 17-20
    label(0)
    sprite('iz070_02', 7)	# 21-27
    sprite('iz070_03', 7)	# 28-34
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('iz070_04', 2)	# 1-2
    sprite('iz070_05', 3)	# 3-5
    sprite('iz070_06', 4)	# 6-9
    sprite('iz070_07', 6)	# 10-15
    sprite('iz070_08', 5)	# 16-20
    sprite('iz070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('iz070_10', 2)	# 1-2
    sprite('iz070_11', 2)	# 3-4
    sprite('iz070_12', 2)	# 5-6
    sprite('iz070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('iz113_00', 3)	# 1-3
    sprite('iz113_01', 3)	# 4-6
    sprite('iz113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('iz113_00', 3)	# 1-3
    sprite('iz113_01', 3)	# 4-6
    sprite('iz113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('iz113_00', 3)	# 1-3
    sprite('iz113_01', 3)	# 4-6
    sprite('iz113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('iz110_00', 2)	# 1-2
    sprite('iz110_01', 2)	# 3-4
    sprite('iz110_02', 2)	# 5-6
    sprite('iz110_03', 2)	# 7-8
    sprite('iz110_04', 2)	# 9-10
    sprite('iz110_06', 2)	# 11-12
    sprite('iz110_07', 2)	# 13-14
    sprite('iz110_08', 200)	# 15-214
    sprite('iz110_09', 3)	# 215-217
    sprite('iz110_10', 3)	# 218-220

@State
def CmnActUkemiLandB():
    sprite('iz111_00', 3)	# 1-3
    sprite('iz111_01', 3)	# 4-6
    sprite('iz111_02', 3)	# 7-9
    sprite('iz111_03', 3)	# 10-12
    sprite('iz111_04', 3)	# 13-15
    sprite('iz111_06', 3)	# 16-18
    sprite('iz111_07', 200)	# 19-218
    sprite('iz111_08', 3)	# 219-221
    sprite('iz111_09', 3)	# 222-224

@State
def CmnActUkemiLandN():
    sprite('iz112_00', 2)	# 1-2
    sprite('iz112_01', 2)	# 3-4
    sprite('iz112_02', 2)	# 5-6
    sprite('iz112_03', 2)	# 7-8
    sprite('iz112_04', 2)	# 9-10
    sprite('iz112_05', 2)	# 11-12
    sprite('iz112_06', 2)	# 13-14
    sprite('iz112_07', 2)	# 15-16
    sprite('iz112_08', 2)	# 17-18
    sprite('iz112_09', 2)	# 19-20

@State
def CmnActUkemiLandNLanding():
    sprite('iz024_00', 3)	# 1-3
    sprite('iz024_01', 3)	# 4-6
    sprite('iz024_02', 3)	# 7-9
    sprite('iz024_03', 3)	# 10-12
    sprite('iz024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('iz040_00', 3)	# 1-3
    sprite('iz040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('iz040_02', 3)	# 1-3
    sprite('iz040_03', 3)	# 4-6
    sprite('iz040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('iz040_01', 3)	# 1-3
    sprite('iz040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('iz040_05', 3)	# 1-3
    label(0)
    sprite('iz040_02', 3)	# 4-6
    sprite('iz040_03', 3)	# 7-9
    sprite('iz040_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('iz040_01', 3)	# 1-3
    sprite('iz040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('iz041_00', 3)	# 1-3
    sprite('iz041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('iz041_02', 3)	# 1-3
    sprite('iz041_03', 3)	# 4-6
    sprite('iz041_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('iz041_01', 3)	# 1-3
    sprite('iz041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('iz041_05', 3)	# 1-3
    label(0)
    sprite('iz041_02', 3)	# 4-6
    sprite('iz041_03', 3)	# 7-9
    sprite('iz041_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('iz041_01', 3)	# 1-3
    sprite('iz041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('iz043_00', 3)	# 1-3
    sprite('iz043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('iz043_02', 3)	# 1-3
    sprite('iz043_03', 3)	# 4-6
    sprite('iz043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('iz043_01', 3)	# 1-3
    sprite('iz043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('iz043_05', 3)	# 1-3
    label(0)
    sprite('iz043_02', 3)	# 4-6
    sprite('iz043_03', 3)	# 7-9
    sprite('iz043_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('iz043_01', 3)	# 1-3
    sprite('iz043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('iz045_00', 3)	# 1-3
    sprite('iz045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('iz045_02', 3)	# 1-3
    sprite('iz045_03', 3)	# 4-6
    sprite('iz045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('iz045_01', 3)	# 1-3
    sprite('iz045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('iz045_05', 3)	# 1-3
    label(0)
    sprite('iz045_02', 3)	# 4-6
    sprite('iz045_03', 3)	# 7-9
    sprite('iz045_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('iz045_01', 3)	# 1-3
    sprite('iz045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('iz090_00', 2)	# 1-2
    sprite('iz090_01', 2)	# 3-4
    sprite('iz090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('iz090_03', 6)	# 6-11
    sprite('iz090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('iz091_00', 2)	# 1-2
    sprite('iz091_01', 2)	# 3-4
    sprite('iz091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('iz091_03', 6)	# 6-11
    sprite('iz091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('iz092_00', 2)	# 1-2
    sprite('iz092_01', 2)	# 3-4
    sprite('iz092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('iz092_03', 6)	# 6-11
    sprite('iz092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('iz025_00', 4)	# 1-4
    sprite('iz025_01', 4)	# 5-8
    sprite('iz025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('iz040_02', 1)	# 1-1
    sprite('iz040_01', 3)	# 2-4
    sprite('iz040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('iz312_00', 3)	# 1-3
    sprite('iz312_01', 3)	# 4-6
    sprite('iz312_02', 3)	# 7-9
    sprite('iz312_03', 3)	# 10-12
    sprite('iz312_04', 3)	# 13-15	 **attackbox here**
    sprite('iz312_05', 3)	# 16-18
    sprite('iz312_06', 3)	# 19-21
    sprite('iz312_07', 3)	# 22-24

@State
def CmnActAirLockWait():
    sprite('iz045_02', 1)	# 1-1
    sprite('iz045_01', 3)	# 2-4
    sprite('iz045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('iz322_00', 3)	# 1-3
    sprite('iz322_01', 3)	# 4-6
    sprite('iz322_02', 8)	# 7-14
    sprite('iz322_03', 3)	# 15-17	 **attackbox here**
    sprite('iz322_04', 3)	# 18-20
    sprite('iz322_05', 3)	# 21-23
    sprite('iz322_06', 3)	# 24-26
    sprite('iz322_07', 3)	# 27-29

@State
def CmnActLandSpin():
    sprite('iz071_00', 4)	# 1-4
    sprite('iz071_01', 4)	# 5-8
    label(0)
    sprite('iz071_02', 2)	# 9-10
    sprite('iz071_03', 2)	# 11-12
    sprite('iz071_04', 2)	# 13-14
    sprite('iz071_05', 2)	# 15-16
    sprite('iz071_06', 2)	# 17-18
    sprite('iz071_07', 2)	# 19-20
    sprite('iz071_08', 2)	# 21-22
    sprite('iz071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('iz071_10', 6)	# 1-6
    sprite('iz071_11', 5)	# 7-11
    sprite('iz071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('iz071_02', 2)	# 1-2
    sprite('iz071_03', 2)	# 3-4
    sprite('iz071_04', 2)	# 5-6
    sprite('iz071_05', 2)	# 7-8
    sprite('iz071_06', 2)	# 9-10
    sprite('iz071_07', 2)	# 11-12
    sprite('iz071_08', 2)	# 13-14
    sprite('iz071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('iz077_00', 2)	# 1-2
    sprite('iz077_01', 2)	# 3-4
    sprite('iz077_00ex01', 2)	# 5-6
    sprite('iz077_01ex01', 2)	# 7-8
    sprite('iz077_00ex02', 2)	# 9-10
    sprite('iz077_01ex02', 2)	# 11-12
    sprite('iz077_00ex03', 2)	# 13-14
    sprite('iz077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('iz077_02', 4)	# 1-4
    label(0)
    sprite('iz077_03', 3)	# 5-7
    sprite('iz077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('iz077_05', 5)	# 1-5
    sprite('iz077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('iz060_07', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('iz060_11', 4)	# 1-4
    sprite('iz060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('iz331_00', 2)	# 1-2
    sprite('iz331_01', 2)	# 3-4
    label(0)
    sprite('iz331_02', 3)	# 5-7
    sprite('iz331_03', 3)	# 8-10
    sprite('iz331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('iz331_05', 2)	# 1-2
    label(0)
    sprite('iz331_06', 3)	# 3-5
    sprite('iz331_07', 3)	# 6-8
    sprite('iz331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('iz331_09', 3)	# 1-3
    sprite('iz331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('iz331_11', 2)	# 1-2
    sprite('iz331_12', 2)	# 3-4
    label(0)
    sprite('iz331_02', 3)	# 5-7
    sprite('iz331_03', 3)	# 8-10
    sprite('iz331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('iz331_05', 2)	# 1-2
    label(0)
    sprite('iz331_06', 3)	# 3-5
    sprite('iz331_07', 3)	# 6-8
    sprite('iz331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('iz331_13', 3)	# 1-3
    sprite('iz331_14', 3)	# 4-6
    label(0)
    sprite('iz020_07', 4)	# 7-10
    sprite('iz020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('iz333_00', 3)	# 1-3	 **attackbox here**
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_armchange', 0)
    sprite('iz333_01', 3)	# 4-6	 **attackbox here**
    sprite('iz333_02', 3)	# 7-9	 **attackbox here**
    sprite('iz333_03', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_IZ_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('iz333_04', 3)	# 1-3	 **attackbox here**
    sprite('iz333_05', 3)	# 4-6	 **attackbox here**
    GFX_0('OverDriveAura', 0)
    GFX_0('OverDriveAura_oku', 1)
    label(0)
    sprite('iz333_06', 3)	# 7-9	 **attackbox here**
    sprite('iz333_07', 3)	# 10-12	 **attackbox here**
    sprite('iz333_05', 3)	# 13-15	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('iz333_08', 3)	# 1-3	 **attackbox here**
    GFX_1('izef_armchange', 0)
    sprite('iz333_09', 3)	# 4-6	 **attackbox here**
    sprite('iz333_10', 3)	# 7-9
    sprite('iz333_11', 3)	# 10-12

@State
def CmnActAirOverDriveBegin():
    sprite('iz333_12', 3)	# 1-3	 **attackbox here**
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_armchange', 0)
    sprite('iz333_13', 3)	# 4-6	 **attackbox here**
    sprite('iz333_14', 3)	# 7-9	 **attackbox here**
    sprite('iz333_15', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_IZ_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('iz333_16', 3)	# 1-3	 **attackbox here**
    sprite('iz333_05', 3)	# 4-6	 **attackbox here**
    GFX_0('OverDriveAura', 0)
    GFX_0('OverDriveAura_oku', 1)
    label(0)
    sprite('iz333_06', 3)	# 7-9	 **attackbox here**
    sprite('iz333_07', 3)	# 10-12	 **attackbox here**
    sprite('iz333_05', 3)	# 13-15	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('iz333_08', 2)	# 1-2	 **attackbox here**
    GFX_1('izef_armchange', 0)
    sprite('iz333_17', 2)	# 3-4
    sprite('iz333_18', 2)	# 5-6
    sprite('iz020_05', 3)	# 7-9
    sprite('iz020_06', 3)	# 10-12
    label(0)
    sprite('iz020_07', 4)	# 13-16
    sprite('iz020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('iz333_00', 3)	# 1-3	 **attackbox here**
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_armchange', 0)
    sprite('iz333_01', 3)	# 4-6	 **attackbox here**
    sprite('iz333_02', 3)	# 7-9	 **attackbox here**
    sprite('iz333_03', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_IZ_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('iz333_04', 3)	# 1-3	 **attackbox here**
    sprite('iz333_05', 3)	# 4-6	 **attackbox here**
    GFX_0('OverDriveAura', 0)
    GFX_0('OverDriveAura_oku', 1)
    label(0)
    sprite('iz333_06', 3)	# 7-9	 **attackbox here**
    sprite('iz333_07', 3)	# 10-12	 **attackbox here**
    sprite('iz333_05', 3)	# 13-15	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('iz333_08', 3)	# 1-3	 **attackbox here**
    GFX_1('izef_armchange', 0)
    sprite('iz333_09', 3)	# 4-6	 **attackbox here**
    sprite('iz333_10', 3)	# 7-9
    sprite('iz333_11', 3)	# 10-12

@State
def CmnActAirCrossRushBegin():
    sprite('iz333_12', 3)	# 1-3	 **attackbox here**
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_armchange', 0)
    sprite('iz333_13', 3)	# 4-6	 **attackbox here**
    sprite('iz333_14', 3)	# 7-9	 **attackbox here**
    sprite('iz333_15', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_IZ_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('iz333_16', 3)	# 1-3	 **attackbox here**
    sprite('iz333_05', 3)	# 4-6	 **attackbox here**
    GFX_0('OverDriveAura', 0)
    GFX_0('OverDriveAura_oku', 1)
    label(0)
    sprite('iz333_06', 3)	# 7-9	 **attackbox here**
    sprite('iz333_07', 3)	# 10-12	 **attackbox here**
    sprite('iz333_05', 3)	# 13-15	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('iz333_08', 2)	# 1-2	 **attackbox here**
    GFX_1('izef_armchange', 0)
    sprite('iz333_17', 2)	# 3-4
    sprite('iz333_18', 2)	# 5-6
    sprite('iz020_05', 3)	# 7-9
    sprite('iz020_06', 3)	# 10-12
    label(0)
    sprite('iz020_07', 4)	# 13-16
    sprite('iz020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('iz331_00', 2)	# 1-2
    sprite('iz331_01', 2)	# 3-4
    label(0)
    sprite('iz331_02', 3)	# 5-7
    sprite('iz331_03', 3)	# 8-10
    sprite('iz331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('iz331_05', 2)	# 1-2
    label(0)
    sprite('iz331_06', 3)	# 3-5
    sprite('iz331_07', 3)	# 6-8
    sprite('iz331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('iz331_09', 3)	# 1-3
    sprite('iz331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('iz331_11', 2)	# 1-2
    sprite('iz331_12', 2)	# 3-4
    label(0)
    sprite('iz331_02', 3)	# 5-7
    sprite('iz331_03', 3)	# 8-10
    sprite('iz331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('iz331_05', 2)	# 1-2
    label(0)
    sprite('iz331_06', 3)	# 3-5
    sprite('iz331_07', 3)	# 6-8
    sprite('iz331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('iz331_13', 3)	# 1-3
    sprite('iz331_14', 3)	# 4-6
    sprite('iz020_05', 3)	# 7-9
    sprite('iz020_06', 3)	# 10-12
    label(0)
    sprite('iz020_07', 4)	# 13-16
    sprite('iz020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)

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
    sprite('iz406_06', 3)	# 32-34	 **attackbox here**
    SFX_3('izse_01')
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    label(0)
    sprite('iz406_06', 3)	# 35-37	 **attackbox here**
    sprite('iz406_07', 3)	# 38-40	 **attackbox here**
    sprite('iz406_08', 3)	# 41-43	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz406_06', 1)	# 44-44	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    sprite('iz406_09', 2)	# 45-46	 **attackbox here**
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('iz406_10', 16)	# 47-62	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    Unknown8000(-1, 1, 1)
    sprite('iz406_11', 4)	# 63-66
    sprite('iz406_12', 4)	# 67-70
    sprite('iz406_13', 4)	# 71-74

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('iz406_09', 2)	# 2-3	 **attackbox here**
    sprite('iz406_10', 4)	# 4-7	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    Unknown8000(-1, 1, 1)
    sprite('iz406_11', 2)	# 8-9
    sprite('iz406_12', 3)	# 10-12
    sprite('iz406_13', 3)	# 13-15
    sprite('iz402_00', 3)	# 16-18
    Unknown3029(1)
    sprite('iz402_01', 3)	# 19-21
    sprite('iz402_02', 2)	# 22-23
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    sprite('iz402_03', 4)	# 24-27
    sprite('iz402_04', 4)	# 28-31
    sprite('iz404_00', 1)	# 32-32
    sprite('iz404_01', 2)	# 33-34
    Unknown7015()
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo_AntiAirA', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    sprite('iz404_02', 3)	# 35-37	 **attackbox here**
    Unknown7009(2)
    sprite('iz404_03', 5)	# 38-42
    sprite('iz404_04', 5)	# 43-47
    sprite('iz404_05', 5)	# 48-52
    sprite('iz404_06', 5)	# 53-57
    sprite('iz404_07', 6)	# 58-63
    sprite('iz404_08', 6)	# 64-69
    sprite('iz404_09', 6)	# 70-75

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(20000)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('iz203_00', 2)	# 1-2
    sprite('iz203_01', 2)	# 3-4
    sprite('iz203_02', 2)	# 5-6	 **attackbox here**
    SFX_3('izse_01')
    Unknown7009(0)
    sprite('iz203_03', 3)	# 7-9	 **attackbox here**
    SFX_0('008_swing_pole_2')
    GFX_0('Kaku5CZanzo', -1)
    GFX_0('5CKakuseiAura', 0)
    GFX_0('5CKakuseiAura_oku', 1)
    sprite('iz203_03', 2)	# 10-11	 **attackbox here**
    sprite('iz203_04', 3)	# 12-14	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('iz203_05', 3)	# 15-17	 **attackbox here**
    sprite('iz203_05ex00', 3)	# 18-20
    sprite('iz203_06', 3)	# 21-23
    sprite('iz203_07', 2)	# 24-25
    sprite('iz203_08', 2)	# 26-27

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(10000)
        AirPushbackY(20000)
        Unknown9016(1)
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        Unknown2004(1, 0)
    sprite('iz202_00', 3)	# 1-3
    sprite('iz202_01', 3)	# 4-6
    Unknown7009(1)
    physicsXImpulse(15000)
    sprite('iz202_02', 2)	# 7-8
    SFX_3('izse_01')
    Unknown1019(50)
    sprite('iz202_03', 2)	# 9-10
    GFX_0('5CZanzo', 0)
    SFX_0('008_swing_pole_2')
    Unknown1019(25)
    sprite('iz202_04', 3)	# 11-13	 **attackbox here**
    Unknown1019(0)
    sprite('iz202_05', 3)	# 14-16	 **attackbox here**
    sprite('iz202_06', 2)	# 17-18	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('iz202_07', 3)	# 19-21
    sprite('iz202_08', 3)	# 22-24
    sprite('iz202_09', 3)	# 25-27
    sprite('iz202_10', 3)	# 28-30
    sprite('iz202_11', 2)	# 31-32
    sprite('iz202_12', 2)	# 33-34

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(3000)
        AirPushbackY(14000)
        PushbackX(20000)
        hitstun(17)
        AirUntechableTime(26)
        Unknown9016(1)
        HitOrBlockCancel('AN_NmlAtk5A_4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
    sprite('iz213_00', 1)	# 1-1
    sprite('iz213_01', 2)	# 2-3
    sprite('iz213_02', 2)	# 4-5
    SFX_0('001_airbackdash_0')
    physicsXImpulse(60000)
    sprite('iz213_03', 2)	# 6-7
    Unknown1019(50)
    SFX_3('izse_08')
    sprite('iz213_04', 2)	# 8-9
    Unknown1019(50)
    Unknown7009(1)
    sprite('iz213_05', 2)	# 10-11
    Unknown1019(50)
    sprite('iz213_06', 2)	# 12-13
    physicsXImpulse(0)
    sprite('iz213_07', 2)	# 14-15	 **attackbox here**
    SFX_0('008_swing_pole_2')
    sprite('iz213_08', 3)	# 16-18	 **attackbox here**
    sprite('iz213_09', 3)	# 19-21	 **attackbox here**
    GFX_1('izef_fire', 0)
    GFX_1('izef_fire_dust', 1)
    GFX_1('izef_fire_dust', 2)
    GFX_1('izef_fire_dust', 3)
    Recovery()
    Unknown2063()
    sprite('iz213_10', 2)	# 22-23	 **attackbox here**
    sprite('iz213_11', 3)	# 24-26
    sprite('iz213_12', 3)	# 27-29
    sprite('iz213_13', 3)	# 30-32
    sprite('iz213_14', 3)	# 33-35
    sprite('iz213_15', 3)	# 36-38
    sprite('iz213_16', 4)	# 39-42
    sprite('iz213_17', 4)	# 43-46

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2300)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(18000)
        AirPushbackX(35000)
        PushbackX(8000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11044(1)
        JumpCancel_(0)
    sprite('iz210_00', 2)	# 1-2
    sprite('iz210_01', 2)	# 3-4
    sprite('iz210_01', 3)	# 5-7
    sprite('iz210_02', 4)	# 8-11
    sprite('iz210_03', 3)	# 12-14
    SFX_0('006_swing_blade_1')
    sprite('iz210_04', 1)	# 15-15	 **attackbox here**
    tag_voice(1, 'biz106_0', 'biz106_1', 'biz106_2', '')
    GFX_0('6AZanzo', -1)
    Unknown30088(1)
    sprite('iz210_04', 2)	# 16-17	 **attackbox here**
    sprite('iz210_05', 4)	# 18-21	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('iz210_06', 5)	# 22-26	 **attackbox here**
    sprite('iz210_07', 5)	# 27-31	 **attackbox here**
    sprite('iz210_08', 5)	# 32-36	 **attackbox here**
    sprite('iz210_09', 5)	# 37-41	 **attackbox here**
    sprite('iz210_10', 3)	# 42-44	 **attackbox here**
    sprite('iz210_11', 3)	# 45-47	 **attackbox here**

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
    sprite('iz200_00', 1)	# 1-1
    sprite('iz200_01', 2)	# 2-3
    sprite('iz200_02', 2)	# 4-5
    SFX_0('008_swing_pole_0')
    Unknown7009(0)
    sprite('iz200_03', 3)	# 6-8	 **attackbox here**
    sprite('iz200_04', 3)	# 9-11
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('iz200_02', 2)	# 12-13
    sprite('iz200_01', 2)	# 14-15
    sprite('iz200_00', 2)	# 16-17

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(15000)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5B_2nd')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
    sprite('iz201_00', 2)	# 1-2
    sprite('iz201_01', 2)	# 3-4
    sprite('iz201_02', 2)	# 5-6
    SFX_3('izse_01')
    sprite('iz201_03', 2)	# 7-8
    sprite('iz201_04', 2)	# 9-10
    SFX_0('004_swing_grap_1_1')
    Unknown7009(0)
    sprite('iz201_05', 3)	# 11-13	 **attackbox here**
    sprite('iz201_06', 3)	# 14-16	 **attackbox here**
    sprite('iz201_07', 2)	# 17-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('iz201_08', 3)	# 19-21
    sprite('iz201_09', 3)	# 22-24
    sprite('iz201_10', 3)	# 25-27
    sprite('iz201_11', 3)	# 28-30
    sprite('iz201_12', 4)	# 31-34

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP2(85)
        AirPushbackX(10000)
        AirPushbackY(30000)
        Unknown9016(1)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
    sprite('iz212_00', 1)	# 1-1
    sprite('iz212_01', 2)	# 2-3
    sprite('iz212_02', 2)	# 4-5
    physicsXImpulse(-4000)
    sprite('iz212_03', 2)	# 6-7
    sprite('iz212_04', 2)	# 8-9
    physicsXImpulse(33800)
    sprite('iz212_05', 2)	# 10-11
    sprite('iz212_06', 2)	# 12-13
    tag_voice(1, 'biz108_0', 'biz108_1', 'biz108_2', '')
    SFX_0('006_swing_blade_2')
    GFX_0('6CZanzo', -1)
    sprite('iz212_07', 3)	# 14-16	 **attackbox here**
    physicsXImpulse(0)
    sprite('iz212_08', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('iz212_09', 3)	# 20-22
    sprite('iz212_10', 3)	# 23-25
    sprite('iz212_11', 3)	# 26-28
    sprite('iz212_12', 3)	# 29-31
    sprite('iz212_13', 3)	# 32-34
    sprite('iz212_14', 3)	# 35-37
    sprite('iz212_15', 3)	# 38-40
    sprite('iz212_16', 3)	# 41-43
    sprite('iz212_17', 3)	# 44-46

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        PushbackX(12000)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('iz230_00', 2)	# 1-2
    sprite('iz230_01', 1)	# 3-3
    sprite('iz230_01', 2)	# 4-5
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    sprite('iz230_02', 3)	# 6-8
    sprite('iz230_03', 3)	# 9-11	 **attackbox here**
    sprite('iz230_04', 5)	# 12-16
    Recovery()
    Unknown2063()
    sprite('iz230_05', 5)	# 17-21
    sprite('iz230_06', 5)	# 22-26

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1100)
        Unknown11092(1)
        PushbackX(5000)
        AirPushbackX(4000)
        AirPushbackY(13000)
        AirUntechableTime(26)
        Unknown9016(1)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('iz233_00', 2)	# 1-2
    sprite('iz233_01', 2)	# 3-4
    sprite('iz233_02', 1)	# 5-5
    sprite('iz233_02', 2)	# 6-7
    GFX_0('2CKakuseiAura', 0)
    SFX_3('izse_01')
    sprite('iz233_03', 2)	# 8-9
    SFX_0('008_swing_pole_2')
    sprite('iz233_04', 2)	# 10-11
    GFX_0('Kaku2CZanzo00', -1)
    Unknown7009(1)
    sprite('iz233_05', 3)	# 12-14	 **attackbox here**
    physicsXImpulse(0)
    sprite('iz233_06', 2)	# 15-16
    sprite('iz233_07', 3)	# 17-19
    SFX_3('izse_01')
    sprite('iz233_08', 1)	# 20-20
    sprite('iz233_09', 3)	# 21-23	 **attackbox here**
    RefreshMultihit()
    PushbackX(-15000)
    AirPushbackX(4000)
    AirPushbackY(20000)
    GFX_0('Kaku2CZanzo01', -1)
    sprite('iz233_10', 4)	# 24-27
    Recovery()
    Unknown2063()
    sprite('iz233_11', 4)	# 28-31
    sprite('iz233_12', 4)	# 32-35
    sprite('iz233_13', 4)	# 36-39
    sprite('iz233_14', 2)	# 40-41

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(85)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(6000)
        AirPushbackY(18000)
        AirUntechableTime(40)
        Unknown2004(1, 0)
    sprite('iz236_00', 3)	# 1-3
    sprite('iz236_01', 3)	# 4-6
    sprite('iz236_02', 3)	# 7-9
    SFX_0('001_airbackdash_0')
    sprite('iz236_03', 3)	# 10-12	 **attackbox here**
    Unknown7007('62697a3130375f3000000000000000006400000062697a3130375f3100000000000000006400000062697a3130375f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1015(40000)
    GFX_0('Kakusei3CAura', 0)
    sprite('iz236_04', 2)	# 13-14	 **attackbox here**
    GFX_0('Kakusei3CAuraFire', 0)
    GFX_1('izef_Drivelight_side', 0)
    SFX_0('004_swing_grap_1_2')
    sprite('iz236_05', 2)	# 15-16	 **attackbox here**
    sprite('iz236_04', 2)	# 17-18	 **attackbox here**
    GFX_1('izef_Drivelight_side', 0)
    Unknown1019(90)
    sprite('iz236_06', 3)	# 19-21
    Recovery()
    Unknown2063()
    Unknown21015('4b616b75736569334341757261000000000000000000000000000000000000006500000000000000')
    Unknown21015('4b616b75736569334341757261466972650000000000000000000000000000006600000000000000')
    Unknown1019(60)
    sprite('iz236_07', 3)	# 22-24
    Unknown1019(40)
    sprite('iz236_08', 3)	# 25-27
    Unknown1019(20)
    sprite('iz236_09', 3)	# 28-30
    sprite('iz236_10', 3)	# 31-33
    sprite('iz236_11', 2)	# 34-35
    sprite('iz236_12', 2)	# 36-37
    sprite('iz236_13', 2)	# 38-39

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1300)
        hitstun(19)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('iz255_00', 2)	# 1-2
    sprite('iz255_01', 2)	# 3-4
    sprite('iz255_02', 2)	# 5-6
    Unknown7009(3)
    sprite('iz255_03', 2)	# 7-8
    SFX_0('003_swing_grap_0_1')
    sprite('iz255_04', 3)	# 9-11	 **attackbox here**
    sprite('iz255_05', 3)	# 12-14	 **attackbox here**
    sprite('iz255_05', 3)	# 15-17	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('iz255_06', 6)	# 18-23
    sprite('iz255_07', 6)	# 24-29

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1300)
        hitstun(19)
        AirUntechableTime(21)
        AirPushbackX(8000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('iz251_00', 2)	# 1-2
    sprite('iz251_01', 1)	# 3-3
    sprite('iz251_01', 1)	# 4-4
    Unknown7009(3)
    SFX_0('004_swing_grap_1_2')
    sprite('iz251_02', 2)	# 5-6
    sprite('iz251_03', 3)	# 7-9	 **attackbox here**
    sprite('iz251_04', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('iz251_05', 3)	# 13-15
    sprite('iz251_06', 3)	# 16-18
    sprite('iz251_07', 3)	# 19-21

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1800)
        blockstun(16)
        Unknown9016(1)
        PushbackX(19800)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('iz253_00', 2)	# 1-2
    sprite('iz253_01', 2)	# 3-4
    sprite('iz253_02', 2)	# 5-6
    sprite('iz253_03', 2)	# 7-8
    SFX_3('izse_08')
    SFX_0('008_swing_pole_2')
    Unknown7009(5)
    sprite('iz253_04', 2)	# 9-10
    sprite('iz253_05', 2)	# 11-12	 **attackbox here**
    SFX_0('019_cloth_a')
    sprite('iz253_06', 5)	# 13-17	 **attackbox here**
    sprite('iz253_07', 3)	# 18-20	 **attackbox here**
    Recovery()
    Unknown2063()
    GFX_1('izef_fire', 0)
    GFX_1('izef_fire', 1)
    GFX_1('izef_fire_dust', 2)
    GFX_1('izef_fire_dust', 3)
    sprite('iz253_08', 3)	# 21-23	 **attackbox here**
    sprite('iz253_09', 3)	# 24-26	 **attackbox here**
    sprite('iz253_10', 3)	# 27-29	 **attackbox here**
    sprite('iz253_11', 3)	# 30-32
    sprite('iz253_12', 3)	# 33-35
    sprite('iz253_13', 3)	# 36-38

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirUntechableTime(40)
        blockstun(16)
        AirPushbackX(19800)
        AirPushbackY(-30000)
        AttackP2(75)
        Unknown9016(1)
        PushbackX(19800)
        HitOrBlockJumpCancel(1)
        Unknown11001(0, 2, 7)
    sprite('iz252_00', 3)	# 1-3
    sprite('iz252_01', 2)	# 4-5
    sprite('iz252_02', 2)	# 6-7
    SFX_3('izse_01')
    SFX_0('008_swing_pole_2')
    Unknown7009(4)
    sprite('iz252_03', 3)	# 8-10
    GFX_0('AIR5CZanzo', 0)
    sprite('iz252_04', 3)	# 11-13	 **attackbox here**
    sprite('iz252_05', 3)	# 14-16	 **attackbox here**
    SFX_0('019_cloth_a')
    sprite('iz252_06', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('iz252_07', 3)	# 20-22
    sprite('iz252_08', 3)	# 23-25
    sprite('iz252_09', 3)	# 26-28
    sprite('iz252_10', 3)	# 29-31
    sprite('iz252_11', 3)	# 32-34

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
    sprite('iz211_00', 3)	# 1-3
    sprite('iz211_01', 3)	# 4-6
    Unknown7007('62697a3135365f3000000000000000006400000062697a3135365f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('iz211_02', 2)	# 7-8
    SFX_0('004_swing_grap_1_1')
    physicsXImpulse(8500)
    physicsYImpulse(17000)
    setGravity(1800)
    sprite('iz211_03', 3)	# 9-11
    sprite('iz211_04', 2)	# 12-13
    sprite('iz211_05', 2)	# 14-15
    sprite('iz211_06', 2)	# 16-17
    sprite('iz211_07', 2)	# 18-19
    sprite('iz211_08', 2)	# 20-21
    SFX_0('006_swing_blade_2')
    sprite('iz211_09', 3)	# 22-24	 **attackbox here**
    GFX_0('6BZanzo', -1)
    sprite('iz211_10', 32767)	# 25-32791
    sendToLabelUpon(2, 0)
    label(0)
    sprite('iz211_11', 3)	# 32792-32794
    Unknown1019(25)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz211_12', 3)	# 32795-32797
    Unknown1019(0)
    sprite('iz211_13', 3)	# 32798-32800
    sprite('iz211_14', 4)	# 32801-32804
    sprite('iz211_15', 4)	# 32805-32808
    sprite('iz211_16', 3)	# 32809-32811

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 16)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('iz211_10', 32767)	# 1-32767
    label(1)
    sprite('iz211_11', 3)	# 32768-32770
    clearUponHandler(2)
    Unknown1019(25)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz211_12', 3)	# 32771-32773
    Unknown1084(1)
    sprite('iz211_13', 3)	# 32774-32776
    sprite('iz211_14', 2)	# 32777-32778
    sprite('iz211_15', 2)	# 32779-32780
    sprite('iz211_16', 2)	# 32781-32782
    label(2)
    sprite('iz202_00', 5)	# 32783-32787
    clearUponHandler(17)
    teleportRelativeY(0)
    sprite('iz202_01', 3)	# 32788-32790
    sprite('iz202_02', 3)	# 32791-32793
    SFX_3('izse_01')
    sprite('iz202_03', 2)	# 32794-32795
    GFX_0('5CZanzo', 0)
    SFX_0('008_swing_pole_2')
    sprite('iz202_04', 3)	# 32796-32798	 **attackbox here**
    tag_voice(1, 'biz157_0', 'biz157_1', '', '')
    sprite('iz202_05', 3)	# 32799-32801	 **attackbox here**
    sprite('iz202_06', 2)	# 32802-32803	 **attackbox here**
    sprite('iz202_07', 3)	# 32804-32806
    sprite('iz202_08', 3)	# 32807-32809
    sprite('iz202_09', 3)	# 32810-32812
    sprite('iz202_10', 3)	# 32813-32815
    sprite('iz202_11', 3)	# 32816-32818
    sprite('iz202_12', 3)	# 32819-32821
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('iz000_00', 7)	# 32822-32828	 **attackbox here**
    sprite('iz000_01', 7)	# 32829-32835	 **attackbox here**
    sprite('iz000_02', 7)	# 32836-32842	 **attackbox here**
    sprite('iz000_03', 7)	# 32843-32849	 **attackbox here**
    sprite('iz000_04', 7)	# 32850-32856	 **attackbox here**
    sprite('iz000_05', 7)	# 32857-32863	 **attackbox here**
    sprite('iz000_06', 7)	# 32864-32870	 **attackbox here**
    sprite('iz000_07', 7)	# 32871-32877	 **attackbox here**
    sprite('iz000_08', 7)	# 32878-32884	 **attackbox here**
    sprite('iz000_09', 7)	# 32885-32891	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 32892-32892

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('iz213_00', 1)	# 1-1
    sprite('iz213_01', 1)	# 2-2
    sprite('iz213_02', 2)	# 3-4
    physicsXImpulse(10000)
    SFX_0('001_airbackdash_0')
    sprite('iz213_03', 2)	# 5-6
    SFX_3('izse_08')
    sprite('iz213_04', 2)	# 7-8
    sprite('iz213_05', 2)	# 9-10
    sprite('iz213_06', 2)	# 11-12
    Unknown1019(0)
    sprite('iz213_07', 2)	# 13-14	 **attackbox here**
    SFX_0('008_swing_pole_2')
    sprite('iz213_08', 3)	# 15-17	 **attackbox here**
    sprite('iz213_09', 3)	# 18-20	 **attackbox here**
    GFX_1('izef_fire', 0)
    GFX_1('izef_fire_dust', 1)
    GFX_1('izef_fire_dust', 2)
    GFX_1('izef_fire_dust', 3)
    sprite('iz213_10', 2)	# 21-22	 **attackbox here**
    sprite('iz213_11', 2)	# 23-24
    sprite('iz213_12', 2)	# 25-26
    sprite('iz213_13', 2)	# 27-28
    sprite('iz213_14', 2)	# 29-30
    sprite('iz213_15', 2)	# 31-32
    sprite('iz213_16', 1)	# 33-33
    sprite('iz213_17', 1)	# 34-34
    label(0)
    sprite('iz000_00', 7)	# 35-41	 **attackbox here**
    sprite('iz000_01', 7)	# 42-48	 **attackbox here**
    sprite('iz000_02', 7)	# 49-55	 **attackbox here**
    sprite('iz000_03', 7)	# 56-62	 **attackbox here**
    sprite('iz000_04', 7)	# 63-69	 **attackbox here**
    sprite('iz000_05', 7)	# 70-76	 **attackbox here**
    sprite('iz000_06', 7)	# 77-83	 **attackbox here**
    sprite('iz000_07', 7)	# 84-90	 **attackbox here**
    sprite('iz000_08', 7)	# 91-97	 **attackbox here**
    sprite('iz000_09', 7)	# 98-104	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 105-105

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('iz402_00', 3)	# 1-3
    Unknown3029(1)
    sprite('iz402_01', 3)	# 4-6
    sprite('iz402_02', 2)	# 7-8
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    sprite('iz402_03', 4)	# 9-12
    sprite('iz402_04', 4)	# 13-16
    sprite('iz404_00', 1)	# 17-17
    sprite('iz404_01', 2)	# 18-19
    Unknown7015()
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo_AntiAirA', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    sprite('iz404_02', 3)	# 20-22	 **attackbox here**
    tag_voice(0, 'biz158_0', 'biz158_1', '', '')
    sprite('iz404_03', 5)	# 23-27
    sprite('iz404_04', 5)	# 28-32
    sprite('iz404_05', 5)	# 33-37
    sprite('iz404_06', 5)	# 38-42
    sprite('iz404_07', 6)	# 43-48
    sprite('iz404_08', 6)	# 49-54
    sprite('iz404_09', 6)	# 55-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('iz000_00', 7)	# 1-7	 **attackbox here**
    sprite('iz000_01', 7)	# 8-14	 **attackbox here**
    sprite('iz000_02', 7)	# 15-21	 **attackbox here**
    sprite('iz000_03', 7)	# 22-28	 **attackbox here**
    sprite('iz000_04', 7)	# 29-35	 **attackbox here**
    sprite('iz000_05', 7)	# 36-42	 **attackbox here**
    sprite('iz000_06', 7)	# 43-49	 **attackbox here**
    sprite('iz000_07', 7)	# 50-56	 **attackbox here**
    sprite('iz000_08', 7)	# 57-63	 **attackbox here**
    sprite('iz000_09', 7)	# 64-70	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz402_00', 3)	# 71-73
    Unknown3029(1)
    sprite('iz402_01', 3)	# 74-76
    sprite('iz402_02', 2)	# 77-78
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    sprite('iz402_03', 4)	# 79-82
    sprite('iz402_04', 4)	# 83-86
    sprite('iz404_00', 1)	# 87-87
    sprite('iz404_01', 2)	# 88-89
    Unknown7015()
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo_AntiAirA', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    sprite('iz404_02', 3)	# 90-92	 **attackbox here**
    tag_voice(0, 'biz158_0', 'biz158_1', '', '')
    sprite('iz404_03', 5)	# 93-97
    sprite('iz404_04', 5)	# 98-102
    sprite('iz404_05', 5)	# 103-107
    sprite('iz404_06', 5)	# 108-112
    sprite('iz404_07', 6)	# 113-118
    sprite('iz404_08', 6)	# 119-124
    sprite('iz404_09', 6)	# 125-130

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 14)	# 1-14
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 15-15
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-300000)
    Unknown1007(400000)
    setGravity(0)
    sprite('iz406_00', 3)	# 16-18
    GFX_0('Iai_AntiAir_Next_406F', -1)
    GFX_0('Iai_AntiAir_Next_406B', -1)
    Unknown3001(0)
    Unknown3004(30)
    StartMultihit()
    SFX_0('airdash_l')
    SFX_0('slash_pole_middle')
    physicsYImpulse(-6500)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('iz406_01', 4)	# 19-22
    Unknown23119(2148384, 10, 2)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setGravity(0)
    physicsYImpulse(2000)
    sprite('iz406_02', 4)	# 23-26
    sprite('iz406_03', 4)	# 27-30
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_04', 4)	# 31-34
    sprite('iz406_05', 4)	# 35-38	 **attackbox here**
    sprite('iz406_06', 3)	# 39-41	 **attackbox here**
    StartMultihit()
    SFX_3('izse_01')
    physicsYImpulse(-80000)
    setGravity(7000)
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    label(0)
    sprite('iz406_06', 3)	# 42-44	 **attackbox here**
    sprite('iz406_07', 3)	# 45-47	 **attackbox here**
    sprite('iz406_08', 3)	# 48-50	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('iz406_09', 5)	# 51-55	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    Unknown1084(1)
    sprite('iz406_10', 9)	# 56-64	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_11', 3)	# 65-67
    sprite('iz406_12', 5)	# 68-72
    sprite('iz406_13', 5)	# 73-77
    sprite('iz000_00', 7)	# 78-84	 **attackbox here**
    sprite('iz000_01', 7)	# 85-91	 **attackbox here**
    sprite('iz000_02', 7)	# 92-98	 **attackbox here**
    sprite('iz000_03', 7)	# 99-105	 **attackbox here**
    sprite('iz000_04', 7)	# 106-112	 **attackbox here**
    sprite('iz000_05', 7)	# 113-119	 **attackbox here**
    sprite('iz000_06', 7)	# 120-126	 **attackbox here**
    sprite('iz000_07', 7)	# 127-133	 **attackbox here**
    sprite('iz000_08', 7)	# 134-140	 **attackbox here**
    sprite('iz000_09', 7)	# 141-147	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('iz210_00', 2)	# 1-2
    sprite('iz210_01', 2)	# 3-4
    sprite('iz210_01', 2)	# 5-6
    sprite('iz210_02', 2)	# 7-8
    sprite('iz210_03', 3)	# 9-11
    SFX_0('006_swing_blade_1')
    sprite('iz210_04', 1)	# 12-12	 **attackbox here**
    GFX_0('6AZanzo', -1)
    sprite('iz210_04', 2)	# 13-14	 **attackbox here**
    sprite('iz210_05', 3)	# 15-17	 **attackbox here**
    sprite('iz210_06', 3)	# 18-20	 **attackbox here**
    sprite('iz210_07', 3)	# 21-23	 **attackbox here**
    sprite('iz210_08', 3)	# 24-26	 **attackbox here**
    sprite('iz210_09', 3)	# 27-29	 **attackbox here**
    sprite('iz210_10', 3)	# 30-32	 **attackbox here**
    sprite('iz210_11', 3)	# 33-35	 **attackbox here**
    sprite('iz000_00', 7)	# 36-42	 **attackbox here**
    sprite('iz000_01', 7)	# 43-49	 **attackbox here**
    sprite('iz000_02', 7)	# 50-56	 **attackbox here**
    sprite('iz000_03', 7)	# 57-63	 **attackbox here**
    sprite('iz000_04', 7)	# 64-70	 **attackbox here**
    sprite('iz000_05', 7)	# 71-77	 **attackbox here**
    sprite('iz000_06', 7)	# 78-84	 **attackbox here**
    sprite('iz000_07', 7)	# 85-91	 **attackbox here**
    sprite('iz000_08', 7)	# 92-98	 **attackbox here**
    sprite('iz000_09', 7)	# 99-105	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
    sprite('iz402_00', 3)	# 1-3
    Unknown3029(1)
    sprite('iz402_01', 3)	# 4-6
    sprite('iz402_02', 2)	# 7-8
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    sprite('iz402_03', 4)	# 9-12
    sprite('iz402_04', 4)	# 13-16
    sprite('iz404_00', 1)	# 17-17
    sprite('iz404_01', 2)	# 18-19
    Unknown7015()
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo_AntiAirA', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    sprite('iz404_02', 3)	# 20-22	 **attackbox here**
    sprite('iz404_03', 5)	# 23-27
    sprite('iz404_04', 5)	# 28-32
    sprite('iz404_05', 5)	# 33-37
    sprite('iz404_06', 5)	# 38-42
    sprite('iz404_07', 6)	# 43-48
    sprite('iz404_08', 6)	# 49-54
    sprite('iz404_09', 6)	# 55-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('iz000_00', 7)	# 1-7	 **attackbox here**
    sprite('iz000_01', 7)	# 8-14	 **attackbox here**
    sprite('iz000_02', 7)	# 15-21	 **attackbox here**
    sprite('iz000_03', 7)	# 22-28	 **attackbox here**
    sprite('iz000_04', 7)	# 29-35	 **attackbox here**
    sprite('iz000_05', 7)	# 36-42	 **attackbox here**
    sprite('iz000_06', 7)	# 43-49	 **attackbox here**
    sprite('iz000_07', 7)	# 50-56	 **attackbox here**
    sprite('iz000_08', 7)	# 57-63	 **attackbox here**
    sprite('iz000_09', 7)	# 64-70	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz402_00', 3)	# 71-73
    Unknown3029(1)
    sprite('iz402_01', 3)	# 74-76
    sprite('iz402_02', 2)	# 77-78
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    sprite('iz402_03', 4)	# 79-82
    sprite('iz402_04', 4)	# 83-86
    sprite('iz404_00', 1)	# 87-87
    sprite('iz404_01', 2)	# 88-89
    Unknown7015()
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo_AntiAirA', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    sprite('iz404_02', 3)	# 90-92	 **attackbox here**
    sprite('iz404_03', 5)	# 93-97
    sprite('iz404_04', 5)	# 98-102
    sprite('iz404_05', 5)	# 103-107
    sprite('iz404_06', 5)	# 108-112
    sprite('iz404_07', 6)	# 113-118
    sprite('iz404_08', 6)	# 119-124
    sprite('iz404_09', 6)	# 125-130

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
    sprite('iz032_00', 3)	# 1-3
    sprite('iz032_00', 4)	# 4-7
    sprite('iz032_01', 4)	# 8-11	 **attackbox here**
    label(0)
    sprite('iz032_02', 4)	# 12-15	 **attackbox here**
    sprite('iz032_03', 4)	# 16-19	 **attackbox here**
    sprite('iz032_04', 4)	# 20-23	 **attackbox here**
    Unknown8006(100, 1, 1)
    sprite('iz032_05', 4)	# 24-27	 **attackbox here**
    sprite('iz032_06', 4)	# 28-31	 **attackbox here**
    sprite('iz032_07', 4)	# 32-35	 **attackbox here**
    sprite('iz032_08', 4)	# 36-39	 **attackbox here**
    sprite('iz032_09', 4)	# 40-43
    Unknown8006(100, 1, 1)
    sprite('iz032_10', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz310_00', 1)	# 48-48
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('iz310_01', 2)	# 49-50
    SFX_0('010_swing_sword_0')
    sprite('iz310_02', 3)	# 51-53	 **attackbox here**
    Unknown1084(1)
    sprite('iz310_02', 3)	# 54-56	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('iz310_03', 3)	# 57-59	 **attackbox here**
    SFX_4('biz154')
    sprite('iz310_04', 5)	# 60-64	 **attackbox here**
    sprite('iz310_05', 6)	# 65-70	 **attackbox here**
    sprite('iz310_06', 3)	# 71-73	 **attackbox here**
    sprite('iz310_07', 3)	# 74-76

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        Hitstop(0)
        AttackP2(100)
        Unknown11001(0, 12, 12)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(100)
        Unknown9142(80)
        Unknown9016(1)
        hitstun(200)
        PushbackX(0)
        JumpCancel_(0)
        Unknown2004(1, 0)
        Unknown11069('ThrowExe')
    sprite('iz310_02ex00', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    GFX_0('ThrowLock_MagicCircle', 1)
    GFX_0('ThrowFunnel', -1)
    StartMultihit()
    Unknown5003(1)
    sprite('iz311_00', 4)	# 4-7	 **attackbox here**
    SFX_4('biz153')
    sprite('iz311_01', 4)	# 8-11	 **attackbox here**
    physicsXImpulse(-30000)
    sprite('iz311_02', 4)	# 12-15	 **attackbox here**
    Unknown1019(40)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz311_03', 6)	# 16-21	 **attackbox here**
    Unknown1019(25)
    sprite('iz311_04', 6)	# 22-27	 **attackbox here**
    Unknown1019(0)
    sprite('iz311_05', 3)	# 28-30
    Unknown21015('5468726f7746756e6e656c0000000000000000000000000000000000000000002d01000000000000')
    EnableCollision(1)
    Unknown1015(48000)
    Unknown2015(250)
    sprite('iz311_06', 1)	# 31-31	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    AttackLevel_(4)
    Damage(2000)
    AttackP1(100)
    AttackP2(50)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(80000)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(500)
    Unknown9178(1)
    WallbounceReboundTime(25)
    Unknown9346(0)
    AirUntechableTime(60)
    Unknown9016(1)
    Unknown11069('')
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown21015('5468726f774c6f636b5f4d61676963436972636c6500000000000000000000002e01000000000000')
    sprite('iz311_06', 13)	# 32-44	 **attackbox here**
    JumpCancel_(1)
    sprite('iz311_07', 4)	# 45-48	 **attackbox here**
    sprite('iz311_08', 4)	# 49-52
    sprite('iz311_09', 4)	# 53-56
    sprite('iz311_10', 4)	# 57-60
    sprite('iz311_11', 4)	# 61-64
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
    sprite('iz032_00', 3)	# 1-3
    sprite('iz032_00', 4)	# 4-7
    sprite('iz032_01', 4)	# 8-11	 **attackbox here**
    label(0)
    sprite('iz032_02', 4)	# 12-15	 **attackbox here**
    sprite('iz032_03', 4)	# 16-19	 **attackbox here**
    sprite('iz032_04', 4)	# 20-23	 **attackbox here**
    Unknown8006(100, 1, 1)
    sprite('iz032_05', 4)	# 24-27	 **attackbox here**
    sprite('iz032_06', 4)	# 28-31	 **attackbox here**
    sprite('iz032_07', 4)	# 32-35	 **attackbox here**
    sprite('iz032_08', 4)	# 36-39	 **attackbox here**
    sprite('iz032_09', 4)	# 40-43
    Unknown8006(100, 1, 1)
    sprite('iz032_10', 4)	# 44-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz310_00', 1)	# 48-48
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('iz310_01', 2)	# 49-50
    SFX_0('010_swing_sword_0')
    sprite('iz310_02', 3)	# 51-53	 **attackbox here**
    Unknown1084(1)
    sprite('iz310_02', 3)	# 54-56	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('iz310_03', 3)	# 57-59	 **attackbox here**
    SFX_4('biz154')
    sprite('iz310_04', 5)	# 60-64	 **attackbox here**
    sprite('iz310_05', 6)	# 65-70	 **attackbox here**
    sprite('iz310_06', 3)	# 71-73	 **attackbox here**
    sprite('iz310_07', 3)	# 74-76

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        Hitstop(0)
        AttackP2(100)
        Unknown11001(0, 12, 12)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(100)
        Unknown9142(80)
        Unknown9016(1)
        hitstun(200)
        PushbackX(0)
        JumpCancel_(0)
        Unknown2004(1, 0)
        AirPushbackX(-32000)
        AirPushbackY(0)
        PushbackX(-32000)
        Hitstop(0)
        AirUntechableTime(48)
        JumpCancel_(0)
        Unknown13021(1)
        Unknown21005(1)
        Unknown2004(1, 0)
        Unknown11069('BackThrowExe')
    sprite('iz310_02ex00', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    StartMultihit()
    GFX_0('ThrowLock_MagicCircle', 1)
    GFX_0('ThrowFunnel', -1)
    Unknown5003(1)
    sprite('iz311_00', 4)	# 4-7	 **attackbox here**
    SFX_4('biz153')
    sprite('iz311_01', 4)	# 8-11	 **attackbox here**
    sprite('iz311_02', 4)	# 12-15	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('iz313_00', 3)	# 16-18
    sprite('iz313_01', 4)	# 19-22
    physicsXImpulse(60000)
    sprite('iz313_02', 4)	# 23-26
    teleportRelativeX(100000)
    Unknown1019(40)
    GFX_1('ef_hitmd', 0)
    sprite('iz313_03', 4)	# 27-30
    Unknown1019(30)
    sprite('iz313_04', 3)	# 31-33
    Unknown1019(20)
    sprite('iz311_04', 6)	# 34-39	 **attackbox here**
    Unknown1019(0)
    Unknown2006()
    sprite('iz311_05', 3)	# 40-42
    Unknown21015('5468726f7746756e6e656c0000000000000000000000000000000000000000002d01000000000000')
    EnableCollision(1)
    Unknown2006()
    Unknown1015(48000)
    Unknown2015(250)
    sprite('iz311_06', 1)	# 43-43	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    AttackLevel_(4)
    Damage(2000)
    AttackP1(100)
    AttackP2(50)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(80000)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(500)
    Unknown9178(1)
    WallbounceReboundTime(25)
    Unknown9346(0)
    AirUntechableTime(60)
    Unknown9202(10)
    Unknown9016(1)
    Unknown21015('5468726f774c6f636b5f4d61676963436972636c6500000000000000000000002e01000000000000')
    Unknown11069('')
    sprite('iz311_06', 13)	# 44-56	 **attackbox here**
    JumpCancel_(1)
    sprite('iz311_07', 4)	# 57-60	 **attackbox here**
    sprite('iz311_08', 4)	# 61-64
    sprite('iz311_09', 4)	# 65-68
    sprite('iz311_10', 4)	# 69-72
    sprite('iz311_11', 4)	# 73-76
    SFX_FOOTSTEP_(100, 1, 1)

@State
def SpDashF_Land():

    def upon_IMMEDIATE():
        Unknown17015()

        def upon_CLEAR_OR_EXIT():
            if (SLOT_12 > 79200):
                SLOT_12 = 79200
            if SLOT_2:
                Unknown13014(1)
                Unknown13015(1)
                if (not CheckInput(0x79)):
                    sendToLabel(1)
                if CheckInput(0x9f):
                    if (not (SLOT_13 >= 20000)):
                        Unknown1021(500)
                if CheckInput(0x51):
                    Unknown1021(-500)

        def upon_STATE_END():
            if (not SLOT_30):
                Unknown1019(60)
                YAccel(50)
                Unknown1043()
        Unknown1084(1)
        Unknown22004(5, 1)
    sprite('iz350_00', 2)	# 1-2
    sprite('iz350_01', 2)	# 3-4	 **attackbox here**
    SFX_3('izse_02')
    sprite('iz350_02', 2)	# 5-6	 **attackbox here**
    GFX_0('HoverDashAura', 0)
    GFX_1('izef_Drivelight', 1)
    physicsXImpulse(28800)
    physicsYImpulse(10000)
    Unknown1028(960)
    sprite('iz350_03', 2)	# 7-8	 **attackbox here**
    sprite('iz350_04', 1)	# 9-9	 **attackbox here**
    sprite('iz350_04', 1)	# 10-10	 **attackbox here**
    sprite('iz350_05', 1)	# 11-11	 **attackbox here**
    GFX_1('izef_Drivelight', 0)
    Unknown2037(1)
    sprite('iz350_05', 1)	# 12-12	 **attackbox here**
    sprite('iz350_02', 2)	# 13-14	 **attackbox here**
    sprite('iz350_03', 2)	# 15-16	 **attackbox here**
    sprite('iz350_04', 2)	# 17-18	 **attackbox here**
    GFX_1('izef_Drivelight', 0)
    sprite('iz350_05', 2)	# 19-20	 **attackbox here**
    sprite('iz350_02', 2)	# 21-22	 **attackbox here**
    sprite('iz350_03', 2)	# 23-24	 **attackbox here**
    GFX_1('izef_Drivelight', 0)
    sprite('iz350_04', 2)	# 25-26	 **attackbox here**
    sprite('iz350_05', 2)	# 27-28	 **attackbox here**
    sprite('iz350_02', 2)	# 29-30	 **attackbox here**
    label(1)
    sprite('iz350_06', 4)	# 31-34	 **attackbox here**
    clearUponHandler(3)
    Unknown1028(0)
    Unknown21015('486f7665724461736841757261000000000000000000000000000000000000009101000000000000')
    GFX_1('izef_Drivelight', 0)

@State
def SpDashF_Air():

    def upon_IMMEDIATE():
        Unknown17015()

        def upon_CLEAR_OR_EXIT():
            if (SLOT_12 > 79200):
                SLOT_12 = 79200
            if SLOT_2:
                Unknown13014(1)
                Unknown13015(1)
                Unknown13011(1)
                Unknown13012(1)
                if (not CheckInput(0x79)):
                    sendToLabel(1)
                if CheckInput(0x9f):
                    if (not (SLOT_13 >= 3000)):
                        Unknown1021(500)
                if CheckInput(0x51):
                    Unknown1021(-500)

        def upon_STATE_END():
            SLOT_10 = 0
            if (not SLOT_30):
                Unknown1019(60)
                YAccel(50)
                Unknown1043()
        physicsXImpulse(0)
        setGravity(0)
        Unknown1045(0)
        Unknown22004(5, 1)
        WhiffCancel('NmlAtkAIR5A')
    sprite('iz350_06', 3)	# 1-3	 **attackbox here**
    if (SLOT_23 <= 125000):
        if SLOT_10:
            Unknown1084(1)
        else:
            physicsYImpulse(31000)
    sprite('iz350_02', 3)	# 4-6	 **attackbox here**
    SFX_3('izse_02')
    GFX_0('HoverDashAura', 0)
    GFX_1('izef_Drivelight', 1)
    physicsXImpulse(21600)
    physicsYImpulse(-6000)
    Unknown1028(960)
    sprite('iz350_03', 2)	# 7-8	 **attackbox here**
    sprite('iz350_04', 2)	# 9-10	 **attackbox here**
    Unknown14070('NmlAtkAIR5A')
    sprite('iz350_05', 1)	# 11-11	 **attackbox here**
    GFX_1('izef_Drivelight', 0)
    sprite('iz350_05', 1)	# 12-12	 **attackbox here**
    WhiffCancelEnable(1)
    Unknown14072('NmlAtkAIR5A')
    Unknown2037(1)
    sprite('iz350_02', 2)	# 13-14	 **attackbox here**
    sprite('iz350_03', 2)	# 15-16	 **attackbox here**
    sprite('iz350_04', 2)	# 17-18	 **attackbox here**
    GFX_1('izef_Drivelight', 0)
    sprite('iz350_05', 2)	# 19-20	 **attackbox here**
    sprite('iz350_02', 2)	# 21-22	 **attackbox here**
    sprite('iz350_03', 2)	# 23-24	 **attackbox here**
    GFX_1('izef_Drivelight', 0)
    sprite('iz350_04', 2)	# 25-26	 **attackbox here**
    sprite('iz350_05', 2)	# 27-28	 **attackbox here**
    sprite('iz350_02', 2)	# 29-30	 **attackbox here**
    GFX_1('izef_Drivelight', 0)
    sprite('iz350_03', 2)	# 31-32	 **attackbox here**
    sprite('iz350_04', 2)	# 33-34	 **attackbox here**
    sprite('iz350_05', 2)	# 35-36	 **attackbox here**
    label(1)
    sprite('iz350_06', 4)	# 37-40	 **attackbox here**
    clearUponHandler(3)
    Unknown1028(0)
    Unknown21015('486f7665724461736841757261000000000000000000000000000000000000009101000000000000')
    GFX_1('izef_Drivelight', 0)

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(3)
        Damage(1800)
        AttackP1(80)
        AttackP2(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(45000)
        AirUntechableTime(45)
        Hitstop(6)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown3069(2)
        Unknown3071(5)
        Unknown3076(1010)
        Unknown3077(1010)

        def upon_78():
            SLOT_51 = 1

        def upon_STATE_END():
            Unknown7015()
    sprite('iz405_00', 3)	# 1-3
    Unknown3029(1)
    sprite('iz405_01', 2)	# 4-5
    sprite('iz405_02', 2)	# 6-7
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    sprite('iz405_03', 3)	# 8-10
    SFX_3('izse_03_start')
    sprite('iz405_04', 3)	# 11-13
    tag_voice(1, 'biz206_1', 'biz206_2', 'biz206_1', 'biz206_0')
    Unknown7015()
    SFX_3('izse_01')
    Unknown14070('AN_CmnActInvincibleAttack_Next')
    sprite('iz405_05', 3)	# 14-16	 **attackbox here**
    GFX_0('Iai_SlashZanzo_AntiAirB', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    sprite('iz405_06', 4)	# 17-20
    if SLOT_51:
        Unknown14072('AN_CmnActInvincibleAttack_Next')
    setInvincible(0)
    Unknown14077(1)
    sprite('iz405_07', 4)	# 21-24
    sprite('iz405_08', 4)	# 25-28
    sprite('iz405_09', 15)	# 29-43
    Unknown14074('AN_CmnActInvincibleAttack_Next')
    sprite('iz405_10', 3)	# 44-46
    Unknown3029(0)
    sprite('iz405_11', 4)	# 47-50
    sprite('iz405_12', 4)	# 51-54
    sprite('iz405_13', 4)	# 55-58
    sprite('iz405_14', 4)	# 59-62

@State
def AN_CmnActInvincibleAttack_Next():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        AttackLevel_(4)
        Damage(1300)
        AttackP1(48)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(-60000)
        AirUntechableTime(100)
        Unknown11001(0, 6, 6)
        Hitstop(2)
        Unknown9118(14)
        Unknown9190(1)
        Unknown14083(0)
        Unknown9016(1)
        Unknown2004(1, 0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown30068(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        Unknown2003(1)
        Unknown1084(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('keep', 1)	# 1-1
    sprite('iz405_07', 2)	# 2-3
    GFX_0('Iai_AntiAir_Next_405F', -1)
    GFX_0('Iai_AntiAir_Next_405B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz405_08', 2)	# 4-5
    SFX_3('izse_04')
    sprite('iz405_09', 2)	# 6-7
    sprite('iz406_00', 1)	# 8-8
    Unknown3004(30)
    EnableCollision(0)
    Unknown2006()
    Unknown1086(22)
    Unknown1007(160000)
    teleportRelativeX(-60000)
    sprite('iz406_00', 3)	# 9-11
    GFX_0('Iai_AntiAir_Next_406F', -1)
    GFX_0('Iai_AntiAir_Next_406B', -1)
    Unknown3001(0)
    Unknown3004(30)
    sprite('iz406_01', 4)	# 12-15
    Unknown23119(2148384, 10, 2)
    setGravity(0)
    physicsYImpulse(2000)
    sprite('iz406_02', 4)	# 16-19
    sprite('iz406_03', 4)	# 20-23
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_04', 4)	# 24-27
    sprite('iz406_05', 4)	# 28-31	 **attackbox here**
    sprite('iz406_06', 3)	# 32-34	 **attackbox here**
    tag_voice(0, 'biz208_0', 'biz208_1', 'biz208_2', '')
    Unknown2003(0)
    SFX_3('izse_01')
    physicsYImpulse(-80000)
    setGravity(7000)
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    label(0)
    sprite('iz406_06', 3)	# 35-37	 **attackbox here**
    sprite('iz406_07', 3)	# 38-40	 **attackbox here**
    sprite('iz406_08', 3)	# 41-43	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('iz406_09', 5)	# 44-48	 **attackbox here**
    setInvincible(0)
    EnableCollision(1)
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    Unknown1084(1)
    Recovery()
    sprite('iz406_10', 9)	# 49-57	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_11', 7)	# 58-64
    sprite('iz406_12', 5)	# 65-69
    sprite('iz406_13', 5)	# 70-74
    ExitState()

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(3)
        Damage(1800)
        Unknown11089(-1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(46)
        AirPushbackX(16000)
        AirPushbackY(45000)
        Unknown9016(1)
        clearUponHandler(2)

        def upon_LANDING():
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)

        def upon_78():
            SLOT_51 = 1
        Unknown3069(2)
        Unknown3071(5)
        Unknown3076(1010)
        Unknown3077(1010)
    sprite('iz408_00', 3)	# 1-3
    physicsYImpulse(0)
    setGravity(0)
    Unknown1019(60)
    sprite('iz408_01', 3)	# 4-6
    tag_voice(1, 'biz207_0', 'biz207_1', 'biz207_2', '')
    sprite('iz408_02', 3)	# 7-9
    SFX_0('slash_pole_slow')
    SFX_3('izse_01')
    Unknown14070('AN_CmnActInvincibleAttackAir_Ne')
    sprite('iz408_03', 2)	# 10-11	 **attackbox here**
    GFX_0('AirAssaultZanzo', -1)
    Unknown1015(3000)
    Unknown1021(3000)
    sprite('iz408_04', 3)	# 12-14	 **attackbox here**
    physicsXImpulse(-7500)
    physicsYImpulse(20000)
    Unknown1044()
    sprite('iz408_05', 3)	# 15-17
    setInvincible(0)
    if SLOT_51:
        Unknown14072('AN_CmnActInvincibleAttackAir_Ne')
    Unknown1021(7000)
    sprite('iz408_06', 3)	# 18-20
    sprite('iz408_07', 3)	# 21-23
    sprite('iz408_08', 3)	# 24-26
    sprite('iz408_09', 3)	# 27-29
    Unknown14074('AN_CmnActInvincibleAttackAir_Ne')
    sprite('iz408_10', 3)	# 30-32
    sprite('iz408_11', 3)	# 33-35
    sprite('iz408_12', 3)	# 36-38
    label(0)
    sprite('iz020_07', 3)	# 39-41
    sprite('iz020_08', 3)	# 42-44
    gotoLabel(0)
    label(1)
    sprite('iz010_02', 4)	# 45-48
    sprite('iz010_01', 4)	# 49-52
    sprite('iz010_00', 4)	# 53-56

@State
def AN_CmnActInvincibleAttackAir_Ne():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        AttackLevel_(4)
        Damage(1300)
        AttackP1(48)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(-140000)
        AirUntechableTime(100)
        Unknown11001(0, 6, 6)
        Hitstop(2)
        Unknown9118(15)
        Unknown9190(1)
        Unknown14083(0)
        Unknown30068(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        Unknown2003(1)
        Unknown1084(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('keep', 1)	# 1-1
    sprite('iz408_07', 3)	# 2-4
    GFX_0('Iai_AntiAir_Next_408F', -1)
    GFX_0('Iai_AntiAir_Next_408B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz408_08', 3)	# 5-7
    SFX_3('izse_04')
    sprite('iz406_00', 1)	# 8-8
    Unknown3004(30)
    EnableCollision(0)
    Unknown2006()
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeX(250000)
    Unknown1007(240000)
    sprite('iz406_00', 3)	# 9-11
    GFX_0('Iai_AntiAir_Next_406F', -1)
    GFX_0('Iai_AntiAir_Next_406B', -1)
    Unknown3001(0)
    Unknown3004(30)
    sprite('iz406_01', 4)	# 12-15
    Unknown23119(2148384, 10, 2)
    setGravity(0)
    physicsYImpulse(2000)
    sprite('iz406_02', 4)	# 16-19
    sprite('iz406_03', 4)	# 20-23
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_04', 4)	# 24-27
    sprite('iz406_05', 4)	# 28-31	 **attackbox here**
    sprite('iz406_06', 3)	# 32-34	 **attackbox here**
    tag_voice(1, 'biz208_0', 'biz208_1', 'biz208_2', '')
    Unknown2003(0)
    SFX_3('izse_01')
    physicsYImpulse(-80000)
    setGravity(7000)
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    label(0)
    sprite('iz406_06', 3)	# 35-37	 **attackbox here**
    sprite('iz406_07', 3)	# 38-40	 **attackbox here**
    sprite('iz406_08', 3)	# 41-43	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('iz406_09', 5)	# 44-48	 **attackbox here**
    setInvincible(0)
    EnableCollision(1)
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    Unknown1084(1)
    Recovery()
    sprite('iz406_10', 11)	# 49-59	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_11', 8)	# 60-67
    sprite('iz406_12', 6)	# 68-73
    sprite('iz406_13', 6)	# 74-79
    ExitState()

@Subroutine
def Warp_DeriveInput():
    Unknown14070('Warp_A_Air_HASEI')
    Unknown14070('Warp_B_Air_HASEI')
    Unknown14070('Warp_D_Air_HASEI')

@Subroutine
def Warp_DeriveTiming():
    Unknown14072('Warp_A_Air_HASEI')
    Unknown14072('Warp_B_Air_HASEI')
    Unknown14072('Warp_D_Air_HASEI')

@Subroutine
def Warp_DeriveClear():
    Unknown14074('Warp_A_Air_HASEI')
    Unknown14074('Warp_B_Air_HASEI')
    Unknown14074('Warp_D_Air_HASEI')

@State
def Shot_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('iz400_00', 3)	# 1-3
    sprite('iz400_01', 3)	# 4-6	 **attackbox here**
    Unknown7007('62697a3230305f3000000000000000006400000062697a3230305f3100000000000000006400000062697a3230305f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Shot', 0)
    sprite('iz400_02', 3)	# 7-9	 **attackbox here**
    SFX_3('izse_05')
    callSubroutine('Warp_DeriveInput')
    sprite('iz400_03', 3)	# 10-12	 **attackbox here**
    Unknown1084(1)
    sprite('iz400_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(-4000)
    physicsYImpulse(3000)
    setGravity(700)
    sprite('iz400_05', 3)	# 16-18	 **attackbox here**
    sprite('iz400_06', 3)	# 19-21	 **attackbox here**
    callSubroutine('Warp_DeriveTiming')
    sprite('iz400_07', 120)	# 22-141	 **attackbox here**
    sendToLabelUpon(2, 0)
    loopRest()
    label(0)
    sprite('iz400_08', 3)	# 142-144	 **attackbox here**
    clearUponHandler(2)
    Unknown1019(60)
    sprite('iz400_09', 3)	# 145-147	 **attackbox here**
    physicsXImpulse(0)
    callSubroutine('Warp_DeriveClear')
    Unknown8000(100, 1, 1)
    sprite('iz400_10', 4)	# 148-151	 **attackbox here**
    sprite('iz400_11', 4)	# 152-155
    Recovery()
    sprite('iz400_12', 4)	# 156-159
    sprite('iz400_13', 3)	# 160-162
    sprite('iz400_14', 3)	# 163-165

@State
def Shot_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11056(0)
        Unknown1084(1)
    sprite('iz204_00', 2)	# 1-2
    sprite('iz204_01', 1)	# 3-3
    sprite('iz204_02', 3)	# 4-6
    GFX_0('KakuseiAura', 0)
    GFX_0('KakuseiAura_oku', 1)
    GFX_0('5DLightsaber_on', -1)
    SFX_0('022_magiccircle_b')
    sprite('iz204_03', 3)	# 7-9
    callSubroutine('Warp_DeriveInput')
    sprite('iz204_04', 3)	# 10-12
    sprite('iz204_02ex00', 3)	# 13-15
    sprite('iz204_03ex00', 3)	# 16-18
    sprite('iz204_04', 3)	# 19-21
    sprite('iz204_05', 2)	# 22-23
    sprite('iz204_06', 1)	# 24-24
    sprite('iz400_00', 3)	# 25-27
    tag_voice(1, 'biz201_0', 'biz201_2', '', '')
    sprite('iz400_01ex00', 3)	# 28-30	 **attackbox here**
    GFX_0('Special_Shot', 0)
    sprite('iz400_02ex00', 3)	# 31-33	 **attackbox here**
    sprite('iz400_03ex00', 3)	# 34-36	 **attackbox here**
    Unknown1084(1)
    GFX_0('ShotD_Aura', 1)
    sprite('iz400_04ex00', 3)	# 37-39	 **attackbox here**
    SFX_3('izse_05')
    GFX_0('ShotD_Aura_back', 0)
    physicsXImpulse(-10000)
    physicsYImpulse(3000)
    setGravity(700)
    sprite('iz400_05ex00', 3)	# 40-42	 **attackbox here**
    callSubroutine('Warp_DeriveTiming')
    sprite('iz400_06ex00', 3)	# 43-45	 **attackbox here**
    sprite('iz400_07ex00', 3)	# 46-48	 **attackbox here**
    sprite('iz400_08ex00', 120)	# 49-168	 **attackbox here**
    sendToLabelUpon(2, 0)
    loopRest()
    label(0)
    sprite('iz400_09ex00', 2)	# 169-170	 **attackbox here**
    clearUponHandler(2)
    Unknown1019(60)
    sprite('iz400_09ex00', 2)	# 171-172	 **attackbox here**
    Unknown1019(20)
    Unknown8000(100, 1, 1)
    callSubroutine('Warp_DeriveClear')
    sprite('iz400_10ex00', 3)	# 173-175	 **attackbox here**
    sprite('iz400_11', 3)	# 176-178
    sprite('iz400_12', 3)	# 179-181
    physicsXImpulse(0)
    Recovery()
    sprite('iz400_13', 2)	# 182-183
    sprite('iz400_14', 2)	# 184-185

@State
def AirShot_A():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('iz401_00', 1)	# 1-1
    Unknown22004(7, 1)
    Unknown1045(0)
    physicsXImpulse(-6000)
    physicsYImpulse(24000)
    setGravity(1300)
    sprite('iz401_00', 3)	# 2-4
    sprite('iz401_01', 2)	# 5-6	 **attackbox here**
    Unknown7007('62697a3230305f3000000000000000006400000062697a3230305f3100000000000000006400000062697a3230305f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Air_Shot', 0)
    sprite('iz401_01', 2)	# 7-8	 **attackbox here**
    callSubroutine('Warp_DeriveInput')
    sprite('iz401_02', 4)	# 9-12	 **attackbox here**
    SFX_3('izse_05')
    sprite('iz401_03', 3)	# 13-15	 **attackbox here**
    sprite('iz401_04', 3)	# 16-18	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    callSubroutine('Warp_DeriveTiming')
    sprite('iz401_05', 3)	# 19-21	 **attackbox here**
    sprite('iz401_06', 3)	# 22-24	 **attackbox here**
    sprite('iz401_07', 3)	# 25-27	 **attackbox here**
    sprite('iz401_06', 3)	# 28-30	 **attackbox here**
    sprite('iz401_08', 3)	# 31-33	 **attackbox here**
    sprite('iz401_09', 3)	# 34-36	 **attackbox here**
    sprite('iz401_10', 3)	# 37-39
    sprite('iz401_11', 3)	# 40-42
    sprite('iz401_12', 3)	# 43-45

@State
def AirShot_B():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('iz401_00', 1)	# 1-1
    Unknown1045(0)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    setGravity(0)
    sprite('iz401_00', 2)	# 2-3
    sprite('iz401_00', 3)	# 4-6
    Unknown7007('62697a3230315f3000000000000000006400000062697a3230315f3100000000000000006400000062697a3230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('iz401_00', 8)	# 7-14
    callSubroutine('Warp_DeriveInput')
    sprite('iz401_01ex00', 2)	# 15-16	 **attackbox here**
    GFX_0('AirSpecial_Shot', 1)
    sprite('iz401_01ex00', 2)	# 17-18	 **attackbox here**
    sprite('iz401_02ex00', 4)	# 19-22	 **attackbox here**
    sprite('iz401_03ex00', 3)	# 23-25	 **attackbox here**
    SFX_3('izse_05')
    sprite('iz401_04ex00', 3)	# 26-28	 **attackbox here**
    GFX_0('AirShotAura', 0)
    Unknown1045(0)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    setGravity(1300)
    SFX_0('003_swing_grap_0_1')
    callSubroutine('Warp_DeriveTiming')
    sprite('iz401_05ex00', 3)	# 29-31	 **attackbox here**
    sprite('iz401_06ex00', 3)	# 32-34	 **attackbox here**
    sprite('iz401_07ex00', 3)	# 35-37	 **attackbox here**
    sprite('iz401_08ex00', 3)	# 38-40	 **attackbox here**
    sprite('iz401_09ex00', 3)	# 41-43	 **attackbox here**
    sprite('iz401_10', 4)	# 44-47
    sprite('iz401_11', 4)	# 48-51
    sprite('iz401_12', 4)	# 52-55

@Subroutine
def IaiSlashZanzou():
    Unknown3069(2)
    Unknown3071(5)
    Unknown3076(1010)
    Unknown3077(1010)

@State
def Iai_Slash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AttackP1(90)
        PushbackX(8000)
        AirPushbackY(12000)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11001(0, 5, 5)
        HitLow(2)
        Hitstop(6)
        AirUntechableTime(30)
        Unknown9016(1)
        Unknown2004(1, 0)
        callSubroutine('IaiSlashZanzou')

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Iai_Slash_Next')
            Unknown14072('Warp_D_LandHitOnly')

        def upon_STATE_END():
            Unknown7015()

        def upon_78():
            clearUponHandler(78)
            Unknown9310(1)
            Unknown11065(1)
            sendToLabel(0)
    sprite('iz402_00', 3)	# 1-3
    Unknown3029(1)
    sprite('iz402_01', 3)	# 4-6
    sprite('iz402_02', 1)	# 7-7
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    tag_voice(1, 'biz205_0', 'biz205_1', 'biz205_2', '')
    Unknown14070('Iai_Slash_Next')
    Unknown14070('Warp_D_LandHitOnly')
    sprite('iz402_05ex', 3)	# 8-10
    Unknown7015()
    SFX_3('izse_01')
    SFX_0('010_swing_sword_2')
    sprite('iz402_06ex', 3)	# 11-13	 **attackbox here**
    GFX_0('Iai_SlashZanzo_Gedan', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    Unknown13(6)
    Unknown13(7)
    sprite('iz402_07ex', 3)	# 14-16	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('iz402_08', 3)	# 17-19
    sprite('iz402_09', 3)	# 20-22
    Unknown14077(0)
    Unknown2063()
    sprite('iz402_10', 3)	# 23-25
    Unknown7015()
    Unknown3029(0)
    Unknown14074('Iai_Slash_Next')
    Unknown14074('Warp_D_LandHitOnly')
    sprite('iz402_11', 2)	# 26-27
    sprite('iz402_12', 2)	# 28-29
    sprite('iz402_13', 2)	# 30-31
    ExitState()
    label(0)
    sprite('iz402_07ex', 6)	# 32-37	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('iz402_08', 6)	# 38-43
    sprite('iz402_09', 6)	# 44-49
    Unknown14077(0)
    Unknown2063()
    sprite('iz402_10', 6)	# 50-55
    Unknown7015()
    Unknown3029(0)
    sprite('iz402_11', 5)	# 56-60
    Unknown14074('Iai_Slash_Next')
    Unknown14074('Warp_D_LandHitOnly')
    sprite('iz402_12', 5)	# 61-65
    sprite('iz402_13', 5)	# 66-70

@State
def Iai_Slash_Next():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(56)
        Unknown11001(0, 5, 5)
        AirPushbackX(20000)
        AirPushbackY(30000)
        PushbackX(12000)
        Unknown11056(0)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown30068(1)
        Unknown14077(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(5)
        Unknown3074('0000000000000000ff00000040000000')
        Unknown3075('0000000000000000c800000000000000')
        Unknown3076(1010)
        Unknown3077(1010)

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Warp_D_LandHitOnly')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('iz403_00', 1)	# 1-1
    Unknown2006()
    SFX_3('izse_04')
    Unknown23119(2148384, 4, 2)
    GFX_0('firespark', -1)
    physicsXImpulse(58000)
    sprite('iz403_00', 2)	# 2-3
    Unknown26('Iaimcircle')
    Unknown13(6)
    Unknown13(7)
    sprite('iz403_00', 3)	# 4-6
    GFX_0('firespark', -1)
    Unknown14070('Warp_D_LandHitOnly')
    sprite('iz403_01', 2)	# 7-8
    GFX_0('firespark', -1)
    sprite('iz403_02', 3)	# 9-11	 **attackbox here**
    SFX_3('izse_01')
    GFX_0('Ia_SlashNextZanzo', -1)
    GFX_0('IaiSlashNextAura', 0)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f736964650000000000000000000000000000')
    setInvincible(0)
    physicsXImpulse(8000)
    tag_voice(1, 'biz204_0', 'biz204_1', 'biz204_2', '')
    sprite('iz403_03', 5)	# 12-16	 **attackbox here**
    Recovery()
    Unknown1019(25)
    sprite('iz403_04', 5)	# 17-21	 **attackbox here**
    Unknown1019(25)
    sprite('iz403_05', 5)	# 22-26	 **attackbox here**
    Unknown14077(1)
    Unknown1084(1)
    Unknown3029(0)
    Unknown14074('Warp_D_LandHitOnly')
    sprite('iz403_06', 4)	# 27-30	 **attackbox here**
    sprite('iz403_07', 4)	# 31-34	 **attackbox here**
    Unknown14077(0)
    sprite('iz403_08', 4)	# 35-38
    sprite('iz403_09', 4)	# 39-42
    sprite('iz403_10', 4)	# 43-46

@State
def Iai_AntiAirA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(90)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(14000)
        AirPushbackY(43000)
        AirUntechableTime(60)
        Hitstop(6)
        Unknown9016(1)
        Unknown2004(1, 0)
        SLOT_59 = 7

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Iai_AntiAir_Next')
            Unknown14072('Warp_D_LandHitOnly')

        def upon_78():
            SLOT_59 = 1
            sendToLabel(0)
        callSubroutine('IaiSlashZanzou')
        Unknown14077(1)

        def upon_STATE_END():
            Unknown7015()
    sprite('iz402_00', 2)	# 1-2
    Unknown3029(1)
    sprite('iz402_01', 1)	# 3-3
    sprite('iz402_01', 1)	# 4-4
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('iz402_02', 2)	# 5-6
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    Unknown2037(1)
    tag_voice(1, 'biz202_0', 'biz202_1', 'biz202_2', '')
    sprite('iz404_00', 1)	# 7-7
    sprite('iz404_01', 2)	# 8-9
    Unknown7015()
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo_AntiAirA', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    Unknown14070('Iai_AntiAir_Next')
    Unknown14070('Warp_D_LandHitOnly')
    sprite('iz404_02', 3)	# 10-12	 **attackbox here**
    sprite('iz404_03', 2)	# 13-14
    setInvincible(0)
    Recovery()
    sprite('iz404_04', 3)	# 15-17
    sprite('iz404_05', 3)	# 18-20
    Unknown2063()
    Unknown14074('Iai_AntiAir_Next')
    Unknown14074('Warp_D_LandHitOnly')
    sprite('iz404_06', 3)	# 21-23
    Unknown3029(0)
    sprite('iz404_07', 3)	# 24-26
    sprite('iz404_08', 3)	# 27-29
    sprite('iz404_09', 3)	# 30-32
    ExitState()
    label(0)
    sprite('iz404_03', 7)	# 33-39
    setInvincible(0)
    Recovery()
    sprite('iz404_04', 4)	# 40-43
    sprite('iz404_04', 3)	# 44-46
    Unknown14074('Iai_AntiAir_Next')
    Unknown14074('Warp_D_LandHitOnly')
    sprite('iz404_05', 7)	# 47-53
    sprite('iz404_06', 7)	# 54-60
    Unknown3029(0)
    sprite('iz404_07', 7)	# 61-67
    sprite('iz404_08', 7)	# 68-74
    sprite('iz404_09', 7)	# 75-81

@State
def Iai_Slash_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP2(75)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(27000)
        AirPushbackY(17000)
        Unknown11001(0, 5, 5)
        Hitstop(6)
        AirUntechableTime(25)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown3069(2)
        Unknown3071(5)
        Unknown3076(1010)
        Unknown3077(1010)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(0)
            clearUponHandler(10)
        Unknown14077(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown7015()
    sprite('iz402_00', 2)	# 1-2
    Unknown3029(1)
    sprite('iz402_01', 1)	# 3-3
    sprite('iz402_01', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('iz402_02', 3)	# 5-7
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    sprite('iz402_03', 3)	# 8-10
    tag_voice(1, 'biz203_0', 'biz203_1', 'biz203_2', '')
    sprite('iz402_05', 2)	# 11-12
    Unknown7015()
    SFX_0('010_swing_sword_2')
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo00', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    Unknown13(6)
    Unknown13(7)
    sprite('iz402_06', 1)	# 13-13	 **attackbox here**
    sprite('iz402_06', 1)	# 14-14	 **attackbox here**
    sprite('iz402_06', 1)	# 15-15	 **attackbox here**
    sprite('iz402_07', 3)	# 16-18	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('iz402_08', 4)	# 19-22
    sprite('iz402_09', 4)	# 23-26
    sprite('iz402_10', 4)	# 27-30
    Unknown7015()
    Recovery()
    Unknown3029(0)
    Unknown2063()
    sprite('iz402_11', 4)	# 31-34
    sprite('iz402_12', 3)	# 35-37
    sprite('iz402_13', 3)	# 38-40
    ExitState()
    label(0)
    sprite('iz403_00', 1)	# 41-41
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)

    def upon_78():
        sendToLabel(1)
        clearUponHandler(78)
        Hitstop(6)
    Unknown2006()
    SFX_3('izse_04')
    Unknown23119(2148384, 4, 2)
    GFX_0('firespark', -1)
    physicsXImpulse(58000)
    sprite('iz403_00', 2)	# 42-43
    Unknown26('Iaimcircle')
    Unknown13(6)
    Unknown13(7)
    sprite('iz403_00', 3)	# 44-46
    GFX_0('firespark', -1)
    sprite('iz403_01', 2)	# 47-48
    GFX_0('firespark', -1)
    sprite('iz403_02', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    AttackP1(90)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirUntechableTime(56)
    Hitstop(12)
    AirPushbackX(5000)
    AirPushbackY(50000)
    PushbackX(12000)
    Unknown11056(0)
    SFX_3('izse_01')
    GFX_0('Ia_SlashNextZanzo', -1)
    GFX_0('IaiSlashNextAura', 0)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f736964650000000000000000000000000000')
    setInvincible(0)
    physicsXImpulse(8000)
    tag_voice(1, 'biz204_0', 'biz204_1', 'biz204_2', '')
    sprite('iz403_03', 1)	# 52-52	 **attackbox here**
    Recovery()
    Unknown1019(25)
    sprite('iz403_04', 1)	# 53-53	 **attackbox here**
    Unknown1019(25)
    sprite('iz403_05', 1)	# 54-54	 **attackbox here**
    Unknown1084(1)
    Unknown3029(0)
    sprite('iz403_06', 1)	# 55-55	 **attackbox here**
    sprite('iz403_07', 2)	# 56-57	 **attackbox here**
    sprite('iz403_08', 2)	# 58-59
    sprite('iz403_09', 2)	# 60-61
    sprite('iz403_10', 2)	# 62-63
    ExitState()
    label(1)
    sprite('keep', 1)	# 64-64
    Unknown2003(1)
    Unknown1084(1)
    clearUponHandler(2)
    sendToLabelUpon(2, 3)
    sprite('iz403_03', 2)	# 65-66	 **attackbox here**
    GFX_0('EX_Iai_AntiAir_Next_405F', -1)
    GFX_0('EX_Iai_AntiAir_Next_405B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz403_04', 2)	# 67-68	 **attackbox here**
    SFX_3('izse_04')
    setInvincible(1)
    sprite('iz403_05', 2)	# 69-70	 **attackbox here**
    sprite('iz406_00', 1)	# 71-71
    Unknown3004(30)
    EnableCollision(0)
    Unknown2006()
    Unknown1086(22)
    Unknown1007(460000)
    teleportRelativeX(-60000)
    sprite('iz406_00', 3)	# 72-74
    GFX_0('Iai_AntiAir_Next_406F', -1)
    GFX_0('Iai_AntiAir_Next_406B', -1)
    Unknown3001(0)
    Unknown3004(30)
    sprite('iz406_01', 4)	# 75-78
    Unknown23119(2148384, 10, 2)
    setGravity(0)
    physicsYImpulse(2000)
    sprite('iz406_02', 4)	# 79-82
    sprite('iz406_03', 4)	# 83-86
    Unknown3001(255)
    Unknown3004(0)
    setInvincible(0)
    sprite('iz406_04', 4)	# 87-90
    sprite('iz406_05', 4)	# 91-94	 **attackbox here**
    sprite('iz406_06', 3)	# 95-97	 **attackbox here**
    Damage(1700)
    AttackP2(75)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(-140000)
    AirUntechableTime(100)
    Unknown11001(0, 6, 6)
    Hitstop(2)
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown9118(15)
    Unknown9190(1)
    Unknown2004(1, 0)
    tag_voice(1, 'biz208_0', 'biz208_1', 'biz208_2', '')
    RefreshMultihit()
    Unknown2003(0)
    SFX_3('izse_01')
    physicsYImpulse(-80000)
    setGravity(7000)
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    label(2)
    sprite('iz406_06', 3)	# 98-100	 **attackbox here**
    sprite('iz406_07', 3)	# 101-103	 **attackbox here**
    sprite('iz406_08', 3)	# 104-106	 **attackbox here**
    gotoLabel(2)
    label(3)
    sprite('iz406_09', 5)	# 107-111	 **attackbox here**
    EnableCollision(1)
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    Unknown1084(1)
    Recovery()
    sprite('iz406_10', 11)	# 112-122	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_11', 8)	# 123-130
    sprite('iz406_12', 6)	# 131-136
    sprite('iz406_13', 6)	# 137-142

@State
def Iai_SlashAir_Low():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1850)
        AttackP1(90)
        AirPushbackX(10000)
        AirPushbackY(45000)
        AirUntechableTime(45)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Hitstop(6)
        Unknown2004(1, 0)

        def upon_12():
            SLOT_59 = 6

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Iai_AntiAir_Next')
            Unknown14072('Warp_D_Air_HASEI')
        callSubroutine('IaiSlashZanzou')
    sprite('iz413_00', 2)	# 1-2
    Unknown1084(1)
    sprite('iz413_01', 1)	# 3-3
    sprite('iz413_01', 1)	# 4-4
    WhiffCancelEnable(1)
    sprite('iz413_02', 2)	# 5-6
    sprite('iz413_03', 1)	# 7-7
    SFX_3('izse_01')
    sprite('iz413_04', 1)	# 8-8
    sprite('iz413_12ex', 2)	# 9-10
    tag_voice(1, 'biz205_0', 'biz205_1', 'biz205_2', '')
    GFX_0('izef_413_c', -1)
    SFX_0('010_swing_sword_2')
    Unknown14070('Iai_AntiAir_Next')
    Unknown14070('Warp_D_Air_HASEI')
    sprite('iz413_13ex', 3)	# 11-13	 **attackbox here**
    sprite('iz413_14ex', 3)	# 14-16
    Recovery()
    sprite('iz413_15', 5)	# 17-21
    sprite('iz413_16', 5)	# 22-26
    Unknown14074('Iai_AntiAir_Next')
    Unknown14074('Warp_D_Air_HASEI')
    sprite('iz413_17', 5)	# 27-31
    sprite('iz413_18', 5)	# 32-36
    sprite('iz413_01', 3)	# 37-39
    Unknown1044()
    sprite('iz413_00', 4)	# 40-43
    sprite('iz020_05', 4)	# 44-47
    sprite('iz020_06', 4)	# 48-51
    label(0)
    sprite('iz020_07', 3)	# 52-54
    sprite('iz020_08', 3)	# 55-57
    gotoLabel(0)

@State
def Iai_SlashAir_High():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(90)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(17000)
        AirPushbackY(53000)
        Unknown9016(1)
        AirUntechableTime(45)
        Hitstop(6)
        Unknown2004(1, 0)

        def upon_78():
            SLOT_59 = 5

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Iai_AntiAir_Next')
            Unknown14072('Warp_D_Air_HASEI')
        callSubroutine('IaiSlashZanzou')
    sprite('iz413_00', 2)	# 1-2
    Unknown1084(1)
    sprite('iz413_01', 1)	# 3-3
    sprite('iz413_01', 1)	# 4-4
    WhiffCancelEnable(1)
    sprite('iz413_02', 2)	# 5-6
    sprite('iz413_05', 2)	# 7-8
    SFX_3('izse_01')
    sprite('iz413_06', 2)	# 9-10
    tag_voice(1, 'biz202_0', 'biz202_1', 'biz202_2', '')
    SFX_0('010_swing_sword_2')
    GFX_0('izef_413_a', -1)
    Unknown14070('Iai_AntiAir_Next')
    Unknown14070('Warp_D_Air_HASEI')
    sprite('iz413_07', 3)	# 11-13	 **attackbox here**
    sprite('iz413_08', 4)	# 14-17
    Recovery()
    sprite('iz413_09', 4)	# 18-21
    sprite('iz413_10', 4)	# 22-25
    Unknown14074('Iai_AntiAir_Next')
    Unknown14074('Warp_D_Air_HASEI')
    sprite('iz413_11', 4)	# 26-29
    sprite('iz413_01', 4)	# 30-33
    Unknown1044()
    sprite('iz413_00', 4)	# 34-37
    sprite('iz020_05', 4)	# 38-41
    sprite('iz020_06', 4)	# 42-45
    label(0)
    sprite('iz020_07', 3)	# 46-48
    sprite('iz020_08', 3)	# 49-51
    gotoLabel(0)

@State
def Iai_AntiAir_Next():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AttackP1(90)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(-140000)
        AirUntechableTime(100)
        Unknown11001(0, 6, 6)
        Hitstop(2)
        Unknown9118(15)
        Unknown9190(1)
        Unknown30068(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        if (SLOT_59 == 1):
            sendToLabel(2)
        if (SLOT_59 == 2):
            sendToLabel(3)
        if (SLOT_59 == 3):
            sendToLabel(4)
        if (SLOT_59 == 4):
            sendToLabel(10)
        if (SLOT_59 == 5):
            sendToLabel(10)
        if (SLOT_59 == 6):
            sendToLabel(10)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        Unknown2037(0)
        if SLOT_4:
            Damage(750)
            Unknown11092(1)
            Unknown2037(1)
        Unknown2003(1)
        Unknown1084(1)
    sprite('keep', 1)	# 1-1
    label(2)
    sprite('iz404_03', 2)	# 2-3
    GFX_0('Iai_AntiAir_Next_404F', -1)
    GFX_0('Iai_AntiAir_Next_404B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz404_04', 2)	# 4-5
    SFX_3('izse_04')
    setInvincible(1)
    sprite('iz404_05', 2)	# 6-7
    gotoLabel(5)
    label(3)
    sprite('iz405_07', 2)	# 8-9
    GFX_0('Iai_AntiAir_Next_405F', -1)
    GFX_0('Iai_AntiAir_Next_405B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz405_08', 2)	# 10-11
    SFX_3('izse_04')
    setInvincible(1)
    sprite('iz405_09', 2)	# 12-13
    gotoLabel(5)
    label(4)
    sprite('iz408_07', 3)	# 14-16
    GFX_0('Iai_AntiAir_Next_408F', -1)
    GFX_0('Iai_AntiAir_Next_408B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz408_08', 3)	# 17-19
    SFX_3('izse_04')
    setInvincible(1)
    gotoLabel(5)
    label(10)
    sprite('iz413_15', 2)	# 20-21
    GFX_0('Iai_AntiAir_Next_413F', -1)
    GFX_0('Iai_AntiAir_Next_413B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz413_16', 2)	# 22-23
    SFX_3('izse_04')
    setInvincible(1)
    sprite('iz413_17', 2)	# 24-25
    gotoLabel(5)
    label(5)
    sprite('iz406_00', 1)	# 26-26
    Unknown3004(30)
    EnableCollision(0)
    Unknown2006()
    Unknown1086(22)
    if (SLOT_59 == 1):
        Unknown1007(300000)
        teleportRelativeX(200000)
        SLOT_59 = 0
    if (SLOT_59 == 2):
        Unknown1007(160000)
        teleportRelativeX(-60000)
        SLOT_59 = 0
    if (SLOT_59 == 3):
        Unknown1084(1)
        teleportRelativeX(250000)
        Unknown1007(180000)
        SLOT_59 = 0
    if (SLOT_59 == 4):
        Unknown1084(1)
        teleportRelativeX(250000)
        Unknown1007(240000)
        SLOT_59 = 0
    if (SLOT_59 == 5):
        Unknown1084(1)
        teleportRelativeX(250000)
        Unknown1007(560000)
        SLOT_59 = 0
    if (SLOT_59 == 6):
        Unknown1084(1)
        teleportRelativeX(75000)
        Unknown1007(360000)
        SLOT_59 = 0
    if (SLOT_59 == 7):
        Unknown1007(160000)
        teleportRelativeX(-60000)
        Unknown1007(100000)
        SLOT_59 = 0
    sprite('iz406_00', 3)	# 27-29
    GFX_0('Iai_AntiAir_Next_406F', -1)
    GFX_0('Iai_AntiAir_Next_406B', -1)
    Unknown3001(0)
    Unknown3004(30)
    sprite('iz406_01', 4)	# 30-33
    Unknown23119(2148384, 10, 2)
    setGravity(0)
    physicsYImpulse(2000)
    sprite('iz406_02', 4)	# 34-37
    sprite('iz406_03', 4)	# 38-41
    Unknown3001(255)
    Unknown3004(0)
    setInvincible(0)
    sprite('iz406_04', 4)	# 42-45
    sprite('iz406_05', 4)	# 46-49	 **attackbox here**
    sprite('iz406_06', 1)	# 50-50	 **attackbox here**
    tag_voice(1, 'biz208_0', 'biz208_1', 'biz208_2', '')
    Unknown2003(0)
    SFX_3('izse_01')
    physicsYImpulse(-80000)
    setGravity(7000)
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    sprite('iz406_06', 1)	# 51-51	 **attackbox here**
    if SLOT_2:
        RefreshMultihit()
    sprite('iz406_06', 1)	# 52-52	 **attackbox here**
    if SLOT_2:
        RefreshMultihit()
    label(0)
    sprite('iz406_06', 3)	# 53-55	 **attackbox here**
    sprite('iz406_07', 3)	# 56-58	 **attackbox here**
    sprite('iz406_08', 3)	# 59-61	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('iz406_09', 5)	# 62-66	 **attackbox here**
    EnableCollision(1)
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    Unknown1084(1)
    Recovery()
    sprite('iz406_10', 11)	# 67-77	 **attackbox here**
    Unknown23183('697a3430365f3130000000000000000000000000000000000000000000000000030000000200000002000000')
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_11', 8)	# 78-85
    Unknown23183('697a3430365f3131000000000000000000000000000000000000000000000000030000000200000002000000')
    sprite('iz406_12', 6)	# 86-91
    Unknown23183('697a3430365f3132000000000000000000000000000000000000000000000000030000000200000002000000')
    sprite('iz406_13', 6)	# 92-97
    Unknown23183('697a3430365f3133000000000000000000000000000000000000000000000000030000000200000002000000')

@State
def Warp_A_Air():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
            Unknown2006()
            Unknown1043()
            Unknown3029(0)
            Unknown23015(0)
        callSubroutine('WarpFlexCancel')
        clearUponHandler(2)
    sprite('iz410_00', 4)	# 1-4
    Unknown2015(50)
    Unknown1019(0)
    physicsYImpulse(3000)
    setGravity(300)
    sprite('iz410_01', 4)	# 5-8
    tag_voice(1, 'biz209_0', 'biz209_1', 'biz209_2', '')
    sprite('iz410_02', 3)	# 9-11
    SFX_3('izse_04')
    GFX_0('Warp_D_Air_Zanzo00', -1)
    GFX_0('Warp_D_Air_Zanzo01', -1)
    GFX_0('WarpEff_D', 0)
    sprite('iz410_02', 3)	# 12-14
    Unknown3032()
    Unknown3004(-30)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    sprite('iz410_03', 3)	# 15-17	 **attackbox here**
    Unknown3001(0)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(1)
    sprite('iz410_03', 3)	# 18-20	 **attackbox here**
    sprite('iz410_03', 1)	# 21-21	 **attackbox here**
    sprite('iz410_03', 1)	# 22-22	 **attackbox here**
    sprite('iz410_03', 1)	# 23-23	 **attackbox here**
    sprite('iz410_03', 1)	# 24-24	 **attackbox here**
    sprite('iz409_03', 2)	# 25-26
    EnableCollision(1)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown3004(60)
    Unknown23015(5)
    clearUponHandler(2)
    setInvincible(0)
    sprite('iz409_04', 2)	# 27-28
    GFX_0('Warp_A_Zanzo00', -1)
    GFX_0('Warp_A_Zanzo01', -1)
    sprite('iz409_05', 3)	# 29-31
    sprite('iz409_06', 3)	# 32-34
    Unknown13014(1)
    WhiffCancelEnable(1)
    sprite('iz409_07', 3)	# 35-37
    sprite('iz409_08', 3)	# 38-40
    sprite('iz409_09', 3)	# 41-43

@State
def Warp_B_Air():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2061(1)
        SLOT_11 = 1

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
            Unknown2006()
            Unknown1043()
            Unknown3029(0)
            Unknown23015(0)
        callSubroutine('WarpFlexCancel')
    sprite('iz410_00', 4)	# 1-4
    Unknown2015(50)
    Unknown1019(0)
    physicsYImpulse(3000)
    setGravity(300)
    sprite('iz410_01', 4)	# 5-8
    tag_voice(1, 'biz209_0', 'biz209_1', 'biz209_2', '')
    sprite('iz410_02', 3)	# 9-11
    SFX_3('izse_04')
    GFX_0('Warp_D_Air_Zanzo00', -1)
    GFX_0('Warp_D_Air_Zanzo01', -1)
    GFX_0('WarpEff_D', 0)
    sprite('iz410_02', 3)	# 12-14
    Unknown3032()
    Unknown3004(-30)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    sprite('iz410_03', 3)	# 15-17	 **attackbox here**
    physicsXImpulse(3000)
    Unknown3001(0)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(1)
    sprite('iz410_03', 3)	# 18-20	 **attackbox here**
    sprite('iz410_03', 1)	# 21-21	 **attackbox here**
    sprite('iz410_03', 1)	# 22-22	 **attackbox here**
    sprite('iz410_03', 1)	# 23-23	 **attackbox here**
    sprite('iz410_03', 1)	# 24-24	 **attackbox here**
    sprite('iz410_03', 1)	# 25-25	 **attackbox here**
    sprite('iz020_02', 3)	# 26-28
    EnableCollision(1)
    Unknown1084(1)
    teleportRelativeX(-5000)
    teleportRelativeY(300000)
    physicsXImpulse(-5000)
    physicsYImpulse(8000)
    Unknown3004(60)
    Unknown23015(5)
    clearUponHandler(2)
    setInvincible(0)
    GFX_0('Warp_B_Air_Zanzo00', -1)
    GFX_0('Warp_B_Air_Zanzo01', -1)
    sprite('iz020_03', 3)	# 29-31
    Unknown1043()
    sprite('iz020_04', 3)	# 32-34

@State
def Warp_A_Air_HASEI():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2061(1)
        Unknown30068(1)
        Unknown22004(0, 0)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
            Unknown2006()
            Unknown1043()
            Unknown3029(0)
            Unknown23015(0)
        callSubroutine('WarpFlexCancel')
        clearUponHandler(2)
    sprite('iz410_00', 4)	# 1-4
    Unknown2015(50)
    Unknown1019(0)
    physicsYImpulse(3000)
    setGravity(300)
    sprite('iz410_01', 4)	# 5-8
    tag_voice(1, 'biz209_0', 'biz209_1', 'biz209_2', '')
    sprite('iz410_02', 3)	# 9-11
    SFX_3('izse_04')
    GFX_0('Warp_D_Air_Zanzo00', -1)
    GFX_0('Warp_D_Air_Zanzo01', -1)
    GFX_0('WarpEff_D', 0)
    sprite('iz410_02', 3)	# 12-14
    Unknown3032()
    Unknown3004(-30)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    sprite('iz410_03', 3)	# 15-17	 **attackbox here**
    Unknown3001(0)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(1)
    sprite('iz410_03', 3)	# 18-20	 **attackbox here**
    sprite('iz410_03', 1)	# 21-21	 **attackbox here**
    sprite('iz410_03', 1)	# 22-22	 **attackbox here**
    sprite('iz410_03', 1)	# 23-23	 **attackbox here**
    sprite('iz410_03', 1)	# 24-24	 **attackbox here**
    sprite('iz409_03', 2)	# 25-26
    EnableCollision(1)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown3004(60)
    Unknown23015(5)
    clearUponHandler(2)
    setInvincible(0)
    sprite('iz409_04', 2)	# 27-28
    GFX_0('Warp_A_Zanzo00', -1)
    GFX_0('Warp_A_Zanzo01', -1)
    sprite('iz409_05', 3)	# 29-31
    sprite('iz409_06', 3)	# 32-34
    Unknown13014(1)
    WhiffCancelEnable(1)
    sprite('iz409_07', 3)	# 35-37
    sprite('iz409_08', 3)	# 38-40
    sprite('iz409_09', 3)	# 41-43

@State
def Warp_B_Air_HASEI():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2061(1)
        SLOT_11 = 1
        Unknown30068(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
            Unknown2006()
            Unknown1043()
            Unknown3029(0)
            Unknown23015(0)
    sprite('iz410_00', 4)	# 1-4
    Unknown2015(50)
    Unknown1019(0)
    physicsYImpulse(3000)
    setGravity(300)
    sprite('iz410_01', 4)	# 5-8
    tag_voice(1, 'biz209_0', 'biz209_1', 'biz209_2', '')
    sprite('iz410_02', 3)	# 9-11
    SFX_3('izse_04')
    GFX_0('Warp_D_Air_Zanzo00', -1)
    GFX_0('Warp_D_Air_Zanzo01', -1)
    GFX_0('WarpEff_D', 0)
    sprite('iz410_02', 3)	# 12-14
    Unknown3032()
    Unknown3004(-30)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    sprite('iz410_03', 3)	# 15-17	 **attackbox here**
    physicsXImpulse(3000)
    Unknown3001(0)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(1)
    Unknown1084(1)
    sprite('iz410_03', 3)	# 18-20	 **attackbox here**
    sprite('iz410_03', 1)	# 21-21	 **attackbox here**
    sprite('iz410_03', 1)	# 22-22	 **attackbox here**
    sprite('iz410_03', 1)	# 23-23	 **attackbox here**
    sprite('iz410_03', 1)	# 24-24	 **attackbox here**
    sprite('iz410_03', 1)	# 25-25	 **attackbox here**
    sprite('iz020_02', 3)	# 26-28
    EnableCollision(1)
    Unknown1084(1)
    teleportRelativeX(-5000)
    teleportRelativeY(250000)
    physicsXImpulse(-5000)
    physicsYImpulse(8000)
    Unknown3004(60)
    Unknown23015(5)
    clearUponHandler(2)
    setInvincible(0)
    GFX_0('Warp_B_Air_Zanzo00', -1)
    GFX_0('Warp_B_Air_Zanzo01', -1)
    sprite('iz020_03', 3)	# 29-31
    Unknown1043()
    sprite('iz020_04', 3)	# 32-34

@State
def Shot_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('iz400_00', 3)	# 1-3
    sprite('iz400_01ex00', 3)	# 4-6	 **attackbox here**
    Unknown7007('62697a3230315f3000000000000000006400000062697a3230315f3100000000000000006400000062697a3230315f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    GFX_0('shotD_Matome', -1)
    sprite('iz400_02ex00', 3)	# 7-9	 **attackbox here**
    callSubroutine('Warp_DeriveInput')
    sprite('iz400_03ex00', 3)	# 10-12	 **attackbox here**
    Unknown1084(1)
    GFX_0('ShotD_Aura', 1)
    sprite('iz400_04ex00', 3)	# 13-15	 **attackbox here**
    SFX_3('izse_05')
    GFX_0('ShotD_Aura_back', 0)
    physicsXImpulse(-10000)
    physicsYImpulse(3000)
    setGravity(700)
    sprite('iz400_05ex00', 3)	# 16-18	 **attackbox here**
    callSubroutine('Warp_DeriveTiming')
    sprite('iz400_06ex00', 3)	# 19-21	 **attackbox here**
    sprite('iz400_07ex00', 3)	# 22-24	 **attackbox here**
    sprite('iz400_08ex00', 120)	# 25-144	 **attackbox here**
    sendToLabelUpon(2, 0)
    loopRest()
    label(0)
    sprite('iz400_09ex00', 2)	# 145-146	 **attackbox here**
    clearUponHandler(2)
    Unknown1019(60)
    sprite('iz400_09ex00', 2)	# 147-148	 **attackbox here**
    Unknown1019(20)
    Unknown8000(100, 1, 1)
    sprite('iz400_10ex00', 3)	# 149-151	 **attackbox here**
    callSubroutine('Warp_DeriveClear')
    sprite('iz400_11', 3)	# 152-154
    sprite('iz400_12', 3)	# 155-157
    physicsXImpulse(0)
    Recovery()
    sprite('iz400_13', 2)	# 158-159
    sprite('iz400_14', 2)	# 160-161

@State
def AirShot_D():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('iz401_00', 1)	# 1-1
    Unknown1045(0)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    setGravity(0)
    sprite('iz401_00', 2)	# 2-3
    sprite('iz401_00', 1)	# 4-4
    Unknown7007('62697a3230315f3000000000000000006400000062697a3230315f3100000000000000006400000062697a3230315f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('iz401_01ex00', 2)	# 5-6	 **attackbox here**
    GFX_0('AirshotD_Matome', -1)
    sprite('iz401_01ex00', 2)	# 7-8	 **attackbox here**
    callSubroutine('Warp_DeriveInput')
    sprite('iz401_02ex00', 4)	# 9-12	 **attackbox here**
    sprite('iz401_03ex00', 3)	# 13-15	 **attackbox here**
    SFX_3('izse_05')
    sprite('iz401_04ex00', 3)	# 16-18	 **attackbox here**
    GFX_0('AirShotAura', 0)
    Unknown1045(0)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    setGravity(1300)
    SFX_0('003_swing_grap_0_1')
    callSubroutine('Warp_DeriveTiming')
    sprite('iz401_05ex00', 3)	# 19-21	 **attackbox here**
    sprite('iz401_06ex00', 3)	# 22-24	 **attackbox here**
    sprite('iz401_07ex00', 3)	# 25-27	 **attackbox here**
    sprite('iz401_08ex00', 3)	# 28-30	 **attackbox here**
    sprite('iz401_09ex00', 3)	# 31-33	 **attackbox here**
    sprite('iz401_10', 4)	# 34-37
    sprite('iz401_11', 4)	# 38-41
    sprite('iz401_12', 4)	# 42-45

@State
def Warp_D_LandHitOnly():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2061(1)
        Unknown30068(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
            Unknown2006()
            Unknown22000()
            Unknown22002()
            Unknown1043()
            Unknown3029(0)
            Unknown23015(0)
        Unknown2037(0)
        if Unknown23145('Iai_Slash_Next'):
            Unknown2037(1)
    sprite('iz409_00', 3)	# 1-3
    Unknown2015(50)
    sprite('iz409_01', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('iz409_02', 3)	# 7-9
    SFX_3('izse_04')
    GFX_0('Warp_D_Land_Zanzo00', -1)
    GFX_0('Warp_D_Land_Zanzo01', -1)
    GFX_0('WarpEff_D', 0)
    tag_voice(1, 'biz211_0', 'biz211_1', 'biz211_2', '')
    sprite('iz409_02', 2)	# 10-11
    Unknown3004(-40)
    Unknown3032()
    sprite('iz410_00ex', 2)	# 12-13
    physicsXImpulse(3000)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    Unknown3001(0)
    setInvincible(1)
    sprite('iz410_01ex', 2)	# 14-15
    physicsXImpulse(12000)
    sprite('null', 3)	# 16-18
    Unknown1019(800)
    sprite('iz410_02ex', 1)	# 19-19
    Unknown48('190000000200000033000000160000000200000017000000')
    if SLOT_2:
        if (SLOT_51 <= 4350000):
            sendToLabel(0)
        else:
            sendToLabel(1)
    elif (SLOT_51 <= 250000):
        sendToLabel(0)
    else:
        sendToLabel(1)
    label(0)
    Unknown1086(22)
    sprite('iz409_10ex00', 1)	# 20-20	 **attackbox here**
    teleportRelativeX(70000)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown2006()
    Unknown23015(5)
    sprite('iz409_10ex00', 2)	# 21-22	 **attackbox here**
    GFX_0('WarpHoverAura', 1)
    GFX_1('izef_firespark', 0)
    EnableCollision(1)
    Unknown3004(60)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3072('dc000000640000006400000064000000')
    Unknown3073('3c000000640000006400000064000000')
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setInvincible(0)
    sprite('iz409_11ex00', 2)	# 23-24	 **attackbox here**
    sprite('iz409_12ex00', 2)	# 25-26	 **attackbox here**
    sprite('iz409_13ex00', 2)	# 27-28	 **attackbox here**
    sprite('iz409_14ex00', 1)	# 29-29	 **attackbox here**
    sprite('iz409_15ex00', 1)	# 30-30	 **attackbox here**
    sprite('iz409_16', 1)	# 31-31
    ExitState()
    label(1)
    Unknown1086(22)
    sprite('iz410_02', 1)	# 32-32
    EnableCollision(1)
    teleportRelativeX(70000)
    Unknown1007(-20000)
    Unknown1084(1)
    physicsXImpulse(500)
    physicsYImpulse(2000)
    Unknown3004(60)
    Unknown23015(5)
    SLOT_4 = 1
    sprite('iz410_03', 1)	# 33-33	 **attackbox here**
    GFX_0('WarpHoverAura_Air', 0)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3072('dc000000640000006400000064000000')
    Unknown3073('3c000000640000006400000064000000')
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setInvincible(0)
    sprite('iz410_04', 1)	# 34-34	 **attackbox here**
    sprite('iz410_05', 1)	# 35-35	 **attackbox here**
    sprite('iz410_06', 1)	# 36-36	 **attackbox here**
    sprite('iz410_07', 1)	# 37-37
    Unknown1043()

@State
def Warp_D_Land():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
            Unknown2006()
            Unknown22000()
            Unknown22002()
            Unknown3029(0)
            Unknown23015(0)
    sprite('iz409_00', 3)	# 1-3
    Unknown2015(50)
    sprite('iz409_00', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    tag_voice(1, 'biz211_0', 'biz211_1', 'biz211_2', '')
    sprite('iz409_01', 2)	# 5-6
    sprite('iz409_02', 3)	# 7-9
    SFX_3('izse_04')
    GFX_0('Warp_D_Land_Zanzo00', -1)
    GFX_0('Warp_D_Land_Zanzo01', -1)
    GFX_0('WarpEff_D', 0)
    sprite('iz409_02', 3)	# 10-12
    Unknown3004(-40)
    Unknown3032()
    physicsXImpulse(3000)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    Unknown3001(0)
    setInvincible(1)
    sprite('iz410_01ex', 3)	# 13-15
    physicsXImpulse(12000)
    sprite('iz410_02ex', 3)	# 16-18
    Unknown1019(800)
    sprite('iz410_02ex', 1)	# 19-19
    Unknown48('190000000200000033000000160000000200000017000000')
    if (SLOT_51 <= 430000):
        sendToLabel(0)
    else:
        sendToLabel(1)
    label(0)
    Unknown1086(22)
    sprite('iz409_10ex00', 1)	# 20-20	 **attackbox here**
    teleportRelativeX(70000)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown2006()
    Unknown23015(5)
    sprite('iz409_10ex00', 2)	# 21-22	 **attackbox here**
    GFX_0('WarpHoverAura', 1)
    GFX_1('izef_firespark', 0)
    EnableCollision(1)
    Unknown3004(60)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3072('dc000000640000006400000064000000')
    Unknown3073('3c000000640000006400000064000000')
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setInvincible(0)
    sprite('iz409_11ex00', 2)	# 23-24	 **attackbox here**
    sprite('iz409_12ex00', 2)	# 25-26	 **attackbox here**
    sprite('iz409_13ex00', 2)	# 27-28	 **attackbox here**
    sprite('iz409_14ex00', 1)	# 29-29	 **attackbox here**
    sprite('iz409_15ex00', 1)	# 30-30	 **attackbox here**
    sprite('iz409_16', 1)	# 31-31
    ExitState()
    label(1)
    Unknown1086(22)
    sprite('iz410_02', 2)	# 32-33
    EnableCollision(1)
    teleportRelativeX(70000)
    Unknown1007(-60000)
    Unknown1084(1)
    physicsXImpulse(500)
    physicsYImpulse(2000)
    Unknown3004(60)
    Unknown23015(5)
    SLOT_4 = 1
    sprite('iz410_03', 2)	# 34-35	 **attackbox here**
    GFX_0('WarpHoverAura_Air', 0)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3072('dc000000640000006400000064000000')
    Unknown3073('3c000000640000006400000064000000')
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setInvincible(0)
    sprite('iz410_04', 2)	# 36-37	 **attackbox here**
    sprite('iz410_05', 2)	# 38-39	 **attackbox here**
    sprite('iz410_06', 2)	# 40-41	 **attackbox here**
    sprite('iz410_07', 1)	# 42-42
    sprite('iz410_07', 1)	# 43-43
    Unknown1043()

@State
def Warp_D_Air():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
            Unknown2006()
            Unknown22000()
            Unknown22002()
            Unknown3029(0)
            Unknown23015(0)
        clearUponHandler(2)
        if Unknown23145('Shot_A'):
            Unknown30068(1)
        if Unknown23145('Shot_B'):
            Unknown30068(1)
        if Unknown23145('AirShot_A'):
            Unknown30068(1)
        if Unknown23145('AirShot_B'):
            Unknown30068(1)
        if Unknown23145('Shot_D'):
            Unknown30068(1)
        if Unknown23145('AirShot_D'):
            Unknown30068(1)
    sprite('iz410_00', 3)	# 1-3
    sprite('iz410_00', 1)	# 4-4
    Unknown2015(50)
    Unknown1019(50)
    physicsYImpulse(3000)
    setGravity(300)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    tag_voice(1, 'biz211_0', 'biz211_1', 'biz211_2', '')
    sprite('iz410_01', 2)	# 5-6
    sprite('iz410_02', 3)	# 7-9
    SFX_3('izse_04')
    GFX_0('Warp_D_Air_Zanzo00', -1)
    GFX_0('Warp_D_Air_Zanzo01', -1)
    GFX_0('WarpEff_D', 0)
    sprite('iz410_02', 3)	# 10-12
    physicsXImpulse(3000)
    Unknown3032()
    Unknown3004(-40)
    SFX_0('001_airbackdash_0')
    EnableCollision(0)
    setInvincible(1)
    sprite('iz410_00ex01', 3)	# 13-15
    physicsXImpulse(12000)
    Unknown3001(0)
    sprite('iz410_01ex01', 3)	# 16-18
    Unknown1019(800)
    sprite('iz410_02ex01', 1)	# 19-19
    Unknown48('190000000200000033000000160000000200000017000000')
    if (SLOT_51 <= 250000):
        sendToLabel(0)
        clearUponHandler(2)
    else:
        sendToLabel(1)
    label(0)
    Unknown1086(22)
    sprite('iz409_10ex00', 1)	# 20-20	 **attackbox here**
    teleportRelativeX(70000)
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown3004(60)
    Unknown2006()
    Unknown23015(5)
    sprite('iz409_10ex00', 2)	# 21-22	 **attackbox here**
    GFX_0('WarpHoverAura', 1)
    GFX_1('izef_firespark', 0)
    EnableCollision(1)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3072('dc000000640000006400000064000000')
    Unknown3073('3c000000640000006400000064000000')
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setInvincible(0)
    sprite('iz409_11ex00', 2)	# 23-24	 **attackbox here**
    sprite('iz409_12ex00', 2)	# 25-26	 **attackbox here**
    sprite('iz409_13ex00', 2)	# 27-28	 **attackbox here**
    sprite('iz409_14ex00', 1)	# 29-29	 **attackbox here**
    sprite('iz409_15ex00', 1)	# 30-30	 **attackbox here**
    sprite('iz409_16', 1)	# 31-31
    ExitState()
    label(1)
    Unknown1086(22)
    sprite('iz410_02', 2)	# 32-33
    EnableCollision(1)
    teleportRelativeX(70000)
    Unknown1007(-60000)
    Unknown1084(1)
    physicsXImpulse(500)
    physicsYImpulse(2000)
    Unknown3004(60)
    Unknown23015(5)
    SLOT_4 = 1
    sprite('iz410_03', 2)	# 34-35	 **attackbox here**
    GFX_0('WarpHoverAura_Air', 0)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3072('dc000000640000006400000064000000')
    Unknown3073('3c000000640000006400000064000000')
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setInvincible(0)
    sprite('iz410_04', 2)	# 36-37	 **attackbox here**
    sprite('iz410_05', 1)	# 38-38	 **attackbox here**
    sprite('iz410_06', 1)	# 39-39	 **attackbox here**
    sprite('iz410_07', 1)	# 40-40
    sprite('iz410_07', 1)	# 41-41
    Unknown1043()

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(5500)
        AttackP1(80)
        AttackP2(60)
        AirUntechableTime(40)
        Unknown9202(20)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        AirPushbackX(50000)
        ProjectileDurabilityLvl(2)
        Unknown9016(1)
        setInvincible(1)
        MinimumDamagePct(33)
        Unknown2004(1, 0)
        Unknown11056(0)
    sprite('iz430_00', 3)	# 1-3
    sprite('iz430_01', 3)	# 4-6	 **attackbox here**
    sprite('iz430_02', 3)	# 7-9	 **attackbox here**
    Unknown2036(78, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('iz430_03', 3)	# 10-12	 **attackbox here**
    sprite('iz430_04', 3)	# 13-15	 **attackbox here**
    sprite('iz430_02', 3)	# 16-18	 **attackbox here**
    sprite('iz430_03', 3)	# 19-21	 **attackbox here**
    SFX_3('izse_06')
    sprite('iz430_04', 3)	# 22-24	 **attackbox here**
    sprite('iz430_02', 3)	# 25-27	 **attackbox here**
    sprite('iz430_03', 3)	# 28-30	 **attackbox here**
    sprite('iz430_04', 3)	# 31-33	 **attackbox here**
    sprite('iz430_05', 3)	# 34-36	 **attackbox here**
    GFX_0('DD_3d_zanzoh', 0)
    GFX_0('DD_pt_edge', 0)
    GFX_0('DD_pt_circle', 0)
    tag_voice(1, 'biz250_0', 'biz250_1', '', '')
    sprite('iz430_06', 3)	# 37-39	 **attackbox here**
    sprite('iz430_07', 3)	# 40-42	 **attackbox here**
    GFX_0('DD_3Dcircle_out', -1)
    GFX_0('DD_3Dcircle_in', -1)
    sprite('iz430_08', 3)	# 43-45	 **attackbox here**
    sprite('iz430_09', 3)	# 46-48	 **attackbox here**
    sprite('iz430_10', 3)	# 49-51	 **attackbox here**
    sprite('iz430_11', 3)	# 52-54	 **attackbox here**
    sprite('iz430_12', 3)	# 55-57	 **attackbox here**
    sprite('iz430_13', 3)	# 58-60	 **attackbox here**
    sprite('iz430_14', 2)	# 61-62	 **attackbox here**
    sprite('iz430_15', 2)	# 63-64	 **attackbox here**
    sprite('iz430_16', 4)	# 65-68	 **attackbox here**
    sprite('iz430_17', 5)	# 69-73	 **attackbox here**
    sprite('iz430_18', 18)	# 74-91	 **attackbox here**
    sprite('iz430_18', 1)	# 92-92	 **attackbox here**
    sprite('iz430_19ex00', 2)	# 93-94	 **attackbox here**
    sprite('iz430_20ex00', 1)	# 95-95	 **attackbox here**
    tag_voice(0, 'biz251_0', 'biz251_1', '', '')
    ScreenShake(20000, 0)
    GFX_0('DD_sword', -1)
    GFX_0('DD_sword_env', -1)
    GFX_0('DD_3d_swordaura', -1)
    GFX_0('UltimateAssaultAura', 0)
    GFX_0('UltimateAssaultAura_back', 1)
    sprite('iz430_20ex00', 2)	# 96-97	 **attackbox here**
    sprite('iz430_21ex00', 3)	# 98-100	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 101-103	 **attackbox here**
    sprite('iz430_20ex00', 3)	# 104-106	 **attackbox here**
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('iz430_21ex00', 3)	# 107-109	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 110-112	 **attackbox here**
    sprite('iz430_20ex00', 3)	# 113-115	 **attackbox here**
    sprite('iz430_21ex00', 3)	# 116-118	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 119-121	 **attackbox here**
    sprite('iz430_23ex00', 3)	# 122-124	 **attackbox here**
    Unknown21015('44445f33645f73776f72646175726100000000000000000000000000000000008913000000000000')
    sprite('iz430_24ex00', 3)	# 125-127	 **attackbox here**
    sprite('iz430_25', 5)	# 128-132
    WhiffCancelEnable(0)
    sprite('iz430_26', 5)	# 133-137
    sprite('iz430_27', 5)	# 138-142
    sprite('iz430_28', 5)	# 143-147
    sprite('iz430_29', 5)	# 148-152

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(6500)
        AttackP1(80)
        AttackP2(60)
        AirUntechableTime(40)
        Unknown9202(20)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        AirPushbackX(50000)
        ProjectileDurabilityLvl(2)
        Unknown9016(1)
        setInvincible(1)
        MinimumDamagePct(31)
        Unknown2004(1, 0)
        Unknown11056(0)
    sprite('iz430_00', 3)	# 1-3
    sprite('iz430_01', 3)	# 4-6	 **attackbox here**
    sprite('iz430_02', 3)	# 7-9	 **attackbox here**
    Unknown2036(78, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('iz430_03', 3)	# 10-12	 **attackbox here**
    sprite('iz430_04', 3)	# 13-15	 **attackbox here**
    sprite('iz430_02', 3)	# 16-18	 **attackbox here**
    sprite('iz430_03', 3)	# 19-21	 **attackbox here**
    SFX_3('izse_06')
    sprite('iz430_04', 3)	# 22-24	 **attackbox here**
    sprite('iz430_02', 3)	# 25-27	 **attackbox here**
    sprite('iz430_03', 3)	# 28-30	 **attackbox here**
    sprite('iz430_04', 3)	# 31-33	 **attackbox here**
    sprite('iz430_05', 3)	# 34-36	 **attackbox here**
    GFX_0('DD_3d_zanzoh', 0)
    GFX_0('DD_pt_edge', 0)
    GFX_0('DD_pt_circle', 0)
    tag_voice(1, 'biz250_0', 'biz250_1', '', '')
    sprite('iz430_06', 3)	# 37-39	 **attackbox here**
    sprite('iz430_07', 3)	# 40-42	 **attackbox here**
    GFX_0('DD_3Dcircle_out', -1)
    GFX_0('DD_3Dcircle_in', -1)
    sprite('iz430_08', 3)	# 43-45	 **attackbox here**
    sprite('iz430_09', 3)	# 46-48	 **attackbox here**
    sprite('iz430_10', 3)	# 49-51	 **attackbox here**
    sprite('iz430_11', 3)	# 52-54	 **attackbox here**
    sprite('iz430_12', 3)	# 55-57	 **attackbox here**
    sprite('iz430_13', 3)	# 58-60	 **attackbox here**
    sprite('iz430_14', 2)	# 61-62	 **attackbox here**
    sprite('iz430_15', 2)	# 63-64	 **attackbox here**
    sprite('iz430_16', 4)	# 65-68	 **attackbox here**
    sprite('iz430_17', 5)	# 69-73	 **attackbox here**
    sprite('iz430_18', 18)	# 74-91	 **attackbox here**
    sprite('iz430_18', 1)	# 92-92	 **attackbox here**
    sprite('iz430_19ex00', 2)	# 93-94	 **attackbox here**
    sprite('iz430_20ex01', 1)	# 95-95	 **attackbox here**
    tag_voice(0, 'biz251_0', 'biz251_1', '', '')
    ScreenShake(20000, 0)
    GFX_0('DD_sword_OD', -1)
    GFX_0('DD_sword_env_OD', -1)
    GFX_0('DD_3d_swordaura', -1)
    GFX_0('UltimateAssaultAura', 0)
    GFX_0('UltimateAssaultAura_back', 1)
    sprite('iz430_20ex01', 2)	# 96-97	 **attackbox here**
    sprite('iz430_21ex01', 3)	# 98-100	 **attackbox here**
    sprite('iz430_22ex01', 3)	# 101-103	 **attackbox here**
    sprite('iz430_20ex01', 3)	# 104-106	 **attackbox here**
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('iz430_21ex01', 3)	# 107-109	 **attackbox here**
    sprite('iz430_22ex01', 3)	# 110-112	 **attackbox here**
    sprite('iz430_20ex00', 3)	# 113-115	 **attackbox here**
    sprite('iz430_21ex00', 3)	# 116-118	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 119-121	 **attackbox here**
    sprite('iz430_23ex00', 3)	# 122-124	 **attackbox here**
    Unknown21015('44445f33645f73776f72646175726100000000000000000000000000000000008913000000000000')
    sprite('iz430_24ex00', 3)	# 125-127	 **attackbox here**
    sprite('iz430_25', 5)	# 128-132
    sprite('iz430_26', 5)	# 133-137
    sprite('iz430_27', 5)	# 138-142
    sprite('iz430_28', 5)	# 143-147
    sprite('iz430_29', 5)	# 148-152

@State
def UltimateStrike():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2200)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(70)
        Unknown9142(65)
        Unknown11072(1, 300000, 0)
        PushbackX(19800)
        Unknown9016(1)
        blockstun(26)
        Hitstop(20)
        MinimumDamagePct(20)
        Unknown11064(1)
        Unknown11068(1)
        Unknown2073(1)
        setInvincible(1)
        Unknown1084(1)

        def upon_78():
            Unknown13024(0)
            enterState('UltimateStrikeAdd')
            Unknown11069('BurstDDFunnel')
            Unknown11084(1)

        def upon_61():
            PushbackX(39900)

        def upon_11():
            ScreenShake(10000, 50000)
    sprite('iz204_00', 2)	# 1-2
    sprite('iz204_01', 1)	# 3-3
    sprite('iz204_02', 2)	# 4-5
    GFX_0('KakuseiMagicCircleDD', -1)
    GFX_0('InstallDD', -1)
    Unknown4049(800)
    Unknown4045('697a65665f6472697665636972636c655f66726f6e7400000000000000000000ffffffff')
    Unknown4054(5)
    Unknown4049(800)
    Unknown4045('697a65665f6472697665636972636c6500000000000000000000000000000000ffffffff')
    GFX_0('KakuseiAuraDD', 0)
    GFX_0('KakuseiAuraDD_oku', 1)
    GFX_0('5DLightsaber_onDD', -1)
    SFX_0('022_magiccircle_b')
    sprite('iz204_03', 2)	# 6-7
    sprite('iz204_04', 60)	# 8-67
    Unknown2036(69, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('iz440_00', 3)	# 68-70	 **attackbox here**
    sprite('iz440_01', 3)	# 71-73	 **attackbox here**
    tag_voice(1, 'biz280_0', 'biz280_1', '', '')
    sprite('iz440_02', 2)	# 74-75	 **attackbox here**
    sprite('iz440_03', 3)	# 76-78	 **attackbox here**
    sprite('iz440_04', 1)	# 79-79	 **attackbox here**
    sprite('iz440_04', 1)	# 80-80	 **attackbox here**
    Unknown2015(200)
    sprite('iz311_05ex01', 2)	# 81-82
    teleportRelativeX(100000)
    Unknown2015(250)
    SFX_0('006_swing_blade_2')
    sprite('iz311_06ex01', 3)	# 83-85	 **attackbox here**
    teleportRelativeX(90000)
    sprite('iz311_06ex01', 8)	# 86-93	 **attackbox here**
    StartMultihit()
    setInvincible(0)
    Unknown2015(-1)
    sprite('iz311_07ex01', 6)	# 94-99
    sprite('iz311_08ex01', 6)	# 100-105
    sprite('iz311_09ex01', 6)	# 106-111
    teleportRelativeX(-60000)
    sprite('iz311_10ex01', 6)	# 112-117
    teleportRelativeX(-60000)
    sprite('iz311_11ex01', 5)	# 118-122
    teleportRelativeX(-70000)
    sprite('iz311_12ex01', 9)	# 123-131

@State
def UltimateStrikeAdd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        MinimumDamagePct(10)
        Unknown13024(0)
        setInvincible(1)
        Unknown11084(1)

        def upon_43():
            if (SLOT_48 == 6002):
                sendToLabel(1)
            if (SLOT_48 == 6003):
                sendToLabel(2)
            if (SLOT_48 == 6014):
                Unknown13024(1)
    sprite('iz311_06ex01', 3)	# 1-3	 **attackbox here**
    GFX_0('BurstDD_MagicCircle', -1)
    GFX_0('BurstDDCamera', -1)
    StartMultihit()
    sprite('iz311_07ex01', 6)	# 4-9
    sprite('iz311_08ex01', 6)	# 10-15
    sprite('iz311_09ex01', 4)	# 16-19
    physicsXImpulse(-10000)
    sprite('iz311_10ex01', 4)	# 20-23
    Unknown1019(25)
    sprite('iz311_11ex01', 4)	# 24-27
    Unknown1019(25)
    sprite('iz400_01ex01', 4)	# 28-31
    tag_voice(0, 'biz281_0', 'biz281_1', '', '')
    GFX_0('BurstDDFunnel', -1)
    sprite('iz400_02ex01', 4)	# 32-35
    Unknown1019(0)
    sprite('iz400_03ex01', 4)	# 36-39
    sprite('iz400_04ex01', 4)	# 40-43
    sprite('iz400_05ex01', 4)	# 44-47
    label(100)
    sprite('iz400_06ex01', 4)	# 48-51
    sprite('iz400_07ex01', 4)	# 52-55
    sprite('iz400_08ex01', 4)	# 56-59
    gotoLabel(100)
    label(1)
    sprite('iz400_09ex01', 4)	# 60-63
    sprite('iz440_05', 4)	# 64-67
    sprite('iz440_06', 4)	# 68-71
    sprite('iz440_07', 4)	# 72-75
    GFX_0('BurstDDSlashEff', -1)
    sprite('iz440_08', 4)	# 76-79
    sprite('iz440_09', 4)	# 80-83
    sprite('iz440_10', 4)	# 84-87
    label(200)
    sprite('iz440_11', 4)	# 88-91
    sprite('iz440_12', 4)	# 92-95
    sprite('iz440_13', 4)	# 96-99
    gotoLabel(200)
    label(2)
    sprite('iz440_14', 3)	# 100-102
    sprite('iz440_15', 3)	# 103-105
    sprite('iz440_16', 3)	# 106-108
    sprite('iz440_17', 3)	# 109-111
    sprite('iz440_18', 3)	# 112-114
    sprite('iz440_19', 3)	# 115-117
    sprite('iz440_20', 3)	# 118-120
    sprite('iz440_21', 3)	# 121-123
    sprite('iz440_22', 3)	# 124-126
    sprite('iz440_23', 3)	# 127-129
    sprite('iz440_21', 3)	# 130-132
    sprite('iz440_22', 3)	# 133-135
    sprite('iz440_23', 3)	# 136-138
    sprite('iz440_21', 3)	# 139-141
    sprite('iz440_22', 3)	# 142-144
    sprite('iz440_23', 3)	# 145-147
    sprite('iz440_21', 3)	# 148-150
    sprite('iz440_22', 3)	# 151-153
    sprite('iz440_23', 3)	# 154-156
    sprite('iz440_21', 3)	# 157-159
    tag_voice(0, 'biz282_0', 'biz282_1', '', '')
    sprite('iz440_22', 3)	# 160-162
    sprite('iz440_23', 3)	# 163-165
    sprite('iz440_24', 6)	# 166-171
    sprite('iz440_25', 6)	# 172-177
    sprite('iz440_26', 2)	# 178-179
    sprite('iz440_27', 3)	# 180-182
    GFX_0('BurstDDSlashEff2', -1)
    sprite('iz440_28', 3)	# 183-185
    sprite('iz440_29', 3)	# 186-188
    sprite('iz440_27', 3)	# 189-191
    sprite('iz440_28', 3)	# 192-194
    sprite('iz440_29', 3)	# 195-197
    sprite('iz440_27', 3)	# 198-200
    sprite('iz440_28', 3)	# 201-203
    sprite('iz440_29', 3)	# 204-206
    sprite('iz440_27', 3)	# 207-209
    sprite('iz440_28', 3)	# 210-212
    sprite('iz440_29', 3)	# 213-215
    sprite('iz440_27', 3)	# 216-218
    sprite('iz440_28', 3)	# 219-221
    sprite('iz440_29', 3)	# 222-224
    GFX_0('BurstDDRetrunEff', -1)
    sprite('iz440_30', 5)	# 225-229
    Unknown21015('4275727374444443616d657261000000000000000000000000000000000000007417000000000000')
    setInvincible(0)
    sprite('iz440_31', 5)	# 230-234
    sprite('iz203_06ex01', 5)	# 235-239
    sprite('iz203_07ex01', 5)	# 240-244
    sprite('iz203_08ex01', 5)	# 245-249
    loopRest()

@State
def UltimateStrike_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2200)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(70)
        Unknown9142(65)
        Unknown11072(1, 300000, 0)
        PushbackX(19800)
        Unknown9016(1)
        blockstun(26)
        Hitstop(20)
        MinimumDamagePct(25)
        Unknown11064(1)
        Unknown11068(1)
        Unknown2073(1)
        setInvincible(1)
        Unknown1084(1)

        def upon_78():
            Unknown13024(0)
            enterState('UltimateStrike_ODAdd')
            Unknown11069('BurstDDFunnel')
            Unknown11084(1)

        def upon_61():
            PushbackX(39900)

        def upon_11():
            ScreenShake(10000, 50000)
    sprite('iz204_00', 2)	# 1-2
    sprite('iz204_01', 1)	# 3-3
    sprite('iz204_02', 2)	# 4-5
    GFX_0('KakuseiMagicCircleDD', -1)
    GFX_0('InstallDD', -1)
    Unknown4049(800)
    Unknown4045('697a65665f6472697665636972636c655f66726f6e7400000000000000000000ffffffff')
    Unknown4054(5)
    Unknown4049(800)
    Unknown4045('697a65665f6472697665636972636c6500000000000000000000000000000000ffffffff')
    GFX_0('KakuseiAuraDD', 0)
    GFX_0('KakuseiAuraDD_oku', 1)
    GFX_0('5DLightsaber_onDD', -1)
    SFX_0('022_magiccircle_b')
    sprite('iz204_03', 2)	# 6-7
    sprite('iz204_04', 60)	# 8-67
    Unknown2036(69, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('iz440_00', 3)	# 68-70	 **attackbox here**
    sprite('iz440_01', 3)	# 71-73	 **attackbox here**
    tag_voice(1, 'biz280_0', 'biz280_1', '', '')
    sprite('iz440_02', 2)	# 74-75	 **attackbox here**
    sprite('iz440_03', 3)	# 76-78	 **attackbox here**
    sprite('iz440_04', 1)	# 79-79	 **attackbox here**
    sprite('iz440_04', 1)	# 80-80	 **attackbox here**
    Unknown2015(200)
    sprite('iz311_05ex01', 2)	# 81-82
    teleportRelativeX(100000)
    Unknown2015(250)
    SFX_0('006_swing_blade_2')
    sprite('iz311_06ex01', 3)	# 83-85	 **attackbox here**
    teleportRelativeX(90000)
    sprite('iz311_06ex01', 8)	# 86-93	 **attackbox here**
    StartMultihit()
    setInvincible(0)
    Unknown2015(-1)
    sprite('iz311_07ex01', 6)	# 94-99
    sprite('iz311_08ex01', 6)	# 100-105
    sprite('iz311_09ex01', 6)	# 106-111
    teleportRelativeX(-60000)
    sprite('iz311_10ex01', 6)	# 112-117
    teleportRelativeX(-60000)
    sprite('iz311_11ex01', 5)	# 118-122
    teleportRelativeX(-70000)
    sprite('iz311_12ex01', 9)	# 123-131

@State
def UltimateStrike_ODAdd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        MinimumDamagePct(10)
        Unknown13024(0)
        setInvincible(1)
        Unknown11084(1)

        def upon_43():
            if (SLOT_48 == 6002):
                sendToLabel(1)
            if (SLOT_48 == 6003):
                sendToLabel(2)
            if (SLOT_48 == 6014):
                Unknown13024(1)
    sprite('iz311_06ex01', 3)	# 1-3	 **attackbox here**
    GFX_0('BurstDD_MagicCircle', -1)
    GFX_0('BurstDDCamera', -1)
    StartMultihit()
    sprite('iz311_07ex01', 6)	# 4-9
    sprite('iz311_08ex01', 6)	# 10-15
    sprite('iz311_09ex01', 4)	# 16-19
    physicsXImpulse(-10000)
    sprite('iz311_10ex01', 4)	# 20-23
    Unknown1019(25)
    sprite('iz311_11ex01', 4)	# 24-27
    Unknown1019(25)
    sprite('iz400_01ex01', 4)	# 28-31
    tag_voice(0, 'biz281_0', 'biz281_1', '', '')
    GFX_0('BurstDDFunnel', -1)
    Unknown23029(1, 6001, 0)
    sprite('iz400_02ex01', 4)	# 32-35
    Unknown1019(0)
    sprite('iz400_03ex01', 4)	# 36-39
    sprite('iz400_04ex01', 4)	# 40-43
    sprite('iz400_05ex01', 4)	# 44-47
    label(100)
    sprite('iz400_06ex01', 4)	# 48-51
    sprite('iz400_07ex01', 4)	# 52-55
    sprite('iz400_08ex01', 4)	# 56-59
    gotoLabel(100)
    label(1)
    sprite('iz400_09ex01', 4)	# 60-63
    sprite('iz440_05', 4)	# 64-67
    sprite('iz440_06', 4)	# 68-71
    sprite('iz440_07', 4)	# 72-75
    GFX_0('BurstDDSlashEff', -1)
    sprite('iz440_08', 4)	# 76-79
    sprite('iz440_09', 4)	# 80-83
    sprite('iz440_10', 4)	# 84-87
    label(200)
    sprite('iz440_11', 4)	# 88-91
    sprite('iz440_12', 4)	# 92-95
    sprite('iz440_13', 4)	# 96-99
    gotoLabel(200)
    label(2)
    sprite('iz440_14', 3)	# 100-102
    sprite('iz440_15', 3)	# 103-105
    sprite('iz440_16', 3)	# 106-108
    sprite('iz440_17', 3)	# 109-111
    sprite('iz440_18', 3)	# 112-114
    sprite('iz440_19', 3)	# 115-117
    sprite('iz440_20', 3)	# 118-120
    sprite('iz440_21', 3)	# 121-123
    sprite('iz440_22', 3)	# 124-126
    sprite('iz440_23', 3)	# 127-129
    sprite('iz440_21', 3)	# 130-132
    sprite('iz440_22', 3)	# 133-135
    sprite('iz440_23', 3)	# 136-138
    sprite('iz440_21', 3)	# 139-141
    sprite('iz440_22', 3)	# 142-144
    sprite('iz440_23', 3)	# 145-147
    sprite('iz440_21', 3)	# 148-150
    sprite('iz440_22', 3)	# 151-153
    sprite('iz440_23', 3)	# 154-156
    sprite('iz440_21', 3)	# 157-159
    tag_voice(0, 'biz282_0', 'biz282_1', '', '')
    sprite('iz440_22', 3)	# 160-162
    sprite('iz440_23', 3)	# 163-165
    sprite('iz440_24', 6)	# 166-171
    sprite('iz440_25', 6)	# 172-177
    sprite('iz440_26', 2)	# 178-179
    sprite('iz440_27', 3)	# 180-182
    GFX_0('BurstDDSlashEff2', -1)
    sprite('iz440_28', 3)	# 183-185
    sprite('iz440_29', 3)	# 186-188
    sprite('iz440_27', 3)	# 189-191
    sprite('iz440_28', 3)	# 192-194
    sprite('iz440_29', 3)	# 195-197
    sprite('iz440_27', 3)	# 198-200
    sprite('iz440_28', 3)	# 201-203
    sprite('iz440_29', 3)	# 204-206
    sprite('iz440_27', 3)	# 207-209
    sprite('iz440_28', 3)	# 210-212
    sprite('iz440_29', 3)	# 213-215
    sprite('iz440_27', 3)	# 216-218
    sprite('iz440_28', 3)	# 219-221
    sprite('iz440_29', 3)	# 222-224
    GFX_0('BurstDDRetrunEff', -1)
    sprite('iz440_30', 5)	# 225-229
    Unknown21015('4275727374444443616d657261000000000000000000000000000000000000007417000000000000')
    setInvincible(0)
    sprite('iz440_31', 5)	# 230-234
    sprite('iz203_06ex01', 5)	# 235-239
    sprite('iz203_07ex01', 5)	# 240-244
    sprite('iz203_08ex01', 5)	# 245-249
    loopRest()

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown1084(1)
        Unknown11064(1)
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(200)
        Damage(0)
        AirUntechableTime(1000)
        hitstun(1000)
        Unknown9310(200)
        Hitstop(20)
        Unknown11001(-5, 1000, 1000)
        Unknown11072(3, 128000, -256000)
        Unknown11068(1)
        Unknown11078(1)
        MinimumDamagePct(100)
        Unknown9016(1)
        Unknown11067(1)
        setInvincible(1)

        def upon_12():
            enterState('AstralHeatExe')
            Unknown23088(1, 1)
    sprite('iz450_00', 3)	# 1-3
    tag_voice(1, 'biz290_0', 'biz290_1', '', '')
    sprite('iz450_01', 3)	# 4-6
    Unknown2036(131, -1, 2)
    Unknown23147()
    Unknown20000(1)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_IZ_AH', -1)
    sprite('iz450_02', 3)	# 7-9
    sprite('iz450_03', 3)	# 10-12
    sprite('iz450_04', 3)	# 13-15
    sprite('iz450_02', 3)	# 16-18
    GFX_0('AST1st_mahojin', -1)
    sprite('iz450_03', 3)	# 19-21
    sprite('iz450_04', 3)	# 22-24
    sprite('iz450_02', 3)	# 25-27
    sprite('iz450_03', 3)	# 28-30
    sprite('iz450_04', 3)	# 31-33
    sprite('iz450_02', 3)	# 34-36
    sprite('iz450_03', 3)	# 37-39
    sprite('iz450_04', 3)	# 40-42
    sprite('iz450_02', 3)	# 43-45
    sprite('iz450_03', 3)	# 46-48
    sprite('iz450_04', 3)	# 49-51
    sprite('iz450_05', 6)	# 52-57
    sprite('iz450_06', 6)	# 58-63
    sprite('iz450_07', 4)	# 64-67
    GFX_1('izef_AH_changelightA', -1)
    sprite('iz450_08', 4)	# 68-71
    sprite('iz450_09', 4)	# 72-75
    sprite('iz450_07', 4)	# 76-79
    Unknown23119(16777215, 12, 1)
    sprite('iz450_08', 4)	# 80-83
    sprite('iz450_09', 4)	# 84-87
    sprite('iz450_07', 4)	# 88-91
    sprite('iz450_08', 4)	# 92-95
    GFX_0('AST_changeBG', 0)
    sprite('iz450_09', 4)	# 96-99
    GFX_1('izef_AH_changelightB', 0)
    GFX_0('AST_changelightC', 0)
    SFX_0('022_magiccircle_b')
    SFX_0('022_magiccircle_b')
    sprite('iz450_10', 6)	# 100-105
    Unknown23119(0, 12, 1)
    sprite('iz450_11', 16)	# 106-121
    GFX_0('AST_1stAuraR', 0)
    GFX_0('AST_1stAuraL', 1)
    sprite('iz450_12', 6)	# 122-127
    sprite('iz450_13', 6)	# 128-133
    sprite('iz450_14', 6)	# 134-139
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(0)
    Unknown3071(5)
    Unknown3074('0000000000000000ff00000080000000')
    Unknown3075('0000000000000000ff00000080000000')
    Unknown3076(1000)
    Unknown3077(1500)
    sprite('iz450_15', 6)	# 140-145
    sprite('iz450_16', 3)	# 146-148	 **attackbox here**
    physicsXImpulse(60000)
    sprite('iz450_17', 3)	# 149-151	 **attackbox here**
    sprite('iz450_18', 3)	# 152-154	 **attackbox here**
    sprite('iz450_19', 5)	# 155-159
    setInvincible(0)
    Unknown1019(80)
    Unknown23118(-1)
    Unknown23119(0, 8, 1)
    GFX_1('izef_dellight', 0)
    GFX_1('izef_dellight', 1)
    GFX_1('izef_dellight', 2)
    GFX_1('izef_dellight', 3)
    GFX_1('izef_dellight', 4)
    GFX_1('izef_dellight', 5)
    GFX_1('izef_dellight', 6)
    GFX_1('izef_dellight', 7)
    sprite('iz450_20', 5)	# 160-164
    Unknown1019(60)
    sprite('iz450_21', 5)	# 165-169
    Unknown1019(40)
    sprite('iz450_22', 5)	# 170-174
    Unknown1019(10)
    sprite('iz450_23', 5)	# 175-179
    physicsXImpulse(0)
    Unknown3029(0)
    sprite('iz450_24', 5)	# 180-184
    sprite('iz450_25', 5)	# 185-189

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        Unknown11069('AstralHeatExe')
        Unknown9016(1)
        Unknown23088(1, 1)
        Unknown23157(1)
        Unknown20000(1)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20004(1)
        Unknown23084(1)
    sprite('iz450_16', 3)	# 1-3	 **attackbox here**
    GFX_0('AstWhite', -1)
    StartMultihit()
    sprite('iz450_17', 3)	# 4-6	 **attackbox here**
    StartMultihit()
    sprite('iz450_18', 3)	# 7-9	 **attackbox here**
    Unknown1000(0)
    teleportRelativeY(0)
    StartMultihit()
    sprite('iz450_16', 1)	# 10-10	 **attackbox here**
    StartMultihit()
    sprite('null', 195)	# 11-205
    GFX_0('iz450cutin', -1)
    Unknown23024(3)
    teleportRelativeY(7800000)
    Unknown3001(0)
    Unknown36(22)
    Unknown3038(1)
    teleportRelativeY(6000000)
    Unknown1000(0)
    setGravity(0)
    Unknown35()
    sprite('null', 45)	# 206-250
    GFX_0('AST_2ndAura', -1)
    sprite('null', 60)	# 251-310
    GFX_0('iz450dammy', -1)
    sprite('null', 40)	# 311-350
    SFX_3('izse_09')
    sprite('null', 115)	# 351-465
    sprite('null', 5)	# 466-470
    ScreenShake(0, 2000)
    SFX_0('019_quake_1')
    sprite('null', 5)	# 471-475
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 476-480
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 481-485
    ScreenShake(0, 2000)
    sprite('null', 5)	# 486-490
    ScreenShake(0, 2000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 491-495
    ScreenShake(0, 2000)
    Unknown7014('izse_09_loop')
    SFX_0('019_quake_0')
    sprite('null', 5)	# 496-500
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 501-505
    ScreenShake(0, 3000)
    sprite('null', 5)	# 506-510
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 511-515
    ScreenShake(0, 3000)
    sprite('null', 5)	# 516-520
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 521-525
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 526-530
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 531-535
    ScreenShake(0, 5000)
    sprite('null', 5)	# 536-540
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 541-545
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 546-550
    ScreenShake(0, 5000)
    Unknown7015()
    SFX_0('019_quake_0')
    sprite('null', 5)	# 551-555
    ScreenShake(0, 5000)
    sprite('null', 5)	# 556-560
    SFX_3('izse_10')
    ScreenShake(0, 30000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 561-565
    ScreenShake(0, 30000)
    sprite('null', 5)	# 566-570
    ScreenShake(0, 20000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 571-575
    ScreenShake(0, 20000)
    sprite('null', 5)	# 576-580
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    sprite('null', 5)	# 581-585
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    sprite('null', 20)	# 586-605
    GFX_0('AstWhitefinish', -1)
    GFX_0('izef_ah_Ryuhai', -1)
    sprite('null', 5)	# 606-610
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('null', 1)	# 611-611
    Unknown23024(2)
    sprite('null', 10)	# 612-621
    Unknown1000(0)
    teleportRelativeY(6000000)
    setGravity(0)
    GFX_0('ASTbg', -1)
    sprite('null', 60)	# 622-681
    GFX_0('izef_ah_javelin2', -1)
    sprite('null', 30)	# 682-711
    Unknown21015('41535462670000000000000000000000000000000000000000000000000000002923000000000000')
    GFX_0('izef_ah_javelin3', -1)
    GFX_1('izef_ahfinish_nigiyakasi', -1)
    Unknown36(22)
    Unknown3038(0)
    Unknown23015(2)
    Unknown1096(600)
    Unknown1007(100000)
    Unknown35()
    sprite('null', 15)	# 712-726
    ScreenShake(15000, 15000)
    SFX_0('025_cleanhit_slash')
    sprite('null', 90)	# 727-816
    GFX_0('AstralHeatKillObject', -1)
    ScreenShake(300000, 300000)
    Unknown21015('697a65665f61685f6a6176656c696e30300000000000000000000000000000002a23000000000000')
    Unknown21015('697a65665f61685f6a6176656c696e5f6261636b6669726530300000000000002b23000000000000')
    sprite('iz450_44', 10)	# 817-826	 **attackbox here**
    Unknown23024(0)
    Unknown20000(1)
    Unknown20007(1)
    Unknown20004(1)
    sprite('iz450_44', 7)	# 827-833	 **attackbox here**
    Unknown2008()
    Unknown3001(255)
    Unknown1000(200000)
    teleportRelativeY(0)
    Unknown4045('697a65665f61685f66696e69736868616e650000000000000000000000000000ffffffff')
    Unknown36(22)
    Unknown3038(1)
    Unknown35()
    sprite('iz450_45', 7)	# 834-840	 **attackbox here**
    sprite('iz450_46', 7)	# 841-847	 **attackbox here**
    sprite('iz450_47', 7)	# 848-854	 **attackbox here**
    sprite('iz450_48', 7)	# 855-861	 **attackbox here**
    Unknown18010()
    Unknown21011(90)
    sprite('iz450_44', 7)	# 862-868	 **attackbox here**
    SFX_1('iz408')
    sprite('iz450_45', 7)	# 869-875	 **attackbox here**
    sprite('iz450_46', 7)	# 876-882	 **attackbox here**
    sprite('iz450_47', 7)	# 883-889	 **attackbox here**
    sprite('iz450_48', 7)	# 890-896	 **attackbox here**
    sprite('iz450_44', 7)	# 897-903	 **attackbox here**
    sprite('iz450_45', 7)	# 904-910	 **attackbox here**
    sprite('iz450_46', 7)	# 911-917	 **attackbox here**
    sprite('iz450_47', 7)	# 918-924	 **attackbox here**
    sprite('iz450_48', 7)	# 925-931	 **attackbox here**
    sprite('iz450_44', 7)	# 932-938	 **attackbox here**
    sprite('iz450_45', 7)	# 939-945	 **attackbox here**
    sprite('iz450_46', 7)	# 946-952	 **attackbox here**
    sprite('iz450_47', 7)	# 953-959	 **attackbox here**
    sprite('iz450_48', 7)	# 960-966	 **attackbox here**
    sprite('iz450_44', 7)	# 967-973	 **attackbox here**
    sprite('iz450_45', 7)	# 974-980	 **attackbox here**
    sprite('iz450_46', 7)	# 981-987	 **attackbox here**
    sprite('iz450_47', 7)	# 988-994	 **attackbox here**
    sprite('iz450_48', 7)	# 995-1001	 **attackbox here**
    sprite('iz450_44', 7)	# 1002-1008	 **attackbox here**
    sprite('iz450_45', 7)	# 1009-1015	 **attackbox here**
    sprite('iz450_46', 7)	# 1016-1022	 **attackbox here**
    sprite('iz450_47', 7)	# 1023-1029	 **attackbox here**
    sprite('iz450_48', 7)	# 1030-1036	 **attackbox here**
    sprite('iz450_44', 7)	# 1037-1043	 **attackbox here**
    sprite('iz450_45', 7)	# 1044-1050	 **attackbox here**
    sprite('iz450_46', 7)	# 1051-1057	 **attackbox here**
    sprite('iz450_47', 7)	# 1058-1064	 **attackbox here**
    sprite('iz450_48', 7)	# 1065-1071	 **attackbox here**
    Unknown23018(1)
    label(0)
    sprite('iz450_44', 7)	# 1072-1078	 **attackbox here**
    sprite('iz450_45', 7)	# 1079-1085	 **attackbox here**
    sprite('iz450_46', 7)	# 1086-1092	 **attackbox here**
    sprite('iz450_47', 7)	# 1093-1099	 **attackbox here**
    sprite('iz450_48', 7)	# 1100-1106	 **attackbox here**
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
    label(0)
    sprite('null', 1)	# 1-1
    EnableCollision(0)
    Unknown2034(0)
    teleportRelativeY(0)
    gotoLabel(0)

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('iz300_00', 2)	# 1-2
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('iz300_01', 2)	# 3-4
    sprite('iz300_02', 2)	# 5-6
    SFX_1('biz404')
    sprite('iz300_03', 20)	# 7-26
    SFX_3('izse_01')
    sprite('iz300_04', 3)	# 27-29
    sprite('iz300_05', 18)	# 30-47	 **attackbox here**
    StartMultihit()
    sprite('iz300_06', 3)	# 48-50	 **attackbox here**
    sprite('iz300_07', 3)	# 51-53	 **attackbox here**
    sprite('iz300_08', 3)	# 54-56	 **attackbox here**
    sprite('iz300_09', 3)	# 57-59
    sprite('iz300_10', 3)	# 60-62
    sprite('iz300_11', 3)	# 63-65
    sprite('iz300_12', 3)	# 66-68

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
    sprite('iz045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('iz045_00', 3)	# 2-4
    sprite('iz045_01', 4)	# 5-8
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    SFX_0('301_overdrive_end')
    label(0)
    sprite('iz045_02', 5)	# 9-13
    sprite('iz045_02', 5)	# 14-18
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
    sprite('iz045_01', 6)	# 19-24
    sprite('iz045_00', 6)	# 25-30

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('iz033_02', 3)	# 1-3
    sprite('iz033_03', 3)	# 4-6
    sprite('iz033_02', 3)	# 7-9
    sprite('iz033_03', 3)	# 10-12
    sprite('iz033_02', 3)	# 13-15
    sprite('iz033_03', 3)	# 16-18
    sprite('iz033_02', 3)	# 19-21
    sprite('iz033_03', 3)	# 22-24
    sprite('iz033_02', 3)	# 25-27
    sprite('iz033_03', 3)	# 28-30
    sprite('iz033_02', 30)	# 31-60

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('iz001_00', 7)	# 1-7
    Unknown1084(1)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('iz001_01', 7)	# 8-14
    sprite('iz001_02', 7)	# 15-21
    sprite('iz001_03', 7)	# 22-28
    sprite('iz001_04', 7)	# 29-35
    sprite('iz001_05', 7)	# 36-42
    sprite('iz001_06', 7)	# 43-49
    sprite('iz001_07', 7)	# 50-56
    sprite('iz001_08', 7)	# 57-63
    sprite('iz001_04', 7)	# 64-70
    label(1)
    Unknown30042(24)
    if SLOT_ReturnVal:
        _gotolabel(2)
    sprite('iz001_05', 7)	# 71-77
    sprite('iz001_06', 7)	# 78-84
    sprite('iz001_07', 7)	# 85-91
    sprite('iz001_08', 7)	# 92-98
    sprite('iz001_04', 7)	# 99-105
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('iz001_09', 7)	# 106-112
    sprite('iz001_10', 7)	# 113-119
    sprite('iz001_11', 7)	# 120-126

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('iz001_00', 7)	# 1-7
    sprite('iz001_01', 7)	# 8-14
    sprite('iz001_02', 7)	# 15-21
    sprite('iz001_03', 7)	# 22-28
    sprite('iz001_04', 7)	# 29-35
    sprite('iz001_05', 7)	# 36-42
    sprite('iz001_06', 7)	# 43-49
    sprite('iz001_07', 7)	# 50-56
    sprite('iz001_08', 7)	# 57-63
    sprite('iz001_04', 7)	# 64-70
    sprite('iz001_05', 6)	# 71-76

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
    sprite('iz252_02', 1)	# 631-631
    Unknown1086(22)
    teleportRelativeX(-300000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    physicsXImpulse(320000)
    physicsYImpulse(-200000)
    setGravity(0)
    sprite('iz252_03', 30)	# 632-661
    GFX_0('AIR5CZanzo', 0)
    label(9)
    sprite('iz252_04', 3)	# 662-664	 **attackbox here**
    SFX_0('019_cloth_a')
    Unknown1019(30)
    EnableCollision(1)
    Unknown2053(1)
    sprite('iz024_01', 3)	# 665-667
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown26('AIR5CZanzo')
    sprite('iz024_02', 12)	# 668-679
    sprite('iz024_03', 3)	# 680-682
    sprite('iz024_04', 4)	# 683-686

@State
def CmnActChangeReturnAppealBurst():
    sprite('iz064_02', 90)	# 1-90

@State
def CmnActChangePartnerQuickIn():
    sprite('iz032_08', 3)	# 1-3	 **attackbox here**
    sprite('iz032_08', 5)	# 4-8	 **attackbox here**
    sprite('iz032_09', 7)	# 9-15
    sprite('iz032_10', 7)	# 16-22
    sprite('iz032_11', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('iz033_00', 1)	# 1-1
    sprite('iz033_01', 2)	# 2-3
    sprite('iz033_02', 2)	# 4-5
    sprite('iz033_02', 1)	# 6-6
    sprite('iz033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('iz033_02', 3)	# 10-12
    sprite('iz033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz033_04', 3)	# 16-18
    sprite('iz033_05', 3)	# 19-21

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
    sprite('iz020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('iz020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('iz010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11042(1)
        Unknown11056(0)
        Unknown1084(1)
    sprite('iz204_00', 2)	# 1-2
    sprite('iz204_01', 1)	# 3-3
    sprite('iz204_02', 3)	# 4-6
    GFX_0('KakuseiAura', 0)
    GFX_0('KakuseiAura_oku', 1)
    GFX_0('5DLightsaber_on', -1)
    SFX_0('022_magiccircle_b')
    sprite('iz204_03', 3)	# 7-9
    sprite('iz204_04', 3)	# 10-12
    sprite('iz204_02ex00', 3)	# 13-15
    sprite('iz204_03ex00', 3)	# 16-18
    sprite('iz204_04', 3)	# 19-21
    sprite('iz204_05', 2)	# 22-23
    sprite('iz204_06', 1)	# 24-24
    sprite('iz400_00', 3)	# 25-27
    tag_voice(1, 'biz201_0', 'biz201_2', '', '')
    sprite('iz400_01ex00', 3)	# 28-30	 **attackbox here**
    GFX_0('Special_Shot_PS', 0)
    sprite('iz400_02ex00', 3)	# 31-33	 **attackbox here**
    sprite('iz400_03ex00', 3)	# 34-36	 **attackbox here**
    Unknown1084(1)
    GFX_0('ShotD_Aura', 1)
    sprite('iz400_04ex00', 3)	# 37-39	 **attackbox here**
    SFX_3('izse_05')
    GFX_0('ShotD_Aura_back', 0)
    physicsXImpulse(-10000)
    physicsYImpulse(3000)
    setGravity(700)
    sprite('iz400_05ex00', 3)	# 40-42	 **attackbox here**
    sprite('iz400_06ex00', 3)	# 43-45	 **attackbox here**
    sprite('iz400_07ex00', 3)	# 46-48	 **attackbox here**
    sprite('iz400_08ex00', 120)	# 49-168	 **attackbox here**
    sendToLabelUpon(2, 0)
    loopRest()
    label(0)
    sprite('iz400_09ex00', 2)	# 169-170	 **attackbox here**
    clearUponHandler(2)
    Unknown1019(60)
    sprite('iz400_09ex00', 2)	# 171-172	 **attackbox here**
    Unknown1019(20)
    Unknown8000(100, 1, 1)
    sprite('iz400_10ex00', 3)	# 173-175	 **attackbox here**
    sprite('iz400_11', 3)	# 176-178
    sprite('iz400_12', 3)	# 179-181
    physicsXImpulse(0)
    Recovery()
    sprite('iz400_13', 2)	# 182-183
    sprite('iz400_14', 2)	# 184-185

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(70)
        AttackP2(80)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(14000)
        AirPushbackY(43000)
        AirUntechableTime(50)
        Hitstop(6)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown11042(1)
        Unknown3069(2)
        Unknown3071(5)
        Unknown3076(1010)
        Unknown3077(1010)

        def upon_STATE_END():
            Unknown7015()
            Unknown3001(255)
            Unknown3004(0)

        def upon_78():
            sendToLabel(1)
    sprite('iz402_00', 2)	# 1-2
    Unknown3029(1)
    sprite('iz402_01', 1)	# 3-3
    sprite('iz402_01', 1)	# 4-4
    sprite('iz402_02', 2)	# 5-6
    SFX_3('izse_03_start')
    GFX_0('Iaimcircle', -1)
    GFX_0('Iai_hold', 100)
    Unknown38(6, 1)
    GFX_0('Iai_hold_add', 100)
    Unknown38(7, 1)
    tag_voice(1, 'biz202_0', 'biz202_1', 'biz202_2', '')
    sprite('iz404_00', 1)	# 7-7
    sprite('iz404_01', 2)	# 8-9
    Unknown7015()
    SFX_3('izse_01')
    GFX_0('Iai_SlashZanzo_AntiAirA', -1)
    Unknown21015('4961696d636972636c6500000000000000000000000000000000000000000000e903000000000000')
    SFX_0('010_swing_sword_2')
    Unknown13(6)
    Unknown13(7)
    sprite('iz404_02', 3)	# 10-12	 **attackbox here**
    sprite('iz404_03', 5)	# 13-17
    Recovery()
    sprite('iz404_04', 9)	# 18-26
    sprite('iz404_05', 7)	# 27-33
    sprite('iz404_06', 5)	# 34-38
    Unknown3029(0)
    sprite('iz404_07', 4)	# 39-42
    sprite('iz404_08', 4)	# 43-46
    sprite('iz404_09', 4)	# 47-50
    ExitState()
    label(1)
    clearUponHandler(78)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(1000)
    AirPushbackY(-80000)
    Unknown9118(20)
    Unknown9190(1)
    Unknown9016(1)
    AirUntechableTime(100)
    Hitstop(2)
    Unknown2004(1, 0)
    clearUponHandler(2)
    sendToLabelUpon(2, 10)
    sprite('keep', 1)	# 51-51
    sprite('iz404_03', 2)	# 52-53
    GFX_0('Iai_AntiAir_Next_404F', -1)
    GFX_0('Iai_AntiAir_Next_404B', -1)
    Unknown3032()
    Unknown3004(-20)
    sprite('iz404_04', 2)	# 54-55
    SFX_3('izse_04')
    sprite('iz404_05', 2)	# 56-57
    sprite('iz406_00', 1)	# 58-58
    Unknown3004(30)
    EnableCollision(0)
    Unknown2006()
    Unknown1086(22)
    Unknown1007(300000)
    teleportRelativeX(100000)
    sprite('iz406_00', 2)	# 59-60
    GFX_0('Iai_AntiAir_Next_406F', -1)
    GFX_0('Iai_AntiAir_Next_406B', -1)
    Unknown3001(0)
    Unknown3004(30)
    sprite('iz406_01', 2)	# 61-62
    Unknown23119(2148384, 10, 2)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    setGravity(0)
    physicsYImpulse(2000)
    sprite('iz406_02', 2)	# 63-64
    sprite('iz406_03', 2)	# 65-66
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_04', 2)	# 67-68
    sprite('iz406_05', 2)	# 69-70	 **attackbox here**
    sprite('iz406_06', 3)	# 71-73	 **attackbox here**
    tag_voice(1, 'biz208_0', 'biz208_1', 'biz208_2', '')
    RefreshMultihit()
    Unknown2003(0)
    SFX_3('izse_01')
    Unknown11058('0100000000000000000000000000000000000000')
    physicsYImpulse(-80000)
    setGravity(7000)
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    label(0)
    sprite('iz406_06', 3)	# 74-76	 **attackbox here**
    sprite('iz406_07', 3)	# 77-79	 **attackbox here**
    sprite('iz406_08', 3)	# 80-82	 **attackbox here**
    gotoLabel(0)
    label(10)
    sprite('iz406_09', 5)	# 83-87	 **attackbox here**
    clearUponHandler(2)
    EnableCollision(1)
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    Unknown1084(1)
    Recovery()
    sprite('iz406_10', 9)	# 88-96	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_11', 8)	# 97-104
    sprite('iz406_12', 6)	# 105-110
    sprite('iz406_13', 6)	# 111-116

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2400)
        AttackP1(70)
        AttackP2(80)
        AirUntechableTime(50)
        AirPushbackX(27000)
        AirPushbackY(15000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Hitstop(6)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown1084(1)
        Unknown11056(0)
        Unknown11042(1)
        Unknown3069(2)
        Unknown3071(5)
        Unknown3076(1010)
        Unknown3077(1010)

        def upon_STATE_END():
            Unknown7015()
    sprite('iz403_00', 2)	# 1-2
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(2500)
    AirPushbackY(31000)
    AirUntechableTime(50)
    Unknown9016(1)
    Unknown2004(1, 0)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)

    def upon_STATE_END():
        Unknown3001(255)
        Unknown3004(0)
    sprite('iz403_00', 2)	# 3-4
    SFX_3('izse_04')
    Unknown23119(2148384, 4, 2)
    GFX_0('firespark', -1)
    physicsXImpulse(58000)
    sprite('iz403_00', 3)	# 5-7
    Unknown26('Iaimcircle')
    Unknown13(6)
    Unknown13(7)
    sprite('iz403_00', 3)	# 8-10
    GFX_0('firespark', -1)
    sprite('iz403_01', 2)	# 11-12
    GFX_0('firespark', -1)
    sprite('iz403_02', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    Unknown11001(0, 5, 5)
    SFX_3('izse_01')
    GFX_0('Ia_SlashNextZanzo', -1)
    GFX_0('IaiSlashNextAura', 0)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f736964650000000000000000000000000000')
    physicsXImpulse(8000)
    tag_voice(1, 'biz204_0', 'biz204_1', 'biz204_2', '')
    sprite('iz403_03', 5)	# 16-20	 **attackbox here**
    Recovery()
    Unknown1019(25)
    sprite('iz403_04', 5)	# 21-25	 **attackbox here**
    Unknown1019(25)
    sprite('iz403_05', 5)	# 26-30	 **attackbox here**
    Unknown1084(1)
    Unknown3029(0)
    sprite('iz403_06', 5)	# 31-35	 **attackbox here**
    sprite('iz403_07', 5)	# 36-40	 **attackbox here**
    sprite('iz403_08', 4)	# 41-44
    sprite('iz403_09', 4)	# 45-48
    sprite('iz403_10', 4)	# 49-52

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
    Unknown2036(119, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-405000)
    Unknown1019(4)
    label(0)
    sprite('iz020_07', 4)	# 3-6
    sprite('iz020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateAssaultDDDOD')
    else:
        enterState('UltimateAssaultDDD')

@State
def UltimateAssaultDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        AirUntechableTime(40)
        Unknown9202(20)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        AirPushbackX(50000)
        ProjectileDurabilityLvl(2)
        Unknown9016(1)
        setInvincible(1)
        Unknown11056(0)
        MinimumDamagePct(100)
        Unknown2004(1, 0)
    sprite('iz430_00', 3)	# 1-3
    sprite('iz430_01', 3)	# 4-6	 **attackbox here**
    sprite('iz430_02', 3)	# 7-9	 **attackbox here**
    sprite('iz430_03', 3)	# 10-12	 **attackbox here**
    sprite('iz430_04', 3)	# 13-15	 **attackbox here**
    sprite('iz430_02', 3)	# 16-18	 **attackbox here**
    sprite('iz430_03', 3)	# 19-21	 **attackbox here**
    SFX_3('izse_06')
    sprite('iz430_04', 3)	# 22-24	 **attackbox here**
    sprite('iz430_02', 3)	# 25-27	 **attackbox here**
    sprite('iz430_03', 3)	# 28-30	 **attackbox here**
    sprite('iz430_04', 3)	# 31-33	 **attackbox here**
    sprite('iz430_05', 3)	# 34-36	 **attackbox here**
    GFX_0('DD_3d_zanzoh', 0)
    GFX_0('DD_pt_edge', 0)
    GFX_0('DD_pt_circle', 0)
    sprite('iz430_06', 3)	# 37-39	 **attackbox here**
    sprite('iz430_07', 3)	# 40-42	 **attackbox here**
    GFX_0('DD_3Dcircle_out', -1)
    GFX_0('DD_3Dcircle_in', -1)
    sprite('iz430_08', 3)	# 43-45	 **attackbox here**
    sprite('iz430_09', 3)	# 46-48	 **attackbox here**
    sprite('iz430_10', 3)	# 49-51	 **attackbox here**
    sprite('iz430_11', 3)	# 52-54	 **attackbox here**
    sprite('iz430_12', 3)	# 55-57	 **attackbox here**
    sprite('iz430_13', 3)	# 58-60	 **attackbox here**
    sprite('iz430_14', 2)	# 61-62	 **attackbox here**
    sprite('iz430_15', 2)	# 63-64	 **attackbox here**
    sprite('iz430_16', 4)	# 65-68	 **attackbox here**
    sprite('iz430_17', 5)	# 69-73	 **attackbox here**
    sprite('iz430_18', 18)	# 74-91	 **attackbox here**
    sprite('iz430_18', 1)	# 92-92	 **attackbox here**
    sprite('iz430_19ex00', 2)	# 93-94	 **attackbox here**
    sprite('iz430_20ex00', 1)	# 95-95	 **attackbox here**
    ScreenShake(20000, 0)
    GFX_0('DD_sword', -1)
    GFX_0('DD_sword_env', -1)
    GFX_0('DD_3d_swordaura', -1)
    GFX_0('UltimateAssaultAura', 0)
    GFX_0('UltimateAssaultAura_back', 1)
    sprite('iz430_20ex00', 2)	# 96-97	 **attackbox here**
    sprite('iz430_21ex00', 3)	# 98-100	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 101-103	 **attackbox here**
    sprite('iz430_20ex00', 3)	# 104-106	 **attackbox here**
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('iz430_21ex00', 3)	# 107-109	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 110-112	 **attackbox here**
    sprite('iz430_20ex00', 3)	# 113-115	 **attackbox here**
    sprite('iz430_21ex00', 3)	# 116-118	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 119-121	 **attackbox here**
    sprite('iz430_23ex00', 3)	# 122-124	 **attackbox here**
    Unknown21015('44445f33645f73776f72646175726100000000000000000000000000000000008913000000000000')
    sprite('iz430_24ex00', 3)	# 125-127	 **attackbox here**
    sprite('iz430_25', 5)	# 128-132
    sprite('iz430_26', 5)	# 133-137
    sprite('iz430_27', 5)	# 138-142
    sprite('iz430_28', 5)	# 143-147
    sprite('iz430_29', 5)	# 148-152

@State
def UltimateAssaultDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2500)
        AttackP1(100)
        AttackP2(100)
        AirUntechableTime(40)
        Unknown9202(20)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        AirPushbackX(50000)
        Unknown9016(1)
        setInvincible(1)
        Unknown11056(0)
        MinimumDamagePct(100)
        Unknown2004(1, 0)
    sprite('iz430_00', 3)	# 1-3
    sprite('iz430_01', 3)	# 4-6	 **attackbox here**
    sprite('iz430_02', 3)	# 7-9	 **attackbox here**
    sprite('iz430_03', 3)	# 10-12	 **attackbox here**
    sprite('iz430_04', 3)	# 13-15	 **attackbox here**
    sprite('iz430_02', 3)	# 16-18	 **attackbox here**
    sprite('iz430_03', 3)	# 19-21	 **attackbox here**
    SFX_3('izse_06')
    sprite('iz430_04', 3)	# 22-24	 **attackbox here**
    sprite('iz430_02', 3)	# 25-27	 **attackbox here**
    sprite('iz430_03', 3)	# 28-30	 **attackbox here**
    sprite('iz430_04', 3)	# 31-33	 **attackbox here**
    sprite('iz430_05', 3)	# 34-36	 **attackbox here**
    GFX_0('DD_3d_zanzoh', 0)
    GFX_0('DD_pt_edge', 0)
    GFX_0('DD_pt_circle', 0)
    sprite('iz430_06', 3)	# 37-39	 **attackbox here**
    sprite('iz430_07', 3)	# 40-42	 **attackbox here**
    GFX_0('DD_3Dcircle_out', -1)
    GFX_0('DD_3Dcircle_in', -1)
    sprite('iz430_08', 3)	# 43-45	 **attackbox here**
    sprite('iz430_09', 3)	# 46-48	 **attackbox here**
    sprite('iz430_10', 3)	# 49-51	 **attackbox here**
    sprite('iz430_11', 3)	# 52-54	 **attackbox here**
    sprite('iz430_12', 3)	# 55-57	 **attackbox here**
    sprite('iz430_13', 3)	# 58-60	 **attackbox here**
    sprite('iz430_14', 2)	# 61-62	 **attackbox here**
    sprite('iz430_15', 2)	# 63-64	 **attackbox here**
    sprite('iz430_16', 4)	# 65-68	 **attackbox here**
    sprite('iz430_17', 5)	# 69-73	 **attackbox here**
    sprite('iz430_18', 18)	# 74-91	 **attackbox here**
    sprite('iz430_18', 1)	# 92-92	 **attackbox here**
    sprite('iz430_19ex00', 2)	# 93-94	 **attackbox here**
    sprite('iz430_20ex01', 1)	# 95-95	 **attackbox here**
    ScreenShake(20000, 0)
    GFX_0('DD_sword_OD', -1)
    GFX_0('DD_sword_env_OD', -1)
    GFX_0('DD_3d_swordaura', -1)
    GFX_0('UltimateAssaultAura', 0)
    GFX_0('UltimateAssaultAura_back', 1)
    sprite('iz430_20ex01', 2)	# 96-97	 **attackbox here**
    sprite('iz430_21ex01', 3)	# 98-100	 **attackbox here**
    sprite('iz430_22ex01', 3)	# 101-103	 **attackbox here**
    sprite('iz430_20ex01', 3)	# 104-106	 **attackbox here**
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('iz430_21ex01', 3)	# 107-109	 **attackbox here**
    sprite('iz430_22ex01', 3)	# 110-112	 **attackbox here**
    sprite('iz430_20ex00', 3)	# 113-115	 **attackbox here**
    sprite('iz430_21ex00', 3)	# 116-118	 **attackbox here**
    sprite('iz430_22ex00', 3)	# 119-121	 **attackbox here**
    sprite('iz430_23ex00', 3)	# 122-124	 **attackbox here**
    Unknown21015('44445f33645f73776f72646175726100000000000000000000000000000000008913000000000000')
    sprite('iz430_24ex00', 3)	# 125-127	 **attackbox here**
    sprite('iz430_25', 5)	# 128-132
    sprite('iz430_26', 5)	# 133-137
    sprite('iz430_27', 5)	# 138-142
    sprite('iz430_28', 5)	# 143-147
    sprite('iz430_29', 5)	# 148-152

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
    sprite('null', 5)	# 121-125
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(400000)
    Unknown2053(1)
    sprite('iz406_00', 3)	# 126-128
    GFX_0('Iai_AntiAir_Next_406F', -1)
    GFX_0('Iai_AntiAir_Next_406B', -1)
    Unknown3001(0)
    Unknown3004(30)
    SFX_0('airdash_l')
    SFX_0('slash_pole_middle')
    sprite('iz406_01', 4)	# 129-132
    Unknown23119(2148384, 10, 2)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('0000000000000000ff00000040000000')
    Unknown3075('0000000000000000c800000000000000')
    Unknown3076(1010)
    Unknown3077(1010)
    sprite('iz406_02', 4)	# 133-136
    sprite('iz406_03', 4)	# 137-140
    Unknown3001(255)
    Unknown3004(0)
    sprite('iz406_04', 4)	# 141-144
    sprite('iz406_05', 4)	# 145-148	 **attackbox here**
    sprite('iz406_06', 3)	# 149-151	 **attackbox here**
    SFX_3('izse_01')
    GFX_0('Iai_AntiAirNext_Zanzo', -1)
    Unknown4054(5)
    Unknown4045('697a65665f696169736c6173686e6578745f6c656e677468000000000000000002000000')
    GFX_0('IaiAntiAirNextAuraL', 0)
    GFX_0('IaiAntiAirNextAuraR', 1)
    physicsYImpulse(-200000)
    label(1)
    sprite('iz406_06', 3)	# 152-154	 **attackbox here**
    sprite('iz406_07', 3)	# 155-157	 **attackbox here**
    sprite('iz406_08', 3)	# 158-160	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('iz406_06', 1)	# 161-161	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown21015('4961695f416e74694169724e6578745f5a616e7a6f0000000000000000000000ea03000000000000')
    Unknown21015('496169416e74694169724e657874417572614c00000000000000000000000000eb03000000000000')
    Unknown21015('496169416e74694169724e657874417572615200000000000000000000000000ec03000000000000')
    Unknown1084(1)
    sprite('iz406_09', 2)	# 162-163	 **attackbox here**
    sprite('iz406_10', 17)	# 164-180	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    Unknown8000(-1, 1, 1)
    sprite('iz406_11', 4)	# 181-184
    sprite('iz406_12', 4)	# 185-188
    sprite('iz406_13', 4)	# 189-192

@Subroutine
def MouthTableInit():
    Unknown18011('biz000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24889, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz500', '001')
    Unknown18011('biz501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz501', '002')
    Unknown18011('biz502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz502', '003')
    Unknown18011('biz503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz503', '004')
    Unknown18011('biz504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz504', '005')
    Unknown18011('biz505', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 13665, 13667, 13665, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz505', '006')
    Unknown18011('biz520', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz520', '007')
    Unknown18011('biz521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz521', '008')
    Unknown18011('biz522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz522', '009')
    Unknown18011('biz523', 12643, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz523', '010')
    Unknown18011('biz524', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24885, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz524', '011')
    Unknown18011('biz525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz525', '012')
    Unknown18011('biz402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz403_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz403_1', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24884, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600bha', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600bma', 12643, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600bmk', 12643, 14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 13361, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600bno', 12643, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14435, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600rbl', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600uyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz601bjn', 12643, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz601pna', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz601uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600use', 13155, 14177, 14179, 14177, 14179, 14177, 13411, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz600kym', 12643, 12641, 25397, 24887, 12337, 14179, 14177, 14179, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz600bha', '017')
    Unknown30092('biz600bma', '018')
    Unknown30092('biz600bmk', '019')
    Unknown30092('biz600bno', '020')
    Unknown30092('biz600pbc', '021')
    Unknown30092('biz600rbl', '022')
    Unknown30092('biz600uyu', '023')
    Unknown30092('biz601bjn', '024')
    Unknown30092('biz601pna', '025')
    Unknown30092('biz601uor', '026')
    Unknown30092('biz600use', '027')
    Unknown30092('biz600kym', '028')
    Unknown18011('biz700bno', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24883, 25399, 24887, 25399, 14131, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz700pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz700rbl', 12643, 14177, 12643, 24880, 25399, 14132, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz700uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz700uyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz701bha', 12643, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 13620, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz701bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz701bma', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz701bmk', 12643, 12641, 25401, 24887, 25399, 24887, 25399, 24889, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz700use', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz700kym', 12643, 12641, 25397, 12593, 12641, 25397, 14130, 12641, 25393, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('biz700bno', '029')
    Unknown30092('biz700pbc', '030')
    Unknown30092('biz700rbl', '031')
    Unknown30092('biz700uor', '032')
    Unknown30092('biz700uyu', '033')
    Unknown30092('biz701bha', '034')
    Unknown30092('biz701bjn', '035')
    Unknown30092('biz701bma', '036')
    Unknown30092('biz701bmk', '037')
    Unknown30092('biz700use', '038')
    Unknown30092('biz700kym', '039')
    Unknown18011('biz291_0', 14433, 13667, 13921, 13923, 13921, 13923, 13665, 13667, 14177, 13923, 14177, 13923, 12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz292_0', 14433, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13921, 13667, 13921, 13411, 13409, 13411, 14177, 13667, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz293_0', 14177, 13923, 14177, 13923, 13665, 13411, 14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz294_0', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 12641, 25398, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz295_0', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 12641, 25398, 24884, 25396, 25396, 24884, 13873, 13411, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz291_1', 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz292_1', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25392, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz293_1', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz294_1', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 14433, 12643, 24882, 25396, 24884, 25396, 24884, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('biz295_1', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_172:
        Unknown18011('biz000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz500', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz501', 12643, 13923, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz502', 12643, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 25397, 24881, 25399, 24887, 25398, 24881, 25399, 24887, 25397, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 13409, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 13361, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz504', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 13923, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz505', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13155, 14177, 13667, 12643, 24881, 25399, 24887, 25399, 25396, 24882, 25399, 24887, 25395, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz520', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz521', 12643, 12899, 14177, 14179, 14177, 14179, 12641, 13667, 14177, 13923, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz522', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14177, 14179, 14177, 14179, 14177, 12899, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz523', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13411, 24882, 25399, 24881, 25399, 24887, 25399, 24887, 25394, 14642, 14177, 13411, 12643, 14177, 12643, 12899, 14177, 14179, 13665, 13155, 14177, 14179, 13921, 12643, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz524', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 13665, 13155, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24881, 25399, 25396, 24883, 25399, 24887, 25394, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24882, 25399, 24887, 25399, 25394, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz525', 12643, 12643, 14177, 13155, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz403_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz403_1', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24884, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600bha', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 24882, 25399, 24887, 25399, 25393, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600bma', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600bmk', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 13667, 14177, 14179, 12899, 12641, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 13921, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13155, 13665, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600bno', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 14177, 13923, 14691, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600pbc', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600rbl', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 12641, 12643, 14177, 14179, 13665, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600uyu', 12643, 12899, 14177, 14179, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz601bjn', 12643, 12643, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 13667, 14177, 13923, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz601pna', 12643, 12643, 14177, 13923, 13155, 14177, 13155, 13155, 14177, 14179, 14177, 13411, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 13153, 12899, 24885, 25399, 25399, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24882, 25399, 24887, 25396, 24881, 25399, 24887, 25396, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz601uor', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600use', 12643, 12643, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 13409, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz600kym', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14177, 13155, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz700bno', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 14129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz700pbc', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 13921, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz700rbl', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 12643, 12643, 14177, 12899, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz700uor', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz700uyu', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz701bha', 12643, 13155, 13921, 12643, 14177, 14179, 14177, 12899, 14177, 13155, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz701bjn', 12643, 13155, 14177, 14179, 13921, 13155, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 14179, 14177, 12643, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz701bma', 12643, 12899, 14177, 14179, 13155, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 13665, 12643, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 13155, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz701bmk', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz700use', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13667, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 14177, 12899, 14177, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz700kym', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13155, 14177, 14179, 14177, 14179, 13153, 12899, 13921, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz291_0', 14433, 13667, 13921, 13923, 13921, 13923, 13665, 13667, 14177, 13923, 14177, 13923, 12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz292_0', 14433, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13921, 13667, 13921, 13411, 13409, 13411, 14177, 13667, 14433, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz293_0', 14177, 13923, 14177, 13923, 13665, 13411, 14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz294_0', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 12641, 25398, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz295_0', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 12641, 25398, 24884, 25396, 25396, 24884, 13873, 13411, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz291_1', 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz292_1', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25392, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz293_1', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz294_1', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 14433, 12643, 24882, 25396, 24884, 25396, 24884, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('biz295_1', 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bha')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bma')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('bmk')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bno')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('pbc')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('rbl')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('uyu')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('bjn')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('pna')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uor')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('use')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('kym')
    if SLOT_ReturnVal:
        _gotolabel(210)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('iz600_00', 1)	# 2-2
    Unknown7006('biz500', 100, 897214818, 12592, 0, 0, 100, 897214818, 13360, 0, 0, 100, 0, 0, 0, 0, 0)
    label(1)
    sprite('iz600_00', 1)	# 3-3
    if SLOT_97:
        _gotolabel(1)
    sprite('iz600_01', 5)	# 4-8
    sprite('iz600_02', 5)	# 9-13	 **attackbox here**
    sprite('iz600_03', 6)	# 14-19	 **attackbox here**
    GFX_1('izef_entryhane', -1)
    GFX_1('izef_entrymcB', -1)
    SFX_0('019_cloth_c')
    sprite('iz600_04', 6)	# 20-25	 **attackbox here**
    sprite('iz600_05', 6)	# 26-31	 **attackbox here**
    sprite('iz600_06', 6)	# 32-37	 **attackbox here**
    Unknown23118(0)
    Unknown23117(16777215, 18)
    sprite('iz600_07', 6)	# 38-43	 **attackbox here**
    sprite('iz600_07ex00', 6)	# 44-49	 **attackbox here**
    sprite('iz600_08', 6)	# 50-55
    sprite('iz600_09', 6)	# 56-61
    Unknown23117(0, 6)
    SFX_0('022_magiccircle_b')
    sprite('iz600_10', 7)	# 62-68
    Unknown23120()
    sprite('iz600_11', 7)	# 69-75
    sprite('iz600_12', 7)	# 76-82
    sprite('iz600_13', 6)	# 83-88
    sprite('iz600_14', 6)	# 89-94
    sprite('iz600_15', 5)	# 95-99
    Unknown23018(1)
    label(2)
    sprite('iz000_00', 7)	# 100-106	 **attackbox here**
    sprite('iz000_01', 7)	# 107-113	 **attackbox here**
    sprite('iz000_02', 7)	# 114-120	 **attackbox here**
    sprite('iz000_03', 7)	# 121-127	 **attackbox here**
    sprite('iz000_04', 7)	# 128-134	 **attackbox here**
    sprite('iz000_05', 7)	# 135-141	 **attackbox here**
    sprite('iz000_06', 7)	# 142-148	 **attackbox here**
    sprite('iz000_07', 7)	# 149-155	 **attackbox here**
    sprite('iz000_08', 7)	# 156-162	 **attackbox here**
    sprite('iz000_09', 7)	# 163-169	 **attackbox here**
    loopRest()
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('iz601_00', 1)	# 170-170
    Unknown7006('biz502', 100, 897214818, 13104, 0, 0, 100, 897214818, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    label(11)
    sprite('iz601_00', 1)	# 171-171
    if SLOT_97:
        _gotolabel(11)
    sprite('iz601_00', 6)	# 172-177
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('iz601_01', 7)	# 178-184
    sprite('iz601_02', 7)	# 185-191
    sprite('iz601_03', 7)	# 192-198
    sprite('iz601_04', 5)	# 199-203
    sprite('iz601_05', 5)	# 204-208
    sprite('iz601_06', 6)	# 209-214
    sprite('iz601_07', 6)	# 215-220
    sprite('iz601_07', 6)	# 221-226
    sprite('iz601_07', 6)	# 227-232
    GFX_1('izef_entrylightB', 0)
    sprite('iz601_08', 7)	# 233-239
    sprite('iz601_09', 7)	# 240-246
    GFX_0('iz601amourlight', -1)
    SFX_0('022_magiccircle_a')
    sprite('iz601_10', 7)	# 247-253
    sprite('iz601_11', 7)	# 254-260
    sprite('iz601_12', 7)	# 261-267
    sprite('iz601_13', 7)	# 268-274
    sprite('iz601_14', 7)	# 275-281
    sprite('iz601_15', 7)	# 282-288
    sprite('iz601_16', 7)	# 289-295
    sprite('iz601_17', 7)	# 296-302
    GFX_1('izef_armchange', 0)
    sprite('iz601_18', 7)	# 303-309
    GFX_0('iz601swdlight', -1)
    sprite('iz601_19', 7)	# 310-316
    sprite('iz601_20', 7)	# 317-323
    sprite('iz601_20', 1)	# 324-324
    Unknown23018(1)
    label(12)
    sprite('iz000_00', 7)	# 325-331	 **attackbox here**
    sprite('iz000_01', 7)	# 332-338	 **attackbox here**
    sprite('iz000_02', 7)	# 339-345	 **attackbox here**
    sprite('iz000_03', 7)	# 346-352	 **attackbox here**
    sprite('iz000_04', 7)	# 353-359	 **attackbox here**
    sprite('iz000_05', 7)	# 360-366	 **attackbox here**
    sprite('iz000_06', 7)	# 367-373	 **attackbox here**
    sprite('iz000_07', 7)	# 374-380	 **attackbox here**
    sprite('iz000_08', 7)	# 381-387	 **attackbox here**
    sprite('iz000_09', 7)	# 388-394	 **attackbox here**
    loopRest()
    gotoLabel(12)
    ExitState()
    label(20)
    sprite('iz634_00', 6)	# 395-400
    sprite('iz634_01', 6)	# 401-406
    sprite('iz634_02', 6)	# 407-412
    sprite('iz634_03', 6)	# 413-418
    sprite('iz634_04', 6)	# 419-424
    SFX_1('biz601uor')
    sprite('iz634_05', 6)	# 425-430
    sprite('iz634_06', 32767)	# 431-33197
    ExitState()
    label(991)
    sprite('iz000_00', 1)	# 33198-33198	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('iz000_00', 7)	# 33199-33205	 **attackbox here**
    sprite('iz000_01', 7)	# 33206-33212	 **attackbox here**
    sprite('iz000_02', 7)	# 33213-33219	 **attackbox here**
    sprite('iz000_03', 7)	# 33220-33226	 **attackbox here**
    sprite('iz000_04', 7)	# 33227-33233	 **attackbox here**
    sprite('iz000_05', 7)	# 33234-33240	 **attackbox here**
    sprite('iz000_06', 7)	# 33241-33247	 **attackbox here**
    sprite('iz000_07', 7)	# 33248-33254	 **attackbox here**
    sprite('iz000_08', 7)	# 33255-33261	 **attackbox here**
    sprite('iz000_09', 7)	# 33262-33268	 **attackbox here**
    gotoLabel(992)
    label(100)
    sprite('iz600_00', 1)	# 33269-33269
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1505000)
    SFX_1('biz600bha')
    label(101)
    sprite('iz600_00', 1)	# 33270-33270
    if SLOT_97:
        _gotolabel(101)
    sprite('iz600_01', 5)	# 33271-33275
    sprite('iz600_02', 5)	# 33276-33280	 **attackbox here**
    sprite('iz600_03', 6)	# 33281-33286	 **attackbox here**
    GFX_1('izef_entryhane', -1)
    GFX_1('izef_entrymcB', -1)
    SFX_0('019_cloth_c')
    sprite('iz600_04', 6)	# 33287-33292	 **attackbox here**
    sprite('iz600_05', 6)	# 33293-33298	 **attackbox here**
    sprite('iz600_06', 6)	# 33299-33304	 **attackbox here**
    Unknown23118(0)
    Unknown23117(16777215, 18)
    sprite('iz600_07', 6)	# 33305-33310	 **attackbox here**
    sprite('iz600_07ex00', 6)	# 33311-33316	 **attackbox here**
    sprite('iz600_08', 6)	# 33317-33322
    sprite('iz600_09', 6)	# 33323-33328
    Unknown23117(0, 6)
    SFX_0('022_magiccircle_b')
    sprite('iz600_10', 7)	# 33329-33335
    Unknown23120()
    sprite('iz600_11', 7)	# 33336-33342
    sprite('iz600_12', 7)	# 33343-33349
    sprite('iz600_13', 6)	# 33350-33355
    sprite('iz600_14', 6)	# 33356-33361
    sprite('iz600_15', 5)	# 33362-33366
    Unknown21007(24, 40)
    Unknown21011(420)
    label(102)
    sprite('iz000_00', 7)	# 33367-33373	 **attackbox here**
    sprite('iz000_01', 7)	# 33374-33380	 **attackbox here**
    sprite('iz000_02', 7)	# 33381-33387	 **attackbox here**
    sprite('iz000_03', 7)	# 33388-33394	 **attackbox here**
    sprite('iz000_04', 7)	# 33395-33401	 **attackbox here**
    sprite('iz000_05', 7)	# 33402-33408	 **attackbox here**
    sprite('iz000_06', 7)	# 33409-33415	 **attackbox here**
    sprite('iz000_07', 7)	# 33416-33422	 **attackbox here**
    sprite('iz000_08', 7)	# 33423-33429	 **attackbox here**
    sprite('iz000_09', 7)	# 33430-33436	 **attackbox here**
    loopRest()
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('iz601_00', 1)	# 33437-33437
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('biz600bma')
    label(111)
    sprite('iz601_00', 1)	# 33438-33438
    if SLOT_97:
        _gotolabel(111)
    sprite('iz601_00', 6)	# 33439-33444
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('iz601_01', 7)	# 33445-33451
    sprite('iz601_02', 7)	# 33452-33458
    sprite('iz601_03', 7)	# 33459-33465
    sprite('iz601_04', 5)	# 33466-33470
    sprite('iz601_05', 5)	# 33471-33475
    sprite('iz601_06', 6)	# 33476-33481
    sprite('iz601_07', 6)	# 33482-33487
    sprite('iz601_07', 6)	# 33488-33493
    sprite('iz601_07', 6)	# 33494-33499
    GFX_1('izef_entrylightB', 0)
    sprite('iz601_08', 7)	# 33500-33506
    sprite('iz601_09', 7)	# 33507-33513
    GFX_0('iz601amourlight', -1)
    SFX_0('022_magiccircle_a')
    sprite('iz601_10', 7)	# 33514-33520
    sprite('iz601_11', 7)	# 33521-33527
    sprite('iz601_12', 7)	# 33528-33534
    sprite('iz601_13', 7)	# 33535-33541
    sprite('iz601_14', 7)	# 33542-33548
    sprite('iz601_15', 7)	# 33549-33555
    sprite('iz601_16', 7)	# 33556-33562
    sprite('iz601_17', 7)	# 33563-33569
    GFX_1('izef_armchange', 0)
    sprite('iz601_18', 7)	# 33570-33576
    GFX_0('iz601swdlight', -1)
    sprite('iz601_19', 7)	# 33577-33583
    sprite('iz601_20', 7)	# 33584-33590
    sprite('iz601_20', 1)	# 33591-33591
    Unknown21007(24, 40)
    Unknown21011(200)
    label(112)
    sprite('iz000_00', 7)	# 33592-33598	 **attackbox here**
    sprite('iz000_01', 7)	# 33599-33605	 **attackbox here**
    sprite('iz000_02', 7)	# 33606-33612	 **attackbox here**
    sprite('iz000_03', 7)	# 33613-33619	 **attackbox here**
    sprite('iz000_04', 7)	# 33620-33626	 **attackbox here**
    sprite('iz000_05', 7)	# 33627-33633	 **attackbox here**
    sprite('iz000_06', 7)	# 33634-33640	 **attackbox here**
    sprite('iz000_07', 7)	# 33641-33647	 **attackbox here**
    sprite('iz000_08', 7)	# 33648-33654	 **attackbox here**
    sprite('iz000_09', 7)	# 33655-33661	 **attackbox here**
    loopRest()
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('iz601_00', 1)	# 33662-33662
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('biz600bmk')
    label(121)
    sprite('iz601_00', 1)	# 33663-33663
    if SLOT_97:
        _gotolabel(121)
    sprite('iz601_00', 6)	# 33664-33669
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('iz601_01', 7)	# 33670-33676
    sprite('iz601_02', 7)	# 33677-33683
    sprite('iz601_03', 7)	# 33684-33690
    sprite('iz601_04', 5)	# 33691-33695
    sprite('iz601_05', 5)	# 33696-33700
    sprite('iz601_06', 6)	# 33701-33706
    sprite('iz601_07', 6)	# 33707-33712
    sprite('iz601_07', 6)	# 33713-33718
    sprite('iz601_07', 6)	# 33719-33724
    GFX_1('izef_entrylightB', 0)
    sprite('iz601_08', 7)	# 33725-33731
    sprite('iz601_09', 7)	# 33732-33738
    GFX_0('iz601amourlight', -1)
    SFX_0('022_magiccircle_a')
    sprite('iz601_10', 7)	# 33739-33745
    sprite('iz601_11', 7)	# 33746-33752
    sprite('iz601_12', 7)	# 33753-33759
    sprite('iz601_13', 7)	# 33760-33766
    sprite('iz601_14', 7)	# 33767-33773
    sprite('iz601_15', 7)	# 33774-33780
    sprite('iz601_16', 7)	# 33781-33787
    sprite('iz601_17', 7)	# 33788-33794
    GFX_1('izef_armchange', 0)
    sprite('iz601_18', 7)	# 33795-33801
    GFX_0('iz601swdlight', -1)
    sprite('iz601_19', 7)	# 33802-33808
    sprite('iz601_20', 7)	# 33809-33815
    sprite('iz601_20', 1)	# 33816-33816
    Unknown21007(24, 40)
    Unknown21011(240)
    label(122)
    sprite('iz000_00', 7)	# 33817-33823	 **attackbox here**
    sprite('iz000_01', 7)	# 33824-33830	 **attackbox here**
    sprite('iz000_02', 7)	# 33831-33837	 **attackbox here**
    sprite('iz000_03', 7)	# 33838-33844	 **attackbox here**
    sprite('iz000_04', 7)	# 33845-33851	 **attackbox here**
    sprite('iz000_05', 7)	# 33852-33858	 **attackbox here**
    sprite('iz000_06', 7)	# 33859-33865	 **attackbox here**
    sprite('iz000_07', 7)	# 33866-33872	 **attackbox here**
    sprite('iz000_08', 7)	# 33873-33879	 **attackbox here**
    sprite('iz000_09', 7)	# 33880-33886	 **attackbox here**
    loopRest()
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('iz601_00', 1)	# 33887-33887
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('biz600bno')
    label(131)
    sprite('iz601_00', 1)	# 33888-33888
    if SLOT_97:
        _gotolabel(131)
    sprite('iz601_00', 6)	# 33889-33894
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('iz601_01', 7)	# 33895-33901
    sprite('iz601_02', 7)	# 33902-33908
    sprite('iz601_03', 7)	# 33909-33915
    sprite('iz601_04', 5)	# 33916-33920
    sprite('iz601_05', 5)	# 33921-33925
    sprite('iz601_06', 6)	# 33926-33931
    sprite('iz601_07', 6)	# 33932-33937
    sprite('iz601_07', 6)	# 33938-33943
    sprite('iz601_07', 6)	# 33944-33949
    GFX_1('izef_entrylightB', 0)
    sprite('iz601_08', 7)	# 33950-33956
    sprite('iz601_09', 7)	# 33957-33963
    GFX_0('iz601amourlight', -1)
    SFX_0('022_magiccircle_a')
    sprite('iz601_10', 7)	# 33964-33970
    sprite('iz601_11', 7)	# 33971-33977
    sprite('iz601_12', 7)	# 33978-33984
    sprite('iz601_13', 7)	# 33985-33991
    sprite('iz601_14', 7)	# 33992-33998
    sprite('iz601_15', 7)	# 33999-34005
    sprite('iz601_16', 7)	# 34006-34012
    sprite('iz601_17', 7)	# 34013-34019
    GFX_1('izef_armchange', 0)
    sprite('iz601_18', 7)	# 34020-34026
    GFX_0('iz601swdlight', -1)
    sprite('iz601_19', 7)	# 34027-34033
    sprite('iz601_20', 7)	# 34034-34040
    sprite('iz601_20', 1)	# 34041-34041
    Unknown21007(24, 40)
    Unknown21011(300)
    label(132)
    sprite('iz000_00', 7)	# 34042-34048	 **attackbox here**
    sprite('iz000_01', 7)	# 34049-34055	 **attackbox here**
    sprite('iz000_02', 7)	# 34056-34062	 **attackbox here**
    sprite('iz000_03', 7)	# 34063-34069	 **attackbox here**
    sprite('iz000_04', 7)	# 34070-34076	 **attackbox here**
    sprite('iz000_05', 7)	# 34077-34083	 **attackbox here**
    sprite('iz000_06', 7)	# 34084-34090	 **attackbox here**
    sprite('iz000_07', 7)	# 34091-34097	 **attackbox here**
    sprite('iz000_08', 7)	# 34098-34104	 **attackbox here**
    sprite('iz000_09', 7)	# 34105-34111	 **attackbox here**
    loopRest()
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('iz600_00', 1)	# 34112-34112
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('biz600pbc')
    label(141)
    sprite('iz600_00', 1)	# 34113-34113
    if SLOT_97:
        _gotolabel(141)
    sprite('iz600_01', 5)	# 34114-34118
    sprite('iz600_02', 5)	# 34119-34123	 **attackbox here**
    sprite('iz600_03', 6)	# 34124-34129	 **attackbox here**
    GFX_1('izef_entryhane', -1)
    GFX_1('izef_entrymcB', -1)
    SFX_0('019_cloth_c')
    sprite('iz600_04', 6)	# 34130-34135	 **attackbox here**
    sprite('iz600_05', 6)	# 34136-34141	 **attackbox here**
    sprite('iz600_06', 6)	# 34142-34147	 **attackbox here**
    Unknown23118(0)
    Unknown23117(16777215, 18)
    sprite('iz600_07', 6)	# 34148-34153	 **attackbox here**
    sprite('iz600_07ex00', 6)	# 34154-34159	 **attackbox here**
    sprite('iz600_08', 6)	# 34160-34165
    sprite('iz600_09', 6)	# 34166-34171
    Unknown23117(0, 6)
    SFX_0('022_magiccircle_b')
    sprite('iz600_10', 7)	# 34172-34178
    Unknown23120()
    sprite('iz600_11', 7)	# 34179-34185
    sprite('iz600_12', 7)	# 34186-34192
    sprite('iz600_13', 6)	# 34193-34198
    sprite('iz600_14', 6)	# 34199-34204
    sprite('iz600_15', 5)	# 34205-34209
    Unknown21007(24, 40)
    Unknown21011(240)
    label(142)
    sprite('iz000_00', 7)	# 34210-34216	 **attackbox here**
    sprite('iz000_01', 7)	# 34217-34223	 **attackbox here**
    sprite('iz000_02', 7)	# 34224-34230	 **attackbox here**
    sprite('iz000_03', 7)	# 34231-34237	 **attackbox here**
    sprite('iz000_04', 7)	# 34238-34244	 **attackbox here**
    sprite('iz000_05', 7)	# 34245-34251	 **attackbox here**
    sprite('iz000_06', 7)	# 34252-34258	 **attackbox here**
    sprite('iz000_07', 7)	# 34259-34265	 **attackbox here**
    sprite('iz000_08', 7)	# 34266-34272	 **attackbox here**
    sprite('iz000_09', 7)	# 34273-34279	 **attackbox here**
    loopRest()
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('iz601_00', 1)	# 34280-34280
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('biz600rbl')
    label(151)
    sprite('iz601_00', 1)	# 34281-34281
    if SLOT_97:
        _gotolabel(151)
    sprite('iz601_00', 6)	# 34282-34287
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('iz601_01', 7)	# 34288-34294
    sprite('iz601_02', 7)	# 34295-34301
    sprite('iz601_03', 7)	# 34302-34308
    sprite('iz601_04', 5)	# 34309-34313
    sprite('iz601_05', 5)	# 34314-34318
    sprite('iz601_06', 6)	# 34319-34324
    sprite('iz601_07', 6)	# 34325-34330
    sprite('iz601_07', 6)	# 34331-34336
    sprite('iz601_07', 6)	# 34337-34342
    GFX_1('izef_entrylightB', 0)
    sprite('iz601_08', 7)	# 34343-34349
    sprite('iz601_09', 7)	# 34350-34356
    GFX_0('iz601amourlight', -1)
    SFX_0('022_magiccircle_a')
    sprite('iz601_10', 7)	# 34357-34363
    sprite('iz601_11', 7)	# 34364-34370
    sprite('iz601_12', 7)	# 34371-34377
    sprite('iz601_13', 7)	# 34378-34384
    sprite('iz601_14', 7)	# 34385-34391
    sprite('iz601_15', 7)	# 34392-34398
    sprite('iz601_16', 7)	# 34399-34405
    sprite('iz601_17', 7)	# 34406-34412
    GFX_1('izef_armchange', 0)
    sprite('iz601_18', 7)	# 34413-34419
    GFX_0('iz601swdlight', -1)
    sprite('iz601_19', 7)	# 34420-34426
    sprite('iz601_20', 7)	# 34427-34433
    sprite('iz601_20', 1)	# 34434-34434
    Unknown21007(24, 40)
    Unknown21011(240)
    label(152)
    sprite('iz000_00', 7)	# 34435-34441	 **attackbox here**
    sprite('iz000_01', 7)	# 34442-34448	 **attackbox here**
    sprite('iz000_02', 7)	# 34449-34455	 **attackbox here**
    sprite('iz000_03', 7)	# 34456-34462	 **attackbox here**
    sprite('iz000_04', 7)	# 34463-34469	 **attackbox here**
    sprite('iz000_05', 7)	# 34470-34476	 **attackbox here**
    sprite('iz000_06', 7)	# 34477-34483	 **attackbox here**
    sprite('iz000_07', 7)	# 34484-34490	 **attackbox here**
    sprite('iz000_08', 7)	# 34491-34497	 **attackbox here**
    sprite('iz000_09', 7)	# 34498-34504	 **attackbox here**
    loopRest()
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('iz600_00', 1)	# 34505-34505
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('biz600uyu')
    label(161)
    sprite('iz600_00', 1)	# 34506-34506
    if SLOT_97:
        _gotolabel(161)
    sprite('iz600_01', 5)	# 34507-34511
    sprite('iz600_02', 5)	# 34512-34516	 **attackbox here**
    sprite('iz600_03', 6)	# 34517-34522	 **attackbox here**
    GFX_1('izef_entryhane', -1)
    GFX_1('izef_entrymcB', -1)
    SFX_0('019_cloth_c')
    sprite('iz600_04', 6)	# 34523-34528	 **attackbox here**
    sprite('iz600_05', 6)	# 34529-34534	 **attackbox here**
    sprite('iz600_06', 6)	# 34535-34540	 **attackbox here**
    Unknown23118(0)
    Unknown23117(16777215, 18)
    sprite('iz600_07', 6)	# 34541-34546	 **attackbox here**
    sprite('iz600_07ex00', 6)	# 34547-34552	 **attackbox here**
    sprite('iz600_08', 6)	# 34553-34558
    sprite('iz600_09', 6)	# 34559-34564
    Unknown23117(0, 6)
    SFX_0('022_magiccircle_b')
    sprite('iz600_10', 7)	# 34565-34571
    Unknown23120()
    sprite('iz600_11', 7)	# 34572-34578
    sprite('iz600_12', 7)	# 34579-34585
    sprite('iz600_13', 6)	# 34586-34591
    sprite('iz600_14', 6)	# 34592-34597
    sprite('iz600_15', 5)	# 34598-34602
    Unknown21007(24, 40)
    Unknown21011(300)
    label(162)
    sprite('iz000_00', 7)	# 34603-34609	 **attackbox here**
    sprite('iz000_01', 7)	# 34610-34616	 **attackbox here**
    sprite('iz000_02', 7)	# 34617-34623	 **attackbox here**
    sprite('iz000_03', 7)	# 34624-34630	 **attackbox here**
    sprite('iz000_04', 7)	# 34631-34637	 **attackbox here**
    sprite('iz000_05', 7)	# 34638-34644	 **attackbox here**
    sprite('iz000_06', 7)	# 34645-34651	 **attackbox here**
    sprite('iz000_07', 7)	# 34652-34658	 **attackbox here**
    sprite('iz000_08', 7)	# 34659-34665	 **attackbox here**
    sprite('iz000_09', 7)	# 34666-34672	 **attackbox here**
    loopRest()
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('iz631_00', 32767)	# 34673-67439
    Unknown2019(-100)
    Unknown1000(-1350000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(171)
    label(171)
    sprite('iz631_01', 6)	# 67440-67445
    sprite('iz631_02', 90)	# 67446-67535
    SFX_1('biz601bjn')
    sprite('iz631_03', 4)	# 67536-67539
    sprite('iz631_04', 4)	# 67540-67543
    sprite('iz631_05', 4)	# 67544-67547
    sprite('iz631_06', 4)	# 67548-67551
    SFX_3('izse_01')
    Unknown23018(1)
    sprite('iz631_07', 32767)	# 67552-100318
    ExitState()
    label(180)
    sprite('iz000_00', 1)	# 100319-100319	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('iz000_00', 7)	# 100320-100326	 **attackbox here**
    sprite('iz000_01', 7)	# 100327-100333	 **attackbox here**
    sprite('iz000_02', 7)	# 100334-100340	 **attackbox here**
    sprite('iz000_03', 7)	# 100341-100347	 **attackbox here**
    sprite('iz000_04', 7)	# 100348-100354	 **attackbox here**
    sprite('iz000_05', 7)	# 100355-100361	 **attackbox here**
    sprite('iz000_06', 7)	# 100362-100368	 **attackbox here**
    sprite('iz000_07', 7)	# 100369-100375	 **attackbox here**
    sprite('iz000_08', 7)	# 100376-100382	 **attackbox here**
    sprite('iz000_09', 7)	# 100383-100389	 **attackbox here**
    gotoLabel(181)
    label(182)
    sprite('iz001_00', 7)	# 100390-100396
    sprite('iz001_01', 7)	# 100397-100403
    sprite('iz001_02', 7)	# 100404-100410
    sprite('iz001_03', 7)	# 100411-100417
    sprite('iz001_04', 7)	# 100418-100424
    SFX_1('biz601pna')
    sprite('iz001_05', 7)	# 100425-100431
    sprite('iz001_06', 7)	# 100432-100438
    sprite('iz001_07', 7)	# 100439-100445
    sprite('iz001_08', 7)	# 100446-100452
    label(183)
    sprite('iz001_04', 7)	# 100453-100459
    sprite('iz001_05', 7)	# 100460-100466
    sprite('iz001_06', 7)	# 100467-100473
    sprite('iz001_07', 7)	# 100474-100480
    sprite('iz001_08', 7)	# 100481-100487
    if SLOT_97:
        _gotolabel(183)
    sprite('iz001_04', 7)	# 100488-100494
    sprite('iz001_05', 7)	# 100495-100501
    sprite('iz001_09', 7)	# 100502-100508
    sprite('iz001_10', 7)	# 100509-100515
    Unknown23018(1)
    label(184)
    sprite('iz000_00', 7)	# 100516-100522	 **attackbox here**
    sprite('iz000_01', 7)	# 100523-100529	 **attackbox here**
    sprite('iz000_02', 7)	# 100530-100536	 **attackbox here**
    sprite('iz000_03', 7)	# 100537-100543	 **attackbox here**
    sprite('iz000_04', 7)	# 100544-100550	 **attackbox here**
    sprite('iz000_05', 7)	# 100551-100557	 **attackbox here**
    sprite('iz000_06', 7)	# 100558-100564	 **attackbox here**
    sprite('iz000_07', 7)	# 100565-100571	 **attackbox here**
    sprite('iz000_08', 7)	# 100572-100578	 **attackbox here**
    sprite('iz000_09', 7)	# 100579-100585	 **attackbox here**
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('iz634_00', 32767)	# 100586-133352
    Unknown1000(-1420000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(191)
    label(191)
    sprite('iz634_01', 6)	# 133353-133358
    Unknown21007(24, 40)
    sprite('iz634_02', 6)	# 133359-133364
    sprite('iz634_03', 6)	# 133365-133370
    sprite('iz634_04', 6)	# 133371-133376
    SFX_1('biz601uor')
    sprite('iz634_05', 6)	# 133377-133382
    Unknown23018(1)
    sprite('iz634_06', 32767)	# 133383-166149
    ExitState()
    label(200)
    sprite('iz602_00', 20)	# 166150-166169
    sprite('iz602_00', 1)	# 166170-166170
    SFX_1('biz600use')
    label(201)
    sprite('iz602_00', 1)	# 166171-166171
    if SLOT_97:
        _gotolabel(201)
    sprite('iz602_00', 30)	# 166172-166201
    sprite('iz602_01', 10)	# 166202-166211
    sprite('iz602_02', 7)	# 166212-166218
    sprite('iz602_03', 7)	# 166219-166225
    sprite('iz602_04', 7)	# 166226-166232
    sprite('iz602_05', 7)	# 166233-166239
    sprite('iz602_06', 7)	# 166240-166246
    sprite('iz602_07', 7)	# 166247-166253
    sprite('iz602_08', 7)	# 166254-166260
    Unknown21007(24, 40)
    Unknown21011(120)
    label(202)
    sprite('iz000_00', 7)	# 166261-166267	 **attackbox here**
    sprite('iz000_01', 7)	# 166268-166274	 **attackbox here**
    sprite('iz000_02', 7)	# 166275-166281	 **attackbox here**
    sprite('iz000_03', 7)	# 166282-166288	 **attackbox here**
    sprite('iz000_04', 7)	# 166289-166295	 **attackbox here**
    sprite('iz000_05', 7)	# 166296-166302	 **attackbox here**
    sprite('iz000_06', 7)	# 166303-166309	 **attackbox here**
    sprite('iz000_07', 7)	# 166310-166316	 **attackbox here**
    sprite('iz000_08', 7)	# 166317-166323	 **attackbox here**
    sprite('iz000_09', 7)	# 166324-166330	 **attackbox here**
    gotoLabel(202)
    label(210)
    sprite('iz600_00', 20)	# 166331-166350
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    sprite('iz600_00', 1)	# 166351-166351
    SFX_1('biz600kym')
    label(211)
    sprite('iz600_00', 1)	# 166352-166352
    if SLOT_97:
        _gotolabel(211)
    sprite('iz600_00', 20)	# 166353-166372
    sprite('iz600_00', 32767)	# 166373-199139
    Unknown21007(24, 40)
    label(212)
    sprite('iz600_01', 5)	# 199140-199144
    sprite('iz600_02', 5)	# 199145-199149	 **attackbox here**
    sprite('iz600_03', 6)	# 199150-199155	 **attackbox here**
    GFX_1('izef_entryhane', -1)
    GFX_1('izef_entrymcB', -1)
    SFX_0('019_cloth_c')
    sprite('iz600_04', 6)	# 199156-199161	 **attackbox here**
    sprite('iz600_05', 6)	# 199162-199167	 **attackbox here**
    sprite('iz600_06', 6)	# 199168-199173	 **attackbox here**
    Unknown23118(0)
    Unknown23117(16777215, 18)
    sprite('iz600_07', 6)	# 199174-199179	 **attackbox here**
    sprite('iz600_07ex00', 6)	# 199180-199185	 **attackbox here**
    sprite('iz600_08', 6)	# 199186-199191
    sprite('iz600_09', 6)	# 199192-199197
    Unknown23117(0, 6)
    SFX_0('022_magiccircle_b')
    sprite('iz600_10', 7)	# 199198-199204
    Unknown23120()
    sprite('iz600_11', 7)	# 199205-199211
    sprite('iz600_12', 7)	# 199212-199218
    sprite('iz600_13', 6)	# 199219-199224
    sprite('iz600_14', 6)	# 199225-199230
    sprite('iz600_15', 5)	# 199231-199235
    Unknown21011(60)
    label(213)
    sprite('iz000_00', 7)	# 199236-199242	 **attackbox here**
    sprite('iz000_01', 7)	# 199243-199249	 **attackbox here**
    sprite('iz000_02', 7)	# 199250-199256	 **attackbox here**
    sprite('iz000_03', 7)	# 199257-199263	 **attackbox here**
    sprite('iz000_04', 7)	# 199264-199270	 **attackbox here**
    sprite('iz000_05', 7)	# 199271-199277	 **attackbox here**
    sprite('iz000_06', 7)	# 199278-199284	 **attackbox here**
    sprite('iz000_07', 7)	# 199285-199291	 **attackbox here**
    sprite('iz000_08', 7)	# 199292-199298	 **attackbox here**
    sprite('iz000_09', 7)	# 199299-199305	 **attackbox here**
    loopRest()
    gotoLabel(213)

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
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('use'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('kym'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('iz611_00', 6)	# 4-9
    sprite('iz611_01', 6)	# 10-15
    sprite('iz611_02', 6)	# 16-21
    sprite('iz611_03', 6)	# 22-27
    sprite('iz611_04', 6)	# 28-33
    sprite('iz611_05', 6)	# 34-39
    sprite('iz611_06', 6)	# 40-45
    sprite('iz611_07', 6)	# 46-51
    sprite('iz611_08', 6)	# 52-57
    sprite('iz611_09', 6)	# 58-63
    sprite('iz611_10', 6)	# 64-69
    if SLOT_158:
        if SLOT_52:
            Unknown7006('biz524', 100, 897214818, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('biz402_0', 100, 880437602, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('biz523', 100, 897214818, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('iz611_11', 6)	# 70-75
    sprite('iz611_12', 6)	# 76-81
    sprite('iz611_13', 6)	# 82-87
    Unknown23018(1)
    label(1)
    sprite('iz611_10', 6)	# 88-93
    sprite('iz611_11', 6)	# 94-99
    sprite('iz611_12', 6)	# 100-105
    sprite('iz611_13', 6)	# 106-111
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('iz612_00', 5)	# 112-116
    sprite('iz612_01', 5)	# 117-121
    sprite('iz612_02', 5)	# 122-126
    sprite('iz612_03', 5)	# 127-131
    sprite('iz612_04', 5)	# 132-136
    sprite('iz612_05', 5)	# 137-141
    sprite('iz612_06', 5)	# 142-146
    if SLOT_158:
        if SLOT_52:
            Unknown7006('biz524', 100, 897214818, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('biz402_0', 100, 880437602, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('biz522', 100, 897214818, 12338, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('iz612_07', 5)	# 147-151
    sprite('iz612_08', 6)	# 152-157
    sprite('iz612_09', 6)	# 158-163
    sprite('iz612_10', 6)	# 164-169
    sprite('iz612_11', 6)	# 170-175
    Unknown23018(1)
    label(11)
    sprite('iz612_07', 6)	# 176-181
    sprite('iz612_08', 6)	# 182-187
    sprite('iz612_09', 6)	# 188-193
    sprite('iz612_10', 6)	# 194-199
    sprite('iz612_11', 6)	# 200-205
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('iz611_00', 6)	# 206-211
    sprite('iz611_01', 6)	# 212-217
    sprite('iz611_02', 6)	# 218-223
    sprite('iz611_03', 6)	# 224-229
    sprite('iz611_04', 6)	# 230-235
    sprite('iz611_05', 6)	# 236-241
    sprite('iz611_06', 6)	# 242-247
    sprite('iz611_07', 6)	# 248-253
    sprite('iz611_08', 6)	# 254-259
    sprite('iz611_09', 6)	# 260-265
    sprite('iz611_10', 6)	# 266-271
    SFX_1('biz700bno')
    sprite('iz611_11', 6)	# 272-277
    sprite('iz611_12', 6)	# 278-283
    sprite('iz611_13', 6)	# 284-289
    label(101)
    sprite('iz611_10', 6)	# 290-295
    sprite('iz611_11', 6)	# 296-301
    sprite('iz611_12', 6)	# 302-307
    sprite('iz611_13', 6)	# 308-313
    loopRest()
    if SLOT_97:
        _gotolabel(101)
    sprite('iz611_10', 6)	# 314-319
    sprite('iz611_11', 6)	# 320-325
    sprite('iz611_12', 6)	# 326-331
    sprite('iz611_13', 6)	# 332-337
    Unknown21007(24, 40)
    Unknown21011(240)
    label(102)
    sprite('iz611_10', 6)	# 338-343
    sprite('iz611_11', 6)	# 344-349
    sprite('iz611_12', 6)	# 350-355
    sprite('iz611_13', 6)	# 356-361
    loopRest()
    gotoLabel(102)
    label(110)
    sprite('iz612_00', 5)	# 362-366
    sprite('iz612_01', 5)	# 367-371
    sprite('iz612_02', 5)	# 372-376
    sprite('iz612_03', 5)	# 377-381
    sprite('iz612_04', 5)	# 382-386
    sprite('iz612_05', 5)	# 387-391
    sprite('iz612_06', 5)	# 392-396
    SFX_1('biz700pbc')
    sprite('iz612_07', 5)	# 397-401
    sprite('iz612_08', 6)	# 402-407
    sprite('iz612_09', 6)	# 408-413
    sprite('iz612_10', 6)	# 414-419
    sprite('iz612_11', 6)	# 420-425
    label(111)
    sprite('iz612_07', 6)	# 426-431
    sprite('iz612_08', 6)	# 432-437
    sprite('iz612_09', 6)	# 438-443
    sprite('iz612_10', 6)	# 444-449
    sprite('iz612_11', 6)	# 450-455
    loopRest()
    if SLOT_97:
        _gotolabel(111)
    sprite('iz612_07', 1)	# 456-456
    Unknown21007(24, 40)
    Unknown21011(320)
    label(112)
    sprite('iz612_07', 6)	# 457-462
    sprite('iz612_08', 6)	# 463-468
    sprite('iz612_09', 6)	# 469-474
    sprite('iz612_10', 6)	# 475-480
    sprite('iz612_11', 6)	# 481-486
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('iz612_00', 5)	# 487-491
    sprite('iz612_01', 5)	# 492-496
    sprite('iz612_02', 5)	# 497-501
    sprite('iz612_03', 5)	# 502-506
    sprite('iz612_04', 5)	# 507-511
    sprite('iz612_05', 5)	# 512-516
    sprite('iz612_06', 5)	# 517-521
    SFX_1('biz700rbl')
    sprite('iz612_07', 5)	# 522-526
    sprite('iz612_08', 6)	# 527-532
    sprite('iz612_09', 6)	# 533-538
    sprite('iz612_10', 6)	# 539-544
    sprite('iz612_11', 6)	# 545-550
    label(121)
    sprite('iz612_07', 6)	# 551-556
    sprite('iz612_08', 6)	# 557-562
    sprite('iz612_09', 6)	# 563-568
    sprite('iz612_10', 6)	# 569-574
    sprite('iz612_11', 6)	# 575-580
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('iz612_07', 6)	# 581-586
    sprite('iz612_08', 6)	# 587-592
    sprite('iz612_09', 6)	# 593-598
    sprite('iz612_10', 6)	# 599-604
    sprite('iz612_11', 6)	# 605-610
    Unknown21007(24, 40)
    Unknown21011(320)
    label(122)
    sprite('iz612_07', 6)	# 611-616
    sprite('iz612_08', 6)	# 617-622
    sprite('iz612_09', 6)	# 623-628
    sprite('iz612_10', 6)	# 629-634
    sprite('iz612_11', 6)	# 635-640
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('iz612_00', 5)	# 641-645
    sprite('iz612_01', 5)	# 646-650
    sprite('iz612_02', 5)	# 651-655
    sprite('iz612_03', 5)	# 656-660
    sprite('iz612_04', 5)	# 661-665
    sprite('iz612_05', 5)	# 666-670
    sprite('iz612_06', 5)	# 671-675
    SFX_1('biz700uor')
    sprite('iz612_07', 5)	# 676-680
    sprite('iz612_08', 6)	# 681-686
    sprite('iz612_09', 6)	# 687-692
    sprite('iz612_10', 6)	# 693-698
    sprite('iz612_11', 6)	# 699-704
    label(131)
    sprite('iz612_07', 6)	# 705-710
    sprite('iz612_08', 6)	# 711-716
    sprite('iz612_09', 6)	# 717-722
    sprite('iz612_10', 6)	# 723-728
    sprite('iz612_11', 6)	# 729-734
    loopRest()
    if SLOT_97:
        _gotolabel(131)
    sprite('iz612_07', 6)	# 735-740
    sprite('iz612_08', 6)	# 741-746
    sprite('iz612_09', 6)	# 747-752
    sprite('iz612_10', 6)	# 753-758
    sprite('iz612_11', 6)	# 759-764
    Unknown21007(24, 40)
    Unknown21011(380)
    label(132)
    sprite('iz612_07', 6)	# 765-770
    sprite('iz612_08', 6)	# 771-776
    sprite('iz612_09', 6)	# 777-782
    sprite('iz612_10', 6)	# 783-788
    sprite('iz612_11', 6)	# 789-794
    loopRest()
    gotoLabel(132)
    label(140)
    sprite('iz615_00', 6)	# 795-800
    sprite('iz615_01', 6)	# 801-806
    sprite('iz615_02', 6)	# 807-812
    sprite('iz615_03', 6)	# 813-818
    sprite('iz615_04', 6)	# 819-824
    sprite('iz615_05', 6)	# 825-830
    SFX_1('biz700uyu')
    sprite('iz615_06', 6)	# 831-836
    sprite('iz615_07', 6)	# 837-842
    label(141)
    sprite('iz615_08', 1)	# 843-843
    if SLOT_97:
        _gotolabel(141)
    sprite('iz615_08', 32767)	# 844-33610
    Unknown21007(24, 40)
    Unknown21011(200)
    label(150)
    sprite('iz000_00', 1)	# 33611-33611	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('iz000_00', 7)	# 33612-33618	 **attackbox here**
    sprite('iz000_01', 7)	# 33619-33625	 **attackbox here**
    sprite('iz000_02', 7)	# 33626-33632	 **attackbox here**
    sprite('iz000_03', 7)	# 33633-33639	 **attackbox here**
    sprite('iz000_04', 7)	# 33640-33646	 **attackbox here**
    sprite('iz000_05', 7)	# 33647-33653	 **attackbox here**
    sprite('iz000_06', 7)	# 33654-33660	 **attackbox here**
    sprite('iz000_07', 7)	# 33661-33667	 **attackbox here**
    sprite('iz000_08', 7)	# 33668-33674	 **attackbox here**
    sprite('iz000_09', 7)	# 33675-33681	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('iz615_00', 6)	# 33682-33687
    sprite('iz615_01', 6)	# 33688-33693
    sprite('iz615_02', 6)	# 33694-33699
    sprite('iz615_03', 6)	# 33700-33705
    sprite('iz615_04', 6)	# 33706-33711
    sprite('iz615_05', 6)	# 33712-33717
    SFX_1('biz701bha')
    sprite('iz615_06', 6)	# 33718-33723
    sprite('iz615_07', 6)	# 33724-33729
    Unknown23018(1)
    sprite('iz615_08', 32767)	# 33730-66496
    label(160)
    sprite('iz000_00', 1)	# 66497-66497	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('iz000_00', 7)	# 66498-66504	 **attackbox here**
    sprite('iz000_01', 7)	# 66505-66511	 **attackbox here**
    sprite('iz000_02', 7)	# 66512-66518	 **attackbox here**
    sprite('iz000_03', 7)	# 66519-66525	 **attackbox here**
    sprite('iz000_04', 7)	# 66526-66532	 **attackbox here**
    sprite('iz000_05', 7)	# 66533-66539	 **attackbox here**
    sprite('iz000_06', 7)	# 66540-66546	 **attackbox here**
    sprite('iz000_07', 7)	# 66547-66553	 **attackbox here**
    sprite('iz000_08', 7)	# 66554-66560	 **attackbox here**
    sprite('iz000_09', 7)	# 66561-66567	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('iz615_00', 6)	# 66568-66573
    sprite('iz615_01', 6)	# 66574-66579
    sprite('iz615_02', 6)	# 66580-66585
    sprite('iz615_03', 6)	# 66586-66591
    sprite('iz615_04', 6)	# 66592-66597
    sprite('iz615_05', 6)	# 66598-66603
    SFX_1('biz701bjn')
    sprite('iz615_06', 6)	# 66604-66609
    sprite('iz615_07', 6)	# 66610-66615
    Unknown23018(1)
    sprite('iz615_08', 32767)	# 66616-99382
    label(170)
    sprite('iz000_00', 1)	# 99383-99383	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('iz000_00', 7)	# 99384-99390	 **attackbox here**
    sprite('iz000_01', 7)	# 99391-99397	 **attackbox here**
    sprite('iz000_02', 7)	# 99398-99404	 **attackbox here**
    sprite('iz000_03', 7)	# 99405-99411	 **attackbox here**
    sprite('iz000_04', 7)	# 99412-99418	 **attackbox here**
    sprite('iz000_05', 7)	# 99419-99425	 **attackbox here**
    sprite('iz000_06', 7)	# 99426-99432	 **attackbox here**
    sprite('iz000_07', 7)	# 99433-99439	 **attackbox here**
    sprite('iz000_08', 7)	# 99440-99446	 **attackbox here**
    sprite('iz000_09', 7)	# 99447-99453	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('iz611_00', 6)	# 99454-99459
    sprite('iz611_01', 6)	# 99460-99465
    sprite('iz611_02', 6)	# 99466-99471
    sprite('iz611_03', 6)	# 99472-99477
    sprite('iz611_04', 6)	# 99478-99483
    sprite('iz611_05', 6)	# 99484-99489
    sprite('iz611_06', 6)	# 99490-99495
    sprite('iz611_07', 6)	# 99496-99501
    sprite('iz611_08', 6)	# 99502-99507
    sprite('iz611_09', 6)	# 99508-99513
    sprite('iz611_10', 6)	# 99514-99519
    SFX_1('biz701bma')
    sprite('iz611_11', 6)	# 99520-99525
    sprite('iz611_12', 6)	# 99526-99531
    sprite('iz611_13', 6)	# 99532-99537
    Unknown23018(1)
    label(173)
    sprite('iz611_10', 6)	# 99538-99543
    sprite('iz611_11', 6)	# 99544-99549
    sprite('iz611_12', 6)	# 99550-99555
    sprite('iz611_13', 6)	# 99556-99561
    loopRest()
    gotoLabel(173)
    label(180)
    sprite('iz000_00', 1)	# 99562-99562	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('iz000_00', 7)	# 99563-99569	 **attackbox here**
    sprite('iz000_01', 7)	# 99570-99576	 **attackbox here**
    sprite('iz000_02', 7)	# 99577-99583	 **attackbox here**
    sprite('iz000_03', 7)	# 99584-99590	 **attackbox here**
    sprite('iz000_04', 7)	# 99591-99597	 **attackbox here**
    sprite('iz000_05', 7)	# 99598-99604	 **attackbox here**
    sprite('iz000_06', 7)	# 99605-99611	 **attackbox here**
    sprite('iz000_07', 7)	# 99612-99618	 **attackbox here**
    sprite('iz000_08', 7)	# 99619-99625	 **attackbox here**
    sprite('iz000_09', 7)	# 99626-99632	 **attackbox here**
    gotoLabel(181)
    label(182)
    sprite('iz611_00', 6)	# 99633-99638
    sprite('iz611_01', 6)	# 99639-99644
    sprite('iz611_02', 6)	# 99645-99650
    sprite('iz611_03', 6)	# 99651-99656
    sprite('iz611_04', 6)	# 99657-99662
    sprite('iz611_05', 6)	# 99663-99668
    sprite('iz611_06', 6)	# 99669-99674
    sprite('iz611_07', 6)	# 99675-99680
    sprite('iz611_08', 6)	# 99681-99686
    sprite('iz611_09', 6)	# 99687-99692
    sprite('iz611_10', 6)	# 99693-99698
    SFX_1('biz701bmk')
    sprite('iz611_11', 6)	# 99699-99704
    sprite('iz611_12', 6)	# 99705-99710
    sprite('iz611_13', 6)	# 99711-99716
    Unknown23018(1)
    label(183)
    sprite('iz611_10', 6)	# 99717-99722
    sprite('iz611_11', 6)	# 99723-99728
    sprite('iz611_12', 6)	# 99729-99734
    sprite('iz611_13', 6)	# 99735-99740
    loopRest()
    gotoLabel(183)
    label(190)
    sprite('iz615_00', 6)	# 99741-99746
    sprite('iz615_01', 6)	# 99747-99752
    sprite('iz615_02', 6)	# 99753-99758
    sprite('iz615_03', 6)	# 99759-99764
    sprite('iz615_04', 6)	# 99765-99770
    sprite('iz615_05', 6)	# 99771-99776
    SFX_1('biz700use')
    sprite('iz615_06', 6)	# 99777-99782
    sprite('iz615_07', 6)	# 99783-99788
    label(191)
    sprite('iz615_08', 1)	# 99789-99789
    if SLOT_97:
        _gotolabel(191)
    sprite('iz615_08', 30)	# 99790-99819
    sprite('iz615_08', 32767)	# 99820-132586
    Unknown21007(24, 40)
    Unknown21011(180)
    label(200)
    sprite('iz615_00', 6)	# 132587-132592
    sprite('iz615_01', 6)	# 132593-132598
    sprite('iz615_02', 6)	# 132599-132604
    sprite('iz615_03', 6)	# 132605-132610
    sprite('iz615_04', 6)	# 132611-132616
    sprite('iz615_05', 6)	# 132617-132622
    SFX_1('biz700kym')
    sprite('iz615_06', 6)	# 132623-132628
    sprite('iz615_07', 6)	# 132629-132634
    label(201)
    sprite('iz615_08', 1)	# 132635-132635
    if SLOT_97:
        _gotolabel(201)
    sprite('iz615_08', 30)	# 132636-132665
    sprite('iz615_08', 32767)	# 132666-165432
    Unknown21007(24, 40)
    Unknown21011(160)

@State
def CmnActLose():
    sprite('iz620_00', 6)	# 1-6
    Unknown4047(64, 65, 66)
    Unknown4049(300)
    Unknown4045('697a65665f74696d656f7574000000000000000000000000000000000000000000000000')
    if SLOT_158:
        Unknown7006('biz403_0', 100, 880437602, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('iz620_01', 6)	# 7-12
    Unknown4047(64, 65, 66)
    Unknown4049(300)
    Unknown4045('697a65665f74696d656f7574000000000000000000000000000000000000000000000000')
    sprite('iz620_02', 6)	# 13-18
    Unknown4047(64, 65, 66)
    Unknown4049(300)
    Unknown4045('697a65665f74696d656f7574000000000000000000000000000000000000000000000000')
    sprite('iz620_03', 6)	# 19-24
    sprite('iz620_04', 6)	# 25-30
    sprite('iz620_05', 6)	# 31-36
    sprite('iz620_06', 6)	# 37-42
    sprite('iz620_07', 6)	# 43-48
    Unknown23018(1)
    sprite('iz620_08', 32767)	# 49-32815
