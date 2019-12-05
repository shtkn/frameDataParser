@Subroutine
def CR_VAR_Reset():
    SLOT_5 = 0

    def upon_11():
        SLOT_5 = 1

    def upon_8():
        SLOT_4 = 0
        SLOT_5 = 0

    def upon_14():
        SLOT_4 = 0
        SLOT_5 = 0

@Subroutine
def NoelComboFirst():
    Unknown3029(1)
    Unknown3069(1)
    Unknown3071(4)
    Unknown3070(1)
    Unknown3074('00000000000000000000000014000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3072('ff000000200000002000000020000000')
    Unknown3073('500000000a0000000a0000000a000000')
    Unknown3076(1010)
    Unknown3077(1010)
    SLOT_4 = 5
    callSubroutine('CR_VAR_Reset')

@Subroutine
def NoelComboHasei():
    Unknown3029(1)
    Unknown3069(1)
    Unknown3071(4)
    Unknown3070(1)
    Unknown3074('00000000000000000000000014000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3072('ff000000200000002000000020000000')
    Unknown3073('500000000a0000000a0000000a000000')
    Unknown3076(1010)
    Unknown3077(1010)
    callSubroutine('ComboVoice')
    SLOT_4 = (SLOT_4 + (-1))
    callSubroutine('CR_VAR_Reset')

@Subroutine
def NoelComboFinish():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(6)
    Unknown3070(2)
    Unknown3074('00000000000000000000000080000000')
    Unknown3075('00000000000000002000000040000000')
    Unknown3072('ff000000200000002000000020000000')
    Unknown3073('500000000a0000000a0000000a000000')
    Unknown3076(1010)
    Unknown3077(1010)
    JumpCancel_(0)
    Unknown3069(1)
    Unknown3074('00000000000000000000000014000000')
    Unknown3075('00000000000000000000000000000000')
    SLOT_4 = (SLOT_4 + (-1))
    callSubroutine('CR_VAR_Reset')

@Subroutine
def NoelComboDeriveInputBegin():
    if (SLOT_4 == 5):
        Unknown14070('con5A_1st')
    if (SLOT_4 == 4):
        Unknown14070('con5A_2nd')
    if (SLOT_4 == 3):
        Unknown14070('con5A_3rd')
    if (SLOT_4 == 2):
        Unknown14070('con5A_4th')
    if (SLOT_4 == 1):
        Unknown14070('con_Finish')
    if (SLOT_4 > 1):
        Unknown14070('con5B_Middle')
        Unknown14070('con2B_Low')
        Unknown14070('con2B_Low_Easy')
        Unknown14070('con5C_Middle')
        Unknown14070('con2C_Low')
        Unknown14070('con2C_Low_Easy')
    Unknown14070('InvincibleAttack_Derive')
    Unknown14070('Special236A_Derive')
    Unknown14070('Special236B_Derive')
    Unknown14070('SpecialThrow_Derive')
    Unknown14070('FlashHaider_Derive')
    Unknown14070('BloomTrigger_Derive')
    Unknown14070('AssaultThrough_Derive')

@Subroutine
def NoelComboDeriveTimingBegin():
    if (SLOT_4 == 5):
        Unknown14072('con5A_1st')
    if (SLOT_4 == 4):
        Unknown14072('con5A_2nd')
    if (SLOT_4 == 3):
        Unknown14072('con5A_3rd')
    if (SLOT_4 == 2):
        Unknown14072('con5A_4th')
    if (SLOT_4 == 1):
        Unknown14072('con_Finish')
    if (SLOT_4 > 1):
        Unknown14072('con5B_Middle')
        Unknown14072('con2B_Low')
        Unknown14072('con2B_Low_Easy')
        Unknown14072('con5C_Middle')
        Unknown14072('con2C_Low')
        Unknown14072('con2C_Low_Easy')
    Unknown14072('InvincibleAttack_Derive')
    Unknown14072('Special236A_Derive')
    Unknown14072('Special236B_Derive')
    Unknown14072('SpecialThrow_Derive')
    Unknown14072('FlashHaider_Derive')
    Unknown14072('BloomTrigger_Derive')
    Unknown14072('AssaultThrough_Derive')

@Subroutine
def NoelComboDeriveClear():
    if (SLOT_4 == 5):
        Unknown14074('con5A_1st')
    if (SLOT_4 == 4):
        Unknown14074('con5A_2nd')
    if (SLOT_4 == 3):
        Unknown14074('con5A_3rd')
    if (SLOT_4 == 2):
        Unknown14074('con5A_4th')
    if (SLOT_4 == 1):
        Unknown14074('con_Finish')
    if (SLOT_4 > 1):
        Unknown14074('con5B_Middle')
        Unknown14074('con2B_Low')
        Unknown14074('con2B_Low_Easy')
        Unknown14074('con5C_Middle')
        Unknown14074('con2C_Low')
        Unknown14074('con2C_Low_Easy')
        Unknown14074('InvincibleAttack_Derive')
        Unknown14074('Special236A_Derive')
        Unknown14074('Special236B_Derive')
        Unknown14074('SpecialThrow_Derive')
        Unknown14074('FlashHaider_Derive')
        Unknown14074('BloomTrigger_Derive')
        Unknown14074('AssaultThrough_Derive')

@Subroutine
def ComboVoice():
    if (SLOT_4 == 2):
        tag_voice(0, 'bno310_0', 'bno310_1', '', '')
    if (SLOT_4 == 3):
        tag_voice(0, 'bno323_0', 'bno323_1', '', '')
    if (SLOT_4 == 4):
        tag_voice(0, 'bno309_0', 'bno309_1', '', '')
    if (SLOT_4 == 5):
        tag_voice(1, 'bno308_0', 'bno308_1', '', '')

@Subroutine
def SpecialBeginCancel():
    if SLOT_4:
        Unknown30068(1)
        SLOT_4 = 0
        if SLOT_5:
            Unknown30068(0)
            SLOT_5 = 0

@Subroutine
def PreInit():
    Unknown12019('626e6f00000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFInitialVelocity(20000)
    DashFMaxVelocity(30000)
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
    MoveMaxChainRepeat(3)
    Unknown14015(0, 400000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 300000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 300000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 300000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown14015(0, 300000, -100000, 100000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(1)
    Unknown15021(2000)
    Unknown14015(0, 300000, -100000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown14015(50000, 480000, -200000, 200000, 900, 50)
    Unknown15012(2000)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14015(0, 420000, -200000, 300000, 1200, 30)
    Move_EndRegister()
    Move_Register('NmlAtk4B', 0x18)
    Unknown14015(-50000, 300000, -200000, 500000, 500, 30)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(300000, 500000, 0, 300000, 1000, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 400000, -300000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_2nd', 0x10)
    Unknown14005(1)
    Unknown14015(0, 450000, -300000, 50000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(50000, 300000, -200000, 100000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(50000, 300000, -100000, 200000, 700, 30)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C_2nd', 0x1)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown14015(50000, 300000, -100000, 200000, 400, 0)
    Move_EndRegister()
    Move_Register('con5A_1st', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 300000, -200000, 250000, 5000, 1000)
    Move_EndRegister()
    Move_Register('con5A_2nd', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 370000, -200000, 250000, 5000, 1000)
    Move_EndRegister()
    Move_Register('con5A_3rd', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 370000, -200000, 250000, 5000, 1000)
    Move_EndRegister()
    Move_Register('con5A_4th', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 600000, -200000, 250000, 5000, 1000)
    Move_EndRegister()
    Move_Register('con_Finish', 0x1)
    Unknown14005(1)
    Move_Input_(0xed)
    Unknown14015(0, 450000, -200000, 250000, 5000, 1000)
    Move_EndRegister()
    Move_Register('con2B_Low_Easy', 0x1)
    Unknown14013('con2B_Low')
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('con5B_Middle', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 800000, -200000, 250000, 8000, 250)
    Move_EndRegister()
    Move_Register('con2B_Low', 0x1)
    Unknown14005(1)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 650000, -200000, 400000, 8000, 250)
    Move_EndRegister()
    Move_Register('con2C_Low_Easy', 0x1)
    Unknown14013('con2C_Low')
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('con5C_Middle', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown15008()
    Unknown14015(0, 200000, -200000, 150000, 8000, 250)
    Move_EndRegister()
    Move_Register('con2C_Low', 0x1)
    Unknown14005(1)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_C)
    Unknown15009()
    Unknown14015(0, 350000, -200000, 100000, 8000, 250)
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
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('Special236A', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x2000)
    Unknown14015(400000, 800000, -200000, 100000, 250, 5)
    Move_EndRegister()
    Move_Register('Special236B', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x2000)
    Unknown14015(800000, 1200000, -200000, 100000, 300, 5)
    Move_EndRegister()
    Move_Register('SpecialThrow', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x2000)
    Unknown15009()
    Unknown14015(100000, 300000, -100000, 150000, 300, 0)
    Move_EndRegister()
    Move_Register('FlashHaider', INPUT_SPECIALMOVE)
    Unknown15016(1, 1, 360)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(100000, 400000, -200000, 100000, 750, 10)
    Move_EndRegister()
    Move_Register('BloomTrigger', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(0, 500000, -100000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('AssaultThrough', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(-300000, 300000, -200000, 250000, 300, 5)
    Move_EndRegister()
    Move_Register('InvincibleAttack_Derive', INPUT_SPECIALMOVE)
    Unknown14013('CmnActInvincibleAttack')
    Move_Input_(0xdf)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('Special236A_Derive', INPUT_SPECIALMOVE)
    Unknown14013('Special236A')
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('Special236B_Derive', INPUT_SPECIALMOVE)
    Unknown14013('Special236B')
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('SpecialThrow_Derive', INPUT_SPECIALMOVE)
    Unknown14013('SpecialThrow')
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('FlashHaider_Derive', INPUT_SPECIALMOVE)
    Unknown14013('FlashHaider')
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('BloomTrigger_Derive', INPUT_SPECIALMOVE)
    Unknown14013('BloomTrigger')
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AssaultThrough_Derive', INPUT_SPECIALMOVE)
    Unknown14013('AssaultThrough')
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -100000, 350000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(2000)
    Unknown15013(5000)
    Unknown14015(0, 300000, -100000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShotOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15014(2000)
    Unknown15013(5000)
    Unknown14015(0, 300000, -100000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAirShot', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(300000, 550000, -600000, -200000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateAirShotOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(300000, 550000, -600000, -200000, 1000, 0)
    Move_EndRegister()
    Move_Register('UltimateShot_Derive', 0x68)
    Unknown14013('UltimateShot')
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('UltimateShotOD_Derive', 0x68)
    Unknown14013('UltimateShotOD')
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk5B', 'con5A_1st', 10000000)
    Unknown15024('NmlAtk2B', 'con5A_1st', 10000000)
    Unknown15024('NmlAtk4B', 'con5A_1st', 10000000)
    Unknown15024('con5A_1st', 'con5A_2nd', 10000000)
    Unknown15024('con5A_2nd', 'con5A_3rd', 10000000)
    Unknown15024('con5A_3rd', 'con5A_4th', 10000000)
    Unknown15024('con5A_4th', 'con_Finish', 10000000)
    Unknown15024('NmlAtk5B', 'con5B_Middle', 10000000)
    Unknown15024('NmlAtk2B', 'con5B_Middle', 10000000)
    Unknown15024('NmlAtk4B', 'con5B_Middle', 10000000)
    Unknown15024('con5B_Middle', 'con2B_Low', 10000000)
    Unknown15024('con2B_Low', 'con5B_Middle', 10000000)
    Unknown15024('con5B_Middle', 'con_Finish', 10000000)
    Unknown15024('con2B_Low', 'con_Finish', 10000000)
    Unknown15024('NmlAtk5B', 'con2C_Low', 10000000)
    Unknown15024('NmlAtk2B', 'con2C_Low', 10000000)
    Unknown15024('NmlAtk4B', 'con2C_Low', 10000000)
    Unknown15024('con5C_Middle', 'con2C_Low', 10000000)
    Unknown15024('con2C_Low', 'con5C_Middle', 10000000)
    Unknown15024('con5C_Middle', 'con_Finish', 10000000)
    Unknown15024('con2C_Low', 'con_Finish', 10000000)
    Unknown15024('NmlAtk2C', 'FlashHaider', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A_2nd', 10000000)
    Unknown15024('NmlAtkAIR5A_2nd', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5C', 'NmlAtkAIR5C_2nd', 10000000)
    Unknown15024('ThrowExe', 'SpecialThrow', 10000000)
    Unknown15024('BackThrowExe', 'SpecialThrow', 10000000)
    Unknown12018(0, 'no062_01')
    Unknown12018(1, 'no062_04')
    Unknown12018(2, 'no062_05')
    Unknown12018(3, 'no062_06')
    Unknown12018(4, 'no062_07')
    Unknown12018(5, 'no062_08')
    Unknown12018(6, 'no062_10')
    Unknown12018(7, 'no041_02')
    Unknown12018(8, 'no040_02')
    Unknown12018(9, 'no045_02')
    Unknown12018(10, 'no060_00')
    Unknown12018(11, 'no060_01')
    Unknown12018(12, 'no060_02')
    Unknown12018(13, 'no060_04')
    Unknown12018(14, 'no060_06')
    Unknown12018(15, 'no060_13')
    Unknown12018(16, 'no050_00')
    Unknown12018(17, 'no052_00')
    Unknown12018(18, 'no054_00')
    Unknown12018(19, 'no000_00')
    Unknown12018(20, 'no000_00')
    Unknown12018(25, 'no063_00')
    Unknown12018(26, 'no063_01')
    Unknown12018(27, 'no063_03')
    Unknown12018(28, 'no063_05')
    Unknown12018(29, 'no063_10')
    Unknown12018(24, 'no073_01')
    Unknown7010(0, 'bno000')
    Unknown7010(1, 'bno001')
    Unknown7010(2, 'bno002')
    Unknown7010(3, 'bno003')
    Unknown7010(4, 'bno004')
    Unknown7010(5, 'bno005')
    Unknown7010(6, 'bno006')
    Unknown7010(7, 'bno007')
    Unknown7010(8, 'bno008')
    Unknown7010(9, 'bno009')
    Unknown7010(10, 'bno010')
    Unknown7010(15, 'bno015')
    Unknown7010(16, 'bno016')
    Unknown7010(17, 'bno017')
    Unknown7010(18, 'bno018')
    Unknown7010(19, 'bno019')
    Unknown7010(20, 'bno020')
    Unknown7010(21, 'bno021')
    Unknown7010(22, 'bno022')
    Unknown7010(23, 'bno023')
    Unknown7010(24, 'bno024')
    Unknown7010(25, 'bno025')
    Unknown7010(28, 'bno028')
    Unknown7010(29, 'bno029')
    Unknown7010(30, 'bno030')
    Unknown7010(31, 'bno031')
    Unknown7010(32, 'bno032')
    Unknown7010(33, 'bno033')
    Unknown7010(34, 'bno034')
    Unknown7010(35, 'bno035')
    Unknown7010(36, 'bno036')
    Unknown7010(37, 'bno037')
    Unknown7010(39, 'bno039')
    Unknown7010(42, 'bno042')
    Unknown7010(43, 'bno043')
    Unknown7010(44, 'bno044')
    Unknown7010(45, 'bno045')
    Unknown7010(46, 'bno046')
    Unknown7010(47, 'bno047')
    Unknown7010(48, 'bno048')
    Unknown7010(49, 'bno049')
    Unknown7010(50, 'bno050')
    Unknown7010(52, 'bno052')
    Unknown7010(53, 'bno053')
    Unknown7010(54, 'bno100_0')
    Unknown7010(55, 'bno100_1')
    Unknown7010(56, 'bno100_2')
    Unknown7010(63, 'bno101_0')
    Unknown7010(64, 'bno101_1')
    Unknown7010(65, 'bno101_2')
    Unknown7010(57, 'bno102_0')
    Unknown7010(58, 'bno102_1')
    Unknown7010(59, 'bno102_2')
    Unknown7010(66, 'bno103_0')
    Unknown7010(67, 'bno103_1')
    Unknown7010(68, 'bno103_2')
    Unknown7010(60, 'bno104_0')
    Unknown7010(61, 'bno104_1')
    Unknown7010(62, 'bno104_2')
    Unknown7010(69, 'bno105_0')
    Unknown7010(70, 'bno105_1')
    Unknown7010(71, 'bno105_2')
    Unknown7010(72, 'bno150')
    Unknown7010(73, 'bno151')
    Unknown7010(74, 'bno152')
    Unknown7010(85, 'bno153')
    Unknown7010(87, 'bno154')
    Unknown7010(88, 'bno155')
    Unknown7010(96, 'bno161_0')
    Unknown7010(97, 'bno161_1')
    Unknown7010(92, 'bno162_0')
    Unknown7010(93, 'bno162_1')
    Unknown7010(98, 'bno163_0')
    Unknown7010(99, 'bno163_1')
    Unknown7010(100, 'bno164_0')
    Unknown7010(101, 'bno164_1')
    Unknown7010(105, 'bno165_0')
    Unknown7010(106, 'bno165_1')
    Unknown7010(102, 'bno166_0')
    Unknown7010(103, 'bno166_1')
    Unknown7010(90, 'bno167_0')
    Unknown7010(91, 'bno167_1')
    Unknown7010(107, 'bno168_0')
    Unknown7010(108, 'bno168_1')
    Unknown7010(110, 'bno169_0')
    Unknown7010(111, 'bno169_1')
    Unknown7010(112, 'bno159_0')
    Unknown7010(113, 'bno159_1')
    Unknown7010(94, 'bno400_0')
    Unknown7010(95, 'bno400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f744f44000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746553686f744f44000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@State
def CmnActStand():
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    if random_(2, 0, 80):
        gotoLabel(0)
    sprite('no001_00', 6)	# 57-62
    SLOT_88 = 960
    sprite('no001_01', 6)	# 63-68
    sprite('no001_02', 6)	# 69-74
    sprite('no001_03', 6)	# 75-80
    SFX_1('bno000')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no001_04', 6)	# 81-86
    sprite('no001_05', 6)	# 87-92
    sprite('no001_06', 6)	# 93-98
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('no003_00', 3)	# 1-3
    sprite('no003_01', 3)	# 4-6
    sprite('no003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('no010_00', 4)	# 1-4
    sprite('no010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('no010_02', 7)	# 1-7
    sprite('no010_03', 7)	# 8-14
    sprite('no010_04', 7)	# 15-21
    sprite('no010_05', 7)	# 22-28
    sprite('no010_06', 7)	# 29-35
    sprite('no010_07', 7)	# 36-42
    sprite('no010_08', 7)	# 43-49
    sprite('no010_09', 7)	# 50-56
    sprite('no010_10', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('no013_00', 3)	# 1-3
    sprite('no013_01', 3)	# 4-6
    sprite('no013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('no010_01', 4)	# 1-4
    sprite('no010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('no023_00', 2)	# 1-2
    sprite('no023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    if SLOT_16:
        gotoLabel(1)
    if SLOT_15:
        gotoLabel(2)
    label(0)
    sprite('no020_00', 3)	# 1-3
    sprite('no020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no020_00', 2)	# 7-8
    sprite('no020_01', 2)	# 9-10
    sprite('no021_00', 5)	# 11-15
    sprite('no021_01', 3)	# 16-18
    sprite('no021_02', 3)	# 19-21
    sprite('no021_03', 3)	# 22-24
    Unknown51(1)
    label(2)
    sprite('no020_00', 2)	# 25-26
    sprite('no020_01', 2)	# 27-28
    sprite('no022_00', 5)	# 29-33
    sprite('no022_01', 3)	# 34-36
    sprite('no022_02', 3)	# 37-39
    sprite('no022_03', 3)	# 40-42
    Unknown51(1)

@State
def CmnActJumpUpperEnd():
    if SLOT_16:
        gotoLabel(1)
    if SLOT_15:
        gotoLabel(2)
    sprite('no020_02', 3)	# 1-3
    sprite('no020_03', 3)	# 4-6
    loopRest()
    ExitState()
    label(1)
    sprite('no021_03', 2)	# 7-8
    sprite('no021_04', 2)	# 9-10
    loopRest()
    ExitState()
    label(2)
    sprite('no022_03', 2)	# 11-12
    sprite('no022_04', 2)	# 13-14
    loopRest()
    ExitState()

@State
def CmnActJumpDown():
    if SLOT_16:
        gotoLabel(1)
    if SLOT_15:
        gotoLabel(2)
    sprite('no020_03', 3)	# 1-3
    sprite('no020_04', 3)	# 4-6
    sprite('no020_05', 3)	# 7-9
    label(0)
    sprite('no020_06', 3)	# 10-12
    sprite('no020_07', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no021_04', 1)	# 16-16
    sprite('no021_05', 3)	# 17-19
    sprite('no021_06', 3)	# 20-22
    label(5)
    sprite('no021_08', 3)	# 23-25
    sprite('no021_09', 3)	# 26-28
    loopRest()
    gotoLabel(5)
    label(2)
    sprite('no022_04', 1)	# 29-29
    sprite('no022_05', 3)	# 30-32
    sprite('no022_06', 3)	# 33-35
    label(6)
    sprite('no022_07', 3)	# 36-38
    sprite('no022_08', 3)	# 39-41
    loopRest()
    gotoLabel(6)

@State
def CmnActJumpLanding():
    sprite('no024_01', 3)	# 1-3
    sprite('no024_02', 3)	# 4-6
    sprite('no024_03', 3)	# 7-9
    sprite('no024_04', 3)	# 10-12

@State
def CmnActLandingStiffLoop():
    sprite('no024_01', 3)	# 1-3
    sprite('no024_02', 32767)	# 4-32770

@State
def CmnActLandingStiffEnd():
    sprite('no024_03', 3)	# 1-3
    sprite('no024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('no030_00', 1)	# 1-1
    sprite('no030_01', 1)	# 2-2
    label(0)
    sprite('no030_02', 5)	# 3-7
    sprite('no030_03', 5)	# 8-12
    sprite('no030_04', 5)	# 13-17
    sprite('no030_05', 5)	# 18-22
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no030_06', 3)	# 23-25
    sprite('no030_07', 3)	# 26-28
    sprite('no030_08', 5)	# 29-33
    sprite('no030_09', 5)	# 34-38
    sprite('no030_10', 3)	# 39-41
    sprite('no030_11', 3)	# 42-44
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('no031_00', 5)	# 1-5
    sprite('no031_01', 5)	# 6-10
    label(0)
    sprite('no031_02', 5)	# 11-15
    sprite('no031_03', 5)	# 16-20
    sprite('no031_04', 5)	# 21-25
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no031_05', 5)	# 26-30
    sprite('no031_06', 5)	# 31-35
    sprite('no031_07', 5)	# 36-40
    sprite('no031_08', 5)	# 41-45
    sprite('no031_09', 5)	# 46-50
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no031_10', 5)	# 51-55
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('no030_00', 2)	# 1-2
    sprite('no030_01', 2)	# 3-4
    sprite('no032_00', 2)	# 5-6
    sprite('no032_01', 2)	# 7-8
    label(0)
    sprite('no032_02', 4)	# 9-12
    sprite('no032_03', 4)	# 13-16
    sprite('no032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 21-24
    sprite('no032_06', 4)	# 25-28
    sprite('no032_07', 4)	# 29-32
    sprite('no032_08', 4)	# 33-36
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 37-40
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('no032_10', 6)	# 1-6
    sprite('no032_11', 5)	# 7-11

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincibleFor(7)
        Unknown1084(1)
        sendToLabelUpon(2, 1)
        Unknown2004(1, 0)
        Unknown23076()
        Unknown23001(100, 0)
    sprite('no033_00', 1)	# 1-1
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no033_01', 2)	# 2-3
    physicsXImpulse(-18000)
    physicsYImpulse(4800)
    setGravity(800)
    sprite('no033_02', 2)	# 4-5
    sprite('no033_03', 2)	# 6-7
    sprite('no033_02', 2)	# 8-9
    sprite('no033_03', 2)	# 10-11
    sprite('no033_02', 2)	# 12-13
    sprite('no033_03', 2)	# 14-15
    label(1)
    clearUponHandler(2)
    sprite('no033_04', 1)	# 16-16
    Unknown1019(50)
    Unknown8000(100, 1, 1)
    sprite('no033_04', 3)	# 17-19
    physicsXImpulse(0)
    sprite('no033_05', 3)	# 20-22

@State
def CmnActBDashLanding():
    sprite('no000_00', 1)	# 1-1

@State
def CmnActAirFDash():
    sprite('no035_00', 3)	# 1-3
    label(0)
    sprite('no035_01', 3)	# 4-6
    sprite('no035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('no036_00', 3)	# 1-3
    label(0)
    sprite('no036_01', 3)	# 4-6
    sprite('no036_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('no050_00', 1)	# 1-1
    sprite('no050_01', 1)	# 2-2
    sprite('no050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('no050_01', 1)	# 1-1
    sprite('no050_02', 1)	# 2-2
    sprite('no050_01', 2)	# 3-4
    sprite('no050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('no050_02', 1)	# 1-1
    sprite('no050_03', 1)	# 2-2
    sprite('no050_02', 2)	# 3-4
    sprite('no050_01', 2)	# 5-6
    sprite('no050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('no050_03', 1)	# 1-1
    sprite('no050_04', 1)	# 2-2
    sprite('no050_03', 2)	# 3-4
    sprite('no050_02', 2)	# 5-6
    sprite('no050_01', 2)	# 7-8
    sprite('no050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('no050_04', 1)	# 1-1
    sprite('no050_05', 1)	# 2-2
    sprite('no050_04', 2)	# 3-4
    sprite('no050_03', 2)	# 5-6
    sprite('no050_02', 2)	# 7-8
    sprite('no050_01', 2)	# 9-10
    sprite('no050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('no052_00', 1)	# 1-1
    sprite('no052_01', 1)	# 2-2
    sprite('no052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('no052_01', 1)	# 1-1
    sprite('no052_02', 1)	# 2-2
    sprite('no052_01', 2)	# 3-4
    sprite('no052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('no052_02', 1)	# 1-1
    sprite('no052_03', 1)	# 2-2
    sprite('no052_02', 2)	# 3-4
    sprite('no052_01', 2)	# 5-6
    sprite('no052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('no052_03', 1)	# 1-1
    sprite('no052_04', 1)	# 2-2
    sprite('no052_03', 2)	# 3-4
    sprite('no052_02', 2)	# 5-6
    sprite('no052_01', 2)	# 7-8
    sprite('no052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('no052_04', 1)	# 1-1
    sprite('no052_05', 1)	# 2-2
    sprite('no052_04', 2)	# 3-4
    sprite('no052_03', 2)	# 5-6
    sprite('no052_02', 2)	# 7-8
    sprite('no052_01', 2)	# 9-10
    sprite('no052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('no054_00', 1)	# 1-1
    sprite('no054_01', 1)	# 2-2
    sprite('no054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('no054_01', 1)	# 1-1
    sprite('no054_02', 1)	# 2-2
    sprite('no054_01', 2)	# 3-4
    sprite('no054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('no054_02', 1)	# 1-1
    sprite('no054_03', 1)	# 2-2
    sprite('no054_02', 2)	# 3-4
    sprite('no054_01', 2)	# 5-6
    sprite('no054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('no054_03', 1)	# 1-1
    sprite('no054_04', 1)	# 2-2
    sprite('no054_03', 2)	# 3-4
    sprite('no054_02', 2)	# 5-6
    sprite('no054_01', 2)	# 7-8
    sprite('no054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('no054_04', 1)	# 1-1
    sprite('no054_05', 1)	# 2-2
    sprite('no054_04', 2)	# 3-4
    sprite('no054_03', 2)	# 5-6
    sprite('no054_02', 2)	# 7-8
    sprite('no054_01', 2)	# 9-10
    sprite('no054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('no060_00', 4)	# 1-4
    sprite('no060_01', 4)	# 5-8

@State
def CmnActBDownUpperEnd():
    sprite('no062_04', 3)	# 1-3
    sprite('no062_05', 3)	# 4-6

@State
def CmnActBDownDown():
    sprite('no062_06', 3)	# 1-3
    sprite('no062_07', 3)	# 4-6
    sprite('no062_08', 3)	# 7-9
    sprite('no062_09', 3)	# 10-12
    label(0)
    sprite('no062_10', 3)	# 13-15
    sprite('no062_11', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('no060_06', 3)	# 1-3

@State
def CmnActBDownBound():
    sprite('no060_07', 3)	# 1-3
    sprite('no060_08', 3)	# 4-6
    sprite('no060_09', 3)	# 7-9
    sprite('no060_10', 3)	# 10-12
    sprite('no060_11', 3)	# 13-15
    sprite('no060_12', 3)	# 16-18

@State
def CmnActBDownLoop():
    label(0)
    sprite('no060_13', 1)	# 1-1
    loopRest()
    gotoLabel(0)

@State
def CmnActBDown2Stand():
    sprite('no061_00', 3)	# 1-3
    sprite('no061_01', 3)	# 4-6
    sprite('no061_02', 3)	# 7-9
    sprite('no061_03', 3)	# 10-12
    sprite('no061_04', 3)	# 13-15
    sprite('no061_05', 3)	# 16-18
    sprite('no061_06', 2)	# 19-20
    sprite('no061_07', 2)	# 21-22
    sprite('no061_08', 2)	# 23-24
    label(0)
    sprite('no061_09', 2)	# 25-26
    sprite('no061_10', 2)	# 27-28
    sprite('no061_11', 2)	# 29-30

@State
def CmnActFDownUpper():
    sprite('no063_00', 3)	# 1-3
    sprite('no063_01', 3)	# 4-6

@State
def CmnActFDownUpperEnd():
    sprite('no063_02', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('no063_03', 3)	# 1-3
    sprite('no063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('no063_05', 3)	# 1-3

@State
def CmnActFDownBound():
    sprite('no063_06', 3)	# 1-3
    sprite('no063_07', 3)	# 4-6
    sprite('no063_08', 3)	# 7-9
    sprite('no063_09', 3)	# 10-12

@State
def CmnActFDownLoop():
    label(0)
    sprite('no063_10', 1)	# 1-1
    loopRest()
    gotoLabel(0)

@State
def CmnActFDown2Stand():
    sprite('no064_00', 2)	# 1-2
    sprite('no064_01', 2)	# 3-4
    sprite('no064_02', 2)	# 5-6
    sprite('no064_03', 2)	# 7-8
    sprite('no064_04', 2)	# 9-10
    sprite('no064_05', 2)	# 11-12
    sprite('no064_06', 2)	# 13-14
    sprite('no064_07', 2)	# 15-16
    sprite('no064_08', 2)	# 17-18

@State
def CmnActVDownUpper():
    sprite('no062_00', 3)	# 1-3
    label(0)
    sprite('no062_01', 3)	# 4-6
    sprite('no062_02', 3)	# 7-9
    sprite('no062_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('no062_04', 3)	# 1-3
    sprite('no062_05', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('no062_06', 3)	# 1-3
    sprite('no062_07', 3)	# 4-6
    sprite('no062_08', 3)	# 7-9
    sprite('no062_09', 3)	# 10-12
    label(0)
    sprite('no062_10', 3)	# 13-15
    sprite('no062_11', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('no062_12', 3)	# 1-3

@State
def CmnActBlowoff():
    sprite('no072_00', 3)	# 1-3
    sprite('no072_01', 3)	# 4-6
    sprite('no072_02', 3)	# 7-9
    label(0)
    sprite('no072_01', 3)	# 10-12
    sprite('no072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('no074_00', 3)	# 1-3
    sprite('no074_01', 3)	# 4-6
    sprite('no074_02', 3)	# 7-9
    sprite('no074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('no082_00', 2)	# 1-2
    sprite('no082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('no071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('no073_00', 3)	# 1-3
    sprite('no073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('no073_02', 3)	# 1-3
    label(0)
    sprite('no073_03', 3)	# 4-6
    sprite('no073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('no070_00', 3)	# 1-3
    sprite('no070_01', 3)	# 4-6
    sprite('no070_02', 3)	# 7-9
    sprite('no070_03', 3)	# 10-12
    sprite('no070_04', 3)	# 13-15
    sprite('no070_05', 3)	# 16-18
    sprite('no070_06', 3)	# 19-21

@State
def CmnActStaggerDown():
    sprite('no070_07', 6)	# 1-6
    sprite('no070_08', 6)	# 7-12
    sprite('no070_09', 4)	# 13-16
    sprite('no070_10', 4)	# 17-20
    sprite('no070_11', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('no070_12', 4)	# 1-4
    sprite('no070_13', 4)	# 5-8

@State
def CmnActUkemiAirF():
    sprite('no113_00', 3)	# 1-3
    sprite('no113_01', 3)	# 4-6
    sprite('no113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('no113_00', 3)	# 1-3
    sprite('no113_01', 3)	# 4-6
    sprite('no113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('no113_00', 3)	# 1-3
    sprite('no113_01', 3)	# 4-6
    sprite('no113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('no112_00', 3)	# 1-3
    sprite('no112_01', 3)	# 4-6
    sprite('no112_02', 3)	# 7-9
    sprite('no112_03', 3)	# 10-12
    sprite('no112_04', 3)	# 13-15
    sprite('no112_05', 3)	# 16-18
    sprite('no112_06', 3)	# 19-21
    sprite('no112_07', 3)	# 22-24
    sprite('no112_08', 3)	# 25-27

@State
def CmnActUkemiLandB():
    sprite('no112_00', 3)	# 1-3
    sprite('no112_01', 3)	# 4-6
    sprite('no112_02', 3)	# 7-9
    sprite('no112_03', 3)	# 10-12
    sprite('no112_04', 3)	# 13-15
    sprite('no112_05', 3)	# 16-18
    sprite('no112_06', 3)	# 19-21
    sprite('no112_07', 3)	# 22-24
    sprite('no112_08', 3)	# 25-27

@State
def CmnActUkemiLandN():
    sprite('no112_00', 3)	# 1-3
    sprite('no112_01', 3)	# 4-6
    sprite('no112_02', 3)	# 7-9
    sprite('no112_03', 3)	# 10-12
    sprite('no112_04', 3)	# 13-15
    sprite('no112_05', 3)	# 16-18
    sprite('no112_06', 3)	# 19-21
    sprite('no112_07', 3)	# 22-24
    sprite('no112_08', 3)	# 25-27

@State
def CmnActUkemiLandNLanding():
    sprite('no024_01', 3)	# 1-3
    sprite('no024_02', 3)	# 4-6
    sprite('no024_03', 3)	# 7-9
    sprite('no024_04', 3)	# 10-12

@State
def CmnActMidGuardPre():
    sprite('no040_00', 3)	# 1-3
    sprite('no040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('no040_02', 5)	# 1-5	 **attackbox here**
    sprite('no040_03', 5)	# 6-10	 **attackbox here**
    sprite('no040_02ex00', 5)	# 11-15
    sprite('no040_03ex00', 5)	# 16-20
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('no040_01', 3)	# 1-3
    sprite('no040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('no040_04', 3)	# 1-3
    label(0)
    sprite('no040_02', 5)	# 4-8	 **attackbox here**
    sprite('no040_03', 5)	# 9-13	 **attackbox here**
    sprite('no040_02ex00', 5)	# 14-18
    sprite('no040_03ex00', 5)	# 19-23
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('no040_01', 3)	# 1-3
    sprite('no040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('no041_00', 3)	# 1-3
    sprite('no041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('no041_02', 5)	# 1-5	 **attackbox here**
    sprite('no041_03', 5)	# 6-10	 **attackbox here**
    sprite('no041_02ex00', 5)	# 11-15	 **attackbox here**
    sprite('no041_03ex00', 5)	# 16-20	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('no041_01', 3)	# 1-3
    sprite('no041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('no041_04', 3)	# 1-3
    label(0)
    sprite('no041_02', 5)	# 4-8	 **attackbox here**
    sprite('no041_03', 5)	# 9-13	 **attackbox here**
    sprite('no041_02ex00', 5)	# 14-18	 **attackbox here**
    sprite('no041_03ex00', 5)	# 19-23	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('no041_01', 3)	# 1-3
    sprite('no041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('no043_00', 3)	# 1-3
    sprite('no043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('no043_02', 5)	# 1-5	 **attackbox here**
    sprite('no043_03', 5)	# 6-10	 **attackbox here**
    sprite('no043_02ex00', 5)	# 11-15	 **attackbox here**
    sprite('no043_03ex00', 5)	# 16-20	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('no043_01', 3)	# 1-3
    sprite('no043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('no043_04', 3)	# 1-3
    label(0)
    sprite('no043_02', 5)	# 4-8	 **attackbox here**
    sprite('no043_03', 5)	# 9-13	 **attackbox here**
    sprite('no043_02ex00', 5)	# 14-18	 **attackbox here**
    sprite('no043_03ex00', 5)	# 19-23	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('no043_01', 3)	# 1-3
    sprite('no043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('no045_00', 3)	# 1-3
    sprite('no045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('no045_02', 5)	# 1-5	 **attackbox here**
    sprite('no045_03', 5)	# 6-10	 **attackbox here**
    sprite('no045_02ex00', 5)	# 11-15	 **attackbox here**
    sprite('no045_03ex00', 5)	# 16-20	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('no045_01', 3)	# 1-3
    sprite('no045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('no045_04', 3)	# 1-3
    label(0)
    sprite('no045_02', 5)	# 4-8	 **attackbox here**
    sprite('no045_03', 5)	# 9-13	 **attackbox here**
    sprite('no045_02ex00', 5)	# 14-18	 **attackbox here**
    sprite('no045_03ex00', 5)	# 19-23	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('no045_01', 3)	# 1-3
    sprite('no045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('no090_00', 2)	# 1-2
    sprite('no090_01', 2)	# 3-4
    sprite('no090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('no090_03', 3)	# 6-8
    sprite('no090_04', 3)	# 9-11
    sprite('no090_05', 2)	# 12-13
    sprite('no090_06', 2)	# 14-15
    sprite('no090_07', 2)	# 16-17

@State
def CmnActGuardBreakCrouch():
    sprite('no091_00', 2)	# 1-2
    sprite('no091_01', 2)	# 3-4
    sprite('no091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('no091_03', 3)	# 6-8
    sprite('no091_04', 3)	# 9-11
    sprite('no091_05', 2)	# 12-13
    sprite('no091_06', 2)	# 14-15
    sprite('no091_07', 2)	# 16-17

@State
def CmnActGuardBreakAir():
    sprite('no092_00', 2)	# 1-2
    sprite('no092_01', 2)	# 3-4
    sprite('no092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('no092_03', 3)	# 6-8
    sprite('no092_04', 3)	# 9-11
    sprite('no092_05', 2)	# 12-13
    sprite('no092_06', 2)	# 14-15
    sprite('no092_07', 2)	# 16-17

@State
def CmnActAirTurn():
    sprite('no025_00', 4)	# 1-4
    sprite('no025_01', 4)	# 5-8
    sprite('no025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('', 10)	# 1-10
    sprite('no040_01', 3)	# 11-13
    sprite('no040_00', 3)	# 14-16

@State
def CmnActLockReject():
    sprite('no287_06', 3)	# 1-3
    sprite('no287_07', 3)	# 4-6
    sprite('no287_08', 3)	# 7-9
    sprite('no287_09', 3)	# 10-12	 **attackbox here**
    sprite('no287_10', 3)	# 13-15
    sprite('no287_11', 3)	# 16-18
    sprite('no287_12', 3)	# 19-21
    sprite('no287_13', 3)	# 22-24

@State
def CmnActAirLockWait():
    sprite('no045_02', 1)	# 1-1	 **attackbox here**
    sprite('no045_01', 3)	# 2-4
    sprite('no045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('no322_00', 3)	# 1-3
    sprite('no322_01', 3)	# 4-6
    sprite('no322_02', 3)	# 7-9
    sprite('no322_03', 3)	# 10-12	 **attackbox here**
    GFX_0('EFF_SakuretsuNear', 0)
    sprite('no322_04', 3)	# 13-15
    sprite('no322_05', 3)	# 16-18

@State
def CmnActLandSpin():
    sprite('no071_00', 4)	# 1-4
    sprite('no071_01', 4)	# 5-8
    label(0)
    sprite('no071_02', 4)	# 9-12
    sprite('no071_03', 4)	# 13-16
    sprite('no071_04', 4)	# 17-20
    sprite('no071_05', 4)	# 21-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('no071_06', 4)	# 1-4
    sprite('no071_07', 4)	# 5-8
    sprite('no071_08', 4)	# 9-12
    sprite('no071_09', 4)	# 13-16

@State
def CmnActVertSpin():
    label(0)
    sprite('no071_02', 4)	# 1-4
    sprite('no071_03', 4)	# 5-8
    sprite('no071_04', 4)	# 9-12
    sprite('no071_05', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('no077_00', 2)	# 1-2
    sprite('no077_01', 2)	# 3-4
    sprite('no077_00ex01', 2)	# 5-6
    sprite('no077_01ex01', 2)	# 7-8
    sprite('no077_00ex02', 2)	# 9-10
    sprite('no077_01ex02', 2)	# 11-12
    sprite('no077_00ex03', 2)	# 13-14
    sprite('no077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('no077_02', 4)	# 1-4
    label(0)
    sprite('no077_03', 3)	# 5-7
    sprite('no077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('no077_05', 5)	# 1-5
    sprite('no077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('no060_04_low', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('no060_09', 3)	# 1-3
    sprite('no060_10', 2)	# 4-5
    sprite('no060_11', 2)	# 6-7
    sprite('no060_12', 2)	# 8-9

@State
def CmnActBurstBegin():
    sprite('no331_00', 2)	# 1-2
    label(0)
    sprite('no331_01add', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('no331_01', 3)	# 1-3
    label(0)
    sprite('no331_02', 2)	# 4-5
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('no331_03', 3)	# 1-3
    sprite('no331_04', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('no332_00', 3)	# 1-3
    label(0)
    sprite('no332_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('no332_02', 3)	# 1-3
    label(0)
    sprite('no332_03', 2)	# 4-5
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('no020_03', 3)	# 1-3
    sprite('no020_04', 3)	# 4-6
    sprite('no020_05', 3)	# 7-9
    label(0)
    sprite('no020_06', 3)	# 10-12
    sprite('no020_07', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('no334_00', 3)	# 1-3
    sprite('no334_01', 3)	# 4-6
    sprite('no334_02', 3)	# 7-9
    sprite('no334_03', 32767)	# 10-32776
    GFX_0('EMB_NO_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('no334_04', 3)	# 1-3
    label(0)
    sprite('no334_05', 3)	# 4-6
    sprite('no334_06', 3)	# 7-9
    sprite('no334_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('no334_08', 4)	# 1-4
    sprite('no334_09', 4)	# 5-8
    sprite('no334_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('no334_11', 3)	# 1-3
    sprite('no334_12', 3)	# 4-6
    sprite('no334_13', 3)	# 7-9
    sprite('no334_14', 32767)	# 10-32776
    GFX_0('EMB_NO_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('no334_15', 3)	# 1-3
    label(0)
    sprite('no334_05', 3)	# 4-6
    sprite('no334_06', 3)	# 7-9
    sprite('no334_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('no334_16', 2)	# 1-2
    sprite('no334_17', 2)	# 3-4
    sprite('no334_18', 2)	# 5-6
    sprite('no020_04', 3)	# 7-9
    sprite('no020_05', 3)	# 10-12
    label(0)
    sprite('no020_06', 4)	# 13-16
    sprite('no020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('no334_00', 3)	# 1-3
    sprite('no334_01', 3)	# 4-6
    sprite('no334_02', 3)	# 7-9
    sprite('no334_03', 32767)	# 10-32776
    GFX_0('EMB_NO_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('no334_04', 3)	# 1-3
    label(0)
    sprite('no334_05', 3)	# 4-6
    sprite('no334_06', 3)	# 7-9
    sprite('no334_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('no334_08', 4)	# 1-4
    sprite('no334_09', 4)	# 5-8
    sprite('no334_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('no334_11', 3)	# 1-3
    sprite('no334_12', 3)	# 4-6
    sprite('no334_13', 3)	# 7-9
    sprite('no334_14', 32767)	# 10-32776
    GFX_0('EMB_NO_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('no334_15', 3)	# 1-3
    label(0)
    sprite('no334_05', 3)	# 4-6
    sprite('no334_06', 3)	# 7-9
    sprite('no334_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('no334_16', 2)	# 1-2
    sprite('no334_17', 2)	# 3-4
    sprite('no334_18', 2)	# 5-6
    sprite('no020_04', 3)	# 7-9
    sprite('no020_05', 3)	# 10-12
    label(0)
    sprite('no020_06', 4)	# 13-16
    sprite('no020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('no332_00', 3)	# 1-3
    sprite('no331_01add', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('no331_01', 3)	# 1-3
    label(0)
    sprite('no331_02', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('keep', 4)	# 1-4
    sprite('no331_03', 3)	# 5-7
    sprite('no331_04', 3)	# 8-10

@State
def CmnActAirCrossChangeBegin():
    sprite('no332_00', 3)	# 1-3
    sprite('no332_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('no332_02', 3)	# 1-3
    label(0)
    sprite('no332_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('keep', 3)	# 1-3
    sprite('no020_03', 3)	# 4-6
    sprite('no020_04', 3)	# 7-9
    sprite('no020_05', 3)	# 10-12
    label(0)
    sprite('no020_06', 4)	# 13-16
    sprite('no020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

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
    sprite('no293_03', 2)	# 32-33
    SFX_0('016_explode_1')
    GFX_0('noef_293', 2)
    sprite('no293_04', 30)	# 34-63	 **attackbox here**
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    label(1)
    sprite('no293_04', 1)	# 64-64	 **attackbox here**
    sprite('no024_01', 5)	# 65-69
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('no024_02', 15)	# 70-84
    sprite('no024_03', 5)	# 85-89
    sprite('no024_04', 5)	# 90-94

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('no024_02', 4)	# 2-5
    sprite('no024_03', 5)	# 6-10
    sprite('no024_04', 5)	# 11-15
    sprite('no292_00', 3)	# 16-18
    sprite('no292_01', 4)	# 19-22
    sprite('no292_02', 4)	# 23-26
    SFX_3('nose_01')
    sprite('no292_03', 3)	# 27-29
    Unknown7009(2)
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_04', 4)	# 30-33
    sprite('no292_04', 1)	# 34-34
    SFX_0('016_explode_1')
    SFX_3('nose_00')
    sprite('no292_05ex02', 3)	# 35-37	 **attackbox here**
    GFX_0('noef_292', -1)
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 5000)
    sprite('no292_06', 4)	# 38-41	 **attackbox here**
    sprite('no292_07', 4)	# 42-45	 **attackbox here**
    StartMultihit()
    sprite('no292_08', 5)	# 46-50
    SFX_0('008_swing_pole_1')
    sprite('no292_09', 5)	# 51-55
    SFX_0('008_swing_pole_1')
    sprite('no292_10', 5)	# 56-60
    SFX_0('008_swing_pole_1')
    sprite('no292_11', 5)	# 61-65
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_12', 5)	# 66-70
    sprite('no292_13', 5)	# 71-75

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(12000)
        AirPushbackY(11000)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)

        def upon_STATE_END():
            Unknown1084(1)
    sprite('no201_00', 3)	# 1-3
    sprite('no201_01', 3)	# 4-6
    Unknown7009(1)
    sprite('no201_02', 2)	# 7-8
    sprite('no201_03', 3)	# 9-11	 **attackbox here**
    SFX_0('008_swing_pole_1')
    sprite('no201_04', 3)	# 12-14	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    Recovery()
    Unknown2063()
    sprite('no201_05', 4)	# 15-18
    sprite('no201_06', 4)	# 19-22
    sprite('no201_07', 4)	# 23-26
    sprite('no201_08', 4)	# 27-30

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        ProjectileDurabilityLvl(1)
        Unknown9018(1)
        PushbackX(18000)
        AirPushbackY(20000)
        hitstun(19)
        AirUntechableTime(21)
        AirHitstunAnimation(10)
        HitJumpCancel(1)
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('no290_00', 2)	# 1-2
    sprite('no290_01', 4)	# 3-6
    Unknown7009(2)
    SFX_3('nose_07')
    sprite('no290_02', 2)	# 7-8
    sprite('no290_03', 2)	# 9-10
    sprite('no290_04', 1)	# 11-11
    sprite('no290_05', 2)	# 12-13	 **attackbox here**
    ScreenShake(0, 5000)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    SFX_0('016_explode_1')
    GFX_0('BLT', 1)
    Unknown22032(0)
    sprite('no290_03', 4)	# 14-17
    SFX_3('nose_01')
    Recovery()
    Unknown2063()
    sprite('no290_02', 5)	# 18-22
    sprite('no290_01', 5)	# 23-27
    sprite('no402_06', 5)	# 28-32

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(1200)
        AirPushbackY(-60000)
        PushbackX(10000)
        Unknown9190(1)
        Unknown9118(40)
        AirPushbackX(6500)
        AirPushbackY(-35000)
        AirUntechableTime(40)
        AirHitstunAnimation(10)
        HitJumpCancel(1)
        HitOrBlockCancel('AN_NmlAtk5A_4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        Unknown2004(1, 0)
    sprite('no211_00', 2)	# 1-2
    teleportRelativeX(60000)
    sprite('no211_01', 2)	# 3-4
    teleportRelativeX(50000)
    Unknown7009(2)
    sprite('no211_02', 2)	# 5-6
    sprite('no211_03', 2)	# 7-8
    sprite('no211_04', 3)	# 9-11
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no211_05', 2)	# 12-13
    sprite('no211_06', 2)	# 14-15
    sprite('no211_07', 2)	# 16-17
    sprite('no211_08', 2)	# 18-19	 **attackbox here**
    SFX_0('004_swing_grap_1_1')
    sprite('no211_09', 3)	# 20-22	 **attackbox here**
    sprite('no211_10', 3)	# 23-25	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('no211_11', 3)	# 26-28	 **attackbox here**
    sprite('no211_12', 3)	# 29-31
    sprite('no211_13', 3)	# 32-34
    sprite('no211_14', 3)	# 35-37
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no211_15', 3)	# 38-40

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        ProjectileDurabilityLvl(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(35000)
        AirPushbackY(17000)
        YImpluseBeforeWallbounce(1600)
        AirUntechableTime(40)
        JumpCancel_(0)
        Unknown11044(1)
    sprite('no292_00', 2)	# 1-2
    Unknown7006('bno207_0', 100, 846163554, 828323632, 0, 0, 100, 846163554, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('no292_01', 2)	# 3-4
    sprite('no292_02', 2)	# 5-6
    SFX_3('nose_01')
    Unknown1047(10000)
    sprite('no292_03', 3)	# 7-9
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_04', 4)	# 10-13
    sprite('no292_04', 1)	# 14-14
    SFX_0('016_explode_1')
    SFX_3('nose_00')
    sprite('no292_05', 3)	# 15-17	 **attackbox here**
    Unknown1084(1)
    GFX_0('noef_292', -1)
    Unknown1047(-2000)
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 5000)
    Unknown30088(1)
    sprite('no292_06', 3)	# 18-20	 **attackbox here**
    Unknown2063()
    sprite('no292_07', 4)	# 21-24	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('no292_08', 4)	# 25-28
    SFX_0('008_swing_pole_1')
    sprite('no292_09', 4)	# 29-32
    SFX_0('008_swing_pole_1')
    sprite('no292_10', 4)	# 33-36
    SFX_0('008_swing_pole_1')
    sprite('no292_11', 3)	# 37-39
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_12', 2)	# 40-41
    sprite('no292_13', 2)	# 42-43

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('NoelComboFirst')
        Unknown2018(0, 50)
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        AirPushbackX(8000)
        AirPushbackY(9000)
        YImpluseBeforeWallbounce(1400)
        hitstun(30)
        AirUntechableTime(30)
        Unknown2004(1, 0)
        JumpCancel_(1)
        Unknown1112('')

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
    sprite('no203_00', 2)	# 1-2
    sprite('no203_01', 1)	# 3-3
    sprite('no203_01', 2)	# 4-5
    Unknown7006('bno109_1', 100, 829386338, 845101360, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_3('nose_07')
    SFX_0('001_airbackdash_0')
    sprite('no203_02', 3)	# 6-8
    sprite('no203_03', 3)	# 9-11
    callSubroutine('NoelComboDeriveInputBegin')
    physicsXImpulse(0)
    Unknown1028(0)
    sprite('no203_04', 3)	# 12-14
    sprite('no203_05', 2)	# 15-16
    Unknown2015(150)
    sprite('no203_06', 3)	# 17-19
    Unknown2015(200)
    sprite('no203_07', 3)	# 20-22
    ScreenShake(0, 5000)
    sprite('no203_08', 4)	# 23-26	 **attackbox here**
    physicsXImpulse(0)
    Unknown1028(0)
    SFX_3('nose_01')
    GFX_0('BLT', 0)
    SFX_0('016_explode_1')
    GFX_0('EFF_SakuretsuNear', 1)
    GFX_0('EFF_SakuretsuNear', 1)
    if SLOT_2:
        callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no203_08', 3)	# 27-29	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('no203_09', 2)	# 30-31	 **attackbox here**
    callSubroutine('NoelComboDeriveTimingBegin')
    StartMultihit()
    sprite('no203_10', 2)	# 32-33
    sprite('no203_10', 4)	# 34-37
    sprite('no203_11', 4)	# 38-41
    Unknown2015(150)
    Unknown7006('bno110_0', 100, 829386338, 828321841, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    callSubroutine('NoelComboDeriveClear')
    sprite('no203_12', 2)	# 42-43
    Unknown2015(0)
    sprite('no203_12', 2)	# 44-45
    sprite('no203_13', 4)	# 46-49

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(11000)
        AirPushbackY(23000)
        AttackP1(90)
        AirUntechableTime(24)
        AirHitstunAnimation(13)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)
    sprite('no210_00', 2)	# 1-2
    sprite('no210_01', 1)	# 3-3
    Unknown7006('bno106_0', 100, 829386338, 828323376, 0, 0, 100, 829386338, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('no210_01', 1)	# 4-4
    sprite('no210_02', 1)	# 5-5
    sprite('no210_02', 1)	# 6-6
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('no210_03', 1)	# 7-7
    sprite('no210_04', 1)	# 8-8	 **attackbox here**
    sprite('no210_04', 2)	# 9-10	 **attackbox here**
    setInvincible(0)
    SFX_0('003_swing_grap_0_1')
    sprite('no210_05', 4)	# 11-14
    Recovery()
    Unknown2063()
    sprite('no210_06', 4)	# 15-18
    sprite('no210_07', 5)	# 19-23
    sprite('no210_08', 5)	# 24-28
    sprite('no210_09', 4)	# 29-32
    sprite('no210_10', 4)	# 33-36
    SFX_FOOTSTEP_(100, 1, 1)

@State
def NmlAtk4B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        AttackP1(80)
        Unknown9018(1)
        Hitstop(6)
        Unknown11001(-2, -2, -2)
        Unknown11058('0000000000000000000000000100000000000000')
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(10)
        Unknown9130(32)
        Unknown9142(32)
        AirUntechableTime(40)
        AirPushbackY(21000)
        Unknown30055('905f01001e00000000000000')
        Unknown30056('a08601001e00000000000000')
        YImpluseBeforeWallbounce(2300)
        PushbackX(20000)
        Unknown2004(1, 0)
        callSubroutine('NoelComboFirst')
        JumpCancel_(1)
    sprite('no214_00', 4)	# 1-4
    sprite('no214_01', 4)	# 5-8
    Unknown7006('bno112_0', 100, 829386338, 828322353, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_3('nose_07')
    SFX_0('001_airbackdash_0')
    setInvincible(1)
    Unknown22019('0000000001000000000000000100000000000000')
    sprite('no214_02', 3)	# 9-11
    sprite('no214_03', 3)	# 12-14
    sprite('no214_04', 3)	# 15-17
    sprite('no214_05', 2)	# 18-19
    sprite('no214_06', 2)	# 20-21
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no214_07', 2)	# 22-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no214_08', 1)	# 24-24	 **attackbox here**
    StartMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 1)
    Unknown36(1)
    Unknown1077(80000, 40000)
    Unknown35()
    GFX_0('noef_gfground', 2)
    sprite('no214_08', 2)	# 25-26	 **attackbox here**
    sprite('no214_09', 2)	# 27-28	 **attackbox here**
    SFX_3('nose_01')
    sprite('no214_09', 4)	# 29-32	 **attackbox here**
    sprite('no214_10', 8)	# 33-40
    callSubroutine('NoelComboDeriveTimingBegin')
    setInvincible(0)
    sprite('no214_11', 4)	# 41-44
    sprite('no214_11', 4)	# 45-48
    callSubroutine('NoelComboDeriveClear')
    sprite('no214_12', 7)	# 49-55
    SFX_FOOTSTEP_(100, 1, 1)

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk4B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        WhiffCancel('NmlAtk2A')
    sprite('no231_00', 2)	# 1-2
    sprite('no231_01', 2)	# 3-4
    sprite('no231_02', 2)	# 5-6
    Unknown7009(0)
    sprite('no231_03', 2)	# 7-8	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    sprite('no231_04', 4)	# 9-12
    Recovery()
    Unknown2063()
    sprite('no231_05', 4)	# 13-16
    WhiffCancelEnable(1)
    sprite('no231_06', 4)	# 17-20

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(700)
        AttackP1(90)
        Unknown11092(1)
        Hitstop(2)
        Unknown9018(1)
        AirUntechableTime(30)
        hitstun(27)
        sendToLabelUpon(4, 1)
        sendToLabelUpon(2, 2)
        callSubroutine('NoelComboFirst')
        GuardPoint_(0)
        Unknown11058('0100000000000000000000000000000000000000')
        YImpluseBeforeWallbounce(1800)
        PushbackX(12000)
        AirHitstunAnimation(10)
    sprite('no213_00', 3)	# 1-3
    sprite('no213_01', 1)	# 4-4
    SFX_3('nose_07')
    Unknown7006('bno109_1', 100, 829386338, 845101360, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    physicsXImpulse(16000)
    physicsYImpulse(21000)
    setGravity(2300)
    Unknown1051(80)
    Unknown2016(250)
    sprite('no213_01', 4)	# 5-8
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000000000000')
    sprite('no213_02', 32767)	# 9-32775
    label(1)
    sprite('no213_03', 4)	# 32776-32779	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(8000)
    AirPushbackX(10000)
    setInvincible(0)
    clearUponHandler(4)
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    GFX_0('EFF_Spark', 1)
    GFX_0('BLT', 0)
    ScreenShake(0, 5000)
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no213_04', 1)	# 32780-32780	 **attackbox here**
    RefreshMultihit()
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    GFX_0('EFF_Spark', 1)
    GFX_0('BLT', 0)
    ScreenShake(0, 5000)
    sprite('no213_04', 1)	# 32781-32781	 **attackbox here**
    GFX_0('EFF_Spark', 2)
    sprite('no213_04', 1)	# 32782-32782	 **attackbox here**
    GFX_0('EFF_Spark', 3)
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    sprite('no213_04', 1)	# 32783-32783	 **attackbox here**
    GFX_0('EFF_Spark', 4)
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    sprite('no213_05', 1)	# 32784-32784	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(16000)
    GFX_0('EFF_Spark', 1)
    GFX_0('BLT', 0)
    ScreenShake(0, 5000)
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    sprite('no213_05', 1)	# 32785-32785	 **attackbox here**
    GFX_0('EFF_Spark', 2)
    sprite('no213_05', 1)	# 32786-32786	 **attackbox here**
    GFX_0('EFF_Spark', 3)
    sprite('no213_05', 1)	# 32787-32787	 **attackbox here**
    GFX_0('EFF_Spark', 4)
    label(3)
    sprite('no213_05', 1)	# 32788-32788	 **attackbox here**
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('no213_06', 4)	# 32789-32792
    Unknown2006()
    Unknown8000(100, 1, 1)
    Unknown1051(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    SFX_3('nose_01')
    callSubroutine('NoelComboDeriveTimingBegin')
    Unknown2006()
    sprite('no213_07', 5)	# 32793-32797
    sprite('no213_08', 6)	# 32798-32803
    callSubroutine('NoelComboDeriveClear')
    sprite('no213_08', 3)	# 32804-32806
    sprite('no213_09', 4)	# 32807-32810
    sprite('no213_09', 1)	# 32811-32811
    sprite('no213_10', 5)	# 32812-32816

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        ProjectileDurabilityLvl(1)
        Unknown9018(1)
        Hitstop(3)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(6000)
        AirPushbackY(16000)
        AirUntechableTime(26)
        JumpCancel_(1)
    sprite('no233_00', 3)	# 1-3
    sprite('no233_01', 3)	# 4-6
    physicsXImpulse(42000)
    sprite('no233_01', 2)	# 7-8
    Unknown7006('bno107_1', 100, 829386338, 845100848, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_0('019_cloth_a')
    sprite('no233_02', 2)	# 9-10
    physicsXImpulse(21000)
    Unknown2015(150)
    sprite('no233_03', 2)	# 11-12
    Unknown1019(65)
    sprite('no233_04', 3)	# 13-15
    sprite('no233_05', 1)	# 16-16	 **attackbox here**
    Unknown1019(0)
    StartMultihit()
    GFX_0('BLT', 0)
    GFX_0('EFF_LongFireTypeB', 1)
    ScreenShake(0, 5000)
    SFX_0('016_explode_1')
    sprite('no233_05', 3)	# 17-19	 **attackbox here**
    SFX_3('nose_01')
    sprite('no233_05', 4)	# 20-23	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    Unknown2015(-1)
    sprite('no233_06', 6)	# 24-29
    sprite('no233_07', 6)	# 30-35
    sprite('no233_08', 6)	# 36-41
    sprite('no233_09', 5)	# 42-46
    sprite('no233_10', 5)	# 47-51

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        ProjectileDurabilityLvl(1)
        Damage(620)
        Unknown11092(1)
        Hitstop(3)
        AirPushbackX(3000)
        AirPushbackY(22000)
        Unknown30056('d08affff3200000000000000')
        HitOrBlockJumpCancel(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
    sprite('no252_00', 1)	# 1-1
    sprite('no252_01', 1)	# 2-2
    sprite('no252_02', 2)	# 3-4
    sprite('no252_03', 2)	# 5-6
    SFX_1('bno105_0')
    sprite('no252_04', 2)	# 7-8
    sprite('no252_05', 1)	# 9-9
    SFX_0('004_swing_grap_1_1')
    Unknown14070('NmlAtkAIR5A_2nd')
    Unknown14070('NmlAtkAIR5B')
    Unknown14070('NmlAtkAIR5C')
    sprite('no252_06', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 1)
    SFX_0('016_explode_1')
    sprite('no252_06', 1)	# 11-11	 **attackbox here**
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 2)
    if SLOT_2:
        HitOverhead(0)
    sprite('no252_07', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 1)
    SFX_0('016_explode_1')
    sprite('no252_07', 1)	# 13-13	 **attackbox here**
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 2)
    if SLOT_2:
        HitOverhead(0)
    sprite('no252_08', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 1)
    Hitstop(5)
    if SLOT_2:
        Unknown14072('NmlAtkAIR5A_2nd')
        Unknown14072('NmlAtkAIR5B')
        Unknown14072('NmlAtkAIR5C')
    sprite('no252_08', 1)	# 15-15	 **attackbox here**
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 2)
    SFX_0('016_explode_1')
    sprite('no252_09', 2)	# 16-17
    SFX_3('nose_01')
    Recovery()
    Unknown2063()
    sprite('no252_10', 4)	# 18-21
    sprite('no252_11', 5)	# 22-26
    Unknown14074('NmlAtkAIR5A_2nd')
    Unknown14074('NmlAtkAIR5B')
    Unknown14074('NmlAtkAIR5C')
    sprite('no252_12', 5)	# 27-31

@State
def NmlAtkAIR5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        AirPushbackX(12000)
        AirPushbackY(13000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_LANDING():
            Unknown26('noef_293')
    sprite('no293_00', 2)	# 1-2
    sprite('no293_01', 2)	# 3-4
    sprite('no293_02', 2)	# 5-6
    Unknown7006('bno104_2', 100, 829386338, 845100336, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('no293_03', 2)	# 7-8
    SFX_0('016_explode_1')
    GFX_0('noef_293', 2)
    sprite('no293_04', 3)	# 9-11	 **attackbox here**
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no293_05', 3)	# 12-14
    Recovery()
    Unknown2063()
    sprite('no293_06', 3)	# 15-17
    sprite('no293_07', 3)	# 18-20
    sprite('no293_08', 4)	# 21-24
    sprite('no293_09', 4)	# 25-28
    sprite('no293_10', 4)	# 29-32
    sprite('no020_05', 3)	# 33-35

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(800)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        AirPushbackX(0)
        AirPushbackY(-36000)
        YImpluseBeforeWallbounce(0)
        Unknown9118(60)
        Hitstop(0)
        PushbackX(10000)
        Unknown9310(4)
        AirUntechableTime(35)
        HitOverhead(0)
        clearUponHandler(2)

        def upon_LANDING():
            callSubroutine('NoelComboDeriveInputBegin')
            sendToLabel(1)
        Unknown1017()
        Unknown1022()
        JumpCancel_(1)
        callSubroutine('NoelComboFirst')
        clearUponHandler(3)
    sprite('no253_00', 5)	# 1-5
    sprite('no253_01', 5)	# 6-10
    Unknown7006('bno114_0', 100, 829386338, 828322865, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown1084(1)
    Unknown1018()
    Unknown1015(20000)
    Unknown1019(20)
    physicsYImpulse(20000)
    setGravity(2000)
    SFX_3('nose_07')
    SFX_0('001_airbackdash_0')
    Unknown1015(80000)
    Unknown1019(10)
    sprite('no253_02', 5)	# 11-15
    sprite('no253_03', 5)	# 16-20
    sprite('no253_04', 1)	# 21-21	 **attackbox here**
    callSubroutine('NoelComboDeriveInputBegin')
    RefreshMultihit()
    physicsYImpulse(3000)
    ScreenShake(0, 5000)
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_LongFireTypeB', 1)
    Unknown36(1)
    Unknown1072(90000)
    Unknown35()
    sprite('no253_04', 3)	# 22-24	 **attackbox here**
    SFX_3('nose_01')
    sprite('no253_05', 1)	# 25-25	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(3000)
    ScreenShake(0, 5000)
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_LongFireTypeB', 1)
    Unknown36(1)
    Unknown2005()
    Unknown1072(90000)
    Unknown35()
    sprite('no253_05', 4)	# 26-29	 **attackbox here**
    SFX_3('nose_01')
    sprite('no253_06', 4)	# 30-33
    sprite('no253_07', 3)	# 34-36
    sprite('no253_08', 3)	# 37-39
    sprite('no253_09', 3)	# 40-42
    sprite('no253_10', 3)	# 43-45
    sprite('no253_11', 3)	# 46-48
    sprite('no253_12', 3)	# 49-51
    sprite('no253_13', 32767)	# 52-32818
    label(1)
    sprite('no024_01', 3)	# 32819-32821
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown2006()
    callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no024_02', 10)	# 32822-32831
    sprite('no024_03', 2)	# 32832-32833
    sprite('no024_04', 2)	# 32834-32835
    callSubroutine('NoelComboDeriveClear')

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(370)
        Unknown11092(1)
        AirUntechableTime(22)
        hitstun(22)
        ProjectileDurabilityLvl(1)
        AirPushbackX(3000)
        AirPushbackY(8000)
        Hitstop(3)
        HitOverhead(0)

        def upon_12():
            Unknown14070('NmlAtkAIR5C_2nd')
    sprite('no404_00', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(10000)
    physicsYImpulse(26000)
    Unknown1043()
    sprite('no404_01', 3)	# 4-6
    tag_voice(1, 'bno201_0', 'bno201_1', 'bno201_2', '')
    sprite('no404_02', 3)	# 7-9
    sprite('no404_03', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    GFX_0('EFF_SakuretsuFar', 2)
    GFX_0('EFF_SakuretsuNear', 3)
    sprite('no404_04', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    GFX_0('EFF_SakuretsuNear', 2)
    GFX_0('EFF_SakuretsuFar', 3)
    sprite('no404_05', 3)	# 16-18	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    GFX_0('EFF_SakuretsuNear', 2)
    GFX_0('EFF_SakuretsuFar', 3)
    sprite('no404_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    GFX_0('EFF_SakuretsuNear', 2)
    GFX_0('EFF_SakuretsuFar', 3)
    sprite('no404_07', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_0('EFF_SakuretsuFar', 1)
    sprite('no404_08', 2)	# 23-24
    SFX_3('nose_01')
    Unknown22004(8, 1)
    Recovery()
    Unknown2063()
    sprite('no404_09', 2)	# 25-26
    Unknown14072('NmlAtkAIR5C_2nd')
    sprite('no404_10', 2)	# 27-28
    sprite('no404_11', 2)	# 29-30
    sprite('no404_12', 2)	# 31-32
    Unknown14074('NmlAtkAIR5C_2nd')
    sprite('no404_13', 2)	# 33-34
    sprite('no404_14', 2)	# 35-36
    loopRest()

@State
def NmlAtkAIR5C_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        HitOverhead(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(38000)
        AirPushbackY(-40000)
        AirUntechableTime(40)
        Unknown9310(1)
        Unknown1084(1)
    sprite('no293_00', 2)	# 1-2
    sprite('no293_01', 2)	# 3-4
    sprite('no293_02', 2)	# 5-6
    sprite('no293_03', 2)	# 7-8
    SFX_0('016_explode_1')
    GFX_0('noef_293', 2)
    sprite('no293_04ex00', 3)	# 9-11	 **attackbox here**
    tag_voice(0, 'bno202_0', 'bno202_1', 'bno202_2', '')
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no293_05', 3)	# 12-14
    Unknown1015(-8000)
    physicsYImpulse(12000)
    setGravity(2400)
    Recovery()
    sprite('no293_06', 3)	# 15-17
    Unknown1019(80)
    Recovery()
    Unknown2063()
    sprite('no293_06', 3)	# 18-20
    Unknown1019(80)
    sprite('no293_07', 3)	# 21-23
    Unknown1019(80)
    sprite('no293_07', 3)	# 24-26
    Unknown1019(80)
    sprite('no293_08', 4)	# 27-30
    Unknown1019(80)
    sprite('no293_09', 4)	# 31-34
    sprite('no293_10', 4)	# 35-38
    sprite('no020_05', 3)	# 39-41
    label(99)
    sprite('no020_06', 3)	# 42-44
    sprite('no020_07', 3)	# 45-47
    loopRest()
    gotoLabel(99)

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('no030_00', 2)	# 1-2
    sprite('no030_01', 2)	# 3-4
    sprite('no032_00', 2)	# 5-6
    sprite('no032_01', 2)	# 7-8
    label(0)
    sprite('no032_02', 4)	# 9-12
    sprite('no032_03', 4)	# 13-16
    sprite('no032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 21-24
    sprite('no032_06', 4)	# 25-28
    sprite('no032_07', 4)	# 29-32
    sprite('no032_08', 4)	# 33-36
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 37-40
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no310_00', 3)	# 41-43
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('no310_01', 3)	# 44-46	 **attackbox here**
    Unknown1084(1)
    SFX_0('010_swing_sword_0')
    sprite('no310_02', 5)	# 47-51
    SFX_4('bno154')
    sprite('no310_03', 13)	# 52-64
    sprite('no310_04', 5)	# 65-69

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(1300)
        AttackP2(50)
        Unknown11092(1)
        Unknown11078(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(60)
        Unknown9142(35)
        EnableCollision(0)
        Hitstop(0)
        Unknown9310(3)
        PushbackX(10000)
        JumpCancel_(1)
        Unknown2018(0, 80)
        Unknown13024(0)
        Unknown11064(1)
    sprite('no310_01', 1)	# 1-1	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('no311_00', 4)	# 2-5
    SFX_1('bno153')
    sprite('no311_01', 4)	# 6-9
    Unknown2018(1, 80)
    sprite('no311_02', 4)	# 10-13	 **attackbox here**
    AirPushbackX(30000)
    sprite('no313_00', 3)	# 14-16
    sprite('no313_01', 3)	# 17-19
    Hitstop(2147483647)
    AttackLevel_(3)
    AirUntechableTime(35)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    RefreshMultihit()
    Unknown11064(0)
    Unknown11023(1)
    sendToLabelUpon(2, 77)
    sprite('no313_02', 8)	# 20-27
    physicsXImpulse(5000)
    physicsYImpulse(15600)
    setGravity(1400)
    Damage(700)
    Unknown9202(20)
    AirPushbackX(20000)
    AirPushbackY(10000)
    sprite('no313_03', 2)	# 28-29	 **attackbox here**
    SFX_0('006_swing_blade_1')
    sprite('no313_04', 2)	# 30-31
    Unknown13024(1)
    sprite('no313_05', 2)	# 32-33
    sprite('no313_06', 2)	# 34-35
    sprite('no313_07', 2)	# 36-37
    sprite('no313_08', 2)	# 38-39
    sprite('no313_09', 100)	# 40-139
    label(77)
    sprite('no313_10', 3)	# 140-142
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('no313_11', 3)	# 143-145
    sprite('no313_12', 3)	# 146-148

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('no030_00', 2)	# 1-2
    sprite('no030_01', 2)	# 3-4
    sprite('no032_00', 2)	# 5-6
    sprite('no032_01', 2)	# 7-8
    label(0)
    sprite('no032_02', 4)	# 9-12
    sprite('no032_03', 4)	# 13-16
    sprite('no032_04', 4)	# 17-20
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 21-24
    sprite('no032_06', 4)	# 25-28
    sprite('no032_07', 4)	# 29-32
    sprite('no032_08', 4)	# 33-36
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 37-40
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no310_00', 3)	# 41-43
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('no310_01', 3)	# 44-46	 **attackbox here**
    Unknown1084(1)
    SFX_0('010_swing_sword_0')
    sprite('no310_02', 5)	# 47-51
    SFX_4('bno154')
    sprite('no310_03', 13)	# 52-64
    sprite('no310_04', 5)	# 65-69

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(1300)
        AttackP2(50)
        Unknown11092(1)
        Unknown11078(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(60)
        Unknown9142(35)
        EnableCollision(0)
        Hitstop(0)
        Unknown9310(3)
        JumpCancel_(1)
        Unknown2018(0, 80)
        Unknown13021(1)
        Unknown21005(1)
        Unknown13024(0)
        Unknown11064(1)
    sprite('no310_01', 1)	# 1-1	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('no311_00', 4)	# 2-5
    SFX_1('bno153')
    sprite('no311_01', 4)	# 6-9
    Unknown2018(1, 80)
    sprite('no311_02', 4)	# 10-13	 **attackbox here**
    sprite('no311_03', 3)	# 14-16
    physicsXImpulse(10000)
    physicsYImpulse(29000)
    setGravity(2100)
    sprite('no311_04', 3)	# 17-19
    sprite('no311_05', 3)	# 20-22
    sprite('no311_06', 3)	# 23-25
    sprite('no311_07', 2)	# 26-27
    sprite('no311_08', 2)	# 28-29
    sprite('no311_09', 2)	# 30-31	 **attackbox here**
    Hitstop(2147483647)
    AttackLevel_(3)
    Damage(700)
    AirUntechableTime(35)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(-20000)
    AirPushbackY(2000)
    Unknown9202(20)
    RefreshMultihit()
    Unknown11064(0)
    Unknown11023(1)
    sendToLabelUpon(2, 77)
    SFX_0('006_swing_blade_1')
    sprite('no311_10', 2)	# 32-33
    Unknown13024(1)
    sprite('no311_11', 2)	# 34-35
    sprite('no311_12', 100)	# 36-135
    label(77)
    sprite('no311_13', 5)	# 136-140
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('no311_14', 5)	# 141-145

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('no406_00', 3)	# 1-3
    sprite('no406_01', 1)	# 4-4
    Unknown7006('bno156_0', 100, 829386338, 828323381, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('no406_01', 2)	# 5-6
    SFX_0('008_swing_pole_1')
    sprite('no406_02', 2)	# 7-8
    sprite('no406_03', 2)	# 9-10
    sprite('no406_01', 2)	# 11-12
    SFX_0('008_swing_pole_1')
    label(0)
    sprite('no406_01', 2)	# 13-14
    clearUponHandler(3)
    sprite('no406_02', 2)	# 15-16
    sprite('no406_03', 2)	# 17-18
    sprite('no406_04', 2)	# 19-20
    SFX_0('004_swing_grap_1_2')
    sprite('no406_05', 1)	# 21-21	 **attackbox here**
    GFX_0('noef_406', -1)
    StartMultihit()
    sprite('no406_05', 3)	# 22-24	 **attackbox here**
    SFX_0('016_explode_1')
    sprite('no406_06', 4)	# 25-28
    sprite('no406_07', 4)	# 29-32
    sprite('no406_08', 4)	# 33-36
    sprite('no406_09', 4)	# 37-40
    sprite('no406_10', 3)	# 41-43
    sprite('no406_11', 3)	# 44-46
    sprite('no406_12', 2)	# 47-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('no406_06', 3)	# 2-4
    sprite('no406_07', 3)	# 5-7
    sprite('no406_08', 3)	# 8-10
    sprite('no406_09', 2)	# 11-12
    sprite('no406_10', 2)	# 13-14
    sprite('no406_11', 2)	# 15-16
    sprite('no406_12', 2)	# 17-18
    sprite('no290_00', 2)	# 19-20
    sprite('no290_01', 4)	# 21-24
    SFX_3('nose_07')
    sprite('no290_02', 2)	# 25-26
    tag_voice(1, 'bno157_0', 'bno157_1', '', '')
    sprite('no290_03', 2)	# 27-28
    sprite('no290_04', 1)	# 29-29
    sprite('no290_05', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    ScreenShake(0, 5000)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    SFX_0('016_explode_1')
    GFX_0('BLT', 1)
    Unknown22032(0)
    sprite('no290_03', 4)	# 32-35
    SFX_3('nose_01')
    Recovery()
    Unknown2063()
    sprite('no290_02', 5)	# 36-40
    sprite('no290_01', 5)	# 41-45
    sprite('no402_06', 5)	# 46-50
    label(0)
    sprite('no000_00', 7)	# 51-57
    sprite('no000_01', 7)	# 58-64
    sprite('no000_02', 7)	# 65-71
    sprite('no000_03', 7)	# 72-78
    sprite('no000_04', 7)	# 79-85
    sprite('no000_05', 7)	# 86-92
    sprite('no000_06', 7)	# 93-99
    sprite('no000_07', 7)	# 100-106
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 107-107

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('no210_00', 5)	# 1-5
    sprite('no210_01', 3)	# 6-8
    Unknown1084(1)
    sprite('no210_01', 3)	# 9-11
    sprite('no210_02', 2)	# 12-13
    sprite('no210_03', 1)	# 14-14
    sprite('no210_04', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('no210_04', 2)	# 16-17	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    sprite('no210_05', 4)	# 18-21
    sprite('no210_06', 4)	# 22-25
    sprite('no210_07', 5)	# 26-30
    sprite('no210_08', 5)	# 31-35
    sprite('no210_09', 4)	# 36-39
    sprite('no210_10', 4)	# 40-43
    label(0)
    sprite('no000_00', 7)	# 44-50
    sprite('no000_01', 7)	# 51-57
    sprite('no000_02', 7)	# 58-64
    sprite('no000_03', 7)	# 65-71
    sprite('no000_04', 7)	# 72-78
    sprite('no000_05', 7)	# 79-85
    sprite('no000_06', 7)	# 86-92
    sprite('no000_07', 7)	# 93-99
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 100-100

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        sendToLabelUpon(2, 3)
    sprite('no292_00', 3)	# 1-3
    sprite('no292_01', 4)	# 4-7
    sprite('no292_02', 4)	# 8-11
    SFX_3('nose_01')
    sprite('no292_03', 3)	# 12-14
    tag_voice(0, 'bno158_0', 'bno158_1', '', '')
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_04', 4)	# 15-18
    sprite('no292_04', 1)	# 19-19
    SFX_0('016_explode_1')
    SFX_3('nose_00')
    sprite('no292_05ex02', 3)	# 20-22	 **attackbox here**
    GFX_0('noef_292', -1)
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 5000)
    sprite('no292_06', 4)	# 23-26	 **attackbox here**
    sprite('no292_07', 4)	# 27-30	 **attackbox here**
    StartMultihit()
    sprite('no292_08', 5)	# 31-35
    SFX_0('008_swing_pole_1')
    sprite('no292_09', 5)	# 36-40
    SFX_0('008_swing_pole_1')
    sprite('no292_10', 5)	# 41-45
    SFX_0('008_swing_pole_1')
    sprite('no292_11', 5)	# 46-50
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_12', 5)	# 51-55
    sprite('no292_13', 5)	# 56-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no292_00', 3)	# 57-59
    sprite('no292_01', 4)	# 60-63
    sprite('no292_02', 4)	# 64-67
    SFX_3('nose_01')
    sprite('no292_03', 3)	# 68-70
    tag_voice(0, 'bno158_0', 'bno158_1', '', '')
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_04', 4)	# 71-74
    sprite('no292_04', 1)	# 75-75
    SFX_0('016_explode_1')
    SFX_3('nose_00')
    sprite('no292_05ex02', 3)	# 76-78	 **attackbox here**
    GFX_0('noef_292', -1)
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 5000)
    sprite('no292_06', 4)	# 79-82	 **attackbox here**
    sprite('no292_07', 4)	# 83-86	 **attackbox here**
    StartMultihit()
    sprite('no292_08', 5)	# 87-91
    SFX_0('008_swing_pole_1')
    sprite('no292_09', 5)	# 92-96
    SFX_0('008_swing_pole_1')
    sprite('no292_10', 5)	# 97-101
    SFX_0('008_swing_pole_1')
    sprite('no292_11', 5)	# 102-106
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_12', 5)	# 107-111
    sprite('no292_13', 5)	# 112-116

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 15)	# 1-15
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 16-16
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1100000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('no032_10', 4)	# 17-20
    sprite('no032_11', 3)	# 21-23
    Unknown1084(1)
    Unknown1045(6000)
    sprite('no213_00', 2)	# 24-25
    sprite('no213_01', 6)	# 26-31
    physicsXImpulse(12000)
    physicsYImpulse(25000)
    setGravity(3800)
    SFX_3('nose_07')
    SFX_0('001_airbackdash_0')

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('no213_02', 2)	# 32-33
    sprite('no213_03', 5)	# 34-38	 **attackbox here**
    StartMultihit()
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    GFX_0('EFF_Spark', 1)
    GFX_0('BLT', 0)
    sprite('no213_04', 3)	# 39-41	 **attackbox here**
    StartMultihit()
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    GFX_0('EFF_Spark', 1)
    GFX_0('BLT', 0)
    sprite('no213_04', 3)	# 42-44	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('EFF_Spark', 2)
    sprite('no213_05', 1)	# 45-45	 **attackbox here**
    StartMultihit()
    SFX_3('nose_00')
    SFX_0('016_explode_1')
    GFX_0('EFF_Spark', 1)
    GFX_0('EFF_Spark', 2)
    GFX_0('BLT', 0)
    sprite('no213_05', 1)	# 46-46	 **attackbox here**
    GFX_0('EFF_Spark', 3)
    GFX_0('EFF_Spark', 4)
    ScreenShake(0, 5000)
    sprite('no213_05', 3)	# 47-49	 **attackbox here**
    label(1)
    sprite('no213_06', 3)	# 50-52
    Unknown2006()
    Unknown8000(100, 1, 1)
    Unknown1051(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    SFX_3('nose_01')
    sprite('no213_07', 3)	# 53-55
    Unknown2006()
    sprite('no213_08', 5)	# 56-60
    sprite('no213_09', 2)	# 61-62
    sprite('no213_09', 1)	# 63-63
    sprite('no213_10', 3)	# 64-66
    sprite('no000_00', 7)	# 67-73
    sprite('no000_01', 7)	# 74-80
    sprite('no000_02', 7)	# 81-87
    sprite('no000_03', 7)	# 88-94
    sprite('no000_04', 7)	# 95-101
    sprite('no000_05', 7)	# 102-108
    sprite('no000_06', 7)	# 109-115
    sprite('no000_07', 7)	# 116-122

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('no211_00', 1)	# 1-1
    sprite('no211_01', 1)	# 2-2
    sprite('no211_02', 1)	# 3-3
    sprite('no211_03', 1)	# 4-4
    sprite('no211_04', 1)	# 5-5
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no211_05', 2)	# 6-7
    sprite('no211_06', 2)	# 8-9
    sprite('no211_07', 2)	# 10-11
    sprite('no211_08', 2)	# 12-13	 **attackbox here**
    SFX_0('004_swing_grap_1_1')
    sprite('no211_09', 3)	# 14-16	 **attackbox here**
    sprite('no211_10', 3)	# 17-19	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('no211_11', 3)	# 20-22	 **attackbox here**
    sprite('no211_12', 3)	# 23-25
    sprite('no211_13', 3)	# 26-28
    sprite('no211_14', 3)	# 29-31
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no211_15', 3)	# 32-34
    loopRest()
    sprite('no000_00', 7)	# 35-41
    sprite('no000_01', 7)	# 42-48
    sprite('no000_02', 7)	# 49-55
    sprite('no000_03', 7)	# 56-62
    sprite('no000_04', 7)	# 63-69
    sprite('no000_05', 7)	# 70-76
    sprite('no000_06', 7)	# 77-83
    sprite('no000_07', 7)	# 84-90

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        sendToLabelUpon(2, 3)
    sprite('no292_00', 3)	# 1-3
    sprite('no292_01', 4)	# 4-7
    sprite('no292_02', 4)	# 8-11
    SFX_3('nose_01')
    sprite('no292_03', 3)	# 12-14
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_04', 4)	# 15-18
    sprite('no292_04', 1)	# 19-19
    SFX_0('016_explode_1')
    SFX_3('nose_00')
    sprite('no292_05ex02', 3)	# 20-22	 **attackbox here**
    GFX_0('noef_292', -1)
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 5000)
    sprite('no292_06', 4)	# 23-26	 **attackbox here**
    sprite('no292_07', 4)	# 27-30	 **attackbox here**
    StartMultihit()
    sprite('no292_08', 5)	# 31-35
    SFX_0('008_swing_pole_1')
    sprite('no292_09', 5)	# 36-40
    SFX_0('008_swing_pole_1')
    sprite('no292_10', 5)	# 41-45
    SFX_0('008_swing_pole_1')
    sprite('no292_11', 5)	# 46-50
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_12', 5)	# 51-55
    sprite('no292_13', 5)	# 56-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no292_00', 3)	# 57-59
    sprite('no292_01', 4)	# 60-63
    sprite('no292_02', 4)	# 64-67
    SFX_3('nose_01')
    sprite('no292_03', 3)	# 68-70
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_04', 4)	# 71-74
    sprite('no292_04', 1)	# 75-75
    SFX_0('016_explode_1')
    SFX_3('nose_00')
    sprite('no292_05ex02', 3)	# 76-78	 **attackbox here**
    GFX_0('noef_292', -1)
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 5000)
    sprite('no292_06', 4)	# 79-82	 **attackbox here**
    sprite('no292_07', 4)	# 83-86	 **attackbox here**
    StartMultihit()
    sprite('no292_08', 5)	# 87-91
    SFX_0('008_swing_pole_1')
    sprite('no292_09', 5)	# 92-96
    SFX_0('008_swing_pole_1')
    sprite('no292_10', 5)	# 97-101
    SFX_0('008_swing_pole_1')
    sprite('no292_11', 5)	# 102-106
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_12', 5)	# 107-111
    sprite('no292_13', 5)	# 112-116

@State
def con5A_1st():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        ProjectileDurabilityLvl(1)
        AttackP2(85)
        Unknown9018(1)
        Hitstop(3)
        AirPushbackX(5000)
        AirPushbackY(8000)
        YImpluseBeforeWallbounce(1600)
        PushbackX(12000)
        hitstun(21)
        AirUntechableTime(31)
        Unknown2004(1, 0)
        callSubroutine('NoelComboHasei')
    sprite('no282_00', 2)	# 1-2
    sprite('no282_01', 2)	# 3-4
    sprite('no282_02', 2)	# 5-6
    sprite('no282_03', 3)	# 7-9
    callSubroutine('NoelComboDeriveInputBegin')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no282_04ex00', 4)	# 10-13	 **attackbox here**
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    GFX_0('EFF_SakuretsuNear', 2)
    GFX_0('EFF_Spark', 2)
    Unknown36(1)
    Unknown1096(1100)
    Unknown35()
    GFX_0('EFF_SakuretsuNear', 3)
    GFX_0('EFF_Spark', 3)
    Unknown36(1)
    Unknown2005()
    Unknown1096(1100)
    Unknown35()
    ScreenShake(0, 5000)
    SFX_0('016_explode_1')
    sprite('no282_04', 2)	# 14-15	 **attackbox here**
    callSubroutine('NoelComboDeriveTimingBegin')
    StartMultihit()
    SFX_3('nose_01')
    sprite('no282_05', 5)	# 16-20
    sprite('no282_06', 5)	# 21-25
    callSubroutine('NoelComboDeriveClear')
    sprite('no282_07', 4)	# 26-29
    sprite('no282_08', 4)	# 30-33
    SFX_FOOTSTEP_(100, 1, 1)

@State
def con5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        Unknown11092(1)
        AirPushbackX(7500)
        AirPushbackY(24000)
        Unknown30056('d8d600003200000000000000')
        YImpluseBeforeWallbounce(2000)
        PushbackX(12000)
        hitstun(30)
        AirUntechableTime(40)
        Hitstop(12)
        AirHitstunAnimation(10)
        callSubroutine('NoelComboHasei')
    sprite('no281_00', 2)	# 1-2
    physicsXImpulse(8000)
    SFX_3('nose_07')
    sprite('no281_01', 2)	# 3-4
    sprite('no281_02', 2)	# 5-6
    physicsXImpulse(0)
    sprite('no281_03', 2)	# 7-8
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no281_04', 2)	# 9-10	 **attackbox here**
    sprite('no281_05', 2)	# 11-12	 **attackbox here**
    StartMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_LongFireTypeB', 1)
    ScreenShake(0, 5000)
    sprite('no281_05', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    Unknown9018(1)
    ProjectileDurabilityLvl(1)
    Hitstop(3)
    WallbounceReboundTime(25)
    sprite('no281_05', 4)	# 15-18	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('no281_06', 2)	# 19-20
    SFX_3('nose_01')
    sprite('no281_06', 5)	# 21-25
    callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no281_07', 6)	# 26-31
    sprite('no281_08', 6)	# 32-37
    callSubroutine('NoelComboDeriveClear')

@State
def con5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(900)
        Unknown11092(1)
        Hitstop(3)
        GroundedHitstunAnimation(1)
        PushbackX(16000)
        AirUntechableTime(35)
        callSubroutine('NoelComboHasei')
        Unknown9018(1)
        Unknown2004(1, 0)
    sprite('no280_00', 1)	# 1-1
    SFX_3('nose_07')
    sprite('no280_01', 1)	# 2-2
    sprite('no280_02', 1)	# 3-3
    sprite('no280_03', 1)	# 4-4
    sprite('no280_04', 2)	# 5-6
    sprite('no280_05', 2)	# 7-8
    sprite('no280_06', 2)	# 9-10
    sprite('no280_07', 2)	# 11-12
    sprite('no280_08', 2)	# 13-14	 **attackbox here**
    GFX_0('EFF_LongFireTypeA', 1)
    SFX_0('016_explode_1')
    GFX_0('BLT', 3)
    ScreenShake(0, 5000)
    AirPushbackX(7000)
    Unknown30056('48e801001e00000000000000')
    AirPushbackY(5000)
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no280_07', 2)	# 15-16
    sprite('no280_08', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(8500)
    YImpluseBeforeWallbounce(1300)
    GFX_0('EFF_LongFireTypeA', 0)
    SFX_0('016_explode_1')
    GFX_0('BLT', 2)
    ScreenShake(0, 5000)
    sprite('no280_08', 10)	# 19-28	 **attackbox here**
    callSubroutine('NoelComboDeriveTimingBegin')
    StartMultihit()
    SFX_3('nose_01')
    sprite('no280_09', 5)	# 29-33
    callSubroutine('NoelComboDeriveClear')
    sprite('no280_10', 5)	# 34-38
    sprite('no280_11', 5)	# 39-43

@State
def con5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(1000)
        Unknown11092(1)
        GroundedHitstunAnimation(0)
        Unknown9130(42)
        Unknown9142(32)
        AirUntechableTime(25)
        hitstun(23)
        Hitstop(3)
        Unknown11001(5, 5, 5)
        AirPushbackX(12000)
        AirPushbackY(17000)
        YImpluseBeforeWallbounce(2600)
        Unknown30056('b0ad01001e00000000000000')
        PushbackX(16000)
        Unknown9018(1)
        Unknown2004(1, 0)
        callSubroutine('NoelComboHasei')
    sprite('no284_00', 5)	# 1-5
    SFX_3('nose_07')
    sprite('no284_01', 4)	# 6-9
    physicsXImpulse(45000)
    sprite('no284_02', 3)	# 10-12
    Unknown1019(80)
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no284_03', 3)	# 13-15
    Unknown1019(45)
    sprite('no284_04', 2)	# 16-17	 **attackbox here**
    StartMultihit()
    sprite('no284_05', 2)	# 18-19	 **attackbox here**
    Unknown1019(0)
    SFX_0('016_explode_1')
    GFX_0('BLT', 1)
    GFX_0('EFF_LongFireTypeA', 3)
    ScreenShake(0, 5000)
    sprite('no284_04', 2)	# 20-21	 **attackbox here**
    StartMultihit()
    sprite('no284_05', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_LongFireTypeA', 2)
    ScreenShake(0, 5000)
    sprite('no284_05', 1)	# 24-24	 **attackbox here**
    StartMultihit()
    sprite('no284_05', 2)	# 25-26	 **attackbox here**
    StartMultihit()
    sprite('no284_06', 5)	# 27-31
    SFX_3('nose_01')
    callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no284_07', 5)	# 32-36
    sprite('no284_08', 5)	# 37-41
    callSubroutine('NoelComboDeriveClear')
    sprite('no284_09', 5)	# 42-46
    sprite('no284_10', 5)	# 47-51
    physicsXImpulse(0)
    sprite('no284_11', 5)	# 52-56

@State
def con5B_Middle():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('NoelComboHasei')
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        AttackP1(90)
        AttackP2(75)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(9000)
        AirPushbackY(24500)
        Hitstop(3)
        Unknown11058('0000000000000000010000000000000000000000')
        AirUntechableTime(45)
        PushbackX(12000)
        Unknown22019('0000000001000000000000000100000000000000')
        Unknown13021(1)
        Unknown21005(1)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if (SLOT_19 <= 450000):
                    sendToLabel(0)
    sprite('no294_00', 1)	# 1-1
    sprite('no294_01', 1)	# 2-2
    Unknown18009(1)
    sprite('no294_02', 1)	# 3-3
    SFX_0('001_airbackdash_0')
    setInvincible(1)
    Unknown22019('0000000001000000000000000100000000000000')
    Unknown2037(1)
    sprite('no294_03', 2)	# 4-5
    physicsXImpulse(55000)
    sprite('no294_04', 2)	# 6-7
    sprite('no294_03', 2)	# 8-9
    Unknown1019(80)
    sprite('no294_04', 2)	# 10-11
    sprite('no294_03', 2)	# 12-13
    Unknown1019(80)
    sprite('no294_04', 2)	# 14-15
    label(0)
    sprite('no294_05', 2)	# 16-17
    clearUponHandler(3)
    setInvincible(1)
    EnableCollision(1)
    Unknown2015(-1)
    Unknown1084(1)
    Unknown18009(0)
    sprite('no294_06', 2)	# 18-19
    Unknown1045(20000)
    sprite('no294_07', 2)	# 20-21
    teleportRelativeX(50000)
    physicsXImpulse(15000)
    sprite('no294_08', 3)	# 22-24
    sprite('no294_09', 3)	# 25-27
    sprite('no294_10', 3)	# 28-30
    teleportRelativeX(50000)
    Unknown1019(30)
    Unknown18009(1)
    sprite('no294_11', 1)	# 31-31
    sprite('no291_14', 1)	# 32-32
    Unknown1084(1)
    callSubroutine('NoelComboDeriveInputBegin')
    Unknown14074('con5B_Middle')
    Unknown2005()
    sprite('no291_15ex00', 4)	# 33-36	 **attackbox here**
    GFX_0('BLT', 0)
    GFX_0('EFF_LongFireTypeD', 1)
    Unknown4004('464c4f52455f425552535400000000000000000000000000000000000000000002000000')
    ScreenShake(0, 5000)
    SFX_0('016_explode_1')
    sprite('no291_16', 2)	# 37-38
    setInvincible(0)
    callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no291_17', 4)	# 39-42
    sprite('no291_18', 4)	# 43-46
    SFX_0('008_swing_pole_1')
    callSubroutine('NoelComboDeriveClear')
    sprite('no291_19', 4)	# 47-50
    SFX_0('008_swing_pole_1')
    sprite('no291_20', 4)	# 51-54
    Unknown18009(0)
    SFX_0('008_swing_pole_1')
    sprite('no291_21', 4)	# 55-58
    SFX_0('008_swing_pole_1')
    sprite('no291_22', 3)	# 59-61
    sprite('no350_00', 2)	# 62-63

@State
def con2B_Low():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(500)
        AttackP1(90)
        AttackP2(75)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(21000)
        YImpluseBeforeWallbounce(1600)
        PushbackX(10000)
        GroundedHitstunAnimation(1)
        Hitstop(2)
        Unknown9018(1)
        AirUntechableTime(32)
        hitstun(27)
        sendToLabelUpon(2, 9)
        callSubroutine('NoelComboHasei')
        GuardPoint_(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2004(1, 0)
    sprite('no234_00', 2)	# 1-2
    Unknown1051(30)
    sprite('no234_00', 2)	# 3-4
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000000000000')
    sprite('no234_01', 3)	# 5-7
    sprite('no234_02', 3)	# 8-10
    physicsXImpulse(31000)
    physicsYImpulse(18000)
    setGravity(1600)
    Unknown23087(40000)
    SFX_0('001_airbackdash_0')
    sprite('no234_03', 3)	# 11-13
    Unknown1019(80)
    sprite('no234_04', 3)	# 14-16
    Unknown1019(80)
    sprite('no234_05', 3)	# 17-19
    Unknown1019(80)
    sprite('no234_06', 3)	# 20-22
    callSubroutine('NoelComboDeriveInputBegin')
    Unknown14074('con2B_Low')
    sprite('no234_07', 3)	# 23-25	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('noef_234', 1)
    Unknown36(1)
    Unknown1072(45000)
    Unknown35()
    sprite('no234_08', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('noef_234', 1)
    Unknown36(1)
    Unknown1072(30000)
    Unknown35()
    sprite('no234_09', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('noef_234', 1)
    Unknown36(1)
    Unknown1072(15000)
    Unknown35()
    sprite('no234_10', 32767)	# 32-32798
    label(9)
    sprite('no234_11', 6)	# 32799-32804
    SFX_1('no108')
    setInvincible(0)
    Unknown23087(0)
    Unknown1084(1)
    sprite('no234_12', 6)	# 32805-32810
    callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no234_13', 4)	# 32811-32814
    sprite('no234_13', 2)	# 32815-32816
    callSubroutine('NoelComboDeriveClear')
    sprite('no234_14', 5)	# 32817-32821

@State
def con5C_Middle():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(90)
        AttackP2(75)
        HitOverhead(2)
        Unknown9190(1)
        Unknown9118(70)
        AirPushbackX(6500)
        AirPushbackY(-35000)
        AirUntechableTime(40)
        YImpluseBeforeWallbounce(0)
        PushbackX(12000)
        GroundedHitstunAnimation(1)
        Unknown2004(1, 0)
        callSubroutine('NoelComboHasei')
    sprite('no283_00', 2)	# 1-2
    SFX_3('nose_07')
    teleportRelativeX(-50000)
    sprite('no283_01', 2)	# 3-4
    sprite('no283_02', 8)	# 5-12
    sprite('no283_03', 1)	# 13-13
    callSubroutine('NoelComboDeriveInputBegin')
    Unknown14074('con5C_Middle')
    sprite('no283_04', 1)	# 14-14
    SFX_0('006_swing_blade_1')
    sprite('no283_05', 1)	# 15-15
    sprite('no283_06', 3)	# 16-18	 **attackbox here**
    Unknown8004(0, 1, 1)
    ScreenShake(0, 5000)
    sprite('no283_07', 3)	# 19-21
    sprite('no283_08', 3)	# 22-24
    sprite('no283_09', 5)	# 25-29
    callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no283_10', 4)	# 30-33
    sprite('no283_10ex01', 5)	# 34-38
    callSubroutine('NoelComboDeriveClear')
    sprite('no283_11', 7)	# 39-45

@State
def con2C_Low():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2018(0, 50)
        AttackLevel_(3)
        Damage(1200)
        AttackP1(90)
        AttackP2(75)
        PushbackX(20000)
        AirPushbackY(22000)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(34)
        callSubroutine('NoelComboHasei')
    sprite('no402_00', 2)	# 1-2
    sprite('no402_01', 2)	# 3-4
    physicsXImpulse(12000)
    Unknown1028(-400)
    SFX_3('nose_07')
    SFX_0('001_airbackdash_0')
    sprite('no290_07', 2)	# 5-6
    sprite('no290_08', 3)	# 7-9
    Unknown1028(0)
    sprite('no290_09', 3)	# 10-12
    sprite('no290_10', 3)	# 13-15
    callSubroutine('NoelComboDeriveInputBegin')
    Unknown14074('con2C_Low')
    Unknown18009(1)
    setInvincible(1)
    Unknown22019('0000000001000000000000000000000000000000')
    sprite('no290_11', 2)	# 16-17
    sprite('no290_12', 2)	# 18-19
    RefreshMultihit()
    SFX_0('006_swing_blade_2')
    sprite('no290_13', 2)	# 20-21
    sprite('no290_14', 4)	# 22-25	 **attackbox here**
    sprite('no290_14', 3)	# 26-28	 **attackbox here**
    physicsXImpulse(0)
    sprite('no290_15', 5)	# 29-33
    callSubroutine('NoelComboDeriveTimingBegin')
    sprite('no290_16', 7)	# 34-40
    setInvincible(0)
    sprite('no290_17', 7)	# 41-47
    Unknown18009(0)
    callSubroutine('NoelComboDeriveClear')
    sprite('no290_18', 6)	# 48-53

@State
def con_Finish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('NoelComboFinish')
        AttackLevel_(5)
        Unknown11092(1)
        GroundedHitstunAnimation(2)
        AirPushbackX(16000)
        AirPushbackY(6000)
        YImpluseBeforeWallbounce(1000)
        Hitstop(16)
        Damage(1000)
        Unknown2004(1, 0)
    sprite('no286_00', 2)	# 1-2
    sprite('no286_01', 1)	# 3-3
    sprite('no286_02', 1)	# 4-4
    sprite('no286_03', 1)	# 5-5
    Unknown7006('bno204_0', 100, 846163554, 828322864, 0, 0, 100, 846163554, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('no286_04', 3)	# 6-8
    sprite('no286_05', 2)	# 9-10
    sprite('no286_06', 2)	# 11-12	 **attackbox here**
    SFX_0('006_swing_blade_1')
    sprite('no286_07', 2)	# 13-14
    sprite('no286_08', 2)	# 15-16
    sprite('no286_09', 2)	# 17-18
    sprite('no286_10', 1)	# 19-19	 **attackbox here**
    StartMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 1)
    GFX_0('EFF_LongFireTypeC', 0)
    Unknown36(1)
    Unknown1064(1200)
    Unknown35()
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    sprite('no286_10', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    Unknown9018(1)
    Unknown9346(1)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(1000)
    YImpluseBeforeWallbounce(100)
    Hitstop(0)
    ProjectileDurabilityLvl(1)
    Damage(1700)
    AirUntechableTime(50)
    AirHitstunAfterWallbounce(50)
    WallbounceReboundTime(0)
    Unknown9346(0)
    sprite('no286_10', 2)	# 22-23	 **attackbox here**
    sprite('no286_10', 2)	# 24-25	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('no286_10', 2)	# 26-27	 **attackbox here**
    sprite('no286_10', 21)	# 28-48	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('no286_11', 5)	# 49-53
    SFX_3('nose_01')
    sprite('no286_12', 3)	# 54-56

@State
def Reload():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2001()
    sprite('no350_00', 2)	# 1-2
    sprite('no350_01', 2)	# 3-4
    sprite('no350_02', 2)	# 5-6
    sprite('no350_03', 2)	# 7-8
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no350_04', 2)	# 9-10
    sprite('no350_05', 2)	# 11-12
    SFX_3('nose_01')
    sprite('no350_06', 2)	# 13-14
    sprite('no350_07', 2)	# 15-16
    loopRest()

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2250)
        AirPushbackX(10000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        sendToLabelUpon(2, 3)
        callSubroutine('SpecialBeginCancel')
    sprite('no289_00', 3)	# 1-3
    sprite('no289_01', 2)	# 4-5
    SFX_0('005_swing_grap_2_1')
    sprite('no289_02', 4)	# 6-9
    sprite('no289_03', 1)	# 10-10	 **attackbox here**
    GFX_0('noef_samaso', 0)
    Unknown7006('bno205_0', 100, 846163554, 828323120, 0, 0, 100, 846163554, 845100336, 0, 0, 100, 0, 0, 0, 0, 0)
    ScreenShake(0, 8000)
    sprite('no289_03', 2)	# 11-12	 **attackbox here**
    physicsXImpulse(6000)
    physicsYImpulse(26000)
    setGravity(1800)
    sprite('no289_03', 4)	# 13-16	 **attackbox here**
    setInvincible(0)
    sprite('no289_04', 2)	# 17-18
    sprite('no289_05', 4)	# 19-22
    sprite('no289_06', 4)	# 23-26
    sprite('no289_07', 4)	# 27-30
    sprite('no289_08', 90)	# 31-120
    label(3)
    sprite('no289_09', 4)	# 121-124
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    Unknown1045(0)
    sprite('no289_10', 6)	# 125-130
    sprite('no289_11', 5)	# 131-135
    sprite('no289_12', 5)	# 136-140

@State
def Special236A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SpecialBeginCancel')
    sprite('no202_00', 2)	# 1-2
    sprite('no202_01', 1)	# 3-3
    sprite('no202_01', 1)	# 4-4
    SFX_3('nose_01')
    Unknown7006('bno200_0', 100, 846163554, 828321840, 0, 0, 100, 846163554, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('no202_02', 2)	# 5-6
    sprite('no202_03', 2)	# 7-8
    sprite('no202_04', 2)	# 9-10
    sprite('no202_05', 2)	# 11-12
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no202_06', 7)	# 13-19
    SFX_3('nose_00')
    GFX_0('BLT', 0)
    GFX_0('noef_MagicShot', 2)
    GFX_0('DIST_NO2', 2)
    GFX_0('EFF_TargetA', 1)
    GFX_0('DIST_NO', 1)
    ScreenShake(0, 5000)
    sprite('no202_07', 5)	# 20-24
    sprite('no202_08', 5)	# 25-29
    sprite('no202_09', 6)	# 30-35
    Recovery()
    sprite('no202_10', 6)	# 36-41
    sprite('no202_11', 4)	# 42-45
    sprite('no202_12', 4)	# 46-49

@State
def Special236B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SpecialBeginCancel')
    sprite('no202_00', 2)	# 1-2
    sprite('no202_01', 1)	# 3-3
    sprite('no202_01', 1)	# 4-4
    SFX_3('nose_01')
    Unknown7006('bno200_0', 100, 846163554, 828321840, 0, 0, 100, 846163554, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('no202_02', 2)	# 5-6
    sprite('no202_03', 2)	# 7-8
    sprite('no202_04', 2)	# 9-10
    sprite('no202_05', 3)	# 11-13
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no202_06', 5)	# 14-18
    SFX_3('nose_00')
    GFX_0('BLT', 0)
    GFX_0('noef_MagicShot', 2)
    GFX_0('DIST_NO2', 2)
    GFX_0('EFF_TargetB', 1)
    GFX_0('DIST_NO', 1)
    ScreenShake(0, 5000)
    sprite('no202_07', 6)	# 19-24
    sprite('no202_08', 6)	# 25-30
    sprite('no202_09', 7)	# 31-37
    Recovery()
    sprite('no202_10', 7)	# 38-44
    sprite('no202_11', 5)	# 45-49
    sprite('no202_12', 5)	# 50-54

@State
def SpecialThrow():

    def upon_IMMEDIATE():
        Unknown17011('SpecialThrowExe', 2, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11045(1)
        Unknown11002(-1)
        Unknown11061(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown30061(0)
        sendToLabelUpon(2, 1)
        callSubroutine('SpecialBeginCancel')
    sprite('no405_00', 3)	# 1-3
    sprite('no405_00', 1)	# 4-4
    sprite('no405_01', 3)	# 5-7
    sprite('no405_02', 3)	# 8-10
    sprite('no405_03', 3)	# 11-13
    sprite('no405_04', 2)	# 14-15
    sprite('no405_05', 3)	# 16-18
    physicsXImpulse(18000)
    physicsYImpulse(20000)
    setGravity(1600)
    Unknown7006('bno203_0', 100, 846163554, 828322608, 0, 0, 100, 846163554, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown8001(0, 0)
    SFX_0('000_airdash_0')
    sprite('no405_06', 3)	# 19-21
    sprite('no405_07', 3)	# 22-24
    sprite('no405_08', 2)	# 25-26
    sprite('no405_09', 2)	# 27-28
    sprite('no405_10', 6)	# 29-34	 **attackbox here**
    sprite('no405_20', 3)	# 35-37
    label(0)
    sprite('no405_21', 3)	# 38-40
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no024_01', 4)	# 41-44
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('no024_02', 4)	# 45-48
    sprite('no024_03', 4)	# 49-52
    sprite('no024_04', 4)	# 53-56

@State
def SpecialThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 1, 0)
        Unknown1084(1)
        AttackLevel_(0)
        Damage(2500)
        AttackP2(80)
        MinimumDamagePct(50)
        Unknown11078(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Unknown9310(30)
        Unknown11002(-1)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(1600)
        teleportRelativeY(50000)
        Unknown13021(1)
        Unknown21005(1)
        Unknown11108('03000000')
    sprite('no405_11', 4)	# 1-4
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('no405_12', 4)	# 5-8
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('no405_13', 4)	# 9-12
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('no405_14', 4)	# 13-16
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('no405_15', 4)	# 17-20
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    SFX_0('004_swing_grap_1_2')
    sprite('no405_16', 4)	# 21-24
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('no405_17', 14)	# 25-38	 **attackbox here**
    physicsXImpulse(3000)
    physicsYImpulse(20000)
    setGravity(2000)
    Unknown1007(200000)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000006000000')
    sprite('no405_18', 6)	# 39-44
    sendToLabelUpon(2, 4)
    label(3)
    sprite('no405_19', 4)	# 45-48
    Unknown1039(150)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('no024_01', 3)	# 49-51
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('no024_02', 3)	# 52-54
    sprite('no024_03', 3)	# 55-57
    sprite('no024_04', 3)	# 58-60
    loopRest()
    ExitState()

@State
def FlashHaider():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(230)
        Unknown9310(1)
        Unknown11092(1)
        Unknown11058('0000000000000000010000000000000000000000')
        Hitstop(0)
        AirPushbackX(3000)
        AirPushbackY(-50000)
        PushbackX(4000)
        SLOT_51 = 5
        callSubroutine('SpecialBeginCancel')
    sprite('no330_00', 2)	# 1-2
    sprite('no330_01', 2)	# 3-4
    sprite('no330_02', 2)	# 5-6
    sprite('no330_03', 3)	# 7-9
    tag_voice(1, 'bno306_0', 'bno306_1', '', '')
    label(0)
    sprite('no330_04', 4)	# 10-13
    sprite('no330_05ex00', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 2)
    Unknown36(1)
    Unknown1077(80000, 40000)
    Unknown35()
    GFX_0('noef_OIUCHI', 1)
    GFX_0('noef_smoke', 1)
    ScreenShake(0, 3000)
    SLOT_51 = (SLOT_51 + (-1))
    sprite('no330_06', 2)	# 16-17	 **attackbox here**
    StartMultihit()
    sprite('no330_05', 2)	# 18-19	 **attackbox here**
    StartMultihit()
    SFX_3('nose_01')
    if CheckInput(0xa):
        if (SLOT_51 > 0):
            sendToLabel(0)
        else:
            enterState('FlashHaider_Finish')
    sprite('no330_06', 3)	# 20-22	 **attackbox here**
    Recovery()
    StartMultihit()
    sprite('no330_10', 8)	# 23-30
    sprite('no330_11', 6)	# 31-36
    loopRest()

@State
def FlashHaider_Finish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(1000)
        Unknown11058('0000000000000000010000000000000000000000')
        AttackP2(100)
        Hitstop(6)
        AirPushbackY(-30000)
        AirUntechableTime(38)
        Unknown9190(1)
        GroundedHitstunAnimation(1)
        Unknown30068(1)
    sprite('no330_07', 4)	# 1-4
    tag_voice(0, 'bno108_1', 'bno108_2', '', '')
    sprite('no330_08ex00', 4)	# 5-8	 **attackbox here**
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 2)
    Unknown36(1)
    Unknown1077(80000, 40000)
    Unknown35()
    GFX_0('noef_OIUCHI', 1)
    GFX_0('noef_smoke', 1)
    ScreenShake(0, 5000)
    sprite('no330_09', 11)	# 9-19	 **attackbox here**
    StartMultihit()
    SFX_3('nose_01')
    Recovery()
    sprite('no330_10', 8)	# 20-27
    sprite('no330_11', 7)	# 28-34

@State
def BloomTrigger():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Unknown30065(0)
        GroundedHitstunAnimation(2)
        AirPushbackX(16000)
        AirPushbackY(6000)
        YImpluseBeforeWallbounce(1000)
        Hitstop(16)
        AttackP1(80)
        Unknown11092(1)
        Damage(900)
        Unknown2004(1, 0)
        MinimumDamagePct(10)
        callSubroutine('SpecialBeginCancel')
    sprite('no286_00', 2)	# 1-2
    sprite('no286_01', 1)	# 3-3
    sprite('no286_02', 1)	# 4-4
    sprite('no286_03', 1)	# 5-5
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown7006('bno204_0', 100, 862940770, 12594, 0, 0, 100, 846163554, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('no286_04', 2)	# 6-7
    sprite('no286_05', 1)	# 8-8
    sprite('no286_06', 2)	# 9-10	 **attackbox here**
    SFX_0('006_swing_blade_1')
    sprite('no286_07', 2)	# 11-12
    sprite('no286_08', 2)	# 13-14
    sprite('no286_09', 2)	# 15-16
    sprite('no286_10', 1)	# 17-17	 **attackbox here**
    StartMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 1)
    GFX_0('EFF_LongFireTypeC', 0)
    Unknown36(1)
    Unknown1064(1200)
    Unknown35()
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    sprite('no286_10', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    Unknown9018(1)
    Unknown9346(1)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(500)
    YImpluseBeforeWallbounce(100)
    Hitstop(0)
    ProjectileDurabilityLvl(1)
    AirUntechableTime(50)
    AirHitstunAfterWallbounce(50)
    Unknown30056('c8af00003200000000000000')
    WallbounceReboundTime(0)
    Unknown9346(0)
    Hitstop(1)
    Damage(900)
    Unknown9017(1)
    sprite('no286_10', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    sprite('no286_10', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('no286_10', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    sprite('no286_10', 15)	# 26-40	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('no286_11', 5)	# 41-45
    SFX_3('nose_01')
    sprite('no286_12', 3)	# 46-48

@State
def AssaultThrough():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(80)
        AttackP2(80)
        Unknown30065(0)
        AirPushbackX(60000)
        AirPushbackY(20000)
        PushbackX(19800)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(27)
        WallbounceReboundTime(5)
        AirHitstunAfterWallbounce(50)
        Unknown9202(15)
        Unknown11056(0)
        Unknown13021(1)
        Unknown21005(1)
        MinimumDamagePct(10)
        callSubroutine('SpecialBeginCancel')
    sprite('no287_00', 3)	# 1-3
    EnableCollision(0)
    sprite('no287_01', 3)	# 4-6
    physicsXImpulse(34000)
    SFX_0('000_airdash_0')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(4)
    Unknown3070(1)
    Unknown3074('00000000000000000000000080000000')
    Unknown3075('00000000000000002000000040000000')
    Unknown3072('ff000000200000002000000020000000')
    Unknown3073('500000000a0000000a0000000a000000')
    Unknown3076(1010)
    Unknown3077(1010)
    sprite('no287_02', 3)	# 7-9
    setInvincible(1)
    Unknown7006('bno206_0', 100, 846163554, 828323376, 0, 0, 100, 846163554, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('no287_03', 3)	# 10-12
    sprite('no287_04', 3)	# 13-15
    sprite('no287_05', 3)	# 16-18
    Unknown1019(80)
    sprite('no287_06', 4)	# 19-22
    setInvincible(0)
    EnableCollision(1)
    Unknown2006()
    physicsXImpulse(0)
    sprite('no287_07', 4)	# 23-26
    sprite('no287_08', 4)	# 27-30
    sprite('no287_09', 9)	# 31-39	 **attackbox here**
    physicsXImpulse(57600)
    SFX_0('005_swing_grap_2_1')
    sprite('no287_10', 4)	# 40-43
    Recovery()
    physicsXImpulse(0)
    sprite('no287_11', 4)	# 44-47
    sprite('no287_12', 4)	# 48-51
    sprite('no287_13', 4)	# 52-55

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2000)
        AttackP1(80)
        AttackP2(100)
        AirUntechableTime(50)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9142(36)
        Unknown2004(1, 0)
        Unknown11072(1, 300000, 0)
        PushbackX(29800)
        SLOT_62 = 0

        def upon_78():
            SLOT_62 = 1
            GuardPoint_(0)
            Unknown2021(1)
            ScreenShake(40000, 5000)
            Unknown13024(0)
            Unknown11069('MajuShotObj')
        Unknown11056(2)
        setInvincible(1)
        GuardPoint_(1)
        Unknown11064(1)
        callSubroutine('SpecialBeginCancel')
    sprite('no431_00', 5)	# 1-5
    Unknown2036(28, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    tag_voice(1, 'bno250_0', 'bno250_1', '', '')
    Unknown30080('')
    sprite('no431_01', 4)	# 6-9
    GFX_0('noef431gun_del', -1)
    SFX_3('nose_21')
    sprite('no431_02', 5)	# 10-14
    GFX_0('noef431gtlptc_make', 0)
    sprite('no431_03', 5)	# 15-19
    GFX_0('noef431gtl_make', -1)
    sprite('no431_04', 5)	# 20-24
    sprite('no431_05', 7)	# 25-31
    sprite('no431_06', 2)	# 32-33
    sprite('no431_07ex01', 5)	# 34-38	 **attackbox here**
    SFX_0('006_swing_blade_1')
    sprite('no431_08', 5)	# 39-43
    SFX_3('nose_03')
    if (not SLOT_62):
        setInvincible(0)
    sprite('no431_09', 5)	# 44-48
    SFX_3('nose_03')
    sprite('no431_10', 5)	# 49-53
    SFX_3('nose_03')
    sprite('no431_11', 3)	# 54-56
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_11', 3)	# 57-59
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_12', 3)	# 60-62
    tag_voice(0, 'bno251_0', 'bno251_1', '', '')
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_12', 3)	# 63-65
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_13', 3)	# 66-68
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_13', 3)	# 69-71
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 2400)
    Unknown1072(-2400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_14', 3)	# 72-74
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 4800)
    Unknown1072(-4800)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_14', 3)	# 75-77
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 7200)
    Unknown1072(-7200)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_15', 3)	# 78-80
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 9600)
    Unknown1072(-9600)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_15', 3)	# 81-83
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 12000)
    Unknown1072(-12000)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_16', 3)	# 84-86
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 14400)
    Unknown1072(-14400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_16', 3)	# 87-89
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 16800)
    Unknown1072(-16800)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_17', 3)	# 90-92
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 19200)
    Unknown1072(-19200)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_17', 3)	# 93-95
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 21600)
    Unknown1072(-21600)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 96-98
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 24000)
    Unknown1072(-24000)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 99-101
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    if SLOT_62:
        Unknown23029(1, 4311, 0)
    GFX_1('ef_hits', 0)
    loopRest()
    if SLOT_62:
        _gotolabel(777)
    sprite('no431_18', 3)	# 102-104
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 105-107
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 108-110
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 111-113
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 114-116
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 117-119
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 120-122
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 123-125
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObj', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    label(777)
    sprite('no431_19', 8)	# 126-133
    sprite('no431_20', 7)	# 134-140
    sprite('no431_21', 6)	# 141-146
    GFX_0('no431_gun', 0)
    loopRest()
    if SLOT_62:
        gotoLabel(0)
    sprite('no431_41', 6)	# 147-152
    SFX_0('022_magiccircle_b')
    GFX_0('noef600ptc_L', 0)
    GFX_0('noef600ptc_R', 1)
    sprite('no431_42', 6)	# 153-158
    sprite('no431_43', 6)	# 159-164
    sprite('no431_44', 6)	# 165-170
    sprite('no431_45', 6)	# 171-176
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(78)
    sprite('no431_22', 3)	# 177-179
    sprite('no431_22', 1)	# 180-180
    sprite('no431_23', 30)	# 181-210
    Unknown2036(100, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown20000(1)
    GFX_0('noef431gun_make', -1)
    sprite('no431_24', 4)	# 211-214
    sprite('no431_25', 4)	# 215-218
    sprite('no431_26', 4)	# 219-222
    ScreenShake(0, 1000)
    sprite('no431_27', 2)	# 223-224	 **attackbox here**
    ScreenShake(0, 1000)
    tag_voice(0, 'bno252_0', 'bno252_1', '', '')
    sprite('no431_28', 2)	# 225-226	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex01', 2)	# 227-228	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('MajuMagicCircle', 2)
    GFX_1('noef_431_charge', 2)
    SFX_3('nose_05')
    sprite('no431_28ex01', 2)	# 229-230	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex02', 2)	# 231-232	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex02', 2)	# 233-234	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex03', 2)	# 235-236	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex03', 2)	# 237-238	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex04', 2)	# 239-240	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex04', 2)	# 241-242	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex05', 2)	# 243-244	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex05', 2)	# 245-246	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex06', 2)	# 247-248	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex06', 2)	# 249-250	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex07', 2)	# 251-252	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 253-254	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 255-256	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 257-258	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 259-260	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 261-262	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 263-264	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 265-266	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 267-268	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 269-270	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 271-272	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 273-274	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 275-276	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 277-278	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 279-280	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 281-282	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 283-284	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 285-286	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 287-288	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 289-290	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 291-292	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 293-294	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 295-296	 **attackbox here**
    ScreenShake(0, 5000)
    RefreshMultihit()
    Unknown11034(0)
    ProjectileDurabilityLvl(2)
    Unknown11058('0000000000000000000000000100000000000000')
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(50000)
    AirPushbackY(55000)
    YImpluseBeforeWallbounce(3000)
    Hitstop(0)
    Damage(4100)
    AttackP2(60)
    MinimumDamagePct(25)
    AirUntechableTime(120)
    Unknown9190(1)
    Unknown9118(15)
    Unknown11072(0, 0, 0)
    Unknown23159('maju_Finish')
    ScreenShake(0, 10000)
    Unknown11069('')
    Unknown11064(0)
    sprite('no431_27ex08', 2)	# 297-298	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('ModelBeam', 2)
    SFX_3('nose_06')
    SFX_3('nose_06')
    sprite('no431_28ex07', 2)	# 299-300	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_29', 5)	# 301-305	 **attackbox here**
    sprite('no431_30', 5)	# 306-310
    sprite('no431_31', 4)	# 311-314
    sprite('no431_32', 4)	# 315-318
    sprite('no431_33', 4)	# 319-322
    sprite('no431_34', 4)	# 323-326
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_35', 4)	# 327-330
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_36', 4)	# 331-334
    Unknown20000(0)
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_37', 4)	# 335-338
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_38', 8)	# 339-346
    sprite('no431_39', 8)	# 347-354
    Unknown13024(1)
    sprite('no431_40', 6)	# 355-360
    loopRest()
    ExitState()

@State
def UltimateShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2000)
        AttackP1(80)
        AttackP2(100)
        AirUntechableTime(50)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9142(36)
        Unknown2004(1, 0)
        Unknown11072(1, 300000, 0)
        PushbackX(34800)
        SLOT_62 = 0

        def upon_78():
            Unknown13024(0)
            SLOT_62 = 1
            GuardPoint_(0)
            Unknown2021(1)
            ScreenShake(40000, 5000)
            Unknown11069('MajuShotObjOD')
        Unknown11056(2)
        setInvincible(1)
        GuardPoint_(1)
        Unknown11064(1)
        callSubroutine('SpecialBeginCancel')
    sprite('no431_00', 5)	# 1-5
    Unknown2036(28, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    tag_voice(1, 'bno250_0', 'bno250_1', '', '')
    Unknown30080('')
    sprite('no431_01', 4)	# 6-9
    GFX_0('noef431gun_del', -1)
    SFX_3('nose_21')
    sprite('no431_02', 5)	# 10-14
    GFX_0('noef431gtlptc_make', 0)
    sprite('no431_03', 5)	# 15-19
    GFX_0('noef431gtl_make', -1)
    sprite('no431_04', 5)	# 20-24
    sprite('no431_05', 7)	# 25-31
    sprite('no431_06', 2)	# 32-33
    sprite('no431_07ex01', 5)	# 34-38	 **attackbox here**
    SFX_0('006_swing_blade_1')
    sprite('no431_08', 5)	# 39-43
    SFX_3('nose_03')
    if (not SLOT_62):
        setInvincible(0)
    sprite('no431_09', 5)	# 44-48
    SFX_3('nose_03')
    sprite('no431_10', 5)	# 49-53
    SFX_3('nose_03')
    sprite('no431_11', 3)	# 54-56
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_11', 3)	# 57-59
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_12', 3)	# 60-62
    tag_voice(0, 'bno251_0', 'bno251_1', '', '')
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_12', 3)	# 63-65
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_13', 3)	# 66-68
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 0)
    Unknown1072(0)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_13', 3)	# 69-71
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 2400)
    Unknown1072(-2400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_14', 3)	# 72-74
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 4800)
    Unknown1072(-4800)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_14', 3)	# 75-77
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 7200)
    Unknown1072(-7200)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_15', 3)	# 78-80
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 9600)
    Unknown1072(-9600)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_15', 3)	# 81-83
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 12000)
    Unknown1072(-12000)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_16', 3)	# 84-86
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 14400)
    Unknown1072(-14400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_16', 3)	# 87-89
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 16800)
    Unknown1072(-16800)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_17', 3)	# 90-92
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 19200)
    Unknown1072(-19200)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_17', 3)	# 93-95
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 21600)
    Unknown1072(-21600)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 96-98
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 24000)
    Unknown1072(-24000)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 99-101
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    if SLOT_62:
        Unknown23029(1, 4311, 0)
    GFX_1('ef_hits', 0)
    loopRest()
    if SLOT_62:
        _gotolabel(777)
    sprite('no431_18', 3)	# 102-104
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 105-107
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 108-110
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 111-113
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 114-116
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 117-119
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 120-122
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    sprite('no431_18', 3)	# 123-125
    SFX_3('nose_23')
    GFX_0('BLT', 1)
    ScreenShake(10000, 0)
    GFX_0('MajuShotObjOD', 0)
    Unknown36(1)
    Unknown1109(175000, 26400)
    Unknown1072(-26400)
    Unknown35()
    GFX_1('ef_hits', 0)
    label(777)
    sprite('no431_19', 8)	# 126-133
    sprite('no431_20', 7)	# 134-140
    sprite('no431_21', 6)	# 141-146
    GFX_0('no431_gun', 0)
    loopRest()
    if SLOT_62:
        gotoLabel(0)
    sprite('no431_41', 6)	# 147-152
    SFX_0('022_magiccircle_b')
    GFX_0('noef600ptc_L', 0)
    GFX_0('noef600ptc_R', 1)
    sprite('no431_42', 6)	# 153-158
    sprite('no431_43', 6)	# 159-164
    sprite('no431_44', 6)	# 165-170
    sprite('no431_45', 6)	# 171-176
    loopRest()
    ExitState()
    label(0)
    clearUponHandler(78)
    sprite('no431_22', 3)	# 177-179
    sprite('no431_22', 1)	# 180-180
    sprite('no431_23', 30)	# 181-210
    Unknown2036(36, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown20000(1)
    GFX_0('noef431gun_make', -1)
    sprite('no431_24', 4)	# 211-214
    sprite('no431_25', 4)	# 215-218
    sprite('no431_26', 4)	# 219-222
    ScreenShake(0, 1000)
    sprite('no431_27', 3)	# 223-225	 **attackbox here**
    sprite('no431_28SP', 3)	# 226-228	 **attackbox here**
    SLOT_52 = 15
    label(101)
    sprite('no431_27', 2)	# 229-230	 **attackbox here**
    ScreenShake(1000, 5000)
    GFX_0('EFF_SakuretsuNear', 0)
    sprite('no431_28SP', 1)	# 231-231	 **attackbox here**
    ScreenShake(5000, 1000)
    GFX_0('BLT', 1)
    GFX_0('MajuShotObj_Tsuika', 1)
    if (not SLOT_52):
        Unknown23029(1, 4311, 0)
    sprite('no431_28SP', 1)	# 232-232	 **attackbox here**
    SLOT_52 = (SLOT_52 + (-1))
    Unknown19(102, 2, 52)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('no431_27', 2)	# 233-234	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28SP', 2)	# 235-236	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27', 2)	# 237-238	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28SP', 2)	# 239-240	 **attackbox here**
    ScreenShake(0, 1000)
    Unknown2036(45, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown20000(1)
    sprite('no431_27', 2)	# 241-242	 **attackbox here**
    ScreenShake(0, 1000)
    tag_voice(0, 'bno252_0', 'bno252_1', '', '')
    sprite('no431_28', 2)	# 243-244	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex01', 2)	# 245-246	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('MajuMagicCircle', 2)
    GFX_1('noef_431_charge', 2)
    SFX_3('nose_05')
    sprite('no431_28ex01', 2)	# 247-248	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex02', 2)	# 249-250	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex02', 2)	# 251-252	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex03', 2)	# 253-254	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex03', 2)	# 255-256	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex04', 2)	# 257-258	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex04', 2)	# 259-260	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex05', 2)	# 261-262	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex05', 2)	# 263-264	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex06', 2)	# 265-266	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex06', 2)	# 267-268	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex07', 2)	# 269-270	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 271-272	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 273-274	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 275-276	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 277-278	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 279-280	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 281-282	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 283-284	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 285-286	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 287-288	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 289-290	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 291-292	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 293-294	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 295-296	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 297-298	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 299-300	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 301-302	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 303-304	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 305-306	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 307-308	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 309-310	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 311-312	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 313-314	 **attackbox here**
    ScreenShake(0, 5000)
    RefreshMultihit()
    Unknown11034(0)
    ProjectileDurabilityLvl(2)
    Unknown11058('0000000000000000000000000100000000000000')
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(35000)
    AirPushbackY(43500)
    YImpluseBeforeWallbounce(3000)
    Hitstop(0)
    Damage(4100)
    AttackP2(60)
    MinimumDamagePct(22)
    AirUntechableTime(120)
    Unknown9190(1)
    Unknown9118(15)
    Unknown11072(0, 0, 0)
    Unknown23159('majuOD_Finish')
    ScreenShake(0, 10000)
    Unknown11064(0)
    Unknown11069('')
    sprite('no431_27ex08', 2)	# 315-316	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('ModelBeam', 2)
    SFX_3('nose_06')
    SFX_3('nose_06')
    sprite('no431_28ex07', 2)	# 317-318	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_29', 5)	# 319-323	 **attackbox here**
    sprite('no431_30', 5)	# 324-328
    sprite('no431_31', 4)	# 329-332
    sprite('no431_32', 4)	# 333-336
    sprite('no431_33', 4)	# 337-340
    sprite('no431_34', 4)	# 341-344
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_35', 4)	# 345-348
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_36', 4)	# 349-352
    Unknown20000(0)
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_37', 4)	# 353-356
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_38', 8)	# 357-364
    sprite('no431_39', 8)	# 365-372
    Unknown13024(1)
    sprite('no431_40', 6)	# 373-378
    loopRest()
    ExitState()

@State
def UltimateAirShot():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown1019(60)
                YAccel(60)
        setInvincible(1)
        Unknown1084(1)
        Unknown13024(1)
        Unknown2064(0)

        def upon_43():
            Unknown2064(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        callSubroutine('SpecialBeginCancel')
    sprite('no430_00', 3)	# 1-3
    sprite('no430_00', 3)	# 4-6
    Unknown2036(21, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown1084(1)
    tag_voice(1, 'bno253_0', 'bno253_1', '', '')
    sprite('no430_00', 6)	# 7-12
    Unknown1015(-5000)
    Unknown1021(24000)
    setGravity(1300)
    sprite('no430_01', 6)	# 13-18
    sprite('no430_02', 6)	# 19-24
    setInvincible(0)
    sprite('no430_03', 6)	# 25-30
    Unknown2037(1)
    sprite('no430_04', 2)	# 31-32
    setGravity(0)
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 33-34
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 35-36
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 37-38
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 39-40
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 41-42
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 43-44
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 45-46
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 47-48
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 49-50
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 51-52
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 53-54
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 55-56
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 57-58
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 59-60
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 61-62
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 63-64
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 65-66
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 1)	# 67-67
    SFX_3('nose_01')
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObj', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_06', 1)	# 68-68
    sprite('no430_07', 3)	# 69-71
    Unknown2037(0)
    sprite('no430_07', 3)	# 72-74
    sprite('no430_08', 3)	# 75-77
    Unknown3029(1)
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    setGravity(800)
    sprite('no430_09', 3)	# 78-80
    sprite('no430_10', 3)	# 81-83
    GFX_0('noef430bzk_make', 0)
    SFX_0('022_magiccircle_a')
    sprite('no430_11', 3)	# 84-86
    sprite('no430_12', 3)	# 87-89
    sprite('no430_13', 3)	# 90-92
    sprite('no430_14', 3)	# 93-95
    tag_voice(0, 'bno254_0', 'bno254_1', '', '')
    sprite('no430_15', 12)	# 96-107
    sprite('no430_16', 5)	# 108-112
    teleportRelativeX(-56000)
    Unknown1007(8000)
    physicsXImpulse(-32000)
    physicsYImpulse(24000)
    GFX_0('noef430bzk_rocket', 0)
    GFX_0('noef430bzk_fire', 1)
    SFX_3('nose_25')
    SFX_3('nose_25')
    sprite('no430_17', 4)	# 113-116
    sprite('no430_18', 4)	# 117-120
    setGravity(300)
    sprite('no430_19', 4)	# 121-124
    sprite('no430_20', 4)	# 125-128
    sprite('no430_21', 4)	# 129-132
    sprite('no430_22', 4)	# 133-136
    physicsXImpulse(-16000)
    Unknown1043()
    sprite('no430_23', 4)	# 137-140
    label(0)
    sprite('no022_07', 3)	# 141-143
    sprite('no022_08', 3)	# 144-146
    sprite('no022_07', 3)	# 147-149
    sprite('no022_08', 3)	# 150-152
    sprite('no022_07', 3)	# 153-155
    sprite('no022_08', 3)	# 156-158
    gotoLabel(0)
    label(1)
    sprite('no024_01', 3)	# 159-161
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('no024_02', 15)	# 162-176
    sprite('no024_03', 3)	# 177-179
    sprite('no024_04', 3)	# 180-182

@State
def UltimateAirShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown1019(60)
                YAccel(60)
        setInvincible(1)
        Unknown1084(1)
        Unknown2064(0)

        def upon_43():
            Unknown2064(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown13024(1)
        callSubroutine('SpecialBeginCancel')
    sprite('no430_00', 3)	# 1-3
    sprite('no430_00', 3)	# 4-6
    Unknown2036(21, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    Unknown1084(1)
    Unknown30080('')
    tag_voice(1, 'bno253_0', 'bno253_1', '', '')
    sprite('no430_00', 6)	# 7-12
    Unknown1015(-5000)
    Unknown1021(24000)
    setGravity(1300)
    sprite('no430_01', 6)	# 13-18
    sprite('no430_02', 6)	# 19-24
    setInvincible(0)
    sprite('no430_03', 6)	# 25-30
    Unknown2037(1)
    sprite('no430_04', 2)	# 31-32
    setGravity(0)
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 33-34
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 35-36
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 37-38
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 39-40
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 41-42
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 43-44
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 45-46
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 47-48
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 49-50
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 51-52
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 53-54
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 55-56
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 57-58
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 59-60
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 61-62
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 63-64
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 65-66
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 1)	# 67-67
    SFX_3('nose_01')
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_06', 1)	# 68-68
    sprite('no430_05', 2)	# 69-70
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 71-72
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 73-74
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 75-76
    SFX_3('nose_01')
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 77-78
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 79-80
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 81-82
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_06', 2)	# 83-84
    SFX_3('nose_01')
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_05', 2)	# 85-86
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no430_04', 2)	# 87-88
    Unknown1015(-10000)
    Unknown1021(10000)
    GFX_0('RanshaShotObjOD', 0)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_1('ef_hits', 0)
    sprite('no430_07', 3)	# 89-91
    Unknown2037(0)
    sprite('no430_07', 3)	# 92-94
    sprite('no430_08', 3)	# 95-97
    Unknown3029(1)
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    setGravity(800)
    sprite('no430_09', 3)	# 98-100
    sprite('no430_10', 3)	# 101-103
    GFX_0('noef430bzk_make', 0)
    SFX_0('022_magiccircle_a')
    sprite('no430_11', 3)	# 104-106
    sprite('no430_12ex', 3)	# 107-109
    sprite('no430_13ex', 3)	# 110-112
    sprite('no430_14ex', 3)	# 113-115
    tag_voice(0, 'bno254_0', 'bno254_1', '', '')
    sprite('no430_15ex', 12)	# 116-127
    sprite('no430_16', 5)	# 128-132
    teleportRelativeX(-56000)
    Unknown1007(8000)
    physicsXImpulse(-32000)
    physicsYImpulse(24000)
    GFX_0('noef430bzk_rocket_OD', 0)
    GFX_0('noef430bzk_fire', 1)
    SFX_3('nose_25')
    SFX_3('nose_25')
    sprite('no430_17', 4)	# 133-136
    sprite('no430_18', 4)	# 137-140
    setGravity(300)
    sprite('no430_19', 4)	# 141-144
    sprite('no430_20', 4)	# 145-148
    sprite('no430_21', 4)	# 149-152
    sprite('no430_22', 4)	# 153-156
    physicsXImpulse(-16000)
    Unknown1043()
    sprite('no430_23', 4)	# 157-160
    sprite('no022_07', 3)	# 161-163
    sprite('no022_08', 3)	# 164-166
    sprite('no022_07', 3)	# 167-169
    label(0)
    sprite('no022_08', 3)	# 170-172
    sprite('no022_07', 3)	# 173-175
    gotoLabel(0)
    label(1)
    sprite('no024_01', 3)	# 176-178
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('no024_02', 15)	# 179-193
    sprite('no024_03', 3)	# 194-196
    sprite('no024_04', 3)	# 197-199

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11063(1)
        setInvincible(1)
        AttackLevel_(4)
        Damage(0)
        Unknown11064(1)
        Unknown11057(0)
        Unknown9130(999)
        Unknown9142(999)
        Hitstop(0)
        hitstun(600)
        Unknown11058('0000000001000000000000000000000000000000')
        ProjectileDurabilityLvl(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown11047('CmnActVDownCrash')
        Unknown11084(1)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        Unknown11042(1)
        Unknown30048(1)

        def upon_78():
            Unknown11080(1)
            enterState('AstralHeatExe')
            Unknown2038(1)
    sprite('no450_00', 3)	# 1-3
    Unknown1084(1)
    sprite('no450_01', 4)	# 4-7
    sprite('no450_02', 4)	# 8-11
    Unknown2036(74, -1, 2)
    Unknown23147()
    setInvincible(1)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_NO_AH', -1)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(10)
    Unknown3074('0000000000000000ff000000ff000000')
    Unknown3075('00000000ff0000000000000000000000')
    Unknown3076(1000)
    Unknown3077(1300)
    SFX_0('019_quake_0')
    SFX_1('bno290')
    sprite('no450_03', 4)	# 12-15
    sprite('no450_04', 4)	# 16-19
    sprite('no450_02', 4)	# 20-23
    sprite('no450_03', 4)	# 24-27
    sprite('no450_04', 4)	# 28-31
    sprite('no450_02', 4)	# 32-35
    sprite('no450_03', 4)	# 36-39
    sprite('no450_04', 4)	# 40-43
    sprite('no450_02', 4)	# 44-47
    sprite('no450_03', 4)	# 48-51
    sprite('no450_04', 4)	# 52-55
    sprite('no450_02', 4)	# 56-59
    sprite('no450_03', 4)	# 60-63
    sprite('no450_04', 4)	# 64-67
    sprite('no450_02', 4)	# 68-71
    sprite('no450_03', 4)	# 72-75
    sprite('no450_04', 4)	# 76-79
    sprite('no450_05', 4)	# 80-83
    sprite('no450_06', 4)	# 84-87
    sprite('no450_07', 4)	# 88-91
    sprite('no450_08', 4)	# 92-95	 **attackbox here**
    GFX_1('noef_AH_firings', 0)
    GFX_1('noef_AH_mcA', 0)
    GFX_0('BLT', 2)
    ScreenShake(0, 5000)
    SFX_0('005_swing_grap_2_2')
    SFX_0('022_magiccircle_a')
    sprite('no450_07', 5)	# 96-100
    sprite('no450_39', 5)	# 101-105
    Unknown3029(0)
    Unknown11067(0)
    EnableCollision(1)
    Unknown2053(1)
    Unknown2034(1)
    sprite('no450_40', 5)	# 106-110
    setInvincible(0)
    sprite('no450_41', 5)	# 111-115
    sprite('no450_42', 5)	# 116-120
    loopRest()

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11067(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2004(1, 0)
        Unknown11068(1)
        Unknown11078(1)
        MinimumDamagePct(100)
        Unknown2003(1)
        setInvincible(1)
        Unknown23088(1, 1)
        Unknown23157(0)
        Unknown23084(1)
        Unknown23024(3)
        Unknown23025(1)
        Unknown1028(0)
        Unknown20006(1)
        Unknown23022(1)
        Unknown2003(1)
        AttackLevel_(0)
        Damage(800)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(10)
        AirPushbackY(1)
        YImpluseBeforeWallbounce(-2)
        AirUntechableTime(600)
        Hitstop(0)
        AttackP2(70)
        Unknown11064(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
    sprite('no451_02', 40)	# 1-40	 **attackbox here**
    GFX_0('AHatemiAnten', -1)
    Unknown21012('41486174656d694566660000000000000000000000000000000000000000000021000000')
    Unknown23024(2)
    sprite('no451_02', 20)	# 41-60	 **attackbox here**
    Unknown3025(-16777216, 20)
    Unknown36(22)
    Unknown3025(-16777216, 20)
    Unknown51(1)
    Unknown2006()
    Unknown35()
    sprite('no450cutin_00', 1)	# 61-61	 **attackbox here**
    Unknown3038(1)
    GFX_0('AHcamera', -1)
    Unknown20003(1)
    Unknown2006()
    sprite('no450cutin_00', 29)	# 62-90	 **attackbox here**
    Unknown21012('414863616d65726100000000000000000000000000000000000000000000000020000000')
    Unknown1000(-200000)
    Unknown36(22)
    Unknown1000(-200000)
    teleportRelativeY(1800000)
    Unknown35()
    sprite('no450cutin_00', 30)	# 91-120	 **attackbox here**
    Unknown3038(0)
    Unknown3025(-1, 10)
    GFX_1('noef_450_opencut00_addu', 0)
    Unknown21012('4148616e74656e536c6f7700000000000000000000000000000000000000000020000000')
    sprite('no450cutin_00', 40)	# 121-160	 **attackbox here**
    SFX_1('bno291')
    sprite('no450cutin_00', 20)	# 161-180	 **attackbox here**
    GFX_0('AHDaburi', -1)
    sprite('no450cutin_02', 10)	# 181-190	 **attackbox here**
    RefreshMultihit()
    Unknown2003(0)
    SFX_3('nose_27')
    GFX_0('AHmazle', 0)
    GFX_0('AHmazle', 1)
    ScreenShake(5000, 5000)
    sprite('no450cutin_02', 10)	# 191-200	 **attackbox here**
    GFX_0('AHanten', -1)
    sprite('no450cutin_01', 10)	# 201-210	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    GFX_0('AHmazle', 1)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    SFX_1('bno292')
    sprite('no450cutin_01', 10)	# 211-220	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_03', 10)	# 221-230	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_03', 10)	# 231-240	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_04', 8)	# 241-248	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_04', 10)	# 249-258	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_05', 8)	# 259-266	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    GFX_0('AHmazle', 1)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_05', 10)	# 267-276	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_01', 8)	# 277-284	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    GFX_0('AHmazle', 1)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_01', 10)	# 285-294	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_02', 6)	# 295-300	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    Unknown2005()
    GFX_0('AHmazle', 0)
    GFX_0('AHmazle', 1)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_02', 10)	# 301-310	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_03', 4)	# 311-314	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_03', 10)	# 315-324	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_04', 4)	# 325-328	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_04', 10)	# 329-338	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_05', 4)	# 339-342	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    GFX_0('AHmazle', 1)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_05', 10)	# 343-352	 **attackbox here**
    GFX_0('AHanten', -1)
    SFX_3('nose_01')
    sprite('no450cutin_01', 4)	# 353-356	 **attackbox here**
    RefreshMultihit()
    Unknown21012('4148616e74656e0000000000000000000000000000000000000000000000000020000000')
    GFX_0('AHmazle', 0)
    GFX_0('AHmazle', 1)
    ScreenShake(5000, 5000)
    SFX_3('nose_27')
    sprite('no450cutin_01', 25)	# 357-381	 **attackbox here**
    GFX_0('AHantenSlow', 1)
    SFX_3('nose_01')
    sprite('no451_03', 5)	# 382-386
    SFX_0('019_quake_1')
    Unknown2006()
    Unknown3001(255)
    Unknown21012('4148616e74656e536c6f7700000000000000000000000000000000000000000020000000')
    Unknown21012('414863616d65726100000000000000000000000000000000000000000000000021000000')
    Unknown36(22)
    teleportRelativeY(120000)
    Unknown3001(255)
    Unknown35()
    sprite('no451_04', 5)	# 387-391
    sprite('no451_05', 5)	# 392-396
    sprite('no451_03', 5)	# 397-401
    SFX_0('019_quake_1')
    sprite('no451_04', 5)	# 402-406
    SFX_0('019_quake_0')
    sprite('no451_05', 5)	# 407-411
    SFX_0('019_quake_1')
    sprite('no451_03', 5)	# 412-416
    Unknown21012('5370686572654d6167694d61746f6d650000000000000000000000000000000021000000')
    SFX_0('019_quake_0')
    sprite('no451_04', 5)	# 417-421
    SFX_0('019_quake_1')
    sprite('no451_05', 5)	# 422-426
    sprite('no451_03', 5)	# 427-431
    SFX_0('019_quake_1')
    sprite('no451_04', 5)	# 432-436
    SFX_0('019_quake_0')
    sprite('no451_05', 5)	# 437-441
    sprite('no451_03', 5)	# 442-446
    SFX_0('019_quake_0')
    SFX_0('022_magiccircle_b')
    sprite('no451_04', 5)	# 447-451
    SFX_0('019_quake_1')
    sprite('no451_05', 5)	# 452-456
    SFX_0('019_quake_0')
    SFX_0('022_magiccircle_b')
    sprite('no451_03', 5)	# 457-461
    sprite('no451_04', 5)	# 462-466
    SFX_0('019_quake_0')
    SFX_0('022_magiccircle_b')
    sprite('no451_05', 5)	# 467-471
    sprite('no451_03', 5)	# 472-476
    SFX_0('019_quake_0')
    SFX_0('022_magiccircle_b')
    sprite('no451_04', 5)	# 477-481
    SFX_0('019_quake_1')
    SFX_0('022_magiccircle_b')
    sprite('no451_05', 5)	# 482-486
    sprite('no451_06', 6)	# 487-492
    SFX_0('008_swing_pole_1')
    SFX_0('019_quake_1')
    sprite('no451_07', 6)	# 493-498
    SFX_0('008_swing_pole_1')
    SFX_0('019_quake_1')
    sprite('no451_08', 6)	# 499-504
    SFX_0('008_swing_pole_1')
    SFX_0('019_quake_1')
    sprite('no451_09', 6)	# 505-510
    SFX_0('008_swing_pole_1')
    SFX_0('019_quake_1')
    sprite('no451_10', 6)	# 511-516
    SFX_0('019_quake_1')
    sprite('no450_31', 50)	# 517-566
    SFX_1('bno293')
    sprite('no451_11', 6)	# 567-572
    sprite('no450_32', 6)	# 573-578
    Unknown21012('5370686572654d6167694d61746f6d650000000000000000000000000000000020000000')
    sprite('no450_33', 5)	# 579-583	 **attackbox here**
    SFX_0('024_getset_b')
    SFX_0('024_getset_b')
    sprite('no450_34', 5)	# 584-588
    SFX_0('019_quake_1')
    SFX_0('016_explode_2')
    sprite('no450_35', 5)	# 589-593
    sprite('no450_34', 5)	# 594-598
    Unknown23011(1)
    SFX_0('019_quake_1')
    SFX_0('016_explode_2')
    sprite('no450_35', 5)	# 599-603
    Unknown23011(1)
    sprite('no450_34', 5)	# 604-608
    Unknown23011(1)
    SFX_0('019_quake_1')
    SFX_0('016_explode_2')
    sprite('no450_35', 5)	# 609-613
    Unknown23011(2)
    SFX_0('019_quake_1')
    SFX_0('016_explode_2')
    sprite('no450_33', 5)	# 614-618	 **attackbox here**
    Unknown23011(2)
    SFX_0('019_quake_1')
    SFX_0('016_explode_2')
    Unknown2003(0)
    RefreshMultihit()
    SFX_3('nose_00')
    AttackLevel_(4)
    Damage(17520)
    Unknown11064(3)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(100000)
    AirPushbackX(2000)
    AirUntechableTime(270)
    Hitstop(0)
    PushbackX(0)
    Unknown11023(1)
    sprite('no450_34', 5)	# 619-623
    sprite('no450_35', 5)	# 624-628
    sprite('no450_34', 5)	# 629-633
    sprite('no450_35', 5)	# 634-638
    sprite('no450_34', 5)	# 639-643
    sprite('no450_35', 5)	# 644-648
    sprite('no450_34', 5)	# 649-653
    sprite('no450_35', 5)	# 654-658
    sprite('no450_34', 5)	# 659-663
    sprite('no450_35', 5)	# 664-668
    sprite('no450_34', 5)	# 669-673
    sprite('no450_35', 5)	# 674-678
    sprite('no450_34', 5)	# 679-683
    sprite('no450_35', 5)	# 684-688
    sprite('no450_34', 5)	# 689-693
    sprite('no450_35', 5)	# 694-698
    sprite('no450_34', 5)	# 699-703
    sprite('no450_35', 5)	# 704-708
    sprite('no450_34', 5)	# 709-713
    sprite('no450_35', 5)	# 714-718
    sprite('no450_34', 5)	# 719-723
    sprite('no450_35', 5)	# 724-728
    Unknown23024(0)
    sprite('no450_34', 5)	# 729-733
    sprite('no450_35', 5)	# 734-738
    sprite('no450_34', 5)	# 739-743
    sprite('no450_35', 5)	# 744-748
    sprite('no450_34', 5)	# 749-753
    sprite('no450_35', 5)	# 754-758
    sprite('no450_34', 5)	# 759-763
    sprite('no450_35', 5)	# 764-768
    sprite('no450_34', 5)	# 769-773
    sprite('no450_35', 5)	# 774-778
    sprite('no450_34', 5)	# 779-783
    sprite('no450_35', 5)	# 784-788
    sprite('no450_34', 5)	# 789-793
    sprite('no450_35', 5)	# 794-798
    sprite('no450_34', 5)	# 799-803
    sprite('no450_35', 5)	# 804-808
    sprite('no450_34', 5)	# 809-813
    sprite('no450_35', 5)	# 814-818
    sprite('no450_34', 5)	# 819-823
    sprite('no450_35', 5)	# 824-828
    Unknown21012('414863616d65726100000000000000000000000000000000000000000000000022000000')
    Unknown20000(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown20006(1)
    SLOT_61 = 1
    sprite('no450_36', 5)	# 829-833
    sprite('no450_37', 5)	# 834-838
    sprite('no450_38', 5)	# 839-843

@State
def AstralHeatOld():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        sendToLabelUpon(12, 1)
        AttackLevel_(4)
        Hitstop(0)
        Unknown11064(1)
        Damage(100)
        Unknown9130(220)
        Unknown9142(200)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        hitstun(60)
        Unknown11072(1, 280000, 0)
        PushbackX(8000)
        Unknown11067(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2004(1, 0)
        Unknown11068(1)
        Unknown11078(1)
        MinimumDamagePct(100)
        setInvincible(1)
    sprite('no450_00', 3)	# 1-3
    Unknown1084(1)
    sprite('no450_01', 4)	# 4-7
    sprite('no450_02', 4)	# 8-11
    Unknown2036(64, -1, 2)
    Unknown23147()
    setInvincible(1)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_NO_AH', -1)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(10)
    Unknown3074('0000000000000000ff000000ff000000')
    Unknown3075('00000000ff0000000000000000000000')
    Unknown3076(1000)
    Unknown3077(1300)
    SFX_0('019_quake_0')
    SFX_1('bno290')
    sprite('no450_03', 4)	# 12-15
    sprite('no450_04', 4)	# 16-19
    sprite('no450_02', 4)	# 20-23
    sprite('no450_03', 4)	# 24-27
    sprite('no450_04', 4)	# 28-31
    sprite('no450_02', 4)	# 32-35
    sprite('no450_03', 4)	# 36-39
    sprite('no450_04', 4)	# 40-43
    sprite('no450_02', 4)	# 44-47
    sprite('no450_03', 4)	# 48-51
    sprite('no450_04', 4)	# 52-55
    sprite('no450_02', 4)	# 56-59
    sprite('no450_03', 4)	# 60-63
    sprite('no450_04', 4)	# 64-67
    sprite('no450_02', 4)	# 68-71
    sprite('no450_03', 4)	# 72-75
    sprite('no450_04', 4)	# 76-79
    sprite('no450_05', 4)	# 80-83
    sprite('no450_06', 4)	# 84-87
    sprite('no450_07', 4)	# 88-91
    sprite('no450_08', 4)	# 92-95	 **attackbox here**
    GFX_1('noef_AH_firings', 0)
    GFX_1('noef_AH_mcA', 0)
    GFX_0('BLT', 2)
    ScreenShake(0, 5000)
    SFX_0('005_swing_grap_2_2')
    SFX_0('022_magiccircle_a')
    sprite('no450_07', 5)	# 96-100
    sprite('no450_39', 5)	# 101-105
    Unknown3029(0)
    Unknown11067(0)
    EnableCollision(1)
    Unknown2053(1)
    Unknown2034(1)
    sprite('no450_40', 5)	# 106-110
    setInvincible(0)
    sprite('no450_41', 5)	# 111-115
    sprite('no450_42', 5)	# 116-120
    loopRest()
    ExitState()

@State
def AstralHeatBackup():
    Unknown18010()
    Unknown21011(240)
    if SLOT_169:
        _gotolabel(482)
    if Unknown42('rg'):
        Unknown12020()
        gotoLabel(100)
    if Unknown42('jn'):
        Unknown12020()
        gotoLabel(110)
    if Unknown42('rc'):
        Unknown12020()
        gotoLabel(120)
    if Unknown42('lc'):
        Unknown12020()
        gotoLabel(130)
    if Unknown42('ny'):
        Unknown12020()
        gotoLabel(140)
    label(482)
    sprite('no610_00', 6)	# 1-6
    sprite('no610_01', 6)	# 7-12
    sprite('no610_02', 6)	# 13-18
    sprite('no610_03', 6)	# 19-24
    sprite('no610_04', 9)	# 25-33
    sprite('no610_05', 6)	# 34-39
    sprite('no610_06', 9)	# 40-48
    sprite('no610_07', 9)	# 49-57
    sprite('no610_08', 6)	# 58-63
    sprite('no610_09', 8)	# 64-71
    sprite('no610_10', 8)	# 72-79
    SFX_0('019_cloth_a')
    sprite('no610_11', 8)	# 80-87
    sprite('no610_12', 8)	# 88-95
    sprite('no610_13', 8)	# 96-103
    loopRest()
    sprite('no610_14', 7)	# 104-110
    SFX_1('no407')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no610_15', 7)	# 111-117
    sprite('no610_16', 7)	# 118-124
    sprite('no610_17', 7)	# 125-131
    sprite('no610_14', 7)	# 132-138
    sprite('no610_15', 7)	# 139-145
    sprite('no610_16', 7)	# 146-152
    sprite('no610_17', 7)	# 153-159
    Unknown21011(100)
    loopRest()
    gotoLabel(78)
    label(77)
    sprite('no610_14', 7)	# 160-166
    SFX_1('no408')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no610_15', 7)	# 167-173
    sprite('no610_16', 7)	# 174-180
    sprite('no610_17', 7)	# 181-187
    sprite('no610_14', 7)	# 188-194
    sprite('no610_15', 7)	# 195-201
    sprite('no610_16', 7)	# 202-208
    sprite('no610_17', 7)	# 209-215
    Unknown21011(40)
    loopRest()
    gotoLabel(78)
    label(78)
    sprite('no610_14', 7)	# 216-222
    sprite('no610_15', 7)	# 223-229
    sprite('no610_16', 7)	# 230-236
    sprite('no610_17', 7)	# 237-243
    loopRest()
    gotoLabel(78)
    label(100)
    sprite('no610_00', 6)	# 244-249
    sprite('no610_01', 6)	# 250-255
    sprite('no610_02', 6)	# 256-261
    sprite('no610_03', 6)	# 262-267
    sprite('no610_04', 9)	# 268-276
    sprite('no610_05', 6)	# 277-282
    sprite('no610_06', 9)	# 283-291
    sprite('no610_07', 9)	# 292-300
    sprite('no610_08', 6)	# 301-306
    sprite('no610_09', 8)	# 307-314
    sprite('no610_10', 8)	# 315-322
    SFX_0('019_cloth_a')
    sprite('no610_11', 8)	# 323-330
    sprite('no610_12', 8)	# 331-338
    sprite('no610_13', 8)	# 339-346
    loopRest()
    sprite('no610_14', 7)	# 347-353
    SFX_1('no501')
    Unknown18003('6138633861386338613863386138633861386338613863386138633861386338613863386138633800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no610_15', 7)	# 354-360
    sprite('no610_16', 7)	# 361-367
    sprite('no610_17', 7)	# 368-374
    sprite('no610_14', 7)	# 375-381
    sprite('no610_15', 7)	# 382-388
    sprite('no610_16', 7)	# 389-395
    sprite('no610_17', 7)	# 396-402
    Unknown21011(100)
    loopRest()
    label(101)
    sprite('no610_14', 7)	# 403-409
    sprite('no610_15', 7)	# 410-416
    sprite('no610_16', 7)	# 417-423
    sprite('no610_17', 7)	# 424-430
    loopRest()
    gotoLabel(101)
    ExitState()
    label(110)
    sprite('no610_00', 6)	# 431-436
    sprite('no610_01', 6)	# 437-442
    sprite('no610_02', 6)	# 443-448
    sprite('no610_03', 6)	# 449-454
    sprite('no610_04', 9)	# 455-463
    sprite('no610_05', 6)	# 464-469
    sprite('no610_06', 9)	# 470-478
    sprite('no610_07', 9)	# 479-487
    sprite('no610_08', 6)	# 488-493
    sprite('no610_09', 8)	# 494-501
    sprite('no610_10', 8)	# 502-509
    SFX_0('019_cloth_a')
    sprite('no610_11', 8)	# 510-517
    sprite('no610_12', 8)	# 518-525
    sprite('no610_13', 8)	# 526-533
    loopRest()
    sprite('no610_14', 7)	# 534-540
    SFX_1('no503')
    Unknown18003('6138633861380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no610_15', 7)	# 541-547
    sprite('no610_16', 7)	# 548-554
    sprite('no610_17', 7)	# 555-561
    sprite('no610_14', 7)	# 562-568
    sprite('no610_15', 7)	# 569-575
    sprite('no610_16', 7)	# 576-582
    sprite('no610_17', 7)	# 583-589
    Unknown18003('6333346138633861386338613863386138633861380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21011(130)
    loopRest()
    label(111)
    sprite('no610_14', 7)	# 590-596
    sprite('no610_15', 7)	# 597-603
    sprite('no610_16', 7)	# 604-610
    sprite('no610_17', 7)	# 611-617
    loopRest()
    gotoLabel(111)
    ExitState()
    label(120)
    sprite('no610_00', 6)	# 618-623
    sprite('no610_01', 6)	# 624-629
    sprite('no610_02', 6)	# 630-635
    sprite('no610_03', 6)	# 636-641
    sprite('no610_04', 9)	# 642-650
    sprite('no610_05', 6)	# 651-656
    sprite('no610_06', 9)	# 657-665
    sprite('no610_07', 9)	# 666-674
    sprite('no610_08', 6)	# 675-680
    sprite('no610_09', 8)	# 681-688
    sprite('no610_10', 8)	# 689-696
    SFX_0('019_cloth_a')
    sprite('no610_11', 8)	# 697-704
    sprite('no610_12', 8)	# 705-712
    sprite('no610_13', 8)	# 713-720
    loopRest()
    sprite('no610_14', 7)	# 721-727
    SFX_1('no507')
    Unknown18003('6137633761370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no610_15', 7)	# 728-734
    sprite('no610_16', 7)	# 735-741
    sprite('no610_17', 7)	# 742-748
    sprite('no610_14', 7)	# 749-755
    sprite('no610_15', 7)	# 756-762
    sprite('no610_16', 7)	# 763-769
    sprite('no610_17', 7)	# 770-776
    Unknown18003('6332306137633761376337613763370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21011(100)
    loopRest()
    label(121)
    sprite('no610_14', 7)	# 777-783
    sprite('no610_15', 7)	# 784-790
    sprite('no610_16', 7)	# 791-797
    sprite('no610_17', 7)	# 798-804
    loopRest()
    gotoLabel(121)
    ExitState()
    label(130)
    if random_(2, 0, 50):
        gotoLabel(135)
    sprite('no610_00', 6)	# 805-810
    sprite('no610_01', 6)	# 811-816
    sprite('no610_02', 6)	# 817-822
    sprite('no610_03', 6)	# 823-828
    sprite('no610_04', 9)	# 829-837
    sprite('no610_05', 6)	# 838-843
    sprite('no610_06', 9)	# 844-852
    sprite('no610_07', 9)	# 853-861
    sprite('no610_08', 6)	# 862-867
    sprite('no610_09', 8)	# 868-875
    sprite('no610_10', 8)	# 876-883
    SFX_0('019_cloth_a')
    sprite('no610_11', 8)	# 884-891
    sprite('no610_12', 8)	# 892-899
    sprite('no610_13', 8)	# 900-907
    loopRest()
    sprite('no610_14', 7)	# 908-914
    SFX_1('no513')
    Unknown18003('6136633661366336613600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no610_15', 7)	# 915-921
    sprite('no610_16', 7)	# 922-928
    sprite('no610_17', 7)	# 929-935
    sprite('no610_14', 7)	# 936-942
    sprite('no610_15', 7)	# 943-949
    sprite('no610_16', 7)	# 950-956
    sprite('no610_17', 7)	# 957-963
    Unknown18003('6334306137633761376337613763376137633761376337000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21011(180)
    loopRest()
    label(131)
    sprite('no610_14', 7)	# 964-970
    sprite('no610_15', 7)	# 971-977
    sprite('no610_16', 7)	# 978-984
    sprite('no610_17', 7)	# 985-991
    loopRest()
    gotoLabel(131)
    ExitState()
    label(135)
    sprite('no611_00', 6)	# 992-997
    sprite('no611_01', 6)	# 998-1003
    sprite('no611_02', 6)	# 1004-1009
    sprite('no611_03', 6)	# 1010-1015
    sprite('no611_04', 6)	# 1016-1021
    sprite('no611_05', 6)	# 1022-1027
    sprite('no611_06', 6)	# 1028-1033
    sprite('no611_07', 6)	# 1034-1039
    sprite('no611_08', 6)	# 1040-1045
    sprite('no611_09', 6)	# 1046-1051
    sprite('no611_10', 6)	# 1052-1057
    sprite('no611_11', 6)	# 1058-1063
    sprite('no611_12', 6)	# 1064-1069
    sprite('no611_13', 6)	# 1070-1075
    sprite('no611_14', 6)	# 1076-1081
    Unknown2004(0, 0)
    EnableCollision(0)
    sprite('no611_15', 6)	# 1082-1087
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown2015(140)
    SFX_1('no513')
    Unknown18003('6136633661366336613600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('no611_16', 6)	# 1088-1093
    sprite('no611_17', 80)	# 1094-1173
    sprite('no611_17', 32767)	# 1174-33940
    Unknown18003('6136633661366136633661366336613661366336613663360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21011(120)
    Unknown51(1)
    ExitState()
    label(140)
    sprite('no620_00', 6)	# 33941-33946
    SFX_1('no523')
    sprite('no620_01', 6)	# 33947-33952
    sprite('no620_02', 6)	# 33953-33958
    sprite('no620_03', 6)	# 33959-33964
    sprite('no620_04', 6)	# 33965-33970
    sprite('no620_05', 6)	# 33971-33976
    sprite('no620_06', 6)	# 33977-33982
    Unknown8000(100, 1, 1)
    sprite('no620_07', 6)	# 33983-33988
    sprite('no620_08', 6)	# 33989-33994
    Unknown21011(180)
    Unknown51(1)
    ExitState()

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        EnableCollision(0)
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
    sprite('no293_03', 3)	# 631-633
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-215000)
    Unknown1007(1200000)
    physicsYImpulse(-240000)
    setGravity(0)
    Unknown2053(1)
    EnableCollision(1)
    SFX_0('016_explode_1')
    GFX_0('noef_293', 2)
    sprite('no293_04', 32767)	# 634-33400	 **attackbox here**
    StartMultihit()
    label(9)
    sprite('no293_04', 3)	# 33401-33403	 **attackbox here**
    sprite('no024_01', 3)	# 33404-33406
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('no024_02', 13)	# 33407-33419
    sprite('no024_03', 3)	# 33420-33422
    sprite('no024_04', 3)	# 33423-33425

@State
def CmnActChangePartnerQuickIn():
    sprite('no032_08', 3)	# 1-3
    sprite('no032_08', 8)	# 4-11
    sprite('no032_09', 7)	# 12-18
    sprite('no032_10', 6)	# 19-24
    sprite('no032_11', 5)	# 25-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('no033_02', 3)	# 1-3
    sprite('no033_03', 3)	# 4-6
    sprite('no033_02', 3)	# 7-9
    sprite('no033_03', 3)	# 10-12
    sprite('no033_02', 3)	# 13-15
    sprite('no033_03', 3)	# 16-18
    sprite('no033_02', 3)	# 19-21
    sprite('no033_03', 3)	# 22-24
    sprite('no033_02', 3)	# 25-27
    sprite('no033_03', 3)	# 28-30
    sprite('no033_02', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('no033_00', 1)	# 1-1
    sprite('no033_01', 2)	# 2-3
    sprite('no033_02', 2)	# 4-5
    Unknown8002()
    sprite('no033_02', 1)	# 6-6
    sprite('no033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('no033_02', 3)	# 10-12
    sprite('no033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no033_04', 3)	# 16-18
    sprite('no033_05', 3)	# 19-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('no301_00', 6)	# 1-6
    sprite('no301_01', 6)	# 7-12
    sprite('no301_02', 6)	# 13-18
    sprite('no301_03', 6)	# 19-24
    sprite('no301_04', 6)	# 25-30
    sprite('no301_05', 7)	# 31-37
    sprite('no301_06', 8)	# 38-45
    sprite('no301_07', 7)	# 46-52
    sprite('no301_08', 6)	# 53-58
    sprite('no301_09', 6)	# 59-64
    sprite('no301_10', 6)	# 65-70
    loopRest()
    sprite('no000_00', 30)	# 71-100

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
    sprite('no021_08', 4)	# 3-6
    Unknown1019(95)
    sprite('no021_09', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('no010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown2004(1, 0)
    sprite('no285_00', 5)	# 1-5
    SFX_3('nose_07')
    sprite('no285_01', 8)	# 6-13
    sprite('no285_02', 8)	# 14-21
    Unknown7006('bno307_0', 100, 862940770, 828323632, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('no285_03', 8)	# 22-29
    sprite('no285_04', 3)	# 30-32
    GFX_0('GunThrowShotObj', -1)
    sprite('no285_05', 3)	# 33-35
    sprite('no285_06', 3)	# 36-38
    sprite('no285_07', 32)	# 39-70
    sprite('no285_08', 2)	# 71-72
    sprite('no285_09', 2)	# 73-74
    sprite('no285_10', 2)	# 75-76
    sprite('no285_11', 4)	# 77-80
    Recovery()
    SFX_0('024_getset_a')
    sprite('no285_12', 4)	# 81-84
    sprite('no285_13', 3)	# 85-87
    sprite('no285_14', 3)	# 88-90

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(1100)
        AttackP1(70)
        Unknown9310(30)
        Unknown11092(1)
        Unknown11058('0000000000000000010000000000000000000000')
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(-2000)
        PushbackX(4000)
        Unknown11042(1)
        ChipDamagePct(5)
        MinimumDamagePct(5)
    sprite('no330_00', 2)	# 1-2
    sprite('no330_01', 2)	# 3-4
    sprite('no330_02', 2)	# 5-6
    sprite('no330_03', 2)	# 7-8
    tag_voice(1, 'bno306_0', 'bno306_1', '', '')
    sprite('no330_04', 3)	# 9-11
    sprite('no330_05ex00', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 2)
    Unknown36(1)
    Unknown1077(80000, 40000)
    Unknown35()
    GFX_0('noef_OIUCHI', 1)
    GFX_0('noef_smoke', 1)
    ScreenShake(0, 3000)
    SLOT_51 = (SLOT_51 + (-1))
    sprite('no330_06', 2)	# 14-15	 **attackbox here**
    Recovery()
    StartMultihit()
    sprite('no330_05', 2)	# 16-17	 **attackbox here**
    StartMultihit()
    SFX_3('nose_01')
    sprite('no330_07', 2)	# 18-19
    sprite('no330_08ex00', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    Damage(1500)
    AirPushbackX(2500)
    AirPushbackY(-38500)
    Unknown9310(0)
    AirUntechableTime(60)
    Unknown9190(1)
    GroundedHitstunAnimation(1)
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 2)
    Unknown36(1)
    Unknown1077(80000, 40000)
    Unknown35()
    GFX_0('noef_OIUCHI', 1)
    GFX_0('noef_smoke', 1)
    ScreenShake(0, 5000)
    sprite('no330_09', 15)	# 22-36	 **attackbox here**
    StartMultihit()
    SFX_3('nose_01')
    Recovery()
    sprite('no330_10', 8)	# 37-44
    sprite('no330_11', 7)	# 45-51
    loopRest()

@State
def CmnActChangePartnerAssistAtk_C():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        ProjectileDurabilityLvl(1)
        Damage(700)
        AttackP1(70)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        Unknown9130(42)
        Unknown9142(32)
        AirUntechableTime(40)
        hitstun(23)
        Hitstop(3)
        Unknown11001(5, 5, 5)
        YImpluseBeforeWallbounce(2000)
        AirPushbackX(7500)
        Unknown30056('b0ad01001e00000000000000')
        PushbackX(16000)
        Unknown9018(1)
        Unknown2004(1, 0)
        Unknown11042(1)

        def upon_78():
            SLOT_51 = 1
            AirPushbackY(20000)
    sprite('no284_00', 2)	# 1-2
    SFX_3('nose_07')
    sprite('no284_01', 4)	# 3-6
    physicsXImpulse(52000)
    sprite('no284_02', 2)	# 7-8
    Unknown1019(85)
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no284_03', 2)	# 9-10
    Unknown1019(45)
    sprite('no284_04', 2)	# 11-12	 **attackbox here**
    StartMultihit()
    sprite('no284_05ex01', 3)	# 13-15	 **attackbox here**
    Unknown1019(0)
    SFX_0('016_explode_1')
    GFX_0('BLT', 1)
    GFX_0('EFF_LongFireTypeA', 3)
    ScreenShake(0, 5000)
    sprite('no284_04', 2)	# 16-17	 **attackbox here**
    Unknown7006('bno307_0', 100, 862940770, 828323632, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    StartMultihit()
    sprite('no284_05ex01', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    SFX_0('016_explode_1')
    GFX_0('BLT', 0)
    GFX_0('EFF_LongFireTypeA', 2)
    ScreenShake(0, 5000)
    sprite('no284_05ex01', 1)	# 21-21	 **attackbox here**
    StartMultihit()
    sprite('no284_05ex01', 2)	# 22-23	 **attackbox here**
    StartMultihit()
    sprite('no284_06', 5)	# 24-28
    SFX_3('nose_01')
    callSubroutine('NoelComboDeriveTimingBegin')
    if SLOT_51:
        sendToLabel(0)
    sprite('no284_07', 5)	# 29-33
    Recovery()
    sprite('no284_08', 5)	# 34-38
    callSubroutine('NoelComboDeriveClear')
    sprite('no284_09', 5)	# 39-43
    sprite('no284_10', 5)	# 44-48
    physicsXImpulse(0)
    sprite('no284_11', 5)	# 49-53
    loopRest()
    ExitState()
    label(0)
    sprite('no286_00', 2)	# 54-55
    sprite('no286_01', 1)	# 56-56
    sprite('no286_02', 2)	# 57-58
    sprite('no286_03', 2)	# 59-60
    sprite('no286_04', 4)	# 61-64
    sprite('no286_05', 2)	# 65-66
    sprite('no286_06', 2)	# 67-68	 **attackbox here**
    AttackLevel_(5)
    RefreshMultihit()
    GroundedHitstunAnimation(2)
    AirPushbackX(16000)
    AirPushbackY(6000)
    YImpluseBeforeWallbounce(1000)
    Hitstop(4)
    clearUponHandler(78)
    Damage(700)
    Unknown2004(1, 0)
    SFX_0('006_swing_blade_1')
    sprite('no286_07', 2)	# 69-70
    sprite('no286_08', 2)	# 71-72
    sprite('no286_09', 2)	# 73-74
    sprite('no286_10', 1)	# 75-75	 **attackbox here**
    StartMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 1)
    GFX_0('EFF_LongFireTypeC', 0)
    Unknown36(1)
    Unknown1064(1200)
    Unknown35()
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    sprite('no286_10', 2)	# 76-77	 **attackbox here**
    RefreshMultihit()
    Unknown9018(1)
    Unknown9346(1)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(1500)
    YImpluseBeforeWallbounce(100)
    Hitstop(0)
    ProjectileDurabilityLvl(1)
    AirUntechableTime(50)
    AirHitstunAfterWallbounce(50)
    Unknown30056('000000000000000000000000')
    WallbounceReboundTime(5)
    Unknown9346(0)
    Hitstop(1)
    Damage(500)
    Unknown9017(1)
    sprite('no286_10', 2)	# 78-79	 **attackbox here**
    RefreshMultihit()
    sprite('no286_10', 2)	# 80-81	 **attackbox here**
    RefreshMultihit()
    sprite('no286_10', 2)	# 82-83	 **attackbox here**
    RefreshMultihit()
    sprite('no286_10', 21)	# 84-104	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('no286_11', 7)	# 105-111
    SFX_3('nose_01')
    sprite('no286_12', 5)	# 112-116

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
    Unknown2036(49, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-75000)
    Unknown1019(4)
    label(0)
    sprite('no021_08', 4)	# 3-6
    sprite('no021_09', 4)	# 7-10
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
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(300)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        Unknown11092(1)
        AirUntechableTime(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9142(36)
        Unknown2004(1, 0)
        Unknown11072(1, 300000, 0)
        AirPushbackY(25000)
        AirPushbackX(3200)
        YImpluseBeforeWallbounce(800)
        PushbackX(5200)
        Unknown11062(1)
        Unknown11064(1)
        setInvincible(1)
        Unknown11056(2)

        def upon_78():
            Unknown2021(1)
            Unknown2038(1)
            Unknown11069('UltimateShotDDD')
    sprite('no214_00', 4)	# 1-4
    sprite('no214_01', 4)	# 5-8
    SFX_3('nose_07')
    SFX_0('001_airbackdash_0')
    sprite('no214_02', 3)	# 9-11
    sprite('no214_03', 3)	# 12-14
    sprite('no214_04', 3)	# 15-17
    sprite('no214_05', 2)	# 18-19
    sprite('no214_06', 2)	# 20-21
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no214_07', 2)	# 22-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no214_08', 1)	# 24-24	 **attackbox here**
    StartMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 1)
    Unknown36(1)
    Unknown1077(80000, 40000)
    Unknown35()
    GFX_0('noef_gfground', 2)
    sprite('no214_08', 5)	# 25-29	 **attackbox here**
    sprite('no214_09', 2)	# 30-31	 **attackbox here**
    if (not SLOT_2):
        setInvincible(0)
    SFX_3('nose_01')
    sprite('no214_09', 4)	# 32-35	 **attackbox here**
    sprite('no214_10', 6)	# 36-41
    loopRest()
    if SLOT_2:
        sendToLabel(1)
    sprite('no214_11', 5)	# 42-46
    sprite('no214_11', 3)	# 47-49
    sprite('no214_12', 6)	# 50-55
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    enterState('Reload')
    ExitState()
    label(1)
    sprite('no431_23', 30)	# 56-85
    Unknown13024(0)
    clearUponHandler(78)
    teleportRelativeX(-150000)
    Unknown2036(100, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown20000(1)
    GFX_0('noef431gun_make_DDD', -1)
    sprite('no431_24', 4)	# 86-89
    sprite('no431_25', 4)	# 90-93
    sprite('no431_26', 4)	# 94-97
    ScreenShake(0, 1000)
    sprite('no431_27', 2)	# 98-99	 **attackbox here**
    ScreenShake(0, 1000)
    tag_voice(0, 'bno252_0', 'bno252_1', '', '')
    sprite('no431_28', 2)	# 100-101	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex01', 2)	# 102-103	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('MajuMagicCircle', 2)
    GFX_1('noef_431_charge', 2)
    SFX_3('nose_05')
    sprite('no431_28ex01', 2)	# 104-105	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex02', 2)	# 106-107	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex02', 2)	# 108-109	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex03', 2)	# 110-111	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex03', 2)	# 112-113	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex04', 2)	# 114-115	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex04', 2)	# 116-117	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex05', 2)	# 118-119	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex05', 2)	# 120-121	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex06', 2)	# 122-123	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex06', 2)	# 124-125	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex07', 2)	# 126-127	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 128-129	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 130-131	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 132-133	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 134-135	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 136-137	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 138-139	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 140-141	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 142-143	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 144-145	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 146-147	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 148-149	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 150-151	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 152-153	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 154-155	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 156-157	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 158-159	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 160-161	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 162-163	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 164-165	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 166-167	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 168-169	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 170-171	 **attackbox here**
    ScreenShake(0, 5000)
    RefreshMultihit()
    Unknown11034(0)
    ProjectileDurabilityLvl(2)
    Unknown11058('0000000000000000000000000100000000000000')
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(35000)
    AirPushbackY(49000)
    YImpluseBeforeWallbounce(1800)
    Hitstop(0)
    Unknown11001(0, 0, 0)
    Damage(1700)
    AirUntechableTime(120)
    Unknown11072(0, 0, 0)
    Unknown23159('maju_Finish')
    ScreenShake(0, 10000)
    Unknown11069('')
    Unknown11064(0)
    sprite('no431_27ex08', 2)	# 172-173	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('ModelBeam', 2)
    SFX_3('nose_06')
    SFX_3('nose_06')
    sprite('no431_28ex07', 2)	# 174-175	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_29', 5)	# 176-180	 **attackbox here**
    sprite('no431_30', 5)	# 181-185
    sprite('no431_31', 4)	# 186-189
    sprite('no431_32', 4)	# 190-193
    sprite('no431_33', 4)	# 194-197
    sprite('no431_34', 4)	# 198-201
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_35', 4)	# 202-205
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_36', 4)	# 206-209
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_37', 4)	# 210-213
    Unknown13024(1)
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_38', 8)	# 214-221
    sprite('no431_39', 8)	# 222-229
    sprite('no431_40', 6)	# 230-235
    loopRest()

@State
def UltimateShotDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(300)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        Unknown11092(1)
        AirUntechableTime(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9142(36)
        Unknown2004(1, 0)
        Unknown11072(1, 300000, 0)
        AirPushbackY(25000)
        AirPushbackX(3200)
        YImpluseBeforeWallbounce(1200)
        PushbackX(5200)
        Unknown11056(2)
        Unknown11064(1)

        def upon_78():
            Unknown2021(1)
            Unknown2038(1)
            Unknown11069('MajuShotObj_TsuikaDDD')
        setInvincible(1)
    sprite('no214_00', 4)	# 1-4
    sprite('no214_01', 4)	# 5-8
    SFX_3('nose_07')
    SFX_0('001_airbackdash_0')
    sprite('no214_02', 3)	# 9-11
    sprite('no214_03', 3)	# 12-14
    sprite('no214_04', 3)	# 15-17
    sprite('no214_05', 2)	# 18-19
    sprite('no214_06', 2)	# 20-21
    callSubroutine('NoelComboDeriveInputBegin')
    sprite('no214_07', 2)	# 22-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no214_08', 1)	# 24-24	 **attackbox here**
    StartMultihit()
    SFX_0('016_explode_1')
    ScreenShake(0, 5000)
    GFX_0('BLT', 0)
    GFX_0('EFF_Spark', 1)
    Unknown36(1)
    Unknown1077(80000, 40000)
    Unknown35()
    GFX_0('noef_gfground', 2)
    sprite('no214_08', 5)	# 25-29	 **attackbox here**
    sprite('no214_09', 2)	# 30-31	 **attackbox here**
    if (not SLOT_2):
        setInvincible(0)
    SFX_3('nose_01')
    sprite('no214_09', 4)	# 32-35	 **attackbox here**
    sprite('no214_10', 6)	# 36-41
    loopRest()
    if SLOT_2:
        sendToLabel(1)
    sprite('no214_11', 5)	# 42-46
    sprite('no214_11', 3)	# 47-49
    sprite('no214_12', 6)	# 50-55
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    enterState('Reload')
    ExitState()
    label(1)
    sprite('no431_23', 30)	# 56-85
    Unknown13024(0)
    clearUponHandler(78)
    teleportRelativeX(-150000)
    Unknown2036(36, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown20000(1)
    GFX_0('noef431gun_make_DDD', -1)
    sprite('no431_24', 4)	# 86-89
    sprite('no431_25', 4)	# 90-93
    sprite('no431_26', 4)	# 94-97
    ScreenShake(0, 1000)
    sprite('no431_27', 3)	# 98-100	 **attackbox here**
    sprite('no431_28SP', 3)	# 101-103	 **attackbox here**
    SLOT_52 = 15
    label(101)
    sprite('no431_27', 2)	# 104-105	 **attackbox here**
    ScreenShake(1000, 5000)
    GFX_0('EFF_SakuretsuNear', 0)
    sprite('no431_28SP', 1)	# 106-106	 **attackbox here**
    ScreenShake(5000, 1000)
    GFX_0('BLT', 1)
    GFX_0('MajuShotObj_TsuikaDDD', 1)
    if (not SLOT_52):
        Unknown23029(1, 4311, 0)
    sprite('no431_28SP', 1)	# 107-107	 **attackbox here**
    SLOT_52 = (SLOT_52 + (-1))
    Unknown19(102, 2, 52)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('no431_27', 2)	# 108-109	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28SP', 2)	# 110-111	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27', 2)	# 112-113	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28SP', 2)	# 114-115	 **attackbox here**
    ScreenShake(0, 1000)
    Unknown2036(45, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown20000(1)
    sprite('no431_27', 2)	# 116-117	 **attackbox here**
    ScreenShake(0, 1000)
    tag_voice(0, 'bno252_0', 'bno252_1', '', '')
    sprite('no431_28', 2)	# 118-119	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex01', 2)	# 120-121	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('MajuMagicCircle', 2)
    GFX_1('noef_431_charge', 2)
    SFX_3('nose_05')
    sprite('no431_28ex01', 2)	# 122-123	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex02', 2)	# 124-125	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex02', 2)	# 126-127	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex03', 2)	# 128-129	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex03', 2)	# 130-131	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex04', 2)	# 132-133	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex04', 2)	# 134-135	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex05', 2)	# 136-137	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex05', 2)	# 138-139	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex06', 2)	# 140-141	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex06', 2)	# 142-143	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex07', 2)	# 144-145	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 146-147	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 148-149	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 150-151	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 152-153	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 154-155	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 156-157	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 158-159	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 160-161	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 162-163	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 164-165	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 166-167	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 168-169	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 170-171	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 172-173	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 174-175	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 176-177	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 178-179	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 180-181	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_27ex08', 2)	# 182-183	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 184-185	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 186-187	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_28ex07', 2)	# 188-189	 **attackbox here**
    ScreenShake(0, 5000)
    RefreshMultihit()
    Unknown11034(0)
    ProjectileDurabilityLvl(2)
    Unknown11058('0000000000000000000000000100000000000000')
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(35000)
    AirPushbackY(43500)
    YImpluseBeforeWallbounce(1800)
    Hitstop(0)
    Damage(1750)
    AirUntechableTime(120)
    Unknown11072(0, 0, 0)
    Unknown11001(0, 0, 0)
    Unknown23159('majuOD_Finish')
    ScreenShake(0, 10000)
    Unknown11069('')
    Unknown11064(0)
    sprite('no431_27ex08', 2)	# 190-191	 **attackbox here**
    ScreenShake(0, 1000)
    GFX_0('ModelBeam', 2)
    SFX_3('nose_06')
    SFX_3('nose_06')
    sprite('no431_28ex07', 2)	# 192-193	 **attackbox here**
    ScreenShake(0, 1000)
    sprite('no431_29', 5)	# 194-198	 **attackbox here**
    sprite('no431_30', 5)	# 199-203
    sprite('no431_31', 4)	# 204-207
    sprite('no431_32', 4)	# 208-211
    sprite('no431_33', 4)	# 212-215
    sprite('no431_34', 4)	# 216-219
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_35', 4)	# 220-223
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_36', 4)	# 224-227
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_37', 4)	# 228-231
    Unknown13024(1)
    SFX_0('008_swing_pole_1')
    GFX_0('noef431gun_turn', 0)
    GFX_0('noef431gun_turn', 1)
    sprite('no431_38', 8)	# 232-239
    sprite('no431_39', 8)	# 240-247
    sprite('no431_40', 6)	# 248-253
    loopRest()
    ExitState()

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('no611_11', 6)	# 1-6
    sprite('no611_12', 6)	# 7-12
    sprite('no611_13', 6)	# 13-18
    sprite('no611_14', 6)	# 19-24
    sprite('no611_15', 6)	# 25-30
    sprite('no611_16', 6)	# 31-36
    sprite('no611_17', 36)	# 37-72
    sprite('no611_17', 1)	# 73-73
    Unknown30042(24)
    if SLOT_ReturnVal:
        _gotolabel(2)
    sprite('keep', 32767)	# 74-32840
    label(2)
    sprite('no611_14', 6)	# 32841-32846
    sprite('no611_12', 6)	# 32847-32852

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_STATE_END():
            Unknown2053(1)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 1)	# 121-121
    Unknown1086(22)
    teleportRelativeX(-105000)
    teleportRelativeX(-1000000)
    Unknown1007(1200000)
    physicsXImpulse(35714)
    physicsYImpulse(-40000)
    setGravity(0)
    sprite('no293_00', 20)	# 122-141
    sprite('no293_01', 2)	# 142-143
    sprite('no293_02', 2)	# 144-145
    sprite('no293_03', 3)	# 146-148
    SFX_0('016_explode_1')
    GFX_0('noef_293', 2)
    Unknown2053(1)
    sprite('no293_04', 3)	# 149-151	 **attackbox here**
    GFX_0('BLT', 0)
    GFX_0('BLT', 1)
    sprite('no293_05', 3)	# 152-154
    sendToLabelUpon(2, 1)
    sprite('no293_06', 3)	# 155-157
    sprite('no293_07', 3)	# 158-160
    sprite('no293_08', 4)	# 161-164
    sprite('no293_09', 4)	# 165-168
    sprite('no293_10', 4)	# 169-172
    sprite('no020_05', 32767)	# 173-32939
    label(1)
    sprite('no024_01', 5)	# 32940-32944
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('no024_02', 14)	# 32945-32958
    sprite('no024_03', 5)	# 32959-32963
    sprite('no024_04', 5)	# 32964-32968

@State
def CmnActChangeReturnAppealBurst():
    sprite('no111_07', 85)	# 1-85

@Subroutine
def MouthTableInit():
    Unknown18011('bno000', 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno500', 14179, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno500', '001')
    Unknown18011('bno501', 14433, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno501', '002')
    Unknown18011('bno502', 14179, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno502', '003')
    Unknown18011('bno503', 14435, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno503', '004')
    Unknown18011('bno504', 14435, 24889, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno504', '005')
    Unknown18011('bno505', 12643, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13618, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno505', '006')
    Unknown18011('bno520', 12643, 14177, 14179, 14177, 14179, 24882, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno520', '007')
    Unknown18011('bno521', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno521', '008')
    Unknown18011('bno522', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno522', '009')
    Unknown18011('bno523', 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno523', '010')
    Unknown18011('bno524', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno524', '011')
    Unknown18011('bno525', 12643, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno525', '012')
    Unknown18011('bno404_0', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno404_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno403_0', 12643, 12343, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno403_1', 12643, 12343, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601biz', 12643, 13921, 13411, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601bjn', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601bma', 12643, 13921, 13923, 13921, 12643, 24880, 25398, 24886, 25398, 14129, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601bmk', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno600brg', 12643, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12853, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno600pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601pna', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 14137, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno600ryn', 12643, 14177, 12899, 24882, 25399, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno600uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno600uva', 12643, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno603bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno604bny', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601ahe', 12643, 12897, 25392, 13623, 12897, 25396, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 13361, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno601bce', 12643, 14177, 12899, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14386, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno603', 12643, 24885, 12849, 13155, 24888, 25397, 14131, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno600brg', '017')
    Unknown30092('bno600pla', '018')
    Unknown30092('bno600ryn', '019')
    Unknown30092('bno600uhy', '020')
    Unknown30092('bno600uva', '021')
    Unknown30092('bno601biz', '022')
    Unknown30092('bno601bjn', '023')
    Unknown30092('bno601bma', '024')
    Unknown30092('bno601bmk', '025')
    Unknown30092('bno601bny', '026')
    Unknown30092('bno601pna', '027')
    Unknown30092('bno604bny', '029')
    Unknown30092('bno601bce', '030')
    Unknown30092('bno603', '031')
    Unknown30092('bno601ahe', '032')
    Unknown18011('bno701biz', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno700bjn', 12643, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno700bma', 12643, 12641, 25394, 12343, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno701bmk', 12643, 12641, 25397, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno701bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno700brg', 12643, 14177, 13155, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno701pla', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 13411, 24884, 12849, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno700pna', 12643, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno701ryn', 12643, 13665, 12899, 24885, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno700uhy', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno701uva', 12643, 14177, 13667, 24882, 12849, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno702bjn', 12643, 14177, 13411, 24882, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno702bny', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno700ahe', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno702ahe', 12643, 13665, 13155, 24885, 12338, 12643, 24888, 25399, 24887, 14385, 12899, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bno700bce', 12899, 13153, 25398, 14388, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bno700bjn', '033')
    Unknown30092('bno700bma', '034')
    Unknown30092('bno700brg', '035')
    Unknown30092('bno700pna', '036')
    Unknown30092('bno700uhy', '037')
    Unknown30092('bno701biz', '038')
    Unknown30092('bno701bmk', '039')
    Unknown30092('bno701bny', '040')
    Unknown30092('bno701pla', '041')
    Unknown30092('bno701ryn', '042')
    Unknown30092('bno701uva', '043')
    Unknown30092('bno702bjn', '044')
    Unknown30092('bno702bny', '045')
    Unknown30092('bno700bce', '046')
    Unknown30092('bno700ahe', '047')
    Unknown30092('bno702ahe', '048')
    if SLOT_172:
        Unknown18011('bno000', 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno500', 12643, 12643, 14177, 14179, 14177, 14179, 13921, 13155, 14177, 14179, 14177, 12899, 13411, 14177, 14179, 13921, 12643, 14177, 14179, 14435, 13153, 14435, 14177, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno501', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13411, 24880, 25399, 24887, 25399, 24887, 25394, 24881, 25399, 24881, 25399, 25393, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno502', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 12899, 12899, 13153, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno503', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno504', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14177, 14179, 14177, 14179, 13409, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno505', 12643, 12643, 14177, 13155, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno520', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 12643, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno521', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13411, 14177, 13411, 12643, 12641, 12643, 24886, 25399, 25397, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24881, 25399, 24887, 25399, 24887, 25399, 25398, 24881, 25399, 25397, 12594, 13409, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno522', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13411, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno523', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno524', 12643, 12643, 12641, 13155, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12641, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24883, 25397, 24881, 25393, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno525', 12643, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 12641, 12899, 14177, 13667, 12643, 14177, 13667, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno404_0', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno404_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno403_0', 12643, 12343, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno403_1', 12643, 12343, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601biz', 12643, 12643, 14177, 14179, 12899, 14177, 12899, 12899, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 12897, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601bjn', 12643, 12899, 13921, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601bma', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24889, 25399, 24887, 25399, 25398, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24884, 25399, 25393, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601bmk', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 24882, 25399, 25396, 24881, 25399, 24887, 25399, 24887, 25399, 25397, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601bny', 12643, 12899, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 12899, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno600brg', 12643, 12899, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno600pla', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601pna', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 12899, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno600ryn', 12643, 12643, 14177, 12643, 12899, 24882, 25399, 25398, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24881, 25396, 24881, 25398, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno600uhy', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 24883, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno600uva', 12643, 14177, 13155, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno603bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno604bny', 12643, 12643, 14177, 14179, 14177, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601ahe', 12643, 14177, 14179, 14177, 14179, 13153, 13155, 24880, 25399, 24887, 25396, 14129, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 13667, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno601bce', 12643, 12643, 13921, 12643, 24885, 25399, 24887, 25399, 24887, 25395, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 24881, 25399, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno603', 12643, 12899, 14177, 13155, 12643, 14177, 13923, 14179, 14177, 14179, 13665, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno701biz', 12643, 12643, 14177, 14179, 14177, 14179, 13153, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 25394, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno700bjn', 12643, 12643, 14177, 12643, 12643, 24884, 25399, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno700bma', 12643, 14177, 14179, 14177, 13923, 12899, 14177, 14179, 13153, 14691, 14177, 13923, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24881, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno701bmk', 12643, 12899, 14177, 14179, 14177, 14179, 13665, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno701bny', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno700brg', 12643, 12643, 14177, 12643, 14435, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 12643, 13155, 13921, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno701pla', 12643, 12643, 14177, 14179, 12897, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24881, 25398, 14641, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno700pna', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 13665, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno701ryn', 12643, 12643, 14177, 13923, 12643, 24881, 25399, 25394, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno700uhy', 12643, 12643, 13921, 13155, 12897, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14177, 14179, 12641, 13155, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno701uva', 12643, 12643, 14177, 13923, 12643, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24889, 25399, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 25396, 24881, 25399, 24887, 25399, 24887, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno702bjn', 12643, 12899, 14177, 12643, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno702bny', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 12641, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno700ahe', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 14177, 14179, 13155, 14177, 14179, 14177, 14179, 12641, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno702ahe', 12643, 14177, 12643, 14435, 12641, 12643, 13153, 13667, 14177, 14179, 14177, 14179, 14177, 12899, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bno700bce', 12643, 12643, 14177, 14179, 14177, 14179, 13153, 13411, 13921, 12643, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 24881, 25399, 24887, 25399, 25398, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('6263650000000000000000000000000062726700000000000000000000000000626a6e00000000000000000000000000626e6f00000000000000000000000000'):
        SLOT_171 = 1
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
    if SLOT_171:
        _gotolabel(1000)
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bjn')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('uhy')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('pna')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('bny')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('bmk')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('uva')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('ryn')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('pla')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('bma')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('biz')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('bce')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('ahe')
    if SLOT_ReturnVal:
        _gotolabel(220)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('no604_00', 6)	# 2-7
    if random_(2, 0, 50):
        SFX_1('bno501')
    else:
        SLOT_51 = 1
    sprite('no604_01', 6)	# 8-13
    SFX_0('008_swing_pole_1')
    sprite('no604_02', 6)	# 14-19
    SFX_0('008_swing_pole_1')
    sprite('no604_03', 6)	# 20-25
    SFX_0('008_swing_pole_1')
    sprite('no604_04', 6)	# 26-31
    sprite('no604_05', 4)	# 32-35
    sprite('no604_05ex01', 4)	# 36-39
    sprite('no604_05ex02', 30)	# 40-69
    sprite('no604_06', 6)	# 70-75
    sprite('no604_07', 6)	# 76-81
    sprite('no604_08', 6)	# 82-87
    sprite('no604_09', 6)	# 88-93
    sprite('no604_10', 6)	# 94-99
    sprite('no604_11', 4)	# 100-103
    sprite('no604_11ex01', 4)	# 104-107
    if SLOT_51:
        SFX_1('bno505')
    label(1)
    sprite('no604_11ex02', 1)	# 108-108
    if SLOT_97:
        _gotolabel(1)
    sprite('no604_11ex02', 30)	# 109-138
    sprite('no604_12', 5)	# 139-143
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    ExitState()
    label(10)
    if sprite('no605_00', 50):	# 144-193
        Unknown7006('bno502', 100, 896495202, 13104, 0, 0, 100, 896495202, 13360, 0, 0, 100, 896495202, 12336, 0, 0, 100)
        SLOT_2 = 1
    sprite('no605_01', 32767)	# 194-32960
    Unknown23018(1)
    ExitState()
    label(20)
    sprite('no000_00', 1)	# 32961-32961
    SFX_1('bno701ryn')
    label(21)
    sprite('no000_00', 7)	# 32962-32968
    sprite('no000_01', 7)	# 32969-32975
    sprite('no000_02', 7)	# 32976-32982
    sprite('no000_03', 7)	# 32983-32989
    sprite('no000_04', 7)	# 32990-32996
    sprite('no000_05', 7)	# 32997-33003
    sprite('no000_06', 7)	# 33004-33010
    sprite('no000_07', 7)	# 33011-33017
    gotoLabel(21)
    label(100)
    if (not SLOT_158):
        Unknown1000(-1230000)
    sprite('no000_00', 7)	# 33018-33024
    sprite('no000_01', 7)	# 33025-33031
    sprite('no000_02', 7)	# 33032-33038
    sprite('no000_03', 7)	# 33039-33045
    sprite('no000_04', 7)	# 33046-33052
    sprite('no000_05', 7)	# 33053-33059
    sprite('no000_06', 7)	# 33060-33066
    sprite('no000_07', 7)	# 33067-33073
    GFX_0('Act3Event_ExclamationControl', -1)
    sprite('no000_00', 7)	# 33074-33080
    sprite('no000_01', 7)	# 33081-33087
    sprite('no000_02', 7)	# 33088-33094
    SFX_1('bno600brg')
    sprite('no000_03', 7)	# 33095-33101
    sprite('no000_04', 7)	# 33102-33108
    sprite('no000_05', 7)	# 33109-33115
    sprite('no000_06', 7)	# 33116-33122
    sprite('no000_07', 7)	# 33123-33129
    sprite('no000_00', 7)	# 33130-33136
    sprite('no003_00', 5)	# 33137-33141
    Unknown2005()
    sprite('no003_01', 5)	# 33142-33146
    sprite('no003_02', 5)	# 33147-33151
    sprite('no000_01', 7)	# 33152-33158
    sprite('no000_02', 7)	# 33159-33165
    sprite('no000_03', 7)	# 33166-33172
    sprite('no000_04', 7)	# 33173-33179
    sprite('no000_05', 7)	# 33180-33186
    sprite('no000_06', 7)	# 33187-33193
    sprite('no000_07', 7)	# 33194-33200
    sprite('no000_00', 7)	# 33201-33207
    sprite('no000_01', 7)	# 33208-33214
    sprite('no000_02', 7)	# 33215-33221
    sprite('no000_03', 7)	# 33222-33228
    sprite('no000_04', 7)	# 33229-33235
    sprite('no000_05', 7)	# 33236-33242
    sprite('no000_06', 7)	# 33243-33249
    sprite('no000_07', 7)	# 33250-33256
    sprite('no000_00', 7)	# 33257-33263
    sprite('no000_01', 7)	# 33264-33270
    sprite('no000_02', 7)	# 33271-33277
    sprite('no000_03', 7)	# 33278-33284
    sprite('no000_04', 7)	# 33285-33291
    sprite('no000_05', 7)	# 33292-33298
    sprite('no000_06', 7)	# 33299-33305
    sprite('no003_00', 5)	# 33306-33310
    Unknown2005()
    sprite('no003_01', 5)	# 33311-33315
    sprite('no003_02', 5)	# 33316-33320
    sprite('no000_07', 7)	# 33321-33327
    label(101)
    sprite('no000_00', 7)	# 33328-33334
    sprite('no000_01', 7)	# 33335-33341
    sprite('no000_02', 7)	# 33342-33348
    sprite('no000_03', 7)	# 33349-33355
    sprite('no000_04', 7)	# 33356-33362
    sprite('no000_05', 7)	# 33363-33369
    sprite('no000_06', 7)	# 33370-33376
    sprite('no000_07', 7)	# 33377-33383
    if SLOT_97:
        _gotolabel(101)
    sprite('no000_00', 1)	# 33384-33384
    Unknown21007(24, 40)
    Unknown23018(1)
    label(102)
    sprite('no000_00', 7)	# 33385-33391
    sprite('no000_01', 7)	# 33392-33398
    sprite('no000_02', 7)	# 33399-33405
    sprite('no000_03', 7)	# 33406-33412
    sprite('no000_04', 7)	# 33413-33419
    sprite('no000_05', 7)	# 33420-33426
    sprite('no000_06', 7)	# 33427-33433
    sprite('no000_07', 7)	# 33434-33440
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('no000_00', 1)	# 33441-33441
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
        SFX_1('bno601bjn')
    label(111)
    sprite('no000_00', 7)	# 33442-33448
    sprite('no000_01', 7)	# 33449-33455
    sprite('no000_02', 7)	# 33456-33462
    sprite('no000_03', 7)	# 33463-33469
    sprite('no000_04', 7)	# 33470-33476
    sprite('no000_05', 7)	# 33477-33483
    sprite('no000_06', 7)	# 33484-33490
    sprite('no000_07', 7)	# 33491-33497
    gotoLabel(111)
    label(112)
    sprite('no000_00', 7)	# 33498-33504
    sprite('no000_01', 7)	# 33505-33511
    sprite('no000_02', 7)	# 33512-33518
    sprite('no000_03', 7)	# 33519-33525
    sprite('no000_04', 7)	# 33526-33532
    sprite('no000_05', 7)	# 33533-33539
    sprite('no000_06', 7)	# 33540-33546
    sprite('no000_07', 7)	# 33547-33553
    if SLOT_97:
        _gotolabel(112)
    sprite('no000_00', 1)	# 33554-33554
    Unknown21011(120)
    label(113)
    sprite('no000_00', 7)	# 33555-33561
    sprite('no000_01', 7)	# 33562-33568
    sprite('no000_02', 7)	# 33569-33575
    sprite('no000_03', 7)	# 33576-33582
    sprite('no000_04', 7)	# 33583-33589
    sprite('no000_05', 7)	# 33590-33596
    sprite('no000_06', 7)	# 33597-33603
    sprite('no000_07', 7)	# 33604-33610
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('no605_00', 6)	# 33611-33616
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bno600uhy')
    sprite('no605_01', 60)	# 33617-33676
    sprite('no605_02', 6)	# 33677-33682
    sprite('no605_03', 6)	# 33683-33688
    sprite('no605_04', 6)	# 33689-33694
    sprite('no605_05', 6)	# 33695-33700
    sprite('no605_06', 6)	# 33701-33706
    sprite('no605_07', 6)	# 33707-33712
    sprite('no605_08', 1)	# 33713-33713
    label(121)
    sprite('no605_08', 1)	# 33714-33714
    if SLOT_97:
        _gotolabel(121)
    sprite('no605_08', 30)	# 33715-33744
    sprite('no605_09', 6)	# 33745-33750
    Unknown21007(24, 40)
    sprite('no605_10', 6)	# 33751-33756
    Unknown21011(240)
    label(122)
    sprite('no000_00', 7)	# 33757-33763
    sprite('no000_01', 7)	# 33764-33770
    sprite('no000_02', 7)	# 33771-33777
    sprite('no000_03', 7)	# 33778-33784
    sprite('no000_04', 7)	# 33785-33791
    sprite('no000_05', 7)	# 33792-33798
    sprite('no000_06', 7)	# 33799-33805
    sprite('no000_07', 7)	# 33806-33812
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('no000_00', 1)	# 33813-33813
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('no000_00', 7)	# 33814-33820
    sprite('no000_01', 7)	# 33821-33827
    sprite('no000_02', 7)	# 33828-33834
    sprite('no000_03', 7)	# 33835-33841
    sprite('no000_04', 7)	# 33842-33848
    sprite('no000_05', 7)	# 33849-33855
    sprite('no000_06', 7)	# 33856-33862
    sprite('no000_07', 7)	# 33863-33869
    gotoLabel(131)
    label(132)
    sprite('no301_00', 6)	# 33870-33875
    SFX_1('bno601pna')
    sprite('no301_01', 6)	# 33876-33881
    sprite('no301_02', 6)	# 33882-33887
    sprite('no301_03', 6)	# 33888-33893
    sprite('no301_04', 6)	# 33894-33899
    sprite('no301_05', 6)	# 33900-33905
    sprite('no301_06', 8)	# 33906-33913
    sprite('no301_07', 6)	# 33914-33919
    sprite('no301_08', 6)	# 33920-33925
    sprite('no301_09', 6)	# 33926-33931
    sprite('no301_10', 6)	# 33932-33937
    Unknown23018(1)
    label(133)
    sprite('no000_00', 7)	# 33938-33944
    sprite('no000_01', 7)	# 33945-33951
    sprite('no000_02', 7)	# 33952-33958
    sprite('no000_03', 7)	# 33959-33965
    sprite('no000_04', 7)	# 33966-33972
    sprite('no000_05', 7)	# 33973-33979
    sprite('no000_06', 7)	# 33980-33986
    sprite('no000_07', 7)	# 33987-33993
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('no602_00', 32767)	# 33994-66760
    if (not SLOT_158):
        Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bno601bny')

    def upon_39():
        clearUponHandler(39)
        sendToLabel(141)
    label(141)
    sprite('no602_00', 1)	# 66761-66761
    SFX_1('bno603bny')
    label(142)
    sprite('no602_00', 1)	# 66762-66762
    if SLOT_97:
        _gotolabel(142)
    sprite('no602_00', 30)	# 66763-66792
    sprite('no602_01', 6)	# 66793-66798
    sprite('no602_02', 6)	# 66799-66804
    sprite('no602_03', 6)	# 66805-66810
    sprite('no602_04', 6)	# 66811-66816
    sprite('no000_00', 1)	# 66817-66817
    SFX_1('bno604bny')
    label(144)
    sprite('no000_00', 7)	# 66818-66824
    sprite('no000_01', 7)	# 66825-66831
    sprite('no000_02', 7)	# 66832-66838
    sprite('no000_03', 7)	# 66839-66845
    sprite('no000_04', 7)	# 66846-66852
    sprite('no000_05', 7)	# 66853-66859
    sprite('no000_06', 7)	# 66860-66866
    sprite('no000_07', 7)	# 66867-66873
    if SLOT_97:
        _gotolabel(144)
    sprite('no000_00', 1)	# 66874-66874
    Unknown21011(120)
    label(145)
    sprite('no000_00', 7)	# 66875-66881
    sprite('no000_01', 7)	# 66882-66888
    sprite('no000_02', 7)	# 66889-66895
    sprite('no000_03', 7)	# 66896-66902
    sprite('no000_04', 7)	# 66903-66909
    sprite('no000_05', 7)	# 66910-66916
    sprite('no000_06', 7)	# 66917-66923
    sprite('no000_07', 7)	# 66924-66930
    gotoLabel(145)
    ExitState()
    label(150)
    sprite('no605_00', 32767)	# 66931-99697
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(151)
    label(151)
    sprite('no605_01', 60)	# 99698-99757
    SFX_1('bno601bmk')
    sprite('no605_02', 6)	# 99758-99763
    sprite('no605_03', 6)	# 99764-99769
    sprite('no605_04', 6)	# 99770-99775
    sprite('no605_05', 6)	# 99776-99781
    sprite('no605_06', 6)	# 99782-99787
    sprite('no605_07', 6)	# 99788-99793
    label(152)
    sprite('no605_08', 1)	# 99794-99794
    if SLOT_97:
        _gotolabel(152)
    sprite('no605_08', 32767)	# 99795-132561
    Unknown21011(120)
    ExitState()
    label(160)
    sprite('no000_00', 1)	# 132562-132562
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('no001_00', 6)	# 132563-132568
    sprite('no001_01', 6)	# 132569-132574
    SFX_1('bno600uva')
    sprite('no001_02', 6)	# 132575-132580
    sprite('no001_03', 6)	# 132581-132586
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no001_04', 6)	# 132587-132592
    sprite('no001_05', 6)	# 132593-132598
    sprite('no001_06', 6)	# 132599-132604
    SFX_FOOTSTEP_(100, 1, 1)
    label(161)
    sprite('no000_00', 7)	# 132605-132611
    sprite('no000_01', 7)	# 132612-132618
    sprite('no000_02', 7)	# 132619-132625
    sprite('no000_03', 7)	# 132626-132632
    sprite('no000_04', 7)	# 132633-132639
    sprite('no000_05', 7)	# 132640-132646
    sprite('no000_06', 7)	# 132647-132653
    sprite('no000_07', 7)	# 132654-132660
    if SLOT_97:
        _gotolabel(161)
    sprite('no000_00', 1)	# 132661-132661
    Unknown21007(24, 40)
    Unknown21011(240)
    label(162)
    sprite('no000_00', 7)	# 132662-132668
    sprite('no000_01', 7)	# 132669-132675
    sprite('no000_02', 7)	# 132676-132682
    sprite('no000_03', 7)	# 132683-132689
    sprite('no000_04', 7)	# 132690-132696
    sprite('no000_05', 7)	# 132697-132703
    sprite('no000_06', 7)	# 132704-132710
    sprite('no000_07', 7)	# 132711-132717
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('no001_00', 6)	# 132718-132723
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('no001_01', 6)	# 132724-132729
    SFX_1('bno600ryn')
    sprite('no001_02', 6)	# 132730-132735
    sprite('no001_03', 6)	# 132736-132741
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no001_04', 6)	# 132742-132747
    sprite('no001_05', 6)	# 132748-132753
    sprite('no001_06', 6)	# 132754-132759
    SFX_FOOTSTEP_(100, 1, 1)
    label(171)
    sprite('no000_00', 7)	# 132760-132766
    sprite('no000_01', 7)	# 132767-132773
    sprite('no000_02', 7)	# 132774-132780
    sprite('no000_03', 7)	# 132781-132787
    sprite('no000_04', 7)	# 132788-132794
    sprite('no000_05', 7)	# 132795-132801
    sprite('no000_06', 7)	# 132802-132808
    sprite('no000_07', 7)	# 132809-132815
    if SLOT_97:
        _gotolabel(171)
    sprite('no000_00', 1)	# 132816-132816
    Unknown21007(24, 40)
    Unknown21011(150)
    label(172)
    sprite('no000_00', 7)	# 132817-132823
    sprite('no000_01', 7)	# 132824-132830
    sprite('no000_02', 7)	# 132831-132837
    sprite('no000_03', 7)	# 132838-132844
    sprite('no000_04', 7)	# 132845-132851
    sprite('no000_05', 7)	# 132852-132858
    sprite('no000_06', 7)	# 132859-132865
    sprite('no000_07', 7)	# 132866-132872
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('no000_00', 7)	# 132873-132879
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('no000_01', 7)	# 132880-132886
    SFX_1('bno600pla')
    sprite('no000_02', 7)	# 132887-132893
    sprite('no000_03', 7)	# 132894-132900
    sprite('no000_04', 7)	# 132901-132907
    sprite('no000_05', 7)	# 132908-132914
    sprite('no000_06', 7)	# 132915-132921
    sprite('no000_07', 7)	# 132922-132928
    sprite('no301_00', 6)	# 132929-132934
    sprite('no301_01', 6)	# 132935-132940
    sprite('no301_02', 6)	# 132941-132946
    sprite('no301_03', 6)	# 132947-132952
    sprite('no301_04', 6)	# 132953-132958
    sprite('no301_05', 6)	# 132959-132964
    sprite('no301_06', 8)	# 132965-132972
    sprite('no301_07', 6)	# 132973-132978
    sprite('no301_08', 6)	# 132979-132984
    sprite('no301_09', 6)	# 132985-132990
    sprite('no301_10', 6)	# 132991-132996
    label(181)
    sprite('no000_00', 7)	# 132997-133003
    sprite('no000_01', 7)	# 133004-133010
    sprite('no000_02', 7)	# 133011-133017
    sprite('no000_03', 7)	# 133018-133024
    sprite('no000_04', 7)	# 133025-133031
    sprite('no000_05', 7)	# 133032-133038
    sprite('no000_06', 7)	# 133039-133045
    sprite('no000_07', 7)	# 133046-133052
    if SLOT_97:
        _gotolabel(181)
    sprite('no000_00', 1)	# 133053-133053
    Unknown21007(24, 40)
    Unknown21011(270)
    label(182)
    sprite('no000_00', 7)	# 133054-133060
    sprite('no000_01', 7)	# 133061-133067
    sprite('no000_02', 7)	# 133068-133074
    sprite('no000_03', 7)	# 133075-133081
    sprite('no000_04', 7)	# 133082-133088
    sprite('no000_05', 7)	# 133089-133095
    sprite('no000_06', 7)	# 133096-133102
    sprite('no000_07', 7)	# 133103-133109
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('no000_00', 1)	# 133110-133110
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('no000_00', 7)	# 133111-133117
    sprite('no000_01', 7)	# 133118-133124
    sprite('no000_02', 7)	# 133125-133131
    sprite('no000_03', 7)	# 133132-133138
    sprite('no000_04', 7)	# 133139-133145
    sprite('no000_05', 7)	# 133146-133152
    sprite('no000_06', 7)	# 133153-133159
    sprite('no000_07', 7)	# 133160-133166
    gotoLabel(191)
    label(192)
    sprite('no301_00', 6)	# 133167-133172
    SFX_1('bno601bma')
    sprite('no301_01', 6)	# 133173-133178
    sprite('no301_02', 6)	# 133179-133184
    sprite('no301_03', 6)	# 133185-133190
    sprite('no301_04', 6)	# 133191-133196
    sprite('no301_05', 6)	# 133197-133202
    sprite('no301_06', 8)	# 133203-133210
    sprite('no301_07', 6)	# 133211-133216
    sprite('no301_08', 6)	# 133217-133222
    sprite('no301_09', 6)	# 133223-133228
    sprite('no301_10', 6)	# 133229-133234
    Unknown23018(1)
    label(193)
    sprite('no000_00', 7)	# 133235-133241
    sprite('no000_01', 7)	# 133242-133248
    sprite('no000_02', 7)	# 133249-133255
    sprite('no000_03', 7)	# 133256-133262
    sprite('no000_04', 7)	# 133263-133269
    sprite('no000_05', 7)	# 133270-133276
    sprite('no000_06', 7)	# 133277-133283
    sprite('no000_07', 7)	# 133284-133290
    gotoLabel(193)
    ExitState()
    label(200)
    sprite('no000_00', 1)	# 133291-133291
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('no000_00', 7)	# 133292-133298
    sprite('no000_01', 7)	# 133299-133305
    sprite('no000_02', 7)	# 133306-133312
    sprite('no000_03', 7)	# 133313-133319
    sprite('no000_04', 7)	# 133320-133326
    sprite('no000_05', 7)	# 133327-133333
    sprite('no000_06', 7)	# 133334-133340
    sprite('no000_07', 7)	# 133341-133347
    gotoLabel(201)
    label(202)
    sprite('no301_00', 6)	# 133348-133353
    SFX_1('bno601biz')
    sprite('no301_01', 6)	# 133354-133359
    sprite('no301_02', 6)	# 133360-133365
    sprite('no301_03', 6)	# 133366-133371
    sprite('no301_04', 6)	# 133372-133377
    sprite('no301_05', 6)	# 133378-133383
    sprite('no301_06', 8)	# 133384-133391
    sprite('no301_07', 6)	# 133392-133397
    sprite('no301_08', 6)	# 133398-133403
    sprite('no301_09', 6)	# 133404-133409
    sprite('no301_10', 6)	# 133410-133415
    Unknown23018(1)
    label(203)
    sprite('no000_00', 7)	# 133416-133422
    sprite('no000_01', 7)	# 133423-133429
    sprite('no000_02', 7)	# 133430-133436
    sprite('no000_03', 7)	# 133437-133443
    sprite('no000_04', 7)	# 133444-133450
    sprite('no000_05', 7)	# 133451-133457
    sprite('no000_06', 7)	# 133458-133464
    sprite('no000_07', 7)	# 133465-133471
    gotoLabel(203)
    label(210)
    sprite('no000_00', 1)	# 133472-133472

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('no000_00', 7)	# 133473-133479
    sprite('no000_01', 7)	# 133480-133486
    sprite('no000_02', 7)	# 133487-133493
    sprite('no000_03', 7)	# 133494-133500
    sprite('no000_04', 7)	# 133501-133507
    sprite('no000_05', 7)	# 133508-133514
    sprite('no000_06', 7)	# 133515-133521
    sprite('no000_07', 7)	# 133522-133528
    gotoLabel(211)
    label(212)
    sprite('no001_00', 6)	# 133529-133534
    sprite('no001_01', 6)	# 133535-133540
    SFX_1('bno601bce')
    Unknown23018(1)
    sprite('no001_02', 6)	# 133541-133546
    sprite('no001_03', 6)	# 133547-133552
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no001_04', 6)	# 133553-133558
    sprite('no001_05', 6)	# 133559-133564
    sprite('no001_06', 6)	# 133565-133570
    SFX_FOOTSTEP_(100, 1, 1)
    label(213)
    sprite('no000_00', 7)	# 133571-133577
    sprite('no000_01', 7)	# 133578-133584
    sprite('no000_02', 7)	# 133585-133591
    sprite('no000_03', 7)	# 133592-133598
    sprite('no000_04', 7)	# 133599-133605
    sprite('no000_05', 7)	# 133606-133612
    sprite('no000_06', 7)	# 133613-133619
    sprite('no000_07', 7)	# 133620-133626
    gotoLabel(213)
    label(220)
    sprite('no611_10', 1)	# 133627-133627

    def upon_40():
        clearUponHandler(40)
        sendToLabel(221)
    sprite('no611_10', 32767)	# 133628-166394
    label(221)
    sprite('no611_10', 100)	# 166395-166494
    SFX_1('bno601ahe')
    sprite('no611_09', 6)	# 166495-166500
    sprite('no611_08', 6)	# 166501-166506
    sprite('no611_07', 6)	# 166507-166512
    sprite('no611_06', 6)	# 166513-166518
    sprite('no611_05', 6)	# 166519-166524
    sprite('no611_04', 6)	# 166525-166530
    sprite('no611_03', 6)	# 166531-166536
    sprite('no611_02', 6)	# 166537-166542
    sprite('no611_01', 6)	# 166543-166548
    sprite('no611_00', 6)	# 166549-166554
    Unknown23018(1)
    label(223)
    sprite('no000_00', 7)	# 166555-166561
    sprite('no000_01', 7)	# 166562-166568
    sprite('no000_02', 7)	# 166569-166575
    sprite('no000_03', 7)	# 166576-166582
    sprite('no000_04', 7)	# 166583-166589
    sprite('no000_05', 7)	# 166590-166596
    sprite('no000_06', 7)	# 166597-166603
    sprite('no000_07', 7)	# 166604-166610
    gotoLabel(223)
    label(1000)
    sprite('no000_00', 7)	# 166611-166617
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 10003):
            sendToLabel(1002)
    label(1001)
    sprite('no000_01', 7)	# 166618-166624
    sprite('no000_02', 7)	# 166625-166631
    sprite('no000_03', 7)	# 166632-166638
    sprite('no000_04', 7)	# 166639-166645
    sprite('no000_05', 7)	# 166646-166652
    sprite('no000_06', 7)	# 166653-166659
    sprite('no000_07', 7)	# 166660-166666
    sprite('no000_00', 7)	# 166667-166673
    gotoLabel(1001)
    label(1002)
    sprite('no651_00', 7)	# 166674-166680
    SFX_1('bno603')
    sprite('no651_01', 7)	# 166681-166687
    sprite('no651_02', 7)	# 166688-166694
    sprite('no651_03', 7)	# 166695-166701
    sprite('no651_04', 7)	# 166702-166708
    sprite('no651_05', 7)	# 166709-166715
    label(1003)
    sprite('no651_06', 1)	# 166716-166716
    if SLOT_97:
        _gotolabel(1003)
    sprite('no651_06', 30)	# 166717-166746
    sprite('no651_06', 32767)	# 166747-199513
    Unknown23029(24, 10004, 0)
    Unknown23029(22, 10004, 0)
    Unknown23029(23, 10004, 0)
    Unknown18008()
    label(991)
    sprite('no000_00', 1)	# 199514-199514
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('no000_00', 7)	# 199515-199521
    sprite('no000_01', 7)	# 199522-199528
    sprite('no000_02', 7)	# 199529-199535
    sprite('no000_03', 7)	# 199536-199542
    sprite('no000_04', 7)	# 199543-199549
    sprite('no000_05', 7)	# 199550-199556
    sprite('no000_06', 7)	# 199557-199563
    sprite('no000_07', 7)	# 199564-199570
    gotoLabel(992)
    label(993)
    sprite('no033_00', 1)	# 199571-199571

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(995)

    def upon_STATE_END():
        Unknown2019(0)
        Unknown3038(1)
        Unknown3001(255)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown3001(255)
    Unknown3004(-20)
    physicsXImpulse(-51000)
    physicsYImpulse(18800)
    setGravity(1500)
    Unknown8002()
    sprite('no033_01', 2)	# 199572-199573
    label(994)
    sprite('no033_02', 3)	# 199574-199576
    sprite('no033_03', 3)	# 199577-199579
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 199580-199582
    ExitState()

@State
def CmnActRoundWin():
    pass

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
            if PartnerChar('brg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('biz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('bce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('ahe'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    if (SLOT_25 >= 300000):
        if (SLOT_26 >= 300000):
            if random_(2, 0, 50):
                gotoLabel(10)
    sprite('no611_00', 6)	# 4-9
    sprite('no611_01', 6)	# 10-15
    sprite('no611_02', 6)	# 16-21
    sprite('no611_03', 6)	# 22-27
    sprite('no611_04', 6)	# 28-33
    sprite('no611_05', 6)	# 34-39
    sprite('no611_06', 6)	# 40-45
    sprite('no611_07', 6)	# 46-51
    sprite('no611_08', 6)	# 52-57
    sprite('no611_09', 6)	# 58-63
    sprite('no611_10', 6)	# 64-69
    sprite('no611_11', 6)	# 70-75
    sprite('no611_12', 6)	# 76-81
    sprite('no611_13', 6)	# 82-87
    sprite('no611_14', 6)	# 88-93
    Unknown36(24)
    Unknown2034(0)
    Unknown2053(0)
    Unknown35()
    Unknown2004(1, 0)
    EnableCollision(0)
    sprite('no611_15', 6)	# 94-99
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown2015(140)
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bno524', 100, 896495202, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('', 0, 879717986, 828322864, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bno523', 100, 896495202, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('no611_16', 6)	# 100-105
    sprite('no611_17', 6)	# 106-111
    Unknown51(1)
    ExitState()
    label(10)
    sprite('no612_00', 6)	# 112-117
    sprite('no612_01', 7)	# 118-124
    sprite('no612_02', 7)	# 125-131
    sprite('no612_03', 4)	# 132-135
    sprite('no612_04', 6)	# 136-141
    sprite('no612_05', 6)	# 142-147
    sprite('no612_06', 6)	# 148-153
    sprite('no612_07', 6)	# 154-159
    sprite('no612_08', 6)	# 160-165
    sprite('no612_09', 6)	# 166-171
    SFX_0('019_cloth_b')
    sprite('no612_10', 6)	# 172-177
    sprite('no612_11', 6)	# 178-183
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bno524', 100, 896495202, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bno404_0', 100, 879717986, 828322864, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bno520', 100, 896495202, 12850, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    loopRest()
    label(11)
    sprite('no612_12', 7)	# 184-190
    sprite('no612_13', 7)	# 191-197
    sprite('no612_14', 7)	# 198-204
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('no620_00', 6)	# 205-210
    SFX_1('bno700brg')
    sprite('no620_01', 6)	# 211-216
    sprite('no620_02', 6)	# 217-222
    sprite('no620_03', 6)	# 223-228
    sprite('no620_04', 6)	# 229-234
    sprite('no620_05', 6)	# 235-240
    sprite('no620_06', 6)	# 241-246
    Unknown8000(100, 1, 1)
    sprite('no620_07', 6)	# 247-252
    label(101)
    sprite('no620_08', 1)	# 253-253
    if SLOT_97:
        _gotolabel(101)
    sprite('no620_08', 32767)	# 254-33020
    Unknown21007(24, 40)
    Unknown21011(280)
    label(110)
    sprite('no612_00', 6)	# 33021-33026

    def upon_40():
        clearUponHandler(40)
        SFX_1('bno702bjn')
        Unknown23018(1)
    sprite('no612_01', 7)	# 33027-33033
    sprite('no612_02', 7)	# 33034-33040
    sprite('no612_03', 4)	# 33041-33044
    sprite('no612_04', 6)	# 33045-33050
    sprite('no612_05', 6)	# 33051-33056
    sprite('no612_06', 6)	# 33057-33062
    sprite('no612_07', 6)	# 33063-33068
    sprite('no612_08', 6)	# 33069-33074
    sprite('no612_09', 6)	# 33075-33080
    SFX_0('019_cloth_b')
    sprite('no612_10', 6)	# 33081-33086
    sprite('no612_11', 6)	# 33087-33092
    SFX_1('bno700bjn')
    label(111)
    sprite('no612_12', 7)	# 33093-33099
    sprite('no612_13', 7)	# 33100-33106
    sprite('no612_14', 7)	# 33107-33113
    if SLOT_97:
        _gotolabel(111)
    sprite('no612_12', 1)	# 33114-33114
    Unknown21007(24, 40)
    label(112)
    sprite('no612_12', 7)	# 33115-33121
    sprite('no612_13', 7)	# 33122-33128
    sprite('no612_14', 7)	# 33129-33135
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('no000_00', 1)	# 33136-33136
    if (not SLOT_158):
        Unknown2019(-1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('no000_00', 7)	# 33137-33143
    sprite('no000_01', 7)	# 33144-33150
    sprite('no000_02', 7)	# 33151-33157
    sprite('no000_03', 7)	# 33158-33164
    sprite('no000_04', 7)	# 33165-33171
    sprite('no000_05', 7)	# 33172-33178
    sprite('no000_06', 7)	# 33179-33185
    sprite('no000_07', 7)	# 33186-33192
    gotoLabel(121)
    label(122)
    sprite('no602_04', 6)	# 33193-33198
    sprite('no602_03', 6)	# 33199-33204
    sprite('no602_02', 6)	# 33205-33210
    sprite('no602_01', 6)	# 33211-33216
    sprite('no602_00', 6)	# 33217-33222
    SFX_1('bno701bny')
    label(123)
    sprite('no602_00', 1)	# 33223-33223
    if SLOT_97:
        _gotolabel(123)
    sprite('no602_00', 30)	# 33224-33253
    sprite('no602_01', 6)	# 33254-33259
    sprite('no602_02', 6)	# 33260-33265
    sprite('no602_03', 6)	# 33266-33271
    sprite('no602_04', 6)	# 33272-33277
    sprite('no000_00', 1)	# 33278-33278
    SFX_1('bno702bny')
    sprite('no301_00', 6)	# 33279-33284
    sprite('no301_01', 6)	# 33285-33290
    sprite('no301_02', 6)	# 33291-33296
    sprite('no301_03', 6)	# 33297-33302
    sprite('no301_04', 6)	# 33303-33308
    sprite('no301_05', 6)	# 33309-33314
    sprite('no301_06', 8)	# 33315-33322
    sprite('no301_07', 6)	# 33323-33328
    sprite('no301_08', 6)	# 33329-33334
    sprite('no301_09', 6)	# 33335-33340
    sprite('no301_10', 6)	# 33341-33346
    Unknown21011(180)
    label(124)
    sprite('no000_00', 7)	# 33347-33353
    sprite('no000_01', 7)	# 33354-33360
    sprite('no000_02', 7)	# 33361-33367
    sprite('no000_03', 7)	# 33368-33374
    sprite('no000_04', 7)	# 33375-33381
    sprite('no000_05', 7)	# 33382-33388
    sprite('no000_06', 7)	# 33389-33395
    sprite('no000_07', 7)	# 33396-33402
    gotoLabel(124)
    label(130)
    sprite('no612_00', 6)	# 33403-33408
    sprite('no612_01', 7)	# 33409-33415
    sprite('no612_02', 7)	# 33416-33422
    sprite('no612_03', 4)	# 33423-33426
    sprite('no612_04', 6)	# 33427-33432
    sprite('no612_05', 6)	# 33433-33438
    sprite('no612_06', 6)	# 33439-33444
    sprite('no612_07', 6)	# 33445-33450
    sprite('no612_08', 6)	# 33451-33456
    sprite('no612_09', 6)	# 33457-33462
    SFX_0('019_cloth_b')
    sprite('no612_10', 6)	# 33463-33468
    sprite('no612_11', 6)	# 33469-33474
    SFX_1('bno700pna')
    label(131)
    sprite('no612_12', 7)	# 33475-33481
    sprite('no612_13', 7)	# 33482-33488
    sprite('no612_14', 7)	# 33489-33495
    if SLOT_97:
        _gotolabel(131)
    sprite('no612_12', 1)	# 33496-33496
    Unknown2034(0)
    Unknown2053(0)
    Unknown21007(24, 40)
    Unknown21011(300)
    label(132)
    sprite('no612_12', 7)	# 33497-33503
    sprite('no612_13', 7)	# 33504-33510
    sprite('no612_14', 7)	# 33511-33517
    loopRest()
    gotoLabel(132)
    label(140)
    sprite('no651_00', 7)	# 33518-33524
    SFX_1('bno700uhy')
    sprite('no651_01', 7)	# 33525-33531
    sprite('no651_02', 60)	# 33532-33591
    sprite('no651_03', 7)	# 33592-33598
    sprite('no651_04', 7)	# 33599-33605
    sprite('no651_05', 7)	# 33606-33612
    label(141)
    sprite('no651_06', 1)	# 33613-33613
    if SLOT_97:
        _gotolabel(141)
    sprite('no651_06', 30)	# 33614-33643
    Unknown21007(24, 40)
    sprite('no651_06', 32767)	# 33644-66410
    Unknown21011(120)
    label(150)
    sprite('no000_00', 1)	# 66411-66411

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('no000_00', 7)	# 66412-66418
    sprite('no000_01', 7)	# 66419-66425
    sprite('no000_02', 7)	# 66426-66432
    sprite('no000_03', 7)	# 66433-66439
    sprite('no000_04', 7)	# 66440-66446
    sprite('no000_05', 7)	# 66447-66453
    sprite('no000_06', 7)	# 66454-66460
    sprite('no000_07', 7)	# 66461-66467
    gotoLabel(151)
    label(152)
    sprite('no651_00', 6)	# 66468-66473
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
    SFX_1('bno701uva')
    sprite('no651_00', 1)	# 66474-66474
    GFX_0('Act3Event_ExclamationControl', -1)
    Unknown23018(1)
    sprite('no651_01', 32767)	# 66475-99241
    label(160)
    sprite('no000_00', 1)	# 99242-99242

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('no000_00', 7)	# 99243-99249
    sprite('no000_01', 7)	# 99250-99256
    sprite('no000_02', 7)	# 99257-99263
    sprite('no000_03', 7)	# 99264-99270
    sprite('no000_04', 7)	# 99271-99277
    sprite('no000_05', 7)	# 99278-99284
    sprite('no000_06', 7)	# 99285-99291
    sprite('no000_07', 7)	# 99292-99298
    gotoLabel(161)
    label(162)
    sprite('no301_00', 6)	# 99299-99304
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
    SFX_1('bno701bmk')
    sprite('no301_01', 6)	# 99305-99310
    sprite('no301_02', 6)	# 99311-99316
    sprite('no301_03', 6)	# 99317-99322
    sprite('no301_04', 6)	# 99323-99328
    sprite('no301_05', 6)	# 99329-99334
    sprite('no301_06', 8)	# 99335-99342
    sprite('no301_07', 6)	# 99343-99348
    sprite('no301_08', 6)	# 99349-99354
    sprite('no301_09', 6)	# 99355-99360
    sprite('no301_10', 6)	# 99361-99366
    Unknown23018(1)
    label(163)
    sprite('no000_00', 7)	# 99367-99373
    sprite('no000_01', 7)	# 99374-99380
    sprite('no000_02', 7)	# 99381-99387
    sprite('no000_03', 7)	# 99388-99394
    sprite('no000_04', 7)	# 99395-99401
    sprite('no000_05', 7)	# 99402-99408
    sprite('no000_06', 7)	# 99409-99415
    sprite('no000_07', 7)	# 99416-99422
    gotoLabel(163)
    label(170)
    sprite('no000_00', 1)	# 99423-99423

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('no000_00', 7)	# 99424-99430
    sprite('no000_01', 7)	# 99431-99437
    sprite('no000_02', 7)	# 99438-99444
    sprite('no000_03', 7)	# 99445-99451
    sprite('no000_04', 7)	# 99452-99458
    sprite('no000_05', 7)	# 99459-99465
    sprite('no000_06', 7)	# 99466-99472
    sprite('no000_07', 7)	# 99473-99479
    gotoLabel(171)
    label(172)
    sprite('no301_00', 6)	# 99480-99485
    SFX_1('bno701ryn')
    sprite('no301_01', 6)	# 99486-99491
    sprite('no301_02', 6)	# 99492-99497
    sprite('no301_03', 6)	# 99498-99503
    sprite('no301_04', 6)	# 99504-99509
    sprite('no301_05', 6)	# 99510-99515
    sprite('no301_06', 8)	# 99516-99523
    sprite('no301_07', 6)	# 99524-99529
    sprite('no301_08', 6)	# 99530-99535
    sprite('no301_09', 6)	# 99536-99541
    sprite('no301_10', 6)	# 99542-99547
    Unknown23018(1)
    label(173)
    sprite('no000_00', 7)	# 99548-99554
    sprite('no000_01', 7)	# 99555-99561
    sprite('no000_02', 7)	# 99562-99568
    sprite('no000_03', 7)	# 99569-99575
    sprite('no000_04', 7)	# 99576-99582
    sprite('no000_05', 7)	# 99583-99589
    sprite('no000_06', 7)	# 99590-99596
    sprite('no000_07', 7)	# 99597-99603
    gotoLabel(173)
    label(180)
    sprite('no000_00', 1)	# 99604-99604

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('no000_00', 7)	# 99605-99611
    sprite('no000_01', 7)	# 99612-99618
    sprite('no000_02', 7)	# 99619-99625
    sprite('no000_03', 7)	# 99626-99632
    sprite('no000_04', 7)	# 99633-99639
    sprite('no000_05', 7)	# 99640-99646
    sprite('no000_06', 7)	# 99647-99653
    sprite('no000_07', 7)	# 99654-99660
    gotoLabel(181)
    label(182)
    sprite('no651_00', 7)	# 99661-99667
    SFX_1('bno701pla')
    sprite('no651_01', 7)	# 99668-99674
    sprite('no651_02', 170)	# 99675-99844
    sprite('no651_03', 7)	# 99845-99851
    sprite('no651_04', 7)	# 99852-99858
    sprite('no651_05', 7)	# 99859-99865
    sprite('no651_06', 32767)	# 99866-132632
    Unknown23018(1)
    label(190)
    sprite('no612_00', 6)	# 132633-132638
    sprite('no612_01', 7)	# 132639-132645
    sprite('no612_02', 7)	# 132646-132652
    sprite('no612_03', 4)	# 132653-132656
    sprite('no612_04', 6)	# 132657-132662
    sprite('no612_05', 6)	# 132663-132668
    sprite('no612_06', 6)	# 132669-132674
    sprite('no612_07', 6)	# 132675-132680
    sprite('no612_08', 6)	# 132681-132686
    sprite('no612_09', 6)	# 132687-132692
    SFX_0('019_cloth_b')
    sprite('no612_10', 6)	# 132693-132698
    sprite('no612_11', 6)	# 132699-132704
    SFX_1('bno700bma')
    label(191)
    sprite('no612_12', 7)	# 132705-132711
    sprite('no612_13', 7)	# 132712-132718
    sprite('no612_14', 7)	# 132719-132725
    if SLOT_97:
        _gotolabel(191)
    sprite('no612_12', 1)	# 132726-132726
    Unknown21007(24, 40)
    Unknown21011(220)
    label(192)
    sprite('no612_12', 7)	# 132727-132733
    sprite('no612_13', 7)	# 132734-132740
    sprite('no612_14', 7)	# 132741-132747
    loopRest()
    gotoLabel(192)
    label(200)
    sprite('no000_00', 1)	# 132748-132748

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('no000_00', 7)	# 132749-132755
    sprite('no000_01', 7)	# 132756-132762
    sprite('no000_02', 7)	# 132763-132769
    sprite('no000_03', 7)	# 132770-132776
    sprite('no000_04', 7)	# 132777-132783
    sprite('no000_05', 7)	# 132784-132790
    sprite('no000_06', 7)	# 132791-132797
    sprite('no000_07', 7)	# 132798-132804
    gotoLabel(201)
    label(202)
    sprite('no301_00', 6)	# 132805-132810
    SFX_1('bno701biz')
    sprite('no301_01', 6)	# 132811-132816
    sprite('no301_02', 6)	# 132817-132822
    sprite('no301_03', 6)	# 132823-132828
    sprite('no301_04', 6)	# 132829-132834
    sprite('no301_05', 6)	# 132835-132840
    sprite('no301_06', 8)	# 132841-132848
    sprite('no301_07', 6)	# 132849-132854
    sprite('no301_08', 6)	# 132855-132860
    sprite('no301_09', 6)	# 132861-132866
    sprite('no301_10', 6)	# 132867-132872
    Unknown23018(1)
    label(203)
    sprite('no000_00', 7)	# 132873-132879
    sprite('no000_01', 7)	# 132880-132886
    sprite('no000_02', 7)	# 132887-132893
    sprite('no000_03', 7)	# 132894-132900
    sprite('no000_04', 7)	# 132901-132907
    sprite('no000_05', 7)	# 132908-132914
    sprite('no000_06', 7)	# 132915-132921
    sprite('no000_07', 7)	# 132922-132928
    gotoLabel(203)
    label(210)
    sprite('no612_00', 6)	# 132929-132934
    sprite('no612_01', 7)	# 132935-132941
    sprite('no612_02', 7)	# 132942-132948
    sprite('no612_03', 4)	# 132949-132952
    sprite('no612_04', 6)	# 132953-132958
    sprite('no612_05', 6)	# 132959-132964
    sprite('no612_06', 6)	# 132965-132970
    sprite('no612_07', 6)	# 132971-132976
    sprite('no612_08', 6)	# 132977-132982
    sprite('no612_09', 6)	# 132983-132988
    SFX_0('019_cloth_b')
    sprite('no612_10', 6)	# 132989-132994
    sprite('no612_11', 6)	# 132995-133000
    SFX_1('bno700bce')
    label(211)
    sprite('no612_12', 7)	# 133001-133007
    sprite('no612_13', 7)	# 133008-133014
    sprite('no612_14', 7)	# 133015-133021
    if SLOT_97:
        _gotolabel(211)
    sprite('no612_12', 1)	# 133022-133022
    Unknown21007(24, 40)
    Unknown21011(150)
    label(212)
    sprite('no612_12', 7)	# 133023-133029
    sprite('no612_13', 7)	# 133030-133036
    sprite('no612_14', 7)	# 133037-133043
    loopRest()
    gotoLabel(212)
    label(220)
    sprite('no611_00', 6)	# 133044-133049

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    sprite('no611_01', 6)	# 133050-133055
    sprite('no611_02', 6)	# 133056-133061
    sprite('no611_03', 6)	# 133062-133067
    sprite('no611_04', 6)	# 133068-133073
    sprite('no611_05', 6)	# 133074-133079
    sprite('no611_06', 6)	# 133080-133085
    sprite('no611_07', 6)	# 133086-133091
    sprite('no611_08', 6)	# 133092-133097
    sprite('no611_09', 6)	# 133098-133103
    sprite('no611_10', 6)	# 133104-133109
    sprite('no611_11', 6)	# 133110-133115
    sprite('no611_12', 6)	# 133116-133121
    sprite('no611_13', 6)	# 133122-133127
    sprite('no611_14', 6)	# 133128-133133
    Unknown2004(1, 0)
    EnableCollision(0)
    sprite('no611_15', 6)	# 133134-133139
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown2015(140)
    sprite('no611_16', 6)	# 133140-133145
    SFX_1('bno700ahe')
    label(221)
    sprite('no611_17', 6)	# 133146-133151
    if SLOT_97:
        _gotolabel(221)
    sprite('no611_17', 32767)	# 133152-165918
    Unknown21007(24, 40)
    label(222)
    sprite('no611_17', 6)	# 165919-165924
    SFX_1('bno702ahe')
    label(223)
    sprite('no611_17', 6)	# 165925-165930
    if SLOT_97:
        _gotolabel(223)
    sprite('no611_17', 32767)	# 165931-198697
    Unknown21011(30)

@State
def CmnActLose():
    sprite('no620_00', 6)	# 1-6
    if random_(2, 0, 50):
        SFX_1('bno403_0')
    else:
        SFX_1('bno403_1')
    sprite('no620_01', 6)	# 7-12
    sprite('no620_02', 6)	# 13-18
    sprite('no620_03', 6)	# 19-24
    sprite('no620_04', 6)	# 25-30
    Unknown23018(1)
    sprite('no620_05', 6)	# 31-36
    sprite('no620_06', 6)	# 37-42
    Unknown8000(100, 1, 1)
    sprite('no620_07', 6)	# 43-48
    sprite('no620_08', 6)	# 49-54
    Unknown51(1)

@State
def EventDefEntryWait():
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryStand():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefWin():
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)

@State
def EventDefLose():
    sprite('no620_08', 32767)	# 1-32767

@State
def EventEntryDark():
    sprite('no602_00', 32767)	# 1-32767
    loopRest()

@State
def EventEntryDarkToStand():
    sprite('no602_01', 6)	# 1-6
    sprite('no602_02', 6)	# 7-12
    sprite('no602_03', 6)	# 13-18
    sprite('no602_04', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def EventCapeEntryWait():
    label(0)
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def EventCapeEntry():
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    sprite('no601_04', 6)	# 25-30
    sprite('no601_05', 6)	# 31-36
    sprite('no601_06', 6)	# 37-42
    sprite('no601_07', 6)	# 43-48
    SFX_0('019_cloth_b')
    sprite('no601_08', 6)	# 49-54
    GFX_0('noef601manto', 0)
    sprite('no601_09', 6)	# 55-60
    sprite('no601_10', 6)	# 61-66
    sprite('no601_11', 6)	# 67-72
    sprite('no601_12', 6)	# 73-78
    loopRest()
    enterState('CmnActStand')

@State
def EventYoroke():
    sprite('no070_04', 32767)	# 1-32767
    loopRest()

@State
def EventYorokeToStand():
    sprite('no070_04', 6)	# 1-6
    sprite('no070_12', 6)	# 7-12
    sprite('no070_13', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def EventDashScreenOut():
    sprite('no032_00', 1)	# 1-1
    Unknown2005()
    Unknown2034(0)
    EnableCollision(0)
    sprite('no032_00', 1)	# 2-2
    physicsXImpulse(32000)
    sprite('no032_01', 2)	# 3-4
    sprite('no032_02', 4)	# 5-8
    sprite('no032_03', 4)	# 9-12
    sprite('no032_04', 4)	# 13-16
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 17-20
    sprite('no032_06', 4)	# 21-24
    sprite('no032_07', 4)	# 25-28
    sprite('no032_08', 4)	# 29-32
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 33-36
    sprite('no032_02', 4)	# 37-40
    sprite('no032_03', 4)	# 41-44
    sprite('no032_04', 4)	# 45-48
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 49-52
    sprite('no032_06', 4)	# 53-56
    sprite('no032_07', 4)	# 57-60
    sprite('no032_08', 4)	# 61-64
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 65-68
    sprite('no032_02', 4)	# 69-72
    sprite('no032_03', 4)	# 73-76
    sprite('no032_04', 4)	# 77-80
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 81-84
    sprite('no032_06', 4)	# 85-88
    sprite('no032_07', 4)	# 89-92
    sprite('no032_08', 4)	# 93-96
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 97-100
    sprite('no032_02', 4)	# 101-104
    sprite('no032_03', 4)	# 105-108
    sprite('no032_04', 4)	# 109-112
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 113-116
    sprite('no032_06', 4)	# 117-120
    sprite('no032_07', 4)	# 121-124
    sprite('no032_08', 4)	# 125-128
    Unknown8006(100, 1, 1)
    sprite('no032_09', 32767)	# 129-32895
    loopRest()

@State
def EventChangeToMu():
    sprite('no611_00', 6)	# 1-6
    sprite('no611_01', 6)	# 7-12
    sprite('no611_02', 6)	# 13-18
    sprite('no611_03', 6)	# 19-24
    sprite('no611_04', 6)	# 25-30
    sprite('no611_05', 6)	# 31-36
    sprite('no611_06', 6)	# 37-42
    sprite('no611_07', 6)	# 43-48
    sprite('no611_08', 6)	# 49-54
    sprite('no611_09', 6)	# 55-60
    SFX_0('302_spsys_drivemotion')
    GFX_1('ef_kakusei', 103)
    sprite('no611_10', 32767)	# 61-32827
    loopRest()

@State
def EventNOVsAM_DarkAngryStart():
    sprite('no602_04', 5)	# 1-5
    sprite('no602_03', 5)	# 6-10
    sprite('no602_02', 5)	# 11-15
    sprite('no602_01', 5)	# 16-20
    sprite('no602_00', 32767)	# 21-32787
    loopRest()

@State
def EventNOVsAM_DarkAngryEnd():
    sprite('no602_01', 5)	# 1-5
    sprite('no602_02', 5)	# 6-10
    sprite('no602_03', 5)	# 11-15
    sprite('no602_04', 5)	# 16-20
    loopRest()
    enterState('CmnActStand')

@State
def EventVSPT1():
    sprite('no000_00', 1)	# 1-1
    Unknown2005()
    label(0)
    sprite('no000_00', 7)	# 2-8
    sprite('no000_01', 7)	# 9-15
    sprite('no000_02', 7)	# 16-22
    sprite('no000_03', 7)	# 23-29
    sprite('no000_04', 7)	# 30-36
    sprite('no000_05', 7)	# 37-43
    sprite('no000_06', 7)	# 44-50
    sprite('no000_07', 7)	# 51-57
    loopRest()
    gotoLabel(0)
    loopRest()

@State
def EventVSPT2():
    sprite('no003_00', 6)	# 1-6
    Unknown2005()
    sprite('no003_01', 6)	# 7-12
    sprite('no003_02', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def EventNOCenterStand():
    Unknown1000(0)
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)

@State
def EventNOStandToHetari():
    sprite('no620_00', 4)	# 1-4
    sprite('no620_01', 4)	# 5-8
    sprite('no620_02', 4)	# 9-12
    sprite('no620_03', 4)	# 13-16
    sprite('no620_04', 4)	# 17-20
    sprite('no620_05', 4)	# 21-24
    sprite('no620_06', 4)	# 25-28
    sprite('no620_07', 4)	# 29-32
    sprite('no620_08', 32767)	# 33-32799

@State
def EventNOHetariUp():
    sprite('no620_07', 32767)	# 1-32767

@State
def EventNOHetari():
    sprite('no620_08', 32767)	# 1-32767

@State
def EventNOHetariDown():
    sprite('no064_02', 9)	# 1-9
    sprite('no064_01', 7)	# 10-16
    sprite('no064_00', 7)	# 17-23
    sprite('no063_10', 32767)	# 24-32790

@State
def EventNOHetariToStand():
    sprite('no620_08', 4)	# 1-4
    sprite('no620_07', 4)	# 5-8
    sprite('no620_06', 4)	# 9-12
    sprite('no620_05', 4)	# 13-16
    sprite('no620_04', 4)	# 17-20
    sprite('no620_03', 4)	# 21-24
    sprite('no620_02', 4)	# 25-28
    sprite('no620_01', 4)	# 29-32
    sprite('no620_00', 4)	# 33-36
    sprite('no000_00', 7)	# 37-43
    sprite('no000_01', 7)	# 44-50
    sprite('no000_02', 7)	# 51-57
    sprite('no000_03', 7)	# 58-64
    sprite('no000_04', 7)	# 65-71
    sprite('no000_05', 7)	# 72-78
    sprite('no000_06', 7)	# 79-85
    sprite('no000_07', 7)	# 86-92
    loopRest()
    enterState('CmnActStand')

@State
def EventHetariSit():
    sprite('no064_08', 6)	# 1-6
    sprite('no064_07', 4)	# 7-10
    sprite('no064_06', 4)	# 11-14
    sprite('no064_05', 2)	# 15-16
    sprite('no064_04', 32767)	# 17-32783
    loopRest()

@State
def EventNOGuard():
    sprite('no041_00', 3)	# 1-3
    sprite('no041_01', 32767)	# 4-32770

@State
def EventNOGuardToStand():
    sprite('no041_01', 5)	# 1-5
    sprite('no041_00', 5)	# 6-10
    sprite('no000_00', 7)	# 11-17
    sprite('no000_01', 7)	# 18-24
    sprite('no000_02', 7)	# 25-31
    sprite('no000_03', 7)	# 32-38
    sprite('no000_04', 7)	# 39-45
    sprite('no000_05', 7)	# 46-52
    sprite('no000_06', 7)	# 53-59
    sprite('no000_07', 7)	# 60-66
    loopRest()
    enterState('CmnActStand')

@State
def EventAIR4D():

    def upon_IMMEDIATE():
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('no291_01', 3)	# 1-3
    Unknown2005()
    Unknown1015(8000)
    physicsYImpulse(30000)
    SFX_0('001_airbackdash_0')
    sprite('no291_02', 3)	# 4-6
    sprite('no291_03', 3)	# 7-9
    setGravity(3200)
    sprite('no291_04', 3)	# 10-12
    sprite('no291_05', 3)	# 13-15
    label(0)
    sprite('no291_06', 3)	# 16-18
    sprite('no291_07', 3)	# 19-21
    sprite('no291_08', 3)	# 22-24
    sprite('no291_09', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no291_10', 5)	# 28-32
    Unknown2006()
    Unknown2005()
    Unknown23072()
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('no291_11', 4)	# 33-36
    sprite('no291_12', 4)	# 37-40
    sprite('no291_13', 4)	# 41-44
    sprite('no010_01', 4)	# 45-48
    Unknown2005()
    Unknown1000(-260000)
    sprite('no010_00', 4)	# 49-52
    loopRest()
    enterState('CmnActStand')

@State
def EventTBvsNOGameSet():
    Unknown1000(-100000)
    sprite('no620_08', 32767)	# 1-32767

@State
def EventBackJump():
    sprite('no620_08', 3)	# 1-3
    sprite('no620_08', 3)	# 4-6
    sprite('no620_08', 3)	# 7-9
    sprite('no074_00', 20)	# 10-29
    SFX_0('001_airbackdash_0')
    Unknown1000(-200000)
    physicsXImpulse(-30000)
    physicsYImpulse(50000)
    sprite('no074_00', 1)	# 30-30
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    loopRest()

@State
def EventNOvsCAEntry00():
    label(0)
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def EventNOvsCAEntry01():
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    sprite('no601_04', 6)	# 25-30
    sprite('no601_05', 6)	# 31-36
    sprite('no601_06', 6)	# 37-42
    sprite('no601_07', 6)	# 43-48
    SFX_0('019_cloth_b')
    sprite('no601_08', 6)	# 49-54
    GFX_0('noef601manto', 0)
    sprite('no601_09', 6)	# 55-60
    sprite('no601_10', 6)	# 61-66
    sprite('no601_11', 6)	# 67-72
    sprite('no601_12', 6)	# 73-78
    loopRest()
    enterState('CmnActStand')

@State
def EventNOvsCAWin00():
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)

@State
def EventNOvsCAWin01():
    sprite('no090_00', 3)	# 1-3
    sprite('no090_01', 3)	# 4-6
    sprite('no090_02', 6)	# 7-12
    sprite('no090_03', 5)	# 13-17
    sprite('no090_04', 4)	# 18-21
    sprite('no090_05', 3)	# 22-24
    sprite('no090_06', 3)	# 25-27
    sprite('no090_07', 3)	# 28-30
    label(0)
    sprite('no000_00', 7)	# 31-37
    sprite('no000_01', 7)	# 38-44
    sprite('no000_02', 7)	# 45-51
    sprite('no000_03', 7)	# 52-58
    sprite('no000_04', 7)	# 59-65
    sprite('no000_05', 7)	# 66-72
    sprite('no000_06', 7)	# 73-79
    sprite('no000_07', 7)	# 80-86
    loopRest()
    gotoLabel(0)

@State
def EventNOvsNYEntry00():
    label(0)
    sprite('no602_00', 6)	# 1-6
    loopRest()
    gotoLabel(0)

@State
def EventNOvsNYEntry01():
    sprite('no602_01', 8)	# 1-8
    sprite('no602_02', 8)	# 9-16
    sprite('no602_03', 8)	# 17-24
    sprite('no602_04', 8)	# 25-32
    enterState('CmnActStand')

@State
def EventJNvsNOEntry00():
    label(0)
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def EventJNvsNOEntry01():
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    sprite('no601_04', 6)	# 25-30
    sprite('no601_05', 6)	# 31-36
    sprite('no601_06', 6)	# 37-42
    sprite('no601_07', 6)	# 43-48
    SFX_0('019_cloth_b')
    sprite('no601_08', 6)	# 49-54
    GFX_0('noef601manto', 0)
    sprite('no601_09', 6)	# 55-60
    sprite('no601_10', 6)	# 61-66
    sprite('no601_11', 6)	# 67-72
    sprite('no601_12', 6)	# 73-78
    loopRest()
    enterState('CmnActStand')

@State
def EventTGvsNOEntry00():
    label(0)
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def EventTGvsNOEntry01():
    sprite('no601_00', 6)	# 1-6
    sprite('no601_01', 6)	# 7-12
    sprite('no601_02', 6)	# 13-18
    sprite('no601_03', 6)	# 19-24
    sprite('no601_04', 6)	# 25-30
    sprite('no601_05', 6)	# 31-36
    sprite('no601_06', 6)	# 37-42
    sprite('no601_07', 6)	# 43-48
    SFX_0('019_cloth_b')
    sprite('no601_08', 6)	# 49-54
    GFX_0('noef601manto', 0)
    sprite('no601_09', 6)	# 55-60
    sprite('no601_10', 6)	# 61-66
    sprite('no601_11', 6)	# 67-72
    sprite('no601_12', 6)	# 73-78
    loopRest()
    enterState('CmnActStand')

@State
def EventTGvsNOLose00():
    sprite('no060_13', 32767)	# 1-32767

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventWalkFrameIn():
    Unknown2034(0)
    Unknown2037(1)
    Unknown1000(-900000)

    def upon_CLEAR_OR_EXIT():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            sendToLabel(1)
    sprite('no030_00', 1)	# 1-1
    physicsXImpulse(4650)
    sprite('no030_01', 1)	# 2-2
    label(0)
    sprite('no030_02', 5)	# 3-7
    sprite('no030_03', 5)	# 8-12
    sprite('no030_04', 5)	# 13-17
    sprite('no030_05', 5)	# 18-22
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no030_06', 3)	# 23-25
    sprite('no030_07', 3)	# 26-28
    sprite('no030_08', 5)	# 29-33
    sprite('no030_09', 5)	# 34-38
    sprite('no030_10', 3)	# 39-41
    sprite('no030_11', 3)	# 42-44
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventNOvsHBWinLoop():
    label(0)
    sprite('no450_34', 6)	# 1-6
    sprite('no450_35', 6)	# 7-12
    loopRest()
    gotoLabel(0)

@State
def EventNOvsHBWinLoopEnd():
    sprite('no450_36', 6)	# 1-6
    sprite('no450_37', 6)	# 7-12
    sprite('no450_38', 6)	# 13-18
    enterState('CmnActStand')

@State
def EventNOvsPHWinLoop():
    label(0)
    sprite('no040_02', 6)	# 1-6	 **attackbox here**
    sprite('no040_03', 6)	# 7-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def EventNOvsPHWinLoopEnd():
    sprite('no040_02', 3)	# 1-3	 **attackbox here**
    sprite('no040_01', 6)	# 4-9
    sprite('no040_00', 6)	# 10-15
    loopRest()
    enterState('CmnActStand')

@State
def EventAREscape():
    sendToLabelUpon(32, 1)
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no111_00', 3)	# 57-59
    physicsXImpulse(-25000)
    sprite('no111_01', 3)	# 60-62
    sprite('no111_02', 3)	# 63-65
    sprite('no111_03', 3)	# 66-68
    sprite('no111_04', 3)	# 69-71
    sprite('no111_06', 3)	# 72-74
    Unknown1019(40)
    sprite('no111_07', 1)	# 75-75
    Unknown1019(40)
    sprite('no111_07', 1)	# 76-76
    Unknown1019(40)
    sprite('no111_07', 1)	# 77-77
    Unknown1019(40)
    sprite('no111_07', 1)	# 78-78
    Unknown1019(40)
    sprite('no111_07', 6)	# 79-84
    Unknown1019(0)
    sprite('no010_01', 4)	# 85-88
    sprite('no010_00', 4)	# 89-92
    Unknown2034(0)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(2)
        elif (SLOT_22 > (-260000)):
            sendToLabel(2)
    sprite('no030_00', 1)	# 93-93
    physicsXImpulse(6250)
    sprite('no030_01', 1)	# 94-94
    label(3)
    sprite('no030_02', 5)	# 95-99
    sprite('no030_03', 5)	# 100-104
    sprite('no030_04', 5)	# 105-109
    sprite('no030_05', 5)	# 110-114
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no030_06', 3)	# 115-117
    sprite('no030_07', 3)	# 118-120
    sprite('no030_08', 5)	# 121-125
    sprite('no030_09', 5)	# 126-130
    sprite('no030_10', 3)	# 131-133
    sprite('no030_11', 3)	# 134-136
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(3)
    label(2)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventAR2():
    sprite('no605_10', 7)	# 1-7
    sprite('no605_09', 7)	# 8-14
    sprite('no605_08', 32767)	# 15-32781

@State
def EventAR2End():
    sprite('no605_08', 7)	# 1-7
    sprite('no605_09', 7)	# 8-14
    sprite('no605_10', 7)	# 15-21
    enterState('CmnActStand')

@State
def EventNOWarp():
    loopRelated(17, 100)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    sprite('keep', 6)	# 1-6
    Unknown1043()
    label(0)
    sprite('keep', 6)	# 7-12
    GFX_1('haef_event_lose', 100)
    SFX_0('014_electric_s')
    sprite('keep', 6)	# 13-18
    gotoLabel(0)
    label(1)
    sprite('keep', 6)	# 19-24
    GFX_1('haef_event_lose', 100)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-7)
    sprite('keep', 30)	# 25-54
    SFX_0('014_electric_sl')
    GFX_1('haef_event_lose_end', 100)
    sprite('keep', 1)	# 55-55
    Unknown2035(1)
    sprite('null', 32767)	# 56-32822
    loopRest()

@State
def EventNOvsNYWin00():
    loopRelated(17, 280)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('no602_00', 6)	# 1-6
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no602_01', 8)	# 7-14
    sprite('no602_02', 8)	# 15-22
    sprite('no602_03', 8)	# 23-30
    sprite('no602_04', 8)	# 31-38
    loopRest()
    enterState('CmnActStand')

@State
def EventAct2NOvsJN():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown2034(0)
    sprite('no602_00', 32767)	# 1-32767
    Unknown20000(1)
    label(0)
    sprite('no602_00', 6)	# 32768-32773
    loopRest()
    gotoLabel(0)

@State
def EventJNEscape():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        setInvincible(1)
    sprite('no030_00', 1)	# 1-1
    physicsXImpulse(1600)
    sprite('no030_01', 1)	# 2-2
    sprite('no030_02', 5)	# 3-7
    sprite('no030_03', 5)	# 8-12
    sprite('no030_04', 5)	# 13-17
    sprite('no030_05', 5)	# 18-22
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no030_06', 3)	# 23-25
    sprite('no030_07', 3)	# 26-28
    sprite('no030_08', 5)	# 29-33
    sprite('no030_09', 5)	# 34-38
    sprite('no030_10', 3)	# 39-41
    sprite('no030_11', 3)	# 42-44
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no030_02', 5)	# 45-49
    sprite('no030_03', 5)	# 50-54
    sprite('no030_04', 5)	# 55-59
    sprite('no030_05', 5)	# 60-64
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no030_06', 3)	# 65-67
    sprite('no030_07', 3)	# 68-70
    sprite('no030_08', 5)	# 71-75
    sprite('no030_09', 5)	# 76-80
    sprite('no030_10', 3)	# 81-83
    sprite('no030_11', 3)	# 84-86
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    label(0)
    sprite('no000_00', 7)	# 87-93
    Unknown1084(1)
    sprite('no000_01', 7)	# 94-100
    sprite('no000_02', 7)	# 101-107
    sprite('no000_03', 7)	# 108-114
    sprite('no000_04', 7)	# 115-121
    sprite('no000_05', 7)	# 122-128
    sprite('no000_06', 7)	# 129-135
    sprite('no000_07', 7)	# 136-142
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no111_00', 3)	# 143-145
    physicsXImpulse(-25000)
    sprite('no111_01', 3)	# 146-148
    sprite('no111_02', 3)	# 149-151
    sprite('no111_03', 3)	# 152-154
    sprite('no111_04', 3)	# 155-157
    sprite('no111_06', 3)	# 158-160
    Unknown1019(40)
    sprite('no111_07', 1)	# 161-161
    Unknown1019(40)
    sprite('no111_07', 1)	# 162-162
    Unknown1019(40)
    sprite('no111_07', 1)	# 163-163
    Unknown1019(40)
    sprite('no111_07', 1)	# 164-164
    Unknown1019(40)
    sprite('no111_07', 6)	# 165-170
    Unknown1019(0)
    sprite('no010_00', 4)	# 171-174
    sprite('no010_01', 4)	# 175-178
    label(0)
    sprite('no010_02', 7)	# 179-185
    sprite('no010_03', 7)	# 186-192
    sprite('no010_04', 7)	# 193-199
    sprite('no010_05', 7)	# 200-206
    sprite('no010_06', 7)	# 207-213
    sprite('no010_07', 7)	# 214-220
    sprite('no010_08', 7)	# 221-227
    sprite('no010_09', 7)	# 228-234
    sprite('no010_10', 7)	# 235-241
    loopRest()
    gotoLabel(0)

@State
def EventJNEscapeEnd():
    sprite('no010_01', 4)	# 1-4
    sprite('no010_00', 4)	# 5-8
    Unknown2034(0)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(2)
        elif (SLOT_22 > (-260000)):
            sendToLabel(2)
    sprite('no032_00', 1)	# 9-9
    physicsXImpulse(24000)
    setInvincible(0)
    sprite('no032_01', 2)	# 10-11
    label(3)
    sprite('no032_02', 4)	# 12-15
    sprite('no032_03', 4)	# 16-19
    sprite('no032_04', 4)	# 20-23
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 24-27
    sprite('no032_06', 4)	# 28-31
    sprite('no032_07', 4)	# 32-35
    sprite('no032_08', 4)	# 36-39
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 40-43
    loopRest()
    gotoLabel(3)
    label(2)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventCrouchLoop():
    label(0)
    sprite('no010_02', 7)	# 1-7
    sprite('no010_03', 7)	# 8-14
    sprite('no010_04', 7)	# 15-21
    sprite('no010_05', 7)	# 22-28
    sprite('no010_06', 7)	# 29-35
    sprite('no010_07', 7)	# 36-42
    sprite('no010_08', 7)	# 43-49
    sprite('no010_09', 7)	# 50-56
    sprite('no010_10', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def EventCrouchToStand():
    sprite('no010_01', 4)	# 1-4
    sprite('no010_00', 4)	# 5-8
    loopRest()
    enterState('CmnActStand')

@State
def EventLittleRunOnCamera():
    sprite('no032_00', 1)	# 1-1
    physicsXImpulse(20000)
    setInvincible(0)
    sprite('no032_01', 2)	# 2-3
    sprite('no032_02', 4)	# 4-7
    sprite('no032_03', 4)	# 8-11
    sprite('no032_04', 4)	# 12-15
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 16-19
    sprite('no032_06', 4)	# 20-23
    loopRest()
    label(0)
    sprite('no000_00', 7)	# 24-30
    Unknown1084(1)
    sprite('no000_01', 7)	# 31-37
    sprite('no000_02', 7)	# 38-44
    sprite('no000_03', 7)	# 45-51
    sprite('no000_04', 7)	# 52-58
    sprite('no000_05', 7)	# 59-65
    sprite('no000_06', 7)	# 66-72
    sprite('no000_07', 7)	# 73-79
    loopRest()
    gotoLabel(0)

@State
def EventNOvsRM00():
    loopRelated(17, 380)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no050_00', 6)	# 57-62
    sprite('no050_01', 6)	# 63-68
    sprite('no050_02', 30)	# 69-98
    sprite('no050_01', 6)	# 99-104
    sprite('no050_00', 6)	# 105-110
    loopRest()
    enterState('CmnActStand')

@State
def EventNOvsRM02():
    loopRelated(17, 380)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    sprite('keep', 32767)	# 1-32767
    label(1)
    enterState('EventNOHetariToStand')

@State
def EventShake():
    sprite('keep', 32767)	# 1-32767
    GFX_0('EventShakeObj', -1)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_novsmi_00():
    sprite('no070_00', 4)	# 1-4
    GFX_0('Act2Event_Fade', -1)
    SFX_0('022_magiccircle_c')
    Unknown3004(-4)
    Unknown36(22)
    Unknown3004(-4)
    Unknown21007(11, 39)
    Unknown35()
    sprite('no070_01', 4)	# 5-8
    sprite('no070_02', 4)	# 9-12
    sprite('no070_03', 4)	# 13-16
    sprite('no070_04', 4)	# 17-20
    sprite('keep', 32767)	# 21-32787
    loopRest()

@State
def Act3Event_jnvsno_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        sendToLabelUpon(32, 0)

        def upon_STATE_END():
            Unknown1084(1)
            Unknown1000(-260000)
    label(9)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    gotoLabel(9)
    label(0)
    sprite('no040_00', 3)	# 57-59
    sprite('no040_04', 8)	# 60-67
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('no040_02', 5)	# 68-72	 **attackbox here**
    Unknown1047(-11000)
    sprite('no040_03', 5)	# 73-77	 **attackbox here**
    sprite('no040_02ex00', 5)	# 78-82
    sprite('no040_03ex00', 5)	# 83-87
    sprite('no040_01', 3)	# 88-90
    sprite('no040_00', 3)	# 91-93
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvsno_01():
    sprite('no605_10', 5)	# 1-5
    sprite('no605_09', 5)	# 6-10
    sprite('no605_04', 6)	# 11-16
    sprite('no605_05', 4)	# 17-20
    SFX_0('010_swing_sword_0')
    sprite('no605_06', 4)	# 21-24
    sprite('no605_07', 4)	# 25-28
    SFX_0('019_cloth_a')
    sprite('no605_08', 30)	# 29-58
    sprite('no605_09', 7)	# 59-65
    sprite('no605_10', 7)	# 66-72
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jnvsno_02():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('no000_00', 7)	# 1-7
    sprite('no070_00', 17)	# 8-24
    Unknown4052()
    Unknown4045('65665f6869746d7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_1')
    ScreenShake(1000, 20000)
    sprite('no070_00', 3)	# 25-27
    Unknown1047(-11000)
    sprite('no070_01', 3)	# 28-30
    sprite('no070_02', 3)	# 31-33
    sprite('no070_03', 3)	# 34-36
    sprite('no070_04', 3)	# 37-39
    sprite('no070_05', 3)	# 40-42
    sprite('no070_06', 32767)	# 43-32809
    loopRest()

@State
def Act3Event_novslc_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        sendToLabelUpon(32, 0)

        def upon_STATE_END():
            Unknown1084(1)
            Unknown1000(-260000)
    label(9)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('no041_00', 3)	# 57-59
    sprite('no041_02', 2)	# 60-61	 **attackbox here**
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('no041_03', 5)	# 62-66	 **attackbox here**
    Unknown1047(-11000)
    sprite('no041_02ex00', 5)	# 67-71	 **attackbox here**
    sprite('no041_03ex00', 5)	# 72-76	 **attackbox here**
    sprite('no041_01', 3)	# 77-79
    sprite('no041_00', 3)	# 80-82
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_novslc_01():
    sprite('no450_00', 6)	# 1-6
    sprite('no450_01', 6)	# 7-12
    label(0)
    sprite('no450_02', 6)	# 13-18
    sprite('no450_03', 6)	# 19-24
    sprite('no450_04', 6)	# 25-30
    loopRest()
    gotoLabel(0)

@State
def Act3Event_novslc_02():
    sprite('keep', 2)	# 1-2
    sprite('no450_01', 6)	# 3-8
    sprite('no450_00', 6)	# 9-14
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_novslc_03():

    def upon_IMMEDIATE():
        Unknown1000(-210000)
        Unknown2003(1)
    sprite('no286_04ex01', 1)	# 1-1
    sprite('no286_05ex01', 2)	# 2-3
    sprite('no286_06ex01', 2)	# 4-5	 **attackbox here**
    sprite('no286_09ex01', 18)	# 6-23	 **attackbox here**
    sprite('no286_10ex01', 7)	# 24-30	 **attackbox here**
    sprite('no286_11ex01', 7)	# 31-37
    sprite('no286_12ex01', 7)	# 38-44
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_novslc_04():
    sprite('no602_04', 6)	# 1-6
    sprite('no602_03', 6)	# 7-12
    sprite('no602_02', 6)	# 13-18
    sprite('no602_01', 6)	# 19-24
    sprite('no602_00', 32767)	# 25-32791
    loopRest()

@State
def Act3Event_novslc_05():
    sprite('keep', 2)	# 1-2
    GFX_0('Act3Event_Image', -1)
    Unknown38(11, 1)
    sprite('keep', 32767)	# 3-32769
    loopRest()

@State
def Act3Event_novslc_06():
    sprite('no602_01', 6)	# 1-6
    Unknown21007(11, 32)
    sprite('no602_02', 6)	# 7-12
    sprite('no602_03', 6)	# 13-18
    sprite('no602_04', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_novsny_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        sendToLabelUpon(32, 0)

        def upon_STATE_END():
            Unknown1084(1)
            Unknown1000(-260000)
    label(9)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('no040_00', 3)	# 57-59
    SLOT_51 = 15
    label(1)
    sprite('keep', 1)	# 60-60
    (SLOT_51 <= 0)
    if SLOT_ReturnVal:
        _gotolabel(4)
    if (not (SLOT_51 <= 1)):
        random_(2, 0, 20)
        if SLOT_ReturnVal:
            _gotolabel(3)
    label(2)
    sprite('no040_04', 3)	# 61-63
    SLOT_51 = (SLOT_51 + (-1))
    Unknown1047(-700)
    loopRest()
    if SLOT_51:
        _gotolabel(1)
    label(3)
    sprite('no041_04', 3)	# 64-66
    SLOT_51 = (SLOT_51 + (-1))
    Unknown1047(-700)
    loopRest()
    if SLOT_51:
        _gotolabel(1)
    label(4)
    sprite('no040_04', 3)	# 67-69
    sprite('no040_02', 5)	# 70-74	 **attackbox here**
    sprite('no040_03', 5)	# 75-79	 **attackbox here**
    sprite('no040_01', 5)	# 80-84
    sprite('no040_00', 5)	# 85-89
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_novsny_01():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('no290_01', 2)	# 1-2
    SFX_3('nose_07')
    sprite('no290_02', 2)	# 3-4
    sprite('no290_03', 2)	# 5-6
    sprite('no290_04', 1)	# 7-7
    sprite('no290_05', 18)	# 8-25	 **attackbox here**
    ScreenShake(0, 5000)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    SFX_0('016_explode_1')
    GFX_0('BLT', 1)
    sprite('no290_03', 5)	# 26-30
    SFX_3('nose_01')
    sprite('no290_02', 6)	# 31-36
    sprite('no290_01', 6)	# 37-42
    sprite('no402_06', 6)	# 43-48
    label(0)
    sprite('no000_00', 7)	# 49-55
    sprite('no000_01', 7)	# 56-62
    sprite('no000_02', 7)	# 63-69
    sprite('no000_03', 7)	# 70-76
    sprite('no000_04', 7)	# 77-83
    sprite('no000_05', 7)	# 84-90
    sprite('no000_06', 7)	# 91-97
    sprite('no000_07', 7)	# 98-104
    loopRest()
    gotoLabel(0)

@State
def Act3Event_novsny_02():
    sprite('no003_00', 5)	# 1-5
    Unknown2005()
    sprite('no003_01', 5)	# 6-10
    sprite('no003_02', 5)	# 11-15
    sprite('no000_00', 7)	# 16-22
    sprite('no000_01', 7)	# 23-29
    sprite('no000_02', 7)	# 30-36
    sprite('no000_03', 7)	# 37-43
    sprite('no000_04', 7)	# 44-50
    Unknown20000(1)
    Unknown20004(1)
    sprite('no000_05', 7)	# 51-57
    sprite('no000_06', 7)	# 58-64
    sprite('no000_07', 7)	# 65-71
    label(0)
    sprite('no000_00', 7)	# 72-78
    sprite('no000_01', 7)	# 79-85
    sprite('no000_02', 7)	# 86-92
    sprite('no000_03', 7)	# 93-99
    sprite('no000_04', 7)	# 100-106
    sprite('no000_05', 7)	# 107-113
    sprite('no000_06', 7)	# 114-120
    sprite('no000_07', 7)	# 121-127
    loopRest()
    gotoLabel(0)

@State
def Act3Event_novstm_00():
    sprite('keep', 2)	# 1-2
    Unknown21007(11, 32)
    sprite('keep', 32767)	# 3-32769
    loopRest()

@State
def Act3Event_novstm_01():
    sprite('no070_00', 4)	# 1-4
    sprite('no070_01', 4)	# 5-8
    sprite('no070_02', 4)	# 9-12
    sprite('no070_03', 4)	# 13-16
    sprite('no070_04', 4)	# 17-20
    sprite('no070_05', 4)	# 21-24
    sprite('no070_06', 32767)	# 25-32791
    loopRest()

@State
def Act3Event_tkvsno_00():

    def upon_IMMEDIATE():
        Unknown1000(-200000)
        sendToLabelUpon(32, 0)
        EnableCollision(0)
    label(9)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('no060_00', 2)	# 57-58
    physicsXImpulse(-3000)
    SFX_0('107_throw_catch')
    ScreenShake(1000, 20000)
    sprite('no060_07', 3)	# 59-61
    sprite('no060_08', 3)	# 62-64
    sprite('no060_09', 3)	# 65-67
    sprite('no060_10', 4)	# 68-71
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('no060_11', 4)	# 72-75
    sprite('no060_12', 32767)	# 76-32842

@State
def Act3Event_tkvsno_01():

    def upon_IMMEDIATE():

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(0)
            Unknown1084(1)
            Unknown1000(-260000)
    sprite('no061_00', 3)	# 1-3
    sprite('no061_01', 3)	# 4-6
    sprite('no061_02', 3)	# 7-9
    sprite('no061_03', 3)	# 10-12
    sprite('no061_04', 3)	# 13-15
    sprite('no061_05', 3)	# 16-18
    sprite('no061_06', 3)	# 19-21
    physicsXImpulse(1000)
    physicsYImpulse(8000)
    Unknown1043()
    sprite('no061_07', 3)	# 22-24
    sprite('no061_08', 32767)	# 25-32791
    label(0)
    sprite('no061_09', 4)	# 32792-32795
    sprite('no061_10', 4)	# 32796-32799
    sprite('no061_11', 4)	# 32800-32803
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tkvsno_02():
    sprite('no287_06', 4)	# 1-4
    sprite('no287_07', 4)	# 5-8
    sprite('no287_08', 4)	# 9-12
    sprite('no287_09', 4)	# 13-16	 **attackbox here**
    GFX_0('Act3Event_Nagenuke', -1)
    sprite('no287_10', 4)	# 17-20
    sprite('no287_11', 4)	# 21-24
    sprite('no287_12', 4)	# 25-28
    sprite('no287_13', 4)	# 29-32
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tkvsno_03():
    sprite('no620_00', 6)	# 1-6
    sprite('no620_01', 6)	# 7-12
    sprite('no620_02', 6)	# 13-18
    sprite('no620_03', 6)	# 19-24
    sprite('no620_04', 6)	# 25-30
    sprite('no620_05', 6)	# 31-36
    sprite('no620_06', 6)	# 37-42
    Unknown8000(100, 1, 1)
    Unknown21007(22, 32)
    sprite('no620_07', 6)	# 43-48
    sprite('no620_08', 32767)	# 49-32815

@State
def Act3Event_tkvsno_04():
    sprite('no064_02', 4)	# 1-4
    sprite('no064_03', 4)	# 5-8
    sprite('no064_04', 4)	# 9-12
    sprite('no064_05', 4)	# 13-16
    sprite('no064_06', 4)	# 17-20
    sprite('no064_07', 4)	# 21-24
    sprite('no064_08', 4)	# 25-28
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tkvsno_05():
    sprite('no064_02', 4)	# 1-4
    sprite('no064_03', 4)	# 5-8
    sprite('no064_04', 4)	# 9-12
    sprite('no064_05', 4)	# 13-16
    sprite('no064_06', 4)	# 17-20
    sprite('no064_07', 4)	# 21-24
    sprite('no064_08', 4)	# 25-28
    label(0)
    sprite('no000_00', 7)	# 29-35
    sprite('no000_01', 7)	# 36-42
    sprite('no000_02', 7)	# 43-49
    sprite('no000_03', 7)	# 50-56
    sprite('no000_04', 7)	# 57-63
    sprite('no000_05', 7)	# 64-70
    sprite('no000_06', 7)	# 71-77
    sprite('no000_07', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def Act3Event_tgvsno_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('no290_00', 2)	# 1-2
    sprite('no290_01', 2)	# 3-4
    SFX_3('nose_07')
    sprite('no290_02', 2)	# 5-6
    sprite('no290_03', 2)	# 7-8
    sprite('no290_04', 2)	# 9-10
    sprite('no290_05', 15)	# 11-25	 **attackbox here**
    ScreenShake(0, 5000)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    SFX_0('016_explode_1')
    GFX_0('BLT', 1)
    sprite('no290_03', 5)	# 26-30
    SFX_3('nose_01')
    sprite('no290_02', 6)	# 31-36
    sprite('no290_01', 6)	# 37-42
    sprite('no402_06', 6)	# 43-48
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsno_01():

    def upon_IMMEDIATE():
        GFX_0('Act3Event_Makoto', -1)
    sprite('no060_13', 32767)	# 1-32767

@State
def Act3Event_muvsno_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('keep', 2)	# 1-2

@State
def Act3Event_muvsno_01():
    sprite('no620_08', 32767)	# 1-32767

@State
def Act3Event_muvsno_02():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown1084(1)
            Unknown1000(-260000)
    sprite('no031_00', 7)	# 1-7
    physicsXImpulse(-1500)
    sprite('no031_01', 7)	# 8-14
    sprite('no031_02', 7)	# 15-21
    sprite('no031_03', 7)	# 22-28
    sprite('no031_04', 7)	# 29-35
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no031_05', 7)	# 36-42
    sprite('no031_06', 7)	# 43-49
    sprite('no031_07', 7)	# 50-56
    sprite('no031_08', 7)	# 57-63
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_muvsno_03():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('no290_00', 2)	# 1-2
    sprite('no290_01', 2)	# 3-4
    SFX_3('nose_07')
    sprite('no290_02', 3)	# 5-7
    sprite('no290_03', 3)	# 8-10
    sprite('no290_04', 3)	# 11-13
    sprite('no290_05', 3)	# 14-16	 **attackbox here**
    ScreenShake(0, 5000)
    GFX_0('EFF_SakuretsuNear', 0)
    GFX_0('EFF_Spark', 0)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()
    SFX_0('016_explode_1')
    GFX_0('BLT', 1)
    sprite('no290_03', 5)	# 17-21
    SFX_3('nose_01')
    sprite('no290_02', 6)	# 22-27
    sprite('no290_01', 6)	# 28-33
    sprite('no402_06', 6)	# 34-39
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvsno_00():

    def upon_IMMEDIATE():
        Unknown2005()
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)

@State
def Act3Event_hbvsno_01():
    sprite('no003_00', 5)	# 1-5
    Unknown2005()
    GFX_0('Act3Event_ExclamationControl', -1)
    sprite('no003_01', 5)	# 6-10
    sprite('no003_02', 5)	# 11-15
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvsno_02():
    sprite('no070_06', 10)	# 1-10
    sprite('no070_12', 6)	# 11-16
    sprite('no070_13', 6)	# 17-22
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvsno_03():
    sprite('no620_00', 6)	# 1-6
    sprite('no620_01', 6)	# 7-12
    sprite('no620_02', 6)	# 13-18
    sprite('no620_03', 6)	# 19-24
    sprite('no620_04', 6)	# 25-30
    sprite('no620_05', 6)	# 31-36
    sprite('no620_06', 6)	# 37-42
    Unknown8000(100, 1, 1)
    sprite('no620_07', 6)	# 43-48
    sprite('no620_08', 32767)	# 49-32815

@State
def Act3Event_hbvsno_04():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('no040_00', 7)	# 1-7
    sprite('no040_04', 17)	# 8-24
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('no040_02', 5)	# 25-29	 **attackbox here**
    Unknown1047(-11000)
    sprite('no040_03', 5)	# 30-34	 **attackbox here**
    sprite('no040_02ex00', 5)	# 35-39
    sprite('no040_03ex00', 5)	# 40-44
    sprite('no040_01', 3)	# 45-47
    sprite('no040_00', 3)	# 48-50
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvsno_05():
    sprite('keep', 2)	# 1-2
    sprite('no450_01', 6)	# 3-8
    sprite('no450_00', 6)	# 9-14
    sprite('no000_00', 3)	# 15-17
    sprite('no003_00', 4)	# 18-21
    Unknown2005()
    sprite('no003_01', 4)	# 22-25
    sprite('no003_02', 4)	# 26-29
    label(0)
    sprite('no000_00', 7)	# 30-36
    sprite('no000_01', 7)	# 37-43
    sprite('no000_02', 7)	# 44-50
    sprite('no000_03', 7)	# 51-57
    sprite('no000_04', 7)	# 58-64
    sprite('no000_05', 7)	# 65-71
    sprite('no000_06', 7)	# 72-78
    sprite('no000_07', 7)	# 79-85
    loopRest()
    gotoLabel(0)

@State
def Act3Event_StandGuard():
    label(0)
    sprite('no041_02', 8)	# 1-8	 **attackbox here**
    sprite('no041_03', 8)	# 9-16	 **attackbox here**
    sprite('no041_02ex00', 8)	# 17-24	 **attackbox here**
    sprite('no041_03ex00', 8)	# 25-32	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act3Event_StandGuardEnd():
    sprite('no041_01', 4)	# 1-4
    sprite('no041_00', 6)	# 5-10
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_CrouchGuard():
    sprite('no043_01', 4)	# 1-4
    label(0)
    sprite('no043_02', 4)	# 5-8	 **attackbox here**
    sprite('no043_02ex00', 4)	# 9-12	 **attackbox here**
    sprite('no043_03', 4)	# 13-16	 **attackbox here**
    sprite('no043_03ex00', 4)	# 17-20	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act3Event_StandToCrouch():
    sprite('no010_01', 8)	# 1-8
    sprite('no010_00', 8)	# 9-16
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_StandToCrouch():
    sprite('no010_01', 8)	# 1-8
    sprite('no010_00', 8)	# 9-16
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Reaction():
    sprite('no001_00', 6)	# 1-6
    sprite('no001_01', 6)	# 7-12
    sprite('no001_02', 6)	# 13-18
    sprite('no001_03', 6)	# 19-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no001_04', 6)	# 25-30
    sprite('no001_05', 6)	# 31-36
    sprite('no001_06', 6)	# 37-42
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Excite():
    sprite('no301_00', 6)	# 1-6
    sprite('no301_01', 6)	# 7-12
    sprite('no301_02', 6)	# 13-18
    sprite('no301_03', 6)	# 19-24
    sprite('no301_04', 6)	# 25-30
    sprite('no301_05', 6)	# 31-36
    sprite('no301_06', 8)	# 37-44
    sprite('no301_07', 6)	# 45-50
    sprite('no301_08', 6)	# 51-56
    sprite('no301_09', 6)	# 57-62
    sprite('no301_10', 6)	# 63-68
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rcvsno_01():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown2034(0)
        EnableCollision(0)
        loopRelated(17, 24)

        def upon_17():
            Unknown36(22)
            Unknown20000(1)
            Unknown35()
    sprite('no032_00', 1)	# 1-1
    sprite('no032_00', 1)	# 2-2
    physicsXImpulse(32000)
    sprite('no032_01', 2)	# 3-4
    sprite('no032_02', 4)	# 5-8
    sprite('no032_03', 4)	# 9-12
    sprite('no032_04', 4)	# 13-16
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 17-20
    sprite('no032_06', 4)	# 21-24
    sprite('no032_07', 4)	# 25-28
    sprite('no032_08', 4)	# 29-32
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 33-36
    sprite('no032_02', 4)	# 37-40
    sprite('no032_03', 4)	# 41-44
    sprite('no032_04', 4)	# 45-48
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 49-52
    sprite('no032_06', 4)	# 53-56
    sprite('no032_07', 4)	# 57-60
    sprite('no032_08', 4)	# 61-64
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 65-68
    sprite('no032_02', 4)	# 69-72
    sprite('no032_03', 4)	# 73-76
    sprite('no032_04', 4)	# 77-80
    sprite('no032_05', 4)	# 81-84
    sprite('no032_06', 4)	# 85-88
    sprite('no032_07', 4)	# 89-92
    sprite('no032_08', 4)	# 93-96
    sprite('no032_09', 4)	# 97-100
    sprite('no032_02', 4)	# 101-104
    sprite('no032_03', 4)	# 105-108
    sprite('no032_04', 4)	# 109-112
    sprite('no032_05', 4)	# 113-116
    sprite('no032_06', 4)	# 117-120
    sprite('no032_07', 4)	# 121-124
    sprite('no032_08', 4)	# 125-128
    Unknown8006(100, 1, 1)
    sprite('no032_09', 32767)	# 129-32895
    loopRest()

@State
def Act3Event_rcvsno_00():
    sprite('no064_02', 4)	# 1-4
    sprite('no064_03', 4)	# 5-8
    sprite('no064_04', 4)	# 9-12
    sprite('no064_05', 4)	# 13-16
    sprite('no064_06', 4)	# 17-20
    sprite('no064_07', 4)	# 21-24
    sprite('no064_08', 4)	# 25-28
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_havsno_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    gotoLabel(0)
    label(1)
    sprite('no070_00', 17)	# 57-73
    Unknown4052()
    Unknown4045('65665f6869746d7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(1000, 20000)
    sprite('no070_00', 3)	# 74-76
    Unknown1047(-11000)
    sprite('no070_01', 4)	# 77-80
    sprite('no070_02', 4)	# 81-84
    sprite('no070_03', 4)	# 85-88
    sprite('no070_04', 4)	# 89-92
    sprite('no070_05', 4)	# 93-96
    sprite('no070_06', 40)	# 97-136
    sprite('no070_07', 6)	# 137-142
    sprite('no070_08', 4)	# 143-146
    sprite('no070_09', 4)	# 147-150
    sprite('no070_10', 4)	# 151-154
    sprite('no070_11', 4)	# 155-158
    sprite('no063_10', 90)	# 159-248
    teleportRelativeX(150000)
    Unknown8003(100, 1, 1)
    sprite('no064_00', 4)	# 249-252
    sprite('no064_01', 4)	# 253-256
    sprite('no064_02', 4)	# 257-260
    sprite('no064_03', 4)	# 261-264
    sprite('no064_04', 4)	# 265-268
    sprite('no064_05', 4)	# 269-272
    sprite('no064_06', 4)	# 273-276
    sprite('no064_07', 4)	# 277-280
    sprite('no064_08', 4)	# 281-284
    loopRest()
    gotoLabel(0)

@State
def Act3Event_rlvsno_00_Loop():
    sprite('no292_00', 2)	# 1-2
    Unknown21007(22, 32)
    sprite('no292_01', 2)	# 3-4
    sprite('no292_02', 2)	# 5-6
    SFX_3('nose_01')
    sprite('no292_03', 3)	# 7-9
    GFX_0('noef229gtlptc_make', 0)
    sprite('no292_04', 4)	# 10-13
    sprite('no292_04', 32767)	# 14-32780
    SFX_0('016_explode_1')
    SFX_3('nose_00')
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 5000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rlvsno_00_LoopEnd():
    sprite('no292_03', 3)	# 1-3
    Unknown21007(22, 41)
    sprite('no292_02', 3)	# 4-6
    sprite('no292_01', 3)	# 7-9
    sprite('no292_00', 3)	# 10-12
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rlvsno_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        sendToLabelUpon(32, 1)
        Unknown2034(0)
        EnableCollision(0)
    label(0)
    sprite('no000_00', 7)	# 1-7
    sprite('no000_01', 7)	# 8-14
    sprite('no000_02', 7)	# 15-21
    sprite('no000_03', 7)	# 22-28
    sprite('no000_04', 7)	# 29-35
    sprite('no000_05', 7)	# 36-42
    sprite('no000_06', 7)	# 43-49
    sprite('no000_07', 7)	# 50-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no074_00', 20)	# 57-76
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000067000000')
    Unknown4045('65665f6869746d7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('103_hit_counter_slash_2')
    SFX_0('101_hit_slash_1')
    sprite('no074_00', 3)	# 77-79
    physicsXImpulse(-26000)
    physicsYImpulse(26000)
    setGravity(1600)
    sprite('no074_01', 3)	# 80-82
    clearUponHandler(2)
    sendToLabelUpon(2, 5)
    sprite('no074_02', 3)	# 83-85
    sprite('no074_03', 3)	# 86-88
    label(2)
    sprite('no074_00', 3)	# 89-91
    sprite('no074_01', 3)	# 92-94
    sprite('no074_02', 3)	# 95-97
    sprite('no074_03', 3)	# 98-100
    loopRest()
    gotoLabel(2)
    label(5)
    sprite('no010_00', 4)	# 101-104
    GFX_0('Act3Event_RCCreate', -1)
    Unknown1084(1)
    sprite('no010_01', 4)	# 105-108
    label(3)
    sprite('no010_02', 7)	# 109-115
    sprite('no010_03', 7)	# 116-122
    sprite('no010_04', 7)	# 123-129
    sprite('no010_05', 7)	# 130-136
    sprite('no010_06', 7)	# 137-143
    sprite('no010_07', 7)	# 144-150
    sprite('no010_08', 7)	# 151-157
    sprite('no010_09', 7)	# 158-164
    sprite('no010_10', 7)	# 165-171
    loopRest()
    gotoLabel(3)

@State
def Act3Event_rlvsno_02():

    def upon_IMMEDIATE():
        Unknown2034(0)
        EnableCollision(0)
    sprite('no010_02', 7)	# 1-7
    Unknown21007(22, 32)
    label(3)
    sprite('no010_03', 7)	# 8-14
    sprite('no010_04', 7)	# 15-21
    sprite('no010_05', 7)	# 22-28
    sprite('no010_06', 7)	# 29-35
    sprite('no010_07', 7)	# 36-42
    sprite('no010_08', 7)	# 43-49
    sprite('no010_09', 7)	# 50-56
    sprite('no010_10', 7)	# 57-63
    sprite('no010_02', 7)	# 64-70
    loopRest()
    gotoLabel(3)

@State
def Act3Event_rlvsno_03():

    def upon_IMMEDIATE():
        Unknown2034(0)
        EnableCollision(0)
    sprite('no010_01', 4)	# 1-4
    sprite('no010_00', 4)	# 5-8
    sprite('no000_00', 7)	# 9-15
    sprite('no032_00', 1)	# 16-16
    Unknown2005()
    Unknown2034(0)
    EnableCollision(0)
    sprite('no032_00', 1)	# 17-17
    physicsXImpulse(32000)
    sprite('no032_01', 2)	# 18-19
    sprite('no032_02', 4)	# 20-23
    sprite('no032_03', 4)	# 24-27
    sprite('no032_04', 4)	# 28-31
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 32-35
    sprite('no032_06', 4)	# 36-39
    sprite('no032_07', 4)	# 40-43
    sprite('no032_08', 4)	# 44-47
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 48-51
    sprite('no032_02', 4)	# 52-55
    sprite('no032_03', 4)	# 56-59
    sprite('no032_04', 4)	# 60-63
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 64-67
    sprite('no032_06', 4)	# 68-71
    sprite('no032_07', 4)	# 72-75
    sprite('no032_08', 4)	# 76-79
    Unknown8006(100, 1, 1)

@State
def Act3Event_izvsno_00():
    sprite('no620_08', 32767)	# 1-32767
    GFX_0('Act3Event_HACreate', -1)

@State
def Act3Event_phvsno_00():
    Unknown2034(0)
    Unknown2053(0)
    Unknown2037(1)
    teleportRelativeX(-2500000)
    Unknown20000(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_38:
            if (SLOT_22 < 1200000):
                Unknown21007(22, 32)
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        else:
            if (SLOT_22 > (-1200000)):
                Unknown21007(22, 32)
            if (SLOT_22 > (-260000)):
                Unknown2037(0)
                sendToLabel(1)
    sprite('no032_00', 1)	# 1-1
    physicsXImpulse(32000)
    sprite('no032_01', 2)	# 2-3
    label(0)
    sprite('no032_02', 4)	# 4-7
    sprite('no032_03', 4)	# 8-11
    sprite('no032_04', 4)	# 12-15
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)	# 16-19
    sprite('no032_06', 4)	# 20-23
    sprite('no032_07', 4)	# 24-27
    sprite('no032_08', 4)	# 28-31
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)	# 32-35
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('no000_00', 6)	# 36-41
    clearUponHandler(3)
    Unknown1084(1)
    Unknown2034(1)
    Unknown2053(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_phvsno_01():
    sprite('no001_00', 6)	# 1-6
    sprite('no001_01', 6)	# 7-12
    sprite('no001_02', 6)	# 13-18
    sprite('no001_03', 6)	# 19-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no001_04', 6)	# 25-30
    sprite('no001_05', 6)	# 31-36
    sprite('no001_06', 6)	# 37-42
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_phvsno_02():
    sprite('no301_00', 6)	# 1-6
    sprite('no301_01', 6)	# 7-12
    sprite('no301_02', 6)	# 13-18
    sprite('no301_03', 6)	# 19-24
    sprite('no301_04', 6)	# 25-30
    sprite('no301_05', 6)	# 31-36
    sprite('no301_06', 8)	# 37-44
    sprite('no301_07', 6)	# 45-50
    sprite('no301_08', 6)	# 51-56
    sprite('no301_09', 6)	# 57-62
    sprite('no301_10', 6)	# 63-68
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_phvsno_03():
    sendToLabelUpon(32, 1)
    sprite('no063_08', 6)	# 1-6
    sprite('no063_09', 6)	# 7-12
    Unknown8003(100, 1, 1)
    sprite('no063_10', 32767)	# 13-32779
    loopRest()
    label(1)
    sprite('no064_00', 50)	# 32780-32829
    clearUponHandler(32)

    def upon_CLEAR_OR_EXIT():
        SLOT_51 = (SLOT_51 + 1)
        if (SLOT_51 == 3):
            if op(4, 2, 52, 0, 2):
                teleportRelativeX(1000)
            else:
                teleportRelativeX(-1000)
            SLOT_51 = 0
            SLOT_52 = (SLOT_52 + 1)
    sprite('no064_01', 8)	# 32830-32837
    sprite('no064_02', 8)	# 32838-32845
    sprite('no064_02', 32767)	# 32846-65612
    clearUponHandler(3)
    loopRest()