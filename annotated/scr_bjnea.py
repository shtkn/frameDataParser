@State
def EMB_JN():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f4a4e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
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
def EMB_JN_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f4a4e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
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
def EMB_JN_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('65665f656d625f4a4e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
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

@Subroutine
def CheckOverDriveShotFreeze():
    if SLOT_109:
        Unknown9287()
        Unknown9250(3)
        Unknown11001(6, 0, 5)

        def upon_12():
            ScreenShake(20000, 20000)

@Subroutine
def CheckOverDriveSpecial():
    if SLOT_109:
        Unknown11043(100)
        Unknown23181(0)

@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('6a6e65665f6d635f7374612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown4061(1)
        Unknown21004(240)
    sprite('null', 42)	# 1-42

@State
def ModelMagicCircle2():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('6a6e65665f6d635f7369742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown4061(1)
        Unknown21004(240)
    sprite('null', 42)	# 1-42

@State
def ModelMagicCircle3():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('6a6e65665f6d635f6a756d2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown4061(1)
        Unknown21004(240)
    sprite('null', 30)	# 1-30

@State
def ModelMagicCircle4():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('6a6e65665f6d635f6673692e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown4061(1)
        Unknown21004(240)
    sprite('null', 42)	# 1-42

@State
def jn_DD_2_ex():

    def upon_IMMEDIATE():
        Unknown4009(3)
        teleportRelativeX(128000)
        Unknown1007(256000)
        Unknown4051(2)
        Unknown23067('jnef_DD_ex')
    sprite('null', 300)	# 1-300

@State
def EffNoutou():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2055(12)
    sprite('null', 12)	# 1-12
    Unknown3038(1)
    GFX_2('jnef_bl')
    SFX_3('jnse_00')

@State
def EffYukikaze():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767
    GFX_2('jnef_yukikaze')

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

@State
def IceMakePtc():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    GFX_1('jnef_icesmoke00', -1)
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f696365707463303000000000000000000000000000000000000000ffffffff')
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f696365707463000000000000000000000000000000000000000000ffffffff')

@State
def IceCirclePtc():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    Unknown4047(175, 175, 175)
    Unknown4045('6a6e65665f636972636c65303000000000000000000000000000000000000000ffffffff')

@State
def IceBreakPtc601():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    Unknown4047(96, 96, 96)
    Unknown4049(500)
    Unknown4045('6a6e65665f69636562726d000000000000000000000000000000000000000000ffffffff')

@State
def jnef601ptc():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    Unknown4047(175, 96, 240)
    Unknown4045('6a6e65663630315f6d6330300000000000000000000000000000000000000000ffffffff')
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65663630315f6d6330310000000000000000000000000000000000000000ffffffff')
    Unknown4047(175, 175, 175)
    Unknown4045('6a6e65663630315f6d6330320000000000000000000000000000000000000000ffffffff')
    Unknown4047(175, 175, 175)
    Unknown4045('6a6e65663630315f6d6330330000000000000000000000000000000000000000ffffffff')
    Unknown4047(175, 175, 175)
    Unknown4045('6a6e65663630315f636972636c65303000000000000000000000000000000000ffffffff')
    Unknown4047(175, 175, 175)
    Unknown4045('6a6e656636303100000000000000000000000000000000000000000000000000ffffffff')

@State
def jnef611_hane():
    sprite('null', 1)	# 1-1
    Unknown4061(1)
    Unknown3038(1)
    Unknown4047(175, 175, 1)
    Unknown4045('6a6e65663631315f68616e65000000000000000000000000000000000000000002000000')

@State
def jnef_25percent():
    sprite('null', 1)	# 1-1
    Unknown1007(300000)
    Unknown4045('6a6e65665f323570657263656e74000000000000000000000000000000000000ffffffff')

@State
def zan_a0():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan_a0', 20)	# 1-20
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(8)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)

@State
def zan_b0():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan202', 24)	# 1-24
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(10)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)

@State
def zan_d0():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan_d0', 1)	# 1-1
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(8)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)
    sprite('vrzan_d1', 1)	# 2-2
    sprite('vrzan_d2', 12)	# 3-14

@State
def zan_e0():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan_e0', 12)	# 1-12
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(6)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)

@State
def zan407():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan407', 12)	# 1-12
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(10)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)

@State
def zan408():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan408_16z', 6)	# 1-6
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(14)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)

@State
def zan409():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan409_06z', 6)	# 1-6
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(14)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)

@State
def zan412():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan412_00', 2)	# 1-2
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(8)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)
    sprite('vrzan412_01', 2)	# 3-4
    sprite('vrzan412_01', 16)	# 5-20
    physicsYImpulse(-4000)

@State
def zan414():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
    sprite('vrzan414_00', 2)	# 1-2
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(14)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)
    sprite('vrzan414_01', 20)	# 3-22

@State
def zan235():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(1)
        teleportRelativeX(130000)
        Unknown1007(-20000)
    sprite('vrzan235_00', 24)	# 1-24
    Unknown3053(1)
    Unknown3040(1)
    Unknown3041(10)
    Unknown3042(242)
    Unknown3043(241)
    Unknown3044(250)

@State
def IcicleSub():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2010()
        Unknown4006(2)
        Unknown3033()
        Unknown3001(255)
    sprite('vrjnef233_00', 3)	# 1-3
    GFX_0('IceMakePtc', -1)
    sprite('vrjnef233_01', 3)	# 4-6
    sprite('vrjnef233_02', 3)	# 7-9
    sprite('vrjnef233_03', 13)	# 10-22
    Unknown3001(200)
    Unknown3004(-20)
    Unknown4047(111, 111, 111)
    Unknown4049(400)
    Unknown4045('6a6e65665f69636562726d00000000000000000000000000000000000000000000000000')
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceMakePtc', -1)
    sprite('vrjnef233_04', 12)	# 23-34

@State
def Icicle_Env():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown3001(0)
    sprite('vrjnef233env', 3)	# 1-3
    Unknown1096(200)
    Unknown1099(30)
    Unknown3004(10)
    sprite('vrjnef233env', 3)	# 4-6
    Unknown1096(900)
    sprite('vrjnef233env', 3)	# 7-9
    Unknown1096(950)
    sprite('vrjnef233env', 16)	# 10-25
    Unknown1099(-10)
    Unknown3004(-10)

@State
def IcicleAttack():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2009()
        AttackLevel_(4)
        AttackP2(75)
        AirPushbackY(20000)
        AirPushbackX(-6000)
        PushbackX(-12000)
        Hitstop(18)
        Unknown9016(1)
        Unknown9019(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(21)
        Unknown11058('0000000000000000000000000100000000000000')
        teleportRelativeX(-100000)
        Unknown3033()
        Unknown1096(1000)
        Unknown3001(255)
        Unknown23089('0100000000000000000000000000000000000000010000000100000001000000')

        def upon_54():
            Unknown23027()
        Unknown2034(1)
        Unknown2053(1)
    sprite('vrjnef233atk_00', 3)	# 1-3
    Unknown1099(-5)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef233atk_01', 3)	# 4-6
    Unknown1096(800)
    Unknown1099(-5)
    GFX_0('Icicle_Env', -1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    sprite('vrjnef233atk_02ex01', 3)	# 7-9
    Unknown1099(0)
    Unknown1096(900)
    sprite('vrjnef233atk_02', 3)	# 10-12	 **attackbox here**
    Unknown1096(1000)
    Unknown1099(5)
    SFX_0('017_freeze_1')
    SFX_0('017_freeze_1')
    sprite('vrjnef233atk_03', 3)	# 13-15
    Unknown1099(0)
    Unknown3001(200)
    Unknown3004(-15)
    sprite('vrjnef233atk_04', 3)	# 16-18
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceCirclePtc', 2)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 1)
    GFX_0('IceBreakPtcL', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcM', 6)
    GFX_0('IceBreakPtcM', 7)
    GFX_0('IceBreakPtcM', 8)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 6)
    GFX_0('IceBreakPtcS', 7)
    GFX_0('IceBreakPtcS', 8)
    GFX_0('IceBreakPtcS', 9)
    SFX_0('018_ice_break_1')
    sprite('vrjnef233atk_05', 10)	# 19-28

@State
def EffAtk5D():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4011(3)
        Unknown3001(255)
    sprite('vrjnef203_01ex', 2)	# 1-2	 **attackbox here**
    GFX_0('EffAtk5D_Env', -1)
    Unknown1056(750)
    Unknown1064(900)
    SFX_0('017_freeze_0')
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    sprite('vrjnef203_01ex', 7)	# 3-9	 **attackbox here**
    Unknown1056(900)
    Unknown1064(950)
    SFX_0('017_freeze_0')
    sprite('vrjnef203_01', 4)	# 10-13	 **attackbox here**
    Unknown4009(0)
    Unknown4007(0)
    Unknown3004(-15)
    Unknown1096(1000)
    Unknown1099(1)
    SFX_0('017_freeze_1')
    sprite('vrjnef203_02', 4)	# 14-17	 **attackbox here**
    sprite('vrjnef203_03', 4)	# 18-21	 **attackbox here**
    GFX_0('IceCirclePtc', 2)
    GFX_0('IceCirclePtc', 3)
    GFX_0('IceCirclePtc', 9)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcM', 6)
    GFX_0('IceBreakPtcM', 8)
    GFX_0('IceBreakPtcM', 9)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 6)
    GFX_0('IceBreakPtcS', 10)
    GFX_0('IceBreakPtcS', 11)
    GFX_0('IceBreakPtcS', 12)
    SFX_0('018_ice_break_1')
    sprite('vrjnef203_04', 20)	# 22-41	 **attackbox here**

@State
def EffAtk5D_Env():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
    sprite('vrjnef203env', 10)	# 1-10
    Unknown3033()
    Unknown1096(1000)
    Unknown1099(2)
    Unknown3001(0)
    Unknown3004(16)
    sprite('vrjnef203env', 20)	# 11-30
    Unknown1099(-5)
    Unknown3001(160)
    Unknown3004(-8)

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
def EffAtk8D():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown3001(255)
    sprite('vrjnef253_00', 2)	# 1-2
    GFX_0('EffAtk8D_Env', -1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    Unknown1096(400)
    Unknown1099(-3)
    SFX_0('017_freeze_0')
    sprite('vrjnef253_00', 2)	# 3-4
    Unknown1096(650)
    Unknown1099(-3)
    SFX_0('017_freeze_0')
    sprite('vrjnef253_00', 12)	# 5-16
    Unknown1096(800)
    Unknown1099(5)
    Unknown3001(255)
    Unknown3004(-24)
    SFX_0('017_freeze_1')

@State
def EffAtk8D_Env():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown3033()
    sprite('vrjnef253env', 4)	# 1-4
    Unknown1096(300)
    Unknown1099(100)
    Unknown3001(0)
    Unknown3004(24)
    sprite('vrjnef253env', 8)	# 5-12
    Unknown1099(5)
    Unknown3001(240)
    Unknown3004(-20)

@State
def jnef311():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(2)
        Unknown3033()
        Unknown2019(-1000)
    sprite('vrjnef311_00', 2)	# 1-2	 **attackbox here**
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffffd0070000d0070000')
    Unknown3001(192)
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef311_01', 2)	# 3-4	 **attackbox here**
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef311_02', 2)	# 5-6	 **attackbox here**
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef311_03', 2)	# 7-8	 **attackbox here**
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef311_04', 2)	# 9-10	 **attackbox here**
    SFX_0('017_freeze_1')
    SFX_0('017_freeze_1')
    sprite('vrjnef311_05', 25)	# 11-35	 **attackbox here**
    sprite('vrjnef311_06', 3)	# 36-38	 **attackbox here**
    sprite('vrjnef311_07', 3)	# 39-41	 **attackbox here**
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceCirclePtc', 6)
    GFX_0('IceBreakPtcL', 6)
    GFX_0('IceBreakPtcM', 7)
    GFX_0('IceBreakPtcM', 8)
    GFX_0('IceBreakPtcM', 9)
    GFX_0('IceBreakPtcM', 10)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 7)
    GFX_0('IceBreakPtcS', 8)
    GFX_0('IceBreakPtcS', 9)
    GFX_0('IceBreakPtcS', 10)
    SFX_0('018_ice_break_1')
    sprite('vrjnef311_08', 12)	# 42-53	 **attackbox here**
    Unknown3004(-30)

@State
def jnef321top():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(2)
        Unknown3033()
        Unknown1096(-1000)
    sprite('vrjnef321_00', 2)	# 1-2	 **attackbox here**
    Unknown3001(192)
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef321_01', 2)	# 3-4	 **attackbox here**
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef321_02', 2)	# 5-6	 **attackbox here**
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef321_03', 2)	# 7-8	 **attackbox here**
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('vrjnef321_04', 2)	# 9-10	 **attackbox here**
    SFX_0('017_freeze_1')
    SFX_0('017_freeze_1')
    sprite('vrjnef321_05', 25)	# 11-35	 **attackbox here**
    sprite('vrjnef321_06', 3)	# 36-38	 **attackbox here**
    sprite('vrjnef321_07', 3)	# 39-41	 **attackbox here**
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcM', 7)
    GFX_0('IceBreakPtcM', 8)
    GFX_0('IceBreakPtcM', 9)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 7)
    GFX_0('IceBreakPtcS', 8)
    GFX_0('IceBreakPtcS', 9)
    SFX_0('018_ice_break_1')
    sprite('vrjnef321_08', 12)	# 42-53	 **attackbox here**
    Unknown3004(-30)

