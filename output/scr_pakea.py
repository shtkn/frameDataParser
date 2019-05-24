@State
def PAK_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('50414b5f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PAK_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PAK_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PAK_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 2050):
            Unknown23185('50414b5f506572736f6e6135413674680000000000000000000000000000000032000000')
        if (SLOT_48 == 2040):
            Unknown23185('50414b5f506572736f6e6143410000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2540):
            Unknown23185('50414b5f506572736f6e614a430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 4320):
            Unknown23185('50414b5f506572736f6e614d6168616a696f6461696e00000000000000000000c8000000')
        if (SLOT_48 == 4321):
            Unknown23185('50414b5f506572736f6e614d6168616a696f6461696e53500000000000000000c8000000')
        if (SLOT_48 == 4322):
            Unknown23185('50414b5f506572736f6e614d6168616a696f6461696e44534400000000000000c8000000')
        if (SLOT_48 == 4323):
            Unknown23185('50414b5f506572736f6e614d6168616a696f6461696e44534453500000000000c8000000')
        if (SLOT_48 == 4500):
            Unknown23185('50414b5f506572736f6e614963686967656b69000000000000000000000000002c010000')
        if (SLOT_48 == 9999):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')
        if (SLOT_48 == 6100):
            Unknown23185('50414b5f506572736f6e614d6174636857696e000000000000000000000000002c010000')

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
    Unknown3031()

@Subroutine
def PAK_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PAK_AttackInit():
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
    callSubroutine('PAK_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAK_SPAttackInit():
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
    callSubroutine('PAK_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAK_DDAttackInit():
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
    callSubroutine('PAK_ReceptionSignal')
    Unknown23023()

@Subroutine
def PAK_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PAK_ForceWarp():
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
    enterState('PAK_PersonaWait')

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
        callSubroutine('PAK_ReceptionSignal')
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
def PAK_Persona5A6th():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000803801000000000000000000804f12000000000000000000')
        callSubroutine('PAK_AttackInit')
        AttackLevel_(3)
        Damage(500)
        AttackP1(90)
        Unknown23078(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11044(1)
        Unknown2053(1)
        Unknown2017(0)
        callSubroutine('PAK_CheckWarp')
        Unknown23059(1)

        def upon_78():
            Unknown23029(3, 2051, 0)
            Hitstop(0)
            enterState('PAK_Persona5A6th_Plus')
    sprite('cs208_00', 6)	# 1-6
    Unknown2015(140)
    sprite('cs208_01', 6)	# 7-12
    sprite('cs208_02', 2)	# 13-14
    SFX_3('hit_m_middle')
    sprite('cs208_03', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('cs208_03', 3)	# 16-18	 **attackbox here**
    Unknown23022(0)
    GFX_1('ef_thunder_damage_g', 1)
    sprite('cs208_03', 4)	# 19-22	 **attackbox here**
    StartMultihit()
    sprite('cs208_04', 6)	# 23-28
    sprite('cs208_05', 6)	# 29-34
    sprite('cs208_06', 6)	# 35-40
    StartMultihit()
    sprite('cs208_07', 6)	# 41-46
    sprite('keep', 32767)	# 47-32813
    enterState('PersonaDeleteAndIdling')

@State
def PAK_Persona5A6th_Plus():

    def upon_IMMEDIATE():
        callSubroutine('PAK_AttackInit')
        Unknown17011('PAK_Persona5A6th_Exe', 1, 0, 0)
        Unknown11002(-1)
        AttackLevel_(3)
        Damage(0)
        AttackP1(90)
        AttackP2(100)
        Hitstop(20)
        Unknown11045(0)
        Unknown30061(1)
        setInvincible(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11034(1)
        Unknown11033(0)
        Unknown2053(1)
        Unknown2017(0)
        callSubroutine('PAK_CheckWarp')

        def upon_78():
            Hitstop(0)
    sprite('keep', 1)	# 1-1
    sprite('cs208_04', 6)	# 2-7
    setInvincible(0)
    sprite('cs208_05', 6)	# 8-13
    sprite('cs208_06', 6)	# 14-19
    StartMultihit()
    sprite('cs208_07', 6)	# 20-25
    sprite('keep', 32767)	# 26-32792
    enterState('PersonaDeleteAndIdling')

@State
def PAK_Persona5A6th_Exe():

    def upon_IMMEDIATE():
        callSubroutine('PAK_AttackInit')
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        Damage(300)
        AttackP1(90)
        Unknown11092(1)
        Unknown11091(0)
        AirPushbackY(-120000)
        AirPushbackX(10000)
        Unknown9190(1)
        Unknown9118(30)
        AirUntechableTime(60)
        Unknown11068(1)
        Hitstop(0)
        Unknown30079(1)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11064(1)
        Unknown23022(1)
        Unknown2017(1)
        Unknown2053(1)
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PAK_CheckWarp')
    sprite('cs209_00', 5)	# 1-5	 **attackbox here**
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('cs209_01', 5)	# 6-10	 **attackbox here**
    sprite('cs209_00', 5)	# 11-15	 **attackbox here**
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown23119(-10420288, 3, 10)
    Unknown4054(12)
    Unknown4045('637365665f32303900000000000000000000000000000000000000000000000001000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000000000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000001000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000002000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000003000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000004000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000005000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000006000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000007000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000008000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000009000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f67000000000000000000000000000a000000')
    sprite('cs209_01', 5)	# 16-20	 **attackbox here**
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('cs209_00', 5)	# 21-25	 **attackbox here**
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000000000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000001000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000002000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000003000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000004000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000005000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000006000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000007000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000008000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000009000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f67000000000000000000000000000a000000')
    sprite('cs209_01', 5)	# 26-30	 **attackbox here**
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('cs209_00', 5)	# 31-35	 **attackbox here**
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000000000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000001000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000002000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000003000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000004000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000005000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000006000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000007000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000008000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f670000000000000000000000000009000000')
    Unknown4054(12)
    Unknown4045('65665f7468756e6465725f64616d6167655f67000000000000000000000000000a000000')
    sprite('cs209_01', 5)	# 36-40	 **attackbox here**
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('cs209_02', 10)	# 41-50
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('cs209_03', 1)	# 51-51
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('cs209_04', 3)	# 52-54	 **attackbox here**
    Unknown5000(26, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Damage(1500)
    Unknown1084(1)
    Unknown30079(0)
    Unknown11064(0)
    ScreenShake(1000, 15000)
    SFX_3('down_steal_m')
    SFX_3('counter_hit_l45')
    Unknown23029(3, 2052, 0)
    sprite('cs209_05', 3)	# 55-57
    sprite('cs209_06', 5)	# 58-62
    sprite('cs209_07', 13)	# 63-75
    sprite('keep', 32767)	# 76-32842
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaCA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff0000000000cbf3ffa0f019000000000000000000')
        callSubroutine('PAK_AttackInit')
        Unknown2017(0)
        Unknown2053(0)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('PAK_CheckWarp')
        Unknown2003(1)
        Unknown23022(1)
        Unknown23059(1)
    sprite('cs204_00', 3)	# 1-3
    sprite('cs204_01', 2)	# 4-5
    sprite('cs204_02', 2)	# 6-7
    sprite('cs204_03', 3)	# 8-10
    sprite('cs204_04', 3)	# 11-13
    sprite('cs204_05', 2)	# 14-15
    sprite('cs204_06', 2)	# 16-17
    SFX_3('slash_sword_middle')
    GFX_0('Zanzoh5C', 100)
    sprite('cs204_07', 1)	# 18-18	 **attackbox here**
    ScreenShake(20000, 20000)
    SFX_3('bomb_m')
    SFX_3('attack_offset')
    sprite('cs204_07', 2)	# 19-20	 **attackbox here**
    sprite('cs204_07', 2)	# 21-22	 **attackbox here**
    Unknown23022(0)
    sprite('cs204_08', 4)	# 23-26
    Unknown4007(0)
    sprite('cs204_09', 4)	# 27-30
    sprite('cs204_10', 4)	# 31-34
    sprite('cs204_08', 4)	# 35-38
    sprite('cs204_09', 4)	# 39-42
    sprite('cs204_10', 4)	# 43-46
    sprite('keep', 32767)	# 47-32813
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaJC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000010b6fdff7011010000000000000000000000000000000000')
        callSubroutine('PAK_AttackInit')
        AttackLevel_(5)
        AirUntechableTime(50)
        AirPushbackX(5000)
        AirPushbackY(-50000)
        GroundedHitstunAnimation(1)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        HitOverhead(2)
        Unknown9310(1)
        Unknown23078(1)
        Unknown2053(1)
        Unknown2017(0)
        Unknown4007(3)
        callSubroutine('PAK_CheckWarp')
        Unknown23059(1)

        def upon_12():
            Unknown23029(3, 2061, 0)
    sprite('cs254_00', 1)	# 1-1
    sprite('cs254_01', 1)	# 2-2
    sprite('cs254_02', 1)	# 3-3
    sprite('cs254_03', 2)	# 4-5
    Unknown4007(0)
    physicsXImpulse(15000)
    sprite('cs254_04', 2)	# 6-7
    sprite('cs254_05', 2)	# 8-9
    Unknown1019(150)
    physicsYImpulse(-10000)
    sprite('cs254_06', 2)	# 10-11
    sprite('cs254_07', 2)	# 12-13
    Unknown1019(150)
    YAccel(150)
    sprite('cs254_08', 2)	# 14-15
    Unknown1019(50)
    GFX_0('ZanzohAir5C', 100)
    sprite('cs254_09', 2)	# 16-17
    Unknown1019(50)
    YAccel(150)
    SFX_3('slash_sword_middle')
    sprite('cs254_10', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('cs254_10', 3)	# 19-21	 **attackbox here**
    sprite('cs254_11', 3)	# 22-24
    sprite('cs254_12', 3)	# 25-27
    sprite('cs254_13', 3)	# 28-30
    sprite('cs254_11', 3)	# 31-33
    sprite('cs254_12', 3)	# 34-36
    sprite('cs254_13', 3)	# 37-39
    sprite('keep', 32767)	# 40-32806
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodain():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000068000000402bfeff60ea000000000000000000000000000000000000')
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)	# 1-4
    sprite('cs432_01', 4)	# 5-8
    sprite('cs432_02', 4)	# 9-12
    sprite('cs432_00', 4)	# 13-16
    sprite('cs432_01', 4)	# 17-20
    sprite('cs432_02', 4)	# 21-24
    sprite('cs432_00', 4)	# 25-28
    sprite('cs432_01', 3)	# 29-31
    sprite('cs432_02', 3)	# 32-34
    sprite('cs432_03', 3)	# 35-37
    sprite('cs432_04', 3)	# 38-40
    sprite('cs432_05', 5)	# 41-45
    GFX_0('LightningPlasma_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)	# 46-50
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)	# 51-55
    sprite('cs432_08', 5)	# 56-60
    sprite('cs432_06', 5)	# 61-65
    sprite('cs432_07', 5)	# 66-70
    sprite('cs432_08', 5)	# 71-75
    sprite('cs432_06', 5)	# 76-80
    sprite('cs432_07', 5)	# 81-85
    sprite('cs432_08', 5)	# 86-90
    sprite('cs432_06', 5)	# 91-95
    sprite('cs432_07', 5)	# 96-100
    sprite('cs432_08', 5)	# 101-105
    sprite('cs432_06', 5)	# 106-110
    sprite('cs432_07', 5)	# 111-115
    sprite('cs432_08', 5)	# 116-120
    sprite('keep', 32767)	# 121-32887
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodainSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000068000000402bfeff60ea000000000000000000000000000000000000')
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)	# 1-4
    sprite('cs432_01', 4)	# 5-8
    sprite('cs432_02', 4)	# 9-12
    sprite('cs432_00', 4)	# 13-16
    sprite('cs432_01', 4)	# 17-20
    sprite('cs432_02', 4)	# 21-24
    sprite('cs432_00', 4)	# 25-28
    sprite('cs432_01', 3)	# 29-31
    sprite('cs432_02', 3)	# 32-34
    sprite('cs432_03', 3)	# 35-37
    sprite('cs432_04', 3)	# 38-40
    sprite('cs432_05', 5)	# 41-45
    GFX_0('LightningPlasmaCD_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)	# 46-50
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)	# 51-55
    sprite('cs432_08', 5)	# 56-60
    sprite('cs432_06', 5)	# 61-65
    sprite('cs432_07', 5)	# 66-70
    sprite('cs432_08', 5)	# 71-75
    sprite('cs432_06', 5)	# 76-80
    sprite('cs432_07', 5)	# 81-85
    sprite('cs432_08', 5)	# 86-90
    sprite('cs432_06', 5)	# 91-95
    sprite('cs432_07', 5)	# 96-100
    sprite('cs432_08', 5)	# 101-105
    sprite('cs432_06', 5)	# 106-110
    sprite('cs432_07', 5)	# 111-115
    sprite('cs432_08', 5)	# 116-120
    sprite('cs432_06', 5)	# 121-125
    sprite('cs432_07', 5)	# 126-130
    sprite('cs432_08', 5)	# 131-135
    sprite('keep', 32767)	# 136-32902
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodainDSD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000068000000402bfeff60ea000000000000000000000000000000000000')
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)	# 1-4
    sprite('cs432_01', 4)	# 5-8
    sprite('cs432_02', 4)	# 9-12
    sprite('cs432_00', 4)	# 13-16
    sprite('cs432_01', 4)	# 17-20
    sprite('cs432_02', 4)	# 21-24
    sprite('cs432_00', 4)	# 25-28
    sprite('cs432_01', 3)	# 29-31
    sprite('cs432_02', 3)	# 32-34
    sprite('cs432_03', 3)	# 35-37
    sprite('cs432_04', 3)	# 38-40
    sprite('cs432_05', 5)	# 41-45
    GFX_0('LightningPlasmaDSD_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)	# 46-50
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)	# 51-55
    sprite('cs432_08', 5)	# 56-60
    sprite('cs432_06', 5)	# 61-65
    sprite('cs432_07', 5)	# 66-70
    sprite('cs432_08', 5)	# 71-75
    sprite('cs432_06', 5)	# 76-80
    sprite('cs432_07', 5)	# 81-85
    sprite('cs432_08', 5)	# 86-90
    sprite('cs432_06', 5)	# 91-95
    sprite('cs432_07', 5)	# 96-100
    sprite('cs432_08', 5)	# 101-105
    sprite('cs432_06', 5)	# 106-110
    sprite('cs432_07', 5)	# 111-115
    sprite('cs432_08', 5)	# 116-120
    sprite('keep', 32767)	# 121-32887
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodainDSDSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000068000000402bfeff60ea000000000000000000000000000000000000')
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)	# 1-4
    sprite('cs432_01', 4)	# 5-8
    sprite('cs432_02', 4)	# 9-12
    sprite('cs432_00', 4)	# 13-16
    sprite('cs432_01', 4)	# 17-20
    sprite('cs432_02', 4)	# 21-24
    sprite('cs432_00', 4)	# 25-28
    sprite('cs432_01', 3)	# 29-31
    sprite('cs432_02', 3)	# 32-34
    sprite('cs432_03', 3)	# 35-37
    sprite('cs432_04', 3)	# 38-40
    sprite('cs432_05', 5)	# 41-45
    GFX_0('LightningPlasmaCDDSD_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)	# 46-50
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)	# 51-55
    sprite('cs432_08', 5)	# 56-60
    sprite('cs432_06', 5)	# 61-65
    sprite('cs432_07', 5)	# 66-70
    sprite('cs432_08', 5)	# 71-75
    sprite('cs432_06', 5)	# 76-80
    sprite('cs432_07', 5)	# 81-85
    sprite('cs432_08', 5)	# 86-90
    sprite('cs432_06', 5)	# 91-95
    sprite('cs432_07', 5)	# 96-100
    sprite('cs432_08', 5)	# 101-105
    sprite('cs432_06', 5)	# 106-110
    sprite('cs432_07', 5)	# 111-115
    sprite('cs432_08', 5)	# 116-120
    sprite('cs432_06', 5)	# 121-125
    sprite('cs432_07', 5)	# 126-130
    sprite('cs432_08', 5)	# 131-135
    sprite('keep', 32767)	# 136-32902
    enterState('PersonaDeleteAndIdling')

@State
def SpecialAtemiGood():

    def upon_IMMEDIATE():
        Unknown23067('akef_403_gooddaze')
        Unknown4009(2)
        Unknown4010(2)
        Unknown1096(800)
    sprite('null', 60)	# 1-60

@State
def SpecialRash00():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(40000)
        Unknown1007(180000)
        Unknown1096(1500)
        Unknown2019(100)
    sprite('vrakef_sp_rash00', 2)	# 1-2
    sprite('vrakef_sp_rash00', 4)	# 3-6
    physicsXImpulse(36000)
    physicsYImpulse(20000)
    Unknown3004(-64)

@State
def SpecialRash01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(130000)
        Unknown1007(270000)
    sprite('vrakef_sp_rash03', 2)	# 1-2
    sprite('vrakef_sp_rash03', 2)	# 3-4
    Unknown3004(-128)

@State
def SpecialRash02():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(-20000)
        Unknown1007(255000)
        Unknown1096(1500)
    sprite('vrakef_sp_rash02', 2)	# 1-2
    sprite('vrakef_sp_rash02', 4)	# 3-6
    physicsXImpulse(60000)
    Unknown3004(-64)

@State
def SpecialRash03():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(122000)
        Unknown1007(250000)
    sprite('vrakef_sp_rash03', 2)	# 1-2
    sprite('vrakef_sp_rash03', 2)	# 3-4
    Unknown3004(-128)

@State
def SpecialRash04():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(130000)
        Unknown1007(240000)
    sprite('vrakef_sp_rash04', 2)	# 1-2

@State
def SpecialRash05():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(80000)
        Unknown1007(320000)
        Unknown1099(50)
        physicsXImpulse(-5000)
        physicsYImpulse(1000)
    sprite('null', 2)	# 1-2
    sprite('vrakef_sp_rash05', 8)	# 3-10
    Unknown3004(-32)

@State
def SpecialQuakeSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_quake_smoke')
        Unknown4009(2)
    sprite('null', 70)	# 1-70

@State
def SpecialBodyBlowFirst():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f73705f626c6f775f77696e643030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown3026(-14336)
        teleportRelativeX(-80000)
        Unknown1007(150000)
        Unknown1096(1200)
    sprite('null', 4)	# 1-4
    Unknown3004(-62)

@State
def SpecialBodyBlowMain():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f73705f626c6f775f77696e643031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(80000)
        Unknown1007(100000)
        Unknown1096(1200)
        Unknown1067(-50)
        Unknown1072(-500)
        Unknown1074(-400)
    sprite('null', 2)	# 1-2
    sprite('null', 5)	# 3-7
    Unknown3004(-51)

@State
def akef_dashupper():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f3430397570706572000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown3026(-14336)
        Unknown1096(1500)
    sprite('null', 2)	# 1-2
    Unknown3001(64)
    Unknown3004(128)
    GFX_1('akef_dashupper_splash', 100)
    sprite('null', 2)	# 3-4
    sprite('null', 4)	# 5-8
    Unknown3004(-32)

@State
def SpecialScrewWind():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_0('SpecialScrewWind00', 100)
        GFX_0('SpecialScrewWind01', 100)
        GFX_0('SpecialScrewWind02', 100)
        Unknown1007(-16000)
    sprite('null', 30)	# 1-30

@State
def SpecialScrewWind00():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f73705f73637265775f77696e6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown1072(20000)
        Unknown4010(2)
        Unknown3032()
        Unknown23118(-14336)
        Unknown1096(500)
        Unknown1066(60)
        Unknown1099(6)
    sprite('null', 10)	# 1-10
    Unknown3004(-25)

@State
def SpecialScrewWind01():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f73705f73637265775f77696e6432000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown1072(20000)
        Unknown4010(2)
        Unknown3032()
        Unknown23118(-14336)
        teleportRelativeX(60000)
        Unknown1096(350)
        Unknown1066(60)
        Unknown1099(4)
        Unknown1007(-12000)
    sprite('null', 15)	# 1-15
    Unknown3004(-20)

@State
def SpecialScrewWind02():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f73705f73637265775f77696e6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown1072(20000)
        Unknown4010(2)
        Unknown3032()
        Unknown23118(-14336)
        teleportRelativeX(100000)
        Unknown1096(250)
        Unknown1058(120)
        Unknown1066(60)
        Unknown1099(2)
        Unknown1007(12000)
    sprite('null', 20)	# 1-20
    Unknown3004(-15)

@State
def SpecialScrewFistAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_404_fistaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1056(500)
        Unknown1064(1000)
        teleportRelativeX(80000)
        GFX_0('SpecialScrewShockWave', 100)
        GFX_0('SpecialScrewShockWave', 100)
        Unknown36(1)
        Unknown1098(70)
        teleportRelativeX(110000)
        Unknown35()
    sprite('null', 2)	# 1-2
    sprite('null', 10)	# 3-12
    Unknown4007(0)
    Unknown1064(1500)
    teleportRelativeX(60000)
    Unknown3004(-25)

@State
def SpecialScrewShockWave():

    def upon_IMMEDIATE():
        Unknown23067('akef_404_shockwave')
        Unknown4011(3)
    sprite('null', 20)	# 1-20

@State
def UltimateUpperSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_dash_smoke')
        Unknown4009(2)
    sprite('null', 70)	# 1-70

@State
def SpecialAirBodyAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_408_bodyaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1500)
        Unknown1072(130000)
        teleportRelativeX(150000)
        Unknown1007(80000)

        def upon_STATE_END():
            GFX_0('SpecialAirAuraEnd', 100)
    sprite('null', 120)	# 1-120

@State
def SpecialAirAuraEnd():

    def upon_IMMEDIATE():
        Unknown23067('akef_408_aura_end')
        Unknown4013(2)
        Unknown4006(2)
        Unknown4011(3)
        teleportRelativeX(-140000)
        Unknown1007(80000)
    sprite('null', 20)	# 1-20

@State
def SpecialAirFistAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_408_fistaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1300)
    sprite('null', 120)	# 1-120

@State
def SpecialDoubleUpperFirst():

    def upon_IMMEDIATE():
        Unknown23067('akef_400_1st_punch')
        Unknown4009(2)
        Unknown4010(2)
    sprite('null', 10)	# 1-10

@State
def SpecialDoubleUpperSecond():

    def upon_IMMEDIATE():
        Unknown23067('akef_400_uppersmoke')
        Unknown4010(2)
        teleportRelativeX(40000)
    sprite('null', 60)	# 1-60

@State
def SpecialDashSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_dash_smoke')
        Unknown4009(2)
    sprite('null', 70)	# 1-70

@State
def UltimateFirstStep():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_1st_step')
        Unknown4009(2)
    sprite('null', 60)	# 1-60

@State
def UltimatePunchSuccess():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_punch_ok')
        Unknown4009(2)
    sprite('null', 60)	# 1-60
    SFX_3('grip_hugs')
    ScreenShake(5000, 10000)

@State
def UltimateFirstPunch():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_1st_punch')
        Unknown4009(2)
    sprite('null', 60)	# 1-60

@State
def UltimateUpperFistAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_431_fistaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767

@State
def UltimateUpperSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_dash_smoke')
        Unknown4009(2)
    sprite('null', 70)	# 1-70

@State
def UltimateUpperWind():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f75707065725f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown3033()
        Unknown3026(-328976)
        teleportRelativeX(-120000)
        Unknown1007(120000)
        physicsXImpulse(8000)
        GFX_0('UltimateUpperWindPlus', 100)
    sprite('null', 20)	# 1-20
    sprite('null', 10)	# 21-30
    Unknown3004(-25)

@State
def UltimateUpperWindPlus():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f75707065725f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown3033()
        Unknown3026(-328976)
        Unknown3001(0)
        teleportRelativeX(120000)
        Unknown1007(200000)
        Unknown1096(600)
    sprite('null', 2)	# 1-2
    Unknown3004(125)
    sprite('null', 20)	# 3-22
    sprite('null', 25)	# 23-47
    Unknown3004(-10)

@State
def UltimateTodomeUpper():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f75707065725f6c6967687400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4010(3)
        Unknown3032()
        Unknown23015(2)
        Unknown2019(500)
        teleportRelativeX(-50000)
        Unknown1056(200)
        Unknown1065(-500)
        Unknown1072(10000)
        GFX_0('UltimateTodomeUpperPlus', 100)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(0)
            if (SLOT_48 == 4302):
                Unknown4007(3)
                sendToLabel(1)
    sprite('null', 2)	# 1-2
    Unknown1057(100)
    physicsXImpulse(5000)
    loopRest()
    sprite('null', 10)	# 3-12
    sprite('null', 15)	# 13-27
    Unknown3004(-50)
    Unknown1059(10)
    ExitState()
    label(1)
    sprite('null', 1)	# 28-28
    GFX_0('UltimateTodomeUpper', 100)
    physicsXImpulse(0)
    loopRest()
    sprite('null', 32767)	# 29-32795
    ExitState()
    label(0)
    sprite('null', 15)	# 32796-32810
    Unknown3004(-15)

@State
def UltimateTodomeUpperB():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f75707065725f6c6967687400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4010(3)
        Unknown23015(2)
        Unknown2019(500)
        Unknown3032()
        teleportRelativeX(-50000)
        Unknown1056(300)
        Unknown1065(-250)
        Unknown1072(10000)
        GFX_0('UltimateTodomeUpperPlus', 100)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(0)
            if (SLOT_48 == 4302):
                Unknown4007(3)
                sendToLabel(1)
    sprite('null', 2)	# 1-2
    Unknown1057(100)
    physicsXImpulse(5000)
    loopRest()
    sprite('null', 10)	# 3-12
    sprite('null', 15)	# 13-27
    Unknown3004(-50)
    Unknown1059(10)
    ExitState()
    label(1)
    sprite('null', 1)	# 28-28
    GFX_0('UltimateTodomeUpperB', 100)
    physicsXImpulse(0)
    loopRest()
    sprite('null', 32767)	# 29-32795
    ExitState()
    label(0)
    sprite('null', 15)	# 32796-32810
    Unknown3004(-15)

@State
def UltimateTodomeUpperPlus():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_2nd_todome')
    sprite('null', 70)	# 1-70

@State
def Zanzoh5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3001(255)
    sprite('vr_cs204_00', 2)	# 1-2
    sprite('vr_cs204_01', 16)	# 3-18
    Unknown3004(-20)

@State
def ZanzohAir5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3001(255)
    sprite('vr_cs254_00', 2)	# 1-2
    sprite('vr_cs254_01', 2)	# 3-4
    sprite('vr_cs254_02', 16)	# 5-20
    Unknown3004(-50)

@State
def LightningPlasma_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(480)
        AttackP1(80)
        AttackP2(97)
        Unknown11091(15)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        Unknown11031(5)
        SLOT_51 = 16
        if (SLOT_6 == 0):
            pass
        if (SLOT_6 == 1):
            Unknown10000(110)
            Unknown11031(6)
        if (SLOT_6 == 2):
            Unknown10000(120)
            Unknown11031(7)
        if (SLOT_6 == 3):
            Unknown10000(130)
            Unknown11031(8)
        if (SLOT_6 == 4):
            Unknown10000(140)
            Unknown11031(9)
        if (SLOT_6 == 5):
            Unknown10000(150)
            Unknown11031(10)

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
            else:
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('dmy_atk00', 1)	# 1-1
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Unknown9083()
    sprite('dmy_atk00', 1)	# 2-2
    Unknown23027()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)	# 3-12
    SLOT_6 = 0
    Unknown21015('556c74696d6174654c696768746e696e67506c61736d61000000000000000000cd10000000000000')

@State
def LightningPlasmaCD_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(410)
        AttackP1(80)
        AttackP2(98)
        Unknown11091(14)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        Unknown11031(5)
        SLOT_51 = 24
        if (SLOT_6 == 0):
            pass
        if (SLOT_6 == 1):
            Unknown10000(110)
            Unknown11031(6)
        if (SLOT_6 == 2):
            Unknown10000(120)
            Unknown11031(7)
        if (SLOT_6 == 3):
            Unknown10000(130)
            Unknown11031(8)
            Unknown11110(99)
        if (SLOT_6 == 4):
            Unknown10000(140)
            Unknown11031(9)
            Unknown11110(96)
        if (SLOT_6 == 5):
            Unknown10000(150)
            Unknown11031(10)
            Unknown11110(94)

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
            else:
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('dmy_atk00', 1)	# 1-1
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Unknown9083()
    sprite('dmy_atk00', 1)	# 2-2
    Unknown23027()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)	# 3-12
    SLOT_6 = 0
    Unknown21015('556c74696d6174654c696768746e696e67506c61736d61000000000000000000cd10000000000000')

@State
def LightningPlasmaDSD_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(125)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        SLOT_51 = 16

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
            else:
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('dmy_atk00', 1)	# 1-1
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Unknown9083()
    sprite('dmy_atk00', 1)	# 2-2
    Unknown23027()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)	# 3-12
    SLOT_6 = 0
    Unknown21015('556c74696d6174654c696768746e696e67506c61736d61000000000000000000cd10000000000000')

@State
def LightningPlasmaCDDSD_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        SLOT_51 = 24

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
            else:
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('dmy_atk00', 1)	# 1-1
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Damage(200)
        Unknown9083()
    sprite('dmy_atk00', 1)	# 2-2
    Unknown23027()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)	# 3-12
    SLOT_6 = 0
    Unknown21015('556c74696d6174654c696768746e696e67506c61736d61000000000000000000cd10000000000000')

