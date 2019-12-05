@State
def PAG_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)
    Unknown3038(1)
    Unknown24('5041475f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PAG_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PAG_ReceptionSignal')
    sprite('null', 32767)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PAG_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 1000):
            Unknown23185('5041475f506572736f6e6135430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 1001):
            Unknown23185('5041475f506572736f6e6135434e6f41747461636b000000000000000000000032000000')
        if (SLOT_48 == 1010):
            Unknown23185('506572736f6e6135425f326e640000000000000000000000000000000000000032000000')
        if (SLOT_48 == 1020):
            Unknown23185('5041475f506572736f6e6141697235430000000000000000000000000000000032000000')
        if (SLOT_48 == 1030):
            Unknown23185('5041475f506572736f6e6141697235440000000000000000000000000000000032000000')
        if (SLOT_48 == 1050):
            Unknown23185('5041475f5370656172000000000000000000000000000000000000000000000064000000')
        if (SLOT_48 == 1040):
            Unknown23185('5041475f506572736f6e61526f6c6c696e67000000000000000000000000000064000000')
        if (SLOT_48 == 1041):
            Unknown23185('5041475f506572736f6e61526f6c6c696e67455800000000000000000000000064000000')
        if (SLOT_48 == 1060):
            Unknown23185('5041475f506572736f6e61417468656e6153757266696e67000000000000000064000000')
        if (SLOT_48 == 1061):
            Unknown23185('5041475f506572736f6e61417468656e6153757266696e674f4400000000000064000000')
        if (SLOT_48 == 1062):
            Unknown23185('5041475f556c74696d617465537065617200000000000000000000000000000064000000')
        if (SLOT_48 == 1070):
            Unknown23185('5041475f506572736f6e6132435f54414700000000000000000000000000000064000000')
        if (SLOT_48 == 1090):
            Unknown23185('5041475f506572736f6e6135445f54414700000000000000000000000000000064000000')
        if (SLOT_48 == 1063):
            Unknown23185('5041475f506572736f6e61417468656e6153757266696e6744554f000000000064000000')
        if (SLOT_48 == 1064):
            Unknown23185('5041475f506572736f6e61417468656e6153757266696e674f4444554f00000064000000')
        if (SLOT_48 == 1065):
            Unknown23185('5041475f556c74696d617465537065617244554f00000000000000000000000064000000')
        if (SLOT_48 == 1080):
            Unknown23185('5041475f506572736f6e614963686967656b690000000000000000000000000064000000')
        if (SLOT_48 == 10):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')
        if (SLOT_48 == 9000):
            Unknown23185('506572736f6e6157696e32000000000000000000000000000000000000000000c8000000')

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
def PAG_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PAG_AttackInit():
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
    callSubroutine('PAG_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAG_SPAttackInit():
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
    callSubroutine('PAG_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAG_DDAttackInit():
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
    callSubroutine('PAG_ReceptionSignal')
    Unknown23023()

@Subroutine
def PAG_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PAG_ForceWarp():
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
    sprite('keep', 32767)
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_0('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PAG_PersonaWait')

@State
def PersonaSummonEffect():
    sprite('null', 30)
    Unknown23015(13)
    Unknown4054(11)
    Unknown4045('706572736f6e615f73756d6d6f6e00000000000000000000000000000000000064000000')

@State
def PersonaSummonEffect_PLAYER():
    sprite('null', 30)
    Unknown1007(288000)
    teleportRelativeX(112000)
    GFX_1('persona_summon_ply', 100)

@State
def PersonaDeleteEffect():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        callSubroutine('PAG_ReceptionSignal')
    sprite('null', 30)
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
def Init_CantCancelPersonaAction():
    SLOT_10 = 1

    def upon_STATE_END():
        SLOT_10 = 0

@State
def PAG_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PAG_AttackInit')
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackX(24000)
        AirPushbackY(16000)
        AirUntechableTime(30)
        Unknown9016(1)
        Unknown23078(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PAG_CheckWarp')
        Unknown23059(1)
    sprite('at204_01', 3)
    Unknown2006()
    sprite('at204_02', 2)
    sprite('at204_03', 2)
    sprite('at204_04', 2)
    RefreshMultihit()
    GFX_0('Zanzoh5C', 100)
    SFX_3('slash_pole_slow')
    sprite('at204_05', 3)
    sprite('at204_06', 3)
    DisableAttackRestOfMove()
    sprite('at204_07', 3)
    sprite('at204_08', 3)
    sprite('at204_09', 3)
    sprite('at204_07', 3)
    sprite('at204_08', 3)
    sprite('at204_09', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_Persona5CNoAttack():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PAG_AttackInit')
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackX(24000)
        AirPushbackY(16000)
        AirUntechableTime(30)
        Unknown9016(1)
        Unknown23078(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PAG_CheckWarp')
        Unknown4009(3)
        Unknown23059(1)
    sprite('at204_01', 3)
    Unknown2006()
    sprite('at204_02', 2)
    sprite('at204_03', 2)
    sprite('at204_04', 2)
    RefreshMultihit()
    GFX_0('Zanzoh5C', 100)
    SFX_3('slash_pole_slow')
    sprite('at204_05', 3)
    sprite('at204_06', 3)
    DisableAttackRestOfMove()
    sprite('at204_07', 3)
    sprite('at204_08', 3)
    sprite('at204_09', 3)
    sprite('at204_07', 3)
    sprite('at204_08', 3)
    sprite('at204_09', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def Persona5B_2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PAG_AttackInit')
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(85)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(30000)
        AirUntechableTime(40)
        Unknown23078(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown2053(1)
        callSubroutine('PAG_CheckWarp')
        Unknown23059(1)
    sprite('at205_03', 1)
    Unknown2006()
    sprite('at206_00', 1)
    sprite('at206_05', 1)
    sprite('at206_06', 1)
    sprite('at206_07', 1)
    sprite('at206_08', 4)
    GFX_0('DBarrierAtk', 0)
    RefreshMultihit()
    physicsXImpulse(60000)
    SFX_3('ag006')
    EnableCollision(0)
    sprite('at206_09', 4)
    SFX_3('airdash_m')
    sprite('at206_08', 4)
    sprite('at206_09', 4)
    Unknown1019(70)
    sprite('at206_10', 4)
    Unknown1019(70)
    Unknown26('DBarrierAtk')
    sprite('at206_11', 4)
    Unknown1019(70)
    sprite('at206_12', 4)
    Unknown1019(0)
    sprite('at206_13', 4)
    sprite('at206_14', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def DBarrierAtk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('616765665f3230365f736869656c645f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(0)
    sprite('null', 10)
    GFX_0('DBarrierAtkShock', 100)
    Unknown3004(17)
    sprite('null', 20)
    sprite('null', 10)
    Unknown3004(-26)

@State
def PAG_PersonaAir5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000b03cffff00000000000000000000000000000000')
        callSubroutine('PAG_AttackInit')
        AttackLevel_(3)
        AttackP1(80)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(20)
        AirPushbackX(10000)
        AirPushbackY(20000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown23078(1)
        Unknown4007(3)
        callSubroutine('PAG_ForceWarp')

        def upon_43():
            if (SLOT_48 == 1021):
                Unknown26('ZanzohAir5C')
                sendToLabel(0)
            if (SLOT_48 == 1022):
                Unknown26('ZanzohAir5C')
                sendToLabel(0)
    sprite('at254_00', 2)
    sprite('at254_01', 2)
    sprite('at254_03', 4)
    Unknown23054('61743235345f303200000000000000000000000000000000000000000000000002000000')
    sprite('at254_03', 2)
    DisableAttackRestOfMove()
    sprite('at254_04', 4)
    sprite('at254_05', 2)
    GFX_0('ZanzohAir5C', 100)
    sprite('at254_06', 3)
    RefreshMultihit()
    Unknown9071()
    AirPushbackY(37000)
    AirUntechableTime(28)
    Unknown9016(1)
    SFX_3('slash_pole_slow')
    sprite('at254_07', 3)
    sprite('at254_08', 3)
    DisableAttackRestOfMove()
    sprite('at254_09', 3)
    label(0)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaAir5D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000a086010050c3000050c30000a0860100a0860100')
        callSubroutine('PAG_AttackInit')
        AttackLevel_(4)
        AttackP1(80)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(12000)
        AirPushbackY(-60000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown9118(40)
        Unknown9016(1)
        HitOverhead(0)
        Unknown23078(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2053(1)
        callSubroutine('PAG_CheckWarp')
        sendToLabelUpon(2, 9)
        Unknown23059(1)
    sprite('at256_00', 2)
    physicsXImpulse(-2000)
    physicsYImpulse(40000)
    SFX_3('highjump_m')
    sprite('at256_01', 2)
    Unknown1084(1)
    sprite('at256_02', 2)
    sprite('at256_03', 2)
    SFX_3('slash_rapier_slow')
    sprite('at256_04', 3)
    physicsXImpulse(24000)
    physicsYImpulse(-40000)
    RefreshMultihit()
    sprite('at256_05', 3)
    label(0)
    sprite('at256_04', 3)
    sprite('at256_05', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 1)
    Unknown1084(1)
    ScreenShake(0, 10000)
    SFX_3('guard_hit_m')
    Unknown8003(100, 1, 1)
    sprite('at256_06', 3)
    sprite('at256_07', 3)
    sprite('at256_08', 3)
    sprite('at256_09', 3)
    sprite('at256_10', 3)
    sprite('at256_08', 3)
    sprite('at256_09', 3)
    sprite('at256_10', 3)
    label(10)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaRolling():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffffb03cffffb03cffffb03cffffb03cffffb03cffff')
        callSubroutine('PAG_SPAttackInit')
        Unknown2010()
        AttackLevel_(3)
        Damage(100)
        AttackP1(60)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(800)
        Unknown9017(1)
        AirUntechableTime(56)
        Hitstop(0)
        Unknown11044(1)
        Unknown11069('PAG_PersonaRolling')
        Unknown11108('03000000')
        Unknown11064(1)
        Unknown30048(1)
        Unknown2037(0)
        callSubroutine('PAG_ForceWarp')
        Unknown2006()

        def upon_CLEAR_OR_EXIT():
            Unknown2071('16000000983a0000e80300000a00000000000000')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
            Unknown36(22)
            EnableCollision(1)
            Unknown35()

        def upon_77():
            Unknown36(22)
            EnableCollision(0)
            Unknown35()
    sprite('at409_00', 3)
    GFX_0('AtenaFlameEX', 0)
    physicsYImpulse(25000)
    sprite('at409_01', 2)
    sprite('at409_02', 2)
    sprite('at409_03', 2)
    sprite('at409_04', 3)
    sprite('at409_05', 2)
    RefreshMultihit()
    clearUponHandler(3)
    sprite('at409_06', 2)
    Unknown1019(30)
    YAccel(30)
    sprite('at409_07', 3)
    Unknown1019(50)
    YAccel(50)
    sprite('at409_08', 6)
    Unknown1084(1)
    label(0)
    sprite('at409_09', 3)
    RefreshMultihit()
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    AirPushbackX(0)
    AirPushbackY(2500)
    YImpluseBeforeWallbounce(800)
    sprite('at409_10', 3)
    RefreshMultihit()
    sprite('at409_11', 2)
    RefreshMultihit()
    sprite('at409_11', 1)
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(0)
    else:
        sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('at409_09', 3)
    GFX_0('AtenaFlameA', 0)
    RefreshMultihit()
    AirPushbackY(10000)
    Unknown30055('000000004600000046000000')
    Unknown30056('000000003200000032000000')
    YImpluseBeforeWallbounce(1500)
    Unknown9190(1)
    Unknown9118(25)
    Unknown36(22)
    EnableCollision(1)
    Unknown35()
    clearUponHandler(77)
    sprite('at409_12', 4)
    sprite('at409_16', 3)
    sprite('at409_17', 3)
    sprite('at409_18', 3)
    RefreshMultihit()
    Damage(1000)
    AirPushbackX(10000)
    AirPushbackY(-40000)
    Unknown11069('')
    Unknown11044(0)
    Unknown11064(0)
    SLOT_10 = 0
    sprite('at409_19', 3)
    GFX_0('AtenaFlameBex', 0)
    physicsXImpulse(-16000)
    physicsYImpulse(40000)
    sprite('at409_20', 3)
    Unknown1019(15)
    YAccel(15)
    sprite('at409_21', 3)
    Unknown1019(80)
    YAccel(80)
    sprite('at409_19', 3)
    Unknown1019(80)
    YAccel(80)
    sprite('at409_20', 3)
    Unknown1019(80)
    YAccel(80)
    sprite('at409_21', 3)
    Unknown1019(60)
    YAccel(60)
    sprite('at409_19', 3)
    Unknown1019(60)
    YAccel(60)
    sprite('at409_20', 3)
    Unknown1019(0)
    YAccel(0)
    sprite('at409_21', 3)
    sprite('at409_19', 3)
    sprite('at409_20', 3)
    sprite('at409_21', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaRollingEX():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffffb03cffffb03cffffb03cffffb03cffffb03cffff')
        callSubroutine('PAG_SPAttackInit')
        Unknown2010()
        AttackLevel_(4)
        Damage(200)
        AttackP1(60)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(800)
        Unknown9017(1)
        AirUntechableTime(56)
        Hitstop(0)
        Unknown11044(1)
        Unknown11069('PAG_PersonaRollingEX')
        Unknown11108('03000000')
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown11064(1)
        Unknown30048(1)
        Unknown2037(1)
        callSubroutine('PAG_ForceWarp')
        Unknown2006()

        def upon_CLEAR_OR_EXIT():
            Unknown2071('16000000983a0000e80300000a00000000000000')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
            Unknown36(22)
            EnableCollision(1)
            Unknown35()

        def upon_77():
            Unknown36(22)
            EnableCollision(0)
            Unknown35()
    sprite('at409_00', 3)
    GFX_0('AtenaFlameEX', 0)
    physicsYImpulse(25000)
    sprite('at409_01', 2)
    sprite('at409_02', 2)
    sprite('at409_03', 2)
    sprite('at409_04', 3)
    sprite('at409_05', 2)
    RefreshMultihit()
    clearUponHandler(3)
    sprite('at409_06', 2)
    Unknown1019(30)
    YAccel(30)
    sprite('at409_07', 3)
    Unknown1019(50)
    YAccel(50)
    sprite('at409_08', 6)
    Unknown1084(1)
    label(0)
    sprite('at409_09', 3)
    RefreshMultihit()
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    AirPushbackX(0)
    AirPushbackY(2500)
    YImpluseBeforeWallbounce(800)
    sprite('at409_10', 3)
    RefreshMultihit()
    sprite('at409_11', 2)
    RefreshMultihit()
    sprite('at409_11', 1)
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(0)
    else:
        sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('at409_09', 3)
    GFX_0('AtenaFlameA', 0)
    RefreshMultihit()
    AirPushbackY(10000)
    Unknown30055('000000004600000046000000')
    Unknown30056('000000003200000032000000')
    YImpluseBeforeWallbounce(1500)
    Unknown9190(1)
    Unknown9118(20)
    Unknown36(22)
    EnableCollision(1)
    Unknown35()
    clearUponHandler(77)
    sprite('at409_12', 4)
    sprite('at409_13', 3)
    sprite('at409_14', 3)
    sprite('at409_15', 3)
    sprite('at409_16', 3)
    sprite('at409_17', 3)
    sprite('at409_18', 3)
    RefreshMultihit()
    Damage(2000)
    AirPushbackX(10000)
    AirPushbackY(-40000)
    Unknown11069('')
    Unknown11044(0)
    Unknown11064(0)
    SLOT_10 = 0
    sprite('at409_19', 3)
    GFX_0('AtenaFlameBex', 0)
    physicsXImpulse(-16000)
    physicsYImpulse(40000)
    sprite('at409_20', 3)
    Unknown1019(15)
    YAccel(15)
    sprite('at409_21', 3)
    Unknown1019(80)
    YAccel(80)
    sprite('at409_19', 3)
    Unknown1019(80)
    YAccel(80)
    sprite('at409_20', 3)
    Unknown1019(80)
    YAccel(80)
    sprite('at409_21', 3)
    Unknown1019(60)
    YAccel(60)
    sprite('at409_19', 3)
    Unknown1019(60)
    YAccel(60)
    sprite('at409_20', 3)
    Unknown1019(0)
    YAccel(0)
    sprite('at409_21', 3)
    sprite('at409_19', 3)
    sprite('at409_20', 3)
    sprite('at409_21', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaAthenaSurfing():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown4009(3)
        callSubroutine('PAG_DDAttackInit')
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(5200)
        MinimumDamagePct(32)
        AttackP1(80)
        AttackP2(60)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(30000)
        AirPushbackY(38000)
        AirUntechableTime(200)
        Hitstop(17)
        Unknown11084(1)
        if SLOT_51:
            Damage(2000)
            MinimumDamagePct(100)
            AttackP1(100)
            AttackP2(100)
        setInvincible(1)
        GuardPoint_(0)
        callSubroutine('PAG_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown30041('')

        def upon_77():
            Unknown23029(3, 5010, 0)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
    sprite('at430_02', 2)
    Unknown2053(0)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    GFX_0('BarrierEnagy', 0)
    GFX_0('BarrierEyeFire', 1)
    sprite('at430_03', 2)
    sprite('at430_04', 2)
    sprite('at430_05', 4)
    sprite('at430_06', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_10', 4)
    GFX_0('eyeHikari', 0)
    GFX_0('eyeHikari', 1)
    sprite('at430_11', 4)
    GFX_0('BarrierDashEyeFire', 0)
    GFX_0('SurfingBarrierAtk', 1)
    RefreshMultihit()
    physicsXImpulse(5000)
    Unknown1028(4500)
    sprite('at430_12', 4)
    GuardPoint_(1)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    setInvincible(0)
    Unknown2003(1)
    Unknown23022(1)
    sprite('at430_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_13', 4)
    sprite('at206_14', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaAthenaSurfingOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown4009(3)
        callSubroutine('PAG_DDAttackInit')
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(4800)
        MinimumDamagePct(23)
        AttackP1(80)
        AttackP2(60)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(30000)
        AirPushbackY(38000)
        AirUntechableTime(200)
        Hitstop(17)
        Unknown11084(1)
        Unknown11072(1, 400000, 50000)
        Unknown11064(1)
        if SLOT_51:
            Damage(2000)
            MinimumDamagePct(100)
            AttackP1(100)
            AttackP2(100)
        setInvincible(1)
        GuardPoint_(0)
        callSubroutine('PAG_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown30041('')

        def upon_80():
            Unknown23029(3, 5010, 0)

        def upon_78():
            Unknown23029(3, 5011, 0)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
    sprite('at430_02', 2)
    Unknown2053(0)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    GFX_0('BarrierEnagy', 0)
    GFX_0('BarrierEyeFire', 1)
    sprite('at430_03', 2)
    sprite('at430_04', 2)
    sprite('at430_05', 4)
    sprite('at430_06', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_10', 4)
    GFX_0('eyeHikari', 0)
    GFX_0('eyeHikari', 1)
    sprite('at430_11', 4)
    GFX_0('BarrierDashEyeFire', 0)
    GFX_0('SurfingBarrierAtk', 1)
    RefreshMultihit()
    physicsXImpulse(5000)
    Unknown1028(4500)
    sprite('at430_12', 4)
    GuardPoint_(1)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    setInvincible(0)
    Unknown2003(1)
    Unknown23022(1)
    sprite('at430_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_13', 4)
    sprite('at206_14', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_UltimateSpear():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PAG_DDAttackInit')
        Unknown2054(1)
        Unknown4009(3)
        Unknown23022(1)
        callSubroutine('Init_CantCancelPersonaAction')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 1

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                Unknown2038(1)
                Unknown51(1)
            if (SLOT_2 > 14):
                clearUponHandler(3)
                Unknown51(0)
            if (SLOT_25 <= 300000):
                Unknown1084(1)
        loopRelated(17, 120)

        def upon_17():
            clearUponHandler(3)
            clearUponHandler(17)
            Unknown51(0)
        Unknown23059(1)
    sprite('at206_12', 2)
    physicsXImpulse(50000)
    sprite('at206_13', 3)
    Unknown1019(50)
    sprite('at206_14', 3)
    Unknown1019(50)
    sprite('at431_00', 3)
    GFX_0('throwEnagytame', 0)
    Unknown1019(50)
    sprite('at431_01', 4)
    Unknown1084(1)
    sprite('at431_02', 4)
    sprite('at431_00', 4)
    sprite('at431_01', 4)
    sprite('at431_02', 4)
    sprite('at431_00', 4)
    sprite('at431_01', 4)
    sprite('at431_02', 4)
    sprite('at431_00', 4)
    sprite('at431_01', 4)
    sprite('at431_02', 2)
    SFX_3('slash_blade_middle')
    sprite('at431_03', 2)
    Unknown26('throwEnagytame')
    sprite('at431_04', 2)
    sprite('at431_05', 2)
    sprite('at431_06ex01', 4)
    GFX_0('throwGroundShock', 1)
    GFX_0('AddSpear', 100)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    setInvincible(0)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaAthenaSurfingDUO():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown4009(3)
        callSubroutine('PAG_DDAttackInit')
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2000)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(30000)
        AirPushbackY(38000)
        AirUntechableTime(200)
        Hitstop(17)
        Unknown11084(1)
        setInvincible(1)
        GuardPoint_(0)
        callSubroutine('PAG_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown30041('')

        def upon_77():
            Unknown23029(3, 5010, 0)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
    sprite('at430_02', 2)
    Unknown2053(0)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    GFX_0('BarrierEnagy', 0)
    GFX_0('BarrierEyeFire', 1)
    sprite('at430_03', 2)
    sprite('at430_04', 2)
    sprite('at430_05', 4)
    sprite('at430_06', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_10', 4)
    GFX_0('eyeHikari', 0)
    GFX_0('eyeHikari', 1)
    sprite('at430_11', 4)
    GFX_0('BarrierDashEyeFire', 0)
    GFX_0('SurfingBarrierAtk', 1)
    RefreshMultihit()
    physicsXImpulse(5000)
    Unknown1028(4500)
    sprite('at430_12', 4)
    GuardPoint_(1)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    setInvincible(0)
    Unknown2003(1)
    Unknown23022(1)
    sprite('at430_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_13', 4)
    sprite('at206_14', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaAthenaSurfingODDUO():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown4009(3)
        callSubroutine('PAG_DDAttackInit')
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2000)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(30000)
        AirPushbackY(38000)
        AirUntechableTime(200)
        Hitstop(17)
        Unknown11084(1)
        Unknown11072(1, 400000, 50000)
        Unknown11064(1)
        setInvincible(1)
        GuardPoint_(0)
        callSubroutine('PAG_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown30041('')

        def upon_80():
            Unknown23029(3, 5010, 0)

        def upon_78():
            Unknown23029(3, 5011, 0)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
    sprite('at430_02', 2)
    Unknown2053(0)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    sprite('at430_00', 2)
    sprite('at430_01', 2)
    sprite('at430_02', 2)
    GFX_0('BarrierEnagy', 0)
    GFX_0('BarrierEyeFire', 1)
    sprite('at430_03', 2)
    sprite('at430_04', 2)
    sprite('at430_05', 4)
    sprite('at430_06', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_07', 4)
    sprite('at430_08', 4)
    sprite('at430_09', 4)
    sprite('at430_10', 4)
    GFX_0('eyeHikari', 0)
    GFX_0('eyeHikari', 1)
    sprite('at430_11', 4)
    GFX_0('BarrierDashEyeFire', 0)
    GFX_0('SurfingBarrierAtk', 1)
    RefreshMultihit()
    physicsXImpulse(5000)
    Unknown1028(4500)
    sprite('at430_12', 4)
    GuardPoint_(1)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    sprite('at430_12', 4)
    sprite('at430_11', 4)
    setInvincible(0)
    Unknown2003(1)
    Unknown23022(1)
    sprite('at430_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_11', 4)
    sprite('at206_12', 4)
    sprite('at206_13', 4)
    sprite('at206_14', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_UltimateSpearDUO():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PAG_DDAttackInit')
        Unknown2054(1)
        Unknown4009(3)
        Unknown23022(1)
        callSubroutine('Init_CantCancelPersonaAction')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 1

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                Unknown2038(1)
                Unknown51(1)
            if (SLOT_2 > 14):
                clearUponHandler(3)
                Unknown51(0)
            if (SLOT_25 <= 300000):
                Unknown1084(1)
        loopRelated(17, 120)

        def upon_17():
            clearUponHandler(3)
            clearUponHandler(17)
            Unknown51(0)
    sprite('at206_12', 2)
    physicsXImpulse(50000)
    sprite('at206_13', 3)
    Unknown1019(50)
    sprite('at206_14', 3)
    Unknown1019(50)
    sprite('at431_00', 3)
    GFX_0('throwEnagytame', 0)
    Unknown1019(50)
    sprite('at431_01', 4)
    Unknown1084(1)
    sprite('at431_02', 4)
    sprite('at431_00', 4)
    sprite('at431_01', 4)
    sprite('at431_02', 4)
    sprite('at431_00', 4)
    sprite('at431_01', 4)
    sprite('at431_02', 4)
    sprite('at431_00', 4)
    sprite('at431_01', 4)
    sprite('at431_02', 2)
    SFX_3('slash_blade_middle')
    sprite('at431_03', 2)
    Unknown26('throwEnagytame')
    sprite('at431_04', 2)
    sprite('at431_05', 2)
    sprite('at431_06ex01', 4)
    GFX_0('throwGroundShock', 1)
    GFX_0('AddSpearDUO', 100)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    setInvincible(0)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_Spear():

    def upon_IMMEDIATE():
        Unknown23184('030000006400000050c300000000000050c3000050c300000000000000000000')
        callSubroutine('PAG_SPAttackInit')
        Unknown2054(1)
        Unknown4009(3)
        Unknown4007(3)
        setInvincible(1)
        callSubroutine('PAG_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
    sprite('at431_00', 4)
    SFX_3('slash_blade_middle')
    sprite('at431_03', 2)
    sprite('at431_04', 2)
    sprite('at431_05', 2)
    sprite('at431_06ex01', 4)
    GFX_0('Spear_Reversal', 100)
    Unknown4007(0)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    setInvincible(0)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('at431_07', 4)
    sprite('at431_08', 4)
    sprite('at431_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_Persona2C_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PAG_SPAttackInit')
        AttackLevel_(5)
        AttackP1(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11042(1)
        Unknown23078(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown2053(1)
        callSubroutine('PAG_CheckWarp')
        Unknown23059(1)
    sprite('at254_04', 2)
    physicsXImpulse(40000)
    sprite('at254_05', 2)
    Unknown4007(0)
    GFX_0('Zanzoh2C', 100)
    Unknown1019(50)
    sprite('at254_06ex', 3)
    RefreshMultihit()
    SFX_3('slash_pole_slow')
    Unknown1019(50)
    sprite('at254_07', 3)
    Unknown1019(50)
    sprite('at254_08', 3)
    Unknown1019(0)
    DisableAttackRestOfMove()
    sprite('at254_09', 3)
    sprite('at254_07', 3)
    sprite('at254_08', 3)
    sprite('at254_09', 3)
    sprite('at254_07', 3)
    sprite('at254_08', 3)
    sprite('at254_09', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_Persona5D_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PAG_SPAttackInit')
        AttackLevel_(4)
        Damage(2000)
        Unknown11032('ffffffffffffffffe0930400ffffffff')
        AttackP1(70)
        AirUntechableTime(60)
        AirPushbackX(10000)
        AirPushbackY(35000)
        PushbackX(60000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11042(1)
        callSubroutine('PAG_CheckWarp')

        def upon_STATE_END():
            Unknown26('DBarrierAtk')
            Unknown26('DBarrierAtkShock')
    sprite('at206_05', 3)
    sprite('at206_06', 3)
    sprite('at206_07', 3)
    sprite('at206_08', 2)
    GFX_0('DBarrierAtk', 0)
    DisableAttackRestOfMove()
    physicsXImpulse(60000)
    SFX_3('ag006')
    sprite('at206_08', 1)
    RefreshMultihit()
    sprite('at206_09', 3)
    SFX_3('airdash_m')
    physicsXImpulse(0)
    Unknown4007(3)
    sprite('at206_08', 3)
    sprite('at206_09', 3)
    sprite('at206_10', 5)
    Unknown1019(40)
    EnableCollision(0)
    Unknown26('DBarrierAtk')
    Unknown26('DBarrierAtkShock')
    sprite('at206_11', 5)
    Unknown1019(40)
    Unknown4007(0)
    sprite('at206_12', 3)
    Unknown1019(40)
    sprite('at206_13', 3)
    Unknown1019(40)
    sprite('at206_14', 3)
    Unknown1019(40)
    sprite('at206_12', 3)
    Unknown1019(40)
    sprite('at206_13', 3)
    Unknown1019(40)
    sprite('at206_14', 3)
    Unknown1019(0)
    sprite('at206_12', 3)
    sprite('at206_13', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAG_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PAG_DDAttackInit')
        callSubroutine('PAG_ForceWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('at450_00', 3)
    Unknown2036(44, -1, 0)
    sprite('at450_01', 3)
    sprite('at450_02', 3)
    sprite('at450_00', 3)
    sprite('at450_01', 3)
    sprite('at450_02', 3)
    sprite('at450_00', 3)
    sprite('at450_01', 3)
    sprite('at450_02', 3)
    sprite('at450_03', 2)
    sprite('at450_04', 2)
    sprite('at450_05', 2)
    sprite('at450_06', 2)
    SFX_3('slash_blade_middle')
    sprite('at450_07', 2)
    sprite('at450_08', 2)
    sprite('at450_09', 2)
    GFX_0('IchigekiSpear', 0)
    Unknown38(5, 1)
    sprite('at450_10', 3)
    sprite('at450_11', 3)
    sprite('at450_12', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def Zanzoh2C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
    sprite('vr_at254_00', 3)
    sprite('vr_at254_01', 27)
    Unknown3004(-30)

@State
def Zanzoh5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3004(-120)
    sprite('vr_at204_00', 2)

@State
def agef202_argia_burner_jump():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-65000)
    Unknown1096(1450)

@State
def agef202_argia_burner_jump_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-65000)
    Unknown1096(1450)

@State
def agef202_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-80000)
    Unknown1064(600)

@State
def agef202_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-105000)
    Unknown1064(600)

@State
def agef202_burner_jump():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-65000)

@State
def agef202_burner_jump_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-65000)

@State
def agef202_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-80000)
    Unknown1064(600)

@State
def agef202_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-105000)
    Unknown1064(600)

@State
def agef208_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1096(800)
    Unknown1072(240000)

@State
def agef208_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1096(750)
    Unknown1072(235000)

@State
def agef208_orgia_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(240000)
    Unknown1064(1250)

@State
def agef208_orgia_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(0)
    Unknown1096(1050)

@State
def DrillAirB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('agef_drill_04')
        Unknown4003('616765665f3235315f6472696c6c5f3030000000000000000000000000000000616765665f3235315f6472696c6c5f30305f3030302e6d6d6f74000000000000')
        Unknown4015()
    sprite('null', 6)
    sprite('null', 15)
    Unknown3004(-26)

@State
def ZanzohAir5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
    sprite('vr_at254_00', 2)
    sprite('vr_at254_01', 16)
    Unknown3004(-26)

@State
def hibana2AB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('616765665f3231315f617369686962616e615f30302e44494700000000000000616765665f3231315f617369686962616e615f30305f3030302e6d6d6f740000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 18)
    Unknown3004(51)
    GFX_1('agef_kickhibana_00', 100)
    GFX_0('hibana2ABa', 100)

@State
def hibana2ABa():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('hibana2ABb', 100)
    sprite('null', 2)
    GFX_0('hibana2ABb', 100)
    sprite('null', 1)
    GFX_0('hibana2ABb', 100)
    sprite('null', 8)
    GFX_0('hibana2ABc', 100)

@State
def hibana2ABb():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4003('616765665f3231315f617369686962616e615f30312e44494700000000000000616765665f3231315f617369686962616e615f30315f3030302e6d6d6f740000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 18)
    Unknown3004(51)

@State
def hibana2ABc():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(3)
        Unknown4003('616765665f3231315f617369686962616e615f30322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(60000)
    sprite('null', 15)
    Unknown3004(-17)

@State
def Throw_bom():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(2000)
        AttackP1(100)
        AttackP2(50)
        MinimumDamagePct(100)
        AirUntechableTime(60)
        AirPushbackX(3500)
        AirPushbackY(40000)
        Unknown9017(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11044(1)
        Unknown23078(1)
        Unknown30048(1)

        def upon_78():
            Unknown23029(3, 3000, 0)
        Unknown4007(22)
        Unknown3032()
        Unknown4061(0)
        Unknown1007(200000)
        teleportRelativeX(-42300)
    sprite('throw_bom', 40)
    GFX_0('Throw_bom_blink', 100)
    StartMultihit()
    sprite('throw_bom', 1)
    RefreshMultihit()
    GFX_1('agef_throwbom_07', 100)
    ScreenShake(0, 10000)

@State
def Throw_bom_blink():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(2)
        GFX_2('agef_throw_bom')
    sprite('null', 20)
    label(0)
    sprite('vr_ag311_00', 1)
    Unknown3001(63)
    sprite('vr_ag311_00', 1)
    Unknown3001(127)
    sprite('vr_ag311_00', 1)
    Unknown3001(191)
    sprite('vr_ag311_00', 1)
    Unknown3001(255)
    sprite('vr_ag311_00', 1)
    Unknown3001(191)
    sprite('vr_ag311_00', 1)
    Unknown3001(127)
    sprite('vr_ag311_00', 1)
    Unknown3001(63)
    sprite('vr_ag311_00', 1)
    Unknown3001(0)
    gotoLabel(0)

@State
def dmy_r_action():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        HitAirUnblockable(3)
        Damage(2500)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(33000)
        AirPushbackX(29000)
        Unknown9017(1)
        AirUntechableTime(29)
        Unknown23078(1)
        Unknown2019(1000)
        Unknown4061(2)
        Unknown3032()
        Unknown3001(0)
    sprite('dmy_r_action', 4)
    RefreshMultihit()

@State
def ReversalNigiyakasi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('626365663430305f736c6173682e444947000000000000000000000000000000626365663430305f736c6173685f303030302e6d6d6f74000000000000000000')
        Unknown4015()
    sprite('null', 23)

@State
def shotgunHikari():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('616765665f3430305f73747265616d5f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('agef_shotgun_09')
        Unknown4015()
    sprite('null', 15)
    GFX_1('agef_shotgun_08', 100)

@State
def agef_orgia_shotgun():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(180000)
    Unknown1096(500)

@State
def agef_orgia_shotgun_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(215000)
    Unknown1096(450)

@State
def agef_orgia_shotgun_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-70000)
    Unknown1096(500)

@State
def agef_orgia_shotgun_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-135000)
    Unknown1096(500)

@State
def tyudanIwa():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('616765665f3235345f73746f6e655f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        teleportRelativeX(200000)
        Unknown1007(-100000)
    sprite('null', 15)
    GFX_1('agef_piresmoke_01', 100)
    GFX_0('tyudanIwaA', 100)
    sprite('null', 15)
    Unknown3004(-26)

@State
def tyudanIwaA():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('616765665f3235345f73746f6e655f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 7)
    sprite('null', 5)
    Unknown3004(-51)

@State
def agef_orgia():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-75000)
    Unknown1096(1500)

@State
def agef_orgia_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-105000)
    Unknown1096(1500)

@State
def agef_orgia_head():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_head')

@State
def agef_orgia_head_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_head_back')
    Unknown1072(180000)

@State
def agef_orgia_on():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 1)
    Unknown23067('agef_orgia_on')
    Unknown1072(-70000)
    Unknown1096(425)
    sprite('null', 8)
    Unknown1099(50)
    sprite('null', 12)
    Unknown1099(0)
    sprite('null', 16)
    Unknown1099(-50)

@State
def agef_orgia_on_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 60)
    Unknown23067('agef_orgia_on_add')

@State
def agef_orgia_on_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 1)
    Unknown23067('agef_orgia_on_back')
    Unknown1072(-125000)
    Unknown1096(350)
    sprite('null', 8)
    Unknown1099(50)
    sprite('null', 12)
    Unknown1099(0)
    sprite('null', 16)
    Unknown1099(-50)

@State
def agef_orgia_on_back_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 60)
    Unknown23067('agef_orgia_on_back_add')

@State
def agef_orgia_on_walk():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 15)
    Unknown23067('agef_orgia_on_walk')

@State
def agef_orgia_on_walk_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 15)
    Unknown23067('agef_orgia_on_walk_back')

@State
def agef_orgia_on_crouch():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 60)
    Unknown23067('agef_orgia_on')
    Unknown1072(-200000)
    Unknown1064(250)
    Unknown1056(1000)

@State
def agef_orgia_on_crouch_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 60)
    Unknown23067('agef_orgia_on_crouch_add')

@State
def agef_orgia_on_crouch_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 60)
    Unknown23067('agef_orgia_on_back')
    Unknown1072(-30000)
    Unknown1064(250)
    Unknown1056(1000)

@State
def agef_orgia_on_crouch_back_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 60)
    Unknown23067('agef_orgia_on_crouch_back_add')

@State
def agef_orgia_dash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1096(1400)

@State
def agef_orgia_dash_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1096(1250)

@State
def agef_orgia_dash_back2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1096(1300)

@State
def agef_orgia_dash_up():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-25000)
    Unknown1096(1400)

@State
def agef_orgia_dash_up_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-35000)
    Unknown1096(1250)

@State
def agef_orgia_dash_up_back2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-30000)
    Unknown1096(1300)

@State
def agef_orgia_dash_down():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(25000)
    Unknown1096(1400)

@State
def agef_orgia_dash_down_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(35000)
    Unknown1096(1250)

@State
def agef_orgia_dash_down_back2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(30000)
    Unknown1096(1300)

@State
def agef_orgia_backdash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-115000)
    Unknown1096(1300)

@State
def agef_orgia_backdash_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-130000)
    Unknown1096(1300)

@State
def agef202_argia_burner_jump():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-65000)
    Unknown1096(1450)

@State
def agef202_argia_burner_jump_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-65000)
    Unknown1096(1450)

@State
def agef_orgia_hovering():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-70000)
    Unknown1096(1200)

@State
def agef_orgia_hovering_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-135000)
    Unknown1096(1125)

@State
def agef_orgia_hovering_back2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-50000)
    Unknown1096(1100)

@State
def agef202_orgia_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-80000)
    Unknown1064(800)

@State
def agef202_orgia_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-105000)
    Unknown1064(800)

@State
def agef207_orgia_burner_turn():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-135000)
    Unknown1064(1000)

@State
def agef207_orgia_burner_turn_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-140000)
    Unknown1096(875)

@State
def agef207_orgia_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(280000)
    Unknown1064(750)

@State
def agef207_orgia_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(240000)
    Unknown1096(680)

@State
def agef_backstep():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(225000)
    Unknown1096(750)

@State
def agef_backstep_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(210000)
    Unknown1096(650)

@State
def agef_backstep_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_backstep_flare')
    Unknown1072(60000)
    Unknown1096(1100)

@State
def agef_backstep_back_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_backstep_back_flare')
    Unknown1072(30000)
    Unknown1096(1050)

@State
def agef_doublejump():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-90000)

@State
def agef_doublejump_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-90000)

@State
def agef_doublejump_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_flare')
    Unknown1072(-90000)
    Unknown1096(1125)

@State
def agef_doublejump_back_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back_flare')
    Unknown1072(-90000)
    Unknown1096(1100)

@State
def agef_airdush():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1096(937)

@State
def agef_airdush_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1096(937)

@State
def agef_airdush_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_flare')
    Unknown1096(1250)

@State
def agef_airdush_back_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back_flare')
    Unknown1096(1200)

@State
def agef_airbackdush():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(220000)
    Unknown1096(875)

@State
def agef_airbackdush_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(205000)
    Unknown1096(675)

@State
def agef202_burner_jump_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-65000)

@State
def agef202_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-80000)
    Unknown1064(600)

