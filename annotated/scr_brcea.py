@State
def dmy():
    sprite('vrdmy', 120)	# 1-120

@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f52432e4449470000000000000000000000000000000000000065665f656d625f52435f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown23015(5)
    sprite('null', 10)	# 1-10
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)	# 11-20
    Unknown3025(-8342273, 10)
    sprite('null', 10)	# 21-30
    Unknown3025(-1, 10)
    sprite('null', 10)	# 31-40
    Unknown3025(-8342273, 10)
    sprite('null', 80)	# 41-120

@State
def EMB_RC_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f52432e4449470000000000000000000000000000000000000065665f656d625f52435f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown23015(5)
    sprite('null', 10)	# 1-10
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 10)	# 11-20
    Unknown3025(-8342273, 10)
    sprite('null', 10)	# 21-30
    Unknown3025(-16744193, 10)
    sprite('null', 10)	# 31-40
    Unknown3025(-16744193, 10)
    sprite('null', 80)	# 41-120

@State
def EMB_RC_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('65665f656d625f52432e4449470000000000000000000000000000000000000065665f656d625f52435f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown23015(5)
        Unknown3032()
    sprite('null', 10)	# 1-10
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 10)	# 11-20
    Unknown3025(-55256, 10)
    sprite('null', 10)	# 21-30
    Unknown3025(-19276, 10)
    sprite('null', 10)	# 31-40
    Unknown3025(-65536, 10)
    sprite('null', 80)	# 41-120

@State
def Gi():

    def upon_IMMEDIATE():
        Unknown32('4769436f6e74726f6c00000000000000')
        Unknown1086(3)
        teleportRelativeX(-120000)
        Unknown1007(360000)
        Unknown4025(3)
        Unknown4009(3)
    sprite('vrgi000_00', 100)	# 1-100
    enterState('GiNeutral')

@State
def GiNeutral():
    label(0)
    sprite('vrgi000_00', 2)	# 1-2
    Unknown2041(1)
    sprite('vrgi000_01', 2)	# 3-4
    sprite('vrgi000_02', 2)	# 5-6
    sprite('vrgi000_03', 2)	# 7-8
    sprite('vrgi000_04', 2)	# 9-10
    sprite('vrgi000_05', 2)	# 11-12
    sprite('vrgi000_06', 2)	# 13-14
    sprite('vrgi000_07', 2)	# 15-16
    sprite('vrgi000_08', 2)	# 17-18
    sprite('vrgi000_09', 2)	# 19-20
    sprite('vrgi000_00', 3)	# 21-23
    Unknown2040(1)
    sprite('vrgi000_01', 3)	# 24-26
    sprite('vrgi000_02', 3)	# 27-29
    sprite('vrgi000_03', 3)	# 30-32
    sprite('vrgi000_04', 3)	# 33-35
    sprite('vrgi000_05', 3)	# 36-38
    sprite('vrgi000_06', 3)	# 39-41
    sprite('vrgi000_07', 3)	# 42-44
    sprite('vrgi000_08', 3)	# 45-47
    sprite('vrgi000_09', 3)	# 48-50
    loopRest()
    gotoLabel(0)