@State
def jnef321bottom():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(2)
        Unknown3033()
    sprite('vrjnef321_00', 2)	# 1-2	 **attackbox here**
    Unknown3001(192)
    sprite('vrjnef321_01', 2)	# 3-4	 **attackbox here**
    sprite('vrjnef321_02', 2)	# 5-6	 **attackbox here**
    sprite('vrjnef321_03', 2)	# 7-8	 **attackbox here**
    sprite('vrjnef321_04', 2)	# 9-10	 **attackbox here**
    sprite('vrjnef321_05', 25)	# 11-35	 **attackbox here**
    sprite('vrjnef321_06', 3)	# 36-38	 **attackbox here**
    sprite('vrjnef321_07', 3)	# 39-41	 **attackbox here**
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcM', 7)
    GFX_0('IceBreakPtcM', 8)
    GFX_0('IceBreakPtcM', 9)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 7)
    GFX_0('IceBreakPtcS', 8)
    GFX_0('IceBreakPtcS', 9)
    sprite('vrjnef321_08', 12)	# 42-53	 **attackbox here**
    Unknown3004(-30)

@State
def EFF28AtkA():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown3033()
        Unknown3001(255)
    sprite('vrjnef405_00', 1)	# 1-1
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    sprite('vrjnef405_01', 3)	# 2-4
    sprite('vrjnef405_02', 3)	# 5-7	 **attackbox here**
    sprite('vrjnef405_03', 3)	# 8-10	 **attackbox here**
    sprite('vrjnef405_04', 3)	# 11-13	 **attackbox here**
    sprite('vrjnef405_05', 3)	# 14-16	 **attackbox here**
    sprite('vrjnef405_06', 8)	# 17-24
    Unknown3001(200)
    Unknown3004(-30)

@State
def EFF28AtkB():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown3001(255)
        Unknown1096(1000)
    sprite('vrjnef405_00', 3)	# 1-3
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    sprite('vrjnef405_01', 3)	# 4-6
    sprite('vrjnef405_02', 3)	# 7-9	 **attackbox here**
    sprite('vrjnef405_03', 3)	# 10-12	 **attackbox here**
    sprite('vrjnef405_04', 3)	# 13-15	 **attackbox here**
    sprite('vrjnef405_05', 3)	# 16-18	 **attackbox here**
    sprite('vrjnef405_06', 8)	# 19-26
    Unknown3001(200)
    Unknown3004(-30)

@State
def EFF28AtkC():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown1064(1400)
        Unknown3001(255)
    sprite('vrjnef406_00', 2)	# 1-2
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    sprite('vrjnef406_01', 2)	# 3-4	 **attackbox here**
    sprite('vrjnef406_02', 2)	# 5-6	 **attackbox here**
    sprite('vrjnef406_03', 2)	# 7-8	 **attackbox here**
    sprite('vrjnef406_04', 2)	# 9-10	 **attackbox here**
    sprite('vrjnef406_05', 2)	# 11-12	 **attackbox here**
    sprite('vrjnef406_06', 2)	# 13-14	 **attackbox here**
    sprite('vrjnef406_07', 2)	# 15-16	 **attackbox here**
    sprite('vrjnef406_08', 6)	# 17-22
    Unknown3001(200)
    Unknown3004(-40)

@State
def EFF28AtkD():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown3001(255)
        Unknown1096(1000)
    sprite('vrjnef407_00', 3)	# 1-3
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    sprite('vrjnef407_01', 2)	# 4-5
    sprite('vrjnef407_02', 2)	# 6-7
    sprite('vrjnef407_03', 2)	# 8-9
    sprite('vrjnef407_04', 2)	# 10-11
    sprite('vrjnef407_05', 6)	# 12-17
    physicsXImpulse(-3000)
    physicsYImpulse(750)
    Unknown3001(200)
    Unknown3004(-30)

@State
def EFF413C():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown1007(224000)
        Unknown1096(2000)
    sprite('vrjnef413_00', 3)	# 1-3
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    sprite('vrjnef413_01', 6)	# 4-9
    sprite('vrjnef413_02', 3)	# 10-12
    sprite('vrjnef413_03', 8)	# 13-20
    Unknown3001(200)
    Unknown3004(-30)

@State
def EFF413D():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown1007(224000)
        Unknown1096(2000)
    sprite('vrjnef413_10', 3)	# 1-3
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('vrjnef413_11', 3)	# 4-6
    sprite('vrjnef413_12', 3)	# 7-9
    sprite('vrjnef413_13', 3)	# 10-12
    Unknown3001(200)
    Unknown3004(-30)

@State
def IceBoard():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown2019(100)
        Unknown3033()
        Unknown1007(110000)

        def upon_45():
            if (not SLOT_51):
                Unknown48('190000000200000053000000030000000200000053000000')

        def upon_43():
            if (SLOT_48 == 4001):
                SLOT_51 = 1
                Unknown4007(3)
                Unknown1000(0)
        Unknown2055(50)
    sprite('vrjnef408_00', 2)	# 1-2
    GFX_0('IceMakePtc', 0)
    Unknown1064(0)
    Unknown1067(100)
    SFX_0('017_freeze_0')
    sprite('vrjnef408_00', 2)	# 3-4
    SFX_0('017_freeze_1')
    sprite('vrjnef408_00', 2)	# 5-6
    SFX_0('017_freeze_0')
    sprite('vrjnef408_00', 2)	# 7-8
    SFX_0('017_freeze_1')
    sprite('vrjnef408_00', 2)	# 9-10
    SFX_0('017_freeze_0')
    label(0)
    sprite('vrjnef408_00', 4)	# 11-14
    Unknown4049(2000)
    Unknown4045('6a6e65665f69636573686f74000000000000000000000000000000000000000000000000')
    Unknown1067(0)
    loopRest()
    gotoLabel(0)

@State
def IceBoardASS():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown2019(100)
        Unknown3033()
        Unknown1007(110000)

        def upon_45():
            if (not SLOT_51):
                Unknown48('190000000200000053000000030000000200000053000000')

        def upon_43():
            if (SLOT_48 == 4001):
                SLOT_51 = 1
                Unknown4007(3)
                Unknown1000(0)
        Unknown2055(50)
    sprite('vrjnef408_00', 2)	# 1-2
    GFX_0('IceMakePtc', 0)
    Unknown1064(0)
    Unknown1067(100)
    SFX_0('017_freeze_0')
    sprite('vrjnef408_00', 2)	# 3-4
    SFX_0('017_freeze_1')
    sprite('vrjnef408_00', 2)	# 5-6
    SFX_0('017_freeze_0')
    sprite('vrjnef408_00', 2)	# 7-8
    SFX_0('017_freeze_1')
    sprite('vrjnef408_00', 2)	# 9-10
    SFX_0('017_freeze_0')
    label(0)
    sprite('vrjnef408_00', 4)	# 11-14
    Unknown4049(2000)
    Unknown4045('6a6e65665f69636573686f74000000000000000000000000000000000000000000000000')
    Unknown1067(0)
    loopRest()
    gotoLabel(0)

@State
def IceBoard_koware():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(0)
        Unknown2019(100)
        Unknown3033()
        Unknown1007(110000)
    sprite('vrjnef408_00', 3)	# 1-3
    GFX_0('IceMakePtc', 0)
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562726200000000000000000000000000000000000000000000000000')
    physicsXImpulse(35000)
    Unknown1015(-15000)
    Unknown3001(164)
    Unknown3004(-20)
    Unknown1096(1000)
    Unknown1099(-15)
    SFX_0('018_ice_break_0')
    sprite('vrjnef408_00', 3)	# 4-6
    SFX_0('018_ice_break_1')
    sprite('vrjnef408_00', 3)	# 7-9
    SFX_0('018_ice_break_0')
    sprite('vrjnef408_00', 3)	# 10-12
    sprite('vrjnef408_00', 3)	# 13-15
    SFX_0('018_ice_break_0')
    sprite('vrjnef408_00', 5)	# 16-20

@State
def ice_shot():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2010()
        AttackLevel_(3)
        Hitstop(8)
        Unknown9019(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown1096(750)
        Unknown53(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 1)
        loopRelated(17, 75)

        def upon_17():
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 5109):
                Unknown23090(25)
            if (SLOT_48 == 4300):
                Unknown23090(25)
    sprite('vrjnef400_00', 1)	# 1-1
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_01', 1)	# 2-2
    sprite('vrjnef400_02', 1)	# 3-3
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_03', 1)	# 4-4
    sprite('vrjnef400_04', 1)	# 5-5
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_05', 1)	# 6-6
    sprite('vrjnef400_06', 1)	# 7-7
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_07', 1)	# 8-8
    sprite('vrjnef400_08', 1)	# 9-9
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_1')
    Unknown1028(3200)
    sprite('vrjnef400_09', 3)	# 10-12	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)	# 13-15	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)	# 16-18	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    label(0)
    sprite('vrjnef400_09', 3)	# 19-21	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 22-31
    Unknown1084(1)
    StartMultihit()
    Unknown3004(-25)
    SFX_0('018_ice_break_1')
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562720000000000000000000000000000000000000000000000000000')
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    clearUponHandler(54)
    clearUponHandler(10)