@State
def agef202_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-105000)
    Unknown1064(600)

@State
def agef207_burner_turn():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-135000)
    Unknown1064(1000)

@State
def agef207_burner_turn_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-140000)
    Unknown1096(875)

@State
def agef207_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-80000)
    Unknown1064(600)

@State
def agef207_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-120000)
    Unknown1064(600)

@State
def agef432_orgia_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)

        def upon_32():
            Unknown1064(1500)

        def upon_33():
            Unknown1072(265000)
            Unknown1064(1500)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(0)
    Unknown1064(1250)

@State
def agef432_orgia_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)

        def upon_32():
            Unknown1064(1500)

        def upon_33():
            Unknown1072(240000)
            Unknown1064(1250)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(0)
    Unknown1096(1250)

@State
def agef432_orgia_burner_3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)

        def upon_32():
            Unknown1064(1800)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(0)
    Unknown1064(1400)

@State
def DBarrierAtk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('616765665f3230365f736869656c645f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(0)
    sprite('null', 10)
    GFX_0('DBarrierAtkShock', 100)
    Unknown3004(17)
    sprite('null', 20)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DBarrierAtkShock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('616765665f3230365f736869656c6473686f636b5f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4011(2)
    sprite('null', 13)
    physicsXImpulse(-8000)

@State
def DBarrierJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('atef_tateaura_00')
        Unknown4003('616765665f3230365f736869656c645f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4011(2)
        Unknown3001(0)
        Unknown1072(-15000)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    Unknown3004(26)
    GFX_0('DBarrierYugamiLoop', 100)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DBarrierYugamiLoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown2019(500)
        Unknown3001(255)
        Unknown1072(-15000)
    label(1)
    sprite('null', 15)
    GFX_0('DBarrierYugami', 100)
    sprite('null', 15)
    GFX_0('DBarrierYugami', 100)
    gotoLabel(1)

@State
def DBarrierYugami():
    sprite('vr_ag_yugami_00', 1)
    Unknown4007(2)
    Unknown4010(2)
    Unknown3032()
    Unknown3057(1)
    Unknown3058(30000)
    Unknown2019(500)
    Unknown1056(200)
    Unknown1056(200)
    sprite('vr_ag_yugami_00', 20)
    Unknown1072(-15000)
    Unknown1059(150)
    Unknown1067(250)
    physicsXImpulse(-7000)
    Unknown3004(-13)
    loopRest()

@State
def __5B_Matome():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2055(200)
    sprite('dmy5AA_ExPoint', 2)
    GFX_0('5B_Shot', 4)
    Unknown23029(1, 2014, 0)
    SFX_3('ag002')
    sprite('dmy5AA_ExPoint', 2)
    GFX_0('5B_Shot', 5)
    Unknown23029(1, 2015, 0)
    SFX_3('ag002')
    sprite('dmy5AA_ExPoint', 2)
    GFX_0('5B_Shot', 6)
    Unknown23029(1, 2016, 0)
    SFX_3('ag002')
    sprite('dmy5AA_ExPoint', 2)
    GFX_0('5B_Shot', 7)
    Unknown23029(1, 2017, 0)
    SFX_3('ag002')
    sprite('dmy5AA_ExPoint', 2)
    GFX_0('5B_Shot', 8)
    Unknown23029(1, 2018, 0)
    SFX_3('ag002')
    sprite('null', 200)
    Unknown4010(0)

@State
def __5B_Shot():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(2)
        Damage(750)
        AttackP1(60)
        AttackP2(100)
        Unknown11092(1)
        AirUntechableTime(20)
        AirPushbackX(3000)
        Unknown11057(700)
        Hitstop(6)
        MinimumDamagePct(0)
        Unknown23182(2)

        def upon_LANDING():
            Unknown13(25)
        Unknown3029(1)
        physicsXImpulse(10000)
        Unknown4061(2)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 2010):
                Unknown1072(29000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2011):
                Unknown1072(21000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2012):
                Unknown1072(13000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2013):
                Unknown1072(5000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2014):
                Unknown1072(-3000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2015):
                Unknown1072(-11000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2016):
                Unknown1072(-19000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2017):
                Unknown1072(-27000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2018):
                Unknown1072(-35000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2019):
                Unknown1072(-43000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown13(25)
            Unknown23029(3, 2019, 0)

        def upon_44():
            Unknown13(25)

        def upon_LANDING():
            GFX_1('agef_handgunshock_04', 100)
            Unknown13(25)
        Unknown23067('agef_gunspeed_00')
    sprite('dmy_machinegun', 60)
    RefreshMultihit()

@State
def __2B_Matome():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2055(200)
    sprite('dmy2B_ExPoint', 2)
    GFX_0('2B_Shot', 3)
    Unknown23029(1, 2313, 0)
    SFX_3('ag002')
    sprite('dmy2B_ExPoint', 2)
    GFX_0('2B_Shot', 4)
    Unknown23029(1, 2314, 0)
    SFX_3('ag002')
    sprite('dmy2B_ExPoint', 2)
    GFX_0('2B_Shot', 5)
    Unknown23029(1, 2315, 0)
    SFX_3('ag002')
    sprite('dmy2B_ExPoint', 2)
    GFX_0('2B_Shot', 6)
    Unknown23029(1, 2316, 0)
    SFX_3('ag002')
    sprite('dmy2B_ExPoint', 2)
    GFX_0('2B_Shot', 7)
    Unknown23029(1, 2317, 0)
    SFX_3('ag002')
    sprite('null', 200)
    Unknown4010(0)

@State
def __2B_Shot():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(2)
        Damage(750)
        AttackP1(60)
        AttackP2(100)
        Unknown11092(1)
        AirUntechableTime(20)
        AirPushbackX(1000)
        Unknown11057(700)
        Hitstop(6)
        Unknown23182(2)
        MinimumDamagePct(0)

        def upon_LANDING():
            Unknown13(25)
        Unknown3029(1)
        physicsXImpulse(10000)
        Unknown4061(2)
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 2310):
                Unknown1072(25000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2311):
                Unknown1072(10000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2312):
                Unknown1072(-5000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2313):
                Unknown1072(-20000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2314):
                Unknown1072(-35000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2315):
                Unknown1072(-50000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2316):
                Unknown1072(-65000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)
            if (SLOT_48 == 2317):
                Unknown1072(-80000)
                Unknown4055(0)
                Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
                Unknown1110(40000, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown13(25)
            Unknown23029(3, 2318, 0)

        def upon_44():
            Unknown13(25)

        def upon_LANDING():
            GFX_1('agef_handgunshock_04', 100)
            Unknown13(25)
        Unknown23067('agef_gunspeed_00')
    sprite('dmy_machinegun', 60)
    RefreshMultihit()

@State
def Gatling_Matome():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2003(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 4031):
                Unknown2037(1)
            if (SLOT_48 == 4030):
                clearUponHandler(43)
                sendToLabel(9)
        Unknown2055(200)
    sprite('null', 2)
    label(0)
    sprite('dmyMachineGun_ExPoint', 2)
    GFX_0('Gatling_Shot', 0)
    if SLOT_2:
        Unknown23029(1, 4032, 0)
    SFX_3('ag002')
    sprite('dmyMachineGun_ExPoint', 2)
    GFX_0('Gatling_Shot', 1)
    if SLOT_2:
        Unknown23029(1, 4032, 0)
    SFX_3('ag002')
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 200)
    Unknown4010(0)

@State
def Gatling_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(230)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(18000)
        AirPushbackY(4000)
        Unknown30056('6079feff1e00000000000000')
        Hitstop(0)
        PushbackX(24800)
        Unknown23182(2)
        Unknown11057(600)
        Unknown11110(90)
        Unknown53(25)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_LANDING():
            Unknown13(25)
        Unknown4055(0)
        Unknown4045('616765665f6d696e6967756e666c6173685f303500000000000000000000000000000000')
        Unknown1110(100000, 0)
        Unknown4061(2)
        GFX_2('agef_gunspeed_00')
        Unknown3038(1)

        def upon_43():
            if (SLOT_48 == 4032):
                Damage(180)
                AttackP2(70)
    sprite('dmy_machinegun00', 1)
    RefreshMultihit()
    sprite('dmy_machinegun', 59)

@State
def Gatling_Matome_TAG():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2003(1)

        def upon_43():
            if (SLOT_48 == 4030):
                clearUponHandler(43)
                sendToLabel(9)
        Unknown2055(200)
    label(0)
    sprite('dmyMachineGun_ExPoint', 2)
    GFX_0('Gatling_Shot_TAG', 0)
    sprite('dmyMachineGun_ExPoint', 2)
    GFX_0('Gatling_Shot_TAG', 1)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 200)
    Unknown4010(0)

@State
def Gatling_Shot_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(300)
        AttackP1(70)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(18000)
        AirPushbackY(4000)
        Unknown30056('6079feff1e00000000000000')
        Hitstop(0)
        Unknown23182(2)
        Unknown11057(600)
        Unknown11042(1)
        Unknown53(25)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_LANDING():
            Unknown13(25)
        Unknown4055(0)
        Unknown4045('616765665f6d696e6967756e666c6173685f303500000000000000000000000000000000')
        Unknown1110(100000, 0)
        Unknown4061(2)
        GFX_2('agef_gunspeed_00')
        Unknown3038(1)
    sprite('dmy_machinegun00', 1)
    RefreshMultihit()
    sprite('dmy_machinegun', 59)

@State
def AirBalkan_Matome():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2003(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 4071):
                Unknown2037(1)
            if (SLOT_48 == 4070):
                clearUponHandler(43)
                sendToLabel(9)
        Unknown2055(200)
    sprite('null', 2)
    label(0)
    sprite('dmyAirMachineGun_ExPoint', 2)
    GFX_0('agef_handgunflash_03A', 0)
    GFX_0('AirBalkan_Shot', 0)
    if SLOT_2:
        Unknown23029(1, 4072, 0)
    SFX_3('ag002')
    sprite('dmyAirMachineGun_ExPoint', 2)
    GFX_0('agef_handgunflash_03A', 0)
    GFX_0('AirBalkan_Shot', 0)
    Unknown36(1)
    teleportRelativeX(-50000)
    Unknown35()
    if SLOT_2:
        Unknown23029(1, 4072, 0)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 200)
    Unknown4010(0)