@State
def GiPlayerDamage():
    sprite('vrgi060_00', 3)	# 1-3
    sprite('vrgi060_01', 3)	# 4-6
    label(0)
    sprite('vrgi060_02', 3)	# 7-9
    sprite('vrgi060_03', 3)	# 10-12
    sprite('vrgi060_04', 3)	# 13-15
    sprite('vrgi060_05', 3)	# 16-18
    sprite('vrgi060_06', 3)	# 19-21
    sprite('vrgi060_04', 3)	# 22-24
    sprite('vrgi060_03', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def GiTurn():
    sprite('vrgi000_10', 2)	# 1-2
    sprite('vrgi000_10', 2)	# 3-4
    Unknown2005()
    sprite('vrgi000_10', 1)	# 5-5
    sprite('keep', 100)	# 6-105
    enterState('GiNeutral')

@State
def GiDash():
    sprite('vrgi030_00', 3)	# 1-3
    label(0)
    sprite('vrgi030_01', 3)	# 4-6
    sprite('vrgi030_02', 3)	# 7-9
    sprite('vrgi030_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def GiDashDown():
    sprite('vrgi032_00', 3)	# 1-3
    label(0)
    sprite('vrgi032_01', 3)	# 4-6
    sprite('vrgi032_02', 3)	# 7-9
    sprite('vrgi032_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def GiDashUp():
    sprite('vrgi033_00', 3)	# 1-3
    label(0)
    sprite('vrgi033_01', 3)	# 4-6
    sprite('vrgi033_02', 3)	# 7-9
    sprite('vrgi033_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def gi_GirdBreak():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown3032()
        Unknown3001(255)
    sprite('vrgi090_02', 4)	# 1-4
    sprite('vrgi090_03', 3)	# 5-7
    sprite('vrgi090_04', 3)	# 8-10
    Unknown3004(-20)

@State
def GiStorm():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5101):
                sendToLabel(0)
            if (SLOT_48 == 5102):
                sendToLabel(1)
            if (SLOT_48 == 5103):
                sendToLabel(99)
        Unknown4008(3)

        def upon_STATE_END():
            Unknown4008(0)
    sprite('vrgi060_00', 3)	# 1-3
    sprite('vrgi060_01', 5)	# 4-8
    sprite('vrgi060_02', 3)	# 9-11
    sprite('vrgi432_00', 4)	# 12-15
    sprite('vrgi432_01', 4)	# 16-19
    sprite('vrgi432_01ex01', 5)	# 20-24
    sprite('vrgi432_02', 5)	# 25-29
    sprite('vrgi432_03', 5)	# 30-34
    label(0)
    sprite('vrgi432_04', 10)	# 35-44
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrgi432_05', 4)	# 45-48
    sprite('vrgi432_06', 4)	# 49-52
    sprite('vrgi432_07', 4)	# 53-56
    loopRest()
    label(2)
    sprite('vrgi432_08', 2)	# 57-58
    sprite('vrgi432_09', 2)	# 59-60
    sprite('vrgi432_10', 2)	# 61-62
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('vrgi432_11', 4)	# 63-66
    sprite('vrgi432_12', 4)	# 67-70
    sprite('vrgi432_13', 4)	# 71-74
    sprite('vrgi432_14', 4)	# 75-78
    enterState('GiNeutral')

@State
def GiHide():
    label(0)
    sprite('null', 1)	# 1-1
    Unknown3038(1)
    loopRest()
    gotoLabel(0)

@State
def nago_medama():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown3032()
        Unknown3001(255)
    sprite('rc063_11n', 5)	# 1-5
    sprite('rc063_11nex00', 5)	# 6-10
    sprite('rc063_11nex01', 8)	# 11-18
    sprite('rc063_11nex02', 5)	# 19-23
    sprite('rc063_11nex03', 5)	# 24-28
    sprite('rc063_11nex04', 5)	# 29-33
    sprite('rc063_11nex05', 5)	# 34-38
    sprite('rc063_11nex06', 5)	# 39-43
    sprite('rc063_11nex07', 5)	# 44-48
    sprite('rc063_11nex08', 5)	# 49-53
    sprite('rc063_11nex09', 20)	# 54-73
    Unknown3004(-20)

@Subroutine
def FlogDie():
    clearUponHandler(3)
    clearUponHandler(2)
    clearUponHandler(19)
    clearUponHandler(44)
    SLOT_59 = 0
    Unknown2037(0)
    Unknown2003(1)
    Unknown23022(1)
    sendToLabel(324)

@Subroutine
def FlogReset():
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23001(0, 0)
    SLOT_52 = 0

@State
def Flog():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown2003(1)
        callSubroutine('FlogReset')
        AttackLevel_(3)
        Damage(400)
        PushbackX(5000)
        Hitstop(2)
        Unknown11001(0, 3, 3)
        Unknown11057(300)
        AirUntechableTime(35)
        Unknown11092(1)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11056(3)
        Unknown12052(1)
        Unknown30065(0)
        Unknown11091(10)
        Unknown9021(1)
        Unknown9266(7)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown2019(-500)
        Unknown4061(1)
        SLOT_56 = 600
        SLOT_59 = 1
        Unknown2053(1)
        Unknown23020(2000)
        Unknown23021(2000)
        setInvincible(1)
        GuardPoint_(1)
        Unknown22019('0000000000000000000000000100000000000000')
        Unknown22031(-2, -1)

        def upon_19():
            if SLOT_59:
                callSubroutine('FlogDie')

        def upon_44():
            if (not SLOT_85):
                if SLOT_59:
                    callSubroutine('FlogDie')

        def upon_53():
            if SLOT_59:
                callSubroutine('FlogDie')

        def upon_3():
            if (not SLOT_85):
                SLOT_56 = (SLOT_56 + (-1))
                if (SLOT_56 < 0):
                    if SLOT_59:
                        callSubroutine('FlogDie')
            if SLOT_85:
                if (not SLOT_21):
                    if SLOT_59:
                        callSubroutine('FlogDie')
            if SLOT_2:
                if (SLOT_29 < 280000):
                    Unknown2037(0)
                    sendToLabel(661)
            if SLOT_2:
                Unknown23030('52435f466c6f6757696e64436865636b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            if SLOT_2:
                if (SLOT_40 < 0):
                    if (SLOT_38 == 0):
                        Unknown2037(0)
                        sendToLabel(322)
                if (SLOT_40 > 0):
                    if (SLOT_38 == 1):
                        Unknown2037(0)
                        sendToLabel(322)

        def upon_43():
            if (SLOT_48 == 3301):
                if SLOT_59:
                    callSubroutine('FlogDie')
            if (SLOT_48 == 3302):
                physicsXImpulse(10000)
                physicsYImpulse(6000)
                setGravity(1300)
            if (SLOT_48 == 3303):
                physicsXImpulse(15000)
                physicsYImpulse(20000)
                setGravity(1300)
    sprite('vrrcef_fgjp03', 3)	# 1-3	 **attackbox here**
    SFX_3('rcse_24')
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(100000)
    Unknown35()
    Unknown1096(500)
    Unknown1099(100)

    def upon_LANDING():
        if SLOT_59:
            sendToLabel(50)
    sprite('vrrcef_fgjp04', 3)	# 4-6	 **attackbox here**
    GFX_0('FlogATK', -1)
    label(55)
    sprite('vrrcef_fgjp05', 4)	# 7-10	 **attackbox here**
    Unknown1096(1200)
    Unknown1099(0)
    gotoLabel(55)
    loopRest()
    label(50)
    Unknown26('FlogATK')
    clearUponHandler(2)
    callSubroutine('FlogReset')
    teleportRelativeY(0)
    sprite('vrrcef_fgjp06', 2)	# 11-12	 **attackbox here**
    Unknown1096(1200)
    Unknown1099(0)
    sprite('vrrcef_fgjp07', 2)	# 13-14
    sprite('vrrcef_fgjp02', 2)	# 15-16
    sprite('vrrcef_fgjp01', 2)	# 17-18
    sprite('vrrcef_fgjp00', 2)	# 19-20
    label(338)
    sprite('vrrcef_fggr00', 2)	# 21-22	 **attackbox here**
    loopRest()
    label(132)
    callSubroutine('FlogReset')
    Unknown2037(1)
    physicsXImpulse(2000)
    sprite('vrrcef_fgwk00', 5)	# 23-27
    sprite('vrrcef_fgwk01', 5)	# 28-32
    SFX_3('rcse_06')
    sprite('vrrcef_fgwk02', 5)	# 33-37
    sprite('vrrcef_fgwk03', 5)	# 38-42
    sprite('vrrcef_fgwk04', 5)	# 43-47
    sprite('vrrcef_fgwk05', 5)	# 48-52
    sprite('vrrcef_fgwk06', 5)	# 53-57
    sprite('vrrcef_fgwk07', 5)	# 58-62
    SFX_3('rcse_06')
    sprite('vrrcef_fgwk08', 5)	# 63-67
    sprite('vrrcef_fgwk09', 5)	# 68-72
    sprite('vrrcef_fgwk10', 5)	# 73-77
    sprite('vrrcef_fgwk11', 5)	# 78-82
    sprite('vrrcef_fgwk01', 5)	# 83-87
    loopRest()
    label(133)
    sprite('vrrcef_fgwk02', 5)	# 88-92
    sprite('vrrcef_fgwk03', 5)	# 93-97
    sprite('vrrcef_fgwk04', 5)	# 98-102
    sprite('vrrcef_fgwk05', 5)	# 103-107
    sprite('vrrcef_fgwk06', 5)	# 108-112
    sprite('vrrcef_fgwk07', 5)	# 113-117
    SFX_3('rcse_06')
    sprite('vrrcef_fgwk08', 5)	# 118-122
    sprite('vrrcef_fgwk09', 5)	# 123-127
    sprite('vrrcef_fgwk10', 5)	# 128-132
    sprite('vrrcef_fgwk11', 5)	# 133-137
    sprite('vrrcef_fgwk01', 5)	# 138-142
    loopRest()
    gotoLabel(133)
    label(134)
    sprite('vrrcef_fgsl00', 6)	# 143-148	 **attackbox here**
    callSubroutine('FlogReset')
    Unknown2037(1)
    Unknown23001(150, 0)
    Unknown23012(150, 0, 0)
    SLOT_52 = 1
    GFX_0('FlogATK2', -1)
    sprite('vrrcef_fgsl00', 6)	# 149-154	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 155-160	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 161-166	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 167-172	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 173-178	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 179-184	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 185-190	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 191-196	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 197-202	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 203-208	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 209-214	 **attackbox here**
    sprite('vrrcef_fgsl00', 6)	# 215-220	 **attackbox here**
    sprite('vrrcef_fgjp06', 4)	# 221-224	 **attackbox here**
    Unknown26('FlogATK2')
    sprite('vrrcef_fgjp07', 4)	# 225-228
    loopRest()
    gotoLabel(132)
    label(135)
    sprite('vrrcef_fgwk00', 2)	# 229-230
    callSubroutine('FlogReset')
    Unknown2037(1)
    Unknown23001(35, 0)
    Unknown23012(35, 0, 0)
    SLOT_52 = 2
    sprite('vrrcef_fgwk01', 2)	# 231-232
    teleportRelativeX(2000)
    sprite('vrrcef_fgwk02', 2)	# 233-234
    teleportRelativeX(-2000)
    sprite('vrrcef_fgwk03', 2)	# 235-236
    teleportRelativeX(2000)
    sprite('vrrcef_fgwk04', 2)	# 237-238
    teleportRelativeX(-2000)
    sprite('vrrcef_fgwk05', 2)	# 239-240
    teleportRelativeX(2000)
    sprite('vrrcef_fgwk06', 2)	# 241-242
    teleportRelativeX(-2000)
    sprite('vrrcef_fgwk07', 2)	# 243-244
    teleportRelativeX(2000)
    loopRest()
    gotoLabel(132)
    label(251)
    callSubroutine('FlogReset')
    Unknown2037(1)
    physicsXImpulse(0)
    sprite('vrrcef_fgjp00', 4)	# 245-248
    sprite('vrrcef_fgjp01', 4)	# 249-252
    sprite('vrrcef_fgjp02', 3)	# 253-255
    Unknown2037(0)
    sprite('vrrcef_fgjp03', 3)	# 256-258	 **attackbox here**
    SFX_3('rcse_24')
    physicsXImpulse(12000)
    physicsYImpulse(13000)
    setGravity(1300)
    sendToLabelUpon(2, 100)
    sprite('vrrcef_fgjp04', 3)	# 259-261	 **attackbox here**
    label(101)
    sprite('vrrcef_fgjp05', 3)	# 262-264	 **attackbox here**
    loopRest()
    gotoLabel(101)
    label(100)
    callSubroutine('FlogReset')
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    sprite('vrrcef_fgjp06', 2)	# 265-266	 **attackbox here**
    Unknown2037(1)
    SFX_3('rcse_06')
    sprite('vrrcef_fgjp07', 3)	# 267-269
    sprite('vrrcef_fgjp02', 6)	# 270-275
    sprite('vrrcef_fgjp01', 6)	# 276-281
    sprite('vrrcef_fgjp00', 10)	# 282-291
    loopRest()
    gotoLabel(132)
    label(322)
    callSubroutine('FlogReset')
    sprite('vrrcef_fggr80', 6)	# 292-297
    Unknown2005()
    Unknown2037(0)
    sprite('vrrcef_fggr00', 6)	# 298-303	 **attackbox here**
    loopRest()
    gotoLabel(132)
    label(661)
    callSubroutine('FlogReset')
    Unknown2037(0)
    physicsXImpulse(0)
    Unknown2003(1)
    sprite('vrrcef_fggr00', 2)	# 304-305	 **attackbox here**
    SLOT_53 = 1
    Unknown23019(80)
    SLOT_56 = 9999
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(2000)
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr01', 2)	# 306-307	 **attackbox here**
    Unknown23019(80)
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(-2000)
    sprite('vrrcef_fggr02', 2)	# 308-309	 **attackbox here**
    Unknown23019(80)
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(2000)
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr03', 2)	# 310-311	 **attackbox here**
    Unknown23019(80)
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(-2000)
    sprite('vrrcef_fggr01', 2)	# 312-313	 **attackbox here**
    Unknown23019(80)
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(2000)
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr00', 2)	# 314-315	 **attackbox here**
    Unknown23019(0)
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(-2000)
    sprite('vrrcef_fggr01', 2)	# 316-317	 **attackbox here**
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(2000)
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr02', 2)	# 318-319	 **attackbox here**
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(-2000)
    sprite('vrrcef_fggr03', 2)	# 320-321	 **attackbox here**
    GFX_0('StayThunder', 0)
    GFX_0('StayThunder', 0)
    teleportRelativeX(2000)
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr00', 3)	# 322-324	 **attackbox here**
    Unknown2003(0)
    RefreshMultihit()
    GFX_0('LightningFrog', -1)
    Unknown38(1, 4)
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr01', 3)	# 325-327	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr02', 3)	# 328-330	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr03', 3)	# 331-333	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr02', 3)	# 334-336	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr01', 3)	# 337-339	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr00', 3)	# 340-342	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr01', 3)	# 343-345	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr02', 3)	# 346-348	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr03', 3)	# 349-351	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr02', 3)	# 352-354	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr01', 3)	# 355-357	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_ll')
    sprite('vrrcef_fggr00', 6)	# 358-363	 **attackbox here**
    Unknown2003(1)
    Unknown23022(1)
    Unknown13(4)
    sprite('vrrcef_fggr01', 6)	# 364-369	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 370-375	 **attackbox here**
    sprite('vrrcef_fggr03', 6)	# 376-381	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 382-387	 **attackbox here**
    GFX_0('LightningFrogDelete', -1)
    SFX_3('rcse_06')
    sprite('vrrcef_fggr01', 6)	# 388-393	 **attackbox here**
    sprite('vrrcef_fggr00', 6)	# 394-399	 **attackbox here**
    loopRest()
    if SLOT_85:
        _gotolabel(337)
    sprite('vrrcef_fggr00', 6)	# 400-405	 **attackbox here**
    sprite('vrrcef_fggr01', 6)	# 406-411	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 412-417	 **attackbox here**
    sprite('vrrcef_fggr03', 6)	# 418-423	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 424-429	 **attackbox here**
    sprite('vrrcef_fggr01', 6)	# 430-435	 **attackbox here**
    gotoLabel(324)
    label(337)
    sprite('vrrcef_fggr00', 6)	# 436-441	 **attackbox here**
    sprite('vrrcef_fggr01', 6)	# 442-447	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 448-453	 **attackbox here**
    sprite('vrrcef_fggr03', 6)	# 454-459	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 460-465	 **attackbox here**
    sprite('vrrcef_fggr01', 6)	# 466-471	 **attackbox here**
    sprite('vrrcef_fggr00', 6)	# 472-477	 **attackbox here**
    sprite('vrrcef_fggr00', 6)	# 478-483	 **attackbox here**
    sprite('vrrcef_fggr01', 6)	# 484-489	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 490-495	 **attackbox here**
    sprite('vrrcef_fggr03', 6)	# 496-501	 **attackbox here**
    sprite('vrrcef_fggr02', 6)	# 502-507	 **attackbox here**
    sprite('vrrcef_fggr01', 6)	# 508-513	 **attackbox here**
    sprite('vrrcef_fggr00', 6)	# 514-519	 **attackbox here**
    loopRest()
    gotoLabel(338)
    label(324)
    SLOT_59 = 0
    Unknown2003(1)
    sprite('vrrcef_fggr03', 1)	# 520-520	 **attackbox here**
    Unknown3032()
    Unknown3004(-14)
    GFX_0('FrogDelete', 0)

@State
def FlogATK():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        AttackLevel_(3)
        Unknown30065(0)
        Unknown11091(10)
        AirUntechableTime(60)
        AirPushbackY(15000)
    sprite('vrrcef_fgjp04_atkcol_damy', 32767)	# 1-32767	 **attackbox here**

@State
def FlogATK2():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        AttackLevel_(3)
        Unknown30065(0)
        Unknown11091(10)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(4000)
        AirPushbackY(25000)
    sprite('vrrcef_fgsl00_atkcol_damy', 32767)	# 1-32767	 **attackbox here**

@State
def LightningFrog():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown4010(2)
        Unknown1096(2700)
        Unknown3001(180)
        Unknown2055(90)
    label(0)
    sprite('vrrcef_lightning03', 2)	# 1-2
    Unknown1099(-200)
    Unknown1077(-180000, 180000)
    sprite('vrrcef_lightning03', 2)	# 3-4
    Unknown1099(200)
    Unknown1077(-180000, 180000)
    loopRest()
    gotoLabel(0)

@State
def LightningFrogDelete():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown4010(2)
        Unknown1096(2200)
        Unknown3001(255)
        Unknown3001(180)
    sprite('vrrcef_lightning03', 2)	# 1-2
    Unknown1099(-200)
    Unknown3004(-20)
    physicsYImpulse(4000)
    Unknown1077(-180000, 180000)
    sprite('vrrcef_lightning03', 2)	# 3-4
    Unknown1077(-180000, 180000)
    sprite('vrrcef_lightning03', 2)	# 5-6
    Unknown1077(-180000, 180000)
    sprite('vrrcef_lightning03', 2)	# 7-8
    Unknown1077(-180000, 180000)

@State
def StayThunder():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(1)
    sprite('vrrcef_stlt00', 1)	# 1-1
    Unknown1096(1000)
    Unknown1079()
    Unknown3001(255)
    Unknown3004(-10)
    sprite('null', 1)	# 2-2
    sprite('vrrcef_stlt01', 1)	# 3-3
    sprite('null', 1)	# 4-4
    sprite('vrrcef_stlt02', 1)	# 5-5
    sprite('null', 1)	# 6-6
    sprite('vrrcef_stlt03', 1)	# 7-7

@State
def ExWindRight():
    sprite('null', 100)	# 1-100
    GFX_1('rcef_exwindR', -1)

@State
def rcef_212Rose():
    sprite('null', 100)	# 1-100
    Unknown4007(2)
    Unknown4047(225, 226, 226)
    Unknown4045('726365665f323132726f73653030000000000000000000000000000000000000ffffffff')
    GFX_1('rcef_212light00', -1)

@State
def rcef_252Wind():
    sprite('null', 100)	# 1-100
    Unknown4007(2)
    GFX_1('rcef_252up_mc02', -1)

    def upon_56():
        Unknown4007(0)

@State
def rc201_Wind():

    def upon_IMMEDIATE():
        Unknown4007(3)

        def upon_56():
            Unknown4007(0)
    sprite('null', 19)	# 1-19
    Unknown3033()
    SFX_0('006_swing_blade_0')
    Unknown4003('726365665f77696e64412e444947000000000000000000000000000000000000726365665f77696e64415f6d6f745f3030302e6d6d6f74000000000000000000')

@State
def rcef_201rose():

    def upon_IMMEDIATE():
        Unknown4007(3)

        def upon_56():
            Unknown4007(0)
    sprite('null', 100)	# 1-100
    GFX_1('rcef_201rose01', 0)
    Unknown4047(225, 226, 227)
    Unknown4045('726365665f323031726f7365303200000000000000000000000000000000000000000000')
    Unknown4047(225, 224, 224)
    Unknown4045('726365665f323031726f7365303300000000000000000000000000000000000000000000')
    GFX_1('rcef_201rose04', 0)

@State
def rcef_202rose():
    sprite('null', 120)	# 1-120
    Unknown4047(225, 226, 227)
    Unknown4045('726365665f323032726f73653030000000000000000000000000000000000000ffffffff')

@State
def rcef_202wind():
    sprite('null', 120)	# 1-120
    GFX_1('rcef_202wind00', -1)
    GFX_1('rcef_202wind01', -1)

@State
def rcef_202tsuki():
    sprite('null', 120)	# 1-120
    Unknown4061(2)
    Unknown4047(233, 127, 127)
    Unknown4045('726365665f3230327473756b6900000000000000000000000000000000000000ffffffff')

@State
def rc231_Wind():
    sprite('null', 19)	# 1-19
    Unknown3033()
    SFX_0('006_swing_blade_0')
    Unknown4003('726365665f77696e64422e444947000000000000000000000000000000000000726365665f77696e64425f6d6f745f3030302e6d6d6f74000000000000000000')

@State
def rcef_231rose():
    sprite('null', 100)	# 1-100
    GFX_1('rcef_231rose01', 0)
    Unknown4047(225, 226, 227)
    Unknown4045('726365665f323331726f7365303200000000000000000000000000000000000000000000')
    Unknown4047(225, 224, 224)
    Unknown4045('726365665f323331726f7365303300000000000000000000000000000000000000000000')
    GFX_1('rcef_231rose04', 0)

@State
def rcef232ChairMc():
    sprite('null', 120)	# 1-120
    GFX_1('rcef_elchair_mc00', 0)
    GFX_1('rcef_elchair_mc01', 0)

@State
def rcef_602EntryPtc():

    def upon_IMMEDIATE():
        pass
    sprite('null', 100)	# 1-100
    GFX_2('rcef_602entryptc')
    GFX_0('rcef_602EntryLight', -1)
    GFX_0('rcef_602EntryRose', -1)
    GFX_0('rcef_602EntryWind', -1)

@State
def rcef_602EntryRose():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 100)	# 1-100
    Unknown4047(225, 226, 227)
    Unknown23067('rcef_602entryrose00')

@State
def rcef_602EntryLight():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 100)	# 1-100
    GFX_2('rcef_602entrylight00')

@State
def rcef_602EntryWind():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 100)	# 1-100
    GFX_2('rcef_602entrywind00')

