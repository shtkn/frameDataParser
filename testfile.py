
@Subroutine
def SkillInit():
    HitOrBlockCancel('Guren_Hasei')
    HitOrBlockCancel('GurenB_Hasei')
    HitOrBlockCancel('Yanagi_Hasei')
    HitOrBlockCancel('Renka_Hasei')
    HitOrBlockCancel('Zantetu_Hasei')
    HitOrBlockCancel('RenkaEx_Hasei')
    if (not SLOT_59):
        Unknown30068(1)
        SFX_3('hase_25')
        GFX_0('ha_power_circle', -1)
        GFX_0('ha_power_light', -1)
        GFX_0('ha_power_bluelight', -1)
        if Unknown23148('RenkaEx'):
            GFX_0('ha_power_2', -1)
        elif Unknown23148('Yanagi'):
            GFX_0('ha_power_2', -1)
        else:
            GFX_0('ha_power_1', -1)
        Unknown2058(-5000)
        AttackP2(100)
    SLOT_59 = 0

    def upon_85():
        SLOT_59 = 1

@State
def GurenA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(80)
        AttackP2(75)
        AirUntechableTime(60)
        AirPushbackX(16000)
        AirPushbackY(16000)
        Unknown9154(26)
        PushbackX(12000)
        Unknown11056(0)
        Unknown9015(1)
        Unknown1084(0)
        Unknown3029(1)
        Unknown3069(0)
        callSubroutine('SkillInit')
    sprite('ha400_00', 2)	# 1-2
    sprite('ha400_01', 1)	# 3-3
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_01', 1)	# 4-4
    Unknown7007('6268613230305f300000000000000000640000006268613230305f310000000000000000640000006268613230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha400_02', 2)	# 5-6
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_03', 4)	# 7-10
    physicsXImpulse(55000)
    Unknown2015(150)
    sprite('ha400_04', 3)	# 11-13
    sprite('ha400_05', 3)	# 14-16	 **attackbox here**
    physicsXImpulse(0)
    setGravity(0)
    sprite('ha400_06', 4)	# 17-20
    SFX_0('208_brake_normal')
    Recovery()
    Unknown2063()
    Unknown2015(-1)
    sprite('ha400_07', 4)	# 21-24
    sprite('ha400_08', 4)	# 25-28
    Unknown3029(0)
    sprite('ha400_09', 4)	# 29-32
    sprite('ha400_10', 4)	# 33-36
    SFX_3('hase_22')