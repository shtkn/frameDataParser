@State
def PNA_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('504e415f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PNA_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PNA_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PNA_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 101):
            Unknown23185('504e415f506572736f6e6135413474680000000000000000000000000000000032000000')
        if (SLOT_48 == 102):
            Unknown23185('504e415f506572736f6e6135420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 103):
            Unknown23185('504e415f506572736f6e613542326e640000000000000000000000000000000032000000')
        if (SLOT_48 == 104):
            Unknown23185('504e415f506572736f6e6135423372640000000000000000000000000000000032000000')
        if (SLOT_48 == 105):
            Unknown23185('504e415f506572736f6e615468726f770000000000000000000000000000000032000000')
        if (SLOT_48 == 201):
            Unknown23185('504e415f506572736f6e6132420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 203):
            Unknown23185('504e415f506572736f6e613242486f6c6400000000000000000000000000000032000000')
        if (SLOT_48 == 204):
            Unknown23185('504e415f506572736f6e6132425f32000000000000000000000000000000000032000000')
        if (SLOT_48 == 301):
            Unknown23185('504e415f506572736f6e614a420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 304):
            Unknown23185('504e415f506572736f6e614a430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 305):
            Unknown23185('504e415f506572736f6e614a5f5465737400000000000000000000000000000032000000')
        if (SLOT_48 == 401):
            Unknown23185('547261700000000000000000000000000000000000000000000000000000000064000000')
        if (SLOT_48 == 402):
            Unknown23185('506172746e657241737369737441746b5f42000000000000000000000000000064000000')
        if (SLOT_48 == 403):
            Unknown23185('5041737361756c74325f5241000000000000000000000000000000000000000064000000')
        if (SLOT_48 == 405):
            Unknown23185('506172746e657241737369737441746b5f44000000000000000000000000000064000000')
        if (SLOT_48 == 502):
            Unknown23185('5042435f506572736f6e61556c74696d61746548414d414f4e00000000000000c8000000')
        if (SLOT_48 == 503):
            Unknown23185('5042435f506572736f6e61556c74696d6174654f4448414d414f4e0000000000c8000000')
        if (SLOT_48 == 504):
            Unknown23185('5042435f506572736f6e61556c74696d6174654d55444f4f4e00000000000000c8000000')
        if (SLOT_48 == 950):
            Unknown23185('504e415f506572736f6e614963686967656b6900000000000000000000000000c8000000')
        if (SLOT_48 == 6001):
            Unknown23185('506572736f6e614d6174636857696e32000000000000000000000000000000002c010000')
        if (SLOT_48 == 3017):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')

@Subroutine
def PersonaReset():
    Unknown4061(1)
    Unknown23022(0)
    Unknown2053(0)
    Unknown23015(11)
    Unknown2019(-1)
    Unknown1084(1)
    Unknown4009(0)
    Unknown4008(0)
    Unknown4007(0)
    EnableCollision(0)
    Unknown30041('')

@Subroutine
def PNA_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PNA_AttackInit():
    Unknown23028(1, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 100
    callSubroutine('PNA_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PNA_SPAttackInit():
    Unknown23028(2, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 110
    callSubroutine('PNA_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PNA_DDAttackInit():
    Unknown23028(3, 1)
    Unknown30037('')
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    SLOT_11 = 120
    callSubroutine('PNA_ReceptionSignal')
    Unknown23023()

@Subroutine
def PNA_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PNA_ForceWarp():
    SLOT_58 = 1
    Unknown3001(0)
    Unknown3004(85)
    loopRelated(17, 4)

    def upon_17():
        Unknown3001(255)
        Unknown3004(0)

@State
def PersonaDeleteAndIdling():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
    sprite('keep', 32767)	# 1-32767
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_3('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PNA_PersonaWait')

@State
def PersonaSummonEffect():
    sprite('null', 30)	# 1-30
    Unknown23015(13)
    Unknown4054(11)
    Unknown4045('706572736f6e615f73756d6d6f6e00000000000000000000000000000000000064000000')

@State
def PersonaSummonEffect_PLAYER():
    sprite('null', 30)	# 1-30
    Unknown1007(288000)
    teleportRelativeX(112000)
    GFX_1('persona_summon_ply', 100)

@State
def PersonaDeleteEffect():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        callSubroutine('PNA_ReceptionSignal')
    sprite('null', 30)	# 1-30
    Unknown2019(1)
    Unknown23053('190000000b000000')
    Unknown4061(1)
    Unknown3032()
    Unknown1059(-100)
    Unknown1067(150)
    Unknown3004(-20)
    Unknown23022(1)
    Unknown4054(11)
    Unknown4045('706572736f6e615f64656c65746500000000000000000000000000000000000064000000')
    Unknown2054(1)
    EnableCollision(0)
    Unknown1084(1)

@State
def PNA_Persona5A4th():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23184('030000006400000010b6fdff400d030000000000000000000000000000000000')
        Unknown23023()
        callSubroutine('PNA_CheckWarp')
        Unknown4007(3)
        Unknown23022(1)
        Unknown11034(1)
    sprite('su400_00', 3)	# 1-3
    sprite('su400_01', 3)	# 4-6
    sprite('su400_02', 3)	# 7-9
    sprite('su400_00', 3)	# 10-12
    sprite('su400_01', 3)	# 13-15
    sprite('su400_02', 3)	# 16-18
    sprite('su400_00', 3)	# 19-21
    sprite('su400_01', 3)	# 22-24
    sprite('su400_02', 3)	# 25-27
    sprite('su400_00', 3)	# 28-30
    sprite('su400_01', 3)	# 31-33
    sprite('su400_02', 4)	# 34-37
    sprite('keep', 32767)	# 38-32804
    enterState('PersonaDeleteAndIdling')

@State
def PNA_Persona5B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feffa08601006079feff20a10700a0860100a0860100')
        callSubroutine('PNA_AttackInit')
        AttackLevel_(3)
        AttackP1(90)
        Unknown9016(1)
        PushbackX(23000)
        AirPushbackY(20000)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown4007(3)
        Unknown23078(1)
        Unknown23059(1)
    sprite('su204_00', 3)	# 1-3
    sprite('su204_01', 3)	# 4-6
    SFX_3('cloth_l')
    sprite('su204_03', 3)	# 7-9	 **attackbox here**
    Unknown23029(3, 12, 0)
    RefreshMultihit()
    GFX_0('suef_5C', 100)
    SFX_3('slash_beam_fast')
    Unknown4007(0)
    sprite('su204_04', 4)	# 10-13	 **attackbox here**
    sprite('su204_05', 15)	# 14-28
    sprite('keep', 32767)	# 29-32795
    enterState('PersonaDeleteAndIdling')

@State
def PNA_Persona5B2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PNA_AttackInit')
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        AttackP2(80)
        Unknown11092(1)
        AirPushbackX(5000)
        AirPushbackY(10000)
        hitstun(20)
        AirUntechableTime(20)
        Hitstop(9)
        PushbackX(12000)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        physicsXImpulse(40000)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('su205_00', 1)	# 1-1
    sprite('su205_01', 1)	# 2-2
    sprite('su205_02', 1)	# 3-3
    sprite('su206_01', 1)	# 4-4
    sprite('su206_02', 2)	# 5-6
    sprite('su206_03', 2)	# 7-8
    GFX_0('suef_5DD', 100)
    sprite('su206_04', 2)	# 9-10	 **attackbox here**
    Unknown1084(1)
    RefreshMultihit()
    SFX_3('slash_beam_middle')
    sprite('su206_06', 2)	# 11-12
    physicsXImpulse(20000)
    Unknown1019(120)
    GFX_0('suef_5DDD', 100)
    sprite('su206_07', 6)	# 13-18	 **attackbox here**
    Unknown23029(2, 12, 0)
    RefreshMultihit()
    SFX_3('slash_beam_middle')
    sprite('su206_07', 7)	# 19-25	 **attackbox here**
    Unknown23029(2, 3020, 0)
    StartMultihit()
    Unknown1019(25)
    sprite('su206_08', 6)	# 26-31
    Unknown1019(25)
    sprite('keep', 32767)	# 32-32798
    enterState('PersonaDeleteAndIdling')

@State
def PNA_Persona5B3rd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000000000000050c3000000000000404b4c00a0860100a0860100')
        callSubroutine('PNA_AttackInit')
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(80)
        AirHitstunAnimation(10)
        AirUntechableTime(24)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown4007(3)
        Unknown23078(1)
        Unknown23059(1)
    sprite('su206_09', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('su206_10', 3)	# 4-6
    physicsXImpulse(20000)
    Unknown1028(-500)
    physicsYImpulse(20000)
    GFX_0('suef_5DDDD', 100)
    sprite('su206_11', 3)	# 7-9	 **attackbox here**
    SFX_3('slash_beam_middle')
    Unknown4007(0)
    sprite('su206_12', 3)	# 10-12
    setInvincible(0)
    sprite('su206_13', 3)	# 13-15
    Unknown1084(1)
    sprite('su206_14', 3)	# 16-18
    sprite('su206_12', 3)	# 19-21
    sprite('su206_13', 3)	# 22-24
    sprite('su206_14', 3)	# 25-27
    sprite('su206_12', 3)	# 28-30
    SFX_3('cloth_l')
    sprite('su206_13', 3)	# 31-33
    sprite('su206_14', 3)	# 34-36
    sprite('keep', 32767)	# 37-32803
    enterState('PersonaDeleteAndIdling')

@State
def PNA_PersonaThrow():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feffa086010000000000000000000000000000000000')
        callSubroutine('PNA_AttackInit')
        AttackLevel_(4)
        Damage(2000)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(50)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(30000)
        AirUntechableTime(120)
        AirHitstunAfterWallbounce(60)
        Unknown9202(20)
        Unknown9362(1)
        Unknown9364(30)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        Unknown11044(1)
        setInvincible(1)
        Unknown30048(1)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)
    sprite('su232_00', 4)	# 1-4
    sprite('su232_01', 4)	# 5-8
    sprite('su232_04', 4)	# 9-12
    physicsXImpulse(15000)
    SFX_3('slash_beam_slow')
    sprite('su232_05', 4)	# 13-16	 **attackbox here**
    GFX_0('suef_2C', 0)
    Unknown23029(2, 12, 0)
    RefreshMultihit()
    Unknown1019(70)
    sprite('su232_06', 4)	# 17-20	 **attackbox here**
    Unknown1019(60)
    sprite('su232_07', 4)	# 21-24	 **attackbox here**
    Unknown1019(60)
    sprite('su232_08', 4)	# 25-28	 **attackbox here**
    Unknown1019(60)
    sprite('su232_06', 4)	# 29-32	 **attackbox here**
    Unknown1019(60)
    sprite('su232_07', 4)	# 33-36	 **attackbox here**
    Unknown1019(0)
    sprite('su232_08', 4)	# 37-40	 **attackbox here**
    sprite('keep', 32767)	# 41-32807
    enterState('PersonaDeleteAndIdling')

@State
def PNA_Persona2B():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PNA_AttackInit')
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(80)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        AirUntechableTime(40)
        AirPushbackX(25000)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)

        def upon_11():
            Unknown1019(40)
        Unknown23059(1)
    sprite('su232_00', 4)	# 1-4
    Unknown2006()
    sprite('su232_01', 4)	# 5-8
    sprite('su232_04', 2)	# 9-10
    physicsXImpulse(50000)
    SFX_3('slash_beam_slow')
    sprite('su232_05', 4)	# 11-14	 **attackbox here**
    GFX_0('suef_2C', 0)
    Unknown23029(2, 12, 0)
    RefreshMultihit()
    Unknown1019(70)
    sprite('su232_06', 4)	# 15-18	 **attackbox here**
    Unknown1019(60)
    sprite('su232_07', 4)	# 19-22	 **attackbox here**
    StartMultihit()
    Unknown1019(60)
    sprite('su232_08', 4)	# 23-26	 **attackbox here**
    Unknown1019(60)
    StartMultihit()
    sprite('su232_06', 4)	# 27-30	 **attackbox here**
    Unknown1019(60)
    StartMultihit()
    sprite('su232_07', 4)	# 31-34	 **attackbox here**
    Unknown1019(0)
    StartMultihit()
    sprite('su232_08', 4)	# 35-38	 **attackbox here**
    StartMultihit()
    sprite('keep', 32767)	# 39-32805
    enterState('PersonaDeleteAndIdling')

@State
def PNA_Persona2BHold():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000000000000050c30000806967ff80969800806967ff80969800')
        callSubroutine('PNA_AttackInit')
        AttackLevel_(4)
        Damage(1700)
        AttackP1(90)
        AttackP2(70)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirUntechableTime(40)
        Unknown9016(1)
        AirPushbackX(80000)
        AirPushbackY(30000)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown23078(1)

        def upon_11():
            Unknown1019(40)
        Unknown23029(3, 3018, 0)
    sprite('su232_01', 5)	# 1-5
    ScreenShake(5000, 0)
    sprite('su232_01', 5)	# 6-10
    ScreenShake(5000, 0)
    sprite('su232_01', 5)	# 11-15
    ScreenShake(5000, 0)
    sprite('su232_01', 5)	# 16-20
    ScreenShake(5000, 0)
    label(0)
    sprite('su232_04', 4)	# 21-24
    physicsXImpulse(50000)
    SFX_3('slash_beam_slow')
    sprite('su232_05', 4)	# 25-28	 **attackbox here**
    GFX_0('suef_2C', 0)
    Unknown23029(2, 12, 0)
    RefreshMultihit()
    Unknown1019(70)
    sprite('su232_06', 4)	# 29-32	 **attackbox here**
    Unknown1019(60)
    sprite('su232_07', 4)	# 33-36	 **attackbox here**
    Unknown1019(60)
    sprite('su232_08', 4)	# 37-40	 **attackbox here**
    Unknown1019(60)
    sprite('su232_06', 4)	# 41-44	 **attackbox here**
    Unknown1019(60)
    StartMultihit()
    sprite('su232_07', 4)	# 45-48	 **attackbox here**
    Unknown1019(0)
    StartMultihit()
    sprite('su232_08', 4)	# 49-52	 **attackbox here**
    StartMultihit()
    sprite('keep', 32767)	# 53-32819
    enterState('PersonaDeleteAndIdling')

@State
def PNA_PersonaJB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff20bf020000000000000000000000000000000000')
        callSubroutine('PNA_AttackInit')
        EnableCollision(0)
        AttackLevel_(3)
        HitOverhead(2)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown4007(3)
        Unknown2053(1)
        Unknown23078(1)
        callSubroutine('PNA_CheckWarp')

        def upon_43():
            if (SLOT_48 == 302):
                sendToLabel(580)
            if (SLOT_48 == 303):
                sendToLabel(580)
    sprite('su254_00', 3)	# 1-3
    sprite('su254_01', 3)	# 4-6
    SFX_3('slash_beam_fast')
    sprite('su254_03', 7)	# 7-13	 **attackbox here**
    RefreshMultihit()
    GFX_0('suef_Air5C', 0)
    sprite('su254_04', 3)	# 14-16
    sprite('su254_05', 3)	# 17-19
    sprite('su254_06', 3)	# 20-22
    sprite('su254_07', 3)	# 23-25
    label(580)
    sprite('keep', 32767)	# 26-32792
    enterState('PersonaDeleteAndIdling')

@State
def PNA_PersonaJC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e00206cfbff20a10700')
        callSubroutine('PNA_AttackInit')
        AttackLevel_(4)
        AttackP2(75)
        AirPushbackX(23000)
        AirPushbackY(15000)
        AirUntechableTime(30)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Hitstop(6)
        PushbackX(29000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2053(1)
        EnableCollision(0)
        Unknown23078(1)
        callSubroutine('PNA_CheckWarp')
        Unknown23059(1)
    sprite('su255_00', 8)	# 1-8	 **attackbox here**
    GFX_0('Air5DTossinAura', 0)
    physicsXImpulse(3000)
    StartMultihit()
    sprite('su255_01', 2)	# 9-10	 **attackbox here**
    Unknown23029(2, 12, 0)
    RefreshMultihit()
    ProjectileDurabilityLvl(1)
    Unknown11034(0)
    Unknown4007(0)
    physicsXImpulse(49700)
    SFX_3('slash_pole_slow')
    sprite('su255_02', 2)	# 11-12	 **attackbox here**
    Unknown1019(80)
    sprite('su255_03', 2)	# 13-14	 **attackbox here**
    Unknown1019(80)
    sprite('su255_04', 2)	# 15-16	 **attackbox here**
    Unknown1019(80)
    sprite('su255_05', 2)	# 17-18	 **attackbox here**
    Unknown1019(80)
    sprite('su255_00', 2)	# 19-20	 **attackbox here**
    Unknown1019(30)
    sprite('su255_01', 2)	# 21-22	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('su255_02', 2)	# 23-24	 **attackbox here**
    sprite('su255_03', 2)	# 25-26	 **attackbox here**
    sprite('su255_06', 4)	# 27-30
    Unknown1019(50)
    sprite('su255_07', 4)	# 31-34
    sprite('su255_08', 4)	# 35-38
    Unknown1019(50)
    sprite('su255_09', 4)	# 39-42
    SFX_3('cloth_l')
    sprite('su255_07', 4)	# 43-46
    Unknown1019(0)
    sprite('su255_08', 4)	# 47-50
    sprite('su255_09', 4)	# 51-54
    SFX_3('cloth_l')
    sprite('su255_07', 4)	# 55-58
    sprite('su255_08', 4)	# 59-62
    sprite('keep', 32767)	# 63-32829
    enterState('PersonaDeleteAndIdling')

@State
def PNA_PersonaJ_Test():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000a08601000000000000000000a0860100a0860100')
        callSubroutine('PNA_AttackInit')
        EnableCollision(0)
        AttackLevel_(3)
        AirPushbackY(20000)
        HitOverhead(2)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Hitstop(9)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown4007(3)
        Unknown2053(1)
        Unknown23078(1)
        callSubroutine('PNA_CheckWarp')

        def upon_43():
            if (SLOT_48 == 302):
                sendToLabel(580)
            if (SLOT_48 == 303):
                sendToLabel(580)
    sprite('su205_00', 2)	# 1-2
    physicsXImpulse(5000)
    sprite('su205_01', 1)	# 3-3
    sprite('su205_02', 1)	# 4-4
    sprite('su206_01', 1)	# 5-5
    sprite('su206_02', 2)	# 6-7
    sprite('su206_03', 2)	# 8-9
    GFX_0('suef_5DD', 100)
    physicsXImpulse(0)
    sprite('su206_04', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_beam_middle')
    sprite('su206_06', 4)	# 13-16
    GFX_0('suef_5DDD', 100)
    sprite('su206_07', 3)	# 17-19	 **attackbox here**
    Unknown23029(2, 12, 0)
    RefreshMultihit()
    SFX_3('slash_beam_middle')
    sprite('su206_07', 10)	# 20-29	 **attackbox here**
    StartMultihit()
    Unknown1019(25)
    sprite('su206_08', 6)	# 30-35
    Unknown1019(25)
    label(580)
    sprite('keep', 32767)	# 36-32802
    enterState('PersonaDeleteAndIdling')

@State
def Trap():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000070a0feff7011010000000000000000000000000000000000')
        callSubroutine('PNA_AttackInit')
        Unknown3032()
        Unknown3001(50)
        Unknown3004(20)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su400_00', 3)	# 1-3
    sprite('su400_01', 3)	# 4-6
    sprite('su400_02', 3)	# 7-9
    sprite('su400_00', 3)	# 10-12
    sprite('su400_01', 3)	# 13-15
    sprite('su400_02', 3)	# 16-18
    sprite('su400_00', 4)	# 19-22
    sprite('su400_01', 4)	# 23-26
    sprite('su400_02', 4)	# 27-30
    sprite('keep', 32767)	# 31-32797
    enterState('PersonaDeleteAndIdling')

@State
def PartnerAssistAtk_B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000605b0300204e000000000000000000000000000000000000')
        callSubroutine('PNA_SPAttackInit')
        AttackLevel_(4)
        Damage(600)
        AttackP1(70)
        Unknown11092(1)
        Hitstop(1)
        PushbackX(12000)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(40000)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        Unknown11042(1)
        ChipDamagePct(5)
        Unknown3032()
        Unknown3001(50)
        Unknown3004(20)
        Unknown11057(500)
        Unknown2053(1)
        EnableCollision(1)
        Unknown2015(50)
        callSubroutine('PNA_CheckWarp')
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23059(1)
    sprite('su410_03', 1)	# 1-1
    StartMultihit()
    physicsXImpulse(0)
    GFX_0('suef_410', 103)
    GFX_0('suef_410_add', 103)
    GFX_0('suef_410_zapper', 103)
    sprite('su410_03', 3)	# 2-4
    RefreshMultihit()
    physicsYImpulse(3000)
    physicsXImpulse(2000)
    sprite('su410_04', 3)	# 5-7	 **attackbox here**
    YAccel(200)
    Unknown1019(200)
    RefreshMultihit()
    sprite('su410_05', 3)	# 8-10	 **attackbox here**
    YAccel(200)
    Unknown1019(200)
    RefreshMultihit()
    sprite('su410_04', 3)	# 11-13	 **attackbox here**
    YAccel(200)
    Unknown1019(200)
    RefreshMultihit()
    sprite('su410_05', 3)	# 14-16	 **attackbox here**
    YAccel(200)
    Unknown1019(200)
    RefreshMultihit()
    sprite('su410_04', 2)	# 17-18	 **attackbox here**
    YAccel(80)
    Unknown1019(50)
    RefreshMultihit()
    sprite('su410_06', 2)	# 19-20
    EnableCollision(0)
    YAccel(0)
    Unknown1019(0)
    setInvincible(0)
    sprite('su410_07', 3)	# 21-23
    Unknown26('suef_410_zapper')
    sprite('su410_08', 5)	# 24-28
    sprite('su410_07', 5)	# 29-33
    sprite('su410_08', 5)	# 34-38
    sprite('su410_07', 5)	# 39-43
    sprite('su410_08', 5)	# 44-48
    sprite('su410_07', 5)	# 49-53
    sprite('su410_08', 5)	# 54-58
    sprite('su410_07', 5)	# 59-63
    sprite('keep', 32767)	# 64-32830
    enterState('PersonaDeleteAndIdling')
    Unknown26('suef_410')
    Unknown26('suef_410_add')

@State
def PAssault2_RA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079fefff049020000000000000000000000000000000000')
        callSubroutine('PNA_AttackInit')
        Unknown23022(1)
        EnableCollision(0)
        Unknown4007(3)
        callSubroutine('PNA_CheckWarp')
    sprite('su400_00', 3)	# 1-3
    sprite('su400_01', 3)	# 4-6
    sprite('su400_02', 3)	# 7-9
    sprite('su400_00', 3)	# 10-12
    sprite('su400_01', 3)	# 13-15
    sprite('su400_02', 3)	# 16-18
    sprite('su400_00', 4)	# 19-22
    sprite('su400_01', 4)	# 23-26
    sprite('su400_02', 4)	# 27-30
    sprite('su400_00', 5)	# 31-35
    sprite('su400_01', 5)	# 36-40
    sprite('su400_02', 5)	# 41-45
    sprite('keep', 32767)	# 46-32812
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateHAMAON():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23023()
        Unknown23184('0300000064000000b03cffffa086010000000000000000000000000000000000')
        callSubroutine('PNA_AttackInit')
        Hitstop(0)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su432_00', 4)	# 1-4
    Unknown2006()
    sprite('su432_01', 10)	# 5-14
    sprite('su432_02', 4)	# 15-18
    sprite('su432_03', 4)	# 19-22
    GFX_0('Hamaon_search', -1)
    Unknown36(1)
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(100000)
    Unknown35()
    Unknown2054(0)
    sprite('su432_04', 4)	# 23-26
    sprite('su432_05', 4)	# 27-30
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 31-34
    sprite('su432_04', 4)	# 35-38
    sprite('su432_05', 4)	# 39-42
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 43-46
    sprite('su432_04', 4)	# 47-50
    sprite('su432_05', 4)	# 51-54
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 55-58
    sprite('su432_04', 4)	# 59-62
    sprite('su432_05', 4)	# 63-66
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 67-70
    sprite('su432_04', 4)	# 71-74
    sprite('su432_05', 4)	# 75-78
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 79-82
    sprite('su432_04', 4)	# 83-86
    sprite('su432_05', 4)	# 87-90
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 91-94
    sprite('su432_04', 4)	# 95-98
    sprite('su432_05', 4)	# 99-102
    sprite('keep', 32767)	# 103-32869
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateODHAMAON():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23023()
        Unknown23184('0300000064000000b03cffffa086010000000000000000000000000000000000')
        callSubroutine('PNA_AttackInit')
        Unknown23056('')
        Hitstop(0)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su432_00', 4)	# 1-4
    Unknown2006()
    sprite('su432_01', 10)	# 5-14
    sprite('su432_02', 4)	# 15-18
    sprite('su432_03', 4)	# 19-22
    GFX_0('Hamaon_search', -1)
    Unknown36(1)
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(100000)
    Unknown35()
    Unknown2054(0)
    sprite('su432_04', 4)	# 23-26
    sprite('su432_05', 4)	# 27-30
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 31-34
    sprite('su432_04', 4)	# 35-38
    sprite('su432_05', 4)	# 39-42
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 43-46
    sprite('su432_04', 4)	# 47-50
    sprite('su432_05', 4)	# 51-54
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 55-58
    sprite('su432_04', 4)	# 59-62
    sprite('su432_05', 4)	# 63-66
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 67-70
    sprite('su432_04', 4)	# 71-74
    sprite('su432_05', 4)	# 75-78
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 79-82
    sprite('su432_04', 4)	# 83-86
    sprite('su432_05', 4)	# 87-90
    SFX_3('cloth_l')
    sprite('su432_03', 4)	# 91-94
    sprite('su432_04', 4)	# 95-98
    sprite('su432_05', 4)	# 99-102
    sprite('keep', 32767)	# 103-32869
    enterState('PersonaDeleteAndIdling')

@State
def PartnerAssistAtk_D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000a0860100806967ff80969800806967ff80969800')
        callSubroutine('PNA_SPAttackInit')
        AttackLevel_(4)
        Damage(1200)
        AttackP1(70)
        Unknown11092(1)
        AirUntechableTime(40)
        AirPushbackX(15000)
        AirPushbackY(3000)
        Unknown9016(1)
        Hitstop(7)
        Unknown11042(1)
        ChipDamagePct(5)
        physicsXImpulse(30000)
        callSubroutine('PNA_CheckWarp')
        Unknown2053(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23059(1)
    sprite('su205_00', 2)	# 1-2
    Unknown1045(40000)
    sprite('su205_01', 1)	# 3-3
    sprite('su205_02', 1)	# 4-4
    sprite('su206_01', 1)	# 5-5
    sprite('su206_02', 2)	# 6-7
    sprite('su206_03', 2)	# 8-9
    GFX_0('suef_5DD', 100)
    sprite('su206_04', 2)	# 10-11	 **attackbox here**
    Unknown1084(1)
    RefreshMultihit()
    SFX_3('slash_beam_middle')
    sprite('su206_06', 2)	# 12-13
    physicsXImpulse(20000)
    Unknown1019(140)
    GFX_0('suef_5DDD', 100)
    sprite('su206_07', 6)	# 14-19	 **attackbox here**

    def upon_78():
        clearUponHandler(78)
        SLOT_10 = 1
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackY(20000)
    SFX_3('slash_beam_middle')
    sprite('su206_07', 10)	# 20-29	 **attackbox here**
    StartMultihit()
    Unknown1019(25)
    sprite('su206_08', 20)	# 30-49
    Unknown1019(25)
    sprite('keep', 32767)	# 50-32816
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateMUDOON():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff289a01000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PNA_AttackInit')
        Unknown23056('')
        EnableCollision(0)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PNA_CheckWarp')
    sprite('su432_00', 3)	# 1-3
    sprite('su432_01', 3)	# 4-6
    sprite('su432_06', 4)	# 7-10
    GFX_0('Mudoon_search', 100)
    sprite('su432_07', 4)	# 11-14
    GFX_0('Mudoon', 100)
    sprite('su432_08', 4)	# 15-18
    sprite('su432_09', 4)	# 19-22
    SFX_3('cloth_l')
    sprite('su432_07', 4)	# 23-26
    sprite('su432_08', 4)	# 27-30
    sprite('su432_09', 4)	# 31-34
    SFX_3('cloth_l')
    sprite('su432_07', 4)	# 35-38
    sprite('su432_08', 4)	# 39-42
    sprite('su432_09', 4)	# 43-46
    SFX_3('cloth_l')
    sprite('su432_07', 4)	# 47-50
    sprite('su432_08', 4)	# 51-54
    sprite('su432_09', 4)	# 55-58
    SFX_3('cloth_l')
    sprite('su432_07', 4)	# 59-62
    sprite('su432_08', 4)	# 63-66
    sprite('su432_09', 4)	# 67-70
    SFX_3('cloth_l')
    sprite('su432_07', 4)	# 71-74
    sprite('su432_08', 4)	# 75-78
    sprite('su432_09', 4)	# 79-82
    SFX_3('cloth_l')
    sprite('su432_07', 4)	# 83-86
    sprite('keep', 32767)	# 87-32853
    enterState('PersonaDeleteAndIdling')

@State
def PNA_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PersonaReset')
        Unknown3032()
        Unknown2012()
        Unknown23022(1)
        Unknown23184('030000006400000010b6fdff400d030000000000000000000000000000000000')
        callSubroutine('PNA_CheckWarp')
        Unknown1086(22)
        teleportRelativeY(120000)
        Unknown4009(3)
        Unknown23066(1)
        Unknown2053(0)
        SLOT_53 = 0

        def upon_43():
            if (SLOT_48 == 9512):
                SLOT_53 = (SLOT_53 + 1)
                if (SLOT_53 == 3):
                    clearUponHandler(43)
                    sendToLabel(10)
            if (SLOT_48 == 9511):
                sendToLabel(0)

        def upon_44():
            sendToLabel(0)
    sprite('su450_00', 8)	# 1-8
    sprite('su450_01', 4)	# 9-12
    GFX_0('ZanzohCircle', 100)
    SFX_0('magiccircle_b')
    sprite('su450_02', 4)	# 13-16
    sprite('su450_03', 4)	# 17-20
    sprite('su450_04', 4)	# 21-24
    sprite('su450_05', 4)	# 25-28
    sprite('su450_06', 4)	# 29-32
    GFX_0('Ichigeki_Marker', 0)
    SFX_0('magiccircle_b')
    sprite('su450_07', 4)	# 33-36
    sprite('su450_08', 4)	# 37-40
    sprite('su450_06', 4)	# 41-44
    sprite('su450_07', 4)	# 45-48
    sprite('su450_08', 4)	# 49-52
    sprite('su450_06', 4)	# 53-56
    sprite('su450_07', 4)	# 57-60
    sprite('su450_08', 4)	# 61-64
    sprite('su450_06', 4)	# 65-68
    Unknown3004(-16)
    sprite('su450_07', 4)	# 69-72
    sprite('su450_08', 4)	# 73-76
    sprite('su450_06', 4)	# 77-80
    loopRest()
    sprite('null', 16)	# 81-96
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 3
    Unknown48('010000000200000033000000190000000200000000000000')
    Unknown36(1)
    Unknown23032(90)
    teleportRelativeY(550000)
    Unknown35()
    SFX_0('magiccircle_b')
    sprite('null', 1)	# 97-97
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 2
    Unknown48('010000000200000033000000190000000200000000000000')
    Unknown36(1)
    Unknown23032(10)
    teleportRelativeY(250000)
    Unknown35()
    SFX_0('magiccircle_b')
    sprite('null', 32767)	# 98-32864
    label(10)
    sprite('null', 1)	# 32865-32865
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000001e25000000000000')
    Unknown21015('4963686967656b695f4d61726b657200000000000000000000000000000000003c25000000000000')
    label(0)
    sprite('keep', 32767)	# 32866-65632
    enterState('PNA_PersonaWait')

@State
def destinyzero_damy():

    def upon_IMMEDIATE():
        Unknown23067('suef_destinyzero_09')
        Unknown1086(22)
        Unknown1007(230000)
        Unknown2007()
    sprite('null', 60)	# 1-60

@State
def destinyzero_main():

    def upon_IMMEDIATE():
        Unknown23067('suef_destinyzero_09')
        Unknown1086(22)
        Unknown1007(230000)
        Unknown2007()
    sprite('null', 60)	# 1-60

@State
def destinyzero_sub():

    def upon_IMMEDIATE():
        Unknown23067('suef_destinyzero_09')
        Unknown1086(23)
        Unknown1007(230000)
        Unknown2007()
    sprite('null', 60)	# 1-60

@State
def destinyzero_Cutin_main1_3Naoto():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown6001(1)
        Unknown2019(500)
        Unknown1000(-640000)
        teleportRelativeY(-640000)
        teleportRelativeX(676500)
        Unknown1007(353000)
        Unknown1096(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)	# 1-3
    Unknown3004(43)
    physicsXImpulse(-40000)
    Unknown1028(3000)
    sprite('vr_pna_cutin', 5)	# 4-8
    sprite('vr_pna_cutin', 25)	# 9-33
    physicsXImpulse(-1000)
    Unknown1028(0)
    sprite('vr_pna_cutin', 4)	# 34-37
    Unknown3004(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)	# 38-59
    Unknown3004(-255)

@State
def destinyzero_Cutin_main1_3dokuro():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown6001(1)
        Unknown2019(1000)
        Unknown1000(-640000)
        teleportRelativeY(-640000)
        teleportRelativeX(676500)
        Unknown1007(370000)
        Unknown1096(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)	# 1-8
    Unknown3004(31)
    physicsXImpulse(-40000)
    Unknown1028(3000)
    sprite('vr_pna_cutin_skull', 25)	# 9-33
    physicsXImpulse(-1000)
    Unknown1028(0)
    sprite('vr_pna_cutin_skull', 27)	# 34-60
    Unknown3004(-51)
    physicsXImpulse(-20000)

@State
def destinyzero_Cutin_sub1_3Naoto():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown6001(1)
        Unknown2019(500)
        Unknown1000(-640000)
        teleportRelativeY(-640000)
        teleportRelativeX(676500)
        Unknown1007(353000)
        Unknown1096(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)	# 1-3
    Unknown3004(43)
    physicsXImpulse(-40000)
    Unknown1028(3000)
    sprite('vr_pna_cutin', 5)	# 4-8
    sprite('vr_pna_cutin', 25)	# 9-33
    physicsXImpulse(-1000)
    Unknown1028(0)
    sprite('vr_pna_cutin', 4)	# 34-37
    Unknown3004(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)	# 38-59
    Unknown3004(-255)

@State
def destinyzero_Cutin_sub1_3dokuro():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown6001(1)
        Unknown2019(1000)
        Unknown1000(-640000)
        teleportRelativeY(-640000)
        teleportRelativeX(676500)
        Unknown1007(370000)
        Unknown1096(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)	# 1-8
    Unknown3004(31)
    physicsXImpulse(-40000)
    Unknown1028(3000)
    sprite('vr_pna_cutin_skull', 25)	# 9-33
    physicsXImpulse(-1000)
    Unknown1028(0)
    sprite('vr_pna_cutin_skull', 27)	# 34-60
    Unknown3004(-51)
    physicsXImpulse(-20000)

@State
def destinyzero_Cutin_main2_4Naoto():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown6001(1)
        Unknown2019(500)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        teleportRelativeX(676500)
        Unknown1007(353000)
        Unknown1096(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)	# 1-3
    Unknown3004(43)
    physicsXImpulse(-40000)
    Unknown1028(3000)
    sprite('vr_pna_cutin', 5)	# 4-8
    sprite('vr_pna_cutin', 25)	# 9-33
    physicsXImpulse(-1000)
    Unknown1028(0)
    sprite('vr_pna_cutin', 4)	# 34-37
    Unknown3004(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)	# 38-59
    Unknown3004(-255)

@State
def destinyzero_Cutin_main2_4dokuro():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown6001(1)
        Unknown2019(1000)
        Unknown1000(-640000)
        teleportRelativeY(-640000)
        teleportRelativeX(-676500)
        Unknown1007(370000)
        Unknown1096(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)	# 1-8
    Unknown3004(31)
    physicsXImpulse(40000)
    Unknown1028(-3000)
    sprite('vr_pna_cutin_skull', 25)	# 9-33
    physicsXImpulse(1000)
    Unknown1028(0)
    sprite('vr_pna_cutin_skull', 27)	# 34-60
    Unknown3004(-51)
    physicsXImpulse(20000)

@State
def destinyzero_Cutin_sub2_4Naoto():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown6001(1)
        Unknown2019(500)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        teleportRelativeX(676500)
        Unknown1007(353000)
        Unknown1096(720)
        Unknown3001(125)
    sprite('vr_pna_cutin', 3)	# 1-3
    Unknown3004(43)
    physicsXImpulse(-40000)
    Unknown1028(3000)
    sprite('vr_pna_cutin', 5)	# 4-8
    sprite('vr_pna_cutin', 25)	# 9-33
    physicsXImpulse(-1000)
    Unknown1028(0)
    sprite('vr_pna_cutin', 4)	# 34-37
    Unknown3004(-25)
    physicsXImpulse(-20000)
    sprite('vr_pna_cutin', 22)	# 38-59
    Unknown3004(-255)

@State
def destinyzero_Cutin_sub2_4dokuro():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown6001(1)
        Unknown2019(1000)
        Unknown1000(-640000)
        teleportRelativeY(-640000)
        teleportRelativeX(-676500)
        Unknown1007(370000)
        Unknown1096(720)
        Unknown3001(0)
    sprite('vr_pna_cutin_skull', 8)	# 1-8
    Unknown3004(31)
    physicsXImpulse(40000)
    Unknown1028(-3000)
    sprite('vr_pna_cutin_skull', 25)	# 9-33
    physicsXImpulse(1000)
    Unknown1028(0)
    sprite('vr_pna_cutin_skull', 27)	# 34-60
    Unknown3004(-51)
    physicsXImpulse(20000)

@State
def DanganD_CCA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1800)
        GroundedHitstunAnimation(1)
        AirPushbackX(30000)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(3000)
        AirUntechableTime(40)
        Unknown11034(1)
        ProjectileDurabilityLvl(1)
        MinimumDamagePct(0)
        Unknown3033()
        Unknown2054(1)
        Unknown11044(1)
        Unknown30088(1)
    sprite('vr_impact2_Ex', 2)	# 1-2	 **attackbox here**
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    SFX_3('ice_break_fast')
    sprite('vr_impact2_Ex', 20)	# 3-22	 **attackbox here**
    Unknown23029(3, 3020, 0)
    Unknown2001()

@State
def DanganD():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1800)
        GroundedHitstunAnimation(1)
        AirPushbackX(30000)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(3000)
        AirUntechableTime(40)
        Unknown11034(1)
        ProjectileDurabilityLvl(1)
        MinimumDamagePct(0)
        Unknown3033()
        Unknown2054(1)
    sprite('vr_impact2_Ex', 2)	# 1-2	 **attackbox here**
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    SFX_3('ice_break_fast')
    sprite('vr_impact2_Ex', 20)	# 3-22	 **attackbox here**
    Unknown23029(3, 3020, 0)
    Unknown2001()

@State
def DanganD_Ex():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1500)
        AttackP1(70)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown9178(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(40)
        AirPushbackX(60000)
        AirPushbackY(25000)
        AirUntechableTime(50)
        Unknown11042(1)
        Unknown3033()
        Unknown2054(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(1)
    sprite('vr_impact2_Ex', 2)	# 1-2	 **attackbox here**
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    SFX_3('ice_break_fast')
    sprite('vr_impact2_Ex', 20)	# 3-22	 **attackbox here**
    Unknown23029(3, 3020, 0)
    Unknown2001()

@State
def DanganDASS():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
    sprite('vr_impact2', 2)	# 1-2	 **attackbox here**
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    SFX_3('ice_break_fast')
    sprite('vr_impact2', 20)	# 3-22	 **attackbox here**
    Unknown2001()

@State
def BarrierBrake():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4015()
        Unknown3001(150)
    sprite('null', 10)	# 1-10
    GFX_1('suef_sheldbrakeb_08', 100)
    Unknown1099(50)
    sprite('null', 10)	# 11-20
    Unknown3004(-26)

@State
def suef_5C():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(1)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_su204_00', 3)	# 1-3
    sprite('vr_su204_01', 16)	# 4-19

@State
def suef_5DD():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(1)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_su206_00', 2)	# 1-2
    sprite('vr_su206_01', 2)	# 3-4

@State
def suef_5DDD():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(1)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_su206_10', 2)	# 1-2
    sprite('vr_su206_11', 3)	# 3-5

@State
def suef_5DDDD():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(1)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_su206_20', 3)	# 1-3
    sprite('vr_su206_21', 3)	# 4-6
    sprite('vr_su206_22', 16)	# 7-22

@State
def suef_2C():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('737565665f32333274756b697375622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 20)	# 1-20
    Unknown23067('suef_bannotuki_07')
    sprite('null', 15)	# 21-35
    Unknown3004(-17)

@State
def suef_Air5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
    sprite('null', 60)	# 1-60
    Unknown4061(1)
    Unknown4047(55, 55, 55)
    Unknown23067('suef_air5c')

@State
def Air5DTossinAura():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown3032()
        Unknown23067('suef_tossin_04')
        Unknown4003('737565665f313231746f7373696e7375622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 30)	# 1-30
    sprite('null', 10)	# 31-40
    Unknown3004(-26)

@State
def GunKira():

    def upon_IMMEDIATE():
        GFX_2('naef_gunkira')
        Unknown4010(2)
        Unknown4007(2)
    sprite('null', 6)	# 1-6
    sprite('null', 60)	# 7-66
    Unknown1084(1)

@State
def Yakkyo():

    def upon_IMMEDIATE():

        def upon_5():
            YAccel(-60)
            Unknown1019(60)

        def upon_LANDING():
            SFX_3('na006')
        Unknown4061(2)
    sprite('vr_trap_yakkyo', 50)	# 1-50
    Unknown1025(-7500, -12500)
    Unknown1026(2500, 3250)
    Unknown1078(-80000, -100000)
    setGravity(2000)
    sprite('vr_trap_yakkyo', 20)	# 51-70
    Unknown3032()
    Unknown3004(-20)

@State
def Jumpsmoke():

    def upon_IMMEDIATE():
        Unknown23067('naef_kicksmoke_04')
    sprite('null', 30)	# 1-30

@State
def Tossin_atk1():

    def upon_IMMEDIATE():
        Unknown23067('naef_407circleA')
        Unknown4007(2)
        Unknown23015(1)
        Unknown4010(2)
    sprite('null', 3)	# 1-3
    Unknown1099(40)
    sprite('null', 7)	# 4-10
    Unknown3004(-40)

@State
def Tossin_atk2():

    def upon_IMMEDIATE():
        Unknown4003('6e6165665f343032746f7373696e5f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4009(2)
        Unknown3032()
        Unknown3001(180)
        Unknown4010(2)
    sprite('null', 14)	# 1-14

@State
def Dangan():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP1(80)
        AttackP2(90)
        Hitstop(5)
        PushbackX(15000)
        Unknown14083(0)
        Unknown23026(80000)
        Unknown3029(1)
        physicsXImpulse(120000)
        Unknown4061(2)
        SLOT_51 = 12

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + (-1))

            def upon_ON_HIT_OR_BLOCK():
                clearUponHandler(10)
                clearUponHandler(3)
                Unknown13(25)
                Unknown21015('53686167656b6941000000000000000000000000000000000000000000000000c80b000000000000')
                Unknown21015('53686167656b6942000000000000000000000000000000000000000000000000c80b000000000000')
                Unknown21015('53686167656b6943000000000000000000000000000000000000000000000000c80b000000000000')

        def upon_43():
            if (SLOT_48 == 3010):
                Unknown1072(0)
                Unknown4055(0)
                Unknown4045('6e6165665f34303167756e66697265000000000000000000000000000000000000000000')
                Unknown1110(120000, 0)
                Damage(600)
                if Unknown48('19000000020000000000000003000000020000003e000000'):
                    MinimumDamagePct(10)
                    Unknown30065(0)
            if (SLOT_48 == 3011):
                Unknown1072(-20000)
                Unknown4055(0)
                Unknown4045('6e6165665f34303167756e66697265000000000000000000000000000000000000000000')
                Unknown1110(120000, 0)
                AirHitstunAnimation(10)
                GroundedHitstunAnimation(10)
                Damage(700)
                if Unknown48('19000000020000000000000003000000020000003e000000'):
                    MinimumDamagePct(10)
                    Unknown30065(0)
                sendToLabel(1)
            if (SLOT_48 == 3019):
                Unknown1072(60000)
                Unknown4055(0)
                Unknown4045('6e6165665f34303167756e66697265000000000000000000000000000000000000000000')
                Unknown1110(120000, 0)
                AirHitstunAnimation(11)
                GroundedHitstunAnimation(11)
                Damage(500)
                if Unknown48('19000000020000000000000003000000020000003e000000'):
                    MinimumDamagePct(10)
                    Unknown30065(0)
                sendToLabel(2)

                def upon_5():
                    YAccel(-100)
                    Unknown1108(0)
                    GFX_1('naef_tyakudan', 100)
        Unknown23067('naef_401dando')
    label(0)
    sprite('vr_dangan_a_front', 2)	# 1-2	 **attackbox here**
    sprite('vr_dangan_a_front', 298)	# 3-300	 **attackbox here**
    loopRest()
    ExitState()
    label(1)
    sprite('vr_dangan_a_front', 1)	# 301-301	 **attackbox here**
    loopRest()
    gotoLabel(9)
    label(2)
    sprite('vr_dangan_a_front', 1)	# 302-302	 **attackbox here**
    label(9)
    sprite('vr_dangan_a', 298)	# 303-600	 **attackbox here**

@State
def Dangan_PS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP1(70)
        AttackP2(90)
        Hitstop(5)
        PushbackX(15000)
        Unknown14083(0)
        Unknown23026(80000)
        Unknown11042(1)
        Unknown3029(1)
        physicsXImpulse(120000)
        Unknown4061(2)

        def upon_CLEAR_OR_EXIT():

            def upon_ON_HIT_OR_BLOCK():
                clearUponHandler(10)
                clearUponHandler(3)
                Unknown13(25)

        def upon_43():
            if (SLOT_48 == 3010):
                Unknown1072(0)
                Unknown4055(0)
                Unknown4045('6e6165665f34303167756e66697265000000000000000000000000000000000000000000')
                Unknown1110(120000, 0)
                Damage(600)
                if Unknown48('19000000020000000000000003000000020000003e000000'):
                    MinimumDamagePct(10)
                    Unknown30065(0)
            if (SLOT_48 == 3011):
                Unknown1072(-20000)
                Unknown4055(0)
                Unknown4045('6e6165665f34303167756e66697265000000000000000000000000000000000000000000')
                Unknown1110(120000, 0)
                AirHitstunAnimation(10)
                GroundedHitstunAnimation(10)
                Damage(700)
                if Unknown48('19000000020000000000000003000000020000003e000000'):
                    MinimumDamagePct(10)
                    Unknown30065(0)
                sendToLabel(1)
            if (SLOT_48 == 3019):
                Unknown1072(60000)
                Unknown4055(0)
                Unknown4045('6e6165665f34303167756e66697265000000000000000000000000000000000000000000')
                Unknown1110(120000, 0)
                AirHitstunAnimation(11)
                GroundedHitstunAnimation(11)
                Damage(500)
                if Unknown48('19000000020000000000000003000000020000003e000000'):
                    MinimumDamagePct(10)
                    Unknown30065(0)
                sendToLabel(2)

                def upon_5():
                    YAccel(-100)
                    Unknown1108(0)
                    GFX_1('naef_tyakudan', 100)
        Unknown23067('naef_401dando')
    label(0)
    sprite('vr_dangan_a_front', 2)	# 1-2	 **attackbox here**
    sprite('vr_dangan_a_front', 298)	# 3-300	 **attackbox here**
    loopRest()
    ExitState()
    label(1)
    sprite('vr_dangan_a_front', 1)	# 301-301	 **attackbox here**
    loopRest()
    gotoLabel(9)
    label(2)
    sprite('vr_dangan_a_front', 1)	# 302-302	 **attackbox here**
    label(9)
    sprite('vr_dangan_a', 298)	# 303-600	 **attackbox here**

@State
def DanganLastA_PS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(1800)
        AttackP1(70)
        ChipDamagePct(20)
        Unknown11042(1)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackX(60000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        WallbounceReboundTime(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown13(25)
        PushbackX(30000)
        Unknown11001(8, 0, 0)
        Unknown3029(1)
        physicsXImpulse(120000)
        Unknown4061(2)
        Unknown1072(0)
        Unknown4055(0)
        Unknown4045('6e6165665f34303167756e666972656c6173740000000000000000000000000000000000')
        Unknown1110(120000, 0)
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)	# 1-2	 **attackbox here**
    RefreshMultihit()
    sprite('vr_dangan_a_front', 300)	# 3-302	 **attackbox here**
    PushbackX(12000)
    Unknown11001(0, 0, 0)

@State
def DanganLastA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(1800)
        AttackP1(80)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackX(60000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        WallbounceReboundTime(0)
        if Unknown48('19000000020000000000000003000000020000003e000000'):
            MinimumDamagePct(10)
            Unknown30065(0)
        PushbackX(30000)
        Unknown11001(8, 0, 0)
        Unknown3029(1)
        physicsXImpulse(120000)
        Unknown4061(2)
        Unknown1072(0)
        Unknown4055(0)
        Unknown4045('6e6165665f34303167756e666972656c6173740000000000000000000000000000000000')
        Unknown1110(120000, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('53686167656b6941000000000000000000000000000000000000000000000000a10f000000000000')
            Unknown13(25)
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)	# 1-2	 **attackbox here**
    RefreshMultihit()
    sprite('vr_dangan_a_front', 300)	# 3-302	 **attackbox here**
    PushbackX(12000)
    Unknown11001(0, 0, 0)

@State
def DanganLastB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(2100)
        AttackP1(80)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackY(40000)
        AirPushbackX(24000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        if Unknown48('19000000020000000000000003000000020000003e000000'):
            MinimumDamagePct(10)
            Unknown30065(0)
        PushbackX(30000)
        Unknown11001(8, 0, 0)
        Unknown3029(1)
        physicsXImpulse(120000)
        Unknown4061(2)
        Unknown1072(-20000)
        Unknown4055(0)
        Unknown4045('6e6165665f34303167756e666972656c6173740000000000000000000000000000000000')
        Unknown1110(120000, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown13(25)
            Unknown21015('53686167656b6942000000000000000000000000000000000000000000000000a10f000000000000')
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)	# 1-2	 **attackbox here**
    RefreshMultihit()
    sprite('vr_dangan_a', 298)	# 3-300	 **attackbox here**
    PushbackX(12000)
    Unknown11001(0, 0, 0)

@State
def DanganLastC():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(1500)
        AttackP1(80)
        AirUntechableTime(50)
        Hitstop(0)
        AirPushbackX(1000)
        AirPushbackY(34000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown23026(80000)
        if Unknown48('19000000020000000000000003000000020000003e000000'):
            MinimumDamagePct(10)
            Unknown30065(0)
        PushbackX(30000)
        Unknown11001(8, 0, 0)
        Unknown3029(1)
        physicsXImpulse(120000)
        Unknown4061(2)
        Unknown1072(60000)
        Unknown4055(0)
        Unknown4045('6e6165665f34303167756e666972656c6173740000000000000000000000000000000000')
        Unknown1110(120000, 0)

        def upon_5():
            YAccel(-100)
            Unknown1108(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown13(25)
            Unknown21015('53686167656b6943000000000000000000000000000000000000000000000000a10f000000000000')
        Unknown23067('naef_401dando')
    sprite('vr_dangan_a_front', 2)	# 1-2	 **attackbox here**
    RefreshMultihit()
    sprite('vr_dangan_a', 298)	# 3-300	 **attackbox here**
    PushbackX(12000)
    Unknown11001(0, 0, 0)

@State
def Tossin_atk2AB():

    def upon_IMMEDIATE():
        Unknown4003('6e6165665f343032746f7373696e5f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4009(2)
        Unknown3032()
        Unknown3001(180)
        Unknown4010(2)
    sprite('null', 14)	# 1-14

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

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_30):

            def upon_42():
                if SLOT_2:
                    Unknown23029(2, 3021, 0)
                    Unknown2038(-1)

@State
def vr_trap_aircore_damy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('vr_trap_aircore_damy', 32767)	# 1-32767

@State
def vr_trap_landcore_damy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('vr_trap_landcore_damy', 32767)	# 1-32767

@State
def TrapMatome():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown23089('0100000000000000000000000000000000000000000000000100000000000000')
        Unknown23091(1)
        teleportRelativeX(40000)
        if SLOT_8:
            Unknown23022(1)

            def upon_43():
                if (SLOT_48 == 3002):
                    Unknown23090(25)
                if (SLOT_48 == 3004):
                    SLOT_55 = 1
                if (SLOT_48 == 3021):
                    Unknown23090(25)

            def upon_CLEAR_OR_EXIT():
                if (SLOT_29 < 400000):
                    Unknown3001(255)
                    if (not SLOT_2):
                        Unknown2037(1)
                        GFX_1('naef_trapdetection_a', 103)
                    Unknown23022(0)
                if (SLOT_29 < 210000):
                    sendToLabel(14)
                    clearUponHandler(3)
                if (SLOT_165 < 210000):
                    sendToLabel(14)
                    clearUponHandler(3)
                if (not Unknown48('19000000020000000000000002000000020000009e000000')):
                    Unknown26('TrapMatome')
                    Unknown26('vr_trap_aircore_damy')
                    Unknown26('vr_trap_landcore_damy')
            sendToLabelUpon(54, 580)
        else:

            def upon_LANDING():
                sendToLabel(3)

            def upon_43():
                if (SLOT_48 == 3003):
                    Unknown23090(25)
                if (SLOT_48 == 3004):
                    SLOT_56 = 1
                if (SLOT_48 == 3021):
                    Unknown23090(25)

            def upon_CLEAR_OR_EXIT():
                if SLOT_IsInOverdrive2:
                    if Unknown48('190000000200000000000000160000000200000025000000'):
                        if (SLOT_29 < 400000):
                            Unknown23022(0)
                            Unknown3001(255)
                            if (not SLOT_2):
                                Unknown2037(1)
                                GFX_1('naef_trapdetection_a', 103)
                        if (SLOT_19 < 210000):
                            sendToLabel(141)
                            clearUponHandler(3)
                        if (SLOT_166 < 210000):
                            sendToLabel(141)
                            clearUponHandler(3)
                if (not Unknown48('19000000020000000000000002000000020000009e000000')):
                    Unknown26('TrapMatome')

            def upon_54():
                sendToLabel(581)
                clearUponHandler(2)
    if (not SLOT_8):
        gotoLabel(100)
    sprite('vr_trap_aircore', 2)	# 1-2
    GFX_1('naef_atrapstart_03', 103)
    GFX_1('naef_trapdetection_a', 103)
    if (SLOT_95 == 0):
        GFX_2('naef_airtrapjizoku2p_00')
    elif (SLOT_95 == 2):
        GFX_2('naef_airtrapjizoku2p_00')
    else:
        GFX_2('naef_airtrapjizoku_05')
    Unknown1084(1)
    GFX_0('vr_trap_aircore_damy', -1)
    sprite('vr_trap_aircore', 10)	# 3-12
    Unknown3004(-5)
    label(4)
    sprite('vr_trap_aircore', 10)	# 13-22
    sprite('vr_trap_aircore', 10)	# 23-32
    sprite('vr_trap_aircore', 10)	# 33-42
    sprite('vr_trap_aircore', 10)	# 43-52
    if (not SLOT_2):
        Unknown3006(-100)
    else:
        Unknown3001(255)
        Unknown3004(0)
    SLOT_57 = (SLOT_57 + 1)
    if (SLOT_57 >= 12):
        sendToLabel(5)
    loopRest()
    gotoLabel(4)
    label(5)
    Unknown3001(0)
    Unknown3004(-5)
    sprite('vr_trap_aircore', 10)	# 53-62
    Unknown3006(-300)
    SLOT_57 = (SLOT_57 + 1)
    if (SLOT_57 >= 17):
        sendToLabel(580)
    loopRest()
    gotoLabel(5)
    label(580)
    sprite('null', 1)	# 63-63
    SLOT_51 = 0
    GFX_1('naef_atrapend_04', 103)
    GFX_0('TrapAntiAirKowareEff', 103)
    loopRest()
    ExitState()
    label(14)
    sprite('null', 1)	# 64-64
    GFX_0('TrapAntiAir', 103)
    if SLOT_55:
        Unknown36(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown35()
    Unknown23090(25)
    ExitState()
    label(100)
    sprite('vr_trap_seed', 12)	# 65-76
    physicsYImpulse(-4000)
    physicsXImpulse(571)
    Unknown23022(1)
    GFX_2('naef_trap_seed')
    Unknown3001(200)
    Unknown3004(-5)
    loopRest()
    Unknown1019(2200)
    YAccel(2200)
    Unknown3004(-20)
    label(0)
    sprite('vr_trap_seed', 1)	# 77-77
    loopRest()
    gotoLabel(0)
    label(3)
    sprite('vr_trap_landcore', 2)	# 78-79
    SLOT_54 = 1
    Unknown3032()
    GFX_1('naef_trapstart_03', 103)
    GFX_1('naef_trapdetection_b', 103)
    if (SLOT_95 == 0):
        Unknown4003('6e6165665f7472617069636f6e32705f67726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    elif (SLOT_95 == 2):
        Unknown4003('6e6165665f7472617069636f6e32705f67726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    else:
        Unknown4003('6e6165665f7472617069636f6e5f67726f756e642e44494700000000000000006e6165665f7472617069636f6e5f67726f756e645f303030302e6d6d6f740000')
        Unknown4015()
    GFX_2('naef_trapjizoku_07')
    teleportRelativeY(0)
    Unknown1084(1)
    GFX_0('vr_trap_landcore_damy', -1)
    sprite('vr_trap_landcore', 10)	# 80-89
    Unknown3004(-5)
    label(8)
    sprite('vr_trap_landcore', 10)	# 90-99
    sprite('vr_trap_landcore', 10)	# 100-109
    sprite('vr_trap_landcore', 10)	# 110-119
    sprite('vr_trap_landcore', 10)	# 120-129
    if (not SLOT_2):
        Unknown3006(-100)
    else:
        Unknown3001(255)
        Unknown3004(0)
    SLOT_58 = (SLOT_58 + 1)
    if (SLOT_58 >= 12):
        sendToLabel(9)
    loopRest()
    gotoLabel(8)
    label(9)
    Unknown3001(0)
    Unknown3004(-5)
    sprite('vr_trap_aircore', 10)	# 130-139
    Unknown3006(-300)
    SLOT_58 = (SLOT_58 + 1)
    if (SLOT_58 >= 17):
        sendToLabel(581)
    loopRest()
    gotoLabel(9)
    label(581)
    sprite('null', 1)	# 140-140
    SLOT_51 = 0
    GFX_1('naef_trapend_05', 103)
    GFX_0('TrapAntiLandKowareEff', 103)
    loopRest()
    ExitState()
    label(141)
    sprite('null', 1)	# 141-141
    GFX_0('TrapAntiLand', 103)
    if SLOT_56:
        Unknown36(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown35()
    Unknown23090(25)

@State
def TrapAntiLand():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        AttackP1(80)
        AttackP2(85)
        Hitstop(4)
        blockstun(11)
        AirPushbackY(22000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11001(0, 8, 8)
        ChipDamagePct(20)
        Unknown3038(1)
    sprite('vr_trap_landexp', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    GFX_2('naef_traphitg_sub')
    Unknown3001(255)
    Unknown23022(1)
    sprite('vr_trap_landexp', 3)	# 3-5	 **attackbox here**
    RefreshMultihit()
    SFX_3('bomb_m')
    sprite('vr_trap_landexp', 3)	# 6-8	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('vr_trap_landexp', 30)	# 9-38	 **attackbox here**
    Unknown2001()

@State
def TrapAntiLandKowareEff():
    sprite('vr_trap_landexp', 30)	# 1-30	 **attackbox here**
    GFX_2('naef_trap_core')
    Unknown3038(1)
    Unknown3001(255)
    Unknown3004(-20)
    Unknown1059(100)

@State
def TrapAntiAir():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        AttackP1(80)
        AttackP2(85)
        Hitstop(1)
        blockstun(11)
        AirPushbackY(22000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11001(0, 8, 8)
        ChipDamagePct(20)
        Unknown3038(1)
    sprite('vr_trap_airexp', 5)	# 1-5	 **attackbox here**
    GFX_2('naef_trapexplosion_05')
    Unknown3001(255)
    DisableAttackRestOfMove()
    Unknown23022(1)
    sprite('vr_trap_airexp', 3)	# 6-8	 **attackbox here**
    RefreshMultihit()
    SFX_3('bomb_m')
    sprite('vr_trap_airexp', 3)	# 9-11	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('vr_trap_airexp', 30)	# 12-41	 **attackbox here**
    Unknown2001()

@State
def TrapAntiAirKowareEff():
    sprite('vr_trap_airexp', 30)	# 1-30	 **attackbox here**
    GFX_2('naef_trap_core_aa')
    Unknown3038(1)
    Unknown3001(255)
    Unknown3004(-20)
    Unknown1059(100)

@State
def suef_410():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4007(2)
        Unknown1007(145000)
        teleportRelativeX(-10000)

        def upon_30():
            Unknown4007(0)
    label(0)
    sprite('null', 3)	# 1-3
    GFX_0('suef_410_body', 100)
    gotoLabel(0)

@State
def suef_410_body():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4007(2)
        GFX_2('suef_410')
    sprite('null', 30)	# 1-30

@State
def suef_410_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
    label(0)
    sprite('null', 6)	# 1-6
    GFX_1('suef_410_add', 100)
    gotoLabel(0)

@State
def suef_410_zapper():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown2054(1)
        Unknown4007(2)
    label(0)
    sprite('null', 6)	# 1-6
    GFX_0('suef_410_slash', 100)
    gotoLabel(0)

@State
def suef_410_slash():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2054(1)
        Unknown4003('737565665f3431302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1096(1800)
        Unknown3001(255)
        Unknown3004(-8)
        Unknown1077(0, 360000)
        Unknown1007(40000)
        teleportRelativeX(30000)
    sprite('null', 15)	# 1-15

@State
def ImpactReversal():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        AirUntechableTime(60)
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(40000)
        Unknown3033()
        Unknown2054(1)
        Unknown30065(100)
        Unknown4007(3)
        HitAirUnblockable(4)
        Unknown11044(1)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000001000000000000000000000000000000')
    sprite('vr_impact', 4)	# 1-4	 **attackbox here**
    GFX_0('BarrierBrake', 100)
    RefreshMultihit()
    SFX_3('ice_break_fast')
    sprite('vr_impact', 20)	# 5-24	 **attackbox here**
    Unknown2001()

@State
def ImpactReversal_CA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        AirUntechableTime(60)
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(40000)
        Unknown3033()
        Unknown2054(1)
        Unknown30065(100)
        Unknown4007(3)
        HitAirUnblockable(4)
        Unknown11044(1)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
    sprite('vr_impact', 4)	# 1-4	 **attackbox here**
    GFX_0('BarrierBrake', 100)
    SFX_3('ice_break_fast')
    sprite('vr_impact', 20)	# 5-24	 **attackbox here**
    Unknown2001()

@State
def DanganReversal():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        Hitstop(0)
        ProjectileDurabilityLvl(3)
        PushbackX(40000)
        AirUntechableTime(32)
        AirPushbackY(20000)
        AirPushbackX(30000)
        YImpluseBeforeWallbounce(2000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown9178(1)
        AirHitstunAfterWallbounce(60)
        Unknown30065(100)
        Unknown11044(1)
        Unknown3032()
        Unknown4003('6e6165665f3430305f666c797368656c6430312e4449470000000000000000006e6165665f3430305f666c797368656c6430315f303030302e6d6d6f74000000')
        Unknown4015()
        Unknown4007(2)
        physicsXImpulse(70000)
        HitAirUnblockable(4)
    sprite('vr_dangan_a', 300)	# 1-300	 **attackbox here**
    Unknown4061(1)
    Unknown23067('suef_danganaura_00')
    GFX_1('naef_401gunfire', 0)
    GFX_0('FlyBarrierDandou', 1)
    GFX_0('FlyBarrierBrake', 100)
    RefreshMultihit()
    SFX_3('ice_break_fast')

@State
def BarrierJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6e6165665f3430305f7368656c6430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4011(2)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 3012):
                sendToLabel(1)
    sprite('null', 20)	# 1-20
    Unknown3004(26)
    GFX_0('BarrierYugamiLoop', 100)
    sprite('null', 32767)	# 21-32787
    label(1)
    sprite('null', 10)	# 32788-32797
    Unknown3004(-26)

@State
def BarrierYugamiLoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(0)
    label(1)
    sprite('null', 15)	# 1-15
    GFX_0('BarrierYugami', 100)
    sprite('null', 15)	# 16-30
    GFX_0('BarrierYugami', 100)
    gotoLabel(1)

@State
def BarrierYugami():
    sprite('vr_na400_yugami', 1)	# 1-1
    Unknown4007(2)
    Unknown4010(2)
    Unknown3032()
    Unknown3057(1)
    Unknown3058(14000)
    sprite('keep', 20)	# 2-21
    Unknown1059(100)
    Unknown1067(200)
    Unknown3004(-13)
    loopRest()

@State
def FlyBarrierBrake():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4015()
    sprite('null', 5)	# 1-5
    sprite('null', 5)	# 6-10
    GFX_1('suef_sheldbrake_05', 100)
    Unknown1099(50)
    sprite('null', 10)	# 11-20
    Unknown3004(-26)

@State
def FlyBarrierDandou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(1)
    sprite('null', 3)	# 1-3
    GFX_1('suef_sheldatk_03', 100)
    gotoLabel(1)

@State
def DanganUltimate():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        ProjectileDurabilityLvl(1)
        Damage(800)
        AttackP1(80)
        AttackP2(90)
        AirUntechableTime(80)
        Hitstop(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        AirPushbackX(1000)
        YImpluseBeforeWallbounce(1000)
        Unknown11001(11, 11, 11)
        physicsXImpulse(130000)
        Unknown4061(2)

        def upon_11():
            Unknown13(25)
        Unknown23067('naef_433dandoA')
        MinimumDamagePct(10)
        Unknown30065(0)
    sprite('vr_dangan_d_big', 1)	# 1-1	 **attackbox here**
    GFX_1('naef_401gunfireEX', 0)
    RefreshMultihit()
    SFX_3('na003')
    sprite('vr_dangan_d', 300)	# 2-301	 **attackbox here**

@State
def Zanzoh_kick():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown1096(1100)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_na433_00', 30)	# 1-30
    GFX_1('naef_407smoke', 100)

@State
def Kick_line():

    def upon_IMMEDIATE():
        Unknown4003('6e6165665f3433336b69636b2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('naef_433kicksub')
        Unknown4009(2)
        Unknown2054(1)
        Unknown4015()
        Unknown1096(1100)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(50)
    sprite('null', 7)	# 11-17
    Unknown3004(-40)

@State
def DanganKakushiA():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(700)
        MinimumDamagePct(17)
        AttackP2(96)
        Unknown23182(2)
        Hitstop(0)
        PushbackX(1000)
        AirUntechableTime(70)
        Hitstop(1)
        Unknown9021(1)
        AirPushbackX(20000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(2000)
        Unknown11068(1)
        Unknown11001(0, 11, 11)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown30056('c0f2fcff6400000000000000')
        Unknown9310(1)
        Unknown2054(1)
        Unknown4061(2)
        Unknown1072(20000)
        Unknown4055(0)
        Unknown4045('6e6165665f34303167756e66697265420000000000000000000000000000000000000000')
        Unknown1110(100000, 0)

        def upon_43():
            if (SLOT_48 == 3013):
                Unknown1072(20000)
                Unknown4055(0)
                Unknown4045('6e6165665f34303167756e66697265420000000000000000000000000000000000000000')
                Unknown1110(100000, 0)
                AirUntechableTime(150)
                YImpluseBeforeWallbounce(1100)
                AirPushbackY(8000)
                Unknown9310(60)

        def upon_LANDING():
            Unknown13(25)
        Unknown23067('naef_401dandoB')
    sprite('vr_dangan_b', 300)	# 1-300	 **attackbox here**
    GFX_1('naef_401gunfireB', 0)
    RefreshMultihit()

@State
def DanganKakushiB():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(4000)
        MinimumDamagePct(25)
        AttackP2(60)
        Hitstop(12)
        PushbackX(1000)
        AirUntechableTime(30)
        AirPushbackY(-100000)
        AirPushbackX(100000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9202(10)
        Unknown9310(10)
        Unknown11110(97)
        Unknown23078(1)
        Unknown4061(2)
        Unknown1072(20000)
        Unknown4055(0)
        Unknown4045('6e6165665f34303167756e66697265430000000000000000000000000000000000000000')
        Unknown1110(130000, 0)

        def upon_LANDING():
            Unknown13(25)

        def upon_12():
            ScreenShake(80000, 0)
            Unknown48('1900000002000000330000001b000000020000005f000000')
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 == 1):
                Unknown23029(3, 9001, 0)
            if (SLOT_51 == 2):
                Unknown23029(3, 9002, 0)
            if (SLOT_51 == 3):
                Unknown23029(3, 9003, 0)
            if (SLOT_51 == 4):
                Unknown23029(3, 9004, 0)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown21015('53656372657447756e4f440000000000000000000000000000000000000000008913000000000000')
        Unknown23067('naef_401dandoC')
    sprite('vr_dangan_c', 300)	# 1-300	 **attackbox here**
    RefreshMultihit()

@State
def Hamaon_search():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown3032()
        Unknown4003('6e6165665f34333268616d615f7365617263682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('suef_431hama_search')
        Unknown4015()
        teleportRelativeY(0)
        teleportRelativeX(150000)
        Unknown3001(0)
        Unknown4011(3)

        def upon_43():
            if (SLOT_48 == 3014):
                Unknown4011(0)
    sprite('null', 12)	# 1-12
    Unknown3004(25)
    SFX_3('magiccircle_a')
    sprite('null', 18)	# 13-30
    GFX_0('Hamaon', 100)
    sprite('null', 10)	# 31-40
    Unknown3004(-26)

@State
def Hamaon():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(3)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        Unknown9021(1)
        AirPushbackX(0)
        AirPushbackY(4000)
        YImpluseBeforeWallbounce(200)
        PushbackX(0)
        Unknown11064(1)
        Unknown30055('000000003200000014000000')
        Unknown30056('c0d401003200000000000000')
        Unknown11070(1)
        teleportRelativeY(0)
        Unknown1064(1500)
        Unknown4051(0)
        Unknown4011(3)
        Unknown3032()
        Unknown4003('6e6165665f34333268616d612e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('suef_431hama')
        Unknown23015(2)
        Unknown4015()

        def upon_78():
            SLOT_55 = 1
            Unknown48('19000000020000003300000016000000020000005f000000')
            if (SLOT_51 == 0):
                Unknown48('19000000020000003400000003000000020000003f000000')
                if (SLOT_52 == 2):
                    SLOT_53 = 1
            elif (SLOT_51 == 1):
                Unknown48('190000000200000034000000030000000200000040000000')
                if (SLOT_52 == 2):
                    SLOT_53 = 1
            elif (SLOT_51 == 2):
                Unknown48('190000000200000034000000030000000200000041000000')
                if (SLOT_52 == 2):
                    SLOT_53 = 1
            elif (SLOT_51 == 3):
                Unknown48('190000000200000034000000030000000200000042000000')
                if (SLOT_52 == 2):
                    SLOT_53 = 1
            if SLOT_53:
                Unknown23083(1)
                Unknown11069('Hamaon')
                SLOT_9 = 1

        def upon_82():
            SLOT_56 = 1
    sprite('vr_dmy_hamaon', 5)	# 1-5
    RefreshMultihit()
    SFX_3('na010')
    sprite('vr_dmy_hamaon', 5)	# 6-10
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 11-15
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 16-20
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 21-25
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 26-30
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 31-35
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 36-40
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 41-45
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 46-50
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 51-55
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 56-60
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 61-65
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 5)	# 66-70
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 4)	# 71-74
    RefreshMultihit()
    sprite('vr_dmy_hamaon', 1)	# 75-75
    if SLOT_56:
        GFX_0('MissMarkHsub', 100)
    loopRest()
    clearUponHandler(78)
    if SLOT_55:
        _gotolabel(1)
    sprite('vr_dmy_hamaon', 24)	# 76-99
    Unknown3004(-10)
    Unknown2001()
    loopRest()
    ExitState()
    label(1)
    sprite('vr_dmy_hamaon_big', 5)	# 100-104
    RefreshMultihit()

    def upon_78():
        Unknown21015('48616d616f6e5f73656172636800000000000000000000000000000000000000c60b000000000000')
        Unknown4011(0)
        SLOT_53 = 0
        Unknown48('19000000020000003300000016000000020000005f000000')
        if (SLOT_51 == 0):
            Unknown48('19000000020000003400000003000000020000003f000000')
            if (SLOT_52 == 2):
                Unknown11069('HamaonKill1P')
                GFX_0('HamaonKill', 103)
                Unknown23029(1, 9011, 0)
                SLOT_53 = 1
        elif (SLOT_51 == 1):
            Unknown48('190000000200000034000000030000000200000040000000')
            if (SLOT_52 == 2):
                Unknown11069('HamaonKill2P')
                GFX_0('HamaonKill', 103)
                Unknown23029(1, 9012, 0)
                SLOT_53 = 1
        elif (SLOT_51 == 2):
            Unknown48('190000000200000034000000030000000200000041000000')
            if (SLOT_52 == 2):
                Unknown11069('HamaonKill3P')
                GFX_0('HamaonKill', 103)
                Unknown23029(1, 9013, 0)
                SLOT_53 = 1
        elif (SLOT_51 == 3):
            Unknown48('190000000200000034000000030000000200000042000000')
            if (SLOT_52 == 2):
                Unknown11069('HamaonKill4P')
                GFX_0('HamaonKill', 103)
                Unknown23029(1, 9014, 0)
                SLOT_53 = 1
        if SLOT_53:
            AirPushbackX(0)
            AirPushbackY(1)
            YImpluseBeforeWallbounce(0)
            hitstun(350)
            AirUntechableTime(350)
            Unknown30048(1)
            Unknown11062(1)
        else:
            AirPushbackX(0)
            AirPushbackY(30000)
            YImpluseBeforeWallbounce(2000)
            AirHitstunAnimation(9)
            GroundedHitstunAnimation(9)
            GFX_0('MissMarkH', 100)
            Unknown11001(0, 19, 19)
    sprite('vr_dmy_hamaon', 10)	# 105-114
    Unknown2001()

@State
def HamaonKill():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Unknown11057(1500)
        Unknown9016(1)
        Damage(99999)
        MinimumDamagePct(100)
        Unknown11106(0)
        AirPushbackX(0)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(2000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown3038(1)
        Unknown23151(22, 103)
        Unknown4007(22)
        Unknown20000(1)
        Unknown30048(1)
        Unknown11069('HamaonKill')
        Unknown11042(1)

        def upon_12():
            SLOT_9 = 0
            Unknown36(22)
            Unknown3004(0)
            Unknown3001(255)
            Unknown35()
        Unknown23083(1)
        SLOT_6 = 0

        def upon_43():
            if (SLOT_48 == 9011):
                Unknown30070('48616d616f6e4b696c6c31500000000000000000000000000000000000000000')
            if (SLOT_48 == 9012):
                Unknown30070('48616d616f6e4b696c6c32500000000000000000000000000000000000000000')
            if (SLOT_48 == 9013):
                Unknown30070('48616d616f6e4b696c6c33500000000000000000000000000000000000000000')
            if (SLOT_48 == 9014):
                Unknown30070('48616d616f6e4b696c6c34500000000000000000000000000000000000000000')
    sprite('vr_dmy_hamaon', 1)	# 1-1
    StartMultihit()
    sprite('vr_dmy_hamaon', 3)	# 2-4
    StartMultihit()
    Unknown36(22)
    Unknown3032()
    Unknown3004(-4)
    Unknown35()
    sprite('vr_dmy_hamaon', 10)	# 5-14
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 15-24
    StartMultihit()
    SFX_3('cut_l')
    sprite('vr_dmy_hamaon', 10)	# 25-34
    StartMultihit()
    GFX_0('HamaonKillIcon', 100)
    sprite('vr_dmy_hamaon', 10)	# 35-44
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 45-54
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 55-64
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 65-74
    StartMultihit()
    sprite('vr_dmy_hamaon', 1)	# 75-75
    ScreenShake(300000, 100000)
    RefreshMultihit()
    Unknown11023(1)
    Unknown23008(0, 0)

@State
def HamaonKillIcon():

    def upon_IMMEDIATE():
        GFX_2('suef_hamadeath_05')
        Unknown4007(2)
        Unknown2007()
    sprite('null', 60)	# 1-60

@State
def MissMarkH():

    def upon_IMMEDIATE():
        Unknown2007()

        def upon_CLEAR_OR_EXIT():
            Unknown23151(22, 103)
            Unknown1007(90000)
    sprite('null', 20)	# 1-20
    GFX_2('naef_miss')

@State
def MissMarkHsub():

    def upon_IMMEDIATE():
        Unknown2007()

        def upon_CLEAR_OR_EXIT():
            Unknown23151(23, 103)
            Unknown1007(90000)
    sprite('null', 20)	# 1-20
    GFX_2('naef_miss')

@State
def MissMarkM():

    def upon_IMMEDIATE():
        Unknown2007()

        def upon_CLEAR_OR_EXIT():
            Unknown23151(22, 103)
            Unknown1007(60000)
    sprite('null', 20)	# 1-20
    sprite('null', 40)	# 21-60
    GFX_2('naef_miss')

@State
def MissMarkMprt():

    def upon_IMMEDIATE():
        Unknown2007()

        def upon_CLEAR_OR_EXIT():
            Unknown23151(23, 103)
            Unknown1007(60000)
    sprite('null', 20)	# 1-20
    sprite('null', 40)	# 21-60
    GFX_2('naef_miss')

@State
def Mudoon_search():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('6e6165665f3433326d75646f5f7365617263682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('suef_431mudo_search')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        teleportRelativeX(130000)
        Unknown1007(160000)

        def upon_43():
            if (SLOT_48 == 3015):
                Unknown4011(0)
    sprite('null', 30)	# 1-30
    Unknown3004(25)
    SFX_3('magiccircle_b')
    sprite('null', 10)	# 31-40
    Unknown3004(-26)

@State
def Mudoon():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(0)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11064(1)
        Unknown4011(3)
        Unknown4051(0)

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 100):
                clearUponHandler(3)
                SLOT_34 = 0
        Unknown2037(0)

        def upon_78():
            Unknown48('190000000200000033000000030000000200000006000000')
            if SLOT_51:
                Unknown2037(1)
            Unknown48('1900000002000000340000001600000002000000aa000000')
            if SLOT_52:
                Unknown2037(0)
            if SLOT_2:
                Unknown21015('556c74696d6174654b696c6c41697200000000000000000000000000000000008a13000000000000')
                Unknown21015('556c74696d6174654b696c6c4169724f440000000000000000000000000000008a13000000000000')
                AirPushbackX(0)
                AirPushbackY(1)
                YImpluseBeforeWallbounce(0)
                Unknown30056('d019fdff6400000000000000')
                AirUntechableTime(320)
                Unknown11069('MudoonKill')
                Unknown30048(1)
                Unknown23083(1)
                SLOT_9 = 1
                AirHitstunAnimation(9)
                GroundedHitstunAnimation(9)
                Unknown9362(0)
                Unknown11062(1)
            else:
                Unknown30056('d019fdff3200000000000000')
                AirPushbackX(150000)
                AirPushbackY(10000)
                YImpluseBeforeWallbounce(0)
                Unknown11001(0, 29, 29)
                Unknown9362(1)
                Unknown9364(66)
                AirHitstunAfterWallbounce(100)
                WallbounceReboundTime(10)
                AirHitstunAnimation(12)
                GroundedHitstunAnimation(12)
                GFX_0('MissMarkM', 100)
                SLOT_34 = 0
            SLOT_56 = 1
            Unknown21015('4d75646f6f6e5f73656172636800000000000000000000000000000000000000c70b000000000000')
            Unknown4011(0)
            SLOT_57 = SLOT_2

        def upon_82():
            Unknown30056('d019fdff3200000000000000')
            AirPushbackX(150000)
            AirPushbackY(10000)
            YImpluseBeforeWallbounce(0)
            Unknown11001(0, 29, 29)
            Unknown9362(1)
            Unknown9364(66)
            AirHitstunAfterWallbounce(100)
            WallbounceReboundTime(10)
            AirHitstunAnimation(12)
            GroundedHitstunAnimation(12)
            GFX_0('MissMarkMprt', 100)
            SLOT_34 = 0
        Unknown4003('6e6165665f3433326d75646f2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown3032()
        teleportRelativeX(110000)
        Unknown1007(160000)

        def upon_16():
            GFX_0('MudoBall', 100)
    sprite('vr_dmy_mudoon', 4)	# 1-4
    SFX_3('na011')
    sprite('vr_dmy_mudoon', 11)	# 5-15
    sprite('vr_dmy_mudoon2', 40)	# 16-55
    sprite('vr_dmy_mudoon2', 1)	# 56-56
    Unknown3004(-26)
    DisableAttackRestOfMove()
    clearUponHandler(16)
    sprite('vr_dmy_mudoon2', 10)	# 57-66
    if SLOT_56:
        if SLOT_57:
            GFX_0('MudoonKill', 100)
    loopRest()
    ExitState()

@State
def MudoBall():

    def upon_IMMEDIATE():
        Unknown2054(1)
        GFX_2('suef_432mudoball')
        physicsXImpulse(90000)
        Unknown1025(10000, -10000)
        Unknown1026(10000, -10000)
        Unknown1099(20)
        Unknown1011(50000, -50000)
        Unknown1010(25000, -25000)
    sprite('null', 6)	# 1-6
    Unknown1019(6)
    YAccel(6)
    Unknown1096(50)
    Unknown3001(50)
    Unknown3004(20)
    Unknown1099(150)
    sprite('null', 4)	# 7-10
    GFX_1('suef_432mudoball_sub', 100)
    Unknown1019(1000)
    YAccel(1000)
    Unknown1099(30)
    sprite('null', 4)	# 11-14
    GFX_1('suef_432mudoball_sub', 100)
    sprite('null', 4)	# 15-18
    GFX_1('suef_432mudoball_sub', 100)
    sprite('null', 4)	# 19-22
    GFX_1('suef_432mudoball_sub', 100)
    Unknown3001(180)
    Unknown3004(-20)
    Unknown1019(15)
    YAccel(15)
    sprite('null', 22)	# 23-44
    GFX_1('suef_432mudoball_sub', 100)

@State
def MudoonKillIcon():

    def upon_IMMEDIATE():
        GFX_2('suef_mudodeath_05')
        Unknown4007(2)
        Unknown2007()
    sprite('null', 60)	# 1-60

@State
def MudoonKill():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Unknown11057(1500)
        Unknown9016(1)
        Damage(99999)
        MinimumDamagePct(100)
        Unknown11106(0)
        AirPushbackX(70000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(2000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown3038(1)
        Unknown23151(22, 103)
        Unknown4007(22)
        Unknown20000(1)
        Unknown30048(1)
        Unknown11069('MudoonKill')
        Unknown11042(1)

        def upon_12():
            SLOT_9 = 0
            Unknown36(22)
            Unknown3004(0)
            Unknown3001(255)
            Unknown35()
        Unknown23083(1)
        SLOT_5 = 0
    sprite('vr_dmy_hamaon', 4)	# 1-4
    StartMultihit()
    Unknown36(22)
    Unknown3032()
    Unknown3004(-4)
    Unknown35()
    sprite('vr_dmy_hamaon', 10)	# 5-14
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 15-24
    StartMultihit()
    SFX_3('cut_l')
    sprite('vr_dmy_hamaon', 10)	# 25-34
    StartMultihit()
    GFX_0('MudoonKillIcon', 100)
    sprite('vr_dmy_hamaon', 10)	# 35-44
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 45-54
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 55-64
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 65-74
    StartMultihit()
    sprite('vr_dmy_hamaon', 10)	# 75-84
    ScreenShake(300000, 100000)
    RefreshMultihit()
    Unknown11023(1)
    Unknown23008(0, 0)

@State
def Ichigeki_RedRay():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown23151(22, 103)
    sprite('null', 20)	# 1-20
    GFX_2('naef_ichigekikakutei_05')
    sprite('null', 1)	# 21-21
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000001f25000000000000')

@State
def RotateGun():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(0)
        Unknown3029(1)
    sprite('vr_na450_rotategun_00', 2)	# 1-2
    physicsXImpulse(3000)
    physicsYImpulse(45000)
    sprite('vr_na450_rotategun_01', 2)	# 3-4
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)	# 5-6
    physicsXImpulse(1000)
    physicsYImpulse(7000)
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)	# 7-8
    sprite('vr_na450_rotategun_02', 2)	# 9-10
    physicsYImpulse(6000)
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)	# 11-12
    sprite('vr_na450_rotategun_02', 2)	# 13-14
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_00', 2)	# 15-16
    sprite('vr_na450_rotategun_01', 2)	# 17-18
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)	# 19-20
    sprite('vr_na450_rotategun_00', 2)	# 21-22
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)	# 23-24
    sprite('vr_na450_rotategun_02', 2)	# 25-26
    SFX_3('slash_rapier_fast')
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)	# 27-28
    physicsYImpulse(-27000)
    physicsXImpulse(2250)
    sprite('vr_na450_rotategun_00', 2)	# 29-30
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_01', 2)	# 31-32
    sprite('vr_na450_rotategun_02', 2)	# 33-34
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_00', 2)	# 35-36
    sprite('vr_na450_rotategun_01', 2)	# 37-38
    SFX_3('slash_rapier_fast')
    sprite('vr_na450_rotategun_02', 2)	# 39-40
    sprite('vr_na450_rotategun_00', 2)	# 41-42
    sprite('vr_na450_rotategun_02', 2)	# 43-44
    GFX_1('naef_guncatchi_03', 0)

@State
def ZanzohCircle():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(3)
    sprite('vr_su450_00', 2)	# 1-2
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_00', 2)	# 3-4
    GFX_1('suef_circlekidou_01', 1)
    sprite('vr_su450_01', 4)	# 5-8
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_02', 4)	# 9-12
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_03', 10)	# 13-22
    GFX_1('suef_circlekidou_01', 0)
    sprite('vr_su450_03', 10)	# 23-32
    Unknown3004(-26)

@Subroutine
def Ichigeki_MarkerSetting():
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 6
    Unknown48('010000000200000033000000190000000200000000000000')
    Unknown36(1)
    Unknown23032(-15)
    Unknown23033(70)
    Unknown35()
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 4
    Unknown48('010000000200000033000000190000000200000000000000')
    Unknown36(1)
    Unknown23032(115)
    Unknown23033(40)
    Unknown35()
    GFX_0('Ichigeki_Marker', 103)
    SLOT_0 = 3
    Unknown48('010000000200000033000000190000000200000000000000')
    Unknown36(1)
    Unknown23032(40)
    Unknown23033(-5)
    Unknown35()

@State
def Ichigeki_Marker():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown4010(3)
        Unknown2054(1)
        AttackLevel_(0)
        Damage(0)
        Hitstop(0)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(500)
        YImpluseBeforeWallbounce(20)
        AirUntechableTime(120)
        Unknown11001(20, 20, 20)
        Unknown11064(1)
        Unknown11032('e022020020ddfdffffffffffffffffff')
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_5():
            SLOT_13 = (SLOT_13 * (-1))

        def upon_78():
            clearUponHandler(43)
            sendToLabel(1)
            Unknown23144('1600000000000000670000000000000000000000000000000000000000000000f1ffffff000000000f000000')

        def upon_61():
            clearUponHandler(43)
            sendToLabel(0)

        def upon_44():
            clearUponHandler(43)
            sendToLabel(0)

        def upon_43():
            if (SLOT_48 == 9532):
                sendToLabel(0)
            if (SLOT_48 == 9531):
                sendToLabel(1)
        Unknown23026(100000)
        Unknown23067('suef_jizokutarget_02')
        DisableAttackRestOfMove()
    sprite('vr_su450_dmy', 1)	# 1-1	 **attackbox here**
    Unknown1096(800)
    sprite('vr_su450_dmy', 5)	# 2-6	 **attackbox here**
    Unknown3004(32)
    if (SLOT_23 < 110000):
        teleportRelativeY(110000)
    sprite('vr_su450_dmy', 5)	# 7-11	 **attackbox here**
    Unknown3004(-12)
    sprite('vr_su450_dmy', 2)	# 12-13	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    Unknown1099(160)
    sprite('vr_su450_dmy', 2)	# 14-15	 **attackbox here**
    Unknown1099(-20)
    sprite('vr_su450_dmy', 2)	# 16-17	 **attackbox here**
    Unknown1099(0)
    sprite('vr_su450_dmy', 10)	# 18-27	 **attackbox here**
    RefreshMultihit()
    sprite('vr_su450_dmy', 1)	# 28-28	 **attackbox here**
    sprite('vr_su450_dmy', 130)	# 29-158	 **attackbox here**
    if (SLOT_51 == 1):
        physicsXImpulse(-525)
        physicsYImpulse(-525)
    if (SLOT_51 == 2):
        physicsXImpulse(0)
        physicsYImpulse(-700)
    if (SLOT_51 == 3):
        physicsXImpulse(525)
        physicsYImpulse(-525)
    if (SLOT_51 == 4):
        physicsXImpulse(-700)
        physicsYImpulse(0)
    if (SLOT_51 == 6):
        physicsXImpulse(700)
        physicsYImpulse(0)
    if (SLOT_51 == 7):
        physicsXImpulse(-525)
        physicsYImpulse(525)
    if (SLOT_51 == 8):
        physicsXImpulse(0)
        physicsYImpulse(700)
    if (SLOT_51 == 9):
        physicsXImpulse(525)
        physicsYImpulse(525)
    sprite('vr_su450_dmy', 50)	# 159-208	 **attackbox here**
    Unknown2001()
    sprite('vr_su450_dmy', 16)	# 209-224	 **attackbox here**
    Unknown21015('504e415f506572736f6e614963686967656b69000000000000000000000000002825000000000000')
    Unknown3004(-16)
    Unknown1099(20)
    Unknown1084(1)
    Unknown2001()
    sprite('null', 32767)	# 225-32991
    loopRest()
    label(1)
    sprite('null', 32767)	# 32992-65758
    clearUponHandler(43)
    Unknown21015('504e415f506572736f6e614963686967656b69000000000000000000000000002725000000000000')
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000001d25000000000000')
    Unknown21015('4963686967656b695f4d61726b657200000000000000000000000000000000003b25000000000000')

    def upon_CLEAR_OR_EXIT():
        Unknown21015('4963686967656b695f4d61726b657200000000000000000000000000000000003b25000000000000')
    label(0)
    sprite('null', 16)	# 65759-65774
    Unknown21015('504e415f506572736f6e614963686967656b69000000000000000000000000002825000000000000')
    Unknown3004(-16)
    Unknown1099(20)
    Unknown1084(1)
    Unknown2001()

@State
def Ichigeki_Scope():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2007()
        Unknown23015(1)
        Unknown2019(100)
        Unknown23180(1)
        Unknown6001(1)
        Unknown1096(1800)
        Unknown1000(-640000)
        teleportRelativeY(-380000)
        Unknown3001(255)
        Unknown23013(0)
        Unknown2053(0)
        Unknown2034(0)

        def upon_43():
            if (SLOT_48 == 9533):
                sendToLabel(0)
            if (SLOT_48 == 9534):
                sendToLabel(1)
    sprite('vr_scope', 32767)	# 1-32767
    label(0)
    sprite('vr_scope', 10)	# 32768-32777
    Unknown3004(-26)
    label(1)
    sprite('vr_scope', 5)	# 32778-32782
    Unknown3004(-51)
    Unknown1099(800)

@State
def Ichigeki_Scope2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2007()
        Unknown23015(3)
        Unknown23180(1)
        Unknown6001(1)
        Unknown1096(1800)
        Unknown1000(-640000)
        teleportRelativeY(-380000)
        Unknown1074(4000)
        Unknown23013(0)
        Unknown2053(0)
        Unknown2034(0)

        def upon_43():
            if (SLOT_48 == 9533):
                sendToLabel(0)
    sprite('vr_scope2', 32767)	# 1-32767
    label(0)
    sprite('vr_scope2', 10)	# 32768-32777
    Unknown3004(-26)

@State
def Ichigeki_Scope3():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2007()
        Unknown23015(3)
        Unknown23180(1)
        Unknown6001(1)
        Unknown1096(1800)
        Unknown1000(-640000)
        teleportRelativeY(-380000)
        Unknown23013(0)
        Unknown2053(0)
        Unknown2034(0)

        def upon_43():
            if (SLOT_48 == 9533):
                sendToLabel(0)
    label(1)
    sprite('null', 20)	# 1-20
    GFX_0('Ichigeki_Scope4', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 5)	# 21-25
    Unknown3004(-51)

@State
def Ichigeki_Scope4():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2007()
        Unknown23015(3)
        Unknown23180(1)
        Unknown6001(1)
        Unknown1096(1800)
        Unknown1000(-640000)
        teleportRelativeY(-380000)
        Unknown23013(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('vr_scope3', 10)	# 1-10
    Unknown1099(-50)
    Unknown3004(-9)
    sprite('vr_scope3', 20)	# 11-30

@State
def IchigekiCamera():

    def upon_IMMEDIATE():
        Unknown3029(1)
        Unknown3032()
        Unknown3001(80)
        Unknown23013(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 9521):
                sendToLabel(0)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20002(0)
            Unknown20003(0)
    label(1)
    sprite('dmy_camera', 32767)	# 1-32767
    Unknown20003(1)
    Unknown23151(22, 103)
    Unknown20001(1)
    Unknown20000(1)
    Unknown20009(900)

    def upon_CLEAR_OR_EXIT():
        Unknown23151(22, 103)
        Unknown1007(-20000)
    label(0)
    sprite('keep', 1)	# 32768-32768
    loopRest()

@State
def IchigekiCutin():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown6001(1)
        Unknown3032()
        Unknown6001(1)
        Unknown1001(640000)
        teleportRelativeX(250000)
        teleportRelativeY(-384000)
        Unknown1007(500000)
        Unknown3001(0)
        Unknown1096(3000)
    sprite('ichigeki0', 10)	# 1-10	 **attackbox here**
    Unknown3004(8)
    physicsXImpulse(40000)
    Unknown1099(-100)
    sprite('ichigeki0', 10)	# 11-20	 **attackbox here**
    physicsXImpulse(200)
    sprite('ichigeki0', 40)	# 21-60	 **attackbox here**
    Unknown1099(0)
    Unknown1096(900)
    sprite('ichigeki0', 1)	# 61-61	 **attackbox here**
    SFX_3('na000')
    sprite('ichigeki0', 1)	# 62-62	 **attackbox here**
    SFX_3('na000')
    sprite('ichigeki0', 1)	# 63-63	 **attackbox here**
    SFX_3('na000')
    sprite('ichigeki0', 2)	# 64-65	 **attackbox here**
    SFX_3('na000')
    sprite('ichigeki0', 6)	# 66-71	 **attackbox here**
    sprite('ichigeki0', 5)	# 72-76	 **attackbox here**
    Unknown1099(300)
    physicsXImpulse(250000)
    physicsYImpulse(130000)
    Unknown3004(-52)

@State
def IchigekiTame_Atk():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Hitstop(120)
        Damage(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11050('010000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        HitLow(99)
        HitOverhead(99)
        HitAirUnblockable(99)
        Unknown23015(4)
    sprite('dmy_atk00', 4)	# 1-4
    RefreshMultihit()
    GFX_0('naef_ichigehit_obj', 100)
    sprite('dmy_atk00', 120)	# 5-124

@State
def naef_ichigehit_obj():

    def upon_IMMEDIATE():
        GFX_2('naef_ichigehit_la')
        Unknown23151(22, 103)
    sprite('null', 124)	# 1-124

@State
def Ichigeki_shot():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown4054(4)
        teleportRelativeY(260000)
        Unknown1000(-400000)
        Unknown4003('737565665f3435305f73686f7430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(4)
        Unknown23151(22, 103)
    sprite('vr_su450_dandou', 10)	# 1-10
    physicsXImpulse(200000)
    Unknown23067('naef_ichigtekishot_07')
    SFX_3('na003')
    sprite('vr_su450_dandou', 20)	# 11-30
    physicsXImpulse(50000)
    sprite('vr_su450_dandou', 10)	# 31-40
    Unknown3004(-26)

@State
def IchigekiExplosion():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown4054(1)
        Unknown4003('737565665f3435305f626f6d30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1096(300)
        Unknown3001(0)
        Unknown3032()
        GFX_2('naef_ichigekihit_09')
        Unknown23151(22, 103)
    sprite('null', 5)	# 1-5
    Unknown3004(51)
    Unknown1099(30)
    sprite('null', 2)	# 6-7
    Unknown1096(600)
    Unknown1099(0)
    sprite('null', 2)	# 8-9
    Unknown1096(1200)
    sprite('null', 4)	# 10-13
    Unknown1096(2400)
    sprite('null', 4)	# 14-17
    Unknown1096(2600)
    sprite('null', 4)	# 18-21
    Unknown1096(2800)
    sprite('null', 30)	# 22-51
    Unknown1096(3000)

@State
def IchigekiBlack():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(2)
        Unknown2019(500)
        Unknown6001(1)
        Unknown2007()
        Unknown1000(-500000)
        teleportRelativeY(-384000)
        Unknown3026(-16777216)
        Unknown3032()
        Unknown23013(0)
    sprite('vr_na450_white', 120)	# 1-120

@State
def Ichigekiwhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(2)
        Unknown23015(1)
        Unknown6001(1)
        Unknown2007()
        Unknown1000(-500000)
        teleportRelativeY(-384000)
        Unknown3032()
        Unknown3001(0)
        Unknown23013(0)
    sprite('vr_na450_white', 20)	# 1-20
    Unknown3004(26)
    sprite('vr_na450_white', 140)	# 21-160
    sprite('vr_na450_white', 20)	# 161-180
    Unknown3004(-17)

@State
def Ichigeki_Atk():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Hitstop(60)
        Damage(100000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11064(3)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        HitLow(99)
        HitOverhead(99)
        HitAirUnblockable(99)
        Unknown1086(22)
        Unknown1007(55000)
    sprite('dmy_atk00', 4)	# 1-4
    RefreshMultihit()
    sprite('null', 1)	# 5-5

@State
def WinYakkyo():

    def upon_IMMEDIATE():

        def upon_5():
            YAccel(-45)
            Unknown1019(45)

        def upon_LANDING():
            SFX_3('na006')
        Unknown4061(2)
    sprite('vr_trap_yakkyo', 50)	# 1-50
    Unknown1025(-1750, -3000)
    Unknown1026(1125, 1625)
    Unknown1078(-5000, -8000)
    setGravity(900)
    sprite('vr_trap_yakkyo', 20)	# 51-70
    Unknown3032()
    Unknown3004(-20)

@State
def PersonaMatchWin2():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23022(1)
        Unknown23023()
        Unknown23184('0300000064000000c0f2fcff60ea000000000000000000000000000000000000')
        callSubroutine('PNA_CheckWarp')
    sprite('su611_00', 4)	# 1-4
    Unknown2019(-500)
    sprite('su611_01', 4)	# 5-8
    sprite('su611_02', 4)	# 9-12
    sprite('su611_03', 4)	# 13-16
    sprite('su611_04', 4)	# 17-20
    Unknown2019(500)
    sprite('su611_05', 4)	# 21-24
    sprite('su611_06', 4)	# 25-28
    sprite('su611_07', 4)	# 29-32
    sprite('su611_08', 4)	# 33-36
    Unknown2019(-500)
    sprite('su611_09', 4)	# 37-40
    sprite('su611_10', 60)	# 41-100
    physicsXImpulse(40000)
    physicsYImpulse(40000)
    sprite('su611_11', 5)	# 101-105
    SLOT_52 = SLOT_23
    Unknown1086(3)
    SLOT_23 = SLOT_52
    teleportRelativeX(-120000)
    teleportRelativeY(500000)
    physicsXImpulse(0)
    physicsYImpulse(-20000)
    sprite('su611_12', 5)	# 106-110
    sprite('su611_11', 5)	# 111-115
    sprite('su611_13', 3)	# 116-118
    YAccel(50)
    sprite('su611_14', 3)	# 119-121
    YAccel(50)
    sprite('su611_15', 5)	# 122-126
    YAccel(0)
    sprite('su611_16', 5)	# 127-131
    sprite('su611_17', 5)	# 132-136
    label(0)
    sprite('su611_15', 5)	# 137-141
    sprite('su611_16', 5)	# 142-146
    sprite('su611_17', 5)	# 147-151
    loopRest()
    gotoLabel(0)
    enterState('PersonaDeleteAndIdling')

@State
def P4U_Cutin_Parent():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)	# 1-1
    GFX_0('P4U_Cutin_Face', 100)

@State
def P4U_Cutin_Face():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown2054(1)
        Unknown13044(0)
        Unknown6001(1)
        Unknown1000(-650000)
        teleportRelativeY(-292000)
        Unknown1096(1350)
        Unknown2037(0)
        Unknown3001(0)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 == 2):
                Unknown1007(15000)
                Unknown3001(150)
            if (SLOT_2 == 3):
                Unknown1007(-30000)
                Unknown3001(180)
            if (SLOT_2 == 4):
                Unknown1007(25000)
                Unknown3001(210)
            if (SLOT_2 == 5):
                Unknown1007(-20000)
                Unknown3001(255)
            if (SLOT_2 == 6):
                Unknown1007(10000)
            Unknown2038(1)
    sprite('vr_99p4u_face00', 45)	# 1-45
    SFX_0('spsys_over_power')
    SFX_0('spsys_over_power')
    if SLOT_168:
        GFX_0('P4U_ka_NotJPN', 100)
    else:
        GFX_0('P4U_ka_JPN', 100)
    sprite('vr_99p4u_face00', 1)	# 46-46
    Unknown3001(180)
    sprite('vr_99p4u_face00', 1)	# 47-47
    Unknown3001(120)
    sprite('vr_99p4u_face00', 1)	# 48-48
    Unknown3001(60)

@State
def P4U_ka_JPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi', 1)	# 1-1
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi', 1)	# 2-2
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi', 1)	# 3-3
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi', 1)	# 4-4
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi', 1)	# 5-5
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi', 1)	# 6-6
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi', 1)	# 7-7
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi', 38)	# 8-45
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi', 1)	# 46-46
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi', 1)	# 47-47
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi', 1)	# 48-48
    Unknown3001(60)
    Unknown1096(100)

@State
def P4U_ka_NotJPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 1-1
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 2-2
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 3-3
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 4-4
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 5-5
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 6-6
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 7-7
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi_notjpn', 38)	# 8-45
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 46-46
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 47-47
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi_notjpn', 1)	# 48-48
    Unknown3001(60)
    Unknown1096(100)