@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown2019(10)
        Unknown4003('726365665f6d632e444947000000000000000000000000000000000000000000726365665f6d635f6d6f745f3030302e6d6d6f74000000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown21004(225)
        Unknown2054(1)
    sprite('null', 20)	# 1-20
    Unknown4007(3)
    sprite('null', 49)	# 21-69
    Unknown4007(0)

@State
def ModelMagicCircleAST():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
    sprite('null', 300)	# 1-300
    GFX_0('AstralMagicCircleA', -1)
    GFX_0('AstralMagicCircleB', -1)

@State
def AstralMagicCircleA():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('726365665f6d63322e4449470000000000000000000000000000000000000000726365665f6d63325f6d6f745f3030302e6d6d6f740000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(800)
    sprite('null', 10)	# 1-10
    Unknown3004(20)
    Unknown1099(50)
    SFX_0('022_magiccircle_b')
    Unknown3026(-65536)
    Unknown3025(-65536, 20)
    sprite('null', 120)	# 11-130
    Unknown1099(0)
    sprite('null', 20)	# 131-150
    Unknown3025(-16777216, 20)
    Unknown3004(-12)

@State
def AstralMagicCircleB():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('726365665f6d63332e4449470000000000000000000000000000000000000000726365665f6d63335f6d6f745f3030302e6d6d6f740000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(600)
    sprite('null', 60)	# 1-60
    sprite('null', 40)	# 61-100
    Unknown1099(5)
    Unknown3004(4)
    SFX_0('022_magiccircle_b')
    Unknown3026(-16777216)
    Unknown3025(1090453504, 40)
    sprite('null', 10)	# 101-110
    Unknown3001(255)
    Unknown1099(0)
    sprite('null', 20)	# 111-130
    Unknown3025(-16777216, 20)
    Unknown3004(-12)
    Unknown1099(2)

@State
def rcef_mc():
    sprite('null', 100)	# 1-100
    Unknown4047(225, 226, 227)
    Unknown4045('726365665f6d6300000000000000000000000000000000000000000000000000ffffffff')

@State
def rcef_600rose():
    sprite('null', 100)	# 1-100
    Unknown4047(265, 266, 266)
    Unknown4045('726365665f363030726f7365000000000000000000000000000000000000000000000000')

@State
def rcef_404flog():
    sprite('null', 100)	# 1-100
    Unknown4007(3)
    Unknown4047(225, 226, 227)
    Unknown4045('726365665f343034666c6f67000000000000000000000000000000000000000000000000')

@State
def LightningRodStart():
    sprite('null', 100)	# 1-100
    Unknown4007(2)
    Unknown4061(1)
    Unknown4047(230, 230, 230)
    Unknown4045('726365665f6c69676874726f645f6d616b650000000000000000000000000000ffffffff')

@State
def LightningRodRoop():
    sprite('null', 100)	# 1-100
    Unknown4010(2)
    Unknown4061(1)
    Unknown4047(239, 239, 239)
    Unknown4045('726365665f6c69676874726f6430300000000000000000000000000000000000ffffffff')
    Unknown4047(230, 230, 230)
    Unknown4045('726365665f6c69676874726f645f726f6f700000000000000000000000000000ffffffff')

@State
def LightningRodDelete():
    sprite('null', 100)	# 1-100
    Unknown4007(2)
    Unknown4061(1)
    Unknown4047(239, 239, 239)
    Unknown4045('726365665f6c69676874726f645f64656c303000000000000000000000000000ffffffff')
    Unknown4047(233, 233, 233)
    Unknown4045('726365665f6c69676874726f645f64656c303100000000000000000000000000ffffffff')
    Unknown4047(230, 230, 230)
    Unknown4045('726365665f6c69676874726f645f64656c000000000000000000000000000000ffffffff')

@State
def BatSummons():
    sprite('null', 100)	# 1-100
    Unknown4007(2)
    Unknown4047(29, 29, 29)
    Unknown4045('726365665f67695f616374303000000000000000000000000000000000000000ffffffff')
    Unknown4047(28, 28, 28)
    Unknown4045('726365665f67695f616374620000000000000000000000000000000000000000ffffffff')

@State
def BatDelete():
    sprite('null', 100)	# 1-100
    Unknown4007(2)
    Unknown4047(29, 29, 29)
    Unknown4045('726365665f67695f616374303000000000000000000000000000000000000000ffffffff')
    Unknown4047(28, 28, 28)
    Unknown4045('726365665f67695f616374303100000000000000000000000000000000000000ffffffff')
    GFX_1('rcef_gi_act', -1)

@State
def BirdSummons():
    sprite('null', 120)	# 1-120
    Unknown4061(2)
    GFX_1('rcef_birdkirakira00', 0)
    Unknown4047(239, 175, 127)
    Unknown4045('726365665f6269726473756d6d6f6e730000000000000000000000000000000000000000')

@State
def FrogDelete():
    sprite('null', 100)	# 1-100
    Unknown4007(2)
    Unknown4061(1)
    Unknown4047(239, 239, 239)
    Unknown4045('726365665f67695f616374303000000000000000000000000000000000000000ffffffff')
    Unknown4047(236, 236, 236)
    Unknown4045('726365665f67695f616374303100000000000000000000000000000000000000ffffffff')
    GFX_1('rcef_gi_act', -1)

@State
def rcef212windA():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_2('rcef_212wind00')
        Unknown4007(2)
        Unknown4013(2)
        Unknown4008(2)
        Unknown4006(2)
    sprite('null', 120)	# 1-120

@State
def rcef212windB():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_2('rcef_212wind01')
        Unknown4007(2)
        Unknown4013(2)
        Unknown4008(2)
        Unknown4006(2)
    sprite('null', 120)	# 1-120

@State
def rcef252windA():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_2('rcef_252wind00')
        Unknown4007(2)
        Unknown4013(2)
        Unknown4008(2)
        Unknown4006(2)

        def upon_56():
            Unknown4007(0)
    sprite('null', 120)	# 1-120

@State
def rcef252windB():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_2('rcef_252wind00')
        Unknown4007(2)
        Unknown4013(2)
        Unknown4008(2)
        Unknown4006(2)

        def upon_56():
            Unknown4007(0)
    sprite('null', 120)	# 1-120

@State
def AstralFinishRose():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1007(-256000)
    sprite('null', 100)	# 1-100
    Unknown4047(226, 226, 225)
    Unknown4045('726365665f61737477696e726f73650000000000000000000000000000000000ffffffff')

@State
def BirdFire():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_2('rcef_birdfire')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4008(2)
        Unknown4006(2)
    sprite('null', 3)	# 1-3
    GFX_1('rcef_birdfire', -1)

@State
def DownFallMcA():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_2('rcef_falldown_mc00')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4008(2)
        Unknown4006(2)
    sprite('null', 30)	# 1-30

@State
def DownFallMcB():

    def upon_IMMEDIATE():
        Unknown3038(1)
        GFX_2('rcef_falldown_mc01')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4008(2)
        Unknown4006(2)
    sprite('null', 30)	# 1-30

@State
def ReichelStormLv4():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f77696e642e44494700000000000000000000000000726365665f73746f726d5f77696e645f6d6f74696f6e5f3030302e6d6d6f7400')
        GFX_0('ReichelStormBG_Air_Lv4', -1)
        Unknown38(4, 1)
        GFX_0('ReichelStormBG_Rain_Lv2', -1)
        Unknown38(5, 1)
        GFX_0('ReichelStormBG_Rain_Lv4', -1)
        Unknown38(6, 1)
        Unknown3033()
        Unknown1096(3000)
        Unknown1000(0)
        teleportRelativeY(160000)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5104):
                sendToLabel(1)
        sendToLabelUpon(56, 1)
    sprite('null', 30)	# 1-30
    Unknown3004(6)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 60)	# 32798-32857
    clearUponHandler(43)
    clearUponHandler(56)
    sprite('null', 60)	# 32858-32917
    Unknown23029(4, 5105, 1)
    Unknown23029(5, 5105, 1)
    Unknown23029(6, 5105, 1)
    Unknown3004(-5)

@State
def Generator():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown2054(1)
        Unknown4011(3)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
    sprite('null', 16)	# 1-16
    sprite('null', 5)	# 17-21
    GFX_0('ReichelStormA', -1)
    physicsYImpulse(5000)
    sprite('null', 5)	# 22-26
    GFX_0('ReichelStormA', -1)
    sprite('null', 5)	# 27-31
    GFX_0('ReichelStormB', -1)
    sprite('null', 5)	# 32-36
    GFX_0('ReichelStormA', -1)
    sprite('null', 5)	# 37-41
    GFX_0('ReichelStormA', -1)
    sprite('null', 5)	# 42-46
    GFX_0('ReichelStormB', -1)
    sprite('null', 5)	# 47-51
    GFX_0('ReichelStormB', -1)
    sprite('null', 5)	# 52-56
    GFX_0('ReichelStormB', -1)
    sprite('null', 15)	# 57-71
    GFX_0('ReichelStormC', -1)
    sprite('null', 10)	# 72-81
    GFX_0('ReichelStormD', -1)

@State
def Generator_OD():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown2054(1)
        Unknown4011(3)
    sprite('null', 16)	# 1-16
    sprite('null', 4)	# 17-20
    GFX_0('ReichelStormA_OD', -1)
    physicsYImpulse(5000)
    sprite('null', 4)	# 21-24
    GFX_0('ReichelStormA_OD', -1)
    sprite('null', 4)	# 25-28
    GFX_0('ReichelStormB_OD', -1)
    sprite('null', 4)	# 29-32
    GFX_0('ReichelStormA_OD', -1)
    sprite('null', 4)	# 33-36
    GFX_0('ReichelStormA_OD', -1)
    sprite('null', 4)	# 37-40
    GFX_0('ReichelStormB_OD', -1)
    sprite('null', 4)	# 41-44
    GFX_0('ReichelStormA_OD', -1)
    sprite('null', 4)	# 45-48
    GFX_0('ReichelStormA_OD', -1)
    sprite('null', 4)	# 49-52
    GFX_0('ReichelStormB_OD', -1)
    sprite('null', 4)	# 53-56
    GFX_0('ReichelStormB_OD', -1)
    sprite('null', 5)	# 57-61
    GFX_0('ReichelStormB_OD', -1)
    sprite('null', 5)	# 62-66
    GFX_0('ReichelStormC_OD', -1)
    sprite('null', 5)	# 67-71
    GFX_0('ReichelStormC_OD', -1)
    sprite('null', 10)	# 72-81
    GFX_0('ReichelStormD_ODFinish', -1)

@Subroutine
def ReichelStorm_Matome():
    Unknown1086(3)
    Unknown23033(50)
    Unknown23032(-4)
    Unknown23001(50, 50)
    Unknown23012(2000, 100, 0)
    Unknown4061(3)
    Unknown2019(-100)
    Unknown3032()
    Unknown3029(1)
    Unknown3069(1)
    Unknown3070(1)
    Unknown3071(2)
    Unknown23013(1)
    Unknown53(1)
    Unknown2054(0)
    Unknown2055(480)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        Unknown23019(0)
        Unknown23001(0, 0)
        Unknown1019(20)
        if random_(2, 0, 50):
            Unknown1019(150)
        if random_(2, 0, 50):
            Unknown1019(150)
        if random_(2, 0, 50):
            Unknown1019(200)
        YAccel(60)
        if random_(2, 0, 50):
            YAccel(130)
        if random_(2, 0, 50):
            YAccel(130)
        if random_(2, 0, 50):
            YAccel(150)
        sendToLabel(1)

    def upon_5():
        clearUponHandler(5)
        Unknown23013(0)
        Unknown1028(0)
        Unknown1019(30)
        if random_(2, 0, 50):
            Unknown1019(130)
        if random_(2, 0, 50):
            Unknown1019(130)
        if random_(2, 0, 50):
            Unknown1019(200)
        YAccel(-60)
        if random_(2, 0, 50):
            YAccel(120)
        if random_(2, 0, 50):
            YAccel(120)
        if random_(2, 0, 50):
            YAccel(150)
        setGravity(1000)

    def upon_44():
        Unknown23001(0, 0)

@Subroutine
def ReichelStorm_Koumori():
    Unknown2011()
    AttackLevel_(3)
    Damage(400)
    Unknown11091(15)
    AttackP1(80)
    AttackP2(60)
    Unknown11092(1)
    Unknown9154(25)
    AirUntechableTime(40)
    AirPushbackX(3000)
    AirPushbackY(35000)
    Unknown23182(2)
    Unknown11110(80)
    Unknown1074(3000)
    physicsXImpulse(18000)
    physicsYImpulse(12000)
    Unknown1028(300)
    setGravity(1500)
    Unknown1026(-3000, 3000)
    Unknown1025(-2000, 6000)
    Unknown1011(50000, 130000)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

    def upon_54():
        clearUponHandler(54)
        sendToLabel(1)
    Unknown23027()

@Subroutine
def ReichelStorm_Ushi():
    Unknown2011()
    AttackLevel_(3)
    Damage(400)
    Unknown11091(15)
    AttackP1(80)
    AttackP2(60)
    Unknown11092(1)
    AirUntechableTime(50)
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    AirPushbackX(3000)
    AirPushbackY(35000)
    Unknown23182(2)
    Unknown11110(80)
    Unknown1074(2500)
    physicsXImpulse(18000)
    physicsYImpulse(12000)
    Unknown1028(300)
    setGravity(1500)
    Unknown1026(-3000, 3000)
    Unknown1025(-2000, 6000)
    Unknown1011(50000, 130000)
    Unknown1077(30000, 160000)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

    def upon_54():
        clearUponHandler(54)
        sendToLabel(1)
    Unknown23026(120000)
    Unknown23027()

@Subroutine
def ReichelStorm_Pumpkin():
    Unknown2011()
    AttackLevel_(4)
    Damage(800)
    Unknown11091(15)
    AttackP1(80)
    AttackP2(60)
    Unknown11092(1)
    AirUntechableTime(90)
    Hitstop(3)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(35000)
    Unknown23182(2)
    Unknown11110(80)
    Unknown1074(7500)
    physicsXImpulse(18000)
    physicsYImpulse(20000)
    Unknown1028(300)
    setGravity(1500)
    Unknown1026(-3000, 3000)
    Unknown1025(-2000, 6000)
    Unknown1011(50000, 100000)
    Unknown23026(120000)
    Unknown23027()

@Subroutine
def ReichelStorm_KingFlog():
    Unknown2011()
    AttackLevel_(5)
    Damage(1200)
    Unknown11091(15)
    AttackP1(80)
    AttackP2(60)
    Unknown11092(1)
    AirUntechableTime(90)
    Hitstop(3)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(35000)
    Unknown23182(2)
    Unknown11110(80)
    Unknown1074(7500)
    physicsXImpulse(18000)
    physicsYImpulse(20000)
    Unknown1028(300)
    setGravity(1500)
    Unknown23026(120000)
    Unknown23027()

@State
def ReichelStormA():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Koumori')
    sprite('vrrcef_stmA', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmA', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmA', 32767)	# 7-32773	 **attackbox here**
    label(1)
    sprite('vrrcef_stmA', 200)	# 32774-32973	 **attackbox here**
    Unknown2003(1)

@State
def ReichelStormA_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Koumori')
        Unknown23056('')
    sprite('vrrcef_stmA', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmA', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmA', 32767)	# 7-32773	 **attackbox here**
    label(1)
    sprite('vrrcef_stmA', 200)	# 32774-32973	 **attackbox here**
    Unknown2003(1)

@State
def ReichelStormB():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Ushi')
    sprite('vrrcef_stmB00', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmB00', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    label(99)
    sprite('vrrcef_stmB00', 2)	# 7-8	 **attackbox here**
    sprite('vrrcef_stmB01', 2)	# 9-10	 **attackbox here**
    sprite('vrrcef_stmB02', 2)	# 11-12	 **attackbox here**
    sprite('vrrcef_stmB03', 2)	# 13-14	 **attackbox here**
    gotoLabel(99)
    label(1)
    sprite('vrrcef_stmB00', 200)	# 15-214	 **attackbox here**
    SFX_3('rcse_20')
    Unknown2003(1)

@State
def ReichelStormB_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Ushi')
        Unknown23056('')
    sprite('vrrcef_stmB00', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmB00', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    label(99)
    sprite('vrrcef_stmB00', 2)	# 7-8	 **attackbox here**
    sprite('vrrcef_stmB01', 2)	# 9-10	 **attackbox here**
    sprite('vrrcef_stmB02', 2)	# 11-12	 **attackbox here**
    sprite('vrrcef_stmB03', 2)	# 13-14	 **attackbox here**
    gotoLabel(99)
    label(1)
    sprite('vrrcef_stmB00', 200)	# 15-214	 **attackbox here**
    SFX_3('rcse_20')
    Unknown2003(1)

@State
def ReichelStormC():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Pumpkin')
        GFX_0('ReichelStormCoption', -1)
        Unknown1096(1200)
    sprite('vrrcef_stmC', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmC', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmC', 32767)	# 7-32773	 **attackbox here**
    label(1)
    sprite('vrrcef_stmC', 10)	# 32774-32783	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmC', 10)	# 32784-32793	 **attackbox here**
    RefreshMultihit()
    Hitstop(11)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')
    sendToLabelUpon(54, 580)
    label(580)
    sprite('vrrcef_stmC', 180)	# 32794-32973	 **attackbox here**
    clearUponHandler(54)
    SFX_3('rcse_22')
    Unknown2003(1)

@State
def ReichelStormC_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_Pumpkin')
        Unknown23056('')
        GFX_0('ReichelStormCoption', -1)
        Unknown23029(1, 5110, 1)
        Unknown1096(1400)
    sprite('vrrcef_stmC', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmC', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmC', 32767)	# 7-32773	 **attackbox here**
    label(1)
    sprite('vrrcef_stmC', 10)	# 32774-32783	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmC', 10)	# 32784-32793	 **attackbox here**
    RefreshMultihit()
    Hitstop(11)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')
    sendToLabelUpon(54, 580)
    label(580)
    sprite('vrrcef_stmC', 180)	# 32794-32973	 **attackbox here**
    clearUponHandler(54)
    SFX_3('rcse_22')
    Unknown2003(1)

@State
def ReichelStormCoption():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4013(2)
        Unknown2019(501)
        Unknown3029(1)
        Unknown3069(1)
        Unknown3070(1)
        Unknown3071(3)
        Unknown2054(1)
        Unknown1096(1000)

        def upon_43():
            if (SLOT_48 == 5110):
                Unknown1096(1200)
    label(0)
    Unknown1074(7500)
    sprite('vrrcef_stmCopt00', 6)	# 1-6
    Unknown1073(30000)
    sprite('vrrcef_stmCopt01', 6)	# 7-12
    Unknown1073(30000)
    sprite('vrrcef_stmCopt02', 6)	# 13-18
    Unknown1073(30000)
    loopRest()
    gotoLabel(0)

@State
def ReichelStormD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_KingFlog')
        GFX_0('ReichelStormDoption', -1)
    sprite('vrrcef_stmD', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmD', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmD', 32767)	# 7-32773	 **attackbox here**
    Unknown4007(0)
    label(1)
    sprite('vrrcef_stmD', 20)	# 32774-32793	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmD', 10)	# 32794-32803	 **attackbox here**
    RefreshMultihit()
    Hitstop(20)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')
    sendToLabelUpon(54, 580)
    label(580)
    sprite('vrrcef_stmD', 150)	# 32804-32953	 **attackbox here**
    clearUponHandler(54)
    SFX_3('rcse_21')
    Unknown2003(1)

@State
def ReichelStormD_OD():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_KingFlog')
        Unknown23056('')
        GFX_0('ReichelStormDoption', -1)
    sprite('vrrcef_stmD', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmD', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmD', 32767)	# 7-32773	 **attackbox here**
    Unknown4007(0)
    label(1)
    sprite('vrrcef_stmD', 20)	# 32774-32793	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmD', 10)	# 32794-32803	 **attackbox here**
    RefreshMultihit()
    Hitstop(20)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')
    sendToLabelUpon(54, 580)
    label(580)
    sprite('vrrcef_stmD', 150)	# 32804-32953	 **attackbox here**
    clearUponHandler(54)
    SFX_3('rcse_21')
    Unknown2003(1)

@State
def ReichelStormD_ODFinish():

    def upon_IMMEDIATE():
        callSubroutine('ReichelStorm_Matome')
        callSubroutine('ReichelStorm_KingFlog')
        Unknown23056('')
        GFX_0('ReichelStormDoptionOver', -1)
        Unknown1096(1300)
    sprite('vrrcef_stmD', 5)	# 1-5	 **attackbox here**
    sprite('vrrcef_stmD', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmD', 32767)	# 7-32773	 **attackbox here**
    Unknown4007(0)
    label(1)
    sprite('vrrcef_stmD', 20)	# 32774-32793	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_stmD', 10)	# 32794-32803	 **attackbox here**
    RefreshMultihit()
    Hitstop(20)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')
    sendToLabelUpon(54, 580)
    label(580)
    sprite('vrrcef_stmD', 150)	# 32804-32953	 **attackbox here**
    clearUponHandler(54)
    SFX_3('rcse_21')
    Unknown2003(1)

@State
def ReichelStormDoption():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown2019(501)
        Unknown3029(1)
        Unknown3069(1)
        Unknown3070(1)
        Unknown3071(3)
        Unknown1074(5500)
        Unknown2054(1)
    label(0)
    sprite('vrrcef_stmDopt00', 4)	# 1-4
    Unknown1073(10000)
    sprite('vrrcef_stmDopt01', 4)	# 5-8
    Unknown1073(10000)
    sprite('vrrcef_stmDopt02', 4)	# 9-12
    Unknown1073(10000)
    loopRest()
    gotoLabel(0)

@State
def ReichelStormDoptionOver():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown2019(501)
        Unknown3029(1)
        Unknown3069(1)
        Unknown3070(1)
        Unknown3071(4)
        Unknown1074(5500)
        Unknown1096(1300)
        Unknown2054(1)
    label(0)
    sprite('vrrcef_stmDopt00', 4)	# 1-4
    Unknown1073(10000)
    sprite('vrrcef_stmDopt01', 4)	# 5-8
    Unknown1073(10000)
    sprite('vrrcef_stmDopt02', 4)	# 9-12
    Unknown1073(10000)
    loopRest()
    gotoLabel(0)

@State
def ReichelStormBG_Air_Lv1():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f6169722e4449470000000000000000000000000000726365665f73746f726d5f6169725f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
    sprite('null', 30)	# 1-30
    Unknown3004(2)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 60)	# 32798-32857
    Unknown3004(-5)

@State
def ReichelStormBG_Air_Lv2():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f6169722e4449470000000000000000000000000000726365665f73746f726d5f6169725f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
    sprite('null', 30)	# 1-30
    Unknown3004(4)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 60)	# 32798-32857
    Unknown3004(-5)

@State
def ReichelStormBG_Air_Lv3():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f6169722e4449470000000000000000000000000000726365665f73746f726d5f6169725f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
    sprite('null', 30)	# 1-30
    Unknown3004(7)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 60)	# 32798-32857
    Unknown3004(-5)

@State
def ReichelStormBG_Air_Lv4():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f6169722e4449470000000000000000000000000000726365665f73746f726d5f6169725f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
    sprite('null', 30)	# 1-30
    Unknown3004(10)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 60)	# 32798-32857
    Unknown3004(-5)