@State
def UltimateLightningPlasma():

    def upon_IMMEDIATE():
        GFX_2('akef_432_lightning')
        Unknown4009(2)
        GFX_0('UltimateLightningPlasma00', 100)
        GFX_0('UltimateLightningPlasma01', 100)
        GFX_0('UltimateLightningPlasma02', 100)
        GFX_0('UltimateLightningPlasma03', 100)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(0)
    sprite('null', 140)	# 1-140
    label(0)
    sprite('null', 1)	# 141-141

@State
def UltimateLightningPlasma00():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f7468756e6465723030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)	# 1-2
    Unknown3001(255)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)	# 3-4
    Unknown3001(20)
    Unknown1056(1000)
    Unknown1064(-1000)
    Unknown1079()
    sprite('null', 2)	# 5-6
    Unknown3001(255)
    Unknown1056(-1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)	# 7-8
    Unknown3001(20)
    Unknown1056(-1000)
    Unknown1064(-1000)
    Unknown1079()
    loopRest()
    gotoLabel(5)

@State
def UltimateLightningPlasma01():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f7468756e6465723031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)	# 1-2
    Unknown3001(50)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)	# 3-4
    Unknown3001(255)
    Unknown1056(1000)
    Unknown1064(-1000)
    Unknown1079()
    sprite('null', 2)	# 5-6
    Unknown1056(-1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)	# 7-8
    Unknown3001(255)
    Unknown1056(-1000)
    Unknown1064(-1000)
    Unknown1079()
    loopRest()
    gotoLabel(5)