@State
def ice_shot_Assist():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2010()
        AttackLevel_(3)
        Hitstop(8)
        Unknown12051(2)
        Unknown12052(1)
        Unknown11042(1)
        Unknown9019(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown1096(750)
        Unknown53(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 1)
        loopRelated(17, 75)

        def upon_17():
            Unknown23090(25)
        if SLOT_136:
            Unknown10000(80)
    sprite('vrjnef400_00', 1)	# 1-1
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_01', 1)	# 2-2
    sprite('vrjnef400_02', 1)	# 3-3
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_03', 1)	# 4-4
    sprite('vrjnef400_04', 1)	# 5-5
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_05', 1)	# 6-6
    sprite('vrjnef400_06', 1)	# 7-7
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_07', 1)	# 8-8
    sprite('vrjnef400_08', 1)	# 9-9
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_1')
    Unknown1028(3200)
    sprite('vrjnef400_09', 3)	# 10-12	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)	# 13-15	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)	# 16-18	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    label(0)
    sprite('vrjnef400_09', 3)	# 19-21	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 22-31
    Unknown1084(1)
    StartMultihit()
    Unknown3004(-25)
    SFX_0('018_ice_break_1')
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562720000000000000000000000000000000000000000000000000000')
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    clearUponHandler(54)
    clearUponHandler(10)

@State
def air_ice_shot():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2010()
        AttackLevel_(3)
        Hitstop(8)
        Unknown9019(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown1096(750)
        Unknown53(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 1)
        loopRelated(17, 75)

        def upon_17():
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 5109):
                Unknown23090(25)
            if (SLOT_48 == 4300):
                Unknown23090(25)
    sprite('vrjnef400_00', 2)	# 1-2
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_01', 2)	# 3-4
    sprite('vrjnef400_02', 2)	# 5-6
    SFX_0('017_freeze_0')
    sprite('vrjnef400_03', 2)	# 7-8
    GFX_0('IceMakePtc', 0)
    sprite('vrjnef400_04', 1)	# 9-9
    SFX_0('017_freeze_0')
    sprite('vrjnef400_05', 2)	# 10-11
    sprite('vrjnef400_06', 1)	# 12-12
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_07', 2)	# 13-14
    sprite('vrjnef400_08', 2)	# 15-16
    SFX_0('017_freeze_1')
    Unknown1108(0)
    physicsXImpulse(20000)
    Unknown1028(1100)
    sprite('vrjnef400_09', 3)	# 17-19	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)	# 20-22	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)	# 23-25	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    label(0)
    sprite('vrjnef400_09', 3)	# 26-28	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 29-38
    Unknown3004(-25)
    Unknown2001()
    SFX_0('018_ice_break_1')
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562720000000000000000000000000000000000000000000000000000')
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    physicsXImpulse(0)
    Unknown1028(0)
    physicsYImpulse(0)
    setGravity(0)
    clearUponHandler(54)
    clearUponHandler(10)

@State
def ice_shot_ex():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        Unknown11092(1)
        Hitstop(8)
        AirUntechableTime(36)
        Unknown9019(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(30)
            Unknown1034(200)
        Unknown3060('0000000076725f6e62635f73686f745f6c69676874000000000000000000000000000000')
        Unknown3066(0, 2000)
        Unknown3067(0, 2000)
        Unknown3063(0, -100000)
        Unknown3064(0, 10000)
        Unknown1096(1000)
        callSubroutine('CheckOverDriveSpecial')
        teleportRelativeX(100000)
        Unknown23027()
        Unknown23089('0300000001000000010000000100000001000000000000000300000000000000')
        sendToLabelUpon(54, 9)
        loopRelated(17, 120)

        def upon_17():
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 5109):
                Unknown23090(25)
            if (SLOT_48 == 4200):
                Unknown23090(25)
    sprite('vrjnef400_00', 1)	# 1-1
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_01', 1)	# 2-2
    sprite('vrjnef400_02', 1)	# 3-3
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_03', 1)	# 4-4
    sprite('vrjnef400_04', 1)	# 5-5
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_05', 1)	# 6-6
    sprite('vrjnef400_06', 1)	# 7-7
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_07', 1)	# 8-8
    sprite('vrjnef400_08', 1)	# 9-9
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_1')
    physicsXImpulse(500)
    Unknown1028(50)
    SLOT_52 = 14
    sprite('vrjnef400_09', 9)	# 10-18	 **attackbox here**
    StartMultihit()
    label(11)
    sprite('vrjnef400_09', 3)	# 19-21	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    RefreshMultihit()
    if (not SLOT_53):
        if SLOT_52:
            SLOT_52 = (SLOT_52 + (-1))
        else:
            SLOT_53 = 1
            Unknown1028(3000)
    loopRest()
    gotoLabel(11)
    label(9)
    sprite('keep', 10)	# 22-31
    Unknown1084(1)
    StartMultihit()
    Unknown3004(-25)
    SFX_0('018_ice_break_1')
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562720000000000000000000000000000000000000000000000000000')
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    clearUponHandler(54)
    clearUponHandler(10)

@State
def ice_shot_ex_Assist():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2010()
        AttackLevel_(3)
        Damage(1200)
        AirPushbackY(15000)
        AttackP1(70)
        Unknown11092(1)
        Hitstop(8)
        AirUntechableTime(36)
        Unknown9019(1)
        Unknown11042(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(30)
            Unknown1034(200)
        Unknown3060('0000000076725f6e62635f73686f745f6c69676874000000000000000000000000000000')
        Unknown3066(0, 2000)
        Unknown3067(0, 2000)
        Unknown3063(0, -100000)
        Unknown3064(0, 10000)
        Unknown1096(1000)
        callSubroutine('CheckOverDriveSpecial')
        teleportRelativeX(100000)
        Unknown23027()
        Unknown23089('0300000001000000010000000100000001000000000000000300000000000000')
        sendToLabelUpon(54, 9)
        loopRelated(17, 120)

        def upon_17():
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 5109):
                Unknown23090(25)
            if (SLOT_48 == 4200):
                Unknown23090(25)
    sprite('vrjnef400_00', 1)	# 1-1
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_01', 1)	# 2-2
    sprite('vrjnef400_02', 1)	# 3-3
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_03', 1)	# 4-4
    sprite('vrjnef400_04', 1)	# 5-5
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_05', 1)	# 6-6
    sprite('vrjnef400_06', 1)	# 7-7
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_07', 1)	# 8-8
    sprite('vrjnef400_08', 1)	# 9-9
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_1')
    physicsXImpulse(500)
    Unknown1028(50)
    SLOT_52 = 14
    sprite('vrjnef400_09', 9)	# 10-18	 **attackbox here**
    StartMultihit()
    label(11)
    sprite('vrjnef400_09', 3)	# 19-21	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    RefreshMultihit()
    if (not SLOT_53):
        if SLOT_52:
            SLOT_52 = (SLOT_52 + (-1))
        else:
            SLOT_53 = 1
            Unknown1028(3000)
    loopRest()
    gotoLabel(11)
    label(9)
    sprite('keep', 10)	# 22-31
    Unknown1084(1)
    StartMultihit()
    Unknown3004(-25)
    SFX_0('018_ice_break_1')
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562720000000000000000000000000000000000000000000000000000')
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    clearUponHandler(54)
    clearUponHandler(10)

@State
def air_ice_shot_ex():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        Unknown11092(1)
        Hitstop(8)
        AirUntechableTime(36)
        Unknown9019(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_ON_HIT_OR_BLOCK():
            Unknown1019(30)
            Unknown1034(200)
        Unknown3060('0000000076725f6e62635f73686f745f6c69676874000000000000000000000000000000')
        Unknown3066(0, 2000)
        Unknown3067(0, 2000)
        Unknown3063(0, -100000)
        Unknown3064(0, 10000)
        Unknown1096(1000)
        callSubroutine('CheckOverDriveSpecial')
        teleportRelativeX(100000)
        Unknown23027()
        Unknown23089('0300000001000000010000000100000001000000000000000300000000000000')
        sendToLabelUpon(54, 9)
        loopRelated(17, 120)

        def upon_17():
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 5109):
                Unknown23090(25)
            if (SLOT_48 == 4200):
                Unknown23090(25)
    sprite('vrjnef400_00', 1)	# 1-1
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_01', 1)	# 2-2
    sprite('vrjnef400_02', 1)	# 3-3
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_03', 1)	# 4-4
    sprite('vrjnef400_04', 1)	# 5-5
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_05', 1)	# 6-6
    sprite('vrjnef400_06', 1)	# 7-7
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_0')
    sprite('vrjnef400_07', 1)	# 8-8
    sprite('vrjnef400_08', 1)	# 9-9
    GFX_0('IceMakePtc', 0)
    SFX_0('017_freeze_1')
    physicsXImpulse(500)
    Unknown1028(1000)
    SLOT_52 = 14
    label(11)
    sprite('vrjnef400_09', 3)	# 10-12	 **attackbox here**
    GFX_1('jnef_iceshot', 0)
    RefreshMultihit()
    if (not SLOT_53):
        if SLOT_52:
            SLOT_52 = (SLOT_52 + (-1))
        else:
            SLOT_53 = 1
            Unknown1028(3000)
    loopRest()
    gotoLabel(11)
    label(9)
    sprite('keep', 10)	# 13-22
    Unknown1084(1)
    StartMultihit()
    Unknown3004(-25)
    SFX_0('018_ice_break_1')
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562720000000000000000000000000000000000000000000000000000')
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    clearUponHandler(54)
    clearUponHandler(10)

@State
def ice_shot_ex2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(16000)
        AirUntechableTime(36)
        Unknown9019(1)
        PushbackX(6000)
        Unknown2019(-100)
        Unknown9021(1)
        Unknown30065(0)
        Unknown11091(10)
        Unknown23027()
        Unknown2053(1)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
        callSubroutine('CheckOverDriveSpecial')
        teleportRelativeX(150000)
        Unknown23027()
        Unknown23089('0300000001000000010000000100000001000000000000000300000000000000')
        sendToLabelUpon(54, 9)
        loopRelated(17, 180)

        def upon_17():
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 5109):
                Unknown23090(25)
            if (SLOT_48 == 4102):
                Unknown23090(25)
    sprite('vrjnef400_50', 10)	# 1-10
    GFX_0('EffAtk8D_Env', -1)
    Unknown1096(450)
    Unknown1099(50)
    Unknown3001(64)
    Unknown3004(20)
    GFX_0('jnef_400ice_pt', -1)
    GFX_0('ModelMagicCircle3', -1)
    Unknown36(1)
    Unknown1096(1000)
    Unknown35()
    sprite('vrjnef400_50', 1)	# 11-11
    GFX_0('jnef_400_env', -1)
    Unknown1096(1000)
    Unknown1099(0)
    Unknown3001(255)
    Unknown3004(0)
    label(0)
    sprite('vrjnef400_50col', 6)	# 12-17	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrjnef400_50', 30)	# 18-47
    Unknown3004(-12)
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    SFX_0('018_ice_break_1')
    Unknown21015('6a6e65665f3430305f656e7600000000000000000000000000000000000000000510000000000000')
    Unknown21015('6a6e65665f3430306963655f70740000000000000000000000000000000000000510000000000000')

