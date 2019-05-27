@Subroutine
def Monsho_AtkData():
    AttackLevel_(1)
    AttackP1(70)
    AttackP2(90)
    Hitstop(6)
    Unknown9154(17)
    AirUntechableTime(21)
    Unknown11028(11)
    Unknown9016(1)

@State
def es203_effAtk():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(20000)
        PushbackX(20000)
        Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 110):
                Unknown13(25)
            if (SLOT_48 == 129):
                Unknown13(25)
            if (SLOT_48 == 103):
                sendToLabel(0)
    sprite('null', 15)	# 1-15
    sprite('null', 5)	# 16-20
    GFX_0('es203_effAtk_Yotyou', -1)
    clearUponHandler(43)
    Unknown38(11, 1)
    label(0)
    clearUponHandler(43)
    sprite('null', 4)	# 21-24
    Unknown13(11)
    GFX_0('esef_203Monsho', 100)
    SFX_3('esse_01')
    sprite('es203_effatk', 3)	# 25-27	 **attackbox here**
    sprite('null', 50)	# 28-77

@State
def es213_effAtk():

    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('Monsho_AtkData')
        AirPushbackX(5500)
        AirPushbackY(35000)
        AirUntechableTime(60)
        Hitstop(4)
        Unknown11042(1)
        Unknown11031(5)
        Unknown11091(5)
        Unknown23089('0100000000000000000000000000000000000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 103):
                sendToLabel(0)
            if (SLOT_48 == 110):
                Unknown13(25)
    sprite('null', 5)	# 1-5
    sprite('null', 7)	# 6-12
    GFX_0('es213_effAtk_Yotyou', -1)
    Unknown38(11, 1)
    label(0)
    sprite('null', 3)	# 13-15
    clearUponHandler(43)
    Unknown13(11)
    GFX_0('esef_213Monsho', -1)
    SFX_3('esse_01')
    sprite('es213_effatk', 3)	# 16-18	 **attackbox here**
    sprite('null', 50)	# 19-68

@State
def es213_effAtk_Yotyou():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('657365665f323133736c6173685f796f74796f7530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown23015(15)
        Unknown1096(850)
    sprite('null', 5)	# 1-5
    Unknown3001(0)
    Unknown3004(10)
    label(0)
    sprite('null', 5)	# 6-10
    sprite('null', 10)	# 11-20
    Unknown3004(-13)
    sprite('null', 10)	# 21-30
    Unknown3004(13)
    gotoLabel(0)


@State
def esef_213Monsho():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('657365665f323133736c61736841646441746b5f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4061(4)
        Unknown21004(241)
        Unknown3038(1)
        Unknown1096(950)
        teleportRelativeY(12000)
    sprite('null', 5)	# 1-5
    ScreenShake(5000, 5000)
    GFX_0('esef_213MonshoAdd', 100)
    Unknown21010(1)
    sprite('null', 10)	# 6-15
    Unknown4009(2)
    Unknown21010(0)
    sprite('vresef213_ParitclePos', 10)	# 16-25
    Unknown4003('657365665f323133736c61736841646441746b5f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('esef_213MonshoAdd')
    Unknown3004(-25)
    Unknown4009(0)
    Unknown4010(0)
    Unknown2054(1)

@State
def esef_213MonshoAdd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4003('657365665f323133736c61736841646441746b5f30306164642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
    sprite('null', 32767)	# 1-32767


@Subroutine
def es400_Init():
    Unknown2010()
    AttackLevel_(2)
    Damage(1500)
    AttackP1(80)
    AttackP2(80)
    AirPushbackX(12000)
    AirPushbackY(12000)
    AirUntechableTime(22)
    Unknown9154(17)
    Hitstop(8)
    PushbackX(8000)
    Unknown9016(1)
    Unknown4011(3)
    Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')

    def upon_54():
        clearUponHandler(43)
        Unknown13(25)
        Unknown23029(4, 124, 0)
    callSubroutine('es400_Delete')

@Subroutine
def es400_Delete():

    def upon_3():
        if SLOT_38:
            Unknown23045('7d000000')
            if (SLOT_22 < SLOT_0):
                clearUponHandler(2)
                clearUponHandler(54)
                clearUponHandler(3)
                Unknown13(25)
                Unknown13(4)
        else:
            Unknown23045('7d000000')
            if (SLOT_22 > SLOT_0):
                clearUponHandler(2)
                clearUponHandler(54)
                clearUponHandler(3)
                Unknown13(25)
                Unknown13(4)

@State
def es400_A():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown1007(128000)
        teleportRelativeX(100000)
    sprite('es400eff_atk1', 3)	# 1-3	 **attackbox here**
    GFX_0('esef_400eff_MatomeA', -1)
    Unknown38(4, 1)
    physicsXImpulse(45000)
    Unknown1028(-1300)
    SFX_3('esse_03')
    sprite('es400eff_atk2', 27)	# 4-30	 **attackbox here**
    Unknown21015('73686f74000000000000000000000000000000000000000000000000000000007800000000000000')
    sprite('null', 1)	# 31-31
    Unknown23029(4, 125, 0)

@State
def es400_B():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown1007(128000)
        teleportRelativeX(100000)

        def upon_43():
            if (SLOT_48 == 126):
                Unknown2003(1)
    sprite('null', 3)	# 1-3
    GFX_0('esef_400eff_MatomeB', -1)
    Unknown38(4, 1)
    physicsXImpulse(2500)
    SFX_3('esse_03')
    sprite('es400eff_atk1', 22)	# 4-25	 **attackbox here**
    clearUponHandler(43)
    sprite('es400eff_atk2', 100)	# 26-125	 **attackbox here**
    Unknown21015('73686f74000000000000000000000000000000000000000000000000000000007800000000000000')
    physicsXImpulse(70000)

@State
def es400_B_2nd():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        Unknown1007(128000)
        teleportRelativeX(110000)

        def upon_43():
            if (SLOT_48 == 119):
                GFX_0('es400_B_2ndEX', -1)
                Unknown26('es400_A')
                Unknown26('esef_400eff_MatomeA')
                Unknown13(25)
                Unknown26('esef_400eff2nd_MatomeB')
                Unknown26('esef_400eff2nd_MatomeB2')
    Unknown48('190000000200000033000000030000000200000033000000')
    if SLOT_51:
        _gotolabel(10)
    sprite('es400eff_atk1', 25)	# 1-25	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB', -1)
    Unknown38(4, 1)
    physicsXImpulse(2500)
    sprite('es400eff_atk2', 100)	# 26-125	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')
    physicsXImpulse(65000)
    ExitState()
    label(10)
    sprite('es400eff_atk1', 3)	# 126-128	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB2', -1)
    Unknown38(4, 1)
    physicsXImpulse(65000)
    sprite('es400eff_atk2', 100)	# 129-228	 **attackbox here**

@State
def es400_B_2ndB():

    def upon_IMMEDIATE():
        callSubroutine('es400_Init')
        Unknown9215()
        Unknown1007(128000)
        teleportRelativeX(110000)

        def upon_43():
            if (SLOT_48 == 119):
                GFX_0('es400_B_2ndEX', -1)
                Unknown26('es400_A')
                Unknown26('esef_400eff_MatomeA')
                Unknown13(25)
                Unknown26('esef_400eff2nd_MatomeB')
                Unknown26('esef_400eff2nd_MatomeB2')
    Unknown48('190000000200000033000000030000000200000033000000')
    if SLOT_51:
        _gotolabel(10)
    sprite('es400eff_atk1', 25)	# 1-25	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB', -1)
    Unknown38(4, 1)
    physicsXImpulse(2500)
    sprite('es400eff_atk2', 100)	# 26-125	 **attackbox here**
    Unknown21015('73686f74320000000000000000000000000000000000000000000000000000007800000000000000')
    physicsXImpulse(65000)
    ExitState()
    label(10)
    sprite('es400eff_atk1', 3)	# 126-128	 **attackbox here**
    GFX_0('esef_400eff2nd_MatomeB2', -1)
    Unknown38(4, 1)
    physicsXImpulse(65000)
    sprite('es400eff_atk2', 100)	# 129-228	 **attackbox here**
