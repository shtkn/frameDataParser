@Subroutine
def PreInit():
    Unknown12019('626a6200000000000000000000000000')

@Subroutine
def MatchInit():
    DashFInitialVelocity(17500)
    DashFAccel(2500)
    DashFMaxVelocity(30000)
    JumpYVelocity(29000)
    Unknown12007(10000)
    Unknown12024(0)
    Unknown13039(4)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('FDash_Turn', 0x1)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Move_EndRegister()
    Move_Register('BDash2FDash', 0x1)
    Move_Input_(0x79)
    Unknown14005(1)
    Unknown14015(600000, 1500000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 370000, -200000, 250000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 250000, -200000, 150000, 1200, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    Unknown14027('NmlAtk4A')
    Unknown14005(1)
    Unknown14015(0, 275000, -200000, 150000, 1200, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    Unknown14027('NmlAtk4A')
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 150000, 1200, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Unknown15015(40, 50)
    Unknown14015(200000, 450000, -200000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown15015(40, 50)
    Unknown14015(0, 400000, -100000, 250000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 450000, -100000, 150000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown14015(-400000, 400000, -200000, 150000, 1000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    Unknown14015(-400000, 400000, -200000, 150000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtk5B3rd', 0x19)
    Unknown14005(1)
    Unknown14015(-400000, 400000, -200000, 150000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtk5B4th', 0x19)
    Unknown14005(1)
    Unknown14015(-400000, 400000, -200000, 150000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtk5B5th', 0x19)
    Unknown14005(1)
    Unknown14015(-50000, 400000, -200000, 50000, 1000, 500)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown15021(6000)
    Unknown14015(-100000, 350000, 100000, 450000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 350000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 650000, -100000, 50000, 500, 10)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 450000, -200000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3036)
    Unknown14015(-400000, 400000, -200000, 150000, 1000, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B2nd', 0x22)
    Unknown14005(1)
    Unknown14015(-400000, 400000, -200000, 150000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B3rd', 0x22)
    Unknown14005(1)
    Unknown14015(-50000, 400000, -200000, 50000, 1000, 500)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-100000, 300000, -500000, -300000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('Assault_Low', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15009()
    Unknown15012(4000)
    Unknown14015(-600000, 450000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('Assault_ChageAttack', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15016(1, 1, 30)
    Unknown14015(-50000, 300000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('Assault_Low_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15009()
    Unknown15012(4000)
    Unknown14015(-600000, 450000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('Assault_Mid', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(4000)
    Unknown14015(-600000, 450000, -100000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('Assault_Multi', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-50000, 300000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('Assault_Mid_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15013(1)
    Unknown15012(4000)
    Unknown14015(-600000, 450000, -100000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('Shiranui_Hagane_236A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('Shiranui_Hagane_Check')
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(500000, 1500000, -400000, 400000, 50, 10)
    Move_EndRegister()
    Move_Register('Shiranui_Hagane_236B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14024('Shiranui_Hagane_Check')
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(500000, 1500000, -400000, 400000, 50, 10)
    Move_EndRegister()
    Move_Register('Shiranui_Hagane_236EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14024('Shiranui_Hagane_Check')
    Unknown15014(1)
    Unknown15012(1)
    Unknown14015(500000, 1500000, -400000, 400000, 50, 10)
    Move_EndRegister()
    Move_Register('Shiranui_Hagane_214A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('Shiranui_Hagane_Check')
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(500000, 1500000, -400000, 400000, 50, 10)
    Move_EndRegister()
    Move_Register('Shiranui_Hagane_214B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14024('Shiranui_Hagane_Check')
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(500000, 1500000, -400000, 400000, 50, 10)
    Move_EndRegister()
    Move_Register('Shiranui_Hagane_214EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14024('Shiranui_Hagane_Check')
    Unknown15014(1)
    Unknown15012(1)
    Unknown14015(500000, 1500000, -400000, 400000, 50, 10)
    Move_EndRegister()
    Move_Register('Rekkouzan_Low', INPUT_SPECIALMOVE)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(-400000, 400000, -200000, 150000, 100, 5)
    Move_EndRegister()
    Move_Register('Rekkouzan_Chage', INPUT_SPECIALMOVE)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14015(-400000, 400000, -200000, 150000, 100, 5)
    Move_EndRegister()
    Move_Register('Rekkouzan_Mid', INPUT_SPECIALMOVE)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14024('AirAssault_Mid_Check')
    Unknown15008()
    Unknown15012(2000)
    Unknown14015(-400000, 350000, -200000, 50000, 100, 5)
    Move_EndRegister()
    Move_Register('Rekkouzan_Multi', INPUT_SPECIALMOVE)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14015(-400000, 400000, -200000, 150000, 100, 1)
    Move_EndRegister()
    Move_Register('Rekkouzan_Low_EX', INPUT_SPECIALMOVE)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(-400000, 400000, -200000, 150000, 100, 5)
    Move_EndRegister()
    Move_Register('Rekkouzan_Mid_EX', INPUT_SPECIALMOVE)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown14024('AirAssault_Mid_Check')
    Unknown15008()
    Unknown15012(2000)
    Unknown14015(-400000, 350000, -200000, 50000, 100, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(7000, 266000, -123000, 655000, 100, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14015(7000, 266000, -123000, 655000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(1)
    Unknown15014(5000)
    Unknown15013(1)
    Unknown15012(0)
    Unknown14015(0, 500000, -200000, 200000, 1, 100)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(1)
    Unknown15014(5000)
    Unknown15013(1)
    Unknown15012(0)
    Unknown14015(0, 500000, -200000, 200000, 1, 100)
    Move_EndRegister()
    Move_Register('UltimateAirAssault', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15012(0)
    Unknown15013(0)
    Unknown14015(50000, 350000, -600000, 200000, 200, 1)
    Move_EndRegister()
    Move_Register('UltimateAirAssault_OD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15012(0)
    Unknown15013(0)
    Unknown14015(50000, 350000, -600000, 200000, 200, 1)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(8000)
    Unknown14015(-300000, 300000, -200000, 300000, 200, 10)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A2nd', 10000000)
    Unknown15024('AN_NmlAtk5A2nd', 'AN_NmlAtk5A3rd', 10000000)
    Unknown15024('AN_NmlAtk5A3rd', 'AN_NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B2nd', 10000000)
    Unknown15024('AN_NmlAtk5B2nd', 'AN_NmlAtk5B3rd', 10000000)
    Unknown15024('AN_NmlAtk5B3rd', 'AN_NmlAtk5B4th', 10000000)
    Unknown15024('AN_NmlAtk5B4th', 'AN_NmlAtk5B5th', 10000000)
    Unknown15024('NmlAtk2C', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5B', 'AN_NmlAtkAIR5B2nd', 10000000)
    Unknown15024('AN_NmlAtkAIR5B2nd', 'AN_NmlAtkAIR5B3rd', 10000000)
    Unknown12018(0, 'jb062_01')
    Unknown12018(1, 'jb062_03')
    Unknown12018(2, 'jb062_04')
    Unknown12018(3, 'jb062_05')
    Unknown12018(4, 'jb062_05')
    Unknown12018(5, 'jb062_06')
    Unknown12018(6, 'jb062_07')
    Unknown12018(7, 'jb041_02')
    Unknown12018(8, 'jb040_02')
    Unknown12018(9, 'jb045_02')
    Unknown12018(10, 'jb060_00')
    Unknown12018(11, 'jb060_01')
    Unknown12018(12, 'jb060_03')
    Unknown12018(13, 'jb060_05')
    Unknown12018(14, 'jb060_07')
    Unknown12018(15, 'jb060_14')
    Unknown12018(16, 'jb050_00')
    Unknown12018(17, 'jb052_00')
    Unknown12018(18, 'jb054_00')
    Unknown12018(25, 'jb063_00')
    Unknown12018(26, 'jb063_01')
    Unknown12018(27, 'jb063_02')
    Unknown12018(28, 'jb063_04')
    Unknown12018(29, 'jb063_10')
    Unknown12018(24, 'jb073_01')
    Unknown7010(0, 'bjb000')
    Unknown7010(1, 'bjb001')
    Unknown7010(2, 'bjb002')
    Unknown7010(3, 'bjb003')
    Unknown7010(4, 'bjb004')
    Unknown7010(5, 'bjb005')
    Unknown7010(6, 'bjb006')
    Unknown7010(7, 'bjb007')
    Unknown7010(8, 'bjb008')
    Unknown7010(9, 'bjb009')
    Unknown7010(10, 'bjb010')
    Unknown7010(15, 'bjb011')
    Unknown7010(16, 'bjb012')
    Unknown7010(17, 'bjb013')
    Unknown7010(18, 'bjb014')
    Unknown7010(19, 'bjb015')
    Unknown7010(20, 'bjb016')
    Unknown7010(21, 'bjb017')
    Unknown7010(22, 'bjb018')
    Unknown7010(23, 'bjb019')
    Unknown7010(24, 'bjb020')
    Unknown7010(25, 'bjb021')
    Unknown7010(28, 'bjb022')
    Unknown7010(29, 'bjb023')
    Unknown7010(30, 'bjb024')
    Unknown7010(31, 'bjb025')
    Unknown7010(32, 'bjb026')
    Unknown7010(33, 'bjb027')
    Unknown7010(34, 'bjb028')
    Unknown7010(35, 'bjb029')
    Unknown7010(36, 'bjb030')
    Unknown7010(37, 'bjb031')
    Unknown7010(39, 'bjb032')
    Unknown7010(42, 'bjb033')
    Unknown7010(43, 'bjb034')
    Unknown7010(44, 'bjb035')
    Unknown7010(45, 'bjb036')
    Unknown7010(46, 'bjb037')
    Unknown7010(47, 'bjb038')
    Unknown7010(48, 'bjb039')
    Unknown7010(49, 'bjb040')
    Unknown7010(50, 'bjb041')
    Unknown7010(52, 'bjb042')
    Unknown7010(53, 'bjb043')
    Unknown7010(54, 'bjb100_0')
    Unknown7010(55, 'bjb100_1')
    Unknown7010(56, 'bjb100_2')
    Unknown7010(63, 'bjb101_0')
    Unknown7010(64, 'bjb101_1')
    Unknown7010(65, 'bjb101_2')
    Unknown7010(57, 'bjb102_0')
    Unknown7010(58, 'bjb102_1')
    Unknown7010(59, 'bjb102_2')
    Unknown7010(66, 'bjb103_0')
    Unknown7010(67, 'bjb103_1')
    Unknown7010(68, 'bjb103_2')
    Unknown7010(60, 'bjb104_0')
    Unknown7010(61, 'bjb104_1')
    Unknown7010(62, 'bjb104_2')
    Unknown7010(69, 'bjb105_0')
    Unknown7010(70, 'bjb105_1')
    Unknown7010(71, 'bjb105_2')
    Unknown7010(72, 'bjb150')
    Unknown7010(73, 'bjb151')
    Unknown7010(74, 'bjb152')
    Unknown7010(85, 'bjb153')
    Unknown7010(87, 'bjb154')
    Unknown7010(88, 'bjb155')
    Unknown7010(96, 'bjb161_0')
    Unknown7010(97, 'bjb161_1')
    Unknown7010(92, 'bjb162_0')
    Unknown7010(93, 'bjb162_1')
    Unknown7010(98, 'bjb163_0')
    Unknown7010(99, 'bjb163_1')
    Unknown7010(100, 'bjb164_0')
    Unknown7010(101, 'bjb164_1')
    Unknown7010(105, 'bjb165_0')
    Unknown7010(106, 'bjb165_1')
    Unknown7010(102, 'bjb166_0')
    Unknown7010(103, 'bjb166_1')
    Unknown7010(90, 'bjb167_0')
    Unknown7010(91, 'bjb167_1')
    Unknown7010(107, 'bjb168_0')
    Unknown7010(108, 'bjb168_1')
    Unknown7010(110, 'bjb169_0')
    Unknown7010(111, 'bjb169_1')
    Unknown7010(94, 'bjb400_0')
    Unknown7010(95, 'bjb400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('04000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnLanding():
    SLOT_61 = 0
    SLOT_63 = 0

@Subroutine
def AirAssault_Mid_Check():
    SLOT_47 = 0
    if (not SLOT_61):
        SLOT_47 = 1

@Subroutine
def Shiranui_Hagane_Check():
    SLOT_47 = 0
    if (not SLOT_63):
        SLOT_47 = 1

@Subroutine
def __4A_AtkData():
    AttackDefaults_StandingNormal()
    AttackLevel_(1)
    PushbackX(12000)
    HitOrBlockJumpCancel(1)
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('CmnActCrushAttack')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('NmlAtkThrow')
    HitOrBlockCancel('NmlAtkBackThrow')

@Subroutine
def DriveInit():
    AttackLevel_(4)
    Damage(1700)
    AttackP2(85)
    Unknown11072(3, -60000, 0)
    PushbackX(0)
    Hitstop(0)
    Unknown11001(12, 24, 29)
    Unknown9016(1)
    HitOverhead(0)
    JumpCancel_(0)
    Unknown13021(1)

    def upon_78():
        clearUponHandler(78)
        clearUponHandler(80)
        GFX_0('Drive_AddAtk', -1)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3001(0)
        if Unknown23148('NmlAtk5A4th'):
            GFX_0('jbef_DriveHit', -1)
        elif Unknown23148('Shiranui_EX'):
            GFX_0('jbef_DriveHit', -1)
        else:
            if Unknown23148('NmlAtkAIR5C'):
                GFX_0('jbef_Air5DHit', -1)
            elif Unknown23148('NmlAtkAIR6C'):
                GFX_0('jbef_Air6DHit', -1)
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            Unknown1084(1)
        sendToLabel(0)
    if SLOT_51:

        def upon_80():
            clearUponHandler(78)
            clearUponHandler(80)
            GFX_0('Drive_AddAtk', -1)
            Unknown1086(22)
            teleportRelativeY(0)
            Unknown3001(0)
            if Unknown23148('NmlAtk5A4th'):
                GFX_0('jbef_DriveHit', -1)
            elif Unknown23148('Shiranui_EX'):
                GFX_0('jbef_DriveHit', -1)
            else:
                if Unknown23148('NmlAtkAIR5C'):
                    GFX_0('jbef_Air5DHit', -1)
                elif Unknown23148('NmlAtkAIR6C'):
                    GFX_0('jbef_Air6DHit', -1)
                clearUponHandler(2)
                Unknown8000(100, 1, 1)
                Unknown1084(1)
            sendToLabel(0)

    def upon_STATE_END():
        Unknown2006()
        Unknown3001(255)

@Subroutine
def Drive_DeriveInputBegin():
    Unknown14070('Assault_Mid')
    Unknown14070('Assault_ChageAttack')
    Unknown14070('Assault_Low')
    Unknown14070('Assault_Multi')
    Unknown14070('Assault_Mid_EX')
    Unknown14070('Assault_Low_EX')
    Unknown14070('UltimateAssault')
    Unknown14070('UltimateAssault_OD')
    Unknown14070('CmnActInvincibleAttack')
    Unknown14070('AstralHeat')

@Subroutine
def Drive_DeriveTimingBegin():
    Unknown14072('Assault_Mid')
    Unknown14072('Assault_ChageAttack')
    Unknown14072('Assault_Low')
    Unknown14072('Assault_Multi')
    Unknown14072('Assault_Mid_EX')
    Unknown14072('Assault_Low_EX')
    Unknown14072('UltimateAssault')
    Unknown14072('UltimateAssault_OD')
    Unknown14072('CmnActInvincibleAttack')
    Unknown14072('AstralHeat')

@Subroutine
def Rekkouzan_Atk():
    AttackLevel_(4)
    Damage(1200)
    AttackP1(80)
    AirPushbackX(24000)
    AirPushbackY(8000)
    Unknown9154(19)
    AirUntechableTime(21)
    Hitstop(7)
    Unknown11028(14)
    Unknown9016(1)
    Unknown23085(1)
    JumpCancel_(0)

@Subroutine
def Rekkouzan_Finish_Atk():
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(15000)
    AirPushbackY(25000)
    AirUntechableTime(40)
    Hitstop(11)
    Unknown11001(0, 2, 4)
    Unknown11058('0100000000000000000000000000000000000000')

@Subroutine
def Rekkouzan_DeriveInputBegin():
    Unknown14070('Rekkouzan_Low')
    Unknown14070('Rekkouzan_Mid')
    Unknown14070('Rekkouzan_Multi')
    Unknown14070('Rekkouzan_Chage')
    Unknown14070('Rekkouzan_Low_EX')
    Unknown14070('Rekkouzan_Mid_EX')
    Unknown14070('CmnActInvincibleAttack')
    Unknown14070('CmnActInvincibleAttackAir')
    Unknown14070('UltimateAssault')
    Unknown14070('UltimateAssault_OD')
    Unknown14070('UltimateAirAssault')
    Unknown14070('UltimateAirAssault_OD')
    Unknown14070('AstralHeat')

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        if Unknown23148('NmlAtk5B2nd'):
            Unknown14070('NmlAtk5B3rd')
        if Unknown23148('NmlAtk5B4th'):
            Unknown14070('NmlAtk5B5th')
        if Unknown23148('NmlAtkAIR5B2nd'):
            Unknown14070('NmlAtkAIR5B3rd')
        Unknown14072('NmlAtk5B2nd')
        Unknown14072('NmlAtk5B3rd')
        Unknown14072('NmlAtk5B4th')
        Unknown14072('NmlAtk5B5th')
        Unknown14072('NmlAtkAIR5B2nd')
        Unknown14072('NmlAtkAIR5B3rd')
        Unknown14072('Rekkouzan_Low')
        Unknown14072('Rekkouzan_Mid')
        Unknown14072('Rekkouzan_Multi')
        Unknown14072('Rekkouzan_Chage')
        Unknown14072('Rekkouzan_Low_EX')
        Unknown14072('Rekkouzan_Mid_EX')
        Unknown14072('CmnActInvincibleAttack')
        Unknown14072('CmnActInvincibleAttackAir')
        Unknown14072('UltimateAssault')
        Unknown14072('UltimateAssault_OD')
        Unknown14072('UltimateAirAssault')
        Unknown14072('UltimateAirAssault_OD')
        Unknown14072('AstralHeat')

@Subroutine
def Rekkouzan_DeriveTimingBegin():
    Unknown14072('NmlAtk5B2nd')
    Unknown14072('NmlAtk5B3rd')
    Unknown14072('NmlAtk5B4th')
    Unknown14072('NmlAtk5B5th')
    Unknown14072('NmlAtkAIR5B2nd')
    Unknown14072('NmlAtkAIR5B3rd')
    Unknown14072('Rekkouzan_Low')
    Unknown14072('Rekkouzan_Mid')
    Unknown14072('Rekkouzan_Multi')
    Unknown14072('Rekkouzan_Chage')
    Unknown14072('Rekkouzan_Low_EX')
    Unknown14072('Rekkouzan_Mid_EX')
    Unknown14072('UltimateAssault')
    Unknown14072('UltimateAssault_OD')
    Unknown14072('UltimateAirAssault')
    Unknown14072('UltimateAirAssault_OD')
    Unknown14072('AstralHeat')

@Subroutine
def Rekkouzan_DeriveClear():
    Unknown14074('NmlAtk5B2nd')
    Unknown14074('NmlAtk5B3rd')
    Unknown14074('NmlAtk5B4th')
    Unknown14074('NmlAtk5B5th')
    Unknown14074('NmlAtkAIR5B2nd')
    Unknown14074('NmlAtkAIR5B3rd')
    Unknown14074('Rekkouzan_Low')
    Unknown14074('Rekkouzan_Mid')
    Unknown14074('Rekkouzan_Multi')
    Unknown14074('Rekkouzan_Chage')
    Unknown14074('Rekkouzan_Low_EX')
    Unknown14074('Rekkouzan_Mid_EX')
    Unknown14074('CmnActInvincibleAttack')
    Unknown14074('CmnActInvincibleAttackAir')
    Unknown14074('UltimateAssault')
    Unknown14074('UltimateAssault_OD')
    Unknown14074('UltimateAirAssault')
    Unknown14074('UltimateAirAssault_OD')
    Unknown14074('AstralHeat')

@Subroutine
def Assault_Low_Atk():
    AttackLevel_(4)
    Damage(2000)
    AttackP1(90)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackY(25000)
    AirPushbackX(2000)
    YImpluseBeforeWallbounce(3000)
    AirUntechableTime(30)
    HitLow(2)
    Unknown9016(1)
    Unknown11058('0000000000000000010000000000000000000000')

    def upon_12():
        clearUponHandler(12)
        Hitstop(20)
        ScreenShake(5000, 3000)

@Subroutine
def Assault_Chage_Atk():
    AttackLevel_(5)
    Damage(2400)
    AttackP2(80)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(3500)
    AirPushbackY(32000)
    YImpluseBeforeWallbounce(1800)
    AirUntechableTime(60)
    PushbackX(19800)
    Hitstop(20)
    Unknown9016(1)

    def upon_ON_HIT_OR_BLOCK():
        ScreenShake(8000, 8000)

    def upon_3():
        if (SLOT_18 == 30):
            if (not SLOT_2):
                Unknown10000(120)
                AttackP2(90)
                AirPushbackY(35000)
                Unknown8004(100, 1, 1)
                Unknown2037(1)
        if SLOT_37:
            if (SLOT_18 >= 44):
                sendToLabel(9)
            if (SLOT_18 >= 17):
                if (not SLOT_2):
                    if CheckInput(0xe):
                        sendToLabel(8)

@Subroutine
def Assault_Mid_Atk():
    AttackLevel_(4)
    Damage(1800)
    AttackP1(80)
    AirPushbackX(20000)
    AirPushbackY(-50000)
    Unknown9202(1)
    Unknown9154(23)
    AirUntechableTime(40)
    Unknown9310(1)
    PushbackX(19800)
    HitOverhead(2)
    Unknown9016(1)
    Unknown11058('0100000000000000000000000000000000000000')

@Subroutine
def Assault_Multi_Atk():
    AttackLevel_(3)
    Damage(500)
    AttackP1(80)
    AttackP2(95)
    AirPushbackY(-20000)
    PushbackX(12000)
    AirUntechableTime(60)
    Unknown9310(10)
    Hitstop(1)
    Unknown11001(0, -1, -1)
    Unknown9016(1)
    Unknown11057(600)
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown11056(0)

@Subroutine
def Assault_MultiFinish_Atk():
    Damage(1500)
    Hitstop(11)
    Unknown11001(0, 0, 2)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(20000)
    Unknown9095()
    PushbackX(19800)
    Unknown9310(-1)
    Unknown11057(1000)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown11056(1)

@State
def CmnActStand():
    label(0)
    sprite('jb000_00', 7)	# 1-7	 **attackbox here**
    sprite('jb000_01', 7)	# 8-14	 **attackbox here**
    sprite('jb000_02', 7)	# 15-21	 **attackbox here**
    sprite('jb000_03', 7)	# 22-28	 **attackbox here**
    sprite('jb000_04', 7)	# 29-35	 **attackbox here**
    sprite('jb000_05', 7)	# 36-42	 **attackbox here**
    sprite('jb000_06', 7)	# 43-49	 **attackbox here**
    sprite('jb000_07', 7)	# 50-56	 **attackbox here**
    sprite('jb000_08', 7)	# 57-63	 **attackbox here**
    sprite('jb000_09', 7)	# 64-70	 **attackbox here**
    if SLOT_87:
        if (not SLOT_122):
            if random_(2, 0, 10):
                sendToLabel(9)
    loopRest()
    sprite('jb000_00ex01', 7)	# 71-77	 **attackbox here**
    sprite('jb000_01ex01', 7)	# 78-84	 **attackbox here**
    sprite('jb000_02ex01', 7)	# 85-91	 **attackbox here**
    sprite('jb000_03ex01', 7)	# 92-98	 **attackbox here**
    sprite('jb000_04ex01', 7)	# 99-105	 **attackbox here**
    sprite('jb000_05ex01', 7)	# 106-112	 **attackbox here**
    sprite('jb000_06ex01', 7)	# 113-119	 **attackbox here**
    sprite('jb000_07ex01', 7)	# 120-126	 **attackbox here**
    sprite('jb000_08ex01', 7)	# 127-133	 **attackbox here**
    sprite('jb000_09ex01', 7)	# 134-140	 **attackbox here**
    if SLOT_87:
        if (not SLOT_122):
            if random_(2, 0, 10):
                sendToLabel(9)
    loopRest()
    sprite('jb000_00ex02', 7)	# 141-147	 **attackbox here**
    sprite('jb000_01ex02', 7)	# 148-154	 **attackbox here**
    sprite('jb000_02ex02', 7)	# 155-161	 **attackbox here**
    sprite('jb000_03ex02', 7)	# 162-168	 **attackbox here**
    sprite('jb000_04ex02', 7)	# 169-175	 **attackbox here**
    sprite('jb000_05ex02', 7)	# 176-182	 **attackbox here**
    sprite('jb000_06ex02', 7)	# 183-189	 **attackbox here**
    sprite('jb000_07ex02', 7)	# 190-196	 **attackbox here**
    sprite('jb000_08ex02', 7)	# 197-203	 **attackbox here**
    sprite('jb000_09ex02', 7)	# 204-210	 **attackbox here**
    if SLOT_87:
        if (not SLOT_122):
            if random_(2, 0, 10):
                sendToLabel(9)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('jb001_00', 6)	# 211-216
    SLOT_88 = 960
    sprite('jb001_01', 6)	# 217-222
    sprite('jb001_02', 6)	# 223-228
    SFX_1('bjb000')
    sprite('jb001_03', 6)	# 229-234
    sprite('jb001_04', 8)	# 235-242
    sprite('jb001_06', 8)	# 243-250
    sprite('jb001_04', 8)	# 251-258
    sprite('jb001_06', 8)	# 259-266
    sprite('jb001_04', 8)	# 267-274
    sprite('jb001_06', 8)	# 275-282
    sprite('jb001_04', 8)	# 283-290
    sprite('jb001_03', 9)	# 291-299
    sprite('jb001_02', 9)	# 300-308
    sprite('jb001_01', 9)	# 309-317
    sprite('jb001_00', 9)	# 318-326
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('jb003_00ex00', 3)	# 1-3
    sprite('jb003_01', 3)	# 4-6
    sprite('jb003_00', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('jb010_00', 4)	# 1-4	 **attackbox here**
    sprite('jb010_01', 4)	# 5-8	 **attackbox here**

@State
def CmnActCrouch():
    label(0)
    sprite('jb010_02', 7)	# 1-7	 **attackbox here**
    sprite('jb010_03', 7)	# 8-14	 **attackbox here**
    sprite('jb010_04', 7)	# 15-21	 **attackbox here**
    sprite('jb010_05', 7)	# 22-28	 **attackbox here**
    sprite('jb010_06', 7)	# 29-35	 **attackbox here**
    sprite('jb010_07', 7)	# 36-42	 **attackbox here**
    sprite('jb010_08', 7)	# 43-49	 **attackbox here**
    sprite('jb010_09', 7)	# 50-56	 **attackbox here**
    sprite('jb010_10', 7)	# 57-63	 **attackbox here**
    sprite('jb010_11', 7)	# 64-70	 **attackbox here**
    sprite('jb010_02ex01', 7)	# 71-77	 **attackbox here**
    sprite('jb010_03ex01', 7)	# 78-84	 **attackbox here**
    sprite('jb010_04ex01', 7)	# 85-91	 **attackbox here**
    sprite('jb010_05ex01', 7)	# 92-98	 **attackbox here**
    sprite('jb010_06ex01', 7)	# 99-105	 **attackbox here**
    sprite('jb010_07ex01', 7)	# 106-112	 **attackbox here**
    sprite('jb010_08ex01', 7)	# 113-119	 **attackbox here**
    sprite('jb010_09ex01', 7)	# 120-126	 **attackbox here**
    sprite('jb010_10ex01', 7)	# 127-133	 **attackbox here**
    sprite('jb010_11ex01', 7)	# 134-140	 **attackbox here**
    sprite('jb010_02ex02', 7)	# 141-147	 **attackbox here**
    sprite('jb010_03ex02', 7)	# 148-154	 **attackbox here**
    sprite('jb010_04ex02', 7)	# 155-161	 **attackbox here**
    sprite('jb010_05ex02', 7)	# 162-168	 **attackbox here**
    sprite('jb010_06ex02', 7)	# 169-175	 **attackbox here**
    sprite('jb010_07ex02', 7)	# 176-182	 **attackbox here**
    sprite('jb010_08ex02', 7)	# 183-189	 **attackbox here**
    sprite('jb010_09ex02', 7)	# 190-196	 **attackbox here**
    sprite('jb010_10ex02', 7)	# 197-203	 **attackbox here**
    sprite('jb010_11ex02', 7)	# 204-210	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('jb013_00ex00', 3)	# 1-3
    sprite('jb013_01', 3)	# 4-6
    sprite('jb013_00', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('jb010_01', 4)	# 1-4	 **attackbox here**
    sprite('jb010_00', 4)	# 5-8	 **attackbox here**

@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        if SLOT_37:
            JumpYVelocity(29000)
        if SLOT_36:
            JumpYVelocity(34000)
        if Unknown23145('BDash2FDash'):
            Unknown1051(60)
    sprite('jb023_00', 2)	# 1-2
    sprite('jb023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('jb020_00', 4)	# 1-4
    sprite('jb020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('jb020_02', 3)	# 1-3
    sprite('jb020_03', 3)	# 4-6
    sprite('jb020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    Unknown23145('Shiranui_Hagane_214A')
    if SLOT_0:
        _gotolabel(0)
    sprite('jb020_05', 3)	# 1-3
    sprite('jb020_06', 3)	# 4-6
    label(0)
    sprite('jb020_07', 4)	# 7-10
    sprite('jb020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('jb024_00', 3)	# 1-3
    sprite('jb024_01', 3)	# 4-6
    sprite('jb024_02', 3)	# 7-9
    sprite('jb024_03', 3)	# 10-12
    sprite('jb024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('jb024_00', 2)	# 1-2
    sprite('jb024_01', 2)	# 3-4
    sprite('jb024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('jb024_03', 3)	# 1-3
    sprite('jb024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('jb030_00', 7)	# 1-7
    label(0)
    sprite('jb030_01', 7)	# 8-14
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb030_02', 7)	# 15-21
    sprite('jb030_03', 7)	# 22-28
    sprite('jb030_04', 7)	# 29-35
    sprite('jb030_05', 7)	# 36-42
    sprite('jb030_06', 7)	# 43-49
    sprite('jb030_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb030_08', 7)	# 57-63
    sprite('jb030_09', 7)	# 64-70
    sprite('jb030_10', 7)	# 71-77
    sprite('jb030_11', 7)	# 78-84
    sprite('jb030_12', 7)	# 85-91
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('jb031_00', 7)	# 1-7
    label(0)
    sprite('jb031_01', 7)	# 8-14
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb031_02', 7)	# 15-21
    sprite('jb031_03', 7)	# 22-28
    sprite('jb031_04', 7)	# 29-35
    sprite('jb031_05', 7)	# 36-42
    sprite('jb031_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('jb031_07', 7)	# 50-56
    sprite('jb031_08', 7)	# 57-63
    sprite('jb031_09', 7)	# 64-70
    sprite('jb031_10', 7)	# 71-77
    sprite('jb031_11', 7)	# 78-84
    sprite('jb031_12', 7)	# 85-91
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            if CheckInput(0x5e):
                Unknown1051(0)
            elif CheckInput(0x37):
                Unknown1051(0)
    sprite('jb030_00', 4)	# 1-4
    sprite('jb032_00', 2)	# 5-6
    sprite('jb032_01', 2)	# 7-8
    label(0)
    sprite('jb032_02', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('jb032_03', 3)	# 13-15
    sprite('jb032_04', 3)	# 16-18
    sprite('jb032_05', 4)	# 19-22
    Unknown8006(100, 1, 1)
    sprite('jb032_06', 3)	# 23-25
    sprite('jb032_07', 3)	# 26-28
    sprite('jb032_08', 3)	# 29-31
    loopRest()
    gotoLabel(0)

@State
def FDash_Turn():

    def upon_IMMEDIATE():
        Unknown17013()
        Unknown23001(100, 100)
        Unknown2018(0, 50)
        sendToLabelUpon(2, 1)
    sprite('jb033_00', 3)	# 1-3
    Unknown1084(1)
    sprite('jb033_01', 3)	# 4-6
    Unknown2005()
    Unknown23072()
    Unknown8002()
    physicsXImpulse(-20000)
    physicsYImpulse(15800)
    setGravity(2400)
    Unknown2017(0)
    Unknown2015(40)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    SFX_1('bjb005')

    def upon_3():
        if SLOT_38:
            if (SLOT_40 <= 0):
                clearUponHandler(3)
                Unknown23072()
        elif (SLOT_40 >= 0):
            clearUponHandler(3)
            Unknown23072()
    sprite('jb033_02', 3)	# 7-9
    sprite('jb033_03', 3)	# 10-12
    sprite('jb033_04', 3)	# 13-15
    sprite('jb033_05', 32767)	# 16-32782
    setInvincible(0)
    Unknown2017(1)
    loopRest()
    label(1)
    sprite('jb033_06', 3)	# 32783-32785
    clearUponHandler(3)
    Unknown8000(100, 1, 1)
    Unknown2018(1, 50)
    Unknown2015(-1)
    setInvincible(0)
    Unknown1084(1)
    sprite('jb033_07', 3)	# 32786-32788
    sprite('jb033_08', 3)	# 32789-32791
    sprite('jb033_09', 3)	# 32792-32794

@State
def CmnActFDashStop():

    def upon_IMMEDIATE():

        def upon_3():
            if CheckInput(0x5e):
                Unknown1051(0)
            elif CheckInput(0x37):
                Unknown1051(0)
    sprite('jb032_09', 2)	# 1-2
    sprite('jb032_10', 3)	# 3-5
    sprite('jb032_11', 3)	# 6-8
    clearUponHandler(3)
    sprite('jb032_12', 2)	# 9-10
    sprite('jb032_13', 2)	# 11-12
    sprite('jb032_14', 2)	# 13-14

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        Unknown1084(1)
        sendToLabelUpon(2, 0)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('jb033_00', 1)	# 1-1
    sprite('jb033_01', 3)	# 2-4
    physicsXImpulse(-18000)
    Unknown1028(-1000)
    physicsYImpulse(15800)
    setGravity(2400)
    Unknown8002()
    sprite('jb033_02', 3)	# 5-7
    sprite('jb033_03', 3)	# 8-10
    sprite('jb033_04', 3)	# 11-13
    sprite('jb033_05', 32767)	# 14-32780
    Unknown14070('BDash2FDash')
    loopRest()
    label(0)
    sprite('jb033_06', 1)	# 32781-32781
    Unknown14072('BDash2FDash')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('jb033_07', 1)	# 32782-32782
    Unknown14074('BDash2FDash')
    sprite('jb033_08', 2)	# 32783-32784
    sprite('jb033_09', 3)	# 32785-32787

@State
def BDash2FDash():

    def upon_IMMEDIATE():
        Unknown28(8, '_NEUTRAL')
    sprite('jb033_06', 2)	# 1-2
    sprite('jb033_07', 2)	# 3-4
    sprite('jb033_08', 2)	# 5-6
    sprite('jb032_01', 2)	# 7-8
    Unknown8006(100, 1, 1)
    Unknown3029(1)
    Unknown1084(1)
    Unknown1045(75000)
    teleportRelativeX(15000)
    sprite('jb032_02', 2)	# 9-10
    Unknown13014(1)
    Unknown13015(1)
    Unknown13008(1)
    sprite('jb032_03', 2)	# 11-12
    sprite('jb032_04', 2)	# 13-14
    sprite('jb032_12', 2)	# 15-16
    sprite('jb032_13', 2)	# 17-18
    sprite('jb032_14', 2)	# 19-20

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('jb035_00', 3)	# 1-3
    label(0)
    sprite('jb035_01', 3)	# 4-6
    sprite('jb035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('jb036_00', 3)	# 1-3
    label(0)
    sprite('jb036_01', 3)	# 4-6
    sprite('jb036_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('jb050_00', 1)	# 1-1
    sprite('jb050_01', 1)	# 2-2
    sprite('jb050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('jb050_01', 1)	# 1-1
    sprite('jb050_02', 1)	# 2-2
    sprite('jb050_01', 2)	# 3-4
    sprite('jb050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('jb050_02', 1)	# 1-1
    sprite('jb050_03', 1)	# 2-2
    sprite('jb050_02', 2)	# 3-4
    sprite('jb050_01', 2)	# 5-6
    sprite('jb050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('jb050_03', 1)	# 1-1
    sprite('jb050_04', 1)	# 2-2
    sprite('jb050_03', 2)	# 3-4
    sprite('jb050_02', 2)	# 5-6
    sprite('jb050_01', 2)	# 7-8
    sprite('jb050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('jb050_04', 1)	# 1-1
    sprite('jb050_04', 1)	# 2-2
    sprite('jb050_04', 2)	# 3-4
    sprite('jb050_03', 2)	# 5-6
    sprite('jb050_02', 2)	# 7-8
    sprite('jb050_01', 2)	# 9-10
    sprite('jb050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('jb052_00', 1)	# 1-1
    sprite('jb052_01', 1)	# 2-2
    sprite('jb052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('jb052_01', 1)	# 1-1
    sprite('jb052_02', 1)	# 2-2
    sprite('jb052_01', 2)	# 3-4
    sprite('jb052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('jb052_02', 1)	# 1-1
    sprite('jb052_03', 1)	# 2-2
    sprite('jb052_02', 2)	# 3-4
    sprite('jb052_01', 2)	# 5-6
    sprite('jb052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('jb052_03', 1)	# 1-1
    sprite('jb052_04', 1)	# 2-2
    sprite('jb052_03', 2)	# 3-4
    sprite('jb052_02', 2)	# 5-6
    sprite('jb052_01', 2)	# 7-8
    sprite('jb052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('jb052_04', 1)	# 1-1
    sprite('jb052_04', 1)	# 2-2
    sprite('jb052_04', 2)	# 3-4
    sprite('jb052_03', 2)	# 5-6
    sprite('jb052_02', 2)	# 7-8
    sprite('jb052_01', 2)	# 9-10
    sprite('jb052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('jb054_00', 1)	# 1-1
    sprite('jb054_01', 1)	# 2-2
    sprite('jb054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('jb054_01', 1)	# 1-1
    sprite('jb054_02', 1)	# 2-2
    sprite('jb054_01', 2)	# 3-4
    sprite('jb054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('jb054_02', 1)	# 1-1
    sprite('jb054_03', 1)	# 2-2
    sprite('jb054_02', 2)	# 3-4
    sprite('jb054_01', 2)	# 5-6
    sprite('jb054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('jb054_03', 1)	# 1-1
    sprite('jb054_04', 1)	# 2-2
    sprite('jb054_03', 2)	# 3-4
    sprite('jb054_02', 2)	# 5-6
    sprite('jb054_01', 2)	# 7-8
    sprite('jb054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('jb054_04', 1)	# 1-1
    sprite('jb054_04', 1)	# 2-2
    sprite('jb054_04', 2)	# 3-4
    sprite('jb054_03', 2)	# 5-6
    sprite('jb054_02', 2)	# 7-8
    sprite('jb054_01', 2)	# 9-10
    sprite('jb054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('jb060_00', 4)	# 1-4
    label(0)
    sprite('jb060_01', 4)	# 5-8
    sprite('jb060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('jb060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('jb062_05', 3)	# 1-3
    sprite('jb062_06', 3)	# 4-6
    label(0)
    sprite('jb062_07', 3)	# 7-9
    sprite('jb062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('jb060_07', 2)	# 1-2
    sprite('jb060_08', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('jb060_09', 3)	# 1-3
    sprite('jb060_10', 3)	# 4-6
    sprite('jb060_11', 3)	# 7-9
    sprite('jb060_12', 3)	# 10-12
    sprite('jb060_13', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('jb060_14', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('jb061_00', 3)	# 1-3
    sprite('jb061_01', 3)	# 4-6
    sprite('jb061_02', 3)	# 7-9
    sprite('jb061_03', 3)	# 10-12
    sprite('jb061_04', 3)	# 13-15
    sprite('jb061_05', 3)	# 16-18
    sprite('jb061_06', 3)	# 19-21
    sprite('jb061_07', 3)	# 22-24
    sprite('jb061_08', 4)	# 25-28

@State
def CmnActFDownUpper():
    sprite('jb063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('jb063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('jb063_02', 3)	# 1-3
    sprite('jb063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('jb063_04', 3)	# 1-3
    sprite('jb063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('jb063_06', 2)	# 1-2
    sprite('jb063_07', 2)	# 3-4
    sprite('jb063_08', 3)	# 5-7
    sprite('jb063_09', 3)	# 8-10
    sprite('jb063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('jb063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('jb064_00', 2)	# 1-2
    sprite('jb064_01', 2)	# 3-4
    sprite('jb064_02', 2)	# 5-6
    sprite('jb064_03', 2)	# 7-8
    sprite('jb064_04', 2)	# 9-10
    sprite('jb064_05', 2)	# 11-12
    sprite('jb064_06', 2)	# 13-14
    sprite('jb064_07', 2)	# 15-16
    sprite('jb064_08', 3)	# 17-19
    sprite('jb064_09', 3)	# 20-22

@State
def CmnActVDownUpper():
    sprite('jb062_00', 3)	# 1-3
    label(0)
    sprite('jb062_01', 3)	# 4-6
    sprite('jb062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('jb062_03', 3)	# 1-3
    sprite('jb062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('jb062_05', 3)	# 1-3
    sprite('jb062_06', 3)	# 4-6
    label(0)
    sprite('jb062_07', 3)	# 7-9
    sprite('jb062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('jb062_09', 2)	# 1-2
    sprite('jb062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('jb072_00', 3)	# 1-3
    sprite('jb072_01', 3)	# 4-6
    sprite('jb072_02', 3)	# 7-9
    label(0)
    sprite('jb072_01', 3)	# 10-12
    sprite('jb072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('jb074_00', 3)	# 1-3
    sprite('jb074_01', 3)	# 4-6
    sprite('jb074_02', 3)	# 7-9
    sprite('jb074_03', 3)	# 10-12
    sprite('jb074_04', 3)	# 13-15
    sprite('jb074_05', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('jb082_00', 3)	# 1-3
    sprite('jb082_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('jb071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('jb073_00', 3)	# 1-3
    sprite('jb073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('jb073_02', 3)	# 1-3
    label(0)
    sprite('jb073_03', 3)	# 4-6
    sprite('jb073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('jb070_00', 2)	# 1-2
    sprite('jb070_01', 2)	# 3-4
    label(0)
    sprite('jb070_02', 3)	# 5-7
    sprite('jb070_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('jb070_04', 4)	# 1-4
    sprite('jb070_05', 4)	# 5-8
    sprite('jb070_06', 4)	# 9-12
    sprite('jb070_07', 4)	# 13-16
    sprite('jb070_08', 4)	# 17-20
    sprite('jb070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('jb070_10', 2)	# 1-2
    sprite('jb070_11', 2)	# 3-4
    sprite('jb070_12', 2)	# 5-6
    sprite('jb070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('jb113_00', 3)	# 1-3
    sprite('jb113_01', 3)	# 4-6
    sprite('jb113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('jb113_00', 3)	# 1-3
    sprite('jb113_01', 3)	# 4-6
    sprite('jb113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('jb113_00', 3)	# 1-3
    sprite('jb113_01', 3)	# 4-6
    sprite('jb113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('jb110_00', 2)	# 1-2
    sprite('jb110_01', 2)	# 3-4
    sprite('jb110_02', 2)	# 5-6
    sprite('jb110_03', 2)	# 7-8
    sprite('jb110_04', 2)	# 9-10
    sprite('jb110_05', 2)	# 11-12
    sprite('jb110_06', 2)	# 13-14
    sprite('jb110_07', 2)	# 15-16
    sprite('jb110_08', 2)	# 17-18
    sprite('jb110_09', 2)	# 19-20
    sprite('jb110_10', 2)	# 21-22
    sprite('jb110_11', 2)	# 23-24
    sprite('jb110_12', 200)	# 25-224
    sprite('jb110_13', 3)	# 225-227
    sprite('jb110_14', 3)	# 228-230

@State
def CmnActUkemiLandB():
    sprite('jb111_00', 2)	# 1-2
    sprite('jb111_01', 2)	# 3-4
    sprite('jb111_02', 2)	# 5-6
    sprite('jb111_03', 2)	# 7-8
    sprite('jb111_04', 2)	# 9-10
    sprite('jb111_05', 2)	# 11-12
    sprite('jb111_06', 2)	# 13-14
    sprite('jb111_07', 2)	# 15-16
    sprite('jb111_08', 2)	# 17-18
    sprite('jb111_09', 2)	# 19-20
    sprite('jb111_10', 2)	# 21-22
    sprite('jb111_11', 2)	# 23-24
    sprite('jb111_12', 200)	# 25-224
    sprite('jb111_13', 3)	# 225-227
    sprite('jb111_14', 3)	# 228-230

@State
def CmnActUkemiLandN():
    sprite('jb112_00', 2)	# 1-2
    sprite('jb112_01', 2)	# 3-4
    sprite('jb112_02', 2)	# 5-6
    sprite('jb112_03', 2)	# 7-8
    sprite('jb112_04', 2)	# 9-10
    sprite('jb112_05', 2)	# 11-12
    sprite('jb112_06', 2)	# 13-14
    sprite('jb112_07', 2)	# 15-16
    sprite('jb112_08', 2)	# 17-18
    sprite('jb112_09', 2)	# 19-20
    sprite('jb112_10', 2)	# 21-22

@State
def CmnActUkemiLandNLanding():
    sprite('jb024_00', 3)	# 1-3
    sprite('jb024_01', 3)	# 4-6
    sprite('jb024_02', 3)	# 7-9
    sprite('jb024_03', 3)	# 10-12
    sprite('jb024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('jb040_00', 3)	# 1-3
    sprite('jb040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('jb040_02', 4)	# 1-4
    sprite('jb040_03', 4)	# 5-8
    sprite('jb040_04', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('jb040_01', 3)	# 1-3
    sprite('jb040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('jb040_05', 3)	# 1-3
    label(0)
    sprite('jb040_02', 4)	# 4-7
    sprite('jb040_03', 4)	# 8-11
    sprite('jb040_04', 4)	# 12-15
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('jb040_01', 3)	# 1-3
    sprite('jb040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('jb041_00', 3)	# 1-3
    sprite('jb041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('jb041_02', 4)	# 1-4
    sprite('jb041_03', 4)	# 5-8
    sprite('jb041_04', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('jb041_01', 3)	# 1-3
    sprite('jb041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('jb041_05', 3)	# 1-3
    label(0)
    sprite('jb041_02', 4)	# 4-7
    sprite('jb041_03', 4)	# 8-11
    sprite('jb041_04', 4)	# 12-15
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('jb041_01', 3)	# 1-3
    sprite('jb041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('jb043_00', 3)	# 1-3
    sprite('jb043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('jb043_02', 4)	# 1-4
    sprite('jb043_03', 4)	# 5-8
    sprite('jb043_04', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('jb043_01', 3)	# 1-3
    sprite('jb043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('jb043_05', 3)	# 1-3
    label(0)
    sprite('jb043_02', 4)	# 4-7
    sprite('jb043_03', 4)	# 8-11
    sprite('jb043_04', 4)	# 12-15
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('jb043_01', 3)	# 1-3
    sprite('jb043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('jb045_00', 3)	# 1-3
    sprite('jb045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('jb045_02', 4)	# 1-4
    sprite('jb045_03', 4)	# 5-8
    sprite('jb045_03', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('jb045_01', 3)	# 1-3
    sprite('jb045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('jb045_05', 3)	# 1-3
    label(0)
    sprite('jb045_02', 4)	# 4-7
    sprite('jb045_03', 4)	# 8-11
    sprite('jb045_04', 4)	# 12-15
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('jb045_01', 3)	# 1-3
    sprite('jb045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('jb090_00', 2)	# 1-2
    sprite('jb090_01', 2)	# 3-4
    sprite('jb090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('jb090_03', 6)	# 6-11
    sprite('jb090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('jb091_00', 2)	# 1-2
    sprite('jb091_01', 2)	# 3-4
    sprite('jb091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('jb091_03', 6)	# 6-11
    sprite('jb091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('jb092_00', 2)	# 1-2
    sprite('jb092_01', 2)	# 3-4
    sprite('jb092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('jb092_03', 6)	# 6-11
    sprite('jb092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('jb025_00ex00', 3)	# 1-3
    sprite('jb025_01', 3)	# 4-6
    sprite('jb025_00', 3)	# 7-9

@State
def CmnActLockWait():
    sprite('jb040_02', 1)	# 1-1
    sprite('jb040_01', 3)	# 2-4
    sprite('jb040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('jb312_00', 3)	# 1-3
    sprite('jb312_01', 3)	# 4-6
    sprite('jb312_02', 5)	# 7-11
    sprite('jb312_03', 2)	# 12-13
    sprite('jb312_04', 8)	# 14-21	 **attackbox here**
    sprite('jb312_05', 3)	# 22-24
    sprite('jb312_06', 3)	# 25-27
    sprite('jb312_07', 2)	# 28-29

@State
def CmnActAirLockWait():
    sprite('jb045_02', 1)	# 1-1
    sprite('jb045_01', 3)	# 2-4
    sprite('jb045_00', 3)	# 5-7

@State
def CmnActAirLockReject():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown1043()
    sprite('jb322_00', 3)	# 1-3
    sprite('jb322_01', 3)	# 4-6
    sprite('jb322_02', 6)	# 7-12
    sprite('jb322_03', 6)	# 13-18	 **attackbox here**
    sprite('jb322_04', 2)	# 19-20
    sprite('jb322_05', 3)	# 21-23
    sprite('jb322_06', 3)	# 24-26
    sprite('jb322_07', 3)	# 27-29

@State
def CmnActLandSpin():
    sprite('jb071_00', 4)	# 1-4
    sprite('jb071_01', 4)	# 5-8
    label(0)
    sprite('jb071_02', 2)	# 9-10
    sprite('jb071_03', 2)	# 11-12
    sprite('jb071_04', 2)	# 13-14
    sprite('jb071_05', 2)	# 15-16
    sprite('jb071_06', 2)	# 17-18
    sprite('jb071_07', 2)	# 19-20
    sprite('jb071_08', 2)	# 21-22
    sprite('jb071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('jb071_10', 6)	# 1-6
    sprite('jb071_11', 5)	# 7-11
    sprite('jb071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('jb071_02', 2)	# 1-2
    sprite('jb071_03', 2)	# 3-4
    sprite('jb071_04', 2)	# 5-6
    sprite('jb071_05', 2)	# 7-8
    sprite('jb071_06', 2)	# 9-10
    sprite('jb071_07', 2)	# 11-12
    sprite('jb071_08', 2)	# 13-14
    sprite('jb071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('jb077_00', 2)	# 1-2
    sprite('jb077_01', 2)	# 3-4
    sprite('jb077_00ex00', 2)	# 5-6
    sprite('jb077_01ex00', 2)	# 7-8
    sprite('jb077_00ex01', 2)	# 9-10
    sprite('jb077_01ex01', 2)	# 11-12
    sprite('jb077_00ex02', 2)	# 13-14
    sprite('jb077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('jb077_02', 4)	# 1-4
    label(0)
    sprite('jb077_03', 3)	# 5-7
    sprite('jb077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('jb077_05', 5)	# 1-5
    sprite('jb077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('jb060_07', 3)	# 1-3
    sprite('jb060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('jb060_13', 4)	# 1-4
    sprite('jb060_14', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('jb331_00', 3)	# 1-3

@State
def CmnActBurstLoop():
    sprite('jb331_01', 3)	# 1-3
    label(0)
    sprite('jb331_02', 3)	# 4-6
    sprite('jb331_03', 3)	# 7-9
    sprite('jb331_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('jb331_05', 3)	# 1-3
    sprite('jb331_06', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('jb331_07', 2)	# 1-2
    sprite('jb331_00ex00', 3)	# 3-5

@State
def CmnActAirBurstLoop():
    sprite('jb331_01ex00', 3)	# 1-3
    label(0)
    sprite('jb331_02ex00', 3)	# 4-6
    sprite('jb331_03ex00', 3)	# 7-9
    sprite('jb331_04ex00', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('jb331_08', 3)	# 1-3
    sprite('jb331_09', 3)	# 4-6
    sprite('jb020_05', 3)	# 7-9
    sprite('jb020_06', 3)	# 10-12
    label(0)
    sprite('jb020_07', 4)	# 13-16
    sprite('jb020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('jb333_00', 3)	# 1-3
    sprite('jb333_01', 3)	# 4-6
    sprite('jb333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('jb333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('jb333_04', 3)	# 1-3
    sprite('jb333_05', 3)	# 4-6
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    sprite('jb333_06', 3)	# 7-9
    sprite('jb333_07', 3)	# 10-12
    label(0)
    sprite('jb333_05', 3)	# 13-15
    sprite('jb333_06', 3)	# 16-18
    sprite('jb333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('jb333_08', 6)	# 1-6
    sprite('jb333_09', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('jb333_10', 3)	# 1-3
    sprite('jb333_11', 3)	# 4-6
    Unknown23119(16639, 20, 1)
    sprite('jb333_13', 3)	# 7-9
    sprite('jb333_14', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('jb333_15', 3)	# 1-3
    sprite('jb333_05ex00', 3)	# 4-6
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    sprite('jb333_06ex00', 3)	# 7-9
    sprite('jb333_07ex00', 3)	# 10-12
    label(0)
    sprite('jb333_05ex00', 3)	# 13-15
    sprite('jb333_06ex00', 3)	# 16-18
    sprite('jb333_07ex00', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('jb333_16', 6)	# 1-6
    sprite('jb333_17', 6)	# 7-12
    label(0)
    sprite('jb020_07', 4)	# 13-16
    sprite('jb020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('jb333_00', 3)	# 1-3
    sprite('jb333_01', 3)	# 4-6
    sprite('jb333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('jb333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('jb333_04', 3)	# 1-3
    sprite('jb333_05', 3)	# 4-6
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    sprite('jb333_06', 3)	# 7-9
    sprite('jb333_07', 3)	# 10-12
    label(0)
    sprite('jb333_05', 3)	# 13-15
    sprite('jb333_06', 3)	# 16-18
    sprite('jb333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('jb333_08', 6)	# 1-6
    sprite('jb333_09', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('jb333_10', 3)	# 1-3
    sprite('jb333_11', 3)	# 4-6
    Unknown23119(16639, 20, 1)
    sprite('jb333_13', 3)	# 7-9
    sprite('jb333_14', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('jb333_15', 3)	# 1-3
    sprite('jb333_05ex00', 3)	# 4-6
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    sprite('jb333_06ex00', 3)	# 7-9
    sprite('jb333_07ex00', 3)	# 10-12
    label(0)
    sprite('jb333_05ex00', 3)	# 13-15
    sprite('jb333_06ex00', 3)	# 16-18
    sprite('jb333_07ex00', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('jb333_16', 6)	# 1-6
    sprite('jb333_17', 6)	# 7-12
    label(0)
    sprite('jb020_07', 4)	# 13-16
    sprite('jb020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('jb333_00', 3)	# 1-3
    sprite('jb333_01', 3)	# 4-6
    sprite('jb333_02', 3)	# 7-9
    sprite('jb333_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('jb333_04', 3)	# 1-3
    sprite('jb333_05', 3)	# 4-6
    sprite('jb333_06', 3)	# 7-9
    sprite('jb333_07', 3)	# 10-12
    label(0)
    sprite('jb333_05', 3)	# 13-15
    sprite('jb333_06', 3)	# 16-18
    sprite('jb333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('jb333_08', 6)	# 1-6
    sprite('jb333_09', 6)	# 7-12

@State
def CmnActAirCrossChangeBegin():
    sprite('jb333_10', 3)	# 1-3
    sprite('jb333_11', 3)	# 4-6
    sprite('jb333_13', 3)	# 7-9
    sprite('jb333_14', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('jb333_15', 3)	# 1-3
    sprite('jb333_05ex00', 3)	# 4-6
    sprite('jb333_06ex00', 3)	# 7-9
    sprite('jb333_07ex00', 3)	# 10-12
    label(0)
    sprite('jb333_05ex00', 3)	# 13-15
    sprite('jb333_06ex00', 3)	# 16-18
    sprite('jb333_07ex00', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('jb333_16', 3)	# 1-3
    sprite('jb333_17', 3)	# 4-6
    sprite('jb020_05', 3)	# 7-9
    sprite('jb020_06', 3)	# 10-12
    label(0)
    sprite('jb020_07', 4)	# 13-16
    sprite('jb020_08', 4)	# 17-20
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
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('jb404_02', 3)	# 26-28
    Unknown1086(22)
    teleportRelativeX(-120000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('jb404_03', 3)	# 29-31
    sprite('jb404_04', 3)	# 32-34
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb404_05', 32767)	# 35-32801	 **attackbox here**
    GFX_0('jbef404_zanzou', 100)
    StartMultihit()
    label(9)
    sprite('keep', 3)	# 32802-32804
    RefreshMultihit()
    Unknown1084(1)
    sprite('jb024_00', 6)	# 32805-32810
    Unknown8000(100, 1, 1)
    sprite('jb024_01', 6)	# 32811-32816
    sprite('jb024_02', 4)	# 32817-32820
    sprite('jb024_03', 3)	# 32821-32823
    sprite('jb024_04', 3)	# 32824-32826

@State
def CmnActChangePartnerQuickIn():
    sprite('jb032_09', 5)	# 1-5
    sprite('jb032_10', 6)	# 6-11
    sprite('jb032_11', 6)	# 12-17
    sprite('jb032_12', 5)	# 18-22
    sprite('jb032_13', 4)	# 23-26
    sprite('jb032_14', 3)	# 27-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('jb033_01', 4)	# 1-4
    sprite('jb033_02', 4)	# 5-8
    sprite('jb033_03', 4)	# 9-12
    sprite('jb033_04', 4)	# 13-16
    sprite('jb033_05', 4)	# 17-20
    sprite('jb033_05', 40)	# 21-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('jb033_00', 1)	# 1-1
    sprite('jb033_01', 3)	# 2-4
    sprite('jb033_02', 3)	# 5-7
    sprite('jb033_03', 3)	# 8-10
    sprite('jb033_04', 3)	# 11-13
    sprite('jb033_05', 32767)	# 14-32780
    label(1)
    sprite('jb033_06', 1)	# 32781-32781
    sprite('jb033_07', 1)	# 32782-32782
    sprite('jb033_08', 2)	# 32783-32784
    sprite('jb033_09', 2)	# 32785-32786

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('jb000_00', 2)	# 1-2	 **attackbox here**
    sprite('jb001_00', 6)	# 3-8
    sprite('jb001_01', 6)	# 9-14
    sprite('jb001_02', 6)	# 15-20
    sprite('jb001_03', 6)	# 21-26
    sprite('jb001_04', 8)	# 27-34
    sprite('jb001_06', 8)	# 35-42
    sprite('jb001_04', 8)	# 43-50
    sprite('jb001_03', 6)	# 51-56
    sprite('jb001_02', 6)	# 57-62
    sprite('jb001_01', 6)	# 63-68
    sprite('jb001_00', 6)	# 69-74
    sprite('jb000_00', 22)	# 75-96	 **attackbox here**

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
    sprite('jb020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('jb020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('jb010_02', 2)	# 11-12	 **attackbox here**
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('jb407_00', 4)	# 1-4
    Unknown1084(1)
    sprite('jb407_01', 5)	# 5-9
    GFX_0('jbef407_NekodamaRady', -1)
    SFX_3('jbse_04')
    sprite('jb407_02', 5)	# 10-14
    sprite('jb407_03', 5)	# 15-19
    sprite('jb407_04', 5)	# 20-24
    sprite('jb407_05', 5)	# 25-29
    Unknown7007('626a623230385f30000000000000000064000000626a623230385f31000000000000000064000000626a623230385f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23090(8)
    sprite('jb407_06', 5)	# 30-34
    GFX_0('Shot_Eff', 0)
    Unknown38(8, 1)
    Unknown26('jbef407_NekodamaRady')
    SFX_0('016_explode_1')
    sprite('jb407_07', 4)	# 35-38
    Unknown1045(-20000)
    sprite('jb407_08', 4)	# 39-42
    sprite('jb407_07', 4)	# 43-46
    sprite('jb407_08', 4)	# 47-50
    Unknown1084(1)
    sprite('jb407_09', 3)	# 51-53

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP1(70)
        AttackP2(85)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(38000)
        YImpluseBeforeWallbounce(1800)
        AirUntechableTime(60)
        PushbackX(19800)
        Hitstop(20)
        Unknown9016(1)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(8000, 8000)
        Unknown11042(1)
        sendToLabelUpon(2, 10)
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('jb406_17', 2)	# 1-2
    physicsXImpulse(50000)
    sprite('jb406_18', 2)	# 3-4
    sprite('jb406_19', 2)	# 5-6
    Unknown1019(20)
    sprite('jb406_01', 2)	# 7-8
    SFX_0('024_getset_b')
    sprite('jb406_02', 2)	# 9-10
    sprite('jb406_03', 2)	# 11-12
    sprite('jb406_06', 2)	# 13-14
    clearUponHandler(3)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a623230375f30000000000000000064000000626a623230375f31000000000000000064000000626a623230375f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1084(1)
    sprite('jb406_07', 1)	# 15-15	 **attackbox here**
    GFX_0('jbef406_zanzou', 100)
    GFX_0('jbef406_zanzou2', 100)
    Unknown8000(100, 1, 0)
    sprite('jb406_07', 2)	# 16-17	 **attackbox here**
    teleportRelativeX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(16000)
    Unknown1043()
    sprite('jb406_08', 3)	# 18-20
    sprite('jb406_09', 3)	# 21-23
    sprite('jb406_10', 3)	# 24-26
    sprite('jb406_11', 3)	# 27-29
    sprite('jb406_12', 32767)	# 30-32796
    label(10)
    sprite('jb406_13', 7)	# 32797-32803
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('jb406_14', 7)	# 32804-32810
    sprite('jb406_15', 7)	# 32811-32817

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Rekkouzan_Atk')
        Damage(1000)
        AttackP1(70)
        Unknown11092(1)
        Unknown11042(1)
        AirPushbackY(10000)
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()

        def upon_78():
            Unknown2037(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('jb400_00', 4)	# 1-4
    Unknown1051(60)
    SFX_4('bjb200_0')
    sprite('jb400_01', 4)	# 5-8
    sprite('jb400_02', 4)	# 9-12
    physicsXImpulse(60000)
    Unknown8007(100, 1, 1)
    sprite('jb400_03', 2)	# 13-14	 **attackbox here**
    GFX_0('jbef400_slash', 100)
    Unknown1019(50)
    SFX_3('jbse_02')
    sprite('jb400_04', 1)	# 15-15
    sprite('jb400_05', 1)	# 16-16
    sprite('jb400_06', 1)	# 17-17
    physicsXImpulse(40000)
    sprite('jb400_07', 1)	# 18-18
    sprite('jb400_08', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    GFX_0('jbef400_slash2', 100)
    Unknown1019(20)
    SFX_3('jbse_02')
    sprite('jb400_09', 2)	# 21-22
    loopRest()
    if SLOT_2:
        sendToLabel(0)
    sprite('jb400_11', 4)	# 23-26
    physicsXImpulse(5000)
    Unknown8010(100, 1, 1)
    callSubroutine('HE_DeriveClear')
    sprite('jb400_12', 4)	# 27-30
    Unknown1019(50)
    sprite('jb400_13', 4)	# 31-34
    Unknown1019(0)
    sprite('jb400_14', 4)	# 35-38
    sprite('jb400_15', 4)	# 39-42
    ExitState()
    label(0)
    sprite('jb400_11', 1)	# 43-43
    Unknown8010(100, 1, 1)
    sprite('jb402_00', 2)	# 44-45
    physicsXImpulse(20000)
    sprite('jb402_01', 2)	# 46-47
    physicsYImpulse(16000)
    Unknown1043()
    sendToLabelUpon(2, 9)
    sprite('jb402_02', 2)	# 48-49
    sprite('jb402_03', 2)	# 50-51
    SFX_4('bjb201_0')
    sprite('jb402_04', 3)	# 52-54	 **attackbox here**
    RefreshMultihit()
    callSubroutine('Rekkouzan_Finish_Atk')
    Damage(1500)
    GFX_0('jbef402_slash', 100)
    SFX_3('jbse_02')
    sprite('jb402_05', 3)	# 55-57
    Recovery()
    Unknown1019(20)
    sprite('jb402_06', 2)	# 58-59
    sprite('jb402_07', 2)	# 60-61
    sprite('jb402_08', 2)	# 62-63
    sprite('jb402_09', 3)	# 64-66
    sprite('jb402_12', 3)	# 67-69
    Unknown2016(-1)
    Unknown23087(-1)
    Unknown1007(-80000)
    sprite('jb020_04', 3)	# 70-72
    sprite('jb020_05', 3)	# 73-75
    sprite('jb020_06', 3)	# 76-78
    label(1)
    sprite('jb020_07', 4)	# 79-82
    sprite('jb020_08', 4)	# 83-86
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('jb024_00', 1)	# 87-87
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('jb024_01', 1)	# 88-88
    sprite('jb024_02', 4)	# 89-92
    sprite('jb024_03', 1)	# 93-93
    sprite('jb024_04', 1)	# 94-94

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
    Unknown2036(77, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-290000)
    Unknown1019(4)
    label(0)
    sprite('jb020_07', 4)	# 3-6
    sprite('jb020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    Unknown1084(1)
    if SLOT_58:
        enterState('ChangePartnerDDOD_Exe')
    else:
        enterState('ChangePartnerDD_Exe')

@State
def ChangePartnerDD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23055('')
        AttackLevel_(5)
        Damage(500)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        PushbackX(0)
        Hitstop(2)
        Unknown11056(0)
        Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11064(1)
        Unknown13024(0)

        def upon_78():
            clearUponHandler(78)
            Unknown1086(22)
            teleportRelativeY(0)
            Unknown3001(0)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('jb431_00', 5)	# 1-5
    setInvincible(1)
    Unknown1084(1)
    sprite('jb431_01', 3)	# 6-8
    sprite('jb431_02', 3)	# 9-11
    sprite('jb431_03', 3)	# 12-14
    sprite('jb431_04', 3)	# 15-17
    sprite('jb431_05', 3)	# 18-20
    sprite('jb431_06', 3)	# 21-23
    sprite('jb431_04', 3)	# 24-26
    sprite('jb431_05', 3)	# 27-29
    sprite('jb431_06', 3)	# 30-32
    sprite('jb431_04', 3)	# 33-35
    sprite('jb431_05', 3)	# 36-38
    sprite('jb431_06', 3)	# 39-41
    sprite('jb431_04', 3)	# 42-44
    sprite('jb431_05', 3)	# 45-47
    loopRest()
    sprite('jb431_07', 3)	# 48-50
    physicsXImpulse(20000)
    tag_voice(1, 'bjb252_0', 'bjb252_1', '', '')
    sprite('jb431_08', 2)	# 51-52
    Unknown1019(200)
    Unknown3004(-20)
    sprite('jb431_09', 12)	# 53-64	 **attackbox here**
    GFX_0('jb431_SlashEff', -1)
    GFX_0('jb431_CircleShockEff', -1)
    Unknown1019(200)
    Unknown2017(0)
    Unknown2015(40)
    SFX_3('jbse_00')
    sprite('jb431_23', 3)	# 65-67
    clearUponHandler(12)
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    physicsXImpulse(20000)
    setInvincible(0)
    sprite('jb431_24', 3)	# 68-70
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_25', 3)	# 71-73
    sprite('jb431_26', 3)	# 74-76
    sprite('jb431_24', 3)	# 77-79
    sprite('jb431_25', 3)	# 80-82
    sprite('jb431_26', 3)	# 83-85
    sprite('jb431_27', 3)	# 86-88
    sprite('jb340_12ex00', 3)	# 89-91
    sprite('jb340_13ex00', 3)	# 92-94
    sprite('jb340_14ex00', 3)	# 95-97
    sprite('jb340_15ex00', 3)	# 98-100
    sprite('jb340_16ex00', 3)	# 101-103
    ExitState()
    label(1)
    sprite('jb431_09', 10)	# 104-113	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11023(1)
    Unknown11066(1)
    Unknown9154(60)
    Unknown11069('ChangePartnerDD_Exe')
    physicsXImpulse(50000)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('jb431_10', 5)	# 114-118
    GFX_0('jb431_SlashEndEff', -1)
    Unknown3004(20)
    Unknown3001(128)
    physicsXImpulse(20000)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('jb431_10', 15)	# 119-133
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_11', 3)	# 134-136
    sprite('jb431_12', 3)	# 137-139
    sprite('jb431_13', 3)	# 140-142
    sprite('jb431_14', 3)	# 143-145	 **attackbox here**
    RefreshMultihit()
    Damage(1000)
    Unknown9155()
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9130(30)
    Unknown9142(60)
    Unknown9132(30)
    Unknown9144(60)
    Unknown9016(1)
    Unknown11050('040000006a6265665f6472697665736c6173685f73756d69000000000000000000000000')
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)
    tag_voice(0, 'bjb253_0', 'bjb253_1', '', '')
    sprite('jb431_15', 3)	# 146-148	 **attackbox here**
    sprite('jb431_16', 3)	# 149-151	 **attackbox here**
    sprite('jb431_17', 3)	# 152-154	 **attackbox here**
    sprite('jb431_15', 3)	# 155-157	 **attackbox here**
    sprite('jb431_16', 3)	# 158-160	 **attackbox here**
    sprite('jb431_17', 3)	# 161-163	 **attackbox here**
    sprite('jb431_15', 3)	# 164-166	 **attackbox here**
    sprite('jb431_16', 3)	# 167-169	 **attackbox here**
    sprite('jb431_17', 3)	# 170-172	 **attackbox here**
    sprite('jb431_15', 3)	# 173-175	 **attackbox here**
    sprite('jb431_16', 3)	# 176-178	 **attackbox here**
    sprite('jb431_17', 3)	# 179-181	 **attackbox here**
    sprite('jb431_18', 5)	# 182-186
    sprite('jb431_19', 5)	# 187-191
    sprite('jb431_20', 5)	# 192-196
    sprite('jb431_21', 5)	# 197-201
    sprite('jb431_22', 4)	# 202-205

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        AttackLevel_(5)
        Damage(800)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        PushbackX(0)
        Hitstop(2)
        Unknown11056(0)
        Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11064(1)
        Unknown13024(0)

        def upon_78():
            clearUponHandler(78)
            Unknown1086(22)
            teleportRelativeY(0)
            Unknown3001(0)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('jb431_00', 5)	# 1-5
    setInvincible(1)
    Unknown1084(1)
    sprite('jb431_01', 3)	# 6-8
    sprite('jb431_02', 3)	# 9-11
    sprite('jb431_03', 3)	# 12-14
    sprite('jb431_04', 3)	# 15-17
    sprite('jb431_05', 3)	# 18-20
    sprite('jb431_06', 3)	# 21-23
    sprite('jb431_04', 3)	# 24-26
    sprite('jb431_05', 3)	# 27-29
    sprite('jb431_06', 3)	# 30-32
    sprite('jb431_04', 3)	# 33-35
    sprite('jb431_05', 3)	# 36-38
    sprite('jb431_06', 3)	# 39-41
    sprite('jb431_04', 3)	# 42-44
    sprite('jb431_05', 3)	# 45-47
    sprite('jb431_07', 3)	# 48-50
    tag_voice(1, 'bjb252_0', 'bjb252_1', '', '')
    physicsXImpulse(20000)
    sprite('jb431_08', 2)	# 51-52
    Unknown1019(200)
    Unknown3004(-20)
    sprite('jb431_09', 12)	# 53-64	 **attackbox here**
    GFX_0('jb431_SlashEff', -1)
    GFX_0('jb431_CircleShockEff', -1)
    Unknown1019(200)
    Unknown2017(0)
    Unknown2015(40)
    SFX_3('jbse_00')
    sprite('jb431_23', 3)	# 65-67
    clearUponHandler(78)
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    physicsXImpulse(20000)
    setInvincible(0)
    sprite('jb431_24', 3)	# 68-70
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_25', 3)	# 71-73
    sprite('jb431_26', 3)	# 74-76
    sprite('jb431_24', 3)	# 77-79
    sprite('jb431_25', 3)	# 80-82
    sprite('jb431_26', 3)	# 83-85
    sprite('jb431_27', 3)	# 86-88
    sprite('jb340_12ex00', 3)	# 89-91
    sprite('jb340_13ex00', 3)	# 92-94
    sprite('jb340_14ex00', 3)	# 95-97
    sprite('jb340_15ex00', 3)	# 98-100
    sprite('jb340_16ex00', 3)	# 101-103
    ExitState()
    label(1)
    sprite('jb431_09', 10)	# 104-113	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11023(1)
    Unknown11066(1)
    Unknown9154(60)
    Unknown11069('ChangePartnerDDOD_Exe')
    physicsXImpulse(50000)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('jb431_10', 5)	# 114-118
    GFX_0('jb431OD_SlashEffMatome', 100)
    Unknown3004(20)
    Unknown3001(128)
    physicsXImpulse(20000)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('jb431_10', 15)	# 119-133
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_11', 3)	# 134-136
    sprite('jb431_12', 3)	# 137-139
    sprite('jb431_13', 3)	# 140-142
    sprite('jb431_14', 3)	# 143-145	 **attackbox here**
    RefreshMultihit()
    Damage(100)
    Unknown9155()
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9130(30)
    Unknown9142(60)
    Unknown9132(30)
    Unknown9144(60)
    Unknown11057(600)
    Unknown9016(1)
    Unknown11050('040000006a6265665f6472697665736c6173685f73756d69000000000000000000000000')
    Unknown21015('6a623433314f445f536c6173684566664d61746f6d6500000000000000000000d610000000000000')
    sprite('jb431_15', 3)	# 146-148	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_16', 3)	# 149-151	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_17', 3)	# 152-154	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_15', 3)	# 155-157	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_16', 3)	# 158-160	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_17', 3)	# 161-163	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_15', 3)	# 164-166	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_16', 3)	# 167-169	 **attackbox here**
    RefreshMultihit()
    Unknown11057(1000)
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)
    tag_voice(0, 'bjb253_0', 'bjb253_1', '', '')
    sprite('jb431_17', 3)	# 170-172	 **attackbox here**
    sprite('jb431_15', 3)	# 173-175	 **attackbox here**
    sprite('jb431_16', 3)	# 176-178	 **attackbox here**
    sprite('jb431_17', 3)	# 179-181	 **attackbox here**
    sprite('jb431_15', 3)	# 182-184	 **attackbox here**
    sprite('jb431_16', 3)	# 185-187	 **attackbox here**
    sprite('jb431_17', 3)	# 188-190	 **attackbox here**
    sprite('jb431_15', 3)	# 191-193	 **attackbox here**
    sprite('jb431_16', 3)	# 194-196	 **attackbox here**
    sprite('jb431_17', 3)	# 197-199	 **attackbox here**
    sprite('jb431_15', 3)	# 200-202	 **attackbox here**
    sprite('jb431_16', 3)	# 203-205	 **attackbox here**
    sprite('jb431_18', 5)	# 206-210
    sprite('jb431_19', 5)	# 211-215
    sprite('jb431_20', 5)	# 216-220
    sprite('jb431_21', 5)	# 221-225
    sprite('jb431_22', 4)	# 226-229

@State
def CmnActChangeRequest():
    pass

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
    sprite('jb404_02', 4)	# 121-124
    Unknown1086(22)
    teleportRelativeX(-120000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    sprite('jb404_03', 4)	# 125-128
    sprite('jb404_04', 3)	# 129-131
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb404_05', 15)	# 132-146	 **attackbox here**
    StartMultihit()
    sprite('jb404_05', 1)	# 147-147	 **attackbox here**
    StartMultihit()
    GFX_0('jbef404_zanzou', 100)
    sprite('jb404_05', 32767)	# 148-32914	 **attackbox here**
    label(9)
    sprite('jb024_00', 7)	# 32915-32921
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('jb024_01', 7)	# 32922-32928
    sprite('jb024_02', 11)	# 32929-32939
    sprite('jb024_03', 3)	# 32940-32942
    sprite('jb024_04', 3)	# 32943-32945

@State
def CmnActChangeReturnAppealBurst():
    sprite('jb620_03', 5)	# 1-5
    sprite('jb620_04', 5)	# 6-10
    sprite('jb620_05', 5)	# 11-15
    sprite('jb620_06', 5)	# 16-20
    sprite('jb620_07', 35)	# 21-55
    sprite('jb010_07', 25)	# 56-80	 **attackbox here**
    teleportRelativeX(-50000)

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        callSubroutine('4A_AtkData')
        WhiffCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtk4A2nd')
    sprite('jb200_00', 2)	# 1-2
    Unknown1051(60)
    sprite('jb200_01', 3)	# 3-5
    sprite('jb200_02', 2)	# 6-7	 **attackbox here**
    Unknown7009(0)
    SFX_0('003_swing_grap_0_0')
    sprite('jb200_02', 2)	# 8-9	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('jb200_03', 3)	# 10-12
    WhiffCancelEnable(1)
    sprite('jb200_04', 3)	# 13-15
    sprite('jb200_01', 3)	# 16-18
    sprite('jb200_00', 2)	# 19-20

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        callSubroutine('4A_AtkData')
        WhiffCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk4A3rd')
    sprite('jb200_04', 2)	# 1-2
    Unknown1051(60)
    sprite('jb200_01', 3)	# 3-5
    sprite('jb200_02ex', 2)	# 6-7	 **attackbox here**
    Unknown7009(0)
    SFX_0('003_swing_grap_0_0')
    sprite('jb200_02ex', 2)	# 8-9	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('jb200_03', 3)	# 10-12
    WhiffCancelEnable(1)
    sprite('jb200_04', 3)	# 13-15
    sprite('jb200_01', 3)	# 16-18
    sprite('jb200_00', 2)	# 19-20

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        callSubroutine('4A_AtkData')
    sprite('jb200_04', 2)	# 1-2
    Unknown1051(60)
    sprite('jb200_01', 3)	# 3-5
    sprite('jb200_02', 2)	# 6-7	 **attackbox here**
    Unknown7009(0)
    SFX_0('003_swing_grap_0_0')
    sprite('jb200_02', 2)	# 8-9	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('jb200_03', 3)	# 10-12
    WhiffCancelEnable(1)
    sprite('jb200_04', 3)	# 13-15
    sprite('jb200_01', 3)	# 16-18
    sprite('jb200_00', 2)	# 19-20

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1200)
        AirPushbackY(20000)
        Unknown1112('')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('jb201_00', 2)	# 1-2
    physicsXImpulse(15000)
    sprite('jb201_00', 2)	# 3-4
    Unknown1019(250)
    sprite('jb201_01', 3)	# 5-7
    Unknown7009(1)
    Unknown1019(10)
    SFX_0('003_swing_grap_0_1')
    sprite('jb201_02', 3)	# 8-10	 **attackbox here**
    sprite('jb201_03', 4)	# 11-14
    Recovery()
    Unknown2063()
    Unknown1084(1)
    sprite('jb201_04', 4)	# 15-18
    sprite('jb201_05', 4)	# 19-22
    sprite('jb201_06', 4)	# 23-26

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(900)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(15000)
        AirPushbackY(10000)
        Unknown9016(1)
        Unknown2004(1, 0)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('jb202_00', 2)	# 1-2
    sprite('jb202_01', 2)	# 3-4
    physicsXImpulse(4000)
    Unknown8006(100, 1, 0)
    sprite('jb202_02', 3)	# 5-7
    Unknown7009(2)
    Unknown1019(500)
    Unknown8006(100, 1, 0)
    SFX_0('010_swing_sword_1')
    sprite('jb202_03', 3)	# 8-10
    Unknown1019(50)
    Unknown8006(100, 1, 0)
    sprite('jb202_04', 1)	# 11-11	 **attackbox here**
    Unknown1019(10)
    StartMultihit()
    GFX_0('jbef202_zanzou', 100)
    sprite('jb202_04', 3)	# 12-14	 **attackbox here**
    sprite('jb202_05', 4)	# 15-18
    sprite('jb202_06', 2)	# 19-20
    Unknown1019(1000)
    Unknown8006(100, 1, 0)
    sprite('jb202_06', 2)	# 21-22
    Unknown1019(200)
    Unknown8006(100, 1, 0)
    SFX_0('010_swing_sword_1')
    sprite('jb202_07', 3)	# 23-25	 **attackbox here**
    Unknown1084(1)
    Unknown8006(100, 1, 0)
    RefreshMultihit()
    AirUntechableTime(23)
    Unknown9071()
    AirPushbackY(30000)
    PushbackX(19800)
    GFX_0('jbef202_zanzou_2nd', 100)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        HitOrBlockCancel('NmlAtk5A3rd')
    sprite('jb202_08', 4)	# 26-29
    Recovery()
    Unknown2063()
    sprite('jb202_09', 3)	# 30-32
    sprite('jb202_10', 3)	# 33-35
    sprite('jb202_11', 3)	# 36-38
    sprite('jb202_12', 3)	# 39-41
    sprite('jb202_13', 3)	# 42-44

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(900)
        AirUntechableTime(26)
        Unknown11092(1)
        Unknown9016(1)
        AirHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        HitJumpCancel(1)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('jb235_00', 3)	# 1-3
    sprite('jb235_01', 3)	# 4-6
    sprite('jb235_02', 3)	# 7-9
    Unknown7009(2)
    SFX_0('010_swing_sword_1')
    sprite('jb235_03', 3)	# 10-12
    sprite('jb235_04', 3)	# 13-15	 **attackbox here**
    GFX_0('jbef235_zanzou', 100)
    sprite('jb235_05', 3)	# 16-18
    sprite('jb235_06', 3)	# 19-21
    sprite('jb235_07', 3)	# 22-24
    Unknown2015(200)
    SFX_0('010_swing_sword_1')
    sprite('jb235_08', 2)	# 25-26
    sprite('jb235_09', 3)	# 27-29	 **attackbox here**
    RefreshMultihit()
    AttackP1(90)
    AirPushbackX(10000)
    AirPushbackY(12000)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    HitLow(2)
    Unknown11058('0000000000000000010000000000000000000000')
    GFX_0('jbef235_zanzou_2nd', 100)
    Unknown2015(250)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        HitOrBlockCancel('NmlAtk5A4th')
    sprite('jb235_10', 3)	# 30-32
    Recovery()
    Unknown2063()
    sprite('jb235_11', 3)	# 33-35
    sprite('jb235_12', 3)	# 36-38
    Unknown2015(-1)
    sprite('jb235_13', 3)	# 39-41
    sprite('jb235_14', 3)	# 42-44
    sprite('jb235_15', 3)	# 45-47
    sprite('jb235_16', 3)	# 48-50

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('DriveInit')
    sprite('jb203_00', 2)	# 1-2
    sprite('jb203_01', 2)	# 3-4
    Unknown1084(1)
    Unknown20(2, 2, 58)
    Unknown4048(0)
    Unknown4045('6a6265665f4472697665596f74796f750000000000000000000000000000000067000000')
    sprite('jb203_02', 2)	# 5-6
    Unknown20(2, 2, 58)
    sprite('jb203_03', 2)	# 7-8
    Unknown20(2, 2, 58)
    Unknown7007('626a623130365f31000000000000000064000000626a623130365f32000000000000000064000000626a623130375f31000000000000000064000000626a623230315f30000000000000000064000000')
    sprite('jb203_05', 2)	# 9-10
    Unknown20(2, 2, 58)
    sprite('jb203_06', 2)	# 11-12	 **attackbox here**
    StartMultihit()
    physicsXImpulse(80000)
    Unknown3004(-30)
    GFX_0('5DStartEff', 0)
    sprite('jb203_06', 10)	# 13-22	 **attackbox here**
    Unknown2017(0)
    Unknown2015(40)
    SFX_3('jbse_08')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('jb203_06', 3)	# 23-25	 **attackbox here**
    StartMultihit()
    physicsXImpulse(110000)
    Unknown21015('3544537461727445666600000000000000000000000000000000000000000000ee07000000000000')
    sprite('jb203_06', 4)	# 26-29	 **attackbox here**
    physicsXImpulse(40000)
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('jb203_07', 4)	# 30-33
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb203_08', 4)	# 34-37
    sprite('jb203_09', 8)	# 38-45
    sprite('jb203_10', 4)	# 46-49
    GFX_1('jbef_noutou', 0)
    SFX_3('jbse_07')
    sprite('jb203_11', 10)	# 50-59
    sprite('jb203_11', 10)	# 60-69
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('jb203_06', 3)	# 70-72	 **attackbox here**
    clearUponHandler(12)
    clearUponHandler(61)
    StartMultihit()
    physicsXImpulse(20000)
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    Unknown21015('3544537461727445666600000000000000000000000000000000000000000000ee07000000000000')
    sprite('jb203_07', 3)	# 73-75
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb203_08', 3)	# 76-78
    sprite('jb203_09', 6)	# 79-84
    sprite('jb203_10', 3)	# 85-87
    GFX_1('jbef_noutou', 0)
    SFX_3('jbse_07')
    sprite('jb203_11', 6)	# 88-93
    loopRest()
    Unknown48('190000000200000002000000160000000200000016000000')
    if SLOT_38:
        (SLOT_22 <= SLOT_2)
        if SLOT_0:
            _gotolabel(9)
    else:
        (SLOT_22 >= SLOT_2)
        if SLOT_0:
            _gotolabel(9)
    sprite('jb203_14', 3)	# 94-96
    sprite('jb203_15', 3)	# 97-99
    ExitState()
    label(9)
    sprite('jb203_12', 3)	# 100-102
    Unknown28(8, 'CmnActStandTurn')
    sprite('jb203_13', 3)	# 103-105

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('Rekkouzan_Atk')
        SLOT_64 = 0
        Unknown1112('')
    sprite('jb400_00', 3)	# 1-3
    Unknown1051(60)
    sprite('jb400_00', 1)	# 4-4
    Unknown8007(100, 1, 1)
    sprite('jb400_01', 4)	# 5-8
    tag_voice(1, 'bjb200_0', 'bjb200_1', '', '')
    sprite('jb400_02', 4)	# 9-12
    physicsXImpulse(40000)
    sprite('jb400_03', 3)	# 13-15	 **attackbox here**
    GFX_0('jbef400_slash', 100)
    Unknown1019(50)
    YAccel(50)
    callSubroutine('Rekkouzan_DeriveInputBegin')
    Unknown14070('NmlAtk5B2nd')
    SFX_3('jbse_02')
    sprite('jb400_04', 3)	# 16-18
    Unknown1019(50)
    YAccel(50)
    Recovery()
    clearUponHandler(3)
    callSubroutine('Rekkouzan_DeriveTimingBegin')
    enterState('NmlAtk5B2nd')
    sprite('jb400_11', 3)	# 19-21
    physicsXImpulse(5000)
    Unknown8010(100, 1, 1)
    callSubroutine('Rekkouzan_DeriveClear')
    sprite('jb400_12', 3)	# 22-24
    Unknown1019(50)
    sprite('jb400_13', 3)	# 25-27
    Unknown1019(0)
    sprite('jb400_14', 3)	# 28-30
    sprite('jb400_15', 2)	# 31-32

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('Rekkouzan_Atk')
        Unknown30068(1)
    sprite('jb400_04', 1)	# 1-1
    Unknown1051(60)
    Unknown8007(100, 1, 1)
    loopRest()
    sprite('jb400_05', 2)	# 2-3
    sprite('jb400_06', 2)	# 4-5
    physicsXImpulse(40000)
    sprite('jb400_07', 2)	# 6-7
    sprite('jb400_08', 3)	# 8-10	 **attackbox here**
    GFX_0('jbef400_slash2', 100)
    Unknown1019(20)
    callSubroutine('Rekkouzan_DeriveInputBegin')
    SFX_3('jbse_02')
    sprite('jb400_09', 3)	# 11-13
    Recovery()
    clearUponHandler(3)
    callSubroutine('Rekkouzan_DeriveTimingBegin')
    sprite('jb400_11', 3)	# 14-16
    physicsXImpulse(5000)
    Unknown8010(100, 1, 1)
    callSubroutine('Rekkouzan_DeriveClear')
    sprite('jb400_12', 3)	# 17-19
    Unknown1019(50)
    sprite('jb400_13', 3)	# 20-22
    Unknown1019(0)
    sprite('jb400_14', 2)	# 23-24
    sprite('jb400_15', 2)	# 25-26

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('Rekkouzan_Atk')
        Unknown30068(1)
        SLOT_64 = 1
    sprite('jb400_09', 1)	# 1-1
    Unknown1051(60)
    Unknown8007(100, 1, 1)
    sprite('jb400_16', 2)	# 2-3
    sprite('jb400_01', 2)	# 4-5
    physicsXImpulse(40000)
    sprite('jb400_02', 2)	# 6-7
    sprite('jb400_03', 3)	# 8-10	 **attackbox here**
    GFX_0('jbef400_slash', 100)
    Unknown1019(50)
    callSubroutine('Rekkouzan_DeriveInputBegin')
    Unknown14070('NmlAtk5B4th')
    SFX_3('jbse_02')
    sprite('jb400_04', 3)	# 11-13
    Recovery()
    clearUponHandler(3)
    callSubroutine('Rekkouzan_DeriveTimingBegin')
    enterState('NmlAtk5B4th')
    sprite('jb400_11', 3)	# 14-16
    physicsXImpulse(5000)
    Unknown8010(100, 1, 1)
    callSubroutine('Rekkouzan_DeriveClear')
    sprite('jb400_12', 4)	# 17-20
    Unknown1019(50)
    sprite('jb400_13', 4)	# 21-24
    Unknown1019(0)
    sprite('jb400_14', 3)	# 25-27
    sprite('jb400_15', 3)	# 28-30

@State
def NmlAtk5B4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('Rekkouzan_Atk')
        Unknown30068(1)
    sprite('jb400_04', 1)	# 1-1
    Unknown1051(60)
    Unknown8007(100, 1, 1)
    sprite('jb400_05', 2)	# 2-3
    sprite('jb400_06', 2)	# 4-5
    physicsXImpulse(40000)
    sprite('jb400_07', 2)	# 6-7
    sprite('jb400_08', 3)	# 8-10	 **attackbox here**
    GFX_0('jbef400_slash2', 100)
    Unknown1019(20)
    callSubroutine('Rekkouzan_DeriveInputBegin')
    SFX_3('jbse_02')
    sprite('jb400_09', 3)	# 11-13
    Recovery()
    clearUponHandler(3)
    callSubroutine('Rekkouzan_DeriveTimingBegin')
    sprite('jb400_11', 3)	# 14-16
    physicsXImpulse(5000)
    Unknown8010(100, 1, 1)
    callSubroutine('Rekkouzan_DeriveClear')
    sprite('jb400_12', 4)	# 17-20
    Unknown1019(50)
    sprite('jb400_13', 4)	# 21-24
    Unknown1019(0)
    sprite('jb400_14', 3)	# 25-27
    sprite('jb400_15', 3)	# 28-30

@State
def NmlAtk5B5th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(25000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown30068(1)
        JumpCancel_(0)

        def upon_STATE_END():
            SLOT_62 = 0
        Unknown28(2, 'CmnActJumpLanding')
        Unknown22004(10, 1)
    sprite('jb402_00', 2)	# 1-2
    Unknown1084(1)
    physicsXImpulse(20000)
    Unknown26('jbef400_slash2')
    Unknown8001(3, 100)
    sprite('jb402_01', 2)	# 3-4
    physicsYImpulse(25000)
    Unknown1043()
    sprite('jb402_02', 2)	# 5-6
    sprite('jb402_03', 2)	# 7-8
    tag_voice(0, 'bjb201_0', 'bjb201_1', '', '')
    sprite('jb402_04', 3)	# 9-11	 **attackbox here**
    GFX_0('jbef402_slash', 100)
    SFX_3('jbse_02')
    sprite('jb402_05', 3)	# 12-14
    Recovery()
    Unknown1019(20)
    sprite('jb402_06', 3)	# 15-17
    sprite('jb402_07', 3)	# 18-20
    sprite('jb402_08', 3)	# 21-23
    sprite('jb402_09', 3)	# 24-26
    sprite('jb402_12', 3)	# 27-29
    sprite('jb020_04', 3)	# 30-32
    sprite('jb020_05', 3)	# 33-35
    sprite('jb020_06', 3)	# 36-38
    label(0)
    sprite('jb020_07', 4)	# 39-42
    sprite('jb020_08', 4)	# 43-46
    loopRest()
    gotoLabel(0)

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(90)
        AirPushbackY(20000)
        HitLow(2)
        Unknown11028(14)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('jb231_00', 3)	# 1-3
    sprite('jb231_01', 2)	# 4-5
    Unknown7009(4)
    SFX_0('003_swing_grap_0_1')
    sprite('jb231_02', 2)	# 6-7
    sprite('jb231_03', 1)	# 8-8	 **attackbox here**
    StartMultihit()
    sprite('jb231_03', 3)	# 9-11	 **attackbox here**
    sprite('jb231_03', 2)	# 12-13	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('jb231_04', 2)	# 14-15
    sprite('jb231_05', 2)	# 16-17
    sprite('jb231_06', 3)	# 18-20
    sprite('jb231_07', 3)	# 21-23
    sprite('jb231_08', 3)	# 24-26

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(90)
        AttackP2(75)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(30000)
        AirUntechableTime(28)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        sendToLabelUpon(2, 9)
    sprite('jb232_00', 3)	# 1-3
    sprite('jb232_01', 3)	# 4-6
    sprite('jb232_02', 3)	# 7-9
    Unknown7009(2)
    SFX_0('010_swing_sword_1')
    sprite('jb232_03', 2)	# 10-11	 **attackbox here**
    StartMultihit()
    GFX_0('jbef232_zanzou', 100)
    teleportRelativeX(4000)
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    Unknown1043()
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('jb232_03', 4)	# 12-15	 **attackbox here**
    physicsYImpulse(20000)
    sprite('jb232_04', 2)	# 16-17	 **attackbox here**
    setInvincible(0)
    sprite('jb232_04', 2)	# 18-19	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('jb232_05', 3)	# 20-22
    sprite('jb232_06', 3)	# 23-25
    sprite('jb232_07', 3)	# 26-28
    sprite('jb232_08', 32767)	# 29-32795
    label(9)
    sprite('jb232_09', 4)	# 32796-32799
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('jb232_10', 4)	# 32800-32803
    sprite('jb232_11', 4)	# 32804-32807
    sprite('jb232_12', 4)	# 32808-32811

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1700)
        AttackP1(90)
        AttackP2(85)
        GroundedHitstunAnimation(0)
        AirHitstunAnimation(11)
        AirPushbackX(15000)
        AirPushbackY(-60000)
        Unknown9310(1)
        AirUntechableTime(25)
        PushbackX(12000)
        Unknown11058('0000000000000000010000000000000000000000')
        HitLow(2)
        Unknown2004(1, 0)
    sprite('jb211_03', 8)	# 1-8
    Unknown2018(1, 60)
    sprite('jb211_04', 5)	# 9-13
    physicsXImpulse(35000)
    Unknown1045(25000)
    SFX_0('003_swing_grap_0_1')
    Unknown7007('626a623130375f30000000000000000064000000626a623130375f31000000000000000064000000626a623130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb211_05', 4)	# 14-17
    Unknown1019(50)
    sprite('jb211_06', 3)	# 18-20	 **attackbox here**
    Unknown1019(10)
    sprite('jb211_07', 1)	# 21-21
    Unknown1019(0)
    sprite('jb211_08', 1)	# 22-22
    sprite('jb211_09', 1)	# 23-23
    SFX_0('003_swing_grap_0_2')
    sprite('jb211_10', 1)	# 24-24
    sprite('jb211_11', 1)	# 25-25	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(8000)
    AirPushbackY(25000)
    Unknown9310(-1)
    Unknown11058('0000000001000000000000000000000000000000')
    HitLow(0)

    def upon_11():
        ScreenShake(5000, 5000)

    def upon_ON_HIT_OR_BLOCK():
        HitJumpCancel(1)
    sprite('jb211_11', 2)	# 26-27	 **attackbox here**
    sprite('jb211_12', 5)	# 28-32
    Recovery()
    Unknown2063()
    Unknown1051(0)
    sprite('jb211_13', 5)	# 33-37
    sprite('jb211_14', 5)	# 38-42
    sprite('jb211_15', 5)	# 43-47
    sprite('jb211_16', 5)	# 48-52

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1200)
        AirUntechableTime(21)
        AirPushbackY(20000)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('jb252_00', 3)	# 1-3
    sprite('jb252_01', 1)	# 4-4
    sprite('jb252_01', 1)	# 5-5
    Unknown7009(5)
    sprite('jb252_02', 3)	# 6-8
    SFX_0('010_swing_sword_1')
    sprite('jb252_03', 3)	# 9-11
    sprite('jb252_04', 2)	# 12-13	 **attackbox here**
    GFX_0('jbef252_zanzou', 100)
    sprite('jb252_05', 3)	# 14-16
    sprite('jb252_06', 3)	# 17-19
    sprite('jb252_07', 3)	# 20-22
    SFX_0('010_swing_sword_1')
    sprite('jb252_08', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    GFX_0('jbef252_zanzou_2nd', 100)
    sprite('jb252_09', 4)	# 25-28
    Recovery()
    Unknown2063()
    Unknown14077(1)
    sprite('jb252_10', 4)	# 29-32
    sprite('jb252_11', 3)	# 33-35
    sprite('jb252_12', 3)	# 36-38

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('Rekkouzan_Atk')
        HitOverhead(0)
        SLOT_64 = 0
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
    sprite('jb400_16', 2)	# 1-2
    Unknown1022()
    Unknown1084(1)
    Unknown2016(100)
    Unknown23087(80000)
    Unknown1007(80000)

    def upon_LANDING():
        Unknown2016(-1)
        Unknown23087(-1)
        Unknown11058('0000000001000000000000000000000000000000')
    sprite('jb400_01', 1)	# 3-3
    sprite('jb400_01', 3)	# 4-6
    Unknown8009(1)
    SFX_4('bjb200_0')
    sprite('jb400_02', 4)	# 7-10
    physicsXImpulse(40000)
    sprite('jb400_03', 3)	# 11-13	 **attackbox here**
    GFX_0('jbef400_slash', 100)
    Unknown1019(50)
    YAccel(50)
    callSubroutine('Rekkouzan_DeriveInputBegin')
    Unknown14070('NmlAtkAIR5B2nd')
    SFX_3('jbse_02')
    sprite('jb400_04', 3)	# 14-16
    Unknown1019(50)
    YAccel(50)
    Recovery()
    clearUponHandler(3)
    callSubroutine('Rekkouzan_DeriveTimingBegin')
    enterState('NmlAtkAIR5B2nd')
    sprite('jb400_11', 3)	# 17-19
    physicsXImpulse(5000)
    YAccel(50)
    callSubroutine('Rekkouzan_DeriveClear')
    sprite('jb400_12', 3)	# 20-22
    Unknown1019(50)
    YAccel(50)
    sprite('jb400_13', 3)	# 23-25
    Unknown1043()
    sprite('jb400_17', 3)	# 26-28
    Unknown2016(-1)
    Unknown23087(-1)
    Unknown1007(-80000)
    sprite('jb400_18', 2)	# 29-30
    sprite('jb020_05', 3)	# 31-33
    sprite('jb020_06', 3)	# 34-36

@State
def NmlAtkAIR5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('Rekkouzan_Atk')
        Unknown30068(1)
        HitOverhead(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
    sprite('jb400_04', 1)	# 1-1
    Unknown1084(1)
    Unknown8009(1)
    Unknown2016(100)
    Unknown23087(80000)

    def upon_LANDING():
        Unknown2016(-1)
        Unknown23087(-1)
        Unknown11058('0000000001000000000000000000000000000000')
    sprite('jb400_05', 2)	# 2-3
    sprite('jb400_06', 2)	# 4-5
    physicsXImpulse(40000)
    sprite('jb400_07', 2)	# 6-7
    sprite('jb400_08', 3)	# 8-10	 **attackbox here**
    GFX_0('jbef400_slash2', 100)
    Unknown1019(20)
    callSubroutine('Rekkouzan_DeriveInputBegin')
    SFX_3('jbse_02')
    sprite('jb400_09', 3)	# 11-13
    Recovery()
    clearUponHandler(3)
    callSubroutine('Rekkouzan_DeriveTimingBegin')
    sprite('jb400_11', 3)	# 14-16
    Unknown1023()
    physicsXImpulse(5000)
    YAccel(35)
    Unknown1043()
    callSubroutine('Rekkouzan_DeriveClear')
    sprite('jb400_12', 3)	# 17-19
    Unknown1019(50)
    YAccel(50)
    sprite('jb400_13', 3)	# 20-22
    sprite('jb400_17', 3)	# 23-25
    Unknown2016(-1)
    Unknown23087(-1)
    Unknown1007(-80000)
    sprite('jb400_18', 2)	# 26-27
    sprite('jb020_05', 3)	# 28-30
    sprite('jb020_06', 3)	# 31-33

@State
def NmlAtkAIR5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirUntechableTime(60)
        HitOverhead(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(6000)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown30068(1)
        JumpCancel_(0)
        if SLOT_36:
            if (not SLOT_62):
                Unknown2016(100)
                Unknown23087(80000)

        def upon_STATE_END():
            SLOT_62 = 0
        Unknown28(2, 'CmnActJumpLanding')
        Unknown22004(10, 1)
    sprite('jb402_00', 2)	# 1-2
    Unknown1084(1)
    physicsXImpulse(20000)
    Unknown26('jbef400_slash2')
    Unknown8001(3, 100)
    sprite('jb402_01', 2)	# 3-4
    if SLOT_36:
        Unknown2016(-1)
        Unknown23087(-1)
        Unknown1007(-80000)
    physicsYImpulse(25000)
    Unknown1043()
    sprite('jb402_02', 2)	# 5-6
    sprite('jb402_03', 2)	# 7-8
    sprite('jb402_04', 3)	# 9-11	 **attackbox here**
    GFX_0('jbef402_slash', 100)
    SFX_3('jbse_02')
    SFX_4('bjb201_0')
    sprite('jb402_05', 3)	# 12-14
    Recovery()
    Unknown1019(20)
    sprite('jb402_06', 3)	# 15-17
    sprite('jb402_07', 3)	# 18-20
    sprite('jb402_08', 3)	# 21-23
    sprite('jb402_09', 3)	# 24-26
    sprite('jb402_12', 3)	# 27-29
    sprite('jb020_04', 3)	# 30-32
    sprite('jb020_05', 3)	# 33-35
    sprite('jb020_06', 3)	# 36-38
    label(0)
    sprite('jb020_07', 4)	# 39-42
    sprite('jb020_08', 4)	# 43-46
    loopRest()
    gotoLabel(0)

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('DriveInit')
        clearUponHandler(2)
    sprite('jb253_00', 3)	# 1-3
    sprite('jb253_01', 3)	# 4-6
    Unknown1084(1)
    Unknown4048(60000)
    Unknown4045('6a6265665f4472697665596f74796f750000000000000000000000000000000067000000')
    Unknown20(2, 2, 58)
    sprite('jb203_02ex00', 3)	# 7-9
    Unknown20(2, 2, 58)
    sprite('jb203_03ex00', 3)	# 10-12
    Unknown20(2, 2, 58)
    sprite('jb203_04ex00', 3)	# 13-15
    Unknown20(2, 2, 58)
    Unknown7007('626a623130365f31000000000000000064000000626a623130365f32000000000000000064000000626a623130375f31000000000000000064000000626a623230315f30000000000000000064000000')
    sprite('jb253_02', 32767)	# 16-32782	 **attackbox here**
    GFX_0('AIR5DStartEff', 0)
    physicsXImpulse(40000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown3004(-20)
    Unknown2017(0)
    Unknown2015(40)
    SFX_3('jbse_08')

    def upon_LANDING():
        Unknown8000(100, 1, 1)
        Unknown1084(1)
        sendToLabel(10)
    loopRest()
    label(0)
    sprite('jb253_03', 3)	# 32783-32785
    Unknown21015('4149523544537461727445666600000000000000000000000000000000000000e209000000000000')
    StartMultihit()
    physicsXImpulse(40000)
    sprite('jb253_03', 4)	# 32786-32789
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('jb253_04', 4)	# 32790-32793
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb253_05', 4)	# 32794-32797
    sprite('jb253_06', 8)	# 32798-32805
    sprite('jb253_07', 4)	# 32806-32809
    GFX_1('jbef_noutou', 0)
    SFX_3('jbse_07')
    callSubroutine('Drive_DeriveInputBegin')
    sprite('jb253_08', 10)	# 32810-32819
    sprite('jb253_08', 10)	# 32820-32829
    callSubroutine('Drive_DeriveTimingBegin')
    JumpCancel_(1)
    loopRest()
    gotoLabel(9)
    label(10)
    sprite('jb253_03', 3)	# 32830-32832
    Unknown21015('4149523544537461727445666600000000000000000000000000000000000000e209000000000000')
    clearUponHandler(12)
    StartMultihit()
    physicsXImpulse(30000)
    sprite('jb253_03', 3)	# 32833-32835
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('jb253_04', 3)	# 32836-32838
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb253_05', 3)	# 32839-32841
    sprite('jb253_06', 6)	# 32842-32847
    sprite('jb253_07', 3)	# 32848-32850
    GFX_1('jbef_noutou', 0)
    SFX_3('jbse_07')
    sprite('jb253_08', 6)	# 32851-32856
    loopRest()
    Unknown48('190000000200000002000000160000000200000016000000')
    if SLOT_38:
        (SLOT_22 <= SLOT_2)
        if SLOT_0:
            _gotolabel(9)
    else:
        (SLOT_22 >= SLOT_2)
        if SLOT_0:
            _gotolabel(9)
    sprite('jb253_11', 3)	# 32857-32859
    sprite('jb253_12', 3)	# 32860-32862
    ExitState()
    label(9)
    sprite('jb253_09', 3)	# 32863-32865
    Unknown28(8, 'CmnActStandTurn')
    sprite('jb253_10', 3)	# 32866-32868

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('jb340_00', 3)	# 1-3
    sprite('jb340_01', 1)	# 4-4
    tag_voice(1, 'bjb156_0', 'bjb156_1', '', '')
    sprite('jb340_01', 2)	# 5-6
    sprite('jb340_02', 3)	# 7-9
    Unknown4047(224, 224, 224)
    sprite('jb340_03', 3)	# 10-12
    sprite('jb340_04', 1)	# 13-13
    sprite('jb340_05', 2)	# 14-15
    physicsXImpulse(15000)
    sprite('jb340_06', 2)	# 16-17
    SFX_0('010_swing_sword_2')
    SFX_3('jbse_03')
    sprite('jb340_07', 2)	# 18-19
    Unknown1019(50)
    sprite('jb340_08', 2)	# 20-21
    sprite('jb340_09', 3)	# 22-24	 **attackbox here**
    Unknown1019(0)
    GFX_0('jbef340_zanzou', 100)
    sprite('jb340_10', 4)	# 25-28
    sprite('jb340_11', 4)	# 29-32
    sprite('jb340_12', 4)	# 33-36
    sprite('jb340_13', 3)	# 37-39
    sprite('jb340_14', 3)	# 40-42
    sprite('jb340_15', 3)	# 43-45
    sprite('jb340_16', 3)	# 46-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown23027()

        def upon_11():
            ScreenShake(20000, 10000)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('jb340_10', 3)	# 2-4
    sprite('jb340_11', 3)	# 5-7
    sprite('jb340_12', 2)	# 8-9
    sprite('jb340_13', 2)	# 10-11
    sprite('jb340_14', 2)	# 12-13
    sprite('jb340_15', 2)	# 14-15
    sprite('jb340_16', 2)	# 16-17
    sprite('jb210_03', 4)	# 18-21
    Unknown2018(1, 60)
    sprite('jb210_04', 4)	# 22-25
    physicsXImpulse(5000)
    SFX_0('003_swing_grap_0_2')
    sprite('jb210_05', 4)	# 26-29
    Unknown1019(50)
    sprite('jb210_06', 4)	# 30-33	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    sprite('jb210_07', 4)	# 34-37
    tag_voice(0, 'bjb157_0', 'bjb157_1', '', '')
    sprite('jb210_08', 4)	# 38-41
    sprite('jb210_09', 3)	# 42-44
    sprite('jb210_10', 3)	# 45-47
    sprite('jb001_00', 6)	# 48-53
    sprite('jb001_01', 6)	# 54-59
    sprite('jb001_02', 6)	# 60-65
    sprite('jb001_03', 6)	# 66-71
    sprite('jb001_04', 8)	# 72-79
    sprite('jb001_06', 8)	# 80-87
    sprite('jb001_04', 8)	# 88-95
    sprite('jb001_06', 8)	# 96-103
    sprite('jb001_04', 8)	# 104-111
    sprite('jb001_06', 8)	# 112-119
    sprite('jb001_04', 8)	# 120-127
    sprite('jb001_03', 9)	# 128-136
    sprite('jb001_02', 9)	# 137-145
    sprite('jb001_01', 9)	# 146-154
    sprite('jb001_00', 9)	# 155-163
    label(0)
    sprite('jb000_00', 7)	# 164-170	 **attackbox here**
    sprite('jb000_01', 7)	# 171-177	 **attackbox here**
    sprite('jb000_02', 7)	# 178-184	 **attackbox here**
    sprite('jb000_03', 7)	# 185-191	 **attackbox here**
    sprite('jb000_04', 7)	# 192-198	 **attackbox here**
    sprite('jb000_05', 7)	# 199-205	 **attackbox here**
    sprite('jb000_06', 7)	# 206-212	 **attackbox here**
    sprite('jb000_07', 7)	# 213-219	 **attackbox here**
    sprite('jb000_08', 7)	# 220-226	 **attackbox here**
    sprite('jb000_09', 7)	# 227-233	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 234-234

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('jb400_11', 3)	# 1-3
    physicsXImpulse(0)
    Unknown8006(100, 1, 0)
    Unknown8007(100, 1, 0)
    sprite('jb401_00', 4)	# 4-7
    sprite('jb401_01', 4)	# 8-11
    Unknown1019(200)
    sprite('jb401_02', 3)	# 12-14
    Unknown1019(500)
    sprite('jb401_03', 4)	# 15-18	 **attackbox here**
    RefreshMultihit()
    GFX_0('jbef401_slash', 100)
    SFX_3('jbse_02')
    Unknown1019(25)
    physicsYImpulse(20000)
    Unknown1043()
    sendToLabelUpon(2, 9)
    sprite('jb401_04', 4)	# 19-22
    Unknown1019(80)
    sprite('jb401_05', 4)	# 23-26
    Unknown1019(50)
    sprite('jb401_06', 4)	# 27-30
    Unknown1019(50)
    sprite('jb401_07', 3)	# 31-33
    sprite('jb401_08', 3)	# 34-36
    sprite('jb401_12', 3)	# 37-39
    sprite('jb401_13', 3)	# 40-42
    sprite('jb401_14', 3)	# 43-45
    sprite('jb020_04', 3)	# 46-48
    sprite('jb020_05', 3)	# 49-51
    sprite('jb020_06', 3)	# 52-54
    label(0)
    sprite('jb020_07', 4)	# 55-58
    sprite('jb020_08', 4)	# 59-62
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('jb401_09', 4)	# 63-66
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 4)	# 67-70
    sprite('jb401_11', 4)	# 71-74
    sprite('jb001_00', 6)	# 75-80
    sprite('jb001_01', 6)	# 81-86
    sprite('jb001_02', 6)	# 87-92
    sprite('jb001_03', 6)	# 93-98
    sprite('jb001_04', 8)	# 99-106
    sprite('jb001_06', 8)	# 107-114
    sprite('jb001_04', 8)	# 115-122
    sprite('jb001_06', 8)	# 123-130
    sprite('jb001_04', 8)	# 131-138
    sprite('jb001_06', 8)	# 139-146
    sprite('jb001_04', 8)	# 147-154
    sprite('jb001_03', 9)	# 155-163
    sprite('jb001_02', 9)	# 164-172
    sprite('jb001_01', 9)	# 173-181
    sprite('jb001_00', 9)	# 182-190
    label(0)
    sprite('jb000_00', 7)	# 191-197	 **attackbox here**
    sprite('jb000_01', 7)	# 198-204	 **attackbox here**
    sprite('jb000_02', 7)	# 205-211	 **attackbox here**
    sprite('jb000_03', 7)	# 212-218	 **attackbox here**
    sprite('jb000_04', 7)	# 219-225	 **attackbox here**
    sprite('jb000_05', 7)	# 226-232	 **attackbox here**
    sprite('jb000_06', 7)	# 233-239	 **attackbox here**
    sprite('jb000_07', 7)	# 240-246	 **attackbox here**
    sprite('jb000_08', 7)	# 247-253	 **attackbox here**
    sprite('jb000_09', 7)	# 254-260	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 261-261

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
        sendToLabelUpon(2, 10)
    sprite('jb406_17', 2)	# 1-2
    sprite('jb406_18', 2)	# 3-4
    sprite('jb406_19', 2)	# 5-6
    Unknown1019(20)
    sprite('jb406_01', 2)	# 7-8
    SFX_0('024_getset_b')
    sprite('jb406_02', 2)	# 9-10
    sprite('jb406_03', 3)	# 11-13
    sprite('jb406_04', 3)	# 14-16
    Unknown1019(50)
    sprite('jb406_06', 3)	# 17-19
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown1084(1)
    tag_voice(0, 'bjb158_0', 'bjb158_1', '', '')
    sprite('jb406_07', 1)	# 20-20	 **attackbox here**
    GFX_0('jbef406_zanzou', 100)
    GFX_0('jbef406_zanzou2', 100)
    Unknown8000(100, 1, 0)
    sprite('jb406_07', 3)	# 21-23	 **attackbox here**
    physicsYImpulse(18000)
    Unknown1043()
    sprite('jb406_08', 4)	# 24-27
    sprite('jb406_09', 4)	# 28-31
    sprite('jb406_10', 4)	# 32-35
    sprite('jb406_11', 4)	# 36-39
    sprite('jb406_12', 32767)	# 40-32806
    label(10)
    sprite('jb406_13', 9)	# 32807-32815
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('jb406_14', 4)	# 32816-32819
    sprite('jb406_15', 4)	# 32820-32823

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
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
    sprite('jb020_07', 4)	# 29-32
    physicsXImpulse(36500)
    physicsYImpulse(-30000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('jb255_00', 3)	# 33-35
    sprite('jb255_01', 2)	# 36-37
    sprite('jb255_02', 2)	# 38-39
    SFX_0('010_swing_sword_1')
    sprite('jb255_03', 2)	# 40-41
    GFX_0('jbef255_zanzou', 100)
    sprite('jb255_04', 3)	# 42-44	 **attackbox here**
    sprite('jb255_05', 4)	# 45-48
    sprite('jb255_06', 4)	# 49-52
    sprite('jb255_07', 4)	# 53-56
    sprite('jb255_08', 4)	# 57-60
    sprite('jb255_09', 4)	# 61-64
    label(2)
    sprite('jb024_00', 3)	# 65-67
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('jb024_01', 3)	# 68-70
    sprite('jb024_02', 3)	# 71-73
    sprite('jb024_03', 3)	# 74-76
    sprite('jb024_04', 3)	# 77-79
    sprite('jb000_00', 7)	# 80-86	 **attackbox here**
    sprite('jb000_01', 7)	# 87-93	 **attackbox here**
    sprite('jb000_02', 7)	# 94-100	 **attackbox here**
    sprite('jb000_03', 7)	# 101-107	 **attackbox here**
    sprite('jb000_04', 7)	# 108-114	 **attackbox here**
    sprite('jb000_05', 7)	# 115-121	 **attackbox here**
    sprite('jb000_06', 7)	# 122-128	 **attackbox here**
    sprite('jb000_07', 7)	# 129-135	 **attackbox here**
    sprite('jb000_08', 7)	# 136-142	 **attackbox here**
    sprite('jb000_09', 7)	# 143-149	 **attackbox here**

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
        sendToLabelUpon(2, 9)
    sprite('jb212_00', 1)	# 1-1
    sprite('jb212_01', 1)	# 2-2
    sprite('jb212_02', 1)	# 3-3
    sprite('jb212_03', 2)	# 4-5
    Unknown1084(1)
    physicsXImpulse(4000)
    physicsYImpulse(4000)
    Unknown1043()
    sprite('jb212_04', 2)	# 6-7
    SFX_0('006_swing_blade_2')
    sprite('jb212_05', 2)	# 8-9
    sprite('jb212_06', 32767)	# 10-32776
    label(9)
    sprite('jb212_07', 3)	# 32777-32779	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown8003(0, 1, 0)
    GFX_0('jbef212_zanzou', 100)
    sprite('jb212_08', 3)	# 32780-32782
    sprite('jb212_09', 3)	# 32783-32785
    sprite('jb212_10', 3)	# 32786-32788
    sprite('jb212_11', 3)	# 32789-32791
    sprite('jb212_12', 3)	# 32792-32794
    sprite('jb212_13', 3)	# 32795-32797
    loopRest()
    sprite('jb001_00', 6)	# 32798-32803
    sprite('jb001_01', 6)	# 32804-32809
    sprite('jb001_02', 6)	# 32810-32815
    sprite('jb001_03', 6)	# 32816-32821
    sprite('jb001_04', 8)	# 32822-32829
    sprite('jb001_06', 8)	# 32830-32837
    sprite('jb001_04', 8)	# 32838-32845
    sprite('jb001_06', 8)	# 32846-32853
    sprite('jb001_04', 8)	# 32854-32861
    sprite('jb001_06', 8)	# 32862-32869
    sprite('jb001_04', 8)	# 32870-32877
    sprite('jb001_03', 9)	# 32878-32886
    sprite('jb001_02', 9)	# 32887-32895
    sprite('jb001_01', 9)	# 32896-32904
    sprite('jb001_00', 9)	# 32905-32913
    sprite('jb000_00', 7)	# 32914-32920	 **attackbox here**
    sprite('jb000_01', 7)	# 32921-32927	 **attackbox here**
    sprite('jb000_02', 7)	# 32928-32934	 **attackbox here**
    sprite('jb000_03', 7)	# 32935-32941	 **attackbox here**
    sprite('jb000_04', 7)	# 32942-32948	 **attackbox here**
    sprite('jb000_05', 7)	# 32949-32955	 **attackbox here**
    sprite('jb000_06', 7)	# 32956-32962	 **attackbox here**
    sprite('jb000_07', 7)	# 32963-32969	 **attackbox here**
    sprite('jb000_08', 7)	# 32970-32976	 **attackbox here**
    sprite('jb000_09', 7)	# 32977-32983	 **attackbox here**

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
        sendToLabelUpon(2, 10)
    sprite('jb406_17', 2)	# 1-2
    sprite('jb406_18', 2)	# 3-4
    sprite('jb406_19', 2)	# 5-6
    Unknown1019(20)
    sprite('jb406_01', 2)	# 7-8
    SFX_0('024_getset_b')
    sprite('jb406_02', 2)	# 9-10
    sprite('jb406_03', 3)	# 11-13
    sprite('jb406_04', 3)	# 14-16
    Unknown1019(50)
    sprite('jb406_06', 3)	# 17-19
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown1084(1)
    sprite('jb406_07', 1)	# 20-20	 **attackbox here**
    GFX_0('jbef406_zanzou', 100)
    GFX_0('jbef406_zanzou2', 100)
    Unknown8000(100, 1, 0)
    sprite('jb406_07', 3)	# 21-23	 **attackbox here**
    physicsYImpulse(18000)
    Unknown1043()
    sprite('jb406_08', 4)	# 24-27
    sprite('jb406_09', 4)	# 28-31
    sprite('jb406_10', 4)	# 32-35
    sprite('jb406_11', 4)	# 36-39
    sprite('jb406_12', 32767)	# 40-32806
    label(10)
    sprite('jb406_13', 9)	# 32807-32815
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('jb406_14', 4)	# 32816-32819
    sprite('jb406_15', 4)	# 32820-32823

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(17500)
            if (SLOT_18 >= 7):
                Unknown1015(2500)
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('jb030_00', 4)	# 1-4
    sprite('jb032_00', 2)	# 5-6
    sprite('jb032_01', 2)	# 7-8
    label(0)
    sprite('jb032_02', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('jb032_03', 3)	# 13-15
    sprite('jb032_04', 3)	# 16-18
    sprite('jb032_05', 4)	# 19-22
    Unknown8006(100, 1, 1)
    sprite('jb032_06', 3)	# 23-25
    sprite('jb032_07', 3)	# 26-28
    sprite('jb032_08', 3)	# 29-31
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jb310_00', 1)	# 32-32
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('jb310_01', 2)	# 33-34
    sprite('jb310_02', 3)	# 35-37	 **attackbox here**
    Unknown1084(1)
    sprite('jb310_03', 3)	# 38-40
    SFX_0('010_swing_sword_0')
    SFX_4('bjb154')
    sprite('jb310_04', 3)	# 41-43
    sprite('jb310_05', 11)	# 44-54
    sprite('jb310_06', 3)	# 55-57
    sprite('jb310_07', 3)	# 58-60

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(-4000)
        AirUntechableTime(60)
        Unknown9310(10)
        Unknown11072(1, 0, 200000)
        Unknown11080(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('ThrowExe')
        JumpCancel_(0)
        Unknown13024(0)
        Unknown2004(1, 0)
    sprite('jb310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('jb311_00', 4)	# 4-7
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('019_cloth_c')
    sprite('jb311_01', 4)	# 8-11
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('jb311_02', 4)	# 12-15	 **attackbox here**
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SFX_0('005_swing_grap_2_1')
    SFX_4('bjb153')
    sprite('jb311_03', 3)	# 16-18
    sprite('jb311_04', 3)	# 19-21
    sprite('jb311_05', 3)	# 22-24
    sprite('jb311_06', 3)	# 25-27
    sprite('jb311_07', 3)	# 28-30	 **attackbox here**
    GFX_0('jbef311_claw', 100)
    SFX_3('jbse_02')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    AttackP2(50)
    Hitstop(8)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(24000)
    AirPushbackY(-36000)
    Unknown11072(0, 0, 0)
    Unknown9016(1)
    Unknown11080(0)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')

    def upon_11():
        JumpCancel_(1)
        Unknown13024(1)
    sprite('jb311_08', 3)	# 31-33
    sprite('jb311_09', 3)	# 34-36
    sprite('jb311_10', 3)	# 37-39
    sprite('jb311_11', 3)	# 40-42

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(17500)
            if (SLOT_18 >= 7):
                Unknown1015(2500)
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('jb030_00', 4)	# 1-4
    sprite('jb032_00', 2)	# 5-6
    sprite('jb032_01', 2)	# 7-8
    label(0)
    sprite('jb032_02', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('jb032_03', 3)	# 13-15
    sprite('jb032_04', 3)	# 16-18
    sprite('jb032_05', 4)	# 19-22
    Unknown8006(100, 1, 1)
    sprite('jb032_06', 3)	# 23-25
    sprite('jb032_07', 3)	# 26-28
    sprite('jb032_08', 3)	# 29-31
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('jb310_00', 1)	# 32-32
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('jb310_01', 2)	# 33-34
    sprite('jb310_02', 3)	# 35-37	 **attackbox here**
    Unknown1084(1)
    sprite('jb310_03', 3)	# 38-40
    SFX_0('010_swing_sword_0')
    SFX_4('bjb154')
    sprite('jb310_04', 3)	# 41-43
    sprite('jb310_05', 11)	# 44-54
    sprite('jb310_06', 3)	# 55-57
    sprite('jb310_07', 3)	# 58-60

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(-1000)
        AirUntechableTime(60)
        Hitstop(8)
        Unknown9310(10)
        Unknown11072(1, 110000, 200000)
        Unknown11069('BackThrowExe')
        JumpCancel_(0)
        Unknown13024(0)
        Unknown2004(1, 0)
    sprite('jb310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('jb313_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('jb313_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('jb313_02', 3)	# 10-12
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('jb313_03', 3)	# 13-15
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('jb313_04', 3)	# 16-18
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_0('003_swing_grap_0_2')
    sprite('jb313_05', 6)	# 19-24	 **attackbox here**
    SFX_4('bjb153')
    sprite('jb313_06', 3)	# 25-27
    sprite('jb313_07', 3)	# 28-30
    sprite('jb311_04', 3)	# 31-33
    Unknown2005()
    sprite('jb311_05', 3)	# 34-36
    sprite('jb311_06', 3)	# 37-39
    sprite('jb311_07', 3)	# 40-42	 **attackbox here**
    GFX_0('jbef311_claw', 100)
    SFX_3('jbse_02')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    AttackP2(50)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(24000)
    AirPushbackY(-36000)
    Unknown11072(0, 0, 0)
    Unknown9016(1)
    Unknown11069('')

    def upon_11():
        JumpCancel_(1)
        Unknown13024(1)
    sprite('jb311_08', 3)	# 43-45
    sprite('jb311_09', 3)	# 46-48
    sprite('jb311_10', 3)	# 49-51
    sprite('jb311_11', 3)	# 52-54

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1700)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(10000)
        Unknown30056('e09304003200000000000000')
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11056(0)

        def upon_STATE_END():
            SLOT_62 = 0
    sprite('jb400_11', 3)	# 1-3
    physicsXImpulse(2500)
    Unknown8006(100, 1, 0)
    Unknown8007(100, 1, 0)
    sprite('jb401_00', 3)	# 4-6
    sprite('jb401_01', 3)	# 7-9
    Unknown1019(200)
    sprite('jb401_02', 2)	# 10-11
    if 
    if (not 
    if (not 
    if (not 
    if (not 
    if (not Unknown23145('NmlAtk5B')):
        Unknown23145('NmlAtk5B2nd')):
        Unknown23145('NmlAtk5B3rd')):
        Unknown23145('NmlAtk5B4th')):
        Unknown23145('NmlAtkAIR5B')):
        Unknown23145('NmlAtkAIR5B2nd'):
        Unknown2037(1)
        SFX_4('bjb202_0')
    else:
        tag_voice(1, 'bjb202_0', 'bjb202_1', 'bjb202_2', '')
    Unknown1019(500)
    sprite('jb401_03ex01', 4)	# 12-15	 **attackbox here**
    GFX_0('jbef401_slash', 100)
    SFX_3('jbse_02')
    Unknown1019(25)
    physicsYImpulse(20000)
    Unknown1043()
    sendToLabelUpon(2, 9)
    sprite('jb401_04', 4)	# 16-19
    setInvincible(0)
    Unknown1019(80)
    sprite('jb402_11', 2)	# 20-21
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown26('jbef400_slash2')
    Unknown8001(3, 100)
    sprite('jb402_01', 2)	# 22-23
    physicsYImpulse(25000)
    Unknown1043()
    sprite('jb402_02', 2)	# 24-25
    sprite('jb402_03', 2)	# 26-27
    if (not SLOT_2):
        tag_voice(0, '', 'bjb203_1', '', '')
    sprite('jb402_04', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(40000)
    AirPushbackY(-60000)
    Unknown30056('000000000000000000000000')
    Unknown9310(1)
    Unknown9016(1)
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown11061(1)
    GFX_0('jbef402_slash', 100)
    SFX_3('jbse_02')
    sprite('jb402_05', 3)	# 31-33
    Unknown1019(20)
    sprite('jb402_06', 3)	# 34-36
    sprite('jb402_07', 3)	# 37-39
    sprite('jb402_08', 3)	# 40-42
    sprite('jb402_09', 3)	# 43-45
    sprite('jb402_12', 3)	# 46-48
    sprite('jb020_04', 3)	# 49-51
    sprite('jb020_05', 3)	# 52-54
    sprite('jb020_06', 3)	# 55-57
    label(0)
    sprite('jb020_07', 4)	# 58-61
    sprite('jb020_08', 4)	# 62-65
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('jb401_09', 6)	# 66-71
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 6)	# 72-77
    sprite('jb401_11', 6)	# 78-83

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1700)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(10000)
        Unknown30056('e09304003200000000000000')
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11056(0)
        Unknown11058('0100000000000000000000000000000000000000')

        def upon_STATE_END():
            SLOT_62 = 0
            Unknown2016(-1)
            Unknown23087(-1)
    sprite('jb400_11', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(5000)
    Unknown8009(1)
    Unknown2016(100)
    Unknown23087(80000)
    sprite('jb401_00', 3)	# 4-6
    sprite('jb401_01', 3)	# 7-9
    Unknown1019(200)
    sprite('jb401_02', 2)	# 10-11
    if 
    if (not 
    if (not 
    if (not 
    if (not 
    if (not Unknown23145('NmlAtk5B')):
        Unknown23145('NmlAtk5B2nd')):
        Unknown23145('NmlAtk5B3rd')):
        Unknown23145('NmlAtk5B4th')):
        Unknown23145('NmlAtkAIR5B')):
        Unknown23145('NmlAtkAIR5B2nd'):
        Unknown2037(1)
        SFX_4('bjb202_0')
    else:
        tag_voice(1, 'bjb202_0', 'bjb202_1', 'bjb202_2', '')
    Unknown1019(500)
    sprite('jb401_03ex01', 4)	# 12-15	 **attackbox here**
    GFX_0('jbef401_slash', 100)
    SFX_3('jbse_02')
    Unknown1019(25)
    physicsYImpulse(20000)
    Unknown1043()
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    sprite('jb401_04', 4)	# 16-19
    setInvincible(0)
    Unknown1019(80)
    sprite('jb402_11', 2)	# 20-21
    Unknown1084(1)
    physicsXImpulse(10000)
    Unknown26('jbef400_slash2')
    Unknown8001(3, 100)
    sprite('jb402_01', 2)	# 22-23
    physicsYImpulse(25000)
    Unknown1043()
    sprite('jb402_02', 2)	# 24-25
    sprite('jb402_03', 2)	# 26-27
    if (not SLOT_2):
        tag_voice(0, '', 'bjb203_1', '', '')
    sprite('jb402_04', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(40000)
    AirPushbackY(-60000)
    Unknown30056('000000000000000000000000')
    Unknown9310(1)
    Unknown9016(1)
    Unknown11061(1)
    GFX_0('jbef402_slash', 100)
    SFX_3('jbse_02')
    sprite('jb402_05', 3)	# 31-33
    Unknown1019(20)
    sprite('jb402_06', 3)	# 34-36
    sprite('jb402_07', 3)	# 37-39
    sprite('jb402_08', 3)	# 40-42
    sprite('jb402_09', 3)	# 43-45
    sprite('jb402_12', 3)	# 46-48
    sprite('jb020_04', 3)	# 49-51
    sprite('jb020_05', 3)	# 52-54
    sprite('jb020_06', 3)	# 55-57
    label(0)
    sprite('jb020_07', 4)	# 58-61
    sprite('jb020_08', 4)	# 62-65
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('jb401_09', 6)	# 66-71
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    Unknown2016(-1)
    Unknown23087(-1)
    sprite('jb401_10', 6)	# 72-77
    sprite('jb401_11', 6)	# 78-83

@State
def Rekkouha():

    def upon_IMMEDIATE():
        Unknown17025('')
        setInvincible(0)
        AttackLevel_(3)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(6000)
        AirUntechableTime(30)
        Unknown9202(10)
        Unknown9178(1)
        Unknown9346(1)
        WallbounceReboundTime(0)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown30068(1)

        def upon_STATE_END():
            SLOT_62 = 0
        Unknown28(2, 'CmnActJumpLanding')
        Unknown22004(10, 1)
    sprite('jb402_11', 2)	# 1-2
    Unknown1084(1)
    physicsXImpulse(20000)
    Unknown26('jbef400_slash2')
    Unknown8001(3, 100)
    sprite('jb402_01', 2)	# 3-4
    physicsYImpulse(25000)
    Unknown1043()
    sprite('jb402_02', 2)	# 5-6
    sprite('jb402_03', 2)	# 7-8
    sprite('jb402_04', 3)	# 9-11	 **attackbox here**
    GFX_0('jbef402_slash', 100)
    SFX_3('jbse_02')
    sprite('jb402_05', 3)	# 12-14
    Unknown1019(20)
    sprite('jb402_06', 3)	# 15-17
    sprite('jb402_07', 3)	# 18-20
    sprite('jb402_08', 3)	# 21-23
    sprite('jb402_09', 3)	# 24-26
    sprite('jb402_12', 3)	# 27-29
    sprite('jb020_04', 3)	# 30-32
    sprite('jb020_05', 3)	# 33-35
    sprite('jb020_06', 3)	# 36-38
    label(0)
    sprite('jb020_07', 4)	# 39-42
    sprite('jb020_08', 4)	# 43-46
    loopRest()
    gotoLabel(0)

@State
def Assault_Low():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Low_Atk')
    sprite('jb403_13', 2)	# 1-2
    Unknown1045(30000)
    Unknown8007(100, 1, 0)
    sprite('jb403_14', 2)	# 3-4
    sprite('jb403_01', 2)	# 5-6
    sprite('jb403_02', 2)	# 7-8
    sprite('jb403_03', 2)	# 9-10
    Unknown1051(50)
    Unknown8006(100, 1, 0)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb403_04', 2)	# 11-12
    Unknown7007('626a623230345f30000000000000000064000000626a623230345f31000000000000000064000000626a623230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb403_05', 2)	# 13-14	 **attackbox here**
    Unknown1084(1)
    GFX_0('jbef403_zanzou', 100)
    GFX_0('jbef403_zanzou2', 100)
    sprite('jb403_06', 2)	# 15-16
    Recovery()
    Unknown2063()
    sprite('jb403_07', 4)	# 17-20
    sprite('jb403_08', 4)	# 21-24
    sprite('jb403_09', 3)	# 25-27
    sprite('jb403_10', 3)	# 28-30
    sprite('jb403_11', 3)	# 31-33
    sprite('jb403_12', 3)	# 34-36

@State
def Assault_ChageAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Chage_Atk')
        sendToLabelUpon(2, 10)
    sprite('jb406_17', 2)	# 1-2
    physicsXImpulse(20000)
    sprite('jb406_18', 2)	# 3-4
    sprite('jb406_19', 2)	# 5-6
    Unknown1019(20)
    sprite('jb406_01', 2)	# 7-8
    SFX_0('024_getset_b')
    sprite('jb406_02', 2)	# 9-10
    sprite('jb406_03', 3)	# 11-13
    label(0)
    sprite('jb406_04', 3)	# 14-16
    Unknown1019(50)
    sprite('jb406_05', 3)	# 17-19
    loopRest()
    gotoLabel(0)
    label(8)
    sprite('jb406_06', 5)	# 20-24
    clearUponHandler(3)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a623230375f30000000000000000064000000626a623230375f31000000000000000064000000626a623230375f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1084(1)
    sprite('jb406_07', 3)	# 25-27	 **attackbox here**
    teleportRelativeX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(16000)
    Unknown1043()
    GFX_0('jbef406_zanzou', 100)
    GFX_0('jbef406_zanzou2', 100)
    Unknown8000(100, 1, 0)
    sprite('jb406_08', 3)	# 28-30
    sprite('jb406_09', 3)	# 31-33
    sprite('jb406_10', 3)	# 34-36
    sprite('jb406_11', 3)	# 37-39
    sprite('jb406_12', 32767)	# 40-32806
    label(9)
    sprite('jb406_06', 3)	# 32807-32809
    clearUponHandler(3)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a623230375f30000000000000000064000000626a623230375f31000000000000000064000000626a623230375f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1084(1)
    sprite('jb406_07', 1)	# 32810-32810	 **attackbox here**
    teleportRelativeX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(24000)
    Unknown1043()
    GFX_0('jbef406_zanzou', 100)
    GFX_0('jbef406_zanzou2', 100)
    Unknown8000(100, 1, 0)
    sprite('jb406_07', 3)	# 32811-32813	 **attackbox here**
    StartMultihit()
    sprite('jb406_08', 4)	# 32814-32817
    sprite('jb406_09', 4)	# 32818-32821
    sprite('jb406_10', 4)	# 32822-32825
    sprite('jb406_11', 4)	# 32826-32829
    sprite('jb406_12', 32767)	# 32830-65596
    label(10)
    sprite('jb406_13', 3)	# 65597-65599
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('jb406_14', 3)	# 65600-65602
    sprite('jb406_15', 3)	# 65603-65605

@State
def Assault_Low_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Low_Atk')
        Damage(2200)
        Unknown11028(24)
        Unknown30065(0)
        Unknown11091(10)
    sprite('jb403_13', 2)	# 1-2
    Unknown1045(60000)
    Unknown8007(100, 1, 0)
    sprite('jb403_14', 1)	# 3-3
    sprite('jb403_14', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('jb403_01', 1)	# 5-5
    sprite('jb403_02', 1)	# 6-6
    sprite('jb403_03', 1)	# 7-7
    Unknown1051(75)
    Unknown8006(100, 1, 0)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb403_04', 1)	# 8-8
    Unknown7007('626a623230345f30000000000000000064000000626a623230345f31000000000000000064000000626a623230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb403_05', 2)	# 9-10	 **attackbox here**
    Unknown1084(1)
    GFX_0('jbef403_zanzou', 100)
    GFX_0('jbef403_zanzou2', 100)
    sprite('jb403_06', 4)	# 11-14
    Recovery()
    Unknown2063()
    sprite('jb403_07', 4)	# 15-18
    sprite('jb403_08', 4)	# 19-22
    sprite('jb403_09', 4)	# 23-26
    sprite('jb403_10', 4)	# 27-30
    sprite('jb403_11', 4)	# 31-34
    sprite('jb403_12', 4)	# 35-38

@State
def Assault_Mid():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Mid_Atk')
        sendToLabelUpon(2, 9)

        def upon_STATE_END():
            Unknown2006()
    sprite('jb404_15', 2)	# 1-2
    sprite('jb404_16', 1)	# 3-3
    sprite('jb404_16', 2)	# 4-5
    Unknown7007('626a623230355f30000000000000000064000000626a623230355f31000000000000000064000000626a623230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb404_17', 3)	# 6-8
    sprite('jb404_01', 4)	# 9-12
    physicsXImpulse(20000)
    physicsYImpulse(20000)
    setGravity(1600)
    Unknown8001(3, 100)
    sprite('jb404_02', 4)	# 13-16
    sprite('jb404_03', 4)	# 17-20
    sprite('jb404_04', 3)	# 21-23
    Unknown1019(80)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb404_05', 1)	# 24-24	 **attackbox here**
    Unknown1019(80)
    StartMultihit()
    GFX_0('jbef404_zanzou', 100)
    sprite('jb404_05', 3)	# 25-27	 **attackbox here**
    sprite('jb404_06', 3)	# 28-30
    Unknown1019(80)
    Recovery()
    sprite('jb404_07', 3)	# 31-33
    Unknown1019(80)
    sprite('jb404_08', 3)	# 34-36
    sprite('jb404_09', 32767)	# 37-32803
    label(9)
    sprite('jb404_10', 6)	# 32804-32809
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('jb404_11', 5)	# 32810-32814

@State
def Assault_Multi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Multi_Atk')
        sendToLabelUpon(2, 2)
    sprite('jb405_00', 3)	# 1-3
    sprite('jb405_01', 3)	# 4-6
    Unknown2017(0)
    physicsXImpulse(30000)
    physicsYImpulse(32000)
    Unknown1043()
    Unknown8001(3, 100)
    sprite('jb405_02', 3)	# 7-9
    Unknown1019(80)
    Unknown7007('626a623230365f30000000000000000064000000626a623230365f31000000000000000064000000626a623230365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb405_03', 3)	# 10-12
    Unknown1019(80)
    sprite('jb405_04', 3)	# 13-15
    Unknown1019(80)
    sprite('jb405_05', 3)	# 16-18	 **attackbox here**
    GFX_0('jbef405_loop', 100)
    Unknown23027()
    Unknown2017(1)
    Unknown3029(1)
    sprite('jb405_06', 3)	# 19-21	 **attackbox here**
    sprite('jb405_07', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    loopRest()
    label(10)
    sprite('jb405_05', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    sprite('jb405_06', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    sprite('jb405_07', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('jb405_08', 4)	# 34-37
    Unknown1084(1)
    Unknown26('jbef405_loop')
    Unknown8000(100, 1, 1)
    ScreenShake(0, 8000)
    Unknown2006()
    sprite('jb405_09', 4)	# 38-41
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb405_10', 4)	# 42-45	 **attackbox here**
    Unknown3029(0)
    GFX_0('jbef405_zanzou', 100)
    RefreshMultihit()
    callSubroutine('Assault_MultiFinish_Atk')
    sprite('jb405_11', 4)	# 46-49
    Recovery()
    Unknown2063()
    sprite('jb405_12', 4)	# 50-53
    sprite('jb405_13', 4)	# 54-57
    sprite('jb405_14', 3)	# 58-60
    sprite('jb405_15', 3)	# 61-63
    sprite('jb405_16', 3)	# 64-66
    sprite('jb405_17', 3)	# 67-69

@State
def Assault_Mid_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Mid_Atk')
        Damage(1980)
        Unknown30065(0)
        Unknown11091(10)
        sendToLabelUpon(2, 9)

        def upon_STATE_END():
            Unknown2006()
    sprite('jb404_15', 1)	# 1-1
    sprite('jb404_16', 1)	# 2-2
    sprite('jb404_17', 1)	# 3-3
    sprite('jb404_01', 4)	# 4-7
    physicsXImpulse(20000)
    physicsYImpulse(20000)
    setGravity(1600)
    Unknown8001(3, 100)
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('626a623230355f30000000000000000064000000626a623230355f31000000000000000064000000626a623230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb404_02', 4)	# 8-11
    sprite('jb404_03', 4)	# 12-15
    sprite('jb404_04', 3)	# 16-18
    Unknown1019(80)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb404_05', 1)	# 19-19	 **attackbox here**
    Unknown1019(80)
    StartMultihit()
    GFX_0('jbef404_zanzou', 100)
    sprite('jb404_05', 3)	# 20-22	 **attackbox here**
    sprite('jb404_06', 3)	# 23-25
    Unknown1019(80)
    Recovery()
    sprite('jb404_07', 3)	# 26-28
    Unknown1019(80)
    sprite('jb404_08', 3)	# 29-31
    sprite('jb404_09', 32767)	# 32-32798
    label(9)
    sprite('jb404_10', 6)	# 32799-32804
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('jb404_11', 5)	# 32805-32809

@State
def Rekkouzan_Low():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Low_Atk')
        Unknown30068(1)
        clearUponHandler(12)

        def upon_STATE_END():
            SLOT_62 = 0
    sprite('jb400_11', 2)	# 1-2
    if SLOT_37:
        Unknown1045(20000)
        Unknown8007(100, 1, 0)
    else:
        Unknown1018()
        Unknown1019(50)
        physicsYImpulse(6000)
        Unknown1043()
    sprite('jb403_00', 2)	# 3-4
    sprite('jb403_01', 2)	# 5-6
    sprite('jb403_02', 2)	# 7-8
    Unknown20(32767, 2, 36)
    if SLOT_36:
        Unknown1039(150)

        def upon_LANDING():
            sendToLabel(0)
    label(0)
    sprite('jb403_03', 2)	# 9-10
    Unknown8006(100, 1, 0)
    loopRest()
    gotoLabel(3)
    label(3)
    sprite('jb403_04', 2)	# 11-12
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a623230345f30000000000000000064000000626a623230345f31000000000000000064000000626a623230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb403_05', 2)	# 13-14	 **attackbox here**
    Unknown1084(1)
    GFX_0('jbef403_zanzou', 100)
    GFX_0('jbef403_zanzou2', 100)
    sprite('jb403_06', 2)	# 15-16
    Recovery()
    sprite('jb403_07', 4)	# 17-20
    sprite('jb403_08', 4)	# 21-24
    sprite('jb403_09', 3)	# 25-27
    sprite('jb403_10', 3)	# 28-30
    sprite('jb403_11', 3)	# 31-33
    sprite('jb403_12', 3)	# 34-36

@State
def Rekkouzan_Chage():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Chage_Atk')
        Unknown30068(1)

        def upon_STATE_END():
            SLOT_62 = 0
    sprite('jb400_11', 1)	# 1-1
    physicsXImpulse(20000)
    if SLOT_36:
        physicsYImpulse(6000)
        Unknown1043()
    sprite('jb400_12', 1)	# 2-2
    sprite('jb400_13', 1)	# 3-3
    sprite('jb406_00', 1)	# 4-4
    Unknown20(32767, 2, 36)
    if SLOT_36:
        Unknown1039(150)

        def upon_LANDING():
            sendToLabel(0)
    label(0)
    sprite('jb406_01', 2)	# 5-6
    SFX_0('024_getset_b')
    sprite('jb406_02', 2)	# 7-8
    sprite('jb406_03', 2)	# 9-10
    Unknown1084(1)
    loopRest()
    gotoLabel(3)
    label(3)
    sprite('jb406_04', 3)	# 11-13
    sprite('jb406_05', 3)	# 14-16
    loopRest()
    gotoLabel(3)
    label(8)
    sprite('jb406_06', 1)	# 17-17
    clearUponHandler(3)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a623230375f30000000000000000064000000626a623230375f31000000000000000064000000626a623230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb406_07', 3)	# 18-20	 **attackbox here**
    teleportRelativeX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(16000)
    Unknown1043()
    GFX_0('jbef406_zanzou', 100)
    GFX_0('jbef406_zanzou2', 100)
    Unknown8000(100, 1, 0)
    sendToLabelUpon(2, 10)
    sprite('jb406_08', 3)	# 21-23
    sprite('jb406_09', 3)	# 24-26
    sprite('jb406_10', 3)	# 27-29
    sprite('jb406_11', 3)	# 30-32
    sprite('jb406_12', 32767)	# 33-32799
    label(9)
    sprite('jb406_06', 3)	# 32800-32802
    clearUponHandler(3)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a623230375f30000000000000000064000000626a623230375f31000000000000000064000000626a623230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb406_07', 1)	# 32803-32803	 **attackbox here**
    teleportRelativeX(40000)
    physicsXImpulse(-4000)
    physicsYImpulse(24000)
    Unknown1043()
    GFX_0('jbef406_zanzou', 100)
    GFX_0('jbef406_zanzou2', 100)
    Unknown8000(100, 1, 0)
    sendToLabelUpon(2, 10)
    sprite('jb406_07', 3)	# 32804-32806	 **attackbox here**
    StartMultihit()
    sprite('jb406_08', 4)	# 32807-32810
    sprite('jb406_09', 4)	# 32811-32814
    sprite('jb406_10', 4)	# 32815-32818
    sprite('jb406_11', 4)	# 32819-32822
    sprite('jb406_12', 32767)	# 32823-65589
    label(10)
    sprite('jb406_13', 3)	# 65590-65592
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('jb406_14', 3)	# 65593-65595
    sprite('jb406_15', 3)	# 65596-65598

@State
def Rekkouzan_Mid():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Mid_Atk')
        Unknown30068(1)
        PushbackX(5000)
        if SLOT_37:
            Unknown8006(100, 1, 0)
            Unknown8007(100, 1, 0)
        if SLOT_36:
            SLOT_61 = 1
            if (not SLOT_62):
                Unknown2016(100)
                Unknown23087(80000)

        def upon_STATE_END():
            SLOT_62 = 0
            Unknown2006()
        Unknown28(2, 'CmnActJumpLanding')
        Unknown22004(10, 1)
    sprite('jb400_11', 1)	# 1-1
    physicsXImpulse(20000)
    sprite('jb404_00', 1)	# 2-2
    sprite('jb404_01', 1)	# 3-3
    if SLOT_36:
        Unknown2016(-1)
        Unknown23087(-1)
        Unknown1007(-80000)
    if SLOT_37:
        Unknown8001(3, 100)
    Unknown1019(30)
    physicsYImpulse(23000)
    Unknown1043()
    sprite('jb404_01', 1)	# 4-4
    Unknown7007('626a623230355f30000000000000000064000000626a623230355f31000000000000000064000000626a623230355f320000000000000000640000000000000000000000000000000000000000000000')
    loopRest()
    gotoLabel(1)
    label(1)
    sprite('jb404_02', 3)	# 5-7
    sprite('jb404_03', 3)	# 8-10
    sprite('jb404_03', 3)	# 11-13
    sprite('jb404_04', 3)	# 14-16
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb404_05', 1)	# 17-17	 **attackbox here**
    StartMultihit()
    GFX_0('jbef404_zanzou', 100)
    sprite('jb404_05', 3)	# 18-20	 **attackbox here**
    sprite('jb404_06', 2)	# 21-22
    Recovery()
    sprite('jb404_07', 2)	# 23-24
    sprite('jb404_08', 2)	# 25-26
    sprite('jb404_09', 2)	# 27-28
    sprite('jb404_13', 2)	# 29-30
    sprite('jb404_14', 2)	# 31-32

@State
def Rekkouzan_Multi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Multi_Atk')
        Unknown30068(1)
        if SLOT_37:
            Unknown8006(100, 1, 0)
            Unknown8007(100, 1, 0)
        if SLOT_36:
            if (not SLOT_62):
                Unknown2016(100)
                Unknown23087(80000)

        def upon_STATE_END():
            SLOT_62 = 0
        sendToLabelUpon(2, 2)
    if SLOT_36:
        _gotolabel(0)
    sprite('jb400_11', 3)	# 1-3
    physicsXImpulse(30000)
    sprite('jb405_00', 3)	# 4-6
    sprite('jb405_01', 3)	# 7-9
    Unknown2017(0)
    Unknown1019(80)
    physicsYImpulse(30000)
    Unknown1043()
    Unknown8001(3, 100)
    sprite('jb405_02', 3)	# 10-12
    Unknown1019(80)
    Unknown7007('626a623230365f30000000000000000064000000626a623230365f31000000000000000064000000626a623230365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb405_03', 3)	# 13-15
    Unknown1019(80)
    sprite('jb405_04', 3)	# 16-18
    Unknown1019(80)
    sprite('jb405_05', 3)	# 19-21	 **attackbox here**
    GFX_0('jbef405_loop', 100)
    Unknown23027()
    Unknown2017(1)
    Unknown3029(1)
    sprite('jb405_06', 3)	# 22-24	 **attackbox here**
    sprite('jb405_07', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(0)
    sprite('jb400_11', 2)	# 28-29
    physicsXImpulse(30000)
    sprite('jb405_00', 2)	# 30-31
    sprite('jb405_01', 3)	# 32-34
    Unknown2017(0)
    Unknown1019(80)
    physicsYImpulse(20000)
    Unknown1043()
    Unknown2016(-1)
    Unknown23087(-1)
    Unknown1007(-80000)
    sprite('jb405_02', 3)	# 35-37
    Unknown1019(80)
    Unknown7007('626a623230365f30000000000000000064000000626a623230365f31000000000000000064000000626a623230365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb405_03', 3)	# 38-40
    Unknown1019(80)
    sprite('jb405_04', 3)	# 41-43
    Unknown1019(80)
    sprite('jb405_05', 3)	# 44-46	 **attackbox here**
    GFX_0('jbef405_loop', 100)
    RefreshMultihit()
    Unknown2017(1)
    Unknown3029(1)
    sprite('jb405_06', 3)	# 47-49	 **attackbox here**
    RefreshMultihit()
    sprite('jb405_07', 3)	# 50-52	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(10)
    sprite('jb405_05', 3)	# 53-55	 **attackbox here**
    RefreshMultihit()
    sprite('jb405_06', 3)	# 56-58	 **attackbox here**
    RefreshMultihit()
    sprite('jb405_07', 3)	# 59-61	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('jb405_08', 4)	# 62-65
    Unknown1084(1)
    Unknown26('jbef405_loop')
    Unknown8000(100, 1, 1)
    ScreenShake(0, 8000)
    Unknown2006()
    sprite('jb405_09', 4)	# 66-69
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb405_10', 4)	# 70-73	 **attackbox here**
    Unknown3029(0)
    GFX_0('jbef405_zanzou', 100)
    RefreshMultihit()
    callSubroutine('Assault_MultiFinish_Atk')
    sprite('jb405_11', 4)	# 74-77
    Recovery()
    Unknown2063()
    sprite('jb405_12', 4)	# 78-81
    sprite('jb405_13', 4)	# 82-85
    sprite('jb405_14', 3)	# 86-88
    sprite('jb405_15', 3)	# 89-91
    sprite('jb405_16', 3)	# 92-94
    sprite('jb405_17', 3)	# 95-97

@State
def Rekkouzan_Low_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Low_Atk')
        Damage(2200)
        Unknown11028(24)
        Unknown30065(0)
        Unknown11091(10)
        Unknown30068(1)
        clearUponHandler(12)

        def upon_STATE_END():
            SLOT_62 = 0
    sprite('jb400_11', 2)	# 1-2
    if SLOT_37:
        Unknown1045(80000)
        Unknown8007(100, 1, 0)
    else:
        Unknown1018()
        Unknown1019(50)
        physicsYImpulse(4000)
        setGravity(3000)
    sprite('jb403_00', 1)	# 3-3
    sprite('jb403_00', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('jb403_01', 1)	# 5-5
    sprite('jb403_02', 1)	# 6-6
    Unknown20(32767, 2, 36)
    if SLOT_36:
        Unknown1039(150)

        def upon_LANDING():
            sendToLabel(0)
    label(0)
    sprite('jb403_03', 1)	# 7-7
    Unknown8006(100, 1, 0)
    loopRest()
    gotoLabel(3)
    label(3)
    sprite('jb403_04', 1)	# 8-8
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    Unknown7007('626a623230345f30000000000000000064000000626a623230345f31000000000000000064000000626a623230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb403_05', 2)	# 9-10	 **attackbox here**
    Unknown1084(1)
    GFX_0('jbef403_zanzou', 100)
    GFX_0('jbef403_zanzou2', 100)
    sprite('jb403_06', 4)	# 11-14
    Recovery()
    sprite('jb403_07', 4)	# 15-18
    sprite('jb403_08', 4)	# 19-22
    sprite('jb403_09', 4)	# 23-26
    sprite('jb403_10', 4)	# 27-30
    sprite('jb403_11', 4)	# 31-34
    sprite('jb403_12', 4)	# 35-38

@State
def Rekkouzan_Mid_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Mid_Atk')
        Damage(1980)
        Unknown30065(0)
        Unknown11091(10)
        Unknown30068(1)
        PushbackX(5000)
        if SLOT_37:
            Unknown8006(100, 1, 0)
            Unknown8007(100, 1, 0)
        if SLOT_36:
            SLOT_61 = 1
            if (not SLOT_62):
                Unknown2016(100)
                Unknown23087(80000)

        def upon_STATE_END():
            SLOT_62 = 0
            Unknown2006()
        Unknown28(2, 'CmnActJumpLanding')
        Unknown22004(7, 1)
    sprite('jb400_11', 1)	# 1-1
    physicsXImpulse(20000)
    sprite('jb404_00', 1)	# 2-2
    sprite('jb404_01', 1)	# 3-3
    if SLOT_36:
        Unknown2016(-1)
        Unknown23087(-1)
        Unknown1007(-80000)
    if SLOT_37:
        Unknown8001(3, 100)
    Unknown1019(30)
    physicsYImpulse(23000)
    setGravity(1900)
    sprite('jb404_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('626a623230355f30000000000000000064000000626a623230355f31000000000000000064000000626a623230355f320000000000000000640000000000000000000000000000000000000000000000')
    loopRest()
    gotoLabel(1)
    label(1)
    sprite('jb404_02', 3)	# 5-7
    sprite('jb404_03', 3)	# 8-10
    sprite('jb404_04', 3)	# 11-13
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb404_05', 1)	# 14-14	 **attackbox here**
    GFX_0('jbef404_zanzou', 100)
    sprite('jb404_05', 3)	# 15-17	 **attackbox here**
    sprite('jb404_06', 2)	# 18-19
    Recovery()
    sprite('jb404_07', 2)	# 20-21
    sprite('jb404_08', 2)	# 22-23
    sprite('jb404_09', 2)	# 24-25
    sprite('jb404_13', 2)	# 26-27
    sprite('jb404_14', 2)	# 28-29

@State
def Shiranui_Hagane_236A():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()
        Unknown14083(0)

        def upon_3():
            if (SLOT_18 >= 3):
                Unknown23029(4, 5000, 0)
        clearUponHandler(2)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
            if (SLOT_48 == 5002):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown2006()
            Unknown3001(255)
    sprite('jb203_00', 3)	# 1-3
    Unknown23183('6a623235335f3030000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_01', 3)	# 4-6
    Unknown23183('6a623235335f3031000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1084(1)
    GFX_0('Shiranui_Hagane_236Aobj', 100)
    Unknown38(4, 1)
    tag_voice(1, 'bjb106_0', 'bjb105_2', 'bjb108_2', '')
    label(100)
    sprite('jb203_02', 3)	# 7-9
    Unknown23183('6a623230335f3032657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_03', 3)	# 10-12
    Unknown23183('6a623230335f3033657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_04', 3)	# 13-15
    Unknown23183('6a623230335f3034657830300000000000000000000000000000000000000000030000000200000024000000')
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb203_02', 300)	# 16-315
    clearUponHandler(3)
    Unknown2017(0)
    Unknown3001(0)
    SLOT_63 = 1

    def upon_3():
        if (SLOT_23 <= 1000):
            SLOT_23 = 1000
    setInvincible(1)
    loopRest()
    label(1)
    sprite('jb203_16', 4)	# 316-319	 **attackbox here**
    clearUponHandler(3)
    Unknown2017(1)
    GFX_0('jbef203_zanzou', 100)
    Unknown1019(5)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown3004(45)
    tag_voice(0, 'bjb106_1', 'bjb106_2', 'bjb107_1', '')
    Unknown14083(1)
    sprite('jb203_16', 2)	# 320-321	 **attackbox here**
    setInvincible(0)
    sprite('jb203_17', 4)	# 322-325
    sprite('jb203_18', 4)	# 326-329
    sprite('jb203_19', 3)	# 330-332

    def upon_LANDING():
        sendToLabel(2)
    sprite('jb020_05', 3)	# 333-335
    sprite('jb020_06', 3)	# 336-338
    label(3)
    sprite('jb020_07', 4)	# 339-342
    sprite('jb020_08', 4)	# 343-346
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('jb401_09', 5)	# 347-351
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 5)	# 352-356
    sprite('jb401_11', 5)	# 357-361

@State
def Shiranui_Hagane_236B():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()
        Unknown14083(0)

        def upon_3():
            if (SLOT_18 >= 3):
                Unknown23029(4, 5000, 0)
        clearUponHandler(2)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
            if (SLOT_48 == 5002):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown2006()
            Unknown3001(255)
    sprite('jb203_00', 3)	# 1-3
    Unknown23183('6a623235335f3030000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_01', 3)	# 4-6
    Unknown23183('6a623235335f3031000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1084(1)
    GFX_0('Shiranui_Hagane_236Bobj', 100)
    Unknown38(4, 1)
    tag_voice(1, 'bjb106_0', 'bjb105_2', 'bjb108_2', '')
    label(100)
    sprite('jb203_02', 3)	# 7-9
    Unknown23183('6a623230335f3032657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_03', 3)	# 10-12
    Unknown23183('6a623230335f3033657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_04', 3)	# 13-15
    Unknown23183('6a623230335f3034657830300000000000000000000000000000000000000000030000000200000024000000')
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb203_02', 300)	# 16-315
    clearUponHandler(3)
    Unknown2017(0)
    Unknown3001(0)
    SLOT_63 = 1

    def upon_3():
        if (SLOT_23 <= 1000):
            SLOT_23 = 1000
    setInvincible(1)
    loopRest()
    label(1)
    sprite('jb203_16', 4)	# 316-319	 **attackbox here**
    clearUponHandler(3)
    Unknown2017(1)
    GFX_0('jbef203_zanzou', 100)
    Unknown1019(5)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown3004(45)
    tag_voice(0, 'bjb106_1', 'bjb106_2', 'bjb107_1', '')
    Unknown14083(1)
    sprite('jb203_16', 2)	# 320-321	 **attackbox here**
    setInvincible(0)
    sprite('jb203_17', 4)	# 322-325
    sprite('jb203_18', 4)	# 326-329
    sprite('jb203_19', 3)	# 330-332

    def upon_LANDING():
        sendToLabel(2)
    sprite('jb020_05', 3)	# 333-335
    sprite('jb020_06', 3)	# 336-338
    label(3)
    sprite('jb020_07', 4)	# 339-342
    sprite('jb020_08', 4)	# 343-346
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('jb401_09', 5)	# 347-351
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 5)	# 352-356
    sprite('jb401_11', 5)	# 357-361

@State
def Shiranui_Hagane_236EX():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()
        Unknown14083(0)

        def upon_3():
            if (SLOT_18 >= 3):
                Unknown23029(4, 5000, 0)
        clearUponHandler(2)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
            if (SLOT_48 == 5002):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown2006()
            Unknown3001(255)
    sprite('jb203_00', 3)	# 1-3
    Unknown23183('6a623235335f3030000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    Unknown23183('6a623235335f3031000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1084(1)
    GFX_0('Shiranui_Hagane_236EXobj', 100)
    Unknown38(4, 1)
    tag_voice(1, 'bjb106_0', 'bjb105_2', 'bjb108_2', '')
    label(100)
    sprite('jb203_02', 3)	# 7-9
    Unknown23183('6a623230335f3032657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_03', 3)	# 10-12
    Unknown23183('6a623230335f3033657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_04', 3)	# 13-15
    Unknown23183('6a623230335f3034657830300000000000000000000000000000000000000000030000000200000024000000')
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb203_02', 300)	# 16-315
    clearUponHandler(3)
    Unknown2017(0)
    Unknown3001(0)
    SLOT_63 = 1

    def upon_3():
        if (SLOT_23 <= 1000):
            SLOT_23 = 1000
    setInvincible(1)
    loopRest()
    label(1)
    sprite('jb203_16', 4)	# 316-319	 **attackbox here**
    clearUponHandler(3)
    Unknown2017(1)
    GFX_0('jbef203_zanzou', 100)
    Unknown1019(5)
    physicsYImpulse(12000)
    Unknown1043()
    Unknown3004(45)
    tag_voice(0, 'bjb106_1', 'bjb106_2', 'bjb107_1', '')
    Unknown14083(1)
    sprite('jb203_16', 2)	# 320-321	 **attackbox here**
    setInvincible(0)
    sprite('jb203_17', 4)	# 322-325
    sprite('jb203_18', 4)	# 326-329
    sprite('jb203_19', 3)	# 330-332

    def upon_LANDING():
        sendToLabel(2)
    sprite('jb020_05', 3)	# 333-335
    sprite('jb020_06', 3)	# 336-338
    label(3)
    sprite('jb020_07', 4)	# 339-342
    sprite('jb020_08', 4)	# 343-346
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('jb401_09', 3)	# 347-349
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 3)	# 350-352
    sprite('jb401_11', 3)	# 353-355

@State
def Shiranui_Hagane_214A():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()
        Unknown14083(0)

        def upon_3():
            if (SLOT_18 >= 3):
                Unknown23029(4, 5000, 0)
        clearUponHandler(2)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
            if (SLOT_48 == 5002):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown2006()
            Unknown3001(255)
    sprite('jb203_00', 3)	# 1-3
    Unknown23183('6a623235335f3030000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_01', 3)	# 4-6
    Unknown23183('6a623235335f3031000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1084(1)
    GFX_0('Shiranui_Hagane_214Aobj', 100)
    Unknown38(4, 1)
    tag_voice(1, 'bjb106_0', 'bjb105_2', 'bjb108_2', '')
    label(100)
    sprite('jb203_02', 3)	# 7-9
    Unknown23183('6a623230335f3032657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_03', 3)	# 10-12
    Unknown23183('6a623230335f3033657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_04', 3)	# 13-15
    Unknown23183('6a623230335f3034657830300000000000000000000000000000000000000000030000000200000024000000')
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb203_02', 300)	# 16-315
    clearUponHandler(3)
    Unknown2017(0)
    Unknown3001(0)
    SLOT_63 = 1

    def upon_3():
        if (SLOT_23 <= 1000):
            SLOT_23 = 1000
    setInvincible(1)
    loopRest()
    label(1)
    sprite('jb203_16', 4)	# 316-319	 **attackbox here**
    clearUponHandler(3)
    Unknown2017(1)
    GFX_0('jbef203_zanzou', 100)
    Unknown1019(5)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown3004(45)
    tag_voice(0, 'bjb106_1', 'bjb106_2', 'bjb107_1', '')
    Unknown14083(1)
    sprite('jb203_16', 2)	# 320-321	 **attackbox here**
    setInvincible(0)
    sprite('jb203_17', 4)	# 322-325
    sprite('jb203_18', 4)	# 326-329
    sprite('jb203_19', 3)	# 330-332

    def upon_LANDING():
        sendToLabel(2)
    sprite('jb020_05', 3)	# 333-335
    sprite('jb020_06', 3)	# 336-338
    label(3)
    sprite('jb020_07', 4)	# 339-342
    sprite('jb020_08', 4)	# 343-346
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('jb401_09', 5)	# 347-351
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 5)	# 352-356
    sprite('jb401_11', 5)	# 357-361

@State
def Shiranui_Hagane_214B():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()
        Unknown14083(0)

        def upon_3():
            if (SLOT_18 >= 3):
                Unknown23029(4, 5000, 0)
        clearUponHandler(2)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
            if (SLOT_48 == 5002):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown2006()
            Unknown3001(255)
    sprite('jb203_00', 3)	# 1-3
    Unknown23183('6a623235335f3030000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_01', 3)	# 4-6
    Unknown23183('6a623235335f3031000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1084(1)
    GFX_0('Shiranui_Hagane_214Bobj', 100)
    Unknown38(4, 1)
    tag_voice(1, 'bjb106_0', 'bjb105_2', 'bjb108_2', '')
    label(100)
    sprite('jb203_02', 3)	# 7-9
    Unknown23183('6a623230335f3032657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_03', 3)	# 10-12
    Unknown23183('6a623230335f3033657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_04', 3)	# 13-15
    Unknown23183('6a623230335f3034657830300000000000000000000000000000000000000000030000000200000024000000')
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb203_02', 300)	# 16-315
    clearUponHandler(3)
    Unknown2017(0)
    Unknown3001(0)
    SLOT_63 = 1

    def upon_3():
        if (SLOT_23 <= 1000):
            SLOT_23 = 1000
    setInvincible(1)
    loopRest()
    label(1)
    sprite('jb203_16', 4)	# 316-319	 **attackbox here**
    clearUponHandler(3)
    Unknown2017(1)
    GFX_0('jbef203_zanzou', 100)
    Unknown1019(5)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown3004(45)
    tag_voice(0, 'bjb106_1', 'bjb106_2', 'bjb107_1', '')
    Unknown14083(1)
    sprite('jb203_16', 2)	# 320-321	 **attackbox here**
    setInvincible(0)
    sprite('jb203_17', 4)	# 322-325
    sprite('jb203_18', 4)	# 326-329
    sprite('jb203_19', 3)	# 330-332

    def upon_LANDING():
        sendToLabel(2)
    sprite('jb020_05', 3)	# 333-335
    sprite('jb020_06', 3)	# 336-338
    label(3)
    sprite('jb020_07', 4)	# 339-342
    sprite('jb020_08', 4)	# 343-346
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('jb401_09', 5)	# 347-351
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 5)	# 352-356
    sprite('jb401_11', 5)	# 357-361

@State
def Shiranui_Hagane_214EX():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()
        Unknown14083(0)

        def upon_3():
            if (SLOT_18 >= 3):
                Unknown23029(4, 5000, 0)
        clearUponHandler(2)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
            if (SLOT_48 == 5002):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown2006()
            Unknown3001(255)
    sprite('jb203_00', 3)	# 1-3
    Unknown23183('6a623235335f3030000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    Unknown23183('6a623235335f3031000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1084(1)
    GFX_0('Shiranui_Hagane_214EXobj', 100)
    Unknown38(4, 1)
    tag_voice(1, 'bjb106_0', 'bjb105_2', 'bjb108_2', '')
    label(100)
    sprite('jb203_02', 3)	# 7-9
    Unknown23183('6a623230335f3032657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_03', 3)	# 10-12
    Unknown23183('6a623230335f3033657830300000000000000000000000000000000000000000030000000200000024000000')
    sprite('jb203_04', 3)	# 13-15
    Unknown23183('6a623230335f3034657830300000000000000000000000000000000000000000030000000200000024000000')
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('jb203_02', 300)	# 16-315
    clearUponHandler(3)
    Unknown2017(0)
    Unknown3001(0)
    SLOT_63 = 1

    def upon_3():
        if (SLOT_23 <= 1000):
            SLOT_23 = 1000
    setInvincible(1)
    loopRest()
    label(1)
    sprite('jb203_16', 4)	# 316-319	 **attackbox here**
    clearUponHandler(3)
    Unknown2017(1)
    GFX_0('jbef203_zanzou', 100)
    Unknown1019(5)
    physicsYImpulse(12000)
    Unknown1043()
    Unknown3004(45)
    tag_voice(0, 'bjb106_1', 'bjb106_2', 'bjb107_1', '')
    Unknown14083(1)
    sprite('jb203_16', 2)	# 320-321	 **attackbox here**
    setInvincible(0)
    sprite('jb203_17', 4)	# 322-325
    sprite('jb203_18', 4)	# 326-329
    sprite('jb203_19', 3)	# 330-332

    def upon_LANDING():
        sendToLabel(2)
    sprite('jb020_05', 3)	# 333-335
    sprite('jb020_06', 3)	# 336-338
    label(3)
    sprite('jb020_07', 4)	# 339-342
    sprite('jb020_08', 4)	# 343-346
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('jb401_09', 3)	# 347-349
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('jb401_10', 3)	# 350-352
    sprite('jb401_11', 3)	# 353-355

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1250)
        AttackP2(100)
        Unknown11091(25)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        PushbackX(0)
        Hitstop(2)
        Unknown11056(0)
        Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11064(1)

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
            Unknown1086(22)
            teleportRelativeY(0)
            Unknown3001(0)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('jb431_00', 5)	# 1-5
    Unknown1084(1)
    setInvincible(1)
    sprite('jb431_01', 3)	# 6-8
    sprite('jb431_02', 3)	# 9-11
    sprite('jb431_03', 3)	# 12-14
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('jb431_04', 3)	# 15-17
    sprite('jb431_05', 3)	# 18-20
    sprite('jb431_06', 3)	# 21-23
    sprite('jb431_04', 3)	# 24-26
    sprite('jb431_05', 3)	# 27-29
    sprite('jb431_06', 3)	# 30-32
    sprite('jb431_04', 3)	# 33-35
    sprite('jb431_05', 3)	# 36-38
    sprite('jb431_06', 3)	# 39-41
    sprite('jb431_04', 3)	# 42-44
    sprite('jb431_05', 3)	# 45-47
    loopRest()
    sprite('jb431_07', 3)	# 48-50
    physicsXImpulse(20000)
    tag_voice(1, 'bjb252_0', 'bjb252_1', '', '')
    sprite('jb431_08', 2)	# 51-52
    Unknown1019(200)
    Unknown3004(-20)
    sprite('jb431_09', 12)	# 53-64	 **attackbox here**
    GFX_0('jb431_SlashEff', -1)
    GFX_0('jb431_CircleShockEff', -1)
    Unknown1019(200)
    Unknown2017(0)
    Unknown2015(40)
    SFX_3('jbse_00')
    sprite('jb431_23', 3)	# 65-67
    clearUponHandler(12)
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    physicsXImpulse(20000)
    setInvincible(0)
    sprite('jb431_24', 3)	# 68-70
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_25', 3)	# 71-73
    sprite('jb431_26', 3)	# 74-76
    sprite('jb431_24', 3)	# 77-79
    sprite('jb431_25', 3)	# 80-82
    sprite('jb431_26', 3)	# 83-85
    sprite('jb431_27', 3)	# 86-88
    sprite('jb340_12ex00', 3)	# 89-91
    sprite('jb340_13ex00', 3)	# 92-94
    sprite('jb340_14ex00', 3)	# 95-97
    sprite('jb340_15ex00', 3)	# 98-100
    sprite('jb340_16ex00', 3)	# 101-103
    ExitState()
    label(1)
    sprite('jb431_09', 10)	# 104-113	 **attackbox here**
    RefreshMultihit()
    Unknown30048(1)
    Hitstop(0)
    Unknown11023(1)
    Unknown11066(1)
    Unknown9154(60)
    Unknown11069('UltimateAssault')
    physicsXImpulse(50000)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('jb431_10', 5)	# 114-118
    GFX_0('jb431_SlashEndEff', -1)
    Unknown3004(20)
    Unknown3001(128)
    physicsXImpulse(20000)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('jb431_10', 15)	# 119-133
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_11', 3)	# 134-136
    sprite('jb431_12', 3)	# 137-139
    sprite('jb431_13', 3)	# 140-142
    sprite('jb431_14', 3)	# 143-145	 **attackbox here**
    RefreshMultihit()
    Damage(4000)
    AttackP2(60)
    Unknown9155()
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9130(30)
    Unknown9142(60)
    Unknown9132(30)
    Unknown9144(60)
    Unknown9016(1)
    Unknown11050('040000006a6265665f6472697665736c6173685f73756d69000000000000000000000000')
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)

    def upon_78():
        Unknown13024(1)
    tag_voice(0, 'bjb253_0', 'bjb253_1', '', '')
    sprite('jb431_15', 3)	# 146-148	 **attackbox here**
    sprite('jb431_16', 3)	# 149-151	 **attackbox here**
    sprite('jb431_17', 3)	# 152-154	 **attackbox here**
    sprite('jb431_15', 3)	# 155-157	 **attackbox here**
    sprite('jb431_16', 3)	# 158-160	 **attackbox here**
    sprite('jb431_17', 3)	# 161-163	 **attackbox here**
    sprite('jb431_15', 3)	# 164-166	 **attackbox here**
    sprite('jb431_16', 3)	# 167-169	 **attackbox here**
    sprite('jb431_17', 3)	# 170-172	 **attackbox here**
    sprite('jb431_15', 3)	# 173-175	 **attackbox here**
    sprite('jb431_16', 3)	# 176-178	 **attackbox here**
    sprite('jb431_17', 3)	# 179-181	 **attackbox here**
    sprite('jb431_18', 5)	# 182-186
    sprite('jb431_19', 5)	# 187-191
    sprite('jb431_20', 5)	# 192-196
    sprite('jb431_21', 5)	# 197-201
    sprite('jb431_22', 4)	# 202-205

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1250)
        AttackP2(100)
        Unknown11091(25)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        PushbackX(0)
        Hitstop(2)
        Unknown11056(0)
        Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11064(1)

        def upon_78():
            clearUponHandler(78)
            Unknown1086(22)
            teleportRelativeY(0)
            Unknown3001(0)
            Unknown13024(0)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('jb431_00', 5)	# 1-5
    Unknown1084(1)
    setInvincible(1)
    sprite('jb431_01', 3)	# 6-8
    sprite('jb431_02', 3)	# 9-11
    sprite('jb431_03', 3)	# 12-14
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('jb431_04', 3)	# 15-17
    sprite('jb431_05', 3)	# 18-20
    sprite('jb431_06', 3)	# 21-23
    sprite('jb431_04', 3)	# 24-26
    sprite('jb431_05', 3)	# 27-29
    sprite('jb431_06', 3)	# 30-32
    sprite('jb431_04', 3)	# 33-35
    sprite('jb431_05', 3)	# 36-38
    sprite('jb431_06', 3)	# 39-41
    sprite('jb431_04', 3)	# 42-44
    sprite('jb431_05', 3)	# 45-47
    sprite('jb431_07', 3)	# 48-50
    physicsXImpulse(20000)
    tag_voice(1, 'bjb252_0', 'bjb252_1', '', '')
    sprite('jb431_08', 2)	# 51-52
    Unknown1019(200)
    Unknown3004(-20)
    sprite('jb431_09', 12)	# 53-64	 **attackbox here**
    GFX_0('jb431_SlashEff', -1)
    GFX_0('jb431_CircleShockEff', -1)
    Unknown1019(200)
    Unknown2017(0)
    Unknown2015(40)
    SFX_3('jbse_00')
    sprite('jb431_23', 3)	# 65-67
    clearUponHandler(78)
    Unknown3004(20)
    Unknown3001(128)
    Unknown2017(1)
    Unknown2015(-1)
    physicsXImpulse(20000)
    setInvincible(0)
    sprite('jb431_24', 3)	# 68-70
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_25', 3)	# 71-73
    sprite('jb431_26', 3)	# 74-76
    sprite('jb431_24', 3)	# 77-79
    sprite('jb431_25', 3)	# 80-82
    sprite('jb431_26', 3)	# 83-85
    sprite('jb431_27', 3)	# 86-88
    sprite('jb340_12ex00', 3)	# 89-91
    sprite('jb340_13ex00', 3)	# 92-94
    sprite('jb340_14ex00', 3)	# 95-97
    sprite('jb340_15ex00', 3)	# 98-100
    sprite('jb340_16ex00', 3)	# 101-103
    ExitState()
    label(1)
    sprite('jb431_09', 10)	# 104-113	 **attackbox here**
    RefreshMultihit()
    Unknown30048(1)
    Hitstop(0)
    Unknown11023(1)
    Unknown11066(1)
    Unknown9154(60)
    Unknown11069('UltimateAssault_OD')
    physicsXImpulse(50000)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('jb431_10', 5)	# 114-118
    GFX_0('jb431OD_SlashEffMatome', 100)
    Unknown3004(20)
    Unknown3001(128)
    physicsXImpulse(20000)
    Unknown2017(1)
    Unknown2015(-1)
    sprite('jb431_10', 15)	# 119-133
    Unknown1084(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('jb431_11', 3)	# 134-136
    sprite('jb431_12', 3)	# 137-139
    sprite('jb431_13', 3)	# 140-142
    sprite('jb431_14', 3)	# 143-145	 **attackbox here**
    RefreshMultihit()
    Damage(650)
    Unknown9155()
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9130(30)
    Unknown9142(60)
    Unknown9132(30)
    Unknown9144(60)
    Unknown11057(600)
    Unknown9016(1)
    Unknown11050('040000006a6265665f6472697665736c6173685f73756d69000000000000000000000000')
    Unknown21015('6a623433314f445f536c6173684566664d61746f6d6500000000000000000000d610000000000000')
    sprite('jb431_15', 3)	# 146-148	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_16', 3)	# 149-151	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_17', 3)	# 152-154	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_15', 3)	# 155-157	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_16', 3)	# 158-160	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_17', 3)	# 161-163	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_15', 3)	# 164-166	 **attackbox here**
    RefreshMultihit()
    sprite('jb431_16', 3)	# 167-169	 **attackbox here**
    RefreshMultihit()
    Unknown11057(1000)
    AttackP2(60)
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)

    def upon_78():
        Unknown13024(1)
    tag_voice(0, 'bjb253_0', 'bjb253_1', '', '')
    sprite('jb431_17', 3)	# 170-172	 **attackbox here**
    sprite('jb431_15', 3)	# 173-175	 **attackbox here**
    sprite('jb431_16', 3)	# 176-178	 **attackbox here**
    sprite('jb431_17', 3)	# 179-181	 **attackbox here**
    sprite('jb431_15', 3)	# 182-184	 **attackbox here**
    sprite('jb431_16', 3)	# 185-187	 **attackbox here**
    sprite('jb431_17', 3)	# 188-190	 **attackbox here**
    sprite('jb431_15', 3)	# 191-193	 **attackbox here**
    sprite('jb431_16', 3)	# 194-196	 **attackbox here**
    sprite('jb431_17', 3)	# 197-199	 **attackbox here**
    sprite('jb431_15', 3)	# 200-202	 **attackbox here**
    sprite('jb431_16', 3)	# 203-205	 **attackbox here**
    sprite('jb431_18', 5)	# 206-210
    sprite('jb431_19', 5)	# 211-215
    sprite('jb431_20', 5)	# 216-220
    sprite('jb431_21', 5)	# 221-225
    sprite('jb431_22', 4)	# 226-229

@State
def UltimateAirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1000)
        AttackP2(100)
        Unknown11091(25)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(11)
        Unknown11072(1, 110000, -30000)
        AirPushbackX(0)
        AirPushbackY(-80000)
        Unknown9190(1)
        Unknown9130(100)
        Unknown9142(100)
        AirUntechableTime(100)
        PushbackX(0)
        Hitstop(1)
        Unknown11056(0)
        Unknown11064(1)
        clearUponHandler(2)

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
            SLOT_51 = 1

        def upon_3():
            if SLOT_51:
                clearUponHandler(3)
                Damage(100)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('jb430_00', 3)	# 1-3
    setInvincible(1)
    Unknown1084(1)
    setGravity(-50)
    sprite('jb430_01', 3)	# 4-6
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('jb430_02', 3)	# 7-9
    sprite('jb430_03', 3)	# 10-12
    sprite('jb430_01', 3)	# 13-15
    sprite('jb430_02', 3)	# 16-18
    sprite('jb430_03', 3)	# 19-21
    sprite('jb430_04', 3)	# 22-24
    tag_voice(1, 'bjb250_0', 'bjb250_1', '', '')
    physicsYImpulse(5000)
    setGravity(500)
    SFX_0('000_airdash_0')
    sprite('jb430_05', 3)	# 25-27
    sprite('jb430_06', 3)	# 28-30
    sprite('jb430_07', 3)	# 31-33
    sprite('jb430_08', 3)	# 34-36
    sprite('jb430_09', 3)	# 37-39
    sprite('jb430_10', 3)	# 40-42
    SFX_3('jbse_01')
    sprite('jb430_11', 3)	# 43-45
    sprite('jb430_12', 3)	# 46-48	 **attackbox here**
    physicsYImpulse(-80000)
    setGravity(0)
    sendToLabelUpon(2, 1)
    label(9)
    sprite('jb430_12', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('jb430_12', 1)	# 52-52	 **attackbox here**
    Unknown23027()
    Unknown2015(-1)
    if SLOT_51:
        _gotolabel(2)
    sprite('jb430_13', 3)	# 53-55
    setInvincible(0)
    sprite('jb430_14', 3)	# 56-58	 **attackbox here**
    sprite('jb430_15', 3)	# 59-61	 **attackbox here**
    sprite('jb430_16', 3)	# 62-64	 **attackbox here**
    sprite('jb430_17', 4)	# 65-68
    sprite('jb430_18', 4)	# 69-72
    sprite('jb430_19', 4)	# 73-76
    sprite('jb430_20', 4)	# 77-80
    sprite('jb430_21', 4)	# 81-84
    sprite('jb430_22', 4)	# 85-88
    sprite('jb430_23', 4)	# 89-92
    ExitState()
    label(2)
    sprite('jb430_12ex', 3)	# 93-95	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(2)
    Unknown11072(0, 0, 0)
    Unknown9190(0)
    Hitstop(0)
    Unknown11066(1)
    Unknown11069('UltimateAirAssault')
    GFX_0('jb430_slashMatome', 100)
    sprite('jb430_13', 3)	# 96-98
    sprite('jb430_14', 3)	# 99-101	 **attackbox here**
    sprite('jb430_15', 3)	# 102-104	 **attackbox here**
    sprite('jb430_16', 3)	# 105-107	 **attackbox here**
    sprite('jb430_14', 3)	# 108-110	 **attackbox here**
    RefreshMultihit()
    Damage(5000)
    AttackP2(60)
    Hitstop(20)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(15000)
    AirPushbackY(40000)
    Unknown9016(1)
    Unknown11050('040000006a6265665f6472697665736c6173685f73756d69000000000000000000000000')
    Unknown11064(0)
    Unknown11069('')
    Unknown13024(1)
    SFX_0('025_cleanhit_slash')
    tag_voice(0, 'bjb251_0', 'bjb251_1', '', '')
    sprite('jb430_15', 3)	# 111-113	 **attackbox here**
    sprite('jb430_16', 3)	# 114-116	 **attackbox here**
    sprite('jb430_14', 3)	# 117-119	 **attackbox here**
    sprite('jb430_15', 3)	# 120-122	 **attackbox here**
    sprite('jb430_16', 3)	# 123-125	 **attackbox here**
    sprite('jb430_14', 3)	# 126-128	 **attackbox here**
    sprite('jb430_15', 3)	# 129-131	 **attackbox here**
    sprite('jb430_16', 3)	# 132-134	 **attackbox here**
    sprite('jb430_14', 3)	# 135-137	 **attackbox here**
    sprite('jb430_15', 3)	# 138-140	 **attackbox here**
    sprite('jb430_16', 3)	# 141-143	 **attackbox here**
    sprite('jb430_17', 4)	# 144-147
    sprite('jb430_18', 4)	# 148-151
    sprite('jb430_19', 4)	# 152-155
    sprite('jb430_20', 4)	# 156-159
    sprite('jb430_21', 4)	# 160-163
    sprite('jb430_22', 4)	# 164-167
    sprite('jb430_23', 4)	# 168-171

@State
def UltimateAirAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1000)
        AttackP2(100)
        Unknown11091(25)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(11)
        Unknown11072(1, 110000, -30000)
        AirPushbackX(0)
        AirPushbackY(-80000)
        Unknown9190(1)
        Unknown9130(100)
        Unknown9142(100)
        AirUntechableTime(100)
        PushbackX(0)
        Hitstop(1)
        Unknown11056(0)
        Unknown11064(1)
        clearUponHandler(2)

        def upon_78():
            clearUponHandler(78)
            SLOT_51 = 1
            Unknown13024(0)

        def upon_3():
            if SLOT_51:
                clearUponHandler(3)
                Damage(100)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('jb430_00', 3)	# 1-3
    setInvincible(1)
    Unknown1084(1)
    setGravity(-50)
    sprite('jb430_01', 3)	# 4-6
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('jb430_02', 3)	# 7-9
    sprite('jb430_03', 3)	# 10-12
    sprite('jb430_01', 3)	# 13-15
    sprite('jb430_02', 3)	# 16-18
    sprite('jb430_03', 3)	# 19-21
    sprite('jb430_04', 3)	# 22-24
    tag_voice(1, 'bjb250_0', 'bjb250_1', '', '')
    physicsYImpulse(5000)
    setGravity(500)
    SFX_0('000_airdash_0')
    sprite('jb430_05', 3)	# 25-27
    sprite('jb430_06', 3)	# 28-30
    sprite('jb430_07', 3)	# 31-33
    sprite('jb430_08', 3)	# 34-36
    sprite('jb430_09', 3)	# 37-39
    sprite('jb430_10', 3)	# 40-42
    SFX_3('jbse_01')
    sprite('jb430_11', 3)	# 43-45
    sprite('jb430_12', 3)	# 46-48	 **attackbox here**
    physicsYImpulse(-80000)
    setGravity(0)
    sendToLabelUpon(2, 1)
    label(9)
    sprite('jb430_12', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('jb430_12', 1)	# 52-52	 **attackbox here**
    Unknown23027()
    Unknown2015(-1)
    if SLOT_51:
        _gotolabel(2)
    sprite('jb430_13', 3)	# 53-55
    setInvincible(0)
    sprite('jb430_14', 3)	# 56-58	 **attackbox here**
    sprite('jb430_15', 3)	# 59-61	 **attackbox here**
    sprite('jb430_16', 3)	# 62-64	 **attackbox here**
    sprite('jb430_17', 4)	# 65-68
    sprite('jb430_18', 4)	# 69-72
    sprite('jb430_19', 4)	# 73-76
    sprite('jb430_20', 4)	# 77-80
    sprite('jb430_21', 4)	# 81-84
    sprite('jb430_22', 4)	# 85-88
    sprite('jb430_23', 4)	# 89-92
    ExitState()
    label(2)
    sprite('jb430_13', 3)	# 93-95
    RefreshMultihit()
    AirHitstunAnimation(2)
    Unknown11072(0, 0, 0)
    Unknown9190(0)
    Hitstop(0)
    Unknown11066(1)
    Unknown11069('UltimateAirAssault_OD')
    GFX_0('jb430_slashMatome', 100)
    sprite('jb430_14', 3)	# 96-98	 **attackbox here**
    sprite('jb430_15', 3)	# 99-101	 **attackbox here**
    sprite('jb430_16', 3)	# 102-104	 **attackbox here**
    sprite('jb430_14', 3)	# 105-107	 **attackbox here**
    sprite('jb430_15', 3)	# 108-110	 **attackbox here**
    sprite('jb430_16', 3)	# 111-113	 **attackbox here**
    sprite('jb430_14', 3)	# 114-116	 **attackbox here**
    sprite('jb430_15', 3)	# 117-119	 **attackbox here**
    sprite('jb430_16', 3)	# 120-122	 **attackbox here**
    sprite('jb430_24', 3)	# 123-125	 **attackbox here**
    RefreshMultihit()
    Damage(1600)
    AttackP2(90)
    Unknown11091(20)
    Hitstop(0)
    Unknown11001(3, 3, 3)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(15000)
    AirPushbackY(40000)
    Unknown9016(1)
    Unknown11050('040000006a6265665f6472697665736c6173685f73756d69000000000000000000000000')
    GFX_0('jb430_ODSlash00', 100)
    SFX_0('025_cleanhit_slash')
    tag_voice(0, 'bjb251_0', 'bjb251_1', '', '')
    sprite('jb430_24', 3)	# 126-128	 **attackbox here**
    RefreshMultihit()
    sprite('jb430_25', 3)	# 129-131	 **attackbox here**
    RefreshMultihit()
    sprite('jb430_25', 3)	# 132-134	 **attackbox here**
    RefreshMultihit()
    sprite('jb403_05ex00', 4)	# 135-138	 **attackbox here**
    RefreshMultihit()
    Hitstop(20)
    Unknown11001(0, 0, 0)
    Unknown11064(0)
    Unknown11069('')
    Unknown13024(1)
    SFX_3('jbse_03')
    SFX_3('jbse_09')
    sprite('jb403_06ex00', 4)	# 139-142
    sprite('jb403_07ex00', 30)	# 143-172
    sprite('jb403_08ex00', 6)	# 173-178
    sprite('jb403_09ex00', 6)	# 179-184
    sprite('jb403_10ex00', 6)	# 185-190
    sprite('jb403_11ex00', 6)	# 191-196
    sprite('jb403_12ex00', 2)	# 197-198

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11069('AstralHeat')
        AttackLevel_(5)
        Damage(0)
        Unknown11091(100)
        Hitstop(3)
        Unknown11072(1, 180000, 0)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        PushbackX(60000)
        Unknown9154(999)
        AirUntechableTime(999)
        Unknown9130(999)
        Unknown9142(999)
        Unknown11066(1)
        Unknown11064(1)
        Unknown11056(0)

        def upon_12():
            clearUponHandler(12)
            GFX_0('Astral_Camera', -1)
            Unknown23088(1, 1)
            Unknown23157(1)
            Unknown11067(1)
            Unknown2017(0)
            Unknown2053(0)
            Unknown2034(0)
            Unknown23084(1)
            Unknown1028(0)
            physicsXImpulse(0)
            SLOT_31 = 0
            SLOT_32 = 0
            sendToLabel(1)
    sprite('jb450_00', 3)	# 1-3
    setInvincible(1)
    Unknown1084(1)
    sprite('jb450_01', 3)	# 4-6
    Unknown2036(35, -1, 2)
    Unknown23147()
    GFX_0('EMB_JB_AH', -1)
    sprite('jb450_02', 3)	# 7-9
    sprite('jb450_03', 3)	# 10-12
    sprite('jb450_04', 3)	# 13-15
    sprite('jb450_05', 3)	# 16-18
    sprite('jb450_03', 3)	# 19-21
    sprite('jb450_04', 3)	# 22-24
    sprite('jb450_05', 3)	# 25-27
    sprite('jb450_03', 3)	# 28-30
    sprite('jb450_04', 3)	# 31-33
    sprite('jb450_05', 3)	# 34-36
    sprite('jb450_03', 3)	# 37-39
    sprite('jb450_04', 3)	# 40-42
    sprite('jb450_05', 3)	# 43-45
    sprite('jb450_06', 3)	# 46-48	 **attackbox here**
    GFX_0('jb450_AtkAura', -1)
    SFX_0('022_magiccircle_b')
    sprite('jb450_07', 3)	# 49-51
    setInvincible(0)
    sprite('jb450_08', 3)	# 52-54
    sprite('jb450_09', 3)	# 55-57
    sprite('jb450_07', 4)	# 58-61
    sprite('jb450_08', 4)	# 62-65
    sprite('jb450_09', 4)	# 66-69
    sprite('jb450_07', 5)	# 70-74
    sprite('jb450_08', 5)	# 75-79
    sprite('jb450_09', 5)	# 80-84
    sprite('jb450_39', 6)	# 85-90
    sprite('jb450_40', 6)	# 91-96
    sprite('jb450_41', 14)	# 97-110
    Unknown21015('6a623435305f41746b41757261000000000000000000000000000000000000009313000000000000')
    sprite('jb321_13ex00', 7)	# 111-117
    sprite('jb321_14ex00', 7)	# 118-124
    sprite('jb321_15ex00', 7)	# 125-131
    ExitState()
    label(1)
    sprite('keep', 2)	# 132-133
    Unknown11056(1)
    sprite('jb450_07', 3)	# 134-136
    sprite('jb450_08', 3)	# 137-139
    sprite('jb450_09', 3)	# 140-142
    sprite('jb450_07', 3)	# 143-145
    sprite('jb450_08', 3)	# 146-148
    sprite('jb450_09', 3)	# 149-151
    sprite('jb450_07', 3)	# 152-154
    sprite('jb450_08', 3)	# 155-157
    sprite('jb450_09', 3)	# 158-160
    sprite('jb450_07', 3)	# 161-163
    sprite('jb450_08', 3)	# 164-166
    sprite('jb450_09', 3)	# 167-169
    sprite('jb450_10', 3)	# 170-172
    sprite('jb450_11', 3)	# 173-175
    Unknown21015('6a623435305f41746b41757261000000000000000000000000000000000000009313000000000000')
    GFX_0('jb450_kaihouAura', -1)
    SFX_3('jbse_05')
    tag_voice(1, 'bjb290_0', 'bjb290_1', '', '')
    sprite('jb450_12', 3)	# 176-178	 **attackbox here**
    sprite('jb450_13', 3)	# 179-181	 **attackbox here**
    sprite('jb450_14', 8)	# 182-189	 **attackbox here**
    GFX_0('jb450_kidou', -1)
    Unknown3029(1)
    Unknown3070(5)
    sprite('jb450_15', 8)	# 190-197	 **attackbox here**
    sprite('jb450_16', 8)	# 198-205	 **attackbox here**
    GFX_0('jb450_kidou2', -1)
    sprite('jb450_17', 8)	# 206-213	 **attackbox here**
    sprite('jb450_18', 3)	# 214-216	 **attackbox here**
    Unknown3029(0)
    sprite('jb450_19', 3)	# 217-219	 **attackbox here**
    sprite('jb450_17', 3)	# 220-222	 **attackbox here**
    sprite('jb450_18', 3)	# 223-225	 **attackbox here**
    sprite('jb450_19', 3)	# 226-228	 **attackbox here**
    sprite('jb450_17', 3)	# 229-231	 **attackbox here**
    sprite('jb450_18', 3)	# 232-234	 **attackbox here**
    sprite('jb450_19', 3)	# 235-237	 **attackbox here**
    sprite('jb450_17', 3)	# 238-240	 **attackbox here**
    sprite('jb450_18', 3)	# 241-243	 **attackbox here**
    sprite('jb450_19', 3)	# 244-246	 **attackbox here**
    sprite('jb450_17', 3)	# 247-249	 **attackbox here**
    sprite('jb450_18', 3)	# 250-252	 **attackbox here**
    sprite('jb450_19', 3)	# 253-255	 **attackbox here**
    tag_voice(0, 'bjb291_0', 'bjb291_1', '', '')
    Unknown21015('41737472616c5f43616d657261000000000000000000000000000000000000008813000000000000')
    GFX_0('jbef_450flash', -1)
    GFX_0('jbef_450weakpointBG', -1)
    sprite('jb450_17', 3)	# 256-258	 **attackbox here**
    sprite('jb450_18', 3)	# 259-261	 **attackbox here**
    sprite('jb450_19', 3)	# 262-264	 **attackbox here**
    sprite('jb450_17', 3)	# 265-267	 **attackbox here**
    sprite('jb450_18', 3)	# 268-270	 **attackbox here**
    sprite('jb450_19', 3)	# 271-273	 **attackbox here**
    sprite('jb450_17', 3)	# 274-276	 **attackbox here**
    sprite('jb450_18', 3)	# 277-279	 **attackbox here**
    sprite('jb450_19', 3)	# 280-282	 **attackbox here**
    sprite('jb450_17', 3)	# 283-285	 **attackbox here**
    sprite('jb450_18', 3)	# 286-288	 **attackbox here**
    sprite('jb450_19', 3)	# 289-291	 **attackbox here**
    sprite('jb450_17', 3)	# 292-294	 **attackbox here**
    sprite('jb450_18', 3)	# 295-297	 **attackbox here**
    sprite('jb450_19', 3)	# 298-300	 **attackbox here**
    sprite('jb450_17', 3)	# 301-303	 **attackbox here**
    sprite('jb450_18', 3)	# 304-306	 **attackbox here**
    sprite('jb450_19', 3)	# 307-309	 **attackbox here**
    sprite('jb450_17', 3)	# 310-312	 **attackbox here**
    sprite('jb450_18', 3)	# 313-315	 **attackbox here**
    sprite('jb450_19', 3)	# 316-318	 **attackbox here**
    sprite('jb450_17', 3)	# 319-321	 **attackbox here**
    sprite('jb450_18', 3)	# 322-324	 **attackbox here**
    sprite('jb450_19', 3)	# 325-327	 **attackbox here**
    sprite('jb450_17', 3)	# 328-330	 **attackbox here**
    sprite('jb450_18', 3)	# 331-333	 **attackbox here**
    sprite('jb450_19', 3)	# 334-336	 **attackbox here**
    sprite('jb450_17', 3)	# 337-339	 **attackbox here**
    sprite('jb450_18', 3)	# 340-342	 **attackbox here**
    sprite('jb450_19', 3)	# 343-345	 **attackbox here**
    sprite('jb450_17', 3)	# 346-348	 **attackbox here**
    sprite('jb450_18', 3)	# 349-351	 **attackbox here**
    sprite('jb450_19', 3)	# 352-354	 **attackbox here**
    sprite('jb450_17', 3)	# 355-357	 **attackbox here**
    Unknown21015('41737472616c5f43616d657261000000000000000000000000000000000000008913000000000000')
    Unknown21015('6a6265665f3435307765616b706f696e744247000000000000000000000000009413000000000000')
    Unknown21015('6a6265665f3435307765616b706f696e740000000000000000000000000000009413000000000000')
    Unknown21015('6a6265665f3435307765616b706f696e745f546572756d6900000000000000009413000000000000')
    sprite('jb450_18', 3)	# 358-360	 **attackbox here**
    sprite('jb450_19', 3)	# 361-363	 **attackbox here**
    sprite('jb450_17', 3)	# 364-366	 **attackbox here**
    sprite('jb450_18', 3)	# 367-369	 **attackbox here**
    sprite('jb450_19', 3)	# 370-372	 **attackbox here**
    sprite('jb450_17', 3)	# 373-375	 **attackbox here**
    sprite('jb450_18', 3)	# 376-378	 **attackbox here**
    sprite('jb450_19', 3)	# 379-381	 **attackbox here**
    sprite('jb450_17', 3)	# 382-384	 **attackbox here**
    sprite('jb450_18', 3)	# 385-387	 **attackbox here**
    sprite('jb450_19', 3)	# 388-390	 **attackbox here**
    sprite('jb450_20', 4)	# 391-394	 **attackbox here**
    sprite('jb450_21', 4)	# 395-398	 **attackbox here**
    sprite('jb450_22', 4)	# 399-402	 **attackbox here**
    sprite('jb450_23', 8)	# 403-410	 **attackbox here**
    sprite('jb450_24', 3)	# 411-413	 **attackbox here**
    SFX_0('000_airdash_0')
    SFX_3('jbse_00')
    sprite('jb450_25', 3)	# 414-416	 **attackbox here**
    tag_voice(0, 'bjb292_0', 'bjb292_1', '', '')
    sprite('jb450_25', 4)	# 417-420	 **attackbox here**
    GFX_1('jbef_450issen', 103)
    GFX_0('jb450_ZanEff', -1)
    Unknown3001(0)
    Unknown1072(340000)
    Unknown1110(110000, 0)
    GFX_0('jb450_BG', -1)
    sprite('jb450_25', 8)	# 421-428	 **attackbox here**
    AttackLevel_(3)
    Damage(4300)
    Hitstop(0)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(0)
    AirPushbackY(1)
    YImpluseBeforeWallbounce(0)
    Unknown11067(1)
    Unknown9016(1)
    RefreshMultihit()

    def upon_3():
        Unknown36(22)
        Unknown1086(22)
        teleportRelativeX(-150000)
        Unknown1007(-100000)
        Unknown35()
    sprite('jb450_25', 10)	# 429-438	 **attackbox here**
    Unknown1084(1)
    sprite('jb450_25', 4)	# 439-442	 **attackbox here**
    GFX_0('jb450_ZanEff', -1)
    Unknown1072(55000)
    Unknown1110(100000, 0)
    RefreshMultihit()

    def upon_3():
        Unknown36(22)
        Unknown1086(22)
        teleportRelativeX(-250000)
        Unknown1007(-400000)
        Unknown35()
    sprite('jb450_25', 7)	# 443-449	 **attackbox here**
    Unknown1084(1)
    sprite('jb450_25', 5)	# 450-454	 **attackbox here**
    GFX_0('jb450_ZanEff', -1)
    Unknown1072(325000)
    Unknown1110(110000, 0)
    RefreshMultihit()

    def upon_3():
        Unknown36(22)
        Unknown1086(22)
        teleportRelativeX(-150000)
        Unknown1007(-50000)
        Unknown35()
    sprite('jb450_25', 3)	# 455-457	 **attackbox here**
    GFX_0('jb450_ZanEff', -1)
    Unknown1072(60000)
    Unknown1110(110000, 0)
    RefreshMultihit()

    def upon_3():
        Unknown36(22)
        Unknown1086(22)
        Unknown3001(0)
        teleportRelativeX(-250000)
        Unknown1007(-400000)
        Unknown35()
    sprite('jb450_25', 6)	# 458-463	 **attackbox here**
    GFX_0('jb450_ZanEff', -1)
    Unknown1072(325000)
    Unknown1110(110000, 0)
    RefreshMultihit()

    def upon_3():
        Unknown36(22)
        Unknown1086(22)
        teleportRelativeX(-150000)
        Unknown1007(-50000)
        Unknown35()
    sprite('jb450_25', 5)	# 464-468	 **attackbox here**
    GFX_0('jb450_ZanEff', -1)
    Unknown1072(60000)
    Unknown1110(120000, 0)
    RefreshMultihit()

    def upon_3():
        Unknown36(22)
        Unknown1086(22)
        teleportRelativeX(-250000)
        Unknown1007(-400000)
        Unknown35()
    sprite('jb450_25', 2)	# 469-470	 **attackbox here**
    GFX_0('jb450_ZanEff', -1)
    Unknown1072(325000)
    Unknown1110(130000, 0)
    RefreshMultihit()

    def upon_3():
        Unknown36(22)
        Unknown1086(22)
        teleportRelativeX(-150000)
        Unknown1007(-50000)
        Unknown35()
    sprite('jb450_25', 25)	# 471-495	 **attackbox here**
    clearUponHandler(3)
    Unknown1072(0)
    Unknown1084(1)
    Unknown36(22)
    Unknown3001(255)
    Unknown1086(22)
    teleportRelativeX(-200000)
    Unknown1007(-100000)
    Unknown35()
    sprite('jb450_25', 20)	# 496-515	 **attackbox here**
    GFX_0('jb450_ZanEff', -1)
    physicsXImpulse(120000)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(100000)
    AirPushbackY(1)
    Unknown9095()
    AirUntechableTime(999)
    Unknown9202(999)
    RefreshMultihit()
    sprite('jb450_25', 24)	# 516-539	 **attackbox here**
    Unknown21015('41737472616c5f43616d657261000000000000000000000000000000000000008a13000000000000')
    sprite('jb450_25', 12)	# 540-551	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(0)
    Damage(0)
    Unknown11072(0, 0, 0)
    Unknown11001(999, 999, 999)
    Unknown11083(1)
    Unknown11023(1)
    Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21015('41737472616c5f43616d657261000000000000000000000000000000000000008b13000000000000')
    GFX_0('jb450_RedBG', -1)
    GFX_0('jbef_450ZanzoNokosiMato', -1)
    sprite('jb450_26', 10)	# 552-561	 **attackbox here**
    Unknown3001(255)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1086(22)
    teleportRelativeX(400000)
    SFX_3('jbse_01')
    sprite('jb450_27', 8)	# 562-569	 **attackbox here**
    sprite('jb450_28', 8)	# 570-577	 **attackbox here**
    sprite('jb450_29', 8)	# 578-585	 **attackbox here**
    sprite('jb450_30', 18)	# 586-603	 **attackbox here**
    tag_voice(0, 'bjb293_0', 'bjb293_1', '', '')
    sprite('jb401_02ex02', 1)	# 604-604	 **attackbox here**
    GFX_0('jb450_Slash', -1)
    SFX_3('jbse_09')
    Unknown21015('41737472616c5f43616d657261000000000000000000000000000000000000008c13000000000000')
    AttackLevel_(5)
    Damage(9000)
    Unknown11001(0, 0, 0)
    AirPushbackX(40000)
    AirPushbackY(40000)
    YImpluseBeforeWallbounce(0)
    Unknown11083(0)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    RefreshMultihit()
    sprite('jb401_02ex02', 2)	# 605-606	 **attackbox here**
    sprite('jb450_31', 3)	# 607-609	 **attackbox here**
    Unknown26('jb450_RedBG')
    GFX_0('jb450_BG2', -1)
    sprite('jb450_32', 3)	# 610-612	 **attackbox here**
    sprite('jb450_33', 3)	# 613-615	 **attackbox here**
    sprite('jb450_34', 3)	# 616-618	 **attackbox here**
    sprite('jb450_32', 3)	# 619-621	 **attackbox here**
    sprite('jb450_33', 3)	# 622-624	 **attackbox here**
    sprite('jb450_34', 3)	# 625-627	 **attackbox here**
    sprite('jb450_32', 3)	# 628-630	 **attackbox here**
    Unknown21015('41737472616c5f43616d657261000000000000000000000000000000000000008d13000000000000')
    sprite('jb450_33', 3)	# 631-633	 **attackbox here**
    sprite('jb450_34', 3)	# 634-636	 **attackbox here**
    sprite('jb450_32', 3)	# 637-639	 **attackbox here**
    sprite('jb450_33', 3)	# 640-642	 **attackbox here**
    sprite('jb450_34', 3)	# 643-645	 **attackbox here**
    sprite('jb401_02ex02', 1)	# 646-646	 **attackbox here**
    Damage(63400)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(0)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(0)
    Unknown11064(4)
    RefreshMultihit()
    Unknown23024(0)
    sprite('jb450_32', 3)	# 647-649	 **attackbox here**
    sprite('jb450_33', 3)	# 650-652	 **attackbox here**
    sprite('jb450_34', 3)	# 653-655	 **attackbox here**
    sprite('jb450_32', 3)	# 656-658	 **attackbox here**
    sprite('jb450_33', 3)	# 659-661	 **attackbox here**
    sprite('jb450_34', 3)	# 662-664	 **attackbox here**
    sprite('jb450_32', 3)	# 665-667	 **attackbox here**
    sprite('jb450_33', 3)	# 668-670	 **attackbox here**
    sprite('jb450_34', 3)	# 671-673	 **attackbox here**
    sprite('jb450_32', 3)	# 674-676	 **attackbox here**
    sprite('jb450_33', 3)	# 677-679	 **attackbox here**
    sprite('jb450_34', 3)	# 680-682	 **attackbox here**
    sprite('jb450_32', 3)	# 683-685	 **attackbox here**
    sprite('jb450_33', 3)	# 686-688	 **attackbox here**
    sprite('jb450_34', 3)	# 689-691	 **attackbox here**
    sprite('jb450_32', 3)	# 692-694	 **attackbox here**
    sprite('jb450_33', 3)	# 695-697	 **attackbox here**
    sprite('jb450_34', 3)	# 698-700	 **attackbox here**
    sprite('jb450_32', 3)	# 701-703	 **attackbox here**
    sprite('jb450_33', 3)	# 704-706	 **attackbox here**
    sprite('jb450_34', 3)	# 707-709	 **attackbox here**
    sprite('jb450_32', 3)	# 710-712	 **attackbox here**
    sprite('jb450_33', 3)	# 713-715	 **attackbox here**
    sprite('jb450_34', 3)	# 716-718	 **attackbox here**
    sprite('jb450_32', 3)	# 719-721	 **attackbox here**
    sprite('jb450_33', 3)	# 722-724	 **attackbox here**
    sprite('jb450_34', 3)	# 725-727	 **attackbox here**
    sprite('jb450_32', 3)	# 728-730	 **attackbox here**
    sprite('jb450_33', 3)	# 731-733	 **attackbox here**
    sprite('jb450_34', 3)	# 734-736	 **attackbox here**
    sprite('jb450_32', 3)	# 737-739	 **attackbox here**
    GFX_0('jb450_BGEnd', -1)
    Unknown21015('41737472616c5f43616d657261000000000000000000000000000000000000008e13000000000000')
    Unknown1000(0)
    teleportRelativeY(0)
    sprite('jb450_35', 60)	# 740-799	 **attackbox here**
    sprite('jb450_35', 80)	# 800-879	 **attackbox here**
    Unknown18010()
    sprite('jb450_36', 7)	# 880-886
    sprite('jb450_37', 7)	# 887-893
    GFX_1('jbef_noutou_bloom', 0)
    SFX_3('jbse_07')
    Unknown21011(90)
    sprite('jb450_38', 32767)	# 894-33660

@Subroutine
def MouthTableInit():
    Unknown18011('bjb000', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb500', 12643, 14177, 14179, 14177, 14179, 14179, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb502', 12643, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb503', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 12857, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb521', 12643, 14177, 14179, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb522', 12899, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb523', 12899, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb403_0', 12643, 14177, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb403_1', 12643, 14177, 12643, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb600bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601bpt', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601bptb', 12643, 14177, 12643, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601bptc', 12643, 14177, 12643, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb600brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601pka', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb600pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb600rbl', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601ume', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb600uor', 12643, 13153, 25392, 24887, 25399, 24887, 25399, 24887, 12849, 14435, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb601uwa', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb700bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14435, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb701bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb701bpt', 12643, 13665, 12643, 24885, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb700brg', 12643, 14177, 13155, 24886, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb700pka', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb701pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb701rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb701ume', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb701uor', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bjb700uwa', 12643, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('62706800000000000000000000000000626a62000000000000000000000000006268610000000000000000000000000062707400000000000000000000000000'):
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
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bjn')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uor')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('ume')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('jb600_00', 20)	# 2-21
    sprite('jb600_01', 7)	# 22-28
    sprite('jb600_02', 90)	# 29-118
    Unknown7006('bjb500', 100, 895642210, 12592, 0, 0, 100, 895642210, 13360, 0, 0, 100, 895642210, 13616, 0, 0, 100)
    sprite('jb600_03', 7)	# 119-125
    sprite('jb600_04', 7)	# 126-132
    SFX_0('019_cloth_c')
    sprite('jb600_05', 7)	# 133-139
    sprite('jb600_06', 7)	# 140-146
    sprite('jb600_07', 10)	# 147-156
    GFX_0('jbef600_manto', 100)
    sprite('jb600_08', 7)	# 157-163
    sprite('jb600_09', 7)	# 164-170
    sprite('jb600_10', 7)	# 171-177
    Unknown23018(1)
    label(1)
    sprite('jb000_00', 7)	# 178-184	 **attackbox here**
    sprite('jb000_01', 7)	# 185-191	 **attackbox here**
    sprite('jb000_02', 7)	# 192-198	 **attackbox here**
    sprite('jb000_03', 7)	# 199-205	 **attackbox here**
    sprite('jb000_04', 7)	# 206-212	 **attackbox here**
    sprite('jb000_05', 7)	# 213-219	 **attackbox here**
    sprite('jb000_06', 7)	# 220-226	 **attackbox here**
    sprite('jb000_07', 7)	# 227-233	 **attackbox here**
    sprite('jb000_08', 7)	# 234-240	 **attackbox here**
    sprite('jb000_09', 7)	# 241-247	 **attackbox here**
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('jb601_00', 1)	# 248-248
    Unknown7006('bjb502', 100, 895642210, 13104, 0, 0, 100, 895642210, 13360, 0, 0, 100, 895642210, 13616, 0, 0, 100)
    label(11)
    sprite('jb601_00', 20)	# 249-268
    sprite('jb601_01', 9)	# 269-277
    sprite('jb601_02', 9)	# 278-286
    loopRest()
    if SLOT_97:
        _gotolabel(11)
    sprite('jb601_00', 20)	# 287-306
    sprite('jb601_03', 9)	# 307-315
    sprite('jb601_04', 9)	# 316-324
    Unknown23018(1)
    label(12)
    sprite('jb000_00', 7)	# 325-331	 **attackbox here**
    sprite('jb000_01', 7)	# 332-338	 **attackbox here**
    sprite('jb000_02', 7)	# 339-345	 **attackbox here**
    sprite('jb000_03', 7)	# 346-352	 **attackbox here**
    sprite('jb000_04', 7)	# 353-359	 **attackbox here**
    sprite('jb000_05', 7)	# 360-366	 **attackbox here**
    sprite('jb000_06', 7)	# 367-373	 **attackbox here**
    sprite('jb000_07', 7)	# 374-380	 **attackbox here**
    sprite('jb000_08', 7)	# 381-387	 **attackbox here**
    sprite('jb000_09', 7)	# 388-394	 **attackbox here**
    gotoLabel(12)
    ExitState()
    label(30)
    sprite('jb000_00', 1)	# 395-395	 **attackbox here**
    SFX_1('bjb701ume')
    label(31)
    sprite('jb000_00', 7)	# 396-402	 **attackbox here**
    sprite('jb000_01', 7)	# 403-409	 **attackbox here**
    sprite('jb000_02', 7)	# 410-416	 **attackbox here**
    sprite('jb000_03', 7)	# 417-423	 **attackbox here**
    sprite('jb000_04', 7)	# 424-430	 **attackbox here**
    sprite('jb000_05', 7)	# 431-437	 **attackbox here**
    sprite('jb000_06', 7)	# 438-444	 **attackbox here**
    sprite('jb000_07', 7)	# 445-451	 **attackbox here**
    sprite('jb000_08', 7)	# 452-458	 **attackbox here**
    sprite('jb000_09', 7)	# 459-465	 **attackbox here**
    gotoLabel(31)
    label(100)
    sprite('jb601_00', 1)	# 466-466
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)
    SFX_1('bjb600brg')
    label(101)
    sprite('jb601_00', 20)	# 467-486
    sprite('jb601_01', 9)	# 487-495
    sprite('jb601_02', 9)	# 496-504
    loopRest()
    if SLOT_97:
        _gotolabel(101)
    sprite('jb601_00', 20)	# 505-524
    Unknown21007(24, 40)
    sprite('jb601_03', 9)	# 525-533
    sprite('jb601_04', 9)	# 534-542
    Unknown21011(240)
    label(102)
    sprite('jb000_00', 7)	# 543-549	 **attackbox here**
    sprite('jb000_01', 7)	# 550-556	 **attackbox here**
    sprite('jb000_02', 7)	# 557-563	 **attackbox here**
    sprite('jb000_03', 7)	# 564-570	 **attackbox here**
    sprite('jb000_04', 7)	# 571-577	 **attackbox here**
    sprite('jb000_05', 7)	# 578-584	 **attackbox here**
    sprite('jb000_06', 7)	# 585-591	 **attackbox here**
    sprite('jb000_07', 7)	# 592-598	 **attackbox here**
    sprite('jb000_08', 7)	# 599-605	 **attackbox here**
    sprite('jb000_09', 7)	# 606-612	 **attackbox here**
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('jb612_00', 8)	# 613-620
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bjb600bjn')
    sprite('jb612_01', 8)	# 621-628
    sprite('jb612_02', 8)	# 629-636
    sprite('jb612_03', 8)	# 637-644
    sprite('jb612_04', 10)	# 645-654
    sprite('jb612_05', 3)	# 655-657
    sprite('jb612_06', 3)	# 658-660
    SFX_0('010_swing_sword_1')
    label(111)
    sprite('jb612_07', 7)	# 661-667
    sprite('jb612_08', 7)	# 668-674
    sprite('jb612_09', 7)	# 675-681
    if SLOT_97:
        _gotolabel(111)
    sprite('jb612_07', 7)	# 682-688
    sprite('jb612_08', 7)	# 689-695
    sprite('jb612_09', 7)	# 696-702
    sprite('jb612_07', 1)	# 703-703
    Unknown21007(24, 40)
    Unknown21011(240)
    label(112)
    sprite('jb612_07', 7)	# 704-710
    sprite('jb612_08', 7)	# 711-717
    sprite('jb612_09', 7)	# 718-724
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('jb000_00', 1)	# 725-725	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('jb000_00', 7)	# 726-732	 **attackbox here**
    sprite('jb000_01', 7)	# 733-739	 **attackbox here**
    sprite('jb000_02', 7)	# 740-746	 **attackbox here**
    sprite('jb000_03', 7)	# 747-753	 **attackbox here**
    sprite('jb000_04', 7)	# 754-760	 **attackbox here**
    sprite('jb000_05', 7)	# 761-767	 **attackbox here**
    sprite('jb000_06', 7)	# 768-774	 **attackbox here**
    sprite('jb000_07', 7)	# 775-781	 **attackbox here**
    sprite('jb000_08', 7)	# 782-788	 **attackbox here**
    sprite('jb000_09', 7)	# 789-795	 **attackbox here**
    gotoLabel(121)
    label(122)
    sprite('jb602_06', 7)	# 796-802
    sprite('jb602_04', 7)	# 803-809
    sprite('jb602_00', 10)	# 810-819
    sprite('jb602_01', 7)	# 820-826
    SFX_1('bjb601bpt')
    sprite('jb602_02', 15)	# 827-841
    sprite('jb602_03', 6)	# 842-847
    label(123)
    sprite('jb602_00', 1)	# 848-848
    if SLOT_97:
        _gotolabel(123)
    sprite('jb602_00', 30)	# 849-878
    sprite('jb602_06', 7)	# 879-885
    Unknown21011(120)
    label(124)
    sprite('jb000_00', 7)	# 886-892	 **attackbox here**
    sprite('jb000_01', 7)	# 893-899	 **attackbox here**
    sprite('jb000_02', 7)	# 900-906	 **attackbox here**
    sprite('jb000_03', 7)	# 907-913	 **attackbox here**
    sprite('jb000_04', 7)	# 914-920	 **attackbox here**
    sprite('jb000_05', 7)	# 921-927	 **attackbox here**
    sprite('jb000_06', 7)	# 928-934	 **attackbox here**
    sprite('jb000_07', 7)	# 935-941	 **attackbox here**
    sprite('jb000_08', 7)	# 942-948	 **attackbox here**
    sprite('jb000_09', 7)	# 949-955	 **attackbox here**
    gotoLabel(124)
    ExitState()
    label(130)
    sprite('jb600_00', 20)	# 956-975
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('jb600_01', 7)	# 976-982
    sprite('jb600_02', 90)	# 983-1072
    SFX_1('bjb600pyu')
    sprite('jb600_03', 7)	# 1073-1079
    sprite('jb600_04', 7)	# 1080-1086
    SFX_0('019_cloth_c')
    sprite('jb600_05', 7)	# 1087-1093
    sprite('jb600_06', 7)	# 1094-1100
    sprite('jb600_07', 10)	# 1101-1110
    GFX_0('jbef600_manto', 100)
    sprite('jb600_08', 7)	# 1111-1117
    sprite('jb600_09', 7)	# 1118-1124
    sprite('jb600_10', 7)	# 1125-1131
    label(131)
    sprite('jb000_00', 7)	# 1132-1138	 **attackbox here**
    sprite('jb000_01', 7)	# 1139-1145	 **attackbox here**
    sprite('jb000_02', 7)	# 1146-1152	 **attackbox here**
    sprite('jb000_03', 7)	# 1153-1159	 **attackbox here**
    sprite('jb000_04', 7)	# 1160-1166	 **attackbox here**
    sprite('jb000_05', 7)	# 1167-1173	 **attackbox here**
    sprite('jb000_06', 7)	# 1174-1180	 **attackbox here**
    sprite('jb000_07', 7)	# 1181-1187	 **attackbox here**
    sprite('jb000_08', 7)	# 1188-1194	 **attackbox here**
    sprite('jb000_09', 7)	# 1195-1201	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('jb000_00', 1)	# 1202-1202	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(132)
    sprite('jb000_00', 7)	# 1203-1209	 **attackbox here**
    sprite('jb000_01', 7)	# 1210-1216	 **attackbox here**
    sprite('jb000_02', 7)	# 1217-1223	 **attackbox here**
    sprite('jb000_03', 7)	# 1224-1230	 **attackbox here**
    sprite('jb000_04', 7)	# 1231-1237	 **attackbox here**
    sprite('jb000_05', 7)	# 1238-1244	 **attackbox here**
    sprite('jb000_06', 7)	# 1245-1251	 **attackbox here**
    sprite('jb000_07', 7)	# 1252-1258	 **attackbox here**
    sprite('jb000_08', 7)	# 1259-1265	 **attackbox here**
    sprite('jb000_09', 7)	# 1266-1272	 **attackbox here**
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('jb600_00', 1)	# 1273-1273
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(141)
    sprite('jb600_00', 32767)	# 1274-34040
    label(141)
    sprite('jb600_01', 7)	# 34041-34047
    sprite('jb600_02', 90)	# 34048-34137
    SFX_1('bjb601uwa')
    sprite('jb600_03', 7)	# 34138-34144
    sprite('jb600_04', 7)	# 34145-34151
    SFX_0('019_cloth_c')
    sprite('jb600_05', 7)	# 34152-34158
    sprite('jb600_06', 7)	# 34159-34165
    sprite('jb600_07', 10)	# 34166-34175
    GFX_0('jbef600_manto', 100)
    sprite('jb600_08', 7)	# 34176-34182
    sprite('jb600_09', 7)	# 34183-34189
    sprite('jb600_10', 7)	# 34190-34196
    Unknown23018(1)
    label(142)
    sprite('jb000_00', 7)	# 34197-34203	 **attackbox here**
    sprite('jb000_01', 7)	# 34204-34210	 **attackbox here**
    sprite('jb000_02', 7)	# 34211-34217	 **attackbox here**
    sprite('jb000_03', 7)	# 34218-34224	 **attackbox here**
    sprite('jb000_04', 7)	# 34225-34231	 **attackbox here**
    sprite('jb000_05', 7)	# 34232-34238	 **attackbox here**
    sprite('jb000_06', 7)	# 34239-34245	 **attackbox here**
    sprite('jb000_07', 7)	# 34246-34252	 **attackbox here**
    sprite('jb000_08', 7)	# 34253-34259	 **attackbox here**
    sprite('jb000_09', 7)	# 34260-34266	 **attackbox here**
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('jb601_00', 1)	# 34267-34267
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bjb600rbl')
    label(151)
    sprite('jb601_00', 20)	# 34268-34287
    sprite('jb601_01', 9)	# 34288-34296
    sprite('jb601_02', 9)	# 34297-34305
    loopRest()
    if SLOT_97:
        _gotolabel(151)
    sprite('jb601_00', 20)	# 34306-34325
    sprite('jb601_03', 9)	# 34326-34334
    sprite('jb601_04', 9)	# 34335-34343
    Unknown21007(24, 40)
    Unknown21011(240)
    label(152)
    sprite('jb000_00', 7)	# 34344-34350	 **attackbox here**
    sprite('jb000_01', 7)	# 34351-34357	 **attackbox here**
    sprite('jb000_02', 7)	# 34358-34364	 **attackbox here**
    sprite('jb000_03', 7)	# 34365-34371	 **attackbox here**
    sprite('jb000_04', 7)	# 34372-34378	 **attackbox here**
    sprite('jb000_05', 7)	# 34379-34385	 **attackbox here**
    sprite('jb000_06', 7)	# 34386-34392	 **attackbox here**
    sprite('jb000_07', 7)	# 34393-34399	 **attackbox here**
    sprite('jb000_08', 7)	# 34400-34406	 **attackbox here**
    sprite('jb000_09', 7)	# 34407-34413	 **attackbox here**
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('jb000_00', 1)	# 34414-34414	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('jb000_00', 7)	# 34415-34421	 **attackbox here**
    sprite('jb000_01', 7)	# 34422-34428	 **attackbox here**
    sprite('jb000_02', 7)	# 34429-34435	 **attackbox here**
    sprite('jb000_03', 7)	# 34436-34442	 **attackbox here**
    sprite('jb000_04', 7)	# 34443-34449	 **attackbox here**
    sprite('jb000_05', 7)	# 34450-34456	 **attackbox here**
    sprite('jb000_06', 7)	# 34457-34463	 **attackbox here**
    sprite('jb000_07', 7)	# 34464-34470	 **attackbox here**
    sprite('jb000_08', 7)	# 34471-34477	 **attackbox here**
    sprite('jb000_09', 7)	# 34478-34484	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('jb300_00', 4)	# 34485-34488
    sprite('jb300_01', 4)	# 34489-34492
    sprite('jb300_02', 6)	# 34493-34498
    sprite('jb300_03', 5)	# 34499-34503
    SFX_1('bjb601pka')
    SFX_0('024_getset_b')
    sprite('jb300_03ex', 12)	# 34504-34515
    sprite('jb300_04', 8)	# 34516-34523
    sprite('jb300_04ex', 12)	# 34524-34535
    sprite('jb300_03', 8)	# 34536-34543
    sprite('jb300_03ex', 12)	# 34544-34555
    sprite('jb300_04', 8)	# 34556-34563
    sprite('jb300_04ex', 12)	# 34564-34575
    label(163)
    sprite('jb300_03', 8)	# 34576-34583
    sprite('jb300_03ex', 12)	# 34584-34595
    sprite('jb300_04', 8)	# 34596-34603
    sprite('jb300_04ex', 12)	# 34604-34615
    if SLOT_97:
        _gotolabel(163)
    sprite('jb300_01', 6)	# 34616-34621
    sprite('jb300_00', 6)	# 34622-34627
    Unknown23018(1)
    label(164)
    sprite('jb000_00', 7)	# 34628-34634	 **attackbox here**
    sprite('jb000_01', 7)	# 34635-34641	 **attackbox here**
    sprite('jb000_02', 7)	# 34642-34648	 **attackbox here**
    sprite('jb000_03', 7)	# 34649-34655	 **attackbox here**
    sprite('jb000_04', 7)	# 34656-34662	 **attackbox here**
    sprite('jb000_05', 7)	# 34663-34669	 **attackbox here**
    sprite('jb000_06', 7)	# 34670-34676	 **attackbox here**
    sprite('jb000_07', 7)	# 34677-34683	 **attackbox here**
    sprite('jb000_08', 7)	# 34684-34690	 **attackbox here**
    sprite('jb000_09', 7)	# 34691-34697	 **attackbox here**
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('jb600_00', 20)	# 34698-34717
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('jb600_01', 7)	# 34718-34724
    sprite('jb600_02', 90)	# 34725-34814
    SFX_1('bjb600uor')
    sprite('jb600_03', 7)	# 34815-34821
    sprite('jb600_04', 7)	# 34822-34828
    SFX_0('019_cloth_c')
    sprite('jb600_05', 7)	# 34829-34835
    sprite('jb600_06', 7)	# 34836-34842
    sprite('jb600_07', 10)	# 34843-34852
    GFX_0('jbef600_manto', 100)
    sprite('jb600_08', 7)	# 34853-34859
    sprite('jb600_09', 7)	# 34860-34866
    sprite('jb600_10', 7)	# 34867-34873
    label(171)
    sprite('jb000_00', 7)	# 34874-34880	 **attackbox here**
    sprite('jb000_01', 7)	# 34881-34887	 **attackbox here**
    sprite('jb000_02', 7)	# 34888-34894	 **attackbox here**
    sprite('jb000_03', 7)	# 34895-34901	 **attackbox here**
    sprite('jb000_04', 7)	# 34902-34908	 **attackbox here**
    sprite('jb000_05', 7)	# 34909-34915	 **attackbox here**
    sprite('jb000_06', 7)	# 34916-34922	 **attackbox here**
    sprite('jb000_07', 7)	# 34923-34929	 **attackbox here**
    sprite('jb000_08', 7)	# 34930-34936	 **attackbox here**
    sprite('jb000_09', 7)	# 34937-34943	 **attackbox here**
    if SLOT_97:
        _gotolabel(171)
    sprite('jb000_00', 1)	# 34944-34944	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(172)
    sprite('jb000_00', 7)	# 34945-34951	 **attackbox here**
    sprite('jb000_01', 7)	# 34952-34958	 **attackbox here**
    sprite('jb000_02', 7)	# 34959-34965	 **attackbox here**
    sprite('jb000_03', 7)	# 34966-34972	 **attackbox here**
    sprite('jb000_04', 7)	# 34973-34979	 **attackbox here**
    sprite('jb000_05', 7)	# 34980-34986	 **attackbox here**
    sprite('jb000_06', 7)	# 34987-34993	 **attackbox here**
    sprite('jb000_07', 7)	# 34994-35000	 **attackbox here**
    sprite('jb000_08', 7)	# 35001-35007	 **attackbox here**
    sprite('jb000_09', 7)	# 35008-35014	 **attackbox here**
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('jb638_00', 10)	# 35015-35024
    Unknown1000(-1230000)
    Unknown2005()
    Unknown2019(0)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bjb601bph')
        Unknown23018(1)
    label(181)
    sprite('jb638_01', 7)	# 35025-35031
    sprite('jb638_02', 7)	# 35032-35038
    sprite('jb638_01', 7)	# 35039-35045
    sprite('jb638_00', 10)	# 35046-35055
    gotoLabel(181)
    ExitState()
    label(190)
    sprite('jb000_00', 1)	# 35056-35056	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('jb000_00', 7)	# 35057-35063	 **attackbox here**
    sprite('jb000_01', 7)	# 35064-35070	 **attackbox here**
    sprite('jb000_02', 7)	# 35071-35077	 **attackbox here**
    sprite('jb000_03', 7)	# 35078-35084	 **attackbox here**
    sprite('jb000_04', 7)	# 35085-35091	 **attackbox here**
    sprite('jb000_05', 7)	# 35092-35098	 **attackbox here**
    sprite('jb000_06', 7)	# 35099-35105	 **attackbox here**
    sprite('jb000_07', 7)	# 35106-35112	 **attackbox here**
    sprite('jb000_08', 7)	# 35113-35119	 **attackbox here**
    sprite('jb000_09', 7)	# 35120-35126	 **attackbox here**
    gotoLabel(191)
    label(192)
    sprite('jb601_04', 9)	# 35127-35135
    SFX_1('bjb601ume')
    sprite('jb601_03', 9)	# 35136-35144
    label(193)
    sprite('jb601_02', 9)	# 35145-35153
    sprite('jb601_01', 9)	# 35154-35162
    sprite('jb601_00', 20)	# 35163-35182
    if SLOT_97:
        _gotolabel(193)
    sprite('jb601_03', 9)	# 35183-35191
    sprite('jb601_04', 9)	# 35192-35200
    Unknown23018(1)
    label(194)
    sprite('jb000_00', 7)	# 35201-35207	 **attackbox here**
    sprite('jb000_01', 7)	# 35208-35214	 **attackbox here**
    sprite('jb000_02', 7)	# 35215-35221	 **attackbox here**
    sprite('jb000_03', 7)	# 35222-35228	 **attackbox here**
    sprite('jb000_04', 7)	# 35229-35235	 **attackbox here**
    sprite('jb000_05', 7)	# 35236-35242	 **attackbox here**
    sprite('jb000_06', 7)	# 35243-35249	 **attackbox here**
    sprite('jb000_07', 7)	# 35250-35256	 **attackbox here**
    sprite('jb000_08', 7)	# 35257-35263	 **attackbox here**
    sprite('jb000_09', 7)	# 35264-35270	 **attackbox here**
    gotoLabel(194)
    ExitState()
    label(991)
    sprite('jb000_00', 1)	# 35271-35271	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('jb000_00', 7)	# 35272-35278	 **attackbox here**
    sprite('jb000_01', 7)	# 35279-35285	 **attackbox here**
    sprite('jb000_02', 7)	# 35286-35292	 **attackbox here**
    sprite('jb000_03', 7)	# 35293-35299	 **attackbox here**
    sprite('jb000_04', 7)	# 35300-35306	 **attackbox here**
    sprite('jb000_05', 7)	# 35307-35313	 **attackbox here**
    sprite('jb000_06', 7)	# 35314-35320	 **attackbox here**
    sprite('jb000_07', 7)	# 35321-35327	 **attackbox here**
    sprite('jb000_08', 7)	# 35328-35334	 **attackbox here**
    sprite('jb000_09', 7)	# 35335-35341	 **attackbox here**
    gotoLabel(992)
    label(993)
    sprite('jb033_00', 2)	# 35342-35343

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
    sprite('jb033_01', 3)	# 35344-35346
    label(994)
    sprite('jb033_02', 3)	# 35347-35349
    sprite('jb033_01', 3)	# 35350-35352
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 35353-35355
    ExitState()
    label(1000)
    sprite('jb601_00', 20)	# 35356-35375
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 10001):
            SFX_1('bjb601')
            sendToLabel(1002)
        if (SLOT_48 == 10004):
            clearUponHandler(43)
            Unknown18008()
    sprite('jb601_01', 9)	# 35376-35384
    sprite('jb601_02', 9)	# 35385-35393
    label(1001)
    sprite('jb601_00', 20)	# 35394-35413
    sprite('jb601_01', 9)	# 35414-35422
    sprite('jb601_02', 9)	# 35423-35431
    gotoLabel(1001)
    label(1002)
    sprite('jb601_00', 20)	# 35432-35451
    sprite('jb601_01', 9)	# 35452-35460
    sprite('jb601_02', 9)	# 35461-35469
    if SLOT_97:
        _gotolabel(1002)
    sprite('jb601_00', 20)	# 35470-35489
    sprite('jb601_00', 1)	# 35490-35490
    Unknown23029(24, 10002, 0)
    Unknown23029(22, 10002, 0)
    Unknown23029(23, 10002, 0)
    Unknown23029(24, 10005, 0)
    Unknown23029(22, 10005, 0)
    Unknown23029(23, 10005, 0)
    sprite('jb601_01', 9)	# 35491-35499
    sprite('jb601_02', 9)	# 35500-35508
    label(1003)
    sprite('jb601_00', 20)	# 35509-35528
    sprite('jb601_01', 9)	# 35529-35537
    sprite('jb601_02', 9)	# 35538-35546
    gotoLabel(1003)

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
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 900000):
                    if (SLOT_145 >= 200000):
                        sendToLabel(170)
                        clearUponHandler(3)
            if PartnerChar('bph'):
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
    sprite('jb610_00', 7)	# 4-10
    Unknown36(24)
    Unknown2034(0)
    Unknown2053(0)
    Unknown35()
    Unknown2004(1, 0)
    sprite('jb610_01', 7)	# 11-17
    sprite('jb610_02', 7)	# 18-24
    sprite('jb610_03', 10)	# 25-34
    sprite('jb610_04', 4)	# 35-38
    sprite('jb610_05', 4)	# 39-42
    GFX_0('jb610_Slash', -1)
    SFX_3('jbse_07')
    sprite('jb610_06', 7)	# 43-49
    sprite('jb610_07', 6)	# 50-55
    sprite('jb610_08', 6)	# 56-61
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bjb524', 100, 895642210, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bjb402_0', 100, 878864994, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bjb522', 100, 895642210, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('jb610_09', 6)	# 62-67
    sprite('jb610_10', 6)	# 68-73
    label(1)
    sprite('jb610_07', 6)	# 74-79
    sprite('jb610_08', 6)	# 80-85
    sprite('jb610_09', 6)	# 86-91
    sprite('jb610_10', 6)	# 92-97
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('jb611_00', 8)	# 98-105
    GFX_0('jb611_Tail', -1)
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bjb524', 100, 895642210, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bjb402_0', 100, 878864994, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bjb520', 100, 895642210, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('jb611_01', 8)	# 106-113
    sprite('jb611_02', 32767)	# 114-32880
    loopRest()
    label(100)
    sprite('jb602_06', 6)	# 32881-32886
    sprite('jb602_04', 6)	# 32887-32892
    sprite('jb602_00', 6)	# 32893-32898
    sprite('jb602_03', 6)	# 32899-32904
    sprite('jb602_01', 7)	# 32905-32911
    SFX_1('bjb700brg')
    sprite('jb602_02', 10)	# 32912-32921
    sprite('jb602_01', 6)	# 32922-32927
    sprite('jb602_00', 60)	# 32928-32987
    GFX_1('jbef_tameiki', 0)
    sprite('jb602_04', 10)	# 32988-32997
    sprite('jb602_05', 10)	# 32998-33007
    sprite('jb602_04', 10)	# 33008-33017
    sprite('jb602_00', 10)	# 33018-33027
    sprite('jb602_04', 10)	# 33028-33037
    sprite('jb602_05', 10)	# 33038-33047
    sprite('jb602_04', 10)	# 33048-33057
    label(101)
    sprite('jb602_00', 1)	# 33058-33058
    if SLOT_97:
        _gotolabel(101)
    sprite('jb602_00', 30)	# 33059-33088
    sprite('jb602_00', 32767)	# 33089-65855
    Unknown21007(24, 40)
    Unknown21011(300)
    label(110)
    sprite('jb611_00', 8)	# 65856-65863
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
    GFX_0('jb611_Tail', -1)
    SFX_1('bjb700bjn')
    sprite('jb611_01', 8)	# 65864-65871
    label(111)
    sprite('jb611_02', 1)	# 65872-65872
    if SLOT_97:
        _gotolabel(111)
    sprite('jb611_02', 30)	# 65873-65902
    sprite('jb611_02', 32767)	# 65903-98669
    Unknown21007(24, 40)
    Unknown21011(240)
    label(120)
    sprite('jb610_00', 7)	# 98670-98676
    Unknown2004(1, 0)
    sprite('jb610_01', 7)	# 98677-98683
    sprite('jb610_02', 7)	# 98684-98690
    sprite('jb610_03', 10)	# 98691-98700
    sprite('jb610_04', 4)	# 98701-98704
    sprite('jb610_05', 4)	# 98705-98708
    GFX_0('jb610_Slash', -1)
    SFX_3('jbse_07')
    sprite('jb610_06', 7)	# 98709-98715
    sprite('jb610_07', 6)	# 98716-98721
    sprite('jb610_08', 6)	# 98722-98727
    SFX_1('bjb700pka')
    sprite('jb610_09', 6)	# 98728-98733
    sprite('jb610_10', 6)	# 98734-98739
    label(121)
    sprite('jb610_07', 6)	# 98740-98745
    sprite('jb610_08', 6)	# 98746-98751
    sprite('jb610_09', 6)	# 98752-98757
    sprite('jb610_10', 6)	# 98758-98763
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('jb610_07', 6)	# 98764-98769
    sprite('jb610_08', 6)	# 98770-98775
    sprite('jb610_09', 6)	# 98776-98781
    sprite('jb610_10', 6)	# 98782-98787
    sprite('jb610_07', 1)	# 98788-98788
    Unknown21007(24, 40)
    Unknown21011(330)
    label(122)
    sprite('jb610_07', 6)	# 98789-98794
    sprite('jb610_08', 6)	# 98795-98800
    sprite('jb610_09', 6)	# 98801-98806
    sprite('jb610_10', 6)	# 98807-98812
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('jb000_00', 1)	# 98813-98813	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('jb000_00', 7)	# 98814-98820	 **attackbox here**
    sprite('jb000_01', 7)	# 98821-98827	 **attackbox here**
    sprite('jb000_02', 7)	# 98828-98834	 **attackbox here**
    sprite('jb000_03', 7)	# 98835-98841	 **attackbox here**
    sprite('jb000_04', 7)	# 98842-98848	 **attackbox here**
    sprite('jb000_05', 7)	# 98849-98855	 **attackbox here**
    sprite('jb000_06', 7)	# 98856-98862	 **attackbox here**
    sprite('jb000_07', 7)	# 98863-98869	 **attackbox here**
    sprite('jb000_08', 7)	# 98870-98876	 **attackbox here**
    sprite('jb000_09', 7)	# 98877-98883	 **attackbox here**
    gotoLabel(131)
    label(132)
    sprite('jb602_06', 6)	# 98884-98889
    sprite('jb602_04', 6)	# 98890-98895
    sprite('jb602_00', 6)	# 98896-98901
    sprite('jb602_03', 6)	# 98902-98907
    sprite('jb602_01', 7)	# 98908-98914
    SFX_1('bjb701pyu')
    sprite('jb602_02', 10)	# 98915-98924
    sprite('jb602_01', 6)	# 98925-98930
    sprite('jb602_00', 60)	# 98931-98990
    GFX_1('jbef_tameiki', 0)
    sprite('jb602_04', 10)	# 98991-99000
    sprite('jb602_05', 10)	# 99001-99010
    sprite('jb602_04', 10)	# 99011-99020
    sprite('jb602_00', 10)	# 99021-99030
    sprite('jb602_04', 10)	# 99031-99040
    sprite('jb602_05', 10)	# 99041-99050
    sprite('jb602_04', 10)	# 99051-99060
    Unknown23018(1)
    sprite('jb602_00', 32767)	# 99061-131827
    label(140)
    sprite('jb610_00', 7)	# 131828-131834
    Unknown2004(1, 0)
    sprite('jb610_01', 7)	# 131835-131841
    sprite('jb610_02', 7)	# 131842-131848
    sprite('jb610_03', 10)	# 131849-131858
    sprite('jb610_04', 4)	# 131859-131862
    sprite('jb610_05', 4)	# 131863-131866
    GFX_0('jb610_Slash', -1)
    SFX_3('jbse_07')
    sprite('jb610_06', 7)	# 131867-131873
    sprite('jb610_07', 6)	# 131874-131879
    sprite('jb610_08', 6)	# 131880-131885
    SFX_1('bjb700uwa')
    sprite('jb610_09', 6)	# 131886-131891
    sprite('jb610_10', 6)	# 131892-131897
    label(141)
    sprite('jb610_07', 6)	# 131898-131903
    sprite('jb610_08', 6)	# 131904-131909
    sprite('jb610_09', 6)	# 131910-131915
    sprite('jb610_10', 6)	# 131916-131921
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('jb610_07', 1)	# 131922-131922
    Unknown21007(24, 40)
    Unknown21011(300)
    label(142)
    sprite('jb610_07', 6)	# 131923-131928
    sprite('jb610_08', 6)	# 131929-131934
    sprite('jb610_09', 6)	# 131935-131940
    sprite('jb610_10', 6)	# 131941-131946
    loopRest()
    gotoLabel(142)
    label(150)
    sprite('jb000_00', 1)	# 131947-131947	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('jb000_00', 7)	# 131948-131954	 **attackbox here**
    sprite('jb000_01', 7)	# 131955-131961	 **attackbox here**
    sprite('jb000_02', 7)	# 131962-131968	 **attackbox here**
    sprite('jb000_03', 7)	# 131969-131975	 **attackbox here**
    sprite('jb000_04', 7)	# 131976-131982	 **attackbox here**
    sprite('jb000_05', 7)	# 131983-131989	 **attackbox here**
    sprite('jb000_06', 7)	# 131990-131996	 **attackbox here**
    sprite('jb000_07', 7)	# 131997-132003	 **attackbox here**
    sprite('jb000_08', 7)	# 132004-132010	 **attackbox here**
    sprite('jb000_09', 7)	# 132011-132017	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('jb602_06', 6)	# 132018-132023
    sprite('jb602_04', 6)	# 132024-132029
    sprite('jb602_00', 6)	# 132030-132035
    sprite('jb602_03', 6)	# 132036-132041
    sprite('jb602_01', 7)	# 132042-132048
    SFX_1('bjb701rbl')
    sprite('jb602_02', 10)	# 132049-132058
    sprite('jb602_01', 6)	# 132059-132064
    sprite('jb602_00', 60)	# 132065-132124
    GFX_1('jbef_tameiki', 0)
    sprite('jb602_04', 10)	# 132125-132134
    sprite('jb602_05', 10)	# 132135-132144
    sprite('jb602_04', 10)	# 132145-132154
    sprite('jb602_00', 10)	# 132155-132164
    sprite('jb602_04', 10)	# 132165-132174
    sprite('jb602_05', 10)	# 132175-132184
    sprite('jb602_04', 10)	# 132185-132194
    Unknown23018(1)
    sprite('jb602_00', 32767)	# 132195-164961
    label(160)
    sprite('jb000_00', 1)	# 164962-164962	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('jb000_00', 7)	# 164963-164969	 **attackbox here**
    sprite('jb000_01', 7)	# 164970-164976	 **attackbox here**
    sprite('jb000_02', 7)	# 164977-164983	 **attackbox here**
    sprite('jb000_03', 7)	# 164984-164990	 **attackbox here**
    sprite('jb000_04', 7)	# 164991-164997	 **attackbox here**
    sprite('jb000_05', 7)	# 164998-165004	 **attackbox here**
    sprite('jb000_06', 7)	# 165005-165011	 **attackbox here**
    sprite('jb000_07', 7)	# 165012-165018	 **attackbox here**
    sprite('jb000_08', 7)	# 165019-165025	 **attackbox here**
    sprite('jb000_09', 7)	# 165026-165032	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('jb611_00', 8)	# 165033-165040
    GFX_0('jb611_Tail', -1)
    SFX_1('bjb701uor')
    sprite('jb611_01', 8)	# 165041-165048
    Unknown23018(1)
    sprite('jb611_02', 32767)	# 165049-197815
    label(170)
    sprite('jb000_00', 1)	# 197816-197816	 **attackbox here**
    Unknown2019(100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)

    def upon_39():
        clearUponHandler(39)
        SFX_1('bjb701bpt')
        Unknown23018(1)
    Unknown48('190000000200000035000000180000000200000027000000')
    if (SLOT_53 == SLOT_39):
        if (not SLOT_39):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                sendToLabel(171)
            else:
                SLOT_54 = 1
        else:
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                sendToLabel(171)
            else:
                SLOT_54 = 1
    elif (not SLOT_39):
        Unknown48('190000000200000033000000180000000200000016000000')
        Unknown47('01000000020000003300000002000000160000000200000033000000')
        if (SLOT_51 >= 0):
            pass
        else:
            sendToLabel(171)
    else:
        Unknown48('190000000200000033000000180000000200000016000000')
        Unknown47('01000000020000003300000002000000160000000200000033000000')
        if (SLOT_51 <= 0):
            pass
        else:
            sendToLabel(171)
    sprite('jb003_00ex00', 3)	# 197817-197819
    Unknown2005()
    sprite('jb003_01', 3)	# 197820-197822
    sprite('jb003_00', 3)	# 197823-197825
    label(171)
    sprite('jb000_00', 7)	# 197826-197832	 **attackbox here**
    sprite('jb000_01', 7)	# 197833-197839	 **attackbox here**
    sprite('jb000_02', 7)	# 197840-197846	 **attackbox here**
    sprite('jb000_03', 7)	# 197847-197853	 **attackbox here**
    sprite('jb000_04', 7)	# 197854-197860	 **attackbox here**
    sprite('jb000_05', 7)	# 197861-197867	 **attackbox here**
    sprite('jb000_06', 7)	# 197868-197874	 **attackbox here**
    sprite('jb000_07', 7)	# 197875-197881	 **attackbox here**
    sprite('jb000_08', 7)	# 197882-197888	 **attackbox here**
    sprite('jb000_09', 7)	# 197889-197895	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('jb635_00', 7)	# 197896-197902
    if SLOT_158:
        Unknown2019(0)
    else:
        Unknown2019(-500)
    sprite('jb635_01', 7)	# 197903-197909
    sprite('jb635_02', 10)	# 197910-197919
    sprite('jb635_03', 7)	# 197920-197926
    sprite('jb635_04', 7)	# 197927-197933
    sprite('jb635_05', 7)	# 197934-197940
    sprite('jb635_06', 32767)	# 197941-230707
    label(180)
    sprite('jb000_00', 1)	# 230708-230708	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('jb000_00', 7)	# 230709-230715	 **attackbox here**
    sprite('jb000_01', 7)	# 230716-230722	 **attackbox here**
    sprite('jb000_02', 7)	# 230723-230729	 **attackbox here**
    sprite('jb000_03', 7)	# 230730-230736	 **attackbox here**
    sprite('jb000_04', 7)	# 230737-230743	 **attackbox here**
    sprite('jb000_05', 7)	# 230744-230750	 **attackbox here**
    sprite('jb000_06', 7)	# 230751-230757	 **attackbox here**
    sprite('jb000_07', 7)	# 230758-230764	 **attackbox here**
    sprite('jb000_08', 7)	# 230765-230771	 **attackbox here**
    sprite('jb000_09', 7)	# 230772-230778	 **attackbox here**
    gotoLabel(181)
    label(182)
    sprite('jb611_00', 8)	# 230779-230786
    GFX_0('jb611_Tail', -1)
    SFX_1('bjb701bph')
    sprite('jb611_01', 8)	# 230787-230794
    Unknown23018(1)
    sprite('jb611_02', 32767)	# 230795-263561
    label(190)
    sprite('jb000_00', 1)	# 263562-263562	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('jb000_00', 7)	# 263563-263569	 **attackbox here**
    sprite('jb000_01', 7)	# 263570-263576	 **attackbox here**
    sprite('jb000_02', 7)	# 263577-263583	 **attackbox here**
    sprite('jb000_03', 7)	# 263584-263590	 **attackbox here**
    sprite('jb000_04', 7)	# 263591-263597	 **attackbox here**
    sprite('jb000_05', 7)	# 263598-263604	 **attackbox here**
    sprite('jb000_06', 7)	# 263605-263611	 **attackbox here**
    sprite('jb000_07', 7)	# 263612-263618	 **attackbox here**
    sprite('jb000_08', 7)	# 263619-263625	 **attackbox here**
    sprite('jb000_09', 7)	# 263626-263632	 **attackbox here**
    gotoLabel(191)
    label(192)
    sprite('jb610_00', 7)	# 263633-263639
    Unknown2004(1, 0)
    sprite('jb610_01', 7)	# 263640-263646
    sprite('jb610_02', 7)	# 263647-263653
    sprite('jb610_03', 10)	# 263654-263663
    sprite('jb610_04', 4)	# 263664-263667
    sprite('jb610_05', 4)	# 263668-263671
    GFX_0('jb610_Slash', -1)
    SFX_3('jbse_07')
    sprite('jb610_06', 7)	# 263672-263678
    sprite('jb610_07', 6)	# 263679-263684
    sprite('jb610_08', 6)	# 263685-263690
    SFX_1('bjb701ume')
    sprite('jb610_09', 6)	# 263691-263696
    sprite('jb610_10', 6)	# 263697-263702
    Unknown23018(1)
    label(193)
    sprite('jb610_07', 6)	# 263703-263708
    sprite('jb610_08', 6)	# 263709-263714
    sprite('jb610_09', 6)	# 263715-263720
    sprite('jb610_10', 6)	# 263721-263726
    loopRest()
    gotoLabel(193)

@State
def CmnActLose():
    sprite('jb620_00', 8)	# 1-8
    sprite('jb620_01', 8)	# 9-16
    Unknown7006('bjb403_0', 100, 878864994, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('jb620_02', 6)	# 17-22
    physicsXImpulse(-1000)
    sprite('jb620_03', 7)	# 23-29
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('jb620_04', 7)	# 30-36
    sprite('jb620_05', 7)	# 37-43
    sprite('jb620_06', 7)	# 44-50
    sprite('jb620_07', 32767)	# 51-32817
    Unknown23018(1)

@State
def EventDefEntryWait():
    label(0)
    sprite('jb000_00', 7)	# 1-7	 **attackbox here**
    sprite('jb000_01', 7)	# 8-14	 **attackbox here**
    sprite('jb000_02', 7)	# 15-21	 **attackbox here**
    sprite('jb000_03', 7)	# 22-28	 **attackbox here**
    sprite('jb000_04', 7)	# 29-35	 **attackbox here**
    sprite('jb000_05', 7)	# 36-42	 **attackbox here**
    sprite('jb000_06', 7)	# 43-49	 **attackbox here**
    sprite('jb000_07', 7)	# 50-56	 **attackbox here**
    sprite('jb000_08', 7)	# 57-63	 **attackbox here**
    sprite('jb000_09', 7)	# 64-70	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryStand():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefWin():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefLose():
    sprite('rg620_05', 32767)	# 1-32767

@State
def EventDefChouhatsu():
    sprite('jb300_00', 4)	# 1-4
    sprite('jb300_01', 4)	# 5-8
    sprite('jb300_02', 4)	# 9-12
    sprite('jb300_03', 6)	# 13-18
    sprite('jb300_04', 6)	# 19-24
    sprite('jb300_05', 7)	# 25-31
    sprite('jb300_04', 6)	# 32-37
    sprite('jb300_05', 7)	# 38-44
    sprite('jb300_03', 9)	# 45-53
    sprite('jb300_06', 6)	# 54-59
    sprite('jb300_07', 6)	# 60-65
    sprite('jb300_08', 6)	# 66-71
    loopRest()
    enterState('CmnActStand')

@State
def EventDefChouhatsu2():
    sprite('jb300_00', 4)	# 1-4
    sprite('jb300_01', 4)	# 5-8
    sprite('jb300_02', 4)	# 9-12
    sprite('jb300_03', 6)	# 13-18
    sprite('jb300_04', 6)	# 19-24
    sprite('jb300_05', 32767)	# 25-32791

@State
def EventDefChouhatsuEnd():
    sprite('jb300_03', 6)	# 1-6
    sprite('jb300_06', 6)	# 7-12
    sprite('jb300_07', 6)	# 13-18
    sprite('jb300_08', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventYoroke():
    sprite('jb070_07', 32767)	# 1-32767
    loopRest()

@State
def EventEntry0_WaitGazingEnemy():
    sprite('jb601_00', 32767)	# 1-32767
    loopRest()

@State
def EventEntry0_PrepareForBattle():
    sprite('rg601_00', 6)	# 1-6
    sprite('rg601_01', 6)	# 7-12
    sprite('rg601_02', 6)	# 13-18
    sprite('rg601_03', 6)	# 19-24
    sprite('rg601_04', 6)	# 25-30
    sprite('rg601_05', 6)	# 31-36
    sprite('rg601_06', 6)	# 37-42
    sprite('rg601_07', 6)	# 43-48
    SFX_3('rgse_05')
    sprite('rg601_08', 6)	# 49-54
    sprite('rg601_09', 6)	# 55-60
    sprite('rg601_10', 6)	# 61-66
    sprite('rg601_11', 4)	# 67-70
    sprite('rg601_12', 4)	# 71-74
    SFX_0('006_swing_blade_1')
    sprite('rg601_13', 4)	# 75-78
    sprite('rg601_14', 4)	# 79-82
    sprite('rg601_15', 4)	# 83-86
    SFX_0('006_swing_blade_1')
    sprite('rg601_16', 4)	# 87-90
    sprite('rg601_17', 6)	# 91-96
    sprite('rg601_18', 6)	# 97-102
    sprite('rg601_19', 3)	# 103-105
    sprite('rg601_20', 6)	# 106-111
    sprite('rg601_21', 6)	# 112-117
    SFX_3('rgse_00')
    sprite('rg601_22', 6)	# 118-123
    sprite('rg601_23', 6)	# 124-129
    loopRest()
    enterState('CmnActStand')

@State
def EventWarpIn():
    Unknown3001(0)
    sprite('rg000_00', 6)	# 1-6
    Unknown3004(10)
    SFX_0('001_airbackdash_0')
    sprite('keep', 20)	# 7-26
    SFX_0('000_airdash_2')
    sprite('keep', 1)	# 27-27
    Unknown3004(0)
    Unknown3001(255)
    loopRest()
    enterState('CmnActStand')

@State
def EventWarpOut():
    sprite('keep', 6)	# 1-6
    Unknown3004(-10)
    SFX_0('001_airbackdash_0')
    sprite('keep', 20)	# 7-26
    SFX_0('000_airdash_2')
    sprite('null', 32767)	# 27-32793
    Unknown3004(0)
    Unknown3001(0)
    loopRest()

@State
def Act3Event_Udekumi():
    label(0)
    sprite('jb601_00', 20)	# 1-20
    sprite('jb601_01', 9)	# 21-29
    sprite('jb601_02', 9)	# 30-38
    loopRest()
    gotoLabel(0)

@State
def Act3Event_UdekumiEnd():
    sprite('jb601_03', 9)	# 1-9
    sprite('jb601_04', 9)	# 10-18
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Think():
    sprite('jb611_00', 8)	# 1-8
    GFX_0('jb611_Tail_Event', -1)
    sprite('jb611_01', 8)	# 9-16
    sprite('jb611_02', 32767)	# 17-32783
    loopRest()

@State
def Act3Event_ThinkEnd():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown26('jb611_Tail_Event')
    sprite('jb611_01', 8)	# 1-8
    sprite('jb611_00', 8)	# 9-16
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_jbvsrg_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
        Unknown2004(1, 0)
        Unknown1000(-320000)
    sprite('jb202_05', 3)	# 1-3
    Unknown8006(100, 1, 0)
    physicsXImpulse(1000)
    sprite('jb202_06', 4)	# 4-7
    physicsXImpulse(5000)
    Unknown8006(100, 1, 0)
    SFX_0('010_swing_sword_1')
    sprite('jb202_07', 11)	# 8-18	 **attackbox here**
    Unknown1084(1)
    Unknown8006(100, 1, 0)
    GFX_0('jbef202_zanzou_2nd', 100)
    sprite('jb202_08', 5)	# 19-23
    sprite('jb202_09', 5)	# 24-28
    sprite('jb202_10', 5)	# 29-33
    sprite('jb202_11', 5)	# 34-38
    sprite('jb202_12', 5)	# 39-43
    sprite('jb202_13', 5)	# 44-48
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Reaction():
    sprite('jb001_00', 6)	# 1-6
    sprite('jb001_01', 6)	# 7-12
    sprite('jb001_02', 6)	# 13-18
    sprite('jb001_03', 6)	# 19-24
    sprite('jb001_04', 8)	# 25-32
    sprite('jb001_06', 8)	# 33-40
    sprite('jb001_04', 8)	# 41-48
    sprite('jb001_06', 8)	# 49-56
    sprite('jb001_04', 8)	# 57-64
    sprite('jb001_06', 8)	# 65-72
    sprite('jb001_04', 8)	# 73-80
    sprite('jb001_03', 9)	# 81-89
    sprite('jb001_02', 9)	# 90-98
    sprite('jb001_01', 9)	# 99-107
    sprite('jb001_00', 9)	# 108-116
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Sword():
    sprite('jb612_00', 8)	# 1-8
    sprite('jb612_01', 8)	# 9-16
    sprite('jb612_02', 8)	# 17-24
    sprite('jb612_03', 8)	# 25-32
    sprite('jb612_04', 10)	# 33-42
    SFX_0('010_swing_sword_1')
    sprite('jb612_05', 3)	# 43-45
    sprite('jb612_06', 3)	# 46-48
    label(0)
    sprite('jb612_07', 7)	# 49-55
    sprite('jb612_08', 7)	# 56-62
    sprite('jb612_09', 7)	# 63-69
    loopRest()
    gotoLabel(0)

@State
def Act3Event_SwordLoop():
    label(0)
    sprite('jb612_07', 7)	# 1-7
    sprite('jb612_08', 7)	# 8-14
    sprite('jb612_09', 7)	# 15-21
    loopRest()
    gotoLabel(0)

@State
def Act3Event_SwordEnd():
    sprite('jb603_08', 7)	# 1-7
    sprite('jb603_09', 9)	# 8-16
    sprite('jb603_10', 7)	# 17-23
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Tameiki():
    sprite('jb602_06', 7)	# 1-7
    sprite('jb602_04', 7)	# 8-14
    sprite('jb602_00', 10)	# 15-24
    sprite('jb602_01', 7)	# 25-31
    sprite('jb602_02', 15)	# 32-46
    sprite('jb602_03', 6)	# 47-52
    sprite('jb602_00', 32767)	# 53-32819
    GFX_1('jbef_tameiki', 0)
    loopRest()

@State
def Act3Event_TameikiEnd():
    sprite('jb602_04', 7)	# 1-7
    sprite('jb602_06', 7)	# 8-14
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Miageru():
    sprite('jb321_15ex00', 7)	# 1-7
    sprite('jb321_14ex00', 7)	# 8-14
    sprite('jb321_13ex00', 7)	# 15-21
    sprite('jb450_39', 6)	# 22-27
    sprite('jb450_40', 7)	# 28-34
    sprite('jb450_41', 32767)	# 35-32801
    loopRest()

@State
def Act3Event_MiageruEnd():
    sprite('jb321_13ex00', 8)	# 1-8
    sprite('jb321_14ex00', 8)	# 9-16
    sprite('jb321_15ex00', 8)	# 17-24
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Kansyo():
    sprite('keep', 4)	# 1-4
    GFX_0('NOISE', -1)
    SFX_0('023_noize')
    sprite('jb040_00', 3)	# 5-7
    sprite('jb040_01', 3)	# 8-10
    label(0)
    sprite('jb040_02', 4)	# 11-14
    sprite('jb040_03', 4)	# 15-18
    sprite('jb040_04', 4)	# 19-22
    loopRest()
    gotoLabel(0)

@State
def Act3Event_Udekumi2():
    sprite('jb601_00', 32767)	# 1-32767
    loopRest()

@State
def Act3Event_UdekumiEnd():
    sprite('jb601_03', 9)	# 1-9
    sprite('jb601_04', 9)	# 10-18
    loopRest()
    enterState('CmnActStand')