@State
def air_ice_shot_ex2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(16000)
        AirUntechableTime(36)
        Unknown9019(1)
        PushbackX(6000)
        Unknown2019(-100)
        Unknown9021(1)
        Unknown30065(0)
        Unknown11091(10)
        Unknown23027()
        Unknown2053(1)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
        callSubroutine('CheckOverDriveSpecial')
        teleportRelativeX(150000)
        Unknown23027()
        Unknown23089('0300000001000000010000000100000001000000000000000300000000000000')
        sendToLabelUpon(54, 9)
        loopRelated(17, 180)

        def upon_17():
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 5109):
                Unknown23090(25)
            if (SLOT_48 == 4102):
                Unknown23090(25)
    sprite('vrjnef400_50', 10)	# 1-10
    GFX_0('EffAtk8D_Env', -1)
    Unknown1096(450)
    Unknown1099(50)
    Unknown3001(64)
    Unknown3004(20)
    GFX_0('jnef_400ice_pt', -1)
    GFX_0('ModelMagicCircle3', -1)
    Unknown36(1)
    Unknown1096(1000)
    Unknown35()
    sprite('vrjnef400_50', 1)	# 11-11
    GFX_0('jnef_400_env', -1)
    Unknown1096(1000)
    Unknown1099(0)
    Unknown3001(255)
    Unknown3004(0)
    label(0)
    sprite('vrjnef400_50col', 6)	# 12-17	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrjnef400_50', 30)	# 18-47
    Unknown3004(-12)
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    SFX_0('018_ice_break_1')
    Unknown21015('6a6e65665f3430305f656e7600000000000000000000000000000000000000000510000000000000')
    Unknown21015('6a6e65665f3430306963655f70740000000000000000000000000000000000000510000000000000')

@State
def jnef_400_env():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        Unknown3001(96)

        def upon_43():
            if (SLOT_48 == 4101):
                sendToLabel(0)
    label(0)
    sprite('vrjnef400env', 15)	# 1-15
    GFX_1('jnef_400bk', -1)
    gotoLabel(0)
    label(0)
    sprite('vrjnef400env', 32)	# 16-47
    Unknown3004(-4)

@State
def jnef_400ice_pt():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)

        def upon_43():
            if (SLOT_48 == 4101):
                sendToLabel(0)
    sprite('null', 5)	# 1-5
    Unknown1096(500)
    Unknown1099(50)
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f343030696365736d6f6b6500000000000000000000000000000000ffffffff')
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f343030696365707463303000000000000000000000000000000000ffffffff')
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f343030696365707463000000000000000000000000000000000000ffffffff')
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('null', 5)	# 6-10
    SFX_0('017_freeze_1')
    SFX_0('017_freeze_1')
    label(0)
    sprite('null', 10)	# 11-20
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f343030696365736d6f6b6500000000000000000000000000000000ffffffff')
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f343030696365707463303000000000000000000000000000000000ffffffff')
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f343030696365707463000000000000000000000000000000000000ffffffff')
    gotoLabel(0)
    label(0)
    sprite('null', 0)	# 21-20