@State
def agef_handgunflash_03A():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1072(45000)
        Unknown4055(0)
        Unknown23067('agef_handgunflash_03')
    sprite('null', 60)

@State
def AirBalkan_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(250)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(4000)
        AirUntechableTime(24)
        Hitstop(0)
        Unknown23182(2)
        Unknown11057(600)
        Unknown53(25)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)

        def upon_LANDING():
            GFX_1('agef_handgunshock_04', 100)
            Unknown13(25)
        Unknown1072(45000)
        Unknown1110(60000, 0)
        Unknown3033()
        Unknown4061(2)
        Unknown3038(1)
        GFX_2('agef_gunspeed_00')

        def upon_43():
            if (SLOT_48 == 4072):
                Damage(250)
    sprite('dmy_machinegunex', 200)
    RefreshMultihit()

@Subroutine
def CanonShot_Init():
    callSubroutine('CanonShot_Atk')
    Unknown4061(2)
    Unknown3033()
    GFX_2('agef_canonsphere_01')
    Unknown2055(200)
    Unknown2015(35)
    Unknown2016(20)
    Unknown23087(20)
    Unknown2053(1)

    def upon_7():
        Unknown1028(0)
        Unknown1019(-20)

    def upon_CLEAR_OR_EXIT():
        if SLOT_51:
            SLOT_51 = 0
        else:
            GFX_1('agef_canonzanzou_01', 100)
            SLOT_51 = 1
        if SLOT_2:
            if CheckInput(INPUT_RELEASE_A):
                sendToLabel(3)

    def upon_ON_HIT_OR_BLOCK():
        sendToLabel(3)

    def upon_LANDING():
        sendToLabel(3)

    def upon_44():
        Unknown13(25)

