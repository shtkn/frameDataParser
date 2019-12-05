@State
def GuardAura():

    def upon_IMMEDIATE():
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 11):
                SLOT_2 = 0
                if SLOT_51:
                    SLOT_51 = 0
                    sendToLabel(15)

        def upon_CLEAR_OR_EXIT():
            Unknown2038(1)
            if (SLOT_2 >= 25):
                if (not SLOT_51):
                    SLOT_51 = 1
                    sendToLabel(20)
    label(10)
    sprite('Action_106_00', 4)	# 1-4
    sprite('Action_106_01', 4)	# 5-8
    sprite('Action_106_02', 4)	# 9-12
    sprite('Action_106_03', 4)	# 13-16
    Unknown4009(3)
    sprite('Action_106_04', 4)	# 17-20
    sprite('Action_106_05', 4)	# 21-24
    label(15)
    sprite('Action_106_02', 4)	# 25-28
    sprite('Action_106_03', 4)	# 29-32
    sprite('Action_106_04', 4)	# 33-36
    sprite('Action_106_05', 4)	# 37-40
    gotoLabel(15)
    label(20)
    sprite('Action_106_06', 4)	# 41-44
    Unknown4009(0)
    sprite('Action_106_07', 4)	# 45-48
    sprite('Action_106_08', 4)	# 49-52
    sprite('Action_106_09', 4)	# 53-56

@State
def CrouchChair():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4008(3)
        Unknown4019(3)
        Unknown2018(1, 30)
        Unknown2020(1)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 21):
                if (not SLOT_51):
                    SLOT_51 = 1
                    Unknown23029(5, 31, 0)
                    sendToLabel(10)
            if (SLOT_48 == 22):
                if SLOT_51:
                    SLOT_51 = 0
                    Unknown23029(5, 32, 0)
                    Unknown23029(6, 42, 0)
                    sendToLabel(1)
            if (SLOT_48 == 26):
                SLOT_51 = 0
                Unknown23029(5, 36, 0)
                Unknown23029(6, 46, 0)
                sendToLabel(1)
        if (SLOT_48 == 25):
            Unknown23029(5, 35, 0)
            Unknown23029(6, 45, 0)
            sendToLabel(5)
        if (SLOT_48 == 23):
            Unknown23029(5, 33, 0)
            Unknown23029(6, 45, 0)
            sendToLabel(100)
        if (SLOT_48 == 24):
            Unknown23029(5, 34, 0)
            Unknown23029(6, 44, 0)
            sendToLabel(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_5:
            Unknown4010(3)
        else:
            Unknown4010(0)
label(0)
sprite('null', 5)	# 1-5
GFX_0('CrouchChair_Front', 100)
Unknown38(5, 1)
GFX_0('CrouchChair_Back', 100)
Unknown38(6, 1)
sprite('Action_110_00', 5)	# 6-10
sprite('Action_110_01', 5)	# 11-15
sprite('Action_110_02', 4)	# 16-19
label(1)
sprite('Action_110_03', 4)	# 20-23
sprite('Action_110_04', 4)	# 24-27
sprite('Action_110_05', 4)	# 28-31
sprite('Action_110_02', 4)	# 32-35
gotoLabel(1)
label(5)
sprite('Action_111_00', 5)	# 36-40
sprite('Action_111_01', 5)	# 41-45
sprite('Action_111_02', 5)	# 46-50
sprite('Action_111_03', 5)	# 51-55
sprite('Action_111_04', 1)	# 56-56
gotoLabel(1)
label(10)
sprite('Action_110_02', 4)	# 57-60
sprite('Action_110_03', 4)	# 61-64
sprite('Action_110_04', 4)	# 65-68
sprite('Action_110_05', 4)	# 69-72
sprite('Action_110_06', 4)	# 73-76
sprite('Action_110_07', 5)	# 77-81
clearUponHandler(54)
clearUponHandler(43)
Unknown4007(0)
sprite('Action_110_08', 5)	# 82-86
ExitState()
label(100)
sprite('null', 10)	# 87-96
loopRest()
gotoLabel(1)
endState()

@State
def CrouchChair_Front():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4008(3)
        Unknown4019(3)
        Unknown2018(1, 30)
        Unknown2020(-1)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 31):
                sendToLabel(10)
            if (SLOT_48 == 32):
                if SLOT_51:
                    SLOT_51 = 0
                    sendToLabel(1)
            if (SLOT_48 == 36):
                SLOT_51 = 0
                sendToLabel(1)
        if (SLOT_48 == 35):
            sendToLabel(5)
        if (SLOT_48 == 33):
            sendToLabel(100)
        if (SLOT_48 == 34):
            sendToLabel(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_5:
            clearUponHandler(3)
            Unknown4010(3)
endUpon()
sprite('null', 15)	# 1-15
label(1)
sprite('Action_110_02ex01', 4)	# 16-19
sprite('Action_110_03ex01', 4)	# 20-23
sprite('Action_110_04ex01', 4)	# 24-27
sprite('Action_110_05ex01', 4)	# 28-31
gotoLabel(1)
label(5)
sprite('Action_111_00ex01', 5)	# 32-36
sprite('Action_111_01ex01', 5)	# 37-41
sprite('Action_111_02ex01', 5)	# 42-46
sprite('Action_111_03ex01', 5)	# 47-51
sprite('Action_111_04ex01', 1)	# 52-52
gotoLabel(1)
label(10)
sprite('Action_110_02ex01', 4)	# 53-56
sprite('Action_110_03ex01', 4)	# 57-60
sprite('Action_110_04ex01', 4)	# 61-64
sprite('Action_110_05ex01', 4)	# 65-68
sprite('Action_110_06ex01', 4)	# 69-72
sprite('Action_110_07ex01', 5)	# 73-77
clearUponHandler(54)
clearUponHandler(43)
Unknown4007(0)
sprite('Action_110_08ex01', 5)	# 78-82
ExitState()
label(100)
sprite('null', 10)	# 83-92
loopRest()
gotoLabel(1)
endState()

@State
def CrouchChair_Back():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown4008(3)
        Unknown4019(3)
        Unknown2018(1, 30)
        Unknown2020(20)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 31):
                sendToLabel(10)
            if (SLOT_48 == 42):
                if SLOT_51:
                    SLOT_51 = 0
                    sendToLabel(1)
            if (SLOT_48 == 46):
                SLOT_51 = 0
                sendToLabel(1)
        if (SLOT_48 == 45):
            sendToLabel(5)
        if (SLOT_48 == 43):
            sendToLabel(100)
        if (SLOT_48 == 44):
            sendToLabel(1)

    def upon_CLEAR_OR_EXIT():
        if SLOT_5:
            clearUponHandler(3)
            Unknown4010(3)
endUpon()
sprite('null', 15)	# 1-15
label(1)
sprite('Action_110_02ex02', 4)	# 16-19
sprite('Action_110_03ex02', 4)	# 20-23
sprite('Action_110_04ex02', 4)	# 24-27
sprite('Action_110_05ex02', 4)	# 28-31
gotoLabel(1)
label(5)
sprite('Action_111_00ex02', 5)	# 32-36
sprite('Action_111_01ex02', 5)	# 37-41
sprite('Action_111_02ex02', 5)	# 42-46
sprite('Action_111_03ex02', 5)	# 47-51
sprite('Action_111_04ex02', 1)	# 52-52
gotoLabel(1)
label(10)
sprite('Action_110_02ex02', 4)	# 53-56
sprite('Action_110_03ex02', 4)	# 57-60
sprite('Action_110_04ex02', 4)	# 61-64
sprite('Action_110_05ex02', 4)	# 65-68
sprite('Action_110_06ex02', 4)	# 69-72
sprite('Action_110_07ex02', 5)	# 73-77
clearUponHandler(54)
clearUponHandler(43)
Unknown4007(0)
sprite('Action_110_08ex02', 5)	# 78-82
ExitState()
label(100)
sprite('null', 10)	# 83-92
loopRest()
gotoLabel(1)
endState()

@State
def CrouchTurnChair():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown4007(3)
        Unknown2019(101)
    sprite('Action_092_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_092_01', 4)	# 4-7	 **attackbox here**
    sprite('Action_092_02', 2)	# 8-9	 **attackbox here**

@State
def DashEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-90000)
        physicsYImpulse(5050)
        Unknown1025(-1500, 0)
        Unknown1026(1000, 2000)
    label(0)
    sprite('null', 1)	# 1-1
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(2)
    label(1)
    sprite('Action_122_00', 3)	# 2-4
    sprite('Action_122_01', 3)	# 5-7
    sprite('Action_122_02', 3)	# 8-10
    sprite('Action_122_03', 3)	# 11-13
    loopRest()
    ExitState()
    label(2)
    sprite('Action_122_05', 3)	# 14-16
    sprite('Action_122_06', 3)	# 17-19
    sprite('Action_122_07', 3)	# 20-22
    sprite('Action_122_08', 3)	# 23-25
    loopRest()
    ExitState()

@State
def BackDashEff():

    def upon_IMMEDIATE():
        teleportRelativeX(90000)
        physicsYImpulse(5050)
        Unknown1025(0, 1500)
        Unknown1026(1000, 2000)
    label(0)
    sprite('null', 1)	# 1-1
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(2)
    label(1)
    sprite('Action_123_00', 3)	# 2-4
    sprite('Action_123_01', 3)	# 5-7
    sprite('Action_123_02', 3)	# 8-10
    sprite('Action_123_03', 3)	# 11-13
    loopRest()
    ExitState()
    label(2)
    sprite('Action_123_05', 3)	# 14-16
    sprite('Action_123_06', 3)	# 17-19
    sprite('Action_123_07', 3)	# 20-22
    sprite('Action_123_08', 3)	# 23-25
    loopRest()
    ExitState()

@State
def ThrowHitmarkMatome():

    def upon_IMMEDIATE():
        Unknown2055(63)

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if (not SLOT_51):
                clearUponHandler(45)
                Unknown13(25)
    label(0)
    sprite('null', 5)	# 1-5
    GFX_0('ThrowHitmark', 100)
    sprite('null', 5)	# 6-10
    GFX_0('ThrowHitmark', 100)
    gotoLabel(0)

@State
def ThrowHitmark():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown23151(22, 103)
    Unknown1010(-80000, 80000)
    Unknown1011(-80000, 80000)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(2)
    label(1)
    sprite('Action_089_00', 5)	# 2-6
    sprite('Action_089_01', 5)	# 7-11
    sprite('Action_089_02', 5)	# 12-16
    sprite('Action_089_03', 5)	# 17-21
    ExitState()
    label(2)
    sprite('Action_089_06', 5)	# 22-26
    sprite('Action_089_07', 5)	# 27-31
    sprite('Action_089_08', 5)	# 32-36
    sprite('Action_089_09', 5)	# 37-41
    ExitState()

@State
def EffAtk5A():

    def upon_IMMEDIATE():
        Unknown2019(-100)
        teleportRelativeX(70000)
    sprite('Action_098_00', 3)	# 1-3
    sprite('Action_098_01', 3)	# 4-6
    sprite('Action_098_02', 3)	# 7-9
    sprite('Action_098_03', 3)	# 10-12
    sprite('Action_098_04', 3)	# 13-15
    sprite('Action_098_05', 3)	# 16-18
    sprite('Action_098_06', 3)	# 19-21
    sprite('Action_098_07', 3)	# 22-24
    SFX_3('SE_Hari_Vanish')
    sprite('Action_098_08', 3)	# 25-27
    sprite('Action_098_09', 3)	# 28-30
    sprite('Action_098_10', 3)	# 31-33
    sprite('Action_098_11', 3)	# 34-36
    sprite('Action_098_12', 1)	# 37-37

@State
def EffAtk5A2nd():

    def upon_IMMEDIATE():
        Unknown2019(-100)
    sprite('Action_078_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_078_01', 4)	# 6-9	 **attackbox here**
    SFX_3('SE_Hari_Vanish')
    sprite('Action_078_02', 4)	# 10-13	 **attackbox here**
    sprite('Action_078_03', 4)	# 14-17	 **attackbox here**
    sprite('Action_078_04', 1)	# 18-18

@State
def EffAtk5A3rd():

    def upon_IMMEDIATE():
        Unknown2019(-100)
    sprite('Action_116_00', 4)	# 1-4
    sprite('Action_116_01', 5)	# 5-9
    sprite('Action_116_02', 5)	# 10-14
    sprite('Action_116_03', 5)	# 15-19
    SFX_3('SE_Hari_Vanish')
    sprite('Action_116_04', 4)	# 20-23
    sprite('Action_116_05', 4)	# 24-27
    sprite('Action_116_06', 1)	# 28-28

@State
def EffAtk5A4thBegin():
    sprite('Action_277_00', 4)	# 1-4
    sprite('Action_277_01', 4)	# 5-8
    sprite('Action_277_02', 4)	# 9-12
    sprite('Action_277_03', 4)	# 13-16

@State
def EffAtk5A4th():
    sprite('Action_284_00', 3)	# 1-3
    sprite('Action_284_01', 3)	# 4-6
    SFX_3('SE_Hari_Vanish')
    sprite('Action_284_02', 3)	# 7-9
    sprite('Action_284_03', 3)	# 10-12
    sprite('Action_284_04', 1)	# 13-13

@State
def EffAtk5B_Atk():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2009()
        AttackLevel_(4)
        AttackP2(75)
        AirPushbackX(12000)
        AirPushbackY(22000)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Hitstop(6)
        Unknown9016(1)
        SLOT_10 = 0

        def upon_77():
            SLOT_10 = 1
    sprite('Action_182_00', 2)	# 1-2
    sprite('Action_182_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_182_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_182_03', 3)	# 8-10	 **attackbox here**
    sprite('Action_182_04ex01', 2)	# 11-12	 **attackbox here**
    sprite('Action_182_05', 4)	# 13-16	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('Action_182_06', 4)	# 17-20	 **attackbox here**
    sprite('Action_182_07', 4)	# 21-24	 **attackbox here**
    sprite('Action_182_08', 1)	# 25-25	 **attackbox here**

@State
def EffAtk5BB_Atk():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2009()
        AttackLevel_(4)
        AirPushbackX(-7000)
        AirPushbackY(25000)
        PushbackX(-30400)
        AirUntechableTime(36)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown23078(1)
        Unknown23013(1)
        Unknown2005()
        Unknown11099(1)
        teleportRelativeX(-700000)

        def upon_43():
            if (SLOT_48 == 103):
                Unknown1086(22)
                teleportRelativeX(-150000)
                teleportRelativeY(0)

        def upon_77():
            SLOT_10 = 1
    sprite('Action_416_00', 2)	# 1-2
    sprite('Action_416_01', 2)	# 3-4
    Unknown2053(0)
    Unknown2034(0)
    SFX_3('SE_Hari_Appear')
    sprite('Action_416_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_416_03', 3)	# 8-10
    sprite('Action_416_04', 3)	# 11-13
    sprite('Action_416_05', 3)	# 14-16
    sprite('Action_416_06', 3)	# 17-19
    sprite('Action_416_07', 3)	# 20-22
    sprite('Action_416_08', 3)	# 23-25
    SFX_3('SE_Hari_Vanish')
    sprite('Action_416_09', 3)	# 26-28
    sprite('Action_416_10', 3)	# 29-31
    sprite('Action_416_11', 1)	# 32-32