@State
def UltimateSlashShotObj():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(1650)
        Unknown11091(14)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(2)
        PushbackX(80000)
        Unknown9130(40)
        Unknown9142(30)
        Unknown9132(45)
        Unknown9144(35)
        AirUntechableTime(28)
        Unknown9168(33)
        AirPushbackX(60000)
        AirPushbackY(1000)
        Unknown9202(20)
        Hitstop(0)
        Unknown9016(1)
        Unknown11057(600)
        Unknown11043(0)
        Unknown9021(1)
        physicsXImpulse(50000)
        Unknown1028(800)
        Unknown2055(120)
        Unknown53(1)
        Unknown4061(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3070(3)
        Unknown3071(4)
        Unknown3076(1000)
        Unknown3077(500)
        Unknown3033()
        Unknown2037(0)

        def upon_78():
            Unknown21015('6963655f73686f74000000000000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6169725f6963655f73686f740000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6963655f73686f745f6578000000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6169725f6963655f73686f745f65780000000000000000000000000000000000f513000000000000')
            Unknown21015('6963655f73686f745f6578320000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6169725f6963655f73686f745f65783200000000000000000000000000000000f513000000000000')
            Unknown2038(1)
            if (SLOT_2 >= 5):
                Unknown2001()
    label(0)
    sprite('vrjnef430_00', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    Unknown3001(255)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_00', 1)	# 2-2	 **attackbox here**
    sprite('vrjnef430_01', 1)	# 3-3	 **attackbox here**
    RefreshMultihit()
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_01', 1)	# 4-4	 **attackbox here**
    sprite('vrjnef430_02', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_02', 1)	# 6-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def OverDriveSlashShotObj():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Unknown11091(15)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(2)
        PushbackX(80000)
        Unknown9130(40)
        Unknown9142(30)
        Unknown9132(45)
        Unknown9144(35)
        AirUntechableTime(28)
        AirPushbackX(60000)
        AirPushbackY(1000)
        Unknown9202(20)
        Hitstop(0)
        Unknown9016(1)
        Unknown11057(600)
        Unknown11043(0)
        Unknown11110(65)
        physicsXImpulse(50000)
        Unknown1028(800)
        Unknown2055(120)
        Unknown53(1)
        Unknown4061(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3070(3)
        Unknown3071(4)
        Unknown3076(1000)
        Unknown3077(500)
        Unknown3033()

        def upon_45():
            if Unknown2065(25):
                clearUponHandler(45)
                Unknown23029(3, 5102, 0)
        Unknown2037(0)

        def upon_78():
            Unknown21015('6963655f73686f74000000000000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6169725f6963655f73686f740000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6963655f73686f745f6578000000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6169725f6963655f73686f745f65780000000000000000000000000000000000f513000000000000')
            Unknown21015('6963655f73686f745f6578320000000000000000000000000000000000000000f513000000000000')
            Unknown21015('6169725f6963655f73686f745f65783200000000000000000000000000000000f513000000000000')
            Unknown23029(3, 5101, 0)
            Unknown11069('OverDriveSlashShotObj')
            Unknown2038(1)
            if (SLOT_2 >= 5):
                Unknown2001()
            GroundedHitstunAnimation(0)
            Unknown9130(110)
            Unknown9142(100)
            Unknown9250(20)
            Unknown9262(100)
            Unknown9021(1)
            Unknown9019(1)
    label(0)
    sprite('vrjnef430_00', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    Unknown3001(255)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_00', 1)	# 2-2	 **attackbox here**
    sprite('vrjnef430_01', 1)	# 3-3	 **attackbox here**
    RefreshMultihit()
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_01', 1)	# 4-4	 **attackbox here**
    sprite('vrjnef430_02', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_02', 1)	# 6-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def IceBow():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4009(2)
        Unknown4007(3)
        Unknown4011(3)
        Unknown3029(1)
        Unknown3070(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1200)

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown4007(0)
                teleportRelativeX(50000)
                Unknown1007(-100000)
                Unknown1073(80000)
    sprite('vrjnef431_00', 6)	# 1-6
    Unknown1072(-18000)
    Unknown3001(0)
    Unknown3004(45)
    Unknown1096(1200)
    sprite('vrjnef431_00', 26)	# 7-32
    Unknown3004(0)
    sprite('vrjnef431_01', 2)	# 33-34
    Unknown3001(255)
    sprite('vrjnef431_02', 2)	# 35-36
    sprite('vrjnef431_03', 10)	# 37-46
    SFX_3('jnse_20')
    SFX_3('jnse_20')
    Unknown3001(212)
    Unknown3004(-10)
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceCirclePtc', 2)
    GFX_0('IceCirclePtc', 3)
    GFX_0('IceCirclePtc', 4)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcM', 6)
    GFX_0('IceBreakPtcM', 7)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcM', 6)
    GFX_0('IceBreakPtcM', 7)
    sprite('vrjnef431_03', 3)	# 47-49
    SFX_3('jnse_20')
    SFX_3('jnse_20')
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 6)
    GFX_0('IceBreakPtcS', 7)
    sprite('vrjnef431_03', 20)	# 50-69

@State
def IceCircleA():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5002):
                teleportRelativeX(225000)
                Unknown1007(-200000)
                Unknown1073(80000)
    Unknown4061(1)
    sprite('vrjnef431b_00', 9)	# 1-9
    Unknown1096(1000)
    Unknown1099(200)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrjnef431b_00', 12)	# 10-21
    Unknown3004(-20)
    Unknown1099(10)

@State
def IceCircleB():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5002):
                teleportRelativeX(250000)
                Unknown1007(-225000)
                Unknown1073(80000)
    Unknown4061(1)
    sprite('vrjnef431b_00', 9)	# 1-9
    Unknown1096(700)
    Unknown1099(100)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrjnef431b_00', 20)	# 10-29
    Unknown3004(-12)
    Unknown1099(20)

@State
def IceCircleC():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5002):
                teleportRelativeX(275000)
                Unknown1007(-250000)
                Unknown1073(80000)
    Unknown4061(1)
    sprite('vrjnef431b_00', 9)	# 1-9
    Unknown1096(250)
    Unknown1099(100)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrjnef431b_00', 30)	# 10-39
    Unknown3004(-8)
    Unknown1099(15)

@State
def IceArrow():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        AttackP2(97)
        Unknown11091(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(0, 30, 30)
        Unknown9250(20)
        Unknown9262(45)
        Unknown11055(1)
        Unknown9019(1)
        Unknown11062(1)
        Unknown11069('IceArrow')
        Unknown2073(1)
        Unknown4011(3)
        Unknown2054(1)
        Unknown53(1)
        Unknown4061(1)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3033()
        Unknown3001(0)
        Unknown3004(40)
        Unknown1096(0)
        Unknown1099(100)
        Unknown1015(-50)
        Unknown1021(-50)
        Unknown2037(1)

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown2037(12)
                AirPushbackX(55000)
                SLOT_51 = 1
                Unknown1072(-28000)
                Unknown1109(120000, 28000)
                Unknown1017()
                Unknown1022()
                physicsXImpulse(0)
                physicsYImpulse(0)
            if (SLOT_48 == 5002):
                Unknown2037(12)
                YImpluseBeforeWallbounce(3000)
                Unknown1007(200000)
                Unknown1072(50000)
                Unknown1109(120000, -50000)
                Unknown1017()
                Unknown1022()
                physicsXImpulse(0)
                physicsYImpulse(0)

        def upon_78():
            clearUponHandler(78)
            Unknown53(0)
            sendToLabel(3)

        def upon_82():
            clearUponHandler(82)
            SLOT_56 = 1

        def upon_3():
            if (not SLOT_2):
                clearUponHandler(3)
                clearUponHandler(78)
                sendToLabel(101)

        def upon_80():
            clearUponHandler(80)
            Unknown23029(3, 5005, 0)
    sprite('vrjnef431atk_00', 10)	# 1-10	 **attackbox here**
    StartMultihit()
    Unknown23024(1)
    sprite('vrjnef431atk_00', 24)	# 11-34	 **attackbox here**
    StartMultihit()
    Unknown1099(0)
    sprite('vrjnef431atk_00', 3)	# 35-37	 **attackbox here**
    Unknown4009(0)
    Unknown1018()
    Unknown1023()
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 38-40	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 41-43	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 44-46	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 47-49	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 50-52	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 53-55	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 56-58	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 59-61	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 62-64	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    loopRest()
    gotoLabel(55)
    label(3)
    sprite('vrjnef431atk_00', 1)	# 65-65	 **attackbox here**
    if SLOT_51:
        Unknown36(22)
        Unknown1086(26)
        teleportRelativeX(-200000)
        Unknown1007(-100000)
        Unknown35()
        if SLOT_56:
            Unknown36(23)
            Unknown1086(26)
            teleportRelativeX(-200000)
            Unknown1007(-100000)
            Unknown35()
    else:
        Unknown36(22)
        Unknown1086(26)
        teleportRelativeX(-200000)
        Unknown1007(-300000)
        Unknown35()
        if SLOT_56:
            Unknown36(23)
            Unknown1086(26)
            teleportRelativeX(-200000)
            Unknown1007(-300000)
            Unknown35()
    Unknown23029(3, 5003, 0)

    def upon_12():
        Unknown1019(106)
        YAccel(106)
        SFX_0('017_freeze_1')
    Damage(300)
    Unknown11050('0400000065665f676972645f64616d616765000000000000000000000000000000000000')
    Unknown9251()
    Unknown30048(1)
    Unknown1017()
    Unknown1022()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown11023(1)
    sprite('vrjnef431atk_00', 19)	# 66-84	 **attackbox here**
    if SLOT_51:
        Unknown1086(22)
        Unknown1007(100000)
        teleportRelativeX(-200000)
    else:
        Unknown1086(22)
        Unknown1007(300000)
        teleportRelativeX(-200000)
    sprite('vrjnef431atk_01', 3)	# 85-87	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(1)
    YAccel(1)
    RefreshMultihit()
    ScreenShake(10000, 0)
    Unknown1099(5)
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 4)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 4)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    sprite('vrjnef431atk_02', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    label(100)
    sprite('vrjnef431atk_03', 2)	# 91-92	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(0, 5000)
    sprite('vrjnef431atk_04', 2)	# 93-94	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    sprite('vrjnef431atk_05', 2)	# 95-96	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(5000, 0)
    sprite('vrjnef431atk_04', 2)	# 97-98	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('vrjnef431atk_02', 3)	# 99-101	 **attackbox here**
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(1000)
    Unknown23029(3, 5004, 0)
    RefreshMultihit()
    Damage(4100)
    Unknown11001(0, 0, 5)
    Unknown11069('')
    Unknown11091(28)
    if SLOT_51:
        YImpluseBeforeWallbounce(10)
        AirHitstunAnimation(12)
        WallbounceReboundTime(-1)
    else:
        pass
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    GFX_1('ef_hitlz', -1)
    sprite('vrjnef431atk_02', 30)	# 102-131	 **attackbox here**
    ScreenShake(30000, 0)
    Unknown1018()
    Unknown1023()
    Unknown1019(150)
    YAccel(150)
    GFX_1('ef_hitlz', -1)
    SFX_0('017_freeze_1')
    sprite('vrjnef431atk_02', 30)	# 132-161	 **attackbox here**
    loopRest()
    label(55)
    sprite('vrjnef431atk_02', 3)	# 162-164	 **attackbox here**

@State
def IceArrow_Assist():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(200)
        Unknown11091(100)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(55000)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(0, 30, 30)
        Unknown9250(20)
        Unknown9262(45)
        Unknown11055(1)
        Unknown9019(1)
        Unknown11062(1)
        Unknown11043(0)
        Unknown12051(2)
        Unknown11069('IceArrow_Assist')
        Unknown4011(3)
        Unknown2054(1)
        Unknown53(1)
        Unknown4061(1)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3033()
        Unknown3001(0)
        Unknown3004(40)
        Unknown1096(0)
        Unknown1099(100)
        Unknown1015(-50)
        Unknown1021(-50)
        Unknown2037(12)
        Unknown1072(-28000)
        Unknown1109(120000, 28000)
        Unknown1017()
        Unknown1022()
        physicsXImpulse(0)
        physicsYImpulse(0)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(3)

        def upon_3():
            if (not SLOT_2):
                clearUponHandler(3)
                clearUponHandler(78)
                sendToLabel(101)
    sprite('vrjnef431atk_00', 10)	# 1-10	 **attackbox here**
    StartMultihit()
    Unknown23024(1)
    sprite('vrjnef431atk_00', 24)	# 11-34	 **attackbox here**
    StartMultihit()
    Unknown1099(0)
    sprite('vrjnef431atk_00', 3)	# 35-37	 **attackbox here**
    Unknown4009(0)
    Unknown1018()
    Unknown1023()
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 38-40	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 41-43	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 44-46	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 47-49	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 50-52	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 53-55	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 56-58	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 59-61	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 62-64	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    loopRest()
    gotoLabel(55)
    label(3)
    sprite('vrjnef431atk_00', 1)	# 65-65	 **attackbox here**
    Unknown36(27)
    Unknown1086(26)
    teleportRelativeX(-200000)
    Unknown1007(-100000)
    Unknown35()
    Unknown23029(3, 5003, 0)

    def upon_12():
        Unknown1019(106)
        YAccel(106)
        SFX_0('017_freeze_1')
    Damage(100)
    Unknown11050('0400000065665f676972645f64616d616765000000000000000000000000000000000000')
    Unknown9251()
    Unknown30048(1)
    Unknown1017()
    Unknown1022()
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('vrjnef431atk_00', 19)	# 66-84	 **attackbox here**
    Unknown1086(22)
    Unknown1007(100000)
    teleportRelativeX(-200000)
    sprite('vrjnef431atk_01', 3)	# 85-87	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(1)
    YAccel(1)
    RefreshMultihit()
    ScreenShake(10000, 0)
    Unknown1099(5)
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 4)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 4)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    sprite('vrjnef431atk_02', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    label(100)
    sprite('vrjnef431atk_03', 2)	# 91-92	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(0, 5000)
    sprite('vrjnef431atk_04', 2)	# 93-94	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    sprite('vrjnef431atk_05', 2)	# 95-96	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(5000, 0)
    sprite('vrjnef431atk_04', 2)	# 97-98	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('vrjnef431atk_02', 3)	# 99-101	 **attackbox here**
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(1000)
    RefreshMultihit()
    Damage(400)
    Unknown11001(0, 0, 5)
    YImpluseBeforeWallbounce(10)
    AirHitstunAnimation(12)
    WallbounceReboundTime(-1)
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    GFX_1('ef_hitlz', -1)
    sprite('vrjnef431atk_02', 30)	# 102-131	 **attackbox here**
    ScreenShake(30000, 0)
    Unknown1018()
    Unknown1023()
    Unknown1019(150)
    YAccel(150)
    GFX_1('ef_hitlz', -1)
    SFX_0('017_freeze_1')
    sprite('vrjnef431atk_02', 30)	# 132-161	 **attackbox here**
    loopRest()
    label(55)
    sprite('vrjnef431atk_02', 3)	# 162-164	 **attackbox here**

@State
def IceArrow_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        AttackP2(98)
        Unknown11091(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(0, 30, 30)
        Unknown9250(20)
        Unknown9262(45)
        Unknown11055(1)
        Unknown9019(1)
        Unknown11062(1)
        Unknown11069('IceArrow_OD')
        Unknown2073(1)
        Unknown4011(3)
        Unknown2054(1)
        Unknown53(1)
        Unknown4061(1)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3033()
        Unknown3001(0)
        Unknown3004(40)
        Unknown1096(0)
        Unknown1099(100)
        Unknown1015(-50)
        Unknown1021(-50)
        Unknown2037(1)

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown2037(20)
                AirPushbackX(55000)
                SLOT_51 = 1
                Unknown1072(-28000)
                Unknown1109(120000, 28000)
                Unknown1017()
                Unknown1022()
                physicsXImpulse(0)
                physicsYImpulse(0)
            if (SLOT_48 == 5002):
                Unknown2037(20)
                YImpluseBeforeWallbounce(3000)
                Unknown1007(200000)
                Unknown1072(50000)
                Unknown1109(120000, -50000)
                Unknown1017()
                Unknown1022()
                physicsXImpulse(0)
                physicsYImpulse(0)

        def upon_78():
            clearUponHandler(78)
            GFX_0('EffAtk8D', 0)
            Unknown53(0)
            sendToLabel(3)

        def upon_82():
            clearUponHandler(82)
            SLOT_56 = 1

        def upon_3():
            if (not SLOT_2):
                clearUponHandler(3)
                clearUponHandler(78)
                sendToLabel(101)

        def upon_80():
            clearUponHandler(80)
            Unknown23029(3, 5005, 0)
    sprite('vrjnef431atk_00', 10)	# 1-10	 **attackbox here**
    StartMultihit()
    Unknown23024(1)
    sprite('vrjnef431atk_00', 24)	# 11-34	 **attackbox here**
    StartMultihit()
    Unknown1099(0)
    sprite('vrjnef431atk_00', 3)	# 35-37	 **attackbox here**
    Unknown4009(0)
    Unknown1018()
    Unknown1023()
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 38-40	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 41-43	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 44-46	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 47-49	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 50-52	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 53-55	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 56-58	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 59-61	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 62-64	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    loopRest()
    gotoLabel(55)
    label(3)
    sprite('vrjnef431atk_00', 1)	# 65-65	 **attackbox here**
    if SLOT_51:
        Unknown36(22)
        Unknown1086(26)
        teleportRelativeX(-200000)
        Unknown1007(-100000)
        Unknown35()
        if SLOT_56:
            Unknown36(23)
            Unknown1086(26)
            teleportRelativeX(-200000)
            Unknown1007(-100000)
            Unknown35()
    else:
        Unknown36(22)
        Unknown1086(26)
        teleportRelativeX(-200000)
        Unknown1007(-300000)
        Unknown35()
        if SLOT_56:
            Unknown36(23)
            Unknown1086(26)
            teleportRelativeX(-200000)
            Unknown1007(-300000)
            Unknown35()
    Unknown23029(3, 5003, 0)

    def upon_12():
        Unknown1019(106)
        YAccel(106)
        SFX_0('017_freeze_1')
    Damage(300)
    Unknown11050('0400000065665f676972645f64616d616765000000000000000000000000000000000000')
    Unknown9251()
    Unknown30048(1)
    Unknown1017()
    Unknown1022()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown11023(1)
    sprite('vrjnef431atk_00', 19)	# 66-84	 **attackbox here**
    if SLOT_51:
        Unknown1086(22)
        Unknown1007(100000)
        teleportRelativeX(-200000)
    else:
        Unknown1086(22)
        Unknown1007(300000)
        teleportRelativeX(-200000)
    sprite('vrjnef431atk_01', 3)	# 85-87	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(1)
    YAccel(1)
    RefreshMultihit()
    ScreenShake(10000, 0)
    Unknown1099(5)
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 4)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 4)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    sprite('vrjnef431atk_02', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    label(100)
    sprite('vrjnef431atk_03', 2)	# 91-92	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(0, 5000)
    sprite('vrjnef431atk_04', 2)	# 93-94	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    sprite('vrjnef431atk_05', 2)	# 95-96	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(5000, 0)
    sprite('vrjnef431atk_04', 2)	# 97-98	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('vrjnef431atk_02', 3)	# 99-101	 **attackbox here**
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(1000)
    Unknown23029(3, 5004, 0)
    RefreshMultihit()
    Damage(3600)
    Unknown11091(27)
    Unknown11001(0, 0, 5)
    Unknown11069('')
    if SLOT_51:
        YImpluseBeforeWallbounce(10)
        AirHitstunAnimation(12)
        WallbounceReboundTime(-1)
    else:
        pass
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    GFX_1('ef_hitlz', -1)
    sprite('vrjnef431atk_02', 30)	# 102-131	 **attackbox here**
    ScreenShake(30000, 0)
    Unknown1018()
    Unknown1023()
    Unknown1019(150)
    YAccel(150)
    GFX_1('ef_hitlz', -1)
    SFX_0('017_freeze_1')
    sprite('vrjnef431atk_02', 30)	# 132-161	 **attackbox here**
    loopRest()
    label(55)
    sprite('vrjnef431atk_02', 3)	# 162-164	 **attackbox here**

@State
def IceArrow_OD_Assist():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(200)
        Unknown11091(100)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(55000)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(0, 30, 30)
        AirUntechableTime(45)
        Unknown11055(1)
        Unknown9019(1)
        Unknown11062(1)
        Unknown11043(0)
        Unknown12051(2)
        Unknown11069('IceArrow_OD_Assist')
        Unknown4011(3)
        Unknown2054(1)
        Unknown53(1)
        Unknown4061(1)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3033()
        Unknown3001(0)
        Unknown3004(40)
        Unknown1096(0)
        Unknown1099(100)
        Unknown1015(-50)
        Unknown1021(-50)
        Unknown2037(18)
        Unknown1072(-28000)
        Unknown1109(120000, 28000)
        Unknown1017()
        Unknown1022()
        physicsXImpulse(0)
        physicsYImpulse(0)

        def upon_78():
            clearUponHandler(78)
            GFX_0('EffAtk8D', 0)
            sendToLabel(3)

        def upon_3():
            if (not SLOT_2):
                clearUponHandler(3)
                clearUponHandler(78)
                sendToLabel(101)
    sprite('vrjnef431atk_00', 10)	# 1-10	 **attackbox here**
    StartMultihit()
    Unknown23024(1)
    sprite('vrjnef431atk_00', 24)	# 11-34	 **attackbox here**
    StartMultihit()
    Unknown1099(0)
    sprite('vrjnef431atk_00', 3)	# 35-37	 **attackbox here**
    Unknown4009(0)
    Unknown1018()
    Unknown1023()
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 38-40	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 41-43	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 44-46	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 47-49	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 50-52	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 53-55	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 56-58	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 59-61	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)	# 62-64	 **attackbox here**
    GFX_1('jnef431_iceshot', -1)
    loopRest()
    gotoLabel(55)
    label(3)
    sprite('vrjnef431atk_00', 1)	# 65-65	 **attackbox here**
    Unknown36(27)
    Unknown1086(26)
    teleportRelativeX(-200000)
    Unknown1007(-100000)
    Unknown35()
    Unknown23029(3, 5003, 0)

    def upon_12():
        Unknown1019(106)
        YAccel(106)
        SFX_0('017_freeze_1')
    Damage(100)
    Unknown11050('0400000065665f676972645f64616d616765000000000000000000000000000000000000')
    Unknown9251()
    Unknown30048(1)
    Unknown1017()
    Unknown1022()
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('vrjnef431atk_00', 19)	# 66-84	 **attackbox here**
    Unknown1086(22)
    Unknown1007(100000)
    teleportRelativeX(-200000)
    sprite('vrjnef431atk_01', 3)	# 85-87	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1019(1)
    YAccel(1)
    RefreshMultihit()
    ScreenShake(10000, 0)
    Unknown1099(5)
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    Unknown4045('6a6e65663433315f69636562720000000000000000000000000000000000000001000000')
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 4)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 4)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    sprite('vrjnef431atk_02', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    label(100)
    sprite('vrjnef431atk_03', 2)	# 91-92	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(0, 5000)
    sprite('vrjnef431atk_04', 2)	# 93-94	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    sprite('vrjnef431atk_05', 2)	# 95-96	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(5000, 0)
    sprite('vrjnef431atk_04', 2)	# 97-98	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('vrjnef431atk_02', 3)	# 99-101	 **attackbox here**
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(1000)
    RefreshMultihit()
    Damage(300)
    Unknown11001(0, 0, 5)
    YImpluseBeforeWallbounce(10)
    AirHitstunAnimation(12)
    WallbounceReboundTime(-1)
    Unknown1019(106)
    YAccel(106)
    SFX_0('017_freeze_1')
    GFX_1('ef_hitlz', -1)
    sprite('vrjnef431atk_02', 30)	# 102-131	 **attackbox here**
    ScreenShake(30000, 0)
    Unknown1018()
    Unknown1023()
    Unknown1019(150)
    YAccel(150)
    GFX_1('ef_hitlz', -1)
    SFX_0('017_freeze_1')
    sprite('vrjnef431atk_02', 30)	# 132-161	 **attackbox here**
    loopRest()
    label(55)
    sprite('vrjnef431atk_02', 3)	# 162-164	 **attackbox here**

@State
def Yukikazedmy():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4009(3)
        Unknown4011(3)
        AttackLevel_(4)
        Damage(1500)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        PushbackX(8000)
        Unknown9142(9999)
        Unknown9130(30)
        Unknown9132(30)
        Unknown9016(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown11056(3)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown9019(1)
        Unknown11108('03000000')
        Unknown1086(22)
    sprite('vrdmy_yukikaze', 1)	# 1-1	 **attackbox here**
    SFX_0('018_ice_break_1')
    GFX_0('JNFreezeDamageBreakParts', -1)
    GFX_0('JNFreezeDamageBreakParts', -1)
    StartMultihit()
    sprite('vrdmy_yukikaze', 3)	# 2-4	 **attackbox here**

@State
def YukikazedmyOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4009(3)
        Unknown4011(3)
        AttackLevel_(4)
        Damage(1500)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        PushbackX(8000)
        Unknown9142(9999)
        Unknown9130(30)
        Unknown9132(30)
        Unknown9016(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown11068(1)
        Unknown11056(3)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown9019(1)
        Unknown11108('03000000')
        Unknown1086(22)
    sprite('vrdmy_yukikaze', 1)	# 1-1	 **attackbox here**
    SFX_0('018_ice_break_1')
    GFX_0('JNFreezeDamageBreakParts', -1)
    GFX_0('JNFreezeDamageBreakParts', -1)
    StartMultihit()
    sprite('vrdmy_yukikaze', 3)	# 2-4	 **attackbox here**

@State
def DDD_Snow():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 4)	# 1-4
    Unknown4045('6a6e65665f4444445f536e6f7700000000000000000000000000000000000000ffffffff')

@State
def JNFreezeDamageBreakParts():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4061(1)
        Unknown1007(256000)
    sprite('null', 200)	# 1-200
    Unknown4047(175, 111, 111)
    Unknown23067('jnef_freezebreak')

@State
def jnef600_envStart():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vrjnef600env', 20)	# 1-20
    Unknown3033()
    Unknown1096(1000)
    Unknown3001(0)
    Unknown3004(6)
    sprite('vrjnef600env', 2)	# 21-22
    Unknown3001(0)

@State
def jnef600_envLoop():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vrjnef600env', 20)	# 1-20
    Unknown3033()
    Unknown3001(120)
    Unknown3004(2)
    sprite('vrjnef600env', 20)	# 21-40
    Unknown3004(-2)

@State
def jnef600_envEnd():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vrjnef600env', 10)	# 1-10
    Unknown3033()
    Unknown1096(1000)
    Unknown1099(-5)
    Unknown3001(120)
    Unknown3004(-20)

@State
def jnef600iceSword():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown2019(500)
        Unknown1096(1000)
        Unknown3001(255)
    sprite('vrjnef600_00', 3)	# 1-3
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('jnef600_envStart', -1)
    SFX_0('017_freeze_0')
    sprite('vrjnef600_01', 3)	# 4-6
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    SFX_0('017_freeze_0')
    sprite('vrjnef600_02', 3)	# 7-9
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    SFX_0('017_freeze_0')
    sprite('vrjnef600_03', 3)	# 10-12
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    SFX_0('017_freeze_0')
    sprite('vrjnef600_04', 2)	# 13-14	 **attackbox here**
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    SFX_0('017_freeze_0')
    sprite('vrjnef600_04ex01', 2)	# 15-16	 **attackbox here**
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    SFX_0('017_freeze_0')
    sprite('vrjnef600_04ex02', 4)	# 17-20	 **attackbox here**
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    SFX_0('017_freeze_1')
    label(0)
    sprite('vrjnef600_04ex03', 20)	# 21-40
    GFX_0('jnef600_envLoop', -1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('vrjnef600_04ex03', 20)	# 41-60
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrjnef600_05', 3)	# 61-63
    GFX_0('jnef600_envEnd', -1)
    sprite('vrjnef600_06', 3)	# 64-66
    Unknown3001(200)
    Unknown3004(-5)
    sprite('vrjnef600_07', 3)	# 67-69
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceCirclePtc', 2)
    GFX_0('IceBreakPtcM', 0)
    GFX_0('IceBreakPtcM', 1)
    GFX_0('IceBreakPtcM', 2)
    GFX_0('IceBreakPtcM', 6)
    GFX_0('IceBreakPtcM', 7)
    GFX_0('IceBreakPtcM', 8)
    GFX_0('IceBreakPtcM', 9)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 6)
    GFX_0('IceBreakPtcS', 7)
    GFX_0('IceBreakPtcS', 8)
    GFX_0('IceBreakPtcS', 9)
    SFX_0('018_ice_break_1')
    sprite('vrjnef600_08', 3)	# 70-72

@State
def jnef601env():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2019(-500)
        Unknown4007(2)
        Unknown4009(2)
    sprite('vrjnef601env', 4)	# 1-4
    Unknown3033()
    Unknown1096(700)
    Unknown1099(25)
    Unknown3001(0)
    Unknown3004(20)
    sprite('vrjnef601env', 20)	# 5-24
    Unknown1099(5)
    Unknown3004(-5)

@State
def jnef601makeSword():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown2019(-100)
        Unknown3033()
        Unknown3001(0)
    sprite('vrjnef601_00', 20)	# 1-20	 **attackbox here**
    Unknown3004(10)
    GFX_0('jnef601ptc', -1)
    GFX_0('jnef601env', -1)
    GFX_0('jnef601Sword', -1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    sprite('vrjnef601_01', 1)	# 21-21	 **attackbox here**
    GFX_0('IceBreakPtc601', 0)
    GFX_0('IceBreakPtc601', 1)
    GFX_0('IceBreakPtc601', 2)
    GFX_0('IceBreakPtcS', 0)
    GFX_0('IceBreakPtcS', 1)
    GFX_0('IceBreakPtcS', 2)
    sprite('vrjnef601_02', 10)	# 22-31	 **attackbox here**
    Unknown3001(200)
    Unknown3004(-20)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    label(0)
    Unknown4061(0)
    sprite('vrjnef601_03', 1)	# 32-32
    Unknown3001(255)
    Unknown3032()
    loopRest()
    gotoLabel(0)
    label(1)
    Unknown4061(0)
    sprite('vrjnef601_03', 6)	# 33-38

@State
def jnef601Sword():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown4010(3)
        Unknown3032()
        Unknown3001(0)
    sprite('vrjnef601_03', 20)	# 1-20
    Unknown3004(15)
    sprite('vrjnef601_03', 4)	# 21-24
    Unknown3001(255)

@State
def jnef611icewing():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown3029(1)
        Unknown3071(10)
        Unknown3074('00000000000000000000000000000000')
        Unknown3075('00000000800000008000000080000000')
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown3033()
    sprite('jnef611_00', 4)	# 1-4
    Unknown2019(-100)
    teleportRelativeX(-60000)
    Unknown1007(60000)
    Unknown1072(-50000)
    Unknown1074(500)
    physicsXImpulse(-1000)
    physicsYImpulse(500)
    Unknown1096(500)
    Unknown1059(5)
    Unknown3001(0)
    Unknown3004(40)
    sprite('jnef611_00', 6)	# 5-10
    Unknown1096(700)
    sprite('jnef611_01', 6)	# 11-16
    Unknown1056(800)
    Unknown1064(800)
    sprite('jnef611_02', 6)	# 17-22
    GFX_0('IceMakePtc', 4)
    GFX_1('jnef_iceptc', 5)
    GFX_1('jnef_iceptc', 6)
    GFX_0('jnef611_hane', 0)
    GFX_0('jnef611_hane', 1)
    GFX_0('jnef611_hane', 2)
    Unknown3001(255)
    sprite('jnef611_03', 6)	# 23-28
    GFX_0('IceMakePtc', 0)
    GFX_1('jnef_iceptc', 1)
    GFX_1('jnef_iceptc', 2)
    GFX_0('jnef611_hane', 4)
    GFX_0('jnef611_hane', 5)
    sprite('jnef611_04', 6)	# 29-34
    GFX_0('IceMakePtc', 0)
    GFX_1('jnef_iceptc', 1)
    GFX_1('jnef_iceptc', 2)
    GFX_0('jnef611_hane', 0)
    sprite('jnef611_05', 6)	# 35-40
    GFX_0('IceMakePtc', 0)
    GFX_1('jnef_iceptc', 1)
    GFX_1('jnef_iceptc', 2)
    GFX_0('jnef611_hane', 2)
    sprite('jnef611_06', 4)	# 41-44
    GFX_0('IceMakePtc', 0)
    GFX_1('jnef_iceptc', 1)
    GFX_1('jnef_iceptc', 2)
    Unknown1059(1)
    physicsXImpulse(200)
    physicsYImpulse(-400)
    sprite('jnef611_07', 4)	# 45-48
    Unknown3001(128)
    Unknown3004(-5)
    sprite('jnef611_08', 6)	# 49-54
    GFX_1('jnef_iceptc', 1)
    GFX_1('jnef_iceptc', 2)
    sprite('jnef611_09', 24)	# 55-78
    sprite('null', 32)	# 79-110

@State
def cmp():
    sprite('vrtest00', 10)	# 1-10
    Unknown3060('000000007672746573743838000000000000000000000000000000000000000000000000')
    Unknown3064(0, 100)
    Unknown3065(0, 200)
    Unknown1096(2000)
    label(0)
    sprite('vrtest00ex01', 10)	# 11-20
    Unknown3060('000000007672746573743839000000000000000000000000000000000000000000000000')
    sprite('vrtest00', 10)	# 21-30
    sprite('vrtest01', 10)	# 31-40
    sprite('vrtest02', 10)	# 41-50
    sprite('vrtest03', 10)	# 51-60
    loopRest()
    gotoLabel(0)

@State
def ef_jnah_A():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f6a6e61685f412e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(160)
        Unknown1056(800)
        Unknown1064(1100)
        Unknown1099(1)
    sprite('null', 255)	# 1-255
    SFX_3('jnse_01')
    SFX_0('017_freeze_0')
    sprite('null', 30)	# 256-285
    SFX_0('018_ice_break_0')
    SFX_0('018_ice_break_1')
    Unknown3004(-10)

@State
def ef_jnah_B():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f6a6e61685f422e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeY(-30000)
        Unknown3001(128)
        Unknown1096(1000)
        Unknown1099(1)
    sprite('null', 10)	# 1-10
    SFX_3('jnse_01')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 11-20
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 21-30
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 31-40
    SFX_0('019_quake_0')
    sprite('null', 10)	# 41-50
    SFX_0('019_quake_0')
    sprite('null', 10)	# 51-60
    SFX_0('017_freeze_0')
    sprite('null', 10)	# 61-70
    SFX_0('019_quake_0')
    sprite('null', 10)	# 71-80
    SFX_0('017_freeze_0')
    sprite('null', 10)	# 81-90
    sprite('null', 10)	# 91-100
    SFX_0('019_quake_0')
    sprite('null', 10)	# 101-110
    SFX_0('017_freeze_0')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 111-120
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 121-130
    SFX_0('017_freeze_0')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 131-140
    SFX_0('018_ice_break_0')
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 141-150
    SFX_0('018_ice_break_0')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 151-160
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 161-170
    SFX_0('018_ice_break_0')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 171-180
    SFX_0('017_freeze_0')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 181-190
    SFX_0('018_ice_break_0')
    SFX_0('018_ice_break_0')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    sprite('null', 10)	# 191-200
    SFX_0('018_ice_break_0')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 201-210
    SFX_0('018_ice_break_0')
    SFX_0('017_freeze_0')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)	# 211-220
    SFX_0('017_freeze_1')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 5)	# 221-225
    sprite('null', 60)	# 226-285
    Unknown3004(-10)

@State
def LookAtMe():

    def upon_IMMEDIATE():
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def AstralStartPtc():

    def upon_IMMEDIATE():
        GFX_2('jnef_ast_start_snow')
        Unknown4011(3)
        Unknown2005()
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767

@State
def AstralFinishPtc():

    def upon_IMMEDIATE():
        GFX_2('jnef_ast_finish')
        Unknown2005()
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767
    GFX_1('jnef_ast_snowfloor', -1)

@State
def JNEF_ast_attack():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 300)	# 1-300
    GFX_2('jnef_ast_attack')

