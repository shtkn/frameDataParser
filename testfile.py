
@Subroutine
def ChainRoot():
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')
    HitJumpCancel(1)

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(170)
        Unknown11092(1)
        Unknown9016(1)
        Hitstop(1)
        Unknown9154(19)
        AirUntechableTime(22)
        Unknown30056('905f01003200000000000000')
        AirPushbackX(22000)
        AirPushbackY(15000)
        Unknown11056(0)
        Unknown11001(-1, -1, -1)
    sprite('Action_045_00', 2)	# 1-2
    sprite('Action_045_01', 2)	# 3-4
    physicsXImpulse(20000)
    Unknown8007(100, 1, 1)
    sprite('Action_403_00', 3)	# 5-7
    sprite('Action_403_01', 3)	# 8-10
    Unknown7009(5)
    sprite('Action_403_02', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade1', 100)
    SFX_3('SE041')
    sprite('Action_403_03', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_04', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade2', 100)
    SFX_3('SE041')
    sprite('Action_403_05', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    Unknown8006(0, 1, 1)
    callSubroutine('ChainRoot')
    sprite('Action_403_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_07', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_08', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    Unknown8006(0, 1, 1)
    GFX_0('Eff66CBlade3', 100)
    SFX_3('SE041')

    def upon_ON_HIT_OR_BLOCK():
        Unknown14070('AN_NmlAtk5A_4th')
    sprite('Action_403_09', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_10', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE041')
    GFX_0('Eff66CBlade4', 100)
    sprite('Action_403_11', 2)	# 29-30	 **attackbox here**
    RefreshMultihit()
    Unknown8006(0, 1, 1)
    sprite('Action_403_12', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade5', 100)
    SFX_3('SE041')
    sprite('Action_403_13', 2)	# 33-34	 **attackbox here**
    RefreshMultihit()

    def upon_ON_HIT_OR_BLOCK():
        Unknown14072('AN_NmlAtk5A_4th')
    sprite('Action_403_14', 4)	# 35-38	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    Unknown14072('AN_NmlAtk5A_4th')
    Unknown1019(50)
    sprite('Action_403_15', 4)	# 39-42	 **attackbox here**
    Unknown14074('AN_NmlAtk5A_4th')
    Unknown1019(50)
    sprite('Action_403_16', 9)	# 43-51
    Unknown8010(0, 1, 1)
    Unknown1019(50)
    sprite('Action_403_16', 6)	# 52-57
    Unknown1019(50)