@State
def Eff5BBB_Atk():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2009()
        AttackLevel_(3)
        Unknown11092(1)
        HitOverhead(2)
        AirPushbackX(0)
        AirPushbackY(-75000)
        PushbackX(0)
        AirUntechableTime(60)
        hitstun(25)
        Unknown9190(1)
        Unknown9118(20)
        Hitstop(3)
        Unknown11001(0, 2, 2)
        Unknown9016(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown2053(1)
        Unknown2034(1)
        Unknown23013(1)
        Unknown1096(1200)
        teleportRelativeX(700000)
        if SLOT_10:
            Unknown1086(22)
        Unknown1007(500000)
        SLOT_10 = 0

        def upon_77():
            SLOT_10 = 1
        sendToLabelUpon(2, 1)

        def upon_53():
            sendToLabel(580)
    sprite('Action_435_00', 2)	# 1-2
    sprite('Action_435_01', 2)	# 3-4
    Unknown2053(0)
    Unknown2034(0)
    SFX_3('SE_Hari_Appear')
    sprite('Action_435_02', 2)	# 5-6
    sprite('Action_435_03', 2)	# 7-8
    sprite('Action_435_04', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(-75000)
    sprite('Action_435_05', 3)	# 12-14	 **attackbox here**
    sprite('Action_435_06', 3)	# 15-17	 **attackbox here**
    label(0)
    sprite('Action_435_07', 3)	# 18-20	 **attackbox here**
    sprite('Action_435_08', 3)	# 21-23	 **attackbox here**
    sprite('Action_435_09', 3)	# 24-26	 **attackbox here**
    sprite('Action_435_10', 3)	# 27-29	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_435_11ex01', 1)	# 30-30	 **attackbox here**
    GFX_0('EffDropShot_Landing', 100)
    sprite('Action_435_11', 1)	# 31-31	 **attackbox here**
    sprite('Action_435_12', 3)	# 32-34	 **attackbox here**
    sprite('Action_435_13', 3)	# 35-37	 **attackbox here**
    GFX_0('EffDropShot_Ralease', 100)
    SFX_3('SE_Hari_Vanish')
    label(580)
    sprite('Action_435_14', 3)	# 38-40	 **attackbox here**
    sprite('Action_435_15', 3)	# 41-43	 **attackbox here**
    sprite('Action_435_16', 3)	# 44-46	 **attackbox here**
    sprite('Action_435_17', 3)	# 47-49	 **attackbox here**
    sprite('Action_435_18', 3)	# 50-52	 **attackbox here**
    sprite('Action_435_19', 3)	# 53-55	 **attackbox here**
    sprite('Action_435_20', 3)	# 56-58	 **attackbox here**
    sprite('Action_435_21', 3)	# 59-61	 **attackbox here**
    sprite('Action_435_22', 3)	# 62-64	 **attackbox here**
    sprite('Action_435_23', 3)	# 65-67	 **attackbox here**
    sprite('Action_435_24', 3)	# 68-70	 **attackbox here**
    sprite('Action_435_25', 3)	# 71-73	 **attackbox here**

@State
def EffAtk2B():
    sprite('Action_100_00', 3)	# 1-3
    sprite('Action_100_01', 3)	# 4-6
    SFX_3('SE_Hari_Vanish')
    sprite('Action_100_02', 3)	# 7-9
    sprite('Action_100_03', 3)	# 10-12
    sprite('Action_100_04', 3)	# 13-15

@State
def EffAtk2BB():
    sprite('Action_115_00', 4)	# 1-4
    sprite('Action_115_01', 4)	# 5-8
    sprite('Action_115_02', 4)	# 9-12
    SFX_3('SE_Hari_Vanish')
    sprite('Action_115_03', 4)	# 13-16
    sprite('Action_115_04', 4)	# 17-20
    sprite('Action_115_05', 1)	# 21-21

@State
def EffAtk2C():
    sprite('Action_101_00', 3)	# 1-3
    sprite('Action_101_01', 3)	# 4-6
    sprite('Action_101_02', 3)	# 7-9
    SFX_3('SE_Hari_Vanish')
    sprite('Action_101_03', 3)	# 10-12
    sprite('Action_101_04', 3)	# 13-15

@State
def EffAtk2CC():
    sprite('Action_117_00', 4)	# 1-4
    sprite('Action_117_01', 4)	# 5-8
    sprite('Action_117_02', 4)	# 9-12
    SFX_3('SE_Hari_Vanish')
    sprite('Action_117_03', 4)	# 13-16
    sprite('Action_117_04', 4)	# 17-20
    sprite('Action_117_05', 1)	# 21-21

@State
def EffAtkAIR5A():
    sprite('Action_093_00', 3)	# 1-3
    sprite('Action_093_01', 3)	# 4-6
    sprite('Action_093_02', 3)	# 7-9
    SFX_3('SE_Hari_Vanish')
    sprite('Action_093_03', 3)	# 10-12
    sprite('Action_093_04', 3)	# 13-15
    sprite('Action_093_05', 1)	# 16-16

@State
def EffAtkAIR5AA():

    def upon_IMMEDIATE():
        teleportRelativeX(263000)
        Unknown1007(193000)
    sprite('Action_086_00', 3)	# 1-3
    sprite('Action_086_01', 3)	# 4-6
    sprite('Action_086_02', 3)	# 7-9
    SFX_3('SE_Hari_Vanish')
    sprite('Action_086_03', 3)	# 10-12
    sprite('Action_086_04', 3)	# 13-15
    sprite('Action_086_05', 3)	# 16-18

@State
def EffAtkAIR5B_Atk():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2009()
        AttackLevel_(4)
        AttackP2(75)
        AirPushbackX(5000)
        AirPushbackY(32000)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Hitstop(6)
        Unknown9016(1)
        Unknown1073(18000)
    sprite('Action_189_00', 2)	# 1-2
    sprite('Action_189_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_189_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_189_03', 3)	# 8-10	 **attackbox here**
    sprite('Action_189_04', 2)	# 11-12	 **attackbox here**
    sprite('Action_189_05', 4)	# 13-16	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('Action_189_06', 4)	# 17-20	 **attackbox here**
    sprite('Action_189_07', 4)	# 21-24	 **attackbox here**
    sprite('Action_189_08', 1)	# 25-25	 **attackbox here**

@State
def EffAtkAIR5B2nd():
    sprite('Action_099_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_099_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_099_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_099_03', 4)	# 13-16	 **attackbox here**
    sprite('Action_099_04', 1)	# 17-17	 **attackbox here**

@State
def EffAtkAIR5BBAtkMatome():

    def upon_IMMEDIATE():
        Unknown4011(3)
        AttackLevel_(2)
        AttackP2(80)
        Unknown11092(1)
        Unknown4007(3)
    sprite('null', 3)	# 1-3
    GFX_0('EffAtkAIR5BBAtkCol1', 100)
    Unknown36(1)
    Unknown1021(-12500)
    Unknown35()
    sprite('null', 3)	# 4-6
    GFX_0('EffAtkAIR5BBAtkCol2', 100)
    Unknown36(1)
    Unknown1021(-13500)
    Unknown35()
    sprite('null', 3)	# 7-9
    GFX_0('EffAtkAIR5BBAtkCol1', 100)
    Unknown36(1)
    Unknown1021(-17500)
    Unknown35()
    sprite('null', 60)	# 10-69
    GFX_0('EffAtkAIR5BBAtkCol2', 100)
    Unknown36(1)
    Unknown1021(-1000)
    Unknown35()

@State
def EffAtkAIR5BBAtkCol1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2009()
        AttackLevel_(2)
        Damage(450)
        AirPushbackY(22000)
        PushbackX(8000)
        AttackP2(80)
        Unknown11092(1)
        Hitstop(3)
        AirUntechableTime(28)
        physicsXImpulse(23500)
        Unknown9016(1)
        Unknown23182(2)
    sprite('null', 2)	# 1-2
    sprite('Action_205_00', 5)	# 3-7	 **attackbox here**
    Unknown1108(90000)
    SFX_3('SE_DrawnSword')
    sprite('Action_146_01', 5)	# 8-12	 **attackbox here**
    sprite('Action_146_02', 30)	# 13-42	 **attackbox here**
    sprite('Action_146_03', 5)	# 43-47
    sprite('Action_146_04', 5)	# 48-52
    sprite('Action_146_05', 5)	# 53-57
    sprite('Action_146_06', 5)	# 58-62

@State
def EffAtkAIR5BBAtkCol2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2009()
        AttackLevel_(2)
        Damage(450)
        AirPushbackY(22000)
        PushbackX(8000)
        AttackP2(80)
        Unknown11092(1)
        Hitstop(3)
        AirUntechableTime(28)
        physicsXImpulse(23500)
        Unknown9016(1)
        Unknown23182(2)
    sprite('null', 2)	# 1-2
    sprite('Action_146_08', 5)	# 3-7	 **attackbox here**
    Unknown1108(95000)
    SFX_3('SE_DrawnSword')
    sprite('Action_146_09', 5)	# 8-12	 **attackbox here**
    sprite('Action_146_10', 30)	# 13-42	 **attackbox here**
    sprite('Action_146_11', 5)	# 43-47
    sprite('Action_146_12', 5)	# 48-52
    sprite('Action_146_13', 5)	# 53-57
    sprite('Action_146_14', 5)	# 58-62

@State
def EffAtkAIR5C():

    def upon_IMMEDIATE():
        Unknown2019(101)
    sprite('Action_097_00', 3)	# 1-3
    sprite('Action_097_01', 3)	# 4-6
    SFX_3('SE_Hari_Vanish')
    sprite('Action_097_02', 3)	# 7-9
    sprite('Action_097_03', 3)	# 10-12
    sprite('Action_097_04', 1)	# 13-13

@State
def AirStandFront():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown2019(-100)
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 51):
                Unknown4007(0)
                sendToLabel(1)
        loopRelated(17, 120)

        def upon_17():
            Unknown13(25)
    sprite('Action_141_00', 3)	# 1-3
    sprite('Action_141_01', 3)	# 4-6
    label(0)
    sprite('Action_141_02', 3)	# 7-9
    sprite('Action_141_03', 3)	# 10-12
    sprite('Action_141_04', 3)	# 13-15
    sprite('Action_141_05', 3)	# 16-18
    gotoLabel(0)
    label(1)
    sprite('Action_141_06', 3)	# 19-21
    sprite('Action_141_07', 1)	# 22-22

@State
def EffBurst():
    sprite('Action_118_00', 4)	# 1-4
    sprite('Action_118_01', 5)	# 5-9
    sprite('Action_118_02', 5)	# 10-14
    sprite('Action_118_03', 4)	# 15-18
    sprite('Action_118_04', 4)	# 19-22
    sprite('Action_118_05', 4)	# 23-26
    sprite('Action_118_06', 1)	# 27-27

@State
def AirStandBack():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown2019(101)
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 52):
                Unknown4007(0)
                sendToLabel(1)
        loopRelated(17, 120)

        def upon_17():
            Unknown13(25)
    sprite('Action_140_00', 3)	# 1-3
    sprite('Action_140_01', 3)	# 4-6
    label(0)
    sprite('Action_140_02', 3)	# 7-9
    sprite('Action_140_03', 3)	# 10-12
    sprite('Action_140_04', 3)	# 13-15
    sprite('Action_140_05', 3)	# 16-18
    gotoLabel(0)
    label(1)
    sprite('Action_140_06', 3)	# 19-21
    sprite('Action_140_07', 1)	# 22-22

@State
def EffAtkThrowCatch():

    def upon_IMMEDIATE():
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('Action_103_00', 3)	# 1-3
    sprite('Action_103_01', 3)	# 4-6
    sprite('Action_103_02', 3)	# 7-9
    sprite('Action_103_03', 3)	# 10-12
    sprite('Action_103_04', 3)	# 13-15
    sprite('Action_103_05', 3)	# 16-18
    sprite('Action_103_06', 1)	# 19-19

@State
def EffAtkThrowMiss():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
    sprite('Action_104_00', 3)	# 1-3
    sprite('Action_104_01', 3)	# 4-6
    sprite('Action_104_02', 3)	# 7-9
    sprite('Action_104_03', 3)	# 10-12
    sprite('Action_104_04', 1)	# 13-13

@State
def EffAtkThrowExe():

    def upon_IMMEDIATE():
        Unknown2019(100)
        Unknown2034(1)
        Unknown23151(22, 103)

        def upon_43():
            if (SLOT_48 == 102):
                sendToLabel(1)
    sprite('Action_059_00', 3)	# 1-3
    SFX_3('SE_AppearInsulator')
    sprite('Action_059_01', 3)	# 4-6
    sprite('Action_059_02', 3)	# 7-9
    sprite('Action_059_03', 3)	# 10-12
    sprite('Action_059_04', 3)	# 13-15
    sprite('Action_059_05', 3)	# 16-18
    sprite('Action_059_06', 3)	# 19-21
    sprite('Action_059_07', 60)	# 22-81
    label(1)
    sprite('Action_059_08', 3)	# 82-84
    sprite('Action_059_09', 3)	# 85-87
    sprite('Action_059_10', 3)	# 88-90
    sprite('Action_059_11', 3)	# 91-93
    sprite('Action_059_12', 3)	# 94-96
    sprite('Action_059_13', 3)	# 97-99

@State
def EffAtk5AAAA_1st():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2009()
        AttackLevel_(4)
        Damage(0)
        AttackP1(100)
        AttackP2(85)
        Hitstop(3)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9016(1)
        Unknown30048(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11072(1, 0, 0)
        Unknown11084(1)
        Unknown11069('EffAtk5AAAA_Exe_Dmykcol')
        Unknown11044(1)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown2019(-1000)
        Unknown11064(1)

        def upon_78():
            Hitstop(0)
            Unknown11001(0, 45, 45)
            Unknown30048(0)
            Unknown23029(3, 101, 0)
        SLOT_11 = 0

        def upon_82():
            SLOT_11 = 1
    sprite('Action_103_00', 3)	# 1-3
    sprite('Action_103_01ex01', 3)	# 4-6	 **attackbox here**
    sprite('Action_103_02ex01', 3)	# 7-9	 **attackbox here**
    sprite('Action_103_03ex01', 3)	# 10-12	 **attackbox here**
    sprite('Action_103_04', 3)	# 13-15
    sprite('Action_103_05', 3)	# 16-18
    sprite('Action_103_06', 1)	# 19-19

@State
def EffAtk5AAAA_Exe():

    def upon_IMMEDIATE():
        Unknown2019(100)
        Unknown2034(1)
        Unknown1086(22)
        teleportRelativeY(250000)

        def upon_43():
            if (SLOT_48 == 102):
                sendToLabel(1)
    sprite('Action_059_00', 3)	# 1-3
    SFX_3('SE_AppearInsulator')
    sprite('Action_059_01', 3)	# 4-6
    sprite('Action_059_02', 3)	# 7-9
    sprite('Action_059_03', 3)	# 10-12
    sprite('Action_059_04', 3)	# 13-15
    sprite('Action_059_05', 3)	# 16-18
    sprite('Action_059_06', 3)	# 19-21
    sprite('Action_059_08', 3)	# 22-24
    sprite('Action_059_09', 3)	# 25-27
    sprite('Action_059_10', 3)	# 28-30
    sprite('Action_059_11', 3)	# 31-33
    sprite('Action_059_12', 3)	# 34-36
    sprite('Action_059_13', 3)	# 37-39

@State
def EffAtk5AAAA_Exe_Dmykcol():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(2500)
        AttackP2(100)
        Hitstop(10)
        AirUntechableTime(60)
        AirPushbackX(60000)
        AirPushbackY(2000)
        YImpluseBeforeWallbounce(5)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        WallbounceReboundTime(30)
        Unknown9016(1)
        JumpCancel_(0)
        Unknown11044(1)
        Unknown23151(22, 103)
        Unknown11023(1)
        Unknown30088(1)

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown2003(0)
            else:
                Unknown2003(1)
            if SLOT_11:
                Unknown48('19000000020000003400000017000000020000001e000000')
                if SLOT_52:
                    Unknown30048(0)
                else:
                    Unknown30048(1)
    sprite('Action_057_04_atkdmy', 3)	# 1-3

@State
def EffCrushFinish():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown2019(101)
        Unknown2003(1)
        teleportRelativeX(-185000)
        teleportRelativeY(350000)
    sprite('Action_211_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_211_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_211_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_211_03', 2)	# 7-8	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_211_04', 3)	# 9-11	 **attackbox here**
    sprite('Action_211_05', 3)	# 12-14	 **attackbox here**
    sprite('Action_211_06', 3)	# 15-17	 **attackbox here**
    sprite('Action_211_07', 3)	# 18-20	 **attackbox here**
    sprite('Action_211_08', 3)	# 21-23	 **attackbox here**
    sprite('Action_211_09', 3)	# 24-26	 **attackbox here**
    sprite('Action_211_10', 3)	# 27-29	 **attackbox here**
    sprite('Action_211_11', 3)	# 30-32	 **attackbox here**
    sprite('Action_211_12', 3)	# 33-35	 **attackbox here**
    sprite('Action_211_13', 3)	# 36-38	 **attackbox here**
    sprite('Action_211_14', 3)	# 39-41	 **attackbox here**
    SFX_3('SE_Hari_Vanish')
    sprite('Action_211_15', 3)	# 42-44	 **attackbox here**
    sprite('Action_211_16', 3)	# 45-47	 **attackbox here**
    sprite('Action_211_17', 3)	# 48-50	 **attackbox here**
    sprite('Action_211_18', 1)	# 51-51	 **attackbox here**

@State
def EffAtkCrushStart():

    def upon_IMMEDIATE():
        teleportRelativeX(90000)
        Unknown1007(5000)
    sprite('Action_075_00', 4)	# 1-4
    sprite('Action_075_01', 4)	# 5-8
    SFX_3('SE_Hari_Vanish')
    sprite('Action_075_02', 4)	# 9-12
    sprite('Action_075_03', 4)	# 13-16
    sprite('Action_075_04', 1)	# 17-17

@State
def EffAtkCrush1stMain():
    sprite('Action_119_00', 3)	# 1-3
    sprite('Action_119_01', 3)	# 4-6
    SFX_3('SE_Hari_Vanish')
    sprite('Action_119_02', 3)	# 7-9
    sprite('Action_119_03', 3)	# 10-12
    sprite('Action_119_04', 3)	# 13-15

@State
def EffAtkCrush2ndMain():
    sprite('Action_083_00', 5)	# 1-5
    sprite('Action_083_01', 5)	# 6-10
    sprite('Action_083_02', 5)	# 11-15
    sprite('Action_083_03', 5)	# 16-20
    SFX_3('SE_Hari_Vanish')
    sprite('Action_083_04', 5)	# 21-25
    sprite('Action_083_05', 5)	# 26-30
    sprite('Action_083_06', 1)	# 31-31

@State
def EffAtkCrush1stSub():
    sprite('Action_077_00', 4)	# 1-4
    sprite('Action_077_01', 4)	# 5-8
    SFX_3('SE_Hari_Vanish')
    sprite('Action_077_02', 4)	# 9-12
    sprite('Action_077_03', 4)	# 13-16
    sprite('Action_077_04', 1)	# 17-17

@State
def EffWarpIn():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-15000)

        def upon_56():
            Unknown4007(0)
    sprite('Action_158_00', 7)	# 1-7
    sprite('Action_158_01', 7)	# 8-14
    sprite('Action_158_02', 7)	# 15-21
    sprite('Action_158_03', 7)	# 22-28
    sprite('Action_158_04', 1)	# 29-29

@State
def EffWarpOut():

    def upon_IMMEDIATE():
        teleportRelativeX(-15000)
    sprite('Action_137_00', 10)	# 1-10
    sprite('Action_137_01', 10)	# 11-20
    SFX_3('SE_Hari_Vanish')
    sprite('Action_137_02', 10)	# 21-30
    sprite('Action_137_03', 10)	# 31-40
    sprite('Action_137_04', 10)	# 41-50

@State
def EffReversalStart():
    sprite('Action_277_00', 4)	# 1-4
    sprite('Action_277_01', 4)	# 5-8
    sprite('Action_277_02', 4)	# 9-12
    sprite('Action_277_03', 4)	# 13-16

@State
def EffReversal():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('Action_280_00', 2)	# 1-2
    GFX_0('EffReversalSub1', 100)
    sprite('Action_280_01', 5)	# 3-7
    GFX_0('EffReversalSub2', 100)
    sprite('Action_280_02', 5)	# 8-12
    GFX_0('EffReversalSub3', 100)
    sprite('Action_280_03', 4)	# 13-16
    sprite('Action_280_04', 1)	# 17-17

@State
def EffReversalSub1():

    def upon_IMMEDIATE():
        Unknown2019(100)
    sprite('Action_273_00', 4)	# 1-4
    SFX_3('SE_Hari_Vanish')
    sprite('Action_273_01', 5)	# 5-9
    sprite('Action_273_02', 5)	# 10-14
    sprite('Action_273_03', 4)	# 15-18
    sprite('Action_273_04', 1)	# 19-19

@State
def EffReversalSub2():

    def upon_IMMEDIATE():
        Unknown2019(100)
    sprite('Action_274_00', 3)	# 1-3
    SFX_3('SE_Hari_Vanish')
    sprite('Action_274_01', 3)	# 4-6
    sprite('Action_274_02', 3)	# 7-9
    sprite('Action_274_03', 3)	# 10-12
    sprite('Action_274_04', 1)	# 13-13

@State
def EffReversalSub3():

    def upon_IMMEDIATE():
        Unknown2019(100)
    sprite('Action_275_00', 3)	# 1-3
    SFX_3('SE_Hari_Vanish')
    sprite('Action_275_01', 3)	# 4-6
    sprite('Action_275_02', 3)	# 7-9
    sprite('Action_275_03', 3)	# 10-12
    sprite('Action_275_04', 1)	# 13-13

