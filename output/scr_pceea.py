@Subroutine
def ChargeDamageUp():
    Unknown48('19000000020000004300000003000000020000003b000000')
    if (SLOT_67 == 1):
        Unknown10000(120)
    if (SLOT_67 == 2):
        Unknown10000(200)
    if (SLOT_67 == 3):
        Unknown10000(300)

@Subroutine
def Charge_Count():
    if SLOT_31:
        pass

@State
def PCE_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('5043455f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PCE_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PCE_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PCE_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 600):
            Unknown23185('506572736f6e614d6174636857696e0000000000000000000000000000000000c8000000')
        if (SLOT_48 == 101):
            Unknown23185('5043455f506572736f6e6135430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 201):
            Unknown23185('5043455f506572736f6e6132430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 102):
            Unknown23185('5043455f506572736f6e6135440000000000000000000000000000000000000032000000')
        if (SLOT_48 == 103):
            Unknown23185('5043455f506572736f6e6135423372640000000000000000000000000000000032000000')
        if (SLOT_48 == 104):
            Unknown23185('5043455f506572736f6e6135435f43410000000000000000000000000000000032000000')
        if (SLOT_48 == 105):
            Unknown23185('5043455f506572736f6e6135445f43410000000000000000000000000000000032000000')
        if (SLOT_48 == 106):
            Unknown23185('5043455f506572736f6e61445f48617365695f4341000000000000000000000032000000')
        if (SLOT_48 == 301):
            Unknown23185('5043455f506572736f6e6141697235430000000000000000000000000000000032000000')
        if (SLOT_48 == 302):
            Unknown23185('5043455f506572736f6e6141697234440000000000000000000000000000000032000000')
        if (SLOT_48 == 401):
            Unknown23185('5043455f506572736f6e61447261676f6e4b69636b410000000000000000000032000000')
        if (SLOT_48 == 402):
            Unknown23185('5043455f506572736f6e61447261676f6e4b69636b420000000000000000000032000000')
        if (SLOT_48 == 403):
            Unknown23185('5043455f506572736f6e61447261676f6e4b69636b457800000000000000000032000000')
        if (SLOT_48 == 404):
            Unknown23185('5043455f506572736f6e61416972447261676f6e4b69636b410000000000000032000000')
        if (SLOT_48 == 405):
            Unknown23185('5043455f506572736f6e61416972447261676f6e4b69636b420000000000000032000000')
        if (SLOT_48 == 406):
            Unknown23185('5043455f506572736f6e61416972447261676f6e4b69636b457800000000000032000000')
        if (SLOT_48 == 407):
            Unknown23185('5043455f506572736f6e614b6f6b7574656e67656b694100000000000000000032000000')
        if (SLOT_48 == 408):
            Unknown23185('5043455f506572736f6e614b6f6b7574656e67656b694200000000000000000032000000')
        if (SLOT_48 == 409):
            Unknown23185('5043455f506572736f6e614b6f6b7574656e67656b694578000000000000000032000000')
        if (SLOT_48 == 410):
            Unknown23185('5043455f506572736f6e614b6f6b7574656e67656b695f50530000000000000032000000')
        if (SLOT_48 == 501):
            Unknown23185('5043455f506572736f6e61476f6448616e64000000000000000000000000000064000000')
        if (SLOT_48 == 502):
            Unknown23185('5043455f506572736f6e61476f6448616e644f4400000000000000000000000064000000')
        if (SLOT_48 == 503):
            Unknown23185('5043455f506572736f6e614167756e6579617375746f72615f4661720000000064000000')
        if (SLOT_48 == 504):
            Unknown23185('5043455f506572736f6e614167756e6579617375746f72615f4e65617200000064000000')
        if (SLOT_48 == 505):
            Unknown23185('5043455f506572736f6e614167756e6579617375746f72614f445f466172000064000000')
        if (SLOT_48 == 506):
            Unknown23185('5043455f506572736f6e614167756e6579617375746f72614f445f4e6561720064000000')
        if (SLOT_48 == 513):
            Unknown23185('5043455f506572736f6e61476f6448616e645f44554f0000000000000000000064000000')
        if (SLOT_48 == 514):
            Unknown23185('5043455f506572736f6e61476f6448616e645f44554f4f44000000000000000064000000')
        if (SLOT_48 == 9999):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')
        if (SLOT_48 == 700):
            Unknown23185('5043455f506572736f6e614963686967656b690000000000000000000000000064000000')

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
    Unknown2017(0)
    Unknown30041('')

    def upon_48():
        Unknown23030('7063655f746f6d6f655f73776f726465666600000000000000000000000000000000000030000000000000000400000000000000000000000000000000000000')

@Subroutine
def PCE_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PCE_AttackInit():
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
    callSubroutine('PCE_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PCE_SPAttackInit():
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
    callSubroutine('PCE_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PCE_DDAttackInit():
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
    Unknown11033(0)
    SLOT_11 = 120
    callSubroutine('PCE_ReceptionSignal')
    Unknown23023()

@Subroutine
def PCE_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PCE_ForceWarp():
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
        SFX_0('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PCE_PersonaWait')

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
        callSubroutine('PCE_ReceptionSignal')
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
    Unknown2017(0)
    Unknown1084(1)

@State
def PCE_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c30000b03cffffe09304000000000050c30000')
        callSubroutine('PCE_AttackInit')
        AttackLevel_(4)
        AttackP1(90)
        Unknown9016(1)
        AirUntechableTime(20)
        Unknown9156(27)
        AirPushbackX(11000)
        AirPushbackY(15000)
        PushbackX(25000)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('ChargeDamageUp')
        Unknown23078(1)
        callSubroutine('PCE_CheckWarp')
        Unknown4007(3)
        Unknown2053(1)
    sprite('to204_00', 3)	# 1-3
    Unknown2006()
    sprite('to204_01', 1)	# 4-4
    GFX_0('Zanzoh5C', 100)
    physicsXImpulse(30000)
    sprite('to204_01', 1)	# 5-5
    Unknown1019(60)
    sprite('to204_02', 2)	# 6-7
    Unknown1019(60)
    SFX_3('slash_pole_middle')
    sprite('to204_04', 1)	# 8-8	 **attackbox here**
    Unknown23054('746f3230345f303300000000000000000000000000000000000000000000000003000000')
    Unknown1019(0)
    RefreshMultihit()
    sprite('to204_04', 2)	# 9-10	 **attackbox here**
    Unknown23022(0)
    sprite('to204_05', 3)	# 11-13
    Unknown4007(0)
    Unknown23027()
    sprite('to204_06', 3)	# 14-16
    SFX_3('cloth_l')
    sprite('to204_04', 4)	# 17-20	 **attackbox here**
    sprite('to204_05', 4)	# 21-24
    sprite('to204_06', 4)	# 25-28
    SFX_3('cloth_l')
    sprite('to204_04', 5)	# 29-33	 **attackbox here**
    sprite('to204_05', 5)	# 34-38
    sprite('to204_06', 5)	# 39-43
    sprite('keep', 32767)	# 44-32810
    enterState('PersonaDeleteAndIdling')

@State
def PCE_Persona5C_CA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c30000b03cffffc05c15000000000050c30000')
        callSubroutine('PCE_AttackInit')
        Unknown23078(1)
        callSubroutine('PCE_CheckWarp')
        Unknown4007(3)
        Unknown2053(0)
        Unknown2017(0)
        Unknown23022(1)
        Unknown2003(1)
    sprite('to204_00', 3)	# 1-3
    Unknown2006()
    sprite('to204_01', 1)	# 4-4
    GFX_0('Zanzoh5C', 100)
    physicsXImpulse(30000)
    sprite('to204_01', 1)	# 5-5
    Unknown1019(60)
    sprite('to204_02', 2)	# 6-7
    Unknown1019(60)
    SFX_3('slash_pole_middle')
    sprite('to204_04', 1)	# 8-8	 **attackbox here**
    Unknown23054('746f3230345f303300000000000000000000000000000000000000000000000003000000')
    Unknown1019(0)
    RefreshMultihit()
    sprite('to204_04', 2)	# 9-10	 **attackbox here**
    sprite('to204_05', 3)	# 11-13
    Unknown4007(0)
    Unknown23027()
    sprite('to204_06', 3)	# 14-16
    SFX_3('cloth_l')
    sprite('to204_04', 4)	# 17-20	 **attackbox here**
    sprite('to204_05', 4)	# 21-24
    sprite('to204_06', 4)	# 25-28
    SFX_3('cloth_l')
    sprite('to204_04', 5)	# 29-33	 **attackbox here**
    sprite('to204_05', 5)	# 34-38
    sprite('to204_06', 5)	# 39-43
    SFX_3('cloth_l')
    sprite('to204_04', 4)	# 44-47	 **attackbox here**
    sprite('to204_05', 4)	# 48-51
    sprite('to204_06', 4)	# 52-55
    SFX_3('cloth_l')
    sprite('to204_04', 4)	# 56-59	 **attackbox here**
    sprite('to204_05', 4)	# 60-63
    sprite('to204_06', 4)	# 64-67
    SFX_3('cloth_l')
    sprite('to204_04', 4)	# 68-71	 **attackbox here**
    sprite('to204_05', 4)	# 72-75
    sprite('to204_06', 4)	# 76-79
    SFX_3('cloth_l')
    sprite('to204_04', 4)	# 80-83	 **attackbox here**
    sprite('to204_05', 4)	# 84-87
    sprite('to204_06', 4)	# 88-91
    sprite('keep', 32767)	# 92-32858
    enterState('PersonaDeleteAndIdling')

@State
def PCE_Persona2C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c300006079feffc05c1500b03cffff50c30000')
        callSubroutine('PCE_AttackInit')
        AttackLevel_(4)
        Damage(1100)
        Unknown9016(1)
        Unknown9266(9)
        AirUntechableTime(30)
        AttackP1(90)
        Unknown11092(1)
        Hitstop(1)
        Unknown11001(8, 8, 8)
        AirPushbackX(14000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(2200)
        PushbackX(5000)
        callSubroutine('ChargeDamageUp')
        Unknown23078(1)
        Unknown2053(1)
        callSubroutine('PCE_CheckWarp')

        def upon_ON_HIT_OR_BLOCK():
            Unknown2037(1)
    sprite('to234_00', 3)	# 1-3
    Unknown2006()
    Unknown23015(0)
    Unknown2018(1, 100)
    sprite('to234_01', 2)	# 4-5
    SFX_3('cloth_l')
    physicsXImpulse(30000)
    sprite('to234_02', 2)	# 6-7
    Unknown1019(80)
    sprite('to234_00', 2)	# 8-9
    Unknown1019(80)
    sprite('to234_03', 2)	# 10-11	 **attackbox here**
    Unknown1019(80)
    sprite('to234_04', 2)	# 12-13	 **attackbox here**
    Unknown1019(80)
    sprite('to234_05', 2)	# 14-15	 **attackbox here**
    SFX_3('slash_pole_middle')
    GFX_0('2C_ice', 100)
    Unknown1019(80)
    sprite('to234_07', 1)	# 16-16	 **attackbox here**
    Unknown23054('746f3233345f303600000000000000000000000000000000000000000000000003000000')
    GFX_1('toef_C2', 0)
    Unknown1084(1)
    RefreshMultihit()
    sprite('to234_07', 2)	# 17-18	 **attackbox here**
    Unknown23022(0)
    sprite('to234_07', 6)	# 19-24	 **attackbox here**
    Unknown23027()
    sprite('to234_08', 1)	# 25-25	 **attackbox here**
    GFX_0('Zanzoh2C', 100)
    sprite('to234_08', 2)	# 26-27	 **attackbox here**
    Unknown1019(60)
    RefreshMultihit()
    Hitstop(8)
    Unknown11001(0, 0, 0)
    AirUntechableTime(30)
    AirPushbackX(3000)
    AirPushbackY(22000)
    PushbackX(5000)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    if SLOT_2:
        Unknown21015('4e6d6c41746b3542326e640000000000000000000000000000000000000000004d04000000000000')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21015('4e6d6c41746b3542326e640000000000000000000000000000000000000000004d04000000000000')
    GFX_1('toef_C2', 0)
    GFX_1('toef_C2', 0)
    GFX_1('toef_C2', 1)
    GFX_1('toef_C2', 2)
    GFX_1('toef_C2', 3)
    GFX_1('toef_C2', 4)
    sprite('to234_09', 3)	# 28-30
    Unknown2017(0)
    sprite('to234_10', 3)	# 31-33
    SFX_3('cloth_l')
    sprite('to234_11', 3)	# 34-36
    sprite('to234_09', 3)	# 37-39
    sprite('to234_10', 3)	# 40-42
    SFX_3('cloth_l')
    sprite('to234_11', 3)	# 43-45
    sprite('to234_09', 3)	# 46-48
    sprite('to234_10', 3)	# 49-51
    SFX_3('cloth_l')
    sprite('to234_11', 3)	# 52-54
    sprite('to234_09', 3)	# 55-57
    sprite('to234_10', 3)	# 58-60
    SFX_3('cloth_l')
    sprite('to234_11', 3)	# 61-63
    sprite('keep', 32767)	# 64-32830
    enterState('PersonaDeleteAndIdling')

@State
def PCE_Persona5D():

    def upon_IMMEDIATE():
        Unknown23184('0300000064000000b03cffff50c3000000000000c05c1500b03cffff50c30000')
        callSubroutine('PCE_AttackInit')
        Unknown2009()
        AttackLevel_(4)
        Damage(50)
        PushbackX(20000)
        Unknown30055('400d03004600000046000000')
        AirPushbackY(15000)
        Hitstop(1)
        Unknown9016(1)
        Unknown11092(1)
        Unknown11042(1)
        Unknown4007(3)
        Unknown2053(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to205_00', 8)	# 1-8
    ScreenShake(20000, 0)
    teleportRelativeX(150000)
    sprite('to205_01', 3)	# 9-11
    Unknown4007(0)
    Unknown30032(1)
    physicsXImpulse(34200)
    GFX_0('Zanzoh5D', 100)
    sprite('to205_02', 3)	# 12-14
    Unknown1019(80)
    sprite('to205_03', 3)	# 15-17
    Unknown1019(80)
    sprite('to205_04', 2)	# 18-19
    Unknown1019(80)
    sprite('to205_05', 2)	# 20-21
    Unknown1019(80)
    SFX_3('slash_pole_fast')
    sprite('to205_06', 2)	# 22-23	 **attackbox here**
    Unknown1019(80)
    RefreshMultihit()
    sprite('to205_07', 3)	# 24-26
    Unknown1019(80)
    sprite('to205_08', 2)	# 27-28	 **attackbox here**
    Unknown1019(80)
    RefreshMultihit()
    sprite('to205_09', 2)	# 29-30
    Unknown1019(80)
    sprite('to205_04', 2)	# 31-32
    Unknown1019(80)
    sprite('to205_05', 2)	# 33-34
    Unknown1019(80)
    SFX_3('slash_pole_fast')
    sprite('to205_06', 2)	# 35-36	 **attackbox here**
    Unknown1019(80)
    RefreshMultihit()
    sprite('to205_07', 3)	# 37-39
    Unknown1019(80)
    sprite('to205_10', 3)	# 40-42
    Unknown30033(1)
    SFX_3('slash_pole_slow')
    label(819)
    sprite('to206_00', 3)	# 43-45
    Unknown23027()
    Unknown1084(1)
    sprite('to206_01', 2)	# 46-47	 **attackbox here**
    Damage(50)
    Hitstop(0)
    AirPushbackY(3000)
    PushbackX(5000)
    Unknown9016(1)
    RefreshMultihit()
    GFX_0('Zanzoh5DD', 0)
    sprite('to206_02', 2)	# 48-49	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_fast')

    def upon_ON_HIT_OR_BLOCK():
        Unknown2038(1)
        if op(4, 2, 2, 0, 3):
            Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        else:
            Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('to206_03', 2)	# 50-51	 **attackbox here**
    RefreshMultihit()
    sprite('to206_01', 2)	# 52-53	 **attackbox here**
    RefreshMultihit()
    GFX_0('Zanzoh5DD', 0)
    SFX_3('slash_pole_fast')
    sprite('to206_02', 2)	# 54-55	 **attackbox here**
    RefreshMultihit()
    sprite('to206_03', 2)	# 56-57	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_fast')
    sprite('to206_01', 2)	# 58-59	 **attackbox here**
    RefreshMultihit()
    GFX_0('Zanzoh5DD', 0)
    sprite('to206_02', 2)	# 60-61	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_fast')
    sprite('to206_03', 2)	# 62-63	 **attackbox here**
    RefreshMultihit()
    sprite('to206_01', 2)	# 64-65	 **attackbox here**
    RefreshMultihit()
    GFX_0('Zanzoh5DD', 0)
    SFX_3('slash_pole_fast')
    sprite('to206_02', 2)	# 66-67	 **attackbox here**
    RefreshMultihit()
    sprite('to206_03', 2)	# 68-69	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_fast')
    sprite('to206_01', 2)	# 70-71	 **attackbox here**
    RefreshMultihit()
    GFX_0('Zanzoh5DD', 0)
    sprite('to206_02', 2)	# 72-73	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_fast')
    sprite('to206_03', 2)	# 74-75	 **attackbox here**
    RefreshMultihit()
    sprite('to206_04', 3)	# 76-78
    GFX_0('Zanzoh5DD_2', 100)
    clearUponHandler(10)
    sprite('to206_05', 2)	# 79-80
    sprite('to206_06', 2)	# 81-82
    sprite('to206_07', 2)	# 83-84
    GFX_0('Zanzoh5DD_3', 100)
    SFX_3('slash_pole_middle')
    sprite('to206_09', 3)	# 85-87	 **attackbox here**
    Unknown23054('746f3230365f303800000000000000000000000000000000000000000000000003000000')
    Unknown2017(0)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(200)
    Hitstop(8)
    AirPushbackX(44000)
    AirPushbackY(30000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown9178(1)
    Unknown9346(1)
    AirHitstunAfterWallbounce(15)
    WallbounceReboundTime(0)
    Unknown2017(0)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30055('000000000000000000000000')
    sprite('to206_10', 3)	# 88-90
    Unknown23027()
    sprite('to206_11', 3)	# 91-93
    SFX_3('cloth_l')
    sprite('to206_09', 3)	# 94-96	 **attackbox here**
    sprite('to206_10', 3)	# 97-99
    sprite('to206_11', 3)	# 100-102
    sprite('to206_09', 3)	# 103-105	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to206_10', 3)	# 106-108
    sprite('to206_11', 3)	# 109-111
    sprite('to206_09', 3)	# 112-114	 **attackbox here**
    sprite('to206_10', 3)	# 115-117
    SFX_3('cloth_l')
    sprite('to206_11', 3)	# 118-120
    sprite('to206_09', 3)	# 121-123	 **attackbox here**
    sprite('to206_10', 3)	# 124-126
    sprite('to206_11', 3)	# 127-129
    SFX_3('cloth_l')
    sprite('to206_09', 3)	# 130-132	 **attackbox here**
    sprite('to206_10', 3)	# 133-135
    sprite('to206_11', 3)	# 136-138
    sprite('to206_09', 3)	# 139-141	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to206_10', 3)	# 142-144
    sprite('to206_11', 3)	# 145-147
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 148-32914
    enterState('PersonaDeleteAndIdling')

@State
def PCE_Persona5B3rd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000c05c1500b03cffff50c30000')
        callSubroutine('PCE_SPAttackInit')
        AttackLevel_(4)
        Damage(1000)
        AttackP1(70)
        PushbackX(20000)
        AirPushbackX(0)
        AirPushbackY(15000)
        Unknown30055('b0ad01003200000000000000')
        Hitstop(1)
        Unknown9016(1)
        Unknown11092(1)
        Unknown11042(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('ChargeDamageUp')
        Unknown4007(3)
        Unknown2053(1)
        Unknown2017(1)
        Unknown2006()
        callSubroutine('PCE_CheckWarp')
    sprite('to205_00', 2)	# 1-2
    ScreenShake(20000, 0)
    sprite('to205_01', 2)	# 3-4
    Unknown4007(0)
    Unknown30032(1)
    physicsXImpulse(30000)
    GFX_0('Zanzoh5D_Short', 100)
    sprite('to205_02', 2)	# 5-6
    Unknown1019(60)
    sprite('to205_03', 2)	# 7-8
    Unknown1019(60)
    sprite('to205_04', 2)	# 9-10
    Unknown1019(60)
    sprite('to205_05', 2)	# 11-12
    Unknown1019(60)
    SFX_3('slash_pole_fast')
    sprite('to205_06', 2)	# 13-14	 **attackbox here**
    Unknown1019(60)
    RefreshMultihit()
    sprite('to205_07', 3)	# 15-17
    Unknown1019(60)
    sprite('to205_08', 2)	# 18-19	 **attackbox here**
    Unknown1019(60)
    RefreshMultihit()
    sprite('to205_09', 2)	# 20-21
    Unknown1019(60)
    sprite('to205_10', 3)	# 22-24
    Unknown30033(1)
    SFX_3('slash_pole_slow')
    if SLOT_53:
        sendToLabel(819)
    sprite('to205_11', 1)	# 25-25
    Unknown30033(0)
    physicsXImpulse(20000)
    sprite('to205_11', 1)	# 26-26
    Unknown1019(85)
    sprite('to205_11', 1)	# 27-27
    Unknown1019(85)
    sprite('to205_12', 1)	# 28-28
    Unknown1019(85)
    sprite('to205_12', 1)	# 29-29
    Unknown1019(85)
    sprite('to205_14', 3)	# 30-32	 **attackbox here**
    Unknown23054('746f3230355f313300000000000000000000000000000000000000000000000003000000')
    GFX_0('Zanzoh5D_2', 100)
    RefreshMultihit()
    AttackLevel_(4)
    Unknown9004()
    Hitstop(8)
    AirUntechableTime(60)
    AirPushbackX(5000)
    AirPushbackY(35000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    callSubroutine('ChargeDamageUp')
    Unknown2017(0)
    Unknown1019(0)
    sprite('to205_15', 3)	# 33-35
    Unknown23027()
    sprite('to205_16', 3)	# 36-38
    SFX_3('cloth_l')
    sprite('to205_14', 3)	# 39-41	 **attackbox here**
    sprite('to205_15', 3)	# 42-44
    sprite('to205_16', 3)	# 45-47
    sprite('to205_14', 3)	# 48-50	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to205_15', 3)	# 51-53
    sprite('to205_16', 3)	# 54-56
    sprite('to205_14', 3)	# 57-59	 **attackbox here**
    sprite('to205_15', 3)	# 60-62
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 63-65
    sprite('to205_14', 3)	# 66-68	 **attackbox here**
    sprite('to205_15', 3)	# 69-71
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 72-74
    sprite('to205_14', 3)	# 75-77	 **attackbox here**
    sprite('to205_15', 3)	# 78-80
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 81-83
    sprite('to205_14', 3)	# 84-86	 **attackbox here**
    sprite('to205_15', 3)	# 87-89
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 90-92
    sprite('to205_14', 3)	# 93-95	 **attackbox here**
    sprite('to205_15', 3)	# 96-98
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 99-101
    sprite('to205_14', 3)	# 102-104	 **attackbox here**
    sprite('to205_15', 3)	# 105-107
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 108-110
    sprite('to205_14', 3)	# 111-113	 **attackbox here**
    sprite('to205_15', 3)	# 114-116
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 117-32883
    enterState('PersonaDeleteAndIdling')
    label(819)
    sprite('to206_00', 3)	# 32884-32886
    Unknown23027()
    Unknown1084(1)
    sprite('to206_01', 2)	# 32887-32888	 **attackbox here**
    Damage(100)
    Hitstop(0)
    AirPushbackY(3000)
    PushbackX(5000)
    Unknown9016(1)
    RefreshMultihit()
    GFX_0('Zanzoh5DD', 0)
    sprite('to206_02', 2)	# 32889-32890	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_fast')
    Unknown11055(1)
    sprite('to206_03', 2)	# 32891-32892	 **attackbox here**
    RefreshMultihit()
    sprite('to206_01', 2)	# 32893-32894	 **attackbox here**
    RefreshMultihit()
    GFX_0('Zanzoh5DD', 0)
    SFX_3('slash_pole_fast')
    sprite('to206_02', 2)	# 32895-32896	 **attackbox here**
    RefreshMultihit()
    sprite('to206_03', 2)	# 32897-32898	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_pole_fast')
    sprite('to206_04', 3)	# 32899-32901
    Unknown23015(0)
    Unknown2019(100)
    GFX_0('Zanzoh5DD_2', 100)
    sprite('to206_05', 2)	# 32902-32903
    sprite('to206_06', 2)	# 32904-32905
    sprite('to206_07', 2)	# 32906-32907
    GFX_0('Zanzoh5DD_3', 100)
    SFX_3('slash_pole_middle')
    sprite('to206_09', 3)	# 32908-32910	 **attackbox here**
    Unknown23054('746f3230365f303800000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(200)
    Hitstop(8)
    AirPushbackX(44000)
    AirPushbackY(30000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown9178(1)
    Unknown9346(1)
    AirHitstunAfterWallbounce(15)
    WallbounceReboundTime(0)
    Unknown2017(0)
    Unknown11055(0)
    sprite('to206_10', 3)	# 32911-32913
    Unknown23027()
    sprite('to206_11', 3)	# 32914-32916
    SFX_3('cloth_l')
    sprite('to206_09', 3)	# 32917-32919	 **attackbox here**
    sprite('to206_10', 3)	# 32920-32922
    sprite('to206_11', 3)	# 32923-32925
    sprite('to206_09', 3)	# 32926-32928	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to206_10', 3)	# 32929-32931
    sprite('to206_11', 3)	# 32932-32934
    sprite('to206_09', 3)	# 32935-32937	 **attackbox here**
    sprite('to206_10', 3)	# 32938-32940
    SFX_3('cloth_l')
    sprite('to206_11', 3)	# 32941-32943
    sprite('to206_09', 3)	# 32944-32946	 **attackbox here**
    sprite('to206_10', 3)	# 32947-32949
    sprite('to206_11', 3)	# 32950-32952
    SFX_3('cloth_l')
    sprite('to206_09', 3)	# 32953-32955	 **attackbox here**
    sprite('to206_10', 3)	# 32956-32958
    sprite('to206_11', 3)	# 32959-32961
    sprite('to206_09', 3)	# 32962-32964	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to206_10', 3)	# 32965-32967
    sprite('to206_11', 3)	# 32968-32970
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 32971-65737
    enterState('PersonaDeleteAndIdling')

@State
def PCE_Persona5D_CA():

    def upon_IMMEDIATE():
        Unknown23184('0300000064000000b03cffff50c3000000000000c05c1500b03cffff50c30000')
        callSubroutine('PCE_AttackInit')
        Unknown2009()
        Unknown9016(1)
        Unknown4007(3)
        callSubroutine('PCE_CheckWarp')
        Unknown23022(1)
        Unknown2003(1)
    sprite('to205_00', 2)	# 1-2
    sprite('to205_10', 2)	# 3-4
    SFX_3('slash_pole_slow')
    sprite('to205_11', 1)	# 5-5
    physicsXImpulse(30000)
    sprite('to205_11', 1)	# 6-6
    Unknown1019(85)
    sprite('to205_11', 1)	# 7-7
    Unknown1019(85)
    sprite('to205_12', 1)	# 8-8
    Unknown1019(85)
    sprite('to205_12', 1)	# 9-9
    Unknown1019(85)
    sprite('to205_14', 3)	# 10-12	 **attackbox here**
    Unknown23054('746f3230355f313300000000000000000000000000000000000000000000000003000000')
    GFX_0('Zanzoh5D_2', 100)
    RefreshMultihit()
    Unknown1019(0)
    sprite('to205_15', 3)	# 13-15
    Unknown23027()
    sprite('to205_16', 3)	# 16-18
    SFX_3('cloth_l')
    sprite('to205_14', 3)	# 19-21	 **attackbox here**
    sprite('to205_15', 3)	# 22-24
    sprite('to205_16', 3)	# 25-27
    sprite('to205_14', 3)	# 28-30	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to205_15', 3)	# 31-33
    sprite('to205_16', 3)	# 34-36
    sprite('to205_14', 3)	# 37-39	 **attackbox here**
    sprite('to205_15', 3)	# 40-42
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 43-45
    sprite('to205_14', 3)	# 46-48	 **attackbox here**
    sprite('to205_15', 3)	# 49-51
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 52-54
    sprite('to205_14', 3)	# 55-57	 **attackbox here**
    sprite('to205_15', 3)	# 58-60
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 61-63
    sprite('to205_14', 3)	# 64-66	 **attackbox here**
    sprite('to205_15', 3)	# 67-69
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 70-72
    sprite('to205_14', 3)	# 73-75	 **attackbox here**
    sprite('to205_15', 3)	# 76-78
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 79-81
    sprite('to205_14', 3)	# 82-84	 **attackbox here**
    sprite('to205_15', 3)	# 85-87
    SFX_3('cloth_l')
    sprite('to205_16', 3)	# 88-90
    sprite('to205_14', 3)	# 91-93	 **attackbox here**
    sprite('to205_15', 3)	# 94-96
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 97-32863
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaD_Hasei_CA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c30000b03cffffc05c15000000000050c30000')
        callSubroutine('PCE_AttackInit')
        Unknown2009()
        Unknown9016(1)
        Unknown23078(1)
        Unknown4007(3)
        Unknown2053(0)
        Unknown2017(0)
        callSubroutine('PCE_CheckWarp')
        Unknown23022(1)
        Unknown2003(1)
    sprite('to206_00', 3)	# 1-3
    sprite('to206_04', 3)	# 4-6
    GFX_0('Zanzoh5DD_2', 100)
    Unknown23015(0)
    Unknown2019(500)
    sprite('to206_05', 2)	# 7-8
    sprite('to206_06', 2)	# 9-10
    sprite('to206_07', 2)	# 11-12
    GFX_0('Zanzoh5DD_3', 100)
    SFX_3('slash_pole_middle')
    sprite('to206_09', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    sprite('to206_10', 3)	# 16-18
    Unknown23027()
    sprite('to206_11', 3)	# 19-21
    SFX_3('cloth_l')
    sprite('to206_09', 3)	# 22-24	 **attackbox here**
    sprite('to206_10', 3)	# 25-27
    sprite('to206_11', 3)	# 28-30
    sprite('to206_09', 3)	# 31-33	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to206_10', 3)	# 34-36
    sprite('to206_11', 3)	# 37-39
    sprite('to206_09', 3)	# 40-42	 **attackbox here**
    sprite('to206_10', 3)	# 43-45
    SFX_3('cloth_l')
    sprite('to206_11', 3)	# 46-48
    sprite('to206_09', 3)	# 49-51	 **attackbox here**
    sprite('to206_10', 3)	# 52-54
    SFX_3('cloth_l')
    sprite('to206_11', 3)	# 55-57
    sprite('to206_09', 3)	# 58-60	 **attackbox here**
    sprite('to206_10', 3)	# 61-63
    SFX_3('cloth_l')
    sprite('to206_11', 3)	# 64-66
    sprite('keep', 32767)	# 67-32833
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAir5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000e09304000000000000000000')
        callSubroutine('PCE_AttackInit')
        AttackLevel_(3)
        AirPushbackY(24000)
        AirUntechableTime(19)
        AttackP1(80)
        HitOverhead(2)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('ChargeDamageUp')
        Unknown23078(1)
        Unknown11056(3)
        callSubroutine('PCE_CheckWarp')
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 3001):
                sendToLabel(580)
            if (SLOT_48 == 3002):
                sendToLabel(580)
    sprite('to254_00', 1)	# 1-1
    physicsXImpulse(25000)
    physicsYImpulse(0)
    sprite('to254_00', 1)	# 2-2
    Unknown1019(80)
    YAccel(80)
    sprite('to254_00', 1)	# 3-3
    Unknown1019(80)
    YAccel(80)
    sprite('to254_00', 1)	# 4-4
    Unknown1019(80)
    YAccel(80)
    sprite('to254_01', 1)	# 5-5
    Unknown1019(80)
    YAccel(80)
    GFX_0('ZanzohAir5C', 100)
    sprite('to254_01', 1)	# 6-6
    Unknown1019(80)
    YAccel(80)
    sprite('to254_01', 1)	# 7-7
    Unknown1019(80)
    YAccel(80)
    SFX_3('slash_pole_middle')
    sprite('to254_03', 1)	# 8-8	 **attackbox here**
    Unknown23054('746f3235345f303200000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Unknown1019(0)
    YAccel(0)
    sprite('to254_03', 3)	# 9-11	 **attackbox here**
    Unknown23022(0)
    sprite('to254_04', 3)	# 12-14
    Unknown23027()
    Unknown4007(0)
    sprite('to254_05', 3)	# 15-17
    sprite('to254_04', 3)	# 18-20
    SFX_3('cloth_l')
    sprite('to254_05', 3)	# 21-23
    sprite('to254_04', 3)	# 24-26
    sprite('to254_05', 3)	# 27-29
    label(580)
    sprite('keep', 32767)	# 30-32796
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAir4D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000e09304000000000000000000')
        callSubroutine('PCE_AttackInit')
        AttackLevel_(3)
        Damage(300)
        AirUntechableTime(25)
        AttackP1(80)
        AirPushbackY(4000)
        PushbackX(22000)
        Hitstop(0)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11092(1)
        Unknown30055('f04902006400000064000000')
        Unknown30056('50c300006400000064000000')
        callSubroutine('ChargeDamageUp')
        Unknown4007(3)
        Unknown2053(1)
        Unknown23078(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to255_00', 2)	# 1-2
    sprite('to255_01', 2)	# 3-4
    Unknown4007(0)
    physicsXImpulse(20000)
    physicsYImpulse(-9000)
    sprite('to255_02', 2)	# 5-6
    Unknown1019(80)
    YAccel(80)
    sprite('to255_03', 2)	# 7-8
    Unknown1019(80)
    YAccel(80)
    sprite('to255_04', 2)	# 9-10
    Unknown1019(80)
    YAccel(80)
    sprite('to255_05', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(80)
    SFX_3('slash_pole_fast')
    sprite('to255_06', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(80)
    GFX_0('ZanzohAir5D', 100)
    sprite('to255_07', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(80)
    SFX_3('slash_pole_fast')
    sprite('to255_05', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(80)
    sprite('to255_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(80)
    SFX_3('slash_pole_fast')
    sprite('to255_07', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    YAccel(80)
    sprite('to255_08', 3)	# 23-25
    Unknown1019(0)
    YAccel(0)
    GFX_0('ZanzohAir5D_2', 100)
    sprite('to255_09', 2)	# 26-27
    sprite('to255_10', 2)	# 28-29
    sprite('to255_11', 2)	# 30-31
    SFX_3('slash_pole_middle')
    sprite('to255_12', 1)	# 32-32
    sprite('to255_13', 1)	# 33-33
    GFX_0('ZanzohAir5D_3', 100)
    sprite('to255_14', 1)	# 34-34
    sprite('to255_15', 1)	# 35-35
    sprite('to255_17', 3)	# 36-38	 **attackbox here**
    Unknown23054('746f3235355f313600000000000000000000000000000000000000000000000002000000')
    Damage(1500)
    Unknown11092(0)
    AirPushbackY(-38000)
    Hitstop(12)
    callSubroutine('ChargeDamageUp')
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    RefreshMultihit()
    sprite('to255_18', 3)	# 39-41
    Unknown23027()
    sprite('to255_19', 3)	# 42-44
    Unknown2001()
    sprite('to255_17', 3)	# 45-47	 **attackbox here**
    sprite('to255_18', 3)	# 48-50
    SFX_3('cloth_l')
    sprite('to255_19', 3)	# 51-53
    sprite('to255_17', 3)	# 54-56	 **attackbox here**
    sprite('to255_18', 3)	# 57-59
    SFX_3('cloth_l')
    sprite('to255_19', 3)	# 60-62
    sprite('to255_17', 3)	# 63-65	 **attackbox here**
    sprite('to255_18', 3)	# 66-68
    SFX_3('cloth_l')
    sprite('to255_19', 3)	# 69-71
    sprite('to255_17', 3)	# 72-74	 **attackbox here**
    sprite('to255_18', 3)	# 75-77
    SFX_3('cloth_l')
    sprite('to255_19', 3)	# 78-80
    sprite('keep', 32767)	# 81-32847
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaDragonKickA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff0000000000000000e80300000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        callSubroutine('PCE_CheckWarp')
    sprite('to404_00', 1)	# 1-1
    Unknown23022(1)
    sprite('to404_01', 2)	# 2-3
    sprite('to404_02', 2)	# 4-5
    sprite('to404_03', 2)	# 6-7
    sprite('to404_04', 2)	# 8-9
    sprite('to404_05', 2)	# 10-11
    sprite('to404_06', 2)	# 12-13
    GFX_0('Zanzoh_DragonKick', 100)
    sprite('to404_07', 2)	# 14-15
    GFX_0('Zanzoh_DragonKick_2', 100)
    sprite('to404_08', 2)	# 16-17
    sprite('to404_09', 3)	# 18-20
    Unknown23022(0)
    sprite('to404_10', 3)	# 21-23
    sprite('to404_11', 3)	# 24-26
    sprite('to404_09', 3)	# 27-29
    sprite('to404_10', 3)	# 30-32
    sprite('to404_11', 3)	# 33-35
    sprite('keep', 32767)	# 36-32802
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaDragonKickB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff0000000000000000e80300000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        callSubroutine('PCE_CheckWarp')
    sprite('to404_00', 1)	# 1-1
    Unknown23022(1)
    sprite('to404_01', 1)	# 2-2
    sprite('to404_02', 1)	# 3-3
    sprite('to404_03', 2)	# 4-5
    sprite('to404_04', 2)	# 6-7
    sprite('to404_05', 2)	# 8-9
    sprite('to404_06', 3)	# 10-12
    GFX_0('Zanzoh_DragonKick', 100)
    sprite('to404_07', 2)	# 13-14
    GFX_0('Zanzoh_DragonKick_2', 100)
    sprite('to404_08', 2)	# 15-16
    sprite('to404_09', 3)	# 17-19
    Unknown23022(0)
    sprite('to404_10', 3)	# 20-22
    sprite('to404_11', 3)	# 23-25
    sprite('to404_09', 3)	# 26-28
    sprite('to404_10', 3)	# 29-31
    sprite('to404_11', 3)	# 32-34
    sprite('keep', 32767)	# 35-32801
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaDragonKickEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff0000000000000000e80300000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        callSubroutine('PCE_CheckWarp')
    sprite('to404_00', 1)	# 1-1
    Unknown23022(1)
    sprite('to404_01', 1)	# 2-2
    sprite('to404_02', 1)	# 3-3
    sprite('to404_03', 2)	# 4-5
    sprite('to404_04', 2)	# 6-7
    sprite('to404_05', 2)	# 8-9
    sprite('to404_06', 3)	# 10-12
    GFX_0('Zanzoh_DragonKick', 100)
    sprite('to404_07', 2)	# 13-14
    GFX_0('Zanzoh_DragonKick_2', 100)
    sprite('to404_08', 2)	# 15-16
    sprite('to404_09', 3)	# 17-19
    Unknown23022(0)
    sprite('to404_10', 3)	# 20-22
    sprite('to404_11', 3)	# 23-25
    sprite('to404_09', 3)	# 26-28
    sprite('to404_10', 3)	# 29-31
    sprite('to404_11', 3)	# 32-34
    sprite('keep', 32767)	# 35-32801
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAirDragonKickA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feffa086010000000000e80300000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        callSubroutine('PCE_CheckWarp')
    sprite('to404_04', 5)	# 1-5
    Unknown23022(1)
    sprite('to404_05', 2)	# 6-7
    sprite('to404_06', 2)	# 8-9
    GFX_0('Zanzoh_DragonKick', 100)
    sprite('to404_07', 2)	# 10-11
    GFX_0('Zanzoh_DragonKick_2', 100)
    sprite('to404_08', 2)	# 12-13
    sprite('to404_09', 3)	# 14-16
    sprite('to404_10', 3)	# 17-19
    sprite('to404_11', 3)	# 20-22
    sprite('to404_09', 3)	# 23-25
    sprite('to404_10', 3)	# 26-28
    sprite('to404_11', 3)	# 29-31
    sprite('to404_09', 3)	# 32-34
    sprite('to404_10', 3)	# 35-37
    sprite('to404_11', 3)	# 38-40
    sprite('keep', 32767)	# 41-32807
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAirDragonKickB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feffa086010000000000e80300000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        callSubroutine('PCE_CheckWarp')
    sprite('to404_04', 3)	# 1-3
    Unknown23022(1)
    sprite('to404_05', 2)	# 4-5
    sprite('to404_06', 2)	# 6-7
    GFX_0('Zanzoh_DragonKick', 100)
    sprite('to404_07', 2)	# 8-9
    GFX_0('Zanzoh_DragonKick_2', 100)
    sprite('to404_08', 2)	# 10-11
    sprite('to404_09', 3)	# 12-14
    sprite('to404_10', 3)	# 15-17
    sprite('to404_11', 3)	# 18-20
    sprite('to404_09', 3)	# 21-23
    sprite('to404_10', 3)	# 24-26
    sprite('to404_11', 3)	# 27-29
    sprite('to404_09', 3)	# 30-32
    sprite('to404_10', 3)	# 33-35
    sprite('to404_11', 3)	# 36-38
    sprite('keep', 32767)	# 39-32805
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAirDragonKickEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feffa086010000000000e80300000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        callSubroutine('PCE_CheckWarp')
    sprite('to404_04', 1)	# 1-1
    Unknown23022(1)
    sprite('to404_05', 2)	# 2-3
    sprite('to404_06', 3)	# 4-6
    GFX_0('Zanzoh_DragonKick', 100)
    sprite('to404_07', 2)	# 7-8
    GFX_0('Zanzoh_DragonKick_2', 100)
    sprite('to404_08', 2)	# 9-10
    sprite('to404_09', 3)	# 11-13
    sprite('to404_10', 3)	# 14-16
    sprite('to404_11', 3)	# 17-19
    sprite('to404_09', 3)	# 20-22
    sprite('to404_10', 3)	# 23-25
    sprite('to404_11', 3)	# 26-28
    sprite('to404_09', 3)	# 29-31
    sprite('to404_10', 3)	# 32-34
    sprite('to404_11', 3)	# 35-37
    sprite('keep', 32767)	# 38-32804
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaKokutengekiA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000605b030060ea00000000000080841e000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        Unknown2009()
        AttackLevel_(4)
        Damage(2040)
        AttackP1(100)
        AirUntechableTime(35)
        PushbackX(20000)
        AirPushbackX(24000)
        AirPushbackY(24000)
        YImpluseBeforeWallbounce(2700)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        Unknown23066(1)
        Unknown2053(1)
        Unknown2017(0)
        callSubroutine('PCE_CheckWarp')
    sprite('to405_00', 2)	# 1-2
    Unknown23022(1)
    GFX_0('KokutengekiTameC', 0)
    sprite('to405_01', 2)	# 3-4
    sprite('to405_02', 4)	# 5-8
    sprite('to405_03', 4)	# 9-12	 **attackbox here**
    RefreshMultihit()
    Unknown11033(1)
    Unknown11034(0)
    sprite('to405_04', 4)	# 13-16	 **attackbox here**
    sprite('to405_05', 4)	# 17-20	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 21-24	 **attackbox here**
    Unknown23022(0)
    Unknown23027()
    sprite('to405_04', 4)	# 25-28	 **attackbox here**
    sprite('to405_05', 4)	# 29-32	 **attackbox here**
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 33-32799
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaKokutengekiB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000605b030060ea00000000000080841e000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        Unknown2010()
        AttackLevel_(5)
        Damage(1200)
        PushbackX(35000)
        AirPushbackX(30000)
        AirPushbackY(35000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        FatalCounter(1)
        Unknown9072(70000)
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        Unknown23066(1)
        Unknown2053(1)
        Unknown2015(200)
        callSubroutine('PCE_CheckWarp')

        def upon_43():
            if (SLOT_48 == 4001):
                Unknown9348(0)
                Unknown11028(31)
            if (SLOT_48 == 4003):
                sendToLabel(0)
    sprite('to405_00', 9)	# 1-9
    Unknown23022(1)
    GFX_0('KokutengekiTameD', 0)
    label(0)
    sprite('to405_00', 4)	# 10-13
    gotoLabel(0)
    label(1)
    sprite('to405_01', 2)	# 14-15
    sprite('to405_02', 2)	# 16-17
    sprite('to405_03', 4)	# 18-21	 **attackbox here**
    Unknown21015('4b6f6b7574656e67656b6954616d654400000000000000000000000000000000a20f000000000000')
    RefreshMultihit()
    Unknown11033(1)
    Unknown11034(0)
    sprite('to405_04', 4)	# 22-25	 **attackbox here**
    sprite('to405_05', 4)	# 26-29	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 30-33	 **attackbox here**
    Unknown23022(0)
    Unknown23027()
    sprite('to405_04', 4)	# 34-37	 **attackbox here**
    sprite('to405_05', 4)	# 38-41	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 42-45	 **attackbox here**
    Unknown2001()
    sprite('to405_04', 4)	# 46-49	 **attackbox here**
    sprite('to405_05', 4)	# 50-53	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 54-57	 **attackbox here**
    sprite('to405_04', 4)	# 58-61	 **attackbox here**
    sprite('to405_05', 4)	# 62-65	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 66-69	 **attackbox here**
    sprite('to405_04', 4)	# 70-73	 **attackbox here**
    sprite('to405_05', 4)	# 74-77	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 78-81	 **attackbox here**
    sprite('to405_04', 4)	# 82-85	 **attackbox here**
    sprite('to405_05', 4)	# 86-89	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 90-93	 **attackbox here**
    sprite('to405_04', 4)	# 94-97	 **attackbox here**
    sprite('to405_05', 4)	# 98-101	 **attackbox here**
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 102-32868
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaKokutengekiEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000c0d4010060ea00000000000080841e000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        Unknown2010()
        AttackLevel_(5)
        Damage(950)
        AttackP2(84)
        PushbackX(50000)
        AirPushbackX(30000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9072(70000)
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        Unknown23066(1)
        Unknown2053(1)
        Unknown4009(3)
        Unknown2015(200)
        callSubroutine('PCE_CheckWarp')
    sprite('to405_00', 4)	# 1-4
    Unknown23022(1)
    GFX_0('KokutengekiTameCD', 0)
    sprite('to405_01', 4)	# 5-8
    sprite('to405_02', 4)	# 9-12
    sprite('to405_03', 4)	# 13-16	 **attackbox here**
    RefreshMultihit()
    Unknown11033(1)
    Unknown11034(0)
    sprite('to405_04', 4)	# 17-20	 **attackbox here**
    sprite('to405_05', 4)	# 21-24	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 25-28	 **attackbox here**
    Unknown23027()
    sprite('to405_04', 4)	# 29-32	 **attackbox here**
    sprite('to405_05', 4)	# 33-36	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 37-40	 **attackbox here**
    Unknown2001()
    sprite('to405_04', 4)	# 41-44	 **attackbox here**
    sprite('to405_05', 4)	# 45-48	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 49-52	 **attackbox here**
    sprite('to405_04', 4)	# 53-56	 **attackbox here**
    sprite('to405_05', 4)	# 57-60	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 61-64	 **attackbox here**
    sprite('to405_04', 4)	# 65-68	 **attackbox here**
    sprite('to405_05', 4)	# 69-72	 **attackbox here**
    Unknown23022(0)
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 73-76	 **attackbox here**
    sprite('to405_04', 4)	# 77-80	 **attackbox here**
    sprite('to405_05', 4)	# 81-84	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 85-88	 **attackbox here**
    sprite('to405_04', 4)	# 89-92	 **attackbox here**
    sprite('to405_05', 4)	# 93-96	 **attackbox here**
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 97-32863
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaKokutengeki_PS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000605b030060ea00000000000080841e000000000000000000')
        callSubroutine('PCE_SPAttackInit')
        Unknown2010()
        AttackLevel_(4)
        AttackP1(70)
        AttackP2(90)
        AirUntechableTime(35)
        PushbackX(20000)
        AirPushbackX(10000)
        AirPushbackY(24000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11042(1)
        callSubroutine('ChargeDamageUp')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            callSubroutine('Charge_Count')
        Unknown23066(1)
        Unknown2053(1)
        Unknown2017(0)
        callSubroutine('PCE_CheckWarp')
    sprite('to405_00', 2)	# 1-2
    Unknown23022(1)
    teleportRelativeX(-75000)
    GFX_0('KokutengekiTameC', 0)
    Unknown36(1)
    teleportRelativeX(-20000)
    Unknown35()
    sprite('to405_01', 2)	# 3-4
    sprite('to405_02', 4)	# 5-8
    sprite('to405_03', 4)	# 9-12	 **attackbox here**
    RefreshMultihit()
    Unknown11033(1)
    Unknown11034(0)
    sprite('to405_04', 4)	# 13-16	 **attackbox here**
    sprite('to405_05', 4)	# 17-20	 **attackbox here**
    SFX_3('cloth_l')
    sprite('to405_03', 4)	# 21-24	 **attackbox here**
    Unknown23022(0)
    Unknown23027()
    sprite('to405_04', 4)	# 25-28	 **attackbox here**
    sprite('to405_05', 4)	# 29-32	 **attackbox here**
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 33-32799
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaGodHand():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050340300f049020000000000000000000000000000000000')
        callSubroutine('PCE_DDAttackInit')
        Unknown2011()
        AttackLevel_(5)
        Damage(5000)
        AttackP2(60)
        Unknown11091(30)
        Hitstop(0)
        Unknown11001(13, 13, 13)
        AirPushbackY(-500000)
        AirPushbackX(1000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9310(20)
        Unknown23022(1)
        callSubroutine('ChargeDamageUp')
        Unknown4009(3)
        Unknown23066(1)
        Unknown2053(1)

        def upon_56():
            Unknown4009(0)
            Unknown2054(0)
        callSubroutine('PCE_ForceWarp')
    sprite('to430_00', 3)	# 1-3
    GFX_0('GodHandKobusiKumo', 0)
    sprite('to430_01', 3)	# 4-6
    sprite('to430_02', 3)	# 7-9
    sprite('to430_00', 3)	# 10-12
    sprite('to430_01', 3)	# 13-15
    sprite('to430_02', 3)	# 16-18
    sprite('to430_00', 3)	# 19-21
    sprite('to430_01', 3)	# 22-24
    sprite('to430_02', 3)	# 25-27
    sprite('to430_00', 3)	# 28-30
    sprite('to430_01', 3)	# 31-33
    sprite('to430_02', 3)	# 34-36
    sprite('to430_00', 3)	# 37-39
    sprite('to430_01', 3)	# 40-42
    sprite('to430_02', 3)	# 43-45
    sprite('to430_00', 3)	# 46-48
    sprite('to430_01', 3)	# 49-51
    sprite('to430_02', 3)	# 52-54
    sprite('to430_03', 3)	# 55-57
    sprite('to430_04', 3)	# 58-60
    SFX_3('bomb_l')
    sprite('to430_05', 6)	# 61-66	 **attackbox here**
    GFX_0('GodHandKobusi', 0)
    GFX_0('GodHandKobusiWind', 1)
    GFX_1('toef_godhandtukene_02', 2)
    ScreenShake(0, 30000)
    RefreshMultihit()
    if SLOT_31:
        pass
    sprite('to430_06', 3)	# 67-69
    Unknown23027()
    sprite('to430_07', 3)	# 70-72
    sprite('to430_05', 3)	# 73-75	 **attackbox here**
    sprite('to430_06', 3)	# 76-78
    sprite('to430_07', 3)	# 79-81
    sprite('to430_05', 3)	# 82-84	 **attackbox here**
    sprite('to430_06', 3)	# 85-87
    sprite('to430_07', 3)	# 88-90
    sprite('to430_05', 3)	# 91-93	 **attackbox here**
    sprite('to430_06', 3)	# 94-96
    sprite('to430_07', 3)	# 97-99
    sprite('to430_05', 3)	# 100-102	 **attackbox here**
    sprite('to430_06', 3)	# 103-105
    sprite('to430_07', 3)	# 106-108
    sprite('keep', 32767)	# 109-32875
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaGodHandOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050340300f049020000000000000000000000000000000000')
        callSubroutine('PCE_DDAttackInit')
        Unknown2011()
        AttackLevel_(5)
        Damage(5000)
        AttackP2(60)
        Unknown11092(1)
        Hitstop(0)
        Unknown11001(13, 13, 13)
        AirPushbackY(-500000)
        AirPushbackX(15000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9310(20)
        Unknown23022(1)
        Unknown11068(1)
        callSubroutine('ChargeDamageUp')
        Unknown4009(3)
        Unknown23066(1)
        Unknown2053(1)

        def upon_56():
            Unknown4009(0)
            Unknown2054(0)
        callSubroutine('PCE_ForceWarp')
    sprite('to430_00', 3)	# 1-3
    GFX_0('GodHandKobusiKumo', 0)
    sprite('to430_01', 3)	# 4-6
    sprite('to430_02', 3)	# 7-9
    sprite('to430_00', 3)	# 10-12
    sprite('to430_01', 3)	# 13-15
    sprite('to430_02', 3)	# 16-18
    sprite('to430_00', 3)	# 19-21
    sprite('to430_01', 3)	# 22-24
    sprite('to430_02', 3)	# 25-27
    sprite('to430_00', 3)	# 28-30
    sprite('to430_01', 3)	# 31-33
    sprite('to430_02', 3)	# 34-36
    sprite('to430_00', 3)	# 37-39
    sprite('to430_01', 3)	# 40-42
    sprite('to430_02', 3)	# 43-45
    sprite('to430_00', 3)	# 46-48
    sprite('to430_01', 3)	# 49-51
    sprite('to430_02', 3)	# 52-54
    sprite('to430_03', 3)	# 55-57
    sprite('to430_04', 3)	# 58-60
    SFX_3('bomb_l')
    sprite('to430_05', 6)	# 61-66	 **attackbox here**
    GFX_0('GodHandKobusi', 0)
    GFX_0('GodHandKobusiWind', 1)
    GFX_1('toef_godhandtukene_02', 2)
    ScreenShake(0, 30000)
    RefreshMultihit()
    if SLOT_31:
        pass
    sprite('to430_06', 3)	# 67-69
    sprite('to430_00', 3)	# 70-72
    Unknown23184('0300000064000000b08f0600f049020000000000000000000000000000000000')
    callSubroutine('PCE_ForceWarp')
    GFX_0('GodHandKobusiKumo', 0)
    sprite('to430_01', 3)	# 73-75
    sprite('to430_02', 3)	# 76-78
    sprite('to430_00', 3)	# 79-81
    sprite('to430_01', 3)	# 82-84
    sprite('to430_02', 3)	# 85-87
    sprite('to430_03', 3)	# 88-90
    sprite('to430_04', 3)	# 91-93
    SFX_3('bomb_l')
    sprite('to430_05', 6)	# 94-99	 **attackbox here**
    GFX_0('GodHandKobusi', 0)
    GFX_0('GodHandKobusiWind', 1)
    GFX_1('toef_godhandtukene_02', 2)
    RefreshMultihit()
    ScreenShake(0, 30000)
    sprite('to430_06', 3)	# 100-102
    Unknown23027()
    sprite('to430_07', 3)	# 103-105
    sprite('to430_05', 3)	# 106-108	 **attackbox here**
    sprite('to430_06', 3)	# 109-111
    sprite('to430_07', 3)	# 112-114
    sprite('to430_05', 3)	# 115-117	 **attackbox here**
    sprite('to430_06', 3)	# 118-120
    sprite('to430_07', 3)	# 121-123
    sprite('to430_05', 3)	# 124-126	 **attackbox here**
    sprite('to430_06', 3)	# 127-129
    sprite('to430_07', 3)	# 130-132
    sprite('to430_05', 3)	# 133-135	 **attackbox here**
    sprite('to430_06', 3)	# 136-138
    sprite('to430_07', 3)	# 139-141
    sprite('keep', 32767)	# 142-32908
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAguneyasutora_Far():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000000000000c0bdf0ff40420f00')
        callSubroutine('PCE_DDAttackInit')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23022(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to432_00', 2)	# 1-2
    GFX_0('meteoStartAura', 0)
    sprite('to432_01', 2)	# 3-4
    sprite('to432_02', 2)	# 5-6
    sprite('to432_00', 2)	# 7-8
    sprite('to432_01', 2)	# 9-10
    sprite('to432_02', 2)	# 11-12
    sprite('to432_00', 2)	# 13-14
    sprite('to432_01', 2)	# 15-16
    sprite('to432_02', 2)	# 17-18
    sprite('to432_00', 2)	# 19-20
    sprite('to432_01', 2)	# 21-22
    sprite('to432_02', 2)	# 23-24
    sprite('to432_00', 2)	# 25-26
    sprite('to432_01', 2)	# 27-28
    sprite('to432_03', 3)	# 29-31
    sprite('to432_04', 3)	# 32-34
    sprite('to432_05', 3)	# 35-37
    GFX_0('meteo_takusanD', 0)
    ScreenShake(0, 10000)
    sprite('to432_06', 2)	# 38-39
    sprite('to432_07', 2)	# 40-41
    sprite('to432_08', 2)	# 42-43
    sprite('to432_06', 2)	# 44-45
    sprite('to432_07', 2)	# 46-47
    sprite('to432_08', 2)	# 48-49
    sprite('to432_06', 2)	# 50-51
    sprite('to432_07', 2)	# 52-53
    sprite('to432_08', 2)	# 54-55
    sprite('to432_06', 2)	# 56-57
    sprite('to432_07', 2)	# 58-59
    sprite('to432_08', 2)	# 60-61
    sprite('to432_06', 2)	# 62-63
    sprite('to432_07', 2)	# 64-65
    sprite('to432_08', 2)	# 66-67
    sprite('to432_06', 2)	# 68-69
    sprite('to432_07', 2)	# 70-71
    sprite('to432_06', 2)	# 72-73
    sprite('to432_07', 2)	# 74-75
    sprite('to432_08', 2)	# 76-77
    sprite('to432_06', 2)	# 78-79
    sprite('to432_07', 2)	# 80-81
    sprite('to432_08', 2)	# 82-83
    sprite('to432_06', 2)	# 84-85
    sprite('to432_07', 2)	# 86-87
    sprite('to432_08', 2)	# 88-89
    sprite('keep', 32767)	# 90-32856
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAguneyasutoraOD_Far():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000000000000c0bdf0ff40420f00')
        callSubroutine('PCE_DDAttackInit')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23022(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to432_00', 2)	# 1-2
    GFX_0('meteoStartAura', 0)
    sprite('to432_01', 2)	# 3-4
    sprite('to432_02', 2)	# 5-6
    sprite('to432_00', 2)	# 7-8
    sprite('to432_01', 2)	# 9-10
    sprite('to432_02', 2)	# 11-12
    sprite('to432_00', 2)	# 13-14
    sprite('to432_01', 2)	# 15-16
    sprite('to432_02', 2)	# 17-18
    sprite('to432_00', 2)	# 19-20
    sprite('to432_01', 2)	# 21-22
    sprite('to432_02', 2)	# 23-24
    sprite('to432_00', 2)	# 25-26
    sprite('to432_01', 2)	# 27-28
    sprite('to432_03', 3)	# 29-31
    sprite('to432_04', 3)	# 32-34
    sprite('to432_05', 3)	# 35-37
    GFX_0('meteo_takusanD_OD', 0)
    ScreenShake(0, 10000)
    sprite('to432_06', 2)	# 38-39
    sprite('to432_07', 2)	# 40-41
    sprite('to432_08', 2)	# 42-43
    sprite('to432_06', 2)	# 44-45
    sprite('to432_07', 2)	# 46-47
    sprite('to432_08', 2)	# 48-49
    sprite('to432_06', 2)	# 50-51
    sprite('to432_07', 2)	# 52-53
    sprite('to432_08', 2)	# 54-55
    sprite('to432_06', 2)	# 56-57
    sprite('to432_07', 2)	# 58-59
    sprite('to432_08', 2)	# 60-61
    sprite('to432_06', 2)	# 62-63
    sprite('to432_07', 2)	# 64-65
    sprite('to432_08', 2)	# 66-67
    sprite('to432_06', 2)	# 68-69
    sprite('to432_07', 2)	# 70-71
    sprite('to432_06', 2)	# 72-73
    sprite('to432_07', 2)	# 74-75
    sprite('to432_08', 2)	# 76-77
    sprite('to432_06', 2)	# 78-79
    sprite('to432_07', 2)	# 80-81
    sprite('to432_08', 2)	# 82-83
    sprite('to432_06', 2)	# 84-85
    sprite('to432_07', 2)	# 86-87
    sprite('to432_08', 2)	# 88-89
    sprite('keep', 32767)	# 90-32856
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAguneyasutora_Near():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000000000000c0bdf0ff40420f00')
        callSubroutine('PCE_DDAttackInit')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23022(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to432_00', 2)	# 1-2
    GFX_0('meteoStartAura', 0)
    sprite('to432_01', 2)	# 3-4
    sprite('to432_02', 2)	# 5-6
    sprite('to432_00', 2)	# 7-8
    sprite('to432_01', 2)	# 9-10
    sprite('to432_02', 2)	# 11-12
    sprite('to432_00', 2)	# 13-14
    sprite('to432_01', 2)	# 15-16
    sprite('to432_02', 2)	# 17-18
    sprite('to432_00', 2)	# 19-20
    sprite('to432_01', 2)	# 21-22
    sprite('to432_02', 2)	# 23-24
    sprite('to432_00', 2)	# 25-26
    sprite('to432_01', 2)	# 27-28
    sprite('to432_03', 3)	# 29-31
    sprite('to432_04', 3)	# 32-34
    sprite('to432_05', 3)	# 35-37
    GFX_0('meteo_takusanC', 0)
    ScreenShake(0, 10000)
    sprite('to432_06', 2)	# 38-39
    sprite('to432_07', 2)	# 40-41
    sprite('to432_08', 2)	# 42-43
    sprite('to432_06', 2)	# 44-45
    sprite('to432_07', 2)	# 46-47
    sprite('to432_08', 2)	# 48-49
    sprite('to432_06', 2)	# 50-51
    sprite('to432_07', 2)	# 52-53
    sprite('to432_08', 2)	# 54-55
    sprite('to432_06', 2)	# 56-57
    sprite('to432_07', 2)	# 58-59
    sprite('to432_08', 2)	# 60-61
    sprite('to432_06', 2)	# 62-63
    sprite('to432_07', 2)	# 64-65
    sprite('to432_08', 2)	# 66-67
    sprite('to432_06', 2)	# 68-69
    sprite('to432_07', 2)	# 70-71
    sprite('to432_06', 2)	# 72-73
    sprite('to432_07', 2)	# 74-75
    sprite('to432_08', 2)	# 76-77
    sprite('to432_06', 2)	# 78-79
    sprite('to432_07', 2)	# 80-81
    sprite('to432_08', 2)	# 82-83
    sprite('to432_06', 2)	# 84-85
    sprite('to432_07', 2)	# 86-87
    sprite('to432_08', 2)	# 88-89
    sprite('keep', 32767)	# 90-32856
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAguneyasutoraOD_Near():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000000000000c0bdf0ff40420f00')
        callSubroutine('PCE_DDAttackInit')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23022(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to432_00', 2)	# 1-2
    GFX_0('meteoStartAura', 0)
    sprite('to432_01', 2)	# 3-4
    sprite('to432_02', 2)	# 5-6
    sprite('to432_00', 2)	# 7-8
    sprite('to432_01', 2)	# 9-10
    sprite('to432_02', 2)	# 11-12
    sprite('to432_00', 2)	# 13-14
    sprite('to432_01', 2)	# 15-16
    sprite('to432_02', 2)	# 17-18
    sprite('to432_00', 2)	# 19-20
    sprite('to432_01', 2)	# 21-22
    sprite('to432_02', 2)	# 23-24
    sprite('to432_00', 2)	# 25-26
    sprite('to432_01', 2)	# 27-28
    sprite('to432_03', 3)	# 29-31
    sprite('to432_04', 3)	# 32-34
    sprite('to432_05', 3)	# 35-37
    GFX_0('meteo_takusanC_OD', 0)
    ScreenShake(0, 10000)
    sprite('to432_06', 2)	# 38-39
    sprite('to432_07', 2)	# 40-41
    sprite('to432_08', 2)	# 42-43
    sprite('to432_06', 2)	# 44-45
    sprite('to432_07', 2)	# 46-47
    sprite('to432_08', 2)	# 48-49
    sprite('to432_06', 2)	# 50-51
    sprite('to432_07', 2)	# 52-53
    sprite('to432_08', 2)	# 54-55
    sprite('to432_06', 2)	# 56-57
    sprite('to432_07', 2)	# 58-59
    sprite('to432_08', 2)	# 60-61
    sprite('to432_06', 2)	# 62-63
    sprite('to432_07', 2)	# 64-65
    sprite('to432_08', 2)	# 66-67
    sprite('to432_06', 2)	# 68-69
    sprite('to432_07', 2)	# 70-71
    sprite('to432_06', 2)	# 72-73
    sprite('to432_07', 2)	# 74-75
    sprite('to432_08', 2)	# 76-77
    sprite('to432_06', 2)	# 78-79
    sprite('to432_07', 2)	# 80-81
    sprite('to432_08', 2)	# 82-83
    sprite('to432_06', 2)	# 84-85
    sprite('to432_07', 2)	# 86-87
    sprite('to432_08', 2)	# 88-89
    sprite('keep', 32767)	# 90-32856
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaAguneyasutoraOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PCE_DDAttackInit')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23022(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to432_00', 2)	# 1-2
    GFX_0('meteoStartAura', 0)
    Unknown2006()
    sprite('to432_01', 2)	# 3-4
    sprite('to432_02', 2)	# 5-6
    sprite('to432_00', 2)	# 7-8
    sprite('to432_01', 2)	# 9-10
    sprite('to432_02', 2)	# 11-12
    sprite('to432_00', 2)	# 13-14
    sprite('to432_01', 2)	# 15-16
    sprite('to432_02', 2)	# 17-18
    sprite('to432_00', 2)	# 19-20
    sprite('to432_01', 2)	# 21-22
    sprite('to432_02', 2)	# 23-24
    sprite('to432_00', 2)	# 25-26
    sprite('to432_01', 2)	# 27-28
    sprite('to432_03', 3)	# 29-31
    sprite('to432_04', 3)	# 32-34
    sprite('to432_05', 3)	# 35-37
    GFX_0('meteo_takusanCD', 0)
    ScreenShake(0, 10000)
    sprite('to432_06', 2)	# 38-39
    sprite('to432_07', 2)	# 40-41
    sprite('to432_08', 2)	# 42-43
    sprite('to432_06', 2)	# 44-45
    sprite('to432_07', 2)	# 46-47
    sprite('to432_08', 2)	# 48-49
    sprite('to432_06', 2)	# 50-51
    sprite('to432_07', 2)	# 52-53
    sprite('to432_08', 2)	# 54-55
    sprite('to432_06', 2)	# 56-57
    sprite('to432_07', 2)	# 58-59
    sprite('to432_08', 2)	# 60-61
    sprite('to432_06', 2)	# 62-63
    sprite('to432_07', 2)	# 64-65
    sprite('to432_08', 2)	# 66-67
    sprite('to432_06', 2)	# 68-69
    sprite('to432_07', 2)	# 70-71
    sprite('to432_06', 2)	# 72-73
    sprite('to432_07', 2)	# 74-75
    sprite('to432_08', 2)	# 76-77
    sprite('to432_06', 2)	# 78-79
    sprite('to432_07', 2)	# 80-81
    sprite('to432_08', 2)	# 82-83
    sprite('to432_06', 2)	# 84-85
    sprite('to432_07', 2)	# 86-87
    sprite('to432_08', 2)	# 88-89
    sprite('keep', 32767)	# 90-32856
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaGodHand_DUO():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050340300f049020000000000000000000000000000000000')
        callSubroutine('PCE_DDAttackInit')
        Unknown2011()
        AttackLevel_(5)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Hitstop(0)
        Unknown11001(13, 13, 13)
        AirPushbackY(-500000)
        AirPushbackX(1000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9310(20)
        Unknown23022(1)
        Unknown4009(3)
        Unknown23066(1)
        Unknown2053(1)

        def upon_56():
            Unknown4009(0)
            Unknown2054(0)
        callSubroutine('PCE_ForceWarp')
    sprite('to430_00', 3)	# 1-3
    GFX_0('GodHandKobusiKumo', 0)
    sprite('to430_01', 3)	# 4-6
    sprite('to430_02', 3)	# 7-9
    sprite('to430_00', 3)	# 10-12
    sprite('to430_01', 3)	# 13-15
    sprite('to430_02', 3)	# 16-18
    sprite('to430_00', 3)	# 19-21
    sprite('to430_01', 3)	# 22-24
    sprite('to430_02', 3)	# 25-27
    sprite('to430_00', 3)	# 28-30
    sprite('to430_01', 3)	# 31-33
    sprite('to430_02', 3)	# 34-36
    sprite('to430_00', 3)	# 37-39
    sprite('to430_01', 3)	# 40-42
    sprite('to430_02', 3)	# 43-45
    sprite('to430_00', 3)	# 46-48
    sprite('to430_01', 3)	# 49-51
    sprite('to430_02', 3)	# 52-54
    sprite('to430_03', 3)	# 55-57
    sprite('to430_04', 3)	# 58-60
    SFX_3('bomb_l')
    sprite('to430_05', 6)	# 61-66	 **attackbox here**
    GFX_0('GodHandKobusi', 0)
    GFX_0('GodHandKobusiWind', 1)
    GFX_1('toef_godhandtukene_02', 2)
    ScreenShake(0, 30000)
    RefreshMultihit()
    sprite('to430_06', 3)	# 67-69
    Unknown23027()
    sprite('to430_07', 3)	# 70-72
    sprite('to430_05', 3)	# 73-75	 **attackbox here**
    sprite('to430_06', 3)	# 76-78
    sprite('to430_07', 3)	# 79-81
    sprite('to430_05', 3)	# 82-84	 **attackbox here**
    sprite('to430_06', 3)	# 85-87
    sprite('to430_07', 3)	# 88-90
    sprite('to430_05', 3)	# 91-93	 **attackbox here**
    sprite('to430_06', 3)	# 94-96
    sprite('to430_07', 3)	# 97-99
    sprite('to430_05', 3)	# 100-102	 **attackbox here**
    sprite('to430_06', 3)	# 103-105
    sprite('to430_07', 3)	# 106-108
    sprite('keep', 32767)	# 109-32875
    enterState('PersonaDeleteAndIdling')

@State
def PCE_PersonaGodHand_DUOOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050340300f049020000000000000000000000000000000000')
        callSubroutine('PCE_DDAttackInit')
        Unknown2011()
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown11001(13, 13, 13)
        AirPushbackY(-500000)
        AirPushbackX(15000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9310(20)
        Unknown23022(1)
        Unknown11068(1)
        Unknown4009(3)
        Unknown23066(1)
        Unknown2053(1)

        def upon_56():
            Unknown4009(0)
            Unknown2054(0)
        callSubroutine('PCE_ForceWarp')
    sprite('to430_00', 3)	# 1-3
    GFX_0('GodHandKobusiKumo', 0)
    sprite('to430_01', 3)	# 4-6
    sprite('to430_02', 3)	# 7-9
    sprite('to430_00', 3)	# 10-12
    sprite('to430_01', 3)	# 13-15
    sprite('to430_02', 3)	# 16-18
    sprite('to430_00', 3)	# 19-21
    sprite('to430_01', 3)	# 22-24
    sprite('to430_02', 3)	# 25-27
    sprite('to430_00', 3)	# 28-30
    sprite('to430_01', 3)	# 31-33
    sprite('to430_02', 3)	# 34-36
    sprite('to430_00', 3)	# 37-39
    sprite('to430_01', 3)	# 40-42
    sprite('to430_02', 3)	# 43-45
    sprite('to430_00', 3)	# 46-48
    sprite('to430_01', 3)	# 49-51
    sprite('to430_02', 3)	# 52-54
    sprite('to430_03', 3)	# 55-57
    sprite('to430_04', 3)	# 58-60
    SFX_3('bomb_l')
    sprite('to430_05', 6)	# 61-66	 **attackbox here**
    GFX_0('GodHandKobusi', 0)
    GFX_0('GodHandKobusiWind', 1)
    GFX_1('toef_godhandtukene_02', 2)
    ScreenShake(0, 30000)
    RefreshMultihit()
    sprite('to430_06', 3)	# 67-69
    sprite('to430_00', 3)	# 70-72
    Unknown23184('0300000064000000b08f0600f049020000000000000000000000000000000000')
    callSubroutine('PCE_ForceWarp')
    GFX_0('GodHandKobusiKumo', 0)
    sprite('to430_01', 3)	# 73-75
    sprite('to430_02', 3)	# 76-78
    sprite('to430_00', 3)	# 79-81
    sprite('to430_01', 3)	# 82-84
    sprite('to430_02', 3)	# 85-87
    sprite('to430_03', 3)	# 88-90
    sprite('to430_04', 3)	# 91-93
    SFX_3('bomb_l')
    sprite('to430_05', 6)	# 94-99	 **attackbox here**
    GFX_0('GodHandKobusi', 0)
    GFX_0('GodHandKobusiWind', 1)
    GFX_1('toef_godhandtukene_02', 2)
    RefreshMultihit()
    Damage(1500)
    ScreenShake(0, 30000)
    sprite('to430_06', 3)	# 100-102
    Unknown23027()
    sprite('to430_07', 3)	# 103-105
    sprite('to430_05', 3)	# 106-108	 **attackbox here**
    sprite('to430_06', 3)	# 109-111
    sprite('to430_07', 3)	# 112-114
    sprite('to430_05', 3)	# 115-117	 **attackbox here**
    sprite('to430_06', 3)	# 118-120
    sprite('to430_07', 3)	# 121-123
    sprite('to430_05', 3)	# 124-126	 **attackbox here**
    sprite('to430_06', 3)	# 127-129
    sprite('to430_07', 3)	# 130-132
    sprite('to430_05', 3)	# 133-135	 **attackbox here**
    sprite('to430_06', 3)	# 136-138
    sprite('to430_07', 3)	# 139-141
    sprite('keep', 32767)	# 142-32908
    enterState('PersonaDeleteAndIdling')

@State
def Zanzoh5C():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3004(-25)
    sprite('vr_to204_00', 2)	# 1-2
    sprite('vr_to204_01', 2)	# 3-4
    sprite('vr_to204_02', 12)	# 5-16

@State
def Zanzoh2C():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3004(-23)
    sprite('vr_to234_05', 12)	# 1-12

@State
def __2C_ice():

    def upon_IMMEDIATE():
        Unknown4010(28)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('746f65665f3233345f69636530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1007(-80000)
    sprite('null', 2)	# 1-2
    SFX_3('ice_fast')
    GFX_1('toef_C2_ice', 100)
    sprite('null', 1)	# 3-3
    SFX_3('ice_fast')
    GFX_0('2C_ice_b', 100)
    sprite('null', 11)	# 4-14
    SFX_3('ice_fast')
    GFX_0('2C_ice_c', 100)
    sprite('null', 10)	# 15-24
    Unknown3004(-25)

@State
def __2C_ice_b():

    def upon_IMMEDIATE():
        Unknown4010(28)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('746f65665f3233345f69636530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown23015(14)
        Unknown1007(8000)
        teleportRelativeX(135000)
    sprite('null', 12)	# 1-12
    GFX_1('toef_C2_ice', 100)
    sprite('null', 10)	# 13-22
    Unknown3004(-25)

@State
def __2C_ice_c():

    def upon_IMMEDIATE():
        Unknown4010(28)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('746f65665f3233345f69636530322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown23015(14)
        Unknown1007(24000)
        teleportRelativeX(260000)
    sprite('null', 11)	# 1-11
    GFX_1('toef_C2_ice', 100)
    sprite('null', 10)	# 12-21
    Unknown3004(-25)

@State
def Zanzoh5D():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_to205_00', 3)	# 1-3
    sprite('vr_to205_01', 3)	# 4-6
    sprite('vr_to205_02', 3)	# 7-9
    sprite('vr_to205_03', 2)	# 10-11
    sprite('vr_to205_04', 2)	# 12-13
    sprite('vr_to205_05', 2)	# 14-15
    sprite('vr_to205_06', 3)	# 16-18
    sprite('vr_to205_07', 2)	# 19-20
    sprite('vr_to205_08', 2)	# 21-22
    sprite('vr_to205_03', 2)	# 23-24
    sprite('vr_to205_04', 2)	# 25-26
    sprite('vr_to205_05', 2)	# 27-28
    sprite('vr_to205_06', 3)	# 29-31
    sprite('vr_to205_09', 3)	# 32-34
    sprite('vr_to205_10', 3)	# 35-37
    sprite('vr_to205_11', 2)	# 38-39

@State
def Zanzoh5D_Short():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_to205_00', 2)	# 1-2
    sprite('vr_to205_01', 2)	# 3-4
    sprite('vr_to205_02', 2)	# 5-6
    sprite('vr_to205_03', 2)	# 7-8
    sprite('vr_to205_04', 2)	# 9-10
    sprite('vr_to205_05', 2)	# 11-12
    sprite('vr_to205_06', 3)	# 13-15
    sprite('vr_to205_07', 2)	# 16-17
    sprite('vr_to205_08', 2)	# 18-19
    sprite('vr_to205_09', 3)	# 20-22
    sprite('vr_to205_10', 3)	# 23-25
    sprite('vr_to205_11', 2)	# 26-27

@State
def Zanzoh5D_2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3004(-25)
    sprite('vr_to205_12', 12)	# 1-12

@State
def Zanzoh5DD():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_to206_00', 2)	# 1-2
    Unknown1072(50000)
    sprite('vr_to206_00', 2)	# 3-4
    Unknown1072(0)
    sprite('vr_to206_00', 2)	# 5-6
    Unknown1072(-60000)

@State
def Zanzoh5DD_2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_to206_10', 3)	# 1-3
    sprite('vr_to206_11', 2)	# 4-5
    sprite('vr_to206_12', 2)	# 6-7

@State
def Zanzoh5DD_3():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3004(-25)
    sprite('vr_to206_13', 12)	# 1-12

@State
def ZanzohAir5C():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3004(-25)
    sprite('vr_to254_00', 3)	# 1-3
    sprite('vr_to254_01', 12)	# 4-15

@State
def ZanzohAir5D():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_to255_01', 2)	# 1-2
    sprite('vr_to255_02', 2)	# 3-4
    sprite('vr_to255_00', 2)	# 5-6
    sprite('vr_to255_01', 2)	# 7-8
    sprite('vr_to255_02', 2)	# 9-10

@State
def ZanzohAir5D_2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_to255_10', 3)	# 1-3
    sprite('vr_to255_11', 2)	# 4-5
    sprite('vr_to255_12', 2)	# 6-7
    sprite('vr_to255_13', 2)	# 8-9
    sprite('vr_to255_14', 1)	# 10-10

@State
def ZanzohAir5D_3():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3004(-25)
    sprite('vr_to255_15', 12)	# 1-12

@State
def Hyper_Counter_Barrier():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('636565665f3430305f626172726965722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1096(1250)
        Unknown3001(159)
    sprite('null', 16)	# 1-16
    Unknown1099(2)
    Unknown3004(-3)
    sprite('null', 22)	# 17-38
    Unknown1099(3)

@State
def Hyper_Counter_Barrier_r():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('636565665f3430305f626172726965725f722e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1096(1250)
        Unknown3001(159)
    sprite('null', 16)	# 1-16
    Unknown1099(2)
    Unknown3004(-3)
    sprite('null', 22)	# 17-38
    Unknown1099(3)

@State
def Hyper_Counter_kick():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3004(-35)
    sprite('vr_ce401_00', 16)	# 1-16
    GFX_1('ceef_tornadokick', 0)
    GFX_1('ceef_tornadokick', 1)

@State
def Hyper_Counter_kick_oku():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(16000)
        Unknown1007(48000)
        Unknown3004(-35)
    sprite('vr_ce401_00', 16)	# 1-16
    GFX_1('ceef_tornadokick', 0)
    GFX_1('ceef_tornadokick', 1)

@State
def ceef_403_kick():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('636565665f3430335f6b69636b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(1)
        Unknown4061(2)
        Unknown23122(240)
        Unknown1096(675)
        teleportRelativeX(-20000)
        Unknown1007(10000)
    sprite('null', 10)	# 1-10
    sprite('null', 4)	# 11-14
    Unknown3004(-64)

@State
def Nouten_stump():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_ce403_20', 3)	# 1-3
    sprite('vr_ce403_21', 3)	# 4-6

@State
def Nouten_stump_hit():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown4007(0)
        Unknown4010(2)
        teleportRelativeX(-64000)
        Unknown3004(-20)
    sprite('vr_ce403_22', 16)	# 1-16

@State
def __100InchPanch_hand():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_100inch_hand')
    sprite('null', 5)	# 1-5
    sprite('null', 5)	# 6-10
    sprite('null', 5)	# 11-15
    sprite('null', 5)	# 16-20
    sprite('null', 5)	# 21-25
    sprite('null', 5)	# 26-30
    sprite('null', 5)	# 31-35
    sprite('null', 5)	# 36-40

@State
def __100InchPanch_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(64000)
    sprite('null', 1)	# 1-1
    GFX_1('ceef_100inch_add', 100)

@State
def __100InchPanch_dash():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
        Unknown1007(220000)
    sprite('null', 2)	# 1-2
    GFX_1('ceef_100inch_dash', 100)

@State
def DragonKick_Launcher():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown1007(-12000)
    sprite('null', 1)	# 1-1
    GFX_1('ceef_dragonkick_launcher_01', 100)

@State
def DragonKick():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown1072(-30000)
        Unknown1056(1500)
    sprite('vr_ce404_00', 2)	# 1-2
    GFX_1('ceef_dragonkick_00', 0)
    sprite('vr_ce404_01', 2)	# 3-4
    GFX_1('ceef_dragonkick_00', 0)
    sprite('vr_ce404_02', 2)	# 5-6
    GFX_1('ceef_dragonkick_00', 0)
    sprite('vr_ce404_03', 2)	# 7-8
    Unknown1099(-100)
    GFX_1('ceef_dragonkick_00', 0)
    sprite('vr_ce404_00', 2)	# 9-10
    GFX_1('ceef_dragonkick_00', 0)
    sprite('vr_ce404_01', 2)	# 11-12
    GFX_1('ceef_dragonkick_00', 0)
    sprite('vr_ce404_02', 2)	# 13-14
    sprite('vr_ce404_03', 2)	# 15-16

@State
def Zanzoh_DragonKick():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_to404_00', 2)	# 1-2

@State
def Zanzoh_DragonKick_2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3004(-25)
    sprite('vr_to404_01', 12)	# 1-12
    GFX_1('toef_dragonkick_07', 0)

@State
def KokutengekiCEtameC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_2('ceef_kokutengeki_02')
        Unknown4007(2)
    sprite('null', 5)	# 1-5
    sprite('null', 5)	# 6-10
    Unknown3004(-51)

@State
def KokutengekiCEtameEX():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_2('ceef_kokutengeki_02')
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 4002):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 5)	# 32768-32772
    Unknown3004(-51)

@State
def KokutengekiTameC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown3001(0)
    sprite('null', 8)	# 1-8
    Unknown3004(104)
    Unknown1099(-100)
    GFX_0('KokutengekiTameSphereC', 100)
    sprite('null', 3)	# 9-11
    Unknown3001(0)
    GFX_0('KokutengekiBomb', 100)

@State
def KokutengekiTameSphereC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('636565665f3430355f74616d655f7370686572652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
    sprite('null', 8)	# 1-8
    Unknown3004(104)
    Unknown1099(-30)
    sprite('null', 3)	# 9-11
    Unknown3001(0)

@State
def KokutengekiTameLineC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('636565665f3430355f73656e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
    sprite('null', 5)	# 1-5
    Unknown3004(104)
    sprite('null', 8)	# 6-13
    Unknown3004(-68)

@State
def KokutengekiTameD():

    def upon_IMMEDIATE():
        GFX_2('toef_kokutenstart_03')
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 4002):
                sendToLabel(1)
    sprite('null', 1)	# 1-1
    label(0)
    sprite('null', 17)	# 2-18
    GFX_0('KokutengekiTameSphereD', 100)
    GFX_0('KokutengekiTameLineD', 100)
    gotoLabel(0)
    label(1)
    sprite('null', 5)	# 19-23
    GFX_0('KokutengekiBomb', 100)

@State
def KokutengekiTameSphereD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('636565665f3430355f74616d655f7370686572652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
    sprite('null', 17)	# 1-17
    Unknown3004(52)
    Unknown1099(-10)
    sprite('null', 5)	# 18-22
    Unknown3001(0)

@State
def KokutengekiTameLineD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('636565665f3430355f73656e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
    sprite('null', 7)	# 1-7
    Unknown3004(52)
    sprite('null', 15)	# 8-22
    Unknown3004(-34)

@State
def KokutengekiTameCD():

    def upon_IMMEDIATE():
        GFX_2('toef_kokutenstart_03')
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 12)	# 1-12
    GFX_0('KokutengekiTameSphereCD', 100)
    GFX_0('KokutengekiTameLineCD', 100)
    sprite('null', 3)	# 13-15
    Unknown3001(0)
    GFX_0('KokutengekiBomb', 100)

@State
def KokutengekiTameSphereCD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('636565665f3430355f74616d655f7370686572652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown3001(0)
    sprite('null', 12)	# 1-12
    Unknown3004(78)
    Unknown1099(-30)
    sprite('null', 3)	# 13-15
    Unknown3001(0)

@State
def KokutengekiTameLineCD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('636565665f3430355f73656e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown3001(0)
        Unknown1096(1400)
    sprite('null', 9)	# 1-9
    Unknown1099(-60)
    Unknown3004(78)
    sprite('null', 5)	# 10-14
    Unknown3004(-51)

@State
def KokutengekiBomb():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3430355f68616a696b6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
    sprite('null', 1)	# 1-1
    Unknown1099(50)
    GFX_0('KokutengekiBombGroundshock', 100)
    GFX_1('toef_kokutenend_07', 100)
    SFX_3('bomb_l')
    sprite('null', 4)	# 2-5
    SFX_3('bomb_l')
    sprite('null', 5)	# 6-10
    Unknown3004(-52)
    GFX_0('KokutengekiBombCircle', 100)

@State
def KokutengekiBombCircle():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3430355f68616a696b6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
    sprite('null', 5)	# 1-5
    Unknown1099(10)
    sprite('null', 5)	# 6-10
    Unknown3004(-52)

@State
def KokutengekiBombGroundshock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3430355f67726f756e6473686f636b2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(4)
        Unknown1007(-350000)
    sprite('null', 10)	# 1-10
    GFX_1('toef_kokutengroundsmoke_00', 100)
    Unknown1059(80)
    Unknown1067(-10)
    Unknown3004(-26)

@State
def Chargestart():

    def upon_IMMEDIATE():
        GFX_2('ceef_startcharge_06')
        Unknown2054(1)
    sprite('null', 80)	# 1-80

@State
def ChargeAModel():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433315f63686172676530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3001(0)
        Unknown1056(1400)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    sprite('null', 20)	# 11-30
    Unknown3004(-17)

@State
def ChargeBModel():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433315f63686172676530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('ceef_jizokucharge_02')
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    Unknown1059(30)
    sprite('null', 15)	# 11-25
    GFX_1('ceef_endcharge_01', 100)
    Unknown1059(0)
    sprite('null', 10)	# 26-35
    Unknown3004(-26)
    Unknown1059(30)

@State
def ChargeABModel():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433315f63686172676530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('ceef_jizokucharge_02')
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    Unknown1059(30)
    sprite('null', 23)	# 11-33
    GFX_1('ceef_endcharge_01', 100)
    Unknown1059(0)
    sprite('null', 10)	# 34-43
    Unknown3004(-26)
    Unknown1059(30)

@State
def GodHandKobusiKumo():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433305f676f6468616e645f6b756d6f2e44494700000000000000636565665f3433305f676f6468616e645f6b756d6f5f303030302e6d6d6f7400')
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 5)	# 1-5
    physicsYImpulse(-2000)
    sprite('null', 15)	# 6-20
    Unknown1059(-7)
    Unknown3004(6)
    sprite('null', 45)	# 21-65
    sprite('null', 10)	# 66-75
    Unknown1059(30)
    Unknown3004(-26)
    GFX_0('GodHandKobusiKumoBrake', 100)

@State
def GodHandKobusiKumoBrake():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433305f676f6468616e645f6b756d6f6272616b652e44494700000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
    sprite('null', 15)	# 1-15
    Unknown1059(30)
    Unknown3004(-17)

@State
def GodHandKobusiKumoShock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433305f676f6468616e645f6b756d6f656e642e444947000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
    sprite('null', 15)	# 1-15
    Unknown1059(30)
    Unknown3004(-17)

@State
def GodHandKobusi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(4)
        Unknown2007()
        Unknown1007(100000)
    sprite('vr_to430_godhand', 4)	# 1-4
    physicsYImpulse(-70000)
    sprite('vr_to430_godhand', 1)	# 5-5
    physicsYImpulse(0)
    SFX_3('quake_l')
    sprite('vr_to430_godhand', 4)	# 6-9
    SFX_3('quake_l')
    sprite('vr_to430_godhand', 15)	# 10-24
    Unknown3004(-17)

@State
def GodHandKobusiCD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(4)
        Unknown2007()
        Unknown1096(1200)
        Unknown1007(100000)
    sprite('vr_to430_godhand', 4)	# 1-4
    physicsYImpulse(-70000)
    sprite('vr_to430_godhand', 1)	# 5-5
    physicsYImpulse(0)
    SFX_3('quake_l')
    sprite('vr_to430_godhand', 4)	# 6-9
    SFX_3('quake_l')
    sprite('vr_to430_godhand', 15)	# 10-24
    Unknown3004(-17)

@State
def GodHandKobusiWind():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433305f676f6468616e645f77696e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 30)	# 1-30
    Unknown3004(-9)
    Unknown1059(20)
    GFX_0('GodHandKobusiKumoShock', 100)

@State
def GodHandKobusiWindCD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433305f676f6468616e645f77696e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1200)
    sprite('null', 30)	# 1-30
    Unknown3004(-9)
    Unknown1059(20)
    GFX_0('GodHandKobusiKumoShock', 100)

@State
def meteo_takusanC():

    def upon_IMMEDIATE():
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        Unknown48('19000000020000003300000003000000020000003b000000')
        if SLOT_51:
            pass
    label(1)
    sprite('null', 10)	# 1-10
    teleportRelativeX(-730000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 11-15
    teleportRelativeX(-130000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 16-25
    teleportRelativeX(370000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 26-30
    teleportRelativeX(-700000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 31-40
    teleportRelativeX(600000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 41-45
    teleportRelativeX(-500000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 46-55
    teleportRelativeX(400000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 56-60
    teleportRelativeX(-300000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 61-70
    teleportRelativeX(600000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 71-75
    teleportRelativeX(-400000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 90)	# 76-165
    label(0)
    sprite('null', 1)	# 166-166

@State
def meteo_takusanC_OD():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        Unknown48('19000000020000003300000003000000020000003b000000')
        if SLOT_51:
            pass
    label(1)
    sprite('null', 10)	# 1-10
    teleportRelativeX(-730000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 11-15
    teleportRelativeX(-130000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 16-25
    teleportRelativeX(370000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 26-30
    teleportRelativeX(-700000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 31-40
    teleportRelativeX(600000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 41-45
    teleportRelativeX(-500000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 46-55
    teleportRelativeX(400000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 56-60
    teleportRelativeX(-300000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 61-70
    teleportRelativeX(600000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 71-75
    teleportRelativeX(-400000)
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 90)	# 76-165
    label(0)
    sprite('null', 1)	# 166-166

@State
def meteo_takusanD():

    def upon_IMMEDIATE():
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        Unknown48('19000000020000003300000003000000020000003b000000')
        if SLOT_51:
            pass
    label(1)
    sprite('null', 10)	# 1-10
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 11-15
    teleportRelativeX(-100000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 16-25
    teleportRelativeX(400000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 26-30
    teleportRelativeX(-700000)
    GFX_0('meteo_col', 100)
    SFX_3('ce004')
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 31-40
    teleportRelativeX(600000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 41-45
    teleportRelativeX(-600000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 46-55
    teleportRelativeX(350000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 56-60
    teleportRelativeX(-270000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 61-70
    teleportRelativeX(600000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 71-75
    teleportRelativeX(-400000)
    GFX_0('meteo_col', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 90)	# 76-165
    label(0)
    sprite('null', 1)	# 166-166

@State
def meteo_takusanD_OD():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        Unknown48('19000000020000003300000003000000020000003b000000')
        if SLOT_51:
            pass
    label(1)
    sprite('null', 10)	# 1-10
    Unknown23033(-55)
    GFX_0('meteo_col_OD', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 11-15
    teleportRelativeX(-100000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 16-25
    teleportRelativeX(400000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 26-30
    teleportRelativeX(-700000)
    GFX_0('meteo_col_OD', 100)
    SFX_3('ce004')
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 31-40
    teleportRelativeX(600000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 41-45
    teleportRelativeX(-600000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 46-55
    teleportRelativeX(350000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 56-60
    teleportRelativeX(-270000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 10)	# 61-70
    teleportRelativeX(600000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 71-75
    teleportRelativeX(-400000)
    GFX_0('meteo_col_OD', 100)
    Unknown23033(-55)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 90)	# 76-165
    label(0)
    sprite('null', 1)	# 166-166

@State
def meteo_takusanCD():

    def upon_IMMEDIATE():
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        Unknown2005()
        sendToLabelUpon(54, 0)
        Unknown48('19000000020000003300000003000000020000003b000000')
        if SLOT_51:
            SLOT_31 = 0
        Unknown1086(22)
        teleportRelativeX(450000)
    label(1)
    sprite('null', 5)	# 1-5
    sprite('null', 3)	# 6-8
    teleportRelativeX(-900000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 9-11
    teleportRelativeX(-370000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 12-16
    teleportRelativeX(800000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 17-19
    teleportRelativeX(-800000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 20-24
    teleportRelativeX(200000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 25-27
    teleportRelativeX(600000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 28-32
    teleportRelativeX(-500000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 33-35
    teleportRelativeX(400000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 36-38
    teleportRelativeX(-900000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 39-43
    teleportRelativeX(800000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 0)	# 44-43
    teleportRelativeX(-500000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 44-48
    teleportRelativeX(-400000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 49-51
    teleportRelativeX(900000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    SFX_3('ce004')
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 52-54
    teleportRelativeX(-370000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 5)	# 55-59
    teleportRelativeX(800000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 3)	# 60-62
    teleportRelativeX(-800000)
    Unknown23033(-55)
    GFX_0('meteo_col', 100)
    callSubroutine('ChargeDamageUp_meteo')
    sprite('null', 90)	# 63-152
    label(0)
    sprite('null', 1)	# 153-153

@Subroutine
def ChargeDamageUp_meteo():
    if (SLOT_51 == 1):
        Unknown23029(1, 5001, 0)
    if (SLOT_51 == 2):
        Unknown23029(1, 5002, 0)
    if (SLOT_51 == 3):
        Unknown23029(1, 5003, 0)

@State
def meteo_col():

    def upon_IMMEDIATE():
        Unknown3001(0)
        Unknown2011()
        AttackLevel_(5)
        Damage(740)
        AttackP2(95)
        Unknown11091(15)
        Unknown9017(1)
        Unknown9021(1)
        Hitstop(0)
        AirUntechableTime(42)
        Unknown9154(30)
        AirPushbackY(10000)
        PushbackX(15000)
        Unknown53(0)
        physicsYImpulse(-50000)
        physicsXImpulse(50000)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        Unknown23015(4)

        def upon_LANDING():
            Unknown23090(25)
            SFX_3('bomb_m')

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown10000(120)
            if (SLOT_48 == 5002):
                Unknown10000(200)
            if (SLOT_48 == 5003):
                Unknown10000(300)
    sprite('vr_to432_col', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    GFX_0('meteo', 0)
    label(1)
    sprite('vr_to432_col', 2)	# 2-3	 **attackbox here**
    GFX_1('toef_meteosmoke_01', 0)
    gotoLabel(1)
    label(0)
    sprite('vr_to432_col', 1)	# 4-4	 **attackbox here**
    GFX_1('toef_meteobrake_09', 0)
    ScreenShake(0, 5000)

@State
def meteo_col_OD():

    def upon_IMMEDIATE():
        Unknown3001(0)
        Unknown2011()
        AttackLevel_(5)
        Damage(960)
        AttackP2(95)
        Unknown11091(15)
        Unknown9017(1)
        Unknown9021(1)
        Hitstop(0)
        AirUntechableTime(42)
        Unknown9154(30)
        AirPushbackY(10000)
        PushbackX(15000)
        Unknown53(0)
        physicsYImpulse(-50000)
        physicsXImpulse(50000)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        Unknown23015(4)

        def upon_LANDING():
            Unknown23090(25)
            SFX_3('bomb_m')

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown10000(120)
            if (SLOT_48 == 5002):
                Unknown10000(200)
            if (SLOT_48 == 5003):
                Unknown10000(300)
    sprite('vr_to432_col', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    GFX_0('meteo', 0)
    label(1)
    sprite('vr_to432_col', 2)	# 2-3	 **attackbox here**
    GFX_1('toef_meteosmoke_01', 0)
    gotoLabel(1)
    label(0)
    sprite('vr_to432_col', 1)	# 4-4	 **attackbox here**
    GFX_1('toef_meteobrake_09', 0)
    ScreenShake(0, 5000)

@State
def meteo():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('636565665f3433325f6d6574656f2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('toef_meteomoe_01')
        Unknown4010(2)
        Unknown4007(2)
        Unknown1072(45000)
        Unknown23015(4)
    sprite('null', 32767)	# 1-32767

@State
def meteoStartAura():

    def upon_IMMEDIATE():
        GFX_2('toef_godaura_11')
        Unknown4010(2)
        Unknown2054(1)
    sprite('null', 44)	# 1-44

@State
def PCE_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('160000006800000070a0feff50c3000000000000000000000000000000000000')
        callSubroutine('PCE_DDAttackInit')
        Unknown2012()
        Unknown4009(3)
        Unknown23066(1)
        Unknown2053(1)
        callSubroutine('PCE_CheckWarp')
    sprite('to450_02', 3)	# 1-3
    Unknown23022(1)
    teleportRelativeY(0)
    sprite('to450_00', 2)	# 4-5
    sprite('to450_00', 2)	# 6-7
    sprite('to450_01', 3)	# 8-10
    sprite('to450_02', 3)	# 11-13
    sprite('to450_00', 3)	# 14-16
    GFX_0('IchigekiDragonAtk', 0)
    sprite('to450_01', 3)	# 17-19
    sprite('to450_02', 3)	# 20-22
    sprite('to450_03', 3)	# 23-25
    sprite('to450_04', 3)	# 26-28
    sprite('to450_05', 3)	# 29-31
    sprite('to450_06', 3)	# 32-34
    sprite('to450_07', 3)	# 35-37
    sprite('to450_08', 3)	# 38-40
    sprite('to450_09', 1)	# 41-41	 **attackbox here**
    Unknown23027()
    physicsYImpulse(60000)
    setGravity(0)
    sprite('to450_09', 1)	# 42-42	 **attackbox here**
    YAccel(30)
    sprite('to450_10', 2)	# 43-44
    YAccel(30)
    sprite('to450_11', 2)	# 45-46
    YAccel(30)
    sprite('to450_09', 2)	# 47-48	 **attackbox here**
    YAccel(30)
    sprite('to450_10', 2)	# 49-50
    YAccel(20)
    sprite('to450_11', 2)	# 51-52
    YAccel(10)
    sprite('to450_09', 2)	# 53-54	 **attackbox here**
    YAccel(0)
    sprite('to450_10', 2)	# 55-56
    sprite('to450_11', 2)	# 57-58
    sprite('to450_09', 2)	# 59-60	 **attackbox here**
    sprite('to450_10', 2)	# 61-62
    sprite('to450_11', 2)	# 63-64
    sprite('to450_09', 4)	# 65-68	 **attackbox here**
    sprite('to450_10', 4)	# 69-72
    sprite('to450_11', 4)	# 73-76
    sprite('to450_09', 6)	# 77-82	 **attackbox here**
    sprite('to450_10', 6)	# 83-88
    sprite('to450_11', 6)	# 89-94
    sprite('to450_09', 6)	# 95-100	 **attackbox here**
    sprite('to450_10', 6)	# 101-106
    sprite('to450_11', 6)	# 107-112
    sprite('keep', 32767)	# 113-32879
    enterState('PersonaDeleteAndIdling')

@State
def IchigekiDragonAtk():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown2012()
        AttackLevel_(5)
        Hitstop(7)
        Damage(0)
        Unknown11064(1)
        AirPushbackX(0)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(10000)
        Unknown9310(60)
        Unknown11031(0)

        def upon_12():
            Unknown21007(3, 32)
        Unknown11033(3)
    sprite('null', 5)	# 1-5
    GFX_0('IchigekiMizubasira', 100)
    GFX_0('IchigekiMizubasira01', 100)
    SFX_3('blaze_normal')
    sprite('null', 5)	# 6-10
    SFX_3('blaze_normal')
    sprite('null', 5)	# 11-15
    SFX_3('blaze_normal')
    sprite('null', 5)	# 16-20
    SFX_3('blaze_normal')
    sprite('null', 5)	# 21-25
    SFX_3('blaze_normal')
    sprite('null', 5)	# 26-30
    SFX_3('blaze_normal')
    sprite('dmy_atk00', 3)	# 31-33
    GFX_0('IchigekiMizubasira05', 100)
    GFX_0('IchigekiDoragon3D', 100)
    StartMultihit()
    sprite('dmy_atk00', 15)	# 34-48
    RefreshMultihit()
    sprite('dmy_atk00', 30)	# 49-78
    Unknown2001()
    sprite('dmy_atk00', 20)	# 79-98

@State
def IchigekiDoragon3D():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('636565665f3435305f7761746572647261676f6e2e4449470000000000000000636565665f3435305f7761746572647261676f6e5f303030302e6d6d6f740000')
        Unknown4010(2)
        Unknown4009(2)
        teleportRelativeX(100000)
        Unknown1007(150000)
    sprite('null', 20)	# 1-20
    GFX_0('IchigekiDoragonHead3D', 100)
    ScreenShake(0, 50000)
    SFX_3('ce000')
    sprite('null', 20)	# 21-40
    Unknown3004(-13)

@State
def IchigekiDoragonHead3D():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('636565665f3435305f7761746572647261676f6e5f686561642e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
    sprite('null', 10)	# 1-10
    sprite('null', 30)	# 11-40
    physicsYImpulse(30000)

@State
def IchigekiMizubasira():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('636565665f3435305f7761746572636f6c756d6e30302e444947000000000000636565665f3435305f7761746572636f6c756d6e30305f303030302e6d6d6f00')
        Unknown3001(0)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4015()
    sprite('null', 45)	# 1-45
    GFX_1('toef_itigeki_tame_06', 100)
    sprite('null', 10)	# 46-55
    teleportRelativeY(5000)
    Unknown1096(1150)
    Unknown3004(51)
    sprite('null', 30)	# 56-85
    sprite('null', 10)	# 86-95
    Unknown3004(-51)

@State
def IchigekiMizubasira01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('636565665f3435305f7761746572636f6c756d6e30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown3001(0)
        Unknown4009(2)
        Unknown4015()
        Unknown1007(100000)
    sprite('null', 30)	# 1-30
    Unknown3004(9)
    sprite('null', 50)	# 31-80
    Unknown1099(0)
    sprite('null', 10)	# 81-90

@State
def IchigekiMizubasira05():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4010(2)
        GFX_2('toef_itigeki_mizubasira_05')
    sprite('null', 60)	# 1-60
    Unknown1007(200000)
    sprite('null', 50)	# 61-110
    Unknown3004(-10)

@State
def ChargeIchigekiModel():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f3433315f63686172676530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('ceef_jizokucharge_02')
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    Unknown1059(30)
    sprite('null', 120)	# 11-130
    GFX_1('ceef_endcharge_01', 100)
    Unknown1059(0)
    sprite('null', 10)	# 131-140
    Unknown3004(-26)
    Unknown1059(30)

@State
def IchigekiJumpSmoke():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('636565665f3435305f79756b6b7572695f736d6f6b652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 20)	# 1-20
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(1)
        Unknown6001(1)
        Unknown1001(640000)
        Unknown4061(0)
        teleportRelativeY(-384000)
        Unknown1007(500000)
        Unknown1096(2000)
        teleportRelativeX(310000)
        Unknown2054(1)
    sprite('ichigeki0', 5)	# 1-5
    Unknown1099(-200)
    sprite('ichigeki0', 30)	# 6-35
    Unknown1099(0)
    sprite('keep', 30)	# 36-65
    sprite('keep', 60)	# 66-125
    Unknown3004(-5)

@State
def IchiHaikei():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(-100)
        Unknown4061(7)
        Unknown1096(3000)
        Unknown2054(1)
    sprite('vr_ce450bg', 30)	# 1-30
    GFX_0('IchiScrew', 0)
    sprite('vr_ce450bg', 30)	# 31-60
    sprite('vr_ce450bg', 60)	# 61-120
    Unknown3004(-5)

@State
def IchiScrew():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2005()
        Unknown23032(50)
        Unknown23033(50)
        Unknown2019(-100)
        Unknown2054(1)
        Unknown21010(1)
        GFX_2('ceef_shutyusen_01')
        Unknown4003('636565665f3435305f637574696e757a7530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 100)	# 1-100
    GFX_1('ceef_deathkira_la', 100)
    Unknown3004(51)
    sprite('null', 10)	# 101-110
    Unknown3004(-26)

@State
def IchigekiWinRainbow():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('636565665f3435305f5261696e626f772e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 90)	# 1-90
    sprite('null', 30)	# 91-120
    Unknown3004(-9)

@State
def IchigekiCamera():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)
        sendToLabelUpon(37, 5)
        Unknown3029(1)
        Unknown3032()
        Unknown3001(80)
        Unknown3038(1)
    sprite('dmy_camera', 32767)	# 1-32767
    label(0)
    sprite('keep', 32767)	# 32768-65534
    if SLOT_38:
        op(2, 2, 52, 0, -1)
        SLOT_22 = SLOT_0
        op(2, 2, 53, 0, -1)
        SLOT_23 = SLOT_0
    else:
        SLOT_22 = SLOT_52
        SLOT_23 = SLOT_53
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(1)
    sprite('keep', 12)	# 65535-65546
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('keep', 15)	# 65547-65561
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown20001(1)
    Unknown1086(22)
    Unknown1007(900000)
    Unknown4007(22)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    physicsYImpulse(-1428)
    setGravity(314)
    sprite('keep', 10)	# 65562-65571
    sprite('keep', 10)	# 65572-65581
    setGravity(2200)
    Unknown4004('534345465f41737452797568616955707065720000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(2000000)
    Unknown35()
    sprite('keep', 10)	# 65582-65591
    sprite('keep', 32767)	# 65592-98358
    label(2)
    sprite('keep', 18)	# 98359-98376
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('keep', 10)	# 98377-98386
    Unknown26('SCEF_ShashaIn')
    Unknown4004('534345465f5368617368614f757400000000000000000000000000000000000064000000')
    Unknown26('SCEF_AstRyuhaiUpper')
    Unknown4007(0)
    Unknown1086(3)
    teleportRelativeX(390000)
    Unknown1007(300000)
    Unknown1084(1)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown20001(1)
    sprite('keep', 32767)	# 98387-131153
    Unknown26('SCEF_FadeBlack12In')
    label(3)
    sprite('keep', 50)	# 131154-131203

    def upon_3():
        SLOT_105 = (SLOT_105 + (-3))
    sprite('keep', 32767)	# 131204-163970
    clearUponHandler(3)
    label(4)
    sprite('keep', 32767)	# 163971-196737
    SLOT_51 = 0
    Unknown20009(1000)
    Unknown1084(1)
    Unknown1086(3)
    teleportRelativeY(0)

@State
def IchigekiCopyZanzoh():
    sprite('null', 60)	# 1-60
    Unknown2019(100)
    Unknown23053('1900000003000000')
    Unknown3032()
    Unknown3004(-1)
    sprite('keep', 300)	# 61-360
    Unknown3004(-5)

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

        def upon_3():
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

@State
def PersonaMatchWin():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23023()
        Unknown23184('0300000064000000701101001873010000000000000000000000000000000000')
        callSubroutine('PCE_AttackInit')
        callSubroutine('PCE_CheckWarp')
        Unknown2053(1)
        Unknown2019(-100)
        Unknown23022(1)
        Unknown23015(0)
    sprite('to611_00', 4)	# 1-4
    sprite('to611_01', 4)	# 5-8
    sprite('to611_02', 4)	# 9-12
    sprite('to611_03', 4)	# 13-16
    sprite('to611_04', 4)	# 17-20
    sprite('to611_05', 4)	# 21-24
    label(0)
    sprite('to611_03', 4)	# 25-28
    sprite('to611_04', 4)	# 29-32
    sprite('to611_05', 4)	# 33-36
    loopRest()
    gotoLabel(0)

@State
def MatchWin2_bikkuri():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 7)	# 1-7
    sprite('null', 5)	# 8-12
    Unknown1096(0)
    Unknown1099(200)
    Unknown2007()
    GFX_2('ceef_matchwin2')
    sprite('null', 32767)	# 13-32779
    Unknown1096(1000)
    Unknown1099(0)