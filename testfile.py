
def init():
    Move_Register('AN_CmnActChangePartnerDDExe', 24)
    Move_Register('AN_CmnActChangePartnerDDODExe', 24)

@State
def AN_CmnActChangePartnerDDExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(4)
        Damage(400)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(28000)
        AirUntechableTime(100)
        Unknown9310(20)
        Unknown11056(2)
        Unknown11064(1)
        Unknown11062(1)
        Unknown1084(1)
        Unknown30019('0000000001000000')

        def upon_STATE_END():
            Unknown2017(1)
            Unknown23087(0)
            Unknown12046(0)
    sprite('nt440_00', 2)	# 1-2
    setInvincible(1)
    Unknown1084(1)
    sprite('nt312_01ex01', 33)	# 3-35
    sprite('nt440_01', 2)	# 36-37
    sprite('nt440_04', 3)	# 38-40
    physicsXImpulse(4000)
    sprite('nt440_05', 3)	# 41-43
    Unknown1019(200)
    sprite('nt440_06', 3)	# 44-46
    sprite('nt440_07', 3)	# 47-49	 **attackbox here**
    Unknown23087(150000)
    Unknown1019(200)
    Unknown8001(3, 100)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('nt440_08', 1)	# 50-50
    Unknown7006('bnt281_0', 100, 846491234, 828322104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    setInvincible(0)
    Unknown12046(10)
    sprite('nt440_08', 1)	# 51-51
    Unknown12046(20)
    sprite('nt440_09', 1)	# 52-52
    Unknown12046(30)
    sprite('nt440_09', 1)	# 53-53
    Unknown12046(40)
    sprite('nt440_09', 1)	# 54-54
    Unknown12046(50)
    sprite('nt440_10', 1)	# 55-55
    Unknown12046(60)
    sprite('nt440_10', 1)	# 56-56
    Unknown12046(70)
    sprite('nt440_10', 1)	# 57-57
    Unknown12046(80)
    sprite('nt440_11', 1)	# 58-58
    Unknown12046(90)
    sprite('nt440_11', 1)	# 59-59
    Unknown12046(100)
    sprite('nt440_11', 1)	# 60-60
    sprite('nt440_12', 3)	# 61-63
    GFX_1('ntef_611_end', 0)
    GFX_1('ntef_611_end', 1)
    SFX_3('ntse_09')
    sprite('nt440_13', 3)	# 64-66
    sprite('nt440_14', 3)	# 67-69
    YAccel(150)
    SFX_3('ntse_04')
    sprite('nt440_15', 3)	# 70-72
    YAccel(150)
    sprite('nt440_16', 3)	# 73-75
    YAccel(150)
    sendToLabelUpon(2, 1)
    sprite('nt440_16', 30)	# 76-105
    Unknown1019(150)
    YAccel(200)
    label(1)
    sprite('nt440_17', 2)	# 106-107	 **attackbox here**
    clearUponHandler(2)
    Unknown1084(1)
    Damage(800)
    Hitstop(8)
    Unknown11001(-5, -5, -5)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-200000)
    Unknown11072(1, 350000, 0)
    Unknown9016(1)
    RefreshMultihit()
    sprite('nt440_18', 3)	# 108-110	 **attackbox here**
    GFX_0('ntef_440Axe', -1)
    Unknown8000(100, 1, 1)
    Unknown12046(0)
    Damage(800)
    Hitstop(9)
    Unknown11001(-1, -1, -1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(28000)
    AirPushbackY(35000)
    Unknown11072(0, 0, 0)
    Unknown11064(0)
    Unknown9310(10)
    Unknown23086(1)
    RefreshMultihit()
    sprite('nt440_19', 3)	# 111-113	 **attackbox here**
    Unknown23027()
    Unknown12046(0)
    sprite('nt440_20', 3)	# 114-116	 **attackbox here**
    sprite('nt440_19', 3)	# 117-119	 **attackbox here**
    sprite('nt440_20', 3)	# 120-122	 **attackbox here**
    sprite('nt440_19', 3)	# 123-125	 **attackbox here**
    sprite('nt440_20', 3)	# 126-128	 **attackbox here**
    sprite('nt440_19', 3)	# 129-131	 **attackbox here**
    Unknown26('BurstDD_Camera')
    sprite('nt440_20', 3)	# 132-134	 **attackbox here**
    sprite('nt440_21', 4)	# 135-138
    sprite('nt440_22', 4)	# 139-142
    sprite('nt440_23', 4)	# 143-146
    sprite('nt440_24', 4)	# 147-150
    sprite('nt403_09ex01', 4)	# 151-154
    sprite('nt403_10ex01', 4)	# 155-158
    sprite('nt403_11ex01', 4)	# 159-162
    sprite('nt601_06ex01', 5)	# 163-167
    sprite('nt601_07ex01', 5)	# 168-172
    sprite('nt601_08ex01', 8)	# 173-180
    SFX_0('019_cloth_a')
    sprite('nt601_09ex01', 5)	# 181-185

@State
def AN_CmnActChangePartnerDDODExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(4)
        Damage(400)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(28000)
        AirUntechableTime(100)
        Unknown9310(20)
        Unknown11056(2)
        Unknown11064(1)
        Unknown11062(1)
        Unknown1084(1)
        Unknown30019('0000000001000000')

        def upon_STATE_END():
            Unknown2017(1)
            Unknown23087(0)
            Unknown12046(0)
    sprite('nt440_00', 2)	# 1-2
    setInvincible(1)
    Unknown1084(1)
    sprite('nt312_01ex01', 33)	# 3-35
    sprite('nt440_01', 2)	# 36-37
    sprite('nt440_04', 3)	# 38-40
    physicsXImpulse(4000)
    sprite('nt440_05', 3)	# 41-43
    Unknown1019(200)
    sprite('nt440_06', 3)	# 44-46
    sprite('nt440_07', 3)	# 47-49	 **attackbox here**
    Unknown23087(150000)
    Unknown1019(200)
    Unknown8001(3, 100)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('nt440_08', 1)	# 50-50
    Unknown7006('bnt281_0', 100, 846491234, 828322104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    setInvincible(0)
    Unknown12046(10)
    sprite('nt440_08', 1)	# 51-51
    Unknown12046(20)
    sprite('nt440_09', 1)	# 52-52
    Unknown12046(30)
    sprite('nt440_09', 1)	# 53-53
    Unknown12046(40)
    sprite('nt440_09', 1)	# 54-54
    Unknown12046(50)
    sprite('nt440_10', 1)	# 55-55
    Unknown12046(60)
    sprite('nt440_10', 1)	# 56-56
    Unknown12046(70)
    sprite('nt440_10', 1)	# 57-57
    Unknown12046(80)
    sprite('nt440_11', 1)	# 58-58
    Unknown12046(90)
    sprite('nt440_11', 1)	# 59-59
    Unknown12046(100)
    sprite('nt440_11', 1)	# 60-60
    sprite('nt440_12', 3)	# 61-63
    GFX_1('ntef_611_end', 0)
    GFX_1('ntef_611_end', 1)
    SFX_3('ntse_09')
    sprite('nt440_13', 3)	# 64-66
    sprite('nt440_14', 3)	# 67-69
    YAccel(150)
    SFX_3('ntse_04')
    sprite('nt440_15', 3)	# 70-72
    YAccel(150)
    sprite('nt440_16', 3)	# 73-75
    YAccel(150)
    sendToLabelUpon(2, 1)
    sprite('nt440_16', 30)	# 76-105
    Unknown1019(150)
    YAccel(200)
    label(1)
    sprite('nt440_17', 2)	# 106-107	 **attackbox here**
    clearUponHandler(2)
    Unknown1084(1)
    Damage(350)
    Hitstop(13)
    Unknown11001(-10, -10, -10)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-200000)
    Unknown11072(1, 300000, 0)
    Unknown9016(1)
    RefreshMultihit()
    sprite('nt440_18', 3)	# 108-110	 **attackbox here**
    GFX_0('ntef_440Axe', -1)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Damage(350)
    Hitstop(1)
    Unknown11001(4, 4, 4)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(70000)
    AirPushbackY(30000)
    Unknown11072(0, 0, 0)
    Unknown11055(1)
    Unknown11057(700)
    Unknown23086(1)
    RefreshMultihit()
    GFX_0('ntef_440LastEx', -1)
    sprite('nt440_19', 3)	# 111-113	 **attackbox here**
    sprite('nt440_20', 3)	# 114-116	 **attackbox here**
    RefreshMultihit()
    sprite('nt440_19', 3)	# 117-119	 **attackbox here**
    sprite('nt440_20', 3)	# 120-122	 **attackbox here**
    RefreshMultihit()
    sprite('nt440_19', 3)	# 123-125	 **attackbox here**
    sprite('nt440_20', 3)	# 126-128	 **attackbox here**
    RefreshMultihit()
    sprite('nt440_19', 3)	# 129-131	 **attackbox here**
    sprite('nt440_20', 3)	# 132-134	 **attackbox here**
    Unknown12046(0)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(28000)
    AirPushbackY(35000)
    Hitstop(0)
    Unknown11001(20, 20, 20)
    Unknown9310(10)
    Unknown11057(1000)
    Unknown11064(0)
    RefreshMultihit()
    sprite('nt440_19', 3)	# 135-137	 **attackbox here**
    sprite('nt440_20', 3)	# 138-140	 **attackbox here**
    sprite('nt440_19', 3)	# 141-143	 **attackbox here**
    sprite('nt440_20', 3)	# 144-146	 **attackbox here**
    sprite('nt440_19', 3)	# 147-149	 **attackbox here**
    sprite('nt440_20', 3)	# 150-152	 **attackbox here**
    sprite('nt440_19', 3)	# 153-155	 **attackbox here**
    sprite('nt440_20', 3)	# 156-158	 **attackbox here**
    sprite('nt440_19', 3)	# 159-161	 **attackbox here**
    Unknown23027()
    Unknown12046(0)
    sprite('nt440_20', 3)	# 162-164	 **attackbox here**
    sprite('nt440_19', 3)	# 165-167	 **attackbox here**
    sprite('nt440_20', 3)	# 168-170	 **attackbox here**
    sprite('nt440_19', 3)	# 171-173	 **attackbox here**
    sprite('nt440_20', 3)	# 174-176	 **attackbox here**
    sprite('nt440_19', 3)	# 177-179	 **attackbox here**
    Unknown26('BurstDD_Camera')
    sprite('nt440_20', 3)	# 180-182	 **attackbox here**
    sprite('nt440_21', 4)	# 183-186
    sprite('nt440_22', 4)	# 187-190
    sprite('nt440_23', 4)	# 191-194
    sprite('nt440_24', 4)	# 195-198
    sprite('nt403_09ex01', 4)	# 199-202
    sprite('nt403_10ex01', 4)	# 203-206
    sprite('nt403_11ex01', 4)	# 207-210
    sprite('nt601_06ex01', 5)	# 211-215
    sprite('nt601_07ex01', 5)	# 216-220
    sprite('nt601_08ex01', 8)	# 221-228
    SFX_0('019_cloth_a')
    sprite('nt601_09ex01', 5)	# 229-233
