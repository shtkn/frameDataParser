@Subroutine
def PreInit():
    Unknown12019('75766100000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
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
    Unknown14015(-3000, 400000, -91000, 127000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(100)
    Unknown15013(4000)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(6000, 300000, -172000, 24000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(-3000, 440000, -91000, 127000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(-3000, 460000, -170000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(-10000, 600000, -219000, -10000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 300000, -300000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5A2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-1000, 300000, -300000, -51000, 10, 0)
    Unknown15016(1, 200, 500)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(-1000, 250000, -10000000, -10000, 10, 0)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(16000, 130000, -112000, 132000, 100, 10)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(16000, 130000, -112000, 132000, 100, 10)
    Move_EndRegister()
    Move_Register('aruma1', INPUT_SPECIALMOVE)
    Move_Input_(0x37)
    Unknown14005(1)
    Unknown14019('Funcaruma1')
    Move_EndRegister()
    Move_Register('aruma2', INPUT_SPECIALMOVE)
    Move_Input_(0x44)
    Unknown14005(1)
    Unknown14019('Funcaruma2')
    Move_EndRegister()
    Move_Register('aruma3', INPUT_SPECIALMOVE)
    Move_Input_(0x51)
    Unknown14005(1)
    Unknown14019('Funcaruma3')
    Move_EndRegister()
    Move_Register('aruma4', INPUT_SPECIALMOVE)
    Move_Input_(0x5e)
    Unknown14005(1)
    Unknown14019('Funcaruma4')
    Move_EndRegister()
    Move_Register('aruma6', INPUT_SPECIALMOVE)
    Move_Input_(0x78)
    Unknown14005(1)
    Unknown14019('Funcaruma6')
    Move_EndRegister()
    Move_Register('aruma7', INPUT_SPECIALMOVE)
    Move_Input_(0x85)
    Unknown14005(1)
    Unknown14019('Funcaruma7')
    Move_EndRegister()
    Move_Register('aruma8', INPUT_SPECIALMOVE)
    Move_Input_(0x92)
    Unknown14005(1)
    Unknown14019('Funcaruma8')
    Move_EndRegister()
    Move_Register('aruma9', INPUT_SPECIALMOVE)
    Move_Input_(0x9f)
    Unknown14005(1)
    Unknown14019('Funcaruma9')
    Move_EndRegister()
    Move_Register('BeamA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(800000, 10000000, -223000, 100000, 100, 10)
    Move_EndRegister()
    Move_Register('BeamB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(500000, 1000000, 150000, 500000, 100, 10)
    Move_EndRegister()
    Move_Register('Beam_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(800000, 10000000, -223000, 100000, 100, 10)
    Move_EndRegister()
    Move_Register('ShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(300000, 1000000, -223000, 150000, 200, 10)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(300000, 1000000, -223000, 100000, 200, 10)
    Move_EndRegister()
    Move_Register('BigShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(300000, 1000000, -223000, 150000, 100, 10)
    Move_EndRegister()
    Move_Register('AirBeamA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(800000, 10000000, -223000, 100000, 100, 0)
    Move_EndRegister()
    Move_Register('AirBeamB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(500000, 4000000, -350000, -600000, 100, 0)
    Move_EndRegister()
    Move_Register('AirBeam_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(800000, 10000000, -223000, 100000, 100, 0)
    Move_EndRegister()
    Move_Register('AirShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(500000, 4000000, -350000, -600000, 200, 0)
    Move_EndRegister()
    Move_Register('AirShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(500000, 4000000, -350000, -600000, 200, 0)
    Move_EndRegister()
    Move_Register('AirBigShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(500000, 4000000, -350000, -600000, 200, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(1000, 400000, -223000, 355000, 200, 0)
    Unknown15016(0, 1, 500)
    Unknown15016(1, 1, 500)
    Unknown15016(2, 1, 500)
    Move_EndRegister()
    Move_Register('AntiAir2nd', INPUT_SPECIALMOVE)
    Unknown15013(10000)
    Unknown15006(100000)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(307000, 1466000, -223000, 355000, 100, 50)
    Unknown15022('030000000500000032000000f4010000')
    Move_EndRegister()
    Move_Register('UltimateShot_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(307000, 1466000, -223000, 355000, 100, 50)
    Unknown15022('030000000500000032000000f4010000')
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(1000, 400000, -223000, 355000, 500, 50)
    Unknown15022('030000000500000032000000f4010000')
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(1000, 400000, -223000, 355000, 500, 50)
    Unknown15022('030000000500000032000000f4010000')
    Move_EndRegister()
    Move_Register('AirUltimateShot', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(307000, 1466000, -223000, 355000, 100, 50)
    Unknown15022('030000000500000032000000f4010000')
    Move_EndRegister()
    Move_Register('AirUltimateShot_OD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(307000, 1466000, -223000, 355000, 100, 50)
    Unknown15022('030000000500000032000000f4010000')
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk2C', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'NmlAtk5B3rd', 10000000)
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
    Unknown12018(16, 'Action_303_00')
    Unknown12018(17, 'Action_304_00')
    Unknown12018(18, 'Action_305_00')
    Unknown12018(19, 'Action_000_00')
    Unknown12018(20, 'Action_000_00')
    Unknown12018(25, 'Action_326_00')
    Unknown12018(26, 'Action_326_02')
    Unknown12018(27, 'Action_326_03')
    Unknown12018(28, 'Action_351_05')
    Unknown12018(29, 'Action_292_00')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'uva000')
    Unknown7010(1, 'uva001')
    Unknown7010(2, 'uva002')
    Unknown7010(3, 'uva003')
    Unknown7010(4, 'uva004')
    Unknown7010(5, 'uva005')
    Unknown7010(6, 'uva006')
    Unknown7010(7, 'uva007')
    Unknown7010(8, 'uva008')
    Unknown7010(9, 'uva009')
    Unknown7010(10, 'uva010')
    Unknown7010(15, 'uva011')
    Unknown7010(16, 'uva012')
    Unknown7010(17, 'uva013')
    Unknown7010(18, 'uva014')
    Unknown7010(19, 'uva015')
    Unknown7010(20, 'uva016')
    Unknown7010(21, 'uva017')
    Unknown7010(22, 'uva018')
    Unknown7010(23, 'uva019')
    Unknown7010(24, 'uva020')
    Unknown7010(25, 'uva021')
    Unknown7010(28, 'uva022')
    Unknown7010(29, 'uva023')
    Unknown7010(30, 'uva024')
    Unknown7010(31, 'uva025')
    Unknown7010(32, 'uva026')
    Unknown7010(33, 'uva027')
    Unknown7010(34, 'uva028')
    Unknown7010(35, 'uva029')
    Unknown7010(36, 'uva030')
    Unknown7010(37, 'uva031')
    Unknown7010(41, 'uva032')
    Unknown7010(42, 'uva033')
    Unknown7010(43, 'uva034')
    Unknown7010(44, 'uva035')
    Unknown7010(45, 'uva036')
    Unknown7010(46, 'uva037')
    Unknown7010(47, 'uva038')
    Unknown7010(48, 'uva039')
    Unknown7010(49, 'uva040')
    Unknown7010(50, 'uva041')
    Unknown7010(52, 'uva042')
    Unknown7010(53, 'uva043')
    Unknown7010(54, 'uva100_0')
    Unknown7010(55, 'uva100_1')
    Unknown7010(56, 'uva100_2')
    Unknown7010(63, 'uva101_0')
    Unknown7010(64, 'uva101_1')
    Unknown7010(65, 'uva101_2')
    Unknown7010(57, 'uva102_0')
    Unknown7010(58, 'uva102_1')
    Unknown7010(59, 'uva102_2')
    Unknown7010(66, 'uva103_0')
    Unknown7010(67, 'uva103_1')
    Unknown7010(68, 'uva103_2')
    Unknown7010(60, 'uva104_0')
    Unknown7010(61, 'uva104_1')
    Unknown7010(62, 'uva104_2')
    Unknown7010(69, 'uva105_0')
    Unknown7010(70, 'uva105_1')
    Unknown7010(71, 'uva105_2')
    Unknown7010(72, 'uva150')
    Unknown7010(73, 'uva151')
    Unknown7010(74, 'uva152')
    Unknown7010(85, 'uva153')
    Unknown7010(94, 'uva400')
    Unknown7010(95, 'uva401')
    Unknown7010(96, 'uva161_0')
    Unknown7010(97, 'uva161_1')
    Unknown7010(98, 'uva163_0')
    Unknown7010(99, 'uva163_1')
    Unknown7010(100, 'uva164_0')
    Unknown7010(101, 'uva164_1')
    Unknown7010(102, 'uva166_0')
    Unknown7010(103, 'uva166_1')
    Unknown7010(92, 'uva162_0')
    Unknown7010(93, 'uva162_1')
    Unknown7010(90, 'uva167_0')
    Unknown7010(91, 'uva167_1')
    Unknown7010(105, 'uva165_0')
    Unknown7010(106, 'uva165_1')
    Unknown7010(107, 'uva168_0')
    Unknown7010(108, 'uva168_1')
    Unknown7010(110, 'uva169_0')
    Unknown7010(111, 'uva169_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3541000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745f4f440000000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def AddChainarumaAir():
    WhiffCancelEnable(1)
    WhiffCancel('aruma1')
    WhiffCancel('aruma2')
    WhiffCancel('aruma3')
    WhiffCancel('aruma4')
    WhiffCancel('aruma6')
    WhiffCancel('aruma7')
    WhiffCancel('aruma8')
    WhiffCancel('aruma9')

@Subroutine
def Funcaruma1():
    Unknown1084(1)
    physicsXImpulse(-4000)
    if (SLOT_23 < 10000):
        physicsYImpulse(0)
    else:
        physicsYImpulse(-4000)

@Subroutine
def Funcaruma2():
    Unknown1084(1)
    if (SLOT_23 < 10000):
        physicsYImpulse(0)
    else:
        physicsYImpulse(-4000)

@Subroutine
def Funcaruma3():
    Unknown1084(1)
    physicsXImpulse(12000)
    if (SLOT_23 < 10000):
        physicsYImpulse(0)
    else:
        physicsYImpulse(-4000)

@Subroutine
def Funcaruma4():
    Unknown1084(1)
    physicsXImpulse(-4000)

@Subroutine
def Funcaruma6():
    Unknown1084(1)
    physicsXImpulse(12000)

@Subroutine
def Funcaruma7():
    Unknown1084(1)
    physicsXImpulse(-4000)
    if SLOT_36:
        physicsYImpulse(4000)

@Subroutine
def Funcaruma8():
    Unknown1084(1)
    physicsYImpulse(4000)

@Subroutine
def Funcaruma9():
    Unknown1084(1)
    physicsXImpulse(12000)
    if SLOT_36:
        physicsYImpulse(4000)

@Subroutine
def OnActionBeginPre():
    Recovery()

@Subroutine
def EnableAirShot():
    SLOT_47 = 0
    if (not SLOT_59):
        SLOT_47 = 1

@Subroutine
def OnLanding():
    SLOT_59 = 0

@Subroutine
def OnPreDraw():
    Unknown23030('5556415f4c696e65416e696d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def CmnActStand():
    sprite('Action_000_00', 1)	# 1-1	 **attackbox here**
    label(0)
    sprite('Action_000_01', 5)	# 2-6	 **attackbox here**
    sprite('Action_000_02', 5)	# 7-11	 **attackbox here**
    sprite('Action_000_03', 5)	# 12-16	 **attackbox here**
    sprite('Action_000_04', 5)	# 17-21	 **attackbox here**
    sprite('Action_000_05', 5)	# 22-26	 **attackbox here**
    sprite('Action_000_06', 5)	# 27-31	 **attackbox here**
    sprite('Action_000_07', 5)	# 32-36	 **attackbox here**
    sprite('Action_000_08', 5)	# 37-41	 **attackbox here**
    sprite('Action_000_09', 5)	# 42-46	 **attackbox here**
    sprite('Action_000_10', 5)	# 47-51	 **attackbox here**
    sprite('Action_000_11', 5)	# 52-56	 **attackbox here**
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 0)
    if SLOT_0:
        _gotolabel(0)
    sprite('Action_000_13', 5)	# 57-61	 **attackbox here**
    SLOT_88 = 960
    sprite('Action_000_14', 5)	# 62-66	 **attackbox here**
    SFX_1('uva000')
    sprite('Action_000_15', 6)	# 67-72	 **attackbox here**
    sprite('Action_000_16', 7)	# 73-79	 **attackbox here**
    sprite('Action_000_17', 7)	# 80-86	 **attackbox here**
    sprite('Action_000_18', 7)	# 87-93	 **attackbox here**
    sprite('Action_000_19', 7)	# 94-100	 **attackbox here**
    sprite('Action_000_20', 5)	# 101-105	 **attackbox here**
    sprite('Action_000_21', 6)	# 106-111	 **attackbox here**
    sprite('Action_000_22', 8)	# 112-119	 **attackbox here**
    sprite('Action_000_23', 6)	# 120-125	 **attackbox here**
    sprite('Action_000_24', 5)	# 126-130	 **attackbox here**
    sprite('Action_000_25', 5)	# 131-135	 **attackbox here**
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_015_01', 4)	# 5-8	 **attackbox here**

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_012_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_012_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_012_03', 1)	# 10-10	 **attackbox here**

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_013_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_013_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_013_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_013_04', 5)	# 21-25	 **attackbox here**
    sprite('Action_013_05', 5)	# 26-30	 **attackbox here**
    sprite('Action_013_06', 5)	# 31-35	 **attackbox here**
    sprite('Action_013_07', 5)	# 36-40	 **attackbox here**
    sprite('Action_013_08', 5)	# 41-45	 **attackbox here**
    sprite('Action_013_09', 5)	# 46-50	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_016_01', 4)	# 5-8	 **attackbox here**

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_014_01', 4)	# 4-7	 **attackbox here**
    sprite('Action_014_02', 5)	# 8-12	 **attackbox here**
    sprite('Action_014_03', 4)	# 13-16	 **attackbox here**
    sprite('Action_014_04', 4)	# 17-20	 **attackbox here**
    sprite('Action_014_05', 3)	# 21-23	 **attackbox here**
    sprite('Action_014_06', 2)	# 24-25	 **attackbox here**
    sprite('Action_014_07', 3)	# 26-28	 **attackbox here**

@State
def CmnActJumpPre():
    Unknown3029(0)
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    sprite('Action_036_00', 4)	# 1-4	 **attackbox here**
    ExitState()
    label(0)
    sprite('Action_035_00', 4)	# 5-8	 **attackbox here**
    ExitState()
    label(1)
    sprite('Action_037_00', 4)	# 9-12	 **attackbox here**
    ExitState()

@State
def CmnActJumpUpper():
    Unknown3029(0)
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    sprite('Action_036_01', 4)	# 1-4	 **attackbox here**
    sprite('Action_036_02', 4)	# 5-8	 **attackbox here**
    ExitState()
    label(0)
    sprite('Action_035_01', 4)	# 9-12	 **attackbox here**
    sprite('Action_035_02', 4)	# 13-16	 **attackbox here**
    ExitState()
    label(1)
    sprite('Action_037_01', 4)	# 17-20	 **attackbox here**
    sprite('Action_037_02', 4)	# 21-24	 **attackbox here**
    sprite('Action_037_03', 3)	# 25-27	 **attackbox here**
    ExitState()

@State
def CmnActJumpUpperEnd():
    Unknown3029(0)
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    sprite('Action_036_03', 4)	# 1-4	 **attackbox here**
    sprite('Action_036_04', 4)	# 5-8	 **attackbox here**
    sprite('Action_036_05', 4)	# 9-12	 **attackbox here**
    ExitState()
    label(0)
    sprite('Action_035_03', 4)	# 13-16	 **attackbox here**
    sprite('Action_035_04', 4)	# 17-20	 **attackbox here**
    sprite('Action_035_05', 4)	# 21-24	 **attackbox here**
    ExitState()
    label(1)
    sprite('Action_037_04', 3)	# 25-27	 **attackbox here**
    sprite('Action_037_05', 3)	# 28-30	 **attackbox here**
    sprite('Action_037_06', 3)	# 31-33	 **attackbox here**
    sprite('Action_037_07', 3)	# 34-36	 **attackbox here**
    sprite('Action_037_08', 3)	# 37-39	 **attackbox here**
    ExitState()

@State
def CmnActJumpDown():
    Unknown3029(0)
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    sprite('Action_036_06', 4)	# 1-4	 **attackbox here**
    sprite('Action_036_07', 3)	# 5-7	 **attackbox here**
    label(20)
    sprite('Action_036_08', 3)	# 8-10	 **attackbox here**
    sprite('Action_036_09', 3)	# 11-13	 **attackbox here**
    gotoLabel(20)
    label(0)
    sprite('Action_035_06', 4)	# 14-17	 **attackbox here**
    sprite('Action_035_07', 3)	# 18-20	 **attackbox here**
    label(10)
    sprite('Action_035_08', 3)	# 21-23	 **attackbox here**
    sprite('Action_035_09', 3)	# 24-26	 **attackbox here**
    gotoLabel(10)
    label(1)
    sprite('Action_037_09', 3)	# 27-29	 **attackbox here**
    sprite('Action_037_10', 3)	# 30-32	 **attackbox here**
    sprite('Action_037_11', 3)	# 33-35	 **attackbox here**
    gotoLabel(1)

@State
def CmnActJumpLanding():
    Unknown3029(0)
    sprite('Action_037_12', 3)	# 1-3	 **attackbox here**
    sprite('Action_037_13', 6)	# 4-9	 **attackbox here**
    sprite('Action_037_14', 5)	# 10-14	 **attackbox here**

@State
def CmnActLandingStiffLoop():
    Unknown3029(0)
    sprite('Action_037_12', 3)	# 1-3	 **attackbox here**
    sprite('Action_037_13', 32767)	# 4-32770	 **attackbox here**

@State
def CmnActLandingStiffEnd():
    Unknown3029(0)
    sprite('Action_037_14', 3)	# 1-3	 **attackbox here**

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_010_01', 4)	# 3-6	 **attackbox here**
    sprite('Action_010_02', 4)	# 7-10	 **attackbox here**
    sprite('Action_010_03', 4)	# 11-14	 **attackbox here**
    sprite('Action_010_04', 4)	# 15-18	 **attackbox here**
    sprite('Action_010_05', 4)	# 19-22	 **attackbox here**
    sprite('Action_010_06', 4)	# 23-26	 **attackbox here**
    sprite('Action_010_07', 4)	# 27-30	 **attackbox here**
    sprite('Action_010_08', 4)	# 31-34	 **attackbox here**
    sprite('Action_010_09', 4)	# 35-38	 **attackbox here**
    sprite('Action_010_10', 4)	# 39-42	 **attackbox here**
    sprite('Action_010_11', 4)	# 43-46	 **attackbox here**
    sprite('Action_010_12', 4)	# 47-50	 **attackbox here**
    sprite('Action_010_13', 4)	# 51-54	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('Action_011_00', 3)	# 1-3	 **attackbox here**
    label(0)
    sprite('Action_011_02', 4)	# 4-7	 **attackbox here**
    sprite('Action_011_03', 4)	# 8-11	 **attackbox here**
    sprite('Action_011_04', 4)	# 12-15	 **attackbox here**
    sprite('Action_011_05', 4)	# 16-19	 **attackbox here**
    sprite('Action_011_06', 4)	# 20-23	 **attackbox here**
    sprite('Action_011_07', 4)	# 24-27	 **attackbox here**
    sprite('Action_011_08', 4)	# 28-31	 **attackbox here**
    sprite('Action_011_09', 4)	# 32-35	 **attackbox here**
    sprite('Action_011_10', 4)	# 36-39	 **attackbox here**
    sprite('Action_011_11', 4)	# 40-43	 **attackbox here**
    sprite('Action_011_12', 4)	# 44-47	 **attackbox here**
    sprite('Action_011_13', 4)	# 48-51	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_045_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_045_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_045_02', 3)	# 7-9	 **attackbox here**
    SFX_3('SE050_SlideDash')
    sprite('Action_045_03', 3)	# 10-12	 **attackbox here**
    sprite('Action_045_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_045_05', 3)	# 16-18	 **attackbox here**
    sprite('Action_045_06', 3)	# 19-21	 **attackbox here**
    sprite('Action_045_07', 3)	# 22-24	 **attackbox here**
    sprite('Action_045_08', 3)	# 25-27	 **attackbox here**
    label(0)
    sprite('Action_045_01', 3)	# 28-30	 **attackbox here**
    sprite('Action_045_02', 3)	# 31-33	 **attackbox here**
    sprite('Action_045_03', 3)	# 34-36	 **attackbox here**
    sprite('Action_045_04', 3)	# 37-39	 **attackbox here**
    sprite('Action_045_05', 3)	# 40-42	 **attackbox here**
    sprite('Action_045_06', 3)	# 43-45	 **attackbox here**
    sprite('Action_045_07', 3)	# 46-48	 **attackbox here**
    sprite('Action_045_08', 3)	# 49-51	 **attackbox here**
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_09', 6)	# 1-6	 **attackbox here**

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincible(1)
        Unknown1084(1)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()

        def upon_3():
            Unknown1019(90)
    sprite('Action_011_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_046_01', 3)	# 4-6	 **attackbox here**
    physicsXImpulse(-43000)
    sprite('Action_046_02', 1)	# 7-7	 **attackbox here**
    sprite('Action_046_02', 2)	# 8-9	 **attackbox here**
    setInvincible(0)
    sprite('Action_046_03', 3)	# 10-12	 **attackbox here**
    sprite('Action_046_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_046_05', 3)	# 16-18	 **attackbox here**
    sprite('Action_046_06', 3)	# 19-21	 **attackbox here**
    sprite('Action_046_07', 3)	# 22-24	 **attackbox here**
    sprite('Action_046_08', 3)	# 25-27	 **attackbox here**
    sprite('Action_046_09', 3)	# 28-30	 **attackbox here**

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('Action_068_01', 3)	# 1-3	 **attackbox here**
    sprite('Action_068_02', 3)	# 4-6	 **attackbox here**
    sprite('Action_068_03', 3)	# 7-9	 **attackbox here**
    sprite('Action_068_04', 3)	# 10-12	 **attackbox here**
    sprite('Action_068_05', 3)	# 13-15	 **attackbox here**
    sprite('Action_068_06', 3)	# 16-18	 **attackbox here**
    sprite('Action_068_07', 3)	# 19-21	 **attackbox here**
    sprite('Action_068_08', 3)	# 22-24	 **attackbox here**
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
    sprite('Action_068_09', 3)	# 1-3	 **attackbox here**
    label(0)
    sprite('Action_068_10', 3)	# 4-6	 **attackbox here**
    sprite('Action_068_11', 3)	# 7-9	 **attackbox here**
    sprite('Action_068_12', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('Action_046_01', 2)	# 1-2	 **attackbox here**
    physicsYImpulse(12000)
    sprite('Action_046_02', 2)	# 3-4	 **attackbox here**
    sprite('Action_140_05', 2)	# 5-6	 **attackbox here**
    sprite('Action_140_06', 2)	# 7-8	 **attackbox here**
    sprite('Action_140_07', 2)	# 9-10	 **attackbox here**
    sprite('Action_140_08', 2)	# 11-12	 **attackbox here**
    sprite('Action_140_09', 2)	# 13-14	 **attackbox here**
    sprite('Action_140_10', 2)	# 15-16	 **attackbox here**
    sprite('Action_140_11', 2)	# 17-18	 **attackbox here**

@State
def CmnActHitStandLv1():
    sprite('Action_300_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_300_00', 1)	# 2-2	 **attackbox here**
    sprite('Action_300_01', 2)	# 3-4	 **attackbox here**

@State
def CmnActHitStandLv2():
    sprite('Action_300_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_300_00', 2)	# 2-3	 **attackbox here**
    sprite('Action_300_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActHitStandLv3():
    sprite('Action_303_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_303_00', 2)	# 2-3	 **attackbox here**
    sprite('Action_303_01', 2)	# 4-5	 **attackbox here**
    sprite('Action_303_02', 2)	# 6-7	 **attackbox here**
    sprite('Action_303_03', 2)	# 8-9	 **attackbox here**

@State
def CmnActHitStandLv4():
    sprite('Action_303_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_303_00', 1)	# 2-2	 **attackbox here**
    sprite('Action_303_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_303_02', 3)	# 6-8	 **attackbox here**
    sprite('Action_303_03', 2)	# 9-10	 **attackbox here**

@State
def CmnActHitStandLv5():
    sprite('Action_303_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_303_00', 3)	# 2-4	 **attackbox here**
    sprite('Action_303_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_303_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_303_03', 4)	# 13-16	 **attackbox here**

@State
def CmnActHitStandLowLv1():
    sprite('Action_304_02', 1)	# 1-1	 **attackbox here**
    sprite('Action_304_02', 1)	# 2-2	 **attackbox here**
    sprite('Action_304_03', 2)	# 3-4	 **attackbox here**

@State
def CmnActHitStandLowLv2():
    sprite('Action_304_02', 1)	# 1-1	 **attackbox here**
    sprite('Action_304_02', 2)	# 2-3	 **attackbox here**
    sprite('Action_304_03', 3)	# 4-6	 **attackbox here**

@State
def CmnActHitStandLowLv3():
    sprite('Action_304_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_304_00', 1)	# 2-2	 **attackbox here**
    sprite('Action_304_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_304_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_304_03', 2)	# 7-8	 **attackbox here**

@State
def CmnActHitStandLowLv4():
    sprite('Action_304_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_304_00', 1)	# 2-2	 **attackbox here**
    sprite('Action_304_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_304_02', 3)	# 6-8	 **attackbox here**
    sprite('Action_304_03', 2)	# 9-10	 **attackbox here**

@State
def CmnActHitStandLowLv5():
    sprite('Action_304_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_304_00', 3)	# 2-4	 **attackbox here**
    sprite('Action_304_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_304_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_304_03', 4)	# 13-16	 **attackbox here**

@State
def CmnActHitCrouchLv1():
    sprite('Action_305_02', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_02', 1)	# 2-2	 **attackbox here**
    sprite('Action_305_03', 2)	# 3-4	 **attackbox here**

@State
def CmnActHitCrouchLv2():
    sprite('Action_305_02', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_02', 2)	# 2-3	 **attackbox here**
    sprite('Action_305_03', 3)	# 4-6	 **attackbox here**

@State
def CmnActHitCrouchLv3():
    sprite('Action_305_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_00', 2)	# 2-3	 **attackbox here**
    sprite('Action_305_01', 2)	# 4-5	 **attackbox here**
    sprite('Action_305_02', 2)	# 6-7	 **attackbox here**
    sprite('Action_305_03', 2)	# 8-9	 **attackbox here**

@State
def CmnActHitCrouchLv4():
    sprite('Action_305_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_00', 1)	# 2-2	 **attackbox here**
    sprite('Action_305_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_305_02', 3)	# 6-8	 **attackbox here**
    sprite('Action_305_03', 2)	# 9-10	 **attackbox here**

@State
def CmnActHitCrouchLv5():
    sprite('Action_305_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_00', 3)	# 2-4	 **attackbox here**
    sprite('Action_305_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_305_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_305_03', 4)	# 13-16	 **attackbox here**

@State
def CmnActBDownUpper():
    sprite('Action_320_00', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_320_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_320_01', 4)	# 9-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('Action_320_02', 4)	# 1-4	 **attackbox here**

@State
def CmnActBDownDown():
    sprite('Action_320_02', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_330_08', 4)	# 5-8	 **attackbox here**
    sprite('Action_330_09', 4)	# 9-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('Action_351_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_331_01', 2)	# 3-4	 **attackbox here**

@State
def CmnActBDownBound():
    sprite('Action_351_01', 3)	# 1-3	 **attackbox here**
    sprite('Action_351_02', 3)	# 4-6	 **attackbox here**
    sprite('Action_351_03', 3)	# 7-9	 **attackbox here**
    sprite('Action_351_04', 3)	# 10-12	 **attackbox here**
    sprite('Action_351_05', 3)	# 13-15	 **attackbox here**

@State
def CmnActBDownLoop():
    sprite('Action_356_04', 1)	# 1-1	 **attackbox here**

@State
def CmnActBDown2Stand():
    sprite('Action_294_11', 4)	# 1-4	 **attackbox here**
    sprite('Action_294_12', 4)	# 5-8	 **attackbox here**
    sprite('Action_294_13', 3)	# 9-11	 **attackbox here**
    sprite('Action_294_14', 3)	# 12-14	 **attackbox here**
    sprite('Action_294_15', 4)	# 15-18	 **attackbox here**
    sprite('Action_294_16', 4)	# 19-22	 **attackbox here**
    sprite('Action_294_17', 4)	# 23-26	 **attackbox here**

@State
def CmnActFDownUpper():
    sprite('Action_326_00', 3)	# 1-3	 **attackbox here**

@State
def CmnActFDownUpperEnd():
    sprite('Action_326_01', 3)	# 1-3	 **attackbox here**

@State
def CmnActFDownDown():
    label(0)
    sprite('Action_326_03', 3)	# 1-3	 **attackbox here**
    sprite('Action_326_04', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('Action_351_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_351_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActFDownBound():
    sprite('Action_354_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_354_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_354_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_354_03', 4)	# 13-16	 **attackbox here**

@State
def CmnActFDownLoop():
    sprite('Action_292_00', 3)	# 1-3	 **attackbox here**

@State
def CmnActFDown2Stand():
    sprite('Action_294_11', 3)	# 1-3	 **attackbox here**
    sprite('Action_294_12', 3)	# 4-6	 **attackbox here**
    sprite('Action_294_13', 3)	# 7-9	 **attackbox here**
    sprite('Action_294_14', 3)	# 10-12	 **attackbox here**
    sprite('Action_294_15', 3)	# 13-15	 **attackbox here**
    sprite('Action_294_16', 3)	# 16-18	 **attackbox here**
    sprite('Action_294_17', 2)	# 19-20	 **attackbox here**

@State
def CmnActVDownUpper():
    sprite('Action_330_00', 3)	# 1-3	 **attackbox here**
    label(0)
    sprite('Action_330_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_330_02', 3)	# 7-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('Action_330_03', 2)	# 1-2	 **attackbox here**
    sprite('Action_330_04', 2)	# 3-4	 **attackbox here**
    sprite('Action_330_05', 2)	# 5-6	 **attackbox here**

@State
def CmnActVDownDown():
    sprite('Action_330_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_330_06', 3)	# 4-6	 **attackbox here**
    label(0)
    sprite('Action_330_08', 4)	# 7-10	 **attackbox here**
    sprite('Action_330_09', 4)	# 11-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('Action_351_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_351_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActBlowoff():
    sprite('Action_331_00', 2)	# 1-2	 **attackbox here**
    label(0)
    sprite('Action_331_02', 3)	# 3-5	 **attackbox here**
    sprite('Action_331_03', 3)	# 6-8	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('Action_333_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_333_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_333_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_333_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_333_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_333_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_333_06', 2)	# 13-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('Action_327_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_327_00', 2)	# 3-4	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('Action_327_00', 1)	# 1-1	 **attackbox here**

@State
def CmnActWallBound():
    sprite('Action_340_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_340_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_340_02', 2)	# 5-6	 **attackbox here**

@State
def CmnActWallBoundDown():
    sprite('Action_340_03', 3)	# 1-3	 **attackbox here**
    sprite('Action_340_04', 3)	# 4-6	 **attackbox here**
    label(0)
    sprite('Action_340_05', 3)	# 7-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('Action_327_00', 14)	# 1-14	 **attackbox here**

@State
def CmnActStaggerDown():
    sprite('Action_327_02', 5)	# 1-5	 **attackbox here**
    sprite('Action_327_03', 5)	# 6-10	 **attackbox here**
    sprite('Action_327_04', 4)	# 11-14	 **attackbox here**
    sprite('Action_328_00', 4)	# 15-18	 **attackbox here**
    sprite('Action_328_01', 4)	# 19-22	 **attackbox here**

@State
def CmnActUkemiStagger():
    sprite('Action_327_00', 8)	# 1-8	 **attackbox here**

@State
def CmnActUkemiAirF():
    sprite('Action_032_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_032_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_032_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_032_03', 1)	# 7-7	 **attackbox here**
    sprite('Action_032_04', 1)	# 8-8	 **attackbox here**
    sprite('Action_032_05', 1)	# 9-9	 **attackbox here**

@State
def CmnActUkemiAirB():
    sprite('Action_032_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_032_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_032_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_032_03', 4)	# 13-16	 **attackbox here**
    sprite('Action_032_04', 4)	# 17-20	 **attackbox here**
    sprite('Action_032_05', 3)	# 21-23	 **attackbox here**

@State
def CmnActUkemiAirN():
    sprite('Action_032_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_032_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_032_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_032_03', 4)	# 13-16	 **attackbox here**
    sprite('Action_032_04', 4)	# 17-20	 **attackbox here**
    sprite('Action_032_05', 3)	# 21-23	 **attackbox here**
    sprite('Action_032_06', 3)	# 24-26	 **attackbox here**
    sprite('Action_032_07', 3)	# 27-29	 **attackbox here**

@State
def CmnActUkemiLandF():
    sprite('Action_041_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_041_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_041_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_041_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_041_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_041_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_041_06', 2)	# 13-14	 **attackbox here**
    sprite('Action_041_07', 2)	# 15-16	 **attackbox here**

@State
def CmnActUkemiLandB():
    sprite('Action_041_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_041_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_041_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_041_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_041_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_041_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_041_06', 2)	# 13-14	 **attackbox here**
    sprite('Action_041_07', 2)	# 15-16	 **attackbox here**

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_041_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_041_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_041_03', 2)	# 9-10	 **attackbox here**
    sprite('Action_041_04', 2)	# 11-12	 **attackbox here**
    sprite('Action_041_05', 3)	# 13-15	 **attackbox here**
    sprite('Action_041_06', 3)	# 16-18	 **attackbox here**
    sprite('Action_041_07', 3)	# 19-21	 **attackbox here**
    sprite('Action_041_08', 3)	# 22-24	 **attackbox here**
    sprite('Action_041_09', 3)	# 25-27	 **attackbox here**
    sprite('Action_041_10', 3)	# 28-30	 **attackbox here**
    sprite('Action_041_11', 20)	# 31-50	 **attackbox here**

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_12', 6)	# 1-6	 **attackbox here**
    sprite('Action_041_13', 9)	# 7-15	 **attackbox here**

@State
def CmnActMidGuardPre():
    sprite('Action_017_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_05', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('Action_017_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_017_01', 5)	# 6-10	 **attackbox here**
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('Action_017_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('Action_017_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_017_01', 5)	# 6-10	 **attackbox here**
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('Action_017_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighGuardPre():
    sprite('Action_017_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_05', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('Action_017_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_017_01', 5)	# 6-10	 **attackbox here**
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('Action_017_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighHeavyGuardLoop():
    sprite('Action_017_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_017_01', 5)	# 6-10	 **attackbox here**

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchGuardPre():
    sprite('Action_018_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_05', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('Action_018_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_018_01', 5)	# 6-10	 **attackbox here**
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('Action_018_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('Action_018_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_018_01', 5)	# 6-10	 **attackbox here**

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirGuardPre():
    sprite('Action_019_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_05', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('Action_019_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_01', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('Action_019_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('Action_019_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_01', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('Action_019_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActGuardBreakStand():
    sprite('Action_017_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_017_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_017_00', 1)	# 5-5	 **attackbox here**
    Unknown2042(1)
    sprite('Action_017_05', 6)	# 6-11	 **attackbox here**
    sprite('Action_017_06', 6)	# 12-17	 **attackbox here**

@State
def CmnActGuardBreakCrouch():
    sprite('Action_018_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_018_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_018_00', 1)	# 5-5	 **attackbox here**
    Unknown2042(1)
    sprite('Action_018_01', 6)	# 6-11	 **attackbox here**
    sprite('Action_018_00', 6)	# 12-17	 **attackbox here**

@State
def CmnActGuardBreakAir():
    sprite('Action_019_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_019_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_019_00', 1)	# 5-5	 **attackbox here**
    Unknown2042(1)
    sprite('Action_019_01', 6)	# 6-11	 **attackbox here**
    sprite('Action_019_00', 6)	# 12-17	 **attackbox here**

@State
def CmnActAirTurn():
    sprite('Action_035_01', 9)	# 1-9	 **attackbox here**

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActLockReject():
    sprite('Action_402_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_402_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_402_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_402_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_402_04', 3)	# 9-11	 **attackbox here**
    sprite('Action_402_05', 5)	# 12-16	 **attackbox here**
    sprite('Action_402_06', 4)	# 17-20	 **attackbox here**
    sprite('Action_402_07', 3)	# 21-23	 **attackbox here**
    sprite('Action_402_08', 3)	# 24-26	 **attackbox here**

@State
def CmnActAirLockWait():
    sprite('Action_019_02', 1)	# 1-1	 **attackbox here**
    sprite('Action_019_03', 3)	# 2-4	 **attackbox here**
    sprite('Action_019_00', 3)	# 5-7	 **attackbox here**

@State
def CmnActLandSpin():
    sprite('Action_000_00', 4)	# 1-4	 **attackbox here**

@State
def CmnActLandSpinDown():
    sprite('Action_000_00', 4)	# 1-4	 **attackbox here**

@State
def CmnActVertSpin():
    sprite('Action_000_00', 4)	# 1-4	 **attackbox here**

@State
def CmnActSlideAir():
    label(0)
    sprite('Action_333_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_333_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_333_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_333_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_333_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_333_05', 2)	# 11-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('Action_351_00', 1)	# 1-1	 **attackbox here**
    label(0)
    sprite('Action_351_01', 3)	# 2-4	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('Action_351_02', 3)	# 1-3	 **attackbox here**
    sprite('Action_351_03', 2)	# 4-5	 **attackbox here**
    sprite('Action_351_04', 2)	# 6-7	 **attackbox here**
    sprite('Action_351_05', 2)	# 8-9	 **attackbox here**

@State
def CmnActAomukeSlideKeep():
    sprite('Action_351_04', 1)	# 1-1	 **attackbox here**
    label(0)
    sprite('Action_351_04', 3)	# 2-4	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('Action_351_02', 3)	# 1-3	 **attackbox here**
    sprite('Action_351_03', 2)	# 4-5	 **attackbox here**
    sprite('Action_351_04', 2)	# 6-7	 **attackbox here**
    sprite('Action_351_05', 2)	# 8-9	 **attackbox here**

@State
def CmnActBurstBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_01', 5)	# 5-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('Action_262_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_262_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirBurstBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_01', 5)	# 5-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    label(0)
    sprite('Action_262_07', 4)	# 1-4	 **attackbox here**
    sprite('Action_262_08', 4)	# 5-8	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771	 **attackbox here**
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('Action_262_05', 6)	# 1-6	 **attackbox here**
    sprite('Action_262_06', 6)	# 7-12	 **attackbox here**

@State
def CmnActAirOverDriveBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771	 **attackbox here**
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('Action_262_07', 6)	# 1-6	 **attackbox here**
    sprite('Action_262_08', 6)	# 7-12	 **attackbox here**
    label(0)
    sprite('Action_262_09', 3)	# 13-15	 **attackbox here**
    sprite('Action_262_10', 3)	# 16-18	 **attackbox here**
    sprite('Action_262_11', 3)	# 19-21	 **attackbox here**
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771	 **attackbox here**
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('Action_262_05', 6)	# 1-6	 **attackbox here**
    sprite('Action_262_06', 6)	# 7-12	 **attackbox here**

@State
def CmnActAirCrossRushBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771	 **attackbox here**
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('Action_262_07', 6)	# 1-6	 **attackbox here**
    sprite('Action_262_08', 6)	# 7-12	 **attackbox here**
    label(0)
    sprite('Action_262_09', 3)	# 13-15	 **attackbox here**
    sprite('Action_262_10', 3)	# 16-18	 **attackbox here**
    sprite('Action_262_11', 3)	# 19-21	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_01', 5)	# 5-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('Action_262_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_262_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirCrossChangeBegin():
    sprite('Action_262_00', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_01', 5)	# 5-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('Action_262_02', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_262_03', 5)	# 5-9	 **attackbox here**
    sprite('Action_262_04', 5)	# 10-14	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('Action_262_07', 3)	# 1-3	 **attackbox here**
    sprite('Action_262_08', 3)	# 4-6	 **attackbox here**
    label(0)
    sprite('Action_262_09', 3)	# 7-9	 **attackbox here**
    sprite('Action_262_10', 3)	# 10-12	 **attackbox here**
    sprite('Action_262_11', 3)	# 13-15	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Unknown9016(1)
        AirPushbackY(12000)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_001_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_001_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_001_02', 2)	# 6-7	 **attackbox here**
    Unknown7009(0)
    SFX_3('SE041')
    sprite('Action_001_03', 3)	# 8-10	 **attackbox here**
    sprite('Action_001_04', 4)	# 11-14	 **attackbox here**
    Unknown2063()
    sprite('Action_001_05', 4)	# 15-18	 **attackbox here**
    sprite('Action_001_06', 4)	# 19-22	 **attackbox here**
    sprite('Action_001_07', 3)	# 23-25	 **attackbox here**

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        Unknown11092(1)
        PushbackX(12000)
        AirPushbackX(3000)
        AirPushbackY(15000)
        Hitstop(2)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_002_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_002_01', 1)	# 2-2	 **attackbox here**
    sprite('Action_002_02', 2)	# 3-4	 **attackbox here**
    sprite('Action_002_03', 2)	# 5-6	 **attackbox here**
    sprite('Action_002_04', 2)	# 7-8	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    sprite('Action_002_05', 2)	# 9-10	 **attackbox here**
    sprite('Action_002_06', 2)	# 11-12	 **attackbox here**
    Unknown14070('AN_NmlAtk5A_3rd')
    tag_voice(1, 'uva103_0', 'uva103_1', 'uva103_2', '')
    sprite('Action_234_00', 2)	# 13-14	 **attackbox here**
    sprite('Action_234_01', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_SwingLightSword')
    sprite('Action_234_02', 2)	# 17-18	 **attackbox here**
    StartMultihit()
    sprite('Action_234_03', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    Hitstop(11)

    def upon_ON_HIT_OR_BLOCK():
        Unknown14072('AN_NmlAtk5A_3rd')
        HitJumpCancel(1)
    sprite('Action_234_04', 3)	# 21-23	 **attackbox here**
    SFX_3('SE045')
    Unknown2063()
    sprite('Action_234_05', 4)	# 24-27	 **attackbox here**
    sprite('Action_234_06', 4)	# 28-31	 **attackbox here**
    Unknown14074('AN_NmlAtk5A_3rd')
    sprite('Action_234_07', 4)	# 32-35	 **attackbox here**
    sprite('Action_234_08', 5)	# 36-40	 **attackbox here**
    sprite('Action_234_09', 5)	# 41-45	 **attackbox here**

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(15000)
        AirPushbackY(15000)
        Unknown9016(1)
        HitOrBlockCancel('AN_NmlAtk5A_4th')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
    sprite('Action_003_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_003_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_003_02', 3)	# 5-7	 **attackbox here**
    tag_voice(1, 'uva104_0', 'uva104_1', 'uva104_2', '')
    sprite('Action_003_03', 4)	# 8-11	 **attackbox here**
    sprite('Action_003_04', 2)	# 12-13	 **attackbox here**
    SFX_3('SE043')
    sprite('Action_003_05', 3)	# 14-16	 **attackbox here**
    Unknown2063()
    sprite('Action_003_06', 4)	# 17-20	 **attackbox here**
    sprite('Action_003_07', 5)	# 21-25	 **attackbox here**
    sprite('Action_003_08', 4)	# 26-29	 **attackbox here**
    sprite('Action_003_09', 4)	# 30-33	 **attackbox here**
    sprite('Action_003_10', 5)	# 34-38	 **attackbox here**

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown11033(1)
        Damage(800)
        AirPushbackY(8000)
        AirUntechableTime(60)
        Hitstop(2)
        PushbackX(12000)
        Unknown9266(14)
        Unknown11056(0)
        JumpCancel_(0)
    sprite('Action_237_00', 3)	# 1-3	 **attackbox here**
    physicsXImpulse(13000)
    sprite('Action_237_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_237_02', 3)	# 7-9	 **attackbox here**
    tag_voice(1, 'uva109_0', 'uva109_1', 'uva109_2', '')
    sprite('Action_237_03', 3)	# 10-12	 **attackbox here**
    physicsXImpulse(8000)
    GFX_0('Vat_238', -1)
    RefreshMultihit()
    sprite('Action_237_19', 3)	# 13-15	 **attackbox here**
    sprite('Action_237_20', 2)	# 16-17	 **attackbox here**
    GFX_0('Vat_238', -1)
    RefreshMultihit()
    sprite('Action_237_05', 2)	# 18-19	 **attackbox here**
    sprite('Action_237_06', 4)	# 20-23	 **attackbox here**
    sprite('Action_237_07', 5)	# 24-28	 **attackbox here**
    sprite('Action_237_08', 2)	# 29-30	 **attackbox here**
    sprite('Action_237_09', 2)	# 31-32	 **attackbox here**
    sprite('Action_237_10', 2)	# 33-34	 **attackbox here**
    GFX_0('Vat_250', -1)
    GFX_0('Vat_251', -1)
    RefreshMultihit()
    sprite('Action_237_11', 2)	# 35-36	 **attackbox here**
    sprite('Action_237_12', 3)	# 37-39	 **attackbox here**
    GFX_0('Vat_250', -1)
    GFX_0('Vat_251', -1)
    RefreshMultihit()
    sprite('Action_237_13', 2)	# 40-41	 **attackbox here**
    sprite('Action_237_14', 7)	# 42-48	 **attackbox here**
    GFX_0('Vat_240', -1)
    physicsXImpulse(-5000)
    RefreshMultihit()
    AirPushbackX(20000)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    sprite('Action_237_15', 10)	# 49-58	 **attackbox here**
    Unknown1019(5)
    sprite('Action_237_16', 7)	# 59-65	 **attackbox here**
    sprite('Action_237_17', 7)	# 66-72	 **attackbox here**

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        AirPushbackY(15000)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5B_2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
    sprite('Action_045_01', 3)	# 1-3	 **attackbox here**
    physicsXImpulse(20000)
    Unknown1028(-1000)
    sprite('Action_402_00', 4)	# 4-7	 **attackbox here**
    GFX_0('Vat_073', -1)
    tag_voice(1, 'uva104_0', 'uva104_1', 'uva104_2', '')
    SFX_3('SE043')
    sprite('Action_402_01', 3)	# 8-10	 **attackbox here**
    sprite('Action_402_02', 2)	# 11-12	 **attackbox here**
    sprite('Action_402_03', 2)	# 13-14	 **attackbox here**
    sprite('Action_402_04', 4)	# 15-18	 **attackbox here**
    Unknown2063()
    sprite('Action_402_05', 4)	# 19-22	 **attackbox here**
    sprite('Action_402_06', 4)	# 23-26	 **attackbox here**
    Unknown1084(1)
    sprite('Action_402_07', 4)	# 27-30	 **attackbox here**
    sprite('Action_402_08', 4)	# 31-34	 **attackbox here**

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(350)
        Hitstop(4)
        PushbackX(19800)
        AirPushbackX(15000)
        AirPushbackY(6000)
        Unknown9016(1)
        Unknown11092(1)
        Unknown11057(800)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1
    sprite('Action_045_01', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(15000)
    Unknown1019(110)
    sprite('Action_403_00', 4)	# 3-6	 **attackbox here**
    sprite('Action_403_01', 4)	# 7-10	 **attackbox here**
    tag_voice(1, 'uva108_0', 'uva108_1', 'uva108_2', '')
    sprite('Action_403_02', 3)	# 11-13
    SFX_3('SE_SwingLightSword')
    GFX_0('Vat_191', -1)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(23000)
    Unknown1007(23000)
    Unknown1072(-9500)
    Unknown35()
    sprite('Action_403_03', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_403_04', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_05', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    Unknown14070('NmlAtk5A')
    Unknown14070('NmlAtk2A')
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk2B')
    Unknown14070('NmlAtk2C')
    Unknown14070('CmnActCrushAttack')
    sprite('Action_403_06', 3)	# 23-25	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_07', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_08', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()
    Unknown1019(20)
    if SLOT_51:
        HitJumpCancel(1)
        Unknown14072('NmlAtk5A')
        Unknown14072('NmlAtk2A')
        Unknown14072('NmlAtk5B')
        Unknown14072('NmlAtk2B')
        Unknown14072('NmlAtk2C')
        Unknown14072('CmnActCrushAttack')
    sprite('Action_403_09', 3)	# 32-34
    Unknown2063()
    sprite('Action_404_00', 4)	# 35-38	 **attackbox here**
    Unknown13(4)
    sprite('Action_404_01', 4)	# 39-42	 **attackbox here**
    sprite('Action_404_02', 4)	# 43-46	 **attackbox here**
    Unknown14074('NmlAtk5A')
    Unknown14074('NmlAtk2A')
    Unknown14074('NmlAtk5B')
    Unknown14074('NmlAtk2B')
    Unknown14074('NmlAtk2C')
    Unknown14074('CmnActCrushAttack')
    sprite('Action_404_03', 4)	# 47-50	 **attackbox here**
    sprite('Action_404_04', 4)	# 51-54	 **attackbox here**
    Unknown1084(1)

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_004_01', 3)	# 2-4	 **attackbox here**
    sprite('Action_004_02', 3)	# 5-7	 **attackbox here**
    Unknown7009(0)
    SFX_3('SE041')
    sprite('Action_004_03', 3)	# 8-10	 **attackbox here**
    sprite('Action_004_04', 1)	# 11-11	 **attackbox here**
    Unknown2063()
    sprite('Action_004_04', 1)	# 12-12	 **attackbox here**
    sprite('Action_004_04', 1)	# 13-13	 **attackbox here**
    sprite('Action_004_05', 3)	# 14-16	 **attackbox here**
    sprite('Action_004_06', 3)	# 17-19	 **attackbox here**
    sprite('Action_004_07', 3)	# 20-22	 **attackbox here**
    sprite('Action_004_08', 3)	# 23-25	 **attackbox here**

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_004_01', 3)	# 2-4	 **attackbox here**
    sprite('Action_004_02', 3)	# 5-7	 **attackbox here**
    Unknown7009(0)
    SFX_3('SE041')
    sprite('Action_004_03', 3)	# 8-10	 **attackbox here**
    sprite('Action_004_04', 1)	# 11-11	 **attackbox here**
    Unknown2063()
    sprite('Action_004_04', 1)	# 12-12	 **attackbox here**
    sprite('Action_004_04', 1)	# 13-13	 **attackbox here**
    sprite('Action_004_05', 3)	# 14-16	 **attackbox here**
    sprite('Action_004_06', 3)	# 17-19	 **attackbox here**
    sprite('Action_004_07', 3)	# 20-22	 **attackbox here**
    sprite('Action_004_08', 3)	# 23-25	 **attackbox here**

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(600)
        Unknown11092(1)
        PushbackX(12000)
        AirPushbackX(3000)
        AirPushbackY(15000)
        Hitstop(2)
        Unknown9016(1)
        HitLow(0)
        AirUntechableTime(20)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('Action_005_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_005_01', 4)	# 4-7	 **attackbox here**
    sprite('Action_005_02', 2)	# 8-9	 **attackbox here**
    tag_voice(1, 'uva103_0', 'uva103_1', 'uva103_2', '')
    SFX_3('SE_SwingLightSword')
    sprite('Action_005_03', 2)	# 10-11	 **attackbox here**
    sprite('Action_235_00', 2)	# 12-13	 **attackbox here**
    sprite('Action_235_01', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_SwingLightSword')
    sprite('Action_235_02', 2)	# 16-17	 **attackbox here**
    StartMultihit()
    sprite('Action_235_03', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    Hitstop(11)

    def upon_ON_HIT_OR_BLOCK():
        HitJumpCancel(1)
    sprite('Action_235_04', 3)	# 20-22	 **attackbox here**
    SFX_3('SE045')
    Unknown2063()
    sprite('Action_235_05', 4)	# 23-26	 **attackbox here**
    sprite('Action_235_06', 4)	# 27-30	 **attackbox here**
    sprite('Action_235_07', 4)	# 31-34	 **attackbox here**
    sprite('Action_235_08', 5)	# 35-39	 **attackbox here**
    sprite('Action_235_09', 5)	# 40-44	 **attackbox here**

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Unknown11033(1)
        Damage(1100)
        AttackP1(90)
        AttackP2(75)
        Unknown11092(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        PushbackX(12000)
        AirPushbackY(15000)
        AirUntechableTime(30)
        Hitstop(8)
        HitLow(2)
        Unknown9266(14)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitJumpCancel(1)
    sprite('Action_231_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_231_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_231_02', 5)	# 9-13	 **attackbox here**
    tag_voice(1, 'uva110_0', 'uva305_0', 'uva305_1', '')
    sprite('Action_231_03', 2)	# 14-15	 **attackbox here**
    GFX_0('Vat_242', -1)
    sprite('Action_231_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_231_05', 4)	# 19-22	 **attackbox here**
    sprite('Action_231_06', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    GFX_0('Vat_242_2', -1)
    sprite('Action_231_07', 3)	# 25-27	 **attackbox here**
    sprite('Action_231_08', 3)	# 28-30	 **attackbox here**
    sprite('Action_231_09', 4)	# 31-34	 **attackbox here**
    sprite('Action_231_10', 8)	# 35-42	 **attackbox here**
    sprite('Action_231_11', 5)	# 43-47	 **attackbox here**
    sprite('Action_231_12', 3)	# 48-50	 **attackbox here**
    sprite('Action_231_13', 3)	# 51-53	 **attackbox here**

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        Unknown9016(1)
        HitOrBlockCancel('AN_NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_008_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_008_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_008_02', 3)	# 6-8	 **attackbox here**
    GFX_0('Vat_074', -1)
    SFX_3('SE042')
    sprite('Action_008_03', 6)	# 9-14	 **attackbox here**
    tag_voice(1, 'uva101_0', 'uva101_1', 'uva101_2', '')
    sprite('Action_008_04', 5)	# 15-19	 **attackbox here**
    Unknown2063()
    sprite('Action_008_05', 6)	# 20-25	 **attackbox here**
    sprite('Action_008_06', 7)	# 26-32	 **attackbox here**

@State
def AN_NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_007_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_007_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_007_02', 4)	# 7-10	 **attackbox here**
    sprite('Action_007_03', 4)	# 11-14	 **attackbox here**
    sprite('Action_007_04', 5)	# 15-19	 **attackbox here**
    sprite('Action_007_05', 5)	# 20-24	 **attackbox here**
    sprite('Action_007_06', 5)	# 25-29	 **attackbox here**
    sprite('Action_007_07', 5)	# 30-34	 **attackbox here**

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(500)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackY(20000)
        AirUntechableTime(19)
        Hitstop(4)
        Unknown9016(1)
        HitOverhead(0)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_009_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_009_01', 5)	# 5-9	 **attackbox here**
    tag_voice(1, 'uva105_0', 'uva105_1', 'uva105_2', '')
    SFX_3('SE_SwingLightSword')
    sprite('Action_009_02', 3)	# 10-12
    GFX_0('Vat_191', -1)
    Unknown36(1)
    teleportRelativeX(23000)
    Unknown1007(23000)
    Unknown1072(-10000)
    Unknown35()
    sprite('Action_009_03', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_009_04', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_009_05', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('Action_009_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_009_07', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_009_08', 2)	# 23-24
    Unknown2063()
    sprite('Action_009_09', 3)	# 25-27	 **attackbox here**
    Unknown26('Vat_191')
    sprite('Action_009_10', 3)	# 28-30	 **attackbox here**

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(750)
        AttackP1(80)
        AttackP2(70)
        Unknown11092(1)
        AirHitstunAnimation(9)
        Hitstop(4)
        PushbackX(6000)
        AirPushbackX(35000)
        AirPushbackY(-40000)
        YImpluseBeforeWallbounce(2500)
        Unknown9154(22)
        AirUntechableTime(30)
        Unknown9310(10)
        HitOverhead(2)
        Unknown9016(1)
        Unknown11056(0)
        JumpCancel_(0)

        def upon_77():
            Unknown2037(1)

        def upon_3():
            if SLOT_2:
                clearUponHandler(3)
                HitOverhead(0)
    sprite('Action_161_00', 8)	# 1-8	 **attackbox here**
    clearUponHandler(2)
    Unknown1084(1)
    physicsXImpulse(2500)
    physicsYImpulse(-2500)
    sprite('Action_161_01', 9)	# 9-17	 **attackbox here**
    tag_voice(1, 'uva210_0', 'uva210_1', 'uva210_2', '')
    sprite('Action_161_02', 2)	# 18-19	 **attackbox here**
    physicsXImpulse(36000)
    physicsYImpulse(-48000)
    Unknown1028(300)
    setGravity(400)
    GFX_0('Vat_077', 0)
    SFX_3('SE038')
    sendToLabelUpon(2, 9)
    label(0)
    sprite('Action_161_03', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    sprite('Action_161_04', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('Action_161_05', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    sprite('Action_161_06', 2)	# 26-27	 **attackbox here**
    RefreshMultihit()
    sprite('Action_161_07', 2)	# 28-29	 **attackbox here**
    RefreshMultihit()
    sprite('Action_161_08', 2)	# 30-31	 **attackbox here**
    gotoLabel(0)
    label(9)
    sprite('Action_161_09', 2)	# 32-33	 **attackbox here**
    RefreshMultihit()
    Unknown8000(100, 1, 1)
    Unknown2006()
    Unknown1084(1)
    physicsXImpulse(5000)
    Unknown1028(-200)
    Unknown26('Vat_077')

    def upon_45():
        if CheckInput(0x13):
            SLOT_51 = 1
    sprite('Action_161_10', 3)	# 34-36	 **attackbox here**
    sprite('Action_161_11', 3)	# 37-39	 **attackbox here**
    if SLOT_51:
        _gotolabel(10)
    sprite('Action_160_12', 3)	# 40-42	 **attackbox here**
    sprite('Action_160_13', 3)	# 43-45	 **attackbox here**
    sprite('Action_160_14', 3)	# 46-48	 **attackbox here**
    sprite('Action_160_15', 3)	# 49-51	 **attackbox here**
    sprite('Action_160_16', 2)	# 52-53	 **attackbox here**
    ExitState()
    label(10)
    sprite('Action_161_11', 1)	# 54-54	 **attackbox here**
    sprite('Action_161_12', 4)	# 55-58	 **attackbox here**
    Unknown8010(100, 1, 0)
    sprite('Action_161_13', 3)	# 59-61	 **attackbox here**
    sprite('Action_161_14', 2)	# 62-63	 **attackbox here**
    SFX_3('SE043')
    sprite('Action_161_15', 6)	# 64-69	 **attackbox here**
    RefreshMultihit()
    Damage(1500)
    AirUntechableTime(60)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(10000)
    YImpluseBeforeWallbounce(500)
    Unknown11028(13)
    WallbounceReboundTime(0)
    Unknown9310(0)
    Hitstop(11)
    HitOverhead(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown1084(1)
    Unknown23159('NmlAtkAIR5C_Hold')
    sprite('Action_161_16', 5)	# 70-74	 **attackbox here**
    Unknown2063()
    sprite('Action_161_17', 5)	# 75-79	 **attackbox here**
    sprite('Action_161_18', 5)	# 80-84	 **attackbox here**
    sprite('Action_161_19', 5)	# 85-89	 **attackbox here**

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_068_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_068_02', 3)	# 5-7	 **attackbox here**
    Unknown1084(1)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    physicsYImpulse(23000)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_068_03', 3)	# 8-10	 **attackbox here**
    tag_voice(1, 'uva156_0', 'uva156_1', '', '')
    sprite('Action_068_04', 3)	# 11-13	 **attackbox here**
    sprite('Action_068_05', 3)	# 14-16	 **attackbox here**
    sprite('Action_068_06', 2)	# 17-18	 **attackbox here**
    sprite('Action_008_00', 2)	# 19-20	 **attackbox here**
    sprite('Action_008_01', 3)	# 21-23	 **attackbox here**
    sprite('Action_008_02', 2)	# 24-25	 **attackbox here**
    GFX_0('Vat_074', -1)
    SFX_3('SE042')
    sprite('Action_008_03', 3)	# 26-28	 **attackbox here**
    sprite('Action_008_04', 5)	# 29-33	 **attackbox here**
    sprite('Action_008_05', 6)	# 34-39	 **attackbox here**
    sprite('Action_008_06', 7)	# 40-46	 **attackbox here**
    label(0)
    sprite('Action_035_08', 3)	# 47-49	 **attackbox here**
    sprite('Action_035_09', 3)	# 50-52	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    Unknown1084(1)
    sprite('Action_037_12', 3)	# 53-55	 **attackbox here**
    sprite('Action_037_13', 5)	# 56-60	 **attackbox here**
    sprite('Action_037_14', 5)	# 61-65	 **attackbox here**

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 18)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_008_04', 5)	# 1-5	 **attackbox here**
    sprite('Action_008_05', 6)	# 6-11	 **attackbox here**
    sprite('Action_008_06', 7)	# 12-18	 **attackbox here**
    label(0)
    sprite('Action_035_08', 3)	# 19-21	 **attackbox here**
    sprite('Action_035_09', 3)	# 22-24	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    Unknown1084(1)
    sprite('Action_037_12', 3)	# 25-27	 **attackbox here**
    sprite('Action_037_13', 6)	# 28-33	 **attackbox here**
    sprite('Action_037_14', 6)	# 34-39	 **attackbox here**
    label(2)
    sprite('Action_002_00', 1)	# 40-40	 **attackbox here**
    sprite('Action_002_01', 1)	# 41-41	 **attackbox here**
    sprite('Action_002_02', 2)	# 42-43	 **attackbox here**
    tag_voice(1, 'uva157_0', 'uva157_1', '', '')
    sprite('Action_002_03', 2)	# 44-45	 **attackbox here**
    sprite('Action_002_04', 2)	# 46-47	 **attackbox here**
    sprite('Action_002_05', 3)	# 48-50	 **attackbox here**
    SFX_3('SE_SwingLightSword')
    sprite('Action_002_06', 3)	# 51-53	 **attackbox here**
    sprite('Action_002_07', 3)	# 54-56	 **attackbox here**
    sprite('Action_002_08', 3)	# 57-59	 **attackbox here**
    sprite('Action_002_09', 2)	# 60-61	 **attackbox here**
    sprite('Action_002_10', 4)	# 62-65	 **attackbox here**
    sprite('Action_002_11', 3)	# 66-68	 **attackbox here**
    sprite('Action_002_12', 4)	# 69-72	 **attackbox here**
    sprite('Action_002_13', 5)	# 73-77	 **attackbox here**
    sprite('Action_000_00', 1)	# 78-78	 **attackbox here**
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    sprite('Action_000_01', 5)	# 79-83	 **attackbox here**
    sprite('Action_000_02', 5)	# 84-88	 **attackbox here**
    sprite('Action_000_03', 5)	# 89-93	 **attackbox here**
    sprite('Action_000_04', 5)	# 94-98	 **attackbox here**
    sprite('Action_000_05', 5)	# 99-103	 **attackbox here**
    sprite('Action_000_06', 5)	# 104-108	 **attackbox here**
    sprite('Action_000_07', 5)	# 109-113	 **attackbox here**
    sprite('Action_000_08', 5)	# 114-118	 **attackbox here**
    sprite('Action_000_09', 5)	# 119-123	 **attackbox here**
    sprite('Action_000_10', 5)	# 124-128	 **attackbox here**
    sprite('Action_000_11', 5)	# 129-133	 **attackbox here**
    loopRest()
    label(10)
    sprite('Action_000_01', 5)	# 134-138	 **attackbox here**
    sprite('Action_000_02', 5)	# 139-143	 **attackbox here**
    sprite('Action_000_03', 5)	# 144-148	 **attackbox here**
    sprite('Action_000_04', 5)	# 149-153	 **attackbox here**
    sprite('Action_000_05', 5)	# 154-158	 **attackbox here**
    sprite('Action_000_06', 5)	# 159-163	 **attackbox here**
    sprite('Action_000_07', 5)	# 164-168	 **attackbox here**
    sprite('Action_000_08', 5)	# 169-173	 **attackbox here**
    sprite('Action_000_09', 5)	# 174-178	 **attackbox here**
    sprite('Action_000_10', 5)	# 179-183	 **attackbox here**
    sprite('Action_000_11', 5)	# 184-188	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 189-189

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_045_01', 5)	# 1-5	 **attackbox here**
    sprite('Action_402_00', 4)	# 6-9	 **attackbox here**
    GFX_0('Vat_073', -1)
    SFX_3('SE043')
    sprite('Action_402_01', 3)	# 10-12	 **attackbox here**
    sprite('Action_402_02', 2)	# 13-14	 **attackbox here**
    sprite('Action_402_03', 2)	# 15-16	 **attackbox here**
    sprite('Action_402_04', 3)	# 17-19	 **attackbox here**
    sprite('Action_402_05', 3)	# 20-22	 **attackbox here**
    sprite('Action_402_06', 3)	# 23-25	 **attackbox here**
    sprite('Action_402_07', 3)	# 26-28	 **attackbox here**
    sprite('Action_402_08', 3)	# 29-31	 **attackbox here**
    sprite('Action_000_01', 5)	# 32-36	 **attackbox here**
    sprite('Action_000_02', 5)	# 37-41	 **attackbox here**
    sprite('Action_000_03', 5)	# 42-46	 **attackbox here**
    sprite('Action_000_04', 5)	# 47-51	 **attackbox here**
    sprite('Action_000_05', 5)	# 52-56	 **attackbox here**
    sprite('Action_000_06', 5)	# 57-61	 **attackbox here**
    sprite('Action_000_07', 5)	# 62-66	 **attackbox here**
    sprite('Action_000_08', 5)	# 67-71	 **attackbox here**
    sprite('Action_000_09', 5)	# 72-76	 **attackbox here**
    sprite('Action_000_10', 5)	# 77-81	 **attackbox here**
    sprite('Action_000_11', 5)	# 82-86	 **attackbox here**
    loopRest()
    label(10)
    sprite('Action_000_01', 5)	# 87-91	 **attackbox here**
    sprite('Action_000_02', 5)	# 92-96	 **attackbox here**
    sprite('Action_000_03', 5)	# 97-101	 **attackbox here**
    sprite('Action_000_04', 5)	# 102-106	 **attackbox here**
    sprite('Action_000_05', 5)	# 107-111	 **attackbox here**
    sprite('Action_000_06', 5)	# 112-116	 **attackbox here**
    sprite('Action_000_07', 5)	# 117-121	 **attackbox here**
    sprite('Action_000_08', 5)	# 122-126	 **attackbox here**
    sprite('Action_000_09', 5)	# 127-131	 **attackbox here**
    sprite('Action_000_10', 5)	# 132-136	 **attackbox here**
    sprite('Action_000_11', 5)	# 137-141	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('keep', 1)	# 142-142

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        sendToLabelUpon(2, 1)
        Unknown11032('ffffffffffffffff00093d00c0f2fcff')
        Unknown23027()
    sprite('Action_000_01', 4)	# 1-4	 **attackbox here**
    sprite('Action_000_02', 4)	# 5-8	 **attackbox here**
    sprite('Action_130_00', 3)	# 9-11	 **attackbox here**
    tag_voice(1, 'uva158_0', 'uva158_1', '', '')
    sprite('Action_130_01', 3)	# 12-14	 **attackbox here**
    sprite('Action_130_02', 3)	# 15-17	 **attackbox here**
    physicsXImpulse(-3000)
    physicsYImpulse(25000)
    setGravity(2000)
    Unknown1021(200)
    Unknown8001(1, 0)
    sprite('Action_130_03', 2)	# 18-19	 **attackbox here**
    sprite('Action_130_04', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_130_05', 3)	# 23-25	 **attackbox here**
    sprite('Action_130_06', 3)	# 26-28	 **attackbox here**
    sprite('Action_130_07', 3)	# 29-31	 **attackbox here**
    sprite('Action_130_08', 3)	# 32-34	 **attackbox here**
    sprite('Action_130_09', 3)	# 35-37	 **attackbox here**
    sprite('Action_130_10', 3)	# 38-40	 **attackbox here**
    sprite('Action_130_11', 3)	# 41-43	 **attackbox here**
    sprite('Action_130_12', 3)	# 44-46	 **attackbox here**
    loopRest()
    label(1)
    sprite('Action_130_13', 3)	# 47-49	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_130_14', 6)	# 50-55	 **attackbox here**
    sprite('Action_130_15', 8)	# 56-63	 **attackbox here**

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
        sendToLabelUpon(2, 1)
        Unknown23027()
    sprite('null', 24)	# 1-24
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 25-25
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('Action_161_00', 9)	# 26-34	 **attackbox here**
    physicsXImpulse(46000)
    physicsYImpulse(-15000)
    setGravity(2500)
    sprite('Action_161_01', 10)	# 35-44	 **attackbox here**
    label(0)
    sprite('Action_161_02', 1)	# 45-45	 **attackbox here**
    sprite('Action_161_03', 1)	# 46-46	 **attackbox here**
    sprite('Action_161_04', 1)	# 47-47	 **attackbox here**
    sprite('Action_161_05', 1)	# 48-48	 **attackbox here**
    sprite('Action_161_06', 1)	# 49-49	 **attackbox here**
    sprite('Action_161_07', 1)	# 50-50	 **attackbox here**
    sprite('Action_161_08', 1)	# 51-51	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_161_09', 5)	# 52-56	 **attackbox here**
    Unknown1084(1)
    RefreshMultihit()
    sprite('Action_161_10', 6)	# 57-62	 **attackbox here**
    sprite('Action_161_11', 6)	# 63-68	 **attackbox here**
    sprite('Action_161_12', 6)	# 69-74	 **attackbox here**
    sprite('Action_000_01', 5)	# 75-79	 **attackbox here**
    sprite('Action_000_02', 5)	# 80-84	 **attackbox here**
    sprite('Action_000_03', 5)	# 85-89	 **attackbox here**
    sprite('Action_000_04', 5)	# 90-94	 **attackbox here**
    sprite('Action_000_05', 5)	# 95-99	 **attackbox here**
    sprite('Action_000_06', 5)	# 100-104	 **attackbox here**
    sprite('Action_000_07', 5)	# 105-109	 **attackbox here**
    sprite('Action_000_08', 5)	# 110-114	 **attackbox here**
    sprite('Action_000_09', 5)	# 115-119	 **attackbox here**
    sprite('Action_000_10', 5)	# 120-124	 **attackbox here**
    sprite('Action_000_11', 5)	# 125-129	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('keep', 4)	# 1-4
    sprite('Action_161_13', 5)	# 5-9	 **attackbox here**
    sprite('Action_161_14', 2)	# 10-11	 **attackbox here**
    sprite('Action_161_15', 6)	# 12-17	 **attackbox here**
    sprite('Action_161_16', 7)	# 18-24	 **attackbox here**
    sprite('Action_161_17', 5)	# 25-29	 **attackbox here**
    sprite('Action_161_18', 5)	# 30-34	 **attackbox here**
    sprite('Action_161_19', 5)	# 35-39	 **attackbox here**
    sprite('Action_000_01', 5)	# 40-44	 **attackbox here**
    sprite('Action_000_02', 5)	# 45-49	 **attackbox here**
    sprite('Action_000_03', 5)	# 50-54	 **attackbox here**
    sprite('Action_000_04', 5)	# 55-59	 **attackbox here**
    sprite('Action_000_05', 5)	# 60-64	 **attackbox here**
    sprite('Action_000_06', 5)	# 65-69	 **attackbox here**
    sprite('Action_000_07', 5)	# 70-74	 **attackbox here**
    sprite('Action_000_08', 5)	# 75-79	 **attackbox here**
    sprite('Action_000_09', 5)	# 80-84	 **attackbox here**
    sprite('Action_000_10', 5)	# 85-89	 **attackbox here**
    sprite('Action_000_11', 5)	# 90-94	 **attackbox here**

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        sendToLabelUpon(2, 1)
        Unknown11032('ffffffffffffffff00093d00c0f2fcff')
        Unknown23027()
    sprite('Action_000_01', 4)	# 1-4	 **attackbox here**
    sprite('Action_000_02', 4)	# 5-8	 **attackbox here**
    sprite('Action_130_00', 3)	# 9-11	 **attackbox here**
    sprite('Action_130_01', 3)	# 12-14	 **attackbox here**
    sprite('Action_130_02', 3)	# 15-17	 **attackbox here**
    physicsXImpulse(-3000)
    physicsYImpulse(25000)
    setGravity(2000)
    Unknown1021(200)
    Unknown8001(1, 0)
    sprite('Action_130_03', 2)	# 18-19	 **attackbox here**
    sprite('Action_130_04', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_130_05', 3)	# 23-25	 **attackbox here**
    sprite('Action_130_06', 3)	# 26-28	 **attackbox here**
    sprite('Action_130_07', 3)	# 29-31	 **attackbox here**
    sprite('Action_130_08', 3)	# 32-34	 **attackbox here**
    sprite('Action_130_09', 3)	# 35-37	 **attackbox here**
    sprite('Action_130_10', 3)	# 38-40	 **attackbox here**
    sprite('Action_130_11', 3)	# 41-43	 **attackbox here**
    sprite('Action_130_12', 3)	# 44-46	 **attackbox here**
    loopRest()
    label(1)
    sprite('Action_130_13', 3)	# 47-49	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_130_14', 6)	# 50-55	 **attackbox here**
    sprite('Action_130_15', 8)	# 56-63	 **attackbox here**

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
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('Action_045_00', 6)	# 1-6	 **attackbox here**
    sprite('Action_045_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_045_02', 3)	# 10-12	 **attackbox here**
    label(0)
    sprite('Action_045_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_045_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_045_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_045_06', 3)	# 22-24	 **attackbox here**
    sprite('Action_045_07', 3)	# 25-27	 **attackbox here**
    sprite('Action_045_08', 3)	# 28-30	 **attackbox here**
    sprite('Action_045_09', 3)	# 31-33	 **attackbox here**
    sprite('Action_045_02', 3)	# 34-36	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 37-37	 **attackbox here**
    clearUponHandler(3)
    Unknown1084(1)
    sprite('Action_055_00', 2)	# 38-39	 **attackbox here**
    SFX_3('SE042')
    sprite('Action_055_01', 3)	# 40-42	 **attackbox here**
    sprite('Action_055_02', 5)	# 43-47	 **attackbox here**
    SFX_1('uva154')
    sprite('Action_055_03', 8)	# 48-55	 **attackbox here**
    sprite('Action_055_04', 4)	# 56-59	 **attackbox here**
    sprite('Action_055_05', 3)	# 60-62	 **attackbox here**
    sprite('Action_055_06', 3)	# 63-65	 **attackbox here**

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AttackP2(50)
        AirPushbackX(80000)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        WallbounceReboundTime(10)
        Hitstop(1)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown9266(14)
    sprite('Action_056_00', 2)	# 1-2	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_056_01', 5)	# 3-7	 **attackbox here**
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_056_02', 7)	# 8-14	 **attackbox here**
    sprite('Action_057_00', 3)	# 15-17	 **attackbox here**
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_01', 4)	# 18-21	 **attackbox here**
    GFX_0('Vat_103', -1)
    SFX_1('uva153')
    sprite('Action_057_02', 4)	# 22-25	 **attackbox here**
    sprite('Action_057_03', 4)	# 26-29	 **attackbox here**
    loopRest()
    sprite('Action_057_04', 6)	# 30-35	 **attackbox here**
    sprite('Action_057_05', 4)	# 36-39	 **attackbox here**
    sprite('Action_057_06', 4)	# 40-43	 **attackbox here**
    sprite('Action_057_07', 3)	# 44-46	 **attackbox here**

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
    sprite('Action_045_00', 6)	# 1-6	 **attackbox here**
    sprite('Action_045_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_045_02', 3)	# 10-12	 **attackbox here**
    label(0)
    sprite('Action_045_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_045_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_045_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_045_06', 3)	# 22-24	 **attackbox here**
    sprite('Action_045_07', 3)	# 25-27	 **attackbox here**
    sprite('Action_045_08', 3)	# 28-30	 **attackbox here**
    sprite('Action_045_09', 3)	# 31-33	 **attackbox here**
    sprite('Action_045_02', 3)	# 34-36	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 37-37	 **attackbox here**
    clearUponHandler(3)
    Unknown1084(1)
    sprite('Action_055_00', 2)	# 38-39	 **attackbox here**
    SFX_3('SE042')
    sprite('Action_055_01', 3)	# 40-42	 **attackbox here**
    sprite('Action_055_02', 5)	# 43-47	 **attackbox here**
    SFX_1('uva154')
    sprite('Action_055_03', 8)	# 48-55	 **attackbox here**
    sprite('Action_055_04', 4)	# 56-59	 **attackbox here**
    sprite('Action_055_05', 3)	# 60-62	 **attackbox here**
    sprite('Action_055_06', 3)	# 63-65	 **attackbox here**

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AttackP2(50)
        AirPushbackX(80000)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        WallbounceReboundTime(10)
        Hitstop(1)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown9266(14)
    sprite('Action_056_00', 2)	# 1-2	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_056_01', 5)	# 3-7	 **attackbox here**
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000008000000')
    sprite('Action_056_02', 7)	# 8-14	 **attackbox here**
    sprite('Action_057_00', 3)	# 15-17	 **attackbox here**
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_01', 4)	# 18-21	 **attackbox here**
    GFX_0('Vat_103', -1)
    SFX_1('uva153')
    sprite('Action_057_02', 4)	# 22-25	 **attackbox here**
    sprite('Action_057_03', 4)	# 26-29	 **attackbox here**
    loopRest()
    sprite('Action_057_04', 6)	# 30-35	 **attackbox here**
    sprite('Action_057_05', 4)	# 36-39	 **attackbox here**
    sprite('Action_057_06', 4)	# 40-43	 **attackbox here**
    sprite('Action_057_07', 3)	# 44-46	 **attackbox here**

@State
def BeamA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 1100):
                sendToLabel(9)
    sprite('Action_120_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_120_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_120_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_120_03', 3)	# 13-15	 **attackbox here**
    GFX_0('Vat_097', -1)
    tag_voice(1, 'uva204_0', 'uva204_1', 'uva204_2', '')
    sprite('Action_120_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_120_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_120_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_120_04', 3)	# 25-27	 **attackbox here**
    sprite('Action_120_05', 3)	# 28-30	 **attackbox here**
    sprite('Action_120_03', 3)	# 31-33	 **attackbox here**
    label(9)
    sprite('keep', 1)	# 34-34
    clearUponHandler(43)
    sprite('Action_120_04', 4)	# 35-38	 **attackbox here**
    sprite('Action_120_05', 4)	# 39-42	 **attackbox here**
    sprite('Action_120_03', 4)	# 43-46	 **attackbox here**
    sprite('Action_120_04', 4)	# 47-50	 **attackbox here**
    sprite('Action_120_05', 4)	# 51-54	 **attackbox here**
    sprite('Action_120_09', 4)	# 55-58	 **attackbox here**
    sprite('Action_120_10', 4)	# 59-62	 **attackbox here**
    sprite('Action_120_11', 4)	# 63-66	 **attackbox here**

@State
def BeamB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 1100):
                sendToLabel(9)
    sprite('Action_121_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_121_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_121_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_121_03', 3)	# 13-15	 **attackbox here**
    GFX_0('Vat_097_B', -1)
    tag_voice(1, 'uva204_0', 'uva204_1', 'uva204_2', '')
    sprite('Action_121_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_121_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_121_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_121_04', 3)	# 25-27	 **attackbox here**
    label(9)
    sprite('keep', 1)	# 28-28
    clearUponHandler(43)
    sprite('Action_121_05', 4)	# 29-32	 **attackbox here**
    sprite('Action_121_03', 4)	# 33-36	 **attackbox here**
    sprite('Action_121_04', 4)	# 37-40	 **attackbox here**
    sprite('Action_121_05', 4)	# 41-44	 **attackbox here**
    sprite('Action_121_03', 4)	# 45-48	 **attackbox here**
    sprite('Action_121_09', 4)	# 49-52	 **attackbox here**
    sprite('Action_121_10', 4)	# 53-56	 **attackbox here**
    sprite('Action_121_11', 4)	# 57-60	 **attackbox here**

@State
def Beam_Ex():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 1100):
                sendToLabel(9)
    sprite('Action_123_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_123_00', 1)	# 4-4	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_123_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_123_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_123_03', 3)	# 13-15	 **attackbox here**
    GFX_0('Vat_083', 0)
    tag_voice(1, 'uva205_0', 'uva205_1', 'uva205_2', '')
    sprite('Action_123_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_123_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_123_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_123_04', 3)	# 25-27	 **attackbox here**
    label(9)
    sprite('keep', 1)	# 28-28
    clearUponHandler(43)
    sprite('Action_123_05', 3)	# 29-31	 **attackbox here**
    sprite('Action_123_03', 3)	# 32-34	 **attackbox here**
    sprite('Action_123_09', 3)	# 35-37	 **attackbox here**
    sprite('Action_123_10', 3)	# 38-40	 **attackbox here**
    sprite('Action_123_11', 3)	# 41-43	 **attackbox here**

@State
def AirBeamA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(5, 1)

        def upon_43():
            if (SLOT_48 == 1100):
                sendToLabel(9)
    sprite('Action_149_00', 3)	# 1-3	 **attackbox here**
    Unknown1084(1)
    sprite('Action_149_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_149_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_149_03', 3)	# 10-12	 **attackbox here**
    GFX_0('Vat_097_AAir', -1)
    tag_voice(1, 'uva204_0', 'uva204_1', 'uva204_2', '')
    sprite('Action_149_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_149_05', 3)	# 16-18	 **attackbox here**
    sprite('Action_149_03', 3)	# 19-21	 **attackbox here**
    sprite('Action_149_04', 3)	# 22-24	 **attackbox here**
    label(9)
    sprite('keep', 1)	# 25-25
    clearUponHandler(43)
    sprite('Action_149_03', 4)	# 26-29	 **attackbox here**
    sprite('Action_149_04', 4)	# 30-33	 **attackbox here**
    sprite('Action_149_05', 4)	# 34-37	 **attackbox here**
    sprite('Action_149_03', 4)	# 38-41	 **attackbox here**
    sprite('Action_149_09', 4)	# 42-45	 **attackbox here**
    physicsYImpulse(3000)
    setGravity(1600)
    sprite('Action_036_06', 4)	# 46-49	 **attackbox here**
    sprite('Action_036_07', 3)	# 50-52	 **attackbox here**
    label(0)
    sprite('Action_036_08', 3)	# 53-55	 **attackbox here**
    sprite('Action_036_09', 3)	# 56-58	 **attackbox here**
    gotoLabel(0)

@State
def AirBeamB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(5, 1)

        def upon_43():
            if (SLOT_48 == 1100):
                sendToLabel(9)
    sprite('Action_150_00', 3)	# 1-3	 **attackbox here**
    Unknown1084(1)
    sprite('Action_150_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_150_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_150_03', 3)	# 10-12	 **attackbox here**
    GFX_0('Vat_097_BAir', -1)
    tag_voice(1, 'uva204_0', 'uva204_1', 'uva204_2', '')
    sprite('Action_150_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_150_05', 3)	# 16-18	 **attackbox here**
    sprite('Action_150_03', 3)	# 19-21	 **attackbox here**
    sprite('Action_150_04', 3)	# 22-24	 **attackbox here**
    label(9)
    sprite('keep', 1)	# 25-25
    clearUponHandler(43)
    sprite('Action_150_03', 4)	# 26-29	 **attackbox here**
    sprite('Action_150_04', 4)	# 30-33	 **attackbox here**
    sprite('Action_150_05', 4)	# 34-37	 **attackbox here**
    sprite('Action_150_03', 4)	# 38-41	 **attackbox here**
    sprite('Action_150_12', 4)	# 42-45	 **attackbox here**
    physicsYImpulse(3000)
    setGravity(1600)
    sprite('Action_036_06', 4)	# 46-49	 **attackbox here**
    sprite('Action_036_07', 3)	# 50-52	 **attackbox here**
    label(0)
    sprite('Action_036_08', 3)	# 53-55	 **attackbox here**
    sprite('Action_036_09', 3)	# 56-58	 **attackbox here**
    gotoLabel(0)

@State
def AirBeam_Ex():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(5, 1)

        def upon_43():
            if (SLOT_48 == 1100):
                sendToLabel(9)
    sprite('Action_151_00', 3)	# 1-3	 **attackbox here**
    Unknown1084(1)
    sprite('Action_151_01', 3)	# 4-6	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_151_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_151_03', 3)	# 10-12	 **attackbox here**
    GFX_0('Vat_083', 0)
    tag_voice(1, 'uva205_0', 'uva205_1', 'uva205_2', '')
    sprite('Action_151_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_151_05', 3)	# 16-18	 **attackbox here**
    label(9)
    sprite('keep', 1)	# 19-19
    clearUponHandler(43)
    sprite('Action_151_03', 4)	# 20-23	 **attackbox here**
    sprite('Action_151_04', 4)	# 24-27	 **attackbox here**
    sprite('Action_151_05', 4)	# 28-31	 **attackbox here**
    sprite('Action_151_03', 4)	# 32-35	 **attackbox here**
    sprite('Action_151_07', 4)	# 36-39	 **attackbox here**
    setGravity(1600)
    sprite('Action_036_08', 3)	# 40-42	 **attackbox here**

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_110_00', 6)	# 1-6	 **attackbox here**
    Unknown1051(60)
    sprite('Action_110_01', 6)	# 7-12	 **attackbox here**
    Unknown1084(1)
    sprite('Action_110_02', 2)	# 13-14	 **attackbox here**
    sprite('Action_110_03', 6)	# 15-20	 **attackbox here**
    GFX_0('Vat_095', 0)
    GFX_0('Vat_101', 0)
    tag_voice(1, 'uva200_0', 'uva200_1', 'uva200_2', '')
    SFX_3('SE_LightBall')
    sprite('Action_110_04', 8)	# 21-28	 **attackbox here**
    Unknown1045(-8000)
    sprite('Action_110_05', 6)	# 29-34	 **attackbox here**
    sprite('Action_110_06', 5)	# 35-39	 **attackbox here**
    sprite('Action_110_07', 5)	# 40-44	 **attackbox here**
    Unknown1084(1)
    sprite('Action_110_08', 5)	# 45-49	 **attackbox here**

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        sendToLabelUpon(2, 1)
        Unknown28(8, 'CmnActCrouch')
    sprite('Action_111_00', 6)	# 1-6	 **attackbox here**
    sprite('Action_111_01', 6)	# 7-12	 **attackbox here**
    sprite('Action_111_02', 2)	# 13-14	 **attackbox here**
    sprite('Action_111_03', 3)	# 15-17	 **attackbox here**
    GFX_0('Vat_095_B', 0)
    GFX_0('Vat_101_B', 0)
    SFX_3('SE_LightBall')
    physicsXImpulse(-18000)
    physicsYImpulse(18000)
    setGravity(2000)
    tag_voice(1, 'uva200_0', 'uva200_1', 'uva200_2', '')
    sprite('Action_111_04', 3)	# 18-20	 **attackbox here**
    sprite('Action_111_05', 3)	# 21-23	 **attackbox here**
    sprite('Action_111_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_111_07', 4)	# 28-31	 **attackbox here**
    sprite('Action_111_08', 4)	# 32-35	 **attackbox here**
    loopRest()
    label(0)
    sprite('Action_037_09', 3)	# 36-38	 **attackbox here**
    sprite('Action_037_10', 3)	# 39-41	 **attackbox here**
    sprite('Action_037_11', 3)	# 42-44	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_111_09', 4)	# 45-48	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_111_10', 10)	# 49-58	 **attackbox here**

@State
def BigShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_113_00', 3)	# 1-3	 **attackbox here**
    Unknown1051(60)
    sprite('Action_113_00', 3)	# 4-6	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_113_01', 6)	# 7-12	 **attackbox here**
    Unknown1084(1)
    GFX_0('Vat_105_B', 0)
    tag_voice(1, 'uva201_1', 'uva201_2', '', '')
    sprite('Action_113_02', 4)	# 13-16	 **attackbox here**
    sprite('Action_113_03', 4)	# 17-20	 **attackbox here**
    sprite('Action_113_04', 4)	# 21-24	 **attackbox here**
    sprite('Action_113_05', 4)	# 25-28	 **attackbox here**
    sprite('Action_113_08', 2)	# 29-30	 **attackbox here**
    sprite('Action_113_09', 6)	# 31-36	 **attackbox here**
    GFX_0('Vat_095_4', 0)
    SFX_3('SE_LightBall')
    sprite('Action_113_10', 8)	# 37-44	 **attackbox here**
    Unknown1045(-8000)
    sprite('Action_113_11', 6)	# 45-50	 **attackbox here**
    sprite('Action_113_12', 5)	# 51-55	 **attackbox here**
    sprite('Action_113_13', 5)	# 56-60	 **attackbox here**
    Unknown1084(1)
    sprite('Action_113_14', 5)	# 61-65	 **attackbox here**

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(5, 1)
    sprite('Action_140_00', 7)	# 1-7	 **attackbox here**
    Unknown1084(1)
    sprite('Action_140_01', 3)	# 8-10	 **attackbox here**
    sprite('Action_140_02', 2)	# 11-12	 **attackbox here**
    sprite('Action_140_03', 10)	# 13-22	 **attackbox here**
    physicsXImpulse(-3500)
    physicsYImpulse(18000)
    setGravity(1200)
    GFX_0('Vat_095_AirA', 0)
    GFX_0('Vat_101_B', 0)
    Unknown36(1)
    Unknown1072(-225000)
    Unknown35()
    tag_voice(1, 'uva200_0', 'uva200_1', 'uva200_2', '')
    SFX_3('SE_LightBall')
    sprite('Action_140_04', 6)	# 23-28	 **attackbox here**
    sprite('Action_140_05', 4)	# 29-32	 **attackbox here**
    sprite('Action_140_06', 4)	# 33-36	 **attackbox here**
    sprite('Action_140_07', 5)	# 37-41	 **attackbox here**
    sprite('Action_140_08', 5)	# 42-46	 **attackbox here**
    sprite('Action_140_09', 5)	# 47-51	 **attackbox here**

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(5, 1)
    sprite('Action_141_00', 7)	# 1-7	 **attackbox here**
    Unknown1084(1)
    sprite('Action_141_01', 3)	# 8-10	 **attackbox here**
    sprite('Action_141_02', 2)	# 11-12	 **attackbox here**
    sprite('Action_141_03', 10)	# 13-22	 **attackbox here**
    physicsXImpulse(-3500)
    physicsYImpulse(18000)
    setGravity(1200)
    GFX_0('Vat_095_AirB', 0)
    GFX_0('Vat_101_B', 0)
    Unknown36(1)
    Unknown1072(-235000)
    Unknown35()
    tag_voice(1, 'uva200_0', 'uva200_1', 'uva200_2', '')
    SFX_3('SE_LightBall')
    sprite('Action_141_04', 6)	# 23-28	 **attackbox here**
    sprite('Action_141_05', 4)	# 29-32	 **attackbox here**
    sprite('Action_141_06', 4)	# 33-36	 **attackbox here**
    sprite('Action_141_07', 5)	# 37-41	 **attackbox here**
    sprite('Action_141_08', 5)	# 42-46	 **attackbox here**
    sprite('Action_141_09', 5)	# 47-51	 **attackbox here**

@State
def AirBigShot():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        Unknown22004(5, 1)
    sprite('Action_142_00', 3)	# 1-3	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    sprite('Action_142_00', 4)	# 4-7	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_142_01', 6)	# 8-13	 **attackbox here**
    GFX_0('Vat_105_Air', 0)
    Unknown36(1)
    Unknown1072(-255000)
    Unknown35()
    tag_voice(1, 'uva201_1', 'uva201_2', '', '')
    sprite('Action_142_02', 2)	# 14-15	 **attackbox here**
    sprite('Action_142_03', 4)	# 16-19	 **attackbox here**
    sprite('Action_142_04', 4)	# 20-23	 **attackbox here**
    sprite('Action_142_05', 4)	# 24-27	 **attackbox here**
    sprite('Action_142_06', 4)	# 28-31	 **attackbox here**
    sprite('Action_142_07', 4)	# 32-35	 **attackbox here**
    sprite('Action_142_08', 2)	# 36-37	 **attackbox here**
    sprite('Action_142_09', 10)	# 38-47	 **attackbox here**
    physicsXImpulse(-3500)
    physicsYImpulse(18000)
    setGravity(1200)
    GFX_0('Vat_095_4Air', 0)
    SFX_3('SE_LightBall')
    Unknown21015('5661745f3130355f416972000000000000000000000000000000000000000000ed03000000000000')
    sprite('Action_142_10', 6)	# 48-53	 **attackbox here**
    sprite('Action_142_11', 4)	# 54-57	 **attackbox here**
    sprite('Action_142_12', 4)	# 58-61	 **attackbox here**
    sprite('Action_142_13', 5)	# 62-66	 **attackbox here**
    sprite('Action_142_14', 5)	# 67-71	 **attackbox here**
    sprite('Action_142_15', 5)	# 72-76	 **attackbox here**

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(12500)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(2500)
        AirUntechableTime(80)
        Hitstop(10)
        Unknown9016(1)
        Unknown11068(1)
        Unknown11056(0)
        sendToLabelUpon(2, 1)

        def upon_78():
            SLOT_51 = 1
        Unknown1051(30)
    sprite('Action_130_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_130_01', 3)	# 6-8	 **attackbox here**
    StartMultihit()
    physicsXImpulse(5000)
    physicsYImpulse(32000)
    setGravity(2000)
    tag_voice(1, 'uva202_0', 'uva202_1', 'uva202_2', '')
    Unknown8001(1, 0)
    sprite('Action_130_02', 3)	# 9-11	 **attackbox here**
    sprite('Action_130_03', 2)	# 12-13	 **attackbox here**
    Unknown14070('AntiAir2nd')
    RefreshMultihit()
    sprite('Action_130_04', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    Hitstop(3)
    sprite('Action_130_04', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_130_04', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_130_05', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_130_06', 3)	# 20-22	 **attackbox here**
    setInvincible(0)
    sprite('Action_130_07', 3)	# 23-25	 **attackbox here**
    sprite('Action_130_08', 3)	# 26-28	 **attackbox here**
    if SLOT_51:
        Unknown14072('AntiAir2nd')
    sprite('Action_130_09', 3)	# 29-31	 **attackbox here**
    Unknown14074('AntiAir2nd')
    label(0)
    sprite('Action_130_10', 3)	# 32-34	 **attackbox here**
    sprite('Action_130_11', 3)	# 35-37	 **attackbox here**
    sprite('Action_130_12', 3)	# 38-40	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_130_13', 5)	# 41-45	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_130_14', 11)	# 46-56	 **attackbox here**
    sprite('Action_130_15', 10)	# 57-66	 **attackbox here**

@State
def AntiAir2nd():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        AttackLevel_(4)
        Damage(1300)
        AttackP1(48)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(50000)
        AirPushbackY(-40000)
        AirUntechableTime(42)
        Unknown9310(20)
        Unknown9016(1)
        Unknown11068(1)
        Unknown11056(0)
        Unknown14083(0)
        Unknown30068(1)
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
    sprite('Action_134_00', 4)	# 1-4	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(2000)
    physicsYImpulse(10000)
    sprite('Action_134_01', 5)	# 5-9	 **attackbox here**
    sprite('Action_134_02', 3)	# 10-12	 **attackbox here**
    physicsXImpulse(-15000)
    physicsYImpulse(15000)
    setGravity(1500)
    tag_voice(1, 'uva301_1', 'uva306_0', 'uva303_0', '')
    sprite('Action_134_03', 5)	# 13-17	 **attackbox here**
    sprite('Action_134_04', 5)	# 18-22	 **attackbox here**
    Unknown1019(40)
    sprite('Action_134_05', 5)	# 23-27	 **attackbox here**
    sprite('Action_134_06', 3)	# 28-30	 **attackbox here**
    sprite('Action_134_07', 3)	# 31-33	 **attackbox here**
    sprite('Action_134_08', 3)	# 34-36	 **attackbox here**
    sprite('Action_134_09', 3)	# 37-39	 **attackbox here**
    sprite('Action_134_10', 3)	# 40-42	 **attackbox here**
    label(0)
    sprite('Action_134_11', 3)	# 43-45	 **attackbox here**
    sprite('Action_134_12', 3)	# 46-48	 **attackbox here**
    sprite('Action_134_13', 3)	# 49-51	 **attackbox here**
    gotoLabel(0)
    label(1)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_134_14', 3)	# 52-54	 **attackbox here**
    sprite('Action_134_15', 6)	# 55-60	 **attackbox here**
    sprite('Action_134_16', 5)	# 61-65	 **attackbox here**

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
        setInvincible(1)
        loopRelated(17, 183)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
    sprite('Action_225_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_225_00', 3)	# 4-6	 **attackbox here**
    Unknown2036(51, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uva250_0', 'uva250_1', '', '')
    SFX_3('SE_SpecialLaserBeam')
    sprite('Action_225_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_225_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_225_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_225_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_225_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_225_06', 3)	# 22-24	 **attackbox here**
    GFX_0('Vat_226', -1)
    sprite('Action_225_07', 3)	# 25-27
    sprite('Action_225_08', 4)	# 28-31
    sprite('Action_225_09', 4)	# 32-35
    sprite('Action_225_10', 4)	# 36-39
    sprite('Action_225_11', 4)	# 40-43
    sprite('Action_225_12', 4)	# 44-47
    sprite('Action_225_13', 4)	# 48-51
    sprite('Action_225_11', 4)	# 52-55
    GFX_0('Vat_228', -1)
    sprite('Action_225_12', 4)	# 56-59
    sprite('Action_225_13', 4)	# 60-63
    sprite('Action_225_11', 4)	# 64-67
    sprite('Action_225_12', 4)	# 68-71
    Unknown1045(-30000)
    sprite('Action_225_13', 4)	# 72-75
    setInvincible(0)
    label(0)
    sprite('Action_225_11', 4)	# 76-79
    sprite('Action_225_12', 4)	# 80-83
    sprite('Action_225_13', 4)	# 84-87
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_225_11', 4)	# 88-91
    Unknown1084(1)
    GFX_0('Vat_228_END', -1)
    Unknown21015('5661745f32323600000000000000000000000000000000000000000000000000d007000000000000')
    sprite('Action_225_12', 4)	# 92-95
    sprite('Action_225_13', 4)	# 96-99
    sprite('Action_225_11', 4)	# 100-103
    sprite('Action_225_12', 4)	# 104-107
    sprite('Action_225_13', 4)	# 108-111
    sprite('Action_225_11', 4)	# 112-115
    sprite('Action_225_12', 4)	# 116-119
    sprite('Action_225_13', 4)	# 120-123
    sprite('Action_225_17', 4)	# 124-127
    sprite('Action_225_18', 4)	# 128-131	 **attackbox here**
    sprite('Action_225_19', 4)	# 132-135	 **attackbox here**
    sprite('Action_225_20', 4)	# 136-139	 **attackbox here**
    sprite('Action_225_21', 4)	# 140-143	 **attackbox here**
    sprite('Action_225_22', 3)	# 144-146	 **attackbox here**

@State
def UltimateShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
        setInvincible(1)
        loopRelated(17, 243)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
    sprite('Action_225_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_225_00', 3)	# 4-6	 **attackbox here**
    Unknown2036(51, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uva250_0', 'uva250_1', '', '')
    SFX_3('SE_SpecialLaserBeam')
    sprite('Action_225_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_225_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_225_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_225_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_225_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_225_06', 3)	# 22-24	 **attackbox here**
    GFX_0('Vat_226', -1)
    Unknown23029(1, 2001, 0)
    sprite('Action_225_07', 3)	# 25-27
    sprite('Action_225_08', 4)	# 28-31
    sprite('Action_225_09', 4)	# 32-35
    sprite('Action_225_10', 4)	# 36-39
    sprite('Action_225_11', 4)	# 40-43
    sprite('Action_225_12', 4)	# 44-47
    sprite('Action_225_13', 4)	# 48-51
    sprite('Action_225_11', 4)	# 52-55
    GFX_0('Vat_228', -1)
    sprite('Action_225_12', 4)	# 56-59
    sprite('Action_225_13', 4)	# 60-63
    sprite('Action_225_11', 4)	# 64-67
    sprite('Action_225_12', 4)	# 68-71
    Unknown1045(-30000)
    sprite('Action_225_13', 4)	# 72-75
    setInvincible(0)
    label(0)
    sprite('Action_225_11', 4)	# 76-79
    sprite('Action_225_12', 4)	# 80-83
    sprite('Action_225_13', 4)	# 84-87
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_225_11', 4)	# 88-91
    Unknown1084(1)
    GFX_0('Vat_228_END', -1)
    Unknown21015('5661745f32323600000000000000000000000000000000000000000000000000d007000000000000')
    sprite('Action_225_12', 4)	# 92-95
    sprite('Action_225_13', 4)	# 96-99
    sprite('Action_225_11', 4)	# 100-103
    sprite('Action_225_12', 4)	# 104-107
    sprite('Action_225_13', 4)	# 108-111
    sprite('Action_225_11', 4)	# 112-115
    sprite('Action_225_12', 4)	# 116-119
    sprite('Action_225_13', 4)	# 120-123
    sprite('Action_225_17', 4)	# 124-127
    sprite('Action_225_18', 4)	# 128-131	 **attackbox here**
    sprite('Action_225_19', 4)	# 132-135	 **attackbox here**
    sprite('Action_225_20', 4)	# 136-139	 **attackbox here**
    sprite('Action_225_21', 4)	# 140-143	 **attackbox here**
    sprite('Action_225_22', 3)	# 144-146	 **attackbox here**

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(950)
        AttackP2(60)
        Unknown11091(13)
        Unknown11092(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(5000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown9310(10)
        Unknown11056(0)
        Unknown30055('90d003005000000000000000')
        Unknown30056('90d003001e00000000000000')
        setInvincible(1)
        sendToLabelUpon(2, 1)
    sprite('Action_262_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_262_00', 2)	# 4-5	 **attackbox here**
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uva251_1', 'uva251_2', '', '')
    sprite('Action_262_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_262_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_262_03', 3)	# 16-18	 **attackbox here**
    sprite('Action_262_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_262_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_262_04', 3)	# 25-27	 **attackbox here**
    sprite('Action_262_03', 3)	# 28-30	 **attackbox here**
    sprite('Action_262_04', 3)	# 31-33	 **attackbox here**
    sprite('Action_262_03', 3)	# 34-36	 **attackbox here**
    sprite('Action_262_04', 3)	# 37-39	 **attackbox here**
    sprite('Action_262_03', 3)	# 40-42	 **attackbox here**
    sprite('Action_262_04', 3)	# 43-45	 **attackbox here**
    sprite('Action_132_00', 3)	# 46-48	 **attackbox here**
    sprite('Action_132_01', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(7000)
    physicsYImpulse(32000)
    setGravity(1500)
    Unknown1021(200)
    Unknown8001(1, 0)
    sprite('Action_132_02', 3)	# 52-54	 **attackbox here**
    sprite('Action_132_03', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    sprite('Action_132_04', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_05', 2)	# 59-60	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(15000)
    sprite('Action_132_06', 3)	# 61-63	 **attackbox here**
    Unknown1019(150)
    YAccel(150)
    setInvincible(0)
    sprite('Action_132_07', 3)	# 64-66	 **attackbox here**
    sprite('Action_132_08', 3)	# 67-69	 **attackbox here**
    sprite('Action_132_09', 4)	# 70-73	 **attackbox here**
    physicsXImpulse(10000)
    physicsYImpulse(-15000)
    sprite('Action_132_10', 3)	# 74-76	 **attackbox here**
    GFX_0('Vat_077', 0)
    SFX_3('SE038')
    label(0)
    sprite('Action_132_11', 2)	# 77-78	 **attackbox here**
    Unknown30055('708203006400000000000000')
    Unknown30056('307500006400000000000000')
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    RefreshMultihit()
    AirPushbackX(8000)
    AirPushbackY(-5000)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_132_12', 2)	# 79-80	 **attackbox here**
    sprite('Action_132_13', 2)	# 81-82	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_14', 2)	# 83-84	 **attackbox here**
    sprite('Action_132_15', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_16', 2)	# 87-88	 **attackbox here**
    sprite('Action_132_17', 2)	# 89-90	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_11', 2)	# 91-92	 **attackbox here**
    sprite('Action_132_12', 2)	# 93-94	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_13', 2)	# 95-96	 **attackbox here**
    sprite('Action_132_14', 2)	# 97-98	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_15', 2)	# 99-100	 **attackbox here**
    sprite('Action_132_16', 2)	# 101-102	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_17', 2)	# 103-104	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_132_18', 2)	# 105-106	 **attackbox here**
    Unknown26('Vat_077')
    Unknown8000(100, 1, 1)
    sprite('Action_132_19', 2)	# 107-108	 **attackbox here**
    sprite('Action_132_20', 3)	# 109-111	 **attackbox here**
    sprite('Action_132_21', 3)	# 112-114	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    physicsXImpulse(7000)
    physicsYImpulse(32000)
    setGravity(1500)
    Unknown1021(200)
    AirPushbackY(20000)
    Unknown9310(0)
    Unknown30055('c04504006400000000000000')
    Unknown30056('90d003001e00000000000000')
    Hitstop(12)
    Unknown8001(1, 0)
    Unknown11058('0000000001000000000000000000000000000000')
    sprite('Action_132_22', 3)	# 115-117	 **attackbox here**
    sendToLabelUpon(2, 3)
    sprite('Action_132_23', 2)	# 118-119	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    sprite('Action_132_24', 2)	# 120-121	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_24', 2)	# 122-123	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_24', 2)	# 124-125	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_25', 3)	# 126-128	 **attackbox here**
    AirPushbackX(16000)
    AirPushbackY(36000)
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    RefreshMultihit()
    sprite('Action_132_26', 3)	# 129-131	 **attackbox here**
    Unknown1019(60)
    sprite('Action_132_27', 3)	# 132-134	 **attackbox here**
    sprite('Action_132_28', 3)	# 135-137	 **attackbox here**
    sprite('Action_132_29', 3)	# 138-140	 **attackbox here**
    label(2)
    sprite('Action_132_30', 3)	# 141-143	 **attackbox here**
    sprite('Action_132_31', 3)	# 144-146	 **attackbox here**
    sprite('Action_132_32', 3)	# 147-149	 **attackbox here**
    gotoLabel(2)
    label(3)
    sprite('Action_132_33', 5)	# 150-154	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_132_34', 8)	# 155-162	 **attackbox here**
    sprite('Action_132_35', 7)	# 163-169	 **attackbox here**

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(950)
        AttackP2(60)
        Unknown11091(12)
        Unknown11092(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(5000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown9310(10)
        Unknown11056(0)
        Unknown30055('90d003005000000000000000')
        Unknown30056('90d003001e00000000000000')
        setInvincible(1)
        sendToLabelUpon(2, 1)
    sprite('Action_262_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_262_00', 2)	# 4-5	 **attackbox here**
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uva251_1', 'uva251_2', '', '')
    sprite('Action_262_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_262_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_262_03', 3)	# 16-18	 **attackbox here**
    sprite('Action_262_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_262_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_262_04', 3)	# 25-27	 **attackbox here**
    sprite('Action_262_03', 3)	# 28-30	 **attackbox here**
    sprite('Action_262_04', 3)	# 31-33	 **attackbox here**
    sprite('Action_262_03', 3)	# 34-36	 **attackbox here**
    sprite('Action_262_04', 3)	# 37-39	 **attackbox here**
    sprite('Action_262_03', 3)	# 40-42	 **attackbox here**
    sprite('Action_262_04', 3)	# 43-45	 **attackbox here**
    sprite('Action_132_00', 3)	# 46-48	 **attackbox here**
    sprite('Action_132_01', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(7000)
    physicsYImpulse(32000)
    setGravity(1500)
    Unknown1021(200)
    Unknown8001(1, 0)
    sprite('Action_132_02', 3)	# 52-54	 **attackbox here**
    sprite('Action_132_03', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    sprite('Action_132_04', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_05', 2)	# 59-60	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(15000)
    sprite('Action_132_06', 3)	# 61-63	 **attackbox here**
    Unknown1019(150)
    YAccel(150)
    setInvincible(0)
    sprite('Action_132_07', 3)	# 64-66	 **attackbox here**
    sprite('Action_132_08', 3)	# 67-69	 **attackbox here**
    sprite('Action_132_09', 4)	# 70-73	 **attackbox here**
    physicsXImpulse(10000)
    physicsYImpulse(-15000)
    sprite('Action_132_10', 3)	# 74-76	 **attackbox here**
    GFX_0('Vat_077', 0)
    SFX_3('SE038')
    label(0)
    sprite('Action_132_11', 2)	# 77-78	 **attackbox here**
    Unknown30055('708203006400000000000000')
    Unknown30056('307500006400000000000000')
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    RefreshMultihit()
    AirPushbackX(8000)
    AirPushbackY(-5000)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_132_12', 2)	# 79-80	 **attackbox here**
    sprite('Action_132_13', 2)	# 81-82	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_14', 2)	# 83-84	 **attackbox here**
    sprite('Action_132_15', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_16', 2)	# 87-88	 **attackbox here**
    sprite('Action_132_17', 2)	# 89-90	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_11', 2)	# 91-92	 **attackbox here**
    sprite('Action_132_12', 2)	# 93-94	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_13', 2)	# 95-96	 **attackbox here**
    sprite('Action_132_14', 2)	# 97-98	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_15', 2)	# 99-100	 **attackbox here**
    sprite('Action_132_16', 2)	# 101-102	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_17', 2)	# 103-104	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_132_18', 2)	# 105-106	 **attackbox here**
    Unknown26('Vat_077')
    Unknown8000(100, 1, 1)
    sprite('Action_132_19', 2)	# 107-108	 **attackbox here**
    sprite('Action_132_20', 3)	# 109-111	 **attackbox here**
    sprite('Action_132_21', 3)	# 112-114	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    physicsXImpulse(7000)
    physicsYImpulse(32000)
    setGravity(1500)
    Unknown1021(200)
    AirPushbackY(20000)
    Unknown9310(0)
    Unknown30055('c04504006400000000000000')
    Unknown30056('90d003001e00000000000000')
    Hitstop(12)
    Unknown8001(1, 0)
    Unknown11058('0000000001000000000000000000000000000000')
    sprite('Action_132_22', 3)	# 115-117	 **attackbox here**
    sendToLabelUpon(2, 3)
    sprite('Action_132_23', 2)	# 118-119	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    sprite('Action_132_24', 2)	# 120-121	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_24', 2)	# 122-123	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_24', 2)	# 124-125	 **attackbox here**
    RefreshMultihit()
    sprite('Action_132_25', 3)	# 126-128	 **attackbox here**
    RefreshMultihit()
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    sprite('Action_132_26', 3)	# 129-131	 **attackbox here**
    Unknown1019(60)
    sprite('Action_132_27', 3)	# 132-134	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(2000)
    physicsYImpulse(10000)
    sprite('Action_134_00', 4)	# 135-138	 **attackbox here**
    sprite('Action_134_01', 5)	# 139-143	 **attackbox here**
    sprite('Action_134_02', 3)	# 144-146	 **attackbox here**
    RefreshMultihit()
    Damage(2600)
    Unknown11091(13)
    AirPushbackX(70000)
    AirPushbackY(-20000)
    AirUntechableTime(42)
    Unknown9310(25)
    Hitstop(16)
    physicsXImpulse(-5000)
    physicsYImpulse(15000)
    setGravity(1500)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_134_03', 5)	# 147-151	 **attackbox here**
    sprite('Action_134_04', 5)	# 152-156	 **attackbox here**
    Unknown1019(40)
    sprite('Action_134_05', 5)	# 157-161	 **attackbox here**
    sprite('Action_134_06', 3)	# 162-164	 **attackbox here**
    sprite('Action_134_07', 3)	# 165-167	 **attackbox here**
    sprite('Action_134_08', 3)	# 168-170	 **attackbox here**
    sprite('Action_134_09', 3)	# 171-173	 **attackbox here**
    sprite('Action_134_10', 3)	# 174-176	 **attackbox here**
    label(2)
    sprite('Action_134_11', 3)	# 177-179	 **attackbox here**
    sprite('Action_134_12', 3)	# 180-182	 **attackbox here**
    sprite('Action_134_13', 3)	# 183-185	 **attackbox here**
    gotoLabel(2)
    label(3)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_134_14', 3)	# 186-188	 **attackbox here**
    sprite('Action_134_15', 6)	# 189-194	 **attackbox here**
    sprite('Action_134_16', 5)	# 195-199	 **attackbox here**

@State
def AirUltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        Unknown1084(1)
        setInvincible(1)
        loopRelated(17, 183)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
        clearUponHandler(2)
        sendToLabelUpon(2, 3)
    sprite('Action_225_00', 3)	# 1-3	 **attackbox here**
    GFX_0('Vat_165', -1)
    sprite('Action_225_00', 3)	# 4-6	 **attackbox here**
    Unknown2036(51, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uva250_0', 'uva250_1', '', '')
    SFX_3('SE_SpecialLaserBeam')
    sprite('Action_225_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_225_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_225_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_225_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_225_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_225_06', 3)	# 22-24	 **attackbox here**
    GFX_0('Vat_226', -1)
    sprite('Action_225_07', 3)	# 25-27
    sprite('Action_225_08', 4)	# 28-31
    sprite('Action_225_09', 4)	# 32-35
    sprite('Action_225_10', 4)	# 36-39
    sprite('Action_225_11', 4)	# 40-43
    sprite('Action_225_12', 4)	# 44-47
    sprite('Action_225_13', 4)	# 48-51
    sprite('Action_225_11', 4)	# 52-55
    GFX_0('Vat_228', -1)
    sprite('Action_225_12', 4)	# 56-59
    sprite('Action_225_13', 4)	# 60-63
    sprite('Action_225_11', 4)	# 64-67
    sprite('Action_225_12', 4)	# 68-71
    sprite('Action_225_13', 4)	# 72-75
    setInvincible(0)
    label(0)
    sprite('Action_225_11', 4)	# 76-79
    sprite('Action_225_12', 4)	# 80-83
    sprite('Action_225_13', 4)	# 84-87
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_225_11', 4)	# 88-91
    GFX_0('Vat_228_END', -1)
    Unknown21015('5661745f32323600000000000000000000000000000000000000000000000000d007000000000000')
    sprite('Action_225_12', 4)	# 92-95
    sprite('Action_225_13', 4)	# 96-99
    sprite('Action_225_11', 4)	# 100-103
    sprite('Action_225_12', 4)	# 104-107
    sprite('Action_225_13', 4)	# 108-111
    sprite('Action_225_17', 4)	# 112-115
    sprite('Action_225_18', 4)	# 116-119	 **attackbox here**
    sprite('Action_225_19', 4)	# 120-123	 **attackbox here**
    Unknown21015('5661745f31363500000000000000000000000000000000000000000000000000d407000000000000')
    sprite('Action_225_20', 4)	# 124-127	 **attackbox here**
    sprite('Action_225_21', 4)	# 128-131	 **attackbox here**
    sprite('Action_164_14', 2)	# 132-133	 **attackbox here**
    sprite('Action_164_15', 3)	# 134-136	 **attackbox here**
    physicsYImpulse(8000)
    setGravity(2200)
    sprite('Action_164_16', 4)	# 137-140	 **attackbox here**
    sprite('Action_164_17', 4)	# 141-144	 **attackbox here**
    sprite('Action_164_18', 4)	# 145-148	 **attackbox here**
    label(2)
    sprite('Action_036_08', 3)	# 149-151	 **attackbox here**
    sprite('Action_036_09', 3)	# 152-154	 **attackbox here**
    gotoLabel(2)
    label(3)
    sprite('Action_037_12', 3)	# 155-157	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_037_13', 3)	# 158-160	 **attackbox here**

@State
def AirUltimateShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        Unknown1084(1)
        setInvincible(1)
        loopRelated(17, 243)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
        clearUponHandler(2)
        sendToLabelUpon(2, 3)
    sprite('Action_225_00', 3)	# 1-3	 **attackbox here**
    GFX_0('Vat_165', -1)
    sprite('Action_225_00', 3)	# 4-6	 **attackbox here**
    Unknown2036(51, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uva250_0', 'uva250_1', '', '')
    SFX_3('SE_SpecialLaserBeam')
    sprite('Action_225_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_225_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_225_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_225_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_225_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_225_06', 3)	# 22-24	 **attackbox here**
    GFX_0('Vat_226', -1)
    Unknown23029(1, 2001, 0)
    sprite('Action_225_07', 3)	# 25-27
    sprite('Action_225_08', 4)	# 28-31
    sprite('Action_225_09', 4)	# 32-35
    sprite('Action_225_10', 4)	# 36-39
    sprite('Action_225_11', 4)	# 40-43
    sprite('Action_225_12', 4)	# 44-47
    sprite('Action_225_13', 4)	# 48-51
    sprite('Action_225_11', 4)	# 52-55
    GFX_0('Vat_228', -1)
    sprite('Action_225_12', 4)	# 56-59
    sprite('Action_225_13', 4)	# 60-63
    sprite('Action_225_11', 4)	# 64-67
    sprite('Action_225_12', 4)	# 68-71
    sprite('Action_225_13', 4)	# 72-75
    setInvincible(0)
    label(0)
    sprite('Action_225_11', 4)	# 76-79
    sprite('Action_225_12', 4)	# 80-83
    sprite('Action_225_13', 4)	# 84-87
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_225_11', 4)	# 88-91
    GFX_0('Vat_228_END', -1)
    Unknown21015('5661745f32323600000000000000000000000000000000000000000000000000d007000000000000')
    sprite('Action_225_12', 4)	# 92-95
    sprite('Action_225_13', 4)	# 96-99
    sprite('Action_225_11', 4)	# 100-103
    sprite('Action_225_12', 4)	# 104-107
    sprite('Action_225_13', 4)	# 108-111
    sprite('Action_225_17', 4)	# 112-115
    sprite('Action_225_18', 4)	# 116-119	 **attackbox here**
    sprite('Action_225_19', 4)	# 120-123	 **attackbox here**
    Unknown21015('5661745f31363500000000000000000000000000000000000000000000000000d407000000000000')
    sprite('Action_225_20', 4)	# 124-127	 **attackbox here**
    sprite('Action_225_21', 4)	# 128-131	 **attackbox here**
    sprite('Action_164_14', 2)	# 132-133	 **attackbox here**
    sprite('Action_164_15', 3)	# 134-136	 **attackbox here**
    physicsYImpulse(8000)
    setGravity(2200)
    sprite('Action_164_16', 4)	# 137-140	 **attackbox here**
    sprite('Action_164_17', 4)	# 141-144	 **attackbox here**
    sprite('Action_164_18', 4)	# 145-148	 **attackbox here**
    label(2)
    sprite('Action_036_08', 3)	# 149-151	 **attackbox here**
    sprite('Action_036_09', 3)	# 152-154	 **attackbox here**
    gotoLabel(2)
    label(3)
    sprite('Action_037_12', 3)	# 155-157	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_037_13', 3)	# 158-160	 **attackbox here**

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(5300)
        Unknown11091(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(300)
        YImpluseBeforeWallbounce(0)
        Unknown11056(0)
        AirUntechableTime(999)
        Unknown11067(1)
        setInvincible(1)
        Unknown11058('0100000000000000000000000000000000000000')

        def upon_78():
            PushbackX(0)
            GFX_0('AstWhiteOut', -1)
            clearUponHandler(78)
            setInvincible(1)
            Unknown23088(1, 1)
            Unknown23157(1)
            Unknown2017(0)
            Unknown2053(0)
            Unknown2034(0)
            Unknown23084(1)
            Unknown20003(1)
            Unknown20004(1)
            sendToLabel(100)
    sprite('Action_451_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_451_01', 4)	# 4-7	 **attackbox here**
    Unknown2036(80, -1, 1)
    Unknown23147()
    physicsXImpulse(-8500)
    physicsYImpulse(28000)
    setGravity(1500)
    sprite('Action_451_02', 4)	# 8-11	 **attackbox here**
    sprite('Action_451_03', 4)	# 12-15	 **attackbox here**
    sprite('Action_451_04', 4)	# 16-19	 **attackbox here**
    sprite('Action_451_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_451_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_451_07', 3)	# 28-30	 **attackbox here**
    physicsXImpulse(-500)
    physicsYImpulse(300)
    setGravity(0)
    GFX_0('Vat_999', 100)
    sprite('Action_451_08', 3)	# 31-33	 **attackbox here**
    SFX_1('uva292')
    sprite('Action_452_00', 3)	# 34-36	 **attackbox here**
    sprite('Action_452_01', 3)	# 37-39	 **attackbox here**
    sprite('Action_452_02', 3)	# 40-42	 **attackbox here**
    sprite('Action_452_03', 3)	# 43-45	 **attackbox here**
    sprite('Action_452_01', 3)	# 46-48	 **attackbox here**
    sprite('Action_452_02', 3)	# 49-51	 **attackbox here**
    sprite('Action_452_03', 3)	# 52-54	 **attackbox here**
    sprite('Action_452_01', 3)	# 55-57	 **attackbox here**
    sprite('Action_452_02', 3)	# 58-60	 **attackbox here**
    sprite('Action_452_03', 3)	# 61-63	 **attackbox here**
    sprite('Action_452_01', 3)	# 64-66	 **attackbox here**
    sprite('Action_452_02', 3)	# 67-69	 **attackbox here**
    sprite('Action_452_03', 3)	# 70-72	 **attackbox here**
    sprite('Action_452_01', 3)	# 73-75	 **attackbox here**
    sprite('Action_452_02', 3)	# 76-78	 **attackbox here**
    sprite('Action_452_04', 2)	# 79-80	 **attackbox here**
    sprite('Action_452_05', 3)	# 81-83	 **attackbox here**
    physicsXImpulse(500)
    physicsYImpulse(-1000)
    setGravity(200)
    StartMultihit()
    sprite('Action_452_06', 3)	# 84-86	 **attackbox here**
    StartMultihit()
    sprite('Action_452_05', 3)	# 87-89	 **attackbox here**
    StartMultihit()
    SFX_3('SE_LaserBeam')
    sprite('Action_452_05', 3)	# 90-92	 **attackbox here**
    physicsXImpulse(90000)
    physicsYImpulse(-13200)
    setGravity(900)
    Unknown2017(0)
    clearUponHandler(2)
    sprite('Action_452_06', 3)	# 93-95	 **attackbox here**
    sprite('Action_452_05', 3)	# 96-98	 **attackbox here**
    sprite('Action_452_06', 3)	# 99-101	 **attackbox here**
    sprite('Action_452_05', 1)	# 102-102	 **attackbox here**
    sprite('Action_068_08', 3)	# 103-105	 **attackbox here**
    Unknown2017(1)
    StartMultihit()
    Unknown1019(60)
    physicsYImpulse(4000)
    setGravity(1200)
    Unknown1019(60)
    setInvincible(0)
    sprite('Action_068_09', 3)	# 106-108	 **attackbox here**
    sendToLabelUpon(2, 1)
    label(0)
    sprite('Action_068_10', 3)	# 109-111	 **attackbox here**
    sprite('Action_068_11', 3)	# 112-114	 **attackbox here**
    sprite('Action_068_12', 3)	# 115-117	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_037_13', 6)	# 118-123	 **attackbox here**
    Unknown1019(0)
    clearUponHandler(2)
    Unknown1045(18000)
    Unknown8000(100, 1, 1)
    sprite('Action_037_14', 5)	# 124-128	 **attackbox here**
    ExitState()
    label(100)
    sprite('keep', 3)	# 129-131
    clearUponHandler(78)
    Unknown1084(1)
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown1007(15000)
    Unknown35()
    Unknown36(25)
    Unknown1086(22)
    teleportRelativeX(-300000)
    Unknown35()
    GFX_0('Astral_Camera', -1)
    Unknown38(4, 1)
    sprite('Action_453_01', 30)	# 132-161	 **attackbox here**
    Unknown1084(1)
    teleportRelativeY(0)
    sprite('Action_453_02', 4)	# 162-165	 **attackbox here**
    sprite('Action_453_03', 4)	# 166-169	 **attackbox here**
    tag_voice(1, 'uva290', '', '', '')
    sprite('Action_453_04', 4)	# 170-173	 **attackbox here**
    sprite('Action_453_05', 4)	# 174-177	 **attackbox here**
    GFX_0('Vat_476', -1)
    loopRest()
    sprite('Action_453_07', 4)	# 178-181
    GFX_0('Vat_462', -1)
    sprite('Action_453_08', 4)	# 182-185
    sprite('Action_453_09', 4)	# 186-189
    sprite('Action_453_10', 4)	# 190-193
    sprite('Action_453_11', 5)	# 194-198
    sprite('Action_454_00', 2)	# 199-200
    GFX_0('Vat_463', -1)
    GFX_0('Vat_464', -1)
    Unknown23029(4, 3002, 0)
    label(10)
    sprite('Action_454_01', 4)	# 201-204
    sprite('Action_454_02', 4)	# 205-208
    sprite('Action_454_03', 4)	# 209-212
    SLOT_51 = (SLOT_51 + 1)
    if (SLOT_51 == 21):
        tag_voice(1, 'uva291', '', '', '')
    if (SLOT_51 >= 23):
        sendToLabel(11)
    gotoLabel(10)
    label(11)
    sprite('Action_455_00', 3)	# 213-215
    Unknown21015('5661745f34373600000000000000000000000000000000000000000000000000b90b000000000000')
    sprite('Action_455_01', 3)	# 216-218
    sprite('Action_455_02', 4)	# 219-222
    sprite('Action_455_03', 4)	# 223-226
    sprite('Action_455_04', 4)	# 227-230
    sprite('Action_455_05', 6)	# 231-236
    sprite('Action_455_06', 3)	# 237-239
    sprite('Action_455_07', 4)	# 240-243
    sprite('Action_455_08', 3)	# 244-246	 **attackbox here**
    GFX_0('Vat_472', -1)
    physicsXImpulse(-500)
    physicsYImpulse(3500)
    setGravity(200)
    clearUponHandler(2)
    sprite('Action_455_09', 4)	# 247-250
    sprite('Action_455_10', 4)	# 251-254
    sprite('Action_455_11', 4)	# 255-258
    sprite('Action_455_12', 4)	# 259-262	 **attackbox here**
    RefreshMultihit()
    Damage(40000)
    Hitstop(1)
    AirPushbackY(50000)
    YImpluseBeforeWallbounce(650)
    AirPushbackX(0)
    Unknown11064(3)
    SFX_3('SE_BigBomb')
    Unknown11023(1)
    sendToLabelUpon(2, 13)
    sprite('Action_456_00', 4)	# 263-266	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(52000)
    setGravity(650)
    sprite('Action_456_01', 4)	# 267-270	 **attackbox here**
    sprite('Action_456_02', 4)	# 271-274	 **attackbox here**
    Unknown23024(0)
    label(12)
    sprite('Action_456_03', 3)	# 275-277	 **attackbox here**
    sprite('Action_456_04', 3)	# 278-280	 **attackbox here**
    sprite('Action_456_05', 3)	# 281-283	 **attackbox here**
    gotoLabel(12)
    label(13)
    sprite('Action_456_06', 3)	# 284-286	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_456_07', 6)	# 287-292	 **attackbox here**
    sprite('Action_456_08', 5)	# 293-297	 **attackbox here**

@State
def AstralHeatEnd():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown20000(1)
        Unknown1000(0)
        Unknown23024(0)
    sprite('Action_000_00', 5)	# 1-5	 **attackbox here**

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
    sprite('Action_261_00', 5)	# 1-5	 **attackbox here**
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('Action_261_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_261_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_261_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_261_04', 4)	# 21-24	 **attackbox here**
    sprite('Action_261_05', 4)	# 25-28	 **attackbox here**
    sprite('Action_261_07', 4)	# 29-32
    sprite('Action_261_08', 4)	# 33-36	 **attackbox here**
    sprite('Action_261_09', 4)	# 37-40	 **attackbox here**
    sprite('Action_261_11', 3)	# 41-43
    sprite('Action_261_12', 3)	# 44-46	 **attackbox here**

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
    sprite('Action_019_17', 2)	# 1-2	 **attackbox here**
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('Action_019_16', 2)	# 3-4	 **attackbox here**
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    label(0)
    sprite('Action_019_15', 5)	# 5-9	 **attackbox here**
    sprite('Action_019_14', 5)	# 10-14	 **attackbox here**
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
    sprite('Action_019_16', 6)	# 15-20	 **attackbox here**
    sprite('Action_019_17', 6)	# 21-26	 **attackbox here**

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_046_01', 3)	# 1-3	 **attackbox here**
    sprite('Action_046_02', 3)	# 4-6	 **attackbox here**
    sprite('Action_046_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_046_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_046_01', 3)	# 13-15	 **attackbox here**
    sprite('Action_046_02', 3)	# 16-18	 **attackbox here**
    sprite('Action_046_01', 3)	# 19-21	 **attackbox here**
    sprite('Action_046_02', 3)	# 22-24	 **attackbox here**
    sprite('Action_046_01', 3)	# 25-27	 **attackbox here**
    sprite('Action_046_02', 3)	# 28-30	 **attackbox here**
    sprite('Action_046_01', 30)	# 31-60	 **attackbox here**

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('Action_000_19', 4)	# 1-4	 **attackbox here**
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('Action_000_20', 8)	# 5-12	 **attackbox here**
    sprite('Action_000_21', 11)	# 13-23	 **attackbox here**
    label(1)
    sprite('Action_000_22', 5)	# 24-28	 **attackbox here**
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('Action_000_23', 12)	# 29-40	 **attackbox here**
    sprite('Action_000_24', 6)	# 41-46	 **attackbox here**

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_052_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_052_01', 8)	# 4-11	 **attackbox here**
    sprite('Action_052_02', 8)	# 12-19	 **attackbox here**
    sprite('Action_052_03', 12)	# 20-31	 **attackbox here**
    sprite('Action_052_07', 11)	# 32-42	 **attackbox here**
    sprite('Action_052_08', 8)	# 43-50	 **attackbox here**
    sprite('Action_052_09', 5)	# 51-55	 **attackbox here**
    sprite('Action_052_10', 5)	# 56-60	 **attackbox here**
    sprite('Action_052_11', 5)	# 61-65	 **attackbox here**
    sprite('Action_052_12', 5)	# 66-70	 **attackbox here**
    sprite('Action_052_13', 5)	# 71-75	 **attackbox here**
    sprite('Action_052_09', 5)	# 76-80	 **attackbox here**
    sprite('Action_052_00', 20)	# 81-100	 **attackbox here**

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('Action_009_02', 4)	# 26-29
    GFX_0('Vat_191', -1)
    Unknown36(1)
    teleportRelativeX(23000)
    Unknown1007(23000)
    Unknown1072(-10000)
    Unknown35()
    SFX_3('SE_SwingLightSword')
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    label(1)
    sprite('Action_009_03', 2)	# 30-31	 **attackbox here**
    sprite('Action_009_04', 2)	# 32-33	 **attackbox here**
    sprite('Action_009_05', 2)	# 34-35	 **attackbox here**
    sprite('Action_009_06', 2)	# 36-37	 **attackbox here**
    sprite('Action_009_07', 2)	# 38-39	 **attackbox here**
    gotoLabel(1)
    label(9)
    sprite('Action_009_03', 3)	# 40-42	 **attackbox here**
    Unknown2017(1)
    Unknown2053(1)
    Unknown1019(30)
    sprite('Action_037_12', 6)	# 43-48	 **attackbox here**
    Unknown26('Vat_191')
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_037_13', 10)	# 49-58	 **attackbox here**
    sprite('Action_037_14', 6)	# 59-64	 **attackbox here**

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_052_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_052_01', 5)	# 4-8	 **attackbox here**
    sprite('Action_052_02', 5)	# 9-13	 **attackbox here**
    sprite('Action_052_03', 9)	# 14-22	 **attackbox here**
    sprite('Action_052_07', 8)	# 23-30	 **attackbox here**
    sprite('Action_052_08', 8)	# 31-38	 **attackbox here**
    sprite('Action_052_09', 5)	# 39-43	 **attackbox here**
    sprite('Action_052_10', 5)	# 44-48	 **attackbox here**
    sprite('Action_052_11', 5)	# 49-53	 **attackbox here**
    sprite('Action_052_12', 5)	# 54-58	 **attackbox here**
    sprite('Action_052_13', 5)	# 59-63	 **attackbox here**
    sprite('Action_052_09', 5)	# 64-68	 **attackbox here**
    sprite('Action_052_00', 30)	# 69-98	 **attackbox here**

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_03ex', 3)	# 1-3	 **attackbox here**
    sprite('Action_045_04', 3)	# 4-6	 **attackbox here**
    sprite('Action_045_05', 3)	# 7-9	 **attackbox here**
    sprite('Action_045_06', 3)	# 10-12	 **attackbox here**
    sprite('Action_045_07', 5)	# 13-17	 **attackbox here**
    sprite('Action_045_08', 5)	# 18-22	 **attackbox here**
    sprite('Action_045_09', 7)	# 23-29	 **attackbox here**

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('Action_011_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_046_01', 2)	# 2-3	 **attackbox here**
    sprite('Action_046_01', 2)	# 4-5	 **attackbox here**
    sprite('Action_046_02', 1)	# 6-6	 **attackbox here**
    sprite('Action_046_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_046_03ex', 1)	# 9-9	 **attackbox here**
    loopRest()
    label(0)
    sprite('Action_046_04ex', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_05ex', 3)	# 13-15	 **attackbox here**
    sprite('Action_046_06ex', 3)	# 16-18	 **attackbox here**

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
    sprite('Action_022_00', 4)	# 3-6	 **attackbox here**
    Unknown1019(95)
    sprite('Action_022_01', 4)	# 7-10	 **attackbox here**
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('Action_037_12', 2)	# 11-12	 **attackbox here**
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_113_00', 3)	# 1-3	 **attackbox here**
    Unknown1051(60)
    sprite('Action_113_00', 3)	# 4-6	 **attackbox here**
    sprite('Action_113_01', 6)	# 7-12	 **attackbox here**
    Unknown1084(1)
    GFX_0('Vat_105_B', 0)
    tag_voice(1, 'uva201_1', 'uva201_2', '', '')
    sprite('Action_113_02', 4)	# 13-16	 **attackbox here**
    sprite('Action_113_03', 4)	# 17-20	 **attackbox here**
    sprite('Action_113_04', 4)	# 21-24	 **attackbox here**
    sprite('Action_113_05', 4)	# 25-28	 **attackbox here**
    sprite('Action_113_06', 4)	# 29-32	 **attackbox here**
    sprite('Action_113_07', 4)	# 33-36	 **attackbox here**
    sprite('Action_113_08', 2)	# 37-38	 **attackbox here**
    sprite('Action_113_09', 6)	# 39-44	 **attackbox here**
    GFX_0('Vat_095_4', 0)
    Unknown23029(1, 1200, 0)
    SFX_3('SE_LightBall')
    sprite('Action_113_10', 8)	# 45-52	 **attackbox here**
    Unknown1045(-8000)
    sprite('Action_113_11', 6)	# 53-58	 **attackbox here**
    sprite('Action_113_12', 5)	# 59-63	 **attackbox here**
    sprite('Action_113_13', 5)	# 64-68	 **attackbox here**
    Unknown1084(1)
    sprite('Action_113_14', 5)	# 69-73	 **attackbox here**

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 1100):
                sendToLabel(9)
    sprite('Action_121_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_121_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_121_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_121_03', 3)	# 13-15	 **attackbox here**
    GFX_0('Vat_097asi', -1)
    tag_voice(1, 'uva204_0', 'uva204_1', 'uva204_2', '')
    sprite('Action_121_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_121_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_121_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_121_04', 3)	# 25-27	 **attackbox here**
    label(9)
    sprite('keep', 1)	# 28-28
    clearUponHandler(43)
    sprite('Action_121_05', 4)	# 29-32	 **attackbox here**
    sprite('Action_121_03', 4)	# 33-36	 **attackbox here**
    sprite('Action_121_04', 4)	# 37-40	 **attackbox here**
    sprite('Action_121_05', 4)	# 41-44	 **attackbox here**
    sprite('Action_121_03', 4)	# 45-48	 **attackbox here**
    sprite('Action_121_04', 4)	# 49-52	 **attackbox here**
    sprite('Action_121_09', 4)	# 53-56	 **attackbox here**
    sprite('Action_121_10', 4)	# 57-60	 **attackbox here**
    sprite('Action_121_11', 4)	# 61-64	 **attackbox here**

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(500)
        AttackP1(70)
        Unknown11092(1)
        Hitstop(4)
        PushbackX(15300)
        AirPushbackX(10000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(1600)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11042(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11056(0)

        def upon_78():
            Unknown2037(1)
    sprite('Action_045_01', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(30000)
    Unknown1019(110)
    sprite('Action_403_00', 4)	# 3-6	 **attackbox here**
    sprite('Action_403_01', 4)	# 7-10	 **attackbox here**
    tag_voice(1, 'uva108_0', 'uva108_1', 'uva108_2', '')
    sprite('Action_403_02', 3)	# 11-13
    GFX_0('Vat_191', -1)
    Unknown38(4, 1)
    Unknown36(4)
    teleportRelativeX(23000)
    Unknown1007(23000)
    Unknown1072(-9500)
    Unknown35()
    SFX_3('SE_SwingLightSword')
    sprite('Action_403_03ex', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_403_04ex', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_05ex', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_06ex', 1)	# 23-23	 **attackbox here**
    RefreshMultihit()
    Unknown1019(20)
    sprite('Action_403_07ex', 1)	# 24-24	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(30000)
    sprite('Action_403_08', 1)	# 25-25	 **attackbox here**
    sprite('Action_403_09', 3)	# 26-28
    sprite('Action_404_00', 4)	# 29-32	 **attackbox here**
    Unknown13(4)
    sprite('Action_404_01', 4)	# 33-36	 **attackbox here**
    sprite('Action_404_02', 6)	# 37-42	 **attackbox here**
    if SLOT_2:
        sendToLabel(99)
    sprite('Action_404_03', 6)	# 43-48	 **attackbox here**
    Unknown1084(1)
    sprite('Action_404_04', 6)	# 49-54	 **attackbox here**
    ExitState()
    label(99)
    sprite('Action_184_00', 3)	# 55-57	 **attackbox here**

    def upon_LANDING():
        sendToLabel(1)
    JumpCancel_(0)
    Unknown2003(1)
    Unknown1084(1)
    sprite('Action_184_01', 3)	# 58-60	 **attackbox here**
    sprite('Action_184_02', 3)	# 61-63	 **attackbox here**
    SFX_4('uva209')
    sprite('Action_184_03', 3)	# 64-66	 **attackbox here**
    sprite('Action_184_04', 3)	# 67-69	 **attackbox here**
    sprite('Action_184_05', 3)	# 70-72	 **attackbox here**
    sprite('Action_184_05', 1)	# 73-73	 **attackbox here**
    GFX_0('Vat_187', 0)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    sprite('Action_184_06', 2)	# 74-75	 **attackbox here**
    sprite('Action_184_07', 2)	# 76-77	 **attackbox here**
    sprite('Action_184_08', 3)	# 78-80	 **attackbox here**
    physicsXImpulse(-3500)
    physicsYImpulse(7000)
    setGravity(600)
    sprite('Action_184_09', 4)	# 81-84	 **attackbox here**
    Unknown2063()
    label(0)
    sprite('Action_184_10', 4)	# 85-88	 **attackbox here**
    sprite('Action_184_11', 4)	# 89-92	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_184_12', 2)	# 93-94	 **attackbox here**
    sprite('Action_184_12', 2)	# 95-96	 **attackbox here**
    Unknown8000(100, 1, 1)
    sprite('Action_184_13', 3)	# 97-99	 **attackbox here**
    sprite('Action_184_14', 2)	# 100-101	 **attackbox here**

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
    Unknown2036(92, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-500000)
    Unknown1019(4)
    label(0)
    sprite('Action_022_00', 4)	# 3-6	 **attackbox here**
    sprite('Action_022_01', 4)	# 7-10	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateShotDDDOD')
    else:
        enterState('UltimateShotDDD')

@State
def UltimateShotDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        Unknown1084(1)
        setInvincible(1)
        loopRelated(17, 183)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
    sprite('Action_225_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_225_00', 3)	# 4-6	 **attackbox here**
    SFX_3('SE_SpecialLaserBeam')
    sprite('Action_225_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_225_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_225_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_225_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_225_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_225_06', 3)	# 22-24	 **attackbox here**
    GFX_0('Vat_226', -1)
    Unknown23029(1, 2002, 0)
    sprite('Action_225_07', 3)	# 25-27
    sprite('Action_225_08', 4)	# 28-31
    sprite('Action_225_09', 4)	# 32-35
    sprite('Action_225_10', 4)	# 36-39
    sprite('Action_225_11', 4)	# 40-43
    sprite('Action_225_12', 4)	# 44-47
    sprite('Action_225_13', 4)	# 48-51
    sprite('Action_225_11', 4)	# 52-55
    GFX_0('Vat_228', -1)
    sprite('Action_225_12', 4)	# 56-59
    sprite('Action_225_13', 4)	# 60-63
    sprite('Action_225_11', 4)	# 64-67
    sprite('Action_225_12', 4)	# 68-71
    Unknown1045(-30000)
    sprite('Action_225_13', 4)	# 72-75
    setInvincible(0)
    label(0)
    sprite('Action_225_11', 4)	# 76-79
    sprite('Action_225_12', 4)	# 80-83
    sprite('Action_225_13', 4)	# 84-87
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_225_11', 4)	# 88-91
    Unknown1084(1)
    GFX_0('Vat_228_END', -1)
    Unknown21015('5661745f32323600000000000000000000000000000000000000000000000000d007000000000000')
    sprite('Action_225_12', 4)	# 92-95
    sprite('Action_225_13', 4)	# 96-99
    sprite('Action_225_11', 4)	# 100-103
    sprite('Action_225_12', 4)	# 104-107
    sprite('Action_225_13', 4)	# 108-111
    sprite('Action_225_11', 4)	# 112-115
    sprite('Action_225_12', 4)	# 116-119
    sprite('Action_225_13', 4)	# 120-123
    sprite('Action_225_17', 4)	# 124-127
    sprite('Action_225_18', 4)	# 128-131	 **attackbox here**
    sprite('Action_225_19', 4)	# 132-135	 **attackbox here**
    sprite('Action_225_20', 4)	# 136-139	 **attackbox here**
    sprite('Action_225_21', 4)	# 140-143	 **attackbox here**
    sprite('Action_225_22', 3)	# 144-146	 **attackbox here**

@State
def UltimateShotDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        Unknown1084(1)
        setInvincible(1)
        loopRelated(17, 213)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(9)
    sprite('Action_225_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_225_00', 3)	# 4-6	 **attackbox here**
    SFX_3('SE_SpecialLaserBeam')
    sprite('Action_225_01', 3)	# 7-9	 **attackbox here**
    sprite('Action_225_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_225_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_225_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_225_05', 3)	# 19-21	 **attackbox here**
    sprite('Action_225_06', 3)	# 22-24	 **attackbox here**
    GFX_0('Vat_226', -1)
    Unknown23029(1, 2003, 0)
    sprite('Action_225_07', 3)	# 25-27
    sprite('Action_225_08', 4)	# 28-31
    sprite('Action_225_09', 4)	# 32-35
    sprite('Action_225_10', 4)	# 36-39
    sprite('Action_225_11', 4)	# 40-43
    sprite('Action_225_12', 4)	# 44-47
    sprite('Action_225_13', 4)	# 48-51
    sprite('Action_225_11', 4)	# 52-55
    GFX_0('Vat_228', -1)
    sprite('Action_225_12', 4)	# 56-59
    sprite('Action_225_13', 4)	# 60-63
    sprite('Action_225_11', 4)	# 64-67
    sprite('Action_225_12', 4)	# 68-71
    Unknown1045(-30000)
    sprite('Action_225_13', 4)	# 72-75
    setInvincible(0)
    label(0)
    sprite('Action_225_11', 4)	# 76-79
    sprite('Action_225_12', 4)	# 80-83
    sprite('Action_225_13', 4)	# 84-87
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_225_11', 4)	# 88-91
    Unknown1084(1)
    GFX_0('Vat_228_END', -1)
    Unknown21015('5661745f32323600000000000000000000000000000000000000000000000000d007000000000000')
    sprite('Action_225_12', 4)	# 92-95
    sprite('Action_225_13', 4)	# 96-99
    sprite('Action_225_11', 4)	# 100-103
    sprite('Action_225_12', 4)	# 104-107
    sprite('Action_225_13', 4)	# 108-111
    sprite('Action_225_11', 4)	# 112-115
    sprite('Action_225_12', 4)	# 116-119
    sprite('Action_225_13', 4)	# 120-123
    sprite('Action_225_17', 4)	# 124-127
    sprite('Action_225_18', 4)	# 128-131	 **attackbox here**
    sprite('Action_225_19', 4)	# 132-135	 **attackbox here**
    sprite('Action_225_20', 4)	# 136-139	 **attackbox here**
    sprite('Action_225_21', 4)	# 140-143	 **attackbox here**
    sprite('Action_225_22', 3)	# 144-146	 **attackbox here**

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 2)	# 121-122
    sprite('null', 4)	# 123-126
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-500000)
    Unknown1007(2400000)
    physicsXImpulse(20000)
    physicsYImpulse(-96000)
    setGravity(0)
    sendToLabelUpon(2, 9)
    sprite('Action_009_02', 4)	# 127-130
    GFX_0('Vat_191', -1)
    Unknown36(1)
    teleportRelativeX(23000)
    Unknown1007(23000)
    Unknown1072(-10000)
    Unknown35()
    SFX_3('SE_SwingLightSword')
    label(1)
    sprite('Action_009_03', 2)	# 131-132	 **attackbox here**
    sprite('Action_009_04', 2)	# 133-134	 **attackbox here**
    sprite('Action_009_05', 2)	# 135-136	 **attackbox here**
    sprite('Action_009_06', 2)	# 137-138	 **attackbox here**
    sprite('Action_009_07', 2)	# 139-140	 **attackbox here**
    gotoLabel(1)
    label(9)
    clearUponHandler(2)
    sprite('Action_009_03', 3)	# 141-143	 **attackbox here**
    sprite('Action_037_12', 8)	# 144-151	 **attackbox here**
    Unknown26('Vat_191')
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_037_13', 14)	# 152-165	 **attackbox here**
    sprite('Action_037_14', 9)	# 166-174	 **attackbox here**

@Subroutine
def MouthTableInit():
    Unknown18011('uva000', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva500', 12643, 12641, 25396, 24887, 25398, 24886, 25398, 24886, 13361, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva502', 12643, 24880, 12345, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva504', 12643, 14177, 14179, 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva505', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva520', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva521', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 13361, 14179, 12641, 25394, 24887, 25399, 14134, 12897, 25397, 24887, 13618, 14179, 12897, 25397, 24887, 13618, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva522', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24888, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva524', 12643, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14691, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva525', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva402_1', 12643, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva403_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva600brc', 12643, 14177, 14179, 14177, 14179, 12641, 25396, 24887, 25399, 14134, 12641, 12336, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva600ume', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601bes', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601bno', 12643, 12641, 12336, 13923, 24880, 13361, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601rwi', 12643, 24880, 12337, 25392, 12342, 14177, 14179, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva601uli', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva603bes', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva603bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva605bes', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva700bes', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva700brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 24882, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva700bno', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 14129, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva700pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva700rrb', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva700rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva701bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 13361, 14179, 12641, 25396, 24887, 13361, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva701uhy', 12643, 12641, 25394, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva701uli', 12643, 14177, 14179, 14177, 13667, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13620, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uva701ume', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12343, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('brc')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bny')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pag')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('ume')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    sprite('Action_050_00', 4)	# 2-5
    Unknown2019(0)
    sprite('Action_050_01', 4)	# 6-9
    sprite('Action_050_02', 4)	# 10-13
    sprite('Action_050_03', 4)	# 14-17
    sprite('Action_050_04', 4)	# 18-21
    sprite('Action_050_05', 4)	# 22-25
    sprite('Action_050_06', 4)	# 26-29
    sprite('Action_050_07', 4)	# 30-33
    sprite('Action_050_08', 5)	# 34-38
    sprite('Action_050_09', 5)	# 39-43
    sprite('Action_050_10', 5)	# 44-48
    if random_(2, 0, 83):
        if random_(2, 0, 50):
            Unknown7006('uva500', 100, 895579765, 12592, 0, 0, 100, 895579765, 13104, 0, 0, 100, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uva504', 100, 895579765, 13616, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown2037(1)
    sprite('Action_050_11', 5)	# 49-53
    SFX_3('SE_MagicExist')
    GFX_0('Entry', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry2', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry3', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    sprite('Action_050_12', 4)	# 54-57	 **attackbox here**
    GFX_0('Vat_skirt', 100)
    sprite('Action_050_13', 4)	# 58-61	 **attackbox here**
    sprite('Action_050_14', 4)	# 62-65	 **attackbox here**
    sprite('Action_050_15', 4)	# 66-69	 **attackbox here**
    sprite('Action_050_16', 4)	# 70-73	 **attackbox here**
    sprite('Action_050_17', 4)	# 74-77	 **attackbox here**
    sprite('Action_050_18', 4)	# 78-81	 **attackbox here**
    sprite('Action_050_19', 4)	# 82-85	 **attackbox here**
    sprite('Action_050_20', 4)	# 86-89	 **attackbox here**
    sprite('Action_050_21', 4)	# 90-93	 **attackbox here**
    sprite('Action_050_22', 4)	# 94-97	 **attackbox here**
    sprite('Action_050_23', 4)	# 98-101	 **attackbox here**
    sprite('Action_050_24', 4)	# 102-105	 **attackbox here**
    sprite('Action_050_25', 4)	# 106-109	 **attackbox here**
    sprite('Action_050_26', 4)	# 110-113	 **attackbox here**
    sprite('Action_050_27', 4)	# 114-117	 **attackbox here**
    sprite('Action_050_28', 4)	# 118-121	 **attackbox here**
    sprite('Action_050_29', 4)	# 122-125	 **attackbox here**
    sprite('Action_050_30', 4)	# 126-129	 **attackbox here**
    sprite('Action_050_31', 4)	# 130-133	 **attackbox here**
    sprite('Action_050_32', 4)	# 134-137	 **attackbox here**
    sprite('Action_050_33', 4)	# 138-141	 **attackbox here**
    sprite('Action_050_34', 4)	# 142-145	 **attackbox here**
    sprite('Action_050_35', 4)	# 146-149	 **attackbox here**
    sprite('Action_050_36', 4)	# 150-153	 **attackbox here**
    sprite('Action_050_38', 4)	# 154-157	 **attackbox here**
    sprite('Action_050_39', 4)	# 158-161	 **attackbox here**
    sprite('Action_050_40', 4)	# 162-165	 **attackbox here**
    sprite('Action_050_41', 4)	# 166-169	 **attackbox here**
    sprite('Action_050_43', 4)	# 170-173	 **attackbox here**
    GFX_0('Vat_Wing', 100)
    sprite('Action_050_44', 4)	# 174-177	 **attackbox here**
    sprite('Action_050_45', 4)	# 178-181	 **attackbox here**
    sprite('Action_050_46', 4)	# 182-185	 **attackbox here**
    sprite('Action_050_47', 4)	# 186-189	 **attackbox here**
    sprite('Action_050_48', 4)	# 190-193	 **attackbox here**
    sprite('Action_050_49', 4)	# 194-197	 **attackbox here**
    sprite('Action_050_50', 4)	# 198-201	 **attackbox here**
    sprite('Action_050_51', 4)	# 202-205	 **attackbox here**
    sprite('Action_050_52', 4)	# 206-209	 **attackbox here**
    sprite('Action_050_53', 4)	# 210-213	 **attackbox here**
    sprite('Action_050_54', 3)	# 214-216
    sprite('Action_050_55', 5)	# 217-221
    sprite('Action_050_56', 6)	# 222-227
    sprite('Action_050_57', 7)	# 228-234
    if SLOT_2:
        SFX_1('uva502')
    sprite('Action_050_58', 7)	# 235-241
    sprite('Action_050_59', 7)	# 242-248
    sprite('Action_050_60', 7)	# 249-255
    sprite('Action_050_61', 5)	# 256-260
    sprite('Action_050_62', 5)	# 261-265
    sprite('Action_050_63', 7)	# 266-272
    sprite('Action_050_64', 5)	# 273-277
    sprite('Action_050_65', 5)	# 278-282
    sprite('Action_050_66', 5)	# 283-287
    Unknown23018(1)
    label(2)
    sprite('Action_000_01', 5)	# 288-292	 **attackbox here**
    sprite('Action_000_02', 5)	# 293-297	 **attackbox here**
    sprite('Action_000_03', 5)	# 298-302	 **attackbox here**
    sprite('Action_000_04', 5)	# 303-307	 **attackbox here**
    sprite('Action_000_05', 5)	# 308-312	 **attackbox here**
    sprite('Action_000_06', 5)	# 313-317	 **attackbox here**
    sprite('Action_000_07', 5)	# 318-322	 **attackbox here**
    sprite('Action_000_08', 5)	# 323-327	 **attackbox here**
    sprite('Action_000_09', 5)	# 328-332	 **attackbox here**
    sprite('Action_000_10', 5)	# 333-337	 **attackbox here**
    sprite('Action_000_11', 5)	# 338-342	 **attackbox here**
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('Action_000_00', 32767)	# 343-33109	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_050_00', 1)	# 33110-33110
    Unknown2019(0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Action_050_00', 4)	# 33111-33114
    sprite('Action_050_01', 4)	# 33115-33118
    sprite('Action_050_02', 4)	# 33119-33122
    sprite('Action_050_03', 4)	# 33123-33126
    sprite('Action_050_04', 4)	# 33127-33130
    sprite('Action_050_05', 4)	# 33131-33134
    gotoLabel(101)
    label(102)
    sprite('Action_050_07', 4)	# 33135-33138
    sprite('Action_050_08', 5)	# 33139-33143
    sprite('Action_050_09', 5)	# 33144-33148
    sprite('Action_050_10', 5)	# 33149-33153
    sprite('Action_050_11', 5)	# 33154-33158
    SFX_3('SE_MagicExist')
    GFX_0('Entry', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry2', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry3', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    sprite('Action_050_12', 4)	# 33159-33162	 **attackbox here**
    GFX_0('Vat_skirt', 100)
    sprite('Action_050_13', 4)	# 33163-33166	 **attackbox here**
    sprite('Action_050_14', 4)	# 33167-33170	 **attackbox here**
    sprite('Action_050_15', 4)	# 33171-33174	 **attackbox here**
    sprite('Action_050_16', 4)	# 33175-33178	 **attackbox here**
    sprite('Action_050_17', 4)	# 33179-33182	 **attackbox here**
    sprite('Action_050_18', 4)	# 33183-33186	 **attackbox here**
    sprite('Action_050_19', 4)	# 33187-33190	 **attackbox here**
    sprite('Action_050_20', 4)	# 33191-33194	 **attackbox here**
    sprite('Action_050_21', 4)	# 33195-33198	 **attackbox here**
    sprite('Action_050_22', 4)	# 33199-33202	 **attackbox here**
    sprite('Action_050_23', 4)	# 33203-33206	 **attackbox here**
    sprite('Action_050_24', 4)	# 33207-33210	 **attackbox here**
    sprite('Action_050_25', 4)	# 33211-33214	 **attackbox here**
    sprite('Action_050_26', 4)	# 33215-33218	 **attackbox here**
    sprite('Action_050_27', 4)	# 33219-33222	 **attackbox here**
    sprite('Action_050_28', 4)	# 33223-33226	 **attackbox here**
    sprite('Action_050_29', 4)	# 33227-33230	 **attackbox here**
    sprite('Action_050_30', 4)	# 33231-33234	 **attackbox here**
    sprite('Action_050_31', 4)	# 33235-33238	 **attackbox here**
    sprite('Action_050_32', 4)	# 33239-33242	 **attackbox here**
    sprite('Action_050_33', 4)	# 33243-33246	 **attackbox here**
    sprite('Action_050_34', 4)	# 33247-33250	 **attackbox here**
    sprite('Action_050_35', 4)	# 33251-33254	 **attackbox here**
    sprite('Action_050_36', 4)	# 33255-33258	 **attackbox here**
    sprite('Action_050_38', 4)	# 33259-33262	 **attackbox here**
    sprite('Action_050_39', 4)	# 33263-33266	 **attackbox here**
    sprite('Action_050_40', 4)	# 33267-33270	 **attackbox here**
    sprite('Action_050_41', 4)	# 33271-33274	 **attackbox here**
    sprite('Action_050_43', 4)	# 33275-33278	 **attackbox here**
    GFX_0('Vat_Wing', 100)
    sprite('Action_050_44', 4)	# 33279-33282	 **attackbox here**
    sprite('Action_050_45', 4)	# 33283-33286	 **attackbox here**
    sprite('Action_050_46', 4)	# 33287-33290	 **attackbox here**
    sprite('Action_050_47', 4)	# 33291-33294	 **attackbox here**
    sprite('Action_050_48', 4)	# 33295-33298	 **attackbox here**
    sprite('Action_050_49', 4)	# 33299-33302	 **attackbox here**
    sprite('Action_050_50', 4)	# 33303-33306	 **attackbox here**
    sprite('Action_050_51', 4)	# 33307-33310	 **attackbox here**
    sprite('Action_050_52', 4)	# 33311-33314	 **attackbox here**
    sprite('Action_050_53', 4)	# 33315-33318	 **attackbox here**
    sprite('Action_050_54', 3)	# 33319-33321
    sprite('Action_050_55', 5)	# 33322-33326
    sprite('Action_050_56', 6)	# 33327-33332
    sprite('Action_050_57', 7)	# 33333-33339
    SFX_1('uva601bno')
    sprite('Action_050_58', 7)	# 33340-33346
    sprite('Action_050_59', 7)	# 33347-33353
    sprite('Action_050_60', 7)	# 33354-33360
    sprite('Action_050_61', 5)	# 33361-33365
    sprite('Action_050_62', 5)	# 33366-33370
    sprite('Action_050_63', 7)	# 33371-33377
    sprite('Action_050_64', 5)	# 33378-33382
    sprite('Action_050_65', 5)	# 33383-33387
    sprite('Action_050_66', 5)	# 33388-33392
    Unknown23018(1)
    label(103)
    sprite('Action_000_01', 5)	# 33393-33397	 **attackbox here**
    sprite('Action_000_02', 5)	# 33398-33402	 **attackbox here**
    sprite('Action_000_03', 5)	# 33403-33407	 **attackbox here**
    sprite('Action_000_04', 5)	# 33408-33412	 **attackbox here**
    sprite('Action_000_05', 5)	# 33413-33417	 **attackbox here**
    sprite('Action_000_06', 5)	# 33418-33422	 **attackbox here**
    sprite('Action_000_07', 5)	# 33423-33427	 **attackbox here**
    sprite('Action_000_08', 5)	# 33428-33432	 **attackbox here**
    sprite('Action_000_09', 5)	# 33433-33437	 **attackbox here**
    sprite('Action_000_10', 5)	# 33438-33442	 **attackbox here**
    sprite('Action_000_11', 5)	# 33443-33447	 **attackbox here**
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('Action_050_00', 4)	# 33448-33451
    Unknown2019(0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 4)	# 33452-33455
    sprite('Action_050_02', 4)	# 33456-33459
    sprite('Action_050_03', 4)	# 33460-33463
    sprite('Action_050_04', 4)	# 33464-33467
    sprite('Action_050_05', 4)	# 33468-33471
    sprite('Action_050_06', 4)	# 33472-33475
    sprite('Action_050_07', 4)	# 33476-33479
    sprite('Action_050_08', 5)	# 33480-33484
    sprite('Action_050_09', 5)	# 33485-33489
    sprite('Action_050_10', 5)	# 33490-33494
    sprite('Action_050_11', 5)	# 33495-33499
    SFX_3('SE_MagicExist')
    GFX_0('Entry', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry2', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry3', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    sprite('Action_050_12', 4)	# 33500-33503	 **attackbox here**
    GFX_0('Vat_skirt', 100)
    sprite('Action_050_13', 4)	# 33504-33507	 **attackbox here**
    sprite('Action_050_14', 4)	# 33508-33511	 **attackbox here**
    sprite('Action_050_15', 4)	# 33512-33515	 **attackbox here**
    sprite('Action_050_16', 4)	# 33516-33519	 **attackbox here**
    sprite('Action_050_17', 4)	# 33520-33523	 **attackbox here**
    sprite('Action_050_18', 4)	# 33524-33527	 **attackbox here**
    sprite('Action_050_19', 4)	# 33528-33531	 **attackbox here**
    SFX_1('uva600brc')
    sprite('Action_050_20', 4)	# 33532-33535	 **attackbox here**
    sprite('Action_050_21', 4)	# 33536-33539	 **attackbox here**
    sprite('Action_050_22', 4)	# 33540-33543	 **attackbox here**
    sprite('Action_050_23', 4)	# 33544-33547	 **attackbox here**
    sprite('Action_050_24', 4)	# 33548-33551	 **attackbox here**
    sprite('Action_050_25', 4)	# 33552-33555	 **attackbox here**
    sprite('Action_050_26', 4)	# 33556-33559	 **attackbox here**
    sprite('Action_050_27', 4)	# 33560-33563	 **attackbox here**
    sprite('Action_050_28', 4)	# 33564-33567	 **attackbox here**
    sprite('Action_050_29', 4)	# 33568-33571	 **attackbox here**
    sprite('Action_050_30', 4)	# 33572-33575	 **attackbox here**
    sprite('Action_050_31', 4)	# 33576-33579	 **attackbox here**
    sprite('Action_050_32', 4)	# 33580-33583	 **attackbox here**
    sprite('Action_050_33', 4)	# 33584-33587	 **attackbox here**
    sprite('Action_050_34', 4)	# 33588-33591	 **attackbox here**
    sprite('Action_050_35', 4)	# 33592-33595	 **attackbox here**
    sprite('Action_050_36', 4)	# 33596-33599	 **attackbox here**
    sprite('Action_050_38', 4)	# 33600-33603	 **attackbox here**
    sprite('Action_050_39', 4)	# 33604-33607	 **attackbox here**
    sprite('Action_050_40', 4)	# 33608-33611	 **attackbox here**
    sprite('Action_050_41', 4)	# 33612-33615	 **attackbox here**
    sprite('Action_050_43', 4)	# 33616-33619	 **attackbox here**
    GFX_0('Vat_Wing', 100)
    sprite('Action_050_44', 4)	# 33620-33623	 **attackbox here**
    sprite('Action_050_45', 4)	# 33624-33627	 **attackbox here**
    sprite('Action_050_46', 4)	# 33628-33631	 **attackbox here**
    sprite('Action_050_47', 4)	# 33632-33635	 **attackbox here**
    sprite('Action_050_48', 4)	# 33636-33639	 **attackbox here**
    sprite('Action_050_49', 4)	# 33640-33643	 **attackbox here**
    sprite('Action_050_50', 4)	# 33644-33647	 **attackbox here**
    sprite('Action_050_51', 4)	# 33648-33651	 **attackbox here**
    sprite('Action_050_52', 4)	# 33652-33655	 **attackbox here**
    sprite('Action_050_53', 4)	# 33656-33659	 **attackbox here**
    sprite('Action_050_54', 3)	# 33660-33662
    sprite('Action_050_55', 5)	# 33663-33667
    sprite('Action_050_56', 6)	# 33668-33673
    sprite('Action_050_57', 7)	# 33674-33680
    sprite('Action_050_58', 7)	# 33681-33687
    sprite('Action_050_59', 7)	# 33688-33694
    sprite('Action_050_60', 7)	# 33695-33701
    sprite('Action_050_61', 5)	# 33702-33706
    sprite('Action_050_62', 5)	# 33707-33711
    sprite('Action_050_63', 7)	# 33712-33718
    sprite('Action_050_64', 5)	# 33719-33723
    sprite('Action_050_65', 5)	# 33724-33728
    sprite('Action_050_66', 5)	# 33729-33733
    Unknown21007(24, 40)
    Unknown21011(240)
    label(111)
    sprite('Action_000_01', 5)	# 33734-33738	 **attackbox here**
    sprite('Action_000_02', 5)	# 33739-33743	 **attackbox here**
    sprite('Action_000_03', 5)	# 33744-33748	 **attackbox here**
    sprite('Action_000_04', 5)	# 33749-33753	 **attackbox here**
    sprite('Action_000_05', 5)	# 33754-33758	 **attackbox here**
    sprite('Action_000_06', 5)	# 33759-33763	 **attackbox here**
    sprite('Action_000_07', 5)	# 33764-33768	 **attackbox here**
    sprite('Action_000_08', 5)	# 33769-33773	 **attackbox here**
    sprite('Action_000_09', 5)	# 33774-33778	 **attackbox here**
    sprite('Action_000_10', 5)	# 33779-33783	 **attackbox here**
    sprite('Action_000_11', 5)	# 33784-33788	 **attackbox here**
    gotoLabel(111)
    ExitState()
    label(120)
    sprite('Action_113_14_Vat633_00', 1)	# 33789-33789	 **attackbox here**
    Unknown2019(-100)
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('Action_113_14_Vat633_00', 6)	# 33790-33795	 **attackbox here**
    sprite('Action_113_14_Vat633_01', 6)	# 33796-33801	 **attackbox here**
    sprite('Action_113_14_Vat633_02', 6)	# 33802-33807	 **attackbox here**
    gotoLabel(121)
    label(122)
    sprite('Action_113_14_Vat633_00', 1)	# 33808-33808	 **attackbox here**
    SFX_1('uva601bny')
    label(123)
    sprite('Action_113_14_Vat633_00', 6)	# 33809-33814	 **attackbox here**
    sprite('Action_113_14_Vat633_01', 6)	# 33815-33820	 **attackbox here**
    sprite('Action_113_14_Vat633_02', 6)	# 33821-33826	 **attackbox here**
    if SLOT_97:
        _gotolabel(123)
    sprite('Action_113_14_Vat633_00', 6)	# 33827-33832	 **attackbox here**
    sprite('Action_113_14_Vat633_01', 6)	# 33833-33838	 **attackbox here**
    sprite('Action_113_14_Vat633_02', 6)	# 33839-33844	 **attackbox here**
    sprite('Action_113_14_Vat633_00', 6)	# 33845-33850	 **attackbox here**
    sprite('Action_113_14_Vat633_01', 6)	# 33851-33856	 **attackbox here**
    sprite('Action_113_14_Vat633_02', 6)	# 33857-33862	 **attackbox here**
    sprite('Action_113_14_Vat633_00', 6)	# 33863-33868	 **attackbox here**
    sprite('Action_113_14_Vat633_01', 6)	# 33869-33874	 **attackbox here**
    sprite('Action_113_14_Vat633_02', 6)	# 33875-33880	 **attackbox here**
    sprite('Action_113_14_Vat633_03', 4)	# 33881-33884	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_113_13_Vat633_04', 6)	# 33885-33890	 **attackbox here**
    sprite('Action_113_12_Vat633_05', 6)	# 33891-33896	 **attackbox here**
    SFX_1('uva603bny')
    sprite('Action_113_12_Vat633_06', 6)	# 33897-33902	 **attackbox here**
    sprite('Action_113_12_Vat633_07', 6)	# 33903-33908	 **attackbox here**
    Unknown23018(1)
    label(124)
    sprite('Action_113_12_Vat633_05', 6)	# 33909-33914	 **attackbox here**
    sprite('Action_113_12_Vat633_06', 6)	# 33915-33920	 **attackbox here**
    sprite('Action_113_12_Vat633_07', 6)	# 33921-33926	 **attackbox here**
    loopRest()
    gotoLabel(124)
    ExitState()
    label(130)
    sprite('Action_000_01ex', 1)	# 33927-33927	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)

    def upon_39():
        clearUponHandler(39)
        sendToLabel(136)
    GFX_0('Entry_ES', 100)
    label(131)
    sprite('Action_000_01ex', 5)	# 33928-33932	 **attackbox here**
    sprite('Action_000_02ex', 5)	# 33933-33937	 **attackbox here**
    sprite('Action_000_03ex', 5)	# 33938-33942	 **attackbox here**
    sprite('Action_000_04ex', 5)	# 33943-33947	 **attackbox here**
    sprite('Action_000_05ex', 5)	# 33948-33952	 **attackbox here**
    sprite('Action_000_06ex', 5)	# 33953-33957	 **attackbox here**
    sprite('Action_000_07ex', 5)	# 33958-33962	 **attackbox here**
    sprite('Action_000_08ex', 5)	# 33963-33967	 **attackbox here**
    sprite('Action_000_09ex', 5)	# 33968-33972	 **attackbox here**
    sprite('Action_000_10ex', 5)	# 33973-33977	 **attackbox here**
    sprite('Action_000_11ex', 5)	# 33978-33982	 **attackbox here**
    gotoLabel(131)
    label(132)
    sprite('Action_000_13ex', 5)	# 33983-33987
    sprite('Action_000_14ex', 5)	# 33988-33992
    SFX_1('uva601bes')
    sprite('Action_000_15ex', 6)	# 33993-33998
    sprite('Action_000_16ex', 7)	# 33999-34005	 **attackbox here**
    sprite('Action_000_17ex', 7)	# 34006-34012	 **attackbox here**
    sprite('Action_000_18ex', 7)	# 34013-34019	 **attackbox here**
    sprite('Action_000_19ex', 7)	# 34020-34026	 **attackbox here**
    sprite('Action_000_20ex', 5)	# 34027-34031	 **attackbox here**
    sprite('Action_000_21ex', 6)	# 34032-34037	 **attackbox here**
    sprite('Action_000_22ex', 8)	# 34038-34045	 **attackbox here**
    sprite('Action_000_23ex', 6)	# 34046-34051
    sprite('Action_000_24ex', 5)	# 34052-34056
    sprite('Action_000_25ex', 5)	# 34057-34061
    label(133)
    sprite('Action_000_01ex', 5)	# 34062-34066	 **attackbox here**
    sprite('Action_000_02ex', 5)	# 34067-34071	 **attackbox here**
    sprite('Action_000_03ex', 5)	# 34072-34076	 **attackbox here**
    sprite('Action_000_04ex', 5)	# 34077-34081	 **attackbox here**
    sprite('Action_000_05ex', 5)	# 34082-34086	 **attackbox here**
    sprite('Action_000_06ex', 5)	# 34087-34091	 **attackbox here**
    sprite('Action_000_07ex', 5)	# 34092-34096	 **attackbox here**
    sprite('Action_000_08ex', 5)	# 34097-34101	 **attackbox here**
    sprite('Action_000_09ex', 5)	# 34102-34106	 **attackbox here**
    sprite('Action_000_10ex', 5)	# 34107-34111	 **attackbox here**
    sprite('Action_000_11ex', 5)	# 34112-34116	 **attackbox here**
    if SLOT_97:
        _gotolabel(133)
    sprite('Action_000_01ex', 5)	# 34117-34121	 **attackbox here**
    sprite('Action_000_02ex', 5)	# 34122-34126	 **attackbox here**
    sprite('Action_000_03ex', 5)	# 34127-34131	 **attackbox here**
    sprite('Action_000_04ex', 5)	# 34132-34136	 **attackbox here**
    sprite('Action_000_05ex', 5)	# 34137-34141	 **attackbox here**
    SFX_1('uva603bes')
    Unknown21015('456e7472795f4553000000000000000000000000000000000000000000000000a10f000000000000')
    sprite('Action_225_00ex', 6)	# 34142-34147
    sprite('Action_225_01ex', 6)	# 34148-34153
    sprite('Action_225_02ex', 6)	# 34154-34159
    sprite('Action_225_03ex', 6)	# 34160-34165
    sprite('Action_225_01ex', 6)	# 34166-34171
    sprite('Action_225_02ex', 6)	# 34172-34177
    sprite('Action_225_03ex', 6)	# 34178-34183
    sprite('Action_225_04ex', 6)	# 34184-34189
    sprite('Action_225_05ex', 6)	# 34190-34195
    sprite('Action_225_06ex', 6)	# 34196-34201
    label(134)
    sprite('Action_225_01ex', 6)	# 34202-34207
    sprite('Action_225_02ex', 6)	# 34208-34213
    sprite('Action_225_03ex', 6)	# 34214-34219
    sprite('Action_225_01ex', 6)	# 34220-34225
    sprite('Action_225_02ex', 6)	# 34226-34231
    sprite('Action_225_03ex', 6)	# 34232-34237
    sprite('Action_225_04ex', 6)	# 34238-34243
    sprite('Action_225_05ex', 6)	# 34244-34249
    sprite('Action_225_06ex', 6)	# 34250-34255
    if SLOT_97:
        _gotolabel(134)
    sprite('Action_225_01ex', 6)	# 34256-34261
    sprite('Action_225_02ex', 6)	# 34262-34267
    Unknown21007(24, 40)
    sprite('Action_225_03ex', 6)	# 34268-34273
    sprite('Action_225_01ex', 6)	# 34274-34279
    sprite('Action_225_02ex', 6)	# 34280-34285
    sprite('Action_225_03ex', 6)	# 34286-34291
    sprite('Action_225_04ex', 6)	# 34292-34297
    sprite('Action_225_05ex', 6)	# 34298-34303
    sprite('Action_225_06ex', 6)	# 34304-34309
    label(135)
    sprite('Action_225_01ex', 6)	# 34310-34315
    sprite('Action_225_02ex', 6)	# 34316-34321
    sprite('Action_225_03ex', 6)	# 34322-34327
    sprite('Action_225_01ex', 6)	# 34328-34333
    sprite('Action_225_02ex', 6)	# 34334-34339
    sprite('Action_225_03ex', 6)	# 34340-34345
    sprite('Action_225_04ex', 6)	# 34346-34351
    sprite('Action_225_05ex', 6)	# 34352-34357
    sprite('Action_225_06ex', 6)	# 34358-34363
    gotoLabel(135)
    label(136)
    sprite('Action_225_01ex', 6)	# 34364-34369
    sprite('Action_225_02ex', 6)	# 34370-34375
    sprite('Action_225_03ex', 6)	# 34376-34381
    sprite('Action_225_01ex', 6)	# 34382-34387
    sprite('Action_225_02ex', 6)	# 34388-34393
    sprite('Action_225_03ex', 6)	# 34394-34399
    sprite('Action_225_04ex', 6)	# 34400-34405
    sprite('Action_225_05ex', 6)	# 34406-34411
    sprite('Action_225_06ex', 6)	# 34412-34417
    sprite('Action_225_07', 6)	# 34418-34423
    sprite('Action_225_08', 6)	# 34424-34429
    sprite('Action_225_09', 6)	# 34430-34435
    sprite('Action_225_10', 6)	# 34436-34441
    Unknown21015('456e7472795f4553000000000000000000000000000000000000000000000000a00f000000000000')
    Unknown21007(24, 39)
    SFX_1('uva605bes')
    sprite('Action_225_11', 6)	# 34442-34447
    sprite('Action_225_12', 6)	# 34448-34453
    sprite('Action_225_19', 6)	# 34454-34459	 **attackbox here**
    sprite('Action_225_20', 6)	# 34460-34465	 **attackbox here**
    sprite('Action_225_21', 6)	# 34466-34471	 **attackbox here**
    sprite('Action_225_22', 6)	# 34472-34477	 **attackbox here**
    Unknown23018(1)
    label(137)
    sprite('Action_000_01', 5)	# 34478-34482	 **attackbox here**
    sprite('Action_000_02', 5)	# 34483-34487	 **attackbox here**
    sprite('Action_000_03', 5)	# 34488-34492	 **attackbox here**
    sprite('Action_000_04', 5)	# 34493-34497	 **attackbox here**
    sprite('Action_000_05', 5)	# 34498-34502	 **attackbox here**
    sprite('Action_000_06', 5)	# 34503-34507	 **attackbox here**
    sprite('Action_000_07', 5)	# 34508-34512	 **attackbox here**
    sprite('Action_000_08', 5)	# 34513-34517	 **attackbox here**
    sprite('Action_000_09', 5)	# 34518-34522	 **attackbox here**
    sprite('Action_000_10', 5)	# 34523-34527	 **attackbox here**
    sprite('Action_000_11', 5)	# 34528-34532	 **attackbox here**
    gotoLabel(137)
    ExitState()
    label(140)
    sprite('Action_050_00', 1)	# 34533-34533
    Unknown2019(0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('Action_050_00', 4)	# 34534-34537
    sprite('Action_050_01', 4)	# 34538-34541
    sprite('Action_050_02', 4)	# 34542-34545
    sprite('Action_050_03', 4)	# 34546-34549
    sprite('Action_050_04', 4)	# 34550-34553
    sprite('Action_050_05', 4)	# 34554-34557
    gotoLabel(141)
    label(142)
    sprite('Action_050_07', 4)	# 34558-34561
    sprite('Action_050_08', 5)	# 34562-34566
    sprite('Action_050_09', 5)	# 34567-34571
    sprite('Action_050_10', 5)	# 34572-34576
    SFX_1('uva601pag')
    sprite('Action_050_11', 5)	# 34577-34581
    SFX_3('SE_MagicExist')
    GFX_0('Entry', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry2', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry3', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    sprite('Action_050_12', 4)	# 34582-34585	 **attackbox here**
    GFX_0('Vat_skirt', 100)
    sprite('Action_050_13', 4)	# 34586-34589	 **attackbox here**
    sprite('Action_050_14', 4)	# 34590-34593	 **attackbox here**
    sprite('Action_050_15', 4)	# 34594-34597	 **attackbox here**
    sprite('Action_050_16', 4)	# 34598-34601	 **attackbox here**
    sprite('Action_050_17', 4)	# 34602-34605	 **attackbox here**
    sprite('Action_050_18', 4)	# 34606-34609	 **attackbox here**
    sprite('Action_050_19', 4)	# 34610-34613	 **attackbox here**
    sprite('Action_050_20', 4)	# 34614-34617	 **attackbox here**
    sprite('Action_050_21', 4)	# 34618-34621	 **attackbox here**
    sprite('Action_050_22', 4)	# 34622-34625	 **attackbox here**
    sprite('Action_050_23', 4)	# 34626-34629	 **attackbox here**
    sprite('Action_050_24', 4)	# 34630-34633	 **attackbox here**
    sprite('Action_050_25', 4)	# 34634-34637	 **attackbox here**
    sprite('Action_050_26', 4)	# 34638-34641	 **attackbox here**
    sprite('Action_050_27', 4)	# 34642-34645	 **attackbox here**
    sprite('Action_050_28', 4)	# 34646-34649	 **attackbox here**
    sprite('Action_050_29', 4)	# 34650-34653	 **attackbox here**
    sprite('Action_050_30', 4)	# 34654-34657	 **attackbox here**
    sprite('Action_050_31', 4)	# 34658-34661	 **attackbox here**
    sprite('Action_050_32', 4)	# 34662-34665	 **attackbox here**
    sprite('Action_050_33', 4)	# 34666-34669	 **attackbox here**
    sprite('Action_050_34', 4)	# 34670-34673	 **attackbox here**
    sprite('Action_050_35', 4)	# 34674-34677	 **attackbox here**
    sprite('Action_050_36', 4)	# 34678-34681	 **attackbox here**
    sprite('Action_050_38', 4)	# 34682-34685	 **attackbox here**
    sprite('Action_050_39', 4)	# 34686-34689	 **attackbox here**
    sprite('Action_050_40', 4)	# 34690-34693	 **attackbox here**
    sprite('Action_050_41', 4)	# 34694-34697	 **attackbox here**
    sprite('Action_050_43', 4)	# 34698-34701	 **attackbox here**
    GFX_0('Vat_Wing', 100)
    sprite('Action_050_44', 4)	# 34702-34705	 **attackbox here**
    sprite('Action_050_45', 4)	# 34706-34709	 **attackbox here**
    sprite('Action_050_46', 4)	# 34710-34713	 **attackbox here**
    sprite('Action_050_47', 4)	# 34714-34717	 **attackbox here**
    sprite('Action_050_48', 4)	# 34718-34721	 **attackbox here**
    sprite('Action_050_49', 4)	# 34722-34725	 **attackbox here**
    sprite('Action_050_50', 4)	# 34726-34729	 **attackbox here**
    sprite('Action_050_51', 4)	# 34730-34733	 **attackbox here**
    sprite('Action_050_52', 4)	# 34734-34737	 **attackbox here**
    sprite('Action_050_53', 4)	# 34738-34741	 **attackbox here**
    sprite('Action_050_54', 3)	# 34742-34744
    sprite('Action_050_55', 5)	# 34745-34749
    sprite('Action_050_56', 6)	# 34750-34755
    sprite('Action_050_57', 7)	# 34756-34762
    sprite('Action_050_58', 7)	# 34763-34769
    sprite('Action_050_59', 7)	# 34770-34776
    sprite('Action_050_60', 7)	# 34777-34783
    sprite('Action_050_61', 5)	# 34784-34788
    sprite('Action_050_62', 5)	# 34789-34793
    sprite('Action_050_63', 7)	# 34794-34800
    sprite('Action_050_64', 5)	# 34801-34805
    sprite('Action_050_65', 5)	# 34806-34810
    sprite('Action_050_66', 5)	# 34811-34815
    Unknown23018(1)
    label(143)
    sprite('Action_000_01', 5)	# 34816-34820	 **attackbox here**
    sprite('Action_000_02', 5)	# 34821-34825	 **attackbox here**
    sprite('Action_000_03', 5)	# 34826-34830	 **attackbox here**
    sprite('Action_000_04', 5)	# 34831-34835	 **attackbox here**
    sprite('Action_000_05', 5)	# 34836-34840	 **attackbox here**
    sprite('Action_000_06', 5)	# 34841-34845	 **attackbox here**
    sprite('Action_000_07', 5)	# 34846-34850	 **attackbox here**
    sprite('Action_000_08', 5)	# 34851-34855	 **attackbox here**
    sprite('Action_000_09', 5)	# 34856-34860	 **attackbox here**
    sprite('Action_000_10', 5)	# 34861-34865	 **attackbox here**
    sprite('Action_000_11', 5)	# 34866-34870	 **attackbox here**
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('Action_000_00', 1)	# 34871-34871	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('Action_000_01', 5)	# 34872-34876	 **attackbox here**
    sprite('Action_000_02', 5)	# 34877-34881	 **attackbox here**
    sprite('Action_000_03', 5)	# 34882-34886	 **attackbox here**
    sprite('Action_000_04', 5)	# 34887-34891	 **attackbox here**
    sprite('Action_000_05', 5)	# 34892-34896	 **attackbox here**
    sprite('Action_000_06', 5)	# 34897-34901	 **attackbox here**
    sprite('Action_000_07', 5)	# 34902-34906	 **attackbox here**
    sprite('Action_000_08', 5)	# 34907-34911	 **attackbox here**
    sprite('Action_000_09', 5)	# 34912-34916	 **attackbox here**
    sprite('Action_000_10', 5)	# 34917-34921	 **attackbox here**
    sprite('Action_000_11', 5)	# 34922-34926	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('Action_000_13', 5)	# 34927-34931	 **attackbox here**
    sprite('Action_000_14', 5)	# 34932-34936	 **attackbox here**
    SFX_1('uva601uhy')
    sprite('Action_000_15', 6)	# 34937-34942	 **attackbox here**
    sprite('Action_000_16', 7)	# 34943-34949	 **attackbox here**
    sprite('Action_000_17', 7)	# 34950-34956	 **attackbox here**
    sprite('Action_000_18', 7)	# 34957-34963	 **attackbox here**
    sprite('Action_000_19', 7)	# 34964-34970	 **attackbox here**
    sprite('Action_000_20', 5)	# 34971-34975	 **attackbox here**
    sprite('Action_000_21', 6)	# 34976-34981	 **attackbox here**
    sprite('Action_000_22', 8)	# 34982-34989	 **attackbox here**
    sprite('Action_000_23', 6)	# 34990-34995	 **attackbox here**
    sprite('Action_000_24', 5)	# 34996-35000	 **attackbox here**
    sprite('Action_000_25', 5)	# 35001-35005	 **attackbox here**
    Unknown23018(1)
    label(153)
    sprite('Action_000_01', 5)	# 35006-35010	 **attackbox here**
    sprite('Action_000_02', 5)	# 35011-35015	 **attackbox here**
    sprite('Action_000_03', 5)	# 35016-35020	 **attackbox here**
    sprite('Action_000_04', 5)	# 35021-35025	 **attackbox here**
    sprite('Action_000_05', 5)	# 35026-35030	 **attackbox here**
    sprite('Action_000_06', 5)	# 35031-35035	 **attackbox here**
    sprite('Action_000_07', 5)	# 35036-35040	 **attackbox here**
    sprite('Action_000_08', 5)	# 35041-35045	 **attackbox here**
    sprite('Action_000_09', 5)	# 35046-35050	 **attackbox here**
    sprite('Action_000_10', 5)	# 35051-35055	 **attackbox here**
    sprite('Action_000_11', 5)	# 35056-35060	 **attackbox here**
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('Action_000_00', 1)	# 35061-35061	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_01', 5)	# 35062-35066	 **attackbox here**
    sprite('Action_000_02', 5)	# 35067-35071	 **attackbox here**
    sprite('Action_000_03', 5)	# 35072-35076	 **attackbox here**
    sprite('Action_000_04', 5)	# 35077-35081	 **attackbox here**
    sprite('Action_000_05', 5)	# 35082-35086	 **attackbox here**
    sprite('Action_000_06', 5)	# 35087-35091	 **attackbox here**
    sprite('Action_000_07', 5)	# 35092-35096	 **attackbox here**
    sprite('Action_000_08', 5)	# 35097-35101	 **attackbox here**
    sprite('Action_000_09', 5)	# 35102-35106	 **attackbox here**
    sprite('Action_000_10', 5)	# 35107-35111	 **attackbox here**
    sprite('Action_000_11', 5)	# 35112-35116	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('Action_000_13', 5)	# 35117-35121	 **attackbox here**
    sprite('Action_000_14', 5)	# 35122-35126	 **attackbox here**
    sprite('Action_000_15', 6)	# 35127-35132	 **attackbox here**
    sprite('Action_000_16', 7)	# 35133-35139	 **attackbox here**
    sprite('Action_000_17', 7)	# 35140-35146	 **attackbox here**
    sprite('Action_000_18', 7)	# 35147-35153	 **attackbox here**
    sprite('Action_000_19', 7)	# 35154-35160	 **attackbox here**
    sprite('Action_000_20', 5)	# 35161-35165	 **attackbox here**
    SFX_1('uva601uli')
    sprite('Action_000_21', 6)	# 35166-35171	 **attackbox here**
    sprite('Action_000_22', 8)	# 35172-35179	 **attackbox here**
    sprite('Action_000_23', 6)	# 35180-35185	 **attackbox here**
    sprite('Action_000_24', 5)	# 35186-35190	 **attackbox here**
    sprite('Action_000_25', 5)	# 35191-35195	 **attackbox here**
    Unknown23018(1)
    label(163)
    sprite('Action_000_01', 5)	# 35196-35200	 **attackbox here**
    sprite('Action_000_02', 5)	# 35201-35205	 **attackbox here**
    sprite('Action_000_03', 5)	# 35206-35210	 **attackbox here**
    sprite('Action_000_04', 5)	# 35211-35215	 **attackbox here**
    sprite('Action_000_05', 5)	# 35216-35220	 **attackbox here**
    sprite('Action_000_06', 5)	# 35221-35225	 **attackbox here**
    sprite('Action_000_07', 5)	# 35226-35230	 **attackbox here**
    sprite('Action_000_08', 5)	# 35231-35235	 **attackbox here**
    sprite('Action_000_09', 5)	# 35236-35240	 **attackbox here**
    sprite('Action_000_10', 5)	# 35241-35245	 **attackbox here**
    sprite('Action_000_11', 5)	# 35246-35250	 **attackbox here**
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('Action_000_00', 1)	# 35251-35251	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('uva601rrb')
        Unknown23018(1)
    label(171)
    sprite('Action_000_01', 5)	# 35252-35256	 **attackbox here**
    sprite('Action_000_02', 5)	# 35257-35261	 **attackbox here**
    sprite('Action_000_03', 5)	# 35262-35266	 **attackbox here**
    sprite('Action_000_04', 5)	# 35267-35271	 **attackbox here**
    sprite('Action_000_05', 5)	# 35272-35276	 **attackbox here**
    sprite('Action_000_06', 5)	# 35277-35281	 **attackbox here**
    sprite('Action_000_07', 5)	# 35282-35286	 **attackbox here**
    sprite('Action_000_08', 5)	# 35287-35291	 **attackbox here**
    sprite('Action_000_09', 5)	# 35292-35296	 **attackbox here**
    sprite('Action_000_10', 5)	# 35297-35301	 **attackbox here**
    sprite('Action_000_11', 5)	# 35302-35306	 **attackbox here**
    gotoLabel(171)
    ExitState()
    label(180)
    sprite('Action_000_00', 1)	# 35307-35307	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('Action_000_01', 5)	# 35308-35312	 **attackbox here**
    sprite('Action_000_02', 5)	# 35313-35317	 **attackbox here**
    sprite('Action_000_03', 5)	# 35318-35322	 **attackbox here**
    sprite('Action_000_04', 5)	# 35323-35327	 **attackbox here**
    sprite('Action_000_05', 5)	# 35328-35332	 **attackbox here**
    sprite('Action_000_06', 5)	# 35333-35337	 **attackbox here**
    sprite('Action_000_07', 5)	# 35338-35342	 **attackbox here**
    sprite('Action_000_08', 5)	# 35343-35347	 **attackbox here**
    sprite('Action_000_09', 5)	# 35348-35352	 **attackbox here**
    sprite('Action_000_10', 5)	# 35353-35357	 **attackbox here**
    sprite('Action_000_11', 5)	# 35358-35362	 **attackbox here**
    gotoLabel(181)
    label(182)
    sprite('Action_052_00', 2)	# 35363-35364	 **attackbox here**
    sprite('Action_052_01', 8)	# 35365-35372	 **attackbox here**
    SFX_1('uva601rwi')
    sprite('Action_052_02', 8)	# 35373-35380	 **attackbox here**
    sprite('Action_052_03', 13)	# 35381-35393	 **attackbox here**
    sprite('Action_052_04', 21)	# 35394-35414	 **attackbox here**
    sprite('Action_052_05', 8)	# 35415-35422	 **attackbox here**
    sprite('Action_052_06', 65)	# 35423-35487	 **attackbox here**
    sprite('Action_052_07', 13)	# 35488-35500	 **attackbox here**
    sprite('Action_052_08', 8)	# 35501-35508	 **attackbox here**
    sprite('Action_052_01', 4)	# 35509-35512	 **attackbox here**
    Unknown23018(1)
    label(183)
    sprite('Action_000_01', 5)	# 35513-35517	 **attackbox here**
    sprite('Action_000_02', 5)	# 35518-35522	 **attackbox here**
    sprite('Action_000_03', 5)	# 35523-35527	 **attackbox here**
    sprite('Action_000_04', 5)	# 35528-35532	 **attackbox here**
    sprite('Action_000_05', 5)	# 35533-35537	 **attackbox here**
    sprite('Action_000_06', 5)	# 35538-35542	 **attackbox here**
    sprite('Action_000_07', 5)	# 35543-35547	 **attackbox here**
    sprite('Action_000_08', 5)	# 35548-35552	 **attackbox here**
    sprite('Action_000_09', 5)	# 35553-35557	 **attackbox here**
    sprite('Action_000_10', 5)	# 35558-35562	 **attackbox here**
    sprite('Action_000_11', 5)	# 35563-35567	 **attackbox here**
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('Action_050_00', 4)	# 35568-35571
    Unknown2019(0)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 4)	# 35572-35575
    sprite('Action_050_02', 4)	# 35576-35579
    sprite('Action_050_03', 4)	# 35580-35583
    sprite('Action_050_04', 4)	# 35584-35587
    sprite('Action_050_05', 4)	# 35588-35591
    sprite('Action_050_06', 4)	# 35592-35595
    sprite('Action_050_07', 4)	# 35596-35599
    sprite('Action_050_08', 5)	# 35600-35604
    sprite('Action_050_09', 5)	# 35605-35609
    sprite('Action_050_10', 5)	# 35610-35614
    sprite('Action_050_11', 5)	# 35615-35619
    SFX_3('SE_MagicExist')
    GFX_0('Entry', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry2', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    GFX_0('Entry3', -1)
    Unknown36(1)
    Unknown1007(260000)
    teleportRelativeX(20000)
    Unknown1021(-1480)
    Unknown35()
    sprite('Action_050_12', 4)	# 35620-35623	 **attackbox here**
    GFX_0('Vat_skirt', 100)
    sprite('Action_050_13', 4)	# 35624-35627	 **attackbox here**
    sprite('Action_050_14', 4)	# 35628-35631	 **attackbox here**
    sprite('Action_050_15', 4)	# 35632-35635	 **attackbox here**
    sprite('Action_050_16', 4)	# 35636-35639	 **attackbox here**
    sprite('Action_050_17', 4)	# 35640-35643	 **attackbox here**
    sprite('Action_050_18', 4)	# 35644-35647	 **attackbox here**
    sprite('Action_050_19', 4)	# 35648-35651	 **attackbox here**
    SFX_1('uva600ume')
    sprite('Action_050_20', 4)	# 35652-35655	 **attackbox here**
    sprite('Action_050_21', 4)	# 35656-35659	 **attackbox here**
    sprite('Action_050_22', 4)	# 35660-35663	 **attackbox here**
    sprite('Action_050_23', 4)	# 35664-35667	 **attackbox here**
    sprite('Action_050_24', 4)	# 35668-35671	 **attackbox here**
    sprite('Action_050_25', 4)	# 35672-35675	 **attackbox here**
    sprite('Action_050_26', 4)	# 35676-35679	 **attackbox here**
    sprite('Action_050_27', 4)	# 35680-35683	 **attackbox here**
    sprite('Action_050_28', 4)	# 35684-35687	 **attackbox here**
    sprite('Action_050_29', 4)	# 35688-35691	 **attackbox here**
    sprite('Action_050_30', 4)	# 35692-35695	 **attackbox here**
    sprite('Action_050_31', 4)	# 35696-35699	 **attackbox here**
    sprite('Action_050_32', 4)	# 35700-35703	 **attackbox here**
    sprite('Action_050_33', 4)	# 35704-35707	 **attackbox here**
    sprite('Action_050_34', 4)	# 35708-35711	 **attackbox here**
    sprite('Action_050_35', 4)	# 35712-35715	 **attackbox here**
    sprite('Action_050_36', 4)	# 35716-35719	 **attackbox here**
    sprite('Action_050_38', 4)	# 35720-35723	 **attackbox here**
    sprite('Action_050_39', 4)	# 35724-35727	 **attackbox here**
    sprite('Action_050_40', 4)	# 35728-35731	 **attackbox here**
    sprite('Action_050_41', 4)	# 35732-35735	 **attackbox here**
    sprite('Action_050_43', 4)	# 35736-35739	 **attackbox here**
    GFX_0('Vat_Wing', 100)
    sprite('Action_050_44', 4)	# 35740-35743	 **attackbox here**
    sprite('Action_050_45', 4)	# 35744-35747	 **attackbox here**
    sprite('Action_050_46', 4)	# 35748-35751	 **attackbox here**
    sprite('Action_050_47', 4)	# 35752-35755	 **attackbox here**
    sprite('Action_050_48', 4)	# 35756-35759	 **attackbox here**
    sprite('Action_050_49', 4)	# 35760-35763	 **attackbox here**
    sprite('Action_050_50', 4)	# 35764-35767	 **attackbox here**
    sprite('Action_050_51', 4)	# 35768-35771	 **attackbox here**
    sprite('Action_050_52', 4)	# 35772-35775	 **attackbox here**
    sprite('Action_050_53', 4)	# 35776-35779	 **attackbox here**
    sprite('Action_050_54', 3)	# 35780-35782
    sprite('Action_050_55', 5)	# 35783-35787
    sprite('Action_050_56', 6)	# 35788-35793
    sprite('Action_050_57', 7)	# 35794-35800
    sprite('Action_050_58', 7)	# 35801-35807
    sprite('Action_050_59', 7)	# 35808-35814
    sprite('Action_050_60', 7)	# 35815-35821
    sprite('Action_050_61', 5)	# 35822-35826
    sprite('Action_050_62', 5)	# 35827-35831
    sprite('Action_050_63', 7)	# 35832-35838
    sprite('Action_050_64', 5)	# 35839-35843
    sprite('Action_050_65', 5)	# 35844-35848
    sprite('Action_050_66', 5)	# 35849-35853
    Unknown21007(24, 40)
    Unknown21011(480)
    label(191)
    sprite('Action_000_01', 5)	# 35854-35858	 **attackbox here**
    sprite('Action_000_02', 5)	# 35859-35863	 **attackbox here**
    sprite('Action_000_03', 5)	# 35864-35868	 **attackbox here**
    sprite('Action_000_04', 5)	# 35869-35873	 **attackbox here**
    sprite('Action_000_05', 5)	# 35874-35878	 **attackbox here**
    sprite('Action_000_06', 5)	# 35879-35883	 **attackbox here**
    sprite('Action_000_07', 5)	# 35884-35888	 **attackbox here**
    sprite('Action_000_08', 5)	# 35889-35893	 **attackbox here**
    sprite('Action_000_09', 5)	# 35894-35898	 **attackbox here**
    sprite('Action_000_10', 5)	# 35899-35903	 **attackbox here**
    sprite('Action_000_11', 5)	# 35904-35908	 **attackbox here**
    gotoLabel(191)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 35909-35909	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_01', 5)	# 35910-35914	 **attackbox here**
    sprite('Action_000_02', 5)	# 35915-35919	 **attackbox here**
    sprite('Action_000_03', 5)	# 35920-35924	 **attackbox here**
    sprite('Action_000_04', 5)	# 35925-35929	 **attackbox here**
    sprite('Action_000_05', 5)	# 35930-35934	 **attackbox here**
    sprite('Action_000_06', 5)	# 35935-35939	 **attackbox here**
    sprite('Action_000_07', 5)	# 35940-35944	 **attackbox here**
    sprite('Action_000_08', 5)	# 35945-35949	 **attackbox here**
    sprite('Action_000_09', 5)	# 35950-35954	 **attackbox here**
    sprite('Action_000_10', 5)	# 35955-35959	 **attackbox here**
    sprite('Action_000_11', 5)	# 35960-35964	 **attackbox here**
    gotoLabel(992)
    label(993)
    sprite('Action_046_00', 2)	# 35965-35966	 **attackbox here**

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
    sprite('Action_046_01', 2)	# 35967-35968	 **attackbox here**
    sprite('Action_046_02', 1)	# 35969-35969	 **attackbox here**
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 35970-35972
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
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('ume'):
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
    sprite('Action_052_00', 2)	# 4-5	 **attackbox here**
    sprite('Action_052_01', 8)	# 6-13	 **attackbox here**
    sprite('Action_052_02', 8)	# 14-21	 **attackbox here**
    sprite('Action_052_03', 13)	# 22-34	 **attackbox here**
    sprite('Action_052_04', 21)	# 35-55	 **attackbox here**
    sprite('Action_052_05', 8)	# 56-63	 **attackbox here**
    sprite('Action_052_06', 25)	# 64-88	 **attackbox here**
    sprite('Action_052_07', 13)	# 89-101	 **attackbox here**
    sprite('Action_052_08', 8)	# 102-109	 **attackbox here**
    sprite('Action_052_09', 5)	# 110-114	 **attackbox here**
    sprite('Action_052_10', 5)	# 115-119	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uva524', 100, 895579765, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uva402_0', 100, 878802549, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uva520', 100, 895579765, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_052_11', 5)	# 120-124	 **attackbox here**
    sprite('Action_052_12', 7)	# 125-131	 **attackbox here**
    sprite('Action_052_13', 5)	# 132-136	 **attackbox here**
    sprite('Action_052_14', 7)	# 137-143	 **attackbox here**
    sprite('Action_052_15', 7)	# 144-150	 **attackbox here**
    sprite('Action_052_16', 8)	# 151-158	 **attackbox here**
    sprite('Action_052_17', 10)	# 159-168	 **attackbox here**
    sprite('Action_052_18', 7)	# 169-175	 **attackbox here**
    sprite('Action_052_19', 9)	# 176-184	 **attackbox here**
    sprite('Action_052_20', 12)	# 185-196	 **attackbox here**
    GFX_0('Win', -1)
    GFX_0('Win_MATOME', -1)
    sprite('Action_052_21', 16)	# 197-212	 **attackbox here**
    sprite('Action_052_22', 7)	# 213-219
    physicsYImpulse(1500)
    sprite('Action_052_23', 7)	# 220-226
    YAccel(50)
    sprite('Action_052_24', 7)	# 227-233
    sprite('Action_052_25', 7)	# 234-240
    Unknown23018(1)
    sprite('Action_052_25', 1)	# 241-241

    def upon_3():
        if (SLOT_13 > 600):
            setGravity(15)
        if (SLOT_13 < (-600)):
            setGravity(-15)
    setGravity(35)
    label(0)
    sprite('Action_052_26', 7)	# 242-248	 **attackbox here**
    physicsXImpulse(100)
    sprite('Action_052_27', 7)	# 249-255	 **attackbox here**
    sprite('Action_052_28', 7)	# 256-262	 **attackbox here**
    sprite('Action_052_29', 7)	# 263-269	 **attackbox here**
    sprite('Action_052_30', 7)	# 270-276	 **attackbox here**
    sprite('Action_052_26', 7)	# 277-283	 **attackbox here**
    sprite('Action_052_27', 7)	# 284-290	 **attackbox here**
    sprite('Action_052_28', 7)	# 291-297	 **attackbox here**
    sprite('Action_052_29', 7)	# 298-304	 **attackbox here**
    sprite('Action_052_30', 7)	# 305-311	 **attackbox here**
    sprite('Action_052_26', 7)	# 312-318	 **attackbox here**
    physicsXImpulse(-100)
    sprite('Action_052_27', 7)	# 319-325	 **attackbox here**
    sprite('Action_052_28', 7)	# 326-332	 **attackbox here**
    sprite('Action_052_29', 7)	# 333-339	 **attackbox here**
    sprite('Action_052_30', 7)	# 340-346	 **attackbox here**
    sprite('Action_052_26', 7)	# 347-353	 **attackbox here**
    sprite('Action_052_27', 7)	# 354-360	 **attackbox here**
    sprite('Action_052_28', 7)	# 361-367	 **attackbox here**
    sprite('Action_052_29', 7)	# 368-374	 **attackbox here**
    sprite('Action_052_30', 7)	# 375-381	 **attackbox here**
    gotoLabel(0)
    label(10)
    sprite('Action_053_00', 6)	# 382-387	 **attackbox here**
    sprite('Action_053_01', 9)	# 388-396	 **attackbox here**
    sprite('Action_053_02', 8)	# 397-404	 **attackbox here**
    sprite('Action_053_03', 5)	# 405-409	 **attackbox here**
    sprite('Action_053_04', 5)	# 410-414	 **attackbox here**
    sprite('Action_053_05', 5)	# 415-419	 **attackbox here**
    sprite('Action_053_06', 5)	# 420-424	 **attackbox here**
    sprite('Action_053_07', 5)	# 425-429	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uva524', 100, 895579765, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uva402_0', 100, 878802549, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uva522', 100, 895579765, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_053_08', 5)	# 430-434	 **attackbox here**
    sprite('Action_053_09', 5)	# 435-439	 **attackbox here**
    sprite('Action_053_10', 5)	# 440-444	 **attackbox here**
    Unknown23018(1)
    label(11)
    sprite('Action_053_11', 5)	# 445-449	 **attackbox here**
    sprite('Action_053_12', 5)	# 450-454	 **attackbox here**
    sprite('Action_053_13', 5)	# 455-459	 **attackbox here**
    sprite('Action_053_14', 5)	# 460-464	 **attackbox here**
    sprite('Action_053_15', 5)	# 465-469	 **attackbox here**
    gotoLabel(11)
    label(100)
    sprite('Action_052_00', 2)	# 470-471	 **attackbox here**
    sprite('Action_052_01', 8)	# 472-479	 **attackbox here**
    sprite('Action_052_02', 8)	# 480-487	 **attackbox here**
    sprite('Action_052_03', 13)	# 488-500	 **attackbox here**
    sprite('Action_052_04', 21)	# 501-521	 **attackbox here**
    sprite('Action_052_05', 8)	# 522-529	 **attackbox here**
    sprite('Action_052_06', 25)	# 530-554	 **attackbox here**
    sprite('Action_052_07', 13)	# 555-567	 **attackbox here**
    sprite('Action_052_08', 8)	# 568-575	 **attackbox here**
    sprite('Action_052_09', 5)	# 576-580	 **attackbox here**
    sprite('Action_052_10', 5)	# 581-585	 **attackbox here**
    SFX_1('uva700bno')
    sprite('Action_052_11', 5)	# 586-590	 **attackbox here**
    sprite('Action_052_12', 7)	# 591-597	 **attackbox here**
    sprite('Action_052_13', 5)	# 598-602	 **attackbox here**
    sprite('Action_052_14', 7)	# 603-609	 **attackbox here**
    sprite('Action_052_15', 7)	# 610-616	 **attackbox here**
    sprite('Action_052_16', 8)	# 617-624	 **attackbox here**
    sprite('Action_052_17', 10)	# 625-634	 **attackbox here**
    sprite('Action_052_18', 7)	# 635-641	 **attackbox here**
    sprite('Action_052_19', 9)	# 642-650	 **attackbox here**
    sprite('Action_052_20', 12)	# 651-662	 **attackbox here**
    GFX_0('Win', -1)
    GFX_0('Win_MATOME', -1)
    sprite('Action_052_21', 16)	# 663-678	 **attackbox here**
    sprite('Action_052_22', 7)	# 679-685
    physicsYImpulse(1500)
    sprite('Action_052_23', 7)	# 686-692
    YAccel(50)
    sprite('Action_052_24', 7)	# 693-699
    sprite('Action_052_25', 7)	# 700-706

    def upon_3():
        if (SLOT_13 > 600):
            setGravity(15)
        if (SLOT_13 < (-600)):
            setGravity(-15)
    setGravity(35)
    label(101)
    sprite('Action_052_26', 7)	# 707-713	 **attackbox here**
    physicsXImpulse(100)
    sprite('Action_052_27', 7)	# 714-720	 **attackbox here**
    sprite('Action_052_28', 7)	# 721-727	 **attackbox here**
    sprite('Action_052_29', 7)	# 728-734	 **attackbox here**
    sprite('Action_052_30', 7)	# 735-741	 **attackbox here**
    sprite('Action_052_26', 7)	# 742-748	 **attackbox here**
    physicsXImpulse(-100)
    sprite('Action_052_27', 7)	# 749-755	 **attackbox here**
    sprite('Action_052_28', 7)	# 756-762	 **attackbox here**
    sprite('Action_052_29', 7)	# 763-769	 **attackbox here**
    sprite('Action_052_30', 7)	# 770-776	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_052_26', 7)	# 777-783	 **attackbox here**
    sprite('Action_052_27', 7)	# 784-790	 **attackbox here**
    sprite('Action_052_28', 7)	# 791-797	 **attackbox here**
    sprite('Action_052_29', 7)	# 798-804	 **attackbox here**
    sprite('Action_052_30', 7)	# 805-811	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(200)
    label(102)
    sprite('Action_052_26', 7)	# 812-818	 **attackbox here**
    sprite('Action_052_27', 7)	# 819-825	 **attackbox here**
    sprite('Action_052_28', 7)	# 826-832	 **attackbox here**
    sprite('Action_052_29', 7)	# 833-839	 **attackbox here**
    sprite('Action_052_30', 7)	# 840-846	 **attackbox here**
    gotoLabel(102)
    label(110)
    sprite('Action_053_00', 6)	# 847-852	 **attackbox here**
    if (not SLOT_158):
        Unknown2019(1000)
    sprite('Action_053_01', 9)	# 853-861	 **attackbox here**
    sprite('Action_053_02', 8)	# 862-869	 **attackbox here**
    sprite('Action_053_03', 5)	# 870-874	 **attackbox here**
    sprite('Action_053_04', 5)	# 875-879	 **attackbox here**
    sprite('Action_053_05', 5)	# 880-884	 **attackbox here**
    sprite('Action_053_06', 5)	# 885-889	 **attackbox here**
    sprite('Action_053_07', 5)	# 890-894	 **attackbox here**
    SFX_1('uva700brc')
    sprite('Action_053_08', 5)	# 895-899	 **attackbox here**
    sprite('Action_053_09', 5)	# 900-904	 **attackbox here**
    sprite('Action_053_10', 5)	# 905-909	 **attackbox here**
    sprite('Action_053_11', 5)	# 910-914	 **attackbox here**
    sprite('Action_053_12', 5)	# 915-919	 **attackbox here**
    sprite('Action_053_13', 5)	# 920-924	 **attackbox here**
    sprite('Action_053_14', 5)	# 925-929	 **attackbox here**
    sprite('Action_053_15', 5)	# 930-934	 **attackbox here**
    label(111)
    sprite('Action_053_11', 5)	# 935-939	 **attackbox here**
    sprite('Action_053_12', 5)	# 940-944	 **attackbox here**
    sprite('Action_053_13', 5)	# 945-949	 **attackbox here**
    sprite('Action_053_14', 5)	# 950-954	 **attackbox here**
    sprite('Action_053_15', 5)	# 955-959	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(111)
    sprite('Action_053_11', 1)	# 960-960	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(360)
    label(112)
    sprite('Action_053_11', 5)	# 961-965	 **attackbox here**
    sprite('Action_053_12', 5)	# 966-970	 **attackbox here**
    sprite('Action_053_13', 5)	# 971-975	 **attackbox here**
    sprite('Action_053_14', 5)	# 976-980	 **attackbox here**
    sprite('Action_053_15', 5)	# 981-985	 **attackbox here**
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('Action_000_00', 1)	# 986-986	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('Action_000_01', 5)	# 987-991	 **attackbox here**
    sprite('Action_000_02', 5)	# 992-996	 **attackbox here**
    sprite('Action_000_03', 5)	# 997-1001	 **attackbox here**
    sprite('Action_000_04', 5)	# 1002-1006	 **attackbox here**
    sprite('Action_000_05', 5)	# 1007-1011	 **attackbox here**
    sprite('Action_000_06', 5)	# 1012-1016	 **attackbox here**
    sprite('Action_000_07', 5)	# 1017-1021	 **attackbox here**
    sprite('Action_000_08', 5)	# 1022-1026	 **attackbox here**
    sprite('Action_000_09', 5)	# 1027-1031	 **attackbox here**
    sprite('Action_000_10', 5)	# 1032-1036	 **attackbox here**
    sprite('Action_000_11', 5)	# 1037-1041	 **attackbox here**
    gotoLabel(121)
    label(122)
    sprite('Action_053_00', 6)	# 1042-1047	 **attackbox here**
    sprite('Action_053_01', 9)	# 1048-1056	 **attackbox here**
    sprite('Action_053_02', 8)	# 1057-1064	 **attackbox here**
    sprite('Action_053_03', 5)	# 1065-1069	 **attackbox here**
    sprite('Action_053_04', 5)	# 1070-1074	 **attackbox here**
    sprite('Action_053_05', 5)	# 1075-1079	 **attackbox here**
    sprite('Action_053_06', 5)	# 1080-1084	 **attackbox here**
    sprite('Action_053_07', 5)	# 1085-1089	 **attackbox here**
    SFX_1('uva701bny')
    sprite('Action_053_08', 5)	# 1090-1094	 **attackbox here**
    sprite('Action_053_09', 5)	# 1095-1099	 **attackbox here**
    sprite('Action_053_10', 5)	# 1100-1104	 **attackbox here**
    Unknown23018(1)
    label(123)
    sprite('Action_053_11', 5)	# 1105-1109	 **attackbox here**
    sprite('Action_053_12', 5)	# 1110-1114	 **attackbox here**
    sprite('Action_053_13', 5)	# 1115-1119	 **attackbox here**
    sprite('Action_053_14', 5)	# 1120-1124	 **attackbox here**
    sprite('Action_053_15', 5)	# 1125-1129	 **attackbox here**
    gotoLabel(123)
    label(130)
    sprite('keep', 1)	# 1130-1130
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
    sprite('keep', 1)	# 1131-1131
    if (not SLOT_2):
        sendToLabel(131)
    sprite('Action_015_00', 4)	# 1132-1135	 **attackbox here**
    Unknown2005()
    sprite('Action_015_01', 4)	# 1136-1139	 **attackbox here**
    label(131)
    sprite('Action_000_00_Vat639_00', 8)	# 1140-1147	 **attackbox here**
    sprite('Action_000_02_Vat639_01', 8)	# 1148-1155	 **attackbox here**
    SFX_1('uva700bes')
    label(132)
    sprite('Action_000_03_Vat639_02', 8)	# 1156-1163	 **attackbox here**
    sprite('Action_000_04_Vat639_03', 8)	# 1164-1171	 **attackbox here**
    sprite('Action_000_05_Vat639_04', 8)	# 1172-1179	 **attackbox here**
    sprite('Action_000_06_Vat639_05', 8)	# 1180-1187	 **attackbox here**
    sprite('Action_000_07_Vat639_06', 8)	# 1188-1195	 **attackbox here**
    sprite('Action_000_08_Vat639_07', 4)	# 1196-1199	 **attackbox here**
    sprite('Action_000_09_Vat639_08', 2)	# 1200-1201	 **attackbox here**
    sprite('Action_000_10_Vat639_09', 8)	# 1202-1209	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(132)
    sprite('Action_000_03_Vat639_02', 1)	# 1210-1210	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(133)
    sprite('Action_000_03_Vat639_02', 8)	# 1211-1218	 **attackbox here**
    sprite('Action_000_04_Vat639_03', 8)	# 1219-1226	 **attackbox here**
    sprite('Action_000_05_Vat639_04', 8)	# 1227-1234	 **attackbox here**
    sprite('Action_000_06_Vat639_05', 8)	# 1235-1242	 **attackbox here**
    sprite('Action_000_07_Vat639_06', 8)	# 1243-1250	 **attackbox here**
    sprite('Action_000_08_Vat639_07', 4)	# 1251-1254	 **attackbox here**
    sprite('Action_000_09_Vat639_08', 2)	# 1255-1256	 **attackbox here**
    sprite('Action_000_10_Vat639_09', 8)	# 1257-1264	 **attackbox here**
    loopRest()
    gotoLabel(133)
    label(140)
    sprite('Action_053_00', 6)	# 1265-1270	 **attackbox here**
    sprite('Action_053_01', 9)	# 1271-1279	 **attackbox here**
    sprite('Action_053_02', 8)	# 1280-1287	 **attackbox here**
    sprite('Action_053_03', 5)	# 1288-1292	 **attackbox here**
    sprite('Action_053_04', 5)	# 1293-1297	 **attackbox here**
    sprite('Action_053_05', 5)	# 1298-1302	 **attackbox here**
    sprite('Action_053_06', 5)	# 1303-1307	 **attackbox here**
    sprite('Action_053_07', 5)	# 1308-1312	 **attackbox here**
    SFX_1('uva700pag')
    sprite('Action_053_08', 5)	# 1313-1317	 **attackbox here**
    sprite('Action_053_09', 5)	# 1318-1322	 **attackbox here**
    sprite('Action_053_10', 5)	# 1323-1327	 **attackbox here**
    label(141)
    sprite('Action_053_11', 5)	# 1328-1332	 **attackbox here**
    sprite('Action_053_12', 5)	# 1333-1337	 **attackbox here**
    sprite('Action_053_13', 5)	# 1338-1342	 **attackbox here**
    sprite('Action_053_14', 5)	# 1343-1347	 **attackbox here**
    sprite('Action_053_15', 5)	# 1348-1352	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('Action_053_11', 1)	# 1353-1353	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(142)
    sprite('Action_053_11', 5)	# 1354-1358	 **attackbox here**
    sprite('Action_053_12', 5)	# 1359-1363	 **attackbox here**
    sprite('Action_053_13', 5)	# 1364-1368	 **attackbox here**
    sprite('Action_053_14', 5)	# 1369-1373	 **attackbox here**
    sprite('Action_053_15', 5)	# 1374-1378	 **attackbox here**
    loopRest()
    gotoLabel(142)
    label(150)
    sprite('Action_000_00', 1)	# 1379-1379	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('Action_000_01', 5)	# 1380-1384	 **attackbox here**
    sprite('Action_000_02', 5)	# 1385-1389	 **attackbox here**
    sprite('Action_000_03', 5)	# 1390-1394	 **attackbox here**
    sprite('Action_000_04', 5)	# 1395-1399	 **attackbox here**
    sprite('Action_000_05', 5)	# 1400-1404	 **attackbox here**
    sprite('Action_000_06', 5)	# 1405-1409	 **attackbox here**
    sprite('Action_000_07', 5)	# 1410-1414	 **attackbox here**
    sprite('Action_000_08', 5)	# 1415-1419	 **attackbox here**
    sprite('Action_000_09', 5)	# 1420-1424	 **attackbox here**
    sprite('Action_000_10', 5)	# 1425-1429	 **attackbox here**
    sprite('Action_000_11', 5)	# 1430-1434	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('Action_053_00', 6)	# 1435-1440	 **attackbox here**
    sprite('Action_053_01', 9)	# 1441-1449	 **attackbox here**
    sprite('Action_053_02', 8)	# 1450-1457	 **attackbox here**
    sprite('Action_053_03', 5)	# 1458-1462	 **attackbox here**
    sprite('Action_053_04', 5)	# 1463-1467	 **attackbox here**
    sprite('Action_053_05', 5)	# 1468-1472	 **attackbox here**
    sprite('Action_053_06', 5)	# 1473-1477	 **attackbox here**
    sprite('Action_053_07', 5)	# 1478-1482	 **attackbox here**
    SFX_1('uva701uhy')
    sprite('Action_053_08', 5)	# 1483-1487	 **attackbox here**
    sprite('Action_053_09', 5)	# 1488-1492	 **attackbox here**
    sprite('Action_053_10', 5)	# 1493-1497	 **attackbox here**
    Unknown23018(1)
    label(153)
    sprite('Action_053_11', 5)	# 1498-1502	 **attackbox here**
    sprite('Action_053_12', 5)	# 1503-1507	 **attackbox here**
    sprite('Action_053_13', 5)	# 1508-1512	 **attackbox here**
    sprite('Action_053_14', 5)	# 1513-1517	 **attackbox here**
    sprite('Action_053_15', 5)	# 1518-1522	 **attackbox here**
    gotoLabel(153)
    label(160)
    sprite('Action_000_00', 1)	# 1523-1523	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_01', 5)	# 1524-1528	 **attackbox here**
    sprite('Action_000_02', 5)	# 1529-1533	 **attackbox here**
    sprite('Action_000_03', 5)	# 1534-1538	 **attackbox here**
    sprite('Action_000_04', 5)	# 1539-1543	 **attackbox here**
    sprite('Action_000_05', 5)	# 1544-1548	 **attackbox here**
    sprite('Action_000_06', 5)	# 1549-1553	 **attackbox here**
    sprite('Action_000_07', 5)	# 1554-1558	 **attackbox here**
    sprite('Action_000_08', 5)	# 1559-1563	 **attackbox here**
    sprite('Action_000_09', 5)	# 1564-1568	 **attackbox here**
    sprite('Action_000_10', 5)	# 1569-1573	 **attackbox here**
    sprite('Action_000_11', 5)	# 1574-1578	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('Action_053_00', 6)	# 1579-1584	 **attackbox here**
    sprite('Action_053_01', 9)	# 1585-1593	 **attackbox here**
    sprite('Action_053_02', 8)	# 1594-1601	 **attackbox here**
    sprite('Action_053_03', 5)	# 1602-1606	 **attackbox here**
    sprite('Action_053_04', 5)	# 1607-1611	 **attackbox here**
    sprite('Action_053_05', 5)	# 1612-1616	 **attackbox here**
    sprite('Action_053_06', 5)	# 1617-1621	 **attackbox here**
    sprite('Action_053_07', 5)	# 1622-1626	 **attackbox here**
    SFX_1('uva701uli')
    sprite('Action_053_08', 5)	# 1627-1631	 **attackbox here**
    sprite('Action_053_09', 5)	# 1632-1636	 **attackbox here**
    sprite('Action_053_10', 5)	# 1637-1641	 **attackbox here**
    Unknown23018(1)
    label(163)
    sprite('Action_053_11', 5)	# 1642-1646	 **attackbox here**
    sprite('Action_053_12', 5)	# 1647-1651	 **attackbox here**
    sprite('Action_053_13', 5)	# 1652-1656	 **attackbox here**
    sprite('Action_053_14', 5)	# 1657-1661	 **attackbox here**
    sprite('Action_053_15', 5)	# 1662-1666	 **attackbox here**
    gotoLabel(163)
    label(170)
    sprite('Action_053_00', 6)	# 1667-1672	 **attackbox here**
    sprite('Action_053_01', 9)	# 1673-1681	 **attackbox here**
    sprite('Action_053_02', 8)	# 1682-1689	 **attackbox here**
    sprite('Action_053_03', 5)	# 1690-1694	 **attackbox here**
    sprite('Action_053_04', 5)	# 1695-1699	 **attackbox here**
    sprite('Action_053_05', 5)	# 1700-1704	 **attackbox here**
    sprite('Action_053_06', 5)	# 1705-1709	 **attackbox here**
    sprite('Action_053_07', 5)	# 1710-1714	 **attackbox here**
    SFX_1('uva700rrb')
    sprite('Action_053_08', 5)	# 1715-1719	 **attackbox here**
    sprite('Action_053_09', 5)	# 1720-1724	 **attackbox here**
    sprite('Action_053_10', 5)	# 1725-1729	 **attackbox here**
    label(171)
    sprite('Action_053_11', 5)	# 1730-1734	 **attackbox here**
    sprite('Action_053_12', 5)	# 1735-1739	 **attackbox here**
    sprite('Action_053_13', 5)	# 1740-1744	 **attackbox here**
    sprite('Action_053_14', 5)	# 1745-1749	 **attackbox here**
    sprite('Action_053_15', 5)	# 1750-1754	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(171)
    sprite('Action_053_11', 1)	# 1755-1755	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(172)
    sprite('Action_053_11', 5)	# 1756-1760	 **attackbox here**
    sprite('Action_053_12', 5)	# 1761-1765	 **attackbox here**
    sprite('Action_053_13', 5)	# 1766-1770	 **attackbox here**
    sprite('Action_053_14', 5)	# 1771-1775	 **attackbox here**
    sprite('Action_053_15', 5)	# 1776-1780	 **attackbox here**
    loopRest()
    gotoLabel(172)
    label(180)
    sprite('Action_053_00', 6)	# 1781-1786	 **attackbox here**
    sprite('Action_053_01', 9)	# 1787-1795	 **attackbox here**
    sprite('Action_053_02', 8)	# 1796-1803	 **attackbox here**
    sprite('Action_053_03', 5)	# 1804-1808	 **attackbox here**
    sprite('Action_053_04', 5)	# 1809-1813	 **attackbox here**
    sprite('Action_053_05', 5)	# 1814-1818	 **attackbox here**
    sprite('Action_053_06', 5)	# 1819-1823	 **attackbox here**
    sprite('Action_053_07', 5)	# 1824-1828	 **attackbox here**
    SFX_1('uva700rwi')
    sprite('Action_053_08', 5)	# 1829-1833	 **attackbox here**
    sprite('Action_053_09', 5)	# 1834-1838	 **attackbox here**
    sprite('Action_053_10', 5)	# 1839-1843	 **attackbox here**
    label(181)
    sprite('Action_053_11', 5)	# 1844-1848	 **attackbox here**
    sprite('Action_053_12', 5)	# 1849-1853	 **attackbox here**
    sprite('Action_053_13', 5)	# 1854-1858	 **attackbox here**
    sprite('Action_053_14', 5)	# 1859-1863	 **attackbox here**
    sprite('Action_053_15', 5)	# 1864-1868	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_053_11', 1)	# 1869-1869	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(270)
    label(182)
    sprite('Action_053_11', 5)	# 1870-1874	 **attackbox here**
    sprite('Action_053_12', 5)	# 1875-1879	 **attackbox here**
    sprite('Action_053_13', 5)	# 1880-1884	 **attackbox here**
    sprite('Action_053_14', 5)	# 1885-1889	 **attackbox here**
    sprite('Action_053_15', 5)	# 1890-1894	 **attackbox here**
    loopRest()
    gotoLabel(182)
    label(190)
    sprite('Action_000_00', 1)	# 1895-1895	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Action_000_01', 5)	# 1896-1900	 **attackbox here**
    sprite('Action_000_02', 5)	# 1901-1905	 **attackbox here**
    sprite('Action_000_03', 5)	# 1906-1910	 **attackbox here**
    sprite('Action_000_04', 5)	# 1911-1915	 **attackbox here**
    sprite('Action_000_05', 5)	# 1916-1920	 **attackbox here**
    sprite('Action_000_06', 5)	# 1921-1925	 **attackbox here**
    sprite('Action_000_07', 5)	# 1926-1930	 **attackbox here**
    sprite('Action_000_08', 5)	# 1931-1935	 **attackbox here**
    sprite('Action_000_09', 5)	# 1936-1940	 **attackbox here**
    sprite('Action_000_10', 5)	# 1941-1945	 **attackbox here**
    sprite('Action_000_11', 5)	# 1946-1950	 **attackbox here**
    gotoLabel(191)
    label(192)
    sprite('Action_053_00', 6)	# 1951-1956	 **attackbox here**
    sprite('Action_053_01', 9)	# 1957-1965	 **attackbox here**
    sprite('Action_053_02', 8)	# 1966-1973	 **attackbox here**
    sprite('Action_053_03', 5)	# 1974-1978	 **attackbox here**
    sprite('Action_053_04', 5)	# 1979-1983	 **attackbox here**
    sprite('Action_053_05', 5)	# 1984-1988	 **attackbox here**
    sprite('Action_053_06', 5)	# 1989-1993	 **attackbox here**
    sprite('Action_053_07', 5)	# 1994-1998	 **attackbox here**
    SFX_1('uva701ume')
    sprite('Action_053_08', 5)	# 1999-2003	 **attackbox here**
    sprite('Action_053_09', 5)	# 2004-2008	 **attackbox here**
    sprite('Action_053_10', 5)	# 2009-2013	 **attackbox here**
    Unknown23018(1)
    label(193)
    sprite('Action_053_11', 5)	# 2014-2018	 **attackbox here**
    sprite('Action_053_12', 5)	# 2019-2023	 **attackbox here**
    sprite('Action_053_13', 5)	# 2024-2028	 **attackbox here**
    sprite('Action_053_14', 5)	# 2029-2033	 **attackbox here**
    sprite('Action_053_15', 5)	# 2034-2038	 **attackbox here**
    gotoLabel(193)

@State
def CmnActLose():
    sprite('Action_248_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_248_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_248_02', 6)	# 11-16	 **attackbox here**
    sprite('Action_248_03', 6)	# 17-22	 **attackbox here**
    sprite('Action_248_04', 6)	# 23-28	 **attackbox here**
    if SLOT_158:
        Unknown7006('uva403_0', 100, 878802549, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_248_05', 7)	# 29-35	 **attackbox here**
    sprite('Action_248_06', 32767)	# 36-32802	 **attackbox here**
    Unknown23018(1)