@State
def EffMidShot():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2010()
        AttackLevel_(5)
        Hitstop(5)
        AirUntechableTime(60)
        AirPushbackX(55000)
        AirPushbackY(1500)
        YImpluseBeforeWallbounce(30)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        WallbounceReboundTime(10)
        Unknown9016(1)
    sprite('Action_211_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_211_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_211_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_211_03', 2)	# 7-8	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_211_04', 3)	# 9-11	 **attackbox here**
    sprite('Action_211_05', 3)	# 12-14	 **attackbox here**
    Unknown23029(3, 531, 0)
    sprite('Action_211_06', 3)	# 15-17	 **attackbox here**
    sprite('Action_211_07', 3)	# 18-20	 **attackbox here**
    sprite('Action_211_08', 3)	# 21-23	 **attackbox here**
    sprite('Action_211_09', 3)	# 24-26	 **attackbox here**
    sprite('Action_211_10', 3)	# 27-29	 **attackbox here**
    sprite('Action_211_11', 3)	# 30-32	 **attackbox here**
    sprite('Action_211_12', 3)	# 33-35	 **attackbox here**
    sprite('Action_211_13', 3)	# 36-38	 **attackbox here**
    sprite('Action_211_14', 3)	# 39-41	 **attackbox here**
    SFX_3('SE_Hari_Vanish')
    sprite('Action_211_15', 3)	# 42-44	 **attackbox here**
    sprite('Action_211_16', 3)	# 45-47	 **attackbox here**
    sprite('Action_211_17', 3)	# 48-50	 **attackbox here**
    sprite('Action_211_18', 1)	# 51-51	 **attackbox here**

@State
def EffBackAttackShot():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2010()
        AttackLevel_(5)
        Hitstop(5)
        AirUntechableTime(60)
        Unknown11001(-4, -4, 4)
        AirPushbackX(-125000)
        AirPushbackY(1500)
        PushbackX(-39900)
        YImpluseBeforeWallbounce(30)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        WallbounceReboundTime(0)
        Unknown9016(1)
        Unknown2005()
        Unknown11099(1)
        Unknown1086(22)
        teleportRelativeX(-250000)
        teleportRelativeY(250000)
    sprite('Action_211_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_211_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_211_02', 4)	# 7-10	 **attackbox here**
    sprite('Action_211_03', 4)	# 11-14	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_211_04', 3)	# 15-17	 **attackbox here**
    sprite('Action_211_05', 3)	# 18-20	 **attackbox here**
    Unknown23029(3, 531, 0)
    sprite('Action_211_06', 3)	# 21-23	 **attackbox here**
    sprite('Action_211_07', 3)	# 24-26	 **attackbox here**
    sprite('Action_211_08', 3)	# 27-29	 **attackbox here**
    sprite('Action_211_09', 3)	# 30-32	 **attackbox here**
    sprite('Action_211_10', 3)	# 33-35	 **attackbox here**
    sprite('Action_211_11', 3)	# 36-38	 **attackbox here**
    sprite('Action_211_12', 3)	# 39-41	 **attackbox here**
    sprite('Action_211_13', 3)	# 42-44	 **attackbox here**
    sprite('Action_211_14', 3)	# 45-47	 **attackbox here**
    SFX_3('SE_Hari_Vanish')
    sprite('Action_211_15', 3)	# 48-50	 **attackbox here**
    sprite('Action_211_16', 3)	# 51-53	 **attackbox here**
    sprite('Action_211_17', 3)	# 54-56	 **attackbox here**
    sprite('Action_211_18', 1)	# 57-57	 **attackbox here**

@State
def EffSpreadShotDel():

    def upon_IMMEDIATE():
        Unknown23015(1)
    sprite('Action_254_00', 5)	# 1-5
    sprite('Action_254_01', 10)	# 6-15
    sprite('Action_254_02', 5)	# 16-20
    sprite('Action_254_03', 1)	# 21-21

@State
def SpreadShotMatome():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2010()
        Unknown2003(1)
        Unknown2019(-1000)

        def upon_43():
            if (SLOT_48 == 508):
                SLOT_58 = 1
    sprite('null', 1)	# 1-1
    sprite('null', 10)	# 2-11
    GFX_0('SpreadShotAtk', 100)
    Unknown23029(1, 504, 0)
    if SLOT_58:
        Unknown23029(1, 509, 0)
    GFX_0('SpreadShotAtk', 100)
    Unknown23029(1, 505, 0)
    if SLOT_58:
        Unknown23029(1, 509, 0)
    GFX_0('SpreadShotAtk', 100)
    Unknown23029(1, 506, 0)
    if SLOT_58:
        Unknown23029(1, 509, 0)
    GFX_0('SpreadShotAtk', 100)
    Unknown23029(1, 501, 0)
    if SLOT_58:
        Unknown23029(1, 509, 0)
    GFX_0('SpreadShotAtk', 100)
    Unknown23029(1, 502, 0)
    if SLOT_58:
        Unknown23029(1, 509, 0)
    GFX_0('SpreadShotAtk', 100)
    Unknown23029(1, 503, 0)
    if SLOT_58:
        Unknown23029(1, 509, 0)

@State
def SpreadShotAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown23015(3)
        Unknown2003(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown1096(100)

        def upon_43():
            if (SLOT_48 == 501):
                teleportRelativeX(10000)
                Unknown1007(25000)
                Unknown1072(-10000)
                physicsXImpulse(-5000)
                physicsYImpulse(24000)
                setGravity(1200)
                Unknown1028(650)
                Unknown1074(4500)
                Unknown1091(2)
                Unknown1059(32)
                Unknown1067(18)
            if (SLOT_48 == 502):
                teleportRelativeX(-20000)
                Unknown1007(40000)
                Unknown1072(-20000)
                physicsXImpulse(-9500)
                physicsYImpulse(28000)
                setGravity(1280)
                Unknown1028(500)
                Unknown1074(4800)
                Unknown1091(1)
                Unknown1059(23)
                Unknown1067(18)
            if (SLOT_48 == 503):
                teleportRelativeX(-50000)
                Unknown1007(40000)
                Unknown1072(-38500)
                physicsXImpulse(-18000)
                physicsYImpulse(32000)
                setGravity(1360)
                Unknown1028(500)
                Unknown1074(5000)
                Unknown1059(18)
                Unknown1067(18)
            if (SLOT_48 == 504):
                teleportRelativeX(10000)
                Unknown1007(-25000)
                Unknown1072(190000)
                physicsXImpulse(-5000)
                physicsYImpulse(-24000)
                setGravity(-1200)
                Unknown1028(650)
                Unknown1074(-4500)
                Unknown1091(2)
                Unknown1059(32)
                Unknown1067(18)
            if (SLOT_48 == 505):
                teleportRelativeX(-20000)
                Unknown1007(-40000)
                Unknown1072(200000)
                physicsXImpulse(-9500)
                physicsYImpulse(-28000)
                setGravity(-1280)
                Unknown1028(500)
                Unknown1074(-4800)
                Unknown1091(1)
                Unknown1059(23)
                Unknown1067(18)
            if (SLOT_48 == 506):
                teleportRelativeX(-50000)
                Unknown1007(-40000)
                Unknown1072(218500)
                physicsXImpulse(-18000)
                physicsYImpulse(-32000)
                setGravity(-1360)
                Unknown1028(500)
                Unknown1074(-5000)
                Unknown1059(18)
                Unknown1067(18)
            if (SLOT_48 == 509):
                SLOT_58 = 1

        def upon_53():
            Unknown13(25)
    sprite('null', 3)	# 1-3
    sprite('Action_252_01', 3)	# 4-6
    Unknown1015(1500)
    Unknown1019(30)
    YAccel(30)
    Unknown1039(30)
    Unknown1034(150)
    sprite('Action_252_01', 2)	# 7-8
    Unknown23048('01000000')
    Unknown23051('76725f75686965663235325f6c61795f61667465722e646473000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23050('0f0000000a000000')
    Unknown23049('ffffffffffffff00')
    Unknown23060(25)
    Unknown23052('2a000000')
    Unknown3032()
    sprite('null', 5)	# 9-13
    clearUponHandler(3)

    def upon_CLEAR_OR_EXIT():
        YAccel(106)
        Unknown1034(108)
        Unknown1039(106)
    GFX_0('SpreadShotAtkImg', 100)
    Unknown38(5, 1)
    sprite('null', 15)	# 14-28
    Unknown1019(30)
    YAccel(130)
    Unknown23029(5, 512, 0)
    GFX_0('SpreadShotAtkCol', 100)
    if SLOT_58:
        Unknown23029(1, 510, 0)
    sprite('null', 10)	# 29-38
    Unknown1074(0)
    sprite('null', 90)	# 39-128
    Unknown1034(30)
    Unknown1039(10)

@State
def SpreadShotAtkOld():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2010()
        Unknown53(1)
        Unknown2019(-100)
        Unknown2003(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown1096(400)

        def upon_43():
            if (SLOT_48 == 501):
                teleportRelativeX(-50000)
                Unknown1007(75000)
                Unknown1072(-10000)
                physicsXImpulse(-5000)
                physicsYImpulse(10000)
                setGravity(450)
                Unknown1028(500)
                Unknown1074(3600)
                Unknown1091(2)
                Unknown1059(25)
                Unknown1067(14)
            if (SLOT_48 == 502):
                teleportRelativeX(-80000)
                Unknown1007(90000)
                Unknown1072(-20000)
                physicsXImpulse(-9500)
                physicsYImpulse(12000)
                setGravity(460)
                Unknown1028(550)
                Unknown1074(3300)
                Unknown1091(1)
                Unknown1059(18)
                Unknown1067(14)
            if (SLOT_48 == 503):
                teleportRelativeX(-110000)
                Unknown1007(90000)
                Unknown1072(-38500)
                physicsXImpulse(-12500)
                physicsYImpulse(12000)
                setGravity(360)
                Unknown1028(600)
                Unknown1074(4000)
                Unknown1059(14)
                Unknown1067(14)
            if (SLOT_48 == 504):
                teleportRelativeX(-50000)
                Unknown1007(-75000)
                Unknown1072(-170000)
                physicsXImpulse(-5000)
                physicsYImpulse(-10000)
                setGravity(-450)
                Unknown1028(500)
                Unknown1074(-3600)
                Unknown1091(2)
                Unknown1059(25)
                Unknown1067(14)
            if (SLOT_48 == 505):
                teleportRelativeX(-80000)
                Unknown1007(-90000)
                Unknown1072(-160000)
                physicsXImpulse(-9500)
                physicsYImpulse(-12000)
                setGravity(-460)
                Unknown1028(550)
                Unknown1074(-3300)
                Unknown1091(1)
                Unknown1059(18)
                Unknown1067(14)
            if (SLOT_48 == 506):
                teleportRelativeX(-110000)
                Unknown1007(-90000)
                Unknown1072(-131500)
                physicsXImpulse(-22500)
                physicsYImpulse(-12000)
                setGravity(-360)
                Unknown1028(700)
                Unknown1074(-3100)
                Unknown1059(14)
                Unknown1067(14)
            if (SLOT_48 == 509):
                SLOT_58 = 1

        def upon_CLEAR_OR_EXIT():
            Unknown2038(1)
            if (SLOT_2 >= 2):
                Unknown2037(0)
                GFX_0('SpreadShotHasen', 100)

        def upon_53():
            Unknown13(25)
    sprite('Action_252_01', 2)	# 1-2
    sprite('Action_252_01', 1)	# 3-3
    GFX_0('SpreadShotHasen', 100)
    sprite('Action_252_01', 5)	# 4-8
    Unknown1015(1500)
    Unknown1019(30)
    YAccel(50)
    Unknown1039(80)
    Unknown1034(150)
    sprite('Action_252_01', 5)	# 9-13
    Unknown1074(0)
    clearUponHandler(3)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(105)
        YAccel(105)
        Unknown1034(105)
        Unknown1039(105)
        Unknown1108(90000)
        GFX_0('SpreadShotHasen', 100)
        Unknown2038(1)
        if (SLOT_2 >= 2):
            Unknown2037(0)
            GFX_0('SpreadShotHasen', 100)
sprite('Action_252_01', 300)	# 14-313
GFX_0('SpreadShotAtkCol', 100)
if SLOT_58:
    Unknown23029(1, 510, 0)
endState()

@State
def SpreadShotHasen():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2019(-99)
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown48('19000000020000000d00000002000000020000000d000000')
        Unknown1019(80)
        YAccel(80)
        Unknown1108(90000)
    sprite('Action_253_00', 5)	# 1-5

@State
def SpreadShotAtkImg():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown23015(3)

        def upon_45():
            if SLOT_51:
                Unknown48('19000000020000000c00000002000000020000000c000000')
                Unknown48('19000000020000000d00000002000000020000000d000000')
                Unknown1019(-3)
                YAccel(-3)

        def upon_43():
            if (SLOT_48 == 512):
                SLOT_51 = 1
    sprite('Action_252_01', 300)	# 1-300

@State
def SpreadShotAtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4006(2)
        AttackLevel_(3)
        Damage(800)
        AirPushbackX(12000)
        AirPushbackY(20000)
        Hitstop(5)
        AttackP2(90)
        AirUntechableTime(43)
        Unknown11057(750)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)

        def upon_43():
            if (SLOT_48 == 510):
                AttackP1(70)
                Unknown11042(1)
    sprite('Action_252_01atkcol', 300)	# 1-300

@State
def LowShotAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        AttackLevel_(4)
        Damage(1700)
        AttackP1(70)
        AirPushbackX(0)
        AirPushbackY(32000)
        YImpluseBeforeWallbounce(900)
        AirUntechableTime(30)
        Hitstop(10)
        AttackP2(90)
        Unknown30065(0)
        MinimumDamagePct(10)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown2019(-500)
        HitLow(2)
        Unknown11044(1)
        Unknown11069('LowShotAtkExe')
        Unknown1086(22)
        teleportRelativeY(0)

        def upon_78():
            Unknown23029(3, 511, 0)
    sprite('null', 10)	# 1-10
    sprite('Action_417_00', 1)	# 11-11
    sprite('Action_417_01', 2)	# 12-13
    sprite('Action_417_02', 2)	# 14-15
    sprite('Action_417_03', 2)	# 16-17
    SFX_3('SE_Hari_Appear')
    sprite('Action_417_04', 3)	# 18-20	 **attackbox here**
    sprite('Action_417_05', 3)	# 21-23	 **attackbox here**
    Unknown23029(3, 513, 0)
    sprite('Action_417_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_417_07', 4)	# 28-31	 **attackbox here**
    sprite('Action_417_08', 4)	# 32-35	 **attackbox here**
    sprite('Action_417_09', 4)	# 36-39	 **attackbox here**
    sprite('Action_417_10', 4)	# 40-43	 **attackbox here**
    sprite('Action_417_11', 4)	# 44-47	 **attackbox here**
    sprite('Action_417_12', 4)	# 48-51	 **attackbox here**
    SFX_3('SE_Hari_Vanish')
    sprite('Action_417_13', 4)	# 52-55	 **attackbox here**
    sprite('Action_417_14', 4)	# 56-59	 **attackbox here**
    sprite('Action_417_15', 4)	# 60-63	 **attackbox here**
    sprite('Action_417_16', 4)	# 64-67	 **attackbox here**
    sprite('Action_417_17', 4)	# 68-71	 **attackbox here**

@State
def LowShotAtkExe():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2010()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(63)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(-45000)
        AirUntechableTime(60)
        Unknown9310(30)
        YImpluseBeforeWallbounce(2000)
        Hitstop(10)
        Unknown30065(0)
        MinimumDamagePct(10)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9016(1)
        Unknown11044(1)
        Unknown2019(-1000)
        Unknown1086(22)
        Unknown1007(280000)

        def upon_78():
            Unknown23029(3, 512, 0)
    sprite('Action_418_00', 1)	# 1-1
    sprite('Action_418_01', 1)	# 2-2
    sprite('Action_418_02', 2)	# 3-4
    sprite('Action_418_03', 2)	# 5-6
    sprite('Action_418_04', 1)	# 7-7
    sprite('Action_418_05', 10)	# 8-17	 **attackbox here**
    sprite('Action_418_06', 3)	# 18-20
    sprite('Action_418_07', 3)	# 21-23
    sprite('Action_418_08', 3)	# 24-26
    sprite('Action_418_09', 3)	# 27-29
    sprite('Action_418_10', 3)	# 30-32
    sprite('Action_418_11', 3)	# 33-35
    sprite('Action_418_12', 1)	# 36-36

@State
def EffDelayShotStart():
    sprite('Action_207_00', 4)	# 1-4
    sprite('Action_207_01', 4)	# 5-8
    sprite('Action_207_02', 4)	# 9-12
    sprite('Action_207_03', 4)	# 13-16
    sprite('Action_207_04', 4)	# 17-20
    sprite('Action_207_05', 3)	# 21-23

@Subroutine
def DelayShotCharge_Param():
    Unknown4010(3)
    Unknown4011(2)
    Unknown2019(-999)
    Unknown2053(1)
    Unknown23013(1)
    Unknown23022(1)
    loopRelated(17, 240)

    def upon_17():
        Unknown13(25)

    def upon_CLEAR_OR_EXIT():
        if SLOT_IsInOverdrive2:
            Unknown2038(1)
            if (not SLOT_51):
                if (SLOT_2 <= 20):
                    Unknown1019(95)
                    YAccel(95)
                else:
                    SLOT_51 = 1
                    SLOT_2 = 0
            elif (not SLOT_52):
                if (SLOT_2 <= 20):
                    Unknown1019(95)
                    YAccel(95)
                else:
                    Unknown4007(0)
                    SLOT_52 = 1
                    SLOT_2 = 0
            elif (not SLOT_53):
                if (SLOT_2 >= 2):
                    Unknown1084(1)
                    SLOT_53 = 1
                    SLOT_2 = 0
                    if (not SLOT_55):
                        SLOT_55 = 1
                        GFX_0('DelayShotAtkMatome', 100)
                        Unknown38(5, 1)
            elif (SLOT_2 >= 32):
                clearUponHandler(3)
                sendToLabel(1)

    def upon_43():
        if (SLOT_48 == 521):
            SLOT_54 = 1
            Unknown4010(0)
            Unknown4007(0)
        if (SLOT_48 == 522):
            physicsXImpulse(25000)
            physicsYImpulse(13000)
        if (SLOT_48 == 523):
            physicsXImpulse(25000)
            physicsYImpulse(-13000)

    def upon_53():
        Unknown23090(25)

    def upon_54():
        clearUponHandler(3)
        clearUponHandler(53)
        Unknown1084(1)
        Unknown23090(5)
        sendToLabel(1)

@State
def EffDelayShotCharge():

    def upon_IMMEDIATE():
        Unknown4007(3)
        callSubroutine('DelayShotCharge_Param')
    sprite('Action_203_00', 3)	# 1-3
    sprite('Action_203_01', 3)	# 4-6
    sprite('Action_203_02', 3)	# 7-9
    sprite('Action_203_03', 3)	# 10-12
    label(0)
    sprite('Action_203_04', 3)	# 13-15
    sprite('Action_203_05', 3)	# 16-18
    sprite('Action_203_06', 3)	# 19-21
    sprite('Action_203_07', 3)	# 22-24
    sprite('Action_203_08', 3)	# 25-27
    sprite('Action_203_09', 3)	# 28-30
    sprite('Action_203_10', 3)	# 31-33
    sprite('Action_203_11', 3)	# 34-36
    gotoLabel(0)
    label(1)
    sprite('Action_203_12', 3)	# 37-39
    sprite('Action_203_13', 3)	# 40-42
    SFX_3('SE_Hari_Vanish')
    sprite('Action_203_14', 3)	# 43-45
    sprite('Action_203_15', 3)	# 46-48

@State
def DelayShotAtkMatome():

    def upon_IMMEDIATE():
        Unknown4011(3)
        AttackLevel_(2)
        AttackP2(80)
        Unknown11092(1)
        SLOT_6 = 0
        SLOT_7 = 0
        if (SLOT_163 >= 150000):
            SLOT_6 = 1
        if (SLOT_163 <= (-150000)):
            SLOT_7 = 1

        def upon_STATE_END():
            SLOT_6 = 0
            SLOT_7 = 0

        def upon_53():
            Unknown13(25)
    sprite('null', 3)	# 1-3
    GFX_0('DelayShotAtkCol1', 100)
    sprite('null', 3)	# 4-6
    GFX_0('DelayShotAtkCol2', 100)
    sprite('null', 3)	# 7-9
    GFX_0('DelayShotAtkCol1', 100)
    Unknown36(1)
    teleportRelativeX(7000)
    Unknown1015(3500)
    Unknown35()
    sprite('null', 3)	# 10-12
    GFX_0('DelayShotAtkCol2', 100)
    Unknown36(1)
    teleportRelativeX(-7000)
    Unknown1015(-3500)
    Unknown35()
    sprite('null', 3)	# 13-15
    GFX_0('DelayShotAtkCol1', 100)
    Unknown36(1)
    teleportRelativeX(-2500)
    Unknown1015(-2500)
    Unknown35()
    sprite('null', 3)	# 16-18
    GFX_0('DelayShotAtkCol2', 100)
    Unknown36(1)
    teleportRelativeX(-2500)
    Unknown1015(2500)
    Unknown35()
    sprite('null', 3)	# 19-21
    GFX_0('DelayShotAtkCol1', 100)
    Unknown36(1)
    teleportRelativeX(6500)
    Unknown1015(6500)
    Unknown35()
    sprite('null', 3)	# 22-24
    GFX_0('DelayShotAtkCol2', 100)
    Unknown36(1)
    teleportRelativeX(-6500)
    Unknown1015(-6500)
    Unknown35()

@State
def DelayShotAtkCol1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2010()
        AttackLevel_(2)
        Damage(500)
        PushbackX(8000)
        AttackP2(80)
        Unknown11092(1)
        Hitstop(3)
        AirUntechableTime(25)
        AirPushbackY(15000)
        physicsXImpulse(1500)
        physicsYImpulse(-23000)
        Unknown9016(1)
        Unknown23182(2)
        if SLOT_6:
            Unknown1015(9000)
        if SLOT_7:
            Unknown1015(-9000)

        def upon_53():
            Unknown13(25)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_23 <= 250000):
                Unknown1019(95)
                YAccel(95)
            if (SLOT_23 <= 100000):
                if (not SLOT_51):
                    SLOT_51 = 1
                    Unknown1019(50)
                    YAccel(50)
                    sendToLabel(0)
    sprite('null', 2)	# 1-2
    sprite('Action_205_00', 5)	# 3-7	 **attackbox here**
    Unknown1108(90000)
    SFX_3('SE_DrawnSword')
    sprite('Action_205_01', 5)	# 8-12	 **attackbox here**
    sprite('Action_205_02', 30)	# 13-42	 **attackbox here**
    label(0)
    sprite('Action_205_03', 5)	# 43-47
    DisableAttackRestOfMove()
    sprite('Action_205_04', 5)	# 48-52
    sprite('Action_205_05', 5)	# 53-57
    sprite('Action_205_06', 5)	# 58-62

@State
def DelayShotAtkCol2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2010()
        AttackLevel_(2)
        Damage(500)
        PushbackX(8000)
        AttackP2(80)
        Unknown11092(1)
        Hitstop(3)
        AirUntechableTime(25)
        AirPushbackY(15000)
        physicsXImpulse(-3500)
        physicsYImpulse(-23000)
        Unknown9016(1)
        Unknown23182(2)
        if SLOT_6:
            Unknown1015(9000)
        if SLOT_7:
            Unknown1015(-9000)

        def upon_53():
            Unknown13(25)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_23 <= 250000):
                Unknown1019(95)
                YAccel(95)
            if (SLOT_23 <= 100000):
                if (not SLOT_51):
                    SLOT_51 = 1
                    Unknown1019(50)
                    YAccel(50)
                    sendToLabel(0)
    sprite('null', 2)	# 1-2
    sprite('Action_205_08', 5)	# 3-7	 **attackbox here**
    Unknown1108(90000)
    SFX_3('SE_DrawnSword')
    sprite('Action_205_09', 5)	# 8-12	 **attackbox here**
    sprite('Action_205_10', 30)	# 13-42	 **attackbox here**
    label(0)
    sprite('Action_205_11', 5)	# 43-47
    DisableAttackRestOfMove()
    sprite('Action_205_12', 5)	# 48-52
    sprite('Action_205_13', 5)	# 53-57
    sprite('Action_205_14', 5)	# 58-62

