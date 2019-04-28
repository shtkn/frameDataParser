@Subroutine
def PreInit():
    Unknown12019('62726300000000000000000000000000')

@Subroutine
def MatchInit():
    DashFInitialVelocity(15000)
    JumpYVelocity(25000)
    SuperJumpYVelocity(32000)
    Unknown12007(10000)
    Unknown12011(1000)
    Unknown12024(0)
    Unknown13039(2)
    Unknown2049(1)
    Unknown23003(0, 1, 1, 1, 9000, 9000, -5242880, -24368)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 200000, -200000, 200000, 3000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(100000, 450000, -150000, 120000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14015(100000, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 250000, -100000, 180000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown14015(100000, 450000, -150000, 120000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x19)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1500)
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown14015(0, 300000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 10000, -100000, 0, 10000, 1)
    Unknown15013(1)
    Unknown15012(1)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(-200000, 200000, -200000, 100000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 300000, -240000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 300000, -240000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(-300000, 300000, -100000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-150000, 150000, -1000000, 100000, 1000, 50)
    Unknown15006(2000)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
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
    Move_Register('ShotLandA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(2000)
    Unknown15012(2000)
    Unknown14015(50000, 550000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('ShotLandB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(600000, 1000000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('ShotLandC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(700000, 1800000, -200000, 200000, 500, 50)
    Unknown15022('0300000005000000000000002c010000')
    Move_EndRegister()
    Move_Register('ShotAirA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3037)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(700000, 2000000, -500000, 0, 500, 0)
    Move_EndRegister()
    Move_Register('ShotAirB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3037)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(400000, 1000000, -500000, 0, 500, 0)
    Move_EndRegister()
    Move_Register('ShotAirC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3037)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(200000, 600000, -500000, 0, 500, 50)
    Unknown15022('0300000005000000000000002c010000')
    Move_EndRegister()
    Move_Register('CallWindSuctionGhostLand', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 600000, -1000000, 100000, 300, 50)
    Move_EndRegister()
    Move_Register('CallWindSuctionGhostAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-100000, 600000, -1000000, 100000, 300, 50)
    Move_EndRegister()
    Move_Register('LightningMini', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 600000, -1000000, 100000, 300, 50)
    Move_EndRegister()
    Move_Register('LightningMiniAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-100000, 600000, -1000000, 100000, 300, 50)
    Move_EndRegister()
    Move_Register('ShotFlogLand', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown15012(3000)
    Unknown14015(500000, 15000000, -200000, 1000000, 1, 50)
    Unknown15022('0300000005000000000000002c010000')
    Move_EndRegister()
    Move_Register('ShotFlogAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown15012(3000)
    Unknown14015(400000, 1200000, -500000, 0, 1, 50)
    Unknown15022('030000000500000001000000e8030000')
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(1)
    Unknown14015(0, 20000, -200000, 150000, 200, 0)
    Move_EndRegister()
    Move_Register('LightningLandB', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(3000)
    Unknown15006(1)
    Unknown14015(-200000, 200000, -200000, 800000, 750, 5)
    Move_EndRegister()
    Move_Register('LightningAirB', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(3000)
    Unknown15006(1)
    Unknown14015(-200000, 200000, -500000, 800000, 750, 5)
    Move_EndRegister()
    Move_Register('UltimateStorm', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(50000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(400000, 1500000, -300000, 300000, 1000, 1)
    Move_EndRegister()
    Move_Register('LightningLandB_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(3000)
    Unknown15006(1)
    Unknown14015(-200000, 200000, -200000, 800000, 750, 5)
    Move_EndRegister()
    Move_Register('LightningAirB_OD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(3000)
    Unknown15006(1)
    Unknown14015(-200000, 200000, -500000, 800000, 750, 5)
    Move_EndRegister()
    Move_Register('UltimateStorm_OD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(50000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(400000, 1500000, -300000, 300000, 1000, 1)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15013(4000)
    Unknown15014(4000)
    Unknown14015(-250000, 250000, -200000, 800000, 1000, 1)
    Move_EndRegister()
    Move_Register('Wind1', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x37)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind1')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind2', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x44)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind2')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind3', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x51)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind3')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind4', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x5e)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind4')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind5', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x6b)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind5')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind6', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x78)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind6')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind7', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x85)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind7')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind8', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x92)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind8')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('Wind9', INPUT_SPECIALMOVE)
    Unknown14021(1)
    Move_Input_(0x9f)
    Unknown14005(1)
    Unknown14024('CheckWindActive')
    Unknown14019('FuncWind9')
    Unknown15005(1)
    Unknown15006(0)
    Unknown15014(0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 100000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5B', 100000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 100000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 200000000)
    Unknown15024('NmlAtk5BBB', 'ShotLandB', 300000000)
    Unknown15024('NmlAtk5BBB', 'ShotLandC', 100000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown14048('ShotLandA', 0x4, 0xed)
    Unknown14048('ShotFlogLand', 0x4, 0x79)
    Unknown14048('LightningLandB', 0x4, 0x5f)
    Unknown14048('LightningLandB_OD', 0x4, 0x5f)
    Unknown14048('ShotAirA', 0x4, 0xed)
    Unknown14048('ShotFlogAir', 0x4, 0x79)
    Unknown14048('LightningAirB', 0x4, 0x5f)
    Unknown14048('LightningAirB_OD', 0x4, 0x5f)
    Unknown12018(0, 'rc762_01')
    Unknown12018(1, 'rc762_04')
    Unknown12018(2, 'rc762_05')
    Unknown12018(3, 'rc762_06')
    Unknown12018(4, 'rc762_07')
    Unknown12018(5, 'rc762_08')
    Unknown12018(6, 'rc762_10')
    Unknown12018(7, 'rc041_02')
    Unknown12018(8, 'rc040_02')
    Unknown12018(9, 'rc045_02')
    Unknown12018(10, 'rc760_00')
    Unknown12018(11, 'rc760_01')
    Unknown12018(12, 'rc760_02')
    Unknown12018(13, 'rc760_03')
    Unknown12018(14, 'rc760_04')
    Unknown12018(15, 'rc760_12')
    Unknown12018(16, 'rc750_00')
    Unknown12018(17, 'rc752_00')
    Unknown12018(18, 'rc754_00')
    Unknown12018(19, 'rc000_00')
    Unknown12018(20, 'rc000_00')
    Unknown12018(25, 'rc063_00')
    Unknown12018(26, 'rc063_01')
    Unknown12018(27, 'rc063_02')
    Unknown12018(28, 'rc063_04')
    Unknown12018(29, 'rc063_13')
    Unknown12018(24, 'rc072_00')
    Unknown7010(0, 'brc000')
    Unknown7010(1, 'brc001')
    Unknown7010(2, 'brc002')
    Unknown7010(3, 'brc003')
    Unknown7010(4, 'brc004')
    Unknown7010(5, 'brc005')
    Unknown7010(6, 'brc006')
    Unknown7010(7, 'brc007')
    Unknown9012('08000000020000006267793030385f30000000000000000000000000')
    Unknown9012('0800000000000000627263303038000000000000000000000a000000')
    Unknown9012('09000000020000006267793030395f30000000000000000000000000')
    Unknown9012('0900000000000000627263303039000000000000000000000a000000')
    Unknown9012('0a000000020000006267793031305f30000000000000000000000000')
    Unknown9012('0a00000000000000627263303130000000000000000000000a000000')
    Unknown9012('0f00000001000000626e673031355f30000000000000000000000000')
    Unknown9012('1000000001000000626e673031365f30000000000000000000000000')
    Unknown9012('1100000001000000626e673031375f30000000000000000000000000')
    Unknown9012('1200000001000000626e673031385f30000000000000000000000000')
    Unknown9012('1300000001000000626e673031395f30000000000000000000000000')
    Unknown9012('1400000001000000626e673032305f30000000000000000000000000')
    Unknown9012('1500000001000000626e673032315f30000000000000000000000000')
    Unknown9012('1600000001000000626e673032325f30000000000000000000000000')
    Unknown9012('0f00000000000000627263303131000000000000000000000a000000')
    Unknown9012('1000000000000000627263303132000000000000000000000a000000')
    Unknown9012('1100000000000000627263303133000000000000000000000a000000')
    Unknown9012('1200000000000000627263303134000000000000000000000a000000')
    Unknown9012('1300000000000000627263303135000000000000000000000a000000')
    Unknown9012('1400000000000000627263303136000000000000000000000a000000')
    Unknown9012('1500000000000000627263303137000000000000000000000a000000')
    Unknown9012('1600000000000000627263303138000000000000000000000a000000')
    Unknown9012('17000000020000006267793032335f30000000000000000000000000')
    Unknown9012('17000000000000006272633031390000000000000000000005000000')
    Unknown9012('18000000020000006267793032345f30000000000000000000000000')
    Unknown9012('18000000000000006272633032300000000000000000000005000000')
    Unknown9012('1900000001000000626e673032355f30000000000000000000000000')
    Unknown9012('1900000000000000627263303231000000000000000000000a000000')
    Unknown9012('1c00000001000000626e673032385f30000000000000000000000000')
    Unknown9012('1c00000000000000627263303232000000000000000000000a000000')
    Unknown9012('1d00000001000000626e673032395f30000000000000000000000000')
    Unknown9012('1d000000000000006272633032330000000000000000000001000000')
    Unknown9012('1e00000001000000626e673033305f30000000000000000000000000')
    Unknown9012('1e000000000000006272633032340000000000000000000001000000')
    Unknown9012('1f00000001000000626e673033315f30000000000000000000000000')
    Unknown9012('1f000000000000006272633032350000000000000000000001000000')
    Unknown9012('2000000001000000626e673033325f30000000000000000000000000')
    Unknown9012('20000000000000006272633032360000000000000000000001000000')
    Unknown9012('2100000001000000626e673033335f30000000000000000000000000')
    Unknown9012('21000000000000006272633032370000000000000000000014000000')
    Unknown9012('2200000001000000626e673033345f30000000000000000000000000')
    Unknown9012('22000000000000006272633032380000000000000000000014000000')
    Unknown9012('2300000001000000626e673033355f30000000000000000000000000')
    Unknown9012('23000000000000006272633032390000000000000000000014000000')
    Unknown9012('2400000001000000626e673033365f30000000000000000000000000')
    Unknown9012('24000000000000006272633033300000000000000000000014000000')
    Unknown9012('2500000001000000626e673033375f30000000000000000000000000')
    Unknown9012('2500000000000000627263303331000000000000000000000a000000')
    Unknown7010(39, 'brc032')
    Unknown9012('2a00000001000000626e673034325f30000000000000000000000000')
    Unknown9012('2a00000000000000627263303333000000000000000000000a000000')
    Unknown7010(43, 'brc034')
    Unknown9012('2c00000001000000626e673034345f30000000000000000000000000')
    Unknown9012('2c000000000000006272633033350000000000000000000001000000')
    Unknown9012('2d00000001000000626e673034355f31000000000000000000000000')
    Unknown9012('2d000000000000006272633033360000000000000000000001000000')
    Unknown9012('2e00000001000000626e673034365f30000000000000000000000000')
    Unknown9012('2e000000000000006272633033370000000000000000000001000000')
    Unknown9012('2f000000020000006267793033375f31000000000000000000000000')
    Unknown9012('2f000000000000006272633033380000000000000000000001000000')
    Unknown9012('3000000001000000626e673034365f31000000000000000000000000')
    Unknown9012('30000000000000006272633033390000000000000000000001000000')
    Unknown7010(49, 'brc040')
    Unknown7010(50, 'brc041')
    Unknown9012('3400000001000000626e673035325f30000000000000000000000000')
    Unknown9012('3400000000000000627263303432000000000000000000000a000000')
    Unknown9012('35000000000000006272633034330000000000000000000000000000')
    Unknown9012('3500000001000000626e673035335f30000000000000000001000000')
    Unknown7010(54, 'brc100_0')
    Unknown7010(55, 'brc100_1')
    Unknown7010(56, 'brc100_2')
    Unknown7010(63, 'brc101_0')
    Unknown7010(64, 'brc101_1')
    Unknown7010(65, 'brc101_2')
    Unknown7010(57, 'brc102_0')
    Unknown7010(58, 'brc102_1')
    Unknown7010(59, 'brc102_2')
    Unknown7010(66, 'brc103_0')
    Unknown7010(67, 'brc103_1')
    Unknown7010(68, 'brc103_2')
    Unknown7010(60, 'brc104_0')
    Unknown7010(61, 'brc104_1')
    Unknown7010(62, 'brc104_2')
    Unknown7010(69, 'brc105_0')
    Unknown7010(70, 'brc105_1')
    Unknown7010(71, 'brc105_2')
    Unknown7010(72, 'brc150')
    Unknown7010(73, 'brc151')
    Unknown7010(74, 'brc152')
    Unknown7010(85, 'brc153')
    Unknown7010(87, 'brc154')
    Unknown7010(88, 'brc155')
    Unknown7010(96, 'brc161_0')
    Unknown7010(97, 'brc161_1')
    Unknown7010(92, 'brc162_0')
    Unknown7010(93, 'brc162_1')
    Unknown7010(98, 'brc163_0')
    Unknown7010(99, 'brc163_1')
    Unknown7010(100, 'brc164_0')
    Unknown7010(101, 'brc164_1')
    Unknown7010(105, 'brc165_0')
    Unknown7010(106, 'brc165_1')
    Unknown7010(102, 'brc166_0')
    Unknown7010(103, 'brc166_1')
    Unknown7010(90, 'brc167_0')
    Unknown7010(91, 'brc167_1')
    Unknown7010(107, 'brc168_0')
    Unknown7010(108, 'brc168_1')
    Unknown7010(110, 'brc169_0')
    Unknown7010(111, 'brc169_1')
    Unknown7010(94, 'brc402_0')
    Unknown7010(95, 'brc402_1')
    GFX_0('Gi', -1)
    Unknown38(11, 1)
    Unknown32('52435f456173794d6f646557696e6400')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553746f726d00000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553746f726d5f4f4400000000000000000000000000000000')
    Unknown12059('040000004c696768746e696e674c616e6442000000000000000000000000000000000000')
    Unknown12059('050000004c696768746e696e674c616e64425f4f44000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def MatchInit2():
    SLOT_61 = 2000

@Subroutine
def OnLanding():
    SLOT_4 = 0

@Subroutine
def AddChainWind():
    WhiffCancelEnable(1)
    WhiffCancel('Wind1')
    WhiffCancel('Wind2')
    WhiffCancel('Wind3')
    WhiffCancel('Wind4')
    WhiffCancel('Wind6')
    WhiffCancel('Wind7')
    WhiffCancel('Wind8')
    WhiffCancel('Wind9')

@Subroutine
def AddChainWind_Air():
    WhiffCancelEnable(1)
    WhiffCancel('Wind1')
    WhiffCancel('Wind2')
    WhiffCancel('Wind3')

@Subroutine
def AddChainWind_Shot():
    WhiffCancelEnable(1)
    if SLOT_38:
        WhiffCancel('Wind1')
        WhiffCancel('Wind2')
        WhiffCancel('Wind4')
        WhiffCancel('Wind7')
        WhiffCancel('Wind8')
    else:
        WhiffCancel('Wind2')
        WhiffCancel('Wind3')
        WhiffCancel('Wind6')
        WhiffCancel('Wind8')
        WhiffCancel('Wind9')

@Subroutine
def FuncWindDefault():
    GFX_0('ModelMagicCircle1', -1)
    GFX_0('rcef_mc', -1)
    GFX_1('rcef_mc_light', -1)
    SLOT_31 = 0
    SLOT_62 = 1
    SLOT_65 = 0
    Unknown16001('57696e6431000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6432000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6433000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6434000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6435000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6436000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6437000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6438000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown16001('57696e6439000000000000000000000000000000000000000000000000000000780000002c010000')
    Unknown23076()

@Subroutine
def FuncWind1():
    if (not SLOT_59):
        Unknown23000(30, -707, -707)
        SFX_3('rcse_08')
        Unknown21007(10, 33)
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind2():
    if (not SLOT_59):
        Unknown23000(30, 0, -1000)
        SFX_3('rcse_08')
        Unknown21007(10, 34)
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind3():
    if (not SLOT_59):
        Unknown23000(30, 707, -707)
        SFX_3('rcse_08')
        Unknown21007(10, 35)
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind4():
    if (not SLOT_59):
        Unknown23000(30, -1000, 0)
        SFX_3('rcse_09')
        Unknown21007(10, 36)
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind5():
    if (not SLOT_59):
        if SLOT_6:
            Unknown23030('52435f57696e6453756374696f6e436865636b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        elif SLOT_38:
            Unknown23000(30, -1000, 0)
        else:
            Unknown23000(30, 1000, 0)
        SFX_3('rcse_09')
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind6():
    if (not SLOT_59):
        Unknown23000(30, 1000, 0)
        SFX_3('rcse_09')
        Unknown21007(10, 38)
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind7():
    if (not SLOT_59):
        Unknown23000(30, -707, 707)
        SFX_3('rcse_10')
        Unknown21007(10, 39)
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind8():
    if (not SLOT_59):
        Unknown23000(30, 0, 1000)
        SFX_3('rcse_10')
        Unknown21007(10, 40)
        callSubroutine('FuncWindDefault')

@Subroutine
def FuncWind9():
    if (not SLOT_59):
        Unknown23000(30, 707, 707)
        SFX_3('rcse_10')
        Unknown21007(10, 41)
        callSubroutine('FuncWindDefault')

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_37:
            SLOT_31 = (SLOT_31 + 100)
        if SLOT_90:
            Unknown58('TRI_BRCWindTime', 2, 67)
            if SLOT_67:
                SLOT_31 = (SLOT_31 + 9000)
        if SLOT_62:
            SLOT_62 = (SLOT_62 + 1)
    if SLOT_170:
        Unknown23029(4, 3101, 0)
        Unknown23029(5, 3101, 0)
        Unknown23029(6, 3101, 0)
        Unknown23008(0, 0)

@Subroutine
def CheckWindActive():
    (SLOT_31 == 9000)
    SLOT_47 = SLOT_0

@Subroutine
def OnActionBegin():
    Unknown2038(0)

@Subroutine
def OnFinalize():
    SLOT_65 = 0

@State
def CmnActStand():
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('rc001_00', 6)	# 64-69
    sprite('rc001_01', 6)	# 70-75
    sprite('rc001_02', 6)	# 76-81
    sprite('rc001_03', 6)	# 82-87
    sprite('rc001_04', 6)	# 88-93
    SLOT_88 = 960
    Unknown9008('01000000626e673030305f300000000000000000')
    sprite('rc001_05', 6)	# 94-99
    sprite('rc001_06', 6)	# 100-105
    sprite('rc001_07', 6)	# 106-111
    sprite('rc001_08', 6)	# 112-117
    sprite('rc001_09', 6)	# 118-123
    sprite('rc001_10', 6)	# 124-129
    sprite('rc001_11', 6)	# 130-135
    sprite('rc001_12', 6)	# 136-141
    SFX_4('brc000')
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('rc003_00', 3)	# 1-3
    sprite('rc003_01', 3)	# 4-6
    sprite('rc003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('rc010_00', 3)	# 1-3
    sprite('rc010_01', 3)	# 4-6
    sprite('rc010_02', 3)	# 7-9
    sprite('rc010_03', 3)	# 10-12
    sprite('rc010_04', 3)	# 13-15

@State
def CmnActCrouch():
    label(0)
    sprite('rc010_05', 6)	# 1-6
    sprite('rc010_06', 6)	# 7-12
    sprite('rc010_07', 6)	# 13-18
    sprite('rc010_08', 6)	# 19-24
    sprite('rc010_09', 6)	# 25-30
    sprite('rc010_10', 6)	# 31-36
    sprite('rc010_11', 6)	# 37-42
    sprite('rc010_12', 6)	# 43-48
    sprite('rc010_13', 6)	# 49-54
    sprite('rc010_14', 6)	# 55-60
    loopRest()
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(0)
    sprite('rc011_00', 8)	# 61-68
    sprite('rc011_01', 8)	# 69-76
    sprite('rc011_02', 8)	# 77-84
    sprite('rc011_03', 8)	# 85-92
    sprite('rc011_04', 8)	# 93-100
    SFX_4('brc300')
    sprite('rc011_05', 8)	# 101-108
    sprite('rc011_06', 12)	# 109-120
    sprite('rc011_07', 8)	# 121-128
    sprite('rc011_08', 8)	# 129-136
    sprite('rc011_09', 8)	# 137-144
    label(1)
    sprite('rc011_10', 16)	# 145-160
    sprite('rc011_11', 16)	# 161-176
    sprite('rc011_12', 16)	# 177-192
    sprite('rc011_13', 16)	# 193-208
    sprite('rc011_14', 16)	# 209-224
    sprite('rc011_15', 16)	# 225-240
    loopRest()
    gotoLabel(1)
    sprite('rc011_16', 8)	# 241-248
    sprite('rc011_17', 8)	# 249-256

@State
def CmnActCrouchTurn():
    sprite('rc013_00', 3)	# 1-3
    sprite('rc013_01', 3)	# 4-6
    sprite('rc013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('rc010_04', 3)	# 1-3
    sprite('rc010_03', 3)	# 4-6
    sprite('rc010_02', 3)	# 7-9
    sprite('rc010_01', 3)	# 10-12
    sprite('rc010_00', 3)	# 13-15

@State
def CmnActJumpPre():
    sprite('rc023_00', 2)	# 1-2
    sprite('rc023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('rc020_00', 3)	# 1-3
    sprite('rc020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('rc020_02', 3)	# 1-3
    sprite('rc020_03', 3)	# 4-6

@State
def CmnActJumpDown():
    sprite('rc020_03', 4)	# 1-4
    sprite('rc020_04', 4)	# 5-8
    sprite('rc020_05', 4)	# 9-12
    label(0)
    sprite('rc020_06', 4)	# 13-16
    sprite('rc020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('rc024_00', 4)	# 1-4
    sprite('rc024_01', 4)	# 5-8
    sprite('rc024_02', 4)	# 9-12
    sprite('rc024_03', 4)	# 13-16
    sprite('rc024_04', 4)	# 17-20

@State
def CmnActLandingStiffLoop():
    sprite('rc024_00', 2)	# 1-2
    sprite('rc024_01', 2)	# 3-4
    sprite('rc024_02', 2)	# 5-6
    sprite('rc024_03', 32767)	# 7-32773

@State
def CmnActLandingStiffEnd():
    sprite('rc024_04', 3)	# 1-3

@State
def CmnActFWalk():
    sprite('rc030_00', 4)	# 1-4
    label(0)
    sprite('rc030_01', 5)	# 5-9
    sprite('rc030_02', 5)	# 10-14
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_03', 5)	# 15-19
    sprite('rc030_04', 5)	# 20-24
    sprite('rc030_05', 5)	# 25-29
    sprite('rc030_06', 5)	# 30-34
    sprite('rc030_07', 5)	# 35-39
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_08', 5)	# 40-44
    sprite('rc030_09', 5)	# 45-49
    sprite('rc030_10', 5)	# 50-54
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():

    def upon_IMMEDIATE():
        Unknown2042(1)
    sprite('rc031_00', 5)	# 1-5
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc031_01', 5)	# 6-10
    label(0)
    sprite('rc031_02', 6)	# 11-16
    sprite('rc031_03', 6)	# 17-22
    sprite('rc031_04', 6)	# 23-28
    sprite('rc031_05', 6)	# 29-34
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalkEnd():
    sprite('rc031_06', 5)	# 1-5
    sprite('rc031_07', 5)	# 6-10

@State
def CmnActFDash():
    sprite('rc032_00', 4)	# 1-4
    sprite('rc032_01', 4)	# 5-8
    sprite('rc032_02', 4)	# 9-12
    SFX_0('000_airdash_0')
    Unknown8006(100, 1, 1)
    label(0)
    sprite('rc032_03', 4)	# 13-16
    sprite('rc032_04', 4)	# 17-20
    sprite('rc032_05', 4)	# 21-24
    sprite('rc032_06', 4)	# 25-28
    sprite('rc032_07', 4)	# 29-32
    sprite('rc032_08', 4)	# 33-36
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('rc032_09', 3)	# 1-3
    sprite('rc032_10', 3)	# 4-6
    Unknown8010(100, 1, 1)
    sprite('rc032_11', 3)	# 7-9
    sprite('rc032_12', 3)	# 10-12
    sprite('rc032_13', 3)	# 13-15
    Unknown13003(1)
    sprite('rc032_14', 3)	# 16-18
    sprite('rc032_15', 3)	# 19-21

@State
def CmnActBDash():
    sprite('rc033_00', 2)	# 1-2
    Unknown22008(7)
    setGravity(800)
    sprite('rc033_01', 2)	# 3-4
    label(0)
    sprite('rc033_02', 3)	# 5-7
    sprite('rc033_03', 3)	# 8-10
    sprite('rc033_04', 3)	# 11-13
    sprite('rc033_05', 3)	# 14-16
    loopRest()
    gotoLabel(0)

@State
def CmnActBDashLanding():
    sprite('rc033_06', 3)	# 1-3
    sprite('rc033_07', 3)	# 4-6
    Unknown13006(1)
    sprite('rc033_08', 3)	# 7-9
    sprite('rc033_09', 3)	# 10-12
    sprite('rc033_10', 3)	# 13-15
    sprite('rc033_11', 3)	# 16-18
    sprite('rc033_12', 3)	# 19-21
    sprite('rc033_13', 3)	# 22-24

@State
def CmnActAirFDash():
    sprite('rc035_00', 3)	# 1-3
    label(0)
    sprite('rc035_01', 3)	# 4-6
    sprite('rc035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('rc036_00', 3)	# 1-3
    label(0)
    sprite('rc036_01', 3)	# 4-6
    sprite('rc036_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('rc050_00', 1)	# 1-1
    sprite('rc050_01', 1)	# 2-2
    sprite('rc050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('rc050_01', 1)	# 1-1
    sprite('rc050_02', 1)	# 2-2
    sprite('rc050_01', 2)	# 3-4
    sprite('rc050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('rc050_02', 1)	# 1-1
    sprite('rc050_03', 1)	# 2-2
    sprite('rc050_02', 2)	# 3-4
    sprite('rc050_01', 2)	# 5-6
    sprite('rc050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('rc050_03', 1)	# 1-1
    sprite('rc050_04', 1)	# 2-2
    sprite('rc050_03', 2)	# 3-4
    sprite('rc050_02', 2)	# 5-6
    sprite('rc050_01', 2)	# 7-8
    sprite('rc050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('rc050_04', 1)	# 1-1
    sprite('rc050_04', 1)	# 2-2
    sprite('rc050_04', 2)	# 3-4
    sprite('rc050_03', 2)	# 5-6
    sprite('rc050_02', 2)	# 7-8
    sprite('rc050_01', 2)	# 9-10
    sprite('rc050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('rc052_00', 1)	# 1-1
    sprite('rc052_01', 1)	# 2-2
    sprite('rc052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('rc052_01', 1)	# 1-1
    sprite('rc052_02', 1)	# 2-2
    sprite('rc052_01', 2)	# 3-4
    sprite('rc052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('rc052_02', 1)	# 1-1
    sprite('rc052_03', 1)	# 2-2
    sprite('rc052_02', 2)	# 3-4
    sprite('rc052_01', 2)	# 5-6
    sprite('rc052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('rc052_03', 1)	# 1-1
    sprite('rc052_04', 1)	# 2-2
    sprite('rc052_03', 2)	# 3-4
    sprite('rc052_02', 2)	# 5-6
    sprite('rc052_01', 2)	# 7-8
    sprite('rc052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('rc052_04', 1)	# 1-1
    sprite('rc052_04', 1)	# 2-2
    sprite('rc052_04', 2)	# 3-4
    sprite('rc052_03', 2)	# 5-6
    sprite('rc052_02', 2)	# 7-8
    sprite('rc052_01', 2)	# 9-10
    sprite('rc052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('rc054_00', 1)	# 1-1
    sprite('rc054_01', 1)	# 2-2
    sprite('rc054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('rc054_01', 1)	# 1-1
    sprite('rc054_02', 1)	# 2-2
    sprite('rc054_01', 2)	# 3-4
    sprite('rc054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('rc054_02', 1)	# 1-1
    sprite('rc054_03', 1)	# 2-2
    sprite('rc054_02', 2)	# 3-4
    sprite('rc054_01', 2)	# 5-6
    sprite('rc054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('rc054_03', 1)	# 1-1
    sprite('rc054_04', 1)	# 2-2
    sprite('rc054_03', 2)	# 3-4
    sprite('rc054_02', 2)	# 5-6
    sprite('rc054_01', 2)	# 7-8
    sprite('rc054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('rc054_04', 1)	# 1-1
    sprite('rc054_04', 1)	# 2-2
    sprite('rc054_04', 2)	# 3-4
    sprite('rc054_03', 2)	# 5-6
    sprite('rc054_02', 2)	# 7-8
    sprite('rc054_01', 2)	# 9-10
    sprite('rc054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('rc060_00', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('rc060_01', 4)	# 5-8	 **attackbox here**
    sprite('rc060_02', 4)	# 9-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('rc062_04', 2)	# 1-2	 **attackbox here**
    sprite('rc062_05', 2)	# 3-4	 **attackbox here**

@State
def CmnActBDownDown():
    sprite('rc062_06', 3)	# 1-3	 **attackbox here**
    sprite('rc062_07', 3)	# 4-6	 **attackbox here**
    label(0)
    sprite('rc062_08', 3)	# 7-9	 **attackbox here**
    sprite('rc062_09', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('rc063_04', 1)	# 1-1	 **attackbox here**
    sprite('rc063_05', 1)	# 2-2	 **attackbox here**

@State
def CmnActBDownBound():
    sprite('rc063_06', 2)	# 1-2	 **attackbox here**
    GFX_0('nago_medama', 104)
    sprite('rc063_07', 2)	# 3-4	 **attackbox here**
    sprite('rc063_08', 3)	# 5-7	 **attackbox here**
    sprite('rc063_09', 3)	# 8-10	 **attackbox here**
    sprite('rc063_10', 3)	# 11-13	 **attackbox here**

@State
def CmnActBDownLoop():
    sprite('rc063_11', 5)	# 1-5	 **attackbox here**
    sprite('rc063_12', 5)	# 6-10	 **attackbox here**
    sprite('rc063_13', 5)	# 11-15	 **attackbox here**

@State
def CmnActBDown2Stand():
    sprite('rc064_00', 4)	# 1-4	 **attackbox here**
    sprite('rc064_01', 4)	# 5-8	 **attackbox here**
    sprite('rc064_02', 3)	# 9-11	 **attackbox here**
    sprite('rc064_03', 2)	# 12-13	 **attackbox here**
    sprite('rc064_04', 2)	# 14-15	 **attackbox here**
    sprite('rc064_05', 2)	# 16-17	 **attackbox here**
    sprite('rc064_06', 2)	# 18-19	 **attackbox here**
    sprite('rc064_07', 2)	# 20-21	 **attackbox here**
    sprite('rc064_08', 2)	# 22-23	 **attackbox here**
    sprite('rc064_09', 2)	# 24-25	 **attackbox here**
    sprite('rc064_10', 3)	# 26-28	 **attackbox here**
    sprite('rc064_11', 3)	# 29-31
    sprite('rc064_12', 3)	# 32-34

@State
def CmnActFDownUpper():
    sprite('rc063_00', 3)	# 1-3	 **attackbox here**

@State
def CmnActFDownUpperEnd():
    sprite('rc063_01', 3)	# 1-3	 **attackbox here**

@State
def CmnActFDownDown():
    label(0)
    sprite('rc063_02', 3)	# 1-3	 **attackbox here**
    sprite('rc063_03', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('rc063_04', 1)	# 1-1	 **attackbox here**
    sprite('rc063_05', 1)	# 2-2	 **attackbox here**

@State
def CmnActFDownBound():
    sprite('rc063_06', 2)	# 1-2	 **attackbox here**
    GFX_0('nago_medama', 104)
    sprite('rc063_07', 2)	# 3-4	 **attackbox here**
    sprite('rc063_08', 3)	# 5-7	 **attackbox here**
    sprite('rc063_09', 3)	# 8-10	 **attackbox here**
    sprite('rc063_10', 3)	# 11-13	 **attackbox here**

@State
def CmnActFDownLoop():
    sprite('rc063_11', 5)	# 1-5	 **attackbox here**
    sprite('rc063_12', 5)	# 6-10	 **attackbox here**
    sprite('rc063_13', 5)	# 11-15	 **attackbox here**

@State
def CmnActFDown2Stand():
    sprite('rc064_00', 4)	# 1-4	 **attackbox here**
    sprite('rc064_01', 4)	# 5-8	 **attackbox here**
    sprite('rc064_02', 3)	# 9-11	 **attackbox here**
    sprite('rc064_03', 2)	# 12-13	 **attackbox here**
    sprite('rc064_04', 2)	# 14-15	 **attackbox here**
    sprite('rc064_05', 2)	# 16-17	 **attackbox here**
    sprite('rc064_06', 2)	# 18-19	 **attackbox here**
    sprite('rc064_07', 2)	# 20-21	 **attackbox here**
    sprite('rc064_08', 2)	# 22-23	 **attackbox here**
    sprite('rc064_09', 2)	# 24-25	 **attackbox here**
    sprite('rc064_10', 3)	# 26-28	 **attackbox here**
    sprite('rc064_11', 3)	# 29-31
    sprite('rc064_12', 3)	# 32-34

@State
def CmnActVDownUpper():
    sprite('rc062_00', 3)	# 1-3	 **attackbox here**
    label(0)
    sprite('rc062_01', 3)	# 4-6	 **attackbox here**
    sprite('rc062_02', 3)	# 7-9	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('rc062_03', 3)	# 1-3	 **attackbox here**
    sprite('rc062_04', 3)	# 4-6	 **attackbox here**
    sprite('rc062_05', 3)	# 7-9	 **attackbox here**

@State
def CmnActVDownDown():
    sprite('rc062_06', 3)	# 1-3	 **attackbox here**
    sprite('rc062_07', 3)	# 4-6	 **attackbox here**
    label(0)
    sprite('rc062_08', 3)	# 7-9	 **attackbox here**
    sprite('rc062_09', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('rc062_10', 1)	# 1-1	 **attackbox here**
    sprite('rc062_11', 1)	# 2-2	 **attackbox here**

@State
def CmnActBlowoff():
    sprite('rc072_00', 3)	# 1-3
    sprite('rc072_01', 3)	# 4-6
    sprite('rc072_02', 3)	# 7-9
    label(0)
    sprite('rc072_01', 3)	# 10-12
    sprite('rc072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('rc074_00', 3)	# 1-3
    sprite('rc074_01', 3)	# 4-6
    sprite('rc074_02', 3)	# 7-9
    sprite('rc074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():

    def upon_IMMEDIATE():
        Unknown2042(1)
        GFX_0('dengeki_ng', -1)
    label(0)
    sprite('rc082_00', 2)	# 1-2
    sprite('rc082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('rc071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('rc073_00', 2)	# 1-2
    sprite('rc073_01', 2)	# 3-4
    sprite('rc072_00', 2)	# 5-6

@State
def CmnActWallBoundDown():
    sprite('rc073_02', 3)	# 1-3
    label(0)
    sprite('rc073_03', 3)	# 4-6
    sprite('rc073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('rc070_00', 3)	# 1-3
    sprite('rc070_01', 3)	# 4-6
    sprite('rc070_02', 3)	# 7-9	 **attackbox here**
    sprite('rc070_03', 3)	# 10-12	 **attackbox here**
    sprite('rc070_04', 3)	# 13-15	 **attackbox here**

@State
def CmnActStaggerDown():
    sprite('rc070_05', 7)	# 1-7	 **attackbox here**
    sprite('rc070_06', 7)	# 8-14	 **attackbox here**
    sprite('rc070_07', 7)	# 15-21	 **attackbox here**

@State
def CmnActUkemiStagger():
    sprite('rc070_08', 5)	# 1-5
    sprite('rc070_09', 5)	# 6-10
    sprite('rc070_10', 5)	# 11-15

@State
def CmnActUkemiAirF():
    sprite('rc113_00', 2)	# 1-2
    sprite('rc113_01', 2)	# 3-4
    sprite('rc113_02', 3)	# 5-7
    sprite('rc113_03', 2)	# 8-9

@State
def CmnActUkemiAirB():
    sprite('rc113_00', 2)	# 1-2
    sprite('rc113_01', 2)	# 3-4
    sprite('rc113_02', 3)	# 5-7
    sprite('rc113_03', 2)	# 8-9

@State
def CmnActUkemiAirN():
    sprite('rc113_00', 2)	# 1-2
    sprite('rc113_01', 2)	# 3-4
    sprite('rc113_02', 3)	# 5-7
    sprite('rc113_03', 2)	# 8-9

@State
def CmnActUkemiLandF():
    sprite('rc110_00', 2)	# 1-2
    sprite('rc110_01', 1)	# 3-3
    sprite('rc110_02', 2)	# 4-5
    sprite('rc110_03', 2)	# 6-7
    sprite('rc110_04', 2)	# 8-9
    sprite('rc110_05', 2)	# 10-11
    sprite('rc110_06', 2)	# 12-13
    sprite('rc110_07', 2)	# 14-15
    sprite('rc110_08', 2)	# 16-17
    sprite('rc110_10', 200)	# 18-217
    sprite('rc110_11', 6)	# 218-223

@State
def CmnActUkemiLandB():
    sprite('rc111_00', 2)	# 1-2
    sprite('rc111_01', 2)	# 3-4
    sprite('rc111_02', 2)	# 5-6
    sprite('rc111_03', 2)	# 7-8
    sprite('rc111_04', 3)	# 9-11
    sprite('rc111_06', 3)	# 12-14
    sprite('rc111_07', 3)	# 15-17
    sprite('rc111_08', 3)	# 18-20
    sprite('rc111_09', 3)	# 21-23
    sprite('rc111_10', 3)	# 24-26
    sprite('rc111_11', 200)	# 27-226
    sprite('rc111_12', 2)	# 227-228
    sprite('rc111_13', 2)	# 229-230
    sprite('rc111_14', 2)	# 231-232

@State
def CmnActUkemiLandN():
    sprite('rc112_00', 2)	# 1-2
    sprite('rc112_01', 2)	# 3-4
    sprite('rc112_02', 2)	# 5-6
    sprite('rc112_03', 2)	# 7-8
    sprite('rc112_04', 2)	# 9-10
    sprite('rc112_05', 2)	# 11-12
    sprite('rc112_06', 2)	# 13-14
    sprite('rc112_07', 2)	# 15-16
    sprite('rc112_08', 2)	# 17-18
    sprite('rc112_09', 2)	# 19-20

@State
def CmnActUkemiLandNLanding():
    sprite('rc024_00', 3)	# 1-3
    sprite('rc024_01', 3)	# 4-6
    sprite('rc024_02', 3)	# 7-9
    sprite('rc024_03', 3)	# 10-12
    sprite('rc024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('rc040_00', 3)	# 1-3
    GFX_0('BatSummons', 0)
    sprite('rc040_01', 2)	# 4-5

@State
def CmnActMidGuardLoop():
    sprite('rc040_02', 3)	# 1-3

@State
def CmnActMidGuardEnd():
    sprite('rc040_01', 3)	# 1-3
    sprite('rc040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('rc040_02', 2)	# 1-2
    sprite('rc040_03', 3)	# 3-5

@State
def CmnActMidHeavyGuardEnd():
    sprite('rc040_02', 3)	# 1-3
    sprite('rc040_01', 3)	# 4-6
    sprite('rc040_00', 3)	# 7-9

@State
def CmnActHighGuardPre():
    sprite('rc041_00', 2)	# 1-2
    sprite('rc041_01', 2)	# 3-4
    GFX_0('BatSummons', 0)
    sprite('rc041_02', 2)	# 5-6

@State
def CmnActHighGuardLoop():
    sprite('rc041_03', 3)	# 1-3

@State
def CmnActHighGuardEnd():
    sprite('rc041_05', 3)	# 1-3
    sprite('rc041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('rc041_04', 3)	# 1-3
    sprite('rc041_03', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('rc041_05', 3)	# 1-3
    sprite('rc041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('rc043_00', 3)	# 1-3
    sprite('rc043_01', 3)	# 4-6
    GFX_0('BatSummons', 0)

@State
def CmnActCrouchGuardLoop():
    sprite('rc043_02', 3)	# 1-3

@State
def CmnActCrouchGuardEnd():
    sprite('rc043_04', 3)	# 1-3
    sprite('rc043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('rc043_03', 3)	# 1-3
    sprite('rc043_02', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('rc043_04', 3)	# 1-3
    sprite('rc043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('rc045_00', 3)	# 1-3
    sprite('rc045_01', 3)	# 4-6
    GFX_0('BatSummons', 0)

@State
def CmnActAirGuardLoop():
    sprite('rc045_02', 3)	# 1-3

@State
def CmnActAirGuardEnd():
    sprite('rc045_04', 3)	# 1-3
    sprite('rc045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('rc045_03', 3)	# 1-3
    sprite('rc045_02', 3)	# 4-6

@State
def CmnActAirHeavyGuardEnd():
    sprite('rc045_04', 3)	# 1-3
    sprite('rc045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('rc090_00', 2)	# 1-2
    sprite('rc090_01', 2)	# 3-4
    sprite('rc090_02', 1)	# 5-5
    Unknown2042(1)
    GFX_0('gi_GirdBreak', 0)
    sprite('rc090_03', 6)	# 6-11
    sprite('rc090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('rc091_00', 2)	# 1-2
    sprite('rc091_01', 2)	# 3-4
    sprite('rc091_02', 1)	# 5-5
    Unknown2042(1)
    GFX_0('gi_GirdBreak', 0)
    sprite('rc091_03', 6)	# 6-11
    sprite('rc091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('rc092_00', 2)	# 1-2
    sprite('rc092_01', 2)	# 3-4
    sprite('rc092_02', 1)	# 5-5
    Unknown2042(1)
    GFX_0('gi_GirdBreak', 0)
    sprite('rc092_03', 4)	# 6-9
    sprite('rc092_04', 4)	# 10-13
    sprite('rc092_04', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('rc025_00', 4)	# 1-4
    sprite('rc025_01', 4)	# 5-8
    sprite('rc025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('rc040_03', 3)	# 1-3
    sprite('rc040_02', 3)	# 4-6
    sprite('rc040_01', 3)	# 7-9
    sprite('rc040_00', 3)	# 10-12

@State
def CmnActLockReject():
    sprite('rc312_00', 2)	# 1-2
    sprite('rc312_01', 2)	# 3-4
    sprite('rc312_02', 2)	# 5-6
    sprite('rc312_03', 4)	# 7-10
    sprite('rc312_04', 4)	# 11-14	 **attackbox here**
    sprite('rc312_04ex01', 2)	# 15-16
    sprite('rc312_05', 8)	# 17-24
    sprite('rc312_06', 2)	# 25-26
    sprite('rc312_06ex01', 2)	# 27-28
    sprite('rc312_07', 2)	# 29-30
    sprite('rc312_07ex01', 2)	# 31-32

@State
def CmnActAirLockWait():
    sprite('rc045_02', 1)	# 1-1
    sprite('rc045_04', 3)	# 2-4
    sprite('rc045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('rc322_00', 2)	# 1-2
    sprite('rc322_01', 2)	# 3-4
    sprite('rc322_02', 8)	# 5-12
    sprite('rc322_03', 2)	# 13-14
    sprite('rc322_04', 4)	# 15-18	 **attackbox here**
    sprite('rc322_05', 4)	# 19-22
    sprite('rc322_06', 4)	# 23-26
    sprite('rc322_07', 4)	# 27-30
    sprite('rc322_08', 4)	# 31-34

@State
def CmnActLandSpin():
    sprite('rc071_00', 4)	# 1-4
    sprite('rc071_01', 4)	# 5-8
    label(0)
    sprite('rc071_02', 2)	# 9-10
    sprite('rc071_03', 2)	# 11-12
    sprite('rc071_04', 2)	# 13-14
    sprite('rc071_05', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('rc071_06', 5)	# 1-5
    sprite('rc071_07', 5)	# 6-10
    sprite('rc071_08', 5)	# 11-15

@State
def CmnActVertSpin():
    label(0)
    sprite('rc071_02', 2)	# 1-2
    sprite('rc071_03', 2)	# 3-4
    sprite('rc071_04', 2)	# 5-6
    sprite('rc071_05', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('rc077_00', 2)	# 1-2	 **attackbox here**
    sprite('rc077_01', 2)	# 3-4	 **attackbox here**
    sprite('rc077_00ex01', 2)	# 5-6	 **attackbox here**
    sprite('rc077_01ex01', 2)	# 7-8	 **attackbox here**
    sprite('rc077_00ex02', 2)	# 9-10	 **attackbox here**
    sprite('rc077_01ex02', 2)	# 11-12	 **attackbox here**
    sprite('rc077_00ex03', 2)	# 13-14	 **attackbox here**
    sprite('rc077_01ex03', 2)	# 15-16	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('rc077_02', 4)	# 1-4	 **attackbox here**
    GFX_0('BatSummons', 0)
    label(0)
    sprite('rc077_03', 3)	# 5-7	 **attackbox here**
    sprite('rc077_04', 3)	# 8-10	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('rc077_05', 5)	# 1-5	 **attackbox here**
    sprite('rc077_06', 4)	# 6-9	 **attackbox here**

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('rc060_07', 3)	# 1-3	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('rc060_09', 3)	# 1-3	 **attackbox here**
    sprite('rc060_10', 3)	# 4-6	 **attackbox here**
    sprite('rc060_11', 3)	# 7-9	 **attackbox here**

@State
def CmnActBurstBegin():
    sprite('rc331_00', 2)	# 1-2
    sprite('rc331_01', 2)	# 3-4
    sprite('rc331_02', 2)	# 5-6
    sprite('rc331_03', 2)	# 7-8
    label(0)
    sprite('rc331_04', 3)	# 9-11
    sprite('rc331_05', 3)	# 12-14
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('rc331_06', 3)	# 1-3
    label(0)
    sprite('rc331_07', 3)	# 4-6
    sprite('rc331_07ex00', 3)	# 7-9
    sprite('rc331_07ex01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('rc331_08', 2)	# 1-2
    sprite('rc331_09', 2)	# 3-4
    sprite('rc331_10', 2)	# 5-6

@State
def CmnActAirBurstBegin():
    sprite('rc332_00', 2)	# 1-2
    sprite('rc332_01', 2)	# 3-4
    sprite('rc332_02', 2)	# 5-6
    sprite('rc332_03', 2)	# 7-8
    label(0)
    sprite('rc332_04', 3)	# 9-11
    sprite('rc332_05', 3)	# 12-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('rc332_06', 3)	# 1-3
    label(0)
    sprite('rc332_07', 3)	# 4-6
    sprite('rc332_07ex00', 3)	# 7-9
    sprite('rc332_07ex01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('rc332_08', 3)	# 1-3
    sprite('rc332_09', 3)	# 4-6
    sprite('rc332_10', 3)	# 7-9
    sprite('rc332_11', 3)	# 10-12
    sprite('rc020_03', 3)	# 13-15
    sprite('rc020_04', 3)	# 16-18
    sprite('rc020_05', 3)	# 19-21
    label(0)
    sprite('rc020_06', 3)	# 22-24
    sprite('rc020_07', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('rc333_00', 3)	# 1-3
    sprite('rc333_01', 3)	# 4-6
    sprite('rc333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('rc333_03', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_RC_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('rc333_04', 3)	# 1-3	 **attackbox here**
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('rc333_05', 3)	# 4-6	 **attackbox here**
    sprite('rc333_06', 3)	# 7-9	 **attackbox here**
    sprite('rc333_07', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('rc333_08', 4)	# 1-4	 **attackbox here**
    sprite('rc333_09', 4)	# 5-8
    sprite('rc333_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('rc333_11', 3)	# 1-3
    sprite('rc333_12', 3)	# 4-6
    sprite('rc333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('rc333_14', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_RC_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('rc333_15', 3)	# 1-3	 **attackbox here**
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('rc333_05', 3)	# 4-6	 **attackbox here**
    sprite('rc333_06', 3)	# 7-9	 **attackbox here**
    sprite('rc333_07', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('rc333_16', 4)	# 1-4	 **attackbox here**
    sprite('rc333_17', 4)	# 5-8
    sprite('rc333_18', 4)	# 9-12
    sprite('rc020_03', 4)	# 13-16
    sprite('rc020_04', 4)	# 17-20
    sprite('rc020_05', 4)	# 21-24
    label(0)
    sprite('rc020_06', 4)	# 25-28
    sprite('rc020_07', 4)	# 29-32
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('rc333_00', 3)	# 1-3
    sprite('rc333_01', 3)	# 4-6
    sprite('rc333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('rc333_03', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_RC_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('rc333_04', 3)	# 1-3	 **attackbox here**
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('rc333_05', 3)	# 4-6	 **attackbox here**
    sprite('rc333_06', 3)	# 7-9	 **attackbox here**
    sprite('rc333_07', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('rc333_08', 4)	# 1-4	 **attackbox here**
    sprite('rc333_09', 4)	# 5-8
    sprite('rc333_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('rc333_11', 3)	# 1-3
    sprite('rc333_12', 3)	# 4-6
    sprite('rc333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('rc333_14', 32767)	# 10-32776	 **attackbox here**
    GFX_0('EMB_RC_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('rc333_15', 3)	# 1-3	 **attackbox here**
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('rc333_05', 3)	# 4-6	 **attackbox here**
    sprite('rc333_06', 3)	# 7-9	 **attackbox here**
    sprite('rc333_07', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('rc333_16', 4)	# 1-4	 **attackbox here**
    sprite('rc333_17', 4)	# 5-8
    sprite('rc333_18', 4)	# 9-12
    sprite('rc020_03', 4)	# 13-16
    sprite('rc020_04', 4)	# 17-20
    sprite('rc020_05', 4)	# 21-24
    label(0)
    sprite('rc020_06', 4)	# 25-28
    sprite('rc020_07', 4)	# 29-32
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('rc331_00', 2)	# 1-2
    sprite('rc331_01', 2)	# 3-4
    sprite('rc331_02', 2)	# 5-6
    sprite('rc331_03', 2)	# 7-8
    label(0)
    sprite('rc331_04', 3)	# 9-11
    sprite('rc331_05', 3)	# 12-14
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('rc331_06', 3)	# 1-3
    label(0)
    sprite('rc331_07', 3)	# 4-6
    sprite('rc331_07ex00', 3)	# 7-9
    sprite('rc331_07ex01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('rc331_08', 2)	# 1-2
    sprite('rc331_09', 2)	# 3-4
    sprite('rc331_10', 2)	# 5-6

@State
def CmnActAirCrossChangeBegin():
    sprite('rc332_00', 2)	# 1-2
    sprite('rc332_01', 2)	# 3-4
    sprite('rc332_02', 2)	# 5-6
    sprite('rc332_03', 2)	# 7-8
    label(0)
    sprite('rc332_04', 3)	# 9-11
    sprite('rc332_05', 3)	# 12-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('rc332_06', 3)	# 1-3
    label(0)
    sprite('rc332_07', 3)	# 4-6
    sprite('rc332_07ex00', 3)	# 7-9
    sprite('rc332_07ex01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('rc332_08', 3)	# 1-3
    sprite('rc332_09', 3)	# 4-6
    sprite('rc332_10', 3)	# 7-9
    sprite('rc332_11', 3)	# 10-12
    sprite('rc020_03', 3)	# 13-15
    sprite('rc020_04', 3)	# 16-18
    sprite('rc020_05', 3)	# 19-21
    label(0)
    sprite('rc020_06', 3)	# 22-24
    sprite('rc020_07', 3)	# 25-27
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
            Unknown2034(0)
            if Unknown30042(25):
                Unknown2034(1)
            if (SLOT_18 == 5):
                Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
                SFX_0('301_overdrive_end')
            if (SLOT_18 == 46):
                sendToLabel(2)
    sprite('rc300_00', 4)	# 1-4
    sprite('rc300_01', 4)	# 5-8
    sprite('rc300_02', 4)	# 9-12
    sprite('rc300_03', 4)	# 13-16
    loopRest()
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    label(0)
    sprite('rc300_04', 6)	# 17-22
    sprite('rc300_05', 6)	# 23-28
    SFX_3('rcse_00')
    sprite('rc300_06', 6)	# 29-34
    sprite('rc300_07', 6)	# 35-40
    sprite('rc300_08', 6)	# 41-46
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc300_09', 6)	# 47-52
    sprite('rc300_10', 6)	# 53-58
    SFX_3('rcse_00')
    sprite('rc300_11', 6)	# 59-64
    sprite('rc300_12', 6)	# 65-70
    sprite('rc300_13', 6)	# 71-76
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rc300_14', 4)	# 77-80
    sprite('rc300_15', 4)	# 81-84
    sprite('rc300_16', 4)	# 85-88
    sprite('rc300_17', 4)	# 89-92

@State
def CmnActChangePartnerQuickIn():
    sprite('rc032_09', 3)	# 1-3
    sprite('rc032_10', 4)	# 4-7
    sprite('rc032_11', 4)	# 8-11
    sprite('rc032_12', 4)	# 12-15
    sprite('rc032_13', 4)	# 16-19
    sprite('rc032_14', 4)	# 20-23
    sprite('rc032_15', 6)	# 24-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('rc033_00', 1)	# 1-1
    sprite('rc033_01', 2)	# 2-3
    sprite('rc033_01', 2)	# 4-5
    loopRest()
    label(0)
    sprite('rc033_02', 3)	# 6-8
    sprite('rc033_03', 3)	# 9-11
    sprite('rc033_04', 3)	# 12-14
    sprite('rc033_05', 3)	# 15-17
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc033_06', 3)	# 18-20
    sprite('rc033_07', 3)	# 21-23

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2042(1)
        Unknown1084(0)
        Unknown11063(1)

        def upon_STATE_END():
            Unknown3001(255)
    sprite('null', 1)	# 1-1
    Unknown1086(24)
    teleportRelativeY(0)
    Unknown23001(0, 0)
    Unknown3001(0)
    Unknown3004(0)
    GFX_1('haef_event_lose_end', 0)
    sprite('rc406_15', 4)	# 2-5
    GFX_0('rcef_602EntryPtc', -1)
    Unknown3004(15)
    sprite('rc406_16', 4)	# 6-9
    sprite('rc406_17', 4)	# 10-13
    sprite('rc406_18', 4)	# 14-17
    loopRest()
    Unknown3004(0)
    Unknown3001(255)
    Unknown23001(100, 100)
    sprite('keep', 100)	# 18-117

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        setGravity(1300)
        Unknown23012(0, 0, 0)
        Unknown1017()
        Unknown1022()
        Unknown1037()
        Unknown1084(1)
        Unknown2034(1)

        def upon_3():
            Unknown23012(0, 0, 0)
            if (not Unknown30042(25)):
                Unknown2034(0)
            if (SLOT_18 == 5):
                Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
                SFX_0('301_overdrive_end')
            if (SLOT_18 == 59):
                Unknown1018()
                Unknown1023()
                Unknown1038()
                Unknown1019(40)
                YAccel(40)
            if (SLOT_18 == 72):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('rc412_00', 4)	# 1-4
    sprite('rc412_01', 4)	# 5-8
    label(0)
    sprite('rc412_02', 5)	# 9-13
    sprite('rc412_03', 5)	# 14-18
    sprite('rc412_04', 5)	# 19-23
    sprite('rc412_05', 5)	# 24-28
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc412_06', 4)	# 29-32
    sprite('rc412_07', 4)	# 33-36

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('rc260_01', 3)	# 26-28
    Unknown1086(22)
    teleportRelativeX(-100000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('rc260_02', 3)	# 29-31
    sprite('rc260_03', 3)	# 32-34
    sprite('rc260_04', 3)	# 35-37
    label(1)
    sprite('rc260_05', 2)	# 38-39	 **attackbox here**
    GFX_1('rcef_falldown', -1)
    GFX_0('DownFallMcA', -1)
    GFX_0('DownFallMcB', 0)
    sprite('rc260_06', 2)	# 40-41	 **attackbox here**
    sprite('rc260_07', 2)	# 42-43	 **attackbox here**
    GFX_1('rcef_falldown', -1)
    sprite('rc260_08', 2)	# 44-45	 **attackbox here**
    sprite('rc260_09', 2)	# 46-47	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('rc260_09ex', 3)	# 48-50	 **attackbox here**
    sprite('rc260_10', 0)	# 51-50
    Unknown8004(100, 1, 1)
    Unknown1084(1)
    ScreenShake(0, 10000)
    GFX_1('rcef_falldown_mc02', -1)
    sprite('rc260_11', 3)	# 51-53
    sprite('rc260_12', 3)	# 54-56
    sprite('rc260_13', 3)	# 57-59
    sprite('rc260_14', 3)	# 60-62
    sprite('rc260_15', 3)	# 63-65
    sprite('rc260_15ex01', 2)	# 66-67
    sprite('rc260_16', 2)	# 68-69
    sprite('rc260_17', 2)	# 70-71

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rc033_01', 2)	# 1-2
    sprite('rc033_02', 3)	# 3-5
    sprite('rc033_03', 3)	# 6-8
    sprite('rc033_04', 3)	# 9-11
    sprite('rc033_05', 3)	# 12-14
    sprite('rc033_02', 3)	# 15-17
    sprite('rc033_03', 3)	# 18-20
    sprite('rc033_04', 3)	# 21-23
    sprite('rc033_05', 3)	# 24-26
    sprite('rc033_02', 3)	# 27-29
    sprite('rc033_03', 3)	# 30-32
    sprite('rc033_04', 30)	# 33-62

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rc001_00', 5)	# 1-5
    sprite('rc001_01', 5)	# 6-10
    sprite('rc001_02', 5)	# 11-15
    sprite('rc001_03', 5)	# 16-20
    sprite('rc001_04', 5)	# 21-25
    sprite('rc001_05', 5)	# 26-30
    sprite('rc001_06', 5)	# 31-35
    sprite('rc001_07', 5)	# 36-40
    sprite('rc001_08', 5)	# 41-45
    sprite('rc001_09', 16)	# 46-61
    sprite('rc001_10', 5)	# 62-66
    sprite('rc001_11', 5)	# 67-71
    sprite('rc001_12', 30)	# 72-101
    loopRest()

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        Unknown30040(1)
        Unknown2003(1)
        Unknown23012(0, 0, 0)
        Unknown2006()
    sprite('rc401_00', 3)	# 1-3	 **attackbox here**
    sprite('rc401_01', 3)	# 4-6	 **attackbox here**
    sprite('rc401_02', 3)	# 7-9	 **attackbox here**
    sprite('rc401_03', 2)	# 10-11	 **attackbox here**
    sprite('rc401_04', 2)	# 12-13	 **attackbox here**
    sprite('rc401_05', 2)	# 14-15	 **attackbox here**
    sprite('rc401_06', 2)	# 16-17	 **attackbox here**
    sprite('rc401_07', 2)	# 18-19	 **attackbox here**
    sprite('rc401_08', 5)	# 20-24	 **attackbox here**
    Unknown7007('6272633230315f300000000000000000640000006272633230315f310000000000000000640000006272633230315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('rcse_25')
    GFX_1('rcef401_bom', 0)
    callSubroutine('Shot_Stack')
    GFX_0('LightningRod_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3108, 0)
    sprite('rc401_08', 5)	# 25-29	 **attackbox here**
    SFX_3('rcse_25')
    GFX_1('rcef401_bom', 0)
    callSubroutine('Shot_Stack')
    GFX_0('LightningRod_TAG', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3109, 0)
    sprite('rc401_09', 5)	# 30-34	 **attackbox here**
    sprite('rc401_10', 3)	# 35-37	 **attackbox here**
    sprite('rc401_11', 3)	# 38-40	 **attackbox here**
    sprite('rc401_12', 3)	# 41-43	 **attackbox here**
    sprite('rc401_13', 3)	# 44-46	 **attackbox here**
    sprite('rc401_14', 3)	# 47-49	 **attackbox here**
    Recovery()
    sprite('rc401_15', 3)	# 50-52	 **attackbox here**
    sprite('rc401_16', 3)	# 53-55
    sprite('rc401_17', 2)	# 56-57

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        Unknown30040(1)
        Unknown2003(1)
        Unknown11063(1)
        Unknown23012(0, 0, 0)
        Unknown2006()
    sprite('rc216_00', 2)	# 1-2
    Unknown7007('6272633230385f300000000000000000640000006272633230385f310000000000000000640000006272633230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rc216_01', 2)	# 3-4
    sprite('rc216_02', 2)	# 5-6
    sprite('rc216_03', 2)	# 7-8
    sprite('rc216_04', 2)	# 9-10
    sprite('rc216_05', 2)	# 11-12
    GFX_0('LightningObjAtkMiniD_TAG', -1)
    Unknown23029(4, 3001, 0)
    Unknown23029(5, 3001, 0)
    Unknown23029(6, 3001, 0)
    Unknown23012(0, 0, 0)
    sprite('rc216_06', 6)	# 13-18
    SFX_0('003_swing_grap_0_2')
    sprite('rc216_07', 6)	# 19-24
    sprite('rc216_08', 4)	# 25-28
    sprite('rc216_09', 4)	# 29-32
    sprite('rc216_10', 4)	# 33-36
    sprite('rc216_11', 4)	# 37-40
    sprite('rc216_12', 4)	# 41-44

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(400)
        AttackP1(70)
        Unknown11092(1)
        AirPushbackX(2000)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(10)
        AirUntechableTime(36)
        Hitstop(1)
        HitAirUnblockable(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        Unknown11057(600)
        Unknown30055('400d03003200000032000000')
        Unknown30056('000000003200000000000000')
        Unknown11042(1)
        Unknown23012(120, 100, 100)
        Unknown22004(5, 1)
        Unknown1084(0)
        Unknown30040(1)
        JumpCancel_(0)
        Unknown2006()
    sprite('rc212_00', 4)	# 1-4
    physicsXImpulse(6000)
    sprite('rc212_01', 4)	# 5-8
    physicsXImpulse(24000)
    sprite('rc212_02', 4)	# 9-12
    Unknown23087(30000)
    physicsYImpulse(12000)
    setGravity(1000)
    sendToLabelUpon(2, 2)
    sprite('rc212_03ex', 3)	# 13-15	 **attackbox here**
    SFX_3('rcse_11')
    Unknown7007('6272633130385f300000000000000000640000006272633130385f310000000000000000640000006272633130385f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown9010('01000000626e673130310000000000000000000032000000626e67313039000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_0('019_cloth_c')
    RefreshMultihit()
    GFX_1('rcef_212_mc00', -1)
    GFX_0('rcef_212Rose', -1)
    GFX_0('rcef212windA', -1)
    GFX_0('rcef212windB', -1)
    sprite('rc212_04', 3)	# 16-18	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_05', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_06', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_07', 3)	# 25-27	 **attackbox here**
    SFX_0('019_cloth_c')
    RefreshMultihit()
    sprite('rc212_08', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_09', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('rc212_03', 3)	# 34-36	 **attackbox here**
    SFX_3('rcse_11')
    SFX_0('019_cloth_c')
    PushbackX(30000)
    RefreshMultihit()
    GFX_0('rcef_212Rose', -1)
    GFX_0('rcef212windA', -1)
    GFX_0('rcef212windB', -1)
    sprite('rc212_04', 3)	# 37-39	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_05', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_06', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_07', 3)	# 46-48	 **attackbox here**
    SFX_0('019_cloth_c')
    RefreshMultihit()
    sprite('rc212_08', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_09', 3)	# 52-54	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rc212_10', 4)	# 55-58
    Unknown23087(0)
    StartMultihit()
    Unknown8000(100, 1, 1)
    Unknown1019(10)
    StartMultihit()
    Recovery()
    sprite('rc212_11', 4)	# 59-62
    StartMultihit()
    sprite('rc212_12', 4)	# 63-66
    sprite('rc212_13', 4)	# 67-70
    sprite('rc212_14', 6)	# 71-76

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
    Unknown2036(71, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('rc020_06', 4)	# 3-6
    sprite('rc020_07', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('LightningLandB_DDDOD')
    else:
        enterState('LightningLandB_DDD')

@State
def LightningLandB_DDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        sendToLabelUpon(2, 2)
        Unknown30063(1)
    sprite('rc430_00', 4)	# 1-4
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(1)
    sprite('rc430_00add', 4)	# 5-8
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_01', 4)	# 9-12
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_02', 4)	# 13-16
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    physicsYImpulse(1600)
    setGravity(0)
    sprite('rc430_03', 4)	# 17-20
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_04', 4)	# 21-24
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_05', 4)	# 25-28
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_06', 4)	# 29-32
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_07', 4)	# 33-36
    physicsYImpulse(0)
    sprite('rc430_08', 4)	# 37-40
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_09', 4)	# 41-44
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtk', 104)
    Unknown23029(1, 3007, 0)
    sprite('rc430_10', 4)	# 45-48
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_11', 4)	# 49-52
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_12', 4)	# 53-56
    Unknown7007('6272633235305f300000000000000000640000006272633235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(0)
    loopRest()
    sprite('rc430_13', 4)	# 57-60
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 61-64
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 65-68
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 69-72
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 73-76
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 77-80
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 81-84
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 85-88
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 89-92
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 93-96
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 97-100
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 101-104
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 105-108
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 109-112
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 113-116
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 117-120
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    sprite('rc430_13', 4)	# 121-124
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 125-128
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 129-132
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 133-136
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    setGravity(1000)
    label(0)
    sprite('rc430_13', 4)	# 137-140
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 141-144
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 145-148
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 149-152
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('rc430_17', 2)	# 153-154
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_18', 4)	# 155-158
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_19', 4)	# 159-162
    SFX_FOOTSTEP_(100, 1, 1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_20', 4)	# 163-166
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')

@State
def LightningLandB_DDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        sendToLabelUpon(2, 2)
        Unknown30063(1)
    sprite('rc430_00', 4)	# 1-4
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(1)
    sprite('rc430_00add', 4)	# 5-8
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_01', 4)	# 9-12
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_02', 4)	# 13-16
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    physicsYImpulse(1600)
    setGravity(0)
    sprite('rc430_03', 4)	# 17-20
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_04', 4)	# 21-24
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_05', 4)	# 25-28
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_06', 4)	# 29-32
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_07', 4)	# 33-36
    physicsYImpulse(0)
    sprite('rc430_08', 4)	# 37-40
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_09', 4)	# 41-44
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtk_Matome', 104)
    Unknown23029(1, 3008, 0)
    sprite('rc430_10', 4)	# 45-48
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_11', 4)	# 49-52
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_12', 4)	# 53-56
    Unknown7007('6272633235305f300000000000000000640000006272633235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(0)
    loopRest()
    sprite('rc430_13', 4)	# 57-60
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 61-64
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 65-68
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 69-72
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 73-76
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 77-80
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 81-84
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 85-88
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 89-92
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 93-96
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 97-100
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 101-104
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 105-108
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 109-112
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 113-116
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 117-120
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    sprite('rc430_13', 4)	# 121-124
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 125-128
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 129-132
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 133-136
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    setGravity(1000)
    label(0)
    sprite('rc430_13', 4)	# 137-140
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 141-144
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 145-148
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 149-152
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('rc430_17', 2)	# 153-154
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_18', 4)	# 155-158
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_19', 4)	# 159-162
    SFX_FOOTSTEP_(100, 1, 1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_20', 4)	# 163-166
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('rc001_00', 6)	# 1-6
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    sprite('rc001_01', 6)	# 7-12
    sprite('rc001_02', 6)	# 13-18
    sprite('rc001_03', 6)	# 19-24
    SFX_0('019_cloth_b')
    sprite('rc001_04', 6)	# 25-30
    sprite('rc001_05', 6)	# 31-36
    sprite('rc001_06', 6)	# 37-42
    sprite('rc001_07', 6)	# 43-48
    sprite('rc001_08', 6)	# 49-54
    sprite('rc001_09', 6)	# 55-60
    sprite('rc001_10', 5)	# 61-65
    label(1)
    sprite('rc001_10', 1)	# 66-66
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rc001_11', 6)	# 67-72
    sprite('rc001_12', 6)	# 73-78
    loopRest()

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
    sprite('rc260_01', 3)	# 121-123
    Unknown1086(22)
    teleportRelativeX(-100000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    sprite('rc260_02', 3)	# 124-126
    sprite('rc260_03', 3)	# 127-129
    sprite('rc260_04', 3)	# 130-132
    label(1)
    sprite('rc260_05ex', 2)	# 133-134	 **attackbox here**
    GFX_1('rcef_falldown', -1)
    GFX_0('DownFallMcA', -1)
    GFX_0('DownFallMcB', 0)
    sprite('rc260_06ex', 2)	# 135-136	 **attackbox here**
    sprite('rc260_07ex', 2)	# 137-138	 **attackbox here**
    GFX_1('rcef_falldown', -1)
    sprite('rc260_08ex', 2)	# 139-140	 **attackbox here**
    sprite('rc260_09ex', 2)	# 141-142	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('rc260_10', 2)	# 143-144
    Unknown8004(100, 1, 1)
    Unknown1084(1)
    ScreenShake(0, 10000)
    GFX_1('rcef_falldown_mc02', -1)
    sprite('rc260_11', 8)	# 145-152
    sprite('rc260_12', 3)	# 153-155
    sprite('rc260_13', 3)	# 156-158
    sprite('rc260_14', 3)	# 159-161
    sprite('rc260_15', 3)	# 162-164
    sprite('rc260_15ex01', 3)	# 165-167
    sprite('rc260_16', 3)	# 168-170
    sprite('rc260_17', 3)	# 171-173

@State
def CmnActChangeReturnAppealBurst():
    sprite('rc091_00', 2)	# 1-2
    sprite('rc091_01', 2)	# 3-4
    sprite('rc091_02', 21)	# 5-25
    sprite('rc091_03', 5)	# 26-30
    sprite('rc091_04', 5)	# 31-35
    sprite('rc010_04', 5)	# 36-40
    sprite('rc010_03', 5)	# 41-45
    sprite('rc010_02', 5)	# 46-50
    sprite('rc010_01', 5)	# 51-55
    sprite('rc010_00', 5)	# 56-60
    sprite('rc000_00', 30)	# 61-90

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        Unknown12051(2)

        def upon_ON_HIT_OR_BLOCK():
            GFX_1('rcef200hataki', 101)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('rc200_00', 1)	# 1-1
    Unknown1051(60)
    sprite('rc200_01', 2)	# 2-3
    sprite('rc200_02', 2)	# 4-5
    sprite('rc200_03', 2)	# 6-7	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    Unknown9010('01000000626e673130300000000000000000000032000000626e67313035000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rc200_04', 2)	# 8-9
    sprite('rc200_05', 2)	# 10-11
    sprite('rc200_06', 2)	# 12-13
    sprite('rc200_07', 3)	# 14-16	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    RefreshMultihit()
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        GFX_1('rcef200hataki', 101)
    sprite('rc200_08', 3)	# 17-19
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('rc200_08', 4)	# 20-23
    sprite('rc200_09', 4)	# 24-27

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(16000)
        PushbackX(15300)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('rc201_col_dmy')
            WhiffCancelEnable(1)
            Unknown13008(1)
            Unknown13015(1)
            WhiffCancel('NmlAtk5AA')
            WhiffCancel('NmlAtk2A')
            WhiffCancel('NmlAtk5B')
            WhiffCancel('NmlAtk2B')
            WhiffCancel('NmlAtk2C')
            WhiffCancel('CmnActCrushAttack')
            WhiffCancel('NmlAtkThrow')
            WhiffCancel('NmlAtkBackThrow')

        def upon_3():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('rc201_00', 2)	# 1-2
    sprite('rc201_01', 2)	# 3-4
    sprite('rc201_02', 3)	# 5-7
    sprite('rc201_03', 3)	# 8-10	 **attackbox here**
    Unknown7009(1)
    Unknown9010('01000000626e673130365f30000000000000000032000000626e67313038000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('rc201_Wind', 0)
    GFX_0('rcef_201rose', 1)
    GFX_1('rcef_201wind', 2)
    GFX_1('rcef_201light', 3)
    GFX_0('rc201_col_dmy', -1)
    sprite('rc201_04', 3)	# 11-13	 **attackbox here**
    sprite('rc201_05', 1)	# 14-14
    Recovery()
    Unknown2063()
    sprite('rc201_06', 1)	# 15-15
    sprite('rc201_07', 1)	# 16-16
    sprite('rc201_08', 1)	# 17-17
    sprite('rc201_09', 2)	# 18-19
    sprite('rc201_10', 2)	# 20-21
    sprite('rc201_11', 2)	# 22-23
    sprite('rc201_12', 2)	# 24-25
    sprite('rc201_13', 2)	# 26-27
    sprite('rc201_14', 1)	# 28-28

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1200)
        AirPushbackX(-5000)
        AirPushbackY(16000)
        PushbackX(-6000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('rc406_col_dmy')
            WhiffCancelEnable(1)
            Unknown13008(1)
            Unknown13015(1)
            WhiffCancel('NmlAtk5AAA')
            WhiffCancel('NmlAtk2A')
            WhiffCancel('NmlAtk5B')
            WhiffCancel('NmlAtk2B')
            WhiffCancel('NmlAtk2C')
            WhiffCancel('CmnActCrushAttack')
            WhiffCancel('NmlAtkThrow')
            WhiffCancel('NmlAtkBackThrow')

        def upon_3():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('rc406_00ex01', 2)	# 1-2
    sprite('rc406_01ex01', 2)	# 3-4
    sprite('rc406_04ex01', 2)	# 5-6
    sprite('rc406_05ex01', 2)	# 7-8
    sprite('rc406_06ex01', 2)	# 9-10
    sprite('rc406_08ex01', 2)	# 11-12
    sprite('rc406_09ex01', 2)	# 13-14
    Unknown7009(2)
    sprite('rc406_12ex01', 3)	# 15-17	 **attackbox here**
    GFX_0('rc201_Wind', 3)
    GFX_0('rcef_201rose', 3)
    GFX_1('rcef_201wind', 3)
    GFX_1('rcef_201light', 3)
    GFX_0('rc406_col_dmy', -1)
    sprite('rc406_13ex01', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('rc406_14ex01', 3)	# 21-23
    sprite('rc406_15ex01', 3)	# 24-26
    sprite('rc406_16ex01', 3)	# 27-29
    sprite('rc406_17ex01', 3)	# 30-32
    sprite('rc406_18ex01', 3)	# 33-35

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(180)
        Unknown11092(1)
        AirPushbackX(2000)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(10)
        Hitstop(2)
        HitAirUnblockable(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        Unknown11057(600)
        Unknown30055('400d03003200000032000000')
        Unknown30056('50c300001e00000000000000')
        Unknown23012(120, 100, 100)
        Unknown22004(5, 1)
        callSubroutine('AddChainWind')
    sprite('rc212_00', 2)	# 1-2
    sprite('rc212_01', 2)	# 3-4
    sprite('rc212_02', 2)	# 5-6
    Unknown23087(30000)
    physicsXImpulse(6000)
    physicsYImpulse(16000)
    setGravity(1000)
    sendToLabelUpon(2, 2)
    sprite('rc212_03', 3)	# 7-9	 **attackbox here**
    SFX_3('rcse_11')
    Unknown7007('6272633130385f300000000000000000640000006272633130385f310000000000000000640000006272633130385f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown9010('01000000626e673130310000000000000000000032000000626e67313039000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_0('019_cloth_c')
    RefreshMultihit()
    GFX_1('rcef_212_mc00', -1)
    GFX_0('rcef_212Rose', -1)
    GFX_0('rcef212windA', -1)
    GFX_0('rcef212windB', -1)
    sprite('rc212_04', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_05', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_06', 3)	# 16-18	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_07', 3)	# 19-21	 **attackbox here**
    SFX_0('019_cloth_c')
    RefreshMultihit()
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5AAAA')
    sprite('rc212_08', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    clearUponHandler(10)
    HitOrBlockCancel('NmlAtk5AAAA')
    sprite('rc212_09', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('rc212_03', 3)	# 28-30	 **attackbox here**
    SFX_3('rcse_11')
    SFX_0('019_cloth_c')
    PushbackX(30000)
    RefreshMultihit()
    GFX_0('rcef_212Rose', -1)
    GFX_0('rcef212windA', -1)
    GFX_0('rcef212windB', -1)
    sprite('rc212_04', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_05', 3)	# 34-36	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_06', 3)	# 37-39	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_07', 3)	# 40-42	 **attackbox here**
    SFX_0('019_cloth_c')
    RefreshMultihit()
    sprite('rc212_08', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    sprite('rc212_09', 3)	# 46-48	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rc212_10', 4)	# 49-52
    Unknown23087(0)
    StartMultihit()
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    StartMultihit()
    Recovery()
    Unknown2063()
    WhiffCancelEnable(0)
    sprite('rc212_11', 4)	# 53-56
    StartMultihit()
    sprite('rc212_12', 4)	# 57-60
    sprite('rc212_13', 4)	# 61-64
    sprite('rc212_14', 6)	# 65-70

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(100)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(-40000)
        AirUntechableTime(40)
        Unknown9310(1)
        Unknown23027()
        HitOverhead(0)
        JumpCancel_(0)
        Unknown30068(1)
        Unknown23019(0)
        Unknown22004(10, 1)
    sprite('rc320_00', 2)	# 1-2
    physicsXImpulse(3000)
    physicsYImpulse(10000)
    Unknown1043()
    sprite('rc320_01', 2)	# 3-4
    sprite('rc320_02', 3)	# 5-7	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    sprite('rc321_03', 6)	# 8-13	 **attackbox here**
    RefreshMultihit()
    SFX_0('004_swing_grap_1_2')
    SFX_1('brc153')
    sprite('rc321_04', 4)	# 14-17
    Recovery()
    sprite('rc321_05', 4)	# 18-21
    sprite('rc321_06', 3)	# 22-24
    sprite('rc321_07', 3)	# 25-27
    sprite('rc321_08', 3)	# 28-30

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(16000)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('rc211_00', 1)	# 1-1
    sprite('rc211_01', 2)	# 2-3
    sprite('rc211_02', 2)	# 4-5
    sprite('rc211_03', 2)	# 6-7
    sprite('rc211_04', 1)	# 8-8
    sprite('rc211_05', 1)	# 9-9
    sprite('rc211_06', 1)	# 10-10
    SFX_0('003_swing_grap_0_1')
    Unknown7009(0)
    Unknown9010('020000006267793130345f30000000000000000032000000626e67313035000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rc211_07', 3)	# 11-13	 **attackbox here**
    sprite('rc211_08', 3)	# 14-16
    Recovery()
    Unknown2063()
    sprite('rc211_09', 3)	# 17-19
    sprite('rc211_10', 3)	# 20-22
    sprite('rc211_11', 3)	# 23-25
    sprite('rc211_12', 3)	# 26-28

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        PushbackX(12000)
        Unknown9016(1)
        Unknown23012(130, 100, 20)
        HitOrBlockCancel('NmlAtk5BBB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('rc202_02', 2)	# 1-2	 **attackbox here**
    sprite('rc202_04', 2)	# 3-4	 **attackbox here**
    GFX_1('rcef_kirakiraA', 0)
    Unknown1045(80000)
    physicsXImpulse(18000)
    sprite('rc202_07', 3)	# 5-7	 **attackbox here**
    GFX_1('rcef_kirakiraA', 0)
    sprite('rc202_08', 3)	# 8-10	 **attackbox here**
    GFX_1('rcef_kirakiraA', 0)
    sprite('rc202_09', 1)	# 11-11	 **attackbox here**
    GFX_1('rcef_kirakiraA', 0)
    sprite('rc202_10', 1)	# 12-12	 **attackbox here**
    SFX_0('006_swing_blade_2')
    Unknown7009(2)
    Unknown9010('020000006267793130345f300000000000000000320000006267793130345f310000000000000000320000006267793130355f300000000000000000320000006267793130355f31000000000000000032000000')
    GFX_1('rcef_kirakiraB', 0)
    GFX_1('rcef_202mc01', 1)
    sprite('rc202_11', 2)	# 13-14	 **attackbox here**
    GFX_1('rcef_kirakiraB', 0)
    GFX_0('rcef_202tsuki', 1)
    GFX_0('rc202SwordLight', -1)
    sprite('rc202_11', 2)	# 15-16	 **attackbox here**
    GFX_1('rcef_kirakiraB', 1)
    sprite('rc202_11', 2)	# 17-18	 **attackbox here**
    GFX_1('rcef_kirakiraB', 1)
    sprite('rc202_11', 2)	# 19-20	 **attackbox here**
    Unknown1051(20)
    Unknown1019(80)
    GFX_1('rcef_kirakiraB', 2)
    sprite('rc202_12', 4)	# 21-24	 **attackbox here**
    Unknown1051(20)
    Unknown1019(60)
    GFX_1('rcef_kirakiraB', 0)
    Recovery()
    Unknown2063()
    sprite('rc202_14', 3)	# 25-27	 **attackbox here**
    Unknown1019(20)
    sprite('rc202_15', 3)	# 28-30	 **attackbox here**
    sprite('rc202_16', 3)	# 31-33
    sprite('rc202_17', 3)	# 34-36
    sprite('rc202_18', 3)	# 37-39
    sprite('rc202_19', 3)	# 40-42

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirUntechableTime(50)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(9)
        Unknown9130(5)
        Unknown9142(50)
        AirPushbackX(44000)
        AirPushbackY(8000)
        PushbackX(70000)
        Unknown9016(1)
        Unknown1045(30000)
        Unknown23012(150, 100, 100)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        callSubroutine('AddChainWind')
    sprite('rc202_12', 2)	# 1-2	 **attackbox here**
    sprite('rc202_21', 2)	# 3-4	 **attackbox here**
    sprite('rc202_21ex01', 6)	# 5-10	 **attackbox here**
    sprite('rc202_22', 4)	# 11-14	 **attackbox here**
    Unknown9010('01000000626e673130365f30000000000000000032000000626e67313038000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23012(40, 100, 100)
    SFX_3('rcse_01')
    SFX_0('006_swing_blade_2')
    GFX_0('rcef_202rose', 0)
    GFX_0('rcef_202wind', 1)
    ScreenShake(10000, 0)
    WhiffCancelEnable(0)
    sprite('rc202_23', 4)	# 15-18	 **attackbox here**
    sprite('rc202_14', 3)	# 19-21	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('rc202_15', 3)	# 22-24	 **attackbox here**
    sprite('rc202_16', 3)	# 25-27
    sprite('rc202_17', 3)	# 28-30
    sprite('rc202_18', 3)	# 31-33
    sprite('rc202_19', 3)	# 34-36

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('rc231_col_dmy')
            WhiffCancelEnable(1)
            Unknown13008(1)
            Unknown13015(1)
            WhiffCancel('NmlAtk5A')
            WhiffCancel('NmlAtk5B')
            WhiffCancel('NmlAtk2B')
            WhiffCancel('NmlAtk2C')
            WhiffCancel('CmnActCrushAttack')
            WhiffCancel('NmlAtkThrow')
            WhiffCancel('NmlAtkBackThrow')

        def upon_3():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('rc231_01', 3)	# 1-3
    sprite('rc231_02', 3)	# 4-6
    sprite('rc231_03', 3)	# 7-9
    sprite('rc231_04', 3)	# 10-12	 **attackbox here**
    GFX_0('rc231_Wind', 0)
    GFX_0('rcef_231rose', 1)
    GFX_1('rcef_231wind', 2)
    GFX_1('rcef_231light', 3)
    Unknown7009(1)
    Unknown9010('020000006267793130325f300000000000000000320000006267793130325f310000000000000000320000006267793130335f300000000000000000320000006267793130335f31000000000000000032000000')
    GFX_0('rc231_col_dmy', -1)
    sprite('rc231_05', 3)	# 13-15	 **attackbox here**
    sprite('rc231_06', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('rc231_07', 3)	# 19-21
    sprite('rc231_08', 3)	# 22-24
    sprite('rc231_09', 3)	# 25-27
    sprite('rc231_10', 3)	# 28-30
    sprite('rc231_11', 3)	# 31-33

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(5)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackY(40000)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
        Unknown9266(7)
        JumpCancel_(0)
        Unknown23017(0)
        Unknown2018(0, 50)
    sprite('rc232_00', 2)	# 1-2
    sprite('rc232_01', 2)	# 3-4
    sprite('rc232_02', 2)	# 5-6
    setInvincible(1)
    GuardPoint_(1)
    Unknown22019('0100000001000000010000000100000000000000')
    Unknown22030(0)
    sprite('rc232_03', 2)	# 7-8
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_sl')
    sprite('rc232_04', 2)	# 9-10
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    sprite('rc232_05', 3)	# 11-13	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_sl')
    sprite('rc232_06', 3)	# 14-16	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    sprite('rc232_07', 1)	# 17-17	 **attackbox here**
    Unknown7009(2)
    Unknown9010('010000006e673131360000000000000000000000320000006e6731313700000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_1('rcef_pachin', 0)
    GFX_0('rcef232ChairMc', -1)
    GFX_0('rc232ElectlicChair', -1)
    SFX_3('rcse_26')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_s')
    sprite('rc232_08', 1)	# 18-18	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_s')
    sprite('rc232_08add01', 1)	# 19-19	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_s')
    sprite('rc232_08add02', 1)	# 20-20	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_s')
    sprite('rc232_08', 1)	# 21-21	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_sl')
    SFX_0('014_electric_s')
    sprite('rc232_08add01', 1)	# 22-22	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_s')
    sprite('rc232_08add02', 1)	# 23-23	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_s')
    sprite('rc232_08ex01', 1)	# 24-24	 **attackbox here**
    setInvincible(0)
    sprite('rc232_08ex02', 1)	# 25-25	 **attackbox here**
    sprite('rc232_08ex03', 1)	# 26-26	 **attackbox here**
    sprite('rc232_08ex01', 1)	# 27-27	 **attackbox here**
    sprite('rc232_08ex02', 1)	# 28-28	 **attackbox here**
    sprite('rc232_08ex03', 1)	# 29-29	 **attackbox here**
    sprite('rc232_08ex01', 1)	# 30-30	 **attackbox here**
    sprite('rc232_08ex02', 1)	# 31-31	 **attackbox here**
    sprite('rc232_08ex03', 1)	# 32-32	 **attackbox here**
    sprite('rc232_08ex01', 1)	# 33-33	 **attackbox here**
    sprite('rc232_08ex02', 1)	# 34-34	 **attackbox here**
    sprite('rc232_08ex03', 1)	# 35-35	 **attackbox here**
    sprite('rc232_08ex01', 1)	# 36-36	 **attackbox here**
    sprite('rc232_08ex02', 1)	# 37-37	 **attackbox here**
    sprite('rc232_09', 3)	# 38-40	 **attackbox here**
    sprite('rc232_10', 3)	# 41-43
    sprite('rc232_11', 3)	# 44-46
    sprite('rc232_12', 3)	# 47-49
    sprite('rc232_13', 3)	# 50-52
    sprite('rc232_14', 3)	# 53-55
    sprite('rc232_15', 3)	# 56-58

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(600)
        AttackP1(90)
        AttackP2(70)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(13500)
        AirUntechableTime(80)
        Unknown11065(1)
        Hitstop(8)
        Unknown9016(1)
        HitLow(2)
        Unknown23012(100, 100, 250)

        def upon_11():
            SLOT_51 = 1

        def upon_3():
            if SLOT_51:
                clearUponHandler(11)
                clearUponHandler(3)
                HitLow(0)
    sprite('rc234_00', 2)	# 1-2
    sprite('rc234_01', 1)	# 3-3
    sprite('rc234_01', 1)	# 4-4
    Unknown7009(2)
    Unknown9010('01000000626e673130370000000000000000000032000000626e67313134000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    callSubroutine('AddChainWind')
    Unknown14084('Wind2')
    sprite('rc234_02', 2)	# 5-6
    SFX_0('004_swing_grap_1_2')
    sprite('rc234_03', 1)	# 7-7
    sprite('rc234_04', 1)	# 8-8
    sprite('rc234_05', 1)	# 9-9
    sprite('rc234_06', 2)	# 10-11	 **attackbox here**
    RefreshMultihit()
    WhiffCancelEnable(0)
    sprite('rc234_07', 2)	# 12-13	 **attackbox here**
    sprite('rc234_08', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('rc234_09', 1)	# 16-16	 **attackbox here**
    sprite('rc234_09', 1)	# 17-17	 **attackbox here**
    AirPushbackX(2000)
    CheckInput(0x13)
    Unknown19(9, 2, 0)
    sprite('rc234_10', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    JumpCancel_(0)
    Unknown2037(1)
    sprite('rc234_11', 2)	# 20-21	 **attackbox here**
    sprite('rc234_12', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('rc234_12ex01', 2)	# 24-25	 **attackbox here**
    SFX_0('004_swing_grap_1_2')
    sprite('rc234_06', 2)	# 26-27	 **attackbox here**
    RefreshMultihit()
    sprite('rc234_07', 2)	# 28-29	 **attackbox here**
    sprite('rc234_08', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    sprite('rc234_09', 2)	# 32-33	 **attackbox here**
    label(9)
    sprite('rc234_13', 2)	# 34-35	 **attackbox here**
    SFX_0('004_swing_grap_1_2')
    RefreshMultihit()
    sprite('rc234_14', 2)	# 36-37	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('rc234_15', 3)	# 38-40
    sprite('rc234_16', 4)	# 41-44
    sprite('rc234_17', 4)	# 45-48
    sprite('rc234_18', 4)	# 49-52

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AirUntechableTime(17)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Unknown23012(100, 250, 20)
    sprite('rc250_00', 3)	# 1-3
    sprite('rc250_01', 2)	# 4-5
    callSubroutine('AddChainWind_Air')
    sprite('rc250_02', 2)	# 6-7
    sprite('rc250_03', 6)	# 8-13	 **attackbox here**
    Unknown7009(3)
    Unknown9010('01000000626e673130320000000000000000000032000000626e67313039000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_0('003_swing_grap_0_0')
    WhiffCancelEnable(0)
    sprite('rc250_04', 4)	# 14-17
    Recovery()
    Unknown2063()
    sprite('rc250_05', 4)	# 18-21
    sprite('rc250_06', 4)	# 22-25

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AirUntechableTime(17)
        AirPushbackY(20000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rc251_00', 3)	# 1-3
    sprite('rc251_01', 1)	# 4-4
    callSubroutine('AddChainWind_Air')
    sprite('rc251_02', 1)	# 5-5
    sprite('rc251_03', 3)	# 6-8	 **attackbox here**
    SFX_0('003_swing_grap_0_0')
    Unknown7009(3)
    Unknown9010('01000000626e673130320000000000000000000032000000626e67313039000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rc251_04', 3)	# 9-11	 **attackbox here**
    sprite('rc251_05', 3)	# 12-14
    Recovery()
    Unknown2063()
    sprite('rc251_06', 3)	# 15-17
    sprite('rc251_07', 3)	# 18-20
    sprite('rc251_08', 3)	# 21-23

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP2(75)
        Unknown9016(1)
        AirUntechableTime(24)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(28000)
        HitOverhead(0)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rc252_00', 4)	# 1-4
    sprite('rc252_01', 3)	# 5-7	 **attackbox here**
    callSubroutine('AddChainWind_Air')
    sprite('rc252_02', 3)	# 8-10	 **attackbox here**
    SFX_3('rcse_01')
    Unknown7009(5)
    Unknown9010('01000000626e673131330000000000000000000032000000626e67313038000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_0('006_swing_blade_2')
    GFX_0('rcef_252Wind', 0)
    GFX_0('rcef252windA', 0)
    GFX_0('rcef252windB', 0)
    sprite('rc252_03', 3)	# 11-13	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('rc252_04', 5)	# 14-18	 **attackbox here**
    Recovery()
    sprite('rc252_05', 5)	# 19-23	 **attackbox here**
    SFX_3('rcse_01')
    Unknown2063()
    sprite('rc252_20', 5)	# 24-28	 **attackbox here**
    sprite('rc252_21', 5)	# 29-33

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown13021(1)
        AttackLevel_(3)
        AttackP2(80)
        AirUntechableTime(90)
        AirHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(-50000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(40)
        Unknown9016(1)
        JumpCancel_(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)

        def upon_3():
            if (SLOT_13 < (-30000)):
                AttackLevel_(4)
                AttackP2(75)
                Hitstop(20)
                Unknown9190(1)
                Unknown9118(60)

                def upon_ON_HIT_OR_BLOCK():
                    ScreenShake(30000, 0)
            if (SLOT_13 < (-60000)):
                AttackLevel_(5)
                AttackP2(80)
                Hitstop(30)
                Unknown9190(1)
                Unknown9118(60)
                Unknown11065(0)
                Unknown11042(2)

                def upon_ON_HIT_OR_BLOCK():
                    ScreenShake(80000, 0)
        Unknown23012(100, 150, 0)
    sprite('rc260_01', 3)	# 1-3
    sprite('rc260_02', 3)	# 4-6
    callSubroutine('AddChainWind_Air')
    sprite('rc260_03', 3)	# 7-9
    SFX_0('005_swing_grap_2_2')
    Unknown7009(5)
    Unknown1084(1)
    setGravity(1400)
    Unknown9010('020000006267793130365f300000000000000000320000006267793130365f310000000000000000320000006267793130375f300000000000000000320000006267793130375f31000000000000000032000000')
    sprite('rc260_04', 3)	# 10-12
    WhiffCancelEnable(0)
    label(0)
    sprite('rc260_05', 2)	# 13-14	 **attackbox here**
    GFX_1('rcef_falldown', -1)
    GFX_0('DownFallMcA', -1)
    GFX_0('DownFallMcB', 0)
    sprite('rc260_06', 2)	# 15-16	 **attackbox here**
    sprite('rc260_07', 2)	# 17-18	 **attackbox here**
    GFX_1('rcef_falldown', -1)
    HitOverhead(0)
    sprite('rc260_08', 2)	# 19-20	 **attackbox here**
    sprite('rc260_09', 2)	# 21-22	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc260_10', 2)	# 23-24
    Unknown8004(100, 1, 1)
    Unknown1084(1)
    ScreenShake(0, 10000)
    GFX_1('rcef_falldown_mc02', -1)
    Recovery()
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')
    sprite('rc260_11', 8)	# 25-32
    sprite('rc260_12', 3)	# 33-35
    sprite('rc260_13', 3)	# 36-38
    sprite('rc260_14', 3)	# 39-41
    sprite('rc260_15', 3)	# 42-44
    sprite('rc260_15ex01', 3)	# 45-47
    sprite('rc260_16', 3)	# 48-50
    sprite('rc260_17', 3)	# 51-53

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(15000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rc032_00', 4)	# 1-4
    sprite('rc032_01', 4)	# 5-8
    sprite('rc032_02', 4)	# 9-12
    SFX_0('000_airdash_0')
    Unknown8006(100, 1, 1)
    label(0)
    sprite('rc032_03', 4)	# 13-16
    sprite('rc032_04', 4)	# 17-20
    sprite('rc032_05', 4)	# 21-24
    sprite('rc032_06', 4)	# 25-28
    sprite('rc032_07', 4)	# 29-32
    sprite('rc032_08', 4)	# 33-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc310_00', 1)	# 37-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rc310_01', 2)	# 38-39
    sprite('rc310_02', 3)	# 40-42	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    Unknown1084(1)
    sprite('rc310_03', 4)	# 43-46
    SFX_4('brc154')
    sprite('rc310_04', 4)	# 47-50
    sprite('rc310_05', 6)	# 51-56
    sprite('rc310_06', 3)	# 57-59
    sprite('rc310_07', 3)	# 60-62
    sprite('rc310_08', 3)	# 63-65

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AirPushbackX(3000)
        AirPushbackY(32000)
        AttackP2(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
    sprite('rc310_02', 1)	# 1-1	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rc311_00', 3)	# 2-4
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_01', 3)	# 5-7
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_02', 3)	# 8-10
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_03', 3)	# 11-13
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_04', 6)	# 14-19
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_05', 2)	# 20-21
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_06', 2)	# 22-23
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_07', 2)	# 24-25	 **attackbox here**
    SFX_0('004_swing_grap_1_2')
    SFX_1('brc153')
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('rc311_08', 10)	# 26-35
    sprite('rc311_09', 3)	# 36-38
    sprite('rc311_10', 3)	# 39-41
    sprite('rc311_11', 3)	# 42-44
    sprite('rc311_12', 3)	# 45-47

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(15000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rc032_00', 4)	# 1-4
    sprite('rc032_01', 4)	# 5-8
    sprite('rc032_02', 4)	# 9-12
    SFX_0('000_airdash_0')
    Unknown8006(100, 1, 1)
    label(0)
    sprite('rc032_03', 4)	# 13-16
    sprite('rc032_04', 4)	# 17-20
    sprite('rc032_05', 4)	# 21-24
    sprite('rc032_06', 4)	# 25-28
    sprite('rc032_07', 4)	# 29-32
    sprite('rc032_08', 4)	# 33-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc310_00', 1)	# 37-37
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rc310_01', 2)	# 38-39
    sprite('rc310_02', 3)	# 40-42	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    Unknown1084(1)
    sprite('rc310_03', 4)	# 43-46
    SFX_4('brc154')
    sprite('rc310_04', 4)	# 47-50
    sprite('rc310_05', 6)	# 51-56
    sprite('rc310_06', 3)	# 57-59
    sprite('rc310_07', 3)	# 60-62
    sprite('rc310_08', 3)	# 63-65

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2018(1, 80)
        AttackLevel_(4)
        Damage(2000)
        AirPushbackX(3000)
        AirPushbackY(32000)
        AttackP2(50)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown11099(1)
        Unknown13021(1)
        Unknown21005(1)
    sprite('rc310_02', 1)	# 1-1	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('rc313_00', 3)	# 2-4
    Unknown5004()
    sprite('rc313_01', 3)	# 5-7
    teleportRelativeX(50000)
    sprite('rc313_02', 3)	# 8-10
    teleportRelativeX(50000)
    sprite('rc313_03', 3)	# 11-13
    teleportRelativeX(50000)
    sprite('rc313_04', 6)	# 14-19
    teleportRelativeX(50000)
    sprite('rc313_05', 3)	# 20-22
    sprite('rc313_06', 3)	# 23-25
    sprite('rc313_07', 10)	# 26-35	 **attackbox here**
    SFX_0('004_swing_grap_1_2')
    SFX_1('brc153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('rc313_08', 3)	# 36-38
    sprite('rc313_09', 3)	# 39-41
    sprite('rc313_10', 3)	# 42-44
    sprite('rc313_11', 3)	# 45-47
    sprite('rc313_12', 3)	# 48-50
    sprite('rc313_13', 2)	# 51-52

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(5)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackY(40000)
        Hitstop(3)
        PushbackX(12000)
        Unknown11058('0000000001000000000000000000000000000000')
        HitAirUnblockable(3)
    sprite('rc440_00', 3)	# 1-3
    setInvincible(1)
    sprite('rc440_01', 3)	# 4-6
    sprite('rc440_02', 3)	# 7-9
    sprite('rc440_03', 3)	# 10-12
    sprite('rc440_03', 3)	# 13-15
    Unknown7007('6272633130335f300000000000000000640000006272633130345f320000000000000000640000006272633130325f300000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('ActInvincibleAttack_Eff', 0)
    sprite('rc440_04', 4)	# 16-19	 **attackbox here**
    sprite('rc440_05', 4)	# 20-23
    setInvincible(0)
    sprite('rc440_06', 4)	# 24-27
    sprite('rc440_07', 4)	# 28-31
    sprite('rc440_05', 4)	# 32-35
    sprite('rc440_06', 4)	# 36-39
    sprite('rc440_07', 4)	# 40-43
    sprite('rc440_05', 4)	# 44-47
    sprite('rc440_06', 4)	# 48-51
    sprite('rc440_07', 4)	# 52-55
    sprite('rc440_05', 4)	# 56-59
    sprite('rc440_06', 4)	# 60-63
    sprite('rc440_04', 4)	# 64-67	 **attackbox here**
    Unknown23027()
    sprite('rc440_03', 4)	# 68-71
    sprite('rc440_02', 4)	# 72-75
    sprite('rc440_01', 4)	# 76-79
    sprite('rc440_00', 4)	# 80-83
    loopRest()

@Subroutine
def Shot_Stack():
    Unknown23029(6, 3101, 0)
    if Unknown46(5):
        Unknown38(6, 5)
    if Unknown46(4):
        Unknown38(5, 4)

@State
def ShotLandA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23012(0, 0, 0)
    sprite('rc400_00', 4)	# 1-4	 **attackbox here**
    sprite('rc400_01', 2)	# 5-6	 **attackbox here**
    sprite('rc400_02', 2)	# 7-8	 **attackbox here**
    sprite('rc400_03', 1)	# 9-9	 **attackbox here**
    Unknown7007('6272633230305f300000000000000000640000006272633230305f310000000000000000640000006272633230305f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_1('rcef_binta', 0)
    SFX_3('rcse_28')
    sprite('rc400_03ex01', 1)	# 10-10	 **attackbox here**
    sprite('rc400_04', 2)	# 11-12	 **attackbox here**
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodA', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3102, 0)
    callSubroutine('AddChainWind_Shot')
    sprite('rc400_05', 5)	# 13-17	 **attackbox here**
    sprite('rc400_06', 3)	# 18-20	 **attackbox here**
    sprite('rc400_06', 2)	# 21-22	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('rc400_07', 4)	# 23-26	 **attackbox here**
    sprite('rc400_08', 4)	# 27-30	 **attackbox here**
    sprite('rc400_09', 4)	# 31-34	 **attackbox here**
    Recovery()
    sprite('rc400_10', 4)	# 35-38
    sprite('rc400_11', 4)	# 39-42

@State
def ShotLandB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23012(0, 0, 0)
    sprite('rc401_00', 2)	# 1-2	 **attackbox here**
    sprite('rc401_01', 2)	# 3-4	 **attackbox here**
    sprite('rc401_02', 2)	# 5-6	 **attackbox here**
    sprite('rc401_03', 2)	# 7-8	 **attackbox here**
    sprite('rc401_04', 2)	# 9-10	 **attackbox here**
    sprite('rc401_05', 2)	# 11-12	 **attackbox here**
    sprite('rc401_06', 2)	# 13-14	 **attackbox here**
    sprite('rc401_07', 2)	# 15-16	 **attackbox here**
    sprite('rc401_08', 5)	# 17-21	 **attackbox here**
    Unknown7007('6272633230315f300000000000000000640000006272633230315f310000000000000000640000006272633230315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('rcse_25')
    GFX_1('rcef401_bom', 0)
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodB', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3103, 0)
    callSubroutine('AddChainWind_Shot')
    sprite('rc401_09', 5)	# 22-26	 **attackbox here**
    sprite('rc401_10', 3)	# 27-29	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('rc401_11', 3)	# 30-32	 **attackbox here**
    sprite('rc401_12', 2)	# 33-34	 **attackbox here**
    sprite('rc401_13', 2)	# 35-36	 **attackbox here**
    sprite('rc401_14', 2)	# 37-38	 **attackbox here**
    Recovery()
    sprite('rc401_15', 2)	# 39-40	 **attackbox here**
    sprite('rc401_16', 2)	# 41-42
    sprite('rc401_17', 2)	# 43-44

@State
def ShotLandC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23012(0, 0, 0)
    sprite('rc401_00', 3)	# 1-3	 **attackbox here**
    sprite('rc401_01', 3)	# 4-6	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('rc401_02', 3)	# 7-9	 **attackbox here**
    sprite('rc401_03', 2)	# 10-11	 **attackbox here**
    sprite('rc401_04', 2)	# 12-13	 **attackbox here**
    sprite('rc401_05', 2)	# 14-15	 **attackbox here**
    sprite('rc401_06', 2)	# 16-17	 **attackbox here**
    sprite('rc401_07', 2)	# 18-19	 **attackbox here**
    sprite('rc401_08', 5)	# 20-24	 **attackbox here**
    Unknown7007('6272633230315f300000000000000000640000006272633230315f310000000000000000640000006272633230315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('rcse_25')
    GFX_1('rcef401_bom', 0)
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodC', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3104, 0)
    callSubroutine('AddChainWind_Shot')
    sprite('rc401_08', 5)	# 25-29	 **attackbox here**
    SFX_3('rcse_25')
    GFX_1('rcef401_bom', 0)
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodC', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3103, 0)
    sprite('rc401_08', 5)	# 30-34	 **attackbox here**
    SFX_3('rcse_25')
    GFX_1('rcef401_bom', 0)
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodC', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3102, 0)
    sprite('rc401_09', 5)	# 35-39	 **attackbox here**
    sprite('rc401_10', 3)	# 40-42	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('rc401_11', 3)	# 43-45	 **attackbox here**
    sprite('rc401_12', 2)	# 46-47	 **attackbox here**
    sprite('rc401_13', 2)	# 48-49	 **attackbox here**
    sprite('rc401_14', 2)	# 50-51	 **attackbox here**
    Recovery()
    sprite('rc401_15', 2)	# 52-53	 **attackbox here**
    sprite('rc401_16', 2)	# 54-55
    sprite('rc401_17', 2)	# 56-57

@State
def ShotAirA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        Unknown22004(10, 1)
        Unknown23012(0, 0, 0)
    sprite('rc402_00', 4)	# 1-4
    sprite('rc402_01', 4)	# 5-8
    sprite('rc402_02', 4)	# 9-12
    SFX_3('rcse_05')
    SFX_0('004_swing_grap_1_1')
    Unknown7007('6272633230325f300000000000000000640000006272633230325f310000000000000000640000006272633230325f320000000000000000640000000000000000000000000000000000000000000000')
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodA_Air', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3105, 0)
    callSubroutine('AddChainWind_Shot')
    sprite('rc402_03', 5)	# 13-17
    sprite('rc402_04', 1)	# 18-18
    sprite('rc402_04', 4)	# 19-22
    WhiffCancelEnable(0)
    sprite('rc402_05', 4)	# 23-26
    setGravity(1850)
    Unknown23001(100, 100)
    Unknown23012(100, 100, 100)
    sprite('rc402_06', 4)	# 27-30
    sprite('rc402_07', 2)	# 31-32
    sprite('rc402_08', 5)	# 33-37
    sprite('rc402_09', 6)	# 38-43
    Recovery()
    sprite('rc402_10', 6)	# 44-49
    sprite('rc020_03', 4)	# 50-53

@State
def ShotAirB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        Unknown22004(10, 1)
        Unknown23012(0, 0, 0)
    sprite('rc403_00', 3)	# 1-3	 **attackbox here**
    sprite('rc403_01', 3)	# 4-6	 **attackbox here**
    sprite('rc403_02', 3)	# 7-9	 **attackbox here**
    sprite('rc403_03', 3)	# 10-12	 **attackbox here**
    sprite('rc403_04', 3)	# 13-15	 **attackbox here**
    sprite('rc403_05', 2)	# 16-17	 **attackbox here**
    sprite('rc403_06', 2)	# 18-19	 **attackbox here**
    sprite('rc403_07', 2)	# 20-21	 **attackbox here**
    GFX_1('rcef_binta', 0)
    Unknown7007('6272633230335f300000000000000000640000006272633230335f310000000000000000640000006272633230335f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('rcse_28')
    sprite('rc403_08', 7)	# 22-28	 **attackbox here**
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodB_Air', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3107, 0)
    callSubroutine('AddChainWind_Shot')
    sprite('rc403_09', 3)	# 29-31	 **attackbox here**
    setGravity(1850)
    Unknown23001(100, 100)
    Unknown23012(100, 100, 100)
    sprite('rc403_10', 3)	# 32-34	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('rc403_11', 3)	# 35-37	 **attackbox here**
    Recovery()
    sprite('rc403_12', 3)	# 38-40	 **attackbox here**
    sprite('rc403_13', 3)	# 41-43
    sprite('rc020_03', 4)	# 44-47
    sprite('rc020_04', 4)	# 48-51
    sprite('rc020_05', 4)	# 52-55

@State
def ShotAirC():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        Unknown22004(10, 1)
        Unknown23012(0, 0, 0)
    sprite('rc403_00', 3)	# 1-3	 **attackbox here**
    sprite('rc403_01', 3)	# 4-6	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('rc403_02', 3)	# 7-9	 **attackbox here**
    sprite('rc403_03', 3)	# 10-12	 **attackbox here**
    sprite('rc403_04', 3)	# 13-15	 **attackbox here**
    sprite('rc403_05', 2)	# 16-17	 **attackbox here**
    sprite('rc403_06', 2)	# 18-19	 **attackbox here**
    sprite('rc403_07', 2)	# 20-21	 **attackbox here**
    GFX_1('rcef_binta', 0)
    Unknown7007('6272633230335f300000000000000000640000006272633230335f310000000000000000640000006272633230335f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('rcse_28')
    sprite('rc403_08', 2)	# 22-23	 **attackbox here**
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodC_Air', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3107, 0)
    callSubroutine('AddChainWind_Shot')
    sprite('rc403_08', 2)	# 24-25	 **attackbox here**
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodC_Air', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3106, 0)
    sprite('rc403_08', 3)	# 26-28	 **attackbox here**
    callSubroutine('Shot_Stack')
    GFX_0('LightningRodC_Air', 0)
    Unknown38(4, 1)
    Unknown23029(4, 3105, 0)
    sprite('rc403_09', 3)	# 29-31	 **attackbox here**
    setGravity(1850)
    Unknown23001(100, 100)
    Unknown23012(100, 100, 100)
    sprite('rc403_10', 3)	# 32-34	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('rc403_11', 3)	# 35-37	 **attackbox here**
    Recovery()
    sprite('rc403_12', 3)	# 38-40	 **attackbox here**
    sprite('rc403_13', 3)	# 41-43
    sprite('rc020_03', 4)	# 44-47
    sprite('rc020_04', 4)	# 48-51
    sprite('rc020_05', 4)	# 52-55

@State
def ShotFlogLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2003(1)
    sprite('rc404_00', 3)	# 1-3
    sprite('rc404_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    callSubroutine('AddChainWind')
    sprite('rc404_02', 3)	# 7-9
    sprite('rc404_03', 3)	# 10-12	 **attackbox here**
    GFX_0('rcef_404flog', 0)
    SFX_0('022_magiccircle_b')
    sprite('rc404_04', 3)	# 13-15
    sprite('rc404_05', 3)	# 16-18
    sprite('rc404_06', 3)	# 19-21	 **attackbox here**
    sprite('rc404_07', 3)	# 22-24	 **attackbox here**
    sprite('rc404_08', 2)	# 25-26	 **attackbox here**
    WhiffCancelEnable(0)
    SFX_0('004_swing_grap_1_1')
    Unknown7007('6272633230345f300000000000000000640000006272633230345f310000000000000000640000006272633230345f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Flog', 0)
    Unknown38(8, 1)
    Unknown23029(8, 3302, 0)
    sprite('rc404_09', 2)	# 27-28	 **attackbox here**
    sprite('rc404_10', 2)	# 29-30	 **attackbox here**
    sprite('rc404_11', 2)	# 31-32	 **attackbox here**
    sprite('rc404_12', 2)	# 33-34	 **attackbox here**
    sprite('rc404_13', 2)	# 35-36	 **attackbox here**
    sprite('rc404_14', 2)	# 37-38
    sprite('rc404_15', 2)	# 39-40
    sprite('rc404_16', 2)	# 41-42
    sprite('rc404_17', 2)	# 43-44

@State
def ShotFlogAir():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown1017()
        Unknown1022()
        Unknown1037()
        Unknown1084(1)
        Unknown2003(1)
        Unknown23001(100, 100)
        Unknown23012(0, 0, 0)

        def upon_3():
            if (not SLOT_51):
                if (SLOT_23 < 60000):
                    Unknown1007(5000)
    sprite('rc405_00', 2)	# 1-2
    sprite('rc405_01', 1)	# 3-3
    sprite('rc405_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    callSubroutine('AddChainWind')
    sprite('rc405_02', 2)	# 5-6
    sprite('rc405_03', 2)	# 7-8
    GFX_0('rcef_404flog', 0)
    SFX_0('022_magiccircle_b')
    sprite('rc405_04', 3)	# 9-11	 **attackbox here**
    sprite('rc405_05', 3)	# 12-14
    sprite('rc405_06', 3)	# 15-17
    sprite('rc405_07', 3)	# 18-20
    sprite('rc405_08', 3)	# 21-23	 **attackbox here**
    Unknown23012(100, 100, 0)
    SLOT_51 = 1
    sprite('rc405_09', 3)	# 24-26	 **attackbox here**
    WhiffCancelEnable(0)
    SFX_0('004_swing_grap_1_1')
    Unknown7007('6272633230355f300000000000000000640000006272633230355f310000000000000000640000006272633230355f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('Flog', 0)
    Unknown38(8, 1)
    Unknown23029(8, 3303, 0)
    sprite('rc405_10', 3)	# 27-29	 **attackbox here**
    sprite('rc405_11', 3)	# 30-32	 **attackbox here**
    sprite('rc405_12', 3)	# 33-35
    sprite('rc405_13', 3)	# 36-38
    sprite('rc405_14', 3)	# 39-41
    Unknown1043()
    sprite('rc405_15', 3)	# 42-44

@State
def LightningMini():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown11063(1)
    sprite('rc216_00', 2)	# 1-2
    sprite('rc216_01', 2)	# 3-4
    sprite('rc216_02', 2)	# 5-6
    Unknown7007('6272633230385f300000000000000000640000006272633230385f310000000000000000640000006272633230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rc216_03', 2)	# 7-8
    sprite('rc216_04', 2)	# 9-10
    sprite('rc216_05', 2)	# 11-12
    Unknown23029(4, 3001, 0)
    Unknown23029(5, 3001, 0)
    Unknown23029(6, 3001, 0)
    Unknown23012(0, 0, 0)
    sprite('rc216_06', 4)	# 13-16
    SFX_0('003_swing_grap_0_2')
    sprite('rc216_07', 4)	# 17-20
    sprite('rc216_08', 4)	# 21-24
    sprite('rc216_09', 4)	# 25-28
    sprite('rc216_10', 4)	# 29-32
    sprite('rc216_11', 4)	# 33-36
    sprite('rc216_12', 4)	# 37-40

@State
def LightningMiniAir():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)
        Unknown11063(1)
        Unknown22004(4, 1)
        Unknown23012(100, 100, 100)
    sprite('rc410_00', 3)	# 1-3
    Unknown1017()
    Unknown1084(1)
    sprite('rc410_01', 3)	# 4-6
    Unknown7007('6272633230395f300000000000000000640000006272633230395f310000000000000000640000006272633230395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rc410_02', 3)	# 7-9
    sprite('rc410_03', 3)	# 10-12
    sprite('rc410_04', 3)	# 13-15
    Unknown1018()
    Unknown1019(70)
    Unknown1043()
    sprite('rc410_05', 5)	# 16-20
    Unknown23029(4, 3001, 0)
    Unknown23029(5, 3001, 0)
    Unknown23029(6, 3001, 0)
    SFX_0('003_swing_grap_0_2')
    sprite('rc410_06', 5)	# 21-25
    sprite('rc410_07', 5)	# 26-30
    sprite('rc410_08', 5)	# 31-35
    sprite('rc410_09', 5)	# 36-40
    sprite('rc410_10', 5)	# 41-45

@State
def CallWindSuctionGhostLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown11063(1)
        Unknown23012(50, 100, 20)
    sprite('rc411_00', 4)	# 1-4
    sprite('rc411_01', 4)	# 5-8
    Unknown7007('6272633231315f300000000000000000640000006272633231315f310000000000000000640000006272633231315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rc411_02', 4)	# 9-12
    sprite('rc411_03', 4)	# 13-16
    Unknown23029(4, 2006, 1)
    Unknown23029(5, 2006, 1)
    Unknown23029(6, 2006, 1)
    sprite('rc411_04', 4)	# 17-20
    sprite('rc411_05', 4)	# 21-24
    sprite('rc411_02', 4)	# 25-28
    sprite('rc411_06', 4)	# 29-32
    sprite('rc411_07', 4)	# 33-36

@State
def CallWindSuctionGhostAir():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)
        Unknown11063(1)
        setGravity(1000)
        if (SLOT_13 < 0):
            physicsYImpulse(0)
        Unknown1019(30)
        clearUponHandler(2)
        sendToLabelUpon(2, 2)

        def upon_3():
            Unknown1021(800)
            YAccel(96)
            if (SLOT_23 > 900000):
                Unknown1021(-300)
            if (SLOT_23 > 1300000):
                Unknown1021(-400)
            if (SLOT_23 > 1600000):
                Unknown1021(-500)
        Unknown23001(100, 100)
        Unknown23012(100, 150, 100)
    sprite('rc412_00', 3)	# 1-3
    sprite('rc412_01', 3)	# 4-6
    Unknown7007('6272633231315f300000000000000000640000006272633231315f310000000000000000640000006272633231315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('rc412_02', 4)	# 7-10
    sprite('rc412_03', 4)	# 11-14
    Unknown23029(4, 2006, 1)
    Unknown23029(5, 2006, 1)
    Unknown23029(6, 2006, 1)
    sprite('rc412_04', 4)	# 15-18
    sprite('rc412_05', 4)	# 19-22
    sprite('rc412_02', 4)	# 23-26
    sprite('rc412_03', 4)	# 27-30
    sprite('rc412_06', 3)	# 31-33
    sprite('rc412_07', 3)	# 34-36
    ExitState()
    label(2)
    sprite('rc252_16', 3)	# 37-39
    Unknown1084(1)
    clearUponHandler(3)
    Unknown8000(100, 1, 1)
    sprite('rc252_17', 3)	# 40-42
    sprite('rc252_18', 3)	# 43-45
    sprite('rc252_19', 3)	# 46-48

@State
def LightningLandB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown23029(4, 3002, 0)
            if (SLOT_48 == 5003):
                Unknown23029(5, 3002, 0)
            if (SLOT_48 == 5004):
                Unknown23029(6, 3002, 0)
        sendToLabelUpon(2, 2)
    sprite('rc430_00', 4)	# 1-4
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(1)
    sprite('rc430_00add', 4)	# 5-8
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    Unknown7007('6272633235305f300000000000000000640000006272633235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rc430_01', 1)	# 9-9
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_01', 3)	# 10-12
    Unknown2036(33, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    sprite('rc430_02', 4)	# 13-16
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    physicsYImpulse(1600)
    setGravity(0)
    sprite('rc430_03', 4)	# 17-20
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_04', 4)	# 21-24
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_05', 4)	# 25-28
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_06', 4)	# 29-32
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_07', 4)	# 33-36
    physicsYImpulse(0)
    sprite('rc430_08', 4)	# 37-40
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_09', 4)	# 41-44
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtk', 104)
    sprite('rc430_10', 4)	# 45-48
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtkSub_Matome', 100)
    sprite('rc430_11', 4)	# 49-52
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_12', 4)	# 53-56
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(0)
    loopRest()
    sprite('rc430_13', 4)	# 57-60
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 61-64
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 65-68
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 69-72
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 73-76
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 77-80
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 81-84
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 85-88
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    sprite('rc430_13', 4)	# 89-92
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 93-96
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 97-100
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 101-104
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 105-108
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 109-112
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 113-116
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 117-120
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    setGravity(1000)
    label(0)
    sprite('rc430_13', 4)	# 121-124
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 125-128
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 129-132
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 133-136
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('rc430_17', 2)	# 137-138
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_18', 4)	# 139-142
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_19', 4)	# 143-146
    SFX_FOOTSTEP_(100, 1, 1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_20', 4)	# 147-150
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')

@State
def LightningAirB():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        clearUponHandler(2)
        sendToLabelUpon(2, 2)
        Unknown1084(1)

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown23029(4, 3002, 0)
            if (SLOT_48 == 5003):
                Unknown23029(5, 3002, 0)
            if (SLOT_48 == 5004):
                Unknown23029(6, 3002, 0)
    sprite('rc431_00', 3)	# 1-3
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(1)
    sprite('rc431_01', 3)	# 4-6
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    Unknown7007('6272633235315f300000000000000000640000006272633235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rc431_01add', 3)	# 7-9
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc431_02', 3)	# 10-12
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_02', 4)	# 13-16
    Unknown2036(30, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    physicsYImpulse(1600)
    setGravity(0)
    sprite('rc430_03', 3)	# 17-19
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_04', 3)	# 20-22
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_05', 4)	# 23-26
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_06', 4)	# 27-30
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_07', 4)	# 31-34
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    physicsYImpulse(0)
    sprite('rc430_08', 4)	# 35-38
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_09', 4)	# 39-42
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtk', 104)
    sprite('rc430_10', 4)	# 43-46
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtkSub_Matome', 100)
    sprite('rc430_11', 4)	# 47-50
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_12', 4)	# 51-54
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(0)
    loopRest()
    sprite('rc430_13', 4)	# 55-58
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 59-62
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 63-66
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 67-70
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 71-74
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 75-78
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 79-82
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 83-86
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    sprite('rc430_13', 4)	# 87-90
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 91-94
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 95-98
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 99-102
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 103-106
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 107-110
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 111-114
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 115-118
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    setGravity(1000)
    sprite('rc430_16', 6)	# 119-124
    sprite('rc430_17', 6)	# 125-130
    sprite('rc430_18', 7)	# 131-137
    label(992)
    sprite('rc430_19', 3)	# 138-140
    loopRest()
    gotoLabel(992)
    label(2)
    sprite('rc430_20', 8)	# 141-148
    Unknown8000(100, 1, 1)

@State
def LightningLandB_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown23029(4, 3003, 0)
            if (SLOT_48 == 5003):
                Unknown23029(5, 3003, 0)
            if (SLOT_48 == 5004):
                Unknown23029(6, 3003, 0)
        sendToLabelUpon(2, 2)
    sprite('rc430_00', 4)	# 1-4
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(1)
    sprite('rc430_00add', 4)	# 5-8
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    Unknown7007('6272633235305f300000000000000000640000006272633235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rc430_01', 1)	# 9-9
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_01', 3)	# 10-12
    Unknown2036(33, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    sprite('rc430_02', 4)	# 13-16
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    physicsYImpulse(1600)
    setGravity(0)
    sprite('rc430_03', 4)	# 17-20
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_04', 4)	# 21-24
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_05', 4)	# 25-28
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_06', 4)	# 29-32
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_07', 4)	# 33-36
    physicsYImpulse(0)
    sprite('rc430_08', 4)	# 37-40
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_09', 4)	# 41-44
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtk_Matome', 104)
    sprite('rc430_10', 4)	# 45-48
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtkSubOD_Matome', 100)
    sprite('rc430_11', 4)	# 49-52
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_12', 4)	# 53-56
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(0)
    loopRest()
    sprite('rc430_13', 4)	# 57-60
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 61-64
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 65-68
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 69-72
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 73-76
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 77-80
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 81-84
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 85-88
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    sprite('rc430_13', 4)	# 89-92
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 93-96
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 97-100
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 101-104
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 105-108
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 109-112
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 113-116
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 117-120
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    setGravity(1000)
    label(0)
    sprite('rc430_13', 4)	# 121-124
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 125-128
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 129-132
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 133-136
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('rc430_17', 2)	# 137-138
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_18', 4)	# 139-142
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_19', 4)	# 143-146
    SFX_FOOTSTEP_(100, 1, 1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_20', 4)	# 147-150
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')

@State
def LightningAirB_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        clearUponHandler(2)
        sendToLabelUpon(2, 2)
        Unknown1084(1)

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown23029(4, 3003, 0)
            if (SLOT_48 == 5003):
                Unknown23029(5, 3003, 0)
            if (SLOT_48 == 5004):
                Unknown23029(6, 3003, 0)
    sprite('rc431_00', 3)	# 1-3
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(1)
    sprite('rc431_01', 3)	# 4-6
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    Unknown7007('6272633235315f300000000000000000640000006272633235315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rc431_01add', 3)	# 7-9
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc431_02', 3)	# 10-12
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_02', 4)	# 13-16
    Unknown2036(30, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    physicsYImpulse(1600)
    setGravity(0)
    sprite('rc430_03', 3)	# 17-19
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_04', 3)	# 20-22
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_05', 4)	# 23-26
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_06', 4)	# 27-30
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_07', 4)	# 31-34
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    physicsYImpulse(0)
    sprite('rc430_08', 4)	# 35-38
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    sprite('rc430_09', 4)	# 39-42
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtk_Matome', 104)
    sprite('rc430_10', 4)	# 43-46
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    GFX_0('LightningObjAtkSubOD_Matome', 100)
    sprite('rc430_11', 4)	# 47-50
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_12', 4)	# 51-54
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('014_electric_m')
    setInvincible(0)
    loopRest()
    sprite('rc430_13', 4)	# 55-58
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 59-62
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 63-66
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 67-70
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_13', 4)	# 71-74
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_14', 4)	# 75-78
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_15', 4)	# 79-82
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    sprite('rc430_16', 4)	# 83-86
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_m')
    loopRest()
    setGravity(1000)
    sprite('rc430_16', 6)	# 87-92
    sprite('rc430_17', 6)	# 93-98
    sprite('rc430_18', 7)	# 99-105
    label(992)
    sprite('rc430_19', 3)	# 106-108
    loopRest()
    gotoLabel(992)
    label(2)
    sprite('rc430_20', 8)	# 109-116
    Unknown8000(100, 1, 1)

@State
def UltimateStorm():

    def upon_IMMEDIATE():
        if SLOT_36:
            AttackDefaults_AirDD()
            Unknown22004(8, 1)
        else:
            AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
    sprite('rc432_00', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('rc432_01', 3)	# 4-6
    sprite('rc432_02', 3)	# 7-9
    sprite('rc432_03', 5)	# 10-14
    Unknown2036(34, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('rc432_04', 5)	# 15-19
    Unknown7007('6272633235325f300000000000000000640000006272633235325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    sprite('rc432_05', 5)	# 20-24
    sprite('rc432_06', 10)	# 25-34
    Unknown23029(11, 5101, 0)
    sprite('rc432_06', 5)	# 35-39
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('rc432_07', 5)	# 40-44
    Unknown23029(11, 5102, 0)
    GFX_0('ReichelStormLv4', -1)
    GFX_0('Generator', -1)
    sprite('rc432_08', 5)	# 45-49
    SFX_3('rcse_10')
    loopRest()
    sprite('rc432_09', 4)	# 50-53
    SFX_3('rcse_23')
    sprite('rc432_10', 4)	# 54-57
    SFX_3('rcse_10')
    sprite('rc432_11', 4)	# 58-61
    SFX_3('rcse_23')
    sprite('rc432_09', 3)	# 62-64
    setInvincible(0)
    sprite('rc432_10', 3)	# 65-67
    sprite('rc432_11', 3)	# 68-70
    SFX_3('rcse_10')
    sprite('rc432_09', 2)	# 71-72
    sprite('rc432_10', 2)	# 73-74
    SFX_3('rcse_23')
    sprite('rc432_11', 2)	# 75-76
    sprite('rc432_09', 3)	# 77-79
    sprite('rc432_10', 3)	# 80-82
    SFX_3('rcse_10')
    sprite('rc432_11', 3)	# 83-85
    SFX_3('rcse_23')
    label(1)
    sprite('rc432_09', 4)	# 86-89
    Unknown21015('5265696368656c53746f726d4c76340000000000000000000000000000000000f013000000000000')
    sprite('rc432_10', 4)	# 90-93
    sprite('rc432_11', 4)	# 94-97
    sprite('rc432_12', 4)	# 98-101
    Unknown23029(11, 5103, 0)
    sprite('rc432_13', 4)	# 102-105
    sprite('rc432_14', 5)	# 106-110
    sprite('rc432_15', 5)	# 111-115

@State
def UltimateStorm_OD():

    def upon_IMMEDIATE():
        if SLOT_36:
            AttackDefaults_AirDD()
            Unknown22004(8, 1)
        else:
            AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
    sprite('rc432_00', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('rc432_01', 3)	# 4-6
    sprite('rc432_02', 3)	# 7-9
    sprite('rc432_03', 5)	# 10-14
    Unknown2036(34, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('rc432_04', 5)	# 15-19
    Unknown7007('6272633235325f300000000000000000640000006272633235325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    sprite('rc432_05', 5)	# 20-24
    sprite('rc432_06', 10)	# 25-34
    Unknown23029(11, 5101, 0)
    sprite('rc432_06', 5)	# 35-39
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('rc432_07', 5)	# 40-44
    Unknown23029(11, 5102, 0)
    GFX_0('ReichelStormLv4', -1)
    GFX_0('Generator_OD', -1)
    sprite('rc432_08', 5)	# 45-49
    SFX_3('rcse_10')
    loopRest()
    sprite('rc432_09', 4)	# 50-53
    SFX_3('rcse_23')
    sprite('rc432_10', 4)	# 54-57
    SFX_3('rcse_10')
    sprite('rc432_11', 4)	# 58-61
    SFX_3('rcse_23')
    sprite('rc432_09', 3)	# 62-64
    setInvincible(0)
    sprite('rc432_10', 3)	# 65-67
    sprite('rc432_11', 3)	# 68-70
    SFX_3('rcse_10')
    sprite('rc432_09', 2)	# 71-72
    sprite('rc432_10', 2)	# 73-74
    SFX_3('rcse_23')
    sprite('rc432_11', 2)	# 75-76
    sprite('rc432_09', 3)	# 77-79
    sprite('rc432_10', 3)	# 80-82
    SFX_3('rcse_10')
    sprite('rc432_11', 3)	# 83-85
    SFX_3('rcse_23')
    label(1)
    sprite('rc432_09', 4)	# 86-89
    Unknown21015('5265696368656c53746f726d4c76340000000000000000000000000000000000f013000000000000')
    sprite('rc432_10', 4)	# 90-93
    sprite('rc432_11', 4)	# 94-97
    sprite('rc432_12', 4)	# 98-101
    Unknown23029(11, 5103, 0)
    sprite('rc432_13', 4)	# 102-105
    sprite('rc432_14', 5)	# 106-110
    sprite('rc432_15', 5)	# 111-115

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        sendToLabelUpon(12, 1)
        Unknown23012(0, 0, 0)
        AttackLevel_(5)
        Hitstop(0)
        AirPushbackX(-200)
        AirPushbackY(6000)
        YImpluseBeforeWallbounce(5)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(5000)
        Unknown11069('AstralHeat')
        HitAirUnblockable(0)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11034(0)
        Unknown11033(2)
        setInvincible(1)
        GuardPoint_(1)
        Unknown23027()
    sprite('rc450_00', 5)	# 1-5
    sprite('rc450_01', 5)	# 6-10
    Unknown2036(120, -1, 2)
    Unknown23147()
    Unknown4004('617572610000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('EMB_RC_AH', 0)
    SFX_1('brc290')
    SFX_0('022_magiccircle_b')
    sprite('rc450_02', 5)	# 11-15
    sprite('rc450_03', 5)	# 16-20
    sprite('rc450_04', 5)	# 21-25
    sprite('rc450_05', 5)	# 26-30
    sprite('rc450_06', 5)	# 31-35
    sprite('rc450_07', 5)	# 36-40
    sprite('rc450_08', 5)	# 41-45
    sprite('rc450_09', 5)	# 46-50
    sprite('rc450_10', 45)	# 51-95	 **attackbox here**
    GFX_0('ModelMagicCircleAST', 0)
    GFX_1('rcef_ASTstart', 0)
    sprite('rc450_10', 40)	# 96-135	 **attackbox here**
    GFX_0('light', 0)
    Unknown36(1)
    teleportRelativeX(1200)
    Unknown35()
    sprite('rc450_10', 40)	# 136-175	 **attackbox here**
    RefreshMultihit()
    Damage(0)
    Unknown11091(100)
    sprite('rc450_11', 5)	# 176-180
    setInvincible(0)
    sprite('rc450_38', 5)	# 181-185
    sprite('rc450_39', 5)	# 186-190
    sprite('rc450_40', 5)	# 191-195
    sprite('rc450_41', 5)	# 196-200
    loopRest()
    ExitState()
    label(1)
    clearUponHandler(12)
    sprite('rc450_10', 40)	# 201-240	 **attackbox here**
    Unknown23088(1, 1)
    Unknown23157(1)
    Unknown2017(0)
    GuardPoint_(0)
    Unknown23084(1)
    Unknown20000(1)
    Unknown20003(1)
    Unknown20006(1)
    sprite('rc450_11', 4)	# 241-244
    Unknown23024(3)
    Unknown23025(1)
    sprite('rc450_12', 4)	# 245-248
    GFX_0('BatDelete', 0)
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    Unknown2037(0)
    physicsXImpulse(0)
    sprite('rc450_13', 4)	# 249-252
    sprite('rc450_14', 4)	# 253-256
    sprite('rc450_15', 4)	# 257-260
    sprite('rc450_16', 4)	# 261-264
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    SFX_0('024_getset_b')
    sprite('rc450_17', 4)	# 265-268
    sprite('rc450_18', 4)	# 269-272
    ScreenShake(0, 5000)
    sprite('rc450_19', 4)	# 273-276
    sprite('rc450_20', 4)	# 277-280
    sprite('rc450_21', 4)	# 281-284
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('00000000ff0000000000000000000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3076(1000)
    Unknown3077(1025)
    setGravity(-6)
    physicsYImpulse(3500)
    ScreenShake(0, 10000)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 285-288
    sprite('rc450_23', 4)	# 289-292	 **attackbox here**
    ScreenShake(0, 10000)
    sprite('rc450_24', 4)	# 293-296
    sprite('rc450_25', 4)	# 297-300
    sprite('rc450_21', 4)	# 301-304
    physicsYImpulse(3000)
    ScreenShake(0, 10000)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 305-308
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    SFX_0('019_quake_0')
    sprite('rc450_23', 4)	# 309-312	 **attackbox here**
    ScreenShake(0, 10000)
    sprite('rc450_24', 4)	# 313-316
    sprite('rc450_25', 4)	# 317-320
    sprite('rc450_21', 4)	# 321-324
    physicsYImpulse(2500)
    SFX_0('015_blaze_2')
    ScreenShake(0, 10000)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 325-328
    SFX_0('019_quake_0')
    sprite('rc450_23', 4)	# 329-332	 **attackbox here**
    ScreenShake(0, 10000)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_24', 4)	# 333-336
    sprite('rc450_25', 4)	# 337-340
    sprite('rc450_21', 4)	# 341-344
    physicsYImpulse(2000)
    ScreenShake(0, 10000)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 345-348
    SFX_0('019_quake_0')
    sprite('rc450_23', 4)	# 349-352	 **attackbox here**
    ScreenShake(0, 10000)
    sprite('rc450_24', 4)	# 353-356
    sprite('rc450_25', 4)	# 357-360
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 361-364
    physicsYImpulse(1500)
    ScreenShake(0, 10000)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 365-368
    SFX_0('019_quake_0')
    sprite('rc450_23', 4)	# 369-372	 **attackbox here**
    ScreenShake(0, 10000)
    sprite('rc450_24', 4)	# 373-376
    sprite('rc450_25', 4)	# 377-380
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 381-384
    Unknown3076(1000)
    Unknown3077(1050)
    setGravity(-3)
    physicsYImpulse(1000)
    ScreenShake(0, 10000)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 385-388
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_23', 4)	# 389-392	 **attackbox here**
    ScreenShake(0, 10000)
    sprite('rc450_24', 4)	# 393-396
    sprite('rc450_25', 4)	# 397-400
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 401-404
    physicsYImpulse(750)
    ScreenShake(0, 10000)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 405-408
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_23', 4)	# 409-412	 **attackbox here**
    ScreenShake(0, 7500)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_24', 4)	# 413-416
    sprite('rc450_25', 4)	# 417-420
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 421-424
    physicsYImpulse(500)
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 425-428
    SFX_0('019_quake_0')
    sprite('rc450_23', 4)	# 429-432	 **attackbox here**
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_24', 4)	# 433-436
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_25', 4)	# 437-440
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 441-444
    Unknown3076(1000)
    Unknown3077(1075)
    physicsYImpulse(250)
    ScreenShake(0, 1000)
    SFX_0('019_quake_1')
    SFX_0('015_blaze_2')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 445-448
    SFX_0('019_quake_1')
    SFX_0('015_blaze_2')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_23', 4)	# 449-452	 **attackbox here**
    SFX_0('019_quake_1')
    SFX_0('015_blaze_2')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_24', 4)	# 453-456
    SFX_0('019_quake_1')
    SFX_0('015_blaze_2')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_25', 4)	# 457-460
    SFX_0('019_quake_1')
    SFX_0('015_blaze_2')
    SFX_0('013_thunder_0')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 461-464
    Unknown3076(1000)
    Unknown3077(1100)
    setGravity(-1)
    physicsYImpulse(0)
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 465-468
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_23', 4)	# 469-472	 **attackbox here**
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_24', 4)	# 473-476
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_25', 4)	# 477-480
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 481-484
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 485-488
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_23', 4)	# 489-492	 **attackbox here**
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_24', 4)	# 493-496
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_25', 4)	# 497-500
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_21', 4)	# 501-504
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_22', 4)	# 505-508
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_23', 4)	# 509-512	 **attackbox here**
    SFX_0('019_quake_1')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_24', 4)	# 513-516
    SFX_0('019_quake_0')
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_25', 4)	# 517-520
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_26', 2)	# 521-522
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    GFX_0('LightningObjAST', 104)
    sprite('rc450_27', 2)	# 523-524
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_28', 4)	# 525-528
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    SFX_0('014_electric_ml')
    sprite('rc450_29', 4)	# 529-532	 **attackbox here**
    RefreshMultihit()
    Damage(47880)
    Unknown11064(3)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Hitstop(0)
    AirPushbackX(0)
    AirPushbackY(5000)
    YImpluseBeforeWallbounce(1000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirUntechableTime(1000)
    Unknown11023(1)
    Unknown11071(1)
    clearUponHandler(2)
    sendToLabelUpon(2, 100)
    Unknown3029(0)
    GFX_0('AstralFinishRose', -1)
    sprite('rc450_30', 4)	# 533-536
    sprite('rc450_31', 4)	# 537-540
    sprite('rc450_30', 4)	# 541-544
    sprite('rc450_29', 4)	# 545-548	 **attackbox here**
    sprite('rc450_28', 4)	# 549-552
    sprite('rc450_29', 4)	# 553-556	 **attackbox here**
    sprite('rc450_30', 4)	# 557-560
    sprite('rc450_31', 4)	# 561-564
    setGravity(5)
    physicsYImpulse(-500)
    sprite('rc450_27', 4)	# 565-568
    physicsYImpulse(-800)
    setGravity(200)
    GFX_0('AstralNago', -1)
    sprite('rc450_26', 4)	# 569-572
    label(99)
    sprite('rc450_21', 4)	# 573-576
    sprite('rc450_22', 4)	# 577-580
    sprite('rc450_23', 4)	# 581-584	 **attackbox here**
    sprite('rc450_24', 4)	# 585-588
    sprite('rc450_25', 4)	# 589-592
    loopRest()
    gotoLabel(99)
    label(100)
    sprite('rc450_33', 5)	# 593-597
    SFX_0('019_quake_0')
    Unknown1084(1)
    clearUponHandler(3)
    Unknown8000(100, 1, 1)
    sprite('rc450_34', 5)	# 598-602
    GFX_0('BatSummons', 0)
    SFX_0('019_quake_0')
    sprite('rc450_35', 5)	# 603-607
    SFX_0('019_quake_0')
    sprite('rc450_36', 5)	# 608-612
    SFX_0('019_quake_0')
    sprite('rc000_00', 7)	# 613-619
    SFX_0('019_quake_0')
    sprite('rc000_01', 7)	# 620-626
    SFX_0('019_quake_0')
    sprite('rc000_02', 7)	# 627-633
    SFX_0('019_quake_0')
    sprite('rc000_03', 7)	# 634-640
    SFX_0('019_quake_0')
    sprite('rc000_04', 7)	# 641-647
    SFX_0('019_quake_0')
    sprite('rc000_05', 7)	# 648-654
    SFX_0('019_quake_0')
    sprite('rc000_06', 7)	# 655-661
    SFX_0('019_quake_0')
    sprite('rc000_07', 7)	# 662-668
    SFX_0('019_quake_0')
    sprite('rc000_08', 7)	# 669-675
    SFX_0('019_quake_0')

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('rc413_00', 2)	# 1-2	 **attackbox here**
    sprite('rc413_01', 1)	# 3-3	 **attackbox here**
    sprite('rc413_01', 1)	# 4-4	 **attackbox here**
    tag_voice(1, 'brc156_0', 'brc156_1', '', '')
    sprite('rc413_02', 2)	# 5-6	 **attackbox here**
    sprite('rc413_03', 2)	# 7-8	 **attackbox here**
    sprite('rc413_04', 2)	# 9-10	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('rc413_05', 3)	# 11-13	 **attackbox here**
    sprite('rc413_06', 6)	# 14-19	 **attackbox here**
    sprite('rc413_07', 2)	# 20-21	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    sprite('rc413_08', 3)	# 22-24	 **attackbox here**
    sprite('rc413_09', 3)	# 25-27	 **attackbox here**
    sprite('rc413_10', 3)	# 28-30	 **attackbox here**
    sprite('rc413_11', 3)	# 31-33	 **attackbox here**
    sprite('rc413_12', 3)	# 34-36	 **attackbox here**
    sprite('rc413_13', 3)	# 37-39	 **attackbox here**
    sprite('rc413_14', 3)	# 40-42	 **attackbox here**
    sprite('rc413_15', 2)	# 43-44	 **attackbox here**
    sprite('rc413_16', 2)	# 45-46	 **attackbox here**
    sprite('rc413_17', 2)	# 47-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)
        Unknown23012(0, 0, 0)
    sprite('rc413_09', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown3029(0)
    sprite('rc413_10', 2)	# 4-5	 **attackbox here**
    sprite('rc413_11', 2)	# 6-7	 **attackbox here**
    sprite('rc413_12', 2)	# 8-9	 **attackbox here**
    sprite('rc413_13', 2)	# 10-11	 **attackbox here**
    sprite('rc413_14', 2)	# 12-13	 **attackbox here**
    sprite('rc413_15', 2)	# 14-15	 **attackbox here**
    sprite('rc413_16', 2)	# 16-17	 **attackbox here**
    sprite('rc413_17', 2)	# 18-19
    sprite('rc211_00', 1)	# 20-20
    sprite('rc211_01', 2)	# 21-22
    sprite('rc211_02', 2)	# 23-24
    sprite('rc211_03', 2)	# 25-26
    sprite('rc211_04', 1)	# 27-27
    sprite('rc211_05', 1)	# 28-28
    sprite('rc211_06', 1)	# 29-29
    SFX_0('003_swing_grap_0_1')
    tag_voice(0, 'brc157_0', 'brc157_1', '', '')
    sprite('rc211_07', 3)	# 30-32	 **attackbox here**
    sprite('rc211_08', 3)	# 33-35
    sprite('rc211_09', 3)	# 36-38
    sprite('rc211_10', 3)	# 39-41
    sprite('rc211_11', 3)	# 42-44
    sprite('rc211_12', 3)	# 45-47
    label(10)
    sprite('rc000_00', 7)	# 48-54
    sprite('rc000_01', 7)	# 55-61
    sprite('rc000_02', 7)	# 62-68
    sprite('rc000_03', 7)	# 69-75
    sprite('rc000_04', 7)	# 76-82
    sprite('rc000_05', 7)	# 83-89
    sprite('rc000_06', 7)	# 90-96
    sprite('rc000_07', 7)	# 97-103
    sprite('rc000_08', 7)	# 104-110
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 111-111

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('rc201_00', 4)	# 1-4
    sprite('rc201_01', 4)	# 5-8
    sprite('rc201_02', 6)	# 9-14
    sprite('rc201_03', 3)	# 15-17	 **attackbox here**
    GFX_0('rc201_Wind', 0)
    GFX_0('rcef_201rose', 1)
    GFX_1('rcef_201wind', 2)
    GFX_1('rcef_201light', 3)
    sprite('rc201_04', 3)	# 18-20	 **attackbox here**
    StartMultihit()
    sprite('rc201_05', 1)	# 21-21
    Recovery()
    Unknown2063()
    sprite('rc201_06', 1)	# 22-22
    sprite('rc201_07', 1)	# 23-23
    sprite('rc201_08', 1)	# 24-24
    sprite('rc201_09', 2)	# 25-26
    sprite('rc201_10', 2)	# 27-28
    sprite('rc201_11', 2)	# 29-30
    sprite('rc201_12', 2)	# 31-32
    sprite('rc201_13', 2)	# 33-34
    sprite('rc201_14', 1)	# 35-35
    label(0)
    sprite('rc000_00', 7)	# 36-42
    sprite('rc000_01', 7)	# 43-49
    sprite('rc000_02', 7)	# 50-56
    sprite('rc000_03', 7)	# 57-63
    sprite('rc000_04', 7)	# 64-70
    sprite('rc000_05', 7)	# 71-77
    sprite('rc000_06', 7)	# 78-84
    sprite('rc000_07', 7)	# 85-91
    sprite('rc000_08', 7)	# 92-98
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 99-99

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('rc440_00', 3)	# 1-3
    sprite('rc440_01', 4)	# 4-7
    sprite('rc440_02', 4)	# 8-11
    sprite('rc440_03', 4)	# 12-15
    sprite('rc440_03', 4)	# 16-19
    tag_voice(0, 'brc158_0', 'brc158_1', '', '')
    GFX_0('BurstDD_WindEff', 0)
    sprite('rc440_04', 2)	# 20-21	 **attackbox here**
    sprite('rc440_05', 3)	# 22-24
    sprite('rc440_06', 3)	# 25-27
    sprite('rc440_07', 3)	# 28-30
    sprite('rc440_05', 3)	# 31-33
    sprite('rc440_06', 3)	# 34-36
    sprite('rc440_07', 3)	# 37-39
    sprite('rc440_05', 3)	# 40-42
    sprite('rc440_06', 3)	# 43-45
    sprite('rc440_07', 3)	# 46-48
    sprite('rc440_03', 3)	# 49-51
    sprite('rc440_02', 3)	# 52-54
    sprite('rc440_01', 3)	# 55-57
    sprite('rc440_00', 3)	# 58-60

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
    teleportRelativeX(-200000)
    Unknown1007(600000)
    setGravity(0)
    sprite('rc260_05', 3)	# 28-30	 **attackbox here**
    StartMultihit()
    SFX_0('airdash_l')
    SFX_0('slash_pole_middle')
    physicsYImpulse(-6500)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('rc260_06', 3)	# 31-33	 **attackbox here**
    StartMultihit()
    physicsYImpulse(-52000)
    sprite('rc260_07', 3)	# 34-36	 **attackbox here**
    StartMultihit()
    SFX_0('005_swing_grap_2_2')
    sprite('rc260_04', 3)	# 37-39
    StartMultihit()
    sprite('rc260_05', 2)	# 40-41	 **attackbox here**
    GFX_1('rcef_falldown', -1)
    StartMultihit()
    sprite('rc260_06', 2)	# 42-43	 **attackbox here**
    sprite('rc260_07', 2)	# 44-45	 **attackbox here**
    StartMultihit()
    GFX_1('rcef_falldown', -1)
    HitOverhead(0)
    sprite('rc260_08', 2)	# 46-47	 **attackbox here**
    StartMultihit()
    sprite('rc260_09', 2)	# 48-49	 **attackbox here**
    StartMultihit()
    label(1)
    sprite('rc260_10', 2)	# 50-51
    Unknown8004(100, 1, 1)
    Unknown1084(1)
    GFX_1('rcef_falldown_mc02', -1)
    sprite('rc260_11', 5)	# 52-56
    sprite('rc260_12', 2)	# 57-58
    sprite('rc260_13', 2)	# 59-60
    sprite('rc260_14', 2)	# 61-62
    sprite('rc260_15', 2)	# 63-64
    sprite('rc260_15ex01', 2)	# 65-66
    sprite('rc260_16', 2)	# 67-68
    sprite('rc260_17', 2)	# 69-70
    sprite('rc000_00', 7)	# 71-77
    sprite('rc000_01', 7)	# 78-84
    sprite('rc000_02', 7)	# 85-91
    sprite('rc000_03', 7)	# 92-98
    sprite('rc000_04', 7)	# 99-105
    sprite('rc000_05', 7)	# 106-112
    sprite('rc000_06', 7)	# 113-119
    sprite('rc000_07', 7)	# 120-126
    sprite('rc000_08', 7)	# 127-133
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('rc213_03', 1)	# 1-1
    sprite('rc213_04', 1)	# 2-2
    sprite('rc213_05', 1)	# 3-3
    sprite('rc213_06', 1)	# 4-4
    sprite('rc213_07', 1)	# 5-5
    sprite('rc213_08', 2)	# 6-7
    sprite('rc213_09', 2)	# 8-9
    sprite('rc213_10', 2)	# 10-11	 **attackbox here**
    StartMultihit()
    SFX_0('006_swing_blade_1')
    sprite('rc213_11', 4)	# 12-15	 **attackbox here**
    ScreenShake(0, 5000)
    sprite('rc213_12', 4)	# 16-19
    sprite('rc213_13', 4)	# 20-23
    sprite('rc213_14', 3)	# 24-26
    sprite('rc213_15', 3)	# 27-29
    sprite('rc213_16', 3)	# 30-32
    loopRest()
    sprite('rc000_00', 7)	# 33-39
    sprite('rc000_01', 7)	# 40-46
    sprite('rc000_02', 7)	# 47-53
    sprite('rc000_03', 7)	# 54-60
    sprite('rc000_04', 7)	# 61-67
    sprite('rc000_05', 7)	# 68-74
    sprite('rc000_06', 7)	# 75-81
    sprite('rc000_07', 7)	# 82-88
    sprite('rc000_08', 7)	# 89-95
    loopRest()

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('rc440_00', 3)	# 1-3
    sprite('rc440_01', 4)	# 4-7
    sprite('rc440_02', 4)	# 8-11
    sprite('rc440_03', 4)	# 12-15
    sprite('rc440_03', 4)	# 16-19
    GFX_0('BurstDD_WindEff', 0)
    sprite('rc440_04', 2)	# 20-21	 **attackbox here**
    sprite('rc440_05', 3)	# 22-24
    sprite('rc440_06', 3)	# 25-27
    sprite('rc440_07', 3)	# 28-30
    sprite('rc440_05', 3)	# 31-33
    sprite('rc440_06', 3)	# 34-36
    sprite('rc440_07', 3)	# 37-39
    sprite('rc440_05', 3)	# 40-42
    sprite('rc440_06', 3)	# 43-45
    sprite('rc440_07', 3)	# 46-48
    sprite('rc440_03', 3)	# 49-51
    sprite('rc440_02', 3)	# 52-54
    sprite('rc440_01', 3)	# 55-57
    sprite('rc440_00', 3)	# 58-60

@Subroutine
def MouthTableInit():
    Unknown18011('brc000', 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc500', 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc501', 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 12593, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc502', 14179, 12641, 25393, 12339, 14177, 14179, 14177, 13411, 24888, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 12342, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc503', 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc504', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 13875, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc505', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 14435, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 13875, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12593, 14179, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc521', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25393, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 12593, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc404_0', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc404_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc405_0', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc405_1', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc600bes', 12643, 12641, 25396, 12849, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc601bha', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc601bph', 12643, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc600brg', 12643, 12641, 25396, 12339, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc600pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc600pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc601uli', 12643, 12641, 25396, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc601umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc601uva', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc700bes', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc700bha', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc700bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc700brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc701pmi', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc700pyu', 12643, 14177, 12643, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc701rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc700uli', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc701uva', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12344, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('brc703umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    label(0)
    sprite('rc040_02', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    if SLOT_169:
        _gotolabel(482)
    if SLOT_122:
        _gotolabel(482)
    if SLOT_123:
        _gotolabel(482)
    PartnerChar('brg')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uva')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(20)
    sprite('rc600_00', 20)	# 2-21	 **attackbox here**
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    sprite('rc600_00', 40)	# 22-61	 **attackbox here**
    sprite('rc600_01', 10)	# 62-71	 **attackbox here**
    sprite('rc600_02', 10)	# 72-81	 **attackbox here**
    sprite('rc600_03', 10)	# 82-91	 **attackbox here**
    sprite('rc600_03add01', 10)	# 92-101	 **attackbox here**
    sprite('rc600_04', 8)	# 102-109	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 110-117	 **attackbox here**
    sprite('rc600_05add01', 30)	# 118-147	 **attackbox here**
    if SLOT_158:
        Unknown7006('brc501', 100, 895709794, 12848, 0, 0, 100, 895709794, 13360, 0, 0, 100, 895709794, 13616, 0, 0, 100)
    label(1)
    sprite('rc600_05add01', 1)	# 148-148	 **attackbox here**
    if SLOT_97:
        _gotolabel(1)
    sprite('rc600_06', 8)	# 149-156	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 157-164	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 165-170	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 171-176	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 177-182	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 183-188	 **attackbox here**
    Unknown21007(24, 41)
    sprite('rc600_12', 6)	# 189-194	 **attackbox here**
    sprite('rc600_13', 6)	# 195-200	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 201-206	 **attackbox here**
    sprite('rc600_15', 6)	# 207-212	 **attackbox here**
    sprite('rc600_16', 6)	# 213-218	 **attackbox here**
    sprite('rc600_17', 6)	# 219-224	 **attackbox here**
    sprite('rc600_18', 6)	# 225-230	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 231-236	 **attackbox here**
    sprite('rc600_20', 6)	# 237-242	 **attackbox here**
    sprite('rc600_21', 6)	# 243-248	 **attackbox here**
    sprite('rc600_22', 6)	# 249-254	 **attackbox here**
    sprite('rc600_23', 6)	# 255-260	 **attackbox here**
    sprite('rc600_24', 6)	# 261-266	 **attackbox here**
    sprite('rc600_25', 6)	# 267-272	 **attackbox here**
    sprite('rc600_26', 6)	# 273-278	 **attackbox here**
    loopRest()
    ExitState()
    label(10)
    sprite('rc601_00', 6)	# 279-284	 **attackbox here**
    Unknown36(24)
    teleportRelativeX(-200000)
    Unknown35()
    sprite('rc601_00add01', 6)	# 285-290	 **attackbox here**
    sprite('rc601_00add02', 6)	# 291-296	 **attackbox here**
    sprite('rc601_00add03', 6)	# 297-302	 **attackbox here**
    sprite('rc601_00add04', 6)	# 303-308	 **attackbox here**
    sprite('rc601_00add05', 6)	# 309-314	 **attackbox here**
    sprite('rc601_01', 6)	# 315-320	 **attackbox here**
    Unknown4049(1500)
    Unknown4045('726365665f62696e74610000000000000000000000000000000000000000000000000000')
    SFX_3('rcse_28')
    SFX_1('ng118')
    SFX_3('rcse_02')
    sprite('rc601_02', 6)	# 321-326	 **attackbox here**
    sprite('rc601_03', 6)	# 327-332	 **attackbox here**
    sprite('rc601_04', 6)	# 333-338	 **attackbox here**
    sprite('rc601_05', 6)	# 339-344	 **attackbox here**
    SFX_0('200_walk_normal_0')
    sprite('rc601_06', 6)	# 345-350	 **attackbox here**
    if SLOT_158:
        Unknown7006('brc500', 100, 895709794, 13104, 0, 0, 100, 895709794, 13360, 0, 0, 100, 895709794, 13616, 0, 0, 100)
    Unknown23018(1)
    sprite('rc601_07', 6)	# 351-356	 **attackbox here**
    sprite('rc601_08', 6)	# 357-362	 **attackbox here**
    SFX_0('200_walk_normal_0')
    sprite('rc601_09', 6)	# 363-368	 **attackbox here**
    sprite('rc601_10', 6)	# 369-374	 **attackbox here**
    sprite('rc601_11', 6)	# 375-380	 **attackbox here**
    SFX_0('200_walk_normal_0')
    sprite('rc601_12', 6)	# 381-386	 **attackbox here**
    SFX_3('rcse_04')
    sprite('rc601_13', 6)	# 387-392	 **attackbox here**
    sprite('rc601_14', 6)	# 393-398	 **attackbox here**
    SFX_0('200_walk_normal_0')
    sprite('rc601_15', 6)	# 399-404	 **attackbox here**
    Unknown21007(24, 41)
    sprite('rc601_16', 6)	# 405-410	 **attackbox here**
    sprite('rc601_17', 6)	# 411-416	 **attackbox here**
    sprite('rc601_18', 6)	# 417-422	 **attackbox here**
    sprite('rc601_19', 3)	# 423-425
    SFX_1('rc412')
    sprite('rc601_20', 6)	# 426-431
    sprite('rc601_21', 6)	# 432-437
    label(11)
    sprite('rc000_00', 7)	# 438-444
    sprite('rc000_01', 7)	# 445-451
    sprite('rc000_02', 7)	# 452-458
    sprite('rc000_03', 7)	# 459-465
    sprite('rc000_04', 7)	# 466-472
    sprite('rc000_05', 7)	# 473-479
    sprite('rc000_06', 7)	# 480-486
    sprite('rc000_07', 7)	# 487-493
    sprite('rc000_08', 7)	# 494-500
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('rc602_00', 6)	# 501-506
    teleportRelativeY(640000)
    Unknown3038(1)
    loopRest()
    clearUponHandler(2)
    sendToLabelUpon(2, 48)
    sprite('rc602_00', 6)	# 507-512
    Unknown3038(0)
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 513-518
    sprite('rc602_02', 6)	# 519-524
    sprite('rc602_03', 6)	# 525-530
    sprite('rc602_04', 6)	# 531-536
    sprite('rc602_00', 6)	# 537-542
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 543-548
    sprite('rc602_02', 6)	# 549-554
    sprite('rc602_03', 6)	# 555-560
    sprite('rc602_04', 6)	# 561-566
    sprite('rc602_00', 6)	# 567-572
    SFX_0('019_cloth_a')
    if SLOT_158:
        Unknown7006('brc500', 100, 895709794, 12592, 0, 0, 100, 895709794, 13360, 0, 0, 100, 895709794, 13616, 0, 0, 100)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 573-578
    sprite('rc602_02', 6)	# 579-584
    sprite('rc602_03', 6)	# 585-590
    sprite('rc602_04', 6)	# 591-596
    sprite('rc602_00', 6)	# 597-602
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 603-608
    sprite('rc602_02', 6)	# 609-614
    sprite('rc602_03', 6)	# 615-620
    sprite('rc602_04', 6)	# 621-626
    sprite('rc602_05', 6)	# 627-632
    sprite('rc602_06', 6)	# 633-638
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(47)
    sprite('rc602_07', 5)	# 639-643
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 644-648
    sprite('rc602_09', 5)	# 649-653
    sprite('rc602_10', 5)	# 654-658
    sprite('rc602_11', 5)	# 659-663
    loopRest()
    gotoLabel(47)
    label(48)
    sprite('rc602_12', 5)	# 664-668
    Unknown21007(24, 41)
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 669-673
    sprite('rc602_14', 5)	# 674-678
    sprite('rc602_15', 5)	# 679-683
    sprite('rc602_16', 5)	# 684-688
    sprite('rc602_18', 7)	# 689-695
    sprite('rc602_19', 5)	# 696-700
    sprite('rc602_20', 5)	# 701-705
    sprite('rc602_21', 5)	# 706-710
    Unknown23018(1)
    label(21)
    sprite('rc000_00', 7)	# 711-717
    sprite('rc000_01', 7)	# 718-724
    sprite('rc000_02', 7)	# 725-731
    sprite('rc000_03', 7)	# 732-738
    sprite('rc000_04', 7)	# 739-745
    sprite('rc000_05', 7)	# 746-752
    sprite('rc000_06', 7)	# 753-759
    sprite('rc000_07', 7)	# 760-766
    sprite('rc000_08', 7)	# 767-773
    gotoLabel(21)
    ExitState()
    label(30)
    sprite('rc000_00', 1)	# 774-774
    SFX_1('brc701pmi')
    label(31)
    sprite('rc000_00', 7)	# 775-781
    sprite('rc000_01', 7)	# 782-788
    sprite('rc000_02', 7)	# 789-795
    sprite('rc000_03', 7)	# 796-802
    sprite('rc000_04', 7)	# 803-809
    sprite('rc000_05', 7)	# 810-816
    sprite('rc000_06', 7)	# 817-823
    sprite('rc000_07', 7)	# 824-830
    sprite('rc000_08', 7)	# 831-837
    gotoLabel(31)
    label(100)
    sprite('rc602_00', 6)	# 838-843
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(640000)
    Unknown3038(1)
    clearUponHandler(2)
    sendToLabelUpon(2, 102)
    sprite('rc602_00', 6)	# 844-849
    Unknown3038(0)
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 850-855
    sprite('rc602_02', 6)	# 856-861
    sprite('rc602_03', 6)	# 862-867
    sprite('rc602_04', 6)	# 868-873
    sprite('rc602_00', 6)	# 874-879
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 880-885
    sprite('rc602_02', 6)	# 886-891
    sprite('rc602_03', 6)	# 892-897
    sprite('rc602_04', 6)	# 898-903
    sprite('rc602_00', 6)	# 904-909
    SFX_0('019_cloth_a')
    SFX_1('brc600brg')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 910-915
    sprite('rc602_02', 6)	# 916-921
    sprite('rc602_03', 6)	# 922-927
    sprite('rc602_04', 6)	# 928-933
    sprite('rc602_00', 6)	# 934-939
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 940-945
    sprite('rc602_02', 6)	# 946-951
    sprite('rc602_03', 6)	# 952-957
    sprite('rc602_04', 6)	# 958-963
    sprite('rc602_05', 6)	# 964-969
    sprite('rc602_06', 6)	# 970-975
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(101)
    sprite('rc602_07', 5)	# 976-980
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 981-985
    sprite('rc602_09', 5)	# 986-990
    sprite('rc602_10', 5)	# 991-995
    sprite('rc602_11', 5)	# 996-1000
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('rc602_12', 5)	# 1001-1005
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 1006-1010
    sprite('rc602_14', 5)	# 1011-1015
    sprite('rc602_15', 5)	# 1016-1020
    sprite('rc602_16', 5)	# 1021-1025
    sprite('rc602_18', 7)	# 1026-1032
    sprite('rc602_19', 5)	# 1033-1037
    sprite('rc602_20', 5)	# 1038-1042
    sprite('rc602_21', 5)	# 1043-1047
    Unknown21011(240)
    label(103)
    sprite('rc000_00', 7)	# 1048-1054
    sprite('rc000_01', 7)	# 1055-1061
    sprite('rc000_02', 7)	# 1062-1068
    sprite('rc000_03', 7)	# 1069-1075
    sprite('rc000_04', 7)	# 1076-1082
    sprite('rc000_05', 7)	# 1083-1089
    sprite('rc000_06', 7)	# 1090-1096
    sprite('rc000_07', 7)	# 1097-1103
    sprite('rc000_08', 7)	# 1104-1110
    if SLOT_97:
        _gotolabel(103)
    sprite('rc000_00', 1)	# 1111-1111
    Unknown21007(24, 40)
    Unknown21011(240)
    label(104)
    sprite('rc000_00', 7)	# 1112-1118
    sprite('rc000_01', 7)	# 1119-1125
    sprite('rc000_02', 7)	# 1126-1132
    sprite('rc000_03', 7)	# 1133-1139
    sprite('rc000_04', 7)	# 1140-1146
    sprite('rc000_05', 7)	# 1147-1153
    sprite('rc000_06', 7)	# 1154-1160
    sprite('rc000_07', 7)	# 1161-1167
    sprite('rc000_08', 7)	# 1168-1174
    gotoLabel(104)
    label(110)
    sprite('rc602_00', 100)	# 1175-1274
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(640000)
    Unknown3038(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(114)
    clearUponHandler(2)
    sendToLabelUpon(2, 112)
    sprite('rc602_00', 6)	# 1275-1280
    Unknown3038(0)
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 1281-1286
    sprite('rc602_02', 6)	# 1287-1292
    sprite('rc602_03', 6)	# 1293-1298
    sprite('rc602_04', 6)	# 1299-1304
    sprite('rc602_00', 6)	# 1305-1310
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 1311-1316
    sprite('rc602_02', 6)	# 1317-1322
    sprite('rc602_03', 6)	# 1323-1328
    sprite('rc602_04', 6)	# 1329-1334
    sprite('rc602_00', 6)	# 1335-1340
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 1341-1346
    sprite('rc602_02', 6)	# 1347-1352
    sprite('rc602_03', 6)	# 1353-1358
    sprite('rc602_04', 6)	# 1359-1364
    sprite('rc602_00', 6)	# 1365-1370
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 1371-1376
    sprite('rc602_02', 6)	# 1377-1382
    sprite('rc602_03', 6)	# 1383-1388
    sprite('rc602_04', 6)	# 1389-1394
    sprite('rc602_05', 6)	# 1395-1400
    sprite('rc602_06', 6)	# 1401-1406
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(111)
    sprite('rc602_07', 5)	# 1407-1411
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 1412-1416
    sprite('rc602_09', 5)	# 1417-1421
    sprite('rc602_10', 5)	# 1422-1426
    sprite('rc602_11', 5)	# 1427-1431
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('rc602_12', 5)	# 1432-1436
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 1437-1441
    sprite('rc602_14', 5)	# 1442-1446
    sprite('rc602_15', 5)	# 1447-1451
    sprite('rc602_16', 5)	# 1452-1456
    sprite('rc602_18', 7)	# 1457-1463
    sprite('rc602_19', 5)	# 1464-1468
    sprite('rc602_20', 5)	# 1469-1473
    sprite('rc602_21', 5)	# 1474-1478
    label(113)
    sprite('rc000_00', 7)	# 1479-1485
    sprite('rc000_01', 7)	# 1486-1492
    sprite('rc000_02', 7)	# 1493-1499
    sprite('rc000_03', 7)	# 1500-1506
    sprite('rc000_04', 7)	# 1507-1513
    sprite('rc000_05', 7)	# 1514-1520
    sprite('rc000_06', 7)	# 1521-1527
    sprite('rc000_07', 7)	# 1528-1534
    sprite('rc000_08', 7)	# 1535-1541
    gotoLabel(113)
    label(114)
    sprite('rc001_00', 6)	# 1542-1547
    SFX_1('brc601bha')
    sprite('rc001_01', 6)	# 1548-1553
    sprite('rc001_02', 6)	# 1554-1559
    sprite('rc001_03', 6)	# 1560-1565
    sprite('rc001_04', 6)	# 1566-1571
    sprite('rc001_05', 6)	# 1572-1577
    sprite('rc001_06', 6)	# 1578-1583
    sprite('rc001_07', 6)	# 1584-1589
    sprite('rc001_08', 6)	# 1590-1595
    sprite('rc001_09', 6)	# 1596-1601
    sprite('rc001_10', 6)	# 1602-1607
    sprite('rc001_11', 6)	# 1608-1613
    sprite('rc001_12', 6)	# 1614-1619
    Unknown23018(1)
    label(115)
    sprite('rc000_00', 7)	# 1620-1626
    sprite('rc000_01', 7)	# 1627-1633
    sprite('rc000_02', 7)	# 1634-1640
    sprite('rc000_03', 7)	# 1641-1647
    sprite('rc000_04', 7)	# 1648-1654
    sprite('rc000_05', 7)	# 1655-1661
    sprite('rc000_06', 7)	# 1662-1668
    sprite('rc000_07', 7)	# 1669-1675
    sprite('rc000_08', 7)	# 1676-1682
    gotoLabel(115)
    ExitState()
    label(120)
    sprite('rc602_00', 32767)	# 1683-34449
    if SLOT_158:
        Unknown1000(-1465000)
    teleportRelativeY(640000)
    Unknown3038(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(121)
    label(121)
    clearUponHandler(2)
    sendToLabelUpon(2, 123)
    sprite('rc602_00', 6)	# 34450-34455
    Unknown3038(0)
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 34456-34461
    sprite('rc602_02', 6)	# 34462-34467
    sprite('rc602_03', 6)	# 34468-34473
    sprite('rc602_04', 6)	# 34474-34479
    sprite('rc602_00', 6)	# 34480-34485
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 34486-34491
    sprite('rc602_02', 6)	# 34492-34497
    sprite('rc602_03', 6)	# 34498-34503
    sprite('rc602_04', 6)	# 34504-34509
    sprite('rc602_00', 6)	# 34510-34515
    SFX_0('019_cloth_a')
    SFX_1('brc600bes')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 34516-34521
    sprite('rc602_02', 6)	# 34522-34527
    sprite('rc602_03', 6)	# 34528-34533
    sprite('rc602_04', 6)	# 34534-34539
    sprite('rc602_00', 6)	# 34540-34545
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 34546-34551
    sprite('rc602_02', 6)	# 34552-34557
    sprite('rc602_03', 6)	# 34558-34563
    sprite('rc602_04', 6)	# 34564-34569
    sprite('rc602_05', 6)	# 34570-34575
    sprite('rc602_06', 6)	# 34576-34581
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(122)
    sprite('rc602_07', 5)	# 34582-34586
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 34587-34591
    sprite('rc602_09', 5)	# 34592-34596
    sprite('rc602_10', 5)	# 34597-34601
    sprite('rc602_11', 5)	# 34602-34606
    loopRest()
    gotoLabel(122)
    label(123)
    sprite('rc602_12', 5)	# 34607-34611
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 34612-34616
    sprite('rc602_14', 5)	# 34617-34621
    sprite('rc602_15', 5)	# 34622-34626
    sprite('rc602_16', 5)	# 34627-34631
    sprite('rc602_18', 7)	# 34632-34638
    sprite('rc602_19', 5)	# 34639-34643
    sprite('rc602_20', 5)	# 34644-34648
    sprite('rc602_21', 5)	# 34649-34653
    Unknown21011(240)
    label(124)
    sprite('rc000_00', 7)	# 34654-34660
    sprite('rc000_01', 7)	# 34661-34667
    sprite('rc000_02', 7)	# 34668-34674
    sprite('rc000_03', 7)	# 34675-34681
    sprite('rc000_04', 7)	# 34682-34688
    sprite('rc000_05', 7)	# 34689-34695
    sprite('rc000_06', 7)	# 34696-34702
    sprite('rc000_07', 7)	# 34703-34709
    sprite('rc000_08', 7)	# 34710-34716
    if SLOT_97:
        _gotolabel(124)
    sprite('rc000_00', 1)	# 34717-34717
    Unknown21007(24, 40)
    Unknown21011(240)
    label(125)
    sprite('rc000_00', 7)	# 34718-34724
    sprite('rc000_01', 7)	# 34725-34731
    sprite('rc000_02', 7)	# 34732-34738
    sprite('rc000_03', 7)	# 34739-34745
    sprite('rc000_04', 7)	# 34746-34752
    sprite('rc000_05', 7)	# 34753-34759
    sprite('rc000_06', 7)	# 34760-34766
    sprite('rc000_07', 7)	# 34767-34773
    sprite('rc000_08', 7)	# 34774-34780
    gotoLabel(125)
    ExitState()
    label(130)
    sprite('rc600_00', 20)	# 34781-34800	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    sprite('rc600_00', 40)	# 34801-34840	 **attackbox here**
    sprite('rc600_01', 10)	# 34841-34850	 **attackbox here**
    sprite('rc600_02', 10)	# 34851-34860	 **attackbox here**
    sprite('rc600_03', 10)	# 34861-34870	 **attackbox here**
    sprite('rc600_03add01', 10)	# 34871-34880	 **attackbox here**
    sprite('rc600_04', 8)	# 34881-34888	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 34889-34896	 **attackbox here**
    sprite('rc600_05add01', 30)	# 34897-34926	 **attackbox here**
    SFX_1('brc600pyu')
    label(131)
    sprite('rc600_05add01', 1)	# 34927-34927	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('rc600_06', 8)	# 34928-34935	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 34936-34943	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 34944-34949	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 34950-34955	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 34956-34961	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 34962-34967	 **attackbox here**
    Unknown21007(24, 40)
    sprite('rc600_12', 6)	# 34968-34973	 **attackbox here**
    sprite('rc600_13', 6)	# 34974-34979	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 34980-34985	 **attackbox here**
    sprite('rc600_15', 6)	# 34986-34991	 **attackbox here**
    sprite('rc600_16', 6)	# 34992-34997	 **attackbox here**
    sprite('rc600_17', 6)	# 34998-35003	 **attackbox here**
    sprite('rc600_18', 6)	# 35004-35009	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 35010-35015	 **attackbox here**
    sprite('rc600_20', 6)	# 35016-35021	 **attackbox here**
    sprite('rc600_21', 6)	# 35022-35027	 **attackbox here**
    sprite('rc600_22', 6)	# 35028-35033	 **attackbox here**
    sprite('rc600_23', 6)	# 35034-35039	 **attackbox here**
    sprite('rc600_24', 6)	# 35040-35045	 **attackbox here**
    sprite('rc600_25', 6)	# 35046-35051	 **attackbox here**
    sprite('rc600_26', 6)	# 35052-35057	 **attackbox here**
    Unknown21011(240)
    label(132)
    sprite('rc000_00', 7)	# 35058-35064
    sprite('rc000_01', 7)	# 35065-35071
    sprite('rc000_02', 7)	# 35072-35078
    sprite('rc000_03', 7)	# 35079-35085
    sprite('rc000_04', 7)	# 35086-35092
    sprite('rc000_05', 7)	# 35093-35099
    sprite('rc000_06', 7)	# 35100-35106
    sprite('rc000_07', 7)	# 35107-35113
    sprite('rc000_08', 7)	# 35114-35120
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('rc600_00', 20)	# 35121-35140	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(141)
        SFX_1('brc601uli')
    sprite('rc600_00', 40)	# 35141-35180	 **attackbox here**
    sprite('rc600_01', 10)	# 35181-35190	 **attackbox here**
    sprite('rc600_02', 10)	# 35191-35200	 **attackbox here**
    sprite('rc600_03', 10)	# 35201-35210	 **attackbox here**
    sprite('rc600_03add01', 10)	# 35211-35220	 **attackbox here**
    sprite('rc600_04', 8)	# 35221-35228	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 35229-35236	 **attackbox here**
    sprite('rc600_05add01', 32767)	# 35237-68003	 **attackbox here**
    label(141)
    sprite('rc600_05add01', 1)	# 68004-68004	 **attackbox here**
    if SLOT_97:
        _gotolabel(141)
    sprite('rc600_06', 8)	# 68005-68012	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 68013-68020	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 68021-68026	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 68027-68032	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 68033-68038	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 68039-68044	 **attackbox here**
    sprite('rc600_12', 6)	# 68045-68050	 **attackbox here**
    sprite('rc600_13', 6)	# 68051-68056	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 68057-68062	 **attackbox here**
    sprite('rc600_15', 6)	# 68063-68068	 **attackbox here**
    sprite('rc600_16', 6)	# 68069-68074	 **attackbox here**
    sprite('rc600_17', 6)	# 68075-68080	 **attackbox here**
    sprite('rc600_18', 6)	# 68081-68086	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 68087-68092	 **attackbox here**
    sprite('rc600_20', 6)	# 68093-68098	 **attackbox here**
    sprite('rc600_21', 6)	# 68099-68104	 **attackbox here**
    sprite('rc600_22', 6)	# 68105-68110	 **attackbox here**
    sprite('rc600_23', 6)	# 68111-68116	 **attackbox here**
    sprite('rc600_24', 6)	# 68117-68122	 **attackbox here**
    sprite('rc600_25', 6)	# 68123-68128	 **attackbox here**
    sprite('rc600_26', 6)	# 68129-68134	 **attackbox here**
    Unknown21011(60)
    label(142)
    sprite('rc000_00', 7)	# 68135-68141
    sprite('rc000_01', 7)	# 68142-68148
    sprite('rc000_02', 7)	# 68149-68155
    sprite('rc000_03', 7)	# 68156-68162
    sprite('rc000_04', 7)	# 68163-68169
    sprite('rc000_05', 7)	# 68170-68176
    sprite('rc000_06', 7)	# 68177-68183
    sprite('rc000_07', 7)	# 68184-68190
    sprite('rc000_08', 7)	# 68191-68197
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('rc000_00', 1)	# 68198-68198
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(153)
    Unknown2037(1)
    label(151)
    sprite('rc000_00', 7)	# 68199-68205
    sprite('rc000_01', 7)	# 68206-68212
    sprite('rc000_02', 7)	# 68213-68219
    sprite('rc000_03', 7)	# 68220-68226
    sprite('rc000_04', 7)	# 68227-68233
    sprite('rc000_05', 7)	# 68234-68240
    sprite('rc000_06', 7)	# 68241-68247
    sprite('rc000_07', 7)	# 68248-68254
    sprite('rc000_08', 7)	# 68255-68261
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(151)
    sprite('rc001_00', 6)	# 68262-68267
    sprite('rc001_01', 6)	# 68268-68273
    sprite('rc001_02', 6)	# 68274-68279
    sprite('rc001_03', 6)	# 68280-68285
    sprite('rc001_04', 6)	# 68286-68291
    sprite('rc001_05', 6)	# 68292-68297
    sprite('rc001_06', 6)	# 68298-68303
    sprite('rc001_07', 6)	# 68304-68309
    sprite('rc001_08', 6)	# 68310-68315
    sprite('rc001_09', 6)	# 68316-68321
    sprite('rc001_10', 6)	# 68322-68327
    sprite('rc001_11', 6)	# 68328-68333
    sprite('rc001_12', 6)	# 68334-68339
    label(152)
    sprite('rc000_00', 7)	# 68340-68346
    sprite('rc000_01', 7)	# 68347-68353
    sprite('rc000_02', 7)	# 68354-68360
    sprite('rc000_03', 7)	# 68361-68367
    sprite('rc000_04', 7)	# 68368-68374
    sprite('rc000_05', 7)	# 68375-68381
    sprite('rc000_06', 7)	# 68382-68388
    sprite('rc000_07', 7)	# 68389-68395
    sprite('rc000_08', 7)	# 68396-68402
    gotoLabel(152)
    label(153)
    sprite('rc300_00', 6)	# 68403-68408
    sprite('rc300_01', 6)	# 68409-68414
    SFX_1('brc601rrb')
    sprite('rc300_02', 6)	# 68415-68420
    sprite('rc300_03', 6)	# 68421-68426
    loopRest()
    sprite('rc300_04', 7)	# 68427-68433
    SFX_3('rcse_00')
    sprite('rc300_05', 7)	# 68434-68440
    sprite('rc300_06', 7)	# 68441-68447
    sprite('rc300_07', 7)	# 68448-68454
    sprite('rc300_08', 7)	# 68455-68461
    sprite('rc300_09', 7)	# 68462-68468
    sprite('rc300_10', 7)	# 68469-68475
    SFX_3('rcse_00')
    sprite('rc300_11', 7)	# 68476-68482
    sprite('rc300_12', 7)	# 68483-68489
    sprite('rc300_13', 7)	# 68490-68496
    loopRest()
    sprite('rc300_04', 7)	# 68497-68503
    sprite('rc300_05', 7)	# 68504-68510
    sprite('rc300_06', 7)	# 68511-68517
    sprite('rc300_07', 7)	# 68518-68524
    sprite('rc300_08', 7)	# 68525-68531
    sprite('rc300_09', 7)	# 68532-68538
    sprite('rc300_10', 7)	# 68539-68545
    sprite('rc300_11', 7)	# 68546-68552
    sprite('rc300_12', 7)	# 68553-68559
    sprite('rc300_13', 7)	# 68560-68566
    sprite('rc300_14', 7)	# 68567-68573
    sprite('rc300_15', 7)	# 68574-68580
    sprite('rc300_16', 7)	# 68581-68587
    sprite('rc300_17', 7)	# 68588-68594
    Unknown23018(1)
    label(154)
    sprite('rc000_00', 7)	# 68595-68601
    sprite('rc000_01', 7)	# 68602-68608
    sprite('rc000_02', 7)	# 68609-68615
    sprite('rc000_03', 7)	# 68616-68622
    sprite('rc000_04', 7)	# 68623-68629
    sprite('rc000_05', 7)	# 68630-68636
    sprite('rc000_06', 7)	# 68637-68643
    sprite('rc000_07', 7)	# 68644-68650
    sprite('rc000_08', 7)	# 68651-68657
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('rc602_00', 32767)	# 68658-101424
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(640000)
    Unknown3038(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(161)
    label(161)
    clearUponHandler(2)
    sendToLabelUpon(2, 163)
    sprite('rc602_00', 6)	# 101425-101430
    Unknown3038(0)
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 101431-101436
    sprite('rc602_02', 6)	# 101437-101442
    sprite('rc602_03', 6)	# 101443-101448
    sprite('rc602_04', 6)	# 101449-101454
    sprite('rc602_00', 6)	# 101455-101460
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 101461-101466
    sprite('rc602_02', 6)	# 101467-101472
    sprite('rc602_03', 6)	# 101473-101478
    sprite('rc602_04', 6)	# 101479-101484
    sprite('rc602_00', 6)	# 101485-101490
    SFX_0('019_cloth_a')
    SFX_1('brc601uva')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 101491-101496
    sprite('rc602_02', 6)	# 101497-101502
    sprite('rc602_03', 6)	# 101503-101508
    sprite('rc602_04', 6)	# 101509-101514
    sprite('rc602_00', 6)	# 101515-101520
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 101521-101526
    sprite('rc602_02', 6)	# 101527-101532
    sprite('rc602_03', 6)	# 101533-101538
    sprite('rc602_04', 6)	# 101539-101544
    sprite('rc602_05', 6)	# 101545-101550
    sprite('rc602_06', 6)	# 101551-101556
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(162)
    sprite('rc602_07', 5)	# 101557-101561
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 101562-101566
    sprite('rc602_09', 5)	# 101567-101571
    sprite('rc602_10', 5)	# 101572-101576
    sprite('rc602_11', 5)	# 101577-101581
    loopRest()
    gotoLabel(162)
    label(163)
    sprite('rc602_12', 5)	# 101582-101586
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 101587-101591
    sprite('rc602_14', 5)	# 101592-101596
    sprite('rc602_15', 5)	# 101597-101601
    sprite('rc602_16', 5)	# 101602-101606
    sprite('rc602_18', 7)	# 101607-101613
    sprite('rc602_19', 5)	# 101614-101618
    sprite('rc602_20', 5)	# 101619-101623
    sprite('rc602_21', 5)	# 101624-101628
    Unknown23018(1)
    label(164)
    sprite('rc000_00', 7)	# 101629-101635
    sprite('rc000_01', 7)	# 101636-101642
    sprite('rc000_02', 7)	# 101643-101649
    sprite('rc000_03', 7)	# 101650-101656
    sprite('rc000_04', 7)	# 101657-101663
    sprite('rc000_05', 7)	# 101664-101670
    sprite('rc000_06', 7)	# 101671-101677
    sprite('rc000_07', 7)	# 101678-101684
    sprite('rc000_08', 7)	# 101685-101691
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('rc600_00', 32767)	# 101692-134458	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(171)
    label(171)
    sprite('rc600_00', 60)	# 134459-134518	 **attackbox here**
    sprite('rc600_01', 10)	# 134519-134528	 **attackbox here**
    sprite('rc600_02', 10)	# 134529-134538	 **attackbox here**
    sprite('rc600_03', 10)	# 134539-134548	 **attackbox here**
    sprite('rc600_03add01', 10)	# 134549-134558	 **attackbox here**
    sprite('rc600_04', 8)	# 134559-134566	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 134567-134574	 **attackbox here**
    sprite('rc600_05add01', 130)	# 134575-134704	 **attackbox here**
    SFX_1('brc601umi')
    sprite('rc600_06', 8)	# 134705-134712	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 134713-134720	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 134721-134726	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 134727-134732	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 134733-134738	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 134739-134744	 **attackbox here**
    sprite('rc600_12', 6)	# 134745-134750	 **attackbox here**
    sprite('rc600_13', 6)	# 134751-134756	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 134757-134762	 **attackbox here**
    sprite('rc600_15', 6)	# 134763-134768	 **attackbox here**
    sprite('rc600_16', 6)	# 134769-134774	 **attackbox here**
    sprite('rc600_17', 6)	# 134775-134780	 **attackbox here**
    sprite('rc600_18', 6)	# 134781-134786	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 134787-134792	 **attackbox here**
    sprite('rc600_20', 6)	# 134793-134798	 **attackbox here**
    sprite('rc600_21', 6)	# 134799-134804	 **attackbox here**
    sprite('rc600_22', 6)	# 134805-134810	 **attackbox here**
    sprite('rc600_23', 6)	# 134811-134816	 **attackbox here**
    sprite('rc600_24', 6)	# 134817-134822	 **attackbox here**
    sprite('rc600_25', 6)	# 134823-134828	 **attackbox here**
    sprite('rc600_26', 6)	# 134829-134834	 **attackbox here**
    Unknown23018(1)
    label(172)
    sprite('rc000_00', 7)	# 134835-134841
    sprite('rc000_01', 7)	# 134842-134848
    sprite('rc000_02', 7)	# 134849-134855
    sprite('rc000_03', 7)	# 134856-134862
    sprite('rc000_04', 7)	# 134863-134869
    sprite('rc000_05', 7)	# 134870-134876
    sprite('rc000_06', 7)	# 134877-134883
    sprite('rc000_07', 7)	# 134884-134890
    sprite('rc000_08', 7)	# 134891-134897
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('rc600_00', 20)	# 134898-134917	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    sprite('rc600_00', 40)	# 134918-134957	 **attackbox here**
    sprite('rc600_01', 10)	# 134958-134967	 **attackbox here**
    sprite('rc600_02', 10)	# 134968-134977	 **attackbox here**
    sprite('rc600_03', 10)	# 134978-134987	 **attackbox here**
    sprite('rc600_03add01', 10)	# 134988-134997	 **attackbox here**
    sprite('rc600_04', 8)	# 134998-135005	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 135006-135013	 **attackbox here**
    sprite('rc600_05add01', 30)	# 135014-135043	 **attackbox here**
    SFX_1('brc600pmi')
    label(181)
    sprite('rc600_05add01', 1)	# 135044-135044	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('rc600_06', 8)	# 135045-135052	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 135053-135060	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 135061-135066	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 135067-135072	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 135073-135078	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 135079-135084	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    sprite('rc600_12', 6)	# 135085-135090	 **attackbox here**
    sprite('rc600_13', 6)	# 135091-135096	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 135097-135102	 **attackbox here**
    sprite('rc600_15', 6)	# 135103-135108	 **attackbox here**
    sprite('rc600_16', 6)	# 135109-135114	 **attackbox here**
    sprite('rc600_17', 6)	# 135115-135120	 **attackbox here**
    sprite('rc600_18', 6)	# 135121-135126	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 135127-135132	 **attackbox here**
    sprite('rc600_20', 6)	# 135133-135138	 **attackbox here**
    sprite('rc600_21', 6)	# 135139-135144	 **attackbox here**
    sprite('rc600_22', 6)	# 135145-135150	 **attackbox here**
    sprite('rc600_23', 6)	# 135151-135156	 **attackbox here**
    sprite('rc600_24', 6)	# 135157-135162	 **attackbox here**
    sprite('rc600_25', 6)	# 135163-135168	 **attackbox here**
    sprite('rc600_26', 6)	# 135169-135174	 **attackbox here**
    label(182)
    sprite('rc000_00', 7)	# 135175-135181
    sprite('rc000_01', 7)	# 135182-135188
    sprite('rc000_02', 7)	# 135189-135195
    sprite('rc000_03', 7)	# 135196-135202
    sprite('rc000_04', 7)	# 135203-135209
    sprite('rc000_05', 7)	# 135210-135216
    sprite('rc000_06', 7)	# 135217-135223
    sprite('rc000_07', 7)	# 135224-135230
    sprite('rc000_08', 7)	# 135231-135237
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('rc602_00', 32767)	# 135238-168004
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    teleportRelativeY(640000)
    Unknown3038(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(191)
    label(191)
    clearUponHandler(2)
    sendToLabelUpon(2, 193)
    sprite('rc602_00', 6)	# 168005-168010
    Unknown3038(0)
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 168011-168016
    sprite('rc602_02', 6)	# 168017-168022
    sprite('rc602_03', 6)	# 168023-168028
    sprite('rc602_04', 6)	# 168029-168034
    sprite('rc602_00', 6)	# 168035-168040
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 168041-168046
    sprite('rc602_02', 6)	# 168047-168052
    sprite('rc602_03', 6)	# 168053-168058
    sprite('rc602_04', 6)	# 168059-168064
    sprite('rc602_00', 6)	# 168065-168070
    SFX_0('019_cloth_a')
    SFX_1('brc601bph')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 168071-168076
    sprite('rc602_02', 6)	# 168077-168082
    sprite('rc602_03', 6)	# 168083-168088
    sprite('rc602_04', 6)	# 168089-168094
    sprite('rc602_00', 6)	# 168095-168100
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 168101-168106
    sprite('rc602_02', 6)	# 168107-168112
    sprite('rc602_03', 6)	# 168113-168118
    sprite('rc602_04', 6)	# 168119-168124
    sprite('rc602_05', 6)	# 168125-168130
    sprite('rc602_06', 6)	# 168131-168136
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(192)
    sprite('rc602_07', 5)	# 168137-168141
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 168142-168146
    sprite('rc602_09', 5)	# 168147-168151
    sprite('rc602_10', 5)	# 168152-168156
    sprite('rc602_11', 5)	# 168157-168161
    loopRest()
    gotoLabel(192)
    label(193)
    sprite('rc602_12', 5)	# 168162-168166
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 168167-168171
    sprite('rc602_14', 5)	# 168172-168176
    sprite('rc602_15', 5)	# 168177-168181
    sprite('rc602_16', 5)	# 168182-168186
    sprite('rc602_18', 7)	# 168187-168193
    sprite('rc602_19', 5)	# 168194-168198
    sprite('rc602_20', 5)	# 168199-168203
    sprite('rc602_21', 5)	# 168204-168208
    Unknown23018(1)
    label(194)
    sprite('rc000_00', 7)	# 168209-168215
    sprite('rc000_01', 7)	# 168216-168222
    sprite('rc000_02', 7)	# 168223-168229
    sprite('rc000_03', 7)	# 168230-168236
    sprite('rc000_04', 7)	# 168237-168243
    sprite('rc000_05', 7)	# 168244-168250
    sprite('rc000_06', 7)	# 168251-168257
    sprite('rc000_07', 7)	# 168258-168264
    sprite('rc000_08', 7)	# 168265-168271
    gotoLabel(194)
    ExitState()
    label(991)
    sprite('rc000_00', 1)	# 168272-168272
    Unknown21007(11, 40)
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('rc000_00', 7)	# 168273-168279
    sprite('rc000_01', 7)	# 168280-168286
    sprite('rc000_02', 7)	# 168287-168293
    sprite('rc000_03', 7)	# 168294-168300
    sprite('rc000_04', 7)	# 168301-168307
    sprite('rc000_05', 7)	# 168308-168314
    sprite('rc000_06', 7)	# 168315-168321
    sprite('rc000_07', 7)	# 168322-168328
    sprite('rc000_08', 7)	# 168329-168335
    gotoLabel(992)
    label(993)
    sprite('rc406_00', 3)	# 168336-168338

    def upon_STATE_END():
        Unknown2019(0)
        Unknown3001(255)
        Unknown3004(0)
    GFX_1('haef_event_lose_end', 0)
    sprite('rc406_01', 3)	# 168339-168341
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc406_02', 3)	# 168342-168344
    sprite('rc406_03', 3)	# 168345-168347
    Unknown3004(-12)
    sprite('rc406_04', 4)	# 168348-168351
    SFX_0('022_magiccircle_b')
    SFX_0('019_cloth_a')
    sprite('rc406_05', 4)	# 168352-168355
    sprite('rc406_06', 4)	# 168356-168359
    sprite('rc406_07', 4)	# 168360-168363
    sprite('rc406_08', 5)	# 168364-168368
    loopRest()
    ExitState()

@State
def CmnActRoundWin():
    sprite('rc300_00', 6)	# 1-6
    GFX_0('BatSummons', 0)
    sprite('rc300_01', 6)	# 7-12
    sprite('rc300_02', 6)	# 13-18
    sprite('rc300_03', 6)	# 19-24
    sprite('rc300_04', 7)	# 25-31
    if random_(2, 0, 50):
        SFX_1('rc400')
    else:
        SFX_1('rc401')
    Unknown23018(1)
    sprite('rc300_05', 7)	# 32-38
    SFX_3('rcse_00')
    sprite('rc300_06', 7)	# 39-45
    sprite('rc300_07', 7)	# 46-52
    sprite('rc300_08', 7)	# 53-59
    sprite('rc300_14', 6)	# 60-65
    sprite('rc300_15', 6)	# 66-71
    sprite('rc300_16', 6)	# 72-77
    sprite('rc300_17', 6)	# 78-83
    loopRest()
    Unknown19(1, 2, 97)
    label(0)
    sprite('rc000_00', 7)	# 84-90
    sprite('rc000_01', 7)	# 91-97
    sprite('rc000_02', 7)	# 98-104
    sprite('rc000_03', 7)	# 105-111
    sprite('rc000_04', 7)	# 112-118
    sprite('rc000_05', 7)	# 119-125
    sprite('rc000_06', 7)	# 126-132
    sprite('rc000_07', 7)	# 133-139
    sprite('rc000_08', 7)	# 140-146
    loopRest()
    if SLOT_97:
        _gotolabel(0)
    label(1)
    label(2)
    sprite('rc000_00', 7)	# 147-153
    sprite('rc000_01', 7)	# 154-160
    sprite('rc000_02', 7)	# 161-167
    sprite('rc000_03', 7)	# 168-174
    sprite('rc000_04', 7)	# 175-181
    sprite('rc000_05', 7)	# 182-188
    sprite('rc000_06', 7)	# 189-195
    sprite('rc000_07', 7)	# 196-202
    sprite('rc000_08', 7)	# 203-209
    loopRest()
    gotoLabel(2)

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
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('bph'):
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
    sprite('rc610_00', 6)	# 4-9
    if SLOT_158:
        Unknown2019(-1000)
    sprite('rc610_01', 6)	# 10-15
    sprite('rc610_02', 6)	# 16-21
    sprite('rc610_03', 6)	# 22-27
    sprite('rc610_04', 6)	# 28-33
    sprite('rc610_05', 6)	# 34-39
    sprite('rc610_06', 6)	# 40-45
    sprite('rc610_07', 6)	# 46-51	 **attackbox here**
    sprite('rc610_08', 6)	# 52-57	 **attackbox here**
    sprite('rc610_09', 6)	# 58-63	 **attackbox here**
    sprite('rc610_10', 6)	# 64-69	 **attackbox here**
    sprite('rc610_11', 6)	# 70-75	 **attackbox here**
    sprite('rc610_12', 6)	# 76-81	 **attackbox here**
    sprite('rc610_13', 6)	# 82-87	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('brc524', 100, 895709794, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('brc404_0', 100, 878932578, 828322864, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('brc520', 100, 0, 0, 0, 0, 0, 895709794, 12850, 0, 0, 100, 895709794, 13106, 0, 0, 100)
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 88-93	 **attackbox here**
    sprite('rc610_15', 6)	# 94-99	 **attackbox here**
    sprite('rc610_16', 6)	# 100-105	 **attackbox here**
    sprite('rc610_17', 6)	# 106-111	 **attackbox here**
    sprite('rc610_18', 6)	# 112-117	 **attackbox here**
    sprite('rc610_19', 6)	# 118-123	 **attackbox here**
    sprite('rc610_20', 6)	# 124-129	 **attackbox here**
    sprite('rc610_21', 6)	# 130-135	 **attackbox here**
    Unknown23018(1)
    sprite('rc610_21add01', 6)	# 136-141	 **attackbox here**
    sprite('rc610_21add02', 6)	# 142-147	 **attackbox here**
    sprite('rc610_21add03', 6)	# 148-153	 **attackbox here**
    sprite('rc610_21add04', 6)	# 154-159	 **attackbox here**
    sprite('rc610_21add03', 6)	# 160-165	 **attackbox here**
    sprite('rc610_21add02', 6)	# 166-171	 **attackbox here**
    sprite('rc610_21add01', 6)	# 172-177	 **attackbox here**
    sprite('rc610_21', 6)	# 178-183	 **attackbox here**
    label(2)
    sprite('rc610_21add01', 6)	# 184-189	 **attackbox here**
    sprite('rc610_21add02', 6)	# 190-195	 **attackbox here**
    sprite('rc610_21add03', 6)	# 196-201	 **attackbox here**
    sprite('rc610_21add04', 6)	# 202-207	 **attackbox here**
    sprite('rc610_21add03', 6)	# 208-213	 **attackbox here**
    sprite('rc610_21add02', 6)	# 214-219	 **attackbox here**
    sprite('rc610_21add01', 6)	# 220-225	 **attackbox here**
    sprite('rc610_21', 6)	# 226-231	 **attackbox here**
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('rc611_00', 6)	# 232-237
    sprite('rc611_01', 6)	# 238-243
    if SLOT_158:
        if SLOT_108:
            Unknown7006('brc404_0', 100, 878932578, 828322864, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            SFX_1('brc521')
    Unknown23018(1)
    sprite('rc611_02', 6)	# 244-249
    sprite('rc611_03', 6)	# 250-255
    SFX_0('019_cloth_b')
    sprite('rc611_04', 6)	# 256-261
    sprite('rc611_05', 14)	# 262-275
    sprite('rc611_06', 6)	# 276-281
    sprite('rc611_07', 6)	# 282-287
    sprite('rc611_08', 6)	# 288-293
    sprite('rc611_08ex01', 6)	# 294-299
    sprite('rc611_08ex02', 6)	# 300-305
    GFX_0('BatDelete', 0)
    sprite('rc611_09', 3)	# 306-308
    Unknown3010(-8)
    Unknown3016(-8)
    Unknown3022(-8)
    sprite('rc611_10', 1)	# 309-309
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 310-310
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 311-311
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 312-312
    SFX_0('019_cloth_c')
    SFX_3('rcse_11')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 313-313
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 314-314
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 315-315
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 316-316
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 317-317
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 318-318
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 319-319
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 320-320
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 321-321
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 322-322
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 323-323
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 324-324
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 325-325
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 326-326
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15ex01', 30)	# 327-356
    Unknown51(1)
    label(100)
    sprite('rc610_00', 6)	# 357-362
    if (not SLOT_158):
        Unknown2019(1000)
    sprite('rc610_01', 6)	# 363-368
    sprite('rc610_02', 6)	# 369-374
    sprite('rc610_03', 6)	# 375-380
    sprite('rc610_04', 6)	# 381-386
    sprite('rc610_05', 6)	# 387-392
    sprite('rc610_06', 6)	# 393-398
    sprite('rc610_07', 6)	# 399-404	 **attackbox here**
    sprite('rc610_08', 6)	# 405-410	 **attackbox here**
    sprite('rc610_09', 6)	# 411-416	 **attackbox here**
    sprite('rc610_10', 6)	# 417-422	 **attackbox here**
    sprite('rc610_11', 6)	# 423-428	 **attackbox here**
    sprite('rc610_12', 6)	# 429-434	 **attackbox here**
    sprite('rc610_13', 6)	# 435-440	 **attackbox here**
    SFX_1('brc700brg')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 441-446	 **attackbox here**
    sprite('rc610_15', 6)	# 447-452	 **attackbox here**
    sprite('rc610_16', 6)	# 453-458	 **attackbox here**
    sprite('rc610_17', 6)	# 459-464	 **attackbox here**
    sprite('rc610_18', 6)	# 465-470	 **attackbox here**
    sprite('rc610_19', 6)	# 471-476	 **attackbox here**
    sprite('rc610_20', 6)	# 477-482	 **attackbox here**
    sprite('rc610_21', 6)	# 483-488	 **attackbox here**
    sprite('rc610_21add01', 6)	# 489-494	 **attackbox here**
    sprite('rc610_21add02', 6)	# 495-500	 **attackbox here**
    sprite('rc610_21add03', 6)	# 501-506	 **attackbox here**
    sprite('rc610_21add04', 6)	# 507-512	 **attackbox here**
    sprite('rc610_21add03', 6)	# 513-518	 **attackbox here**
    sprite('rc610_21add02', 6)	# 519-524	 **attackbox here**
    sprite('rc610_21add01', 6)	# 525-530	 **attackbox here**
    sprite('rc610_21', 6)	# 531-536	 **attackbox here**
    label(101)
    sprite('rc610_21add01', 6)	# 537-542	 **attackbox here**
    sprite('rc610_21add02', 6)	# 543-548	 **attackbox here**
    sprite('rc610_21add03', 6)	# 549-554	 **attackbox here**
    sprite('rc610_21add04', 6)	# 555-560	 **attackbox here**
    sprite('rc610_21add03', 6)	# 561-566	 **attackbox here**
    sprite('rc610_21add02', 6)	# 567-572	 **attackbox here**
    sprite('rc610_21add01', 6)	# 573-578	 **attackbox here**
    sprite('rc610_21', 6)	# 579-584	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('rc610_21add01', 1)	# 585-585	 **attackbox here**
    Unknown21011(310)
    Unknown21007(24, 40)
    label(102)
    sprite('rc610_21add01', 6)	# 586-591	 **attackbox here**
    sprite('rc610_21add02', 6)	# 592-597	 **attackbox here**
    sprite('rc610_21add03', 6)	# 598-603	 **attackbox here**
    sprite('rc610_21add04', 6)	# 604-609	 **attackbox here**
    sprite('rc610_21add03', 6)	# 610-615	 **attackbox here**
    sprite('rc610_21add02', 6)	# 616-621	 **attackbox here**
    sprite('rc610_21add01', 6)	# 622-627	 **attackbox here**
    sprite('rc610_21', 6)	# 628-633	 **attackbox here**
    gotoLabel(102)
    label(110)
    sprite('rc610_00', 6)	# 634-639
    Unknown2019(1000)
    sprite('rc610_01', 6)	# 640-645
    sprite('rc610_02', 6)	# 646-651
    sprite('rc610_03', 6)	# 652-657
    sprite('rc610_04', 6)	# 658-663
    sprite('rc610_05', 6)	# 664-669
    sprite('rc610_06', 6)	# 670-675
    sprite('rc610_07', 6)	# 676-681	 **attackbox here**
    sprite('rc610_08', 6)	# 682-687	 **attackbox here**
    sprite('rc610_09', 6)	# 688-693	 **attackbox here**
    sprite('rc610_10', 6)	# 694-699	 **attackbox here**
    sprite('rc610_11', 6)	# 700-705	 **attackbox here**
    sprite('rc610_12', 6)	# 706-711	 **attackbox here**
    sprite('rc610_13', 6)	# 712-717	 **attackbox here**
    SFX_1('brc700bha')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 718-723	 **attackbox here**
    sprite('rc610_15', 6)	# 724-729	 **attackbox here**
    sprite('rc610_16', 6)	# 730-735	 **attackbox here**
    sprite('rc610_17', 6)	# 736-741	 **attackbox here**
    sprite('rc610_18', 6)	# 742-747	 **attackbox here**
    sprite('rc610_19', 6)	# 748-753	 **attackbox here**
    sprite('rc610_20', 6)	# 754-759	 **attackbox here**
    sprite('rc610_21', 6)	# 760-765	 **attackbox here**
    sprite('rc610_21add01', 6)	# 766-771	 **attackbox here**
    sprite('rc610_21add02', 6)	# 772-777	 **attackbox here**
    sprite('rc610_21add03', 6)	# 778-783	 **attackbox here**
    sprite('rc610_21add04', 6)	# 784-789	 **attackbox here**
    sprite('rc610_21add03', 6)	# 790-795	 **attackbox here**
    sprite('rc610_21add02', 6)	# 796-801	 **attackbox here**
    sprite('rc610_21add01', 6)	# 802-807	 **attackbox here**
    sprite('rc610_21', 6)	# 808-813	 **attackbox here**
    label(111)
    sprite('rc610_21add01', 6)	# 814-819	 **attackbox here**
    sprite('rc610_21add02', 6)	# 820-825	 **attackbox here**
    sprite('rc610_21add03', 6)	# 826-831	 **attackbox here**
    sprite('rc610_21add04', 6)	# 832-837	 **attackbox here**
    sprite('rc610_21add03', 6)	# 838-843	 **attackbox here**
    sprite('rc610_21add02', 6)	# 844-849	 **attackbox here**
    sprite('rc610_21add01', 6)	# 850-855	 **attackbox here**
    sprite('rc610_21', 6)	# 856-861	 **attackbox here**
    if SLOT_97:
        _gotolabel(111)
    sprite('rc610_21add01', 1)	# 862-862	 **attackbox here**
    Unknown21011(360)
    Unknown21007(24, 40)
    label(112)
    sprite('rc610_21add01', 6)	# 863-868	 **attackbox here**
    sprite('rc610_21add02', 6)	# 869-874	 **attackbox here**
    sprite('rc610_21add03', 6)	# 875-880	 **attackbox here**
    sprite('rc610_21add04', 6)	# 881-886	 **attackbox here**
    sprite('rc610_21add03', 6)	# 887-892	 **attackbox here**
    sprite('rc610_21add02', 6)	# 893-898	 **attackbox here**
    sprite('rc610_21add01', 6)	# 899-904	 **attackbox here**
    sprite('rc610_21', 6)	# 905-910	 **attackbox here**
    gotoLabel(112)
    label(120)
    sprite('rc610_00', 6)	# 911-916
    Unknown2019(1000)
    sprite('rc610_01', 6)	# 917-922
    sprite('rc610_02', 6)	# 923-928
    sprite('rc610_03', 6)	# 929-934
    sprite('rc610_04', 6)	# 935-940
    sprite('rc610_05', 6)	# 941-946
    sprite('rc610_06', 6)	# 947-952
    sprite('rc610_07', 6)	# 953-958	 **attackbox here**
    sprite('rc610_08', 6)	# 959-964	 **attackbox here**
    sprite('rc610_09', 6)	# 965-970	 **attackbox here**
    sprite('rc610_10', 6)	# 971-976	 **attackbox here**
    sprite('rc610_11', 6)	# 977-982	 **attackbox here**
    sprite('rc610_12', 6)	# 983-988	 **attackbox here**
    sprite('rc610_13', 6)	# 989-994	 **attackbox here**
    SFX_1('brc700bes')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 995-1000	 **attackbox here**
    sprite('rc610_15', 6)	# 1001-1006	 **attackbox here**
    sprite('rc610_16', 6)	# 1007-1012	 **attackbox here**
    sprite('rc610_17', 6)	# 1013-1018	 **attackbox here**
    sprite('rc610_18', 6)	# 1019-1024	 **attackbox here**
    sprite('rc610_19', 6)	# 1025-1030	 **attackbox here**
    sprite('rc610_20', 6)	# 1031-1036	 **attackbox here**
    sprite('rc610_21', 6)	# 1037-1042	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1043-1048	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1049-1054	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1055-1060	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1061-1066	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1067-1072	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1073-1078	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1079-1084	 **attackbox here**
    sprite('rc610_21', 6)	# 1085-1090	 **attackbox here**
    label(121)
    sprite('rc610_21add01', 6)	# 1091-1096	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1097-1102	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1103-1108	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1109-1114	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1115-1120	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1121-1126	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1127-1132	 **attackbox here**
    sprite('rc610_21', 6)	# 1133-1138	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('rc610_21add01', 1)	# 1139-1139	 **attackbox here**
    Unknown21011(240)
    Unknown21007(24, 40)
    label(122)
    sprite('rc610_21add01', 6)	# 1140-1145	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1146-1151	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1152-1157	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1158-1163	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1164-1169	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1170-1175	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1176-1181	 **attackbox here**
    sprite('rc610_21', 6)	# 1182-1187	 **attackbox here**
    gotoLabel(122)
    label(130)
    sprite('rc610_00', 6)	# 1188-1193
    if (not SLOT_158):
        Unknown2019(1000)
    sprite('rc610_01', 6)	# 1194-1199
    sprite('rc610_02', 6)	# 1200-1205
    sprite('rc610_03', 6)	# 1206-1211
    sprite('rc610_04', 6)	# 1212-1217
    sprite('rc610_05', 6)	# 1218-1223
    sprite('rc610_06', 6)	# 1224-1229
    sprite('rc610_07', 6)	# 1230-1235	 **attackbox here**
    sprite('rc610_08', 6)	# 1236-1241	 **attackbox here**
    sprite('rc610_09', 6)	# 1242-1247	 **attackbox here**
    sprite('rc610_10', 6)	# 1248-1253	 **attackbox here**
    sprite('rc610_11', 6)	# 1254-1259	 **attackbox here**
    sprite('rc610_12', 6)	# 1260-1265	 **attackbox here**
    sprite('rc610_13', 6)	# 1266-1271	 **attackbox here**
    SFX_1('brc700pyu')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 1272-1277	 **attackbox here**
    sprite('rc610_15', 6)	# 1278-1283	 **attackbox here**
    sprite('rc610_16', 6)	# 1284-1289	 **attackbox here**
    sprite('rc610_17', 6)	# 1290-1295	 **attackbox here**
    sprite('rc610_18', 6)	# 1296-1301	 **attackbox here**
    sprite('rc610_19', 6)	# 1302-1307	 **attackbox here**
    sprite('rc610_20', 6)	# 1308-1313	 **attackbox here**
    sprite('rc610_21', 6)	# 1314-1319	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1320-1325	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1326-1331	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1332-1337	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1338-1343	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1344-1349	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1350-1355	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1356-1361	 **attackbox here**
    sprite('rc610_21', 6)	# 1362-1367	 **attackbox here**
    label(131)
    sprite('rc610_21add01', 6)	# 1368-1373	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1374-1379	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1380-1385	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1386-1391	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1392-1397	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1398-1403	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1404-1409	 **attackbox here**
    sprite('rc610_21', 6)	# 1410-1415	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('rc610_21add01', 1)	# 1416-1416	 **attackbox here**
    Unknown21011(120)
    Unknown21007(24, 40)
    label(132)
    sprite('rc610_21add01', 6)	# 1417-1422	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1423-1428	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1429-1434	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1435-1440	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1441-1446	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1447-1452	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1453-1458	 **attackbox here**
    sprite('rc610_21', 6)	# 1459-1464	 **attackbox here**
    gotoLabel(132)
    label(140)
    sprite('rc610_00', 6)	# 1465-1470
    if (not SLOT_158):
        Unknown2019(1000)
    sprite('rc610_01', 6)	# 1471-1476
    sprite('rc610_02', 6)	# 1477-1482
    sprite('rc610_03', 6)	# 1483-1488
    sprite('rc610_04', 6)	# 1489-1494
    sprite('rc610_05', 6)	# 1495-1500
    sprite('rc610_06', 6)	# 1501-1506
    sprite('rc610_07', 6)	# 1507-1512	 **attackbox here**
    sprite('rc610_08', 6)	# 1513-1518	 **attackbox here**
    sprite('rc610_09', 6)	# 1519-1524	 **attackbox here**
    sprite('rc610_10', 6)	# 1525-1530	 **attackbox here**
    sprite('rc610_11', 6)	# 1531-1536	 **attackbox here**
    sprite('rc610_12', 6)	# 1537-1542	 **attackbox here**
    sprite('rc610_13', 6)	# 1543-1548	 **attackbox here**
    SFX_1('brc700uli')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 1549-1554	 **attackbox here**
    sprite('rc610_15', 6)	# 1555-1560	 **attackbox here**
    sprite('rc610_16', 6)	# 1561-1566	 **attackbox here**
    sprite('rc610_17', 6)	# 1567-1572	 **attackbox here**
    sprite('rc610_18', 6)	# 1573-1578	 **attackbox here**
    sprite('rc610_19', 6)	# 1579-1584	 **attackbox here**
    sprite('rc610_20', 6)	# 1585-1590	 **attackbox here**
    sprite('rc610_21', 6)	# 1591-1596	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1597-1602	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1603-1608	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1609-1614	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1615-1620	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1621-1626	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1627-1632	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1633-1638	 **attackbox here**
    sprite('rc610_21', 6)	# 1639-1644	 **attackbox here**
    label(141)
    sprite('rc610_21add01', 6)	# 1645-1650	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1651-1656	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1657-1662	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1663-1668	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1669-1674	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1675-1680	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1681-1686	 **attackbox here**
    sprite('rc610_21', 6)	# 1687-1692	 **attackbox here**
    if SLOT_97:
        _gotolabel(141)
    sprite('rc610_21add01', 1)	# 1693-1693	 **attackbox here**
    Unknown21011(200)
    Unknown21007(24, 40)
    label(142)
    sprite('rc610_21add01', 6)	# 1694-1699	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1700-1705	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1706-1711	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1712-1717	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1718-1723	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1724-1729	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1730-1735	 **attackbox here**
    sprite('rc610_21', 6)	# 1736-1741	 **attackbox here**
    gotoLabel(142)
    label(150)
    sprite('rc000_00', 1)	# 1742-1742
    if (not SLOT_158):
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('rc000_00', 7)	# 1743-1749
    sprite('rc000_01', 7)	# 1750-1756
    sprite('rc000_02', 7)	# 1757-1763
    sprite('rc000_03', 7)	# 1764-1770
    sprite('rc000_04', 7)	# 1771-1777
    sprite('rc000_05', 7)	# 1778-1784
    sprite('rc000_06', 7)	# 1785-1791
    sprite('rc000_07', 7)	# 1792-1798
    sprite('rc000_08', 7)	# 1799-1805
    gotoLabel(151)
    label(152)
    sprite('rc610_00', 6)	# 1806-1811
    sprite('rc610_01', 6)	# 1812-1817
    sprite('rc610_02', 6)	# 1818-1823
    sprite('rc610_03', 6)	# 1824-1829
    sprite('rc610_04', 6)	# 1830-1835
    sprite('rc610_05', 6)	# 1836-1841
    sprite('rc610_06', 6)	# 1842-1847
    sprite('rc610_07', 6)	# 1848-1853	 **attackbox here**
    sprite('rc610_08', 6)	# 1854-1859	 **attackbox here**
    sprite('rc610_09', 6)	# 1860-1865	 **attackbox here**
    sprite('rc610_10', 6)	# 1866-1871	 **attackbox here**
    sprite('rc610_11', 6)	# 1872-1877	 **attackbox here**
    sprite('rc610_12', 6)	# 1878-1883	 **attackbox here**
    sprite('rc610_13', 6)	# 1884-1889	 **attackbox here**
    SFX_1('brc701rrb')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 1890-1895	 **attackbox here**
    sprite('rc610_15', 6)	# 1896-1901	 **attackbox here**
    sprite('rc610_16', 6)	# 1902-1907	 **attackbox here**
    sprite('rc610_17', 6)	# 1908-1913	 **attackbox here**
    sprite('rc610_18', 6)	# 1914-1919	 **attackbox here**
    sprite('rc610_19', 6)	# 1920-1925	 **attackbox here**
    sprite('rc610_20', 6)	# 1926-1931	 **attackbox here**
    sprite('rc610_21', 6)	# 1932-1937	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1938-1943	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1944-1949	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1950-1955	 **attackbox here**
    sprite('rc610_21add04', 6)	# 1956-1961	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1962-1967	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1968-1973	 **attackbox here**
    sprite('rc610_21add01', 6)	# 1974-1979	 **attackbox here**
    sprite('rc610_21', 6)	# 1980-1985	 **attackbox here**
    Unknown23018(1)
    label(153)
    sprite('rc610_21add01', 6)	# 1986-1991	 **attackbox here**
    sprite('rc610_21add02', 6)	# 1992-1997	 **attackbox here**
    sprite('rc610_21add03', 6)	# 1998-2003	 **attackbox here**
    sprite('rc610_21add04', 6)	# 2004-2009	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2010-2015	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2016-2021	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2022-2027	 **attackbox here**
    sprite('rc610_21', 6)	# 2028-2033	 **attackbox here**
    gotoLabel(153)
    label(160)
    sprite('rc000_00', 1)	# 2034-2034
    if (not SLOT_158):
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('rc000_00', 7)	# 2035-2041
    sprite('rc000_01', 7)	# 2042-2048
    sprite('rc000_02', 7)	# 2049-2055
    sprite('rc000_03', 7)	# 2056-2062
    sprite('rc000_04', 7)	# 2063-2069
    sprite('rc000_05', 7)	# 2070-2076
    sprite('rc000_06', 7)	# 2077-2083
    sprite('rc000_07', 7)	# 2084-2090
    sprite('rc000_08', 7)	# 2091-2097
    gotoLabel(161)
    label(162)
    sprite('rc610_00', 6)	# 2098-2103
    sprite('rc610_01', 6)	# 2104-2109
    sprite('rc610_02', 6)	# 2110-2115
    sprite('rc610_03', 6)	# 2116-2121
    sprite('rc610_04', 6)	# 2122-2127
    sprite('rc610_05', 6)	# 2128-2133
    sprite('rc610_06', 6)	# 2134-2139
    sprite('rc610_07', 6)	# 2140-2145	 **attackbox here**
    sprite('rc610_08', 6)	# 2146-2151	 **attackbox here**
    sprite('rc610_09', 6)	# 2152-2157	 **attackbox here**
    sprite('rc610_10', 6)	# 2158-2163	 **attackbox here**
    sprite('rc610_11', 6)	# 2164-2169	 **attackbox here**
    sprite('rc610_12', 6)	# 2170-2175	 **attackbox here**
    sprite('rc610_13', 6)	# 2176-2181	 **attackbox here**
    SFX_1('brc701uva')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 2182-2187	 **attackbox here**
    sprite('rc610_15', 6)	# 2188-2193	 **attackbox here**
    sprite('rc610_16', 6)	# 2194-2199	 **attackbox here**
    sprite('rc610_17', 6)	# 2200-2205	 **attackbox here**
    sprite('rc610_18', 6)	# 2206-2211	 **attackbox here**
    sprite('rc610_19', 6)	# 2212-2217	 **attackbox here**
    sprite('rc610_20', 6)	# 2218-2223	 **attackbox here**
    sprite('rc610_21', 6)	# 2224-2229	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2230-2235	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2236-2241	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2242-2247	 **attackbox here**
    sprite('rc610_21add04', 6)	# 2248-2253	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2254-2259	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2260-2265	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2266-2271	 **attackbox here**
    sprite('rc610_21', 6)	# 2272-2277	 **attackbox here**
    Unknown23018(1)
    label(163)
    sprite('rc610_21add01', 6)	# 2278-2283	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2284-2289	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2290-2295	 **attackbox here**
    sprite('rc610_21add04', 6)	# 2296-2301	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2302-2307	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2308-2313	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2314-2319	 **attackbox here**
    sprite('rc610_21', 6)	# 2320-2325	 **attackbox here**
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('rc000_00', 1)	# 2326-2326
    if (not SLOT_158):
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('rc000_00', 7)	# 2327-2333
    sprite('rc000_01', 7)	# 2334-2340
    sprite('rc000_02', 7)	# 2341-2347
    sprite('rc000_03', 7)	# 2348-2354
    sprite('rc000_04', 7)	# 2355-2361
    sprite('rc000_05', 7)	# 2362-2368
    sprite('rc000_06', 7)	# 2369-2375
    sprite('rc000_07', 7)	# 2376-2382
    sprite('rc000_08', 7)	# 2383-2389
    gotoLabel(171)
    label(172)
    sprite('rc610_00', 6)	# 2390-2395
    sprite('rc610_01', 6)	# 2396-2401
    sprite('rc610_02', 6)	# 2402-2407
    sprite('rc610_03', 6)	# 2408-2413
    sprite('rc610_04', 6)	# 2414-2419
    sprite('rc610_05', 6)	# 2420-2425
    sprite('rc610_06', 6)	# 2426-2431
    sprite('rc610_07', 6)	# 2432-2437	 **attackbox here**
    sprite('rc610_08', 6)	# 2438-2443	 **attackbox here**
    sprite('rc610_09', 6)	# 2444-2449	 **attackbox here**
    sprite('rc610_10', 6)	# 2450-2455	 **attackbox here**
    sprite('rc610_11', 6)	# 2456-2461	 **attackbox here**
    sprite('rc610_12', 6)	# 2462-2467	 **attackbox here**
    sprite('rc610_13', 6)	# 2468-2473	 **attackbox here**
    SFX_1('brc703umi')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 2474-2479	 **attackbox here**
    sprite('rc610_15', 6)	# 2480-2485	 **attackbox here**
    sprite('rc610_16', 6)	# 2486-2491	 **attackbox here**
    sprite('rc610_17', 6)	# 2492-2497	 **attackbox here**
    sprite('rc610_18', 6)	# 2498-2503	 **attackbox here**
    sprite('rc610_19', 6)	# 2504-2509	 **attackbox here**
    sprite('rc610_20', 6)	# 2510-2515	 **attackbox here**
    sprite('rc610_21', 6)	# 2516-2521	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2522-2527	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2528-2533	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2534-2539	 **attackbox here**
    sprite('rc610_21add04', 6)	# 2540-2545	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2546-2551	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2552-2557	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2558-2563	 **attackbox here**
    sprite('rc610_21', 6)	# 2564-2569	 **attackbox here**
    Unknown23018(1)
    label(173)
    sprite('rc610_21add01', 6)	# 2570-2575	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2576-2581	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2582-2587	 **attackbox here**
    sprite('rc610_21add04', 6)	# 2588-2593	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2594-2599	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2600-2605	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2606-2611	 **attackbox here**
    sprite('rc610_21', 6)	# 2612-2617	 **attackbox here**
    loopRest()
    gotoLabel(173)
    label(180)
    sprite('rc000_00', 1)	# 2618-2618
    if (not SLOT_158):
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('rc000_00', 7)	# 2619-2625
    sprite('rc000_01', 7)	# 2626-2632
    sprite('rc000_02', 7)	# 2633-2639
    sprite('rc000_03', 7)	# 2640-2646
    sprite('rc000_04', 7)	# 2647-2653
    sprite('rc000_05', 7)	# 2654-2660
    sprite('rc000_06', 7)	# 2661-2667
    sprite('rc000_07', 7)	# 2668-2674
    sprite('rc000_08', 7)	# 2675-2681
    gotoLabel(181)
    label(182)
    sprite('rc610_00', 6)	# 2682-2687
    sprite('rc610_01', 6)	# 2688-2693
    sprite('rc610_02', 6)	# 2694-2699
    sprite('rc610_03', 6)	# 2700-2705
    sprite('rc610_04', 6)	# 2706-2711
    sprite('rc610_05', 6)	# 2712-2717
    sprite('rc610_06', 6)	# 2718-2723
    sprite('rc610_07', 6)	# 2724-2729	 **attackbox here**
    sprite('rc610_08', 6)	# 2730-2735	 **attackbox here**
    sprite('rc610_09', 6)	# 2736-2741	 **attackbox here**
    sprite('rc610_10', 6)	# 2742-2747	 **attackbox here**
    sprite('rc610_11', 6)	# 2748-2753	 **attackbox here**
    sprite('rc610_12', 6)	# 2754-2759	 **attackbox here**
    sprite('rc610_13', 6)	# 2760-2765	 **attackbox here**
    SFX_1('brc701pmi')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 2766-2771	 **attackbox here**
    sprite('rc610_15', 6)	# 2772-2777	 **attackbox here**
    sprite('rc610_16', 6)	# 2778-2783	 **attackbox here**
    sprite('rc610_17', 6)	# 2784-2789	 **attackbox here**
    sprite('rc610_18', 6)	# 2790-2795	 **attackbox here**
    sprite('rc610_19', 6)	# 2796-2801	 **attackbox here**
    sprite('rc610_20', 6)	# 2802-2807	 **attackbox here**
    sprite('rc610_21', 6)	# 2808-2813	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2814-2819	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2820-2825	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2826-2831	 **attackbox here**
    sprite('rc610_21add04', 6)	# 2832-2837	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2838-2843	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2844-2849	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2850-2855	 **attackbox here**
    sprite('rc610_21', 6)	# 2856-2861	 **attackbox here**
    Unknown23018(1)
    label(183)
    sprite('rc610_21add01', 6)	# 2862-2867	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2868-2873	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2874-2879	 **attackbox here**
    sprite('rc610_21add04', 6)	# 2880-2885	 **attackbox here**
    sprite('rc610_21add03', 6)	# 2886-2891	 **attackbox here**
    sprite('rc610_21add02', 6)	# 2892-2897	 **attackbox here**
    sprite('rc610_21add01', 6)	# 2898-2903	 **attackbox here**
    sprite('rc610_21', 6)	# 2904-2909	 **attackbox here**
    gotoLabel(183)
    label(190)
    sprite('rc610_00', 6)	# 2910-2915
    if (not SLOT_158):
        Unknown2019(1000)
    sprite('rc610_01', 6)	# 2916-2921
    sprite('rc610_02', 6)	# 2922-2927
    sprite('rc610_03', 6)	# 2928-2933
    sprite('rc610_04', 6)	# 2934-2939
    sprite('rc610_05', 6)	# 2940-2945
    sprite('rc610_06', 6)	# 2946-2951
    sprite('rc610_07', 6)	# 2952-2957	 **attackbox here**
    sprite('rc610_08', 6)	# 2958-2963	 **attackbox here**
    sprite('rc610_09', 6)	# 2964-2969	 **attackbox here**
    sprite('rc610_10', 6)	# 2970-2975	 **attackbox here**
    sprite('rc610_11', 6)	# 2976-2981	 **attackbox here**
    sprite('rc610_12', 6)	# 2982-2987	 **attackbox here**
    sprite('rc610_13', 6)	# 2988-2993	 **attackbox here**
    SFX_1('brc700bph')
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 2994-2999	 **attackbox here**
    sprite('rc610_15', 6)	# 3000-3005	 **attackbox here**
    sprite('rc610_16', 6)	# 3006-3011	 **attackbox here**
    sprite('rc610_17', 6)	# 3012-3017	 **attackbox here**
    sprite('rc610_18', 6)	# 3018-3023	 **attackbox here**
    sprite('rc610_19', 6)	# 3024-3029	 **attackbox here**
    sprite('rc610_20', 6)	# 3030-3035	 **attackbox here**
    sprite('rc610_21', 6)	# 3036-3041	 **attackbox here**
    sprite('rc610_21add01', 6)	# 3042-3047	 **attackbox here**
    sprite('rc610_21add02', 6)	# 3048-3053	 **attackbox here**
    sprite('rc610_21add03', 6)	# 3054-3059	 **attackbox here**
    sprite('rc610_21add04', 6)	# 3060-3065	 **attackbox here**
    sprite('rc610_21add03', 6)	# 3066-3071	 **attackbox here**
    sprite('rc610_21add02', 6)	# 3072-3077	 **attackbox here**
    sprite('rc610_21add01', 6)	# 3078-3083	 **attackbox here**
    sprite('rc610_21', 6)	# 3084-3089	 **attackbox here**
    Unknown2037(1)
    Unknown21011(330)
    label(191)
    sprite('rc610_21add01', 6)	# 3090-3095	 **attackbox here**
    sprite('rc610_21add02', 6)	# 3096-3101	 **attackbox here**
    sprite('rc610_21add03', 6)	# 3102-3107	 **attackbox here**
    sprite('rc610_21add04', 6)	# 3108-3113	 **attackbox here**
    sprite('rc610_21add03', 6)	# 3114-3119	 **attackbox here**
    sprite('rc610_21add02', 6)	# 3120-3125	 **attackbox here**
    if (not SLOT_2):
        Unknown21007(24, 40)
    sprite('rc610_21add01', 6)	# 3126-3131	 **attackbox here**
    sprite('rc610_21', 6)	# 3132-3137	 **attackbox here**
    Unknown2038(-1)
    gotoLabel(191)
    label(1000)
    sprite('rc001_00', 5)	# 3138-3142
    sprite('rc001_01', 5)	# 3143-3147
    sprite('rc001_02', 5)	# 3148-3152
    sprite('rc001_03', 5)	# 3153-3157
    sprite('rc001_04', 5)	# 3158-3162
    sprite('rc001_05', 5)	# 3163-3167
    sprite('rc001_06', 5)	# 3168-3172
    sprite('rc001_07', 5)	# 3173-3177
    sprite('rc001_08', 5)	# 3178-3182
    sprite('rc001_09', 16)	# 3183-3198
    sprite('rc001_10', 5)	# 3199-3203
    sprite('rc001_11', 5)	# 3204-3208
    sprite('rc001_12', 2)	# 3209-3210
    sprite('rc406_00', 3)	# 3211-3213

    def upon_STATE_END():
        Unknown2019(0)
        Unknown3001(255)
        Unknown3004(0)
    GFX_1('haef_event_lose_end', 0)
    sprite('rc406_01', 3)	# 3214-3216
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc406_02', 3)	# 3217-3219
    sprite('rc406_03', 3)	# 3220-3222
    Unknown3004(-12)
    sprite('rc406_04', 4)	# 3223-3226
    SFX_0('022_magiccircle_b')
    SFX_0('019_cloth_a')
    sprite('rc406_05', 4)	# 3227-3230
    sprite('rc406_06', 4)	# 3231-3234
    sprite('rc406_07', 4)	# 3235-3238
    sprite('rc406_08', 5)	# 3239-3243

@State
def CmnActLose():
    sprite('rc620_00', 6)	# 1-6
    sprite('rc620_01', 6)	# 7-12
    sprite('rc620_02', 6)	# 13-18
    sprite('rc620_03', 6)	# 19-24
    if SLOT_158:
        Unknown7006('brc405_0', 100, 878932578, 828323120, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    SFX_3('rcse_00')
    Unknown8000(0, 1, 0)
    Unknown23018(1)
    sprite('rc620_04', 6)	# 25-30
    sprite('rc620_05', 6)	# 31-36
    sprite('rc620_06', 6)	# 37-42
    sprite('rc620_07', 8)	# 43-50
    GFX_0('rc620nago', -1)
    sprite('rc620_08', 8)	# 51-58
    SFX_3('rcse_00')
    sprite('rc620_09', 8)	# 59-66
    sprite('rc620_10', 8)	# 67-74
    label(9)
    sprite('rc620_07', 8)	# 75-82
    sprite('rc620_08', 8)	# 83-90
    sprite('rc620_09', 8)	# 91-98
    sprite('rc620_10', 8)	# 99-106
    loopRest()
    gotoLabel(9)

@State
def EventDefEntryWait():
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryWaitReverse():

    def upon_IMMEDIATE():
        Unknown2005()
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
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
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def EventDefLose():
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def EventFingerSnap():
    sprite('keep', 1)	# 1-1
    SFX_3('rcse_26')
    loopRest()
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('rc602_00', 32767)	# 1-32767
    Unknown3038(1)
    loopRest()

@State
def EventEntryTeaWait():
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    sprite('rc600_00', 32767)	# 1-32767	 **attackbox here**

@State
def EventEntryTeaLoop():
    sprite('rc600_00', 10)	# 1-10	 **attackbox here**
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    sprite('rc600_01', 10)	# 11-20	 **attackbox here**
    sprite('rc600_02', 10)	# 21-30	 **attackbox here**
    sprite('rc600_03', 30)	# 31-60	 **attackbox here**
    sprite('rc600_03add01', 10)	# 61-70	 **attackbox here**
    sprite('rc600_04', 8)	# 71-78	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 79-86	 **attackbox here**
    sprite('rc600_05add01', 32767)	# 87-32853	 **attackbox here**

@State
def EventEntryTeaToStand():
    sprite('rc600_06', 8)	# 1-8	 **attackbox here**
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 9-16	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 17-22	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 23-28	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 29-34	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 35-40	 **attackbox here**
    sprite('rc600_12', 6)	# 41-46	 **attackbox here**
    sprite('rc600_13', 6)	# 47-52	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 53-58	 **attackbox here**
    sprite('rc600_15', 6)	# 59-64	 **attackbox here**
    sprite('rc600_16', 6)	# 65-70	 **attackbox here**
    sprite('rc600_17', 6)	# 71-76	 **attackbox here**
    sprite('rc600_18', 6)	# 77-82	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 83-88	 **attackbox here**
    sprite('rc600_20', 6)	# 89-94	 **attackbox here**
    sprite('rc600_21', 6)	# 95-100	 **attackbox here**
    sprite('rc600_22', 6)	# 101-106	 **attackbox here**
    sprite('rc600_23', 6)	# 107-112	 **attackbox here**
    sprite('rc600_24', 6)	# 113-118	 **attackbox here**
    sprite('rc600_25', 6)	# 119-124	 **attackbox here**
    sprite('rc600_26', 6)	# 125-130	 **attackbox here**
    loopRest()
    enterState('CmnActStand')

@State
def EventRCFlyEntryWait():
    sprite('rc602_00', 6)	# 1-6
    teleportRelativeY(720000)
    loopRest()

@State
def EventStamp():
    sprite('rc211_00', 32767)	# 1-32767
    Unknown1000(-40000)
    loopRest()

@State
def EventRCFlyEntry():
    teleportRelativeY(720000)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('rc602_00', 6)	# 1-6
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 7-12
    sprite('rc602_02', 6)	# 13-18
    sprite('rc602_03', 6)	# 19-24
    sprite('rc602_04', 6)	# 25-30
    sprite('rc602_00', 6)	# 31-36
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 37-42
    sprite('rc602_02', 6)	# 43-48
    sprite('rc602_03', 6)	# 49-54
    sprite('rc602_04', 6)	# 55-60
    sprite('rc602_00', 6)	# 61-66
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 67-72
    sprite('rc602_02', 6)	# 73-78
    sprite('rc602_03', 6)	# 79-84
    sprite('rc602_04', 6)	# 85-90
    sprite('rc602_00', 6)	# 91-96
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 97-102
    sprite('rc602_02', 6)	# 103-108
    sprite('rc602_03', 6)	# 109-114
    sprite('rc602_04', 6)	# 115-120
    sprite('rc602_05', 6)	# 121-126
    sprite('rc602_06', 6)	# 127-132
    Unknown1000(-260000)
    setGravity(-46)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(0)
    sprite('rc602_07', 5)	# 133-137
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 138-142
    sprite('rc602_09', 5)	# 143-147
    sprite('rc602_10', 5)	# 148-152
    sprite('rc602_11', 5)	# 153-157
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc602_12', 5)	# 158-162
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 163-167
    sprite('rc602_14', 5)	# 168-172
    sprite('rc602_15', 5)	# 173-177
    sprite('rc602_16', 5)	# 178-182
    sprite('rc602_18', 7)	# 183-189
    sprite('rc602_19', 5)	# 190-194
    sprite('rc602_20', 5)	# 195-199
    sprite('rc602_21', 5)	# 200-204
    loopRest()
    enterState('CmnActStand')

@State
def EventRCExcite():
    sprite('rc300_00', 6)	# 1-6
    GFX_0('BatSummons', 0)
    sprite('rc300_01', 6)	# 7-12
    sprite('rc300_02', 6)	# 13-18
    sprite('rc300_03', 6)	# 19-24
    loopRest()
    sprite('rc300_09', 7)	# 25-31
    sprite('rc300_10', 7)	# 32-38
    SFX_3('rcse_00')
    sprite('rc300_11', 7)	# 39-45
    sprite('rc300_12', 7)	# 46-52
    sprite('rc300_13', 7)	# 53-59
    sprite('rc300_14', 6)	# 60-65
    sprite('rc300_15', 6)	# 66-71
    sprite('rc300_16', 6)	# 72-77
    sprite('rc300_17', 6)	# 78-83
    loopRest()
    enterState('CmnActStand')

@State
def EventRCStandCenter():
    Unknown1000(-130000)
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def EventWarpout():
    sprite('rc611_00', 6)	# 1-6
    sprite('rc611_01', 6)	# 7-12
    sprite('rc611_02', 6)	# 13-18
    sprite('rc611_03', 6)	# 19-24
    SFX_0('019_cloth_b')
    sprite('rc611_04', 6)	# 25-30
    sprite('rc611_05', 14)	# 31-44
    sprite('rc611_06', 6)	# 45-50
    sprite('rc611_07', 6)	# 51-56
    sprite('rc611_08', 6)	# 57-62
    sprite('rc611_08ex01', 6)	# 63-68
    sprite('rc611_08ex02', 6)	# 69-74
    GFX_0('BatDelete', 0)
    sprite('rc611_09', 3)	# 75-77
    Unknown3010(-8)
    Unknown3016(-8)
    Unknown3022(-8)
    sprite('rc611_10', 1)	# 78-78
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 79-79
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 80-80
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 81-81
    SFX_0('019_cloth_c')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 82-82
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 83-83
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 84-84
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 85-85
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 86-86
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 87-87
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 88-88
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 89-89
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 90-90
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 91-91
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 92-92
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 93-93
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 94-94
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 95-95
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15ex01', 32767)	# 96-32862
    Unknown51(1)

@State
def EventNOVsRC_HavingTeaPrepare():
    sprite('rc600_05', 32767)	# 1-32767	 **attackbox here**
    loopRest()

@State
def EventNOVsRC_HavingTeaDrink():
    sprite('rc600_05', 10)	# 1-10	 **attackbox here**
    sprite('rc600_04', 10)	# 11-20	 **attackbox here**
    sprite('rc600_03', 30)	# 21-50	 **attackbox here**
    sprite('rc600_03add01', 10)	# 51-60	 **attackbox here**
    sprite('rc600_04', 8)	# 61-68	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 69-76	 **attackbox here**
    sprite('rc600_05add01', 30)	# 77-106	 **attackbox here**
    loopRest()
    enterState('EventNOVsRC_HavingTeaPrepare')

@State
def EventRCvsCAWin():
    label(0)
    sprite('rc010_05', 6)	# 1-6
    sprite('rc010_06', 6)	# 7-12
    sprite('rc010_07', 6)	# 13-18
    sprite('rc010_08', 6)	# 19-24
    sprite('rc010_09', 6)	# 25-30
    sprite('rc010_10', 6)	# 31-36
    sprite('rc010_11', 6)	# 37-42
    sprite('rc010_12', 6)	# 43-48
    sprite('rc010_13', 6)	# 49-54
    sprite('rc010_14', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def EventRCvsJNWin00():
    sprite('rc600_05', 32767)	# 1-32767	 **attackbox here**
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)

@State
def EventRCvsJNWin01():
    sprite('rc600_05', 8)	# 1-8	 **attackbox here**
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    sprite('rc600_04', 8)	# 9-16	 **attackbox here**
    sprite('rc600_03add01', 8)	# 17-24	 **attackbox here**
    sprite('rc600_00', 10)	# 25-34	 **attackbox here**
    sprite('rc600_01', 10)	# 35-44	 **attackbox here**
    sprite('rc600_02', 10)	# 45-54	 **attackbox here**
    sprite('rc600_03', 30)	# 55-84	 **attackbox here**
    sprite('rc600_03add01', 10)	# 85-94	 **attackbox here**
    sprite('rc600_04', 8)	# 95-102	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 103-110	 **attackbox here**
    sprite('rc600_05add01', 30)	# 111-140	 **attackbox here**
    sprite('rc600_06', 8)	# 141-148	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 149-156	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 157-162	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 163-168	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 169-174	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 175-180	 **attackbox here**
    sprite('rc600_12', 6)	# 181-186	 **attackbox here**
    sprite('rc600_13', 6)	# 187-192	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 193-198	 **attackbox here**
    sprite('rc600_15', 6)	# 199-204	 **attackbox here**
    sprite('rc600_16', 6)	# 205-210	 **attackbox here**
    sprite('rc600_17', 6)	# 211-216	 **attackbox here**
    sprite('rc600_18', 6)	# 217-222	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 223-228	 **attackbox here**
    sprite('rc600_20', 6)	# 229-234	 **attackbox here**
    sprite('rc600_21', 6)	# 235-240	 **attackbox here**
    sprite('rc600_22', 6)	# 241-246	 **attackbox here**
    sprite('rc600_23', 6)	# 247-252	 **attackbox here**
    sprite('rc600_24', 6)	# 253-258	 **attackbox here**
    sprite('rc600_25', 6)	# 259-264	 **attackbox here**
    sprite('rc600_26', 6)	# 265-270	 **attackbox here**
    enterState('CmnActStand')

@State
def EventLCvsRCLose00():
    sprite('rc611_00', 6)	# 1-6
    sprite('rc611_01', 6)	# 7-12
    sprite('rc611_02', 6)	# 13-18
    sprite('rc611_03', 6)	# 19-24
    SFX_0('019_cloth_b')
    sprite('rc611_04', 6)	# 25-30
    sprite('rc611_05', 14)	# 31-44
    sprite('rc611_06', 6)	# 45-50
    sprite('rc611_07', 6)	# 51-56
    sprite('rc611_08', 6)	# 57-62
    sprite('rc611_08ex01', 6)	# 63-68
    sprite('rc611_08ex02', 6)	# 69-74
    GFX_0('BatDelete', 0)
    sprite('rc611_09', 3)	# 75-77
    Unknown3010(-8)
    Unknown3016(-8)
    Unknown3022(-8)
    sprite('rc611_10', 1)	# 78-78
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 79-79
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 80-80
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 81-81
    SFX_0('019_cloth_c')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 82-82
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 83-83
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 84-84
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 85-85
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 86-86
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 87-87
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 88-88
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 89-89
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 90-90
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 91-91
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 92-92
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 93-93
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 94-94
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 95-95
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15ex01', 32767)	# 96-32862

@State
def EventNYvsRCEntry00():
    label(0)
    sprite('rc600_00', 5)	# 1-5	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def EventNYvsRCEntry01():
    sprite('rc600_00', 10)	# 1-10	 **attackbox here**
    sprite('rc600_01', 10)	# 11-20	 **attackbox here**
    sprite('rc600_02', 10)	# 21-30	 **attackbox here**
    sprite('rc600_03', 30)	# 31-60	 **attackbox here**
    sprite('rc600_03add01', 10)	# 61-70	 **attackbox here**
    sprite('rc600_04', 8)	# 71-78	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 79-86	 **attackbox here**
    sprite('rc600_05add01', 30)	# 87-116	 **attackbox here**
    sprite('rc600_06', 8)	# 117-124	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 125-132	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 133-138	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 139-144	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 145-150	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 151-156	 **attackbox here**
    sprite('rc600_12', 6)	# 157-162	 **attackbox here**
    sprite('rc600_13', 6)	# 163-168	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 169-174	 **attackbox here**
    sprite('rc600_15', 6)	# 175-180	 **attackbox here**
    sprite('rc600_16', 6)	# 181-186	 **attackbox here**
    sprite('rc600_17', 6)	# 187-192	 **attackbox here**
    sprite('rc600_18', 6)	# 193-198	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 199-204	 **attackbox here**
    sprite('rc600_20', 6)	# 205-210	 **attackbox here**
    sprite('rc600_21', 6)	# 211-216	 **attackbox here**
    sprite('rc600_22', 6)	# 217-222	 **attackbox here**
    sprite('rc600_23', 6)	# 223-228	 **attackbox here**
    sprite('rc600_24', 6)	# 229-234	 **attackbox here**
    sprite('rc600_25', 6)	# 235-240	 **attackbox here**
    sprite('rc600_26', 6)	# 241-246	 **attackbox here**
    enterState('CmnActStand')

@State
def EventCAvsRCEntry00():
    label(0)
    sprite('rc300_04', 32767)	# 1-32767
    Unknown3001(0)
    loopRest()
    gotoLabel(0)

@State
def EventCAvsRCEntry01():

    def upon_IMMEDIATE():
        Unknown3032()
    sprite('rc300_04', 60)	# 1-60
    Unknown3001(0)
    Unknown3004(0)
    sprite('rc300_04', 21)	# 61-81
    GFX_1('haef_event_lose_end', 0)
    Unknown3001(0)
    Unknown3004(5)
    sprite('rc300_04', 28)	# 82-109
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('000_airdash_0')
    sprite('rc300_04', 28)	# 110-137
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('000_airdash_0')
    sprite('rc300_04', 28)	# 138-165
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('000_airdash_0')
    sprite('rc300_04', 28)	# 166-193
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('000_airdash_0')
    sprite('rc300_04', 28)	# 194-221
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('000_airdash_0')
    sprite('rc300_15', 7)	# 222-228
    Unknown3004(0)
    Unknown3001(255)
    sprite('rc300_16', 7)	# 229-235
    sprite('rc300_17', 7)	# 236-242
    enterState('CmnActStand')

@State
def EventCAvsRCLoser00():
    label(0)
    sprite('rc010_05', 6)	# 1-6
    sprite('rc010_06', 6)	# 7-12
    sprite('rc010_07', 6)	# 13-18
    sprite('rc010_08', 6)	# 19-24
    sprite('rc010_09', 6)	# 25-30
    sprite('rc010_10', 6)	# 31-36
    sprite('rc010_11', 6)	# 37-42
    sprite('rc010_12', 6)	# 43-48
    sprite('rc010_13', 6)	# 49-54
    sprite('rc010_14', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def EventCAvsRCLoser01():
    sprite('rc010_04', 3)	# 1-3
    sprite('rc010_03', 3)	# 4-6
    sprite('rc010_02', 3)	# 7-9
    sprite('rc010_01', 3)	# 10-12
    sprite('rc010_00', 3)	# 13-15
    label(0)
    sprite('rc000_00', 7)	# 16-22
    sprite('rc000_01', 7)	# 23-29
    sprite('rc000_02', 7)	# 30-36
    sprite('rc000_03', 7)	# 37-43
    sprite('rc000_04', 7)	# 44-50
    sprite('rc000_05', 7)	# 51-57
    sprite('rc000_06', 7)	# 58-64
    sprite('rc000_07', 7)	# 65-71
    sprite('rc000_08', 7)	# 72-78
    loopRest()
    gotoLabel(0)

@State
def EventCAvsRCLoser02():
    sprite('rc611_00', 6)	# 1-6
    sprite('rc611_01', 6)	# 7-12
    sprite('rc611_02', 6)	# 13-18
    sprite('rc611_03', 6)	# 19-24
    SFX_0('019_cloth_b')
    sprite('rc611_04', 6)	# 25-30
    sprite('rc611_05', 14)	# 31-44
    sprite('rc611_06', 6)	# 45-50
    sprite('rc611_07', 6)	# 51-56
    sprite('rc611_08', 6)	# 57-62
    sprite('rc611_08ex01', 6)	# 63-68
    sprite('rc611_08ex02', 6)	# 69-74
    GFX_0('BatDelete', 0)
    sprite('rc611_09', 3)	# 75-77
    Unknown3010(-8)
    Unknown3016(-8)
    Unknown3022(-8)
    sprite('rc611_10', 1)	# 78-78
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 79-79
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_10', 1)	# 80-80
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 81-81
    SFX_0('019_cloth_c')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 82-82
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_11', 1)	# 83-83
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 84-84
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 85-85
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_12', 1)	# 86-86
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 87-87
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 88-88
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_13', 1)	# 89-89
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 90-90
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 91-91
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_14', 1)	# 92-92
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 93-93
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 94-94
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15', 1)	# 95-95
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    Unknown4045('726365665f6d6174636877696e000000000000000000000000000000000000006a000000')
    sprite('rc611_15ex01', 32767)	# 96-32862
    Unknown51(1)

@State
def EventRCvsRG01():
    sprite('rc411_00', 6)	# 1-6
    sprite('rc411_01', 6)	# 7-12
    label(0)
    sprite('rc411_02', 6)	# 13-18
    sprite('rc411_03', 6)	# 19-24
    sprite('rc411_04', 6)	# 25-30
    sprite('rc411_05', 6)	# 31-36
    gotoLabel(0)

@State
def EventRCvsRG01End():
    sprite('rc411_06', 6)	# 1-6
    sprite('rc411_07', 6)	# 7-12
    enterState('CmnActStand')

@State
def EventRCvsAM1():
    sprite('rc003_00', 3)	# 1-3
    Unknown2005()
    sprite('rc003_01', 3)	# 4-6
    sprite('rc003_02', 3)	# 7-9
    sprite('rc000_02', 6)	# 10-15
    sprite('rc000_03', 6)	# 16-21
    sprite('rc000_04', 6)	# 22-27
    sprite('rc000_05', 6)	# 28-33
    sprite('rc000_06', 6)	# 34-39
    sprite('rc000_07', 6)	# 40-45
    loopRelated(17, 160)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(0)
    sprite('rc030_00', 6)	# 46-51
    physicsXImpulse(800)
    label(10)
    sprite('rc030_01', 6)	# 52-57
    sprite('rc030_02', 6)	# 58-63
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_03', 6)	# 64-69
    sprite('rc030_04', 6)	# 70-75
    sprite('rc030_05', 6)	# 76-81
    sprite('rc030_06', 6)	# 82-87
    sprite('rc030_07', 6)	# 88-93
    sprite('rc030_08', 6)	# 94-99
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_09', 6)	# 100-105
    sprite('rc030_10', 6)	# 106-111
    gotoLabel(10)
    label(0)
    sprite('rc000_00', 6)	# 112-117
    physicsXImpulse(0)
    sprite('rc000_01', 6)	# 118-123
    sprite('rc000_02', 6)	# 124-129
    sprite('rc000_03', 6)	# 130-135
    sprite('rc000_04', 6)	# 136-141
    sprite('rc000_05', 6)	# 142-147
    sprite('rc000_06', 6)	# 148-153
    sprite('rc000_07', 6)	# 154-159
    sprite('rc000_08', 6)	# 160-165
    gotoLabel(0)

@State
def EventRCvsAM2():
    sprite('rc003_00', 3)	# 1-3
    Unknown2005()
    sprite('rc003_01', 3)	# 4-6
    sprite('rc003_02', 3)	# 7-9
    enterState('CmnActStand')

@State
def EventRCvsAM3():

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(3)
        elif (SLOT_22 > (-260000)):
            sendToLabel(3)
    sprite('rc030_00', 1)	# 1-1
    physicsXImpulse(2400)
    sprite('rc030_00', 4)	# 2-5
    label(2)
    sprite('rc030_01', 5)	# 6-10
    sprite('rc030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_03', 5)	# 16-20
    sprite('rc030_04', 5)	# 21-25
    sprite('rc030_05', 5)	# 26-30
    sprite('rc030_06', 5)	# 31-35
    sprite('rc030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_08', 5)	# 41-45
    sprite('rc030_09', 5)	# 46-50
    sprite('rc030_10', 5)	# 51-55
    loopRest()
    gotoLabel(2)
    label(3)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventEntryWalk():
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
    sprite('rc030_00', 1)	# 1-1
    physicsXImpulse(2400)
    sprite('rc030_00', 4)	# 2-5
    label(0)
    sprite('rc030_01', 5)	# 6-10
    sprite('rc030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_03', 5)	# 16-20
    sprite('rc030_04', 5)	# 21-25
    sprite('rc030_05', 5)	# 26-30
    sprite('rc030_06', 5)	# 31-35
    sprite('rc030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_08', 5)	# 41-45
    sprite('rc030_09', 5)	# 46-50
    sprite('rc030_10', 5)	# 51-55
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventRCVSNTWalk():
    sprite('rc000_00', 6)	# 1-6
    Unknown2037(1)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 > 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 < (-260000)):
            sendToLabel(1)
    sprite('rc031_00', 5)	# 7-11
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(-800)
    sprite('rc031_01', 5)	# 12-16
    label(0)
    sprite('rc031_02', 6)	# 17-22
    sprite('rc031_03', 6)	# 23-28
    sprite('rc031_04', 6)	# 29-34
    sprite('rc031_05', 6)	# 35-40
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventRCvsNTStand():
    Unknown1000(-200000)
    enterState('CmnActStand')

@State
def EventVsRCEntryWaitReverse():

    def upon_IMMEDIATE():
        Unknown1000(-352000)
    sprite('rc000_00', 7)	# 1-7
    Unknown2005()
    label(0)
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    sprite('rc000_00', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def EventCreateLifeLink():
    sprite('keep', 7)	# 1-7
    GFX_0('Fade1', 0)
    loopRest()
    enterState('CmnActStand')

@State
def EventAct2RGEntryWait():
    label(0)
    sprite('rc602_00', 6)	# 1-6
    teleportRelativeY(640000)
    Unknown3038(1)
    loopRest()
    gotoLabel(0)

@State
def EventAct2RGEntry():
    sprite('rc602_00', 6)	# 1-6
    sendToLabelUpon(2, 48)
    Unknown3038(0)
    setGravity(25)
    physicsYImpulse(-1200)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 7-12
    sprite('rc602_02', 6)	# 13-18
    sprite('rc602_03', 6)	# 19-24
    sprite('rc602_04', 6)	# 25-30
    sprite('rc602_00', 6)	# 31-36
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 37-42
    sprite('rc602_02', 6)	# 43-48
    sprite('rc602_03', 6)	# 49-54
    sprite('rc602_04', 6)	# 55-60
    sprite('rc602_00', 6)	# 61-66
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 67-72
    sprite('rc602_02', 6)	# 73-78
    sprite('rc602_03', 6)	# 79-84
    sprite('rc602_04', 6)	# 85-90
    sprite('rc602_00', 6)	# 91-96
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 97-102
    sprite('rc602_02', 6)	# 103-108
    sprite('rc602_03', 6)	# 109-114
    sprite('rc602_04', 6)	# 115-120
    sprite('rc602_05', 6)	# 121-126
    sprite('rc602_06', 6)	# 127-132
    Unknown1000(-260000)
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(47)
    sprite('rc602_07', 5)	# 133-137
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 138-142
    sprite('rc602_09', 5)	# 143-147
    sprite('rc602_10', 5)	# 148-152
    sprite('rc602_11', 5)	# 153-157
    loopRest()
    gotoLabel(47)
    label(48)
    sprite('rc602_12', 5)	# 158-162
    Unknown1043()
    physicsYImpulse(0)
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 163-167
    sprite('rc602_14', 5)	# 168-172
    sprite('rc602_15', 5)	# 173-177
    sprite('rc602_16', 5)	# 178-182
    sprite('rc602_18', 7)	# 183-189
    sprite('rc602_19', 5)	# 190-194
    sprite('rc602_20', 5)	# 195-199
    sprite('rc602_21', 5)	# 200-204
    Unknown21011(60)
    loopRest()
    enterState('CmnActStand')

@State
def EventBackWalk():
    sprite('rc031_00', 5)	# 1-5
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(-800)
    sprite('rc031_01', 5)	# 6-10
    sprite('rc031_02', 6)	# 11-16
    sprite('rc031_03', 6)	# 17-22
    sprite('rc031_04', 6)	# 23-28
    sprite('rc031_05', 6)	# 29-34
    sprite('rc031_02', 6)	# 35-40
    loopRest()
    physicsXImpulse(0)
    enterState('CmnActStand')

@State
def EventReverseStand():
    sprite('rc003_00', 3)	# 1-3
    Unknown2005()
    sprite('rc003_01', 3)	# 4-6
    sprite('rc003_02', 3)	# 7-9
    sprite('rc000_00', 7)	# 10-16
    label(0)
    sprite('rc000_01', 7)	# 17-23
    sprite('rc000_02', 7)	# 24-30
    sprite('rc000_03', 7)	# 31-37
    sprite('rc000_04', 7)	# 38-44
    sprite('rc000_05', 7)	# 45-51
    sprite('rc000_06', 7)	# 52-58
    sprite('rc000_07', 7)	# 59-65
    sprite('rc000_08', 7)	# 66-72
    sprite('rc000_00', 7)	# 73-79
    loopRest()
    gotoLabel(0)

@State
def EventShake():
    sprite('keep', 2)	# 1-2
    GFX_0('EventShakeObj', -1)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_FallEntry():

    def upon_IMMEDIATE():
        teleportRelativeY(640000)
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_FallEntryEnd():

    def upon_IMMEDIATE():
        setGravity(25)
        physicsYImpulse(-1200)

        def upon_LANDING():
            sendToLabel(0)
            Unknown1043()
            Unknown1084(1)
            Unknown1000(-260000)
    Unknown2037(4)
    label(8)
    sprite('rc602_00', 6)	# 1-6
    Unknown2038(-1)
    SFX_0('019_cloth_a')
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_01', 6)	# 7-12
    sprite('rc602_02', 6)	# 13-18
    sprite('rc602_03', 6)	# 19-24
    sprite('rc602_04', 6)	# 25-30
    loopRest()
    if SLOT_2:
        _gotolabel(8)
    sprite('rc602_05', 6)	# 31-36
    sprite('rc602_06', 6)	# 37-42
    Unknown1000(-260000)
    setGravity(-66)
    physicsYImpulse(-6400)
    physicsXImpulse(0)
    label(9)
    sprite('rc602_07', 5)	# 43-47
    SFX_0('019_cloth_a')
    sprite('rc602_08', 5)	# 48-52
    sprite('rc602_09', 5)	# 53-57
    sprite('rc602_10', 5)	# 58-62
    sprite('rc602_11', 5)	# 63-67
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('rc602_12', 5)	# 68-72
    SFX_0('200_walk_normal_0')
    Unknown8000(100, 1, 0)
    GFX_0('rcef_602EntryPtc', -1)
    sprite('rc602_13', 5)	# 73-77
    sprite('rc602_14', 5)	# 78-82
    sprite('rc602_15', 5)	# 83-87
    sprite('rc602_16', 5)	# 88-92
    sprite('rc602_18', 7)	# 93-99
    sprite('rc602_19', 5)	# 100-104
    sprite('rc602_20', 5)	# 105-109
    sprite('rc602_21', 5)	# 110-114
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Win():
    sprite('rc610_00', 6)	# 1-6
    sprite('rc610_01', 6)	# 7-12
    sprite('rc610_02', 6)	# 13-18
    sprite('rc610_03', 6)	# 19-24
    sprite('rc610_04', 6)	# 25-30
    sprite('rc610_05', 6)	# 31-36
    sprite('rc610_06', 6)	# 37-42
    sprite('rc610_07', 6)	# 43-48	 **attackbox here**
    sprite('rc610_08', 6)	# 49-54	 **attackbox here**
    sprite('rc610_09', 6)	# 55-60	 **attackbox here**
    sprite('rc610_10', 6)	# 61-66	 **attackbox here**
    sprite('rc610_11', 6)	# 67-72	 **attackbox here**
    sprite('rc610_12', 6)	# 73-78	 **attackbox here**
    sprite('rc610_13', 6)	# 79-84	 **attackbox here**
    SFX_0('019_cloth_c')
    sprite('rc610_14', 6)	# 85-90	 **attackbox here**
    sprite('rc610_15', 6)	# 91-96	 **attackbox here**
    sprite('rc610_16', 6)	# 97-102	 **attackbox here**
    sprite('rc610_17', 6)	# 103-108	 **attackbox here**
    sprite('rc610_18', 6)	# 109-114	 **attackbox here**
    sprite('rc610_19', 6)	# 115-120	 **attackbox here**
    sprite('rc610_20', 6)	# 121-126	 **attackbox here**
    sprite('rc610_21', 6)	# 127-132	 **attackbox here**
    label(0)
    sprite('rc610_21add01', 6)	# 133-138	 **attackbox here**
    sprite('rc610_21add02', 6)	# 139-144	 **attackbox here**
    sprite('rc610_21add03', 6)	# 145-150	 **attackbox here**
    sprite('rc610_21add04', 6)	# 151-156	 **attackbox here**
    sprite('rc610_21add03', 6)	# 157-162	 **attackbox here**
    sprite('rc610_21add02', 6)	# 163-168	 **attackbox here**
    sprite('rc610_21add01', 6)	# 169-174	 **attackbox here**
    sprite('rc610_21', 6)	# 175-180	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Reaction():
    sprite('rc001_00', 6)	# 1-6
    sprite('rc001_01', 6)	# 7-12
    sprite('rc001_02', 6)	# 13-18
    sprite('rc001_03', 6)	# 19-24
    sprite('rc001_04', 6)	# 25-30
    sprite('rc001_05', 6)	# 31-36
    sprite('rc001_06', 6)	# 37-42
    sprite('rc001_07', 6)	# 43-48
    sprite('rc001_08', 6)	# 49-54
    sprite('rc001_09', 6)	# 55-60
    sprite('rc001_10', 6)	# 61-66
    sprite('rc001_11', 6)	# 67-72
    sprite('rc001_12', 6)	# 73-78
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_cavsrc_00():
    sprite('rc010_00', 6)	# 1-6
    sprite('rc010_01', 6)	# 7-12
    sprite('rc010_02', 6)	# 13-18
    sprite('rc010_03', 6)	# 19-24
    sprite('rc010_04', 6)	# 25-30
    label(0)
    sprite('rc010_05', 8)	# 31-38
    sprite('rc010_06', 8)	# 39-46
    sprite('rc010_07', 8)	# 47-54
    sprite('rc010_08', 8)	# 55-62
    sprite('rc010_09', 8)	# 63-70
    sprite('rc010_10', 8)	# 71-78
    sprite('rc010_11', 8)	# 79-86
    sprite('rc010_12', 8)	# 87-94
    sprite('rc010_13', 8)	# 95-102
    sprite('rc010_14', 8)	# 103-110
    loopRest()
    gotoLabel(0)

@State
def Act2Event_cavsrc_01():
    sprite('rc011_00', 10)	# 1-10
    sprite('rc011_01', 10)	# 11-20
    sprite('rc011_02', 10)	# 21-30
    label(0)
    sprite('rc011_03', 10)	# 31-40
    sprite('rc011_04', 10)	# 41-50
    sprite('rc011_05', 10)	# 51-60
    sprite('rc011_06', 10)	# 61-70
    sprite('rc011_07', 10)	# 71-80
    gotoLabel(0)

@State
def Act2Event_cavsrc_02():
    sprite('rc011_02', 6)	# 1-6
    sprite('rc011_01', 6)	# 7-12
    sprite('rc011_00', 6)	# 13-18
    sprite('rc010_04', 6)	# 19-24
    sprite('rc010_03', 6)	# 25-30
    sprite('rc010_02', 6)	# 31-36
    sprite('rc010_01', 6)	# 37-42
    sprite('rc010_00', 6)	# 43-48
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_vhvsrc_00():

    def upon_IMMEDIATE():
        Unknown2019(-500)
    sprite('rc030_00', 4)	# 1-4
    physicsXImpulse(1000)
    label(0)
    sprite('rc030_01', 7)	# 5-11
    sprite('rc030_02', 7)	# 12-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc030_03', 7)	# 19-25
    sprite('rc030_04', 7)	# 26-32
    sprite('rc030_05', 7)	# 33-39
    sprite('rc030_06', 7)	# 40-46
    sprite('rc063_00', 3)	# 47-49	 **attackbox here**
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    setGravity(2000)
    sprite('rc063_01', 3)	# 50-52	 **attackbox here**
    sprite('rc063_02', 3)	# 53-55	 **attackbox here**
    sprite('rc063_03', 3)	# 56-58	 **attackbox here**
    sprite('rc063_04', 3)	# 59-61	 **attackbox here**
    sprite('rc063_05', 3)	# 62-64	 **attackbox here**
    sprite('rc063_06', 2)	# 65-66	 **attackbox here**
    GFX_0('nago_medama', 104)
    physicsXImpulse(0)
    physicsYImpulse(2000)
    setGravity(2000)
    SFX_0('209_down_normal_0')
    sprite('rc063_07', 2)	# 67-68	 **attackbox here**
    sprite('rc063_08', 3)	# 69-71	 **attackbox here**
    sprite('rc063_09', 3)	# 72-74	 **attackbox here**
    sprite('rc063_10', 3)	# 75-77	 **attackbox here**
    sprite('rc063_11', 4)	# 78-81	 **attackbox here**
    sprite('rc063_12', 4)	# 82-85	 **attackbox here**
    sprite('rc063_13', 32767)	# 86-32852	 **attackbox here**
    loopRest()

@State
def Act2Event_vhvsrc_01():
    sprite('rc064_00', 5)	# 1-5	 **attackbox here**
    sprite('rc064_01', 5)	# 6-10	 **attackbox here**
    sprite('rc064_02', 4)	# 11-14	 **attackbox here**
    sprite('rc064_03', 4)	# 15-18	 **attackbox here**
    sprite('rc064_04', 4)	# 19-22	 **attackbox here**
    sprite('rc064_05', 4)	# 23-26	 **attackbox here**
    sprite('rc064_06', 4)	# 27-30	 **attackbox here**
    sprite('rc064_07', 4)	# 31-34	 **attackbox here**
    sprite('rc064_08', 4)	# 35-38	 **attackbox here**
    sprite('rc064_09', 4)	# 39-42	 **attackbox here**
    sprite('rc064_10', 4)	# 43-46	 **attackbox here**
    sprite('rc064_11', 4)	# 47-50
    sprite('rc064_12', 4)	# 51-54
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_izvsrc_00_Loop():
    sprite('rc060_07', 4)	# 1-4	 **attackbox here**
    teleportRelativeX(260000)
    Unknown8003(100, 1, 0)
    SFX_0('104_guard_grap_1')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    ScreenShake(3000, 18000)
    Unknown1047(-30000)
    sprite('rc060_07', 4)	# 5-8	 **attackbox here**
    Unknown8003(100, 1, 1)
    sprite('rc060_07', 4)	# 9-12	 **attackbox here**
    Unknown8003(100, 1, 0)
    sprite('rc060_07', 4)	# 13-16	 **attackbox here**
    Unknown8003(100, 1, 0)
    sprite('rc060_12', 3)	# 17-19	 **attackbox here**
    Unknown8003(100, 1, 0)
    sprite('rc060_13', 3)	# 20-22	 **attackbox here**
    Unknown8003(100, 1, 0)
    sprite('rc060_14', 3)	# 23-25	 **attackbox here**
    Unknown8003(100, 1, 0)
    Unknown1084(1)
    label(0)
    sprite('rc060_15', 7)	# 26-32	 **attackbox here**
    sprite('rc060_16', 7)	# 33-39	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act2Event_izvsrc_00_End():
    sprite('rc061_00', 6)	# 1-6	 **attackbox here**
    sprite('rc061_01', 6)	# 7-12	 **attackbox here**
    sprite('rc061_02', 6)	# 13-18	 **attackbox here**
    sprite('rc061_03', 6)	# 19-24	 **attackbox here**
    sprite('rc061_04', 6)	# 25-30	 **attackbox here**
    GFX_1('rcef_pachinB', 0)
    SFX_3('rcse_26')
    sprite('rc061_05', 6)	# 31-36	 **attackbox here**
    sprite('rc061_06', 6)	# 37-42	 **attackbox here**
    sprite('rc061_07', 6)	# 43-48	 **attackbox here**
    sprite('rc061_08', 6)	# 49-54	 **attackbox here**
    sprite('rc061_09', 6)	# 55-60	 **attackbox here**
    sprite('rc061_10', 6)	# 61-66	 **attackbox here**
    sprite('rc061_11', 6)	# 67-72
    sprite('rc061_12', 6)	# 73-78
    sprite('rc061_13', 6)	# 79-84
    sprite('rc061_14', 6)	# 85-90
    sprite('rc061_15', 6)	# 91-96
    sprite('rc061_16', 6)	# 97-102
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_WalkScreenOut():
    Unknown2017(0)
    Unknown2034(0)
    Unknown2006()
    Unknown2005()
    SLOT_51 = 0
    sprite('rc030_00', 1)	# 1-1
    physicsXImpulse(2400)
    sprite('rc030_00', 4)	# 2-5
    label(0)
    sprite('rc030_01', 5)	# 6-10
    sprite('rc030_02', 5)	# 11-15
    if (SLOT_51 <= 4):
        Unknown8006(100, 0, 1)
    sprite('rc030_03', 5)	# 16-20
    sprite('rc030_04', 5)	# 21-25
    sprite('rc030_05', 5)	# 26-30
    sprite('rc030_06', 5)	# 31-35
    sprite('rc030_07', 5)	# 36-40
    if (SLOT_51 <= 4):
        Unknown8006(100, 0, 1)
    sprite('rc030_08', 5)	# 41-45
    sprite('rc030_09', 5)	# 46-50
    sprite('rc030_10', 5)	# 51-55
    loopRest()
    SLOT_51 = (SLOT_51 + 1)
    gotoLabel(0)

@State
def Act3Event_jnvsrc_00():
    sprite('rc406_00', 6)	# 1-6
    sprite('rc406_01', 6)	# 7-12
    sprite('rc406_02', 6)	# 13-18
    sprite('rc406_03', 32767)	# 19-32785
    loopRest()

@State
def Act3Event_jnvsrc_01():
    sprite('rc406_15', 6)	# 1-6
    sprite('rc406_16', 6)	# 7-12
    sprite('rc406_17', 6)	# 13-18
    sprite('rc406_18', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_CrouchLoop():
    label(0)
    sprite('rc010_05', 6)	# 1-6
    sprite('rc010_06', 6)	# 7-12
    sprite('rc010_07', 6)	# 13-18
    sprite('rc010_08', 6)	# 19-24
    sprite('rc010_09', 6)	# 25-30
    sprite('rc010_10', 6)	# 31-36
    sprite('rc010_11', 6)	# 37-42
    sprite('rc010_12', 6)	# 43-48
    sprite('rc010_13', 6)	# 49-54
    sprite('rc010_14', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def Act3Event_StandToCrouch():
    sprite('rc010_00', 3)	# 1-3
    sprite('rc010_01', 3)	# 4-6
    sprite('rc010_02', 3)	# 7-9
    sprite('rc010_03', 3)	# 10-12
    sprite('rc010_04', 3)	# 13-15
    loopRest()
    enterState('Act3Event_CrouchLoop')

@State
def Act3Event_CrouchToStand():
    sprite('rc010_04', 3)	# 1-3
    sprite('rc010_03', 3)	# 4-6
    sprite('rc010_02', 3)	# 7-9
    sprite('rc010_01', 3)	# 10-12
    sprite('rc010_00', 3)	# 13-15
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Lose():
    sprite('rc620_00', 6)	# 1-6
    sprite('rc620_01', 6)	# 7-12
    sprite('rc620_02', 6)	# 13-18
    sprite('rc620_03', 6)	# 19-24
    Unknown8000(0, 1, 0)
    sprite('rc620_04', 6)	# 25-30
    sprite('rc620_05', 6)	# 31-36
    sprite('rc620_06', 6)	# 37-42
    sprite('rc620_07', 8)	# 43-50
    GFX_0('rc620nago', -1)
    sprite('rc620_08', 8)	# 51-58
    sprite('rc620_09', 8)	# 59-66
    sprite('rc620_10', 8)	# 67-74
    label(9)
    sprite('rc620_07', 8)	# 75-82
    sprite('rc620_08', 8)	# 83-90
    sprite('rc620_09', 8)	# 91-98
    sprite('rc620_10', 8)	# 99-106
    loopRest()
    gotoLabel(9)

@State
def Act3Event_rcvsrg_00():

    def upon_IMMEDIATE():
        Unknown1000(-150000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rc033_00', 2)	# 64-65
    setGravity(800)
    physicsXImpulse(-7500)
    physicsYImpulse(8800)
    sprite('rc033_01', 2)	# 66-67
    sendToLabelUpon(2, 3)
    label(2)
    sprite('rc033_02', 3)	# 68-70
    sprite('rc033_03', 3)	# 71-73
    sprite('rc033_04', 3)	# 74-76
    sprite('rc033_05', 3)	# 77-79
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('rc033_06', 3)	# 80-82
    clearUponHandler(2)
    Unknown1084(1)
    sprite('rc033_07', 3)	# 83-85
    sprite('rc033_08', 3)	# 86-88
    sprite('rc033_09', 3)	# 89-91
    sprite('rc033_10', 3)	# 92-94
    sprite('rc033_11', 3)	# 95-97
    sprite('rc033_12', 3)	# 98-100
    sprite('rc033_13', 3)	# 101-103
    loopRest()
    enterState('Act2Event_vhvsrc_00')

@State
def Act3Event_ntvsrc_00():

    def upon_IMMEDIATE():
        if SLOT_38:

            def upon_32():
                callSubroutine('FuncWind6')
        else:

            def upon_32():
                callSubroutine('FuncWind4')
        AttackDefaults_StandingDD()
    label(0)
    sprite('rc000_00', 7)	# 1-7
    sprite('rc000_01', 7)	# 8-14
    sprite('rc000_02', 7)	# 15-21
    sprite('rc000_03', 7)	# 22-28
    sprite('rc000_04', 7)	# 29-35
    sprite('rc000_05', 7)	# 36-42
    sprite('rc000_06', 7)	# 43-49
    sprite('rc000_07', 7)	# 50-56
    sprite('rc000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ntvsrc_01():

    def upon_IMMEDIATE():
        Unknown2003(1)
        Unknown2017(0)
        AttackDefaults_StandingDD()
    sprite('rc450_00', 5)	# 1-5
    sprite('rc450_01', 5)	# 6-10
    sprite('rc450_02', 5)	# 11-15
    sprite('rc450_03', 5)	# 16-20
    sprite('rc450_04', 5)	# 21-25
    sprite('rc450_05', 5)	# 26-30
    sprite('rc450_06', 5)	# 31-35
    sprite('rc450_07', 5)	# 36-40
    sprite('rc450_08', 5)	# 41-45
    if SLOT_38:
        callSubroutine('FuncWind4')
    else:
        callSubroutine('FuncWind6')
    Unknown21007(22, 32)
    sprite('rc450_09', 5)	# 46-50
    sprite('rc450_10', 32767)	# 51-32817	 **attackbox here**

@State
def Act3Event_ntvsrc_02():
    sprite('rc450_11', 5)	# 1-5
    sprite('rc450_38', 5)	# 6-10
    sprite('rc450_39', 5)	# 11-15
    sprite('rc450_40', 5)	# 16-20
    sprite('rc450_41', 5)	# 21-25
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_StormLoop():
    sprite('rc432_00', 6)	# 1-6
    sprite('rc432_01', 6)	# 7-12
    sprite('rc432_02', 6)	# 13-18
    sprite('rc432_03', 6)	# 19-24
    sprite('rc432_04', 6)	# 25-30
    sprite('rc432_05', 6)	# 31-36
    sprite('rc432_06', 15)	# 37-51
    Unknown21007(11, 33)
    sprite('rc432_07', 6)	# 52-57
    Unknown21007(11, 34)
    sprite('rc432_08', 6)	# 58-63
    label(0)
    sprite('rc432_09', 6)	# 64-69
    sprite('rc432_10', 6)	# 70-75
    sprite('rc432_11', 6)	# 76-81
    loopRest()
    gotoLabel(0)

@State
def Act3Event_StormLoopEnd():
    label(1)
    sprite('rc432_12', 7)	# 1-7
    Unknown21007(11, 35)
    sprite('rc432_13', 7)	# 8-14
    sprite('rc432_14', 7)	# 15-21
    sprite('rc432_15', 7)	# 22-28
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ChouhatuLoop():
    sprite('rc300_00', 6)	# 1-6
    GFX_0('BatSummons', 0)
    sprite('rc300_01', 6)	# 7-12
    sprite('rc300_02', 6)	# 13-18
    sprite('rc300_03', 6)	# 19-24
    loopRest()
    label(0)
    sprite('rc300_04', 7)	# 25-31
    SFX_3('rcse_00')
    Unknown2038(1)
    sprite('rc300_05', 7)	# 32-38
    sprite('rc300_06', 7)	# 39-45
    sprite('rc300_07', 7)	# 46-52
    sprite('rc300_08', 7)	# 53-59
    sprite('rc300_09', 7)	# 60-66
    sprite('rc300_10', 7)	# 67-73
    SFX_3('rcse_00')
    sprite('rc300_11', 7)	# 74-80
    sprite('rc300_12', 7)	# 81-87
    sprite('rc300_13', 7)	# 88-94
    loopRest()
    (SLOT_2 <= 5)
    if SLOT_0:
        _gotolabel(0)
    label(1)
    sprite('rc300_04', 7)	# 95-101
    sprite('rc300_05', 7)	# 102-108
    sprite('rc300_06', 7)	# 109-115
    sprite('rc300_07', 7)	# 116-122
    sprite('rc300_08', 7)	# 123-129
    sprite('rc300_09', 7)	# 130-136
    sprite('rc300_10', 7)	# 137-143
    sprite('rc300_11', 7)	# 144-150
    sprite('rc300_12', 7)	# 151-157
    sprite('rc300_13', 7)	# 158-164
    loopRest()
    gotoLabel(1)

@State
def Act3Event_ChouhatuLoopEnd():
    sprite('rc300_14', 6)	# 1-6
    sprite('rc300_15', 6)	# 7-12
    sprite('rc300_16', 6)	# 13-18
    sprite('rc300_17', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_RCFlyEntryWait():
    sprite('rc602_00', 6)	# 1-6
    Unknown3038(1)
    teleportRelativeY(720000)
    loopRest()

@State
def Act3Event_EntryWalkWait():
    sprite('rc602_00', 6)	# 1-6
    Unknown3038(1)
    Unknown1000(-900000)
    loopRest()

@State
def Act3Event_nyvsrc_00():
    sprite('rc620_00', 6)	# 1-6
    sprite('rc620_01', 6)	# 7-12
    sprite('rc620_02', 6)	# 13-18
    sprite('rc620_03', 6)	# 19-24
    Unknown8000(0, 1, 0)
    sprite('rc620_04', 6)	# 25-30
    sprite('rc620_05', 6)	# 31-36
    sprite('rc620_06', 6)	# 37-42
    sprite('rc620_07', 8)	# 43-50
    GFX_0('rc620nago', -1)
    sprite('rc620_08', 8)	# 51-58
    sprite('rc620_09', 8)	# 59-66
    sprite('rc620_10', 8)	# 67-74
    label(9)
    sprite('rc620_07', 8)	# 75-82
    sprite('rc620_08', 8)	# 83-90
    sprite('rc620_09', 8)	# 91-98
    sprite('rc620_10', 8)	# 99-106
    loopRest()
    gotoLabel(9)

@State
def Act3Event_amvsrc_00():
    sprite('rc600_05', 32767)	# 1-32767	 **attackbox here**
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    loopRest()

@State
def Act3Event_amvsrc_01():
    sprite('rc600_05', 8)	# 1-8	 **attackbox here**
    GFX_0('rc600giPot', -1)
    Unknown38(9, 1)
    sprite('rc600_04', 8)	# 9-16	 **attackbox here**
    sprite('rc600_03add01', 8)	# 17-24	 **attackbox here**
    sprite('rc600_00', 10)	# 25-34	 **attackbox here**
    sprite('rc600_01', 10)	# 35-44	 **attackbox here**
    sprite('rc600_02', 10)	# 45-54	 **attackbox here**
    sprite('rc600_03', 30)	# 55-84	 **attackbox here**
    sprite('rc600_03add01', 10)	# 85-94	 **attackbox here**
    sprite('rc600_04', 8)	# 95-102	 **attackbox here**
    SFX_3('rcse_03')
    sprite('rc600_05', 8)	# 103-110	 **attackbox here**
    sprite('rc600_05add01', 30)	# 111-140	 **attackbox here**
    sprite('rc600_06', 8)	# 141-148	 **attackbox here**
    SFX_3('rcse_11')
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_07', 8)	# 149-156	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_08', 6)	# 157-162	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    Unknown13(9)
    sprite('rc600_09', 6)	# 163-168	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_10', 6)	# 169-174	 **attackbox here**
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    GFX_0('rcef_600rose', 106)
    sprite('rc600_11', 6)	# 175-180	 **attackbox here**
    sprite('rc600_12', 6)	# 181-186	 **attackbox here**
    sprite('rc600_13', 6)	# 187-192	 **attackbox here**
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rc600_14', 6)	# 193-198	 **attackbox here**
    sprite('rc600_15', 6)	# 199-204	 **attackbox here**
    sprite('rc600_16', 6)	# 205-210	 **attackbox here**
    sprite('rc600_17', 6)	# 211-216	 **attackbox here**
    sprite('rc600_18', 6)	# 217-222	 **attackbox here**
    SFX_0('019_cloth_b')
    sprite('rc600_19', 6)	# 223-228	 **attackbox here**
    sprite('rc600_20', 6)	# 229-234	 **attackbox here**
    sprite('rc600_21', 6)	# 235-240	 **attackbox here**
    sprite('rc600_22', 6)	# 241-246	 **attackbox here**
    sprite('rc600_23', 6)	# 247-252	 **attackbox here**
    sprite('rc600_24', 6)	# 253-258	 **attackbox here**
    sprite('rc600_25', 6)	# 259-264	 **attackbox here**
    sprite('rc600_26', 6)	# 265-270	 **attackbox here**
    loopRest()
    enterState('CmnActStand')