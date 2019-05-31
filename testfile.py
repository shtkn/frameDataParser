
@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('jn213_00', 2)	# 1-2
    sprite('jn213_01', 2)	# 3-4
    sprite('jn213_02', 2)	# 5-6
    Unknown2015(120)
    sprite('jn213_03', 2)	# 7-8
    GFX_0('ModelMagicCircle2', 1)
    Unknown8004(100, 0, 1)
    ScreenShake(0, 5000)
    Unknown23030('6a6e5f64726976655f666c6173680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('jn213_04', 3)	# 9-11
    GFX_0('EffAtk6D', 0)
    Unknown2015(150)
    sprite('jn213_05', 3)	# 12-14
    sprite('jn213_06', 3)	# 15-17
    sprite('jn213_07', 3)	# 18-20
    sprite('jn213_08', 6)	# 21-26
    sprite('jn213_09', 3)	# 27-29	 **attackbox here**
    Unknown2015(120)
    Recovery()
    Unknown2063()
    sprite('jn213_10', 3)	# 30-32
    Unknown2015(-1)
    sprite('jn213_11', 3)	# 33-35
    sprite('jn213_12', 3)	# 36-38
    sprite('jn213_13', 3)	# 39-41
    sprite('jn213_14', 3)	# 42-44
    sprite('jn213_15', 3)	# 45-47
    sprite('jn213_16', 3)	# 48-50
