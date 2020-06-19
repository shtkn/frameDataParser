
def init():
    Move_Register('CmnActInvincibleAttack', 24)
    Move_Register('CmnActChangePartnerAssistAtk_A', 24)
    Move_Register('CmnActChangePartnerAssistAtk_B', 24)
    Move_Register('CmnActChangePartnerAssistAtk_D', 24)
    Move_Register('AN_ChangePartnerDD_Exe', 24)
    Move_Register('AN_ChangePartnerDDOD_Exe', 24)
    Move_Register('AstralHeat', 24)
    Move_Register('Ichigeki', 24)
    Move_Register('UltimateDUOSP', 24)
    Move_Register('UltimateDUO', 24)


    Move_Register('AntiAir_D', 24)



@State
def AntiAir_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(900)
        AttackP1(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(10000)
        AirUntechableTime(44)
        Hitstop(1)
        FreezeCount(10)
        FreezeDuration(50)
        HitAirUnblockable(3)
        Unknown9016(1)
        Unknown11056(0)
        StarterRating(0)
        ConsumeSuperMeter(-2500)
        GFX_0('jnef_25percent', -1)
        setInvincible(1)
        Unknown2004(1, 0)
        callSubroutine('CheckDriveFlash')
        callSubroutine('CheckOverDriveSpecial')
        if SLOT_137:
            Unknown10000(80)
    sprite('jn407_00', 3)	# 1-3
    Unknown3029(1)
    Unknown3069(0)
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('jnse_22')
    sprite('jn407_01', 3)	# 4-6
    sprite('jn407_02', 3)	# 7-9
    sprite('jn407_03', 3)	# 10-12
    sprite('jn407_04', 3)	# 13-15	 **attackbox here**
    SFX_3('jnse_21')
    GFX_0('zan407', 0)
    SFX_0('009_swing_rapier_0')
    SFX_1('jn208')
    sprite('jn407_05', 3)	# 16-18
    sprite('jn407_06', 3)	# 19-21
    sprite('jn407_07', 3)	# 22-24
    setInvincible(0)
    sprite('jn407_08', 3)	# 25-27
    sprite('jn407_26', 3)	# 28-30
    sprite('jn407_26', 54)	# 31-84
    sendToLabelUpon(26, 0)
    sprite('jn407_26', 1)	# 85-85
    Unknown8004(100, 1, 1)
    HitOverhead(4)
    HitLow(4)
    HitAirUnblockable(4)
    FatalCounter(1)
    loopRest()
    label(0)
    clearUponHandler(26)
    sprite('jn407_09', 3)	# 86-88
    sprite('jn407_10', 2)	# 89-90
    sprite('jn407_11', 2)	# 91-92
    SFX_3('jnse_21')
    GFX_0('EFF28AtkD', 0)
    sprite('jn407_12', 2)	# 93-94	 **attackbox here**
    StartMultihit()
    sprite('jn407_12', 1)	# 95-95	 **attackbox here**
    RefreshMultihit()
    Damage(1200)
    if SLOT_137:
        Unknown10000(80)
    Hitstop(20)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(48000)
    AirPushbackY(12000)
    WallbounceReboundTime(5)
    AirHitstunAfterWallbounce(44)
    Unknown9362(1)
    Unknown9364(30)
    Unknown9310(1)
    Unknown9202(30)
    Unknown9251()
    HitAirUnblockable(0)
    StarterRating(3)
    if SLOT_58:
        Unknown9107()
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    SFX_1('jn209')
    sprite('jn407_13', 3)	# 96-98
    sprite('jn407_14', 3)	# 99-101
    sprite('jn407_15', 3)	# 102-104
    sprite('jn407_16', 3)	# 105-107
    sprite('jn407_17', 3)	# 108-110
    sprite('jn407_18', 3)	# 111-113
    sprite('jn407_19', 3)	# 114-116
    sprite('jn407_20', 3)	# 117-119
    sprite('jn407_21', 5)	# 120-124
    sprite('jn407_22', 4)	# 125-128
    Unknown3029(0)
    sprite('jn407_23', 3)	# 129-131
    sprite('jn407_24', 3)	# 132-134
    GFX_0('EffNoutou', 0)
    sprite('jn407_25', 3)	# 135-137
