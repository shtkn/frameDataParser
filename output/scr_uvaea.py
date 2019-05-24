@State
def Vat_191():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    label(0)
    sprite('Action_191_00', 5)	# 1-5
    sprite('Action_191_01', 5)	# 6-10
    sprite('Action_191_02', 5)	# 11-15
    sprite('Action_191_03', 5)	# 16-20
    sprite('Action_191_04', 5)	# 21-25
    sprite('Action_191_05', 5)	# 26-30
    loopRest()
    gotoLabel(0)

@State
def Vat_238():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(90000)
        teleportRelativeX(150000)
        Unknown1007(260000)
    sprite('Action_238_00', 3)	# 1-3
    SFX_3('SE_AppearBit')
    sprite('Action_238_01', 3)	# 4-6
    sprite('Action_238_02', 3)	# 7-9

@State
def Vat_238_2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(90000)
        teleportRelativeX(150000)
        Unknown1007(260000)
    sprite('Action_238_03', 3)	# 1-3
    SFX_3('SE_AppearBit')
    sprite('Action_238_04', 3)	# 4-6
    sprite('Action_238_05', 3)	# 7-9

@State
def Vat_250():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('Action_250_00', 4)	# 1-4
    SFX_3('SE_AppearBit')
    sprite('Action_250_01', 4)	# 5-8
    sprite('Action_250_02', 4)	# 9-12

@State
def Vat_251():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('Action_251_00', 4)	# 1-4
    sprite('Action_251_01', 4)	# 5-8
    sprite('Action_251_02', 4)	# 9-12

@State
def Vat_240():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('Action_240_00', 4)	# 1-4	 **attackbox here**
    SFX_3('SE_AppearBit')
    sprite('Action_240_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_240_02', 4)	# 9-12	 **attackbox here**

@State
def Vat_238Air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(125000)
        teleportRelativeX(100000)
        Unknown1007(200000)
    sprite('Action_238_00', 3)	# 1-3
    SFX_3('SE_AppearBit')
    sprite('Action_238_01', 3)	# 4-6
    sprite('Action_238_02', 3)	# 7-9

@State
def Vat_238_2Air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(125000)
        teleportRelativeX(100000)
        Unknown1007(200000)
    sprite('Action_238_03', 3)	# 1-3
    SFX_3('SE_AppearBit')
    sprite('Action_238_04', 3)	# 4-6
    sprite('Action_238_05', 3)	# 7-9

@State
def Vat_250Air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(35000)
        teleportRelativeX(-160000)
        Unknown1007(43000)
    sprite('Action_250_00', 4)	# 1-4
    SFX_3('SE_AppearBit')
    sprite('Action_250_01', 4)	# 5-8
    sprite('Action_250_02', 4)	# 9-12

@State
def Vat_251Air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(35000)
        teleportRelativeX(-140000)
        Unknown1007(54000)
    sprite('Action_251_00', 4)	# 1-4
    sprite('Action_251_01', 4)	# 5-8
    sprite('Action_251_02', 4)	# 9-12

@State
def Vat_240Air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(35000)
        teleportRelativeX(-150000)
        Unknown1007(47000)
    sprite('Action_240_00', 4)	# 1-4	 **attackbox here**
    SFX_3('SE_AppearBit')
    sprite('Action_240_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_240_02', 4)	# 9-12	 **attackbox here**

@State
def Vat_242():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(3)
    sprite('Action_242_00', 4)	# 1-4
    SFX_3('SE_AppearBit')
    sprite('Action_242_01', 4)	# 5-8
    sprite('Action_242_02', 4)	# 9-12

@State
def Vat_242_2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(3)
    sprite('Action_242_03', 4)	# 1-4
    SFX_3('SE_AppearBit')
    sprite('Action_242_04', 4)	# 5-8
    sprite('Action_242_05', 4)	# 9-12

