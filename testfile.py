
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


    Move_Register('AirAssault', 24)


@State
def AirAssault():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(90)
        AttackP2(82)
        GroundedHitstunAnimation(2)
        Unknown9130(8)
        Unknown9142(99)
        AirHitstunAnimation(17)
        AirPushbackX(24000)
        AirPushbackY(-36000)
        Unknown11058('0100000000000000000000000000000000000000')
        AirUntechableTime(36)
        PushbackX(19800)
        Unknown9310(1)
        Unknown9016(1)
        StarterRating(2)
        if SLOT_110:
            FreezeCount(5)
            FreezeDuration(55)
        callSubroutine('CheckDriveFlash')
        if SLOT_137:
            Unknown10000(80)
    sprite('jn413_00', 2)	# 1-2
    callSubroutine('OverDrivePowerUpSkill')
    Unknown1019(20)
    Unknown1051(0)
    YAccel(0)
    Unknown1039(-20)
    sprite('jn413_01', 2)	# 3-4
    sprite('jn413_02', 2)	# 5-6
    sprite('jn413_05', 3)	# 7-9
    SFX_1('jn215')
    sprite('jn413_06', 3)	# 10-12
    Unknown1084(1)
    physicsXImpulse(-9000)
    physicsYImpulse(20000)
    setGravity(1800)
    SFX_0('009_swing_rapier_2')
    SFX_3('jnse_21')
    GFX_0('EFF413C', -1)
    sprite('jn413_07', 3)	# 13-15	 **attackbox here**
    Unknown22004(8, 1)
    sprite('jn413_08', 3)	# 16-18
    Recovery()
    Unknown1019(50)
    sprite('jn413_09', 3)	# 19-21
    sprite('jn413_10', 6)	# 22-27
    GFX_0('EffNoutou', 0)
    Unknown1019(50)
    sprite('jn413_11', 5)	# 28-32
    Unknown1019(50)
    sprite('jn413_12', 5)	# 33-37
    sprite('jn020_05', 3)	# 38-40
    sprite('jn020_06', 3)	# 41-43
    sprite('jn020_07', 3)	# 44-46
    label(0)
    sprite('jn020_08', 3)	# 47-49
    sprite('jn020_09', 3)	# 50-52
    gotoLabel(0)