@Subroutine
def CanonShot_Atk():
    AttackLevel_(3)
    AttackP1(80)
    AttackP2(70)
    Unknown11092(1)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(0)
    Unknown9017(1)

@Subroutine
def CanonShot_Atk2nd():
    AirUntechableTime(60)
    AirPushbackX(3000)
    AirPushbackY(28000)
    Hitstop(1)

@State
def CanonShot_A():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('CanonShot_Init')
        physicsXImpulse(30000)
        physicsYImpulse(22500)
        Unknown1028(-800)
        setGravity(2000)
    sprite('dmy_canon', 10)
    sprite('dmy_canon', 2)
    label(2)
    sprite('dmy_canon', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('dmy_canon00', 5)
    RefreshMultihit()
    callSubroutine('CanonShot_Atk2nd')
    SLOT_51 = 0
    Unknown2037(0)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(44)
    Unknown1084(1)
    GFX_1('agef_bom_06', 0)
    Unknown3004(-50)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    DisableAttackRestOfMove()
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)

@State
def CanonShot_B():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('CanonShot_Init')
        clearUponHandler(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
            else:
                GFX_1('agef_canonzanzou_01', 100)
                SLOT_51 = 1
            if SLOT_2:
                if CheckInput(INPUT_RELEASE_B):
                    sendToLabel(3)

        def upon_4():
            Unknown1019(95)
            Unknown1028(0)
        physicsXImpulse(22000)
        physicsYImpulse(30000)
        Unknown1028(-350)
        setGravity(1000)
    sprite('dmy_canon', 10)
    sprite('dmy_canon', 2)
    label(2)
    sprite('dmy_canon', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('dmy_canon00', 5)
    RefreshMultihit()
    callSubroutine('CanonShot_Atk2nd')
    SLOT_51 = 0
    Unknown2037(0)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(44)
    Unknown1084(1)
    GFX_1('agef_bom_06', 0)
    Unknown3004(-50)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    DisableAttackRestOfMove()
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)

@State
def AirCanonShot_A():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('CanonShot_Init')
        physicsXImpulse(15000)
        physicsYImpulse(5000)
        Unknown1028(-375)
        setGravity(700)
    sprite('dmy_canon', 10)
    sprite('dmy_canon', 23)
    sprite('dmy_canon', 2)
    Unknown1028(0)
    label(2)
    sprite('dmy_canon', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('dmy_canon00', 5)
    RefreshMultihit()
    callSubroutine('CanonShot_Atk2nd')
    SLOT_51 = 0
    Unknown2037(0)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(44)
    Unknown1084(1)
    GFX_1('agef_bom_06', 0)
    Unknown3004(-50)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    DisableAttackRestOfMove()
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)

@State
def AirCanonShot_B():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('CanonShot_Init')
        clearUponHandler(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
            else:
                GFX_1('agef_canonzanzou_01', 100)
                SLOT_51 = 1
            if SLOT_2:
                if CheckInput(INPUT_RELEASE_B):
                    sendToLabel(3)
        physicsXImpulse(30000)
        physicsYImpulse(5000)
        Unknown1028(-700)
        setGravity(700)
    sprite('dmy_canon', 10)
    sprite('dmy_canon', 23)
    sprite('dmy_canon', 2)
    Unknown1028(0)
    label(2)
    sprite('dmy_canon', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('dmy_canon00', 5)
    RefreshMultihit()
    callSubroutine('CanonShot_Atk2nd')
    SLOT_51 = 0
    Unknown2037(0)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(44)
    Unknown1084(1)
    GFX_1('agef_bom_06', 0)
    Unknown3004(-50)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    DisableAttackRestOfMove()
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)

@State
def CanonShot_TAGMatome():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown11042(1)
    sprite('null', 3)
    GFX_0('CanonShot_TAG1', 100)
    sprite('null', 300)
    GFX_0('CanonShot_TAG2', 100)

@State
def CanonShot_TAG1():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('CanonShot_Init')
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        Unknown11042(1)
        physicsXImpulse(15000)
        physicsYImpulse(25000)
        Unknown1028(-250)
        setGravity(2000)
        Unknown48('190000000200000033000000030000000200000013000000')
        if (SLOT_51 <= 300000):
            physicsXImpulse(7000)
            physicsYImpulse(25000)
            Unknown1028(-250)
            setGravity(1500)

        def upon_4():
            Unknown1019(97)
            Unknown1028(0)
    sprite('dmy_canon', 10)
    sprite('dmy_canon', 2)
    Unknown2037(1)
    label(2)
    sprite('dmy_canon', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('dmy_canon00', 5)
    RefreshMultihit()
    callSubroutine('CanonShot_Atk2nd')
    SLOT_51 = 0
    Unknown2037(0)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(44)
    Unknown1084(1)
    GFX_1('agef_bom_06', 0)
    Unknown3004(-50)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    DisableAttackRestOfMove()
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)

@State
def CanonShot_TAG2():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('CanonShot_Init')
        Unknown23182(2)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        Unknown11042(1)
        physicsXImpulse(25000)
        physicsYImpulse(25000)
        Unknown1028(-250)
        setGravity(2000)
        Unknown48('190000000200000033000000030000000200000013000000')
        if (SLOT_51 >= 800000):
            physicsXImpulse(28500)
            physicsYImpulse(25000)
            Unknown1028(-250)
            setGravity(1500)

        def upon_4():
            Unknown1019(97)
            Unknown1028(0)
    sprite('dmy_canon', 10)
    sprite('dmy_canon', 2)
    Unknown2037(1)
    label(2)
    sprite('dmy_canon', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('dmy_canon00', 5)
    RefreshMultihit()
    callSubroutine('CanonShot_Atk2nd')
    SLOT_51 = 0
    Unknown2037(0)
    clearUponHandler(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(44)
    Unknown1084(1)
    GFX_1('agef_bom_06', 0)
    Unknown3004(-50)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)
    DisableAttackRestOfMove()
    sprite('dmy_canon00', 5)
    GFX_1('agef_bom_06', 0)

@State
def agef_aircanon_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1096(800)
    Unknown1072(250000)

@State
def agef_aircanon_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1096(750)
    Unknown1072(230000)

@State
def agef_aircanon_orgia_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(250000)
    Unknown1064(1400)

@State
def agef_aircanon_orgia_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(230000)
    Unknown1096(1200)

@State
def agef_aircanon_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1096(750)
    Unknown1072(230000)

@State
def agef_aircanon_orgia_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(250000)
    Unknown1064(1400)

@State
def agef_aircanon_orgia_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(230000)
    Unknown1096(1200)

@State
def FlamethrowerStart():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_firestart_01')
    sprite('null', 24)

@State
def FlamethrowerD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3430385f666972655f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('FlameCircleD', 100)
    Unknown1074(30000)
    sprite('null', 10)
    Unknown1074(20000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def FlameCircleD():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown3032()
        GFX_2('agef_firecircle_02')
    sprite('null', 15)
    sprite('null', 10)
    Unknown3004(-26)

@State
def FlamethrowerC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3430385f666972655f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('FlameCircleC', 100)
    Unknown1074(30000)
    sprite('null', 20)
    Unknown1074(20000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def FlameCircleC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_firecircle_02')
    sprite('null', 25)
    sprite('null', 10)
    Unknown3004(-26)

@State
def AtenaFlame():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3430385f666972655f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 10)
    Unknown3004(26)
    sprite('null', 25)
    sprite('null', 10)
    Unknown3004(-26)

@State
def AtenaFlameEX():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3430385f666972655f303165782e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 20)
    Unknown3004(17)
    Unknown1074(2000)
    sprite('null', 31)
    sprite('null', 10)
    Unknown3004(-26)

@State
def AtenaFlameA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3430385f666972655f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 23)

@State
def AtenaFlameB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3430385f666972655f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 8)
    Unknown1072(60000)
    sprite('null', 5)
    Unknown3004(-51)

@State
def AtenaFlameBex():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3430385f666972655f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1056(1700)
    sprite('null', 8)
    Unknown1072(60000)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Pandora_Matome():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2003(1)

        def upon_43():
            if (SLOT_48 == 4100):
                clearUponHandler(43)
                sendToLabel(9)
        Unknown2055(300)
    label(0)
    sprite('dmyRapidMissile_ExPoint', 4)
    GFX_0('Pandora_Shot', 0)
    sprite('dmyRapidMissile_ExPoint', 4)
    GFX_0('Pandora_Shot', 1)
    sprite('dmyRapidMissile_ExPoint', 4)
    GFX_0('Pandora_Shot', 2)
    sprite('dmyRapidMissile_ExPoint', 4)
    GFX_0('Pandora_Shot', 3)
    sprite('dmyRapidMissile_ExPoint', 4)
    GFX_0('Pandora_Shot', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 300)
    Unknown4010(0)

@State
def Pandora_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        AirUntechableTime(28)
        hitstun(28)
        Hitstop(3)
        AirPushbackX(12000)
        AirPushbackY(8000)
        PushbackX(15000)
        Unknown9017(1)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown11110(60)
        Unknown4061(2)

        def upon_ON_HIT_OR_BLOCK():
            Unknown13(25)
            SFX_3('bomb_m')

        def upon_LANDING():
            Unknown13(25)
            SFX_3('bomb_m')

        def upon_44():
            Unknown13(25)
            SFX_3('bomb_m')

        def upon_46():
            Unknown13(25)
            SFX_3('bomb_m')
    sprite('dmy_missile', 19)
    GFX_0('MissileBackfire', 0)
    physicsXImpulse(-20000)
    Unknown1028(700)
    SFX_3('ag005')
    sprite('dmy_missile', 21)
    Unknown1028(1600)
    SLOT_13 = SLOT_41
    YAccel(1)
    sprite('dmy_missile', 10)
    SFX_3('blaze_normal')
    label(0)
    sprite('dmy_missile', 30)
    Unknown53(1)
    loopRest()
    gotoLabel(0)

@State
def agef_missile_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-115000)
    Unknown1096(1200)