@State
def EventEffSpKensei():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4061(7)
        Unknown3032()

        def upon_44():
            Unknown14()
        Unknown1096(1100)
        teleportRelativeX(720000)
        Unknown1007(210000)
        Unknown2005()
    sprite('vrhzef407_00', 3)	# 1-3
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    Unknown3001(55)
    Unknown3004(25)
    sprite('vrhzef407_01', 3)	# 4-6
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    sprite('vrhzef407_02', 2)	# 7-8
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_03', 4)	# 9-12
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_04', 18)	# 13-30
    Unknown4007(0)
    GFX_0('HZEF_Aura', 0)
    GFX_0('HZEF_Aura', 1)
    GFX_0('HZEF_Aura', 2)
    GFX_0('HZEF_Aura', 3)
    GFX_0('HZEF_Aura', 4)
    GFX_0('HZEF_Aura', 5)
    GFX_0('HZEF_Aura', 6)
    GFX_0('HZEF_Aura', 7)
    GFX_0('HZEF_Aura', 8)
    GFX_0('HZEF_Aura', 9)
    GFX_0('HZEF_Aura', 10)
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    GFX_0('HZEF_AuraDelete', 6)
    GFX_0('HZEF_AuraDelete', 7)
    GFX_0('HZEF_AuraDelete', 8)
    GFX_0('HZEF_AuraDelete', 9)
    GFX_0('HZEF_AuraDelete', 10)
    sprite('vrhzef407_05', 4)	# 31-34
    GFX_0('HZEF_AuraDelete', 0)
    GFX_0('HZEF_AuraDelete', 1)
    GFX_0('HZEF_AuraDelete', 2)
    GFX_0('HZEF_AuraDelete', 3)
    GFX_0('HZEF_AuraDelete', 4)
    GFX_0('HZEF_AuraDelete', 5)
    sprite('vrhzef407_06', 4)	# 35-38