@State
def WarpShotAtkMatome():

    def upon_IMMEDIATE():
        Unknown4011(2)
        AttackLevel_(2)
        AttackP2(80)
        Unknown11092(1)
        Unknown4007(3)

        def upon_53():
            Unknown13(25)
    sprite('null', 3)	# 1-3
    GFX_0('WarpShotAtkCol1', 100)
    sprite('null', 3)	# 4-6
    GFX_0('WarpShotAtkCol2', 100)
    sprite('null', 3)	# 7-9
    GFX_0('WarpShotAtkCol1', 100)
    Unknown36(1)
    Unknown1021(3500)
    Unknown35()
    sprite('null', 3)	# 10-12
    GFX_0('WarpShotAtkCol2', 100)
    Unknown36(1)
    Unknown1021(-3500)
    Unknown35()
    sprite('null', 3)	# 13-15
    GFX_0('WarpShotAtkCol1', 100)
    Unknown36(1)
    Unknown1021(-2500)
    Unknown35()
    sprite('null', 3)	# 16-18
    GFX_0('WarpShotAtkCol2', 100)
    Unknown36(1)
    Unknown1021(2500)
    Unknown35()
    sprite('null', 3)	# 19-21
    GFX_0('WarpShotAtkCol1', 100)
    Unknown36(1)
    Unknown1021(6500)
    Unknown35()
    sprite('null', 3)	# 22-24
    GFX_0('WarpShotAtkCol2', 100)
    Unknown36(1)
    Unknown1021(-6500)
    Unknown35()

@State
def EffDropShot_Pacchin():
    sprite('Action_432_00', 5)	# 1-5
    sprite('Action_432_01', 5)	# 6-10
    sprite('Action_432_02', 1)	# 11-11

@State
def EffDropShot_Landing():

    def upon_IMMEDIATE():
        Unknown2019(-101)
    sprite('Action_434_00', 4)	# 1-4
    sprite('Action_434_01', 4)	# 5-8
    sprite('Action_434_02', 4)	# 9-12
    sprite('Action_434_03', 1)	# 13-13

@State
def EffDropShot_Ralease():

    def upon_IMMEDIATE():
        Unknown2019(-101)
    sprite('Action_433_00', 3)	# 1-3
    sprite('Action_433_01', 3)	# 4-6
    sprite('Action_433_02', 3)	# 7-9
    sprite('Action_433_03', 3)	# 10-12
    sprite('Action_433_04', 3)	# 13-15
    sprite('Action_433_05', 3)	# 16-18
    sprite('Action_433_06', 1)	# 19-19

@State
def EffDropShot_Atk():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2010()
        AttackLevel_(4)
        AttackP2(75)
        Unknown11092(1)
        HitOverhead(2)
        AirPushbackX(0)
        AirPushbackY(-75000)
        PushbackX(0)
        AirUntechableTime(60)
        hitstun(25)
        Unknown9310(1)
        Hitstop(3)
        Unknown11001(0, 6, 6)
        Unknown9016(1)
        AirHitstunAnimation(10)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown2053(1)
        Unknown2034(1)
        Unknown1096(1200)
        Unknown1086(22)
        Unknown1007(650000)

        def upon_78():
            Unknown2038(1)

        def upon_53():
            sendToLabel(580)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_23 <= (-150000)):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('Action_441_00', 3)	# 1-3
    sprite('Action_441_01', 3)	# 4-6
    Unknown2053(0)
    Unknown2034(0)
    SFX_3('SE_Hari_Appear')
    sprite('Action_441_02', 2)	# 7-8
    sprite('Action_441_03', 2)	# 9-10
    sprite('Action_441_04', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(-75000)
    sprite('Action_441_05', 3)	# 14-16	 **attackbox here**
    sprite('Action_441_06', 3)	# 17-19	 **attackbox here**
    label(0)
    sprite('Action_441_07', 3)	# 20-22	 **attackbox here**
    sprite('Action_441_08', 3)	# 23-25	 **attackbox here**
    sprite('Action_441_09', 3)	# 26-28	 **attackbox here**
    sprite('Action_441_10', 3)	# 29-31	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_441_11ex01', 1)	# 32-32	 **attackbox here**
    GFX_0('EffDropShot_Landing', 100)
    Unknown1084(1)
    teleportRelativeY(-150000)
    sprite('Action_441_11', 1)	# 33-33
    Unknown19(580, 2, 2)
    sprite('Action_441_12', 3)	# 34-36	 **attackbox here**
    RefreshMultihit()
    Damage(0)
    Unknown9130(18)
    Unknown9142(100)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Hitstop(0)
    Unknown30048(1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(78)
    sendToLabelUpon(78, 580)
    sprite('Action_441_13', 3)	# 37-39	 **attackbox here**
    label(580)
    sprite('Action_441_14', 3)	# 40-42	 **attackbox here**
    sprite('Action_441_15', 3)	# 43-45	 **attackbox here**
    sprite('Action_441_16', 3)	# 46-48	 **attackbox here**
    sprite('Action_441_17', 3)	# 49-51	 **attackbox here**
    sprite('Action_441_18', 3)	# 52-54	 **attackbox here**
    sprite('Action_441_19', 3)	# 55-57	 **attackbox here**
    sprite('Action_441_20', 3)	# 58-60	 **attackbox here**
    sprite('Action_441_21', 3)	# 61-63	 **attackbox here**
    GFX_0('EffDropShot_Ralease', 100)
    SFX_3('SE_Hari_Vanish')
    sprite('Action_441_22', 3)	# 64-66	 **attackbox here**
    sprite('Action_441_23', 3)	# 67-69	 **attackbox here**
    sprite('Action_441_24', 3)	# 70-72	 **attackbox here**
    sprite('Action_441_25', 3)	# 73-75	 **attackbox here**

@Subroutine
def StormShotAtkParam():
    Unknown2010()
    Unknown4011(2)
    AttackLevel_(3)
    Damage(600)
    hitstun(23)
    AirUntechableTime(23)
    AttackP1(80)
    AttackP2(90)
    Hitstop(2)
    PushbackX(6600)
    Unknown9016(1)
    Unknown11057(300)
    Unknown23013(1)

    def upon_44():
        DisableAttackRestOfMove()
        Unknown2003(1)

    def upon_53():
        Unknown13(25)

@State
def StormShotCharge():

    def upon_IMMEDIATE():
        Unknown2019(1000)
        Unknown1007(450000)
        teleportRelativeX(-150000)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 1)

        def upon_53():
            Unknown23090(25)
    sprite('Action_450_00', 5)	# 1-5
    sprite('Action_450_01', 5)	# 6-10
    sprite('Action_450_02', 5)	# 11-15
    Unknown2037(4)
    label(0)
    sprite('Action_450_03', 5)	# 16-20
    Unknown2038(-1)
    sprite('Action_450_04', 5)	# 21-25
    sprite('Action_450_05', 5)	# 26-30
    GFX_0('StormShotAtkMatome', 100)
    SFX_3('SE_DrawnSword')
    sprite('Action_450_06', 5)	# 31-35
    if SLOT_2:
        _gotolabel(0)
    label(1)
    sprite('Action_450_07', 5)	# 36-40
    sprite('Action_450_08', 5)	# 41-45
    sprite('Action_450_09', 2)	# 46-47

@State
def StormShotAtkMatome():

    def upon_IMMEDIATE():
        Unknown4011(3)
        teleportRelativeX(80000)
        Unknown1007(-80000)

        def upon_53():
            Unknown13(25)
    sprite('null', 5)	# 1-5
    sprite('null', 2)	# 6-7
    GFX_0('StormShotAtk1', 100)
    sprite('null', 2)	# 8-9
    GFX_0('StormShotAtk2', 100)
    sprite('null', 2)	# 10-11
    GFX_0('StormShotAtk3', 100)
    sprite('null', 2)	# 12-13
    GFX_0('StormShotAtk4', 100)
    sprite('null', 2)	# 14-15
    GFX_0('StormShotAtk5', 100)
    sprite('null', 2)	# 16-17
    GFX_0('StormShotAtk6', 100)
    sprite('null', 2)	# 18-19
    GFX_0('StormShotAtk7', 100)

@State
def StormShotAtk1():

    def upon_IMMEDIATE():
        callSubroutine('StormShotAtkParam')
    sprite('Action_451_00', 3)	# 1-3
    sprite('Action_451_01', 3)	# 4-6
    sprite('Action_451_02', 3)	# 7-9
    sprite('Action_451_03', 3)	# 10-12
    physicsXImpulse(75000)
    physicsYImpulse(-84000)
    sendToLabelUpon(2, 1)
    sprite('Action_451_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_451_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_451_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_451_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_451_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_451_08', 3)	# 28-30
    sprite('Action_451_09', 3)	# 31-33
    sprite('Action_451_10', 3)	# 34-36
    sprite('Action_451_11', 3)	# 37-39
    sprite('Action_451_12', 3)	# 40-42
    sprite('Action_451_13', 3)	# 43-45
    sprite('Action_451_14', 3)	# 46-48
    sprite('Action_451_15', 1)	# 49-49

@State
def StormShotAtk2():

    def upon_IMMEDIATE():
        callSubroutine('StormShotAtkParam')
    sprite('Action_452_00', 3)	# 1-3
    teleportRelativeX(192000)
    sprite('Action_452_01', 3)	# 4-6
    sprite('Action_452_02', 3)	# 7-9
    sprite('Action_452_03', 3)	# 10-12
    physicsXImpulse(144000)
    physicsYImpulse(-66000)
    sendToLabelUpon(2, 1)
    sprite('Action_452_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_452_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_452_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_452_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_452_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_452_08', 3)	# 28-30
    sprite('Action_452_09', 3)	# 31-33
    sprite('Action_452_10', 3)	# 34-36
    sprite('Action_452_11', 3)	# 37-39
    sprite('Action_452_12', 3)	# 40-42
    sprite('Action_452_13', 3)	# 43-45
    sprite('Action_452_14', 3)	# 46-48
    sprite('Action_452_15', 1)	# 49-49

@State
def StormShotAtk3():

    def upon_IMMEDIATE():
        callSubroutine('StormShotAtkParam')
    sprite('Action_453_00', 3)	# 1-3
    teleportRelativeX(-72000)
    sprite('Action_453_01', 3)	# 4-6
    sprite('Action_453_02', 3)	# 7-9
    sprite('Action_453_03', 3)	# 10-12
    physicsXImpulse(54000)
    physicsYImpulse(-90000)
    sendToLabelUpon(2, 1)
    sprite('Action_453_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_453_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_453_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_453_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_453_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_453_08', 3)	# 28-30
    sprite('Action_453_09', 3)	# 31-33
    sprite('Action_453_10', 3)	# 34-36
    sprite('Action_453_11', 3)	# 37-39
    sprite('Action_453_12', 3)	# 40-42
    sprite('Action_453_13', 3)	# 43-45
    sprite('Action_453_14', 3)	# 46-48
    sprite('Action_453_15', 1)	# 49-49

@State
def StormShotAtk4():

    def upon_IMMEDIATE():
        callSubroutine('StormShotAtkParam')
    sprite('Action_454_00', 3)	# 1-3
    teleportRelativeX(120000)
    Unknown1007(100000)
    sprite('Action_454_01', 3)	# 4-6
    sprite('Action_454_02', 3)	# 7-9
    sprite('Action_454_03', 3)	# 10-12
    physicsXImpulse(90000)
    physicsYImpulse(-75000)
    sendToLabelUpon(2, 1)
    sprite('Action_454_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_454_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_454_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_454_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_454_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_454_08', 3)	# 28-30
    sprite('Action_454_09', 3)	# 31-33
    sprite('Action_454_10', 3)	# 34-36
    sprite('Action_454_11', 3)	# 37-39
    sprite('Action_454_12', 3)	# 40-42
    sprite('Action_454_13', 3)	# 43-45
    sprite('Action_454_14', 3)	# 46-48
    sprite('Action_454_15', 1)	# 49-49

@State
def StormShotAtk5():

    def upon_IMMEDIATE():
        callSubroutine('StormShotAtkParam')
    sprite('Action_455_00', 3)	# 1-3
    teleportRelativeX(-32000)
    sprite('Action_455_01', 3)	# 4-6
    sprite('Action_455_02', 3)	# 7-9
    sprite('Action_455_03', 3)	# 10-12
    physicsXImpulse(24000)
    physicsYImpulse(-90000)
    sendToLabelUpon(2, 1)
    sprite('Action_455_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_455_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_455_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_455_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_455_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_455_08', 3)	# 28-30
    sprite('Action_455_09', 3)	# 31-33
    sprite('Action_455_10', 3)	# 34-36
    sprite('Action_455_11', 3)	# 37-39
    sprite('Action_455_12', 3)	# 40-42
    sprite('Action_455_13', 3)	# 43-45
    sprite('Action_455_14', 3)	# 46-48
    sprite('Action_455_15', 1)	# 49-49

@State
def StormShotAtk6():

    def upon_IMMEDIATE():
        callSubroutine('StormShotAtkParam')
    sprite('Action_456_00', 3)	# 1-3
    teleportRelativeX(-60000)
    sprite('Action_456_01', 3)	# 4-6
    sprite('Action_456_02', 3)	# 7-9
    sprite('Action_456_03', 3)	# 10-12
    physicsXImpulse(45000)
    physicsYImpulse(-90000)
    sendToLabelUpon(2, 1)
    sprite('Action_456_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_456_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_456_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_456_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_456_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_456_08', 3)	# 28-30
    sprite('Action_456_09', 3)	# 31-33
    sprite('Action_456_10', 3)	# 34-36
    sprite('Action_456_11', 3)	# 37-39
    sprite('Action_456_12', 3)	# 40-42
    sprite('Action_456_13', 3)	# 43-45
    sprite('Action_456_14', 3)	# 46-48
    sprite('Action_456_15', 1)	# 49-49

@State
def StormShotAtk7():

    def upon_IMMEDIATE():
        callSubroutine('StormShotAtkParam')
    sprite('Action_457_00', 3)	# 1-3
    teleportRelativeX(80000)
    sprite('Action_457_01', 3)	# 4-6
    sprite('Action_457_02', 3)	# 7-9
    sprite('Action_457_03', 3)	# 10-12
    physicsXImpulse(60000)
    physicsYImpulse(-90000)
    sendToLabelUpon(2, 1)
    sprite('Action_457_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_457_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_457_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_457_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_457_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_457_08', 3)	# 28-30
    sprite('Action_457_09', 3)	# 31-33
    sprite('Action_457_10', 3)	# 34-36
    sprite('Action_457_11', 3)	# 37-39
    sprite('Action_457_12', 3)	# 40-42
    sprite('Action_457_13', 3)	# 43-45
    sprite('Action_457_14', 3)	# 46-48
    sprite('Action_457_15', 1)	# 49-49

@State
def AllRangeShotFade():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 10)	# 1-10
    Unknown3004(25)
    sprite('vr_white', 10)	# 11-20
    Unknown3001(255)
    Unknown3004(0)
    sprite('vr_white', 10)	# 21-30
    Unknown3004(-25)