@State
def agef_missile_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-140000)
    Unknown1096(1200)

@State
def agef_orgia_shotgun():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(180000)
    Unknown1096(500)

@State
def agef_orgia_shotgun_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(215000)
    Unknown1096(450)

@State
def agef_orgia_shotgun_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-70000)
    Unknown1096(500)

@State
def agef_orgia_shotgun_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-135000)
    Unknown1096(500)

@State
def MissileBackfire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4015()
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2019(500)
        GFX_2('agef_missilefire_02')
        Unknown3001(0)

        def upon_STATE_END():
            GFX_1('agef_bom_05', 100)
    sprite('null', 20)
    Unknown3004(17)
    label(1)
    sprite('null', 1)
    GFX_1('agef_missilesmoke', 100)
    gotoLabel(1)

@State
def BarrierEnagy():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433305f736869656c645f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 33)
    GFX_1('atef_surfingtame_02', 100)
    Unknown1099(-5)
    sprite('null', 5)
    Unknown3004(-26)

@State
def SurfingBarrierAtk():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433305f736869656c645f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(200)
    sprite('null', 3)
    GFX_0('DBarrierAtkShock', 100)
    sprite('null', 3)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    sprite('null', 3)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    sprite('null', 3)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    sprite('null', 3)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    sprite('null', 3)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    sprite('null', 3)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    sprite('null', 5)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    Unknown3004(-26)