@State
def Vat_086():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000000000000010000000000000000000000')
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(15000)
        AirUntechableTime(30)
        Unknown9016(1)
        HitLow(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23027()
        Unknown23078(1)
    sprite('Action_086_00', 6)	# 1-6	 **attackbox here**
    physicsXImpulse(60000)
    sprite('Action_086_01', 7)	# 7-13	 **attackbox here**
    Unknown1084(1)
    sprite('Action_086_02', 8)	# 14-21
    physicsXImpulse(-40000)
    sprite('Action_086_03', 9)	# 22-30
    sprite('Action_086_04', 2)	# 31-32
    sprite('Action_086_05', 5)	# 33-37

@State
def Vat_074():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('Action_074_00', 3)	# 1-3
    sprite('Action_074_01', 7)	# 4-10
    sprite('Action_074_02', 1)	# 11-11

@State
def Vat_073():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('Action_073_00', 5)	# 1-5
    sprite('Action_073_01', 5)	# 6-10
    sprite('Action_073_02', 5)	# 11-15
    sprite('Action_073_03', 5)	# 16-20
    sprite('Action_073_04', 5)	# 21-25
    sprite('Action_073_05', 1)	# 26-26

@Subroutine
def Beam_Init():
    Unknown4007(3)
    Unknown4009(3)
    AttackLevel_(5)
    Damage(2000)
    AttackP2(85)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(15000)
    AirPushbackY(20000)
    Hitstop(9)
    AirUntechableTime(60)
    PushbackX(12000)
    Unknown9266(14)
    Unknown23027()
    Unknown23089('0100000000000000000000000000000000000000010000000100000001000000')

    def upon_54():
        clearUponHandler(54)
        Unknown4007(0)
        Unknown4009(0)
        sendToLabel(9)

@State
def Vat_097():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Beam_Init')
        teleportRelativeX(110000)
        Unknown1007(250000)
    sprite('Action_097_00', 2)	# 1-2	 **attackbox here**
    SFX_3('SE_LaserBeam')
    sprite('Action_097_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_097_02', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_097_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_097_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_097_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_097_06', 2)	# 13-14	 **attackbox here**
    sprite('Action_097_07', 2)	# 15-16	 **attackbox here**
    Unknown23029(3, 1100, 0)
    Unknown23027()
    sprite('Action_097_08', 2)	# 17-18	 **attackbox here**
    sprite('Action_097_09', 2)	# 19-20	 **attackbox here**
    sprite('Action_097_10', 2)	# 21-22	 **attackbox here**
    sprite('Action_097_11', 2)	# 23-24	 **attackbox here**
    label(9)
    sprite('Action_097_12', 2)	# 25-26	 **attackbox here**
    clearUponHandler(54)
    Unknown4007(0)
    Unknown4009(0)
    Unknown23027()
    sprite('Action_097_13', 2)	# 27-28	 **attackbox here**
    sprite('Action_097_14', 2)	# 29-30	 **attackbox here**
    sprite('Action_097_15', 1)	# 31-31	 **attackbox here**

@State
def Vat_097_AAir():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Beam_Init')
        AirPushbackX(20000)
        AirPushbackY(10000)
        teleportRelativeX(110000)
        Unknown1007(250000)
    sprite('Action_097_00', 2)	# 1-2	 **attackbox here**
    SFX_3('SE_LaserBeam')
    sprite('Action_097_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_097_02', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_097_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_097_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_097_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_097_06', 2)	# 13-14	 **attackbox here**
    sprite('Action_097_07', 2)	# 15-16	 **attackbox here**
    Unknown23029(3, 1100, 0)
    Unknown23027()
    sprite('Action_097_08', 2)	# 17-18	 **attackbox here**
    sprite('Action_097_09', 2)	# 19-20	 **attackbox here**
    sprite('Action_097_11', 2)	# 21-22	 **attackbox here**
    label(9)
    sprite('Action_097_12', 2)	# 23-24	 **attackbox here**
    clearUponHandler(54)
    Unknown4007(0)
    Unknown4009(0)
    Unknown23027()
    sprite('Action_097_13', 2)	# 25-26	 **attackbox here**
    sprite('Action_097_14', 2)	# 27-28	 **attackbox here**
    sprite('Action_097_15', 1)	# 29-29	 **attackbox here**

@State
def Vat_097_B():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Beam_Init')
        Unknown1072(-25000)
        teleportRelativeX(110000)
        Unknown1007(250000)
    sprite('Action_097_00ex', 2)	# 1-2	 **attackbox here**
    SFX_3('SE_LaserBeam')
    sprite('Action_097_01ex', 2)	# 3-4	 **attackbox here**
    sprite('Action_097_02ex', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_097_03ex', 2)	# 7-8	 **attackbox here**
    sprite('Action_097_04ex', 2)	# 9-10	 **attackbox here**
    sprite('Action_097_05ex', 2)	# 11-12	 **attackbox here**
    sprite('Action_097_06ex', 2)	# 13-14	 **attackbox here**
    sprite('Action_097_07ex', 2)	# 15-16	 **attackbox here**
    Unknown23029(3, 1100, 0)
    Unknown23027()
    sprite('Action_097_08ex', 2)	# 17-18	 **attackbox here**
    sprite('Action_097_09ex', 2)	# 19-20	 **attackbox here**
    sprite('Action_097_10ex', 2)	# 21-22	 **attackbox here**
    sprite('Action_097_11ex', 2)	# 23-24	 **attackbox here**
    label(9)
    sprite('Action_097_12ex', 2)	# 25-26	 **attackbox here**
    clearUponHandler(54)
    Unknown4007(0)
    Unknown4009(0)
    Unknown23027()
    sprite('Action_097_13ex', 2)	# 27-28	 **attackbox here**
    sprite('Action_097_14ex', 2)	# 29-30	 **attackbox here**
    sprite('Action_097_15ex', 1)	# 31-31	 **attackbox here**

@State
def Vat_097_BAir():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Beam_Init')
        AirPushbackX(20000)
        AirPushbackY(10000)
        Unknown1072(27500)
        teleportRelativeX(125000)
        Unknown1007(205000)
    sprite('Action_097_00ex', 2)	# 1-2	 **attackbox here**
    SFX_3('SE_LaserBeam')
    sprite('Action_097_01ex', 2)	# 3-4	 **attackbox here**
    sprite('Action_097_02ex', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_097_03ex', 2)	# 7-8	 **attackbox here**
    sprite('Action_097_04ex', 2)	# 9-10	 **attackbox here**
    sprite('Action_097_05ex', 2)	# 11-12	 **attackbox here**
    sprite('Action_097_06ex', 2)	# 13-14	 **attackbox here**
    sprite('Action_097_07ex', 2)	# 15-16	 **attackbox here**
    Unknown23029(3, 1100, 0)
    Unknown23027()
    sprite('Action_097_08ex', 2)	# 17-18	 **attackbox here**
    sprite('Action_097_09ex', 2)	# 19-20	 **attackbox here**
    sprite('Action_097_11ex', 2)	# 21-22	 **attackbox here**
    label(9)
    sprite('Action_097_12ex', 2)	# 23-24	 **attackbox here**
    clearUponHandler(54)
    Unknown4007(0)
    Unknown4009(0)
    Unknown23027()
    sprite('Action_097_13ex', 2)	# 25-26	 **attackbox here**
    sprite('Action_097_14ex', 2)	# 27-28	 **attackbox here**
    sprite('Action_097_15ex', 1)	# 29-29	 **attackbox here**

@State
def Vat_097asi():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Beam_Init')
        AttackP1(70)
        Unknown9071()
        AirPushbackY(42000)
        Unknown11042(1)
        Unknown1072(-25000)
        teleportRelativeX(110000)
        Unknown1007(250000)
    sprite('Action_097_00ex', 2)	# 1-2	 **attackbox here**
    SFX_3('SE_LaserBeam')
    sprite('Action_097_01ex', 2)	# 3-4	 **attackbox here**
    sprite('Action_097_02ex', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_097_03ex', 2)	# 7-8	 **attackbox here**
    sprite('Action_097_04ex', 2)	# 9-10	 **attackbox here**
    sprite('Action_097_05ex', 2)	# 11-12	 **attackbox here**
    sprite('Action_097_06ex', 2)	# 13-14	 **attackbox here**
    sprite('Action_097_07ex', 2)	# 15-16	 **attackbox here**
    Unknown23029(3, 1100, 0)
    Unknown23027()
    sprite('Action_097_08ex', 2)	# 17-18	 **attackbox here**
    sprite('Action_097_09ex', 2)	# 19-20	 **attackbox here**
    sprite('Action_097_10ex', 2)	# 21-22	 **attackbox here**
    sprite('Action_097_11ex', 2)	# 23-24	 **attackbox here**
    label(9)
    sprite('Action_097_12ex', 2)	# 25-26	 **attackbox here**
    clearUponHandler(54)
    Unknown4007(0)
    Unknown4009(0)
    Unknown23027()
    sprite('Action_097_13ex', 2)	# 27-28	 **attackbox here**
    sprite('Action_097_14ex', 2)	# 29-30	 **attackbox here**
    sprite('Action_097_15ex', 1)	# 31-31	 **attackbox here**

@State
def Vat_083():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Beam_Init')
        Damage(2500)
        AirPushbackX(45000)
        Unknown30065(0)
        Unknown11091(10)
    sprite('Action_083_00', 2)	# 1-2	 **attackbox here**
    SFX_3('SE_LaserBeam')
    sprite('Action_083_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_083_02', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_083_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_083_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_083_06', 2)	# 13-14	 **attackbox here**
    sprite('Action_083_07', 2)	# 15-16	 **attackbox here**
    Unknown23029(3, 1100, 0)
    sprite('Action_083_08', 2)	# 17-18	 **attackbox here**
    sprite('Action_083_09', 2)	# 19-20	 **attackbox here**
    sprite('Action_083_10', 2)	# 21-22	 **attackbox here**
    sprite('Action_083_11', 2)	# 23-24	 **attackbox here**
    label(9)
    sprite('Action_083_12', 2)	# 25-26	 **attackbox here**
    clearUponHandler(54)
    Unknown4007(0)
    Unknown4009(0)
    Unknown23027()
    sprite('Action_083_13', 2)	# 27-28	 **attackbox here**
    sprite('Action_083_14', 2)	# 29-30	 **attackbox here**

@Subroutine
def Shot_Init():
    AttackLevel_(3)
    AttackP1(80)
    AirPushbackX(10000)
    AirPushbackY(16000)
    Unknown9154(24)
    AirUntechableTime(30)
    Unknown9266(14)
    Unknown53(1)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        GFX_0('Vat_078', -1)
        SFX_3('SE_BombEnergy')
    Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

    def upon_54():
        Unknown13(25)
        GFX_0('Vat_096', -1)

@State
def Vat_095():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Init')

        def upon_43():
            if (SLOT_48 == 1000):
                Unknown13(25)
                GFX_0('Vat_096', -1)
    sprite('Action_095_00', 10)	# 1-10	 **attackbox here**
    physicsXImpulse(20000)
    label(0)
    sprite('Action_095_01', 10)	# 11-20	 **attackbox here**
    sprite('Action_095_02', 10)	# 21-30	 **attackbox here**
    sprite('Action_095_03', 10)	# 31-40	 **attackbox here**
    sprite('Action_095_04', 10)	# 41-50	 **attackbox here**
    sprite('Action_095_05', 10)	# 51-60	 **attackbox here**
    sprite('Action_095_06', 10)	# 61-70	 **attackbox here**
    gotoLabel(0)

@State
def Vat_101():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(90000)
    sprite('Action_101_00', 5)	# 1-5
    sprite('Action_101_01', 5)	# 6-10
    sprite('Action_101_02', 5)	# 11-15
    sprite('Action_101_03', 5)	# 16-20
    sprite('Action_101_04', 1)	# 21-21

@State
def Vat_095_B():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Init')
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)

        def upon_43():
            if (SLOT_48 == 1001):
                Unknown13(25)
                GFX_0('Vat_096', -1)
    sprite('Action_095_00', 10)	# 1-10	 **attackbox here**
    physicsXImpulse(52000)
    label(0)
    sprite('Action_095_01', 10)	# 11-20	 **attackbox here**
    sprite('Action_095_02', 10)	# 21-30	 **attackbox here**
    sprite('Action_095_03', 10)	# 31-40	 **attackbox here**
    sprite('Action_095_04', 10)	# 41-50	 **attackbox here**
    sprite('Action_095_05', 10)	# 51-60	 **attackbox here**
    sprite('Action_095_06', 10)	# 61-70	 **attackbox here**
    gotoLabel(0)

@State
def Vat_095_Basi():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Init')
        AttackP1(70)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        Unknown11042(1)

        def upon_43():
            if (SLOT_48 == 1001):
                Unknown13(25)
                GFX_0('Vat_096', -1)
    sprite('Action_095_00', 10)	# 1-10	 **attackbox here**
    physicsXImpulse(52000)
    label(0)
    sprite('Action_095_01', 10)	# 11-20	 **attackbox here**
    sprite('Action_095_02', 10)	# 21-30	 **attackbox here**
    sprite('Action_095_03', 10)	# 31-40	 **attackbox here**
    sprite('Action_095_04', 10)	# 41-50	 **attackbox here**
    sprite('Action_095_05', 10)	# 51-60	 **attackbox here**
    sprite('Action_095_06', 10)	# 61-70	 **attackbox here**
    gotoLabel(0)

@State
def Vat_101_B():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown1072(90000)
    sprite('Action_101_00', 5)	# 1-5
    sprite('Action_101_01', 5)	# 6-10
    sprite('Action_101_02', 5)	# 11-15
    sprite('Action_101_03', 5)	# 16-20
    sprite('Action_101_04', 1)	# 21-21

@State
def Vat_078():

    def upon_IMMEDIATE():
        Unknown1072(270000)
    sprite('Action_078_00', 5)	# 1-5
    sprite('Action_078_01', 5)	# 6-10
    sprite('Action_078_02', 5)	# 11-15
    sprite('Action_078_03', 5)	# 16-20
    sprite('Action_078_04', 1)	# 21-21

@State
def Vat_096():

    def upon_IMMEDIATE():
        pass
    sprite('Action_096_00', 10)	# 1-10
    sprite('Action_096_01', 10)	# 11-20
    sprite('Action_096_02', 10)	# 21-30
    sprite('Action_096_03', 10)	# 31-40
    sprite('Action_096_04', 1)	# 41-41

@State
def Vat_083ds():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown23056('')
        AttackLevel_(4)
        Damage(500)
        AttackP1(48)
        AttackP2(100)
        Unknown11092(1)
        Unknown11091(20)
        Hitstop(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(60)
        AirPushbackX(40000)
        AirPushbackY(10000)
        Unknown11001(0, 9, 9)
        Unknown9266(14)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = (SLOT_51 + 1)

        def upon_3():
            if (SLOT_51 >= 10):
                Unknown23027()
    sprite('Action_083_00', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    sprite('Action_083_01', 2)	# 3-4	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_02', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_03', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_04', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_05', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_06', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_07', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_08', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_09', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_10', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_11', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_12', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_13', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    sprite('Action_083_14', 2)	# 29-30	 **attackbox here**

@State
def Vat_095_3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        physicsXImpulse(60000)
        AirPushbackX(20000)
        Unknown1056(800)
        Unknown1064(800)
        Hitstop(1)
        Unknown11001(0, 9, 9)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown53(1)
        Unknown9266(14)

        def upon_12():
            sendToLabel(0)
        Unknown23089('0500000001000000010000000000000000000000000000000500000005000000')

        def upon_54():
            Unknown13(25)
            GFX_0('Vat_085', -1)

        def upon_43():
            if (SLOT_48 == 1003):
                Unknown13(25)
                GFX_0('Vat_085', -1)
    label(0)
    sprite('Action_099_00', 10)	# 1-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_01', 10)	# 11-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_02', 10)	# 21-30	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_03', 10)	# 31-40	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_04', 10)	# 41-50	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_05', 10)	# 51-60	 **attackbox here**
    RefreshMultihit()
    gotoLabel(0)

@State
def Vat_105_A():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1072(90000)
    sprite('Action_105_00', 5)	# 1-5
    sprite('Action_105_01', 32)	# 6-37
    GFX_0('Vat_107', 0)
    sprite('Action_102_00', 5)	# 38-42
    sprite('Action_102_01', 5)	# 43-47
    sprite('Action_102_02', 5)	# 48-52
    sprite('Action_102_03', 5)	# 53-57
    sprite('Action_102_04', 1)	# 58-58
    Unknown26('Vat_107')

@State
def Vat_107():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1072(90000)
    label(0)
    sprite('Action_107_00', 10)	# 1-10
    sprite('Action_107_01', 10)	# 11-20
    sprite('Action_107_02', 10)	# 21-30
    sprite('Action_107_03', 10)	# 31-40
    sprite('Action_107_04', 10)	# 41-50
    gotoLabel(0)

@State
def Vat_085():

    def upon_IMMEDIATE():
        pass
    sprite('Action_085_00', 10)	# 1-10
    sprite('Action_085_01', 10)	# 11-20
    sprite('Action_085_02', 10)	# 21-30
    sprite('Action_085_03', 10)	# 31-40
    sprite('Action_085_04', 1)	# 41-41

@State
def Vat_095_4():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Init')
        Damage(900)
        Unknown11092(1)
        Hitstop(5)
        Unknown30065(0)
        Unknown11091(10)

        def upon_ON_HIT_OR_BLOCK():
            Unknown1017()
            Unknown2037(4)

        def upon_3():
            if SLOT_2:
                Unknown1019(60)
                Unknown2038(-1)
                Unknown2053(1)
            else:
                Unknown2053(0)
                physicsXImpulse(52000)
        Unknown23089('0300000001000000010000000100000001000000000000000300000003000000')

        def upon_54():
            Unknown1084(1)
            Unknown13(25)
            GFX_0('Vat_085', -1)

        def upon_43():
            if (SLOT_48 == 1200):
                AttackP1(70)
                Unknown11042(1)
                Unknown30065(50)
                Unknown11091(0)
                GroundedHitstunAnimation(9)
    label(0)
    sprite('Action_099_00', 5)	# 1-5	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_00', 5)	# 6-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_01', 5)	# 11-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_01', 5)	# 16-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_02', 5)	# 21-25	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_02', 5)	# 26-30	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_03', 5)	# 31-35	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_03', 5)	# 36-40	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_04', 5)	# 41-45	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_04', 5)	# 46-50	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_05', 5)	# 51-55	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_05', 5)	# 56-60	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)

@State
def Vat_095_4Air():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Init')
        Damage(900)
        Unknown11092(1)
        Hitstop(5)
        Unknown30065(0)
        Unknown11091(10)
        physicsXImpulse(6000)
        physicsYImpulse(5000)
        setGravity(800)
        Unknown23026(100000)

        def upon_5():
            physicsXImpulse(6000)
            physicsYImpulse(20000)
            setGravity(800)
            Unknown8000(104, 1, 0)
        Unknown23089('0300000001000000010000000100000001000000000000000300000003000000')

        def upon_54():
            Unknown1084(1)
            Unknown13(25)
            GFX_0('Vat_085', -1)
    label(0)
    sprite('Action_099_00', 10)	# 1-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_01', 10)	# 11-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_02', 10)	# 21-30	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_03', 10)	# 31-40	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_04', 10)	# 41-50	 **attackbox here**
    RefreshMultihit()
    sprite('Action_099_05', 10)	# 51-60	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)

@State
def Vat_105_B():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1072(90000)
    sprite('Action_105_00', 2)	# 1-2
    sprite('Action_105_01', 16)	# 3-18
    GFX_0('Vat_107_B', 0)
    sprite('Action_102_00', 5)	# 19-23
    sprite('Action_102_01', 5)	# 24-28
    sprite('Action_102_02', 5)	# 29-33
    sprite('Action_102_03', 5)	# 34-38
    sprite('Action_102_04', 1)	# 39-39
    Unknown26('Vat_107_B')

@State
def Vat_105_Air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1072(90000)

        def upon_43():
            if (SLOT_48 == 1005):
                Unknown4007(0)
    sprite('Action_105_00', 5)	# 1-5
    sprite('Action_105_01', 16)	# 6-21
    GFX_0('Vat_107_B', 0)
    sprite('Action_102_00', 5)	# 22-26
    sprite('Action_102_01', 5)	# 27-31
    sprite('Action_102_02', 5)	# 32-36
    sprite('Action_102_03', 5)	# 37-41
    sprite('Action_102_04', 1)	# 42-42
    Unknown26('Vat_107_B')

@State
def Vat_107_B():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1072(90000)
    label(0)
    sprite('Action_107_00', 10)	# 1-10
    sprite('Action_107_01', 10)	# 11-20
    sprite('Action_107_02', 10)	# 21-30
    sprite('Action_107_03', 10)	# 31-40
    sprite('Action_107_04', 10)	# 41-50
    gotoLabel(0)

@State
def Vat_187():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(70)
        AttackP2(90)
        Hitstop(4)
        AirUntechableTime(100)
        AirPushbackX(5400)
        AirPushbackY(35000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown2018(0, 1000)
        Unknown9266(14)
        Unknown11031(0)
        Unknown11042(1)
    sprite('Action_187_00', 1)	# 1-1
    GFX_0('Vat_186', -1)
    sprite('Action_187_01', 2)	# 2-3
    sprite('Action_187_02', 2)	# 4-5
    SFX_3('SE_SwingLightSword')
    sprite('Action_187_03', 10)	# 6-15	 **attackbox here**
    sprite('Action_187_04', 10)	# 16-25
    sprite('Action_187_05', 10)	# 26-35
    sprite('Action_187_06', 1)	# 36-36
    sprite('Action_187_07', 1)	# 37-37

@State
def Vat_186():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown2018(0, 1000)
    sprite('Action_186_00', 3)	# 1-3
    sprite('Action_186_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_186_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_186_03', 3)	# 10-12	 **attackbox here**
    sprite('Action_186_04', 2)	# 13-14	 **attackbox here**
    sprite('Action_186_05', 2)	# 15-16	 **attackbox here**
    sprite('Action_186_06', 2)	# 17-18	 **attackbox here**
    sprite('Action_186_07', 2)	# 19-20	 **attackbox here**
    sprite('Action_186_08', 2)	# 21-22	 **attackbox here**
    sprite('Action_186_09', 2)	# 23-24	 **attackbox here**
    sprite('Action_186_10', 2)	# 25-26	 **attackbox here**
    sprite('Action_186_11', 2)	# 27-28	 **attackbox here**
    sprite('Action_186_12', 2)	# 29-30	 **attackbox here**
    sprite('Action_186_13', 2)	# 31-32	 **attackbox here**
    sprite('Action_186_14', 2)	# 33-34	 **attackbox here**
    sprite('Action_186_15', 5)	# 35-39	 **attackbox here**
    sprite('Action_186_16', 5)	# 40-44	 **attackbox here**
    sprite('Action_186_17', 5)	# 45-49	 **attackbox here**
    sprite('Action_186_18', 5)	# 50-54	 **attackbox here**
    sprite('Action_186_19', 3)	# 55-57	 **attackbox here**
    sprite('Action_186_20', 3)	# 58-60

@State
def Vat_095_AirA():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Init')
        physicsXImpulse(12000)
        physicsYImpulse(-10000)

        def upon_3():
            if (SLOT_23 < 320000):
                YAccel(95)
            if (SLOT_23 < 200000):
                YAccel(97)
            if (SLOT_23 < 161700):
                clearUponHandler(3)
                physicsYImpulse(0)
                teleportRelativeY(161700)

        def upon_43():
            if (SLOT_48 == 1000):
                Unknown13(25)
                GFX_0('Vat_096', -1)
    sprite('Action_095_00', 10)	# 1-10	 **attackbox here**
    label(0)
    sprite('Action_095_01', 10)	# 11-20	 **attackbox here**
    sprite('Action_095_02', 10)	# 21-30	 **attackbox here**
    sprite('Action_095_03', 10)	# 31-40	 **attackbox here**
    sprite('Action_095_04', 10)	# 41-50	 **attackbox here**
    sprite('Action_095_05', 10)	# 51-60	 **attackbox here**
    sprite('Action_095_06', 10)	# 61-70	 **attackbox here**
    gotoLabel(0)

@State
def Vat_095_AirB():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Init')
        physicsXImpulse(30000)
        physicsYImpulse(-20000)

        def upon_3():
            if (SLOT_23 < 320000):
                YAccel(97)
            if (SLOT_23 < 300000):
                YAccel(97)
            if (SLOT_23 < 280000):
                YAccel(97)
            if (SLOT_23 < 260000):
                YAccel(97)
            if (SLOT_23 < 240000):
                YAccel(97)
            if (SLOT_23 < 220000):
                YAccel(97)
            if (SLOT_23 < 200000):
                YAccel(98)
            if (SLOT_23 < 180000):
                YAccel(98)
            if (SLOT_23 < 161700):
                clearUponHandler(3)
                physicsYImpulse(0)
                teleportRelativeY(161700)

        def upon_43():
            if (SLOT_48 == 1001):
                Unknown13(25)
                GFX_0('Vat_096', -1)
    sprite('Action_095_00', 10)	# 1-10	 **attackbox here**
    label(0)
    sprite('Action_095_01', 10)	# 11-20	 **attackbox here**
    sprite('Action_095_02', 10)	# 21-30	 **attackbox here**
    sprite('Action_095_03', 10)	# 31-40	 **attackbox here**
    sprite('Action_095_04', 10)	# 41-50	 **attackbox here**
    sprite('Action_095_05', 10)	# 51-60	 **attackbox here**
    sprite('Action_095_06', 10)	# 61-70	 **attackbox here**
    gotoLabel(0)

@State
def Vat_077():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1072(-26000)
    label(0)
    sprite('Action_077_00', 8)	# 1-8
    sprite('Action_077_01', 8)	# 9-16
    sprite('Action_077_02', 8)	# 17-24
    sprite('Action_077_03', 8)	# 25-32
    sprite('Action_077_04', 8)	# 33-40
    sprite('Action_077_05', 8)	# 41-48
    gotoLabel(0)

@State
def Vat_226():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(500)
        Unknown11091(11)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirUntechableTime(60)
        AirPushbackX(70000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(1000)
        WallbounceReboundTime(0)
        Unknown9310(1)
        Hitstop(4)
        PushbackX(12000)
        Unknown30056('f04902001e00000000000000')
        Unknown9266(14)
        Unknown11110(80)
        Unknown23027()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)

        def upon_43():
            if (SLOT_48 == 2001):
                Damage(430)
                Unknown11091(10)
                Unknown1056(1200)
                Unknown1064(1200)
                teleportRelativeX(8000)
            if (SLOT_48 == 2002):
                Damage(100)
                Unknown11091(100)
                AttackP1(100)
                AttackP2(100)
            if (SLOT_48 == 2003):
                Damage(100)
                Unknown11091(100)
                AttackP1(100)
                AttackP2(100)
                Unknown1056(1200)
                Unknown1064(1200)
                teleportRelativeX(8000)
            if (SLOT_48 == 2000):
                sendToLabel(9)
    sprite('Action_226_00', 6)	# 1-6
    sprite('Action_226_01', 6)	# 7-12
    sprite('Action_226_02', 6)	# 13-18
    sprite('Action_226_03', 5)	# 19-23
    sprite('Action_226_06', 12)	# 24-35
    sprite('Action_226_07', 4)	# 36-39
    sprite('Action_226_08', 4)	# 40-43
    sprite('Action_226_09', 3)	# 44-46	 **attackbox here**
    sprite('Action_226_10', 3)	# 47-49	 **attackbox here**
    RefreshMultihit()
    sprite('Action_226_11', 3)	# 50-52	 **attackbox here**
    label(0)
    sprite('Action_226_12', 3)	# 53-55	 **attackbox here**
    RefreshMultihit()
    sprite('Action_226_13', 3)	# 56-58	 **attackbox here**
    sprite('Action_226_14', 3)	# 59-61	 **attackbox here**
    RefreshMultihit()
    sprite('Action_226_15', 3)	# 62-64	 **attackbox here**
    sprite('Action_226_16', 3)	# 65-67	 **attackbox here**
    RefreshMultihit()
    sprite('Action_226_17', 3)	# 68-70	 **attackbox here**
    sprite('Action_226_18', 3)	# 71-73	 **attackbox here**
    RefreshMultihit()
    sprite('Action_226_19', 3)	# 74-76	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_226_20', 3)	# 77-79
    Unknown23027()
    sprite('Action_226_21', 4)	# 80-83
    sprite('Action_226_22', 4)	# 84-87
    sprite('Action_226_23', 4)	# 88-91
    sprite('Action_226_24', 4)	# 92-95
    sprite('Action_226_25', 4)	# 96-99
    sprite('Action_226_26', 1)	# 100-100

@State
def Vat_228():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown2018(0, 100)
    sprite('Action_228_00', 12)	# 1-12
    sprite('Action_228_01', 12)	# 13-24
    sprite('Action_228_02', 12)	# 25-36
    label(0)
    sprite('Action_228_03', 12)	# 37-48
    sprite('Action_228_04', 12)	# 49-60
    sprite('Action_228_05', 12)	# 61-72
    sprite('Action_228_06', 12)	# 73-84
    gotoLabel(0)

@State
def Vat_228_END():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown2018(0, 100)
        Unknown26('Vat_228')
    sprite('Action_228_11', 13)	# 1-13
    sprite('Action_228_12', 10)	# 14-23

@State
def Vat_103():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('Action_103_00', 5)	# 1-5
    sprite('Action_103_01', 4)	# 6-9
    sprite('Action_103_02', 4)	# 10-13
    sprite('Action_103_03', 5)	# 14-18
    sprite('Action_103_04', 1)	# 19-19

@State
def Vat_165():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 2004):
                sendToLabel(0)
    sprite('Action_165_00', 3)	# 1-3
    sprite('Action_165_01', 3)	# 4-6
    sprite('Action_165_02', 3)	# 7-9
    sprite('Action_165_03', 3)	# 10-12
    sprite('Action_165_04', 3)	# 13-15
    sprite('Action_165_05', 3)	# 16-18
    sprite('Action_165_06', 3)	# 19-21
    sprite('Action_165_07', 1000)	# 22-1021
    label(0)
    sprite('Action_165_08', 3)	# 1022-1024
    Unknown4007(0)
    sprite('Action_165_09', 3)	# 1025-1027
    sprite('Action_165_10', 3)	# 1028-1030
    sprite('Action_165_11', 3)	# 1031-1033
    sprite('Action_165_12', 3)	# 1034-1036
    sprite('Action_165_13', 3)	# 1037-1039
    sprite('Action_165_14', 3)	# 1040-1042
    sprite('Action_165_15', 3)	# 1043-1045
    sprite('Action_165_16', 3)	# 1046-1048
    sprite('Action_165_17', 3)	# 1049-1051

@State
def Vat_168():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
    sprite('Action_168_03', 8)	# 1-8
    sprite('Action_168_02', 7)	# 9-15
    sprite('Action_168_01', 6)	# 16-21
    sprite('Action_168_00', 180)	# 22-201
    sprite('Action_168_01', 6)	# 202-207
    sprite('Action_168_02', 7)	# 208-214
    sprite('Action_168_03', 8)	# 215-222

@State
def Vat_999():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown2019(-4000)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_999_01', 3)	# 1-3	 **attackbox here**
    sprite('Action_999_02', 3)	# 4-6	 **attackbox here**
    sprite('Action_999_03', 3)	# 7-9	 **attackbox here**
    sprite('Action_999_04', 3)	# 10-12	 **attackbox here**
    sprite('Action_999_05', 3)	# 13-15	 **attackbox here**
    sprite('Action_999_06', 4)	# 16-19	 **attackbox here**
    sprite('Action_999_07', 3)	# 20-22	 **attackbox here**
    sprite('Action_999_08', 2)	# 23-24	 **attackbox here**
    sprite('Action_999_09', 2)	# 25-26	 **attackbox here**
    sprite('Action_999_10', 2)	# 27-28	 **attackbox here**
    sprite('Action_999_11', 4)	# 29-32	 **attackbox here**
    sprite('Action_999_12', 6)	# 33-38	 **attackbox here**
    sprite('Action_999_13', 7)	# 39-45	 **attackbox here**
    sprite('Action_999_14', 4)	# 46-49	 **attackbox here**
    sprite('Action_999_15', 4)	# 50-53	 **attackbox here**
    sprite('Action_999_16', 3)	# 54-56	 **attackbox here**
    sprite('Action_999_17', 3)	# 57-59	 **attackbox here**
    sprite('Action_999_18', 3)	# 60-62	 **attackbox here**
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)

@State
def AstWhiteOut():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 15)	# 1-15
    Unknown3004(20)
    sprite('vr_white', 30)	# 16-45
    Unknown3001(255)
    Unknown3004(0)
    sprite('vr_white', 30)	# 46-75
    Unknown3004(-9)

@State
def Vat_462():

    def upon_IMMEDIATE():
        Unknown2019(100)
    sprite('Action_462_00', 5)	# 1-5
    sprite('Action_462_01', 5)	# 6-10
    sprite('Action_462_02', 5)	# 11-15
    sprite('Action_462_03', 5)	# 16-20
    sprite('Action_462_04', 16)	# 21-36
    sprite('Action_462_05', 4)	# 37-40
    SFX_3('SE_LaserBeam')
    sprite('Action_462_06', 4)	# 41-44
    SFX_3('SE_LaserBeam')
    sprite('Action_462_07', 4)	# 45-48
    SFX_3('SE_LaserBeam')
    sprite('Action_462_08', 4)	# 49-52
    SFX_3('SE_LaserBeam')
    sprite('Action_462_09', 4)	# 53-56
    SFX_3('SE_LaserBeam')
    sprite('Action_462_10', 4)	# 57-60
    SFX_3('SE_LaserBeam')
    sprite('Action_462_11', 4)	# 61-64
    sprite('Action_462_12', 4)	# 65-68
    sprite('Action_462_13', 4)	# 69-72
    sprite('Action_462_14', 4)	# 73-76
    sprite('Action_462_15', 4)	# 77-80

@State
def Astral_Camera():

    def upon_IMMEDIATE():
        Unknown4011(3)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        Unknown23013(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)

        def upon_43():
            if (SLOT_48 == 3002):
                sendToLabel(0)
            if (SLOT_48 == 3003):
                sendToLabel(1)
    sprite('null', 32767)	# 1-32767
    Unknown1086(22)
    teleportRelativeX(35000)
    label(0)
    sprite('null', 1)	# 32768-32768
    sprite('null', 32767)	# 32769-65535

    def upon_3():
        Unknown1086(22)
        teleportRelativeX(35000)
        if (SLOT_105 <= 1650):
            SLOT_105 = (SLOT_105 + 3)
        else:
            Unknown1084(1)
            SLOT_105 = 1650
            clearUponHandler(3)
    label(1)
    sprite('null', 32767)	# 65536-98302
    SLOT_105 = 1000
    Unknown23032(50)
    teleportRelativeY(0)
    Unknown23013(1)
    Unknown2053(1)
    Unknown2034(1)
    Unknown1084(1)

@State
def Vat_476():

    def upon_IMMEDIATE():
        Unknown2019(-100)

        def upon_43():
            if (SLOT_48 == 3001):
                sendToLabel(1)
    sprite('Action_476_00', 8)	# 1-8
    label(0)
    sprite('Action_476_01', 10)	# 9-18
    sprite('Action_476_02', 10)	# 19-28
    sprite('Action_476_03', 10)	# 29-38
    sprite('Action_476_04', 10)	# 39-48
    sprite('Action_476_05', 10)	# 49-58
    gotoLabel(0)
    label(1)
    sprite('Action_476_06', 8)	# 59-66
    sprite('Action_476_07', 8)	# 67-74

@State
def Vat_463():

    def upon_IMMEDIATE():
        Unknown2019(100)
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('Action_463_00', 6)	# 1-6
    sprite('Action_463_01', 6)	# 7-12
    SFX_3('SE_MagicExist')
    sprite('Action_463_02', 6)	# 13-18
    sprite('Action_463_03', 6)	# 19-24
    sprite('Action_463_04', 6)	# 25-30
    sprite('Action_463_05', 6)	# 31-36
    sprite('Action_463_06', 6)	# 37-42
    sprite('Action_463_07', 6)	# 43-48
    sprite('Action_463_08', 6)	# 49-54
    sprite('Action_463_09', 6)	# 55-60
    sprite('Action_463_10', 6)	# 61-66
    sprite('Action_463_11', 6)	# 67-72
    sprite('Action_463_12', 6)	# 73-78
    sprite('Action_463_13', 33)	# 79-111
    sprite('Action_463_14', 60)	# 112-171
    sprite('Action_463_15', 60)	# 172-231
    sprite('Action_463_16', 90)	# 232-321

@State
def Vat_464():

    def upon_IMMEDIATE():
        Unknown2019(100)
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('Action_464_00', 6)	# 1-6
    sprite('Action_464_01', 6)	# 7-12
    sprite('Action_464_02', 6)	# 13-18
    sprite('Action_464_03', 6)	# 19-24
    sprite('Action_464_04', 6)	# 25-30
    sprite('Action_464_05', 6)	# 31-36
    sprite('Action_464_06', 6)	# 37-42
    sprite('Action_464_07', 6)	# 43-48
    sprite('Action_464_08', 6)	# 49-54
    sprite('Action_464_09', 6)	# 55-60
    sprite('Action_464_10', 6)	# 61-66
    sprite('Action_464_11', 6)	# 67-72
    sprite('Action_464_12', 6)	# 73-78
    sprite('Action_464_13', 6)	# 79-84
    SFX_3('SE_EarthQuake')
    sprite('Action_464_14', 5)	# 85-89
    GFX_0('Vat_465', -1)
    sprite('Action_464_15', 5)	# 90-94
    sprite('Action_464_16', 5)	# 95-99
    GFX_0('Vat_466', -1)
    sprite('Action_464_17', 5)	# 100-104
    sprite('Action_464_18', 5)	# 105-109
    GFX_0('Vat_467', -1)
    sprite('Action_464_19', 5)	# 110-114
    GFX_0('Vat_468', -1)
    sprite('Action_464_14', 5)	# 115-119
    GFX_0('Vat_469', -1)
    sprite('Action_464_15', 5)	# 120-124
    GFX_0('Vat_470', -1)
    sprite('Action_464_16', 5)	# 125-129
    sprite('Action_464_17', 5)	# 130-134
    sprite('Action_464_18', 5)	# 135-139
    sprite('Action_464_19', 5)	# 140-144
    sprite('Action_464_14', 5)	# 145-149
    sprite('Action_464_15', 5)	# 150-154
    sprite('Action_464_16', 5)	# 155-159
    sprite('Action_464_17', 5)	# 160-164
    sprite('Action_464_18', 5)	# 165-169
    sprite('Action_464_19', 5)	# 170-174
    sprite('Action_464_14', 5)	# 175-179
    sprite('Action_464_15', 5)	# 180-184
    sprite('Action_464_16', 5)	# 185-189
    sprite('Action_464_17', 5)	# 190-194
    sprite('Action_464_18', 5)	# 195-199
    sprite('Action_464_19', 5)	# 200-204
    sprite('Action_464_14', 5)	# 205-209
    sprite('Action_464_15', 5)	# 210-214
    sprite('Action_464_16', 5)	# 215-219
    sprite('Action_464_17', 5)	# 220-224
    sprite('Action_464_18', 5)	# 225-229
    sprite('Action_464_19', 5)	# 230-234
    sprite('Action_464_14', 5)	# 235-239
    sprite('Action_464_15', 5)	# 240-244
    sprite('Action_464_16', 5)	# 245-249
    sprite('Action_464_17', 5)	# 250-254
    sprite('Action_464_18', 5)	# 255-259
    sprite('Action_464_19', 5)	# 260-264
    sprite('Action_464_14', 5)	# 265-269
    sprite('Action_464_15', 5)	# 270-274
    sprite('Action_464_16', 5)	# 275-279
    sprite('Action_464_17', 5)	# 280-284
    sprite('Action_464_18', 5)	# 285-289
    sprite('Action_464_19', 5)	# 290-294
    sprite('Action_464_14', 5)	# 295-299
    sprite('Action_464_15', 5)	# 300-304
    sprite('Action_464_16', 5)	# 305-309
    sprite('Action_464_17', 5)	# 310-314
    sprite('Action_464_18', 5)	# 315-319
    sprite('Action_464_19', 5)	# 320-324
    sprite('Action_464_14', 5)	# 325-329
    sprite('Action_464_15', 5)	# 330-334
    sprite('Action_464_16', 5)	# 335-339
    sprite('Action_464_17', 5)	# 340-344
    sprite('Action_464_18', 5)	# 345-349
    sprite('Action_464_19', 2)	# 350-351

@State
def Vat_465():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2019(-100)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 3000):
                sendToLabel(1)
    sprite('Action_465_00', 3)	# 1-3
    sprite('Action_465_01', 3)	# 4-6
    SFX_3('SE_LaserBeam')
    sprite('Action_465_02', 3)	# 7-9
    sprite('Action_465_03', 3)	# 10-12
    sprite('Action_465_04', 3)	# 13-15
    sprite('Action_465_05', 3)	# 16-18
    label(0)
    sprite('Action_465_06', 3)	# 19-21
    sprite('Action_465_07', 3)	# 22-24
    sprite('Action_465_08', 3)	# 25-27
    sprite('Action_465_09', 3)	# 28-30
    sprite('Action_465_10', 3)	# 31-33
    sprite('Action_465_11', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('Action_465_12', 3)	# 37-39
    sprite('Action_465_13', 3)	# 40-42
    gotoLabel(1)

@State
def Vat_466():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2019(100)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 3000):
                sendToLabel(1)
    sprite('Action_466_00', 3)	# 1-3
    sprite('Action_466_01', 3)	# 4-6
    SFX_3('SE_LaserBeam')
    sprite('Action_466_02', 3)	# 7-9
    sprite('Action_466_03', 3)	# 10-12
    sprite('Action_466_04', 3)	# 13-15
    sprite('Action_466_05', 3)	# 16-18
    label(0)
    sprite('Action_466_06', 3)	# 19-21
    sprite('Action_466_07', 3)	# 22-24
    sprite('Action_466_08', 3)	# 25-27
    sprite('Action_466_09', 3)	# 28-30
    sprite('Action_466_10', 3)	# 31-33
    sprite('Action_466_11', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('Action_466_12', 3)	# 37-39
    sprite('Action_466_13', 3)	# 40-42
    gotoLabel(1)

@State
def Vat_467():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2019(-100)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 3000):
                sendToLabel(1)
    sprite('Action_467_00', 3)	# 1-3
    sprite('Action_467_01', 3)	# 4-6
    SFX_3('SE_LaserBeam')
    sprite('Action_467_02', 3)	# 7-9
    sprite('Action_467_03', 3)	# 10-12
    sprite('Action_467_04', 3)	# 13-15
    sprite('Action_467_05', 3)	# 16-18
    label(0)
    sprite('Action_467_06', 3)	# 19-21
    sprite('Action_467_07', 3)	# 22-24
    sprite('Action_467_08', 3)	# 25-27
    sprite('Action_467_09', 3)	# 28-30
    sprite('Action_467_10', 3)	# 31-33
    sprite('Action_467_11', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('Action_467_12', 3)	# 37-39
    sprite('Action_467_13', 3)	# 40-42
    gotoLabel(1)

@State
def Vat_468():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2019(100)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 3000):
                sendToLabel(1)
    sprite('Action_468_00', 3)	# 1-3
    sprite('Action_468_01', 3)	# 4-6
    SFX_3('SE_LaserBeam')
    sprite('Action_468_02', 3)	# 7-9
    sprite('Action_468_03', 3)	# 10-12
    sprite('Action_468_04', 3)	# 13-15
    sprite('Action_468_05', 3)	# 16-18
    label(0)
    sprite('Action_468_06', 3)	# 19-21
    sprite('Action_468_07', 3)	# 22-24
    sprite('Action_468_08', 3)	# 25-27
    sprite('Action_468_09', 3)	# 28-30
    sprite('Action_468_10', 3)	# 31-33
    sprite('Action_468_11', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('Action_468_12', 3)	# 37-39
    sprite('Action_468_13', 3)	# 40-42
    gotoLabel(1)

@State
def Vat_469():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2019(-100)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 3000):
                sendToLabel(1)
    sprite('Action_469_00', 3)	# 1-3
    sprite('Action_469_01', 3)	# 4-6
    SFX_3('SE_LaserBeam')
    sprite('Action_469_02', 3)	# 7-9
    sprite('Action_469_03', 3)	# 10-12
    sprite('Action_469_04', 3)	# 13-15
    sprite('Action_469_05', 3)	# 16-18
    label(0)
    sprite('Action_469_06', 3)	# 19-21
    sprite('Action_469_07', 3)	# 22-24
    sprite('Action_469_08', 3)	# 25-27
    sprite('Action_469_09', 3)	# 28-30
    sprite('Action_469_10', 3)	# 31-33
    sprite('Action_469_11', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('Action_469_12', 3)	# 37-39
    sprite('Action_469_13', 3)	# 40-42
    gotoLabel(1)

@State
def Vat_470():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2019(100)
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 3000):
                sendToLabel(1)
    sprite('Action_470_00', 3)	# 1-3
    sprite('Action_470_01', 3)	# 4-6
    SFX_3('SE_LaserBeam')
    sprite('Action_470_02', 3)	# 7-9
    sprite('Action_470_03', 3)	# 10-12
    sprite('Action_470_04', 3)	# 13-15
    sprite('Action_470_05', 3)	# 16-18
    label(0)
    sprite('Action_470_06', 3)	# 19-21
    sprite('Action_470_07', 3)	# 22-24
    sprite('Action_470_08', 3)	# 25-27
    sprite('Action_470_09', 3)	# 28-30
    sprite('Action_470_10', 3)	# 31-33
    sprite('Action_470_11', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('Action_470_12', 3)	# 37-39
    sprite('Action_470_13', 3)	# 40-42
    gotoLabel(1)

@State
def Vat_472():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2019(-500)
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('Action_472_00', 3)	# 1-3
    sprite('Action_472_01', 3)	# 4-6
    sprite('Action_472_02', 3)	# 7-9
    Unknown4004('6566666563745f3439350000000000000000000000000000000000000000000064000000')
    sprite('Action_472_03', 3)	# 10-12
    sprite('Action_472_04', 3)	# 13-15
    sprite('Action_472_05', 3)	# 16-18
    sprite('Action_472_06', 3)	# 19-21
    Unknown21015('5661745f34363500000000000000000000000000000000000000000000000000b80b000000000000')
    Unknown21015('5661745f34363600000000000000000000000000000000000000000000000000b80b000000000000')
    Unknown21015('5661745f34363700000000000000000000000000000000000000000000000000b80b000000000000')
    Unknown21015('5661745f34363800000000000000000000000000000000000000000000000000b80b000000000000')
    Unknown21015('5661745f34363900000000000000000000000000000000000000000000000000b80b000000000000')
    Unknown21015('5661745f34373000000000000000000000000000000000000000000000000000b80b000000000000')
    GFX_0('AstWhiteOut2', -1)
    sprite('Action_472_07', 3)	# 22-24	 **attackbox here**
    sprite('Action_472_08', 3)	# 25-27
    sprite('Action_472_09', 3)	# 28-30
    sprite('Action_472_10', 3)	# 31-33
    sprite('Action_472_11', 3)	# 34-36
    sprite('Action_472_12', 3)	# 37-39
    sprite('Action_472_13', 3)	# 40-42
    sprite('Action_472_14', 3)	# 43-45
    sprite('Action_472_11', 3)	# 46-48
    sprite('Action_472_12', 3)	# 49-51
    sprite('Action_472_13', 3)	# 52-54
    sprite('Action_472_14', 3)	# 55-57

@State
def AstWhiteOut2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown23015(4)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 30)	# 1-30
    Unknown3004(8)
    sprite('vr_white', 100)	# 31-130
    Unknown3001(255)
    Unknown21015('41737472616c5f43616d65726100000000000000000000000000000000000000bb0b000000000000')
    sprite('vr_white', 45)	# 131-175
    Unknown3004(-5)

@State
def Vat_Wing():

    def upon_IMMEDIATE():
        Unknown2019(1000)
    sprite('Action_050_43wing', 4)	# 1-4
    sprite('Action_050_44wing', 4)	# 5-8
    sprite('Action_050_45wing', 4)	# 9-12
    sprite('Action_050_46wing', 4)	# 13-16
    sprite('Action_050_47wing', 4)	# 17-20
    sprite('Action_050_48wing', 4)	# 21-24
    sprite('Action_050_49wing', 4)	# 25-28
    sprite('Action_050_50wing', 4)	# 29-32
    sprite('Action_050_51wing', 4)	# 33-36
    sprite('Action_050_52wing', 4)	# 37-40
    sprite('Action_050_53wing', 4)	# 41-44
    sprite('Action_050_54wing', 3)	# 45-47
    sprite('Action_050_55wing', 5)	# 48-52
    sprite('Action_050_56wing', 6)	# 53-58
    sprite('Action_050_57wing', 7)	# 59-65
    sprite('Action_050_58wing', 7)	# 66-72
    sprite('Action_050_59wing', 7)	# 73-79
    sprite('Action_050_60wing', 7)	# 80-86
    sprite('Action_050_61wing', 5)	# 87-91
    sprite('Action_050_62wing', 5)	# 92-96
    sprite('Action_050_63wing', 7)	# 97-103
    sprite('Action_050_64wing', 5)	# 104-108
    sprite('Action_050_65wing', 5)	# 109-113
    sprite('Action_050_66wing', 5)	# 114-118

@State
def Entry():

    def upon_IMMEDIATE():
        Unknown2019(-100)
        Unknown3001(255)
        loopRelated(17, 130)

        def upon_17():
            Unknown3004(-5)
    sprite('Action_071_01', 10)	# 1-10
    sprite('Action_071_02', 10)	# 11-20
    sprite('Action_071_03', 10)	# 21-30
    sprite('Action_071_04', 10)	# 31-40
    sprite('Action_071_05', 10)	# 41-50
    sprite('Action_071_06', 10)	# 51-60
    sprite('Action_071_07', 10)	# 61-70
    sprite('Action_071_08', 10)	# 71-80
    label(0)
    sprite('Action_071_09', 10)	# 81-90
    sprite('Action_071_10', 10)	# 91-100
    gotoLabel(0)

@State
def Entry2():

    def upon_IMMEDIATE():
        Unknown2019(0)
        Unknown3001(255)
        loopRelated(17, 130)

        def upon_17():
            Unknown3004(-5)
    label(0)
    sprite('Action_072_00', 10)	# 1-10
    sprite('Action_072_01', 10)	# 11-20
    gotoLabel(0)

@State
def Entry3():

    def upon_IMMEDIATE():
        Unknown2019(100)
        Unknown3001(255)
        loopRelated(17, 130)

        def upon_17():
            Unknown3004(-5)
    label(0)
    sprite('Action_072_00', 10)	# 1-10
    sprite('Action_072_01', 10)	# 11-20
    gotoLabel(0)

@State
def Entry_ES():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 4000):
                sendToLabel(1)
            if (SLOT_48 == 4001):
                Unknown3004(1)
        Unknown3001(0)
    label(0)
    sprite('Action_226_22', 1)	# 1-1
    gotoLabel(0)
    label(1)
    sprite('Action_226_23', 4)	# 2-5
    sprite('Action_226_24', 4)	# 6-9
    sprite('Action_226_25', 4)	# 10-13
    sprite('Action_226_26', 1)	# 14-14

@State
def Vat_skirt():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
    sprite('Action_050_12ex', 4)	# 1-4
    sprite('Action_050_13ex', 4)	# 5-8
    sprite('Action_050_14ex', 4)	# 9-12
    sprite('Action_050_15ex', 4)	# 13-16
    sprite('Action_050_16ex', 4)	# 17-20
    sprite('Action_050_17ex', 4)	# 21-24
    sprite('Action_050_18ex', 4)	# 25-28
    sprite('Action_050_19ex', 4)	# 29-32
    sprite('Action_050_20ex', 4)	# 33-36
    sprite('Action_050_21ex', 4)	# 37-40
    sprite('Action_050_22ex', 4)	# 41-44
    sprite('Action_050_23ex', 4)	# 45-48
    sprite('Action_050_24ex', 4)	# 49-52
    sprite('Action_050_25ex', 4)	# 53-56
    sprite('Action_050_26ex', 4)	# 57-60
    sprite('Action_050_27ex', 4)	# 61-64
    sprite('Action_050_28ex', 4)	# 65-68
    sprite('Action_050_29ex', 4)	# 69-72
    sprite('Action_050_30ex', 4)	# 73-76
    sprite('Action_050_31ex', 4)	# 77-80
    sprite('Action_050_32ex', 4)	# 81-84
    sprite('Action_050_33ex', 4)	# 85-88
    sprite('Action_050_34ex', 4)	# 89-92
    sprite('Action_050_35ex', 4)	# 93-96
    sprite('Action_050_36ex', 4)	# 97-100
    sprite('Action_050_38ex', 4)	# 101-104
    sprite('Action_050_39ex', 4)	# 105-108
    sprite('Action_050_40ex', 4)	# 109-112
    sprite('Action_050_41ex', 4)	# 113-116
    sprite('Action_050_43ex', 4)	# 117-120
    sprite('Action_050_44ex', 4)	# 121-124
    sprite('Action_050_45ex', 4)	# 125-128
    sprite('Action_050_46ex', 4)	# 129-132
    sprite('Action_050_47ex', 4)	# 133-136
    sprite('Action_050_48ex', 4)	# 137-140
    sprite('Action_050_49ex', 4)	# 141-144
    sprite('Action_050_50ex', 4)	# 145-148
    sprite('Action_050_51ex', 4)	# 149-152
    sprite('Action_050_52ex', 4)	# 153-156
    sprite('Action_050_53ex', 4)	# 157-160

@State
def Win():

    def upon_IMMEDIATE():
        Unknown3001(120)
    sprite('Action_089_00', 30)	# 1-30
    sprite('Action_089_01', 30)	# 31-60
    label(0)
    sprite('Action_089_02', 60)	# 61-120
    sprite('Action_089_03', 60)	# 121-180
    sprite('Action_089_04', 60)	# 181-240
    sprite('Action_089_05', 60)	# 241-300
    sprite('Action_089_06', 60)	# 301-360
    sprite('Action_089_07', 60)	# 361-420
    gotoLabel(0)

@State
def Win2_Top():

    def upon_IMMEDIATE():
        Unknown1010(-300000, 300000)
        Unknown1007(40000)
        physicsYImpulse(8000)
        if random_(2, 0, 50):
            physicsXImpulse(1000)
        else:
            physicsXImpulse(-1000)
    sprite('Action_090_00', 30)	# 1-30
    sprite('Action_090_01', 30)	# 31-60
    YAccel(50)
    sprite('Action_090_02', 3)	# 61-63
    YAccel(10)

@State
def Win2_Middle():

    def upon_IMMEDIATE():
        Unknown1010(-300000, 300000)
        Unknown1007(20000)
        physicsYImpulse(7000)
        if random_(2, 0, 50):
            physicsXImpulse(1000)
        else:
            physicsXImpulse(-1000)
    sprite('Action_090_04', 30)	# 1-30
    sprite('Action_090_05', 30)	# 31-60
    YAccel(30)
    sprite('Action_090_06', 3)	# 61-63

@State
def Win2_Bottom():

    def upon_IMMEDIATE():
        Unknown1010(-300000, 300000)
        physicsYImpulse(3000)
        if random_(2, 0, 50):
            physicsXImpulse(1000)
        else:
            physicsXImpulse(-1000)
    sprite('Action_090_08', 30)	# 1-30
    sprite('Action_090_09', 30)	# 31-60
    YAccel(30)
    sprite('Action_090_10', 3)	# 61-63

@State
def Win_MATOME():

    def upon_IMMEDIATE():
        pass
    label(0)
    sprite('null', 7)	# 1-7
    if random_(2, 0, 33):
        GFX_0('Win2_Top', -1)
    elif random_(2, 0, 50):
        GFX_0('Win2_Middle', -1)
    else:
        GFX_0('Win2_Bottom', -1)
    gotoLabel(0)