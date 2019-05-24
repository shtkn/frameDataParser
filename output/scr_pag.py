@Subroutine
def PreInit():
    Unknown12019('70616700000000000000000000000000')

@Subroutine
def MatchInit():
    DashFInitialVelocity(15000)
    DashFMaxVelocity(24000)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(3)
    Unknown13039(1)
    Unknown2049(1)
    Unknown23003(0, 1, 10, 4, 6000, 6000, -65536, -23296)
    Unknown23041(0, 1)
    Unknown23003(1, 0, 0, 1, 420, 420, -5242880, -24368)
    Move_Register('CancelOrgiaDash', INPUT_SPECIALMOVE)
    Move_Input_(0xda)
    Move_AirGround_(0x304d)
    Unknown14005(1)
    Unknown14013('OrgiaDash')
    Move_EndRegister()
    Move_Register('OrgiaDash', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Move_AirGround_(0x304d)
    Unknown14020(1)
    Unknown14004(1)
    Move_EndRegister()
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(2)
    Unknown14015(-34000, 446000, -85000, 175000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(3000, 413000, -66000, 283000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(-2000, 514000, 382000, 426000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15014(1)
    Unknown15012(1)
    Unknown14015(-2000, 514000, -15000, 426000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(2)
    Unknown14015(9000, 204000, -71000, 122000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(3000, 413000, -66000, 283000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x1)
    MoveMaxChainRepeat(1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th', 0x1)
    MoveMaxChainRepeat(1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14015(-2000, 514000, -15000, 426000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(6000, 213000, -100000, -20000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown15016(1, 15, 20)
    MoveMaxChainRepeat(1)
    Unknown15021(1500)
    Unknown14015(120000, 850000, 10000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15016(1, 15, 20)
    Unknown15021(2000)
    Unknown14015(80000, 500000, 200000, 600000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(20000, 430000, -219000, -66000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(50000, 400000, -100000, 0, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(-18000, 219000, -377000, 41000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5A_2nd', 0x10)
    Unknown14005(1)
    Unknown14015(22000, 247000, -36000, 188000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(59000, 375000, -234000, 468000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown15021(500)
    Unknown14015(146000, 446000, -562000, -192000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
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
    Move_Register('NmlAtk5AEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('NmlAtk5A')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk5BEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('NmlAtk5B')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk2BEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x45)
    Unknown14013('NmlAtk2B')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AN_CmnActCrushAttackEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('CmnActCrushAttack')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk2CEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x45)
    Unknown14013('NmlAtk2C')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtkThrowEX', 0x1)
    Move_Input_(0xd3)
    Unknown14005(1)
    Unknown14013('NmlAtkThrow')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtkBackThrowEX', 0x1)
    Move_Input_(0xd3)
    Unknown14005(1)
    Unknown14013('NmlAtkBackThrow')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('MachineGunA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(14000, 1800000, -54000, 68000, 250, 1)
    Move_EndRegister()
    Move_Register('MachineGunB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15016(1, 0, 36)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(14000, 1800000, -54000, 68000, 250, 1)
    Move_EndRegister()
    Move_Register('AirMachineGunA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(282000, 686000, -400000, 50000, 100, 1)
    Move_EndRegister()
    Move_Register('AirMachineGunB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(282000, 686000, -400000, 50000, 100, 1)
    Move_EndRegister()
    Move_Register('CannonA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(282000, 686000, -200000, 280000, 100, 1)
    Move_EndRegister()
    Move_Register('CannonB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(540000, 1194000, -200000, 280000, 100, 1)
    Move_EndRegister()
    Move_Register('AirCannonA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(282000, 686000, -200000, 280000, 100, 1)
    Move_EndRegister()
    Move_Register('AirCannonB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown14015(540000, 1194000, -200000, 280000, 100, 1)
    Move_EndRegister()
    Move_Register('MegidoFire', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown15013(2000)
    Unknown15012(1)
    Unknown14015(3000, 737000, -201000, 743000, 100, 25)
    Move_EndRegister()
    Move_Register('Pandora', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15013(1)
    Unknown15012(1000)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(-113000, 1739000, -375000, 460000, 50, 1)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-7000, 342000, -199000, 83000, 250, 0)
    Move_EndRegister()
    Move_Register('AthenaSurfing', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x300e)
    Unknown15013(3000)
    Unknown14015(2000, 1739000, -275000, 292000, 250, 0)
    Move_EndRegister()
    Move_Register('AthenaSurfingOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3083)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3081)
    Unknown15013(3000)
    Unknown14015(2000, 1739000, -275000, 292000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAirThrow', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15013(3000)
    Unknown15021(3000)
    Unknown14015(-113000, 450000, -375000, 460000, 250, 1)
    Move_EndRegister()
    Move_Register('UltimateAirThrowOD', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15010()
    Unknown15013(3000)
    Unknown15021(3000)
    Unknown14015(-113000, 450000, -375000, 460000, 250, 1)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(1)
    Unknown15012(1)
    Unknown15013(20000)
    Unknown15016(3, 73, 75)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 450000, -250000, 150000, 250, 0)
    Move_EndRegister()
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtk4A4th', 10000000)
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtkAIR5A', 'AN_NmlAtkAIR5A_2nd', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtk2C', 'OrgiaDash', 10000000)
    Unknown7010(0, 'pag000')
    Unknown7010(1, 'pag001')
    Unknown7010(2, 'pag002')
    Unknown7010(3, 'pag003')
    Unknown7010(4, 'pag004')
    Unknown7010(5, 'pag005')
    Unknown7010(6, 'pag006')
    Unknown7010(7, 'pag007')
    Unknown7010(8, 'pag008')
    Unknown7010(9, 'pag009')
    Unknown7010(10, 'pag010')
    Unknown7010(15, 'pag015')
    Unknown7010(16, 'pag016')
    Unknown7010(17, 'pag017')
    Unknown7010(18, 'pag018')
    Unknown7010(19, 'pag019')
    Unknown7010(20, 'pag020')
    Unknown7010(21, 'pag021')
    Unknown7010(22, 'pag022')
    Unknown7010(23, 'pag023')
    Unknown7010(24, 'pag024')
    Unknown7010(25, 'pag025')
    Unknown7010(28, 'pag028')
    Unknown7010(29, 'pag029')
    Unknown7010(30, 'pag030')
    Unknown7010(31, 'pag031')
    Unknown7010(32, 'pag032')
    Unknown7010(33, 'pag033')
    Unknown7010(34, 'pag034')
    Unknown7010(35, 'pag035')
    Unknown7010(36, 'pag036')
    Unknown7010(37, 'pag037')
    Unknown7010(39, 'pag039')
    Unknown7010(42, 'pag042')
    Unknown7010(43, 'pag043')
    Unknown7010(44, 'pag044')
    Unknown7010(45, 'pag045')
    Unknown7010(46, 'pag046')
    Unknown7010(47, 'pag047')
    Unknown7010(48, 'pag048')
    Unknown7010(49, 'pag049')
    Unknown7010(50, 'pag050')
    Unknown7010(52, 'pag052')
    Unknown7010(53, 'pag053')
    Unknown7010(54, 'pag100_0')
    Unknown7010(55, 'pag100_1')
    Unknown7010(56, 'pag100_2')
    Unknown7010(63, 'pag101_0')
    Unknown7010(64, 'pag101_1')
    Unknown7010(65, 'pag101_2')
    Unknown7010(57, 'pag102_0')
    Unknown7010(58, 'pag102_1')
    Unknown7010(59, 'pag102_2')
    Unknown7010(66, 'pag103_0')
    Unknown7010(67, 'pag103_1')
    Unknown7010(68, 'pag103_2')
    Unknown7010(60, 'pag104_0')
    Unknown7010(61, 'pag104_1')
    Unknown7010(62, 'pag104_2')
    Unknown7010(69, 'pag105_0')
    Unknown7010(70, 'pag105_1')
    Unknown7010(71, 'pag105_2')
    Unknown7010(72, 'pag150')
    Unknown7010(73, 'pag151')
    Unknown7010(74, 'pag152')
    Unknown7010(85, 'pag153')
    Unknown7010(87, 'pag154')
    Unknown7010(88, 'pag155')
    Unknown7010(96, 'pag161_0')
    Unknown7010(97, 'pag161_1')
    Unknown7010(92, 'pag162_0')
    Unknown7010(93, 'pag162_1')
    Unknown7010(98, 'pag163_0')
    Unknown7010(99, 'pag163_1')
    Unknown7010(100, 'pag164_0')
    Unknown7010(101, 'pag164_1')
    Unknown7010(105, 'pag165_0')
    Unknown7010(106, 'pag165_1')
    Unknown7010(102, 'pag166_0')
    Unknown7010(103, 'pag166_1')
    Unknown7010(90, 'pag167_0')
    Unknown7010(91, 'pag167_1')
    Unknown7010(107, 'pag168_0')
    Unknown7010(108, 'pag168_1')
    Unknown7010(110, 'pag169_0')
    Unknown7010(111, 'pag169_1')
    Unknown7010(94, 'pag400_0')
    Unknown7010(95, 'pag400_1')
    Unknown12018(0, 'ag060_00')
    Unknown12018(1, 'ag060_01')
    Unknown12018(2, 'ag060_02')
    Unknown12018(3, 'ag060_03')
    Unknown12018(4, 'ag060_04')
    Unknown12018(5, 'ag060_05')
    Unknown12018(6, 'ag060_06')
    Unknown12018(7, 'ag041_02')
    Unknown12018(8, 'ag040_02')
    Unknown12018(9, 'ag045_02')
    Unknown12018(10, 'ag060_00')
    Unknown12018(11, 'ag060_01')
    Unknown12018(12, 'ag060_03')
    Unknown12018(13, 'ag060_05')
    Unknown12018(14, 'ag060_07')
    Unknown12018(15, 'ag125_00')
    Unknown12018(16, 'ag050_00')
    Unknown12018(17, 'ag052_00')
    Unknown12018(18, 'ag054_00')
    Unknown12018(19, 'ag000_00')
    Unknown12018(20, 'ag000_00')
    Unknown12018(25, 'ag063_00')
    Unknown12018(26, 'ag063_01')
    Unknown12018(27, 'ag063_02')
    Unknown12018(28, 'ag063_05')
    Unknown12018(29, 'ag060_12')
    Unknown12018(24, 'ag072_03')
    GFX_0('PAG_PersonaCreate', -1)
    Unknown38(11, 1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000417468656e6153757266696e6700000000000000000000000000000000000000')
    Unknown12059('03000000417468656e6153757266696e674f440000000000000000000000000000000000')
    Unknown12059('04000000556c74696d6174654169725468726f7700000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174654169725468726f774f440000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    SLOT_64 = (SLOT_64 + 1)
    if (SLOT_64 >= 2):
        SLOT_64 = 0
    if (not SLOT_114):
        if SLOT_90:
            Unknown58('TRI_PAGModeChange', 2, 67)
            if SLOT_67:
                SLOT_31 = 6000
                SLOT_59 = 0
        if SLOT_59:
            if (not Unknown23148('CmnActTagBattleWait')):
                if (not SLOT_30):
                    if random_(2, 0, 50):
                        GFX_1('agef_overheat', 107)
            SLOT_32 = (SLOT_32 + (-1))
            if (not SLOT_32):
                SLOT_59 = 0
        else:
            SLOT_32 = 420
            if (not Unknown23148('OrgiaDash')):
                SLOT_31 = (SLOT_31 + 5)
            if (not SLOT_31):
                SLOT_59 = 1
                tag_voice(1, 'pag304_0', 'pag304_1', '', '')
    if SLOT_170:
        Unknown23008(0, 0)

@Subroutine
def Burner_Delete():
    Unknown26('agef_doublejump')
    Unknown26('agef_doublejump_back')
    Unknown26('agef_doublejump_flare')
    Unknown26('agef_doublejump_back_flare')
    Unknown26('agef_backstep')
    Unknown26('agef_backstep_back')
    Unknown26('agef_backstep_flare')
    Unknown26('agef_backstep_back_flare')
    Unknown26('agef_airbackdush')
    Unknown26('agef_airbackdush_back')
    Unknown26('agef_backstep_flare')
    Unknown26('agef_backstep_back_flare')
    Unknown26('agef202_burner_jump')
    Unknown26('agef202_burner_jump_back')
    Unknown26('agef202_argia_burner_jump')
    Unknown26('agef202_argia_burner_jump_back')
    Unknown26('agef202_burner')
    Unknown26('agef202_burner_back')
    Unknown26('agef202_orgia_burner')
    Unknown26('agef202_orgia_burner_back')
    Unknown26('agef_orgia_shotgun')
    Unknown26('agef_orgia_shotgun_back')
    Unknown26('agef_orgia_shotgun_burner')
    Unknown26('agef_orgia_shotgun_burner_back')
    Unknown26('agef_orgia_dash')
    Unknown26('agef_orgia_dash_back')
    Unknown26('agef_orgia_dash_back2')
    Unknown26('agef_orgia_dash_up')
    Unknown26('agef_orgia_dash_up_back')
    Unknown26('agef_orgia_dash_up_back2')
    Unknown26('agef_orgia_dash_down')
    Unknown26('agef_orgia_dash_down_back')
    Unknown26('agef_orgia_dash_down_back2')
    Unknown26('agef_orgia_backdash')
    Unknown26('agef_orgia_backdash_back')
    Unknown26('agef_orgia_hovering')
    Unknown26('agef_orgia_hovering_back')
    Unknown26('agef_orgia_hovering_back2')
    Unknown26('agef_missile_burner')
    Unknown26('agef_missile_burner_back')
    Unknown26('agef_aircanon_burner')
    Unknown26('agef_aircanon_burner_back')
    Unknown26('agef_aircanon_orgia_burner')
    Unknown26('agef_aircanon_orgia_burner_back')
    Unknown26('agef208_burner')
    Unknown26('agef208_burner_back')
    Unknown26('agef208_orgia_burner')
    Unknown26('agef208_orgia_burner_back')
    Unknown26('agef207_burner_turn')
    Unknown26('agef207_burner_turn_back')
    Unknown26('agef207_orgia_burner_turn')
    Unknown26('agef207_orgia_burner_turn_back')
    Unknown26('agef207_burner')
    Unknown26('agef207_burner_back')
    Unknown26('agef207_orgia_burner')
    Unknown26('agef207_orgia_burner_back')
    Unknown26('agef_surfing_burner_hold')
    Unknown26('agef_surfing_burner_hold_back')
    Unknown26('agef_surfing_orgia_hold')
    Unknown26('agef_surfing_orgia_hold_back')
    Unknown26('agef_surfing_burner')
    Unknown26('agef_surfing_burner_back')
    Unknown26('agef_surfing_orgia')
    Unknown26('agef_surfing_orgia_back')
    Unknown26('agef432_burner')
    Unknown26('agef432_burner_back')
    Unknown26('agef432_burner_3')
    Unknown26('agef432_orgia_burner')
    Unknown26('agef432_orgia_burner_back')
    Unknown26('agef432_orgia_burner_3')

@State
def CmnActStand():
    label(0)
    sprite('ag000_00', 6)	# 1-6
    sprite('ag000_01', 6)	# 7-12
    sprite('ag000_02', 6)	# 13-18
    sprite('ag000_03', 6)	# 19-24
    sprite('ag000_04', 6)	# 25-30
    sprite('ag000_05', 6)	# 31-36
    sprite('ag000_06', 6)	# 37-42
    sprite('ag000_07', 6)	# 43-48
    sprite('ag000_08', 6)	# 49-54
    sprite('ag000_09', 6)	# 55-60
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('ag001_00', 7)	# 61-67
    SLOT_88 = 960
    sprite('ag001_01', 18)	# 68-85
    sprite('ag001_02', 2)	# 86-87
    SFX_0('008_swing_pole_0')
    SFX_4('pag000')
    sprite('ag001_03', 2)	# 88-89
    sprite('ag001_04', 2)	# 90-91
    sprite('ag001_01', 2)	# 92-93
    SFX_0('008_swing_pole_0')
    sprite('ag001_02', 2)	# 94-95
    sprite('ag001_03', 2)	# 96-97
    sprite('ag001_04', 2)	# 98-99
    SFX_0('008_swing_pole_0')
    sprite('ag001_01', 2)	# 100-101
    sprite('ag001_02', 2)	# 102-103
    sprite('ag001_03', 2)	# 104-105
    SFX_0('008_swing_pole_0')
    sprite('ag001_04', 2)	# 106-107
    sprite('ag001_01', 2)	# 108-109
    sprite('ag001_02', 2)	# 110-111
    SFX_0('008_swing_pole_0')
    sprite('ag001_03', 2)	# 112-113
    sprite('ag001_04', 2)	# 114-115
    sprite('ag001_01', 2)	# 116-117
    SFX_0('008_swing_pole_0')
    sprite('ag001_02', 2)	# 118-119
    sprite('ag001_03', 2)	# 120-121
    sprite('ag001_04', 2)	# 122-123
    SFX_0('008_swing_pole_0')
    sprite('ag001_01', 2)	# 124-125
    sprite('ag001_02', 2)	# 126-127
    sprite('ag001_03', 2)	# 128-129
    SFX_0('008_swing_pole_0')
    sprite('ag001_04', 2)	# 130-131
    sprite('ag001_01', 2)	# 132-133
    sprite('ag001_02', 2)	# 134-135
    SFX_0('008_swing_pole_0')
    sprite('ag001_03', 2)	# 136-137
    sprite('ag001_04', 2)	# 138-139
    sprite('ag001_01', 2)	# 140-141
    SFX_0('008_swing_pole_0')
    sprite('ag001_02', 2)	# 142-143
    sprite('ag001_03', 2)	# 144-145
    sprite('ag001_04', 2)	# 146-147
    sprite('ag001_01', 15)	# 148-162
    sprite('ag001_00', 7)	# 163-169
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ag003_00', 4)	# 1-4
    sprite('ag003_01', 4)	# 5-8
    sprite('ag003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('ag010_00', 4)	# 1-4
    sprite('ag010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ag010_02', 6)	# 1-6
    sprite('ag010_03', 6)	# 7-12
    sprite('ag010_04', 6)	# 13-18
    sprite('ag010_05', 6)	# 19-24
    sprite('ag010_06', 6)	# 25-30
    sprite('ag010_07', 6)	# 31-36
    sprite('ag010_08', 6)	# 37-42
    sprite('ag010_09', 6)	# 43-48
    sprite('ag010_10', 6)	# 49-54
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ag013_00', 4)	# 1-4
    sprite('ag013_01', 4)	# 5-8
    sprite('ag013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('ag010_01', 4)	# 1-4
    sprite('ag010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ag010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    if (SLOT_23 > 1000):
        sendToLabel(1)
    label(0)
    sprite('ag020_00', 4)	# 1-4
    sprite('ag020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ag020_00', 4)	# 9-12
    GFX_0('agef_doublejump', 0)
    GFX_0('agef_doublejump_back', 1)
    GFX_0('agef_doublejump_flare', 0)
    GFX_0('agef_doublejump_back_flare', 1)
    sprite('ag020_01', 4)	# 13-16
    callSubroutine('Burner_Delete')
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpper():
    label(0)
    sprite('ag020_02', 2)	# 1-2
    sprite('ag020_03', 4)	# 3-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ag020_02', 4)	# 1-4
    sprite('ag020_03', 2)	# 5-6
    sprite('ag020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ag020_05', 4)	# 1-4
    sprite('ag020_06', 2)	# 5-6
    label(0)
    sprite('ag020_07', 4)	# 7-10
    sprite('ag020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ag010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('ag231_01', 2)	# 1-2
    sprite('ag231_00', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('ag231_01', 6)	# 1-6

@State
def CmnActFWalk():
    sprite('ag030_00', 5)	# 1-5
    sprite('ag030_01', 5)	# 6-10
    label(0)
    sprite('ag030_02', 5)	# 11-15
    sprite('ag030_03', 5)	# 16-20
    sprite('ag030_04', 5)	# 21-25
    sprite('ag030_05', 5)	# 26-30
    sprite('ag030_06', 5)	# 31-35
    sprite('ag030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ag030_08', 5)	# 41-45
    sprite('ag030_09', 5)	# 46-50
    sprite('ag030_10', 5)	# 51-55
    sprite('ag030_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)
    sprite('ag030_00', 3)	# 61-63

@State
def CmnActBWalk():
    sprite('ag031_00', 5)	# 1-5
    sprite('ag031_01', 5)	# 6-10
    label(0)
    sprite('ag031_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ag031_03', 5)	# 16-20
    sprite('ag031_04', 5)	# 21-25
    sprite('ag031_05', 5)	# 26-30
    sprite('ag031_06', 5)	# 31-35
    sprite('ag031_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ag031_08', 5)	# 41-45
    sprite('ag031_09', 5)	# 46-50
    sprite('ag031_10', 5)	# 51-55
    sprite('ag031_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)
    sprite('ag031_00', 3)	# 61-63

@State
def CmnActFDash():
    sprite('ag032_00', 4)	# 1-4
    label(0)
    sprite('ag032_01', 5)	# 5-9
    sprite('ag032_02', 5)	# 10-14
    Unknown8006(100, 1, 1)
    sprite('ag032_03', 5)	# 15-19
    sprite('ag032_04', 5)	# 20-24
    sprite('ag032_05', 5)	# 25-29
    sprite('ag032_06', 5)	# 30-34
    Unknown8006(100, 1, 1)
    sprite('ag032_07', 5)	# 35-39
    sprite('ag032_08', 5)	# 40-44
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():

    def upon_IMMEDIATE():
        Unknown13019(1)

        def upon_3():
            if (SLOT_18 == 4):
                Unknown13005(1)
                Unknown13001(1)
    sprite('ag032_09', 6)	# 1-6
    sprite('ag032_10', 6)	# 7-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincible(1)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('ag033_00', 2)	# 1-2
    sprite('ag033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    GFX_0('agef_backstep', 0)
    GFX_0('agef_backstep_back', 1)
    GFX_0('agef_backstep_flare', 0)
    GFX_0('agef_backstep_back_flare', 1)
    SFX_3('blaze_normal')
    sprite('ag033_02', 2)	# 6-7
    sprite('ag033_02', 1)	# 8-8
    setInvincible(0)
    sprite('ag033_01', 3)	# 9-11
    sprite('ag033_02', 3)	# 12-14
    label(0)
    sprite('ag033_01', 3)	# 15-17
    sprite('ag033_02', 3)	# 18-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ag033_03', 3)	# 21-23
    callSubroutine('Burner_Delete')
    setInvincible(0)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ag033_04', 3)	# 24-26

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirTurn():
    sprite('ag025_00', 1)	# 1-1
    sprite('ag025_01', 2)	# 2-3
    sprite('ag025_02', 1)	# 4-4

@State
def CmnActAirFDash():
    sprite('ag035_00', 3)	# 1-3
    sprite('ag035_01', 3)	# 4-6
    GFX_0('agef_airdush', 0)
    GFX_0('agef_airdush_back', 1)
    GFX_0('agef_airdush_flare', 0)
    GFX_0('agef_airdush_back_flare', 1)
    GFX_1('agef_airdush_sonicboom', 0)
    GFX_1('agef_airdush_back_sonicboom', 1)
    SFX_3('blaze_normal')
    sprite('ag035_02', 3)	# 7-9
    label(0)
    sprite('ag035_01', 3)	# 10-12
    sprite('ag035_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    sprite('ag035_00', 4)	# 16-19

@State
def CmnActAirBDash():
    sprite('ag033_01', 3)	# 1-3
    physicsYImpulse(12000)
    GFX_0('agef_airbackdush', 0)
    GFX_0('agef_airbackdush_back', 1)
    GFX_0('agef_backstep_flare', 0)
    GFX_0('agef_backstep_back_flare', 1)
    SFX_3('blaze_normal')
    sprite('ag033_02', 3)	# 4-6
    sprite('ag033_01', 3)	# 7-9
    sprite('ag033_02', 3)	# 10-12
    sprite('ag033_01', 3)	# 13-15
    sprite('ag033_02', 3)	# 16-18
    callSubroutine('Burner_Delete')
    sprite('ag033_01', 3)	# 19-21
    sprite('ag033_02', 3)	# 22-24
    sprite('ag020_05', 3)	# 25-27
    sprite('ag020_06', 3)	# 28-30
    label(0)
    sprite('ag020_07', 4)	# 31-34
    sprite('ag020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ag050_00', 1)	# 1-1
    sprite('ag050_01', 1)	# 2-2
    sprite('ag050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ag050_01', 1)	# 1-1
    sprite('ag050_02', 1)	# 2-2
    sprite('ag050_01', 2)	# 3-4
    sprite('ag050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ag050_02', 1)	# 1-1
    sprite('ag050_03', 1)	# 2-2
    sprite('ag050_02', 2)	# 3-4
    sprite('ag050_01', 2)	# 5-6
    sprite('ag050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ag050_03', 1)	# 1-1
    sprite('ag050_04', 1)	# 2-2
    sprite('ag050_03', 2)	# 3-4
    sprite('ag050_02', 2)	# 5-6
    sprite('ag050_01', 2)	# 7-8
    sprite('ag050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ag050_04', 1)	# 1-1
    sprite('ag050_04', 1)	# 2-2
    sprite('ag050_04', 2)	# 3-4
    sprite('ag050_03', 2)	# 5-6
    sprite('ag050_02', 2)	# 7-8
    sprite('ag050_01', 2)	# 9-10
    sprite('ag050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ag052_00', 1)	# 1-1
    sprite('ag052_01', 1)	# 2-2
    sprite('ag052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ag052_01', 1)	# 1-1
    sprite('ag052_02', 1)	# 2-2
    sprite('ag052_01', 2)	# 3-4
    sprite('ag052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ag052_02', 1)	# 1-1
    sprite('ag052_03', 1)	# 2-2
    sprite('ag052_02', 2)	# 3-4
    sprite('ag052_01', 2)	# 5-6
    sprite('ag052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ag052_03', 1)	# 1-1
    sprite('ag052_04', 1)	# 2-2
    sprite('ag052_03', 2)	# 3-4
    sprite('ag052_02', 2)	# 5-6
    sprite('ag052_01', 2)	# 7-8
    sprite('ag052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ag052_04', 1)	# 1-1
    sprite('ag052_04', 1)	# 2-2
    sprite('ag052_04', 2)	# 3-4
    sprite('ag052_03', 2)	# 5-6
    sprite('ag052_02', 2)	# 7-8
    sprite('ag052_01', 2)	# 9-10
    sprite('ag052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ag054_00', 1)	# 1-1
    sprite('ag054_01', 1)	# 2-2
    sprite('ag054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ag054_01', 1)	# 1-1
    sprite('ag054_02', 1)	# 2-2
    sprite('ag054_01', 2)	# 3-4
    sprite('ag054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ag054_02', 1)	# 1-1
    sprite('ag054_03', 1)	# 2-2
    sprite('ag054_02', 2)	# 3-4
    sprite('ag054_01', 2)	# 5-6
    sprite('ag054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ag054_03', 1)	# 1-1
    sprite('ag054_04', 1)	# 2-2
    sprite('ag054_03', 2)	# 3-4
    sprite('ag054_02', 2)	# 5-6
    sprite('ag054_01', 2)	# 7-8
    sprite('ag054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ag054_04', 1)	# 1-1
    sprite('ag054_04', 1)	# 2-2
    sprite('ag054_04', 2)	# 3-4
    sprite('ag054_03', 2)	# 5-6
    sprite('ag054_02', 2)	# 7-8
    sprite('ag054_01', 2)	# 9-10
    sprite('ag054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ag060_00', 4)	# 1-4
    label(0)
    sprite('ag060_01', 4)	# 5-8
    sprite('ag060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ag060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ag060_04', 8)	# 1-8
    label(1)
    sprite('ag060_05', 4)	# 9-12
    sprite('ag060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('ag060_07', 4)	# 1-4

@State
def CmnActBDownBound():
    sprite('ag060_08', 2)	# 1-2
    sprite('ag060_09', 2)	# 3-4
    sprite('ag060_10', 2)	# 5-6
    sprite('ag060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('ag060_12', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('ag064_00', 4)	# 1-4
    sprite('ag064_01', 4)	# 5-8
    sprite('ag064_02', 4)	# 9-12
    sprite('ag064_03', 4)	# 13-16

@State
def CmnActFDownUpper():
    sprite('ag063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ag063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ag063_03', 3)	# 1-3
    sprite('ag063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ag063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('ag060_08', 2)	# 1-2
    sprite('ag060_09', 2)	# 3-4
    sprite('ag060_10', 2)	# 5-6
    sprite('ag060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('ag060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ag064_00', 6)	# 1-6
    sprite('ag064_01', 6)	# 7-12
    sprite('ag064_02', 6)	# 13-18
    sprite('ag064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('ag060_00', 4)	# 1-4
    label(0)
    sprite('ag060_01', 4)	# 5-8
    sprite('ag060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ag060_03', 4)	# 1-4
    sprite('ag060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('ag060_04', 8)	# 1-8
    label(0)
    sprite('ag060_05', 4)	# 9-12
    sprite('ag060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ag060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('ag072_00', 3)	# 1-3
    sprite('ag072_01', 3)	# 4-6
    sprite('ag072_02', 3)	# 7-9
    label(0)
    sprite('ag072_01', 3)	# 10-12
    sprite('ag072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ag074_00', 2)	# 1-2
    sprite('ag074_01', 2)	# 3-4
    sprite('ag074_02', 2)	# 5-6
    sprite('ag074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('ag072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('ag063_00', 3)	# 1-3
    label(0)
    sprite('ag063_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('ag082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('ag052_01', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('ag070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('ag070_01', 4)	# 1-4
    sprite('ag070_02', 4)	# 5-8
    sprite('ag070_03', 4)	# 9-12
    sprite('ag070_04', 4)	# 13-16
    sprite('ag070_05', 4)	# 17-20
    sprite('ag070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ag040_03', 2)	# 1-2
    sprite('ag040_02', 2)	# 3-4
    sprite('ag040_01', 2)	# 5-6
    sprite('ag040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('ag020_02', 3)	# 1-3
    sprite('ag020_03', 3)	# 4-6
    sprite('ag020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('ag020_02', 3)	# 1-3
    sprite('ag020_03', 3)	# 4-6
    sprite('ag020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('ag020_02', 3)	# 1-3
    sprite('ag020_03', 3)	# 4-6
    sprite('ag020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('ag112_00', 3)	# 1-3
    sprite('ag112_01', 3)	# 4-6
    sprite('ag112_02', 3)	# 7-9
    sprite('ag112_03', 3)	# 10-12
    sprite('ag112_04', 3)	# 13-15
    sprite('ag112_05', 3)	# 16-18
    sprite('ag020_07', 4)	# 19-22
    sprite('ag020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandF():
    sprite('ag112_00', 3)	# 1-3
    sprite('ag112_01', 3)	# 4-6
    sprite('ag112_02', 3)	# 7-9
    sprite('ag112_03', 3)	# 10-12
    sprite('ag112_04', 3)	# 13-15
    sprite('ag112_05', 3)	# 16-18
    sprite('ag020_07', 4)	# 19-22
    sprite('ag020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('ag112_00', 3)	# 1-3
    sprite('ag112_01', 3)	# 4-6
    sprite('ag112_02', 3)	# 7-9
    sprite('ag112_03', 3)	# 10-12
    sprite('ag112_04', 3)	# 13-15
    sprite('ag112_05', 3)	# 16-18
    sprite('ag020_07', 4)	# 19-22
    sprite('ag020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('ag010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('ag040_00', 3)	# 1-3
    sprite('ag040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ag040_02', 5)	# 1-5
    sprite('ag040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ag040_01', 3)	# 1-3
    sprite('ag040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ag040_04', 1)	# 1-1
    label(0)
    sprite('ag040_02', 5)	# 2-6
    sprite('ag040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ag040_01', 3)	# 1-3
    sprite('ag040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ag040_00', 3)	# 1-3
    sprite('ag040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('ag040_04', 1)	# 1-1
    label(0)
    sprite('ag040_02', 5)	# 2-6
    sprite('ag040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ag040_01', 3)	# 1-3
    sprite('ag040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ag040_04', 1)	# 1-1
    label(0)
    sprite('ag040_02', 5)	# 2-6
    sprite('ag040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ag040_01', 3)	# 1-3
    sprite('ag040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ag043_00', 3)	# 1-3
    sprite('ag043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ag043_02', 5)	# 1-5
    sprite('ag043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ag043_01', 3)	# 1-3
    sprite('ag043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ag043_04', 1)	# 1-1
    label(0)
    sprite('ag043_02', 5)	# 2-6
    sprite('ag043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ag043_01', 3)	# 1-3
    sprite('ag043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ag045_00', 3)	# 1-3
    sprite('ag045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ag045_02', 5)	# 1-5
    sprite('ag045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ag045_01', 3)	# 1-3
    sprite('ag045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ag045_04', 1)	# 1-1
    label(0)
    sprite('ag045_02', 5)	# 2-6
    sprite('ag045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ag045_01', 3)	# 1-3
    sprite('ag045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ag040_04', 2)	# 1-2
    sprite('ag040_04', 2)	# 3-4
    sprite('ag040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ag040_02', 4)	# 6-9
    sprite('ag040_01', 4)	# 10-13
    sprite('ag040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ag043_04', 2)	# 1-2
    sprite('ag043_04', 2)	# 3-4
    sprite('ag043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ag043_02', 4)	# 6-9
    sprite('ag043_01', 4)	# 10-13
    sprite('ag043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ag045_04', 2)	# 1-2
    sprite('ag045_04', 2)	# 3-4
    sprite('ag045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ag045_02', 4)	# 6-9
    sprite('ag045_01', 4)	# 10-13
    sprite('ag045_00', 4)	# 14-17

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('ag200_00', 2)	# 1-2
    sprite('ag200_01', 4)	# 3-6
    sprite('ag200_02', 2)	# 7-8	 **attackbox here**
    sprite('ag200_04', 4)	# 9-12	 **attackbox here**
    sprite('ag200_04', 5)	# 13-17	 **attackbox here**
    sprite('ag200_05', 4)	# 18-21
    sprite('ag200_06', 4)	# 22-25
    sprite('ag200_07', 4)	# 26-29

@State
def CmnActAirLockWait():
    sprite('nt045_02', 1)	# 1-1
    sprite('nt045_01', 3)	# 2-4
    sprite('nt045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ag251_00', 3)	# 1-3
    sprite('ag251_01', 2)	# 4-5
    sprite('ag251_02', 2)	# 6-7
    sprite('ag251_03', 2)	# 8-9	 **attackbox here**
    sprite('ag251_04', 2)	# 10-11	 **attackbox here**
    sprite('ag251_05', 2)	# 12-13	 **attackbox here**
    sprite('ag251_06', 2)	# 14-15	 **attackbox here**
    sprite('ag251_03', 2)	# 16-17	 **attackbox here**
    sprite('ag251_04', 2)	# 18-19	 **attackbox here**
    sprite('ag251_05', 2)	# 20-21	 **attackbox here**
    sprite('ag251_06', 2)	# 22-23	 **attackbox here**
    sprite('ag251_07', 3)	# 24-26
    sprite('ag251_08', 3)	# 27-29

@State
def CmnActLandSpin():
    sprite('ag071_00', 2)	# 1-2
    label(0)
    sprite('ag071_01', 2)	# 3-4
    sprite('ag071_02', 2)	# 5-6
    sprite('ag071_03', 2)	# 7-8
    sprite('ag071_04', 2)	# 9-10
    sprite('ag071_05', 2)	# 11-12
    sprite('ag071_06', 2)	# 13-14
    sprite('ag071_07', 2)	# 15-16
    sprite('ag071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ag040_02', 3)	# 1-3
    sprite('ag040_01', 3)	# 4-6
    sprite('ag040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('ag071_00', 2)	# 1-2
    label(0)
    sprite('ag071_01', 2)	# 3-4
    sprite('ag071_02', 2)	# 5-6
    sprite('ag071_03', 2)	# 7-8
    sprite('ag071_04', 2)	# 9-10
    sprite('ag071_05', 2)	# 11-12
    sprite('ag071_06', 2)	# 13-14
    sprite('ag071_07', 2)	# 15-16
    sprite('ag071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('ag124_00', 2)	# 1-2
    label(0)
    sprite('ag124_01', 2)	# 3-4
    sprite('ag124_02', 2)	# 5-6
    sprite('ag124_03', 2)	# 7-8
    sprite('ag124_04', 2)	# 9-10
    sprite('ag124_05', 2)	# 11-12
    sprite('ag124_06', 2)	# 13-14
    sprite('ag124_07', 2)	# 15-16
    sprite('ag124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ag077_02', 4)	# 1-4
    label(0)
    sprite('ag077_03', 3)	# 5-7
    sprite('ag077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ag077_05', 5)	# 1-5
    sprite('ag077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('ag077_02', 4)	# 1-4
    label(0)
    sprite('ag077_03', 3)	# 5-7
    sprite('ag077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ag077_05', 5)	# 1-5
    sprite('ag077_06', 4)	# 6-9

@State
def CmnActBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    label(0)
    sprite('ag121_00', 3)	# 1-3
    sprite('ag121_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('ag121_02', 3)	# 1-3
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActBurstEnd():
    sprite('ag121_05', 3)	# 1-3
    sprite('ag121_06', 3)	# 4-6
    sprite('ag020_04', 3)	# 7-9
    sprite('ag020_05', 3)	# 10-12
    sprite('ag020_06', 3)	# 13-15
    label(2)
    sprite('ag020_07', 4)	# 16-19
    sprite('ag020_08', 4)	# 20-23
    loopRest()
    gotoLabel(2)

@State
def CmnActAirBurstBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
    label(0)
    sprite('ag121_00', 3)	# 1-3
    sprite('ag121_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('ag121_02', 3)	# 1-3
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirBurstEnd():
    sprite('ag121_05', 3)	# 1-3
    sprite('ag121_06', 3)	# 4-6
    sprite('ag020_04', 3)	# 7-9
    sprite('ag020_05', 3)	# 10-12
    sprite('ag020_06', 3)	# 13-15
    label(2)
    sprite('ag020_07', 4)	# 16-19
    sprite('ag020_08', 4)	# 20-23
    loopRest()
    gotoLabel(2)

@State
def CmnActOverDriveBegin():
    sprite('ag121_00', 2)	# 1-2
    sprite('ag121_00', 2)	# 3-4
    sprite('ag121_01', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ag121_01', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ag121_02', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActOverDriveEnd():
    sprite('ag121_05', 6)	# 1-6
    sprite('ag121_06', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('ag121_00', 2)	# 1-2
    sprite('ag121_00', 2)	# 3-4
    sprite('ag121_01', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('ag121_01', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ag121_02', 3)	# 1-3
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirOverDriveEnd():
    sprite('ag121_05', 6)	# 1-6
    sprite('ag121_06', 6)	# 7-12
    label(0)
    sprite('ag020_07', 4)	# 13-16
    sprite('ag020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ag121_00', 2)	# 1-2
    sprite('ag121_00', 2)	# 3-4
    sprite('ag121_01', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(11)
    Unknown23148('PAG_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 10, 0)
    sprite('ag121_01', 1)	# 7-7
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ag121_02', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossRushEnd():
    sprite('ag121_05', 6)	# 1-6
    sprite('ag121_06', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('ag121_00', 2)	# 1-2
    sprite('ag121_00', 2)	# 3-4
    sprite('ag121_01', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    Unknown36(11)
    Unknown23148('PAG_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 10, 0)
    sprite('ag121_01', 1)	# 7-7
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ag121_02', 3)	# 1-3
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossRushEnd():
    sprite('ag121_05', 6)	# 1-6
    sprite('ag121_06', 6)	# 7-12
    label(0)
    sprite('ag020_07', 4)	# 13-16
    sprite('ag020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
        Unknown36(11)
        Unknown23148('PAG_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 10, 0)
    label(0)
    sprite('ag121_00', 2)	# 1-2
    sprite('ag121_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('ag121_02', 3)	# 1-3
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossChangeEnd():
    sprite('ag121_05', 3)	# 1-3
    sprite('ag121_06', 3)	# 4-6
    sprite('ag020_05', 4)	# 7-10
    sprite('ag020_06', 2)	# 11-12
    sprite('ag020_07', 4)	# 13-16
    sprite('ag020_08', 4)	# 17-20
    loopRest()

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        SLOT_65 = 1
        SLOT_66 = 1
        Unknown36(11)
        Unknown23148('PAG_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 10, 0)
    label(0)
    sprite('ag121_00', 2)	# 1-2
    sprite('ag121_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():

    def upon_STATE_END():
        SLOT_65 = 0
        SLOT_66 = 0
    sprite('ag121_02', 3)	# 1-3
    label(1)
    sprite('ag121_03', 3)	# 4-6
    sprite('ag121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossChangeEnd():
    sprite('ag121_05', 3)	# 1-3
    sprite('ag121_06', 3)	# 4-6
    sprite('ag020_05', 4)	# 7-10
    sprite('ag020_06', 2)	# 11-12
    label(0)
    sprite('ag020_07', 4)	# 13-16
    sprite('ag020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(12000)
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        Unknown1112('')
    sprite('ag203_00', 1)	# 1-1
    sprite('ag203_01', 1)	# 2-2
    sprite('ag203_02', 1)	# 3-3
    sprite('ag203_02', 1)	# 4-4
    SFX_3('ag000')
    sprite('ag203_03', 3)	# 5-7
    GFX_1('agef_5bshot_11', 0)
    sprite('ag203_04', 2)	# 8-9
    sprite('ag203_06', 3)	# 10-12	 **attackbox here**
    physicsXImpulse(-4000)
    Unknown7009(1)
    SFX_3('blaze_normal')
    sprite('ag203_06', 3)	# 13-15	 **attackbox here**
    GFX_1('agef_5bshotsmoke_00', 1)
    Unknown23027()
    Unknown1019(60)
    Recovery()
    Unknown2063()
    sprite('ag203_06', 3)	# 16-18	 **attackbox here**
    GFX_1('agef_5bshotsmoke_00', 2)
    Unknown1019(60)
    sprite('ag203_06', 3)	# 19-21	 **attackbox here**
    GFX_1('agef_5bshotsmoke_00', 3)
    Unknown1019(60)
    sprite('ag203_06', 3)	# 22-24	 **attackbox here**
    GFX_1('agef_5bshotsmoke_00', 4)
    Unknown1019(60)
    sprite('ag203_07', 3)	# 25-27
    GFX_1('agef_5bshotsmoke_00', 0)
    Unknown1019(60)
    sprite('ag203_08', 4)	# 28-31
    GFX_1('agef_5bshotsmoke_00', 0)
    Unknown1019(60)
    sprite('ag203_09', 4)	# 32-35
    GFX_1('agef_5bshotsmoke_00', 0)
    Unknown1084(1)

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('ag204_00', 3)	# 1-3
    sprite('ag204_01', 3)	# 4-6
    sprite('ag204_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 1000, 0)
    Unknown7007('7061673132315f300000000000000000640000007061673132315f310000000000000000640000007061673132315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag204_03', 3)	# 10-12
    sprite('ag204_02', 3)	# 13-15
    sprite('ag204_03', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('ag204_02', 3)	# 19-21
    sprite('ag204_03', 3)	# 22-24
    sprite('ag204_02', 3)	# 25-27
    sprite('ag204_03', 3)	# 28-30
    sprite('ag204_02', 3)	# 31-33
    sprite('ag204_03', 3)	# 34-36
    sprite('ag204_04', 3)	# 37-39

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')

        def upon_STATE_END():
            Unknown36(11)
            Unknown23078(0)
            Unknown35()
    sprite('ag205_00', 3)	# 1-3
    sprite('ag205_01', 2)	# 4-5
    Unknown7009(2)
    Unknown23029(11, 1010, 0)
    sprite('ag205_02', 4)	# 6-9
    GFX_1('persona_enter_ply', 0)
    sprite('ag205_03', 4)	# 10-13
    sprite('ag205_04', 4)	# 14-17
    sprite('ag205_03', 4)	# 18-21
    sprite('ag205_04', 3)	# 22-24
    sprite('ag205_04', 1)	# 25-25
    Recovery()
    Unknown2063()
    sprite('ag205_03', 4)	# 26-29
    sprite('ag205_04', 4)	# 30-33
    sprite('ag205_03', 4)	# 34-37
    sprite('ag205_04', 4)	# 38-41
    sprite('ag205_03', 4)	# 42-45
    sprite('ag205_04', 4)	# 46-49
    sprite('ag205_05', 4)	# 50-53

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AirPushbackX(12000)
        AirPushbackY(-55000)
        Unknown9310(1)
        HitOverhead(0)
        Unknown11058('0100000000000000000000000000000000000000')
        JumpCancel_(0)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            physicsXImpulse(-12000)
            physicsYImpulse(16000)
            Unknown1043()
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ag202_00', 2)	# 1-2
    sprite('ag202_01', 2)	# 3-4
    GFX_0('agef202_burner_jump', 0)
    GFX_0('agef202_burner_jump_back', 1)
    sprite('ag202_02', 2)	# 5-6
    teleportRelativeX(70000)
    callSubroutine('Burner_Delete')
    GFX_0('agef202_burner_jump', 0)
    GFX_0('agef202_burner_jump_back', 1)
    sprite('ag202_03', 2)	# 7-8
    SLOT_67 = SLOT_19
    if (SLOT_67 > 750000):
        SLOT_67 = 750000
    SLOT_12 = SLOT_67
    Unknown1019(8)
    physicsYImpulse(42000)
    setGravity(3000)
    callSubroutine('Burner_Delete')
    GFX_0('agef202_burner_jump', 0)
    GFX_0('agef202_burner_jump_back', 1)
    sprite('ag202_04', 2)	# 9-10
    callSubroutine('Burner_Delete')
    sprite('ag202_05', 3)	# 11-13
    sprite('ag202_06', 3)	# 14-16
    sprite('ag202_07', 3)	# 17-19
    Unknown1019(50)
    sprite('ag202_08', 2)	# 20-21
    GFX_0('agef202_burner', 0)
    GFX_0('agef202_burner_back', 1)
    Unknown1019(50)
    sprite('ag202_09', 2)	# 22-23
    callSubroutine('Burner_Delete')
    SFX_3('hit_m_slow')
    Unknown1019(50)
    sprite('ag202_10', 6)	# 24-29	 **attackbox here**
    RefreshMultihit()
    Unknown7009(2)
    sprite('ag202_11', 6)	# 30-35
    Recovery()
    Unknown2063()
    sprite('ag202_12', 6)	# 36-41
    sprite('ag020_04', 3)	# 42-44
    sprite('ag020_05', 4)	# 45-48
    sprite('ag020_06', 2)	# 49-50
    label(0)
    sprite('ag020_07', 4)	# 51-54
    sprite('ag020_08', 4)	# 55-58
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag231_01', 2)	# 59-60
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    callSubroutine('Burner_Delete')
    sprite('ag231_00', 2)	# 61-62
    sprite('ag231_01', 2)	# 63-64

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AttackP1(100)
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ag200_00', 1)	# 1-1
    sprite('ag200_01', 2)	# 2-3
    sprite('ag200_02', 2)	# 4-5	 **attackbox here**
    StartMultihit()
    sprite('ag200_04', 3)	# 6-8	 **attackbox here**
    Unknown23054('61673230305f303300000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    sprite('ag200_04', 7)	# 9-15	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ag200_05', 3)	# 16-18
    sprite('ag200_06', 3)	# 19-21
    sprite('ag200_07', 3)	# 22-24

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9154(19)
        AirUntechableTime(19)
        AirPushbackX(12000)
        AirPushbackY(20000)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            HitOrBlockCancel('CancelOrgiaDash')
            HitOrBlockCancel('NmlAtk4A3rd')
            Unknown14070('NmlAtk5AEx')
            Unknown14070('NmlAtk5BEx')
            Unknown14070('NmlAtk2BEx')
            Unknown14070('AN_CmnActCrushAttackEx')
            Unknown14070('NmlAtk2CEx')
            Unknown14070('AN_NmlAtkThrowEX')
            Unknown14070('AN_NmlAtkBackThrowEX')
            HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('CmnActInvincibleAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ag206_00', 3)	# 1-3
    sprite('ag206_01', 2)	# 4-5
    sprite('ag206_02', 2)	# 6-7
    physicsXImpulse(3000)
    sprite('ag206_03', 2)	# 8-9
    Unknown1019(400)
    sprite('ag206_04', 6)	# 10-15	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    Unknown1019(300)
    physicsYImpulse(6000)
    setGravity(2000)
    Unknown7009(1)
    sprite('ag206_05', 3)	# 16-18
    Unknown1019(60)
    Recovery()
    Unknown2063()
    sprite('ag206_06', 3)	# 19-21
    Unknown1019(60)
    sprite('ag206_07', 3)	# 22-24
    sprite('ag020_04', 3)	# 25-27
    sprite('ag020_05', 4)	# 28-31
    sprite('ag020_06', 2)	# 32-33
    label(0)
    sprite('ag020_07', 4)	# 34-37
    sprite('ag020_08', 4)	# 38-41
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag231_01', 3)	# 42-44
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown21015('41697242616c6b616e5f4d61746f6d6500000000000000000000000000000000e60f000000000000')
    callSubroutine('Burner_Delete')
    Unknown14072('NmlAtk5AEx')
    Unknown14072('NmlAtk5BEx')
    Unknown14072('NmlAtk2BEx')
    Unknown14072('AN_CmnActCrushAttackEx')
    Unknown14072('NmlAtk2CEx')
    Unknown14072('AN_NmlAtkThrowEX')
    Unknown14072('AN_NmlAtkBackThrowEX')
    sprite('ag231_00', 1)	# 45-45
    sprite('ag231_00', 6)	# 46-51
    Unknown14074('NmlAtk5AEx')
    Unknown14074('NmlAtk5BEx')
    Unknown14074('NmlAtk2BEx')
    Unknown14074('AN_CmnActCrushAttackEx')
    Unknown14074('NmlAtk2CEx')
    Unknown14074('AN_NmlAtkThrowEX')
    Unknown14074('AN_NmlAtkBackThrowEX')
    sprite('ag231_01', 3)	# 52-54

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP2(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(30000)
        AirUntechableTime(40)
        HitOverhead(0)
        HitOrBlockCancel('CancelOrgiaDash')
        HitJumpCancel(1)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1

        def upon_8():
            Unknown21005(1)
            Unknown23073()
        Unknown22004(10, 1)
    sprite('ag208_00', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(3500)
    physicsYImpulse(2200)
    sprite('ag208_01', 3)	# 4-6
    Unknown1019(200)
    YAccel(200)
    SFX_0('003_swing_grap_0_1')
    sprite('ag208_02', 1)	# 7-7	 **attackbox here**
    StartMultihit()
    Unknown1019(400)
    YAccel(400)
    GFX_0('agef202_burner_jump', 0)
    GFX_0('agef202_burner_jump_back', 1)
    sprite('ag208_02', 2)	# 8-9	 **attackbox here**
    RefreshMultihit()
    Unknown14070('NmlAtk4A4th')
    Unknown7009(0)
    sprite('ag208_03', 2)	# 10-11
    callSubroutine('Burner_Delete')
    Unknown1019(80)
    YAccel(150)
    Recovery()
    Unknown2063()
    sprite('ag208_04', 4)	# 12-15
    Unknown1019(-30)
    sprite('ag208_05', 2)	# 16-17
    Unknown23027()
    YAccel(70)
    setGravity(2000)
    sprite('ag208_05', 2)	# 18-19
    if SLOT_51:
        Unknown14072('NmlAtk4A4th')
    sprite('ag207_06', 6)	# 20-25
    Unknown1019(80)
    YAccel(70)
    Unknown2001()
    sprite('ag020_04', 3)	# 26-28
    Unknown1019(80)
    YAccel(70)
    Unknown14073('NmlAtk4A4th')

@State
def NmlAtk4A4th():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        AirPushbackX(12000)
        AirPushbackY(-55000)
        Unknown9310(1)
        HitOverhead(0)
        JumpCancel_(0)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            physicsXImpulse(-12000)
            physicsYImpulse(16000)
            Unknown1043()
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ag202_05', 3)	# 1-3
    physicsXImpulse(18000)
    physicsYImpulse(24000)
    setGravity(3000)
    sprite('ag202_06', 3)	# 4-6
    sprite('ag202_07', 3)	# 7-9
    sprite('ag202_08', 2)	# 10-11
    GFX_0('agef202_burner', 0)
    GFX_0('agef202_burner_back', 1)
    Unknown1019(50)
    sprite('ag202_09', 2)	# 12-13
    callSubroutine('Burner_Delete')
    SFX_3('hit_m_slow')
    Unknown1019(50)
    sprite('ag202_10', 6)	# 14-19	 **attackbox here**
    RefreshMultihit()
    Unknown7009(2)
    sprite('ag202_11', 6)	# 20-25
    Recovery()
    Unknown2063()
    sprite('ag202_12', 6)	# 26-31
    sprite('ag020_04', 3)	# 32-34
    sprite('ag020_05', 4)	# 35-38
    sprite('ag020_06', 2)	# 39-40
    label(0)
    sprite('ag020_07', 4)	# 41-44
    sprite('ag020_08', 4)	# 45-48
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag231_01', 2)	# 49-50
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    callSubroutine('Burner_Delete')
    sprite('ag231_00', 2)	# 51-52
    sprite('ag231_01', 2)	# 53-54

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(70)
        GroundedHitstunAnimation(9)
        AirPushbackY(18000)
        AirUntechableTime(20)
        Hitstop(9)
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown1112('')

        def upon_ON_HIT_OR_BLOCK():
            HitOrBlockJumpCancel(1)

        def upon_43():
            if (SLOT_48 == 2019):
                HitJumpCancel(1)
    sprite('ag200_07', 3)	# 1-3
    sprite('ag201_00', 3)	# 4-6
    sprite('ag201_01', 3)	# 7-9
    SFX_3('hit_l_fast')
    sprite('ag201_02', 3)	# 10-12	 **attackbox here**
    Unknown7009(1)

    def upon_45():
        if CheckInput(0xa):
            SLOT_2 = 1
            clearUponHandler(45)
    sprite('ag201_03', 3)	# 13-15	 **attackbox here**
    loopRest()
    Unknown19(0, 2, 2)
    sprite('ag201_04', 2)	# 16-17
    GFX_0('5B_Matome', 100)
    Unknown23027()
    sprite('ag201_04', 2)	# 18-19
    sprite('ag201_05', 2)	# 20-21
    sprite('ag201_05', 2)	# 22-23
    sprite('ag201_06', 2)	# 24-25
    sprite('ag201_06', 2)	# 26-27
    sprite('ag201_07', 2)	# 28-29
    sprite('ag201_08', 3)	# 30-32	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('ag201_09', 3)	# 33-35
    sprite('ag201_10', 3)	# 36-38
    sprite('ag201_11', 3)	# 39-41
    sprite('ag201_12', 3)	# 42-44
    ExitState()
    label(0)
    sprite('ag201_04', 3)	# 45-47
    clearUponHandler(45)
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ag201_05', 3)	# 48-50
    sprite('ag201_06', 3)	# 51-53
    sprite('ag201_07', 2)	# 54-55
    sprite('ag201_08', 2)	# 56-57	 **attackbox here**
    sprite('ag201_09', 2)	# 58-59
    sprite('ag201_10', 2)	# 60-61
    sprite('ag201_11', 2)	# 62-63
    sprite('ag201_12', 2)	# 64-65

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(1000)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ag230_00', 2)	# 1-2
    sprite('ag230_00', 2)	# 3-4
    sprite('ag230_01', 3)	# 5-7
    SFX_0('003_swing_grap_0_0')
    sprite('ag230_03', 2)	# 8-9	 **attackbox here**
    RefreshMultihit()
    Unknown7009(0)
    sprite('ag230_03', 7)	# 10-16	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ag230_00', 4)	# 17-20

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(70)
        GroundedHitstunAnimation(9)
        AirPushbackY(18000)
        AirUntechableTime(20)
        Hitstop(9)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')

        def upon_ON_HIT_OR_BLOCK():
            HitOrBlockJumpCancel(1)

        def upon_43():
            if (SLOT_48 == 2318):
                HitJumpCancel(1)
    sprite('ag231_00', 3)	# 1-3
    sprite('ag231_01', 3)	# 4-6
    sprite('ag231_02', 2)	# 7-8
    sprite('ag231_02', 2)	# 9-10
    SFX_3('hit_l_fast')
    Unknown7009(1)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ag231_03', 2)	# 11-12	 **attackbox here**

    def upon_45():
        if CheckInput(0xa):
            SLOT_2 = 1
            clearUponHandler(45)
    loopRest()
    Unknown19(0, 2, 2)
    sprite('ag231_03', 2)	# 13-14	 **attackbox here**
    GFX_0('2B_Matome', 100)
    Unknown23027()
    setInvincible(0)
    sprite('ag231_04', 2)	# 15-16	 **attackbox here**
    sprite('ag231_04', 2)	# 17-18	 **attackbox here**
    sprite('ag231_05', 2)	# 19-20
    sprite('ag231_05', 2)	# 21-22
    sprite('ag231_05', 6)	# 23-28
    sprite('ag231_06', 4)	# 29-32
    Recovery()
    Unknown2063()
    sprite('ag231_07', 4)	# 33-36
    sprite('ag231_08', 4)	# 37-40
    ExitState()
    label(0)
    sprite('ag231_04ex', 2)	# 41-42	 **attackbox here**
    clearUponHandler(45)
    setInvincible(0)
    sprite('ag231_05ex', 2)	# 43-44	 **attackbox here**
    sprite('ag231_05', 6)	# 45-50
    Recovery()
    Unknown2063()
    sprite('ag231_06', 4)	# 51-54
    sprite('ag231_07', 4)	# 55-58
    sprite('ag231_08', 4)	# 59-62

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        Hitstop(5)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(18000)
        AirUntechableTime(40)
        HitLow(2)
        HitOrBlockCancel('CancelOrgiaDash')
    sprite('ag211_00', 3)	# 1-3
    sprite('ag211_01', 1)	# 4-4
    sprite('ag211_01', 2)	# 5-6
    physicsXImpulse(15000)
    sprite('ag211_02', 2)	# 7-8
    GFX_0('hibana2AB', 100)
    sprite('ag211_03', 3)	# 9-11
    SFX_0('005_swing_grap_2_1')
    sprite('ag211_04', 5)	# 12-16	 **attackbox here**
    RefreshMultihit()
    Unknown7007('7061673130375f300000000000000000640000007061673130375f310000000000000000640000007061673130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag211_05', 4)	# 17-20
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('ag211_06', 4)	# 21-24
    Unknown1019(50)
    sprite('ag211_07', 4)	# 25-28
    Unknown1019(50)
    sprite('ag211_08', 4)	# 29-32
    Unknown1019(0)
    Unknown2001()

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        AirHitstunAnimation(10)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('AN_NmlAtkAIR5A_2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('ag250_00', 2)	# 1-2
    sprite('ag250_01', 4)	# 3-6
    sprite('ag250_02', 2)	# 7-8
    SFX_0('004_swing_grap_1_0')
    sprite('ag250_03', 8)	# 9-16	 **attackbox here**
    RefreshMultihit()
    Unknown7009(3)
    sprite('ag250_04', 2)	# 17-18
    Recovery()
    Unknown2063()
    sprite('ag250_05', 2)	# 19-20
    sprite('ag250_06', 3)	# 21-23
    sprite('ag250_07', 3)	# 24-26

@State
def AN_NmlAtkAIR5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(80)
        Unknown9016(1)

        def upon_11():
            Unknown2037(1)
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ag251_00', 2)	# 1-2
    sprite('ag251_01', 2)	# 3-4
    sprite('ag251_02', 2)	# 5-6
    SFX_3('ag003')
    sprite('ag251_03', 2)	# 7-8	 **attackbox here**
    GFX_0('DrillAirB', 0)
    RefreshMultihit()
    Unknown7009(4)
    sprite('ag251_04', 2)	# 9-10	 **attackbox here**
    if SLOT_2:
        HitOverhead(0)
    sprite('ag251_05', 2)	# 11-12	 **attackbox here**
    if SLOT_2:
        HitOverhead(0)
    sprite('ag251_06', 2)	# 13-14	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ag251_03', 2)	# 15-16	 **attackbox here**
    sprite('ag251_04', 2)	# 17-18	 **attackbox here**
    sprite('ag251_05', 2)	# 19-20	 **attackbox here**
    sprite('ag251_06', 2)	# 21-22	 **attackbox here**
    sprite('ag251_07', 2)	# 23-24
    sprite('ag251_08', 2)	# 25-26

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_LANDING():
            Unknown23029(11, 1021, 0)

        def upon_STATE_END():
            Unknown23029(11, 1022, 0)
        Unknown4009(11)
        HitOrBlockCancel('CancelOrgiaDash')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ag254_00', 3)	# 1-3
    sprite('ag254_01', 4)	# 4-7
    Unknown23029(11, 1020, 0)
    Unknown7007('7061673132335f300000000000000000640000007061673132335f310000000000000000640000007061673132335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag254_02', 4)	# 8-11
    sprite('ag254_03', 4)	# 12-15
    sprite('ag254_02', 4)	# 16-19
    sprite('ag254_03', 4)	# 20-23
    sprite('ag254_02', 4)	# 24-27
    sprite('ag254_03', 4)	# 28-31
    Recovery()
    Unknown2063()
    sprite('ag254_04', 4)	# 32-35

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockCancel('CancelOrgiaDash')

        def upon_STATE_END():
            Unknown36(11)
            Unknown23078(0)
            Unknown35()
            Unknown1043()
    sprite('ag255_00', 3)	# 1-3
    sprite('ag255_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown22004(6, 1)
    sprite('ag255_02', 3)	# 7-9
    Unknown23029(11, 1030, 0)
    Unknown7007('7061673132305f300000000000000000640000007061673132305f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ag255_03', 3)	# 10-12
    sprite('ag255_04', 3)	# 13-15
    sprite('ag255_03', 3)	# 16-18
    sprite('ag255_04', 3)	# 19-21
    sprite('ag255_03', 3)	# 22-24
    sprite('ag255_04', 3)	# 25-27
    sprite('ag255_03', 3)	# 28-30
    sprite('ag255_04', 3)	# 31-33
    sprite('ag255_03', 3)	# 34-36
    sprite('ag255_04', 3)	# 37-39
    sprite('ag255_03', 3)	# 40-42
    Recovery()
    Unknown2063()
    Unknown1018()
    Unknown1038()
    Unknown1019(85)
    sprite('ag255_04', 3)	# 43-45
    sprite('ag255_03', 3)	# 46-48
    sprite('ag255_05', 3)	# 49-51
    sprite('ag020_04', 3)	# 52-54

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
        sendToLabelUpon(2, 1)
        Unknown11058('0100000000000000000000000000000000000000')
    sprite('ag210_00', 3)	# 1-3
    sprite('ag210_01', 3)	# 4-6
    sprite('ag210_02', 3)	# 7-9
    SFX_3('ag001')
    Unknown7007('7061673135365f300000000000000000640000007061673135365f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    physicsXImpulse(17000)
    physicsYImpulse(25000)
    setGravity(3300)
    sprite('ag210_03', 2)	# 10-11
    sprite('ag210_04', 2)	# 12-13
    sprite('ag210_05', 3)	# 14-16
    sprite('ag210_06', 3)	# 17-19
    sprite('ag210_07', 3)	# 20-22
    Unknown1084(1)
    sprite('ag210_08', 3)	# 23-25
    SFX_0('211_down_steal_0')
    sprite('ag210_09', 3)	# 26-28	 **attackbox here**
    GFX_0('tyudanIwa', 100)
    Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
    Unknown4004('6566666563745f32393000000000000000000000000000000000000000000000ffff0000')
    Unknown1084(1)
    RefreshMultihit()
    Unknown23086(1)
    ScreenShake(0, 10000)
    sprite('ag210_10', 3)	# 29-31
    Unknown23027()
    physicsXImpulse(-5000)
    setGravity(2400)
    sprite('ag210_11', 3)	# 32-34
    sprite('ag210_12', 32767)	# 35-32801
    label(1)
    sprite('ag210_13', 2)	# 32802-32803
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ag210_14', 4)	# 32804-32807
    sprite('ag210_15', 1)	# 32808-32808
    sprite('ag210_16', 1)	# 32809-32809

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        setGravity(3000)
    sprite('ag210_10', 2)	# 1-2
    physicsYImpulse(2000)
    setGravity(2200)
    sprite('ag210_11', 2)	# 3-4
    sprite('ag210_12', 8)	# 5-12
    label(1)
    sprite('ag210_13', 2)	# 13-14
    Unknown1084(1)
    clearUponHandler(2)
    sprite('ag210_14', 2)	# 15-16
    sprite('ag210_15', 2)	# 17-18
    sprite('ag210_16', 2)	# 19-20
    sprite('ag203_00', 1)	# 21-21
    sprite('ag203_01', 1)	# 22-22
    sprite('ag203_02', 1)	# 23-23
    SFX_3('ag000')
    sprite('ag203_03', 1)	# 24-24
    sprite('ag203_03', 2)	# 25-26
    GFX_1('agef_5bshot_11', 0)
    sprite('ag203_04', 3)	# 27-29
    sprite('ag203_05', 2)	# 30-31	 **attackbox here**
    tag_voice(1, 'pag157_0', 'pag157_1', '', '')
    sprite('ag203_06', 3)	# 32-34	 **attackbox here**
    StartMultihit()
    SFX_3('blaze_normal')
    sprite('ag203_06', 3)	# 35-37	 **attackbox here**
    StartMultihit()
    GFX_1('agef_5bshotsmoke_00', 1)
    sprite('ag203_06', 3)	# 38-40	 **attackbox here**
    StartMultihit()
    GFX_1('agef_5bshotsmoke_00', 2)
    sprite('ag203_06', 3)	# 41-43	 **attackbox here**
    StartMultihit()
    GFX_1('agef_5bshotsmoke_00', 3)
    sprite('ag203_06', 3)	# 44-46	 **attackbox here**
    StartMultihit()
    GFX_1('agef_5bshotsmoke_00', 4)
    sprite('ag203_07', 3)	# 47-49
    GFX_1('agef_5bshotsmoke_00', 0)
    sprite('ag203_08', 4)	# 50-53
    GFX_1('agef_5bshotsmoke_00', 0)
    Unknown2001()
    sprite('ag203_09', 4)	# 54-57
    GFX_1('agef_5bshotsmoke_00', 0)
    sprite('ag000_01', 6)	# 58-63
    sprite('ag000_02', 6)	# 64-69
    sprite('ag000_03', 6)	# 70-75
    sprite('ag000_04', 6)	# 76-81
    sprite('ag000_05', 6)	# 82-87
    sprite('ag000_06', 6)	# 88-93
    sprite('ag000_07', 6)	# 94-99
    sprite('ag000_08', 6)	# 100-105
    sprite('ag000_09', 6)	# 106-111
    label(10)
    sprite('ag000_01', 6)	# 112-117
    sprite('ag000_02', 6)	# 118-123
    sprite('ag000_03', 6)	# 124-129
    sprite('ag000_04', 6)	# 130-135
    sprite('ag000_05', 6)	# 136-141
    sprite('ag000_06', 6)	# 142-147
    sprite('ag000_07', 6)	# 148-153
    sprite('ag000_08', 6)	# 154-159
    sprite('ag000_09', 6)	# 160-165
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 166-166

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
    sprite('ag203_07', 2)	# 1-2
    sprite('ag203_08', 2)	# 3-4
    sprite('ag203_09', 2)	# 5-6
    sprite('ag208_00', 4)	# 7-10
    Unknown1084(1)
    physicsXImpulse(13000)
    physicsYImpulse(2500)
    sprite('ag208_01', 3)	# 11-13
    SFX_0('003_swing_grap_0_1')
    sprite('ag208_02', 1)	# 14-14	 **attackbox here**
    StartMultihit()
    GFX_0('agef202_burner_jump', 0)
    GFX_0('agef202_burner_jump_back', 1)
    sprite('ag208_02', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('ag208_03', 2)	# 17-18
    callSubroutine('Burner_Delete')
    Unknown1019(80)
    YAccel(250)
    sprite('ag208_04', 4)	# 19-22
    Unknown1019(-90)
    sprite('ag208_05', 2)	# 23-24
    Unknown23027()
    YAccel(70)
    setGravity(2000)
    sprite('ag208_05', 2)	# 25-26
    sprite('ag207_06', 7)	# 27-33
    Unknown1019(80)
    YAccel(70)
    Unknown2001()
    sprite('ag020_04', 9)	# 34-42
    Unknown1019(80)
    YAccel(70)
    label(10)
    sprite('ag010_00', 3)	# 43-45
    clearUponHandler(2)
    Unknown1084(1)
    sprite('ag000_00', 6)	# 46-51
    loopRest()
    sprite('ag000_01', 6)	# 52-57
    sprite('ag000_02', 6)	# 58-63
    sprite('ag000_03', 6)	# 64-69
    sprite('ag000_04', 6)	# 70-75
    sprite('ag000_05', 6)	# 76-81
    sprite('ag000_06', 6)	# 82-87
    sprite('ag000_07', 6)	# 88-93
    sprite('ag000_08', 6)	# 94-99
    sprite('ag000_09', 6)	# 100-105
    label(0)
    sprite('ag000_01', 6)	# 106-111
    sprite('ag000_02', 6)	# 112-117
    sprite('ag000_03', 6)	# 118-123
    sprite('ag000_04', 6)	# 124-129
    sprite('ag000_05', 6)	# 130-135
    sprite('ag000_06', 6)	# 136-141
    sprite('ag000_07', 6)	# 142-147
    sprite('ag000_08', 6)	# 148-153
    sprite('ag000_09', 6)	# 154-159
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 160-160

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('ag000_01', 6)	# 1-6
    sprite('ag204_00', 4)	# 7-10
    sprite('ag204_01', 2)	# 11-12
    sprite('ag204_01', 2)	# 13-14
    tag_voice(0, 'pag158_0', 'pag158_1', '', '')
    Unknown23029(11, 1000, 0)
    Unknown4020(11)
    sprite('ag204_02', 4)	# 15-18
    GFX_1('persona_enter_ply', 0)
    sprite('ag204_03', 4)	# 19-22
    sprite('ag204_02', 4)	# 23-26
    sprite('ag204_03', 5)	# 27-31
    sprite('ag204_02', 5)	# 32-36
    sprite('ag204_03', 5)	# 37-41
    sprite('ag204_02', 5)	# 42-46
    sprite('ag204_03', 5)	# 47-51
    sprite('ag204_02', 5)	# 52-56
    sprite('ag204_04', 5)	# 57-61
    Unknown4020(0)

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 26)	# 1-26
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 27-27
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('ag250_00', 2)	# 28-29
    StartMultihit()
    SFX_3('slash_pole_middle')
    physicsXImpulse(7500)
    physicsYImpulse(-6500)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('ag250_00', 2)	# 30-31
    StartMultihit()
    physicsXImpulse(50000)
    physicsYImpulse(-39000)
    sprite('ag250_01', 8)	# 32-39
    sprite('ag250_02', 2)	# 40-41
    SFX_0('004_swing_grap_1_0')
    sprite('ag250_03', 4)	# 42-45	 **attackbox here**
    RefreshMultihit()
    sprite('ag250_04', 2)	# 46-47
    sprite('ag250_05', 2)	# 48-49
    sprite('ag250_06', 3)	# 50-52
    sprite('ag250_07', 3)	# 53-55
    label(1)
    sprite('ag010_00', 3)	# 56-58
    Unknown8000(100, 1, 1)
    setGravity(0)
    physicsYImpulse(0)
    Unknown1019(0)
    Unknown13(4)
    Unknown23087(0)
    sprite('ag000_00', 6)	# 59-64
    loopRest()
    sprite('ag000_01', 6)	# 65-70
    sprite('ag000_02', 6)	# 71-76
    sprite('ag000_03', 6)	# 77-82
    sprite('ag000_04', 6)	# 83-88
    sprite('ag000_05', 6)	# 89-94
    sprite('ag000_06', 6)	# 95-100
    sprite('ag000_07', 6)	# 101-106
    sprite('ag000_08', 6)	# 107-112
    sprite('ag000_09', 6)	# 113-118
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('ag400_00', 4)	# 1-4
    Unknown1084(1)
    sprite('ag400_00', 3)	# 5-7
    SFX_0('003_swing_grap_0_0')
    sprite('ag400_01', 4)	# 8-11	 **attackbox here**
    StartMultihit()
    GFX_0('dmy_r_action', 2)
    GFX_0('shotgunHikari', 3)
    GFX_1('agef_shotgungrond_01', 4)
    setGravity(1600)
    physicsYImpulse(15000)
    physicsXImpulse(-3000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(10)
    sprite('ag400_01', 3)	# 12-14	 **attackbox here**
    sprite('ag400_02', 3)	# 15-17
    GFX_0('agef_orgia_shotgun', 0)
    GFX_0('agef_orgia_shotgun_back', 1)
    sprite('ag400_03', 2)	# 18-19
    sprite('ag400_04', 2)	# 20-21
    sprite('ag400_05', 2)	# 22-23
    callSubroutine('Burner_Delete')
    sprite('ag400_06', 2)	# 24-25
    label(0)
    sprite('ag400_05', 4)	# 26-29
    sprite('ag400_06', 4)	# 30-33
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('ag401_00', 15)	# 34-48
    clearUponHandler(2)
    Unknown1084(1)
    sprite('ag000_01', 6)	# 49-54
    sprite('ag000_02', 6)	# 55-60
    sprite('ag000_03', 6)	# 61-66
    sprite('ag000_04', 6)	# 67-72
    sprite('ag000_05', 6)	# 73-78
    sprite('ag000_06', 6)	# 79-84
    sprite('ag000_07', 6)	# 85-90
    sprite('ag000_08', 6)	# 91-96
    sprite('ag000_09', 6)	# 97-102
    loopRest()

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ag000_01', 6)	# 1-6
    sprite('ag204_00', 4)	# 7-10
    sprite('ag204_01', 2)	# 11-12
    sprite('ag204_01', 2)	# 13-14
    Unknown23029(11, 1000, 0)
    Unknown4020(11)
    sprite('ag204_02', 4)	# 15-18
    GFX_1('persona_enter_ply', 0)
    sprite('ag204_03', 4)	# 19-22
    sprite('ag204_02', 4)	# 23-26
    sprite('ag204_03', 5)	# 27-31
    sprite('ag204_02', 5)	# 32-36
    sprite('ag204_03', 5)	# 37-41
    sprite('ag204_02', 5)	# 42-46
    sprite('ag204_03', 5)	# 47-51
    sprite('ag204_02', 5)	# 52-56
    sprite('ag204_04', 5)	# 57-61
    Unknown4020(0)

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkThrowExe', 1, 0, 0)
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
    sprite('ag032_00', 2)	# 1-2
    label(0)
    sprite('ag032_01', 4)	# 3-6
    sprite('ag032_02', 4)	# 7-10
    Unknown8006(100, 1, 1)
    sprite('ag032_03', 4)	# 11-14
    sprite('ag032_04', 4)	# 15-18
    sprite('ag032_05', 4)	# 19-22
    sprite('ag032_06', 4)	# 23-26
    Unknown8006(100, 1, 1)
    sprite('ag032_07', 4)	# 27-30
    sprite('ag032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ag310_00', 1)	# 35-35
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ag310_01', 1)	# 36-36
    sprite('ag310_01', 1)	# 37-37
    sprite('ag310_02', 3)	# 38-40	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    sprite('ag310_03', 3)	# 41-43
    sprite('ag310_04', 10)	# 44-53
    SFX_4('pag154')
    sprite('ag310_05', 5)	# 54-58
    sprite('ag310_00', 5)	# 59-63

@State
def NmlAtkThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        PushbackX(0)
        JumpCancel_(0)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9142(60)
        Unknown11069('Throw_bom')

        def upon_43():
            if (SLOT_48 == 3000):
                clearUponHandler(43)
                JumpCancel_(1)
                HitOrBlockCancel('CancelOrgiaDash')
    sprite('ag310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ag310_02', 1)	# 5-5	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_3('ag004')
    StartMultihit()
    sprite('ag311_00', 28)	# 6-33	 **attackbox here**
    RefreshMultihit()
    GFX_0('Throw_bom', 0)
    sprite('ag311_00', 3)	# 34-36	 **attackbox here**
    SFX_4('pag153')
    sprite('ag311_01', 3)	# 37-39	 **attackbox here**
    sprite('ag311_02', 3)	# 40-42
    sprite('ag311_01', 3)	# 43-45	 **attackbox here**
    sprite('ag311_02', 3)	# 46-48
    sprite('ag311_03', 9)	# 49-57
    Unknown23027()
    sprite('ag311_04', 4)	# 58-61
    SFX_3('ag000')
    sprite('ag311_05', 4)	# 62-65
    sprite('ag311_06', 4)	# 66-69

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkBackThrowExe', 1, 0, 0)
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
    sprite('ag032_00', 2)	# 1-2
    label(0)
    sprite('ag032_01', 4)	# 3-6
    sprite('ag032_02', 4)	# 7-10
    Unknown8006(100, 1, 1)
    sprite('ag032_03', 4)	# 11-14
    sprite('ag032_04', 4)	# 15-18
    sprite('ag032_05', 4)	# 19-22
    sprite('ag032_06', 4)	# 23-26
    Unknown8006(100, 1, 1)
    sprite('ag032_07', 4)	# 27-30
    sprite('ag032_08', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ag310_00', 1)	# 35-35
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ag310_01', 1)	# 36-36
    sprite('ag310_01', 1)	# 37-37
    sprite('ag310_02', 3)	# 38-40	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    sprite('ag310_03', 3)	# 41-43
    sprite('ag310_04', 10)	# 44-53
    SFX_4('pag154')
    sprite('ag310_05', 5)	# 54-58
    sprite('ag310_00', 5)	# 59-63

@State
def NmlAtkBackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        PushbackX(0)
        JumpCancel_(0)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9142(60)
        Unknown11069('Throw_bom')

        def upon_43():
            if (SLOT_48 == 3000):
                clearUponHandler(43)
                JumpCancel_(1)
                HitOrBlockCancel('CancelOrgiaDash')
    sprite('ag310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ag310_02', 1)	# 5-5	 **attackbox here**
    Unknown2005()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_3('ag004')
    StartMultihit()
    sprite('ag311_00', 28)	# 6-33	 **attackbox here**
    RefreshMultihit()
    GFX_0('Throw_bom', 0)
    sprite('ag311_00', 3)	# 34-36	 **attackbox here**
    SFX_4('pag153')
    sprite('ag311_01', 3)	# 37-39	 **attackbox here**
    sprite('ag311_02', 3)	# 40-42
    sprite('ag311_01', 3)	# 43-45	 **attackbox here**
    sprite('ag311_02', 3)	# 46-48
    sprite('ag311_03', 9)	# 49-57
    Unknown23027()
    sprite('ag311_04', 4)	# 58-61
    SFX_3('ag000')
    sprite('ag311_05', 4)	# 62-65
    sprite('ag311_06', 4)	# 66-69

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        sendToLabelUpon(2, 9)
    sprite('ag431_00', 6)	# 1-6
    Unknown1084(1)
    sprite('ag431_01', 6)	# 7-12
    Unknown23029(11, 1050, 0)
    tag_voice(1, 'pag221_0', 'pag221_1', 'pag222_0', 'pag222_1')
    sprite('ag431_02', 4)	# 13-16
    sprite('ag431_03', 4)	# 17-20
    physicsXImpulse(-800)
    physicsYImpulse(4000)
    setGravity(30)
    sprite('ag431_04', 4)	# 21-24
    setInvincible(0)
    sprite('ag431_05', 4)	# 25-28
    sprite('ag431_04', 4)	# 29-32
    setGravity(500)
    sprite('ag431_05', 4)	# 33-36
    sprite('ag431_06', 4)	# 37-40
    sprite('ag431_07', 4)	# 41-44
    sprite('ag431_08', 4)	# 45-48
    sprite('ag020_04', 3)	# 49-51
    sprite('ag020_05', 4)	# 52-55
    sprite('ag020_06', 2)	# 56-57
    label(0)
    sprite('ag020_07', 4)	# 58-61
    sprite('ag020_08', 4)	# 62-65
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag231_01', 2)	# 66-67
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 14)	# 68-81
    sprite('ag231_01', 2)	# 82-83
    sprite('ag010_02', 2)	# 84-85
    sprite('ag010_01', 4)	# 86-89
    sprite('ag010_00', 4)	# 90-93

@State
def MachineGunA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('ag403_00', 2)	# 1-2
    sprite('ag403_01', 2)	# 3-4
    sprite('ag403_02', 2)	# 5-6
    SFX_3('ag001')
    Unknown7007('7061673230355f300000000000000000640000007061673230355f310000000000000000640000007061673230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag403_03', 2)	# 7-8
    sprite('ag403_04', 2)	# 9-10
    sprite('ag403_05', 1)	# 11-11
    sprite('ag403_06', 1)	# 12-12
    sprite('ag403_08', 1)	# 13-13
    sprite('ag403_09', 2)	# 14-15	 **attackbox here**
    GFX_0('Gatling_Matome', 100)
    sprite('ag403_10', 2)	# 16-17
    sprite('ag403_09', 2)	# 18-19	 **attackbox here**
    sprite('ag403_10', 2)	# 20-21
    sprite('ag403_09', 2)	# 22-23	 **attackbox here**
    sprite('ag403_10', 2)	# 24-25
    sprite('ag403_09', 2)	# 26-27	 **attackbox here**
    sprite('ag403_10', 2)	# 28-29
    sprite('ag403_09', 2)	# 30-31	 **attackbox here**
    sprite('ag403_10', 2)	# 32-33
    sprite('ag403_09', 3)	# 34-36	 **attackbox here**
    Unknown21015('4761746c696e675f4d61746f6d65000000000000000000000000000000000000be0f000000000000')
    sprite('ag403_10', 3)	# 37-39
    sprite('ag403_09', 3)	# 40-42	 **attackbox here**
    sprite('ag403_10', 3)	# 43-45
    sprite('ag403_11', 5)	# 46-50
    Recovery()
    sprite('ag403_12', 5)	# 51-55
    sprite('ag403_13', 5)	# 56-60
    sprite('ag403_14', 5)	# 61-65

@State
def MachineGunB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('ag403_00', 3)	# 1-3
    sprite('ag403_01', 3)	# 4-6
    sprite('ag403_02', 3)	# 7-9
    SFX_3('ag001')
    Unknown7007('7061673230355f300000000000000000640000007061673230355f310000000000000000640000007061673230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag403_03', 5)	# 10-14
    sprite('ag403_04', 3)	# 15-17
    sprite('ag403_05', 2)	# 18-19
    sprite('ag403_06', 2)	# 20-21
    sprite('ag403_07', 2)	# 22-23
    sprite('ag403_08', 2)	# 24-25
    sprite('ag403_09', 2)	# 26-27	 **attackbox here**
    GFX_0('Gatling_Matome', 100)
    sprite('ag403_10', 2)	# 28-29
    sprite('ag403_09', 2)	# 30-31	 **attackbox here**
    sprite('ag403_10', 2)	# 32-33
    sprite('ag403_09', 2)	# 34-35	 **attackbox here**
    sprite('ag403_10', 2)	# 36-37
    sprite('ag403_09', 2)	# 38-39	 **attackbox here**
    sprite('ag403_10', 2)	# 40-41
    sprite('ag403_09', 2)	# 42-43	 **attackbox here**
    sprite('ag403_10', 2)	# 44-45
    sprite('ag403_09', 2)	# 46-47	 **attackbox here**
    sprite('ag403_10', 2)	# 48-49
    sprite('ag403_09', 2)	# 50-51	 **attackbox here**
    sprite('ag403_10', 2)	# 52-53
    sprite('ag403_09', 1)	# 54-54	 **attackbox here**
    sprite('ag403_09', 1)	# 55-55	 **attackbox here**
    sendToLabelUpon(24, 1)
    sprite('ag403_10', 2)	# 56-57
    sprite('ag403_09', 2)	# 58-59	 **attackbox here**
    sprite('ag403_10', 2)	# 60-61
    sprite('ag403_09', 2)	# 62-63	 **attackbox here**
    sprite('ag403_10', 2)	# 64-65
    sprite('ag403_09', 2)	# 66-67	 **attackbox here**
    sprite('ag403_10', 2)	# 68-69
    sprite('ag403_09', 2)	# 70-71	 **attackbox here**
    sprite('ag403_10', 2)	# 72-73
    sprite('ag403_09', 2)	# 74-75	 **attackbox here**
    sprite('ag403_10', 2)	# 76-77
    sprite('ag403_09', 2)	# 78-79	 **attackbox here**
    sprite('ag403_10', 2)	# 80-81
    sprite('ag403_09', 2)	# 82-83	 **attackbox here**
    sprite('ag403_10', 2)	# 84-85
    sprite('ag403_09', 3)	# 86-88	 **attackbox here**
    Unknown21015('4761746c696e675f4d61746f6d65000000000000000000000000000000000000be0f000000000000')
    clearUponHandler(24)
    sprite('ag403_10', 3)	# 89-91
    sprite('ag403_09', 3)	# 92-94	 **attackbox here**
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('ag403_09', 3)	# 95-97	 **attackbox here**
    Unknown21015('4761746c696e675f4d61746f6d65000000000000000000000000000000000000be0f000000000000')
    clearUponHandler(24)
    label(9)
    sprite('ag403_10', 3)	# 98-100
    sprite('ag403_09', 3)	# 101-103	 **attackbox here**
    sprite('ag403_10', 3)	# 104-106
    sprite('ag403_11', 5)	# 107-111
    Recovery()
    sprite('ag403_12', 5)	# 112-116
    sprite('ag403_13', 5)	# 117-121
    sprite('ag403_14', 5)	# 122-126

@State
def AirMachineGunA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(6, 1)
    sprite('ag207_00', 2)	# 1-2
    Unknown1084(1)
    physicsXImpulse(-2000)
    physicsYImpulse(20000)
    Unknown1043()
    GFX_0('agef207_burner_turn', 0)
    GFX_0('agef207_burner_turn_back', 1)
    sprite('ag207_01', 1)	# 3-3
    sprite('ag207_01', 1)	# 4-4
    SFX_3('ag007')
    sprite('ag207_02', 2)	# 5-6
    callSubroutine('Burner_Delete')
    sprite('ag207_03', 2)	# 7-8
    sprite('ag207_04', 2)	# 9-10
    sprite('ag207_05', 2)	# 11-12
    sprite('ag207_06', 2)	# 13-14
    sprite('ag207_07', 4)	# 15-18
    Unknown1007(-30000)
    Unknown1084(1)
    GFX_0('agef207_burner', 2)
    GFX_0('agef207_burner_back', 3)
    sprite('ag207_08', 4)	# 19-22
    GFX_0('AirBalkan_Matome', 100)
    Unknown7007('7061673230315f300000000000000000640000007061673230315f310000000000000000640000007061673331335f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag207_07', 4)	# 23-26
    sprite('ag207_08', 4)	# 27-30
    sprite('ag207_07', 4)	# 31-34
    sprite('ag207_08', 4)	# 35-38
    sprite('ag207_07', 4)	# 39-42
    Unknown21015('41697242616c6b616e5f4d61746f6d6500000000000000000000000000000000e60f000000000000')
    sprite('ag207_08', 4)	# 43-46
    sprite('ag207_07', 4)	# 47-50
    callSubroutine('Burner_Delete')
    physicsXImpulse(-2000)
    Unknown1043()
    sprite('ag207_08', 4)	# 51-54
    sprite('ag207_07', 4)	# 55-58
    sprite('ag020_04', 3)	# 59-61

@State
def AirMachineGunB():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ag207_00', 2)	# 1-2
    Unknown1084(1)
    physicsXImpulse(-6000)
    physicsYImpulse(24000)
    Unknown1043()
    GFX_0('agef207_burner_turn', 0)
    GFX_0('agef207_burner_turn_back', 1)
    sprite('ag207_01', 1)	# 3-3
    sprite('ag207_01', 2)	# 4-5
    SFX_3('ag007')
    sprite('ag207_02', 3)	# 6-8
    callSubroutine('Burner_Delete')
    sprite('ag207_03', 4)	# 9-12
    sprite('ag207_04', 4)	# 13-16
    sprite('ag207_05', 4)	# 17-20
    sprite('ag207_06', 4)	# 21-24
    sprite('ag207_07', 4)	# 25-28
    Unknown1019(30)
    YAccel(30)
    Unknown1039(30)
    GFX_0('agef207_burner', 2)
    GFX_0('agef207_burner_back', 3)
    sprite('ag207_08', 4)	# 29-32
    GFX_0('AirBalkan_Matome', 100)
    Unknown7007('7061673230315f300000000000000000640000007061673230315f310000000000000000640000007061673331335f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag207_07', 4)	# 33-36
    sprite('ag207_08', 4)	# 37-40
    sprite('ag207_07', 4)	# 41-44
    sprite('ag207_08', 4)	# 45-48
    sprite('ag207_07', 4)	# 49-52
    sprite('ag207_08', 4)	# 53-56
    sprite('ag207_07', 4)	# 57-60
    sprite('ag207_08', 4)	# 61-64
    sprite('ag207_07', 4)	# 65-68
    Unknown21015('41697242616c6b616e5f4d61746f6d6500000000000000000000000000000000e60f000000000000')
    sprite('ag020_04', 3)	# 69-71
    sprite('ag020_05', 4)	# 72-75
    sprite('ag020_06', 2)	# 76-77
    label(0)
    sprite('ag020_07', 4)	# 78-81
    sprite('ag020_08', 4)	# 82-85
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag231_01', 2)	# 86-87
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown21015('41697242616c6b616e5f4d61746f6d6500000000000000000000000000000000e60f000000000000')
    callSubroutine('Burner_Delete')
    sprite('ag231_00', 8)	# 88-95
    sprite('ag231_01', 2)	# 96-97
    sprite('ag010_02', 2)	# 98-99
    sprite('ag010_01', 4)	# 100-103
    sprite('ag010_00', 4)	# 104-107

@State
def CannonA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ag404_00', 3)	# 1-3
    sprite('ag404_01', 3)	# 4-6
    SFX_3('ag001')
    Unknown7007('7061673230375f300000000000000000640000007061673230375f310000000000000000640000007061673230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag404_02', 3)	# 7-9
    sprite('ag404_03', 3)	# 10-12
    sprite('ag404_04', 3)	# 13-15
    sprite('ag404_05', 3)	# 16-18
    SFX_0('200_walk_normal_2')
    sprite('ag404_06', 3)	# 19-21
    SFX_0('200_walk_normal_2')
    sprite('ag404_07', 3)	# 22-24
    sprite('ag404_08', 3)	# 25-27
    GFX_1('agef_emptysmoke_00', 0)
    GFX_1('agef_canonshot_05', 0)
    GFX_0('CanonShot_A', 0)
    SFX_3('ag005')
    Unknown8004(100, 1, 1)
    sprite('ag404_09', 3)	# 28-30
    sprite('ag404_06', 3)	# 31-33
    sprite('ag404_07', 3)	# 34-36
    sprite('ag404_06', 3)	# 37-39
    sprite('ag404_07', 3)	# 40-42
    sprite('ag404_06', 3)	# 43-45
    sprite('ag404_10', 3)	# 46-48
    sprite('ag404_11', 3)	# 49-51
    sprite('ag404_12', 3)	# 52-54
    sprite('ag404_13', 3)	# 55-57
    sprite('ag404_00', 3)	# 58-60

@State
def CannonB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ag404_00', 3)	# 1-3
    sprite('ag404_01', 3)	# 4-6
    SFX_3('ag001')
    Unknown7007('7061673230375f300000000000000000640000007061673230375f310000000000000000640000007061673230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag404_02', 3)	# 7-9
    sprite('ag404_03', 3)	# 10-12
    sprite('ag404_04', 3)	# 13-15
    sprite('ag404_05', 3)	# 16-18
    SFX_0('200_walk_normal_2')
    sprite('ag404_06', 3)	# 19-21
    SFX_0('200_walk_normal_2')
    sprite('ag404_07', 3)	# 22-24
    sprite('ag404_06', 3)	# 25-27
    sprite('ag404_07', 3)	# 28-30
    sprite('ag404_06', 3)	# 31-33
    sprite('ag404_07', 3)	# 34-36
    sprite('ag404_08', 3)	# 37-39
    GFX_1('agef_emptysmoke_00', 0)
    GFX_1('agef_canonshot_05', 0)
    GFX_0('CanonShot_B', 0)
    SFX_3('ag005')
    Unknown8004(100, 1, 1)
    sprite('ag404_09', 3)	# 40-42
    sprite('ag404_10', 3)	# 43-45
    sprite('ag404_11', 3)	# 46-48
    sprite('ag404_12', 3)	# 49-51
    sprite('ag404_13', 3)	# 52-54
    sprite('ag404_00', 3)	# 55-57

@State
def AirCannonA():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('ag411_00', 3)	# 1-3
    GFX_0('agef_aircanon_burner', 0)
    GFX_0('agef_aircanon_burner_back', 1)
    sprite('ag411_01', 2)	# 4-5
    SFX_3('ag001')
    Unknown1019(80)
    YAccel(60)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown22004(6, 1)
    sprite('ag411_02', 3)	# 6-8
    sprite('ag411_03', 3)	# 9-11
    SFX_0('200_walk_normal_2')
    sprite('ag411_04', 3)	# 12-14
    sprite('ag411_03', 3)	# 15-17
    SFX_0('200_walk_normal_2')
    sprite('ag411_04', 3)	# 18-20
    sprite('ag411_05', 4)	# 21-24
    GFX_1('agef_emptysmoke_00', 2)
    Unknown4048(32000)
    Unknown4045('616765665f63616e6f6e73686f745f303500000000000000000000000000000002000000')
    GFX_0('AirCanonShot_A', 2)
    SFX_3('ag005')
    sprite('ag411_06', 4)	# 25-28
    WhiffCancelEnable(1)
    sprite('ag411_03', 3)	# 29-31
    sprite('ag411_04', 3)	# 32-34
    sprite('ag411_07', 3)	# 35-37
    sprite('ag411_08', 3)	# 38-40
    callSubroutine('Burner_Delete')
    sprite('ag411_09', 3)	# 41-43
    sprite('ag411_10', 3)	# 44-46
    WhiffCancelEnable(0)
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(70)
    YAccel(70)
    callSubroutine('Burner_Delete')
    sprite('ag411_11', 3)	# 47-49
    sprite('ag411_00', 3)	# 50-52

@State
def AirCannonB():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('ag411_00', 3)	# 1-3
    GFX_0('agef_aircanon_burner', 0)
    GFX_0('agef_aircanon_burner_back', 1)
    sprite('ag411_01', 2)	# 4-5
    SFX_3('ag001')
    Unknown1019(80)
    YAccel(60)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown22004(6, 1)
    Unknown7006('ag335', 100, 859006817, 54, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ag411_02', 3)	# 6-8
    sprite('ag411_03', 3)	# 9-11
    SFX_0('200_walk_normal_2')
    sprite('ag411_04', 3)	# 12-14
    sprite('ag411_03', 3)	# 15-17
    SFX_0('200_walk_normal_2')
    sprite('ag411_04', 3)	# 18-20
    sprite('ag411_05', 4)	# 21-24
    GFX_1('agef_emptysmoke_00', 2)
    Unknown4048(32000)
    Unknown4045('616765665f63616e6f6e73686f745f303500000000000000000000000000000002000000')
    GFX_0('AirCanonShot_B', 2)
    SFX_3('ag005')
    sprite('ag411_06', 4)	# 25-28
    WhiffCancelEnable(1)
    sprite('ag411_03', 3)	# 29-31
    sprite('ag411_04', 3)	# 32-34
    sprite('ag411_07', 3)	# 35-37
    sprite('ag411_08', 3)	# 38-40
    callSubroutine('Burner_Delete')
    sprite('ag411_09', 3)	# 41-43
    sprite('ag411_10', 3)	# 44-46
    WhiffCancelEnable(0)
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(70)
    YAccel(70)
    callSubroutine('Burner_Delete')
    sprite('ag411_11', 3)	# 47-49
    sprite('ag411_00', 3)	# 50-52

@State
def MegidoFire():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(80)
        AttackP2(75)
        AirUntechableTime(32)
        AirPushbackX(2000)
        Unknown30055('000000003c00000000000000')
        Unknown30056('c0f2fcff3c00000000000000')
        YImpluseBeforeWallbounce(1800)
        Hitstop(7)
        Unknown9017(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11044(1)
        Unknown11069('PAG_PersonaRollingEX')
        Unknown30065(0)
        Unknown11091(10)
        Unknown11064(1)
        Unknown2073(1)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(100)

        def upon_11():
            SLOT_51 = 1
        clearUponHandler(2)

        def upon_LANDING():
            sendToLabel(9)
        if SLOT_37:
            Unknown23159('MegidoFire_Land')
            Unknown2037(1)
        if SLOT_36:
            Unknown23159('MegidoFire_Air')
    sprite('ag408_00', 3)	# 1-3
    sprite('ag408_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    if SLOT_2:
        physicsXImpulse(10000)
        physicsYImpulse(15000)
        setGravity(3000)
    else:
        physicsXImpulse(10000)
        physicsYImpulse(30000)
        setGravity(1500)
    Unknown7007('7061673231365f300000000000000000640000007061673231365f310000000000000000640000007061673231365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag408_02', 3)	# 7-9
    if SLOT_2:
        physicsXImpulse(20000)
        setGravity(500)
    else:
        pass
    sprite('ag408_03', 3)	# 10-12
    GFX_0('FlamethrowerStart', 0)
    GFX_0('FlamethrowerStart', 1)
    GFX_0('FlamethrowerStart', 2)
    GFX_0('FlamethrowerStart', 3)
    label(0)
    sprite('ag408_04', 3)	# 13-15	 **attackbox here**
    GFX_0('FlamethrowerD', 0)
    GFX_1('agef_rollfire_03', 1)
    GFX_1('agef_rollfire_03', 2)
    RefreshMultihit()
    SFX_0('015_blaze_2')
    sprite('ag408_05', 3)	# 16-18	 **attackbox here**
    GFX_1('agef_rollfire_03', 0)
    GFX_1('agef_rollfire_03', 1)
    sprite('ag408_06', 3)	# 19-21	 **attackbox here**
    GFX_1('agef_rollfire_03', 0)
    GFX_1('agef_rollfire_03', 1)
    sprite('ag408_07', 3)	# 22-24	 **attackbox here**
    GFX_1('agef_rollfire_03', 0)
    GFX_1('agef_rollfire_03', 1)
    RefreshMultihit()
    sprite('ag408_08', 3)	# 25-27	 **attackbox here**
    GFX_1('agef_rollfire_03', 0)
    GFX_1('agef_rollfire_03', 1)
    sprite('ag408_09', 3)	# 28-30	 **attackbox here**
    GFX_1('agef_rollfire_03', 0)
    GFX_1('agef_rollfire_03', 1)
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('ag408_12', 4)	# 31-34
    Unknown26('FlamethrowerD')
    GFX_1('agef_fireend_01', 0)
    setGravity(800)
    Unknown2017(0)
    Unknown23029(11, 1040, 0)
    sprite('ag020_04', 3)	# 35-37
    sprite('ag020_05', 4)	# 38-41
    sprite('ag020_06', 2)	# 42-43
    label(1)
    sprite('ag020_07', 4)	# 44-47
    Unknown1043()
    sprite('ag020_08', 4)	# 48-51
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ag231_01', 2)	# 52-53
    Unknown26('FlamethrowerD')
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 2)	# 54-55
    sprite('ag231_01', 2)	# 56-57
    sprite('ag010_02', 2)	# 58-59
    sprite('ag010_01', 2)	# 60-61
    sprite('ag010_00', 2)	# 62-63

@State
def Pandora():

    def upon_IMMEDIATE():
        Unknown17003()
        if SLOT_37:
            Unknown2038(1)
    sprite('ag410_00', 3)	# 1-3
    GFX_0('agef_missile_burner', 0)
    GFX_0('agef_missile_burner_back', 1)
    Unknown1084(1)
    sprite('ag410_01', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    physicsXImpulse(-7000)
    physicsYImpulse(700)
    setGravity(0)
    Unknown2015(250)
    if SLOT_2:
        Unknown7006('pag218_0', 100, 845635952, 828323889, 0, 0, 100, 845635952, 845101105, 0, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown7006('pag219_0', 100, 845635952, 828324145, 0, 0, 100, 845635952, 845101361, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ag410_02', 2)	# 6-7
    sprite('ag410_03', 2)	# 8-9
    sprite('ag410_04', 2)	# 10-11
    sprite('ag410_05', 2)	# 12-13
    sprite('ag410_06', 2)	# 14-15
    sprite('ag410_07', 2)	# 16-17
    sprite('ag410_08', 3)	# 18-20
    GFX_0('Pandora_Matome', 100)
    Unknown1015(-10000)
    Unknown1028(200)
    Unknown14070('CancelOrgiaDash')
    sprite('ag410_09', 3)	# 21-23
    sprite('ag410_08', 3)	# 24-26
    sprite('ag410_09', 3)	# 27-29
    sprite('ag410_08', 3)	# 30-32
    sprite('ag410_09', 3)	# 33-35
    sprite('ag410_08', 3)	# 36-38
    sprite('ag410_09', 3)	# 39-41
    sprite('ag410_08', 3)	# 42-44
    sprite('ag410_09', 3)	# 45-47
    Unknown14072('CancelOrgiaDash')
    sprite('ag410_08', 3)	# 48-50
    sprite('ag410_09', 3)	# 51-53
    sprite('ag410_08', 3)	# 54-56
    sprite('ag410_09', 3)	# 57-59
    sprite('ag410_08', 3)	# 60-62
    sprite('ag410_09', 3)	# 63-65
    Unknown21015('50616e646f72615f4d61746f6d650000000000000000000000000000000000000410000000000000')
    sprite('ag410_08', 3)	# 66-68
    sprite('ag410_09', 3)	# 69-71
    Unknown1019(30)
    Unknown1028(0)
    sprite('ag410_10', 2)	# 72-73
    sprite('ag410_11', 2)	# 74-75
    sprite('ag410_04', 2)	# 76-77
    sprite('ag410_03', 2)	# 78-79
    sprite('ag410_02', 2)	# 80-81
    sprite('ag410_01', 2)	# 82-83
    sprite('ag410_00', 2)	# 84-85
    callSubroutine('Burner_Delete')
    sprite('ag020_04', 3)	# 86-88
    Unknown1084(1)
    Unknown1043()
    sprite('ag020_05', 4)	# 89-92
    sprite('ag020_06', 2)	# 93-94
    label(0)
    sprite('ag020_07', 4)	# 95-98
    sprite('ag020_08', 4)	# 99-102
    loopRest()
    gotoLabel(0)

@State
def OrgiaDash():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        setGravity(0)

        def upon_STATE_END():
            callSubroutine('Burner_Delete')
            if (not SLOT_30):
                setGravity(2000)
        loopRelated(17, 60)

        def upon_17():
            sendToLabel(9)
        if SLOT_93:
            SLOT_31 = (SLOT_31 + (-1500))
        else:
            Unknown30068(1)
            SLOT_31 = (SLOT_31 + (-1500))
    sprite('ag405_03', 3)	# 1-3
    Unknown1084(1)
    sprite('ag406_00', 3)	# 4-6

    def upon_3():
        if (SLOT_23 <= 100000):
            physicsYImpulse(13000)
        else:
            clearUponHandler(3)
            physicsYImpulse(0)
    Unknown7007('7061673231325f300000000000000000640000007061673231325f310000000000000000640000007061673231325f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown3029(1)
    sprite('ag406_01', 1)	# 7-7
    physicsXImpulse(24000)
    loopRest()
    label(0)
    sprite('ag406_01', 4)	# 8-11
    Unknown13014(1)
    Unknown13015(1)
    clearUponHandler(3)

    def upon_3():
        if CheckInput(0x93):
            Unknown2037(8)
            Unknown1021(3000)
        elif CheckInput(0x45):
            Unknown2037(2)
            Unknown1021(-3000)
        elif CheckInput(0x5f):
            sendToLabel(9)
        else:
            Unknown2037(0)
            if (SLOT_13 < (-1500)):
                Unknown1021(1500)
            if (SLOT_13 > 1500):
                Unknown1021(-1500)
            if (SLOT_13 >= (-1500)):
                if (SLOT_13 <= 1500):
                    physicsYImpulse(0)
        if (SLOT_13 >= 12000):
            SLOT_13 = 12000
        if (SLOT_13 <= (-12000)):
            SLOT_13 = (-12000)
        Unknown1015(300)
        if (SLOT_12 >= 36000):
            SLOT_12 = 36000
        SLOT_31 = (SLOT_31 + (-15))
        if (not SLOT_31):
            sendToLabel(9)
    callSubroutine('Burner_Delete')
    if (SLOT_2 == 2):
        GFX_0('agef_orgia_dash_down', 0)
        GFX_0('agef_orgia_dash_down_back', 1)
        GFX_0('agef_orgia_dash_down_back2', 2)
    elif (SLOT_2 == 8):
        GFX_0('agef_orgia_dash_up', 0)
        GFX_0('agef_orgia_dash_up_back', 1)
        GFX_0('agef_orgia_dash_up_back2', 2)
    else:
        GFX_0('agef_orgia_dash', 0)
        GFX_0('agef_orgia_dash_back', 1)
        GFX_0('agef_orgia_dash_back2', 2)
    SFX_3('blaze_normal')
    sprite('ag406_02', 4)	# 12-15
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag406_00', 4)	# 16-19
    callSubroutine('Burner_Delete')
    Unknown3029(0)
    Unknown1019(50)
    setGravity(2000)
    clearUponHandler(3)
    clearUponHandler(17)
    sprite('ag405_02', 4)	# 20-23

@State
def AthenaSurfing():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        setInvincible(1)
        Unknown2003(1)
        Unknown4020(11)
        Unknown4009(11)
        SLOT_2 = SLOT_36

        def upon_43():
            if (SLOT_48 == 5010):
                clearUponHandler(43)
                Unknown2017(1)
                Unknown4020(0)
                sendToLabel(2)
        clearUponHandler(2)
    sprite('ag430_00', 3)	# 1-3
    Unknown23183('61673433305f3135000000000000000000000000000000000000000000000000030000000200000002000000')
    sprite('ag430_00', 8)	# 4-11
    Unknown23183('61673433305f3135000000000000000000000000000000000000000000000000080000000200000002000000')
    Unknown23029(11, 1060, 0)
    Unknown1084(1)
    Unknown2036(58, -1, 0)
    Unknown2058(-10000)
    tag_voice(1, 'pag251_0', 'pag251_1', '', '')
    Unknown30080('')
    sendToLabelUpon(2, 9)
    sprite('ag430_01', 6)	# 12-17
    teleportRelativeX(20000)
    sprite('ag430_02', 6)	# 18-23
    physicsXImpulse(-5000)
    physicsYImpulse(26000)
    setGravity(1700)
    sprite('ag430_03', 6)	# 24-29
    sprite('ag430_04', 6)	# 30-35
    sprite('ag430_05', 6)	# 36-41
    sprite('ag430_06', 4)	# 42-45
    Unknown1019(60)
    YAccel(60)
    setGravity(0)
    GFX_0('agef_surfing_burner_hold', 0)
    GFX_0('agef_surfing_burner_hold_back', 1)
    sprite('ag430_07', 4)	# 46-49
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 50-53
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 54-57
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 58-61
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 62-65
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 66-69
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_08', 3)	# 70-72
    Unknown13024(1)
    Unknown7007('7061673235325f300000000000000000640000007061673235345f300000000000000000640000007061673235325f310000000000000000640000007061673235345f31000000000000000064000000')
    SFX_0('019_quake_0')
    GuardPoint_(1)
    physicsXImpulse(5000)
    Unknown1028(4500)
    Unknown2017(0)
    callSubroutine('Burner_Delete')
    GFX_0('agef_surfing_burner', 0)
    GFX_0('agef_surfing_burner_back', 1)
    sprite('ag430_09', 3)	# 73-75
    sprite('ag430_08', 3)	# 76-78
    sprite('ag430_09', 3)	# 79-81
    sprite('ag430_08', 3)	# 82-84
    sprite('ag430_09', 3)	# 85-87
    sprite('ag430_08', 3)	# 88-90
    sprite('ag430_10', 2)	# 91-92
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 93-95
    Unknown1019(60)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 96-98
    Unknown1019(70)
    Unknown2017(1)
    sprite('ag430_11', 3)	# 99-101
    Unknown1019(70)
    sprite('ag430_12', 3)	# 102-104
    Unknown1019(70)
    sprite('ag430_11', 3)	# 105-107
    Unknown1019(70)
    sprite('ag430_13', 6)	# 108-113
    setGravity(2000)
    sprite('ag430_14', 6)	# 114-119
    sprite('ag020_04', 3)	# 120-122
    sprite('ag020_05', 4)	# 123-126
    sprite('ag020_06', 2)	# 127-128
    clearUponHandler(3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ag430_10', 2)	# 129-130
    physicsXImpulse(70000)
    setGravity(0)
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 131-133
    Unknown1019(80)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 134-136
    Unknown1019(90)
    sprite('ag430_11', 3)	# 137-139
    Unknown1019(90)
    sprite('ag430_12', 3)	# 140-142
    Unknown1019(70)
    sprite('ag430_11', 3)	# 143-145
    Unknown1019(60)
    sprite('ag430_12', 3)	# 146-148
    Unknown1019(50)
    sprite('ag430_13', 6)	# 149-154
    Unknown1019(60)
    setGravity(1000)
    Unknown2017(1)
    sprite('ag430_14', 1)	# 155-155
    sprite('ag430_14', 6)	# 156-161
    sprite('ag020_04', 3)	# 162-164
    sprite('ag020_05', 4)	# 165-168
    sprite('ag020_06', 2)	# 169-170
    loopRest()
    gotoLabel(1)
    label(1)
    sprite('ag020_07', 4)	# 171-174
    callSubroutine('Burner_Delete')
    sprite('ag020_08', 4)	# 175-178
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ag231_01', 2)	# 179-180
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 4)	# 181-184
    sprite('ag231_01', 2)	# 185-186
    sprite('ag010_02', 2)	# 187-188
    sprite('ag010_01', 4)	# 189-192
    sprite('ag010_00', 4)	# 193-196

@State
def AthenaSurfingOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        setInvincible(1)
        Unknown2003(1)
        Unknown4020(11)
        Unknown4009(11)
        SLOT_2 = SLOT_36

        def upon_43():
            if (SLOT_48 == 5010):
                sendToLabel(2)
                Unknown2017(1)
                Unknown4020(0)
            if (SLOT_48 == 5011):
                Unknown13024(0)
                enterState('UltimateSpear')
        clearUponHandler(2)
    sprite('ag430_00', 3)	# 1-3
    Unknown23183('61673433305f3135000000000000000000000000000000000000000000000000030000000200000002000000')
    sprite('ag430_00', 8)	# 4-11
    Unknown23183('61673433305f3135000000000000000000000000000000000000000000000000080000000200000002000000')
    Unknown23029(11, 1061, 0)
    Unknown1084(1)
    Unknown2036(58, -1, 0)
    Unknown2058(-10000)
    tag_voice(1, 'pag251_0', 'pag251_1', '', '')
    Unknown30080('')
    sendToLabelUpon(2, 9)
    sprite('ag430_01', 6)	# 12-17
    teleportRelativeX(20000)
    sprite('ag430_02', 6)	# 18-23
    physicsXImpulse(-5000)
    physicsYImpulse(26000)
    setGravity(1700)
    sprite('ag430_03', 6)	# 24-29
    sprite('ag430_04', 6)	# 30-35
    sprite('ag430_05', 6)	# 36-41
    sprite('ag430_06', 4)	# 42-45
    Unknown1019(60)
    YAccel(60)
    setGravity(0)
    GFX_0('agef_surfing_burner_hold', 0)
    GFX_0('agef_surfing_burner_hold_back', 1)
    sprite('ag430_07', 4)	# 46-49
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 50-53
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 54-57
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 58-61
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 62-65
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 66-69
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_08', 3)	# 70-72
    Unknown13024(1)
    Unknown7007('7061673235325f300000000000000000640000007061673235345f300000000000000000640000007061673235325f310000000000000000640000007061673235345f31000000000000000064000000')
    SFX_0('019_quake_0')
    GuardPoint_(1)
    physicsXImpulse(5000)
    Unknown1028(4500)
    Unknown2017(0)
    callSubroutine('Burner_Delete')
    GFX_0('agef_surfing_burner', 0)
    GFX_0('agef_surfing_burner_back', 1)
    sprite('ag430_09', 3)	# 73-75
    sprite('ag430_08', 3)	# 76-78
    sprite('ag430_09', 3)	# 79-81
    sprite('ag430_08', 3)	# 82-84
    sprite('ag430_09', 3)	# 85-87
    sprite('ag430_08', 3)	# 88-90
    sprite('ag430_10', 2)	# 91-92
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 93-95
    Unknown1019(60)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 96-98
    Unknown1019(70)
    Unknown2017(1)
    sprite('ag430_11', 3)	# 99-101
    Unknown1019(70)
    sprite('ag430_12', 3)	# 102-104
    Unknown1019(70)
    sprite('ag430_11', 3)	# 105-107
    Unknown1019(70)
    sprite('ag430_13', 6)	# 108-113
    setGravity(2000)
    sprite('ag430_14', 6)	# 114-119
    sprite('ag020_04', 3)	# 120-122
    sprite('ag020_05', 4)	# 123-126
    sprite('ag020_06', 2)	# 127-128
    clearUponHandler(3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ag430_10', 2)	# 129-130
    physicsXImpulse(70000)
    setGravity(0)
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 131-133
    Unknown1019(80)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 134-136
    Unknown1019(90)
    sprite('ag430_11', 3)	# 137-139
    Unknown1019(90)
    sprite('ag430_12', 3)	# 140-142
    Unknown1019(70)
    sprite('ag430_11', 3)	# 143-145
    Unknown1019(60)
    sprite('ag430_12', 3)	# 146-148
    Unknown1019(50)
    sprite('ag430_13', 6)	# 149-154
    Unknown1019(60)
    setGravity(1000)
    Unknown2017(1)
    sprite('ag430_14', 1)	# 155-155
    sprite('ag430_14', 6)	# 156-161
    sprite('ag020_04', 3)	# 162-164
    sprite('ag020_05', 4)	# 165-168
    sprite('ag020_06', 2)	# 169-170
    loopRest()
    gotoLabel(1)
    label(1)
    sprite('ag020_07', 4)	# 171-174
    callSubroutine('Burner_Delete')
    sprite('ag020_08', 4)	# 175-178
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ag231_01', 2)	# 179-180
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 4)	# 181-184
    sprite('ag231_01', 2)	# 185-186
    sprite('ag010_02', 2)	# 187-188
    sprite('ag010_01', 4)	# 189-192
    sprite('ag010_00', 4)	# 193-196

@State
def UltimateSpear():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        setInvincible(1)
        GuardPoint_(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        if Unknown23145('AthenaSurfingDDD'):
            Unknown2037(1)
        if Unknown23145('AthenaSurfingDDDOD'):
            Unknown2037(1)
        Unknown30068(1)

        def upon_3():
            Unknown48('19000000020000003400000016000000020000001e000000')
            if (not SLOT_52):
                setInvincible(0)
    sprite('ag430_10', 2)	# 1-2
    Unknown2036(58, -1, 0)
    physicsXImpulse(50000)
    if SLOT_2:
        Unknown23029(11, 1065, 0)
    else:
        Unknown23029(11, 1062, 0)
    sprite('ag430_11', 3)	# 3-5
    Unknown1019(50)
    sprite('ag430_13', 3)	# 6-8
    Unknown1019(50)
    sprite('ag431_00', 3)	# 9-11
    Unknown1019(50)
    tag_voice(1, 'pag255_0', 'pag255_1', 'pag257_0', 'pag257_1')
    sprite('ag431_00', 40)	# 12-51
    Unknown1084(1)
    Unknown23024(2)
    sprite('ag431_01', 3)	# 52-54
    sprite('ag431_02', 4)	# 55-58
    sprite('ag431_03', 4)	# 59-62
    physicsXImpulse(-2000)
    physicsYImpulse(8000)
    setGravity(30)
    tag_voice(0, 'pag256_0', 'pag256_1', 'pag258_0', 'pag258_1')
    sprite('ag431_04', 4)	# 63-66
    sprite('ag431_05', 4)	# 67-70
    sprite('ag431_04', 4)	# 71-74
    Unknown1084(1)
    sprite('ag431_05', 4)	# 75-78
    sprite('ag431_04', 4)	# 79-82
    sprite('ag431_05', 4)	# 83-86
    sprite('ag431_04', 4)	# 87-90
    sprite('ag431_05', 4)	# 91-94
    sprite('ag431_04', 4)	# 95-98
    sprite('ag431_05', 4)	# 99-102
    sprite('ag431_04', 4)	# 103-106
    sprite('ag431_05', 4)	# 107-110
    sprite('ag431_04', 4)	# 111-114
    sprite('ag431_05', 4)	# 115-118
    sprite('ag431_04', 4)	# 119-122
    sprite('ag431_05', 4)	# 123-126
    sprite('ag431_04', 4)	# 127-130
    setGravity(500)
    sprite('ag431_05', 4)	# 131-134
    sprite('ag431_06', 4)	# 135-138
    sprite('ag431_07', 4)	# 139-142
    sprite('ag431_08', 4)	# 143-146
    sprite('ag020_04', 3)	# 147-149
    Unknown1043()
    sprite('ag020_05', 4)	# 150-153
    sprite('ag020_06', 2)	# 154-155
    label(0)
    sprite('ag020_07', 4)	# 156-159
    Unknown1039(200)
    sprite('ag020_08', 4)	# 160-163
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag611_00', 6)	# 164-169
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag611_01', 10)	# 170-179
    sprite('ag611_02', 6)	# 180-185
    sprite('ag611_03', 20)	# 186-205
    sprite('ag611_02', 6)	# 206-211
    sprite('ag611_01', 6)	# 212-217
    sprite('ag611_00', 6)	# 218-223

@State
def UltimateAirThrow():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAirThrow_Exe', 3, 1, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11032('e093040000000000400d0300c0f2fcff')
        Unknown11054(300000)
        Unknown11002(-1)
        Unknown30061(1)
        Unknown11082(1)

        def upon_3():
            if (SLOT_18 == 15):
                Unknown2036(65, -1, 0)
                Unknown2058(-10000)
                Unknown30080('')
            if SLOT_51:
                if (SLOT_29 < 350000):
                    sendToLabel(2)
                    SLOT_51 = 0
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        callSubroutine('Burner_Delete')
        if SLOT_37:
            Unknown23159('UltimateAirThrow_Land')
        if SLOT_36:
            Unknown23159('UltimateAirThrow_Air')
    if SLOT_36:
        _gotolabel(0)
    sprite('ag407_00', 2)	# 1-2
    setInvincible(1)
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    Unknown1084(1)
    SFX_3('ag006')
    sprite('ag407_01', 2)	# 3-4
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    physicsXImpulse(-10000)
    physicsYImpulse(10000)
    sprite('ag407_02', 2)	# 5-6
    tag_voice(1, 'pag259_0', 'pag260_0', '', '')
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_03', 2)	# 7-8
    callSubroutine('Burner_Delete')
    sprite('ag407_02', 2)	# 9-10
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_03', 2)	# 11-12
    callSubroutine('Burner_Delete')
    sprite('ag407_02', 2)	# 13-14
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_03', 2)	# 15-16
    callSubroutine('Burner_Delete')
    sprite('ag407_04', 3)	# 17-19
    Unknown1019(50)
    YAccel(50)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ag405_00', 2)	# 20-21
    setInvincible(1)
    Unknown1084(1)
    physicsYImpulse(2000)
    SFX_3('ag006')
    sprite('ag405_01', 2)	# 22-23
    sprite('ag405_02', 2)	# 24-25
    tag_voice(1, 'pag259_0', 'pag260_0', '', '')
    sprite('ag405_03', 2)	# 26-27
    GFX_0('agef_orgia_hovering', 0)
    GFX_0('agef_orgia_hovering_back', 1)
    GFX_0('agef_orgia_hovering_back2', 2)
    sprite('ag405_04', 2)	# 28-29
    callSubroutine('Burner_Delete')
    sprite('ag405_03', 2)	# 30-31
    GFX_0('agef_orgia_hovering', 0)
    GFX_0('agef_orgia_hovering_back', 1)
    GFX_0('agef_orgia_hovering_back2', 2)
    sprite('ag405_04', 2)	# 32-33
    callSubroutine('Burner_Delete')
    sprite('ag405_02', 2)	# 34-35
    sprite('ag405_01', 2)	# 36-37
    Unknown1019(50)
    YAccel(50)
    sprite('ag405_00', 2)	# 38-39
    loopRest()
    label(1)
    sprite('ag020_04', 4)	# 40-43
    Unknown1019(50)
    YAccel(50)
    sprite('ag432_00', 3)	# 44-46
    Unknown1084(1)
    sprite('ag432_01', 3)	# 47-49
    SFX_3('ag000')
    sprite('ag432_02', 3)	# 50-52
    sprite('ag432_03', 42)	# 53-94
    sprite('ag432_04', 3)	# 95-97
    SFX_3('airdash_m')
    physicsXImpulse(30000)
    setGravity(0)
    callSubroutine('Burner_Delete')
    GFX_0('agef432_orgia_burner', 1)
    GFX_0('agef432_orgia_burner_back', 2)
    GFX_0('agef432_orgia_burner_3', 3)
    SLOT_51 = 1
    sprite('ag432_05', 3)	# 98-100
    sprite('ag432_04', 3)	# 101-103
    sprite('ag432_05', 3)	# 104-106
    gotoLabel(3)
    label(2)
    sprite('ag432_06', 3)	# 107-109
    sprite('ag432_07', 3)	# 110-112	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    RefreshMultihit()
    sprite('ag432_08', 4)	# 113-116	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    sprite('ag432_09', 4)	# 117-120
    label(3)
    sprite('ag432_10', 4)	# 121-124
    clearUponHandler(3)
    setInvincible(0)
    Unknown1019(80)
    YAccel(80)
    setGravity(1600)
    callSubroutine('Burner_Delete')
    tag_voice(0, 'pag261_0', 'pag261_1', '', '')
    sprite('ag432_11', 4)	# 125-128
    Unknown1019(80)
    YAccel(80)
    sprite('ag432_12', 4)	# 129-132
    Unknown1019(80)
    YAccel(80)
    sprite('ag020_04', 3)	# 133-135
    sprite('ag020_05', 4)	# 136-139
    sprite('ag020_06', 2)	# 140-141
    label(4)
    sprite('ag020_07', 4)	# 142-145
    sprite('ag020_08', 4)	# 146-149
    loopRest()
    gotoLabel(4)
    label(9)
    sprite('ag231_01', 2)	# 150-151
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 14)	# 152-165
    sprite('ag231_01', 2)	# 166-167
    sprite('ag010_02', 2)	# 168-169
    sprite('ag010_01', 4)	# 170-173
    sprite('ag010_00', 4)	# 174-177

@State
def UltimateAirThrow_Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(1000)
        Unknown11091(60)
        AttackP2(60)
        Hitstop(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(120)
        Unknown9178(1)
        Unknown9362(1)
        Unknown9364(120)
        Unknown11102(1)
        Unknown11069('Orion_Shot')
        Unknown23027()
        Unknown30048(1)
        Unknown2034(1)
        Unknown2053(1)
        Unknown2017(1)
        SLOT_51 = 4

        def upon_3():
            if SLOT_2:
                if (SLOT_25 <= 250000):
                    clearUponHandler(3)
                    sendToLabel(2)

        def upon_STATE_END():
            Unknown26('UltimateAirThrow_Camera')

        def upon_12():
            ScreenShake(50000, 10000)
            SFX_3('guard_hit_l')
            SFX_3('damage_hit_mh')
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        Unknown13024(0)
        Unknown30068(1)
    sprite('ag432_07', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown1084(1)
    GFX_0('agef432_orgia_burner', 1)
    GFX_0('agef432_orgia_burner_back', 2)
    GFX_0('agef432_orgia_burner_3', 3)
    Unknown7015()
    Unknown7014('ag007')
    GFX_0('UltimateAirThrow_Camera', 100)
    sprite('ag432_07', 3)	# 4-6	 **attackbox here**
    physicsXImpulse(90000)
    setGravity(0)
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    callSubroutine('Burner_Delete')
    GFX_0('agef432_orgia_burner', 1)
    Unknown21007(1, 32)
    GFX_0('agef432_orgia_burner_back', 2)
    Unknown21007(1, 32)
    GFX_0('agef432_orgia_burner_3', 3)
    Unknown21007(1, 32)
    Unknown21012('556c74696d6174654169725468726f775f43616d65726100000000000000000020000000')
    Unknown2037(1)
    sprite('ag432_08', 3)	# 7-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    label(1)
    sprite('ag432_07', 3)	# 10-12	 **attackbox here**
    Unknown7015()
    Unknown7014('ag007')
    if (not SLOT_52):
        Unknown1019(110)
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    sprite('ag432_08', 3)	# 13-15	 **attackbox here**
    if (not SLOT_52):
        Unknown1019(110)
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    if (SLOT_12 >= 515000):
        SLOT_52 = 1
        physicsXImpulse(515000)
    gotoLabel(1)
    label(2)
    sprite('ag432_07', 20)	# 16-35	 **attackbox here**
    Unknown1019(0)
    Unknown7015()
    clearUponHandler(55)
    RefreshMultihit()
    sprite('ag433_00', 4)	# 36-39
    Unknown1007(-30000)
    physicsXImpulse(-4000)
    callSubroutine('Burner_Delete')
    tag_voice(0, 'pag259_1', 'pag260_1', '', '')
    sprite('ag433_01', 4)	# 40-43
    Unknown1019(200)
    SFX_3('ag001')
    sprite('ag433_02', 5)	# 44-48
    GFX_0('agef432_orgia_burner', 0)
    Unknown21007(1, 33)
    GFX_0('agef432_orgia_burner_back', 1)
    Unknown21007(1, 33)
    sprite('ag433_03', 5)	# 49-53
    Unknown1019(500)
    sprite('ag433_04', 5)	# 54-58
    Unknown1019(30)
    sprite('ag433_05', 4)	# 59-62
    Unknown1019(50)
    sprite('ag433_05', 4)	# 63-66
    Unknown1019(50)
    sprite('ag433_06', 4)	# 67-70
    Unknown1019(0)
    label(4)
    sprite('ag433_06', 3)	# 71-73
    SFX_3('ag002')
    SFX_3('ag003')
    GFX_0('Orion_Shot', 0)
    GFX_0('Orion_Shot', 3)
    physicsXImpulse(-6000)
    physicsYImpulse(1500)
    sprite('ag433_07', 3)	# 74-76
    SFX_3('ag002')
    GFX_0('Orion_Shot', 1)
    GFX_0('Orion_Shot', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('ag433_08', 3)	# 77-79
    SFX_3('ag002')
    GFX_0('Orion_Shot', 0)
    GFX_0('Orion_Shot', 3)
    Unknown1019(50)
    YAccel(50)
    sprite('ag433_09', 2)	# 80-81
    SFX_3('ag002')
    GFX_0('Orion_Shot', 1)
    GFX_0('Orion_Shot', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('ag433_09', 1)	# 82-82
    if SLOT_51:
        SLOT_51 = (SLOT_51 + (-1))
        sendToLabel(4)
    sprite('ag433_06', 3)	# 83-85
    SFX_3('ag002')
    GFX_0('Orion_Shot', 0)
    Unknown23029(1, 6000, 0)
    sprite('ag433_10', 6)	# 86-91
    tag_voice(0, 'pag263_0', 'pag263_1', '', '')
    sprite('ag433_11', 6)	# 92-97
    Unknown13024(1)
    callSubroutine('Burner_Delete')
    sprite('ag433_12', 6)	# 98-103
    sprite('ag433_13', 6)	# 104-109
    setGravity(2000)
    Unknown26('UltimateAirThrow_Camera')
    sprite('ag020_04', 3)	# 110-112
    sprite('ag020_05', 4)	# 113-116
    sprite('ag020_06', 2)	# 117-118
    label(5)
    sprite('ag020_07', 4)	# 119-122
    sprite('ag020_08', 4)	# 123-126
    loopRest()
    gotoLabel(5)
    label(9)
    sprite('ag231_01', 2)	# 127-128
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 10)	# 129-138
    sprite('ag231_01', 2)	# 139-140
    sprite('ag010_02', 2)	# 141-142
    sprite('ag010_01', 4)	# 143-146
    sprite('ag010_00', 4)	# 147-150

@State
def UltimateAirThrowOD():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAirThrowOD_Exe', 5, 1, 0)
        Unknown23055('')
        AttackP1(80)
        Unknown11032('e093040000000000400d0300c0f2fcff')
        Unknown11054(300000)
        Unknown11002(-1)
        Unknown30061(1)
        Unknown11082(1)

        def upon_3():
            if (SLOT_18 == 15):
                Unknown2036(65, -1, 0)
                Unknown2058(-10000)
                Unknown30080('')
            if SLOT_51:
                if (SLOT_29 < 350000):
                    sendToLabel(2)
                    SLOT_51 = 0
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        callSubroutine('Burner_Delete')
        if SLOT_37:
            Unknown23159('UltimateAirThrowOD_Land')
        if SLOT_36:
            Unknown23159('UltimateAirThrowOD_Air')
    if SLOT_36:
        _gotolabel(0)
    sprite('ag407_00', 2)	# 1-2
    setInvincible(1)
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    Unknown1084(1)
    SFX_3('ag006')
    sprite('ag407_01', 2)	# 3-4
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    physicsXImpulse(-10000)
    physicsYImpulse(10000)
    sprite('ag407_02', 2)	# 5-6
    tag_voice(1, 'pag259_0', 'pag260_0', '', '')
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_03', 2)	# 7-8
    callSubroutine('Burner_Delete')
    sprite('ag407_02', 2)	# 9-10
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_03', 2)	# 11-12
    callSubroutine('Burner_Delete')
    sprite('ag407_02', 2)	# 13-14
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_03', 2)	# 15-16
    callSubroutine('Burner_Delete')
    sprite('ag407_04', 4)	# 17-20
    Unknown1019(50)
    YAccel(50)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ag405_00', 2)	# 21-22
    setInvincible(1)
    Unknown1084(1)
    physicsYImpulse(2000)
    SFX_3('ag006')
    sprite('ag405_01', 2)	# 23-24
    sprite('ag405_02', 2)	# 25-26
    tag_voice(1, 'pag259_0', 'pag260_0', '', '')
    sprite('ag405_03', 2)	# 27-28
    GFX_0('agef_orgia_hovering', 0)
    GFX_0('agef_orgia_hovering_back', 1)
    GFX_0('agef_orgia_hovering_back2', 2)
    sprite('ag405_04', 2)	# 29-30
    callSubroutine('Burner_Delete')
    sprite('ag405_03', 2)	# 31-32
    GFX_0('agef_orgia_hovering', 0)
    GFX_0('agef_orgia_hovering_back', 1)
    GFX_0('agef_orgia_hovering_back2', 2)
    sprite('ag405_04', 2)	# 33-34
    callSubroutine('Burner_Delete')
    sprite('ag405_02', 2)	# 35-36
    sprite('ag405_01', 2)	# 37-38
    Unknown1019(50)
    YAccel(50)
    sprite('ag405_00', 2)	# 39-40
    loopRest()
    label(1)
    sprite('ag020_04', 4)	# 41-44
    Unknown1019(50)
    YAccel(50)
    sprite('ag432_00', 3)	# 45-47
    Unknown1084(1)
    sprite('ag432_01', 3)	# 48-50
    SFX_3('ag000')
    sprite('ag432_02', 3)	# 51-53
    sprite('ag432_03', 42)	# 54-95
    SFX_1('ag339')
    sprite('ag432_04', 3)	# 96-98
    SFX_3('airdash_m')
    physicsXImpulse(30000)
    setGravity(0)
    callSubroutine('Burner_Delete')
    GFX_0('agef432_orgia_burner', 1)
    GFX_0('agef432_orgia_burner_back', 2)
    GFX_0('agef432_orgia_burner_3', 3)
    SLOT_51 = 1
    sprite('ag432_05', 3)	# 99-101
    sprite('ag432_04', 3)	# 102-104
    sprite('ag432_05', 3)	# 105-107
    gotoLabel(3)
    label(2)
    sprite('ag432_06', 3)	# 108-110
    sprite('ag432_07', 3)	# 111-113	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    RefreshMultihit()
    sprite('ag432_08', 4)	# 114-117	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    sprite('ag432_09', 4)	# 118-121
    Unknown7007('6167333431000000000000000000000064000000616734303000000000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(3)
    sprite('ag432_10', 4)	# 122-125
    clearUponHandler(3)
    setInvincible(0)
    Unknown1019(80)
    YAccel(80)
    setGravity(1600)
    callSubroutine('Burner_Delete')
    tag_voice(0, 'pag261_0', 'pag261_1', '', '')
    sprite('ag432_11', 4)	# 126-129
    Unknown1019(80)
    YAccel(80)
    sprite('ag432_12', 4)	# 130-133
    Unknown1019(80)
    YAccel(80)
    sprite('ag020_04', 3)	# 134-136
    sprite('ag020_05', 4)	# 137-140
    sprite('ag020_06', 2)	# 141-142
    label(4)
    sprite('ag020_07', 4)	# 143-146
    sprite('ag020_08', 4)	# 147-150
    loopRest()
    gotoLabel(4)
    label(9)
    sprite('ag231_01', 2)	# 151-152
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 14)	# 153-166
    sprite('ag231_01', 2)	# 167-168
    sprite('ag010_02', 2)	# 169-170
    sprite('ag010_01', 4)	# 171-174
    sprite('ag010_00', 4)	# 175-178

@State
def UltimateAirThrowOD_Exe():

    def upon_IMMEDIATE():
        Unknown17012(5, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(1000)
        AttackP2(60)
        Unknown11091(60)
        Hitstop(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(120)
        Unknown9178(1)
        Unknown9362(1)
        Unknown9364(120)
        Unknown11102(1)
        Unknown11069('OrionSP_Shot')
        Unknown23027()
        Unknown30048(1)
        Unknown2034(1)
        Unknown2053(1)
        Unknown2017(1)
        SLOT_51 = 4

        def upon_3():
            if SLOT_2:
                Unknown48('19000000020000003500000016000000020000001a000000')
                if (SLOT_53 <= 60000):
                    clearUponHandler(3)
                    sendToLabel(2)

        def upon_STATE_END():
            Unknown26('UltimateAirThrow_Camera')

        def upon_12():
            clearUponHandler(12)
            ScreenShake(50000, 10000)
            SFX_3('guard_hit_l')
            SFX_3('damage_hit_mh')
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        Unknown13024(0)
        Unknown30068(1)
    sprite('ag432_07', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown1084(1)
    GFX_0('agef432_orgia_burner', 1)
    GFX_0('agef432_orgia_burner_back', 2)
    GFX_0('agef432_orgia_burner_3', 3)
    Unknown7015()
    Unknown7014('ag007')
    GFX_0('UltimateAirThrow_Camera', 100)
    sprite('ag432_07', 3)	# 4-6	 **attackbox here**
    physicsXImpulse(90000)
    setGravity(0)
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    callSubroutine('Burner_Delete')
    GFX_0('agef432_orgia_burner', 1)
    Unknown21007(1, 32)
    GFX_0('agef432_orgia_burner_back', 2)
    Unknown21007(1, 32)
    GFX_0('agef432_orgia_burner_3', 3)
    Unknown21007(1, 32)
    Unknown21012('556c74696d6174654169725468726f775f43616d65726100000000000000000020000000')
    Unknown2037(1)
    sprite('ag432_08', 3)	# 7-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    label(1)
    sprite('ag432_07', 3)	# 10-12	 **attackbox here**
    Unknown7015()
    Unknown7014('ag007')
    if (not SLOT_52):
        Unknown1019(110)
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    sprite('ag432_08', 3)	# 13-15	 **attackbox here**
    if (not SLOT_52):
        Unknown1019(110)
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    if (SLOT_12 >= 515000):
        SLOT_52 = 1
        physicsXImpulse(515000)
    gotoLabel(1)
    label(2)
    sprite('ag432_07', 20)	# 16-35	 **attackbox here**
    Unknown1019(0)
    Unknown7015()
    clearUponHandler(55)
    RefreshMultihit()
    sprite('ag433_00', 4)	# 36-39
    Unknown1007(-30000)
    physicsXImpulse(-4000)
    callSubroutine('Burner_Delete')
    tag_voice(0, 'pag259_1', 'pag260_1', '', '')
    sprite('ag433_01', 4)	# 40-43
    Unknown1019(200)
    SFX_3('ag001')
    sprite('ag433_02', 5)	# 44-48
    GFX_0('agef432_orgia_burner', 0)
    Unknown21007(1, 33)
    GFX_0('agef432_orgia_burner_back', 1)
    Unknown21007(1, 33)
    sprite('ag433_03', 5)	# 49-53
    Unknown1019(500)
    sprite('ag433_04', 5)	# 54-58
    Unknown1019(30)
    sprite('ag433_05', 4)	# 59-62
    Unknown1019(50)
    sprite('ag433_05', 4)	# 63-66
    Unknown1019(50)
    sprite('ag433_06', 4)	# 67-70
    Unknown1019(0)
    label(4)
    sprite('ag433_06', 3)	# 71-73
    SFX_3('ag002')
    SFX_3('ag003')
    GFX_0('OrionSP_Shot', 0)
    GFX_0('OrionSP_Shot', 3)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    sprite('ag433_07', 3)	# 74-76
    SFX_3('ag002')
    GFX_0('OrionSP_Shot', 1)
    GFX_0('OrionSP_Shot', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('ag433_08', 3)	# 77-79
    SFX_3('ag002')
    GFX_0('OrionSP_Shot', 0)
    GFX_0('OrionSP_Shot', 3)
    Unknown1019(50)
    YAccel(50)
    sprite('ag433_09', 2)	# 80-81
    SFX_3('ag002')
    GFX_0('OrionSP_Shot', 1)
    GFX_0('OrionSP_Shot', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('ag433_09', 1)	# 82-82
    if SLOT_51:
        SLOT_51 = (SLOT_51 + (-1))
        sendToLabel(4)
    sprite('ag433_06', 3)	# 83-85
    SFX_3('ag002')
    GFX_0('OrionSP_Shot', 0)
    Unknown23029(1, 6000, 0)
    sprite('ag433_10', 6)	# 86-91
    sprite('ag433_11', 6)	# 92-97
    callSubroutine('Burner_Delete')
    sprite('ag433_12', 6)	# 98-103
    sprite('ag433_13', 6)	# 104-109
    Unknown26('UltimateAirThrow_Camera')
    sprite('ag321_02', 4)	# 110-113
    Unknown23027()
    Unknown1084(1)
    sprite('ag321_03', 4)	# 114-117
    sprite('ag321_04', 4)	# 118-121
    sprite('ag321_05', 4)	# 122-125
    sprite('ag321_06', 4)	# 126-129
    sprite('ag321_07', 18)	# 130-147
    tag_voice(0, 'pag264_0', 'pag264_1', '', '')
    sprite('ag321_08', 9)	# 148-156	 **attackbox here**
    GFX_1('agef_airnagesmoke_01', 0)
    GFX_0('OrionLastCanon', 0)
    ScreenShake(20000, 5000)
    sprite('ag321_08', 2)	# 157-158	 **attackbox here**
    RefreshMultihit()
    AttackP2(100)
    Unknown11091(10)
    Hitstop(40)
    AirPushbackX(0)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(0)
    WallbounceReboundTime(0)
    Unknown9362(0)
    AirHitstunAnimation(10)
    Unknown11069('')
    Unknown11050('040000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ag321_08', 2)	# 159-160	 **attackbox here**
    RefreshMultihit()
    Damage(1800)
    Unknown11091(21)
    Hitstop(1)
    Unknown9362(0)
    WallbounceReboundTime(0)
    AirHitstunAnimation(10)
    AirPushbackX(0)
    AirPushbackY(45000)
    Unknown9017(1)
    Unknown11050('020000004f72696f6e46696e697368000000000000000000000000000000000000000000')
    ScreenShake(10000, 10000)
    Unknown9310(1)
    physicsXImpulse(-5000)
    physicsYImpulse(10000)
    setGravity(1000)
    SFX_3('bomb_m')
    sprite('ag321_09', 4)	# 161-164
    Unknown13024(1)
    sprite('ag321_10', 4)	# 165-168
    sprite('ag321_11', 4)	# 169-172
    sprite('ag321_12', 4)	# 173-176
    sprite('ag321_13', 4)	# 177-180
    setGravity(2000)
    sprite('ag020_04', 3)	# 181-183
    sprite('ag020_05', 4)	# 184-187
    sprite('ag020_06', 2)	# 188-189
    label(5)
    sprite('ag020_07', 4)	# 190-193
    sprite('ag020_08', 4)	# 194-197
    loopRest()
    gotoLabel(5)
    label(9)
    sprite('ag231_01', 2)	# 198-199
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 4)	# 200-203
    sprite('ag231_01', 2)	# 204-205
    sprite('ag010_02', 2)	# 206-207
    sprite('ag010_01', 4)	# 208-211
    sprite('ag010_00', 4)	# 212-215

@State
def AstralHeat():

    def upon_IMMEDIATE():
        Unknown17018()
        AttackLevel_(3)
        Damage(5099)
        Unknown11091(100)
        Unknown22004(30, 30)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 7023):
                sendToLabel(1)
            if (SLOT_48 == 7001):
                setInvincible(1)
                Unknown23083(1)
                Unknown23084(1)
                Unknown23088(1, 1)
            if (SLOT_48 == 7002):
                Unknown23157(1)
                sendToLabel(3)
            if (SLOT_48 == 7003):
                sendToLabel(4)
    sprite('ag450_00', 34)	# 1-34
    Unknown1084(1)
    Unknown2036(60, -1, 2)
    Unknown23147()
    GFX_0('P4U_Cutin_Parent', 100)
    tag_voice(1, 'pag290_0', 'pag290_1', '', '')
    sprite('ag450_00', 5)	# 35-39
    GFX_0('IchigekiTobiFire', 0)
    physicsXImpulse(-48000)
    physicsYImpulse(24000)
    sprite('ag450_01', 2)	# 40-41
    Unknown1019(50)
    YAccel(50)
    sprite('ag450_02', 2)	# 42-43
    Unknown1019(50)
    YAccel(50)
    sprite('ag450_03', 2)	# 44-45
    Unknown1019(50)
    YAccel(50)
    sprite('ag450_04', 2)	# 46-47
    Unknown1019(50)
    YAccel(50)
    sprite('ag450_05', 2)	# 48-49
    Unknown1019(50)
    YAccel(50)
    sprite('ag450_06', 2)	# 50-51
    Unknown1084(1)
    sprite('ag450_07', 2)	# 52-53
    GFX_0('IchigekiRenshaFire', 0)
    Unknown21015('4963686967656b69546f62694669726500000000000000000000000000000000711b000000000000')
    sprite('ag450_08', 2)	# 54-55
    sprite('ag450_09', 2)	# 56-57
    sprite('ag450_10', 2)	# 58-59
    sprite('ag450_09', 2)	# 60-61
    sprite('ag450_10', 2)	# 62-63
    sprite('ag450_09', 2)	# 64-65
    GFX_0('Ichigeki_Shot', 0)
    Unknown23029(1, 7021, 0)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 66-67
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 68-69
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 70-71
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 72-73
    GFX_0('Ichigeki_Shot', 0)
    Unknown23029(1, 7021, 0)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 74-75
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 76-77
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 78-79
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 80-81
    GFX_0('Ichigeki_Shot', 0)
    Unknown23029(1, 7021, 0)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 82-83
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 84-85
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 86-87
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 88-89
    GFX_0('Ichigeki_Shot', 0)
    Unknown23029(1, 7021, 0)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 90-91
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 92-93
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_10', 2)	# 94-95
    GFX_0('Ichigeki_Shot', 1)
    SFX_3('ag002')
    sprite('ag450_09', 2)	# 96-97
    GFX_0('Ichigeki_Shot', 1)
    Unknown23029(1, 7022, 0)
    Unknown21015('4963686967656b69546f62694669726500000000000000000000000000000000711b000000000000')
    SFX_3('ag005')
    sprite('ag450_10', 3)	# 98-100
    sprite('ag450_09', 3)	# 101-103
    sprite('ag450_10', 3)	# 104-106
    sprite('ag450_09', 3)	# 107-109
    sprite('ag450_10', 3)	# 110-112
    sprite('ag450_09', 3)	# 113-115
    sprite('ag450_10', 3)	# 116-118
    sprite('ag450_09', 3)	# 119-121
    sprite('ag450_10', 3)	# 122-124
    setGravity(700)
    sprite('ag450_09', 3)	# 125-127
    setInvincible(0)
    sprite('ag450_05', 3)	# 128-130
    sprite('ag450_04', 3)	# 131-133
    sprite('ag450_03', 3)	# 134-136
    sprite('ag450_02', 3)	# 137-139
    sprite('ag020_04', 3)	# 140-142
    sprite('ag020_05', 4)	# 143-146
    sprite('ag020_06', 2)	# 147-148
    label(0)
    sprite('ag020_07', 4)	# 149-152
    sprite('ag020_08', 4)	# 153-156
    loopRest()
    gotoLabel(0)
    ExitState()
    label(1)
    sprite('ag450_11', 3)	# 157-159
    sprite('ag450_12', 3)	# 160-162
    sprite('ag450_13', 10)	# 163-172
    sprite('ag450_14', 3)	# 173-175
    sprite('ag450_15', 3)	# 176-178
    sprite('ag450_16', 3)	# 179-181
    sprite('ag450_17', 3)	# 182-184
    sprite('ag450_16', 3)	# 185-187
    sprite('ag450_16', 3)	# 188-190
    sprite('ag450_17', 3)	# 191-193
    Unknown23029(11, 1080, 0)
    sprite('ag450_17', 3)	# 194-196
    sprite('ag450_16', 3)	# 197-199
    sprite('ag450_17', 3)	# 200-202
    sprite('ag450_16', 3)	# 203-205
    sprite('ag450_17', 3)	# 206-208
    sprite('ag450_16', 3)	# 209-211
    sprite('ag450_17', 3)	# 212-214
    sprite('ag450_16', 3)	# 215-217
    sprite('ag450_17', 3)	# 218-220
    sprite('ag450_16', 3)	# 221-223
    sprite('ag450_17', 3)	# 224-226
    sprite('ag450_16', 3)	# 227-229
    sprite('ag450_17', 3)	# 230-232
    sprite('ag450_16', 3)	# 233-235
    sprite('ag450_05', 3)	# 236-238
    setGravity(700)
    sprite('ag450_04', 3)	# 239-241
    sprite('ag450_03', 3)	# 242-244
    sprite('ag450_02', 3)	# 245-247
    sprite('ag020_04', 3)	# 248-250
    sprite('ag020_05', 4)	# 251-254
    sprite('ag020_06', 2)	# 255-256
    label(0)
    sprite('ag020_07', 4)	# 257-260
    sprite('ag020_08', 4)	# 261-264
    loopRest()
    gotoLabel(0)
    ExitState()
    label(3)
    sprite('ag450_18', 20)	# 265-284
    Unknown21015('4963686967656b6952656e736861466972650000000000000000000000000000711b000000000000')
    teleportRelativeY(0)
    sprite('ag450_18', 30)	# 285-314
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000641b000000000000')
    sprite('ag450_19', 3)	# 315-317
    GFX_0('IchigekiSmoke', 0)
    GFX_0('IchigekiSmoke2', 1)
    SFX_3('ag008')
    sprite('ag450_20', 3)	# 318-320
    sprite('ag450_21', 3)	# 321-323
    sprite('ag450_22', 3)	# 324-326
    sprite('ag450_21', 3)	# 327-329
    GFX_0('IchigekiThunderTame', 100)
    GFX_0('IchigekiThunderBallTame', 0)
    sprite('ag450_22', 3)	# 330-332
    sprite('ag450_21', 3)	# 333-335
    sprite('ag450_22', 3)	# 336-338
    SFX_3('ag009')
    SFX_3('electric_l')
    tag_voice(0, 'pag291_0', 'pag291_1', '', '')
    sprite('ag450_21', 3)	# 339-341
    sprite('ag450_22', 3)	# 342-344
    sprite('ag450_21', 3)	# 345-347
    sprite('ag450_22', 3)	# 348-350
    sprite('ag450_21', 3)	# 351-353
    sprite('ag450_22', 3)	# 354-356
    sprite('ag450_21', 3)	# 357-359
    sprite('ag450_22', 3)	# 360-362
    sprite('ag450_21', 3)	# 363-365
    sprite('ag450_22', 3)	# 366-368
    sprite('ag450_21', 3)	# 369-371
    SFX_3('electric_l')
    sprite('ag450_22', 3)	# 372-374
    sprite('ag450_21', 3)	# 375-377
    sprite('ag450_22', 3)	# 378-380
    sprite('ag450_21', 3)	# 381-383
    sprite('ag450_22', 3)	# 384-386
    sprite('ag450_21', 3)	# 387-389
    sprite('ag450_22', 3)	# 390-392
    sprite('ag450_21', 3)	# 393-395
    sprite('ag450_22', 3)	# 396-398
    sprite('ag450_21', 3)	# 399-401
    sprite('ag450_22', 3)	# 402-404
    sprite('ag450_21', 3)	# 405-407
    sprite('ag450_22', 3)	# 408-410
    sprite('ag450_21', 3)	# 411-413
    SFX_3('electric_l')
    sprite('ag450_22', 3)	# 414-416
    sprite('ag450_21', 3)	# 417-419
    sprite('ag450_22', 3)	# 420-422
    sprite('ag450_21', 3)	# 423-425
    sprite('ag450_22', 3)	# 426-428
    sprite('ag450_21', 3)	# 429-431
    sprite('ag450_22', 3)	# 432-434
    sprite('ag450_21', 3)	# 435-437
    sprite('ag450_22', 3)	# 438-440
    sprite('ag450_21', 3)	# 441-443
    sprite('ag450_22', 3)	# 444-446
    sprite('ag450_21', 3)	# 447-449
    sprite('ag450_22', 3)	# 450-452
    sprite('ag450_21', 3)	# 453-455
    sprite('ag450_22', 3)	# 456-458
    sprite('ag450_21', 3)	# 459-461
    sprite('ag450_22', 3)	# 462-464
    sprite('ag450_21', 3)	# 465-467
    sprite('ag450_22', 3)	# 468-470
    sprite('ag450_21', 3)	# 471-473
    sprite('ag450_22', 3)	# 474-476
    sprite('ag450_21', 3)	# 477-479
    sprite('ag450_22', 70)	# 480-549
    GFX_0('IchigekiPicture', 100)
    tag_voice(0, 'pag292_0', 'pag292_1', '', '')
    sprite('ag450_22', 10)	# 550-559
    sprite('ag450_24', 2)	# 560-561	 **attackbox here**
    GFX_0('Ichigeki_LastShot', 0)
    Unknown38(4, 1)
    GFX_0('BigYakkyo', 1)
    GFX_1('agef_yakkyoshock_la', 1)
    SFX_3('ag011')
    tag_voice(0, 'pag293_0', 'pag293_1', '', '')
    sprite('ag450_24', 2)	# 562-563	 **attackbox here**
    SFX_3('ag011')
    sprite('ag450_24', 3)	# 564-566	 **attackbox here**
    SFX_3('ag011')
    sprite('ag450_24', 1)	# 567-567	 **attackbox here**
    Unknown4004('534345465f4147527975686169596f6b6f00000000000000000000000000000064000000')
    Unknown26('IchigekiThunderBallTame')
    Unknown26('IchigekiThunderTame')
    sprite('ag450_24', 8)	# 568-575	 **attackbox here**
    GFX_1('agef_ichigekifire_la', 0)
    sprite('ag450_24', 32767)	# 576-33342	 **attackbox here**
    label(4)
    sprite('ag450_24', 50)	# 33343-33392	 **attackbox here**
    sprite('ag450_24', 10)	# 33393-33402	 **attackbox here**
    sprite('ag450_24', 10)	# 33403-33412	 **attackbox here**
    Unknown26('SCEF_AGRyuhaiYoko')
    RefreshMultihit()
    AirPushbackX(0)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(0)
    Unknown11023(1)
    Unknown11064(3)
    Unknown36(22)
    Unknown3001(0)
    Unknown35()
    Unknown1000(0)
    sprite('ag070_03', 70)	# 33413-33482
    GFX_0('IchigekiWinSmoke', 0)
    Unknown18010()
    Unknown23024(0)
    sprite('ag070_03', 30)	# 33483-33512
    Unknown20000(1)
    sprite('ag070_03', 30)	# 33513-33542
    tag_voice(0, 'pag294_0', 'pag294_1', '', '')
    sprite('ag070_03', 30)	# 33543-33572
    sprite('ag070_03', 30)	# 33573-33602
    sprite('ag070_02', 8)	# 33603-33610
    Unknown21015('4963686967656b6957696e536d6f6b6500000000000000000000000000000000711b000000000000')
    sprite('ag070_01', 8)	# 33611-33618
    sprite('ag070_00', 8)	# 33619-33626
    sprite('ag000_00', 10)	# 33627-33636

@State
def TagExitChar():

    def upon_IMMEDIATE():
        pass
    sprite('keep', 32767)	# 1-32767
    Unknown3038(1)
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(-2000000)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown2017(0)
        Unknown2034(0)
        teleportRelativeY(0)
        SLOT_65 = 1
    label(0)
    sprite('null', 1)	# 1-1
    gotoLabel(0)

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('ag202_05', 2)	# 26-27
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    sprite('ag202_06', 4)	# 28-31
    sprite('ag202_07', 4)	# 32-35
    sprite('ag202_08', 4)	# 36-39
    GFX_0('agef202_burner', 0)
    GFX_0('agef202_burner_back', 1)
    sprite('ag202_08', 1)	# 40-40
    callSubroutine('Burner_Delete')
    sprite('ag202_09', 32767)	# 41-32807
    SFX_0('004_swing_grap_1_0')
    label(9)
    sprite('ag202_10', 3)	# 32808-32810	 **attackbox here**
    callSubroutine('Burner_Delete')
    Unknown1084(1)
    sprite('ag010_00', 3)	# 32811-32813
    Unknown8000(100, 1, 1)
    sprite('ag231_01', 8)	# 32814-32821
    sprite('ag231_00', 4)	# 32822-32825
    sprite('ag231_01', 3)	# 32826-32828
    sprite('ag010_00', 4)	# 32829-32832

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
        Unknown2034(0)
        Unknown2053(0)
        Unknown2017(0)
        physicsXImpulse(-51000)
        physicsYImpulse(18800)
        setGravity(1500)
        Unknown8002()
    if SLOT_5:
        _gotolabel(100)
    sprite('ag033_01', 3)	# 1-3
    sendToLabelUpon(2, 1)
    Unknown8002()
    sprite('ag033_02', 3)	# 4-6
    loopRest()
    label(0)
    sprite('ag033_01', 3)	# 7-9
    sprite('ag033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ag033_03', 3)	# 13-15
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('ag033_04', 3)	# 16-18
    loopRest()
    ExitState()
    label(100)
    sprite('ag407_00', 3)	# 19-21
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    Unknown1084(1)
    SFX_3('ag006')
    Unknown7006('ag317', 100, 808609633, 51, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ag407_01', 4)	# 22-25
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    physicsXImpulse(-65000)
    physicsYImpulse(25000)
    SFX_3('ag006')
    sprite('ag407_02', 4)	# 26-29
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_02', 4)	# 30-33
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_02', 4)	# 34-37
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_02', 4)	# 38-41
    callSubroutine('Burner_Delete')
    GFX_0('agef_orgia_backdash', 0)
    GFX_0('agef_orgia_backdash_back', 1)
    sprite('ag407_03', 4)	# 42-45
    sprite('null', 7)	# 46-52
    loopRest()

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('ag601_12', 7)	# 1-7
    sprite('ag601_09', 7)	# 8-14
    sprite('ag601_10', 32)	# 15-46
    sprite('ag601_11', 8)	# 47-54
    sprite('ag601_12', 8)	# 55-62

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        Unknown17015()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('ag045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('ag045_00', 3)	# 2-4
    sprite('ag045_01', 4)	# 5-8
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    label(0)
    sprite('ag045_02', 5)	# 9-13
    sprite('ag045_03', 5)	# 14-18
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
    sprite('ag045_01', 6)	# 19-24
    sprite('ag045_00', 6)	# 25-30

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17015()
    sprite('ag601_12', 7)	# 1-7
    sprite('ag601_09', 7)	# 8-14
    label(1)
    sprite('ag601_10', 15)	# 15-29
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ag601_11', 8)	# 30-37
    sprite('ag601_12', 8)	# 38-45

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ag601_12', 7)	# 1-7
    sprite('ag601_09', 7)	# 8-14
    sprite('ag601_10', 46)	# 15-60
    sprite('ag601_11', 8)	# 61-68
    sprite('ag601_12', 8)	# 69-76
    callSubroutine('Burner_Delete')

@State
def CmnActChangePartnerQuickIn():
    sprite('ag032_05', 3)	# 1-3
    sprite('ag032_06', 5)	# 4-8
    sprite('ag032_09', 7)	# 9-15
    sprite('ag032_09', 7)	# 16-22
    sprite('ag032_10', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
        SLOT_65 = 1
    sprite('ag033_00', 1)	# 1-1
    sprite('ag033_01', 2)	# 2-3
    sprite('ag033_02', 2)	# 4-5
    sprite('ag033_02', 1)	# 6-6
    sprite('ag033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('ag033_02', 3)	# 10-12
    sprite('ag033_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ag033_04', 3)	# 16-18
    sprite('ag033_04', 3)	# 19-21

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
    sprite('ag020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ag020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ag010_00', 2)	# 11-12
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
    sprite('ag404_00', 3)	# 1-3
    sprite('ag404_01', 3)	# 4-6
    SFX_3('ag001')
    Unknown7007('7061673230375f300000000000000000640000007061673230375f310000000000000000640000007061673230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ag404_02', 3)	# 7-9
    sprite('ag404_03', 3)	# 10-12
    sprite('ag404_04', 3)	# 13-15
    sprite('ag404_05', 3)	# 16-18
    SFX_0('200_walk_normal_2')
    sprite('ag404_06', 3)	# 19-21
    SFX_0('200_walk_normal_2')
    sprite('ag404_07', 3)	# 22-24
    sprite('ag404_06', 3)	# 25-27
    sprite('ag404_07', 3)	# 28-30
    sprite('ag404_08', 3)	# 31-33
    GFX_1('agef_emptysmoke_00', 0)
    GFX_1('agef_canonshot_05', 0)
    GFX_0('CanonShot_TAGMatome', 0)
    SFX_3('ag005')
    Unknown8004(100, 1, 1)
    sprite('ag404_09', 3)	# 34-36
    sprite('ag404_10', 3)	# 37-39
    sprite('ag404_11', 3)	# 40-42
    sprite('ag404_12', 3)	# 43-45
    sprite('ag404_13', 3)	# 46-48
    sprite('ag404_00', 3)	# 49-51

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
        if SLOT_11:
            enterState('CmnActChangePartnerAssistAtk_D')
    sprite('ag204_00', 3)	# 1-3
    sprite('ag204_01', 3)	# 4-6
    sprite('ag204_02', 3)	# 7-9
    Unknown23029(11, 1070, 0)
    Unknown7007('7061673132315f300000000000000000640000007061673132315f310000000000000000640000007061673132315f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_1('persona_enter_ply', 0)
    sprite('ag204_03', 3)	# 10-12
    sprite('ag204_02', 3)	# 13-15
    sprite('ag204_03', 3)	# 16-18
    sprite('ag204_02', 3)	# 19-21
    Recovery()
    Unknown2063()
    sprite('ag204_03', 3)	# 22-24
    sprite('ag204_02', 3)	# 25-27
    sprite('ag204_03', 3)	# 28-30
    sprite('ag204_02', 3)	# 31-33
    sprite('ag204_03', 3)	# 34-36
    sprite('ag204_02', 3)	# 37-39
    sprite('ag204_03', 3)	# 40-42
    sprite('ag204_02', 3)	# 43-45
    sprite('ag204_03', 3)	# 46-48
    sprite('ag204_02', 3)	# 49-51
    sprite('ag204_03', 3)	# 52-54
    sprite('ag204_02', 3)	# 55-57
    sprite('ag204_03', 3)	# 58-60
    sprite('ag204_04', 4)	# 61-64
    sprite('ag000_00', 3)	# 65-67

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
        Unknown9154(60)
        AirUntechableTime(60)
        AirPushbackX(24000)
        AirPushbackY(18000)
        Unknown11042(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11056(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)

        def upon_78():
            Unknown2037(1)
            clearUponHandler(78)
            clearUponHandler(2)
    sprite('ag206_00', 3)	# 1-3
    sprite('ag206_01', 2)	# 4-5
    sprite('ag206_02', 2)	# 6-7
    physicsXImpulse(3000)
    sprite('ag206_03', 2)	# 8-9
    Unknown1019(400)
    sprite('ag206_04', 3)	# 10-12	 **attackbox here**
    Unknown8009(1)
    StartMultihit()
    Unknown1019(400)
    sprite('ag206_04ex', 8)	# 13-20	 **attackbox here**
    SFX_0('003_swing_grap_0_1')
    physicsYImpulse(6000)
    setGravity(1800)
    Unknown7009(1)
    sprite('ag206_05', 3)	# 21-23
    if SLOT_2:
        sendToLabel(10)
    else:
        Recovery()
    clearUponHandler(78)
    sprite('ag206_06', 3)	# 24-26
    Unknown1019(60)
    sprite('ag206_07', 3)	# 27-29
    sprite('ag020_04', 3)	# 30-32
    sprite('ag020_05', 4)	# 33-36
    sprite('ag020_06', 2)	# 37-38
    label(0)
    sprite('ag020_07', 4)	# 39-42
    sprite('ag020_08', 4)	# 43-46
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ag231_01', 4)	# 47-50
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown21015('41697242616c6b616e5f4d61746f6d6500000000000000000000000000000000e60f000000000000')
    callSubroutine('Burner_Delete')
    sprite('ag231_00', 7)	# 51-57
    sprite('ag231_00', 7)	# 58-64
    sprite('ag231_01', 7)	# 65-71
    sprite('ag010_01', 5)	# 72-76
    sprite('ag010_00', 5)	# 77-81
    ExitState()
    label(10)
    sprite('ag208_00', 3)	# 82-84
    Unknown22004(10, 1)
    Unknown1084(1)
    physicsXImpulse(3500)
    physicsYImpulse(2200)

    def upon_ON_HIT_OR_BLOCK():
        SLOT_51 = 1
    sprite('ag208_01', 3)	# 85-87
    Unknown1019(200)
    YAccel(200)
    SFX_0('003_swing_grap_0_1')
    sprite('ag208_02', 1)	# 88-88	 **attackbox here**
    StartMultihit()
    Unknown1019(400)
    YAccel(400)
    GFX_0('agef202_burner_jump', 0)
    GFX_0('agef202_burner_jump_back', 1)
    sprite('ag208_02', 2)	# 89-90	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(5000)
    AirPushbackY(30000)
    Unknown7009(0)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('ag208_03', 2)	# 91-92
    callSubroutine('Burner_Delete')
    Unknown1019(80)
    YAccel(150)
    Recovery()
    sprite('ag208_04', 4)	# 93-96
    Unknown1019(-30)
    sprite('ag208_05', 2)	# 97-98
    Unknown23027()
    YAccel(70)
    setGravity(2000)
    sprite('ag208_05', 2)	# 99-100
    sprite('ag207_06', 6)	# 101-106
    Unknown1019(80)
    YAccel(70)
    Unknown2001()
    sprite('ag020_04', 3)	# 107-109
    Unknown1019(80)
    YAccel(70)

@State
def CmnActChangePartnerDD():

    def upon_IMMEDIATE():
        setInvincible(1)
        if SLOT_162:
            SLOT_54 = 1

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
    sprite('null', 1)	# 1-1
    Unknown2036(91, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('ag020_07', 4)	# 3-6
    sprite('ag020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_54:
        enterState('AthenaSurfingDDDOD')
    else:
        enterState('AthenaSurfingDDD')

@State
def AthenaSurfingDDD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        setInvincible(1)
        Unknown2003(1)
        Unknown4020(11)
        Unknown4009(11)

        def upon_43():
            if (SLOT_48 == 5010):
                clearUponHandler(43)
                Unknown2017(1)
                Unknown4020(0)
                sendToLabel(2)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ag430_00', 8)	# 1-8
    Unknown23029(11, 1063, 0)
    Unknown1084(1)
    sprite('ag430_01', 6)	# 9-14
    teleportRelativeX(20000)
    sprite('ag430_02', 6)	# 15-20
    physicsXImpulse(-5000)
    physicsYImpulse(26000)
    setGravity(1700)
    sprite('ag430_03', 6)	# 21-26
    sprite('ag430_04', 6)	# 27-32
    sprite('ag430_05', 6)	# 33-38
    sprite('ag430_06', 4)	# 39-42
    Unknown1019(60)
    YAccel(60)
    setGravity(0)
    GFX_0('agef_surfing_burner_hold', 0)
    GFX_0('agef_surfing_burner_hold_back', 1)
    sprite('ag430_07', 4)	# 43-46
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 47-50
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 51-54
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 55-58
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 59-62
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 63-66
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_08', 3)	# 67-69
    Unknown13024(1)
    Unknown7007('7061673235325f300000000000000000640000007061673235345f300000000000000000640000007061673235325f310000000000000000640000007061673235345f31000000000000000064000000')
    SFX_0('019_quake_0')
    GuardPoint_(1)
    physicsXImpulse(5000)
    Unknown1028(4500)
    Unknown2017(0)
    callSubroutine('Burner_Delete')
    GFX_0('agef_surfing_burner', 0)
    GFX_0('agef_surfing_burner_back', 1)
    sprite('ag430_09', 3)	# 70-72
    sprite('ag430_08', 3)	# 73-75
    sprite('ag430_09', 3)	# 76-78
    sprite('ag430_08', 3)	# 79-81
    sprite('ag430_09', 3)	# 82-84
    sprite('ag430_08', 3)	# 85-87
    sprite('ag430_10', 2)	# 88-89
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 90-92
    Unknown1019(60)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 93-95
    Unknown1019(70)
    Unknown2017(1)
    sprite('ag430_11', 3)	# 96-98
    Unknown1019(70)
    sprite('ag430_12', 3)	# 99-101
    Unknown1019(70)
    sprite('ag430_11', 3)	# 102-104
    Unknown1019(70)
    sprite('ag430_13', 6)	# 105-110
    setGravity(2000)
    sprite('ag430_14', 6)	# 111-116
    sprite('ag020_04', 3)	# 117-119
    sprite('ag020_05', 4)	# 120-123
    sprite('ag020_06', 2)	# 124-125
    clearUponHandler(3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ag430_10', 2)	# 126-127
    physicsXImpulse(70000)
    setGravity(0)
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 128-130
    Unknown1019(80)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 131-133
    Unknown1019(90)
    sprite('ag430_11', 3)	# 134-136
    Unknown1019(90)
    sprite('ag430_12', 3)	# 137-139
    Unknown1019(70)
    sprite('ag430_11', 3)	# 140-142
    Unknown1019(60)
    sprite('ag430_12', 3)	# 143-145
    Unknown1019(50)
    sprite('ag430_13', 6)	# 146-151
    Unknown1019(60)
    setGravity(1000)
    Unknown2017(1)
    sprite('ag430_14', 1)	# 152-152
    sprite('ag430_14', 6)	# 153-158
    sprite('ag020_04', 3)	# 159-161
    sprite('ag020_05', 4)	# 162-165
    sprite('ag020_06', 2)	# 166-167
    loopRest()
    gotoLabel(1)
    label(1)
    sprite('ag020_07', 4)	# 168-171
    callSubroutine('Burner_Delete')
    sprite('ag020_08', 4)	# 172-175
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ag231_01', 2)	# 176-177
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 4)	# 178-181
    sprite('ag231_01', 2)	# 182-183
    sprite('ag010_02', 2)	# 184-185
    sprite('ag010_01', 4)	# 186-189
    sprite('ag010_00', 4)	# 190-193

@State
def AthenaSurfingDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        setInvincible(1)
        Unknown2003(1)
        Unknown4020(11)
        Unknown4009(11)

        def upon_43():
            if (SLOT_48 == 5010):
                sendToLabel(2)
                Unknown2017(1)
                Unknown4020(0)
            if (SLOT_48 == 5011):
                enterState('UltimateSpear')
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ag430_00', 8)	# 1-8
    Unknown23029(11, 1064, 0)
    Unknown1084(1)
    sprite('ag430_01', 6)	# 9-14
    teleportRelativeX(20000)
    sprite('ag430_02', 6)	# 15-20
    physicsXImpulse(-5000)
    physicsYImpulse(26000)
    setGravity(1700)
    sprite('ag430_03', 6)	# 21-26
    sprite('ag430_04', 6)	# 27-32
    sprite('ag430_05', 6)	# 33-38
    sprite('ag430_06', 4)	# 39-42
    Unknown1019(60)
    YAccel(60)
    setGravity(0)
    GFX_0('agef_surfing_burner_hold', 0)
    GFX_0('agef_surfing_burner_hold_back', 1)
    sprite('ag430_07', 4)	# 43-46
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 47-50
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 51-54
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 55-58
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_07', 4)	# 59-62
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_06', 4)	# 63-66
    Unknown1019(60)
    YAccel(60)
    sprite('ag430_08', 3)	# 67-69
    Unknown13024(1)
    Unknown7007('7061673235325f300000000000000000640000007061673235345f300000000000000000640000007061673235325f310000000000000000640000007061673235345f31000000000000000064000000')
    SFX_0('019_quake_0')
    GuardPoint_(1)
    physicsXImpulse(5000)
    Unknown1028(4500)
    Unknown2017(0)
    callSubroutine('Burner_Delete')
    GFX_0('agef_surfing_burner', 0)
    GFX_0('agef_surfing_burner_back', 1)
    sprite('ag430_09', 3)	# 70-72
    sprite('ag430_08', 3)	# 73-75
    sprite('ag430_09', 3)	# 76-78
    sprite('ag430_08', 3)	# 79-81
    sprite('ag430_09', 3)	# 82-84
    sprite('ag430_08', 3)	# 85-87
    sprite('ag430_10', 2)	# 88-89
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 90-92
    Unknown1019(60)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 93-95
    Unknown1019(70)
    Unknown2017(1)
    sprite('ag430_11', 3)	# 96-98
    Unknown1019(70)
    sprite('ag430_12', 3)	# 99-101
    Unknown1019(70)
    sprite('ag430_11', 3)	# 102-104
    Unknown1019(70)
    sprite('ag430_13', 6)	# 105-110
    setGravity(2000)
    sprite('ag430_14', 6)	# 111-116
    sprite('ag020_04', 3)	# 117-119
    sprite('ag020_05', 4)	# 120-123
    sprite('ag020_06', 2)	# 124-125
    clearUponHandler(3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ag430_10', 2)	# 126-127
    physicsXImpulse(70000)
    setGravity(0)
    setInvincible(0)
    callSubroutine('Burner_Delete')
    sprite('ag430_11', 3)	# 128-130
    Unknown1019(80)
    Unknown1028(0)
    sprite('ag430_12', 3)	# 131-133
    Unknown1019(90)
    sprite('ag430_11', 3)	# 134-136
    Unknown1019(90)
    sprite('ag430_12', 3)	# 137-139
    Unknown1019(70)
    sprite('ag430_11', 3)	# 140-142
    Unknown1019(60)
    sprite('ag430_12', 3)	# 143-145
    Unknown1019(50)
    sprite('ag430_13', 6)	# 146-151
    Unknown1019(60)
    setGravity(1000)
    Unknown2017(1)
    sprite('ag430_14', 1)	# 152-152
    sprite('ag430_14', 6)	# 153-158
    sprite('ag020_04', 3)	# 159-161
    sprite('ag020_05', 4)	# 162-165
    sprite('ag020_06', 2)	# 166-167
    loopRest()
    gotoLabel(1)
    label(1)
    sprite('ag020_07', 4)	# 168-171
    callSubroutine('Burner_Delete')
    sprite('ag020_08', 4)	# 172-175
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ag231_01', 2)	# 176-177
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ag231_00', 4)	# 178-181
    sprite('ag231_01', 2)	# 182-183
    sprite('ag010_02', 2)	# 184-185
    sprite('ag010_01', 4)	# 186-189
    sprite('ag010_00', 4)	# 190-193

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
    sprite('ag202_05', 4)	# 127-130
    callSubroutine('Burner_Delete')
    sprite('ag202_06', 4)	# 131-134
    sprite('ag202_07', 4)	# 135-138
    sprite('ag202_08', 4)	# 139-142
    GFX_0('agef202_burner', 0)
    GFX_0('agef202_burner_back', 1)
    Unknown2053(1)
    sprite('ag202_08', 1)	# 143-143
    callSubroutine('Burner_Delete')
    sprite('ag202_09', 4)	# 144-147
    SFX_0('004_swing_grap_1_0')
    sprite('ag202_10', 3)	# 148-150	 **attackbox here**
    sprite('ag202_11', 4)	# 151-154
    sendToLabelUpon(2, 9)
    sprite('ag202_12', 4)	# 155-158
    label(1)
    sprite('ag202_12', 4)	# 159-162
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ag010_00', 5)	# 163-167
    Unknown2017(1)
    Unknown2053(1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('ag231_01', 12)	# 168-179
    sprite('ag231_00', 5)	# 180-184
    sprite('ag231_01', 4)	# 185-188
    sprite('ag010_00', 4)	# 189-192

@State
def CmnActChangeReturnAppealBurst():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('keep', 1)	# 1-1
    sprite('ag611_00', 8)	# 2-9
    sprite('ag611_01', 8)	# 10-17
    sprite('ag611_02', 8)	# 18-25
    sprite('ag611_03', 60)	# 26-85
    sprite('ag611_02', 8)	# 86-93
    sprite('ag611_00', 8)	# 94-101

@Subroutine
def MouthTableInit():
    Unknown18011('pag000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag501', 12643, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag502', 13921, 13923, 13921, 12643, 24882, 25398, 24886, 25398, 24886, 12337, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag503', 13921, 13923, 13921, 12643, 24882, 25398, 24886, 25398, 24886, 12337, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag506', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 12849, 14179, 12641, 25394, 24887, 12849, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag507', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag521', 12643, 12641, 25394, 24887, 12849, 12899, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag524', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag403_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag403_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag600bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag600brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag600btg', 12643, 14177, 14179, 12641, 25394, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag600pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag600uva', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag601pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag601pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag601pla', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag601uhy', 12643, 12897, 25392, 24887, 25399, 12849, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag700bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag700brg', 12643, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 12643, 24882, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag700pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 13921, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag700pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag700pla', 12643, 14177, 12643, 24882, 25399, 14130, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag700pmi', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag701btg', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 12849, 14177, 14179, 12641, 25394, 14130, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag701rrb', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 12899, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag700uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pag701uva', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('brg')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('btg')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uva')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(10)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(20)
    sprite('ag600_00', 1)	# 2-2
    if random_(2, 0, 33):
        Unknown2037(7)
        SLOT_51 = 1
    else:
        SLOT_53 = 1
    sprite('ag600_00', 6)	# 3-8
    sprite('ag600_01', 6)	# 9-14
    sprite('ag600_02', 6)	# 15-20
    if SLOT_51:
        SFX_1('pag506')
    sprite('ag600_02', 1)	# 21-21
    if SLOT_53:
        sendToLabel(2)
    label(1)
    sprite('ag600_00', 6)	# 22-27
    sprite('ag600_01', 6)	# 28-33
    sprite('ag600_02', 6)	# 34-39
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(1)
    label(2)
    sprite('ag600_03', 6)	# 40-45
    if SLOT_53:
        Unknown7006('pag502', 100, 895967600, 13104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ag600_04', 20)	# 46-65
    sprite('ag600_05', 5)	# 66-70
    SFX_0('cloth_m')
    sprite('ag600_06', 5)	# 71-75
    sprite('ag600_07', 5)	# 76-80
    sprite('ag600_08', 5)	# 81-85
    sprite('ag600_09', 5)	# 86-90
    sprite('ag600_10', 5)	# 91-95
    sprite('ag600_11', 5)	# 96-100
    sprite('ag600_13', 6)	# 101-106
    sprite('ag600_15', 6)	# 107-112
    Unknown21007(24, 41)
    GFX_0('agef_entry1', 100)
    sprite('ag600_16', 14)	# 113-126
    sprite('ag600_17', 6)	# 127-132
    sprite('ag600_18', 6)	# 133-138
    sprite('ag600_19', 6)	# 139-144
    Unknown23018(1)
    label(3)
    sprite('ag000_00', 6)	# 145-150
    sprite('ag000_01', 6)	# 151-156
    sprite('ag000_02', 6)	# 157-162
    sprite('ag000_03', 6)	# 163-168
    sprite('ag000_04', 6)	# 169-174
    sprite('ag000_05', 6)	# 175-180
    sprite('ag000_06', 6)	# 181-186
    sprite('ag000_07', 6)	# 187-192
    sprite('ag000_08', 6)	# 193-198
    sprite('ag000_09', 6)	# 199-204
    gotoLabel(3)
    ExitState()
    label(10)
    Unknown1000(-1280000)
    GFX_0('agef_entry2_hole', 100)
    GFX_0('agef_entry2_pod', 100)
    GFX_0('agef_entry2_seat', 100)
    GFX_0('agef_entry2_pod2', 100)
    GFX_0('agef_entry2_ring', 100)
    sprite('ag601_00b', 6)	# 205-210
    sprite('ag601_00b', 20)	# 211-230
    physicsXImpulse(2500)
    physicsYImpulse(-7500)
    SFX_3('ag000')
    sprite('ag601_00b', 2)	# 231-232
    Unknown1084(1)
    teleportRelativeX(-2000)
    Unknown1007(5000)
    SFX_0('slash_sword_fast')
    sprite('ag601_00b', 20)	# 233-252
    teleportRelativeX(2000)
    Unknown1007(-5000)
    sprite('ag601_00c', 4)	# 253-256
    Unknown21012('616765665f656e747279325f72696e670000000000000000000000000000000020000000')
    sprite('ag601_00d', 4)	# 257-260
    sprite('ag601_00e', 4)	# 261-264
    sprite('ag601_00f', 4)	# 265-268
    sprite('ag601_00g', 4)	# 269-272
    sprite('ag601_00', 6)	# 273-278
    sprite('ag601_01', 6)	# 279-284
    sprite('ag601_02', 6)	# 285-290
    sprite('ag601_03', 6)	# 291-296
    sprite('ag601_04', 7)	# 297-303
    sprite('ag601_05', 7)	# 304-310
    sprite('ag601_06', 13)	# 311-323
    Unknown21012('616765665f656e747279325f686f6c650000000000000000000000000000000020000000')
    sprite('ag601_07', 6)	# 324-329
    Unknown7006('pag504', 100, 895967600, 13616, 0, 0, 100, 895967600, 13872, 0, 0, 100, 895967600, 14128, 0, 0, 100)
    Unknown21007(24, 41)
    Unknown21012('616765665f656e747279325f706f64000000000000000000000000000000000020000000')
    Unknown21012('616765665f656e747279325f736561740000000000000000000000000000000020000000')
    Unknown21012('616765665f656e747279325f706f64320000000000000000000000000000000020000000')
    sprite('ag601_08', 15)	# 330-344
    sprite('ag601_09', 6)	# 345-350
    sprite('ag601_10', 6)	# 351-356
    SFX_0('slash_knife_fast')
    label(11)
    sprite('ag601_10', 1)	# 357-357
    if SLOT_97:
        _gotolabel(11)
    sprite('ag601_11', 26)	# 358-383
    sprite('ag601_12', 6)	# 384-389
    Unknown23018(1)
    label(12)
    sprite('ag000_00', 6)	# 390-395
    sprite('ag000_01', 6)	# 396-401
    sprite('ag000_02', 6)	# 402-407
    sprite('ag000_03', 6)	# 408-413
    sprite('ag000_04', 6)	# 414-419
    sprite('ag000_05', 6)	# 420-425
    sprite('ag000_06', 6)	# 426-431
    sprite('ag000_07', 6)	# 432-437
    sprite('ag000_08', 6)	# 438-443
    sprite('ag000_09', 6)	# 444-449
    gotoLabel(12)
    ExitState()
    label(20)
    sprite('null', 3)	# 450-452
    Unknown2034(0)
    Unknown1000(-1783500)
    teleportRelativeY(320000)
    sprite('null', 3)	# 453-455
    if random_(2, 0, 50):
        SLOT_51 = 1
    else:
        SLOT_53 = 1
    sprite('ag035_00', 3)	# 456-458
    physicsXImpulse(27000)
    setGravity(400)
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 459-461
    GFX_0('agef_airdush', 0)
    GFX_0('agef_airdush_back', 1)
    GFX_0('agef_airdush_flare', 0)
    GFX_0('agef_airdush_back_flare', 1)
    sprite('ag035_02', 3)	# 462-464
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 465-467
    Unknown1019(50)
    sprite('ag035_02', 3)	# 468-470
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 471-473
    sprite('ag035_02', 3)	# 474-476
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 477-479
    sprite('ag035_02', 3)	# 480-482
    SFX_0('blaze_normal')
    sprite('ag035_00', 4)	# 483-486
    Unknown26('agef_airdush')
    Unknown26('agef_airdush_back')
    Unknown26('agef_airdush_flare')
    Unknown26('agef_airdush_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    sprite('ag400_05', 4)	# 487-490
    Unknown1084(1)
    physicsXImpulse(0)
    setGravity(0)
    if SLOT_51:
        SFX_1('pag500')
        physicsYImpulse(-1300)
    if SLOT_53:
        SFX_1('pag501')
        physicsYImpulse(-1000)
    sendToLabelUpon(2, 22)
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    SFX_3('ag007')
    sprite('ag400_06', 4)	# 491-494
    sprite('ag400_05', 4)	# 495-498
    sprite('ag400_06', 4)	# 499-502
    sprite('ag400_05', 4)	# 503-506
    GFX_1('agef_entry3_smoke', 104)
    sprite('ag400_06', 4)	# 507-510
    sprite('ag400_05', 4)	# 511-514
    sprite('ag400_06', 4)	# 515-518
    sprite('ag400_05', 4)	# 519-522
    sprite('ag400_06', 4)	# 523-526
    sprite('ag400_05', 4)	# 527-530
    SFX_3('ag007')
    label(21)
    sprite('ag400_06', 4)	# 531-534
    sprite('ag400_05', 4)	# 535-538
    loopRest()
    gotoLabel(21)
    label(22)
    sprite('ag401_00', 1)	# 539-539
    Unknown1000(-1230000)
    SFX_0('walk_stone_light')
    Unknown1084(1)
    sprite('ag401_00', 5)	# 540-544
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    Unknown23018(1)
    label(23)
    sprite('ag000_00', 6)	# 545-550
    sprite('ag000_01', 6)	# 551-556
    sprite('ag000_02', 6)	# 557-562
    sprite('ag000_03', 6)	# 563-568
    sprite('ag000_04', 6)	# 569-574
    sprite('ag000_05', 6)	# 575-580
    sprite('ag000_06', 6)	# 581-586
    sprite('ag000_07', 6)	# 587-592
    sprite('ag000_08', 6)	# 593-598
    sprite('ag000_09', 6)	# 599-604
    gotoLabel(23)
    ExitState()
    label(30)
    sprite('ag000_00', 2)	# 605-606
    SFX_1('pag000')
    label(31)
    sprite('ag000_00', 6)	# 607-612
    sprite('ag000_01', 6)	# 613-618
    sprite('ag000_02', 6)	# 619-624
    sprite('ag000_03', 6)	# 625-630
    sprite('ag000_04', 6)	# 631-636
    sprite('ag000_05', 6)	# 637-642
    sprite('ag000_06', 6)	# 643-648
    sprite('ag000_07', 6)	# 649-654
    sprite('ag000_08', 6)	# 655-660
    sprite('ag000_09', 6)	# 661-666
    gotoLabel(31)
    label(100)
    sprite('ag001_00', 7)	# 667-673
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)
    sprite('ag001_01', 18)	# 674-691
    sprite('ag001_02', 2)	# 692-693
    SFX_0('slash_knife_slow')
    SFX_1('pag600brg')
    sprite('ag001_03', 2)	# 694-695
    sprite('ag001_04', 2)	# 696-697
    sprite('ag001_01', 2)	# 698-699
    SFX_0('slash_knife_slow')
    sprite('ag001_02', 2)	# 700-701
    sprite('ag001_03', 2)	# 702-703
    sprite('ag001_04', 2)	# 704-705
    SFX_0('slash_knife_slow')
    sprite('ag001_01', 2)	# 706-707
    sprite('ag001_02', 2)	# 708-709
    sprite('ag001_03', 2)	# 710-711
    SFX_0('slash_knife_slow')
    sprite('ag001_04', 2)	# 712-713
    sprite('ag001_01', 2)	# 714-715
    sprite('ag001_02', 2)	# 716-717
    SFX_0('slash_knife_slow')
    sprite('ag001_03', 2)	# 718-719
    sprite('ag001_04', 2)	# 720-721
    sprite('ag001_01', 2)	# 722-723
    SFX_0('slash_knife_slow')
    sprite('ag001_02', 2)	# 724-725
    sprite('ag001_03', 2)	# 726-727
    sprite('ag001_04', 2)	# 728-729
    SFX_0('slash_knife_slow')
    sprite('ag001_01', 2)	# 730-731
    sprite('ag001_02', 2)	# 732-733
    sprite('ag001_03', 2)	# 734-735
    SFX_0('slash_knife_slow')
    sprite('ag001_04', 2)	# 736-737
    sprite('ag001_01', 2)	# 738-739
    sprite('ag001_02', 2)	# 740-741
    SFX_0('slash_knife_slow')
    sprite('ag001_03', 2)	# 742-743
    sprite('ag001_04', 2)	# 744-745
    sprite('ag001_01', 2)	# 746-747
    SFX_0('slash_knife_slow')
    sprite('ag001_02', 2)	# 748-749
    sprite('ag001_03', 2)	# 750-751
    sprite('ag001_04', 2)	# 752-753
    sprite('ag001_01', 15)	# 754-768
    sprite('ag001_00', 7)	# 769-775
    label(101)
    sprite('ag000_00', 6)	# 776-781
    sprite('ag000_01', 6)	# 782-787
    sprite('ag000_02', 6)	# 788-793
    sprite('ag000_03', 6)	# 794-799
    sprite('ag000_04', 6)	# 800-805
    sprite('ag000_05', 6)	# 806-811
    sprite('ag000_06', 6)	# 812-817
    sprite('ag000_07', 6)	# 818-823
    sprite('ag000_08', 6)	# 824-829
    sprite('ag000_09', 6)	# 830-835
    if SLOT_97:
        _gotolabel(101)
    sprite('ag000_00', 1)	# 836-836
    Unknown21007(24, 40)
    Unknown21011(250)
    label(102)
    sprite('ag000_00', 6)	# 837-842
    sprite('ag000_01', 6)	# 843-848
    sprite('ag000_02', 6)	# 849-854
    sprite('ag000_03', 6)	# 855-860
    sprite('ag000_04', 6)	# 861-866
    sprite('ag000_05', 6)	# 867-872
    sprite('ag000_06', 6)	# 873-878
    sprite('ag000_07', 6)	# 879-884
    sprite('ag000_08', 6)	# 885-890
    sprite('ag000_09', 6)	# 891-896
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('ag600_00', 6)	# 897-902
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ag600_01', 6)	# 903-908
    sprite('ag600_02', 6)	# 909-914
    SFX_1('pag600btg')
    sprite('ag600_00', 6)	# 915-920
    sprite('ag600_01', 6)	# 921-926
    sprite('ag600_02', 6)	# 927-932
    sprite('ag600_00', 6)	# 933-938
    sprite('ag600_01', 6)	# 939-944
    sprite('ag600_02', 6)	# 945-950
    sprite('ag600_03', 6)	# 951-956
    sprite('ag600_04', 20)	# 957-976
    sprite('ag600_05', 5)	# 977-981
    SFX_0('cloth_m')
    sprite('ag600_06', 5)	# 982-986
    sprite('ag600_07', 5)	# 987-991
    sprite('ag600_08', 5)	# 992-996
    sprite('ag600_09', 5)	# 997-1001
    sprite('ag600_10', 5)	# 1002-1006
    sprite('ag600_11', 5)	# 1007-1011
    sprite('ag600_13', 6)	# 1012-1017
    sprite('ag600_15', 6)	# 1018-1023
    GFX_0('agef_entry1', 100)
    sprite('ag600_16', 14)	# 1024-1037
    sprite('ag600_17', 6)	# 1038-1043
    sprite('ag600_18', 6)	# 1044-1049
    sprite('ag600_19', 6)	# 1050-1055
    Unknown21007(24, 40)
    Unknown21011(120)
    label(111)
    sprite('ag000_00', 6)	# 1056-1061
    sprite('ag000_01', 6)	# 1062-1067
    sprite('ag000_02', 6)	# 1068-1073
    sprite('ag000_03', 6)	# 1074-1079
    sprite('ag000_04', 6)	# 1080-1085
    sprite('ag000_05', 6)	# 1086-1091
    sprite('ag000_06', 6)	# 1092-1097
    sprite('ag000_07', 6)	# 1098-1103
    sprite('ag000_08', 6)	# 1104-1109
    sprite('ag000_09', 6)	# 1110-1115
    gotoLabel(111)
    ExitState()
    label(120)
    sprite('ag600_00', 1)	# 1116-1116
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ag600_00', 6)	# 1117-1122
    sprite('ag600_01', 6)	# 1123-1128
    sprite('ag600_02', 6)	# 1129-1134
    loopRest()
    gotoLabel(121)
    label(122)
    sprite('ag600_00', 6)	# 1135-1140
    SFX_1('pag601pbc')
    sprite('ag600_01', 6)	# 1141-1146
    sprite('ag600_02', 6)	# 1147-1152
    sprite('ag600_00', 6)	# 1153-1158
    sprite('ag600_01', 6)	# 1159-1164
    sprite('ag600_02', 6)	# 1165-1170
    sprite('ag600_00', 6)	# 1171-1176
    sprite('ag600_01', 6)	# 1177-1182
    sprite('ag600_02', 6)	# 1183-1188
    sprite('ag600_03', 6)	# 1189-1194
    sprite('ag600_04', 20)	# 1195-1214
    sprite('ag600_05', 5)	# 1215-1219
    SFX_0('cloth_m')
    sprite('ag600_06', 5)	# 1220-1224
    sprite('ag600_07', 5)	# 1225-1229
    sprite('ag600_08', 5)	# 1230-1234
    sprite('ag600_09', 5)	# 1235-1239
    sprite('ag600_10', 5)	# 1240-1244
    sprite('ag600_11', 5)	# 1245-1249
    sprite('ag600_13', 6)	# 1250-1255
    sprite('ag600_15', 6)	# 1256-1261
    GFX_0('agef_entry1', 100)
    sprite('ag600_16', 14)	# 1262-1275
    sprite('ag600_17', 6)	# 1276-1281
    sprite('ag600_18', 6)	# 1282-1287
    sprite('ag600_19', 6)	# 1288-1293
    Unknown21011(120)
    label(123)
    sprite('ag000_00', 6)	# 1294-1299
    sprite('ag000_01', 6)	# 1300-1305
    sprite('ag000_02', 6)	# 1306-1311
    sprite('ag000_03', 6)	# 1312-1317
    sprite('ag000_04', 6)	# 1318-1323
    sprite('ag000_05', 6)	# 1324-1329
    sprite('ag000_06', 6)	# 1330-1335
    sprite('ag000_07', 6)	# 1336-1341
    sprite('ag000_08', 6)	# 1342-1347
    sprite('ag000_09', 6)	# 1348-1353
    gotoLabel(123)
    ExitState()
    label(130)
    sprite('ag000_00', 1)	# 1354-1354

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ag000_00', 6)	# 1355-1360
    sprite('ag000_01', 6)	# 1361-1366
    sprite('ag000_02', 6)	# 1367-1372
    sprite('ag000_03', 6)	# 1373-1378
    sprite('ag000_04', 6)	# 1379-1384
    sprite('ag000_05', 6)	# 1385-1390
    sprite('ag000_06', 6)	# 1391-1396
    sprite('ag000_07', 6)	# 1397-1402
    sprite('ag000_08', 6)	# 1403-1408
    sprite('ag000_09', 6)	# 1409-1414
    gotoLabel(131)
    label(132)
    sprite('ag001_00', 7)	# 1415-1421
    sprite('ag001_01', 18)	# 1422-1439
    sprite('ag001_02', 2)	# 1440-1441
    SFX_0('slash_knife_slow')
    SFX_1('pag601uhy')
    sprite('ag001_03', 2)	# 1442-1443
    sprite('ag001_04', 2)	# 1444-1445
    sprite('ag001_01', 2)	# 1446-1447
    SFX_0('slash_knife_slow')
    sprite('ag001_02', 2)	# 1448-1449
    sprite('ag001_03', 2)	# 1450-1451
    sprite('ag001_04', 2)	# 1452-1453
    SFX_0('slash_knife_slow')
    sprite('ag001_01', 2)	# 1454-1455
    sprite('ag001_02', 2)	# 1456-1457
    sprite('ag001_03', 2)	# 1458-1459
    SFX_0('slash_knife_slow')
    sprite('ag001_04', 2)	# 1460-1461
    sprite('ag001_01', 2)	# 1462-1463
    sprite('ag001_02', 2)	# 1464-1465
    SFX_0('slash_knife_slow')
    sprite('ag001_03', 2)	# 1466-1467
    sprite('ag001_04', 2)	# 1468-1469
    sprite('ag001_01', 2)	# 1470-1471
    SFX_0('slash_knife_slow')
    sprite('ag001_02', 2)	# 1472-1473
    sprite('ag001_03', 2)	# 1474-1475
    sprite('ag001_04', 2)	# 1476-1477
    SFX_0('slash_knife_slow')
    sprite('ag001_01', 2)	# 1478-1479
    sprite('ag001_02', 2)	# 1480-1481
    sprite('ag001_03', 2)	# 1482-1483
    SFX_0('slash_knife_slow')
    sprite('ag001_04', 2)	# 1484-1485
    sprite('ag001_01', 2)	# 1486-1487
    sprite('ag001_02', 2)	# 1488-1489
    SFX_0('slash_knife_slow')
    sprite('ag001_03', 2)	# 1490-1491
    sprite('ag001_04', 2)	# 1492-1493
    sprite('ag001_01', 2)	# 1494-1495
    SFX_0('slash_knife_slow')
    sprite('ag001_02', 2)	# 1496-1497
    sprite('ag001_03', 2)	# 1498-1499
    sprite('ag001_04', 2)	# 1500-1501
    label(133)
    sprite('ag001_01', 1)	# 1502-1502
    if SLOT_97:
        _gotolabel(133)
    sprite('ag001_01', 15)	# 1503-1517
    sprite('ag001_00', 7)	# 1518-1524
    Unknown21007(24, 40)
    Unknown21011(120)
    label(134)
    sprite('ag000_00', 6)	# 1525-1530
    sprite('ag000_01', 6)	# 1531-1536
    sprite('ag000_02', 6)	# 1537-1542
    sprite('ag000_03', 6)	# 1543-1548
    sprite('ag000_04', 6)	# 1549-1554
    sprite('ag000_05', 6)	# 1555-1560
    sprite('ag000_06', 6)	# 1561-1566
    sprite('ag000_07', 6)	# 1567-1572
    sprite('ag000_08', 6)	# 1573-1578
    sprite('ag000_09', 6)	# 1579-1584
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('ag403_00', 7)	# 1585-1591
    SFX_3('ag001')
    Unknown2019(-100)
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(141)
    sprite('ag403_01', 7)	# 1592-1598
    sprite('ag403_02', 6)	# 1599-1604
    sprite('ag403_03', 8)	# 1605-1612
    sprite('ag403_04', 6)	# 1613-1618
    sprite('ag403_05', 5)	# 1619-1623
    sprite('ag403_06', 5)	# 1624-1628
    sprite('ag403_07', 6)	# 1629-1634
    sprite('ag403_08', 6)	# 1635-1640
    sprite('ag403_09', 6)	# 1641-1646	 **attackbox here**
    sprite('ag645_00', 6)	# 1647-1652
    sprite('ag645_01', 27)	# 1653-1679
    sprite('ag645_01ex2', 5)	# 1680-1684
    sprite('ag645_01ex1', 25)	# 1685-1709
    sprite('ag645_01ex2', 7)	# 1710-1716
    sprite('ag645_01ex3', 42)	# 1717-1758
    sprite('ag645_01ex2', 5)	# 1759-1763
    sprite('ag645_01ex1', 30)	# 1764-1793
    sprite('ag645_01ex2', 7)	# 1794-1800
    sprite('ag645_01ex3', 42)	# 1801-1842
    sprite('ag645_01ex2', 5)	# 1843-1847
    sprite('ag645_01ex1', 40)	# 1848-1887
    sprite('ag645_01ex2', 7)	# 1888-1894
    sprite('ag645_01ex3', 32767)	# 1895-34661
    label(141)
    sprite('ag645_02', 6)	# 34662-34667
    sprite('ag645_03', 18)	# 34668-34685
    Unknown2037(3)
    SFX_1('pag601rrb')
    label(142)
    sprite('ag645_04', 2)	# 34686-34687
    sprite('ag645_05', 2)	# 34688-34689
    sprite('ag645_06', 2)	# 34690-34691
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(142)
    sprite('ag645_03', 32767)	# 34692-67458
    Unknown21011(120)
    ExitState()
    label(150)
    sprite('null', 3)	# 67459-67461
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-1783500)
    else:
        Unknown1000(-2018500)
    teleportRelativeY(320000)
    sprite('null', 3)	# 67462-67464
    sprite('ag035_00', 3)	# 67465-67467
    physicsXImpulse(27000)
    setGravity(400)
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67468-67470
    GFX_0('agef_airdush', 0)
    GFX_0('agef_airdush_back', 1)
    GFX_0('agef_airdush_flare', 0)
    GFX_0('agef_airdush_back_flare', 1)
    sprite('ag035_02', 3)	# 67471-67473
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67474-67476
    Unknown1019(50)
    sprite('ag035_02', 3)	# 67477-67479
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67480-67482
    sprite('ag035_02', 3)	# 67483-67485
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67486-67488
    sprite('ag035_02', 3)	# 67489-67491
    SFX_0('blaze_normal')
    sprite('ag035_00', 4)	# 67492-67495
    Unknown26('agef_airdush')
    Unknown26('agef_airdush_back')
    Unknown26('agef_airdush_flare')
    Unknown26('agef_airdush_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    sprite('ag400_05', 4)	# 67496-67499
    Unknown1084(1)
    physicsXImpulse(0)
    physicsYImpulse(-1000)
    setGravity(0)
    sendToLabelUpon(2, 152)
    SFX_1('pag600uva')
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    SFX_3('ag007')
    sprite('ag400_06', 4)	# 67500-67503
    sprite('ag400_05', 4)	# 67504-67507
    sprite('ag400_06', 4)	# 67508-67511
    sprite('ag400_05', 4)	# 67512-67515
    GFX_1('agef_entry3_smoke', 104)
    sprite('ag400_06', 4)	# 67516-67519
    sprite('ag400_05', 4)	# 67520-67523
    sprite('ag400_06', 4)	# 67524-67527
    sprite('ag400_05', 4)	# 67528-67531
    sprite('ag400_06', 4)	# 67532-67535
    sprite('ag400_05', 4)	# 67536-67539
    SFX_3('ag007')
    label(151)
    sprite('ag400_06', 4)	# 67540-67543
    sprite('ag400_05', 4)	# 67544-67547
    loopRest()
    gotoLabel(151)
    label(152)
    sprite('ag401_00', 1)	# 67548-67548
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_0('walk_stone_light')
    Unknown1084(1)
    sprite('ag401_00', 5)	# 67549-67553
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    Unknown21011(420)
    label(153)
    sprite('ag000_00', 6)	# 67554-67559
    sprite('ag000_01', 6)	# 67560-67565
    sprite('ag000_02', 6)	# 67566-67571
    sprite('ag000_03', 6)	# 67572-67577
    sprite('ag000_04', 6)	# 67578-67583
    sprite('ag000_05', 6)	# 67584-67589
    sprite('ag000_06', 6)	# 67590-67595
    sprite('ag000_07', 6)	# 67596-67601
    sprite('ag000_08', 6)	# 67602-67607
    sprite('ag000_09', 6)	# 67608-67613
    Unknown21007(24, 40)
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('ag600_00', 1)	# 67614-67614
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ag600_00', 6)	# 67615-67620
    sprite('ag600_01', 6)	# 67621-67626
    sprite('ag600_02', 6)	# 67627-67632
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('ag600_00', 6)	# 67633-67638
    SFX_1('pag601pla')
    sprite('ag600_01', 6)	# 67639-67644
    sprite('ag600_02', 6)	# 67645-67650
    sprite('ag600_00', 6)	# 67651-67656
    sprite('ag600_01', 6)	# 67657-67662
    sprite('ag600_02', 6)	# 67663-67668
    sprite('ag600_00', 6)	# 67669-67674
    sprite('ag600_01', 6)	# 67675-67680
    sprite('ag600_02', 6)	# 67681-67686
    sprite('ag600_03', 6)	# 67687-67692
    sprite('ag600_04', 20)	# 67693-67712
    sprite('ag600_05', 5)	# 67713-67717
    SFX_0('cloth_m')
    sprite('ag600_06', 5)	# 67718-67722
    sprite('ag600_07', 5)	# 67723-67727
    sprite('ag600_08', 5)	# 67728-67732
    sprite('ag600_09', 5)	# 67733-67737
    sprite('ag600_10', 5)	# 67738-67742
    sprite('ag600_11', 5)	# 67743-67747
    sprite('ag600_13', 6)	# 67748-67753
    sprite('ag600_15', 6)	# 67754-67759
    GFX_0('agef_entry1', 100)
    sprite('ag600_16', 14)	# 67760-67773
    sprite('ag600_17', 6)	# 67774-67779
    sprite('ag600_18', 6)	# 67780-67785
    sprite('ag600_19', 6)	# 67786-67791
    Unknown23018(1)
    label(163)
    sprite('ag000_00', 6)	# 67792-67797
    sprite('ag000_01', 6)	# 67798-67803
    sprite('ag000_02', 6)	# 67804-67809
    sprite('ag000_03', 6)	# 67810-67815
    sprite('ag000_04', 6)	# 67816-67821
    sprite('ag000_05', 6)	# 67822-67827
    sprite('ag000_06', 6)	# 67828-67833
    sprite('ag000_07', 6)	# 67834-67839
    sprite('ag000_08', 6)	# 67840-67845
    sprite('ag000_09', 6)	# 67846-67851
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('null', 3)	# 67852-67854
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-1783500)
    else:
        Unknown1000(-2018500)
    teleportRelativeY(320000)
    sprite('null', 3)	# 67855-67857
    sprite('ag035_00', 3)	# 67858-67860
    physicsXImpulse(27000)
    setGravity(400)
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67861-67863
    GFX_0('agef_airdush', 0)
    GFX_0('agef_airdush_back', 1)
    GFX_0('agef_airdush_flare', 0)
    GFX_0('agef_airdush_back_flare', 1)
    sprite('ag035_02', 3)	# 67864-67866
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67867-67869
    Unknown1019(50)
    sprite('ag035_02', 3)	# 67870-67872
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67873-67875
    sprite('ag035_02', 3)	# 67876-67878
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 67879-67881
    sprite('ag035_02', 3)	# 67882-67884
    SFX_0('blaze_normal')
    sprite('ag035_00', 4)	# 67885-67888
    Unknown26('agef_airdush')
    Unknown26('agef_airdush_back')
    Unknown26('agef_airdush_flare')
    Unknown26('agef_airdush_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    sprite('ag400_05', 4)	# 67889-67892
    Unknown1084(1)
    physicsXImpulse(0)
    physicsYImpulse(-1000)
    setGravity(0)
    sendToLabelUpon(2, 172)
    SFX_1('pag600pmi')
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    SFX_3('ag007')
    sprite('ag400_06', 4)	# 67893-67896
    sprite('ag400_05', 4)	# 67897-67900
    sprite('ag400_06', 4)	# 67901-67904
    sprite('ag400_05', 4)	# 67905-67908
    GFX_1('agef_entry3_smoke', 104)
    sprite('ag400_06', 4)	# 67909-67912
    sprite('ag400_05', 4)	# 67913-67916
    sprite('ag400_06', 4)	# 67917-67920
    sprite('ag400_05', 4)	# 67921-67924
    sprite('ag400_06', 4)	# 67925-67928
    sprite('ag400_05', 4)	# 67929-67932
    SFX_3('ag007')
    label(171)
    sprite('ag400_06', 4)	# 67933-67936
    sprite('ag400_05', 4)	# 67937-67940
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('ag401_00', 1)	# 67941-67941
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_0('walk_stone_light')
    Unknown1084(1)
    sprite('ag401_00', 5)	# 67942-67946
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    label(173)
    sprite('ag000_00', 6)	# 67947-67952
    sprite('ag000_01', 6)	# 67953-67958
    sprite('ag000_02', 6)	# 67959-67964
    sprite('ag000_03', 6)	# 67965-67970
    sprite('ag000_04', 6)	# 67971-67976
    sprite('ag000_05', 6)	# 67977-67982
    sprite('ag000_06', 6)	# 67983-67988
    sprite('ag000_07', 6)	# 67989-67994
    sprite('ag000_08', 6)	# 67995-68000
    sprite('ag000_09', 6)	# 68001-68006
    if SLOT_97:
        _gotolabel(173)
    sprite('ag000_00', 1)	# 68007-68007
    Unknown21007(24, 40)
    Unknown21011(240)
    label(174)
    sprite('ag000_00', 6)	# 68008-68013
    sprite('ag000_01', 6)	# 68014-68019
    sprite('ag000_02', 6)	# 68020-68025
    sprite('ag000_03', 6)	# 68026-68031
    sprite('ag000_04', 6)	# 68032-68037
    sprite('ag000_05', 6)	# 68038-68043
    sprite('ag000_06', 6)	# 68044-68049
    sprite('ag000_07', 6)	# 68050-68055
    sprite('ag000_08', 6)	# 68056-68061
    sprite('ag000_09', 6)	# 68062-68067
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('null', 3)	# 68068-68070
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-1783500)
    else:
        Unknown1000(-2018500)
    teleportRelativeY(320000)
    sprite('null', 3)	# 68071-68073
    sprite('ag035_00', 3)	# 68074-68076
    physicsXImpulse(27000)
    setGravity(400)
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 68077-68079
    GFX_0('agef_airdush', 0)
    GFX_0('agef_airdush_back', 1)
    GFX_0('agef_airdush_flare', 0)
    GFX_0('agef_airdush_back_flare', 1)
    sprite('ag035_02', 3)	# 68080-68082
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 68083-68085
    Unknown1019(50)
    sprite('ag035_02', 3)	# 68086-68088
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 68089-68091
    sprite('ag035_02', 3)	# 68092-68094
    SFX_0('blaze_normal')
    sprite('ag035_01', 3)	# 68095-68097
    sprite('ag035_02', 3)	# 68098-68100
    SFX_0('blaze_normal')
    sprite('ag035_00', 4)	# 68101-68104
    Unknown26('agef_airdush')
    Unknown26('agef_airdush_back')
    Unknown26('agef_airdush_flare')
    Unknown26('agef_airdush_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    sprite('ag400_05', 4)	# 68105-68108
    Unknown1084(1)
    physicsXImpulse(0)
    physicsYImpulse(-1000)
    setGravity(0)
    sendToLabelUpon(2, 182)
    SFX_1('pag600bph')
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    GFX_0('agef_entry3', 0)
    GFX_0('agef_entry3_back', 1)
    GFX_0('agef_entry3_flare', 0)
    GFX_0('agef_entry3_back_flare', 1)
    SFX_3('ag007')
    sprite('ag400_06', 4)	# 68109-68112
    sprite('ag400_05', 4)	# 68113-68116
    sprite('ag400_06', 4)	# 68117-68120
    sprite('ag400_05', 4)	# 68121-68124
    GFX_1('agef_entry3_smoke', 104)
    sprite('ag400_06', 4)	# 68125-68128
    sprite('ag400_05', 4)	# 68129-68132
    sprite('ag400_06', 4)	# 68133-68136
    sprite('ag400_05', 4)	# 68137-68140
    sprite('ag400_06', 4)	# 68141-68144
    sprite('ag400_05', 4)	# 68145-68148
    SFX_3('ag007')
    label(181)
    sprite('ag400_06', 4)	# 68149-68152
    sprite('ag400_05', 4)	# 68153-68156
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('ag401_00', 1)	# 68157-68157
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_0('walk_stone_light')
    Unknown1084(1)
    sprite('ag401_00', 5)	# 68158-68162
    Unknown26('agef_entry3')
    Unknown26('agef_entry3_back')
    Unknown26('agef_entry3_flare')
    Unknown26('agef_entry3_back_flare')
    Unknown2037(1)
    Unknown21011(370)
    label(183)
    sprite('ag000_00', 6)	# 68163-68168
    sprite('ag000_01', 6)	# 68169-68174
    sprite('ag000_02', 6)	# 68175-68180
    if (not SLOT_2):
        Unknown21007(24, 40)
    sprite('ag000_03', 6)	# 68181-68186
    sprite('ag000_04', 6)	# 68187-68192
    sprite('ag000_05', 6)	# 68193-68198
    sprite('ag000_06', 6)	# 68199-68204
    sprite('ag000_07', 6)	# 68205-68210
    sprite('ag000_08', 6)	# 68211-68216
    sprite('ag000_09', 6)	# 68217-68222
    Unknown2038(-1)
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('ag600_00', 1)	# 68223-68223
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ag600_00', 6)	# 68224-68229
    sprite('ag600_01', 6)	# 68230-68235
    sprite('ag600_02', 6)	# 68236-68241
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('ag600_00', 6)	# 68242-68247
    SFX_1('pag601pak')
    sprite('ag600_01', 6)	# 68248-68253
    sprite('ag600_02', 6)	# 68254-68259
    sprite('ag600_00', 6)	# 68260-68265
    sprite('ag600_01', 6)	# 68266-68271
    sprite('ag600_02', 6)	# 68272-68277
    sprite('ag600_00', 6)	# 68278-68283
    sprite('ag600_01', 6)	# 68284-68289
    sprite('ag600_02', 6)	# 68290-68295
    sprite('ag600_03', 6)	# 68296-68301
    sprite('ag600_04', 20)	# 68302-68321
    sprite('ag600_05', 5)	# 68322-68326
    SFX_0('cloth_m')
    sprite('ag600_06', 5)	# 68327-68331
    sprite('ag600_07', 5)	# 68332-68336
    sprite('ag600_08', 5)	# 68337-68341
    sprite('ag600_09', 5)	# 68342-68346
    sprite('ag600_10', 5)	# 68347-68351
    sprite('ag600_11', 5)	# 68352-68356
    sprite('ag600_13', 6)	# 68357-68362
    sprite('ag600_15', 6)	# 68363-68368
    GFX_0('agef_entry1', 100)
    sprite('ag600_16', 14)	# 68369-68382
    sprite('ag600_17', 6)	# 68383-68388
    sprite('ag600_18', 6)	# 68389-68394
    sprite('ag600_19', 6)	# 68395-68400
    Unknown21011(210)
    label(193)
    sprite('ag000_00', 6)	# 68401-68406
    sprite('ag000_01', 6)	# 68407-68412
    sprite('ag000_02', 6)	# 68413-68418
    sprite('ag000_03', 6)	# 68419-68424
    sprite('ag000_04', 6)	# 68425-68430
    sprite('ag000_05', 6)	# 68431-68436
    Unknown21007(24, 40)
    sprite('ag000_06', 6)	# 68437-68442
    sprite('ag000_07', 6)	# 68443-68448
    sprite('ag000_08', 6)	# 68449-68454
    sprite('ag000_09', 6)	# 68455-68460
    gotoLabel(193)
    ExitState()
    label(991)
    sprite('ag000_00', 1)	# 68461-68461
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ag000_00', 6)	# 68462-68467
    sprite('ag000_01', 6)	# 68468-68473
    sprite('ag000_02', 6)	# 68474-68479
    sprite('ag000_03', 6)	# 68480-68485
    sprite('ag000_04', 6)	# 68486-68491
    sprite('ag000_05', 6)	# 68492-68497
    sprite('ag000_06', 6)	# 68498-68503
    sprite('ag000_07', 6)	# 68504-68509
    sprite('ag000_08', 6)	# 68510-68515
    sprite('ag000_09', 6)	# 68516-68521
    gotoLabel(992)
    label(993)
    sprite('ag033_00', 2)	# 68522-68523

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
    sprite('ag033_01', 3)	# 68524-68526
    label(994)
    sprite('ag033_01', 3)	# 68527-68529
    sprite('ag033_02', 3)	# 68530-68532
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 68533-68535
    ExitState()

@State
def CmnActRoundWin():
    sprite('keep', 32767)	# 1-32767

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
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('bph'):
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
    sprite('ag610_00', 6)	# 4-9
    physicsYImpulse(1)
    setGravity(-100)
    GFX_0('agef_win_burner_r60', 0)
    SFX_0('blaze_normal')
    if SLOT_158:
        GFX_0('MatchWinCamera', 100)
    sprite('ag610_00', 6)	# 10-15
    sprite('ag610_01', 6)	# 16-21
    Unknown26('agef_win_burner_r60')
    GFX_0('agef_win_burner_r75', 0)
    GFX_0('agef_win_burner_somke', 104)
    SFX_0('blaze_normal')
    sprite('ag610_02', 6)	# 22-27
    Unknown26('agef_win_burner_r75')
    GFX_0('agef_win_burner', 0)
    GFX_0('agef_win_burner_line', 0)
    sprite('ag610_03', 6)	# 28-33
    SFX_0('blaze_normal')
    sprite('ag610_04', 6)	# 34-39
    setGravity(210)
    sprite('ag610_03', 6)	# 40-45
    SFX_0('blaze_normal')
    sprite('ag610_04', 6)	# 46-51
    sprite('ag610_05', 3)	# 52-54
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    SFX_0('blaze_normal')
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pag524', 100, 895967600, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pag402_0', 100, 879190384, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pag522', 100, 895967600, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ag610_06', 6)	# 55-60
    setGravity(-150)
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    SFX_0('slash_knife_fast')
    label(1)
    sprite('ag610_07', 5)	# 61-65
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 66-70
    sprite('ag610_07', 5)	# 71-75
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 76-80
    setGravity(150)
    sprite('ag610_07', 5)	# 81-85
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 86-90
    sprite('ag610_07', 5)	# 91-95
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 96-100
    setGravity(-150)
    if SLOT_97:
        _gotolabel(1)
    sprite('ag610_07', 5)	# 101-105
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 106-110
    sprite('ag610_09', 5)	# 111-115
    setGravity(-10)
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    SFX_0('blaze_normal')
    sprite('ag610_10', 6)	# 116-121
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    sprite('ag610_11', 20)	# 122-141
    sprite('ag610_12', 5)	# 142-146
    setGravity(-100)
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner_upper', 0)
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 147-151
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 152-156
    sprite('ag610_13', 5)	# 157-161
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 162-166
    setGravity(-500)
    sprite('ag610_13', 5)	# 167-171
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 172-176
    sprite('ag610_13', 5)	# 177-181
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 182-186
    setGravity(-900)
    sprite('ag610_13', 5)	# 187-191
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 192-196
    sprite('ag610_13', 5)	# 197-201
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 202-206
    sprite('ag610_13', 5)	# 207-211
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 212-216
    sprite('ag610_12', 5)	# 217-221
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 222-226
    sprite('ag610_12', 5)	# 227-231
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 232-236
    sprite('ag610_12', 5)	# 237-241
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 242-246
    sprite('ag610_12', 5)	# 247-251
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 252-256
    sprite('ag610_12', 5)	# 257-261
    SFX_0('blaze_normal')
    Unknown1084(1)
    label(2)
    sprite('ag610_13', 1)	# 262-262
    gotoLabel(2)
    label(10)
    sprite('ag611_00', 6)	# 263-268
    sprite('ag611_01', 20)	# 269-288
    sprite('ag611_02', 6)	# 289-294
    GFX_0('agef_win2_steam_r', 0)
    GFX_0('agef_win2_steam_l', 1)
    GFX_0('agef_win2_steam_r', 2)
    GFX_0('agef_win2_steam_l', 3)
    GFX_0('agef_win2_steam_r', 4)
    GFX_0('agef_win2_steam_l', 5)
    SFX_3('ag008')
    sprite('ag611_03', 20)	# 295-314
    sprite('ag611_03', 20)	# 315-334
    Unknown23029(11, 9000, 0)
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pag524', 100, 895967600, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pag402_0', 100, 879190384, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pag520', 100, 895967600, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ag611_04', 7)	# 335-341
    sprite('ag611_05', 7)	# 342-348
    sprite('ag611_06', 18)	# 349-366
    sprite('ag611_07', 7)	# 367-373
    sprite('ag611_08', 7)	# 374-380
    sprite('ag611_09', 7)	# 381-387
    label(11)
    sprite('ag611_10', 6)	# 388-393
    sprite('ag611_11', 6)	# 394-399
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('ag001_00', 1)	# 400-400
    SFX_1('pag701uva')
    label(21)
    sprite('ag001_01', 18)	# 401-418
    sprite('ag001_02', 2)	# 419-420
    SFX_0('slash_knife_slow')
    sprite('ag001_03', 2)	# 421-422
    sprite('ag001_04', 2)	# 423-424
    gotoLabel(21)
    ExitState()
    label(100)
    sprite('ag611_00', 6)	# 425-430
    sprite('ag611_01', 20)	# 431-450
    sprite('ag611_02', 6)	# 451-456
    GFX_0('agef_win2_steam_r', 0)
    GFX_0('agef_win2_steam_l', 1)
    GFX_0('agef_win2_steam_r', 2)
    GFX_0('agef_win2_steam_l', 3)
    GFX_0('agef_win2_steam_r', 4)
    GFX_0('agef_win2_steam_l', 5)
    SFX_3('ag008')
    sprite('ag611_03', 20)	# 457-476
    sprite('ag611_03', 20)	# 477-496
    Unknown23029(11, 9000, 0)
    SFX_1('pag700brg')
    sprite('ag611_04', 7)	# 497-503
    sprite('ag611_05', 7)	# 504-510
    sprite('ag611_06', 18)	# 511-528
    sprite('ag611_07', 7)	# 529-535
    sprite('ag611_08', 7)	# 536-542
    sprite('ag611_09', 7)	# 543-549
    label(101)
    sprite('ag611_10', 6)	# 550-555
    sprite('ag611_11', 6)	# 556-561
    loopRest()
    if SLOT_97:
        _gotolabel(101)
    sprite('ag611_10', 1)	# 562-562
    Unknown21007(24, 40)
    Unknown21011(300)
    label(102)
    sprite('ag611_10', 6)	# 563-568
    sprite('ag611_11', 6)	# 569-574
    loopRest()
    gotoLabel(102)
    label(110)
    sprite('ag000_00', 1)	# 575-575

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ag000_00', 6)	# 576-581
    sprite('ag000_01', 6)	# 582-587
    sprite('ag000_02', 6)	# 588-593
    sprite('ag000_03', 6)	# 594-599
    sprite('ag000_04', 6)	# 600-605
    sprite('ag000_05', 6)	# 606-611
    sprite('ag000_06', 6)	# 612-617
    sprite('ag000_07', 6)	# 618-623
    sprite('ag000_08', 6)	# 624-629
    sprite('ag000_09', 6)	# 630-635
    gotoLabel(111)
    label(112)
    sprite('ag610_00', 6)	# 636-641
    physicsYImpulse(1)
    setGravity(-100)
    GFX_0('agef_win_burner_r60', 0)
    SFX_0('blaze_normal')
    sprite('ag610_00', 6)	# 642-647
    sprite('ag610_01', 6)	# 648-653
    Unknown26('agef_win_burner_r60')
    GFX_0('agef_win_burner_r75', 0)
    GFX_0('agef_win_burner_somke', 104)
    SFX_0('blaze_normal')
    sprite('ag610_02', 6)	# 654-659
    Unknown26('agef_win_burner_r75')
    GFX_0('agef_win_burner', 0)
    GFX_0('agef_win_burner_line', 0)
    sprite('ag610_03', 6)	# 660-665
    SFX_0('blaze_normal')
    sprite('ag610_04', 6)	# 666-671
    setGravity(210)
    sprite('ag610_03', 6)	# 672-677
    SFX_0('blaze_normal')
    sprite('ag610_04', 6)	# 678-683
    sprite('ag610_05', 3)	# 684-686
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    SFX_0('blaze_normal')
    SFX_1('pag701btg')
    Unknown21011(200)
    sprite('ag610_06', 6)	# 687-692
    setGravity(-150)
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    SFX_0('slash_knife_fast')
    sprite('ag610_07', 5)	# 693-697
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 698-702
    sprite('ag610_07', 5)	# 703-707
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 708-712
    setGravity(150)
    sprite('ag610_07', 5)	# 713-717
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 718-722
    sprite('ag610_07', 5)	# 723-727
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 728-732
    setGravity(-150)
    sprite('ag610_07', 5)	# 733-737
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 738-742
    sprite('ag610_07', 5)	# 743-747
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 748-752
    setGravity(150)
    sprite('ag610_07', 5)	# 753-757
    SFX_0('blaze_normal')
    sprite('ag610_08', 5)	# 758-762
    sprite('ag610_09', 5)	# 763-767
    Unknown21007(24, 40)
    setGravity(-10)
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    SFX_0('blaze_normal')
    sprite('ag610_10', 6)	# 768-773
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner', 0)
    sprite('ag610_11', 20)	# 774-793
    sprite('ag610_12', 5)	# 794-798
    setGravity(-100)
    Unknown26('agef_win_burner')
    GFX_0('agef_win_burner_upper', 0)
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 799-803
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 804-808
    sprite('ag610_13', 5)	# 809-813
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 814-818
    setGravity(-500)
    sprite('ag610_13', 5)	# 819-823
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 824-828
    sprite('ag610_13', 5)	# 829-833
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 834-838
    setGravity(-900)
    sprite('ag610_13', 5)	# 839-843
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 844-848
    sprite('ag610_13', 5)	# 849-853
    SFX_0('blaze_normal')
    sprite('ag610_12', 5)	# 854-858
    sprite('ag610_13', 5)	# 859-863
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 864-868
    sprite('ag610_12', 5)	# 869-873
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 874-878
    sprite('ag610_12', 5)	# 879-883
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 884-888
    sprite('ag610_12', 5)	# 889-893
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 894-898
    sprite('ag610_12', 5)	# 899-903
    SFX_0('blaze_normal')
    sprite('ag610_13', 5)	# 904-908
    sprite('ag610_12', 5)	# 909-913
    SFX_0('blaze_normal')
    sprite('ag610_13', 32767)	# 914-33680
    label(120)
    sprite('ag611_00', 6)	# 33681-33686
    sprite('ag611_01', 20)	# 33687-33706
    sprite('ag611_02', 6)	# 33707-33712
    GFX_0('agef_win2_steam_r', 0)
    GFX_0('agef_win2_steam_l', 1)
    GFX_0('agef_win2_steam_r', 2)
    GFX_0('agef_win2_steam_l', 3)
    GFX_0('agef_win2_steam_r', 4)
    GFX_0('agef_win2_steam_l', 5)
    SFX_3('ag008')
    sprite('ag611_03', 20)	# 33713-33732
    sprite('ag611_03', 20)	# 33733-33752
    Unknown23029(11, 9000, 0)
    SFX_1('pag700pbc')
    sprite('ag611_04', 7)	# 33753-33759
    sprite('ag611_05', 7)	# 33760-33766
    sprite('ag611_06', 18)	# 33767-33784
    sprite('ag611_07', 7)	# 33785-33791
    sprite('ag611_08', 7)	# 33792-33798
    sprite('ag611_09', 7)	# 33799-33805
    label(121)
    sprite('ag611_10', 6)	# 33806-33811
    sprite('ag611_11', 6)	# 33812-33817
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('ag611_10', 1)	# 33818-33818
    Unknown21007(24, 40)
    Unknown21011(360)
    label(122)
    sprite('ag611_10', 6)	# 33819-33824
    sprite('ag611_11', 6)	# 33825-33830
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('ag601_12', 7)	# 33831-33837
    sprite('ag601_09', 7)	# 33838-33844
    SFX_1('pag700uhy')
    label(131)
    sprite('ag601_10', 1)	# 33845-33845
    if SLOT_97:
        _gotolabel(131)
    sprite('ag601_10', 30)	# 33846-33875
    sprite('ag601_10', 32767)	# 33876-66642
    Unknown21007(24, 40)
    Unknown21011(120)
    label(140)
    sprite('ag000_00', 1)	# 66643-66643

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ag000_00', 6)	# 66644-66649
    sprite('ag000_01', 6)	# 66650-66655
    sprite('ag000_02', 6)	# 66656-66661
    sprite('ag000_03', 6)	# 66662-66667
    sprite('ag000_04', 6)	# 66668-66673
    sprite('ag000_05', 6)	# 66674-66679
    sprite('ag000_06', 6)	# 66680-66685
    sprite('ag000_07', 6)	# 66686-66691
    sprite('ag000_08', 6)	# 66692-66697
    sprite('ag000_09', 6)	# 66698-66703
    gotoLabel(141)
    label(142)
    sprite('ag601_12', 7)	# 66704-66710
    sprite('ag601_09', 7)	# 66711-66717
    SFX_1('pag701rrb')
    label(143)
    sprite('ag601_10', 1)	# 66718-66718
    if SLOT_97:
        _gotolabel(143)
    sprite('ag601_10', 30)	# 66719-66748
    sprite('ag601_10', 32767)	# 66749-99515
    Unknown21011(120)
    label(150)
    sprite('ag000_00', 1)	# 99516-99516

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ag000_00', 6)	# 99517-99522
    sprite('ag000_01', 6)	# 99523-99528
    sprite('ag000_02', 6)	# 99529-99534
    sprite('ag000_03', 6)	# 99535-99540
    sprite('ag000_04', 6)	# 99541-99546
    sprite('ag000_05', 6)	# 99547-99552
    sprite('ag000_06', 6)	# 99553-99558
    sprite('ag000_07', 6)	# 99559-99564
    sprite('ag000_08', 6)	# 99565-99570
    sprite('ag000_09', 6)	# 99571-99576
    gotoLabel(151)
    label(152)
    sprite('ag611_00', 6)	# 99577-99582
    sprite('ag611_01', 20)	# 99583-99602
    sprite('ag611_02', 6)	# 99603-99608
    GFX_0('agef_win2_steam_r', 0)
    GFX_0('agef_win2_steam_l', 1)
    GFX_0('agef_win2_steam_r', 2)
    GFX_0('agef_win2_steam_l', 3)
    GFX_0('agef_win2_steam_r', 4)
    GFX_0('agef_win2_steam_l', 5)
    SFX_3('ag008')
    sprite('ag611_03', 20)	# 99609-99628
    sprite('ag611_03', 20)	# 99629-99648
    Unknown23029(11, 9000, 0)
    SFX_1('pag701uva')
    sprite('ag611_04', 7)	# 99649-99655
    sprite('ag611_05', 7)	# 99656-99662
    sprite('ag611_06', 18)	# 99663-99680
    sprite('ag611_07', 7)	# 99681-99687
    sprite('ag611_08', 7)	# 99688-99694
    sprite('ag611_09', 7)	# 99695-99701
    sprite('ag611_10', 6)	# 99702-99707
    sprite('ag611_11', 6)	# 99708-99713
    Unknown23018(1)
    label(153)
    sprite('ag611_10', 6)	# 99714-99719
    sprite('ag611_11', 6)	# 99720-99725
    loopRest()
    gotoLabel(153)
    label(160)
    sprite('ag601_12', 7)	# 99726-99732
    SFX_1('pag700pla')
    sprite('ag601_09', 7)	# 99733-99739
    label(161)
    sprite('ag601_10', 1)	# 99740-99740
    if SLOT_97:
        _gotolabel(161)
    sprite('ag601_10', 20)	# 99741-99760
    sprite('ag601_10', 32767)	# 99761-132527
    Unknown21007(24, 40)
    Unknown21011(300)
    label(170)
    sprite('ag611_00', 6)	# 132528-132533
    sprite('ag611_01', 20)	# 132534-132553
    sprite('ag611_02', 6)	# 132554-132559
    GFX_0('agef_win2_steam_r', 0)
    GFX_0('agef_win2_steam_l', 1)
    GFX_0('agef_win2_steam_r', 2)
    GFX_0('agef_win2_steam_l', 3)
    GFX_0('agef_win2_steam_r', 4)
    GFX_0('agef_win2_steam_l', 5)
    SFX_3('ag008')
    sprite('ag611_03', 20)	# 132560-132579
    sprite('ag611_03', 20)	# 132580-132599
    Unknown23029(11, 9000, 0)
    SFX_1('pag700pmi')
    sprite('ag611_04', 7)	# 132600-132606
    sprite('ag611_05', 7)	# 132607-132613
    sprite('ag611_06', 18)	# 132614-132631
    sprite('ag611_07', 7)	# 132632-132638
    sprite('ag611_08', 7)	# 132639-132645
    sprite('ag611_09', 7)	# 132646-132652
    label(171)
    sprite('ag611_10', 6)	# 132653-132658
    sprite('ag611_11', 6)	# 132659-132664
    loopRest()
    if SLOT_97:
        _gotolabel(171)
    sprite('ag611_10', 1)	# 132665-132665
    Unknown21007(24, 40)
    Unknown21011(240)
    label(172)
    sprite('ag611_10', 6)	# 132666-132671
    sprite('ag611_11', 6)	# 132672-132677
    loopRest()
    gotoLabel(172)
    label(180)
    sprite('ag601_12', 7)	# 132678-132684
    SFX_1('pag700bph')
    sprite('ag601_09', 7)	# 132685-132691
    label(181)
    sprite('ag601_10', 1)	# 132692-132692
    if SLOT_97:
        _gotolabel(181)
    sprite('ag601_10', 20)	# 132693-132712
    sprite('ag601_10', 32767)	# 132713-165479
    Unknown21007(24, 40)
    Unknown21011(280)
    label(190)
    sprite('ag611_00', 6)	# 165480-165485
    sprite('ag611_01', 20)	# 165486-165505
    sprite('ag611_02', 6)	# 165506-165511
    GFX_0('agef_win2_steam_r', 0)
    GFX_0('agef_win2_steam_l', 1)
    GFX_0('agef_win2_steam_r', 2)
    GFX_0('agef_win2_steam_l', 3)
    GFX_0('agef_win2_steam_r', 4)
    GFX_0('agef_win2_steam_l', 5)
    SFX_3('ag008')
    sprite('ag611_03', 20)	# 165512-165531
    sprite('ag611_03', 20)	# 165532-165551
    Unknown23029(11, 9000, 0)
    SFX_1('pag700pak')
    sprite('ag611_04', 7)	# 165552-165558
    sprite('ag611_05', 7)	# 165559-165565
    sprite('ag611_06', 18)	# 165566-165583
    sprite('ag611_07', 7)	# 165584-165590
    sprite('ag611_08', 7)	# 165591-165597
    sprite('ag611_09', 7)	# 165598-165604
    label(191)
    sprite('ag611_10', 6)	# 165605-165610
    sprite('ag611_11', 6)	# 165611-165616
    loopRest()
    if SLOT_97:
        _gotolabel(191)
    sprite('ag611_10', 1)	# 165617-165617
    Unknown21007(24, 40)
    Unknown21011(240)
    label(192)
    sprite('ag611_10', 6)	# 165618-165623
    sprite('ag611_11', 6)	# 165624-165629
    loopRest()
    gotoLabel(192)

@State
def CmnActLose():
    sprite('ag070_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('pag403_0', 100, 879190384, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ag070_01', 6)	# 7-12
    sprite('ag070_02', 2)	# 13-14
    Unknown8000(100, 1, 1)
    sprite('ag070_03', 1)	# 15-15
    sprite('ag070_03', 32767)	# 16-32782
    Unknown21011(60)
    GFX_1('agef_lose', 0)
    GFX_1('agef_lose', 2)