@State
def BarrierEyeFire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433305f657965666972655f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 25)
    Unknown3004(17)
    sprite('null', 18)

@State
def SurfingBarrierAtkOD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433305f736869656c645f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(200)

        def upon_43():
            if (SLOT_48 == 5013):
                sendToLabel(1)
    sprite('null', 3)
    GFX_0('DBarrierAtkShock', 100)
    label(0)
    sprite('null', 3)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    sprite('null', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown4045('617465665f73757266696e67666972655f30300000000000000000000000000064000000')
    Unknown3004(-26)

@State
def BarrierDashEyeFire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433305f657965666972655f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 15)
    sprite('null', 5)
    Unknown3004(-51)

@State
def eyeHikari():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 4)
    GFX_2('atef_eyelight_05')
    sprite('null', 5)
    physicsXImpulse(12500)

@State
def DBarrierAtkShock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('616765665f3230365f736869656c6473686f636b5f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4011(2)
    sprite('null', 13)
    physicsXImpulse(-8000)

@State
def agef_surfing_orgia_hold():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner')
    Unknown1072(-90000)
    Unknown1064(800)

@State
def agef_surfing_orgia_hold_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1072(-90000)
    Unknown1064(800)

@State
def agef_surfing_orgia():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 2)
    Unknown23067('agef_orgia_burner')
    Unknown1096(2400)
    SFX_3('ag006')
    sprite('null', 32767)
    SFX_3('airdash_m')

@State
def agef_surfing_orgia_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)
    Unknown23067('agef_orgia_burner_back')
    Unknown1096(2400)

@State
def agef_surfing_burner_hold():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-90000)
    Unknown1064(400)

@State
def agef_surfing_burner_hold_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-90000)
    Unknown1064(400)

@State
def agef_surfing_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 2)
    Unknown23067('agef_burner')
    Unknown1096(1750)
    SFX_3('ag006')
    sprite('null', 32767)
    SFX_3('airdash_m')

@State
def agef_surfing_burner_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1096(1750)

@State
def throwEnagyD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433315f7961726973706565645f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1056(1000)
    sprite('null', 5)
    GFX_0('throwEnagy3', 100)
    sprite('null', 20)
    sprite('null', 30)
    Unknown3004(-17)

@State
def throwEnagyOD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433315f7961726973706565645f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1056(1000)
    sprite('null', 5)
    GFX_0('throwEnagy3', 100)
    sprite('null', 20)
    sprite('null', 30)
    sprite('null', 30)
    Unknown3004(-17)

@State
def throwEnagy3():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433315f7961726973706565645f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 4)
    sprite('null', 10)
    Unknown3004(-26)
    physicsYImpulse(50000)
    Unknown1059(-50)
    sprite('null', 5)

@State
def throwEnagytame():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433315f7961726973706565645f30322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1072(45000)
        Unknown3001(0)
    sprite('null', 38)
    Unknown3004(7)
    GFX_2('atef_nagetame_00')
    sprite('null', 21)
    Unknown3004(0)
    sprite('null', 2)
    physicsYImpulse(50000)
    physicsXImpulse(-5000)
    Unknown1074(-6000)
    Unknown1067(100)
    Unknown1059(50)
    sprite('null', 2)
    physicsXImpulse(-20000)
    sprite('null', 10)
    Unknown1072(0)
    Unknown1074(0)

@State
def throwEnagytameD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433315f7961726973706565645f30322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1072(45000)
        Unknown3001(0)
    sprite('null', 40)
    Unknown3004(7)
    GFX_2('atef_nagetame_00')
    sprite('null', 29)
    Unknown3004(0)
    sprite('null', 2)
    Unknown1072(35000)
    Unknown1007(50000)
    sprite('null', 2)
    physicsXImpulse(0)
    Unknown1007(50000)
    teleportRelativeX(-50000)
    sprite('null', 10)
    physicsXImpulse(0)
    Unknown1007(50000)
    teleportRelativeX(-50000)
    Unknown1072(0)
    Unknown1074(0)