@State
def UltimateLightningPlasma02():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f7468756e6465723032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)	# 1-2
    Unknown3001(100)
    Unknown1056(1000)
    Unknown1064(1000)
    sprite('null', 2)	# 3-4
    Unknown3001(50)
    Unknown1056(1000)
    Unknown1064(-1000)
    sprite('null', 2)	# 5-6
    Unknown3001(100)
    Unknown1056(-1000)
    Unknown1064(1000)
    sprite('null', 2)	# 7-8
    Unknown3001(50)
    Unknown1056(-1000)
    Unknown1064(-1000)
    loopRest()
    gotoLabel(5)

@State
def UltimateLightningPlasma03():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f756c746d5f7468756e6465723033000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)	# 1-2
    Unknown3001(150)
    Unknown1056(1000)
    Unknown1064(1000)
    sprite('null', 2)	# 3-4
    Unknown3001(255)
    Unknown1056(1000)
    Unknown1064(-1000)
    sprite('null', 2)	# 5-6
    Unknown3001(150)
    Unknown1056(-1000)
    Unknown1064(1000)
    sprite('null', 2)	# 7-8
    Unknown3001(255)
    Unknown1056(-1000)
    Unknown1064(-1000)
    loopRest()
    gotoLabel(5)

@State
def caef_ultimate_globe2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1096(1000)
        Unknown2019(-100)
        GFX_0('caef_ultimate_globe_add2', 100)
        Unknown38(4, 1)

        def upon_STATE_END():
            Unknown13(4)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(10)
    label(0)
    sprite('vr_csef_globe00', 4)	# 1-4
    sprite('vr_csef_globe01', 4)	# 5-8
    sprite('vr_csef_globe02', 4)	# 9-12
    sprite('vr_csef_globe03', 4)	# 13-16
    sprite('vr_csef_globe04', 4)	# 17-20
    sprite('vr_csef_globe05', 4)	# 21-24
    sprite('vr_csef_globe06', 4)	# 25-28
    sprite('vr_csef_globe07', 4)	# 29-32
    sprite('vr_csef_globe08', 4)	# 33-36
    sprite('vr_csef_globe09', 4)	# 37-40
    sprite('vr_csef_globe10', 4)	# 41-44
    sprite('vr_csef_globe11', 4)	# 45-48
    gotoLabel(0)
    label(10)
    sprite('vr_csef_globe00', 2)	# 49-50
    Unknown1099(-100)
    sprite('vr_csef_globe01', 2)	# 51-52
    sprite('vr_csef_globe02', 2)	# 53-54
    sprite('vr_csef_globe03', 2)	# 55-56
    sprite('vr_csef_globe04', 2)	# 57-58

