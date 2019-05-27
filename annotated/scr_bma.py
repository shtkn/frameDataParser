@Subroutine
def PreInit():
    Unknown12019('626d6100000000000000000000000000')

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
    Unknown14015(0, 450000, -200000, 200000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th', 0x6)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x1)
    Move_AirGround_(0x2000)
    Unknown14024('FuncAtkDrive')
    Unknown15014(1)
    Unknown14015(800000, 1800000, -200000, 500000, 250, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 800000, -200000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown14015(0, 750000, -200000, 150000, 50, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    Unknown15009()
    Unknown14015(0, 300000, -150000, 150000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown15021(2000)
    Unknown15013(1)
    Unknown14015(-150000, 500000, 150000, 500000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(0, 350000, -150000, 150000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(-100000, 350000, -300000, 300000, 1500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown15013(500)
    Unknown14015(-100000, 250000, -150000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x1)
    Move_AirGround_(0x2001)
    Unknown14024('FuncAtkDrive')
    Unknown14015(800000, 1800000, -500000, 500000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B2nd', 0x22)
    Unknown14005(1)
    Unknown14015(-500000, 800000, -500000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-100000, 350000, -300000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 230000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 230000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0x10b)
    Move_AirGround_(0x3008)
    Unknown14015(0, 1200000, -200000, 350000, 500, 10)
    Move_EndRegister()
    Move_Register('Assault_A_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    Unknown14005(1)
    Unknown14019('Func_Assault_A_EX')
    Unknown14015(400000, 700000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Assault_A_EX_nama', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0x10b)
    Move_Input_(INPUT_PRESS_A)
    Unknown14019('Func_Assault_A_EX')
    Unknown14015(400000, 700000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Assault_A', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    Unknown14005(1)
    Unknown14019('Func_Assault_A')
    Unknown14015(400000, 700000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Assault_A_nama', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14019('Func_Assault_A')
    Unknown14015(400000, 700000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Assault_B_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    Unknown14005(1)
    Unknown14019('Func_Assault_B_EX')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Assault_B_EX_nama', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0x10b)
    Move_Input_(INPUT_PRESS_B)
    Unknown14019('Func_Assault_B_EX')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Assault_B', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    Unknown14005(1)
    Unknown14019('Func_Assault_B')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Assault_B_nama', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14019('Func_Assault_B')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Assault_C_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14019('Func_Assault_C_EX')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Assault_C_EX_nama', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0x10b)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14019('Func_Assault_C_EX')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Assault_C', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x67)
    Move_Input_(0x4c)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14019('Func_Assault_C')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Assault_C_nama', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14019('Func_Assault_C')
    Unknown14015(900000, 1200000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Backflip', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3008)
    Move_Input_(0x10c)
    Unknown14024('Check_Backflip')
    Unknown14015(-50000, 450000, -500000, 500000, 250, 10)
    Move_EndRegister()
    Move_Register('Backflip_A_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x81)
    Unknown14005(1)
    Unknown14015(-200000, 200000, -1000000, -100000, 50, 0)
    Move_EndRegister()
    Move_Register('Backflip_A', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(0x81)
    Unknown14005(1)
    Unknown14019('Func_Backflip_A')
    Unknown14015(-200000, 200000, -1000000, -100000, 50, 0)
    Move_EndRegister()
    Move_Register('Backflip_A_nama', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14019('Func_Backflip_A')
    Unknown14015(-200000, 200000, -1000000, -100000, 50, 0)
    Move_EndRegister()
    Move_Register('Backflip_B_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x81)
    Unknown14005(1)
    Unknown14015(150000, 550000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_B', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x81)
    Unknown14005(1)
    Unknown14019('Func_Backflip_B')
    Unknown14015(150000, 550000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_B_nama', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14019('Func_Backflip_B')
    Unknown14015(150000, 550000, -1000000, -100000, 250, 0)
    Move_EndRegister()
    Move_Register('Backflip_C_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x81)
    Unknown14005(1)
    Unknown14013('Backflip_C')
    Move_AirGround_(0x3086)
    Unknown14015(150000, 550000, -1000000, -100000, 50, 0)
    Move_EndRegister()
    Move_Register('Backflip_C', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x81)
    Unknown14005(1)
    Unknown14019('Func_Backflip_C')
    Move_AirGround_(0x3086)
    Unknown14015(150000, 550000, -1000000, -100000, 50, 0)
    Move_EndRegister()
    Move_Register('Backflip_C_nama', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14019('Func_Backflip_C')
    Move_AirGround_(0x3086)
    Unknown14015(150000, 550000, -1000000, -100000, 50, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(300000, 1000000, -1000000, -100000, 150, 0)
    Move_EndRegister()
    Move_Register('AntiAir2nd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14015(300000, 1000000, -1000000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateJump', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(-200000, 200000, -200000, 1000000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateJump_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(-200000, 200000, -200000, 1000000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 600000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(0, 600000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'Assault_B', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'Assault_B', 10000000)
    Unknown15024('NmlAtk2C', 'Assault_A', 10000000)
    Unknown12018(0, 'ma062_01')
    Unknown12018(1, 'ma062_03')
    Unknown12018(2, 'ma062_04')
    Unknown12018(3, 'ma062_05')
    Unknown12018(4, 'ma062_05')
    Unknown12018(5, 'ma062_06')
    Unknown12018(6, 'ma062_07')
    Unknown12018(7, 'ma041_02')
    Unknown12018(8, 'ma040_02')
    Unknown12018(9, 'ma045_02')
    Unknown12018(10, 'ma060_00')
    Unknown12018(11, 'ma060_01')
    Unknown12018(12, 'ma060_03')
    Unknown12018(13, 'ma060_05')
    Unknown12018(14, 'ma060_07')
    Unknown12018(15, 'ma060_14')
    Unknown12018(16, 'ma050_00')
    Unknown12018(17, 'ma052_00')
    Unknown12018(18, 'ma054_00')
    Unknown12018(19, 'ma000_00')
    Unknown12018(20, 'ma000_00')
    Unknown12018(25, 'ma063_00')
    Unknown12018(26, 'ma063_01')
    Unknown12018(27, 'ma063_02')
    Unknown12018(28, 'ma063_04')
    Unknown12018(29, 'ma063_10')
    Unknown12018(24, 'ma073_01')
    Unknown7010(0, 'bma000')
    Unknown7010(1, 'bma001')
    Unknown7010(2, 'bma002')
    Unknown7010(3, 'bma003')
    Unknown7010(4, 'bma004')
    Unknown7010(5, 'bma005')
    Unknown7010(6, 'bma006')
    Unknown7010(7, 'bma007')
    Unknown7010(8, 'bma008')
    Unknown7010(9, 'bma009')
    Unknown7010(10, 'bma010')
    Unknown7010(15, 'bma011')
    Unknown7010(16, 'bma012')
    Unknown7010(17, 'bma013')
    Unknown7010(18, 'bma014')
    Unknown7010(19, 'bma015')
    Unknown7010(20, 'bma016')
    Unknown7010(21, 'bma017')
    Unknown7010(22, 'bma018')
    Unknown7010(23, 'bma019')
    Unknown7010(24, 'bma020')
    Unknown7010(25, 'bma021')
    Unknown7010(28, 'bma022')
    Unknown7010(29, 'bma023')
    Unknown7010(30, 'bma024')
    Unknown7010(31, 'bma025')
    Unknown7010(32, 'bma026')
    Unknown7010(33, 'bma027')
    Unknown7010(34, 'bma028')
    Unknown7010(35, 'bma029')
    Unknown7010(36, 'bma030')
    Unknown7010(37, 'bma031')
    Unknown7010(39, 'bma032')
    Unknown7010(42, 'bma033')
    Unknown7010(43, 'bma034')
    Unknown7010(44, 'bma035')
    Unknown7010(45, 'bma036')
    Unknown7010(46, 'bma037')
    Unknown7010(47, 'bma038')
    Unknown7010(48, 'bma039')
    Unknown7010(49, 'bma040')
    Unknown7010(50, 'bma041')
    Unknown7010(52, 'bma042')
    Unknown7010(53, 'bma043')
    Unknown7010(54, 'bma100_0')
    Unknown7010(55, 'bma100_1')
    Unknown7010(56, 'bma100_2')
    Unknown7010(63, 'bma101_0')
    Unknown7010(64, 'bma101_1')
    Unknown7010(65, 'bma101_2')
    Unknown7010(57, 'bma102_0')
    Unknown7010(58, 'bma102_1')
    Unknown7010(59, 'bma102_2')
    Unknown7010(66, 'bma103_0')
    Unknown7010(67, 'bma103_1')
    Unknown7010(68, 'bma103_2')
    Unknown7010(60, 'bma104_0')
    Unknown7010(61, 'bma104_1')
    Unknown7010(62, 'bma104_2')
    Unknown7010(69, 'bma105_0')
    Unknown7010(70, 'bma105_1')
    Unknown7010(71, 'bma105_2')
    Unknown7010(72, 'bma150')
    Unknown7010(73, 'bma151')
    Unknown7010(74, 'bma152')
    Unknown7010(85, 'bma153')
    Unknown7010(87, 'bma154')
    Unknown7010(88, 'bma155')
    Unknown7010(96, 'bma161_0')
    Unknown7010(97, 'bma161_1')
    Unknown7010(92, 'bma162_0')
    Unknown7010(93, 'bma162_1')
    Unknown7010(98, 'bma163_0')
    Unknown7010(99, 'bma163_1')
    Unknown7010(100, 'bma164_0')
    Unknown7010(101, 'bma164_1')
    Unknown7010(105, 'bma165_0')
    Unknown7010(106, 'bma165_1')
    Unknown7010(102, 'bma166_0')
    Unknown7010(103, 'bma166_1')
    Unknown7010(90, 'bma167_0')
    Unknown7010(91, 'bma167_1')
    Unknown7010(107, 'bma168_0')
    Unknown7010(108, 'bma168_1')
    Unknown7010(110, 'bma169_0')
    Unknown7010(111, 'bma169_1')
    Unknown7010(94, 'bma400_0')
    Unknown7010(95, 'bma400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174654a756d700000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d6174654a756d705f4f440000000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def FuncAtkDrive():
    SLOT_47 = 0
    if CheckInput(0xb):
        if CheckInput(0x93):
            SLOT_64 = 1
            SLOT_47 = SLOT_0
        elif CheckInput(0x45):
            SLOT_64 = 2
            SLOT_47 = SLOT_0
        else:
            SLOT_64 = 0
            SLOT_47 = 1

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_21:
            if SLOT_4:
                SLOT_4 = (SLOT_4 + (-1))
                if (SLOT_4 <= 0):
                    SLOT_4 = 0

@Subroutine
def MatchInit2():
    SLOT_5 = 2

@Subroutine
def OnLanding():
    SLOT_5 = 2

@Subroutine
def OnActionBegin():
    if (not Unknown23148('Assault')):
        if (not Unknown23148('Backflip')):
            SLOT_60 = 0
            SLOT_61 = 0

@Subroutine
def DeriveInputBegin():
    Unknown14070('Assault')
    Unknown14070('Assault_A_EX_nama')
    Unknown14070('Assault_B_EX_nama')
    Unknown14070('Assault_C_EX_nama')
    Unknown14070('Backflip')
    Unknown14070('UltimateJump')
    Unknown14070('UltimateJump_OD')
    Unknown14070('UltimateAssault')
    Unknown14070('UltimateAssault_OD')
    Unknown14070('AstralHeat')
    Unknown14070('CmnActInvincibleAttack')

@Subroutine
def DeriveTimingBegin():
    Unknown14072('Assault')
    Unknown14072('Assault_A_EX_nama')
    Unknown14072('Assault_B_EX_nama')
    Unknown14072('Assault_C_EX_nama')
    Unknown14072('Backflip')
    Unknown14072('UltimateJump')
    Unknown14072('UltimateJump_OD')
    Unknown14072('UltimateAssault')
    Unknown14072('UltimateAssault_OD')
    Unknown14072('AstralHeat')
    Unknown14072('CmnActInvincibleAttack')

@Subroutine
def Check_Backflip():
    SLOT_47 = 0
    if (SLOT_5 >= 1):
        SLOT_47 = 1

@Subroutine
def Func_Assault_A():
    if (not (SLOT_60 == 11)):
        SLOT_60 = 1

@Subroutine
def Func_Assault_B():
    if (not (SLOT_60 == 12)):
        SLOT_60 = 2

@Subroutine
def Func_Assault_C():
    if (not (SLOT_60 == 13)):
        SLOT_60 = 3

@Subroutine
def Func_Assault_A_EX():
    SLOT_60 = 11

@Subroutine
def Func_Assault_B_EX():
    SLOT_60 = 12

@Subroutine
def Func_Assault_C_EX():
    SLOT_60 = 13

@Subroutine
def Func_Backflip_A():
    if (not (SLOT_60 == 11)):
        SLOT_60 = 1

@Subroutine
def Func_Backflip_B():
    if (not (SLOT_60 == 12)):
        SLOT_60 = 2

@Subroutine
def Func_Backflip_C():
    if (not (SLOT_60 == 13)):
        SLOT_60 = 3

@Subroutine
def Func_Assault_D():
    if (not (SLOT_60 == 21)):
        SLOT_60 = 20

@Subroutine
def Func_Assault_D_OD():
    SLOT_60 = 21

@Subroutine
def Func_Backflip_D():
    if (not (SLOT_60 == 31)):
        SLOT_60 = 30

@Subroutine
def Func_Backflip_D_OD():
    SLOT_60 = 31

@State
def CmnActStand():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
    label(0)
    sprite('ma000_00', 7)	# 1-7
    if SLOT_6:
        if Unknown23145('NmlAtk5B'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-225000)
            Unknown35()
        if Unknown23145('NmlAtk5B2nd'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-225000)
            Unknown35()
    sprite('ma000_01', 7)	# 8-14
    sprite('ma000_02', 7)	# 15-21
    sprite('ma000_03', 7)	# 22-28
    sprite('ma000_04', 7)	# 29-35
    sprite('ma000_05', 7)	# 36-42
    sprite('ma000_06', 7)	# 43-49
    sprite('ma000_07', 7)	# 50-56
    sprite('ma000_08', 7)	# 57-63
    sprite('ma000_09', 7)	# 64-70
    sprite('ma000_10', 7)	# 71-77
    sprite('ma000_11', 7)	# 78-84
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('ma001_00', 7)	# 85-91
    SLOT_88 = 960
    SFX_1('bma000')
    sprite('ma001_01', 7)	# 92-98
    SFX_0('008_swing_pole_2')
    sprite('ma001_02', 7)	# 99-105
    sprite('ma001_03', 7)	# 106-112
    GFX_0('maef_001_zanzou', -1)
    sprite('ma001_04', 7)	# 113-119
    sprite('ma001_05', 7)	# 120-126
    sprite('ma001_06', 7)	# 127-133
    SFX_0('008_swing_pole_2')
    sprite('ma001_07', 7)	# 134-140
    GFX_0('maef_001_zanzou2', -1)
    sprite('ma001_08', 7)	# 141-147
    sprite('ma001_09', 7)	# 148-154
    sprite('ma001_10', 7)	# 155-161
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ma003_00', 3)	# 1-3
    sprite('ma003_01', 3)	# 4-6
    sprite('ma003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('ma010_00', 4)	# 1-4
    sprite('ma010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ma010_02', 6)	# 1-6
    sprite('ma010_03', 6)	# 7-12
    sprite('ma010_04', 6)	# 13-18
    sprite('ma010_05', 6)	# 19-24
    sprite('ma010_06', 6)	# 25-30
    sprite('ma010_07', 6)	# 31-36
    sprite('ma010_08', 6)	# 37-42
    sprite('ma010_09', 6)	# 43-48
    sprite('ma010_10', 6)	# 49-54
    sprite('ma010_11', 6)	# 55-60
    sprite('ma010_12', 6)	# 61-66
    sprite('ma010_13', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ma013_00', 3)	# 1-3
    sprite('ma013_01', 3)	# 4-6
    sprite('ma013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('ma010_01', 4)	# 1-4
    sprite('ma010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ma023_00', 2)	# 1-2
    sprite('ma023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ma020_00', 4)	# 1-4
    sprite('ma020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ma020_02', 3)	# 1-3
    sprite('ma020_03', 3)	# 4-6
    sprite('ma020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ma020_05', 3)	# 1-3
    sprite('ma020_06', 3)	# 4-6
    label(0)
    sprite('ma020_07', 4)	# 7-10
    sprite('ma020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ma024_00', 3)	# 1-3
    sprite('ma024_01', 3)	# 4-6
    sprite('ma024_02', 3)	# 7-9
    sprite('ma024_03', 3)	# 10-12
    sprite('ma024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('ma024_00', 2)	# 1-2
    sprite('ma024_01', 2)	# 3-4
    sprite('ma024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('ma024_03', 3)	# 1-3
    sprite('ma024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('ma030_00', 7)	# 1-7
    label(0)
    sprite('ma030_01', 7)	# 8-14
    sprite('ma030_02', 7)	# 15-21
    sprite('ma030_03', 7)	# 22-28
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_04', 7)	# 29-35
    sprite('ma030_05', 7)	# 36-42
    sprite('ma030_06', 7)	# 43-49
    sprite('ma030_07', 7)	# 50-56
    sprite('ma030_08', 7)	# 57-63
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma030_09', 7)	# 64-70
    sprite('ma030_10', 7)	# 71-77
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('ma031_00', 7)	# 1-7
    label(0)
    sprite('ma031_01', 7)	# 8-14
    sprite('ma031_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma031_03', 7)	# 22-28
    sprite('ma031_04', 7)	# 29-35
    sprite('ma031_05', 7)	# 36-42
    sprite('ma031_06', 7)	# 43-49
    sprite('ma031_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ma031_08', 7)	# 57-63
    sprite('ma031_09', 7)	# 64-70
    sprite('ma031_10', 7)	# 71-77
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('ma032_00', 2)	# 1-2
    label(0)
    sprite('ma032_01', 4)	# 3-6
    sprite('ma032_02', 3)	# 7-9
    sprite('ma032_03', 3)	# 10-12
    Unknown8006(100, 1, 1)
    sprite('ma032_04', 3)	# 13-15
    sprite('ma032_05', 3)	# 16-18
    sprite('ma032_06', 4)	# 19-22
    sprite('ma032_07', 3)	# 23-25
    sprite('ma032_08', 3)	# 26-28
    Unknown8006(100, 1, 1)
    sprite('ma032_09', 3)	# 29-31
    sprite('ma032_10', 3)	# 32-34
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ma032_11', 4)	# 1-4
    sprite('ma032_12', 4)	# 5-8
    sprite('ma032_13', 4)	# 9-12
    sprite('ma032_14', 4)	# 13-16
    sprite('ma032_15', 4)	# 17-20

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
    sprite('ma033_00', 2)	# 1-2
    sprite('ma033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('ma033_02', 2)	# 6-7
    sprite('ma033_02', 1)	# 8-8
    setInvincible(0)
    loopRest()
    label(0)
    sprite('ma033_01', 3)	# 9-11
    sprite('ma033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ma033_03', 2)	# 15-16
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ma033_04', 2)	# 17-18
    sprite('ma033_05', 2)	# 19-20
    sprite('ma033_06', 2)	# 21-22

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('ma035_00', 3)	# 1-3
    label(0)
    sprite('ma035_01', 3)	# 4-6
    sprite('ma035_02', 3)	# 7-9
    sprite('ma035_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ma036_00', 3)	# 1-3
    label(0)
    sprite('ma036_01', 3)	# 4-6
    sprite('ma036_02', 3)	# 7-9
    sprite('ma036_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirTurn():
    sprite('ma025_00', 4)	# 1-4
    sprite('ma025_01', 4)	# 5-8
    sprite('ma025_00ex01', 4)	# 9-12

@State
def CmnActHitStandLv1():
    sprite('ma050_00', 1)	# 1-1
    sprite('ma050_01', 1)	# 2-2
    sprite('ma050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ma050_01', 1)	# 1-1
    sprite('ma050_02', 1)	# 2-2
    sprite('ma050_01', 2)	# 3-4
    sprite('ma050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ma050_02', 1)	# 1-1
    sprite('ma050_03', 1)	# 2-2
    sprite('ma050_02', 2)	# 3-4
    sprite('ma050_01', 2)	# 5-6
    sprite('ma050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ma050_03', 1)	# 1-1
    sprite('ma050_04', 1)	# 2-2
    sprite('ma050_03', 2)	# 3-4
    sprite('ma050_02', 2)	# 5-6
    sprite('ma050_01', 2)	# 7-8
    sprite('ma050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ma050_04', 1)	# 1-1
    sprite('ma050_04', 1)	# 2-2
    sprite('ma050_04', 2)	# 3-4
    sprite('ma050_03', 2)	# 5-6
    sprite('ma050_02', 2)	# 7-8
    sprite('ma050_01', 2)	# 9-10
    sprite('ma050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ma052_00', 1)	# 1-1
    sprite('ma052_01', 1)	# 2-2
    sprite('ma052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ma052_01', 1)	# 1-1
    sprite('ma052_02', 1)	# 2-2
    sprite('ma052_01', 2)	# 3-4
    sprite('ma052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ma052_02', 1)	# 1-1
    sprite('ma052_03', 1)	# 2-2
    sprite('ma052_02', 2)	# 3-4
    sprite('ma052_01', 2)	# 5-6
    sprite('ma052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ma052_03', 1)	# 1-1
    sprite('ma052_04', 1)	# 2-2
    sprite('ma052_03', 2)	# 3-4
    sprite('ma052_02', 2)	# 5-6
    sprite('ma052_01', 2)	# 7-8
    sprite('ma052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ma052_04', 1)	# 1-1
    sprite('ma052_04', 1)	# 2-2
    sprite('ma052_04', 2)	# 3-4
    sprite('ma052_03', 2)	# 5-6
    sprite('ma052_02', 2)	# 7-8
    sprite('ma052_01', 2)	# 9-10
    sprite('ma052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ma054_00', 1)	# 1-1
    sprite('ma054_01', 1)	# 2-2
    sprite('ma054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ma054_01', 1)	# 1-1
    sprite('ma054_02', 1)	# 2-2
    sprite('ma054_01', 2)	# 3-4
    sprite('ma054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ma054_02', 1)	# 1-1
    sprite('ma054_03', 1)	# 2-2
    sprite('ma054_02', 2)	# 3-4
    sprite('ma054_01', 2)	# 5-6
    sprite('ma054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ma054_03', 1)	# 1-1
    sprite('ma054_04', 1)	# 2-2
    sprite('ma054_03', 2)	# 3-4
    sprite('ma054_02', 2)	# 5-6
    sprite('ma054_01', 2)	# 7-8
    sprite('ma054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ma054_04', 1)	# 1-1
    sprite('ma054_04', 1)	# 2-2
    sprite('ma054_04', 2)	# 3-4
    sprite('ma054_03', 2)	# 5-6
    sprite('ma054_02', 2)	# 7-8
    sprite('ma054_01', 2)	# 9-10
    sprite('ma054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ma060_00', 4)	# 1-4
    label(0)
    sprite('ma060_01', 4)	# 5-8
    sprite('ma060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ma062_05', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ma062_06', 4)	# 1-4
    label(0)
    sprite('ma062_07', 3)	# 5-7
    sprite('ma062_08', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ma063_04', 3)	# 1-3
    sprite('ma063_05', 3)	# 4-6

@State
def CmnActBDownBound():
    sprite('ma063_06', 2)	# 1-2
    sprite('ma063_07', 2)	# 3-4
    sprite('ma063_08', 3)	# 5-7
    sprite('ma063_09', 3)	# 8-10
    sprite('ma063_10', 3)	# 11-13

@State
def CmnActBDownLoop():
    sprite('ma063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('ma064_00', 3)	# 1-3
    sprite('ma064_01', 3)	# 4-6
    sprite('ma064_02', 3)	# 7-9
    sprite('ma064_03', 3)	# 10-12
    sprite('ma064_04', 3)	# 13-15
    sprite('ma064_05', 3)	# 16-18
    sprite('ma064_06', 3)	# 19-21
    sprite('ma064_07', 3)	# 22-24
    sprite('ma064_08', 3)	# 25-27

@State
def CmnActFDownUpper():
    sprite('ma063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ma063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ma063_02', 3)	# 1-3
    sprite('ma063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ma063_04', 3)	# 1-3
    sprite('ma063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('ma063_06', 2)	# 1-2
    sprite('ma063_07', 2)	# 3-4
    sprite('ma063_08', 3)	# 5-7
    sprite('ma063_09', 3)	# 8-10
    sprite('ma063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('ma063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ma064_00', 3)	# 1-3
    sprite('ma064_01', 3)	# 4-6
    sprite('ma064_02', 3)	# 7-9
    sprite('ma064_03', 3)	# 10-12
    sprite('ma064_04', 3)	# 13-15
    sprite('ma064_05', 3)	# 16-18
    sprite('ma064_06', 3)	# 19-21
    sprite('ma064_07', 3)	# 22-24
    sprite('ma064_08', 3)	# 25-27

@State
def CmnActVDownUpper():
    sprite('ma062_00', 3)	# 1-3
    label(0)
    sprite('ma062_01', 3)	# 4-6
    sprite('ma062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ma062_03', 3)	# 1-3
    sprite('ma062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('ma062_05', 3)	# 1-3
    sprite('ma062_06', 3)	# 4-6
    label(0)
    sprite('ma062_07', 3)	# 7-9
    sprite('ma062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ma062_09', 2)	# 1-2
    sprite('ma062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('ma072_00', 3)	# 1-3
    sprite('ma072_01', 3)	# 4-6
    sprite('ma072_02', 3)	# 7-9
    label(0)
    sprite('ma072_01', 3)	# 10-12
    sprite('ma072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ma074_00', 3)	# 1-3
    sprite('ma074_01', 3)	# 4-6
    sprite('ma074_02', 3)	# 7-9
    sprite('ma074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('ma082_00', 2)	# 1-2
    sprite('ma082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('ma071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ma073_00', 3)	# 1-3
    sprite('ma073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('ma073_02', 3)	# 1-3
    label(0)
    sprite('ma073_03', 3)	# 4-6
    sprite('ma073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ma070_00', 2)	# 1-2
    sprite('ma070_01', 2)	# 3-4
    label(0)
    sprite('ma070_02', 5)	# 5-9
    sprite('ma070_03', 5)	# 10-14
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('ma070_04', 4)	# 1-4
    sprite('ma070_05', 4)	# 5-8
    sprite('ma070_06', 4)	# 9-12
    sprite('ma070_07', 4)	# 13-16
    sprite('ma070_08', 4)	# 17-20
    sprite('ma070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ma070_10', 2)	# 1-2
    sprite('ma070_11', 2)	# 3-4
    sprite('ma070_12', 2)	# 5-6
    sprite('ma070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ma113_00', 3)	# 1-3
    sprite('ma113_01', 3)	# 4-6
    sprite('ma113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('ma113_00', 3)	# 1-3
    sprite('ma113_01', 3)	# 4-6
    sprite('ma113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('ma113_00', 3)	# 1-3
    sprite('ma113_01', 3)	# 4-6
    sprite('ma113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('ma110_00', 2)	# 1-2
    sprite('ma110_01', 2)	# 3-4
    sprite('ma110_02', 2)	# 5-6
    sprite('ma110_03', 2)	# 7-8
    sprite('ma110_04', 2)	# 9-10
    sprite('ma110_05', 2)	# 11-12
    sprite('ma110_06', 2)	# 13-14
    sprite('ma110_07', 2)	# 15-16
    sprite('ma110_08', 200)	# 17-216
    sprite('ma110_09', 3)	# 217-219
    sprite('ma110_10', 3)	# 220-222

@State
def CmnActUkemiLandB():
    sprite('ma111_00', 2)	# 1-2
    sprite('ma111_01', 2)	# 3-4
    sprite('ma111_02', 2)	# 5-6
    sprite('ma111_03', 2)	# 7-8
    sprite('ma111_04', 2)	# 9-10
    sprite('ma111_05', 2)	# 11-12
    sprite('ma111_06', 2)	# 13-14
    sprite('ma111_07', 2)	# 15-16
    sprite('ma111_08', 200)	# 17-216
    sprite('ma111_09', 3)	# 217-219
    sprite('ma111_10', 3)	# 220-222

@State
def CmnActUkemiLandN():
    sprite('ma112_00', 2)	# 1-2
    sprite('ma112_01', 2)	# 3-4
    sprite('ma112_02', 2)	# 5-6
    sprite('ma112_03', 2)	# 7-8
    sprite('ma112_04', 2)	# 9-10
    sprite('ma112_05', 2)	# 11-12
    sprite('ma112_06', 2)	# 13-14
    sprite('ma112_07', 2)	# 15-16
    sprite('ma112_08', 2)	# 17-18

@State
def CmnActUkemiLandNLanding():
    sprite('ma024_00', 3)	# 1-3
    sprite('ma024_01', 3)	# 4-6
    sprite('ma024_02', 3)	# 7-9
    sprite('ma024_03', 3)	# 10-12
    sprite('ma024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('ma040_00', 3)	# 1-3
    sprite('ma040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ma040_02', 4)	# 1-4
    sprite('ma040_03', 4)	# 5-8
    sprite('ma040_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ma040_01', 3)	# 1-3
    sprite('ma040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('ma040_05', 3)	# 1-3
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ma040_01', 3)	# 1-3
    sprite('ma040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ma041_00', 3)	# 1-3
    sprite('ma041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ma041_02', 4)	# 1-4
    sprite('ma041_03', 4)	# 5-8
    sprite('ma041_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ma041_01', 3)	# 1-3
    sprite('ma041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ma041_05', 3)	# 1-3

@State
def CmnActHighHeavyGuardEnd():
    sprite('ma041_01', 3)	# 1-3
    sprite('ma041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ma043_00', 3)	# 1-3
    sprite('ma043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ma043_02', 4)	# 1-4
    sprite('ma043_03', 4)	# 5-8
    sprite('ma043_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ma043_01', 3)	# 1-3
    sprite('ma043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ma043_05', 3)	# 1-3

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ma043_01', 3)	# 1-3
    sprite('ma043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ma045_00', 3)	# 1-3
    sprite('ma045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ma045_02', 4)	# 1-4
    sprite('ma045_03', 4)	# 5-8
    sprite('ma045_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ma045_01', 3)	# 1-3
    sprite('ma045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ma045_05', 3)	# 1-3

@State
def CmnActAirHeavyGuardEnd():
    sprite('ma045_01', 3)	# 1-3
    sprite('ma045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ma090_00', 2)	# 1-2
    sprite('ma090_01', 2)	# 3-4
    sprite('ma090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ma090_03', 6)	# 6-11
    sprite('ma090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('ma091_00', 2)	# 1-2
    sprite('ma091_01', 2)	# 3-4
    sprite('ma091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ma091_03', 6)	# 6-11
    sprite('ma091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('ma092_00', 2)	# 1-2
    sprite('ma092_01', 2)	# 3-4
    sprite('ma092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ma092_03', 6)	# 6-11
    sprite('ma092_04', 6)	# 12-17

@State
def CmnActLockWait():
    sprite('ma040_02', 1)	# 1-1
    sprite('ma040_01', 3)	# 2-4
    sprite('ma040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('ma312_00', 3)	# 1-3
    sprite('ma312_01', 3)	# 4-6
    sprite('ma312_02', 3)	# 7-9
    sprite('ma312_03', 6)	# 10-15	 **attackbox here**
    sprite('ma312_04', 5)	# 16-20
    sprite('ma312_05', 3)	# 21-23
    sprite('ma312_06', 3)	# 24-26
    sprite('ma312_07', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('ma045_02', 1)	# 1-1
    sprite('ma045_01', 3)	# 2-4
    sprite('ma045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ma322_00', 3)	# 1-3
    sprite('ma322_01', 3)	# 4-6
    sprite('ma322_02', 3)	# 7-9
    sprite('ma322_03', 6)	# 10-15	 **attackbox here**
    sprite('ma322_04', 6)	# 16-21
    sprite('ma322_05', 4)	# 22-25
    sprite('ma322_06', 4)	# 26-29

@State
def CmnActLandSpin():
    sprite('ma071_00', 4)	# 1-4
    sprite('ma071_01', 4)	# 5-8
    label(0)
    sprite('ma071_02', 2)	# 9-10
    sprite('ma071_03', 2)	# 11-12
    sprite('ma071_04', 2)	# 13-14
    sprite('ma071_05', 2)	# 15-16
    sprite('ma071_06', 2)	# 17-18
    sprite('ma071_07', 2)	# 19-20
    sprite('ma071_08', 2)	# 21-22
    sprite('ma071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ma071_10', 6)	# 1-6
    sprite('ma071_11', 5)	# 7-11
    sprite('ma071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('ma071_02', 2)	# 1-2
    sprite('ma071_03', 2)	# 3-4
    sprite('ma071_04', 2)	# 5-6
    sprite('ma071_05', 2)	# 7-8
    sprite('ma071_06', 2)	# 9-10
    sprite('ma071_07', 2)	# 11-12
    sprite('ma071_08', 2)	# 13-14
    sprite('ma071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('ma077_00', 2)	# 1-2
    sprite('ma077_01', 2)	# 3-4
    sprite('ma077_00ex01', 2)	# 5-6
    sprite('ma077_01ex01', 2)	# 7-8
    sprite('ma077_00ex02', 2)	# 9-10
    sprite('ma077_01ex02', 2)	# 11-12
    sprite('ma077_00ex03', 2)	# 13-14
    sprite('ma077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ma077_02', 4)	# 1-4
    label(0)
    sprite('ma077_03', 3)	# 5-7
    sprite('ma077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ma077_05', 5)	# 1-5
    sprite('ma077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('ma060_07', 3)	# 1-3
    sprite('ma060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ma060_11', 4)	# 1-4
    sprite('ma060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('ma331_00', 2)	# 1-2
    sprite('ma331_01', 2)	# 3-4
    label(0)
    sprite('ma331_02', 3)	# 5-7
    sprite('ma331_03', 3)	# 8-10
    sprite('ma331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ma331_05', 2)	# 1-2
    label(0)
    sprite('ma331_06', 3)	# 3-5
    sprite('ma331_07', 3)	# 6-8
    sprite('ma331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ma331_09', 3)	# 1-3
    sprite('ma331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('ma331_11', 2)	# 1-2
    sprite('ma331_12', 2)	# 3-4
    label(0)
    sprite('ma331_02', 3)	# 5-7
    sprite('ma331_03', 3)	# 8-10
    sprite('ma331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ma331_05', 2)	# 1-2
    label(0)
    sprite('ma331_06', 3)	# 3-5
    sprite('ma331_07', 3)	# 6-8
    sprite('ma331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ma331_13', 4)	# 1-4
    sprite('ma331_14', 4)	# 5-8
    sprite('ma020_06', 4)	# 9-12
    label(0)
    sprite('ma020_07', 4)	# 13-16
    sprite('ma020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('ma333_00', 3)	# 1-3
    sprite('ma333_01', 3)	# 4-6
    sprite('ma333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ma333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ma333_04', 3)	# 1-3
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ma333_05', 3)	# 4-6
    sprite('ma333_06', 3)	# 7-9
    sprite('ma333_07', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('ma333_08', 6)	# 1-6
    sprite('ma333_09', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('ma333_10', 3)	# 1-3
    sprite('ma333_11', 3)	# 4-6
    sprite('ma333_12', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ma333_13', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ma333_14', 3)	# 1-3
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ma333_05', 3)	# 4-6
    sprite('ma333_06', 3)	# 7-9
    sprite('ma333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ma333_15', 6)	# 1-6
    sprite('ma333_16', 6)	# 7-12
    label(0)
    sprite('ma020_07', 4)	# 13-16
    sprite('ma020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ma333_00', 3)	# 1-3
    sprite('ma333_01', 3)	# 4-6
    sprite('ma333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ma333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ma333_04', 3)	# 1-3
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ma333_05', 3)	# 4-6
    sprite('ma333_06', 3)	# 7-9
    sprite('ma333_07', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('ma333_08', 6)	# 1-6
    sprite('ma333_09', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('ma333_10', 3)	# 1-3
    sprite('ma333_11', 3)	# 4-6
    sprite('ma333_12', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ma333_13', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ma333_14', 3)	# 1-3
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ma333_05', 3)	# 4-6
    sprite('ma333_06', 3)	# 7-9
    sprite('ma333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ma333_15', 6)	# 1-6
    sprite('ma333_16', 6)	# 7-12
    label(0)
    sprite('ma020_07', 4)	# 13-16
    sprite('ma020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('ma331_00', 2)	# 1-2
    sprite('ma331_01', 2)	# 3-4
    label(0)
    sprite('ma331_02', 3)	# 5-7
    sprite('ma331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('ma331_04', 2)	# 1-2
    sprite('ma331_05', 2)	# 3-4
    label(0)
    sprite('ma331_06', 3)	# 5-7
    sprite('ma331_07', 3)	# 8-10
    sprite('ma331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ma331_09', 3)	# 1-3
    sprite('ma331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('ma332_00', 2)	# 1-2
    sprite('ma332_01', 2)	# 3-4
    label(0)
    sprite('ma332_02', 3)	# 5-7
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('ma332_03', 2)	# 1-2
    sprite('ma332_04', 2)	# 3-4
    label(0)
    sprite('ma332_05', 2)	# 5-6
    sprite('ma332_06', 2)	# 7-8
    sprite('ma332_07', 2)	# 9-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ma332_08', 2)	# 1-2
    sprite('ma020_05', 2)	# 3-4
    sprite('ma020_06', 2)	# 5-6
    label(0)
    sprite('ma020_07', 4)	# 7-10
    sprite('ma020_08', 4)	# 11-14
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

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('ma300_00', 4)	# 1-4
    loopRest()
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    SFX_0('301_overdrive_end')
    sprite('ma300_01', 4)	# 5-8
    sprite('ma300_02', 4)	# 9-12
    sprite('ma300_03', 4)	# 13-16
    sprite('ma300_05', 27)	# 17-43
    sprite('ma300_03', 4)	# 44-47
    sprite('ma300_06', 5)	# 48-52
    sprite('ma300_07', 5)	# 53-57
    sprite('ma300_08', 5)	# 58-62

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('ma045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('ma045_00', 3)	# 2-4
    sprite('ma045_01', 4)	# 5-8
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    SFX_0('301_overdrive_end')
    label(0)
    sprite('ma045_02', 5)	# 9-13
    sprite('ma045_02ex', 5)	# 14-18
    loopRest()
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
    gotoLabel(0)
    label(1)
    sprite('ma045_01', 6)	# 19-24
    sprite('ma045_00', 6)	# 25-30

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('ma403_05', 3)	# 26-28	 **attackbox here**
    GFX_0('maef_403', 0)
    Unknown1086(22)
    teleportRelativeX(-15000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('ma403_06', 3)	# 29-31	 **attackbox here**
    label(1)
    sprite('ma403_05', 3)	# 32-34	 **attackbox here**
    sprite('ma403_06', 3)	# 35-37	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ma403_07', 3)	# 38-40	 **attackbox here**
    Unknown26('maef_403')
    Unknown26('maef_401_ring')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown23027()
    Recovery()
    sprite('ma403_07', 6)	# 41-46	 **attackbox here**
    sprite('ma403_08', 8)	# 47-54
    sprite('ma403_09', 4)	# 55-58
    sprite('ma403_10', 4)	# 59-62

@State
def CmnActChangePartnerQuickIn():
    sprite('ma032_08', 3)	# 1-3
    sprite('ma032_09', 3)	# 4-6
    sprite('ma032_10', 3)	# 7-9
    sprite('ma032_11', 4)	# 10-13
    sprite('ma032_12', 4)	# 14-17
    sprite('ma032_13', 4)	# 18-21
    sprite('ma032_14', 4)	# 22-25
    sprite('ma032_15', 4)	# 26-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ma033_01', 3)	# 1-3
    sprite('ma033_02', 3)	# 4-6
    sprite('ma033_01', 3)	# 7-9
    sprite('ma033_02', 3)	# 10-12
    sprite('ma033_01', 3)	# 13-15
    sprite('ma033_02', 3)	# 16-18
    sprite('ma033_01', 3)	# 19-21
    sprite('ma033_02', 3)	# 22-24
    sprite('ma033_01', 3)	# 25-27
    sprite('ma033_02', 3)	# 28-30
    sprite('ma033_01', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ma033_00', 3)	# 1-3
    sprite('ma033_01', 2)	# 4-5
    sprite('ma033_02', 2)	# 6-7
    sprite('ma033_02', 1)	# 8-8
    sprite('ma033_03', 3)	# 9-11
    loopRest()
    label(0)
    sprite('ma033_02', 3)	# 12-14
    sprite('ma033_03', 3)	# 15-17
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ma033_04', 3)	# 18-20
    sprite('ma033_05', 3)	# 21-23

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ma300_00', 6)	# 1-6
    sprite('ma300_01', 6)	# 7-12
    sprite('ma300_02', 6)	# 13-18
    sprite('ma300_03', 8)	# 19-26
    sprite('ma300_04', 10)	# 27-36
    sprite('ma300_05', 10)	# 37-46
    sprite('ma300_06', 5)	# 47-51
    sprite('ma300_07', 5)	# 52-56
    sprite('ma001_08', 5)	# 57-61
    sprite('ma001_09', 5)	# 62-66
    sprite('ma001_10', 5)	# 67-71
    sprite('ma000_00', 30)	# 72-101

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
    sprite('ma020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ma020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ma010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('ma501_00', 5)	# 1-5
    sprite('ma501_01', 5)	# 6-10
    sprite('ma501_02', 4)	# 11-14
    sprite('ma501_03', 4)	# 15-18	 **attackbox here**
    Unknown7007('626d613131315f30000000000000000064000000626d613131315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_0('008_swing_pole_1')
    GFX_0('maef_501_zanzou2', -1)
    StartMultihit()
    sprite('ma501_03', 3)	# 19-21	 **attackbox here**
    StartMultihit()
    sprite('ma501_04', 1)	# 22-22
    sprite('ma501_04', 3)	# 23-25
    GFX_0('maef_muzzle', 3)
    sprite('ma501_04', 2)	# 26-27
    GFX_0('maef_501_atk1', 3)
    sprite('ma501_05', 3)	# 28-30
    sprite('ma501_05', 1)	# 31-31
    sprite('ma501_05', 1)	# 32-32
    sprite('ma502_06', 5)	# 33-37
    sprite('ma501_03', 3)	# 38-40	 **attackbox here**
    Unknown7007('626d613131325f30000000000000000064000000626d613131325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_0('008_swing_pole_1')
    GFX_0('maef_501_zanzou', -1)
    StartMultihit()
    sprite('ma501_03', 2)	# 41-42	 **attackbox here**
    StartMultihit()
    sprite('ma501_04', 3)	# 43-45
    GFX_0('maef_muzzle', 4)
    sprite('ma501_04', 2)	# 46-47
    GFX_0('maef_501_atk2', 4)
    sprite('ma501_05', 3)	# 48-50
    sprite('ma501_05', 1)	# 51-51
    sprite('ma501_05', 1)	# 52-52
    sprite('ma501_06', 5)	# 53-57
    sprite('ma501_07', 5)	# 58-62
    sprite('ma501_08', 5)	# 63-67
    Recovery()
    sprite('ma501_09', 5)	# 68-72
    SFX_0('008_swing_pole_1')
    sprite('ma501_10', 5)	# 73-77
    sprite('ma501_11', 5)	# 78-82
    sprite('ma501_12', 5)	# 83-87

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11042(1)
        AttackLevel_(4)
        AttackP1(70)
        AttackP2(85)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(40000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
    sprite('ma010_00', 3)	# 1-3
    sprite('ma232_00', 3)	# 4-6
    physicsXImpulse(12000)
    sprite('ma232_01', 2)	# 7-8
    Unknown1028(2000)
    Unknown7009(2)
    sprite('ma232_02', 2)	# 9-10
    SFX_0('006_swing_blade_1')
    sprite('ma232_03', 2)	# 11-12
    sprite('ma232_04', 4)	# 13-16	 **attackbox here**
    Unknown1084(1)
    GFX_0('maef_232', -1)
    sprite('ma232_05', 5)	# 17-21
    Recovery()
    Unknown2063()
    sprite('ma232_06', 5)	# 22-26
    sprite('ma232_07', 5)	# 27-31
    sprite('ma232_08', 5)	# 32-36
    sprite('ma232_09', 5)	# 37-41
    sprite('ma232_10', 5)	# 42-46
    sprite('ma010_01', 4)	# 47-50
    sprite('ma010_00', 4)	# 51-54

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11042(1)
        AttackLevel_(4)
        Damage(2000)
        AttackP1(70)
        AttackP2(85)
        AirUntechableTime(60)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(20000)
        WallbounceReboundTime(15)
        Unknown9016(1)
    sprite('ma400_00', 3)	# 1-3
    sprite('ma400_01', 3)	# 4-6
    SFX_0('000_airdash_0')
    sprite('ma400_02', 2)	# 7-8
    physicsXImpulse(45000)
    Unknown8007(100, 1, 1)
    sprite('ma401_00', 1)	# 9-9
    Unknown1051(30)
    sprite('ma401_01', 1)	# 10-10
    Unknown7007('626d613230315f30000000000000000064000000626d613230315f31000000000000000064000000626d613230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma401_02', 1)	# 11-11
    sprite('ma401_03', 1)	# 12-12
    sprite('ma401_04', 2)	# 13-14	 **attackbox here**
    GFX_0('maef_401', 0)
    Unknown8006(100, 1, 1)
    SFX_3('mase_06')
    Unknown1084(1)
    physicsXImpulse(90000)
    sprite('ma401_05', 2)	# 15-16	 **attackbox here**
    sprite('ma401_04', 2)	# 17-18	 **attackbox here**
    sprite('ma401_05', 2)	# 19-20	 **attackbox here**
    sprite('ma401_05ex01', 1)	# 21-21	 **attackbox here**
    StartMultihit()
    Unknown26('maef_401')
    Recovery()
    sprite('ma401_06', 3)	# 22-24
    Unknown1019(20)
    sprite('ma401_07', 6)	# 25-30
    Unknown1019(50)
    Unknown1051(0)
    sprite('ma401_08', 4)	# 31-34
    Unknown1019(50)
    sprite('ma401_09', 4)	# 35-38
    sprite('ma401_10', 4)	# 39-42
    sprite('ma401_11', 4)	# 43-46
    Unknown1084(1)
    sprite('ma401_12', 3)	# 47-49

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
    Unknown2036(43, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('ma020_07', 4)	# 3-6
    sprite('ma020_08', 4)	# 7-10
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
        Unknown30063(1)
        AttackLevel_(5)
        Damage(80)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown9154(30)
        AirUntechableTime(100)
        PushbackX(3000)
        Hitstop(1)
        Unknown11072(1, 400000, 0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(100)
        Unknown9142(80)
        Unknown11069('ChangePartnerDD_Exe')
        Unknown11056(0)
        Unknown11064(1)
        Unknown9016(1)
        Unknown11057(750)
        setInvincible(1)

        def upon_78():
            setInvincible(1)
    sprite('ma440_00', 6)	# 1-6
    sprite('ma440_01', 6)	# 7-12
    Unknown1084(1)
    teleportRelativeX(59000)
    sprite('ma440_02', 6)	# 13-18
    sprite('ma440_03', 3)	# 19-21	 **attackbox here**
    Unknown23086(1)
    tag_voice(1, 'bma281_0', 'bma281_1', '', '')
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash1', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_04', 3)	# 22-24	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash2', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_05', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash3', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_06', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    sprite('ma440_07', 3)	# 31-33	 **attackbox here**
    sprite('ma440_08', 3)	# 34-36	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash4', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_09', 3)	# 37-39	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash5', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_03', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash1', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_04', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash2', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_05', 3)	# 46-48	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash3', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_06', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    sprite('ma440_07', 3)	# 52-54	 **attackbox here**
    sprite('ma440_08', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash4', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_08', 1)	# 57-57	 **attackbox here**
    sprite('ma440_09', 3)	# 58-60	 **attackbox here**
    RefreshMultihit()
    Unknown11001(10, 10, 10)
    PushbackX(30400)
    Unknown23086(0)
    GFX_0('maef_440_slash5', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_10', 6)	# 61-66
    sprite('ma440_14', 8)	# 67-74
    sprite('ma440_15', 8)	# 75-82
    SFX_0('006_swing_blade_2')
    sprite('ma440_16', 8)	# 83-90
    sprite('ma440_17', 4)	# 91-94	 **attackbox here**
    StartMultihit()
    physicsXImpulse(140000)
    sprite('ma440_17', 1)	# 95-95	 **attackbox here**
    tag_voice(0, 'bma282_0', 'bma282_1', '', '')
    Unknown1019(50)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1040)
    Hitstop(15)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(60000)
    AirPushbackY(20000)
    Unknown11057(1000)
    SFX_0('025_cleanhit_slash')
    GFX_0('maef_440_finish', -1)
    GFX_0('maef_440_finish2', -1)
    ScreenShake(32000, 32000)
    Unknown11064(0)
    Unknown11069('')
    sprite('ma440_17', 3)	# 96-98	 **attackbox here**
    Unknown1084(1)
    setInvincible(0)
    sprite('ma440_18', 5)	# 99-103
    sprite('ma440_19', 5)	# 104-108
    sprite('ma440_20', 5)	# 109-113
    sprite('ma440_21', 5)	# 114-118
    sprite('ma440_22', 5)	# 119-123
    sprite('ma440_23', 5)	# 124-128
    sprite('ma503_09', 5)	# 129-133
    teleportRelativeX(-30000)
    SFX_0('008_swing_pole_2')
    sprite('ma503_10', 5)	# 134-138
    sprite('ma503_11', 5)	# 139-143

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(60)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown9154(30)
        AirUntechableTime(100)
        PushbackX(3000)
        Hitstop(1)
        Unknown11072(1, 400000, 0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(100)
        Unknown9142(80)
        Unknown11069('ChangePartnerDDOD_Exe')
        Unknown11056(0)
        Unknown11064(1)
        Unknown9016(1)
        Unknown11057(750)
        setInvincible(1)

        def upon_78():
            setInvincible(1)
    sprite('ma440_00', 6)	# 1-6
    sprite('ma440_01', 6)	# 7-12
    Unknown1084(1)
    teleportRelativeX(59000)
    sprite('ma440_02', 6)	# 13-18
    sprite('ma440_03', 3)	# 19-21	 **attackbox here**
    Unknown23086(1)
    tag_voice(1, 'bma281_0', 'bma281_1', '', '')
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash1', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_04', 3)	# 22-24	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash2', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_05', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash3', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_06', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    sprite('ma440_07', 3)	# 31-33	 **attackbox here**
    sprite('ma440_08', 3)	# 34-36	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash4', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_09', 3)	# 37-39	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash5', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_03', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash1', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_04', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash2', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_05', 3)	# 46-48	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash3', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_06', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    sprite('ma440_07', 3)	# 52-54	 **attackbox here**
    sprite('ma440_08', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash4', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_08', 1)	# 57-57	 **attackbox here**
    sprite('ma440_09', 3)	# 58-60	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    Unknown3029(1)
    Unknown3069(2)
    GFX_0('maef_440_slash5', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_03', 3)	# 61-63	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash1', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_04', 3)	# 64-66	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash2', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_05', 3)	# 67-69	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash3', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_06', 3)	# 70-72	 **attackbox here**
    RefreshMultihit()
    sprite('ma440_07', 3)	# 73-75	 **attackbox here**
    sprite('ma440_08', 3)	# 76-78	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    GFX_0('maef_440_slash4', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_09', 3)	# 79-81	 **attackbox here**
    RefreshMultihit()
    Unknown11001(10, 10, 10)
    PushbackX(30400)
    Unknown23086(0)
    GFX_0('maef_440_slash5', -1)
    ScreenShake(10000, 10000)
    sprite('ma440_10', 6)	# 82-87
    sprite('ma440_14', 8)	# 88-95
    sprite('ma440_15', 8)	# 96-103
    SFX_0('006_swing_blade_2')
    sprite('ma440_16', 8)	# 104-111
    sprite('ma440_17', 4)	# 112-115	 **attackbox here**
    StartMultihit()
    physicsXImpulse(140000)
    sprite('ma440_17', 1)	# 116-116	 **attackbox here**
    SFX_1('ma282')
    tag_voice(0, 'bma282_0', 'bma282_1', '', '')
    Unknown1019(50)
    RefreshMultihit()
    Unknown11064(0)
    AttackLevel_(5)
    Damage(1420)
    Hitstop(15)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(60000)
    AirPushbackY(20000)
    Unknown11057(1000)
    SFX_0('025_cleanhit_slash')
    GFX_0('maef_440_finish', -1)
    GFX_0('maef_440_finish2', -1)
    ScreenShake(32000, 32000)
    Unknown11069('')
    sprite('ma440_17', 3)	# 117-119	 **attackbox here**
    Unknown1084(1)
    setInvincible(0)
    sprite('ma440_18', 5)	# 120-124
    sprite('ma440_19', 5)	# 125-129
    sprite('ma440_20', 5)	# 130-134
    sprite('ma440_21', 5)	# 135-139
    sprite('ma440_22', 5)	# 140-144
    sprite('ma440_23', 5)	# 145-149
    sprite('ma503_09', 5)	# 150-154
    teleportRelativeX(-30000)
    SFX_0('008_swing_pole_2')
    sprite('ma503_10', 5)	# 155-159
    sprite('ma503_11', 5)	# 160-164

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('ma600_16', 5)	# 1-5
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('ma600_15', 5)	# 6-10
    sprite('ma600_14', 5)	# 11-15
    sprite('ma600_04', 5)	# 16-20
    sprite('ma600_05', 5)	# 21-25
    sprite('ma600_06', 12)	# 26-37
    sprite('ma600_07', 4)	# 38-41
    sprite('ma600_08', 4)	# 42-45
    sprite('ma600_09', 6)	# 46-51
    sprite('ma600_10', 5)	# 52-56
    sprite('ma600_11', 6)	# 57-62
    sprite('ma600_12', 10)	# 63-72
    SFX_3('mase_00')
    label(1)
    sprite('ma600_12', 1)	# 73-73
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ma600_13', 3)	# 74-76
    sprite('ma600_14', 3)	# 77-79
    sprite('ma600_15', 3)	# 80-82
    sprite('ma600_16', 3)	# 83-85

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
    sprite('ma403_05', 3)	# 121-123	 **attackbox here**
    GFX_0('maef_403', 0)
    Unknown1086(22)
    teleportRelativeX(-15000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    sprite('ma403_06', 3)	# 124-126	 **attackbox here**
    label(1)
    sprite('ma403_05', 3)	# 127-129	 **attackbox here**
    sprite('ma403_06', 3)	# 130-132	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ma403_07', 6)	# 133-138	 **attackbox here**
    Unknown26('maef_403')
    Unknown26('maef_401_ring')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown23027()
    sprite('ma403_07', 7)	# 139-145	 **attackbox here**
    sprite('ma403_08', 10)	# 146-155
    sprite('ma403_09', 4)	# 156-159
    sprite('ma403_10', 4)	# 160-163

@State
def CmnActChangeReturnAppealBurst():
    sprite('ma111_07', 50)	# 1-50
    sprite('ma111_08', 5)	# 51-55
    sprite('ma111_09', 30)	# 56-85

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        AttackLevel_(3)
        Hitstop(14)
        AirHitstunAnimation(10)
        AirPushbackY(20000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A2nd')

        def upon_12():
            SLOT_61 = 1
        Unknown2004(1, 0)
    sprite('ma202_00', 3)	# 1-3
    sprite('ma202_01', 2)	# 4-5
    Unknown7009(2)
    GFX_0('maef_202', -1)
    sprite('ma202_02', 2)	# 6-7
    SFX_0('006_swing_blade_1')
    sprite('ma202_03', 2)	# 8-9
    sprite('ma202_04', 4)	# 10-13	 **attackbox here**
    GFX_0('maef_202_2', -1)
    sprite('ma202_05', 1)	# 14-14
    Recovery()
    Unknown2063()
    sprite('ma202_05', 2)	# 15-16
    sprite('ma202_06', 3)	# 17-19
    sprite('ma202_07', 3)	# 20-22
    sprite('ma202_08', 3)	# 23-25
    sprite('ma202_09', 2)	# 26-27
    sprite('ma202_10', 2)	# 28-29

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        PushbackX(30400)
        AirPushbackX(20000)
        AirPushbackY(14000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A3rd')
        Unknown2004(1, 0)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    teleportRelativeX(-64000)
    sprite('ma530_13', 1)	# 2-2
    sprite('ma530_01', 2)	# 3-4
    sprite('ma530_02', 2)	# 5-6
    sprite('ma530_03', 2)	# 7-8
    SFX_0('006_swing_blade_1')
    Unknown7007('626d613131395f30000000000000000064000000626d613131395f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    physicsXImpulse(50000)
    sprite('ma530_04', 3)	# 9-11	 **attackbox here**
    GFX_0('maef_530', -1)
    Unknown1019(20)
    sprite('ma530_04', 2)	# 12-13	 **attackbox here**
    Unknown1019(50)
    sprite('ma530_05', 2)	# 14-15
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('ma530_06', 3)	# 16-18
    sprite('ma530_07', 3)	# 19-21
    Unknown1019(50)
    sprite('ma530_08', 3)	# 22-24
    Unknown1019(50)
    sprite('ma530_09', 3)	# 25-27
    teleportRelativeX(-40000)
    sprite('ma530_10', 2)	# 28-29
    Unknown1084(1)
    sprite('ma530_11', 2)	# 30-31

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(250)
        Unknown11092(1)
        Unknown9154(21)
        AirUntechableTime(24)
        Hitstop(2)
        AirPushbackX(12000)
        AirPushbackY(8000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown9016(1)
        JumpCancel_(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(80)
    sprite('ma533_00', 2)	# 1-2
    Unknown1018()
    Unknown1019(40)
    sprite('ma533_01', 2)	# 3-4
    sprite('ma533_02', 2)	# 5-6
    sprite('ma533_03', 1)	# 7-7	 **attackbox here**
    StartMultihit()
    GFX_0('maef_533', -1)
    Unknown7007('626d613132325f30000000000000000064000000626d613132325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ma533_03', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    sprite('ma533_04', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    sprite('ma533_05', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    JumpCancel_(1)
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('CmnActCrushAttack')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtk5A4th')
    sprite('ma533_03ex00', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    sprite('ma533_04ex00', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    sprite('ma533_05ex00', 3)	# 23-25	 **attackbox here**
    RefreshMultihit()
    sprite('ma533_03ex00', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    sprite('ma533_04ex00', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    sprite('ma533_05ex00', 3)	# 32-34	 **attackbox here**
    RefreshMultihit()
    sprite('ma533_06', 3)	# 35-37
    Unknown26('maef_533')
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('ma533_07', 3)	# 38-40
    Unknown1019(50)
    sprite('ma501_09', 4)	# 41-44
    Unknown1084(1)
    sprite('ma501_10', 4)	# 45-48
    sprite('ma501_11', 4)	# 49-52
    sprite('ma501_12', 4)	# 53-56

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2300)
        AirUntechableTime(60)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        JumpCancel_(0)
        Unknown9016(1)
    sprite('ma340_00', 2)	# 1-2
    sprite('ma340_01', 1)	# 3-3
    sprite('ma340_01', 1)	# 4-4
    Unknown7007('626d613130355f30000000000000000064000000626d613130355f31000000000000000064000000626d613130355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma340_02', 2)	# 5-6
    sprite('ma340_04', 2)	# 7-8
    sprite('ma340_05', 2)	# 9-10
    SFX_0('006_swing_blade_1')
    physicsXImpulse(35000)
    sprite('ma340_06', 2)	# 11-12
    sprite('ma340_07', 1)	# 13-13	 **attackbox here**
    Unknown1019(30)
    GFX_0('maef_340', -1)
    sprite('ma340_07', 8)	# 14-21	 **attackbox here**
    Recovery()
    Unknown2063()
    Unknown23027()
    Unknown1019(50)
    sprite('ma340_08', 3)	# 22-24
    Unknown1019(50)
    sprite('ma340_09', 3)	# 25-27
    Unknown1019(50)
    sprite('ma340_10', 3)	# 28-30
    Unknown1019(50)
    sprite('ma340_11', 3)	# 31-33
    Unknown1019(50)
    sprite('ma340_12', 3)	# 34-36
    Unknown1019(50)
    sprite('ma340_13', 3)	# 37-39
    Unknown1019(50)
    sprite('ma340_14', 4)	# 40-43
    Unknown1019(50)
    sprite('ma340_15', 5)	# 44-48
    Unknown1019(0)

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk4A2nd')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_61 = 1
        Unknown2004(1, 0)
    sprite('ma201_00', 2)	# 1-2
    sprite('ma201_01', 1)	# 3-3
    sprite('ma201_01', 1)	# 4-4
    SFX_0('004_swing_grap_1_1')
    sprite('ma201_02', 3)	# 5-7
    Unknown7009(1)
    sprite('ma201_03', 4)	# 8-11	 **attackbox here**
    sprite('ma201_04', 4)	# 12-15
    Recovery()
    Unknown2063()
    sprite('ma201_05', 4)	# 16-19
    sprite('ma201_06', 4)	# 20-23
    sprite('ma201_07', 4)	# 24-27
    sprite('ma201_08', 4)	# 28-31

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        PushbackX(30400)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk4A3rd')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_61 = 1
    sprite('ma201_04', 1)	# 1-1
    sprite('ma530_12', 1)	# 2-2
    Unknown8000(100, 1, 1)
    sprite('ma500_01', 2)	# 3-4
    sprite('ma500_02', 2)	# 5-6
    physicsXImpulse(37500)
    Unknown7007('626d613131305f30000000000000000064000000626d613131305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_0('008_swing_pole_1')
    sprite('ma500_03', 3)	# 7-9	 **attackbox here**
    GFX_0('maef_500', -1)
    Unknown1084(1)
    sprite('ma500_04', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('ma500_05', 3)	# 13-15
    sprite('ma500_06', 3)	# 16-18
    sprite('ma500_07', 3)	# 19-21
    sprite('ma500_08', 3)	# 22-24
    sprite('ma500_09', 3)	# 25-27

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        PushbackX(40000)
        AirPushbackX(40000)
        AirPushbackY(12000)
        Unknown11056(0)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk4A4th')
    sprite('ma503_00', 3)	# 1-3
    sprite('ma503_01', 3)	# 4-6
    sprite('ma503_02', 3)	# 7-9
    sprite('ma503_03', 3)	# 10-12
    Unknown7007('626d613131335f30000000000000000064000000626d613131335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ma503_04', 3)	# 13-15
    GFX_0('maef_503', -1)
    GFX_0('maef_503_wind', -1)
    physicsXImpulse(60000)
    Unknown8004(100, 1, 1)
    Unknown8007(100, 1, 1)
    sprite('ma503_05', 4)	# 16-19	 **attackbox here**
    Unknown1019(50)
    sprite('ma503_06', 3)	# 20-22
    Unknown1019(30)
    Recovery()
    Unknown2063()
    Unknown8006(100, 1, 1)
    sprite('ma503_07', 3)	# 23-25
    Unknown1019(30)
    Unknown8006(100, 1, 1)
    sprite('ma503_08', 3)	# 26-28
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('ma503_09', 3)	# 29-31
    Unknown1019(0)
    sprite('ma503_10', 4)	# 32-35
    sprite('ma503_11', 5)	# 36-40

@State
def NmlAtk4A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2300)
        AirUntechableTime(60)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(68000)
        AirPushbackY(12000)
        JumpCancel_(0)
        Unknown9016(1)
        Unknown2004(1, 0)
    sprite('ma522_00', 4)	# 1-4
    sprite('ma522_01', 4)	# 5-8
    Unknown7007('626d613131385f30000000000000000064000000626d613131385f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ma522_02', 4)	# 9-12
    physicsXImpulse(20000)
    SFX_0('006_swing_blade_2')
    sprite('ma522_03', 3)	# 13-15	 **attackbox here**
    GFX_0('maef_522', 0)
    GFX_0('maef_522_ribon', -1)
    Unknown1019(500)
    Unknown8007(100, 1, 1)
    sprite('ma522_04', 3)	# 16-18	 **attackbox here**
    Unknown1019(20)
    sprite('ma522_05', 3)	# 19-21	 **attackbox here**
    Unknown1019(50)
    sprite('ma522_05', 3)	# 22-24	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ma522_06', 6)	# 25-30
    Unknown21015('6d6165665f353232000000000000000000000000000000000000000000000000e903000000000000')
    Unknown26('maef_522_ribon')
    Unknown1019(50)
    sprite('ma522_07', 4)	# 31-34
    Unknown1019(50)
    sprite('ma522_08', 4)	# 35-38
    Unknown1019(0)
    sprite('ma522_09', 4)	# 39-42
    sprite('ma522_10', 5)	# 43-47

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        Unknown11063(1)
        SLOT_51 = 1
        SLOT_7 = 0
        if CheckInput(0xa):
            SLOT_56 = 1

        def upon_43():
            if (SLOT_48 == 1000):
                JumpCancel_(1)
            if (SLOT_48 == 1005):
                Unknown14074('NmlAtk5B2nd')

        def upon_3():
            if CheckInput(0xe):
                SLOT_57 = 1
            if (SLOT_18 >= 120):
                SLOT_57 = 1
            if (not SLOT_57):
                if SLOT_56:
                    if SLOT_54:
                        if (SLOT_64 == 0):
                            if CheckInput(0x93):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 1
                                sendToLabel(10)
                            if CheckInput(0x45):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 2
                                sendToLabel(20)
                        if (SLOT_64 == 1):
                            if (not CheckInput(0x93)):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                        if (SLOT_64 >= 2):
                            if (not CheckInput(0x45)):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                    elif (not SLOT_57):
                        if CheckInput(0x93):
                            SLOT_64 = 1
                        elif CheckInput(0x45):
                            SLOT_64 = 2
                        else:
                            SLOT_64 = 0
            if SLOT_54:
                SLOT_55 = (SLOT_55 + 1)
                if SLOT_7:
                    Unknown23099(127)
                    SLOT_53 = (SLOT_53 + 1)
                    if (SLOT_53 >= 20):
                        SLOT_52 = 1
                        SLOT_57 = 1
                elif (SLOT_55 >= 36):
                    Unknown8004(100, 1, 0)
                    SFX_3('mase_01')
                    Unknown21015('6d6165665f445f7061727469636c655f61000000000000000000000000000000ea03000000000000')
                    Unknown21015('6d6165665f445f7061727469636c655f62000000000000000000000000000000ea03000000000000')
                    Unknown21015('6d6165665f445f7061727469636c655f63000000000000000000000000000000ea03000000000000')
                    SLOT_7 = 1
            if SLOT_52:
                if SLOT_57:
                    clearUponHandler(3)
                    if (SLOT_64 <= 1):
                        sendToLabel(50)
                    if (SLOT_64 >= 2):
                        sendToLabel(52)

        def upon_STATE_END():
            if SLOT_62:
                SLOT_6 = 1
                SLOT_62 = 0
    sprite('ma203_00', 3)	# 1-3
    SLOT_59 = 0
    sprite('ma203_01', 3)	# 4-6
    sprite('ma203_02', 2)	# 7-8
    sprite('ma203_02', 1)	# 9-9
    if SLOT_57:
        pass
    else:
        tag_voice(1, 'bma106_0', 'bma106_1', 'bma106_2', '')
    sprite('ma203_03', 1)	# 10-10
    sprite('ma203_03', 1)	# 11-11
    SLOT_54 = 1
    SLOT_56 = 0
    (SLOT_64 == 1)
    if SLOT_0:
        _gotolabel(9)
    (SLOT_64 == 2)
    if SLOT_0:
        _gotolabel(19)
    sprite('ma203_03', 1)	# 12-12
    sprite('ma203_04', 1)	# 13-13
    GFX_0('maef_D_hold', 0)
    SFX_3('mase_09')
    sprite('ma203_04', 1)	# 14-14
    gotoLabel(0)
    label(9)
    sprite('ma204_00', 2)	# 15-16
    sprite('ma204_01', 4)	# 17-20
    GFX_0('maef_203_up2', 0)
    SFX_3('mase_09')
    sprite('ma204_02', 3)	# 21-23
    SLOT_52 = 1
    SLOT_56 = 1
    loopRest()
    gotoLabel(11)
    label(19)
    sprite('ma205_00', 2)	# 24-25
    sprite('ma205_01', 4)	# 26-29
    GFX_0('maef_203_down2', 0)
    SFX_3('mase_09')
    sprite('ma205_02', 3)	# 30-32
    SLOT_52 = 1
    SLOT_56 = 1
    loopRest()
    gotoLabel(21)
    label(0)
    sprite('ma203_04', 3)	# 33-35
    GFX_0('maef_D_hold', 0)
    sprite('ma203_05', 3)	# 36-38
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma203_06', 3)	# 39-41
    label(1)
    sprite('ma203_05', 3)	# 42-44
    sprite('ma203_06', 3)	# 45-47
    sprite('ma203_04', 3)	# 48-50
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ma204_00', 3)	# 51-53
    GFX_0('maef_203_up', 0)
    sprite('ma204_01', 3)	# 54-56
    GFX_0('maef_203_up2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma204_02', 3)	# 57-59
    label(11)
    sprite('ma204_03', 3)	# 60-62
    sprite('ma204_01', 3)	# 63-65
    sprite('ma204_02', 3)	# 66-68
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('ma205_00', 3)	# 69-71
    GFX_0('maef_203_down', 0)
    sprite('ma205_01', 3)	# 72-74
    GFX_0('maef_203_down2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma205_02', 3)	# 75-77
    label(21)
    sprite('ma205_03', 3)	# 78-80
    sprite('ma205_01', 3)	# 81-83
    sprite('ma205_02', 3)	# 84-86
    loopRest()
    gotoLabel(21)
    label(50)
    sprite('keep', 3)	# 87-89
    sprite('ma203_07', 3)	# 90-92
    Unknown23183('6d613230345f3034000000000000000000000000000000000000000000000000030000000200000040000000')
    tag_voice(0, 'bma107_0', 'bma107_1', 'bma107_2', '')
    Unknown14070('NmlAtk5B2nd')
    sprite('ma203_08', 3)	# 93-95
    SLOT_62 = 1
    Unknown26('maef_D')
    if SLOT_64:
        GFX_0('ma203Shot', 1)
        Unknown38(11, 1)
        Unknown23029(11, 1008, 0)
        SFX_3('mase_02')
    else:
        GFX_0('ma203Shot', 0)
        Unknown38(11, 1)
        Unknown23029(11, 1006, 0)
        SFX_3('mase_02')
    sprite('ma203_09', 3)	# 96-98
    Unknown14072('NmlAtk5B2nd')
    Unknown23099(0)
    sprite('ma203_10', 3)	# 99-101
    sprite('ma203_11', 3)	# 102-104
    sprite('ma203_09', 3)	# 105-107
    sprite('ma203_10', 3)	# 108-110
    sprite('ma203_11', 3)	# 111-113
    sprite('ma203_09', 2)	# 114-115
    loopRest()
    gotoLabel(99)
    label(52)
    sprite('keep', 3)	# 116-118
    sprite('ma205_04', 3)	# 119-121
    tag_voice(0, 'bma107_0', 'bma107_1', 'bma107_2', '')
    Unknown14070('NmlAtk5B2nd')
    sprite('ma203_09', 3)	# 122-124
    SLOT_62 = 1
    Unknown26('maef_D')
    GFX_0('ma203Shot', 0)
    Unknown38(11, 1)
    Unknown23029(11, 1007, 0)
    SFX_3('mase_02')
    sprite('ma203_10', 3)	# 125-127
    Unknown14072('NmlAtk5B2nd')
    Unknown23099(0)
    sprite('ma203_11', 3)	# 128-130
    sprite('ma203_09', 3)	# 131-133
    sprite('ma203_10', 3)	# 134-136
    sprite('ma203_11', 3)	# 137-139
    sprite('ma203_09', 3)	# 140-142
    sprite('ma203_10', 2)	# 143-144
    label(99)
    sprite('keep', 1)	# 145-145
    Unknown14074('NmlAtk5B2nd')
    sprite('ma203_12', 4)	# 146-149
    sprite('ma203_13', 4)	# 150-153
    SLOT_51 = 0
    sprite('ma203_14', 4)	# 154-157
    GFX_0('maef_catch', 0)
    Unknown36(1)
    Unknown1072(34000)
    Unknown35()
    Unknown23029(11, 1003, 0)
    SLOT_62 = 0
    sprite('ma203_15', 4)	# 158-161
    sprite('ma203_16', 4)	# 162-165
    sprite('ma203_17', 4)	# 166-169

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 1000):
                SLOT_51 = 1
                callSubroutine('DeriveInputBegin')

        def upon_3():
            if SLOT_52:
                if SLOT_51:
                    callSubroutine('DeriveTimingBegin')

        def upon_STATE_END():
            Unknown23029(11, 1003, 0)
            SLOT_62 = 0
        SLOT_62 = 1
    sprite('keep', 1)	# 1-1
    sprite('ma203_18', 3)	# 2-4
    sprite('ma203_19', 3)	# 5-7
    Unknown23029(11, 1004, 0)
    sprite('ma203_20', 3)	# 8-10
    sprite('ma203_21', 3)	# 11-13
    sprite('ma203_22', 3)	# 14-16
    sprite('ma203_23', 3)	# 17-19
    sprite('ma203_21', 3)	# 20-22
    SLOT_52 = 1
    sprite('ma203_22', 3)	# 23-25
    sprite('ma203_24', 4)	# 26-29
    sprite('ma203_14', 4)	# 30-33
    GFX_0('maef_catch', 0)
    Unknown36(1)
    Unknown1072(35000)
    Unknown35()
    Unknown23029(11, 1003, 0)
    SLOT_62 = 0
    sprite('ma203_15', 4)	# 34-37
    sprite('ma203_16', 4)	# 38-41
    sprite('ma203_17', 3)	# 42-44

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    Unknown23145('NmlAtk2A')
    if SLOT_0:
        _gotolabel(1)
    sprite('ma230_00', 2)	# 1-2
    Unknown1051(60)
    sprite('ma230_01', 2)	# 3-4
    SFX_0('004_swing_grap_1_0')
    sprite('ma230_02', 2)	# 5-6
    gotoLabel(9)
    label(1)
    sprite('ma230_01', 3)	# 7-9
    Unknown1051(60)
    SFX_0('004_swing_grap_1_0')
    sprite('ma230_02', 3)	# 10-12
    label(9)
    sprite('ma230_03', 1)	# 13-13	 **attackbox here**
    Unknown7009(0)
    sprite('ma230_03', 2)	# 14-15	 **attackbox here**
    sprite('ma230_04', 3)	# 16-18
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('ma230_02', 3)	# 19-21
    sprite('ma230_01', 3)	# 22-24
    sprite('ma230_00', 3)	# 25-27

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        AirUntechableTime(24)
        AirPushbackX(8000)
        AirPushbackY(32000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_61 = 1
    sprite('ma232_00', 3)	# 1-3
    sprite('ma232_01', 3)	# 4-6
    Unknown7009(2)
    sprite('ma232_02', 3)	# 7-9
    SFX_0('006_swing_blade_1')
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ma232_03', 3)	# 10-12
    sprite('ma232_04', 4)	# 13-16	 **attackbox here**
    GFX_0('maef_232', -1)
    sprite('ma232_05', 5)	# 17-21
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ma232_06', 5)	# 22-26
    sprite('ma232_07', 5)	# 27-31
    sprite('ma232_08', 5)	# 32-36
    sprite('ma232_09', 5)	# 37-41
    sprite('ma232_10', 5)	# 42-46

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirUntechableTime(40)
        Hitstop(6)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(4000)
        AirPushbackY(16000)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        Unknown2004(1, 0)
    sprite('ma231_00', 3)	# 1-3
    sprite('ma231_01', 2)	# 4-5
    SFX_0('008_swing_pole_1')
    sprite('ma231_02', 2)	# 6-7
    sprite('ma231_03', 2)	# 8-9
    Unknown7009(1)
    GFX_0('maef_231', -1)
    sprite('ma231_04', 3)	# 10-12	 **attackbox here**
    sprite('ma231_05', 1)	# 13-13
    sprite('ma540_11', 3)	# 14-16
    teleportRelativeX(25000)
    sprite('ma540_12', 3)	# 17-19
    sprite('ma540_02', 2)	# 20-21
    Unknown7007('626d613132335f30000000000000000064000000626d613132335f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ma540_03', 2)	# 22-23
    GFX_0('maef_540', -1)
    SFX_0('006_swing_blade_1')
    sprite('ma540_04', 3)	# 24-26	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Hitstop(12)
    AirPushbackX(20000)
    AirPushbackY(18000)
    Unknown9016(1)
    sprite('ma540_05', 3)	# 27-29	 **attackbox here**
    sprite('ma540_06', 3)	# 30-32
    Recovery()
    Unknown2063()
    sprite('ma540_07', 4)	# 33-36
    sprite('ma540_08', 4)	# 37-40
    sprite('ma540_09', 4)	# 41-44
    sprite('ma540_10', 4)	# 45-48

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        AirPushbackX(3000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ma252_00', 2)	# 1-2
    sprite('ma252_01', 2)	# 3-4
    sprite('ma252_02', 3)	# 5-7
    Unknown7009(2)
    SFX_0('006_swing_blade_1')
    sprite('ma252_03', 3)	# 8-10
    sprite('ma252_04', 4)	# 11-14	 **attackbox here**
    GFX_0('maef_252', -1)
    sprite('ma252_05', 4)	# 15-18
    Recovery()
    Unknown2063()
    sprite('ma252_06', 4)	# 19-22
    sprite('ma252_07', 4)	# 23-26
    sprite('ma252_08', 4)	# 27-30
    sprite('ma252_09', 4)	# 31-34
    sprite('ma252_10', 4)	# 35-38

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(23)
        AirPushbackX(3000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ma322_00', 3)	# 1-3
    sprite('ma322_01', 2)	# 4-5
    sprite('ma322_02', 2)	# 6-7
    sprite('ma322_03', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    sprite('ma322_04ex', 3)	# 10-12	 **attackbox here**
    sprite('ma322_05', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('ma322_06', 4)	# 17-20

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        Unknown1017()
        Unknown1022()
        Unknown23001(0, 0)
        SLOT_51 = 1
        SLOT_7 = 0
        if CheckInput(0xa):
            SLOT_56 = 1

        def upon_43():
            if (SLOT_48 == 1000):
                JumpCancel_(1)
            if (SLOT_48 == 1005):
                Unknown14074('NmlAtkAIR5B2nd')

        def upon_3():
            if CheckInput(0xe):
                SLOT_57 = 1
            if (SLOT_18 >= 60):
                SLOT_57 = 1
            if (not SLOT_57):
                if SLOT_56:
                    if SLOT_54:
                        if (SLOT_64 == 0):
                            if CheckInput(0x93):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 1
                                sendToLabel(10)
                            if CheckInput(0x45):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 2
                                sendToLabel(20)
                        if (SLOT_64 == 1):
                            if (not CheckInput(0x93)):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                        if (SLOT_64 >= 2):
                            if (not CheckInput(0x45)):
                                SLOT_52 = 0
                                SLOT_56 = 0
                                SLOT_55 = 1
                                SLOT_64 = 0
                                sendToLabel(0)
                    elif (not SLOT_57):
                        if CheckInput(0x93):
                            SLOT_64 = 1
                        elif CheckInput(0x45):
                            SLOT_64 = 2
                        else:
                            SLOT_64 = 0
            if SLOT_54:
                SLOT_55 = (SLOT_55 + 1)
                if SLOT_7:
                    Unknown23099(127)
                    SLOT_53 = (SLOT_53 + 1)
                    if (SLOT_53 >= 20):
                        SLOT_52 = 1
                        SLOT_57 = 1
                elif (SLOT_55 >= 36):
                    ScreenShake(0, 5000)
                    SFX_3('mase_01')
                    Unknown21015('6d6165665f445f7061727469636c655f61000000000000000000000000000000ea03000000000000')
                    Unknown21015('6d6165665f445f7061727469636c655f62000000000000000000000000000000ea03000000000000')
                    Unknown21015('6d6165665f445f7061727469636c655f63000000000000000000000000000000ea03000000000000')
                    SLOT_7 = 1
            if SLOT_52:
                if SLOT_57:
                    clearUponHandler(3)
                    sendToLabel(50)

        def upon_LANDING():
            Unknown23029(11, 1003, 0)
            Unknown26('maef_D')
    sprite('ma253_00', 3)	# 1-3
    SLOT_59 = 0
    sprite('ma253_01', 3)	# 4-6
    Unknown22004(9, 1)
    sprite('ma253_02', 2)	# 7-8
    Unknown1084(1)
    Unknown1018()
    Unknown1023()
    Unknown1019(50)
    YAccel(50)
    sprite('ma253_02', 1)	# 9-9
    if SLOT_57:
        tag_voice(1, 'bma106_0', 'bma106_1', '', '')
    else:
        tag_voice(1, 'bma106_0', 'bma106_1', 'bma106_2', '')
    sprite('ma253_03', 2)	# 10-11
    Unknown1019(20)
    YAccel(30)
    sprite('ma253_03', 1)	# 12-12
    SLOT_54 = 1
    SLOT_56 = 0
    (SLOT_64 == 1)
    if SLOT_0:
        _gotolabel(9)
    (SLOT_64 == 2)
    if SLOT_0:
        _gotolabel(19)
    sprite('ma254_00', 3)	# 13-15
    YAccel(10)
    setGravity(50)
    sprite('ma254_01', 3)	# 16-18
    GFX_0('maef_AirD_hold', 0)
    SFX_3('mase_09')
    sprite('ma254_02', 1)	# 19-19
    sprite('ma254_02', 2)	# 20-21
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma254_03', 3)	# 22-24
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ma253_04', 3)	# 25-27
    YAccel(10)
    setGravity(50)
    sprite('ma253_04', 3)	# 28-30
    GFX_0('maef_253_up2', 0)
    SFX_3('mase_09')
    sprite('ma253_05', 1)	# 31-31
    sprite('ma253_05', 2)	# 32-33
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma253_06', 3)	# 34-36
    loopRest()
    gotoLabel(11)
    label(19)
    sprite('ma255_00', 3)	# 37-39
    YAccel(10)
    setGravity(50)
    sprite('ma255_01', 3)	# 40-42
    GFX_0('maef_253_down2', 0)
    SFX_3('mase_09')
    sprite('ma255_02', 1)	# 43-43
    sprite('ma255_02', 2)	# 44-45
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma255_03', 3)	# 46-48
    loopRest()
    gotoLabel(21)
    label(0)
    sprite('ma254_01', 3)	# 49-51
    GFX_0('maef_AirD_hold', 0)
    sprite('ma254_02', 3)	# 52-54
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma254_03', 3)	# 55-57
    label(1)
    sprite('ma254_01', 3)	# 58-60
    sprite('ma254_02', 3)	# 61-63
    sprite('ma254_03', 3)	# 64-66
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ma254_00', 3)	# 67-69
    GFX_0('maef_253_up', 0)
    sprite('ma253_04', 3)	# 70-72
    GFX_0('maef_253_up2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma253_05', 3)	# 73-75
    label(11)
    sprite('ma253_04', 3)	# 76-78
    sprite('ma253_05', 3)	# 79-81
    sprite('ma253_06', 3)	# 82-84
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('ma255_00', 3)	# 85-87
    GFX_0('maef_253_down', 0)
    sprite('ma255_01', 3)	# 88-90
    GFX_0('maef_253_down2', 0)
    SLOT_52 = 1
    SLOT_56 = 1
    sprite('ma255_02', 3)	# 91-93
    label(21)
    sprite('ma255_01', 3)	# 94-96
    sprite('ma255_02', 3)	# 97-99
    sprite('ma255_03', 3)	# 100-102
    loopRest()
    gotoLabel(21)
    label(50)
    sprite('keep', 3)	# 103-105
    sprite('ma254_04', 3)	# 106-108
    (SLOT_64 >= 2)
    Unknown23183('6d613235355f3034000000000000000000000000000000000000000000000000030000000200000000000000')
    (SLOT_64 == 1)
    Unknown23183('6d613235335f3037000000000000000000000000000000000000000000000000030000000200000000000000')
    tag_voice(0, 'bma107_0', 'bma107_1', 'bma107_2', '')
    Unknown14070('NmlAtkAIR5B2nd')
    sprite('ma253_08', 3)	# 109-111
    SLOT_62 = 1
    Unknown26('maef_D')
    if SLOT_64:
        if (SLOT_64 >= 2):
            GFX_0('ma203Shot', 2)
            Unknown38(11, 1)
            Unknown23029(11, 1010, 0)
            SFX_3('mase_02')
        else:
            GFX_0('ma203Shot', 0)
            Unknown38(11, 1)
            Unknown23029(11, 1011, 0)
            SFX_3('mase_02')
    else:
        GFX_0('ma203Shot', 1)
        Unknown38(11, 1)
        Unknown23029(11, 1009, 0)
        SFX_3('mase_02')
    sprite('ma253_09', 3)	# 112-114
    Unknown1022()
    Unknown1084(1)
    Unknown14072('NmlAtkAIR5B2nd')
    Unknown23099(0)
    sprite('ma253_10', 3)	# 115-117
    sprite('ma253_11', 3)	# 118-120
    sprite('ma253_09', 3)	# 121-123
    sprite('ma253_10', 3)	# 124-126
    sprite('ma253_11', 3)	# 127-129
    sprite('ma253_09', 2)	# 130-131
    label(99)
    sprite('keep', 1)	# 132-132
    Unknown14074('NmlAtkAIR5B2nd')
    Unknown1023()
    Unknown1043()
    sprite('ma253_12', 4)	# 133-136
    sprite('ma253_13', 4)	# 137-140
    sprite('ma253_14', 4)	# 141-144
    GFX_0('maef_catch', 0)
    Unknown36(1)
    Unknown1072(-35000)
    Unknown35()
    Unknown23029(11, 1003, 0)
    SLOT_62 = 0
    sprite('ma253_15', 4)	# 145-148
    sprite('ma253_16', 4)	# 149-152
    sprite('ma253_17', 4)	# 153-156
    sprite('ma020_05', 3)	# 157-159
    Recovery()
    sprite('ma020_06', 3)	# 160-162
    label(999)
    sprite('ma020_07', 4)	# 163-166
    sprite('ma020_08', 4)	# 167-170
    gotoLabel(999)

@State
def NmlAtkAIR5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 1000):
                SLOT_51 = 1
                Unknown14070('Backflip')
                Unknown14070('Backflip_A_nama')
                Unknown14070('Backflip_B_nama')
                Unknown14070('Backflip_C_nama')
                Unknown14070('CmnActInvincibleAttackAir')

        def upon_3():
            if SLOT_52:
                if SLOT_51:
                    Unknown14072('Backflip')
                    Unknown14072('Backflip_A_nama')
                    Unknown14072('Backflip_B_nama')
                    Unknown14072('Backflip_C_nama')
                    Unknown14072('CmnActInvincibleAttackAir')

        def upon_LANDING():
            Unknown23029(11, 1003, 0)

        def upon_STATE_END():
            Unknown23029(11, 1003, 0)
            SLOT_62 = 0
        SLOT_62 = 1
    sprite('keep', 1)	# 1-1
    sprite('ma253_18', 3)	# 2-4
    sprite('ma253_19', 3)	# 5-7
    Unknown23029(11, 1004, 0)
    sprite('ma253_20', 3)	# 8-10
    sprite('ma253_21', 3)	# 11-13
    SLOT_52 = 1
    sprite('ma253_22', 3)	# 14-16
    sprite('ma253_23', 3)	# 17-19
    sprite('ma253_21', 3)	# 20-22
    sprite('ma253_22', 3)	# 23-25
    Unknown1043()
    sprite('ma253_24', 4)	# 26-29
    sprite('ma253_14', 4)	# 30-33
    GFX_0('maef_catch', 0)
    Unknown36(1)
    Unknown1072(-35000)
    Unknown35()
    Unknown23029(11, 1003, 0)
    SLOT_62 = 0
    sprite('ma253_15', 4)	# 34-37
    sprite('ma253_16', 4)	# 38-41
    sprite('ma253_17', 3)	# 42-44
    sprite('ma020_05', 3)	# 45-47
    Recovery()
    sprite('ma020_06', 3)	# 48-50
    label(999)
    sprite('ma020_07', 4)	# 51-54
    sprite('ma020_08', 4)	# 55-58
    gotoLabel(999)

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        AttackP2(80)
        AirUntechableTime(26)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(23000)
        AirPushbackY(22000)
        HitOverhead(0)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockJumpCancel(1)
        Unknown22004(4, 1)
        Unknown9016(1)
    sprite('ma321_00', 2)	# 1-2
    StartMultihit()
    sprite('ma321_01', 1)	# 3-3
    StartMultihit()
    sprite('ma321_02', 1)	# 4-4	 **attackbox here**
    Unknown7007('626d613131395f30000000000000000064000000626d613131395f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    StartMultihit()
    sprite('ma321_03', 1)	# 5-5
    sprite('ma321_04', 2)	# 6-7
    Unknown1019(60)
    physicsYImpulse(10000)
    setGravity(2000)
    sprite('ma321_05', 2)	# 8-9
    sprite('ma321_06', 2)	# 10-11
    sprite('ma321_07', 3)	# 12-14
    SFX_0('006_swing_blade_1')
    sprite('ma321_08', 2)	# 15-16
    sprite('ma321_09', 6)	# 17-22	 **attackbox here**
    GFX_0('maef_321', -1)
    sprite('ma321_10', 4)	# 23-26
    Recovery()
    Unknown2063()
    sprite('ma321_11', 4)	# 27-30
    sprite('ma321_12', 4)	# 31-34
    sprite('ma321_13', 4)	# 35-38
    sprite('ma321_14', 4)	# 39-42

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown2004(1, 0)

        def upon_STATE_END():
            Unknown2015(-1)
    sprite('ma532_00', 3)	# 1-3
    Unknown1018()
    Unknown1019(80)
    sprite('ma532_01', 2)	# 4-5
    Unknown1019(80)
    tag_voice(1, 'bma156_0', 'bma156_1', '', '')
    sprite('ma532_02', 2)	# 6-7
    SFX_0('019_cloth_b')
    Unknown1019(80)
    sprite('ma532_03', 3)	# 8-10
    Unknown2015(200)
    sprite('ma532_04', 3)	# 11-13
    sprite('ma532_05', 3)	# 14-16
    sprite('ma532_06', 3)	# 17-19
    physicsXImpulse(15000)
    SFX_0('004_swing_grap_1_2')
    sprite('ma532_07', 3)	# 20-22
    sprite('ma532_08', 3)	# 23-25
    Unknown1019(200)
    sprite('ma532_09', 3)	# 26-28	 **attackbox here**
    Unknown1084(1)
    teleportRelativeX(380000)
    Unknown8000(100, 1, 1)
    sprite('ma532_09', 5)	# 29-33	 **attackbox here**
    Unknown2003(1)
    sprite('ma532_10', 4)	# 34-37	 **attackbox here**
    sprite('ma532_11', 3)	# 38-40
    sprite('ma532_12', 3)	# 41-43
    sprite('ma532_13', 3)	# 44-46

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
    sprite('ma531_06ex01', 2)	# 2-3	 **attackbox here**
    Unknown23027()
    sprite('ma531_07', 5)	# 4-8	 **attackbox here**
    sprite('ma531_08', 4)	# 9-12
    sprite('ma531_09', 3)	# 13-15
    sprite('ma531_10', 2)	# 16-17
    Unknown2015(-1)
    sprite('ma531_11', 2)	# 18-19
    sprite('ma531_12', 2)	# 20-21
    sprite('ma201_00', 3)	# 22-24
    sprite('ma201_01', 3)	# 25-27
    SFX_0('004_swing_grap_1_1')
    tag_voice(0, 'bma157_0', 'bma157_1', '', '')
    sprite('ma201_02', 2)	# 28-29
    sprite('ma201_03', 4)	# 30-33	 **attackbox here**
    RefreshMultihit()
    sprite('ma201_03', 2)	# 34-35	 **attackbox here**
    StartMultihit()
    sprite('ma201_04', 7)	# 36-42
    label(0)
    sprite('ma000_00', 7)	# 43-49
    sprite('ma000_01', 7)	# 50-56
    sprite('ma000_02', 7)	# 57-63
    sprite('ma000_03', 7)	# 64-70
    sprite('ma000_04', 7)	# 71-77
    sprite('ma000_05', 7)	# 78-84
    sprite('ma000_06', 7)	# 85-91
    sprite('ma000_07', 7)	# 92-98
    sprite('ma000_08', 7)	# 99-105
    sprite('ma000_09', 7)	# 106-112
    sprite('ma000_10', 7)	# 113-119
    sprite('ma000_11', 7)	# 120-126
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 127-127

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('ma510_11', 4)	# 2-5
    sprite('ma510_01', 4)	# 6-9
    sprite('ma510_02', 3)	# 10-12
    sprite('ma510_03', 2)	# 13-14
    sprite('ma510_04', 4)	# 15-18	 **attackbox here**
    RefreshMultihit()
    sprite('ma510_05', 4)	# 19-22
    sprite('ma510_06', 4)	# 23-26
    label(0)
    sprite('ma511_00', 4)	# 27-30
    sprite('ma511_01', 2)	# 31-32
    sprite('ma511_01', 2)	# 33-34
    sprite('ma511_02', 4)	# 35-38
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 39-39
    sprite('ma510_07', 2)	# 40-41
    sprite('ma510_08', 2)	# 42-43
    sprite('ma510_09', 2)	# 44-45
    sprite('ma510_10', 2)	# 46-47

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
        Unknown2004(1, 0)
    sprite('keep', 1)	# 1-1
    sprite('ma522_00', 6)	# 2-7
    sprite('ma522_01', 6)	# 8-13
    tag_voice(0, 'bma158_0', 'bma158_1', '', '')
    sprite('ma522_02', 6)	# 14-19
    SFX_0('006_swing_blade_2')
    sprite('ma522_03', 3)	# 20-22	 **attackbox here**
    GFX_0('maef_522', 0)
    GFX_0('maef_522_ribon', -1)
    Unknown8007(100, 1, 1)
    sprite('ma522_04', 3)	# 23-25	 **attackbox here**
    sprite('ma522_05', 3)	# 26-28	 **attackbox here**
    sprite('ma522_04', 3)	# 29-31	 **attackbox here**
    sprite('ma522_05', 3)	# 32-34	 **attackbox here**
    sprite('ma522_04', 3)	# 35-37	 **attackbox here**
    sprite('ma522_05', 3)	# 38-40	 **attackbox here**
    sprite('ma522_06', 5)	# 41-45
    Unknown21015('6d6165665f353232000000000000000000000000000000000000000000000000e903000000000000')
    Unknown26('maef_522_ribon')
    sprite('ma522_07', 4)	# 46-49
    sprite('ma522_08', 4)	# 50-53
    sprite('ma522_09', 4)	# 54-57
    sprite('ma522_10', 3)	# 58-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown23027()
        Unknown30073(1)
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 15)	# 1-15
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 16-16
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    sprite('ma403_11', 2)	# 17-18
    Unknown1007(250000)
    sprite('ma403_12ex', 2)	# 19-20
    sprite('ma403_13ex', 2)	# 21-22
    sprite('ma403_14ex', 2)	# 23-24
    sprite('ma403_15ex', 2)	# 25-26
    sprite('ma403_20', 3)	# 27-29	 **attackbox here**
    Unknown1109(75000, -20000)
    GFX_0('maef_403C', 0)
    SFX_3('mase_05')
    sprite('ma403_21', 3)	# 30-32	 **attackbox here**
    label(0)
    sprite('ma403_20', 3)	# 33-35	 **attackbox here**
    sprite('ma403_21', 3)	# 36-38	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ma403_18', 2)	# 39-40	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    physicsYImpulse(0)
    Unknown26('maef_403C')
    Unknown26('maef_401_ring')
    Unknown8000(100, 1, 1)
    sprite('ma403_18', 4)	# 41-44	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('ma403_19', 8)	# 45-52
    sprite('ma403_09', 3)	# 53-55
    Unknown1084(1)
    sprite('ma403_10', 3)	# 56-58
    label(2)
    sprite('ma000_00', 7)	# 59-65
    sprite('ma000_01', 7)	# 66-72
    sprite('ma000_02', 7)	# 73-79
    sprite('ma000_03', 7)	# 80-86
    sprite('ma000_04', 7)	# 87-93
    sprite('ma000_05', 7)	# 94-100
    sprite('ma000_06', 7)	# 101-107
    sprite('ma000_07', 7)	# 108-114
    sprite('ma000_08', 7)	# 115-121
    sprite('ma000_09', 7)	# 122-128
    sprite('ma000_10', 7)	# 129-135
    sprite('ma000_11', 7)	# 136-142
    gotoLabel(2)
    label(1)
    sprite('keep', 1)	# 143-143

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown2004(1, 0)
    sprite('ma520_00', 3)	# 1-3
    sprite('ma520_01', 3)	# 4-6
    sprite('ma520_02', 3)	# 7-9
    SFX_0('004_swing_grap_1_1')
    sprite('ma520_03', 2)	# 10-11
    GFX_0('maef_520_slash', -1)
    sprite('ma520_04', 3)	# 12-14	 **attackbox here**
    sprite('ma520_06', 4)	# 15-18
    sprite('ma520_07', 4)	# 19-22
    label(0)
    sprite('ma511_00', 4)	# 23-26
    sprite('ma511_01', 2)	# 27-28
    sprite('ma511_01', 2)	# 29-30
    sprite('ma511_02', 4)	# 31-34
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 35-35
    sprite('ma510_07', 2)	# 36-37
    sprite('ma510_08', 2)	# 38-39
    sprite('ma510_09', 2)	# 40-41
    sprite('ma510_10', 2)	# 42-43

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown9016(1)
        Unknown30075(1)
        Unknown2004(1, 0)
    sprite('keep', 1)	# 1-1
    sprite('ma522_00', 6)	# 2-7
    sprite('ma522_01', 6)	# 8-13
    sprite('ma522_02', 6)	# 14-19
    SFX_0('006_swing_blade_2')
    sprite('ma522_03', 3)	# 20-22	 **attackbox here**
    GFX_0('maef_522', 0)
    GFX_0('maef_522_ribon', -1)
    Unknown8007(100, 1, 1)
    sprite('ma522_04', 3)	# 23-25	 **attackbox here**
    sprite('ma522_05', 3)	# 26-28	 **attackbox here**
    sprite('ma522_04', 3)	# 29-31	 **attackbox here**
    sprite('ma522_05', 3)	# 32-34	 **attackbox here**
    sprite('ma522_04', 3)	# 35-37	 **attackbox here**
    sprite('ma522_05', 3)	# 38-40	 **attackbox here**
    sprite('ma522_06', 5)	# 41-45
    Unknown21015('6d6165665f353232000000000000000000000000000000000000000000000000e903000000000000')
    Unknown26('maef_522_ribon')
    sprite('ma522_07', 4)	# 46-49
    sprite('ma522_08', 4)	# 50-53
    sprite('ma522_09', 4)	# 54-57
    sprite('ma522_10', 3)	# 58-60

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
    sprite('ma032_00', 2)	# 1-2
    label(0)
    sprite('ma032_01', 4)	# 3-6
    sprite('ma032_02', 3)	# 7-9
    sprite('ma032_03', 3)	# 10-12
    Unknown8006(100, 1, 1)
    sprite('ma032_04', 3)	# 13-15
    sprite('ma032_05', 3)	# 16-18
    sprite('ma032_06', 4)	# 19-22
    sprite('ma032_07', 3)	# 23-25
    sprite('ma032_08', 3)	# 26-28
    Unknown8006(100, 1, 1)
    sprite('ma032_09', 3)	# 29-31
    sprite('ma032_10', 3)	# 32-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ma310_00', 1)	# 35-35
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ma310_01', 2)	# 36-37
    sprite('ma310_02', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('ma310_03', 3)	# 41-43
    SFX_0('010_swing_sword_0')
    sprite('ma310_04', 3)	# 44-46
    SFX_1('bma154')
    sprite('ma310_05', 11)	# 47-57
    sprite('ma310_06', 3)	# 58-60
    sprite('ma310_07', 3)	# 61-63

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirUntechableTime(80)
        AirPushbackX(1000)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(2400)
        Unknown9016(1)
        Unknown11069('ThrowExe')
        JumpCancel_(0)
    sprite('ma310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ma311_00', 4)	# 4-7
    Unknown2015(100)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_1('bma153')
    sprite('ma311_01', 4)	# 8-11
    Unknown2015(200)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_0('006_swing_blade_1')
    sprite('ma311_02', 4)	# 12-15
    Unknown2015(300)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ma311_03', 8)	# 16-23	 **attackbox here**
    Unknown2015(400)
    Unknown36(22)
    Unknown2035(1)
    GFX_1('maef_311shadow', -1)
    Unknown35()
    sprite('ma311_04', 4)	# 24-27
    Unknown2015(500)
    sprite('ma311_05', 4)	# 28-31
    Unknown2015(-1)
    sprite('ma311_05ex1', 4)	# 32-35
    sprite('ma311_05ex2', 14)	# 36-49
    sprite('ma311_05ex2', 8)	# 50-57
    GFX_0('maef_311_shadow2', -1)
    sprite('ma311_06', 4)	# 58-61
    sprite('ma311_07', 4)	# 62-65
    SFX_0('006_swing_blade_1')
    sprite('ma311_08', 3)	# 66-68	 **attackbox here**
    GFX_0('maef_311', -1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    Hitstop(12)
    AttackP2(50)
    AirPushbackX(3000)
    AirPushbackY(-60000)
    Unknown9095()
    Unknown9190(1)
    Unknown9118(30)
    Unknown9310(1)
    Unknown11069('')

    def upon_12():
        JumpCancel_(1)
    sprite('ma311_09', 3)	# 69-71
    sprite('ma311_10', 3)	# 72-74
    sprite('ma311_11', 3)	# 75-77
    sprite('ma311_12', 3)	# 78-80
    sprite('ma311_13', 3)	# 81-83
    sprite('ma311_14', 3)	# 84-86

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
    sprite('ma032_00', 2)	# 1-2
    label(0)
    sprite('ma032_01', 4)	# 3-6
    sprite('ma032_02', 3)	# 7-9
    sprite('ma032_03', 3)	# 10-12
    Unknown8006(100, 1, 1)
    sprite('ma032_04', 3)	# 13-15
    sprite('ma032_05', 3)	# 16-18
    sprite('ma032_06', 4)	# 19-22
    sprite('ma032_07', 3)	# 23-25
    sprite('ma032_08', 3)	# 26-28
    Unknown8006(100, 1, 1)
    sprite('ma032_09', 3)	# 29-31
    sprite('ma032_10', 3)	# 32-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ma310_00', 1)	# 35-35
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ma310_01', 2)	# 36-37
    sprite('ma310_02', 3)	# 38-40	 **attackbox here**
    Unknown1084(1)
    sprite('ma310_03', 3)	# 41-43
    SFX_0('010_swing_sword_0')
    sprite('ma310_04', 3)	# 44-46
    SFX_1('bma154')
    sprite('ma310_05', 11)	# 47-57
    sprite('ma310_06', 3)	# 58-60
    sprite('ma310_07', 3)	# 61-63

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(80)
        Hitstop(0)
        AirPushbackX(-7000)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(2400)
        Unknown9016(1)
        Unknown11069('BackThrowExe')
        JumpCancel_(0)
    sprite('ma310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ma311_00', 4)	# 4-7
    Unknown2015(100)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_1('bma153')
    sprite('ma311_01', 4)	# 8-11
    Unknown2015(200)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_0('006_swing_blade_1')
    sprite('ma311_02', 4)	# 12-15
    Unknown2015(300)
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ma311_03', 8)	# 16-23	 **attackbox here**
    Unknown2015(400)
    Unknown36(22)
    Unknown2035(1)
    GFX_1('maef_311shadow', -1)
    Unknown35()
    sprite('ma311_04', 4)	# 24-27
    Unknown2015(500)
    sprite('ma311_05', 4)	# 28-31
    Unknown2015(-1)
    sprite('ma311_05ex1', 4)	# 32-35
    sprite('ma311_05ex2', 14)	# 36-49
    sprite('ma311_05ex2', 8)	# 50-57
    Unknown2006()
    GFX_0('maef_311_shadow2_b', -1)
    sprite('ma311_06', 4)	# 58-61
    sprite('ma311_07', 4)	# 62-65
    SFX_0('006_swing_blade_1')
    sprite('ma311_08', 3)	# 66-68	 **attackbox here**
    GFX_0('maef_311', -1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    Hitstop(12)
    AttackP2(50)
    AirPushbackX(3000)
    AirPushbackY(-60000)
    Unknown9095()
    Unknown9190(1)
    Unknown9118(30)
    Unknown9310(1)
    Unknown11069('')

    def upon_12():
        JumpCancel_(1)
    sprite('ma311_09', 3)	# 69-71
    sprite('ma311_10', 3)	# 72-74
    sprite('ma311_11', 3)	# 75-77
    sprite('ma311_12', 3)	# 78-80
    sprite('ma311_13', 3)	# 81-83
    sprite('ma311_14', 3)	# 84-86

@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()
        Unknown11063(1)
        WhiffCancelEnable(1)
        WhiffCancel('UltimateJump')
        WhiffCancel('UltimateJump_OD')
        WhiffCancel('UltimateAssault')
        WhiffCancel('UltimateAssault_OD')
        Unknown14070('Assault_A_EX')
        Unknown14070('Assault_B_EX')
        Unknown14070('Assault_C_EX')
        Unknown14070('CmnActInvincibleAttack')
        loopRelated(17, 4)

        def upon_17():
            Unknown14071('Assault_A_EX')
            Unknown14071('Assault_B_EX')
            Unknown14071('Assault_C_EX')
            Unknown14070('Assault_A')
            Unknown14070('Assault_B')
            Unknown14070('Assault_C')
            Unknown13008(0)
            Unknown13026(0)
            SLOT_61 = 0
            clearUponHandler(17)
        if SLOT_60:
            if (SLOT_60 == 20):
                enterState('UltimateJump')
            if (SLOT_60 == 21):
                enterState('UltimateJump_OD')
            if (SLOT_60 == 30):
                enterState('UltimateAssault')
            if (SLOT_60 == 31):
                enterState('UltimateAssault_OD')
        SLOT_4 = 8
        if SLOT_93:
            Unknown13008(1)
        if SLOT_61:
            Unknown13008(1)
        Unknown23145('Assault')
        SLOT_51 = SLOT_0

        def upon_STATE_END():
            SLOT_60 = 0
    if SLOT_51:
        _gotolabel(0)
    sprite('ma400_00', 3)	# 1-3
    if SLOT_6:
        if Unknown23145('NmlAtk5B'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-210000)
            Unknown35()
        if Unknown23145('NmlAtk5B2nd'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-210000)
            Unknown35()
    label(0)
    sprite('ma400_01', 3)	# 4-6
    SFX_0('000_airdash_0')
    sprite('ma400_02', 2)	# 7-8
    if (not SLOT_60):
        Unknown7007('626d613230305f30000000000000000064000000626d613230305f31000000000000000064000000626d613230305f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(45000)
    Unknown8007(100, 1, 1)
    WhiffCancel('Assault')
    WhiffCancel('Backflip')
    Unknown14072('Assault_A')
    Unknown14072('Assault_B')
    Unknown14072('Assault_C')
    Unknown14072('Assault_A_EX')
    Unknown14072('Assault_B_EX')
    Unknown14072('Assault_C_EX')
    Unknown14072('CmnActInvincibleAttack')

    def upon_3():
        if SLOT_60:
            if (SLOT_60 == 1):
                enterState('Assault_A')
            if (SLOT_60 == 2):
                enterState('Assault_B')
            if (SLOT_60 == 3):
                enterState('Assault_C')
            if (SLOT_60 == 11):
                enterState('Assault_A_EX')
            if (SLOT_60 == 12):
                enterState('Assault_B_EX')
            if (SLOT_60 == 13):
                enterState('Assault_C_EX')
    sprite('ma400_03', 2)	# 9-10
    Unknown1047(28000)
    Unknown1019(80)
    sprite('ma400_02', 2)	# 11-12
    sprite('ma400_03', 2)	# 13-14
    Unknown1019(80)
    sprite('ma400_02', 2)	# 15-16
    sprite('ma400_03', 2)	# 17-18
    Unknown1019(60)
    sprite('ma400_02', 2)	# 19-20
    Unknown1019(60)
    sprite('ma400_04', 2)	# 21-22
    Unknown1019(50)
    Unknown2006()
    clearUponHandler(3)
    sprite('ma400_04', 2)	# 23-24
    Unknown13014(1)
    Unknown13015(1)
    sprite('ma400_05', 2)	# 25-26
    Unknown1084(1)
    sprite('ma400_05', 2)	# 27-28

@Subroutine
def Assault_A_Init():
    AttackLevel_(3)
    AttackP1(80)
    Unknown9154(27)
    Unknown11028(21)
    AirUntechableTime(30)
    AirPushbackX(33000)
    AirPushbackY(20000)
    Unknown11001(0, 0, 0)
    AirHitstunAnimation(13)
    Unknown9016(1)

@Subroutine
def Assault_Ajizoku_Init():
    AttackLevel_(5)
    AirHitstunAnimation(10)
    AirPushbackX(-2000)
    AirPushbackY(22000)
    Hitstop(12)
    Unknown11001(0, 0, 8)

@State
def Assault_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_A_Init')
        Damage(2000)

        def upon_11():
            Unknown2037(1)
            sendToLabel(9)
    sprite('ma401_00', 1)	# 1-1
    sprite('ma401_01', 1)	# 2-2
    sprite('ma401_02', 1)	# 3-3
    sprite('ma401_03', 1)	# 4-4
    Unknown7007('626d613230315f30000000000000000064000000626d613230315f31000000000000000064000000626d613230315f320000000000000000000000000000000000000000000000000000000000000000')
    sprite('ma401_04', 2)	# 5-6	 **attackbox here**
    GFX_0('maef_401', 0)
    Unknown8006(100, 1, 1)
    SFX_3('mase_06')
    Unknown1084(1)
    physicsXImpulse(60000)
    sprite('ma401_05', 1)	# 7-7	 **attackbox here**
    sprite('ma401_05ex01', 1)	# 8-8	 **attackbox here**
    Unknown26('maef_401')
    if (not SLOT_2):
        clearUponHandler(3)
        callSubroutine('Assault_Ajizoku_Init')
        Damage(2400)
        Unknown11050('020000006d6165665f3430315f6869740000000000000000000000000000000000000000')
        GFX_0('maef_401_impact', 0)
        clearUponHandler(11)

        def upon_11():
            ScreenShake(0, 30000)
    label(9)
    sprite('ma401_06', 4)	# 9-12
    clearUponHandler(11)
    Recovery()
    Unknown1019(50)
    Unknown26('maef_401')
    sprite('ma401_07', 4)	# 13-16
    Unknown1019(50)
    Unknown1051(0)
    sprite('ma401_08', 3)	# 17-19
    Unknown1019(50)
    sprite('ma401_09', 3)	# 20-22
    sprite('ma401_10', 3)	# 23-25
    sprite('ma401_11', 4)	# 26-29
    Unknown1084(1)
    sprite('ma401_12', 4)	# 30-33

@State
def Assault_A_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_A_Init')
        Damage(2200)

        def upon_11():
            Unknown2037(1)
            sendToLabel(9)
    sprite('ma401_00', 1)	# 1-1
    sprite('ma401_01', 1)	# 2-2
    sprite('ma401_02', 1)	# 3-3
    sprite('ma401_03', 1)	# 4-4
    Unknown7007('626d613230315f30000000000000000064000000626d613230315f31000000000000000064000000626d613230315f320000000000000000000000000000000000000000000000000000000000000000')
    sprite('ma401_04', 2)	# 5-6	 **attackbox here**
    GFX_0('maef_401', 0)
    Unknown8006(100, 1, 1)
    SFX_3('mase_06')
    Unknown1084(1)
    physicsXImpulse(60000)
    sprite('ma401_05', 1)	# 7-7	 **attackbox here**
    sprite('ma401_05ex01', 1)	# 8-8	 **attackbox here**
    Unknown26('maef_401')
    if (not SLOT_2):
        clearUponHandler(3)
        callSubroutine('Assault_Ajizoku_Init')
        Damage(2600)
        Unknown11050('020000006d6165665f3430315f6869740000000000000000000000000000000000000000')
        GFX_0('maef_401_impact', 0)
        clearUponHandler(11)

        def upon_11():
            ScreenShake(0, 30000)
    label(9)
    sprite('ma401_06', 4)	# 9-12
    clearUponHandler(11)
    Recovery()
    Unknown1019(50)
    Unknown26('maef_401')
    sprite('ma401_07', 4)	# 13-16
    Unknown1019(50)
    Unknown1051(0)
    sprite('ma401_08', 3)	# 17-19
    Unknown1019(50)
    sprite('ma401_09', 3)	# 20-22
    sprite('ma401_10', 3)	# 23-25
    sprite('ma401_11', 4)	# 26-29
    Unknown1084(1)
    sprite('ma401_12', 4)	# 30-33

@Subroutine
def Assault_B_Init():
    AttackLevel_(4)
    AttackP1(80)
    AirUntechableTime(36)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(44000)
    AirPushbackY(20000)
    Unknown9016(1)

@Subroutine
def Assault_Bjizoku_Init():
    AttackLevel_(5)
    Hitstop(13)

@State
def Assault_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_B_Init')
        Damage(2200)

        def upon_11():
            Unknown2037(1)
    sprite('ma401_00', 3)	# 1-3
    Unknown1051(30)
    sprite('ma401_01', 2)	# 4-5
    Unknown7007('626d613230325f30000000000000000064000000626d613230325f31000000000000000064000000626d613230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma401_02', 2)	# 6-7
    sprite('ma401_03', 2)	# 8-9
    sprite('ma401_04', 2)	# 10-11	 **attackbox here**
    GFX_0('maef_401', 0)
    Unknown8006(100, 1, 1)
    SFX_3('mase_06')
    Unknown1084(1)
    physicsXImpulse(90000)
    sprite('ma401_05', 2)	# 12-13	 **attackbox here**
    sprite('ma401_04', 2)	# 14-15	 **attackbox here**
    sprite('ma401_05', 1)	# 16-16	 **attackbox here**
    sprite('ma401_05ex01', 1)	# 17-17	 **attackbox here**
    Unknown26('maef_401')
    if (not SLOT_2):
        clearUponHandler(3)
        callSubroutine('Assault_Bjizoku_Init')
        Damage(2600)
        Unknown11050('020000006d6165665f3430315f6869740000000000000000000000000000000000000000')
        GFX_0('maef_401_impact', 0)
        clearUponHandler(11)

        def upon_11():
            ScreenShake(0, 30000)
    sprite('ma401_06', 3)	# 18-20
    Recovery()
    Unknown1019(20)
    sprite('ma401_07', 3)	# 21-23
    Unknown1019(50)
    Unknown1051(0)
    sprite('ma401_08', 3)	# 24-26
    Unknown1019(50)
    sprite('ma401_09', 3)	# 27-29
    sprite('ma401_10', 3)	# 30-32
    sprite('ma401_11', 3)	# 33-35
    Unknown1084(1)
    sprite('ma401_12', 2)	# 36-37

@State
def Assault_B_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_B_Init')
        Damage(2600)

        def upon_11():
            Unknown2037(1)
    sprite('ma401_00', 3)	# 1-3
    Unknown1051(30)
    sprite('ma401_01', 2)	# 4-5
    Unknown7007('626d613230325f30000000000000000064000000626d613230325f31000000000000000064000000626d613230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma401_02', 2)	# 6-7
    sprite('ma401_03', 2)	# 8-9
    sprite('ma401_04', 2)	# 10-11	 **attackbox here**
    GFX_0('maef_401', 0)
    Unknown8006(100, 1, 1)
    SFX_3('mase_06')
    Unknown1084(1)
    physicsXImpulse(90000)
    sprite('ma401_05', 2)	# 12-13	 **attackbox here**
    sprite('ma401_04', 2)	# 14-15	 **attackbox here**
    sprite('ma401_05', 1)	# 16-16	 **attackbox here**
    sprite('ma401_05ex01', 1)	# 17-17	 **attackbox here**
    Unknown26('maef_401')
    if (not SLOT_2):
        clearUponHandler(3)
        callSubroutine('Assault_Bjizoku_Init')
        Damage(3000)
        Unknown11050('020000006d6165665f3430315f6869740000000000000000000000000000000000000000')
        GFX_0('maef_401_impact', 0)
        clearUponHandler(11)

        def upon_11():
            ScreenShake(0, 30000)
    sprite('ma401_06', 3)	# 18-20
    Recovery()
    Unknown1019(20)
    sprite('ma401_07', 3)	# 21-23
    Unknown1019(50)
    Unknown1051(0)
    sprite('ma401_08', 3)	# 24-26
    Unknown1019(50)
    sprite('ma401_09', 3)	# 27-29
    sprite('ma401_10', 3)	# 30-32
    sprite('ma401_11', 3)	# 33-35
    Unknown1084(1)
    sprite('ma401_12', 2)	# 36-37

@Subroutine
def Assault_C_Init():
    AttackLevel_(4)
    AttackP1(80)
    Unknown11092(1)
    AirUntechableTime(60)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(44000)
    AirPushbackY(20000)
    Hitstop(3)
    Unknown9016(1)
    Unknown11091(10)
    Unknown30065(0)

@Subroutine
def Assault_Cjizoku_Init():
    AttackLevel_(5)
    PushbackX(53000)

@State
def Assault_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_C_Init')
        Damage(2000)

        def upon_11():
            Unknown2037(1)

        def upon_3():
            if SLOT_2:
                clearUponHandler(3)
                Damage(380)
    sprite('ma401_00', 3)	# 1-3
    Unknown1051(30)
    sprite('ma401_01', 2)	# 4-5
    sprite('ma401_02', 2)	# 6-7
    sprite('ma401_03', 2)	# 8-9
    Unknown7007('626d613230315f30000000000000000064000000626d613230315f31000000000000000064000000626d613230315f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ma401_04', 2)	# 10-11	 **attackbox here**
    GFX_0('maef_401', 0)
    Unknown8006(100, 1, 1)
    SFX_3('mase_06')
    Unknown1084(1)
    physicsXImpulse(90000)
    sprite('ma401_05', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    sprite('ma401_04', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('ma401_05', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    Hitstop(13)
    sprite('ma401_05ex01', 1)	# 17-17	 **attackbox here**
    Unknown26('maef_401')
    if (not SLOT_2):
        clearUponHandler(3)
        callSubroutine('Assault_Cjizoku_Init')
        Damage(2600)
        Unknown11050('020000006d6165665f3430315f6869740000000000000000000000000000000000000000')
        GFX_0('maef_401_impact', 0)
        clearUponHandler(11)

        def upon_11():
            ScreenShake(0, 30000)
    label(9)
    sprite('ma401_06', 3)	# 18-20
    clearUponHandler(11)
    Recovery()
    Unknown1019(50)
    Unknown26('maef_401')
    sprite('ma401_07', 2)	# 21-22
    Unknown1019(50)
    Unknown1051(0)
    sprite('ma401_08', 2)	# 23-24
    Unknown1019(50)
    sprite('ma401_09', 2)	# 25-26
    sprite('ma401_10', 2)	# 27-28
    sprite('ma401_11', 2)	# 29-30
    Unknown1084(1)
    sprite('ma401_12', 2)	# 31-32

@State
def Assault_C_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_C_Init')
        Damage(2600)

        def upon_11():
            Unknown2037(1)

        def upon_3():
            if SLOT_2:
                clearUponHandler(3)
                Damage(300)
    sprite('ma401_00', 3)	# 1-3
    Unknown1051(30)
    sprite('ma401_01', 2)	# 4-5
    sprite('ma401_02', 2)	# 6-7
    sprite('ma401_03', 2)	# 8-9
    Unknown7007('626d613230315f30000000000000000064000000626d613230315f31000000000000000064000000626d613230315f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ma401_04', 2)	# 10-11	 **attackbox here**
    GFX_0('maef_401', 0)
    Unknown8006(100, 1, 1)
    SFX_3('mase_06')
    Unknown1084(1)
    physicsXImpulse(90000)
    sprite('ma401_05', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    sprite('ma401_04', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('ma401_05', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    Hitstop(13)
    sprite('ma401_05ex01', 1)	# 17-17	 **attackbox here**
    Unknown26('maef_401')
    if (not SLOT_2):
        clearUponHandler(3)
        callSubroutine('Assault_Cjizoku_Init')
        Damage(3000)
        Unknown11050('020000006d6165665f3430315f6869740000000000000000000000000000000000000000')
        GFX_0('maef_401_impact', 0)
        clearUponHandler(11)

        def upon_11():
            ScreenShake(0, 30000)
    label(9)
    sprite('ma401_06', 3)	# 18-20
    clearUponHandler(11)
    Recovery()
    Unknown1019(50)
    Unknown26('maef_401')
    sprite('ma401_07', 2)	# 21-22
    Unknown1019(50)
    Unknown1051(0)
    sprite('ma401_08', 2)	# 23-24
    Unknown1019(50)
    sprite('ma401_09', 2)	# 25-26
    sprite('ma401_10', 2)	# 27-28
    sprite('ma401_11', 2)	# 29-30
    Unknown1084(1)
    sprite('ma401_12', 2)	# 31-32

@State
def Backflip():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        WhiffCancelEnable(1)
        WhiffCancel('UltimateJump')
        WhiffCancel('UltimateJump_OD')
        WhiffCancel('UltimateAssault')
        WhiffCancel('UltimateAssault_OD')
        Unknown14070('Backflip_A')
        Unknown14070('Backflip_B')
        Unknown14070('Backflip_C')
        Unknown14070('CmnActInvincibleAttackAir')
        loopRelated(17, 4)

        def upon_17():
            Unknown13008(0)
            SLOT_61 = 0
            SLOT_5 = (SLOT_5 + (-1))
            clearUponHandler(17)
        if SLOT_60:
            if (SLOT_60 == 20):
                enterState('UltimateJump')
            if (SLOT_60 == 21):
                enterState('UltimateJump_OD')
            if (SLOT_60 == 30):
                enterState('UltimateAssault')
            if (SLOT_60 == 31):
                enterState('UltimateAssault_OD')
        if SLOT_61:
            Unknown13008(1)
        Unknown23145('Assault')
        SLOT_51 = SLOT_0

        def upon_STATE_END():
            if (SLOT_4 >= 4):
                SLOT_4 = 4
    if SLOT_36:
        _gotolabel(100)
    sprite('ma402_00', 3)	# 1-3
    Unknown23183('6d613430325f3038000000000000000000000000000000000000000000000000030000000200000033000000')
    Unknown1051(150)
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000001000000')
    SLOT_4 = 8
    if SLOT_93:
        Unknown13008(1)
    if SLOT_6:
        if Unknown23145('NmlAtk5B'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-240000)
            Unknown35()
        if Unknown23145('NmlAtk5B2nd'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-240000)
            Unknown35()
    sprite('ma402_01', 2)	# 4-5
    sprite('ma402_02', 5)	# 6-10
    Unknown22019('0100000001000000010000000100000001000000')
    Unknown8001(0, 0)
    Unknown3029(1)
    physicsXImpulse(-8000)
    physicsYImpulse(35000)
    Unknown1043()
    Unknown22004(4, 1)
    loopRest()
    gotoLabel(9)
    label(100)
    sprite('ma402_10', 3)	# 11-13
    SLOT_4 = 16
    Unknown1019(-20)
    Unknown1015(-4000)
    physicsYImpulse(60000)
    setGravity(2400)
    if SLOT_93:
        Unknown13008(1)
    if SLOT_6:
        if Unknown23145('NmlAtkAIR5B'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-240000)
            Unknown35()
        if Unknown23145('NmlAtkAIR5B2nd'):
            GFX_0('maef_catch', 0)
            Unknown36(1)
            Unknown1072(-240000)
            Unknown35()
    sprite('ma402_09', 2)	# 14-15
    sprite('ma402_02', 2)	# 16-17
    YAccel(60)
    setInvincible(1)
    Unknown8002()
    SFX_0('000_airdash_0')
    Unknown3029(1)
    Unknown22004(4, 1)
    loopRest()
    label(9)
    sprite('ma402_03', 5)	# 18-22
    if (not SLOT_60):
        Unknown7007('626d613230345f30000000000000000064000000626d613230345f31000000000000000064000000626d613230345f320000000000000000640000000000000000000000000000000000000000000000')
    WhiffCancel('Backflip')
    Unknown14072('Backflip_A')
    Unknown14072('Backflip_B')
    Unknown14072('Backflip_C')
    Unknown14072('Backflip_A_EX')
    Unknown14072('Backflip_B_EX')
    Unknown14072('Backflip_C_EX')
    Unknown14072('CmnActInvincibleAttackAir')

    def upon_3():
        if CheckInput(0x79):
            if SLOT_2:
                Unknown13014(1)
        else:
            Unknown13014(0)
            if SLOT_60:
                if (SLOT_60 == 1):
                    enterState('Backflip_A')
                if (SLOT_60 == 2):
                    enterState('Backflip_B')
                if (SLOT_60 == 3):
                    enterState('Backflip_C')
    sprite('ma402_04', 5)	# 23-27
    setInvincible(0)
    Unknown2037(1)
    Unknown14074('Backflip_A')
    Unknown14074('Backflip_B')
    Unknown14074('Backflip_C')
    WhiffCancel('Backflip_A_EX')
    WhiffCancel('Backflip_B_EX')
    WhiffCancel('Backflip_C_EX')
    sprite('ma402_06', 5)	# 28-32
    Unknown1043()
    sprite('ma402_07', 5)	# 33-37
    sprite('ma020_04', 3)	# 38-40
    Recovery()
    clearUponHandler(3)
    Unknown13014(1)
    Unknown13019(1)
    sprite('ma020_05', 3)	# 41-43
    sprite('ma020_06', 3)	# 44-46
    label(0)
    sprite('ma020_07', 4)	# 47-50
    sprite('ma020_08', 4)	# 51-54
    loopRest()
    gotoLabel(0)

@Subroutine
def Backflip_Init():
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    Unknown1019(-10)
    Unknown1051(10)
    physicsYImpulse(15000)
    setGravity(750)
    AttackLevel_(4)
    AttackP1(80)
    Damage(2000)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirUntechableTime(40)
    Unknown9310(1)
    Unknown9016(1)

@State
def Backflip_A():

    def upon_IMMEDIATE():
        Unknown17003()
        AirPushbackX(1000)
        AirPushbackY(-72000)

        def upon_12():
            setGravity(1000)
        callSubroutine('Backflip_Init')
    sprite('ma403_00', 2)	# 1-2
    sprite('ma403_01', 1)	# 3-3
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_01', 1)	# 4-4
    Unknown7007('626d613230355f30000000000000000064000000626d613230355f31000000000000000064000000626d613230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma403_02', 2)	# 5-6
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_03', 2)	# 7-8
    sprite('ma403_04', 2)	# 9-10
    sprite('ma403_05ex', 3)	# 11-13	 **attackbox here**
    GFX_0('maef_403', 0)
    SFX_3('mase_05')
    Unknown1084(1)
    physicsYImpulse(-66000)
    Unknown1043()
    sprite('ma403_06', 3)	# 14-16	 **attackbox here**
    label(0)
    sprite('ma403_05', 3)	# 17-19	 **attackbox here**
    sprite('ma403_06', 3)	# 20-22	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_07', 2)	# 23-24	 **attackbox here**
    Unknown26('maef_403')
    Unknown26('maef_401_ring')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown23027()
    Recovery()
    sprite('ma403_07', 4)	# 25-28	 **attackbox here**
    sprite('ma403_08', 6)	# 29-34
    sprite('ma403_09', 3)	# 35-37
    sprite('ma403_10', 3)	# 38-40

@State
def Backflip_A_EX():

    def upon_IMMEDIATE():
        Unknown17003()
        AirPushbackX(1000)
        AirPushbackY(-72000)

        def upon_12():
            setGravity(1000)
        callSubroutine('Backflip_Init')
    sprite('ma403_00', 4)	# 1-4
    sprite('ma403_01', 4)	# 5-8
    Unknown7007('626d613230355f30000000000000000064000000626d613230355f31000000000000000064000000626d613230355f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_02', 4)	# 9-12
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_03', 4)	# 13-16
    sprite('ma403_04', 4)	# 17-20
    sprite('ma403_05ex', 3)	# 21-23	 **attackbox here**
    GFX_0('maef_403', 0)
    SFX_3('mase_05')
    Unknown1084(1)
    physicsYImpulse(-66000)
    Unknown1043()
    sprite('ma403_06', 3)	# 24-26	 **attackbox here**
    label(0)
    sprite('ma403_05', 3)	# 27-29	 **attackbox here**
    sprite('ma403_06', 3)	# 30-32	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_07', 2)	# 33-34	 **attackbox here**
    Unknown26('maef_403')
    Unknown26('maef_401_ring')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    GFX_0('maef_403_landing', 0)
    ScreenShake(0, 15000)
    Unknown8004(100, 0, 1)
    RefreshMultihit()
    AttackP2(85)
    Unknown11001(4, 4, 9)
    AirPushbackX(-3000)
    AirPushbackY(25000)
    Unknown9310(-1)
    Unknown9015(1)
    sprite('ma403_07', 4)	# 35-38	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('ma403_08', 8)	# 39-46
    sprite('ma403_09', 3)	# 47-49
    sprite('ma403_10', 3)	# 50-52

@State
def Backflip_B():

    def upon_IMMEDIATE():
        Unknown17003()
        AirPushbackX(24000)
        AirPushbackY(-58000)
        YImpluseBeforeWallbounce(1000)
        Unknown9202(5)

        def upon_12():
            Unknown1028(450)
            setGravity(900)
        callSubroutine('Backflip_Init')
    sprite('ma403_11', 2)	# 1-2
    sprite('ma403_12', 1)	# 3-3
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_12', 1)	# 4-4
    Unknown7007('626d613230365f30000000000000000064000000626d613230365f31000000000000000064000000626d613230365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma403_13', 2)	# 5-6
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_14', 2)	# 7-8
    sprite('ma403_15', 2)	# 9-10
    sprite('ma403_16', 3)	# 11-13	 **attackbox here**
    GFX_0('maef_403B', 0)
    SFX_3('mase_05')
    Unknown1084(1)
    physicsXImpulse(30000)
    physicsYImpulse(-60000)
    sprite('ma403_17', 3)	# 14-16	 **attackbox here**
    label(0)
    sprite('ma403_16', 3)	# 17-19	 **attackbox here**
    sprite('ma403_17', 3)	# 20-22	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 2)	# 23-24	 **attackbox here**
    Unknown26('maef_403B')
    Unknown26('maef_401_ring')
    Unknown1019(20)
    physicsYImpulse(0)
    Unknown8000(100, 1, 1)
    Unknown23027()
    Recovery()
    sprite('ma403_18', 4)	# 25-28	 **attackbox here**
    sprite('ma403_19', 8)	# 29-36
    Unknown1019(50)
    sprite('ma403_09', 3)	# 37-39
    Unknown1084(1)
    sprite('ma403_10', 3)	# 40-42

@State
def Backflip_B_EX():

    def upon_IMMEDIATE():
        Unknown17003()
        AirPushbackX(24000)
        AirPushbackY(-58000)
        YImpluseBeforeWallbounce(1000)
        Unknown9202(5)

        def upon_12():
            Unknown1028(450)
            setGravity(900)
        callSubroutine('Backflip_Init')
    sprite('ma403_11', 4)	# 1-4
    sprite('ma403_12', 4)	# 5-8
    Unknown7007('626d613230365f30000000000000000064000000626d613230365f31000000000000000064000000626d613230365f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_13', 4)	# 9-12
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_14', 4)	# 13-16
    sprite('ma403_15', 4)	# 17-20
    sprite('ma403_16', 3)	# 21-23	 **attackbox here**
    GFX_0('maef_403B', 0)
    SFX_3('mase_05')
    Unknown1084(1)
    physicsXImpulse(30000)
    physicsYImpulse(-60000)
    sprite('ma403_17', 3)	# 24-26	 **attackbox here**
    label(0)
    sprite('ma403_16', 3)	# 27-29	 **attackbox here**
    sprite('ma403_17', 3)	# 30-32	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 2)	# 33-34	 **attackbox here**
    Unknown26('maef_403B')
    Unknown26('maef_401_ring')
    Unknown1019(20)
    physicsYImpulse(0)
    Unknown8000(100, 1, 1)
    GFX_0('maef_403_landing', 0)
    ScreenShake(0, 15000)
    Unknown8004(100, 0, 1)
    RefreshMultihit()
    AttackP2(85)
    AirPushbackX(8000)
    AirPushbackY(30000)
    Unknown9095()
    Unknown11001(4, 4, 9)
    Unknown9310(-1)
    Unknown9203()
    Unknown9015(1)
    sprite('ma403_18', 4)	# 35-38	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('ma403_19', 8)	# 39-46
    Unknown1019(50)
    sprite('ma403_09', 3)	# 47-49
    Unknown1084(1)
    sprite('ma403_10', 3)	# 50-52

@State
def Backflip_C():

    def upon_IMMEDIATE():
        Unknown17003()
        Damage(2000)
        AirPushbackX(1000)
        AirPushbackY(-72000)
        Unknown11091(10)
        Unknown30065(0)

        def upon_12():
            setGravity(1000)
        callSubroutine('Backflip_Init')
    sprite('ma403_00', 2)	# 1-2
    sprite('ma403_01', 1)	# 3-3
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_01', 1)	# 4-4
    Unknown7007('626d613230355f30000000000000000064000000626d613230355f31000000000000000064000000626d613230355f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ma403_02', 2)	# 5-6
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_03', 2)	# 7-8
    sprite('ma403_04', 2)	# 9-10
    sprite('ma403_05ex', 3)	# 11-13	 **attackbox here**
    GFX_0('maef_403', 0)
    SFX_3('mase_05')
    Unknown1084(1)
    physicsYImpulse(-66000)
    Unknown1043()
    sprite('ma403_06', 3)	# 14-16	 **attackbox here**
    label(0)
    sprite('ma403_05', 3)	# 17-19	 **attackbox here**
    sprite('ma403_06', 3)	# 20-22	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_07', 2)	# 23-24	 **attackbox here**
    Unknown26('maef_403')
    Unknown26('maef_401_ring')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    GFX_0('maef_403_landing', 0)
    ScreenShake(0, 15000)
    Unknown8004(100, 0, 1)
    RefreshMultihit()
    Unknown11001(6, 0, 5)
    AirPushbackX(-3000)
    AirPushbackY(25000)
    Unknown9310(-1)
    Unknown9015(1)
    Unknown11028(22)
    Hitstop(16)
    sprite('ma403_07', 4)	# 25-28	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('ma403_08', 6)	# 29-34
    sprite('ma403_09', 3)	# 35-37
    sprite('ma403_10', 3)	# 38-40

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(60)
        Hitstop(8)
        AirPushbackX(17000)
        AirPushbackY(32000)
        YImpluseBeforeWallbounce(1800)
        Unknown11001(0, 4, 4)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown11056(0)
        Unknown9016(1)
        sendToLabelUpon(2, 9)

        def upon_78():
            SLOT_51 = 1
    sprite('ma401_00', 3)	# 1-3
    sprite('ma401_00', 1)	# 4-4
    Unknown7007('626d613230335f30000000000000000064000000626d613230335f31000000000000000064000000626d613230335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma401_01', 2)	# 5-6
    sprite('ma401_02', 2)	# 7-8
    sprite('ma401_03', 2)	# 9-10
    sprite('ma401_13ex_01', 2)	# 11-12
    Unknown14070('AntiAir2nd')
    GFX_0('maef_401C', 0)
    SFX_3('mase_06')
    Unknown1084(1)
    Unknown1045(10000)
    physicsXImpulse(60000)
    physicsYImpulse(35000)
    Unknown1028(-3000)
    setGravity(1800)
    sprite('ma401_14ex', 2)	# 13-14	 **attackbox here**
    sprite('ma401_13ex', 2)	# 15-16	 **attackbox here**
    sprite('ma401_14ex', 1)	# 17-17	 **attackbox here**
    sprite('ma401_14ex01', 1)	# 18-18	 **attackbox here**
    Unknown26('maef_401C')
    sprite('ma401_15', 3)	# 19-21
    if SLOT_51:
        Unknown14072('AntiAir2nd')
    setInvincible(0)
    Unknown1034(0)
    Unknown1019(50)
    YAccel(50)
    sprite('ma401_16', 3)	# 22-24
    Unknown14074('AntiAir2nd')
    Unknown1019(50)
    YAccel(50)
    sprite('ma321_11', 3)	# 25-27
    sprite('ma321_12', 3)	# 28-30
    sprite('ma321_13', 3)	# 31-33
    sprite('ma321_14', 3)	# 34-36
    sprite('ma020_04', 3)	# 37-39
    sprite('ma020_05', 3)	# 40-42
    sprite('ma020_06', 3)	# 43-45
    label(0)
    sprite('ma020_07', 4)	# 46-49
    sprite('ma020_08', 4)	# 50-53
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma024_00', 2)	# 54-55
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ma024_00', 2)	# 56-57
    sprite('ma024_01', 3)	# 58-60
    sprite('ma024_02', 8)	# 61-68
    sprite('ma024_03', 3)	# 69-71
    sprite('ma024_04', 3)	# 72-74

@State
def AntiAir2nd():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        AttackLevel_(4)
        Damage(1000)
        AttackP1(48)
        AttackP2(100)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Hitstop(10)
        Unknown11001(0, 0, 0)
        AirUntechableTime(40)
        Unknown9310(1)
        AirPushbackX(40000)
        AirPushbackY(-66000)
        YImpluseBeforeWallbounce(1000)
        Unknown9202(5)
        Unknown9016(1)

        def upon_12():
            Unknown1028(800)
            setGravity(800)
        Unknown1019(-10)
        Unknown1051(10)
        physicsYImpulse(15000)
        setGravity(750)
        YAccel(200)
        setInvincible(0)
        Unknown30068(1)
        Unknown14083(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ma402_10', 3)	# 1-3
    Unknown1019(-20)
    Unknown1015(-4000)
    physicsYImpulse(60000)
    setGravity(2400)
    sprite('ma402_09', 2)	# 4-5
    sprite('ma402_02', 2)	# 6-7
    YAccel(60)
    Unknown8002()
    SFX_0('000_airdash_0')
    Unknown3029(1)
    sprite('ma403_11', 2)	# 8-9
    sprite('ma403_12ex', 1)	# 10-10
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_12ex', 1)	# 11-11
    Unknown7007('626d613230375f30000000000000000064000000626d613230375f31000000000000000064000000626d613230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma403_13ex', 2)	# 12-13
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_14ex', 2)	# 14-15
    sprite('ma403_15ex', 2)	# 16-17
    sprite('ma403_20', 3)	# 18-20	 **attackbox here**
    GFX_0('maef_403C', 0)
    SFX_3('mase_05')
    Unknown1084(1)
    physicsXImpulse(50000)
    physicsYImpulse(-50000)
    sprite('ma403_21', 3)	# 21-23	 **attackbox here**
    label(0)
    sprite('ma403_20', 3)	# 24-26	 **attackbox here**
    sprite('ma403_21', 3)	# 27-29	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 6)	# 30-35	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown26('maef_403C')
    Unknown26('maef_401_ring')
    Unknown1019(20)
    physicsYImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ma403_18', 7)	# 36-42	 **attackbox here**
    Unknown1019(20)
    sprite('ma403_19', 10)	# 43-52
    Unknown1084(1)
    sprite('ma403_09', 4)	# 53-56
    sprite('ma403_10', 4)	# 57-60

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(2300)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirUntechableTime(40)
        Unknown9310(1)
        AirPushbackX(40000)
        AirPushbackY(-66000)
        YImpluseBeforeWallbounce(1000)
        Unknown9202(5)
        Unknown9016(1)

        def upon_12():
            Unknown1028(800)
            setGravity(800)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ma402_10', 3)	# 1-3
    Unknown1019(-20)
    Unknown1015(-4000)
    physicsYImpulse(60000)
    setGravity(2400)
    sprite('ma402_09', 2)	# 4-5
    sprite('ma402_02', 2)	# 6-7
    YAccel(60)
    Unknown8002()
    SFX_0('000_airdash_0')
    Unknown3029(1)
    sprite('ma403_11', 2)	# 8-9
    sprite('ma403_12ex', 1)	# 10-10
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_12ex', 1)	# 11-11
    Unknown7007('626d613230375f30000000000000000064000000626d613230375f31000000000000000064000000626d613230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ma403_13ex', 2)	# 12-13
    Unknown1019(50)
    YAccel(50)
    sprite('ma403_14ex', 2)	# 14-15
    sprite('ma403_15ex', 2)	# 16-17
    sprite('ma403_20', 3)	# 18-20	 **attackbox here**
    GFX_0('maef_403C', 0)
    SFX_3('mase_05')
    Unknown1084(1)
    physicsXImpulse(50000)
    physicsYImpulse(-50000)
    sprite('ma403_21', 3)	# 21-23	 **attackbox here**
    label(0)
    sprite('ma403_20', 3)	# 24-26	 **attackbox here**
    setInvincible(0)
    sprite('ma403_21', 3)	# 27-29	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma403_18', 6)	# 30-35	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Unknown26('maef_403C')
    Unknown26('maef_401_ring')
    Unknown1019(20)
    physicsYImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ma403_18', 7)	# 36-42	 **attackbox here**
    Unknown1019(20)
    sprite('ma403_19', 10)	# 43-52
    Unknown1084(1)
    sprite('ma403_09', 4)	# 53-56
    sprite('ma403_10', 4)	# 57-60

@State
def UltimateJump():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1800)
        Unknown11092(1)
        Unknown11091(16)
        PushbackX(8000)
        Unknown11001(0, -5, -5)
        AirUntechableTime(100)
        Unknown9310(1)
        AirPushbackX(-1000)
        AirPushbackY(60000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11084(1)
        Unknown11069('UltimateJump')
        Unknown13024(0)
        Unknown11064(1)

        def upon_STATE_END():
            Unknown26('dmyCamera')
            Unknown20007(0)
            Unknown1043()

        def upon_78():
            clearUponHandler(78)
            SLOT_51 = 1
            Unknown23022(1)
            Unknown20007(1)
        sendToLabelUpon(2, 99)
        Unknown48('19000000020000003a0000001600000002000000aa000000')

        def upon_3():
            Unknown36(22)
            Unknown23148('CmnActChangePartnerIn')
            Unknown48('160000000200000039000000190000000200000000000000')
            Unknown35()
    sprite('ma431_00', 3)	# 1-3
    setInvincible(1)
    sprite('ma431_01', 3)	# 4-6
    Unknown2036(25, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'bma252_0', 'bma252_1', '', '')
    sprite('ma431_02', 3)	# 7-9
    Unknown1084(1)
    sprite('ma431_03', 15)	# 10-24
    GFX_0('maef431', -1)
    sprite('ma431_04', 3)	# 25-27
    GFX_0('maef431_jump', -1)
    sprite('ma431_05', 3)	# 28-30
    sprite('ma431_06', 1)	# 31-31	 **attackbox here**
    Unknown8001(1, 0)
    sprite('ma431_06', 3)	# 32-34	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(100)
    AirPushbackY(10000)
    YImpluseBeforeWallbounce(200)
    Unknown11001(0, 0, 8)
    Hitstop(6)
    physicsXImpulse(0)
    physicsYImpulse(120000)
    setGravity(-10000)

    def upon_3():
        if (SLOT_23 >= 2600000):
            clearUponHandler(3)
            Unknown1084(1)
            teleportRelativeY(2600000)
            sendToLabel(11)
    sprite('ma431_07', 4)	# 35-38	 **attackbox here**
    setInvincible(0)
    if (not SLOT_58):
        if SLOT_57:
            GFX_0('dmyCamera', 100)
            Unknown38(4, 1)
        else:
            Unknown20007(1)
    else:
        GFX_0('dmyCamera', 100)
        Unknown38(4, 1)
    Unknown2015(10)
    label(5)
    sprite('ma431_06', 3)	# 39-41	 **attackbox here**
    sprite('ma431_07', 3)	# 42-44	 **attackbox here**
    loopRest()
    gotoLabel(5)
    label(11)
    sprite('null', 1)	# 45-45
    Unknown21015('646d7943616d6572610000000000000000000000000000000000000000000000b80b000000000000')
    sprite('null', 10)	# 46-55
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000140000000200000033000000')
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    Unknown26('maef431_jump')
    Unknown2015(-1)
    if (not SLOT_58):
        if SLOT_51:
            Unknown1086(22)
            Unknown1007(800000)
        if SLOT_57:
            Unknown48('190000000200000053000000040000000200000053000000')
        else:
            Unknown48('190000000200000053000000160000000200000053000000')
    else:
        if SLOT_51:
            Unknown1086(4)
            Unknown1007(800000)
        Unknown48('190000000200000053000000040000000200000053000000')
    teleportRelativeX(-5000)
    sprite('ma431_08', 1)	# 56-56	 **attackbox here**
    tag_voice(0, 'bma253_0', 'bma253_1', '', '')
    if (SLOT_25 <= 200000):
        SLOT_22 = 1750000
    RefreshMultihit()
    if SLOT_51:
        Damage(8700)
        Hitstop(0)
    else:
        Damage(5000)
    PushbackX(30400)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(1500)
    AirPushbackY(-160000)
    YImpluseBeforeWallbounce(2000)
    Unknown9310(50)
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown11064(0)
    Unknown11069('')
    Unknown2006()
    physicsYImpulse(-150000)
    setGravity(20000)

    def upon_12():
        SFX_0('025_cleanhit_slash')
        physicsYImpulse(-80000)
        setGravity(10000)
    sprite('ma431_08', 4)	# 57-60	 **attackbox here**
    GFX_0('maef431_fall', -1)
    SFX_3('mase_08')
    SFX_3('mase_08')
    label(0)
    sprite('ma431_09', 4)	# 61-64	 **attackbox here**
    sprite('ma431_08', 4)	# 65-68	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma431_10', 15)	# 69-83
    Unknown26('maef431_fall')
    GFX_0('maef431_crash', -1)
    Unknown13024(1)
    Unknown1084(1)
    setInvincible(0)
    Unknown8000(100, 1, 1)
    sprite('ma431_11', 5)	# 84-88
    Unknown20007(0)
    Unknown26('dmyCamera')
    sprite('ma431_12', 3)	# 89-91
    Unknown2006()
    sprite('ma431_13', 3)	# 92-94
    sprite('ma402_02', 4)	# 95-98
    physicsXImpulse(-8000)
    physicsYImpulse(28000)
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 99)
    sprite('ma402_03', 3)	# 99-101
    sprite('ma402_04', 3)	# 102-104
    sprite('ma402_05', 3)	# 105-107
    sprite('ma402_06', 3)	# 108-110
    sprite('ma402_07', 3)	# 111-113
    sprite('ma020_04', 3)	# 114-116
    sprite('ma020_05', 3)	# 117-119
    sprite('ma020_06', 3)	# 120-122
    label(1)
    sprite('ma020_07', 4)	# 123-126
    sprite('ma020_08', 4)	# 127-130
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('ma024_00', 2)	# 131-132
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ma024_01', 5)	# 133-137
    sprite('ma024_02', 5)	# 138-142
    sprite('ma024_03', 9)	# 143-151
    sprite('ma024_04', 5)	# 152-156

@State
def UltimateJump_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1000)
        Unknown11092(1)
        Unknown11091(13)
        PushbackX(8000)
        Unknown11001(0, -5, -5)
        AirUntechableTime(100)
        Unknown9310(1)
        AirPushbackX(-1000)
        AirPushbackY(60000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11084(1)
        Unknown11069('UltimateJump_OD')
        Unknown13024(0)
        Unknown11064(1)

        def upon_STATE_END():
            Unknown20007(0)
            Unknown1043()

        def upon_78():
            clearUponHandler(78)
            SLOT_51 = 1
            Unknown23022(1)
            Unknown20007(1)
            sendToLabel(10)
        sendToLabelUpon(2, 99)
        Unknown48('19000000020000003a0000001600000002000000aa000000')

        def upon_3():
            Unknown36(22)
            Unknown23148('CmnActChangePartnerIn')
            Unknown48('160000000200000039000000190000000200000000000000')
            Unknown35()
    sprite('ma431_00', 3)	# 1-3
    setInvincible(1)
    sprite('ma431_01', 3)	# 4-6
    Unknown2036(25, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'bma252_0', 'bma252_1', '', '')
    sprite('ma431_02', 3)	# 7-9
    Unknown1084(1)
    sprite('ma431_03', 15)	# 10-24
    GFX_0('maef431', -1)
    sprite('ma431_04', 3)	# 25-27
    GFX_0('maef431_jump_od', -1)
    sprite('ma431_05', 3)	# 28-30
    sprite('ma431_06', 1)	# 31-31	 **attackbox here**
    Unknown8001(1, 0)
    sprite('ma431_06', 3)	# 32-34	 **attackbox here**
    clearUponHandler(78)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(100)
    AirPushbackY(10000)
    YImpluseBeforeWallbounce(200)
    Unknown11001(0, 0, 8)
    Hitstop(6)
    physicsXImpulse(0)
    physicsYImpulse(120000)
    setGravity(-10000)

    def upon_3():
        if SLOT_51:
            Damage(170)
        if (SLOT_23 >= 2600000):
            clearUponHandler(3)
            Unknown1084(1)
            teleportRelativeY(2600000)
            sendToLabel(11)
    sprite('ma431_07', 4)	# 35-38	 **attackbox here**
    setInvincible(0)
    if (not SLOT_58):
        if SLOT_57:
            GFX_0('dmyCamera', 100)
            Unknown38(4, 1)
        else:
            Unknown20007(1)
    else:
        GFX_0('dmyCamera', 100)
        Unknown38(4, 1)
    Unknown2015(10)
    label(5)
    sprite('ma431_06', 3)	# 39-41	 **attackbox here**
    sprite('ma431_07', 3)	# 42-44	 **attackbox here**
    loopRest()
    gotoLabel(5)
    label(10)
    sprite('ma431_07', 2)	# 45-46	 **attackbox here**
    RefreshMultihit()
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Hitstop(3)
    Unknown11001(0, -2, -2)
    Unknown11056(1)
    AirPushbackY(40000)
    YImpluseBeforeWallbounce(200)
    physicsXImpulse(0)
    physicsYImpulse(80000)
    setGravity(0)
    Unknown2015(10)
    sprite('ma431_06', 2)	# 47-48	 **attackbox here**
    RefreshMultihit()
    sprite('ma431_07', 2)	# 49-50	 **attackbox here**
    RefreshMultihit()
    sprite('ma431_06', 2)	# 51-52	 **attackbox here**
    RefreshMultihit()
    sprite('ma431_07', 2)	# 53-54	 **attackbox here**
    RefreshMultihit()
    sprite('ma431_06', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    sprite('ma431_07', 3)	# 57-59	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(100)
    AirPushbackY(15000)
    YImpluseBeforeWallbounce(200)
    Unknown11001(0, 0, 8)
    Hitstop(6)
    sprite('ma431_06', 3)	# 60-62	 **attackbox here**

    def upon_3():
        if (SLOT_23 >= 2600000):
            clearUponHandler(3)
            Unknown1084(1)
            teleportRelativeY(2600000)
            sendToLabel(11)
    loopRest()
    gotoLabel(5)
    label(11)
    sprite('null', 1)	# 63-63
    Unknown21015('646d7943616d6572610000000000000000000000000000000000000000000000b80b000000000000')
    sprite('null', 10)	# 64-73
    clearUponHandler(3)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000140000000200000033000000')
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    Unknown26('maef431_jump_od')
    Unknown2015(-1)
    if (not SLOT_58):
        if SLOT_51:
            Unknown1086(22)
            Unknown1007(800000)
        if SLOT_57:
            Unknown48('190000000200000053000000040000000200000053000000')
        else:
            Unknown48('190000000200000053000000160000000200000053000000')
    else:
        if SLOT_51:
            Unknown1086(4)
            Unknown1007(800000)
        Unknown48('190000000200000053000000040000000200000053000000')
    teleportRelativeX(-5000)
    sprite('ma431_08', 1)	# 74-74	 **attackbox here**
    tag_voice(0, 'bma253_0', 'bma253_1', '', '')
    if (SLOT_25 <= 200000):
        SLOT_22 = 1750000
    RefreshMultihit()
    if SLOT_51:
        Damage(8200)
        Hitstop(0)
    else:
        Damage(6000)
    PushbackX(30400)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(1500)
    AirPushbackY(-160000)
    YImpluseBeforeWallbounce(2000)
    Unknown9310(50)
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown11064(0)
    Unknown11069('')
    Unknown2006()
    physicsYImpulse(-150000)
    setGravity(20000)

    def upon_12():
        SFX_0('025_cleanhit_slash')
        physicsYImpulse(-80000)
        setGravity(10000)
    sprite('ma431_08', 4)	# 75-78	 **attackbox here**
    GFX_0('maef431_fall_od', -1)
    SFX_3('mase_08')
    SFX_3('mase_08')
    label(0)
    sprite('ma431_09', 4)	# 79-82	 **attackbox here**
    sprite('ma431_08', 4)	# 83-86	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ma431_10', 15)	# 87-101
    Unknown26('maef431_fall_od')
    GFX_0('maef431_crash_od', -1)
    Unknown13024(1)
    Unknown1084(1)
    setInvincible(0)
    Unknown8000(100, 1, 1)
    sprite('ma431_11', 5)	# 102-106
    Unknown20007(0)
    Unknown26('dmyCamera')
    sprite('ma431_12', 3)	# 107-109
    Unknown2006()
    sprite('ma431_13', 3)	# 110-112
    sprite('ma402_02', 4)	# 113-116
    physicsXImpulse(-8000)
    physicsYImpulse(28000)
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 99)
    sprite('ma402_03', 3)	# 117-119
    sprite('ma402_04', 3)	# 120-122
    sprite('ma402_05', 3)	# 123-125
    sprite('ma402_06', 3)	# 126-128
    sprite('ma402_07', 3)	# 129-131
    sprite('ma020_04', 3)	# 132-134
    sprite('ma020_05', 3)	# 135-137
    sprite('ma020_06', 3)	# 138-140
    label(1)
    sprite('ma020_07', 4)	# 141-144
    sprite('ma020_08', 4)	# 145-148
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('ma024_00', 2)	# 149-150
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ma024_01', 5)	# 151-155
    sprite('ma024_02', 5)	# 156-160
    sprite('ma024_03', 9)	# 161-169
    sprite('ma024_04', 5)	# 170-174

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(5200)
        Unknown11091(31)
        AirUntechableTime(60)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9202(10)
        AirPushbackX(60000)
        AirPushbackY(12000)
        Unknown11001(10, 10, 18)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(60)
        Unknown9016(1)
        teleportRelativeY(0)
        setInvincible(1)
    sprite('ma430_00', 3)	# 1-3
    sprite('ma430_01', 3)	# 4-6
    Unknown2036(47, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_3('mase_09')
    sprite('ma430_02', 4)	# 7-10
    sprite('ma430_06', 3)	# 11-13	 **attackbox here**
    tag_voice(1, 'bma250_0', 'bma250_1', '', '')
    Unknown1051(50)
    sendToLabelUpon(2, 9)
    sprite('ma430_07', 3)	# 14-16	 **attackbox here**
    sprite('ma430_08', 3)	# 17-19	 **attackbox here**
    sprite('ma402_01ex01', 2)	# 20-21	 **attackbox here**
    GFX_0('maef430_ex', 0)
    GFX_0('maef430_ex', 1)
    Unknown1084(1)
    sprite('ma402_02ex01', 4)	# 22-25	 **attackbox here**
    GFX_0('maef430_ex', 0)
    GFX_0('maef430_ex', 1)
    physicsXImpulse(-12000)
    physicsYImpulse(20000)
    setGravity(2000)
    sprite('ma402_03ex01', 4)	# 26-29	 **attackbox here**
    GFX_0('maef430_ex', 0)
    sprite('ma402_04ex01', 4)	# 30-33	 **attackbox here**
    GFX_0('maef430_ex', 0)
    sprite('ma402_05ex01', 4)	# 34-37	 **attackbox here**
    GFX_0('maef430_ex', 0)
    sprite('ma402_06ex01', 4)	# 38-41	 **attackbox here**
    sprite('ma430_09', 40)	# 42-81	 **attackbox here**
    label(9)
    sprite('ma430_10', 2)	# 82-83	 **attackbox here**
    Unknown1019(30)
    GFX_0('maef430', -1)
    sprite('ma430_11', 2)	# 84-85
    GFX_0('maef430_lance', -1)
    sprite('ma430_12', 2)	# 86-87
    sprite('ma430_13', 2)	# 88-89
    Unknown1084(1)
    sprite('ma430_14', 2)	# 90-91
    sprite('ma430_15', 2)	# 92-93
    Unknown26('maef430')
    SFX_3('mase_07')
    SFX_3('mase_07')
    sprite('ma430_16', 2)	# 94-95
    sprite('ma430_17', 4)	# 96-99	 **attackbox here**
    Unknown2015(150)
    physicsXImpulse(120000)
    Unknown1028(3000)
    StartMultihit()
    sprite('ma430_17', 2)	# 100-101	 **attackbox here**
    tag_voice(0, 'bma251_0', 'bma251_1', '', '')
    GFX_0('maef430_strike', -1)
    GFX_0('maef430_bg', -1)

    def upon_ON_HIT_OR_BLOCK():
        Unknown1019(0)
        Unknown1028(0)
    sprite('ma430_18', 3)	# 102-104	 **attackbox here**
    sprite('ma430_19', 3)	# 105-107	 **attackbox here**
    Unknown1019(0)
    Unknown1028(0)
    sprite('ma430_20', 3)	# 108-110
    setInvincible(0)
    Unknown23027()
    sprite('ma430_18', 3)	# 111-113	 **attackbox here**
    sprite('ma430_19', 3)	# 114-116	 **attackbox here**
    sprite('ma430_20', 3)	# 117-119
    sprite('ma430_21', 4)	# 120-123
    sprite('ma430_22', 4)	# 124-127
    Unknown2015(-1)
    sprite('ma001_03', 4)	# 128-131
    GFX_0('maef_001_zanzou', -1)
    SFX_0('008_swing_pole_2')
    sprite('ma001_04', 4)	# 132-135
    sprite('ma001_05', 4)	# 136-139
    sprite('ma001_06', 4)	# 140-143
    sprite('ma001_07', 4)	# 144-147
    GFX_0('maef_001_zanzou2', -1)
    SFX_0('008_swing_pole_2')
    sprite('ma001_08', 4)	# 148-151
    sprite('ma001_09', 3)	# 152-154
    sprite('ma001_10', 2)	# 155-156

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(6200)
        Unknown11091(30)
        AirUntechableTime(60)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9202(10)
        AirPushbackX(60000)
        AirPushbackY(12000)
        Unknown11001(10, 10, 18)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(60)
        Unknown9016(1)

        def upon_12():
            GFX_0('maef430_od', -1)
        teleportRelativeY(0)
        setInvincible(1)
    sprite('ma430_00', 3)	# 1-3
    sprite('ma430_01', 3)	# 4-6
    SFX_3('mase_09')
    Unknown2036(47, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('ma430_02', 3)	# 7-9
    sprite('ma430_02', 1)	# 10-10
    sprite('ma430_06', 3)	# 11-13	 **attackbox here**
    tag_voice(1, 'bma250_0', 'bma250_1', '', '')
    Unknown1051(50)
    sendToLabelUpon(2, 9)
    sprite('ma430_07', 3)	# 14-16	 **attackbox here**
    sprite('ma430_08', 3)	# 17-19	 **attackbox here**
    sprite('ma402_01ex01', 2)	# 20-21	 **attackbox here**
    GFX_0('maef430_ex', 0)
    Unknown1084(1)
    sprite('ma402_02ex01', 4)	# 22-25	 **attackbox here**
    GFX_0('maef430_ex', 0)
    GFX_0('maef430_ex', 1)
    physicsXImpulse(-12000)
    physicsYImpulse(20000)
    setGravity(2000)
    sprite('ma402_03ex01', 4)	# 26-29	 **attackbox here**
    GFX_0('maef430_ex', 0)
    sprite('ma402_04ex01', 4)	# 30-33	 **attackbox here**
    GFX_0('maef430_ex', 0)
    sprite('ma402_05ex01', 4)	# 34-37	 **attackbox here**
    GFX_0('maef430_ex', 0)
    sprite('ma402_06ex01', 4)	# 38-41	 **attackbox here**
    sprite('ma430_09', 40)	# 42-81	 **attackbox here**
    label(9)
    sprite('ma430_10', 2)	# 82-83	 **attackbox here**
    Unknown1019(30)
    GFX_0('maef430', -1)
    sprite('ma430_11', 2)	# 84-85
    GFX_0('maef430_lance', -1)
    sprite('ma430_12', 2)	# 86-87
    sprite('ma430_13', 2)	# 88-89
    Unknown1084(1)
    sprite('ma430_14', 2)	# 90-91
    sprite('ma430_15', 2)	# 92-93
    Unknown26('maef430')
    SFX_3('mase_07')
    SFX_3('mase_07')
    sprite('ma430_16', 2)	# 94-95
    sprite('ma430_17', 4)	# 96-99	 **attackbox here**
    Unknown8007(100, 1, 1)
    Unknown2015(150)
    physicsXImpulse(120000)
    Unknown1028(3000)
    StartMultihit()
    sprite('ma430_17', 2)	# 100-101	 **attackbox here**
    tag_voice(0, 'bma251_0', 'bma251_1', '', '')
    GFX_0('maef430_strike', -1)
    GFX_0('maef430_bg', -1)
    ScreenShake(16000, 16000)
    Unknown8004(100, 1, 1)

    def upon_ON_HIT_OR_BLOCK():
        Unknown1019(0)
        Unknown1028(0)
    sprite('ma430_18', 3)	# 102-104	 **attackbox here**
    Unknown8010(100, 1, 1)
    sprite('ma430_19', 3)	# 105-107	 **attackbox here**
    Unknown1019(0)
    Unknown1028(0)
    sprite('ma430_20', 3)	# 108-110
    setInvincible(0)
    Unknown23027()
    sprite('ma430_18', 3)	# 111-113	 **attackbox here**
    sprite('ma430_19', 3)	# 114-116	 **attackbox here**
    sprite('ma430_20', 3)	# 117-119
    sprite('ma430_21', 4)	# 120-123
    sprite('ma430_22', 4)	# 124-127
    Unknown2015(-1)
    sprite('ma001_03', 4)	# 128-131
    GFX_0('maef_001_zanzou', -1)
    SFX_0('008_swing_pole_2')
    sprite('ma001_04', 4)	# 132-135
    sprite('ma001_05', 4)	# 136-139
    sprite('ma001_06', 4)	# 140-143
    sprite('ma001_07', 4)	# 144-147
    GFX_0('maef_001_zanzou2', -1)
    SFX_0('008_swing_pole_2')
    sprite('ma001_08', 4)	# 148-151
    sprite('ma001_09', 3)	# 152-154
    sprite('ma001_10', 2)	# 155-156

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Damage(0)
        Unknown11091(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(100)
        Unknown9142(80)
        Unknown11072(1, 200000, 0)
        Unknown9016(1)
        Unknown11064(1)
        Unknown11001(20, 0, 0)
        Unknown11069('AstralHeatExe')
        Unknown28(12, 'AstralHeatExe')
        setInvincible(1)
        SLOT_66 = 0
        if random_(2, 0, 50):
            SLOT_66 = 1
    sprite('ma450_00', 3)	# 1-3
    sprite('ma450_01', 3)	# 4-6
    sprite('ma450_02', 3)	# 7-9
    if SLOT_66:
        SFX_1('bma290_0')
    else:
        SFX_1('bma290_1')
    Unknown2036(105, -1, 2)
    GFX_0('EMB_MA_AH', -1)
    Unknown23147()
    GFX_0('maef450', -1)
    sprite('ma450_03', 3)	# 10-12
    sprite('ma450_04', 3)	# 13-15
    sprite('ma450_02', 3)	# 16-18
    sprite('ma450_03', 3)	# 19-21
    sprite('ma450_04', 3)	# 22-24
    sprite('ma450_02', 3)	# 25-27
    sprite('ma450_03', 3)	# 28-30
    sprite('ma450_04', 3)	# 31-33
    sprite('ma450_02', 3)	# 34-36
    sprite('ma450_03', 3)	# 37-39
    sprite('ma450_04', 3)	# 40-42
    sprite('ma450_02', 3)	# 43-45
    sprite('ma450_03', 3)	# 46-48
    sprite('ma450_04', 3)	# 49-51
    sprite('ma450_02', 3)	# 52-54
    sprite('ma450_03', 3)	# 55-57
    sprite('ma450_04', 3)	# 58-60
    sprite('ma450_02', 3)	# 61-63
    sprite('ma450_03', 3)	# 64-66
    sprite('ma450_04', 3)	# 67-69
    sprite('ma450_02', 3)	# 70-72
    sprite('ma450_03', 3)	# 73-75
    sprite('ma450_04', 3)	# 76-78
    sprite('ma450_02', 3)	# 79-81
    sprite('ma450_03', 3)	# 82-84
    sprite('ma450_04', 3)	# 85-87
    sprite('ma450_02', 3)	# 88-90
    sprite('ma450_03', 3)	# 91-93
    sprite('ma450_04', 3)	# 94-96
    sprite('ma450_02', 3)	# 97-99
    sprite('ma450_03', 3)	# 100-102
    sprite('ma450_04', 3)	# 103-105
    sprite('ma450_05', 4)	# 106-109
    sprite('ma450_06', 3)	# 110-112
    sprite('ma450_06', 1)	# 113-113
    SFX_0('006_swing_blade_2')
    sprite('ma450_07', 3)	# 114-116
    sprite('ma450_08', 3)	# 117-119
    teleportRelativeX(50000)
    sprite('ma450_09', 3)	# 120-122	 **attackbox here**
    GFX_0('maef450_slash', -1)
    sprite('ma450_10', 3)	# 123-125
    setInvincible(0)
    sprite('ma450_11', 3)	# 126-128
    sprite('ma450_12', 3)	# 129-131
    sprite('ma450_10', 3)	# 132-134
    sprite('ma450_11', 3)	# 135-137
    sprite('ma450_12', 3)	# 138-140
    sprite('ma450_10', 3)	# 141-143
    sprite('ma450_11', 3)	# 144-146
    sprite('ma450_12', 3)	# 147-149
    sprite('ma450_36', 4)	# 150-153
    sprite('ma450_37', 4)	# 154-157
    sprite('ma001_01', 4)	# 158-161
    SFX_0('008_swing_pole_2')
    sprite('ma001_02', 4)	# 162-165
    sprite('ma001_03', 4)	# 166-169
    sprite('ma001_04', 4)	# 170-173
    sprite('ma001_05', 4)	# 174-177
    sprite('ma001_06', 4)	# 178-181
    SFX_0('008_swing_pole_2')
    sprite('ma001_07', 4)	# 182-185
    sprite('ma001_08', 4)	# 186-189
    sprite('ma001_09', 4)	# 190-193
    sprite('ma001_10', 4)	# 194-197

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(2800)
        Unknown11091(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(40000)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(9999)
        Unknown9016(1)
        Unknown11064(1)
        Unknown11069('AstralHeatExe')
        Unknown11023(1)
        Unknown23084(1)
        Unknown23088(1, 1)
        Unknown23157(0)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20000(1)
        Unknown20006(1)
    sprite('ma450_10', 3)	# 1-3
    sprite('ma450_11', 3)	# 4-6
    sprite('ma450_12', 3)	# 7-9
    sprite('ma450_10', 3)	# 10-12
    sprite('ma450_11', 3)	# 13-15
    sprite('ma450_12', 3)	# 16-18
    sprite('ma450_10', 4)	# 19-22
    if SLOT_66:
        SFX_1('bma291_0')
    else:
        SFX_1('bma291_1')
    sprite('ma450_11', 4)	# 23-26
    sprite('ma450_12', 4)	# 27-30
    sprite('ma450_13', 4)	# 31-34
    sprite('ma450_14', 4)	# 35-38
    sprite('ma450_15', 4)	# 39-42
    sprite('ma450_16', 4)	# 43-46
    sprite('ma450_17', 4)	# 47-50
    sprite('ma450_18', 3)	# 51-53
    physicsXImpulse(2000)
    sprite('ma450_19', 3)	# 54-56
    Unknown1019(200)
    sprite('ma450_20', 3)	# 57-59
    Unknown1019(200)
    SFX_0('006_swing_blade_2')
    sprite('ma450_21', 3)	# 60-62
    Unknown1019(80)
    sprite('ma450_22', 3)	# 63-65
    physicsXImpulse(50000)
    sprite('ma450_23', 3)	# 66-68	 **attackbox here**
    if SLOT_66:
        SFX_1('bma292_0')
    else:
        SFX_1('bma292_1')
    RefreshMultihit()
    Unknown1084(1)
    GFX_0('maef450_upper', -1)
    sprite('ma450_24', 3)	# 69-71
    sprite('ma450_25', 3)	# 72-74
    sprite('ma450_26', 3)	# 75-77
    sprite('ma450_27', 4)	# 78-81
    sprite('ma450_28', 4)	# 82-85
    sprite('ma530_07', 4)	# 86-89
    teleportRelativeX(-100000)
    sprite('ma530_08', 4)	# 90-93
    sprite('ma530_09', 4)	# 94-97
    teleportRelativeX(-40000)
    sprite('ma530_10', 4)	# 98-101
    Unknown1084(1)
    sprite('ma530_11', 4)	# 102-105
    sprite('ma000_00', 3)	# 106-108
    sprite('ma023_00', 4)	# 109-112
    sprite('ma023_01', 4)	# 113-116
    sprite('ma020_00', 4)	# 117-120
    Unknown8001(1, 0)
    physicsYImpulse(90000)
    Unknown20000(0)
    GFX_0('AstralCamera', -1)
    sprite('ma020_01', 4)	# 121-124
    Unknown36(22)
    Unknown3038(1)
    Unknown1000(0)
    teleportRelativeY(6000000)
    setGravity(0)
    Unknown35()
    sprite('ma020_00', 4)	# 125-128
    sprite('ma020_01', 4)	# 129-132
    sprite('null', 30)	# 133-162
    Unknown21015('41737472616c43616d6572610000000000000000000000000000000000000000a10f000000000000')
    sprite('null', 20)	# 163-182
    Unknown1084(1)
    Unknown1000(0)
    teleportRelativeY(1400000)
    Unknown21015('41737472616c43616d6572610000000000000000000000000000000000000000a20f000000000000')
    sprite('ma450_29', 3)	# 183-185
    Unknown1099(-1)
    physicsYImpulse(200)
    GFX_0('maef450_charge', 0)
    sprite('ma450_30', 3)	# 186-188
    sprite('ma450_31', 3)	# 189-191
    sprite('ma450_29', 3)	# 192-194
    sprite('ma450_30', 3)	# 195-197
    sprite('ma450_31', 3)	# 198-200
    sprite('ma450_29', 3)	# 201-203
    sprite('ma450_30', 3)	# 204-206
    sprite('ma450_31', 3)	# 207-209
    sprite('ma450_29', 3)	# 210-212
    sprite('ma450_30', 3)	# 213-215
    sprite('ma450_31', 3)	# 216-218
    if SLOT_66:
        SFX_1('bma293_0')
    else:
        SFX_1('bma293_1')
    sprite('ma450_29', 3)	# 219-221
    sprite('ma450_30', 3)	# 222-224
    sprite('ma450_31', 3)	# 225-227
    sprite('ma450_29', 3)	# 228-230
    sprite('ma450_30', 3)	# 231-233
    sprite('ma450_31', 3)	# 234-236
    sprite('ma450_29', 3)	# 237-239
    sprite('ma450_30', 3)	# 240-242
    sprite('ma450_31', 3)	# 243-245
    sprite('ma450_29', 3)	# 246-248
    Unknown1099(0)
    physicsYImpulse(0)
    sprite('ma450_30', 3)	# 249-251
    sprite('ma450_31', 3)	# 252-254
    sprite('ma450_29', 3)	# 255-257
    sprite('ma450_30', 3)	# 258-260
    sprite('ma450_31', 3)	# 261-263
    sprite('ma450_29', 3)	# 264-266
    sprite('ma450_30', 3)	# 267-269
    sprite('ma450_31', 3)	# 270-272
    sprite('ma450_29', 3)	# 273-275
    if SLOT_66:
        SFX_1('bma294_0')
    sprite('ma450_30', 3)	# 276-278
    sprite('ma450_31', 3)	# 279-281
    sprite('ma450_29', 3)	# 282-284
    sprite('ma450_30', 3)	# 285-287
    sprite('ma450_31', 3)	# 288-290
    sprite('ma450_29', 3)	# 291-293
    if (not SLOT_66):
        SFX_1('bma294_1')
    sprite('ma450_30', 3)	# 294-296
    sprite('ma450_31', 3)	# 297-299
    sprite('ma450_29', 3)	# 300-302
    sprite('ma450_30', 3)	# 303-305
    sprite('ma450_31', 3)	# 306-308
    sprite('ma450_29', 3)	# 309-311
    sprite('ma450_30', 3)	# 312-314
    sprite('ma450_31', 3)	# 315-317
    sprite('ma450_32', 3)	# 318-320
    sprite('ma450_32ex', 3)	# 321-323
    GFX_0('maef450_throw', 0)
    Unknown26('maef450_charge')
    SFX_3('mase_07')
    SFX_3('mase_08')
    sprite('ma450_33', 3)	# 324-326
    sprite('ma450_33ex', 3)	# 327-329
    sprite('ma450_33', 3)	# 330-332
    sprite('ma450_33ex', 3)	# 333-335
    sprite('ma450_33', 3)	# 336-338
    sprite('ma450_33ex', 3)	# 339-341
    Unknown21015('41737472616c43616d6572610000000000000000000000000000000000000000a30f000000000000')
    Unknown26('maef450_throw')
    sprite('ma450_33', 3)	# 342-344
    sprite('ma450_33ex', 3)	# 345-347
    sprite('ma450_33', 3)	# 348-350
    sprite('ma450_33ex', 3)	# 351-353
    Unknown3004(-36)
    sprite('ma450_33', 3)	# 354-356
    sprite('ma450_33ex', 3)	# 357-359
    sprite('ma450_33', 3)	# 360-362
    sprite('null', 33)	# 363-395
    sprite('null', 285)	# 396-680
    Unknown21015('41737472616c43616d6572610000000000000000000000000000000000000000a40f000000000000')
    sprite('null', 30)	# 681-710
    Unknown21015('41737472616c43616d6572610000000000000000000000000000000000000000a50f000000000000')
    sprite('ma450_23', 60)	# 711-770	 **attackbox here**
    Unknown3038(1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(30800)
    Unknown11091(100)
    AirPushbackX(0)
    AirPushbackY(100000)
    YImpluseBeforeWallbounce(0)
    Hitstop(0)
    AirUntechableTime(9999)
    Unknown11064(3)
    Unknown11050('090000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23024(0)
    sprite('null', 60)	# 771-830
    Unknown3038(0)
    sprite('null', 40)	# 831-870
    Unknown20000(0)
    GFX_0('ma450yari_dummy', -1)
    sprite('ma450_38', 3)	# 871-873
    sendToLabelUpon(2, 99)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    teleportRelativeY(800000)
    teleportRelativeX(-180000)
    Unknown1043()
    sprite('ma450_39', 3)	# 874-876
    label(0)
    sprite('ma450_40', 4)	# 877-880
    sprite('ma450_41', 4)	# 881-884
    gotoLabel(0)
    label(99)
    sprite('ma450_42', 3)	# 885-887
    SFX_0('204_runjump_normal_1')
    sprite('ma450_43', 3)	# 888-890
    sprite('ma450_44', 3)	# 891-893
    sprite('ma450_45', 3)	# 894-896
    sprite('ma450_46', 3)	# 897-899
    sprite('ma450_47', 3)	# 900-902
    sprite('ma450_34', 4)	# 903-906
    teleportRelativeX(180000)
    Unknown26('ma450yari_dummy')
    sprite('ma450_35', 4)	# 907-910
    sprite('ma601_05', 6)	# 911-916
    SFX_0('024_getset_b')
    sprite('ma601_06', 6)	# 917-922
    sprite('ma601_07', 6)	# 923-928
    sprite('ma601_08', 15)	# 929-943
    sprite('ma601_09', 6)	# 944-949
    SFX_0('008_swing_pole_2')
    sprite('ma601_10', 6)	# 950-955
    sprite('ma601_11', 8)	# 956-963
    sprite('ma601_12', 8)	# 964-971
    sprite('ma601_13', 6)	# 972-977
    sprite('ma601_14', 6)	# 978-983
    sprite('ma000_00', 8)	# 984-991
    Unknown18010()
    sprite('ma610_00', 7)	# 992-998
    sprite('ma610_01', 8)	# 999-1006
    sprite('ma610_02', 12)	# 1007-1018
    sprite('ma610_03', 6)	# 1019-1024
    sprite('ma610_04', 12)	# 1025-1036
    sprite('ma610_05', 6)	# 1037-1042
    sprite('ma610_06', 6)	# 1043-1048
    Unknown21011(60)
    Unknown23018(1)
    sprite('ma610_06', 32767)	# 1049-33815

@Subroutine
def MouthTableInit():
    Unknown18011('bma000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma500', 12643, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma502', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24888, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma505', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma520', 12643, 12641, 25393, 12341, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma522', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma524', 12643, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma525', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12345, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma402_1', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma403_0', 12643, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma403_1', 12643, 13665, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma601baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma601biz', 12643, 12641, 25394, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma600bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma601bmk', 12643, 14177, 12643, 24882, 25399, 12337, 13921, 13923, 13921, 13923, 13921, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma600bno', 12643, 12641, 25397, 24887, 25399, 24887, 25399, 13621, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma600pce', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 14131, 12897, 25392, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma600pmi', 12643, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma601rrb', 12643, 24880, 13617, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma601uhy', 12643, 14177, 13155, 24880, 25399, 12337, 14177, 12643, 24880, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma601ume', 12641, 14179, 13409, 25392, 24887, 25399, 24887, 25399, 24887, 14129, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma701baz', 12643, 24880, 13617, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma700biz', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 13155, 24887, 25399, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma701bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma701bmk', 12643, 14177, 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma701bno', 12643, 14177, 12643, 24880, 12338, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma701pce', 12643, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma700pmi', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma700rrb', 12643, 12897, 25392, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma700uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 12899, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma701ume', 12643, 13153, 25392, 12340, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma290_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 12337, 14179, 12897, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma293_0', 14177, 12643, 24880, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma294_0', 14177, 14179, 14177, 14179, 12641, 25396, 13361, 13153, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma290_1', 13665, 13667, 13665, 13667, 13665, 13667, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma293_1', 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bma294_1', 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bjn')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bno')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('biz')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('ume')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('ma600_00', 10)	# 2-11
    sprite('ma600_00', 60)	# 12-71
    Unknown7006('bma502', 100, 895577442, 13104, 0, 0, 100, 895577442, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ma600_01', 6)	# 72-77
    sprite('ma600_02', 6)	# 78-83
    sprite('ma600_03', 6)	# 84-89
    SFX_0('019_cloth_c')
    sprite('ma600_04', 6)	# 90-95
    sprite('ma600_05', 6)	# 96-101
    sprite('ma600_06', 7)	# 102-108
    SFX_0('019_cloth_c')
    sprite('ma600_07', 7)	# 109-115
    sprite('ma600_08', 7)	# 116-122
    sprite('ma600_09', 6)	# 123-128
    GFX_0('maef_600', -1)
    sprite('ma600_10', 7)	# 129-135
    sprite('ma600_11', 6)	# 136-141
    sprite('ma600_12', 6)	# 142-147
    sprite('ma600_13', 6)	# 148-153
    SFX_0('008_swing_pole_2')
    sprite('ma600_14', 6)	# 154-159
    sprite('ma501_10', 6)	# 160-165
    sprite('ma501_11', 6)	# 166-171
    sprite('ma501_12', 6)	# 172-177
    Unknown23018(1)
    label(1)
    sprite('ma000_00', 7)	# 178-184
    sprite('ma000_01', 7)	# 185-191
    sprite('ma000_02', 7)	# 192-198
    sprite('ma000_03', 7)	# 199-205
    sprite('ma000_04', 7)	# 206-212
    sprite('ma000_05', 7)	# 213-219
    sprite('ma000_06', 7)	# 220-226
    sprite('ma000_07', 7)	# 227-233
    sprite('ma000_08', 7)	# 234-240
    sprite('ma000_09', 7)	# 241-247
    sprite('ma000_10', 7)	# 248-254
    sprite('ma000_11', 7)	# 255-261
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('ma601_00', 10)	# 262-271
    sprite('ma601_00', 30)	# 272-301
    if random_(2, 0, 66):
        Unknown7006('bma500', 100, 0, 0, 0, 0, 0, 895577442, 13360, 0, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown2037(1)
    sprite('ma601_00', 40)	# 302-341
    GFX_0('maef_601', -1)
    sprite('ma601_01', 6)	# 342-347
    Unknown26('maef_601')
    GFX_1('maef_601smoke', -1)
    ScreenShake(10000, 10000)
    SFX_3('mase_04')
    sprite('ma601_02', 6)	# 348-353
    sprite('ma601_03', 6)	# 354-359
    sprite('ma601_04', 6)	# 360-365
    sprite('ma601_05', 7)	# 366-372
    sprite('ma601_06', 7)	# 373-379
    sprite('ma601_07', 7)	# 380-386
    sprite('ma601_08', 7)	# 387-393
    sprite('ma601_09', 5)	# 394-398
    SFX_0('008_swing_pole_2')
    sprite('ma601_10', 7)	# 399-405
    if SLOT_2:
        SFX_1('bma501')
    sprite('ma601_11', 7)	# 406-412
    sprite('ma601_12', 7)	# 413-419
    sprite('ma601_13', 7)	# 420-426
    sprite('ma601_14', 7)	# 427-433
    Unknown23018(1)
    label(11)
    sprite('ma000_00', 7)	# 434-440
    sprite('ma000_01', 7)	# 441-447
    sprite('ma000_02', 7)	# 448-454
    sprite('ma000_03', 7)	# 455-461
    sprite('ma000_04', 7)	# 462-468
    sprite('ma000_05', 7)	# 469-475
    sprite('ma000_06', 7)	# 476-482
    sprite('ma000_07', 7)	# 483-489
    sprite('ma000_08', 7)	# 490-496
    sprite('ma000_09', 7)	# 497-503
    sprite('ma000_10', 7)	# 504-510
    sprite('ma000_11', 7)	# 511-517
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('ma602_00', 7)	# 518-524
    sprite('ma602_01', 7)	# 525-531
    sprite('ma602_02', 7)	# 532-538
    sprite('ma602_01', 7)	# 539-545
    sprite('ma602_00', 7)	# 546-552
    sprite('ma602_01', 7)	# 553-559
    sprite('ma602_02', 7)	# 560-566
    sprite('ma602_03', 7)	# 567-573
    sprite('ma602_04', 7)	# 574-580
    sprite('ma602_05', 7)	# 581-587
    sprite('ma602_06', 7)	# 588-594
    sprite('ma602_07', 5)	# 595-599
    sprite('ma602_08', 40)	# 600-639
    SFX_1('ma416')
    sprite('ma602_09', 6)	# 640-645
    sprite('ma602_10', 6)	# 646-651
    sprite('ma602_11', 6)	# 652-657
    sprite('ma602_12', 6)	# 658-663
    sprite('ma602_13', 10)	# 664-673
    sprite('ma602_12', 6)	# 674-679
    sprite('ma602_11', 6)	# 680-685
    sprite('ma602_10', 6)	# 686-691
    sprite('ma602_09', 6)	# 692-697
    sprite('ma602_08', 30)	# 698-727
    sprite('ma602_14', 6)	# 728-733
    sprite('ma203_14', 6)	# 734-739
    sprite('ma203_15', 6)	# 740-745
    sprite('ma203_16', 6)	# 746-751
    sprite('ma203_17', 6)	# 752-757
    Unknown21011(60)
    label(21)
    sprite('ma000_00', 7)	# 758-764
    sprite('ma000_01', 7)	# 765-771
    sprite('ma000_02', 7)	# 772-778
    sprite('ma000_03', 7)	# 779-785
    sprite('ma000_04', 7)	# 786-792
    sprite('ma000_05', 7)	# 793-799
    sprite('ma000_06', 7)	# 800-806
    sprite('ma000_07', 7)	# 807-813
    sprite('ma000_08', 7)	# 814-820
    sprite('ma000_09', 7)	# 821-827
    sprite('ma000_10', 7)	# 828-834
    sprite('ma000_11', 7)	# 835-841
    gotoLabel(21)
    ExitState()
    label(30)
    sprite('ma000_00', 1)	# 842-842
    SFX_1('bma700ume')
    label(31)
    sprite('ma000_00', 7)	# 843-849
    sprite('ma000_01', 7)	# 850-856
    sprite('ma000_02', 7)	# 857-863
    sprite('ma000_03', 7)	# 864-870
    sprite('ma000_04', 7)	# 871-877
    sprite('ma000_05', 7)	# 878-884
    sprite('ma000_06', 7)	# 885-891
    sprite('ma000_07', 7)	# 892-898
    sprite('ma000_08', 7)	# 899-905
    sprite('ma000_09', 7)	# 906-912
    sprite('ma000_10', 7)	# 913-919
    sprite('ma000_11', 7)	# 920-926
    gotoLabel(31)
    label(991)
    sprite('ma000_00', 1)	# 927-927
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ma000_00', 7)	# 928-934
    sprite('ma000_01', 7)	# 935-941
    sprite('ma000_02', 7)	# 942-948
    sprite('ma000_03', 7)	# 949-955
    sprite('ma000_04', 7)	# 956-962
    sprite('ma000_05', 7)	# 963-969
    sprite('ma000_06', 7)	# 970-976
    sprite('ma000_07', 7)	# 977-983
    sprite('ma000_08', 7)	# 984-990
    sprite('ma000_09', 7)	# 991-997
    sprite('ma000_10', 7)	# 998-1004
    sprite('ma000_11', 7)	# 1005-1011
    gotoLabel(992)
    label(100)
    sprite('ma000_00', 1)	# 1012-1012
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('ma000_00', 7)	# 1013-1019
    sprite('ma000_01', 7)	# 1020-1026
    sprite('ma000_02', 7)	# 1027-1033
    sprite('ma000_03', 7)	# 1034-1040
    sprite('ma000_04', 7)	# 1041-1047
    sprite('ma000_05', 7)	# 1048-1054
    sprite('ma000_06', 7)	# 1055-1061
    sprite('ma000_07', 7)	# 1062-1068
    sprite('ma000_08', 7)	# 1069-1075
    sprite('ma000_09', 7)	# 1076-1082
    sprite('ma000_10', 7)	# 1083-1089
    sprite('ma000_11', 7)	# 1090-1096
    gotoLabel(101)
    label(102)
    sprite('ma300_00', 7)	# 1097-1103
    SFX_1('bma601baz')
    sprite('ma300_01', 7)	# 1104-1110
    SFX_0('019_cloth_a')
    sprite('ma300_02', 7)	# 1111-1117
    sprite('ma300_03', 7)	# 1118-1124
    sprite('ma300_04', 7)	# 1125-1131
    sprite('ma300_05', 12)	# 1132-1143
    sprite('ma300_06', 7)	# 1144-1150
    sprite('ma300_07', 7)	# 1151-1157
    sprite('ma001_08', 7)	# 1158-1164
    sprite('ma001_09', 7)	# 1165-1171
    sprite('ma001_10', 7)	# 1172-1178
    Unknown23018(1)
    label(103)
    sprite('ma000_00', 7)	# 1179-1185
    sprite('ma000_01', 7)	# 1186-1192
    sprite('ma000_02', 7)	# 1193-1199
    sprite('ma000_03', 7)	# 1200-1206
    sprite('ma000_04', 7)	# 1207-1213
    sprite('ma000_05', 7)	# 1214-1220
    sprite('ma000_06', 7)	# 1221-1227
    sprite('ma000_07', 7)	# 1228-1234
    sprite('ma000_08', 7)	# 1235-1241
    sprite('ma000_09', 7)	# 1242-1248
    sprite('ma000_10', 7)	# 1249-1255
    sprite('ma000_11', 7)	# 1256-1262
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('ma600_00', 10)	# 1263-1272
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ma600_00', 60)	# 1273-1332
    SFX_1('bma600bjn')
    sprite('ma600_01', 6)	# 1333-1338
    sprite('ma600_02', 6)	# 1339-1344
    sprite('ma600_03', 6)	# 1345-1350
    SFX_0('019_cloth_c')
    sprite('ma600_04', 6)	# 1351-1356
    sprite('ma600_05', 6)	# 1357-1362
    sprite('ma600_06', 7)	# 1363-1369
    SFX_0('019_cloth_c')
    sprite('ma600_07', 7)	# 1370-1376
    sprite('ma600_08', 7)	# 1377-1383
    sprite('ma600_09', 6)	# 1384-1389
    GFX_0('maef_600', -1)
    sprite('ma600_10', 7)	# 1390-1396
    sprite('ma600_11', 6)	# 1397-1402
    sprite('ma600_12', 6)	# 1403-1408
    sprite('ma600_13', 6)	# 1409-1414
    SFX_0('008_swing_pole_2')
    sprite('ma600_14', 6)	# 1415-1420
    sprite('ma501_10', 6)	# 1421-1426
    sprite('ma501_11', 6)	# 1427-1432
    sprite('ma501_12', 6)	# 1433-1438
    label(111)
    sprite('ma000_00', 7)	# 1439-1445
    sprite('ma000_01', 7)	# 1446-1452
    sprite('ma000_02', 7)	# 1453-1459
    sprite('ma000_03', 7)	# 1460-1466
    sprite('ma000_04', 7)	# 1467-1473
    sprite('ma000_05', 7)	# 1474-1480
    sprite('ma000_06', 7)	# 1481-1487
    sprite('ma000_07', 7)	# 1488-1494
    sprite('ma000_08', 7)	# 1495-1501
    sprite('ma000_09', 7)	# 1502-1508
    sprite('ma000_10', 7)	# 1509-1515
    sprite('ma000_11', 7)	# 1516-1522
    if SLOT_97:
        _gotolabel(111)
    sprite('ma000_00', 1)	# 1523-1523
    Unknown21007(24, 40)
    Unknown21011(240)
    label(112)
    sprite('ma000_00', 7)	# 1524-1530
    sprite('ma000_01', 7)	# 1531-1537
    sprite('ma000_02', 7)	# 1538-1544
    sprite('ma000_03', 7)	# 1545-1551
    sprite('ma000_04', 7)	# 1552-1558
    sprite('ma000_05', 7)	# 1559-1565
    sprite('ma000_06', 7)	# 1566-1572
    sprite('ma000_07', 7)	# 1573-1579
    sprite('ma000_08', 7)	# 1580-1586
    sprite('ma000_09', 7)	# 1587-1593
    sprite('ma000_10', 7)	# 1594-1600
    sprite('ma000_11', 7)	# 1601-1607
    gotoLabel(112)
    ExitState()
    label(120)
    ExitState()
    label(130)
    sprite('ma600_00', 10)	# 1608-1617
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ma600_00', 60)	# 1618-1677
    SFX_1('bma600bno')
    sprite('ma600_01', 6)	# 1678-1683
    sprite('ma600_02', 6)	# 1684-1689
    sprite('ma600_03', 6)	# 1690-1695
    SFX_0('019_cloth_c')
    sprite('ma600_04', 6)	# 1696-1701
    sprite('ma600_05', 6)	# 1702-1707
    sprite('ma600_06', 7)	# 1708-1714
    SFX_0('019_cloth_c')
    sprite('ma600_07', 7)	# 1715-1721
    sprite('ma600_08', 7)	# 1722-1728
    sprite('ma600_09', 6)	# 1729-1734
    GFX_0('maef_600', -1)
    sprite('ma600_10', 7)	# 1735-1741
    sprite('ma600_11', 6)	# 1742-1747
    sprite('ma600_12', 6)	# 1748-1753
    sprite('ma600_13', 6)	# 1754-1759
    SFX_0('008_swing_pole_2')
    sprite('ma600_14', 6)	# 1760-1765
    sprite('ma501_10', 6)	# 1766-1771
    sprite('ma501_11', 6)	# 1772-1777
    sprite('ma501_12', 6)	# 1778-1783
    label(131)
    sprite('ma000_00', 7)	# 1784-1790
    sprite('ma000_01', 7)	# 1791-1797
    sprite('ma000_02', 7)	# 1798-1804
    sprite('ma000_03', 7)	# 1805-1811
    sprite('ma000_04', 7)	# 1812-1818
    sprite('ma000_05', 7)	# 1819-1825
    sprite('ma000_06', 7)	# 1826-1832
    sprite('ma000_07', 7)	# 1833-1839
    sprite('ma000_08', 7)	# 1840-1846
    sprite('ma000_09', 7)	# 1847-1853
    sprite('ma000_10', 7)	# 1854-1860
    sprite('ma000_11', 7)	# 1861-1867
    if SLOT_97:
        _gotolabel(131)
    sprite('ma000_00', 1)	# 1868-1868
    Unknown21007(24, 40)
    Unknown21011(360)
    label(132)
    sprite('ma000_00', 7)	# 1869-1875
    sprite('ma000_01', 7)	# 1876-1882
    sprite('ma000_02', 7)	# 1883-1889
    sprite('ma000_03', 7)	# 1890-1896
    sprite('ma000_04', 7)	# 1897-1903
    sprite('ma000_05', 7)	# 1904-1910
    sprite('ma000_06', 7)	# 1911-1917
    sprite('ma000_07', 7)	# 1918-1924
    sprite('ma000_08', 7)	# 1925-1931
    sprite('ma000_09', 7)	# 1932-1938
    sprite('ma000_10', 7)	# 1939-1945
    sprite('ma000_11', 7)	# 1946-1952
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('ma600_00', 10)	# 1953-1962
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ma600_00', 60)	# 1963-2022
    SFX_1('bma600pce')
    sprite('ma600_01', 6)	# 2023-2028
    sprite('ma600_02', 6)	# 2029-2034
    sprite('ma600_03', 6)	# 2035-2040
    SFX_0('019_cloth_c')
    sprite('ma600_04', 6)	# 2041-2046
    sprite('ma600_05', 6)	# 2047-2052
    sprite('ma600_06', 7)	# 2053-2059
    SFX_0('019_cloth_c')
    sprite('ma600_07', 7)	# 2060-2066
    sprite('ma600_08', 7)	# 2067-2073
    sprite('ma600_09', 6)	# 2074-2079
    GFX_0('maef_600', -1)
    sprite('ma600_10', 7)	# 2080-2086
    sprite('ma600_11', 6)	# 2087-2092
    sprite('ma600_12', 6)	# 2093-2098
    sprite('ma600_13', 6)	# 2099-2104
    SFX_0('008_swing_pole_2')
    sprite('ma600_14', 6)	# 2105-2110
    sprite('ma501_10', 6)	# 2111-2116
    sprite('ma501_11', 6)	# 2117-2122
    sprite('ma501_12', 6)	# 2123-2128
    Unknown21011(420)
    label(141)
    sprite('ma000_00', 7)	# 2129-2135
    sprite('ma000_01', 7)	# 2136-2142
    sprite('ma000_02', 7)	# 2143-2149
    sprite('ma000_03', 7)	# 2150-2156
    Unknown21007(24, 40)
    sprite('ma000_04', 7)	# 2157-2163
    sprite('ma000_05', 7)	# 2164-2170
    sprite('ma000_06', 7)	# 2171-2177
    sprite('ma000_07', 7)	# 2178-2184
    sprite('ma000_08', 7)	# 2185-2191
    sprite('ma000_09', 7)	# 2192-2198
    sprite('ma000_10', 7)	# 2199-2205
    sprite('ma000_11', 7)	# 2206-2212
    gotoLabel(141)
    ExitState()
    label(150)
    sprite('ma615_00', 6)	# 2213-2218
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
        Unknown2037(1)
    else:
        Unknown1000(-1465000)
    sprite('ma615_01', 6)	# 2219-2224
    sprite('ma615_02', 9)	# 2225-2233
    sprite('ma615_03', 9)	# 2234-2242
    sprite('ma615_04', 9)	# 2243-2251
    SFX_1('bma600pmi')
    sprite('ma615_05', 10)	# 2252-2261
    sprite('ma615_06', 9)	# 2262-2270
    sprite('ma615_02', 9)	# 2271-2279
    sprite('ma615_03', 9)	# 2280-2288
    sprite('ma615_04', 9)	# 2289-2297
    sprite('ma615_05', 10)	# 2298-2307
    sprite('ma615_06', 9)	# 2308-2316
    label(151)
    sprite('ma615_02', 9)	# 2317-2325
    sprite('ma615_03', 9)	# 2326-2334
    sprite('ma615_04', 9)	# 2335-2343
    sprite('ma615_05', 10)	# 2344-2353
    sprite('ma615_06', 9)	# 2354-2362
    loopRest()
    if SLOT_97:
        _gotolabel(151)
    sprite('ma615_02', 9)	# 2363-2371
    sprite('ma615_03', 9)	# 2372-2380
    sprite('ma615_04', 9)	# 2381-2389
    sprite('ma615_05', 10)	# 2390-2399
    Unknown21007(24, 40)
    Unknown21011(240)
    sprite('ma615_06', 9)	# 2400-2408
    sprite('ma615_02', 11)	# 2409-2419
    sprite('ma615_01', 6)	# 2420-2425
    sprite('ma615_00', 5)	# 2426-2430
    sprite('ma615_00', 1)	# 2431-2431
    if (not SLOT_2):
        sendToLabel(152)
    sprite('ma003_00', 3)	# 2432-2434
    Unknown2005()
    sprite('ma003_01', 3)	# 2435-2437
    sprite('ma003_00ex01', 3)	# 2438-2440
    label(152)
    sprite('ma000_00', 7)	# 2441-2447
    sprite('ma000_01', 7)	# 2448-2454
    sprite('ma000_02', 7)	# 2455-2461
    sprite('ma000_03', 7)	# 2462-2468
    sprite('ma000_04', 7)	# 2469-2475
    sprite('ma000_05', 7)	# 2476-2482
    sprite('ma000_06', 7)	# 2483-2489
    sprite('ma000_07', 7)	# 2490-2496
    sprite('ma000_08', 7)	# 2497-2503
    sprite('ma000_09', 7)	# 2504-2510
    sprite('ma000_10', 7)	# 2511-2517
    sprite('ma000_11', 7)	# 2518-2524
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('ma000_00', 1)	# 2525-2525
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2037(1)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ma000_00', 7)	# 2526-2532
    sprite('ma000_01', 7)	# 2533-2539
    sprite('ma000_02', 7)	# 2540-2546
    sprite('ma000_03', 7)	# 2547-2553
    sprite('ma000_04', 7)	# 2554-2560
    sprite('ma000_05', 7)	# 2561-2567
    sprite('ma000_06', 7)	# 2568-2574
    sprite('ma000_07', 7)	# 2575-2581
    sprite('ma000_08', 7)	# 2582-2588
    sprite('ma000_09', 7)	# 2589-2595
    sprite('ma000_10', 7)	# 2596-2602
    sprite('ma000_11', 7)	# 2603-2609
    gotoLabel(161)
    label(162)
    sprite('keep', 1)	# 2610-2610
    if (not SLOT_2):
        sendToLabel(163)
    sprite('ma003_00', 3)	# 2611-2613
    Unknown2005()
    sprite('ma003_01', 3)	# 2614-2616
    sprite('ma003_00ex01', 3)	# 2617-2619
    label(163)
    sprite('ma611_00', 5)	# 2620-2624
    SFX_1('bma601rrb')
    sprite('ma611_01', 5)	# 2625-2629
    sprite('ma611_02', 5)	# 2630-2634
    Unknown23018(1)
    sprite('ma611_03', 32767)	# 2635-35401
    ExitState()
    label(170)
    sprite('ma000_00', 1)	# 35402-35402
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ma000_00', 7)	# 35403-35409
    sprite('ma000_01', 7)	# 35410-35416
    sprite('ma000_02', 7)	# 35417-35423
    sprite('ma000_03', 7)	# 35424-35430
    sprite('ma000_04', 7)	# 35431-35437
    sprite('ma000_05', 7)	# 35438-35444
    sprite('ma000_06', 7)	# 35445-35451
    sprite('ma000_07', 7)	# 35452-35458
    sprite('ma000_08', 7)	# 35459-35465
    sprite('ma000_09', 7)	# 35466-35472
    sprite('ma000_10', 7)	# 35473-35479
    sprite('ma000_11', 7)	# 35480-35486
    gotoLabel(171)
    label(172)
    sprite('ma615_00', 6)	# 35487-35492
    sprite('ma615_01', 6)	# 35493-35498
    sprite('ma615_02', 9)	# 35499-35507
    sprite('ma615_03', 9)	# 35508-35516
    sprite('ma615_04', 9)	# 35517-35525
    SFX_1('bma601uhy')
    sprite('ma615_05', 10)	# 35526-35535
    sprite('ma615_06', 9)	# 35536-35544
    sprite('ma615_02', 9)	# 35545-35553
    sprite('ma615_03', 9)	# 35554-35562
    sprite('ma615_04', 9)	# 35563-35571
    sprite('ma615_05', 10)	# 35572-35581
    sprite('ma615_06', 9)	# 35582-35590
    label(173)
    sprite('ma615_02', 9)	# 35591-35599
    sprite('ma615_03', 9)	# 35600-35608
    sprite('ma615_04', 9)	# 35609-35617
    sprite('ma615_05', 10)	# 35618-35627
    sprite('ma615_06', 9)	# 35628-35636
    loopRest()
    if SLOT_97:
        _gotolabel(173)
    sprite('ma615_02', 9)	# 35637-35645
    sprite('ma615_03', 9)	# 35646-35654
    sprite('ma615_04', 9)	# 35655-35663
    sprite('ma615_05', 10)	# 35664-35673
    sprite('ma615_06', 9)	# 35674-35682
    sprite('ma615_02', 11)	# 35683-35693
    sprite('ma615_01', 6)	# 35694-35699
    sprite('ma615_00', 6)	# 35700-35705
    Unknown23018(1)
    label(174)
    sprite('ma000_00', 7)	# 35706-35712
    sprite('ma000_01', 7)	# 35713-35719
    sprite('ma000_02', 7)	# 35720-35726
    sprite('ma000_03', 7)	# 35727-35733
    sprite('ma000_04', 7)	# 35734-35740
    sprite('ma000_05', 7)	# 35741-35747
    sprite('ma000_06', 7)	# 35748-35754
    sprite('ma000_07', 7)	# 35755-35761
    sprite('ma000_08', 7)	# 35762-35768
    sprite('ma000_09', 7)	# 35769-35775
    sprite('ma000_10', 7)	# 35776-35782
    sprite('ma000_11', 7)	# 35783-35789
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('ma000_00', 1)	# 35790-35790
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('ma000_00', 7)	# 35791-35797
    sprite('ma000_01', 7)	# 35798-35804
    sprite('ma000_02', 7)	# 35805-35811
    sprite('ma000_03', 7)	# 35812-35818
    sprite('ma000_04', 7)	# 35819-35825
    sprite('ma000_05', 7)	# 35826-35832
    sprite('ma000_06', 7)	# 35833-35839
    sprite('ma000_07', 7)	# 35840-35846
    sprite('ma000_08', 7)	# 35847-35853
    sprite('ma000_09', 7)	# 35854-35860
    sprite('ma000_10', 7)	# 35861-35867
    sprite('ma000_11', 7)	# 35868-35874
    gotoLabel(181)
    label(182)
    sprite('ma300_00', 7)	# 35875-35881
    SFX_1('bma601biz')
    sprite('ma300_01', 7)	# 35882-35888
    SFX_0('019_cloth_a')
    sprite('ma300_02', 7)	# 35889-35895
    sprite('ma300_03', 7)	# 35896-35902
    sprite('ma300_04', 7)	# 35903-35909
    sprite('ma300_05', 12)	# 35910-35921
    sprite('ma300_06', 7)	# 35922-35928
    sprite('ma300_07', 7)	# 35929-35935
    sprite('ma001_08', 7)	# 35936-35942
    sprite('ma001_09', 7)	# 35943-35949
    sprite('ma001_10', 7)	# 35950-35956
    Unknown23018(1)
    label(183)
    sprite('ma000_00', 7)	# 35957-35963
    sprite('ma000_01', 7)	# 35964-35970
    sprite('ma000_02', 7)	# 35971-35977
    sprite('ma000_03', 7)	# 35978-35984
    sprite('ma000_04', 7)	# 35985-35991
    sprite('ma000_05', 7)	# 35992-35998
    sprite('ma000_06', 7)	# 35999-36005
    sprite('ma000_07', 7)	# 36006-36012
    sprite('ma000_08', 7)	# 36013-36019
    sprite('ma000_09', 7)	# 36020-36026
    sprite('ma000_10', 7)	# 36027-36033
    sprite('ma000_11', 7)	# 36034-36040
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('ma000_00', 1)	# 36041-36041
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2037(1)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ma000_00', 7)	# 36042-36048
    sprite('ma000_01', 7)	# 36049-36055
    sprite('ma000_02', 7)	# 36056-36062
    sprite('ma000_03', 7)	# 36063-36069
    sprite('ma000_04', 7)	# 36070-36076
    sprite('ma000_05', 7)	# 36077-36083
    sprite('ma000_06', 7)	# 36084-36090
    sprite('ma000_07', 7)	# 36091-36097
    sprite('ma000_08', 7)	# 36098-36104
    sprite('ma000_09', 7)	# 36105-36111
    sprite('ma000_10', 7)	# 36112-36118
    sprite('ma000_11', 7)	# 36119-36125
    gotoLabel(191)
    label(192)
    sprite('keep', 1)	# 36126-36126
    if (not SLOT_2):
        sendToLabel(193)
    sprite('ma003_00', 3)	# 36127-36129
    Unknown2005()
    sprite('ma003_01', 3)	# 36130-36132
    sprite('ma003_00ex01', 3)	# 36133-36135
    label(193)
    sprite('ma611_00', 5)	# 36136-36140
    SFX_1('bma601ume')
    sprite('ma611_01', 5)	# 36141-36145
    sprite('ma611_02', 5)	# 36146-36150
    Unknown23018(1)
    sprite('ma611_03', 32767)	# 36151-68917
    ExitState()
    label(200)
    sprite('ma634_00', 32767)	# 68918-101684
    if SLOT_158:
        Unknown1000(-1300000)
    else:
        Unknown1000(-1300000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bma601bmk')
        Unknown23018(1)
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
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('biz'):
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
    sprite('keep', 1)	# 4-4
    if SLOT_158:
        if SLOT_52:
            sendToLabel(0)
        elif random_(2, 0, 50):
            sendToLabel(0)
        else:
            sendToLabel(10)
    elif random_(2, 0, 50):
        sendToLabel(0)
    else:
        sendToLabel(10)
    label(0)
    sprite('ma610_00', 7)	# 5-11
    sprite('ma610_01', 8)	# 12-19
    sprite('ma610_02', 12)	# 20-31
    sprite('ma610_03', 6)	# 32-37
    sprite('ma610_04', 12)	# 38-49
    sprite('ma610_05', 6)	# 50-55
    sprite('ma610_06', 6)	# 56-61
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bma524', 100, 895577442, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bma402_0', 100, 878800226, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bma522', 100, 895577442, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ma610_06', 32767)	# 62-32828
    label(10)
    sprite('ma615_00', 6)	# 32829-32834
    sprite('ma615_01', 6)	# 32835-32840
    sprite('ma615_02', 9)	# 32841-32849
    sprite('ma615_03', 9)	# 32850-32858
    sprite('ma615_04', 9)	# 32859-32867
    if SLOT_158:
        if SLOT_108:
            Unknown7006('bma402_0', 100, 878800226, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bma520', 100, 895577442, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ma615_05', 10)	# 32868-32877
    sprite('ma615_06', 9)	# 32878-32886
    sprite('ma615_02', 9)	# 32887-32895
    sprite('ma615_03', 9)	# 32896-32904
    sprite('ma615_04', 9)	# 32905-32913
    sprite('ma615_05', 10)	# 32914-32923
    sprite('ma615_06', 9)	# 32924-32932
    label(11)
    sprite('ma615_02', 9)	# 32933-32941
    sprite('ma615_03', 9)	# 32942-32950
    sprite('ma615_04', 9)	# 32951-32959
    sprite('ma615_05', 10)	# 32960-32969
    sprite('ma615_06', 9)	# 32970-32978
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('ma611_00', 5)	# 32979-32983
    Unknown2053(0)
    Unknown2034(0)
    Unknown20003(1)
    SFX_1('ma407')
    sprite('ma611_01', 5)	# 32984-32988
    sprite('ma611_02', 5)	# 32989-32993
    sprite('ma611_03', 10)	# 32994-33003
    sprite('ma611_04', 5)	# 33004-33008
    teleportRelativeX(-40000)
    sprite('ma611_05', 5)	# 33009-33013
    teleportRelativeX(-40000)
    sprite('ma602_08', 80)	# 33014-33093
    teleportRelativeX(-10000)
    sprite('ma602_09', 3)	# 33094-33096
    sprite('ma602_10', 3)	# 33097-33099
    sprite('ma602_11', 3)	# 33100-33102
    sprite('ma602_12', 3)	# 33103-33105
    sprite('ma602_13', 6)	# 33106-33111
    sprite('ma602_12', 3)	# 33112-33114
    sprite('ma602_11', 3)	# 33115-33117
    sprite('ma602_10', 3)	# 33118-33120
    sprite('ma602_09', 3)	# 33121-33123
    sprite('ma602_08', 3)	# 33124-33126
    sprite('ma602_08', 20)	# 33127-33146
    SFX_1('bma520')
    Unknown23018(1)
    sprite('ma003_00', 3)	# 33147-33149
    Unknown2005()
    sprite('ma003_01', 3)	# 33150-33152
    sprite('ma003_00ex01', 3)	# 33153-33155
    sprite('ma032_00ex', 4)	# 33156-33159
    Unknown8007(100, 1, 1)
    physicsXImpulse(5000)
    Unknown1028(500)
    sprite('ma032_01ex', 4)	# 33160-33163
    sprite('ma032_02ex', 3)	# 33164-33166
    sprite('ma032_03ex', 3)	# 33167-33169
    Unknown8006(100, 1, 1)
    sprite('ma032_04ex', 3)	# 33170-33172
    sprite('ma032_05ex', 3)	# 33173-33175
    sprite('ma032_06ex', 4)	# 33176-33179
    sprite('ma032_07ex', 3)	# 33180-33182
    sprite('ma032_08ex', 3)	# 33183-33185
    Unknown8006(100, 1, 1)
    sprite('ma032_09ex', 3)	# 33186-33188
    sprite('ma032_10ex', 3)	# 33189-33191
    sprite('ma032_01ex', 4)	# 33192-33195
    sprite('ma032_02ex', 3)	# 33196-33198
    sprite('ma032_03ex', 3)	# 33199-33201
    Unknown8006(100, 1, 1)
    sprite('ma032_04ex', 3)	# 33202-33204
    sprite('ma032_05ex', 3)	# 33205-33207
    sprite('ma032_06ex', 4)	# 33208-33211
    sprite('ma032_07ex', 3)	# 33212-33214
    sprite('ma032_08ex', 3)	# 33215-33217
    Unknown8006(100, 1, 1)
    sprite('ma032_09ex', 3)	# 33218-33220
    sprite('ma032_10ex', 3)	# 33221-33223
    label(21)
    sprite('ma032_01ex', 4)	# 33224-33227
    sprite('ma032_02ex', 3)	# 33228-33230
    sprite('ma032_03ex', 3)	# 33231-33233
    sprite('ma032_04ex', 3)	# 33234-33236
    sprite('ma032_05ex', 3)	# 33237-33239
    sprite('ma032_06ex', 4)	# 33240-33243
    sprite('ma032_07ex', 3)	# 33244-33246
    sprite('ma032_08ex', 3)	# 33247-33249
    sprite('ma032_09ex', 3)	# 33250-33252
    sprite('ma032_10ex', 3)	# 33253-33255
    loopRest()
    gotoLabel(21)
    label(100)
    sprite('ma000_00', 6)	# 33256-33261

    def upon_40():
        clearUponHandler(40)
        SFX_1('bma701baz')
        Unknown23018(1)
    sprite('ma001_01', 6)	# 33262-33267
    sprite('ma620_00', 6)	# 33268-33273
    SFX_0('008_swing_pole_2')
    sprite('ma203_00', 6)	# 33274-33279
    sprite('ma620_01', 6)	# 33280-33285
    sprite('ma620_02', 6)	# 33286-33291
    sprite('ma620_02ex1', 6)	# 33292-33297
    sprite('ma620_02ex2', 6)	# 33298-33303
    sprite('ma620_03', 6)	# 33304-33309
    sprite('ma620_04', 6)	# 33310-33315
    sprite('ma620_05', 6)	# 33316-33321
    sprite('ma620_05ex1', 32767)	# 33322-66088
    label(110)
    sprite('ma000_00', 1)	# 66089-66089

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ma000_00', 7)	# 66090-66096
    sprite('ma000_01', 7)	# 66097-66103
    sprite('ma000_02', 7)	# 66104-66110
    sprite('ma000_03', 7)	# 66111-66117
    sprite('ma000_04', 7)	# 66118-66124
    sprite('ma000_05', 7)	# 66125-66131
    sprite('ma000_06', 7)	# 66132-66138
    sprite('ma000_07', 7)	# 66139-66145
    sprite('ma000_08', 7)	# 66146-66152
    sprite('ma000_09', 7)	# 66153-66159
    sprite('ma000_10', 7)	# 66160-66166
    sprite('ma000_11', 7)	# 66167-66173
    gotoLabel(111)
    label(112)
    sprite('ma610_00', 7)	# 66174-66180
    sprite('ma610_01', 8)	# 66181-66188
    sprite('ma610_02', 12)	# 66189-66200
    sprite('ma610_03', 6)	# 66201-66206
    sprite('ma610_04', 12)	# 66207-66218
    sprite('ma610_05', 6)	# 66219-66224
    sprite('ma610_06', 6)	# 66225-66230
    SFX_1('bma701bjn')
    Unknown23018(1)
    sprite('ma610_06', 32767)	# 66231-98997
    label(120)
    sprite('ma000_00', 1)	# 98998-98998

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ma000_00', 7)	# 98999-99005
    sprite('ma000_01', 7)	# 99006-99012
    sprite('ma000_02', 7)	# 99013-99019
    sprite('ma000_03', 7)	# 99020-99026
    sprite('ma000_04', 7)	# 99027-99033
    sprite('ma000_05', 7)	# 99034-99040
    sprite('ma000_06', 7)	# 99041-99047
    sprite('ma000_07', 7)	# 99048-99054
    sprite('ma000_08', 7)	# 99055-99061
    sprite('ma000_09', 7)	# 99062-99068
    sprite('ma000_10', 7)	# 99069-99075
    sprite('ma000_11', 7)	# 99076-99082
    gotoLabel(121)
    label(122)
    sprite('ma610_00', 7)	# 99083-99089
    sprite('ma610_01', 8)	# 99090-99097
    sprite('ma610_02', 12)	# 99098-99109
    sprite('ma610_03', 6)	# 99110-99115
    sprite('ma610_04', 12)	# 99116-99127
    sprite('ma610_05', 6)	# 99128-99133
    sprite('ma610_06', 6)	# 99134-99139
    SFX_1('bma701bmk')
    Unknown23018(1)
    sprite('ma610_06', 32767)	# 99140-131906
    label(130)
    sprite('ma000_00', 1)	# 131907-131907

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ma000_00', 7)	# 131908-131914
    sprite('ma000_01', 7)	# 131915-131921
    sprite('ma000_02', 7)	# 131922-131928
    sprite('ma000_03', 7)	# 131929-131935
    sprite('ma000_04', 7)	# 131936-131942
    sprite('ma000_05', 7)	# 131943-131949
    sprite('ma000_06', 7)	# 131950-131956
    sprite('ma000_07', 7)	# 131957-131963
    sprite('ma000_08', 7)	# 131964-131970
    sprite('ma000_09', 7)	# 131971-131977
    sprite('ma000_10', 7)	# 131978-131984
    sprite('ma000_11', 7)	# 131985-131991
    gotoLabel(131)
    label(132)
    sprite('ma610_00', 7)	# 131992-131998
    sprite('ma610_01', 8)	# 131999-132006
    sprite('ma610_02', 12)	# 132007-132018
    sprite('ma610_03', 6)	# 132019-132024
    sprite('ma610_04', 12)	# 132025-132036
    sprite('ma610_05', 6)	# 132037-132042
    sprite('ma610_06', 6)	# 132043-132048
    SFX_1('bma701bno')
    Unknown23018(1)
    sprite('ma610_06', 32767)	# 132049-164815
    label(140)
    sprite('ma000_00', 1)	# 164816-164816

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ma000_00', 7)	# 164817-164823
    sprite('ma000_01', 7)	# 164824-164830
    sprite('ma000_02', 7)	# 164831-164837
    sprite('ma000_03', 7)	# 164838-164844
    sprite('ma000_04', 7)	# 164845-164851
    sprite('ma000_05', 7)	# 164852-164858
    sprite('ma000_06', 7)	# 164859-164865
    sprite('ma000_07', 7)	# 164866-164872
    sprite('ma000_08', 7)	# 164873-164879
    sprite('ma000_09', 7)	# 164880-164886
    sprite('ma000_10', 7)	# 164887-164893
    sprite('ma000_11', 7)	# 164894-164900
    gotoLabel(141)
    label(142)
    sprite('ma615_00', 6)	# 164901-164906
    sprite('ma615_01', 6)	# 164907-164912
    sprite('ma615_02', 9)	# 164913-164921
    sprite('ma615_03', 9)	# 164922-164930
    sprite('ma615_04', 9)	# 164931-164939
    SFX_1('bma701pce')
    sprite('ma615_05', 10)	# 164940-164949
    sprite('ma615_06', 9)	# 164950-164958
    sprite('ma615_02', 9)	# 164959-164967
    sprite('ma615_03', 9)	# 164968-164976
    sprite('ma615_04', 9)	# 164977-164985
    sprite('ma615_05', 10)	# 164986-164995
    sprite('ma615_06', 9)	# 164996-165004
    Unknown23018(1)
    label(143)
    sprite('ma615_02', 9)	# 165005-165013
    sprite('ma615_03', 9)	# 165014-165022
    sprite('ma615_04', 9)	# 165023-165031
    sprite('ma615_05', 10)	# 165032-165041
    sprite('ma615_06', 9)	# 165042-165050
    loopRest()
    gotoLabel(143)
    label(150)
    sprite('ma620_00', 7)	# 165051-165057
    SFX_1('bma700pmi')
    sprite('ma602_07', 7)	# 165058-165064
    sprite('ma602_08', 50)	# 165065-165114
    sprite('ma602_09', 6)	# 165115-165120
    sprite('ma602_10', 6)	# 165121-165126
    sprite('ma602_11', 6)	# 165127-165132
    sprite('ma602_12', 6)	# 165133-165138
    sprite('ma602_13', 10)	# 165139-165148
    sprite('ma602_12', 6)	# 165149-165154
    sprite('ma602_11', 6)	# 165155-165160
    sprite('ma602_10', 6)	# 165161-165166
    sprite('ma602_09', 6)	# 165167-165172
    label(151)
    sprite('ma602_08', 1)	# 165173-165173
    if SLOT_97:
        _gotolabel(151)
    sprite('ma602_08', 32767)	# 165174-197940
    Unknown21007(24, 40)
    Unknown21011(180)
    label(160)
    sprite('ma615_00', 6)	# 197941-197946
    sprite('ma615_01', 6)	# 197947-197952
    sprite('ma615_02', 9)	# 197953-197961
    sprite('ma615_03', 9)	# 197962-197970
    sprite('ma615_04', 9)	# 197971-197979
    SFX_1('bma700rrb')
    sprite('ma615_05', 10)	# 197980-197989
    sprite('ma615_06', 9)	# 197990-197998
    sprite('ma615_02', 9)	# 197999-198007
    sprite('ma615_03', 9)	# 198008-198016
    sprite('ma615_04', 9)	# 198017-198025
    sprite('ma615_05', 10)	# 198026-198035
    sprite('ma615_06', 9)	# 198036-198044
    label(161)
    sprite('ma615_02', 9)	# 198045-198053
    sprite('ma615_03', 9)	# 198054-198062
    sprite('ma615_04', 9)	# 198063-198071
    sprite('ma615_05', 10)	# 198072-198081
    sprite('ma615_06', 9)	# 198082-198090
    loopRest()
    if SLOT_97:
        _gotolabel(161)
    sprite('ma615_02', 1)	# 198091-198091
    Unknown21007(24, 40)
    Unknown21011(240)
    label(162)
    sprite('ma615_02', 9)	# 198092-198100
    sprite('ma615_03', 9)	# 198101-198109
    sprite('ma615_04', 9)	# 198110-198118
    sprite('ma615_05', 10)	# 198119-198128
    sprite('ma615_06', 9)	# 198129-198137
    loopRest()
    gotoLabel(162)
    label(170)
    sprite('ma610_00', 7)	# 198138-198144
    sprite('ma610_01', 8)	# 198145-198152
    sprite('ma610_02', 12)	# 198153-198164
    sprite('ma610_03', 6)	# 198165-198170
    sprite('ma610_04', 12)	# 198171-198182
    sprite('ma610_05', 6)	# 198183-198188
    sprite('ma610_06', 6)	# 198189-198194
    SFX_1('bma700uhy')
    label(171)
    sprite('ma610_06', 1)	# 198195-198195
    if SLOT_97:
        _gotolabel(171)
    sprite('ma610_06', 15)	# 198196-198210
    sprite('ma610_06', 32767)	# 198211-230977
    Unknown21007(24, 40)
    Unknown21011(180)
    label(180)
    sprite('ma610_00', 7)	# 230978-230984
    sprite('ma610_01', 8)	# 230985-230992
    sprite('ma610_02', 12)	# 230993-231004
    sprite('ma610_03', 6)	# 231005-231010
    sprite('ma610_04', 12)	# 231011-231022
    sprite('ma610_05', 6)	# 231023-231028
    sprite('ma610_06', 6)	# 231029-231034
    SFX_1('bma700biz')
    label(181)
    sprite('ma610_06', 1)	# 231035-231035
    if SLOT_97:
        _gotolabel(181)
    sprite('ma610_06', 32767)	# 231036-263802
    Unknown21007(24, 40)
    Unknown21011(180)
    label(190)
    sprite('ma000_00', 1)	# 263803-263803

    def upon_40():
        clearUponHandler(40)
        SFX_1('bma701ume')
        Unknown23018(1)
    label(191)
    sprite('ma000_00', 7)	# 263804-263810
    sprite('ma000_01', 7)	# 263811-263817
    sprite('ma000_02', 7)	# 263818-263824
    sprite('ma000_03', 7)	# 263825-263831
    sprite('ma000_04', 7)	# 263832-263838
    sprite('ma000_05', 7)	# 263839-263845
    sprite('ma000_06', 7)	# 263846-263852
    sprite('ma000_07', 7)	# 263853-263859
    sprite('ma000_08', 7)	# 263860-263866
    sprite('ma000_09', 7)	# 263867-263873
    sprite('ma000_10', 7)	# 263874-263880
    sprite('ma000_11', 7)	# 263881-263887
    gotoLabel(191)

@State
def CmnActLose():
    sprite('ma000_00', 6)	# 1-6
    sprite('ma001_01', 6)	# 7-12
    sprite('ma620_00', 6)	# 13-18
    SFX_0('008_swing_pole_2')
    sprite('ma203_00', 6)	# 19-24
    sprite('ma620_01', 6)	# 25-30
    sprite('ma620_02', 6)	# 31-36
    sprite('ma620_02ex1', 6)	# 37-42
    sprite('ma620_02ex2', 6)	# 43-48
    sprite('ma620_03', 6)	# 49-54
    if SLOT_158:
        Unknown7006('bma403_0', 100, 878800226, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ma620_04', 6)	# 55-60
    sprite('ma620_05', 6)	# 61-66
    sprite('ma620_05ex1', 32767)	# 67-32833