@State
def throwGroundShock():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3433315f7961726973706565645f30332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Spear_Reversal():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(2400)
        AttackP2(60)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackY(42000)
        Unknown30056('f04902003200000000000000')
        YImpluseBeforeWallbounce(2200)
        AirUntechableTime(60)
        PushbackX(12000)
        Unknown11084(1)
        Unknown9266(4)
        Unknown9016(1)
        Unknown30065(100)
        HitAirUnblockable(3)
        Unknown11044(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown4061(2)
        Unknown3033()
    sprite('dmy_spear', 2)
    GFX_0('throwEnagyD', 0)
    RefreshMultihit()
    physicsYImpulse(130000)
    ScreenShake(0, 8000)
    sprite('dmy_spear', 30)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirUntechableTime(40)
    HitAirUnblockable(0)

@State
def AddSpear():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(3700)
        AttackP1(48)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(80000)
        AirUntechableTime(200)
        Hitstop(30)
        Unknown9310(20)
        Unknown11084(1)
        Unknown9266(4)
        Unknown9016(1)
        Unknown4061(2)
        Unknown3033()

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(2, 5000, 0)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
    sprite('dmy_spear', 60)
    GFX_0('throwEnagyD', 0)
    RefreshMultihit()
    physicsYImpulse(130000)
    ScreenShake(0, 80000)

@State
def AddSpearDUO():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(500)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(80000)
        AirUntechableTime(200)
        Hitstop(30)
        Unknown9310(20)
        Unknown11084(1)
        Unknown9266(4)
        Unknown9016(1)
        Unknown4061(2)
        Unknown3033()

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(2, 5000, 0)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
    sprite('dmy_spear', 60)
    GFX_0('throwEnagyD', 0)
    RefreshMultihit()
    physicsYImpulse(130000)
    ScreenShake(0, 80000)

@State
def UltimateAirThrow_Camera():

    def upon_IMMEDIATE():
        Unknown2034(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    Unknown20000(1)
    Unknown1086(3)
    Unknown1007(200000)
    label(0)
    sprite('null', 32767)
    physicsXImpulse(90000)

@State
def Orion_Shot():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(310)
        MinimumDamagePct(12)
        AttackP2(100)
        Hitstop(0)
        Unknown9178(1)
        WallbounceReboundTime(0)
        AirUntechableTime(120)
        AirPushbackX(40000)
        AirPushbackY(5000)
        AirHitstunAnimation(12)
        Unknown11057(500)
        Unknown11069('Orion_Shot')
        Unknown30048(1)
        Unknown1025(80000, 120000)
        Unknown1096(1200)
        Unknown53(25)
        GFX_2('agef_gunspeed_00')
        Unknown3038(1)
        Unknown4055(0)
        Unknown4045('616765665f6d696e6967756e666c6173685f303500000000000000000000000000000000')
        Unknown4061(2)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(3000, 1000)

        def upon_43():
            if (SLOT_48 == 6000):
                Unknown11069('')
    sprite('dmy_machinegunex', 4)
    RefreshMultihit()
    sprite('dmy_machinegunex', 60)
    Unknown11023(1)

@State
def OrionSP_Shot():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(300)
        MinimumDamagePct(10)
        AttackP2(100)
        Hitstop(0)
        Unknown9178(1)
        WallbounceReboundTime(0)
        AirUntechableTime(120)
        AirPushbackX(40000)
        AirPushbackY(3000)
        AirHitstunAnimation(12)
        Unknown9362(1)
        Unknown11057(500)
        Unknown11069('OrionSP_Shot')
        Unknown30048(1)
        Unknown1025(80000, 120000)
        Unknown1096(1200)
        Unknown53(25)
        GFX_2('agef_gunspeed_00')
        Unknown3038(1)
        Unknown4055(0)
        Unknown4045('616765665f6d696e6967756e666c6173685f303500000000000000000000000000000000')
        Unknown4061(2)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(3000, 1000)

        def upon_43():
            if (SLOT_48 == 6000):
                Unknown11069('UltimateAirThrowOD_Exe')
    sprite('dmy_machinegunex', 4)
    RefreshMultihit()
    sprite('dmy_machinegunex', 60)
    Unknown11023(1)

@State
def OrionLastCanon():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        GFX_2('agef_canonsphere_01')
        teleportRelativeX(300000)
        physicsXImpulse(30000)
        Unknown1096(2500)
    sprite('null', 10)
    sprite('null', 60)
    Unknown1096(3000)
    Unknown1086(22)
    Unknown1007(220000)
    Unknown1084(1)

@State
def OrionFinish():

    def upon_IMMEDIATE():
        Unknown23067('agef_throwbom_07')
        Unknown3032()
        Unknown4061(0)
        Unknown1096(4050)
        Unknown26('OrionLastCanon')
    sprite('null', 60)

@State
def Ichigeki_Shot():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Damage(500)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(2000)
        AirPushbackY(2000)
        AirUntechableTime(200)
        Hitstop(0)
        Unknown11001(0, 0, 0)
        Unknown11084(1)
        Unknown11055(1)
        Unknown9310(1)
        Unknown11064(1)
        Unknown1072(25000)
        Unknown4055(0)
        Unknown4045('616765665f68616e6467756e666c6173685f303300000000000000000000000000000000')
        Unknown3033()
        Unknown4061(2)
        Unknown2054(1)
        Unknown53(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 7021):
                sendToLabel(1)
            if (SLOT_48 == 7022):
                sendToLabel(2)
    label(0)
    sprite('null', 1)
    sprite('dmy_machinegunex', 32767)
    Unknown1110(120000, 0)
    GFX_0('AgYakkyo', 100)
    GFX_2('agef_gunspeed_00')

    def upon_LANDING():
        GFX_1('agef_handgunshock_04', 100)
        Unknown13(25)
    loopRest()
    label(1)
    sprite('dmy_canon', 10)
    Unknown1110(120000, 0)
    Unknown9017(1)

    def upon_LANDING():
        GFX_1('agef_handgunshock_04', 100)
        Unknown13(25)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('dmy_canon', 10)
    Unknown1110(120000, 0)
    AirPushbackX(20000)
    AirPushbackY(38000)
    YImpluseBeforeWallbounce(1800)
    Unknown9017(1)
    Unknown1096(3000)
    if (SLOT_20 >= 500000):
        AirPushbackY(42000)
    if (SLOT_20 >= 700000):
        AirPushbackY(45000)

    def upon_12():
        Unknown23029(3, 7023, 0)

    def upon_LANDING():
        GFX_1('agef_handgunshock_04', 100)
        Unknown13(25)

    def upon_STATE_END():
        GFX_1('agef_bom_06', 0)
        SFX_3('bomb_m')
    loopRest()
    gotoLabel(2)

@State
def AgYakkyo():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_LANDING():
            YAccel(-60)
            Unknown1019(60)
            SFX_3('ag013')
        Unknown4061(2)
    sprite('vr_trap_yakkyo', 50)
    Unknown1025(-7500, -12500)
    Unknown1026(10000, 13000)
    Unknown1078(-1000, -10000)
    setGravity(2000)
    sprite('vr_trap_yakkyo', 20)
    Unknown3032()
    Unknown3004(-20)

@State
def BigYakkyo():

    def upon_IMMEDIATE():

        def upon_LANDING():
            YAccel(-60)
            Unknown1019(60)
            SFX_3('na006')
        Unknown4061(2)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    physicsXImpulse(-25000)
    physicsYImpulse(30000)
    Unknown1074(-10000)
    setGravity(2000)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)
    sprite('vr_trap_yakkyo2', 2)
    GFX_1('agef_yakkyoshock_smk', 0)

@State
def IchigekiSpear():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(10000)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirUntechableTime(9999)
        AirPushbackX(5000)
        AirPushbackY(10)
        YImpluseBeforeWallbounce(0)
        Hitstop(0)
        Unknown11001(-1, -1, -1)
        Unknown11084(1)
        Unknown9016(1)
        Unknown11064(1)
        Unknown11072(1, 500000, -200000)
        Unknown3032()
        Unknown4061(1)
        GFX_2('atef_ichiyarinage_pos')
        Unknown2054(1)

        def upon_78():
            clearUponHandler(78)
            ScreenShake(3000, 3000)
            GFX_0('IchigekiCamera', 100)
            Unknown21015('41737472616c4865617400000000000000000000000000000000000000000000591b000000000000')
            Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000631b000000000000')
            sendToLabel(0)
            Unknown23084(1)
            Unknown36(22)
            Unknown2053(0)
            Unknown2034(0)
            Unknown35()

        def upon_43():
            if (SLOT_48 == 7024):
                sendToLabel(2)
    sprite('vr_at450_00', 1)
    physicsXImpulse(70000)
    sprite('vr_at450_00', 32767)
    RefreshMultihit()
    label(0)
    sprite('vr_at450_00', 6)
    sprite('vr_at450_00', 4)
    Unknown36(22)
    physicsXImpulse(-70000)
    Unknown35()
    sprite('vr_at450_00', 10)
    sprite('vr_at450_00', 6)
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('vr_at450_00', 4)
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000005a1b000000000000')
    sprite('vr_at450_00', 1)
    Unknown36(22)
    physicsXImpulse(0)
    physicsYImpulse(1)
    setGravity(0)
    teleportRelativeY(705000)
    setGravity(0)
    Unknown35()

    def upon_CLEAR_OR_EXIT():
        Unknown36(22)
        physicsXImpulse(0)
        physicsYImpulse(1)
        setGravity(0)
        Unknown35()
    Unknown1086(22)
    physicsXImpulse(0)
    Unknown1007(200000)
    sprite('vr_at450_00', 19)
    sprite('vr_at450_00', 300)
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    sprite('vr_at450_00', 4)
    label(1)
    sprite('vr_at450_00', 4)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('vr_at450_00', 4)
    Unknown3001(0)
    loopRest()
    gotoLabel(2)

@State
def IchigekiThunderTame():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3435305f7468756e6465725f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 10)
    Unknown3004(26)
    sprite('null', 32767)

@State
def IchigekiThunderTame2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3435305f7468756e6465725f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 10)
    Unknown3004(26)
    sprite('null', 32767)

@State
def IchigekiThunderBallTame():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown3001(0)
        Unknown1096(2000)
        GFX_2('agef_ichigekishot_td2')
    sprite('null', 15)
    GFX_1('agef_ichigekiyotyou_th2', 100)
    sprite('null', 15)
    Unknown3001(255)
    Unknown1099(-20)
    sprite('null', 30)
    GFX_0('IchigekiThunderBallTame2', 100)
    GFX_0('IchigekiThunderTame2', 100)
    sprite('null', 32767)
    Unknown1099(0)

