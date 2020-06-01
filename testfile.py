
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


    Move_Register('OffensiveCounterLand', 24)
    Move_Register('OffensiveCounterAir', 24)


@State
def OffensiveCounterLand():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(750)
        AttackP1(80)
        AttackP2(60)
        Unknown11001(0, 0, 0)
        AirPushbackX(12000)
        AirPushbackY(17000)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown30065(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown9266(6)
        Unknown2006()
        Unknown11092(1)
        callSubroutine('AtkEffLightning')
        Unknown2021(1)
        Unknown14083(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ubl320_00', 2)	# 1-2
    setInvincible(1)
    sprite('ubl320_01', 1)	# 3-3
    sprite('ubl320_02', 1)	# 4-4
    sprite('ubl320_03', 1)	# 5-5
    GFX_0('ubl_320_NearSpark_Eff', 100)
    GFX_0('ubl_310_BackSpark_Eff', 100)
    SFX_0('014_electric_sl')
    SFX_0('014_electric_sl')
    Unknown23119(4128831, 3, -1)
    sprite('ubl320_04', 1)	# 6-6	 **attackbox here**
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    SFX_0('014_electric_s')
    sprite('ubl320_07', 7)	# 19-25	 **attackbox here**
    StartMultihit()
    sprite('ubl320_08', 8)	# 26-33
    sprite('ubl320_09', 8)	# 34-41

@State
def OffensiveCounterAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(750)
        AttackP1(80)
        AttackP2(60)
        Unknown11001(0, 0, 0)
        AirPushbackX(12000)
        AirPushbackY(17000)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown30065(100)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown9266(6)
        Unknown2006()
        Unknown11092(1)
        callSubroutine('AtkEffLightning')
        Unknown2021(1)
        Unknown14083(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ubl320_00', 2)	# 1-2
    setInvincible(1)
    physicsXImpulse(5000)
    Unknown1028(-500)
    physicsYImpulse(0)
    setGravity(0)
    sprite('ubl320_01', 1)	# 3-3
    sprite('ubl320_02', 1)	# 4-4
    physicsXImpulse(0)
    Unknown1028(0)
    sprite('ubl320_03', 1)	# 5-5
    GFX_0('ubl_320_NearSpark_Eff', 100)
    GFX_0('ubl_310_BackSpark_Eff', 100)
    SFX_0('014_electric_sl')
    SFX_0('014_electric_sl')
    Unknown23119(4128831, 3, -1)
    sprite('ubl320_04', 1)	# 6-6	 **attackbox here**
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_05', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_0('014_electric_s')
    sprite('ubl320_07', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    SFX_0('014_electric_s')
    sprite('ubl320_07', 7)	# 19-25	 **attackbox here**
    StartMultihit()
    Unknown1043()
    sprite('ubl320_08', 2)	# 26-27
    sprite('ubl320_09', 2)	# 28-29
    label(0)
    sprite('ubl020_00', 3)	# 30-32
    sprite('ubl020_01', 3)	# 33-35
    sprite('ubl020_02', 3)	# 36-38
    loopRest()
    gotoLabel(0)