@State
def AllRangeShotAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(262)
        MinimumDamagePct(8)
        Unknown11064(1)
        AttackP2(100)
        Unknown11092(1)
        Hitstop(1)
        AirPushbackX(0)
        AirPushbackY(10)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(300)
        Unknown9016(1)
        Unknown30048(1)
        Unknown11023(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown11069('AllRangeShotAtk')

        def upon_43():
            if (SLOT_48 == 1150):
                Damage(50)
                AttackP1(100)
                AttackP2(100)
                MinimumDamagePct(100)
                SLOT_58 = 1
            if (SLOT_48 == 1151):
                Unknown20000(0)
                Unknown20003(0)
    sprite('null', 11)	# 1-11
    GFX_0('AllRangeShotFade', 100)
    Unknown1086(22)
    teleportRelativeY(550000)
    sprite('null', 9)	# 12-20
    Unknown36(22)
    teleportRelativeY(150000)
    Unknown35()
    sprite('null', 10)	# 21-30
    GFX_0('AllRangeShotEff1', 100)
    GFX_0('AllRangeShotEff2', 100)
    GFX_0('AllRangeShotEff4', 100)
    GFX_0('AllRangeShotEff5', 100)
    GFX_0('AllRangeShotEff6', 100)
    GFX_0('AllRangeShotEff7', 100)
    GFX_0('AllRangeShotEff8', 100)
    GFX_0('AllRangeShotEff10', 100)
    GFX_0('AllRangeShotEff11', 100)
    GFX_0('AllRangeShotEff12', 100)
    GFX_0('AllRangeShotEff13', 100)
    GFX_0('AllRangeShotEff14', 100)
    GFX_0('AllRangeShotEff15', 100)
    GFX_0('AllRangeShotEff16', 100)
    GFX_0('AllRangeShotEff17', 100)
    sprite('null', 10)	# 31-40
    SLOT_105 = 1800
    sprite('null', 20)	# 41-60
    SFX_3('SE_Hari_Appear')
    sprite('null', 3)	# 61-63
    Unknown21015('416c6c52616e676553686f744566663100000000000000000000000000000000e903000000000000')
    physicsYImpulse(-600)

    def upon_CLEAR_OR_EXIT():
        SLOT_105 = (SLOT_105 - 4)
        if (SLOT_105 <= 900):
            clearUponHandler(3)
            physicsYImpulse(0)
            SLOT_105 = 900
    sprite('Action_235atkcol', 6)	# 64-69
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663200000000000000000000000000000000ea03000000000000')
    sprite('Action_235atkcol', 6)	# 70-75
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663800000000000000000000000000000000eb03000000000000')
    sprite('Action_235atkcol', 6)	# 76-81
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663400000000000000000000000000000000ec03000000000000')
    sprite('Action_235atkcol', 6)	# 82-87
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663500000000000000000000000000000000ed03000000000000')
    sprite('Action_235atkcol', 6)	# 88-93
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663600000000000000000000000000000000ee03000000000000')
    sprite('Action_235atkcol', 6)	# 94-99
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663700000000000000000000000000000000ef03000000000000')
    sprite('Action_235atkcol', 6)	# 100-105
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663800000000000000000000000000000000f003000000000000')
    sprite('Action_235atkcol', 6)	# 106-111
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663100000000000000000000000000000000f103000000000000')
    sprite('Action_235atkcol', 6)	# 112-117
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663130000000000000000000000000000000f203000000000000')
    sprite('Action_235atkcol', 6)	# 118-123
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663131000000000000000000000000000000f303000000000000')
    sprite('Action_235atkcol', 6)	# 124-129
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663132000000000000000000000000000000f403000000000000')
    sprite('null', 20)	# 130-149
    sprite('null', 8)	# 150-157
    clearUponHandler(3)
    physicsYImpulse(0)
    SFX_3('SE_Hari_Appear')
    sprite('Action_235atkcol', 1)	# 158-158
    Unknown21015('416c6c52616e676553686f7445666631000000000000000000000000000000004d04000000000000')
    Unknown21015('416c6c52616e676553686f7445666632000000000000000000000000000000004e04000000000000')
    Unknown21015('416c6c52616e676553686f7445666634000000000000000000000000000000005004000000000000')
    Unknown21015('416c6c52616e676553686f7445666635000000000000000000000000000000005104000000000000')
    Unknown21015('416c6c52616e676553686f7445666636000000000000000000000000000000005204000000000000')
    Unknown21015('416c6c52616e676553686f7445666637000000000000000000000000000000005304000000000000')
    Unknown21015('416c6c52616e676553686f7445666638000000000000000000000000000000005404000000000000')
    Unknown21015('416c6c52616e676553686f7445666631300000000000000000000000000000005604000000000000')
    Unknown21015('416c6c52616e676553686f7445666631310000000000000000000000000000005704000000000000')
    Unknown21015('416c6c52616e676553686f7445666631320000000000000000000000000000005804000000000000')
    Unknown21015('416c6c52616e676553686f7445666631330000000000000000000000000000005904000000000000')
    Unknown21015('416c6c52616e676553686f7445666631340000000000000000000000000000005a04000000000000')
    Unknown21015('416c6c52616e676553686f7445666631350000000000000000000000000000005b04000000000000')
    Unknown21015('416c6c52616e676553686f7445666631360000000000000000000000000000005c04000000000000')
    Unknown21015('416c6c52616e676553686f7445666631370000000000000000000000000000005d04000000000000')
    sprite('Action_235atkcol', 40)	# 159-198
    RefreshMultihit()
    Damage(7685)
    MinimumDamagePct(18)
    Unknown11064(0)
    Hitstop(20)
    AirPushbackY(30000)
    YImpluseBeforeWallbounce(2000)
    Unknown9310(1)
    Unknown11069('')
    ScreenShake(50000, 50000)
    if SLOT_58:
        Damage(1700)
        MinimumDamagePct(100)

    def upon_78():
        SFX_3('SE_BigBomb_Short')

@State
def AllRangeShotAtkOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(185)
        MinimumDamagePct(8)
        Unknown11064(1)
        AttackP2(100)
        Unknown11092(1)
        Hitstop(1)
        AirPushbackX(0)
        AirPushbackY(10)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(300)
        Unknown9016(1)
        Unknown30048(1)
        Unknown11023(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown11069('AllRangeShotAtkOD')

        def upon_43():
            if (SLOT_48 == 1150):
                Damage(50)
                AttackP1(100)
                AttackP2(100)
                MinimumDamagePct(100)
                SLOT_58 = 1
            if (SLOT_48 == 1151):
                Unknown20000(0)
                Unknown20003(0)
    sprite('null', 11)	# 1-11
    GFX_0('AllRangeShotFade', 100)
    Unknown1086(22)
    teleportRelativeY(550000)
    sprite('null', 9)	# 12-20
    Unknown36(22)
    teleportRelativeY(150000)
    Unknown35()
    sprite('null', 10)	# 21-30
    GFX_0('AllRangeShotEff1', 100)
    GFX_0('AllRangeShotEff2', 100)
    GFX_0('AllRangeShotEff4', 100)
    GFX_0('AllRangeShotEff5', 100)
    GFX_0('AllRangeShotEff6', 100)
    GFX_0('AllRangeShotEff7', 100)
    GFX_0('AllRangeShotEff8', 100)
    GFX_0('AllRangeShotEff10', 100)
    GFX_0('AllRangeShotEff11', 100)
    GFX_0('AllRangeShotEff12', 100)
    GFX_0('AllRangeShotEff13', 100)
    GFX_0('AllRangeShotEff14', 100)
    GFX_0('AllRangeShotEff15', 100)
    GFX_0('AllRangeShotEff16', 100)
    GFX_0('AllRangeShotEff17', 100)
    sprite('null', 10)	# 31-40
    SLOT_105 = 1800
    sprite('null', 20)	# 41-60
    SFX_3('SE_Hari_Appear')
    sprite('null', 3)	# 61-63
    Unknown21015('416c6c52616e676553686f744566663100000000000000000000000000000000e903000000000000')
    physicsYImpulse(-600)

    def upon_CLEAR_OR_EXIT():
        SLOT_105 = (SLOT_105 - 3)
        if (SLOT_105 <= 900):
            clearUponHandler(3)
            physicsYImpulse(0)
            SLOT_105 = 900
    sprite('Action_235atkcol', 6)	# 64-69
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663200000000000000000000000000000000ea03000000000000')
    sprite('Action_235atkcol', 6)	# 70-75
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663800000000000000000000000000000000eb03000000000000')
    sprite('Action_235atkcol', 6)	# 76-81
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663400000000000000000000000000000000ec03000000000000')
    sprite('Action_235atkcol', 6)	# 82-87
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663500000000000000000000000000000000ed03000000000000')
    sprite('Action_235atkcol', 6)	# 88-93
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663600000000000000000000000000000000ee03000000000000')
    sprite('Action_235atkcol', 6)	# 94-99
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663700000000000000000000000000000000ef03000000000000')
    sprite('Action_235atkcol', 6)	# 100-105
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663800000000000000000000000000000000f003000000000000')
    sprite('Action_235atkcol', 6)	# 106-111
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663100000000000000000000000000000000f103000000000000')
    sprite('Action_235atkcol', 6)	# 112-117
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663130000000000000000000000000000000f203000000000000')
    sprite('Action_235atkcol', 6)	# 118-123
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663131000000000000000000000000000000f303000000000000')
    sprite('Action_235atkcol', 6)	# 124-129
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663132000000000000000000000000000000f403000000000000')
    sprite('Action_235atkcol', 6)	# 130-135
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663133000000000000000000000000000000f503000000000000')
    sprite('Action_235atkcol', 6)	# 136-141
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663134000000000000000000000000000000f603000000000000')
    sprite('Action_235atkcol', 6)	# 142-147
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663135000000000000000000000000000000f703000000000000')
    sprite('Action_235atkcol', 6)	# 148-153
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663136000000000000000000000000000000f803000000000000')
    sprite('Action_235atkcol', 6)	# 154-159
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663137000000000000000000000000000000f903000000000000')
    sprite('Action_235atkcol', 3)	# 160-162
    RefreshMultihit()
    SFX_3('SE_Hari_Appear')
    Unknown21015('416c6c52616e676553686f744566663100000000000000000000000000000000e903000000000000')
    sprite('Action_235atkcol', 3)	# 163-165
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663200000000000000000000000000000000ea03000000000000')
    sprite('Action_235atkcol', 3)	# 166-168
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663800000000000000000000000000000000eb03000000000000')
    sprite('Action_235atkcol', 3)	# 169-171
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663400000000000000000000000000000000ec03000000000000')
    sprite('Action_235atkcol', 3)	# 172-174
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663500000000000000000000000000000000ed03000000000000')
    sprite('Action_235atkcol', 3)	# 175-177
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663600000000000000000000000000000000ee03000000000000')
    sprite('Action_235atkcol', 3)	# 178-180
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663700000000000000000000000000000000ef03000000000000')
    sprite('Action_235atkcol', 3)	# 181-183
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663800000000000000000000000000000000f003000000000000')
    sprite('Action_235atkcol', 3)	# 184-186
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663100000000000000000000000000000000f103000000000000')
    sprite('Action_235atkcol', 3)	# 187-189
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663130000000000000000000000000000000f203000000000000')
    sprite('Action_235atkcol', 3)	# 190-192
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663131000000000000000000000000000000f303000000000000')
    sprite('Action_235atkcol', 3)	# 193-195
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663132000000000000000000000000000000f403000000000000')
    sprite('Action_235atkcol', 3)	# 196-198
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663133000000000000000000000000000000f503000000000000')
    sprite('Action_235atkcol', 3)	# 199-201
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663134000000000000000000000000000000f603000000000000')
    sprite('Action_235atkcol', 3)	# 202-204
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663135000000000000000000000000000000f703000000000000')
    sprite('Action_235atkcol', 3)	# 205-207
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663136000000000000000000000000000000f803000000000000')
    sprite('Action_235atkcol', 3)	# 208-210
    RefreshMultihit()
    Unknown21015('416c6c52616e676553686f744566663137000000000000000000000000000000f903000000000000')
    sprite('null', 20)	# 211-230
    sprite('null', 8)	# 231-238
    clearUponHandler(3)
    physicsYImpulse(0)
    SFX_3('SE_Hari_Appear')
    sprite('Action_235atkcol', 1)	# 239-239
    Unknown21015('416c6c52616e676553686f7445666631000000000000000000000000000000004d04000000000000')
    Unknown21015('416c6c52616e676553686f7445666632000000000000000000000000000000004e04000000000000')
    Unknown21015('416c6c52616e676553686f7445666634000000000000000000000000000000005004000000000000')
    Unknown21015('416c6c52616e676553686f7445666635000000000000000000000000000000005104000000000000')
    Unknown21015('416c6c52616e676553686f7445666636000000000000000000000000000000005204000000000000')
    Unknown21015('416c6c52616e676553686f7445666637000000000000000000000000000000005304000000000000')
    Unknown21015('416c6c52616e676553686f7445666638000000000000000000000000000000005404000000000000')
    Unknown21015('416c6c52616e676553686f7445666631300000000000000000000000000000005604000000000000')
    Unknown21015('416c6c52616e676553686f7445666631310000000000000000000000000000005704000000000000')
    Unknown21015('416c6c52616e676553686f7445666631320000000000000000000000000000005804000000000000')
    Unknown21015('416c6c52616e676553686f7445666631330000000000000000000000000000005904000000000000')
    Unknown21015('416c6c52616e676553686f7445666631340000000000000000000000000000005a04000000000000')
    Unknown21015('416c6c52616e676553686f7445666631350000000000000000000000000000005b04000000000000')
    Unknown21015('416c6c52616e676553686f7445666631360000000000000000000000000000005c04000000000000')
    Unknown21015('416c6c52616e676553686f7445666631370000000000000000000000000000005d04000000000000')
    sprite('Action_235atkcol', 40)	# 240-279
    RefreshMultihit()
    Damage(7139)
    MinimumDamagePct(16)
    Unknown11064(0)
    Hitstop(20)
    AirPushbackY(30000)
    YImpluseBeforeWallbounce(2000)
    Unknown9310(1)
    Unknown11069('')
    ScreenShake(75000, 75000)
    if SLOT_58:
        Damage(1100)
        MinimumDamagePct(100)

    def upon_78():
        SFX_3('SE_BigBomb_Short')

@State
def AllRangeShotEff1():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(580)
                GFX_0('AllRangeShotEff1', 100)
            if (SLOT_48 == 1101):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_00', 5)	# 21-25
    sprite('Action_235_01', 5)	# 26-30
    sprite('Action_235_02', 32767)	# 31-32797
    label(580)
    sprite('Action_235_03', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_04', 5)	# 32803-32807
    sprite('Action_235_05', 5)	# 32808-32812
    sprite('Action_235_06', 5)	# 32813-32817
    sprite('Action_235_07', 5)	# 32818-32822

@State
def AllRangeShotEff2():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1002):
                sendToLabel(580)
                GFX_0('AllRangeShotEff2', 100)
            if (SLOT_48 == 1102):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_09', 5)	# 21-25
    sprite('Action_235_10', 5)	# 26-30
    sprite('Action_235_11', 32767)	# 31-32797
    label(580)
    sprite('Action_235_12', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_13', 5)	# 32803-32807
    sprite('Action_235_14', 5)	# 32808-32812
    sprite('Action_235_15', 5)	# 32813-32817
    sprite('Action_235_16', 5)	# 32818-32822

@State
def AllRangeShotEff3():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(580)
                GFX_0('AllRangeShotEff3', 100)
            if (SLOT_48 == 1103):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_18', 5)	# 21-25
    sprite('Action_235_19', 5)	# 26-30
    sprite('Action_235_20', 32767)	# 31-32797
    label(580)
    sprite('Action_235_21', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_22', 5)	# 32803-32807
    sprite('Action_235_23', 5)	# 32808-32812
    sprite('Action_235_24', 5)	# 32813-32817
    sprite('Action_235_25', 5)	# 32818-32822

@State
def AllRangeShotEff4():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1004):
                sendToLabel(580)
                GFX_0('AllRangeShotEff4', 100)
            if (SLOT_48 == 1104):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_27', 5)	# 21-25
    sprite('Action_235_28', 5)	# 26-30
    sprite('Action_235_29', 32767)	# 31-32797
    label(580)
    sprite('Action_235_30', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_31', 5)	# 32803-32807
    sprite('Action_235_32', 5)	# 32808-32812
    sprite('Action_235_33', 5)	# 32813-32817
    sprite('Action_235_34', 5)	# 32818-32822

@State
def AllRangeShotEff5():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1005):
                sendToLabel(580)
                GFX_0('AllRangeShotEff5', 100)
            if (SLOT_48 == 1105):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_36', 5)	# 21-25
    sprite('Action_235_37', 5)	# 26-30
    sprite('Action_235_38', 32767)	# 31-32797
    label(580)
    sprite('Action_235_39', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_40', 5)	# 32803-32807
    sprite('Action_235_41', 5)	# 32808-32812
    sprite('Action_235_42', 5)	# 32813-32817
    sprite('Action_235_43', 5)	# 32818-32822

@State
def AllRangeShotEff6():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1006):
                sendToLabel(580)
                GFX_0('AllRangeShotEff6', 100)
            if (SLOT_48 == 1106):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_45', 5)	# 21-25
    sprite('Action_235_46', 5)	# 26-30
    sprite('Action_235_47', 32767)	# 31-32797
    label(580)
    sprite('Action_235_48', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_49', 5)	# 32803-32807
    sprite('Action_235_50', 5)	# 32808-32812
    sprite('Action_235_51', 5)	# 32813-32817
    sprite('Action_235_52', 5)	# 32818-32822

@State
def AllRangeShotEff7():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1007):
                sendToLabel(580)
                GFX_0('AllRangeShotEff7', 100)
            if (SLOT_48 == 1107):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_54', 5)	# 21-25
    sprite('Action_235_55', 5)	# 26-30
    sprite('Action_235_56', 32767)	# 31-32797
    label(580)
    sprite('Action_235_57', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_58', 5)	# 32803-32807
    sprite('Action_235_59', 5)	# 32808-32812
    sprite('Action_235_60', 5)	# 32813-32817
    sprite('Action_235_61', 5)	# 32818-32822

@State
def AllRangeShotEff8():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1008):
                sendToLabel(580)
                GFX_0('AllRangeShotEff8', 100)
            if (SLOT_48 == 1108):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_63', 5)	# 21-25
    sprite('Action_235_64', 5)	# 26-30
    sprite('Action_235_65', 32767)	# 31-32797
    label(580)
    sprite('Action_235_66', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_67', 5)	# 32803-32807
    sprite('Action_235_68', 5)	# 32808-32812
    sprite('Action_235_69', 5)	# 32813-32817
    sprite('Action_235_70', 5)	# 32818-32822

@State
def AllRangeShotEff9():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1009):
                sendToLabel(580)
                GFX_0('AllRangeShotEff9', 100)
            if (SLOT_48 == 1109):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_72', 5)	# 21-25
    sprite('Action_235_73', 5)	# 26-30
    sprite('Action_235_74', 32767)	# 31-32797
    label(580)
    sprite('Action_235_75', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_76', 5)	# 32803-32807
    sprite('Action_235_77', 5)	# 32808-32812
    sprite('Action_235_78', 5)	# 32813-32817
    sprite('Action_235_79', 5)	# 32818-32822

@State
def AllRangeShotEff10():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1010):
                sendToLabel(580)
                GFX_0('AllRangeShotEff10', 100)
            if (SLOT_48 == 1110):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_81', 5)	# 21-25
    sprite('Action_235_82', 5)	# 26-30
    sprite('Action_235_83', 32767)	# 31-32797
    label(580)
    sprite('Action_235_84', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_85', 5)	# 32803-32807
    sprite('Action_235_86', 5)	# 32808-32812
    sprite('Action_235_87', 5)	# 32813-32817
    sprite('Action_235_88', 5)	# 32818-32822

@State
def AllRangeShotEff11():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1011):
                sendToLabel(580)
                GFX_0('AllRangeShotEff11', 100)
            if (SLOT_48 == 1111):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_90', 5)	# 21-25
    sprite('Action_235_91', 5)	# 26-30
    sprite('Action_235_92', 32767)	# 31-32797
    label(580)
    sprite('Action_235_93', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_94', 5)	# 32803-32807
    sprite('Action_235_95', 5)	# 32808-32812
    sprite('Action_235_96', 5)	# 32813-32817
    sprite('Action_235_97', 5)	# 32818-32822

@State
def AllRangeShotEff12():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1012):
                sendToLabel(580)
                GFX_0('AllRangeShotEff12', 100)
            if (SLOT_48 == 1112):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_108', 5)	# 21-25
    sprite('Action_235_109', 5)	# 26-30
    sprite('Action_235_110', 32767)	# 31-32797
    label(580)
    sprite('Action_235_111', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_112', 5)	# 32803-32807
    sprite('Action_235_113', 5)	# 32808-32812
    sprite('Action_235_114', 5)	# 32813-32817
    sprite('Action_235_115', 5)	# 32818-32822

@State
def AllRangeShotEff13():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1013):
                sendToLabel(580)
                GFX_0('AllRangeShotEff13', 100)
            if (SLOT_48 == 1113):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_117', 5)	# 21-25
    sprite('Action_235_118', 5)	# 26-30
    sprite('Action_235_119', 32767)	# 31-32797
    label(580)
    sprite('Action_235_120', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_121', 5)	# 32803-32807
    sprite('Action_235_122', 5)	# 32808-32812
    sprite('Action_235_123', 5)	# 32813-32817
    sprite('Action_235_124', 5)	# 32818-32822

@State
def AllRangeShotEff14():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1014):
                sendToLabel(580)
                GFX_0('AllRangeShotEff14', 100)
            if (SLOT_48 == 1114):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_126', 5)	# 21-25
    sprite('Action_235_127', 5)	# 26-30
    sprite('Action_235_128', 32767)	# 31-32797
    label(580)
    sprite('Action_235_129', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_130', 5)	# 32803-32807
    sprite('Action_235_131', 5)	# 32808-32812
    sprite('Action_235_132', 5)	# 32813-32817
    sprite('Action_235_133', 5)	# 32818-32822

@State
def AllRangeShotEff15():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1015):
                sendToLabel(580)
                GFX_0('AllRangeShotEff15', 100)
            if (SLOT_48 == 1115):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_135', 5)	# 21-25
    sprite('Action_235_136', 5)	# 26-30
    sprite('Action_235_137', 32767)	# 31-32797
    label(580)
    sprite('Action_235_138', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_139', 5)	# 32803-32807
    sprite('Action_235_140', 5)	# 32808-32812
    sprite('Action_235_141', 5)	# 32813-32817
    sprite('Action_235_142', 5)	# 32818-32822

@State
def AllRangeShotEff16():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1016):
                sendToLabel(580)
                GFX_0('AllRangeShotEff16', 100)
            if (SLOT_48 == 1116):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_144', 5)	# 21-25
    sprite('Action_235_145', 5)	# 26-30
    sprite('Action_235_146', 32767)	# 31-32797
    label(580)
    sprite('Action_235_147', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_148', 5)	# 32803-32807
    sprite('Action_235_149', 5)	# 32808-32812
    sprite('Action_235_150', 5)	# 32813-32817
    sprite('Action_235_151', 5)	# 32818-32822

@State
def AllRangeShotEff17():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 1017):
                sendToLabel(580)
                GFX_0('AllRangeShotEff17', 100)
            if (SLOT_48 == 1117):
                sendToLabel(580)
    sprite('null', 20)	# 1-20
    sprite('Action_235_153', 5)	# 21-25
    sprite('Action_235_154', 5)	# 26-30
    sprite('Action_235_155', 32767)	# 31-32797
    label(580)
    sprite('Action_235_156', 5)	# 32798-32802
    Unknown2019(-500)
    sprite('Action_235_157', 5)	# 32803-32807
    sprite('Action_235_158', 5)	# 32808-32812
    sprite('Action_235_159', 5)	# 32813-32817
    sprite('Action_235_160', 5)	# 32818-32822

@State
def UltimateHole_Atk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown11063(1)
        Unknown11066(1)
        AttackLevel_(0)
        Damage(0)
        Unknown11064(1)
        AttackP1(80)
        AttackP2(60)
        PushbackX(0)
        Hitstop(5)
        hitstun(240)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown4009(3)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown2019(-1000)
        Unknown30048(1)
        Unknown11064(1)
        HitOverhead(2)
        HitLow(2)
        Unknown11045(1)
        Unknown11082(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11072(1, 0, 0)
        Unknown11084(1)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown11069('UltimateHole_HoldAtkEff')

        def upon_78():
            SLOT_51 = 1
            SFX_3('SE_ApperLightBlade')
            Unknown23029(3, 1201, 0)

        def upon_CLEAR_OR_EXIT():
            Unknown48('19000000020000003400000016000000020000001e000000')
            if SLOT_52:
                Unknown11045(0)
            else:
                Unknown11045(1)
    sprite('Action_107_00', 5)	# 1-5
    sprite('Action_107_01', 5)	# 6-10
    sprite('Action_107_02', 5)	# 11-15
    sprite('Action_107_03', 5)	# 16-20
    sprite('Action_107_04ex01', 5)	# 21-25	 **attackbox here**
    sprite('Action_107_05ex01', 5)	# 26-30	 **attackbox here**
    sprite('Action_107_06ex01', 5)	# 31-35	 **attackbox here**
    sprite('Action_107_07ex01', 5)	# 36-40	 **attackbox here**
    sprite('Action_107_08ex01', 5)	# 41-45	 **attackbox here**
    sprite('Action_107_09', 9)	# 46-54	 **attackbox here**
    if SLOT_51:
        sendToLabel(10)
    else:
        Unknown23029(3, 1202, 0)
    sprite('Action_107_10', 9)	# 55-63	 **attackbox here**
    sprite('Action_107_11', 9)	# 64-72	 **attackbox here**
    sprite('Action_107_12', 9)	# 73-81
    sprite('Action_107_13', 9)	# 82-90
    sprite('Action_107_14', 1)	# 91-91
    ExitState()
    label(10)
    sprite('Action_107_08', 5)	# 92-96	 **attackbox here**
    sprite('Action_107_09', 10)	# 97-106	 **attackbox here**
    sprite('Action_107_10', 10)	# 107-116	 **attackbox here**
    GFX_0('UltimateBlackHoleLoop', 100)
    Unknown38(5, 1)
    sprite('Action_107_11', 9)	# 117-125	 **attackbox here**
    sprite('Action_107_12', 72)	# 126-197
    sprite('Action_107_13', 20)	# 198-217
    sprite('Action_107_14', 60)	# 218-277
    sprite('Action_107_14', 1)	# 278-278
    Unknown13(5)

@State
def UltimateHole_AtkOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown11063(1)
        Unknown11066(1)
        AttackLevel_(0)
        Damage(0)
        Unknown11064(1)
        AttackP1(80)
        AttackP2(60)
        PushbackX(0)
        Hitstop(5)
        hitstun(240)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown4009(3)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown2019(-1000)
        Unknown30048(1)
        Unknown11064(1)
        HitOverhead(2)
        HitLow(2)
        Unknown11045(1)
        Unknown11082(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11072(1, 0, 0)
        Unknown11084(1)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown11069('UltimateHoleOD_LowShotAtk')

        def upon_78():
            SLOT_51 = 1
            SFX_3('SE_ApperLightBlade')
            Unknown23029(3, 1201, 0)

        def upon_CLEAR_OR_EXIT():
            Unknown48('19000000020000003400000016000000020000001e000000')
            if SLOT_52:
                Unknown11045(0)
            else:
                Unknown11045(1)
    sprite('Action_107_00', 5)	# 1-5
    sprite('Action_107_01', 5)	# 6-10
    sprite('Action_107_02', 5)	# 11-15
    sprite('Action_107_03', 5)	# 16-20
    sprite('Action_107_04ex01', 5)	# 21-25	 **attackbox here**
    sprite('Action_107_05ex01', 5)	# 26-30	 **attackbox here**
    sprite('Action_107_06ex01', 5)	# 31-35	 **attackbox here**
    sprite('Action_107_07ex01', 5)	# 36-40	 **attackbox here**
    sprite('Action_107_08ex01', 5)	# 41-45	 **attackbox here**
    sprite('Action_107_09', 9)	# 46-54	 **attackbox here**
    if SLOT_51:
        sendToLabel(10)
    else:
        Unknown23029(3, 1202, 0)
    sprite('Action_107_10', 9)	# 55-63	 **attackbox here**
    sprite('Action_107_11', 9)	# 64-72	 **attackbox here**
    sprite('Action_107_12', 9)	# 73-81
    sprite('Action_107_13', 9)	# 82-90
    sprite('Action_107_14', 1)	# 91-91
    ExitState()
    label(10)
    sprite('Action_107_08', 5)	# 92-96	 **attackbox here**
    sprite('Action_107_09', 10)	# 97-106	 **attackbox here**
    sprite('Action_107_10', 10)	# 107-116	 **attackbox here**
    GFX_0('UltimateBlackHoleLoop', 100)
    Unknown38(5, 1)
    sprite('Action_107_11', 9)	# 117-125	 **attackbox here**
    sprite('Action_107_12', 102)	# 126-227
    sprite('Action_107_13', 50)	# 228-277
    sprite('Action_107_14', 90)	# 278-367
    sprite('Action_107_14', 1)	# 368-368
    Unknown13(5)

@State
def UltimateHole_HoldAtkEff():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4010(2)
        AttackLevel_(4)
        Damage(1303)
        MinimumDamagePct(5)
        Unknown11064(1)
        AttackP1(48)
        AttackP2(100)
        PushbackX(0)
        hitstun(120)
        Unknown9310(1)
        Hitstop(3)
        Unknown9016(1)
        Unknown2053(1)
        Unknown2034(1)
        Unknown23013(1)
        Unknown1096(1200)
        Unknown1086(22)
        Unknown1007(800000)
        Unknown11069('UltimateHole_HoldAtkEff')
        sendToLabelUpon(2, 1)
        loopRelated(17, 600)

        def upon_17():
            sendToLabel(580)
    sprite('Action_435_03', 2)	# 1-2
    SFX_3('SE_Hari_Appear')
    sprite('Action_435_04', 3)	# 3-5	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(-100000)
    sprite('Action_435_05', 3)	# 6-8	 **attackbox here**
    sprite('Action_435_06', 3)	# 9-11	 **attackbox here**
    label(0)
    sprite('Action_435_07', 3)	# 12-14	 **attackbox here**
    sprite('Action_435_08', 3)	# 15-17	 **attackbox here**
    sprite('Action_435_09', 3)	# 18-20	 **attackbox here**
    sprite('Action_435_10', 3)	# 21-23	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_435_11ex01', 1)	# 24-24	 **attackbox here**
    GFX_0('EffDropShot_Landing', 100)
    sprite('Action_435_11', 1)	# 25-25	 **attackbox here**
    sprite('Action_435_12', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    Damage(0)
    Unknown9130(240)
    Unknown9142(240)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Hitstop(0)
    Unknown30048(1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('UltimateBlackHoleSwordAtk')
    sprite('Action_435_13', 3)	# 29-31	 **attackbox here**
    sprite('Action_435_14', 3)	# 32-34	 **attackbox here**
    sprite('Action_435_15', 3)	# 35-37	 **attackbox here**
    sprite('Action_435_16', 3)	# 38-40	 **attackbox here**
    label(10)
    sprite('Action_435_17', 3)	# 41-43	 **attackbox here**
    sprite('Action_435_18', 3)	# 44-46	 **attackbox here**
    sprite('Action_435_19', 3)	# 47-49	 **attackbox here**
    sprite('Action_435_20', 3)	# 50-52	 **attackbox here**
    gotoLabel(10)
    label(580)
    sprite('Action_435_21', 3)	# 53-55	 **attackbox here**
    sprite('Action_435_22', 3)	# 56-58	 **attackbox here**
    sprite('Action_435_23', 3)	# 59-61	 **attackbox here**
    sprite('Action_435_24', 3)	# 62-64	 **attackbox here**
    sprite('Action_435_25', 3)	# 65-67	 **attackbox here**

@State
def UltimateHoleOD_LowShotAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(3909)
        MinimumDamagePct(9)
        Unknown11064(1)
        AttackP1(48)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(5000)
        YImpluseBeforeWallbounce(500)
        AirUntechableTime(600)
        Hitstop(15)
        Unknown9310(1000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown2019(-500)
        Unknown11072(1, 0, 450000)
        Unknown30048(1)
        Unknown11069('UltimateBlackHoleSwordAtk')
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('Action_417_00', 1)	# 1-1
    sprite('Action_417_01', 2)	# 2-3
    sprite('Action_417_02', 2)	# 4-5
    sprite('Action_417_03', 2)	# 6-7
    SFX_3('SE_Hari_Appear')
    sprite('Action_417_04', 3)	# 8-10	 **attackbox here**
    SFX_3('SE207_BladeFinish')
    sprite('Action_417_05', 3)	# 11-13	 **attackbox here**
    sprite('Action_417_06', 4)	# 14-17	 **attackbox here**
    sprite('Action_417_07', 4)	# 18-21	 **attackbox here**
    sprite('Action_417_08', 4)	# 22-25	 **attackbox here**
    sprite('Action_417_09', 4)	# 26-29	 **attackbox here**
    sprite('Action_417_10', 4)	# 30-33	 **attackbox here**
    sprite('Action_417_11', 4)	# 34-37	 **attackbox here**
    sprite('Action_417_12', 4)	# 38-41	 **attackbox here**
    SFX_3('SE_Hari_Vanish')
    sprite('Action_417_13', 4)	# 42-45	 **attackbox here**
    sprite('Action_417_14', 4)	# 46-49	 **attackbox here**
    sprite('Action_417_15', 4)	# 50-53	 **attackbox here**
    sprite('Action_417_16', 4)	# 54-57	 **attackbox here**
    sprite('Action_417_17', 4)	# 58-61	 **attackbox here**

@State
def UltimateHoleCharge():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown2019(-1000)
        Unknown1096(3000)
        Unknown1086(22)
        teleportRelativeX(-900000)
        Unknown1007(1500000)
    sprite('null', 20)	# 1-20
    sprite('Action_450_00', 5)	# 21-25
    sprite('Action_450_01', 5)	# 26-30
    sprite('Action_450_02', 5)	# 31-35
    sprite('Action_450_03', 5)	# 36-40
    sprite('Action_450_04', 5)	# 41-45
    sprite('Action_450_05', 5)	# 46-50
    sprite('Action_450_06', 5)	# 51-55
    sprite('Action_450_03', 5)	# 56-60
    sprite('Action_450_04', 5)	# 61-65
    sprite('Action_450_05', 5)	# 66-70
    SFX_3('SE_DrawnSword')
    sprite('Action_450_06', 5)	# 71-75
    sprite('Action_450_03', 5)	# 76-80
    GFX_0('UltimateBlackHoleSwordAtk', 100)
    SFX_3('SE_DrawnSword')
    Unknown2038(-1)
    sprite('Action_450_04', 5)	# 81-85
    sprite('Action_450_05', 5)	# 86-90
    sprite('Action_450_06', 5)	# 91-95
    sprite('Action_450_03', 5)	# 96-100
    sprite('Action_450_04', 5)	# 101-105
    sprite('Action_450_05', 5)	# 106-110
    sprite('Action_450_06', 5)	# 111-115
    sprite('Action_450_03', 5)	# 116-120
    sprite('Action_450_04', 5)	# 121-125
    sprite('Action_450_05', 5)	# 126-130
    sprite('Action_450_06', 5)	# 131-135
    sprite('Action_450_03', 5)	# 136-140
    sprite('Action_450_04', 5)	# 141-145
    sprite('Action_450_05', 5)	# 146-150
    sprite('Action_450_06', 5)	# 151-155
    sprite('Action_450_03', 5)	# 156-160
    sprite('Action_450_04', 5)	# 161-165
    sprite('Action_450_05', 5)	# 166-170
    sprite('Action_450_06', 5)	# 171-175
    sprite('Action_450_03', 5)	# 176-180
    sprite('Action_450_04', 5)	# 181-185
    sprite('Action_450_05', 5)	# 186-190
    sprite('Action_450_06', 5)	# 191-195
    label(1)
    sprite('Action_450_07', 5)	# 196-200
    sprite('Action_450_08', 5)	# 201-205
    sprite('Action_450_09', 2)	# 206-207

@State
def UltimateBlackHoleSwordAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown2019(-1001)
        AttackLevel_(5)
        Damage(9636)
        MinimumDamagePct(16)
        AttackP1(48)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(1500)
        Unknown9310(20)
        Hitstop(0)
        AirUntechableTime(600)
        Unknown11023(1)
        Unknown30048(1)
        DisableAttackRestOfMove()
        Unknown1096(5000)
        Unknown9016(1)
        Unknown11057(4000)

        def upon_78():
            SFX_3('SE_BigBomb_Short')
    sprite('Action_457_00', 6)	# 1-6
    ScreenShake(15000, 5000)
    teleportRelativeX(20000)
    Unknown1007(-150000)
    sprite('Action_457_01', 6)	# 7-12
    sprite('Action_457_02', 6)	# 13-18
    sprite('Action_457_03', 4)	# 19-22
    physicsXImpulse(2000)
    physicsYImpulse(-3000)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(110)
        YAccel(110)
    sendToLabelUpon(2, 1)
    sprite('Action_457_04', 3)	# 23-25	 **attackbox here**
    sprite('Action_457_05', 3)	# 26-28	 **attackbox here**
    sprite('Action_457_04', 3)	# 29-31	 **attackbox here**
    sprite('Action_457_05', 3)	# 32-34	 **attackbox here**
    sprite('Action_457_04', 3)	# 35-37	 **attackbox here**
    sprite('Action_457_05', 3)	# 38-40	 **attackbox here**
    sprite('Action_457_04', 3)	# 41-43	 **attackbox here**
    sprite('Action_457_05', 3)	# 44-46	 **attackbox here**
    sprite('Action_457_04', 3)	# 47-49	 **attackbox here**
    sprite('Action_457_05', 3)	# 50-52	 **attackbox here**
    sprite('Action_457_04', 3)	# 53-55	 **attackbox here**
    RefreshMultihit()
    label(0)
    sprite('Action_457_05', 3)	# 56-58	 **attackbox here**
    sprite('Action_457_04', 3)	# 59-61	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_457_07', 3)	# 62-64	 **attackbox here**
    teleportRelativeX(-50000)
    Unknown1084(1)
    clearUponHandler(3)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    Unknown23015(1)
    Unknown1096(2500)
    Unknown35()
    Unknown4004('6566666563745f33383200000000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    Unknown23015(1)
    Unknown1096(2500)
    Unknown35()
    sprite('Action_457_08', 3)	# 65-67
    sprite('Action_457_09', 3)	# 68-70
    sprite('Action_457_10', 3)	# 71-73
    sprite('Action_457_11', 3)	# 74-76
    sprite('Action_457_12', 3)	# 77-79
    sprite('Action_457_13', 3)	# 80-82
    sprite('Action_457_14', 3)	# 83-85
    sprite('Action_457_15', 1)	# 86-86

@State
def UltimateBlackHoleLoop():

    def upon_IMMEDIATE():
        Unknown4019(2)
        Unknown2019(-1000)
        Unknown1007(-50000)
        Unknown1096(1800)
        loopRelated(17, 600)

        def upon_17():
            Unknown13(25)
    label(0)
    sprite('Action_417_07ex01', 10)	# 1-10
    sprite('Action_417_08ex01', 10)	# 11-20
    sprite('Action_417_09ex01', 10)	# 21-30
    gotoLabel(0)
    label(580)
    sprite('Action_417_15ex01', 4)	# 31-34
    sprite('Action_417_16ex01', 4)	# 35-38	 **attackbox here**
    sprite('Action_417_17ex01', 1)	# 39-39	 **attackbox here**

@State
def UltimateHoleCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown20003(1)

        def upon_43():
            if (SLOT_48 == 1203):
                sendToLabel(0)
        loopRelated(17, 600)

        def upon_17():
            Unknown13(25)
    sprite('null', 40)	# 1-40
    sprite('null', 32767)	# 41-32807
    Unknown20000(1)
    Unknown1086(22)
    teleportRelativeY(750000)
    SLOT_105 = 2500
    label(0)
    sprite('null', 30)	# 32808-32837
    Unknown20000(0)
    Unknown20001(1)

@Subroutine
def UltimateStormAtkParam():
    Unknown2011()
    Unknown23056('')
    AttackLevel_(4)
    Damage(440)
    AttackP1(60)
    AttackP2(80)
    Unknown11092(1)
    blockstun(20)
    hitstun(23)
    AirUntechableTime(23)
    Hitstop(2)
    AirPushbackX(6000)
    AirPushbackY(11000)
    Unknown11110(66)
    MinimumDamagePct(18)
    PushbackX(6600)
    Unknown9016(1)
    Unknown11057(500)
    Unknown23013(1)
    Unknown23182(2)
    Unknown30070('556c74696d61746553746f726d41746b00000000000000000000000000000000')

    def upon_44():
        DisableAttackRestOfMove()
        Unknown2003(1)

    def upon_53():
        Unknown13(25)

    def upon_43():
        if (SLOT_48 == 1301):
            Unknown30070('556c74696d61746553746f726d41746b4f440000000000000000000000000000')
            Damage(460)
            MinimumDamagePct(19)

@State
def UltimateStormCharge():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4009(3)
        Unknown2019(1000)
        Unknown1007(600000)
        teleportRelativeX(-200000)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 1)

        def upon_53():
            Unknown23090(25)
    sprite('Action_450_00', 5)	# 1-5
    sprite('Action_450_01', 5)	# 6-10
    sprite('Action_450_02', 5)	# 11-15
    Unknown2037(6)
    GFX_0('UltimateStormAtkMatome', 100)
    label(0)
    sprite('Action_450_03', 5)	# 16-20
    Unknown2038(-1)
    sprite('Action_450_04', 5)	# 21-25
    sprite('Action_450_05', 5)	# 26-30
    sprite('Action_450_06', 5)	# 31-35
    if SLOT_2:
        _gotolabel(0)
    label(1)
    sprite('Action_450_07', 5)	# 36-40
    sprite('Action_450_08', 5)	# 41-45
    sprite('Action_450_09', 2)	# 46-47

@State
def UltimateStormAtkMatome():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4011(3)
        teleportRelativeX(100000)
        Unknown1007(-80000)
        AttackP1(60)
        AttackP2(80)
        Unknown11092(1)

        def upon_53():
            Unknown13(25)
    sprite('null', 1)	# 1-1
    Unknown2037(4)
    label(0)
    sprite('null', 8)	# 2-9
    SFX_3('SE_DrawnSword')
    sprite('null', 2)	# 10-11
    GFX_0('UltimateStormAtk1', 100)
    sprite('null', 2)	# 12-13
    GFX_0('UltimateStormAtk2', 100)
    sprite('null', 2)	# 14-15
    GFX_0('UltimateStormAtk3', 100)
    sprite('null', 2)	# 16-17
    GFX_0('UltimateStormAtk4', 100)
    sprite('null', 2)	# 18-19
    GFX_0('UltimateStormAtk5', 100)
    sprite('null', 2)	# 20-21
    GFX_0('UltimateStormAtk6', 100)
    sprite('null', 2)	# 22-23
    GFX_0('UltimateStormAtk7', 100)
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(0)
    sprite('null', 1)	# 24-24
    SFX_3('SE_DrawnSword')

@State
def UltimateStormChargeOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4009(3)
        Unknown2019(1000)
        Unknown1007(600000)
        teleportRelativeX(-200000)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 1)

        def upon_53():
            Unknown23090(25)
    sprite('Action_450_00', 5)	# 1-5
    sprite('Action_450_01', 5)	# 6-10
    sprite('Action_450_02', 5)	# 11-15
    Unknown2037(6)
    GFX_0('UltimateStormAtkMatomeOD', 100)
    label(0)
    sprite('Action_450_03', 5)	# 16-20
    Unknown2038(-1)
    sprite('Action_450_04', 5)	# 21-25
    sprite('Action_450_05', 5)	# 26-30
    sprite('Action_450_06', 5)	# 31-35
    if SLOT_2:
        _gotolabel(0)
    label(1)
    sprite('Action_450_07', 5)	# 36-40
    sprite('Action_450_08', 5)	# 41-45
    sprite('Action_450_09', 2)	# 46-47

@State
def UltimateStormAtkMatomeOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4011(3)
        teleportRelativeX(100000)
        Unknown1007(-80000)
        AttackP1(60)
        AttackP2(80)
        Unknown11092(1)

        def upon_53():
            Unknown13(25)
    sprite('null', 1)	# 1-1
    Unknown2037(5)
    label(0)
    sprite('null', 8)	# 2-9
    SFX_3('SE_DrawnSword')
    sprite('null', 2)	# 10-11
    GFX_0('UltimateStormAtk1', 100)
    Unknown23029(1, 1301, 0)
    sprite('null', 2)	# 12-13
    GFX_0('UltimateStormAtk2', 100)
    Unknown23029(1, 1301, 0)
    sprite('null', 2)	# 14-15
    GFX_0('UltimateStormAtk3', 100)
    Unknown23029(1, 1301, 0)
    sprite('null', 2)	# 16-17
    GFX_0('UltimateStormAtk4', 100)
    Unknown23029(1, 1301, 0)
    sprite('null', 2)	# 18-19
    GFX_0('UltimateStormAtk5', 100)
    Unknown23029(1, 1301, 0)
    sprite('null', 2)	# 20-21
    GFX_0('UltimateStormAtk6', 100)
    Unknown23029(1, 1301, 0)
    sprite('null', 2)	# 22-23
    GFX_0('UltimateStormAtk7', 100)
    Unknown23029(1, 1301, 0)
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(0)
    sprite('null', 1)	# 24-24
    SFX_3('SE_DrawnSword')

@State
def UltimateStormAtk1():

    def upon_IMMEDIATE():
        callSubroutine('UltimateStormAtkParam')
    sprite('Action_451_00', 3)	# 1-3
    sprite('Action_451_01', 3)	# 4-6
    sprite('Action_451_02', 3)	# 7-9
    sprite('Action_451_03', 3)	# 10-12
    sprite('Action_451_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(100000)
    physicsYImpulse(-112000)
    sendToLabelUpon(2, 1)
    sprite('Action_451_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_451_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_451_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_451_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_451_08', 3)	# 28-30
    sprite('Action_451_09', 3)	# 31-33
    sprite('Action_451_10', 3)	# 34-36
    sprite('Action_451_11', 3)	# 37-39
    sprite('Action_451_12', 3)	# 40-42
    sprite('Action_451_13', 3)	# 43-45
    sprite('Action_451_14', 3)	# 46-48
    sprite('Action_451_15', 1)	# 49-49

@State
def UltimateStormAtk2():

    def upon_IMMEDIATE():
        callSubroutine('UltimateStormAtkParam')
    sprite('Action_452_00', 3)	# 1-3
    teleportRelativeX(240000)
    sprite('Action_452_01', 3)	# 4-6
    sprite('Action_452_02', 3)	# 7-9
    sprite('Action_452_03', 3)	# 10-12
    sprite('Action_452_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(192000)
    physicsYImpulse(-88000)
    sendToLabelUpon(2, 1)
    sprite('Action_452_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_452_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_452_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_452_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_452_08', 3)	# 28-30
    sprite('Action_452_09', 3)	# 31-33
    sprite('Action_452_10', 3)	# 34-36
    sprite('Action_452_11', 3)	# 37-39
    sprite('Action_452_12', 3)	# 40-42
    sprite('Action_452_13', 3)	# 43-45
    sprite('Action_452_14', 3)	# 46-48
    sprite('Action_452_15', 1)	# 49-49

@State
def UltimateStormAtk3():

    def upon_IMMEDIATE():
        callSubroutine('UltimateStormAtkParam')
    sprite('Action_453_00', 3)	# 1-3
    teleportRelativeX(-90000)
    sprite('Action_453_01', 3)	# 4-6
    sprite('Action_453_02', 3)	# 7-9
    sprite('Action_453_03', 3)	# 10-12
    sprite('Action_453_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(72000)
    physicsYImpulse(-120000)
    sendToLabelUpon(2, 1)
    sprite('Action_453_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_453_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_453_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_453_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_453_08', 3)	# 28-30
    sprite('Action_453_09', 3)	# 31-33
    sprite('Action_453_10', 3)	# 34-36
    sprite('Action_453_11', 3)	# 37-39
    sprite('Action_453_12', 3)	# 40-42
    sprite('Action_453_13', 3)	# 43-45
    sprite('Action_453_14', 3)	# 46-48
    sprite('Action_453_15', 1)	# 49-49

@State
def UltimateStormAtk4():

    def upon_IMMEDIATE():
        callSubroutine('UltimateStormAtkParam')
    sprite('Action_454_00', 3)	# 1-3
    teleportRelativeX(150000)
    Unknown1007(125000)
    sprite('Action_454_01', 3)	# 4-6
    sprite('Action_454_02', 3)	# 7-9
    sprite('Action_454_03', 3)	# 10-12
    sprite('Action_454_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(120000)
    physicsYImpulse(-100000)
    sendToLabelUpon(2, 1)
    sprite('Action_454_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_454_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_454_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_454_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_454_08', 3)	# 28-30
    sprite('Action_454_09', 3)	# 31-33
    sprite('Action_454_10', 3)	# 34-36
    sprite('Action_454_11', 3)	# 37-39
    sprite('Action_454_12', 3)	# 40-42
    sprite('Action_454_13', 3)	# 43-45
    sprite('Action_454_14', 3)	# 46-48
    sprite('Action_454_15', 1)	# 49-49

@State
def UltimateStormAtk5():

    def upon_IMMEDIATE():
        callSubroutine('UltimateStormAtkParam')
    sprite('Action_455_00', 3)	# 1-3
    teleportRelativeX(-40000)
    sprite('Action_455_01', 3)	# 4-6
    sprite('Action_455_02', 3)	# 7-9
    sprite('Action_455_03', 3)	# 10-12
    sprite('Action_455_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(-8000)
    physicsYImpulse(-120000)
    sendToLabelUpon(2, 1)
    sprite('Action_455_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_455_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_455_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_455_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_455_08', 3)	# 28-30
    sprite('Action_455_09', 3)	# 31-33
    sprite('Action_455_10', 3)	# 34-36
    sprite('Action_455_11', 3)	# 37-39
    sprite('Action_455_12', 3)	# 40-42
    sprite('Action_455_13', 3)	# 43-45
    sprite('Action_455_14', 3)	# 46-48
    sprite('Action_455_15', 1)	# 49-49

@State
def UltimateStormAtk6():

    def upon_IMMEDIATE():
        callSubroutine('UltimateStormAtkParam')
    sprite('Action_456_00', 3)	# 1-3
    teleportRelativeX(-75000)
    sprite('Action_456_01', 3)	# 4-6
    sprite('Action_456_02', 3)	# 7-9
    sprite('Action_456_03', 3)	# 10-12
    sprite('Action_456_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(60000)
    physicsYImpulse(-120000)
    sendToLabelUpon(2, 1)
    sprite('Action_456_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_456_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_456_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_456_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_456_08', 3)	# 28-30
    sprite('Action_456_09', 3)	# 31-33
    sprite('Action_456_10', 3)	# 34-36
    sprite('Action_456_11', 3)	# 37-39
    sprite('Action_456_12', 3)	# 40-42
    sprite('Action_456_13', 3)	# 43-45
    sprite('Action_456_14', 3)	# 46-48
    sprite('Action_456_15', 1)	# 49-49

@State
def UltimateStormAtk7():

    def upon_IMMEDIATE():
        callSubroutine('UltimateStormAtkParam')
    sprite('Action_457_00', 3)	# 1-3
    teleportRelativeX(100000)
    sprite('Action_457_01', 3)	# 4-6
    sprite('Action_457_02', 3)	# 7-9
    sprite('Action_457_03', 3)	# 10-12
    sprite('Action_457_04', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(80000)
    physicsYImpulse(-120000)
    sendToLabelUpon(2, 1)
    sprite('Action_457_05', 3)	# 16-18	 **attackbox here**
    label(0)
    sprite('Action_457_04', 3)	# 19-21	 **attackbox here**
    sprite('Action_457_05', 3)	# 22-24	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_457_07', 3)	# 25-27	 **attackbox here**
    Unknown1084(1)
    sprite('Action_457_08', 3)	# 28-30
    sprite('Action_457_09', 3)	# 31-33
    sprite('Action_457_10', 3)	# 34-36
    sprite('Action_457_11', 3)	# 37-39
    sprite('Action_457_12', 3)	# 40-42
    sprite('Action_457_13', 3)	# 43-45
    sprite('Action_457_14', 3)	# 46-48
    sprite('Action_457_15', 1)	# 49-49

@State
def AstralShotAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(1000)
        Hitstop(5)
        PushbackX(3500)
        hitstun(999)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        MinimumDamagePct(100)
        Unknown11064(1)
        Unknown11056(2)
        Unknown11072(1, 0, 0)
        Unknown9016(1)
        Unknown4009(3)
        Unknown11086(1)
        Unknown1086(22)
        teleportRelativeY(0)

        def upon_78():
            Unknown2038(1)
            Unknown23029(3, 5001, 1)

        def upon_44():
            Unknown4009(0)
            Unknown2003(1)
    sprite('Action_390_00', 40)	# 1-40	 **attackbox here**
    sprite('Action_390_01', 3)	# 41-43	 **attackbox here**
    sprite('Action_390_02', 3)	# 44-46	 **attackbox here**
    sprite('Action_390_03', 3)	# 47-49	 **attackbox here**
    sprite('Action_390_04', 3)	# 50-52	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_390_05', 3)	# 53-55	 **attackbox here**
    RefreshMultihit()
    sprite('Action_390_06', 3)	# 56-58	 **attackbox here**
    RefreshMultihit()
    sprite('Action_390_07', 3)	# 59-61	 **attackbox here**
    RefreshMultihit()
    sprite('Action_390_08', 3)	# 62-64	 **attackbox here**
    RefreshMultihit()
    sprite('Action_390_09', 3)	# 65-67	 **attackbox here**
    RefreshMultihit()
    sprite('Action_390_10', 3)	# 68-70	 **attackbox here**
    sprite('Action_390_11', 3)	# 71-73	 **attackbox here**
    sprite('Action_390_12', 5)	# 74-78	 **attackbox here**
    if SLOT_2:
        Unknown36(22)
        Unknown3004(-6)
        Unknown3025(-16777216, 20)
        Unknown35()
    sprite('Action_390_13', 3)	# 79-81	 **attackbox here**
    Unknown19(0, 2, 2)
    sprite('Action_390_14', 3)	# 82-84	 **attackbox here**
    sprite('Action_390_15', 3)	# 85-87	 **attackbox here**
    sprite('Action_390_16', 3)	# 88-90	 **attackbox here**
    sprite('Action_390_17', 3)	# 91-93	 **attackbox here**
    sprite('Action_390_18', 3)	# 94-96	 **attackbox here**
    label(0)
    sprite('Action_390_19', 3)	# 97-99	 **attackbox here**
    sprite('Action_390_20', 3)	# 100-102	 **attackbox here**
    sprite('Action_390_21', 3)	# 103-105	 **attackbox here**
    sprite('Action_390_22', 3)	# 106-108	 **attackbox here**
    sprite('Action_390_23', 3)	# 109-111	 **attackbox here**
    sprite('Action_390_24', 3)	# 112-114	 **attackbox here**
    sprite('Action_390_25', 3)	# 115-117	 **attackbox here**
    sprite('Action_390_26', 1)	# 118-118	 **attackbox here**

@State
def AstralWarpOut():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown2019(-100)
    sprite('Action_385_00', 4)	# 1-4
    sprite('Action_385_01', 4)	# 5-8
    SFX_3('SE_SwingLightSword')
    sprite('Action_385_02', 4)	# 9-12
    sprite('Action_385_03', 4)	# 13-16
    sprite('Action_385_04', 1)	# 17-17

@State
def AstralCamera():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5004):
                Unknown20000(1)
                sendToLabel(0)
    sprite('null', 25)	# 1-25
    sprite('null', 10)	# 26-35
    Unknown2053(0)
    Unknown2034(0)
    EnableCollision(0)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown23057(50)
    teleportRelativeY(0)
    SLOT_105 = 1100
    SLOT_12 = SLOT_163
    Unknown1019(15)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(90)
    sprite('null', 5)	# 36-40
    clearUponHandler(3)
    Unknown1019(30)
    sprite('null', 5)	# 41-45
    Unknown1019(0)
    sprite('null', 5)	# 46-50
    physicsYImpulse(115000)
    sprite('null', 32767)	# 51-32817
    Unknown1019(0)
    YAccel(0)
    SLOT_105 = 1000
    label(0)
    sprite('null', 8)	# 32818-32825
    Unknown1084(1)
    setGravity(0)
    physicsYImpulse(137500)
    sprite('null', 32767)	# 32826-65592
    clearUponHandler(3)
    YAccel(0)
    setGravity(0)

@State
def AstralExeAura():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown2019(1000)
    label(0)
    sprite('Action_388_01', 5)	# 1-5
    sprite('Action_388_02', 5)	# 6-10
    sprite('Action_388_03', 5)	# 11-15
    gotoLabel(0)
    label(580)
    sprite('Action_388_04', 5)	# 16-20
    sprite('Action_388_05', 5)	# 21-25
    sprite('Action_388_06', 5)	# 26-30
    sprite('Action_388_07', 5)	# 31-35
    sprite('Action_388_08', 5)	# 36-40

@State
def AstralExeBlackOut():

    def upon_IMMEDIATE():
        Unknown2019(101)
        Unknown1007(250000)
    sprite('Action_383_00', 6)	# 1-6
    sprite('Action_383_01', 6)	# 7-12
    SFX_3('SE_ChargeUp')
    sprite('Action_383_02', 6)	# 13-18	 **attackbox here**
    sprite('Action_383_03', 6)	# 19-24	 **attackbox here**
    sprite('Action_383_04', 6)	# 25-30	 **attackbox here**
    sprite('Action_383_05', 6)	# 31-36	 **attackbox here**
    sprite('Action_383_06', 6)	# 37-42	 **attackbox here**
    SFX_3('SE_EarthQuake')
    sprite('Action_383_07', 5)	# 43-47	 **attackbox here**
    sprite('Action_383_08', 5)	# 48-52	 **attackbox here**
    sprite('Action_383_09', 5)	# 53-57	 **attackbox here**
    sprite('Action_383_10', 4)	# 58-61	 **attackbox here**
    sprite('Action_383_11', 4)	# 62-65
    sprite('Action_383_12', 40)	# 66-105
    sprite('Action_383_13', 30)	# 106-135
    Unknown23029(3, 5002, 1)
    sprite('Action_383_14', 12)	# 136-147
    sprite('Action_383_15', 27)	# 148-174
    GFX_0('AstralExeAtkFlashBG', 100)
    sprite('Action_383_16', 27)	# 175-201
    GFX_0('AstralExeAtkFlash', 100)
    sprite('Action_383_17', 18)	# 202-219
    sprite('Action_383_17', 18)	# 220-237
    SFX_1('uhi293')
    sprite('Action_383_18', 82)	# 238-319
    sprite('Action_383_19', 82)	# 320-401
    GFX_0('AstralWhiteOut', 100)
    sprite('Action_383_20', 3)	# 402-404
    sprite('Action_383_21', 2)	# 405-406	 **attackbox here**
    SFX_3('SE_EarthQuake')

@State
def AstralExeAtkFlash():

    def upon_IMMEDIATE():
        Unknown23015(1)
    sprite('Action_386_00', 6)	# 1-6
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_01', 5)	# 7-11
    sprite('null', 4)	# 12-15
    sprite('Action_386_03', 7)	# 16-22
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_04', 4)	# 23-26
    sprite('null', 4)	# 27-30
    sprite('Action_386_06', 6)	# 31-36
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_07', 3)	# 37-39
    sprite('null', 3)	# 40-42
    sprite('Action_386_09', 5)	# 43-47
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_10', 3)	# 48-50
    sprite('null', 3)	# 51-53
    sprite('Action_386_12', 5)	# 54-58
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_13', 3)	# 59-61
    sprite('null', 3)	# 62-64
    sprite('Action_386_15', 5)	# 65-69
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_16', 3)	# 70-72
    sprite('null', 3)	# 73-75
    sprite('Action_386_18', 5)	# 76-80
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_19', 3)	# 81-83
    sprite('null', 3)	# 84-86
    sprite('Action_386_21', 5)	# 87-91
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_22', 3)	# 92-94
    sprite('null', 3)	# 95-97
    sprite('Action_386_24', 5)	# 98-102
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_L')
    sprite('Action_386_25', 3)	# 103-105
    sprite('null', 3)	# 106-108
    sprite('Action_386_27', 5)	# 109-113
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_28', 2)	# 114-115
    sprite('null', 2)	# 116-117
    sprite('Action_386_30', 4)	# 118-121
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_31', 1)	# 122-122
    sprite('null', 1)	# 123-123
    sprite('Action_386_33', 4)	# 124-127
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_34', 2)	# 128-129
    sprite('null', 2)	# 130-131
    sprite('Action_386_36', 4)	# 132-135
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_37', 2)	# 136-137
    sprite('null', 2)	# 138-139
    sprite('Action_386_39', 4)	# 140-143
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_40', 2)	# 144-145
    sprite('null', 2)	# 146-147
    sprite('Action_386_42', 4)	# 148-151
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_43', 2)	# 152-153
    sprite('null', 2)	# 154-155
    sprite('Action_386_45', 4)	# 156-159
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_46', 2)	# 160-161
    sprite('null', 2)	# 162-163
    sprite('Action_386_48', 4)	# 164-167
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_49', 2)	# 168-169
    sprite('null', 1)	# 170-170
    sprite('Action_386_51', 3)	# 171-173
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_52', 1)	# 174-174
    sprite('null', 1)	# 175-175
    sprite('Action_386_54', 3)	# 176-178
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_M')
    sprite('Action_386_55', 1)	# 179-179
    sprite('null', 1)	# 180-180
    sprite('Action_386_57', 3)	# 181-183
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_S')
    sprite('Action_386_58', 1)	# 184-184
    sprite('null', 1)	# 185-185
    sprite('Action_386_60', 3)	# 186-188
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_S')
    sprite('Action_386_61', 1)	# 189-189
    sprite('null', 1)	# 190-190
    sprite('Action_386_63', 3)	# 191-193
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_S')
    sprite('Action_386_64', 1)	# 194-194
    sprite('null', 1)	# 195-195
    sprite('Action_386_66', 3)	# 196-198
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_S')
    sprite('Action_386_67', 1)	# 199-199
    sprite('null', 1)	# 200-200
    sprite('Action_386_69', 3)	# 201-203
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_S')
    sprite('Action_386_70', 1)	# 204-204
    sprite('null', 1)	# 205-205
    sprite('Action_386_72', 3)	# 206-208
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_S')
    sprite('Action_386_73', 1)	# 209-209
    sprite('null', 1)	# 210-210
    sprite('Action_386_75', 3)	# 211-213
    GFX_0('AstralExeAtkDmyCol', 100)
    sprite('Action_386_76', 1)	# 214-214
    sprite('null', 1)	# 215-215
    sprite('Action_386_78', 3)	# 216-218
    GFX_0('AstralExeAtkDmyCol', 100)
    SFX_3('SE202_BladeC_S')
    sprite('Action_386_79', 1)	# 219-219
    sprite('null', 1)	# 220-220
    sprite('Action_386_81', 3)	# 221-223
    GFX_0('AstralExeAtkDmyCol', 100)
    sprite('Action_386_82', 1)	# 224-224
    sprite('null', 1)	# 225-225
    sprite('Action_386_84', 1)	# 226-226
    GFX_0('AstralExeAtkDmyCol', 100)
    sprite('Action_386_85', 1)	# 227-227
    sprite('null', 1)	# 228-228
    sprite('Action_386_87', 1)	# 229-229
    GFX_0('AstralExeAtkDmyCol', 100)
    sprite('Action_386_88', 1)	# 230-230
    sprite('null', 1)	# 231-231
    sprite('Action_386_90', 1)	# 232-232
    GFX_0('AstralExeAtkDmyCol', 100)
    sprite('Action_386_91', 1)	# 233-233
    sprite('null', 1)	# 234-234
    sprite('Action_386_93', 1)	# 235-235
    GFX_0('AstralExeAtkDmyCol', 100)
    sprite('Action_386_94', 1)	# 236-236
    sprite('null', 1)	# 237-237
    sprite('Action_386_96', 1)	# 238-238
    GFX_0('AstralExeAtkFinishDmyCol', 100)
    sprite('Action_386_97', 1)	# 239-239

@State
def AstralExeAtkDmyCol():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(1000)
        Unknown11064(1)
        MinimumDamagePct(100)
        Hitstop(0)
        Unknown11001(0, 0, 0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        PushbackX(0)
        AirUntechableTime(999)
        hitstun(999)
        Unknown9016(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown23151(22, 103)
        Unknown11086(1)
    sprite('Action_386_atkcol', 5)	# 1-5

@State
def AstralExeAtkFinishDmyCol():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(62999)
        Unknown11064(3)
        MinimumDamagePct(100)
        Hitstop(0)
        Unknown11001(0, 0, 0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        PushbackX(0)
        AirUntechableTime(999)
        hitstun(999)
        Unknown9016(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown23151(22, 103)

        def upon_78():
            Unknown23029(3, 5003, 0)
            Unknown26('AstralExeAtkFlashBG')
            Unknown26('AstralExeAura')
            Unknown26('AstralCamera')
            Unknown36(22)
            Unknown3001(255)
            Unknown3004(0)
            Unknown35()
    sprite('Action_386_atkcol', 5)	# 1-5
    SFX_3('SE_BigBomb')

@State
def AstralExeAtkFlashBG():

    def upon_IMMEDIATE():
        Unknown2019(-100)
    sprite('Action_384_00', 32)	# 1-32
    sprite('Action_384_01', 32)	# 33-64
    label(0)
    sprite('Action_384_02', 32)	# 65-96
    sprite('Action_384_03', 32)	# 97-128
    sprite('Action_384_04', 32)	# 129-160
    gotoLabel(0)

@State
def AstralWhiteOut():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 80)	# 1-80
    Unknown3004(3)
    sprite('vr_white', 150)	# 81-230
    Unknown3001(255)
    Unknown3004(0)
    sprite('vr_white', 60)	# 231-290
    Unknown3004(-4)

@State
def AstralCutIn():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        Unknown23015(5)
        if SLOT_38:
            Unknown1000(-640000)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('null', 2)	# 1-2
    sprite('Action_999_01', 3)	# 3-5
    sprite('Action_999_02', 3)	# 6-8
    sprite('Action_999_03', 3)	# 9-11
    sprite('Action_999_04', 4)	# 12-15
    sprite('Action_999_05', 4)	# 16-19
    sprite('Action_999_06', 4)	# 20-23
    sprite('Action_999_07', 4)	# 24-27
    sprite('Action_999_08', 4)	# 28-31
    sprite('Action_999_09', 2)	# 32-33
    sprite('Action_999_10', 4)	# 34-37
    sprite('Action_999_11', 4)	# 38-41
    sprite('Action_999_12', 6)	# 42-47
    sprite('Action_999_13', 5)	# 48-52
    sprite('Action_999_14', 3)	# 53-55
    sprite('Action_999_15', 3)	# 56-58	 **attackbox here**
    sprite('Action_999_16', 3)	# 59-61	 **attackbox here**
    sprite('Action_999_17', 3)	# 62-64	 **attackbox here**
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)
    sprite('Action_999_18', 3)	# 65-67	 **attackbox here**
    sprite('Action_999_19', 3)	# 68-70	 **attackbox here**
    sprite('Action_999_20', 1)	# 71-71	 **attackbox here**

@State
def Entry_Back_Aura():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown2020(100)
    sprite('Action_120_13_1', 1)	# 1-1
    sprite('Action_120_14_1', 10)	# 2-11
    sprite('Action_120_15_1', 10)	# 12-21
    sprite('Action_120_16_1', 10)	# 22-31
    sprite('Action_120_17_1', 10)	# 32-41
    sprite('Action_120_18_1', 10)	# 42-51
    sprite('Action_120_19_1', 10)	# 52-61
    sprite('Action_120_20_1', 1)	# 62-62

@State
def Entry_Front_Aura():

    def upon_IMMEDIATE():
        Unknown4019(3)
        Unknown2020(-100)
    sprite('Action_120_13_2', 1)	# 1-1
    sprite('Action_120_14_2', 10)	# 2-11	 **attackbox here**
    sprite('Action_120_15_2', 10)	# 12-21	 **attackbox here**
    sprite('Action_120_16_2', 10)	# 22-31	 **attackbox here**
    sprite('Action_120_17_2', 10)	# 32-41	 **attackbox here**
    sprite('Action_120_18_2', 10)	# 42-51	 **attackbox here**
    sprite('Action_120_19_2', 10)	# 52-61
    sprite('Action_120_20_2', 1)	# 62-62

@State
def Win_Effect():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown2019(-1000)
    label(1)
    sprite('null', 1)	# 1-1
    Unknown23166('CmnActFDownLoop')
    if SLOT_ReturnVal:
        _gotolabel(2)
    Unknown19(1, 2, 0)
    label(2)
    sprite('Action_107_00', 5)	# 2-6
    SFX_3('SE_AppearInsulator')
    sprite('Action_107_01', 5)	# 7-11
    sprite('Action_107_02', 5)	# 12-16
    sprite('Action_107_03', 5)	# 17-21
    sprite('Action_107_04', 5)	# 22-26	 **attackbox here**
    sprite('Action_107_05', 5)	# 27-31	 **attackbox here**
    sprite('Action_107_06', 5)	# 32-36	 **attackbox here**
    Unknown36(22)
    Unknown3004(-51)
    Unknown2035(1)
    Unknown35()
    sprite('Action_107_07', 5)	# 37-41	 **attackbox here**
    sprite('Action_107_08', 5)	# 42-46	 **attackbox here**
    sprite('Action_107_09', 5)	# 47-51	 **attackbox here**
    sprite('Action_107_10', 5)	# 52-56	 **attackbox here**
    sprite('Action_107_11', 5)	# 57-61	 **attackbox here**
    sprite('Action_107_12', 5)	# 62-66
    SFX_3('SE_BloodFallDown')
    sprite('Action_107_13', 5)	# 67-71
    sprite('Action_107_14', 1)	# 72-72
