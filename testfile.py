
@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(10000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        Unknown1112('')
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    Unknown7009(1)
    sprite('es201_04', 5)	# 8-12	 **attackbox here**
    GFX_0('esef_201', -1)
    sprite('es201_05', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 16-18
    sprite('es201_07', 3)	# 19-21
    sprite('es201_08', 3)	# 22-24
    sprite('es201_09', 3)	# 25-27
    sprite('es201_10', 3)	# 28-30

@State
def NmlAtk5B():
    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        PushbackX(39900)
        AirPushbackX(15000)
        AirPushbackY(-100000)
        Unknown9310(10)
        Unknown9202(1)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B2nd')
        Unknown1112('')
        Unknown2004(1, 0)
    sprite('es203_00', 3)	# 1-3
    sprite('es203_01', 3)	# 4-6
    Unknown23029(11, 110, 0)
    GFX_0('eseff_DTame', 0)
    Unknown36(1)
    Unknown1072(42500)
    Unknown35()
    SFX_3('esse_02')
    sprite('es203_02', 2)	# 7-8
    sprite('es203_03', 2)	# 9-10
    SFX_3('esse_02')
    sprite('es203_02', 2)	# 11-12
    sprite('es203_03', 2)	# 13-14
    SFX_3('esse_02')
    sprite('es203_04', 2)	# 15-16
    Unknown21015('65736566665f4454616d650000000000000000000000000000000000000000006400000000000000')
    SFX_0('006_swing_blade_2')
    Unknown7009(3)
    sprite('es203_05', 3)	# 17-19
    sprite('es203_06', 2)	# 20-21
    sprite('es203_07', 2)	# 22-23
    sprite('es203_08', 5)	# 24-28	 **attackbox here**
    Unknown2015(200)
    GFX_0('esef_203', -1)
    SFX_3('esse_00')
    GFX_0('es203_effAtk', -1)
    Unknown38(11, 1)
    sprite('es203_09', 9)	# 29-37
    Recovery()
    Unknown2063()
    sprite('es203_10', 5)	# 38-42
    sprite('es203_11', 5)	# 43-47
    sprite('es203_12', 5)	# 48-52
    Unknown2015(-1)
    sprite('es203_13', 5)	# 53-57
    sprite('es203_14', 4)	# 58-61

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(80)
        AirPushbackY(28000)
        AirUntechableTime(22)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)
    sprite('es232_00', 2)	# 1-2
    sprite('es232_01', 2)	# 3-4
    sprite('es232_02', 3)	# 5-7
    SFX_0('006_swing_blade_1')
    sprite('es232_03', 2)	# 8-9
    Unknown7007('6265733130375f300000000000000000640000006265733130375f310000000000000000640000006265733130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('es232_04', 3)	# 10-12	 **attackbox here**
    GFX_0('esef_232', -1)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('es232_05', 4)	# 13-16
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('es232_06', 4)	# 17-20
    sprite('es232_07', 6)	# 21-26
    sprite('es232_08', 6)	# 27-32
    sprite('es232_09', 6)	# 33-38
    sprite('es232_10', 6)	# 39-44

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('es400_00', 2)	# 1-2
    sprite('es400_01', 1)	# 3-3
    sprite('es400_01', 2)	# 4-5
    tag_voice(1, 'bes200_0', 'bes200_1', 'bes200_2', '')
    sprite('es400_04', 3)	# 6-8
    sprite('es400_05', 3)	# 9-11
    sprite('es400_06', 3)	# 12-14
    Unknown14070('ShotA_2nd')
    Unknown14070('ShotB_2nd')
    sprite('es400_07', 3)	# 15-17
    GFX_0('esef_400_zanzou', -1)
    GFX_0('es400_A', -1)
    Unknown38(4, 1)
    sprite('es400_08', 3)	# 18-20
    Unknown14072('ShotA_2nd')
    Unknown14072('ShotB_2nd')
    sprite('es400_09', 3)	# 21-23
    sprite('es400_10', 3)	# 24-26
    sprite('es400_08', 3)	# 27-29
    sprite('es400_09', 3)	# 30-32
    sprite('es400_10', 3)	# 33-35
    Unknown14074('ShotA_2nd')
    Unknown14074('ShotB_2nd')
    sprite('es400_08', 3)	# 36-38
    sprite('es400_11', 3)	# 39-41
    Recovery()
    sprite('es400_12', 3)	# 42-44

@State
def ShotB_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        if Unknown23145('ShotA'):
            SLOT_51 = 1

            def upon_3():
                if Unknown46(4):
                    if SLOT_2:
                        Unknown59('04000000670000000600000067000000')
                        if (SLOT_0 < 50000):
                            clearUponHandler(3)
                            Unknown21015('65733430305f425f326e640000000000000000000000000000000000000000007700000000000000')
                            Unknown21015('65733430305f425f326e644200000000000000000000000000000000000000007700000000000000')
    sprite('es400_13', 2)	# 1-2
    sprite('es400_14', 4)	# 3-6
    sprite('es400_15', 4)	# 7-10
    sprite('es400_16', 2)	# 11-12
    sprite('es400_17', 3)	# 13-15
    GFX_0('esef_400_zanzou2', -1)
    if Unknown23145('ShotA'):
        GFX_0('es400_B_2nd', -1)
    else:
        GFX_0('es400_B_2ndB', -1)
    Unknown38(6, 1)
    Unknown2037(1)
    sprite('es400_18', 4)	# 16-19
    tag_voice(0, 'bes201_0', 'bes201_1', 'bes201_2', '')
    sprite('es400_19', 4)	# 20-23
    sprite('es400_20', 4)	# 24-27
    sprite('es400_18', 3)	# 28-30
    sprite('es400_21', 3)	# 31-33
    sprite('es400_22', 3)	# 34-36
    Recovery()
    sprite('es400_23', 3)	# 37-39
    sprite('es400_24', 3)	# 40-42


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(2500)
        AttackP1(80)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown9154(60)
        Unknown11056(0)
        Unknown11069('UltimateAssault')
        Unknown11064(1)
        Unknown30048(1)
        Unknown23055('')

        def upon_12():
            clearUponHandler(12)
            Unknown13024(0)
            Unknown21005(1)
            Unknown13021(1)
            sendToLabel(0)
            Unknown21015('65733230335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733231335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733233335f65666641746b00000000000000000000000000000000000000006700000000000000')
            Unknown21015('65733235335f65666641746b00000000000000000000000000000000000000006700000000000000')

        def upon_STATE_END():
            Unknown26('esef_431Camera')
            Unknown3001(255)
            Unknown3004(0)

        def upon_3():
            if (not SLOT_158):
                clearUponHandler(3)
                Unknown26('esef_431Camera')
    sprite('es431_00', 2)	# 1-2
    setInvincible(1)
    sprite('es431_01', 1)	# 3-3
    sprite('es431_01', 3)	# 4-6
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('es431_02', 4)	# 7-10
    sprite('es431_03', 16)	# 11-26
    GFX_0('esef_431Eff', -1)
    tag_voice(1, 'bes252_0', 'bes252_1', '', '')
    sprite('es431_04', 6)	# 27-32
    sprite('es431_05', 6)	# 33-38
    sprite('es431_06', 6)	# 39-44
    sprite('es431_07', 5)	# 45-49
    sprite('es431_08', 3)	# 50-52
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006800000000000000')
    Unknown3029(1)
    physicsXImpulse(15000)
    physicsYImpulse(18000)
    SFX_3('esse_04')
    SFX_0('000_airdash_0')
    sprite('es431_09', 3)	# 53-55	 **attackbox here**
    Unknown1019(700)
    physicsYImpulse(0)
    sprite('es431_10', 3)	# 56-58	 **attackbox here**
    sprite('es431_09', 3)	# 59-61	 **attackbox here**
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    sprite('es431_11', 4)	# 62-65
    setInvincible(0)
    Unknown1019(70)
    teleportRelativeY(0)
    sprite('es110_03ex00', 4)	# 66-69
    Unknown1019(70)
    sprite('es110_04ex00', 4)	# 70-73
    Unknown1019(70)
    sprite('es110_05ex00', 4)	# 74-77
    Unknown1019(70)
    sprite('es110_06ex00', 4)	# 78-81
    Unknown1019(70)
    sprite('es110_07ex00', 4)	# 82-85
    Unknown1084(1)
    Unknown3029(0)
    ExitState()
    label(0)
    sprite('es431_12', 5)	# 86-90
    Unknown21015('657365665f3433314566660000000000000000000000000000000000000000006900000000000000')
    Unknown1019(50)
    sprite('es431_13', 5)	# 91-95
    Unknown1019(50)
    sprite('es431_14', 5)	# 96-100
    Unknown2017(0)
    Unknown1019(50)
    sprite('es431_15', 5)	# 101-105
    Unknown1019(50)
    Unknown3004(-8)
    sprite('es431_16', 5)	# 106-110
    sprite('es431_17', 5)	# 111-115
    GFX_0('esef_431Eff2', -1)
    SFX_3('esse_09')
    SFX_3('esse_09')
    tag_voice(0, 'bes253_0', 'bes253_1', '', '')
    sprite('es431_18', 3)	# 116-118	 **attackbox here**
    Unknown3029(0)
    Unknown1019(0)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(0)
    sprite('es431_18', 9)	# 119-127	 **attackbox here**
    GFX_0('esef_431EffSlash', -1)
    GFX_0('esef_431Camera', -1)
    GFX_0('esef_431EffEsRay', 100)
    Unknown2015(50)
    physicsXImpulse(96000)
    Unknown1028(-8000)
    Unknown3004(42)
    Damage(4300)
    Unknown11091(33)
    AttackP2(60)
    Hitstop(0)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    PushbackX(-30000)
    Unknown9130(50)
    Unknown9142(200)
    Unknown9132(50)
    Unknown9144(200)
    Unknown9016(1)
    Unknown11023(1)
    Unknown11069('')
    Unknown11064(0)
    Unknown11066(1)
    Unknown11084(1)
    Unknown13024(1)
    RefreshMultihit()
    sprite('es431_18', 3)	# 128-130	 **attackbox here**
    Unknown2017(1)
    Unknown2015(-1)
    GFX_0('esef_431EffScrew', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('es431_19', 2)	# 131-132	 **attackbox here**
    sprite('es431_20', 2)	# 133-134	 **attackbox here**
    sprite('es431_21', 2)	# 135-136	 **attackbox here**
    sprite('es431_22', 2)	# 137-138	 **attackbox here**
    sprite('es431_19', 2)	# 139-140	 **attackbox here**
    sprite('es431_20', 2)	# 141-142	 **attackbox here**
    sprite('es431_21', 2)	# 143-144	 **attackbox here**
    sprite('es431_22', 2)	# 145-146	 **attackbox here**
    sprite('es431_19', 3)	# 147-149	 **attackbox here**
    sprite('es431_20', 3)	# 150-152	 **attackbox here**
    sprite('es431_21', 3)	# 153-155	 **attackbox here**
    sprite('es431_22', 3)	# 156-158	 **attackbox here**
    sprite('es431_19', 4)	# 159-162	 **attackbox here**
    sprite('es431_20', 4)	# 163-166	 **attackbox here**
    sprite('es431_21', 4)	# 167-170	 **attackbox here**
    sprite('es431_22', 4)	# 171-174	 **attackbox here**
    sprite('es431_19', 4)	# 175-178	 **attackbox here**
    sprite('es431_20', 4)	# 179-182	 **attackbox here**
    sprite('es431_21', 4)	# 183-186	 **attackbox here**
    sprite('es431_22', 3)	# 187-189	 **attackbox here**
    sprite('es431_22', 1)	# 190-190	 **attackbox here**
    Unknown26('esef_431Camera')
    sprite('es431_23', 5)	# 191-195
    sprite('es431_24', 5)	# 196-200