
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
