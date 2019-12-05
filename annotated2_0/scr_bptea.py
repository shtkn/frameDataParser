@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f50542e4449470000000000000000000000000000000000000065665f656d625f50545f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown23015(5)
    sprite('null', 8)	# 1-8
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 8)	# 9-16
    Unknown3025(-8342273, 10)
    sprite('null', 8)	# 17-24
    Unknown3025(-1, 10)
    sprite('null', 8)	# 25-32
    Unknown3025(-8342273, 10)
    sprite('null', 18)	# 33-50

@State
def EMB_PT_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f50542e4449470000000000000000000000000000000000000065665f656d625f50545f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown23015(5)
    sprite('null', 8)	# 1-8
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 8)	# 9-16
    Unknown3025(-8342273, 10)
    sprite('null', 8)	# 17-24
    Unknown3025(-16744193, 10)
    sprite('null', 8)	# 25-32
    Unknown3025(-16744193, 10)
    sprite('null', 18)	# 33-50

@State
def EMB_PT_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f50542e4449470000000000000000000000000000000000000065665f656d625f50545f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown23015(5)
    sprite('null', 8)	# 1-8
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 8)	# 9-16
    Unknown3025(-55256, 10)
    sprite('null', 8)	# 17-24
    Unknown3025(-19276, 10)
    sprite('null', 8)	# 25-32
    Unknown3025(-65536, 10)
    sprite('null', 18)	# 33-50

@State
def DebugObject():
    sprite('null', 2)	# 1-2
    loopRest()
    sprite('null', 30)	# 3-32
    GFX_0('Shabon', -1)

@State
def ShabonDist():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4010(2)
        Unknown3057(1)
        Unknown3058(12000)
        Unknown23015(1)

        def upon_33():
            sendToLabel(10)
    sprite('vr_shabon_dist', 32767)	# 1-32767
    label(10)
    sprite('vr_shabon_dist', 8)	# 32768-32775
    Unknown1099(20)
    Unknown3004(-30)

@State
def Shabon1():
    sprite('vr_shabon00', 4)	# 1-4
    Unknown23015(1)
    sprite('vr_shabon01', 4)	# 5-8

