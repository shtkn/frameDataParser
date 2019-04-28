@Subroutine
def PreInit():
    Unknown12019('626d6b00000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFInitialVelocity(20000)
    DashFMaxVelocity(30000)
    Unknown12024(2)
    Unknown13039(1)
    Unknown2049(1)
    Unknown23003(0, 1, 2, 2, 300, 0, -49152, -65281)
    Unknown23010(0, 1)
    Unknown23008(0, 0)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('Blocking2nd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Unknown15006(100000)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('Blocking3rd', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0x1c)
    Unknown15006(100000)
    Unknown15016(3, 15, 16)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('NmlAtkExcite', 0x5f)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('DonguriThrow', 0x5f)
    Unknown14005(1)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14015(100000, 300000, -120000, 200000, 2000, 50)
    Move_EndRegister()
    Move_Register('Atk5AA', 0x7)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown15006(3000)
    Unknown14015(0, 300000, -120000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Atk5AAA', 0x7)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown15006(3000)
    Unknown14015(0, 300000, -120000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Atk5AAAA', 0x7)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown15016(0, 10, 14)
    Unknown15012(1)
    Unknown14015(0, 300000, -120000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown15006(1)
    Unknown15013(1)
    Unknown14015(0, 200000, -50000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('Atk4A2nd', 0x6)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown14027('NmlAtk4A')
    Unknown15013(1)
    Unknown15006(3000)
    Unknown14015(0, 300000, -120000, 200000, 1500, 10)
    Move_EndRegister()
    Move_Register('Atk4A3rd', 0x6)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown14027('NmlAtk4A')
    Unknown15013(1)
    Unknown15006(3000)
    Unknown14015(0, 300000, -120000, 200000, 1500, 10)
    Move_EndRegister()
    Move_Register('Atk4A4th', 0x6)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown14027('NmlAtk4A')
    Unknown15013(1)
    Unknown15006(3000)
    Unknown14015(0, 300000, -120000, 200000, 1500, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(3)
    Unknown15013(2000)
    Unknown14015(0, 200000, -100000, 150000, 1500, 10)
    Move_EndRegister()
    Move_Register('Atk2A2nd', 0x4)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown14027('NmlAtk2A')
    Unknown15006(3000)
    Unknown14015(0, 300000, -100000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('Atk2A3rd', 0x4)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown14027('NmlAtk2A')
    Unknown15006(3000)
    Unknown14015(0, 300000, -100000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('Atk2A4th', 0x4)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown14027('NmlAtk2A')
    Unknown15006(3000)
    Unknown14015(0, 300000, -100000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(3)
    Unknown15021(4000)
    Unknown14015(0, 300000, 100000, 350000, 1500, 50)
    Move_EndRegister()
    Move_Register('Atk5BB', 0x19)
    Unknown14005(1)
    Move_Input_(0xb)
    Unknown14015(0, 300000, -120000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Atk5BBB', 0x19)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown15016(1, 10, 14)
    Unknown15014(1)
    Unknown15012(1)
    Unknown14015(0, 300000, -200000, 400000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14027('NmlAtk5B')
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 250000, -100000, 100000, 1300, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5C', 0x2b)
    Unknown15021(1)
    Unknown15015(24, 26)
    Unknown14015(0, 300000, -200000, 100000, 1500, 0)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('Atk5C2nd', 0x2b)
    Unknown14005(1)
    Move_Input_(0x14)
    MoveMaxChainRepeat(2)
    Unknown15006(4000)
    Unknown14015(-50000, 400000, -200000, 150000, 1000, 0)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown15016(2, 15, 25)
    Unknown14015(300000, 550000, 0, 300000, 100, 0)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15006(1)
    Unknown14015(0, 300000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('AtkAir5A2nd', 0x1)
    Unknown14005(1)
    Move_Input_(0x2)
    Unknown15006(500000)
    Unknown14015(0, 300000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15013(3000)
    Unknown14015(0, 250000, 0, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-150000, 150000, -600000, -100000, 800, 0)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('BunshinStepA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15012(40000)
    Unknown14015(0, 1000000, -200000, 200000, 100, 10)
    Move_EndRegister()
    Move_Register('BunshinStepB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15012(30000)
    Unknown14015(500000, 800000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('BunshinStepC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(1)
    Unknown15006(1)
    Unknown15012(30000)
    Unknown14015(0, 450000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('DashStop', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15013(0)
    Unknown15012(5000)
    Unknown14015(0, 300000, -200000, 200000, 2500, 10)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('Urmawari', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15013(0)
    Unknown15012(5000)
    Unknown14015(0, 300000, -200000, 300000, 2500, 10)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('DashUpper', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown15000(0)
    Unknown15003(0)
    Unknown14015(0, 500000, -200000, 350000, 5000, 10)
    Move_EndRegister()
    Move_Register('DashStraight', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15016(1, 10, 14)
    Unknown14015(500000, 1000000, -200000, 200000, 250, 11)
    Move_EndRegister()
    Move_Register('UpperBodyBlow', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15016(1, 9, 14)
    Unknown15012(8000)
    Unknown14015(0, 350000, -200000, 150000, 1000, 11)
    Move_EndRegister()
    Move_Register('UpperChudan', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15021(5000)
    Unknown14015(0, 350000, -200000, 400000, 800, 0)
    Move_EndRegister()
    Move_Register('UpperGedan', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15012(5000)
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UpperRush1_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15021(1)
    Unknown15013(10000)
    Unknown14015(0, 350000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('UpperRush1_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15021(1)
    Unknown15013(10000)
    Unknown14015(0, 350000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('CreateEnergyBall', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3008)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15012(1000)
    Unknown15013(1000)
    Unknown14015(0, 320000, -200000, 150000, 300, 100)
    Move_EndRegister()
    Move_Register('PunchShot', INPUT_SPECIALMOVE)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown15016(0, 15, 20)
    Unknown15021(1)
    Unknown14015(400000, 1000000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('Pile Bunker', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_236)
    Unknown15014(1500)
    Unknown14015(0, 300000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('DashStraight_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown15016(2, 10, 14)
    Unknown14015(500000, 1000000, -200000, 200000, 750, 10)
    Move_EndRegister()
    Move_Register('UpperBodyBlow_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown15016(2, 9, 14)
    Unknown15012(8000)
    Unknown14015(500000, 1000000, -200000, 200000, 750, 10)
    Move_EndRegister()
    Move_Register('PowerDunk3', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Move_AirGround_(0x3038)
    Unknown15016(2, 10, 13)
    Unknown15006(100000)
    Unknown15013(5000)
    Unknown15012(5000)
    Unknown14015(0, 700000, -500000, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('AutoBlocking', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_D)
    Move_Input_(INPUT_214)
    Unknown14004(1)
    Unknown15014(2000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 200000, -200000, 300000, 500, 10)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('SiriusJolt', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(INPUT_236)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15013(0)
    Unknown15012(80000)
    Unknown14015(0, 450000, -200000, 100000, 100, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(1)
    Unknown15012(0)
    Unknown15015(38, 40)
    Unknown15014(6000)
    Unknown14015(-50000, 200000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15015(38, 40)
    Unknown14015(-50000, 200000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('PowerDunkAINP', INPUT_SPECIALMOVE)
    Unknown14013('PowerDunk')
    Move_AirGround_(0x2001)
    Move_Input_(0x1)
    Unknown14005(1)
    Move_AirGround_(0x3038)
    Unknown15016(1, 14, 18)
    Unknown15006(100000)
    Unknown15013(100000)
    Unknown14015(0, 250000, -150000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('PowerDunkBINP', INPUT_SPECIALMOVE)
    Unknown14013('PowerDunk')
    Move_AirGround_(0x2001)
    Move_Input_(0xa)
    Unknown14005(1)
    Move_AirGround_(0x3038)
    Unknown15016(1, 14, 18)
    Unknown15006(100000)
    Unknown15013(100000)
    Unknown14015(0, 250000, -150000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('PowerDunkCINP', INPUT_SPECIALMOVE)
    Unknown14013('PowerDunk')
    Move_AirGround_(0x2001)
    Move_Input_(0x13)
    Unknown14005(1)
    Move_AirGround_(0x3038)
    Unknown15016(1, 14, 18)
    Unknown15006(100000)
    Unknown15013(100000)
    Unknown14015(0, 250000, -150000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('PowerDunk', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Unknown14005(1)
    Move_AirGround_(0x3038)
    Unknown15016(1, 14, 18)
    Unknown15006(100000)
    Unknown15013(100000)
    Unknown14015(0, 250000, -150000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('ShinSyouryu1', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15016(1, 32, 42)
    Unknown15020(500, 1000, 1, 1000)
    Unknown15006(2000)
    Unknown15013(2000)
    Unknown15012(1)
    Unknown15014(2000)
    Unknown14015(0, 260000, -100000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('ShinSyouryu2', 0x68)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu2AINP', 0x68)
    Unknown14013('ShinSyouryu2')
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu2BINP', 0x68)
    Unknown14013('ShinSyouryu2')
    Move_AirGround_(0x2000)
    Move_Input_(0xa)
    Unknown14005(1)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu2CINP', 0x68)
    Unknown14013('ShinSyouryu2')
    Move_AirGround_(0x2000)
    Move_Input_(0x13)
    Unknown14005(1)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu3', 0x68)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('ShinSyouryu3AINP', 0x68)
    Unknown14013('ShinSyouryu3')
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('ShinSyouryu3BINP', 0x68)
    Unknown14013('ShinSyouryu3')
    Move_AirGround_(0x2000)
    Move_Input_(0xa)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('ShinSyouryu3CINP', 0x68)
    Unknown14013('ShinSyouryu3')
    Move_AirGround_(0x2000)
    Move_Input_(0x13)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('ShinSyouryu1_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x3089)
    Unknown15016(1, 32, 42)
    Unknown15020(500, 1000, 1, 1000)
    Unknown15006(3000)
    Unknown15013(5000)
    Unknown15012(1)
    Unknown15014(2000)
    Unknown14015(0, 300000, -100000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('ShinSyouryu2_OD', 0x68)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu2_ODAINP', 0x68)
    Unknown14013('ShinSyouryu2_OD')
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu2_ODBINP', 0x68)
    Unknown14013('ShinSyouryu2_OD')
    Move_AirGround_(0x2000)
    Move_Input_(0xa)
    Unknown14005(1)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu2_ODCINP', 0x68)
    Unknown14013('ShinSyouryu2_OD')
    Move_AirGround_(0x2000)
    Move_Input_(0x13)
    Unknown14005(1)
    Unknown15016(1, 28, 38)
    Unknown15013(10000)
    Unknown14015(0, 230000, -100000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('ShinSyouryu3_OD', 0x68)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('ShinSyouryu3_ODAINP', 0x68)
    Unknown14013('ShinSyouryu3_OD')
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('ShinSyouryu3_ODBINP', 0x68)
    Unknown14013('ShinSyouryu3_OD')
    Move_AirGround_(0x2000)
    Move_Input_(0xa)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('ShinSyouryu3_ODCINP', 0x68)
    Unknown14013('ShinSyouryu3_OD')
    Move_AirGround_(0x2000)
    Move_Input_(0x13)
    Unknown14005(1)
    Unknown15013(10000)
    Unknown15016(1, 60, 70)
    Unknown14015(0, 230000, -100000, 200000, 1, 5000)
    Move_EndRegister()
    Move_Register('BigPunch', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(1500)
    Unknown15016(1, 65, 75)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(400000, 750000, 100000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('BigPunch_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x3089)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(1500)
    Unknown15016(1, 65, 75)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(400000, 750000, 100000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(1)
    Unknown15012(1)
    Unknown15013(20000)
    Unknown15016(3, 73, 75)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 450000, -250000, 150000, 1000, 0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'Atk5AA', 10000000)
    Unknown15024('Atk5AA', 'Atk5AAA', 10000000)
    Unknown15024('Atk5AAA', 'Atk5AAAA', 10000000)
    Unknown15024('NmlAtk5B', 'Atk5BB', 10000000)
    Unknown15024('Atk5BB', 'Atk5BBB', 10000000)
    Unknown15024('Atk5BBB', 'FJump', 10000000)
    Unknown15024('Atk4A2nd', 'NmlAtk5A', 10000000)
    Unknown15024('Atk4A3rd', 'NmlAtk5A', 10000000)
    Unknown15024('Atk4A4th', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtkAIR5C', 'NmlAtkAIR5A', 10000000)
    Unknown15024('ShinSyouryu1', 'ShinSyouryu2', 10000000)
    Unknown15024('ShinSyouryu2', 'ShinSyouryu3', 10000000)
    Unknown15024('ShinSyouryu1_OD', 'ShinSyouryu2_OD', 10000000)
    Unknown15024('ShinSyouryu2_OD', 'ShinSyouryu3_OD', 10000000)
    Unknown14048('Syouryu', 0x4, 0xed)
    Unknown14048('BunshinStepA', 0x4, 0x79)
    Unknown14048('ShinSyouryu1', 0x4, 0x5f)
    Unknown14048('ShinSyouryu1_OD', 0x4, 0x5f)
    Unknown14048('SiriusJolt', 0x4, 0x45)
    Unknown14048('Air_Syouryu', 0x4, 0xed)
    Unknown14048('PowerDunk', 0x4, 0xed)
    Unknown14048('DashStraight', 0x4, 0xed)
    Unknown14048('ShinSyouryu2', 0x4, 0xed)
    Unknown14048('ShinSyouryu3', 0x4, 0xed)
    Unknown14048('ShinSyouryu2_OD', 0x4, 0xed)
    Unknown14048('ShinSyouryu3_OD', 0x4, 0xed)
    Unknown14049('NmlAtk5A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk5A', 'NmlAtk6A', 3, 0)
    Unknown14049('NmlAtk5B', 'NmlAtk5D', 0, 0)
    Unknown14049('NmlAtk5B', 'NmlAtk5C', 1, 200000)
    Unknown14049('NmlAtk5B', 'NmlAtk6A', 12, 0)
    Unknown14049('NmlAtk5C', 'Atk5C2nd', 0, 0)
    Unknown14049('Atk5C2nd', 'BunshinStepA', 0, 0)
    Unknown14049('Atk5C2nd', 'ShinSyouryu1', 1, 200000)
    Unknown14049('Atk5C2nd', 'ShinSyouryu1_OD', 1, 200000)
    Unknown14049('Atk5C2nd', 'FJump', 12, 0)
    Unknown14049('Atk5C2nd', 'BunshinStepA', 13, 0)
    Unknown14049('NmlAtk5D', 'BunshinStepA', 0, 0)
    Unknown14049('NmlAtk5D', 'BigPunch', 8, 0)
    Unknown14049('NmlAtk5D', 'BigPunch_OD', 8, 0)
    Unknown14049('NmlAtk5D', 'CreateEnergyBall', 3, 0)
    Unknown14049('NmlAtk6A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk6A', 'FHighJump', 12, 0)
    Unknown14049('NmlAtk6A', 'BunshinStepA', 13, 0)
    Unknown14049('NmlAtk6B', 'NmlAtk5D', 0, 0)
    Unknown14049('NmlAtk6B', 'Atk5C2nd', 1, 200000)
    Unknown14049('NmlAtk6C', 'NmlAtk5D', 0, 0)
    Unknown14049('NmlAtk6C', 'BigPunch', 6, 0)
    Unknown14049('NmlAtk6C', 'BigPunch_OD', 6, 0)
    Unknown14049('BunshinStepA', 'DashStraight', 0, 0)
    Unknown14049('BunshinStepA', 'UpperRush1', 1, 300000)
    Unknown14049('BunshinStepB', 'NmlAtkAIR5C', 0, 0)
    Unknown14049('UpperRush1', 'UpperBodyBlow', 0, 0)
    Unknown14049('CreateEnergyBall', 'PunchShot', 0, 0)
    Unknown14049('ThrowExe', 'BunshinStepB', 0, 0)
    Unknown14049('BackThrowExe', 'SiriusJolt', 0, 0)
    Unknown14049('ThrowExe', 'BigPunch', 6, 0)
    Unknown14049('ThrowExe', 'BigPunch_OD', 6, 0)
    Unknown14049('Syouryu', 'PowerDunk', 0, 0)
    Unknown14049('ShinSyouryu1', 'ShinSyouryu2', 0, 0)
    Unknown14049('ShinSyouryu2', 'ShinSyouryu3', 0, 0)
    Unknown14049('ShinSyouryu1_OD', 'ShinSyouryu2_OD', 0, 0)
    Unknown14049('ShinSyouryu2_OD', 'ShinSyouryu3_OD', 0, 0)
    Unknown14049('NmlAtk2A', 'NmlAtk2B', 0, 0)
    Unknown14049('NmlAtk2A', 'NmlAtk5A', 3, 0)
    Unknown14049('NmlAtk2B', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk2C', 'BunshinStepB', 6, 0)
    Unknown14049('NmlAtk2D', 'Syouryu', 0, 0)
    Unknown14049('NmlAtk2D', 'BunshinStepA', 13, 0)
    Unknown14049('NmlAtk2D', 'BigPunch', 6, 0)
    Unknown14049('NmlAtk2D', 'BigPunch_OD', 6, 0)
    Unknown14049('NmlAtk3C', 'BunshinStepA', 0, 0)
    Unknown14049('NmlAtk3C', 'ShinSyouryu1', 1, 200000)
    Unknown14049('NmlAtk3C', 'ShinSyouryu1_OD', 1, 200000)
    Unknown14049('NmlAtk3C', 'BunshinStepA', 13, 0)
    Unknown14049('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    Unknown14049('NmlAtkAIR5A', 'AtkAIR5A2nd', 13, 0)
    Unknown14049('NmlAtkAIR5A', 'AtkAIR5A3rd', 13, 0)
    Unknown14049('NmlAtkAIR5A', 'AtkAIR5A4th', 13, 0)
    Unknown14049('AtkAIR5A2nd', 'AtkAIR5A3rd', 13, 0)
    Unknown14049('AtkAIR5A2nd', 'AtkAIR5A4th', 13, 0)
    Unknown14049('AtkAIR5A3rd', 'AtkAIR5A2nd', 13, 0)
    Unknown14049('AtkAIR5A3rd', 'AtkAIR5A4th', 13, 0)
    Unknown14049('AtkAIR5A4th', 'AtkAIR5A2nd', 13, 0)
    Unknown14049('AtkAIR5A4th', 'AtkAIR5A3rd', 13, 0)
    Unknown14049('NmlAtkAIR5B', 'Air_Syouryu', 3, 0)
    Unknown14049('NmlAtkAIR5B', 'FJump', 12, 0)
    Unknown14049('NmlAtkAIR5B', 'NmlAtkAIR5A', 13, 0)
    Unknown14049('NmlAtkAIR5C', 'NmlAtkAIR5B', 3, 0)
    Unknown14049('NmlAtkAIR5C', 'AtkAir5C2nd', 0, 0)
    Unknown14049('NmlAtkAIR5C', 'AtkAir5C2nd', 13, 0)
    Unknown14049('Air_Syouryu', 'PowerDunk', 0, 0)
    Unknown12018(0, 'mk062_01')
    Unknown12018(1, 'mk062_03')
    Unknown12018(2, 'mk062_04')
    Unknown12018(3, 'mk062_05')
    Unknown12018(4, 'mk062_05')
    Unknown12018(5, 'mk062_06')
    Unknown12018(6, 'mk062_07')
    Unknown12018(7, 'mk041_02')
    Unknown12018(8, 'mk040_02')
    Unknown12018(9, 'mk045_02')
    Unknown12018(10, 'mk060_00')
    Unknown12018(11, 'mk060_01')
    Unknown12018(12, 'mk060_03')
    Unknown12018(13, 'mk060_05')
    Unknown12018(14, 'mk060_07')
    Unknown12018(15, 'mk060_14')
    Unknown12018(16, 'mk050_00')
    Unknown12018(17, 'mk052_00')
    Unknown12018(18, 'mk054_00')
    Unknown12018(19, 'mk000_00')
    Unknown12018(20, 'mk000_00')
    Unknown12018(25, 'mk063_00')
    Unknown12018(26, 'mk063_01')
    Unknown12018(27, 'mk063_02')
    Unknown12018(28, 'mk063_04')
    Unknown12018(29, 'mk063_10')
    Unknown12018(24, 'mk073_01')
    Unknown7010(0, 'bmk000')
    Unknown7010(1, 'bmk001')
    Unknown7010(2, 'bmk002')
    Unknown7010(3, 'bmk003')
    Unknown7010(4, 'bmk004')
    Unknown7010(5, 'bmk005')
    Unknown7010(6, 'bmk006')
    Unknown7010(7, 'bmk007')
    Unknown7010(8, 'bmk008')
    Unknown7010(9, 'bmk009')
    Unknown7010(10, 'bmk010')
    Unknown7010(15, 'bmk011')
    Unknown7010(16, 'bmk012')
    Unknown7010(17, 'bmk013')
    Unknown7010(18, 'bmk014')
    Unknown7010(19, 'bmk015')
    Unknown7010(20, 'bmk016')
    Unknown7010(21, 'bmk017')
    Unknown7010(22, 'bmk018')
    Unknown7010(23, 'bmk019')
    Unknown7010(24, 'bmk020')
    Unknown7010(25, 'bmk021')
    Unknown7010(28, 'bmk022')
    Unknown7010(29, 'bmk023')
    Unknown7010(30, 'bmk024')
    Unknown7010(31, 'bmk025')
    Unknown7010(32, 'bmk026')
    Unknown7010(33, 'bmk027')
    Unknown7010(34, 'bmk028')
    Unknown7010(35, 'bmk029')
    Unknown7010(36, 'bmk030')
    Unknown7010(37, 'bmk031')
    Unknown7010(39, 'bmk032')
    Unknown7010(42, 'bmk033')
    Unknown7010(43, 'bmk034')
    Unknown7010(44, 'bmk035')
    Unknown7010(45, 'bmk036')
    Unknown7010(46, 'bmk037')
    Unknown7010(47, 'bmk038')
    Unknown7010(48, 'bmk039')
    Unknown7010(49, 'bmk040')
    Unknown7010(50, 'bmk041')
    Unknown7010(52, 'bmk042')
    Unknown7010(53, 'bmk043')
    Unknown7010(54, 'bmk100_0')
    Unknown7010(55, 'bmk100_1')
    Unknown7010(56, 'bmk100_2')
    Unknown7010(63, 'bmk101_0')
    Unknown7010(64, 'bmk101_1')
    Unknown7010(65, 'bmk101_2')
    Unknown7010(57, 'bmk102_0')
    Unknown7010(58, 'bmk102_1')
    Unknown7010(59, 'bmk102_2')
    Unknown7010(66, 'bmk103_0')
    Unknown7010(67, 'bmk103_1')
    Unknown7010(68, 'bmk103_2')
    Unknown7010(60, 'bmk104_0')
    Unknown7010(61, 'bmk104_1')
    Unknown7010(62, 'bmk104_2')
    Unknown7010(69, 'bmk105_0')
    Unknown7010(70, 'bmk105_1')
    Unknown7010(71, 'bmk105_2')
    Unknown7010(72, 'bmk150')
    Unknown7010(73, 'bmk151')
    Unknown7010(74, 'bmk152')
    Unknown7010(85, 'bmk153')
    Unknown7010(87, 'bmk154')
    Unknown7010(88, 'bmk155')
    Unknown7010(96, 'bmk161_0')
    Unknown7010(97, 'bmk161_1')
    Unknown7010(92, 'bmk162_0')
    Unknown7010(93, 'bmk162_1')
    Unknown7010(98, 'bmk163_0')
    Unknown7010(99, 'bmk163_1')
    Unknown7010(100, 'bmk164_0')
    Unknown7010(101, 'bmk164_1')
    Unknown7010(105, 'bmk165_0')
    Unknown7010(106, 'bmk165_1')
    Unknown7010(102, 'bmk166_0')
    Unknown7010(103, 'bmk166_1')
    Unknown7010(90, 'bmk167_0')
    Unknown7010(91, 'bmk167_1')
    Unknown7010(107, 'bmk168_0')
    Unknown7010(108, 'bmk168_1')
    Unknown7010(110, 'bmk169_0')
    Unknown7010(111, 'bmk169_1')
    Unknown7010(94, 'bmk400_0')
    Unknown7010(95, 'bmk400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('0200000042696750756e6368000000000000000000000000000000000000000000000000')
    Unknown12059('0300000042696750756e63685f4f44000000000000000000000000000000000000000000')
    Unknown12059('040000005368696e53796f75727975310000000000000000000000000000000000000000')
    Unknown12059('050000005368696e53796f75727975315f4f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if SLOT_5:
        SLOT_5 = (SLOT_5 + (-1))
    if SLOT_59:
        SLOT_59 = (SLOT_59 + (-1))
    if CheckInput(0xfb):
        if SLOT_59:
            SLOT_5 = 0
        else:
            SLOT_5 = 4
            SLOT_59 = 40

@Subroutine
def OnLanding():
    SLOT_34 = 0

@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if Unknown23145('CmnActOverDriveEnd'):
        SLOT_47 = 1

@Subroutine
def CheckOverDrive():
    if SLOT_109:
        SLOT_51 = 1
    else:
        SLOT_51 = 0

@Subroutine
def MakotoDriveSetting():
    SLOT_57 = 1
    Unknown23008(0, 1)

    def upon_3():
        if CheckInput(0x5):
            if CheckInput(0xe):
                if CheckInput(0x17):
                    SLOT_57 = 0
        if SLOT_57:
            if SLOT_58:
                SLOT_31 = (SLOT_31 + (-1))
                if (SLOT_31 <= 0):
                    clearUponHandler(3)
            else:
                SLOT_31 = (SLOT_31 + 1)
                if (SLOT_31 >= SLOT_102):
                    SLOT_58 = 1
        else:
            if SLOT_55:
                if (SLOT_56 <= 1):
                    if SLOT_58:
                        clearUponHandler(3)
                        Unknown21015('447269766552696e670000000000000000000000000000000000000000000000e903000000000000')
                        sendToLabel(1)
                    elif (SLOT_31 == SLOT_101):
                        clearUponHandler(3)
                        Unknown21015('447269766552696e670000000000000000000000000000000000000000000000e903000000000000')
                        sendToLabel(1)
                if (SLOT_56 == 2):
                    if SLOT_58:
                        clearUponHandler(3)
                        Unknown21015('447269766552696e670000000000000000000000000000000000000000000000e903000000000000')
                        sendToLabel(2)
                    elif (SLOT_31 == SLOT_102):
                        clearUponHandler(3)
                        Unknown21015('447269766552696e670000000000000000000000000000000000000000000000e903000000000000')
                        sendToLabel(2)
            if (not SLOT_58):
                if (not (SLOT_31 == SLOT_101)):
                    if (not (SLOT_31 == SLOT_102)):
                        SLOT_31 = (SLOT_31 + 1)
        if (SLOT_31 <= SLOT_101):
            SLOT_56 = 1
            Unknown23007(0, -16776961)
            Unknown23038(0, -16776961)
            Unknown23006(0, 2)
        elif (SLOT_31 <= SLOT_102):
            SLOT_56 = 2
            Unknown23007(0, -6291201)
            Unknown23038(0, -6291201)
            Unknown23006(0, 3)

    def upon_STATE_END():
        Unknown7015()
        SLOT_55 = 0
        SLOT_56 = 0
        SLOT_57 = 0
        SLOT_58 = 0
        SLOT_31 = 0
        Unknown23008(0, 0)
        Unknown23007(0, -16776961)
        Unknown23038(0, -16776961)
        Unknown23006(0, 2)

@Subroutine
def AfterImage_Lv2():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(1)
    Unknown3071(6)
    Unknown3074('00000000ff0000008000000000000000')
    Unknown3075('00000000000000000000000000000000')

@Subroutine
def AfterImage_Lv3():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(1)
    Unknown3071(8)
    Unknown3074('000000000000000080000000ff000000')
    Unknown3075('00000000000000000000000000000000')

@Subroutine
def AfterImage_LvG():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(1)
    Unknown3071(8)
    Unknown3074('00000000ff000000ff00000000000000')
    Unknown3075('00000000000000000000000000000000')

@State
def CmnActStand():
    label(0)
    sprite('mk000_00', 5)	# 1-5
    sprite('mk000_01', 5)	# 6-10
    sprite('mk000_02', 6)	# 11-16
    sprite('mk000_03', 6)	# 17-22
    sprite('mk000_04', 5)	# 23-27
    sprite('mk000_05', 5)	# 28-32
    sprite('mk000_06', 6)	# 33-38
    sprite('mk000_07', 6)	# 39-44
    sprite('mk000_08', 5)	# 45-49
    sprite('mk000_09', 5)	# 50-54
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    if random_(2, 0, 33):
        gotoLabel(30)
    if random_(2, 0, 40):
        gotoLabel(31)
    if random_(2, 0, 50):
        gotoLabel(32)
    if random_(2, 0, 33):
        gotoLabel(33)
    if random_(2, 0, 50):
        gotoLabel(34)
    gotoLabel(35)
    label(30)
    sprite('mk000_10', 4)	# 55-58
    SLOT_88 = 240
    SFX_4('bmk002')
    sprite('mk000_11', 7)	# 59-65
    sprite('mk000_12', 7)	# 66-72
    sprite('mk000_13', 4)	# 73-76
    sprite('mk000_14', 5)	# 77-81
    sprite('mk000_15', 5)	# 82-86
    Unknown8002()
    sprite('mk000_11', 7)	# 87-93
    sprite('mk000_12', 7)	# 94-100
    sprite('mk000_13', 4)	# 101-104
    sprite('mk000_14', 5)	# 105-109
    sprite('mk000_15', 5)	# 110-114
    Unknown8002()
    loopRest()
    gotoLabel(0)
    label(31)
    sprite('mk000_16', 6)	# 115-120
    SLOT_88 = 240
    sprite('mk000_17', 6)	# 121-126
    sprite('mk000_18', 6)	# 127-132
    Unknown8002()
    sprite('mk000_19', 6)	# 133-138
    sprite('mk000_20', 6)	# 139-144
    sprite('mk000_21', 6)	# 145-150
    sprite('mk000_22', 6)	# 151-156
    sprite('mk000_23', 6)	# 157-162
    Unknown8002()
    sprite('mk000_24', 6)	# 163-168
    sprite('mk000_25', 6)	# 169-174
    sprite('mk000_26', 6)	# 175-180
    loopRest()
    gotoLabel(0)
    label(32)
    sprite('mk000_27', 6)	# 181-186
    SLOT_88 = 240
    SFX_1('bmk000')
    sprite('mk000_28', 6)	# 187-192
    sprite('mk000_29', 6)	# 193-198
    sprite('mk000_30', 6)	# 199-204
    Unknown8002()
    sprite('mk000_31', 6)	# 205-210
    sprite('mk000_32', 6)	# 211-216
    sprite('mk000_33', 6)	# 217-222
    sprite('mk000_34', 6)	# 223-228
    Unknown8002()
    sprite('mk000_35', 6)	# 229-234
    loopRest()
    gotoLabel(0)
    label(33)
    sprite('mk000_10', 4)	# 235-238
    SLOT_88 = 480
    sprite('mk000_11', 7)	# 239-245
    sprite('mk000_12', 7)	# 246-252
    sprite('mk000_13', 4)	# 253-256
    sprite('mk000_14', 5)	# 257-261
    sprite('mk000_15', 5)	# 262-266
    Unknown8002()
    sprite('mk000_11', 7)	# 267-273
    sprite('mk000_12', 7)	# 274-280
    sprite('mk000_13', 4)	# 281-284
    sprite('mk000_14', 5)	# 285-289
    sprite('mk000_15', 5)	# 290-294
    Unknown8002()
    loopRest()
    gotoLabel(0)
    label(34)
    sprite('mk000_16', 6)	# 295-300
    SLOT_88 = 480
    sprite('mk000_17', 6)	# 301-306
    sprite('mk000_18', 6)	# 307-312
    Unknown8002()
    sprite('mk000_19', 6)	# 313-318
    sprite('mk000_20', 6)	# 319-324
    sprite('mk000_21', 6)	# 325-330
    sprite('mk000_22', 6)	# 331-336
    sprite('mk000_23', 6)	# 337-342
    Unknown8002()
    sprite('mk000_24', 6)	# 343-348
    sprite('mk000_25', 6)	# 349-354
    sprite('mk000_26', 6)	# 355-360
    loopRest()
    gotoLabel(0)
    label(35)
    sprite('mk000_27', 6)	# 361-366
    SLOT_88 = 480
    SFX_1('bmk000')
    sprite('mk000_28', 6)	# 367-372
    sprite('mk000_29', 6)	# 373-378
    sprite('mk000_30', 6)	# 379-384
    Unknown8002()
    sprite('mk000_31', 6)	# 385-390
    sprite('mk000_32', 6)	# 391-396
    sprite('mk000_33', 6)	# 397-402
    sprite('mk000_34', 6)	# 403-408
    Unknown8002()
    sprite('mk000_35', 6)	# 409-414
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('mk003_00', 3)	# 1-3
    SFX_4('bmk001')
    sprite('mk003_01', 3)	# 4-6
    sprite('mk003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('mk010_00', 4)	# 1-4
    sprite('mk010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('mk010_02', 7)	# 1-7
    sprite('mk010_03', 7)	# 8-14
    sprite('mk010_04', 7)	# 15-21
    sprite('mk010_05', 7)	# 22-28
    sprite('mk010_06', 7)	# 29-35
    sprite('mk010_07', 7)	# 36-42
    sprite('mk010_08', 7)	# 43-49
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('mk013_00', 3)	# 1-3
    sprite('mk013_01', 3)	# 4-6
    sprite('mk013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('mk010_01', 4)	# 1-4
    sprite('mk010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('mk023_00', 2)	# 1-2
    sprite('mk023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    sprite('mk020_00', 4)	# 1-4
    sprite('mk020_01', 4)	# 5-8
    SFX_4('bmk007')
    gotoLabel(0)
    label(1)
    sprite('mk020_00', 4)	# 9-12
    sprite('mk020_01', 4)	# 13-16
    SFX_4('bmk002')
    gotoLabel(0)
    label(2)
    sprite('mk020_00', 4)	# 17-20
    sprite('mk020_01', 4)	# 21-24
    SFX_4('bmk003')
    gotoLabel(0)
    label(0)
    sprite('mk020_00', 4)	# 25-28
    sprite('mk020_01', 4)	# 29-32
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('mk020_02', 3)	# 1-3
    sprite('mk020_03', 3)	# 4-6
    sprite('mk020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('mk020_05', 3)	# 1-3
    sprite('mk020_06', 3)	# 4-6
    label(0)
    sprite('mk020_07', 4)	# 7-10
    sprite('mk020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('mk024_00', 3)	# 1-3
    sprite('mk024_01', 3)	# 4-6
    sprite('mk024_02', 3)	# 7-9
    sprite('mk024_03', 3)	# 10-12
    sprite('mk024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('mk024_00', 2)	# 1-2
    sprite('mk024_01', 2)	# 3-4
    sprite('mk024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('mk024_03', 3)	# 1-3
    sprite('mk024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('mk030_00', 5)	# 1-5
    sprite('mk030_01', 6)	# 6-11
    label(0)
    sprite('mk030_02', 6)	# 12-17
    sprite('mk030_03', 6)	# 18-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk030_04', 6)	# 24-29
    sprite('mk030_05', 6)	# 30-35
    sprite('mk030_06', 6)	# 36-41
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('mk031_00', 7)	# 1-7
    sprite('mk031_01', 7)	# 8-14
    label(0)
    sprite('mk031_02', 7)	# 15-21
    sprite('mk031_03', 7)	# 22-28
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk031_04', 7)	# 29-35
    sprite('mk031_05', 7)	# 36-42
    sprite('mk031_06', 7)	# 43-49
    sprite('mk031_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk031_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('mk032_10', 3)	# 1-3
    sprite('mk032_00', 4)	# 4-7
    sprite('mk032_01', 4)	# 8-11
    label(0)
    sprite('mk032_02', 4)	# 12-15
    sprite('mk032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 20-23
    sprite('mk032_05', 4)	# 24-27
    sprite('mk032_06', 4)	# 28-31
    sprite('mk032_07', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 36-38
    sprite('mk032_01', 2)	# 39-40
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('mk032_09', 8)	# 1-8
    sprite('mk032_10', 4)	# 9-12

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
    sprite('mk033_00', 1)	# 1-1
    sprite('mk033_01', 2)	# 2-3
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    SFX_4('bmk005')
    sprite('mk033_02', 2)	# 4-5
    sprite('mk033_02', 1)	# 6-6
    sprite('mk033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('mk033_02', 3)	# 10-12
    sprite('mk033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mk033_04', 3)	# 16-18
    Unknown1084(1)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('mk033_05', 3)	# 19-21

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('mk035_00', 3)	# 1-3
    SFX_4('mk004')
    label(0)
    sprite('mk035_01', 3)	# 4-6
    sprite('mk035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('mk036_00', 3)	# 1-3
    SFX_4('mk006')
    label(0)
    sprite('mk036_01', 3)	# 4-6
    sprite('mk036_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('mk050_00', 1)	# 1-1
    sprite('mk050_01', 1)	# 2-2
    sprite('mk050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('mk050_01', 1)	# 1-1
    sprite('mk050_02', 1)	# 2-2
    sprite('mk050_01', 2)	# 3-4
    sprite('mk050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('mk050_02', 1)	# 1-1
    sprite('mk050_03', 1)	# 2-2
    sprite('mk050_02', 2)	# 3-4
    sprite('mk050_01', 2)	# 5-6
    sprite('mk050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('mk050_03', 1)	# 1-1
    sprite('mk050_04', 1)	# 2-2
    sprite('mk050_03', 2)	# 3-4
    sprite('mk050_02', 2)	# 5-6
    sprite('mk050_01', 2)	# 7-8
    sprite('mk050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('mk050_03', 1)	# 1-1
    sprite('mk050_04', 1)	# 2-2
    sprite('mk050_04', 2)	# 3-4
    sprite('mk050_03', 2)	# 5-6
    sprite('mk050_02', 2)	# 7-8
    sprite('mk050_01', 2)	# 9-10
    sprite('mk050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('mk052_00', 1)	# 1-1
    sprite('mk052_01', 1)	# 2-2
    sprite('mk052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('mk052_01', 1)	# 1-1
    sprite('mk052_02', 1)	# 2-2
    sprite('mk052_01', 2)	# 3-4
    sprite('mk052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('mk052_02', 1)	# 1-1
    sprite('mk052_03', 1)	# 2-2
    sprite('mk052_02', 2)	# 3-4
    sprite('mk052_01', 2)	# 5-6
    sprite('mk052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('mk052_03', 1)	# 1-1
    sprite('mk052_04', 1)	# 2-2
    sprite('mk052_03', 2)	# 3-4
    sprite('mk052_02', 2)	# 5-6
    sprite('mk052_01', 2)	# 7-8
    sprite('mk052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('mk052_04', 1)	# 1-1
    sprite('mk052_04', 1)	# 2-2
    sprite('mk052_04', 2)	# 3-4
    sprite('mk052_03', 2)	# 5-6
    sprite('mk052_02', 2)	# 7-8
    sprite('mk052_01', 2)	# 9-10
    sprite('mk052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('mk054_00', 1)	# 1-1
    sprite('mk054_01', 1)	# 2-2
    sprite('mk054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('mk054_01', 1)	# 1-1
    sprite('mk054_02', 1)	# 2-2
    sprite('mk054_01', 2)	# 3-4
    sprite('mk054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('mk054_02', 1)	# 1-1
    sprite('mk054_03', 1)	# 2-2
    sprite('mk054_02', 2)	# 3-4
    sprite('mk054_01', 2)	# 5-6
    sprite('mk054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('mk054_03', 1)	# 1-1
    sprite('mk054_04', 1)	# 2-2
    sprite('mk054_03', 2)	# 3-4
    sprite('mk054_02', 2)	# 5-6
    sprite('mk054_01', 2)	# 7-8
    sprite('mk054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('mk054_04', 1)	# 1-1
    sprite('mk054_04', 1)	# 2-2
    sprite('mk054_04', 2)	# 3-4
    sprite('mk054_03', 2)	# 5-6
    sprite('mk054_02', 2)	# 7-8
    sprite('mk054_01', 2)	# 9-10
    sprite('mk054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('mk060_00', 8)	# 1-8
    label(0)
    sprite('mk060_01', 4)	# 9-12
    sprite('mk060_02', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('mk060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('mk062_07', 4)	# 1-4
    label(0)
    sprite('mk062_08', 4)	# 5-8
    sprite('mk062_09', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('mk062_10', 2)	# 1-2

@State
def CmnActBDownBound():
    sprite('mk063_06', 2)	# 1-2
    sprite('mk063_07', 2)	# 3-4
    sprite('mk063_08', 3)	# 5-7
    sprite('mk063_09', 3)	# 8-10
    sprite('mk063_10', 3)	# 11-13

@State
def CmnActBDownLoop():
    sprite('mk063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('mk064_00', 2)	# 1-2
    sprite('mk064_01', 2)	# 3-4
    sprite('mk064_02', 2)	# 5-6
    sprite('mk064_03', 2)	# 7-8
    sprite('mk064_04', 2)	# 9-10
    sprite('mk064_05', 2)	# 11-12
    sprite('mk064_06', 2)	# 13-14
    sprite('mk064_07', 2)	# 15-16
    sprite('mk064_08', 2)	# 17-18
    sprite('mk064_09', 2)	# 19-20
    sprite('mk064_10', 2)	# 21-22

@State
def CmnActFDownUpper():
    sprite('mk063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('mk063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('mk063_02', 3)	# 1-3
    sprite('mk063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('mk063_04', 3)	# 1-3
    sprite('mk063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('mk063_06', 2)	# 1-2
    sprite('mk063_07', 2)	# 3-4
    sprite('mk063_08', 3)	# 5-7
    sprite('mk063_09', 3)	# 8-10
    sprite('mk063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('mk063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('mk064_00', 2)	# 1-2
    sprite('mk064_01', 2)	# 3-4
    sprite('mk064_02', 2)	# 5-6
    sprite('mk064_03', 2)	# 7-8
    sprite('mk064_04', 2)	# 9-10
    sprite('mk064_05', 2)	# 11-12
    sprite('mk064_06', 2)	# 13-14
    sprite('mk064_07', 2)	# 15-16
    sprite('mk064_08', 2)	# 17-18
    sprite('mk064_09', 2)	# 19-20
    sprite('mk064_10', 2)	# 21-22

@State
def CmnActVDownUpper():
    sprite('mk062_00', 3)	# 1-3
    label(0)
    sprite('mk062_01', 3)	# 4-6
    sprite('mk062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('mk062_03', 3)	# 1-3
    sprite('mk062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('mk062_05', 3)	# 1-3
    sprite('mk062_06', 3)	# 4-6
    sprite('mk062_07', 3)	# 7-9
    label(0)
    sprite('mk062_08', 3)	# 10-12
    sprite('mk062_09', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('mk062_10', 2)	# 1-2

@State
def CmnActBlowoff():
    sprite('mk072_00', 3)	# 1-3
    sprite('mk072_01', 3)	# 4-6
    sprite('mk072_02', 3)	# 7-9
    label(0)
    sprite('mk072_01', 3)	# 10-12
    sprite('mk072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('mk074_00', 3)	# 1-3
    sprite('mk074_01', 3)	# 4-6
    sprite('mk074_02', 3)	# 7-9
    sprite('mk074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('mk082_00', 2)	# 1-2
    sprite('mk082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('mk071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('mk073_00', 3)	# 1-3
    sprite('mk073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('mk073_02', 3)	# 1-3
    label(0)
    sprite('mk073_03', 3)	# 4-6
    sprite('mk073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('mk070_00', 3)	# 1-3
    sprite('mk070_01', 3)	# 4-6
    label(0)
    sprite('mk070_02', 3)	# 7-9
    sprite('mk070_03', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('mk070_04', 4)	# 1-4
    sprite('mk070_05', 4)	# 5-8
    sprite('mk070_06', 4)	# 9-12
    sprite('mk070_07', 4)	# 13-16
    sprite('mk070_08', 4)	# 17-20
    sprite('mk070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('mk070_10', 5)	# 1-5
    sprite('mk070_11', 2)	# 6-7
    sprite('mk070_12', 3)	# 8-10
    sprite('mk070_13', 3)	# 11-13

@State
def CmnActUkemiAirF():
    sprite('mk113_00', 3)	# 1-3
    sprite('mk113_01', 3)	# 4-6
    sprite('mk113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('mk113_00', 3)	# 1-3
    sprite('mk113_01', 3)	# 4-6
    sprite('mk113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('mk113_00', 3)	# 1-3
    sprite('mk113_01', 3)	# 4-6
    sprite('mk113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('mk110_00', 2)	# 1-2
    sprite('mk110_01', 2)	# 3-4
    sprite('mk110_02', 2)	# 5-6
    sprite('mk110_03', 2)	# 7-8
    sprite('mk110_04', 2)	# 9-10
    sprite('mk110_06', 2)	# 11-12
    sprite('mk110_07', 2)	# 13-14
    sprite('mk110_08', 200)	# 15-214
    sprite('mk110_09', 2)	# 215-216

@State
def CmnActUkemiLandB():
    sprite('mk111_00', 3)	# 1-3
    sprite('mk111_01', 3)	# 4-6
    sprite('mk111_02', 3)	# 7-9
    sprite('mk111_03', 3)	# 10-12
    sprite('mk111_04', 3)	# 13-15
    sprite('mk111_06', 3)	# 16-18
    sprite('mk111_07', 200)	# 19-218
    sprite('mk111_08', 3)	# 219-221
    sprite('mk111_09', 3)	# 222-224

@State
def CmnActUkemiLandN():
    sprite('mk112_00', 2)	# 1-2
    sprite('mk112_01', 2)	# 3-4
    sprite('mk112_02', 2)	# 5-6
    sprite('mk112_03', 2)	# 7-8
    sprite('mk112_04', 2)	# 9-10
    sprite('mk112_05', 2)	# 11-12
    sprite('mk112_06', 2)	# 13-14
    sprite('mk112_07', 2)	# 15-16
    sprite('mk112_08', 2)	# 17-18
    sprite('mk112_09', 2)	# 19-20

@State
def CmnActUkemiLandNLanding():
    sprite('mk024_00', 3)	# 1-3
    sprite('mk024_01', 3)	# 4-6
    sprite('mk024_02', 3)	# 7-9
    sprite('mk024_03', 3)	# 10-12
    sprite('mk024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('mk040_00', 3)	# 1-3
    sprite('mk040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('mk040_02', 3)	# 1-3
    sprite('mk040_03', 3)	# 4-6
    sprite('mk040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('mk040_01', 3)	# 1-3
    sprite('mk040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('mk040_05', 2)	# 1-2
    label(0)
    sprite('mk040_02', 2)	# 3-4
    sprite('mk040_03', 2)	# 5-6
    sprite('mk040_04', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('mk040_01', 3)	# 1-3
    sprite('mk040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('mk041_00', 3)	# 1-3
    sprite('mk041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('mk041_02', 2)	# 1-2
    sprite('mk041_03', 2)	# 3-4
    sprite('mk041_04', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('mk041_01', 3)	# 1-3
    sprite('mk041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('mk041_05', 2)	# 1-2
    label(0)
    sprite('mk041_02', 2)	# 3-4
    sprite('mk041_03', 2)	# 5-6
    sprite('mk041_04', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('mk041_01', 3)	# 1-3
    sprite('mk041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('mk043_00', 3)	# 1-3
    sprite('mk043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('mk043_02', 2)	# 1-2
    sprite('mk043_03', 2)	# 3-4
    sprite('mk043_04', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('mk043_01', 3)	# 1-3
    sprite('mk043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('mk043_05', 2)	# 1-2
    label(0)
    sprite('mk043_02', 2)	# 3-4
    sprite('mk043_03', 2)	# 5-6
    sprite('mk043_04', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('mk043_01', 3)	# 1-3
    sprite('mk043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('mk045_00', 3)	# 1-3
    sprite('mk045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    sprite('mk045_02', 3)	# 1-3
    sprite('mk045_03', 3)	# 4-6
    sprite('mk045_04', 3)	# 7-9

@State
def CmnActAirGuardEnd():
    sprite('mk045_01', 3)	# 1-3
    sprite('mk045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('mk045_05', 2)	# 1-2
    label(0)
    sprite('mk045_02', 2)	# 3-4
    sprite('mk045_03', 2)	# 5-6
    sprite('mk045_04', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('mk045_01', 3)	# 1-3
    sprite('mk045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('mk090_00', 2)	# 1-2
    sprite('mk090_01', 2)	# 3-4
    sprite('mk090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('mk090_03', 6)	# 6-11
    sprite('mk090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('mk091_00', 2)	# 1-2
    sprite('mk091_01', 2)	# 3-4
    sprite('mk091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('mk091_03', 6)	# 6-11
    sprite('mk091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('mk092_00', 2)	# 1-2
    sprite('mk092_01', 2)	# 3-4
    sprite('mk092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('mk092_03', 6)	# 6-11
    sprite('mk092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('mk025_00', 4)	# 1-4
    sprite('mk025_01', 4)	# 5-8
    sprite('mk025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('mk040_02', 1)	# 1-1
    sprite('mk040_01', 3)	# 2-4
    sprite('mk040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('mk312_00', 2)	# 1-2
    sprite('mk312_01', 2)	# 3-4
    sprite('mk312_02', 2)	# 5-6
    sprite('mk312_03', 8)	# 7-14	 **attackbox here**
    sprite('mk312_04', 4)	# 15-18
    sprite('mk312_05', 3)	# 19-21
    sprite('mk312_06', 2)	# 22-23
    sprite('mk312_07', 2)	# 24-25

@State
def CmnActAirLockWait():
    sprite('mk045_02', 1)	# 1-1
    sprite('mk045_01', 3)	# 2-4
    sprite('mk045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('mk322_00', 2)	# 1-2
    sprite('mk322_01', 2)	# 3-4
    sprite('mk322_02', 8)	# 5-12
    sprite('mk322_03', 2)	# 13-14	 **attackbox here**
    sprite('mk322_04', 3)	# 15-17
    sprite('mk322_03', 2)	# 18-19	 **attackbox here**
    sprite('mk322_02', 2)	# 20-21

@State
def CmnActLandSpin():
    sprite('mk071_00', 3)	# 1-3
    sprite('mk071_01', 3)	# 4-6
    label(0)
    sprite('mk071_02', 2)	# 7-8
    sprite('mk071_03', 2)	# 9-10
    sprite('mk071_04', 2)	# 11-12
    sprite('mk071_05', 2)	# 13-14
    sprite('mk071_06', 2)	# 15-16
    sprite('mk071_07', 2)	# 17-18
    sprite('mk071_08', 2)	# 19-20
    sprite('mk071_09', 2)	# 21-22
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('mk071_10', 6)	# 1-6
    sprite('mk071_11', 5)	# 7-11
    sprite('mk071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('mk071_02', 2)	# 1-2
    sprite('mk071_03', 2)	# 3-4
    sprite('mk071_04', 2)	# 5-6
    sprite('mk071_05', 2)	# 7-8
    sprite('mk071_06', 2)	# 9-10
    sprite('mk071_07', 2)	# 11-12
    sprite('mk071_08', 2)	# 13-14
    sprite('mk071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('mk077_00', 2)	# 1-2
    sprite('mk077_01', 2)	# 3-4
    sprite('mk077_00ex01', 2)	# 5-6
    sprite('mk077_01ex01', 2)	# 7-8
    sprite('mk077_00ex02', 2)	# 9-10
    sprite('mk077_01ex02', 2)	# 11-12
    sprite('mk077_00ex03', 2)	# 13-14
    sprite('mk077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('mk077_02', 4)	# 1-4
    label(0)
    sprite('mk077_03', 3)	# 5-7
    sprite('mk077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('mk077_05', 5)	# 1-5
    sprite('mk077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('mk060_07', 3)	# 1-3
    sprite('mk060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('mk060_11', 4)	# 1-4
    sprite('mk060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('mk331_00', 2)	# 1-2
    sprite('mk331_01', 2)	# 3-4
    label(0)
    sprite('mk331_02', 3)	# 5-7
    sprite('mk331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('mk331_04', 2)	# 1-2
    sprite('mk331_05', 2)	# 3-4
    label(0)
    sprite('mk331_06', 3)	# 5-7
    sprite('mk331_07', 3)	# 8-10
    sprite('mk331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('mk331_09', 3)	# 1-3
    sprite('mk331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('mk332_00', 2)	# 1-2
    sprite('mk332_01', 2)	# 3-4
    label(0)
    sprite('mk332_02', 3)	# 5-7
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('mk332_03', 2)	# 1-2
    sprite('mk332_04', 2)	# 3-4
    sprite('mk332_05', 2)	# 5-6
    label(0)
    sprite('mk332_06', 2)	# 7-8
    sprite('mk332_07', 2)	# 9-10
    sprite('mk332_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('mk020_05', 3)	# 1-3
    sprite('mk020_06', 3)	# 4-6
    label(0)
    sprite('mk020_07', 4)	# 7-10
    sprite('mk020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('mk333_00', 3)	# 1-3
    sprite('mk333_01', 3)	# 4-6
    sprite('mk333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('mk333_03', 32767)	# 10-32776
    GFX_0('EMB_MK_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('mk333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('mk333_05', 3)	# 4-6
    sprite('mk333_06', 3)	# 7-9
    sprite('mk333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('mk333_08', 4)	# 1-4
    sprite('mk333_09', 4)	# 5-8
    sprite('mk333_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('mk333_11', 3)	# 1-3
    sprite('mk333_12', 3)	# 4-6
    sprite('mk333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('mk333_14', 32767)	# 10-32776
    GFX_0('EMB_MK_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('mk333_15', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('mk333_05ex00', 3)	# 4-6
    sprite('mk333_06ex00', 3)	# 7-9
    sprite('mk333_07ex00', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('mk333_16', 4)	# 1-4
    sprite('mk333_17', 4)	# 5-8
    sprite('mk333_18', 4)	# 9-12
    label(0)
    sprite('mk020_07', 4)	# 13-16
    sprite('mk020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('mk333_00', 3)	# 1-3
    sprite('mk333_01', 3)	# 4-6
    sprite('mk333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('mk333_03', 32767)	# 10-32776
    GFX_0('EMB_MK_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('mk333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('mk333_05', 3)	# 4-6
    sprite('mk333_06', 3)	# 7-9
    sprite('mk333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('mk333_08', 4)	# 1-4
    sprite('mk333_09', 4)	# 5-8
    sprite('mk333_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('mk333_11', 3)	# 1-3
    sprite('mk333_12', 3)	# 4-6
    sprite('mk333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('mk333_14', 32767)	# 10-32776
    GFX_0('EMB_MK_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('mk333_15', 3)	# 1-3
    label(0)
    sprite('mk333_05ex00', 3)	# 4-6
    sprite('mk333_06ex00', 3)	# 7-9
    sprite('mk333_07ex00', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('mk333_16', 4)	# 1-4
    sprite('mk333_17', 4)	# 5-8
    sprite('mk333_18', 4)	# 9-12
    label(0)
    sprite('mk020_07', 4)	# 13-16
    sprite('mk020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('mk331_00', 2)	# 1-2
    sprite('mk331_01', 2)	# 3-4
    label(0)
    sprite('mk331_02', 4)	# 5-8
    sprite('mk331_03', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('mk331_04', 2)	# 1-2
    sprite('mk331_05', 2)	# 3-4
    label(0)
    sprite('mk331_06', 3)	# 5-7
    sprite('mk331_07', 3)	# 8-10
    sprite('mk331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('mk331_09', 3)	# 1-3
    sprite('mk331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('mk332_00', 2)	# 1-2
    sprite('mk332_01', 2)	# 3-4
    label(0)
    sprite('mk332_02', 3)	# 5-7
    sprite('mk332_03', 2)	# 8-9
    sprite('mk332_04', 2)	# 10-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('mk332_05', 2)	# 1-2
    label(0)
    sprite('mk332_06', 2)	# 3-4
    sprite('mk332_07', 2)	# 5-6
    sprite('mk332_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('mk332_09', 3)	# 1-3
    sprite('mk332_10', 3)	# 4-6
    label(0)
    sprite('mk020_07', 4)	# 7-10
    sprite('mk020_08', 4)	# 11-14
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
    sprite('mk300_00', 4)	# 1-4
    loopRest()
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    SFX_0('301_overdrive_end')
    sprite('mk300_01', 4)	# 5-8
    sprite('mk300_02', 4)	# 9-12
    sprite('mk300_03', 4)	# 13-16
    sprite('mk300_04', 16)	# 17-32
    sprite('mk300_03', 16)	# 33-48
    sprite('mk300_05', 4)	# 49-52
    sprite('mk300_06', 5)	# 53-57
    sprite('mk300_07', 5)	# 58-62

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('mk045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('mk045_00', 3)	# 2-4
    sprite('mk045_01', 4)	# 5-8
    label(0)
    sprite('mk045_02', 5)	# 9-13
    sprite('mk045_02', 5)	# 14-18
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
    sprite('mk045_01', 6)	# 19-24
    sprite('mk045_00', 6)	# 25-30

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('mk321_13', 3)	# 26-28	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    label(1)
    sprite('mk321_13ex', 3)	# 29-31	 **attackbox here**
    sprite('mk321_14ex', 3)	# 32-34	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('mk321_13ex', 3)	# 35-37	 **attackbox here**
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    sprite('mk321_15', 4)	# 38-41
    StartMultihit()
    sprite('mk321_16', 3)	# 42-44
    Recovery()
    sprite('mk321_17', 3)	# 45-47
    sprite('mk321_18', 3)	# 48-50
    sprite('mk321_19', 3)	# 51-53
    sprite('mk321_20', 3)	# 54-56
    sprite('mk321_21', 3)	# 57-59

@State
def CmnActChangePartnerQuickIn():
    sprite('mk032_06', 4)	# 1-4
    sprite('mk032_07', 5)	# 5-9
    Unknown8006(100, 1, 1)
    sprite('mk032_09', 14)	# 10-23
    sprite('mk032_10', 6)	# 24-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('mk033_01', 3)	# 1-3
    sprite('mk033_02', 3)	# 4-6
    sprite('mk033_03', 3)	# 7-9
    sprite('mk033_02', 3)	# 10-12
    sprite('mk033_03', 3)	# 13-15
    sprite('mk033_02', 3)	# 16-18
    sprite('mk033_03', 3)	# 19-21
    sprite('mk033_02', 3)	# 22-24
    sprite('mk033_03', 3)	# 25-27
    sprite('mk033_02', 3)	# 28-30
    sprite('mk033_03', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('mk033_00', 1)	# 1-1
    sprite('mk033_01', 2)	# 2-3
    sprite('mk033_02', 2)	# 4-5
    sprite('mk033_02', 1)	# 6-6
    sprite('mk033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('mk033_02', 3)	# 10-12
    sprite('mk033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mk033_04', 3)	# 16-18
    sprite('mk033_05', 3)	# 19-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('mk000_10', 8)	# 1-8
    sprite('mk000_11', 7)	# 9-15
    sprite('mk000_12', 7)	# 16-22
    sprite('mk000_13', 4)	# 23-26
    sprite('mk000_14', 8)	# 27-34
    sprite('mk000_15', 8)	# 35-42
    Unknown8002()
    sprite('mk000_11', 7)	# 43-49
    sprite('mk000_12', 7)	# 50-56
    sprite('mk000_13', 4)	# 57-60
    sprite('mk000_14', 8)	# 61-68
    sprite('mk000_15', 8)	# 69-76
    Unknown8002()

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(99)
    sprite('null', 2)	# 1-2
    label(98)
    sprite('mk020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('mk020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(98)
    label(99)
    sprite('mk024_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2200)
        AttackP1(70)
        AirUntechableTime(60)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(12000)
        Unknown11042(1)
        Unknown30040(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)

        def upon_3():
            if (SLOT_19 < 700000):
                clearUponHandler(3)
                sendToLabel(10)
        Unknown3029(1)
        Unknown3069(0)
        Unknown3070(2)
        Unknown3071(8)
    sprite('mk404_00', 3)	# 1-3
    sprite('mk404_00', 1)	# 4-4
    SFX_3('mkse_21')
    GFX_0('FakeBunshinStepB', 100)
    GFX_0('FakeBunshinStepC', 100)
    sprite('mk404_01', 1)	# 5-5
    physicsXImpulse(13000)
    sprite('mk404_02', 2)	# 6-7
    sprite('mk404_03', 2)	# 8-9
    Unknown1019(200)
    sprite('mk404_03', 2)	# 10-11
    sprite('mk404_04', 4)	# 12-15
    sprite('mk404_05', 4)	# 16-19
    sprite('mk404_06', 4)	# 20-23
    sprite('mk404_07', 4)	# 24-27
    sprite('mk404_08', 4)	# 28-31
    sprite('mk404_09', 4)	# 32-35
    loopRest()
    label(10)
    sprite('mk404_04', 2)	# 36-37
    clearUponHandler(3)
    Unknown1084(1)
    physicsXImpulse(10000)
    sprite('mk413_00', 2)	# 38-39
    physicsXImpulse(8000)
    sprite('mk413_01', 2)	# 40-41
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 42-44
    sprite('mk413_01', 3)	# 45-47
    physicsXImpulse(6000)
    sprite('mk413_02', 3)	# 48-50
    sprite('mk413_01', 3)	# 51-53
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 54-56
    sprite('mk413_01', 3)	# 57-59
    sprite('keep', 1)	# 60-60
    SFX_4('mk215')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv3')
    sprite('mk413_04', 3)	# 61-63
    Unknown7015()
    SFX_3('mkse_03')
    Unknown2015(150)
    physicsXImpulse(100000)
    Unknown8007(100, 1, 1)
    sprite('mk413_05', 6)	# 64-69	 **attackbox here**
    Unknown1019(60)
    ScreenShake(0, 35000)
    GFX_0('mkef413_lv3', -1)
    GFX_1('mkef_Lv3Puncheairwall', 0)
    loopRest()
    sprite('mk413_06', 4)	# 70-73
    Unknown1019(30)
    Unknown2015(-1)
    Unknown8010(100, 1, 1)
    Recovery()
    sprite('mk413_07', 4)	# 74-77
    Unknown8010(100, 1, 1)
    sprite('mk404_12', 3)	# 78-80
    sprite('mk404_13', 3)	# 81-83

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        AttackLevel_(5)
        Damage(2000)
        AttackP1(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9190(1)
        Unknown9118(50)
        AirPushbackY(-67000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(50)
        Unknown9310(1)
        PushbackX(19800)
        Unknown11042(1)
        Unknown11058('0100000000000000000000000000000000000000')
        clearUponHandler(2)
        sendToLabelUpon(2, 11)
        Unknown3029(1)
        Unknown3069(0)
        Unknown22004(9, 1)
        Unknown30040(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('mk023_00', 3)	# 1-3
    sprite('mk023_00', 1)	# 4-4
    SFX_3('mkse_21')
    GFX_0('FakeBunshinStepA', 100)
    GFX_0('FakeBunshinStepB', 100)
    sprite('mk023_01', 2)	# 5-6
    sprite('mk411_00', 4)	# 7-10
    physicsXImpulse(35000)
    physicsYImpulse(42000)
    setGravity(2200)

    def upon_3():
        if (SLOT_19 <= 150000):
            Unknown1019(45)
    Unknown22003(-1)
    Unknown22001(-1)
    sprite('mk411_01', 4)	# 11-14
    label(10)
    sprite('mk402_00', 2)	# 15-16
    clearUponHandler(3)
    Unknown1019(15)
    YAccel(80)
    setGravity(900)
    sprite('mk402_01', 2)	# 17-18
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAuraAir', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk402_03', 1)	# 19-19
    Unknown7015()
    Unknown3029(0)
    sprite('mk402_03', 1)	# 20-20
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572614169720000000000000000000000000000fe03000000000000')
    callSubroutine('AfterImage_Lv3')
    Unknown7007('626d6b3231335f30000000000000000064000000626d6b3231335f31000000000000000064000000626d6b3231335f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('mkse_03')
    sprite('mk402_04', 1)	# 21-21
    setGravity(3100)
    sprite('mk402_05', 2)	# 22-23
    sprite('mk402_06', 2)	# 24-25
    GFX_0('PowerDunkAirwallLv3', 0)
    sprite('mk402_07ex', 20)	# 26-45	 **attackbox here**
    GFX_0('DriveLv3PunchefPowerDunk', 0)
    sprite('mk402_08', 3)	# 46-48
    sprite('mk402_09', 3)	# 49-51
    sprite('mk402_10', 3)	# 52-54
    sprite('mk402_11', 3)	# 55-57
    loopRest()
    label(11)
    sprite('mk024_00', 3)	# 58-60
    Unknown1084(1)
    sprite('mk024_01', 3)	# 61-63
    sprite('mk024_02', 3)	# 64-66
    sprite('mk024_03', 3)	# 67-69
    sprite('mk024_04', 3)	# 70-72

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        AirUntechableTime(22)
        Hitstop(4)
        Unknown11028(11)
        PushbackX(10000)
        AirPushbackY(15000)
        Unknown11056(0)
        Unknown11042(1)
        Unknown3029(1)
        Unknown3069(0)
        Unknown30040(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('mk404_00', 3)	# 1-3
    sprite('mk404_00', 1)	# 4-4
    SFX_3('mkse_21')
    GFX_0('FakeBunshinStepB', 100)
    GFX_0('FakeBunshinStepC', 100)
    sprite('mk404_01', 1)	# 5-5
    physicsXImpulse(13000)
    sprite('mk404_02', 2)	# 6-7
    sprite('mk404_03', 2)	# 8-9

    def upon_3():
        if (SLOT_19 < 180000):
            clearUponHandler(3)
            sendToLabel(10)
    Unknown1019(200)
    sprite('mk404_03', 2)	# 10-11
    sprite('mk404_04', 4)	# 12-15
    sprite('mk404_05', 4)	# 16-19
    sprite('mk404_06', 4)	# 20-23
    sprite('mk404_07', 4)	# 24-27
    loopRest()
    label(10)
    clearUponHandler(3)
    sprite('mk410_00', 2)	# 28-29
    sprite('mk410_01', 2)	# 30-31
    sprite('mk410_02', 2)	# 32-33
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_03', 2)	# 34-35	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    sprite('mk410_04', 2)	# 36-37
    Unknown1019(200)
    sprite('mk410_05', 2)	# 38-39
    sprite('mk410_06', 2)	# 40-41
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_07', 2)	# 42-43	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    sprite('mk410_08', 2)	# 44-45
    physicsXImpulse(8000)
    sprite('mk410_09', 2)	# 46-47
    sprite('mk410_10', 2)	# 48-49
    sprite('mk410_11', 2)	# 50-51
    Unknown7007('626d6b3231325f30000000000000000064000000626d6b3231325f31000000000000000064000000626d6b3231325f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_12', 4)	# 52-55	 **attackbox here**
    Unknown1019(0)
    Damage(2000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirUntechableTime(40)
    Hitstop(7)
    AirPushbackX(8000)
    AirPushbackY(30000)
    RefreshMultihit()
    sprite('mk410_13', 12)	# 56-67
    Recovery()
    Unknown3029(0)
    sprite('mk410_14', 4)	# 68-71
    sprite('mk410_15', 4)	# 72-75
    sprite('mk410_16', 4)	# 76-79
    sprite('mk410_17', 4)	# 80-83
    sprite('mk410_18', 4)	# 84-87
    sprite('mk410_19', 4)	# 88-91

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
    Unknown2036(134, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-245000)
    Unknown1019(4)
    label(0)
    sprite('mk020_07', 4)	# 3-6
    sprite('mk020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('BigPunchDD_OD')
    else:
        enterState('BigPunchDD')

@State
def BigPunchDD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        Unknown1084(0)
        Unknown2003(1)
        Unknown2004(1, 0)
        Unknown30063(1)
        Unknown23158('3c0000004b000000')
        Unknown23029(4, 1065, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk430_00', 4)	# 1-4
    Unknown23008(0, 0)
    setInvincible(1)
    sprite('mk430_01', 16)	# 5-20
    sprite('mk430_02', 4)	# 21-24
    sprite('mk430_03', 4)	# 25-28
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargeWind', 1)
    sprite('mk430_04', 3)	# 29-31
    sprite('mk430_05', 3)	# 32-34
    loopRest()
    label(1)
    label(2)
    label(3)
    sprite('mk430_04', 3)	# 35-37
    GFX_0('BigPunch_SE', -1)
    sprite('mk430_05', 3)	# 38-40
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk430_06', 7)	# 41-47
    sprite('mk430_07', 8)	# 48-55
    sprite('mk430_08', 9)	# 56-64
    sprite('mk430_09', 10)	# 65-74
    sprite('mk430_10', 12)	# 75-86
    GFX_0('mkef_circle_middle', 1)
    GFX_0('mkef_circle_large', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 11)	# 87-97
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_430circlering_lv3', 1)
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk430_12', 4)	# 98-101
    ScreenShake(8000, 0)
    sprite('mk430_13', 4)	# 102-105
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 3)	# 106-108	 **attackbox here**
    GFX_0('mk430cutin_lv3Duo', -1)
    GFX_0('DriveLv3PunchefD', 1)
    GFX_0('mkef_jumpsmoke23', 2)
    ScreenShake(0, 35000)
    callSubroutine('AfterImage_Lv3')
    loopRest()
    gotoLabel(29)
    label(29)
    sprite('mk430_15', 3)	# 109-111	 **attackbox here**
    sprite('mk430_14', 3)	# 112-114	 **attackbox here**
    setInvincible(0)
    sprite('mk430_15', 3)	# 115-117	 **attackbox here**
    sprite('mk430_14', 3)	# 118-120	 **attackbox here**
    sprite('mk430_15', 3)	# 121-123	 **attackbox here**
    sprite('mk430_14', 4)	# 124-127	 **attackbox here**
    sprite('mk430_15', 4)	# 128-131	 **attackbox here**
    sprite('mk430_14', 5)	# 132-136	 **attackbox here**
    sprite('mk430_15', 5)	# 137-141	 **attackbox here**
    sprite('mk430_16', 5)	# 142-146	 **attackbox here**
    sprite('mk430_17', 5)	# 147-151
    sprite('mk430_18', 5)	# 152-156
    sprite('mk430_19', 5)	# 157-161
    sprite('mk430_20', 5)	# 162-166

@State
def BigPunchDD_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown1084(0)
        Unknown2003(1)
        Unknown2004(1, 0)
        Unknown30063(1)
        Unknown23158('3c0000004b000000')
        Unknown23029(4, 1065, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk430_00', 4)	# 1-4
    Unknown23008(0, 0)
    setInvincible(1)
    sprite('mk430_01', 16)	# 5-20
    sprite('mk430_02', 4)	# 21-24
    sprite('mk430_03', 4)	# 25-28
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargeWind', 1)
    sprite('mk430_04', 3)	# 29-31
    sprite('mk430_05', 3)	# 32-34
    sprite('mk430_04', 3)	# 35-37
    sprite('mk430_05', 3)	# 38-40
    loopRest()
    label(1)
    label(2)
    label(3)
    sprite('mk430_04', 3)	# 41-43
    GFX_0('BigPunch_SE', -1)
    sprite('mk430_05', 3)	# 44-46
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk430_06', 7)	# 47-53
    sprite('mk430_07', 8)	# 54-61
    sprite('mk430_08', 9)	# 62-70
    sprite('mk430_09', 8)	# 71-78
    sprite('mk430_10', 9)	# 79-87
    GFX_0('mkef_circle_middle', 1)
    GFX_0('mkef_circle_large', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 12)	# 88-99
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_430circlering_lv3', 1)
    GFX_0('DriveChargelightning', 0)
    Unknown23119(8421376, 10, 1)
    ScreenShake(6000, 0)
    sprite('mk430_12', 3)	# 100-102
    ScreenShake(8000, 0)
    sprite('mk430_13', 3)	# 103-105
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 3)	# 106-108	 **attackbox here**
    GFX_0('mk430cutin_lvGDuo', -1)
    GFX_0('DriveLvG_PunchefD', 1)
    GFX_0('mkef_jumpsmoke23', 2)
    ScreenShake(0, 35000)
    callSubroutine('AfterImage_LvG')
    sprite('mk430_15', 3)	# 109-111	 **attackbox here**
    sprite('mk430_14', 3)	# 112-114	 **attackbox here**
    setInvincible(0)
    sprite('mk430_15', 3)	# 115-117	 **attackbox here**
    sprite('mk430_14', 3)	# 118-120	 **attackbox here**
    sprite('mk430_15', 3)	# 121-123	 **attackbox here**
    sprite('mk430_14', 4)	# 124-127	 **attackbox here**
    sprite('mk430_15', 4)	# 128-131	 **attackbox here**
    sprite('mk430_14', 5)	# 132-136	 **attackbox here**
    Unknown23119(0, 10, 1)
    sprite('mk430_15', 5)	# 137-141	 **attackbox here**
    sprite('mk430_16', 5)	# 142-146	 **attackbox here**
    sprite('mk430_17', 5)	# 147-151
    sprite('mk430_18', 5)	# 152-156
    sprite('mk430_19', 5)	# 157-161
    sprite('mk430_20', 5)	# 162-166

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('mk300_00', 4)	# 1-4
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('mk300_01', 4)	# 5-8
    sprite('mk300_02', 4)	# 9-12
    sprite('mk300_03', 4)	# 13-16
    sprite('mk300_04', 8)	# 17-24
    sprite('mk300_03', 8)	# 25-32
    sprite('mk300_04', 8)	# 33-40
    sprite('mk300_03', 8)	# 41-48
    sprite('mk300_04', 8)	# 49-56
    sprite('mk300_05', 4)	# 57-60
    sprite('mk300_06', 5)	# 61-65
    sprite('mk300_07', 5)	# 66-70
    label(1)
    sprite('mk300_07', 1)	# 71-71
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('mk000_00', 3)	# 72-74
    sprite('mk000_01', 3)	# 75-77
    sprite('mk000_02', 3)	# 78-80
    sprite('mk000_03', 3)	# 81-83

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
    sprite('mk321_13', 3)	# 121-123	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('mk321_13ex', 2)	# 124-125	 **attackbox here**
    sprite('mk321_14ex', 2)	# 126-127	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('mk321_13', 4)	# 128-131	 **attackbox here**
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 5000)
    StartMultihit()
    sprite('mk321_15', 4)	# 132-135
    StartMultihit()
    sprite('mk321_16', 3)	# 136-138
    sprite('mk321_17', 4)	# 139-142
    sprite('mk321_18', 4)	# 143-146
    sprite('mk321_19', 4)	# 147-150
    sprite('mk321_20', 4)	# 151-154
    sprite('mk321_21', 4)	# 155-158

@State
def CmnActChangeReturnAppealBurst():
    sprite('mk111_07', 4)	# 1-4
    sprite('mk111_08', 50)	# 5-54
    sprite('mk111_09', 50)	# 55-104

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown11050('020000006d6b65665f6869745f6d6964646c650000000000000000000000000000000000')
        AirPushbackY(10000)
        HitOrBlockCancel('Atk5AA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
    sprite('mk201_00', 3)	# 1-3
    sprite('mk201_01', 3)	# 4-6
    Unknown23153(65000)
    sprite('mk201_02', 1)	# 7-7
    Unknown23153(35000)
    sprite('mk201_03', 1)	# 8-8
    Unknown23153(20000)
    sprite('mk201_04', 1)	# 9-9	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    Unknown7009(0)
    Unknown23153(5000)
    sprite('mk201_04', 5)	# 10-14	 **attackbox here**
    sprite('mk201_05', 4)	# 15-18
    Recovery()
    Unknown2063()
    Unknown23153(5000)
    sprite('mk201_06', 3)	# 19-21
    Unknown23153(20000)
    sprite('mk201_07', 3)	# 22-24
    Unknown23153(-10000)
    sprite('mk201_08', 3)	# 25-27
    Unknown23153(-5000)
    sprite('mk201_09', 3)	# 28-30
    Unknown23153(-15000)

@State
def Atk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(10000)
        PushbackX(8000)
        Unknown11050('020000006d6b65665f6869745f6869676800000000000000000000000000000000000000')
        HitOrBlockCancel('Atk5AAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('mk202_00', 2)	# 1-2
    sprite('mk202_01', 4)	# 3-6
    sprite('mk202_02', 1)	# 7-7
    teleportRelativeX(50000)
    sprite('mk202_03ex01', 1)	# 8-8	 **attackbox here**
    teleportRelativeX(50000)
    GFX_1('mkef_smoke', 2)
    SFX_0('004_swing_grap_1_1')
    Unknown7009(1)
    sprite('mk202_03', 6)	# 9-14	 **attackbox here**
    sprite('mk202_03', 2)	# 15-16	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('mk202_04', 4)	# 17-20
    sprite('mk202_13', 2)	# 21-22
    sprite('mk202_14', 2)	# 23-24
    sprite('mk202_15', 3)	# 25-27
    sprite('mk202_16', 3)	# 28-30

@State
def Atk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(10000)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6869676800000000000000000000000000000000000000')
        Unknown9154(21)
        AirUntechableTime(24)
        HitOrBlockCancel('Atk5AAAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
    sprite('mk202_05', 4)	# 1-4
    sprite('mk202_06', 2)	# 5-6
    sprite('mk202_07', 6)	# 7-12	 **attackbox here**
    Unknown7009(1)
    SFX_0('004_swing_grap_1_1')
    RefreshMultihit()
    Unknown4048(-130000)
    Unknown4049(850)
    Unknown4045('6d6b65665f323032736d6f726b0000000000000000000000000000000000000000000000')
    sprite('mk202_08', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('mk202_09', 5)	# 17-21
    sprite('mk202_10', 5)	# 22-26
    sprite('mk202_11', 5)	# 27-31
    sprite('mk202_12', 5)	# 32-36

@State
def Atk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AirPushbackX(40000)
        Unknown11056(0)
        JumpCancel_(0)
        Unknown2004(1, 0)
        Unknown23158('0a0000000e000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1031, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk203_00', 2)	# 1-2
    sprite('mk203_01', 4)	# 3-6
    SLOT_55 = 1
    Unknown7014('mkse_01')
    teleportRelativeX(-70000)
    Unknown2015(150)
    sprite('mk203_02', 3)	# 7-9
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 1)
    sprite('mk203_03', 3)	# 10-12
    sprite('mk203_02', 3)	# 13-15
    sprite('mk203_03', 3)	# 16-18
    sprite('mk203_02', 3)	# 19-21
    GFX_0('DriveChargelightning', 1)
    sprite('mk203_03', 3)	# 22-24
    sprite('mk203_02', 3)	# 25-27
    sprite('mk203_03', 3)	# 28-30
    Unknown21015('447269766543686172676557696e6400000000000000000000000000000000000004000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk203_03', 5)	# 31-35
    sprite('mk203_01', 3)	# 36-38
    SLOT_55 = 0
    sprite('mk203_00', 3)	# 39-41
    teleportRelativeX(70000)
    loopRest()
    ExitState()
    label(1)
    AttackLevel_(4)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackY(12000)
    AirUntechableTime(60)
    sprite('mk203_04', 2)	# 42-43
    teleportRelativeX(50000)
    physicsXImpulse(50000)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv2')
    sprite('mk203_05', 1)	# 44-44
    SFX_0('004_swing_grap_1_1')
    ScreenShake(0, 5000)
    sprite('mk203_06', 2)	# 45-46
    Unknown1019(60)
    Unknown7015()
    Unknown7007('626d6b3130385f30000000000000000064000000626d6b3130385f31000000000000000064000000626d6b3130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('mk203_07ex01', 3)	# 47-49	 **attackbox here**
    Unknown1019(30)
    GFX_0('DriveLv2PunchefD', 0)
    loopRest()
    gotoLabel(99)
    label(2)
    AttackLevel_(5)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(60)
    Hitstop(15)
    sprite('mk203_04', 1)	# 50-50
    teleportRelativeX(50000)
    physicsXImpulse(75000)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv3')
    sprite('mk203_05', 1)	# 51-51
    Unknown8007(100, 1, 1)
    Unknown7015()
    SFX_3('mkse_03')
    ScreenShake(0, 35000)
    sprite('mk203_06', 2)	# 52-53
    Unknown7007('626d6b3130385f30000000000000000064000000626d6b3130385f31000000000000000064000000626d6b3130385f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('ShinigPunch_D', -1)
    sprite('mk203_07ex02', 3)	# 54-56	 **attackbox here**
    Unknown1019(60)
    GFX_0('DriveLv3PunchefD', 0)
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk203_08', 2)	# 57-58
    Unknown1019(0)
    Unknown2015(100)
    Recovery()
    Unknown2063()
    sprite('mk203_09', 2)	# 59-60
    sprite('mk203_10', 2)	# 61-62
    sprite('mk203_10ex00', 2)	# 63-64
    sprite('mk203_11', 2)	# 65-66
    sprite('mk203_12', 3)	# 67-69
    sprite('mk203_13', 3)	# 70-72
    sprite('mk203_14', 3)	# 73-75
    sprite('mk203_15', 3)	# 76-78
    sprite('mk203_16', 6)	# 79-84
    sprite('mk203_17', 3)	# 85-87

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('mk200_00', 1)	# 1-1
    Unknown1051(60)
    random_(2, 0, 34)
    if SLOT_0:
        _gotolabel(30)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(31)
    sprite('mk200_01ex01', 1)	# 2-2
    sprite('mk200_02ex01', 1)	# 3-3
    sprite('mk200_03', 1)	# 4-4
    sprite('mk200_04ex01', 1)	# 5-5	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    HitOrBlockCancel('Atk4A4th')
    sprite('mk200_04ex01', 1)	# 6-6	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A4th')
    sprite('mk200_01', 6)	# 7-12
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(30)
    sprite('mk200_01', 1)	# 13-13
    sprite('mk200_02', 1)	# 14-14
    sprite('mk200_03', 1)	# 15-15
    SFX_0('003_swing_grap_0_0')
    sprite('mk200_04', 1)	# 16-16	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk4A2nd')
    sprite('mk200_04', 1)	# 17-17	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A2nd')
    sprite('mk200_01ex00', 6)	# 18-23
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(31)
    sprite('mk200_01ex00', 1)	# 24-24
    sprite('mk200_02ex00', 1)	# 25-25
    sprite('mk200_03', 1)	# 26-26
    SFX_0('003_swing_grap_0_0')
    sprite('mk200_04ex00', 1)	# 27-27	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk4A3rd')
    sprite('mk200_04ex00', 1)	# 28-28	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A3rd')
    sprite('mk200_01ex01', 6)	# 29-34
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk200_00', 5)	# 35-39

@State
def Atk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(30)
    sprite('mk200_01ex01', 2)	# 1-2
    sprite('mk200_02ex01', 1)	# 3-3
    sprite('mk200_03', 1)	# 4-4
    sprite('mk200_04ex01', 1)	# 5-5	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    HitOrBlockCancel('Atk4A4th')
    sprite('mk200_04ex01', 1)	# 6-6	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A4th')
    sprite('mk200_01', 6)	# 7-12
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(30)
    sprite('mk200_01ex00', 2)	# 13-14
    SFX_0('003_swing_grap_0_0')
    sprite('mk200_02ex00', 1)	# 15-15
    sprite('mk200_03', 1)	# 16-16
    sprite('mk200_04ex00', 1)	# 17-17	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk4A3rd')
    sprite('mk200_04ex00', 1)	# 18-18	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A3rd')
    sprite('mk200_01ex01', 6)	# 19-24
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk200_00', 5)	# 25-29

@State
def Atk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(30)
    label(30)
    sprite('mk200_01', 2)	# 1-2
    SFX_0('003_swing_grap_0_0')
    sprite('mk200_02', 1)	# 3-3
    sprite('mk200_03', 1)	# 4-4
    sprite('mk200_04', 1)	# 5-5	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk4A2nd')
    sprite('mk200_04', 1)	# 6-6	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A2nd')
    sprite('mk200_01ex00', 6)	# 7-12
    Recovery()
    Unknown2063()
    gotoLabel(32)
    sprite('mk200_01ex01', 2)	# 13-14
    sprite('mk200_02ex01', 1)	# 15-15
    sprite('mk200_03', 1)	# 16-16
    sprite('mk200_04ex01', 2)	# 17-18	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    HitOrBlockCancel('Atk4A4th')
    sprite('mk200_04ex01', 1)	# 19-19	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A4th')
    sprite('mk200_01', 6)	# 20-25
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk200_00', 5)	# 26-30

@State
def Atk4A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(30)
    sprite('mk200_01ex00', 2)	# 1-2
    SFX_0('003_swing_grap_0_0')
    sprite('mk200_02ex00', 1)	# 3-3
    sprite('mk200_03', 1)	# 4-4
    sprite('mk200_04ex00', 1)	# 5-5	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk4A3rd')
    sprite('mk200_04ex00', 1)	# 6-6	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A3rd')
    sprite('mk200_01ex01', 6)	# 7-12
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(30)
    sprite('mk200_01', 2)	# 13-14
    SFX_0('003_swing_grap_0_0')
    sprite('mk200_02', 1)	# 15-15
    sprite('mk200_03', 1)	# 16-16
    sprite('mk200_04', 1)	# 17-17	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk4A2nd')
    sprite('mk200_04', 1)	# 18-18	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk4A2nd')
    sprite('mk200_01ex00', 6)	# 19-24
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk200_00', 5)	# 25-29

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(70)
        AirUntechableTime(26)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(28000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        Unknown2004(1, 0)
        HitOrBlockCancel('Atk5BB')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
    sprite('mk210_00', 1)	# 1-1
    sprite('mk210_02', 2)	# 2-3
    sprite('mk210_03', 1)	# 4-4
    sprite('mk210_03', 5)	# 5-9
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('mk210_04', 1)	# 10-10
    Unknown23153(64000)
    Unknown7009(1)
    SFX_0('004_swing_grap_1_1')
    physicsXImpulse(30000)
    sprite('mk210_05', 2)	# 11-12	 **attackbox here**
    Unknown1019(50)
    sprite('mk210_05', 2)	# 13-14	 **attackbox here**
    Unknown1019(30)
    sprite('mk210_06', 3)	# 15-17
    Unknown1019(20)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('mk210_07', 4)	# 18-21
    Unknown1019(10)
    sprite('mk210_08', 5)	# 22-26
    Unknown1019(0)
    sprite('mk210_09', 2)	# 27-28
    teleportRelativeX(-64000)
    sprite('mk210_10', 3)	# 29-31
    sprite('mk210_11', 3)	# 32-34
    sprite('mk210_12', 3)	# 35-37

@State
def Atk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        PushbackX(8000)
        AirPushbackX(8000)
        AirPushbackY(-62000)
        Unknown9310(1)
        AirUntechableTime(27)
        Unknown11050('020000006d6b65665f6869745f6d6964646c650000000000000000000000000000000000')
        HitOrBlockCancel('Atk5BBB')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('mk211_00', 3)	# 1-3
    sprite('mk211_01', 3)	# 4-6
    sprite('mk211_02', 3)	# 7-9
    teleportRelativeX(20000)
    Unknown7009(1)
    sprite('mk211_03', 2)	# 10-11
    teleportRelativeX(10000)
    sprite('mk211_04', 2)	# 12-13
    SFX_0('004_swing_grap_1_1')
    sprite('mk211_05', 3)	# 14-16	 **attackbox here**
    sprite('mk211_06', 4)	# 17-20
    Recovery()
    Unknown2063()
    sprite('mk211_07', 6)	# 21-26
    sprite('mk211_08', 6)	# 27-32
    teleportRelativeX(20000)
    sprite('mk211_09', 6)	# 33-38
    sprite('mk211_10', 6)	# 39-44

@State
def Atk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(8000)
        Unknown11058('0000000001000000000000000000000000000000')
        HitJumpCancel(1)
        Unknown18009(1)
        Unknown23158('0a0000000e000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1032, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk233_00', 3)	# 1-3
    sprite('mk233_01', 3)	# 4-6
    Unknown7014('mkse_01')
    sprite('mk233_02', 5)	# 7-11
    SLOT_55 = 1
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 1)
    sprite('mk233_03', 5)	# 12-16
    sprite('mk233_02', 5)	# 17-21
    sprite('mk233_03', 5)	# 22-26
    GFX_0('DriveChargelightning', 0)
    sprite('mk233_02', 5)	# 27-31
    sprite('mk233_03', 5)	# 32-36
    sprite('mk233_02', 5)	# 37-41
    Unknown21015('447269766543686172676557696e6400000000000000000000000000000000000004000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk233_03', 5)	# 42-46
    sprite('mk233_01', 3)	# 47-49
    SLOT_55 = 0
    sprite('mk233_00', 3)	# 50-52
    loopRest()
    ExitState()
    label(1)
    AttackLevel_(4)
    AirPushbackY(38000)
    AirUntechableTime(25)
    Unknown23159('NmlAtk2D_Lv2')
    sprite('mk233_04', 1)	# 53-53
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv2')
    sprite('mk233_05', 2)	# 54-55
    Unknown18009(0)
    physicsXImpulse(60000)
    sprite('mk233_06', 2)	# 56-57
    Unknown1019(50)
    Unknown7015()
    Unknown7007('626d6b3130385f30000000000000000064000000626d6b3130385f31000000000000000064000000626d6b3130385f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    ScreenShake(0, 5000)
    Unknown21015('447269766543686172676557696e6400000000000000000000000000000000000004000000000000')
    sprite('mk233_07', 2)	# 58-59
    Unknown1019(50)
    sprite('mk233_08', 1)	# 60-60
    Unknown1019(50)
    sprite('mk233_09', 1)	# 61-61
    Unknown1019(50)
    sprite('mk233_10ex01', 5)	# 62-66	 **attackbox here**
    Unknown1019(0)
    GFX_0('DriveLv2Punchef2D', 4)
    loopRest()
    gotoLabel(99)
    label(2)
    AttackLevel_(5)
    AttackP2(80)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(38000)
    AirUntechableTime(28)
    Hitstop(15)
    sprite('mk233_04', 1)	# 67-67
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv3')
    sprite('mk233_05', 2)	# 68-69
    Unknown18009(0)
    physicsXImpulse(86000)
    sprite('mk233_06', 2)	# 70-71
    Unknown1019(50)
    Unknown7015()
    Unknown7007('626d6b3130385f30000000000000000064000000626d6b3130385f31000000000000000064000000626d6b3130385f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('mkse_03')
    ScreenShake(0, 35000)
    Unknown21015('447269766543686172676557696e6400000000000000000000000000000000000004000000000000')
    sprite('mk233_07', 1)	# 72-72
    Unknown1019(50)
    sprite('mk233_08', 1)	# 73-73
    Unknown1019(50)
    sprite('mk233_09', 1)	# 74-74
    Unknown1019(50)
    sprite('mk233_10ex02', 5)	# 75-79	 **attackbox here**
    Unknown1019(0)
    GFX_0('DriveLv3Punchef2D', 4)
    GFX_0('ShinigPunch_2D', -1)
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk233_11', 4)	# 80-83
    Recovery()
    Unknown2063()
    sprite('mk233_12', 4)	# 84-87
    sprite('mk233_13', 4)	# 88-91
    sprite('mk233_14', 4)	# 92-95
    sprite('mk233_15', 4)	# 96-99
    sprite('mk233_16', 4)	# 100-103
    sprite('mk233_17', 4)	# 104-107
    sprite('mk233_18', 4)	# 108-111

@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(700)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(15000)
        PushbackX(8000)
        Unknown11050('020000006d6b65665f6869745f6869676800000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('Atk5C2nd')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitJumpCancel(1)
    sprite('mk202_00', 2)	# 1-2
    sprite('mk202_01', 4)	# 3-6
    sprite('mk202_02', 1)	# 7-7
    sprite('mk202_03ex01', 1)	# 8-8	 **attackbox here**
    teleportRelativeX(50000)
    GFX_1('mkef_smoke', 2)
    SFX_0('004_swing_grap_1_1')
    Unknown7009(2)
    sprite('mk202_03', 6)	# 9-14	 **attackbox here**
    sprite('mk202_03', 2)	# 15-16	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('mk202_04', 4)	# 17-20
    sprite('mk202_13', 2)	# 21-22
    sprite('mk202_14', 2)	# 23-24
    Unknown14085('NmlAtk6B')
    Unknown14085('NmlAtk6C')
    Unknown14085('NmlAtk2C')
    Unknown14085('NmlAtk3C')
    Unknown14085('NmlAtk5D')
    Unknown14085('NmlAtk2D')
    sprite('mk202_15', 3)	# 25-27
    sprite('mk202_16', 3)	# 28-30
    Unknown14085('Atk5C2nd')

@State
def Atk5C2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP2(82)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6869676800000000000000000000000000000000000000')
        Unknown9154(21)
        AirUntechableTime(24)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitJumpCancel(1)
    sprite('mk202_05', 4)	# 1-4
    sprite('mk202_06', 2)	# 5-6
    sprite('mk202_07', 6)	# 7-12	 **attackbox here**
    Unknown7009(2)
    SFX_0('004_swing_grap_1_1')
    RefreshMultihit()
    Unknown4048(-130000)
    Unknown4049(850)
    Unknown4045('6d6b65665f323032736d6f726b0000000000000000000000000000000000000000000000')
    sprite('mk202_08', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('mk202_09', 3)	# 17-19
    sprite('mk202_10', 3)	# 20-22
    sprite('mk202_11', 3)	# 23-25
    sprite('mk202_12', 3)	# 26-28

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('mk230_00', 1)	# 1-1
    Unknown1051(60)
    random_(2, 0, 34)
    if SLOT_0:
        _gotolabel(30)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(31)
    sprite('mk230_01ex01', 2)	# 2-3
    sprite('mk230_02ex01', 1)	# 4-4
    sprite('mk230_03', 1)	# 5-5
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_04ex01', 1)	# 6-6	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A4th')
    sprite('mk230_04ex01', 2)	# 7-8	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A4th')
    sprite('mk230_01', 5)	# 9-13
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(30)
    sprite('mk230_01', 2)	# 14-15
    sprite('mk230_02', 1)	# 16-16
    sprite('mk230_03', 1)	# 17-17
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    sprite('mk230_04', 1)	# 18-18	 **attackbox here**
    HitOrBlockCancel('Atk2A2nd')
    sprite('mk230_04', 2)	# 19-20	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A2nd')
    sprite('mk230_01ex00', 5)	# 21-25
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(31)
    sprite('mk230_01ex00', 2)	# 26-27
    sprite('mk230_02ex00', 1)	# 28-28
    sprite('mk230_03', 1)	# 29-29
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_04ex00', 1)	# 30-30	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A3rd')
    sprite('mk230_04ex00', 2)	# 31-32	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A3rd')
    sprite('mk230_01ex01', 5)	# 33-37
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk230_00', 5)	# 38-42

@State
def Atk2A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(30)
    sprite('mk230_02ex01', 2)	# 1-2
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_02ex01', 1)	# 3-3
    sprite('mk230_03', 1)	# 4-4
    sprite('mk230_04ex01', 1)	# 5-5	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A4th')
    sprite('mk230_04ex01', 2)	# 6-7	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A4th')
    sprite('mk230_01', 5)	# 8-12
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(30)
    sprite('mk230_02ex00', 2)	# 13-14
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_02ex00', 1)	# 15-15
    sprite('mk230_03', 1)	# 16-16
    sprite('mk230_04ex00', 1)	# 17-17	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A3rd')
    sprite('mk230_04ex00', 2)	# 18-19	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A3rd')
    sprite('mk230_01ex01', 5)	# 20-24
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk230_00', 5)	# 25-29

@State
def Atk2A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(30)
    sprite('mk230_02ex01', 2)	# 1-2
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_02ex01', 1)	# 3-3
    sprite('mk230_03', 1)	# 4-4
    sprite('mk230_04ex01', 1)	# 5-5	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A4th')
    sprite('mk230_04ex01', 2)	# 6-7	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A4th')
    sprite('mk230_01', 5)	# 8-12
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(30)
    sprite('mk230_02', 2)	# 13-14
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_02', 1)	# 15-15
    sprite('mk230_03', 1)	# 16-16
    sprite('mk230_04', 1)	# 17-17	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A2nd')
    sprite('mk230_04', 2)	# 18-19	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A2nd')
    sprite('mk230_01ex00', 5)	# 20-24
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk230_00', 5)	# 25-29

@State
def Atk2A4th():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(30)
    sprite('mk230_02ex00', 2)	# 1-2
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_02ex00', 1)	# 3-3
    sprite('mk230_03', 1)	# 4-4
    sprite('mk230_04ex00', 1)	# 5-5	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A3rd')
    sprite('mk230_04ex00', 2)	# 6-7	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A3rd')
    sprite('mk230_01ex01', 5)	# 8-12
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(30)
    sprite('mk230_02', 2)	# 13-14
    SFX_0('003_swing_grap_0_0')
    sprite('mk230_02', 1)	# 15-15
    sprite('mk230_03', 1)	# 16-16
    sprite('mk230_04', 1)	# 17-17	 **attackbox here**
    Unknown7009(0)
    HitOrBlockCancel('Atk2A2nd')
    sprite('mk230_04', 2)	# 18-19	 **attackbox here**
    WhiffCancelEnable(1)
    WhiffCancel('Atk2A2nd')
    sprite('mk230_01ex00', 5)	# 20-24
    Recovery()
    Unknown2063()
    gotoLabel(32)
    label(32)
    sprite('mk230_00', 5)	# 25-29

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        HitLow(2)
        Unknown11050('020000006d6b65665f6869745f6d6964646c650000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('mk231_00', 2)	# 1-2
    sprite('mk231_01', 3)	# 3-5
    sprite('mk231_01', 2)	# 6-7
    Unknown7009(1)
    SFX_0('003_swing_grap_0_2')
    sprite('mk231_02', 1)	# 8-8
    sprite('mk231_03', 3)	# 9-11	 **attackbox here**
    sprite('mk231_04', 2)	# 12-13
    Recovery()
    Unknown2063()
    sprite('mk231_05', 2)	# 14-15
    sprite('mk231_06', 3)	# 16-18
    sprite('mk231_07', 4)	# 19-22
    sprite('mk231_08', 4)	# 23-26

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(6000)
        AirPushbackY(14000)
        AirUntechableTime(40)
        Unknown2004(1, 0)
    sprite('mk234_00', 2)	# 1-2
    sprite('mk234_01', 2)	# 3-4
    sprite('mk234_01', 1)	# 5-5
    physicsXImpulse(18000)
    SFX_0('019_cloth_b')
    sprite('mk234_02', 3)	# 6-8
    setInvincible(1)
    Unknown22019('0100000001000000000000000000000000000000')
    GuardPoint_(0)
    Unknown7007('626d6b3130355f30000000000000000064000000626d6b3130355f31000000000000000064000000626d6b3130355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('mk234_03', 3)	# 9-11
    Unknown1019(80)
    sprite('mk234_04', 2)	# 12-13
    SFX_0('019_cloth_b')
    sprite('mk234_05', 2)	# 14-15
    Unknown1019(60)
    sprite('mk234_06', 2)	# 16-17
    sprite('mk234_07', 2)	# 18-19
    CheckInput(0x13)
    if SLOT_0:
        _gotolabel(48)
    sprite('mk234_08', 2)	# 20-21
    sprite('mk234_09', 2)	# 22-23
    physicsXImpulse(24000)
    sprite('mk234_10', 2)	# 24-25
    setInvincible(0)
    SFX_0('003_swing_grap_0_2')
    sprite('mk234_11', 2)	# 26-27
    sprite('mk234_12', 2)	# 28-29
    Unknown1019(80)
    sprite('mk234_13', 4)	# 30-33	 **attackbox here**
    Unknown2006()
    Unknown1019(60)
    sprite('mk234_14', 4)	# 34-37
    Recovery()
    Unknown2063()
    Unknown1019(60)
    sprite('mk234_15', 4)	# 38-41
    Unknown1019(0)
    sprite('mk010_02', 4)	# 42-45
    loopRest()
    ExitState()
    label(48)
    sprite('mk234_00', 2)	# 46-47
    sprite('mk234_01', 2)	# 48-49
    sprite('mk234_01', 1)	# 50-50
    physicsXImpulse(18000)
    SFX_0('019_cloth_b')
    sprite('mk234_02ex', 2)	# 51-52
    setInvincible(0)
    sprite('mk234_03ex', 2)	# 53-54
    Unknown1019(80)
    sprite('mk234_04ex', 2)	# 55-56
    SFX_0('019_cloth_b')
    sprite('mk234_05ex', 2)	# 57-58
    Unknown1019(60)
    sprite('mk234_06ex', 2)	# 59-60
    sprite('mk234_07ex', 2)	# 61-62

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown11050('020000006d6b65665f6869745f6d6964646c650000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('AtkAir5A2nd')
        WhiffCancel('AtkAir5A2nd')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('mk252_00', 2)	# 1-2
    sprite('mk252_01', 3)	# 3-5
    sprite('mk252_02', 3)	# 6-8
    sprite('mk252_03', 1)	# 9-9
    SFX_0('004_swing_grap_1_1')
    Unknown7009(4)
    sprite('mk252_04', 3)	# 10-12	 **attackbox here**
    sprite('mk252_05', 3)	# 13-15	 **attackbox here**
    WhiffCancelEnable(1)
    sprite('mk252_06', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('mk252_03', 3)	# 19-21
    sprite('mk252_02', 2)	# 22-23
    sprite('mk252_02', 1)	# 24-24
    WhiffCancelEnable(0)
    sprite('mk252_01', 2)	# 25-26

@State
def AtkAir5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown11050('020000006d6b65665f6869745f6869676800000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('mk252_07', 1)	# 1-1
    sprite('mk252_08', 1)	# 2-2
    sprite('mk252_09', 2)	# 3-4
    SFX_0('004_swing_grap_1_1')
    sprite('mk252_10', 3)	# 5-7	 **attackbox here**
    Unknown7009(4)
    sprite('mk252_11', 4)	# 8-11
    Recovery()
    Unknown2063()
    sprite('mk252_12', 4)	# 12-15
    sprite('mk252_13', 4)	# 16-19
    sprite('mk252_14', 5)	# 20-24
    sprite('mk252_15', 5)	# 25-29

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Unknown11050('020000006d6b65665f6869745f6d6964646c650000000000000000000000000000000000')
        AirHitstunAnimation(10)
        AirUntechableTime(26)
        AirPushbackY(30000)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('mk251_00', 3)	# 1-3
    sprite('mk251_01', 3)	# 4-6
    SFX_0('003_swing_grap_0_2')
    sprite('mk251_02', 4)	# 7-10
    sprite('mk251_03', 4)	# 11-14	 **attackbox here**
    Unknown7009(5)
    sprite('mk251_04', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('mk251_05', 3)	# 18-20
    sprite('mk251_06', 3)	# 21-23
    sprite('mk251_07', 3)	# 24-26

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP2(70)
        Unknown11050('020000006d6b65665f6869745f7461696c73700000000000000000000000000000000000')
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(10)
        AirPushbackY(-20000)
        AirUntechableTime(30)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            sendToLabel(1)
    sprite('mk253_00', 2)	# 1-2
    sprite('mk253_01', 3)	# 3-5
    clearUponHandler(2)

    def upon_LANDING():
        sendToLabel(9)
    Unknown1084(1)
    physicsYImpulse(20000)
    physicsXImpulse(10000)
    Unknown1043()
    setGravity(1500)
    sprite('mk253_02', 3)	# 6-8
    Unknown7007('626d6b3130355f30000000000000000064000000626d6b3130355f31000000000000000064000000626d6b3130355f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(2000)
    sprite('mk253_03', 5)	# 9-13
    label(0)
    sprite('mk253_05', 4)	# 14-17	 **attackbox here**
    sprite('mk253_04', 4)	# 18-21	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mk253_06', 4)	# 22-25	 **attackbox here**
    WhiffCancel('NmlAtkAIR5A')
    WhiffCancel('NmlAtkAIR5B')
    clearUponHandler(2)

    def upon_LANDING():
        sendToLabel(11)
    physicsYImpulse(12000)
    physicsXImpulse(3000)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('mk253_07', 2)	# 26-27
    sprite('mk253_09', 2)	# 28-29
    WhiffCancelEnable(1)
    sprite('mk253_10', 2)	# 30-31
    loopRest()
    label(10)
    sprite('mk020_07', 4)	# 32-35
    sprite('mk020_08', 4)	# 36-39
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('mk024_00', 1)	# 40-40
    clearUponHandler(2)
    WhiffCancelEnable(0)
    Unknown1084(1)
    sprite('mk024_01', 1)	# 41-41
    sprite('mk024_02', 2)	# 42-43
    sprite('mk024_03', 2)	# 44-45
    sprite('mk024_04', 2)	# 46-47
    ExitState()
    label(9)
    sprite('keep', 1)	# 48-48
    Unknown8000(100, 1, 1)
    StartMultihit()
    Unknown1084(1)
    Recovery()
    Unknown2063()
    sprite('mk024_00', 2)	# 49-50
    sprite('mk024_01', 2)	# 51-52
    sprite('mk024_02', 4)	# 53-56

@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AirUntechableTime(26)
        AirHitstunAnimation(10)
        AirPushbackY(27000)
        Unknown11050('020000006d6b65665f6869745f6c6f770000000000000000000000000000000000000000')
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockJumpCancel(1)
    sprite('mk210_00', 1)	# 1-1
    sprite('mk210_02', 2)	# 2-3
    sprite('mk210_03', 1)	# 4-4
    sprite('mk210_03', 5)	# 5-9
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('mk210_04', 1)	# 10-10
    Unknown23153(64000)
    Unknown7009(0)
    SFX_0('004_swing_grap_1_1')
    sprite('mk210_05', 4)	# 11-14	 **attackbox here**
    sprite('mk210_06', 3)	# 15-17
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('mk210_07', 4)	# 18-21
    sprite('mk210_08', 5)	# 22-26
    sprite('mk210_09', 2)	# 27-28
    teleportRelativeX(-64000)
    sprite('mk210_10', 3)	# 29-31
    sprite('mk210_11', 3)	# 32-34
    sprite('mk210_12', 3)	# 35-37

@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(750)
        AttackP1(80)
        Unknown11090(110)
        GroundedHitstunAnimation(3)
        PushbackX(8000)
        AirPushbackY(-42000)
        Unknown9190(1)
        Unknown9118(40)
        AirUntechableTime(24)
        HitOverhead(2)
        Unknown12051(2)
        Unknown11050('020000006d6b65665f6869745f6d6964646c650000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('Atk5C2nd')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
    sprite('mk211_00', 6)	# 1-6
    sprite('mk211_01', 4)	# 7-10
    sprite('mk211_01', 4)	# 11-14
    sprite('mk211_02', 3)	# 15-17
    teleportRelativeX(20000)
    SFX_1('mk104')
    sprite('mk211_03', 2)	# 18-19
    teleportRelativeX(10000)
    sprite('mk211_04', 2)	# 20-21
    SFX_0('004_swing_grap_1_1')
    sprite('mk211_05', 3)	# 22-24	 **attackbox here**
    sprite('mk211_06', 4)	# 25-28
    Recovery()
    Unknown2063()
    sprite('mk211_07', 4)	# 29-32
    sprite('mk211_08', 4)	# 33-36
    teleportRelativeX(20000)
    sprite('mk211_09', 4)	# 37-40
    sprite('mk211_10', 4)	# 41-44

@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(900)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(22000)
        AirUntechableTime(23)
        Unknown9168(35)
        Unknown11050('020000006d6b65665f6869745f6869676800000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
    sprite('mk212_00', 2)	# 1-2
    sprite('mk212_01', 4)	# 3-6
    sprite('mk212_02', 2)	# 7-8
    Unknown7009(2)
    sprite('mk212_03', 2)	# 9-10
    sprite('mk212_04', 2)	# 11-12
    physicsXImpulse(6000)
    teleportRelativeX(40000)
    sprite('mk212_05', 1)	# 13-13
    teleportRelativeX(15000)
    GFX_1('mkef_smoke', 0)
    sprite('mk212_06', 2)	# 14-15	 **attackbox here**
    physicsXImpulse(40000)
    SFX_0('004_swing_grap_1_1')
    sprite('mk212_06', 2)	# 16-17	 **attackbox here**
    Unknown1019(80)
    sprite('mk212_06', 2)	# 18-19	 **attackbox here**
    Unknown1019(60)
    sprite('mk212_06', 2)	# 20-21	 **attackbox here**
    Unknown1019(40)
    sprite('mk212_07', 3)	# 22-24
    physicsXImpulse(0)
    Recovery()
    Unknown2063()
    sprite('mk212_08', 3)	# 25-27
    teleportRelativeX(55000)
    sprite('mk212_09', 5)	# 28-32
    sprite('mk212_10', 5)	# 33-37
    sprite('mk212_11', 4)	# 38-41

@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        Unknown17013()
        loopRelated(17, 61)

        def upon_17():
            Unknown13019(1)
            Unknown13026(1)
            Unknown13015(1)
    if random_(2, 0, 10):
        sendToLabel(9)
    sprite('mk300_00', 6)	# 1-6
    sprite('mk300_01', 6)	# 7-12
    if random_(2, 0, 50):
        SFX_1('mk404')
    else:
        SFX_1('mk405')
    sprite('mk300_02', 6)	# 13-18
    sprite('mk300_03', 6)	# 19-24
    sprite('mk300_04', 6)	# 25-30
    sprite('mk300_05', 6)	# 31-36
    sprite('mk300_06', 6)	# 37-42
    sprite('mk300_07', 5)	# 43-47
    loopRest()
    ExitState()
    label(9)
    sprite('mk600_16', 7)	# 48-54
    sprite('mk600_15', 8)	# 55-62
    sprite('mk600_14', 2)	# 63-64
    SFX_0('004_swing_grap_1_0')
    SFX_1('mk300')
    sprite('mk600_10', 2)	# 65-66
    sprite('mk600_10', 6)	# 67-72
    if (not SLOT_6):
        GFX_0('DonguriShot', 100)
    sprite('mk600_11', 6)	# 73-78
    sprite('mk600_12', 6)	# 79-84
    sprite('mk600_13', 20)	# 85-104
    sprite('mk600_14', 8)	# 105-112
    Unknown2001()
    sprite('mk600_15', 8)	# 113-120
    sprite('mk600_16', 8)	# 121-128

@State
def DonguriThrow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown23027()
        loopRelated(17, 61)

        def upon_17():
            Unknown13019(1)
            Unknown13026(1)
            Unknown13015(1)
    sprite('mk600_16', 8)	# 1-8
    sprite('mk600_15', 8)	# 9-16
    sprite('mk600_14', 2)	# 17-18
    SFX_0('004_swing_grap_1_0')
    SFX_1('mk103')
    sprite('mk600_10', 2)	# 19-20
    sprite('mk600_10', 6)	# 21-26
    if (not SLOT_6):
        GFX_0('DonguriShot', 100)
    sprite('mk600_11', 6)	# 27-32
    sprite('mk600_12', 6)	# 33-38
    sprite('mk600_13', 20)	# 39-58
    sprite('mk600_14', 8)	# 59-66
    Unknown2001()
    sprite('mk600_15', 8)	# 67-74
    sprite('mk600_16', 8)	# 75-82

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('mk414_00', 3)	# 1-3
    sprite('mk414_00', 1)	# 4-4
    tag_voice(1, 'bmk156_0', 'bmk156_1', '', '')
    sprite('mk414_01', 3)	# 5-7
    Unknown4047(224, 224, 224)
    SFX_0('003_swing_grap_0_1')
    sprite('mk414_02', 3)	# 8-10
    sprite('mk414_03', 3)	# 11-13
    SFX_0('003_swing_grap_0_1')
    sprite('mk414_04', 2)	# 14-15
    sprite('mk414_05', 2)	# 16-17
    sprite('mk414_06', 4)	# 18-21
    physicsXImpulse(35000)
    SFX_0('004_swing_grap_1_2')
    sprite('mk414_07', 3)	# 22-24	 **attackbox here**
    GFX_0('GuardCrash', -1)
    physicsXImpulse(0)
    sprite('mk414_08', 5)	# 25-29
    sprite('mk414_09', 5)	# 30-34
    sprite('mk414_10', 5)	# 35-39
    sprite('mk414_11', 5)	# 40-44
    sprite('mk414_12', 4)	# 45-48

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
    sprite('mk414_08', 3)	# 2-4
    sprite('mk414_09', 3)	# 5-7
    sprite('mk414_10', 3)	# 8-10
    sprite('mk414_11', 3)	# 11-13
    sprite('mk414_12', 3)	# 14-16
    sprite('mk212_00', 2)	# 17-18
    sprite('mk212_01', 2)	# 19-20
    sprite('mk212_02', 2)	# 21-22
    sprite('mk212_03', 3)	# 23-25
    tag_voice(1, 'bmk157_0', 'bmk157_1', '', '')
    sprite('mk212_04', 3)	# 26-28
    sprite('mk212_05', 1)	# 29-29
    GFX_1('mkef_smoke', 0)
    sprite('mk212_06', 2)	# 30-31	 **attackbox here**
    physicsXImpulse(0)
    RefreshMultihit()
    SFX_0('004_swing_grap_1_1')
    sprite('mk212_06', 2)	# 32-33	 **attackbox here**
    Unknown1019(80)
    sprite('mk212_06', 2)	# 34-35	 **attackbox here**
    Unknown1019(60)
    sprite('mk212_06', 2)	# 36-37	 **attackbox here**
    Unknown1019(40)
    sprite('mk212_07', 3)	# 38-40
    physicsXImpulse(0)
    sprite('mk212_08', 3)	# 41-43
    sprite('mk212_09', 5)	# 44-48
    sprite('mk212_10', 5)	# 49-53
    sprite('mk212_11', 4)	# 54-57
    sprite('mk000_00', 5)	# 58-62
    sprite('mk000_01', 5)	# 63-67
    sprite('mk000_02', 6)	# 68-73
    sprite('mk000_03', 6)	# 74-79
    sprite('mk000_04', 5)	# 80-84
    sprite('mk000_05', 5)	# 85-89
    sprite('mk000_06', 6)	# 90-95
    sprite('mk000_07', 6)	# 96-101
    sprite('mk000_08', 5)	# 102-106
    sprite('mk000_09', 5)	# 107-111
    label(0)
    sprite('mk000_00', 5)	# 112-116
    sprite('mk000_01', 5)	# 117-121
    sprite('mk000_02', 6)	# 122-127
    sprite('mk000_03', 6)	# 128-133
    sprite('mk000_04', 5)	# 134-138
    sprite('mk000_05', 5)	# 139-143
    sprite('mk000_06', 6)	# 144-149
    sprite('mk000_07', 6)	# 150-155
    sprite('mk000_08', 5)	# 156-160
    sprite('mk000_09', 5)	# 161-165
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 166-166

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('mk412_00ex00', 2)	# 1-2
    sprite('mk412_01ex00', 2)	# 3-4
    SFX_3('mkse_04')
    sprite('mk412_02ex00', 2)	# 5-6
    sprite('mk410_09ex00', 2)	# 7-8
    sprite('mk410_10ex00', 3)	# 9-11
    sprite('mk410_11ex00', 3)	# 12-14
    SFX_0('004_swing_grap_1_1')
    sprite('mk440_01', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('mk440_01', 2)	# 16-17	 **attackbox here**
    sprite('mk440_02', 8)	# 18-25
    sprite('mk410_14ex00', 8)	# 26-33
    sprite('mk410_15ex00', 8)	# 34-41
    sprite('mk410_16ex00', 8)	# 42-49
    sprite('mk410_17ex00', 7)	# 50-56
    sprite('mk410_18ex00', 7)	# 57-63
    sprite('mk410_19ex00', 7)	# 64-70
    sprite('mk000_00', 5)	# 71-75
    sprite('mk000_01', 5)	# 76-80
    sprite('mk000_02', 6)	# 81-86
    sprite('mk000_03', 6)	# 87-92
    sprite('mk000_04', 5)	# 93-97
    sprite('mk000_05', 5)	# 98-102
    sprite('mk000_06', 6)	# 103-108
    sprite('mk000_07', 6)	# 109-114
    sprite('mk000_08', 5)	# 115-119
    sprite('mk000_09', 5)	# 120-124
    label(0)
    sprite('mk000_00', 5)	# 125-129
    sprite('mk000_01', 5)	# 130-134
    sprite('mk000_02', 6)	# 135-140
    sprite('mk000_03', 6)	# 141-146
    sprite('mk000_04', 5)	# 147-151
    sprite('mk000_05', 5)	# 152-156
    sprite('mk000_06', 6)	# 157-162
    sprite('mk000_07', 6)	# 163-168
    sprite('mk000_08', 5)	# 169-173
    sprite('mk000_09', 5)	# 174-178
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 179-179

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('mk403_06', 3)	# 1-3
    sprite('mk403_07', 3)	# 4-6
    sprite('mk403_08', 3)	# 7-9
    sprite('mk403_09', 3)	# 10-12
    tag_voice(0, 'bmk158_0', 'bmk158_1', '', '')
    sprite('mk403_10', 3)	# 13-15
    Unknown8006(100, 1, 1)
    Unknown8007(100, 1, 1)
    GFX_1('mkef_403speedline', 1)
    sprite('mk403_11', 4)	# 16-19	 **attackbox here**
    StartMultihit()
    SFX_3('mkse_03')
    GFX_0('BlockingSpeedLine', -1)
    GFX_1('mkef_403smoke', -1)
    sprite('mk403_12ex01', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('mk403_13', 4)	# 24-27
    sprite('mk403_14', 4)	# 28-31
    sprite('mk403_15', 4)	# 32-35
    sprite('mk403_16', 4)	# 36-39
    sprite('mk403_17', 4)	# 40-43
    sprite('mk403_18', 4)	# 44-47
    sprite('mk403_19', 4)	# 48-51
    sprite('mk003_00', 3)	# 52-54
    sprite('mk003_01', 3)	# 55-57
    sprite('mk003_02', 3)	# 58-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
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
    sprite('mk252_07', 2)	# 29-30
    StartMultihit()
    physicsXImpulse(7500)
    physicsYImpulse(-6500)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('mk252_08', 2)	# 31-32
    StartMultihit()
    physicsXImpulse(50000)
    physicsYImpulse(-39000)
    sprite('mk252_09', 9)	# 33-41
    sprite('mk252_10', 3)	# 42-44	 **attackbox here**
    RefreshMultihit()
    sprite('mk252_11', 3)	# 45-47
    sprite('mk252_12', 3)	# 48-50
    sprite('mk252_13', 3)	# 51-53
    sprite('mk252_14', 3)	# 54-56
    sprite('mk252_15', 3)	# 57-59
    label(1)
    sprite('mk024_00', 3)	# 60-62
    Unknown8000(100, 1, 1)
    setGravity(0)
    physicsYImpulse(0)
    Unknown1019(0)
    Unknown23087(0)
    sprite('mk024_01', 3)	# 63-65
    sprite('mk024_02', 3)	# 66-68
    sprite('mk024_03', 3)	# 69-71
    sprite('mk024_04', 3)	# 72-74
    sprite('mk000_00', 5)	# 75-79
    sprite('mk000_01', 5)	# 80-84
    sprite('mk000_02', 6)	# 85-90
    sprite('mk000_03', 6)	# 91-96
    sprite('mk000_04', 5)	# 97-101
    sprite('mk000_05', 5)	# 102-106
    sprite('mk000_06', 6)	# 107-112
    sprite('mk000_07', 6)	# 113-118
    sprite('mk000_08', 5)	# 119-123
    sprite('mk000_09', 5)	# 124-128

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('mk408_00', 1)	# 1-1
    sprite('mk408_01', 2)	# 2-3
    sprite('mk408_02', 2)	# 4-5
    sprite('mk408_03', 2)	# 6-7
    sprite('mk408_04', 2)	# 8-9
    sprite('mk408_05', 2)	# 10-11
    sprite('mk408_06', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('mk408_07', 2)	# 13-14	 **attackbox here**
    sprite('mk408_08', 4)	# 15-18
    sprite('mk408_09', 4)	# 19-22
    sprite('mk408_10', 4)	# 23-26
    sprite('mk408_11', 4)	# 27-30
    loopRest()
    sprite('mk000_00', 5)	# 31-35
    sprite('mk000_01', 5)	# 36-40
    sprite('mk000_02', 6)	# 41-46
    sprite('mk000_03', 6)	# 47-52
    sprite('mk000_04', 5)	# 53-57
    sprite('mk000_05', 5)	# 58-62
    sprite('mk000_06', 6)	# 63-68
    sprite('mk000_07', 6)	# 69-74
    sprite('mk000_08', 5)	# 75-79
    sprite('mk000_09', 5)	# 80-84

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('mk403_06', 3)	# 1-3
    sprite('mk403_07', 3)	# 4-6
    sprite('mk403_08', 3)	# 7-9
    sprite('mk403_09', 3)	# 10-12
    sprite('mk403_10', 3)	# 13-15
    Unknown8006(100, 1, 1)
    Unknown8007(100, 1, 1)
    GFX_1('mkef_403speedline', 1)
    sprite('mk403_11', 4)	# 16-19	 **attackbox here**
    StartMultihit()
    SFX_3('mkse_03')
    GFX_0('BlockingSpeedLine', -1)
    GFX_1('mkef_403smoke', -1)
    sprite('mk403_12ex01', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('mk403_13', 4)	# 24-27
    sprite('mk403_14', 4)	# 28-31
    sprite('mk403_15', 4)	# 32-35
    sprite('mk403_16', 4)	# 36-39
    sprite('mk403_17', 4)	# 40-43
    sprite('mk403_18', 4)	# 44-47
    sprite('mk403_19', 4)	# 48-51
    sprite('mk003_00', 3)	# 52-54
    sprite('mk003_01', 3)	# 55-57
    sprite('mk003_02', 3)	# 58-60

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
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('mk032_10', 3)	# 1-3
    sprite('mk032_00', 4)	# 4-7
    sprite('mk032_01', 4)	# 8-11
    label(0)
    sprite('mk032_02', 4)	# 12-15
    sprite('mk032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 20-23
    sprite('mk032_05', 4)	# 24-27
    sprite('mk032_06', 4)	# 28-31
    sprite('mk032_07', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 36-38
    sprite('mk032_01', 2)	# 39-40
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mk310_00', 1)	# 41-41
    Unknown1084(1)
    clearUponHandler(3)
    sprite('mk310_01', 2)	# 42-43
    SFX_0('010_swing_sword_0')
    sprite('mk310_02', 3)	# 44-46	 **attackbox here**
    sprite('mk310_03', 4)	# 47-50
    SFX_4('bmk154')
    sprite('mk310_04', 4)	# 51-54
    sprite('mk310_05', 11)	# 55-65
    sprite('mk310_06', 4)	# 66-69

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(7000)
        AirPushbackY(35500)
        AirUntechableTime(42)
        Hitstop(3)
        Unknown9015(1)
        Unknown2004(1, 0)
        JumpCancel_(1)
        Unknown13024(0)
    sprite('mk310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('mk311_00', 3)	# 4-6
    SFX_1('bmk153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk311_01', 3)	# 7-9
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk311_02', 3)	# 10-12	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    GFX_1('mkef_hit_tail', 1)
    sprite('mk311_03', 3)	# 13-15	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    sprite('mk311_04', 3)	# 16-18	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    sprite('mk311_02', 3)	# 19-21	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    GFX_1('mkef_hit_tail', 2)
    sprite('mk311_03', 3)	# 22-24	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    sprite('mk311_04', 3)	# 25-27	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    sprite('mk311_02', 3)	# 28-30	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    GFX_1('mkef_hit_tail', 3)
    sprite('mk311_03', 3)	# 31-33	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    sprite('mk311_04', 3)	# 34-36	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    SFX_3('mkse_06')
    Unknown23011(1)
    GFX_1('mkef_hit_tail', 1)
    sprite('mk311_05', 3)	# 37-39
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk311_06', 3)	# 40-42
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk311_07', 3)	# 43-45
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk311_08', 3)	# 46-48
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk311_09', 4)	# 49-52	 **attackbox here**
    sprite('mk311_10', 4)	# 53-56
    sprite('mk311_11', 4)	# 57-60
    sprite('mk311_12', 4)	# 61-64
    sprite('mk311_13', 3)	# 65-67
    sprite('mk311_14', 3)	# 68-70
    sprite('mk311_15', 3)	# 71-73
    SFX_FOOTSTEP_(100, 1, 1)

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
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('mk032_10', 3)	# 1-3
    sprite('mk032_00', 4)	# 4-7
    sprite('mk032_01', 4)	# 8-11
    label(0)
    sprite('mk032_02', 4)	# 12-15
    sprite('mk032_03', 4)	# 16-19
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 20-23
    sprite('mk032_05', 4)	# 24-27
    sprite('mk032_06', 4)	# 28-31
    sprite('mk032_07', 4)	# 32-35
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 36-38
    sprite('mk032_01', 2)	# 39-40
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mk310_00', 1)	# 41-41
    Unknown1084(1)
    clearUponHandler(3)
    sprite('mk310_01', 2)	# 42-43
    SFX_0('010_swing_sword_0')
    sprite('mk310_02', 3)	# 44-46	 **attackbox here**
    sprite('mk310_03', 4)	# 47-50
    SFX_4('bmk154')
    sprite('mk310_04', 4)	# 51-54
    sprite('mk310_05', 11)	# 55-65
    sprite('mk310_06', 4)	# 66-69

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown11050('020000006d6b65665f6869745f7461696c73705f6e616765000000000000000000000000')
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackY(-32000)
        AirPushbackX(-2200)
        AirUntechableTime(60)
        YImpluseBeforeWallbounce(1600)
        Unknown9310(24)
        Unknown2004(1, 0)
        Unknown13021(1)
        Unknown11001(0, 15, 0)
        JumpCancel_(0)
        Unknown13024(0)
    sprite('mk310_02', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('mk313_00', 3)	# 4-6	 **attackbox here**
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000002000000')
    StartMultihit()
    sprite('mk313_01', 3)	# 7-9
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000002000000')
    sprite('mk313_02', 3)	# 10-12
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000002000000')
    sprite('mk313_03', 3)	# 13-15
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000002000000')
    sprite('mk313_04', 3)	# 16-18
    physicsXImpulse(8000)
    physicsYImpulse(20000)
    Unknown1043()
    Unknown5000(17, 0)
    Unknown5004()
    sprite('mk313_05', 3)	# 19-21
    Unknown5000(16, 0)
    Unknown5004()
    sprite('mk313_06', 3)	# 22-24
    Unknown5000(16, 0)
    Unknown5004()
    sprite('mk313_07', 4)	# 25-28
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000002000000')
    sprite('mk313_08', 100)	# 29-128
    Unknown5000(15, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    sendToLabelUpon(2, 45)
    loopRest()
    label(45)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('mk313_09', 3)	# 129-131	 **attackbox here**
    SFX_4('bmk153')
    SFX_3('mkse_06')
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk313_10', 6)	# 132-137
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mk313_11', 6)	# 138-143
    sprite('mk313_12', 5)	# 144-148
    teleportRelativeX(12000)
    physicsXImpulse(12000)
    JumpCancel_(1)
    sprite('mk313_12', 4)	# 149-152
    sprite('mk313_13', 4)	# 153-156
    Unknown1019(80)
    sprite('mk313_14', 4)	# 157-160
    Unknown1019(60)
    sprite('mk313_15', 4)	# 161-164
    Unknown1019(40)
    sprite('mk313_16', 4)	# 165-168
    sprite('mk000_00', 1)	# 169-169
    Unknown2006()

@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        Unknown17011('AirThrowExe', 1, 1, 0)
    sprite('mk320_00', 3)	# 1-3
    sprite('mk320_01', 3)	# 4-6
    SFX_0('010_swing_sword_0')
    sprite('mk320_02', 3)	# 7-9	 **attackbox here**
    Unknown22004(4, 1)
    sprite('mk320_03', 3)	# 10-12
    sprite('mk320_04', 4)	# 13-16
    sprite('mk320_05', 8)	# 17-24
    SFX_4('mk155')
    sprite('mk320_06', 4)	# 25-28
    sprite('mk320_07', 4)	# 29-32

@State
def AirThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 1, 0)
        Unknown2018(0, 80)
        AttackLevel_(4)
        Damage(700)
        AttackP1(100)
        AttackP2(50)
        Hitstop(0)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(-40000)
        Unknown12051(2)
        Unknown9310(30)
        AirUntechableTime(60)
        Unknown22004(0, 0)
        Unknown28(12, 'AirThrow2')
    sprite('mk320_02', 5)	# 1-5	 **attackbox here**
    Unknown5000(9, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    StartMultihit()
    sprite('mk321_00', 3)	# 6-8
    Unknown5000(9, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('mk321_01', 3)	# 9-11
    Unknown5000(9, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('mk321_02', 3)	# 12-14
    Unknown5000(9, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('mk321_03', 3)	# 15-17
    Unknown5000(9, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('mk321_04', 3)	# 18-20	 **attackbox here**

@State
def AirThrow2():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(100)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(5000)
        AirPushbackY(-40000)
        Hitstop(16)
        Unknown9310(36)
        AirUntechableTime(60)
        Unknown11091(100)
        Unknown11044(1)
        JumpCancel_(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 47)
    sprite('mk321_05', 6)	# 1-6
    setInvincible(1)
    sprite('mk321_05', 1)	# 7-7
    physicsXImpulse(-9000)
    physicsYImpulse(12000)
    sprite('mk321_06', 3)	# 8-10
    setGravity(1200)
    sprite('mk321_06', 1)	# 11-11
    physicsYImpulse(4000)
    sprite('mk321_07', 2)	# 12-13
    sprite('mk321_08', 2)	# 14-15
    setGravity(0)
    sprite('mk321_09', 2)	# 16-17
    sprite('mk321_10', 2)	# 18-19
    physicsXImpulse(-1000)
    SFX_4('mk154')
    sprite('mk321_11', 3)	# 20-22
    sprite('mk321_12', 3)	# 23-25
    physicsXImpulse(0)
    sprite('mk321_13', 1)	# 26-26	 **attackbox here**
    teleportRelativeX(98000)
    Unknown1007(40000)
    SFX_3('mkse_13')
    label(46)
    sprite('mk321_13', 2)	# 27-28	 **attackbox here**
    physicsXImpulse(6000)
    physicsYImpulse(-34000)
    Unknown9310(24)
    sprite('mk321_14', 2)	# 29-30	 **attackbox here**
    gotoLabel(46)
    label(47)
    sprite('mk321_13', 2)	# 31-32	 **attackbox here**
    Hitstop(16)
    ScreenShake(0, 35000)
    Unknown1084(1)
    sprite('mk321_15', 3)	# 33-35
    sprite('mk321_16', 4)	# 36-39
    sprite('mk321_17', 5)	# 40-44
    sprite('mk321_18', 4)	# 45-48
    sprite('mk321_19', 2)	# 49-50
    sprite('mk321_20', 2)	# 51-52
    sprite('mk321_21', 2)	# 53-54

@State
def AutoBlocking():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(0)
        Damage(0)
        AttackP2(80)
        AirHitstunAnimation(16)
        GroundedHitstunAnimation(7)
        Unknown11030(25)
        Unknown11001(10, 0, 10)
        PushbackX(8000)
        AirPushbackY(8000)
        Unknown11066(1)
        Unknown11084(1)
        Unknown11085(1)
        Unknown12051(2)
        Unknown12055(1)
        Unknown2018(0, 60)
        Unknown13024(0)

        def upon_12():
            Unknown2058(500)
            Unknown7009(1)
            SFX_3('mkse_22')
            Unknown2037(1)

        def upon_42():
            WhiffCancel('Blocking3rd')
        setInvincible(1)
        GuardPoint_(1)
        Unknown22030(0)
        Unknown22019('0000000001000000000000000000000000000000')
        HitCancel('Blocking3rd')
    sprite('mk403_00', 2)	# 1-2
    SFX_0('003_swing_grap_0_2')
    sprite('mk403_01', 2)	# 3-4
    sprite('mk403_03', 2)	# 5-6
    sprite('mk403_04', 2)	# 7-8	 **attackbox here**
    StartMultihit()
    sprite('mk403_05', 5)	# 9-13	 **attackbox here**
    sprite('mk403_05', 13)	# 14-26	 **attackbox here**
    if (not SLOT_2):
        setInvincible(0)
    WhiffCancelEnable(1)
    Unknown23027()
    sprite('mk403_03', 6)	# 27-32
    WhiffCancelEnable(0)
    sprite('mk403_02', 6)	# 33-38

@State
def Blocking3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AirHitstunAnimation(10)
        PushbackX(-5000)
        AirPushbackY(42000)
        AirPushbackX(-1000)
        Hitstop(0)
        Unknown11056(0)
        Unknown23158('0a00000010000000')
        GFX_0('DriveRing', 100)
        Unknown23155('01000000426c6f636b696e67706f7300000000000000000000000000000000000000000000000000')
        callSubroutine('MakotoDriveSetting')
    sprite('mk403_06', 4)	# 1-4
    Unknown7014('mkse_00')
    setInvincible(1)
    Unknown22019('0100000001000000000000000000000000000000')
    sprite('mk403_07', 4)	# 5-8
    sprite('mk403_08', 4)	# 9-12
    sprite('mk403_09', 6)	# 13-18
    SLOT_55 = 1
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    sprite('mk403_08', 6)	# 19-24
    sprite('mk403_09', 6)	# 25-30
    sprite('mk403_08', 5)	# 31-35
    sprite('mk403_08', 1)	# 36-36
    SLOT_55 = 0
    if (SLOT_56 == 4):
        sendToLabel(4)
    label(1)
    AttackLevel_(3)
    Damage(1000)
    AirUntechableTime(30)
    Unknown9154(30)
    sprite('mk403_10', 2)	# 37-38
    Unknown7015()
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    GFX_0('BlockingPunchLv1', 2)
    sprite('mk403_10', 2)	# 39-40
    Unknown8006(100, 1, 1)
    Unknown8007(100, 1, 1)
    GFX_1('mkef_403speedline', 1)
    Unknown1015(130000)
    Unknown2017(0)
    Unknown2015(40)
    loopRest()
    gotoLabel(100)
    label(2)
    AttackLevel_(4)
    Damage(1200)
    AirUntechableTime(45)
    Unknown9154(33)
    sprite('mk403_10', 2)	# 41-42
    Unknown7015()
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    GFX_0('BlockingPunchLv2', 2)
    sprite('mk403_10', 2)	# 43-44
    Unknown8006(100, 1, 1)
    Unknown8007(100, 1, 1)
    callSubroutine('AfterImage_Lv2')
    Unknown1015(130000)
    Unknown2017(0)
    Unknown2015(40)
    loopRest()
    gotoLabel(100)
    label(3)
    AttackLevel_(5)
    Damage(1400)
    AirUntechableTime(60)
    Unknown9154(36)
    FatalCounter(1)
    sprite('mk403_10', 2)	# 45-46
    Unknown7015()
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    GFX_0('BlockingPunchLv3', 2)
    sprite('mk403_10', 2)	# 47-48
    GFX_1('mkef_403speedline', 1)
    callSubroutine('AfterImage_Lv3')
    Unknown1015(130000)
    Unknown2017(0)
    Unknown2015(40)
    loopRest()
    gotoLabel(100)
    label(4)
    AttackLevel_(5)
    Damage(1600)
    AirUntechableTime(60)
    Unknown9154(36)
    FatalCounter(1)
    sprite('mk403_10', 2)	# 49-50
    Unknown7015()
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    GFX_0('BlockingPunchLv3_G', 2)
    sprite('mk403_10', 2)	# 51-52
    GFX_1('mkef_403speedline', 1)
    callSubroutine('AfterImage_LvG')
    Unknown1015(130000)
    Unknown2017(0)
    Unknown2015(40)
    loopRest()
    gotoLabel(100)
    label(100)
    sendToLabelUpon(11, 101)
    sprite('mk403_11', 4)	# 53-56	 **attackbox here**
    SFX_3('mkse_03')
    GFX_0('BlockingSpeedLine', -1)
    GFX_1('mkef_403smoke', -1)
    SFX_1('mk204')
    Unknown1019(70)
    sprite('mk403_11', 4)	# 57-60	 **attackbox here**
    GFX_0('BlockingWind', 0)
    label(101)
    sprite('mk403_12', 1)	# 61-61
    Unknown1019(70)
    setInvincible(0)
    Recovery()
    sprite('mk403_12', 1)	# 62-62
    Unknown1019(70)
    sprite('mk403_12', 1)	# 63-63
    Unknown1019(70)
    sprite('mk403_12', 1)	# 64-64
    Unknown1019(70)
    sprite('mk403_12', 20)	# 65-84
    Unknown1019(0)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('mk403_13', 3)	# 85-87
    sprite('mk403_14', 3)	# 88-90
    sprite('mk403_16', 3)	# 91-93
    sprite('mk403_17', 3)	# 94-96
    sprite('mk403_18', 3)	# 97-99
    sprite('mk403_19', 3)	# 100-102
    sprite('mk403_19', 3)	# 103-105
    Unknown2005()
    enterState('CmnActStand')

@State
def BunshinStepA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown3029(1)
        Unknown3069(0)
    sprite('mk404_00', 3)	# 1-3
    sprite('mk404_00', 1)	# 4-4
    SFX_3('mkse_21')
    Unknown7007('626d6b3230355f30000000000000000064000000626d6b3230355f31000000000000000064000000626d6b3230355f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('FakeBunshinStepB', 100)
    GFX_0('FakeBunshinStepC', 100)
    physicsXImpulse(10000)
    sprite('mk404_01', 1)	# 5-5
    sprite('mk404_02', 2)	# 6-7
    Unknown14070('Pile Bunker')
    Unknown14070('DashStraight')
    Unknown14070('DashStraight_EX')
    Unknown14070('UpperRush1_A')
    Unknown14072('UpperRush1_A')
    sprite('mk404_03', 2)	# 8-9
    Unknown1019(200)
    Unknown14072('Pile Bunker')
    Unknown14072('DashStraight')
    Unknown14072('DashStraight_EX')
    sprite('mk404_03', 2)	# 10-11
    sprite('mk404_04', 4)	# 12-15
    Unknown1019(150)
    sprite('mk404_05', 4)	# 16-19
    sprite('mk404_06', 4)	# 20-23
    sprite('mk404_07', 4)	# 24-27
    sprite('mk404_08', 4)	# 28-31
    sprite('mk404_09', 4)	# 32-35
    loopRest()
    enterState('DashStop')

@State
def BunshinStepB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        WhiffCancel('NmlAtkAIR5A')
        WhiffCancel('NmlAtkAIR5B')
        WhiffCancel('NmlAtkAIR5C')
        Unknown14070('PowerDunk3')
        Unknown3029(1)
        Unknown3069(0)
        Unknown22004(5, 1)
        sendToLabelUpon(2, 11)

        def upon_STATE_END():
            Unknown1019(70)
    sprite('mk023_00', 3)	# 1-3
    sprite('mk023_00', 1)	# 4-4
    SFX_3('mkse_21')
    Unknown7007('626d6b3230355f30000000000000000064000000626d6b3230355f31000000000000000064000000626d6b3230355f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('FakeBunshinStepA', 100)
    GFX_0('FakeBunshinStepC', 100)
    sprite('mk023_01', 2)	# 5-6
    sprite('mk411_00', 4)	# 7-10
    physicsXImpulse(24000)
    physicsYImpulse(30000)
    setGravity(2000)
    Unknown22003(-1)
    Unknown22001(-1)
    sprite('mk411_01', 4)	# 11-14
    sprite('mk411_02', 3)	# 15-17
    WhiffCancelEnable(1)
    Unknown14072('PowerDunk3')
    sprite('mk411_03', 3)	# 18-20
    sprite('mk411_04', 3)	# 21-23
    sprite('mk411_05', 3)	# 24-26
    sprite('mk411_12', 2)	# 27-28
    sprite('mk411_13', 2)	# 29-30
    sprite('mk411_14', 3)	# 31-33
    label(10)
    sprite('mk411_15', 2)	# 34-35
    sprite('mk411_16', 2)	# 36-37
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('mk411_06', 1)	# 38-38
    Unknown3029(0)
    sprite('mk411_07', 1)	# 39-39
    sprite('mk411_08', 1)	# 40-40
    sprite('mk411_09', 1)	# 41-41
    sprite('mk411_10', 1)	# 42-42
    sprite('mk411_11', 1)	# 43-43

@State
def BunshinStepC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        WhiffCancel('NmlAtkAIR5A')
        WhiffCancel('NmlAtkAIR5B')
        WhiffCancel('NmlAtkAIR5C')
        Unknown14070('PowerDunk3')
        Unknown3029(1)
        Unknown3069(0)
        Unknown22004(5, 1)
        sendToLabelUpon(2, 11)
    sprite('mk023_00', 3)	# 1-3
    sprite('mk023_00', 1)	# 4-4
    SFX_3('mkse_21')
    Unknown7007('626d6b3230355f30000000000000000064000000626d6b3230355f31000000000000000064000000626d6b3230355f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('FakeBunshinStepA', 100)
    GFX_0('FakeBunshinStepB', 100)
    sprite('mk023_01', 2)	# 5-6
    sprite('mk411_00', 4)	# 7-10
    physicsXImpulse(9000)
    physicsYImpulse(42000)
    setGravity(2200)
    Unknown22003(-1)
    Unknown22001(-1)
    sprite('mk411_01', 4)	# 11-14
    sprite('mk411_02', 3)	# 15-17
    WhiffCancelEnable(1)
    Unknown14072('PowerDunk3')
    sprite('mk411_03', 3)	# 18-20
    sprite('mk411_04', 3)	# 21-23
    sprite('mk411_05', 3)	# 24-26
    sprite('mk411_12', 2)	# 27-28
    Unknown1019(80)
    sprite('mk411_13', 2)	# 29-30
    sprite('mk411_14', 3)	# 31-33
    label(10)
    sprite('mk411_15', 2)	# 34-35
    sprite('mk411_16', 2)	# 36-37
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('mk411_06', 1)	# 38-38
    Unknown3029(0)
    sprite('mk411_07', 1)	# 39-39
    sprite('mk411_08', 1)	# 40-40
    sprite('mk411_09', 1)	# 41-41
    sprite('mk411_10', 1)	# 42-42
    sprite('mk411_11', 1)	# 43-43

@State
def DashStop():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown3029(1)
        Unknown3069(0)
    sprite('mk404_10', 2)	# 1-2
    Unknown8002()
    physicsXImpulse(20000)
    sprite('mk404_11', 5)	# 3-7
    SFX_0('205_runjump_garden_0')
    Unknown1019(80)
    sprite('mk404_12', 3)	# 8-10
    Unknown1019(50)
    sprite('mk404_13', 1)	# 11-11
    Unknown7007('626d6b3230365f30000000000000000064000000626d6b3230365f31000000000000000064000000626d6b3230365f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown3029(0)

@State
def Urmawari():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('mk405_00', 2)	# 1-2
    Unknown2017(0)
    SFX_0('001_airbackdash_0')
    Unknown8006(100, 1, 0)
    GFX_1('mkef_405speedline', 0)
    Unknown3029(1)
    physicsXImpulse(25000)
    SFX_1('mk207')
    sprite('mk405_01', 3)	# 3-5
    sprite('mk405_02', 3)	# 6-8
    sprite('mk405_03', 3)	# 9-11
    sprite('mk405_04', 3)	# 12-14
    Unknown8006(100, 1, 0)
    Unknown1019(80)
    sprite('mk405_05', 3)	# 15-17
    Unknown8006(100, 1, 0)
    Unknown1019(30)
    sprite('mk405_06', 3)	# 18-20
    Unknown2017(1)
    Unknown1019(10)
    sprite('mk000_00', 1)	# 21-21
    Unknown3029(0)
    Unknown2006()

@State
def DashUpper():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(550)
        PushbackX(12000)
        AirUntechableTime(26)
        HitAirUnblockable(3)
        HitOrBlockCancel('UpperChudan')
        HitOrBlockCancel('UpperGedan')
        HitOrBlockCancel('UpperRush1')
        HitOrBlockCancel('UpperBodyBlow')
        HitOrBlockCancel('Pile Bunker')
        Unknown3029(1)
        Unknown3069(0)
    sprite('mk406_00', 1)	# 1-1
    physicsXImpulse(26000)
    sprite('mk406_01', 2)	# 2-3
    sprite('mk406_02', 2)	# 4-5
    sprite('mk406_03', 2)	# 6-7
    sprite('mk406_04', 2)	# 8-9
    SFX_1('mk208')
    Unknown1019(50)
    sprite('mk406_05', 2)	# 10-11
    Unknown1019(50)
    SFX_0('004_swing_grap_1_1')
    sprite('mk406_06', 4)	# 12-15	 **attackbox here**
    Unknown1019(0)
    sprite('mk406_07', 4)	# 16-19
    Recovery()
    sprite('mk406_08', 3)	# 20-22
    sprite('mk406_09', 3)	# 23-25
    sprite('mk406_10', 3)	# 26-28
    Unknown14077(0)
    sprite('mk406_11', 3)	# 29-31
    sprite('mk406_12', 3)	# 32-34
    Unknown3029(0)

@State
def DashStraight():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackP1(70)
        Hitstop(9)
        AirPushbackX(48000)
        PushbackX(19800)
        Unknown3029(1)
        Unknown3069(0)
        Unknown23158('0a0000000e000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1044, 0)
        callSubroutine('MakotoDriveSetting')
        Unknown30068(1)
        loopRelated(17, 8)

        def upon_17():
            setInvincible(1)
            Unknown22019('0000000000000000010000000000000000000000')
    sprite('mk404_04', 2)	# 1-2
    Unknown7014('mkse_00')
    physicsXImpulse(10000)
    sprite('mk413_00', 2)	# 3-4
    physicsXImpulse(8000)
    sprite('mk413_01', 2)	# 5-6
    SLOT_55 = 1
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 7-9
    sprite('mk413_01', 3)	# 10-12
    physicsXImpulse(6000)
    sprite('mk413_02', 3)	# 13-15
    sprite('mk413_01', 3)	# 16-18
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 19-21
    setInvincible(0)
    sprite('mk413_01', 3)	# 22-24
    sprite('mk413_02', 3)	# 25-27
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    AirPushbackY(12000)
    AirUntechableTime(30)
    Unknown9154(25)
    sprite('keep', 2)	# 28-29
    Unknown7007('626d6b3231355f30000000000000000064000000626d6b3231355f31000000000000000064000000626d6b3231355f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv2')
    sprite('mk413_04', 3)	# 30-32
    Unknown7015()
    SFX_0('004_swing_grap_1_1')
    SFX_0('004_swing_grap_1_1')
    Unknown2015(150)
    physicsXImpulse(80000)
    Unknown8007(100, 1, 1)
    sprite('mk413_05', 6)	# 33-38	 **attackbox here**
    Unknown1019(60)
    GFX_0('mkef413_lv2', -1)
    GFX_1('mkef_Lv2Puncheairwall', 0)
    loopRest()
    gotoLabel(99)
    label(2)
    AttackLevel_(5)
    AirPushbackY(17000)
    AirUntechableTime(40)
    Unknown9154(27)
    Unknown23159('DashStraightTame')
    sprite('keep', 1)	# 39-39
    SFX_4('mk215')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv3')
    sprite('mk413_04', 3)	# 40-42
    Unknown7015()
    SFX_3('mkse_03')
    Unknown2015(150)
    physicsXImpulse(100000)
    Unknown8007(100, 1, 1)
    sprite('mk413_05', 6)	# 43-48	 **attackbox here**
    Unknown1019(60)
    ScreenShake(0, 35000)
    GFX_0('mkef413_lv3', -1)
    GFX_1('mkef_Lv3Puncheairwall', 0)
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk413_06', 4)	# 49-52
    setInvincible(0)
    Unknown1019(30)
    Unknown2015(-1)
    Unknown8010(100, 1, 1)
    Recovery()
    sprite('mk413_07', 5)	# 53-57
    Unknown8010(100, 1, 1)
    sprite('mk404_12', 5)	# 58-62
    Unknown1019(0)
    sprite('mk404_13', 5)	# 63-67

@State
def DashStraight_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(70)
        Damage(2200)
        AirPushbackY(17000)
        PushbackX(29900)
        Unknown9154(27)
        AirUntechableTime(60)
        Hitstop(9)
        AirPushbackX(48000)
        Unknown30065(0)
        Unknown11091(10)
        Unknown3029(1)
        Unknown3069(0)
        Unknown23158('0a0000000e000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1044, 0)
        callSubroutine('MakotoDriveSetting')
        Unknown30068(1)
        loopRelated(17, 8)

        def upon_17():
            setInvincible(1)
            Unknown22019('0000000000000000010000000000000000000000')
    sprite('mk404_04', 2)	# 1-2
    Unknown23008(0, 0)
    Unknown7014('mkse_00')
    physicsXImpulse(10000)
    sprite('mk413_00', 2)	# 3-4
    physicsXImpulse(8000)
    sprite('mk413_01', 2)	# 5-6
    Unknown23125('')
    Unknown2058(-5000)
    SLOT_55 = 1
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 7-9
    sprite('mk413_01', 3)	# 10-12
    physicsXImpulse(6000)
    sprite('mk413_02', 3)	# 13-15
    sprite('mk413_01', 3)	# 16-18
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 19-21
    setInvincible(0)
    sprite('mk413_01', 3)	# 22-24
    sprite('mk413_02', 3)	# 25-27
    SLOT_55 = 0
    loopRest()
    label(1)
    label(2)
    sprite('keep', 1)	# 28-28
    Unknown7007('626d6b3231355f30000000000000000064000000626d6b3231355f31000000000000000064000000626d6b3231355f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_LvG')
    sprite('mk413_04', 3)	# 29-31
    Unknown7015()
    SFX_3('mkse_03')
    Unknown2015(150)
    physicsXImpulse(90000)
    Unknown8007(100, 1, 1)
    sprite('mk413_05', 6)	# 32-37	 **attackbox here**
    Unknown1019(40)
    ScreenShake(0, 35000)
    GFX_0('mkef413_lvG', -1)
    GFX_1('mkef_PuncheairwallLvG', 0)
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk413_06', 4)	# 38-41
    setInvincible(0)
    Unknown1019(30)
    Unknown2015(-1)
    Unknown8010(100, 1, 1)
    Recovery()
    sprite('mk413_07', 3)	# 42-44
    Unknown8010(100, 1, 1)
    sprite('mk404_12', 2)	# 45-46
    sprite('mk404_13', 3)	# 47-49

@State
def Pile__sp__Bunker():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1700)
        AttackP1(80)
        AirUntechableTime(40)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(50000)
        AirPushbackY(20000)
        PushbackX(50000)
        Unknown3029(1)
        Unknown3069(0)
        Unknown3070(2)
        Unknown3071(8)
    sprite('mk406_10', 2)	# 1-2
    Unknown1084(1)
    sprite('mk407_00', 3)	# 3-5
    physicsXImpulse(-30000)
    sprite('mk407_01', 2)	# 6-7
    Unknown1019(60)
    sprite('mk407_01', 1)	# 8-8
    setInvincible(1)
    sprite('mk407_02', 3)	# 9-11
    Unknown8006(100, 1, 1)
    Unknown1019(60)
    sprite('mk407_03', 4)	# 12-15
    Unknown8006(100, 1, 1)
    Unknown1084(1)
    sprite('mk407_04', 2)	# 16-17
    Unknown7007('626d6b3230395f30000000000000000064000000626d6b3230395f31000000000000000064000000626d6b3230395f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('mkse_03')
    Unknown8007(100, 1, 1)
    ScreenShake(0, 15000)
    physicsXImpulse(130000)
    setInvincible(0)
    sprite('mk407_05', 2)	# 18-19
    GFX_1('mkef_Lv3Puncheairwall', 0)
    sprite('mk407_06', 3)	# 20-22	 **attackbox here**
    GFX_0('DriveLv3PunchefD', 1)
    Unknown8003(100, 1, 1)
    Unknown1019(15)
    sprite('mk407_07', 4)	# 23-26
    Unknown1019(0)
    sprite('mk407_08', 4)	# 27-30
    sprite('mk407_09', 4)	# 31-34
    sprite('mk407_10', 5)	# 35-39
    sprite('mk407_11', 5)	# 40-44
    Unknown3029(0)
    sprite('mk407_12', 3)	# 45-47

@State
def UpperChudan():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(3)
        Damage(1000)
        AirUntechableTime(40)
        AirHitstunAnimation(11)
        AirPushbackY(-42000)
        YImpluseBeforeWallbounce(0)
        HitOverhead(2)
        Unknown3029(1)
        Unknown3069(0)
    sprite('mk404_12', 1)	# 1-1
    sprite('mk408_00', 1)	# 2-2
    sprite('mk408_01', 1)	# 3-3
    physicsXImpulse(3000)
    sprite('mk408_02', 1)	# 4-4
    Unknown1019(200)
    sprite('mk408_03', 2)	# 5-6
    Unknown1019(200)
    sprite('mk408_04', 2)	# 7-8
    Unknown1019(200)
    sprite('mk408_05', 2)	# 9-10
    Unknown1019(200)
    SFX_0('004_swing_grap_1_2')
    sprite('mk408_06', 1)	# 11-11	 **attackbox here**
    Unknown1019(40)
    sprite('mk408_07', 2)	# 12-13	 **attackbox here**
    Unknown1019(40)
    sprite('mk408_08', 4)	# 14-17
    physicsXImpulse(0)
    Recovery()
    sprite('mk408_09', 4)	# 18-21
    sprite('mk408_10', 4)	# 22-25
    sprite('mk408_11', 4)	# 26-29
    Unknown3029(0)

@State
def UpperGedan():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(3)
        Damage(1000)
        AirUntechableTime(30)
        HitLow(2)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(18000)
        AirUntechableTime(40)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown3029(1)
        Unknown3069(0)
    sprite('mk409_02', 3)	# 1-3
    physicsXImpulse(18000)
    sprite('mk409_03', 4)	# 4-7
    sprite('mk409_04', 3)	# 8-10
    Unknown1019(30)
    SFX_0('004_swing_grap_1_1')
    sprite('mk409_05', 2)	# 11-12	 **attackbox here**
    physicsXImpulse(0)
    sprite('mk409_06', 2)	# 13-14	 **attackbox here**
    sprite('mk409_08', 2)	# 15-16
    Recovery()
    sprite('mk409_09', 2)	# 17-18
    sprite('mk409_10', 2)	# 19-20
    sprite('mk409_11', 2)	# 21-22
    sprite('mk409_12', 3)	# 23-25
    sprite('mk409_13', 3)	# 26-28
    Unknown3029(0)

@State
def UpperRush1_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(500)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(22)
        PushbackX(10000)
        AirPushbackY(10000)
        Unknown3029(1)
        Unknown3069(0)
        Unknown30068(1)
    sprite('keep', 2)	# 1-2
    physicsXImpulse(15000)
    sprite('mk410_00', 2)	# 3-4
    sprite('mk410_01', 2)	# 5-6
    sprite('mk410_02', 2)	# 7-8
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_03', 3)	# 9-11	 **attackbox here**
    Unknown1019(50)

    def upon_45():
        if CheckInput(INPUT_PRESS_A):
            Unknown2037(1)
        if CheckInput(INPUT_PRESS_B):
            Unknown2037(0)
        if CheckInput(INPUT_PRESS_C):
            Unknown2037(0)
    RefreshMultihit()
    Unknown14070('Pile Bunker')
    Unknown14070('UpperBodyBlow')
    Unknown14070('UpperBodyBlow_EX')
    sprite('mk410_04', 2)	# 12-13
    Unknown1019(200)
    sprite('mk410_05', 2)	# 14-15
    sprite('mk410_06', 2)	# 16-17
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_07', 3)	# 18-20	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    loopRest()
    Unknown19(10, 2, 2)
    label(0)
    Hitstop(3)
    AirPushbackY(5000)
    Unknown23159('UpperRush1_Add')
    clearUponHandler(45)
    sprite('mk410_08', 1)	# 21-21
    Unknown1019(200)
    sprite('mk410_01', 1)	# 22-22
    sprite('mk410_02', 1)	# 23-23
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_03', 2)	# 24-25	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    sprite('mk410_04', 1)	# 26-26
    Unknown1019(200)
    sprite('mk410_05', 1)	# 27-27
    sprite('mk410_06', 1)	# 28-28
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_07', 2)	# 29-30	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    sprite('mk410_08', 1)	# 31-31
    Unknown1019(200)
    sprite('mk410_01', 1)	# 32-32
    sprite('mk410_02', 1)	# 33-33
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_03', 2)	# 34-35	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    sprite('mk410_04', 1)	# 36-36
    Unknown1019(200)
    sprite('mk410_05', 1)	# 37-37
    sprite('mk410_06', 1)	# 38-38
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_07', 2)	# 39-40	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    label(10)
    clearUponHandler(45)
    sprite('mk410_08', 2)	# 41-42
    physicsXImpulse(8000)
    if (not SLOT_2):
        Unknown14072('Pile Bunker')
        Unknown14072('UpperBodyBlow')
        Unknown14072('UpperBodyBlow_EX')
    sprite('mk410_09', 2)	# 43-44
    Unknown14073('Pile Bunker')
    Unknown14073('UpperBodyBlow')
    Unknown14073('UpperBodyBlow_EX')
    sprite('mk410_10', 2)	# 45-46
    sprite('mk410_11', 2)	# 47-48
    Unknown7007('626d6b3231325f30000000000000000064000000626d6b3231325f31000000000000000064000000626d6b3231325f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    sprite('mk410_12', 4)	# 49-52	 **attackbox here**
    Unknown1019(0)
    Damage(1500)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirUntechableTime(50)
    Hitstop(11)
    AirPushbackX(8000)
    AirPushbackY(39000)
    RefreshMultihit()
    sprite('mk410_13', 12)	# 53-64
    Recovery()
    Unknown3029(0)
    sprite('mk410_14', 4)	# 65-68
    sprite('mk410_15', 4)	# 69-72
    sprite('mk410_16', 4)	# 73-76
    sprite('mk410_17', 4)	# 77-80
    sprite('mk410_18', 4)	# 81-84
    sprite('mk410_19', 4)	# 85-88

@State
def UpperRush1_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    enterState('UpperRush1_A')

@State
def UpperBodyBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AirHitstunAnimation(10)
        PushbackX(12000)
        Hitstop(8)
        Unknown3029(1)
        Unknown3069(0)
        Unknown30068(1)
        Unknown23158('090000000e000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1050, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk412_01', 1)	# 1-1
    Unknown7014('mkse_00')
    sprite('mk412_02', 1)	# 2-2
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk412_03', 2)	# 3-4
    SLOT_55 = 1
    sprite('mk412_02', 2)	# 5-6
    sprite('mk412_03', 3)	# 7-9
    sprite('mk412_02', 3)	# 10-12
    GFX_0('DriveChargelightning', 0)
    sprite('mk412_03', 3)	# 13-15
    sprite('mk412_02', 3)	# 16-18
    sprite('mk412_03', 3)	# 19-21
    sprite('mk412_02', 3)	# 22-24
    GFX_0('DriveChargelightning', 0)
    sprite('mk412_03', 3)	# 25-27
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    AttackP2(75)
    Unknown11001(0, 3, 8)
    AirUntechableTime(30)
    AirPushbackY(25000)
    sprite('mk412_04', 1)	# 28-28
    Unknown7007('626d6b3231345f30000000000000000064000000626d6b3231345f31000000000000000064000000626d6b3231345f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(10000)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv2')
    sprite('mk412_05', 1)	# 29-29
    Unknown1019(300)
    Unknown7015()
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    SFX_0('004_swing_grap_1_1')
    SFX_0('004_swing_grap_1_1')
    sprite('mk412_06', 3)	# 30-32	 **attackbox here**
    Unknown1019(10)
    GFX_0('Drive412Lv2_hit', 0)
    GFX_0('Drive412Lv2', 0)
    Unknown36(1)
    Unknown1096(600)
    Unknown35()
    sprite('mk412_07', 5)	# 33-37
    Recovery()
    Unknown1084(1)
    sprite('mk412_08', 6)	# 38-43
    sprite('mk412_09', 6)	# 44-49
    loopRest()
    gotoLabel(99)
    label(2)
    AttackLevel_(5)
    AttackP2(80)
    Unknown11001(0, 3, 11)
    AirUntechableTime(36)
    sprite('mk412_03', 3)	# 50-52
    Unknown7007('626d6b3231345f30000000000000000064000000626d6b3231345f31000000000000000064000000626d6b3231345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('mk412_04', 2)	# 53-54
    physicsXImpulse(10000)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_Lv3')
    sprite('mk412_05', 2)	# 55-56
    Unknown1019(400)
    Unknown7015()
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    SFX_3('mkse_03')
    sprite('mk412_06', 3)	# 57-59	 **attackbox here**
    Unknown1019(10)
    ScreenShake(0, 35000)
    GFX_0('Drive412Lv3_hit', 0)
    GFX_0('Drive412Lv3', 0)
    Unknown36(1)
    Unknown1096(800)
    Unknown35()
    sprite('mk412_07', 2)	# 60-61
    Recovery()
    Unknown1084(1)
    sprite('mk412_08', 4)	# 62-65
    sprite('mk412_09', 2)	# 66-67
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk412_10', 3)	# 68-70

@State
def UpperBodyBlow_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP2(80)
        AirHitstunAnimation(10)
        AirUntechableTime(36)
        Hitstop(6)
        Unknown11001(0, 3, 11)
        PushbackX(12000)
        Unknown30065(0)
        Unknown11091(10)
        Unknown3029(1)
        Unknown3069(0)
        Unknown30068(1)
        Unknown23158('060000000c000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1050, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk412_00', 2)	# 1-2
    Unknown23008(0, 0)
    sprite('mk412_01', 2)	# 3-4
    Unknown7014('mkse_00')
    sprite('mk412_02', 2)	# 5-6
    Unknown23125('')
    Unknown2058(-5000)
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk412_03', 2)	# 7-8
    SLOT_55 = 1
    sprite('mk412_02', 2)	# 9-10
    sprite('mk412_03', 3)	# 11-13
    sprite('mk412_02', 3)	# 14-16
    GFX_0('DriveChargelightning', 0)
    sprite('mk412_03', 3)	# 17-19
    sprite('mk412_02', 3)	# 20-22
    sprite('mk412_03', 3)	# 23-25
    sprite('mk412_02', 3)	# 26-28
    GFX_0('DriveChargelightning', 0)
    sprite('mk412_03', 3)	# 29-31
    SLOT_55 = 0
    loopRest()
    label(1)
    label(2)
    sprite('mk412_04', 2)	# 32-33
    Unknown7007('626d6b3231345f30000000000000000064000000626d6b3231345f31000000000000000064000000626d6b3231345f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(10000)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_LvG')
    sprite('mk412_05', 2)	# 34-35
    Unknown1019(300)
    Unknown7015()
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    SFX_3('mkse_03')
    sprite('mk412_06', 3)	# 36-38	 **attackbox here**
    Unknown1019(10)
    ScreenShake(0, 35000)
    Unknown1019(50)
    GFX_0('Drive412LvG_hit', 0)
    GFX_0('Drive412LvG', 0)
    Unknown36(1)
    Unknown1096(800)
    Unknown35()
    sprite('mk412_07', 2)	# 39-40
    Recovery()
    Unknown1084(1)
    sprite('mk412_08', 4)	# 41-44
    sprite('mk412_09', 2)	# 45-46
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk412_10', 3)	# 47-49

@State
def CreateEnergyBall():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
    sprite('mk400_00', 2)	# 1-2
    sprite('mk400_01', 2)	# 3-4
    tag_voice(1, 'bmk200_0', 'bmk200_1', 'bmk200_2', '')
    sprite('mk400_02', 3)	# 5-7
    sprite('mk400_03', 2)	# 8-9
    sprite('mk400_04', 4)	# 10-13
    sprite('mk400_05', 2)	# 14-15
    GFX_0('mkef_hibana', 0)
    SFX_3('mkse_20')
    SFX_0('014_electric_sl')
    Unknown14070('PunchShot')
    sprite('mk400_06', 3)	# 16-18
    GFX_0('EnergyBall', 103)
    sprite('mk400_07', 3)	# 19-21
    sprite('mk400_07', 3)	# 22-24
    Unknown14072('PunchShot')
    sprite('mk400_08', 4)	# 25-28
    sprite('mk400_09', 6)	# 29-34
    sprite('mk400_10', 6)	# 35-40
    Unknown14074('PunchShot')
    sprite('mk400_11', 6)	# 41-46
    sprite('mk400_12', 3)	# 47-49
    Recovery()

@State
def PunchShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AirHitstunAnimation(18)
        AirPushbackX(50000)
        AirPushbackY(15000)
        Hitstop(9)
        Unknown30068(1)
        Unknown23158('0f00000014000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1042, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk406_10', 2)	# 1-2
    Unknown7014('mkse_00')
    sprite('mk407_00', 2)	# 3-4
    sprite('mk407_01', 2)	# 5-6
    SLOT_55 = 1
    sprite('mk407_02', 4)	# 7-10
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    sprite('mk407_03', 4)	# 11-14
    sprite('mk407_02', 4)	# 15-18
    sprite('mk407_03', 4)	# 19-22
    sprite('mk407_02', 4)	# 23-26
    sprite('mk407_03', 4)	# 27-30
    sprite('mk407_02', 4)	# 31-34
    sprite('mk407_03', 4)	# 35-38
    sprite('mk407_02', 4)	# 39-42
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    Damage(700)
    sprite('mk407_04', 2)	# 43-44
    callSubroutine('AfterImage_Lv3')
    Unknown7015()
    tag_voice(0, 'bmk201_0', 'bmk201_1', 'bmk201_2', '')
    SFX_3('mkse_03')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    ScreenShake(0, 35000)
    sprite('mk407_05', 1)	# 45-45
    sprite('mk407_06', 3)	# 46-48	 **attackbox here**
    GFX_1('mkef_400Lv3airwall', 0)
    GFX_0('DriveLv3PunchefD', 0)
    Unknown38(5, 1)
    Unknown21015('456e6572677942616c6c000000000000000000000000000000000000000000001504000000000000')
    sprite('mk407_07', 3)	# 49-51
    loopRest()
    gotoLabel(99)
    label(2)
    AttackLevel_(5)
    Damage(1000)
    sprite('mk407_04', 2)	# 52-53
    callSubroutine('AfterImage_Lv3')
    Unknown7015()
    tag_voice(0, 'bmk201_0', 'bmk201_1', 'bmk201_2', '')
    SFX_3('mkse_03')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    ScreenShake(0, 35000)
    sprite('mk407_05', 1)	# 54-54
    sprite('mk407_06', 3)	# 55-57	 **attackbox here**
    GFX_1('mkef_400Lv3airwall', 0)
    GFX_0('DriveLv3PunchefD', 0)
    Unknown38(5, 1)
    Unknown21015('456e6572677942616c6c000000000000000000000000000000000000000000001604000000000000')
    sprite('mk407_07', 3)	# 58-60
    loopRest()
    gotoLabel(99)
    label(3)
    AttackLevel_(5)
    Damage(1100)
    FatalCounter(1)
    Unknown23159('PunchShot_Lv3')
    sprite('mk407_04', 2)	# 61-62
    callSubroutine('AfterImage_Lv3')
    Unknown7015()
    SFX_1('mk201')
    SFX_3('mkse_03')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    ScreenShake(0, 35000)
    sprite('mk407_05', 1)	# 63-63
    sprite('mk407_06', 3)	# 64-66	 **attackbox here**
    GFX_1('mkef_400Lv3airwall', 0)
    GFX_0('DriveLv3PunchefD', 0)
    Unknown38(5, 1)
    Unknown21015('456e6572677942616c6c000000000000000000000000000000000000000000001604000000000000')
    sprite('mk407_07', 3)	# 67-69
    loopRest()
    gotoLabel(99)
    label(4)
    AttackLevel_(5)
    Damage(1100)
    FatalCounter(1)
    Unknown23159('PunchShot_LvG')
    sprite('mk407_04', 2)	# 70-71
    Unknown7015()
    SFX_1('mk201')
    SFX_3('mkse_03')
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    callSubroutine('AfterImage_LvG')
    ScreenShake(0, 35000)
    sprite('mk407_05', 1)	# 72-72
    sprite('mk407_06', 3)	# 73-75	 **attackbox here**
    Unknown21015('456e6572677942616c6c000000000000000000000000000000000000000000001704000000000000')
    GFX_1('mkef_400LvGairwall', 0)
    GFX_0('DriveLvG_PunchefD', 0)
    sprite('mk407_07', 3)	# 76-78
    Unknown21015('456e6572677942616c6c000000000000000000000000000000000000000000001704000000000000')
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk407_08', 3)	# 79-81
    sprite('mk407_09', 3)	# 82-84
    sprite('mk407_10', 3)	# 85-87
    sprite('mk407_11', 3)	# 88-90
    Unknown3029(0)
    sprite('mk407_12', 3)	# 91-93

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1500)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(50000)
        AirPushbackX(12000)
        AirUntechableTime(50)
        setInvincible(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 41)

        def upon_78():
            Unknown2037(1)
            clearUponHandler(78)
    sprite('mk401_00', 2)	# 1-2
    sprite('mk401_01', 3)	# 3-5
    sprite('mk401_02', 3)	# 6-8
    sprite('mk401_03', 2)	# 9-10	 **attackbox here**
    sprite('mk401_04', 2)	# 11-12	 **attackbox here**
    SFX_0('006_swing_blade_2')
    tag_voice(1, 'bmk202_0', 'bmk202_1', 'bmk202_2', '')
    sprite('mk401_05', 2)	# 13-14
    GFX_0('DriveLv3PunchefSyouryu', 0)
    SFX_0('011_spin_0')
    Unknown8001(3, 100)
    physicsYImpulse(40000)
    physicsXImpulse(12000)
    teleportRelativeX(48000)
    setGravity(2100)
    sprite('mk401_06', 2)	# 15-16	 **attackbox here**
    sprite('mk401_07', 2)	# 17-18	 **attackbox here**
    setInvincible(0)
    sprite('mk401_06', 2)	# 19-20	 **attackbox here**
    sprite('mk401_07', 2)	# 21-22	 **attackbox here**
    sprite('mk401_06', 2)	# 23-24	 **attackbox here**
    sprite('mk401_07', 2)	# 25-26	 **attackbox here**
    if SLOT_2:
        HitCancel('PowerDunkAINP')
        HitCancel('PowerDunkBINP')
        HitCancel('PowerDunkCINP')
    sprite('mk401_08', 3)	# 27-29
    sprite('mk401_09', 3)	# 30-32
    sprite('mk401_10', 3)	# 33-35
    sprite('mk401_11', 3)	# 36-38
    sprite('mk401_12', 3)	# 39-41
    sprite('mk401_13', 3)	# 42-44
    Unknown14077(0)
    label(40)
    sprite('mk020_07', 4)	# 45-48
    sprite('mk020_08', 4)	# 49-52
    loopRest()
    gotoLabel(40)
    label(41)
    sprite('mk024_00', 4)	# 53-56
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('mk024_01', 4)	# 57-60
    sprite('mk024_02', 3)	# 61-63
    sprite('mk024_03', 3)	# 64-66
    sprite('mk024_04', 3)	# 67-69

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1500)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(35000)
        AirPushbackX(10000)
        AirUntechableTime(50)
        Unknown11058('0100000000000000000000000000000000000000')
        setInvincible(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 41)

        def upon_78():
            Unknown2037(1)
            clearUponHandler(78)
    sprite('mk401_03', 2)	# 1-2	 **attackbox here**
    Unknown1084(1)
    SFX_0('006_swing_blade_2')
    StartMultihit()
    sprite('mk401_04', 2)	# 3-4	 **attackbox here**
    SFX_0('011_spin_0')
    StartMultihit()
    sprite('mk401_05', 3)	# 5-7
    tag_voice(1, 'bmk202_0', 'bmk202_1', 'bmk202_2', '')
    GFX_0('DriveLv3PunchefSyouryu_Air', 0)
    physicsYImpulse(36000)
    physicsXImpulse(10000)
    setGravity(2100)
    sprite('mk401_06', 2)	# 8-9	 **attackbox here**
    sprite('mk401_07', 2)	# 10-11	 **attackbox here**
    setInvincible(0)
    sprite('mk401_06', 2)	# 12-13	 **attackbox here**
    sprite('mk401_07', 2)	# 14-15	 **attackbox here**
    if SLOT_2:
        HitCancel('PowerDunkAINP')
        HitCancel('PowerDunkBINP')
        HitCancel('PowerDunkCINP')
    sprite('mk401_08', 3)	# 16-18
    sprite('mk401_09', 3)	# 19-21
    sprite('mk401_10', 3)	# 22-24
    sprite('mk401_11', 3)	# 25-27
    sprite('mk401_12', 3)	# 28-30
    sprite('mk401_13', 3)	# 31-33
    Unknown14077(0)
    label(40)
    sprite('mk020_07', 4)	# 34-37
    sprite('mk020_08', 4)	# 38-41
    loopRest()
    gotoLabel(40)
    label(41)
    sprite('mk024_00', 4)	# 42-45
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('mk024_01', 4)	# 46-49
    sprite('mk024_02', 3)	# 50-52
    sprite('mk024_03', 3)	# 53-55
    sprite('mk024_04', 3)	# 56-58

@State
def PowerDunk():

    def upon_IMMEDIATE():
        Unknown17025('')
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        AirPushbackY(-50000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)
        Unknown11058('0100000000000000000000000000000000000000')
        AttackP1(48)
        AttackP2(100)
        Unknown22004(10, 1)
        Unknown23158('0e00000012000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1043, 0)
        callSubroutine('MakotoDriveSetting')
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('mk402_00', 2)	# 1-2
    Unknown7014('mkse_00')
    Unknown1019(120)
    setGravity(900)
    sprite('mk402_01', 2)	# 3-4
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAuraAir', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk402_02', 2)	# 5-6
    sprite('mk402_01', 2)	# 7-8
    sprite('mk402_02', 2)	# 9-10
    GFX_0('DriveChargelightning', 1)
    sprite('mk402_01', 2)	# 11-12
    sprite('mk402_02', 2)	# 13-14
    sprite('mk402_01', 2)	# 15-16
    sprite('mk402_02', 2)	# 17-18
    SLOT_55 = 1
    sprite('mk402_01', 2)	# 19-20
    sprite('mk402_02', 2)	# 21-22
    sprite('mk402_01', 2)	# 23-24
    sprite('mk402_02', 2)	# 25-26
    sprite('mk402_01', 2)	# 27-28
    sprite('mk402_02', 2)	# 29-30
    sprite('mk402_01', 2)	# 31-32
    sprite('mk402_02', 2)	# 33-34
    sprite('mk402_01', 2)	# 35-36
    sprite('mk402_02', 2)	# 37-38
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    Damage(2000)
    sprite('mk402_03', 2)	# 39-40
    Unknown7015()
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572614169720000000000000000000000000000fe03000000000000')
    tag_voice(0, 'bmk203_0', 'bmk203_1', 'bmk203_2', '')
    SFX_0('004_swing_grap_1_1')
    SFX_0('004_swing_grap_1_1')
    ScreenShake(0, 35000)
    sprite('mk402_04', 2)	# 41-42
    sprite('mk402_05', 2)	# 43-44
    sprite('mk402_06', 2)	# 45-46
    GFX_0('PowerDunkAirwallLv2', 0)
    sprite('mk402_07', 6)	# 47-52	 **attackbox here**
    GFX_0('DriveLv2PunchefPowerDunk', 0)
    Unknown1044()
    sprite('mk402_08', 2)	# 53-54
    Recovery()
    sprite('mk402_09', 2)	# 55-56
    sprite('mk402_10', 2)	# 57-58
    sprite('mk402_11', 2)	# 59-60
    loopRest()
    gotoLabel(99)
    label(2)
    AttackLevel_(5)
    Damage(2500)
    Hitstop(20)
    Unknown23159('PowerDunkTame')
    sprite('mk402_03', 2)	# 61-62
    Unknown7015()
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572614169720000000000000000000000000000fe03000000000000')
    tag_voice(0, 'bmk203_0', 'bmk203_1', 'bmk203_2', '')
    SFX_3('mkse_03')
    ScreenShake(0, 35000)
    sprite('mk402_04', 1)	# 63-63
    sprite('mk402_05', 1)	# 64-64
    sprite('mk402_06', 2)	# 65-66
    GFX_0('PowerDunkAirwallLv3', 0)
    sprite('mk402_07', 6)	# 67-72	 **attackbox here**
    GFX_0('DriveLv3PunchefPowerDunk', 0)
    Unknown1044()
    sprite('mk402_08', 2)	# 73-74
    Recovery()
    sprite('mk402_09', 2)	# 75-76
    sprite('mk402_10', 2)	# 77-78
    sprite('mk402_11', 2)	# 79-80
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk402_12', 3)	# 81-83
    sprite('mk402_13', 3)	# 84-86
    sprite('mk402_14', 3)	# 87-89
    label(100)
    sprite('mk020_07', 4)	# 90-93
    sprite('mk020_08', 4)	# 94-97
    loopRest()
    gotoLabel(100)

@State
def PowerDunk3():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackP1(80)
        AirHitstunAnimation(10)
        AirPushbackY(-44000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)
        PushbackX(19800)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown12051(2)
        Unknown3029(1)
        Unknown3069(0)
        Unknown23158('0a0000000d000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1043, 0)
        callSubroutine('MakotoDriveSetting')
        if Unknown23145('BunshinStepB'):
            AirPushbackX(15000)
            YAccel(80)
            setGravity(800)
        if Unknown23145('BunshinStepC'):
            Unknown1019(20)
            YAccel(80)
            setGravity(1600)
    sprite('mk402_00', 2)	# 1-2
    Unknown7014('mkse_00')
    sprite('mk402_01', 2)	# 3-4
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAuraAir', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk402_02', 2)	# 5-6
    sprite('mk402_01', 2)	# 7-8
    sprite('mk402_02', 2)	# 9-10
    SLOT_55 = 1
    GFX_0('DriveChargelightning', 1)
    sprite('mk402_01', 2)	# 11-12
    sprite('mk402_02', 2)	# 13-14
    sprite('mk402_01', 2)	# 15-16
    sprite('mk402_02', 2)	# 17-18
    sprite('mk402_01', 2)	# 19-20
    sprite('mk402_02', 2)	# 21-22
    sprite('mk402_01', 2)	# 23-24
    sprite('mk402_02', 2)	# 25-26
    sprite('mk402_01', 2)	# 27-28
    sprite('mk402_02', 2)	# 29-30
    sprite('mk402_01', 2)	# 31-32
    sprite('mk402_02', 2)	# 33-34
    sprite('mk402_01', 2)	# 35-36
    sprite('mk402_02', 2)	# 37-38
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    Damage(1700)
    sprite('mk402_03', 1)	# 39-39
    Unknown7015()
    Unknown3029(0)
    sprite('mk402_03', 1)	# 40-40
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572614169720000000000000000000000000000fe03000000000000')
    callSubroutine('AfterImage_Lv2')
    Unknown7007('626d6b3231335f30000000000000000064000000626d6b3231335f31000000000000000064000000626d6b3231335f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_1')
    ScreenShake(0, 35000)
    sprite('mk402_04', 2)	# 41-42
    setGravity(2000)
    sprite('mk402_05', 3)	# 43-45
    sprite('mk402_06', 3)	# 46-48
    GFX_0('PowerDunkAirwallLv2', 0)
    sprite('mk402_07ex', 20)	# 49-68	 **attackbox here**
    GFX_0('DriveLv2PunchefPowerDunk', 0)
    sprite('mk402_08', 3)	# 69-71
    Recovery()
    sprite('mk402_09', 3)	# 72-74
    sprite('mk402_10', 3)	# 75-77
    sprite('mk402_11', 3)	# 78-80
    loopRest()
    gotoLabel(99)
    label(2)
    AttackLevel_(5)
    Damage(2000)
    Hitstop(20)
    sprite('mk402_03', 1)	# 81-81
    Unknown7015()
    Unknown3029(0)
    sprite('mk402_03', 1)	# 82-82
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572614169720000000000000000000000000000fe03000000000000')
    callSubroutine('AfterImage_Lv3')
    SFX_1('mk213')
    SFX_3('mkse_03')
    ScreenShake(0, 35000)
    sprite('mk402_04', 1)	# 83-83
    setGravity(3100)
    sprite('mk402_05', 2)	# 84-85
    sprite('mk402_06', 2)	# 86-87
    GFX_0('PowerDunkAirwallLv3', 0)
    sprite('mk402_07ex', 20)	# 88-107	 **attackbox here**
    GFX_0('DriveLv3PunchefPowerDunk', 0)
    sprite('mk402_08', 3)	# 108-110
    Recovery()
    sprite('mk402_09', 3)	# 111-113
    sprite('mk402_10', 3)	# 114-116
    sprite('mk402_11', 3)	# 117-119
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('mk402_12', 3)	# 120-122
    sprite('mk402_13', 3)	# 123-125
    sprite('mk402_14', 3)	# 126-128

@State
def SiriusJolt():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        AttackP1(90)
        AttackP2(80)
        Damage(2000)
        Hitstop(22)
        AirUntechableTime(50)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(90000)
        AirPushbackY(35000)
        Unknown9178(1)
        WallbounceReboundTime(30)
        AirHitstunAfterWallbounce(40)
        Unknown9362(1)
        Unknown9364(30)
        Unknown30065(0)
        Unknown11091(10)
        Unknown11061(1)
        HitLow(4)
        HitAirUnblockable(4)
        HitOverhead(4)

        def upon_43():
            if (SLOT_48 == 1041):
                Unknown2003(1)

        def upon_3():
            Unknown48('190000000200000033000000160000000200000017000000')
            if (SLOT_51 == 0):
                RefreshMultihit()
            else:
                Unknown23027()

        def upon_12():
            ScreenShake(0, 50000)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(3)
            Unknown21015('6d6b65665f3431355f61746b00000000000000000000000000000000000000001104000000000000')
        Unknown2004(1, 0)
    sprite('mk415_00', 2)	# 1-2
    sprite('mk415_01', 2)	# 3-4
    sprite('mk415_02', 3)	# 5-7
    Unknown7007('626d6b3231365f30000000000000000064000000626d6b3231365f31000000000000000064000000626d6b3231365f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('mk415_03', 4)	# 8-11
    sprite('mk415_04', 4)	# 12-15
    sprite('mk415_05', 2)	# 16-17
    sprite('mk415_06', 2)	# 18-19
    Unknown2015(150)
    sprite('mk415_07', 2)	# 20-21
    sprite('mk415_08', 2)	# 22-23
    sprite('mk415_09', 2)	# 24-25
    SFX_0('003_swing_grap_0_2')
    sprite('mk415_10', 3)	# 26-28	 **attackbox here**
    GFX_0('mkef_415_atk', -1)
    GFX_0('mkef_415_punch', 0)
    GFX_1('mkef_415smoke', -1)
    SFX_3('mkse_03')
    sprite('mk415_11', 2)	# 29-30
    Unknown2015(100)
    Recovery()
    sprite('mk415_12', 2)	# 31-32
    sprite('mk415_13', 3)	# 33-35
    sprite('mk415_14', 3)	# 36-38
    sprite('mk415_15', 3)	# 39-41
    sprite('mk415_16', 5)	# 42-46
    sprite('mk415_17', 4)	# 47-50
    sprite('mk415_18', 4)	# 51-54

@State
def ShinSyouryu1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown11091(15)
        Hitstop(30)
        GroundedHitstunAnimation(2)
        AttackP2(100)
        Unknown9130(30)
        Unknown9142(60)
        PushbackX(0)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        YImpluseBeforeWallbounce(200)
        AirPushbackX(0)
        AirPushbackY(1000)
        Unknown11032('801a060050c30000ffffffffffffffff')
        Unknown11072(1, 150000, 75000)
        Unknown11062(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11064(1)
        Unknown11050('020000006d6b65665f3433314c7633666972737400000000000000000000000000000000')
        Unknown30048(1)
        Unknown11068(1)
        Unknown13024(0)

        def upon_12():
            Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
        Unknown1084(0)
        Unknown2004(1, 0)
        Unknown23079(0)
        HitCancel('ShinSyouryu2AINP')
        HitCancel('ShinSyouryu2BINP')
        HitCancel('ShinSyouryu2CINP')
        sendToLabelUpon(11, 30)
        Unknown23158('200000002a000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1061, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk431_00', 1)	# 1-1
    setInvincible(1)
    Unknown2036(42, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_MK', -1)
    Unknown30080('')
    sprite('mk431_01', 4)	# 2-5
    tag_voice(1, 'bmk252_0', 'bmk252_1', '', '')
    sprite('mk431_02', 3)	# 6-8
    sprite('mk431_03', 3)	# 9-11
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    sprite('mk431_04', 3)	# 12-14
    Unknown2037(3)
    label(10)
    sprite('mk431_03', 3)	# 15-17
    sprite('mk431_04', 2)	# 18-19
    sprite('mk431_04', 1)	# 20-20
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(10)
    label(11)
    sprite('mk431_03', 3)	# 21-23
    SLOT_55 = 1
    sprite('mk431_04', 3)	# 24-26
    sprite('mk431_03', 3)	# 27-29
    sprite('mk431_04', 3)	# 30-32
    SFX_0('005_swing_grap_2_1')
    Unknown2037(8)
    label(12)
    sprite('mk431_03', 3)	# 33-35
    setInvincible(0)
    sprite('mk431_04', 2)	# 36-37
    SFX_0('005_swing_grap_2_1')
    sprite('mk431_04', 1)	# 38-38
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(12)
    label(13)
    sprite('mk431_03', 3)	# 39-41
    sprite('mk431_04', 3)	# 42-44
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    Damage(1500)
    sprite('mk431_03', 2)	# 45-46
    callSubroutine('AfterImage_Lv2')
    sprite('mk431_04', 2)	# 47-48
    sprite('mk431_05', 3)	# 49-51
    GFX_0('DriveLv2PunchefSyouryu2', 4)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    GFX_0('mkef_jumpsmoke12', 0)
    GFX_0('DriveChargelightning', 1)
    GFX_0('DriveChargelightning', 2)
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_06', 4)	# 52-55	 **attackbox here**
    GFX_0('DriveChargelightning', 0)
    GFX_0('DriveChargelightning', 1)
    ScreenShake(0, 20000)
    loopRest()
    gotoLabel(29)
    label(2)
    AttackLevel_(5)
    Damage(2000)
    Unknown23159('ShinSyouryu1Tame')
    sprite('mk431_03', 1)	# 56-56
    callSubroutine('AfterImage_Lv3')
    sprite('mk431_04', 2)	# 57-58
    sprite('mk431_05', 3)	# 59-61
    GFX_0('DriveLv3PunchefSyouryu2', 4)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    GFX_0('mkef_jumpsmoke13', 0)
    GFX_0('DriveChargelightning', 1)
    GFX_0('DriveChargelightning', 2)
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_06', 4)	# 62-65	 **attackbox here**
    GFX_0('DriveChargelightning', 0)
    GFX_0('DriveChargelightning', 1)
    GFX_1('mkef_431Punch1st', 0)
    ScreenShake(0, 90000)
    loopRest()
    gotoLabel(29)
    label(3)
    AttackLevel_(5)
    Damage(1100)
    sprite('mk431_03', 1)	# 66-66
    callSubroutine('AfterImage_Lv3')
    sprite('mk431_04', 2)	# 67-68
    sprite('mk431_05', 3)	# 69-71
    GFX_0('DriveLv3PunchefSyouryu2', 4)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    GFX_0('mkef_jumpsmoke13', 0)
    GFX_0('DriveChargelightning', 1)
    GFX_0('DriveChargelightning', 2)
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_06', 4)	# 72-75	 **attackbox here**
    GFX_0('DriveChargelightning', 0)
    GFX_0('DriveChargelightning', 1)
    GFX_1('mkef_431Punch1st', 0)
    ScreenShake(0, 90000)
    loopRest()
    gotoLabel(29)
    label(29)
    sprite('mk431_33', 20)	# 76-95
    label(30)
    Unknown14077(0)
    setInvincible(0)
    sprite('mk431_33', 4)	# 96-99
    Unknown13024(1)
    sprite('mk431_34', 6)	# 100-105
    tag_voice(0, 'bmk253_0', 'bmk253_1', '', '')
    sprite('mk431_35', 20)	# 106-125
    Unknown3029(0)
    sprite('mk431_36', 4)	# 126-129
    sprite('mk431_37', 4)	# 130-133
    sprite('mk431_38', 4)	# 134-137
    physicsXImpulse(-2000)
    sprite('mk431_39', 4)	# 138-141
    sprite('mk431_40', 4)	# 142-145
    sprite('mk431_41', 4)	# 146-149
    sprite('mk431_42', 4)	# 150-153
    physicsXImpulse(0)

@State
def ShinSyouryu2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown11091(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AttackP2(60)
        AirPushbackX(-3000)
        AirPushbackY(80000)
        AirUntechableTime(150)
        Hitstop(30)
        Unknown11001(0, 4, 4)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11032('801a060050c30000ffffffffffffffff')
        Unknown11062(1)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown30048(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
        Unknown1084(0)
        HitCancel('ShinSyouryu3AINP')
        HitCancel('ShinSyouryu3BINP')
        HitCancel('ShinSyouryu3CINP')
        setInvincible(1)
        Unknown23158('1c00000026000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1062, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk431_07', 4)	# 1-4
    setInvincible(1)
    Unknown2036(43, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    sprite('mk431_08', 4)	# 5-8
    sprite('mk431_09', 4)	# 9-12
    sprite('mk431_10', 3)	# 13-15
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    sprite('mk431_11', 3)	# 16-18
    Unknown2037(2)
    label(10)
    sprite('mk431_10', 3)	# 19-21
    sprite('mk431_11', 2)	# 22-23
    sprite('mk431_11', 1)	# 24-24
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(10)
    label(11)
    sprite('mk431_10', 2)	# 25-26
    SLOT_55 = 1
    sprite('mk431_11', 3)	# 27-29
    Unknown2037(7)
    label(12)
    sprite('mk431_10', 3)	# 30-32
    sprite('mk431_11', 2)	# 33-34
    sprite('mk431_11', 1)	# 35-35
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(12)
    label(13)
    sprite('mk431_10', 3)	# 36-38
    sprite('mk431_11', 3)	# 39-41
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    Damage(1500)
    sprite('mk431_10', 2)	# 42-43
    callSubroutine('AfterImage_Lv2')
    sprite('mk431_11', 2)	# 44-45
    tag_voice(0, 'bmk254_0', 'bmk254_1', '', '')
    sprite('mk431_12', 3)	# 46-48
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_13', 4)	# 49-52	 **attackbox here**
    GFX_0('DriveLv2Punchef2D', 2)
    GFX_0('mkef_431Lv2secondtame', 0)
    GFX_0('mkef_431_2ndsub_back', 0)
    GFX_0('mkef_jumpsmoke22', 1)
    ScreenShake(0, 72000)
    Unknown13024(1)
    sprite('mk431_14', 5)	# 53-57
    GFX_0('mkef_431Lv2second', 0)
    loopRest()
    gotoLabel(30)
    label(2)
    AttackLevel_(5)
    Damage(2000)
    Unknown23159('ShinSyouryu2Tame')
    sprite('mk431_10', 2)	# 58-59
    callSubroutine('AfterImage_Lv3')
    sprite('mk431_11', 3)	# 60-62
    tag_voice(0, 'bmk254_0', 'bmk254_1', '', '')
    sprite('mk431_12', 4)	# 63-66
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_13', 4)	# 67-70	 **attackbox here**
    GFX_0('DriveLv3Punchef2D', 2)
    GFX_0('mkef_431Lv3secondtame', 0)
    GFX_0('mkef_431_2ndsub_back', 0)
    GFX_0('mkef_jumpsmoke23', 1)
    ScreenShake(0, 90000)
    Unknown13024(1)
    sprite('mk431_14', 5)	# 71-75
    GFX_0('mkef_431Lv3second', 0)
    loopRest()
    gotoLabel(30)
    label(3)
    AttackLevel_(5)
    Damage(1100)
    sprite('mk431_10', 2)	# 76-77
    callSubroutine('AfterImage_Lv3')
    sprite('mk431_11', 3)	# 78-80
    SFX_1('mk254')
    sprite('mk431_12', 4)	# 81-84
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_13', 4)	# 85-88	 **attackbox here**
    GFX_0('DriveLv3Punchef2D', 2)
    GFX_0('mkef_431Lv3secondtame', 0)
    GFX_0('mkef_431_2ndsub_back', 0)
    GFX_0('mkef_jumpsmoke23', 1)
    ScreenShake(0, 90000)
    Unknown13024(1)
    sprite('mk431_14', 5)	# 89-93
    GFX_0('mkef_431Lv3second', 0)
    loopRest()
    gotoLabel(30)
    label(30)
    sprite('mk431_15', 5)	# 94-98
    sprite('mk431_16', 6)	# 99-104
    Unknown14077(0)
    setInvincible(0)
    sprite('mk431_17', 16)	# 105-120
    sprite('mk410_12', 3)	# 121-123	 **attackbox here**
    StartMultihit()
    sprite('mk410_13', 3)	# 124-126
    sprite('mk410_14', 3)	# 127-129
    sprite('mk410_15', 3)	# 130-132
    sprite('mk410_16', 3)	# 133-135
    sprite('mk410_17', 3)	# 136-138
    sprite('mk410_18', 3)	# 139-141
    sprite('mk410_19', 3)	# 142-144

@State
def ShinSyouryu3():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        Unknown11091(15)
        AttackP2(100)
        Hitstop(35)
        AirHitstunAnimation(10)
        AirUntechableTime(100)
        Unknown9310(20)
        AirPushbackY(-100000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11108('03000000')
        Unknown30048(1)
        Unknown11068(1)
        setInvincible(1)
        Unknown13024(0)
        Unknown22004(12, 1)
        Unknown2017(0)
        Unknown23158('3c00000046000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1063, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk431_17', 3)	# 1-3
    sprite('mk431_18', 3)	# 4-6
    GFX_0('mk431dummy', -1)
    sprite('null', 3)	# 7-9
    GFX_0('mk431_dmyatk', 100)
    sprite('mk431_19', 3)	# 10-12
    Unknown20000(1)
    teleportRelativeY(1650000)
    sprite('mk431_20', 3)	# 13-15
    sprite('mk431_21', 3)	# 16-18
    sprite('mk431_22', 3)	# 19-21
    sprite('mk431_21', 3)	# 22-24
    sprite('mk431_22', 3)	# 25-27
    sprite('mk431_21', 3)	# 28-30
    Unknown2036(50, -1, 0)
    sprite('mk431_22', 3)	# 31-33
    ScreenShake(2000, 0)
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk431_21', 3)	# 34-36
    sprite('mk431_22', 3)	# 37-39
    sprite('mk431_21', 3)	# 40-42
    GFX_0('DriveChargelightning', 0)
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 43-45
    sprite('mk431_21', 3)	# 46-48
    sprite('mk431_22', 3)	# 49-51
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk431_21', 3)	# 52-54
    sprite('mk431_22', 3)	# 55-57
    GFX_0('DriveChargelightning', 0)
    ScreenShake(8000, 0)
    sprite('mk431_21', 3)	# 58-60
    sprite('mk431_22', 3)	# 61-63
    sprite('mk431_21', 3)	# 64-66
    GFX_0('DriveChargelightning', 0)
    ScreenShake(10000, 0)
    sprite('mk431_21', 3)	# 67-69
    sprite('mk431_22', 3)	# 70-72
    GFX_0('DriveChargelightning', 0)
    ScreenShake(12000, 0)
    sprite('mk431_21', 3)	# 73-75
    SLOT_55 = 1
    sprite('mk431_22', 3)	# 76-78
    GFX_0('DriveChargelightning', 0)
    ScreenShake(14000, 0)
    sprite('mk431_21', 3)	# 79-81
    sprite('mk431_22', 3)	# 82-84
    sprite('mk431_21', 3)	# 85-87
    GFX_0('DriveChargelightning', 0)
    ScreenShake(16000, 0)
    sprite('mk431_22', 3)	# 88-90
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 91-93
    sprite('mk431_22', 3)	# 94-96
    ScreenShake(14000, 0)
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 97-99
    sprite('mk431_22', 3)	# 100-102
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 103-105
    ScreenShake(10000, 0)
    sprite('mk431_22', 3)	# 106-108
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 109-111
    sprite('mk431_22', 3)	# 112-114
    SFX_0('019_quake_0')
    ScreenShake(8000, 0)
    sprite('mk431_21', 3)	# 115-117
    sprite('mk431_22', 3)	# 118-120
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 121-123
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 124-126
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 127-129
    sprite('mk431_22', 3)	# 130-132
    SFX_0('019_quake_0')
    ScreenShake(4000, 0)
    sprite('mk431_21', 3)	# 133-135
    sprite('mk431_22', 3)	# 136-138
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 139-141
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 142-144
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 145-147
    sprite('mk431_22', 3)	# 148-150
    SFX_0('019_quake_0')
    ScreenShake(4000, 0)
    sprite('mk431_21', 3)	# 151-153
    sprite('mk431_22', 3)	# 154-156
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 157-159
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 160-162
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 163-165
    sprite('mk431_22', 3)	# 166-168
    SFX_0('019_quake_0')
    ScreenShake(4000, 0)
    sprite('mk431_21', 3)	# 169-171
    sprite('mk431_22', 3)	# 172-174
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 175-177
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 178-180
    SLOT_55 = 0
    loopRest()
    label(1)
    AttackLevel_(4)
    Damage(5000)
    sprite('mk431_21', 3)	# 181-183
    callSubroutine('AfterImage_Lv2')
    tag_voice(0, 'bmk255_0', 'bmk255_1', '', '')
    sprite('mk431_22', 3)	# 184-186
    sprite('mk431_23', 3)	# 187-189
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk431_24', 3)	# 190-192
    sprite('mk431_25', 3)	# 193-195
    SFX_3('mkse_04')
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    GFX_0('mk431cutin_punchLv2', -1)
    sprite('mk431_26', 3)	# 196-198	 **attackbox here**
    GFX_0('DriveLv2PunchefPowerDunk', 1)
    GFX_1('mkef_431hit3rd', 0)
    RefreshMultihit()
    ScreenShake(0, 72000)
    sprite('mk431_26', 3)	# 199-201	 **attackbox here**
    loopRest()
    gotoLabel(30)
    label(2)
    AttackLevel_(5)
    Damage(7900)
    Unknown23159('ShinSyouryu3Tame')
    sprite('mk431_21', 3)	# 202-204
    Unknown21015('6d6b343331637574696e5f7570000000000000000000000000000000000000002804000000000000')
    tag_voice(0, 'bmk255_0', 'bmk255_1', '', '')
    callSubroutine('AfterImage_Lv3')
    sprite('mk431_22', 3)	# 205-207
    sprite('mk431_23', 3)	# 208-210
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk431_24', 3)	# 211-213
    sprite('mk431_25', 3)	# 214-216
    SFX_3('mkse_04')
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    GFX_0('mk431cutin_punchLv3', -1)
    sprite('mk431_26', 3)	# 217-219	 **attackbox here**
    GFX_0('DriveLv3PunchefPowerDunk', 1)
    GFX_1('mkef_431hit3rd', 0)
    GFX_1('mkef_431hit3rd', 0)
    RefreshMultihit()
    ScreenShake(0, 120000)
    sprite('mk431_26', 3)	# 220-222	 **attackbox here**
    loopRest()
    gotoLabel(30)
    label(3)
    AttackLevel_(5)
    Damage(4200)
    sprite('mk431_21', 3)	# 223-225
    Unknown21015('6d6b343331637574696e5f7570000000000000000000000000000000000000002804000000000000')
    SFX_1('mk255')
    callSubroutine('AfterImage_Lv3')
    sprite('mk431_22', 3)	# 226-228
    sprite('mk431_23', 3)	# 229-231
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk431_24', 3)	# 232-234
    sprite('mk431_25', 3)	# 235-237
    SFX_3('mkse_04')
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    GFX_0('mk431cutin_punchLv3', -1)
    sprite('mk431_26', 3)	# 238-240	 **attackbox here**
    GFX_0('DriveLv3PunchefPowerDunk', 1)
    GFX_1('mkef_431hit3rd', 0)
    GFX_1('mkef_431hit3rd', 0)
    RefreshMultihit()
    ScreenShake(0, 120000)
    sprite('mk431_26', 3)	# 241-243	 **attackbox here**
    loopRest()
    gotoLabel(30)
    label(30)
    sprite('mk431_28', 3)	# 244-246
    Unknown1044()
    Unknown2017(1)
    sprite('mk431_29', 3)	# 247-249
    sprite('mk431_30', 3)	# 250-252
    Unknown3029(0)
    sprite('mk431_31', 3)	# 253-255
    sprite('mk431_32', 3)	# 256-258
    Unknown13024(1)
    sprite('mk020_06', 5)	# 259-263
    label(35)
    sprite('mk020_07', 4)	# 264-267
    Unknown20000(0)
    sprite('mk020_08', 4)	# 268-271
    gotoLabel(35)

@State
def ShinSyouryu1_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        AttackP2(100)
        Damage(2000)
        Unknown11091(15)
        Hitstop(30)
        GroundedHitstunAnimation(2)
        Unknown9130(30)
        Unknown9142(60)
        PushbackX(0)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        YImpluseBeforeWallbounce(100)
        AirPushbackX(0)
        AirPushbackY(100)
        Unknown11032('801a060050c30000ffffffffffffffff')
        Unknown11072(1, 150000, 75000)
        Unknown11062(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11064(1)
        Unknown11050('020000006d6b65665f3433314c7633666972737400000000000000000000000000000000')
        Unknown30048(1)
        Unknown11068(1)
        Unknown13024(0)

        def upon_12():
            Unknown2017(0)

        def upon_STATE_END():
            Unknown2017(1)
        Unknown1084(0)
        Unknown2004(1, 0)
        Unknown23079(0)
        HitCancel('ShinSyouryu2_ODAINP')
        HitCancel('ShinSyouryu2_ODBINP')
        HitCancel('ShinSyouryu2_ODCINP')
        sendToLabelUpon(11, 30)
        Unknown23158('160000002a000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1061, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk431_00', 1)	# 1-1
    Unknown23008(0, 0)
    setInvincible(1)
    Unknown2036(42, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_MK', -1)
    Unknown30080('')
    sprite('mk431_01', 4)	# 2-5
    tag_voice(1, 'bmk252_0', 'bmk252_1', '', '')
    sprite('mk431_02', 3)	# 6-8
    sprite('mk431_03', 3)	# 9-11
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    sprite('mk431_04', 3)	# 12-14
    Unknown2037(3)
    label(10)
    sprite('mk431_03', 3)	# 15-17
    sprite('mk431_04', 2)	# 18-19
    sprite('mk431_04', 1)	# 20-20
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(10)
    label(11)
    sprite('mk431_03', 3)	# 21-23
    SLOT_55 = 1
    sprite('mk431_04', 3)	# 24-26
    sprite('mk431_03', 3)	# 27-29
    sprite('mk431_04', 3)	# 30-32
    SFX_0('005_swing_grap_2_1')
    Unknown2037(8)
    label(12)
    sprite('mk431_03', 3)	# 33-35
    setInvincible(0)
    sprite('mk431_04', 2)	# 36-37
    SFX_0('005_swing_grap_2_1')
    sprite('mk431_04', 1)	# 38-38
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(12)
    label(13)
    sprite('mk431_03', 3)	# 39-41
    sprite('mk431_04', 3)	# 42-44
    SLOT_55 = 0
    loopRest()
    label(1)
    label(2)
    label(3)
    label(4)
    sprite('mk431_03', 2)	# 45-46
    sprite('mk431_04', 2)	# 47-48
    sprite('mk431_05', 3)	# 49-51
    GFX_0('DriveLv3PunchefSyouryu2', 4)
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    GFX_0('mkef_jumpsmoke13', 0)
    GFX_0('DriveChargelightning', 1)
    GFX_0('DriveChargelightning', 2)
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_06', 4)	# 52-55	 **attackbox here**
    GFX_0('DriveChargelightning', 0)
    GFX_0('DriveChargelightning', 1)
    GFX_1('mkef_431Punch1st', 0)
    callSubroutine('AfterImage_LvG')
    ScreenShake(0, 90000)
    sprite('mk431_33', 20)	# 56-75
    label(30)
    Unknown14077(0)
    setInvincible(0)
    sprite('mk431_33', 4)	# 76-79
    Unknown13024(1)
    sprite('mk431_34', 6)	# 80-85
    SFX_1('mk253')
    sprite('mk431_35', 20)	# 86-105
    Unknown3029(0)
    sprite('mk431_36', 4)	# 106-109
    sprite('mk431_37', 4)	# 110-113
    sprite('mk431_38', 4)	# 114-117
    physicsXImpulse(-2000)
    sprite('mk431_39', 4)	# 118-121
    sprite('mk431_40', 4)	# 122-125
    sprite('mk431_41', 4)	# 126-129
    sprite('mk431_42', 4)	# 130-133
    physicsXImpulse(0)

@State
def ShinSyouryu2_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(3)
        Damage(30)
        Unknown11091(15)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-3000)
        AirPushbackY(80000)
        AirUntechableTime(150)
        Unknown9154(30)
        Hitstop(1)
        Unknown11001(0, 4, 4)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11032('801a060050c30000ffffffffffffffff')
        Unknown11062(1)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown30048(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2017(1)
        Unknown1084(0)
        Unknown13024(0)
        setInvincible(1)

        def upon_11():
            if SLOT_2:
                PushbackX(2500)
                AirHitstunAnimation(5)
                GroundedHitstunAnimation(5)
                Unknown2037(0)
            else:
                PushbackX(-2500)
                AirHitstunAnimation(4)
                GroundedHitstunAnimation(4)
                Unknown2037(1)
        SLOT_51 = 1
        Unknown23158('1700000026000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1062, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk431_07', 4)	# 1-4
    Unknown23008(0, 0)
    Unknown2036(43, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    sprite('mk431_08', 4)	# 5-8
    sprite('mk431_09', 4)	# 9-12
    sprite('mk431_10', 3)	# 13-15
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    sprite('mk431_11', 3)	# 16-18
    Unknown2037(2)
    label(10)
    sprite('mk431_10', 3)	# 19-21
    sprite('mk431_11', 2)	# 22-23
    sprite('mk431_11', 1)	# 24-24
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(10)
    else:
        sendToLabel(11)
    label(11)
    sprite('mk431_10', 2)	# 25-26
    SLOT_55 = 1
    sprite('mk431_11', 3)	# 27-29
    Unknown2037(7)
    label(12)
    sprite('mk431_10', 3)	# 30-32
    sprite('mk431_11', 2)	# 33-34
    sprite('mk431_11', 1)	# 35-35
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(12)
    else:
        sendToLabel(13)
    label(13)
    sprite('mk431_10', 3)	# 36-38
    sprite('mk431_11', 3)	# 39-41
    SLOT_55 = 0
    loopRest()
    label(1)
    label(2)
    label(3)
    label(4)
    sprite('mk431_10', 3)	# 42-44
    callSubroutine('AfterImage_LvG')
    sprite('mk450_19', 4)	# 45-48
    sprite('mk450_20', 4)	# 49-52
    GFX_0('mk450_footef', 0)
    tag_voice(0, 'bmk291_0', 'bmk291_1', '', '')
    sprite('mk450_21', 2)	# 53-54	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(10000)
    ScreenShake(0, 20000)
    GFX_0('mk450_hibana', -1)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_22', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex00', 2)	# 59-60	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    ScreenShake(0, 20000)
    sprite('mk450_23ex01', 2)	# 61-62	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex02', 2)	# 63-64	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex03', 2)	# 65-66	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex04', 2)	# 67-68	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    ScreenShake(0, 20000)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_23ex05', 2)	# 69-70	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex06', 2)	# 71-72	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex07', 2)	# 73-74	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex08', 2)	# 75-76	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    ScreenShake(0, 20000)
    sprite('mk450_23ex09', 2)	# 77-78	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex10', 2)	# 79-80	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex11', 2)	# 81-82	 **attackbox here**
    RefreshMultihit()
    GFX_0('mk450_footef', 0)
    sprite('mk450_23ex12', 2)	# 83-84	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    ScreenShake(0, 20000)
    sprite('mk450_23ex13', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex14', 2)	# 87-88	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex15', 2)	# 89-90	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex16', 2)	# 91-92	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    ScreenShake(0, 20000)
    sprite('mk450_23ex17', 2)	# 93-94	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex18', 2)	# 95-96	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex19', 2)	# 97-98	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex20', 2)	# 99-100	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    ScreenShake(0, 20000)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_23ex21', 2)	# 101-102	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex22', 2)	# 103-104	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex23', 2)	# 105-106	 **attackbox here**
    RefreshMultihit()
    sprite('mk450_23ex24', 2)	# 107-108	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    ScreenShake(0, 20000)
    sprite('mk431_11', 3)	# 109-111
    SFX_1('mk254')
    sprite('mk431_12', 4)	# 112-115
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    sprite('mk431_13', 4)	# 116-119	 **attackbox here**
    clearUponHandler(11)

    def upon_12():
        HitCancel('ShinSyouryu3_ODAINP')
        HitCancel('ShinSyouryu3_ODBINP')
        HitCancel('ShinSyouryu3_ODCINP')
        Unknown13024(1)
        clearUponHandler(12)
    GFX_0('DriveLv3Punchef2D', 2)
    GFX_0('mkef_431Lv3secondtame', 0)
    GFX_0('mkef_431_2ndsub_back', 0)
    GFX_0('mkef_jumpsmoke23', 1)
    ScreenShake(0, 90000)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1200)
    AttackP2(60)
    Hitstop(30)
    Unknown11001(0, 4, 4)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    if SLOT_136:
        Unknown10000(80)
    sprite('mk431_14', 5)	# 120-124
    GFX_0('mkef_431Lv3second', 0)
    sprite('mk431_15', 5)	# 125-129
    sprite('mk431_16', 6)	# 130-135
    Unknown13024(1)
    Unknown14077(0)
    setInvincible(0)
    Unknown2021(0)
    sprite('mk431_17', 16)	# 136-151
    sprite('mk410_12', 3)	# 152-154	 **attackbox here**
    StartMultihit()
    sprite('mk410_13', 3)	# 155-157
    sprite('mk410_14', 3)	# 158-160
    sprite('mk410_15', 3)	# 161-163
    sprite('mk410_16', 3)	# 164-166
    sprite('mk410_17', 3)	# 167-169
    sprite('mk410_18', 3)	# 170-172
    sprite('mk410_19', 3)	# 173-175

@State
def ShinSyouryu3_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(10500)
        Unknown11091(15)
        AttackP2(100)
        Hitstop(35)
        AirHitstunAnimation(10)
        AirUntechableTime(100)
        Unknown9310(20)
        AirPushbackY(-100000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11108('03000000')
        Unknown30048(1)
        Unknown11068(1)
        setInvincible(1)
        Unknown13024(0)
        Unknown22004(12, 1)
        Unknown2017(0)
        SLOT_51 = 1
        Unknown23158('3200000046000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1063, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk431_17', 3)	# 1-3
    Unknown23008(0, 0)
    sprite('mk431_18', 3)	# 4-6
    GFX_0('mk431dummy', -1)
    sprite('null', 3)	# 7-9
    GFX_0('mk431_dmyatkOD', 100)
    sprite('mk431_19', 3)	# 10-12
    Unknown20000(1)
    teleportRelativeY(1650000)
    sprite('mk431_20', 3)	# 13-15
    sprite('mk431_21', 3)	# 16-18
    sprite('mk431_22', 3)	# 19-21
    sprite('mk431_21', 3)	# 22-24
    sprite('mk431_22', 3)	# 25-27
    sprite('mk431_21', 3)	# 28-30
    Unknown2036(50, -1, 0)
    sprite('mk431_22', 3)	# 31-33
    ScreenShake(2000, 0)
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk431_21', 3)	# 34-36
    sprite('mk431_22', 3)	# 37-39
    sprite('mk431_21', 3)	# 40-42
    GFX_0('DriveChargelightning', 0)
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 43-45
    sprite('mk431_21', 3)	# 46-48
    sprite('mk431_22', 3)	# 49-51
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk431_21', 3)	# 52-54
    sprite('mk431_22', 3)	# 55-57
    GFX_0('DriveChargelightning', 0)
    ScreenShake(8000, 0)
    sprite('mk431_21', 3)	# 58-60
    sprite('mk431_22', 3)	# 61-63
    sprite('mk431_21', 3)	# 64-66
    GFX_0('DriveChargelightning', 0)
    ScreenShake(10000, 0)
    sprite('mk431_21', 3)	# 67-69
    sprite('mk431_22', 3)	# 70-72
    GFX_0('DriveChargelightning', 0)
    ScreenShake(12000, 0)
    sprite('mk431_21', 3)	# 73-75
    SLOT_55 = 1
    sprite('mk431_22', 3)	# 76-78
    GFX_0('DriveChargelightning', 0)
    ScreenShake(14000, 0)
    sprite('mk431_21', 3)	# 79-81
    sprite('mk431_22', 3)	# 82-84
    sprite('mk431_21', 3)	# 85-87
    GFX_0('DriveChargelightning', 0)
    ScreenShake(16000, 0)
    sprite('mk431_22', 3)	# 88-90
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 91-93
    sprite('mk431_22', 3)	# 94-96
    ScreenShake(14000, 0)
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 97-99
    sprite('mk431_22', 3)	# 100-102
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 103-105
    ScreenShake(10000, 0)
    sprite('mk431_22', 3)	# 106-108
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 109-111
    sprite('mk431_22', 3)	# 112-114
    SFX_0('019_quake_0')
    ScreenShake(8000, 0)
    sprite('mk431_21', 3)	# 115-117
    sprite('mk431_22', 3)	# 118-120
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 121-123
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 124-126
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 127-129
    sprite('mk431_22', 3)	# 130-132
    SFX_0('019_quake_0')
    ScreenShake(4000, 0)
    sprite('mk431_21', 3)	# 133-135
    sprite('mk431_22', 3)	# 136-138
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 139-141
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 142-144
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 145-147
    sprite('mk431_22', 3)	# 148-150
    SFX_0('019_quake_0')
    ScreenShake(4000, 0)
    sprite('mk431_21', 3)	# 151-153
    sprite('mk431_22', 3)	# 154-156
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 157-159
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 160-162
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 163-165
    sprite('mk431_22', 3)	# 166-168
    SFX_0('019_quake_0')
    ScreenShake(4000, 0)
    sprite('mk431_21', 3)	# 169-171
    sprite('mk431_22', 3)	# 172-174
    SFX_0('019_quake_0')
    sprite('mk431_21', 3)	# 175-177
    ScreenShake(4000, 0)
    sprite('mk431_22', 3)	# 178-180
    SLOT_55 = 0
    loopRest()
    label(1)
    label(2)
    label(3)
    label(4)
    sprite('mk431_21', 3)	# 181-183
    Unknown21015('6d6b343331637574696e5f7570000000000000000000000000000000000000002804000000000000')
    tag_voice(0, 'bmk255_0', 'bmk255_1', '', '')
    callSubroutine('AfterImage_LvG')
    sprite('mk431_22', 3)	# 184-186
    sprite('mk431_23', 3)	# 187-189
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk431_24', 3)	# 190-192
    sprite('mk431_25', 3)	# 193-195
    SFX_3('mkse_04')
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    GFX_0('mk431cutin_punchLvG', -1)
    sprite('mk431_26', 3)	# 196-198	 **attackbox here**
    GFX_0('DriveLvG_PunchefPowerDunk', 1)
    GFX_1('mkef_431hit3rd', 0)
    GFX_1('mkef_431hit3rd', 0)
    RefreshMultihit()
    ScreenShake(0, 120000)
    sprite('mk431_26', 3)	# 199-201	 **attackbox here**
    Unknown36(22)
    Unknown1044()
    Unknown35()
    sprite('mk431_28', 3)	# 202-204
    Unknown1044()
    Unknown2017(1)
    sprite('mk431_29', 3)	# 205-207
    sprite('mk431_30', 3)	# 208-210
    Unknown3029(0)
    sprite('mk431_31', 3)	# 211-213
    sprite('mk431_32', 3)	# 214-216
    Unknown13024(1)
    sprite('mk020_06', 5)	# 217-221
    label(35)
    sprite('mk020_07', 4)	# 222-225
    Unknown13024(1)
    Unknown20000(0)
    sprite('mk020_08', 4)	# 226-229
    gotoLabel(35)

@State
def BigPunch():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown1084(0)
        Unknown2003(1)
        Unknown2004(1, 0)
        Unknown23158('410000004b000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1065, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk430_00', 4)	# 1-4
    tag_voice(1, 'bmk250_0', 'bmk250_1', '', '')
    setInvincible(1)
    sprite('mk430_01', 16)	# 5-20
    Unknown2036(192, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_MK', -1)
    Unknown30080('')
    sprite('mk430_02', 4)	# 21-24
    sprite('mk430_03', 4)	# 25-28
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargeWind', 1)
    sprite('mk430_04', 3)	# 29-31
    sprite('mk430_05', 3)	# 32-34
    Unknown2037(4)
    label(10)
    sprite('mk430_04', 3)	# 35-37
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_05', 3)	# 38-40
    sprite('mk430_04', 3)	# 41-43
    sprite('mk430_05', 3)	# 44-46
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_04', 3)	# 47-49
    sprite('mk430_05', 2)	# 50-51
    sprite('mk430_05', 1)	# 52-52
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(10)
    label(11)
    sprite('mk430_04', 3)	# 53-55
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_05', 3)	# 56-58
    sprite('mk430_04', 3)	# 59-61
    SLOT_55 = 1
    sprite('mk430_05', 3)	# 62-64
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_04', 3)	# 65-67
    sprite('mk430_05', 3)	# 68-70
    sprite('mk430_04', 3)	# 71-73
    GFX_0('DriveChargelightning', 0)
    SLOT_55 = 0
    loopRest()
    label(1)
    sprite('mk430_04', 3)	# 74-76
    GFX_0('BigPunch_SE', -1)
    sprite('mk430_05', 3)	# 77-79
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk430_06', 7)	# 80-86
    tag_voice(0, 'bmk251_0', 'bmk251_1', '', '')
    sprite('mk430_07', 8)	# 87-94
    sprite('mk430_08', 9)	# 95-103
    sprite('mk430_09', 10)	# 104-113
    sprite('mk430_10', 12)	# 114-125
    GFX_0('mkef_circle_small', 1)
    GFX_0('mkef_circle_middle', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 14)	# 126-139
    GFX_0('mkef_mahojin_middle', 1)
    GFX_0('mkef_mahojin_middle', 1)
    GFX_0('mkef_430circlering_lv2', 1)
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk430_12', 4)	# 140-143
    ScreenShake(8000, 0)
    sprite('mk430_13', 4)	# 144-147
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 3)	# 148-150	 **attackbox here**
    GFX_0('mk430cutin_lv2', -1)
    GFX_0('DriveLv2PunchefD', 1)
    GFX_0('mkef_jumpsmoke22', 2)
    ScreenShake(0, 20000)
    loopRest()
    gotoLabel(29)
    label(2)
    sprite('mk430_04', 3)	# 151-153
    GFX_0('BigPunch_SE', -1)
    sprite('mk430_05', 3)	# 154-156
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk430_06', 7)	# 157-163
    tag_voice(0, 'bmk251_0', 'bmk251_1', '', '')
    sprite('mk430_07', 8)	# 164-171
    sprite('mk430_08', 9)	# 172-180
    sprite('mk430_09', 10)	# 181-190
    sprite('mk430_10', 12)	# 191-202
    GFX_0('mkef_circle_middle', 1)
    GFX_0('mkef_circle_large', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 14)	# 203-216
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_430circlering_lv3', 1)
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk430_12', 4)	# 217-220
    ScreenShake(8000, 0)
    sprite('mk430_13', 4)	# 221-224
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 3)	# 225-227	 **attackbox here**
    GFX_0('mk430cutin_lv3', -1)
    GFX_0('DriveLv3PunchefD', 1)
    GFX_0('mkef_jumpsmoke23', 2)
    ScreenShake(0, 35000)
    callSubroutine('AfterImage_Lv3')
    loopRest()
    gotoLabel(29)
    label(3)
    sprite('mk430_04', 3)	# 228-230
    GFX_0('BigPunch_SE', -1)
    sprite('mk430_05', 3)	# 231-233
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk430_06', 7)	# 234-240
    SFX_1('mk251')
    sprite('mk430_07', 8)	# 241-248
    sprite('mk430_08', 9)	# 249-257
    sprite('mk430_09', 10)	# 258-267
    sprite('mk430_10', 12)	# 268-279
    GFX_0('mkef_circle_middle', 1)
    GFX_0('mkef_circle_large', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 14)	# 280-293
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_430circlering_lv3', 1)
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk430_12', 4)	# 294-297
    ScreenShake(8000, 0)
    sprite('mk430_13', 4)	# 298-301
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 3)	# 302-304	 **attackbox here**
    GFX_0('mk430cutin_lv3', -1)
    GFX_0('DriveLv3PunchefD', 1)
    GFX_0('mkef_jumpsmoke23', 2)
    ScreenShake(0, 35000)
    callSubroutine('AfterImage_Lv3')
    loopRest()
    gotoLabel(29)
    label(29)
    sprite('mk430_15', 3)	# 305-307	 **attackbox here**
    sprite('mk430_14', 3)	# 308-310	 **attackbox here**
    setInvincible(0)
    sprite('mk430_15', 3)	# 311-313	 **attackbox here**
    sprite('mk430_14', 3)	# 314-316	 **attackbox here**
    sprite('mk430_15', 3)	# 317-319	 **attackbox here**
    sprite('mk430_14', 4)	# 320-323	 **attackbox here**
    sprite('mk430_15', 4)	# 324-327	 **attackbox here**
    sprite('mk430_14', 5)	# 328-332	 **attackbox here**
    sprite('mk430_15', 5)	# 333-337	 **attackbox here**
    sprite('mk430_16', 5)	# 338-342	 **attackbox here**
    sprite('mk430_17', 5)	# 343-347
    sprite('mk430_18', 5)	# 348-352
    sprite('mk430_19', 5)	# 353-357
    sprite('mk430_20', 5)	# 358-362

@State
def BigPunch_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        Unknown1084(0)
        Unknown2003(1)
        Unknown2004(1, 0)
        Unknown23158('3c0000004b000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1065, 0)
    sprite('mk430_00', 4)	# 1-4
    tag_voice(1, 'bmk250_0', 'bmk250_1', '', '')
    setInvincible(1)
    sprite('mk430_01', 16)	# 5-20
    Unknown2036(201, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_MK', -1)
    Unknown30080('')
    sprite('mk430_02', 4)	# 21-24
    sprite('mk430_03', 4)	# 25-28
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargeWind', 1)
    sprite('mk430_04', 3)	# 29-31
    sprite('mk430_05', 3)	# 32-34
    Unknown2037(4)
    label(10)
    sprite('mk430_04', 3)	# 35-37
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_05', 3)	# 38-40
    sprite('mk430_04', 3)	# 41-43
    sprite('mk430_05', 3)	# 44-46
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_04', 3)	# 47-49
    sprite('mk430_05', 2)	# 50-51
    sprite('mk430_05', 1)	# 52-52
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(10)
    else:
        sendToLabel(11)
    label(11)
    sprite('mk430_04', 3)	# 53-55
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_05', 3)	# 56-58
    sprite('mk430_04', 3)	# 59-61
    SLOT_55 = 1
    sprite('mk430_05', 3)	# 62-64
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_04', 3)	# 65-67
    sprite('mk430_05', 3)	# 68-70
    sprite('mk430_04', 3)	# 71-73
    GFX_0('DriveChargelightning', 0)
    SLOT_55 = 0
    loopRest()
    label(1)
    label(2)
    label(3)
    label(4)
    sprite('mk430_04', 3)	# 74-76
    GFX_0('BigPunch_SE', -1)
    sprite('mk430_05', 3)	# 77-79
    Unknown21015('447269766543686172676557696e640000000000000000000000000000000000ff03000000000000')
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    sprite('mk430_06', 7)	# 80-86
    tag_voice(0, 'bmk251_0', 'bmk251_1', '', '')
    sprite('mk430_07', 8)	# 87-94
    sprite('mk430_08', 9)	# 95-103
    sprite('mk430_09', 10)	# 104-113
    sprite('mk430_10', 11)	# 114-124
    GFX_0('mkef_circle_middle', 1)
    GFX_0('mkef_circle_large', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 12)	# 125-136
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_430circlering_lv3', 1)
    GFX_0('DriveChargelightning', 0)
    Unknown23119(8421376, 10, 1)
    ScreenShake(6000, 0)
    sprite('mk430_12', 3)	# 137-139
    ScreenShake(8000, 0)
    sprite('mk430_13', 3)	# 140-142
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 3)	# 143-145	 **attackbox here**
    GFX_0('mk430cutin_lvG', -1)
    GFX_0('DriveLvG_PunchefD', 1)
    GFX_0('mkef_jumpsmoke23', 2)
    ScreenShake(0, 35000)
    callSubroutine('AfterImage_LvG')
    sprite('mk430_15', 3)	# 146-148	 **attackbox here**
    sprite('mk430_14', 3)	# 149-151	 **attackbox here**
    setInvincible(0)
    sprite('mk430_15', 3)	# 152-154	 **attackbox here**
    sprite('mk430_14', 3)	# 155-157	 **attackbox here**
    sprite('mk430_15', 3)	# 158-160	 **attackbox here**
    sprite('mk430_14', 4)	# 161-164	 **attackbox here**
    sprite('mk430_15', 4)	# 165-168	 **attackbox here**
    sprite('mk430_14', 5)	# 169-173	 **attackbox here**
    Unknown23119(0, 10, 1)
    sprite('mk430_15', 5)	# 174-178	 **attackbox here**
    sprite('mk430_16', 5)	# 179-183	 **attackbox here**
    sprite('mk430_17', 5)	# 184-188
    sprite('mk430_18', 5)	# 189-193
    sprite('mk430_19', 5)	# 194-198
    sprite('mk430_20', 5)	# 199-203

@State
def BurstDD():

    def upon_IMMEDIATE():
        Unknown17022('')
        Unknown11028(22)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(100)
        Unknown9142(80)
        Unknown11072(1, 150000, 0)
        PushbackX(60000)
        Unknown11069('BurstDDAdd')

        def upon_12():
            enterState('BurstDDAdd')
            Unknown23024(1)
            Unknown2017(0)

        def upon_61():
            PushbackX(39900)

        def upon_11():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            Unknown2062()
    sprite('mk431_09ex00', 4)	# 1-4
    SFX_1('mk280')
    setInvincible(1)
    Unknown1084(1)
    Unknown4004('427572737444446566660000000000000000000000000000000000000000000067000000')
    sprite('mk431_10ex00', 3)	# 5-7
    sprite('mk431_11ex00', 3)	# 8-10
    sprite('mk431_10ex00', 3)	# 11-13
    sprite('mk431_11ex00', 3)	# 14-16
    SFX_0('004_swing_grap_1_2')
    sprite('mk431_12ex00', 3)	# 17-19
    physicsXImpulse(40000)
    sprite('mk431_13ex00', 3)	# 20-22	 **attackbox here**
    Unknown1019(20)
    sprite('mk410_13ex00', 2)	# 23-24
    setInvincible(0)
    Unknown1084(1)
    sprite('mk410_14ex00', 3)	# 25-27
    sprite('mk410_15ex00', 3)	# 28-30
    sprite('mk410_16ex00', 3)	# 31-33
    sprite('mk410_17ex00', 3)	# 34-36
    sprite('mk410_18ex00', 3)	# 37-39
    sprite('mk410_19ex00', 3)	# 40-42

@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        Unknown17022('')
        Unknown11028(22)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(100)
        Unknown9142(80)
        Unknown11072(1, 150000, 0)
        PushbackX(60000)
        Unknown11069('BurstDDAdd')

        def upon_12():
            enterState('BurstDDAdd')
            Unknown23024(1)
            Unknown2017(0)

        def upon_61():
            PushbackX(39900)

        def upon_11():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            Unknown2062()
        if Unknown23145('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('mk431_09ex00', 2)	# 1-2
    SFX_1('mk280')
    setInvincible(1)
    Unknown1084(1)
    Unknown4004('427572737444446566660000000000000000000000000000000000000000000067000000')
    sprite('mk431_10ex00', 2)	# 3-4
    sprite('mk431_11ex00', 2)	# 5-6
    SFX_0('004_swing_grap_1_2')
    sprite('mk431_12ex00', 3)	# 7-9
    physicsXImpulse(40000)
    sprite('mk431_13ex00', 3)	# 10-12	 **attackbox here**
    Unknown1019(20)
    sprite('mk410_13ex00', 2)	# 13-14
    setInvincible(0)
    Unknown1084(1)
    sprite('mk410_14ex00', 3)	# 15-17
    sprite('mk410_15ex00', 3)	# 18-20
    sprite('mk410_16ex00', 3)	# 21-23
    sprite('mk410_17ex00', 3)	# 24-26
    sprite('mk410_18ex00', 3)	# 27-29
    sprite('mk410_19ex00', 3)	# 30-32

@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        Unknown17023('')
        AttackLevel_(5)
        Damage(800)
        AttackP2(100)
        Unknown9154(100)
        AirUntechableTime(100)
        YImpluseBeforeWallbounce(1500)
        Unknown9130(100)
        Unknown9142(80)
        Unknown9310(10)
        Unknown11056(0)
        Unknown11064(1)
        Unknown11043(0)
        Unknown11031(0)
        Unknown11091(0)
        Unknown11069('BurstDDAdd')

        def upon_STATE_END():
            Unknown26('BurstDD_Camera')
            Unknown2017(1)
            Unknown2053(1)
        Unknown2004(1, 0)
        Unknown23024(1)
    sprite('mk431_13ex00', 3)	# 1-3	 **attackbox here**
    Unknown23027()
    sprite('mk201_07ex00', 3)	# 4-6
    sprite('mk201_08ex00', 3)	# 7-9
    GFX_0('BurstDD_Camera', -1)
    sprite('mk201_09ex00', 3)	# 10-12
    sprite('mk023_00ex00', 2)	# 13-14
    sprite('mk023_01ex00', 2)	# 15-16
    sprite('mk440_00', 5)	# 17-21
    Unknown8001(3, 100)
    physicsXImpulse(20000)
    physicsYImpulse(15000)
    setGravity(1500)
    sprite('mk251_01ex00', 5)	# 22-26
    SFX_0('004_swing_grap_1_2')
    sprite('mk251_02ex00', 5)	# 27-31
    SFX_1('mk281')
    sprite('mk251_03ex00', 3)	# 32-34	 **attackbox here**
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    AirPushbackX(1000)
    AirPushbackY(60000)
    RefreshMultihit()
    Unknown1019(60)
    Unknown11023(1)
    sprite('mk251_04ex00', 2)	# 35-36
    Unknown11023(0)
    sprite('mk251_05ex00', 2)	# 37-38
    sprite('mk251_06ex00', 2)	# 39-40
    sprite('mk251_07ex00', 1)	# 41-41
    GFX_1('mkef_fakebunshin', 103)
    Unknown21012('427572737444445f43616d65726100000000000000000000000000000000000020000000')
    Unknown1084(1)
    sprite('mk402_00ex00', 3)	# 42-44
    teleportRelativeX(-100000)
    Unknown1007(1200000)
    physicsXImpulse(5000)
    physicsYImpulse(16000)
    setGravity(500)
    sprite('mk402_01ex00', 3)	# 45-47
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAuraAir', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk402_02ex00', 3)	# 48-50
    sprite('mk402_01ex00', 3)	# 51-53
    sprite('mk402_02ex00', 3)	# 54-56
    GFX_0('DriveChargelightning', 1)
    sprite('mk402_01ex00', 3)	# 57-59
    sprite('mk402_02ex00', 3)	# 60-62
    sprite('mk402_03ex00', 2)	# 63-64
    Unknown21012('447269766543686172676541757261416972000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    sprite('mk402_04ex00', 2)	# 65-66
    SFX_0('004_swing_grap_1_1')
    SFX_0('004_swing_grap_1_2')
    sprite('mk402_05ex00', 2)	# 67-68
    if SLOT_51:
        GFX_0('PowerDunkAirwallLvG', 0)
    else:
        GFX_0('PowerDunkAirwallLv3', 0)
    sprite('mk402_06ex00', 2)	# 69-70
    sprite('mk402_07ex00', 3)	# 71-73	 **attackbox here**
    SFX_3('mkse_03')
    if SLOT_51:
        GFX_0('DriveLvG_PunchefPowerDunk', 0)
    else:
        GFX_0('DriveLv3PunchefPowerDunk', 0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(-80000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown9118(40)
    if SLOT_51:
        Unknown9118(30)
    RefreshMultihit()
    sprite('mk402_08ex00', 1)	# 74-74
    GFX_1('mkef_fakebunshin', 103)
    Unknown21012('427572737444445f43616d65726100000000000000000000000000000000000021000000')
    if SLOT_51:
        _gotolabel(100)
    sprite('mk403_16ex00', 20)	# 75-94
    GFX_1('mkef_fakebunshin', 103)
    Unknown3032()
    Unknown3001(0)
    teleportRelativeX(-200000)
    teleportRelativeY(0)
    Unknown3029(0)
    Unknown1084(1)
    sprite('mk403_16ex00', 3)	# 95-97
    Unknown3004(14)
    sprite('mk403_17ex00', 3)	# 98-100
    sprite('mk403_18ex00', 3)	# 101-103
    sprite('mk403_19ex00', 2)	# 104-105
    GFX_0('mk440cutin', 0)
    sprite('mk412_00ex00', 3)	# 106-108
    sprite('mk412_01ex00', 3)	# 109-111
    Unknown3031()
    Unknown3001(255)
    Unknown3004(0)
    SFX_3('mkse_04')
    sprite('mk412_02ex00', 3)	# 112-114
    sprite('mk410_09ex00', 3)	# 115-117
    physicsXImpulse(5000)
    sprite('mk410_10ex00', 3)	# 118-120
    Unknown1019(200)
    sprite('mk410_11ex00', 3)	# 121-123
    SFX_0('004_swing_grap_1_1')
    Unknown1019(300)
    sprite('mk440_01', 1)	# 124-124	 **attackbox here**
    SFX_1('mk282')
    SFX_3('mkse_03')
    Unknown1019(0)
    Damage(900)
    Hitstop(26)
    ScreenShake(25000, 50000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(25000)
    AirPushbackY(32000)
    YImpluseBeforeWallbounce(2000)
    Unknown9191()
    Unknown9311()
    Unknown11064(0)
    RefreshMultihit()
    sprite('mk440_01', 2)	# 125-126	 **attackbox here**
    Unknown21012('427572737444445f43616d65726100000000000000000000000000000000000024000000')
    sprite('mk440_02', 8)	# 127-134
    sprite('mk410_14ex00', 8)	# 135-142
    sprite('mk410_15ex00', 8)	# 143-150
    sprite('mk410_16ex00', 8)	# 151-158
    sprite('mk410_17ex00', 7)	# 159-165
    sprite('mk410_18ex00', 7)	# 166-172
    sprite('mk410_19ex00', 7)	# 173-179
    ExitState()
    label(100)
    sprite('mk405_00ex00', 11)	# 180-190
    teleportRelativeX(100000)
    teleportRelativeY(0)
    Unknown1084(1)
    sprite('mk405_00ex00', 4)	# 191-194
    Unknown2017(0)
    Unknown2053(0)
    physicsXImpulse(40000)
    sprite('mk405_01ex00', 4)	# 195-198
    Unknown1019(80)
    sprite('mk405_02ex00', 3)	# 199-201
    Unknown1019(80)
    sprite('mk405_03ex00', 3)	# 202-204
    Unknown1019(80)
    sprite('mk403_08ex00', 4)	# 205-208
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    Unknown1019(80)
    sprite('mk403_09ex00', 4)	# 209-212
    Unknown1019(80)
    sprite('mk403_08ex00', 4)	# 213-216
    Unknown1019(80)
    sprite('mk403_10ex00', 2)	# 217-218
    GFX_0('BlockingPunchLv3_G', 2)
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    Unknown1019(-80)
    sprite('mk403_10ex00', 2)	# 219-220
    SFX_1('mk283')
    GFX_1('mkef_403speedline', 1)
    physicsXImpulse(-140000)
    Unknown2017(0)
    Unknown2015(40)
    sprite('mk403_11ex00', 3)	# 221-223	 **attackbox here**
    SFX_3('mkse_03')
    SFX_3('mkse_03')
    GFX_0('BlockingSpeedLine', -1)
    GFX_1('mkef_403smoke', -1)
    Unknown1019(80)
    Unknown11099(1)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(13000)
    AirPushbackY(42000)
    YImpluseBeforeWallbounce(1500)
    Hitstop(0)
    RefreshMultihit()
    sprite('mk403_11ex00', 3)	# 224-226	 **attackbox here**
    GFX_0('BlockingWind', 0)
    Unknown21012('427572737444445f43616d65726100000000000000000000000000000000000022000000')
    sprite('mk403_12ex00', 3)	# 227-229
    Unknown1019(80)
    sprite('mk403_13ex00', 3)	# 230-232
    Unknown1019(80)
    sprite('mk403_14ex00', 3)	# 233-235
    Unknown1019(80)
    sprite('mk403_15ex00', 3)	# 236-238
    Unknown1019(0)
    sprite('mk403_16ex00', 3)	# 239-241
    sprite('mk403_17ex00', 3)	# 242-244
    sprite('mk403_18ex00', 3)	# 245-247
    sprite('mk403_19ex00', 3)	# 248-250
    sprite('mk414_00ex00', 3)	# 251-253
    Unknown2017(1)
    Unknown2015(-1)
    sprite('mk414_01ex00', 3)	# 254-256
    sprite('mk414_02ex00', 3)	# 257-259
    sprite('mk414_03ex00', 3)	# 260-262
    GFX_0('mk440cutin_Active', 0)
    sprite('mk414_01ex00', 3)	# 263-265
    sprite('mk414_02ex00', 3)	# 266-268
    sprite('mk414_04ex00', 2)	# 269-270
    SFX_1('mk284')
    SFX_3('mkse_04')
    sprite('mk410_09ex00', 3)	# 271-273
    physicsXImpulse(5000)
    sprite('mk410_10ex00', 3)	# 274-276
    Unknown1019(200)
    sprite('mk410_11ex00', 3)	# 277-279
    SFX_0('004_swing_grap_1_1')
    Unknown1019(300)
    sprite('mk440_01', 3)	# 280-282	 **attackbox here**
    Unknown1019(0)
    Damage(1530)
    Unknown11099(0)
    Hitstop(15)
    ScreenShake(25000, 50000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(14000)
    AirPushbackY(38000)
    YImpluseBeforeWallbounce(2000)
    Unknown9191()
    RefreshMultihit()
    sprite('mk440_02', 4)	# 283-286
    sprite('mk410_14ex00', 4)	# 287-290
    sprite('mk410_15ex00', 3)	# 291-293
    GFX_0('mk440cutin_Active2', -1)
    sprite('mk408_02ex00', 3)	# 294-296
    sprite('mk440_03', 3)	# 297-299
    SFX_3('mkse_04')
    sprite('mk440_04', 2)	# 300-301
    sprite('mk440_05', 2)	# 302-303
    sprite('mk440_06', 2)	# 304-305
    sprite('mk440_07', 2)	# 306-307
    sprite('mk440_08', 3)	# 308-310
    sprite('mk440_09', 2)	# 311-312
    SFX_1('mk282')
    sprite('mk440_10', 1)	# 313-313	 **attackbox here**
    Hitstop(26)
    ScreenShake(100000, 100000)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    AirPushbackX(60000)
    AirPushbackY(10000)
    Unknown11064(0)
    RefreshMultihit()
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    Unknown21012('6d6b343430637574696e5f41637469766532000000000000000000000000000021000000')
    sprite('mk440_10', 8)	# 314-321	 **attackbox here**
    Unknown21012('427572737444445f43616d65726100000000000000000000000000000000000023000000')
    Unknown3029(0)
    sprite('mk440_11', 7)	# 322-328
    sprite('mk440_12', 7)	# 329-335
    sprite('mk440_13', 7)	# 336-342
    sprite('mk440_14', 7)	# 343-349
    sprite('mk440_15', 7)	# 350-356
    sprite('mk024_02ex00', 7)	# 357-363
    sprite('mk024_03ex00', 7)	# 364-370
    sprite('mk024_04ex00', 7)	# 371-377

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Hitstop(30)
        Unknown11064(1)
        Damage(0)
        Unknown9154(50)
        Unknown9015(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(220)
        Unknown9142(200)
        PushbackX(15000)
        Unknown11001(-6, 0, 0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11091(100)
        setInvincible(1)

        def upon_12():
            enterState('AstralHeatExe')
        Unknown23158('410000004b000000')
        GFX_0('DriveRing', 100)
        Unknown38(4, 1)
        Unknown23029(4, 1071, 0)
        callSubroutine('MakotoDriveSetting')
    sprite('mk450_00', 4)	# 1-4
    sprite('mk450_01', 4)	# 5-8
    tag_voice(1, 'bmk290_0', 'bmk290_1', '', '')
    Unknown2036(90, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_MK_AH', -1)
    Unknown20000(1)
    Unknown20003(0)
    Unknown20002(1)
    sprite('mk450_01', 3)	# 9-11
    sprite('mk450_02', 3)	# 12-14
    sprite('mk450_03', 3)	# 15-17
    sprite('mk450_04', 3)	# 18-20
    sprite('mk450_05', 3)	# 21-23
    sprite('mk450_06', 3)	# 24-26
    sprite('mk450_07', 4)	# 27-30
    GFX_0('mk450_energy', 0)
    GFX_0('mk450_tame', 0)
    sprite('mk450_08', 4)	# 31-34
    sprite('mk450_07', 4)	# 35-38
    sprite('mk450_08', 4)	# 39-42
    SLOT_55 = 1
    GFX_0('DriveChargeAura', 0)
    sprite('mk450_07', 4)	# 43-46
    sprite('mk450_08', 4)	# 47-50
    sprite('mk450_07', 4)	# 51-54
    sprite('mk450_08', 4)	# 55-58
    sprite('mk450_07', 4)	# 59-62
    sprite('mk450_08', 4)	# 63-66
    sprite('mk450_07', 4)	# 67-70
    sprite('mk450_08', 4)	# 71-74
    sprite('mk450_07', 4)	# 75-78
    sprite('mk450_08', 4)	# 79-82
    sprite('mk450_07', 4)	# 83-86
    sprite('mk450_08', 4)	# 87-90
    setInvincible(0)
    sprite('mk450_07', 4)	# 91-94
    sprite('mk450_08', 4)	# 95-98
    sprite('mk450_07', 4)	# 99-102
    sprite('mk450_08', 4)	# 103-106
    sprite('mk450_07', 4)	# 107-110
    sprite('mk450_08', 4)	# 111-114
    SLOT_55 = 0
    loopRest()
    label(1)
    sprite('mk450_07', 4)	# 115-118
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    Unknown20000(0)
    sprite('mk450_08', 4)	# 119-122
    sprite('mk450_07', 4)	# 123-126
    sprite('mk450_08', 4)	# 127-130
    sprite('mk450_07', 4)	# 131-134
    sprite('mk450_08', 4)	# 135-138
    sprite('mk450_07', 4)	# 139-142
    sprite('mk450_08', 4)	# 143-146
    sprite('mk450_07', 4)	# 147-150
    sprite('mk450_08', 4)	# 151-154
    sprite('mk450_09', 4)	# 155-158
    Unknown7015()
    SFX_3('mkse_18')
    Unknown4045('6d6b65665f6a756d70736d6f6b6532000000000000000000000000000000000000000000')
    Unknown21015('6d6b3435305f74616d65000000000000000000000000000000000000000000003004000000000000')
    SLOT_52 = 1
    sprite('mk450_10', 4)	# 159-162
    GFX_0('mk450_syogeki', 0)
    physicsXImpulse(20000)

    def upon_3():
        (SLOT_19 < 300000)
        if op(5, 2, 0, 2, 52):
            clearUponHandler(3)
            sendToLabel(50)
    sprite('mk450_11', 2)	# 163-164
    sprite('mk450_10', 2)	# 165-166
    sprite('mk450_11', 2)	# 167-168
    sprite('mk450_10', 2)	# 169-170
    setInvincible(0)
    sprite('mk450_11', 2)	# 171-172
    sprite('mk450_10', 2)	# 173-174
    sprite('mk450_11', 2)	# 175-176
    sprite('mk032_09', 3)	# 177-179
    SLOT_52 = 0
    sprite('mk032_10', 3)	# 180-182
    loopRest()
    ExitState()
    label(50)
    sprite('mk450_12', 4)	# 183-186
    sprite('mk450_13', 4)	# 187-190	 **attackbox here**
    GFX_0('mk450_impact', 0)
    Unknown1084(1)
    sprite('mk450_14', 4)	# 191-194
    setInvincible(0)
    sprite('mk450_15', 4)	# 195-198
    sprite('mk450_45', 4)	# 199-202
    Unknown21015('6d6b3435305f696d7061637400000000000000000000000000000000000000003104000000000000')
    sprite('mk450_46', 4)	# 203-206
    sprite('mk450_47', 4)	# 207-210
    sprite('mk450_48', 4)	# 211-214
    sprite('mk450_49', 4)	# 215-218
    loopRest()
    ExitState()
    label(2)
    sprite('mk450_07', 4)	# 219-222
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    Unknown20000(0)
    sprite('mk450_08', 4)	# 223-226
    sprite('mk450_07', 4)	# 227-230
    sprite('mk450_08', 4)	# 231-234
    sprite('mk450_07', 4)	# 235-238
    sprite('mk450_09', 4)	# 239-242
    Unknown7015()
    SFX_3('mkse_18')
    Unknown21015('6d6b3435305f74616d65000000000000000000000000000000000000000000003004000000000000')
    SLOT_52 = 1
    sprite('mk450_10', 2)	# 243-244
    GFX_0('mk450_syogeki', 0)
    physicsXImpulse(35000)

    def upon_3():
        (SLOT_19 < 300000)
        if op(5, 2, 0, 2, 52):
            clearUponHandler(3)
            sendToLabel(51)
    sprite('mk450_11', 2)	# 245-246
    sprite('mk450_10', 2)	# 247-248
    sprite('mk450_11', 2)	# 249-250
    sprite('mk450_10', 2)	# 251-252
    sprite('mk450_11', 2)	# 253-254
    setInvincible(0)
    sprite('mk450_10', 2)	# 255-256
    sprite('mk450_11', 2)	# 257-258
    sprite('mk032_09', 3)	# 259-261
    SLOT_52 = 0
    sprite('mk032_10', 3)	# 262-264
    loopRest()
    ExitState()
    label(51)
    sprite('mk450_12', 4)	# 265-268
    sprite('mk450_13', 4)	# 269-272	 **attackbox here**
    GFX_0('mk450_impact', 0)
    ScreenShake(60000, 0)
    Unknown1084(1)
    sprite('mk450_14', 4)	# 273-276
    setInvincible(0)
    sprite('mk450_15', 4)	# 277-280
    sprite('mk450_45', 4)	# 281-284
    Unknown21015('6d6b3435305f696d7061637400000000000000000000000000000000000000003104000000000000')
    sprite('mk450_46', 4)	# 285-288
    sprite('mk450_47', 4)	# 289-292
    sprite('mk450_48', 4)	# 293-296
    sprite('mk450_49', 4)	# 297-300
    loopRest()
    ExitState()
    label(3)
    FatalCounter(1)
    sprite('mk450_07', 4)	# 301-304
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    Unknown20000(0)
    sprite('mk450_08', 4)	# 305-308
    sprite('mk450_07', 4)	# 309-312
    sprite('mk450_09', 4)	# 313-316
    Unknown7015()
    SFX_3('mkse_18')
    Unknown21012('6d6b3435305f74616d650000000000000000000000000000000000000000000020000000')
    SLOT_52 = 1
    sprite('mk450_10', 2)	# 317-318
    GFX_0('mk450_syogeki', 0)
    physicsXImpulse(50000)

    def upon_3():
        (SLOT_19 < 300000)
        if op(5, 2, 0, 2, 52):
            clearUponHandler(3)
            sendToLabel(52)
    sprite('mk450_11', 2)	# 319-320
    sprite('mk450_10', 2)	# 321-322
    sprite('mk450_11', 2)	# 323-324
    sprite('mk450_10', 2)	# 325-326
    sprite('mk450_11', 2)	# 327-328
    sprite('mk450_10', 2)	# 329-330
    setInvincible(0)
    sprite('mk450_11', 2)	# 331-332
    sprite('mk032_09', 3)	# 333-335
    SLOT_52 = 0
    sprite('mk032_10', 3)	# 336-338
    loopRest()
    ExitState()
    label(4)
    FatalCounter(1)
    sprite('mk450_07', 4)	# 339-342
    sprite('mk450_08', 4)	# 343-346
    sprite('mk450_07', 4)	# 347-350
    sprite('mk450_08', 4)	# 351-354
    sprite('mk450_07', 4)	# 355-358
    sprite('mk450_08', 4)	# 359-362
    sprite('mk450_07', 4)	# 363-366
    sprite('mk450_08', 4)	# 367-370
    sprite('mk450_07', 4)	# 371-374
    Unknown21015('4472697665436861726765417572610000000000000000000000000000000000fd03000000000000')
    Unknown20000(0)
    sprite('mk450_08', 4)	# 375-378
    sprite('mk450_07', 4)	# 379-382
    sprite('mk450_08', 4)	# 383-386
    sprite('mk450_09', 4)	# 387-390
    Unknown7015()
    SFX_3('mkse_18')
    Unknown21015('6d6b3435305f74616d65000000000000000000000000000000000000000000003004000000000000')
    SLOT_52 = 1
    sprite('mk450_10', 2)	# 391-392
    GFX_0('mk450_syogeki', 0)
    physicsXImpulse(50000)

    def upon_3():
        (SLOT_19 < 300000)
        if op(5, 2, 0, 2, 52):
            clearUponHandler(3)
            sendToLabel(52)
    sprite('mk450_11', 2)	# 393-394
    sprite('mk450_10', 2)	# 395-396
    sprite('mk450_11', 2)	# 397-398
    sprite('mk450_10', 2)	# 399-400
    sprite('mk450_11', 2)	# 401-402
    sprite('mk450_10', 2)	# 403-404
    setInvincible(0)
    sprite('mk450_11', 2)	# 405-406
    sprite('mk032_09', 3)	# 407-409
    SLOT_52 = 0
    sprite('mk032_10', 3)	# 410-412
    loopRest()
    ExitState()
    label(52)
    sprite('mk450_12', 4)	# 413-416
    sprite('mk450_13', 4)	# 417-420	 **attackbox here**
    GFX_0('mk450_impact', 0)
    ScreenShake(80000, 0)
    Unknown1084(1)
    sprite('mk450_14', 4)	# 421-424
    setInvincible(0)
    sprite('mk450_15', 4)	# 425-428
    sprite('mk450_45', 4)	# 429-432
    Unknown21015('6d6b3435305f696d7061637400000000000000000000000000000000000000003104000000000000')
    sprite('mk450_46', 4)	# 433-436
    sprite('mk450_47', 4)	# 437-440
    sprite('mk450_48', 4)	# 441-444
    sprite('mk450_49', 4)	# 445-448
    loopRest()
    ExitState()

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        Unknown11069('AstralHeatExe')
        Unknown23088(1, 1)
        Unknown23157(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)
        Unknown2006()
        Unknown23084(1)
        AttackLevel_(3)
        Damage(300)
    sprite('mk450_15', 4)	# 1-4
    GFX_0('mk450_bunsan', 0)
    sprite('mk450_16', 4)	# 5-8
    sprite('mk450_17', 4)	# 9-12
    GFX_0('mk450_bgef', -1)
    sprite('mk450_18', 4)	# 13-16
    sprite('mk450_19', 4)	# 17-20
    tag_voice(0, 'bmk291_0', 'bmk291_1', '', '')
    sprite('mk450_20', 4)	# 21-24
    GFX_0('mk450_footef', 0)
    sprite('mk450_21', 2)	# 25-26	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    Unknown11048(20)
    PushbackX(2500)
    Unknown9154(300)
    Hitstop(1)
    RefreshMultihit()
    ScreenShake(0, 20000)
    GFX_0('mk450_hibana', -1)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_22', 2)	# 27-28	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23', 2)	# 29-30	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex00', 2)	# 31-32	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    ScreenShake(0, 20000)
    sprite('mk450_23ex01', 2)	# 33-34	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex02', 2)	# 35-36	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex03', 2)	# 37-38	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex04', 2)	# 39-40	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    ScreenShake(0, 20000)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_23ex05', 2)	# 41-42	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex06', 2)	# 43-44	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex07', 2)	# 45-46	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex08', 2)	# 47-48	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    ScreenShake(0, 20000)
    sprite('mk450_23ex09', 2)	# 49-50	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex10', 2)	# 51-52	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex11', 2)	# 53-54	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    GFX_0('mk450_footef', 0)
    sprite('mk450_23ex12', 2)	# 55-56	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    ScreenShake(0, 20000)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_23ex13', 2)	# 57-58	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex14', 2)	# 59-60	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(-2500)
    RefreshMultihit()
    sprite('mk450_23ex15', 2)	# 61-62	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(-2500)
    RefreshMultihit()
    sprite('mk450_23ex16', 2)	# 63-64	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    RefreshMultihit()
    ScreenShake(0, 20000)
    sprite('mk450_23ex17', 2)	# 65-66	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex18', 2)	# 67-68	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(-2500)
    RefreshMultihit()
    sprite('mk450_23ex19', 2)	# 69-70	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(-2500)
    RefreshMultihit()
    sprite('mk450_23ex20', 2)	# 71-72	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    RefreshMultihit()
    ScreenShake(0, 20000)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_23ex21', 2)	# 73-74	 **attackbox here**
    tag_voice(0, 'bmk292_0', 'bmk292_1', '', '')
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex22', 2)	# 75-76	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(-2500)
    RefreshMultihit()
    sprite('mk450_23ex23', 2)	# 77-78	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(-2500)
    RefreshMultihit()
    sprite('mk450_23ex24', 2)	# 79-80	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    RefreshMultihit()
    ScreenShake(0, 20000)
    sprite('mk450_23ex01', 2)	# 81-82	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex02', 2)	# 83-84	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex03', 2)	# 85-86	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex04', 2)	# 87-88	 **attackbox here**
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(2500)
    RefreshMultihit()
    ScreenShake(0, 20000)
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_23ex05', 2)	# 89-90	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    sprite('mk450_23ex06', 2)	# 91-92	 **attackbox here**
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    RefreshMultihit()
    Unknown11069('AstralHeatKillObject')
    sprite('mk450_24', 6)	# 93-98
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_25', 6)	# 99-104
    sprite('mk450_26', 6)	# 105-110
    GFX_1('mkef_450bgmc', -1)
    sprite('mk450_27', 6)	# 111-116
    sprite('mk450_28', 6)	# 117-122
    GFX_0('mk450cutin_tame', -1)
    sprite('mk450_29', 6)	# 123-128
    sprite('mk450_30', 7)	# 129-135
    sprite('mk450_31', 16)	# 136-151
    sprite('mk450_31', 4)	# 152-155
    sprite('null', 4)	# 156-159
    Unknown36(22)
    Unknown3038(1)
    teleportRelativeY(40000000)
    setGravity(0)
    Unknown35()
    GFX_0('mk450cutin_impact', -1)
    GFX_0('mk450cutin_impact_small', -1)
    GFX_1('mkef_450star', -1)
    ScreenShake(0, 50000)
    sprite('null', 40)	# 160-199
    tag_voice(0, 'bmk293_0', 'bmk293_1', '', '')
    SFX_0('016_explode_1')
    SFX_0('016_explode_1')
    sprite('null', 36)	# 200-235
    SFX_3('mkse_14')
    SFX_3('mkse_14')
    sprite('null', 8)	# 236-243
    GFX_0('AstWhite', -1)
    sprite('null', 15)	# 244-258
    Unknown20001(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown23024(3)
    Unknown1000(0)
    sprite('null', 12)	# 259-270
    sprite('null', 58)	# 271-328
    SFX_3('mkse_11')
    SFX_3('mkse_11')
    sprite('null', 7)	# 329-335
    GFX_0('bmk_AH_ray', -1)
    sprite('vrmkef450dmy01', 1)	# 336-336	 **attackbox here**
    ScreenShake(0, 300000)
    Unknown23027()
    GFX_0('AstralHeatKillObject', -1)
    SFX_3('mkse_12')
    SFX_3('mkse_12')
    sprite('null', 193)	# 337-529
    sprite('null', 15)	# 530-544
    Unknown23024(0)
    sprite('mk450_32', 15)	# 545-559
    Unknown3001(255)
    teleportRelativeY(0)
    Unknown1000(0)
    sprite('mk450_33', 4)	# 560-563
    SFX_3('mkse_07')
    sprite('mk450_33', 4)	# 564-567
    sprite('mk450_32', 4)	# 568-571
    sprite('mk450_33', 4)	# 572-575
    sprite('mk450_32', 4)	# 576-579
    Unknown4045('6d6b3435305f6b616d69667562756b6900000000000000000000000000000000ffffffff')
    Unknown4054(4)
    Unknown4045('6d6b3435305f6b616d69667562756b6966726f6e740000000000000000000000ffffffff')
    sprite('mk450_33', 4)	# 580-583
    sprite('mk450_32', 4)	# 584-587
    sprite('mk450_33', 4)	# 588-591
    sprite('mk450_34', 4)	# 592-595
    sprite('mk450_35', 4)	# 596-599
    Unknown18010()
    Unknown21011(180)
    sprite('mk450_36', 4)	# 600-603
    sprite('mk450_37', 4)	# 604-607
    sprite('mk450_38', 6)	# 608-613
    sprite('mk450_39', 3)	# 614-616
    sprite('mk450_40', 6)	# 617-622
    sprite('mk450_41', 6)	# 623-628
    tag_voice(0, 'bmk294_0', 'bmk294_1', '', '')
    sprite('mk450_42', 6)	# 629-634
    sprite('mk450_43', 6)	# 635-640
    sprite('mk450_44', 100)	# 641-740
    sprite('mk450_44', 140)	# 741-880
    SFX_3('mkse_09')
    sprite('mk450_44', 140)	# 881-1020
    SFX_3('mkse_09')
    sprite('mk450_44', 140)	# 1021-1160
    SFX_3('mkse_09')
    sprite('mk450_44', 32767)	# 1161-33927

@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBOunce_()
        Unknown2017(0)

        def upon_14():
            SFX_1('mk054')
    sprite('mk900_00', 8)	# 1-8	 **attackbox here**
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
    GFX_0('RLAstLockmc', 0)
    GFX_0('RLAstLockAura', 0)
    sprite('mk900_01', 8)	# 9-16	 **attackbox here**
    sprite('mk900_02', 8)	# 17-24	 **attackbox here**
    label(0)
    sprite('mk900_00', 8)	# 25-32	 **attackbox here**
    sprite('mk900_01', 8)	# 33-40	 **attackbox here**
    sprite('mk900_02', 8)	# 41-48	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBOunce_()
        Unknown2017(0)
        teleportRelativeY(220000)
    sprite('mk901_00', 50)	# 1-50
    physicsYImpulse(-150)
    sprite('mk901_00', 50)	# 51-100
    physicsYImpulse(150)
    SFX_1('mk055')
    label(0)
    sprite('mk901_00', 50)	# 101-150
    physicsYImpulse(-150)
    sprite('mk901_00', 50)	# 151-200
    physicsYImpulse(150)
    gotoLabel(0)

@Subroutine
def MouthTableInit():
    Unknown18011('bmk000', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk500', 14179, 14177, 14179, 14177, 14179, 14433, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk501', 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk502', 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk503', 12643, 14641, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk505', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk520', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk521', 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk522', 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk523', 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk524', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 14132, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk403_0', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk403_1', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk601biz', 12643, 14177, 12643, 24880, 12338, 13411, 24887, 12338, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk600bma', 12643, 13153, 25392, 24887, 12339, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 14131, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk600bno', 12643, 12641, 25394, 24887, 25399, 24887, 14129, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk601btg', 12643, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk601pak', 12643, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk600pce', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 12337, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk600pyo', 12643, 12897, 25392, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk601rwi', 12643, 14177, 12899, 24882, 25399, 24887, 12340, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk600uca', 12643, 14177, 14179, 12897, 25392, 14130, 12641, 25392, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk600ugo', 12643, 12897, 25396, 24887, 12849, 13667, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700biz', 12643, 14177, 12643, 24882, 25399, 24887, 12339, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700bma', 12643, 14177, 14179, 13409, 25392, 12340, 14177, 14179, 14177, 12899, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700bno', 12643, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24882, 25397, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700btg', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700pak', 12643, 14177, 12643, 24884, 25399, 24887, 25399, 24887, 13618, 13411, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk701pyo', 12643, 12641, 25394, 24887, 25399, 24887, 12849, 14179, 12897, 25392, 14130, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700rwi', 12643, 14177, 12899, 24887, 12338, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk702rwi', 12643, 14177, 13155, 24887, 13625, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700uca', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk700ugo', 12643, 14177, 14179, 13409, 25397, 13620, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk702pce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bmk703pce', 12643, 14177, 14179, 14177, 12643, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('btg')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('biz')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('bma')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    if random_(2, 0, 50):
        gotoLabel(10)
    sprite('mk600_00', 6)	# 2-7
    if random_(2, 0, 50):
        SLOT_51 = (SLOT_51 + 1)
    else:
        SLOT_2 = (SLOT_2 + 1)
    sprite('mk600_00', 35)	# 8-42
    if SLOT_51:
        SFX_1('bmk500')
    sprite('mk600_00', 20)	# 43-62
    sprite('mk600_00', 15)	# 63-77
    if SLOT_2:
        sendToLabel(1)
    label(1)
    sprite('mk600_01', 9)	# 78-86
    sprite('mk600_02', 6)	# 87-92
    sprite('mk600_03', 6)	# 93-98
    sprite('mk600_04', 6)	# 99-104
    sprite('mk600_05', 6)	# 105-110
    sprite('mk600_06', 6)	# 111-116
    sprite('mk600_07', 6)	# 117-122
    sprite('mk600_08', 6)	# 123-128
    SFX_0('019_cloth_b')
    sprite('mk600_09', 6)	# 129-134
    sprite('mk600_10', 6)	# 135-140
    if SLOT_2:
        SFX_1('bmk503')
    GFX_0('EntryMant', 0)
    Unknown21007(24, 41)
    sprite('mk600_11', 6)	# 141-146
    sprite('mk600_12', 6)	# 147-152
    sprite('mk600_13', 6)	# 153-158
    sprite('mk600_14', 6)	# 159-164
    sprite('mk600_15', 6)	# 165-170
    sprite('mk600_16', 6)	# 171-176
    Unknown23018(1)
    label(2)
    sprite('mk000_00', 5)	# 177-181
    sprite('mk000_01', 5)	# 182-186
    sprite('mk000_02', 6)	# 187-192
    sprite('mk000_03', 6)	# 193-198
    sprite('mk000_04', 5)	# 199-203
    sprite('mk000_05', 5)	# 204-208
    sprite('mk000_06', 6)	# 209-214
    sprite('mk000_07', 6)	# 215-220
    sprite('mk000_08', 5)	# 221-225
    sprite('mk000_09', 5)	# 226-230
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('mk601_00', 6)	# 231-236
    sprite('mk601_01', 6)	# 237-242
    sprite('mk601_02', 4)	# 243-246
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    sprite('mk601_03', 6)	# 247-252
    sprite('mk601_04', 6)	# 253-258
    sprite('mk601_05', 6)	# 259-264
    sprite('mk601_06', 6)	# 265-270
    sprite('mk601_07', 4)	# 271-274
    SFX_0('008_swing_pole_0')
    sprite('mk601_08', 4)	# 275-278
    sprite('mk601_09', 4)	# 279-282
    SFX_0('008_swing_pole_0')
    sprite('mk601_10', 4)	# 283-286
    sprite('mk601_11', 8)	# 287-294
    SFX_0('008_swing_pole_1')
    sprite('mk601_12', 6)	# 295-300
    Unknown7006('bmk501', 100, 896232802, 12848, 0, 0, 100, 0, 0, 0, 0, 0, 896232802, 13616, 0, 0, 100)
    Unknown21007(24, 41)
    label(11)
    sprite('mk601_13', 8)	# 301-308
    if SLOT_97:
        _gotolabel(11)
    sprite('mk601_13', 30)	# 309-338
    sprite('mk601_13', 5)	# 339-343
    label(12)
    sprite('mk601_13', 8)	# 344-351
    if SLOT_97:
        _gotolabel(12)
    sprite('mk601_14', 6)	# 352-357
    sprite('mk601_15', 6)	# 358-363
    Unknown23018(1)
    loopRest()
    ExitState()
    label(20)
    sprite('mk602_00', 5)	# 364-368
    loopRest()
    if SLOT_17:
        _gotolabel(20)
    sprite('mk602_00', 120)	# 369-488
    SFX_1('mk416')
    label(21)
    sprite('mk602_00', 5)	# 489-493
    if SLOT_97:
        _gotolabel(21)
    sprite('mk602_03', 120)	# 494-613
    sprite('mk602_04', 8)	# 614-621
    sprite('mk602_05', 60)	# 622-681
    SFX_1('mk417')
    sprite('mk602_01', 8)	# 682-689
    sprite('mk602_02', 8)	# 690-697
    Unknown21011(60)
    loopRest()
    ExitState()
    label(30)
    sprite('mk611_09', 6)	# 698-703	 **attackbox here**
    SFX_1('bmk700pak')
    label(31)
    sprite('mk611_09', 6)	# 704-709	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 710-715	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 716-721	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 722-727	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 728-733	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 734-739	 **attackbox here**
    gotoLabel(31)
    label(100)
    sprite('mk615_00', 6)	# 740-745
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown2037(3)
    sprite('mk615_01', 1)	# 746-746
    SFX_1('bmk600bno')
    label(101)
    sprite('mk615_01', 6)	# 747-752
    sprite('mk615_02', 6)	# 753-758
    sprite('mk615_03', 6)	# 759-764
    sprite('mk615_04', 6)	# 765-770
    sprite('mk615_05', 6)	# 771-776
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(101)
    sprite('mk615_06', 6)	# 777-782
    sprite('mk615_07', 7)	# 783-789
    sprite('mk615_08', 10)	# 790-799
    sprite('mk615_09', 5)	# 800-804
    sprite('mk615_10', 5)	# 805-809
    sprite('mk615_11', 6)	# 810-815
    sprite('mk615_12', 6)	# 816-821
    label(102)
    sprite('mk615_13', 1)	# 822-822
    if SLOT_97:
        _gotolabel(102)
    sprite('mk615_13', 50)	# 823-872
    sprite('mk615_13', 32767)	# 873-33639
    Unknown21007(24, 40)
    Unknown23018(1)
    ExitState()
    label(110)
    sprite('mk600_00', 32767)	# 33640-66406
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-1000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(111)
    label(111)
    sprite('mk600_00', 70)	# 66407-66476
    SFX_1('bmk601btg')
    sprite('mk600_01', 9)	# 66477-66485
    sprite('mk600_02', 6)	# 66486-66491
    sprite('mk600_03', 6)	# 66492-66497
    sprite('mk600_04', 6)	# 66498-66503
    sprite('mk600_05', 6)	# 66504-66509
    sprite('mk600_06', 6)	# 66510-66515
    sprite('mk600_07', 6)	# 66516-66521
    sprite('mk600_08', 6)	# 66522-66527
    SFX_0('019_cloth_b')
    sprite('mk600_09', 6)	# 66528-66533
    sprite('mk600_10', 6)	# 66534-66539
    GFX_0('EntryMant', 0)
    sprite('mk600_11', 6)	# 66540-66545
    sprite('mk600_12', 6)	# 66546-66551
    sprite('mk600_13', 6)	# 66552-66557
    sprite('mk600_14', 6)	# 66558-66563
    sprite('mk600_15', 6)	# 66564-66569
    sprite('mk600_16', 6)	# 66570-66575
    Unknown23018(1)
    label(112)
    sprite('mk000_00', 5)	# 66576-66580
    sprite('mk000_01', 5)	# 66581-66585
    sprite('mk000_02', 6)	# 66586-66591
    sprite('mk000_03', 6)	# 66592-66597
    sprite('mk000_04', 5)	# 66598-66602
    sprite('mk000_05', 5)	# 66603-66607
    sprite('mk000_06', 6)	# 66608-66613
    Unknown21007(24, 40)
    sprite('mk000_07', 6)	# 66614-66619
    sprite('mk000_08', 5)	# 66620-66624
    sprite('mk000_09', 5)	# 66625-66629
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('mk601_00', 6)	# 66630-66635
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('mk601_01', 6)	# 66636-66641
    sprite('mk601_02', 4)	# 66642-66645
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    sprite('mk601_03', 6)	# 66646-66651
    sprite('mk601_04', 6)	# 66652-66657
    sprite('mk601_05', 6)	# 66658-66663
    sprite('mk601_06', 6)	# 66664-66669
    sprite('mk601_07', 4)	# 66670-66673
    SFX_0('008_swing_pole_0')
    sprite('mk601_08', 4)	# 66674-66677
    sprite('mk601_09', 4)	# 66678-66681
    SFX_0('008_swing_pole_0')
    sprite('mk601_10', 4)	# 66682-66685
    sprite('mk601_11', 8)	# 66686-66693
    SFX_0('008_swing_pole_1')
    sprite('mk601_12', 6)	# 66694-66699
    SFX_1('bmk600pyo')
    label(121)
    sprite('mk601_13', 1)	# 66700-66700
    if SLOT_97:
        _gotolabel(121)
    sprite('mk601_13', 30)	# 66701-66730
    sprite('mk601_13', 8)	# 66731-66738
    sprite('mk601_14', 6)	# 66739-66744
    sprite('mk601_15', 6)	# 66745-66750
    Unknown21007(24, 40)
    Unknown23018(1)
    label(122)
    sprite('mk000_00', 5)	# 66751-66755
    sprite('mk000_01', 5)	# 66756-66760
    sprite('mk000_02', 6)	# 66761-66766
    sprite('mk000_03', 6)	# 66767-66772
    sprite('mk000_04', 5)	# 66773-66777
    sprite('mk000_05', 5)	# 66778-66782
    sprite('mk000_06', 6)	# 66783-66788
    sprite('mk000_07', 6)	# 66789-66794
    sprite('mk000_08', 5)	# 66795-66799
    sprite('mk000_09', 5)	# 66800-66804
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('mk000_00', 1)	# 66805-66805
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bmk600pce')
    label(131)
    sprite('mk000_00', 5)	# 66806-66810
    sprite('mk000_01', 5)	# 66811-66815
    sprite('mk000_02', 6)	# 66816-66821
    sprite('mk000_03', 6)	# 66822-66827
    sprite('mk000_04', 5)	# 66828-66832
    sprite('mk000_05', 5)	# 66833-66837
    sprite('mk000_06', 6)	# 66838-66843
    sprite('mk000_07', 6)	# 66844-66849
    sprite('mk000_08', 5)	# 66850-66854
    sprite('mk000_09', 5)	# 66855-66859
    if SLOT_97:
        _gotolabel(131)
    sprite('mk000_00', 5)	# 66860-66864
    sprite('mk000_01', 5)	# 66865-66869
    sprite('mk000_02', 6)	# 66870-66875
    sprite('mk000_03', 6)	# 66876-66881
    sprite('mk000_04', 5)	# 66882-66886
    sprite('mk331_00', 6)	# 66887-66892
    sprite('mk331_01', 6)	# 66893-66898
    sprite('mk331_04', 6)	# 66899-66904
    sprite('mk331_05', 6)	# 66905-66910
    Unknown2037(5)
    Unknown21011(180)
    label(132)
    sprite('mk331_06', 6)	# 66911-66916
    sprite('mk331_07', 6)	# 66917-66922
    sprite('mk331_08', 6)	# 66923-66928
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(132)
    label(133)
    sprite('mk331_06', 6)	# 66929-66934
    Unknown21007(24, 40)
    sprite('mk331_07', 6)	# 66935-66940
    sprite('mk331_08', 6)	# 66941-66946
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('mk600_00', 120)	# 66947-67066
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bmk600ugo')
    sprite('mk600_01', 9)	# 67067-67075
    sprite('mk600_02', 6)	# 67076-67081
    sprite('mk600_03', 6)	# 67082-67087
    sprite('mk600_04', 6)	# 67088-67093
    sprite('mk600_05', 6)	# 67094-67099
    sprite('mk600_06', 6)	# 67100-67105
    sprite('mk600_07', 6)	# 67106-67111
    sprite('mk600_08', 6)	# 67112-67117
    SFX_0('019_cloth_b')
    sprite('mk600_09', 6)	# 67118-67123
    sprite('mk600_10', 6)	# 67124-67129
    GFX_0('EntryMant', 0)
    sprite('mk600_11', 6)	# 67130-67135
    sprite('mk600_12', 6)	# 67136-67141
    sprite('mk600_13', 6)	# 67142-67147
    sprite('mk600_14', 6)	# 67148-67153
    sprite('mk600_15', 6)	# 67154-67159
    sprite('mk600_16', 6)	# 67160-67165
    Unknown21007(24, 40)
    Unknown23018(1)
    label(141)
    sprite('mk000_00', 5)	# 67166-67170
    sprite('mk000_01', 5)	# 67171-67175
    sprite('mk000_02', 6)	# 67176-67181
    sprite('mk000_03', 6)	# 67182-67187
    sprite('mk000_04', 5)	# 67188-67192
    sprite('mk000_05', 5)	# 67193-67197
    sprite('mk000_06', 6)	# 67198-67203
    sprite('mk000_07', 6)	# 67204-67209
    sprite('mk000_08', 5)	# 67210-67214
    sprite('mk000_09', 5)	# 67215-67219
    gotoLabel(141)
    ExitState()
    label(150)
    sprite('mk602_00', 32767)	# 67220-99986
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(151)
    label(151)
    sprite('mk602_00', 1)	# 99987-99987
    SFX_1('bmk601rwi')
    label(152)
    sprite('mk602_00', 1)	# 99988-99988
    if SLOT_97:
        _gotolabel(152)
    sprite('mk602_00', 60)	# 99989-100048
    sprite('mk602_04', 8)	# 100049-100056
    sprite('mk602_05', 32767)	# 100057-132823
    Unknown23018(1)
    ExitState()
    label(160)
    sprite('mk601_00', 6)	# 132824-132829
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('mk601_01', 6)	# 132830-132835
    sprite('mk601_02', 4)	# 132836-132839
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    sprite('mk601_03', 6)	# 132840-132845
    sprite('mk601_04', 6)	# 132846-132851
    sprite('mk601_05', 6)	# 132852-132857
    sprite('mk601_06', 6)	# 132858-132863
    sprite('mk601_07', 4)	# 132864-132867
    SFX_0('008_swing_pole_0')
    sprite('mk601_08', 4)	# 132868-132871
    sprite('mk601_09', 4)	# 132872-132875
    SFX_0('008_swing_pole_0')
    sprite('mk601_10', 4)	# 132876-132879
    sprite('mk601_11', 8)	# 132880-132887
    SFX_0('008_swing_pole_1')
    sprite('mk601_12', 6)	# 132888-132893
    SFX_1('bmk600uca')
    label(161)
    sprite('mk601_13', 1)	# 132894-132894
    if SLOT_97:
        _gotolabel(161)
    sprite('mk601_13', 30)	# 132895-132924
    sprite('mk601_13', 8)	# 132925-132932
    sprite('mk601_14', 6)	# 132933-132938
    sprite('mk601_15', 6)	# 132939-132944
    Unknown21007(24, 40)
    Unknown21011(300)
    label(162)
    sprite('mk000_00', 5)	# 132945-132949
    sprite('mk000_01', 5)	# 132950-132954
    sprite('mk000_02', 6)	# 132955-132960
    sprite('mk000_03', 6)	# 132961-132966
    sprite('mk000_04', 5)	# 132967-132971
    sprite('mk000_05', 5)	# 132972-132976
    sprite('mk000_06', 6)	# 132977-132982
    sprite('mk000_07', 6)	# 132983-132988
    sprite('mk000_08', 5)	# 132989-132993
    sprite('mk000_09', 5)	# 132994-132998
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('mk000_00', 1)	# 132999-132999
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('mk000_00', 5)	# 133000-133004
    sprite('mk000_01', 5)	# 133005-133009
    sprite('mk000_02', 6)	# 133010-133015
    sprite('mk000_03', 6)	# 133016-133021
    sprite('mk000_04', 5)	# 133022-133026
    sprite('mk000_05', 5)	# 133027-133031
    sprite('mk000_06', 6)	# 133032-133037
    sprite('mk000_07', 6)	# 133038-133043
    sprite('mk000_08', 5)	# 133044-133048
    sprite('mk000_09', 5)	# 133049-133053
    gotoLabel(171)
    label(172)
    sprite('mk615_00', 6)	# 133054-133059
    sprite('mk615_01', 6)	# 133060-133065
    SFX_1('bmk601biz')
    sprite('mk615_02', 6)	# 133066-133071
    sprite('mk615_03', 6)	# 133072-133077
    sprite('mk615_04', 6)	# 133078-133083
    sprite('mk615_05', 6)	# 133084-133089
    sprite('mk615_06', 6)	# 133090-133095
    sprite('mk615_07', 7)	# 133096-133102
    sprite('mk615_08', 10)	# 133103-133112
    sprite('mk615_09', 5)	# 133113-133117
    sprite('mk615_10', 5)	# 133118-133122
    sprite('mk615_11', 6)	# 133123-133128
    sprite('mk615_12', 6)	# 133129-133134
    Unknown23018(1)
    sprite('mk615_13', 32767)	# 133135-165901
    ExitState()
    label(180)
    sprite('mk000_00', 1)	# 165902-165902
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('mk000_00', 5)	# 165903-165907
    sprite('mk000_01', 5)	# 165908-165912
    sprite('mk000_02', 6)	# 165913-165918
    sprite('mk000_03', 6)	# 165919-165924
    sprite('mk000_04', 5)	# 165925-165929
    sprite('mk000_05', 5)	# 165930-165934
    sprite('mk000_06', 6)	# 165935-165940
    sprite('mk000_07', 6)	# 165941-165946
    sprite('mk000_08', 5)	# 165947-165951
    sprite('mk000_09', 5)	# 165952-165956
    gotoLabel(181)
    label(182)
    sprite('mk615_00', 6)	# 165957-165962
    sprite('mk615_01', 6)	# 165963-165968
    SFX_1('bmk601pak')
    sprite('mk615_02', 6)	# 165969-165974
    sprite('mk615_03', 6)	# 165975-165980
    sprite('mk615_04', 6)	# 165981-165986
    sprite('mk615_05', 6)	# 165987-165992
    sprite('mk615_06', 6)	# 165993-165998
    sprite('mk615_07', 7)	# 165999-166005
    sprite('mk615_08', 10)	# 166006-166015
    sprite('mk615_09', 5)	# 166016-166020
    sprite('mk615_10', 5)	# 166021-166025
    sprite('mk615_11', 6)	# 166026-166031
    sprite('mk615_12', 6)	# 166032-166037
    Unknown23018(1)
    sprite('mk615_13', 32767)	# 166038-198804
    ExitState()
    label(190)
    sprite('mk634_00', 1)	# 198805-198805
    if SLOT_158:
        Unknown1000(-1199000)
    else:
        Unknown1000(-1199000)
    SFX_1('bmk600bma')
    Unknown2019(-500)
    label(191)
    sprite('mk634_00', 6)	# 198806-198811
    sprite('mk634_01', 6)	# 198812-198817
    sprite('mk634_02', 6)	# 198818-198823
    sprite('mk634_03', 6)	# 198824-198829
    sprite('mk634_04', 6)	# 198830-198835
    if SLOT_97:
        _gotolabel(191)
    sprite('mk634_00', 1)	# 198836-198836
    Unknown21007(24, 40)
    Unknown21011(240)
    label(192)
    sprite('mk634_00', 6)	# 198837-198842
    sprite('mk634_01', 6)	# 198843-198848
    sprite('mk634_02', 6)	# 198849-198854
    sprite('mk634_03', 6)	# 198855-198860
    sprite('mk634_04', 6)	# 198861-198866
    gotoLabel(192)
    ExitState()
    label(991)
    sprite('mk000_00', 1)	# 198867-198867
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('mk000_00', 5)	# 198868-198872
    sprite('mk000_01', 5)	# 198873-198877
    sprite('mk000_02', 6)	# 198878-198883
    sprite('mk000_03', 6)	# 198884-198889
    sprite('mk000_04', 5)	# 198890-198894
    sprite('mk000_05', 5)	# 198895-198899
    sprite('mk000_06', 6)	# 198900-198905
    sprite('mk000_07', 6)	# 198906-198911
    sprite('mk000_08', 5)	# 198912-198916
    sprite('mk000_09', 5)	# 198917-198921
    gotoLabel(992)
    label(993)
    sprite('mk033_00', 2)	# 198922-198923

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
    sprite('mk033_01', 2)	# 198924-198925
    label(994)
    sprite('mk033_02', 3)	# 198926-198928
    sprite('mk033_01', 3)	# 198929-198931
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 198932-198934
    ExitState()

@State
def CmnActRoundWin():
    sprite('mk615_00', 6)	# 1-6
    sprite('mk615_01', 6)	# 7-12
    sprite('mk615_02', 6)	# 13-18
    sprite('mk615_03', 6)	# 19-24
    sprite('mk615_04', 6)	# 25-30
    sprite('mk615_05', 6)	# 31-36
    sprite('mk615_06', 6)	# 37-42
    sprite('mk615_07', 7)	# 43-49
    sprite('mk615_08', 10)	# 50-59
    sprite('mk615_09', 5)	# 60-64
    sprite('mk615_10', 5)	# 65-69
    sprite('mk615_11', 6)	# 70-75
    sprite('mk615_12', 6)	# 76-81
    if random_(2, 0, 50):
        SFX_1('mk400')
    else:
        SFX_1('mk401')
    Unknown23018(1)
    label(0)
    sprite('mk615_13', 10)	# 82-91
    loopRest()
    if SLOT_97:
        _gotolabel(0)
    sprite('mk615_13', 32767)	# 92-32858

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
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('biz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('pak'):
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
    sprite('mk200_00', 2)	# 4-5
    sprite('mk200_01ex01', 1)	# 6-6
    sprite('mk200_02ex01', 1)	# 7-7
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 8-8
    sprite('mk200_04ex01', 1)	# 9-9	 **attackbox here**
    sprite('mk200_04ex01', 1)	# 10-10	 **attackbox here**
    sprite('mk200_01', 1)	# 11-11
    sprite('mk200_01ex00', 1)	# 12-12
    sprite('mk200_02ex00', 1)	# 13-13
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 14-14
    sprite('mk200_04ex00', 1)	# 15-15	 **attackbox here**
    sprite('mk200_04ex00', 2)	# 16-17	 **attackbox here**
    sprite('mk200_01ex01', 2)	# 18-19
    sprite('mk200_00', 2)	# 20-21
    loopRest()
    sprite('mk000_00', 2)	# 22-23
    sprite('mk412_00', 2)	# 24-25
    sprite('mk412_01', 1)	# 26-26
    sprite('mk412_02', 1)	# 27-27
    sprite('mk412_03', 1)	# 28-28
    sprite('mk412_04', 1)	# 29-29
    sprite('mk412_05', 1)	# 30-30
    SFX_0('004_swing_grap_1_1')
    sprite('mk412_06', 3)	# 31-33	 **attackbox here**
    sprite('mk412_07', 3)	# 34-36
    sprite('mk412_08', 8)	# 37-44
    sprite('mk412_09', 2)	# 45-46
    sprite('mk412_10', 2)	# 47-48
    sprite('mk202_00', 2)	# 49-50
    teleportRelativeX(-15000)
    Unknown3029(1)
    sprite('mk202_01', 2)	# 51-52
    sprite('mk202_02', 2)	# 53-54
    sprite('mk202_03', 2)	# 55-56	 **attackbox here**
    teleportRelativeX(30000)
    ScreenShake(15000, 15000)
    Unknown1056(1050)
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    SFX_0('004_swing_grap_1_1')
    SFX_0('209_down_normal_0')
    SFX_0('024_getset_a')
    sprite('mk202_03', 5)	# 57-61	 **attackbox here**
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    sprite('mk202_04', 15)	# 62-76
    sprite('mk202_13', 4)	# 77-80
    sprite('mk202_14', 2)	# 81-82
    sprite('mk202_15', 2)	# 83-84
    sprite('mk202_16', 3)	# 85-87
    Unknown3029(0)
    sprite('mk610_01', 2)	# 88-89
    sprite('mk610_02', 2)	# 90-91
    sprite('mk610_03', 3)	# 92-94
    sprite('mk610_04', 4)	# 95-98
    sprite('mk610_05', 4)	# 99-102
    sprite('mk610_06', 4)	# 103-106
    sprite('mk610_07', 4)	# 107-110
    sprite('mk610_08', 4)	# 111-114
    sprite('mk610_09', 4)	# 115-118
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bmk524', 100, 896232802, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bmk402_0', 100, 879455586, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bmk522', 100, 896232802, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('mk610_10', 6)	# 119-124
    label(1)
    sprite('mk610_11', 6)	# 125-130
    loopRest()
    if SLOT_97:
        _gotolabel(1)
    sprite('mk610_11', 32767)	# 131-32897
    Unknown23018(1)
    loopRest()
    label(10)
    sprite('mk611_00', 6)	# 32898-32903
    sprite('mk611_01', 6)	# 32904-32909
    sprite('mk611_02', 6)	# 32910-32915
    sprite('mk611_03', 6)	# 32916-32921
    sprite('mk611_04', 6)	# 32922-32927
    sprite('mk611_05', 6)	# 32928-32933
    sprite('mk611_06', 6)	# 32934-32939
    sprite('mk611_07', 6)	# 32940-32945
    sprite('mk611_08', 6)	# 32946-32951
    sprite('mk611_09', 6)	# 32952-32957	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bmk524', 100, 896232802, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bmk402_0', 100, 879455586, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bmk520', 100, 896232802, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(11)
    sprite('mk611_09', 6)	# 32958-32963	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 32964-32969	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 32970-32975	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 32976-32981	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 32982-32987	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 32988-32993	 **attackbox here**
    if SLOT_97:
        _gotolabel(11)
    Unknown23018(1)
    label(12)
    sprite('mk611_09', 6)	# 32994-32999	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 33000-33005	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 33006-33011	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 33012-33017	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 33018-33023	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 33024-33029	 **attackbox here**
    loopRest()
    gotoLabel(12)
    label(100)
    sprite('mk611_00', 6)	# 33030-33035
    sprite('mk611_01', 6)	# 33036-33041
    sprite('mk611_02', 6)	# 33042-33047
    sprite('mk611_03', 6)	# 33048-33053
    sprite('mk611_04', 6)	# 33054-33059
    sprite('mk611_05', 6)	# 33060-33065
    sprite('mk611_06', 6)	# 33066-33071
    sprite('mk611_07', 6)	# 33072-33077
    sprite('mk611_08', 6)	# 33078-33083
    sprite('mk611_09', 6)	# 33084-33089	 **attackbox here**
    SFX_1('bmk700btg')
    label(101)
    sprite('mk611_09', 6)	# 33090-33095	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 33096-33101	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 33102-33107	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 33108-33113	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 33114-33119	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 33120-33125	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('mk611_09', 1)	# 33126-33126	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    label(102)
    sprite('mk611_09', 6)	# 33127-33132	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 33133-33138	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 33139-33144	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 33145-33150	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 33151-33156	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 33157-33162	 **attackbox here**
    loopRest()
    gotoLabel(102)
    label(110)
    sprite('mk000_00', 1)	# 33163-33163
    Unknown2034(0)
    Unknown2053(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('mk000_00', 5)	# 33164-33168
    sprite('mk000_01', 5)	# 33169-33173
    sprite('mk000_02', 6)	# 33174-33179
    sprite('mk000_03', 6)	# 33180-33185
    sprite('mk000_04', 5)	# 33186-33190
    sprite('mk000_05', 5)	# 33191-33195
    sprite('mk000_06', 6)	# 33196-33201
    sprite('mk000_07', 6)	# 33202-33207
    sprite('mk000_08', 5)	# 33208-33212
    sprite('mk000_09', 5)	# 33213-33217
    gotoLabel(111)
    label(112)
    sprite('mk611_00', 6)	# 33218-33223
    sprite('mk611_01', 6)	# 33224-33229
    sprite('mk611_02', 6)	# 33230-33235
    sprite('mk611_03', 6)	# 33236-33241
    sprite('mk611_04', 6)	# 33242-33247
    sprite('mk611_05', 6)	# 33248-33253
    sprite('mk611_06', 6)	# 33254-33259
    sprite('mk611_07', 6)	# 33260-33265
    sprite('mk611_08', 6)	# 33266-33271
    sprite('mk611_09', 6)	# 33272-33277	 **attackbox here**
    SFX_1('bmk701pyo')
    label(113)
    sprite('mk611_09', 6)	# 33278-33283	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 33284-33289	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 33290-33295	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 33296-33301	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 33302-33307	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 33308-33313	 **attackbox here**
    if SLOT_97:
        _gotolabel(113)
    sprite('mk611_09', 1)	# 33314-33314	 **attackbox here**
    Unknown23018(1)
    label(114)
    sprite('mk611_09', 6)	# 33315-33320	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 33321-33326	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 33327-33332	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 33333-33338	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 33339-33344	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 33345-33350	 **attackbox here**
    gotoLabel(114)
    label(120)
    sprite('mk000_00', 1)	# 33351-33351

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('mk000_00', 5)	# 33352-33356
    sprite('mk000_01', 5)	# 33357-33361
    sprite('mk000_02', 6)	# 33362-33367
    sprite('mk000_03', 6)	# 33368-33373
    sprite('mk000_04', 5)	# 33374-33378
    sprite('mk000_05', 5)	# 33379-33383
    sprite('mk000_06', 6)	# 33384-33389
    sprite('mk000_07', 6)	# 33390-33395
    sprite('mk000_08', 5)	# 33396-33400
    sprite('mk000_09', 5)	# 33401-33405
    gotoLabel(121)
    label(122)
    sprite('mk610_01', 2)	# 33406-33407
    SFX_1('bmk702pce')
    sprite('mk610_02', 2)	# 33408-33409
    sprite('mk610_03', 3)	# 33410-33412
    sprite('mk610_04', 4)	# 33413-33416
    sprite('mk610_05', 4)	# 33417-33420
    sprite('mk610_06', 4)	# 33421-33424
    sprite('mk610_07', 4)	# 33425-33428
    sprite('mk610_08', 4)	# 33429-33432
    sprite('mk610_09', 4)	# 33433-33436
    sprite('mk610_10', 6)	# 33437-33442
    sprite('mk610_11', 6)	# 33443-33448
    label(123)
    sprite('mk610_11', 1)	# 33449-33449
    if SLOT_97:
        _gotolabel(123)
    sprite('mk610_11', 50)	# 33450-33499
    sprite('mk610_11', 32767)	# 33500-66266
    SFX_1('bmk703pce')
    Unknown21011(120)
    label(130)
    sprite('mk611_00', 6)	# 66267-66272

    def upon_40():
        clearUponHandler(40)
        SFX_1('bmk702rwi')
    sprite('mk611_01', 6)	# 66273-66278
    sprite('mk611_02', 6)	# 66279-66284
    sprite('mk611_03', 6)	# 66285-66290
    sprite('mk611_04', 6)	# 66291-66296
    sprite('mk611_05', 6)	# 66297-66302
    sprite('mk611_06', 6)	# 66303-66308
    sprite('mk611_07', 6)	# 66309-66314
    sprite('mk611_08', 6)	# 66315-66320
    sprite('mk611_09', 6)	# 66321-66326	 **attackbox here**
    SFX_1('bmk700rwi')
    label(131)
    sprite('mk611_09', 6)	# 66327-66332	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 66333-66338	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 66339-66344	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 66345-66350	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 66351-66356	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 66357-66362	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('mk611_09', 1)	# 66363-66363	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(460)
    label(132)
    sprite('mk611_09', 6)	# 66364-66369	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 66370-66375	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 66376-66381	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 66382-66387	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 66388-66393	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 66394-66399	 **attackbox here**
    loopRest()
    gotoLabel(132)
    label(140)
    sprite('mk200_00', 2)	# 66400-66401
    sprite('mk200_01ex01', 1)	# 66402-66402
    sprite('mk200_02ex01', 1)	# 66403-66403
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 66404-66404
    sprite('mk200_04ex01', 1)	# 66405-66405	 **attackbox here**
    sprite('mk200_04ex01', 1)	# 66406-66406	 **attackbox here**
    sprite('mk200_01', 1)	# 66407-66407
    sprite('mk200_01ex00', 1)	# 66408-66408
    sprite('mk200_02ex00', 1)	# 66409-66409
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 66410-66410
    sprite('mk200_04ex00', 1)	# 66411-66411	 **attackbox here**
    sprite('mk200_04ex00', 2)	# 66412-66413	 **attackbox here**
    sprite('mk200_01ex01', 2)	# 66414-66415
    sprite('mk200_00', 2)	# 66416-66417
    loopRest()
    sprite('mk000_00', 2)	# 66418-66419
    sprite('mk412_00', 2)	# 66420-66421
    sprite('mk412_01', 1)	# 66422-66422
    sprite('mk412_02', 1)	# 66423-66423
    sprite('mk412_03', 1)	# 66424-66424
    sprite('mk412_04', 1)	# 66425-66425
    sprite('mk412_05', 1)	# 66426-66426
    SFX_0('004_swing_grap_1_1')
    sprite('mk412_06', 3)	# 66427-66429	 **attackbox here**
    sprite('mk412_07', 3)	# 66430-66432
    sprite('mk412_08', 8)	# 66433-66440
    sprite('mk412_09', 2)	# 66441-66442
    sprite('mk412_10', 2)	# 66443-66444
    sprite('mk202_00', 2)	# 66445-66446
    teleportRelativeX(-15000)
    Unknown3029(1)
    sprite('mk202_01', 2)	# 66447-66448
    sprite('mk202_02', 2)	# 66449-66450
    sprite('mk202_03', 2)	# 66451-66452	 **attackbox here**
    teleportRelativeX(30000)
    ScreenShake(15000, 15000)
    Unknown1056(1050)
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    SFX_0('004_swing_grap_1_1')
    SFX_0('209_down_normal_0')
    SFX_0('024_getset_a')
    sprite('mk202_03', 5)	# 66453-66457	 **attackbox here**
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    sprite('mk202_04', 15)	# 66458-66472
    sprite('mk202_13', 4)	# 66473-66476
    sprite('mk202_14', 2)	# 66477-66478
    sprite('mk202_15', 2)	# 66479-66480
    sprite('mk202_16', 3)	# 66481-66483
    Unknown3029(0)
    sprite('mk610_01', 2)	# 66484-66485
    sprite('mk610_02', 2)	# 66486-66487
    sprite('mk610_03', 3)	# 66488-66490
    sprite('mk610_04', 4)	# 66491-66494
    sprite('mk610_05', 4)	# 66495-66498
    sprite('mk610_06', 4)	# 66499-66502
    sprite('mk610_07', 4)	# 66503-66506
    sprite('mk610_08', 4)	# 66507-66510
    sprite('mk610_09', 4)	# 66511-66514
    SFX_1('bmk700ugo')
    sprite('mk610_10', 6)	# 66515-66520
    label(141)
    sprite('mk610_11', 1)	# 66521-66521
    if SLOT_97:
        _gotolabel(141)
    sprite('mk610_11', 30)	# 66522-66551
    Unknown21011(460)
    sprite('mk610_11', 32767)	# 66552-99318
    Unknown21007(24, 40)
    label(150)
    sprite('mk611_00', 6)	# 99319-99324
    if SLOT_158:
        Unknown2019(-1000)
    else:
        Unknown2019(1000)
    sprite('mk611_01', 6)	# 99325-99330
    sprite('mk611_02', 6)	# 99331-99336
    sprite('mk611_03', 6)	# 99337-99342
    sprite('mk611_04', 6)	# 99343-99348
    sprite('mk611_05', 6)	# 99349-99354
    sprite('mk611_06', 6)	# 99355-99360
    sprite('mk611_07', 6)	# 99361-99366
    sprite('mk611_08', 6)	# 99367-99372
    sprite('mk611_09', 6)	# 99373-99378	 **attackbox here**
    SFX_1('bmk700uca')
    label(151)
    sprite('mk611_09', 6)	# 99379-99384	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 99385-99390	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 99391-99396	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 99397-99402	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 99403-99408	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 99409-99414	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('mk611_09', 1)	# 99415-99415	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(270)
    label(152)
    sprite('mk611_09', 6)	# 99416-99421	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 99422-99427	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 99428-99433	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 99434-99439	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 99440-99445	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 99446-99451	 **attackbox here**
    loopRest()
    gotoLabel(152)
    label(160)
    sprite('mk611_00', 6)	# 99452-99457
    sprite('mk611_01', 6)	# 99458-99463
    sprite('mk611_02', 6)	# 99464-99469
    sprite('mk611_03', 6)	# 99470-99475
    sprite('mk611_04', 6)	# 99476-99481
    sprite('mk611_05', 6)	# 99482-99487
    sprite('mk611_06', 6)	# 99488-99493
    sprite('mk611_07', 6)	# 99494-99499
    sprite('mk611_08', 6)	# 99500-99505
    sprite('mk611_09', 6)	# 99506-99511	 **attackbox here**
    SFX_1('bmk700bno')
    label(161)
    sprite('mk611_09', 6)	# 99512-99517	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 99518-99523	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 99524-99529	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 99530-99535	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 99536-99541	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 99542-99547	 **attackbox here**
    if SLOT_97:
        _gotolabel(161)
    sprite('mk611_09', 6)	# 99548-99553	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 99554-99559	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 99560-99565	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 99566-99571	 **attackbox here**
    Unknown21007(24, 40)
    sprite('mk611_09ex04', 6)	# 99572-99577	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 99578-99583	 **attackbox here**
    Unknown21011(240)
    label(162)
    sprite('mk611_09', 6)	# 99584-99589	 **attackbox here**
    sprite('mk611_09ex01', 6)	# 99590-99595	 **attackbox here**
    sprite('mk611_09ex02', 6)	# 99596-99601	 **attackbox here**
    sprite('mk611_09ex03', 6)	# 99602-99607	 **attackbox here**
    sprite('mk611_09ex04', 6)	# 99608-99613	 **attackbox here**
    sprite('mk611_09ex05', 6)	# 99614-99619	 **attackbox here**
    loopRest()
    gotoLabel(162)
    label(170)
    sprite('mk200_00', 2)	# 99620-99621
    sprite('mk200_01ex01', 1)	# 99622-99622
    sprite('mk200_02ex01', 1)	# 99623-99623
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 99624-99624
    sprite('mk200_04ex01', 1)	# 99625-99625	 **attackbox here**
    sprite('mk200_04ex01', 1)	# 99626-99626	 **attackbox here**
    sprite('mk200_01', 1)	# 99627-99627
    sprite('mk200_01ex00', 1)	# 99628-99628
    sprite('mk200_02ex00', 1)	# 99629-99629
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 99630-99630
    sprite('mk200_04ex00', 1)	# 99631-99631	 **attackbox here**
    sprite('mk200_04ex00', 2)	# 99632-99633	 **attackbox here**
    sprite('mk200_01ex01', 2)	# 99634-99635
    sprite('mk200_00', 2)	# 99636-99637
    loopRest()
    sprite('mk000_00', 2)	# 99638-99639
    sprite('mk412_00', 2)	# 99640-99641
    sprite('mk412_01', 1)	# 99642-99642
    sprite('mk412_02', 1)	# 99643-99643
    sprite('mk412_03', 1)	# 99644-99644
    sprite('mk412_04', 1)	# 99645-99645
    sprite('mk412_05', 1)	# 99646-99646
    SFX_0('004_swing_grap_1_1')
    sprite('mk412_06', 3)	# 99647-99649	 **attackbox here**
    sprite('mk412_07', 3)	# 99650-99652
    sprite('mk412_08', 8)	# 99653-99660
    sprite('mk412_09', 2)	# 99661-99662
    sprite('mk412_10', 2)	# 99663-99664
    sprite('mk202_00', 2)	# 99665-99666
    teleportRelativeX(-15000)
    Unknown3029(1)
    sprite('mk202_01', 2)	# 99667-99668
    sprite('mk202_02', 2)	# 99669-99670
    sprite('mk202_03', 2)	# 99671-99672	 **attackbox here**
    teleportRelativeX(30000)
    ScreenShake(15000, 15000)
    Unknown1056(1050)
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    SFX_0('004_swing_grap_1_1')
    SFX_0('209_down_normal_0')
    SFX_0('024_getset_a')
    sprite('mk202_03', 5)	# 99673-99677	 **attackbox here**
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    sprite('mk202_04', 15)	# 99678-99692
    sprite('mk202_13', 4)	# 99693-99696
    sprite('mk202_14', 2)	# 99697-99698
    sprite('mk202_15', 2)	# 99699-99700
    sprite('mk202_16', 3)	# 99701-99703
    Unknown3029(0)
    sprite('mk610_01', 2)	# 99704-99705
    sprite('mk610_02', 2)	# 99706-99707
    sprite('mk610_03', 3)	# 99708-99710
    sprite('mk610_04', 4)	# 99711-99714
    sprite('mk610_05', 4)	# 99715-99718
    sprite('mk610_06', 4)	# 99719-99722
    sprite('mk610_07', 4)	# 99723-99726
    sprite('mk610_08', 4)	# 99727-99730
    sprite('mk610_09', 4)	# 99731-99734
    SFX_1('bmk700bma')
    sprite('mk610_10', 6)	# 99735-99740
    label(171)
    sprite('mk610_11', 1)	# 99741-99741
    if SLOT_97:
        _gotolabel(171)
    sprite('mk610_11', 32767)	# 99742-132508
    Unknown21007(24, 40)
    Unknown21011(320)
    label(180)
    sprite('mk200_00', 2)	# 132509-132510
    sprite('mk200_01ex01', 1)	# 132511-132511
    sprite('mk200_02ex01', 1)	# 132512-132512
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 132513-132513
    sprite('mk200_04ex01', 1)	# 132514-132514	 **attackbox here**
    sprite('mk200_04ex01', 1)	# 132515-132515	 **attackbox here**
    sprite('mk200_01', 1)	# 132516-132516
    sprite('mk200_01ex00', 1)	# 132517-132517
    sprite('mk200_02ex00', 1)	# 132518-132518
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 132519-132519
    sprite('mk200_04ex00', 1)	# 132520-132520	 **attackbox here**
    sprite('mk200_04ex00', 2)	# 132521-132522	 **attackbox here**
    sprite('mk200_01ex01', 2)	# 132523-132524
    sprite('mk200_00', 2)	# 132525-132526
    loopRest()
    sprite('mk000_00', 2)	# 132527-132528
    sprite('mk412_00', 2)	# 132529-132530
    sprite('mk412_01', 1)	# 132531-132531
    sprite('mk412_02', 1)	# 132532-132532
    sprite('mk412_03', 1)	# 132533-132533
    sprite('mk412_04', 1)	# 132534-132534
    sprite('mk412_05', 1)	# 132535-132535
    SFX_0('004_swing_grap_1_1')
    sprite('mk412_06', 3)	# 132536-132538	 **attackbox here**
    sprite('mk412_07', 3)	# 132539-132541
    sprite('mk412_08', 8)	# 132542-132549
    sprite('mk412_09', 2)	# 132550-132551
    sprite('mk412_10', 2)	# 132552-132553
    sprite('mk202_00', 2)	# 132554-132555
    teleportRelativeX(-15000)
    Unknown3029(1)
    sprite('mk202_01', 2)	# 132556-132557
    sprite('mk202_02', 2)	# 132558-132559
    sprite('mk202_03', 2)	# 132560-132561	 **attackbox here**
    teleportRelativeX(30000)
    ScreenShake(15000, 15000)
    Unknown1056(1050)
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    SFX_0('004_swing_grap_1_1')
    SFX_0('209_down_normal_0')
    SFX_0('024_getset_a')
    sprite('mk202_03', 5)	# 132562-132566	 **attackbox here**
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    sprite('mk202_04', 15)	# 132567-132581
    sprite('mk202_13', 4)	# 132582-132585
    sprite('mk202_14', 2)	# 132586-132587
    sprite('mk202_15', 2)	# 132588-132589
    sprite('mk202_16', 3)	# 132590-132592
    Unknown3029(0)
    sprite('mk610_01', 2)	# 132593-132594
    sprite('mk610_02', 2)	# 132595-132596
    sprite('mk610_03', 3)	# 132597-132599
    sprite('mk610_04', 4)	# 132600-132603
    sprite('mk610_05', 4)	# 132604-132607
    sprite('mk610_06', 4)	# 132608-132611
    sprite('mk610_07', 4)	# 132612-132615
    sprite('mk610_08', 4)	# 132616-132619
    sprite('mk610_09', 4)	# 132620-132623
    SFX_1('bmk700biz')
    sprite('mk610_10', 6)	# 132624-132629
    label(181)
    sprite('mk610_11', 1)	# 132630-132630
    if SLOT_97:
        _gotolabel(181)
    sprite('mk610_11', 32767)	# 132631-165397
    Unknown21007(24, 40)
    Unknown21011(240)
    label(190)
    sprite('mk200_00', 2)	# 165398-165399
    sprite('mk200_01ex01', 1)	# 165400-165400
    sprite('mk200_02ex01', 1)	# 165401-165401
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 165402-165402
    sprite('mk200_04ex01', 1)	# 165403-165403	 **attackbox here**
    sprite('mk200_04ex01', 1)	# 165404-165404	 **attackbox here**
    sprite('mk200_01', 1)	# 165405-165405
    sprite('mk200_01ex00', 1)	# 165406-165406
    sprite('mk200_02ex00', 1)	# 165407-165407
    SFX_0('004_swing_grap_1_0')
    sprite('mk200_03', 1)	# 165408-165408
    sprite('mk200_04ex00', 1)	# 165409-165409	 **attackbox here**
    sprite('mk200_04ex00', 2)	# 165410-165411	 **attackbox here**
    sprite('mk200_01ex01', 2)	# 165412-165413
    sprite('mk200_00', 2)	# 165414-165415
    loopRest()
    sprite('mk000_00', 2)	# 165416-165417
    sprite('mk412_00', 2)	# 165418-165419
    sprite('mk412_01', 1)	# 165420-165420
    sprite('mk412_02', 1)	# 165421-165421
    sprite('mk412_03', 1)	# 165422-165422
    sprite('mk412_04', 1)	# 165423-165423
    sprite('mk412_05', 1)	# 165424-165424
    SFX_0('004_swing_grap_1_1')
    sprite('mk412_06', 3)	# 165425-165427	 **attackbox here**
    sprite('mk412_07', 3)	# 165428-165430
    sprite('mk412_08', 8)	# 165431-165438
    sprite('mk412_09', 2)	# 165439-165440
    sprite('mk412_10', 2)	# 165441-165442
    sprite('mk202_00', 2)	# 165443-165444
    teleportRelativeX(-15000)
    Unknown3029(1)
    sprite('mk202_01', 2)	# 165445-165446
    sprite('mk202_02', 2)	# 165447-165448
    sprite('mk202_03', 2)	# 165449-165450	 **attackbox here**
    teleportRelativeX(30000)
    ScreenShake(15000, 15000)
    Unknown1056(1050)
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    SFX_0('004_swing_grap_1_1')
    SFX_0('209_down_normal_0')
    SFX_0('024_getset_a')
    sprite('mk202_03', 5)	# 165451-165455	 **attackbox here**
    GFX_1('ef_smokes', 104)
    GFX_1('ef_jumpcircle00', 104)
    sprite('mk202_04', 15)	# 165456-165470
    sprite('mk202_13', 4)	# 165471-165474
    sprite('mk202_14', 2)	# 165475-165476
    sprite('mk202_15', 2)	# 165477-165478
    sprite('mk202_16', 3)	# 165479-165481
    Unknown3029(0)
    sprite('mk610_01', 2)	# 165482-165483
    sprite('mk610_02', 2)	# 165484-165485
    sprite('mk610_03', 3)	# 165486-165488
    sprite('mk610_04', 4)	# 165489-165492
    sprite('mk610_05', 4)	# 165493-165496
    sprite('mk610_06', 4)	# 165497-165500
    sprite('mk610_07', 4)	# 165501-165504
    sprite('mk610_08', 4)	# 165505-165508
    sprite('mk610_09', 4)	# 165509-165512
    SFX_1('bmk700pak')
    sprite('mk610_10', 6)	# 165513-165518
    label(191)
    sprite('mk610_11', 1)	# 165519-165519
    if SLOT_97:
        _gotolabel(191)
    sprite('mk610_11', 15)	# 165520-165534
    sprite('mk610_11', 32767)	# 165535-198301
    Unknown21007(24, 40)
    Unknown21011(240)

@State
def CmnActLose():
    sprite('mk620_00', 7)	# 1-7
    sprite('mk620_01', 7)	# 8-14
    sprite('mk620_02', 7)	# 15-21
    sprite('mk620_03', 7)	# 22-28
    sprite('mk620_04', 7)	# 29-35
    sprite('mk620_05', 7)	# 36-42
    sprite('mk620_06', 7)	# 43-49
    sprite('mk620_07', 7)	# 50-56
    sprite('mk620_08', 7)	# 57-63
    sprite('mk620_09', 7)	# 64-70
    sprite('mk620_10', 15)	# 71-85
    sprite('mk620_10', 5)	# 86-90
    if random_(2, 0, 50):
        SFX_1('bmk403_0')
    else:
        SFX_1('bmk403_1')
    label(1)
    sprite('mk620_10', 8)	# 91-98
    loopRest()
    if SLOT_97:
        _gotolabel(1)
    sprite('mk620_10', 32767)	# 99-32865
    Unknown23018(1)

@State
def EventDefEntryWait():
    label(0)
    sprite('mk000_00', 5)	# 1-5
    sprite('mk000_01', 5)	# 6-10
    sprite('mk000_02', 6)	# 11-16
    sprite('mk000_03', 6)	# 17-22
    sprite('mk000_04', 5)	# 23-27
    sprite('mk000_05', 5)	# 28-32
    sprite('mk000_06', 6)	# 33-38
    sprite('mk000_07', 6)	# 39-44
    sprite('mk000_08', 5)	# 45-49
    sprite('mk000_09', 5)	# 50-54
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryStand():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefEntryFDashOut():
    Unknown2017(0)
    Unknown2034(0)
    sprite('mk032_00', 2)	# 1-2
    SLOT_51 = 0
    label(0)
    sprite('mk032_01', 2)	# 3-4
    physicsXImpulse(21000)
    Unknown1028(200)
    sprite('mk032_02', 4)	# 5-8
    sprite('mk032_03', 4)	# 9-12
    if (SLOT_51 <= 4):
        Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 13-16
    sprite('mk032_05', 4)	# 17-20
    sprite('mk032_06', 4)	# 21-24
    sprite('mk032_07', 4)	# 25-28
    if (SLOT_51 <= 4):
        Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 29-31
    loopRest()
    SLOT_51 = (SLOT_51 + 1)
    gotoLabel(0)

@State
def EventDefEntryFDashOutOpposite():
    Unknown2017(0)
    Unknown2034(0)
    Unknown2006()
    Unknown2005()
    sprite('mk032_00', 2)	# 1-2
    SLOT_51 = 0
    label(0)
    sprite('mk032_01', 2)	# 3-4
    physicsXImpulse(21000)
    Unknown1028(200)
    sprite('mk032_02', 4)	# 5-8
    sprite('mk032_03', 4)	# 9-12
    if (SLOT_51 <= 4):
        Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 13-16
    sprite('mk032_05', 4)	# 17-20
    sprite('mk032_06', 4)	# 21-24
    sprite('mk032_07', 4)	# 25-28
    if (SLOT_51 <= 4):
        Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 29-31
    loopRest()
    SLOT_51 = (SLOT_51 + 1)
    gotoLabel(0)

@State
def EventDefEntryFDashIn():
    Unknown2017(0)
    Unknown2034(0)
    Unknown1000(-1280000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 400000):
                sendToLabel(1)
        elif (SLOT_22 > (-400000)):
            sendToLabel(1)
    sprite('mk032_01', 1)	# 1-1
    physicsXImpulse(21000)
    Unknown1028(200)
    label(0)
    sprite('mk032_01', 2)	# 2-3
    sprite('mk032_02', 4)	# 4-7
    sprite('mk032_03', 4)	# 8-11
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 12-15
    sprite('mk032_05', 4)	# 16-19
    sprite('mk032_06', 4)	# 20-23
    sprite('mk032_07', 4)	# 24-27
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 28-30
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('mk032_09', 3)	# 31-33
    teleportRelativeX(20000)
    Unknown1019(70)
    sprite('mk032_09', 3)	# 34-36
    Unknown1019(70)
    sprite('mk032_09', 3)	# 37-39
    Unknown1019(70)
    sprite('mk032_09', 3)	# 40-42
    Unknown1019(70)
    sprite('mk024_00', 3)	# 43-45
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('mk024_00', 2)	# 46-47
    sprite('mk024_01', 2)	# 48-49
    sprite('mk024_02', 2)	# 50-51
    sprite('mk024_03', 2)	# 52-53
    sprite('mk024_04', 2)	# 54-55
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    loopRest()

@State
def EventDefWin():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefLose():
    sprite('mk620_10', 32767)	# 1-32767

@State
def EventLose1():
    sprite('mk070_09', 32767)	# 1-32767

@State
def EventLose2():
    sprite('mk063_11', 32767)	# 1-32767

@State
def EventYoroke():
    label(0)
    sprite('mk070_02', 5)	# 1-5
    gotoLabel(0)

@State
def EventYorokeToStand():
    sprite('mk070_02', 7)	# 1-7
    sprite('mk070_03', 7)	# 8-14
    sprite('mk070_10', 7)	# 15-21
    sprite('mk070_11', 7)	# 22-28
    sprite('mk070_12', 7)	# 29-35
    sprite('mk070_13', 7)	# 36-42
    loopRest()
    enterState('CmnActStand')

@State
def EventYorokeToStand():
    sprite('mk070_02', 7)	# 1-7
    sprite('mk070_03', 7)	# 8-14
    sprite('mk070_10', 7)	# 15-21
    sprite('mk070_11', 7)	# 22-28
    sprite('mk070_12', 7)	# 29-35
    sprite('mk070_13', 7)	# 36-42
    loopRest()
    enterState('EventVsTBSad')

@State
def EventCrouchLoop():
    label(0)
    sprite('mk010_02', 7)	# 1-7
    sprite('mk010_03', 7)	# 8-14
    sprite('mk010_04', 7)	# 15-21
    sprite('mk010_05', 7)	# 22-28
    sprite('mk010_06', 7)	# 29-35
    sprite('mk010_07', 7)	# 36-42
    sprite('mk010_08', 7)	# 43-49
    loopRest()
    gotoLabel(0)

@State
def EventCrouchToStand():
    sprite('mk010_01', 4)	# 1-4
    sprite('mk010_00', 4)	# 5-8
    loopRest()
    enterState('CmnActStand')

@State
def EventVsTKEntry01():
    sprite('mk600_00', 32767)	# 1-32767

@State
def EventVsTKEntry02():
    sprite('mk600_01', 9)	# 1-9
    sprite('mk600_02', 6)	# 10-15
    sprite('mk600_03', 6)	# 16-21
    sprite('mk600_04', 6)	# 22-27
    sprite('mk600_05', 6)	# 28-33
    sprite('mk600_06', 6)	# 34-39
    sprite('mk600_07', 6)	# 40-45
    sprite('mk600_08', 6)	# 46-51
    SFX_0('019_cloth_b')
    sprite('mk600_09', 6)	# 52-57
    sprite('mk600_10', 6)	# 58-63
    GFX_0('EntryMant', 0)
    sprite('mk600_11', 6)	# 64-69
    sprite('mk600_12', 6)	# 70-75
    sprite('mk600_13', 6)	# 76-81
    sprite('mk600_14', 6)	# 82-87
    sprite('mk600_15', 6)	# 88-93
    sprite('mk600_16', 6)	# 94-99
    loopRest()
    enterState('CmnActStand')

@State
def EventvsTBStay():
    Unknown2034(0)
    sprite('null', 32767)	# 1-32767
    Unknown1000(-985000)

@State
def EventvsTBDash():
    Unknown2034(0)
    sprite('mk032_00', 2)	# 1-2
    physicsXImpulse(25000)
    label(0)
    sprite('mk032_01', 2)	# 3-4
    sprite('mk032_02', 4)	# 5-8
    sprite('mk032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 13-16
    sprite('mk032_05', 4)	# 17-20
    sprite('mk032_06', 4)	# 21-24
    sprite('mk032_07', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 29-31
    loopRest()
    gotoLabel(0)

@State
def EventvsTGRoundWin():
    sprite('mk615_00', 6)	# 1-6
    sprite('mk615_01', 6)	# 7-12
    sprite('mk615_02', 6)	# 13-18
    sprite('mk615_03', 6)	# 19-24
    sprite('mk615_04', 6)	# 25-30
    sprite('mk615_05', 6)	# 31-36
    sprite('mk615_06', 6)	# 37-42
    sprite('mk615_07', 7)	# 43-49
    sprite('mk615_08', 10)	# 50-59
    sprite('mk615_09', 5)	# 60-64
    sprite('mk615_10', 5)	# 65-69
    sprite('mk615_11', 6)	# 70-75
    sprite('mk615_12', 6)	# 76-81
    sprite('mk615_13', 32767)	# 82-32848

@State
def EventVsTBExcite():
    sprite('mk300_00', 6)	# 1-6
    sprite('mk300_01', 6)	# 7-12
    sprite('mk300_02', 6)	# 13-18
    sprite('mk300_03', 6)	# 19-24
    sprite('mk300_04', 32767)	# 25-32791

@State
def EventVsTBExciteEnd():
    sprite('mk300_05', 6)	# 1-6
    sprite('mk300_06', 6)	# 7-12
    sprite('mk300_07', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def EventVsTBSad():
    sprite('mk620_00', 32767)	# 1-32767
    loopRest()

@State
def EventVsIZExcite():
    sprite('mk611_00', 6)	# 1-6
    sprite('mk611_01', 6)	# 7-12
    sprite('mk611_02', 6)	# 13-18
    sprite('mk611_03', 6)	# 19-24
    sprite('mk601_00', 6)	# 25-30
    sprite('mk601_00', 6)	# 31-36
    sprite('mk601_01', 6)	# 37-42
    sprite('mk601_02', 4)	# 43-46
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    sprite('mk601_03', 6)	# 47-52
    sprite('mk601_04', 6)	# 53-58
    sprite('mk601_05', 6)	# 59-64
    sprite('mk601_06', 6)	# 65-70
    sprite('mk601_07', 4)	# 71-74
    SFX_0('008_swing_pole_0')
    sprite('mk601_08', 4)	# 75-78
    sprite('mk601_09', 4)	# 79-82
    SFX_0('008_swing_pole_0')
    sprite('mk601_10', 4)	# 83-86
    sprite('mk601_11', 8)	# 87-94
    SFX_0('008_swing_pole_1')
    sprite('mk601_12', 6)	# 95-100
    sprite('mk601_13', 270)	# 101-370
    sprite('mk601_14', 6)	# 371-376
    sprite('mk601_15', 6)	# 377-382
    loopRest()
    enterState('CmnActStand')

@State
def EventYorokeSit():
    sprite('mk070_00', 3)	# 1-3
    sprite('mk070_01', 3)	# 4-6
    sprite('mk070_02', 3)	# 7-9
    sprite('mk070_03', 3)	# 10-12
    sprite('mk070_04', 4)	# 13-16
    sprite('mk070_05', 4)	# 17-20
    sprite('mk070_06', 32767)	# 21-32787
    loopRest()

@State
def EventStandup():
    sprite('mk070_06', 4)	# 1-4
    sprite('mk070_05', 4)	# 5-8
    sprite('mk070_04', 4)	# 9-12
    sprite('mk070_03', 3)	# 13-15
    sprite('mk070_02', 3)	# 16-18
    sprite('mk070_01', 3)	# 19-21
    sprite('mk070_00', 3)	# 22-24
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
    sprite('mk030_00', 5)	# 1-5
    physicsXImpulse(4650)
    sprite('mk030_01', 6)	# 6-11
    label(0)
    sprite('mk030_02', 6)	# 12-17
    sprite('mk030_03', 6)	# 18-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk030_04', 6)	# 24-29
    sprite('mk030_05', 6)	# 30-35
    sprite('mk030_06', 6)	# 36-41
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventDashScreenOut():
    sprite('mk032_00', 2)	# 1-2
    Unknown2005()
    Unknown2034(0)
    Unknown2017(0)
    sprite('mk032_01', 2)	# 3-4
    physicsXImpulse(32000)
    sprite('mk032_02', 4)	# 5-8
    sprite('mk032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 13-16
    sprite('mk032_05', 4)	# 17-20
    sprite('mk032_06', 4)	# 21-24
    sprite('mk032_07', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 29-31
    sprite('mk032_01', 2)	# 32-33
    sprite('mk032_02', 4)	# 34-37
    sprite('mk032_03', 4)	# 38-41
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 42-45
    sprite('mk032_05', 4)	# 46-49
    sprite('mk032_06', 4)	# 50-53
    sprite('mk032_07', 4)	# 54-57
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 58-60
    sprite('mk032_01', 2)	# 61-62
    sprite('mk032_02', 4)	# 63-66
    sprite('mk032_03', 4)	# 67-70
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 71-74
    sprite('mk032_05', 4)	# 75-78
    sprite('mk032_06', 4)	# 79-82
    sprite('mk032_07', 4)	# 83-86
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 87-89
    loopRest()

@State
def EventMKWalkFrameInToKyoro():
    Unknown1000(-900000)
    Unknown2034(0)
    Unknown2037(1)

    def upon_3():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(1)
    sprite('mk030_00', 5)	# 1-5
    physicsXImpulse(4650)
    sprite('mk030_01', 6)	# 6-11
    label(0)
    sprite('mk030_02', 6)	# 12-17
    sprite('mk030_03', 6)	# 18-23
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk030_04', 6)	# 24-29
    sprite('mk030_05', 6)	# 30-35
    sprite('mk030_06', 6)	# 36-41
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    label(2)
    sprite('mk000_00', 5)	# 42-46
    sprite('mk000_01', 5)	# 47-51
    sprite('mk000_02', 6)	# 52-57
    sprite('mk000_03', 6)	# 58-63
    sprite('mk000_04', 5)	# 64-68
    sprite('mk000_05', 5)	# 69-73
    sprite('mk000_06', 6)	# 74-79
    sprite('mk000_07', 6)	# 80-85
    sprite('mk000_08', 5)	# 86-90
    sprite('mk000_09', 5)	# 91-95
    sprite('mk000_00', 5)	# 96-100
    sprite('mk000_01', 5)	# 101-105
    sprite('mk000_02', 6)	# 106-111
    sprite('mk000_03', 6)	# 112-117
    sprite('mk000_04', 5)	# 118-122
    sprite('mk000_05', 5)	# 123-127
    label(3)
    sprite('mk003_00', 5)	# 128-132
    Unknown2005()
    sprite('mk003_01', 5)	# 133-137
    sprite('mk003_02', 5)	# 138-142
    sprite('mk000_00', 5)	# 143-147
    sprite('mk000_01', 5)	# 148-152
    sprite('mk000_02', 6)	# 153-158
    sprite('mk000_03', 6)	# 159-164
    sprite('mk000_04', 5)	# 165-169
    sprite('mk000_05', 5)	# 170-174
    sprite('mk000_06', 6)	# 175-180
    sprite('mk003_00', 5)	# 181-185
    Unknown2005()
    sprite('mk003_01', 5)	# 186-190
    sprite('mk003_02', 5)	# 191-195
    loopRest()
    enterState('CmnActStand')

@State
def EventBUkemi():
    sendToLabelUpon(32, 1)
    label(0)
    sprite('mk000_00', 5)	# 1-5
    sprite('mk000_01', 5)	# 6-10
    sprite('mk000_02', 6)	# 11-16
    sprite('mk000_03', 6)	# 17-22
    sprite('mk000_04', 5)	# 23-27
    sprite('mk000_05', 5)	# 28-32
    sprite('mk000_06', 6)	# 33-38
    sprite('mk000_07', 6)	# 39-44
    sprite('mk000_08', 5)	# 45-49
    sprite('mk000_09', 5)	# 50-54
    gotoLabel(0)
    label(1)
    sprite('mk111_00', 4)	# 55-58
    physicsXImpulse(-12000)
    Unknown2006()
    sprite('mk111_01', 4)	# 59-62
    sprite('mk111_02', 4)	# 63-66
    sprite('mk111_03', 4)	# 67-70
    sprite('mk111_04', 4)	# 71-74
    Unknown1019(40)
    sprite('mk111_05', 4)	# 75-78
    Unknown1019(40)
    sprite('mk111_06', 4)	# 79-82
    Unknown1019(40)
    sprite('mk111_07', 4)	# 83-86
    Unknown1019(40)
    sprite('mk111_08', 4)	# 87-90
    Unknown1019(40)
    sprite('mk111_09', 8)	# 91-98
    Unknown1019(0)
    sprite('mk010_01', 4)	# 99-102
    sprite('mk010_00', 4)	# 103-106
    Unknown2034(0)
    Unknown2037(1)
    sprite('mk000_00', 5)	# 107-111
    sprite('mk000_01', 5)	# 112-116
    sprite('mk000_02', 6)	# 117-122
    sprite('mk000_03', 6)	# 123-128

    def upon_3():
        if SLOT_2:
            if (SLOT_19 < 520000):
                Unknown2037(0)
                sendToLabel(3)
    sprite('mk030_00', 5)	# 129-133
    physicsXImpulse(4650)
    sprite('mk030_01', 6)	# 134-139
    label(2)
    sprite('mk030_02', 6)	# 140-145
    sprite('mk030_03', 6)	# 146-151
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk030_04', 6)	# 152-157
    sprite('mk030_05', 6)	# 158-163
    sprite('mk030_06', 6)	# 164-169
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(2)
    label(3)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventRLvsMKAction():
    sprite('mk000_00', 7)	# 1-7
    sprite('mk000_01', 7)	# 8-14
    sprite('mk000_02', 7)	# 15-21
    sprite('mk000_03', 7)	# 22-28
    sprite('mk031_00', 7)	# 29-35
    physicsXImpulse(-1000)
    sprite('mk031_01', 7)	# 36-42
    sprite('mk031_02', 7)	# 43-49
    sprite('mk031_03', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk031_04', 7)	# 57-63
    sprite('mk031_05', 7)	# 64-70
    sprite('mk031_06', 7)	# 71-77
    sprite('mk031_07', 7)	# 78-84
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('mk031_08', 7)	# 85-91
    loopRest()
    enterState('CmnActStand')

@State
def EventVsTKEntry01EX():
    sprite('mk603_00', 32767)	# 1-32767

@State
def EventVsTKEntry02EX():
    sprite('mk603_01', 9)	# 1-9
    sprite('mk603_02', 6)	# 10-15
    sprite('mk603_03', 6)	# 16-21
    sprite('mk603_04', 6)	# 22-27
    sprite('mk603_05', 6)	# 28-33
    sprite('mk603_06', 6)	# 34-39
    sprite('mk603_07', 6)	# 40-45
    sprite('mk603_08', 6)	# 46-51
    SFX_0('cloth_m')
    sprite('mk603_09', 6)	# 52-57
    sprite('mk600_10', 6)	# 58-63
    GFX_0('EntryMant2', 0)
    sprite('mk600_11', 6)	# 64-69
    sprite('mk600_12', 6)	# 70-75
    sprite('mk600_13', 6)	# 76-81
    sprite('mk600_14', 6)	# 82-87
    sprite('mk600_15', 6)	# 88-93
    sprite('mk600_16', 6)	# 94-99
    loopRest()
    enterState('CmnActStand')

@State
def EventDashStraight():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1000(-800000)
        Unknown3029(1)
        Unknown3069(0)
    sprite('mk404_04', 2)	# 1-2
    Unknown7014('mkse_00')
    physicsXImpulse(10000)
    sprite('mk413_00', 2)	# 3-4
    physicsXImpulse(8000)
    sprite('mk413_01', 2)	# 5-6
    SLOT_55 = 1
    GFX_0('DriveChargeWind', 0)
    GFX_0('DriveChargeAura', 0)
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 7-9
    sprite('mk413_01', 3)	# 10-12
    physicsXImpulse(6000)
    sprite('mk413_02', 3)	# 13-15
    sprite('mk413_01', 3)	# 16-18
    GFX_0('DriveChargelightning', 0)
    sprite('mk413_02', 3)	# 19-21
    sprite('mk413_01', 3)	# 22-24
    sprite('mk413_02', 3)	# 25-27
    sprite('keep', 1)	# 28-28
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    callSubroutine('AfterImage_Lv3')
    sprite('mk413_04', 3)	# 29-31
    Unknown7015()
    SFX_3('mkse_03')
    Unknown2015(150)
    physicsXImpulse(50000)
    Unknown8007(100, 1, 1)
    sprite('mk413_05', 3)	# 32-34	 **attackbox here**
    Unknown1019(40)
    ScreenShake(0, 35000)
    GFX_0('mkef413_lv3', -1)
    GFX_1('mkef_Lv3Puncheairwall', 0)
    sprite('mk413_05', 3)	# 35-37	 **attackbox here**
    Unknown21007(22, 32)
    sprite('mk413_06', 4)	# 38-41
    Unknown1019(30)
    Unknown2015(-1)
    Unknown8010(100, 1, 1)
    sprite('mk413_07', 4)	# 42-45
    Unknown8010(100, 1, 1)
    sprite('mk404_12', 3)	# 46-48
    sprite('mk404_13', 3)	# 49-51
    Unknown1084(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def EventVsMKExciteLoop():
    sprite('mk611_00', 6)	# 1-6
    sprite('mk611_01', 6)	# 7-12
    sprite('mk611_02', 6)	# 13-18
    sprite('mk611_03', 6)	# 19-24
    sprite('mk601_00', 6)	# 25-30
    sprite('mk601_00', 6)	# 31-36
    sprite('mk601_01', 6)	# 37-42
    sprite('mk601_02', 4)	# 43-46
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    sprite('mk601_03', 6)	# 47-52
    sprite('mk601_04', 6)	# 53-58
    sprite('mk601_05', 6)	# 59-64
    sprite('mk601_06', 6)	# 65-70
    sprite('mk601_07', 4)	# 71-74
    SFX_0('008_swing_pole_0')
    sprite('mk601_08', 4)	# 75-78
    sprite('mk601_09', 4)	# 79-82
    SFX_0('008_swing_pole_0')
    sprite('mk601_10', 4)	# 83-86
    sprite('mk601_11', 8)	# 87-94
    SFX_0('008_swing_pole_1')
    sprite('mk601_12', 6)	# 95-100
    sprite('mk601_13', 32767)	# 101-32867

@State
def EventVsMKExciteLoopEnd():
    sprite('mk601_14', 6)	# 1-6
    sprite('mk601_15', 6)	# 7-12
    loopRest()
    enterState('CmnActStand')

@State
def EventVsMULose():
    sprite('mk070_06', 32767)	# 1-32767

@State
def EventVsMULoseDown():
    sprite('mk070_07', 6)	# 1-6
    sprite('mk070_08', 6)	# 7-12
    sprite('mk070_09', 6)	# 13-18
    sprite('mk063_11', 32767)	# 19-32785
    teleportRelativeX(130000)

@State
def Act2Event_Yoroke():
    sprite('mk070_02', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_YorokeEnd():
    sprite('mk070_02', 6)	# 1-6
    sprite('mk070_03', 6)	# 7-12
    sprite('mk070_10', 6)	# 13-18
    sprite('mk070_11', 6)	# 19-24
    sprite('mk070_12', 6)	# 25-30
    sprite('mk070_13', 6)	# 31-36
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Posing():
    sprite('mk450_00', 4)	# 1-4
    sprite('mk450_01', 4)	# 5-8
    sprite('mk450_02', 3)	# 9-11
    teleportRelativeX(20000)
    sprite('mk450_03', 3)	# 12-14
    teleportRelativeX(20000)
    sprite('mk450_04', 3)	# 15-17
    teleportRelativeX(20000)
    sprite('mk450_05', 3)	# 18-20
    teleportRelativeX(20000)
    sprite('mk450_06', 3)	# 21-23
    label(0)
    sprite('mk450_07', 4)	# 24-27
    sprite('mk450_08', 4)	# 28-31
    loopRest()
    gotoLabel(0)

@State
def Act2Event_PosingEnd():
    sprite('keep', 2)	# 1-2
    sprite('mk450_06', 3)	# 3-5
    sprite('mk450_05', 3)	# 6-8
    teleportRelativeX(-20000)
    sprite('mk450_04', 3)	# 9-11
    teleportRelativeX(-20000)
    sprite('mk450_03', 3)	# 12-14
    teleportRelativeX(-20000)
    sprite('mk450_02', 3)	# 15-17
    teleportRelativeX(-20000)
    sprite('mk450_01', 4)	# 18-21
    sprite('mk450_00', 4)	# 22-25
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ntvsmk_00():
    sprite('null', 32767)	# 1-32767

@State
def Act2Event_ntvsmk_01():
    sprite('mk603_00', 32767)	# 1-32767

@State
def Act2Event_ntvsmk_02():
    sprite('mk603_01', 9)	# 1-9
    sprite('mk603_02', 6)	# 10-15
    sprite('mk603_03', 6)	# 16-21
    sprite('mk603_04', 6)	# 22-27
    sprite('mk603_05', 6)	# 28-33
    sprite('mk603_06', 6)	# 34-39
    sprite('mk603_07', 6)	# 40-45
    sprite('mk603_08', 6)	# 46-51
    SFX_0('019_cloth_b')
    sprite('mk603_09', 6)	# 52-57
    sprite('mk600_10', 6)	# 58-63
    GFX_0('EntryMant2', 0)
    sprite('mk600_11', 6)	# 64-69
    sprite('mk600_12', 6)	# 70-75
    sprite('mk600_13', 6)	# 76-81
    sprite('mk600_14', 6)	# 82-87
    sprite('mk600_15', 6)	# 88-93
    sprite('mk600_16', 6)	# 94-99
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ntvsmk_03():
    sprite('mk430_00', 4)	# 1-4
    sprite('mk430_01', 4)	# 5-8
    sprite('mk430_02', 4)	# 9-12
    sprite('mk430_03', 4)	# 13-16
    sprite('mk430_04', 3)	# 17-19
    sprite('mk430_05', 3)	# 20-22
    label(0)
    sprite('mk430_04', 3)	# 23-25
    GFX_0('DriveChargelightning', 0)
    sprite('mk430_05', 3)	# 26-28
    sprite('mk430_04', 3)	# 29-31
    sprite('mk430_05', 3)	# 32-34
    GFX_0('DriveChargelightning', 0)
    loopRest()
    gotoLabel(0)

@State
def Act2Event_ntvsmk_04():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('mk430_06', 5)	# 1-5
    sprite('mk430_07', 5)	# 6-10
    sprite('mk430_08', 5)	# 11-15
    sprite('mk430_09', 5)	# 16-20
    sprite('mk430_10', 7)	# 21-27
    GFX_0('mkef_circle_middle', 1)
    GFX_0('mkef_circle_large', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 7)	# 28-34
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_430circlering_lv3', 1)
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk430_12', 4)	# 35-38
    ScreenShake(8000, 0)
    Unknown21007(22, 32)
    sprite('mk430_13', 4)	# 39-42
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 3)	# 43-45	 **attackbox here**
    GFX_0('Event_mk430cutin_lv3', -1)
    GFX_0('DriveLv3PunchefD', 1)
    GFX_0('mkef_jumpsmoke23', 2)
    ScreenShake(0, 35000)
    callSubroutine('AfterImage_Lv3')
    sprite('mk430_15', 3)	# 46-48	 **attackbox here**
    sprite('mk430_14', 3)	# 49-51	 **attackbox here**
    sprite('mk430_15', 3)	# 52-54	 **attackbox here**
    sprite('mk430_14', 3)	# 55-57	 **attackbox here**
    sprite('mk430_15', 3)	# 58-60	 **attackbox here**
    sprite('mk430_14', 4)	# 61-64	 **attackbox here**
    sprite('mk430_15', 4)	# 65-68	 **attackbox here**
    sprite('mk430_14', 5)	# 69-73	 **attackbox here**
    sprite('mk430_15', 5)	# 74-78	 **attackbox here**
    sprite('mk430_16', 5)	# 79-83	 **attackbox here**
    sprite('mk430_17', 5)	# 84-88
    sprite('mk430_18', 5)	# 89-93
    sprite('mk430_19', 5)	# 94-98
    sprite('mk430_20', 5)	# 99-103
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_ntvsmk_05():

    def upon_IMMEDIATE():
        Unknown2034(0)
        sendToLabelUpon(2, 1)
    sprite('mk023_00', 4)	# 1-4
    sprite('mk023_01', 4)	# 5-8
    sprite('mk411_00', 4)	# 9-12
    Unknown21007(22, 32)
    Unknown8001(3, 100)
    physicsXImpulse(-18000)
    physicsYImpulse(32000)
    setGravity(1800)
    sprite('mk411_01', 4)	# 13-16
    sprite('mk411_02', 3)	# 17-19
    sprite('mk411_03', 3)	# 20-22
    sprite('mk411_04', 3)	# 23-25
    sprite('mk411_05', 3)	# 26-28
    sprite('mk411_03', 3)	# 29-31
    sprite('mk411_04', 3)	# 32-34
    sprite('mk411_05', 3)	# 35-37
    label(0)
    sprite('mk411_15', 2)	# 38-39
    sprite('mk411_16', 2)	# 40-41
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)	# 42-51
    Unknown3038(1)
    Unknown1084(1)
    loopRest()

@State
def Act2Event_kgvsmk_00():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        sendToLabelUpon(2, 0)
    sprite('mk415_00', 3)	# 1-3
    sprite('mk415_01', 3)	# 4-6
    sprite('mk415_02', 4)	# 7-10
    sprite('mk415_03', 5)	# 11-15
    sprite('mk415_04', 5)	# 16-20
    sprite('mk415_05', 3)	# 21-23
    sprite('mk415_06', 2)	# 24-25
    sprite('mk415_07', 2)	# 26-27
    sprite('mk415_08', 2)	# 28-29
    sprite('mk415_09', 2)	# 30-31
    SFX_0('003_swing_grap_0_2')
    sprite('mk415_10', 20)	# 32-51	 **attackbox here**
    GFX_0('mkef_415_punch', 0)
    GFX_1('mkef_415smoke', -1)
    SFX_3('mkse_03')
    Unknown21007(22, 32)
    sprite('mk415_11', 2)	# 52-53
    sprite('mk415_12', 2)	# 54-55
    sprite('mk415_13', 3)	# 56-58
    sprite('mk415_14', 3)	# 59-61
    sprite('mk415_15', 3)	# 62-64
    sprite('mk415_16', 5)	# 65-69
    sprite('mk415_17', 4)	# 70-73
    sprite('mk415_18', 4)	# 74-77
    sprite('mk033_00', 1)	# 78-78
    Unknown2004(0, 0)
    Unknown1000(-66000)
    sprite('mk033_01', 2)	# 79-80
    physicsXImpulse(-12000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('mk033_02', 2)	# 81-82
    sprite('mk033_02', 1)	# 83-83
    sprite('mk033_03', 3)	# 84-86
    loopRest()
    label(9)
    sprite('mk033_02', 3)	# 87-89
    sprite('mk033_03', 3)	# 90-92
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('mk033_04', 3)	# 93-95
    Unknown1084(1)
    Unknown1000(-260000)
    Unknown8000(100, 1, 1)
    sprite('mk033_05', 3)	# 96-98
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_kgvsmk_01():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('mk430_06', 5)	# 1-5
    sprite('mk430_07', 5)	# 6-10
    sprite('mk430_08', 5)	# 11-15
    sprite('mk430_09', 5)	# 16-20
    sprite('mk430_10', 7)	# 21-27
    GFX_0('mkef_circle_middle', 1)
    GFX_0('mkef_circle_large', 2)
    ScreenShake(4000, 0)
    sprite('mk430_11', 7)	# 28-34
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_mahojin_large', 1)
    GFX_0('mkef_430circlering_lv3', 1)
    GFX_0('DriveChargelightning', 0)
    ScreenShake(6000, 0)
    sprite('mk430_12', 4)	# 35-38
    ScreenShake(8000, 0)
    sprite('mk430_13', 4)	# 39-42
    SFX_3('mkse_04')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    ScreenShake(10000, 0)
    sprite('mk430_14', 25)	# 43-67	 **attackbox here**
    Unknown21007(22, 32)
    GFX_0('Event_mk430cutin_lv3', -1)
    GFX_0('DriveLv3PunchefD', 1)
    GFX_0('mkef_jumpsmoke23', 2)
    ScreenShake(0, 35000)
    sprite('mk430_15', 3)	# 68-70	 **attackbox here**
    sprite('mk430_14', 3)	# 71-73	 **attackbox here**
    sprite('mk430_15', 3)	# 74-76	 **attackbox here**
    sprite('mk430_14', 3)	# 77-79	 **attackbox here**
    sprite('mk430_15', 3)	# 80-82	 **attackbox here**
    sprite('mk430_14', 4)	# 83-86	 **attackbox here**
    sprite('mk430_15', 4)	# 87-90	 **attackbox here**
    sprite('keep', 1)	# 91-91
    Unknown3029(0)
    label(9)
    sprite('mk430_14', 5)	# 92-96	 **attackbox here**
    sprite('mk430_15', 5)	# 97-101	 **attackbox here**
    loopRest()
    gotoLabel(9)

@State
def Act2Event_kgvsmk_02():

    def upon_IMMEDIATE():
        Unknown1000(-180000)
    sprite('keep', 1)	# 1-1
    loopRest()
    enterState('Act2Event_Yoroke')

@State
def Act2Event_mkvsmi_00():
    sprite('mk620_00', 6)	# 1-6
    sprite('mk620_01', 6)	# 7-12
    sprite('mk620_02', 32767)	# 13-32779
    loopRest()

@State
def Act2Event_mkvsmi_01():
    sprite('keep', 6)	# 1-6
    sprite('mk620_01', 6)	# 7-12
    sprite('mk620_00', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_mkvsmi_02():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        sendToLabelUpon(2, 0)
    sprite('mk415_00', 3)	# 1-3
    sprite('mk415_01', 3)	# 4-6
    sprite('mk415_02', 4)	# 7-10
    sprite('mk415_03', 5)	# 11-15
    sprite('mk415_04', 5)	# 16-20
    sprite('mk415_05', 3)	# 21-23
    sprite('mk415_06', 2)	# 24-25
    sprite('mk415_07', 2)	# 26-27
    sprite('mk415_08', 2)	# 28-29
    sprite('mk415_09', 2)	# 30-31
    SFX_0('003_swing_grap_0_2')
    sprite('mk415_10', 3)	# 32-34	 **attackbox here**
    GFX_0('mkef_415_punch', 0)
    GFX_1('mkef_415smoke', -1)
    SFX_3('mkse_03')
    sprite('mk415_11', 2)	# 35-36
    sprite('mk415_12', 2)	# 37-38
    sprite('mk415_13', 3)	# 39-41
    sprite('mk415_14', 3)	# 42-44
    sprite('mk415_15', 3)	# 45-47
    sprite('mk415_16', 5)	# 48-52
    sprite('mk415_17', 4)	# 53-56
    sprite('mk415_18', 4)	# 57-60
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_mkvstb_00():

    def upon_IMMEDIATE():
        Unknown2005()
    label(0)
    sprite('mk000_00', 5)	# 1-5
    sprite('mk000_01', 5)	# 6-10
    sprite('mk000_02', 6)	# 11-16
    sprite('mk000_03', 6)	# 17-22
    sprite('mk000_04', 5)	# 23-27
    sprite('mk000_05', 5)	# 28-32
    sprite('mk000_06', 6)	# 33-38
    sprite('mk000_07', 6)	# 39-44
    sprite('mk000_08', 5)	# 45-49
    sprite('mk000_09', 5)	# 50-54
    loopRest()
    gotoLabel(0)

@State
def Act2Event_mkvstb_01():
    sprite('keep', 2)	# 1-2
    sprite('mk003_00', 5)	# 3-7
    Unknown2005()
    sprite('mk003_01', 5)	# 8-12
    sprite('mk003_02', 5)	# 13-17
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_mkvstb_02():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('keep', 2)	# 1-2
    sprite('mk003_00', 5)	# 3-7
    Unknown2005()
    sprite('mk003_01', 5)	# 8-12
    sprite('mk003_02', 5)	# 13-17
    sprite('mk032_00', 3)	# 18-20
    sprite('mk032_01', 3)	# 21-23
    physicsXImpulse(24000)
    sprite('mk032_02', 4)	# 24-27
    sprite('mk032_03', 4)	# 28-31
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 32-35
    sprite('mk032_05', 4)	# 36-39
    sprite('mk032_06', 4)	# 40-43
    sprite('mk032_07', 4)	# 44-47
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 48-50
    sprite('mk032_01', 2)	# 51-52
    sprite('mk032_02', 4)	# 53-56
    sprite('mk032_03', 4)	# 57-60
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 61-64
    sprite('mk032_05', 4)	# 65-68
    sprite('mk032_06', 4)	# 69-72
    sprite('mk032_07', 4)	# 73-76
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 77-79
    sprite('mk032_01', 2)	# 80-81
    sprite('mk032_02', 4)	# 82-85
    sprite('mk032_03', 4)	# 86-89
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 90-93
    sprite('mk032_05', 4)	# 94-97
    sprite('mk032_06', 4)	# 98-101
    sprite('mk032_07', 4)	# 102-105
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 106-108
    sprite('null', 32767)	# 109-32875
    Unknown1084(1)
    Unknown3038(1)
    loopRest()

@State
def Act2Event_Reaction1():
    sprite('mk000_27', 6)	# 1-6
    sprite('mk000_28', 6)	# 7-12
    sprite('mk000_29', 6)	# 13-18
    sprite('mk000_30', 6)	# 19-24
    Unknown8002()
    sprite('mk000_31', 6)	# 25-30
    sprite('mk000_32', 6)	# 31-36
    sprite('mk000_33', 6)	# 37-42
    sprite('mk000_34', 6)	# 43-48
    Unknown8002()
    sprite('mk000_35', 6)	# 49-54
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Komari():
    sprite('mk620_00', 6)	# 1-6
    sprite('mk620_01', 6)	# 7-12
    sprite('mk620_02', 32767)	# 13-32779
    loopRest()

@State
def Act2Event_KomariEnd():
    sprite('keep', 6)	# 1-6
    sprite('mk620_01', 6)	# 7-12
    sprite('mk620_00', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_Kurukuru():
    sprite('mk601_05', 6)	# 1-6
    sprite('mk601_06', 6)	# 7-12
    sprite('mk601_07', 4)	# 13-16
    SFX_0('008_swing_pole_0')
    sprite('mk601_08', 4)	# 17-20
    sprite('mk601_09', 4)	# 21-24
    SFX_0('008_swing_pole_0')
    sprite('mk601_10', 4)	# 25-28
    sprite('mk601_11', 8)	# 29-36
    SFX_0('008_swing_pole_1')
    sprite('mk601_12', 6)	# 37-42
    sprite('mk601_13', 40)	# 43-82
    sprite('mk601_14', 6)	# 83-88
    sprite('mk601_15', 6)	# 89-94
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_WalkIn():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1000(-720000)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 260000):
                    clearUponHandler(3)
                    Unknown1000(-260000)
                    Unknown1084(1)
                    sendToLabel(0)
            elif (SLOT_22 > (-260000)):
                clearUponHandler(3)
                Unknown1000(-260000)
                Unknown1084(1)
                sendToLabel(0)
    sprite('mk030_00', 6)	# 1-6
    physicsXImpulse(4650)
    sprite('mk030_01', 6)	# 7-12
    label(9)
    sprite('mk030_02', 6)	# 13-18
    sprite('mk030_03', 6)	# 19-24
    sprite('mk030_04', 6)	# 25-30
    sprite('mk030_05', 6)	# 31-36
    sprite('mk030_06', 6)	# 37-42
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)	# 43-43
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventEntryFDashIn():
    Unknown2017(0)
    Unknown2034(0)
    Unknown1000(-1280000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 400000):
                sendToLabel(1)
        elif (SLOT_22 > (-400000)):
            sendToLabel(1)
    sprite('mk032_01', 1)	# 1-1
    physicsXImpulse(21000)
    Unknown1028(200)
    label(0)
    sprite('mk032_01', 2)	# 2-3
    sprite('mk032_02', 4)	# 4-7
    sprite('mk032_03', 4)	# 8-11
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 12-15
    sprite('mk032_05', 4)	# 16-19
    sprite('mk032_06', 4)	# 20-23
    sprite('mk032_07', 4)	# 24-27
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 28-30
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('mk032_09', 3)	# 31-33
    teleportRelativeX(20000)
    Unknown1019(70)
    sprite('mk032_09', 3)	# 34-36
    Unknown1019(70)
    sprite('mk032_09', 3)	# 37-39
    Unknown1019(70)
    sprite('mk032_09', 3)	# 40-42
    Unknown1019(70)
    sprite('mk024_00', 3)	# 43-45
    Unknown1084(1)
    Unknown1000(-260000)
    sprite('mk024_00', 2)	# 46-47
    sprite('mk024_01', 2)	# 48-49
    sprite('mk024_02', 2)	# 50-51
    sprite('mk024_03', 2)	# 52-53
    sprite('mk024_04', 2)	# 54-55
    enterState('CmnActStand')

@State
def Act2EvenFDashOutOpposite():
    Unknown2017(0)
    Unknown2034(0)
    Unknown2006()
    Unknown2005()
    sprite('mk032_00', 2)	# 1-2
    SLOT_51 = 0
    label(0)
    sprite('mk032_01', 2)	# 3-4
    physicsXImpulse(21000)
    Unknown1028(200)
    sprite('mk032_02', 4)	# 5-8
    sprite('mk032_03', 4)	# 9-12
    if (SLOT_51 <= 4):
        Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 13-16
    sprite('mk032_05', 4)	# 17-20
    sprite('mk032_06', 4)	# 21-24
    sprite('mk032_07', 4)	# 25-28
    if (SLOT_51 <= 4):
        Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 29-31
    loopRest()
    SLOT_51 = (SLOT_51 + 1)
    gotoLabel(0)

@State
def Act2Event_mkvsrl_00():
    sprite('mk620_00', 7)	# 1-7
    sprite('mk620_01', 7)	# 8-14
    sprite('mk620_02', 7)	# 15-21
    sprite('mk620_03', 7)	# 22-28
    sprite('mk620_04', 7)	# 29-35
    Unknown8000(100, 1, 1)
    sprite('mk620_05', 7)	# 36-42
    sprite('mk620_06', 32767)	# 43-32809
    loopRest()

@State
def Act2Event_mkvsrl_01():
    sprite('keep', 6)	# 1-6
    sprite('mk064_04', 4)	# 7-10
    sprite('mk064_05', 4)	# 11-14
    sprite('mk064_06', 4)	# 15-18
    sprite('mk064_07', 4)	# 19-22
    sprite('mk064_08', 4)	# 23-26
    sprite('mk064_09', 4)	# 27-30
    sprite('mk064_10', 4)	# 31-34
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_mkvsrl_02():
    sprite('keep', 6)	# 1-6
    sprite('mk064_04', 4)	# 7-10
    sprite('mk064_05', 4)	# 11-14
    sprite('mk064_06', 4)	# 15-18
    sprite('mk064_07', 4)	# 19-22
    sprite('mk064_08', 4)	# 23-26
    sprite('mk064_09', 4)	# 27-30
    sprite('mk064_10', 4)	# 31-34
    loopRest()
    label(0)
    sprite('mk000_00', 6)	# 35-40
    sprite('mk000_01', 6)	# 41-46
    sprite('mk000_02', 7)	# 47-53
    sprite('mk000_03', 7)	# 54-60
    sprite('mk000_04', 6)	# 61-66
    sprite('mk000_05', 6)	# 67-72
    sprite('mk000_06', 7)	# 73-79
    sprite('mk000_07', 7)	# 80-86
    sprite('mk000_08', 6)	# 87-92
    sprite('mk000_09', 6)	# 93-98
    loopRest()
    gotoLabel(0)

@State
def Act3Event_rgvsmk_00():
    sprite('mk300_00', 6)	# 1-6
    sprite('mk300_01', 6)	# 7-12
    sprite('mk300_02', 6)	# 13-18
    sprite('mk300_03', 6)	# 19-24
    sprite('mk300_04', 32767)	# 25-32791
    loopRest()

@State
def Act3Event_rgvsmk_01():
    sprite('mk300_05', 6)	# 1-6
    sprite('mk300_06', 6)	# 7-12
    sprite('mk300_07', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvsmk_02():
    sprite('mk611_00', 6)	# 1-6
    sprite('mk611_01', 6)	# 7-12
    sprite('mk611_02', 6)	# 13-18
    sprite('mk611_03', 6)	# 19-24
    sprite('mk611_04', 6)	# 25-30
    sprite('mk611_05', 32767)	# 31-32797
    loopRest()

@State
def Act3Event_rgvsmk_03():
    sprite('keep', 2)	# 1-2
    sprite('mk611_04', 6)	# 3-8
    sprite('mk611_03', 6)	# 9-14
    sprite('mk611_02', 6)	# 15-20
    sprite('mk611_01', 6)	# 21-26
    sprite('mk611_00', 6)	# 27-32
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_rgvsmk_04():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('mk000_00', 4)	# 1-4
    sprite('mk070_00', 12)	# 5-16
    GFX_1('ef_hitmd', 103)
    SFX_0('100_hit_grap_1')
    ScreenShake(1000, 20000)
    sprite('mk070_00', 4)	# 17-20
    Unknown1047(-11000)
    sprite('mk070_01', 4)	# 21-24
    sprite('mk070_02', 4)	# 25-28
    sprite('mk070_03', 32767)	# 29-32795
    loopRest()

@State
def Act3Event_rgvsmk_05():
    sprite('keep', 2)	# 1-2
    sprite('mk070_10', 5)	# 3-7
    sprite('mk070_11', 5)	# 8-12
    sprite('mk070_12', 5)	# 13-17
    sprite('mk070_13', 5)	# 18-22
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsmk_00():

    def upon_IMMEDIATE():
        Unknown1000(-1200000)
        Unknown2034(0)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 360000):
                    sendToLabel(0)
                    clearUponHandler(3)
            elif (SLOT_22 > (-360000)):
                sendToLabel(0)
                clearUponHandler(3)
    sprite('mk032_00', 2)	# 1-2
    physicsXImpulse(20000)
    label(9)
    sprite('mk032_01', 2)	# 3-4
    sprite('mk032_02', 4)	# 5-8
    sprite('mk032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 13-16
    sprite('mk032_05', 4)	# 17-20
    sprite('mk032_06', 4)	# 21-24
    sprite('mk032_07', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 29-31
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('mk032_09', 6)	# 32-37
    physicsXImpulse(0)
    Unknown1045(10000)
    sprite('mk032_10', 4)	# 38-41
    Unknown1084(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsmk_01():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        sendToLabelUpon(2, 0)
    sprite('mk415_00', 3)	# 1-3
    sprite('mk415_01', 3)	# 4-6
    sprite('mk415_02', 4)	# 7-10
    sprite('mk415_03', 5)	# 11-15
    sprite('mk415_04', 5)	# 16-20
    sprite('mk415_05', 3)	# 21-23
    sprite('mk415_06', 2)	# 24-25
    sprite('mk415_07', 2)	# 26-27
    Unknown21007(22, 32)
    sprite('mk415_08', 2)	# 28-29
    sprite('mk415_09', 2)	# 30-31
    SFX_0('003_swing_grap_0_2')
    sprite('mk415_10', 20)	# 32-51	 **attackbox here**
    GFX_0('mkef_415_punch', 0)
    GFX_1('mkef_415smoke', -1)
    SFX_3('mkse_03')
    sprite('mk415_11', 2)	# 52-53
    sprite('mk415_12', 2)	# 54-55
    sprite('mk415_13', 3)	# 56-58
    sprite('mk415_14', 3)	# 59-61
    sprite('mk415_15', 3)	# 62-64
    sprite('mk415_16', 5)	# 65-69
    sprite('mk415_17', 4)	# 70-73
    sprite('mk415_18', 4)	# 74-77
    sprite('mk033_00', 1)	# 78-78
    Unknown2004(0, 0)
    Unknown1000(-66000)
    sprite('mk033_01', 2)	# 79-80
    physicsXImpulse(-12000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('mk033_02', 2)	# 81-82
    sprite('mk033_02', 1)	# 83-83
    sprite('mk033_03', 3)	# 84-86
    loopRest()
    label(9)
    sprite('mk033_02', 3)	# 87-89
    sprite('mk033_03', 3)	# 90-92
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('mk033_04', 3)	# 93-95
    Unknown1084(1)
    Unknown1000(-260000)
    Unknown8000(100, 1, 1)
    sprite('mk033_05', 3)	# 96-98
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_tgvsmk_02():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown1000(-260000)
    sprite('mk602_02', 7)	# 1-7
    sprite('mk602_01', 7)	# 8-14
    sprite('mk430_00', 6)	# 15-20
    sprite('mk601_01', 6)	# 21-26
    teleportRelativeX(-45000)
    sprite('mk601_00', 10)	# 27-36
    sprite('mk601_01', 2)	# 37-38
    sprite('mk601_02', 3)	# 39-41
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    ScreenShake(0, 10000)
    sprite('mk601_03', 6)	# 42-47
    sprite('mk601_04', 40)	# 48-87
    sprite('mk601_05', 6)	# 88-93
    sprite('mk601_15', 6)	# 94-99
    loopRest()
    enterState('Act2Event_Reaction1')

@State
def Act3Event_tgvsmk_03():
    sprite('mk070_04', 5)	# 1-5
    sprite('mk070_05', 5)	# 6-10
    sprite('mk070_06', 5)	# 11-15
    sprite('mk070_07', 5)	# 16-20
    sprite('mk070_08', 5)	# 21-25
    sprite('mk070_09', 5)	# 26-30
    sprite('mk063_11', 32767)	# 31-32797
    Unknown8000(100, 1, 0)
    SFX_0('209_down_normal_0')
    teleportRelativeX(110000)

@State
def Act3Event_tgvsmk_04():
    sprite('mk064_00', 4)	# 1-4
    sprite('mk064_01', 4)	# 5-8
    sprite('mk064_02', 4)	# 9-12
    sprite('mk064_03', 4)	# 13-16
    sprite('mk064_04', 4)	# 17-20
    sprite('mk064_05', 4)	# 21-24
    sprite('mk064_06', 4)	# 25-28
    sprite('mk064_07', 4)	# 29-32
    sprite('mk064_08', 4)	# 33-36
    sprite('mk064_09', 4)	# 37-40
    sprite('mk064_10', 4)	# 41-44
    loopRest()
    label(0)
    sprite('mk000_00', 5)	# 45-49
    sprite('mk000_01', 5)	# 50-54
    sprite('mk000_02', 6)	# 55-60
    sprite('mk000_03', 6)	# 61-66
    sprite('mk000_04', 5)	# 67-71
    sprite('mk000_05', 5)	# 72-76
    sprite('mk000_06', 6)	# 77-82
    sprite('mk000_07', 6)	# 83-88
    sprite('mk000_08', 5)	# 89-93
    sprite('mk000_09', 5)	# 94-98
    loopRest()
    gotoLabel(0)

@State
def Act3Event_tgvsmk_05():
    sprite('keep', 2)	# 1-2
    sprite('mk003_00', 5)	# 3-7
    Unknown2005()
    sprite('mk003_01', 5)	# 8-12
    sprite('mk003_02', 5)	# 13-17
    label(0)
    sprite('mk000_00', 5)	# 18-22
    sprite('mk000_01', 5)	# 23-27
    sprite('mk000_02', 6)	# 28-33
    sprite('mk000_03', 6)	# 34-39
    sprite('mk000_04', 5)	# 40-44
    sprite('mk000_05', 5)	# 45-49
    sprite('mk000_06', 6)	# 50-55
    sprite('mk000_07', 6)	# 56-61
    sprite('mk000_08', 5)	# 62-66
    sprite('mk000_09', 5)	# 67-71
    loopRest()
    gotoLabel(0)

@State
def Act3Event_hzvsmk_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('mk000_00', 7)	# 1-7
    sprite('mk070_00', 19)	# 8-26
    Unknown4052()
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_2')
    ScreenShake(1000, 20000)
    sprite('mk070_00', 4)	# 27-30
    Unknown1047(-11000)
    sprite('mk070_01', 4)	# 31-34
    sprite('mk070_02', 4)	# 35-38
    sprite('mk070_03', 32767)	# 39-32805
    loopRest()

@State
def Act3Event_mkvstg_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1000(-720000)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 160000):
                    clearUponHandler(3)
                    Unknown1000(-160000)
                    Unknown1084(1)
                    sendToLabel(0)
            elif (SLOT_22 > (-160000)):
                clearUponHandler(3)
                Unknown1000(-160000)
                Unknown1084(1)
                sendToLabel(0)
    sprite('mk030_00', 6)	# 1-6
    physicsXImpulse(4650)
    sprite('mk030_01', 6)	# 7-12
    label(9)
    sprite('mk030_02', 6)	# 13-18
    sprite('mk030_03', 6)	# 19-24
    sprite('mk030_04', 6)	# 25-30
    sprite('mk030_05', 6)	# 31-36
    sprite('mk030_06', 6)	# 37-42
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)	# 43-43
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mkvstg_01():

    def upon_IMMEDIATE():

        def upon_LANDING():
            sendToLabel(0)
            Unknown1084(1)
            Unknown1000(-260000)
            Unknown8000(100, 1, 1)
    sprite('mk033_00', 3)	# 1-3
    sprite('mk033_01', 2)	# 4-5
    physicsXImpulse(-10000)
    physicsYImpulse(7500)
    Unknown1043()
    Unknown8002()
    sprite('mk033_02', 3)	# 6-8
    sprite('mk033_03', 3)	# 9-11
    loopRest()
    label(9)
    sprite('mk033_02', 3)	# 12-14
    sprite('mk033_03', 3)	# 15-17
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('mk033_04', 3)	# 18-20
    sprite('mk033_05', 3)	# 21-23
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mkvstg_02():

    def upon_IMMEDIATE():
        Unknown2003(1)
        Unknown2004(1, 0)
    sprite('mk203_04', 3)	# 1-3
    teleportRelativeX(50000)
    physicsXImpulse(10000)
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    sprite('mk203_05', 2)	# 4-5
    Unknown8007(100, 1, 1)
    SFX_3('mkse_03')
    sprite('mk203_06', 2)	# 6-7
    sprite('mk203_07', 16)	# 8-23	 **attackbox here**
    Unknown1084(1)
    sprite('mk203_08', 3)	# 24-26
    sprite('mk203_09', 4)	# 27-30
    sprite('mk203_10', 3)	# 31-33
    sprite('mk203_10ex00', 3)	# 34-36
    sprite('mk203_11', 4)	# 37-40
    sprite('mk203_12', 4)	# 41-44
    sprite('mk203_13', 4)	# 45-48
    sprite('mk203_14', 4)	# 49-52
    sprite('mk203_15', 4)	# 53-56
    sprite('mk203_16', 8)	# 57-64
    sprite('mk203_17', 4)	# 65-68
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mkvskk_00():
    sprite('mk620_00', 6)	# 1-6
    sprite('mk620_01', 6)	# 7-12
    sprite('mk620_02', 30)	# 13-42
    sprite('mk620_01', 6)	# 43-48
    sprite('mk620_00', 6)	# 49-54
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mkvskk_01():
    sprite('mk000_10', 4)	# 1-4
    sprite('mk000_11', 7)	# 5-11
    sprite('mk000_12', 7)	# 12-18
    sprite('mk000_13', 4)	# 19-22
    sprite('mk000_14', 5)	# 23-27
    sprite('mk000_15', 5)	# 28-32
    Unknown8002()
    sprite('mk000_11', 7)	# 33-39
    sprite('mk000_12', 7)	# 40-46
    sprite('mk000_13', 4)	# 47-50
    sprite('mk000_14', 5)	# 51-55
    sprite('mk000_15', 5)	# 56-60
    Unknown8002()
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mkvskg_00():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown1000(-260000)
    sprite('mk602_01', 7)	# 1-7
    sprite('mk430_00', 6)	# 8-13
    sprite('mk601_01', 6)	# 14-19
    teleportRelativeX(-45000)
    sprite('mk601_00', 10)	# 20-29
    sprite('mk601_01', 2)	# 30-31
    sprite('mk601_02', 3)	# 32-34
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    ScreenShake(0, 10000)
    sprite('mk601_03', 6)	# 35-40
    sprite('mk601_04', 40)	# 41-80
    sprite('mk601_05', 6)	# 81-86
    sprite('mk601_15', 6)	# 87-92
    loopRest()
    enterState('Act2Event_Reaction1')

@State
def Act3Event_mkvskg_01():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
    sprite('mk430_15', 6)	# 1-6	 **attackbox here**
    sprite('mk430_16', 6)	# 7-12	 **attackbox here**
    sprite('mk430_17', 6)	# 13-18
    sprite('mk430_18', 6)	# 19-24
    sprite('mk430_19', 6)	# 25-30
    sprite('mk430_20', 6)	# 31-36
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mkvsiz_00():

    def upon_IMMEDIATE():
        GFX_0('Act3Event_Noel', -1)
        Unknown38(11, 1)
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('Act2Event_NoDisp')

@State
def Act3Event_mkvsiz_01():

    def upon_IMMEDIATE():
        Unknown1000(-1200000)
        Unknown2034(0)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 310000):
                    sendToLabel(0)
                    clearUponHandler(3)
            elif (SLOT_22 > (-310000)):
                sendToLabel(0)
                clearUponHandler(3)
    sprite('mk032_00', 2)	# 1-2
    physicsXImpulse(20000)
    label(9)
    sprite('mk032_01', 2)	# 3-4
    sprite('mk032_02', 4)	# 5-8
    sprite('mk032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('mk032_04', 4)	# 13-16
    sprite('mk032_05', 4)	# 17-20
    sprite('mk032_06', 4)	# 21-24
    sprite('mk032_07', 4)	# 25-28
    Unknown8006(100, 1, 1)
    sprite('mk032_08', 3)	# 29-31
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('mk032_09', 6)	# 32-37
    physicsXImpulse(0)
    Unknown1047(10000)
    sprite('mk032_10', 4)	# 38-41
    sprite('mk040_00', 3)	# 42-44
    sprite('mk040_01', 3)	# 45-47
    Unknown21007(22, 32)
    sprite('mk040_02', 16)	# 48-63
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('mk040_03', 4)	# 64-67
    Unknown1047(-10000)
    sprite('mk040_04', 4)	# 68-71
    sprite('mk040_01', 4)	# 72-75
    sprite('mk040_00', 4)	# 76-79
    Unknown1084(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mkvsiz_02():

    def upon_IMMEDIATE():
        loopRelated(17, 90)

        def upon_17():
            clearUponHandler(17)
            Unknown21007(11, 32)

        def upon_STATE_END():
            clearUponHandler(17)
            Unknown21007(11, 32)
    sprite('mk450_00', 4)	# 1-4
    sprite('mk450_01', 4)	# 5-8
    sprite('mk450_02', 3)	# 9-11
    teleportRelativeX(20000)
    sprite('mk450_03', 3)	# 12-14
    teleportRelativeX(20000)
    sprite('mk450_04', 3)	# 15-17
    teleportRelativeX(20000)
    sprite('mk450_05', 3)	# 18-20
    teleportRelativeX(20000)
    label(0)
    sprite('mk450_06', 4)	# 21-24
    sprite('mk450_07', 4)	# 25-28
    sprite('mk450_08', 4)	# 29-32
    loopRest()
    gotoLabel(0)

@State
def Act3Event_Posing():
    sprite('mk450_00', 4)	# 1-4
    sprite('mk450_01', 4)	# 5-8
    sprite('mk450_02', 3)	# 9-11
    teleportRelativeX(20000)
    sprite('mk450_03', 3)	# 12-14
    teleportRelativeX(20000)
    sprite('mk450_04', 3)	# 15-17
    teleportRelativeX(20000)
    sprite('mk450_05', 3)	# 18-20
    teleportRelativeX(20000)
    label(0)
    sprite('mk450_06', 4)	# 21-24
    sprite('mk450_07', 4)	# 25-28
    sprite('mk450_08', 4)	# 29-32
    loopRest()
    gotoLabel(0)

@State
def Act3Event_PosingEnd():
    sprite('keep', 2)	# 1-2
    sprite('mk450_05', 3)	# 3-5
    teleportRelativeX(-20000)
    sprite('mk450_04', 3)	# 6-8
    teleportRelativeX(-20000)
    sprite('mk450_03', 3)	# 9-11
    teleportRelativeX(-20000)
    sprite('mk450_02', 3)	# 12-14
    teleportRelativeX(-20000)
    sprite('mk450_01', 4)	# 15-18
    sprite('mk450_00', 4)	# 19-22
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_EntryPoncho():
    sprite('mk600_00', 32767)	# 1-32767

@State
def Act3Event_EntryNugi():
    sprite('mk600_01', 9)	# 1-9
    sprite('mk600_02', 6)	# 10-15
    sprite('mk600_03', 6)	# 16-21
    sprite('mk600_04', 6)	# 22-27
    sprite('mk600_05', 6)	# 28-33
    sprite('mk600_06', 6)	# 34-39
    sprite('mk600_07', 6)	# 40-45
    sprite('mk600_08', 6)	# 46-51
    SFX_0('019_cloth_b')
    sprite('mk600_09', 6)	# 52-57
    sprite('mk600_10', 6)	# 58-63
    GFX_0('EntryMant', 0)
    sprite('mk600_11', 6)	# 64-69
    sprite('mk600_12', 6)	# 70-75
    sprite('mk600_13', 6)	# 76-81
    sprite('mk600_14', 6)	# 82-87
    sprite('mk600_15', 6)	# 88-93
    sprite('mk600_16', 6)	# 94-99
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Excite():
    sprite('mk300_00', 6)	# 1-6
    sprite('mk300_01', 6)	# 7-12
    sprite('mk300_02', 6)	# 13-18
    sprite('mk300_03', 6)	# 19-24
    sprite('mk300_04', 6)	# 25-30
    sprite('mk300_05', 6)	# 31-36
    sprite('mk300_06', 6)	# 37-42
    sprite('mk300_07', 6)	# 43-48
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_blvsmk_00():

    def upon_IMMEDIATE():
        Unknown21007(22, 32)
    sprite('mk600_00', 32767)	# 1-32767

@State
def Act3Event_blvsmk_01():
    sprite('mk611_00', 6)	# 1-6
    sprite('mk611_01', 6)	# 7-12
    sprite('mk611_02', 6)	# 13-18
    sprite('mk611_03', 6)	# 19-24
    sprite('mk611_04', 6)	# 25-30
    sprite('mk611_05', 6)	# 31-36
    sprite('mk611_06', 32767)	# 37-32803
    loopRest()

@State
def Act3Event_blvsmk_02():
    sprite('mk611_05', 6)	# 1-6
    sprite('mk611_04', 6)	# 7-12
    sprite('mk611_03', 6)	# 13-18
    sprite('mk611_02', 6)	# 19-24
    sprite('mk611_01', 6)	# 25-30
    sprite('mk611_00', 6)	# 31-36
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_izvsmk_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
        Unknown2004(1, 0)
    sprite('mk203_04', 3)	# 1-3
    setInvincible(1)
    teleportRelativeX(50000)
    physicsXImpulse(10000)
    Unknown21012('447269766543686172676541757261000000000000000000000000000000000020000000')
    Unknown21012('447269766543686172676557696e64000000000000000000000000000000000020000000')
    sprite('mk203_05', 2)	# 4-5
    Unknown8007(100, 1, 1)
    SFX_3('mkse_03')
    sprite('mk203_06', 2)	# 6-7
    sprite('mk203_07', 16)	# 8-23	 **attackbox here**
    GFX_0('Eventoffset_Sosai', -1)
    Unknown1084(1)
    sprite('mk203_08', 3)	# 24-26
    sprite('mk203_09', 4)	# 27-30
    sprite('mk203_10', 3)	# 31-33
    sprite('mk203_10ex00', 3)	# 34-36
    sprite('mk203_11', 4)	# 37-40
    sprite('mk203_12', 4)	# 41-44
    sprite('mk203_13', 4)	# 45-48
    sprite('mk203_14', 4)	# 49-52
    sprite('mk203_15', 4)	# 53-56
    sprite('mk203_16', 8)	# 57-64
    sprite('mk203_17', 4)	# 65-68
    setInvincible(0)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_esvsmk_00():
    sprite('mk615_00', 6)	# 1-6
    sprite('mk615_06', 6)	# 7-12
    sprite('mk615_07', 7)	# 13-19
    sprite('mk615_08', 10)	# 20-29
    sprite('mk615_09', 5)	# 30-34
    clearUponHandler(3)
    sprite('mk615_10', 5)	# 35-39
    label(0)
    sprite('mk615_11', 7)	# 40-46
    sprite('mk615_12', 7)	# 47-53
    sprite('mk615_13', 7)	# 54-60
    loopRest()
    gotoLabel(0)

@State
def Act3Event_esvsmk_01():
    sprite('mk300_00', 6)	# 1-6
    sprite('mk000_27', 6)	# 7-12
    sprite('mk000_28', 6)	# 13-18
    sprite('mk000_29', 6)	# 19-24
    sprite('mk000_30', 6)	# 25-30
    Unknown8002()
    sprite('mk000_31', 6)	# 31-36
    sprite('mk000_32', 6)	# 37-42
    sprite('mk000_33', 6)	# 43-48
    sprite('mk000_34', 6)	# 49-54
    Unknown8002()
    sprite('mk000_35', 6)	# 55-60
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_esvsmk_02():
    sprite('mk610_00', 7)	# 1-7
    sprite('mk610_01', 7)	# 8-14
    label(0)
    sprite('mk610_02', 7)	# 15-21
    sprite('mk610_03', 7)	# 22-28
    sprite('mk610_04', 7)	# 29-35
    loopRest()
    gotoLabel(0)

@State
def Act3Event_esvsmk_03():
    sprite('mk070_00', 6)	# 1-6
    sprite('mk070_01', 6)	# 7-12
    Unknown2037(0)

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 >= 300):
            clearUponHandler(3)
            sendToLabel(1)
    label(0)
    sprite('mk070_02', 3)	# 13-15
    sprite('mk070_03', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mk070_02', 6)	# 19-24
    sprite('mk070_03', 6)	# 25-30
    sprite('mk070_10', 6)	# 31-36
    sprite('mk070_11', 6)	# 37-42
    sprite('mk070_12', 6)	# 43-48
    sprite('mk070_13', 6)	# 49-54
    loopRest()
    sprite('mk300_00', 6)	# 55-60
    sprite('mk300_01', 6)	# 61-66
    sprite('mk300_02', 6)	# 67-72
    sprite('mk300_03', 6)	# 73-78
    sprite('mk300_04', 6)	# 79-84
    sprite('mk300_05', 6)	# 85-90
    sprite('mk300_06', 6)	# 91-96
    sprite('mk300_07', 6)	# 97-102
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_esvsmk_04():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown1000(-260000)
    sprite('mk602_02', 7)	# 1-7
    sprite('mk602_01', 7)	# 8-14
    sprite('mk430_00', 6)	# 15-20
    sprite('mk601_01', 6)	# 21-26
    teleportRelativeX(-45000)
    sprite('mk601_00', 10)	# 27-36
    sprite('mk601_01', 2)	# 37-38
    sprite('mk601_02', 3)	# 39-41
    GFX_0('mkef_hibana', 0)
    SFX_0('024_getset_b')
    ScreenShake(0, 10000)
    sprite('mk601_03', 6)	# 42-47
    sprite('mk601_04', 10)	# 48-57
    sprite('mk601_05', 6)	# 58-63
    sprite('mk601_06', 6)	# 64-69
    sprite('mk601_07', 4)	# 70-73
    SFX_0('008_swing_pole_0')
    sprite('mk601_08', 4)	# 74-77
    sprite('mk601_09', 4)	# 78-81
    SFX_0('008_swing_pole_0')
    sprite('mk601_10', 4)	# 82-85
    sprite('mk601_11', 8)	# 86-93
    SFX_0('008_swing_pole_1')
    sprite('mk601_12', 6)	# 94-99
    sprite('mk601_13', 40)	# 100-139
    sprite('mk601_14', 6)	# 140-145
    sprite('mk601_15', 6)	# 146-151
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_esvsmk_05():
    sprite('mk611_00', 6)	# 1-6
    sprite('mk611_01', 6)	# 7-12
    sprite('mk611_02', 6)	# 13-18
    sprite('mk611_03', 6)	# 19-24
    sprite('mk611_04', 6)	# 25-30
    sprite('mk611_05', 6)	# 31-36
    sprite('mk611_06', 32767)	# 37-32803
    loopRest()

@State
def Act3Event_esvsmk_06():
    sprite('mk611_05', 6)	# 1-6
    sprite('mk611_04', 6)	# 7-12
    sprite('mk611_03', 6)	# 13-18
    sprite('mk611_02', 6)	# 19-24
    sprite('mk611_01', 6)	# 25-30
    sprite('mk611_00', 6)	# 31-36
    loopRest()
    enterState('Act3Event_esvsmk_07')

@State
def Act3Event_esvsmk_07():
    sprite('mk300_00', 6)	# 1-6
    sprite('mk300_01', 6)	# 7-12
    sprite('mk300_02', 6)	# 13-18
    sprite('mk300_03', 6)	# 19-24
    sprite('mk300_04', 6)	# 25-30
    sprite('mk300_05', 6)	# 31-36
    sprite('mk300_06', 6)	# 37-42
    sprite('mk300_07', 6)	# 43-48
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_mavsmk_00():
    sprite('keep', 6)	# 1-6
    Unknown21007(22, 32)
    sprite('mk620_01', 6)	# 7-12
    sprite('mk620_00', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')