@State
def ReichelStormBG_Rain_Lv1():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f7261696e5f4c76312e444947000000000000000000726365665f73746f726d5f7261696e5f4c76315f6d6f74696f6e5f3030302e00')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
        Unknown4011(3)
    sprite('null', 30)	# 1-30
    Unknown3004(4)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 15)	# 32798-32812
    Unknown3004(-20)

@State
def ReichelStormBG_Rain_Lv2():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f7261696e5f4c76322e444947000000000000000000726365665f73746f726d5f7261696e5f4c76325f6d6f74696f6e5f3030302e00')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
        Unknown4011(3)
    sprite('null', 30)	# 1-30
    Unknown3004(6)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 15)	# 32798-32812
    Unknown3004(-20)

@State
def ReichelStormBG_Rain_Lv3():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f7261696e5f4c76332e444947000000000000000000726365665f73746f726d5f7261696e5f4c76335f6d6f74696f6e5f3030302e00')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
        Unknown4011(3)
    sprite('null', 30)	# 1-30
    Unknown3004(10)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 15)	# 32798-32812
    Unknown3004(-20)

@State
def ReichelStormBG_Rain_Lv4():

    def upon_IMMEDIATE():
        Unknown4003('726365665f73746f726d5f7261696e5f4c76342e444947000000000000000000726365665f73746f726d5f7261696e5f4c76345f6d6f74696f6e5f3030302e00')
        Unknown3033()
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 5105):
                sendToLabel(1)
        Unknown4011(3)
    sprite('null', 30)	# 1-30
    Unknown3004(10)
    sprite('null', 32767)	# 31-32797
    Unknown3004(0)
    label(1)
    sprite('null', 15)	# 32798-32812
    Unknown3004(-20)

