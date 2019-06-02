
@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('es400_00', 2)	# 1-2
    sprite('es400_01', 1)	# 3-3
    sprite('es400_01', 2)	# 4-5
    tag_voice(1, 'bes200_0', 'bes200_1', 'bes200_2', '')
    sprite('es400_04', 3)	# 6-8
    sprite('es400_05', 3)	# 9-11
    sprite('es400_06', 3)	# 12-14
    Unknown14070('ShotA_2nd')
    Unknown14070('ShotB_2nd')
    sprite('es400_07', 3)	# 15-17
    GFX_0('esef_400_zanzou', -1)
    GFX_0('es400_A', -1)
    Unknown38(4, 1)
    sprite('es400_08', 3)	# 18-20
    Unknown14072('ShotA_2nd')
    Unknown14072('ShotB_2nd')
    sprite('es400_09', 3)	# 21-23
    sprite('es400_10', 3)	# 24-26
    sprite('es400_08', 3)	# 27-29
    sprite('es400_09', 3)	# 30-32
    sprite('es400_10', 3)	# 33-35
    Unknown14074('ShotA_2nd')
    Unknown14074('ShotB_2nd')
    sprite('es400_08', 3)	# 36-38
    sprite('es400_11', 3)	# 39-41
    Recovery()
    sprite('es400_12', 3)	# 42-44