@State
def HZEF_Aura():

    def upon_IMMEDIATE():
        Unknown4009(2)
        GFX_2('hzef_envaura')
        Unknown3033()
        Unknown1096(800)
    sprite('null', 20)	# 1-20
    Unknown3004(-15)

@State
def HZEF_AuraDelete():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4054(2)
        Unknown23067('hzef_deleteaura')
        Unknown1096(600)
    sprite('null', 60)	# 1-60

@State
def RushAssaultFinishAtkObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4009(3)
        Unknown4011(3)
        AttackLevel_(4)
        AttackP1(100)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackX(20000)
        PushbackX(-24000)
        Hitstop(0)
        Unknown9016(1)
        Unknown11056(3)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11108('03000000')
        Unknown11023(1)
        Unknown30048(1)
        Unknown11091(0)
        callSubroutine('CheckOverDriveSpecial')

        def upon_ON_HIT_OR_BLOCK():
            Unknown1086(27)
            SFX_0('018_ice_break_1')
            GFX_0('JNFreezeDamageBreakParts', -1)
            GFX_0('JNFreezeDamageBreakParts', -1)

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown2003(0)
            else:
                Unknown2003(1)
            if SLOT_6:
                Unknown48('19000000020000003400000017000000020000001e000000')
                if SLOT_52:
                    Unknown30048(0)
                else:
                    Unknown30048(1)
    sprite('vrdmy_yukikaze', 3)	# 1-3	 **attackbox here**

