@Subroutine
def PreInit():
    Unknown12019('75797500000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFInitialVelocity(15000)
    Unknown12038(23000)
    Unknown12034(33)
    Unknown12036(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(2)
    Unknown13039(2)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_AirGround_(0x3008)
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 420000, -100000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 400000, -100000, 450000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 480000, -100000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 320000, -100000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 300000, -200000, 50000, 1100, 30)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 300000, -200000, 50000, 1100, 30)
    Move_EndRegister()
    Move_Register('AtkB_Finish', 0x1)
    Move_Input_(INPUT_PRESS_B)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 800000, -200000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('AtkB_2nd', 0x1)
    Move_Input_(INPUT_PRESS_B)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 800000, -200000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(50000, 500000, 0, 400000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 700000, -200000, 50000, 800, 30)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 500000, -200000, 50000, 800, 30)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 550000, -80000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 500000, -50000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 550000, -250000, 20000, 2000, 50)
    Unknown15021(500)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5B_2nd', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5B_3rd', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 180000, -500000, 50000, 2000, 50)
    Unknown15021(500)
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
    Move_Register('SlashA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3001)
    Unknown14015(0, 1000000, -100000, 150000, 200, 200)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('SlashA_Comb', INPUT_SPECIALMOVE)
    Unknown14013('SlashA')
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x67)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3001)
    Unknown14015(0, 1000000, -100000, 150000, 200, 50)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('SlashB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3001)
    Unknown14015(250000, 800000, -100000, 350000, 100, 50)
    Unknown15021(2500)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('SlashB_Comb', INPUT_SPECIALMOVE)
    Unknown14013('SlashB')
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x67)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3001)
    Unknown14015(250000, 800000, -100000, 350000, 100, 50)
    Unknown15021(2500)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('SlashC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3001)
    Unknown14015(0, 1350000, -100000, 200000, 150, 10)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('SlashC_Comb', INPUT_SPECIALMOVE)
    Unknown14013('SlashC')
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(0x67)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3001)
    Unknown14015(0, 1350000, -100000, 200000, 150, 10)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('AirSlashA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3001)
    Unknown14015(300000, 900000, -250000, 50000, 150, 30)
    Unknown15021(2500)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('AirSlashA_Comb', INPUT_SPECIALMOVE)
    Unknown14013('AirSlashA')
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x67)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3001)
    Unknown14015(300000, 900000, -250000, 50000, 150, 30)
    Unknown15021(2500)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('AirSlashB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3001)
    Unknown14015(500000, 950000, -600000, 20000, 150, 30)
    Unknown15021(500)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('AirSlashB_Comb', INPUT_SPECIALMOVE)
    Unknown14013('AirSlashB')
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x67)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3001)
    Unknown14015(500000, 950000, -600000, 20000, 150, 30)
    Unknown15021(500)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('AirSlashC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3001)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('AirSlashC_Comb', INPUT_SPECIALMOVE)
    Unknown14013('AirSlashC')
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(0x67)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3001)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('ShukuchiA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('ShukuchiA_Comb', INPUT_SPECIALMOVE)
    Unknown14013('ShukuchiA')
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('ShukuchiB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('ShukuchiB_Comb', INPUT_SPECIALMOVE)
    Unknown14013('ShukuchiB')
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('ShukuchiC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('ShukuchiC_Comb', INPUT_SPECIALMOVE)
    Unknown14013('ShukuchiC')
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('AirShukuchiA', INPUT_SPECIALMOVE)
    Unknown14027('SlashA')
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('AirShukuchiA_Comb', INPUT_SPECIALMOVE)
    Unknown14013('AirShukuchiA')
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('AirShukuchiB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('AirShukuchiB_Comb', INPUT_SPECIALMOVE)
    Unknown14013('AirShukuchiB')
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('AirShukuchiC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('AirShukuchiC_Comb', INPUT_SPECIALMOVE)
    Unknown14013('AirShukuchiC')
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(300000, 1350000, -250000, 50000, 50, 30)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(3000)
    Unknown14015(-50000, 300000, -100000, 350000, 400, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14015(-50000, 300000, -100000, 350000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateSlash', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('UltimateSlashOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('UltimateRush', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('UltimateRushOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('UltimateAirRush', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('UltimateAirRushOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Unknown15016(0, 10, 40)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk5B', 'AtkB_2nd', 10000000)
    Unknown15024('AtkB_2nd', 'AtkB_Finish', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk2B', 'AtkB_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'SlashA', 10000000)
    Unknown15024('AtkB_2nd', 'SlashA', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'SlashB', 10000000)
    Unknown15024('AtkB_2nd', 'SlashB', 10000000)
    Unknown15024('SlashA', 'SlashA_Comb', 10000000)
    Unknown15024('SlashA', 'SlashB_Comb', 10000000)
    Unknown15024('SlashA', 'SlashC_Comb', 10000000)
    Unknown15024('SlashA', 'ShukuchiA_Comb', 10000000)
    Unknown15024('SlashA', 'ShukuchiB_Comb', 10000000)
    Unknown15024('SlashA', 'ShukuchiC_Comb', 10000000)
    Unknown15024('SlashA_Comb', 'SlashA_Comb', 10000000)
    Unknown15024('SlashA_Comb', 'SlashB_Comb', 10000000)
    Unknown15024('SlashA_Comb', 'SlashC_Comb', 10000000)
    Unknown15024('SlashA_Comb', 'ShukuchiA_Comb', 10000000)
    Unknown15024('SlashA_Comb', 'ShukuchiB_Comb', 10000000)
    Unknown15024('SlashA_Comb', 'ShukuchiC_Comb', 10000000)
    Unknown15024('AirSlashA', 'AirSlashA_Comb', 10000000)
    Unknown15024('AirSlashA', 'AirSlashB_Comb', 10000000)
    Unknown15024('AirSlashA', 'AirSlashC_Comb', 10000000)
    Unknown15024('AirSlashA', 'AirShukuchiA_Comb', 10000000)
    Unknown15024('AirSlashA', 'AirShukuchiB_Comb', 10000000)
    Unknown15024('AirSlashA', 'AirShukuchiC_Comb', 10000000)
    Unknown15024('AirSlashA_Comb', 'AirSlashA_Comb', 10000000)
    Unknown15024('AirSlashA_Comb', 'AirSlashB_Comb', 10000000)
    Unknown15024('AirSlashA_Comb', 'AirSlashC_Comb', 10000000)
    Unknown15024('AirSlashA_Comb', 'AirShukuchiA_Comb', 10000000)
    Unknown15024('AirSlashA_Comb', 'AirShukuchiB_Comb', 10000000)
    Unknown15024('AirSlashA_Comb', 'AirShukuchiC_Comb', 10000000)
    Unknown15024('SlashB', 'SlashA_Comb', 10000000)
    Unknown15024('SlashB', 'SlashB_Comb', 10000000)
    Unknown15024('SlashB', 'SlashC_Comb', 10000000)
    Unknown15024('SlashB', 'ShukuchiA_Comb', 10000000)
    Unknown15024('SlashB', 'ShukuchiB_Comb', 10000000)
    Unknown15024('SlashB', 'ShukuchiC_Comb', 10000000)
    Unknown15024('SlashB_Comb', 'SlashA_Comb', 10000000)
    Unknown15024('SlashB_Comb', 'SlashB_Comb', 10000000)
    Unknown15024('SlashB_Comb', 'SlashC_Comb', 10000000)
    Unknown15024('SlashB_Comb', 'ShukuchiA_Comb', 10000000)
    Unknown15024('SlashB_Comb', 'ShukuchiB_Comb', 10000000)
    Unknown15024('SlashB_Comb', 'ShukuchiC_Comb', 10000000)
    Unknown15024('AirSlashB', 'AirSlashA_Comb', 10000000)
    Unknown15024('AirSlashB', 'AirSlashB_Comb', 10000000)
    Unknown15024('AirSlashB', 'AirSlashC_Comb', 10000000)
    Unknown15024('AirSlashB', 'AirShukuchiA_Comb', 10000000)
    Unknown15024('AirSlashB', 'AirShukuchiB_Comb', 10000000)
    Unknown15024('AirSlashB', 'AirShukuchiC_Comb', 10000000)
    Unknown15024('AirSlashB_Comb', 'AirSlashA_Comb', 10000000)
    Unknown15024('AirSlashB_Comb', 'AirSlashB_Comb', 10000000)
    Unknown15024('AirSlashB_Comb', 'AirSlashC_Comb', 10000000)
    Unknown15024('AirSlashB_Comb', 'AirShukuchiA_Comb', 10000000)
    Unknown15024('AirSlashB_Comb', 'AirShukuchiB_Comb', 10000000)
    Unknown15024('AirSlashB_Comb', 'AirShukuchiC_Comb', 10000000)
    Unknown15024('SlashC', 'SlashA_Comb', 10000000)
    Unknown15024('SlashC', 'SlashB_Comb', 10000000)
    Unknown15024('SlashC', 'SlashC_Comb', 10000000)
    Unknown15024('SlashC', 'ShukuchiA_Comb', 10000000)
    Unknown15024('SlashC', 'ShukuchiB_Comb', 10000000)
    Unknown15024('SlashC', 'ShukuchiC_Comb', 10000000)
    Unknown15024('SlashC_Comb', 'SlashA_Comb', 10000000)
    Unknown15024('SlashC_Comb', 'SlashB_Comb', 10000000)
    Unknown15024('SlashC_Comb', 'SlashC_Comb', 10000000)
    Unknown15024('SlashC_Comb', 'ShukuchiA_Comb', 10000000)
    Unknown15024('SlashC_Comb', 'ShukuchiB_Comb', 10000000)
    Unknown15024('SlashC_Comb', 'ShukuchiC_Comb', 10000000)
    Unknown15024('AirSlashC', 'AirSlashA_Comb', 10000000)
    Unknown15024('AirSlashC', 'AirSlashB_Comb', 10000000)
    Unknown15024('AirSlashC', 'AirSlashC_Comb', 10000000)
    Unknown15024('AirSlashC', 'AirShukuchiA_Comb', 10000000)
    Unknown15024('AirSlashC', 'AirShukuchiB_Comb', 10000000)
    Unknown15024('AirSlashC', 'AirShukuchiC_Comb', 10000000)
    Unknown15024('AirSlashC_Comb', 'AirSlashA_Comb', 10000000)
    Unknown15024('AirSlashC_Comb', 'AirSlashB_Comb', 10000000)
    Unknown15024('AirSlashC_Comb', 'AirSlashC_Comb', 10000000)
    Unknown15024('AirSlashC_Comb', 'AirShukuchiA_Comb', 10000000)
    Unknown15024('AirSlashC_Comb', 'AirShukuchiB_Comb', 10000000)
    Unknown15024('AirSlashC_Comb', 'AirShukuchiC_Comb', 10000000)
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
    Unknown7010(0, 'uyu000')
    Unknown7010(1, 'uyu001')
    Unknown7010(2, 'uyu002')
    Unknown7010(3, 'uyu003')
    Unknown7010(4, 'uyu004')
    Unknown7010(5, 'uyu005')
    Unknown7010(6, 'uyu006')
    Unknown7010(7, 'uyu007')
    Unknown7010(8, 'uyu008')
    Unknown7010(9, 'uyu009')
    Unknown7010(10, 'uyu010')
    Unknown7010(15, 'uyu011')
    Unknown7010(16, 'uyu012')
    Unknown7010(17, 'uyu013')
    Unknown7010(18, 'uyu014')
    Unknown7010(19, 'uyu015')
    Unknown7010(20, 'uyu016')
    Unknown7010(21, 'uyu017')
    Unknown7010(22, 'uyu018')
    Unknown7010(23, 'uyu019')
    Unknown7010(24, 'uyu020')
    Unknown7010(25, 'uyu021')
    Unknown7010(28, 'uyu022')
    Unknown7010(29, 'uyu023')
    Unknown7010(30, 'uyu024')
    Unknown7010(31, 'uyu025')
    Unknown7010(32, 'uyu026')
    Unknown7010(33, 'uyu027')
    Unknown7010(34, 'uyu028')
    Unknown7010(35, 'uyu029')
    Unknown7010(36, 'uyu030')
    Unknown7010(37, 'uyu031')
    Unknown7010(39, 'uyu032')
    Unknown7010(42, 'uyu033')
    Unknown7010(43, 'uyu034')
    Unknown7010(44, 'uyu035')
    Unknown7010(45, 'uyu036')
    Unknown7010(46, 'uyu037')
    Unknown7010(47, 'uyu038')
    Unknown7010(48, 'uyu039')
    Unknown7010(49, 'uyu040')
    Unknown7010(50, 'uyu041')
    Unknown7010(52, 'uyu042')
    Unknown7010(53, 'uyu043')
    Unknown7010(54, 'uyu100_0')
    Unknown7010(55, 'uyu100_1')
    Unknown7010(56, 'uyu100_2')
    Unknown7010(63, 'uyu101_0')
    Unknown7010(64, 'uyu101_1')
    Unknown7010(65, 'uyu101_2')
    Unknown7010(57, 'uyu102_0')
    Unknown7010(58, 'uyu102_1')
    Unknown7010(59, 'uyu102_2')
    Unknown7010(66, 'uyu103_0')
    Unknown7010(67, 'uyu103_1')
    Unknown7010(68, 'uyu103_2')
    Unknown7010(60, 'uyu104_0')
    Unknown7010(61, 'uyu104_1')
    Unknown7010(62, 'uyu104_2')
    Unknown7010(69, 'uyu105_0')
    Unknown7010(70, 'uyu105_1')
    Unknown7010(71, 'uyu105_2')
    Unknown7010(72, 'uyu150')
    Unknown7010(74, 'uyu152')
    Unknown7010(85, 'uyu153')
    Unknown7010(87, 'uyu154')
    Unknown7010(88, 'uyu155')
    Unknown7010(96, 'uyu161_0')
    Unknown7010(97, 'uyu161_1')
    Unknown7010(92, 'uyu162_0')
    Unknown7010(93, 'uyu162_1')
    Unknown7010(98, 'uyu163_0')
    Unknown7010(99, 'uyu163_1')
    Unknown7010(100, 'uyu164_0')
    Unknown7010(101, 'uyu164_1')
    Unknown7010(105, 'uyu165_0')
    Unknown7010(106, 'uyu165_1')
    Unknown7010(102, 'uyu166_0')
    Unknown7010(103, 'uyu166_1')
    Unknown7010(90, 'uyu167_0')
    Unknown7010(91, 'uyu167_1')
    Unknown7010(107, 'uyu168_0')
    Unknown7010(108, 'uyu168_1')
    Unknown7010(110, 'uyu169_0')
    Unknown7010(111, 'uyu169_1')
    Unknown7010(94, 'uyu400_0')
    Unknown7010(95, 'uyu400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d617465527573680000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d617465527573684f44000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465536c61736800000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465536c6173684f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def MatchInit2():
    SLOT_5 = 3

@Subroutine
def OnFrameStep():
    if SLOT_4:
        WalkFSpeed(1200)
        WalkBSpeed(1200)
        Unknown13029(0)
    else:
        WalkFSpeed(8000)
        WalkBSpeed(6000)
        Unknown13029(1)
    if (not SLOT_60):
        SLOT_5 = 3
        SLOT_7 = 0
    if (not SLOT_158):
        SLOT_4 = 0
    if (not SLOT_21):
        SLOT_4 = 0
    if SLOT_4:
        SLOT_61 = 0
        SLOT_62 = 0

@Subroutine
def OnDamage():
    SLOT_60 = 0
    SLOT_4 = 0

@Subroutine
def OnGuard():
    SLOT_60 = 0
    SLOT_4 = 0

@Subroutine
def ChainRoot():
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')
    HitJumpCancel(1)

@Subroutine
def IaiSakeInit():
    SLOT_60 = 0

    def upon_3():
        if SLOT_4:
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            if SLOT_2:
                Unknown2037(0)
            else:
                Unknown2037(1)
                GFX_0('IaiStand_DmyObj', 100)
        else:
            setInvincible(0)
            Unknown26('IaiStand_DmyObj')

    def upon_43():
        if (SLOT_48 == 100):
            enterState('IaiSake_Auto')

    def upon_STATE_END():
        setInvincible(0)
        Unknown26('IaiStand_DmyObj')

@State
def CmnActStand():

    def upon_IMMEDIATE():
        callSubroutine('IaiSakeInit')
    if SLOT_4:
        _gotolabel(10)
    Unknown23145('NmlAtk5A')
    if SLOT_0:
        _gotolabel(1)
    Unknown23145('AN_NmlAtk5A_2nd')
    if SLOT_0:
        _gotolabel(1)
    label(0)
    sprite('Action_000_00', 8)	# 1-8	 **attackbox here**
    sprite('Action_000_01', 8)	# 9-16	 **attackbox here**
    sprite('Action_000_02', 8)	# 17-24	 **attackbox here**
    sprite('Action_000_03', 8)	# 25-32	 **attackbox here**
    sprite('Action_000_04', 8)	# 33-40	 **attackbox here**
    sprite('Action_000_05', 8)	# 41-48	 **attackbox here**
    sprite('Action_000_06', 8)	# 49-56	 **attackbox here**
    sprite('Action_000_07', 8)	# 57-64	 **attackbox here**
    sprite('Action_000_08', 8)	# 65-72	 **attackbox here**
    sprite('Action_000_09', 8)	# 73-80	 **attackbox here**
    sprite('Action_000_10', 8)	# 81-88	 **attackbox here**
    sprite('Action_000_11', 8)	# 89-96	 **attackbox here**
    sprite('Action_000_12', 8)	# 97-104	 **attackbox here**
    sprite('Action_000_13', 8)	# 105-112	 **attackbox here**
    sprite('Action_000_14', 8)	# 113-120	 **attackbox here**
    sprite('Action_000_15', 8)	# 121-128	 **attackbox here**
    sprite('Action_000_16', 8)	# 129-136	 **attackbox here**
    sprite('Action_000_17', 8)	# 137-144	 **attackbox here**
    sprite('Action_000_18', 8)	# 145-152	 **attackbox here**
    sprite('Action_000_19', 8)	# 153-160	 **attackbox here**
    sprite('Action_000_20', 8)	# 161-168	 **attackbox here**
    sprite('Action_000_21', 8)	# 169-176	 **attackbox here**
    sprite('Action_000_22', 8)	# 177-184	 **attackbox here**
    sprite('Action_000_23', 8)	# 185-192	 **attackbox here**
    sprite('Action_000_24', 8)	# 193-200	 **attackbox here**
    sprite('Action_000_25', 8)	# 201-208	 **attackbox here**
    sprite('Action_000_26', 8)	# 209-216	 **attackbox here**
    sprite('Action_000_27', 8)	# 217-224	 **attackbox here**
    sprite('Action_000_28', 8)	# 225-232	 **attackbox here**
    sprite('Action_000_29', 8)	# 233-240	 **attackbox here**
    sprite('Action_000_30', 8)	# 241-248	 **attackbox here**
    sprite('Action_000_31', 8)	# 249-256	 **attackbox here**
    sprite('Action_000_32', 6)	# 257-262	 **attackbox here**
    sprite('Action_000_33', 2)	# 263-264	 **attackbox here**
    sprite('Action_000_34', 8)	# 265-272	 **attackbox here**
    sprite('Action_000_35', 8)	# 273-280	 **attackbox here**
    sprite('Action_000_36', 8)	# 281-288	 **attackbox here**
    sprite('Action_000_37', 8)	# 289-296	 **attackbox here**
    sprite('Action_000_38', 8)	# 297-304	 **attackbox here**
    sprite('Action_000_39', 8)	# 305-312	 **attackbox here**
    sprite('Action_000_40', 8)	# 313-320	 **attackbox here**
    sprite('Action_000_41', 8)	# 321-328	 **attackbox here**
    sprite('Action_000_42', 8)	# 329-336	 **attackbox here**
    sprite('Action_000_43', 8)	# 337-344	 **attackbox here**
    sprite('Action_000_44', 8)	# 345-352	 **attackbox here**
    sprite('Action_000_45', 8)	# 353-360	 **attackbox here**
    sprite('Action_000_46', 8)	# 361-368	 **attackbox here**
    sprite('Action_000_47', 8)	# 369-376	 **attackbox here**
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
    sprite('Action_000_49', 5)	# 377-381
    sprite('Action_000_50', 6)	# 382-387
    sprite('Action_000_51', 6)	# 388-393
    SFX_1('uyu000')
    sprite('Action_000_52', 3)	# 394-396	 **attackbox here**
    sprite('Action_000_53', 7)	# 397-403	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 404-408	 **attackbox here**
    sprite('Action_000_55', 8)	# 409-416	 **attackbox here**
    sprite('Action_000_56', 7)	# 417-423	 **attackbox here**
    sprite('Action_000_53', 7)	# 424-430	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 431-435	 **attackbox here**
    sprite('Action_000_55', 8)	# 436-443	 **attackbox here**
    sprite('Action_000_56', 7)	# 444-450	 **attackbox here**
    sprite('Action_000_57', 6)	# 451-456
    sprite('Action_000_58', 6)	# 457-462
    sprite('Action_000_59', 5)	# 463-467
    gotoLabel(0)
    label(1)
    sprite('Action_002_11', 6)	# 468-473	 **attackbox here**
    sprite('Action_002_12', 7)	# 474-480
    sprite('Action_002_13', 3)	# 481-483
    sprite('Action_002_14', 4)	# 484-487
    gotoLabel(0)
    label(10)
    sprite('Action_420_00', 2)	# 488-489
    if SLOT_4:
        _gotolabel(10)
    label(11)
    sprite('Action_418_00', 3)	# 490-492
    sprite('Action_418_01', 3)	# 493-495
    sprite('Action_418_02', 2)	# 496-497
    gotoLabel(0)

@State
def CmnActStandTurn():

    def upon_IMMEDIATE():
        callSubroutine('IaiSakeInit')
    if SLOT_4:
        _gotolabel(10)
    sprite('Action_015_00', 3)	# 1-3
    sprite('Action_015_01', 3)	# 4-6
    loopRest()
    ExitState()
    label(10)
    sprite('Action_419_00', 3)	# 7-9
    sprite('Action_419_01', 3)	# 10-12
    loopRest()

@State
def IaiSake_Auto():

    def upon_IMMEDIATE():
        Unknown17013()
        setInvincible(1)
        Unknown13014(1)
        Unknown13015(1)
        Unknown13031(1)
        Unknown2019(1000)

        def upon_3():
            GFX_0('IaiStand_DmyObj', 100)

        def upon_43():
            if (SLOT_48 == 100):
                Unknown2037(1)

        def upon_STATE_END():
            Unknown2019(0)
    sprite('Action_156_00', 1)	# 1-1
    sprite('Action_156_01', 2)	# 2-3
    sprite('Action_156_02', 2)	# 4-5
    label(0)
    sprite('Action_156_03', 7)	# 6-12
    Unknown2037(0)
    sprite('Action_156_04', 7)	# 13-19
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('Action_156_05', 4)	# 20-23
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('Action_156_06', 4)	# 24-27

@State
def CmnActStand2Crouch():
    if SLOT_4:
        _gotolabel(1)
    sprite('Action_012_00', 3)	# 1-3
    sprite('Action_012_01', 3)	# 4-6
    sprite('Action_012_02', 2)	# 7-8
    ExitState()
    label(1)
    sprite('Action_420_00', 8)	# 9-16
    ExitState()

@State
def CmnActCrouch():
    if SLOT_4:
        _gotolabel(1)
    label(0)
    sprite('Action_013_00', 8)	# 1-8
    sprite('Action_013_01', 16)	# 9-24
    sprite('Action_013_02', 8)	# 25-32
    sprite('Action_013_03', 8)	# 33-40
    sprite('Action_013_04', 8)	# 41-48
    sprite('Action_013_05', 32)	# 49-80
    sprite('Action_013_06', 8)	# 81-88
    sprite('Action_013_07', 6)	# 89-94
    sprite('Action_013_08', 2)	# 95-96
    sprite('Action_013_09', 8)	# 97-104
    sprite('Action_013_10', 8)	# 105-112
    sprite('Action_013_11', 8)	# 113-120
    sprite('Action_013_12', 8)	# 121-128
    sprite('Action_013_13', 8)	# 129-136
    sprite('Action_013_14', 8)	# 137-144
    sprite('Action_013_15', 8)	# 145-152
    sprite('Action_013_16', 8)	# 153-160
    sprite('Action_013_17', 8)	# 161-168
    sprite('Action_013_18', 8)	# 169-176
    sprite('Action_013_19', 8)	# 177-184
    sprite('Action_013_20', 8)	# 185-192
    sprite('Action_013_21', 8)	# 193-200
    sprite('Action_013_22', 8)	# 201-208
    sprite('Action_013_23', 8)	# 209-216
    sprite('Action_013_24', 6)	# 217-222
    sprite('Action_013_25', 2)	# 223-224
    sprite('Action_013_26', 8)	# 225-232
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_420_00', 8)	# 233-240
    loopRest()
    gotoLabel(1)

@State
def CmnActCrouchTurn():

    def upon_IMMEDIATE():
        callSubroutine('IaiSakeInit')
    if SLOT_4:
        _gotolabel(1)
    sprite('Action_016_00', 3)	# 1-3
    sprite('Action_016_01', 3)	# 4-6
    ExitState()
    label(1)
    sprite('Action_419_00', 3)	# 7-9
    sprite('Action_419_01', 3)	# 10-12
    ExitState()

@State
def CmnActCrouch2Stand():
    if SLOT_4:
        _gotolabel(1)
    sprite('Action_014_00', 3)	# 1-3
    sprite('Action_014_01', 3)	# 4-6
    sprite('Action_014_02', 3)	# 7-9
    sprite('Action_014_03', 3)	# 10-12
    ExitState()
    label(1)
    sprite('Action_420_00', 12)	# 13-24
    ExitState()

@State
def CmnActJumpPre():
    if SLOT_4:
        _gotolabel(424)
    sprite('Action_036_00', 4)	# 1-4
    ExitState()
    label(424)
    sprite('Action_171_00', 4)	# 5-8

@State
def CmnActJumpUpper():
    if SLOT_4:
        _gotolabel(424)
    if SLOT_16:
        _gotolabel(1)
    label(0)
    sprite('Action_036_01', 3)	# 1-3
    sprite('Action_036_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_067_01', 4)	# 7-10
    sprite('Action_067_02', 4)	# 11-14
    gotoLabel(0)
    label(424)
    sprite('Action_171_01', 1)	# 15-15
    sprite('Action_171_02', 1)	# 16-16
    sprite('Action_171_03', 1)	# 17-17
    sprite('Action_171_04', 1)	# 18-18
    sprite('Action_171_05', 1)	# 19-19
    sprite('Action_171_06', 1)	# 20-20
    gotoLabel(424)

@State
def CmnActJumpUpperEnd():
    if SLOT_4:
        _gotolabel(424)
    sprite('Action_035_02', 2)	# 1-2
    sprite('Action_035_03', 2)	# 3-4
    sprite('Action_035_04', 2)	# 5-6
    sprite('Action_035_05', 2)	# 7-8
    sprite('Action_035_06', 2)	# 9-10
    ExitState()
    label(424)
    sprite('Action_171_07', 2)	# 11-12
    sprite('Action_171_08', 2)	# 13-14
    sprite('Action_171_09', 2)	# 15-16

@State
def CmnActJumpDown():
    if SLOT_4:
        _gotolabel(424)
    label(0)
    sprite('Action_022_00', 3)	# 1-3
    sprite('Action_022_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(424)
    sprite('Action_421_03', 5)	# 7-11
    sprite('Action_421_04', 5)	# 12-16
    loopRest()
    gotoLabel(424)

@State
def CmnActJumpLanding():
    if SLOT_4:
        _gotolabel(424)
    sprite('Action_023_00', 2)	# 1-2
    sprite('Action_023_01', 1)	# 3-3
    sprite('Action_023_02', 2)	# 4-5
    sprite('Action_023_03', 3)	# 6-8
    ExitState()
    label(424)
    sprite('Action_422_00', 4)	# 9-12

@State
def CmnActLandingStiffLoop():
    sprite('Action_403_13', 32767)	# 1-32767

@State
def CmnActLandingStiffEnd():
    sprite('Action_403_14', 2)	# 1-2
    sprite('Action_403_15', 2)	# 3-4
    sprite('Action_403_16', 2)	# 5-6

@State
def CmnActFWalk():

    def upon_IMMEDIATE():
        if (not SLOT_4):
            GFX_0('WalkOnpuMatome', 100)
    if SLOT_4:
        _gotolabel(442)
    label(0)
    sprite('Action_010_00', 5)	# 1-5
    sprite('Action_010_01', 5)	# 6-10
    sprite('Action_010_02', 5)	# 11-15
    sprite('Action_010_03', 6)	# 16-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_04', 5)	# 22-26
    sprite('Action_010_05', 5)	# 27-31
    sprite('Action_010_06', 5)	# 32-36
    sprite('Action_010_07', 5)	# 37-41
    sprite('Action_010_08', 5)	# 42-46
    sprite('Action_010_09', 6)	# 47-52
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_10', 5)	# 53-57
    sprite('Action_010_11', 5)	# 58-62
    loopRest()
    gotoLabel(0)
    label(442)
    sprite('Action_153_00', 7)	# 63-69
    sprite('Action_153_01', 7)	# 70-76
    sprite('Action_153_02', 7)	# 77-83
    sprite('Action_153_03', 7)	# 84-90
    sprite('Action_153_04', 7)	# 91-97
    sprite('Action_153_05', 10)	# 98-107
    loopRest()
    gotoLabel(442)

@State
def CmnActBWalk():

    def upon_IMMEDIATE():
        if (not SLOT_4):
            GFX_0('WalkOnpuMatome', 100)
    if SLOT_4:
        _gotolabel(442)
    label(0)
    sprite('Action_011_00', 5)	# 1-5
    sprite('Action_011_01', 5)	# 6-10
    sprite('Action_011_02', 5)	# 11-15
    sprite('Action_011_03', 6)	# 16-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_04', 5)	# 22-26
    sprite('Action_011_05', 5)	# 27-31
    sprite('Action_011_06', 5)	# 32-36
    sprite('Action_011_07', 5)	# 37-41
    sprite('Action_011_08', 5)	# 42-46
    sprite('Action_011_09', 6)	# 47-52
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_10', 5)	# 53-57
    sprite('Action_011_11', 5)	# 58-62
    loopRest()
    gotoLabel(0)
    label(442)
    sprite('Action_154_00', 7)	# 63-69
    sprite('Action_154_01', 7)	# 70-76
    sprite('Action_154_02', 7)	# 77-83
    sprite('Action_154_03', 7)	# 84-90
    sprite('Action_154_04', 7)	# 91-97
    sprite('Action_154_05', 10)	# 98-107
    loopRest()
    gotoLabel(442)

@State
def CmnActFDash():

    def upon_IMMEDIATE():
        if SLOT_4:
            enterState('IaiFDash')
    sprite('Action_045_00', 6)	# 1-6
    sprite('Action_045_01', 2)	# 7-8
    SFX_0('000_airdash_1')
    label(0)
    sprite('Action_045_02', 3)	# 9-11
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_03', 3)	# 12-14
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_06', 3)	# 21-23
    sprite('Action_045_07', 3)	# 24-26
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_08', 6)	# 1-6
    sprite('Action_045_09', 4)	# 7-10

@State
def IaiFDash():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_8():
            Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
            Unknown36(1)
            Unknown1007(150000)
            Unknown35()
    sprite('Action_159_04', 8)	# 1-8
    sprite('Action_166_05', 1)	# 9-9
    setInvincible(1)
    SFX_1('uyu302_0')
    sprite('Action_166_06', 1)	# 10-10
    Unknown4004('6566666563745f3530300000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_166_07', 1)	# 11-11
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('Action_166_08', 1)	# 12-12
    sprite('Action_166_09', 1)	# 13-13
    sprite('null', 1)	# 14-14
    Unknown2017(0)
    physicsXImpulse(450000)
    if (SLOT_25 <= 60000):
        teleportRelativeX(-10000)
    Unknown2006()
    sprite('null', 1)	# 15-15
    Unknown2017(1)
    Unknown1019(0)
    Unknown2006()
    Unknown4004('6566666563745f3530320000000000000000000000000000000000000000000064000000')
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(-200000)
    Unknown35()
    sprite('Action_166_11', 1)	# 16-16
    sprite('Action_166_13', 1)	# 17-17
    sprite('Action_166_14', 1)	# 18-18
    sprite('Action_166_15', 1)	# 19-19
    setInvincible(0)
    sprite('Action_166_16', 1)	# 20-20
    sprite('Action_166_17', 1)	# 21-21
    sprite('Action_166_18', 1)	# 22-22
    sprite('Action_166_19', 1)	# 23-23

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        if SLOT_4:
            enterState('IaiBDash')
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        Unknown1084(1)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('Action_046_00', 1)	# 1-1
    sprite('Action_046_01', 2)	# 2-3
    SFX_4('uyu006')
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('Action_046_02', 3)	# 4-6
    loopRest()
    label(0)
    sprite('Action_046_03', 3)	# 7-9
    sprite('Action_046_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_05', 2)	# 13-14
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    clearUponHandler(3)
    sprite('Action_046_06', 2)	# 15-16
    sprite('Action_046_07', 2)	# 17-18

@State
def CmnActBDashLanding():
    pass

@State
def IaiBDash():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_8():
            Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
            Unknown36(1)
            Unknown1007(150000)
            Unknown35()
    sprite('Action_159_04', 8)	# 1-8
    setInvincible(1)
    sprite('Action_166_05', 1)	# 9-9
    SFX_1('uyu207_1')
    sprite('Action_166_06', 1)	# 10-10
    Unknown4004('6566666563745f3530300000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_166_07', 1)	# 11-11
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('Action_166_08', 1)	# 12-12
    sprite('Action_166_09', 1)	# 13-13
    sprite('null', 4)	# 14-17
    teleportRelativeX(-250000)
    Unknown2006()
    sprite('null', 1)	# 18-18
    Unknown4004('6566666563745f3530320000000000000000000000000000000000000000000064000000')
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(-200000)
    Unknown35()
    label(0)
    sprite('Action_166_11', 1)	# 19-19
    sprite('Action_166_13', 1)	# 20-20
    sprite('Action_166_14', 1)	# 21-21
    sprite('Action_166_15', 1)	# 22-22
    setInvincible(0)
    sprite('Action_166_16', 1)	# 23-23
    sprite('Action_166_17', 5)	# 24-28
    sprite('Action_166_18', 6)	# 29-34
    sprite('Action_166_19', 4)	# 35-38
    ExitState()
    label(1)
    sprite('keep', 2)	# 39-40
    sprite('Action_166_22', 1)	# 41-41
    setInvincible(0)
    sprite('Action_166_23', 1)	# 42-42
    sprite('Action_166_17', 5)	# 43-47
    sprite('Action_166_18', 6)	# 48-53
    sprite('Action_166_19', 4)	# 54-57

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        if SLOT_4:
            enterState('IaiAirFDash')
    sprite('Action_068_01', 2)	# 1-2
    sprite('Action_068_02', 2)	# 3-4
    sprite('Action_068_03', 2)	# 5-6
    sprite('Action_068_04', 3)	# 7-9
    sprite('Action_068_05', 3)	# 10-12
    sprite('Action_068_06', 3)	# 13-15
    sprite('Action_068_07', 3)	# 16-18
    sprite('Action_068_08', 3)	# 19-21
    sprite('Action_068_09', 3)	# 22-24
    sprite('Action_068_10', 1)	# 25-25
    enterState('AirFDashRigor')

@State
def IaiAirFDash():

    def upon_IMMEDIATE():
        Unknown17015()
        SLOT_51 = SLOT_38
    sprite('Action_180_03', 3)	# 1-3
    Unknown1084(1)
    sprite('Action_180_04', 2)	# 4-5
    sprite('Action_180_04', 2)	# 6-7
    SFX_1('uyu302_0')
    setInvincible(1)
    sprite('Action_180_05', 1)	# 8-8
    Unknown1084(1)
    Unknown4004('6566666563745f3530310000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_180_06', 1)	# 9-9
    sprite('Action_180_07', 1)	# 10-10
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown1007(85000)
    Unknown35()
    sprite('Action_180_08', 1)	# 11-11
    sprite('Action_180_09', 1)	# 12-12
    sprite('null', 1)	# 13-13
    Unknown2017(0)
    physicsXImpulse(500000)
    setGravity(0)
    sprite('null', 1)	# 14-14
    Unknown2017(1)
    Unknown1084(1)
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(-200000)
    Unknown1007(85000)
    Unknown35()
    label(0)
    sprite('Action_167_13ex01', 1)	# 15-15
    Unknown2006()
    setInvincible(0)
    sprite('Action_180_13', 1)	# 16-16
    sprite('Action_180_14', 1)	# 17-17
    sprite('Action_180_15', 1)	# 18-18
    sprite('Action_180_16', 1)	# 19-19
    sprite('Action_180_17', 2)	# 20-21
    physicsXImpulse(-10000)
    setGravity(1500)
    SLOT_52 = SLOT_38
    if (SLOT_51 == SLOT_52):
        SLOT_12 = (SLOT_12 * (-1))
    ExitState()

@State
def AirFDashRigor():

    def upon_IMMEDIATE():
        Unknown13014(1)
        Unknown13015(1)
        Unknown13031(1)
        Unknown13019(1)
        Unknown28(2, 'CmnActJumpLanding')
    label(0)
    sprite('Action_068_11', 3)	# 1-3
    sprite('Action_068_12', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        if SLOT_4:
            enterState('IaiAirBDash')
    sprite('Action_046_03', 4)	# 1-4
    physicsYImpulse(12000)
    sprite('Action_046_04', 4)	# 5-8
    label(0)
    sprite('Action_046_03', 4)	# 9-12
    sprite('Action_046_04', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def IaiAirBDash():

    def upon_IMMEDIATE():
        Unknown17015()
        SLOT_51 = SLOT_38
    sprite('Action_180_03', 3)	# 1-3
    Unknown1084(1)
    Unknown22001(-1)
    Unknown22003(-1)
    sprite('Action_180_04', 2)	# 4-5
    sprite('Action_180_04', 2)	# 6-7
    SFX_1('uyu207_1')
    setInvincible(1)
    sprite('Action_180_05', 1)	# 8-8
    Unknown4004('6566666563745f3530310000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_180_06', 1)	# 9-9
    sprite('Action_180_07', 1)	# 10-10
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown1007(85000)
    Unknown35()
    sprite('Action_180_08', 1)	# 11-11
    sprite('Action_180_09', 1)	# 12-12
    sprite('null', 1)	# 13-13
    Unknown2017(0)
    physicsXImpulse(-300000)
    setGravity(0)
    sprite('null', 1)	# 14-14
    Unknown2017(1)
    Unknown1084(1)
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    Unknown2005()
    teleportRelativeX(-200000)
    Unknown1007(85000)
    Unknown35()
    label(0)
    sprite('Action_162_20', 1)	# 15-15
    Unknown2006()
    setInvincible(0)
    sprite('Action_162_21', 1)	# 16-16
    sprite('Action_162_22', 1)	# 17-17
    sprite('Action_162_23', 1)	# 18-18
    sprite('Action_162_24', 1)	# 19-19
    sprite('Action_180_17', 2)	# 20-21
    physicsXImpulse(10000)
    setGravity(1500)
    SLOT_52 = SLOT_38
    if (SLOT_51 == SLOT_52):
        SLOT_12 = (SLOT_12 * (-1))

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
    sprite('Action_041_00', 3)	# 1-3
    sprite('Action_041_01', 3)	# 4-6
    sprite('Action_041_02', 3)	# 7-9
    sprite('Action_041_03', 3)	# 10-12
    sprite('Action_041_04', 3)	# 13-15
    label(0)
    sprite('Action_041_05', 3)	# 16-18
    sprite('Action_041_06', 3)	# 19-21
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_07', 5)	# 1-5
    sprite('Action_041_08', 5)	# 6-10
    sprite('Action_041_09', 5)	# 11-15

@State
def CmnActMidGuardPre():
    sprite('Action_017_08', 3)	# 1-3
    sprite('Action_017_09', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('Action_017_10', 5)	# 1-5
    sprite('Action_017_11', 5)	# 6-10
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('Action_017_10', 5)	# 1-5
    sprite('Action_017_11', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('Action_017_06', 5)	# 1-5
    sprite('Action_017_07', 5)	# 6-10

@State
def CmnActHighGuardPre():
    sprite('Action_017_08', 3)	# 1-3
    sprite('Action_017_09', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('Action_017_10', 5)	# 1-5
    sprite('Action_017_11', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('Action_017_10', 5)	# 1-5
    sprite('Action_017_11', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('Action_018_08', 3)	# 1-3
    sprite('Action_018_09', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('Action_018_10', 5)	# 1-5
    sprite('Action_018_11', 5)	# 6-10
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('Action_018_10', 5)	# 1-5
    sprite('Action_018_11', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('Action_019_08', 3)	# 1-3
    sprite('Action_019_09', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('Action_019_10', 5)	# 1-5
    sprite('Action_019_11', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('Action_019_10', 5)	# 1-5
    sprite('Action_019_11', 5)	# 6-10
    loopRest()
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
    sprite('Action_136_01', 2)	# 1-2
    sprite('Action_136_02', 3)	# 3-5
    sprite('Action_136_03', 2)	# 6-7
    sprite('Action_136_04', 1)	# 8-8	 **attackbox here**
    sprite('Action_136_05', 2)	# 9-10	 **attackbox here**
    sprite('Action_136_06', 3)	# 11-13	 **attackbox here**
    sprite('Action_136_07', 4)	# 14-17	 **attackbox here**
    sprite('Action_136_08', 3)	# 18-20
    sprite('Action_136_09', 3)	# 21-23
    sprite('Action_136_10', 2)	# 24-25
    sprite('Action_136_11', 2)	# 26-27

@State
def CmnActAirLockWait():
    sprite('Action_019_02', 1)	# 1-1
    sprite('Action_019_01', 3)	# 2-4
    sprite('Action_019_00', 3)	# 5-7

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
    SLOT_4 = 0
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
    SLOT_4 = 0
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
    SLOT_4 = 0
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
    SLOT_4 = 0
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
def IaiJumpDown_ToLand():

    def upon_IMMEDIATE():
        Unknown17015()
        clearUponHandler(2)

        def upon_5():
            sendToLabel(1)
    sprite('Action_421_00', 5)	# 1-5
    sprite('Action_421_01', 4)	# 6-9
    sprite('Action_421_02', 4)	# 10-13
    label(0)
    sprite('Action_421_03', 5)	# 14-18
    sprite('Action_421_04', 5)	# 19-23
    gotoLabel(0)
    label(1)
    sprite('Action_422_00', 4)	# 24-27
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    loopRest()

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(13000)
        Unknown1112('')
        Unknown9016(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_002_00', 3)	# 1-3
    Unknown1051(120)
    sprite('Action_002_00', 2)	# 4-5
    SLOT_4 = 0
    sprite('Action_002_01', 4)	# 6-9
    Unknown7009(1)
    sprite('Action_002_02ex01', 3)	# 10-12	 **attackbox here**
    GFX_0('5B_Blade', 100)
    SFX_3('SE042')
    SFX_3('SE_DrawnSword')
    sprite('Action_002_03', 2)	# 13-14
    Recovery()
    Unknown2063()
    sprite('Action_002_04', 2)	# 15-16
    sprite('Action_002_05', 3)	# 17-19
    sprite('Action_002_06', 3)	# 20-22
    sprite('Action_002_07', 2)	# 23-24	 **attackbox here**
    sprite('Action_002_08', 3)	# 25-27	 **attackbox here**
    sprite('Action_002_09', 3)	# 28-30	 **attackbox here**
    sprite('Action_002_10', 4)	# 31-34	 **attackbox here**
    SFX_3('SE_SheatheSword')

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirUntechableTime(22)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_003_00', 3)	# 1-3
    sprite('Action_003_01', 1)	# 4-4
    SLOT_4 = 0
    sprite('Action_003_01', 3)	# 5-7
    teleportRelativeX(-7000)
    sprite('Action_003_02', 2)	# 8-9
    sprite('Action_003_03', 2)	# 10-11
    Unknown7007('7579753130365f300000000000000000640000007579753130365f310000000000000000640000007579753130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_003_04', 4)	# 12-15	 **attackbox here**
    teleportRelativeX(50000)
    SFX_3('SE043')
    SFX_3('SE_DrawnSword')
    GFX_0('5C_Blade', 100)
    sprite('Action_003_05', 5)	# 16-20
    Recovery()
    Unknown2063()
    sprite('Action_003_06', 6)	# 21-26
    sprite('Action_003_07', 5)	# 27-31
    sprite('Action_003_08', 3)	# 32-34	 **attackbox here**
    teleportRelativeX(-50000)
    sprite('Action_003_09', 5)	# 35-39	 **attackbox here**
    SFX_3('SE_SheatheSword')

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(350)
        AirUntechableTime(20)
        Hitstop(3)
        Unknown11092(1)
        PushbackX(9800)
        AirPushbackX(8500)
        AirPushbackY(8000)
        callSubroutine('ChainRoot')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown2038(1)
    sprite('Action_136_00', 2)	# 1-2
    sprite('Action_136_01', 1)	# 3-3
    teleportRelativeX(50000)
    sprite('Action_136_01', 2)	# 4-5
    SLOT_4 = 0
    sprite('Action_136_02', 2)	# 6-7
    teleportRelativeX(50000)
    physicsXImpulse(17500)
    Unknown1028(-900)
    sprite('Action_136_03', 2)	# 8-9
    teleportRelativeX(50000)
    SFX_1('uyu110_0')
    sprite('Action_136_04', 3)	# 10-12	 **attackbox here**
    teleportRelativeX(20000)
    Unknown14070('AN_NmlAtk5A_4th')
    sprite('Action_136_05', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    GFX_0('4C_Zanzo', 100)
    SFX_3('SE_ClothesSwing2')
    sprite('Action_136_06', 4)	# 16-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_136_07', 5)	# 20-24	 **attackbox here**
    Unknown1084(1)
    RefreshMultihit()
    Hitstop(11)
    sprite('Action_136_08', 2)	# 25-26
    Recovery()
    Unknown2063()
    sprite('Action_136_09', 5)	# 27-31
    if SLOT_2:
        Unknown14072('AN_NmlAtk5A_4th')
    sprite('Action_136_10', 5)	# 32-36
    Unknown14074('AN_NmlAtk5A_4th')
    sprite('Action_136_11', 5)	# 37-41

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(20000)
        AirPushbackX(-5000)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirUntechableTime(40)
        JumpCancel_(0)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(10)
    sprite('Action_134_00', 1)	# 1-1
    sprite('Action_134_01', 2)	# 2-3
    SLOT_4 = 0
    teleportRelativeX(-20000)
    sprite('Action_134_02', 2)	# 4-5
    teleportRelativeX(-10000)
    SFX_4('uyu110_1')
    sprite('Action_134_03', 2)	# 6-7
    teleportRelativeX(-40000)
    GFX_0('4B_Zanzo', 100)
    SFX_3('SE_ClothesSwing1')
    sprite('Action_134_04', 2)	# 8-9
    teleportRelativeX(-30000)
    sprite('Action_134_05', 3)	# 10-12	 **attackbox here**
    sprite('Action_134_06', 3)	# 13-15
    Recovery()
    sprite('Action_134_07', 6)	# 16-21
    sprite('Action_134_08', 6)	# 22-27
    teleportRelativeX(-40000)
    sprite('Action_134_09', 6)	# 28-33
    sprite('Action_134_10', 6)	# 34-39
    ExitState()
    label(10)
    sprite('Action_134_06', 3)	# 40-42
    sprite('Action_134_07', 6)	# 43-48
    sprite('Action_135_02', 2)	# 49-50
    teleportRelativeX(30500)
    sprite('Action_135_03', 3)	# 51-53
    sprite('Action_135_04', 3)	# 54-56
    teleportRelativeX(-42000)
    sprite('Action_135_05', 4)	# 57-60
    SFX_3('SE_ClothesSwing2')
    GFX_0('4BAdd_Zanzo', 100)
    sprite('Action_135_06', 4)	# 61-64	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    AirPushbackX(12000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    SFX_4('uyu108_2')
    sprite('Action_135_07', 6)	# 65-70
    Recovery()
    sprite('Action_135_08', 5)	# 71-75
    sprite('Action_135_09', 6)	# 76-81
    sprite('Action_135_10', 5)	# 82-86

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_005_00', 2)	# 1-2
    sprite('Action_005_01', 3)	# 3-5
    sprite('Action_005_02', 2)	# 6-7
    Unknown7009(4)
    SFX_3('SE042')
    sprite('Action_005_03', 3)	# 8-10	 **attackbox here**
    SLOT_4 = 0
    sprite('Action_005_04', 4)	# 11-14	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_005_05', 4)	# 15-18
    sprite('Action_005_06', 4)	# 19-22
    sprite('Action_005_07', 4)	# 23-26

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1600)
        AttackP1(90)
        PushbackX(12000)
        AirPushbackY(22000)
        Unknown9016(1)
        Hitstop(8)
        Unknown11001(0, 4, 6)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AtkB_2nd')
        HitOrBlockCancel('AtkB_Finish')

        def upon_3():
            if (SLOT_18 > 3):
                SLOT_4 = 0
            if (SLOT_18 == 6):
                setInvincible(1)
                Unknown22019('0100000000000000000000000000000000000000')
        if Unknown23145('NmlAtk2B'):
            SLOT_51 = 1
        if Unknown23145('AtkB_2nd'):
            SLOT_51 = 1
        if SLOT_4:
            Unknown23159('Iai5B')
            SLOT_51 = 1
    if SLOT_51:
        _gotolabel(100)
    sprite('Action_425_00', 2)	# 1-2
    sprite('Action_425_01', 2)	# 3-4
    sprite('Action_425_02', 2)	# 5-6
    sprite('Action_425_03', 2)	# 7-8
    sprite('Action_425_04', 2)	# 9-10
    label(100)
    sprite('Action_425_05', 2)	# 11-12
    Unknown20(6, 2, 51)
    Unknown1084(1)
    sprite('Action_425_06', 2)	# 13-14	 **attackbox here**
    Unknown7006('uyu109_0', 100, 829782389, 828324144, 0, 0, 100, 829782389, 845101360, 0, 0, 100, 863336821, 811545392, 0, 0, 100)
    SFX_3('SE_DrawnSword')
    GFX_0('6A_Blade', 100)
    sprite('Action_425_07', 7)	# 15-21	 **attackbox here**
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('Action_425_08', 5)	# 22-26	 **attackbox here**
    sprite('Action_425_09', 3)	# 27-29	 **attackbox here**
    sprite('Action_425_10', 6)	# 30-35	 **attackbox here**
    SFX_3('SE_SheatheSword')
    sprite('Action_418_00', 4)	# 36-39
    sprite('Action_418_01', 4)	# 40-43
    sprite('Action_418_02', 2)	# 44-45

@State
def AtkB_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1600)
        PushbackX(12000)
        AirPushbackY(15000)
        Unknown9016(1)
        Hitstop(8)
        Unknown11001(0, 4, 6)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AtkB_Finish')
    sprite('Action_426_05', 6)	# 1-6
    Unknown1084(1)
    sprite('Action_426_06ex01', 2)	# 7-8	 **attackbox here**
    Unknown7006('uyu109_0', 100, 829782389, 828324144, 0, 0, 100, 829782389, 845101360, 0, 0, 100, 863336821, 811545392, 0, 0, 100)
    SFX_3('SE_DrawnSword')
    GFX_0('6B_Blade', 100)
    sprite('Action_426_07', 7)	# 9-15	 **attackbox here**
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('Action_426_08', 5)	# 16-20	 **attackbox here**
    sprite('Action_426_09', 3)	# 21-23	 **attackbox here**
    sprite('Action_426_10', 6)	# 24-29	 **attackbox here**
    SFX_3('SE_SheatheSword')
    sprite('Action_418_00', 4)	# 30-33
    sprite('Action_418_01', 4)	# 34-37
    sprite('Action_418_02', 2)	# 38-39

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1600)
        AttackP1(90)
        PushbackX(12000)
        AirPushbackY(12000)
        Unknown9016(1)
        HitLow(2)
        Hitstop(8)
        Unknown11001(0, 4, 6)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AtkB_2nd')
        HitOrBlockCancel('AtkB_Finish')
        Unknown11058('0000000000000000010000000000000000000000')

        def upon_3():
            if (SLOT_18 > 3):
                SLOT_4 = 0
        if Unknown23145('NmlAtk5B'):
            SLOT_51 = 1
        if Unknown23145('AtkB_2nd'):
            SLOT_51 = 1
        if SLOT_4:
            Unknown23159('Iai2B')
            SLOT_51 = 1
    if SLOT_51:
        _gotolabel(100)
    sprite('Action_427_00', 2)	# 1-2
    sprite('Action_427_01', 2)	# 3-4
    sprite('Action_427_02', 2)	# 5-6
    sprite('Action_427_03', 2)	# 7-8
    sprite('Action_427_04', 2)	# 9-10
    label(100)
    sprite('Action_427_05', 2)	# 11-12
    Unknown20(6, 2, 51)
    Unknown1084(1)
    sprite('Action_427_06', 2)	# 13-14	 **attackbox here**
    Unknown7006('uyu109_0', 100, 829782389, 828324144, 0, 0, 100, 829782389, 845101360, 0, 0, 100, 863336821, 811545648, 0, 0, 100)
    SFX_3('SE_DrawnSword')
    GFX_0('6C_Blade', 100)
    sprite('Action_427_07', 7)	# 15-21	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_427_08', 5)	# 22-26	 **attackbox here**
    sprite('Action_427_09', 3)	# 27-29	 **attackbox here**
    sprite('Action_427_10', 6)	# 30-35	 **attackbox here**
    SFX_3('SE_SheatheSword')
    sprite('Action_418_00', 4)	# 36-39
    sprite('Action_418_01', 4)	# 40-43
    sprite('Action_418_02', 2)	# 44-45

@State
def AtkB_Finish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(1600)
        Unknown11092(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackY(12000)
        AirPushbackX(60000)
        AirUntechableTime(60)
        WallbounceReboundTime(0)
        PushbackX(30400)
        Hitstop(2)
        Unknown11001(0, 3, 8)
        Unknown9016(1)
        JumpCancel_(0)
    sprite('Action_420_00', 3)	# 1-3
    sprite('Action_236_00', 3)	# 4-6
    SFX_3('SE_DrawnSword')
    GFX_0('FF_Start', 100)
    SFX_4('uyu105_1')
    sprite('Action_236_01', 2)	# 7-8
    sprite('Action_236_02', 2)	# 9-10
    GFX_0('FF_Blade_1st', 100)
    GFX_0('FF_Blade_2nd', 100)
    sprite('Action_236_03', 3)	# 11-13	 **attackbox here**
    sprite('Action_236_03', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_236_05', 3)	# 17-19
    sprite('Action_236_06', 3)	# 20-22
    sprite('Action_236_07', 2)	# 23-24	 **attackbox here**
    sprite('Action_236_08', 2)	# 25-26	 **attackbox here**
    sprite('Action_236_09', 2)	# 27-28	 **attackbox here**
    sprite('Action_236_10', 3)	# 29-31
    sprite('Action_236_11', 2)	# 32-33
    sprite('Action_236_12', 2)	# 34-35
    sprite('Action_236_13', 2)	# 36-37
    sprite('Action_236_14', 2)	# 38-39
    SFX_3('SE_SheatheSword')
    sprite('Action_418_00', 4)	# 40-43
    sprite('Action_418_01', 4)	# 44-47
    sprite('Action_418_02', 2)	# 48-49

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(90)
        AttackP2(75)
        Unknown11092(1)
        Hitstop(2)
        AirUntechableTime(30)
        Unknown9016(1)
        HitLow(2)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(1500)
        AirPushbackY(14000)
        YImpluseBeforeWallbounce(1500)
        PushbackX(12000)
        callSubroutine('ChainRoot')
        HitJumpCancel(1)
        Unknown14085('CmnActCrushAttack')
    sprite('Action_006_00', 3)	# 1-3
    sprite('Action_006_00', 1)	# 4-4
    SLOT_4 = 0
    sprite('Action_006_01', 4)	# 5-8
    sprite('Action_006_02', 3)	# 9-11
    teleportRelativeX(44000)
    Unknown7007('7579753130375f300000000000000000640000007579753130375f310000000000000000640000007579753130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_006_03', 2)	# 12-13	 **attackbox here**
    teleportRelativeX(47000)
    GFX_0('2C_Blade_1st', 100)
    SFX_3('SE_DrawnSword')
    sprite('Action_006_04', 2)	# 14-15	 **attackbox here**
    sprite('Action_006_05', 2)	# 16-17	 **attackbox here**
    sprite('Action_006_06', 2)	# 18-19	 **attackbox here**
    SFX_3('SE043')
    GFX_0('2C_Blade_2nd', 100)
    sprite('Action_006_07', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    Unknown9071()
    AirPushbackY(15000)
    Unknown9095()
    Hitstop(12)
    Unknown9215()
    sprite('Action_006_08', 3)	# 22-24
    Recovery()
    Unknown2063()
    sprite('Action_006_09', 5)	# 25-29
    sprite('Action_006_10', 4)	# 30-33
    sprite('Action_006_11', 3)	# 34-36	 **attackbox here**
    sprite('Action_006_12', 6)	# 37-42	 **attackbox here**
    SFX_3('SE_SheatheSword')
    sprite('Action_006_13', 4)	# 43-46	 **attackbox here**
    sprite('Action_006_14', 3)	# 47-49
    loopRest()

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1550)
        AirPushbackY(22000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A_2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_008_00', 5)	# 1-5
    sprite('Action_008_01', 5)	# 6-10
    sprite('Action_008_02', 2)	# 11-12	 **attackbox here**
    SLOT_4 = 0
    Unknown7009(3)
    GFX_0('AIR5B_Blade', 100)
    SFX_3('SE042')
    SFX_3('SE_DrawnSword')
    sprite('Action_008_03', 2)	# 13-14
    Recovery()
    Unknown2063()
    sprite('Action_008_04', 5)	# 15-19
    sprite('Action_008_05', 4)	# 20-23
    sprite('Action_008_06', 6)	# 24-29
    GFX_0('AIR5B_Release', 100)
    SFX_3('SE_SheatheSword')
    sprite('Action_008_07', 5)	# 30-34

@State
def NmlAtkAIR5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1550)
        AirPushbackY(22000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_009_00', 3)	# 1-3
    sprite('Action_009_01', 4)	# 4-7
    sprite('Action_009_02', 2)	# 8-9	 **attackbox here**
    SLOT_4 = 0
    SFX_3('SE_DrawnSword')
    SFX_3('SE043')
    Unknown7009(5)
    GFX_0('AIR5C_Blade', 100)
    sprite('Action_009_03', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('Action_009_04', 4)	# 14-17
    sprite('Action_009_05', 4)	# 18-21
    SFX_3('SE_SheatheSword')
    GFX_0('AIR5C_Release', 100)
    sprite('Action_009_06', 4)	# 22-25
    sprite('Action_009_07', 4)	# 26-29

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1600)
        Unknown9016(1)
        AirUntechableTime(17)
        Hitstop(8)
        AirPushbackY(12000)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('AN_NmlAtkAIR5B_2nd')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_3():
            if (SLOT_18 > 3):
                SLOT_4 = 0
    if SLOT_4:
        _gotolabel(100)
    sprite('Action_467_00', 3)	# 1-3
    sprite('Action_467_01', 3)	# 4-6
    sprite('Action_467_02', 3)	# 7-9
    label(100)
    sprite('Action_467_03', 4)	# 10-13
    Unknown20(6, 2, 4)
    sprite('Action_467_04ex01', 3)	# 14-16	 **attackbox here**
    Unknown7006('uyu109_0', 100, 829782389, 828324144, 0, 0, 100, 829782389, 845101360, 0, 0, 100, 863336821, 811545904, 0, 0, 100)
    SFX_3('SE_DrawnSword')
    GFX_0('AIR6C_Blade', 100)
    sprite('Action_467_05', 2)	# 17-18	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_467_06', 4)	# 19-22	 **attackbox here**
    sprite('Action_467_07', 5)	# 23-27	 **attackbox here**
    sprite('Action_467_08', 7)	# 28-34	 **attackbox here**
    SFX_3('SE_SheatheSword')
    sprite('Action_423_00', 2)	# 35-36
    sprite('Action_423_01', 2)	# 37-38

@State
def AN_NmlAtkAIR5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1600)
        Unknown9016(1)
        AirUntechableTime(22)
        Hitstop(8)
        AirPushbackY(28000)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('AN_NmlAtkAIR5B_3rd')
        HitOrBlockJumpCancel(1)
    sprite('Action_466_03', 6)	# 1-6
    sprite('Action_466_04', 3)	# 7-9	 **attackbox here**
    Unknown7006('uyu109_0', 100, 829782389, 828324144, 0, 0, 100, 829782389, 845101360, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('SE_DrawnSword')
    GFX_0('AIR6B_Blade', 100)
    sprite('Action_466_05', 2)	# 10-11	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_466_06', 4)	# 12-15	 **attackbox here**
    sprite('Action_466_07', 5)	# 16-20	 **attackbox here**
    sprite('Action_466_08', 7)	# 21-27	 **attackbox here**
    SFX_3('SE_SheatheSword')
    sprite('Action_423_00', 2)	# 28-29
    sprite('Action_423_01', 2)	# 30-31

@State
def AN_NmlAtkAIR5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        Damage(2300)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackY(12000)
        AirPushbackX(60000)
        AirUntechableTime(60)
        Unknown9202(10)
        WallbounceReboundTime(0)
        PushbackX(30400)
        Hitstop(2)
        Unknown11001(0, 6, 11)
        Unknown9016(1)
        JumpCancel_(0)
        Unknown1017()
        Unknown1022()
    label(100)
    sprite('Action_421_03', 3)	# 1-3
    Unknown1084(1)
    sprite('Action_421_04', 5)	# 4-8
    SFX_3('SE_DrawnSword')
    SFX_4('uyu105_1')
    sprite('Action_225_03', 3)	# 9-11
    GFX_0('FF_Sakura3', 100)
    sprite('Action_225_04', 2)	# 12-13	 **attackbox here**
    sprite('Action_225_05', 2)	# 14-15	 **attackbox here**
    sprite('Action_225_06', 6)	# 16-21	 **attackbox here**
    GFX_0('FF_Blade_1st', 100)
    GFX_0('FF_Blade_2nd', 100)
    sprite('Action_225_07', 6)	# 22-27
    Recovery()
    sprite('Action_225_08', 4)	# 28-31	 **attackbox here**
    sprite('Action_225_09', 4)	# 32-35	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(60)
    YAccel(60)
    setGravity(2800)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_225_10', 6)	# 36-41	 **attackbox here**
    sprite('Action_225_11', 6)	# 42-47
    SFX_3('SE_SheatheSword')
    sprite('Action_423_00', 2)	# 48-49
    sprite('Action_423_01', 2)	# 50-51
    sprite('Action_423_02', 2)	# 52-53
    sprite('Action_423_03', 2)	# 54-55
    sprite('Action_423_04', 2)	# 56-57
    label(0)
    sprite('Action_022_00', 3)	# 58-60
    sprite('Action_022_01', 3)	# 61-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_023_00', 1)	# 64-64
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_023_01', 1)	# 65-65
    sprite('Action_023_02', 1)	# 66-66
    sprite('Action_023_03', 1)	# 67-67

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1500)
        AirUntechableTime(60)
        Unknown9154(23)
        Unknown11001(0, -3, 2)
        AirPushbackX(15000)
        AirPushbackY(-70000)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockJumpCancel(1)
        loopRelated(17, 300)

        def upon_17():
            clearUponHandler(17)
            Unknown1043()
    sprite('Action_007_00', 4)	# 1-4
    sprite('Action_007_01', 6)	# 5-10
    SFX_1('uyu108_1')
    SFX_3('SE043')
    sprite('Action_007_02', 4)	# 11-14	 **attackbox here**
    SLOT_4 = 0
    label(0)
    sprite('Action_007_03', 5)	# 15-19	 **attackbox here**
    sprite('Action_007_04', 5)	# 20-24	 **attackbox here**
    gotoLabel(0)

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
                SLOT_4 = 0
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('Action_045_00', 6)	# 1-6
    sprite('Action_045_01', 2)	# 7-8
    SFX_0('000_airdash_1')
    label(0)
    sprite('Action_045_02', 3)	# 9-11
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_03', 3)	# 12-14
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_06', 3)	# 21-23
    sprite('Action_045_07', 3)	# 24-26
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 27-27
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_00', 2)	# 28-29
    SFX_3('SE042')
    sprite('Action_055_01', 3)	# 30-32	 **attackbox here**
    Unknown1084(1)
    sprite('Action_055_02', 2)	# 33-34
    SFX_4('uyu154')
    sprite('Action_055_03', 5)	# 35-39
    sprite('Action_055_04', 6)	# 40-45
    sprite('Action_055_05', 5)	# 46-50
    sprite('Action_055_06', 5)	# 51-55

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(16)
        Unknown9142(100)
    sprite('Action_056_00', 6)	# 1-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_056_01', 2)	# 7-8
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('Action_057_00', 4)	# 9-12
    SFX_1('uyu153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_01', 8)	# 13-20
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 25)	# 21-45
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 4)	# 46-49
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_04', 2)	# 50-51	 **attackbox here**
    teleportRelativeX(104000)
    physicsXImpulse(5000)
    Unknown1028(-500)
    StartMultihit()
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('Action_057_04', 7)	# 52-58	 **attackbox here**
    sprite('Action_057_05', 3)	# 59-61
    sprite('Action_057_06', 5)	# 62-66
    sprite('Action_057_07', 5)	# 67-71
    Unknown1084(1)
    sprite('Action_057_08', 5)	# 72-76
    sprite('Action_057_09', 4)	# 77-80
    sprite('Action_057_10', 4)	# 81-84

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
                SLOT_4 = 0
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('Action_045_00', 6)	# 1-6
    sprite('Action_045_01', 2)	# 7-8
    SFX_0('000_airdash_1')
    label(0)
    sprite('Action_045_02', 3)	# 9-11
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_03', 3)	# 12-14
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_06', 3)	# 21-23
    sprite('Action_045_07', 3)	# 24-26
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 27-27
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_00', 2)	# 28-29
    SFX_3('SE042')
    sprite('Action_055_01', 3)	# 30-32	 **attackbox here**
    Unknown1084(1)
    sprite('Action_055_02', 2)	# 33-34
    SFX_4('uyu154')
    sprite('Action_055_03', 5)	# 35-39
    sprite('Action_055_04', 6)	# 40-45
    sprite('Action_055_05', 5)	# 46-50
    sprite('Action_055_06', 5)	# 51-55

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(16)
        Unknown9142(100)
    sprite('Action_056_00', 6)	# 1-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_056_01', 2)	# 7-8
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('Action_057_00', 4)	# 9-12
    SFX_4('uyu153')
    Unknown2005()
    Unknown36(22)
    Unknown2005()
    Unknown35()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_01', 8)	# 13-20
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 25)	# 21-45
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 4)	# 46-49
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_04', 2)	# 50-51	 **attackbox here**
    teleportRelativeX(104000)
    physicsXImpulse(5000)
    Unknown1028(-500)
    StartMultihit()
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('Action_057_04', 7)	# 52-58	 **attackbox here**
    sprite('Action_057_05', 3)	# 59-61
    sprite('Action_057_06', 5)	# 62-66
    sprite('Action_057_07', 5)	# 67-71
    Unknown1084(1)
    sprite('Action_057_08', 5)	# 72-76
    sprite('Action_057_09', 4)	# 77-80
    sprite('Action_057_10', 4)	# 81-84

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
    sprite('Action_068_00', 3)	# 1-3
    sprite('Action_068_00', 1)	# 4-4
    SLOT_4 = 0
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
    tag_voice(1, 'uyu156_0', 'uyu156_1', '', '')
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 2)	# 14-15
    sprite('Action_137_11', 4)	# 16-19
    sprite('Action_137_12', 4)	# 20-23
    sprite('Action_137_13', 2)	# 24-25
    GFX_0('AIR2C_Blade', 100)
    SFX_3('SE043')
    SFX_3('SE_DrawnSword')
    sprite('Action_137_14', 3)	# 26-28	 **attackbox here**
    sprite('Action_137_14', 2)	# 29-30	 **attackbox here**
    Unknown23027()
    sprite('Action_137_15', 4)	# 31-34
    sprite('Action_137_16', 3)	# 35-37
    sprite('Action_137_17', 4)	# 38-41
    sprite('Action_137_18', 4)	# 42-45
    sprite('Action_137_19', 6)	# 46-51
    label(0)
    sprite('Action_007_03', 5)	# 52-56	 **attackbox here**
    sprite('Action_007_04', 5)	# 57-61	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_014_00', 4)	# 62-65
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_014_01', 3)	# 66-68
    sprite('Action_014_02', 3)	# 69-71
    Unknown18009(0)
    sprite('Action_014_03', 3)	# 72-74

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 19)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_137_14', 2)	# 1-2	 **attackbox here**
    Unknown23027()
    sprite('Action_137_15', 4)	# 3-6
    label(0)
    sprite('Action_068_09', 3)	# 7-9
    sprite('Action_068_10', 2)	# 10-11
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_069_01', 3)	# 12-14
    sprite('Action_069_02', 3)	# 15-17
    sprite('Action_069_03', 30)	# 18-47
    label(2)
    sprite('Action_136_00', 1)	# 48-48
    sprite('Action_136_01', 2)	# 49-50
    teleportRelativeX(50000)
    sprite('Action_136_02', 2)	# 51-52
    teleportRelativeX(50000)
    sprite('Action_136_03', 2)	# 53-54
    teleportRelativeX(50000)
    sprite('Action_136_04', 3)	# 55-57	 **attackbox here**
    teleportRelativeX(20000)
    tag_voice(0, 'uyu157_0', 'uyu157_1', '', '')
    sprite('Action_136_05', 3)	# 58-60	 **attackbox here**
    RefreshMultihit()
    GFX_0('4C_Zanzo', 100)
    SFX_3('SE_ClothesSwing2')
    sprite('Action_136_06', 5)	# 61-65	 **attackbox here**
    sprite('Action_136_07', 5)	# 66-70	 **attackbox here**
    label(10)
    sprite('Action_000_00', 8)	# 71-78	 **attackbox here**
    sprite('Action_000_01', 8)	# 79-86	 **attackbox here**
    sprite('Action_000_02', 8)	# 87-94	 **attackbox here**
    sprite('Action_000_03', 8)	# 95-102	 **attackbox here**
    sprite('Action_000_04', 8)	# 103-110	 **attackbox here**
    sprite('Action_000_05', 8)	# 111-118	 **attackbox here**
    sprite('Action_000_06', 8)	# 119-126	 **attackbox here**
    sprite('Action_000_07', 8)	# 127-134	 **attackbox here**
    sprite('Action_000_08', 8)	# 135-142	 **attackbox here**
    sprite('Action_000_09', 8)	# 143-150	 **attackbox here**
    sprite('Action_000_10', 8)	# 151-158	 **attackbox here**
    sprite('Action_000_11', 8)	# 159-166	 **attackbox here**
    sprite('Action_000_12', 8)	# 167-174	 **attackbox here**
    sprite('Action_000_13', 8)	# 175-182	 **attackbox here**
    sprite('Action_000_14', 8)	# 183-190	 **attackbox here**
    sprite('Action_000_15', 8)	# 191-198	 **attackbox here**
    sprite('Action_000_16', 8)	# 199-206	 **attackbox here**
    sprite('Action_000_17', 8)	# 207-214	 **attackbox here**
    sprite('Action_000_18', 8)	# 215-222	 **attackbox here**
    sprite('Action_000_19', 8)	# 223-230	 **attackbox here**
    sprite('Action_000_20', 8)	# 231-238	 **attackbox here**
    sprite('Action_000_21', 8)	# 239-246	 **attackbox here**
    sprite('Action_000_22', 8)	# 247-254	 **attackbox here**
    sprite('Action_000_23', 8)	# 255-262	 **attackbox here**
    sprite('Action_000_24', 8)	# 263-270	 **attackbox here**
    sprite('Action_000_25', 8)	# 271-278	 **attackbox here**
    sprite('Action_000_26', 8)	# 279-286	 **attackbox here**
    sprite('Action_000_27', 8)	# 287-294	 **attackbox here**
    sprite('Action_000_28', 8)	# 295-302	 **attackbox here**
    sprite('Action_000_29', 8)	# 303-310	 **attackbox here**
    sprite('Action_000_30', 8)	# 311-318	 **attackbox here**
    sprite('Action_000_31', 8)	# 319-326	 **attackbox here**
    sprite('Action_000_32', 6)	# 327-332	 **attackbox here**
    sprite('Action_000_33', 2)	# 333-334	 **attackbox here**
    sprite('Action_000_34', 8)	# 335-342	 **attackbox here**
    sprite('Action_000_35', 8)	# 343-350	 **attackbox here**
    sprite('Action_000_36', 8)	# 351-358	 **attackbox here**
    sprite('Action_000_37', 8)	# 359-366	 **attackbox here**
    sprite('Action_000_38', 8)	# 367-374	 **attackbox here**
    sprite('Action_000_39', 8)	# 375-382	 **attackbox here**
    sprite('Action_000_40', 8)	# 383-390	 **attackbox here**
    sprite('Action_000_41', 8)	# 391-398	 **attackbox here**
    sprite('Action_000_42', 8)	# 399-406	 **attackbox here**
    sprite('Action_000_43', 8)	# 407-414	 **attackbox here**
    sprite('Action_000_44', 8)	# 415-422	 **attackbox here**
    sprite('Action_000_45', 8)	# 423-430	 **attackbox here**
    sprite('Action_000_46', 8)	# 431-438	 **attackbox here**
    sprite('Action_000_47', 8)	# 439-446	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 447-447

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_136_08', 4)	# 1-4
    sprite('Action_134_02', 4)	# 5-8
    teleportRelativeX(60000)
    sprite('Action_134_03', 4)	# 9-12
    teleportRelativeX(-60000)
    GFX_0('4B_Zanzo', 100)
    SFX_3('SE_ClothesSwing1')
    sprite('Action_134_04', 2)	# 13-14
    teleportRelativeX(-42000)
    sprite('Action_134_05', 3)	# 15-17	 **attackbox here**
    sprite('Action_134_06', 3)	# 18-20
    sprite('Action_134_07', 6)	# 21-26
    sprite('Action_134_08', 5)	# 27-31
    teleportRelativeX(-55000)
    sprite('Action_134_09', 5)	# 32-36
    sprite('Action_134_10', 5)	# 37-41
    label(0)
    sprite('Action_000_00', 8)	# 42-49	 **attackbox here**
    sprite('Action_000_01', 8)	# 50-57	 **attackbox here**
    sprite('Action_000_02', 8)	# 58-65	 **attackbox here**
    sprite('Action_000_03', 8)	# 66-73	 **attackbox here**
    sprite('Action_000_04', 8)	# 74-81	 **attackbox here**
    sprite('Action_000_05', 8)	# 82-89	 **attackbox here**
    sprite('Action_000_06', 8)	# 90-97	 **attackbox here**
    sprite('Action_000_07', 8)	# 98-105	 **attackbox here**
    sprite('Action_000_08', 8)	# 106-113	 **attackbox here**
    sprite('Action_000_09', 8)	# 114-121	 **attackbox here**
    sprite('Action_000_10', 8)	# 122-129	 **attackbox here**
    sprite('Action_000_11', 8)	# 130-137	 **attackbox here**
    sprite('Action_000_12', 8)	# 138-145	 **attackbox here**
    sprite('Action_000_13', 8)	# 146-153	 **attackbox here**
    sprite('Action_000_14', 8)	# 154-161	 **attackbox here**
    sprite('Action_000_15', 8)	# 162-169	 **attackbox here**
    sprite('Action_000_16', 8)	# 170-177	 **attackbox here**
    sprite('Action_000_17', 8)	# 178-185	 **attackbox here**
    sprite('Action_000_18', 8)	# 186-193	 **attackbox here**
    sprite('Action_000_19', 8)	# 194-201	 **attackbox here**
    sprite('Action_000_20', 8)	# 202-209	 **attackbox here**
    sprite('Action_000_21', 8)	# 210-217	 **attackbox here**
    sprite('Action_000_22', 8)	# 218-225	 **attackbox here**
    sprite('Action_000_23', 8)	# 226-233	 **attackbox here**
    sprite('Action_000_24', 8)	# 234-241	 **attackbox here**
    sprite('Action_000_25', 8)	# 242-249	 **attackbox here**
    sprite('Action_000_26', 8)	# 250-257	 **attackbox here**
    sprite('Action_000_27', 8)	# 258-265	 **attackbox here**
    sprite('Action_000_28', 8)	# 266-273	 **attackbox here**
    sprite('Action_000_29', 8)	# 274-281	 **attackbox here**
    sprite('Action_000_30', 8)	# 282-289	 **attackbox here**
    sprite('Action_000_31', 8)	# 290-297	 **attackbox here**
    sprite('Action_000_32', 6)	# 298-303	 **attackbox here**
    sprite('Action_000_33', 2)	# 304-305	 **attackbox here**
    sprite('Action_000_34', 8)	# 306-313	 **attackbox here**
    sprite('Action_000_35', 8)	# 314-321	 **attackbox here**
    sprite('Action_000_36', 8)	# 322-329	 **attackbox here**
    sprite('Action_000_37', 8)	# 330-337	 **attackbox here**
    sprite('Action_000_38', 8)	# 338-345	 **attackbox here**
    sprite('Action_000_39', 8)	# 346-353	 **attackbox here**
    sprite('Action_000_40', 8)	# 354-361	 **attackbox here**
    sprite('Action_000_41', 8)	# 362-369	 **attackbox here**
    sprite('Action_000_42', 8)	# 370-377	 **attackbox here**
    sprite('Action_000_43', 8)	# 378-385	 **attackbox here**
    sprite('Action_000_44', 8)	# 386-393	 **attackbox here**
    sprite('Action_000_45', 8)	# 394-401	 **attackbox here**
    sprite('Action_000_46', 8)	# 402-409	 **attackbox here**
    sprite('Action_000_47', 8)	# 410-417	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 418-418

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('Action_003_00', 5)	# 1-5
    sprite('Action_003_01', 5)	# 6-10
    teleportRelativeX(-7000)
    sprite('Action_003_01', 2)	# 11-12
    sprite('Action_003_02', 4)	# 13-16
    sprite('Action_003_03', 3)	# 17-19
    tag_voice(0, 'uyu158_0', 'uyu158_1', '', '')
    sprite('Action_003_04', 4)	# 20-23	 **attackbox here**
    teleportRelativeX(50000)
    SFX_3('SE043')
    SFX_3('SE_DrawnSword')
    GFX_0('5C_Blade', 100)
    sprite('Action_003_05', 4)	# 24-27
    sprite('Action_003_06', 5)	# 28-32
    sprite('Action_003_07', 4)	# 33-36
    sprite('Action_003_08', 3)	# 37-39	 **attackbox here**
    teleportRelativeX(-50000)
    sprite('Action_003_09', 5)	# 40-44	 **attackbox here**
    sprite('Action_003_10', 6)	# 45-50	 **attackbox here**
    sprite('Action_003_11', 7)	# 51-57
    sprite('Action_003_12', 3)	# 58-60
    sprite('Action_003_13', 4)	# 61-64

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 26)	# 1-26
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 27-27
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-950000)
    Unknown1007(100000)
    physicsXImpulse(75000)
    physicsYImpulse(10000)
    setGravity(1500)
    sprite('Action_035_05', 6)	# 28-33
    Unknown1019(60)
    sprite('Action_008_00', 4)	# 34-37
    Unknown1019(70)
    sprite('Action_008_01', 4)	# 38-41

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        sendToLabel(1)
    Unknown1019(70)
    sprite('Action_008_02', 3)	# 42-44	 **attackbox here**
    GFX_0('AIR5B_Blade', 100)
    SFX_3('SE042')
    SFX_3('SE_DrawnSword')
    Unknown1019(70)
    sprite('Action_008_03', 3)	# 45-47
    sprite('Action_008_04', 5)	# 48-52
    sprite('Action_008_05', 3)	# 53-55
    GFX_0('AIR5B_Release', 100)
    sprite('Action_008_06', 5)	# 56-60
    sprite('Action_008_07', 32767)	# 61-32827
    label(1)
    sprite('Action_008_08', 3)	# 32828-32830
    sprite('Action_008_09', 3)	# 32831-32833
    sprite('Action_008_10', 3)	# 32834-32836
    sprite('Action_008_11', 3)	# 32837-32839
    sprite('Action_000_00', 8)	# 32840-32847	 **attackbox here**
    sprite('Action_000_01', 8)	# 32848-32855	 **attackbox here**
    sprite('Action_000_02', 8)	# 32856-32863	 **attackbox here**
    sprite('Action_000_03', 8)	# 32864-32871	 **attackbox here**
    sprite('Action_000_04', 8)	# 32872-32879	 **attackbox here**
    sprite('Action_000_05', 8)	# 32880-32887	 **attackbox here**
    sprite('Action_000_06', 8)	# 32888-32895	 **attackbox here**
    sprite('Action_000_07', 8)	# 32896-32903	 **attackbox here**
    sprite('Action_000_08', 8)	# 32904-32911	 **attackbox here**
    sprite('Action_000_09', 8)	# 32912-32919	 **attackbox here**
    sprite('Action_000_10', 8)	# 32920-32927	 **attackbox here**
    sprite('Action_000_11', 8)	# 32928-32935	 **attackbox here**
    sprite('Action_000_12', 8)	# 32936-32943	 **attackbox here**
    sprite('Action_000_13', 8)	# 32944-32951	 **attackbox here**
    sprite('Action_000_14', 8)	# 32952-32959	 **attackbox here**
    sprite('Action_000_15', 8)	# 32960-32967	 **attackbox here**
    sprite('Action_000_16', 8)	# 32968-32975	 **attackbox here**
    sprite('Action_000_17', 8)	# 32976-32983	 **attackbox here**
    sprite('Action_000_18', 8)	# 32984-32991	 **attackbox here**
    sprite('Action_000_19', 8)	# 32992-32999	 **attackbox here**
    sprite('Action_000_20', 8)	# 33000-33007	 **attackbox here**
    sprite('Action_000_21', 8)	# 33008-33015	 **attackbox here**
    sprite('Action_000_22', 8)	# 33016-33023	 **attackbox here**
    sprite('Action_000_23', 8)	# 33024-33031	 **attackbox here**
    sprite('Action_000_24', 8)	# 33032-33039	 **attackbox here**
    sprite('Action_000_25', 8)	# 33040-33047	 **attackbox here**
    sprite('Action_000_26', 8)	# 33048-33055	 **attackbox here**
    sprite('Action_000_27', 8)	# 33056-33063	 **attackbox here**
    sprite('Action_000_28', 8)	# 33064-33071	 **attackbox here**
    sprite('Action_000_29', 8)	# 33072-33079	 **attackbox here**
    sprite('Action_000_30', 8)	# 33080-33087	 **attackbox here**
    sprite('Action_000_31', 8)	# 33088-33095	 **attackbox here**
    sprite('Action_000_32', 6)	# 33096-33101	 **attackbox here**
    sprite('Action_000_33', 2)	# 33102-33103	 **attackbox here**
    sprite('Action_000_34', 8)	# 33104-33111	 **attackbox here**
    sprite('Action_000_35', 8)	# 33112-33119	 **attackbox here**
    sprite('Action_000_36', 8)	# 33120-33127	 **attackbox here**
    sprite('Action_000_37', 8)	# 33128-33135	 **attackbox here**
    sprite('Action_000_38', 8)	# 33136-33143	 **attackbox here**
    sprite('Action_000_39', 8)	# 33144-33151	 **attackbox here**
    sprite('Action_000_40', 8)	# 33152-33159	 **attackbox here**
    sprite('Action_000_41', 8)	# 33160-33167	 **attackbox here**
    sprite('Action_000_42', 8)	# 33168-33175	 **attackbox here**
    sprite('Action_000_43', 8)	# 33176-33183	 **attackbox here**
    sprite('Action_000_44', 8)	# 33184-33191	 **attackbox here**
    sprite('Action_000_45', 8)	# 33192-33199	 **attackbox here**
    sprite('Action_000_46', 8)	# 33200-33207	 **attackbox here**
    sprite('Action_000_47', 8)	# 33208-33215	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('keep', 2)	# 1-2
    sprite('Action_002_00', 5)	# 3-7
    sprite('Action_002_01', 4)	# 8-11
    sprite('Action_002_02', 3)	# 12-14	 **attackbox here**
    GFX_0('5B_Blade', 100)
    SFX_3('SE042')
    SFX_3('SE_DrawnSword')
    sprite('Action_002_03', 4)	# 15-18
    Recovery()
    Unknown2063()
    sprite('Action_002_04', 3)	# 19-21
    sprite('Action_002_05', 4)	# 22-25
    sprite('Action_002_06', 3)	# 26-28
    sprite('Action_002_07', 2)	# 29-30	 **attackbox here**
    sprite('Action_002_08', 3)	# 31-33	 **attackbox here**
    sprite('Action_002_09', 3)	# 34-36	 **attackbox here**
    sprite('Action_002_10', 5)	# 37-41	 **attackbox here**
    sprite('Action_002_11', 6)	# 42-47	 **attackbox here**
    Unknown13002(1)
    Unknown13003(1)
    Unknown13005(1)
    Unknown13006(1)
    Unknown13008(1)
    Unknown13014(1)
    Unknown13015(1)
    Unknown13017(1)
    Unknown13021(1)
    Unknown13019(1)
    Unknown13026(1)
    Unknown13029(1)
    Unknown13031(1)
    sprite('Action_002_12', 7)	# 48-54
    sprite('Action_002_13', 3)	# 55-57
    sprite('Action_002_14', 4)	# 58-61
    loopRest()

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
    sprite('Action_003_00', 5)	# 1-5
    sprite('Action_003_01', 5)	# 6-10
    teleportRelativeX(-7000)
    sprite('Action_003_01', 2)	# 11-12
    sprite('Action_003_02', 4)	# 13-16
    sprite('Action_003_03', 3)	# 17-19
    sprite('Action_003_04', 4)	# 20-23	 **attackbox here**
    teleportRelativeX(50000)
    SFX_3('SE043')
    SFX_3('SE_DrawnSword')
    GFX_0('5C_Blade', 100)
    sprite('Action_003_05', 4)	# 24-27
    sprite('Action_003_06', 5)	# 28-32
    sprite('Action_003_07', 4)	# 33-36
    sprite('Action_003_08', 3)	# 37-39	 **attackbox here**
    teleportRelativeX(-50000)
    sprite('Action_003_09', 5)	# 40-44	 **attackbox here**
    sprite('Action_003_10', 6)	# 45-50	 **attackbox here**
    sprite('Action_003_11', 7)	# 51-57
    sprite('Action_003_12', 3)	# 58-60
    sprite('Action_003_13', 4)	# 61-64

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1000)
        PushbackX(12000)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(60)

        def upon_78():
            SLOT_51 = 1

        def upon_43():
            if (SLOT_48 == 1000):
                Unknown2038(1)
    if SLOT_4:
        _gotolabel(0)
    sprite('Action_450_00', 1)	# 1-1
    Unknown1084(1)
    sprite('Action_450_01', 1)	# 2-2
    sprite('Action_450_02', 1)	# 3-3
    sprite('Action_450_03', 1)	# 4-4
    sprite('Action_450_04', 1)	# 5-5
    label(0)
    sprite('Action_450_05', 3)	# 6-8
    SLOT_4 = 0
    sprite('Action_450_06', 3)	# 9-11
    sprite('Action_461_00', 2)	# 12-13
    physicsXImpulse(24000)
    physicsYImpulse(1200)
    Unknown23087(60000)
    Unknown7006('uyu203_0', 100, 846559605, 828322608, 0, 0, 100, 846559605, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown4004('6566666563745f3530350000000000000000000000000000000000000000000064000000')
    SFX_0('002_highjump_0')
    sprite('Action_461_01', 1)	# 14-14
    sprite('Action_461_02', 1)	# 15-15
    physicsYImpulse(28000)
    setGravity(2500)
    sprite('Action_461_03ex01', 2)	# 16-17	 **attackbox here**
    sprite('Action_461_04ex01', 3)	# 18-20	 **attackbox here**
    if SLOT_51:
        Unknown2017(0)
    sprite('Action_461_05', 3)	# 21-23
    sprite('Action_461_06', 1)	# 24-24
    SFX_3('SE_DrawnSword')
    sprite('Action_461_07', 3)	# 25-27
    GFX_0('Yae_AtkCol', -1)
    setGravity(1200)
    sendToLabelUpon(2, 10)
    sprite('Action_461_08', 4)	# 28-31
    setInvincible(0)
    sprite('Action_461_09', 4)	# 32-35
    Unknown2017(1)
    sprite('Action_461_10', 4)	# 36-39
    sprite('Action_461_11', 4)	# 40-43
    sprite('Action_461_12', 4)	# 44-47
    GFX_0('Yae_AirRelease', -1)
    sprite('Action_461_13', 4)	# 48-51
    SFX_3('SE_SheatheSword')
    sprite('Action_461_14', 4)	# 52-55
    label(5)
    sprite('Action_461_13', 4)	# 56-59
    sprite('Action_461_14', 4)	# 60-63
    gotoLabel(5)
    label(10)
    sprite('Action_461_19', 3)	# 64-66
    Unknown8000(100, 1, 1)
    setInvincible(0)
    Unknown18009(1)
    Unknown1084(1)
    sprite('Action_461_20', 10)	# 67-76
    sprite('Action_461_21', 14)	# 77-90
    SFX_3('SE_SheatheSword')
    if SLOT_2:
        SFX_1('uyu203_2')
        GFX_0('Yae_AddAtk', 100)
        GFX_0('Yae_Release', 100)
    sprite('Action_461_22', 5)	# 91-95
    sprite('Action_461_23', 2)	# 96-97
    sprite('Action_461_15', 3)	# 98-100
    Unknown2006()
    sprite('Action_461_16', 3)	# 101-103
    sprite('Action_461_17', 3)	# 104-106
    Unknown18009(0)
    sprite('Action_461_18', 3)	# 107-109

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1000)
        PushbackX(12000)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(60)

        def upon_43():
            if (SLOT_48 == 1000):
                Unknown2038(1)
    if SLOT_4:
        _gotolabel(0)
    sprite('Action_489_00', 2)	# 1-2
    Unknown1084(1)
    sprite('Action_489_01', 2)	# 3-4
    sprite('Action_489_02', 2)	# 5-6
    label(0)
    sprite('Action_489_03', 3)	# 7-9
    SLOT_4 = 0
    clearUponHandler(2)
    sprite('Action_489_04', 3)	# 10-12
    sprite('Action_461_00', 2)	# 13-14
    physicsXImpulse(22500)
    physicsYImpulse(1200)
    Unknown7006('uyu203_0', 100, 846559605, 828322608, 0, 0, 100, 846559605, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown4004('6566666563745f3530360000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1072(75000)
    teleportRelativeX(-80000)
    Unknown1007(150000)
    Unknown35()
    SFX_0('001_airbackdash_0')
    sprite('Action_461_01', 1)	# 15-15
    sprite('Action_461_02', 1)	# 16-16
    physicsYImpulse(28000)
    setGravity(2500)
    sprite('Action_461_03', 2)	# 17-18	 **attackbox here**
    sprite('Action_461_04', 3)	# 19-21	 **attackbox here**
    Unknown2017(0)
    sprite('Action_461_05', 3)	# 22-24
    sprite('Action_461_06', 1)	# 25-25
    SFX_3('SE_DrawnSword')
    sprite('Action_461_07', 3)	# 26-28
    GFX_0('AirYae_AtkCol', -1)
    setGravity(1800)
    sendToLabelUpon(2, 10)
    sprite('Action_461_08', 4)	# 29-32
    setInvincible(0)
    sprite('Action_461_09', 4)	# 33-36
    Unknown2017(1)
    label(5)
    sprite('Action_461_10', 4)	# 37-40
    sprite('Action_461_09', 4)	# 41-44
    gotoLabel(5)
    label(10)
    sprite('Action_461_19', 3)	# 45-47
    Unknown8000(100, 1, 1)
    setInvincible(0)
    Unknown18009(1)
    Unknown1084(1)
    sprite('Action_461_20', 3)	# 48-50
    SFX_3('SE_SheatheSword')
    sprite('Action_461_21', 10)	# 51-60
    sprite('Action_461_22', 5)	# 61-65
    sprite('Action_461_23', 2)	# 66-67
    sprite('Action_461_15', 3)	# 68-70
    Unknown2006()
    sprite('Action_461_16', 3)	# 71-73
    sprite('Action_461_17', 3)	# 74-76
    Unknown18009(0)
    sprite('Action_461_18', 3)	# 77-79

@Subroutine
def SlashHoldToKamae():

    def upon_3():
        if CheckInput(0x1):
            SLOT_61 = (SLOT_61 + 1)
        elif CheckInput(0xa):
            SLOT_61 = (SLOT_61 + 1)
        elif CheckInput(0x13):
            SLOT_61 = (SLOT_61 + 1)
        else:
            SLOT_61 = 0
        if (SLOT_61 >= 21):
            SLOT_62 = 1
        if SLOT_62:
            if (not SLOT_61):
                if CheckInput(0xed):
                    SLOT_61 = 0
                    SLOT_62 = 0

@Subroutine
def SlashHasei_Input():
    Unknown14070('SlashA')
    Unknown14070('SlashB')
    Unknown14070('SlashC')
    Unknown14070('AirSlashA')
    Unknown14070('AirSlashB')
    Unknown14070('AirSlashC')
    Unknown14070('ShukuchiA')
    Unknown14070('ShukuchiB')
    Unknown14070('ShukuchiC')
    Unknown14070('AirShukuchiA')
    Unknown14070('AirShukuchiB')
    Unknown14070('AirShukuchiC')
    Unknown14070('SlashA_Comb')
    Unknown14070('SlashB_Comb')
    Unknown14070('SlashC_Comb')
    Unknown14070('AirSlashA_Comb')
    Unknown14070('AirSlashB_Comb')
    Unknown14070('AirSlashC_Comb')
    Unknown14070('ShukuchiA_Comb')
    Unknown14070('ShukuchiB_Comb')
    Unknown14070('ShukuchiC_Comb')
    Unknown14070('AirShukuchiA_Comb')
    Unknown14070('AirShukuchiB_Comb')
    Unknown14070('AirShukuchiC_Comb')

@Subroutine
def SlashHasei_Timing():
    if (not SLOT_58):
        Unknown14072('SlashA')
        Unknown14072('SlashB')
        Unknown14072('SlashC')
        Unknown14072('AirSlashA')
        Unknown14072('AirSlashB')
        Unknown14072('AirSlashC')
        Unknown14072('ShukuchiA')
        Unknown14072('ShukuchiB')
        Unknown14072('ShukuchiC')
        Unknown14072('AirShukuchiA')
        Unknown14072('AirShukuchiB')
        Unknown14072('AirShukuchiC')
        Unknown14072('SlashA_Comb')
        Unknown14072('SlashB_Comb')
        Unknown14072('SlashC_Comb')
        Unknown14072('AirSlashA_Comb')
        Unknown14072('AirSlashB_Comb')
        Unknown14072('AirSlashC_Comb')
        Unknown14072('ShukuchiA_Comb')
        Unknown14072('ShukuchiB_Comb')
        Unknown14072('ShukuchiC_Comb')
        Unknown14072('AirShukuchiA_Comb')
        Unknown14072('AirShukuchiB_Comb')
        Unknown14072('AirShukuchiC_Comb')

@Subroutine
def SlashHasei_Clear():
    Unknown14074('SlashA')
    Unknown14074('SlashB')
    Unknown14074('SlashC')
    Unknown14074('AirSlashA')
    Unknown14074('AirSlashB')
    Unknown14074('AirSlashC')
    Unknown14074('ShukuchiA')
    Unknown14074('ShukuchiB')
    Unknown14074('ShukuchiC')
    Unknown14074('AirShukuchiA')
    Unknown14074('AirShukuchiB')
    Unknown14074('AirShukuchiC')
    Unknown14074('SlashA_Comb')
    Unknown14074('SlashB_Comb')
    Unknown14074('SlashC_Comb')
    Unknown14074('AirSlashA_Comb')
    Unknown14074('AirSlashB_Comb')
    Unknown14074('AirSlashC_Comb')
    Unknown14074('ShukuchiA_Comb')
    Unknown14074('ShukuchiB_Comb')
    Unknown14074('ShukuchiC_Comb')
    Unknown14074('AirShukuchiA_Comb')
    Unknown14074('AirShukuchiB_Comb')
    Unknown14074('AirShukuchiC_Comb')
    Unknown14074('CmnActInvincibleAttack')
    Unknown14074('CmnActInvincibleAttackAir')
    SLOT_60 = 0

@Subroutine
def SlashHaseiChallengeNamed():
    if SLOT_60:
        if Unknown23148('SlashA'):
            Unknown23159('SlashHaseiA')
        if Unknown23145('AirSlashA'):
            Unknown23159('SlashHaseiA')
        if Unknown23148('SlashB'):
            Unknown23159('SlashHaseiB')
        if Unknown23145('AirSlashB'):
            Unknown23159('SlashHaseiB')
        if Unknown23148('SlashC'):
            Unknown23159('SlashHaseiC')
        if Unknown23145('AirSlashC'):
            Unknown23159('SlashHaseiC')
        if Unknown23145('Shukuchi_End_Front'):
            Unknown23159('ShukuchiSlash')
        if Unknown23145('Shukuchi_End_Back'):
            Unknown23159('ShukuchiSlash')
        if Unknown23145('Shukuchi_End_FrontAir'):
            Unknown23159('ShukuchiSlash')
        if Unknown23145('Shukuchi_End_BackAir'):
            Unknown23159('ShukuchiSlash')
    else:
        if Unknown23148('SlashA'):
            Unknown23159('SlashNama')
        if Unknown23148('AirSlashA'):
            Unknown23159('AirSlashNama')
        if Unknown23148('SlashB'):
            Unknown23159('SlashNama')
        if Unknown23148('AirSlashB'):
            Unknown23159('AirSlashNama')
        if Unknown23148('SlashC'):
            Unknown23159('SlashNama')
        if Unknown23148('AirSlashC'):
            Unknown23159('AirSlashNama')
    if SLOT_4:
        if Unknown23148('SlashA'):
            Unknown23159('IaiSlash')
        if Unknown23148('SlashB'):
            Unknown23159('IaiSlash')
        if Unknown23148('SlashC'):
            Unknown23159('IaiSlash')
        if Unknown23148('AirSlashA'):
            Unknown23159('IaiAirSlash')
        if Unknown23148('AirSlashB'):
            Unknown23159('IaiAirSlash')
        if Unknown23148('AirSlashC'):
            Unknown23159('IaiAirSlash')

@Subroutine
def SlashAtk():
    AttackLevel_(4)
    Damage(1300)
    AttackP1(60)
    AttackP2(90)
    AirUntechableTime(38)
    PushbackX(12000)
    Unknown11001(4, 8, 16)
    Hitstop(1)
    Unknown11028(23)
    YImpluseBeforeWallbounce(2200)
    Unknown9016(1)
    Unknown11056(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown2037(1)
    callSubroutine('SlashHaseiChallengeNamed')
    if SLOT_4:
        if (not SLOT_60):
            SLOT_7 = 1
    if SLOT_7:
        SLOT_56 = 1
    if SLOT_60:
        SLOT_56 = 1
    if (not SLOT_60):
        SLOT_60 = 1
        SLOT_61 = 0
    if (SLOT_5 < 3):
        Unknown30068(1)
    if (SLOT_5 <= 1):
        SLOT_58 = 1
        Unknown11068(1)
        Unknown11044(1)

    def upon_78():
        SLOT_57 = 1
        if SLOT_58:
            Unknown14083(0)
            setInvincible(1)
            if (not SLOT_7):
                Unknown11069('Slash_AddAtk')
            elif SLOT_37:
                Unknown11069('SlashFinishSP')
            else:
                Unknown11069('AirSlashFinishSP')
    SLOT_9 = 0

    def upon_82():
        if SLOT_58:
            if (not SLOT_7):
                SLOT_9 = 1
    SLOT_4 = 0
    SLOT_62 = 0
    callSubroutine('SlashHoldToKamae')

    def upon_STATE_END():
        if (SLOT_18 <= 3):
            SLOT_60 = 0

@State
def SlashA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SlashAtk')
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(58000)
        AirPushbackY(18000)
        Unknown9178(1)
        WallbounceReboundTime(1)
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_438_00', 1)	# 1-1
    sprite('Action_438_01', 1)	# 2-2
    sprite('Action_438_02', 2)	# 3-4
    sprite('Action_438_03', 2)	# 5-6
    sprite('Action_438_04', 2)	# 7-8
    label(100)
    sprite('Action_438_05', 4)	# 9-12
    Unknown1084(1)
    sprite('Action_438_06', 2)	# 13-14
    SLOT_5 = (SLOT_5 + (-1))
    Unknown7006('uyu201_0', 100, 846559605, 828322096, 0, 0, 100, 863336821, 811545904, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_438_07', 1)	# 15-15
    GFX_0('SlashA_Blade', 100)
    callSubroutine('SlashHasei_Input')
    sprite('Action_438_08', 1)	# 16-16
    sprite('Action_438_09', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_DrawnSword')
    sprite('Action_438_12', 6)	# 19-24
    Recovery()
    if SLOT_2:
        callSubroutine('SlashHasei_Timing')
    if (not SLOT_7):
        if SLOT_58:
            if SLOT_57:
                enterState('SlashFinish')
    if SLOT_7:
        if SLOT_58:
            if SLOT_57:
                enterState('SlashFinishSP')
    sprite('Action_438_13', 6)	# 25-30
    sprite('Action_438_14', 3)	# 31-33	 **attackbox here**
    callSubroutine('SlashHasei_Clear')
    sprite('Action_438_15', 3)	# 34-36	 **attackbox here**
    sprite('Action_438_16', 3)	# 37-39	 **attackbox here**
    sprite('Action_438_17', 3)	# 40-42
    SFX_3('SE_SheatheSword')
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_438_18', 4)	# 43-46
    sprite('Action_438_19', 4)	# 47-50
    sprite('Action_438_20', 4)	# 51-54
    sprite('Action_438_21', 3)	# 55-57
    Unknown19(102, 2, 4)
    ExitState()
    label(101)
    sprite('Action_438_18', 2)	# 58-59
    sprite('Action_438_19', 2)	# 60-61
    sprite('Action_438_20', 2)	# 62-63
    sprite('Action_438_21', 1)	# 64-64
    label(102)
    sprite('Action_418_00', 3)	# 65-67
    sprite('Action_418_01', 3)	# 68-70
    sprite('Action_418_02', 2)	# 71-72

@State
def SlashB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SlashAtk')
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(1000)
        AirPushbackY(30000)
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_437_00', 1)	# 1-1
    sprite('Action_437_01', 1)	# 2-2
    sprite('Action_437_02', 2)	# 3-4
    sprite('Action_437_03', 2)	# 5-6
    sprite('Action_437_04', 2)	# 7-8
    label(100)
    sprite('Action_437_05', 3)	# 9-11
    Unknown1084(1)
    sprite('Action_437_05', 1)	# 12-12
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_437_06', 2)	# 13-14
    SLOT_5 = (SLOT_5 + (-1))
    Unknown7006('uyu200_0', 100, 846559605, 828321840, 0, 0, 100, 846559605, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_437_07', 1)	# 15-15
    GFX_0('SlashB_Blade', 100)
    callSubroutine('SlashHasei_Input')
    sprite('Action_437_08', 1)	# 16-16
    sprite('Action_437_09', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_DrawnSword')
    sprite('Action_437_12', 6)	# 19-24
    setInvincible(0)
    Recovery()
    if SLOT_2:
        callSubroutine('SlashHasei_Timing')
    if (not SLOT_7):
        if SLOT_58:
            if SLOT_57:
                enterState('SlashFinish')
    if SLOT_7:
        if SLOT_58:
            if SLOT_57:
                enterState('SlashFinishSP')
    sprite('Action_437_13', 6)	# 25-30
    sprite('Action_437_14', 3)	# 31-33	 **attackbox here**
    callSubroutine('SlashHasei_Clear')
    sprite('Action_437_15', 3)	# 34-36	 **attackbox here**
    sprite('Action_437_16', 3)	# 37-39	 **attackbox here**
    sprite('Action_437_17', 3)	# 40-42
    SFX_3('SE_SheatheSword')
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_437_18', 4)	# 43-46
    sprite('Action_437_19', 4)	# 47-50
    sprite('Action_437_20', 4)	# 51-54
    sprite('Action_437_21', 3)	# 55-57
    Unknown19(102, 2, 4)
    ExitState()
    label(101)
    sprite('Action_437_18', 2)	# 58-59
    sprite('Action_437_19', 2)	# 60-61
    sprite('Action_437_20', 2)	# 62-63
    sprite('Action_437_21', 1)	# 64-64
    label(102)
    sprite('Action_418_00', 3)	# 65-67
    sprite('Action_418_01', 3)	# 68-70
    sprite('Action_418_02', 2)	# 71-72

@State
def SlashC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SlashAtk')
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Damage(2200)
        AirPushbackX(58000)
        AirPushbackY(18000)
        PushbackX(30400)
        Unknown9178(1)
        WallbounceReboundTime(1)
        Unknown11091(10)
        Unknown30065(0)
        Unknown11001(8, 8, 16)
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_438_00', 1)	# 1-1
    sprite('Action_438_01', 1)	# 2-2
    sprite('Action_438_02', 1)	# 3-3
    sprite('Action_438_02', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_438_03', 2)	# 5-6
    sprite('Action_438_04', 2)	# 7-8
    label(100)
    sprite('Action_438_05', 3)	# 9-11
    sprite('Action_438_05', 1)	# 12-12
    if SLOT_56:
        Unknown23125('')
        Unknown2058(-5000)
    Unknown1084(1)
    sprite('Action_438_06', 2)	# 13-14
    SLOT_5 = (SLOT_5 + (-1))
    Unknown7006('uyu200_0', 100, 846559605, 828321840, 0, 0, 100, 846559605, 828323888, 0, 0, 100, 846559605, 845100848, 0, 0, 100)
    sprite('Action_438_07', 1)	# 15-15
    GFX_0('SlashEx_Blade', 100)
    callSubroutine('SlashHasei_Input')
    sprite('Action_438_08', 1)	# 16-16
    sprite('Action_438_09ex02', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_DrawnSword')
    sprite('Action_438_12', 6)	# 19-24
    Recovery()
    if SLOT_2:
        callSubroutine('SlashHasei_Timing')
    if (not SLOT_7):
        if SLOT_58:
            if SLOT_57:
                enterState('SlashFinish')
    if SLOT_7:
        if SLOT_58:
            if SLOT_57:
                enterState('SlashFinishSP')
    sprite('Action_438_13', 6)	# 25-30
    sprite('Action_438_14', 3)	# 31-33	 **attackbox here**
    callSubroutine('SlashHasei_Clear')
    sprite('Action_438_15', 3)	# 34-36	 **attackbox here**
    sprite('Action_438_16', 3)	# 37-39	 **attackbox here**
    sprite('Action_438_17', 3)	# 40-42
    SFX_3('SE_SheatheSword')
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_438_18', 4)	# 43-46
    sprite('Action_438_19', 4)	# 47-50
    sprite('Action_438_20', 4)	# 51-54
    sprite('Action_438_21', 3)	# 55-57
    Unknown19(102, 2, 4)
    ExitState()
    label(101)
    sprite('Action_438_18', 2)	# 58-59
    sprite('Action_438_19', 2)	# 60-61
    sprite('Action_438_20', 2)	# 62-63
    sprite('Action_438_21', 1)	# 64-64
    label(102)
    sprite('Action_418_00', 3)	# 65-67
    sprite('Action_418_01', 3)	# 68-70
    sprite('Action_418_02', 2)	# 71-72

@State
def SlashFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown30068(1)
        callSubroutine('SlashHoldToKamae')
        SLOT_60 = 0
    sprite('Action_439_20', 6)	# 1-6
    setInvincible(1)
    sprite('Action_439_21', 5)	# 7-11	 **attackbox here**
    sprite('Action_439_22', 5)	# 12-16	 **attackbox here**
    sprite('Action_439_23', 4)	# 17-20	 **attackbox here**
    sprite('Action_439_24', 4)	# 21-24
    Unknown7006('uyu301_0', 100, 863336821, 828322096, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_439_25', 11)	# 25-35	 **attackbox here**
    SFX_3('SE_SheatheSword')
    GFX_0('UltimateRush_Release', 100)
    GFX_0('Slash_AddAtk', 100)
    if SLOT_2:
        Unknown23029(1, 1100, 1)
    setInvincible(0)
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_439_26', 5)	# 36-40
    sprite('Action_439_27', 4)	# 41-44
    sprite('Action_439_28', 2)	# 45-46
    sprite('Action_420_00', 22)	# 47-68
    Unknown19(102, 2, 4)
    ExitState()
    label(101)
    sprite('Action_439_26', 3)	# 69-71
    sprite('Action_439_27', 2)	# 72-73
    sprite('Action_439_28', 1)	# 74-74
    label(102)
    sprite('Action_420_00', 19)	# 75-93
    sprite('Action_418_00', 3)	# 94-96
    sprite('Action_418_01', 3)	# 97-99
    sprite('Action_418_02', 2)	# 100-101

@State
def SlashFinishSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP2(90)
        Unknown11063(1)
        Unknown30068(1)
        callSubroutine('SlashHoldToKamae')
        SLOT_60 = 0
        Hitstop(10)
        AirPushbackX(30000)
        Unknown30055('d0dd06001e0000001e000000')
        Unknown30056('a08601001e0000001e000000')
        Unknown11056(2)
        Unknown23073()
        Unknown11068(1)
        Unknown14083(0)
        Unknown11044(1)
        Unknown11069('SlashFinishSP_AtkCol')

        def upon_43():
            if (SLOT_48 == 1000):
                Unknown23073()
                Unknown2038(1)
    sprite('Action_167_04', 6)	# 1-6
    Unknown1084(1)
    setInvincible(1)
    sprite('Action_167_05', 1)	# 7-7
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_167_06', 1)	# 8-8
    Unknown2017(0)
    Unknown2015(40)
    Unknown4004('6566666563745f3530300000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_167_07', 1)	# 9-9
    GFX_0('Shukuchi_WindEff', 100)
    sprite('Action_167_08', 1)	# 10-10
    sprite('Action_167_09', 1)	# 11-11
    sprite('null', 1)	# 12-12
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown2005()
    Unknown1086(22)
    Unknown1007(15000)
    teleportRelativeX(-300000)
    sprite('Action_461_00', 1)	# 13-13
    Unknown7006('uyu203_0', 100, 846559605, 828322608, 0, 0, 100, 846559605, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown2017(1)
    sprite('Action_461_00', 1)	# 14-14
    sprite('Action_461_01', 1)	# 15-15
    physicsYImpulse(1200)
    sprite('Action_461_02', 1)	# 16-16
    physicsYImpulse(35000)
    setGravity(3500)
    Unknown4004('6566666563745f3530360000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1072(75000)
    teleportRelativeX(-80000)
    Unknown1007(150000)
    Unknown35()
    SFX_0('001_airbackdash_0')
    sprite('Action_461_03', 2)	# 17-18	 **attackbox here**
    sprite('Action_461_04', 8)	# 19-26	 **attackbox here**
    physicsXImpulse(36000)
    sprite('Action_461_05', 3)	# 27-29
    Unknown1019(150)
    Unknown2034(1)
    Unknown2017(0)
    Unknown2015(-1)
    sprite('Action_461_06', 1)	# 30-30
    SFX_3('SE_DrawnSword')
    sprite('Action_461_07', 3)	# 31-33
    GFX_0('SlashFinishSP_AtkCol', -1)
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 10)
    sprite('Action_461_08', 4)	# 34-37
    sprite('Action_461_09', 4)	# 38-41
    label(5)
    sprite('Action_461_10', 4)	# 42-45
    sprite('Action_461_09', 4)	# 46-49
    gotoLabel(5)
    label(10)
    sprite('Action_461_19', 3)	# 50-52
    Unknown23073()
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    Unknown18009(1)
    Unknown1084(1)
    sprite('Action_461_20', 10)	# 53-62
    sprite('Action_461_21', 10)	# 63-72
    Unknown23183('0000000000000000000000000000000000000000000000000000000000000000250000000200000002000000')
    SFX_1('uyu203_2')
    SFX_3('SE_SheatheSword')
    if SLOT_2:
        GFX_0('SlashFinishSP_AddAtk', 100)
        GFX_0('Yae_Release', 100)
        Unknown14083(1)
    setInvincible(0)
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_461_22', 7)	# 73-79
    Unknown18009(0)
    sprite('Action_461_23', 4)	# 80-83
    sprite('Action_461_24', 6)	# 84-89
    Unknown19(102, 2, 4)
    Unknown2006()
    ExitState()
    label(101)
    sprite('Action_461_22', 5)	# 90-94
    Unknown18009(0)
    sprite('Action_461_23', 2)	# 95-96
    label(102)
    sprite('Action_461_24', 4)	# 97-100
    Unknown2006()
    sprite('Action_418_00', 3)	# 101-103
    sprite('Action_418_01', 3)	# 104-106
    sprite('Action_418_02', 2)	# 107-108

@State
def AirSlashA():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('SlashAtk')
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(58000)
        AirPushbackY(18000)
        Unknown9178(1)
        WallbounceReboundTime(1)
        Unknown1017()
        Unknown1022()
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_478_00', 3)	# 1-3
    sprite('Action_478_01', 2)	# 4-5
    Unknown1084(1)
    sprite('Action_478_02', 3)	# 6-8
    label(100)
    sprite('Action_478_03', 4)	# 9-12
    Unknown1084(1)
    sprite('Action_478_04', 2)	# 13-14
    SLOT_5 = (SLOT_5 + (-1))
    Unknown7006('uyu200_0', 100, 846559605, 828321840, 0, 0, 100, 846559605, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_478_05', 2)	# 15-16
    callSubroutine('SlashHasei_Input')
    sprite('Action_478_07', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('AirSlashA_Blade', 100)
    sprite('Action_478_10', 16)	# 19-34
    Recovery()
    if SLOT_2:
        callSubroutine('SlashHasei_Timing')
    if (not SLOT_7):
        if SLOT_58:
            if SLOT_57:
                enterState('AirSlashFinish')
    if SLOT_7:
        if SLOT_58:
            if SLOT_57:
                enterState('AirSlashFinishSP')
    sprite('Action_478_11', 4)	# 35-38	 **attackbox here**
    callSubroutine('SlashHasei_Clear')
    sprite('Action_478_12', 3)	# 39-41	 **attackbox here**
    sprite('Action_478_12', 1)	# 42-42	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(60)
    YAccel(60)
    setGravity(1600)
    if SLOT_62:
        SLOT_4 = 1
        Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
        Unknown36(1)
        Unknown1007(150000)
        Unknown35()
    sprite('Action_478_13', 6)	# 43-48	 **attackbox here**
    sprite('Action_478_14', 6)	# 49-54
    loopRest()
    SFX_3('SE_SheatheSword')
    Unknown19(101, 2, 4)
    label(0)
    sprite('Action_421_03', 5)	# 55-59
    Unknown19(101, 2, 4)
    sprite('Action_421_04', 5)	# 60-64
    gotoLabel(0)
    ExitState()
    label(101)
    sprite('Action_423_00', 2)	# 65-66
    sprite('Action_423_01', 2)	# 67-68
    sprite('Action_423_02', 2)	# 69-70
    sprite('Action_423_03', 2)	# 71-72
    sprite('Action_423_04', 2)	# 73-74
    label(102)
    sprite('Action_022_00', 3)	# 75-77
    sprite('Action_022_01', 3)	# 78-80
    loopRest()
    gotoLabel(102)

@State
def AirSlashB():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('SlashAtk')
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackY(32000)
        Unknown1017()
        Unknown1022()
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_477_00', 3)	# 1-3
    sprite('Action_477_01', 2)	# 4-5
    Unknown1084(1)
    sprite('Action_477_02', 3)	# 6-8
    label(100)
    sprite('Action_477_03', 4)	# 9-12
    Unknown1084(1)
    sprite('Action_477_04', 2)	# 13-14	 **attackbox here**
    SLOT_5 = (SLOT_5 + (-1))
    Unknown7006('uyu208_1', 100, 846559605, 845100848, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_477_05', 2)	# 15-16	 **attackbox here**
    callSubroutine('SlashHasei_Input')
    sprite('Action_477_07', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('AirSlashC_Blade', 100)
    sprite('Action_478_10', 16)	# 19-34
    Recovery()
    if SLOT_2:
        callSubroutine('SlashHasei_Timing')
    if (not SLOT_7):
        if SLOT_58:
            if SLOT_57:
                enterState('AirSlashFinish')
    if SLOT_7:
        if SLOT_58:
            if SLOT_57:
                enterState('AirSlashFinishSP')
    sprite('Action_477_11', 4)	# 35-38	 **attackbox here**
    callSubroutine('SlashHasei_Clear')
    sprite('Action_477_12', 3)	# 39-41	 **attackbox here**
    sprite('Action_477_12', 1)	# 42-42	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(60)
    YAccel(60)
    setGravity(1600)
    if SLOT_62:
        SLOT_4 = 1
        Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
        Unknown36(1)
        Unknown1007(150000)
        Unknown35()
    sprite('Action_477_13', 6)	# 43-48	 **attackbox here**
    sprite('Action_477_14', 6)	# 49-54
    SFX_3('SE_SheatheSword')
    Unknown19(101, 2, 4)
    label(0)
    sprite('Action_421_03', 5)	# 55-59
    Unknown19(101, 2, 4)
    sprite('Action_421_04', 5)	# 60-64
    gotoLabel(0)
    ExitState()
    label(101)
    sprite('Action_423_00', 2)	# 65-66
    sprite('Action_423_01', 2)	# 67-68
    sprite('Action_423_02', 2)	# 69-70
    sprite('Action_423_03', 2)	# 71-72
    sprite('Action_423_04', 2)	# 73-74
    label(102)
    sprite('Action_022_00', 3)	# 75-77
    sprite('Action_022_01', 3)	# 78-80
    loopRest()
    gotoLabel(102)

@State
def AirSlashC():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('SlashAtk')
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown1017()
        Unknown1022()
        Damage(2200)
        AirPushbackX(58000)
        AirPushbackY(18000)
        PushbackX(30400)
        Unknown9178(1)
        WallbounceReboundTime(1)
        Unknown11091(10)
        Unknown30065(0)
        Unknown11001(8, 8, 16)
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_478_00', 3)	# 1-3
    sprite('Action_478_01', 2)	# 4-5
    Unknown1084(1)
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_478_02', 3)	# 6-8
    label(100)
    sprite('Action_478_03', 3)	# 9-11
    sprite('Action_478_03', 1)	# 12-12
    if SLOT_56:
        Unknown23125('')
        Unknown2058(-5000)
    Unknown1084(1)
    sprite('Action_478_04', 2)	# 13-14
    SLOT_5 = (SLOT_5 + (-1))
    Unknown7006('uyu200_0', 100, 846559605, 828321840, 0, 0, 100, 846559605, 828323888, 0, 0, 100, 846559605, 845100848, 0, 0, 100)
    sprite('Action_478_05', 2)	# 15-16
    callSubroutine('SlashHasei_Input')
    sprite('Action_478_07ex02', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('AirSlashEx_Blade', 100)
    sprite('Action_478_10', 16)	# 19-34
    Recovery()
    if SLOT_2:
        callSubroutine('SlashHasei_Timing')
    if (not SLOT_7):
        if SLOT_58:
            if SLOT_57:
                enterState('AirSlashFinish')
    if SLOT_7:
        if SLOT_58:
            if SLOT_57:
                enterState('AirSlashFinishSP')
    sprite('Action_478_11', 4)	# 35-38	 **attackbox here**
    callSubroutine('SlashHasei_Clear')
    sprite('Action_478_12', 3)	# 39-41	 **attackbox here**
    sprite('Action_478_12', 1)	# 42-42	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(60)
    YAccel(60)
    setGravity(1600)
    if SLOT_62:
        SLOT_4 = 1
        Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
        Unknown36(1)
        Unknown1007(150000)
        Unknown35()
    sprite('Action_478_13', 6)	# 43-48	 **attackbox here**
    sprite('Action_478_14', 6)	# 49-54
    SFX_3('SE_SheatheSword')
    Unknown19(101, 2, 4)
    label(0)
    sprite('Action_421_03', 5)	# 55-59
    Unknown19(101, 2, 4)
    sprite('Action_421_04', 5)	# 60-64
    gotoLabel(0)
    ExitState()
    label(101)
    sprite('Action_423_00', 2)	# 65-66
    sprite('Action_423_01', 2)	# 67-68
    sprite('Action_423_02', 2)	# 69-70
    sprite('Action_423_03', 2)	# 71-72
    sprite('Action_423_04', 2)	# 73-74
    label(102)
    sprite('Action_022_00', 3)	# 75-77
    sprite('Action_022_01', 3)	# 78-80
    loopRest()
    gotoLabel(102)

@State
def AirSlashFinish():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)
        Unknown30068(1)
        callSubroutine('SlashHoldToKamae')
        SLOT_60 = 0
        clearUponHandler(2)

        def upon_LANDING():
            sendToLabel(30)
    sprite('Action_479_14', 6)	# 1-6
    setInvincible(1)
    Unknown1084(1)
    setGravity(0)
    sprite('Action_479_15', 5)	# 7-11	 **attackbox here**
    sprite('Action_479_16', 5)	# 12-16	 **attackbox here**
    Unknown7006('uyu301_0', 100, 863336821, 828322096, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_479_17', 12)	# 17-28	 **attackbox here**
    SFX_3('SE_SheatheSword')
    GFX_0('UltimateAirRush_Release', 100)
    GFX_0('Slash_AddAtk', 100)
    setInvincible(0)
    sprite('Action_479_18', 4)	# 29-32
    sprite('Action_421_00', 10)	# 33-42
    sprite('Action_421_00', 6)	# 43-48
    Unknown1043()
    sprite('Action_421_01', 4)	# 49-52
    sprite('Action_421_02', 4)	# 53-56
    label(25)
    sprite('Action_421_03', 5)	# 57-61
    sprite('Action_421_04', 5)	# 62-66
    gotoLabel(25)
    label(30)
    sprite('Action_422_00', 4)	# 67-70
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_422_00', 8)	# 71-78
    Unknown19(101, 2, 4)
    ExitState()
    label(101)
    sprite('Action_418_00', 3)	# 79-81
    sprite('Action_418_01', 3)	# 82-84
    sprite('Action_418_02', 2)	# 85-86

@State
def AirSlashFinishSP():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AttackP2(90)
        Unknown11063(1)
        Unknown30068(1)
        callSubroutine('SlashHoldToKamae')
        SLOT_60 = 0
        Hitstop(10)
        AirPushbackX(30000)
        Unknown30055('d0dd06001e0000001e000000')
        Unknown30056('a08601001e0000001e000000')
        Unknown11056(2)
        Unknown23073()
        Unknown11068(1)
        Unknown14083(0)
        Unknown11044(1)
        Unknown11069('SlashFinishSP_AtkCol')

        def upon_43():
            if (SLOT_48 == 1000):
                Unknown23073()
                Unknown2038(1)
    sprite('Action_180_04', 6)	# 1-6
    Unknown1084(1)
    setInvincible(1)
    sprite('Action_180_05', 1)	# 7-7
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_180_06', 1)	# 8-8
    Unknown2017(0)
    Unknown2015(40)
    Unknown4004('6566666563745f3530300000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_180_07', 1)	# 9-9
    GFX_0('Shukuchi_WindEff', 100)
    sprite('Action_180_08', 1)	# 10-10
    sprite('Action_180_09', 1)	# 11-11
    sprite('null', 1)	# 12-12
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown2005()
    Unknown1086(22)
    Unknown1007(15000)
    teleportRelativeX(-300000)
    sprite('Action_461_00', 1)	# 13-13
    Unknown7006('uyu203_0', 100, 846559605, 828322608, 0, 0, 100, 846559605, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown2017(1)
    sprite('Action_461_00', 1)	# 14-14
    sprite('Action_461_01', 1)	# 15-15
    physicsYImpulse(1200)
    sprite('Action_461_02', 1)	# 16-16
    physicsYImpulse(35000)
    setGravity(3500)
    Unknown4004('6566666563745f3530360000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1072(75000)
    teleportRelativeX(-80000)
    Unknown1007(150000)
    Unknown35()
    SFX_0('001_airbackdash_0')
    sprite('Action_461_03', 2)	# 17-18	 **attackbox here**
    sprite('Action_461_04', 8)	# 19-26	 **attackbox here**
    physicsXImpulse(36000)
    sprite('Action_461_05', 3)	# 27-29
    Unknown1019(150)
    Unknown2034(1)
    Unknown2017(0)
    Unknown2015(-1)
    sprite('Action_461_06', 1)	# 30-30
    SFX_3('SE_DrawnSword')
    sprite('Action_461_07', 3)	# 31-33
    GFX_0('SlashFinishSP_AtkCol', -1)
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 10)
    sprite('Action_461_08', 4)	# 34-37
    sprite('Action_461_09', 4)	# 38-41
    label(5)
    sprite('Action_461_10', 4)	# 42-45
    sprite('Action_461_09', 4)	# 46-49
    gotoLabel(5)
    label(10)
    sprite('Action_461_19', 3)	# 50-52
    Unknown23073()
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    Unknown18009(1)
    Unknown1084(1)
    sprite('Action_461_20', 10)	# 53-62
    sprite('Action_461_21', 10)	# 63-72
    Unknown23183('0000000000000000000000000000000000000000000000000000000000000000250000000200000002000000')
    SFX_1('uyu203_2')
    SFX_3('SE_SheatheSword')
    if SLOT_2:
        GFX_0('SlashFinishSP_AddAtk', 100)
        GFX_0('Yae_Release', 100)
        Unknown14083(1)
    setInvincible(0)
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_461_22', 7)	# 73-79
    Unknown18009(0)
    sprite('Action_461_23', 4)	# 80-83
    sprite('Action_461_24', 6)	# 84-89
    Unknown2006()
    Unknown19(102, 2, 4)
    ExitState()
    label(101)
    sprite('Action_461_22', 5)	# 90-94
    Unknown18009(0)
    sprite('Action_461_23', 2)	# 95-96
    label(102)
    sprite('Action_461_24', 4)	# 97-100
    Unknown2006()
    sprite('Action_418_00', 3)	# 101-103
    sprite('Action_418_01', 3)	# 104-106
    sprite('Action_418_02', 2)	# 107-108

@Subroutine
def ShukuchiInit():
    Unknown11063(1)
    Unknown2061(1)
    if SLOT_4:
        SLOT_56 = 1
    if SLOT_60:
        SLOT_56 = 1
        Unknown30068(1)
    SLOT_61 = 0
    SLOT_62 = 0
    Unknown23145('SlashA')
    SLOT_52 = (SLOT_52 + SLOT_0)
    Unknown23145('SlashB')
    SLOT_52 = (SLOT_52 + SLOT_0)
    Unknown23145('SlashC')
    SLOT_52 = (SLOT_52 + SLOT_0)
    Unknown23145('AirSlashA')
    SLOT_52 = (SLOT_52 + SLOT_0)
    Unknown23145('AirSlashB')
    SLOT_52 = (SLOT_52 + SLOT_0)
    Unknown23145('AirSlashC')
    SLOT_52 = (SLOT_52 + SLOT_0)

    def upon_8():
        if SLOT_37:
            if SLOT_51:
                enterState('Shukuchi_End_Front')
            else:
                enterState('Shukuchi_End_Back')
        elif SLOT_51:
            enterState('Shukuchi_End_FrontAir')
        else:
            enterState('Shukuchi_End_BackAir')

@State
def ShukuchiA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('ShukuchiInit')
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_165_00', 4)	# 1-4
    sprite('Action_165_01', 5)	# 5-9
    sprite('Action_165_02', 5)	# 10-14
    sprite('Action_165_03', 5)	# 15-19
    label(100)
    sprite('Action_165_04', 3)	# 20-22
    Unknown1084(1)
    sprite('Action_165_05', 1)	# 23-23
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_165_06', 1)	# 24-24
    setInvincible(1)
    Unknown2017(0)
    Unknown4004('6566666563745f3530300000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_165_07', 1)	# 25-25
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('Action_165_08', 1)	# 26-26
    sprite('Action_165_09', 1)	# 27-27
    sprite('null', 15)	# 28-42
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-500000)
    SLOT_51 = SLOT_38
    Unknown2006()
    Unknown47('09000000020000003300000002000000260000000200000033000000')
    sprite('null', 1)	# 43-43

@State
def ShukuchiB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('ShukuchiInit')
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_166_00', 4)	# 1-4
    sprite('Action_166_01', 5)	# 5-9
    sprite('Action_166_02', 5)	# 10-14
    sprite('Action_166_03', 5)	# 15-19
    label(100)
    sprite('Action_166_04', 3)	# 20-22
    Unknown1084(1)
    sprite('Action_166_05', 1)	# 23-23
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_166_06', 1)	# 24-24
    setInvincible(1)
    Unknown2017(0)
    Unknown4004('6566666563745f3530300000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_166_07', 1)	# 25-25
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('Action_166_08', 1)	# 26-26
    sprite('Action_166_09', 1)	# 27-27
    sprite('null', 11)	# 28-38
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown2017(0)
    Unknown1086(22)
    teleportRelativeY(0)
    if (SLOT_25 <= 60000):
        teleportRelativeX(-60000)
    else:
        teleportRelativeX(350000)
    SLOT_51 = SLOT_38
    Unknown2006()
    Unknown47('09000000020000003300000002000000260000000200000033000000')
    sprite('null', 1)	# 39-39

@State
def ShukuchiC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('ShukuchiInit')
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_167_00', 4)	# 1-4
    sprite('Action_167_01', 5)	# 5-9
    sprite('Action_167_02', 5)	# 10-14
    sprite('Action_167_03', 5)	# 15-19
    label(100)
    sprite('Action_167_04', 3)	# 20-22
    Unknown1084(1)
    sprite('Action_167_05', 1)	# 23-23
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_167_06', 1)	# 24-24
    setInvincible(1)
    Unknown2017(0)
    Unknown4004('6566666563745f3530300000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_167_07', 1)	# 25-25
    GFX_0('Shukuchi_WindEff', 100)
    sprite('Action_167_08', 1)	# 26-26
    sprite('Action_167_09', 1)	# 27-27
    sprite('null', 11)	# 28-38
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown1086(22)
    Unknown1007(150000)
    if (SLOT_5 >= 3):
        teleportRelativeY(270000)
    if (SLOT_25 <= 60000):
        teleportRelativeX(-60000)
    else:
        teleportRelativeX(350000)
    SLOT_51 = SLOT_38
    Unknown2006()
    Unknown47('09000000020000003300000002000000260000000200000033000000')
    sprite('null', 1)	# 39-39

@State
def AirShukuchiA():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('ShukuchiInit')
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_180_00', 3)	# 1-3
    sprite('Action_180_00', 2)	# 4-5
    Unknown1084(1)
    sprite('Action_180_01', 5)	# 6-10
    sprite('Action_180_02', 5)	# 11-15
    sprite('Action_180_03', 5)	# 16-20
    label(100)
    sprite('Action_180_04', 3)	# 21-23
    Unknown1084(1)
    sprite('Action_180_05', 1)	# 24-24
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_180_06', 1)	# 25-25
    setInvincible(1)
    Unknown2017(0)
    Unknown4004('6566666563745f3530310000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_180_07', 1)	# 26-26
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown1007(85000)
    Unknown35()
    sprite('Action_180_08', 1)	# 27-27
    sprite('Action_180_09', 1)	# 28-28
    sprite('null', 11)	# 29-39
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown1086(22)
    Unknown1007(150000)
    if (SLOT_23 <= 270000):
        teleportRelativeY(270000)
    teleportRelativeX(-500000)
    SLOT_51 = SLOT_38
    Unknown2006()
    Unknown47('09000000020000003300000002000000260000000200000033000000')
    sprite('null', 1)	# 40-40

@State
def AirShukuchiB():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('ShukuchiInit')
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_181_00', 3)	# 1-3
    sprite('Action_181_00', 2)	# 4-5
    Unknown1084(1)
    sprite('Action_181_01', 5)	# 6-10
    sprite('Action_181_02', 5)	# 11-15
    sprite('Action_181_03', 5)	# 16-20
    label(100)
    sprite('Action_181_04', 3)	# 21-23
    Unknown1084(1)
    sprite('Action_181_05', 1)	# 24-24
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_181_06', 1)	# 25-25
    setInvincible(1)
    Unknown2017(0)
    Unknown4004('6566666563745f3530310000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_181_07', 1)	# 26-26
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown1007(85000)
    Unknown35()
    sprite('Action_181_08', 1)	# 27-27
    sprite('Action_181_09', 1)	# 28-28
    sprite('null', 11)	# 29-39
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown1086(22)
    Unknown1007(150000)
    if (SLOT_23 <= 300000):
        teleportRelativeY(300000)
    if (SLOT_25 <= 60000):
        teleportRelativeX(-60000)
    else:
        teleportRelativeX(350000)
    SLOT_51 = SLOT_38
    Unknown2006()
    Unknown47('09000000020000003300000002000000260000000200000033000000')
    sprite('null', 1)	# 40-40

@State
def AirShukuchiC():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('ShukuchiInit')
    if SLOT_56:
        _gotolabel(100)
    sprite('Action_182_00', 3)	# 1-3
    sprite('Action_182_00', 2)	# 4-5
    Unknown1084(1)
    sprite('Action_182_01', 5)	# 6-10
    sprite('Action_182_02', 5)	# 11-15
    sprite('Action_182_03', 5)	# 16-20
    label(100)
    sprite('Action_182_04', 3)	# 21-23
    Unknown1084(1)
    sprite('Action_182_05', 1)	# 24-24
    Unknown7006('uyu205_0', 100, 846559605, 828323120, 0, 0, 100, 846559605, 845100336, 0, 0, 100, 846559605, 811546416, 0, 0, 100)
    sprite('Action_182_06', 1)	# 25-25
    setInvincible(1)
    Unknown2017(0)
    Unknown4004('6566666563745f3530310000000000000000000000000000000000000000000064000000')
    Unknown4004('416972446173684645666600000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(1500)
    Unknown1007(200000)
    Unknown35()
    sprite('Action_182_07', 1)	# 26-26
    GFX_0('Shukuchi_WindEff', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown1007(85000)
    Unknown35()
    sprite('Action_182_08', 1)	# 27-27
    sprite('Action_182_09', 1)	# 28-28
    sprite('null', 11)	# 29-39
    SFX_3('SE_ClothesSwing2')
    Unknown2034(0)
    Unknown1086(22)
    teleportRelativeY(0)
    if (SLOT_25 <= 60000):
        teleportRelativeX(-60000)
    else:
        teleportRelativeX(350000)
    SLOT_51 = SLOT_38
    Unknown2006()
    Unknown47('09000000020000003300000002000000260000000200000033000000')
    sprite('null', 1)	# 40-40

@State
def Shukuchi_End_Front():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2017(0)
        Unknown4004('6566666563745f3530320000000000000000000000000000000000000000000064000000')
        GFX_0('Shukuchi_WindEff', 100)
        Unknown36(1)
        teleportRelativeX(-200000)
        Unknown35()
        Unknown30068(1)
    sprite('null', 1)	# 1-1
    sprite('Action_165_13', 1)	# 2-2
    sprite('Action_165_14', 1)	# 3-3
    sprite('Action_165_15', 1)	# 4-4
    sprite('Action_165_16', 1)	# 5-5
    sprite('Action_165_17', 3)	# 6-8
    if SLOT_5:
        if (SLOT_5 <= 2):
            Unknown2006()
            if Unknown23145('ShukuchiA'):
                enterState('SlashA')
            if Unknown23145('ShukuchiB'):
                enterState('SlashB')
            if Unknown23145('AirShukuchiC'):
                enterState('SlashB')
    sprite('Action_165_18', 3)	# 9-11
    Unknown2017(1)
    SLOT_4 = 0
    sprite('Action_165_19', 1)	# 12-12
    sprite('Action_418_00', 6)	# 13-18
    sprite('Action_418_01', 6)	# 19-24
    sprite('Action_418_02', 4)	# 25-28

@State
def Shukuchi_End_Back():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2017(0)
        Unknown4004('6566666563745f3530320000000000000000000000000000000000000000000064000000')
        GFX_0('Shukuchi_WindEff', 100)
        Unknown36(1)
        Unknown2005()
        teleportRelativeX(-200000)
        Unknown35()
        Unknown30068(1)
    sprite('null', 1)	# 1-1
    sprite('Action_165_22', 1)	# 2-2
    sprite('Action_165_23', 1)	# 3-3
    sprite('Action_165_24', 1)	# 4-4
    sprite('Action_165_25', 1)	# 5-5
    sprite('Action_165_17', 3)	# 6-8
    if SLOT_5:
        if (SLOT_5 <= 2):
            Unknown2006()
            if Unknown23145('ShukuchiA'):
                enterState('SlashA')
            if Unknown23145('ShukuchiB'):
                enterState('SlashB')
            if Unknown23145('AirShukuchiC'):
                enterState('SlashB')
    sprite('Action_165_18', 3)	# 9-11
    Unknown2017(1)
    SLOT_4 = 0
    sprite('Action_165_19', 1)	# 12-12
    sprite('Action_418_00', 6)	# 13-18
    sprite('Action_418_01', 6)	# 19-24
    sprite('Action_418_02', 4)	# 25-28

@State
def Shukuchi_End_FrontAir():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2061(1)
        Unknown2017(0)
        GFX_0('Shukuchi_WindEff', 100)
        Unknown36(1)
        teleportRelativeX(-200000)
        Unknown35()
        Unknown30068(1)
    sprite('null', 1)	# 1-1
    sprite('Action_167_13', 1)	# 2-2
    sprite('Action_167_14', 1)	# 3-3
    sprite('Action_167_15', 1)	# 4-4
    sprite('Action_167_16', 1)	# 5-5
    physicsXImpulse(10000)
    setGravity(1000)
    sprite('Action_167_17', 3)	# 6-8
    if SLOT_5:
        if (SLOT_5 <= 2):
            Unknown2006()
            if Unknown23145('AirShukuchiA'):
                enterState('AirSlashB')
            if Unknown23145('AirShukuchiB'):
                enterState('AirSlashB')
            if Unknown23145('ShukuchiC'):
                enterState('AirSlashB')
    sprite('Action_167_18', 1)	# 9-9
    Unknown2017(1)
    SLOT_4 = 0
    sprite('Action_423_00', 3)	# 10-12
    sprite('Action_423_01', 3)	# 13-15
    sprite('Action_423_02', 3)	# 16-18
    sprite('Action_423_03', 3)	# 19-21

@State
def Shukuchi_End_BackAir():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown2061(1)
        Unknown2017(0)
        GFX_0('Shukuchi_WindEff', 100)
        Unknown36(1)
        Unknown2005()
        teleportRelativeX(-200000)
        Unknown35()
        Unknown30068(1)
    sprite('null', 1)	# 1-1
    sprite('Action_167_21', 1)	# 2-2
    sprite('Action_167_22', 1)	# 3-3
    sprite('Action_167_23', 1)	# 4-4
    sprite('Action_167_24', 1)	# 5-5
    physicsXImpulse(-10000)
    setGravity(1000)
    sprite('Action_167_17', 3)	# 6-8
    if SLOT_5:
        if (SLOT_5 <= 2):
            Unknown2006()
            if Unknown23145('AirShukuchiA'):
                Unknown23159('SlashWarpHaseiA')
                enterState('AirSlashB')
            if Unknown23145('AirShukuchiB'):
                Unknown23159('SlashWarpHaseiB')
                enterState('AirSlashB')
            if Unknown23145('ShukuchiC'):
                Unknown23159('SlashWarpHaseiC')
                enterState('AirSlashB')
    sprite('Action_167_18', 1)	# 9-9
    Unknown2017(1)
    SLOT_4 = 0
    sprite('Action_423_00', 3)	# 10-12
    sprite('Action_423_01', 3)	# 13-15
    sprite('Action_423_02', 3)	# 16-18
    sprite('Action_423_03', 3)	# 19-21

@Subroutine
def DS_KamaeAction():
    if SLOT_4:
        SLOT_56 = 1
    if SLOT_7:
        SLOT_56 = 1
    if (SLOT_5 < 3):
        if SLOT_60:
            SLOT_56 = 1
    Unknown23145('SlashFinish')
    SLOT_56 = (SLOT_56 + SLOT_0)
    Unknown23145('SlashFinishSP')
    SLOT_56 = (SLOT_56 + SLOT_0)
    Unknown23145('AirSlashFinish')
    SLOT_56 = (SLOT_56 + SLOT_0)
    Unknown23145('AirSlashFinishSP')
    SLOT_56 = (SLOT_56 + SLOT_0)
    SLOT_4 = 0
    SLOT_60 = 0
    SLOT_61 = 0
    SLOT_62 = 0

@State
def UltimateSlash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2000)
        Unknown11091(10)
        Unknown30055('60ae0a003200000000000000')
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        PushbackX(2000)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Hitstop(9)
        Unknown11001(10, 10, 10)
        Unknown2073(1)
        Unknown9154(60)
        Unknown11064(1)
        Unknown11032('804f120000000000ffffffffffffffff')
        setInvincible(1)
        SLOT_59 = 0
        if random_(2, 0, 50):
            SLOT_59 = 1

        def upon_STATE_END():
            SLOT_4 = 0
        callSubroutine('DS_KamaeAction')
    if SLOT_56:
        _gotolabel(0)
    sprite('Action_215_00', 7)	# 1-7
    Unknown1084(1)
    Unknown23024(1)
    Unknown2036(35, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_215_01', 4)	# 8-11
    sprite('Action_215_02', 4)	# 12-15
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('Action_215_02', 4)	# 16-19
    Unknown1084(1)
    Unknown23024(1)
    Unknown2036(20, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    label(1)
    sprite('Action_215_03', 34)	# 20-53
    if SLOT_59:
        SFX_1('uyu250_0')
    else:
        SFX_1('uyu250_1')
    sprite('Action_215_04', 1)	# 54-54
    SFX_3('SE_DrawnSword')
    sprite('Action_215_05', 3)	# 55-57	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade1', 100)

    def upon_78():
        SLOT_58 = 1
        Unknown13024(0)
        GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_06', 3)	# 58-60
    sprite('Action_215_06', 3)	# 61-63
    if (not SLOT_58):
        setInvincible(0)
    sprite('Action_215_07', 4)	# 64-67
    GFX_0('IW_Zanzo', 100)
    sprite('Action_215_08', 4)	# 68-71
    sprite('Action_215_09', 5)	# 72-76
    sprite('Action_215_10', 1)	# 77-77
    SFX_3('SE_DrawnSword')
    sprite('Action_215_11', 2)	# 78-79	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade2', 100)
    Unknown30055('000000000000000000000000')
    clearUponHandler(78)

    def upon_78():
        Unknown13024(0)
        if SLOT_158:
            Unknown11069('UltimateSlashExe')
            Unknown2038(1)
            Unknown23024(2)
            GFX_0('IW_Kanji_Tsubomi', 100)
            GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_12', 1)	# 80-80	 **attackbox here**
    clearUponHandler(78)
    Unknown23027()
    loopRest()
    if SLOT_2:
        if SLOT_158:
            enterState('UltimateSlashExe')
    sprite('Action_215_13', 4)	# 81-84
    setInvincible(0)
    sprite('Action_215_14', 4)	# 85-88
    sprite('Action_215_15', 4)	# 89-92
    sprite('Action_215_16', 6)	# 93-98
    sprite('Action_215_17', 7)	# 99-105
    SFX_3('SE_SheatheSword')
    sprite('Action_215_17', 2)	# 106-107
    sprite('Action_215_19', 10)	# 108-117	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(100000)
    Unknown2017(0)
    Unknown1028(-4000)
    Unknown11069('')
    Hitstop(2)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9154(15)
    Unknown9130(16)
    Unknown9142(100)
    Unknown11064(0)
    Unknown2073(0)

    def upon_77():
        Unknown1019(75)
        Unknown1034(75)
    sprite('Action_215_20', 6)	# 118-123
    Unknown2017(1)
    sprite('Action_215_21', 6)	# 124-129
    sprite('Action_215_22', 4)	# 130-133
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown1028(-1000)
    sprite('Action_215_23', 4)	# 134-137
    sprite('Action_215_24', 2)	# 138-139
    GFX_0('IW_Ralease', 100)
    sprite('Action_215_25', 5)	# 140-144
    Unknown1084(1)
    sprite('Action_215_26', 5)	# 145-149
    sprite('Action_215_27', 6)	# 150-155
    SFX_3('SE_SheatheSword')
    sprite('Action_215_28', 20)	# 156-175
    sprite('Action_215_29', 5)	# 176-180
    sprite('Action_215_30', 5)	# 181-185

@State
def UltimateSlashExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(0)
        Hitstop(2)
        Unknown11091(24)
        AttackP2(100)
        PushbackX(0)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown9154(120)
        Unknown11064(1)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11069('UltimateSlashExe')
        Unknown23022(1)
        Unknown2034(0)
        Unknown2053(0)
        Unknown2017(0)
        Unknown13024(0)

        def upon_STATE_END():
            Unknown23022(0)
            Unknown2034(1)
            Unknown2053(1)

        def upon_3():
            if (not SLOT_158):
                Unknown26('IWExe_Camera')
                Unknown2034(1)
                Unknown2053(1)
    sprite('Action_215_12', 4)	# 1-4	 **attackbox here**
    RefreshMultihit()
    Unknown11001(0, 90, 90)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_215_13', 5)	# 5-9
    sprite('Action_215_14', 5)	# 10-14
    sprite('Action_215_15', 5)	# 15-19
    GFX_0('IWExe_Camera', 100)
    sprite('Action_215_16', 7)	# 20-26
    sprite('Action_215_17', 9)	# 27-35
    sprite('Action_216_00', 1)	# 36-36
    Unknown1086(22)
    GFX_0('IWExe_Blade1', 100)
    GFX_0('IWExe_Kimono', 100)
    GFX_0('IWExe_Tanmono', 100)
    physicsXImpulse(32000)
    Unknown1028(-1700)
    if SLOT_59:
        SFX_1('uyu251_0')
    sprite('Action_216_01', 1)	# 37-37
    sprite('Action_216_02', 1)	# 38-38
    sprite('Action_216_03', 4)	# 39-42
    sprite('Action_216_04', 4)	# 43-46
    GFX_0('IW_Kanji_Moe', 100)
    sprite('Action_216_03', 4)	# 47-50
    sprite('Action_216_04', 4)	# 51-54
    sprite('Action_216_05', 6)	# 55-60
    Unknown1084(1)
    sprite('Action_216_06', 8)	# 61-68	 **attackbox here**
    sprite('Action_216_07', 9)	# 69-77	 **attackbox here**
    sprite('Action_216_08', 9)	# 78-86	 **attackbox here**
    sprite('Action_216_09', 8)	# 87-94	 **attackbox here**
    GFX_0('IW_Kanji_Saku', 100)
    sprite('Action_216_10', 6)	# 95-100	 **attackbox here**
    sprite('Action_216_11', 4)	# 101-104	 **attackbox here**
    sprite('Action_216_12', 3)	# 105-107	 **attackbox here**
    physicsXImpulse(-100000)
    Unknown1028(4000)
    sprite('Action_216_13', 3)	# 108-110
    SFX_3('SE_DrawnSword')
    GFX_0('IWExe_Blade2', 100)
    Unknown1019(3)
    Unknown1028(0)
    physicsYImpulse(27500)
    setGravity(1500)
    sprite('Action_216_14', 3)	# 111-113
    sprite('Action_216_15', 3)	# 114-116	 **attackbox here**
    GFX_0('IW_Kanji_Chiru', 100)
    RefreshMultihit()
    Damage(6500)
    AirUntechableTime(120)
    Unknown9310(1)
    AirPushbackX(1000)
    AirPushbackY(52000)
    YImpluseBeforeWallbounce(1200)
    Unknown11001(0, -25, -25)
    Hitstop(27)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')
    Unknown11072(1, 150000, 500000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    Unknown11064(0)
    Unknown11056(2)
    GFX_0('IW_Sakura_MatomeFinish', 100)
    Unknown23029(1, 5000, 1)
    if (not SLOT_59):
        SFX_1('uyu251_1')
    sprite('Action_216_16', 1)	# 117-117
    Unknown2017(1)
    sprite('Action_216_17', 1)	# 118-118
    sprite('Action_216_18', 1)	# 119-119
    sprite('Action_216_19', 4)	# 120-123
    sprite('Action_216_20', 8)	# 124-131
    sprite('Action_216_21', 5)	# 132-136
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_216_22', 4)	# 137-140
    sprite('Action_216_23', 4)	# 141-144
    label(0)
    sprite('Action_216_24', 4)	# 145-148
    sprite('Action_216_25', 4)	# 149-152
    gotoLabel(0)
    label(1)
    sprite('Action_216_26', 2)	# 153-154	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_216_27', 3)	# 155-157	 **attackbox here**
    sprite('Action_216_28', 3)	# 158-160	 **attackbox here**
    sprite('Action_216_29', 3)	# 161-163	 **attackbox here**
    sprite('Action_216_30ex01', 4)	# 164-167	 **attackbox here**
    sprite('Action_216_31ex01', 10)	# 168-177	 **attackbox here**
    GFX_0('KimonoDmy', 100)
    sprite('Action_216_26', 3)	# 178-180	 **attackbox here**
    sprite('Action_216_33', 2)	# 181-182	 **attackbox here**
    sprite('Action_216_34', 4)	# 183-186
    sprite('Action_216_35', 15)	# 187-201
    Unknown13024(1)
    GFX_0('IW_Release', 100)
    SFX_3('SE_SheatheSword')
    sprite('Action_216_36', 5)	# 202-206
    loopRest()
    label(100)
    sprite('Action_216_37', 5)	# 207-211
    sprite('Action_216_38', 4)	# 212-215
    loopRest()
    ExitState()

@State
def UltimateSlashOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(2000)
        Unknown11091(10)
        Unknown30055('60ae0a003200000000000000')
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        PushbackX(15000)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Hitstop(9)
        Unknown11001(10, 10, 10)
        Unknown2073(1)
        Unknown9154(60)
        Unknown11064(1)
        Unknown11032('804f120000000000ffffffffffffffff')
        setInvincible(1)
        SLOT_59 = 0
        if random_(2, 0, 50):
            SLOT_59 = 1

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            SLOT_4 = 0
            if (not SLOT_54):
                Unknown20007(0)
        callSubroutine('DS_KamaeAction')
    if SLOT_56:
        _gotolabel(0)
    sprite('Action_215_00', 7)	# 1-7
    Unknown1084(1)
    Unknown23024(1)
    Unknown2036(35, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_215_01', 4)	# 8-11
    sprite('Action_215_02', 4)	# 12-15
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('Action_215_02', 4)	# 16-19
    Unknown1084(1)
    Unknown23024(1)
    Unknown2036(20, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    label(1)
    sprite('Action_215_03', 34)	# 20-53
    if SLOT_59:
        SFX_1('uyu250_0')
    else:
        SFX_1('uyu250_1')
    sprite('Action_215_04', 1)	# 54-54
    SFX_3('SE_DrawnSword')
    sprite('Action_215_05', 3)	# 55-57	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade1', 100)

    def upon_78():
        SLOT_58 = 1
        Unknown13024(0)
        GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_06', 3)	# 58-60
    sprite('Action_215_06', 3)	# 61-63
    sprite('Action_215_07', 4)	# 64-67
    GFX_0('IW_Zanzo', 100)
    sprite('Action_215_08', 4)	# 68-71
    sprite('Action_215_09', 5)	# 72-76
    sprite('Action_215_10', 1)	# 77-77
    SFX_3('SE_DrawnSword')
    sprite('Action_215_11', 2)	# 78-79	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade2', 100)
    Unknown30055('000000000000000000000000')
    Unknown11069('UltimateSlashOD')
    clearUponHandler(78)

    def upon_78():
        Unknown13024(0)
        Unknown2038(1)
        Unknown23024(2)
        GFX_0('IW_Kanji_Tsubomi', 100)
        GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_12', 1)	# 80-80	 **attackbox here**
    clearUponHandler(78)
    Unknown23027()
    sprite('Action_215_13', 3)	# 81-83
    sprite('Action_215_14', 3)	# 84-86
    sprite('Action_215_15', 3)	# 87-89
    sprite('Action_215_16', 5)	# 90-94
    sprite('Action_215_17', 7)	# 95-101
    SFX_3('SE_SheatheSword')
    sprite('Action_215_17', 2)	# 102-103
    loopRest()
    if SLOT_2:
        _gotolabel(10)
    sprite('Action_215_19', 10)	# 104-113	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(100000)
    Unknown2017(0)
    Unknown1028(-4000)
    Unknown11069('')
    Hitstop(2)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9154(15)
    Unknown9130(16)
    Unknown9142(100)
    Unknown11064(0)
    Unknown2073(0)

    def upon_77():
        Unknown1019(75)
        Unknown1034(75)
    sprite('Action_215_20', 6)	# 114-119
    Unknown2017(1)
    sprite('Action_215_21', 6)	# 120-125
    sprite('Action_215_22', 4)	# 126-129
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown1028(-1000)
    sprite('Action_215_23', 4)	# 130-133
    sprite('Action_215_24', 2)	# 134-135
    GFX_0('IW_Ralease', 100)
    sprite('Action_215_25', 5)	# 136-140
    Unknown1084(1)
    sprite('Action_215_26', 5)	# 141-145
    sprite('Action_215_27', 6)	# 146-151
    SFX_3('SE_SheatheSword')
    sprite('Action_215_28', 20)	# 152-171
    sprite('Action_215_29', 5)	# 172-176
    sprite('Action_215_30', 5)	# 177-181
    ExitState()
    label(10)
    sprite('Action_215_19', 4)	# 182-185	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(270000)
    Unknown2017(0)
    Unknown1028(-4000)
    Unknown3004(-40)
    Damage(400)
    Hitstop(2)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9154(15)
    Unknown9130(16)
    Unknown9142(100)
    Unknown30048(1)

    def upon_78():
        Unknown23024(2)
        Unknown13024(0)
        Unknown20007(1)
        if (not SLOT_2):
            if SLOT_158:
                Unknown2038(1)
                GFX_0('IW_Kanji_Tsubomi', 100)
                GFX_0('IW_Sakura_Matome', 100)
        if SLOT_54:
            if SLOT_158:
                Unknown11069('UltimateSlashODExe')
    sprite('Action_215_19', 4)	# 186-189	 **attackbox here**
    Unknown2005()
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(180000)
    Unknown1028(-4000)
    sprite('Action_215_19', 4)	# 190-193	 **attackbox here**
    Unknown2005()
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(180000)
    Unknown1028(-4000)
    sprite('Action_215_19', 4)	# 194-197	 **attackbox here**
    SLOT_54 = 1
    Unknown2005()
    RefreshMultihit()
    physicsXImpulse(165000)
    Unknown1028(-4000)
    loopRest()
    if SLOT_2:
        if SLOT_158:
            Unknown3001(255)
            Unknown3004(0)
            Unknown2005()
            enterState('UltimateSlashODExe')
        else:
            Unknown3004(38)
    else:
        Unknown3004(38)
    sprite('Action_215_22', 2)	# 198-199
    clearUponHandler(78)
    setInvincible(0)
    Unknown1084(1)
    sprite('Action_215_19', 2)	# 200-201	 **attackbox here**
    Unknown2005()
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(360000)
    Unknown1028(-8000)
    Unknown11064(0)
    Unknown11069('')
    sprite('Action_215_22', 4)	# 202-205
    Unknown2017(1)
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown1028(-1000)
    sprite('Action_215_23', 4)	# 206-209
    sprite('Action_215_24', 2)	# 210-211
    SFX_3('SE_SheatheSword')
    GFX_0('IW_Ralease', 100)
    sprite('Action_215_25', 5)	# 212-216
    Unknown1084(1)
    sprite('Action_215_26', 5)	# 217-221
    sprite('Action_215_27', 6)	# 222-227
    sprite('Action_215_28', 30)	# 228-257
    sprite('Action_215_29', 5)	# 258-262
    sprite('Action_215_30', 5)	# 263-267

@State
def UltimateSlashODExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2200)
        Hitstop(2)
        Unknown11091(20)
        AttackP2(100)
        PushbackX(0)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown9154(120)
        Unknown11064(1)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11069('UltimateSlashODExe')
        Unknown20007(1)
        Unknown23022(1)
        Unknown2034(0)
        Unknown2053(0)
        Unknown2017(0)
        Unknown13024(0)

        def upon_STATE_END():
            Unknown23022(0)
            Unknown2034(1)
            Unknown2053(1)

        def upon_3():
            if (not SLOT_158):
                Unknown26('IWExe_Camera')
                Unknown2034(1)
                Unknown2053(1)
    sprite('Action_215_14ex01', 4)	# 1-4	 **attackbox here**
    RefreshMultihit()
    Unknown11001(0, 90, 90)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_215_15', 5)	# 5-9
    Unknown20007(0)
    GFX_0('IWExe_Camera', 100)
    sprite('Action_215_16', 7)	# 10-16
    sprite('Action_215_17', 9)	# 17-25
    SFX_3('SE_SheatheSword')
    sprite('Action_216_00', 1)	# 26-26
    Unknown1086(22)
    GFX_0('IWExe_Blade1', 100)
    GFX_0('IWExe_Kimono', 100)
    GFX_0('IWExe_Tanmono', 100)
    physicsXImpulse(32000)
    Unknown1028(-1700)
    if SLOT_59:
        SFX_1('uyu251_0')
    sprite('Action_216_01', 1)	# 27-27
    sprite('Action_216_02', 1)	# 28-28
    sprite('Action_216_03', 4)	# 29-32
    sprite('Action_216_04', 4)	# 33-36
    GFX_0('IW_Kanji_Moe', 100)
    sprite('Action_216_03', 4)	# 37-40
    sprite('Action_216_04', 4)	# 41-44
    sprite('Action_216_05', 6)	# 45-50
    Unknown1084(1)
    sprite('Action_216_06', 8)	# 51-58	 **attackbox here**
    sprite('Action_216_07', 9)	# 59-67	 **attackbox here**
    sprite('Action_216_08', 9)	# 68-76	 **attackbox here**
    sprite('Action_216_09', 8)	# 77-84	 **attackbox here**
    GFX_0('IW_Kanji_Saku', 100)
    sprite('Action_216_10', 6)	# 85-90	 **attackbox here**
    sprite('Action_216_11', 4)	# 91-94	 **attackbox here**
    sprite('Action_216_12', 3)	# 95-97	 **attackbox here**
    physicsXImpulse(-100000)
    Unknown1028(4000)
    sprite('Action_216_13', 3)	# 98-100
    SFX_3('SE_DrawnSword')
    GFX_0('IWExe_Blade2', 100)
    Unknown1019(3)
    Unknown1028(0)
    physicsYImpulse(27500)
    setGravity(1500)
    sprite('Action_216_14', 3)	# 101-103
    sprite('Action_216_15', 3)	# 104-106	 **attackbox here**
    GFX_0('IW_Kanji_Chiru', 100)
    RefreshMultihit()
    AirUntechableTime(120)
    Unknown9310(30)
    AirPushbackX(-1000)
    AirPushbackY(52000)
    YImpluseBeforeWallbounce(1200)
    Unknown11001(0, -25, -25)
    Hitstop(27)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('IWOD_AddAtk')
    Unknown11072(1, 150000, 500000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    GFX_0('IW_Sakura_MatomeFinish', 100)
    Unknown23029(1, 5000, 1)
    if (not SLOT_59):
        SFX_1('uyu251_1')
    sprite('Action_216_16', 1)	# 107-107
    Unknown2017(1)
    sprite('Action_216_17', 1)	# 108-108
    sprite('Action_216_18', 1)	# 109-109
    sprite('Action_216_19', 4)	# 110-113
    sprite('Action_216_20', 8)	# 114-121
    sprite('Action_216_21', 5)	# 122-126
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_216_22', 4)	# 127-130
    sprite('Action_216_23', 4)	# 131-134
    label(0)
    sprite('Action_216_24', 4)	# 135-138
    sprite('Action_216_25', 4)	# 139-142
    gotoLabel(0)
    label(1)
    sprite('Action_216_26', 2)	# 143-144	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_216_27', 3)	# 145-147	 **attackbox here**
    sprite('Action_216_28', 3)	# 148-150	 **attackbox here**
    sprite('Action_216_29', 3)	# 151-153	 **attackbox here**
    sprite('Action_216_30', 4)	# 154-157	 **attackbox here**
    sprite('Action_216_30ex01', 4)	# 158-161	 **attackbox here**
    sprite('Action_216_31ex01', 10)	# 162-171	 **attackbox here**
    GFX_0('KimonoDmy', 100)
    sprite('Action_216_26', 3)	# 172-174	 **attackbox here**
    sprite('Action_216_33', 2)	# 175-176	 **attackbox here**
    sprite('Action_216_34', 4)	# 177-180
    sprite('Action_216_35', 34)	# 181-214
    GFX_0('IWOD_AddAtk', 100)
    GFX_0('IW_Release', 100)
    SFX_3('SE_SheatheSword')
    SFX_1('uyu252')
    sprite('Action_216_36', 5)	# 215-219
    Unknown13024(1)
    loopRest()
    label(100)
    sprite('Action_216_37', 5)	# 220-224
    sprite('Action_216_38', 4)	# 225-228
    loopRest()
    ExitState()

@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(590)
        Hitstop(1)
        Unknown11057(800)
        Unknown11091(15)
        AttackP1(80)
        AttackP2(96)
        AirPushbackY(3500)
        AirPushbackY(8000)
        Unknown30055('40600a005000000000000000')
        Unknown30056('a08601005000000000000000')
        YImpluseBeforeWallbounce(1200)
        PushbackX(5000)
        Unknown9016(1)
        AirUntechableTime(60)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        setInvincible(1)
        if random_(2, 0, 50):
            SLOT_51 = 1
        callSubroutine('DS_KamaeAction')

        def upon_78():
            SLOT_57 = 1
            setInvincible(0)
            Unknown22008(45)
    if SLOT_56:
        _gotolabel(0)
    sprite('Action_262_00', 5)	# 1-5
    Unknown23024(1)
    Unknown2036(35, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 4)	# 37-40
    sprite('Action_439_00', 1)	# 41-41
    sprite('Action_439_01', 1)	# 42-42
    sprite('Action_439_02', 1)	# 43-43
    sprite('Action_439_03', 2)	# 44-45
    sprite('Action_439_04', 2)	# 46-47
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('Action_229_01', 6)	# 48-53
    sprite('Action_229_02', 6)	# 54-59
    Unknown23024(1)
    Unknown2036(35, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_229_03', 6)	# 60-65
    GFX_0('FF_Start', 100)
    sprite('Action_229_04', 22)	# 66-87
    label(1)
    sprite('Action_439_05', 2)	# 88-89
    callSubroutine('SlashHoldToKamae')
    sprite('Action_439_06', 2)	# 90-91
    sprite('Action_439_07', 1)	# 92-92
    if SLOT_51:
        SFX_1('uyu254_0')
    sprite('Action_439_08', 1)	# 93-93	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('SlashB_Blade', 100)
    RefreshMultihit()
    sprite('Action_439_08', 1)	# 94-94	 **attackbox here**
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    RefreshMultihit()
    sprite('Action_439_08', 1)	# 95-95	 **attackbox here**
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    RefreshMultihit()
    sprite('Action_439_10', 1)	# 96-96
    sprite('Action_439_11', 1)	# 97-97
    if (not SLOT_57):
        setInvincible(0)
    sprite('Action_439_06', 1)	# 98-98
    sprite('Action_439_07', 1)	# 99-99
    sprite('Action_439_08', 1)	# 100-100	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_08', 1)	# 101-101	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_10', 1)	# 102-102
    sprite('Action_439_11', 1)	# 103-103
    if (not SLOT_51):
        SFX_1('uyu254_1')
    sprite('Action_439_06', 1)	# 104-104
    Unknown2038(1)
    sprite('Action_439_07', 1)	# 105-105
    sprite('Action_439_08', 1)	# 106-106	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('Action_439_08', 1)	# 107-107	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_10', 1)	# 108-108
    sprite('Action_439_11', 1)	# 109-109
    sprite('Action_439_06', 1)	# 110-110
    sprite('Action_439_07', 1)	# 111-111
    sprite('Action_439_08', 1)	# 112-112	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_08', 1)	# 113-113	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('Action_439_10', 1)	# 114-114
    sprite('Action_439_11', 1)	# 115-115
    sprite('Action_439_06', 1)	# 116-116
    sprite('Action_439_07', 1)	# 117-117
    sprite('Action_439_08', 1)	# 118-118	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_08', 1)	# 119-119	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_10', 1)	# 120-120
    sprite('Action_439_11', 1)	# 121-121
    sprite('Action_439_06', 1)	# 122-122
    sprite('Action_439_07', 1)	# 123-123
    sprite('Action_439_08', 2)	# 124-125	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    Hitstop(3)
    Unknown11001(0, 15, 15)
    AirPushbackX(8000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(2000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)

    def upon_78():
        clearUponHandler(78)
        sendToLabel(20)
    sprite('Action_439_10', 6)	# 126-131
    sprite('Action_439_11', 5)	# 132-136
    sprite('Action_439_12', 5)	# 137-141	 **attackbox here**
    loopRest()
    Unknown19(100, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_439_13', 8)	# 142-149	 **attackbox here**
    sprite('Action_439_14', 8)	# 150-157
    sprite('Action_439_15', 8)	# 158-165
    sprite('Action_439_16', 6)	# 166-171
    sprite('Action_439_17', 5)	# 172-176
    sprite('Action_439_18', 3)	# 177-179
    ExitState()
    label(100)
    sprite('Action_439_13', 6)	# 180-185	 **attackbox here**
    sprite('Action_439_14', 6)	# 186-191
    sprite('Action_439_15', 6)	# 192-197
    sprite('Action_439_16', 4)	# 198-201
    SFX_3('SE_SheatheSword')
    sprite('Action_439_17', 3)	# 202-204
    sprite('Action_439_18', 2)	# 205-206
    sprite('Action_418_00', 4)	# 207-210
    sprite('Action_418_01', 4)	# 211-214
    sprite('Action_418_02', 3)	# 215-217
    ExitState()
    label(20)
    sprite('Action_439_20', 9)	# 218-226
    sprite('Action_439_21', 7)	# 227-233	 **attackbox here**
    sprite('Action_439_22', 7)	# 234-240	 **attackbox here**
    sprite('Action_439_23', 6)	# 241-246	 **attackbox here**
    sprite('Action_439_24', 6)	# 247-252
    sprite('Action_439_25', 6)	# 253-258	 **attackbox here**
    StartMultihit()
    SFX_3('SE_SheatheSword')
    GFX_0('UltimateRush_Release', 100)
    GFX_0('UltimateRush_AddAtk', 100)
    sprite('Action_439_26', 4)	# 259-262
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_439_27', 5)	# 263-267
    sprite('Action_439_28', 20)	# 268-287
    sprite('Action_420_00', 4)	# 288-291
    ExitState()
    label(101)
    sprite('Action_439_27', 5)	# 292-296
    sprite('Action_439_28', 12)	# 297-308
    sprite('Action_420_00', 4)	# 309-312
    loopRest()
    sprite('Action_418_00', 3)	# 313-315
    sprite('Action_418_01', 3)	# 316-318
    sprite('Action_418_02', 2)	# 319-320

@State
def UltimateRushOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(370)
        Hitstop(1)
        Unknown11028(30)
        Unknown11057(800)
        Unknown11091(15)
        AttackP1(80)
        AttackP2(98)
        AirPushbackY(3500)
        AirPushbackY(8000)
        Unknown30055('40600a005000000000000000')
        Unknown30056('a08601005000000000000000')
        YImpluseBeforeWallbounce(700)
        PushbackX(5000)
        Unknown9016(1)
        AirUntechableTime(60)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        setInvincible(1)
        if random_(2, 0, 50):
            SLOT_51 = 1
        callSubroutine('DS_KamaeAction')

        def upon_78():
            SLOT_57 = 1
            setInvincible(0)
            Unknown22008(45)
    if SLOT_56:
        _gotolabel(0)
    sprite('Action_262_00', 5)	# 1-5
    Unknown23024(1)
    Unknown2036(35, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 4)	# 37-40
    sprite('Action_439_00', 1)	# 41-41
    sprite('Action_439_01', 1)	# 42-42
    sprite('Action_439_02', 1)	# 43-43
    sprite('Action_439_03', 2)	# 44-45
    sprite('Action_439_04', 2)	# 46-47
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('Action_229_01', 6)	# 48-53
    sprite('Action_229_02', 6)	# 54-59
    Unknown23024(1)
    Unknown2036(35, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_229_03', 6)	# 60-65
    GFX_0('FF_Start', 100)
    sprite('Action_229_04', 22)	# 66-87
    label(1)
    sprite('Action_439_05', 2)	# 88-89
    callSubroutine('SlashHoldToKamae')
    sprite('Action_439_06', 2)	# 90-91
    sprite('Action_439_07', 1)	# 92-92
    if SLOT_51:
        SFX_1('uyu254_0')
    if (not SLOT_51):
        SFX_1('uyu254_1')
    sprite('Action_439_08', 1)	# 93-93	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('SlashB_Blade', 100)
    RefreshMultihit()
    sprite('Action_439_08', 1)	# 94-94	 **attackbox here**
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    RefreshMultihit()
    sprite('Action_439_08', 1)	# 95-95	 **attackbox here**
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    RefreshMultihit()
    sprite('Action_439_10', 1)	# 96-96
    sprite('Action_439_11', 1)	# 97-97
    if (not SLOT_57):
        setInvincible(0)
    sprite('Action_439_06', 1)	# 98-98
    sprite('Action_439_07', 1)	# 99-99
    sprite('Action_439_08', 1)	# 100-100	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_08', 1)	# 101-101	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_10', 1)	# 102-102
    sprite('Action_439_11', 1)	# 103-103
    sprite('Action_439_06', 1)	# 104-104
    Unknown2038(1)
    sprite('Action_439_07', 1)	# 105-105
    sprite('Action_439_08', 1)	# 106-106	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('Action_439_08', 1)	# 107-107	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_10', 1)	# 108-108
    sprite('Action_439_11', 1)	# 109-109
    sprite('Action_439_06', 1)	# 110-110
    sprite('Action_439_07', 1)	# 111-111
    sprite('Action_439_08', 1)	# 112-112	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_08', 1)	# 113-113	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('Action_439_10', 1)	# 114-114
    sprite('Action_439_11', 1)	# 115-115
    sprite('Action_439_06', 1)	# 116-116
    sprite('Action_439_07', 1)	# 117-117
    sprite('Action_439_08', 1)	# 118-118	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_08', 1)	# 119-119	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_10', 1)	# 120-120
    sprite('Action_439_11', 1)	# 121-121
    sprite('Action_439_06', 1)	# 122-122
    sprite('Action_439_07', 1)	# 123-123
    sprite('Action_439_08', 1)	# 124-124	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('Action_439_08', 1)	# 125-125	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_10', 1)	# 126-126
    sprite('Action_439_11', 1)	# 127-127
    sprite('Action_439_06', 1)	# 128-128
    sprite('Action_439_07', 1)	# 129-129
    sprite('Action_439_08', 1)	# 130-130	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_08', 1)	# 131-131	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('Action_439_10', 1)	# 132-132
    sprite('Action_439_11', 1)	# 133-133
    sprite('Action_439_06', 1)	# 134-134
    sprite('Action_439_07', 1)	# 135-135
    sprite('Action_439_08', 1)	# 136-136	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_08', 1)	# 137-137	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_10', 1)	# 138-138
    sprite('Action_439_11', 1)	# 139-139
    sprite('Action_439_06', 1)	# 140-140
    sprite('Action_439_07', 1)	# 141-141
    sprite('Action_439_08', 1)	# 142-142	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('Action_439_08', 1)	# 143-143	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('Action_439_10', 1)	# 144-144
    sprite('Action_439_11', 1)	# 145-145
    sprite('Action_229_00', 3)	# 146-148
    sprite('Action_229_01', 4)	# 149-152
    GFX_0('FF_Start', 100)
    sprite('Action_229_02', 3)	# 153-155
    GFX_0('FF_Sakura3', 100)
    sprite('Action_229_03', 3)	# 156-158
    sprite('Action_420_00', 10)	# 159-168
    sprite('Action_236_00', 1)	# 169-169
    sprite('Action_236_01', 1)	# 170-170
    sprite('Action_236_02', 1)	# 171-171
    sprite('Action_236_03ex01', 2)	# 172-173	 **attackbox here**
    SFX_1('uyu255')
    GFX_0('UltimateRush_Blade2_ODFinish', 100)
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    Damage(900)
    Unknown11028(20)
    Unknown11091(10)
    Hitstop(5)
    Unknown11001(4, 4, 4)
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    AirPushbackX(10000)
    AirPushbackY(28000)
    PushbackX(0)
    YImpluseBeforeWallbounce(2000)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9130(21)
    Unknown9142(100)
    Unknown9132(21)
    Unknown9144(100)
    Unknown11064(0)

    def upon_78():
        clearUponHandler(78)
        SLOT_58 = 1
    sprite('Action_236_03', 1)	# 174-174	 **attackbox here**
    if SLOT_58:
        GFX_0('UltimateRush_Blade2_ODFinish_Ma', 100)
    sprite('Action_236_03', 3)	# 175-177	 **attackbox here**
    Hitstop(2)
    if SLOT_58:
        RefreshMultihit()
        SFX_0('025_cleanhit_slash')
    sprite('Action_236_03', 3)	# 178-180	 **attackbox here**
    if SLOT_58:
        RefreshMultihit()
    sprite('Action_236_03', 2)	# 181-182	 **attackbox here**
    if SLOT_58:
        RefreshMultihit()
    sprite('Action_236_03', 1)	# 183-183	 **attackbox here**
    if SLOT_58:
        sendToLabel(20)
    sprite('Action_439_10', 6)	# 184-189
    sprite('Action_439_11', 5)	# 190-194
    sprite('Action_439_12', 5)	# 195-199	 **attackbox here**
    sprite('Action_439_13', 6)	# 200-205	 **attackbox here**
    sprite('Action_439_14', 6)	# 206-211
    loopRest()
    Unknown19(100, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_439_15', 8)	# 212-219
    SFX_3('SE_SheatheSword')
    sprite('Action_439_16', 6)	# 220-225
    sprite('Action_439_17', 5)	# 226-230
    sprite('Action_439_18', 4)	# 231-234
    ExitState()
    label(100)
    sprite('Action_439_15', 6)	# 235-240
    SFX_3('SE_SheatheSword')
    sprite('Action_439_16', 4)	# 241-244
    sprite('Action_439_17', 3)	# 245-247
    sprite('Action_439_18', 2)	# 248-249
    sprite('Action_418_00', 3)	# 250-252
    sprite('Action_418_01', 3)	# 253-255
    sprite('Action_418_02', 2)	# 256-257
    ExitState()
    label(20)
    sprite('Action_439_20', 12)	# 258-269
    sprite('Action_439_21', 5)	# 270-274	 **attackbox here**
    sprite('Action_439_22', 5)	# 275-279	 **attackbox here**
    sprite('Action_439_23', 4)	# 280-283	 **attackbox here**
    sprite('Action_439_24', 6)	# 284-289
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_439_25', 8)	# 290-297	 **attackbox here**
    SFX_3('SE_SheatheSword')
    GFX_0('UltimateRush_Release', 100)
    sprite('Action_439_26', 6)	# 298-303
    sprite('Action_439_27', 7)	# 304-310
    sprite('Action_439_28', 6)	# 311-316
    ExitState()
    label(101)
    sprite('Action_439_25', 6)	# 317-322	 **attackbox here**
    SFX_3('SE_SheatheSword')
    GFX_0('UltimateRush_Release', 100)
    sprite('Action_439_26', 4)	# 323-326
    sprite('Action_439_27', 5)	# 327-331
    sprite('Action_439_28', 4)	# 332-335
    sprite('Action_418_00', 3)	# 336-338
    sprite('Action_418_01', 3)	# 339-341
    sprite('Action_418_02', 2)	# 342-343

@State
def UltimateAirRush():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(590)
        Hitstop(1)
        Unknown11057(800)
        Unknown11091(15)
        AttackP1(80)
        AttackP2(96)
        AirPushbackY(3500)
        AirPushbackY(8000)
        Unknown30055('40600a003200000000000000')
        Unknown30056('a08601003200000000000000')
        YImpluseBeforeWallbounce(1200)
        PushbackX(5000)
        Unknown9016(1)
        AirUntechableTime(60)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        setInvincible(1)
        if random_(2, 0, 50):
            SLOT_51 = 1
        clearUponHandler(2)

        def upon_LANDING():
            sendToLabel(30)
        callSubroutine('DS_KamaeAction')

        def upon_78():
            SLOT_57 = 1
            setInvincible(0)
            Unknown22008(45)
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    if SLOT_56:
        _gotolabel(0)
    sprite('Action_262_00', 5)	# 1-5
    Unknown23024(1)
    Unknown2036(36, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 4)	# 37-40
    sprite('Action_225_00', 1)	# 41-41
    sprite('Action_225_01', 1)	# 42-42
    sprite('Action_225_02', 1)	# 43-43
    sprite('Action_225_03', 2)	# 44-45
    sprite('Action_225_04', 2)	# 46-47	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('Action_225_01', 6)	# 48-53
    sprite('Action_225_02', 6)	# 54-59
    Unknown23024(1)
    Unknown2036(36, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_225_03', 6)	# 60-65
    GFX_0('FF_Start', 100)
    sprite('Action_225_03', 22)	# 66-87
    label(1)
    sprite('Action_479_04', 3)	# 88-90	 **attackbox here**
    callSubroutine('SlashHoldToKamae')
    sprite('Action_479_05', 2)	# 91-92	 **attackbox here**
    if SLOT_51:
        SFX_1('uyu254_0')
    sprite('Action_479_06ex01', 1)	# 93-93	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('AirSlashB_Blade', 100)
    RefreshMultihit()
    sprite('Action_479_06ex01', 1)	# 94-94	 **attackbox here**
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    RefreshMultihit()
    sprite('Action_479_06ex01', 1)	# 95-95	 **attackbox here**
    GFX_0('UltimateAirRush_Blade2_Pt1', 100)
    RefreshMultihit()
    sprite('Action_479_07', 1)	# 96-96
    sprite('Action_479_08', 1)	# 97-97
    if (not SLOT_57):
        setInvincible(0)
    sprite('Action_479_04', 1)	# 98-98	 **attackbox here**
    sprite('Action_479_05', 1)	# 99-99	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 100-100	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_06ex01', 1)	# 101-101	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_07', 1)	# 102-102
    sprite('Action_479_08', 1)	# 103-103
    if (not SLOT_51):
        SFX_1('uyu254_1')
    sprite('Action_479_04', 1)	# 104-104	 **attackbox here**
    Unknown2038(1)
    sprite('Action_479_05', 1)	# 105-105	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 106-106	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt1', 100)
    sprite('Action_479_06ex01', 1)	# 107-107	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_07', 1)	# 108-108
    sprite('Action_479_08', 1)	# 109-109
    sprite('Action_479_04', 1)	# 110-110	 **attackbox here**
    sprite('Action_479_05', 1)	# 111-111	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 112-112	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_06ex01', 1)	# 113-113	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt1', 100)
    sprite('Action_479_07', 1)	# 114-114
    sprite('Action_479_08', 1)	# 115-115
    sprite('Action_479_04', 1)	# 116-116	 **attackbox here**
    sprite('Action_479_05', 1)	# 117-117	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 118-118	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_06ex01', 1)	# 119-119	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_07', 1)	# 120-120
    sprite('Action_479_08', 1)	# 121-121
    sprite('Action_479_04', 1)	# 122-122	 **attackbox here**
    sprite('Action_479_05', 1)	# 123-123	 **attackbox here**
    sprite('Action_479_06ex01', 2)	# 124-125	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    Hitstop(3)
    Unknown11001(0, 15, 15)
    AirPushbackX(8000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(2000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)

    def upon_78():
        clearUponHandler(78)
        sendToLabel(20)
    sprite('Action_479_07', 6)	# 126-131
    sprite('Action_479_08', 5)	# 132-136
    sprite('Action_479_09', 5)	# 137-141	 **attackbox here**
    sprite('Action_479_10', 6)	# 142-147	 **attackbox here**
    sprite('Action_479_11', 6)	# 148-153	 **attackbox here**
    sprite('Action_479_12', 6)	# 154-159
    SFX_3('SE_SheatheSword')
    physicsYImpulse(10000)
    sprite('Action_421_00', 6)	# 160-165
    YAccel(20)
    sprite('Action_421_01', 6)	# 166-171
    Unknown1043()
    sprite('Action_421_02', 6)	# 172-177
    loopRest()
    gotoLabel(25)
    label(20)
    sprite('Action_479_14', 9)	# 178-186
    sprite('Action_479_15', 7)	# 187-193	 **attackbox here**
    sprite('Action_479_16', 7)	# 194-200	 **attackbox here**
    sprite('Action_479_17', 15)	# 201-215	 **attackbox here**
    StartMultihit()
    SFX_3('SE_SheatheSword')
    GFX_0('UltimateAirRush_Release', 100)
    GFX_0('UltimateRush_AddAtk', 100)
    sprite('Action_479_18', 6)	# 216-221
    physicsYImpulse(10000)
    sprite('Action_421_00', 6)	# 222-227
    YAccel(20)
    sprite('Action_421_01', 6)	# 228-233
    Unknown1043()
    sprite('Action_421_02', 6)	# 234-239
    label(25)
    sprite('Action_421_03', 5)	# 240-244
    sprite('Action_421_04', 5)	# 245-249
    gotoLabel(25)
    label(30)
    sprite('Action_422_00', 4)	# 250-253
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_422_00', 8)	# 254-261
    ExitState()
    label(101)
    sprite('Action_418_00', 3)	# 262-264
    sprite('Action_418_01', 3)	# 265-267
    sprite('Action_418_02', 2)	# 268-269

@State
def UltimateAirRushOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(370)
        Hitstop(1)
        Unknown11028(30)
        Unknown11057(800)
        Unknown11091(15)
        AttackP1(80)
        AttackP2(98)
        AirPushbackY(3500)
        AirPushbackY(9000)
        Unknown30055('40600a003200000000000000')
        Unknown30056('f04902005000000000000000')
        YImpluseBeforeWallbounce(1200)
        PushbackX(5000)
        Unknown9016(1)
        AirUntechableTime(60)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        setInvincible(1)
        if random_(2, 0, 50):
            SLOT_51 = 1
        clearUponHandler(2)

        def upon_LANDING():
            sendToLabel(30)
        callSubroutine('DS_KamaeAction')

        def upon_78():
            SLOT_57 = 1
            setInvincible(0)
            Unknown22008(45)
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    if SLOT_56:
        _gotolabel(0)
    sprite('Action_262_00', 5)	# 1-5
    Unknown23024(1)
    Unknown2036(36, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 4)	# 37-40
    sprite('Action_225_00', 1)	# 41-41
    sprite('Action_225_01', 1)	# 42-42
    sprite('Action_225_02', 1)	# 43-43
    sprite('Action_225_03', 2)	# 44-45
    sprite('Action_225_04', 2)	# 46-47	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('Action_225_01', 6)	# 48-53
    sprite('Action_225_02', 6)	# 54-59
    Unknown23024(1)
    Unknown2036(36, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    SFX_1('uyu253')
    sprite('Action_225_03', 6)	# 60-65
    GFX_0('AirFF_Start', 100)
    sprite('Action_225_03', 22)	# 66-87
    label(1)
    sprite('Action_479_04', 3)	# 88-90	 **attackbox here**
    callSubroutine('SlashHoldToKamae')
    sprite('Action_479_05', 2)	# 91-92	 **attackbox here**
    if SLOT_51:
        SFX_1('uyu254_0')
    sprite('Action_479_06ex01', 1)	# 93-93	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('AirSlashB_Blade', 100)
    RefreshMultihit()
    sprite('Action_479_06ex01', 1)	# 94-94	 **attackbox here**
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    RefreshMultihit()
    sprite('Action_479_06ex01', 1)	# 95-95	 **attackbox here**
    GFX_0('UltimateAirRush_Blade2_Pt1', 100)
    RefreshMultihit()
    sprite('Action_479_07', 1)	# 96-96
    sprite('Action_479_08', 1)	# 97-97
    if (not SLOT_57):
        setInvincible(0)
    sprite('Action_479_04', 1)	# 98-98	 **attackbox here**
    sprite('Action_479_05', 1)	# 99-99	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 100-100	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_06ex01', 1)	# 101-101	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_07', 1)	# 102-102
    sprite('Action_479_08', 1)	# 103-103
    if (not SLOT_51):
        SFX_1('uyu254_1')
    sprite('Action_479_04', 1)	# 104-104	 **attackbox here**
    Unknown2038(1)
    sprite('Action_479_05', 1)	# 105-105	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 106-106	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt1', 100)
    sprite('Action_479_06ex01', 1)	# 107-107	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_07', 1)	# 108-108
    sprite('Action_479_08', 1)	# 109-109
    sprite('Action_479_04', 1)	# 110-110	 **attackbox here**
    sprite('Action_479_05', 1)	# 111-111	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 112-112	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_06ex01', 1)	# 113-113	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt1', 100)
    sprite('Action_479_07', 1)	# 114-114
    sprite('Action_479_08', 1)	# 115-115
    sprite('Action_479_04', 1)	# 116-116	 **attackbox here**
    sprite('Action_479_05', 1)	# 117-117	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 118-118	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_06ex01', 1)	# 119-119	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_07', 1)	# 120-120
    sprite('Action_479_08', 1)	# 121-121
    sprite('Action_479_04', 1)	# 122-122	 **attackbox here**
    sprite('Action_479_05', 1)	# 123-123	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 124-124	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_06ex01', 1)	# 125-125	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_07', 1)	# 126-126
    sprite('Action_479_08', 1)	# 127-127
    sprite('Action_479_04', 1)	# 128-128	 **attackbox here**
    sprite('Action_479_05', 1)	# 129-129	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 130-130	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_06ex01', 1)	# 131-131	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_07', 1)	# 132-132
    sprite('Action_479_08', 1)	# 133-133
    sprite('Action_479_04', 1)	# 134-134	 **attackbox here**
    sprite('Action_479_05', 1)	# 135-135	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 136-136	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_06ex01', 1)	# 137-137	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_07', 1)	# 138-138
    sprite('Action_479_08', 1)	# 139-139
    sprite('Action_479_04', 1)	# 140-140	 **attackbox here**
    sprite('Action_479_05', 1)	# 141-141	 **attackbox here**
    sprite('Action_479_06ex01', 1)	# 142-142	 **attackbox here**
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt3', 100)
    sprite('Action_479_06ex01', 1)	# 143-143	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateAirRush_Blade2_Pt2', 100)
    sprite('Action_479_07', 1)	# 144-144
    sprite('Action_479_08', 1)	# 145-145
    sprite('Action_225_09', 3)	# 146-148	 **attackbox here**
    sprite('Action_225_10', 3)	# 149-151	 **attackbox here**
    GFX_0('AirFF_Start', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(65000)
    Unknown35()
    sprite('Action_225_11', 3)	# 152-154
    GFX_0('FF_Sakura3', 100)
    sprite('Action_421_00', 8)	# 155-162
    sprite('Action_225_02', 2)	# 163-164
    sprite('Action_225_03', 2)	# 165-166
    sprite('Action_225_04', 2)	# 167-168	 **attackbox here**
    sprite('Action_225_05', 2)	# 169-170	 **attackbox here**
    sprite('Action_225_06', 2)	# 171-172	 **attackbox here**
    SFX_1('uyu255')
    GFX_0('UltimateAirRush_ODFinish', 100)
    SFX_3('SE_DrawnSword')
    RefreshMultihit()
    Damage(900)
    Unknown11028(20)
    Unknown11091(10)
    Hitstop(5)
    Unknown11001(4, 4, 4)
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    AirPushbackX(10000)
    AirPushbackY(28000)
    PushbackX(0)
    YImpluseBeforeWallbounce(2000)
    Unknown9130(16)
    Unknown9142(100)
    Unknown11064(0)

    def upon_78():
        clearUponHandler(78)
        SLOT_58 = 1
    sprite('Action_225_06', 1)	# 173-173	 **attackbox here**
    if SLOT_58:
        GFX_0('UltimateAirRushODFinish_Matome', 100)
    sprite('Action_225_06', 3)	# 174-176	 **attackbox here**
    Hitstop(2)
    if SLOT_58:
        RefreshMultihit()
        SFX_0('025_cleanhit_slash')
    sprite('Action_225_06', 3)	# 177-179	 **attackbox here**
    if SLOT_58:
        RefreshMultihit()
    sprite('Action_225_06', 2)	# 180-181	 **attackbox here**
    if SLOT_58:
        RefreshMultihit()
    sprite('Action_225_06', 1)	# 182-182	 **attackbox here**
    if SLOT_58:
        sendToLabel(20)
    sprite('Action_225_07', 6)	# 183-188
    sprite('Action_225_08', 5)	# 189-193	 **attackbox here**
    sprite('Action_225_09', 5)	# 194-198	 **attackbox here**
    sprite('Action_225_10', 6)	# 199-204	 **attackbox here**
    sprite('Action_225_11', 6)	# 205-210
    SFX_3('SE_SheatheSword')
    physicsYImpulse(10000)
    sprite('Action_421_00', 4)	# 211-214
    YAccel(20)
    sprite('Action_421_01', 4)	# 215-218
    Unknown1043()
    sprite('Action_421_02', 4)	# 219-222
    gotoLabel(25)
    label(20)
    sprite('Action_479_14', 6)	# 223-228
    sprite('Action_479_15', 5)	# 229-233	 **attackbox here**
    sprite('Action_479_16', 5)	# 234-238	 **attackbox here**
    sprite('Action_479_17', 8)	# 239-246	 **attackbox here**
    SFX_3('SE_SheatheSword')
    GFX_0('UltimateAirRush_Release', 100)
    sprite('Action_479_18', 4)	# 247-250
    physicsYImpulse(10000)
    sprite('Action_421_00', 4)	# 251-254
    YAccel(20)
    sprite('Action_421_01', 4)	# 255-258
    Unknown1043()
    sprite('Action_421_02', 4)	# 259-262
    label(25)
    sprite('Action_421_03', 5)	# 263-267
    sprite('Action_421_04', 5)	# 268-272
    gotoLabel(25)
    label(30)
    sprite('Action_422_00', 4)	# 273-276
    loopRest()
    Unknown19(101, 2, 62)
    SLOT_4 = 1
    Unknown4004('6566666563745f3530340000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(150000)
    Unknown35()
    sprite('Action_422_00', 8)	# 277-284
    ExitState()
    label(101)
    sprite('Action_418_00', 3)	# 285-287
    SLOT_4 = 0
    sprite('Action_418_01', 3)	# 288-290
    sprite('Action_418_02', 2)	# 291-292

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(0)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11091(100)
        PushbackX(19800)
        Hitstop(3)
        AirPushbackX(0)
        AirPushbackY(250)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(9999)
        Unknown11056(2)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        SLOT_60 = 0
        SLOT_61 = 0
        SLOT_62 = 0

        def upon_80():
            physicsXImpulse(115200)
            sendToLabel(10)

        def upon_78():
            setInvincible(1)
            Unknown2038(1)
            Unknown23157(1)
            Unknown23088(1, 1)
            Unknown23084(1)
            sendToLabel(666)
            Unknown36(22)
            teleportRelativeY(10)
            Unknown35()

        def upon_43():
            if (SLOT_48 == 8001):
                GFX_0('IWEXIST_BG_Back', 100)
                GFX_0('IWEXIST_BG_Front', 100)
                Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
                Unknown3026(-13619152)
                Unknown36(22)
                Unknown1021(450)
                Unknown3026(-13619152)
                Unknown35()
                Unknown21015('495745584953545f43616d657261000000000000000000000000000000000000421f000000000000')
            if (SLOT_48 == 8003):
                SFX_1('uyu291')
            if (SLOT_48 == 8004):
                sendToLabel(670)
            if (SLOT_48 == 8005):
                sendToLabel(672)

        def upon_STATE_END():
            SLOT_4 = 0
            Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_535_00', 6)	# 1-6
    setInvincible(1)
    Unknown1084(1)
    Unknown2036(75, -1, 1)
    Unknown23147()
    GFX_0('UYU_CutIn', 100)
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    sprite('Action_535_01', 6)	# 7-12
    SFX_1('uyu292')
    sprite('Action_535_02', 6)	# 13-18
    sprite('Action_535_03', 6)	# 19-24
    sprite('Action_535_04', 6)	# 25-30
    sprite('Action_535_05', 6)	# 31-36
    sprite('Action_535_06', 50)	# 37-86
    sprite('Action_535_07', 5)	# 87-91
    Unknown2017(0)
    GFX_0('IW_Blade3', 100)
    Unknown3004(-50)
    sprite('Action_215_19', 2)	# 92-93	 **attackbox here**
    SFX_3('SE_DrawnSword')
    physicsXImpulse(360000)
    sprite('Action_215_19', 2)	# 94-95	 **attackbox here**
    Unknown1019(80)
    sprite('Action_215_19', 2)	# 96-97	 **attackbox here**
    Unknown1019(80)
    label(10)
    sprite('Action_215_19', 2)	# 98-99	 **attackbox here**
    setInvincible(0)
    Unknown23027()
    Unknown3004(31)
    sprite('Action_215_20', 6)	# 100-105
    Unknown2017(1)
    Unknown1084(1)
    Unknown1045(35000)
    sprite('Action_215_21', 6)	# 106-111
    sprite('Action_215_22', 4)	# 112-115
    sprite('Action_215_23', 4)	# 116-119
    sprite('Action_215_24', 2)	# 120-121
    GFX_0('IW_Ralease', 100)
    sprite('Action_215_25', 5)	# 122-126
    Unknown1084(1)
    sprite('Action_215_26', 5)	# 127-131
    sprite('Action_215_27', 6)	# 132-137
    SFX_3('SE_SheatheSword')
    sprite('Action_215_28', 20)	# 138-157
    sprite('Action_215_29', 5)	# 158-162
    sprite('Action_215_30', 5)	# 163-167
    ExitState()
    label(666)
    sprite('keep', 10)	# 168-177
    Unknown1084(1)
    Unknown3001(0)
    Unknown2053(0)
    Unknown2034(0)
    GFX_0('IWEXIST_Camera', 100)
    sprite('keep', 1)	# 178-178
    Unknown1086(22)
    teleportRelativeX(150000)
    Unknown1007(150000)
    GFX_0('IWEXIST_Kimono', 100)
    sprite('Action_535_10', 2)	# 179-180
    Unknown3001(255)
    Unknown3004(0)
    physicsXImpulse(12000)
    physicsYImpulse(12000)
    setGravity(1500)
    Unknown3038(0)
    sprite('Action_535_11', 5)	# 181-185	 **attackbox here**
    sendToLabelUpon(2, 668)
    label(667)
    sprite('Action_535_12', 5)	# 186-190	 **attackbox here**
    sprite('Action_535_13', 5)	# 191-195	 **attackbox here**
    sprite('Action_535_14', 5)	# 196-200	 **attackbox here**
    loopRest()
    gotoLabel(667)
    label(668)
    sprite('Action_535_15', 5)	# 201-205
    Unknown1019(30)
    sprite('Action_535_16', 5)	# 206-210
    sprite('Action_535_17', 5)	# 211-215
    Unknown1084(1)
    Unknown1045(3000)
    sprite('Action_535_18', 6)	# 216-221
    sprite('Action_535_19', 5)	# 222-226
    sprite('Action_535_20', 5)	# 227-231
    sprite('Action_535_21', 5)	# 232-236
    SFX_1('uyu293')
    label(669)
    sprite('Action_535_22', 5)	# 237-241	 **attackbox here**
    sprite('Action_535_23', 5)	# 242-246	 **attackbox here**
    sprite('Action_535_24', 5)	# 247-251	 **attackbox here**
    sprite('Action_535_25', 5)	# 252-256	 **attackbox here**
    gotoLabel(669)
    label(670)
    sprite('Action_536_05', 4)	# 257-260
    sprite('Action_536_06', 3)	# 261-263
    sprite('Action_536_07', 1)	# 264-264
    physicsXImpulse(-80000)
    sprite('Action_536_08', 1)	# 265-265
    sprite('null', 5)	# 266-270
    GFX_0('IWEX_BlackOut', 100)
    GFX_0('IWEXIST_SlushEff', 100)
    GFX_0('IWEX_IaiDmyAtk', 100)
    sprite('null', 19)	# 271-289
    Unknown1084(1)
    sprite('Action_536_10', 4)	# 290-293	 **attackbox here**
    GFX_0('IWEX_Sakura_MatomeFinish', 100)
    Unknown1045(-48000)
    label(671)
    sprite('Action_536_11', 4)	# 294-297	 **attackbox here**
    sprite('Action_536_12', 4)	# 298-301	 **attackbox here**
    sprite('Action_536_13', 4)	# 302-305	 **attackbox here**
    sprite('Action_536_14', 4)	# 306-309	 **attackbox here**
    gotoLabel(671)
    label(672)
    sprite('Action_537_00', 120)	# 310-429
    Unknown26('IWEXIST_Camera')
    Unknown23024(0)
    Unknown3026(-1)
    Unknown26('IWEX_SakuraParticle')
    Unknown26('IWEX_SakuraParticle2')
    Unknown26('IWEXIST_BG_Front')
    Unknown26('IWEXIST_BG_Back')
    Unknown1084(1)
    Unknown1000(-260000)
    Unknown36(22)
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown35()
    sprite('Action_537_00', 20)	# 430-449
    SFX_3('SE_SheatheSword')
    sprite('Action_537_01', 6)	# 450-455
    sprite('Action_537_02', 7)	# 456-462
    sprite('Action_537_03', 3)	# 463-465
    sprite('Action_537_04', 4)	# 466-469

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
    sprite('Action_000_00', 3)	# 1-3	 **attackbox here**
sprite('Action_000_00', 3)	# 4-6	 **attackbox here**

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_000_49', 5)	# 1-5
    sprite('Action_000_50', 6)	# 6-11
    sprite('Action_000_51', 6)	# 12-17
    sprite('Action_000_52', 3)	# 18-20	 **attackbox here**
    sprite('Action_000_53', 7)	# 21-27	 **attackbox here**
    sprite('Action_000_54', 5)	# 28-32	 **attackbox here**
    sprite('Action_000_55', 8)	# 33-40	 **attackbox here**
    sprite('Action_000_56', 7)	# 41-47	 **attackbox here**
    sprite('Action_000_53', 7)	# 48-54	 **attackbox here**
    sprite('Action_000_54', 5)	# 55-59	 **attackbox here**
    sprite('Action_000_55', 8)	# 60-67	 **attackbox here**
    sprite('Action_000_56', 7)	# 68-74	 **attackbox here**
    sprite('Action_000_57', 6)	# 75-80
    sprite('Action_000_58', 6)	# 81-86
    sprite('Action_000_59', 30)	# 87-116

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)
    sprite('null', 7)	# 1-7
    sprite('Action_007_03', 3)	# 8-10	 **attackbox here**
    Unknown23027()
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-100000)
    Unknown1007(2400000)
    physicsXImpulse(3333)
    physicsYImpulse(-80000)
    setGravity(0)
    sprite('Action_007_03', 5)	# 11-15	 **attackbox here**
    sprite('Action_007_04', 5)	# 16-20	 **attackbox here**
    sprite('Action_007_03', 5)	# 21-25	 **attackbox here**
    sprite('Action_007_04', 5)	# 26-30	 **attackbox here**
    sprite('Action_007_03', 5)	# 31-35	 **attackbox here**
    sprite('Action_007_04', 5)	# 36-40	 **attackbox here**

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(9)
    label(1)
    sprite('Action_007_03', 5)	# 41-45	 **attackbox here**
    sprite('Action_007_04', 5)	# 46-50	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_403_13', 13)	# 51-63
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_403_14', 5)	# 64-68
    sprite('Action_403_15', 3)	# 69-71
    sprite('Action_403_16', 2)	# 72-73

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_02', 2)	# 1-2
    sprite('Action_045_03', 2)	# 3-4
    sprite('Action_045_02', 2)	# 5-6
    sprite('Action_045_03', 3)	# 7-9
    sprite('Action_045_02', 3)	# 10-12
    sprite('Action_045_03', 3)	# 13-15
    sprite('Action_045_02', 3)	# 16-18
    sprite('Action_045_08', 7)	# 19-25
    sprite('Action_045_09', 4)	# 26-29

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
    sprite('Action_046_01', 2)	# 4-5
    sprite('Action_046_02', 4)	# 6-9
    sprite('Action_046_03', 3)	# 10-12
    loopRest()
    label(0)
    sprite('Action_046_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_04', 3)	# 16-18
    sprite('Action_046_05', 3)	# 19-21

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_046_01', 3)	# 1-3
    sprite('Action_046_02', 3)	# 4-6
    sprite('Action_046_03', 3)	# 7-9
    sprite('Action_046_04', 3)	# 10-12
    sprite('Action_046_03', 3)	# 13-15
    sprite('Action_046_04', 3)	# 16-18
    sprite('Action_046_03', 3)	# 19-21
    sprite('Action_046_04', 3)	# 22-24
    sprite('Action_046_03', 3)	# 25-27
    sprite('Action_046_04', 3)	# 28-30
    sprite('Action_046_03', 30)	# 31-60

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
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP1(70)
        AttackP2(85)
        Hitstop(10)
        Unknown11001(5, 5, 7)
        AirUntechableTime(60)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(75000)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(500)
        PushbackX(19800)
        WallbounceReboundTime(1)
        Unknown9016(1)
        Unknown11042(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_438_00', 1)	# 1-1
    sprite('Action_438_01', 1)	# 2-2
    sprite('Action_438_02', 2)	# 3-4
    sprite('Action_438_03', 2)	# 5-6
    sprite('Action_438_04', 2)	# 7-8
    sprite('Action_438_05', 4)	# 9-12
    sprite('Action_438_06', 2)	# 13-14
    Unknown7006('uyu201_0', 100, 846559605, 828322096, 0, 0, 100, 863336821, 811545904, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_438_07', 2)	# 15-16
    GFX_0('SlashA_Blade', 100)
    sprite('Action_438_09', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_DrawnSword')
    sprite('Action_438_12', 4)	# 19-22
    Recovery()
    sprite('Action_438_13', 3)	# 23-25
    sprite('Action_438_14', 2)	# 26-27	 **attackbox here**
    sprite('Action_438_15', 2)	# 28-29	 **attackbox here**
    sprite('Action_438_16', 3)	# 30-32	 **attackbox here**
    sprite('Action_438_17', 5)	# 33-37
    sprite('Action_438_18', 3)	# 38-40
    sprite('Action_438_19', 2)	# 41-42
    sprite('Action_438_20', 2)	# 43-44
    sprite('Action_438_21', 1)	# 45-45
    SFX_3('SE_SheatheSword')
    sprite('Action_418_00', 3)	# 46-48
    sprite('Action_418_01', 3)	# 49-51
    sprite('Action_418_02', 2)	# 52-53

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirUntechableTime(60)
        AirPushbackX(8000)
        AirPushbackY(40000)
        PushbackX(19800)
        AttackP1(70)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        Unknown11042(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_425_00', 1)	# 1-1
    sprite('Action_425_01', 1)	# 2-2
    sprite('Action_425_01', 1)	# 3-3
    sprite('Action_425_02', 1)	# 4-4
    sprite('Action_425_03', 2)	# 5-6
    sprite('Action_425_04', 2)	# 7-8
    sprite('Action_425_05', 2)	# 9-10
    sprite('Action_425_06ex01', 2)	# 11-12	 **attackbox here**
    Unknown7006('uyu109_0', 100, 829782389, 828324144, 0, 0, 100, 829782389, 845101360, 0, 0, 100, 863336821, 811545392, 0, 0, 100)
    SFX_3('SE_DrawnSword')
    GFX_0('6A_Blade', 100)
    sprite('Action_425_07', 4)	# 13-16	 **attackbox here**
    Recovery()
    sprite('Action_425_08', 5)	# 17-21	 **attackbox here**
    sprite('Action_425_09', 3)	# 22-24	 **attackbox here**
    sprite('Action_425_10', 3)	# 25-27	 **attackbox here**
    SFX_3('SE_SheatheSword')
    sprite('Action_418_00', 4)	# 28-31
    sprite('Action_418_01', 4)	# 32-35
    sprite('Action_418_02', 3)	# 36-38

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
        AirUntechableTime(30)
        AttackP1(70)
        AirPushbackX(15000)
        AirPushbackY(12500)
        PushbackX(6000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Hitstop(4)
        Unknown11042(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_450_00', 1)	# 1-1
    sprite('Action_450_01', 1)	# 2-2
    sprite('Action_450_02', 1)	# 3-3
    sprite('Action_450_03', 1)	# 4-4
    sprite('Action_450_04', 1)	# 5-5
    sprite('Action_403_00', 5)	# 6-10
    sprite('Action_403_01', 4)	# 11-14
    physicsXImpulse(48000)
    physicsYImpulse(12000)
    setGravity(1000)
    sprite('Action_403_02ex01', 8)	# 15-22	 **attackbox here**
    Unknown1019(85)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_403_03', 1)	# 23-23
    SFX_4('uyu110_2')
    Unknown1019(80)
    Unknown23027()
    sprite('Action_403_04', 3)	# 24-26	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_DrawnSword')
    GFX_0('66C_Blade', 100)
    physicsXImpulse(-15000)
    Unknown1028(1200)
    physicsYImpulse(20000)
    Unknown1043()
    AttackLevel_(3)
    Hitstop(8)
    AirUntechableTime(60)
    Unknown9190(1)
    AirPushbackX(10000)
    AirPushbackY(-45000)
    PushbackX(19800)
    YImpluseBeforeWallbounce(0)
    Unknown9118(55)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    Unknown9016(1)
    sprite('Action_403_05', 4)	# 27-30
    Unknown23027()
    Recovery()
    sprite('Action_403_06', 4)	# 31-34
    Unknown1028(0)
    sprite('Action_403_05', 4)	# 35-38
    sprite('Action_403_06', 4)	# 39-42
    sprite('Action_403_07', 4)	# 43-46
    SFX_3('SE_SheatheSword')
    sprite('Action_403_08', 4)	# 47-50
    sprite('Action_403_09', 4)	# 51-54
    sprite('Action_403_10', 4)	# 55-58
    label(0)
    sprite('Action_403_11', 3)	# 59-61
    sprite('Action_403_12', 3)	# 62-64
    gotoLabel(0)
    label(1)
    sprite('Action_403_13', 5)	# 65-69
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_403_14', 5)	# 70-74
    sprite('Action_403_15', 3)	# 75-77
    Unknown18009(0)
    sprite('Action_403_16', 2)	# 78-79

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
    Unknown2036(75, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-500000)
    Unknown1019(4)
    label(0)
    sprite('Action_022_00', 3)	# 3-5
    sprite('Action_022_01', 3)	# 6-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 9-18
    if SLOT_58:
        enterState('UltimateSlashODDDD')
    else:
        enterState('UltimateSlashDDD')

@State
def UltimateSlashDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(500)
        Unknown11091(100)
        Unknown30055('60ae0a003200000000000000')
        AttackP1(100)
        AttackP2(100)
        PushbackX(15000)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Hitstop(9)
        Unknown11001(10, 10, 10)
        Unknown2073(1)
        Unknown9154(60)
        Unknown11064(1)
        Unknown30063(1)
        Unknown11032('804f120000000000ffffffffffffffff')
        setInvincible(1)
        SLOT_59 = 0
        if random_(2, 0, 50):
            SLOT_59 = 1
    sprite('Action_215_00', 7)	# 1-7
    Unknown1084(1)
    sprite('Action_215_01', 4)	# 8-11
    sprite('Action_215_02', 4)	# 12-15
    loopRest()
    label(1)
    sprite('Action_215_03', 34)	# 16-49
    if SLOT_59:
        SFX_1('uyu250_0')
    else:
        SFX_1('uyu250_1')
    sprite('Action_215_04', 1)	# 50-50
    SFX_3('SE_DrawnSword')
    sprite('Action_215_05', 3)	# 51-53	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade1', 100)

    def upon_78():
        SLOT_58 = 1
        GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_06', 3)	# 54-56
    sprite('Action_215_06', 3)	# 57-59
    sprite('Action_215_07', 4)	# 60-63
    GFX_0('IW_Zanzo', 100)
    sprite('Action_215_08', 4)	# 64-67
    sprite('Action_215_09', 5)	# 68-72
    sprite('Action_215_10', 1)	# 73-73
    SFX_3('SE_DrawnSword')
    sprite('Action_215_11', 2)	# 74-75	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade2', 100)
    Unknown30055('000000000000000000000000')
    clearUponHandler(78)

    def upon_78():
        if SLOT_158:
            Unknown11069('UltimateSlashDDDExe')
            Unknown2038(1)
            Unknown23024(2)
            GFX_0('IW_Kanji_Tsubomi', 100)
            GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_12', 1)	# 76-76	 **attackbox here**
    clearUponHandler(78)
    Unknown23027()
    loopRest()
    if SLOT_2:
        if SLOT_158:
            enterState('UltimateSlashDDDExe')
    sprite('Action_215_13', 5)	# 77-81
    setInvincible(0)
    sprite('Action_215_14', 5)	# 82-86
    sprite('Action_215_15', 5)	# 87-91
    sprite('Action_215_16', 7)	# 92-98
    sprite('Action_215_17', 7)	# 99-105
    SFX_3('SE_SheatheSword')
    sprite('Action_215_17', 2)	# 106-107
    sprite('Action_215_19', 10)	# 108-117	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(100000)
    Unknown2017(0)
    Unknown1028(-4000)
    Unknown11069('')
    Hitstop(2)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9154(15)
    Unknown9130(16)
    Unknown9142(100)
    Unknown11064(0)
    Unknown2073(0)
    sprite('Action_215_20', 6)	# 118-123
    Unknown2017(1)
    sprite('Action_215_21', 6)	# 124-129
    sprite('Action_215_22', 4)	# 130-133
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown1028(-1000)
    sprite('Action_215_23', 4)	# 134-137
    sprite('Action_215_24', 2)	# 138-139
    GFX_0('IW_Ralease', 100)
    sprite('Action_215_25', 5)	# 140-144
    Unknown1084(1)
    sprite('Action_215_26', 5)	# 145-149
    sprite('Action_215_27', 6)	# 150-155
    SFX_3('SE_SheatheSword')
    sprite('Action_215_28', 20)	# 156-175
    sprite('Action_215_29', 5)	# 176-180
    sprite('Action_215_30', 5)	# 181-185

@State
def UltimateSlashDDDExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(0)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        Hitstop(2)
        PushbackX(0)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown9154(120)
        Unknown11064(1)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11069('UltimateSlashDDDExe')
        Unknown23022(1)
        Unknown2034(0)
        Unknown2053(0)
        Unknown2017(0)
        Unknown30063(1)

        def upon_STATE_END():
            Unknown23022(0)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_215_12', 4)	# 1-4	 **attackbox here**
    RefreshMultihit()
    Unknown11001(0, 60, 60)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('IWExe_Camera', 100)
    sprite('Action_215_13', 5)	# 5-9
    sprite('Action_215_14', 5)	# 10-14
    sprite('Action_215_15', 5)	# 15-19
    sprite('Action_215_16', 7)	# 20-26
    sprite('Action_215_17', 9)	# 27-35
    SFX_3('SE_SheatheSword')
    sprite('Action_216_00', 1)	# 36-36
    Unknown1086(22)
    GFX_0('IWExe_Blade1', 100)
    GFX_0('IWExe_Kimono', 100)
    GFX_0('IWExe_Tanmono', 100)
    physicsXImpulse(32000)
    Unknown1028(-1700)
    if SLOT_59:
        SFX_1('uyu251_0')
    sprite('Action_216_01', 1)	# 37-37
    sprite('Action_216_02', 1)	# 38-38
    sprite('Action_216_03', 4)	# 39-42
    sprite('Action_216_04', 4)	# 43-46
    GFX_0('IW_Kanji_Moe', 100)
    sprite('Action_216_03', 4)	# 47-50
    sprite('Action_216_04', 4)	# 51-54
    sprite('Action_216_05', 6)	# 55-60
    Unknown1084(1)
    sprite('Action_216_06', 8)	# 61-68	 **attackbox here**
    sprite('Action_216_07', 9)	# 69-77	 **attackbox here**
    sprite('Action_216_08', 9)	# 78-86	 **attackbox here**
    sprite('Action_216_09', 8)	# 87-94	 **attackbox here**
    GFX_0('IW_Kanji_Saku', 100)
    sprite('Action_216_10', 6)	# 95-100	 **attackbox here**
    sprite('Action_216_11', 4)	# 101-104	 **attackbox here**
    sprite('Action_216_12', 3)	# 105-107	 **attackbox here**
    physicsXImpulse(-100000)
    Unknown1028(4000)
    sprite('Action_216_13', 3)	# 108-110
    SFX_3('SE_DrawnSword')
    GFX_0('IWExe_Blade2', 100)
    Unknown1019(3)
    Unknown1028(0)
    physicsYImpulse(27500)
    setGravity(1500)
    sprite('Action_216_14', 3)	# 111-113
    sprite('Action_216_15', 3)	# 114-116	 **attackbox here**
    GFX_0('IW_Kanji_Chiru', 100)
    RefreshMultihit()
    Damage(1500)
    AirUntechableTime(120)
    Unknown9310(1)
    AirPushbackX(1000)
    AirPushbackY(52000)
    YImpluseBeforeWallbounce(1200)
    Unknown11001(0, -25, -25)
    Hitstop(27)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')
    Unknown11072(1, 150000, 500000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    Unknown11064(0)
    Unknown11056(2)
    GFX_0('IW_Sakura_MatomeFinish', 100)
    Unknown23029(1, 5000, 1)
    if (not SLOT_59):
        SFX_1('uyu251_1')
    sprite('Action_216_16', 1)	# 117-117
    Unknown2017(1)
    sprite('Action_216_17', 1)	# 118-118
    sprite('Action_216_18', 1)	# 119-119
    sprite('Action_216_19', 4)	# 120-123
    sprite('Action_216_20', 8)	# 124-131
    sprite('Action_216_21', 5)	# 132-136
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_216_22', 4)	# 137-140
    sprite('Action_216_23', 4)	# 141-144
    label(0)
    sprite('Action_216_24', 4)	# 145-148
    sprite('Action_216_25', 4)	# 149-152
    gotoLabel(0)
    label(1)
    sprite('Action_216_26', 2)	# 153-154	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_216_27', 3)	# 155-157	 **attackbox here**
    sprite('Action_216_28', 3)	# 158-160	 **attackbox here**
    sprite('Action_216_29', 3)	# 161-163	 **attackbox here**
    sprite('Action_216_30ex01', 4)	# 164-167	 **attackbox here**
    sprite('Action_216_31ex01', 10)	# 168-177	 **attackbox here**
    GFX_0('KimonoDmy', 100)
    sprite('Action_216_26', 3)	# 178-180	 **attackbox here**
    sprite('Action_216_33', 2)	# 181-182	 **attackbox here**
    sprite('Action_216_34', 4)	# 183-186
    sprite('Action_216_35', 15)	# 187-201
    GFX_0('IW_Release', 100)
    sprite('Action_216_36', 5)	# 202-206
    SFX_3('SE_SheatheSword')
    loopRest()
    label(100)
    sprite('Action_216_37', 5)	# 207-211
    sprite('Action_216_38', 4)	# 212-215
    loopRest()
    ExitState()

@State
def UltimateSlashODDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(500)
        Unknown11091(100)
        Unknown30055('60ae0a003200000000000000')
        AttackP1(100)
        AttackP2(100)
        PushbackX(15000)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Hitstop(9)
        Unknown11001(10, 10, 10)
        Unknown2073(1)
        Unknown9154(60)
        Unknown11064(1)
        Unknown30063(1)
        Unknown11032('804f120000000000ffffffffffffffff')
        setInvincible(1)
        SLOT_59 = 0
        if random_(2, 0, 50):
            SLOT_59 = 1

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            SLOT_4 = 0
            if (not SLOT_54):
                Unknown20007(0)
    sprite('Action_215_00', 7)	# 1-7
    Unknown1084(1)
    sprite('Action_215_01', 4)	# 8-11
    sprite('Action_215_02', 4)	# 12-15
    loopRest()
    label(1)
    sprite('Action_215_03', 34)	# 16-49
    if SLOT_59:
        SFX_1('uyu250_0')
    else:
        SFX_1('uyu250_1')
    sprite('Action_215_04', 1)	# 50-50
    SFX_3('SE_DrawnSword')
    sprite('Action_215_05', 3)	# 51-53	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade1', 100)

    def upon_78():
        SLOT_58 = 1
        GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_06', 3)	# 54-56
    sprite('Action_215_06', 3)	# 57-59
    sprite('Action_215_07', 4)	# 60-63
    GFX_0('IW_Zanzo', 100)
    sprite('Action_215_08', 4)	# 64-67
    sprite('Action_215_09', 5)	# 68-72
    sprite('Action_215_10', 1)	# 73-73
    SFX_3('SE_DrawnSword')
    sprite('Action_215_11', 2)	# 74-75	 **attackbox here**
    RefreshMultihit()
    GFX_0('IW_Blade2', 100)
    Unknown30055('000000000000000000000000')
    Unknown11069('UltimateSlashODDDD')
    clearUponHandler(78)

    def upon_78():
        Unknown2038(1)
        Unknown23024(2)
        GFX_0('IW_Kanji_Tsubomi', 100)
        GFX_0('IW_Sakura_Matome', 100)
    sprite('Action_215_12', 1)	# 76-76	 **attackbox here**
    clearUponHandler(78)
    Unknown23027()
    sprite('Action_215_13', 3)	# 77-79
    sprite('Action_215_14', 3)	# 80-82
    sprite('Action_215_15', 3)	# 83-85
    sprite('Action_215_16', 5)	# 86-90
    sprite('Action_215_17', 7)	# 91-97
    SFX_3('SE_SheatheSword')
    sprite('Action_215_17', 2)	# 98-99
    loopRest()
    if SLOT_2:
        _gotolabel(10)
    sprite('Action_215_19', 10)	# 100-109	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(100000)
    Unknown2017(0)
    Unknown1028(-4000)
    Unknown11069('')
    Hitstop(2)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9154(15)
    Unknown9130(16)
    Unknown9142(100)
    Unknown11064(0)
    Unknown2073(0)

    def upon_77():
        Unknown1019(75)
        Unknown1034(75)
    sprite('Action_215_20', 6)	# 110-115
    Unknown2017(1)
    sprite('Action_215_21', 6)	# 116-121
    sprite('Action_215_22', 4)	# 122-125
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown1028(-1000)
    sprite('Action_215_23', 4)	# 126-129
    sprite('Action_215_24', 2)	# 130-131
    GFX_0('IW_Ralease', 100)
    sprite('Action_215_25', 5)	# 132-136
    Unknown1084(1)
    sprite('Action_215_26', 5)	# 137-141
    sprite('Action_215_27', 6)	# 142-147
    SFX_3('SE_SheatheSword')
    sprite('Action_215_28', 20)	# 148-167
    sprite('Action_215_29', 5)	# 168-172
    sprite('Action_215_30', 5)	# 173-177
    ExitState()
    label(10)
    sprite('Action_215_19', 4)	# 178-181	 **attackbox here**
    SFX_3('SE_DrawnSword')
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(270000)
    Unknown2017(0)
    Unknown1028(-4000)
    Unknown3004(-40)
    Damage(50)
    Hitstop(2)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9154(15)
    Unknown9130(16)
    Unknown9142(100)
    Unknown30048(1)

    def upon_78():
        Unknown23024(2)
        Unknown20007(1)
        if (not SLOT_2):
            if SLOT_158:
                Unknown2038(1)
                GFX_0('IW_Kanji_Tsubomi', 100)
                GFX_0('IW_Sakura_Matome', 100)
        if SLOT_54:
            if SLOT_158:
                Unknown11069('UltimateSlashODDDDExe')
    sprite('Action_215_19', 4)	# 182-185	 **attackbox here**
    Unknown2005()
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(180000)
    Unknown1028(-4000)
    sprite('Action_215_19', 4)	# 186-189	 **attackbox here**
    Unknown2005()
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(180000)
    Unknown1028(-4000)
    sprite('Action_215_19', 4)	# 190-193	 **attackbox here**
    SLOT_54 = 1
    Unknown2005()
    RefreshMultihit()
    physicsXImpulse(165000)
    Unknown1028(-4000)
    loopRest()
    if SLOT_2:
        if SLOT_158:
            Unknown3001(255)
            Unknown3004(0)
            Unknown2005()
            enterState('UltimateSlashODDDDExe')
        else:
            Unknown3004(38)
    else:
        Unknown3004(38)
    sprite('Action_215_22', 2)	# 194-195
    clearUponHandler(78)
    setInvincible(0)
    Unknown1084(1)
    sprite('Action_215_19', 2)	# 196-197	 **attackbox here**
    Unknown2005()
    GFX_0('IW_Blade3', 100)
    RefreshMultihit()
    physicsXImpulse(360000)
    Unknown1028(-8000)
    Unknown11064(0)
    Unknown11069('')
    sprite('Action_215_22', 4)	# 198-201
    Unknown2017(1)
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown1028(-1000)
    sprite('Action_215_23', 4)	# 202-205
    sprite('Action_215_24', 2)	# 206-207
    GFX_0('IW_Ralease', 100)
    SFX_3('SE_SheatheSword')
    sprite('Action_215_25', 5)	# 208-212
    Unknown1084(1)
    sprite('Action_215_26', 5)	# 213-217
    sprite('Action_215_27', 6)	# 218-223
    sprite('Action_215_28', 30)	# 224-253
    sprite('Action_215_29', 5)	# 254-258
    sprite('Action_215_30', 5)	# 259-263

@State
def UltimateSlashODDDDExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(0)
        Hitstop(2)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        PushbackX(0)
        Unknown9016(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown9154(120)
        Unknown11064(1)
        Unknown11023(1)
        Unknown30063(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11069('UltimateSlashODDDDExe')
        Unknown20007(1)
        Unknown23022(1)
        Unknown2034(0)
        Unknown2053(0)
        Unknown2017(0)

        def upon_STATE_END():
            Unknown23022(0)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_215_14ex01', 4)	# 1-4	 **attackbox here**
    RefreshMultihit()
    Unknown11001(0, 90, 90)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_215_15', 5)	# 5-9
    Unknown20007(0)
    GFX_0('IWExe_Camera', 100)
    sprite('Action_215_16', 7)	# 10-16
    sprite('Action_215_17', 9)	# 17-25
    SFX_3('SE_SheatheSword')
    sprite('Action_216_00', 1)	# 26-26
    Unknown1086(22)
    GFX_0('IWExe_Blade1', 100)
    GFX_0('IWExe_Kimono', 100)
    GFX_0('IWExe_Tanmono', 100)
    physicsXImpulse(32000)
    Unknown1028(-1700)
    if SLOT_59:
        SFX_1('uyu251_0')
    sprite('Action_216_01', 1)	# 27-27
    sprite('Action_216_02', 1)	# 28-28
    sprite('Action_216_03', 4)	# 29-32
    sprite('Action_216_04', 4)	# 33-36
    GFX_0('IW_Kanji_Moe', 100)
    sprite('Action_216_03', 4)	# 37-40
    sprite('Action_216_04', 4)	# 41-44
    sprite('Action_216_05', 6)	# 45-50
    Unknown1084(1)
    sprite('Action_216_06', 8)	# 51-58	 **attackbox here**
    sprite('Action_216_07', 9)	# 59-67	 **attackbox here**
    sprite('Action_216_08', 9)	# 68-76	 **attackbox here**
    sprite('Action_216_09', 8)	# 77-84	 **attackbox here**
    GFX_0('IW_Kanji_Saku', 100)
    sprite('Action_216_10', 6)	# 85-90	 **attackbox here**
    sprite('Action_216_11', 4)	# 91-94	 **attackbox here**
    sprite('Action_216_12', 3)	# 95-97	 **attackbox here**
    physicsXImpulse(-100000)
    Unknown1028(4000)
    sprite('Action_216_13', 3)	# 98-100
    SFX_3('SE_DrawnSword')
    GFX_0('IWExe_Blade2', 100)
    Unknown1019(3)
    Unknown1028(0)
    physicsYImpulse(27500)
    setGravity(1500)
    sprite('Action_216_14', 3)	# 101-103
    sprite('Action_216_15', 3)	# 104-106	 **attackbox here**
    GFX_0('IW_Kanji_Chiru', 100)
    RefreshMultihit()
    Damage(1500)
    AirUntechableTime(120)
    Unknown9310(30)
    AirPushbackX(-1000)
    AirPushbackY(52000)
    YImpluseBeforeWallbounce(1200)
    Unknown11001(0, -25, -25)
    Hitstop(27)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('IWOD_AddAtkDDD')
    Unknown11072(1, 150000, 500000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    GFX_0('IW_Sakura_MatomeFinish', 100)
    Unknown23029(1, 5000, 1)
    if (not SLOT_59):
        SFX_1('uyu251_1')
    sprite('Action_216_16', 1)	# 107-107
    Unknown2017(1)
    sprite('Action_216_17', 1)	# 108-108
    sprite('Action_216_18', 1)	# 109-109
    sprite('Action_216_19', 4)	# 110-113
    sprite('Action_216_20', 8)	# 114-121
    sprite('Action_216_21', 5)	# 122-126
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_216_22', 4)	# 127-130
    sprite('Action_216_23', 4)	# 131-134
    label(0)
    sprite('Action_216_24', 4)	# 135-138
    sprite('Action_216_25', 4)	# 139-142
    gotoLabel(0)
    label(1)
    sprite('Action_216_26', 2)	# 143-144	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_216_27', 3)	# 145-147	 **attackbox here**
    sprite('Action_216_28', 3)	# 148-150	 **attackbox here**
    sprite('Action_216_29', 3)	# 151-153	 **attackbox here**
    sprite('Action_216_30ex01', 4)	# 154-157	 **attackbox here**
    sprite('Action_216_31ex01', 10)	# 158-167	 **attackbox here**
    GFX_0('KimonoDmy', 100)
    sprite('Action_216_26', 3)	# 168-170	 **attackbox here**
    sprite('Action_216_33', 2)	# 171-172	 **attackbox here**
    sprite('Action_216_34', 4)	# 173-176
    sprite('Action_216_35', 34)	# 177-210
    GFX_0('IWOD_AddAtkDDD', 100)
    GFX_0('IW_Release', 100)
    SFX_1('uyu252')
    SFX_3('SE_SheatheSword')
    sprite('Action_216_36', 5)	# 211-215
    loopRest()
    label(100)
    sprite('Action_216_37', 5)	# 216-220
    sprite('Action_216_38', 4)	# 221-224
    loopRest()
    ExitState()

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 1)	# 121-121
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-500000)
    Unknown1007(2400000)
    physicsXImpulse(17857)
    physicsYImpulse(-85714)
    setGravity(0)
    sprite('Action_007_03', 5)	# 122-126	 **attackbox here**
    sprite('Action_007_04', 5)	# 127-131	 **attackbox here**
    sprite('Action_007_03', 5)	# 132-136	 **attackbox here**
    sprite('Action_007_04', 5)	# 137-141	 **attackbox here**
    sprite('Action_007_03', 5)	# 142-146	 **attackbox here**
    sprite('Action_007_04', 5)	# 147-151	 **attackbox here**

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(9)
    label(1)
    sprite('Action_007_03', 5)	# 152-156	 **attackbox here**
    sprite('Action_007_04', 5)	# 157-161	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_403_13', 16)	# 162-177
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_403_14', 7)	# 178-184
    sprite('Action_403_15', 5)	# 185-189
    sprite('Action_403_16', 4)	# 190-193

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_02', 3)	# 1-3
    sprite('Action_312_03', 3)	# 4-6
    sprite('Action_312_04', 26)	# 7-32
    sprite('Action_312_05', 4)	# 33-36
    sprite('Action_312_06', 4)	# 37-40
    sprite('Action_312_07', 4)	# 41-44
    sprite('Action_312_08', 4)	# 45-48
    sprite('Action_014_00', 3)	# 49-51
    sprite('Action_014_01', 5)	# 52-56
    sprite('Action_014_02', 6)	# 57-62
    sprite('Action_000_00', 30)	# 63-92	 **attackbox here**

@Subroutine
def MouthTableInit():
    Unknown18011('uyu000', 12643, 12641, 25396, 24887, 25399, 24887, 13361, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu500', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu502', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 12849, 14177, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 12341, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu522', 12643, 14177, 12643, 24880, 12339, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu523', 12643, 14177, 14691, 14177, 12899, 24885, 25399, 12337, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu524', 12643, 12641, 25394, 24887, 25399, 24887, 12849, 14179, 12897, 25392, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu404_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu404_1', 12643, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu405_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu405_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu600bjn', 12643, 12897, 25392, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu600bpt', 12643, 13153, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu600pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu600pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu600rbl', 12643, 13665, 13667, 14177, 12643, 24882, 25397, 24885, 25399, 12849, 14177, 12643, 24882, 12339, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu600ugo', 12643, 14177, 14179, 12641, 25394, 12339, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu600uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu601bha', 12643, 14177, 12643, 24882, 25399, 24887, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu601biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 12643, 24887, 12338, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu601pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 13617, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu601rrb', 12643, 12897, 25397, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 12897, 25392, 12343, 14177, 14179, 14177, 12643, 24880, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu603bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu700bjn', 12643, 14177, 14179, 12897, 25392, 24887, 25399, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu700bpt', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu700pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 12337, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu700pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu700rbl', 12643, 12641, 25396, 24887, 13361, 14179, 12897, 25394, 12339, 14177, 14179, 14177, 14179, 13921, 13923, 13921, 12643, 24882, 25398, 24886, 25398, 12849, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 12339, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu700uhy', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 12338, 12643, 24885, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu701bha', 12643, 13921, 13923, 13921, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu701biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu701pyo', 12643, 13153, 25397, 12850, 14177, 14179, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13618, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu701rrb', 12643, 12641, 25394, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 12643, 24880, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uyu701ugo', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 12338, 13411, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bjn')
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
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('biz')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    sprite('Action_050_00', 3)	# 2-4	 **attackbox here**
    sprite('Action_050_01', 3)	# 5-7	 **attackbox here**
    if random_(2, 0, 50):
        Unknown7006('uyu500', 100, 896891253, 12592, 0, 0, 100, 896891253, 12848, 0, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown7006('uyu503', 100, 896891253, 13360, 0, 0, 100, 896891253, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_050_02', 7)	# 8-14	 **attackbox here**
    sprite('Action_050_03', 6)	# 15-20	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 21-29	 **attackbox here**
    sprite('Action_050_05', 7)	# 30-36	 **attackbox here**
    label(1)
    sprite('Action_050_02', 7)	# 37-43	 **attackbox here**
    sprite('Action_050_03', 6)	# 44-49	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 50-58	 **attackbox here**
    sprite('Action_050_05', 7)	# 59-65	 **attackbox here**
    if SLOT_97:
        _gotolabel(1)
    sprite('Action_050_06', 6)	# 66-71
    sprite('Action_050_07', 6)	# 72-77
    sprite('Action_050_08', 5)	# 78-82
    Unknown23018(1)
    label(2)
    sprite('Action_000_00', 8)	# 83-90	 **attackbox here**
    sprite('Action_000_01', 8)	# 91-98	 **attackbox here**
    sprite('Action_000_02', 8)	# 99-106	 **attackbox here**
    sprite('Action_000_03', 8)	# 107-114	 **attackbox here**
    sprite('Action_000_04', 8)	# 115-122	 **attackbox here**
    sprite('Action_000_05', 8)	# 123-130	 **attackbox here**
    sprite('Action_000_06', 8)	# 131-138	 **attackbox here**
    sprite('Action_000_07', 8)	# 139-146	 **attackbox here**
    sprite('Action_000_08', 8)	# 147-154	 **attackbox here**
    sprite('Action_000_09', 8)	# 155-162	 **attackbox here**
    sprite('Action_000_10', 8)	# 163-170	 **attackbox here**
    sprite('Action_000_11', 8)	# 171-178	 **attackbox here**
    sprite('Action_000_12', 8)	# 179-186	 **attackbox here**
    sprite('Action_000_13', 8)	# 187-194	 **attackbox here**
    sprite('Action_000_14', 8)	# 195-202	 **attackbox here**
    sprite('Action_000_15', 8)	# 203-210	 **attackbox here**
    sprite('Action_000_16', 8)	# 211-218	 **attackbox here**
    sprite('Action_000_17', 8)	# 219-226	 **attackbox here**
    sprite('Action_000_18', 8)	# 227-234	 **attackbox here**
    sprite('Action_000_19', 8)	# 235-242	 **attackbox here**
    sprite('Action_000_20', 8)	# 243-250	 **attackbox here**
    sprite('Action_000_21', 8)	# 251-258	 **attackbox here**
    sprite('Action_000_22', 8)	# 259-266	 **attackbox here**
    sprite('Action_000_23', 8)	# 267-274	 **attackbox here**
    sprite('Action_000_24', 8)	# 275-282	 **attackbox here**
    sprite('Action_000_25', 8)	# 283-290	 **attackbox here**
    sprite('Action_000_26', 8)	# 291-298	 **attackbox here**
    sprite('Action_000_27', 8)	# 299-306	 **attackbox here**
    sprite('Action_000_28', 8)	# 307-314	 **attackbox here**
    sprite('Action_000_29', 8)	# 315-322	 **attackbox here**
    sprite('Action_000_30', 8)	# 323-330	 **attackbox here**
    sprite('Action_000_31', 8)	# 331-338	 **attackbox here**
    sprite('Action_000_32', 6)	# 339-344	 **attackbox here**
    sprite('Action_000_33', 2)	# 345-346	 **attackbox here**
    sprite('Action_000_34', 8)	# 347-354	 **attackbox here**
    sprite('Action_000_35', 8)	# 355-362	 **attackbox here**
    sprite('Action_000_36', 8)	# 363-370	 **attackbox here**
    sprite('Action_000_37', 8)	# 371-378	 **attackbox here**
    sprite('Action_000_38', 8)	# 379-386	 **attackbox here**
    sprite('Action_000_39', 8)	# 387-394	 **attackbox here**
    sprite('Action_000_40', 8)	# 395-402	 **attackbox here**
    sprite('Action_000_41', 8)	# 403-410	 **attackbox here**
    sprite('Action_000_42', 8)	# 411-418	 **attackbox here**
    sprite('Action_000_43', 8)	# 419-426	 **attackbox here**
    sprite('Action_000_44', 8)	# 427-434	 **attackbox here**
    sprite('Action_000_45', 8)	# 435-442	 **attackbox here**
    sprite('Action_000_46', 8)	# 443-450	 **attackbox here**
    sprite('Action_000_47', 8)	# 451-458	 **attackbox here**
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('Action_000_00', 32767)	# 459-33225	 **attackbox here**
    SFX_1('uyu701ugo')
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 33226-33226	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 8)	# 33227-33234	 **attackbox here**
    sprite('Action_000_01', 8)	# 33235-33242	 **attackbox here**
    sprite('Action_000_02', 8)	# 33243-33250	 **attackbox here**
    sprite('Action_000_03', 8)	# 33251-33258	 **attackbox here**
    sprite('Action_000_04', 8)	# 33259-33266	 **attackbox here**
    sprite('Action_000_05', 8)	# 33267-33274	 **attackbox here**
    sprite('Action_000_06', 8)	# 33275-33282	 **attackbox here**
    sprite('Action_000_07', 8)	# 33283-33290	 **attackbox here**
    sprite('Action_000_08', 8)	# 33291-33298	 **attackbox here**
    sprite('Action_000_09', 8)	# 33299-33306	 **attackbox here**
    sprite('Action_000_10', 8)	# 33307-33314	 **attackbox here**
    sprite('Action_000_11', 8)	# 33315-33322	 **attackbox here**
    sprite('Action_000_12', 8)	# 33323-33330	 **attackbox here**
    sprite('Action_000_13', 8)	# 33331-33338	 **attackbox here**
    sprite('Action_000_14', 8)	# 33339-33346	 **attackbox here**
    sprite('Action_000_15', 8)	# 33347-33354	 **attackbox here**
    sprite('Action_000_16', 8)	# 33355-33362	 **attackbox here**
    sprite('Action_000_17', 8)	# 33363-33370	 **attackbox here**
    sprite('Action_000_18', 8)	# 33371-33378	 **attackbox here**
    sprite('Action_000_19', 8)	# 33379-33386	 **attackbox here**
    sprite('Action_000_20', 8)	# 33387-33394	 **attackbox here**
    sprite('Action_000_21', 8)	# 33395-33402	 **attackbox here**
    sprite('Action_000_22', 8)	# 33403-33410	 **attackbox here**
    sprite('Action_000_23', 8)	# 33411-33418	 **attackbox here**
    sprite('Action_000_24', 8)	# 33419-33426	 **attackbox here**
    sprite('Action_000_25', 8)	# 33427-33434	 **attackbox here**
    sprite('Action_000_26', 8)	# 33435-33442	 **attackbox here**
    sprite('Action_000_27', 8)	# 33443-33450	 **attackbox here**
    sprite('Action_000_28', 8)	# 33451-33458	 **attackbox here**
    sprite('Action_000_29', 8)	# 33459-33466	 **attackbox here**
    sprite('Action_000_30', 8)	# 33467-33474	 **attackbox here**
    sprite('Action_000_31', 8)	# 33475-33482	 **attackbox here**
    sprite('Action_000_32', 6)	# 33483-33488	 **attackbox here**
    sprite('Action_000_33', 2)	# 33489-33490	 **attackbox here**
    sprite('Action_000_34', 8)	# 33491-33498	 **attackbox here**
    sprite('Action_000_35', 8)	# 33499-33506	 **attackbox here**
    sprite('Action_000_36', 8)	# 33507-33514	 **attackbox here**
    sprite('Action_000_37', 8)	# 33515-33522	 **attackbox here**
    sprite('Action_000_38', 8)	# 33523-33530	 **attackbox here**
    sprite('Action_000_39', 8)	# 33531-33538	 **attackbox here**
    sprite('Action_000_40', 8)	# 33539-33546	 **attackbox here**
    sprite('Action_000_41', 8)	# 33547-33554	 **attackbox here**
    sprite('Action_000_42', 8)	# 33555-33562	 **attackbox here**
    sprite('Action_000_43', 8)	# 33563-33570	 **attackbox here**
    sprite('Action_000_44', 8)	# 33571-33578	 **attackbox here**
    sprite('Action_000_45', 8)	# 33579-33586	 **attackbox here**
    sprite('Action_000_46', 8)	# 33587-33594	 **attackbox here**
    sprite('Action_000_47', 8)	# 33595-33602	 **attackbox here**
    gotoLabel(992)
    ExitState()
    label(100)
    sprite('Action_050_00', 3)	# 33603-33605	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 3)	# 33606-33608	 **attackbox here**
    SFX_1('uyu600bjn')
    sprite('Action_050_02', 7)	# 33609-33615	 **attackbox here**
    sprite('Action_050_03', 6)	# 33616-33621	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 33622-33630	 **attackbox here**
    sprite('Action_050_05', 7)	# 33631-33637	 **attackbox here**
    label(101)
    sprite('Action_050_02', 7)	# 33638-33644	 **attackbox here**
    sprite('Action_050_03', 6)	# 33645-33650	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 33651-33659	 **attackbox here**
    sprite('Action_050_05', 7)	# 33660-33666	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_050_06', 6)	# 33667-33672
    sprite('Action_050_07', 6)	# 33673-33678
    sprite('Action_050_08', 5)	# 33679-33683
    Unknown21011(270)
    label(102)
    sprite('Action_000_00', 8)	# 33684-33691	 **attackbox here**
    sprite('Action_000_01', 8)	# 33692-33699	 **attackbox here**
    sprite('Action_000_02', 8)	# 33700-33707	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_03', 8)	# 33708-33715	 **attackbox here**
    sprite('Action_000_04', 8)	# 33716-33723	 **attackbox here**
    sprite('Action_000_05', 8)	# 33724-33731	 **attackbox here**
    sprite('Action_000_06', 8)	# 33732-33739	 **attackbox here**
    sprite('Action_000_07', 8)	# 33740-33747	 **attackbox here**
    sprite('Action_000_08', 8)	# 33748-33755	 **attackbox here**
    sprite('Action_000_09', 8)	# 33756-33763	 **attackbox here**
    sprite('Action_000_10', 8)	# 33764-33771	 **attackbox here**
    sprite('Action_000_11', 8)	# 33772-33779	 **attackbox here**
    sprite('Action_000_12', 8)	# 33780-33787	 **attackbox here**
    sprite('Action_000_13', 8)	# 33788-33795	 **attackbox here**
    sprite('Action_000_14', 8)	# 33796-33803	 **attackbox here**
    sprite('Action_000_15', 8)	# 33804-33811	 **attackbox here**
    sprite('Action_000_16', 8)	# 33812-33819	 **attackbox here**
    sprite('Action_000_17', 8)	# 33820-33827	 **attackbox here**
    sprite('Action_000_18', 8)	# 33828-33835	 **attackbox here**
    sprite('Action_000_19', 8)	# 33836-33843	 **attackbox here**
    sprite('Action_000_20', 8)	# 33844-33851	 **attackbox here**
    sprite('Action_000_21', 8)	# 33852-33859	 **attackbox here**
    sprite('Action_000_22', 8)	# 33860-33867	 **attackbox here**
    sprite('Action_000_23', 8)	# 33868-33875	 **attackbox here**
    sprite('Action_000_24', 8)	# 33876-33883	 **attackbox here**
    sprite('Action_000_25', 8)	# 33884-33891	 **attackbox here**
    sprite('Action_000_26', 8)	# 33892-33899	 **attackbox here**
    sprite('Action_000_27', 8)	# 33900-33907	 **attackbox here**
    sprite('Action_000_28', 8)	# 33908-33915	 **attackbox here**
    sprite('Action_000_29', 8)	# 33916-33923	 **attackbox here**
    sprite('Action_000_30', 8)	# 33924-33931	 **attackbox here**
    sprite('Action_000_31', 8)	# 33932-33939	 **attackbox here**
    sprite('Action_000_32', 6)	# 33940-33945	 **attackbox here**
    sprite('Action_000_33', 2)	# 33946-33947	 **attackbox here**
    sprite('Action_000_34', 8)	# 33948-33955	 **attackbox here**
    sprite('Action_000_35', 8)	# 33956-33963	 **attackbox here**
    sprite('Action_000_36', 8)	# 33964-33971	 **attackbox here**
    sprite('Action_000_37', 8)	# 33972-33979	 **attackbox here**
    sprite('Action_000_38', 8)	# 33980-33987	 **attackbox here**
    sprite('Action_000_39', 8)	# 33988-33995	 **attackbox here**
    sprite('Action_000_40', 8)	# 33996-34003	 **attackbox here**
    sprite('Action_000_41', 8)	# 34004-34011	 **attackbox here**
    sprite('Action_000_42', 8)	# 34012-34019	 **attackbox here**
    sprite('Action_000_43', 8)	# 34020-34027	 **attackbox here**
    sprite('Action_000_44', 8)	# 34028-34035	 **attackbox here**
    sprite('Action_000_45', 8)	# 34036-34043	 **attackbox here**
    sprite('Action_000_46', 8)	# 34044-34051	 **attackbox here**
    sprite('Action_000_47', 8)	# 34052-34059	 **attackbox here**
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('Yuz636_00', 30)	# 34060-34089
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1334000)
    SFX_1('uyu600bpt')
    Unknown2019(-500)
    sprite('Yuz636_01', 6)	# 34090-34095
    Unknown21007(24, 40)
    label(111)
    sprite('Yuz636_02', 6)	# 34096-34101	 **attackbox here**
    sprite('Yuz636_03', 6)	# 34102-34107	 **attackbox here**
    sprite('Yuz636_04', 6)	# 34108-34113	 **attackbox here**
    sprite('Yuz636_03', 6)	# 34114-34119	 **attackbox here**
    if SLOT_97:
        _gotolabel(111)
    sprite('Yuz636_02', 1)	# 34120-34120	 **attackbox here**
    Unknown21007(24, 39)
    Unknown21011(240)
    label(112)
    sprite('Yuz636_02', 6)	# 34121-34126	 **attackbox here**
    sprite('Yuz636_03', 6)	# 34127-34132	 **attackbox here**
    sprite('Yuz636_04', 6)	# 34133-34138	 **attackbox here**
    sprite('Yuz636_03', 6)	# 34139-34144	 **attackbox here**
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('Action_050_00', 3)	# 34145-34147	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 3)	# 34148-34150	 **attackbox here**
    SFX_1('uyu600bjn')
    sprite('Action_050_02', 7)	# 34151-34157	 **attackbox here**
    sprite('Action_050_03', 6)	# 34158-34163	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 34164-34172	 **attackbox here**
    sprite('Action_050_05', 7)	# 34173-34179	 **attackbox here**
    label(121)
    sprite('Action_050_02', 7)	# 34180-34186	 **attackbox here**
    sprite('Action_050_03', 6)	# 34187-34192	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 34193-34201	 **attackbox here**
    sprite('Action_050_05', 7)	# 34202-34208	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_050_06', 6)	# 34209-34214
    sprite('Action_050_07', 6)	# 34215-34220
    sprite('Action_050_08', 5)	# 34221-34225
    Unknown21011(270)
    label(122)
    sprite('Action_000_00', 8)	# 34226-34233	 **attackbox here**
    sprite('Action_000_01', 8)	# 34234-34241	 **attackbox here**
    sprite('Action_000_02', 8)	# 34242-34249	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_03', 8)	# 34250-34257	 **attackbox here**
    sprite('Action_000_04', 8)	# 34258-34265	 **attackbox here**
    sprite('Action_000_05', 8)	# 34266-34273	 **attackbox here**
    sprite('Action_000_06', 8)	# 34274-34281	 **attackbox here**
    sprite('Action_000_07', 8)	# 34282-34289	 **attackbox here**
    sprite('Action_000_08', 8)	# 34290-34297	 **attackbox here**
    sprite('Action_000_09', 8)	# 34298-34305	 **attackbox here**
    sprite('Action_000_10', 8)	# 34306-34313	 **attackbox here**
    sprite('Action_000_11', 8)	# 34314-34321	 **attackbox here**
    sprite('Action_000_12', 8)	# 34322-34329	 **attackbox here**
    sprite('Action_000_13', 8)	# 34330-34337	 **attackbox here**
    sprite('Action_000_14', 8)	# 34338-34345	 **attackbox here**
    sprite('Action_000_15', 8)	# 34346-34353	 **attackbox here**
    sprite('Action_000_16', 8)	# 34354-34361	 **attackbox here**
    sprite('Action_000_17', 8)	# 34362-34369	 **attackbox here**
    sprite('Action_000_18', 8)	# 34370-34377	 **attackbox here**
    sprite('Action_000_19', 8)	# 34378-34385	 **attackbox here**
    sprite('Action_000_20', 8)	# 34386-34393	 **attackbox here**
    sprite('Action_000_21', 8)	# 34394-34401	 **attackbox here**
    sprite('Action_000_22', 8)	# 34402-34409	 **attackbox here**
    sprite('Action_000_23', 8)	# 34410-34417	 **attackbox here**
    sprite('Action_000_24', 8)	# 34418-34425	 **attackbox here**
    sprite('Action_000_25', 8)	# 34426-34433	 **attackbox here**
    sprite('Action_000_26', 8)	# 34434-34441	 **attackbox here**
    sprite('Action_000_27', 8)	# 34442-34449	 **attackbox here**
    sprite('Action_000_28', 8)	# 34450-34457	 **attackbox here**
    sprite('Action_000_29', 8)	# 34458-34465	 **attackbox here**
    sprite('Action_000_30', 8)	# 34466-34473	 **attackbox here**
    sprite('Action_000_31', 8)	# 34474-34481	 **attackbox here**
    sprite('Action_000_32', 6)	# 34482-34487	 **attackbox here**
    sprite('Action_000_33', 2)	# 34488-34489	 **attackbox here**
    sprite('Action_000_34', 8)	# 34490-34497	 **attackbox here**
    sprite('Action_000_35', 8)	# 34498-34505	 **attackbox here**
    sprite('Action_000_36', 8)	# 34506-34513	 **attackbox here**
    sprite('Action_000_37', 8)	# 34514-34521	 **attackbox here**
    sprite('Action_000_38', 8)	# 34522-34529	 **attackbox here**
    sprite('Action_000_39', 8)	# 34530-34537	 **attackbox here**
    sprite('Action_000_40', 8)	# 34538-34545	 **attackbox here**
    sprite('Action_000_41', 8)	# 34546-34553	 **attackbox here**
    sprite('Action_000_42', 8)	# 34554-34561	 **attackbox here**
    sprite('Action_000_43', 8)	# 34562-34569	 **attackbox here**
    sprite('Action_000_44', 8)	# 34570-34577	 **attackbox here**
    sprite('Action_000_45', 8)	# 34578-34585	 **attackbox here**
    sprite('Action_000_46', 8)	# 34586-34593	 **attackbox here**
    sprite('Action_000_47', 8)	# 34594-34601	 **attackbox here**
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('Action_050_00', 3)	# 34602-34604	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 3)	# 34605-34607	 **attackbox here**
    SFX_1('uyu600pyo')
    sprite('Action_050_02', 7)	# 34608-34614	 **attackbox here**
    sprite('Action_050_03', 6)	# 34615-34620	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 34621-34629	 **attackbox here**
    sprite('Action_050_05', 7)	# 34630-34636	 **attackbox here**
    label(131)
    sprite('Action_050_02', 7)	# 34637-34643	 **attackbox here**
    sprite('Action_050_03', 6)	# 34644-34649	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 34650-34658	 **attackbox here**
    sprite('Action_050_05', 7)	# 34659-34665	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_050_06', 6)	# 34666-34671
    sprite('Action_050_07', 6)	# 34672-34677
    sprite('Action_050_08', 5)	# 34678-34682
    Unknown21011(270)
    label(132)
    sprite('Action_000_00', 8)	# 34683-34690	 **attackbox here**
    sprite('Action_000_01', 8)	# 34691-34698	 **attackbox here**
    sprite('Action_000_02', 8)	# 34699-34706	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_03', 8)	# 34707-34714	 **attackbox here**
    sprite('Action_000_04', 8)	# 34715-34722	 **attackbox here**
    sprite('Action_000_05', 8)	# 34723-34730	 **attackbox here**
    sprite('Action_000_06', 8)	# 34731-34738	 **attackbox here**
    sprite('Action_000_07', 8)	# 34739-34746	 **attackbox here**
    sprite('Action_000_08', 8)	# 34747-34754	 **attackbox here**
    sprite('Action_000_09', 8)	# 34755-34762	 **attackbox here**
    sprite('Action_000_10', 8)	# 34763-34770	 **attackbox here**
    sprite('Action_000_11', 8)	# 34771-34778	 **attackbox here**
    sprite('Action_000_12', 8)	# 34779-34786	 **attackbox here**
    sprite('Action_000_13', 8)	# 34787-34794	 **attackbox here**
    sprite('Action_000_14', 8)	# 34795-34802	 **attackbox here**
    sprite('Action_000_15', 8)	# 34803-34810	 **attackbox here**
    sprite('Action_000_16', 8)	# 34811-34818	 **attackbox here**
    sprite('Action_000_17', 8)	# 34819-34826	 **attackbox here**
    sprite('Action_000_18', 8)	# 34827-34834	 **attackbox here**
    sprite('Action_000_19', 8)	# 34835-34842	 **attackbox here**
    sprite('Action_000_20', 8)	# 34843-34850	 **attackbox here**
    sprite('Action_000_21', 8)	# 34851-34858	 **attackbox here**
    sprite('Action_000_22', 8)	# 34859-34866	 **attackbox here**
    sprite('Action_000_23', 8)	# 34867-34874	 **attackbox here**
    sprite('Action_000_24', 8)	# 34875-34882	 **attackbox here**
    sprite('Action_000_25', 8)	# 34883-34890	 **attackbox here**
    sprite('Action_000_26', 8)	# 34891-34898	 **attackbox here**
    sprite('Action_000_27', 8)	# 34899-34906	 **attackbox here**
    sprite('Action_000_28', 8)	# 34907-34914	 **attackbox here**
    sprite('Action_000_29', 8)	# 34915-34922	 **attackbox here**
    sprite('Action_000_30', 8)	# 34923-34930	 **attackbox here**
    sprite('Action_000_31', 8)	# 34931-34938	 **attackbox here**
    sprite('Action_000_32', 6)	# 34939-34944	 **attackbox here**
    sprite('Action_000_33', 2)	# 34945-34946	 **attackbox here**
    sprite('Action_000_34', 8)	# 34947-34954	 **attackbox here**
    sprite('Action_000_35', 8)	# 34955-34962	 **attackbox here**
    sprite('Action_000_36', 8)	# 34963-34970	 **attackbox here**
    sprite('Action_000_37', 8)	# 34971-34978	 **attackbox here**
    sprite('Action_000_38', 8)	# 34979-34986	 **attackbox here**
    sprite('Action_000_39', 8)	# 34987-34994	 **attackbox here**
    sprite('Action_000_40', 8)	# 34995-35002	 **attackbox here**
    sprite('Action_000_41', 8)	# 35003-35010	 **attackbox here**
    sprite('Action_000_42', 8)	# 35011-35018	 **attackbox here**
    sprite('Action_000_43', 8)	# 35019-35026	 **attackbox here**
    sprite('Action_000_44', 8)	# 35027-35034	 **attackbox here**
    sprite('Action_000_45', 8)	# 35035-35042	 **attackbox here**
    sprite('Action_000_46', 8)	# 35043-35050	 **attackbox here**
    sprite('Action_000_47', 8)	# 35051-35058	 **attackbox here**
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('Action_050_00', 3)	# 35059-35061	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 3)	# 35062-35064	 **attackbox here**
    SFX_1('uyu600rbl')
    sprite('Action_050_02', 7)	# 35065-35071	 **attackbox here**
    sprite('Action_050_03', 6)	# 35072-35077	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 35078-35086	 **attackbox here**
    sprite('Action_050_05', 7)	# 35087-35093	 **attackbox here**
    label(141)
    sprite('Action_050_02', 7)	# 35094-35100	 **attackbox here**
    sprite('Action_050_03', 6)	# 35101-35106	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 35107-35115	 **attackbox here**
    sprite('Action_050_05', 7)	# 35116-35122	 **attackbox here**
    if SLOT_97:
        _gotolabel(141)
    sprite('Action_050_06', 6)	# 35123-35128
    sprite('Action_050_07', 6)	# 35129-35134
    sprite('Action_050_08', 5)	# 35135-35139
    Unknown21011(240)
    label(142)
    sprite('Action_000_00', 8)	# 35140-35147	 **attackbox here**
    sprite('Action_000_01', 8)	# 35148-35155	 **attackbox here**
    sprite('Action_000_02', 8)	# 35156-35163	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_03', 8)	# 35164-35171	 **attackbox here**
    sprite('Action_000_04', 8)	# 35172-35179	 **attackbox here**
    sprite('Action_000_05', 8)	# 35180-35187	 **attackbox here**
    sprite('Action_000_06', 8)	# 35188-35195	 **attackbox here**
    sprite('Action_000_07', 8)	# 35196-35203	 **attackbox here**
    sprite('Action_000_08', 8)	# 35204-35211	 **attackbox here**
    sprite('Action_000_09', 8)	# 35212-35219	 **attackbox here**
    sprite('Action_000_10', 8)	# 35220-35227	 **attackbox here**
    sprite('Action_000_11', 8)	# 35228-35235	 **attackbox here**
    sprite('Action_000_12', 8)	# 35236-35243	 **attackbox here**
    sprite('Action_000_13', 8)	# 35244-35251	 **attackbox here**
    sprite('Action_000_14', 8)	# 35252-35259	 **attackbox here**
    sprite('Action_000_15', 8)	# 35260-35267	 **attackbox here**
    sprite('Action_000_16', 8)	# 35268-35275	 **attackbox here**
    sprite('Action_000_17', 8)	# 35276-35283	 **attackbox here**
    sprite('Action_000_18', 8)	# 35284-35291	 **attackbox here**
    sprite('Action_000_19', 8)	# 35292-35299	 **attackbox here**
    sprite('Action_000_20', 8)	# 35300-35307	 **attackbox here**
    sprite('Action_000_21', 8)	# 35308-35315	 **attackbox here**
    sprite('Action_000_22', 8)	# 35316-35323	 **attackbox here**
    sprite('Action_000_23', 8)	# 35324-35331	 **attackbox here**
    sprite('Action_000_24', 8)	# 35332-35339	 **attackbox here**
    sprite('Action_000_25', 8)	# 35340-35347	 **attackbox here**
    sprite('Action_000_26', 8)	# 35348-35355	 **attackbox here**
    sprite('Action_000_27', 8)	# 35356-35363	 **attackbox here**
    sprite('Action_000_28', 8)	# 35364-35371	 **attackbox here**
    sprite('Action_000_29', 8)	# 35372-35379	 **attackbox here**
    sprite('Action_000_30', 8)	# 35380-35387	 **attackbox here**
    sprite('Action_000_31', 8)	# 35388-35395	 **attackbox here**
    sprite('Action_000_32', 6)	# 35396-35401	 **attackbox here**
    sprite('Action_000_33', 2)	# 35402-35403	 **attackbox here**
    sprite('Action_000_34', 8)	# 35404-35411	 **attackbox here**
    sprite('Action_000_35', 8)	# 35412-35419	 **attackbox here**
    sprite('Action_000_36', 8)	# 35420-35427	 **attackbox here**
    sprite('Action_000_37', 8)	# 35428-35435	 **attackbox here**
    sprite('Action_000_38', 8)	# 35436-35443	 **attackbox here**
    sprite('Action_000_39', 8)	# 35444-35451	 **attackbox here**
    sprite('Action_000_40', 8)	# 35452-35459	 **attackbox here**
    sprite('Action_000_41', 8)	# 35460-35467	 **attackbox here**
    sprite('Action_000_42', 8)	# 35468-35475	 **attackbox here**
    sprite('Action_000_43', 8)	# 35476-35483	 **attackbox here**
    sprite('Action_000_44', 8)	# 35484-35491	 **attackbox here**
    sprite('Action_000_45', 8)	# 35492-35499	 **attackbox here**
    sprite('Action_000_46', 8)	# 35500-35507	 **attackbox here**
    sprite('Action_000_47', 8)	# 35508-35515	 **attackbox here**
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('Action_050_00', 3)	# 35516-35518	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 3)	# 35519-35521	 **attackbox here**
    SFX_1('uyu600ugo')
    sprite('Action_050_02', 7)	# 35522-35528	 **attackbox here**
    sprite('Action_050_03', 6)	# 35529-35534	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 35535-35543	 **attackbox here**
    sprite('Action_050_05', 7)	# 35544-35550	 **attackbox here**
    label(151)
    sprite('Action_050_02', 7)	# 35551-35557	 **attackbox here**
    sprite('Action_050_03', 6)	# 35558-35563	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 35564-35572	 **attackbox here**
    sprite('Action_050_05', 7)	# 35573-35579	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('Action_050_06', 6)	# 35580-35585
    sprite('Action_050_07', 6)	# 35586-35591
    sprite('Action_050_08', 5)	# 35592-35596
    Unknown21011(360)
    label(152)
    sprite('Action_000_00', 8)	# 35597-35604	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_01', 8)	# 35605-35612	 **attackbox here**
    sprite('Action_000_02', 8)	# 35613-35620	 **attackbox here**
    sprite('Action_000_03', 8)	# 35621-35628	 **attackbox here**
    sprite('Action_000_04', 8)	# 35629-35636	 **attackbox here**
    sprite('Action_000_05', 8)	# 35637-35644	 **attackbox here**
    sprite('Action_000_06', 8)	# 35645-35652	 **attackbox here**
    sprite('Action_000_07', 8)	# 35653-35660	 **attackbox here**
    sprite('Action_000_08', 8)	# 35661-35668	 **attackbox here**
    sprite('Action_000_09', 8)	# 35669-35676	 **attackbox here**
    sprite('Action_000_10', 8)	# 35677-35684	 **attackbox here**
    sprite('Action_000_11', 8)	# 35685-35692	 **attackbox here**
    sprite('Action_000_12', 8)	# 35693-35700	 **attackbox here**
    sprite('Action_000_13', 8)	# 35701-35708	 **attackbox here**
    sprite('Action_000_14', 8)	# 35709-35716	 **attackbox here**
    sprite('Action_000_15', 8)	# 35717-35724	 **attackbox here**
    sprite('Action_000_16', 8)	# 35725-35732	 **attackbox here**
    sprite('Action_000_17', 8)	# 35733-35740	 **attackbox here**
    sprite('Action_000_18', 8)	# 35741-35748	 **attackbox here**
    sprite('Action_000_19', 8)	# 35749-35756	 **attackbox here**
    sprite('Action_000_20', 8)	# 35757-35764	 **attackbox here**
    sprite('Action_000_21', 8)	# 35765-35772	 **attackbox here**
    sprite('Action_000_22', 8)	# 35773-35780	 **attackbox here**
    sprite('Action_000_23', 8)	# 35781-35788	 **attackbox here**
    sprite('Action_000_24', 8)	# 35789-35796	 **attackbox here**
    sprite('Action_000_25', 8)	# 35797-35804	 **attackbox here**
    sprite('Action_000_26', 8)	# 35805-35812	 **attackbox here**
    sprite('Action_000_27', 8)	# 35813-35820	 **attackbox here**
    sprite('Action_000_28', 8)	# 35821-35828	 **attackbox here**
    sprite('Action_000_29', 8)	# 35829-35836	 **attackbox here**
    sprite('Action_000_30', 8)	# 35837-35844	 **attackbox here**
    sprite('Action_000_31', 8)	# 35845-35852	 **attackbox here**
    sprite('Action_000_32', 6)	# 35853-35858	 **attackbox here**
    sprite('Action_000_33', 2)	# 35859-35860	 **attackbox here**
    sprite('Action_000_34', 8)	# 35861-35868	 **attackbox here**
    sprite('Action_000_35', 8)	# 35869-35876	 **attackbox here**
    sprite('Action_000_36', 8)	# 35877-35884	 **attackbox here**
    sprite('Action_000_37', 8)	# 35885-35892	 **attackbox here**
    sprite('Action_000_38', 8)	# 35893-35900	 **attackbox here**
    sprite('Action_000_39', 8)	# 35901-35908	 **attackbox here**
    sprite('Action_000_40', 8)	# 35909-35916	 **attackbox here**
    sprite('Action_000_41', 8)	# 35917-35924	 **attackbox here**
    sprite('Action_000_42', 8)	# 35925-35932	 **attackbox here**
    sprite('Action_000_43', 8)	# 35933-35940	 **attackbox here**
    sprite('Action_000_44', 8)	# 35941-35948	 **attackbox here**
    sprite('Action_000_45', 8)	# 35949-35956	 **attackbox here**
    sprite('Action_000_46', 8)	# 35957-35964	 **attackbox here**
    sprite('Action_000_47', 8)	# 35965-35972	 **attackbox here**
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('Action_050_00', 3)	# 35973-35975	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_01', 3)	# 35976-35978	 **attackbox here**
    SFX_1('uyu600uhy')
    sprite('Action_050_02', 7)	# 35979-35985	 **attackbox here**
    sprite('Action_050_03', 6)	# 35986-35991	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 35992-36000	 **attackbox here**
    sprite('Action_050_05', 7)	# 36001-36007	 **attackbox here**
    label(161)
    sprite('Action_050_02', 7)	# 36008-36014	 **attackbox here**
    sprite('Action_050_03', 6)	# 36015-36020	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_050_04', 9)	# 36021-36029	 **attackbox here**
    sprite('Action_050_05', 7)	# 36030-36036	 **attackbox here**
    if SLOT_97:
        _gotolabel(161)
    sprite('Action_050_06', 6)	# 36037-36042
    Unknown21007(24, 40)
    sprite('Action_050_07', 6)	# 36043-36048
    sprite('Action_050_08', 5)	# 36049-36053
    Unknown21011(220)
    label(162)
    sprite('Action_000_00', 8)	# 36054-36061	 **attackbox here**
    sprite('Action_000_01', 8)	# 36062-36069	 **attackbox here**
    sprite('Action_000_02', 8)	# 36070-36077	 **attackbox here**
    sprite('Action_000_03', 8)	# 36078-36085	 **attackbox here**
    sprite('Action_000_04', 8)	# 36086-36093	 **attackbox here**
    sprite('Action_000_05', 8)	# 36094-36101	 **attackbox here**
    sprite('Action_000_06', 8)	# 36102-36109	 **attackbox here**
    sprite('Action_000_07', 8)	# 36110-36117	 **attackbox here**
    sprite('Action_000_08', 8)	# 36118-36125	 **attackbox here**
    sprite('Action_000_09', 8)	# 36126-36133	 **attackbox here**
    sprite('Action_000_10', 8)	# 36134-36141	 **attackbox here**
    sprite('Action_000_11', 8)	# 36142-36149	 **attackbox here**
    sprite('Action_000_12', 8)	# 36150-36157	 **attackbox here**
    sprite('Action_000_13', 8)	# 36158-36165	 **attackbox here**
    sprite('Action_000_14', 8)	# 36166-36173	 **attackbox here**
    sprite('Action_000_15', 8)	# 36174-36181	 **attackbox here**
    sprite('Action_000_16', 8)	# 36182-36189	 **attackbox here**
    sprite('Action_000_17', 8)	# 36190-36197	 **attackbox here**
    sprite('Action_000_18', 8)	# 36198-36205	 **attackbox here**
    sprite('Action_000_19', 8)	# 36206-36213	 **attackbox here**
    sprite('Action_000_20', 8)	# 36214-36221	 **attackbox here**
    sprite('Action_000_21', 8)	# 36222-36229	 **attackbox here**
    sprite('Action_000_22', 8)	# 36230-36237	 **attackbox here**
    sprite('Action_000_23', 8)	# 36238-36245	 **attackbox here**
    sprite('Action_000_24', 8)	# 36246-36253	 **attackbox here**
    sprite('Action_000_25', 8)	# 36254-36261	 **attackbox here**
    sprite('Action_000_26', 8)	# 36262-36269	 **attackbox here**
    sprite('Action_000_27', 8)	# 36270-36277	 **attackbox here**
    sprite('Action_000_28', 8)	# 36278-36285	 **attackbox here**
    sprite('Action_000_29', 8)	# 36286-36293	 **attackbox here**
    sprite('Action_000_30', 8)	# 36294-36301	 **attackbox here**
    sprite('Action_000_31', 8)	# 36302-36309	 **attackbox here**
    sprite('Action_000_32', 6)	# 36310-36315	 **attackbox here**
    sprite('Action_000_33', 2)	# 36316-36317	 **attackbox here**
    sprite('Action_000_34', 8)	# 36318-36325	 **attackbox here**
    sprite('Action_000_35', 8)	# 36326-36333	 **attackbox here**
    sprite('Action_000_36', 8)	# 36334-36341	 **attackbox here**
    sprite('Action_000_37', 8)	# 36342-36349	 **attackbox here**
    sprite('Action_000_38', 8)	# 36350-36357	 **attackbox here**
    sprite('Action_000_39', 8)	# 36358-36365	 **attackbox here**
    sprite('Action_000_40', 8)	# 36366-36373	 **attackbox here**
    sprite('Action_000_41', 8)	# 36374-36381	 **attackbox here**
    sprite('Action_000_42', 8)	# 36382-36389	 **attackbox here**
    sprite('Action_000_43', 8)	# 36390-36397	 **attackbox here**
    sprite('Action_000_44', 8)	# 36398-36405	 **attackbox here**
    sprite('Action_000_45', 8)	# 36406-36413	 **attackbox here**
    sprite('Action_000_46', 8)	# 36414-36421	 **attackbox here**
    sprite('Action_000_47', 8)	# 36422-36429	 **attackbox here**
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('Action_000_00', 1)	# 36430-36430	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)

    def upon_39():
        clearUponHandler(39)
        sendToLabel(175)
    label(171)
    sprite('Action_000_00', 8)	# 36431-36438	 **attackbox here**
    sprite('Action_000_01', 8)	# 36439-36446	 **attackbox here**
    sprite('Action_000_02', 8)	# 36447-36454	 **attackbox here**
    sprite('Action_000_03', 8)	# 36455-36462	 **attackbox here**
    sprite('Action_000_04', 8)	# 36463-36470	 **attackbox here**
    sprite('Action_000_05', 8)	# 36471-36478	 **attackbox here**
    sprite('Action_000_06', 8)	# 36479-36486	 **attackbox here**
    sprite('Action_000_07', 8)	# 36487-36494	 **attackbox here**
    sprite('Action_000_08', 8)	# 36495-36502	 **attackbox here**
    sprite('Action_000_09', 8)	# 36503-36510	 **attackbox here**
    sprite('Action_000_10', 8)	# 36511-36518	 **attackbox here**
    sprite('Action_000_11', 8)	# 36519-36526	 **attackbox here**
    sprite('Action_000_12', 8)	# 36527-36534	 **attackbox here**
    sprite('Action_000_13', 8)	# 36535-36542	 **attackbox here**
    sprite('Action_000_14', 8)	# 36543-36550	 **attackbox here**
    sprite('Action_000_15', 8)	# 36551-36558	 **attackbox here**
    sprite('Action_000_16', 8)	# 36559-36566	 **attackbox here**
    sprite('Action_000_17', 8)	# 36567-36574	 **attackbox here**
    sprite('Action_000_18', 8)	# 36575-36582	 **attackbox here**
    sprite('Action_000_19', 8)	# 36583-36590	 **attackbox here**
    sprite('Action_000_20', 8)	# 36591-36598	 **attackbox here**
    sprite('Action_000_21', 8)	# 36599-36606	 **attackbox here**
    sprite('Action_000_22', 8)	# 36607-36614	 **attackbox here**
    sprite('Action_000_23', 8)	# 36615-36622	 **attackbox here**
    sprite('Action_000_24', 8)	# 36623-36630	 **attackbox here**
    sprite('Action_000_25', 8)	# 36631-36638	 **attackbox here**
    sprite('Action_000_26', 8)	# 36639-36646	 **attackbox here**
    sprite('Action_000_27', 8)	# 36647-36654	 **attackbox here**
    sprite('Action_000_28', 8)	# 36655-36662	 **attackbox here**
    sprite('Action_000_29', 8)	# 36663-36670	 **attackbox here**
    sprite('Action_000_30', 8)	# 36671-36678	 **attackbox here**
    sprite('Action_000_31', 8)	# 36679-36686	 **attackbox here**
    sprite('Action_000_32', 6)	# 36687-36692	 **attackbox here**
    sprite('Action_000_33', 2)	# 36693-36694	 **attackbox here**
    sprite('Action_000_34', 8)	# 36695-36702	 **attackbox here**
    sprite('Action_000_35', 8)	# 36703-36710	 **attackbox here**
    sprite('Action_000_36', 8)	# 36711-36718	 **attackbox here**
    sprite('Action_000_37', 8)	# 36719-36726	 **attackbox here**
    sprite('Action_000_38', 8)	# 36727-36734	 **attackbox here**
    sprite('Action_000_39', 8)	# 36735-36742	 **attackbox here**
    sprite('Action_000_40', 8)	# 36743-36750	 **attackbox here**
    sprite('Action_000_41', 8)	# 36751-36758	 **attackbox here**
    sprite('Action_000_42', 8)	# 36759-36766	 **attackbox here**
    sprite('Action_000_43', 8)	# 36767-36774	 **attackbox here**
    sprite('Action_000_44', 8)	# 36775-36782	 **attackbox here**
    sprite('Action_000_45', 8)	# 36783-36790	 **attackbox here**
    sprite('Action_000_46', 8)	# 36791-36798	 **attackbox here**
    sprite('Action_000_47', 8)	# 36799-36806	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_000_49', 5)	# 36807-36811
    sprite('Action_000_50', 6)	# 36812-36817
    SFX_1('uyu601bha')
    sprite('Action_000_51', 6)	# 36818-36823
    sprite('Action_000_52', 3)	# 36824-36826	 **attackbox here**
    sprite('Action_000_53', 7)	# 36827-36833	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 36834-36838	 **attackbox here**
    sprite('Action_000_55', 8)	# 36839-36846	 **attackbox here**
    sprite('Action_000_56', 7)	# 36847-36853	 **attackbox here**
    sprite('Action_000_53', 7)	# 36854-36860	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 36861-36865	 **attackbox here**
    sprite('Action_000_55', 8)	# 36866-36873	 **attackbox here**
    sprite('Action_000_56', 7)	# 36874-36880	 **attackbox here**
    label(173)
    sprite('Action_000_53', 7)	# 36881-36887	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 36888-36892	 **attackbox here**
    sprite('Action_000_55', 8)	# 36893-36900	 **attackbox here**
    sprite('Action_000_56', 7)	# 36901-36907	 **attackbox here**
    if SLOT_97:
        _gotolabel(173)
    sprite('Action_000_57', 6)	# 36908-36913
    sprite('Action_000_58', 6)	# 36914-36919
    sprite('Action_000_59', 5)	# 36920-36924
    Unknown21007(24, 40)
    label(174)
    sprite('Action_000_00', 8)	# 36925-36932	 **attackbox here**
    sprite('Action_000_01', 8)	# 36933-36940	 **attackbox here**
    sprite('Action_000_02', 8)	# 36941-36948	 **attackbox here**
    sprite('Action_000_03', 8)	# 36949-36956	 **attackbox here**
    sprite('Action_000_04', 8)	# 36957-36964	 **attackbox here**
    sprite('Action_000_05', 8)	# 36965-36972	 **attackbox here**
    sprite('Action_000_06', 8)	# 36973-36980	 **attackbox here**
    sprite('Action_000_07', 8)	# 36981-36988	 **attackbox here**
    sprite('Action_000_08', 8)	# 36989-36996	 **attackbox here**
    sprite('Action_000_09', 8)	# 36997-37004	 **attackbox here**
    sprite('Action_000_10', 8)	# 37005-37012	 **attackbox here**
    sprite('Action_000_11', 8)	# 37013-37020	 **attackbox here**
    sprite('Action_000_12', 8)	# 37021-37028	 **attackbox here**
    sprite('Action_000_13', 8)	# 37029-37036	 **attackbox here**
    sprite('Action_000_14', 8)	# 37037-37044	 **attackbox here**
    sprite('Action_000_15', 8)	# 37045-37052	 **attackbox here**
    sprite('Action_000_16', 8)	# 37053-37060	 **attackbox here**
    sprite('Action_000_17', 8)	# 37061-37068	 **attackbox here**
    sprite('Action_000_18', 8)	# 37069-37076	 **attackbox here**
    sprite('Action_000_19', 8)	# 37077-37084	 **attackbox here**
    sprite('Action_000_20', 8)	# 37085-37092	 **attackbox here**
    sprite('Action_000_21', 8)	# 37093-37100	 **attackbox here**
    sprite('Action_000_22', 8)	# 37101-37108	 **attackbox here**
    sprite('Action_000_23', 8)	# 37109-37116	 **attackbox here**
    sprite('Action_000_24', 8)	# 37117-37124	 **attackbox here**
    sprite('Action_000_25', 8)	# 37125-37132	 **attackbox here**
    sprite('Action_000_26', 8)	# 37133-37140	 **attackbox here**
    sprite('Action_000_27', 8)	# 37141-37148	 **attackbox here**
    sprite('Action_000_28', 8)	# 37149-37156	 **attackbox here**
    sprite('Action_000_29', 8)	# 37157-37164	 **attackbox here**
    sprite('Action_000_30', 8)	# 37165-37172	 **attackbox here**
    sprite('Action_000_31', 8)	# 37173-37180	 **attackbox here**
    sprite('Action_000_32', 6)	# 37181-37186	 **attackbox here**
    sprite('Action_000_33', 2)	# 37187-37188	 **attackbox here**
    sprite('Action_000_34', 8)	# 37189-37196	 **attackbox here**
    sprite('Action_000_35', 8)	# 37197-37204	 **attackbox here**
    sprite('Action_000_36', 8)	# 37205-37212	 **attackbox here**
    sprite('Action_000_37', 8)	# 37213-37220	 **attackbox here**
    sprite('Action_000_38', 8)	# 37221-37228	 **attackbox here**
    sprite('Action_000_39', 8)	# 37229-37236	 **attackbox here**
    sprite('Action_000_40', 8)	# 37237-37244	 **attackbox here**
    sprite('Action_000_41', 8)	# 37245-37252	 **attackbox here**
    sprite('Action_000_42', 8)	# 37253-37260	 **attackbox here**
    sprite('Action_000_43', 8)	# 37261-37268	 **attackbox here**
    sprite('Action_000_44', 8)	# 37269-37276	 **attackbox here**
    sprite('Action_000_45', 8)	# 37277-37284	 **attackbox here**
    sprite('Action_000_46', 8)	# 37285-37292	 **attackbox here**
    sprite('Action_000_47', 8)	# 37293-37300	 **attackbox here**
    gotoLabel(174)
    label(175)
    sprite('Action_262_00', 5)	# 37301-37305
    SFX_1('uyu603bha')
    sprite('Action_262_01', 5)	# 37306-37310
    sprite('Action_262_02', 5)	# 37311-37315
    label(176)
    sprite('Action_262_03', 3)	# 37316-37318
    sprite('Action_262_04', 3)	# 37319-37321
    if SLOT_97:
        _gotolabel(176)
    sprite('Action_262_05', 5)	# 37322-37326
    sprite('Action_262_06', 5)	# 37327-37331
    Unknown23018(1)
    label(177)
    sprite('Action_000_00', 8)	# 37332-37339	 **attackbox here**
    sprite('Action_000_01', 8)	# 37340-37347	 **attackbox here**
    sprite('Action_000_02', 8)	# 37348-37355	 **attackbox here**
    sprite('Action_000_03', 8)	# 37356-37363	 **attackbox here**
    sprite('Action_000_04', 8)	# 37364-37371	 **attackbox here**
    sprite('Action_000_05', 8)	# 37372-37379	 **attackbox here**
    sprite('Action_000_06', 8)	# 37380-37387	 **attackbox here**
    sprite('Action_000_07', 8)	# 37388-37395	 **attackbox here**
    sprite('Action_000_08', 8)	# 37396-37403	 **attackbox here**
    sprite('Action_000_09', 8)	# 37404-37411	 **attackbox here**
    sprite('Action_000_10', 8)	# 37412-37419	 **attackbox here**
    sprite('Action_000_11', 8)	# 37420-37427	 **attackbox here**
    sprite('Action_000_12', 8)	# 37428-37435	 **attackbox here**
    sprite('Action_000_13', 8)	# 37436-37443	 **attackbox here**
    sprite('Action_000_14', 8)	# 37444-37451	 **attackbox here**
    sprite('Action_000_15', 8)	# 37452-37459	 **attackbox here**
    sprite('Action_000_16', 8)	# 37460-37467	 **attackbox here**
    sprite('Action_000_17', 8)	# 37468-37475	 **attackbox here**
    sprite('Action_000_18', 8)	# 37476-37483	 **attackbox here**
    sprite('Action_000_19', 8)	# 37484-37491	 **attackbox here**
    sprite('Action_000_20', 8)	# 37492-37499	 **attackbox here**
    sprite('Action_000_21', 8)	# 37500-37507	 **attackbox here**
    sprite('Action_000_22', 8)	# 37508-37515	 **attackbox here**
    sprite('Action_000_23', 8)	# 37516-37523	 **attackbox here**
    sprite('Action_000_24', 8)	# 37524-37531	 **attackbox here**
    sprite('Action_000_25', 8)	# 37532-37539	 **attackbox here**
    sprite('Action_000_26', 8)	# 37540-37547	 **attackbox here**
    sprite('Action_000_27', 8)	# 37548-37555	 **attackbox here**
    sprite('Action_000_28', 8)	# 37556-37563	 **attackbox here**
    sprite('Action_000_29', 8)	# 37564-37571	 **attackbox here**
    sprite('Action_000_30', 8)	# 37572-37579	 **attackbox here**
    sprite('Action_000_31', 8)	# 37580-37587	 **attackbox here**
    sprite('Action_000_32', 6)	# 37588-37593	 **attackbox here**
    sprite('Action_000_33', 2)	# 37594-37595	 **attackbox here**
    sprite('Action_000_34', 8)	# 37596-37603	 **attackbox here**
    sprite('Action_000_35', 8)	# 37604-37611	 **attackbox here**
    sprite('Action_000_36', 8)	# 37612-37619	 **attackbox here**
    sprite('Action_000_37', 8)	# 37620-37627	 **attackbox here**
    sprite('Action_000_38', 8)	# 37628-37635	 **attackbox here**
    sprite('Action_000_39', 8)	# 37636-37643	 **attackbox here**
    sprite('Action_000_40', 8)	# 37644-37651	 **attackbox here**
    sprite('Action_000_41', 8)	# 37652-37659	 **attackbox here**
    sprite('Action_000_42', 8)	# 37660-37667	 **attackbox here**
    sprite('Action_000_43', 8)	# 37668-37675	 **attackbox here**
    sprite('Action_000_44', 8)	# 37676-37683	 **attackbox here**
    sprite('Action_000_45', 8)	# 37684-37691	 **attackbox here**
    sprite('Action_000_46', 8)	# 37692-37699	 **attackbox here**
    sprite('Action_000_47', 8)	# 37700-37707	 **attackbox here**
    gotoLabel(177)
    ExitState()
    label(180)
    sprite('Action_000_00', 1)	# 37708-37708	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('Action_000_00', 8)	# 37709-37716	 **attackbox here**
    sprite('Action_000_01', 8)	# 37717-37724	 **attackbox here**
    sprite('Action_000_02', 8)	# 37725-37732	 **attackbox here**
    sprite('Action_000_03', 8)	# 37733-37740	 **attackbox here**
    sprite('Action_000_04', 8)	# 37741-37748	 **attackbox here**
    sprite('Action_000_05', 8)	# 37749-37756	 **attackbox here**
    sprite('Action_000_06', 8)	# 37757-37764	 **attackbox here**
    sprite('Action_000_07', 8)	# 37765-37772	 **attackbox here**
    sprite('Action_000_08', 8)	# 37773-37780	 **attackbox here**
    sprite('Action_000_09', 8)	# 37781-37788	 **attackbox here**
    sprite('Action_000_10', 8)	# 37789-37796	 **attackbox here**
    sprite('Action_000_11', 8)	# 37797-37804	 **attackbox here**
    sprite('Action_000_12', 8)	# 37805-37812	 **attackbox here**
    sprite('Action_000_13', 8)	# 37813-37820	 **attackbox here**
    sprite('Action_000_14', 8)	# 37821-37828	 **attackbox here**
    sprite('Action_000_15', 8)	# 37829-37836	 **attackbox here**
    sprite('Action_000_16', 8)	# 37837-37844	 **attackbox here**
    sprite('Action_000_17', 8)	# 37845-37852	 **attackbox here**
    sprite('Action_000_18', 8)	# 37853-37860	 **attackbox here**
    sprite('Action_000_19', 8)	# 37861-37868	 **attackbox here**
    sprite('Action_000_20', 8)	# 37869-37876	 **attackbox here**
    sprite('Action_000_21', 8)	# 37877-37884	 **attackbox here**
    sprite('Action_000_22', 8)	# 37885-37892	 **attackbox here**
    sprite('Action_000_23', 8)	# 37893-37900	 **attackbox here**
    sprite('Action_000_24', 8)	# 37901-37908	 **attackbox here**
    sprite('Action_000_25', 8)	# 37909-37916	 **attackbox here**
    sprite('Action_000_26', 8)	# 37917-37924	 **attackbox here**
    sprite('Action_000_27', 8)	# 37925-37932	 **attackbox here**
    sprite('Action_000_28', 8)	# 37933-37940	 **attackbox here**
    sprite('Action_000_29', 8)	# 37941-37948	 **attackbox here**
    sprite('Action_000_30', 8)	# 37949-37956	 **attackbox here**
    sprite('Action_000_31', 8)	# 37957-37964	 **attackbox here**
    sprite('Action_000_32', 6)	# 37965-37970	 **attackbox here**
    sprite('Action_000_33', 2)	# 37971-37972	 **attackbox here**
    sprite('Action_000_34', 8)	# 37973-37980	 **attackbox here**
    sprite('Action_000_35', 8)	# 37981-37988	 **attackbox here**
    sprite('Action_000_36', 8)	# 37989-37996	 **attackbox here**
    sprite('Action_000_37', 8)	# 37997-38004	 **attackbox here**
    sprite('Action_000_38', 8)	# 38005-38012	 **attackbox here**
    sprite('Action_000_39', 8)	# 38013-38020	 **attackbox here**
    sprite('Action_000_40', 8)	# 38021-38028	 **attackbox here**
    sprite('Action_000_41', 8)	# 38029-38036	 **attackbox here**
    sprite('Action_000_42', 8)	# 38037-38044	 **attackbox here**
    sprite('Action_000_43', 8)	# 38045-38052	 **attackbox here**
    sprite('Action_000_44', 8)	# 38053-38060	 **attackbox here**
    sprite('Action_000_45', 8)	# 38061-38068	 **attackbox here**
    sprite('Action_000_46', 8)	# 38069-38076	 **attackbox here**
    sprite('Action_000_47', 8)	# 38077-38084	 **attackbox here**
    gotoLabel(181)
    label(182)
    sprite('Action_000_49', 5)	# 38085-38089
    sprite('Action_000_50', 6)	# 38090-38095
    SFX_1('uyu601rrb')
    sprite('Action_000_51', 6)	# 38096-38101
    sprite('Action_000_52', 3)	# 38102-38104	 **attackbox here**
    sprite('Action_000_53', 7)	# 38105-38111	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 38112-38116	 **attackbox here**
    sprite('Action_000_55', 8)	# 38117-38124	 **attackbox here**
    sprite('Action_000_56', 7)	# 38125-38131	 **attackbox here**
    sprite('Action_000_53', 7)	# 38132-38138	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 38139-38143	 **attackbox here**
    sprite('Action_000_55', 8)	# 38144-38151	 **attackbox here**
    sprite('Action_000_56', 7)	# 38152-38158	 **attackbox here**
    label(183)
    sprite('Action_000_53', 7)	# 38159-38165	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 38166-38170	 **attackbox here**
    sprite('Action_000_55', 8)	# 38171-38178	 **attackbox here**
    sprite('Action_000_56', 7)	# 38179-38185	 **attackbox here**
    if SLOT_97:
        _gotolabel(183)
    sprite('Action_000_57', 6)	# 38186-38191
    sprite('Action_000_58', 6)	# 38192-38197
    sprite('Action_000_59', 5)	# 38198-38202
    Unknown23018(1)
    label(184)
    sprite('Action_000_00', 8)	# 38203-38210	 **attackbox here**
    sprite('Action_000_01', 8)	# 38211-38218	 **attackbox here**
    sprite('Action_000_02', 8)	# 38219-38226	 **attackbox here**
    sprite('Action_000_03', 8)	# 38227-38234	 **attackbox here**
    sprite('Action_000_04', 8)	# 38235-38242	 **attackbox here**
    sprite('Action_000_05', 8)	# 38243-38250	 **attackbox here**
    sprite('Action_000_06', 8)	# 38251-38258	 **attackbox here**
    sprite('Action_000_07', 8)	# 38259-38266	 **attackbox here**
    sprite('Action_000_08', 8)	# 38267-38274	 **attackbox here**
    sprite('Action_000_09', 8)	# 38275-38282	 **attackbox here**
    sprite('Action_000_10', 8)	# 38283-38290	 **attackbox here**
    sprite('Action_000_11', 8)	# 38291-38298	 **attackbox here**
    sprite('Action_000_12', 8)	# 38299-38306	 **attackbox here**
    sprite('Action_000_13', 8)	# 38307-38314	 **attackbox here**
    sprite('Action_000_14', 8)	# 38315-38322	 **attackbox here**
    sprite('Action_000_15', 8)	# 38323-38330	 **attackbox here**
    sprite('Action_000_16', 8)	# 38331-38338	 **attackbox here**
    sprite('Action_000_17', 8)	# 38339-38346	 **attackbox here**
    sprite('Action_000_18', 8)	# 38347-38354	 **attackbox here**
    sprite('Action_000_19', 8)	# 38355-38362	 **attackbox here**
    sprite('Action_000_20', 8)	# 38363-38370	 **attackbox here**
    sprite('Action_000_21', 8)	# 38371-38378	 **attackbox here**
    sprite('Action_000_22', 8)	# 38379-38386	 **attackbox here**
    sprite('Action_000_23', 8)	# 38387-38394	 **attackbox here**
    sprite('Action_000_24', 8)	# 38395-38402	 **attackbox here**
    sprite('Action_000_25', 8)	# 38403-38410	 **attackbox here**
    sprite('Action_000_26', 8)	# 38411-38418	 **attackbox here**
    sprite('Action_000_27', 8)	# 38419-38426	 **attackbox here**
    sprite('Action_000_28', 8)	# 38427-38434	 **attackbox here**
    sprite('Action_000_29', 8)	# 38435-38442	 **attackbox here**
    sprite('Action_000_30', 8)	# 38443-38450	 **attackbox here**
    sprite('Action_000_31', 8)	# 38451-38458	 **attackbox here**
    sprite('Action_000_32', 6)	# 38459-38464	 **attackbox here**
    sprite('Action_000_33', 2)	# 38465-38466	 **attackbox here**
    sprite('Action_000_34', 8)	# 38467-38474	 **attackbox here**
    sprite('Action_000_35', 8)	# 38475-38482	 **attackbox here**
    sprite('Action_000_36', 8)	# 38483-38490	 **attackbox here**
    sprite('Action_000_37', 8)	# 38491-38498	 **attackbox here**
    sprite('Action_000_38', 8)	# 38499-38506	 **attackbox here**
    sprite('Action_000_39', 8)	# 38507-38514	 **attackbox here**
    sprite('Action_000_40', 8)	# 38515-38522	 **attackbox here**
    sprite('Action_000_41', 8)	# 38523-38530	 **attackbox here**
    sprite('Action_000_42', 8)	# 38531-38538	 **attackbox here**
    sprite('Action_000_43', 8)	# 38539-38546	 **attackbox here**
    sprite('Action_000_44', 8)	# 38547-38554	 **attackbox here**
    sprite('Action_000_45', 8)	# 38555-38562	 **attackbox here**
    sprite('Action_000_46', 8)	# 38563-38570	 **attackbox here**
    sprite('Action_000_47', 8)	# 38571-38578	 **attackbox here**
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('Action_000_00', 1)	# 38579-38579	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Action_000_00', 8)	# 38580-38587	 **attackbox here**
    sprite('Action_000_01', 8)	# 38588-38595	 **attackbox here**
    sprite('Action_000_02', 8)	# 38596-38603	 **attackbox here**
    sprite('Action_000_03', 8)	# 38604-38611	 **attackbox here**
    sprite('Action_000_04', 8)	# 38612-38619	 **attackbox here**
    sprite('Action_000_05', 8)	# 38620-38627	 **attackbox here**
    sprite('Action_000_06', 8)	# 38628-38635	 **attackbox here**
    sprite('Action_000_07', 8)	# 38636-38643	 **attackbox here**
    sprite('Action_000_08', 8)	# 38644-38651	 **attackbox here**
    sprite('Action_000_09', 8)	# 38652-38659	 **attackbox here**
    sprite('Action_000_10', 8)	# 38660-38667	 **attackbox here**
    sprite('Action_000_11', 8)	# 38668-38675	 **attackbox here**
    sprite('Action_000_12', 8)	# 38676-38683	 **attackbox here**
    sprite('Action_000_13', 8)	# 38684-38691	 **attackbox here**
    sprite('Action_000_14', 8)	# 38692-38699	 **attackbox here**
    sprite('Action_000_15', 8)	# 38700-38707	 **attackbox here**
    sprite('Action_000_16', 8)	# 38708-38715	 **attackbox here**
    sprite('Action_000_17', 8)	# 38716-38723	 **attackbox here**
    sprite('Action_000_18', 8)	# 38724-38731	 **attackbox here**
    sprite('Action_000_19', 8)	# 38732-38739	 **attackbox here**
    sprite('Action_000_20', 8)	# 38740-38747	 **attackbox here**
    sprite('Action_000_21', 8)	# 38748-38755	 **attackbox here**
    sprite('Action_000_22', 8)	# 38756-38763	 **attackbox here**
    sprite('Action_000_23', 8)	# 38764-38771	 **attackbox here**
    sprite('Action_000_24', 8)	# 38772-38779	 **attackbox here**
    sprite('Action_000_25', 8)	# 38780-38787	 **attackbox here**
    sprite('Action_000_26', 8)	# 38788-38795	 **attackbox here**
    sprite('Action_000_27', 8)	# 38796-38803	 **attackbox here**
    sprite('Action_000_28', 8)	# 38804-38811	 **attackbox here**
    sprite('Action_000_29', 8)	# 38812-38819	 **attackbox here**
    sprite('Action_000_30', 8)	# 38820-38827	 **attackbox here**
    sprite('Action_000_31', 8)	# 38828-38835	 **attackbox here**
    sprite('Action_000_32', 6)	# 38836-38841	 **attackbox here**
    sprite('Action_000_33', 2)	# 38842-38843	 **attackbox here**
    sprite('Action_000_34', 8)	# 38844-38851	 **attackbox here**
    sprite('Action_000_35', 8)	# 38852-38859	 **attackbox here**
    sprite('Action_000_36', 8)	# 38860-38867	 **attackbox here**
    sprite('Action_000_37', 8)	# 38868-38875	 **attackbox here**
    sprite('Action_000_38', 8)	# 38876-38883	 **attackbox here**
    sprite('Action_000_39', 8)	# 38884-38891	 **attackbox here**
    sprite('Action_000_40', 8)	# 38892-38899	 **attackbox here**
    sprite('Action_000_41', 8)	# 38900-38907	 **attackbox here**
    sprite('Action_000_42', 8)	# 38908-38915	 **attackbox here**
    sprite('Action_000_43', 8)	# 38916-38923	 **attackbox here**
    sprite('Action_000_44', 8)	# 38924-38931	 **attackbox here**
    sprite('Action_000_45', 8)	# 38932-38939	 **attackbox here**
    sprite('Action_000_46', 8)	# 38940-38947	 **attackbox here**
    sprite('Action_000_47', 8)	# 38948-38955	 **attackbox here**
    gotoLabel(191)
    label(192)
    sprite('Action_000_49', 5)	# 38956-38960
    sprite('Action_000_50', 6)	# 38961-38966
    SFX_1('uyu601pla')
    sprite('Action_000_51', 6)	# 38967-38972
    sprite('Action_000_52', 3)	# 38973-38975	 **attackbox here**
    sprite('Action_000_53', 7)	# 38976-38982	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 38983-38987	 **attackbox here**
    sprite('Action_000_55', 8)	# 38988-38995	 **attackbox here**
    sprite('Action_000_56', 7)	# 38996-39002	 **attackbox here**
    sprite('Action_000_53', 7)	# 39003-39009	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 39010-39014	 **attackbox here**
    sprite('Action_000_55', 8)	# 39015-39022	 **attackbox here**
    sprite('Action_000_56', 7)	# 39023-39029	 **attackbox here**
    label(193)
    sprite('Action_000_53', 7)	# 39030-39036	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 39037-39041	 **attackbox here**
    sprite('Action_000_55', 8)	# 39042-39049	 **attackbox here**
    sprite('Action_000_56', 7)	# 39050-39056	 **attackbox here**
    if SLOT_97:
        _gotolabel(193)
    sprite('Action_000_57', 6)	# 39057-39062
    sprite('Action_000_58', 6)	# 39063-39068
    sprite('Action_000_59', 5)	# 39069-39073
    Unknown23018(1)
    label(194)
    sprite('Action_000_00', 8)	# 39074-39081	 **attackbox here**
    sprite('Action_000_01', 8)	# 39082-39089	 **attackbox here**
    sprite('Action_000_02', 8)	# 39090-39097	 **attackbox here**
    sprite('Action_000_03', 8)	# 39098-39105	 **attackbox here**
    sprite('Action_000_04', 8)	# 39106-39113	 **attackbox here**
    sprite('Action_000_05', 8)	# 39114-39121	 **attackbox here**
    sprite('Action_000_06', 8)	# 39122-39129	 **attackbox here**
    sprite('Action_000_07', 8)	# 39130-39137	 **attackbox here**
    sprite('Action_000_08', 8)	# 39138-39145	 **attackbox here**
    sprite('Action_000_09', 8)	# 39146-39153	 **attackbox here**
    sprite('Action_000_10', 8)	# 39154-39161	 **attackbox here**
    sprite('Action_000_11', 8)	# 39162-39169	 **attackbox here**
    sprite('Action_000_12', 8)	# 39170-39177	 **attackbox here**
    sprite('Action_000_13', 8)	# 39178-39185	 **attackbox here**
    sprite('Action_000_14', 8)	# 39186-39193	 **attackbox here**
    sprite('Action_000_15', 8)	# 39194-39201	 **attackbox here**
    sprite('Action_000_16', 8)	# 39202-39209	 **attackbox here**
    sprite('Action_000_17', 8)	# 39210-39217	 **attackbox here**
    sprite('Action_000_18', 8)	# 39218-39225	 **attackbox here**
    sprite('Action_000_19', 8)	# 39226-39233	 **attackbox here**
    sprite('Action_000_20', 8)	# 39234-39241	 **attackbox here**
    sprite('Action_000_21', 8)	# 39242-39249	 **attackbox here**
    sprite('Action_000_22', 8)	# 39250-39257	 **attackbox here**
    sprite('Action_000_23', 8)	# 39258-39265	 **attackbox here**
    sprite('Action_000_24', 8)	# 39266-39273	 **attackbox here**
    sprite('Action_000_25', 8)	# 39274-39281	 **attackbox here**
    sprite('Action_000_26', 8)	# 39282-39289	 **attackbox here**
    sprite('Action_000_27', 8)	# 39290-39297	 **attackbox here**
    sprite('Action_000_28', 8)	# 39298-39305	 **attackbox here**
    sprite('Action_000_29', 8)	# 39306-39313	 **attackbox here**
    sprite('Action_000_30', 8)	# 39314-39321	 **attackbox here**
    sprite('Action_000_31', 8)	# 39322-39329	 **attackbox here**
    sprite('Action_000_32', 6)	# 39330-39335	 **attackbox here**
    sprite('Action_000_33', 2)	# 39336-39337	 **attackbox here**
    sprite('Action_000_34', 8)	# 39338-39345	 **attackbox here**
    sprite('Action_000_35', 8)	# 39346-39353	 **attackbox here**
    sprite('Action_000_36', 8)	# 39354-39361	 **attackbox here**
    sprite('Action_000_37', 8)	# 39362-39369	 **attackbox here**
    sprite('Action_000_38', 8)	# 39370-39377	 **attackbox here**
    sprite('Action_000_39', 8)	# 39378-39385	 **attackbox here**
    sprite('Action_000_40', 8)	# 39386-39393	 **attackbox here**
    sprite('Action_000_41', 8)	# 39394-39401	 **attackbox here**
    sprite('Action_000_42', 8)	# 39402-39409	 **attackbox here**
    sprite('Action_000_43', 8)	# 39410-39417	 **attackbox here**
    sprite('Action_000_44', 8)	# 39418-39425	 **attackbox here**
    sprite('Action_000_45', 8)	# 39426-39433	 **attackbox here**
    sprite('Action_000_46', 8)	# 39434-39441	 **attackbox here**
    sprite('Action_000_47', 8)	# 39442-39449	 **attackbox here**
    gotoLabel(194)
    ExitState()
    label(200)
    sprite('Action_000_00', 1)	# 39450-39450	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 8)	# 39451-39458	 **attackbox here**
    sprite('Action_000_01', 8)	# 39459-39466	 **attackbox here**
    sprite('Action_000_02', 8)	# 39467-39474	 **attackbox here**
    sprite('Action_000_03', 8)	# 39475-39482	 **attackbox here**
    sprite('Action_000_04', 8)	# 39483-39490	 **attackbox here**
    sprite('Action_000_05', 8)	# 39491-39498	 **attackbox here**
    sprite('Action_000_06', 8)	# 39499-39506	 **attackbox here**
    sprite('Action_000_07', 8)	# 39507-39514	 **attackbox here**
    sprite('Action_000_08', 8)	# 39515-39522	 **attackbox here**
    sprite('Action_000_09', 8)	# 39523-39530	 **attackbox here**
    sprite('Action_000_10', 8)	# 39531-39538	 **attackbox here**
    sprite('Action_000_11', 8)	# 39539-39546	 **attackbox here**
    sprite('Action_000_12', 8)	# 39547-39554	 **attackbox here**
    sprite('Action_000_13', 8)	# 39555-39562	 **attackbox here**
    sprite('Action_000_14', 8)	# 39563-39570	 **attackbox here**
    sprite('Action_000_15', 8)	# 39571-39578	 **attackbox here**
    sprite('Action_000_16', 8)	# 39579-39586	 **attackbox here**
    sprite('Action_000_17', 8)	# 39587-39594	 **attackbox here**
    sprite('Action_000_18', 8)	# 39595-39602	 **attackbox here**
    sprite('Action_000_19', 8)	# 39603-39610	 **attackbox here**
    sprite('Action_000_20', 8)	# 39611-39618	 **attackbox here**
    sprite('Action_000_21', 8)	# 39619-39626	 **attackbox here**
    sprite('Action_000_22', 8)	# 39627-39634	 **attackbox here**
    sprite('Action_000_23', 8)	# 39635-39642	 **attackbox here**
    sprite('Action_000_24', 8)	# 39643-39650	 **attackbox here**
    sprite('Action_000_25', 8)	# 39651-39658	 **attackbox here**
    sprite('Action_000_26', 8)	# 39659-39666	 **attackbox here**
    sprite('Action_000_27', 8)	# 39667-39674	 **attackbox here**
    sprite('Action_000_28', 8)	# 39675-39682	 **attackbox here**
    sprite('Action_000_29', 8)	# 39683-39690	 **attackbox here**
    sprite('Action_000_30', 8)	# 39691-39698	 **attackbox here**
    sprite('Action_000_31', 8)	# 39699-39706	 **attackbox here**
    sprite('Action_000_32', 6)	# 39707-39712	 **attackbox here**
    sprite('Action_000_33', 2)	# 39713-39714	 **attackbox here**
    sprite('Action_000_34', 8)	# 39715-39722	 **attackbox here**
    sprite('Action_000_35', 8)	# 39723-39730	 **attackbox here**
    sprite('Action_000_36', 8)	# 39731-39738	 **attackbox here**
    sprite('Action_000_37', 8)	# 39739-39746	 **attackbox here**
    sprite('Action_000_38', 8)	# 39747-39754	 **attackbox here**
    sprite('Action_000_39', 8)	# 39755-39762	 **attackbox here**
    sprite('Action_000_40', 8)	# 39763-39770	 **attackbox here**
    sprite('Action_000_41', 8)	# 39771-39778	 **attackbox here**
    sprite('Action_000_42', 8)	# 39779-39786	 **attackbox here**
    sprite('Action_000_43', 8)	# 39787-39794	 **attackbox here**
    sprite('Action_000_44', 8)	# 39795-39802	 **attackbox here**
    sprite('Action_000_45', 8)	# 39803-39810	 **attackbox here**
    sprite('Action_000_46', 8)	# 39811-39818	 **attackbox here**
    sprite('Action_000_47', 8)	# 39819-39826	 **attackbox here**
    gotoLabel(201)
    label(202)
    sprite('Action_000_49', 5)	# 39827-39831
    sprite('Action_000_50', 6)	# 39832-39837
    SFX_1('uyu601biz')
    sprite('Action_000_51', 6)	# 39838-39843
    sprite('Action_000_52', 3)	# 39844-39846	 **attackbox here**
    sprite('Action_000_53', 7)	# 39847-39853	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 39854-39858	 **attackbox here**
    sprite('Action_000_55', 8)	# 39859-39866	 **attackbox here**
    sprite('Action_000_56', 7)	# 39867-39873	 **attackbox here**
    sprite('Action_000_53', 7)	# 39874-39880	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 39881-39885	 **attackbox here**
    sprite('Action_000_55', 8)	# 39886-39893	 **attackbox here**
    sprite('Action_000_56', 7)	# 39894-39900	 **attackbox here**
    label(203)
    sprite('Action_000_53', 7)	# 39901-39907	 **attackbox here**
    SFX_3('SE243_Smoke1')
    sprite('Action_000_54', 5)	# 39908-39912	 **attackbox here**
    sprite('Action_000_55', 8)	# 39913-39920	 **attackbox here**
    sprite('Action_000_56', 7)	# 39921-39927	 **attackbox here**
    if SLOT_97:
        _gotolabel(203)
    sprite('Action_000_57', 6)	# 39928-39933
    sprite('Action_000_58', 6)	# 39934-39939
    sprite('Action_000_59', 5)	# 39940-39944
    Unknown23018(1)
    label(204)
    sprite('Action_000_00', 8)	# 39945-39952	 **attackbox here**
    sprite('Action_000_01', 8)	# 39953-39960	 **attackbox here**
    sprite('Action_000_02', 8)	# 39961-39968	 **attackbox here**
    sprite('Action_000_03', 8)	# 39969-39976	 **attackbox here**
    sprite('Action_000_04', 8)	# 39977-39984	 **attackbox here**
    sprite('Action_000_05', 8)	# 39985-39992	 **attackbox here**
    sprite('Action_000_06', 8)	# 39993-40000	 **attackbox here**
    sprite('Action_000_07', 8)	# 40001-40008	 **attackbox here**
    sprite('Action_000_08', 8)	# 40009-40016	 **attackbox here**
    sprite('Action_000_09', 8)	# 40017-40024	 **attackbox here**
    sprite('Action_000_10', 8)	# 40025-40032	 **attackbox here**
    sprite('Action_000_11', 8)	# 40033-40040	 **attackbox here**
    sprite('Action_000_12', 8)	# 40041-40048	 **attackbox here**
    sprite('Action_000_13', 8)	# 40049-40056	 **attackbox here**
    sprite('Action_000_14', 8)	# 40057-40064	 **attackbox here**
    sprite('Action_000_15', 8)	# 40065-40072	 **attackbox here**
    sprite('Action_000_16', 8)	# 40073-40080	 **attackbox here**
    sprite('Action_000_17', 8)	# 40081-40088	 **attackbox here**
    sprite('Action_000_18', 8)	# 40089-40096	 **attackbox here**
    sprite('Action_000_19', 8)	# 40097-40104	 **attackbox here**
    sprite('Action_000_20', 8)	# 40105-40112	 **attackbox here**
    sprite('Action_000_21', 8)	# 40113-40120	 **attackbox here**
    sprite('Action_000_22', 8)	# 40121-40128	 **attackbox here**
    sprite('Action_000_23', 8)	# 40129-40136	 **attackbox here**
    sprite('Action_000_24', 8)	# 40137-40144	 **attackbox here**
    sprite('Action_000_25', 8)	# 40145-40152	 **attackbox here**
    sprite('Action_000_26', 8)	# 40153-40160	 **attackbox here**
    sprite('Action_000_27', 8)	# 40161-40168	 **attackbox here**
    sprite('Action_000_28', 8)	# 40169-40176	 **attackbox here**
    sprite('Action_000_29', 8)	# 40177-40184	 **attackbox here**
    sprite('Action_000_30', 8)	# 40185-40192	 **attackbox here**
    sprite('Action_000_31', 8)	# 40193-40200	 **attackbox here**
    sprite('Action_000_32', 6)	# 40201-40206	 **attackbox here**
    sprite('Action_000_33', 2)	# 40207-40208	 **attackbox here**
    sprite('Action_000_34', 8)	# 40209-40216	 **attackbox here**
    sprite('Action_000_35', 8)	# 40217-40224	 **attackbox here**
    sprite('Action_000_36', 8)	# 40225-40232	 **attackbox here**
    sprite('Action_000_37', 8)	# 40233-40240	 **attackbox here**
    sprite('Action_000_38', 8)	# 40241-40248	 **attackbox here**
    sprite('Action_000_39', 8)	# 40249-40256	 **attackbox here**
    sprite('Action_000_40', 8)	# 40257-40264	 **attackbox here**
    sprite('Action_000_41', 8)	# 40265-40272	 **attackbox here**
    sprite('Action_000_42', 8)	# 40273-40280	 **attackbox here**
    sprite('Action_000_43', 8)	# 40281-40288	 **attackbox here**
    sprite('Action_000_44', 8)	# 40289-40296	 **attackbox here**
    sprite('Action_000_45', 8)	# 40297-40304	 **attackbox here**
    sprite('Action_000_46', 8)	# 40305-40312	 **attackbox here**
    sprite('Action_000_47', 8)	# 40313-40320	 **attackbox here**
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
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 700000):
                    if (SLOT_145 >= 250000):
                        sendToLabel(110)
                        clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 900000):
                    if (SLOT_145 >= 100000):
                        sendToLabel(140)
                        clearUponHandler(3)
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('biz'):
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
            if (not SLOT_108):
                if (SLOT_19 <= 900000):
                    if (SLOT_19 >= 200000):
                        if random_(2, 0, 50):
                            sendToLabel(10)
                        else:
                            sendToLabel(0)
            else:
                sendToLabel(0)
        else:
            sendToLabel(0)
    label(0)
    sprite('Action_053_00', 5)	# 5-9
    sprite('Action_053_01', 5)	# 10-14	 **attackbox here**
    sprite('Action_053_02', 7)	# 15-21	 **attackbox here**
    sprite('Action_053_03', 11)	# 22-32	 **attackbox here**
    sprite('Action_053_04', 16)	# 33-48	 **attackbox here**
    sprite('Action_053_05', 6)	# 49-54	 **attackbox here**
    sprite('Action_053_06', 5)	# 55-59	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 60-64	 **attackbox here**
    teleportRelativeX(-50000)
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uyu524', 100, 896891253, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uyu404_0', 100, 880114037, 828322864, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uyu520', 100, 896891253, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 65-69	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 70-76	 **attackbox here**
    sprite('Action_053_10', 8)	# 77-84	 **attackbox here**
    sprite('Action_053_11', 6)	# 85-90	 **attackbox here**
    Unknown23018(1)
    label(1)
    sprite('Action_053_12', 5)	# 91-95	 **attackbox here**
    sprite('Action_053_13', 5)	# 96-100	 **attackbox here**
    sprite('Action_053_14', 5)	# 101-105	 **attackbox here**
    gotoLabel(1)
    label(10)
    sprite('Action_010_00', 1)	# 106-106
    physicsXImpulse(8000)
    Unknown2053(0)
    Unknown2034(0)
    Unknown20000(1)

    def upon_3():
        if (SLOT_29 < 200000):
            clearUponHandler(3)
            Unknown1084(1)
            sendToLabel(12)
    label(11)
    sprite('Action_010_00', 5)	# 107-111
    sprite('Action_010_01', 5)	# 112-116
    sprite('Action_010_02', 5)	# 117-121
    sprite('Action_010_03', 6)	# 122-127
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_04', 5)	# 128-132
    sprite('Action_010_05', 5)	# 133-137
    sprite('Action_010_06', 5)	# 138-142
    sprite('Action_010_07', 5)	# 143-147
    sprite('Action_010_08', 5)	# 148-152
    sprite('Action_010_09', 6)	# 153-158
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_10', 5)	# 159-163
    sprite('Action_010_11', 5)	# 164-168
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('Action_052_13', 6)	# 169-174
    if SLOT_158:
        Unknown7006('uyu522', 100, 896891253, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_052_14', 6)	# 175-180
    sprite('Action_052_15', 6)	# 181-186
    sprite('Action_052_16', 7)	# 187-193
    Unknown23018(1)
    sprite('Action_052_17', 32767)	# 194-32960	 **attackbox here**
    label(100)
    sprite('Action_052_13', 6)	# 32961-32966
    SFX_1('uyu700bjn')
    sprite('Action_052_14', 6)	# 32967-32972
    sprite('Action_052_15', 6)	# 32973-32978
    sprite('Action_052_16', 7)	# 32979-32985
    label(101)
    sprite('Action_052_17', 1)	# 32986-32986	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_052_17', 20)	# 32987-33006	 **attackbox here**
    sprite('Action_052_17', 32767)	# 33007-65773	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(110)
    sprite('Action_010_00', 1)	# 65774-65774
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
    physicsXImpulse(8000)
    Unknown2053(0)
    Unknown2034(0)

    def upon_3():
        if (SLOT_145 < 110000):
            clearUponHandler(3)
            Unknown1084(1)
            sendToLabel(112)
    Unknown2019(-500)
    label(111)
    sprite('Action_010_00', 5)	# 65775-65779
    sprite('Action_010_01', 5)	# 65780-65784
    sprite('Action_010_02', 5)	# 65785-65789
    sprite('Action_010_03', 6)	# 65790-65795
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_04', 5)	# 65796-65800
    sprite('Action_010_05', 5)	# 65801-65805
    sprite('Action_010_06', 5)	# 65806-65810
    sprite('Action_010_07', 5)	# 65811-65815
    sprite('Action_010_08', 5)	# 65816-65820
    sprite('Action_010_09', 6)	# 65821-65826
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_10', 5)	# 65827-65831
    sprite('Action_010_11', 5)	# 65832-65836
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('Yuz636_00', 30)	# 65837-65866
    SFX_1('uyu700bpt')
    sprite('Yuz636_01', 6)	# 65867-65872
    Unknown21007(24, 40)
    label(113)
    sprite('Yuz636_02', 6)	# 65873-65878	 **attackbox here**
    sprite('Yuz636_03', 6)	# 65879-65884	 **attackbox here**
    sprite('Yuz636_04', 6)	# 65885-65890	 **attackbox here**
    sprite('Yuz636_03', 6)	# 65891-65896	 **attackbox here**
    if SLOT_97:
        _gotolabel(113)
    sprite('Yuz636_02', 1)	# 65897-65897	 **attackbox here**
    Unknown21007(24, 39)
    Unknown21011(240)
    label(114)
    sprite('Yuz636_02', 6)	# 65898-65903	 **attackbox here**
    sprite('Yuz636_03', 6)	# 65904-65909	 **attackbox here**
    sprite('Yuz636_04', 6)	# 65910-65915	 **attackbox here**
    sprite('Yuz636_03', 6)	# 65916-65921	 **attackbox here**
    gotoLabel(114)
    label(120)
    sprite('Action_053_00', 5)	# 65922-65926
    sprite('Action_053_01', 5)	# 65927-65931	 **attackbox here**
    sprite('Action_053_02', 7)	# 65932-65938	 **attackbox here**
    sprite('Action_053_03', 11)	# 65939-65949	 **attackbox here**
    sprite('Action_053_04', 16)	# 65950-65965	 **attackbox here**
    sprite('Action_053_05', 6)	# 65966-65971	 **attackbox here**
    sprite('Action_053_06', 5)	# 65972-65976	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 65977-65981	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_1('uyu700pbc')
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 65982-65986	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 65987-65993	 **attackbox here**
    sprite('Action_053_10', 8)	# 65994-66001	 **attackbox here**
    sprite('Action_053_11', 6)	# 66002-66007	 **attackbox here**
    label(121)
    sprite('Action_053_12', 5)	# 66008-66012	 **attackbox here**
    sprite('Action_053_13', 5)	# 66013-66017	 **attackbox here**
    sprite('Action_053_14', 5)	# 66018-66022	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_053_14', 1)	# 66023-66023	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    label(122)
    sprite('Action_053_12', 5)	# 66024-66028	 **attackbox here**
    sprite('Action_053_13', 5)	# 66029-66033	 **attackbox here**
    sprite('Action_053_14', 5)	# 66034-66038	 **attackbox here**
    gotoLabel(122)
    label(130)
    sprite('Action_053_00', 5)	# 66039-66043
    sprite('Action_053_01', 5)	# 66044-66048	 **attackbox here**
    sprite('Action_053_02', 7)	# 66049-66055	 **attackbox here**
    sprite('Action_053_03', 11)	# 66056-66066	 **attackbox here**
    sprite('Action_053_04', 16)	# 66067-66082	 **attackbox here**
    sprite('Action_053_05', 6)	# 66083-66088	 **attackbox here**
    sprite('Action_053_06', 5)	# 66089-66093	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 66094-66098	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_1('uyu700rbl')
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 66099-66103	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 66104-66110	 **attackbox here**
    sprite('Action_053_10', 8)	# 66111-66118	 **attackbox here**
    sprite('Action_053_11', 6)	# 66119-66124	 **attackbox here**
    label(131)
    sprite('Action_053_12', 5)	# 66125-66129	 **attackbox here**
    sprite('Action_053_13', 5)	# 66130-66134	 **attackbox here**
    sprite('Action_053_14', 5)	# 66135-66139	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_053_12', 5)	# 66140-66144	 **attackbox here**
    sprite('Action_053_13', 5)	# 66145-66149	 **attackbox here**
    sprite('Action_053_14', 5)	# 66150-66154	 **attackbox here**
    sprite('Action_053_12', 5)	# 66155-66159	 **attackbox here**
    sprite('Action_053_13', 5)	# 66160-66164	 **attackbox here**
    sprite('Action_053_14', 5)	# 66165-66169	 **attackbox here**
    sprite('Action_053_12', 5)	# 66170-66174	 **attackbox here**
    sprite('Action_053_13', 5)	# 66175-66179	 **attackbox here**
    sprite('Action_053_14', 5)	# 66180-66184	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(180)
    label(132)
    sprite('Action_053_12', 5)	# 66185-66189	 **attackbox here**
    sprite('Action_053_13', 5)	# 66190-66194	 **attackbox here**
    sprite('Action_053_14', 5)	# 66195-66199	 **attackbox here**
    gotoLabel(132)
    label(140)
    sprite('keep', 1)	# 66200-66200
    Unknown2053(0)
    Unknown2034(0)

    def upon_3():
        if (SLOT_145 < 100000):
            clearUponHandler(3)
            Unknown1084(1)
            sendToLabel(142)
    sprite('keep', 1)	# 66201-66201
    Unknown48('190000000200000036000000180000000200000036000000')
    if SLOT_54:
        if (not SLOT_39):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                pass
            else:
                Unknown2005()
        else:
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                pass
            else:
                Unknown2005()
    sprite('Action_010_00', 1)	# 66202-66202
    physicsXImpulse(8000)
    label(141)
    sprite('Action_010_00', 5)	# 66203-66207
    sprite('Action_010_01', 5)	# 66208-66212
    sprite('Action_010_02', 5)	# 66213-66217
    sprite('Action_010_03', 6)	# 66218-66223
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_04', 5)	# 66224-66228
    sprite('Action_010_05', 5)	# 66229-66233
    sprite('Action_010_06', 5)	# 66234-66238
    sprite('Action_010_07', 5)	# 66239-66243
    sprite('Action_010_08', 5)	# 66244-66248
    sprite('Action_010_09', 6)	# 66249-66254
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_10', 5)	# 66255-66259
    sprite('Action_010_11', 5)	# 66260-66264
    loopRest()
    gotoLabel(141)
    label(142)
    sprite('Yuz646_00', 6)	# 66265-66270
    Unknown2019(1000)
    SFX_1('uyu700uhy')
    sprite('Yuz646_01', 10)	# 66271-66280
    Unknown21007(24, 40)
    sprite('Yuz646_02', 6)	# 66281-66286
    sprite('Yuz646_03', 6)	# 66287-66292
    sprite('Yuz646_04', 6)	# 66293-66298	 **attackbox here**
    sprite('Yuz646_05', 6)	# 66299-66304	 **attackbox here**
    sprite('Yuz646_06', 6)	# 66305-66310	 **attackbox here**
    label(143)
    sprite('Yuz646_04', 6)	# 66311-66316	 **attackbox here**
    sprite('Yuz646_05', 6)	# 66317-66322	 **attackbox here**
    sprite('Yuz646_06', 6)	# 66323-66328	 **attackbox here**
    if SLOT_97:
        _gotolabel(143)
    sprite('Yuz646_04', 1)	# 66329-66329	 **attackbox here**
    Unknown21007(24, 39)
    Unknown21011(180)
    label(144)
    sprite('Yuz646_04', 6)	# 66330-66335	 **attackbox here**
    sprite('Yuz646_05', 6)	# 66336-66341	 **attackbox here**
    sprite('Yuz646_06', 6)	# 66342-66347	 **attackbox here**
    gotoLabel(144)
    label(150)
    sprite('Action_000_00', 1)	# 66348-66348	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('Action_000_00', 8)	# 66349-66356	 **attackbox here**
    sprite('Action_000_01', 8)	# 66357-66364	 **attackbox here**
    sprite('Action_000_02', 8)	# 66365-66372	 **attackbox here**
    sprite('Action_000_03', 8)	# 66373-66380	 **attackbox here**
    sprite('Action_000_04', 8)	# 66381-66388	 **attackbox here**
    sprite('Action_000_05', 8)	# 66389-66396	 **attackbox here**
    sprite('Action_000_06', 8)	# 66397-66404	 **attackbox here**
    sprite('Action_000_07', 8)	# 66405-66412	 **attackbox here**
    sprite('Action_000_08', 8)	# 66413-66420	 **attackbox here**
    sprite('Action_000_09', 8)	# 66421-66428	 **attackbox here**
    sprite('Action_000_10', 8)	# 66429-66436	 **attackbox here**
    sprite('Action_000_11', 8)	# 66437-66444	 **attackbox here**
    sprite('Action_000_12', 8)	# 66445-66452	 **attackbox here**
    sprite('Action_000_13', 8)	# 66453-66460	 **attackbox here**
    sprite('Action_000_14', 8)	# 66461-66468	 **attackbox here**
    sprite('Action_000_15', 8)	# 66469-66476	 **attackbox here**
    sprite('Action_000_16', 8)	# 66477-66484	 **attackbox here**
    sprite('Action_000_17', 8)	# 66485-66492	 **attackbox here**
    sprite('Action_000_18', 8)	# 66493-66500	 **attackbox here**
    sprite('Action_000_19', 8)	# 66501-66508	 **attackbox here**
    sprite('Action_000_20', 8)	# 66509-66516	 **attackbox here**
    sprite('Action_000_21', 8)	# 66517-66524	 **attackbox here**
    sprite('Action_000_22', 8)	# 66525-66532	 **attackbox here**
    sprite('Action_000_23', 8)	# 66533-66540	 **attackbox here**
    sprite('Action_000_24', 8)	# 66541-66548	 **attackbox here**
    sprite('Action_000_25', 8)	# 66549-66556	 **attackbox here**
    sprite('Action_000_26', 8)	# 66557-66564	 **attackbox here**
    sprite('Action_000_27', 8)	# 66565-66572	 **attackbox here**
    sprite('Action_000_28', 8)	# 66573-66580	 **attackbox here**
    sprite('Action_000_29', 8)	# 66581-66588	 **attackbox here**
    sprite('Action_000_30', 8)	# 66589-66596	 **attackbox here**
    sprite('Action_000_31', 8)	# 66597-66604	 **attackbox here**
    sprite('Action_000_32', 6)	# 66605-66610	 **attackbox here**
    sprite('Action_000_33', 2)	# 66611-66612	 **attackbox here**
    sprite('Action_000_34', 8)	# 66613-66620	 **attackbox here**
    sprite('Action_000_35', 8)	# 66621-66628	 **attackbox here**
    sprite('Action_000_36', 8)	# 66629-66636	 **attackbox here**
    sprite('Action_000_37', 8)	# 66637-66644	 **attackbox here**
    sprite('Action_000_38', 8)	# 66645-66652	 **attackbox here**
    sprite('Action_000_39', 8)	# 66653-66660	 **attackbox here**
    sprite('Action_000_40', 8)	# 66661-66668	 **attackbox here**
    sprite('Action_000_41', 8)	# 66669-66676	 **attackbox here**
    sprite('Action_000_42', 8)	# 66677-66684	 **attackbox here**
    sprite('Action_000_43', 8)	# 66685-66692	 **attackbox here**
    sprite('Action_000_44', 8)	# 66693-66700	 **attackbox here**
    sprite('Action_000_45', 8)	# 66701-66708	 **attackbox here**
    sprite('Action_000_46', 8)	# 66709-66716	 **attackbox here**
    sprite('Action_000_47', 8)	# 66717-66724	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('Action_053_00', 5)	# 66725-66729
    sprite('Action_053_01', 5)	# 66730-66734	 **attackbox here**
    sprite('Action_053_02', 7)	# 66735-66741	 **attackbox here**
    sprite('Action_053_03', 11)	# 66742-66752	 **attackbox here**
    SFX_1('uyu701bha')
    sprite('Action_053_04', 16)	# 66753-66768	 **attackbox here**
    sprite('Action_053_05', 6)	# 66769-66774	 **attackbox here**
    sprite('Action_053_06', 5)	# 66775-66779	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 66780-66784	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 66785-66789	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 66790-66796	 **attackbox here**
    sprite('Action_053_10', 8)	# 66797-66804	 **attackbox here**
    sprite('Action_053_11', 6)	# 66805-66810	 **attackbox here**
    sprite('Action_053_12', 5)	# 66811-66815	 **attackbox here**
    sprite('Action_053_13', 5)	# 66816-66820	 **attackbox here**
    sprite('Action_053_14', 5)	# 66821-66825	 **attackbox here**
    Unknown23018(1)
    label(153)
    sprite('Action_053_12', 5)	# 66826-66830	 **attackbox here**
    sprite('Action_053_13', 5)	# 66831-66835	 **attackbox here**
    sprite('Action_053_14', 5)	# 66836-66840	 **attackbox here**
    gotoLabel(153)
    label(160)
    sprite('Action_000_00', 1)	# 66841-66841	 **attackbox here**
    Unknown2034(0)
    Unknown2053(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 8)	# 66842-66849	 **attackbox here**
    sprite('Action_000_01', 8)	# 66850-66857	 **attackbox here**
    sprite('Action_000_02', 8)	# 66858-66865	 **attackbox here**
    sprite('Action_000_03', 8)	# 66866-66873	 **attackbox here**
    sprite('Action_000_04', 8)	# 66874-66881	 **attackbox here**
    sprite('Action_000_05', 8)	# 66882-66889	 **attackbox here**
    sprite('Action_000_06', 8)	# 66890-66897	 **attackbox here**
    sprite('Action_000_07', 8)	# 66898-66905	 **attackbox here**
    sprite('Action_000_08', 8)	# 66906-66913	 **attackbox here**
    sprite('Action_000_09', 8)	# 66914-66921	 **attackbox here**
    sprite('Action_000_10', 8)	# 66922-66929	 **attackbox here**
    sprite('Action_000_11', 8)	# 66930-66937	 **attackbox here**
    sprite('Action_000_12', 8)	# 66938-66945	 **attackbox here**
    sprite('Action_000_13', 8)	# 66946-66953	 **attackbox here**
    sprite('Action_000_14', 8)	# 66954-66961	 **attackbox here**
    sprite('Action_000_15', 8)	# 66962-66969	 **attackbox here**
    sprite('Action_000_16', 8)	# 66970-66977	 **attackbox here**
    sprite('Action_000_17', 8)	# 66978-66985	 **attackbox here**
    sprite('Action_000_18', 8)	# 66986-66993	 **attackbox here**
    sprite('Action_000_19', 8)	# 66994-67001	 **attackbox here**
    sprite('Action_000_20', 8)	# 67002-67009	 **attackbox here**
    sprite('Action_000_21', 8)	# 67010-67017	 **attackbox here**
    sprite('Action_000_22', 8)	# 67018-67025	 **attackbox here**
    sprite('Action_000_23', 8)	# 67026-67033	 **attackbox here**
    sprite('Action_000_24', 8)	# 67034-67041	 **attackbox here**
    sprite('Action_000_25', 8)	# 67042-67049	 **attackbox here**
    sprite('Action_000_26', 8)	# 67050-67057	 **attackbox here**
    sprite('Action_000_27', 8)	# 67058-67065	 **attackbox here**
    sprite('Action_000_28', 8)	# 67066-67073	 **attackbox here**
    sprite('Action_000_29', 8)	# 67074-67081	 **attackbox here**
    sprite('Action_000_30', 8)	# 67082-67089	 **attackbox here**
    sprite('Action_000_31', 8)	# 67090-67097	 **attackbox here**
    sprite('Action_000_32', 6)	# 67098-67103	 **attackbox here**
    sprite('Action_000_33', 2)	# 67104-67105	 **attackbox here**
    sprite('Action_000_34', 8)	# 67106-67113	 **attackbox here**
    sprite('Action_000_35', 8)	# 67114-67121	 **attackbox here**
    sprite('Action_000_36', 8)	# 67122-67129	 **attackbox here**
    sprite('Action_000_37', 8)	# 67130-67137	 **attackbox here**
    sprite('Action_000_38', 8)	# 67138-67145	 **attackbox here**
    sprite('Action_000_39', 8)	# 67146-67153	 **attackbox here**
    sprite('Action_000_40', 8)	# 67154-67161	 **attackbox here**
    sprite('Action_000_41', 8)	# 67162-67169	 **attackbox here**
    sprite('Action_000_42', 8)	# 67170-67177	 **attackbox here**
    sprite('Action_000_43', 8)	# 67178-67185	 **attackbox here**
    sprite('Action_000_44', 8)	# 67186-67193	 **attackbox here**
    sprite('Action_000_45', 8)	# 67194-67201	 **attackbox here**
    sprite('Action_000_46', 8)	# 67202-67209	 **attackbox here**
    sprite('Action_000_47', 8)	# 67210-67217	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('Action_053_00', 5)	# 67218-67222
    sprite('Action_053_01', 5)	# 67223-67227	 **attackbox here**
    sprite('Action_053_02', 7)	# 67228-67234	 **attackbox here**
    sprite('Action_053_03', 11)	# 67235-67245	 **attackbox here**
    SFX_1('uyu701pyo')
    sprite('Action_053_04', 16)	# 67246-67261	 **attackbox here**
    sprite('Action_053_05', 6)	# 67262-67267	 **attackbox here**
    sprite('Action_053_06', 5)	# 67268-67272	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 67273-67277	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 67278-67282	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 67283-67289	 **attackbox here**
    sprite('Action_053_10', 8)	# 67290-67297	 **attackbox here**
    sprite('Action_053_11', 6)	# 67298-67303	 **attackbox here**
    sprite('Action_053_12', 5)	# 67304-67308	 **attackbox here**
    sprite('Action_053_13', 5)	# 67309-67313	 **attackbox here**
    sprite('Action_053_14', 5)	# 67314-67318	 **attackbox here**
    Unknown23018(1)
    label(163)
    sprite('Action_053_12', 5)	# 67319-67323	 **attackbox here**
    sprite('Action_053_13', 5)	# 67324-67328	 **attackbox here**
    sprite('Action_053_14', 5)	# 67329-67333	 **attackbox here**
    gotoLabel(163)
    label(170)
    sprite('Action_000_00', 1)	# 67334-67334	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_000_00', 8)	# 67335-67342	 **attackbox here**
    sprite('Action_000_01', 8)	# 67343-67350	 **attackbox here**
    sprite('Action_000_02', 8)	# 67351-67358	 **attackbox here**
    sprite('Action_000_03', 8)	# 67359-67366	 **attackbox here**
    sprite('Action_000_04', 8)	# 67367-67374	 **attackbox here**
    sprite('Action_000_05', 8)	# 67375-67382	 **attackbox here**
    sprite('Action_000_06', 8)	# 67383-67390	 **attackbox here**
    sprite('Action_000_07', 8)	# 67391-67398	 **attackbox here**
    sprite('Action_000_08', 8)	# 67399-67406	 **attackbox here**
    sprite('Action_000_09', 8)	# 67407-67414	 **attackbox here**
    sprite('Action_000_10', 8)	# 67415-67422	 **attackbox here**
    sprite('Action_000_11', 8)	# 67423-67430	 **attackbox here**
    sprite('Action_000_12', 8)	# 67431-67438	 **attackbox here**
    sprite('Action_000_13', 8)	# 67439-67446	 **attackbox here**
    sprite('Action_000_14', 8)	# 67447-67454	 **attackbox here**
    sprite('Action_000_15', 8)	# 67455-67462	 **attackbox here**
    sprite('Action_000_16', 8)	# 67463-67470	 **attackbox here**
    sprite('Action_000_17', 8)	# 67471-67478	 **attackbox here**
    sprite('Action_000_18', 8)	# 67479-67486	 **attackbox here**
    sprite('Action_000_19', 8)	# 67487-67494	 **attackbox here**
    sprite('Action_000_20', 8)	# 67495-67502	 **attackbox here**
    sprite('Action_000_21', 8)	# 67503-67510	 **attackbox here**
    sprite('Action_000_22', 8)	# 67511-67518	 **attackbox here**
    sprite('Action_000_23', 8)	# 67519-67526	 **attackbox here**
    sprite('Action_000_24', 8)	# 67527-67534	 **attackbox here**
    sprite('Action_000_25', 8)	# 67535-67542	 **attackbox here**
    sprite('Action_000_26', 8)	# 67543-67550	 **attackbox here**
    sprite('Action_000_27', 8)	# 67551-67558	 **attackbox here**
    sprite('Action_000_28', 8)	# 67559-67566	 **attackbox here**
    sprite('Action_000_29', 8)	# 67567-67574	 **attackbox here**
    sprite('Action_000_30', 8)	# 67575-67582	 **attackbox here**
    sprite('Action_000_31', 8)	# 67583-67590	 **attackbox here**
    sprite('Action_000_32', 6)	# 67591-67596	 **attackbox here**
    sprite('Action_000_33', 2)	# 67597-67598	 **attackbox here**
    sprite('Action_000_34', 8)	# 67599-67606	 **attackbox here**
    sprite('Action_000_35', 8)	# 67607-67614	 **attackbox here**
    sprite('Action_000_36', 8)	# 67615-67622	 **attackbox here**
    sprite('Action_000_37', 8)	# 67623-67630	 **attackbox here**
    sprite('Action_000_38', 8)	# 67631-67638	 **attackbox here**
    sprite('Action_000_39', 8)	# 67639-67646	 **attackbox here**
    sprite('Action_000_40', 8)	# 67647-67654	 **attackbox here**
    sprite('Action_000_41', 8)	# 67655-67662	 **attackbox here**
    sprite('Action_000_42', 8)	# 67663-67670	 **attackbox here**
    sprite('Action_000_43', 8)	# 67671-67678	 **attackbox here**
    sprite('Action_000_44', 8)	# 67679-67686	 **attackbox here**
    sprite('Action_000_45', 8)	# 67687-67694	 **attackbox here**
    sprite('Action_000_46', 8)	# 67695-67702	 **attackbox here**
    sprite('Action_000_47', 8)	# 67703-67710	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_053_00', 5)	# 67711-67715
    sprite('Action_053_01', 5)	# 67716-67720	 **attackbox here**
    sprite('Action_053_02', 7)	# 67721-67727	 **attackbox here**
    sprite('Action_053_03', 11)	# 67728-67738	 **attackbox here**
    SFX_1('uyu701rrb')
    sprite('Action_053_04', 16)	# 67739-67754	 **attackbox here**
    sprite('Action_053_05', 6)	# 67755-67760	 **attackbox here**
    sprite('Action_053_06', 5)	# 67761-67765	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 67766-67770	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 67771-67775	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 67776-67782	 **attackbox here**
    sprite('Action_053_10', 8)	# 67783-67790	 **attackbox here**
    sprite('Action_053_11', 6)	# 67791-67796	 **attackbox here**
    sprite('Action_053_12', 5)	# 67797-67801	 **attackbox here**
    sprite('Action_053_13', 5)	# 67802-67806	 **attackbox here**
    sprite('Action_053_14', 5)	# 67807-67811	 **attackbox here**
    Unknown23018(1)
    label(173)
    sprite('Action_053_12', 5)	# 67812-67816	 **attackbox here**
    sprite('Action_053_13', 5)	# 67817-67821	 **attackbox here**
    sprite('Action_053_14', 5)	# 67822-67826	 **attackbox here**
    gotoLabel(173)
    label(180)
    sprite('Action_000_00', 1)	# 67827-67827	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('Action_000_00', 8)	# 67828-67835	 **attackbox here**
    sprite('Action_000_01', 8)	# 67836-67843	 **attackbox here**
    sprite('Action_000_02', 8)	# 67844-67851	 **attackbox here**
    sprite('Action_000_03', 8)	# 67852-67859	 **attackbox here**
    sprite('Action_000_04', 8)	# 67860-67867	 **attackbox here**
    sprite('Action_000_05', 8)	# 67868-67875	 **attackbox here**
    sprite('Action_000_06', 8)	# 67876-67883	 **attackbox here**
    sprite('Action_000_07', 8)	# 67884-67891	 **attackbox here**
    sprite('Action_000_08', 8)	# 67892-67899	 **attackbox here**
    sprite('Action_000_09', 8)	# 67900-67907	 **attackbox here**
    sprite('Action_000_10', 8)	# 67908-67915	 **attackbox here**
    sprite('Action_000_11', 8)	# 67916-67923	 **attackbox here**
    sprite('Action_000_12', 8)	# 67924-67931	 **attackbox here**
    sprite('Action_000_13', 8)	# 67932-67939	 **attackbox here**
    sprite('Action_000_14', 8)	# 67940-67947	 **attackbox here**
    sprite('Action_000_15', 8)	# 67948-67955	 **attackbox here**
    sprite('Action_000_16', 8)	# 67956-67963	 **attackbox here**
    sprite('Action_000_17', 8)	# 67964-67971	 **attackbox here**
    sprite('Action_000_18', 8)	# 67972-67979	 **attackbox here**
    sprite('Action_000_19', 8)	# 67980-67987	 **attackbox here**
    sprite('Action_000_20', 8)	# 67988-67995	 **attackbox here**
    sprite('Action_000_21', 8)	# 67996-68003	 **attackbox here**
    sprite('Action_000_22', 8)	# 68004-68011	 **attackbox here**
    sprite('Action_000_23', 8)	# 68012-68019	 **attackbox here**
    sprite('Action_000_24', 8)	# 68020-68027	 **attackbox here**
    sprite('Action_000_25', 8)	# 68028-68035	 **attackbox here**
    sprite('Action_000_26', 8)	# 68036-68043	 **attackbox here**
    sprite('Action_000_27', 8)	# 68044-68051	 **attackbox here**
    sprite('Action_000_28', 8)	# 68052-68059	 **attackbox here**
    sprite('Action_000_29', 8)	# 68060-68067	 **attackbox here**
    sprite('Action_000_30', 8)	# 68068-68075	 **attackbox here**
    sprite('Action_000_31', 8)	# 68076-68083	 **attackbox here**
    sprite('Action_000_32', 6)	# 68084-68089	 **attackbox here**
    sprite('Action_000_33', 2)	# 68090-68091	 **attackbox here**
    sprite('Action_000_34', 8)	# 68092-68099	 **attackbox here**
    sprite('Action_000_35', 8)	# 68100-68107	 **attackbox here**
    sprite('Action_000_36', 8)	# 68108-68115	 **attackbox here**
    sprite('Action_000_37', 8)	# 68116-68123	 **attackbox here**
    sprite('Action_000_38', 8)	# 68124-68131	 **attackbox here**
    sprite('Action_000_39', 8)	# 68132-68139	 **attackbox here**
    sprite('Action_000_40', 8)	# 68140-68147	 **attackbox here**
    sprite('Action_000_41', 8)	# 68148-68155	 **attackbox here**
    sprite('Action_000_42', 8)	# 68156-68163	 **attackbox here**
    sprite('Action_000_43', 8)	# 68164-68171	 **attackbox here**
    sprite('Action_000_44', 8)	# 68172-68179	 **attackbox here**
    sprite('Action_000_45', 8)	# 68180-68187	 **attackbox here**
    sprite('Action_000_46', 8)	# 68188-68195	 **attackbox here**
    sprite('Action_000_47', 8)	# 68196-68203	 **attackbox here**
    gotoLabel(181)
    label(182)
    sprite('Action_053_00', 5)	# 68204-68208
    sprite('Action_053_01', 5)	# 68209-68213	 **attackbox here**
    sprite('Action_053_02', 7)	# 68214-68220	 **attackbox here**
    sprite('Action_053_03', 11)	# 68221-68231	 **attackbox here**
    SFX_1('uyu701ugo')
    sprite('Action_053_04', 16)	# 68232-68247	 **attackbox here**
    sprite('Action_053_05', 6)	# 68248-68253	 **attackbox here**
    sprite('Action_053_06', 5)	# 68254-68258	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 68259-68263	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 68264-68268	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 68269-68275	 **attackbox here**
    sprite('Action_053_10', 8)	# 68276-68283	 **attackbox here**
    sprite('Action_053_11', 6)	# 68284-68289	 **attackbox here**
    sprite('Action_053_12', 5)	# 68290-68294	 **attackbox here**
    sprite('Action_053_13', 5)	# 68295-68299	 **attackbox here**
    sprite('Action_053_14', 5)	# 68300-68304	 **attackbox here**
    Unknown23018(1)
    label(183)
    sprite('Action_053_12', 5)	# 68305-68309	 **attackbox here**
    sprite('Action_053_13', 5)	# 68310-68314	 **attackbox here**
    sprite('Action_053_14', 5)	# 68315-68319	 **attackbox here**
    gotoLabel(183)
    label(190)
    sprite('Action_053_00', 5)	# 68320-68324
    sprite('Action_053_01', 5)	# 68325-68329	 **attackbox here**
    sprite('Action_053_02', 7)	# 68330-68336	 **attackbox here**
    sprite('Action_053_03', 11)	# 68337-68347	 **attackbox here**
    sprite('Action_053_04', 16)	# 68348-68363	 **attackbox here**
    sprite('Action_053_05', 6)	# 68364-68369	 **attackbox here**
    sprite('Action_053_06', 5)	# 68370-68374	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 68375-68379	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_1('uyu700pla')
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 68380-68384	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 68385-68391	 **attackbox here**
    sprite('Action_053_10', 8)	# 68392-68399	 **attackbox here**
    sprite('Action_053_11', 6)	# 68400-68405	 **attackbox here**
    label(191)
    sprite('Action_053_12', 5)	# 68406-68410	 **attackbox here**
    sprite('Action_053_13', 5)	# 68411-68415	 **attackbox here**
    sprite('Action_053_14', 5)	# 68416-68420	 **attackbox here**
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_053_12', 5)	# 68421-68425	 **attackbox here**
    sprite('Action_053_13', 5)	# 68426-68430	 **attackbox here**
    sprite('Action_053_14', 5)	# 68431-68435	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(192)
    sprite('Action_053_12', 5)	# 68436-68440	 **attackbox here**
    sprite('Action_053_13', 5)	# 68441-68445	 **attackbox here**
    sprite('Action_053_14', 5)	# 68446-68450	 **attackbox here**
    gotoLabel(192)
    label(200)
    sprite('Action_000_00', 1)	# 68451-68451	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 8)	# 68452-68459	 **attackbox here**
    sprite('Action_000_01', 8)	# 68460-68467	 **attackbox here**
    sprite('Action_000_02', 8)	# 68468-68475	 **attackbox here**
    sprite('Action_000_03', 8)	# 68476-68483	 **attackbox here**
    sprite('Action_000_04', 8)	# 68484-68491	 **attackbox here**
    sprite('Action_000_05', 8)	# 68492-68499	 **attackbox here**
    sprite('Action_000_06', 8)	# 68500-68507	 **attackbox here**
    sprite('Action_000_07', 8)	# 68508-68515	 **attackbox here**
    sprite('Action_000_08', 8)	# 68516-68523	 **attackbox here**
    sprite('Action_000_09', 8)	# 68524-68531	 **attackbox here**
    sprite('Action_000_10', 8)	# 68532-68539	 **attackbox here**
    sprite('Action_000_11', 8)	# 68540-68547	 **attackbox here**
    sprite('Action_000_12', 8)	# 68548-68555	 **attackbox here**
    sprite('Action_000_13', 8)	# 68556-68563	 **attackbox here**
    sprite('Action_000_14', 8)	# 68564-68571	 **attackbox here**
    sprite('Action_000_15', 8)	# 68572-68579	 **attackbox here**
    sprite('Action_000_16', 8)	# 68580-68587	 **attackbox here**
    sprite('Action_000_17', 8)	# 68588-68595	 **attackbox here**
    sprite('Action_000_18', 8)	# 68596-68603	 **attackbox here**
    sprite('Action_000_19', 8)	# 68604-68611	 **attackbox here**
    sprite('Action_000_20', 8)	# 68612-68619	 **attackbox here**
    sprite('Action_000_21', 8)	# 68620-68627	 **attackbox here**
    sprite('Action_000_22', 8)	# 68628-68635	 **attackbox here**
    sprite('Action_000_23', 8)	# 68636-68643	 **attackbox here**
    sprite('Action_000_24', 8)	# 68644-68651	 **attackbox here**
    sprite('Action_000_25', 8)	# 68652-68659	 **attackbox here**
    sprite('Action_000_26', 8)	# 68660-68667	 **attackbox here**
    sprite('Action_000_27', 8)	# 68668-68675	 **attackbox here**
    sprite('Action_000_28', 8)	# 68676-68683	 **attackbox here**
    sprite('Action_000_29', 8)	# 68684-68691	 **attackbox here**
    sprite('Action_000_30', 8)	# 68692-68699	 **attackbox here**
    sprite('Action_000_31', 8)	# 68700-68707	 **attackbox here**
    sprite('Action_000_32', 6)	# 68708-68713	 **attackbox here**
    sprite('Action_000_33', 2)	# 68714-68715	 **attackbox here**
    sprite('Action_000_34', 8)	# 68716-68723	 **attackbox here**
    sprite('Action_000_35', 8)	# 68724-68731	 **attackbox here**
    sprite('Action_000_36', 8)	# 68732-68739	 **attackbox here**
    sprite('Action_000_37', 8)	# 68740-68747	 **attackbox here**
    sprite('Action_000_38', 8)	# 68748-68755	 **attackbox here**
    sprite('Action_000_39', 8)	# 68756-68763	 **attackbox here**
    sprite('Action_000_40', 8)	# 68764-68771	 **attackbox here**
    sprite('Action_000_41', 8)	# 68772-68779	 **attackbox here**
    sprite('Action_000_42', 8)	# 68780-68787	 **attackbox here**
    sprite('Action_000_43', 8)	# 68788-68795	 **attackbox here**
    sprite('Action_000_44', 8)	# 68796-68803	 **attackbox here**
    sprite('Action_000_45', 8)	# 68804-68811	 **attackbox here**
    sprite('Action_000_46', 8)	# 68812-68819	 **attackbox here**
    sprite('Action_000_47', 8)	# 68820-68827	 **attackbox here**
    gotoLabel(201)
    label(202)
    sprite('Action_053_00', 5)	# 68828-68832
    sprite('Action_053_01', 5)	# 68833-68837	 **attackbox here**
    sprite('Action_053_02', 7)	# 68838-68844	 **attackbox here**
    sprite('Action_053_03', 11)	# 68845-68855	 **attackbox here**
    sprite('Action_053_04', 16)	# 68856-68871	 **attackbox here**
    sprite('Action_053_05', 6)	# 68872-68877	 **attackbox here**
    sprite('Action_053_06', 5)	# 68878-68882	 **attackbox here**
    teleportRelativeX(-18000)
    sprite('Action_053_07', 5)	# 68883-68887	 **attackbox here**
    teleportRelativeX(-50000)
    SFX_3('SE045')
    sprite('Action_053_08', 5)	# 68888-68892	 **attackbox here**
    teleportRelativeX(-30000)
    sprite('Action_053_09', 7)	# 68893-68899	 **attackbox here**
    sprite('Action_053_10', 8)	# 68900-68907	 **attackbox here**
    SFX_1('uyu701biz')
    sprite('Action_053_11', 6)	# 68908-68913	 **attackbox here**
    sprite('Action_053_12', 5)	# 68914-68918	 **attackbox here**
    sprite('Action_053_13', 5)	# 68919-68923	 **attackbox here**
    sprite('Action_053_14', 5)	# 68924-68928	 **attackbox here**
    Unknown23018(1)
    label(203)
    sprite('Action_053_12', 5)	# 68929-68933	 **attackbox here**
    sprite('Action_053_13', 5)	# 68934-68938	 **attackbox here**
    sprite('Action_053_14', 5)	# 68939-68943	 **attackbox here**
    gotoLabel(203)

@State
def CmnActLose():
    sprite('Action_248_00', 4)	# 1-4
    sprite('Action_248_01', 5)	# 5-9
    if SLOT_158:
        Unknown7006('uyu405_0', 100, 880114037, 828323120, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_248_02', 6)	# 10-15
    sprite('Action_248_03', 5)	# 16-20
    sprite('Action_248_04', 4)	# 21-24
    GFX_0('TimeUp_Lose', -1)
    Unknown23018(1)
    sprite('Action_248_05', 32767)	# 25-32791