@State
def caef_ultimate_globe_add2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4010(2)
        Unknown2019(-100)
    sprite('vr_csef_globe_add', 32767)	# 1-32767

@State
def PAK_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c300000000000000000000000000000000000000000000')
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown23022(1)
        Unknown23066(1)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 4511):
                sendToLabel(0)
            if (SLOT_48 == 4512):
                sendToLabel(1)
            if (SLOT_48 == 4513):
                sendToLabel(2)
    sprite('cs450_00', 6)	# 1-6
    sprite('cs450_01', 6)	# 7-12
    sprite('cs450_02', 6)	# 13-18
    sprite('cs450_03', 6)	# 19-24
    sprite('cs450_04', 6)	# 25-30
    sprite('cs450_05', 6)	# 31-36
    sprite('cs450_06', 6)	# 37-42
    GFX_0('caef_Ichigeki_globe', 0)
    GFX_0('caef_Ichigeki_globe_col', 0)
    sprite('cs450_07', 6)	# 43-48
    sprite('cs450_08', 6)	# 49-54
    sprite('cs450_06', 6)	# 55-60
    GFX_0('450Vacuum', 0)
    sprite('cs450_07', 6)	# 61-66
    sprite('cs450_08', 6)	# 67-72
    sprite('cs450_06', 6)	# 73-78
    sprite('cs450_07', 6)	# 79-84
    sprite('cs450_08', 6)	# 85-90
    sprite('cs450_06', 6)	# 91-96
    sprite('cs450_07', 6)	# 97-102
    sprite('cs450_08', 6)	# 103-108
    sprite('cs450_07', 6)	# 109-114
    sprite('cs450_08', 6)	# 115-120
    Unknown26('caef_Ichigeki_globe_col')
    sprite('cs450_06', 6)	# 121-126
    sprite('cs450_07', 6)	# 127-132
    sprite('cs450_08', 6)	# 133-138
    sprite('cs450_06', 6)	# 139-144
    sprite('cs450_07', 6)	# 145-150
    sprite('cs450_08', 6)	# 151-156
    sprite('cs450_06', 6)	# 157-162
    sprite('cs450_07', 6)	# 163-168
    sprite('cs450_08', 6)	# 169-174
    gotoLabel(9)
    label(0)
    sprite('cs450_06', 6)	# 175-180
    Unknown23022(1)
    sprite('cs450_07', 6)	# 181-186
    sprite('cs450_08', 6)	# 187-192
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)	# 193-32959
    Unknown23022(1)
    Unknown21015('34353056616375756d0000000000000000000000000000000000000000000000b411000000000000')
    Unknown26('caef_Ichigeki_globe')
    Unknown26('caef_Ichigeki_globe_col')
    Unknown1000(2500000)
    label(2)
    sprite('cs450_09', 8)	# 32960-32967
    Unknown23022(1)
    GFX_0('caef_Ichigeki_globe', 0)
    Unknown1000(0)
    teleportRelativeY(5930000)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('cs450_10', 8)	# 32968-32975
    GFX_0('450globeyoin', 0)
    SFX_3('bomb_m')
    sprite('cs450_11', 8)	# 32976-32983
    sprite('cs450_11', 8)	# 32984-32991
    sprite('cs450_09', 8)	# 32992-32999
    sprite('cs450_10', 8)	# 33000-33007
    sprite('cs450_09', 8)	# 33008-33015
    sprite('cs450_10', 8)	# 33016-33023
    sprite('cs450_11', 8)	# 33024-33031
    sprite('cs450_09', 8)	# 33032-33039
    sprite('cs450_10', 8)	# 33040-33047
    sprite('cs450_11', 8)	# 33048-33055
    sprite('cs450_09', 8)	# 33056-33063
    sprite('cs450_10', 8)	# 33064-33071
    sprite('cs450_11', 8)	# 33072-33079
    sprite('cs450_09', 8)	# 33080-33087
    sprite('cs450_10', 8)	# 33088-33095
    sprite('cs450_11', 8)	# 33096-33103
    sprite('cs450_09', 8)	# 33104-33111
    sprite('cs450_10', 8)	# 33112-33119
    sprite('cs450_11', 8)	# 33120-33127
    sprite('cs450_09', 8)	# 33128-33135
    sprite('cs450_10', 8)	# 33136-33143
    sprite('cs450_11', 8)	# 33144-33151
    label(3)
    sprite('cs450_09', 8)	# 33152-33159
    sprite('cs450_10', 8)	# 33160-33167
    sprite('cs450_11', 8)	# 33168-33175
    sprite('cs450_09', 8)	# 33176-33183
    sprite('cs450_10', 8)	# 33184-33191
    sprite('cs450_11', 8)	# 33192-33199
    sprite('cs450_09', 8)	# 33200-33207
    sprite('cs450_10', 8)	# 33208-33215
    sprite('cs450_11', 8)	# 33216-33223
    gotoLabel(3)
    label(9)
    sprite('keep', 32767)	# 33224-65990
    enterState('PersonaDeleteAndIdling')

