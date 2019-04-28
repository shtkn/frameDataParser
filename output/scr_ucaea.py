@State
def __5A_Eff():

    def upon_IMMEDIATE():
        Unknown1096(1200)
    sprite('Action_074_00', 4)	# 1-4
    sprite('Action_074_01', 2)	# 5-6
    sprite('Action_074_02', 2)	# 7-8

@State
def __5AAA_Eff():

    def upon_IMMEDIATE():
        Unknown4009(3)
        teleportRelativeX(100000)
        Unknown23089('0000000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(0)
    sprite('Action_075_00', 2)	# 1-2
    sprite('Action_075_01', 2)	# 3-4
    SFX_3('SE_BloodCongeals')
    sprite('Action_075_02', 8)	# 5-12
    label(0)
    sprite('Action_075_03', 2)	# 13-14
    clearUponHandler(54)
    Unknown4009(0)
    sprite('Action_075_04', 2)	# 15-16
    sprite('Action_075_05', 2)	# 17-18

@State
def __5AAA_Eff_NPS():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4011(3)
        Unknown23089('0000000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(0)
    sprite('Action_075_00', 2)	# 1-2
    sprite('Action_075_01', 2)	# 3-4
    SFX_3('SE_BloodCongeals')
    sprite('Action_075_02', 6)	# 5-10
    sprite('Action_075_02', 2)	# 11-12
    Unknown4007(0)
    label(0)
    sprite('Action_075_03', 2)	# 13-14
    clearUponHandler(54)
    Unknown4009(0)
    sprite('Action_075_04', 2)	# 15-16
    sprite('Action_075_05', 2)	# 17-18

@State
def __5B_Eff():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4011(3)
        teleportRelativeX(-130000)
        Unknown23089('0000000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(0)
    sprite('Action_071_00', 2)	# 1-2
    sprite('Action_071_01', 4)	# 3-6
    SFX_3('SE_BloodCongeals')
    sprite('Action_071_02', 2)	# 7-8
    Unknown4007(0)
    label(0)
    sprite('Action_071_03', 2)	# 9-10
    clearUponHandler(54)
    Unknown4009(0)
    sprite('Action_071_04', 2)	# 11-12
    sprite('Action_071_05', 1)	# 13-13

@State
def __5BB_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(3)
        teleportRelativeX(-90000)
        Unknown23089('0000000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(0)
    sprite('Action_073_00', 2)	# 1-2
    sprite('Action_073_01', 7)	# 3-9
    SFX_3('SE_BloodCongeals')
    sprite('Action_073_02', 4)	# 10-13
    label(0)
    sprite('Action_073_03', 2)	# 14-15
    clearUponHandler(54)
    Unknown4009(0)
    sprite('Action_073_04', 2)	# 16-17
    sprite('Action_073_05', 1)	# 18-18

@State
def __5C_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(3)
        teleportRelativeX(-10000)
        Unknown23089('0000000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(0)
    sprite('Action_072_00', 2)	# 1-2
    sprite('Action_072_01', 7)	# 3-9
    SFX_3('SE_BloodCongeals')
    label(0)
    sprite('Action_072_02', 10)	# 10-19
    clearUponHandler(54)
    Unknown4009(0)
    sprite('Action_072_03', 2)	# 20-21
    sprite('Action_072_04', 2)	# 22-23
    sprite('Action_072_05', 2)	# 24-25

@State
def __6B_Eff():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        teleportRelativeX(65000)
        Unknown1007(252000)
        physicsXImpulse(50000)
        Unknown1028(1500)
        Unknown1072(90000)
        AttackLevel_(3)
        AttackP2(85)
        AirPushbackX(8000)
        AirPushbackY(9000)
        AirUntechableTime(32)
        Hitstop(4)
        Unknown11001(10, 10, 12)
        Unknown9016(1)
        Unknown23078(1)
        Unknown11050('0200000065665f6869746d6d5f7465737400000000000000000000000000000000000000')
        Unknown2034(1)

        def upon_7():
            clearUponHandler(7)
            Unknown23029(3, 1941, 0)
            Unknown1084(1)
            sendToLabel(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown23029(3, 1941, 0)
            Unknown1084(1)
            sendToLabel(1)
    sprite('Action_194_00', 1)	# 1-1
    SFX_3('SE_BloodSplashA')
    sprite('Action_194_01ex00', 255)	# 2-256	 **attackbox here**
    label(1)
    sprite('Action_194_01', 1)	# 257-257	 **attackbox here**
    GFX_0('6BEnd_Eff', -1)
    StartMultihit()
    ExitState()
    label(2)
    sprite('Action_194_01', 10)	# 258-267	 **attackbox here**
    GFX_0('6BEnd_Eff', -1)
    StartMultihit()
    ExitState()

@State
def __6BEnd_Eff():

    def upon_IMMEDIATE():
        Unknown1096(850)
        Unknown1072(90000)
    sprite('Action_196_00', 5)	# 1-5	 **attackbox here**
    SFX_3('SE017_BoundMinHigh')
    sprite('Action_196_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_196_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_196_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_196_04', 1)	# 21-21	 **attackbox here**

@State
def __6BB_Eff():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(2200)
        AttackP2(70)
        Unknown11092(1)
        AirUntechableTime(30)
        Unknown11028(18)
        AirPushbackX(2000)
        AirPushbackY(22000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9016(1)
        Unknown23182(3)
        Unknown2053(1)
        Unknown11099(1)
        Unknown2005()
        Unknown23078(1)
        teleportRelativeY(0)
    sprite('Action_215_00', 5)	# 1-5
    SFX_3('SE_BloodSplashB')
    sprite('Action_215_01', 7)	# 6-12	 **attackbox here**
    sprite('Action_215_02', 10)	# 13-22
    sprite('Action_215_03', 3)	# 23-25
    sprite('Action_215_04', 3)	# 26-28
    sprite('Action_215_05', 1)	# 29-29

@State
def __6B_PS_Eff():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        teleportRelativeX(65000)
        Unknown1007(252000)
        physicsXImpulse(40000)
        Unknown1028(1500)
        Unknown1072(90000)
        AttackLevel_(3)
        AttackP1(70)
        AirUntechableTime(25)
        Hitstop(0)
        Unknown11001(10, 10, 12)
        Unknown9016(1)
        Unknown11042(1)
        Unknown11050('0200000065665f6869746d6d5f7465737400000000000000000000000000000000000000')
        Unknown2034(1)

        def upon_7():
            clearUponHandler(7)
            Unknown1084(1)
            sendToLabel(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1084(1)
            sendToLabel(1)

        def upon_78():
            Unknown21015('436d6e4163744368616e6765506172746e657241737369737441746b5f4100009507000000000000')
        Unknown23089('0100000000000000000000000000000001000000000000000000000000000000')

        def upon_54():
            clearUponHandler(54)
            Unknown1084(1)
            sendToLabel(2)
    sprite('Action_194_00', 1)	# 1-1
    sprite('Action_194_01ex00', 255)	# 2-256	 **attackbox here**
    label(1)
    sprite('Action_194_01', 10)	# 257-266	 **attackbox here**
    GFX_0('6BEnd_Eff', -1)
    StartMultihit()
    enterState('BloodPool_B')
    ExitState()
    label(2)
    sprite('Action_194_01', 10)	# 267-276	 **attackbox here**
    GFX_0('6BEnd_Eff', -1)
    StartMultihit()
    ExitState()

@State
def __6BB_PS_Eff():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        AttackP1(70)
        AirUntechableTime(40)
        AirPushbackX(2000)
        AirPushbackY(35000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9016(1)
        Unknown11042(1)
        Unknown2053(1)
        Unknown11099(1)
        Unknown2005()
    sprite('Action_215_00', 5)	# 1-5
    sprite('Action_215_01', 7)	# 6-12	 **attackbox here**
    sprite('Action_215_02', 10)	# 13-22
    sprite('Action_215_03', 3)	# 23-25
    sprite('Action_215_04', 3)	# 26-28
    sprite('Action_215_05', 1)	# 29-29

@State
def __2A_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('Action_085_00', 4)	# 1-4
    sprite('Action_085_01', 2)	# 5-6
    sprite('Action_085_02', 2)	# 7-8

@State
def __2C_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(3)
        Unknown4007(3)
        Unknown23089('0000000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(0)
    sprite('Action_086_00', 2)	# 1-2
    sprite('Action_086_01', 3)	# 3-5
    SFX_3('SE_BloodCongeals')
    sprite('Action_086_01', 4)	# 6-9
    Unknown4007(0)
    sprite('Action_086_02', 3)	# 10-12
    label(0)
    sprite('Action_086_03', 2)	# 13-14
    clearUponHandler(54)
    Unknown4009(0)
    sprite('Action_086_04', 2)	# 15-16
    sprite('Action_086_05', 2)	# 17-18

@State
def __3C_Eff():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown23089('0000000000000000000000000000000000000000010000000000000000000000')

        def upon_54():
            sendToLabel(0)
    sprite('Action_084_00', 1)	# 1-1
    sprite('Action_084_01', 7)	# 2-8
    SFX_3('SE_BloodCongeals')
    sprite('Action_084_02', 3)	# 9-11
    sprite('Action_084_03', 2)	# 12-13
    clearUponHandler(54)
    Unknown4009(0)
    sprite('Action_084_04', 2)	# 14-15
    sprite('Action_084_05', 2)	# 16-17

@State
def JA_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-50000)
        Unknown1007(50000)
    sprite('Action_077_00', 3)	# 1-3
    sprite('Action_077_01', 3)	# 4-6
    sprite('Action_077_02', 2)	# 7-8
    sprite('Action_077_03', 2)	# 9-10

@State
def JB_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4011(3)

        def upon_43():
            if (SLOT_48 == 9981):
                Unknown13(25)
    sprite('Action_078_00', 2)	# 1-2
    loopRest()
    clearUponHandler(43)
    sprite('Action_078_01', 3)	# 3-5
    SFX_3('SE_BloodCongeals')
    sprite('Action_078_01', 4)	# 6-9
    Unknown4007(0)
    sprite('Action_078_03', 2)	# 10-11
    Unknown4009(0)
    sprite('Action_078_04', 2)	# 12-13
    sprite('Action_078_05', 2)	# 14-15

@State
def JC_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4011(3)

        def upon_43():
            if (SLOT_48 == 9981):
                Unknown13(25)

        def upon_3():
            if (SLOT_18 >= 3):
                clearUponHandler(43)
                clearUponHandler(3)
    sprite('Action_081_00', 7)	# 1-7
    SFX_3('SE_BloodCongeals')
    sprite('Action_081_01', 2)	# 8-9
    Unknown4009(0)
    Unknown4007(0)
    sprite('Action_081_02', 2)	# 10-11
    sprite('Action_081_03', 2)	# 12-13

@State
def JC_Burst_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4011(3)

        def upon_43():
            if (SLOT_48 == 9981):
                sendToLabel(1)
    sprite('Action_081_00', 32767)	# 1-32767
    SFX_3('SE_BloodCongeals')
    label(1)
    sprite('Action_081_01', 2)	# 32768-32769
    Unknown4009(0)
    Unknown4007(0)
    sprite('Action_081_02', 2)	# 32770-32771
    sprite('Action_081_03', 2)	# 32772-32773

@State
def J6B_Eff():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        teleportRelativeX(50000)
        Unknown1007(240000)
        physicsXImpulse(40000)
        physicsYImpulse(-40000)
        Unknown1028(400)
        setGravity(400)
        Unknown1072(135000)
        AttackLevel_(3)
        AttackP2(85)
        AirPushbackX(3000)
        AirPushbackY(-30000)
        AirUntechableTime(40)
        Hitstop(4)
        Unknown11028(13)
        Unknown11001(10, 10, 12)
        Unknown9016(1)
        Unknown23078(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown23029(3, 1911, 0)
            Unknown1084(1)
            sendToLabel(1)
        Unknown23026(50000)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown23029(3, 1911, 0)
            Unknown1084(1)
            sendToLabel(1)
        Unknown53(1)
        Unknown2055(300)
    sprite('Action_195_01ex00', 2)	# 1-2	 **attackbox here**
    SFX_3('SE_BloodSplashA')
    label(0)
    sprite('Action_195_01ex00', 1)	# 3-3	 **attackbox here**
    Hitstop(0)
    Unknown23078(0)
    gotoLabel(0)
    label(1)
    sprite('Action_195_01', 1)	# 4-4	 **attackbox here**
    GFX_0('J6BEnd_Eff', -1)
    StartMultihit()

@State
def J6BEnd_Eff():

    def upon_IMMEDIATE():
        Unknown1096(850)
        Unknown1072(135000)
    sprite('Action_196_00', 5)	# 1-5	 **attackbox here**
    SFX_3('SE017_BoundMinHigh')
    sprite('Action_196_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_196_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_196_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_196_04', 1)	# 21-21	 **attackbox here**

@State
def J6BB_Eff():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(2200)
        AttackP2(70)
        Unknown11092(1)
        AirUntechableTime(30)
        AirPushbackX(2000)
        AirPushbackY(22000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9016(1)
        Unknown23182(3)
        Unknown2053(1)
        Unknown11099(1)
        Unknown2005()
        Unknown23078(1)
        teleportRelativeY(0)
    sprite('Action_215_00', 5)	# 1-5
    SFX_3('SE_BloodSplashB')
    sprite('Action_215_01', 7)	# 6-12	 **attackbox here**
    sprite('Action_215_02', 10)	# 13-22
    sprite('Action_215_03', 3)	# 23-25
    sprite('Action_215_04', 3)	# 26-28
    sprite('Action_215_05', 1)	# 29-29

@State
def InvincibleAttack_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('Action_204_00', 3)	# 1-3
    SFX_3('SE_BloodSplashB')
    sprite('Action_204_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_204_02', 6)	# 7-12	 **attackbox here**
    sprite('Action_204_03', 6)	# 13-18	 **attackbox here**
    sprite('Action_204_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_204_05', 3)	# 22-24	 **attackbox here**
    sprite('Action_204_06', 3)	# 25-27	 **attackbox here**

@State
def InvincibleAttackEX_Eff():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
    sprite('Action_207_00', 2)	# 1-2
    SFX_3('SE_BloodSplashB')
    sprite('Action_207_01', 2)	# 3-4
    sprite('Action_207_02', 2)	# 5-6
    sprite('Action_207_03', 2)	# 7-8
    sprite('Action_207_04', 2)	# 9-10
    sprite('Action_207_05', 2)	# 11-12
    sprite('Action_207_06', 2)	# 13-14
    sprite('Action_207_07', 2)	# 15-16
    sprite('Action_207_08', 1)	# 17-17

@State
def ThrowExe_Eff():

    def upon_IMMEDIATE():
        Unknown23015(11)
        Unknown1096(1250)
        teleportRelativeX(75000)
        Unknown1007(-50000)
    sprite('Action_083_00', 3)	# 1-3
    sprite('Action_083_01', 3)	# 4-6
    SFX_3('SE_BloodCongeals')
    sprite('Action_083_02', 10)	# 7-16
    sprite('Action_083_03', 3)	# 17-19
    sprite('Action_083_04', 3)	# 20-22
    sprite('Action_083_05', 3)	# 23-25
    sprite('Action_083_06', 3)	# 26-28

@State
def RotationShot_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1200)
        AirHitstunAnimation(9)
        Unknown11092(1)
        AirPushbackY(22000)
        AirUntechableTime(24)
        Hitstop(3)
        Unknown11001(3, 3, 5)
        PushbackX(9800)
        Unknown9016(1)
        Unknown2053(1)
        Unknown23013(1)
        Unknown23015(11)
        teleportRelativeX(100000)
        Unknown1007(250000)

        def upon_3():
            if (SLOT_23 < 150000):
                teleportRelativeY(150000)
            if SLOT_51:
                if SLOT_52:
                    clearUponHandler(3)
                    sendToLabel(1)
            if 
            if (not (SLOT_53 == 4)):
                (SLOT_54 == 2):
                Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 1301):
                Unknown30070('526f746174696f6e53686f744c616e6441000000000000000000000000000000')
                setGravity(-2000)
            if (SLOT_48 == 1302):
                Unknown30070('526f746174696f6e53686f744c616e6442000000000000000000000000000000')
                setGravity(-2000)
                physicsXImpulse(35000)
            if (SLOT_48 == 1304):
                Unknown30070('526f746174696f6e53686f744169724100000000000000000000000000000000')
                setGravity(-1500)
            if (SLOT_48 == 1305):
                Unknown30070('526f746174696f6e53686f744169724200000000000000000000000000000000')
                setGravity(-1500)
                physicsXImpulse(35000)
            if (SLOT_48 == 1307):
                Unknown30070('526f746174696f6e53686f744c616e64415f5053000000000000000000000000')
                setGravity(-2000)
                physicsXImpulse(30000)
                AttackP1(70)
                Unknown11042(1)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirUntechableTime(40)
            if (SLOT_48 == 1308):
                clearUponHandler(43)
                sendToLabel(1)
        SLOT_4 = 1

        def upon_44():
            SLOT_52 = 1

        def upon_54():
            sendToLabel(0)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown2037(1)
        SLOT_58 = 1
    sprite('Action_136_02', 3)	# 1-3
    physicsXImpulse(20000)
    physicsYImpulse(-20000)
    SFX_3('SE_BloodSplashA')
    SFX_3('SE045')
    sprite('Action_136_03', 3)	# 4-6
    sprite('Action_136_04', 3)	# 7-9
    sprite('Action_136_05', 3)	# 10-12
    sprite('Action_136_06', 3)	# 13-15
    sprite('Action_136_07', 3)	# 16-18
    sprite('Action_136_08', 2)	# 19-20
    sprite('Action_136_09', 2)	# 21-22
    Unknown1019(50)
    YAccel(0)
    setGravity(0)
    sprite('Action_136_10', 2)	# 23-24
    Unknown23015(0)
    SLOT_51 = 1
    label(2)
    sprite('Action_136_11', 4)	# 25-28	 **attackbox here**
    RefreshMultihit()
    if (SLOT_53 == 0):
        physicsXImpulse(-5000)
    SFX_3('SE045')
    sprite('Action_136_12', 4)	# 29-32	 **attackbox here**
    sprite('Action_136_13', 4)	# 33-36	 **attackbox here**
    loopRest()
    SLOT_53 = (SLOT_53 + 1)
    if SLOT_2:
        SLOT_54 = (SLOT_54 + 1)
    gotoLabel(2)
    label(0)
    sprite('Action_136_15', 1)	# 37-37
    Unknown1084(1)
    sprite('Action_136_16', 3)	# 38-40
    sprite('Action_136_17', 3)	# 41-43
    sprite('Action_136_18', 3)	# 44-46
    sprite('Action_136_19', 3)	# 47-49
    sprite('Action_136_20', 3)	# 50-52
    sprite('Action_136_21', 32767)	# 53-32819
    GFX_0('RotationShot_Blood', -1)
    enterState('BloodPool_RS')
    ExitState()
    label(1)
    sprite('Action_136_15', 1)	# 32820-32820
    Unknown1084(1)
    sprite('Action_136_16', 3)	# 32821-32823
    sprite('Action_136_17', 3)	# 32824-32826
    sprite('Action_136_18', 3)	# 32827-32829
    sprite('Action_136_19', 3)	# 32830-32832
    sprite('Action_136_20', 3)	# 32833-32835
    sprite('Action_136_21', 1)	# 32836-32836
    GFX_0('RotationShot_Blood', -1)
    ExitState()

@State
def RotationShotEx_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(600)
        Unknown11092(1)
        Hitstop(0)
        Unknown11001(3, 3, 5)
        AirPushbackY(18000)
        AirUntechableTime(24)
        PushbackX(9800)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        Unknown11050('0200000065665f686974736d5f7465737400000000000000000000000000000000000000')
        Unknown2053(1)
        Unknown30065(0)
        Unknown11091(10)
        Unknown23015(11)
        teleportRelativeX(100000)
        Unknown1007(250000)

        def upon_3():
            if (SLOT_23 < 200000):
                teleportRelativeY(200000)
            if SLOT_51:
                if SLOT_52:
                    clearUponHandler(3)
                    sendToLabel(2)
            if 
            if (not (SLOT_53 == 4)):
                (SLOT_54 == 2):
                Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 1303):
                Unknown30070('526f746174696f6e53686f744c616e6443000000000000000000000000000000')
                setGravity(-2000)
            if (SLOT_48 == 1306):
                Unknown30070('526f746174696f6e53686f744169724300000000000000000000000000000000')
                setGravity(-1500)
            if (SLOT_48 == 1308):
                clearUponHandler(43)
                sendToLabel(2)

        def upon_44():
            SLOT_52 = 1
        SLOT_4 = 1

        def upon_54():
            sendToLabel(1)
        SLOT_58 = 1
    sprite('Action_135_00', 3)	# 1-3
    physicsXImpulse(20000)
    physicsYImpulse(-20000)
    sprite('Action_135_01', 3)	# 4-6
    sprite('Action_135_02', 3)	# 7-9
    sprite('Action_135_03', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE045')
    SFX_3('SE_BloodSplashA')
    sprite('Action_135_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_135_05', 3)	# 16-18	 **attackbox here**
    sprite('Action_135_06', 2)	# 19-20	 **attackbox here**
    sprite('Action_135_07', 2)	# 21-22	 **attackbox here**
    Unknown1019(50)
    YAccel(0)
    setGravity(0)
    sprite('Action_135_08', 2)	# 23-24	 **attackbox here**
    Unknown23015(0)
    SLOT_51 = 1

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        Unknown2037(1)
    label(0)
    sprite('Action_135_09', 4)	# 25-28	 **attackbox here**
    RefreshMultihit()
    if (SLOT_53 == 0):
        physicsXImpulse(-5000)
    SFX_3('SE045')
    sprite('Action_135_10', 4)	# 29-32	 **attackbox here**
    RefreshMultihit()
    sprite('Action_135_11', 4)	# 33-36	 **attackbox here**
    RefreshMultihit()
    loopRest()
    SLOT_53 = (SLOT_53 + 1)
    if SLOT_2:
        SLOT_54 = (SLOT_54 + 1)
    gotoLabel(0)
    label(1)
    sprite('Action_135_13', 1)	# 37-37
    Unknown1084(1)
    sprite('Action_135_14', 3)	# 38-40
    sprite('Action_135_15', 3)	# 41-43
    sprite('Action_135_16', 3)	# 44-46
    sprite('Action_135_17', 3)	# 47-49
    sprite('Action_135_18', 3)	# 50-52
    sprite('Action_135_19', 32767)	# 53-32819
    GFX_0('RotationShot_Blood', -1)
    enterState('BloodPool_RS')
    ExitState()
    label(2)
    sprite('Action_135_13', 1)	# 32820-32820
    Unknown1084(1)
    sprite('Action_135_14', 3)	# 32821-32823
    sprite('Action_135_15', 3)	# 32824-32826
    sprite('Action_135_16', 3)	# 32827-32829
    sprite('Action_135_17', 3)	# 32830-32832
    sprite('Action_135_18', 3)	# 32833-32835
    sprite('Action_135_19', 1)	# 32836-32836
    GFX_0('RotationShot_Blood', -1)
    ExitState()

@State
def RotationShot_Blood():

    def upon_IMMEDIATE():
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                if (SLOT_23 < 250000):
                    clearUponHandler(3)
                    Unknown1084(1)
                    sendToLabel(1)
        SLOT_4 = 0
    sprite('Action_146_00', 1)	# 1-1
    Unknown1056(700)
    Unknown1064(600)
    setGravity(10000)
    sprite('Action_146_01', 15)	# 2-16
    Unknown2037(1)
    Unknown1056(500)
    Unknown1064(700)
    sprite('Action_146_02', 32767)	# 17-32783
    Unknown1056(400)
    Unknown1064(1500)
    label(1)
    sprite('Action_146_03', 3)	# 32784-32786
    Unknown1056(750)
    Unknown1064(500)
    teleportRelativeY(0)
    sprite('Action_146_04', 3)	# 32787-32789
    sprite('Action_146_05', 3)	# 32790-32792
    sprite('Action_146_06', 10)	# 32793-32802
    sprite('Action_146_07', 1)	# 32803-32803
    Unknown1096(0)

@State
def DoubleShot1st_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        AttackLevel_(3)
        AttackP1(70)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(17500)
        AirPushbackY(20000)
        AirUntechableTime(25)
        Unknown11042(1)
        Unknown9016(1)
        Hitstop(0)
        Unknown11001(10, 10, 12)
        Unknown23015(6)
        Unknown2053(1)

        def upon_43():
            if (SLOT_48 == 1491):
                Unknown30070('446f75626c6553686f7431737441000000000000000000000000000000000000')
                teleportRelativeX(200000)
            if (SLOT_48 == 1492):
                Unknown30070('446f75626c6553686f7431737442000000000000000000000000000000000000')
                teleportRelativeX(300000)
    sprite('null', 1)	# 1-1
    sprite('Action_153_00', 2)	# 2-3
    SFX_3('SE_BloodSplashB')
    sprite('Action_153_01', 3)	# 4-6
    sprite('Action_153_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_153_03', 27)	# 9-35
    sprite('Action_153_04', 2)	# 36-37	 **attackbox here**
    Unknown23015(11)
    sprite('Action_153_05', 2)	# 38-39	 **attackbox here**
    sprite('Action_153_06', 2)	# 40-41	 **attackbox here**
    sprite('Action_153_07', 10)	# 42-51
    sprite('Action_153_08', 10)	# 52-61
    sprite('Action_153_09', 1)	# 62-62

@State
def DoubleShot2nd_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        AttackLevel_(3)
        AttackP1(70)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(5000)
        AirPushbackY(30000)
        AirUntechableTime(45)
        Unknown11042(1)
        Unknown9016(1)
        Unknown2053(1)

        def upon_43():
            if (SLOT_48 == 1493):
                Unknown30070('446f75626c6553686f74326e6441000000000000000000000000000000000000')
                teleportRelativeX(300000)
            if (SLOT_48 == 1494):
                Unknown30070('446f75626c6553686f74326e6442000000000000000000000000000000000000')
                teleportRelativeX(400000)
    sprite('null', 1)	# 1-1
    sprite('Action_155_00', 2)	# 2-3
    SFX_3('SE_BloodSplashB')
    sprite('Action_155_01', 3)	# 4-6
    sprite('Action_155_02', 7)	# 7-13	 **attackbox here**
    sprite('Action_155_03', 3)	# 14-16
    Unknown23015(11)
    sprite('Action_155_04', 3)	# 17-19	 **attackbox here**
    sprite('Action_155_05', 3)	# 20-22	 **attackbox here**
    sprite('Action_155_06', 3)	# 23-25	 **attackbox here**
    sprite('Action_155_07', 10)	# 26-35	 **attackbox here**
    sprite('Action_155_08', 10)	# 36-45
    sprite('Action_155_09', 1)	# 46-46

@State
def DoubleShotC():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4011(3)
        Unknown1096(850)
        teleportRelativeX(-58000)
        Unknown1007(-100000)
        Unknown2003(1)
    sprite('Action_156_00', 2)	# 1-2
    sprite('Action_156_01', 2)	# 3-4
    sprite('Action_156_02', 2)	# 5-6
    sprite('Action_156_03', 2)	# 7-8
    sprite('Action_156_04', 2)	# 9-10
    sprite('Action_156_05', 2)	# 11-12
    physicsYImpulse(-10000)
    setGravity(3500)
    sprite('Action_156_06', 2)	# 13-14
    SFX_3('SE_BloodSplashB')
    sprite('Action_156_07ex01', 6)	# 15-20	 **attackbox here**

@State
def DoubleShotC_Ground():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(1000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        Unknown9016(1)
        Hitstop(3)
        AirUntechableTime(40)
        AirPushbackX(8000)
        AirPushbackY(15000)
        Unknown11056(3)
        teleportRelativeX(-70000)
        teleportRelativeY(0)

        def upon_44():
            Unknown2003(1)
    sprite('Action_156_07ex02', 4)	# 1-4	 **attackbox here**
    StartMultihit()
    SFX_3('SE_BloodSplashB')
    sprite('Action_156_08ex02', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_BloodSplashB')
    sprite('Action_156_09ex02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_10ex02', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_14ex02', 19)	# 11-29	 **attackbox here**
    sprite('null', 10)	# 30-39
    GFX_0('DoubleShotC_Ground_Last', -1)
    enterState('BloodPool_C1')

@State
def DoubleShotC_Ground_Last():
    sprite('Action_156_15ex02', 3)	# 1-3	 **attackbox here**
    sprite('Action_156_16ex02', 3)	# 4-6	 **attackbox here**
    sprite('Action_156_17ex02', 3)	# 7-9	 **attackbox here**
    sprite('Action_156_18', 1)	# 10-10

@State
def DoubleShotC_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-70000)
        teleportRelativeY(0)
        Unknown2003(1)
    sprite('null', 4)	# 1-4
    sprite('Action_156_08ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_156_09ex01', 2)	# 7-8	 **attackbox here**
    sprite('Action_156_10ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_156_14ex01', 19)	# 11-29
    sprite('null', 10)	# 30-39
    GFX_0('DoubleShotC_Eff_Last', -1)
    enterState('BloodPool_C2')

@State
def DoubleShotC_Eff_Last():
    sprite('Action_156_15ex01', 3)	# 1-3
    sprite('Action_156_16ex01', 3)	# 4-6
    sprite('Action_156_17ex01', 3)	# 7-9
    sprite('Action_156_18', 1)	# 10-10

@State
def PushUpShot_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown2053(1)

        def upon_43():
            if (SLOT_48 == 1791):
                SLOT_51 = 1
                teleportRelativeX(300000)
            if (SLOT_48 == 1792):
                SLOT_51 = 2
                teleportRelativeX(600000)
            if (SLOT_48 == 1793):
                SLOT_51 = 3
                teleportRelativeX(900000)
    sprite('null', 2)	# 1-2
    sprite('null', 1)	# 3-3
    if random_(2, 0, 33):
        GFX_0('PushUpShotTypeA', -1)
        if (SLOT_51 == 1):
            Unknown23029(1, 1791, 0)
        if (SLOT_51 == 2):
            Unknown23029(1, 1792, 0)
        if (SLOT_51 == 3):
            Unknown23029(1, 1793, 0)
    elif random_(2, 0, 50):
        GFX_0('PushUpShotTypeB', -1)
        if (SLOT_51 == 1):
            Unknown23029(1, 1791, 0)
        if (SLOT_51 == 2):
            Unknown23029(1, 1792, 0)
        if (SLOT_51 == 3):
            Unknown23029(1, 1793, 0)
    else:
        GFX_0('PushUpShotTypeC', -1)
        if (SLOT_51 == 1):
            Unknown23029(1, 1791, 0)
        if (SLOT_51 == 2):
            Unknown23029(1, 1792, 0)
        if (SLOT_51 == 3):
            Unknown23029(1, 1793, 0)
    sprite('null', 10)	# 4-13
    enterState('BloodPool_PU')

@Subroutine
def PushUpShotInit():
    Unknown2010()
    Unknown4011(3)
    AttackLevel_(3)
    Damage(2000)
    AttackP2(80)
    Unknown11092(1)
    HitLow(2)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(12000)
    AirPushbackY(15000)
    AirUntechableTime(30)
    Hitstop(0)
    Unknown11001(11, 11, 13)
    Unknown9016(1)
    Unknown23182(3)

@State
def PushUpShotTypeA():

    def upon_IMMEDIATE():
        callSubroutine('PushUpShotInit')

        def upon_43():
            if (SLOT_48 == 1791):
                Unknown30070('50757368557053686f7441000000000000000000000000000000000000000000')
            if (SLOT_48 == 1792):
                Unknown30070('50757368557053686f7442000000000000000000000000000000000000000000')
            if (SLOT_48 == 1793):
                Unknown30070('50757368557053686f7443000000000000000000000000000000000000000000')
    sprite('Action_175_00', 2)	# 1-2
    GFX_0('PushUpShotAtk', -1)
    Unknown4020(1)
    sprite('Action_175_01', 3)	# 3-5
    sprite('Action_175_02', 2)	# 6-7
    sprite('Action_175_02', 13)	# 8-20
    Unknown4020(0)
    sprite('Action_175_03', 1)	# 21-21
    sprite('Action_175_04', 3)	# 22-24
    sprite('Action_175_05', 3)	# 25-27
    sprite('Action_175_06', 3)	# 28-30
    sprite('Action_175_07', 1)	# 31-31
    loopRest()
    ExitState()

@State
def PushUpShotTypeB():

    def upon_IMMEDIATE():
        callSubroutine('PushUpShotInit')

        def upon_43():
            if (SLOT_48 == 1791):
                Unknown30070('50757368557053686f7441000000000000000000000000000000000000000000')
            if (SLOT_48 == 1792):
                Unknown30070('50757368557053686f7442000000000000000000000000000000000000000000')
            if (SLOT_48 == 1793):
                Unknown30070('50757368557053686f7443000000000000000000000000000000000000000000')
    sprite('Action_176_00', 2)	# 1-2
    GFX_0('PushUpShotAtk', -1)
    Unknown4020(1)
    sprite('Action_176_01', 3)	# 3-5
    sprite('Action_176_02', 2)	# 6-7
    sprite('Action_176_02', 13)	# 8-20
    Unknown4020(0)
    sprite('Action_176_03', 1)	# 21-21
    sprite('Action_176_04', 3)	# 22-24
    sprite('Action_176_05', 3)	# 25-27
    sprite('Action_176_06', 3)	# 28-30
    sprite('Action_176_07', 1)	# 31-31

@State
def PushUpShotTypeC():

    def upon_IMMEDIATE():
        callSubroutine('PushUpShotInit')

        def upon_43():
            if (SLOT_48 == 1791):
                Unknown30070('50757368557053686f7441000000000000000000000000000000000000000000')
            if (SLOT_48 == 1792):
                Unknown30070('50757368557053686f7442000000000000000000000000000000000000000000')
            if (SLOT_48 == 1793):
                Unknown30070('50757368557053686f7443000000000000000000000000000000000000000000')
    sprite('Action_177_00', 2)	# 1-2
    GFX_0('PushUpShotAtk', -1)
    Unknown4020(1)
    sprite('Action_177_01', 3)	# 3-5
    sprite('Action_177_02', 2)	# 6-7
    sprite('Action_177_02', 13)	# 8-20
    Unknown4020(0)
    sprite('Action_177_03', 1)	# 21-21
    sprite('Action_177_04', 3)	# 22-24
    sprite('Action_177_05', 3)	# 25-27
    sprite('Action_177_06', 3)	# 28-30
    sprite('Action_177_07', 1)	# 31-31

@State
def PushUpShotAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown4007(2)
        Unknown23027()
    sprite('null', 4)	# 1-4
    SFX_3('SE_BloodSplashB')
    sprite('Action_175_Atk', 3)	# 5-7	 **attackbox here**
    sprite('null', 2)	# 8-9

@State
def PushUpShotTypeEx():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(0)
        Damage(3000)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpluseBeforeWallbounce(0)
        AttackP1(60)
        AttackP2(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9154(5)
        AirUntechableTime(5)
        Unknown9016(1)
        Unknown11084(1)
        Hitstop(0)
        Unknown11062(1)
        Unknown11068(1)
        Unknown23182(3)
        Unknown1086(22)
        teleportRelativeY(0)

        def upon_78():
            Unknown11064(1)
            GFX_0('PushUpShotExe', -1)
            Unknown1087(22, 25)
            Unknown14()

        def upon_82():
            Unknown11064(0)
            AirPushbackX(8000)
            AirPushbackY(22000)
            YImpluseBeforeWallbounce(2000)
    sprite('null', 2)	# 1-2
    sprite('Action_185_00', 2)	# 3-4
    SFX_3('SE_BloodSplashB')
    sprite('Action_185_01', 3)	# 5-7	 **attackbox here**
    sprite('Action_185_02', 20)	# 8-27
    sprite('Action_185_03', 5)	# 28-32
    sprite('Action_185_04', 3)	# 33-35
    sprite('Action_185_05', 3)	# 36-38
    sprite('Action_185_06', 3)	# 39-41
    sprite('Action_185_07', 3)	# 42-44

@State
def PushUpShotTypeEx_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(0)
        Damage(4000)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpluseBeforeWallbounce(0)
        AttackP1(60)
        AttackP2(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9154(5)
        AirUntechableTime(5)
        Unknown9016(1)
        Unknown11084(1)
        Hitstop(0)
        Unknown11062(1)
        Unknown11068(1)
        Unknown23182(3)
        Unknown1086(22)
        teleportRelativeY(0)

        def upon_78():
            Unknown11064(1)
            GFX_0('PushUpShotExe', -1)
            Unknown1087(22, 25)
            Unknown14()

        def upon_82():
            Unknown11064(0)
            AirPushbackX(8000)
            AirPushbackY(22000)
            YImpluseBeforeWallbounce(2000)
    sprite('null', 2)	# 1-2
    sprite('Action_185_00', 2)	# 3-4
    SFX_3('SE_BloodSplashB')
    sprite('Action_185_01', 3)	# 5-7	 **attackbox here**
    sprite('Action_185_02', 20)	# 8-27
    sprite('Action_185_03', 5)	# 28-32
    sprite('Action_185_04', 3)	# 33-35
    sprite('Action_185_05', 3)	# 36-38
    sprite('Action_185_06', 3)	# 39-41
    sprite('Action_185_07', 3)	# 42-44

@State
def PushUpShotExe():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(0)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9154(300)
        AirUntechableTime(300)
        AirPushbackX(0)
        AirPushbackY(1)
        PushbackX(0)
        Unknown9016(1)
        Hitstop(0)
        Unknown11001(0, 180, 180)
        Unknown11072(1, 0, 0)
        Unknown11067(1)
        Unknown11068(1)
        Unknown11064(1)
        Unknown11062(1)
        Unknown30048(1)
        Unknown11084(1)
        Unknown2019(1000)
        Unknown23182(3)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_78():
            clearUponHandler(78)
            Unknown36(22)
            Unknown2019(500)
            Unknown35()
            Unknown23029(3, 1794, 0)
            Unknown48('1900000002000000020000001600000002000000aa000000')
            if SLOT_2:
                Unknown11001(0, 110, 110)
        SLOT_11 = 1

        def upon_STATE_END():
            Unknown36(22)
            Unknown2019(0)
            Unknown35()
            SLOT_11 = 0
    sprite('Action_185_08', 2)	# 1-2	 **attackbox here**
    GFX_0('PushUpShotDD_Clear', -1)
    sprite('Action_185_08', 2)	# 3-4	 **attackbox here**
    StartMultihit()

    def upon_3():
        if (not Unknown23146('1600000050757368557053686f7445786500000000000000000000000000000000000000')):
            clearUponHandler(3)
            Unknown26('PushUpShotDD_Clear')
            sendToLabel(0)
    sprite('Action_185_09', 5)	# 5-9	 **attackbox here**
    sprite('Action_185_10', 10)	# 10-19	 **attackbox here**
    StartMultihit()
    sprite('Action_185_10', 20)	# 20-39	 **attackbox here**
    sprite('Action_185_10', 20)	# 40-59	 **attackbox here**
    sprite('Action_185_10', 20)	# 60-79	 **attackbox here**
    sprite('Action_185_10', 20)	# 80-99	 **attackbox here**
    sprite('Action_185_10', 20)	# 100-119	 **attackbox here**
    sprite('Action_185_10', 20)	# 120-139	 **attackbox here**
    sprite('Action_185_10', 20)	# 140-159	 **attackbox here**
    sprite('Action_185_10', 20)	# 160-179	 **attackbox here**
    sprite('Action_185_10', 10)	# 180-189	 **attackbox here**
    RefreshMultihit()
    clearUponHandler(3)
    Unknown11067(0)
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9130(10)
    Unknown9142(999)
    Unknown11064(0)
    Unknown11094(1)
    Unknown30048(0)
    Unknown11001(0, 0, 0)
    label(0)
    sprite('Action_187_00', 5)	# 190-194
    sprite('Action_187_01', 3)	# 195-197
    sprite('Action_187_02', 3)	# 198-200
    sprite('Action_187_03', 3)	# 201-203

@State
def PushUpShotDD_Clear():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown2003(1)
        Unknown2019(100)
    sprite('Action_185_08ex00', 4)	# 1-4
    sprite('Action_185_09ex00', 5)	# 5-9
    sprite('Action_185_10ex00', 10)	# 10-19
    sprite('Action_185_10ex00', 20)	# 20-39
    sprite('Action_185_10ex00', 20)	# 40-59
    sprite('Action_185_10ex00', 20)	# 60-79
    sprite('Action_185_10ex00', 20)	# 80-99
    sprite('Action_185_10ex00', 20)	# 100-119
    sprite('Action_185_10ex00', 20)	# 120-139
    sprite('Action_185_10ex00', 20)	# 140-159
    sprite('Action_185_10ex00', 20)	# 160-179
    sprite('Action_185_10ex00', 10)	# 180-189
    sprite('Action_187_00', 5)	# 190-194
    sprite('Action_187_01', 3)	# 195-197
    sprite('Action_187_02', 3)	# 198-200
    sprite('Action_187_03', 3)	# 201-203

@Subroutine
def NormalDissolveInit():
    Unknown4010(0)
    Unknown4011(0)
    Unknown3001(255)
    teleportRelativeY(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown23015(11)
    if (SLOT_95 == 0):
        Unknown2037(0)
    if (SLOT_95 == 2):
        Unknown2037(0)
    if (SLOT_95 == 1):
        Unknown2037(1)
    if (SLOT_95 == 3):
        Unknown2037(1)

    def upon_43():
        if (SLOT_48 == 9991):
            enterState('BloodAtk_RS')
        if (SLOT_48 == 9992):
            SLOT_51 = 5
        if (SLOT_48 == 9994):
            SLOT_51 = 4
            SLOT_59 = 1
        if (SLOT_48 == 9993):
            enterState('BloodAtk_RS_PS')
        if (SLOT_48 == 9999):
            clearUponHandler(43)
            sendToLabel(1)

    def upon_3():
        SLOT_51 = (SLOT_51 + (-1))
        if (SLOT_51 < 0):
            SLOT_51 = 0
        if (SLOT_51 == 1):
            if random_(2, 0, 33):
                enterState('BloodAtk_PUA')
            elif random_(2, 0, 50):
                enterState('BloodAtk_PUB')
            else:
                enterState('BloodAtk_PUC')
        if (SLOT_60 == 1):
            SLOT_60 = 0
            enterState('BloodPool_Hide')

    def upon_53():
        sendToLabel(1)

@Subroutine
def SpecialDissolveInit():
    Unknown4010(0)
    Unknown4011(0)
    Unknown3001(255)
    teleportRelativeY(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown23015(11)
    if (SLOT_95 == 0):
        Unknown2037(0)
    if (SLOT_95 == 2):
        Unknown2037(0)
    if (SLOT_95 == 1):
        Unknown2037(1)
    if (SLOT_95 == 3):
        Unknown2037(1)

    def upon_43():
        if (SLOT_48 == 9991):
            enterState('BloodAtk_RS')
        if (SLOT_48 == 9992):
            SLOT_51 = 5
        if (SLOT_48 == 9994):
            SLOT_51 = 4
            SLOT_59 = 1
        if (SLOT_48 == 9993):
            enterState('BloodAtk_RS_PS')
        if (SLOT_48 == 9999):
            clearUponHandler(43)
            sendToLabel(2)

    def upon_3():
        SLOT_51 = (SLOT_51 + (-1))
        if (SLOT_51 < 0):
            SLOT_51 = 0
        if (SLOT_51 == 1):
            if random_(2, 0, 33):
                enterState('BloodAtk_PUA')
            elif random_(2, 0, 50):
                enterState('BloodAtk_PUB')
            else:
                enterState('BloodAtk_PUC')
        if (SLOT_60 == 1):
            SLOT_60 = 0
            enterState('BloodPool_Hide')

    def upon_53():
        sendToLabel(2)

@State
def BloodPool_B():

    def upon_IMMEDIATE():
        callSubroutine('NormalDissolveInit')
        teleportRelativeX(100000)
    sprite('Action_108_00', 3)	# 1-3
    Unknown23183('416374696f6e5f3131325f303000000000000000000000000000000000000000030000000200000002000000')
    SFX_3('SE_BloodPool')
    sprite('Action_108_01', 3)	# 4-6
    Unknown23183('416374696f6e5f3131325f303100000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_02', 3)	# 7-9
    Unknown23183('416374696f6e5f3131325f303200000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_03', 3)	# 10-12
    Unknown23183('416374696f6e5f3131325f303300000000000000000000000000000000000000030000000200000002000000')
    label(2)
    sprite('Action_108_03', 3)	# 13-15
    Unknown23183('416374696f6e5f3131325f303300000000000000000000000000000000000000030000000200000002000000')
    loopRest()
    random_(2, 0, 10)
    if SLOT_0:
        _gotolabel(0)
    gotoLabel(2)
    label(0)
    sprite('Action_108_04', 3)	# 16-18
    Unknown23183('416374696f6e5f3131325f303400000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_05', 3)	# 19-21
    Unknown23183('416374696f6e5f3131325f303500000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_06', 3)	# 22-24
    Unknown23183('416374696f6e5f3131325f303600000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_07', 3)	# 25-27
    Unknown23183('416374696f6e5f3131325f303700000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_08', 3)	# 28-30
    Unknown23183('416374696f6e5f3131325f303800000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_09', 3)	# 31-33
    Unknown23183('416374696f6e5f3131325f303900000000000000000000000000000000000000030000000200000002000000')
    gotoLabel(2)
    label(1)
    sprite('Action_108_11', 10)	# 34-43
    Unknown23183('416374696f6e5f3131325f3131000000000000000000000000000000000000000a0000000200000002000000')
    Unknown3001(255)
    Unknown3004(-25)
    Unknown1059(-50)
    Unknown1067(-100)
    sprite('Action_108_12', 1)	# 44-44
    Unknown23183('416374696f6e5f3131325f313200000000000000000000000000000000000000010000000200000002000000')

@State
def BloodPool_C1():

    def upon_IMMEDIATE():
        callSubroutine('NormalDissolveInit')
        teleportRelativeX(300000)
    sprite('Action_108_00', 3)	# 1-3
    Unknown23183('416374696f6e5f3131325f303000000000000000000000000000000000000000030000000200000002000000')
    SFX_3('SE_BloodPool')
    sprite('Action_108_01', 3)	# 4-6
    Unknown23183('416374696f6e5f3131325f303100000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_02', 3)	# 7-9
    Unknown23183('416374696f6e5f3131325f303200000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_03', 3)	# 10-12
    Unknown23183('416374696f6e5f3131325f303300000000000000000000000000000000000000030000000200000002000000')
    label(2)
    sprite('Action_108_03', 3)	# 13-15
    Unknown23183('416374696f6e5f3131325f303300000000000000000000000000000000000000030000000200000002000000')
    loopRest()
    random_(2, 0, 10)
    if SLOT_0:
        _gotolabel(0)
    gotoLabel(2)
    label(0)
    sprite('Action_108_04', 3)	# 16-18
    Unknown23183('416374696f6e5f3131325f303400000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_05', 3)	# 19-21
    Unknown23183('416374696f6e5f3131325f303500000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_06', 3)	# 22-24
    Unknown23183('416374696f6e5f3131325f303600000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_07', 3)	# 25-27
    Unknown23183('416374696f6e5f3131325f303700000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_08', 3)	# 28-30
    Unknown23183('416374696f6e5f3131325f303800000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_09', 3)	# 31-33
    Unknown23183('416374696f6e5f3131325f303900000000000000000000000000000000000000030000000200000002000000')
    gotoLabel(2)
    label(1)
    sprite('Action_108_11', 10)	# 34-43
    Unknown23183('416374696f6e5f3131325f3131000000000000000000000000000000000000000a0000000200000002000000')
    Unknown3001(255)
    Unknown3004(-25)
    Unknown1059(-50)
    Unknown1067(-100)
    sprite('Action_108_12', 1)	# 44-44
    Unknown23183('416374696f6e5f3131325f313200000000000000000000000000000000000000010000000200000002000000')

@State
def BloodPool_C2():

    def upon_IMMEDIATE():
        callSubroutine('NormalDissolveInit')
    sprite('Action_108_00', 3)	# 1-3
    Unknown23183('416374696f6e5f3131325f303000000000000000000000000000000000000000030000000200000002000000')
    SFX_3('SE_BloodPool')
    sprite('Action_108_01', 3)	# 4-6
    Unknown23183('416374696f6e5f3131325f303100000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_02', 3)	# 7-9
    Unknown23183('416374696f6e5f3131325f303200000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_03', 3)	# 10-12
    Unknown23183('416374696f6e5f3131325f303300000000000000000000000000000000000000030000000200000002000000')
    label(2)
    sprite('Action_108_03', 3)	# 13-15
    Unknown23183('416374696f6e5f3131325f303300000000000000000000000000000000000000030000000200000002000000')
    loopRest()
    random_(2, 0, 10)
    if SLOT_0:
        _gotolabel(0)
    gotoLabel(2)
    label(0)
    sprite('Action_108_04', 3)	# 16-18
    Unknown23183('416374696f6e5f3131325f303400000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_05', 3)	# 19-21
    Unknown23183('416374696f6e5f3131325f303500000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_06', 3)	# 22-24
    Unknown23183('416374696f6e5f3131325f303600000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_07', 3)	# 25-27
    Unknown23183('416374696f6e5f3131325f303700000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_08', 3)	# 28-30
    Unknown23183('416374696f6e5f3131325f303800000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_108_09', 3)	# 31-33
    Unknown23183('416374696f6e5f3131325f303900000000000000000000000000000000000000030000000200000002000000')
    gotoLabel(2)
    label(1)
    sprite('Action_108_11', 10)	# 34-43
    Unknown23183('416374696f6e5f3131325f3131000000000000000000000000000000000000000a0000000200000002000000')
    Unknown3001(255)
    Unknown3004(-25)
    Unknown1059(-50)
    Unknown1067(-100)
    sprite('Action_108_12', 1)	# 44-44
    Unknown23183('416374696f6e5f3131325f313200000000000000000000000000000000000000010000000200000002000000')

@State
def BloodPool_RS():

    def upon_IMMEDIATE():
        callSubroutine('SpecialDissolveInit')
    sprite('Action_106_00', 3)	# 1-3
    Unknown23183('416374696f6e5f3131305f303000000000000000000000000000000000000000030000000200000002000000')
    SFX_3('SE_BloodPool')
    sprite('Action_106_01', 3)	# 4-6
    Unknown23183('416374696f6e5f3131305f303100000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_106_02', 3)	# 7-9
    Unknown23183('416374696f6e5f3131305f303200000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_106_03', 3)	# 10-12
    Unknown23183('416374696f6e5f3131305f303300000000000000000000000000000000000000030000000200000002000000')
    label(3)
    sprite('Action_106_03', 3)	# 13-15
    Unknown23183('416374696f6e5f3131305f303300000000000000000000000000000000000000030000000200000002000000')
    loopRest()
    random_(2, 0, 10)
    if SLOT_0:
        _gotolabel(0)
    gotoLabel(3)
    label(0)
    sprite('Action_106_04', 3)	# 16-18
    Unknown23183('416374696f6e5f3131305f303400000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_106_05', 3)	# 19-21
    Unknown23183('416374696f6e5f3131305f303500000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_106_06', 3)	# 22-24
    Unknown23183('416374696f6e5f3131305f303600000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_106_07', 3)	# 25-27
    Unknown23183('416374696f6e5f3131305f303700000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_106_08', 3)	# 28-30
    Unknown23183('416374696f6e5f3131305f303800000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_106_09', 3)	# 31-33
    Unknown23183('416374696f6e5f3131305f303900000000000000000000000000000000000000030000000200000002000000')
    gotoLabel(3)
    label(2)
    sprite('Action_108_11', 10)	# 34-43
    Unknown23183('416374696f6e5f3131325f3131000000000000000000000000000000000000000a0000000200000002000000')
    Unknown3001(255)
    Unknown3004(-25)
    Unknown1059(-50)
    Unknown1067(-100)
    sprite('Action_108_12', 1)	# 44-44
    Unknown23183('416374696f6e5f3131325f313200000000000000000000000000000000000000010000000200000002000000')

@State
def BloodPool_PU():

    def upon_IMMEDIATE():
        callSubroutine('SpecialDissolveInit')
    sprite('Action_107_00', 3)	# 1-3
    Unknown23183('416374696f6e5f3131315f303000000000000000000000000000000000000000030000000200000002000000')
    SFX_3('SE_BloodPool')
    sprite('Action_107_01', 3)	# 4-6
    Unknown23183('416374696f6e5f3131315f303100000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_107_02', 3)	# 7-9
    Unknown23183('416374696f6e5f3131315f303200000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_107_03', 3)	# 10-12
    Unknown23183('416374696f6e5f3131315f303300000000000000000000000000000000000000030000000200000002000000')
    label(3)
    sprite('Action_107_03', 3)	# 13-15
    Unknown23183('416374696f6e5f3131315f303300000000000000000000000000000000000000030000000200000002000000')
    loopRest()
    random_(2, 0, 10)
    if SLOT_0:
        _gotolabel(0)
    gotoLabel(3)
    label(0)
    sprite('Action_107_04', 3)	# 16-18
    Unknown23183('416374696f6e5f3131315f303400000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_107_05', 3)	# 19-21
    Unknown23183('416374696f6e5f3131315f303500000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_107_06', 3)	# 22-24
    Unknown23183('416374696f6e5f3131315f303600000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_107_07', 3)	# 25-27
    Unknown23183('416374696f6e5f3131315f303700000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_107_08', 3)	# 28-30
    Unknown23183('416374696f6e5f3131315f303800000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_107_09', 3)	# 31-33
    Unknown23183('416374696f6e5f3131315f303900000000000000000000000000000000000000030000000200000002000000')
    gotoLabel(3)
    label(2)
    sprite('Action_108_11', 10)	# 34-43
    Unknown23183('416374696f6e5f3131325f3131000000000000000000000000000000000000000a0000000200000002000000')
    Unknown3001(255)
    Unknown3004(-25)
    Unknown1059(-50)
    Unknown1067(-100)
    sprite('Action_108_12', 1)	# 44-44
    Unknown23183('416374696f6e5f3131325f313200000000000000000000000000000000000000010000000200000002000000')

@State
def BloodPool_Hide():

    def upon_IMMEDIATE():

        def upon_3():
            if (SLOT_60 == 2):
                SLOT_60 = 0
                if Unknown23145('BloodPool_B'):
                    enterState('BloodPool_B')
                elif Unknown23145('BloodPool_RS'):
                    enterState('BloodPool_RS')
                elif Unknown23145('BloodPool_PU'):
                    enterState('BloodPool_PU')
                elif Unknown23145('BloodPool_C1'):
                    enterState('BloodPool_C1')
                elif Unknown23145('BloodPool_C2'):
                    enterState('BloodPool_C2')
    sprite('null', 1800)	# 1-1800

@State
def BloodAtk_RS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP2(95)
        Damage(1500)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        Hitstop(8)
        Unknown9016(1)
        teleportRelativeY(0)
        Unknown2006()

        def upon_44():
            clearUponHandler(44)
            sendToLabel(1)
    sprite('Action_147_01', 3)	# 1-3
    sprite('Action_147_02', 3)	# 4-6
    sprite('Action_147_03', 3)	# 7-9
    sprite('Action_147_04', 3)	# 10-12
    sprite('Action_147_05', 3)	# 13-15
    sprite('Action_147_06', 3)	# 16-18
    physicsXImpulse(40000)
    Unknown1028(500)
    sprite('Action_147_09', 3)	# 19-21	 **attackbox here**
    sprite('Action_147_10', 3)	# 22-24	 **attackbox here**
    sprite('Action_147_11', 3)	# 25-27	 **attackbox here**
    sprite('Action_147_12', 3)	# 28-30	 **attackbox here**
    sprite('Action_147_13', 3)	# 31-33	 **attackbox here**
    sprite('Action_147_14', 3)	# 34-36	 **attackbox here**
    label(1)
    sprite('Action_147_16', 4)	# 37-40
    Unknown1019(5)
    Unknown1028(0)
    Unknown1059(-75)
    Unknown1067(-100)
    sprite('Action_147_17', 4)	# 41-44
    Unknown1056(700)
    Unknown1064(600)
    Unknown1059(0)
    Unknown1067(0)
    sprite('Action_147_18', 4)	# 45-48
    sprite('Action_147_19', 1)	# 49-49

@State
def BloodAtk_RS_PS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1500)
        AttackP1(70)
        AttackP2(95)
        Unknown11042(1)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        Hitstop(8)
        Unknown9016(1)
        teleportRelativeY(0)
        Unknown2006()

        def upon_44():
            clearUponHandler(44)
            sendToLabel(1)
    sprite('Action_147_01', 3)	# 1-3
    sprite('Action_147_02', 3)	# 4-6
    sprite('Action_147_03', 3)	# 7-9
    sprite('Action_147_04', 3)	# 10-12
    sprite('Action_147_05', 3)	# 13-15
    sprite('Action_147_06', 3)	# 16-18
    physicsXImpulse(40000)
    Unknown1028(500)
    sprite('Action_147_09', 3)	# 19-21	 **attackbox here**
    sprite('Action_147_10', 3)	# 22-24	 **attackbox here**
    sprite('Action_147_11', 3)	# 25-27	 **attackbox here**
    sprite('Action_147_12', 3)	# 28-30	 **attackbox here**
    sprite('Action_147_13', 3)	# 31-33	 **attackbox here**
    sprite('Action_147_14', 3)	# 34-36	 **attackbox here**
    label(1)
    sprite('Action_147_16', 4)	# 37-40
    Unknown1019(5)
    Unknown1028(0)
    Unknown1059(-75)
    Unknown1067(-100)
    sprite('Action_147_17', 4)	# 41-44
    Unknown1056(700)
    Unknown1064(600)
    Unknown1059(0)
    Unknown1067(0)
    sprite('Action_147_18', 4)	# 45-48
    sprite('Action_147_19', 1)	# 49-49

@Subroutine
def BloodAtkInit_PU():
    Unknown2010()
    Unknown4011(3)
    AttackLevel_(3)
    Damage(1000)
    AttackP2(80)
    Unknown11092(1)
    HitLow(2)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(12000)
    AirPushbackY(22000)
    AirUntechableTime(30)
    Unknown9016(1)
    Hitstop(0)
    Unknown11001(11, 11, 13)
    Unknown11056(3)
    Unknown23182(3)
    Unknown23015(0)
    Unknown30070('426c6f6f6441746b5f5055000000000000000000000000000000000000000000')
    teleportRelativeY(0)

    def upon_78():
        if SLOT_59:
            if Unknown23146('1600000050757368557053686f7445786500000000000000000000000000000000000000'):
                Unknown2011()
                AttackP1(48)
                AttackP2(100)
                AirHitstunAnimation(10)
                GroundedHitstunAnimation(10)
                Unknown9154(300)
                AirUntechableTime(300)
                AirPushbackX(0)
                AirPushbackY(1)
                YImpluseBeforeWallbounce(0)
                PushbackX(0)
                Unknown9016(1)
                Unknown11084(1)
                Hitstop(0)
                Unknown11067(1)
                Unknown11068(1)
                Unknown11083(1)
                Unknown11064(1)
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
                Unknown11062(1)
                Unknown4011(3)
                Unknown30070('50757368557053686f7445786500000000000000000000000000000000000000')

    def upon_82():
        if SLOT_59:
            if Unknown23146('1600000050757368557053686f7445786500000000000000000000000000000000000000'):
                Unknown2010()
                AttackP1(48)
                AttackP2(100)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirPushbackX(8000)
                AirPushbackY(22000)
                Unknown9154(5)
                AirUntechableTime(5)
                YImpluseBeforeWallbounce(2000)
                Unknown9016(1)
                Unknown11084(1)
                Hitstop(0)
                Unknown11001(11, 11, 13)
                Unknown11062(0)
                Unknown11064(0)
                Unknown11067(0)
                Unknown11068(0)
                Unknown11083(0)

    def upon_STATE_END():
        SLOT_59 = 0

@State
def BloodAtk_PUA():

    def upon_IMMEDIATE():
        callSubroutine('BloodAtkInit_PU')
    sprite('Action_175_00', 2)	# 1-2
    GFX_0('PushUpShotAtk', -1)
    Unknown4020(1)
    sprite('Action_175_01', 3)	# 3-5
    sprite('Action_175_02', 2)	# 6-7
    sprite('Action_175_02', 13)	# 8-20
    Unknown4020(0)
    sprite('Action_175_03', 1)	# 21-21
    sprite('Action_175_04', 3)	# 22-24
    sprite('Action_175_05', 3)	# 25-27
    sprite('Action_175_06', 3)	# 28-30
    sprite('Action_175_07', 1)	# 31-31

@State
def BloodAtk_PUB():

    def upon_IMMEDIATE():
        callSubroutine('BloodAtkInit_PU')
    sprite('Action_176_00', 2)	# 1-2
    GFX_0('PushUpShotAtk', -1)
    Unknown4020(1)
    sprite('Action_176_01', 3)	# 3-5
    sprite('Action_176_02', 2)	# 6-7
    sprite('Action_176_02', 13)	# 8-20
    Unknown4020(0)
    sprite('Action_176_03', 1)	# 21-21
    sprite('Action_176_04', 3)	# 22-24
    sprite('Action_176_05', 3)	# 25-27
    sprite('Action_176_06', 3)	# 28-30
    sprite('Action_176_07', 1)	# 31-31

@State
def BloodAtk_PUC():

    def upon_IMMEDIATE():
        callSubroutine('BloodAtkInit_PU')
    sprite('Action_177_00', 2)	# 1-2
    GFX_0('PushUpShotAtk', -1)
    Unknown4020(1)
    sprite('Action_177_01', 3)	# 3-5
    sprite('Action_177_02', 2)	# 6-7
    sprite('Action_177_02', 13)	# 8-20
    Unknown4020(0)
    sprite('Action_177_03', 1)	# 21-21
    sprite('Action_177_04', 3)	# 22-24
    sprite('Action_177_05', 3)	# 25-27
    sprite('Action_177_06', 3)	# 28-30
    sprite('Action_177_07', 1)	# 31-31

@State
def UltimateCommandThrowEff():

    def upon_IMMEDIATE():
        Unknown23015(11)
    sprite('Action_082_00', 3)	# 1-3
    sprite('Action_082_01', 3)	# 4-6
    SFX_3('SE_BloodCongeals')
    sprite('Action_082_02', 15)	# 7-21
    GFX_0('DrainEff', -1)
    sprite('Action_082_03', 3)	# 22-24
    sprite('Action_082_04', 3)	# 25-27
    sprite('Action_082_05', 3)	# 28-30
    sprite('Action_082_06', 3)	# 31-33

@State
def DrainEff():

    def upon_IMMEDIATE():
        Unknown4007(1)
    sprite('Action_089_00', 5)	# 1-5
    sprite('Action_089_01', 5)	# 6-10
    sprite('Action_089_02', 5)	# 11-15
    sprite('Action_089_03', 5)	# 16-20
    sprite('Action_089_04', 1)	# 21-21

@State
def UltimateShotEffMaster():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 2504):
                clearUponHandler(43)
                SLOT_51 = 1
            if (SLOT_48 == 2505):
                clearUponHandler(43)
                SLOT_51 = 2
            if (SLOT_48 == 2506):
                clearUponHandler(43)
                SLOT_51 = 3
    sprite('null', 6)	# 1-6
    GFX_0('UltimateShotEff', -1)
    if (SLOT_51 == 1):
        Unknown23029(1, 2504, 0)
    elif (SLOT_51 == 3):
        Unknown23029(1, 2506, 0)
    sprite('null', 8)	# 7-14
    teleportRelativeX(-7500)
    Unknown1007(-5000)
    GFX_0('UltimateShotEff', -1)
    if (SLOT_51 == 1):
        Unknown23029(1, 2504, 0)
    elif (SLOT_51 == 3):
        Unknown23029(1, 2506, 0)
    sprite('null', 60)	# 15-74
    GFX_0('UltimateShotAtk', -1)
    if (SLOT_51 == 1):
        Unknown23029(1, 2504, 0)
    elif (SLOT_51 == 2):
        Unknown23029(1, 2505, 0)
    elif (SLOT_51 == 3):
        Unknown23029(1, 2506, 0)

@State
def UltimateShotAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        AirUntechableTime(200)
        Hitstop(3)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(60000)
        AirPushbackY(25000)
        Unknown9310(1)
        Unknown9178(1)
        WallbounceReboundTime(0)
        Unknown9016(1)
        Unknown11091(25)

        def upon_77():
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 2):
                Unknown2003(1)

        def upon_81():
            SLOT_52 = (SLOT_52 + 1)
            if (SLOT_52 >= 2):
                Unknown30048(1)

        def upon_43():
            if (SLOT_48 == 2504):
                clearUponHandler(43)
                Damage(500)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                Unknown9310(-1)
                AirUntechableTime(60)
                Unknown2054(1)
            if (SLOT_48 == 2505):
                clearUponHandler(43)
                Damage(2500)
            if (SLOT_48 == 2506):
                clearUponHandler(43)
                Damage(750)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                Unknown9310(-1)
                AirUntechableTime(60)
                Unknown2054(1)
    sprite('null', 2)	# 1-2
    sprite('Action_250_Atk_01', 2)	# 3-4	 **attackbox here**
    RefreshMultihit()
    sprite('Action_250_Atk_02', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_250_Atk_03', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_250_Atk_04', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_250_Atk_04', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    sprite('null', 2)	# 13-14

@State
def UltimateShotEff():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 2504):
                clearUponHandler(43)
            if (SLOT_48 == 2506):
                clearUponHandler(43)
    sprite('null', 1)	# 1-1
    sprite('Action_254_00', 7)	# 2-8
    sprite('Action_254_01', 3)	# 9-11
    sprite('Action_254_02', 3)	# 12-14
    sprite('Action_254_03', 10)	# 15-24

@State
def UltimateShotFootEff():

    def upon_IMMEDIATE():
        Unknown2011()
        teleportRelativeY(0)
        AttackLevel_(4)
        Damage(500)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        AirPushbackX(20000)
        AirPushbackY(22000)
        AttackP1(80)
        AttackP2(100)
        Unknown11091(15)
        Hitstop(0)
        Unknown9016(1)
        Unknown11064(1)
        HitLow(2)
        Unknown11032('40420f00ffffffff40420f00c0bdf0ff')
        Unknown11069('UltimateShotFootEff_Add')

        def upon_78():
            Unknown23029(3, 2501, 0)
            GFX_0('UltimateShotFootEff_Add', -1)
            if (SLOT_51 == 1):
                Unknown23029(1, 2504, 0)
            elif (SLOT_51 == 2):
                Unknown23029(1, 2505, 0)
            elif (SLOT_51 == 3):
                Unknown23029(1, 2506, 0)

        def upon_43():
            if (SLOT_48 == 2502):
                clearUponHandler(43)
                sendToLabel(1)
            if (SLOT_48 == 2504):
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                SLOT_51 = 1
                HitLow(0)
                Unknown2054(1)
            if (SLOT_48 == 2505):
                SLOT_51 = 2
            if (SLOT_48 == 2506):
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                SLOT_51 = 3
                HitLow(0)
                Unknown2054(1)
    sprite('Action_257_00', 5)	# 1-5
    sprite('Action_257_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_257_02', 32767)	# 11-32777
    label(1)
    sprite('Action_257_03', 3)	# 32778-32780
    sprite('Action_257_04', 3)	# 32781-32783
    sprite('Action_257_05', 3)	# 32784-32786
    sprite('Action_257_06', 1)	# 32787-32787

@State
def UltimateShotFootEff_Add():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        AttackP2(100)
        Unknown11091(15)
        Damage(500)
        AirUntechableTime(100)
        AirPushbackX(10000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1000)
        Unknown9016(1)
        Unknown11057(750)
        Hitstop(3)
        Unknown30048(1)
        Unknown11064(1)
        Unknown1086(22)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 2504):
                clearUponHandler(43)
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
            if (SLOT_48 == 2505):
                clearUponHandler(43)
            if (SLOT_48 == 2506):
                clearUponHandler(43)
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
    sprite('Action_175_Atk', 7)	# 1-7	 **attackbox here**
    StartMultihit()
    sprite('Action_175_Atk', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    Unknown11069('UltimateShotFootEff_Add')
    sprite('Action_175_Atk', 3)	# 11-13	 **attackbox here**
    Unknown1086(22)
    RefreshMultihit()
    Unknown11069('UltimateShotAtkExe')

@State
def UltimateShotAtkExe():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        AttackP2(100)
        Unknown9016(1)
        Hitstop(0)
        Unknown11001(0, 100, 100)
        Unknown11091(15)
        Unknown11057(750)
        Unknown11064(1)
        Unknown9266(15)
        Damage(500)
        Unknown9154(90)
        AirUntechableTime(90)
        Unknown1086(22)
        Unknown1007(200000)

        def upon_43():
            if (SLOT_48 == 2504):
                clearUponHandler(43)
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                SLOT_51 = 1
            if (SLOT_48 == 2505):
                clearUponHandler(43)
                SLOT_51 = 2
            if (SLOT_48 == 2506):
                clearUponHandler(43)
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                SLOT_51 = 3
    sprite('null', 1)	# 1-1
    sprite('Action_243_00', 3)	# 2-4	 **attackbox here**
    RefreshMultihit()
    Unknown11069('UltimateShotAtkExe')
    sprite('Action_243_01', 3)	# 5-7
    sprite('Action_243_02', 3)	# 8-10
    sprite('Action_243_03', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    sprite('Action_243_04', 3)	# 14-16
    sprite('Action_243_05', 3)	# 17-19
    sprite('null', 9)	# 20-28
    sprite('Action_243_07', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()
    sprite('Action_243_08', 3)	# 32-34
    sprite('Action_243_09', 3)	# 35-37
    sprite('Action_243_10', 3)	# 38-40	 **attackbox here**
    RefreshMultihit()
    sprite('Action_243_11', 3)	# 41-43	 **attackbox here**
    RefreshMultihit()
    sprite('Action_244_00', 2)	# 44-45
    if (SLOT_51 == 1):
        Damage(100)
    elif (SLOT_51 == 2):
        pass
    elif (SLOT_51 == 3):
        Damage(100)
    Unknown1086(22)
    Unknown1007(200000)
    sprite('Action_244_01', 2)	# 46-47
    sprite('Action_244_02', 2)	# 48-49
    sprite('Action_244_03', 2)	# 50-51	 **attackbox here**
    RefreshMultihit()
    sprite('Action_244_04', 2)	# 52-53
    sprite('Action_244_05', 2)	# 54-55
    sprite('Action_244_06', 2)	# 56-57
    sprite('Action_246_00', 3)	# 58-60
    if (SLOT_51 == 1):
        Damage(100)
    elif (SLOT_51 == 2):
        pass
    elif (SLOT_51 == 3):
        Damage(200)
    Unknown1086(22)
    Unknown1007(200000)
    sprite('Action_246_01', 3)	# 61-63	 **attackbox here**
    RefreshMultihit()
    sprite('Action_246_02', 3)	# 64-66
    sprite('Action_246_03', 3)	# 67-69	 **attackbox here**
    RefreshMultihit()
    Unknown11069('UltimateShotAtkFinish')
    if (SLOT_51 == 2):
        Unknown11001(0, 0, 0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        YImpluseBeforeWallbounce(1)
        AirPushbackX(500)
        AirPushbackY(200)
        AirUntechableTime(180)
    elif (SLOT_51 == 3):
        Unknown11001(0, 0, 0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        YImpluseBeforeWallbounce(1)
        AirPushbackX(500)
        AirPushbackY(200)
        AirUntechableTime(180)
    sprite('Action_246_04', 3)	# 70-72
    sprite('Action_246_05', 3)	# 73-75
    sprite('Action_246_06', 3)	# 76-78

@State
def UltimateShotAtkFinish():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Unknown9016(1)
        Hitstop(0)
        Unknown11091(15)
        Unknown11057(750)
        Unknown11064(1)
        Unknown9266(15)
        Damage(500)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(500)
        AirPushbackY(35000)
        AirUntechableTime(90)
        Unknown11001(12, 12, 12)
        Unknown1086(22)
        Unknown1007(200000)

        def upon_43():
            if (SLOT_48 == 2504):
                clearUponHandler(43)
                Damage(300)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                SLOT_51 = 1
            if (SLOT_48 == 2505):
                clearUponHandler(43)
                Unknown11001(10, 10, 10)
                Unknown2037(1)
            if (SLOT_48 == 2506):
                clearUponHandler(43)
                Damage(200)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                Unknown11001(10, 10, 10)
                Unknown2037(1)
                SLOT_51 = 1
    sprite('Action_241_00', 3)	# 1-3
    SFX_3('SE_BigBomb')
    label(0)
    sprite('Action_241_01', 3)	# 4-6	 **attackbox here**
    RefreshMultihit()
    Unknown11069('UltimateShotAtkFinish')
    sprite('Action_241_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_241_02', 1)	# 9-9	 **attackbox here**
    StartMultihit()
    if (not SLOT_2):
        sendToLabel(1)
    sprite('Action_241_03', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    Unknown2037(0)
    gotoLabel(0)
    label(1)
    sprite('Action_241_03', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    if (not SLOT_51):
        Damage(2000)
        AttackP2(60)
    Unknown11069('')
    Unknown11064(0)
    Unknown9266(0)

    def upon_78():
        Unknown23029(3, 2503, 0)
    sprite('Action_241_04', 3)	# 16-18
    sprite('Action_241_05', 3)	# 19-21
    sprite('Action_241_06', 3)	# 22-24

@State
def WinEff1():

    def upon_IMMEDIATE():
        pass
    sprite('Action_087_00', 3)	# 1-3
    sprite('Action_087_01', 3)	# 4-6
    sprite('Action_087_02', 3)	# 7-9

@State
def WinEff2():

    def upon_IMMEDIATE():
        pass
    sprite('Action_088_00', 3)	# 1-3
    sprite('Action_088_01', 3)	# 4-6
    sprite('Action_088_02', 3)	# 7-9
    sprite('Action_088_03', 3)	# 10-12
    sprite('Action_088_04', 3)	# 13-15
    sprite('Action_088_05', 3)	# 16-18
    sprite('Action_088_06', 3)	# 19-21
    sprite('Action_088_07', 3)	# 22-24

@State
def AH_Attack1():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Hitstop(3)
        AirUntechableTime(999)
        YImpluseBeforeWallbounce(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(3000)
        Unknown9016(1)
        Damage(3000)
        Unknown11091(100)
        Unknown1086(22)
        teleportRelativeY(0)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 2611, 0)
    sprite('Action_385_00', 4)	# 1-4
    sprite('Action_385_01', 0)	# 5-4
    sprite('Action_385_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_385_03', 3)	# 8-10	 **attackbox here**
    sprite('Action_385_04', 3)	# 11-13	 **attackbox here**
    sprite('Action_385_05', 3)	# 14-16
    sprite('Action_385_06', 3)	# 17-19
    sprite('Action_385_07', 3)	# 20-22
    sprite('Action_385_08', 3)	# 23-25
    sprite('Action_385_09', 3)	# 26-28
    sprite('Action_385_10', 3)	# 29-31
    sprite('Action_385_11', 3)	# 32-34
    sprite('Action_385_12', 3)	# 35-37

@State
def AH_Attack2():

    def upon_IMMEDIATE():
        Unknown1086(3)
        teleportRelativeY(0)
        Unknown2037(8)
    sprite('Action_386_00', 7)	# 1-7
    sprite('Action_386_01', 7)	# 8-14
    sprite('Action_386_02', 7)	# 15-21
    sprite('Action_386_03', 7)	# 22-28
    sprite('Action_386_04', 7)	# 29-35
    label(0)
    sprite('Action_386_05', 7)	# 36-42
    if (not SLOT_2):
        sendToLabel(1)
    sprite('Action_386_06', 7)	# 43-49
    sprite('Action_386_07', 7)	# 50-56
    sprite('Action_386_08', 7)	# 57-63
    sprite('Action_386_09', 7)	# 64-70
    loopRest()
    Unknown2038(-1)
    gotoLabel(0)
    label(1)
    sprite('Action_386_10', 7)	# 71-77
    sprite('Action_386_11', 7)	# 78-84
    sprite('Action_386_12', 7)	# 85-91
    sprite('Action_386_13', 7)	# 92-98
    sprite('Action_386_14', 7)	# 99-105

@State
def AH_Attack3():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(450)
        Unknown11091(100)
        AirUntechableTime(999)
        YImpluseBeforeWallbounce(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(1)
        Hitstop(0)
        Unknown9016(1)
        Unknown23151(22, 103)
        Unknown2019(-500)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 2612, 0)
    sprite('Action_387_00', 5)	# 1-5	 **attackbox here**
    Unknown1007(-100000)
    sprite('Action_387_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_387_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_387_03', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_387_03', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_387_03', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_387_04', 5)	# 21-25	 **attackbox here**
    sprite('Action_387_05', 5)	# 26-30	 **attackbox here**
    sprite('Action_387_06', 5)	# 31-35	 **attackbox here**
    sprite('Action_387_07', 5)	# 36-40	 **attackbox here**
    sprite('Action_387_08', 5)	# 41-45	 **attackbox here**
    sprite('Action_387_09', 5)	# 46-50	 **attackbox here**
    sprite('Action_387_10', 60)	# 51-110	 **attackbox here**
    sprite('Action_387_11', 5)	# 111-115	 **attackbox here**
    sprite('Action_387_12', 5)	# 116-120	 **attackbox here**
    RefreshMultihit()
    Unknown11057(800)
    Unknown21015('41485f5368616b65000000000000000000000000000000000000000000000000340a000000000000')
    sprite('Action_387_13', 5)	# 121-125	 **attackbox here**
    RefreshMultihit()
    Unknown2037(24)
    label(0)
    sprite('Action_387_14', 5)	# 126-130	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    loopRest()
    if (not SLOT_2):
        sendToLabel(1)
    gotoLabel(0)
    label(1)
    sprite('Action_387_14', 55)	# 131-185	 **attackbox here**
    sprite('Action_387_15', 5)	# 186-190	 **attackbox here**
    RefreshMultihit()
    Damage(5000)
    Unknown11091(100)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    AirPushbackY(0)
    YImpluseBeforeWallbounce(0)
    SFX_3('SE_BigBomb')
    GFX_0('AH_Attack5', -1)
    Unknown36(22)
    Unknown3026(0)
    Unknown35()
    GFX_0('AH_Rock_Matome', -1)
    sprite('Action_387_16', 5)	# 191-195	 **attackbox here**
    sprite('Action_387_17', 5)	# 196-200	 **attackbox here**
    sprite('Action_387_18', 5)	# 201-205	 **attackbox here**
    sprite('Action_387_19', 5)	# 206-210	 **attackbox here**
    sprite('Action_387_20', 9)	# 211-219	 **attackbox here**
    sprite('Action_387_20', 1)	# 220-220	 **attackbox here**
    GFX_0('AH_Attack_Dmy', -1)
    Unknown26('AH_Attack2')
    Unknown26('AH_BG')
    Unknown26('AH_Shake')
    Unknown21015('41485f43616d65726100000000000000000000000000000000000000000000003b0a000000000000')
    Unknown23029(3, 2619, 0)
    sprite('null', 40)	# 221-260
    sprite('null', 1)	# 261-261
    Unknown26('AH_Rock_Matome')
    Unknown36(22)
    Unknown3026(-1)
    Unknown35()

@State
def AH_Attack_Dmy():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(8500)
        Unknown11091(100)
        Unknown11064(3)
        Unknown3001(0)
        Unknown11023(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        AirPushbackX(0)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(2000)
        Hitstop(0)
    sprite('Action_387_03', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    Unknown36(22)
    teleportRelativeY(1200000)
    Unknown2054(1)
    Unknown35()

@State
def AH_Attack4():

    def upon_IMMEDIATE():
        Unknown1086(3)
    sprite('Action_384_00', 3)	# 1-3
    sprite('Action_384_01', 3)	# 4-6
    sprite('Action_384_02', 3)	# 7-9
    sprite('Action_384_03', 3)	# 10-12
    sprite('Action_384_04', 3)	# 13-15
    sprite('Action_384_05', 3)	# 16-18
    sprite('Action_384_06', 3)	# 19-21
    sprite('Action_384_07', 3)	# 22-24

@State
def AH_Attack5():
    sprite('Action_389_00', 5)	# 1-5
    sprite('Action_389_01', 5)	# 6-10

@State
def AH_Rock_Matome():
    sprite('null', 500)	# 1-500
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(8000, 18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, 8000)
    Unknown1026(-8000, -18000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(8000, 18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()
    GFX_0('AH_Rock', -1)
    Unknown36(1)
    Unknown1025(-8000, -18000)
    Unknown1026(8000, -8000)
    Unknown35()

@State
def AH_Rock():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown4010(2)
        Unknown23015(1)
        Unknown1079()
    Unknown61(0, 0, 0, 6, 0, 9999, 0, 9999, 0, 9999, 0, 9999)
    SLOT_2 = SLOT_0
    if (SLOT_2 == 0):
        sendToLabel(0)
    elif (SLOT_2 == 1):
        sendToLabel(1)
    elif (SLOT_2 == 2):
        sendToLabel(2)
    elif (SLOT_2 == 3):
        sendToLabel(3)
    elif (SLOT_2 == 4):
        sendToLabel(4)
    elif (SLOT_2 == 1):
        sendToLabel(5)
    elif (SLOT_2 == 6):
        sendToLabel(6)
    label(0)
    sprite('Action_388_00', 15)	# 1-15
    sprite('Action_388_01', 15)	# 16-30
    sprite('Action_388_02', 15)	# 31-45
    ExitState()
    label(1)
    sprite('Action_388_04', 15)	# 46-60
    sprite('Action_388_05', 15)	# 61-75
    sprite('Action_388_06', 15)	# 76-90
    ExitState()
    label(2)
    sprite('Action_388_08', 15)	# 91-105
    sprite('Action_388_09', 15)	# 106-120
    sprite('Action_388_10', 15)	# 121-135
    ExitState()
    label(3)
    sprite('Action_388_12', 15)	# 136-150
    sprite('Action_388_13', 15)	# 151-165
    sprite('Action_388_14', 15)	# 166-180
    ExitState()
    label(4)
    sprite('Action_388_16', 15)	# 181-195
    sprite('Action_388_17', 15)	# 196-210
    sprite('Action_388_18', 15)	# 211-225
    ExitState()
    label(5)
    sprite('Action_388_20', 15)	# 226-240
    sprite('Action_388_21', 15)	# 241-255
    sprite('Action_388_22', 15)	# 256-270
    ExitState()
    label(6)
    sprite('Action_388_24', 15)	# 271-285
    sprite('Action_388_25', 15)	# 286-300
    sprite('Action_388_26', 15)	# 301-315

@State
def AH_White():
    sprite('vr_white', 40)	# 1-40
    Unknown2019(-500)
    Unknown3032()
    Unknown3001(0)
    Unknown3004(20)
    Unknown1096(4000)
    sprite('vr_white', 20)	# 41-60
    Unknown3004(-10)
    GFX_0('AH_Shake', -1)
    sprite('vr_white', 10)	# 61-70
    Unknown21015('41485f5368616b65000000000000000000000000000000000000000000000000330a000000000000')

@State
def AH_BG():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown1000(0)
        teleportRelativeY(350000)
        Unknown1056(1200)
        Unknown2055(1500)
    sprite('Action_392_00', 3)	# 1-3
    sprite('Action_392_01', 3)	# 4-6
    sprite('Action_392_02', 3)	# 7-9
    sprite('Action_392_03', 3)	# 10-12
    sprite('Action_392_04', 32767)	# 13-32779

@State
def AH_Shake():

    def upon_IMMEDIATE():
        Unknown2055(1500)

        def upon_43():
            if (SLOT_48 == 2611):
                sendToLabel(0)
            if (SLOT_48 == 2612):
                sendToLabel(1)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 5)	# 32768-32772
    ScreenShake(1500, 1500)
    gotoLabel(0)
    label(1)
    sprite('null', 5)	# 32773-32777
    ScreenShake(3000, 3000)
    gotoLabel(1)

@State
def AH_Wave_Matome():

    def upon_IMMEDIATE():
        Unknown2037(10)
    label(0)
    sprite('null', 2)	# 1-2
    GFX_0('AH_Wave', 100)
    Unknown2038(-1)
    loopRest()
    if (not SLOT_2):
        sendToLabel(1)
    gotoLabel(0)
    label(1)

@State
def AH_Wave():

    def upon_IMMEDIATE():
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown1010(-800000, 800000)
    sprite('Action_391_00', 10)	# 1-10
    sprite('Action_391_01', 10)	# 11-20
    sprite('Action_391_02', 1)	# 21-21
    sprite('Action_391_03', 10)	# 22-31
    sprite('Action_391_04', 10)	# 32-41
    sprite('Action_391_05', 1)	# 42-42
    sprite('Action_391_06', 10)	# 43-52
    sprite('Action_391_07', 10)	# 53-62
    sprite('Action_391_08', 1)	# 63-63

@State
def AH_Camera():

    def upon_IMMEDIATE():
        Unknown20009(1000)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown2054(1)
        Unknown20003(1)

        def upon_STATE_END():
            Unknown20000(0)

        def upon_43():
            if (SLOT_48 == 2611):
                sendToLabel(0)
            if (SLOT_48 == 2619):
                sendToLabel(1)
    sprite('null', 10)	# 1-10
    sprite('null', 999)	# 11-1009
    Unknown20000(1)
    ExitState()
    label(0)
    sprite('null', 30)	# 1010-1039
    sprite('null', 300)	# 1040-1339
    Unknown1086(22)
    Unknown1007(150000)
    Unknown20009(820)
    ExitState()
    label(1)
    sprite('null', 20)	# 1340-1359
    Unknown20009(1000)
    teleportRelativeY(2000000)
    sprite('null', 100)	# 1360-1459
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown20000(1)
    Unknown20001(1)

@State
def TagCutIn():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(2000)
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-580000)
        Unknown1001(640000)
        SFX_0('301_overdrive_end')
        loopRelated(17, 30)

        def upon_17():
            sendToLabel(1)
    sprite('Action_997_01', 2)	# 1-2
    sprite('Action_997_02', 2)	# 3-4
    sprite('Action_997_03', 2)	# 5-6
    label(0)
    sprite('Action_997_04', 3)	# 7-9
    sprite('Action_997_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 13-13

@State
def DDCutIn():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_999_01', 2)	# 1-2
    sprite('Action_999_02', 2)	# 3-4
    sprite('Action_999_03', 2)	# 5-6
    sprite('Action_999_04', 4)	# 7-10
    sprite('Action_999_05', 6)	# 11-16
    sprite('Action_999_06', 3)	# 17-19
    sprite('Action_999_07', 2)	# 20-21
    sprite('Action_999_08', 3)	# 22-24
    sprite('Action_999_09', 3)	# 25-27
    sprite('Action_999_10', 3)	# 28-30
    sprite('Action_999_11', 5)	# 31-35
    sprite('Action_999_12', 8)	# 36-43
    sprite('Action_999_13', 6)	# 44-49
    sprite('Action_999_14', 4)	# 50-53
    sprite('Action_999_15', 3)	# 54-56
    sprite('Action_999_16', 3)	# 57-59	 **attackbox here**
    sprite('Action_999_17', 3)	# 60-62	 **attackbox here**
    physicsXImpulse(30800)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)
    sprite('Action_999_18', 3)	# 63-65	 **attackbox here**
    sprite('Action_999_19', 3)	# 66-68	 **attackbox here**
    sprite('Action_999_20', 1)	# 69-69	 **attackbox here**

@State
def BurstAtkEff():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(350)
        AttackP2(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        Unknown11042(1)
        AirPushbackY(30000)
        AirUntechableTime(90)
        Unknown9016(1)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown23027()
    sprite('Action_385_01', 4)	# 1-4
    sprite('Action_385_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_385_03', 3)	# 8-10	 **attackbox here**
    sprite('Action_385_04', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    sprite('Action_385_05', 3)	# 14-16
    sprite('Action_385_06', 3)	# 17-19
    sprite('Action_385_07', 3)	# 20-22
    sprite('Action_385_08', 3)	# 23-25
    sprite('Action_385_09', 3)	# 26-28
    sprite('Action_385_10', 3)	# 29-31
    sprite('Action_385_11', 3)	# 32-34
    sprite('Action_385_12', 3)	# 35-37

@State
def ef_hitlm_test():

    def upon_IMMEDIATE():
        Unknown1077(0, 360000)
        Unknown1096(1100)
    sprite('null', 1)	# 1-1
    GFX_2('ef_hitlm')
    sprite('null', 18)	# 2-19

@State
def ef_hitmm_test():

    def upon_IMMEDIATE():
        Unknown1077(0, 360000)
        Unknown1096(950)
    sprite('null', 1)	# 1-1
    GFX_2('ef_hitmm')
    sprite('null', 18)	# 2-19

@State
def ef_hitsm_test():

    def upon_IMMEDIATE():
        Unknown1077(0, 360000)
        Unknown1096(900)
    sprite('null', 1)	# 1-1
    GFX_2('ef_hitsm')
    sprite('null', 18)	# 2-19

@State
def RejectGuardEff_test():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
    sprite('null', 32)	# 1-32
    GFX_2('ef_reject_guard')

@State
def RejectGuardEff_test2():

    def upon_IMMEDIATE():
        teleportRelativeX(150000)
    sprite('null', 32)	# 1-32
    GFX_2('ef_girdm')

@State
def CrossBurstEff_test():

    def upon_IMMEDIATE():
        pass
    sprite('null', 32)	# 1-32
    GFX_1('ef_throw_test', -1)

@State
def Win1():

    def upon_IMMEDIATE():
        pass
    sprite('Action_087_00', 3)	# 1-3
    sprite('Action_087_01', 3)	# 4-6
    sprite('Action_087_02', 3)	# 7-9

@State
def Win2():

    def upon_IMMEDIATE():
        pass
    sprite('Action_088_00', 3)	# 1-3
    sprite('Action_088_01', 3)	# 4-6
    sprite('Action_088_02', 3)	# 7-9
    sprite('Action_088_03', 3)	# 10-12
    sprite('Action_088_04', 3)	# 13-15
    sprite('Action_088_05', 3)	# 16-18
    sprite('Action_088_06', 3)	# 19-21
    sprite('Action_088_07', 3	# 22-24