@State
def rc202SwordLight():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
    sprite('vrrcef202_11', 4)	# 1-4	 **attackbox here**
    Unknown3001(255)
    sprite('vrrcef202_12', 8)	# 5-12	 **attackbox here**
    Unknown3004(-30)

@State
def rc232ElectlicChair():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown2055(13)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
    label(0)
    sprite('vrrcef_232_07', 1)	# 1-1
    sprite('vrrcef_232_08', 1)	# 2-2
    sprite('vrrcef_232_08add01', 1)	# 3-3
    sprite('vrrcef_232_08add02', 1)	# 4-4
    loopRest()
    gotoLabel(0)

@State
def Bird():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(600)
        AttackP1(80)
        AttackP2(92)
        Hitstop(9)
        Unknown9154(20)
        AirUntechableTime(20)
        Unknown12051(2)
        Unknown23027()
        Unknown3032()
        Unknown4061(1)
        Unknown23013(1)
        Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
        Unknown36(1)
        teleportRelativeY(80000)
        Unknown35()
        Unknown2037(4)
        SLOT_51 = 300

        def upon_43():
            if (SLOT_48 == 1103):
                if SLOT_2:
                    sendToLabel(99)
            if (SLOT_48 == 1001):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(1)
            if (SLOT_48 == 1002):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(2)
            if (SLOT_48 == 1003):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(3)
            if (SLOT_48 == 1004):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(4)
            if (SLOT_48 == 1006):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(6)
            if (SLOT_48 == 1007):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(7)
            if (SLOT_48 == 1008):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(8)
            if (SLOT_48 == 1001):
                if SLOT_2:
                    SLOT_51 = 180
                    Unknown2038(-1)
                    sendToLabel(9)

        def upon_3():
            if SLOT_51:
                SLOT_51 = (SLOT_51 + (-1))
                if (not SLOT_51):
                    SLOT_2 = 0
        sendToLabelUpon(2, 129)
        Unknown23089('0100000000000000000000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown2037(0)
    label(0)
    if (not SLOT_2):
        sendToLabel(99)
    sprite('vrrcef_pump00', 2)	# 1-2
    GFX_0('BirdFire', -1)
    Unknown23027()
    physicsXImpulse(1500)
    physicsYImpulse(1000)
    Unknown1096(1000)
    Unknown1099(0)
    sendToLabelUpon(2, 0)
    sprite('vrrcef_pump01', 2)	# 3-4
    sprite('vrrcef_pump02', 2)	# 5-6
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pump03', 2)	# 7-8
    sprite('vrrcef_pump02', 2)	# 9-10
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pump01', 2)	# 11-12
    loopRest()
    gotoLabel(0)
    label(129)
    sprite('vrrcef_pump00', 2)	# 13-14
    GFX_0('BirdFire', -1)
    Unknown23027()
    physicsXImpulse(1000)
    physicsYImpulse(1000)
    Unknown1096(1000)
    Unknown1099(0)
    sendToLabelUpon(2, 129)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrrcef_pumpsidedown00', 2)	# 15-16	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown2007()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    loopRest()
    gotoLabel(13)
    label(2)
    sprite('vrrcef_pumpdown00', 2)	# 17-18	 **attackbox here**
    GFX_0('BirdFire', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpdown01', 2)	# 19-20	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)	# 21-22	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(-45000)
    RefreshMultihit()
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown01', 2)	# 23-24	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)	# 25-26	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(2000)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpdown01', 2)	# 27-28	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)	# 29-30	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown01', 2)	# 31-32	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)	# 33-34	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown01', 2)	# 35-36	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpdown00', 2)	# 37-38	 **attackbox here**
    GFX_0('BirdFire', -1)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpdown01', 2)	# 39-40	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(1000)
    loopRest()
    gotoLabel(0)
    label(3)
    sprite('vrrcef_pumpsidedown00', 2)	# 41-42	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown2008()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    loopRest()
    gotoLabel(13)
    label(13)
    sprite('vrrcef_pumpsidedown01', 2)	# 43-44	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)	# 45-46	 **attackbox here**
    physicsXImpulse(31815)
    physicsYImpulse(-31815)
    RefreshMultihit()
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown01', 2)	# 47-48	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)	# 49-50	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(2000)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpsidedown01', 2)	# 51-52	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)	# 53-54	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown01', 2)	# 55-56	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)	# 57-58	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown01', 2)	# 59-60	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsidedown00', 2)	# 61-62	 **attackbox here**
    GFX_0('BirdFire', -1)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpsidedown01', 2)	# 63-64	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(1000)
    loopRest()
    gotoLabel(0)
    label(4)
    sprite('vrrcef_pumpside00', 2)	# 65-66	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown2007()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    loopRest()
    gotoLabel(46)
    label(6)
    sprite('vrrcef_pumpside00', 2)	# 67-68	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown2008()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    loopRest()
    gotoLabel(46)
    label(46)
    sprite('vrrcef_pumpside01', 2)	# 69-70	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 71-72	 **attackbox here**
    physicsXImpulse(45000)
    physicsYImpulse(0)
    RefreshMultihit()
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)	# 73-74	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 75-76	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(2000)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpside01', 2)	# 77-78	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 79-80	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)	# 81-82	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 83-84	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)	# 85-86	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 87-88	 **attackbox here**
    GFX_0('BirdFire', -1)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpside01', 2)	# 89-90	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(1000)
    loopRest()
    gotoLabel(0)
    label(7)
    sprite('vrrcef_pumpsideup00', 2)	# 91-92	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown2007()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    loopRest()
    gotoLabel(79)
    label(8)
    sprite('vrrcef_pumpup00', 2)	# 93-94	 **attackbox here**
    GFX_0('BirdFire', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpup01', 2)	# 95-96	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)	# 97-98	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(45000)
    RefreshMultihit()
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup01', 2)	# 99-100	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)	# 101-102	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(2000)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpup01', 2)	# 103-104	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)	# 105-106	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup01', 2)	# 107-108	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)	# 109-110	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup01', 2)	# 111-112	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpup00', 2)	# 113-114	 **attackbox here**
    GFX_0('BirdFire', -1)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpup01', 2)	# 115-116	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(1000)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrrcef_pumpsideup00', 2)	# 117-118	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown2008()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1096(1000)
    Unknown1099(100)
    SFX_0('001_airbackdash_0')
    SFX_0('006_swing_blade_1')
    SFX_0('015_blaze_0')
    loopRest()
    gotoLabel(79)
    label(79)
    sprite('vrrcef_pumpsideup01', 2)	# 119-120	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)	# 121-122	 **attackbox here**
    physicsXImpulse(31815)
    physicsYImpulse(31815)
    RefreshMultihit()
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup01', 2)	# 123-124	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)	# 125-126	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(2000)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpsideup01', 2)	# 127-128	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)	# 129-130	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup01', 2)	# 131-132	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)	# 133-134	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup01', 2)	# 135-136	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpsideup00', 2)	# 137-138	 **attackbox here**
    GFX_0('BirdFire', -1)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpsideup01', 2)	# 139-140	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(1000)
    loopRest()
    gotoLabel(0)
    label(99)
    clearUponHandler(3)
    Unknown2003(1)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1099(0)
    Unknown1096(1000)
    SLOT_2 = 0
    clearUponHandler(2)
    sprite('vrrcef_sbbreak00', 2)	# 141-142
    sprite('vrrcef_sbbreak01', 2)	# 143-144
    sprite('vrrcef_sbbreak02', 2)	# 145-146
    sprite('vrrcef_sbbreak03', 2)	# 147-148

@Subroutine
def LightningRod_Initialize():
    Unknown2010()
    Unknown4061(1)
    Unknown3032()
    Unknown3001(255)
    Unknown2053(1)

    def upon_7():
        if SLOT_54:
            clearUponHandler(7)
            Unknown1019(-60)
            SLOT_55 = 40
    Unknown23001(100, 100)
    Unknown23012(100, 100, 0)

    def upon_53():
        sendToLabel(35)

    def upon_3():
        if SLOT_2:
            if SLOT_66:
                SLOT_55 = (SLOT_55 + (-1))
                if (not SLOT_55):
                    RefreshMultihit()
    AttackLevel_(3)
    Damage(1230)
    AttackP1(80)
    GroundedHitstunAnimation(9)
    AirPushbackY(12000)
    AirUntechableTime(30)

    def upon_43():
        if (SLOT_48 == 3101):
            if SLOT_2:
                clearUponHandler(43)
                sendToLabel(35)
        if (SLOT_48 == 3001):
            if SLOT_2:
                clearUponHandler(2)
                SLOT_54 = 0
                Unknown23027()
                sendToLabel(48)
        if (SLOT_48 == 3002):
            if SLOT_2:
                clearUponHandler(2)
                SLOT_54 = 0
                Unknown23027()
                sendToLabel(47)
        if (SLOT_48 == 3003):
            if SLOT_2:
                clearUponHandler(2)
                SLOT_54 = 0
                Unknown23027()
                sendToLabel(49)
        if (SLOT_48 == 3004):
            clearUponHandler(2)
            SLOT_54 = 0
            Unknown23027()
            sendToLabel(53)
        if (SLOT_48 == 3005):
            clearUponHandler(2)
            SLOT_54 = 0
            Unknown23027()
            sendToLabel(47)
        if (SLOT_48 == 3006):
            clearUponHandler(2)
            SLOT_54 = 0
            Unknown23027()
            sendToLabel(49)
        if (SLOT_48 == 3102):
            AirPushbackX(7000)
            physicsXImpulse(7000)
            physicsYImpulse(8500)
            setGravity(1200)
        if (SLOT_48 == 3103):
            AirPushbackX(9500)
            physicsXImpulse(9500)
            physicsYImpulse(27000)
            setGravity(1200)
        if (SLOT_48 == 3104):
            AirPushbackX(12000)
            physicsXImpulse(15000)
            physicsYImpulse(36000)
            setGravity(1200)
        if (SLOT_48 == 3105):
            AirPushbackX(21000)
            physicsXImpulse(21000)
            physicsYImpulse(25000)
            setGravity(1500)
        if (SLOT_48 == 3106):
            AirPushbackX(27000)
            physicsXImpulse(27000)
            physicsYImpulse(-9000)
            setGravity(1500)
        if (SLOT_48 == 3107):
            AirPushbackX(13000)
            physicsXImpulse(13000)
            physicsYImpulse(-30000)
            setGravity(1000)
        if (SLOT_48 == 3108):
            AttackP1(70)
            AirPushbackX(9500)
            Unknown11042(1)
            physicsXImpulse(9500)
            physicsYImpulse(27000)
            setGravity(1200)
        if (SLOT_48 == 3109):
            AttackP1(70)
            AirPushbackX(12000)
            Unknown11042(1)
            physicsXImpulse(15000)
            physicsYImpulse(36000)
            setGravity(1200)
        if (SLOT_48 == 2006):
            if SLOT_2:
                clearUponHandler(2)
                Unknown23027()
                sendToLabel(52)
        if (SLOT_48 == 2007):
            if SLOT_2:
                clearUponHandler(2)
                Unknown23027()
                sendToLabel(51)

        def upon_58():
            if Unknown23156('ShotCatch'):
                if (SLOT_2 == 1):
                    if SLOT_66:
                        sendToLabel(50)
    sendToLabelUpon(2, 70)
    Unknown23089('0100000000000000000000000100000001000000000000000000000000000000')

    def upon_54():
        Unknown23027()
        Unknown3029(0)
        Unknown23118(0)
        Unknown1019(-30)
        physicsYImpulse(20000)
        Unknown23001(0, 0)
        Unknown23014()
        Unknown1074(-10000)

    def upon_44():
        GFX_0('StayThunder', 100)
        GFX_0('StayThunder', 100)
        GFX_0('StayThunder', 100)
        GFX_0('StayThunder', 100)
        Unknown3026(-6250336)
        Unknown3029(1)
        Unknown3071(6)
        Unknown2001()
        clearUponHandler(44)

    def upon_ON_HIT_OR_BLOCK():
        SLOT_66 = 1
        Unknown23027()