@State
def IchigekiCamera():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20002(0)
            Unknown20003(0)

        def upon_43():
            if (SLOT_48 == 4521):
                sendToLabel(1)
            if (SLOT_48 == 4522):
                sendToLabel(2)
            if (SLOT_48 == 4523):
                sendToLabel(3)
            if (SLOT_48 == 4524):
                sendToLabel(4)
            if (SLOT_48 == 4525):
                sendToLabel(5)
    label(1)
    sprite('null', 10)	# 1-10
    Unknown1086(3)
    teleportRelativeX(260000)
    Unknown1007(275000)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown23013(0)
    Unknown2008()

    def upon_3():
        SLOT_105 = (SLOT_105 + (-10))
    sprite('null', 5)	# 11-15
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-20))
    sprite('null', 5)	# 16-20
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-30))
    sprite('null', 5)	# 21-25
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-40))
    sprite('keep', 10)	# 26-35
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-50))
    sprite('keep', 20)	# 36-55
    clearUponHandler(3)
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    Unknown23024(3)
    sprite('keep', 32767)	# 56-32822
    Unknown20009(1000)
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000009611000000000000')
    label(2)
    sprite('keep', 20)	# 32823-32842
    Unknown1000(0)
    teleportRelativeY(1200000)
    physicsXImpulse(0)
    physicsYImpulse(-60000)
    Unknown20000(1)
    Unknown20001(1)
    Unknown26('SCEF_FadeBlack12In')
    sprite('keep', 30)	# 32843-32872
    sprite('keep', 30)	# 32873-32902
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000009711000000000000')
    label(3)
    sprite('keep', 20)	# 32903-32922
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('keep', 2)	# 32923-32924
    teleportRelativeY(1950000)
    physicsYImpulse(62500)
    sprite('keep', 18)	# 32925-32942
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown36(1)
    Unknown1096(8000)
    Unknown35()
    Unknown20009(3800)
    Unknown20000(1)
    Unknown20001(1)
    sprite('keep', 10)	# 32943-32952
    physicsYImpulse(-10000)
    sprite('keep', 60)	# 32953-33012
    physicsYImpulse(-8000)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-30))
    SFX_3('ak000')
    sprite('keep', 5)	# 33013-33017
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-150))
    physicsYImpulse(70000)
    sprite('keep', 10)	# 33018-33027
    GFX_0('IchigekiWhite', 100)
    GFX_1('csef_450flash', 100)
    sprite('keep', 32767)	# 33028-65794
    clearUponHandler(3)
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000009811000000000000')
    label(4)
    sprite('keep', 80)	# 65795-65874
    teleportRelativeY(0)
    physicsYImpulse(0)
    Unknown20009(1000)
    Unknown20007(1)
    Unknown20001(1)
    sprite('keep', 32767)	# 65875-98641
    GFX_1('csef_450flash', 100)
    label(5)
    sprite('keep', 20)	# 98642-98661
    sprite('keep', 195)	# 98662-98856
    Unknown1000(0)
    teleportRelativeY(6300000)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown20000(1)
    Unknown20001(1)
    sprite('keep', 60)	# 98857-98916
    Unknown1000(-134000)
    teleportRelativeY(6550000)
    physicsYImpulse(-900)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20009(100)

    def upon_3():
        SLOT_105 = (SLOT_105 + 9)
    sprite('keep', 80)	# 98917-98996
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + 7)
    physicsYImpulse(-700)
    sprite('keep', 80)	# 98997-99076
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + 3)
    physicsYImpulse(-300)
    sprite('keep', 30)	# 99077-99106
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000009911000000000000')
    label(6)
    sprite('keep', 20)	# 99107-99126
    clearUponHandler(3)
    Unknown20009(1000)
    Unknown1000(0)
    teleportRelativeY(0)
    GFX_0('450finishsmoke', 103)
    Unknown23024(0)
    sprite('keep', 32767)	# 99127-131893
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')

