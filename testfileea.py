
@State
def EffAtk6D():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2009()
        AttackLevel_(4)
        AttackP1(100)
        AirHitstunAnimation(10)
        AirUntechableTime(26)
        AirPushbackY(20000)
        PushbackX(19800)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown9016(1)
        Unknown9019(1)

        def upon_12():
            ScreenShake(5000, 5000)
        Unknown23078(1)
        teleportRelativeX(120000)
        Unknown23089('0100000000000000000000000000000000000000010000000100000001000000')

        def upon_54():
            Unknown23027()
    sprite('vrjnef213_00', 3)	# 1-3	 **attackbox here**
    GFX_0('EffAtk6D_Env', -1)
    Unknown3033()
    Unknown3001(128)
    Unknown1096(600)
    Unknown1099(-3)
    SFX_0('017_freeze_0')
    Unknown2003(1)
    sprite('vrjnef213_00', 3)	# 4-6	 **attackbox here**
    Unknown3001(255)
    Unknown1096(900)
    Unknown1099(-3)
    SFX_0('017_freeze_0')
    sprite('vrjnef213_00', 6)	# 7-12	 **attackbox here**
    Unknown1096(1100)
    Unknown1099(-3)
    SFX_0('017_freeze_1')
    Unknown2003(0)
    sprite('vrjnef213_01', 4)	# 13-16
    Unknown3001(200)
    Unknown3004(-20)
    physicsXImpulse(1200)
    Unknown1015(10)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceCirclePtc', 2)
    GFX_0('IceBreakPtcL', 1)
    GFX_0('IceBreakPtcL', 2)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 6)
    GFX_0('IceBreakPtcS', 7)
    GFX_0('IceBreakPtcS', 8)
    SFX_0('018_ice_break_1')
    sprite('vrjnef213_03', 4)	# 17-20
    sprite('vrjnef213_05', 4)	# 21-24



@State
def EffAtk6D_Env():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vrjnef213env', 10)	# 1-10
    Unknown3033()
    Unknown1096(1000)
    Unknown1099(20)
    Unknown3001(0)
    Unknown3004(24)
    physicsXImpulse(800)
    sprite('vrjnef213env', 10)	# 11-20
    Unknown1099(-5)
    Unknown3001(240)
    Unknown3004(-24)
    physicsXImpulse(1000)


@State
def IceBreakPtcL():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    Unknown4047(96, 96, 96)
    Unknown4045('6a6e65665f69636562726c000000000000000000000000000000000000000000ffffffff')

@State
def IceBreakPtcM():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    Unknown4047(96, 96, 96)
    Unknown4045('6a6e65665f69636562726d000000000000000000000000000000000000000000ffffffff')

@State
def IceBreakPtcS():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    Unknown4047(96, 96, 96)
    Unknown4045('6a6e65665f696365627273000000000000000000000000000000000000000000ffffffff')
