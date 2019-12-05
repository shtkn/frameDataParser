@Subroutine
def ItemIconUpDate():
    if (SLOT_5 == 1):
        Unknown23006(0, 18)
    if (SLOT_5 == 2):
        Unknown23006(0, 19)
    if (SLOT_5 == 3):
        Unknown23006(0, 20)
    if (SLOT_5 == 4):
        Unknown23006(0, 27)
    if (SLOT_5 == 5):
        Unknown23006(0, 22)
    if (SLOT_5 == 6):
        Unknown23006(0, 23)
    if (SLOT_5 == 7):
        Unknown23006(0, 24)
    if (SLOT_5 == 8):
        Unknown23006(0, 25)
    if (SLOT_5 == 9):
        Unknown23006(0, 26)
    if (SLOT_5 == 10):
        Unknown23006(0, 21)
    if (SLOT_5 == 11):
        Unknown23006(0, 28)
    if (SLOT_5 == 12):
        Unknown23006(0, 29)
    if (SLOT_5 >= 13):
        Unknown23006(0, 30)

@State
def PKU_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('504b555f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PKU_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PKU_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PKU_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 110):
            Unknown23185('504b555f506572736f6e6135425f326e6400000000000000000000000000000032000000')
        if (SLOT_48 == 120):
            Unknown23185('504b555f506572736f6e6135425f33726400000000000000000000000000000032000000')
        if (SLOT_48 == 130):
            Unknown23185('504b555f506572736f6e6141697235420000000000000000000000000000000032000000')
        if (SLOT_48 == 510):
            Unknown23185('504b555f506572736f6e61547269706c6554564300000000000000000000000032000000')
        if (SLOT_48 == 550):
            Unknown23185('504b555f4974656d53686f6f744100000000000000000000000000000000000032000000')
        if (SLOT_48 == 551):
            Unknown23185('504b555f4974656d53686f6f744200000000000000000000000000000000000032000000')
        if (SLOT_48 == 552):
            Unknown23185('504b555f4974656d53686f6f744578000000000000000000000000000000000032000000')
        if (SLOT_48 == 553):
            Unknown23185('504b555f4974656d53686f6f745441470000000000000000000000000000000032000000')
        if (SLOT_48 == 600):
            Unknown23185('504b555f556c74696d6174654d697373696c650000000000000000000000000064000000')
        if (SLOT_48 == 610):
            Unknown23185('504b555f556c74696d6174654d697373696c654f44000000000000000000000064000000')
        if (SLOT_48 == 611):
            Unknown23185('504b555f556c74696d6174654d697373696c655441470000000000000000000064000000')
        if (SLOT_48 == 700):
            Unknown23185('504b555f506572736f6e6141737472616c00000000000000000000000000000096000000')
        if (SLOT_48 == 7002):
            if Unknown23148('PKU_PersonaAstral2'):
                Unknown23185('504b555f506572736f6e6141737472616c57696e00000000000000000000000096000000')
        if (SLOT_48 == 9999):
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
    Unknown3031()

@Subroutine
def PKU_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PKU_AttackInit():
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
    callSubroutine('PKU_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PKU_SPAttackInit():
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
    callSubroutine('PKU_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PKU_DDAttackInit():
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
    Unknown11058('0000000001000000000000000000000000000000')
    SLOT_11 = 120
    callSubroutine('PKU_ReceptionSignal')
    Unknown23023()

@Subroutine
def PKU_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PKU_ForceWarp():
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
    enterState('PKU_PersonaWait')

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
        callSubroutine('PKU_ReceptionSignal')
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

@Subroutine
def ObjectTeamColor():
    Unknown4061(2)
    Unknown3000(0)
    if (SLOT_95 == 0):
        Unknown3000(0)
    if (SLOT_95 == 1):
        Unknown3000(1)
    if (SLOT_95 == 2):
        Unknown3000(0)
    if (SLOT_95 == 3):
        Unknown3000(1)

@State
def PKU_Persona5B_2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PKU_AttackInit')
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9362(1)
        Unknown9178(1)
        AirPushbackX(72000)
        AirPushbackY(7000)
        AirUntechableTime(30)
        WallbounceReboundTime(30)
        Unknown9346(0)
        Unknown23078(1)
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')

        def upon_77():
            Unknown1019(80)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 1100, 0)
    sprite('ki204_00', 2)	# 1-2
    Unknown2006()
    sprite('ki204_01', 3)	# 3-5
    sprite('ki204_02', 2)	# 6-7
    physicsXImpulse(63000)
    SFX_3('hit_h_slow')
    sprite('ki204_03', 1)	# 8-8	 **attackbox here**
    RefreshMultihit()
    sprite('ki204_03', 2)	# 9-10	 **attackbox here**
    sprite('ki204_04', 3)	# 11-13	 **attackbox here**
    sprite('ki204_03', 3)	# 14-16	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_04', 3)	# 17-19	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_03', 3)	# 20-22	 **attackbox here**
    Unknown1019(49)
    sprite('ki204_04', 3)	# 23-25	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown1019(70)
    sprite('ki204_03', 3)	# 26-28	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_04', 3)	# 29-31	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_03', 3)	# 32-34	 **attackbox here**
    Unknown1019(70)
    sprite('keep', 32767)	# 35-32801
    enterState('PersonaDeleteAndIdling')

@State
def PKU_Persona5B_3rd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PKU_AttackInit')
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-15000)
        AirPushbackY(28000)
        AirUntechableTime(30)
        Unknown23078(1)
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')

        def upon_77():
            Unknown1019(50)
    sprite('ki232_00', 2)	# 1-2
    Unknown2006()
    sprite('ki232_01', 2)	# 3-4
    sprite('ki232_02', 6)	# 5-10
    SFX_3('hit_h_slow')
    sprite('ki232_03ex01', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('ki232_03ex01', 1)	# 12-12	 **attackbox here**
    sprite('ki232_04', 3)	# 13-15	 **attackbox here**
    physicsYImpulse(25000)
    setGravity(2000)
    sprite('ki232_05', 3)	# 16-18	 **attackbox here**
    sprite('ki232_06', 3)	# 19-21	 **attackbox here**
    sprite('ki232_07', 3)	# 22-24	 **attackbox here**
    sprite('ki232_08', 3)	# 25-27
    sprite('ki232_09', 3)	# 28-30
    sprite('ki232_10', 3)	# 31-33
    sprite('ki232_08', 3)	# 34-36
    sprite('ki232_09', 3)	# 37-39
    sprite('ki232_10', 3)	# 40-42
    sprite('ki232_08', 3)	# 43-45
    sprite('ki232_09', 3)	# 46-48
    sprite('ki232_10', 3)	# 49-51
    sprite('ki232_08', 3)	# 52-54
    sprite('ki232_09', 3)	# 55-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PKU_PersonaAir5B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PKU_AttackInit')
        AttackLevel_(4)
        AttackP2(75)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9178(1)
        WallbounceReboundTime(10)
        AirPushbackX(45000)
        AirPushbackY(22000)
        AirUntechableTime(42)
        Unknown9346(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PKU_CheckWarp')
    sprite('ki204_00', 3)	# 1-3
    Unknown2006()
    sprite('ki204_01', 11)	# 4-14
    sprite('ki204_02', 3)	# 15-17
    physicsXImpulse(36000)
    SFX_3('hit_h_slow')
    sprite('ki204_03', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('ki204_03', 2)	# 19-20	 **attackbox here**
    Unknown23022(0)
    sprite('ki204_04', 3)	# 21-23	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_03', 3)	# 24-26	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_04', 3)	# 27-29	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_03', 3)	# 30-32	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_04', 3)	# 33-35	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown1019(70)
    Unknown23029(3, 998, 0)
    sprite('ki204_03', 3)	# 36-38	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_04', 3)	# 39-41	 **attackbox here**
    Unknown1019(70)
    sprite('ki204_03', 3)	# 42-44	 **attackbox here**
    Unknown1019(70)
    sprite('keep', 32767)	# 45-32811
    enterState('PersonaDeleteAndIdling')

@State
def PKU_PersonaTripleTVC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff0000000000000000000000000000000000000000')
        callSubroutine('PKU_SPAttackInit')
        Unknown23022(1)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')

        def upon_14():
            Unknown23029(3, 5106, 0)

        def upon_43():
            if (SLOT_48 == 511):
                enterState('PersonaTVWarp')
    sprite('ki404_00', 3)	# 1-3
    Unknown2006()
    sprite('ki404_01', 4)	# 4-7
    sprite('ki404_02', 3)	# 8-10
    sprite('ki404_03', 3)	# 11-13
    GFX_1('kief_sikoshock_04', 0)
    ScreenShake(0, 10000)
    sprite('ki404_04', 1)	# 14-14
    sprite('ki404_04', 2)	# 15-16
    Unknown23022(0)
    sprite('ki404_05', 3)	# 17-19
    sprite('ki404_06', 3)	# 20-22
    sprite('ki404_07', 3)	# 23-25
    sprite('ki404_05', 3)	# 26-28
    sprite('ki404_06', 3)	# 29-31
    sprite('ki404_07', 3)	# 32-34
    sprite('ki404_05', 3)	# 35-37
    sprite('ki404_06', 3)	# 38-40
    sprite('ki404_07', 3)	# 41-43
    sprite('keep', 32767)	# 44-32810
    enterState('PersonaDeleteAndIdling')

@State
def PersonaTVWarp():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PKU_SPAttackInit')
        Unknown23151(3, 104)
        Unknown2018(1, 0)
        setInvincible(1)
    sprite('ki405_00', 20)	# 1-20
    Unknown2006()
    sprite('ki405_01', 3)	# 21-23
    sprite('ki405_02', 15)	# 24-38
    GFX_1('kuef_closesmoke_01', 0)
    sprite('ki405_03', 4)	# 39-42
    sprite('ki405_04', 4)	# 43-46
    sprite('ki405_05', 4)	# 47-50
    sprite('ki405_06', 4)	# 51-54
    sprite('ki405_07', 25)	# 55-79
    setInvincible(0)
    sprite('keep', 32767)	# 80-32846
    enterState('PersonaDeleteAndIdling')

@State
def PKU_ItemShootA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000206cfbff80841e00c0bdf0ff40420f00')
        callSubroutine('PKU_SPAttackInit')
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackX(18000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1800)
        Hitstop(0)
        Unknown11001(5, 5, 8)
        AirUntechableTime(30)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('ki205_00', 2)	# 1-2	 **attackbox here**
    sprite('ki205_01', 2)	# 3-4	 **attackbox here**
    StartMultihit()
    sprite('ki205_02', 2)	# 5-6	 **attackbox here**
    SFX_3('hit_m_slow')
    sprite('ki205_04', 2)	# 7-8
    physicsXImpulse(10000)
    sprite('ki205_05', 2)	# 9-10
    Unknown1019(60)
    sprite('ki205_06', 3)	# 11-13
    callSubroutine('Item')
    Unknown23029(1, 5112, 0)
    Unknown1019(60)
    sprite('ki205_07', 3)	# 14-16
    Unknown1019(60)
    sprite('ki205_08', 3)	# 17-19
    Unknown1019(60)
    sprite('ki205_06', 3)	# 20-22
    Unknown1019(60)
    sprite('ki205_07', 3)	# 23-25
    Unknown1019(60)
    sprite('ki205_08', 3)	# 26-28
    Unknown1019(60)
    sprite('ki205_06', 3)	# 29-31
    Unknown1019(0)
    setInvincible(0)
    DisableAttackRestOfMove()
    sprite('ki205_07', 3)	# 32-34
    sprite('ki205_08', 3)	# 35-37
    sprite('ki205_06', 3)	# 38-40
    sprite('ki205_07', 3)	# 41-43
    sprite('ki205_08', 3)	# 44-46
    sprite('ki205_06', 3)	# 47-49
    sprite('ki205_07', 3)	# 50-52
    sprite('ki205_08', 3)	# 53-55
    sprite('ki205_06', 3)	# 56-58
    sprite('ki205_07', 3)	# 59-61
    sprite('ki205_08', 3)	# 62-64
    sprite('ki205_06', 3)	# 65-67
    sprite('ki205_07', 3)	# 68-70
    sprite('ki205_08', 3)	# 71-73
    sprite('keep', 32767)	# 74-32840
    enterState('PersonaDeleteAndIdling')

@State
def PKU_ItemShootB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000206cfbff80841e00c0bdf0ff40420f00')
        callSubroutine('PKU_SPAttackInit')
        AttackLevel_(3)
        AttackP1(90)
        Damage(900)
        Unknown11092(1)
        AirPushbackX(18000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1800)
        Hitstop(0)
        Unknown11001(5, 5, 8)
        AirUntechableTime(48)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('ki205_00', 2)	# 1-2	 **attackbox here**
    sprite('ki205_01', 2)	# 3-4	 **attackbox here**
    StartMultihit()
    sprite('ki205_02', 2)	# 5-6	 **attackbox here**
    SFX_3('hit_m_slow')
    sprite('ki205_01', 3)	# 7-9	 **attackbox here**
    sprite('ki205_02', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 3)	# 13-15	 **attackbox here**
    sprite('ki205_02', 3)	# 16-18	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 3)	# 19-21	 **attackbox here**
    sprite('ki205_02', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_04', 2)	# 25-26
    physicsXImpulse(10000)
    sprite('ki205_05', 2)	# 27-28
    Unknown1019(60)
    sprite('ki205_06', 3)	# 29-31
    callSubroutine('Item')
    Unknown23029(1, 5112, 0)
    Unknown1019(60)
    sprite('ki205_07', 3)	# 32-34
    Unknown1019(60)
    sprite('ki205_08', 3)	# 35-37
    Unknown1019(60)
    setInvincible(0)
    sprite('ki205_05', 2)	# 38-39
    Unknown1019(60)
    sprite('ki205_04', 2)	# 40-41
    Unknown1019(60)
    sprite('ki205_04', 2)	# 42-43
    Unknown1019(0)
    SFX_3('hit_m_slow')
    sprite('ki205_05', 2)	# 44-45
    sprite('ki205_06', 3)	# 46-48
    callSubroutine('Item')
    sprite('ki205_07', 3)	# 49-51
    sprite('ki205_08', 3)	# 52-54
    sprite('ki205_06', 3)	# 55-57
    sprite('ki205_07', 3)	# 58-60
    sprite('ki205_08', 3)	# 61-63
    sprite('ki205_06', 3)	# 64-66
    sprite('ki205_07', 3)	# 67-69
    sprite('ki205_08', 3)	# 70-72
    sprite('ki205_06', 3)	# 73-75
    sprite('ki205_07', 3)	# 76-78
    sprite('ki205_08', 3)	# 79-81
    sprite('ki205_07', 3)	# 82-84
    sprite('ki205_08', 3)	# 85-87
    sprite('ki205_06', 3)	# 88-90
    sprite('ki205_07', 3)	# 91-93
    sprite('ki205_08', 3)	# 94-96
    sprite('keep', 32767)	# 97-32863
    enterState('PersonaDeleteAndIdling')

@State
def PKU_ItemShootEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000206cfbff80841e00c0bdf0ff40420f00')
        callSubroutine('PKU_SPAttackInit')
        AttackLevel_(3)
        AttackP1(90)
        Damage(600)
        Unknown11092(1)
        AirPushbackX(18000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1800)
        Hitstop(0)
        Unknown11001(5, 5, 8)
        AirUntechableTime(48)
        Unknown30065(0)
        MinimumDamagePct(10)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('ki205_00', 2)	# 1-2	 **attackbox here**
    sprite('ki205_01', 1)	# 3-3	 **attackbox here**
    sprite('ki205_02', 1)	# 4-4	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 1)	# 5-5	 **attackbox here**
    sprite('ki205_02', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 1)	# 7-7	 **attackbox here**
    sprite('ki205_02', 1)	# 8-8	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 1)	# 9-9	 **attackbox here**
    sprite('ki205_02', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 1)	# 11-11	 **attackbox here**
    sprite('ki205_02', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 1)	# 13-13	 **attackbox here**
    sprite('ki205_02', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 1)	# 15-15	 **attackbox here**
    sprite('ki205_02', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_01', 1)	# 17-17	 **attackbox here**
    sprite('ki205_02', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('ki205_01', 1)	# 19-19	 **attackbox here**
    sprite('ki205_02', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    sprite('ki205_01', 1)	# 21-21	 **attackbox here**
    sprite('ki205_02', 1)	# 22-22	 **attackbox here**
    RefreshMultihit()
    sprite('ki205_01', 1)	# 23-23	 **attackbox here**
    sprite('ki205_02', 1)	# 24-24	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_slow')
    sprite('ki205_04', 2)	# 25-26
    physicsXImpulse(10000)
    sprite('ki205_05', 1)	# 27-27
    Unknown1019(60)
    sprite('ki205_06', 2)	# 28-29
    callSubroutine('Item')
    Unknown23029(1, 5111, 0)
    Unknown1019(60)
    sprite('ki205_07', 2)	# 30-31
    Unknown1019(60)
    sprite('ki205_08', 2)	# 32-33
    Unknown1019(60)
    setInvincible(0)
    sprite('ki205_05', 2)	# 34-35
    Unknown1019(60)
    sprite('ki205_04', 2)	# 36-37
    Unknown1019(60)
    sprite('ki205_04', 2)	# 38-39
    Unknown1019(0)
    SFX_3('hit_m_slow')
    sprite('ki205_05', 2)	# 40-41
    sprite('ki205_06', 3)	# 42-44
    callSubroutine('Item')
    sprite('ki205_07', 3)	# 45-47
    sprite('ki205_08', 3)	# 48-50
    sprite('ki205_06', 3)	# 51-53
    sprite('ki205_07', 3)	# 54-56
    sprite('ki205_08', 3)	# 57-59
    sprite('ki205_06', 3)	# 60-62
    sprite('ki205_07', 3)	# 63-65
    sprite('ki205_08', 3)	# 66-68
    sprite('ki205_07', 3)	# 69-71
    sprite('ki205_08', 3)	# 72-74
    sprite('ki205_06', 3)	# 75-77
    sprite('keep', 32767)	# 78-32844
    enterState('PersonaDeleteAndIdling')

@State
def PKU_ItemShootTAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000c0f2fcff0000000040420f0080841e00c0bdf0ff00000000')
        callSubroutine('PKU_SPAttackInit')
        AttackLevel_(3)
        AttackP1(70)
        Unknown11042(1)
        AirPushbackX(25000)
        AirPushbackY(10000)
        Hitstop(0)
        Unknown11001(5, 5, 8)
        AirUntechableTime(60)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')
    sprite('ki205_00', 2)	# 1-2	 **attackbox here**
    sprite('ki205_01', 2)	# 3-4	 **attackbox here**
    StartMultihit()
    sprite('ki205_02', 2)	# 5-6	 **attackbox here**
    SFX_3('hit_m_slow')
    sprite('ki205_04', 2)	# 7-8
    physicsXImpulse(10000)
    sprite('ki205_05', 2)	# 9-10
    Unknown1019(60)
    sprite('ki205_06', 3)	# 11-13
    callSubroutine('Item')
    Unknown1019(60)
    sprite('ki205_07', 3)	# 14-16
    Unknown1019(60)
    sprite('ki205_08', 3)	# 17-19
    Unknown1019(60)
    sprite('ki205_06', 3)	# 20-22
    Unknown1019(60)
    sprite('ki205_07', 3)	# 23-25
    Unknown1019(60)
    sprite('ki205_08', 3)	# 26-28
    Unknown1019(60)
    sprite('ki205_06', 3)	# 29-31
    Unknown1019(0)
    setInvincible(0)
    DisableAttackRestOfMove()
    sprite('ki205_07', 3)	# 32-34
    sprite('ki205_08', 3)	# 35-37
    sprite('ki205_06', 3)	# 38-40
    sprite('ki205_07', 3)	# 41-43
    sprite('ki205_08', 3)	# 44-46
    sprite('keep', 32767)	# 47-32813
    enterState('PersonaDeleteAndIdling')

@State
def PKU_UltimateMissile():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000702ffcff0000000000000000000000000000000000000000')
        callSubroutine('PKU_DDAttackInit')
        AttackLevel_(4)
        Damage(2400)
        Hitstop(0)
        AirPushbackY(40000)
        AirPushbackX(50000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        MinimumDamagePct(40)
        Unknown2053(1)
        Unknown2054(1)
        callSubroutine('PKU_CheckWarp')
        Unknown23022(1)
    sprite('ki430_00', 29)	# 1-29
    Unknown2006()
    sprite('ki430_01', 4)	# 30-33
    sprite('ki430_02', 3)	# 34-36
    GFX_0('MissileMaster', 0)
    Unknown38(4, 1)
    Unknown23029(4, 6101, 0)
    sprite('ki430_03', 3)	# 37-39
    sprite('ki430_04', 3)	# 40-42
    sprite('ki430_05', 3)	# 43-45
    sprite('ki430_06', 3)	# 46-48
    sprite('ki430_07', 3)	# 49-51
    sprite('ki430_05', 3)	# 52-54
    sprite('ki430_06', 3)	# 55-57
    sprite('ki430_07', 3)	# 58-60
    sprite('ki430_05', 3)	# 61-63
    sprite('ki430_06', 3)	# 64-66
    sprite('keep', 32767)	# 67-32833
    enterState('PersonaDeleteAndIdling')

@State
def PKU_UltimateMissileOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000702ffcff0000000000000000000000000000000000000000')
        callSubroutine('PKU_DDAttackInit')
        Unknown2053(1)
        Unknown2054(1)
        callSubroutine('PKU_CheckWarp')
        Unknown23022(1)
    sprite('ki430_00', 29)	# 1-29
    Unknown2006()
    sprite('ki430_01', 4)	# 30-33
    sprite('ki430_02', 3)	# 34-36
    GFX_0('MissileMaster', 1)
    Unknown38(4, 1)
    Unknown23029(4, 6102, 0)
    sprite('ki430_03', 3)	# 37-39
    sprite('ki430_04', 3)	# 40-42
    sprite('ki430_05', 3)	# 43-45
    sprite('ki430_06', 3)	# 46-48
    sprite('ki430_07', 3)	# 49-51
    sprite('ki430_06', 3)	# 52-54
    sprite('ki430_05', 3)	# 55-57
    sprite('ki430_04', 3)	# 58-60
    sprite('ki430_03', 3)	# 61-63
    sprite('ki430_02', 3)	# 64-66
    sprite('ki430_01', 3)	# 67-69
    sprite('ki430_00', 10)	# 70-79
    sprite('ki430_01', 3)	# 80-82
    sprite('ki430_02', 3)	# 83-85
    Unknown23029(4, 6103, 0)
    sprite('ki430_03', 3)	# 86-88
    sprite('ki430_04', 3)	# 89-91
    sprite('ki430_05', 3)	# 92-94
    sprite('ki430_06', 3)	# 95-97
    sprite('ki430_07', 3)	# 98-100
    sprite('ki430_05', 3)	# 101-103
    sprite('ki430_06', 3)	# 104-106
    sprite('ki430_07', 3)	# 107-109
    sprite('ki430_05', 3)	# 110-112
    sprite('ki430_06', 3)	# 113-115
    sprite('keep', 32767)	# 116-32882
    enterState('PersonaDeleteAndIdling')

@State
def PKU_UltimateMissileTAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000702ffcff0000000000000000000000000000000000000000')
        callSubroutine('PKU_SPAttackInit')
        Unknown2053(1)
        callSubroutine('PKU_CheckWarp')
        Unknown4007(3)
        Unknown2034(1)
        Unknown23022(0)

        def upon_14():
            clearUponHandler(14)
            clearUponHandler(44)
            Unknown23029(4, 6106, 0)

        def upon_44():
            clearUponHandler(14)
            clearUponHandler(44)
            Unknown23029(4, 6106, 0)
    sprite('ki430_00', 12)	# 1-12
    Unknown2006()
    sprite('ki430_01', 4)	# 13-16
    sprite('ki430_02', 3)	# 17-19
    GFX_0('MissileMaster', 0)
    Unknown38(4, 1)
    Unknown23029(4, 6104, 0)
    sprite('ki430_03', 3)	# 20-22
    sprite('ki430_04', 3)	# 23-25
    sprite('ki430_05', 3)	# 26-28
    sprite('ki430_06', 3)	# 29-31
    sprite('ki430_07', 3)	# 32-34
    sprite('ki430_05', 3)	# 35-37
    sprite('ki430_06', 3)	# 38-40
    sprite('ki430_07', 3)	# 41-43
    sprite('ki430_05', 3)	# 44-46
    sprite('ki430_06', 3)	# 47-49
    sprite('keep', 32767)	# 50-32816
    enterState('PersonaDeleteAndIdling')

@State
def PKU_PersonaAstral():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006700000020a1070040420f0000000000000000000000000000000000')
        callSubroutine('PKU_DDAttackInit')
        Unknown2012()
        AttackLevel_(5)
        Damage(1000)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11064(1)
        MinimumDamagePct(100)
        AirPushbackX(0)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(10000)
        Unknown11042(1)
        Unknown9310(60)
        PushbackX(10000)
        Unknown11084(1)
        Unknown11086(1)
        Unknown21010(1)
        callSubroutine('PKU_ForceWarp')
        Unknown2053(0)
        Unknown2054(1)
        Unknown23033(-20)
        sendToLabelUpon(2, 1)

        def upon_12():
            Unknown23029(3, 7000, 0)
            sendToLabel(2)
        Unknown23022(1)
    sprite('ki450_00', 4)	# 1-4
    sprite('ki450_01', 4)	# 5-8
    sprite('ki450_00', 4)	# 9-12
    sprite('ki450_01', 4)	# 13-16
    setGravity(2000)
    label(0)
    sprite('ki450_00', 4)	# 17-20
    sprite('ki450_01', 4)	# 21-24
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ki450_02', 1)	# 25-25	 **attackbox here**
    GFX_1('kief_450shogeki', 0)
    RefreshMultihit()
    ScreenShake(20000, 0)
    SFX_3('down_marble_m')
    sprite('ki450_02', 25)	# 26-50	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown23022(0)
    sprite('keep', 32767)	# 51-32817
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(2)
    sprite('ki450_02', 5)	# 32818-32822	 **attackbox here**
    sprite('ki450_02', 12)	# 32823-32834	 **attackbox here**
    sprite('null', 32767)	# 32835-65601
    enterState('PKU_PersonaAstral2')

@State
def PKU_PersonaAstral2():

    def upon_IMMEDIATE():
        callSubroutine('PKU_DDAttackInit')
        sendToLabelUpon(2, 2)
        Unknown23022(1)
    sprite('ki450_03', 3)	# 1-3
    sprite('ki450_04', 3)	# 4-6
    sprite('ki450_05', 3)	# 7-9
    sprite('ki450_06', 3)	# 10-12
    sprite('ki450_07', 3)	# 13-15
    sprite('ki450_08', 3)	# 16-18
    sprite('ki450_09', 3)	# 19-21
    sprite('ki450_04', 3)	# 22-24
    sprite('ki450_05', 3)	# 25-27
    sprite('ki450_06', 3)	# 28-30
    sprite('ki450_07', 3)	# 31-33
    sprite('ki450_08', 3)	# 34-36
    sprite('ki450_09', 3)	# 37-39
    sprite('ki450_04', 3)	# 40-42
    sprite('ki450_05', 3)	# 43-45
    sprite('ki450_06', 3)	# 46-48
    sprite('ki450_07', 3)	# 49-51
    sprite('ki450_08', 3)	# 52-54
    sprite('ki450_09', 3)	# 55-57
    sprite('ki450_04', 3)	# 58-60
    sprite('ki450_05', 3)	# 61-63
    sprite('ki450_06', 3)	# 64-66
    sprite('ki450_07', 3)	# 67-69
    sprite('ki450_08', 3)	# 70-72
    sprite('ki450_09', 3)	# 73-75
    sprite('ki450_04', 3)	# 76-78
    sprite('ki450_05', 3)	# 79-81
    sprite('ki450_06', 3)	# 82-84
    GFX_0('450Kemuri', 0)
    SFX_3('bomb_m')
    ScreenShake(0, 10000)
    sprite('ki450_10', 4)	# 85-88
    Unknown36(22)
    Unknown3001(0)
    Unknown1084(1)
    setGravity(0)
    Unknown35()
    SFX_3('bound_steal_m')
    ScreenShake(0, 10000)
    Unknown1064(600)
    sprite('ki450_11', 4)	# 89-92
    Unknown1064(750)
    sprite('ki450_11', 54)	# 93-146
    Unknown1064(1000)
    sprite('ki450_12', 1)	# 147-147
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 148-150
    physicsYImpulse(10)
    setGravity(-50)
    GFX_0('450uchiage', 0)
    sprite('ki450_13', 3)	# 151-153
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 154-156
    ScreenShake(15000, 0)
    sprite('ki450_12', 3)	# 157-159
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 160-162
    sprite('ki450_14', 3)	# 163-165
    setGravity(-300)
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 166-168
    sprite('ki450_13', 3)	# 169-171
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 172-174
    sprite('ki450_12', 3)	# 175-177
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 178-180
    sprite('ki450_14', 3)	# 181-183
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 184-186
    ScreenShake(15000, 0)
    setGravity(-500)
    sprite('ki450_13', 3)	# 187-189
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 190-192
    sprite('ki450_12', 3)	# 193-195
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 196-198
    sprite('ki450_14', 3)	# 199-201
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 202-204
    ScreenShake(15000, 0)
    sprite('ki450_13', 3)	# 205-207
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 208-210
    sprite('ki450_12', 3)	# 211-213
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 214-216
    sprite('ki450_14', 3)	# 217-219
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 220-222
    ScreenShake(15000, 0)
    sprite('ki450_13', 3)	# 223-225
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 226-228
    sprite('ki450_12', 3)	# 229-231
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 232-234
    sprite('ki450_14', 3)	# 235-237
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 238-240
    ScreenShake(15000, 0)
    sprite('ki450_13', 3)	# 241-243
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 244-246
    sprite('ki450_12', 3)	# 247-249
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 250-252
    sprite('ki450_14', 3)	# 253-255
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 256-258
    ScreenShake(15000, 0)
    sprite('ki450_13', 3)	# 259-261
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 262-264
    sprite('ki450_12', 3)	# 265-267
    ScreenShake(15000, 0)
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 268-270
    sprite('ki450_14', 3)	# 271-273
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 274-276
    sprite('ki450_13', 3)	# 277-279
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 280-282
    sprite('ki450_12', 3)	# 283-285
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 286-288
    sprite('ki450_14', 3)	# 289-291
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 292-294
    sprite('ki450_13', 3)	# 295-297
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 298-300
    sprite('ki450_12', 3)	# 301-303
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 304-306
    sprite('ki450_14', 3)	# 307-309
    SFX_3('quake_l')
    sprite('ki450_12', 3)	# 310-312
    sprite('ki450_13', 3)	# 313-315
    SFX_3('quake_l')
    sprite('ki450_14', 3)	# 316-318
    sprite('ki450_12', 3)	# 319-321
    SFX_3('quake_l')
    sprite('ki450_13', 3)	# 322-324
    sprite('ki450_14', 32767)	# 325-33091

@State
def PKU_PersonaAstralWin():

    def upon_IMMEDIATE():
        callSubroutine('PKU_DDAttackInit')
        sendToLabelUpon(2, 2)
        Unknown23022(1)
    label(0)
    sprite('ki450_15', 6)	# 1-6
    Unknown1084(1)
    Unknown1086(3)
    teleportRelativeX(500000)
    teleportRelativeY(700000)
    setGravity(1000)
    sprite('ki450_16', 6)	# 7-12
    label(1)
    sprite('ki450_15', 6)	# 13-18
    sprite('ki450_16', 6)	# 19-24
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ki450_17', 14)	# 25-38
    ScreenShake(0, 8000)
    SFX_3('quake_l')
    sprite('ki450_18', 4)	# 39-42
    label(3)
    sprite('ki450_19', 5)	# 43-47
    sprite('ki450_20', 5)	# 48-52
    sprite('ki450_21', 5)	# 53-57
    loopRest()
    gotoLabel(3)
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def AsiWater():

    def upon_IMMEDIATE():
        Unknown3032()
        callSubroutine('ObjectTeamColor')
        teleportRelativeX(120000)
        Unknown1096(800)

        def upon_44():
            Unknown13(25)
    sprite('null', 5)	# 1-5
    sprite('vr_ku211_00', 4)	# 6-9
    sprite('vr_ku211_01', 4)	# 10-13
    GFX_0('AsiSakana', 0)
    sprite('vr_ku211_02', 4)	# 14-17
    sprite('vr_ku211_03', 4)	# 18-21
    sprite('vr_ku211_04', 4)	# 22-25
    sprite('vr_ku211_05', 4)	# 26-29
    sprite('vr_ku211_06', 10)	# 30-39
    Unknown3004(-51)

@State
def AsiSakana():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(300)
        AttackP2(100)
        AirPushbackY(-30000)
        Hitstop(0)
        Unknown2053(1)
        Unknown2034(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000000000000010000000000000000000000')
        ChipDamagePct(0)
        MinimumDamagePct(0)
        Unknown3032()
        callSubroutine('ObjectTeamColor')

        def upon_5():
            YAccel(-50)
            Unknown1019(50)
            Unknown3004(-7)

        def upon_ON_HIT_OR_BLOCK():
            physicsXImpulse(-2500)
            physicsYImpulse(20000)
            setGravity(2200)

        def upon_12():
            Hitstop(3)

        def upon_44():
            Unknown13(25)
        DisableAttackRestOfMove()

        def upon_53():
            clearUponHandler(5)
            Unknown3004(-16)
    sprite('vr_ku211_07', 4)	# 1-4	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    physicsXImpulse(12000)
    physicsYImpulse(31500)
    setGravity(2200)
    sprite('vr_ku211_08', 4)	# 5-8	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    sprite('vr_ku211_07', 5)	# 9-13	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    GFX_1('kuef_sakanamizu_00', 1)
    sprite('vr_ku211_08', 5)	# 14-18	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    GFX_1('kuef_sakanamizu_00', 1)
    sprite('vr_ku211_07', 6)	# 19-24	 **attackbox here**
    sprite('vr_ku211_08', 1)	# 25-25	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ku211_08', 5)	# 26-30	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('vr_ku211_07', 6)	# 31-36	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 37-42	 **attackbox here**
    sprite('vr_ku211_07', 6)	# 43-48	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 49-54	 **attackbox here**
    sprite('vr_ku211_07', 6)	# 55-60	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 61-66	 **attackbox here**
    sprite('vr_ku211_07', 6)	# 67-72	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 73-78	 **attackbox here**

@State
def AsiWater_Crush():

    def upon_IMMEDIATE():
        Unknown3032()
        callSubroutine('ObjectTeamColor')
        teleportRelativeX(120000)
        Unknown1096(800)

        def upon_44():
            Unknown13(25)
    sprite('null', 5)	# 1-5
    sprite('vr_ku211_00', 4)	# 6-9
    sprite('vr_ku211_01', 4)	# 10-13
    GFX_0('AsiSakana_Crush', 0)
    sprite('vr_ku211_02', 4)	# 14-17
    sprite('vr_ku211_03', 4)	# 18-21
    sprite('vr_ku211_04', 4)	# 22-25
    sprite('vr_ku211_05', 4)	# 26-29
    sprite('vr_ku211_06', 10)	# 30-39
    Unknown3004(-51)

@State
def AsiSakana_Crush():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown23022(1)
        Unknown3032()
        callSubroutine('ObjectTeamColor')

        def upon_5():
            YAccel(-50)
            Unknown1019(50)
            Unknown3004(-7)

        def upon_44():
            Unknown13(25)
        DisableAttackRestOfMove()

        def upon_53():
            clearUponHandler(5)
            Unknown3004(-16)
    sprite('vr_ku211_07', 4)	# 1-4	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    physicsXImpulse(12000)
    physicsYImpulse(31500)
    setGravity(2200)
    sprite('vr_ku211_08', 4)	# 5-8	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    sprite('vr_ku211_07', 5)	# 9-13	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    GFX_1('kuef_sakanamizu_00', 1)
    sprite('vr_ku211_08', 5)	# 14-18	 **attackbox here**
    GFX_1('kuef_sakanamizu_00', 0)
    GFX_1('kuef_sakanamizu_00', 1)
    sprite('vr_ku211_07', 6)	# 19-24	 **attackbox here**
    sprite('vr_ku211_08', 1)	# 25-25	 **attackbox here**
    sprite('vr_ku211_08', 5)	# 26-30	 **attackbox here**
    sprite('vr_ku211_07', 6)	# 31-36	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 37-42	 **attackbox here**
    sprite('vr_ku211_07', 6)	# 43-48	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 49-54	 **attackbox here**
    sprite('vr_ku211_07', 6)	# 55-60	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 61-66	 **attackbox here**
    sprite('vr_ku211_07', 6)	# 67-72	 **attackbox here**
    sprite('vr_ku211_08', 6)	# 73-78	 **attackbox here**

@State
def kuef_202():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(0)
    sprite('vr_ku202_00', 8)	# 1-8
    Unknown3004(-32)

@State
def ScrewWind():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('6b7565663430325f736372657730302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()

        def upon_43():
            if (SLOT_48 == 2000):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    GFX_2('kuef_scurewcircle_01')
    label(0)
    sprite('null', 10)	# 32768-32777
    Unknown3004(-26)
    Unknown1067(100)

@State
def Tvwarp():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Hitstop(6)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(7000)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(2000)
        Unknown2053(1)
        callSubroutine('ObjectTeamColor')
        Unknown2003(1)
        Unknown2019(500)
        Unknown2018(0, 0)
        Unknown23015(11)

        def upon_43():
            if (SLOT_48 == 5100):
                pass
            if (SLOT_48 == 5101):
                pass
            if (SLOT_48 == 5102):
                Unknown1086(22)
                teleportRelativeY(0)
                teleportRelativeX(-250000)
                DisableAttackRestOfMove()
            if (SLOT_48 == 5104):
                Unknown2034(1)
            if (SLOT_48 == 5105):
                Unknown2034(0)
        sendToLabelUpon(54, 0)

        def upon_53():
            sendToLabel(0)
        if (SLOT_25 <= 250000):
            teleportRelativeX(-250000)
        DisableAttackRestOfMove()
    sprite('vr_ku405_00', 1)	# 1-1	 **attackbox here**
    sprite('vr_ku405_00', 2)	# 2-3	 **attackbox here**
    sprite('vr_ku405_01', 2)	# 4-5	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ku405_02', 2)	# 6-7	 **attackbox here**
    sprite('vr_ku405_03', 2)	# 8-9	 **attackbox here**
    sprite('vr_ku405_04', 2)	# 10-11	 **attackbox here**
    sprite('vr_ku405_05', 2)	# 12-13	 **attackbox here**
    sprite('vr_ku405_06', 2)	# 14-15
    sprite('vr_ku405_07', 2)	# 16-17
    sprite('vr_ku405_08', 2)	# 18-19
    SFX_3('down_stone_m')
    sprite('vr_ku405_09', 2)	# 20-21
    SFX_3('down_stone_m')
    sprite('vr_ku405_10', 2)	# 22-23
    sprite('vr_ku405_09', 15)	# 24-38
    sprite('vr_ku405_09', 10)	# 39-48
    label(0)
    sprite('vr_ku405_14', 3)	# 49-51
    sprite('vr_ku405_15', 3)	# 52-54
    sprite('vr_ku405_17', 3)	# 55-57
    sprite('vr_ku405_19', 3)	# 58-60

@State
def Tvwarp_Back():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Hitstop(6)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(7000)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(2000)
        Unknown2053(1)
        callSubroutine('ObjectTeamColor')
        Unknown2003(1)
        Unknown2019(500)
        Unknown2018(0, 0)
        Unknown23015(11)

        def upon_43():
            if (SLOT_48 == 5104):
                Unknown2034(1)
            if (SLOT_48 == 5105):
                Unknown2034(0)
        sendToLabelUpon(54, 0)

        def upon_53():
            sendToLabel(0)
        Unknown1086(22)
        teleportRelativeY(0)
        teleportRelativeX(250000)
        DisableAttackRestOfMove()
    sprite('vr_ku405_00ex01', 1)	# 1-1	 **attackbox here**
    sprite('vr_ku405_00ex01', 2)	# 2-3	 **attackbox here**
    sprite('vr_ku405_01ex01', 2)	# 4-5	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ku405_02ex01', 2)	# 6-7	 **attackbox here**
    sprite('vr_ku405_03ex01', 2)	# 8-9	 **attackbox here**
    sprite('vr_ku405_04ex01', 2)	# 10-11	 **attackbox here**
    sprite('vr_ku405_05ex01', 2)	# 12-13	 **attackbox here**
    sprite('vr_ku405_06ex01', 2)	# 14-15
    sprite('vr_ku405_07ex01', 2)	# 16-17
    sprite('vr_ku405_08ex01', 2)	# 18-19
    SFX_3('down_stone_m')
    sprite('vr_ku405_09ex01', 2)	# 20-21
    SFX_3('down_stone_m')
    sprite('vr_ku405_10ex01', 2)	# 22-23
    sprite('vr_ku405_09ex01', 15)	# 24-38
    sprite('vr_ku405_09ex01', 10)	# 39-48
    label(0)
    sprite('vr_ku405_14ex01', 3)	# 49-51
    sprite('vr_ku405_15ex01', 3)	# 52-54
    sprite('vr_ku405_17ex01', 3)	# 55-57
    sprite('vr_ku405_19ex01', 3)	# 58-60
    ExitState()

@State
def MissileMaster():

    def upon_IMMEDIATE():
        Unknown23056('')
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)

        def upon_43():
            if (SLOT_48 == 6101):
                GFX_0('Missile', 100)
            if (SLOT_48 == 6102):
                GFX_0('MissileOD1', 100)
            if (SLOT_48 == 6103):
                Unknown23151(2, 1)
                GFX_0('MissileOD2', 100)
            if (SLOT_48 == 6104):
                Unknown23151(2, 1)
                GFX_0('MissileTAG', 100)
                Unknown38(4, 1)
            if (SLOT_48 == 6106):
                Unknown23029(4, 6106, 0)
    sprite('null', 300)	# 1-300

@State
def Missile():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(2)
        Hitstop(7)
        Unknown11001(0, 3, 3)
        AirPushbackY(15000)
        AirPushbackX(2000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        MinimumDamagePct(10)
        Unknown4009(3)
        Unknown3032()
        Unknown4061(1)
        Unknown2019(500)
        Unknown53(1)
        Unknown23013(1)
        DisableAttackRestOfMove()

        def upon_LANDING():
            sendToLabel(0)

        def upon_77():
            sendToLabel(2)
    sprite('vr_kief430_missile', 3)	# 1-3	 **attackbox here**
    physicsXImpulse(3000)
    physicsYImpulse(-1500)
    Unknown1072(15000)
    sprite('vr_kief430_missile', 20)	# 4-23	 **attackbox here**
    sprite('vr_kief430_missile', 2)	# 24-25	 **attackbox here**
    sprite('vr_kief430_missile', 2)	# 26-27	 **attackbox here**
    Unknown4009(0)
    GFX_0('MissileHibana', 0)
    sprite('vr_kief430_missile', 4)	# 28-31	 **attackbox here**
    Unknown1015(12000)
    Unknown1021(-8000)
    GFX_1('kief_backsmoke_02', 0)
    RefreshMultihit()
    SLOT_52 = 1
    sprite('vr_kief430_missile', 4)	# 32-35	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-3000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief430_missile', 4)	# 36-39	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-2000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief430_missile', 4)	# 40-43	 **attackbox here**
    label(1)
    sprite('vr_kief430_missile', 4)	# 44-47	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-1000)
    GFX_1('kief_backsmoke_02', 0)
    SFX_3('bomb_m')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 1)	# 48-48
    Unknown4009(0)
    DisableAttackRestOfMove()
    ScreenShake(15000, 15000)
    GFX_1('kief_sikoshock_01', 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    loopRest()
    label(2)
    sprite('dmy_atk', 2)	# 49-50
    Unknown3001(0)
    teleportRelativeX(150000)
    DisableAttackRestOfMove()
    Unknown53(0)
    Unknown23013(0)
    Unknown2053(1)
    clearUponHandler(2)
    clearUponHandler(77)
    Unknown1084(1)
    AttackLevel_(4)
    Damage(4500)
    Hitstop(0)
    AirPushbackY(32000)
    AirPushbackX(26000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirUntechableTime(90)
    MinimumDamagePct(20)
    Unknown9017(1)
    sprite('dmy_atk', 8)	# 51-58
    RefreshMultihit()
    SFX_3('bomb_s')
    SFX_3('bomb_m')
    SFX_3('bomb_l')
    Unknown3001(0)
    GFX_1('kief_bomb_10', 1)
    GFX_1('kief_backsmoke_00', 0)
    sprite('dmy_atk', 2)	# 59-60
    DisableAttackRestOfMove()
    ExitState()
    label(3)
    sprite('keep', 35)	# 61-95
    DisableAttackRestOfMove()
    SLOT_52 = 0
    Unknown3004(-7)
    Unknown1084(1)

@State
def MissileOD1():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(2350)
        Hitstop(7)
        Unknown11001(0, 3, 3)
        AirPushbackY(15000)
        AirPushbackX(2000)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(2)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        MinimumDamagePct(10)
        Unknown4009(3)
        Unknown3032()
        Unknown4061(1)
        Unknown2019(500)
        Unknown53(1)
        Unknown23013(1)
        DisableAttackRestOfMove()

        def upon_LANDING():
            sendToLabel(0)

        def upon_77():
            sendToLabel(2)
    sprite('vr_kief430_missile', 3)	# 1-3	 **attackbox here**
    physicsXImpulse(3000)
    physicsYImpulse(-1500)
    Unknown1072(15000)
    sprite('vr_kief430_missile', 20)	# 4-23	 **attackbox here**
    sprite('vr_kief430_missile', 2)	# 24-25	 **attackbox here**
    sprite('vr_kief430_missile', 2)	# 26-27	 **attackbox here**
    GFX_0('MissileHibana', 0)
    Unknown4009(0)
    sprite('vr_kief430_missile', 4)	# 28-31	 **attackbox here**
    Unknown1015(12000)
    Unknown1021(-8000)
    GFX_1('kief_backsmoke_02', 0)
    RefreshMultihit()
    sprite('vr_kief430_missile', 4)	# 32-35	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-3000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief430_missile', 4)	# 36-39	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-2000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief430_missile', 4)	# 40-43	 **attackbox here**
    label(1)
    sprite('vr_kief430_missile', 4)	# 44-47	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-1000)
    GFX_1('kief_backsmoke_02', 0)
    SFX_3('bomb_m')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 1)	# 48-48
    Unknown4009(0)
    DisableAttackRestOfMove()
    ScreenShake(15000, 15000)
    GFX_1('kief_sikoshock_01', 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    loopRest()
    label(2)
    sprite('dmy_atk', 2)	# 49-50
    Unknown1084(1)
    Unknown3001(0)
    teleportRelativeX(150000)
    DisableAttackRestOfMove()
    SLOT_52 = 0
    Unknown53(0)
    Unknown23013(0)
    Unknown2053(1)
    clearUponHandler(2)
    clearUponHandler(77)
    AttackLevel_(4)
    Damage(2600)
    Hitstop(0)
    AirPushbackY(22000)
    AirPushbackX(26000)
    YImpluseBeforeWallbounce(1100)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirUntechableTime(90)
    MinimumDamagePct(16)
    Unknown9017(1)
    sprite('dmy_atk', 8)	# 51-58
    RefreshMultihit()
    SFX_3('bomb_s')
    SFX_3('bomb_m')
    SFX_3('bomb_l')
    Unknown3001(0)
    GFX_1('kief_bomb_10', 1)
    GFX_1('kief_backsmoke_00', 0)
    sprite('dmy_atk', 2)	# 59-60
    DisableAttackRestOfMove()
    ExitState()
    label(3)
    sprite('keep', 35)	# 61-95
    DisableAttackRestOfMove()
    SLOT_52 = 0
    Unknown3004(-7)
    Unknown1084(1)

@State
def MissileOD2():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(2350)
        Hitstop(7)
        Unknown11001(0, 3, 3)
        AirPushbackY(15000)
        AirPushbackX(2000)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(2)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        MinimumDamagePct(10)
        Unknown4009(3)
        Unknown3032()
        Unknown4061(1)
        Unknown2019(500)
        Unknown53(1)
        Unknown23013(1)
        DisableAttackRestOfMove()

        def upon_LANDING():
            sendToLabel(0)

        def upon_77():
            sendToLabel(2)
    sprite('vr_kief430_missile', 3)	# 1-3	 **attackbox here**
    physicsXImpulse(3000)
    physicsYImpulse(-1500)
    Unknown1072(6000)
    sprite('vr_kief430_missile', 2)	# 4-5	 **attackbox here**
    sprite('vr_kief430_missile', 2)	# 6-7	 **attackbox here**
    GFX_0('MissileHibana', 0)
    Unknown4009(0)
    sprite('vr_kief430_missile', 4)	# 8-11	 **attackbox here**
    Unknown1015(12000)
    Unknown1021(-1000)
    GFX_1('kief_backsmoke_02', 0)
    RefreshMultihit()
    sprite('vr_kief430_missile', 4)	# 12-15	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-1000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief430_missile', 4)	# 16-19	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-1000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief430_missile', 4)	# 20-23	 **attackbox here**
    label(1)
    sprite('vr_kief430_missile', 4)	# 24-27	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-1000)
    GFX_1('kief_backsmoke_02', 0)
    SFX_3('bomb_m')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('keep', 1)	# 28-28
    Unknown4009(0)
    DisableAttackRestOfMove()
    ScreenShake(15000, 15000)
    GFX_1('kief_sikoshock_01', 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    loopRest()
    label(2)
    sprite('dmy_atk', 2)	# 29-30
    Unknown1084(1)
    Unknown3001(0)
    teleportRelativeX(150000)
    DisableAttackRestOfMove()
    SLOT_52 = 0
    Unknown53(0)
    Unknown23013(0)
    Unknown2053(1)
    clearUponHandler(2)
    clearUponHandler(77)
    AttackLevel_(4)
    Damage(2600)
    Hitstop(0)
    AirPushbackY(22000)
    AirPushbackX(26000)
    YImpluseBeforeWallbounce(1800)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirUntechableTime(90)
    MinimumDamagePct(16)
    Unknown9017(1)
    sprite('dmy_atk', 8)	# 31-38
    RefreshMultihit()
    SFX_3('bomb_s')
    SFX_3('bomb_m')
    SFX_3('bomb_l')
    Unknown3001(0)
    GFX_1('kief_bomb_10', 1)
    GFX_1('kief_backsmoke_00', 0)
    sprite('dmy_atk', 2)	# 39-40
    DisableAttackRestOfMove()
    ExitState()
    label(3)
    sprite('keep', 35)	# 41-75
    DisableAttackRestOfMove()
    SLOT_52 = 0
    Unknown3004(-7)
    Unknown1084(1)

@State
def MissileTAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(70)
        Unknown11092(1)
        Unknown23182(3)
        Unknown11042(1)
        Hitstop(7)
        Unknown11001(0, 3, 3)
        AirPushbackY(24500)
        AirPushbackX(28000)
        YImpluseBeforeWallbounce(1600)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        Unknown3032()
        Unknown4061(1)
        Unknown2019(500)
        Unknown53(1)
        Unknown23013(1)
        DisableAttackRestOfMove()

        def upon_CLEAR_OR_EXIT():
            if (SLOT_23 <= 100000):
                clearUponHandler(3)
                sendToLabel(0)
            if (SLOT_25 <= 150000):
                clearUponHandler(3)
                sendToLabel(2)

        def upon_43():
            if (SLOT_48 == 6106):
                clearUponHandler(3)
                Unknown2003(1)
                sendToLabel(2)
    sprite('vr_kief431_missile', 3)	# 1-3	 **attackbox here**
    teleportRelativeX(250000)
    Unknown1007(-50000)
    physicsXImpulse(3000)
    physicsYImpulse(-1500)
    Unknown1072(-12000)
    sprite('vr_kief431_missile', 20)	# 4-23	 **attackbox here**
    sprite('vr_kief431_missile', 2)	# 24-25	 **attackbox here**
    sprite('vr_kief431_missile', 2)	# 26-27	 **attackbox here**
    GFX_0('MissileHibanaTAG', 0)
    sprite('vr_kief431_missile', 4)	# 28-31	 **attackbox here**
    Unknown1015(12000)
    Unknown1021(-8000)
    GFX_1('kief_backsmoke_02', 0)
    RefreshMultihit()
    SLOT_52 = 1
    sprite('vr_kief431_missile', 4)	# 32-35	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-3000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief431_missile', 4)	# 36-39	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-2000)
    GFX_1('kief_backsmoke_02', 0)
    sprite('vr_kief431_missile', 4)	# 40-43	 **attackbox here**
    label(1)
    sprite('vr_kief431_missile', 4)	# 44-47	 **attackbox here**
    Unknown1015(9000)
    Unknown1021(-1000)
    GFX_1('kief_backsmoke_02', 0)
    SFX_3('bomb_m')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vr_ki431_00', 1)	# 48-48
    teleportRelativeX(80000)
    Unknown1007(-50000)
    Unknown4009(0)
    DisableAttackRestOfMove()
    ScreenShake(15000, 15000)
    GFX_1('kief_sikoshock_01', 0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    label(10)
    sprite('vr_ki431_00', 1)	# 49-49
    Unknown2038(1)
    if (SLOT_2 == 1):
        Unknown23119(-1, 240, 1)
    if (SLOT_2 >= 12):
        sendToLabel(2)
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('dmy_atk', 2)	# 50-51
    Unknown3001(0)
    teleportRelativeX(150000)
    DisableAttackRestOfMove()
    Unknown53(0)
    Unknown23013(0)
    Unknown2053(1)
    clearUponHandler(2)
    clearUponHandler(77)
    Unknown1084(1)
    AttackLevel_(4)
    Damage(1500)
    Unknown9017(1)
    Hitstop(7)
    AirPushbackY(24500)
    AirPushbackX(28000)
    YImpluseBeforeWallbounce(1600)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirUntechableTime(60)
    sprite('dmy_atk', 8)	# 52-59
    RefreshMultihit()
    SFX_3('bomb_s')
    SFX_3('bomb_m')
    SFX_3('bomb_l')
    Unknown3001(0)
    GFX_1('kief_bomb_10', 1)
    GFX_1('kief_backsmoke_00', 0)
    sprite('dmy_atk', 2)	# 60-61
    DisableAttackRestOfMove()
    ExitState()
    label(3)
    sprite('keep', 35)	# 62-96
    DisableAttackRestOfMove()
    Unknown3004(-7)
    Unknown1084(1)

@State
def MissileHibana():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4054(2)
        Unknown23067('kief_backfire_05')
    sprite('null', 30)	# 1-30

@State
def MissileHibanaTAG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4054(2)
        Unknown23067('kief_backfire_05')
        Unknown1072(25000)
    sprite('null', 30)	# 1-30

@State
def kuef_433_upper():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('6b7565663433335f75707065722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1007(-160000)
    sprite('null', 18)	# 1-18

@State
def Nihil_Camera():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(3)

        def upon_43():
            if (SLOT_48 == 6500):
                sendToLabel(0)
            if (SLOT_48 == 6501):
                sendToLabel(1)
            if (SLOT_48 == 6502):
                sendToLabel(3)
            if (SLOT_48 == 6503):
                sendToLabel(99)
        loopRelated(17, 360)

        def upon_17():
            Unknown13(25)
    sprite('null', 30)	# 1-30
    Unknown1086(22)
    physicsYImpulse(200000)
    Unknown20009(980)
    Unknown20000(1)
    sprite('null', 20)	# 31-50
    Unknown1084(1)
    sprite('null', 32767)	# 51-32817
    label(0)
    sprite('null', 32767)	# 32818-65584
    clearUponHandler(3)
    Unknown1086(3)
    Unknown20001(1)
    Unknown20002(1)
    teleportRelativeY(0)
    Unknown20009(900)
    Unknown20000(1)
    teleportRelativeX(180000)
    label(3)
    sprite('null', 32767)	# 65585-98351
    Unknown20001(0)
    Unknown20009(1300)
    label(1)
    sprite('null', 50)	# 98352-98401
    Unknown20003(0)
    Unknown2034(1)
    sprite('null', 32767)	# 98402-131168
    Unknown20000(0)
    label(99)
    sprite('null', 25)	# 131169-131193
    Unknown20000(0)
    Unknown20003(0)
    Unknown2034(1)

@State
def ShadowKuma():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(5800)
        AttackP1(48)
        AttackP2(100)
        MinimumDamagePct(26)
        AirPushbackY(22000)
        AirPushbackX(150000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(200)
        Unknown9310(20)
        Unknown9178(1)
        Unknown9346(0)
        Unknown11023(1)
        Unknown9016(1)
        Unknown11068(1)
        Unknown11084(1)
        Unknown2053(1)
        Unknown2015(600)
        EnableCollision(0)
        Unknown23022(1)
        teleportRelativeX(500000)
        sendToLabelUpon(12, 101)

        def upon_8():
            Unknown21015('4e6968696c5f43616d65726100000000000000000000000000000000000000006719000000000000')
            if SLOT_57:
                Unknown23029(3, 6512, 0)
            else:
                Unknown23029(3, 6511, 0)

        def upon_43():
            if (SLOT_48 == 6520):
                Damage(8200)
                SLOT_56 = 1
                MinimumDamagePct(21)
        Unknown2005()
        Unknown2019(1000)
    sprite('null', 30)	# 1-30
    Unknown36(22)
    teleportRelativeX(430000)
    teleportRelativeY(1000000)
    Unknown1084(1)
    setGravity(0)
    Unknown35()
    GFX_0('Nihil_hole', 100)
    sprite('null', 5)	# 31-35
    ScreenShake(2000, 1000)
    SFX_3('quake_s')
    sprite('null', 5)	# 36-40
    ScreenShake(3000, 1000)
    SFX_3('quake_s')
    sprite('null', 5)	# 41-45
    ScreenShake(4000, 1000)
    SFX_3('quake_s')
    sprite('ku435_00', 7)	# 46-52
    ScreenShake(5000, 1000)
    SFX_3('quake_s')
    sprite('ku435_01', 7)	# 53-59
    ScreenShake(6000, 1000)
    SFX_3('quake_s')
    sprite('ku435_02', 7)	# 60-66
    ScreenShake(7000, 1000)
    sprite('ku435_03', 7)	# 67-73
    ScreenShake(8000, 1000)
    sprite('ku435_04', 7)	# 74-80
    ScreenShake(9000, 1000)
    sprite('ku435_05', 7)	# 81-87
    ScreenShake(10000, 1000)
    sprite('ku435_06', 7)	# 88-94
    Unknown2036(45, -1, 0)
    Unknown7006('pku262_0', 100, 846556016, 828322358, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown21015('4e6968696c5f43616d65726100000000000000000000000000000000000000006619000000000000')
    sprite('ku435_07', 6)	# 95-100
    sprite('ku435_08', 6)	# 101-106
    sprite('ku435_06', 6)	# 107-112
    sprite('ku435_07', 6)	# 113-118
    sprite('ku435_08', 6)	# 119-124
    sprite('ku435_06', 6)	# 125-130
    GFX_0('Nihil_charge', 0)
    sprite('ku435_07', 6)	# 131-136
    sprite('ku435_08', 6)	# 137-142
    Unknown23029(3, 6510, 0)
    Unknown36(22)
    physicsYImpulse(-25000)
    Unknown35()
    label(0)
    sprite('ku435_06', 6)	# 143-148

    def upon_CLEAR_OR_EXIT():
        Unknown2038(1)
        Unknown48('030000000200000034000000190000000200000002000000')
        SLOT_58 = (SLOT_58 + 1)
        if (SLOT_2 >= 20):
            if CheckInput(INPUT_PRESS_A):
                clearUponHandler(3)
                sendToLabel(100)
            if CheckInput(INPUT_PRESS_B):
                clearUponHandler(3)
                sendToLabel(100)
            if CheckInput(INPUT_PRESS_C):
                clearUponHandler(3)
                sendToLabel(100)
        if (SLOT_2 == 25):
            Unknown4049(2000)
            Unknown4045('65665f676972646d6973735f670000000000000000000000000000000000000001000000')
        if (SLOT_2 >= 35):
            clearUponHandler(3)
            sendToLabel(100)
    sprite('ku435_07', 6)	# 149-154
    sprite('ku435_08', 6)	# 155-160
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku435_10', 4)	# 161-164
    Unknown26('Nihil_charge')
    sprite('ku435_11', 4)	# 165-168
    sprite('ku435_05', 4)	# 169-172
    ScreenShake(4000, 1000)
    SFX_3('quake_s')
    sprite('ku435_04', 4)	# 173-176
    ScreenShake(6000, 1000)
    SFX_3('quake_s')
    sprite('ku435_03', 4)	# 177-180
    Unknown21015('4e6968696c5f686f6c65000000000000000000000000000000000000000000007319000000000000')
    ScreenShake(8000, 1000)
    sprite('ku435_02', 4)	# 181-184
    ScreenShake(6000, 1000)
    sprite('ku435_01', 4)	# 185-188
    ScreenShake(4000, 1000)
    sprite('ku435_00', 4)	# 189-192
    ScreenShake(2000, 1000)
    sprite('null', 2)	# 193-194
    loopRest()
    ExitState()
    label(100)
    sprite('ku435_09', 2)	# 195-196
    Unknown2036(63, -1, 0)
    Unknown23119(0, 25, 1)
    if (SLOT_2 <= 28):
        if (SLOT_2 >= 25):
            AttackLevel_(5)
            Damage(6380)
            Hitstop(40)
            AirUntechableTime(70)
            AirHitstunAfterWallbounce(50)
            WallbounceReboundTime(40)
            Unknown9215()
            AirPushbackX(550000)
            AirPushbackY(20000)
            AirHitstunAnimation(12)
            Unknown23029(3, 6513, 0)
            SFX_3('quake_l')
            SLOT_58 = 1
            if SLOT_56:
                Damage(9020)
                MinimumDamagePct(21)
    Unknown21015('4e6968696c5f43616d65726100000000000000000000000000000000000000006519000000000000')
    sprite('ku435_12', 10)	# 197-206
    Unknown7006('pku263_0', 100, 846556016, 828322614, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_58:
        Unknown7006('pku264_0', 100, 846556016, 828322870, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        ScreenShake(20000, 20000)
        SFX_3('quake_l')
    sprite('ku435_13', 10)	# 207-216
    if SLOT_56:
        ScreenShake(25000, 25000)
        SFX_3('quake_l')
    sprite('ku435_14', 10)	# 217-226
    if SLOT_56:
        ScreenShake(30000, 30000)
        SFX_3('quake_l')
    sprite('ku435_14', 10)	# 227-236
    if SLOT_56:
        ScreenShake(30000, 30000)
        SFX_3('quake_l')
    sprite('ku435_14', 10)	# 237-246
    Unknown26('Nihil_charge')
    if SLOT_56:
        ScreenShake(30000, 30000)
        SFX_3('quake_l')
    sprite('ku435_14', 10)	# 247-256
    if SLOT_56:
        ScreenShake(30000, 30000)
        SFX_3('quake_l')
    sprite('ku435_15', 2)	# 257-258
    GFX_0('Nihil_swing', 100)
    GFX_1('kuef_433swing', 0)
    GFX_1('kuef_433swing', 1)
    sprite('ku435_16', 2)	# 259-260
    GFX_1('kuef_433swing', 0)
    GFX_1('kuef_433swing', 1)
    sprite('ku435_17', 2)	# 261-262
    SFX_3('hit_h_slow')
    GFX_1('kuef_433swing', 0)
    GFX_1('kuef_433swing', 1)
    sprite('ku435_18', 3)	# 263-265	 **attackbox here**
    SFX_3('blood_h')
    GFX_1('kuef_433swing', 0)
    GFX_1('kuef_433swing', 1)
    RefreshMultihit()
    GFX_1('kuef_433finish', 100)
    sprite('ku435_18', 20)	# 266-285	 **attackbox here**
    DisableAttackRestOfMove()
    GFX_1('kuef_433swing', 0)
    GFX_1('kuef_433swing', 1)
    label(99)
    sprite('ku435_18', 13)	# 286-298	 **attackbox here**
    DisableAttackRestOfMove()
    if (SLOT_58 <= 30):
        SLOT_57 = 1
    sprite('ku435_19', 7)	# 299-305
    ScreenShake(10000, 1000)
    SFX_3('quake_s')
    sprite('ku435_20', 7)	# 306-312
    ScreenShake(8000, 1000)
    SFX_3('quake_s')
    sprite('ku435_21', 7)	# 313-319
    ScreenShake(6000, 1000)
    SFX_3('quake_s')
    sprite('ku435_22', 7)	# 320-326
    ScreenShake(4000, 1000)
    sprite('null', 30)	# 327-356
    Unknown21015('4e6968696c5f686f6c65000000000000000000000000000000000000000000007319000000000000')
    ExitState()
    label(101)
    sprite('ku435_19', 7)	# 357-363
    clearUponHandler(12)
    ScreenShake(10000, 1000)
    SFX_3('quake_s')
    sprite('ku435_20', 7)	# 364-370
    ScreenShake(8000, 1000)
    SFX_3('quake_s')
    sprite('ku435_21', 7)	# 371-377
    ScreenShake(6000, 1000)
    SFX_3('quake_s')
    sprite('ku435_22', 7)	# 378-384
    Unknown23029(3, 6521, 0)
    ScreenShake(4000, 1000)
    sprite('null', 30)	# 385-414
    Unknown21015('4e6968696c5f686f6c65000000000000000000000000000000000000000000007319000000000000')
    ExitState()

@State
def Nihil_hole():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        GFX_2('kuef_433hole')
        teleportRelativeX(-64000)

        def upon_43():
            if (SLOT_48 == 6515):
                sendToLabel(1)
    sprite('null', 7)	# 1-7
    Unknown1096(0)
    sprite('null', 1)	# 8-8
    Unknown1096(500)
    GFX_0('Nihil_hole_add', 100)
    sprite('null', 20)	# 9-28
    Unknown1099(25)
    sprite('null', 250)	# 29-278
    Unknown1096(1000)
    Unknown1099(0)
    GFX_0('Nihil_IdlingSmoke', 100)
    label(1)
    sprite('null', 32)	# 279-310
    clearUponHandler(43)
    Unknown21015('4e6968696c5f49646c696e67536d6f6b650000000000000000000000000000007319000000000000')
    sprite('null', 16)	# 311-326
    Unknown3004(-16)
    Unknown26('Nihil_hole_add')

@State
def Nihil_hole_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
    label(0)
    sprite('null', 10)	# 1-10
    GFX_1('kuef_433smoke', 100)
    gotoLabel(0)

@State
def Nihil_IdlingSmoke():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('6b7565663433335f736d6f6b652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown3035()
        Unknown1007(-40000)
        Unknown1056(1350)

        def upon_43():
            if (SLOT_48 == 6515):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 32)	# 32768-32799
    Unknown3004(-8)

@State
def Nihil_charge():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown1007(48000)
        teleportRelativeX(16000)
        Unknown2019(1000)
        SFX_3('electric_l')
    label(0)
    sprite('null', 10)	# 1-10
    GFX_1('kuef_433charge', 100)
    gotoLabel(0)

@State
def Nihil_swing():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('6b7565663433335f7377696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown21010(1)
        Unknown1007(300000)
        teleportRelativeX(-200000)
    sprite('null', 19)	# 1-19

@State
def UltimateGorogoroCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4009(3)
        Unknown20000(1)
        Unknown20009(1050)
    sprite('null', 32767)	# 1-32767

@State
def UltimateGorogoroTama():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown4061(1)
        Unknown2053(0)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Unknown11034(1)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(3000)
        AirPushbackY(32000)
        PushbackX(0)
        AirUntechableTime(150)
        Unknown9310(10)
        Hitstop(0)
        MinimumDamagePct(100)
        Unknown11084(1)
        Unknown23022(1)

        def upon_12():
            SFX_3('down_steal_m')
            SFX_3('grip_hugs')
        Unknown4007(2)
        Unknown1007(-230000)
        DisableAttackRestOfMove()

        def upon_43():
            if (SLOT_48 == 6530):
                RefreshMultihit()
            if (SLOT_48 == 6531):
                Unknown2003(1)
                clearUponHandler(43)
                sendToLabel(1)
            if (SLOT_48 == 6532):
                Damage(1250)
                Unknown11069('UltimateGorogoroTama')
            if (SLOT_48 == 6534):
                Unknown3038(1)
                DisableAttackRestOfMove()
            if (SLOT_48 == 6535):
                Unknown3038(0)
                RefreshMultihit()
                AirPushbackY(40000)
                Unknown11069('')

        def upon_78():
            Unknown23029(3, 6533, 0)
    sprite('ki432_00', 3)	# 1-3	 **attackbox here**
    GFX_0('kuef_432_smoke', 100)
    sprite('ki432_01', 3)	# 4-6	 **attackbox here**
    sprite('ki432_02', 3)	# 7-9	 **attackbox here**
    sprite('ki432_03', 3)	# 10-12	 **attackbox here**
    label(0)
    sprite('ki432_00', 3)	# 13-15	 **attackbox here**
    sprite('ki432_01', 3)	# 16-18	 **attackbox here**
    sprite('ki432_02', 3)	# 19-21	 **attackbox here**
    sprite('ki432_03', 3)	# 22-24	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 25-25

@State
def kuef_432_smoke():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    label(0)
    sprite('null', 1)	# 1-1
    GFX_1('kuef_432_smoke', 0)
    gotoLabel(0)

@State
def kuef_432_Trampoline():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown2019(100)
        Unknown4061(0)
        Unknown3032()
    sprite('vr_ku432_00', 4)	# 1-4
    sprite('vr_ku432_01', 4)	# 5-8
    sprite('vr_ku432_02', 11)	# 9-19
    sprite('vr_ku432_03', 3)	# 20-22
    sprite('vr_ku432_04', 8)	# 23-30
    sprite('vr_ku432_05', 4)	# 31-34
    sprite('vr_ku432_03', 4)	# 35-38
    Unknown3005(-32)
    GFX_1('kuef_toranporin', 0)
    sprite('vr_ku432_02', 4)	# 39-42

@Subroutine
def Item():
    if (SLOT_5 == 1):
        GFX_0('Item_brahman', 0)
    if (SLOT_5 == 2):
        GFX_0('Item_drpepper', 0)
    if (SLOT_5 == 3):
        GFX_0('Item_agni', 0)
    if (SLOT_5 == 4):
        GFX_0('Item_muscledrink', 0)
    if (SLOT_5 == 5):
        GFX_0('Item_fusenbomb', 0)
    if (SLOT_5 == 6):
        GFX_0('Item_drumkan', 0)
    if (SLOT_5 == 7):
        GFX_0('Item_rockethanabi', 0)
    if (SLOT_5 == 8):
        GFX_0('Item_dryice', 0)
    if (SLOT_5 == 9):
        GFX_0('Item_dorondama', 0)
    if (SLOT_5 == 10):
        GFX_0('Item_buttaix', 0)
    if (SLOT_5 == 11):
        GFX_0('Item_kazaguruma', 0)
    if (SLOT_5 == 12):
        GFX_0('Item_denden', 0)
    if (SLOT_5 >= 13):
        callSubroutine('OkeStack')
        GFX_0('Item_okemaster', 0)
        Unknown38(4, 1)
    if SLOT_IsPlayer2:
        Unknown58('TRI_PKUItemFix', 2, 67)
        if (SLOT_67 == 0):
            SLOT_5 = (SLOT_5 + 1)
            if (SLOT_5 > 13):
                SLOT_5 = 1
    else:
        SLOT_5 = (SLOT_5 + 1)
        if (SLOT_5 > 13):
            SLOT_5 = 1
    callSubroutine('ItemIconUpDate')

@Subroutine
def ItemColor():
    Unknown4061(3)
    Unknown3000(0)
    if (SLOT_95 == 0):
        Unknown3000(0)
    if (SLOT_95 == 1):
        Unknown3000(1)
    if (SLOT_95 == 2):
        Unknown3000(0)
    if (SLOT_95 == 3):
        Unknown3000(1)
    Unknown3032()

@Subroutine
def ItemParam():
    Unknown2034(1)
    Unknown23013(1)
    Unknown2053(1)
    Unknown23015(3)

    def upon_43():
        if (SLOT_48 == 5111):
            physicsXImpulse(12000)
        if (SLOT_48 == 5112):
            physicsXImpulse(2000)

    def upon_LANDING():
        sendToLabel(5)

    def upon_53():
        clearUponHandler(2)
        clearUponHandler(53)
        Unknown23090(25)

    def upon_45():
        Unknown48('19000000020000003a0000000300000002000000aa000000')
        if SLOT_58:
            clearUponHandler(45)
            clearUponHandler(2)
            clearUponHandler(53)
            Unknown23090(25)

@State
def Item_brahman():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        AirUntechableTime(38)
        Hitstop(0)
        Unknown11084(1)
        Unknown9021(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        Unknown23022(0)
        Unknown23091(1)

        def upon_54():
            clearUponHandler(2)
            sendToLabel(6)
    sprite('vr_ki205_br00', 32767)	# 1-32767
    label(5)
    sprite('vr_ki205_br01', 10)	# 32768-32777
    GFX_1('kief_205jimen_s', 100)
    Unknown1084(1)
    Unknown2034(0)
    sprite('vr_ki205_br02', 4)	# 32778-32781
    sprite('vr_ki205_br00', 6)	# 32782-32787
    sprite('vr_ki205_br00ex', 200)	# 32788-32987	 **attackbox here**
    Unknown23067('kief_205brahman')
    Unknown2006()
    RefreshMultihit()
    physicsYImpulse(4500)
    physicsXImpulse(4900)
    SFX_3('blaze_long')
    sprite('vr_ki205_br00ex', 16)	# 32988-33003	 **attackbox here**
    Unknown3004(-20)
    label(6)
    sprite('vr_ki205_br00ex', 10)	# 33004-33013	 **attackbox here**
    DisableAttackRestOfMove()
    teleportRelativeX(50000)
    Unknown1007(50000)
    DisableAttackRestOfMove()
    GFX_1('kief_205itemhit', 100)
    Unknown23118(-32768)
    Unknown1099(70)
    Unknown3004(-300)

@State
def Item_drpepper():

    def upon_IMMEDIATE():
        Unknown23022(1)
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)

        def upon_CLEAR_OR_EXIT():
            Unknown48('19000000020000003500000016000000020000004b000000')
            Unknown48('19000000020000003600000003000000020000004b000000')
            Unknown48('19000000020000003700000018000000020000004b000000')
            if SLOT_51:
                Unknown59('16000000640000001900000064000000')
                if (SLOT_0 < 120000):
                    if (not SLOT_132):
                        if SLOT_53:
                            clearUponHandler(3)
                            Unknown36(22)
                            GFX_1('kief_stkaifuku', 104)
                            GFX_1('kief_spkaifuku', 104)
                            Unknown2068(5000)
                            Unknown35()
                            SFX_3('ku018')
                            Unknown13(25)
                if SLOT_158:
                    Unknown59('03000000640000001900000064000000')
                    if (SLOT_0 < 120000):
                        Unknown48('190000000200000000000000160000000200000084000000')
                        if SLOT_IsInOverdrive2:
                            if SLOT_ReturnVal:
                                clearUponHandler(3)
                                GFX_1('kief_stkaifuku', 104)
                                GFX_1('kief_spkaifuku', 104)
                                Unknown2068(5000)
                                SFX_3('ku018')
                                Unknown13(25)
                else:
                    Unknown59('18000000640000001900000064000000')
                    if (SLOT_0 < 120000):
                        if (not Unknown48('190000000200000000000000160000000200000084000000')):
                            if SLOT_55:
                                clearUponHandler(3)
                                GFX_1('kief_stkaifuku', 104)
                                GFX_1('kief_spkaifuku', 104)
                                Unknown2068(5000)
                                SFX_3('ku018')
                                Unknown13(25)

        def upon_54():
            Unknown13(25)
    sprite('vr_ki205_drpepper00', 32767)	# 1-32767
    label(5)
    sprite('vr_ki205_drpepper00', 30)	# 32768-32797
    GFX_1('kief_205jimen_s', 100)
    setGravity(1800)
    YAccel(-10)
    Unknown1019(15)
    sendToLabelUpon(2, 6)
    label(6)
    sprite('vr_ki205_drpepper00', 2)	# 32798-32799
    GFX_1('kief_205jimen_s', 100)
    YAccel(0)
    Unknown1019(0)
    Unknown2034(0)
    Unknown2053(0)
    sprite('vr_ki205_drpepper00', 18)	# 32800-32817
    SLOT_51 = 1
    sprite('vr_ki205_drpepper00', 160)	# 32818-32977
    Unknown23119(-1, 8, 2)
    sprite('vr_ki205_drpepper00', 160)	# 32978-33137
    Unknown23119(-1, 8, 2)
    sprite('vr_ki205_drpepper00', 160)	# 33138-33297
    Unknown23119(-1, 8, 2)
    sprite('vr_ki205_drpepper00', 16)	# 33298-33313
    clearUponHandler(3)
    Unknown3004(-20)

@State
def Item_agni():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9178(1)
        AirUntechableTime(48)
        AirPushbackX(25000)
        AirPushbackY(35000)
        Unknown11084(1)
        Unknown9346(0)
        WallbounceReboundTime(20)
        Hitstop(0)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)
        Unknown23089('0100000000000000000000000100000001000000000000000100000000000000')
        Unknown23022(0)
        Unknown23091(1)

        def upon_54():
            clearUponHandler(54)
            clearUponHandler(2)
            sendToLabel(7)
    sprite('vr_ki205_ag00', 32767)	# 1-32767
    label(5)
    sprite('vr_ki205_ag01', 2)	# 32768-32769
    Unknown2034(0)
    GFX_1('kief_205jimen_s', 100)
    YAccel(0)
    Unknown1019(0)
    setGravity(0)
    sprite('vr_ki205_ag02', 4)	# 32770-32773
    sprite('vr_ki205_ag00', 43)	# 32774-32816
    sprite('vr_ki205_ag00ex', 200)	# 32817-33016	 **attackbox here**
    Unknown2006()
    Unknown23067('kief_205agni')
    RefreshMultihit()
    physicsYImpulse(13000)
    physicsXImpulse(35000)
    Unknown2053(0)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_38 == 0):
            Unknown23045('62000000')
            if (SLOT_22 > SLOT_0):
                clearUponHandler(3)
                sendToLabel(6)
        else:
            Unknown23045('62000000')
            if (SLOT_22 < SLOT_0):
                clearUponHandler(3)
                sendToLabel(6)
    SFX_3('blaze_long')
    sprite('vr_ki205_ag00ex', 16)	# 33017-33032	 **attackbox here**
    Unknown3004(-20)
    ExitState()
    label(6)
    sprite('vr_ki205_ag00ex', 200)	# 33033-33232	 **attackbox here**
    clearUponHandler(3)
    Unknown2005()
    RefreshMultihit()
    physicsXImpulse(33000)
    physicsYImpulse(20000)
    ExitState()
    label(7)
    sprite('keep', 10)	# 33233-33242
    clearUponHandler(2)
    clearUponHandler(54)
    DisableAttackRestOfMove()
    GFX_1('kief_205itemhit', 100)
    Unknown23118(-32768)
    Unknown1099(70)
    Unknown3004(-50)

@State
def Item_buttaix():

    def upon_IMMEDIATE():
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        Unknown23022(1)
        physicsYImpulse(29000)
        physicsXImpulse(6500)
        setGravity(1000)

        def upon_54():
            clearUponHandler(3)
            Unknown13(25)

        def upon_CLEAR_OR_EXIT():
            Unknown48('19000000020000003500000016000000020000004b000000')
            Unknown48('19000000020000003600000003000000020000004b000000')
            Unknown48('19000000020000003700000018000000020000004b000000')
            if SLOT_51:
                Unknown59('16000000640000001900000064000000')
                if (SLOT_0 < 120000):
                    if (not SLOT_132):
                        if SLOT_53:
                            clearUponHandler(3)
                            if Unknown42('bma'):
                                Unknown36(22)
                                SFX_4('bma160_1')
                                GFX_1('kief_spkaifuku', 104)
                                Unknown21000(1250)
                                Unknown2068(2500)
                                Unknown35()
                            else:
                                Unknown36(22)
                                GFX_1('kief_spkaifuku', 104)
                                Unknown21001(-2500)
                                ConsumeSuperMeter(-5000)
                                Unknown35()
                            SFX_3('distortion_a')
                            Unknown13(25)
                if SLOT_158:
                    Unknown59('03000000640000001900000064000000')
                    if (SLOT_0 < 120000):
                        if (not Unknown48('190000000200000000000000160000000200000084000000')):
                            if SLOT_IsInOverdrive2:
                                clearUponHandler(3)
                                GFX_1('kief_spkaifuku', 100)
                                Unknown36(3)
                                Unknown21001(-2500)
                                ConsumeSuperMeter(-5000)
                                Unknown35()
                                SFX_3('distortion_a')
                                Unknown13(25)
                else:
                    Unknown59('18000000640000001900000064000000')
                    if (SLOT_0 < 120000):
                        if (not Unknown48('190000000200000000000000160000000200000084000000')):
                            if SLOT_55:
                                clearUponHandler(3)
                                GFX_1('kief_spkaifuku', 104)
                                if PartnerChar('bma'):
                                    Unknown36(24)
                                    SFX_4('bma160_1')
                                    GFX_1('kief_spkaifuku', 104)
                                    Unknown21000(1250)
                                    Unknown2068(2500)
                                    Unknown35()
                                else:
                                    Unknown36(24)
                                    Unknown21001(-2500)
                                    ConsumeSuperMeter(-5000)
                                    Unknown35()
                                SFX_3('distortion_a')
                                Unknown13(25)
    sprite('vr_ki205_buttaix01', 32767)	# 1-32767
    label(5)
    sprite('vr_ki205_buttaix00', 30)	# 32768-32797
    GFX_1('kief_205jimen_s', 100)
    GFX_0('Item_buttaixeff', 100)
    Unknown38(4, 1)
    setGravity(1800)
    YAccel(-10)
    Unknown1019(15)
    sendToLabelUpon(2, 6)
    label(6)
    sprite('vr_ki205_buttaix00ex', 2)	# 32798-32799	 **attackbox here**
    GFX_1('kief_205jimen_s', 100)
    Unknown23119(-11206571, 9, 20)
    YAccel(0)
    Unknown1019(0)
    Unknown2034(0)
    Unknown2053(0)
    sprite('vr_ki205_buttaix00ex', 480)	# 32800-33279	 **attackbox here**
    SLOT_51 = 1
    sprite('vr_ki205_buttaix00', 16)	# 33280-33295
    clearUponHandler(3)
    Unknown3004(-20)
    label(10)
    sprite('vr_ki205_buttaix00', 14)	# 33296-33309
    Unknown23029(4, 5110, 0)
    Unknown3004(-20)

@State
def Item_buttaixeff():

    def upon_IMMEDIATE():
        GFX_2('kief_205buttaix')
        Unknown4007(2)
        Unknown3001(0)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 5110):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown3004(15)
    label(0)
    sprite('null', 30)	# 32768-32797
    Unknown3004(-9)

@State
def Item_fusenbomb():

    def upon_IMMEDIATE():
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        physicsYImpulse(50000)
        physicsXImpulse(3700)
        clearUponHandler(43)
        clearUponHandler(2)

        def upon_43():
            if (SLOT_48 == 5111):
                physicsXImpulse(6500)
            if (SLOT_48 == 5112):
                physicsXImpulse(1000)

        def upon_53():
            Unknown13(25)
    sprite('vr_ki205_fusenbomb01', 40)	# 1-40
    GFX_0('Item_fusenbomb_hibana', 0)
    sprite('vr_ki205_fusenbomb01', 3)	# 41-43
    GFX_0('Item_fusenbomb_rakka', 0)
    Unknown3004(-100)

@State
def Item_fusenbomb_rakka():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(3500)
        Hitstop(0)
        AirUntechableTime(120)
        AirPushbackY(50000)
        AirPushbackX(16000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        ProjectileDurabilityLvl(2)
        Unknown9017(1)
        callSubroutine('ItemColor')
        teleportRelativeX(30000)
        Unknown23033(-5)
        physicsXImpulse(100)
        physicsYImpulse(-1300)
        setGravity(5)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_23 < 650000):
                sendToLabel(5)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                Unknown13(25)

        def upon_53():
            Unknown13(25)
    sprite('vr_ki205_fusenbomb00', 32767)	# 1-32767
    GFX_0('Item_fusenbomb_hibana', 0)
    Unknown48('190000000200000053000000160000000200000053000000')
    label(5)
    sprite('vr_ki205_fusenbomb00', 200)	# 32768-32967
    clearUponHandler(3)
    Unknown23119(-1, 8, 24)
    SFX_3('ku008')

    def upon_CLEAR_OR_EXIT():
        if (SLOT_20 <= 350000):
            if (SLOT_19 <= 100000):
                sendToLabel(6)
        if (SLOT_23 <= 50000):
            sendToLabel(6)
    label(6)
    sprite('vr_ki205_fusenbomb02', 11)	# 32968-32978	 **attackbox here**
    clearUponHandler(3)
    ScreenShake(15000, 15000)
    RefreshMultihit()
    GFX_1('kief_205fusenbomb', 100)
    Unknown23118(-32768)
    Unknown1099(30)
    Unknown3004(-40)
    SFX_3('bomb_m')

@State
def Item_fusenbomb_hibana():

    def upon_IMMEDIATE():
        GFX_2('kief_205doronhibana')
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767

@State
def Item_drumkan():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(300)
        Unknown11092(1)
        AirUntechableTime(33)
        hitstun(30)
        blockstun(13)
        Hitstop(0)
        PushbackX(16500)
        AirPushbackX(5500)
        AirPushbackY(-8000)
        Unknown53(1)
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(4)
        sendToLabelUpon(54, 580)

        def upon_53():
            clearUponHandler(53)
            Unknown23090(25)
    sprite('vr_ki205_drumkan00', 32767)	# 1-32767	 **attackbox here**
    RefreshMultihit()
    Unknown1078(-4000, -6000)
    label(4)
    sprite('vr_ki205_drumkan00ex', 32767)	# 32768-65534	 **attackbox here**
    clearUponHandler(2)
    clearUponHandler(10)
    GFX_1('kief_205jimen_l', 100)
    physicsYImpulse(23000)
    physicsXImpulse(6400)
    setGravity(1400)
    Unknown1074(10000)
    AirPushbackY(25000)
    hitstun(17)
    Unknown9190(1)
    Unknown9118(5)
    SFX_3('ku017')

    def upon_LANDING():
        sendToLabel(6)
    label(5)
    sprite('vr_ki205_drumkan00ex', 32767)	# 65535-98301	 **attackbox here**
    Unknown2053(0)
    Unknown2034(0)
    clearUponHandler(2)
    clearUponHandler(10)
    GFX_1('kief_205jimen_l', 100)
    RefreshMultihit()
    physicsYImpulse(23000)
    physicsXImpulse(6400)
    setGravity(1400)
    Unknown1074(10000)
    AirPushbackY(25000)
    hitstun(17)
    Unknown9190(1)
    Unknown9118(5)
    SFX_3('ku017')

    def upon_LANDING():
        sendToLabel(6)
    label(6)
    sprite('vr_ki205_drumkan01', 4)	# 98302-98305	 **attackbox here**

    def upon_CLEAR_OR_EXIT():

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = (SLOT_51 + 1)
        if (SLOT_51 >= 8):
            Unknown23090(25)
    RefreshMultihit()
    Unknown1074(0)
    Unknown1072(0)
    physicsXImpulse(7000)
    Unknown2053(0)
    Unknown2034(0)
    label(0)
    sprite('vr_ki205_drumkan02', 4)	# 98306-98309
    SFX_3('ku007')
    sprite('vr_ki205_drumkan03', 4)	# 98310-98313
    sprite('vr_ki205_drumkan04', 4)	# 98314-98317	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ki205_drumkan05', 4)	# 98318-98321
    sprite('vr_ki205_drumkan06', 4)	# 98322-98325
    sprite('vr_ki205_drumkan01', 4)	# 98326-98329	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ki205_drumkan01', 16)	# 98330-98345	 **attackbox here**
    clearUponHandler(3)
    clearUponHandler(10)
    Unknown3004(-20)
    DisableAttackRestOfMove()
    loopRest()
    ExitState()
    label(580)
    sprite('vr_ki205_drumkan00', 20)	# 98346-98365	 **attackbox here**
    DisableAttackRestOfMove()
    SFX_3('ku017')
    Unknown1074(12000)
    Unknown1084(1)
    physicsXImpulse(-3000)
    physicsYImpulse(30000)
    setGravity(2000)
    Unknown3032()
    Unknown3004(-10)
    sprite('vr_ki205_drumkan00', 30)	# 98366-98395	 **attackbox here**
    loopRest()
    ExitState()

@State
def Item_rockethanabi():

    def upon_IMMEDIATE():
        Unknown23067('kief_205rockethanabi')
        Unknown2009()
        AttackLevel_(3)
        Hitstop(0)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9021(1)
        Unknown9017(1)
        Unknown53(1)
        callSubroutine('ItemColor')
        Unknown23015(3)
        sendToLabelUpon(11, 10)
        sendToLabelUpon(44, 10)
        sendToLabelUpon(46, 10)

        def upon_CLEAR_OR_EXIT():
            if (not SLOT_2):
                Unknown23046('00000000')
                if (SLOT_23 > SLOT_0):
                    Unknown2037(10)
                    YAccel(-100)
                    Unknown1108(0)
            if SLOT_2:
                Unknown2038(-1)

        def upon_5():
            teleportRelativeX(30000)
            YAccel(-100)
            Unknown1108(0)
        GFX_0('Rocketfiresmoke', 100)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                clearUponHandler(45)
                clearUponHandler(2)
                clearUponHandler(53)
                Unknown13(25)

        def upon_53():
            Unknown13(25)
    sprite('vr_ki205_rockethanabi00', 3)	# 1-3	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(44000)
    physicsXImpulse(17000)
    Unknown1108(0)
    SFX_3('ku015')
    label(0)
    sprite('vr_ki205_rockethanabi00', 3)	# 4-6	 **attackbox here**
    gotoLabel(0)
    label(10)
    sprite('vr_ki205_rockethanabi00', 10)	# 7-16	 **attackbox here**
    DisableAttackRestOfMove()
    GFX_1('kief_205itemhit', 100)
    Unknown23118(-32768)
    Unknown1099(70)
    Unknown3004(-50)

@State
def Rocketfiresmoke():

    def upon_IMMEDIATE():
        Unknown53(1)
        Unknown4007(2)
        Unknown4010(2)
    label(1)
    sprite('null', 1)	# 1-1
    GFX_1('kief_205rocketsmoke', 100)
    loopRest()
    gotoLabel(1)

@State
def Item_dryice():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)

        def upon_44():
            Hitstop(48)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        PushbackX(3000)
        AirUntechableTime(60)
        YImpluseBeforeWallbounce(1200)
        AirPushbackY(19500)
        Unknown9019(1)
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        Unknown23015(3)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            clearUponHandler(2)
            Unknown23029(4, 5110, 0)
            GFX_1('ef_jizoku_ice', 100)
            GFX_1('ef_jizoku_ice', 100)
            GFX_1('ef_jizoku_ice', 100)
            Unknown13(25)
    sprite('vr_ki205_dryice01', 32767)	# 1-32767	 **attackbox here**
    GFX_0('Item_dryiceeff', 100)
    Unknown38(4, 1)
    RefreshMultihit()
    SFX_3('ku016')
    label(5)
    sprite('vr_ki205_dryice00', 14)	# 32768-32781	 **attackbox here**
    GFX_1('kief_205jimen_s', 100)
    YAccel(-15)
    Unknown1019(15)
    setGravity(1800)
    Unknown2034(0)
    Unknown2053(0)
    sprite('vr_ki205_dryice00ex', 60)	# 32782-32841	 **attackbox here**
    YAccel(0)
    Unknown1019(0)
    sprite('vr_ki205_dryice00', 16)	# 32842-32857	 **attackbox here**
    sprite('keep', 10)	# 32858-32867
    Unknown23090(25)
    label(10)
    sprite('keep', 14)	# 32868-32881
    Unknown3004(-30)
    Unknown3032()
    Unknown13(25)

@State
def Item_dryiceeff():

    def upon_IMMEDIATE():
        GFX_2('kief_205dryice')
        Unknown4007(2)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 5110):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown3004(15)
    label(0)
    sprite('null', 30)	# 32768-32797
    Unknown3004(-9)

@State
def Item_dorondama():

    def upon_IMMEDIATE():
        Unknown53(2)
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)
        GFX_0('Item_dorondamahibana', 100)
        Unknown38(4, 1)
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')

        def upon_54():
            Unknown13(25)
    sprite('vr_ki205_dorondama00', 32767)	# 1-32767
    label(5)
    sprite('vr_ki205_dorondama00', 20)	# 32768-32787
    GFX_1('kief_205jimen_s', 100)
    YAccel(-15)
    Unknown1019(15)
    sprite('vr_ki205_dorondama00', 200)	# 32788-32987
    Unknown2034(0)
    Unknown2053(0)
    ScreenShake(5000, 5000)
    Unknown23029(4, 5110, 0)
    Unknown3004(-20)
    GFX_0('Item_dorondamaeff', 100)
    GFX_1('kief_205fusenbomb02', 100)
    YAccel(0)
    Unknown1019(0)

@State
def Item_dorondamahibana():

    def upon_IMMEDIATE():
        GFX_2('kief_205doronhibana')
        Unknown4007(2)
        Unknown4006(2)
        Unknown53(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 5110):
                sendToLabel(0)

        def upon_53():
            clearUponHandler(45)
            clearUponHandler(53)
            sendToLabel(0)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                clearUponHandler(53)
                clearUponHandler(45)
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 20)	# 32768-32787
    Unknown3004(-15)

@State
def Item_dorondamaeff():

    def upon_IMMEDIATE():
        Unknown23015(4)
        GFX_2('kief_205dorondama')
        Unknown4007(2)
        Unknown3001(0)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                clearUponHandler(53)
                clearUponHandler(45)
                sendToLabel(0)

        def upon_53():
            clearUponHandler(45)
            clearUponHandler(53)
            sendToLabel(0)
    sprite('null', 170)	# 1-170
    SFX_3('bomb_m')
    Unknown3004(15)
    label(0)
    sprite('null', 30)	# 171-200
    Unknown3004(-9)

@State
def Item_muscledrink():

    def upon_IMMEDIATE():
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        Unknown23022(1)
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)
        Unknown23015(3)

        def upon_54():
            Unknown13(25)

        def upon_CLEAR_OR_EXIT():
            Unknown48('19000000020000003500000016000000020000004b000000')
            Unknown48('19000000020000003600000003000000020000004b000000')
            Unknown48('19000000020000003700000018000000020000004b000000')
            if SLOT_51:
                Unknown59('16000000640000001900000064000000')
                if (SLOT_0 < 120000):
                    if (not SLOT_132):
                        if SLOT_53:
                            clearUponHandler(3)
                            Unknown36(22)
                            GFX_1('kief_spkaifuku', 104)
                            Unknown21000(2000)
                            Unknown30029(2000)
                            Unknown35()
                            SFX_3('distortion_a')
                            Unknown13(25)
                if SLOT_158:
                    Unknown59('03000000640000001900000064000000')
                    if (SLOT_0 < 120000):
                        if (not Unknown48('190000000200000000000000160000000200000084000000')):
                            if SLOT_158:
                                if SLOT_IsInOverdrive2:
                                    clearUponHandler(3)
                                    GFX_1('kief_spkaifuku', 104)
                                    Unknown36(3)
                                    Unknown21000(2000)
                                    Unknown30029(2000)
                                    Unknown35()
                            elif SLOT_55:
                                clearUponHandler(3)
                                GFX_1('kief_spkaifuku', 104)
                                Unknown36(24)
                                Unknown21000(2000)
                                Unknown30029(2000)
                                Unknown35()
                            SFX_3('distortion_a')
                            Unknown13(25)
                else:
                    Unknown59('18000000640000001900000064000000')
                    if (SLOT_0 < 120000):
                        if (not Unknown48('190000000200000000000000160000000200000084000000')):
                            if SLOT_55:
                                clearUponHandler(3)
                                GFX_1('kief_spkaifuku', 104)
                                Unknown36(24)
                                Unknown21000(2000)
                                Unknown30029(2000)
                                Unknown35()
                                SFX_3('distortion_a')
                                Unknown13(25)
    sprite('vr_ki205_muscledrink00', 32767)	# 1-32767
    label(5)
    sprite('vr_ki205_muscledrink00', 30)	# 32768-32797
    GFX_1('kief_205jimen_s', 100)
    setGravity(1800)
    YAccel(-10)
    Unknown1019(15)
    sendToLabelUpon(2, 6)
    if SLOT_56:
        SLOT_51 = 1
    label(6)
    sprite('vr_ki205_muscledrink00', 2)	# 32798-32799
    GFX_1('kief_205jimen_s', 100)
    YAccel(0)
    Unknown1019(0)
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_56:
        SLOT_51 = 1
    sprite('vr_ki205_muscledrink00', 18)	# 32800-32817
    SLOT_51 = 1
    sprite('vr_ki205_muscledrink00', 160)	# 32818-32977
    Unknown23119(-1, 8, 2)
    sprite('vr_ki205_muscledrink00', 160)	# 32978-33137
    Unknown23119(-1, 8, 2)
    sprite('vr_ki205_muscledrink00', 160)	# 33138-33297
    Unknown23119(-1, 8, 2)
    sprite('vr_ki205_muscledrink00', 16)	# 33298-33313
    clearUponHandler(3)
    Unknown3004(-20)

@State
def Item_kazaguruma():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(2)
        Damage(650)
        Unknown11092(1)
        AirPushbackX(20000)
        AirPushbackY(30000)
        PushbackX(35000)
        AirUntechableTime(20)
        Hitstop(0)
        Unknown9016(1)
        callSubroutine('ItemColor')
        physicsYImpulse(34000)
        physicsXImpulse(24000)
        setGravity(1400)
        Unknown1028(-300)
        Unknown23015(3)
        Unknown3029(1)
        Unknown3069(1)
        Unknown3070(3)
        Unknown3071(4)
        Unknown3072('ff000000ff000000ff000000ff000000')
        Unknown3073('00000000ff000000ff000000ff000000')

        def upon_44():
            sendToLabel(0)

        def upon_43():
            if (SLOT_48 == 5111):
                physicsXImpulse(38000)
            if (SLOT_48 == 5112):
                physicsXImpulse(24000)
                setGravity(1400)
        sendToLabelUpon(2, 0)
        loopRelated(17, 45)

        def upon_17():
            sendToLabel(5)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                clearUponHandler(45)
                clearUponHandler(53)
                Unknown23090(25)

        def upon_53():
            clearUponHandler(45)
            clearUponHandler(53)
            Unknown23090(25)

        def upon_54():
            Unknown13(25)
    label(10)
    sprite('vr_ki205_kazaguruma00', 3)	# 1-3	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('vr_ki205_kazaguruma01', 3)	# 4-6	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    sprite('vr_ki205_kazaguruma02', 3)	# 7-9	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    RefreshMultihit()
    sprite('vr_ki205_kazaguruma00', 3)	# 10-12	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    SFX_3('slash_knife_slow')
    sprite('vr_ki205_kazaguruma01', 3)	# 13-15	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    RefreshMultihit()
    sprite('vr_ki205_kazaguruma02', 3)	# 16-18	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    loopRest()
    gotoLabel(10)
    label(5)
    sprite('vr_ki205_kazaguruma00', 3)	# 19-21	 **attackbox here**
    Unknown1028(-3300)
    GFX_1('kief_205kazaguruma', 100)
    RefreshMultihit()
    Unknown1019(75)
    YAccel(80)
    AirPushbackX(20000)
    setGravity(1100)
    Unknown11099(1)
    SFX_3('slash_knife_slow')
    sprite('vr_ki205_kazaguruma01', 3)	# 22-24	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    Unknown1019(75)
    YAccel(80)
    sprite('vr_ki205_kazaguruma02', 3)	# 25-27	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    RefreshMultihit()
    Unknown1019(75)
    YAccel(80)
    sprite('vr_ki205_kazaguruma00', 3)	# 28-30	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    Unknown1019(75)
    YAccel(80)
    SFX_3('slash_knife_slow')
    sprite('vr_ki205_kazaguruma01', 3)	# 31-33	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    RefreshMultihit()
    Unknown1019(75)
    YAccel(80)
    sprite('vr_ki205_kazaguruma02', 3)	# 34-36	 **attackbox here**
    GFX_1('kief_205kazaguruma', 100)
    Unknown1019(75)
    YAccel(80)
    loopRest()
    gotoLabel(5)
    label(0)
    sprite('null', 1)	# 37-37
    GFX_1('kief_205kazaguruma', 100)
    DisableAttackRestOfMove()
    Unknown3029(0)
    GFX_1('kief_205itemhit', 100)
    Unknown3004(-60)

@State
def Item_denden():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(1000)
        Unknown11092(1)
        Hitstop(0)
        PushbackX(0)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(50)
        Hitstop(0)
        Unknown11001(25, 15, 15)
        AirPushbackY(9500)
        YImpluseBeforeWallbounce(2500)
        Unknown9310(10)
        Unknown11044(1)
        Unknown9021(1)
        Unknown9018(1)
        ProjectileDurabilityLvl(2)
        PushbackX(0)
        Unknown53(0)
        callSubroutine('ItemColor')
        callSubroutine('ItemParam')
        physicsYImpulse(34000)
        physicsXImpulse(6500)
        setGravity(1600)
        Unknown23015(3)

        def upon_54():
            Unknown13(25)
    sprite('vr_ki205_denden01', 5)	# 1-5
    label(10)
    sprite('vr_ki205_denden02', 5)	# 6-10
    sprite('vr_ki205_denden03', 5)	# 11-15
    sprite('vr_ki205_denden01', 5)	# 16-20
    loopRest()
    gotoLabel(10)
    label(5)
    sprite('vr_ki205_denden00', 14)	# 21-34
    GFX_1('kief_205jimen_s', 100)
    YAccel(-15)
    Unknown1019(15)
    setGravity(1800)
    Unknown2053(0)
    Unknown2034(0)
    sprite('vr_ki205_denden00', 1)	# 35-35
    YAccel(0)
    Unknown1019(0)
    sprite('vr_ki205_denden00', 15)	# 36-50
    GFX_1('kief_205dendentarget', 100)
    Unknown23119(-1, 8, 2)
    sprite('vr_ki205_denden00ex', 6)	# 51-56	 **attackbox here**
    Unknown23119(-1, 10, 2)
    RefreshMultihit()
    GFX_1('kief_205denden', 100)
    SFX_3('thunder_s')
    sprite('vr_ki205_denden00ex', 6)	# 57-62	 **attackbox here**
    Unknown23119(-1, 10, 2)
    RefreshMultihit()
    GFX_1('kief_205denden', 100)
    SFX_3('thunder_s')
    sprite('vr_ki205_denden00ex', 6)	# 63-68	 **attackbox here**
    Unknown23119(-1, 10, 2)
    RefreshMultihit()
    GFX_1('kief_205denden', 100)
    SFX_3('thunder_s')
    sprite('vr_ki205_denden00ex', 4)	# 69-72	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3004(-70)

@Subroutine
def OkeStack():
    Unknown23029(6, 5120, 0)
    if Unknown46(5):
        Unknown38(6, 5)
    if Unknown46(4):
        Unknown38(5, 4)

@State
def Item_okemaster():

    def upon_IMMEDIATE():
        Unknown2035(1)

        def upon_43():
            if (SLOT_48 == 5120):
                Unknown23090(25)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                clearUponHandler(45)
                clearUponHandler(53)
                Unknown23090(25)

        def upon_53():
            clearUponHandler(45)
            clearUponHandler(53)
            Unknown23090(25)

        def upon_54():
            Unknown13(25)
    sprite('null', 70)	# 1-70
    GFX_0('Oke_throw', 100)
    sprite('null', 20)	# 71-90
    Unknown1086(22)
    if Unknown23166('CmnActChangePartnerIn'):
        Unknown23032(50)
    teleportRelativeX(-1575000)
    Unknown23033(-55)
    GFX_0('Oke_meteo', 100)
    teleportRelativeX(325000)
    GFX_0('Oke_meteo', 100)
    teleportRelativeX(325000)
    GFX_0('Oke_meteo', 100)
    teleportRelativeX(325000)
    GFX_0('Oke_meteo', 100)
    sprite('null', 20)	# 91-110
    teleportRelativeX(-650000)
    GFX_0('Oke_meteo', 100)
    teleportRelativeX(325000)
    GFX_0('Oke_meteo', 100)
    teleportRelativeX(325000)
    GFX_0('Oke_meteo', 100)
    sprite('null', 20)	# 111-130
    teleportRelativeX(-195000)
    GFX_0('Oke_meteo', 100)
    teleportRelativeX(325000)
    GFX_0('Oke_meteo', 100)
    sprite('null', 180)	# 131-310

@State
def Oke_throw():

    def upon_IMMEDIATE():
        callSubroutine('ItemColor')
        Unknown4010(2)
        physicsYImpulse(35000)
        physicsXImpulse(6500)
        Unknown1074(14000)
        Unknown2035(1)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                clearUponHandler(45)
                clearUponHandler(53)
                Unknown23090(25)

        def upon_53():
            clearUponHandler(45)
            clearUponHandler(53)
            Unknown23090(25)

        def upon_54():
            Unknown13(25)
    sprite('vr_ki205_oke00', 70)	# 1-70
    sprite('vr_ki205_oke00', 15)	# 71-85
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 86-100
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 101-115
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 116-130
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 131-145
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 146-160
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 161-175
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 176-190
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 191-205
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 206-220
    SFX_3('bound_wood_m')
    sprite('vr_ki205_oke00', 15)	# 221-235
    SFX_3('bound_wood_m')

@State
def Oke_meteo():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(2)
        AttackLevel_(3)
        ProjectileDurabilityLvl(2)
        Damage(700)
        AttackP2(95)
        MinimumDamagePct(0)
        Unknown9021(1)
        Hitstop(0)
        Unknown11001(0, 10, 10)
        hitstun(30)
        AirUntechableTime(60)
        AirPushbackX(1800)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(1200)
        AirHitstunAnimation(13)
        blockstun(5)
        PushbackX(7920)
        Unknown9017(1)
        Unknown11084(1)
        Unknown23182(2)
        Unknown11092(1)
        Unknown2035(1)
        callSubroutine('ItemColor')
        Unknown3031()
        Unknown23015(3)
        Unknown53(0)
        physicsYImpulse(-10000)
        physicsXImpulse(10000)
        Unknown1074(14000)
        Unknown11044(0)
        sendToLabelUpon(2, 0)
        sendToLabelUpon(11, 0)

        def upon_45():
            Unknown48('19000000020000003a0000000300000002000000aa000000')
            if SLOT_58:
                Unknown23090(25)

        def upon_53():
            Unknown13(25)

        def upon_54():
            Unknown13(25)
    sprite('vr_ki205_oke01', 32767)	# 1-32767	 **attackbox here**
    RefreshMultihit()
    GFX_0('Meteoeff', 100)
    label(0)
    sprite('vr_ki205_oke01', 10)	# 32768-32777	 **attackbox here**
    GFX_1('kief_205itemhit', 100)
    ScreenShake(5000, 5000)
    Unknown23118(-32768)
    Unknown1099(70)
    Unknown3004(-50)

@State
def Meteoeff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('kief_205okemeteo')
        Unknown2035(1)
        physicsYImpulse(-10000)
        physicsXImpulse(10000)
    label(0)
    sprite('null', 6)	# 1-6
    GFX_1('kief_205okemeteo_add', 100)
    gotoLabel(0)

@State
def IchigekiCamera():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2053(0)

        def upon_43():
            if (SLOT_48 == 7011):
                sendToLabel(0)
    sprite('keep', 32767)	# 1-32767
    teleportRelativeX(500000)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(0)
    sprite('keep', 32767)	# 32768-65534
    Unknown1000(0)
    Unknown20003(0)
    Unknown20001(1)

@State
def __450Kemuri():

    def upon_IMMEDIATE():
        Unknown23015(4)
        GFX_2('kuef_toranporin')
        Unknown3001(255)
        Unknown1096(2000)
    sprite('null', 10)	# 1-10
    physicsXImpulse(-8000)
    physicsYImpulse(8000)
    sprite('null', 30)	# 11-40
    Unknown3004(-10)

@State
def __450uchiage():

    def upon_IMMEDIATE():
        Unknown23067('kief_450rocketsmoke')
        Unknown4007(2)
    sprite('null', 300)	# 1-300
    sprite('null', 10)	# 301-310
    Unknown3004(-26)

@State
def Hanabidama():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown3032()
        GFX_0('Hanabihibana', 0)
        Unknown38(4, 1)
        Unknown2019(-1000)
    sprite('vr_ku450_00', 5)	# 1-5
    sprite('vr_ku450_01', 43)	# 6-48	 **attackbox here**
    physicsYImpulse(18000)
    physicsXImpulse(12000)
    setGravity(1000)
    sprite('vr_ku450_00', 1)	# 49-49
    Unknown23029(4, 7001, 0)
    Unknown3004(-255)

@State
def Hanabihibana():

    def upon_IMMEDIATE():
        GFX_2('kief_450hibana')
        Unknown4007(2)
        Unknown4010(2)
        Unknown2019(-1000)
        Unknown1096(1600)

        def upon_43():
            if (SLOT_48 == 7001):
                sendToLabel(1)
    sprite('null', 7)	# 1-7
    SFX_3('ku008')
    sprite('null', 7)	# 8-14
    SFX_3('ku008')
    sprite('null', 7)	# 15-21
    SFX_3('ku008')
    sprite('null', 32767)	# 22-32788
    label(1)
    sprite('null', 1)	# 32789-32789
    Unknown3004(-255)

@State
def __450cutinsmoke():

    def upon_IMMEDIATE():
        Unknown23067('kief_450cutinsmoke')
        Unknown1007(100000)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    sprite('null', 200)	# 21-220
    Unknown3004(6)
    sprite('null', 26)	# 221-246
    Unknown3004(-10)

@State
def Cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('6b7565663435305f637574696e62672e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown23015(2)
        Unknown2007()
        Unknown3001(0)
    sprite('null', 150)	# 1-150
    Unknown3004(10)
    sprite('null', 70)	# 151-220
    Unknown3004(-4)

@State
def IchigekiPictureA():

    def upon_IMMEDIATE():
        Unknown6001(1)
        Unknown2007()
        Unknown23015(4)
        Unknown3032()
        Unknown3001(0)
        Unknown1096(900)
        Unknown1000(100000)
        teleportRelativeY(70000)
    sprite('ichigeki0', 130)	# 1-130
    Unknown3004(10)
    sprite('ichigeki0', 70)	# 131-200
    Unknown23119(60, 30, 1)
    Unknown3004(-4)

@State
def IchigekiPictureB():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown6001(1)
        Unknown2007()
        Unknown23015(2)
        Unknown3032()
        Unknown3001(0)
        Unknown1096(850)
        Unknown1000(-520000)
        teleportRelativeY(20000)
    sprite('ichigeki1', 25)	# 1-25
    Unknown3004(7)
    sprite('ichigeki1', 135)	# 26-160
    Unknown3004(0)
    sprite('ichigeki1', 70)	# 161-230
    Unknown23119(60, 30, 1)
    Unknown3004(-4)

@State
def __450kintokirocket():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown6001(1)
        Unknown23015(2)
        Unknown3032()
        Unknown3001(0)
        if SLOT_38:
            Unknown1000(-485000)
            teleportRelativeY(48000)
        else:
            Unknown1000(440000)
            teleportRelativeY(48000)
        Unknown2007()
        physicsXImpulse(-2400)
        Unknown1099(-6)
    sprite('vr_ku450_02', 70)	# 1-70
    Unknown3004(30)
    sprite('vr_ku450_02', 68)	# 71-138
    sprite('vr_ku450_02', 17)	# 139-155
    Unknown3004(-15)

@State
def __450cutinsmoke():

    def upon_IMMEDIATE():
        Unknown23067('kief_450cutinsmoke')
        Unknown1007(100000)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    sprite('null', 200)	# 21-220
    Unknown3004(6)
    sprite('null', 26)	# 221-246
    Unknown3004(-10)

@State
def __450rocketsmoke():

    def upon_IMMEDIATE():
        Unknown23067('kief_450upsmoke')
        Unknown2007()
        Unknown1096(1300)
        Unknown1108(0)
        teleportRelativeX(7000)
        physicsYImpulse(5000)
        physicsXImpulse(-1600)
        Unknown3001(0)
        Unknown1099(-6)
    sprite('null', 20)	# 1-20
    sprite('null', 90)	# 21-110
    Unknown3004(6)
    sprite('null', 17)	# 111-127
    Unknown3004(-15)

@State
def __450kirari():

    def upon_IMMEDIATE():
        Unknown23067('kief_450rocketflash')
        Unknown4007(2)
        Unknown2007()
        teleportRelativeX(-177000)
    sprite('null', 32767)	# 1-32767
    SFX_3('spsys_g_cancel')

@State
def __450kumahanabi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23067('kief_c450hanabi')
        teleportRelativeY(400000)
        Unknown3001(0)
    sprite('null', 50)	# 1-50
    GFX_0('450joshomain', 100)
    sprite('null', 100)	# 51-150
    GFX_0('450josho_renzoku1', 100)
    GFX_0('450josho_renzoku2', 100)
    sprite('null', 30)	# 151-180
    GFX_0('450kumahanabiface', 100)
    ScreenShake(10000, 10000)
    Unknown3004(25)
    sprite('null', 120)	# 181-300
    GFX_0('450hanabi_r', 100)
    GFX_0('450hanabi_l', 100)
    GFX_0('450hanabiyoin', 100)
    sprite('null', 30)	# 301-330
    Unknown3004(-9)

@State
def __450joshomain():

    def upon_IMMEDIATE():
        Unknown23067('kief_450josho')
        teleportRelativeY(-200000)
        physicsYImpulse(3500)
    sprite('null', 90)	# 1-90
    sprite('null', 10)	# 91-100
    Unknown3004(-26)

@State
def __450kumahanabiface():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6b7565663435305f68616e6162692e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeY(400000)
        Unknown3001(0)
    sprite('null', 100)	# 1-100
    ScreenShake(10000, 10000)
    Unknown3004(25)
    sprite('null', 30)	# 101-130
    Unknown3004(-9)

@State
def __450josho_renzoku1():

    def upon_IMMEDIATE():
        teleportRelativeY(-200000)
        Unknown1026(1500, 3000)
        Unknown23067('kief_450joshosmall1')
        Unknown3001(0)
    sprite('null', 90)	# 1-90
    Unknown3004(25)
    sprite('null', 10)	# 91-100
    Unknown3004(-26)

@State
def __450josho_renzoku2():

    def upon_IMMEDIATE():
        teleportRelativeY(-200000)
        Unknown1026(1500, 3000)
        Unknown23067('kief_450joshosmall2')
        Unknown3001(0)
    sprite('null', 90)	# 1-90
    Unknown3004(25)
    sprite('null', 10)	# 91-100
    Unknown3004(-26)

@State
def __450hanabi_r():

    def upon_IMMEDIATE():
        Unknown23067('kief_a450hanabi')
        Unknown3001(0)
    sprite('null', 2)	# 1-2
    Unknown3004(25)
    SFX_3('ku010')
    sprite('null', 18)	# 3-20
    SFX_3('ku010')
    sprite('null', 2)	# 21-22
    SFX_3('ku010')
    sprite('null', 18)	# 23-40
    SFX_3('ku010')
    sprite('null', 2)	# 41-42
    SFX_3('ku010')
    sprite('null', 8)	# 43-50
    SFX_3('ku010')
    sprite('null', 2)	# 51-52
    SFX_3('ku010')
    sprite('null', 8)	# 53-60
    SFX_3('ku010')
    sprite('null', 2)	# 61-62
    SFX_3('ku010')
    sprite('null', 8)	# 63-70
    SFX_3('ku010')
    sprite('null', 2)	# 71-72
    SFX_3('ku010')
    sprite('null', 8)	# 73-80
    SFX_3('ku010')
    sprite('null', 2)	# 81-82
    SFX_3('ku010')
    sprite('null', 8)	# 83-90
    SFX_3('ku010')
    sprite('null', 10)	# 91-100
    Unknown3004(-26)

@State
def __450hanabi_l():

    def upon_IMMEDIATE():
        Unknown23067('kief_b450hanabi')
        Unknown3001(0)
    sprite('null', 90)	# 1-90
    Unknown3004(25)
    sprite('null', 10)	# 91-100
    Unknown3004(-26)
    SFX_3('bomb_m')

@State
def __450hanabiyoin():

    def upon_IMMEDIATE():
        Unknown23067('kief_450hanabiyoin')
        Unknown3001(0)
    sprite('null', 90)	# 1-90
    Unknown3004(25)
    sprite('null', 10)	# 91-100
    Unknown3004(-26)

@State
def __450hanabiBG():

    def upon_IMMEDIATE():
        teleportRelativeY(400000)
        Unknown3032()
        Unknown4003('6b7565663435305f68616e61626962672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(2)
        Unknown3001(0)
    sprite('null', 300)	# 1-300
    Unknown3004(20)
    sprite('null', 20)	# 301-320
    Unknown3004(-12)

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
    SFX_3('spsys_over_power')
    SFX_3('spsys_over_power')
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

@State
def CrashAura():

    def upon_IMMEDIATE():
        GFX_2('kuef_433aura')
        sendToLabelUpon(54, 0)
        Unknown4009(3)
    sprite('null', 180)	# 1-180
    label(0)
    sprite('null', 1)	# 181-181

@State
def ToujouTVTaiki():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown2019(100)
    sprite('vr_ku600_00', 32767)	# 1-32767
    GFX_0('TVhaikeiA', 100)

@State
def TVhaikeiA():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown4010(2)
        Unknown2019(100)
        GFX_0('TVnoiseA', 100)
    label(0)
    sprite('vr_ku600_05', 3)	# 1-3
    sprite('vr_ku600_06', 3)	# 4-6
    sprite('vr_ku600_07', 3)	# 7-9
    gotoLabel(0)

@State
def TVhaikeiB():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown4010(2)
        Unknown2019(100)
        Unknown3032()
        GFX_0('TVnoiseB', 100)
    sprite('vr_ku600_05', 3)	# 1-3
    sprite('vr_ku600_06', 3)	# 4-6
    sprite('vr_ku600_07', 3)	# 7-9
    sprite('vr_ku600_05', 3)	# 10-12
    sprite('vr_ku600_06', 3)	# 13-15
    Unknown1067(0)
    sprite('vr_ku600_07', 3)	# 16-18
    sprite('vr_ku600_05', 3)	# 19-21
    sprite('vr_ku600_06', 3)	# 22-24
    sprite('vr_ku600_07', 3)	# 25-27
    sprite('vr_ku600_05', 3)	# 28-30
    sprite('vr_ku600_06', 3)	# 31-33
    sprite('vr_ku600_07', 3)	# 34-36
    sprite('vr_ku600_05', 3)	# 37-39
    sprite('vr_ku600_06', 3)	# 40-42
    sprite('vr_ku600_07', 3)	# 43-45
    Unknown3004(-26)
    sprite('vr_ku600_05', 3)	# 46-48
    sprite('vr_ku600_06', 3)	# 49-51
    sprite('vr_ku600_07', 3)	# 52-54

@State
def TVnoiseA():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown4010(2)
        Unknown2019(0)
        Unknown3032()
        Unknown3001(80)
    sprite('vr_ku600_08', 2)	# 1-2
    sprite('vr_ku600_09', 2)	# 3-4
    sprite('vr_ku600_10', 2)	# 5-6
    sprite('vr_ku600_11', 2)	# 7-8
    label(0)
    sprite('vr_ku600_08', 2)	# 9-10
    Unknown3004(0)
    sprite('vr_ku600_09', 2)	# 11-12
    sprite('vr_ku600_10', 2)	# 13-14
    sprite('vr_ku600_11', 2)	# 15-16
    gotoLabel(0)

@State
def TVnoiseB():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown4010(2)
        Unknown2019(0)
        Unknown3032()
        Unknown3001(80)
    sprite('vr_ku600_08', 2)	# 1-2
    sprite('vr_ku600_09', 2)	# 3-4
    sprite('vr_ku600_10', 2)	# 5-6
    sprite('vr_ku600_11', 2)	# 7-8

@State
def ToujouTV():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown2019(100)
    sprite('vr_ku600_00', 50)	# 1-50
    GFX_0('TVhaikeiB', 100)
    sprite('vr_ku600_00', 3)	# 51-53
    physicsYImpulse(3000)
    Unknown1067(10)
    sprite('vr_ku600_00', 6)	# 54-59
    Unknown4045('6b7565665f747668616d6f6e5f636c000000000000000000000000000000000000000000')
    physicsYImpulse(-3000)
    Unknown1067(-5)
    sprite('vr_ku600_00', 30)	# 60-89
    physicsYImpulse(0)
    Unknown1067(0)
    sprite('vr_ku600_01', 4)	# 90-93
    sprite('vr_ku600_02', 4)	# 94-97
    sprite('vr_ku600_03', 4)	# 98-101
    sprite('vr_ku600_04', 4)	# 102-105
    sprite('null', 60)	# 106-165

@State
def TVYugamiLoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sprite('null', 10)	# 1-10
    GFX_0('TVYugami', 100)
    sprite('null', 10)	# 11-20
    GFX_0('TVYugami', 100)
    sprite('null', 10)	# 21-30
    GFX_0('TVYugami', 100)
    sprite('null', 10)	# 31-40
    GFX_0('TVYugami', 100)

@State
def TVYugami():
    sprite('vr_ku600_yugami', 1)	# 1-1
    Unknown4007(2)
    Unknown3032()
    Unknown3057(1)
    Unknown3058(15000)
    Unknown1096(300)
    sprite('vr_ku600_yugami', 20)	# 2-21
    Unknown1099(25)
    Unknown3001(239)
    loopRest()

@State
def Win1():
    sprite('ku032_00', 3)	# 1-3
    physicsXImpulse(-18000)
    Unknown2005()
    Unknown2053(0)
    Unknown2034(0)
    Unknown2035(1)
    sprite('ku032_01', 3)	# 4-6
    sprite('ku032_02', 3)	# 7-9
    sprite('ku032_03', 3)	# 10-12
    sprite('ku032_04', 3)	# 13-15
    Unknown8006(100, 1, 1)
    sprite('ku032_05', 3)	# 16-18
    sprite('ku032_06', 3)	# 19-21
    sprite('ku032_07', 3)	# 22-24
    sprite('ku032_08', 3)	# 25-27
    Unknown8006(100, 1, 1)
    sprite('ku032_01', 3)	# 28-30
    sprite('ku032_02', 3)	# 31-33
    sprite('ku032_03', 3)	# 34-36
    sprite('ku032_04', 3)	# 37-39
    Unknown8006(100, 1, 1)
    sprite('ku032_05', 3)	# 40-42
    sprite('ku032_06', 3)	# 43-45
    sprite('ku032_07', 3)	# 46-48
    sprite('ku032_08', 3)	# 49-51
    Unknown8006(100, 1, 1)
    sprite('ku032_01', 3)	# 52-54
    sprite('ku032_02', 3)	# 55-57
    sprite('ku032_03', 3)	# 58-60
    sprite('ku032_04', 3)	# 61-63
    Unknown8006(100, 1, 1)
    sprite('ku032_05', 3)	# 64-66
    sprite('ku032_06', 3)	# 67-69
    sprite('ku032_07', 3)	# 70-72
    sprite('ku032_08', 3)	# 73-75
    Unknown8006(100, 1, 1)
    Unknown2005()
    sprite('ku032_08', 35)	# 76-110
    Unknown2035(1)
    sprite('ku610_00', 18)	# 111-128
    Unknown23015(1)
    Unknown6001(1)
    if (SLOT_39 == 0):
        teleportRelativeY(-1120000)
        Unknown1000(120000)

        def upon_CLEAR_OR_EXIT():
            Unknown1007(27777)
            teleportRelativeX(22222)
    else:
        teleportRelativeY(-1120000)
        Unknown1000(-1200000)

        def upon_CLEAR_OR_EXIT():
            Unknown1007(27777)
            teleportRelativeX(22222)
    Unknown2019(-4000)
    Unknown1084(1)
    sprite('ku610_00', 10)	# 129-138
    clearUponHandler(3)
    if (SLOT_39 == 0):
        teleportRelativeY(-620000)
        Unknown1000(600000)
    else:
        teleportRelativeY(-620000)
        Unknown1000(-680000)
    sprite('ku610_01', 6)	# 139-144
    sprite('ku610_02', 6)	# 145-150
    SFX_3('ku016')
    sprite('ku610_03', 32767)	# 151-32917
    GFX_0('BigKiraWin', 100)

@State
def BigKiraWin():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
    sprite('vr_ku610_00', 4)	# 1-4
    Unknown6001(1)
    teleportRelativeY(-520000)
    Unknown1000(640000)
    if SLOT_38:
        teleportRelativeY(-520000)
        Unknown1000(-600000)
    Unknown2019(-4000)
    Unknown1084(1)
    Unknown1096(400)
    sprite('vr_ku610_00', 4)	# 5-8
    Unknown1096(800)
    sprite('vr_ku610_00', 4)	# 9-12
    Unknown1096(1000)
    sprite('vr_ku610_00', 4)	# 13-16
    Unknown1096(400)

@State
def KiraKiraWin():

    def upon_IMMEDIATE():
        callSubroutine('ObjectTeamColor')
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('kuef_enterkira_02')
    sprite('null', 32767)	# 1-32767