@State
def caef_Ichigeki_globe():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vr_csef_globe00', 4)	# 1-4
    sprite('vr_csef_globe01', 4)	# 5-8
    sprite('vr_csef_globe02', 4)	# 9-12
    sprite('vr_csef_globe03', 4)	# 13-16
    sprite('vr_csef_globe04', 4)	# 17-20
    sprite('vr_csef_globe05', 4)	# 21-24
    sprite('vr_csef_globe06', 4)	# 25-28
    sprite('vr_csef_globe07', 4)	# 29-32
    sprite('vr_csef_globe08', 4)	# 33-36
    sprite('vr_csef_globe09', 4)	# 37-40
    sprite('vr_csef_globe10', 4)	# 41-44
    sprite('vr_csef_globe11', 4)	# 45-48
    label(0)
    sprite('vr_csef_globe00', 4)	# 49-52
    sprite('vr_csef_globe01', 4)	# 53-56
    sprite('vr_csef_globe02', 4)	# 57-60
    sprite('vr_csef_globe03', 4)	# 61-64
    sprite('vr_csef_globe04', 4)	# 65-68
    sprite('vr_csef_globe05', 4)	# 69-72
    sprite('vr_csef_globe06', 4)	# 73-76
    sprite('vr_csef_globe07', 4)	# 77-80
    sprite('vr_csef_globe08', 4)	# 81-84
    sprite('vr_csef_globe09', 4)	# 85-88
    sprite('vr_csef_globe10', 4)	# 89-92
    sprite('vr_csef_globe11', 4)	# 93-96
    gotoLabel(0)