@State
def UltimateShotOverDrive():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        AirPushbackY(20000)
        Hitstop(6)
        Unknown9016(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9130(130)
        Unknown9142(120)
        Unknown9250(100)
        Unknown9262(120)
        AirUntechableTime(120)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11056(2)
        Unknown11064(1)
        Unknown23182(3)
        Unknown9019(1)
        Unknown2053(1)
        Unknown3033()
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown2005()
        Unknown11069('OverDriveSlashShotObj')

        def upon_43():
            if (SLOT_48 == 5104):
                Unknown1096(850)
                teleportRelativeX(100000)
            if (SLOT_48 == 5105):
                Unknown1096(1000)
                teleportRelativeX(-180000)
                Unknown2005()
                AirPushbackX(-5500)
                AirPushbackY(-2000)
                PushbackX(-30400)
            if (SLOT_48 == 5106):
                Unknown1096(1100)
                teleportRelativeX(60000)
                AirPushbackY(10000)
                Unknown11069('OverDriveSlashShotFinish')
            if (SLOT_48 == 5107):
                sendToLabel(0)

        def upon_12():
            Unknown23029(3, 5108, 0)

        def upon_44():
            SLOT_51 = 1
    sprite('vrjnef233atk_00', 3)	# 1-3
    Unknown30070('4f7665724472697665536c61736853686f744f626a0000000000000000000000')
    Unknown1099(-5)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    SFX_0('017_freeze_0')
    sprite('vrjnef233atk_01', 3)	# 4-6
    Unknown1099(-5)
    GFX_0('Icicle_Env', -1)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    GFX_0('IceMakePtc', 3)
    GFX_0('IceMakePtc', 4)
    SFX_0('017_freeze_0')
    sprite('vrjnef233atk_02ex01', 3)	# 7-9
    Unknown1099(0)
    SFX_0('017_freeze_0')
    loopRest()
    if SLOT_51:
        _gotolabel(0)
    sprite('vrjnef233atk_02', 3)	# 10-12	 **attackbox here**
    ScreenShake(30000, 30000)
    Unknown1099(5)
    SFX_0('017_freeze_1')
    sprite('vrjnef233atk_02', 90)	# 13-102	 **attackbox here**
    StartMultihit()
    Unknown1099(0)
    loopRest()
    label(0)
    clearUponHandler(44)
    sprite('vrjnef233atk_03', 3)	# 103-105
    Unknown1099(0)
    Unknown3001(200)
    Unknown3004(-15)
    sprite('vrjnef233atk_04', 3)	# 106-108
    GFX_0('IceCirclePtc', 0)
    GFX_0('IceCirclePtc', 1)
    GFX_0('IceCirclePtc', 2)
    GFX_0('IceBreakPtcL', 0)
    GFX_0('IceBreakPtcL', 1)
    GFX_0('IceBreakPtcL', 2)
    GFX_0('IceBreakPtcM', 3)
    GFX_0('IceBreakPtcM', 4)
    GFX_0('IceBreakPtcM', 5)
    GFX_0('IceBreakPtcM', 6)
    GFX_0('IceBreakPtcM', 7)
    GFX_0('IceBreakPtcM', 8)
    GFX_0('IceBreakPtcS', 3)
    GFX_0('IceBreakPtcS', 4)
    GFX_0('IceBreakPtcS', 5)
    GFX_0('IceBreakPtcS', 6)
    GFX_0('IceBreakPtcS', 7)
    GFX_0('IceBreakPtcS', 8)
    GFX_0('IceBreakPtcS', 9)
    SFX_0('018_ice_break_1')
    sprite('vrjnef233atk_05', 10)	# 109-118

@State
def OverDriveSlashShotFinish():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4009(3)
        Unknown4011(3)
        AttackLevel_(4)
        Damage(1000)
        Unknown11091(1)
        AttackP2(100)
        PushbackX(8000)
        Unknown9142(9999)
        Unknown9130(30)
        Unknown9310(15)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown11056(3)
        Unknown9016(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown1086(22)
    sprite('vrdmy_yukikaze', 1)	# 1-1	 **attackbox here**
    SFX_0('018_ice_break_1')
    GFX_0('JNFreezeDamageBreakParts', -1)
    GFX_0('JNFreezeDamageBreakParts', -1)
    StartMultihit()
    sprite('vrdmy_yukikaze', 3)	# 2-4	 **attackbox here**

@State
def ptPhantom():

    def upon_IMMEDIATE():
        Unknown4061(6)
        Unknown3001(0)
        Unknown3032()
        Unknown1007(70000)
        sendToLabelUpon(32, 1)
    sprite('pt999_00', 22)	# 1-22
    SFX_0('302_spsys_rapid')
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
def EventTBHitEff():
    sprite('null', 5)	# 1-5
    Unknown4052()
    Unknown4045('65665f6869746c7a0000000000000000000000000000000000000000000000006c000000')
    SFX_0('101_hit_slash_3')

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
def EventIceMakePtc():
    sprite('null', 1)	# 1-1
    Unknown1000(0)
    teleportRelativeY(80000)
    Unknown1010(-50000, 50000)
    Unknown1011(-50000, 50000)
    Unknown4061(1)
    Unknown3038(1)
    GFX_1('jnef_icesmoke00', -1)
    Unknown4047(175, 96, 48)
    Unknown4045('6a6e65665f696365707463303000000000000000000000000000000000000000ffffffff')
    Unknown4047(175, 96, 48)
    Unknown4049(2000)
    Unknown4045('6a6e65665f696365707463000000000000000000000000000000000000000000ffffffff')
    Unknown4049(2000)

@State
def Event_UltimateSlashShotObj():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2011()
        physicsXImpulse(50000)
        Unknown1028(800)
        Unknown2055(120)
        Unknown53(1)
        Unknown4061(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3070(3)
        Unknown3071(4)
        Unknown3076(1000)
        Unknown3077(500)
        Unknown3033()
        Unknown2003(1)
    label(0)
    sprite('vrjnef430_00', 1)	# 1-1	 **attackbox here**
    Unknown3001(255)
    GFX_0('IceMakePtc', 0)
    GFX_0('IceMakePtc', 1)
    GFX_0('IceMakePtc', 2)
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_00', 1)	# 2-2	 **attackbox here**
    sprite('vrjnef430_01', 1)	# 3-3	 **attackbox here**
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_01', 1)	# 4-4	 **attackbox here**
    sprite('vrjnef430_02', 1)	# 5-5	 **attackbox here**
    Unknown4018('01000000464c4f52455f46524f5354000000000000000000000000000000000000000000ffffffff8403000084030000')
    SFX_3('jnse_01')
    sprite('vrjnef430_02', 1)	# 6-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ptPhantom_Renew():

    def upon_IMMEDIATE():
        Unknown4061(6)
        Unknown3001(0)
        Unknown3032()
        teleportRelativeX(-50000)
        Unknown1007(70000)
        Unknown2019(-500)
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
        Unknown4061(6)
        Unknown3001(0)
        Unknown3032()
        Unknown1007(70000)
        sendToLabelUpon(32, 1)
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
def Act3Event_IceBoard():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4010(3)
        Unknown2019(100)
        Unknown3033()
        Unknown1007(160000)

        def upon_45():
            if (not SLOT_51):
                Unknown48('190000000200000053000000030000000200000053000000')

        def upon_32():
            SLOT_51 = 1
            Unknown4007(3)
            Unknown1000(0)
        Unknown2055(50)
    sprite('vrjnef408_00', 2)	# 1-2
    GFX_0('IceMakePtc', 0)
    Unknown1064(0)
    Unknown1067(100)
    SFX_0('017_freeze_0')
    sprite('vrjnef408_00', 2)	# 3-4
    SFX_0('017_freeze_1')
    sprite('vrjnef408_00', 2)	# 5-6
    SFX_0('017_freeze_0')
    sprite('vrjnef408_00', 2)	# 7-8
    SFX_0('017_freeze_1')
    sprite('vrjnef408_00', 2)	# 9-10
    SFX_0('017_freeze_0')
    label(0)
    sprite('vrjnef408_00', 4)	# 11-14
    Unknown4049(2000)
    Unknown4045('6a6e65665f69636573686f74000000000000000000000000000000000000000000000000')
    Unknown1067(0)
    loopRest()
    gotoLabel(0)

@State
def Act3Event_IceBoard_koware():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown4007(0)
        Unknown2019(100)
        Unknown3033()
        Unknown1007(160000)
    sprite('vrjnef408_00', 3)	# 1-3
    GFX_0('IceMakePtc', 0)
    Unknown4049(1500)
    Unknown4047(111, 111, 111)
    Unknown4045('6a6e65665f69636562726200000000000000000000000000000000000000000000000000')
    physicsXImpulse(35000)
    Unknown1015(-15000)
    Unknown3001(164)
    Unknown3004(-20)
    Unknown1096(1000)
    Unknown1099(-15)
    SFX_0('018_ice_break_0')
    sprite('vrjnef408_00', 3)	# 4-6
    SFX_0('018_ice_break_1')
    sprite('vrjnef408_00', 3)	# 7-9
    SFX_0('018_ice_break_0')
    sprite('vrjnef408_00', 3)	# 10-12
    sprite('vrjnef408_00', 3)	# 13-15
    SFX_0('018_ice_break_0')
    sprite('vrjnef408_00', 5)	# 16-20

@State
def Act3Event_Offset():

    def upon_IMMEDIATE():
        Unknown1001(0)
        teleportRelativeY(200000)
    sprite('null', 4)	# 1-4
    GFX_1('ef_offset', 0)
    SFX_0('108_attack_offset')
    ScreenShake(30000, 30000)

@State
def TagCutIn():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(2000)
        Unknown6001(1)
        Unknown1096(700)
        Unknown3001(0)
        Unknown23023()
        Unknown2005()
    sprite('vr_01rg_base11', 5)	# 1-5
    Unknown1015(-40000)
    Unknown3005(20)
    sprite('vr_01rg_base11', 40)	# 6-45
    physicsXImpulse(0)
    Unknown3001(255)
    Unknown1015(-300)
    sprite('vr_01rg_base11', 40)	# 46-85
    Unknown3005(-51)

@State
def DDCutIn():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(500)
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-440000)
        Unknown1001(300000)
        Unknown3001(0)
        Unknown2054(1)
        Unknown23023()
        Unknown2005()
    sprite('vr_01rg_base13', 5)	# 1-5
    Unknown1015(-40000)
    Unknown3005(20)
    GFX_0('DDCutInBase', 100)
    sprite('vr_01rg_base13', 20)	# 6-25
    physicsXImpulse(0)
    Unknown3001(160)
    Unknown1015(-2000)
    sprite('vr_01rg_base13', 20)	# 26-45
    Unknown1015(500)
    sprite('vr_01rg_base13', 40)	# 46-85
    Unknown3005(-51)

@State
def DDCutInBase():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(2000)
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-440000)
        Unknown1001(520000)
        Unknown3001(0)
        Unknown2054(1)
        Unknown23023()
        Unknown2005()
        Unknown4010(2)
    sprite('vr_01rg_base14', 5)	# 1-5
    Unknown3005(5)
    sprite('vr_01rg_base14', 40)	# 6-45
    physicsXImpulse(0)
    sprite('vr_01rg_base14', 40)	# 46-85
    Unknown3005(-51)