@State
def Shabon2():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown11001(0, 60, 60)
        Damage(800)
        AttackP1(70)
        GroundedHitstunAnimation(5)
        Hitstop(5)
        Unknown11050('0700000072756e6a756d705f77617465725f6c0000000000000000000000000000000000')
        Unknown11056(3)
        Unknown11032('20bf0200e040fdff20bf0200c081faff')
        Unknown11066(1)
        Unknown11084(1)
        Unknown11042(1)
        Unknown23015(1)
        Unknown23089('0100000000000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 10)
        Unknown23091(1)
        Unknown2053(1)
        Unknown23026(135000)
        Unknown2015(270)
        Unknown23180(1)

        def upon_LANDING():
            YAccel(-50)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23022(1)

        def upon_14():
            DisableAttackRestOfMove()
            Unknown23090(25)

        def upon_12():
            sendToLabel(11)
            Unknown23089('0100000000000000000000000000000000000000000000000000000000000000')
        Unknown1056(1620)
        Unknown1064(1380)

        def upon_CLEAR_OR_EXIT():
            SLOT_52 = (SLOT_52 + 1)
            if (not op(4, 2, 52, 0, 30)):
                if SLOT_51:
                    SLOT_51 = 0
                else:
                    SLOT_51 = 1
            if SLOT_51:
                Unknown1057(8)
                Unknown1065(-8)
            else:
                Unknown1057(-8)
                Unknown1065(8)
        GFX_0('ShabonDist', -1)
        Unknown38(4, 1)
        GFX_1('ptef_shaboncreate', -1)
    sprite('vr_shabon', 1)	# 1-1	 **attackbox here**
    label(1)
    sprite('vr_shabon', 12)	# 2-13	 **attackbox here**
    physicsXImpulse(2500)
    physicsYImpulse(-500)

    def upon_7():
        Unknown1019(-50)
    sprite('vr_shabon', 40)	# 14-53	 **attackbox here**
    sprite('vr_shabon', 1)	# 54-54	 **attackbox here**
    Unknown23090(25)
    loopRest()
    ExitState()
    label(11)
    sprite('vr_shabon', 1)	# 55-55	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown2053(0)
    SFX_3('ptse_27')
    Unknown23151(22, 103)
    Unknown4007(22)
    Unknown2054(1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1096(1200)
    Unknown1099(125)
    Unknown3004(40)
    Unknown36(4)
    Unknown3058(25000)
    Unknown35()
    sprite('vr_shabon', 12)	# 56-67	 **attackbox here**
    sprite('vr_shabon', 43)	# 68-110	 **attackbox here**
    Unknown3001(255)
    Unknown1096(2800)
    Unknown1099(0)
    Unknown3004(0)
    sprite('vr_shabon', 1)	# 111-111	 **attackbox here**
    Unknown23090(25)
    loopRest()
    ExitState()
    label(10)
    sprite('vr_shabonkoware', 30)	# 112-141
    DisableAttackRestOfMove()
    StartMultihit()
    setInvincible(1)
    Unknown1099(20)
    Unknown3004(-20)
    Unknown1019(40)
    YAccel(40)
    setGravity(0)
    Unknown2001()
    SFX_0('207_runjump_water_0')
    SFX_0('207_runjump_water_0')
    Unknown21012('536861626f6e446973740000000000000000000000000000000000000000000021000000')
    GFX_1('ptef_shabonkoware', -1)
    ExitState()

@State
def test1_2():
    sprite('test1_pt204_07_lv2', 3000)	# 1-3000	 **attackbox here**
    Unknown1007(300000)

@State
def test0():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        GroundedHitstunAnimation(9)
        Damage(550)
        AirUntechableTime(30)
        Unknown1074(7500)
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
    sprite('test0_pt204_07_lv2', 300)	# 1-300	 **attackbox here**

@State
def test1():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        GroundedHitstunAnimation(9)
        Damage(550)
        AirUntechableTime(30)
        Unknown1074(7500)
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
    sprite('test2_pt204_07_lv2', 300)	# 1-300	 **attackbox here**

@State
def test2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        GroundedHitstunAnimation(9)
        Damage(550)
        AirUntechableTime(30)
        Unknown1074(7500)
        Unknown1026(3000, 15000)
        Unknown1025(-2000, 2000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
    sprite('test1_pt204_07_lv2', 300)	# 1-300	 **attackbox here**

@Subroutine
def ItemThrowInit():
    AttackLevel_(4)
    Damage(1300)
    AirPushbackX(30000)
    GroundedHitstunAnimation(9)
    AirUntechableTime(30)
    AttackP1(70)
    setGravity(400)
    physicsXImpulse(38000)
    physicsYImpulse(12000)
    setGravity(1600)
    Unknown11042(1)
    if SLOT_5:
        AttackLevel_(5)
        Damage(1500)

@State
def Hummer():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Unknown11050('06000000707465665f6869745f70696b6f68616e5f7468726f7700000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_hummer', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_hummer', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def __16t_Hummer():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1800)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        Unknown11050('06000000707465665f6869745f6f746865725f7468726f77000000000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_16thummer', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_16thummer', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def Cat_Hummer():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1150)
        Unknown11050('06000000707465665f6869745f6361745f7468726f770000000000000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_Cat_hummer', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Cat_hummer', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def Lion_Hummer():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1500)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        Unknown11050('06000000707465665f6869745f6f746865725f7468726f77000000000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_Lion_hummer', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Lion_hummer', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def Frying-pan():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1100)
        Unknown11050('06000000707465665f6869745f66726970616e5f7468726f770000000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_Frying-pan', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Frying-pan', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def Harisen():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1300)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        Unknown11050('06000000707465665f6869745f6861726973656e5f7468726f7700000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_Harisen', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Harisen', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def Bat():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1200)
        Unknown11050('06000000707465665f6869745f6261745f7468726f770000000000000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_Bat', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Bat', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def Kanabou():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1600)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        Unknown11050('06000000707465665f6869745f6f746865725f7468726f77000000000000000000000000')
        Unknown1074(7500)
        Unknown1026(3000, 8000)
        Unknown1025(-4000, 4000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_Kanabou', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Kanabou', 30)	# 31-60	 **attackbox here**
    StartMultihit()

@State
def PaletteControlObj1():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c696768740000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(50000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@State
def PaletteControlObj2():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c696768740000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(100000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@State
def PaletteControlObj3():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c696768740000000000000000000000000000000000000000000000000000000005000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(150000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@State
def PaletteControlObj4():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c696768740000000000000000000000000000000000000000000000000000000007000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(200000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@State
def PaletteControlObj5():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c696768740000000000000000000000000000000000000000000000000000000009000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(250000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@State
def PaletteControlObj6():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c69676874000000000000000000000000000000000000000000000000000000000b000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(300000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@State
def PaletteControlObj7():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c69676874000000000000000000000000000000000000000000000000000000000d000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(300000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@State
def PaletteControlObj8():

    def upon_IMMEDIATE():
        Unknown3053(1)

        def upon_48():
            Unknown23030('50545f4c69676874000000000000000000000000000000000000000000000000000000000f000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(300000)
        teleportRelativeY(-200000)
    sprite('null', 32767)	# 1-32767

@Subroutine
def SetHikariColorByObjReg0():
    Unknown47('09000000020000003b00000000000000010000000200000037000000')
    Unknown47('09000000020000003b00000000000000020000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-60396)
    Unknown47('09000000020000003b00000000000000030000000200000037000000')
    Unknown47('09000000020000003b00000000000000040000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-15461121)
    Unknown47('09000000020000003b00000000000000050000000200000037000000')
    Unknown47('09000000020000003b00000000000000060000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-15401196)
    Unknown47('09000000020000003b00000000000000070000000200000037000000')
    Unknown47('09000000020000003b00000000000000080000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-690166)
    Unknown47('09000000020000003b00000000000000090000000200000037000000')
    Unknown47('09000000020000003b000000000000000a0000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-658171)
    Unknown47('09000000020000003b000000000000000b0000000200000037000000')
    Unknown47('09000000020000003b000000000000000c0000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-16386571)
    Unknown47('09000000020000003b000000000000000d0000000200000037000000')
    Unknown47('09000000020000003b000000000000000e0000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-64001)
    Unknown47('09000000020000003b000000000000000f0000000200000037000000')
    Unknown47('09000000020000003b00000000000000100000000200000038000000')
    if op(6, 2, 55, 2, 56):
        Unknown23118(-69999)

@State
def SphereLight():

    def upon_IMMEDIATE():

        def upon_16():
            Unknown23179(1)
            SLOT_59 = SLOT_4
            callSubroutine('SetHikariColorByObjReg0')

        def upon_53():
            Unknown14()
        Unknown2054(1)
        SLOT_51 = 1

        def upon_48():
            Unknown1085(3, 13, 0)

        def upon_45():
            SLOT_52 = (SLOT_52 + 1)
            if SLOT_51:
                if SLOT_28:
                    Unknown1085(3, 13, 0)
                    if (not op(4, 2, 52, 0, 8)):
                        GFX_1('ptef_driveptc', -1)
                if (not SLOT_28):
                    sendToLabel(0)
                    SLOT_51 = 0
                if (not SLOT_4):
                    sendToLabel(0)
                    SLOT_51 = 0
                    Unknown21012('5370686572654c696768745f4d6f64656c00000000000000000000000000000021000000')
            elif SLOT_28:
                if SLOT_59:
                    sendToLabel(1)
                    SLOT_51 = 1
        GFX_0('SphereLight_Model', -1)
    label(0)
    sprite('null', 32767)	# 1-32767
    label(1)
    sprite('vr_sphere_light2', 20)	# 32768-32787
    Unknown23179(1)
    Unknown23180(1)
    Unknown3033()
    Unknown1096(0)
    Unknown3001(0)
    Unknown3004(8)
    Unknown1099(100)
    Unknown1074(8000)
    Unknown2019(500)
    if (not op(4, 2, 59, 0, 2)):
        Unknown21012('5370686572654c696768745f4d6f64656c00000000000000000000000000000020000000')
    loopRest()
    Unknown1099(0)
    Unknown1096(2000)
    Unknown1074(800)
    Unknown3001(190)
    label(2)
    sprite('vr_sphere_light2', 4)	# 32788-32791
    Unknown3001(190)
    Unknown3004(-17)
    sprite('vr_sphere_light2', 4)	# 32792-32795
    Unknown3004(17)
    loopRest()
    gotoLabel(2)

@State
def SphereLight_Shutsugen():
    sprite('null', 30)	# 1-30
    Unknown23067('ptef_drivepurg')
    GFX_0('yugami_ring', -1)
    Unknown2054(1)
    sprite('null', 30)	# 31-60
    Unknown3004(-30)

@State
def SphereLight_Model():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6b7572756b7572752e444947000000000000000000000000000000707465665f6b7572756b7572755f6d6f74696f6e5f3030302e6d6d6f74000000')
        Unknown4015()
        Unknown2019(500)
        Unknown2054(1)
        Unknown4025(3)

        def upon_53():
            Unknown14()

        def upon_16():
            Unknown2071('0200000000000000000000005000000001000000')
            Unknown23179(1)
            SLOT_59 = SLOT_5
            callSubroutine('SetHikariColorByObjReg0')
        Unknown1096(350)
        Unknown1088(1000)
        Unknown3001(0)

        def upon_45():
            if SLOT_5:
                if SLOT_28:
                    Unknown3004(30)
                    Unknown23179(1)
                    SLOT_59 = SLOT_5
                    callSubroutine('SetHikariColorByObjReg0')
                else:
                    Unknown3004(-30)
            else:
                Unknown3004(-30)

        def upon_33():
            Unknown3004(-30)
    sprite('null', 32767)	# 1-32767

@State
def StaggerSoul():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown3032()
        teleportRelativeY(270000)
        teleportRelativeX(50000)
        Unknown3001(220)
    sprite('vrptef070_00', 8)	# 1-8
    physicsYImpulse(2000)
    sprite('vrptef070_00', 14)	# 9-22
    Unknown3004(-10)
    sprite('vrptef070_00', 10)	# 23-32
    Unknown3004(-20)

@State
def ptef_hit_low():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_low', -1)
    SFX_3('ptse_15')

@State
def ptef_hit_middle():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_16')

@State
def ptef_hit_high():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_high', -1)
    SFX_3('ptse_17')

@State
def ptef_hit_fripan():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_18')
    SFX_0('102_hit_counter_grap_1')

@State
def ptef_hit_harisen():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_19')

@State
def ptef_hit_bat():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_20')
    SFX_0('102_hit_counter_grap_1')

@State
def ptef_hit_pikohan_throw():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_02')

@State
def ptef_hit_fripan_throw():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_18')
    SFX_0('102_hit_counter_grap_1')

@State
def ptef_hit_harisen_throw():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_19')
    SFX_0('100_hit_grap_2')

@State
def ptef_hit_bat_throw():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_20')
    SFX_0('102_hit_counter_grap_1')

@State
def ptef_hit_cat_throw():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_3('ptse_24')

@State
def ptef_hit_other_throw():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_0('100_hit_grap_2')

@State
def ptef_hit_kanabou():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_hit_middle', -1)
    SFX_0('025_cleanhit_grap')

@State
def ptef_hit_throw():
    sprite('null', 1)	# 1-1
    GFX_1('ptef_throw', -1)
    SFX_3('ptse_18')
    SFX_0('102_hit_counter_grap_1')

@State
def Atk6CZanzo():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown3032()
        teleportRelativeY(420000)
        teleportRelativeX(-20000)
    sprite('vrptef212_00', 3)	# 1-3
    sprite('vrptef212_01', 3)	# 4-6
    Unknown3004(-10)
    sprite('vrptef212_02', 3)	# 7-9
    sprite('vrptef212_02', 3)	# 10-12
    Unknown3004(-45)
    teleportRelativeX(-20000)
    Unknown1007(-5000)

@State
def ThrowBind():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown4003('707465665f62696e642e44494700000000000000000000000000000000000000707465665f62696e645f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1096(1000)
        Unknown1007(-40000)
    sprite('null', 38)	# 1-38
    sprite('null', 20)	# 39-58
    Unknown3004(-20)
    Unknown1099(30)

@State
def ThrowMcircle():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6b6f75736f6b75636972636c652e44494700000000000000000000707465665f6b6f75736f6b75636972636c655f6d6f74696f6e5f3030302e6d00')
        Unknown4015()
        Unknown3033()
        Unknown1096(1100)
        Unknown1007(-40000)
        sendToLabelUpon(32, 12)
    sprite('null', 8)	# 1-8
    Unknown3001(0)
    Unknown3004(20)
    sprite('null', 30)	# 9-38
    Unknown3001(255)
    sprite('null', 10)	# 39-48
    Unknown3004(-35)
    Unknown1099(75)

@State
def Throwef():

    def upon_IMMEDIATE():
        GFX_2('ptef_throwef')
        Unknown3033()
        Unknown1096(900)
        Unknown1007(-20000)
        Unknown3001(0)
    sprite('null', 5)	# 1-5
    Unknown3004(40)
    sprite('null', 35)	# 6-40
    Unknown3001(255)
    sprite('null', 20)	# 41-60
    Unknown3004(-20)

@State
def ThrowKousoku():
    sprite('null', 4)	# 1-4
    GFX_0('ThrowMcircle', 1)
    GFX_0('Throwef', 1)
    sprite('null', 1)	# 5-5
    GFX_0('ThrowBind', 1)

@State
def MagicIron():

    def upon_IMMEDIATE():
        Unknown3001(255)
        Unknown3032()
        Unknown11066(1)
        Unknown4009(3)

        def upon_32():
            teleportRelativeX(-600000)
            Unknown1007(100000)
            sendToLabel(0)

        def upon_33():
            teleportRelativeX(600000)
            Unknown1007(100000)
            sendToLabel(1)

        def upon_34():
            teleportRelativeX(-15000)
            Unknown1007(250000)
            sendToLabel(2)
    sprite('null', 1)	# 1-1
    label(0)
    sprite('vrptef311_00', 32767)	# 2-32768	 **attackbox here**

    def upon_11():
        sendToLabel(3)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(2000)
    physicsYImpulse(-10000)
    setGravity(-200)
    Unknown3038(0)
    sendToLabelUpon(35, 3)
    loopRest()
    ExitState()
    label(1)
    sprite('vrptef311_00', 32767)	# 32769-65535	 **attackbox here**

    def upon_11():
        sendToLabel(4)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(-1500)
    physicsYImpulse(-10000)
    setGravity(-200)
    sendToLabelUpon(36, 4)
    loopRest()
    ExitState()
    label(2)
    sprite('vrptef311_00', 32767)	# 65536-98302	 **attackbox here**

    def upon_11():
        sendToLabel(5)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    physicsYImpulse(-36000)
    sendToLabelUpon(37, 5)
    loopRest()
    ExitState()
    label(3)
    sprite('vrptef311_00', 1)	# 98303-98303	 **attackbox here**
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(-10000)
    physicsYImpulse(31000)
    setGravity(3000)
    Unknown1019(90)
    YAccel(90)
    sprite('vrptef311_00', 20)	# 98304-98323	 **attackbox here**
    Unknown3004(-10)
    loopRest()
    ExitState()
    label(4)
    sprite('vrptef311_00', 1)	# 98324-98324	 **attackbox here**
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(10000)
    physicsYImpulse(31000)
    setGravity(3000)
    Unknown1019(90)
    YAccel(90)
    sprite('vrptef311_00', 20)	# 98325-98344	 **attackbox here**
    Unknown3004(-10)
    loopRest()
    ExitState()
    label(5)
    sprite('vrptef311_00', 20)	# 98345-98364	 **attackbox here**
    Unknown23026(135000)

    def upon_LANDING():
        StartMultihit()
        Unknown1028(0)
        physicsXImpulse(0)
        physicsYImpulse(31000)
        setGravity(3000)
        Unknown1019(90)
        YAccel(90)
        Unknown3004(-10)
    sprite('vrptef311_00', 20)	# 98365-98384	 **attackbox here**
    loopRest()
    ExitState()

@State
def Kemuri():

    def upon_IMMEDIATE():
        GFX_2('ptef_311smoke')
        Unknown3032()
        teleportRelativeX(-600000)
        Unknown1007(100000)
    sprite('null', 40)	# 1-40

@State
def Kemuri2():

    def upon_IMMEDIATE():
        GFX_2('ptef_311smoke')
        Unknown3032()
        teleportRelativeX(600000)
        Unknown1007(100000)
    sprite('null', 40)	# 1-40

@State
def Kemuri3():

    def upon_IMMEDIATE():
        GFX_2('ptef_311smoke')
        Unknown3032()
        Unknown1007(200000)
    sprite('null', 40)	# 1-40

@State
def Kemuri4():

    def upon_IMMEDIATE():
        GFX_2('ptef_311smoke')
        Unknown3032()
        Unknown1086(22)
        teleportRelativeX(-15000)
        Unknown1007(500000)
    sprite('null', 40)	# 1-40

@State
def pt203_mahojin():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6d61686f6a696e312e444947000000000000000000000000000000707465665f6d61686f6a696e315f6d6f74696f6e5f3030302e6d6d6f74000000')
        Unknown4015()
        Unknown4007(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(600)
        Unknown1007(20000)
    sprite('null', 20)	# 1-20
    sprite('null', 30)	# 21-50
    Unknown4007(0)
    sprite('null', 13)	# 51-63
    Unknown3004(-20)

@State
def pt203_airmahojin():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6d61686f6a696e312e444947000000000000000000000000000000707465665f6d61686f6a696e315f6d6f74696f6e5f3030302e6d6d6f74000000')
        Unknown4010(2)
        Unknown4015()
        Unknown4007(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(600)
        Unknown1007(20000)
    sprite('null', 20)	# 1-20
    sprite('null', 30)	# 21-50
    Unknown4007(0)
    sprite('null', 13)	# 51-63
    Unknown3004(-30)

@State
def pt203_aura1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown3033()
        Unknown23015(5)
        Unknown1007(8000)
        Unknown1056(3000)
        Unknown1064(4200)
        Unknown3026(-1775742726)
    sprite('vrptef_env', 50)	# 1-50
    sprite('vrptef_env', 20)	# 51-70
    Unknown1099(-100)
    Unknown3004(-20)

@State
def pt203_aura2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown3033()
        Unknown1007(-30000)
        Unknown3001(0)
        Unknown1056(5400)
        Unknown1064(1400)
        Unknown3026(5299310)
    sprite('vrptef_env', 15)	# 1-15
    Unknown3004(10)
    sprite('vrptef_env', 5)	# 16-20
    Unknown3004(0)
    sprite('vrptef_env', 20)	# 21-40
    Unknown1099(-100)
    Unknown3004(-20)

@State
def pt203_aura3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown3033()
        Unknown23015(2)
        Unknown1007(-11000)
        Unknown3001(0)
        Unknown1056(3200)
        Unknown1064(2000)
        Unknown3026(15091360)
    sprite('vrptef_env', 20)	# 1-20
    sprite('vrptef_env', 10)	# 21-30
    Unknown3004(18)
    sprite('vrptef_env', 10)	# 31-40
    Unknown3004(0)
    sprite('vrptef_env', 60)	# 41-100
    Unknown3004(-20)

@State
def pt203_airaura1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown3033()
        Unknown23015(5)
        Unknown1007(8000)
        Unknown1056(3000)
        Unknown1064(4200)
        Unknown3026(-1692514586)
    sprite('vrptef_env', 20)	# 1-20
    sprite('vrptef_env', 15)	# 21-35
    Unknown1099(-100)
    Unknown3004(-20)

@State
def pt203_airaura2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown3033()
        Unknown1007(-30000)
        Unknown1056(5400)
        Unknown1064(1400)
        Unknown3026(1347476590)
    sprite('vrptef_env', 20)	# 1-20
    sprite('vrptef_env', 20)	# 21-40
    Unknown1099(-100)
    Unknown3004(-20)

@State
def pt203_airaura3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        Unknown3033()
        Unknown1007(-11000)
        Unknown1056(3200)
        Unknown1064(2000)
        Unknown3026(1523724930)
    sprite('vrptef_env', 20)	# 1-20
    sprite('vrptef_env', 10)	# 21-30
    Unknown3004(-30)

@State
def pt203_mahojinsub():

    def upon_IMMEDIATE():
        GFX_2('ptef_203mahojin')
        Unknown3033()
        Unknown2054(1)
    sprite('null', 70)	# 1-70

@State
def pt203_stick():

    def upon_IMMEDIATE():
        GFX_2('ptef_203stick')
        Unknown3033()
        Unknown1096(750)
    sprite('null', 70)	# 1-70

@State
def yugami_ring():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown21010(1)
        Unknown1096(1400)
    sprite('vr_yugami', 5)	# 1-5
    Unknown1099(50)
    Unknown3057(1)
    Unknown3058(28000)
    sprite('vr_yugami', 8)	# 6-13
    Unknown1099(100)
    Unknown3059(-2800)

@State
def Atk5DHiWave():

    def upon_IMMEDIATE():
        GFX_2('ptef_dustB03')
        Unknown3033()
        Unknown3001(128)
    sprite('null', 60)	# 1-60

@State
def Atk5DHiquake():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        HitLow(100)
        HitOverhead(100)
        Unknown30069(1)
        Hitstop(0)
        AirPushbackX(6000)
        AirPushbackY(8000)
        Unknown9310(30)
        Unknown1056(4000)
    sprite('vrdmy_jishin', 1)	# 1-1
    SFX_0('019_quake_1')

@State
def Atk5DHiquake_Assist():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        HitLow(100)
        HitOverhead(100)
        Hitstop(0)
        AirPushbackX(6000)
        AirPushbackY(8000)
        Unknown9310(30)
        Unknown1056(4000)
        Unknown11042(1)
    sprite('vrdmy_jishin', 1)	# 1-1
    SFX_0('019_quake_1')

@State
def Bomb():

    def upon_IMMEDIATE():
        Unknown2010()
        AirUntechableTime(14)
        hitstun(17)
        Unknown3032()
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        Unknown2053(1)
        AttackLevel_(1)
        Damage(650)
        Hitstop(1)
        AttackP1(80)
        AttackP2(90)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1404):
                setGravity(1500)
                physicsXImpulse(1000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1401):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                setGravity(1500)
                physicsXImpulse(9000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1402):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                setGravity(1500)
                physicsXImpulse(5000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1403):
                Unknown2038(1)
                MinimumDamagePct(10)
                Unknown30065(0)
                setGravity(1500)
                physicsXImpulse(1000)
                physicsYImpulse(27000)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(0)

        def upon_LANDING():
            sendToLabel(1)

        def upon_44():
            sendToLabel(5)
    sprite('vrptef208_bomb00', 32767)	# 1-32767	 **attackbox here**
    GFX_0('BombSpark', 0)
    SFX_3('ptse_06')
    SFX_0('016_explode_0')
    SFX_3('ptse_01')
    label(0)
    sprite('vrptef208_bomb00', 2)	# 32768-32769	 **attackbox here**
    clearUponHandler(44)
    GFX_0('BombAttackFire', 1)
    if SLOT_2:
        Unknown23029(1, 1405, 0)
    SFX_3('ptse_26')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb00', 3)	# 32770-32772	 **attackbox here**
    Unknown1099(60)
    Unknown3004(-30)
    sprite('vrptef208_bomb00', 1)	# 32773-32773	 **attackbox here**
    gotoLabel(2)
    loopRest()
    label(1)
    sprite('vrptef208_bomb00', 2)	# 32774-32775	 **attackbox here**
    clearUponHandler(44)
    StartMultihit()
    GFX_0('BombFire', -1)
    if SLOT_2:
        Unknown23029(1, 1405, 0)
    SFX_3('ptse_26')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb00', 3)	# 32776-32778	 **attackbox here**
    StartMultihit()
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb00', 1)	# 32779-32779	 **attackbox here**
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(5)
    sprite('vrptef208_bomb00', 2)	# 32780-32781	 **attackbox here**
    clearUponHandler(44)
    StartMultihit()
    GFX_0('BombFire', -1)
    Unknown23029(1, 1304, 0)
    SFX_3('ptse_26')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb00', 3)	# 32782-32784	 **attackbox here**
    StartMultihit()
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb00', 1)	# 32785-32785	 **attackbox here**
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(2)
    sprite('null', 1)	# 32786-32786
    ExitState()

@State
def SpBomb():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(800)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(14)
        hitstun(17)
        Hitstop(1)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        Unknown3032()
        Unknown2053(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1404):
                setGravity(1500)
                physicsXImpulse(1000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1401):
                Unknown2038(1)
                MinimumDamagePct(10)
                Unknown30065(0)
                setGravity(1500)
                physicsXImpulse(9000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1402):
                Unknown2038(1)
                MinimumDamagePct(10)
                Unknown30065(0)
                setGravity(1500)
                physicsXImpulse(5000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1403):
                Unknown2038(1)
                MinimumDamagePct(10)
                Unknown30065(0)
                setGravity(1500)
                physicsXImpulse(1000)
                physicsYImpulse(27000)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(0)

        def upon_LANDING():
            sendToLabel(1)

        def upon_44():
            sendToLabel(5)
    sprite('vrptef208_bomb01', 32767)	# 1-32767	 **attackbox here**
    GFX_0('BombBigSpark', 0)
    SFX_3('ptse_06')
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    label(0)
    sprite('vrptef208_bomb01', 1)	# 32768-32768	 **attackbox here**
    clearUponHandler(44)
    GFX_0('SpAttackBombFire', 1)
    if SLOT_2:
        Unknown23029(1, 1405, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb01', 3)	# 32769-32771	 **attackbox here**
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb01', 1)	# 32772-32772	 **attackbox here**
    gotoLabel(2)
    loopRest()
    label(1)
    sprite('vrptef208_bomb01', 2)	# 32773-32774	 **attackbox here**
    clearUponHandler(44)
    StartMultihit()
    GFX_0('SpBombFire', -1)
    if SLOT_2:
        Unknown23029(1, 1405, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb01', 3)	# 32775-32777	 **attackbox here**
    StartMultihit()
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb01', 1)	# 32778-32778	 **attackbox here**
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(5)
    sprite('vrptef208_bomb01', 2)	# 32779-32780	 **attackbox here**
    clearUponHandler(44)
    StartMultihit()
    GFX_0('SpBombFire', -1)
    Unknown23029(1, 1304, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb01', 3)	# 32781-32783	 **attackbox here**
    StartMultihit()
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb01', 1)	# 32784-32784	 **attackbox here**
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(2)
    sprite('null', 1)	# 32785-32785

@State
def BombSpark():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4061(1)
        Unknown3033()
    label(15)
    sprite('vrptef208_bombspark00', 2)	# 1-2
    sprite('vrptef208_bombspark01', 2)	# 3-4
    gotoLabel(15)

@State
def BombBigSpark():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4061(1)
        Unknown3033()
    label(15)
    sprite('vrptef208_bombspark00', 2)	# 1-2
    sprite('vrptef208_bombspark01', 2)	# 3-4
    gotoLabel(15)

@State
def BombAttackFire():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(20000)
        Damage(1500)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(30)
        Unknown9017(1)

        def upon_43():
            if (SLOT_48 == 1405):
                Unknown30065(0)
                MinimumDamagePct(10)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    GFX_1('ptef_bombattackfire', 0)
    sprite('vrdmy_bombfire00', 15)	# 3-17

@State
def BombFire():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        Damage(1500)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(30)
        Unknown9017(1)

        def upon_43():
            if (SLOT_48 == 1304):
                Unknown2003(1)
            if (SLOT_48 == 1405):
                Unknown30065(0)
                MinimumDamagePct(10)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    GFX_1('ptef_bombDfire', 0)
    sprite('vrdmy_bombfire01', 15)	# 3-17

@State
def SpAttackBombFire():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1800)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        AirUntechableTime(30)
        AttackP1(80)
        AttackP2(90)
        Unknown9017(1)
        GFX_2('ptef_bombattackfire')

        def upon_43():
            if (SLOT_48 == 1405):
                Unknown30065(0)
                MinimumDamagePct(10)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    Unknown1096(1500)
    sprite('vrdmy_bombfire00', 15)	# 3-17

@State
def SpBombFire():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1800)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        AirUntechableTime(30)
        AttackP1(80)
        AttackP2(90)
        Unknown9017(1)
        GFX_2('ptef_bombattackfire')

        def upon_43():
            if (SLOT_48 == 1304):
                Unknown2003(1)
            if (SLOT_48 == 1405):
                Unknown30065(0)
                MinimumDamagePct(10)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    Unknown1096(1500)
    sprite('vrdmy_bombfire01', 15)	# 3-17

@State
def Bomb_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AirUntechableTime(14)
        hitstun(17)
        Unknown3032()
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        Unknown2053(1)
        AttackLevel_(1)
        Damage(650)
        Hitstop(1)
        AttackP1(70)
        AttackP2(90)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11042(1)

        def upon_43():
            if (SLOT_48 == 1401):
                setGravity(1500)
                physicsXImpulse(18000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1402):
                setGravity(1500)
                physicsXImpulse(11000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1403):
                setGravity(1500)
                physicsXImpulse(4000)
                physicsYImpulse(27000)

    def upon_ON_HIT_OR_BLOCK():
        sendToLabel(0)

    def upon_LANDING():
        sendToLabel(1)
    sprite('vrptef208_bomb00', 32767)	# 1-32767	 **attackbox here**
    GFX_0('BombSpark', 0)
    SFX_3('ptse_06')
    SFX_0('016_explode_0')
    SFX_3('ptse_01')
    label(0)
    sprite('vrptef208_bomb00', 2)	# 32768-32769	 **attackbox here**
    GFX_0('BombAttackFire_TAG', 1)
    SFX_3('ptse_26')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb00', 3)	# 32770-32772	 **attackbox here**
    Unknown1099(60)
    Unknown3004(-30)
    sprite('vrptef208_bomb00', 1)	# 32773-32773	 **attackbox here**
    gotoLabel(2)
    loopRest()
    label(1)
    sprite('vrptef208_bomb00', 2)	# 32774-32775	 **attackbox here**
    StartMultihit()
    GFX_0('BombFire_TAG', -1)
    SFX_3('ptse_26')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb00', 3)	# 32776-32778	 **attackbox here**
    StartMultihit()
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb00', 1)	# 32779-32779	 **attackbox here**
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(2)
    sprite('null', 1)	# 32780-32780

@State
def SpBomb_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(800)
        AttackP1(70)
        AttackP2(90)
        AirUntechableTime(14)
        hitstun(17)
        Hitstop(1)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        Unknown3032()
        Unknown2053(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11042(1)

        def upon_43():
            if (SLOT_48 == 1401):
                setGravity(1500)
                physicsXImpulse(18000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1402):
                setGravity(1500)
                physicsXImpulse(11000)
                physicsYImpulse(27000)
            if (SLOT_48 == 1403):
                setGravity(1500)
                physicsXImpulse(4000)
                physicsYImpulse(27000)

    def upon_ON_HIT_OR_BLOCK():
        sendToLabel(0)

    def upon_LANDING():
        sendToLabel(1)
    SLOT_59 = SLOT_4
    Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vrptef208_bomb01', 32767)	# 1-32767	 **attackbox here**
    GFX_0('BombBigSpark', 0)
    SFX_3('ptse_06')
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    label(0)
    sprite('vrptef208_bomb01', 1)	# 32768-32768	 **attackbox here**
    GFX_0('SpAttackBombFire_TAG', 1)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb01', 3)	# 32769-32771	 **attackbox here**
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb01', 1)	# 32772-32772	 **attackbox here**
    gotoLabel(2)
    loopRest()
    label(1)
    sprite('vrptef208_bomb01', 2)	# 32773-32774	 **attackbox here**
    StartMultihit()
    GFX_0('SpBombFire_TAG', -1)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_bomb01', 3)	# 32775-32777	 **attackbox here**
    StartMultihit()
    Unknown1099(60)
    Unknown3004(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb01', 1)	# 32778-32778	 **attackbox here**
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(2)
    sprite('null', 1)	# 32779-32779

@State
def BombAttackFire_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(20000)
        Damage(1500)
        AttackP1(70)
        AttackP2(90)
        AirUntechableTime(30)
        Unknown9017(1)
        Unknown11042(1)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    GFX_1('ptef_bombattackfire', 0)
    sprite('vrdmy_bombfire00', 15)	# 3-17

@State
def BombFire_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        Damage(1500)
        AttackP1(70)
        AttackP2(90)
        AirUntechableTime(30)
        Unknown9017(1)
        Unknown11042(1)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    GFX_1('ptef_bombDfire', 0)
    sprite('vrdmy_bombfire01', 15)	# 3-17

@State
def SpAttackBombFire_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1800)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        AirUntechableTime(30)
        AttackP1(70)
        AttackP2(90)
        Unknown9017(1)
        GFX_2('ptef_bombattackfire')
        Unknown11042(1)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    Unknown1096(1500)
    sprite('vrdmy_bombfire00', 15)	# 3-17

@State
def SpBombFire_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1800)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        AirUntechableTime(30)
        AttackP1(70)
        AttackP2(90)
        Unknown9017(1)
        GFX_2('ptef_bombattackfire')
        Unknown11042(1)
    sprite('vrdmy_bombfire00', 2)	# 1-2
    StartMultihit()
    Unknown1096(1500)
    sprite('vrdmy_bombfire01', 15)	# 3-17

@State
def Missile():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(650)
        AttackP1(80)
        AttackP2(90)
        PushbackX(10000)
        Hitstop(1)
        ProjectileDurabilityLvl(1)
        Unknown2053(0)
        Unknown53(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1301):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(0)
            if (SLOT_48 == 1302):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(1)
            if (SLOT_48 == 1303):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(2)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_44():
            sendToLabel(5)
    sprite('vrptef208_missile00', 150)	# 1-150	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    SFX_0('016_explode_0')
    SFX_3('ptse_01')
    Unknown1028(1500)
    SFX_3('ptse_06')
    loopRest()
    ExitState()
    label(0)
    sprite('vrptef208_missile00', 150)	# 151-300	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    Unknown1028(1500)
    SFX_3('ptse_06')
    loopRest()
    label(1)
    sprite('vrptef208_missile00', 20)	# 301-320	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 130)	# 321-450	 **attackbox here**
    Unknown1028(1500)
    SFX_3('ptse_06')
    loopRest()
    label(2)
    sprite('vrptef208_missile00', 40)	# 451-490	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 110)	# 491-600	 **attackbox here**
    Unknown1028(1500)
    SFX_3('ptse_06')
    loopRest()
    label(3)
    sprite('vrptef208_missile00', 2)	# 601-602	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('MissileFire', -1)
    if SLOT_2:
        Unknown23029(1, 1305, 0)
    if SLOT_51:
        Unknown23029(1, 1306, 0)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile00', 3)	# 603-605	 **attackbox here**
    Unknown1099(80)
    sprite('null', 1)	# 606-606
    ExitState()
    label(5)
    sprite('vrptef208_missile00', 2)	# 607-608	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('MissileFire', -1)
    Unknown23029(1, 1304, 0)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile00', 3)	# 609-611	 **attackbox here**
    Unknown1099(80)
    sprite('null', 1)	# 612-612
    ExitState()

@State
def MissileB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(650)
        AttackP1(80)
        AttackP2(90)
        PushbackX(10000)
        Hitstop(1)
        ProjectileDurabilityLvl(1)
        Unknown2053(0)
        Unknown53(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1301):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(0)
            if (SLOT_48 == 1302):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(1)
            if (SLOT_48 == 1303):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(2)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_44():
            sendToLabel(5)
    sprite('vrptef208_missile00', 30)	# 1-30	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    SFX_0('016_explode_0')
    SFX_3('ptse_01')
    sprite('vrptef208_missile00', 150)	# 31-180	 **attackbox here**
    Unknown1028(4000)
    SFX_3('ptse_06')
    loopRest()
    ExitState()
    label(0)
    sprite('vrptef208_missile00', 30)	# 181-210	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 150)	# 211-360	 **attackbox here**
    Unknown1028(4000)
    SFX_3('ptse_06')
    loopRest()
    label(1)
    sprite('vrptef208_missile00', 50)	# 361-410	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 130)	# 411-540	 **attackbox here**
    Unknown1028(4000)
    SFX_3('ptse_06')
    loopRest()
    label(2)
    sprite('vrptef208_missile00', 70)	# 541-610	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 110)	# 611-720	 **attackbox here**
    Unknown1028(4000)
    SFX_3('ptse_06')
    loopRest()
    label(3)
    sprite('vrptef208_missile00', 2)	# 721-722	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('MissileFire', -1)
    if SLOT_2:
        Unknown23029(1, 1305, 0)
    if SLOT_51:
        Unknown23029(1, 1306, 0)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile00', 3)	# 723-725	 **attackbox here**
    Unknown1099(80)
    sprite('null', 1)	# 726-726
    ExitState()
    label(5)
    sprite('vrptef208_missile00', 2)	# 727-728	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('MissileFire', -1)
    Unknown23029(1, 1304, 0)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile00', 3)	# 729-731	 **attackbox here**
    Unknown1099(80)
    sprite('null', 1)	# 732-732
    ExitState()

@State
def SpMissile():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        AttackP2(90)
        PushbackX(10000)
        Hitstop(1)
        ProjectileDurabilityLvl(1)
        teleportRelativeX(120000)
        Unknown53(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1301):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(0)
            if (SLOT_48 == 1302):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(1)
            if (SLOT_48 == 1303):
                Unknown2038(1)
                SLOT_51 = 1
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(2)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_44():
            sendToLabel(5)
    sprite('vrptef208_missile01', 120)	# 1-120	 **attackbox here**
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    physicsXImpulse(1800)
    Unknown1028(2000)
    SFX_0('016_explode_2')
    SFX_3('ptse_01')
    SFX_3('ptse_06')
    loopRest()
    ExitState()
    label(0)
    sprite('vrptef208_missile01', 120)	# 121-240	 **attackbox here**
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    physicsXImpulse(1800)
    Unknown1028(3000)
    loopRest()
    ExitState()
    label(1)
    sprite('vrptef208_missile01', 120)	# 241-360	 **attackbox here**
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    physicsXImpulse(1800)
    Unknown1028(3000)
    loopRest()
    ExitState()
    label(2)
    sprite('vrptef208_missile01', 120)	# 361-480	 **attackbox here**
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    physicsXImpulse(1800)
    Unknown1028(3000)
    loopRest()
    ExitState()
    label(3)
    sprite('vrptef208_missile01', 1)	# 481-481	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('SpMissileFire', 3)
    if SLOT_2:
        Unknown23029(1, 1305, 0)
    if SLOT_51:
        Unknown23029(1, 1306, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile01', 3)	# 482-484	 **attackbox here**
    Unknown1099(80)
    ExitState()
    label(5)
    sprite('vrptef208_missile01', 1)	# 485-485	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('SpMissileFire', 3)
    Unknown23029(1, 1304, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile01', 3)	# 486-488	 **attackbox here**
    Unknown1099(80)

@State
def SpMissileB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        AttackP2(90)
        PushbackX(10000)
        Hitstop(1)
        ProjectileDurabilityLvl(1)
        teleportRelativeX(120000)
        Unknown53(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1301):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(0)
            if (SLOT_48 == 1302):
                Unknown2038(1)
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(1)
            if (SLOT_48 == 1303):
                Unknown2038(1)
                SLOT_51 = 1
                Unknown30065(0)
                MinimumDamagePct(10)
                sendToLabel(2)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_44():
            sendToLabel(5)
    sprite('vrptef208_missile01', 30)	# 1-30	 **attackbox here**
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    physicsXImpulse(1800)
    SFX_0('016_explode_2')
    SFX_3('ptse_01')
    sprite('vrptef208_missile01', 120)	# 31-150	 **attackbox here**
    Unknown1028(4800)
    SFX_3('ptse_06')
    loopRest()
    ExitState()
    label(0)
    sprite('vrptef208_missile01', 30)	# 151-180	 **attackbox here**
    physicsXImpulse(60000)
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)	# 181-240	 **attackbox here**
    Unknown1028(4000)
    loopRest()
    label(1)
    sprite('vrptef208_missile01', 30)	# 241-270	 **attackbox here**
    physicsXImpulse(60000)
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)	# 271-330	 **attackbox here**
    Unknown1028(4000)
    loopRest()
    label(2)
    sprite('vrptef208_missile01', 10)	# 331-340	 **attackbox here**
    physicsXImpulse(60000)
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)	# 341-400	 **attackbox here**
    Unknown1028(4000)
    loopRest()
    label(3)
    sprite('vrptef208_missile01', 1)	# 401-401	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('SpMissileFire', 3)
    if SLOT_2:
        Unknown23029(1, 1305, 0)
    if SLOT_51:
        Unknown23029(1, 1306, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile01', 3)	# 402-404	 **attackbox here**
    Unknown1099(80)
    ExitState()
    label(5)
    sprite('vrptef208_missile01', 1)	# 405-405	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('SpMissileFire', 3)
    Unknown23029(1, 1304, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile01', 3)	# 406-408	 **attackbox here**
    Unknown1099(80)

@State
def MissileFire():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1500)
        AttackP1(80)
        AttackP2(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(25000)
        AirUntechableTime(30)
        Hitstop(0)
        ProjectileDurabilityLvl(1)
        Unknown9017(1)

        def upon_43():
            if (SLOT_48 == 1305):
                AirPushbackX(5000)
                AirPushbackY(25000)
                YImpluseBeforeWallbounce(1800)
                Unknown30065(0)
                MinimumDamagePct(10)
            if (SLOT_48 == 1306):
                AirPushbackY(25000)
                YImpluseBeforeWallbounce(2000)
                AirUntechableTime(20)
            if (SLOT_48 == 1304):
                Unknown2003(1)
    sprite('vrdmy_bombfire02', 10)	# 1-10
    GFX_1('ptef_missileattackfire', 0)

@State
def SpMissileFire():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(80)
        AttackP2(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(25000)
        AirUntechableTime(30)
        Hitstop(0)
        ProjectileDurabilityLvl(1)
        Unknown9017(1)
        GFX_2('ptef_missileattackfire')

        def upon_43():
            if (SLOT_48 == 1305):
                AirPushbackX(5000)
                AirPushbackY(20000)
                YImpluseBeforeWallbounce(1800)
                Unknown11001(5, 0, 2)
                PushbackX(9000)
                Hitstop(5)
                AirUntechableTime(50)
                Unknown30065(0)
                MinimumDamagePct(10)
            if (SLOT_48 == 1306):
                PushbackX(19800)
            if (SLOT_48 == 1304):
                Unknown2003(1)
    sprite('vrdmy_bombfire02', 10)	# 1-10
    Unknown1096(1500)
    sprite('vrdmy_bombfire02', 35)	# 11-45
    StartMultihit()

@State
def Missile_TAG():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(650)
        AttackP1(70)
        AttackP2(90)
        PushbackX(10000)
        Hitstop(1)
        ProjectileDurabilityLvl(1)
        MinimumDamagePct(5)
        ChipDamagePct(5)
        Unknown53(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1301):
                sendToLabel(0)
            if (SLOT_48 == 1302):
                sendToLabel(1)
            if (SLOT_48 == 1303):
                sendToLabel(2)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_44():
            sendToLabel(5)
        Unknown11042(1)
    sprite('vrptef208_missile00', 150)	# 1-150	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    SFX_0('016_explode_0')
    SFX_3('ptse_01')
    Unknown1028(1500)
    SFX_3('ptse_06')
    loopRest()
    ExitState()
    label(0)
    sprite('vrptef208_missile00', 30)	# 151-180	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 150)	# 181-330	 **attackbox here**
    Unknown1028(4000)
    SFX_3('ptse_06')
    loopRest()
    label(1)
    sprite('vrptef208_missile00', 20)	# 331-350	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 130)	# 351-480	 **attackbox here**
    Unknown1028(4000)
    SFX_3('ptse_06')
    loopRest()
    label(2)
    sprite('vrptef208_missile00', 40)	# 481-520	 **attackbox here**
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 110)	# 521-630	 **attackbox here**
    Unknown1028(1500)
    SFX_3('ptse_06')
    loopRest()
    label(3)
    sprite('vrptef208_missile00', 2)	# 631-632	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('MissileFire_TAG', -1)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile00', 3)	# 633-635	 **attackbox here**
    Unknown1099(80)
    sprite('null', 1)	# 636-636
    ExitState()
    label(5)
    sprite('vrptef208_missile00', 2)	# 637-638	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('MissileFire', -1)
    Unknown23029(1, 1304, 0)
    SFX_0('016_explode_1')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile00', 3)	# 639-641	 **attackbox here**
    Unknown1099(80)
    sprite('null', 1)	# 642-642
    ExitState()

@State
def SpMissile_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(800)
        AttackP1(70)
        AttackP2(90)
        PushbackX(10000)
        Hitstop(1)
        ProjectileDurabilityLvl(1)
        teleportRelativeX(120000)
        Unknown53(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 1301):
                sendToLabel(0)
            if (SLOT_48 == 1302):
                sendToLabel(1)
            if (SLOT_48 == 1303):
                sendToLabel(2)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_44():
            sendToLabel(5)
        Unknown11042(1)
    sprite('vrptef208_missile01', 120)	# 1-120	 **attackbox here**
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    physicsXImpulse(1800)
    Unknown1028(2000)
    SFX_0('016_explode_2')
    SFX_3('ptse_01')
    SFX_3('ptse_06')
    loopRest()
    ExitState()
    label(0)
    sprite('vrptef208_missile01', 30)	# 121-150	 **attackbox here**
    physicsXImpulse(60000)
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)	# 151-210	 **attackbox here**
    Unknown1028(4000)
    loopRest()
    label(1)
    sprite('vrptef208_missile01', 30)	# 211-240	 **attackbox here**
    physicsXImpulse(60000)
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)	# 241-300	 **attackbox here**
    Unknown1028(4000)
    loopRest()
    label(2)
    sprite('vrptef208_missile01', 10)	# 301-310	 **attackbox here**
    physicsXImpulse(60000)
    GFX_0('MissileBackfire_front', 0)
    GFX_0('MissileBackfire_front', 1)
    GFX_0('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)	# 311-370	 **attackbox here**
    Unknown1028(4000)
    loopRest()
    label(3)
    sprite('vrptef208_missile01', 1)	# 371-371	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('SpMissileFire', 3)
    if SLOT_2:
        Unknown23029(1, 1305, 0)
    if SLOT_51:
        Unknown23029(1, 1306, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile01', 3)	# 372-374	 **attackbox here**
    Unknown1099(80)
    ExitState()
    label(5)
    sprite('vrptef208_missile01', 1)	# 375-375	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    GFX_0('SpMissileFire', 3)
    Unknown23029(1, 1304, 0)
    SFX_0('016_explode_2')
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1099(-30)
    sprite('vrptef208_missile01', 3)	# 376-378	 **attackbox here**
    Unknown1099(80)

@State
def MissileFire_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1500)
        AttackP1(70)
        AttackP2(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(25000)
        AirUntechableTime(30)
        Hitstop(0)
        ProjectileDurabilityLvl(1)
        Unknown9017(1)
        Unknown11042(1)
    sprite('vrdmy_bombfire02', 10)	# 1-10
    GFX_1('ptef_missileattackfire', 0)

@State
def SpMissileFire_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(70)
        AttackP2(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(25000)
        AirUntechableTime(30)
        Hitstop(0)
        ProjectileDurabilityLvl(1)
        Unknown9017(1)
        GFX_2('ptef_missileattackfire')
        Unknown11042(1)
    sprite('vrdmy_bombfire02', 10)	# 1-10
    Unknown1096(1500)
    sprite('vrdmy_bombfire02', 35)	# 11-45
    StartMultihit()

@State
def MissileBackfire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1096(1200)
    sprite('vrptef208_missilefire00', 3)	# 1-3
    sprite('vrptef208_missilefire01', 3)	# 4-6
    GFX_1('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)	# 7-9
    sprite('vrptef208_missilefire00', 3)	# 10-12
    sprite('vrptef208_missilefire01', 3)	# 13-15
    sprite('vrptef208_missilefire02', 3)	# 16-18
    sprite('vrptef208_missilefire00', 3)	# 19-21
    sprite('vrptef208_missilefire01', 3)	# 22-24
    sprite('vrptef208_missilefire02', 3)	# 25-27
    label(15)
    sprite('vrptef208_missilefire00', 3)	# 28-30
    GFX_1('ptef430charge', -1)
    sprite('vrptef208_missilefire01', 3)	# 31-33
    GFX_1('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)	# 34-36
    GFX_1('ptef430charge', -1)
    gotoLabel(15)

@State
def MissileBackfire_front():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1096(1200)
    label(15)
    sprite('vrptef208_missilefire00', 3)	# 1-3
    GFX_1('ptef430charge', -1)
    sprite('vrptef208_missilefire01', 3)	# 4-6
    GFX_1('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)	# 7-9
    GFX_1('ptef430charge', -1)
    gotoLabel(15)

@State
def MissileBackfire_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1096(800)
    label(15)
    sprite('vrptef208_missilefire00', 3)	# 1-3
    GFX_1('ptef430charge', -1)
    sprite('vrptef208_missilefire01', 3)	# 4-6
    GFX_1('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)	# 7-9
    GFX_1('ptef430charge', -1)
    gotoLabel(15)

@State
def Trap():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown2053(1)
        Unknown3032()
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2003(1)
        Unknown23089('0100000000000000000000000100000000000000000000000100000000000000')

        def upon_54():
            sendToLabel(2)
            clearUponHandler(54)
            clearUponHandler(2)
        Unknown23022(1)
        Unknown23020(1100)
        Unknown23021(1100)
        sendToLabelUpon(19, 3)
        loopRelated(17, 300)
        sendToLabelUpon(17, 3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if (SLOT_19 < 150000):
                    clearUponHandler(3)
                    sendToLabel(1)
        sendToLabelUpon(2, 0)
        sendToLabelUpon(32, 2)
        sendToLabelUpon(53, 2)
    sprite('vrptef209_box00', 32767)	# 1-32767
    sendToLabelUpon(33, 10)
    sendToLabelUpon(34, 20)
    sendToLabelUpon(35, 30)
    label(10)
    sprite('vrptef209_box00', 10)	# 32768-32777
    sprite('vrptef209_box00', 32767)	# 32778-65544
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    setGravity(1500)
    loopRest()
    label(20)
    sprite('vrptef209_box00', 32767)	# 65545-98311
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    physicsXImpulse(14000)
    physicsYImpulse(18000)
    setGravity(1500)
    loopRest()
    label(30)
    sprite('vrptef209_box00', 32767)	# 98312-131078
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    physicsXImpulse(500)
    physicsYImpulse(20000)
    setGravity(1500)
    loopRest()
    label(0)
    sprite('vrptef209_box00', 2)	# 131079-131080
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown1099(-30)
    Unknown23022(0)
    sprite('vrptef209_box00', 3)	# 131081-131083
    sprite('vrptef209_box00', 1)	# 131084-131084
    Unknown1099(0)
    Unknown2037(1)
    loopRest()
    sprite('vrptef209_box00', 719)	# 131085-131803
    sprite('vrptef209_box00', 1)	# 131804-131804
    gotoLabel(2)
    label(1)
    sprite('vrptef209_box00', 2)	# 131805-131806
    Unknown23022(1)
    sprite('null', 1)	# 131807-131807
    GFX_0('TrapAttack', 1)
    loopRest()
    ExitState()
    label(2)
    sprite('vrptef209_box00', 2)	# 131808-131809
    Unknown23022(1)
    clearUponHandler(3)
    Unknown1084(1)
    Unknown3004(-10)
    sprite('vrptef209_box00', 10)	# 131810-131819
    sprite('vrptef209_box00', 10)	# 131820-131829
    sprite('vrptef209_box00', 10)	# 131830-131839
    loopRest()
    ExitState()
    label(3)
    sprite('vrptef209_box01', 10)	# 131840-131849
    Unknown23022(1)
    Unknown1084(1)
    clearUponHandler(3)
    clearUponHandler(2)
    clearUponHandler(54)
    clearUponHandler(17)
    SFX_3('ptse_02')
    GFX_1('ptef_boxbom', 0)
    Unknown3004(-15)
    sprite('vrptef209_box00', 10)	# 131850-131859

@State
def TrapAttack():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(40000)
        Damage(1100)
        AttackP1(70)
        AirUntechableTime(55)
        Unknown11042(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vrptef209_box01', 2)	# 1-2
    SFX_3('ptse_08')
    SFX_3('ptse_02')
    StartMultihit()
    sprite('vrptef209_box02', 5)	# 3-7	 **attackbox here**
    GFX_1('ptef_boxbom', 0)
    GFX_0('spring_01', -1)
    sprite('vrptef209_box03', 5)	# 8-12	 **attackbox here**
    GFX_0('spring_02', -1)
    sprite('vrptef209_box04', 5)	# 13-17	 **attackbox here**
    GFX_0('spring_03', -1)
    sprite('vrptef209_box05', 5)	# 18-22	 **attackbox here**
    GFX_0('spring_04', -1)
    sprite('vrptef209_box06', 5)	# 23-27
    sprite('vrptef209_box07', 10)	# 28-37
    Unknown3004(-25)
    Unknown21012('737072696e675f3034000000000000000000000000000000000000000000000020000000')
    sprite('vrptef209_box07', 10)	# 38-47

@State
def spring_01():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        teleportRelativeX(10000)
        Unknown1007(50000)
    sprite('vrptef209_spring01', 5)	# 1-5

@State
def spring_02():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        teleportRelativeX(10000)
        Unknown1007(50000)
    sprite('vrptef209_spring02', 5)	# 1-5

@State
def spring_03():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        teleportRelativeX(10000)
        Unknown1007(50000)
    sprite('vrptef209_spring03', 5)	# 1-5

@State
def spring_04():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        teleportRelativeX(10000)
        Unknown1007(50000)
        sendToLabelUpon(32, 1)
    sprite('vrptef209_spring02', 32767)	# 1-32767
    label(1)
    sprite('vrptef209_spring02', 8)	# 32768-32775
    Unknown3004(-31)

@State
def SpTrap():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackP1(70)
        Damage(1000)
        Hitstop(5)
        AirPushbackY(50000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown2053(1)
        Unknown3032()
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2003(1)
        Unknown23022(1)
        Unknown23020(1600)
        Unknown23021(1600)
        sendToLabelUpon(19, 3)
        loopRelated(17, 300)
        sendToLabelUpon(17, 3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if (SLOT_19 < 200000):
                    clearUponHandler(3)
                    sendToLabel(1)
        sendToLabelUpon(2, 0)
        sendToLabelUpon(32, 2)
        sendToLabelUpon(53, 2)
    sprite('vrptef209_spbox00', 32767)	# 1-32767
    sendToLabelUpon(33, 10)
    sendToLabelUpon(34, 20)
    sendToLabelUpon(35, 30)
    label(10)
    sprite('vrptef209_spbox00', 10)	# 32768-32777
    sprite('vrptef209_spbox00', 32767)	# 32778-65544
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    setGravity(1500)
    loopRest()
    label(20)
    sprite('vrptef209_spbox00', 32767)	# 65545-98311
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    physicsXImpulse(14000)
    physicsYImpulse(18000)
    setGravity(1500)
    loopRest()
    label(30)
    sprite('vrptef209_spbox00', 32767)	# 98312-131078
    SFX_3('ptse_01')
    SFX_0('016_explode_0')
    physicsXImpulse(500)
    physicsYImpulse(20000)
    setGravity(1500)
    loopRest()
    label(0)
    sprite('vrptef209_spbox00', 2)	# 131079-131080
    teleportRelativeY(0)
    Unknown1084(1)
    Unknown1099(-30)
    Unknown23022(0)
    sprite('vrptef209_spbox00', 3)	# 131081-131083
    sprite('vrptef209_spbox00', 1)	# 131084-131084
    Unknown1099(0)
    Unknown2037(1)
    loopRest()
    sprite('vrptef209_spbox00', 959)	# 131085-132043
    sprite('vrptef209_spbox00', 1)	# 132044-132044
    gotoLabel(2)
    label(1)
    sprite('vrptef209_spbox00', 2)	# 132045-132046
    Unknown23022(1)
    SFX_0('016_explode_2')
    Unknown1099(300)
    sprite('null', 3)	# 132047-132049
    RefreshMultihit()
    GFX_0('Kemuri3', 1)
    GFX_0('SpTrapAttack', 1)
    ExitState()
    label(2)
    sprite('vrptef209_spbox00', 2)	# 132050-132051
    Unknown23022(1)
    clearUponHandler(3)
    Unknown1084(1)
    Unknown3004(-10)
    sprite('vrptef209_spbox00', 10)	# 132052-132061
    sprite('vrptef209_spbox00', 10)	# 132062-132071
    sprite('vrptef209_spbox00', 10)	# 132072-132081
    loopRest()
    ExitState()
    label(3)
    sprite('vrptef209_spbox01', 10)	# 132082-132091
    Unknown23022(1)
    Unknown1084(1)
    clearUponHandler(3)
    clearUponHandler(2)
    clearUponHandler(54)
    clearUponHandler(17)
    SFX_3('ptse_02')
    GFX_1('ptef_boxbom', 0)
    Unknown3004(-15)
    sprite('vrptef209_spbox00', 10)	# 132092-132101

@State
def SpTrapAttack():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(70)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(50000)
        AirUntechableTime(55)
        MinimumDamagePct(20)
        Unknown11042(1)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vrptef209_spbox01', 2)	# 1-2
    SFX_3('ptse_08')
    SFX_3('ptse_24')
    StartMultihit()
    sprite('vrptef209_spbox02', 5)	# 3-7	 **attackbox here**
    GFX_1('ptef_boxbom', 0)
    GFX_0('SPspring_01', -1)
    GFX_0('spbox_parts01', -1)
    GFX_0('spbox_parts02', -1)
    sprite('vrptef209_spbox03', 5)	# 8-12	 **attackbox here**
    GFX_0('SPspring_02', -1)
    sprite('vrptef209_spbox04', 5)	# 13-17	 **attackbox here**
    GFX_0('SPspring_03', -1)
    sprite('vrptef209_spbox05', 5)	# 18-22	 **attackbox here**
    GFX_0('SPspring_04', -1)
    sprite('vrptef209_spbox06', 5)	# 23-27	 **attackbox here**
    sprite('vrptef209_spbox07', 10)	# 28-37	 **attackbox here**
    Unknown3004(-25)
    Unknown21012('5350737072696e675f303400000000000000000000000000000000000000000020000000')
    GFX_0('pt209_neko_rocket', -1)
    sprite('null', 30)	# 38-67

@State
def spbox_parts01():

    def upon_IMMEDIATE():
        Unknown2009()
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vrptef209_spbox_parts01', 20)	# 1-20
    Unknown3004(-12)
    physicsXImpulse(10000)
    physicsYImpulse(30000)
    Unknown1043()

@State
def spbox_parts02():

    def upon_IMMEDIATE():
        Unknown2009()
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vrptef209_spbox_parts02', 20)	# 1-20
    Unknown3004(-12)
    physicsXImpulse(-10000)
    physicsYImpulse(15000)
    Unknown1043()

@State
def SPspring_01():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        Unknown1096(1200)
        teleportRelativeX(10000)
        Unknown1007(50000)
    sprite('vrptef209_spring01', 5)	# 1-5

@State
def SPspring_02():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        Unknown1096(1200)
        teleportRelativeX(10000)
        Unknown1007(50000)
    sprite('vrptef209_spring02', 5)	# 1-5

@State
def SPspring_03():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        Unknown1096(1200)
        teleportRelativeX(10000)
        Unknown1007(50000)
    sprite('vrptef209_spring03', 5)	# 1-5

@State
def SPspring_04():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown2020(1)
        Unknown1096(1200)
        teleportRelativeX(10000)
        Unknown1007(50000)
        sendToLabelUpon(32, 1)
    sprite('vrptef209_spring02', 32767)	# 1-32767
    label(1)
    sprite('vrptef209_spring02', 8)	# 32768-32775
    Unknown3004(-31)

@State
def pt209_neko_rocket():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown3032()
        Unknown4061(0)
        Unknown1007(52000)
        AttackLevel_(3)
        AttackP1(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(50000)
        Damage(800)
        AirUntechableTime(55)
    sprite('vrptef209_neko_rocket', 2)	# 1-2	 **attackbox here**
    teleportRelativeX(10000)
    sprite('vrptef209_neko_rocket', 2)	# 3-4	 **attackbox here**
    teleportRelativeX(-20000)
    sprite('vrptef209_neko_rocket', 2)	# 5-6	 **attackbox here**
    teleportRelativeX(20000)
    sprite('vrptef209_neko_rocket', 2)	# 7-8	 **attackbox here**
    teleportRelativeX(-20000)
    sprite('vrptef209_neko_rocket', 2)	# 9-10	 **attackbox here**
    teleportRelativeX(20000)
    sprite('vrptef209_neko_rocket', 2)	# 11-12	 **attackbox here**
    teleportRelativeX(-20000)
    sprite('vrptef209_neko_rocket', 5)	# 13-17	 **attackbox here**
    SFX_3('ptse_06')
    physicsYImpulse(-1000)
    sprite('vrptef209_neko_rocket', 5)	# 18-22	 **attackbox here**
    physicsYImpulse(7000)
    GFX_0('pt209_neko_Backfire', 0)
    GFX_0('pt209_neko_Backfire', 1)
    GFX_0('pt209_neko_Backfire', 2)
    sprite('vrptef209_neko_rocket', 5)	# 23-27	 **attackbox here**
    YAccel(300)
    sprite('vrptef209_neko_rocket', 45)	# 28-72	 **attackbox here**
    YAccel(300)

@State
def pt209_neko_Backfire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1056(800)
        Unknown1064(1200)
        Unknown3001(223)
        Unknown1072(-90000)
        Unknown1007(-57000)
        teleportRelativeX(-3000)
        GFX_2('ptef209_rocket_firering')
    label(0)
    sprite('vrptef208_missilefire00', 3)	# 1-3
    GFX_1('ptef209_rocket', -1)
    sprite('vrptef208_missilefire01', 3)	# 4-6
    GFX_1('ptef209_rocket', -1)
    sprite('vrptef208_missilefire02', 3)	# 7-9
    GFX_1('ptef209_rocket', -1)
    gotoLabel(0)

@State
def pt_box():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
    sprite('vrptef209_box00', 32767)	# 1-32767
    Unknown1007(224000)
    teleportRelativeX(224000)
    setGravity(1500)
    GFX_1('ptef_drivethrow', -1)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('vrptef209_box00', 30)	# 32768-32797
    setGravity(0)
    physicsYImpulse(0)
    sprite('vrptef209_box01', 3)	# 32798-32800
    sprite('vrptef209_box02', 3)	# 32801-32803	 **attackbox here**
    GFX_1('ptef_boxbom', 0)
    sprite('vrptef209_box03', 3)	# 32804-32806	 **attackbox here**
    sprite('vrptef209_box04', 3)	# 32807-32809	 **attackbox here**
    sprite('vrptef209_box05', 3)	# 32810-32812	 **attackbox here**
    sprite('vrptef209_box06', 3)	# 32813-32815
    sprite('vrptef209_box07', 3)	# 32816-32818
    sprite('vrptef209_box07', 32)	# 32819-32850
    Unknown3004(-8)

@State
def pt_box2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
    sprite('vrptef209_spbox00', 32767)	# 1-32767
    Unknown1007(224000)
    teleportRelativeX(224000)
    setGravity(1500)
    GFX_1('ptef_drivethrow', -1)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('vrptef209_spbox00', 30)	# 32768-32797
    setGravity(0)
    physicsYImpulse(0)
    sprite('vrptef209_spbox01', 3)	# 32798-32800
    sprite('vrptef209_spbox02', 3)	# 32801-32803	 **attackbox here**
    GFX_1('ptef_boxbom', 0)
    sprite('vrptef209_spbox03', 3)	# 32804-32806	 **attackbox here**
    sprite('vrptef209_spbox04', 3)	# 32807-32809	 **attackbox here**
    sprite('vrptef209_spbox05', 3)	# 32810-32812	 **attackbox here**
    sprite('vrptef209_spbox06', 3)	# 32813-32815	 **attackbox here**
    sprite('vrptef209_spbox07', 32)	# 32816-32847	 **attackbox here**
    Unknown3004(-8)

@State
def AirSlideMcirle():

    def upon_IMMEDIATE():
        Unknown4010(3)
        GFX_2('ptef_airspecialmc')
        Unknown3033()
    sprite('null', 20)	# 1-20
    Unknown1007(200000)

@State
def AirSlideBalloon():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown3032()
    sprite('vrptef401_03', 2)	# 1-2
    Unknown3001(220)
    GFX_1('ptef_401balloonlight', 0)
    GFX_1('ptef_401balloonlight', 1)
    GFX_1('ptef_401balloonlight', 2)
    GFX_1('ptef_401balloonwave', 1)
    sprite('vrptef401_04', 2)	# 3-4
    sprite('vrptef401_05', 4)	# 5-8

@State
def AssaultAwave():

    def upon_IMMEDIATE():
        Unknown4010(3)
        GFX_2('ptef_403attack')
        Unknown3033()
    sprite('null', 3)	# 1-3
    Unknown1072(20000)
    Unknown4007(2)
    sprite('null', 30)	# 4-33
    Unknown4007(0)

@State
def AssaultBwave():

    def upon_IMMEDIATE():
        Unknown4010(3)
        GFX_2('ptef_403attack')
        Unknown3033()
    sprite('null', 3)	# 1-3
    Unknown1072(-20000)
    Unknown4007(2)
    sprite('null', 30)	# 4-33
    Unknown4007(0)

@State
def AssaultCwave():

    def upon_IMMEDIATE():
        Unknown4010(3)
        GFX_2('ptef_403attack')
        Unknown3033()
    sprite('null', 3)	# 1-3
    Unknown1072(70000)
    Unknown4007(2)
    sprite('null', 30)	# 4-33
    Unknown4007(0)

@State
def CommandThrowMcircle():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6b6f75736f6b75636972636c652e44494700000000000000000000707465665f6b6f75736f6b75636972636c655f6d6f74696f6e5f3030302e6d00')
        Unknown4015()
        Unknown3033()
        Unknown1096(1100)
        Unknown1007(-40000)
        sendToLabelUpon(32, 12)
    sprite('null', 30)	# 1-30
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 440)	# 31-470
    Unknown3001(255)
    label(12)
    sprite('null', 10)	# 471-480
    Unknown3004(-30)
    Unknown1099(25)

@State
def CommandThrowHeart():

    def upon_IMMEDIATE():
        Unknown4009(22)
        Unknown3032()
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vrptef404_00', 3)	# 1-3
    sprite('vrptef404_01', 3)	# 4-6
    sprite('vrptef404_02', 51)	# 7-57
    sprite('vrptef404_02', 6)	# 58-63
    Unknown23119(16777215, 6, 2)

@State
def CommandThrowRod():

    def upon_IMMEDIATE():
        Unknown3032()
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vrptef404_03', 4)	# 1-4
    Unknown3001(255)
    Unknown23118(16777215)
    Unknown23119(0, 4, 1)
    sprite('vrptef404_03', 1)	# 5-5

@State
def FakeDoll():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(100)
        Unknown11089(10)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(100)
        Unknown9310(10)
        Unknown11043(1000)
        Unknown11106(0)
        Unknown11084(1)
        Unknown11066(1)
        Unknown11064(1)
        Unknown11050('06000000707465665f6869745f6c6f770000000000000000000000000000000000000000')
        setInvincible(1)

        def upon_ON_HIT_OR_BLOCK():
            DisableAttackRestOfMove()
    sprite('null', 1)	# 1-1
    if Unknown42('ha'):
        if random_(2, 0, 35):
            gotoLabel(11)
        gotoLabel(10)
    if Unknown42('rg'):
        if random_(2, 0, 35):
            gotoLabel(12)
        gotoLabel(10)
    if Unknown42('hz'):
        if random_(2, 0, 35):
            gotoLabel(13)
        gotoLabel(10)
    if Unknown42('bn'):
        if random_(2, 0, 35):
            gotoLabel(14)
        gotoLabel(10)
    if Unknown42('ar'):
        if random_(2, 0, 55):
            gotoLabel(10)
        if random_(2, 0, 60):
            gotoLabel(15)
        if random_(2, 0, 60):
            gotoLabel(16)
        gotoLabel(17)
    gotoLabel(10)
    loopRest()
    label(10)
    sprite('vrptef406_00', 15)	# 2-16	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 20)
    sprite('vrptef406_00', 32767)	# 17-32783	 **attackbox here**
    RefreshMultihit()
    label(20)
    sprite('vrptef406_00', 10)	# 32784-32793	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_00', 5)	# 32794-32798	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_00', 1)	# 32799-32799	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(11)
    sprite('vrptef406_01', 15)	# 32800-32814	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 21)
    sprite('vrptef406_01', 32767)	# 32815-65581	 **attackbox here**
    RefreshMultihit()
    label(21)
    sprite('vrptef406_01', 10)	# 65582-65591	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_01', 5)	# 65592-65596	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_01', 1)	# 65597-65597	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(12)
    sprite('vrptef406_02', 15)	# 65598-65612	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 22)
    sprite('vrptef406_02', 32767)	# 65613-98379	 **attackbox here**
    RefreshMultihit()
    label(22)
    sprite('vrptef406_02', 10)	# 98380-98389	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_02', 5)	# 98390-98394	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_02', 1)	# 98395-98395	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(13)
    sprite('vrptef406_03', 15)	# 98396-98410	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 23)
    sprite('vrptef406_03', 32767)	# 98411-131177	 **attackbox here**
    RefreshMultihit()
    label(23)
    sprite('vrptef406_03', 10)	# 131178-131187	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_03', 5)	# 131188-131192	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_03', 1)	# 131193-131193	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(14)
    sprite('vrptef406_04', 15)	# 131194-131208	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 24)
    sprite('vrptef406_04', 32767)	# 131209-163975	 **attackbox here**
    RefreshMultihit()
    label(24)
    sprite('vrptef406_04', 10)	# 163976-163985	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_04', 5)	# 163986-163990	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_04', 1)	# 163991-163991	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(15)
    sprite('vrptef406_05', 15)	# 163992-164006	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 25)
    sprite('vrptef406_05', 32767)	# 164007-196773	 **attackbox here**
    RefreshMultihit()
    label(25)
    sprite('vrptef406_05', 10)	# 196774-196783	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_05', 5)	# 196784-196788	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_05', 1)	# 196789-196789	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(16)
    sprite('vrptef406_06', 15)	# 196790-196804	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 26)
    sprite('vrptef406_06', 32767)	# 196805-229571	 **attackbox here**
    RefreshMultihit()
    label(26)
    sprite('vrptef406_06', 10)	# 229572-229581	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_06', 5)	# 229582-229586	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_06', 1)	# 229587-229587	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(17)
    sprite('vrptef406_07', 15)	# 229588-229602	 **attackbox here**
    teleportRelativeY(75000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    StartMultihit()
    Unknown1028(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 27)
    sprite('vrptef406_07', 32767)	# 229603-262369	 **attackbox here**
    RefreshMultihit()
    label(27)
    sprite('vrptef406_07', 10)	# 262370-262379	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_07', 5)	# 262380-262384	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_07', 1)	# 262385-262385	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)

@State
def Atemi_Smoke():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('null', 1)	# 1-1
    Unknown1007(150000)
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_leaf', -1)
    loopRest()

@State
def DollMaker():

    def upon_IMMEDIATE():
        Unknown23056('')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 8)	# 1-8
    GFX_0('AttackDoll1', -1)
    sprite('null', 7)	# 9-15
    sprite('null', 8)	# 16-23
    GFX_0('AttackDoll1', -1)
    sprite('null', 8)	# 24-31
    GFX_0('AttackDoll1', -1)
    sprite('null', 8)	# 32-39
    GFX_0('AttackDoll1', -1)
    sprite('null', 8)	# 40-47
    GFX_0('AttackDoll1', -1)
    sprite('null', 8)	# 48-55
    GFX_0('AttackDoll1', -1)
    sprite('null', 8)	# 56-63
    GFX_0('AttackDoll1', -1)
    label(0)
    sprite('null', 120)	# 64-183
    clearUponHandler(32)

@State
def AttackDoll1():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown1086(22)
        teleportRelativeX(-15000)
        Unknown1007(500000)
        Damage(400)
        AirPushbackY(15000)
        AirUntechableTime(100)
        AttackP1(48)
        AttackP2(100)
        MinimumDamagePct(15)
        Hitstop(0)
        Unknown23182(2)
        Unknown11050('06000000707465665f6869745f6c6f770000000000000000000000000000000000000000')
    sprite('null', 1)	# 1-1
    Unknown61(0, 1, 0, 8, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    SLOT_53 = SLOT_0
    if (SLOT_53 == 1):
        gotoLabel(11)
    if (SLOT_53 == 2):
        gotoLabel(12)
    if (SLOT_53 == 3):
        gotoLabel(13)
    if (SLOT_53 == 4):
        gotoLabel(14)
    if (SLOT_53 == 5):
        gotoLabel(15)
    if (SLOT_53 == 6):
        gotoLabel(16)
    if (SLOT_53 == 7):
        gotoLabel(17)
    if (SLOT_53 == 8):
        gotoLabel(18)
    loopRest()
    label(11)
    sprite('vrptef406_00', 32767)	# 2-32768	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 21)
    label(21)
    sprite('vrptef406_00', 20)	# 32769-32788	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_00', 5)	# 32789-32793	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_00', 1)	# 32794-32794	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(12)
    sprite('vrptef406_01', 32767)	# 32795-65561	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 22)
    label(22)
    sprite('vrptef406_01', 20)	# 65562-65581	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_01', 5)	# 65582-65586	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_01', 1)	# 65587-65587	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(13)
    sprite('vrptef406_02', 32767)	# 65588-98354	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 23)
    label(23)
    sprite('vrptef406_02', 20)	# 98355-98374	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_02', 5)	# 98375-98379	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_02', 1)	# 98380-98380	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(14)
    sprite('vrptef406_03', 32767)	# 98381-131147	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)

    def upon_LANDING():
        StartMultihit()
        Unknown1028(0)
        physicsXImpulse(0)
        Unknown1019(90)
        YAccel(90)
        sendToLabel(24)
    label(24)
    sprite('vrptef406_03', 20)	# 131148-131167	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_03', 5)	# 131168-131172	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_03', 1)	# 131173-131173	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(15)
    sprite('vrptef406_04', 32767)	# 131174-163940	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 25)
    label(25)
    sprite('vrptef406_04', 20)	# 163941-163960	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_04', 5)	# 163961-163965	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_04', 1)	# 163966-163966	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(16)
    sprite('vrptef406_05', 32767)	# 163967-196733	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 26)
    label(26)
    sprite('vrptef406_05', 20)	# 196734-196753	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_05', 5)	# 196754-196758	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_05', 1)	# 196759-196759	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(17)
    sprite('vrptef406_06', 32767)	# 196760-229526	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 27)
    label(27)
    sprite('vrptef406_06', 20)	# 229527-229546	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_06', 5)	# 229547-229551	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_06', 1)	# 229552-229552	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(18)
    sprite('vrptef406_07', 32767)	# 229553-262319	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 28)
    label(28)
    sprite('vrptef406_07', 20)	# 262320-262339	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_07', 5)	# 262340-262344	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_07', 1)	# 262345-262345	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()

@State
def DollMaker_DDD():

    def upon_IMMEDIATE():
        Unknown23056('')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 8)	# 1-8
    GFX_0('AttackDoll1_DDD', -1)
    sprite('null', 7)	# 9-15
    sprite('null', 8)	# 16-23
    GFX_0('AttackDoll1_DDD', -1)
    sprite('null', 8)	# 24-31
    GFX_0('AttackDoll1_DDD', -1)
    sprite('null', 8)	# 32-39
    GFX_0('AttackDoll1_DDD', -1)
    sprite('null', 8)	# 40-47
    GFX_0('AttackDoll1_DDD', -1)
    sprite('null', 8)	# 48-55
    GFX_0('AttackDoll1_DDD', -1)
    sprite('null', 8)	# 56-63
    GFX_0('AttackDoll1_DDD', -1)
    Unknown23029(1, 7001, 0)
    label(0)
    sprite('null', 120)	# 64-183
    clearUponHandler(32)

@State
def AttackDoll1_DDD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown1086(22)
        teleportRelativeX(-15000)
        Unknown1007(500000)
        Damage(71)
        AirPushbackY(15000)
        AirUntechableTime(100)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        Hitstop(0)
        Unknown23182(2)
        Unknown11050('06000000707465665f6869745f6c6f770000000000000000000000000000000000000000')

        def upon_43():
            (SLOT_48 == 7001)
            Damage(74)
    sprite('null', 1)	# 1-1
    Unknown61(0, 1, 0, 8, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    SLOT_53 = SLOT_0
    if (SLOT_53 == 1):
        gotoLabel(11)
    if (SLOT_53 == 2):
        gotoLabel(12)
    if (SLOT_53 == 3):
        gotoLabel(13)
    if (SLOT_53 == 4):
        gotoLabel(14)
    if (SLOT_53 == 5):
        gotoLabel(15)
    if (SLOT_53 == 6):
        gotoLabel(16)
    if (SLOT_53 == 7):
        gotoLabel(17)
    if (SLOT_53 == 8):
        gotoLabel(18)
    loopRest()
    label(11)
    sprite('vrptef406_00', 32767)	# 2-32768	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 21)
    label(21)
    sprite('vrptef406_00', 20)	# 32769-32788	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_00', 5)	# 32789-32793	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_00', 1)	# 32794-32794	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(12)
    sprite('vrptef406_01', 32767)	# 32795-65561	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 22)
    label(22)
    sprite('vrptef406_01', 20)	# 65562-65581	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_01', 5)	# 65582-65586	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_01', 1)	# 65587-65587	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(13)
    sprite('vrptef406_02', 32767)	# 65588-98354	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 23)
    label(23)
    sprite('vrptef406_02', 20)	# 98355-98374	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_02', 5)	# 98375-98379	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_02', 1)	# 98380-98380	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(14)
    sprite('vrptef406_03', 32767)	# 98381-131147	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)

    def upon_LANDING():
        StartMultihit()
        Unknown1028(0)
        physicsXImpulse(0)
        Unknown1019(90)
        YAccel(90)
        sendToLabel(24)
    label(24)
    sprite('vrptef406_03', 20)	# 131148-131167	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_03', 5)	# 131168-131172	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_03', 1)	# 131173-131173	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(15)
    sprite('vrptef406_04', 32767)	# 131174-163940	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 25)
    label(25)
    sprite('vrptef406_04', 20)	# 163941-163960	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_04', 5)	# 163961-163965	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_04', 1)	# 163966-163966	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(16)
    sprite('vrptef406_05', 32767)	# 163967-196733	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 26)
    label(26)
    sprite('vrptef406_05', 20)	# 196734-196753	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_05', 5)	# 196754-196758	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_05', 1)	# 196759-196759	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(17)
    sprite('vrptef406_06', 32767)	# 196760-229526	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 27)
    label(27)
    sprite('vrptef406_06', 20)	# 229527-229546	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_06', 5)	# 229547-229551	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_06', 1)	# 229552-229552	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()
    label(18)
    sprite('vrptef406_07', 32767)	# 229553-262319	 **attackbox here**
    GFX_1('ptef_atemi_smoke', -1)
    GFX_1('ptef_atemi_doll', -1)
    Unknown1028(0)
    Unknown1025(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    Unknown1019(90)
    YAccel(90)
    sendToLabelUpon(2, 28)
    label(28)
    sprite('vrptef406_07', 20)	# 262320-262339	 **attackbox here**
    SFX_3('ptse_00')
    Unknown1074(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_07', 5)	# 262340-262344	 **attackbox here**
    Unknown3004(-15)
    sprite('vrptef406_07', 1)	# 262345-262345	 **attackbox here**
    GFX_1('ptef_drivethrow', -1)
    GFX_1('ptef_winsmoke', -1)
    GFX_1('ptef_winsmoke', -1)
    ExitState()

@State
def pt430_mahojin():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6d61686f6a696e322e444947000000000000000000000000000000707465665f6d61686f6a696e325f6d6f74696f6e5f3030302e6d6d6f74000000')
        Unknown4015()
        Unknown23015(5)
        Unknown2054(1)
        Unknown3033()
        Unknown1007(20000)
        Unknown1096(800)
    sprite('null', 100)	# 1-100

@State
def ptef_430power():

    def upon_IMMEDIATE():
        GFX_2('ptef_430power')
        Unknown2054(1)
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 45)	# 1-45
    sprite('null', 7)	# 46-52
    Unknown3004(-40)

@State
def pt430_circle1():

    def upon_IMMEDIATE():
        Unknown4003('707465665f636972636c65312e44494700000000000000000000000000000000707465665f636972636c65315f6d6f74696f6e5f3030302e6d6d6f7400000000')
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown1096(850)
    sprite('null', 65)	# 1-65

@State
def pt430_circle2():

    def upon_IMMEDIATE():
        Unknown4003('707465665f636972636c65322e44494700000000000000000000000000000000707465665f636972636c65325f6d6f74696f6e5f3030302e6d6d6f7400000000')
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown1096(800)
    sprite('null', 65)	# 1-65

@State
def pt430_mahojinsub():

    def upon_IMMEDIATE():
        GFX_2('ptef_430mahojin')
        Unknown2054(1)
        Unknown3033()
    sprite('null', 100)	# 1-100

@State
def pt430_aura1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(5)
        Unknown1007(8000)
        Unknown1056(4000)
        Unknown1064(5600)
        Unknown3001(0)
        Unknown3026(2642170)
    sprite('vrptef_env', 20)	# 1-20
    sprite('vrptef_env', 30)	# 21-50
    Unknown3004(20)
    sprite('vrptef_env', 50)	# 51-100
    Unknown3004(-20)

@State
def pt430_aura2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1007(-78000)
        Unknown1056(8500)
        Unknown1064(3000)
        Unknown3001(0)
        Unknown3026(2657340)
    sprite('vrptef_env', 20)	# 1-20
    sprite('vrptef_env', 30)	# 21-50
    Unknown3004(20)
    sprite('vrptef_env', 50)	# 51-100
    Unknown3004(-20)

@State
def pt430_aura3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1007(-11000)
        Unknown23015(5)
        Unknown3001(0)
        Unknown1056(4600)
        Unknown1064(2800)
        Unknown3026(10490960)
    sprite('vrptef_env', 20)	# 1-20
    sprite('vrptef_env', 30)	# 21-50
    Unknown3004(20)
    sprite('vrptef_env', 50)	# 51-100
    Unknown3004(-20)

@State
def pt430_stick():

    def upon_IMMEDIATE():
        GFX_2('ptef_430stick')
        Unknown4009(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 70)	# 1-70

@State
def pt430_kurukuru():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6b7572756b7572752e444947000000000000000000000000000000707465665f6b7572756b7572755f6d6f74696f6e5f3030302e6d6d6f74000000')
        Unknown4015()
        Unknown23015(5)
        Unknown2054(1)
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 55)	# 1-55

@State
def ptef_431aura():

    def upon_IMMEDIATE():
        GFX_2('ptef_431aura')
        Unknown2054(1)
        Unknown3033()
    sprite('null', 70)	# 1-70

@State
def pt431_startcircle():

    def upon_IMMEDIATE():
        Unknown4003('707465665f7374617274636972636c652e444947000000000000000000000000707465665f7374617274636972636c655f6d6f74696f6e5f3030302e6d6d6f00')
        Unknown4015()
        Unknown2054(1)
        Unknown4010(3)
        Unknown4007(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(800)
    sprite('null', 65)	# 1-65

@State
def pt431_floorcircle():

    def upon_IMMEDIATE():
        Unknown4003('707465665f666c6f6f72636972636c652e444947000000000000000000000000707465665f666c6f6f72636972636c655f6d6f74696f6e5f3030302e6d6d6f00')
        Unknown4015()
        Unknown2054(1)
        Unknown4010(3)
        Unknown4007(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(850)
    sprite('null', 180)	# 1-180

@State
def pt431_ranbucircle():

    def upon_IMMEDIATE():
        Unknown4003('707465665f72616e6275636972636c652e444947000000000000000000000000707465665f72616e6275636972636c655f6d6f74696f6e5f3030302e6d6d6f00')
        Unknown4015()
        Unknown2054(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1007(10000)
        Unknown1096(700)
    sprite('null', 100)	# 1-100

@State
def pt431_tornado():

    def upon_IMMEDIATE():
        Unknown4003('707465665f746f726e61646f2e44494700000000000000000000000000000000707465665f746f726e61646f5f6d6f74696f6e5f3030302e6d6d6f7400000000')
        Unknown4015()
        Unknown2054(1)
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1007(-30000)
        Unknown1096(800)
    sprite('null', 100)	# 1-100

@State
def pt431_smoke():

    def upon_IMMEDIATE():
        GFX_2('ptef_smoke')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 105)	# 1-105
    sprite('null', 20)	# 106-125
    Unknown3004(-15)

@State
def pt431_aura1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        Unknown3001(0)
        teleportRelativeY(41000)
        Unknown1056(5600)
        Unknown1064(5200)
        Unknown3026(2629360)
    sprite('vrptef_env', 25)	# 1-25
    sprite('vrptef_env', 30)	# 26-55
    Unknown3004(20)
    sprite('vrptef_env', 43)	# 56-98
    sprite('vrptef_env', 50)	# 99-148
    Unknown3004(-20)

@State
def pt431_aura2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        Unknown3001(0)
        teleportRelativeY(-51000)
        Unknown1056(4600)
        Unknown1064(3200)
        Unknown3026(1346620)
    sprite('vrptef_env', 25)	# 1-25
    sprite('vrptef_env', 30)	# 26-55
    Unknown3004(20)
    sprite('vrptef_env', 43)	# 56-98
    sprite('vrptef_env', 50)	# 99-148
    Unknown3004(-20)

@State
def pt431_aura3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown3033()
        teleportRelativeY(-81000)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3001(0)
        Unknown1056(5000)
        Unknown1064(3000)
        Unknown3026(686170)
    sprite('vrptef_env', 15)	# 1-15
    sprite('vrptef_env', 15)	# 16-30
    Unknown3004(20)
    sprite('vrptef_env', 40)	# 31-70
    sprite('vrptef_env', 30)	# 71-100
    Unknown3004(-10)

@State
def pt440kira():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown1007(130000)
    label(0)
    sprite('null', 4)	# 1-4
    GFX_1('ptef_440kira_00', -1)
    gotoLabel(0)

@State
def pt440HitEx():

    def upon_IMMEDIATE():
        pass
    sprite('null', 5)	# 1-5
    Unknown4049(1700)
    Unknown4045('707465665f6869745f6d6964646c653035000000000000000000000000000000ffffffff')
    sprite('null', 5)	# 6-10
    Unknown4049(1700)
    Unknown4045('707465665f6869745f6d6964646c653035000000000000000000000000000000ffffffff')
    sprite('null', 5)	# 11-15
    Unknown4049(1700)
    Unknown4045('707465665f6869745f6d6964646c653035000000000000000000000000000000ffffffff')

@State
def Astral1stBeam():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)
        GFX_2('ptef_450fast')
        Unknown3033()
        sendToLabelUpon(32, 12)
    sprite('null', 350)	# 1-350
    label(12)
    sprite('null', 14)	# 351-364
    Unknown3004(-20)
    Unknown1059(20)
    Unknown1067(30)

@State
def AstralMcircle():

    def upon_IMMEDIATE():
        Unknown4003('707465665f6b6f75736f6b75636972636c652e44494700000000000000000000707465665f6b6f75736f6b75636972636c655f6d6f74696f6e5f3030302e6d00')
        Unknown4015()
        Unknown3033()
        Unknown1096(1100)
        Unknown1007(-60000)
    sprite('null', 30)	# 1-30
    Unknown23151(22, 103)
    Unknown4007(22)
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 460)	# 31-490
    Unknown3001(255)
    sprite('null', 10)	# 491-500
    Unknown3004(-30)
    Unknown1099(15)

@State
def Fade1():
    sprite('vr_fade', 9)	# 1-9
    Unknown3032()
    Unknown1096(20000)
    Unknown23015(3)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown6001(1)
    Unknown3026(-16777216)
    Unknown3001(0)
    Unknown3004(22)
    sprite('vr_fade', 254)	# 10-263
    Unknown3004(0)
    sprite('vr_fade', 9)	# 264-272
    Unknown3004(-22)

@State
def AstralAura():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        Unknown3026(16750230)
        sendToLabelUpon(32, 13)
    sprite('vrptef_env450_00', 3)	# 1-3
    Unknown3004(20)
    Unknown3001(0)
    sprite('vrptef_env450_01', 3)	# 4-6
    sprite('vrptef_env450_02', 3)	# 7-9
    Unknown3004(0)
    Unknown3001(200)
    label(15)
    sprite('vrptef_env450_00', 3)	# 10-12
    sprite('vrptef_env450_01', 3)	# 13-15
    sprite('vrptef_env450_02', 3)	# 16-18
    gotoLabel(15)
    label(13)
    sprite('vrptef_env450_00', 10)	# 19-28
    Unknown3004(-20)
    Unknown1099(20)

@State
def AstralAura02():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        Unknown1056(6000)
        Unknown1064(6000)
        teleportRelativeX(10000)
        Unknown3026(16750230)
        sendToLabelUpon(32, 13)
    sprite('vrptef_env', 25)	# 1-25
    Unknown3004(9)
    Unknown3001(0)
    sprite('vrptef_env', 32767)	# 26-32792
    Unknown3004(0)
    Unknown3001(255)
    label(13)
    sprite('null', 10)	# 32793-32802
    Unknown3004(-20)
    Unknown1099(20)

@State
def pt450cutin_hand():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(0)
        Unknown3032()
        Unknown2007()
        Unknown6001(1)
        Unknown1000(-400000)
        teleportRelativeY(-384000)
        Unknown1096(400)
    sprite('pt450cutin_00', 4)	# 1-4
    Unknown23118(16777215)
    Unknown1099(175)
    sprite('pt450cutin_00', 4)	# 5-8
    GFX_0('pt450cutin_hand_par', -1)
    SFX_3('ptse_13')
    Unknown23117(0, 4)
    Unknown1099(0)
    Unknown1096(1000)
    sprite('pt450cutin_00', 2)	# 9-10
    Unknown23120()
    sprite('pt450cutin_00', 27)	# 11-37
    sprite('pt450cutin_00', 3)	# 38-40
    Unknown1099(50)
    Unknown3004(-30)
    sprite('pt450cutin_00', 4)	# 41-44
    Unknown3004(-40)

@State
def pt450cutin_handbg():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(0)
        Unknown3032()
        Unknown2007()
        Unknown6001(1)
        Unknown1000(-400000)
        teleportRelativeY(-384000)
        Unknown1096(400)
    sprite('vr_pt450cutinbg00', 4)	# 1-4
    Unknown23118(16777215)
    Unknown1099(175)
    sprite('vr_pt450cutinbg00', 4)	# 5-8
    Unknown23117(0, 4)
    Unknown1099(0)
    Unknown1096(1000)
    sprite('vr_pt450cutinbg01', 8)	# 9-16
    Unknown23120()
    sprite('vr_pt450cutinbg02', 8)	# 17-24
    sprite('vr_pt450cutinbg00', 8)	# 25-32
    sprite('vr_pt450cutinbg01', 5)	# 33-37
    sprite('vr_pt450cutinbg01', 3)	# 38-40
    Unknown1099(50)
    Unknown3004(-30)
    sprite('vr_pt450cutinbg02', 4)	# 41-44
    Unknown3004(-40)

@State
def pt450cutin_hand_par():

    def upon_IMMEDIATE():
        Unknown4054(4)
        Unknown23067('ptef_450change')
        Unknown3033()
        Unknown23032(70)
        Unknown23033(50)
    sprite('null', 30)	# 1-30
    sprite('null', 6)	# 31-36
    Unknown3004(-40)

@State
def pt450cutin_leg():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(0)
        Unknown3032()
        Unknown2007()
        Unknown6001(1)
        Unknown1000(-880000)
        teleportRelativeY(-384000)
        Unknown1096(400)
    sprite('pt450cutin_01', 4)	# 1-4
    Unknown23118(16777215)
    Unknown1099(175)
    sprite('pt450cutin_01', 4)	# 5-8
    Unknown23117(0, 4)
    Unknown1099(0)
    Unknown1096(1000)
    GFX_0('pt450cutin_leg_par', -1)
    SFX_3('ptse_13')
    sprite('pt450cutin_01', 2)	# 9-10
    Unknown23120()
    sprite('pt450cutin_01', 27)	# 11-37
    sprite('pt450cutin_01', 3)	# 38-40
    Unknown1099(50)
    Unknown3004(-30)
    sprite('pt450cutin_01', 4)	# 41-44
    Unknown3004(-40)

@State
def pt450cutin_legbg():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(0)
        Unknown3032()
        Unknown2007()
        Unknown6001(1)
        Unknown1000(-880000)
        teleportRelativeY(-384000)
        Unknown1096(400)
    sprite('vr_pt450cutinbg00re', 4)	# 1-4
    Unknown23118(16777215)
    Unknown1099(175)
    sprite('vr_pt450cutinbg00re', 4)	# 5-8
    Unknown23117(0, 4)
    Unknown1099(0)
    Unknown1096(1000)
    sprite('vr_pt450cutinbg01re', 8)	# 9-16
    Unknown23120()
    sprite('vr_pt450cutinbg02re', 8)	# 17-24
    sprite('vr_pt450cutinbg00re', 8)	# 25-32
    sprite('vr_pt450cutinbg01re', 5)	# 33-37
    sprite('vr_pt450cutinbg01re', 3)	# 38-40
    Unknown1099(50)
    Unknown3004(-30)
    sprite('vr_pt450cutinbg02re', 4)	# 41-44
    Unknown3004(-40)

@State
def pt450cutin_leg_par():

    def upon_IMMEDIATE():
        Unknown4054(4)
        Unknown23067('ptef_450change')
        Unknown3033()
        Unknown23032(30)
        Unknown23033(50)
    sprite('null', 30)	# 1-30
    sprite('null', 6)	# 31-36
    Unknown3004(-40)

@State
def pt450cutin_bustup():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(0)
        Unknown3032()
        Unknown2019(-4000)
        Unknown6001(1)
        teleportRelativeY(-1200000)
        Unknown1001(640000)
        SLOT_59 = SLOT_4
        Unknown23030('50545f4c696e6b436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('pt450cutin_02', 5)	# 1-5
    Unknown23118(16777215)
    physicsYImpulse(75000)
    sprite('pt450cutin_03', 5)	# 6-10
    sprite('pt450cutin_04', 5)	# 11-15
    physicsYImpulse(100)
    sprite('pt450cutin_05', 5)	# 16-20
    Unknown23117(0, 6)
    GFX_0('pt450cutin_up_par', -1)
    sprite('pt450cutin_02', 1)	# 21-21
    sprite('pt450cutin_02', 4)	# 22-25
    Unknown23120()
    physicsYImpulse(200)
    sprite('pt450cutin_03', 5)	# 26-30
    SFX_3('ptse_17')
    sprite('pt450cutin_04', 5)	# 31-35
    sprite('pt450cutin_05', 5)	# 36-40
    physicsYImpulse(400)
    sprite('pt450cutin_06', 5)	# 41-45
    sprite('pt450cutin_07', 5)	# 46-50
    sprite('pt450cutin_08', 5)	# 51-55
    GFX_0('pt450cutin_kira', -1)
    sprite('pt450cutin_09', 5)	# 56-60
    sprite('pt450cutin_10', 5)	# 61-65
    sprite('pt450cutin_11', 5)	# 66-70
    sprite('pt450cutin_08', 5)	# 71-75
    sprite('pt450cutin_09', 5)	# 76-80
    sprite('pt450cutin_10', 5)	# 81-85
    sprite('pt450cutin_11', 5)	# 86-90
    sprite('pt450cutin_08', 5)	# 91-95
    sprite('pt450cutin_09', 5)	# 96-100
    physicsYImpulse(200)
    sprite('pt450cutin_10', 5)	# 101-105
    sprite('pt450cutin_11', 5)	# 106-110
    physicsYImpulse(0)
    sprite('pt450cutin_08', 5)	# 111-115
    sprite('pt450cutin_12', 6)	# 116-121
    Unknown21012('7074343530637574696e5f6b697261000000000000000000000000000000000020000000')
    Unknown1007(36000)
    sprite('pt450cutin_13', 6)	# 122-127
    physicsYImpulse(3000)
    sprite('pt450cutin_14', 6)	# 128-133
    Unknown3004(-20)
    sprite('pt450cutin_15', 6)	# 134-139

@State
def pt450cutin_up_par():

    def upon_IMMEDIATE():
        Unknown4054(4)
        Unknown23067('ptef_450change')
        Unknown3033()
        Unknown1096(1200)
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 40)	# 1-40
    sprite('null', 20)	# 41-60
    Unknown3004(-10)
    Unknown1099(10)

@State
def pt450cutin_kira():

    def upon_IMMEDIATE():
        Unknown4054(4)
        Unknown23067('ptef_450cutin')
        Unknown3033()
        Unknown23032(50)
        Unknown23033(50)
        sendToLabelUpon(32, 14)
    sprite('null', 32767)	# 1-32767
    label(14)
    sprite('null', 20)	# 32768-32787
    Unknown3004(-10)
    Unknown1099(10)

@State
def pt450cutin_bustupbg():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(0)
        Unknown3032()
        Unknown2019(4000)
        Unknown2007()
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-384000)
        Unknown1001(640000)
    sprite('vr_pt450cutinbg03', 10)	# 1-10
    Unknown3004(25)
    Unknown3001(0)
    sprite('vr_pt450cutinbg03', 121)	# 11-131
    Unknown3004(0)
    Unknown3001(255)
    sprite('vr_pt450cutinbg03', 6)	# 132-137
    Unknown3004(-5)
    sprite('vr_pt450cutinbg03', 12)	# 138-149
    Unknown3004(-20)

@State
def pt450_mahojin1():

    def upon_IMMEDIATE():
        Unknown4003('707465665f61686d61686f6a696e2e4449470000000000000000000000000000707465665f61686d61686f6a696e5f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(2)
        Unknown4015()
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1096(1000)
        Unknown1000(250000)
        teleportRelativeY(250000)
    sprite('null', 20)	# 1-20
    sprite('null', 160)	# 21-180
    sprite('null', 40)	# 181-220
    Unknown3004(-15)

@State
def pt450_mahojin2():

    def upon_IMMEDIATE():
        Unknown4003('707465665f61686d61686f6a696e322e44494700000000000000000000000000707465665f61686d61686f6a696e325f6d6f74696f6e5f3030302e6d6d6f7400')
        Unknown4010(2)
        Unknown4015()
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1096(1000)
        Unknown1000(200000)
        teleportRelativeY(250000)
    sprite('null', 140)	# 1-140

@State
def pt450_mahojin3():

    def upon_IMMEDIATE():
        Unknown4003('707465665f61686d61686f6a696e332e44494700000000000000000000000000707465665f61686d61686f6a696e335f6d6f74696f6e5f3030302e6d6d6f7400')
        Unknown4010(2)
        Unknown4015()
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1096(1000)
        Unknown1000(200000)
        teleportRelativeY(250000)
    sprite('null', 89)	# 1-89
    sprite('null', 5)	# 90-94
    physicsXImpulse(-5000)
    Unknown1099(40)
    sprite('null', 46)	# 95-140
    physicsXImpulse(-5000)
    Unknown1099(10)

@State
def pt450Beam():

    def upon_IMMEDIATE():
        Unknown4054(4)
        Unknown23067('ptef_450splash')
        Unknown2054(1)
        Unknown3033()
    sprite('null', 16)	# 1-16
    Unknown3001(0)
    sprite('null', 10)	# 17-26
    Unknown1064(0)
    Unknown1067(110)
    Unknown3001(255)
    physicsXImpulse(-6000)
    sprite('null', 110)	# 27-136
    physicsXImpulse(0)
    Unknown1067(0)

@State
def FadeWhite():
    sprite('vr_fade', 15)	# 1-15
    Unknown3032()
    Unknown1096(20000)
    Unknown23015(3)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown6001(1)
    Unknown3026(-1)
    Unknown3001(0)
    Unknown3004(17)
    sprite('vr_fade', 60)	# 16-75
    Unknown3004(0)
    sprite('vr_fade', 15)	# 76-90
    Unknown3004(-17)

@State
def AstralAuraWin():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        Unknown1056(6000)
        Unknown1064(6000)
        teleportRelativeX(10000)
        Unknown21004(208)
    sprite('vrptef_env', 10)	# 1-10
    Unknown3004(18)
    Unknown3001(0)
    sprite('vrptef_env', 32767)	# 11-32777
    Unknown3004(0)
    Unknown3001(180)

@State
def EntryHeart():

    def upon_IMMEDIATE():
        GFX_2('ptef_entryheartB')
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 10)	# 1-10
    sprite('null', 5)	# 11-15
    physicsYImpulse(8000)
    sprite('null', 10)	# 16-25
    physicsYImpulse(10000)
    Unknown1099(10)
    sprite('null', 10)	# 26-35
    Unknown1099(15)
    physicsYImpulse(15000)
    sprite('null', 15)	# 36-50
    physicsYImpulse(20000)

@State
def EntryRod():

    def upon_IMMEDIATE():
        Unknown1096(1000)
        teleportRelativeY(820000)
        teleportRelativeX(-85000)
        Unknown1072(100000)
        Unknown1074(-20000)
        physicsYImpulse(-18200)
        Unknown3032()
    sprite('vrptef601_00', 16)	# 1-16
    SFX_0('008_swing_pole_0')
    sprite('vrptef601_00', 5)	# 17-21
    Unknown1074(-15000)
    sprite('vrptef601_00', 3)	# 22-24
    Unknown1074(-12000)

@State
def FusenEntry():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1007(120000)
        Unknown1000(-20000)
        Unknown3032()
        Unknown3001(230)
    sprite('vrptef602_09', 6)	# 1-6
    sprite('vrptef602_02', 8)	# 7-14
    SFX_3('ptse_00')
    sprite('vrptef602_08', 8)	# 15-22
    sprite('vrptef602_07', 8)	# 23-30
    sprite('vrptef602_08', 8)	# 31-38
    sprite('vrptef602_02', 8)	# 39-46
    SFX_3('ptse_00')
    sprite('vrptef602_09', 8)	# 47-54
    sprite('vrptef602_10', 8)	# 55-62
    sprite('vrptef602_09', 8)	# 63-70
    sprite('vrptef602_02', 8)	# 71-78
    SFX_3('ptse_00')
    sprite('vrptef602_08', 8)	# 79-86
    sprite('vrptef602_07', 8)	# 87-94
    sprite('vrptef602_08', 8)	# 95-102
    sprite('vrptef602_02', 8)	# 103-110
    SFX_3('ptse_00')
    sprite('vrptef602_09', 8)	# 111-118
    sprite('vrptef602_10', 8)	# 119-126
    sprite('vrptef602_09', 8)	# 127-134
    sprite('vrptef602_02', 8)	# 135-142
    SFX_3('ptse_00')
    sprite('vrptef602_08', 8)	# 143-150
    sprite('vrptef602_07', 8)	# 151-158
    sprite('vrptef602_08', 8)	# 159-166
    sprite('vrptef602_02', 8)	# 167-174
    SFX_3('ptse_00')
    sprite('vrptef401_04', 6)	# 175-180
    Unknown4007(0)
    Unknown1096(1300)
    Unknown3004(-10)
    SFX_0('100_hit_grap_0')
    sprite('vrptef401_05', 6)	# 181-186
    loopRest()

@State
def EventPT01_ibbn():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        Unknown4061(7)
        Unknown2018(0, 100)
    label(0)
    sprite('bn000_00', 7)	# 1-7
    sprite('bn000_01', 7)	# 8-14
    sprite('bn000_02', 7)	# 15-21
    sprite('bn000_03', 7)	# 22-28
    sprite('bn000_04', 7)	# 29-35
    sprite('bn000_05', 7)	# 36-42
    sprite('bn000_06', 7)	# 43-49
    sprite('bn000_07', 7)	# 50-56
    sprite('bn000_08', 7)	# 57-63
    sprite('bn000_09', 7)	# 64-70
    sprite('bn000_11', 7)	# 71-77
    loopRest()
    gotoLabel(0)
    label(1)
    Unknown3032()
    sprite('bn050_00', 1)	# 78-78
    sprite('bn050_01', 1)	# 79-79
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    Unknown3004(-10)
    sprite('bn050_02', 30)	# 80-109
    sprite('bn050_02', 5)	# 110-114
    Unknown3038(1)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('bn050_02', 5)	# 115-119
    Unknown3004(0)
    GFX_1('haef_event_lose_end', 103)
    sprite('bn050_02', 32767)	# 120-32886

@State
def ptPhantom():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3001(0)
        Unknown3032()
        Unknown1007(70000)
        teleportRelativeX(-50000)
    sprite('pt999_00', 15)	# 1-15
    Unknown3004(10)
    sprite('pt999_00', 6)	# 16-21
    Unknown3001(160)
    Unknown3004(0)
    sprite('pt999_00', 120)	# 22-141
    sprite('pt999_00', 6)	# 142-147
    Unknown3004(-2)
    physicsXImpulse(-1000)
    sprite('pt999_00', 6)	# 148-153
    physicsXImpulse(-400)
    sprite('pt999_00', 6)	# 154-159
    sprite('pt999_00', 6)	# 160-165
    sprite('pt999_00', 6)	# 166-171
    sprite('pt999_00', 6)	# 172-177
    sprite('pt999_00', 6)	# 178-183
    sprite('pt999_00', 6)	# 184-189
    sprite('pt999_00', 6)	# 190-195
    sprite('pt999_00', 6)	# 196-201
    sprite('pt999_00', 6)	# 202-207
    sprite('pt999_00', 6)	# 208-213

@State
def ptPhantom_2():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3001(0)
        Unknown3032()
        Unknown1007(70000)
    sprite('pt999_00', 22)	# 1-22
    Unknown3004(10)
    sprite('pt999_00', 6)	# 23-28
    Unknown3004(0)
    Unknown23119(3289650, 120, 120)
    sendToLabelUpon(32, 1)
    label(0)
    sprite('pt999_00', 50)	# 29-78
    physicsYImpulse(100)
    sprite('pt999_00', 50)	# 79-128
    sprite('pt999_00', 20)	# 129-148
    physicsYImpulse(0)
    sprite('pt999_00', 100)	# 149-248
    physicsYImpulse(-100)
    sprite('pt999_00', 10)	# 249-258
    physicsYImpulse(0)
    gotoLabel(0)
    label(1)
    sprite('pt999_00', 6)	# 259-264
    Unknown1084(1)
    Unknown3004(-5)
    physicsXImpulse(-300)
    sprite('pt999_00', 6)	# 265-270
    sprite('pt999_00', 6)	# 271-276
    sprite('pt999_00', 6)	# 277-282
    sprite('pt999_00', 6)	# 283-288
    sprite('pt999_00', 6)	# 289-294
    sprite('pt999_00', 6)	# 295-300
    sprite('pt999_00', 6)	# 301-306
    sprite('pt999_00', 6)	# 307-312
    sprite('pt999_00', 6)	# 313-318
    sprite('pt999_00', 6)	# 319-324
    sprite('pt999_00', 6)	# 325-330

@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown1086(22)
        teleportRelativeY(0)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 1000)	# 1-1000
    Unknown20000(1)
    Unknown20003(1)
    label(1)
    sprite('null', 1)	# 1001-1001
    Unknown20000(0)
    Unknown20003(0)

@State
def ptef_408_splash():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown4010(2)
        teleportRelativeY(0)
    label(0)
    sprite('null', 3)	# 1-3
    GFX_1('ptef408splash', -1)
    gotoLabel(0)

@State
def ptef_409_ring():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('vrptef409_01', 3)	# 1-3	 **attackbox here**
    sprite('vrptef409_02', 5)	# 4-8	 **attackbox here**
    sprite('vrptef409_03', 5)	# 9-13	 **attackbox here**
    sprite('vrptef409_04', 2)	# 14-15	 **attackbox here**
    sprite('vrptef409_05', 2)	# 16-17	 **attackbox here**

@State
def ptef_409_ring_air():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('vrptef409_14', 3)	# 1-3	 **attackbox here**
    sprite('vrptef409_02ex01', 5)	# 4-8	 **attackbox here**
    sprite('vrptef409_15', 5)	# 9-13	 **attackbox here**
    sprite('vrptef409_16', 2)	# 14-15	 **attackbox here**
    sprite('vrptef409_17', 2)	# 16-17	 **attackbox here**

@State
def BoomerangAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1100)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        Hitstop(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(55)
        hitstun(30)
        AirPushbackX(2500)
        AirPushbackY(32000)
        Unknown11001(6, 0, 2)
        Unknown11042(1)
        Unknown2055(300)
        Unknown23013(1)
        Unknown2053(0)
        teleportRelativeX(-100000)
        Unknown1007(-64000)
        Unknown3032()
        Unknown4061(0)
        Unknown3038(1)
        physicsXImpulse(35000)
        Unknown1028(-500)

        def upon_44():
            Unknown2001()
            Unknown3001(144)
            Unknown26('Boomerang_blm')
            Unknown21012('426f6f6d6572616e675f77696e6700000000000000000000000000000000000021000000')
            Unknown21012('426f6f6d6572616e675f77696e675f620000000000000000000000000000000021000000')

        def upon_ON_HIT_OR_BLOCK():
            pass

        def upon_CLEAR_OR_EXIT():
            Unknown1019(99)
            if (not SLOT_2):
                Unknown48('190000000200000034000000030000000200000017000000')
                Unknown47('01000000020000001700000002000000340000000200000034000000')
                Unknown47('03000000020000003400000000000000d3ffffff020000000d000000')
                if (SLOT_12 < 10000):
                    Unknown2037(1)
                    sendToLabel(1)
            else:
                Unknown59('19000000640000000300000064000000')
                if (SLOT_0 < 150000):
                    Unknown2037(0)
                    clearUponHandler(3)
                Unknown59('19000000640000000300000064000000')
                if (SLOT_0 >= 5000000):
                    clearUponHandler(3)
    sprite('vrptef409_boomerang', 32767)	# 1-32767	 **attackbox here**
    SFX_3('ptse_30')
    GFX_0('Boomerang_ring', 0)
    GFX_0('Boomerang_wing', 0)
    GFX_0('Boomerang_wing_b', 0)
    GFX_0('Boomerang_pt', 0)
    GFX_0('Boomerang_blm', 0)
    label(1)
    sprite('vrptef409_boomerang', 20)	# 32768-32787	 **attackbox here**
    Unknown1028(-300)
    sprite('vrptef409_boomerang', 32767)	# 32788-65554	 **attackbox here**
    Unknown2005()
    RefreshMultihit()
    Unknown1028(1500)
    sprite('keep', 4)	# 65555-65558
    Unknown3001(255)
    Unknown3004(-51)
    Unknown1084(1)
    ExitState()
    label(2)
    sprite('keep', 4)	# 65559-65562
    Unknown3001(255)
    Unknown3004(-51)
    Unknown1084(1)
    if (SLOT_4 == 15):
        SLOT_31 = (SLOT_31 + 1)
    else:
        Unknown23029(3, 0, 0)

@State
def Boomerang_ring():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
        Unknown4003('707465665f34303972696e6700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown1096(500)
        Unknown23015(7)
    sprite('null', 32767)	# 1-32767

@State
def Boomerang_wing():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3032()
        Unknown23015(8)

        def upon_33():
            SLOT_51 = 1
            Unknown3001(144)
            Unknown3004(-7)
    label(0)
    sprite('vrptef409_wing00', 4)	# 1-4
    sprite('vrptef409_wing01', 4)	# 5-8
    sprite('vrptef409_wing02', 4)	# 9-12
    sprite('vrptef409_wing01', 4)	# 13-16
    Unknown19(0, 2, 51)
    sprite('vrptef409_wing00', 4)	# 17-20
    sprite('vrptef409_wing01', 4)	# 21-24
    sprite('vrptef409_wing02', 4)	# 25-28

@State
def Boomerang_wing_b():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3032()
        Unknown23015(6)

        def upon_33():
            SLOT_51 = 1
            Unknown3001(144)
            Unknown3004(-7)
    label(0)
    sprite('vrptef409_wing00b', 4)	# 1-4
    sprite('vrptef409_wing01b', 4)	# 5-8
    sprite('vrptef409_wing02b', 4)	# 9-12
    sprite('vrptef409_wing01b', 4)	# 13-16
    Unknown19(0, 2, 51)
    sprite('vrptef409_wing00b', 4)	# 17-20
    sprite('vrptef409_wing01b', 4)	# 21-24
    sprite('vrptef409_wing02b', 4)	# 25-28

@State
def Boomerang_blm():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
        Unknown23067('ptef409_bloom')
        Unknown1096(925)
    sprite('null', 32767)	# 1-32767

@State
def Boomerang_pt():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 4)	# 1-4
    GFX_1('ptef409_light', -1)
    gotoLabel(0)

@State
def SPBoomerangAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1350)
        ProjectileDurabilityLvl(2)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        Hitstop(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        hitstun(40)
        AirPushbackX(2500)
        AirPushbackY(32000)
        Unknown11001(6, 0, 5)
        Unknown11042(1)
        Unknown3032()
        Unknown4061(0)
        Unknown3038(1)
        Unknown2055(300)
        Unknown23013(1)
        Unknown2053(0)
        teleportRelativeX(-100000)
        Unknown1007(-64000)
        physicsXImpulse(35000)
        Unknown1028(-500)

        def upon_44():
            Unknown2001()
            Unknown3001(144)
            Unknown26('Boomerang_blm_sp')
            Unknown21012('5350426f6f6d6572616e675f77696e670000000000000000000000000000000021000000')
            Unknown21012('5350426f6f6d6572616e675f77696e675f62000000000000000000000000000021000000')

        def upon_ON_HIT_OR_BLOCK():
            pass

        def upon_CLEAR_OR_EXIT():
            Unknown1019(99)
            Unknown48('190000000200000034000000030000000200000017000000')
            Unknown47('01000000020000001700000002000000340000000200000034000000')
            Unknown47('03000000020000003400000000000000c4ffffff020000000d000000')
            if (not SLOT_2):
                if (SLOT_12 < 10000):
                    Unknown2037(1)
                    sendToLabel(1)
            else:
                Unknown59('19000000640000000300000064000000')
                if (SLOT_0 < 200000):
                    Unknown2037(0)
                    clearUponHandler(3)
                Unknown59('19000000640000000300000064000000')
                if (SLOT_0 >= 5000000):
                    clearUponHandler(3)
    sprite('vrptef409_boomerang_sp', 32767)	# 1-32767	 **attackbox here**
    SFX_3('ptse_30')
    GFX_0('SPBoomerang_ring', 0)
    GFX_0('SPBoomerang_wing', 0)
    GFX_0('SPBoomerang_wing_b', 0)
    GFX_0('Boomerang_pt', 0)
    GFX_0('Boomerang_blm_sp', 0)
    label(1)
    sprite('vrptef409_boomerang_sp', 20)	# 32768-32787	 **attackbox here**
    Unknown1028(-300)
    sprite('vrptef409_boomerang_sp', 32767)	# 32788-65554	 **attackbox here**
    Unknown2005()
    RefreshMultihit()
    Unknown1028(1500)
    sprite('keep', 4)	# 65555-65558
    Unknown3001(255)
    Unknown3004(-51)
    Unknown1084(1)
    ExitState()
    label(2)
    sprite('keep', 4)	# 65559-65562
    Unknown3001(255)
    Unknown3004(-51)
    Unknown1084(1)
    if (SLOT_4 == 16):
        SLOT_31 = (SLOT_31 + 1)
    else:
        Unknown23029(3, 1, 0)

@State
def SPBoomerang_ring():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
        Unknown4003('707465665f34303972696e6732000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown1096(750)
        Unknown23015(7)
    sprite('null', 32767)	# 1-32767

@State
def SPBoomerang_wing():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3032()
        Unknown23015(8)

        def upon_33():
            SLOT_51 = 1
            Unknown3001(144)
            Unknown3004(-7)
    label(0)
    sprite('vrptef409_sp_wing00', 4)	# 1-4
    sprite('vrptef409_sp_wing01', 4)	# 5-8
    Unknown19(0, 2, 51)
    sprite('vrptef409_sp_wing00', 4)	# 9-12
    sprite('vrptef409_sp_wing01', 4)	# 13-16
    sprite('vrptef409_sp_wing00', 4)	# 17-20
    sprite('vrptef409_sp_wing01', 4)	# 21-24

@State
def SPBoomerang_wing_b():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3032()
        Unknown23015(6)

        def upon_33():
            SLOT_51 = 1
            Unknown3001(144)
            Unknown3004(-7)
    label(0)
    sprite('vrptef409_sp_wing00b', 4)	# 1-4
    sprite('vrptef409_sp_wing01b', 4)	# 5-8
    Unknown19(0, 2, 51)
    sprite('vrptef409_sp_wing00b', 4)	# 9-12
    sprite('vrptef409_sp_wing01b', 4)	# 13-16
    sprite('vrptef409_sp_wing00b', 4)	# 17-20
    sprite('vrptef409_sp_wing01b', 4)	# 21-24

@State
def Boomerang_blm_sp():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4025(2)
        Unknown23067('ptef409_bloom')
        Unknown1096(1390)
    sprite('null', 32767)	# 1-32767

@State
def Boomerang():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(900)
        HitAirUnblockable(3)
        Unknown1074(7500)
        Unknown1026(3000, 15000)
        Unknown1025(-2000, 2000)
        Unknown3038(1)

        def upon_11():
            Unknown26('Boomerang_pt')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_Boomerang', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    GFX_0('Boomerang_ring', 0)
    GFX_0('Boomerang_wing', 0)
    GFX_0('Boomerang_wing_b', 0)
    GFX_0('Boomerang_pt', 0)
    label(10)
    sprite('vr_Boomerang', 30)	# 31-60	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('vr_Boomerang', 30)	# 61-90	 **attackbox here**
    StartMultihit()

@State
def SPBoomerang():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ItemThrowInit')
        Damage(1100)
        HitAirUnblockable(3)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        Unknown1074(7500)
        Unknown1026(3000, 15000)
        Unknown1025(-2000, 2000)
        Unknown3038(1)

        def upon_11():
            Unknown26('Boomerang_pt')
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

        def upon_54():
            DisableAttackRestOfMove()
            Unknown3029(0)
            Unknown23118(0)
            Unknown1019(-30)
            physicsYImpulse(20000)
            Unknown23001(0, 0)
            Unknown23014()
            Unknown1074(-10000)
        Unknown4011(3)
        sendToLabelUpon(2, 1)
    label(0)
    sprite('vr_SPboomerang', 30)	# 1-30	 **attackbox here**
    SFX_0('008_swing_pole_1')
    GFX_0('SPBoomerang_ring', 0)
    GFX_0('SPBoomerang_wing', 0)
    GFX_0('SPBoomerang_wing_b', 0)
    GFX_0('Boomerang_pt', 0)
    label(10)
    sprite('vr_SPboomerang', 30)	# 31-60	 **attackbox here**
    SFX_0('008_swing_pole_1')
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('vr_SPboomerang', 30)	# 61-90	 **attackbox here**
    StartMultihit()

@State
def Act3Event_ptPhantom_Renew():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3001(0)
        Unknown3032()
        teleportRelativeX(-50000)
        Unknown1007(70000)
        Unknown2019(1000)
        sendToLabelUpon(32, 9)
    sprite('pt999_00', 45)	# 1-45
    SFX_0('302_spsys_rapid')
    Unknown3004(5)
    GFX_1('ef_tekitou_b', 0)
    sprite('pt999_00', 6)	# 46-51
    Unknown3004(0)
    Unknown23119(3289650, 120, 120)
    label(0)
    sprite('pt999_00', 50)	# 52-101
    physicsYImpulse(100)
    sprite('pt999_00', 50)	# 102-151
    sprite('pt999_00', 20)	# 152-171
    physicsYImpulse(0)
    sprite('pt999_00', 100)	# 172-271
    physicsYImpulse(-100)
    sprite('pt999_00', 10)	# 272-281
    physicsYImpulse(0)
    gotoLabel(0)
    label(9)
    sprite('pt999_00', 6)	# 282-287
    Unknown1084(1)
    Unknown3004(-5)
    physicsXImpulse(-300)
    sprite('pt999_00', 6)	# 288-293
    sprite('pt999_00', 6)	# 294-299
    sprite('pt999_00', 6)	# 300-305
    sprite('pt999_00', 6)	# 306-311
    sprite('pt999_00', 6)	# 312-317
    sprite('pt999_00', 6)	# 318-323
    sprite('pt999_00', 6)	# 324-329
    sprite('pt999_00', 6)	# 330-335
    sprite('pt999_00', 6)	# 336-341
    sprite('pt999_00', 6)	# 342-347
    sprite('pt999_00', 6)	# 348-353

@State
def ptPhantom_NoSound():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3001(0)
        Unknown3032()
        Unknown1007(70000)
        sendToLabelUpon(32, 1)
        Unknown2019(1000)
    sprite('pt999_00', 22)	# 1-22
    Unknown3004(10)
    sprite('pt999_00', 6)	# 23-28
    Unknown3004(0)
    Unknown23119(3289650, 120, 120)
    label(0)
    sprite('pt999_00', 50)	# 29-78
    physicsYImpulse(100)
    sprite('pt999_00', 50)	# 79-128
    sprite('pt999_00', 20)	# 129-148
    physicsYImpulse(0)
    sprite('pt999_00', 100)	# 149-248
    physicsYImpulse(-100)
    sprite('pt999_00', 10)	# 249-258
    physicsYImpulse(0)
    gotoLabel(0)
    label(1)
    sprite('pt999_00', 6)	# 259-264
    Unknown1084(1)
    Unknown3004(-5)
    physicsXImpulse(-300)
    sprite('pt999_00', 6)	# 265-270
    sprite('pt999_00', 6)	# 271-276
    sprite('pt999_00', 6)	# 277-282
    sprite('pt999_00', 6)	# 283-288
    sprite('pt999_00', 6)	# 289-294
    sprite('pt999_00', 6)	# 295-300
    sprite('pt999_00', 6)	# 301-306
    sprite('pt999_00', 6)	# 307-312
    sprite('pt999_00', 6)	# 313-318
    sprite('pt999_00', 6)	# 319-324
    sprite('pt999_00', 6)	# 325-330

@State
def Act2Event_Camera():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown1000(0)
        teleportRelativeY(800000)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(9)
        Unknown20000(1)
        loopRelated(17, 2000)
        sendToLabelUpon(17, 9)
    sprite('null', 32767)	# 1-32767
    Unknown20003(1)
    loopRest()
    label(0)
    sprite('null', 32767)	# 32768-65534
    Unknown1086(3)
    loopRest()
    label(9)
    sprite('null', 10)	# 65535-65544
    Unknown20000(0)
    Unknown20003(0)

@State
def Act2Event_Fade():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown3001(0)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 60)	# 1-60
    Unknown1096(20000)
    Unknown3026(-16777216)
    Unknown3004(4)
    Unknown23024(2)
    sprite('null', 32767)	# 61-32827
    Unknown3004(0)
    Unknown3001(255)

@State
def Act3Event_FadeWhite():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
    sprite('vr_fade', 30)	# 1-30
    Unknown3032()
    Unknown1096(20000)
    Unknown23015(3)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown6001(1)
    Unknown3026(-1)
    Unknown3001(0)
    Unknown3004(8)
    sprite('vr_fade', 32767)	# 31-32797
    Unknown3004(0)
    Unknown3001(255)
    label(0)
    sprite('vr_fade', 30)	# 32798-32827
    Unknown3004(-8)