@State
def caef_Ichigeki_globe_col():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(10000)
        Unknown11064(1)
        AirUntechableTime(10000)
        Unknown9310(10000)
        AirPushbackX(0)
        AirPushbackY(150)
        YImpluseBeforeWallbounce(3)
        Unknown11072(1, 5000, -220000)
        GroundedHitstunAnimation(1)
        Unknown30055('000000000200000002000000')
        Unknown30056('000000000200000002000000')
        Unknown11033(3)
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(3)
        Unknown23027()

        def upon_12():
            Unknown21015('41737472616c48656174000000000000000000000000000000000000000000009511000000000000')
    sprite('dmy_atk00', 15)	# 1-15
    Unknown21003(1000, 250)
    sprite('dmy_atk00', 15)	# 16-30
    Unknown21003(4000, 1000)
    sprite('dmy_atk00', 15)	# 31-45
    Unknown21003(7000, 1750)
    SFX_3('ak003')
    sprite('dmy_atk00', 15)	# 46-60
    Unknown21003(10000, 2500)
    RefreshMultihit()
    SFX_3('ak003')
    sprite('dmy_atk00', 15)	# 61-75
    Unknown21003(11000, 2750)
    SFX_3('ak003')
    sprite('dmy_atk00', 15)	# 76-90
    Unknown21003(12000, 3000)
    SFX_3('ak003')
    sprite('dmy_atk00', 15)	# 91-105
    SFX_3('ak003')
    sprite('dmy_atk00', 15)	# 106-120
    SFX_3('ak003')
    sprite('dmy_atk00', 32767)	# 121-32887

@State
def __450Vacuum():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        GFX_2('csef_450vacuum')
        Unknown4010(2)
        Unknown3032()
        Unknown3057(1)
        Unknown3058(1000)
        Unknown1096(2500)
        Unknown1099(-20)

        def upon_43():
            if (SLOT_48 == 4532):
                sendToLabel(0)
    sprite('vr_ak_yugami', 5)	# 1-5
    Unknown1074(5000)
    Unknown3058(4000)
    sprite('vr_ak_yugami', 10)	# 6-15
    Unknown1074(10000)
    Unknown3058(8000)
    sprite('vr_ak_yugami', 15)	# 16-30
    Unknown1074(25000)
    Unknown3058(14000)
    sprite('vr_ak_yugami', 20)	# 31-50
    Unknown1074(50000)
    Unknown3058(19000)
    sprite('vr_ak_yugami', 32767)	# 51-32817
    Unknown1074(90000)
    Unknown3058(24000)
    label(0)
    sprite('vr_ak_yugami', 5)	# 32818-32822
    Unknown1074(90000)
    Unknown3058(24000)
    Unknown3004(-51)

@State
def Groundglobe():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f343530676c6f62652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeY(0)
        Unknown1000(0)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 4531):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    Unknown3004(50)
    label(0)
    sprite('null', 10)	# 32768-32777
    Unknown3004(-26)

