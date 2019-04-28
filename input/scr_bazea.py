@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f415a2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
        Unknown1096(1500)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 80)

@State
def EMB_AZ_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f415a2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
        Unknown1096(1500)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-16744193, 10)
    sprite('null', 10)
    Unknown3025(-16744193, 10)
    sprite('null', 80)

@State
def EMB_AZ_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('65665f656d625f415a2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
        Unknown1096(1500)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-1761673216, 10)
    sprite('null', 10)
    Unknown3025(-1761662936, 10)
    sprite('null', 10)
    Unknown3025(-1761626956, 10)
    sprite('null', 10)
    Unknown3025(-1761673216, 10)
    sprite('null', 80)

@State
def __032rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('617a65665f343035726f636b30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(625)
        teleportRelativeX(-20000)
        Unknown1007(15000)
    sprite('null', 5)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-51)

@State
def dashEff():

    def upon_IMMEDIATE():
        Unknown4008(2)
        Unknown2054(1)
        GFX_2('azef_newdash2')
    sprite('null', 50)

@State
def dashEff2():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown2054(1)
        GFX_2('azef_newdash3')
    sprite('null', 50)

@State
def weakhit00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown4010(2)
        Unknown1007(150000)
        Unknown1096(2400)
        Unknown23015(4)
        Unknown2007()
    sprite('null', 30)
    GFX_2('azef_weakhit_red')