@State
def LightningRodA():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00', 2)	# 1-2	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(9500)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodB():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00ex', 1)	# 1-1	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)	# 2-2	 **attackbox here**
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(9500)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodC():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
        Unknown30065(0)
        Unknown11091(10)
    sprite('vrrcef_lightrod00ex', 1)	# 1-1	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)	# 2-2	 **attackbox here**
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(12000)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRod_TAG():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00ex', 1)	# 1-1	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)	# 2-2	 **attackbox here**
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(12000)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodA_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
        if SLOT_136:
            Unknown10000(80)
    sprite('vrrcef_lightrod00', 2)	# 1-2	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodB_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00', 2)	# 1-2	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodC_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
        Unknown30065(0)
        Unknown11091(10)
    sprite('vrrcef_lightrod00', 2)	# 1-2	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(43)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def rcef_412rose():
    sprite('null', 120)	# 1-120
    Unknown4047(225, 226, 227)
    Unknown4045('726365665f3431325f726f736500000000000000000000000000000000000000ffffffff')

@State
def LightningObjAtk():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2011()
        Unknown4019(3)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(4)
        Damage(1100)
        Unknown11091(10)
        AttackP2(60)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirUntechableTime(100)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11056(3)
        Unknown11057(500)
        Unknown9021(1)
        Unknown9266(7)
        PushbackX(12000)
        Hitstop(6)
        Unknown11001(0, 14, 19)

        def upon_43():
            if (SLOT_48 == 3007):
                Damage(250)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)

        def upon_3():

            def upon_77():
                SLOT_51 = (SLOT_51 + 1)

            def upon_81():
                SLOT_52 = (SLOT_52 + 1)
            if (SLOT_51 >= 8):
                Unknown2003(1)
                sendToLabel(0)
                clearUponHandler(3)
                clearUponHandler(81)
            if (SLOT_52 >= 8):
                Unknown30048(1)
    sprite('vrrcef_lightning01', 2)	# 1-2
    Unknown1072(15000)
    teleportRelativeX(150000)
    Unknown1056(4000)
    Unknown1064(1000)
    StartMultihit()
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning01', 2)	# 5-6
    Unknown1072(-15000)
    teleportRelativeX(-300000)
    Unknown1056(-4000)
    Unknown1064(1000)
    StartMultihit()
    sprite('vrrcef_lightning00SP', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    teleportRelativeX(150000)
    Unknown1056(2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 9-10	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 11-12	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 13-14	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 15-16	 **attackbox here**
    Unknown1072(0)
    Unknown1056(2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 17-18	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 19-20	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 21-22	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 23-24	 **attackbox here**
    Unknown1072(0)
    Unknown1056(2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 25-26	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 27-28	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 29-30	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 31-32	 **attackbox here**
    Unknown1072(0)
    Unknown1056(2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 33-34	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 35-36	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 37-38	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 39-40	 **attackbox here**
    Unknown1072(0)
    Unknown1056(2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 41-42	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 43-44	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 45-46	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 47-48	 **attackbox here**
    Unknown1072(0)
    Unknown1056(2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 49-50	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 51-52	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 53-54	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 55-56	 **attackbox here**
    Unknown1072(0)
    Unknown1056(2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 57-58	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 59-60	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 61-62	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    label(0)
    sprite('vrrcef_lightning01', 2)	# 63-64
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 65-66
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)

@State
def LightningObjAtk_Matome():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4061(2)
        Unknown2011()
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(4)
        Damage(1370)
        Unknown11091(10)
        AttackP2(60)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11056(3)
        Unknown11057(500)
        Unknown9021(1)
        Unknown9266(7)
        PushbackX(12000)
        Hitstop(6)
        Unknown11001(0, 14, 19)
        Unknown11110(92)

        def upon_43():
            if (SLOT_48 == 3008):
                Damage(310)
                AttackP1(100)
                AttackP2(100)
                Unknown11091(100)
                Unknown2037(1)
                SLOT_51 = 1
    sprite('null', 6)	# 1-6
    GFX_0('LightningObjAtk_OD', 100)
    GFX_0('LightningObjAtk_OD', 100)
    Unknown23029(1, 5007, 1)
    sprite('vrrcef_lightning00_atk', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('vrrcef_lightning00_atk', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    if SLOT_51:
        Damage(330)
    sprite('null', 4)	# 23-26

@State
def LightningObjAtk_OD():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4019(3)
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        Unknown1072(15000)
        teleportRelativeX(125000)

        def upon_43():
            if (SLOT_48 == 5007):
                teleportRelativeX(-310000)
        Unknown2003(1)
    sprite('vrrcef_lightning01', 2)	# 1-2
    Unknown1056(2000)
    Unknown1064(1000)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning01', 2)	# 5-6
    Unknown1072(-15000)
    teleportRelativeX(200000)
    Unknown1056(-2000)
    Unknown1064(1000)
    sprite('vrrcef_lightning00SP', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    teleportRelativeX(-170000)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 9-10	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 11-12	 **attackbox here**
    Unknown1056(1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 15-16	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 17-18	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 19-20	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00SP', 2)	# 21-22	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 23-24	 **attackbox here**
    Unknown1056(1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 25-26	 **attackbox here**
    Unknown1056(-1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 27-28	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 29-30	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 31-32	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 33-34	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 35-36	 **attackbox here**
    Unknown1056(1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 37-38	 **attackbox here**
    Unknown1056(-1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 39-40	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 41-42	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 43-44	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 45-46	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 47-48	 **attackbox here**
    Unknown1056(1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 49-50	 **attackbox here**
    Unknown1056(-1500)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 51-52	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning00SP', 2)	# 53-54	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(2000)
    GFX_0('LightningLand', -1)
    sprite('vrrcef_lightning01', 2)	# 55-56
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 57-58
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)

@State
def LightningObjAtkSub_Matome():
    sprite('null', 4)	# 1-4
    Unknown21015('4c696768746e696e674c616e64420000000000000000000000000000000000008a13000000000000')
    Unknown21015('4c696768746e696e6741697242000000000000000000000000000000000000008a13000000000000')
    sprite('null', 4)	# 5-8
    Unknown21015('4c696768746e696e674c616e64420000000000000000000000000000000000008b13000000000000')
    Unknown21015('4c696768746e696e6741697242000000000000000000000000000000000000008b13000000000000')
    sprite('null', 60)	# 9-68
    Unknown21015('4c696768746e696e674c616e64420000000000000000000000000000000000008c13000000000000')
    Unknown21015('4c696768746e696e6741697242000000000000000000000000000000000000008c13000000000000')

@State
def LightningObjAtkSub():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2011()
        Unknown23056('')
        Unknown4019(3)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(2)
        Damage(500)
        Unknown11091(10)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11057(500)
        Unknown11056(3)
        Unknown9021(1)
        Unknown9266(7)
        Hitstop(6)
        Unknown11001(0, 14, 19)
        Unknown11064(1)
    sprite('vrrcef_lightning01', 2)	# 1-2
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    sprite('vrrcef_lightning01', 2)	# 5-6
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    if SLOT_52:
        Unknown1056(1050)
        Unknown1064(2000)
    else:
        Unknown1056(750)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 9-10	 **attackbox here**
    if SLOT_52:
        Unknown1056(750)
        Unknown1064(2000)
    else:
        Unknown1056(-750)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 11-12	 **attackbox here**
    if SLOT_52:
        Unknown1056(1250)
        Unknown1064(2000)
    else:
        Unknown1056(1000)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    if SLOT_52:
        Unknown1056(1250)
        Unknown1064(2000)
    else:
        Unknown1056(-1000)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 15-16
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 17-18
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)

@State
def LightningObjAtkSubOD_Matome():
    sprite('null', 4)	# 1-4
    Unknown21015('4c696768746e696e674c616e64425f4f440000000000000000000000000000008a13000000000000')
    Unknown21015('4c696768746e696e67416972425f4f44000000000000000000000000000000008a13000000000000')
    sprite('null', 4)	# 5-8
    Unknown21015('4c696768746e696e674c616e64425f4f440000000000000000000000000000008b13000000000000')
    Unknown21015('4c696768746e696e67416972425f4f44000000000000000000000000000000008b13000000000000')
    sprite('null', 60)	# 9-68
    Unknown21015('4c696768746e696e674c616e64425f4f440000000000000000000000000000008c13000000000000')
    Unknown21015('4c696768746e696e67416972425f4f44000000000000000000000000000000008c13000000000000')

@State
def LightningObjAtkSubOD():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2011()
        Unknown23056('')
        Unknown4019(3)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(2)
        Damage(500)
        Unknown11091(10)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(100)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11057(500)
        Unknown11056(3)
        Unknown9021(1)
        Unknown9266(7)
        Hitstop(6)
        Unknown11001(0, 14, 19)
        Unknown11064(1)
    sprite('vrrcef_lightning01', 2)	# 1-2
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    sprite('vrrcef_lightning01', 2)	# 5-6
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    if SLOT_52:
        Unknown1056(1050)
        Unknown1064(2000)
    else:
        Unknown1056(750)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 9-10	 **attackbox here**
    if SLOT_52:
        Unknown1056(750)
        Unknown1064(2000)
    else:
        Unknown1056(-750)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 11-12	 **attackbox here**
    if SLOT_52:
        Unknown1056(1250)
        Unknown1064(2000)
    else:
        Unknown1056(1000)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    if SLOT_52:
        Unknown1056(1250)
        Unknown1064(2000)
    else:
        Unknown1056(-1000)
        Unknown1064(2000)
    RefreshMultihit()
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 15-16
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 17-18
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)

@State
def EffLightningMiniBoss():
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    sprite('null', 30)	# 1-30
    Unknown23032(40)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 31-60
    teleportRelativeX(200000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 61-90
    teleportRelativeX(200000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 91-120
    teleportRelativeX(200000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 121-150
    ExitState()
    label(0)
    sprite('null', 30)	# 151-180
    Unknown23032(90)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 181-210
    teleportRelativeX(-200000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 211-240
    teleportRelativeX(-200000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 241-270
    teleportRelativeX(-200000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 271-300
    ExitState()
    label(1)
    sprite('null', 60)	# 301-360
    sprite('null', 20)	# 361-380
    Unknown1086(3)
    teleportRelativeY(0)
    sprite('null', 40)	# 381-420
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 20)	# 421-440
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 40)	# 441-480
    GFX_0('LightningObjAtkMini', -1)
    ExitState()

@State
def EffLightningMiniEntryHZ():
    sprite('null', 30)	# 1-30
    Unknown1000(0)
    teleportRelativeY(0)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 31-60
    teleportRelativeX(-250000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 61-90
    teleportRelativeX(250000)
    GFX_0('LightningObjAtkMini', -1)
    sprite('null', 30)	# 91-120

@State
def LightningObjAtkMini():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2010()
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(2)
        Unknown11092(1)
        Hitstop(12)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11057(500)
        AirUntechableTime(34)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11056(3)
        Unknown12052(1)
        Unknown23182(3)
        Unknown23042()
        Unknown9021(1)
        Unknown9266(7)
        Unknown1056(500)
        Unknown3001(200)
    sprite('vrrcef_lightning01', 2)	# 1-2
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    sprite('vrrcef_lightning01', 2)	# 5-6
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    Unknown1056(750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 9-10	 **attackbox here**
    Unknown1056(-750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 11-12	 **attackbox here**
    Unknown1056(1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 15-16
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 17-18
    GFX_0('LightningOption', -1)

@State
def LightningObjAtkMini_Event():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2010()
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(2)
        Damage(600)
        Hitstop(12)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        Unknown11057(500)
        AirUntechableTime(42)
        Unknown11058('0000000000000000000000000100000000000000')
        AttackP1(80)
        Unknown11056(3)
        Unknown1056(500)
        Unknown3001(200)
    sprite('vrrcef_lightning01', 2)	# 1-2
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    sprite('vrrcef_lightning01', 2)	# 5-6
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    Unknown1056(750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 9-10	 **attackbox here**
    Unknown1056(-750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 11-12	 **attackbox here**
    Unknown1056(1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 15-16
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 17-18
    GFX_0('LightningOption', -1)

@State
def LightningOption():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        Unknown3001(200)
    sprite('null', 3)	# 1-3
    sprite('vrrcef_lightning01', 2)	# 4-5
    Unknown1010(-100000, 100000)
    Unknown1062(-2000, 2000)
    Unknown1025(-50000, 50000)
    Unknown1064(1000)

@State
def LightningLand():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown4009(2)
        Unknown4010(3)
        if SLOT_109:
            SLOT_52 = 1
        if SLOT_52:
            Unknown1056(3900)
            Unknown1064(2900)
        else:
            Unknown1056(4900)
            Unknown1064(2400)
        Unknown3001(255)
    sprite('vrrcef_lightning02', 2)	# 1-2
    Unknown1099(-200)
    sprite('vrrcef_lightning02', 3)	# 3-5
    Unknown3004(-85)

@State
def LightningLandSub():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown4009(2)
        Unknown4010(3)
        Unknown1056(2800)
        Unknown1064(2000)
        Unknown3001(255)
        Unknown3001(200)
    sprite('vrrcef_lightning02', 2)	# 1-2
    Unknown1099(-200)
    sprite('vrrcef_lightning02', 3)	# 3-5
    Unknown3004(-85)

@State
def rc600giPot():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(-500)
        Unknown4010(3)
    label(0)
    sprite('rc600_00ex01', 6)	# 1-6	 **attackbox here**
    sprite('rc600_01ex01', 6)	# 7-12	 **attackbox here**
    sprite('rc600_02ex01', 6)	# 13-18	 **attackbox here**
    sprite('rc600_03ex01', 6)	# 19-24	 **attackbox here**
    sprite('rc600_04ex01', 6)	# 25-30	 **attackbox here**
    sprite('rc600_05ex01', 6)	# 31-36	 **attackbox here**
    sprite('rc600_06ex01', 6)	# 37-42	 **attackbox here**
    sprite('rc600_07ex01', 6)	# 43-48	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def rc620nago():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(-100)
        Unknown4010(3)
    sprite('rc620_07n', 4)	# 1-4	 **attackbox here**
    sprite('rc620_07nex01', 4)	# 5-8	 **attackbox here**
    sprite('rc620_07nex02', 4)	# 9-12	 **attackbox here**
    Unknown8000(0, 1, 0)
    sprite('rc620_07nex03', 4)	# 13-16	 **attackbox here**
    label(0)
    sprite('rc620_07nex04', 4)	# 17-20	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def dengeki():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('rc082_00', 1)	# 1-1
    Unknown4061(6)
    Unknown1102(-150, 150)
    Unknown1010(-1000, 1000)
    Unknown1011(-5000, 5000)
    sprite('rc082_00', 1)	# 2-2
    Unknown1096(1000)
    sprite('rc082_01', 1)	# 3-3
    Unknown4061(7)
    Unknown1102(-150, 150)
    Unknown1010(-1000, 1000)
    Unknown1011(-5000, 5000)
    sprite('rc082_01', 1)	# 4-4
    Unknown1096(1000)
    loopRest()

@State
def dengeki_ng():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown2019(100)

        def upon_16():
            Unknown23016()
    sprite('rc082_00n', 32767)	# 1-32767

@State
def AstralNago():

    def upon_IMMEDIATE():
        Unknown4007(2)
        physicsYImpulse(-5000)
        teleportRelativeY(720000)
        teleportRelativeX(8000)
        Unknown1056(-1000)
    sprite('rc450_n08', 6)	# 1-6
    sprite('rc450_n08ex01', 6)	# 7-12
    sprite('rc450_n08', 6)	# 13-18
    sprite('rc450_n08ex02', 6)	# 19-24
    sprite('rc450_n08', 6)	# 25-30
    sprite('rc450_n08ex01', 6)	# 31-36
    sprite('rc450_n08', 6)	# 37-42
    sprite('rc450_n08ex02', 6)	# 43-48
    sprite('rc450_n08', 6)	# 49-54
    sprite('rc450_n08ex01', 3)	# 55-57
    sprite('rc450_n08ex01', 1)	# 58-58
    GFX_0('BatDelete', 0)

@State
def LightningObjAST():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2011()
        Unknown3033()
        Unknown2019(100)
        Unknown2003(1)
    sprite('vrrcef_lightning01', 1)	# 1-1
    Unknown1072(15000)
    teleportRelativeX(150000)
    Unknown1056(2000)
    Unknown1064(1000)
    StartMultihit()
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning01', 1)	# 2-2
    Unknown1072(-15000)
    teleportRelativeX(-300000)
    Unknown1056(-2000)
    Unknown1064(1000)
    StartMultihit()
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 3-4	 **attackbox here**
    Unknown1072(0)
    teleportRelativeX(150000)
    Unknown1056(2400)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 5-6	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 7-8	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 9-10	 **attackbox here**
    Unknown1056(-3000)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 11-12	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 15-16	 **attackbox here**
    teleportRelativeX(100000)
    Unknown1056(2400)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 17-18	 **attackbox here**
    Unknown1056(-2400)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 19-20	 **attackbox here**
    Unknown1056(3000)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 21-22	 **attackbox here**
    teleportRelativeX(-200000)
    Unknown1056(-3000)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 23-24	 **attackbox here**
    teleportRelativeX(200000)
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 25-26	 **attackbox here**
    teleportRelativeX(-150000)
    Unknown1056(-1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning01', 2)	# 27-28
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 29-30
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)

@State
def light():
    sprite('vr_light', 40)	# 1-40
    Unknown4007(3)
    Unknown4010(3)
    Unknown2019(-500)
    Unknown2054(1)
    Unknown3033()
    Unknown1056(100)
    Unknown1059(35)
    Unknown3026(-16777216)
    Unknown3025(-65536, 40)
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('vr_light', 40)	# 41-80
    Unknown1059(0)
    Unknown1056(1500)
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('vr_light', 10)	# 81-90
    Unknown3026(-65536)
    Unknown3025(-16777216, 10)
    Unknown1059(5)
    SFX_0('019_quake_0')

@State
def haka():
    sprite('vr_haka', 10)	# 1-10
    Unknown2019(500)
    Unknown1064(0)
    Unknown1056(3000)
    Unknown1067(300)
    sprite('vr_haka', 1000)	# 11-1010
    Unknown1067(0)

@State
def TestAstLightning():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11064(3)
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(2)
        Damage(800)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        AirUntechableTime(100)
        Unknown11057(500)
    sprite('null', 200)	# 1-200
    sprite('vrrcef_lightning01', 2)	# 201-202
    Unknown1072(15000)
    teleportRelativeX(150000)
    Unknown1056(2000)
    Unknown1064(1000)
    StartMultihit()
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 203-204
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning01', 2)	# 205-206
    Unknown1072(-15000)
    teleportRelativeX(-300000)
    Unknown1056(-2000)
    Unknown1064(1000)
    StartMultihit()
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 207-208	 **attackbox here**
    Unknown1072(0)
    teleportRelativeX(150000)
    Unknown1056(1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 209-210	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 211-212	 **attackbox here**
    Unknown1056(1500)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 213-214	 **attackbox here**
    Unknown1056(-1500)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 215-216	 **attackbox here**
    Unknown1072(0)
    Unknown1056(1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning00', 2)	# 217-218	 **attackbox here**
    Unknown1056(-1200)
    Unknown1064(1000)
    RefreshMultihit()
    GFX_0('LightningLand', -1)
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_1')
    SFX_0('013_thunder_0')
    sprite('vrrcef_lightning01', 2)	# 219-220
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 221-222
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)

@State
def WindSuctionGhost():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(500)
        AttackP2(100)
        PushbackX(8000)
        Unknown30055('000000000f00000000000000')
        Unknown11056(3)
        Unknown12052(1)
        Unknown23182(3)
        Unknown23013(1)
        Unknown9021(1)
        Unknown4061(1)
        Unknown3032()
        Unknown13044(1)
        Unknown2019(-100)
        GFX_0('WindSuctionGhost_fin', -1)

        def upon_12():
            SLOT_52 = 1
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            sendToLabel(99)

        def upon_3():
            if (SLOT_2 == 1):
                Unknown2006()
                Unknown2072('1600000000000000000000007017000001000000')
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 26):
                SLOT_51 = 0
                SFX_3('rcse_27')
    sprite('vrrcef412_00', 4)	# 1-4	 **attackbox here**
    Unknown23027()
    sprite('vrrcef412_01', 4)	# 5-8	 **attackbox here**
    sprite('vrrcef412_02', 4)	# 9-12	 **attackbox here**
    Unknown2037(1)
    sprite('vrrcef412_00', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    sprite('vrrcef412_01', 3)	# 16-18	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 19-21	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 22-24	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 25-27	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 28-30	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 31-33	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 34-36	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 37-39	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 40-42	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 43-45	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 46-48	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 49-51	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 52-54	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 55-57	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 58-60	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 61-63	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 64-66	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 67-69	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 70-72	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 73-75	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 76-78	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 79-81	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 82-84	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 85-87	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 88-90	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 91-93	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 94-96	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 97-99	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 100-102	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 103-105	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 106-108	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 109-111	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 112-114	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 115-117	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 118-120	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 121-123	 **attackbox here**
    sprite('vrrcef412_01', 3)	# 124-126	 **attackbox here**
    sprite('vrrcef412_02', 3)	# 127-129	 **attackbox here**
    sprite('vrrcef412_00', 3)	# 130-132	 **attackbox here**
    label(99)
    sprite('vrrcef412_00', 6)	# 133-138	 **attackbox here**
    Unknown1084(1)
    Unknown23027()
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    GFX_0('WindSuctionGhost_fin_end', -1)
    Unknown3004(-10)
    clearUponHandler(3)
    clearUponHandler(11)
    if SLOT_52:
        Unknown23027()
        Unknown13(25)
        GFX_0('LightningObjAtkMini', 104)
        SLOT_5 = 0
    sprite('vrrcef412_01', 6)	# 139-144	 **attackbox here**
    sprite('vrrcef412_02', 13)	# 145-157	 **attackbox here**

@State
def WindSuctionGhost_fin():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4008(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4061(1)
        Unknown3032()
        Unknown13044(1)
        Unknown4025(2)
    sprite('vrrcef412_10', 32767)	# 1-32767
    Unknown1074(30000)

@State
def WindSuctionGhost_fin_end():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4008(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4061(1)
        Unknown3032()
        Unknown13044(1)
        Unknown4025(22)
    sprite('vrrcef412_10', 32767)	# 1-32767
    Unknown1074(30000)
    Unknown3004(-25)

@State
def Fade1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4061(0)
        Unknown3001(160)
        teleportRelativeY(3000)
        Unknown2019(-500)
        Unknown3032()
    sprite('rc000_00', 15)	# 1-15
    Unknown3004(-9)
    Unknown1099(50)
    physicsYImpulse(-12000)
    sprite('rc000_00', 20)	# 16-35
    Unknown1099(-130)
    physicsYImpulse(12000)
    sprite('rc000_00', 2)	# 36-37
    Unknown1096(0)

@State
def LightningObjAtkMini_Event2():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2010()
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        Unknown11057(500)
        Unknown1056(500)
        Unknown3001(200)
        Unknown1086(22)
        teleportRelativeX(-50000)
    sprite('vrrcef_lightning01', 2)	# 1-2
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    sprite('vrrcef_lightning01', 2)	# 5-6
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    Unknown1056(750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 9-10	 **attackbox here**
    Unknown1056(-750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 11-12	 **attackbox here**
    Unknown1056(1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 15-16
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 17-18
    GFX_0('LightningOption', -1)

@State
def EventShakeObj():
    sprite('null', 40)	# 1-40
    sprite('null', 8)	# 41-48
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 8)	# 49-56
    ScreenShake(0, 3000)
    sprite('null', 8)	# 57-64
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 8)	# 65-72
    ScreenShake(0, 3000)
    sprite('null', 8)	# 73-80
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 8)	# 81-88
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 8)	# 89-96
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    sprite('null', 8)	# 97-104
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    label(0)
    sprite('null', 8)	# 105-112
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    loopRest()
    gotoLabel(0)

@State
def LightningObjAtkMiniD_TAG():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown2010()
        Unknown3033()
        Unknown2019(100)
        AttackLevel_(2)
        Damage(1000)
        AttackP1(70)
        Unknown11092(1)
        Hitstop(12)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11057(500)
        AirUntechableTime(34)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11056(3)
        Unknown12052(1)
        Unknown23182(3)
        Unknown23042()
        Unknown9021(1)
        Unknown9266(7)
        Unknown11042(1)
        Unknown1056(500)
        teleportRelativeX(300000)
        teleportRelativeY(0)
        if (SLOT_19 <= 300000):
            Unknown1086(22)
            teleportRelativeY(0)
        Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_32():
            AirPushbackY(25000)
            Hitstop(12)
            AirUntechableTime(34)
    sprite('null', 3)	# 1-3
    sprite('vrrcef_lightning01', 2)	# 4-5
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 6-7
    sprite('vrrcef_lightning01', 2)	# 8-9
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 10-11	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    Unknown1056(750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 12-13	 **attackbox here**
    Unknown1056(-750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 14-15	 **attackbox here**
    Unknown1056(1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 16-17	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 18-19
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 20-21
    GFX_0('LightningOption', -1)

@State
def LightningRod_TAG():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
        AttackP1(60)
        AttackP2(100)
        Unknown11090(110)
    sprite('vrrcef_lightrod00ex', 1)	# 1-1	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)	# 2-2	 **attackbox here**
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(9500)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodExB():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00ex', 1)	# 1-1	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)	# 2-2	 **attackbox here**
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(9500)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodExC():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00ex', 1)	# 1-1	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    GroundedHitstunAnimation(9)
    AirPushbackY(16000)
    AirUntechableTime(40)
    sprite('vrrcef_lightrod00', 1)	# 2-2	 **attackbox here**
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    GroundedHitstunAnimation(0)
    AirPushbackY(12000)
    AirUntechableTime(30)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodExB_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00', 2)	# 1-2	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def LightningRodExC_Air():

    def upon_IMMEDIATE():
        callSubroutine('LightningRod_Initialize')
    sprite('vrrcef_lightrod00', 2)	# 1-2	 **attackbox here**
    Unknown1096(500)
    Unknown1074(30000)
    sprite('vrrcef_lightrod00', 2)	# 3-4	 **attackbox here**
    Unknown1096(750)
    sprite('vrrcef_lightrod00', 5)	# 5-9	 **attackbox here**
    Unknown1096(1000)
    Unknown2037(1)
    sprite('vrrcef_lightrod00', 32767)	# 10-32776	 **attackbox here**
    SLOT_54 = 1
    loopRest()
    label(70)
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown23118(0)
    Unknown3029(0)
    Unknown23001(0, 0)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown2037(2)
    SLOT_66 = 0
    clearUponHandler(2)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown1072(0)
    Unknown1074(0)
    Unknown2019(500)
    sprite('vrrcef_lightrod01', 3)	# 32777-32779
    GFX_0('LightningRodStart', -1)
    SFX_0('012_stab_fast')
    sprite('vrrcef_lightrod02', 3)	# 32780-32782
    sprite('vrrcef_lightrod03', 3)	# 32783-32785
    sprite('vrrcef_lightrod04', 3)	# 32786-32788
    Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeY(512000)
    Unknown35()
    label(77)
    sprite('vrrcef_lightrod05', 5)	# 32789-32793
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown2019(500)
    GFX_0('LightningRodRoop', -1)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    GFX_0('StayThunder', 106)
    physicsYImpulse(500)
    Unknown1021(-50)
    sprite('vrrcef_lightrod05', 5)	# 32794-32798
    physicsYImpulse(250)
    Unknown1021(-25)
    sprite('vrrcef_lightrod05', 5)	# 32799-32803
    physicsYImpulse(100)
    Unknown1021(-10)
    sprite('vrrcef_lightrod05', 5)	# 32804-32808
    physicsYImpulse(-500)
    Unknown1021(50)
    sprite('vrrcef_lightrod05', 5)	# 32809-32813
    physicsYImpulse(-250)
    Unknown1021(25)
    sprite('vrrcef_lightrod05', 5)	# 32814-32818
    physicsYImpulse(-100)
    Unknown1021(10)
    loopRest()
    gotoLabel(77)
    label(35)
    Unknown2037(0)
    sprite('keep', 20)	# 32819-32838
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    Unknown3004(-12)
    GFX_0('LightningRodDelete', -1)
    Unknown1084(1)
    clearUponHandler(2)
    Unknown2001()
    loopRest()
    ExitState()
    label(47)
    Unknown2037(0)
    sprite('keep', 30)	# 32839-32868
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSub', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(48)
    Unknown2037(0)
    sprite('keep', 30)	# 32869-32898
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkMini', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(49)
    Unknown2037(0)
    sprite('keep', 30)	# 32899-32928
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningObjAtkSubOD', 104)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(50)
    Unknown2037(0)
    Unknown23027()
    sprite('keep', 15)	# 32929-32943
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    Unknown3004(-31)
    loopRest()
    ExitState()
    label(51)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32944-32973
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindRateUpGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(52)
    Unknown2037(0)
    GFX_1('rcef_412_wind', 0)
    GFX_0('rcef_412rose', 0)
    sprite('keep', 30)	# 32974-33003
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    clearUponHandler(58)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('WindSuctionGhost', 0)
    Unknown3004(-12)
    loopRest()
    ExitState()
    label(53)
    Unknown2037(0)
    sprite('keep', 30)	# 33004-33033
    Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
    clearUponHandler(44)
    Unknown3026(-1)
    Unknown3029(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown23012(0, 0, 0)
    Unknown23014()
    Unknown1074(0)
    GFX_0('LightningRodDelete', 104)
    Unknown3004(-12)
    loopRest()

@State
def ActInvincibleAttack_Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('rcef_430core')
        Unknown4003('726365665f3434305f74726e61646f00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1064(1600)
        Unknown1056(100)
        Unknown1088(100)
        teleportRelativeX(150000)
        Unknown3001(0)
        Unknown4007(3)
    sprite('null', 3)	# 1-3
    Unknown3004(18)
    Unknown1059(200)
    Unknown1091(200)
    SFX_3('rcse_08')
    SFX_3('rcse_09')
    SFX_3('rcse_10')
    sprite('null', 3)	# 4-6
    Unknown1059(100)
    Unknown1091(100)
    sprite('null', 4)	# 7-10
    Unknown1059(50)
    Unknown1091(50)
    sprite('null', 10)	# 11-20
    Unknown3004(0)
    SFX_3('rcse_09')
    sprite('null', 20)	# 21-40
    Unknown3004(-13)
    Unknown1059(-80)
    Unknown1091(-80)

@State
def Bird_Burst():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(350)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(9)
        AirPushbackX(24000)
        AirPushbackY(-75000)
        Hitstop(10)
        Unknown11028(13)
        AirUntechableTime(120)
        AttackP2(10)
        Unknown11084(1)
        Unknown11026(1)
        Unknown11064(2)
        Unknown11056(3)
        Unknown23078(1)
        Unknown23027()
        Unknown3032()
        Unknown4061(1)
        Unknown23013(1)
        Unknown4004('636d6e5f6a7564676d656e740000000000000000000000000000000000000000ffff0000')
        Unknown36(1)
        teleportRelativeY(80000)
        Unknown35()
        Unknown1086(22)
        teleportRelativeX(-1500000)
        setGravity(0)
        SLOT_12 = SLOT_19
        teleportRelativeX(12000)
        Unknown1007(240000)
        Unknown1019(3)
        Unknown2003(1)

        def upon_3():
            if (SLOT_18 >= 50):
                clearUponHandler(3)
                sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 1101):
                Unknown2003(0)
            if (SLOT_48 == 1102):
                Unknown2003(1)
    label(0)
    sprite('vrrcef_pumpside01', 2)	# 1-2	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 3-4	 **attackbox here**
    RefreshMultihit()
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)	# 5-6	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 7-8	 **attackbox here**
    GFX_0('BirdFire', -1)
    Unknown1099(0)
    Unknown1096(2000)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpside01', 2)	# 9-10	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 11-12	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)	# 13-14	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 15-16	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside01', 2)	# 17-18	 **attackbox here**
    GFX_0('BirdFire', -1)
    sprite('vrrcef_pumpside00', 2)	# 19-20	 **attackbox here**
    GFX_0('BirdFire', -1)
    SFX_0('015_blaze_0')
    sprite('vrrcef_pumpside01', 2)	# 21-22	 **attackbox here**
    GFX_0('BirdFire', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1099(0)
    Unknown1096(1000)
    sprite('vrrcef_sbbreak00', 2)	# 23-24
    sprite('vrrcef_sbbreak01', 2)	# 25-26
    sprite('vrrcef_sbbreak02', 2)	# 27-28
    sprite('vrrcef_sbbreak03', 2)	# 29-30

@State
def LightningObjAtkMini_Burst():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        Unknown10001(2)
        Unknown23078(1)
        Unknown1056(500)
        Unknown3001(200)
        teleportRelativeX(200000)
        teleportRelativeY(0)
    sprite('vrrcef_lightning01', 2)	# 1-2
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 3-4
    sprite('vrrcef_lightning01', 2)	# 5-6
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 7-8	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    Unknown1056(750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 9-10	 **attackbox here**
    Unknown23027()
    Unknown1056(-750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 11-12	 **attackbox here**
    Unknown1056(1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 13-14	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 15-16
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 17-18
    GFX_0('LightningOption', -1)

@State
def LightningObjAtkMini_ChangePartn():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4061(2)
        Unknown3033()
        Unknown2019(100)
        Unknown2054(1)
        AttackLevel_(3)
        Damage(350)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(9)
        AirPushbackX(24000)
        AirPushbackY(-75000)
        Hitstop(10)
        Unknown11028(24)
        AirUntechableTime(120)
        AttackP2(10)
        Unknown11084(1)
        Unknown11026(1)
        Unknown11064(2)
        Unknown11056(3)
        Unknown23078(1)
        Unknown1056(500)
        Unknown3001(200)
        Unknown9021(1)
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('null', 5)	# 1-5
    sprite('vrrcef_lightning01', 2)	# 6-7
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    SFX_0('013_thunder_0')
    sprite('null', 2)	# 8-9
    sprite('vrrcef_lightning01', 2)	# 10-11
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('vrrcef_lightning00', 2)	# 12-13	 **attackbox here**
    Unknown1072(0)
    Unknown1059(-100)
    Unknown1056(750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 14-15	 **attackbox here**
    Unknown1056(-750)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 16-17	 **attackbox here**
    Unknown1056(1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('vrrcef_lightning00', 2)	# 18-19	 **attackbox here**
    Unknown1056(-1000)
    Unknown1064(1000)
    GFX_0('LightningLandSub', -1)
    sprite('null', 2)	# 20-21
    GFX_0('LightningOption', -1)
    GFX_0('LightningOption', -1)
    sprite('null', 2)	# 22-23
    GFX_0('LightningOption', -1)

@State
def BurstDD_WindEff():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('rcef_430core')
        Unknown4003('726365665f3434305f74726e61646f00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1064(1600)
        Unknown1056(100)
        Unknown1088(100)
        teleportRelativeX(150000)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(18)
    Unknown1059(105)
    Unknown1091(105)
    SFX_3('rcse_08')
    SFX_3('rcse_09')
    SFX_3('rcse_10')
    sprite('null', 10)	# 11-20
    Unknown3004(0)
    SFX_3('rcse_09')
    sprite('null', 20)	# 21-40
    Unknown1059(-8)
    Unknown1091(-8)
    Unknown1067(1)
    SFX_3('rcse_10')
    sprite('null', 20)	# 41-60
    Unknown3004(-13)
    Unknown1059(-80)
    Unknown1091(-80)

@Subroutine
def IvyBlossom_Homing_TAG():
    if (SLOT_53 == 0):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 1):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 2):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 3):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 4):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 5):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 6):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 7):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 8):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')
    if (SLOT_53 == 9):
        Unknown23144('1600000000000000690000000000000000000000000000000000000000000000feffffff0000000002000000')

@Subroutine
def ShotDelete_dmy():
    Unknown4011(2)
    Unknown4010(2)
    Unknown4007(2)
    Unknown4009(2)
    GuardPoint_(1)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown22031(0, 0)
    Unknown22032(1)
    Unknown2037(1)

    def upon_3():
        if (not SLOT_30):

            def upon_42():
                if SLOT_2:
                    Unknown21007(3, 32)
                    Unknown2038(-1)

@State
def rc201_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('rc201_03_col_damy', 3)	# 1-3
    sprite('rc201_04_col_damy', 3)	# 4-6

@State
def rc406_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('rc406_12_col_damy', 3)	# 1-3

@State
def rc231_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('rc231_04_col_damy', 3)	# 1-3
    sprite('rc231_05_col_damy', 3)	# 4-6