@State
def Ichigekibeam():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('616b65665f3435306265616d2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('akef_450punch')
        Unknown2054(1)
        Unknown3032()
    sprite('null', 600)	# 1-600
    sprite('null', 20)	# 601-620
    Unknown3004(-13)

@State
def Ichigekiimpact():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('616b65665f343530686974696d706163742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3032()
    sprite('null', 30)	# 1-30
    sprite('null', 80)	# 31-110
    Unknown1099(40)
    sprite('null', 20)	# 111-130
    Unknown3004(-13)

@State
def Ichigekiimpact_bg():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown23015(1)
        GFX_2('csef_450aura')
        Unknown2054(1)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 30)	# 1-30
    sprite('null', 100)	# 31-130
    Unknown3004(6)
    sprite('null', 20)	# 131-150
    Unknown3004(-13)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown23015(2)
        Unknown6001(1)
        Unknown2007()
        Unknown1000(0)
        teleportRelativeY(200000)
        Unknown3001(0)
        Unknown3004(8)
        GFX_0('Cutinbg', 100)
        Unknown23119(16777215, 166, 1)
        GFX_0('450flasheff', 100)
    SLOT_51 = 20
    label(1)
    sprite('ichigeki', 2)	# 1-2	 **attackbox here**
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-6000, 6000)
    Unknown1011(-6000, 6000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(10, 2, 51)
    gotoLabel(1)
    label(10)
    SLOT_51 = 20
    label(11)
    sprite('ichigeki', 2)	# 3-4	 **attackbox here**
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-8000, 8000)
    Unknown1011(-8000, 8000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(20, 2, 51)
    gotoLabel(11)
    label(20)
    SLOT_51 = 30
    label(21)
    sprite('ichigeki', 1)	# 5-5	 **attackbox here**
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-14000, 14000)
    Unknown1011(-14000, 14000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(30, 2, 51)
    gotoLabel(21)
    label(30)
    SLOT_51 = 55
    label(31)
    sprite('ichigeki', 1)	# 6-6	 **attackbox here**
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-18000, 18000)
    Unknown1011(-18000, 18000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(0, 2, 51)
    gotoLabel(31)
    label(0)
    sprite('ichigeki', 1)	# 7-7	 **attackbox here**

@State
def __450flasheff():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        teleportRelativeX(550000)
        teleportRelativeY(5800000)
        Unknown1096(2500)
    sprite('null', 100)	# 1-100
    GFX_1('akef450_flash', 100)

@State
def Cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('616b65665f343530637574696e62672e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown23015(2)
        Unknown2007()
        Unknown3001(0)
        Unknown1007(850000)
    sprite('null', 40)	# 1-40
    Unknown3004(15)
    sprite('null', 115)	# 41-155
    Unknown23119(16777215, 110, 1)
    sprite('null', 45)	# 156-200
    sprite('null', 30)	# 201-230
    Unknown3004(-9)

@State
def __450burst():

    def upon_IMMEDIATE():
        Unknown1000(0)
        teleportRelativeY(6300000)
        Unknown3032()
    sprite('null', 40)	# 1-40
    sprite('null', 20)	# 41-60
    GFX_1('csef_450burst', 100)
    Unknown23119(-14216, 30, 1)
    Unknown3004(-13)

@State
def __450globeyoin():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(2)
        Unknown3032()
    sprite('null', 30)	# 1-30
    sprite('null', 50)	# 31-80
    GFX_1('csef_450globeyoin', 100)
    GFX_1('csef_450globehikari', 100)
    sprite('null', 20)	# 81-100
    Unknown3004(-13)

@State
def IchigekiWhite():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown23015(4)
        Unknown1096(5000)
        Unknown4007(2)
        Unknown3001(0)
    sprite('vr_ak450_white', 30)	# 1-30
    Unknown3004(16)
    sprite('vr_ak450_white', 25)	# 31-55
    Unknown3004(-11)

@State
def __450finishsmoke():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23067('csef_450smoke')
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 90)	# 1-90
    sprite('null', 26)	# 91-116
    Unknown3004(-10)

@State
def LifeLinkEff():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 1)	# 1-1
    Unknown4045('6e7465665f73746f72795f6c6966656c696e6b6566665f6c696e653200000000ffffffff')

@State
def PAK_PersonaMatchWin():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff20bf02006079feff20bf02006079feff20bf0200')
        callSubroutine('PersonaReset')
        callSubroutine('PAK_CheckWarp')
        Unknown23022(1)
        Unknown4007(3)
    sprite('cs610_00', 6)	# 1-6
    physicsYImpulse(-6000)
    sprite('cs610_01', 6)	# 7-12
    sprite('cs610_00', 6)	# 13-18
    sprite('cs610_01', 6)	# 19-24
    sprite('cs610_00', 6)	# 25-30
    sprite('cs610_02', 6)	# 31-36
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 15000)
    sprite('cs610_03', 6)	# 37-42
    label(9)
    sprite('cs610_04', 6)	# 43-48
    SFX_0('cloth_l')
    sprite('cs610_05', 6)	# 49-54
    sprite('cs610_06', 6)	# 55-60
    gotoLabel(9)
    sprite('keep', 32767)	# 61-32827
    enterState('PersonaDeleteAndIdling')

@State
def akef_entry_shadows():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
        teleportRelativeY(0)
    sprite('vr_ak600_00', 32767)	# 1-32767
    GFX_0('akef_entry_bag', 100)

@State
def akef_entry_shadows_clash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
    sprite('vr_ak600_00', 8)	# 1-8
    Unknown1000(-1230000)
    Unknown3004(-32)
    GFX_1('akef_entry_clash02', 0)
    GFX_1('akef_entry_clash02', 1)
    GFX_1('akef_entry_clash02', 2)
    GFX_1('akef_entry_clash02', 3)
    GFX_1('akef_entry_clash02', 4)
    GFX_1('akef_entry_clash02', 5)
    GFX_1('akef_entry_clash02', 6)
    GFX_1('akef_entry_clash02', 7)
    GFX_0('akef_entry_bag_clash', 100)

@State
def akef_entry_bag():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
        teleportRelativeX(50000)
        Unknown1007(500000)
    sprite('vr_ak600_10', 32767)	# 1-32767

@State
def akef_entry_bag_clash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
        teleportRelativeX(50000)
        Unknown1007(500000)
    sprite('vr_ak600_11', 60)	# 1-60
    physicsXImpulse(12000)
    physicsYImpulse(8000)
    Unknown3004(-8)
    Unknown1074(15000)

@State
def pak644_wind():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(30000)
    sprite('null', 1)	# 1-1
    GFX_1('pakef644_landwind', 100)

@State
def pak644_wind_3D():

    def upon_IMMEDIATE():
        pass
    sprite('null', 2)	# 1-2
    GFX_1('pakef644_knackle', 100)
    GFX_0('pak644_wind_3D_1', 100)
    sprite('null', 3)	# 3-5
    GFX_0('pak644_wind_3D_2', 100)
    sprite('null', 3)	# 6-8
    GFX_0('pak644_wind_3D_3', 100)
    sprite('null', 3)	# 9-11
    GFX_0('pak644_wind_3D_4', 100)

@State
def pak644_wind_3D_1():

    def upon_IMMEDIATE():
        Unknown4003('70616b65665f36303077696e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(2500)
        Unknown1072(-45000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)	# 1-60
    Unknown2055(9)
    Unknown1099(500)

@State
def pak644_wind_3D_2():

    def upon_IMMEDIATE():
        Unknown4003('70616b65665f36303077696e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(2500)
        Unknown1072(45000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)	# 1-60
    Unknown2055(9)
    Unknown1099(500)

@State
def pak644_wind_3D_3():

    def upon_IMMEDIATE():
        Unknown4003('70616b65665f36303077696e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(1750)
        Unknown1007(-125000)
        Unknown1072(-15000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)	# 1-60
    Unknown2055(9)
    Unknown1099(500)

@State
def pak644_wind_3D_4():

    def upon_IMMEDIATE():
        Unknown4003('70616b65665f36303077696e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(2500)
        Unknown1007(-175000)
        Unknown1072(15000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)	# 1-60
    Unknown2055(9)
    Unknown1099(500)

@State
def WinCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
    sprite('null', 32767)	# 1-32767

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