@State
def weakpoint01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(255)
        Unknown1096(2300)
        Unknown4061(1)
        Unknown21004(16)
        Unknown4003('617a65665f7765616b706f696e7430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()

        def upon_16():
            Unknown2071('160000000000000060ea00006400000001000000')
        Unknown4025(22)

        def upon_43():
            if (SLOT_48 == 100):
                clearUponHandler(16)
                clearUponHandler(43)
                sendToLabel(0)
    sprite('null', 20)
    GFX_0('weakstart01', -1)
    Unknown1099(-27)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(300)

@State
def weakstart01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sprite('null', 5)
    sprite('null', 30)
    GFX_2('azef_weakhit_03')

@State
def weakhit01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown4010(2)
        Unknown1007(150000)
        Unknown1096(2400)
        Unknown23015(4)
        Unknown2007()
    sprite('null', 30)
    GFX_2('azef_weakhit_yellow')

@State
def weakpoint00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(255)
        Unknown1072(180000)
        Unknown1096(2300)
        Unknown4061(1)
        Unknown21004(17)
        Unknown4003('617a65665f7765616b706f696e7430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()

        def upon_16():
            Unknown2071('160000000000000080c7feff6400000001000000')
        Unknown4025(22)

        def upon_43():
            if (SLOT_48 == 101):
                clearUponHandler(16)
                clearUponHandler(43)
                sendToLabel(0)
    sprite('null', 20)
    GFX_0('weakstart00', -1)
    Unknown1099(-25)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    Unknown3004(-27)
    Unknown1099(300)

@State
def weakstart00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sprite('null', 5)
    sprite('null', 30)
    GFX_2('azef_weakhit_02')

@Subroutine
def CheckCrouchGuardCrash():
    if Unknown23166('CmnActCrouchGuardPre'):
        SLOT_57 = 1
    if Unknown23166('CmnActCrouchGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActCrouchHeavyGuardLoop'):
        SLOT_57 = 1

@State
def azef_203_atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(1400)
        AttackP1(80)
        AirPushbackY(-20000)
        AirHitstunAnimation(11)
        Unknown9154(23)
        PushbackX(19800)
        HitOverhead(2)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        JumpCancel_(1)
        HitOrBlockCancel('NmlAtk5A4th')
        Unknown9190(1)
        Unknown11109('01000000')
        Unknown23078(1)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('4e6d6c41746b3541337264000000000000000000000000000000000000000000f007000000000000')

        def upon_43():
            if (SLOT_48 == 2031):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            callSubroutine('CheckCrouchGuardCrash')
            if SLOT_57:
                Unknown11001(0, 0, 5)
                Damage(1500)
                Hitstop(15)
                GroundedHitstunAnimation(2)
                Unknown9130(48)
                Unknown9142(36)
                AirUntechableTime(60)
                AirPushbackY(-30000)
                Unknown9190(1)
                ScreenShake(32000, 32000)
                GFX_0('weakhit00', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
            else:
                ScreenShake(4000, 4000)
                Unknown7007('62617a3231305f3000000000000000006400000062617a3231305f3100000000000000006400000062617a3231305f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az203_07', 3)
    Unknown3038(1)

@State
def azef_253_atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(1200)
        AirUntechableTime(30)
        AirPushbackX(36000)
        AirPushbackY(-36000)
        HitOverhead(2)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        Unknown11109('01000000')
        Unknown23078(1)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('4e6d6c41746b4149523542000000000000000000000000000000000000000000e409000000000000')

        def upon_43():
            if (SLOT_48 == 2531):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            callSubroutine('CheckCrouchGuardCrash')
            if SLOT_57:
                Damage(1300)
                Hitstop(15)
                AirUntechableTime(60)
                GroundedHitstunAnimation(2)
                Unknown9130(48)
                Unknown9142(32)
                AirHitstunAnimation(9)
                Unknown9190(1)
                Unknown9118(40)
                AirPushbackX(24000)
                AirPushbackY(-36000)
                ScreenShake(32000, 32000)
                GFX_0('weakhit00', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
            else:
                ScreenShake(4000, 4000)
                Unknown7007('62617a3231305f3000000000000000006400000062617a3231305f3100000000000000006400000062617a3231305f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az253_08', 5)
    Unknown3038(1)

@State
def azef_404_atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1800)
        AttackP1(80)
        AirPushbackX(60000)
        AirPushbackY(15000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(60)
        HitOverhead(2)
        PushbackX(66800)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        Unknown30065(0)
        Unknown11109('01000000')
        Unknown23078(1)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('56616e697368696e6741747461636b0000000000000000000000000000000000cb0f000000000000')

        def upon_43():
            if (SLOT_48 == 4042):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            SFX_0('025_cleanhit_grap')
            callSubroutine('CheckCrouchGuardCrash')
            if SLOT_57:
                Damage(1900)
                AirHitstunAnimation(12)
                GroundedHitstunAnimation(12)
                Unknown9178(1)
                Unknown9346(1)
                Unknown9362(1)
                Unknown9364(30)
                AirHitstunAfterWallbounce(30)
                AirPushbackX(35000)
                AirPushbackY(1000)
                YImpluseBeforeWallbounce(20)
                SFX_3('azse_05')
                ScreenShake(4000, 4000)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
                Unknown21015('56616e697368696e6741747461636b0000000000000000000000000000000000ce0f000000000000')
            else:
                ScreenShake(4000, 4000)
                Unknown7007('62617a3231305f3000000000000000006400000062617a3231305f3100000000000000006400000062617a3231305f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az404_06', 3)
    Unknown3038(1)
    sprite('az404_07', 3)
    Unknown3038(1)
    sprite('az404_08', 3)
    Unknown3038(1)

@State
def azef_404_atk_MAX():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1800)
        AttackP1(80)
        AirPushbackX(60000)
        AirPushbackY(15000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(60)
        HitOverhead(2)
        PushbackX(66800)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        Unknown30065(0)
        Unknown11109('01000000')
        Unknown23078(1)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('56616e697368696e6741747461636b0000000000000000000000000000000000cd0f000000000000')

        def upon_43():
            if (SLOT_48 == 4044):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            SFX_0('025_cleanhit_grap')
            callSubroutine('CheckCrouchGuardCrash')
            if SLOT_57:
                Damage(1900)
                AirHitstunAnimation(12)
                GroundedHitstunAnimation(12)
                Unknown9178(1)
                Unknown9346(1)
                Unknown9362(1)
                Unknown9364(30)
                AirHitstunAfterWallbounce(30)
                AirPushbackX(35000)
                AirPushbackY(1000)
                YImpluseBeforeWallbounce(20)
                SFX_3('azse_05')
                ScreenShake(4000, 4000)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
                Unknown21015('56616e697368696e6741747461636b0000000000000000000000000000000000ce0f000000000000')
            else:
                ScreenShake(4000, 4000)
                Unknown7007('62617a3231305f3000000000000000006400000062617a3231305f3100000000000000006400000062617a3231305f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az404_06', 3)
    Unknown3038(1)
    sprite('az404_07', 3)
    Unknown3038(1)
    sprite('az404_08', 3)
    Unknown3038(1)

@Subroutine
def CheckStandGuardCrash():
    if Unknown23166('CmnActMidGuardPre'):
        SLOT_57 = 1
    if Unknown23166('CmnActMidGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActMidHeavyGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActHighGuardPre'):
        SLOT_57 = 1
    if Unknown23166('CmnActHighGuardLoop'):
        SLOT_57 = 1
    if Unknown23166('CmnActHighHeavyGuardLoop'):
        SLOT_57 = 1

@State
def azef_233_atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(90)
        HitLow(2)
        Unknown9154(25)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(-2000)
        AirPushbackY(10000)
        AirUntechableTime(40)
        JumpCancel_(0)
        PushbackX(15300)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        Unknown11061(1)
        Unknown23078(1)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('4e6d6c41746b32420000000000000000000000000000000000000000000000001b09000000000000')

        def upon_43():
            if (SLOT_48 == 2332):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            callSubroutine('CheckStandGuardCrash')
            if SLOT_57:
                Damage(1300)
                Hitstop(15)
                AirPushbackY(6000)
                GroundedHitstunAnimation(11)
                Unknown9310(10)
                GFX_0('weakhit01', -1)
                ScreenShake(32000, 32000)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
            else:
                ScreenShake(8000, 8000)
                Unknown7007('62617a3231315f3000000000000000006400000062617a3231315f3100000000000000006400000062617a3231315f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az233_03', 3)
    Unknown3038(1)

@State
def azef_234_atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(1400)
        AttackP1(90)
        AirPushbackX(8000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(8000)
        AirUntechableTime(40)
        HitLow(2)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        JumpCancel_(0)
        Unknown11061(1)
        Unknown23078(1)
        Unknown11084(1)
        Unknown9202(1)
        Unknown9310(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('4e6d6c41746b32430000000000000000000000000000000000000000000000002509000000000000')

        def upon_43():
            if (SLOT_48 == 2342):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            callSubroutine('CheckStandGuardCrash')
            if SLOT_57:
                Damage(1500)
                AirPushbackY(-36000)
                Unknown9095()
                Hitstop(15)
                AirUntechableTime(60)
                Unknown9190(1)
                ScreenShake(32000, 32000)
                GFX_0('weakhit01', -1)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_02')
                Unknown9202(0)
                Unknown9310(0)
            else:
                Unknown7007('62617a3231315f3000000000000000006400000062617a3231315f3100000000000000006400000062617a3231315f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az234_03', 3)
    Unknown3038(1)
    sprite('az234_04', 3)
    Unknown3038(1)

@State
def azef_403_atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(90)
        AirPushbackX(6000)
        AirPushbackY(27000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        HitLow(2)
        PushbackX(50000)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        Unknown30065(0)
        Unknown11061(1)
        Unknown23078(1)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('4475737441747461636b00000000000000000000000000000000000000000000c90f000000000000')

        def upon_43():
            if (SLOT_48 == 4042):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            SFX_0('025_cleanhit_grap')
            callSubroutine('CheckStandGuardCrash')
            if SLOT_57:
                Damage(1600)
                AttackLevel_(4)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(65)
                AirPushbackX(5000)
                AirPushbackY(40000)
                YImpluseBeforeWallbounce(750)
                SFX_3('azse_05')
                Unknown21015('4475737441747461636b00000000000000000000000000000000000000000000cd0f000000000000')
                ScreenShake(8000, 8000)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
            else:
                ScreenShake(8000, 8000)
                Unknown7007('62617a3231315f3000000000000000006400000062617a3231315f3100000000000000006400000062617a3231315f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az403_09', 5)
    Unknown3038(1)

@State
def azef_403_atk_MAX():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(90)
        AirPushbackX(6000)
        AirPushbackY(27000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        HitLow(2)
        PushbackX(50000)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11034(1)
        Unknown11033(0)
        Unknown30065(0)
        Unknown11061(1)
        Unknown23078(1)
        Unknown11084(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('4475737441747461636b00000000000000000000000000000000000000000000cb0f000000000000')

        def upon_43():
            if (SLOT_48 == 4044):
                Unknown2003(1)

        def upon_78():
            clearUponHandler(78)
            SFX_0('025_cleanhit_grap')
            callSubroutine('CheckStandGuardCrash')
            if SLOT_57:
                Damage(1600)
                AttackLevel_(4)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(65)
                AirPushbackX(5000)
                AirPushbackY(40000)
                YImpluseBeforeWallbounce(750)
                SFX_3('azse_05')
                Unknown21015('4475737441747461636b00000000000000000000000000000000000000000000cd0f000000000000')
                ScreenShake(8000, 8000)
                Unknown7007('62617a3231325f3000000000000000006400000062617a3231325f3100000000000000006400000062617a3231325f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
            else:
                ScreenShake(8000, 8000)
                Unknown7007('62617a3231315f3000000000000000006400000062617a3231315f3100000000000000006400000062617a3231315f320000000000000000640000000000000000000000000000000000000000000000')
                SFX_3('azse_01')
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('az403_09', 5)
    Unknown3038(1)

@State
def __203swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(900)
    sprite('null', 14)
    GFX_0('203yugami', -1)
    Unknown4003('617a65665f3230337377696e6730302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def __203yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(-25000)
        Unknown1096(900)
    sprite('vr_azef203_yugami', 15)
    Unknown3057(1)
    Unknown3058(35000)
    Unknown3059(-2500)

@State
def __213swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(255)
        Unknown1096(900)
    sprite('null', 14)
    GFX_0('213yugami', -1)
    Unknown4003('617a65665f3231337377696e6730302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def __213yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(-25000)
        Unknown1096(900)
    sprite('vr_azef213_yugami', 15)
    Unknown3057(1)
    Unknown3058(35000)
    Unknown3059(-2500)

@State
def __213rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('617a65665f343032726f636b2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1000)
        teleportRelativeX(-20000)
        Unknown1007(15000)
    sprite('null', 5)
    sprite('null', 10)
    Unknown4049(700)
    Unknown4045('617a65665f343032726f636b736d6f6b655f706f730000000000000000000000ffffffff')
    sprite('null', 5)
    Unknown3004(-51)

@State
def __232rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1500)
        teleportRelativeX(400000)
        Unknown4003('617a65665f323332726f636b30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)
    Unknown1007(-40000)
    ScreenShake(5000, 5000)
    sprite('null', 2)
    Unknown1007(40000)
    sprite('null', 2)
    Unknown3001(0)
    GFX_0('232rock01', -1)
    sprite('null', 4)
    GFX_0('232rock02', -1)
    sprite('null', 2)
    GFX_0('232rock03', -1)
    sprite('null', 20)
    GFX_0('232rock04', -1)

@State
def __232rock01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1500)
        Unknown4003('617a65665f323332726f636b30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 2)

@State
def __232rock02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1500)
        Unknown4003('617a65665f323332726f636b30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)

@State
def __232rock03():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1500)
        teleportRelativeX(-150000)
        Unknown1007(-5000)
        Unknown4003('617a65665f323332726f636b30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('azef_rockshadow_00')
    sprite('null', 2)

@State
def __232rock04():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1500)
        teleportRelativeX(-150000)
        Unknown1007(-5000)
        Unknown4003('617a65665f323332726f636b30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('azef_rockshadow_00')
    sprite('null', 5)
    GFX_1('azef_232brokerock_rock2', -1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __232rock_col():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(1200)
        AttackP1(90)
        AttackP2(70)
        Unknown11033(1)
        Unknown11034(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9154(22)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        AirPushbackX(8800)
        AirPushbackY(35000)
        Unknown3038(1)
        Unknown23078(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Unknown9178(1)
            Unknown9362(1)
            Unknown9364(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                Unknown1017()
        Unknown23089('0100000001000000010000000000000001000000000000000100000001000000')

        def upon_54():
            sendToLabel(580)
        Unknown2037(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('4e6d6c41746b32410000000000000000000000000000000000000000000000001109000000000000')
    sprite('null', 5)
    sprite('vr_azef232_00col', 4)
    sprite('vr_azef232_01col', 2)
    label(580)
    sprite('null', 2)

@State
def __253swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(255)
        Unknown1096(900)
    sprite('null', 6)
    Unknown4003('617a65665f3235337377696e6730302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def __255swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(0)
        Unknown1007(230000)
    sprite('null', 3)
    sprite('null', 3)
    Unknown3001(255)
    Unknown4003('617a65665f3235357377696e6730302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def azef_409_fall():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('azef_409punch')
    label(0)
    sprite('null', 2)
    GFX_1('azef_409punch_add', -1)
    gotoLabel(0)

@State
def azef_409_rock():

    def upon_IMMEDIATE():
        Unknown4003('617a65665f3430366a69776172652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1750)
        teleportRelativeY(50000)
        teleportRelativeX(100000)
    sprite('null', 5)
    GFX_0('azef_409_hibiware', -1)
    Unknown4049(845)
    Unknown4045('617a65665f3430365f73746f6e65000000000000000000000000000000000000ffffffff')
    sprite('null', 20)
    Unknown3004(-10)

@State
def azef_409_hibiware():

    def upon_IMMEDIATE():
        Unknown4003('617a65665f68696269776172652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1500)
        teleportRelativeY(100000)
        Unknown23015(2)
    sprite('null', 4)
    sprite('null', 8)
    Unknown3004(-26)

@State
def __405smoke():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
    GFX_1('azef_405tossin_smoke', -1)
    label(0)
    sprite('null', 1)
    GFX_1('azef_405tossin', -1)
    gotoLabel(0)

@State
def __405punch():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(255)
        Unknown1096(800)
    sprite('null', 15)
    Unknown4003('617a65665f34303570756e636830302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()

@State
def __400impact():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('617a65665f343030696d7061637430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1007(280000)
        teleportRelativeX(200000)
        Unknown3001(255)
        Unknown1096(1700)
    sprite('null', 10)
    GFX_1('azef_400impact_pos', -1)
    GFX_0('400yugami', -1)
    sprite('null', 5)

@State
def __400yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1200)
        teleportRelativeX(30000)
        Unknown1007(15000)
    sprite('vr_azef400_yugami', 15)
    Unknown3057(1)
    Unknown3058(50000)
    Unknown3059(-3000)

@State
def __401swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('617a65665f343031696d7061637430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1096(1700)
        Unknown3001(200)
    sprite('null', 10)
    sprite('null', 5)

@State
def __402rock1():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('617a65665f343032726f636b2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1500)
        teleportRelativeX(-20000)
        Unknown1007(15000)
    sprite('null', 5)
    sprite('null', 10)
    GFX_1('azef_402rocksmoke_pos', -1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __402swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('617a65665f3430327377696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1096(1000)
        Unknown3001(255)
        Unknown1007(300000)
        teleportRelativeX(100000)
    sprite('null', 14)

@State
def __407aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3038(1)
        Unknown4003('617a65665f6175726130300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    label(1)
    sprite('vr_azef407_efpos00', 1)
    GFX_0('407yugami', -1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000000000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000001000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000002000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    GFX_0('407boya2', 2)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    GFX_0('407boya2', 5)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000006000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000007000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000008000000')
    GFX_0('407boya2', 8)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000009000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000a000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000b000000')
    GFX_0('407boya2', 11)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000c000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000d000000')
    GFX_0('407boya2', 13)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000e000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000f000000')
    GFX_0('407boya2', 15)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000010000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000011000000')
    GFX_0('407boya2', 17)
    sprite('vr_azef407_efpos00', 5)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000012000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000013000000')
    GFX_0('407boya2', 19)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000000000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000001000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000002000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    GFX_0('407boya', 1)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    GFX_0('407boya', 2)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000006000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000007000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000008000000')
    GFX_0('407boya', 7)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000009000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000a000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000b000000')
    GFX_0('407boya', 8)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000c000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000d000000')
    GFX_0('407boya', 11)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000e000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000f000000')
    GFX_0('407boya', 14)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000010000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000011000000')
    GFX_0('407boya', 16)
    sprite('vr_azef407_efpos00', 5)
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000012000000')
    Unknown4054(12)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000013000000')
    GFX_0('407boya', 18)
    gotoLabel(1)
    label(0)
    sprite('vr_azef407_efpos00', 5)
    Unknown3004(-51)

@State
def __407boya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(500)
        Unknown4003('617a65665f6175726130310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(11)
        Unknown3001(0)
    sprite('null', 19)
    Unknown3004(26)
    Unknown1067(20)
    Unknown1070(-300, 500)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __407boya2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(500)
        Unknown4003('617a65665f6175726130310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(11)
        Unknown2005()
        Unknown3001(0)
    sprite('null', 19)
    Unknown3004(26)
    Unknown1067(20)
    Unknown1070(-300, 500)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __407yugami():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(180000)
        teleportRelativeX(40000)
    sprite('vr_azef407_yugami', 60)
    Unknown1099(10)
    physicsYImpulse(-2000)
    Unknown3004(-9)
    Unknown3057(1)
    Unknown3058(10000)
    Unknown3059(-1500)

@State
def __407Kyushu():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(250000)
        teleportRelativeX(140000)
        Unknown1096(1300)
    sprite('null', 25)
    GFX_2('azef_407kyushu_tubusub')
    SFX_0('022_magiccircle_b')

@State
def __408sphere():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1007(230000)
        teleportRelativeX(20000)
        Unknown4003('617a65665f34303874616d6100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
        Unknown2010()
        AttackLevel_(3)
        AttackP1(80)
        Unknown11033(2)
        Damage(1800)
        AirUntechableTime(30)
        AirPushbackX(54000)
        AirPushbackY(18000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown9015(1)
        Hitstop(3)
        sendToLabelUpon(10, 580)
        Unknown4011(3)
        Unknown3038(1)
        GFX_2('azef_408_ambient00')

        def upon_43():
            if (SLOT_48 == 4081):
                AttackLevel_(3)
                Unknown11033(2)
                Damage(1800)
                AirUntechableTime(40)
                AirPushbackX(54000)
                AirPushbackY(18000)
                GroundedHitstunAnimation(18)
                AirHitstunAnimation(18)
                Unknown9178(1)
                WallbounceReboundTime(1)
            if (SLOT_48 == 4089):
                Unknown2037(1)
            if (SLOT_48 == 4082):
                Unknown2037(1)
                AttackP1(70)
                Unknown11042(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Unknown9178(1)
            Unknown9362(1)
            Unknown9364(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(12)
                AirHitstunAnimation(12)
                Unknown1017()
    label(0)
    sprite('vr_azef408_col', 1)
    StartMultihit()
    teleportRelativeX(60000)
    sprite('vr_azef408_col', 1)
    if SLOT_2:
        GuardPoint_(1)
        Unknown22019('0000000000000000000000000100000000000000')
        Unknown22032(1)
        Unknown23142(1)
    sprite('vr_azef408_col', 7)
    Unknown22006(0)
    sprite('vr_azef408_col', 1)
    GFX_0('408JizokuSmoke', -1)
    Unknown3004(51)
    RefreshMultihit()
    sprite('vr_azef408_col', 3)
    physicsXImpulse(80000)
    gotoLabel(9)
    label(9)
    sprite('vr_azef408_col', 4)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    label(580)
    sprite('vr_azef408_col', 5)
    Unknown26('408JizokuSmoke')
    physicsXImpulse(0)
    GFX_1('azef_408_brake_tubu', -1)
    sprite('vr_azef408_col', 5)
    Unknown3004(-51)

@State
def __408sphereStart():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown1007(230000)
        teleportRelativeX(130000)
    sprite('null', 5)
    GFX_1('azef_407kyushu_tubusub', -1)
    sprite('null', 8)
    GFX_2('azef_408_sub')
    Unknown1099(30)
    physicsXImpulse(1500)

@State
def __408JizokuSmoke():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 2)
    GFX_1('azef_408_jizokuaura_tubu', -1)
    gotoLabel(0)

@State
def __408sphereJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('617a65665f34303874616d6132000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1077(-5000, 5000)
        Unknown1011(-15000, 15000)
        Unknown1102(0, 2500)
        Unknown1064(1500)
        Unknown1056(2000)
        Unknown3001(255)
    sprite('null', 7)
    Unknown1067(-30)
    Unknown3004(-37)

@State
def az406_dummy2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(900)
        AirPushbackX(1000)
        AirPushbackY(26000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9015(1)
        Hitstop(3)
        Unknown3038(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Unknown9178(1)
            Unknown9362(1)
            Unknown9364(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(12)
                AirHitstunAnimation(12)
                Unknown1017()
    sprite('null', 2)
    sprite('vr_azef406_col', 3)

@State
def rocktest():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(2000)
        teleportRelativeY(0)
    sprite('null', 1)
    sprite('null', 0)
    GFX_0('hibiware', -1)
    ScreenShake(8000, 8000)
    sprite('null', 5)
    Unknown4003('617a65665f3430366a69776172652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_1('azef_406_stone', -1)
    sprite('null', 5)
    Unknown3004(-10)
    sprite('null', 14)

@State
def hibiware():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1500)
        teleportRelativeY(0)
    sprite('null', 4)
    Unknown4003('617a65665f68696269776172652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)
    Unknown3004(-26)

@State
def az406_dummy():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(100)
        AttackP2(80)
        AirPushbackX(-3000)
        AirPushbackY(23000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9015(1)
        Hitstop(3)
        Unknown3038(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Unknown9178(1)
            Unknown9362(1)
            Unknown9364(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(12)
                AirHitstunAnimation(12)
                Unknown1017()
    sprite('null', 2)
    sprite('vr_azef406_col', 3)

@State
def az406_dummy_5B3rd():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        AttackP1(100)
        AirPushbackY(22000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9015(1)
        Unknown3038(1)
        Unknown23078(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Unknown9178(1)
            Unknown9362(1)
            Unknown9364(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(12)
                AirHitstunAnimation(12)
                Unknown1017()
    sprite('null', 5)
    sprite('vr_azef406_col', 3)

@State
def __404tame():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('azef_404tame_addcircle')
        Unknown1007(250000)
        teleportRelativeX(-50000)

        def upon_43():
            if (SLOT_48 == 4041):
                clearUponHandler(43)
                sendToLabel(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __404swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617a65665f3430347377696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(250000)
        teleportRelativeX(250000)
        Unknown3001(0)
    sprite('null', 1)
    sprite('null', 1)
    Unknown3001(255)
    GFX_1('azef_blood_01', -1)
    sprite('null', 1)
    sprite('null', 1)
    GFX_1('azef_blood_01', -1)
    sprite('null', 1)
    sprite('null', 8)
    GFX_1('azef_blood_01', -1)

@State
def __404nigiyakasi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(250000)
        teleportRelativeX(250000)
    sprite('null', 5)
    GFX_2('azef_404impact_thunder')
    sprite('null', 10)
    Unknown3004(-26)

@State
def azef_dustattack_hold():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)
    GFX_1('azef_dustattack_hold', -1)
    gotoLabel(0)

@State
def __403swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('617a65665f3430337377696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1096(700)
        Unknown3001(255)
    sprite('null', 14)
    GFX_1('azef_403backadd_00', -1)
    GFX_0('403yugami', -1)

@State
def __403yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(230000)
        teleportRelativeX(55000)
    sprite('vr_azef403_yugami', 15)
    Unknown3057(1)
    Unknown3058(40000)
    Unknown3059(-2500)

@State
def __431swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('617a65665f3433317377696e67303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(160000)
        teleportRelativeX(350000)
        Unknown1096(2000)
    sprite('null', 10)
    GFX_0('431yugami', -1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431yugami():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
    sprite('vr_azef431_yugami', 15)
    Unknown1099(10)
    physicsYImpulse(-2000)
    Unknown3004(-9)
    Unknown3057(1)
    Unknown3058(30000)
    Unknown3059(-1500)

@State
def __431ODAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 4311):
                clearUponHandler(43)
                sendToLabel(0)
        Unknown4003('617a65665f343331617572612e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        Unknown1096(950)
    sprite('null', 10)
    GFX_0('431Odaura', -1)
    Unknown3004(17)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    Unknown3004(0)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000000000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000001000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000002000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000006000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000007000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000008000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000009000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000a000000')
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000b000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000d000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000e000000')
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 10)
    Unknown21015('3433314f64617572610000000000000000000000000000000000000000000000d810000000000000')
    Unknown3004(-51)

@State
def __431Odaura():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3001(170)

        def upon_43():
            if (SLOT_48 == 4311):
                clearUponHandler(43)
                sendToLabel(0)
        Unknown2019(100)
    sprite('null', 5)
    label(1)
    sprite('vr_azef431_00', 3)
    sprite('vr_azef431_01', 3)
    sprite('vr_azef431_02', 3)
    gotoLabel(1)
    label(0)
    sprite('vr_azef431_00', 3)
    Unknown3004(-26)
    sprite('vr_azef431_01', 3)
    sprite('vr_azef431_02', 3)

@State
def __430HandAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown23015(2)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 0)
    GFX_1('azef_408handaura_add', 1)
    GFX_0('430Hand01', 0)
    GFX_0('430Hand01', 1)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 2)
    GFX_1('azef_408handaura_add', 3)
    GFX_0('430Hand01', 2)
    GFX_0('430Hand01', 3)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 4)
    GFX_1('azef_408handaura_add', 5)
    GFX_0('430Hand01', 4)
    GFX_0('430Hand01', 5)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 6)
    GFX_1('azef_408handaura_add', 7)
    GFX_0('430Hand01', 6)
    GFX_0('430Hand01', 7)
    sprite('vr_azef430_efpos00', 2)
    GFX_1('azef_408handaura_add', 8)
    GFX_1('azef_408handaura_add', 9)
    GFX_0('430Hand01', 8)
    GFX_0('430Hand01', 9)
    sprite('vr_azef430_efpos00', 2)
    GFX_1('azef_408handaura_add', 10)
    GFX_1('azef_408handaura_add', 11)
    GFX_0('430Hand01', 10)
    GFX_0('430Hand01', 11)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 12)
    GFX_1('azef_408handaura_add', 13)
    GFX_0('430Hand01', 12)
    GFX_0('430Hand01', 13)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 14)
    GFX_1('azef_408handaura_add', 15)
    GFX_0('430Hand01', 14)
    GFX_0('430Hand01', 15)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 16)
    GFX_1('azef_408handaura_add', 17)
    GFX_0('430Hand01', 16)
    GFX_0('430Hand01', 17)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 18)
    GFX_1('azef_408handaura_add', 19)
    GFX_0('430Hand01', 18)
    GFX_0('430Hand01', 19)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 20)
    GFX_1('azef_408handaura_add', 21)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 22)
    GFX_1('azef_408handaura_add', 23)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 24)
    sprite('vr_azef430_efpos00', 7)
    GFX_1('azef_408handaura_add', 25)
    GFX_1('azef_408handaura_add', 26)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 27)
    GFX_1('azef_408handaura_add', 28)

@State
def __430BodyAura():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(2)
    sprite('vr_azef430_efpos01', 3)
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    Unknown4054(12)
    Unknown4045('617a65665f34303868616e64617572615f6164640000000000000000000000006a000000')
    sprite('vr_azef430_efpos01', 3)
    GFX_0('430Hand02', 0)
    GFX_0('430Hand02', 1)
    GFX_0('430Hand02', 2)
    GFX_0('430Hand02', 3)
    GFX_0('430Hand02', 4)
    GFX_0('430Hand02', 5)
    GFX_0('430Hand02', 6)
    GFX_0('430Hand02', 7)

@State
def __430Hand01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(400)
        Unknown4003('617a65665f6175726130310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 19)
    Unknown1099(10)
    Unknown1077(-45000, 45000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __430Hand02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(400)
        Unknown4003('617a65665f6175726130310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 5)
    sprite('null', 14)
    Unknown3004(26)
    Unknown1099(10)
    Unknown1077(-45000, 45000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __430aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 4301):
                clearUponHandler(43)
                sendToLabel(0)
    label(1)
    sprite('vr_azef430_efpos02', 2)
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000000000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000001000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000002000000')
    GFX_0('407boya', 0)
    GFX_0('430boya', 1)
    GFX_0('407boya', 2)
    sprite('vr_azef430_efpos02', 2)
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    GFX_0('407boya', 3)
    GFX_0('430boya', 4)
    GFX_0('407boya', 5)
    sprite('vr_azef430_efpos02', 2)
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000006000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000007000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000008000000')
    GFX_0('430boya', 6)
    GFX_0('407boya', 7)
    GFX_0('407boya2', 8)
    sprite('vr_azef430_efpos02', 3)
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000009000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000a000000')
    Unknown4054(2)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000b000000')
    GFX_0('407boya', 9)
    GFX_0('430boya', 10)
    GFX_0('407boya', 11)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    Unknown3004(-51)

@State
def __430boya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(500)
        Unknown4003('617a65665f6175726130310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(12)
        Unknown3001(0)
    sprite('null', 19)
    Unknown3004(26)
    Unknown1067(20)
    Unknown1070(500, 1000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __430Atk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('617a65665f34333073686f636b303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(200000)
        teleportRelativeX(200000)
        Unknown1096(300)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    Unknown1099(50)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    sprite('null', 4)
    ScreenShake(6000, 6000)
    Unknown1099(5)
    sprite('null', 4)
    ScreenShake(6000, 6000)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    Unknown3004(-51)
    Unknown1099(-90)

@State
def __430shock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('617a65665f34333073686f636b303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(200000)
        teleportRelativeX(200000)
        Unknown23015(2)
    sprite('null', 5)
    ScreenShake(3000, 3000)
    GFX_0('430shock01', -1)
    GFX_0('430Speed', -1)
    sprite('null', 5)
    Unknown3004(-26)
    sprite('null', 10)
    Unknown21015('3433305370656564000000000000000000000000000000000000000000000000ce10000000000000')
    sprite('null', 15)

@State
def __430shock01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown23015(2)
    sprite('null', 45)
    GFX_2('azef_408_tukihit_add2')

@State
def __430Speed():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 4302):
                clearUponHandler(43)
                sendToLabel(0)
    sprite('null', 32767)
    GFX_2('azef_408_speedline_down')
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def BrustDD_SlashEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4061(1)
        Unknown2005()
        Unknown1056(900)
        Unknown1064(1100)
        Unknown3001(255)
        Unknown1007(100000)
        teleportRelativeX(-100000)
        Unknown3032()
    sprite('vr_azef440_00', 4)
    sprite('vr_azef440_01', 4)
    sprite('vr_azef440_02', 4)
    sprite('vr_azef440_03', 5)
    Unknown3004(-51)

@State
def BrustDD_SlashEff2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown2005()
        Unknown1007(250000)
        teleportRelativeX(-180000)
        Unknown4007(2)
        Unknown3029(1)
        Unknown21010(1)
    sprite('vr_azef440_10', 6)
    Unknown1096(1200)
    sprite('vr_azef440_11', 5)
    Unknown1096(1400)
    Unknown21010(0)
    sprite('vr_azef440_12', 12)
    Unknown1096(1500)
    Unknown1099(20)
    sprite('vr_azef440_13', 4)
    GFX_1('azef_440brust_00', -1)
    sprite('vr_azef440_14', 4)
    Unknown3004(-51)

@State
def BrustDD_SlashEff3():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown2005()
        Unknown1007(290000)
        Unknown4007(2)
        Unknown21010(1)
        Unknown1096(1700)
    sprite('vr_azef440_20', 2)
    GFX_0('BrustDD_brust', -1)
    Unknown23015(11)
    sprite('vr_azef440_21', 2)
    sprite('vr_azef440_22', 2)
    teleportRelativeX(35000)
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(20000)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(150000)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-45000)
    Unknown23015(11)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-140000)
    Unknown23015(11)
    Unknown35()
    sprite('vr_azef440_22', 4)
    teleportRelativeX(35000)
    sprite('vr_azef440_23', 4)
    teleportRelativeX(35000)
    Unknown21010(0)
    sprite('vr_azef440_24', 4)
    teleportRelativeX(35000)
    sprite('vr_azef440_25', 4)
    teleportRelativeX(35000)
    Unknown3004(-26)
    sprite('vr_azef440_26', 5)
    teleportRelativeX(35000)

@State
def BrustDD_brust():

    def upon_IMMEDIATE():
        GFX_2('azef_440brust2_00')
        Unknown21010(1)
    sprite('null', 10)
    sprite('null', 50)
    Unknown21010(0)

@State
def BrustDD_EXeff():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown1096(1500)
        Unknown3033()
    sprite('vr_azef440_30', 2)
    sprite('vr_azef440_31', 2)
    sprite('vr_azef440_32', 8)
    sprite('vr_azef440_33', 3)
    sprite('vr_azef440_34', 3)
    sprite('vr_azef440_35', 3)
    Unknown3004(-26)
    sprite('vr_azef440_36', 3)
    sprite('vr_azef440_37', 3)

@State
def BrustDD_SlashEffEx():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4061(1)
        Unknown2005()
        Unknown1056(1300)
        Unknown1064(1560)
        Unknown3001(255)
        Unknown1007(10000)
        teleportRelativeX(-100000)
        Unknown3032()
    sprite('vr_azef440_00', 4)
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-10000)
    teleportRelativeX(-125000)
    Unknown1097(500)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-45000)
    teleportRelativeX(-125000)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-90000)
    teleportRelativeX(-125000)
    Unknown35()
    sprite('vr_azef440_01', 4)
    sprite('vr_azef440_02', 4)
    sprite('vr_azef440_03', 5)
    Unknown3004(-51)

@State
def BrustDD_EXeff2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown1096(1500)
        Unknown3033()
    sprite('vr_azef440_32', 8)
    sprite('vr_azef440_33', 3)
    sprite('vr_azef440_34', 3)
    sprite('vr_azef440_35', 3)
    Unknown3004(-26)
    sprite('vr_azef440_36', 3)
    sprite('vr_azef440_37', 3)

@State
def BrustDD_SlashEff2Ex():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown2005()
        Unknown1007(250000)
        teleportRelativeX(-180000)
        Unknown4007(2)
        Unknown3029(1)
        Unknown21010(1)
    sprite('vr_azef440_10', 6)
    Unknown1096(1400)
    sprite('vr_azef440_11', 5)
    Unknown1096(1700)
    Unknown21010(0)
    sprite('vr_azef440_12', 12)
    Unknown1096(1800)
    Unknown1099(40)
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(450000)
    Unknown1097(250)
    Unknown23015(6)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-450000)
    Unknown1097(500)
    Unknown23015(6)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(1800000)
    Unknown1097(500)
    Unknown23015(6)
    Unknown35()
    sprite('vr_azef440_13', 4)
    GFX_1('azef_440brust_01', -1)
    sprite('vr_azef440_14', 4)
    Unknown3004(-51)

@State
def BrustDD_SlashEff3Ex():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown2005()
        Unknown1007(290000)
        Unknown4007(2)
        Unknown21010(1)
        Unknown1096(2000)
    sprite('vr_azef440_20', 2)
    GFX_0('BrustDD_brust', -1)
    Unknown23015(11)
    sprite('vr_azef440_21', 2)
    sprite('vr_azef440_22', 2)
    teleportRelativeX(35000)
    sprite('vr_azef440_22', 4)
    teleportRelativeX(35000)
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(45000)
    Unknown1097(700)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(120000)
    Unknown1097(700)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-45000)
    Unknown23015(11)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-140000)
    Unknown23015(11)
    Unknown35()
    sprite('vr_azef440_23', 4)
    teleportRelativeX(35000)
    Unknown21010(0)
    sprite('vr_azef440_24', 4)
    teleportRelativeX(35000)
    sprite('vr_azef440_25', 4)
    teleportRelativeX(35000)
    Unknown3004(-26)
    sprite('vr_azef440_26', 5)
    teleportRelativeX(35000)

@State
def __440Aura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3038(1)
        sendToLabelUpon(32, 0)
        Unknown4003('617a65665f6175726130320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        Unknown1096(950)
    sprite('null', 5)
    Unknown3004(51)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    Unknown3004(0)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000000000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000001000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000002000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000006000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000007000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000008000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000009000000')
    sprite('vr_azef610_efpos00', 2)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 10)
    Unknown3004(-51)

@State
def __450neppaMatome():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(150000)
    sprite('null', 1)
    GFX_0('450neppa00', -1)
    GFX_1('azef_450neppa_circle', -1)
    sprite('null', 7)
    GFX_0('450neppa01', -1)
    sprite('null', 7)
    GFX_0('450neppa01', -1)
    sprite('null', 7)

@State
def __450neppa00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('617a65665f3435306e65707061303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
    sprite('null', 20)
    sprite('null', 7)
    Unknown3004(-51)

@State
def __450neppa01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('617a65665f3435306e65707061303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
    sprite('null', 7)
    sprite('null', 7)
    Unknown3004(-51)
endState()

@State
def nepparock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown2054(1)
        Unknown1096(2000)
        teleportRelativeX(160000)
        Unknown4003('617a65665f3430366a69776172652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 10)
    GFX_1('azef_406_stone', -1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __450swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4010(2)
        Unknown4003('617a65665f343030696d7061637430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(30000)
        Unknown3001(255)
        Unknown1064(3200)
        Unknown1056(2400)
        Unknown2005()
        Unknown1073(100000)
    sprite('null', 10)

@State
def __450rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('617a65665f726f636b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(280000)
    sprite('null', 6)
    GFX_0('450smoke', -1)
    Unknown36(22)
    Unknown1007(15000)
    setGravity(0)
    Unknown35()
    Unknown1073(3250)
    Unknown1007(70000)
    sprite('null', 50)
    Unknown1073(1625)
    Unknown1007(35000)
    Unknown36(22)
    Unknown1007(30000)
    Unknown35()
    sprite('null', 40)
    Unknown1073(812)
    Unknown1007(40000)
    Unknown36(22)
    Unknown1007(30000)
    Unknown35()
    sprite('null', 40)
    Unknown1073(406)
    Unknown1007(20000)
    Unknown36(22)
    Unknown1007(15000)
    Unknown35()
    sprite('null', 60)
    Unknown36(22)
    Unknown1007(15000)
    Unknown35()
    Unknown1073(203)
    Unknown1007(10000)
    sprite('null', 20)
    GFX_0('AHsection', -1)
    physicsYImpulse(60000)
    Unknown36(22)
    Unknown1007(15000)
    physicsYImpulse(100000)
    Unknown23015(2)
    Unknown35()

@State
def __450smoke():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown23015(4)
        Unknown1007(-30000)
        teleportRelativeX(-20000)
    sprite('null', 6)
    GFX_0('450smokeb', -1)
    Unknown4054(4)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f62727573740000000000000000ffffffff')
    sprite('null', 50)
    Unknown4054(4)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f73746f6e653200000000000000ffffffff')
    sprite('null', 40)
    Unknown4054(4)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f73746f6e653200000000000000ffffffff')
    sprite('null', 40)
    Unknown4054(4)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f73746f6e653200000000000000ffffffff')
    sprite('null', 60)
    Unknown4054(4)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f73746f6e653200000000000000ffffffff')

@State
def __450smokeb():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown23015(2)
        Unknown1007(-30000)
        teleportRelativeX(-20000)
    sprite('null', 6)
    Unknown4054(2)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f62627275737400000000000000ffffffff')
    sprite('null', 50)
    Unknown4054(2)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f62000000000000000000000000ffffffff')
    sprite('null', 40)
    Unknown4054(2)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f62000000000000000000000000ffffffff')
    sprite('null', 40)
    Unknown4054(2)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f62000000000000000000000000ffffffff')
    sprite('null', 60)
    Unknown4054(2)
    Unknown4045('617a65665f34353073746f6e65736d6f6b655f62000000000000000000000000ffffffff')

@State
def __450smokec():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown23015(2)
        Unknown1007(-100000)
        teleportRelativeX(300000)
        Unknown1096(1500)
        GFX_2('azef_utiagesmoke_02')
    sprite('null', 50)

@State
def IrezumiRay():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4007(2)
        Unknown4061(1)
        Unknown3001(0)
        Unknown1007(7000)
    sprite('vr_azef450_00', 20)
    Unknown3004(26)
    GFX_0('IrezumiRayLine', -1)
    sprite('vr_azef450_00', 30)
    Unknown3004(-26)

@State
def IrezumiRayLine():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4007(2)
        Unknown4061(1)
        Unknown3001(0)
    sprite('vr_azef450_01', 20)
    Unknown3004(26)
    sprite('vr_azef450_01', 20)
    Unknown3004(-13)

@State
def az450_dummy():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11064(3)
        AttackLevel_(5)
        Damage(44800)
        Unknown11091(100)
        Unknown11056(3)
        Unknown11071(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(10000)
        Unknown11023(1)
        Unknown1086(22)
        Unknown3038(1)
        Unknown1096(3000)
sprite('null', 7)
sprite('vr_azef450_col', 10)
Unknown11023(1)
sprite('az450cutin_01', 3000)
endState()

@State
def __450Cam():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown20000(1)
        Unknown1007(300000)
    sprite('null', 6)
    Unknown20009(990)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(980)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(970)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(960)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(950)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(940)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(930)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(920)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(910)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(900)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(890)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(880)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(870)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(860)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(850)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(840)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(830)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(820)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(810)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(800)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(790)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(780)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(770)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(760)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 4)
    Unknown20009(100)
    GFX_1('azef_ahanten05', -1)
    ScreenShake(1275, 1275)
    sprite('null', 11)
    Unknown20009(1000)
    Unknown1007(-800000)
    Unknown20000(0)

@State
def AHshadow():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahshadow_00')
        Unknown1007(300000)
    sprite('null', 165)

@State
def AHanten00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahanten01')
        Unknown23032(50)
    sprite('null', 90)

@State
def AHanten01():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahanten04')
    sprite('null', 90)

@State
def AHanten02():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_lastanten01')
        Unknown1007(300000)
        Unknown23032(50)
    sprite('null', 90)

@State
def AHsection():

    def upon_IMMEDIATE():
        Unknown4003('617a65665f73656374696f6e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 60)

@State
def AHSmoke():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahfinishbg03')
    sprite('null', 32767)

@State
def AHaura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3038(1)
        sendToLabelUpon(32, 0)
        Unknown4003('617a65665f6175726130320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000000000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000001000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000002000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000006000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000007000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000008000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000009000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000a000000')
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000b000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000d000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000e000000')
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    Unknown3004(-51)

@State
def __610aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3038(1)
        sendToLabelUpon(32, 0)
        Unknown4003('617a65665f3631306175726130300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000000000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000001000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000002000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000003000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000004000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000005000000')
    GFX_0('407boya', 1)
    GFX_0('407boya', 5)
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000006000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000007000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000008000000')
    Unknown4045('617a65665f3430376261636b617572615f30320000000000000000000000000009000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000a000000')
    GFX_0('407boya2', 6)
    GFX_0('407boya2', 9)
    GFX_0('407boya2', 10)
    sprite('vr_azef610_efpos00', 2)
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000b000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000d000000')
    Unknown4045('617a65665f3430376261636b617572615f3032000000000000000000000000000e000000')
    GFX_0('407boya2', 11)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    Unknown3004(-51)