@State
def IchigekiTobiFire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_ichigekifly_tb')

        def upon_43():
            if (SLOT_48 == 7025):
                sendToLabel(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def IchigekiRenshaFire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_ichigekifly2b_cl')

        def upon_43():
            if (SLOT_48 == 7025):
                sendToLabel(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def IchigekiThunderBallTame2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_ichigekiyotyou2_tb')
    sprite('null', 32767)

@State
def IchigekiSmoke():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_opensmk_ue')
        Unknown1072(-45000)
    sprite('null', 50)

@State
def IchigekiSmoke2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_opensmk_ue')
        Unknown1072(-120000)
    sprite('null', 50)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(1)
        Unknown6001(1)
        Unknown1000(-640000)
        teleportRelativeY(-2384000)
        Unknown1007(3000000)
        teleportRelativeX(1600000)
        Unknown1096(2000)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1001(640000)
        teleportRelativeX(1600000)
    sprite('ichigeki0', 5)
    Unknown1099(-160)
    physicsXImpulse(-150000)
    physicsYImpulse(-60000)
    sprite('ichigeki0', 60)
    Unknown1099(-1)
    physicsXImpulse(-350)
    physicsYImpulse(-500)
    sprite('keep', 5)
    Unknown3004(-51)

@State
def Ichigeki_LastShot():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(20000)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(500)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(9999)
        Hitstop(2)
        Unknown11001(8, 0, 8)
        Unknown11084(1)
        Unknown11055(1)

        def upon_12():
            clearUponHandler(12)
            physicsXImpulse(0)
            physicsYImpulse(0)
            Unknown1067(5)
            Unknown21015('4963686967656b69537065617200000000000000000000000000000000000000701b000000000000')
            GFX_0('IchigekiBomb', 100)
            Unknown21015('41737472616c48656174000000000000000000000000000000000000000000005b1b000000000000')
            sendToLabel(1)
        Unknown4007(2)
        Unknown3032()
        Unknown3001(0)
        Unknown1096(2000)
        Unknown3038(1)
        GFX_2('agef_ichigekishot_th2')
    sprite('dmy_ichigekitama', 10)
    physicsXImpulse(3000)
    sprite('dmy_ichigekitama', 5)
    ScreenShake(3000, 3000)
    Unknown3004(51)
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000651b000000000000')
    sprite('dmy_ichigekitama', 4)
    ScreenShake(3000, 3000)
    RefreshMultihit()
    physicsXImpulse(80000)
    SFX_3('ag010')
    sprite('dmy_ichigekitama', 12)
    RefreshMultihit()
    sprite('dmy_ichigekitama', 20)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('dmy_ichigekitama', 20)
    SFX_3('ag010')
    sprite('dmy_ichigekitama', 12)
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('dmy_ichigekitama', 60)
    physicsXImpulse(80000)
    Unknown1007(500000)
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000661b000000000000')
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    SFX_3('ag010')
    label(0)
    sprite('dmy_ichigekitama', 4)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('dmy_ichigekitama', 3)
    SFX_3('damage_magic_mh')
    sprite('dmy_ichigekitama', 3)
    SFX_3('damage_magic_mh')
    sprite('dmy_ichigekitama', 3)
    SFX_3('damage_magic_mh')
    sprite('dmy_ichigekitama', 11)
    sprite('dmy_ichigekitama', 20)
    Unknown3004(-26)

@State
def IchigekiHit():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_ichigekihit_tb')
    sprite('null', 3)
    SFX_3('quake_l')
    SFX_3('bomb_l')
    sprite('null', 32767)
    SFX_3('quake_l')
    SFX_3('bomb_l')

@State
def IchigekiBomb2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3435305f626f6d5f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 20)
    sprite('null', 10)
    Unknown3004(-26)

@State
def IchigekiBomb():

    def upon_IMMEDIATE():
        Unknown4006(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('616765665f3435305f626f6d5f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 25)
    Unknown3004(9)
    Unknown1099(150)
    GFX_0('IchigekiHit', 100)
    sprite('null', 10)
    GFX_0('IchigekiBomb2', 100)
    Unknown1099(300)
    sprite('null', 30)
    GFX_0('Ichigekiwhite', 100)
    sprite('null', 30)
    Unknown26('IchigekiHit')

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
    sprite('vr_ag450_white', 30)
    Unknown3004(30)
    sprite('vr_ag450_white', 100)
    Unknown3004(-26)
    sprite('vr_ag450_white', 10)
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000671b000000000000')

@State
def IchigekiWinSmoke():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_2('agef_ichigekihit_bsmk3')

        def upon_43():
            if (SLOT_48 == 7025):
                sendToLabel(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown3004(-17)

@State
def MatchWinCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
    sprite('null', 32767)

@State
def IchigekiCamera():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 7011):
                sendToLabel(1)
            if (SLOT_48 == 7012):
                sendToLabel(2)
            if (SLOT_48 == 7013):
                sendToLabel(3)
            if (SLOT_48 == 7014):
                sendToLabel(4)
            if (SLOT_48 == 7015):
                sendToLabel(5)
        Unknown2054(1)

        def upon_CLEAR_OR_EXIT():
            SLOT_105 = (SLOT_105 + SLOT_51)
        Unknown3029(1)
        Unknown3032()
        Unknown3001(80)
        Unknown2053(0)
        Unknown2034(0)
        Unknown3038(1)
    label(1)
    sprite('keep', 32767)
    teleportRelativeX(-250000)
    physicsXImpulse(70000)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20002(1)
    Unknown20003(1)
    label(2)
    sprite('keep', 10)
    physicsXImpulse(0)
    Unknown1086(3)
    teleportRelativeX(1000000)
    Unknown1007(100000)
    Unknown20009(400)
    sprite('keep', 20)
    physicsYImpulse(-5000)
    physicsXImpulse(-50000)

    def upon_CLEAR_OR_EXIT():
        SLOT_105 = (SLOT_105 + 30)
    sprite('keep', 32767)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown20009(1000)
    clearUponHandler(3)
    Unknown1086(3)
    label(3)
    sprite('keep', 19)
    Unknown1086(4)
    physicsXImpulse(80000)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(4)
    sprite('null', 32767)
    Unknown1086(22)
    physicsXImpulse(0)
    Unknown1007(200000)
    label(5)
    sprite('keep', 32767)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown20009(1000)
    Unknown1086(3)

@State
def agef_entry1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(0)
        Unknown3032()
        Unknown3001(250)
    sprite('vr_agef600_15', 5)
    Unknown3004(-13)
    sprite('vr_agef600_16', 5)
    sprite('vr_agef600_17', 5)
    sprite('vr_agef600_18', 5)

@State
def agef_entry2_pod():

    def upon_IMMEDIATE():
        teleportRelativeX(50000)
        Unknown1007(-150000)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3032()
        Unknown13044(1)
        Unknown23069(1)
        sendToLabelUpon(32, 0)
    sprite('vr_agef601_pod00', 32767)
    label(0)
    sprite('vr_agef601_pod02', 3)
    sprite('vr_agef601_pod04', 3)
    sprite('vr_agef601_pod06', 3)
    sprite('vr_agef601_pod08', 3)
    sprite('vr_agef601_pod10', 3)
    sprite('vr_agef601_pod12', 3)
    sprite('vr_agef601_pod14', 3)
    sprite('vr_agef601_pod15', 3)

@State
def agef_entry2_pod2():

    def upon_IMMEDIATE():
        teleportRelativeX(50000)
        Unknown1007(-150000)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3032()
        Unknown13044(1)
        Unknown23069(1)
        sendToLabelUpon(32, 0)
    sprite('vr_agef601_pod01', 32767)
    label(0)
    sprite('vr_agef601_pod03', 3)
    sprite('vr_agef601_pod05', 3)
    sprite('vr_agef601_pod07', 3)
    sprite('vr_agef601_pod09', 3)
    sprite('vr_agef601_pod11', 3)
    sprite('vr_agef601_pod13', 3)

@State
def agef_entry2_hole():

    def upon_IMMEDIATE():
        teleportRelativeX(50000)
        Unknown1007(-150000)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3032()
        Unknown13044(1)
        sendToLabelUpon(32, 0)
    sprite('vr_agef601_hole00', 32767)
    label(0)
    sprite('vr_agef601_hole01', 6)
    SFX_3('ag003')
    sprite('vr_agef601_hole02', 6)
    sprite('vr_agef601_hole03', 30)
    sprite('vr_agef601_hole02', 6)
    SFX_3('ag003')
    sprite('vr_agef601_hole01', 6)
    sprite('vr_agef601_hole00', 10)
    sprite('vr_agef601_hole00', 32767)
    Unknown3004(-8)

@State
def agef_entry2_seat():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        Unknown3032()
        Unknown13044(1)
        Unknown23069(1)
        sendToLabelUpon(32, 0)
    sprite('vr_agef601_seat', 32767)
    label(0)
    sprite('vr_agef601_seat00', 3)
    sprite('vr_agef601_seat01', 3)
    sprite('vr_agef601_seat02', 3)

@State
def agef_entry2_ring():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        Unknown3032()
        Unknown13044(1)
        Unknown23069(1)
        sendToLabelUpon(32, 0)
    sprite('vr_agef601_ring00', 32767)
    label(0)
    sprite('vr_agef601_ring00', 1)
    sprite('vr_agef601_ring01', 4)
    sprite('vr_agef601_ring02', 4)
    sprite('vr_agef601_ring03', 4)
    sprite('vr_agef601_ring04', 4)
    sprite('vr_agef601_ring05', 4)
    sprite('vr_agef601_ring06', 4)

@State
def agef_entry3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner')
    Unknown1072(-80000)
    Unknown1096(675)
    Unknown1007(-8000)

@State
def agef_entry3_back():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-110000)
    Unknown1096(525)
    Unknown1007(-8000)

@State
def agef_entry3_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_backstep_flare')
    Unknown1072(-80000)
    Unknown1056(600)
    Unknown1064(800)
    Unknown1007(6000)

@State
def agef_entry3_back_flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_backstep_back_flare')
    Unknown1072(-110000)
    Unknown1056(700)
    Unknown1064(550)
    Unknown1007(13500)

@State
def agef_win_burner_r60():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-60000)
    Unknown1064(300)

@State
def agef_win_burner_r75():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-75000)
    Unknown1064(425)

@State
def agef_win_burner():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-90000)
    Unknown1064(750)
    Unknown1007(-8000)

@State
def agef_win_burner_upper():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_burner_back')
    Unknown1072(-90000)
    Unknown1096(1250)
    Unknown1007(-64000)

@State
def agef_win_burner_line():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 32767)
    Unknown23067('agef_win_burner_line')

@State
def agef_win_burner_somke():
    sprite('null', 32767)
    Unknown23067('agef_win_smoke')

@State
def agef_win2_steam_r():
    sprite('null', 32767)
    Unknown23067('agef_win2_steam')
    Unknown1072(30000)

@State
def agef_win2_steam_l():
    sprite('null', 32767)
    Unknown23067('agef_win2_steam')
    Unknown1072(-30000)

@State
def MatchWinCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
    sprite('null', 32767)

@State
def PersonaWin2():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23022(1)
        Unknown23015(2)
        Unknown23023()
        Unknown23184('030000006400000070110100a086010070110100a086010070110100a0860100')
        callSubroutine('PAG_CheckWarp')
    sprite('at611_00', 20)
    sprite('at611_01', 2)
    GFX_0('Win2', 100)
    sprite('at611_02', 2)
    sprite('at611_03', 2)
    SFX_3('slash_pole_fast')
    sprite('at611_04', 3)
    sprite('at611_05', 3)
    sprite('at611_06', 6)
    sprite('at611_07', 6)
    label(3)
    sprite('at611_08', 4)
    sprite('at611_09', 4)
    sprite('at611_10', 4)
    gotoLabel(3)

@State
def Win2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(1)
    sprite('vr_at611_00', 2)
    sprite('vr_at611_01', 2)
    sprite('vr_at611_02', 4)

@State
def P4U_Cutin_Parent():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)
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
    sprite('vr_99p4u_face00', 45)
    SFX_0('spsys_over_power')
    SFX_0('spsys_over_power')
    if SLOT_168:
        GFX_0('P4U_ka_NotJPN', 100)
    else:
        GFX_0('P4U_ka_JPN', 100)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(180)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(120)
    sprite('vr_99p4u_face00', 1)
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
    sprite('vr_p4_ka_mozi', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi', 1)
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
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi_notjpn', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(60)
    Unknown1096(100)