
def init():
    Move_Register('Assault_Low', 24)

@Subroutine
def Assault_Low_Atk():
    AttackLevel_(4)
    Damage(2000)
    AttackP1(90)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackY(25000)
    AirPushbackX(2000)
    YImpluseBeforeWallbounce(3000)
    AirUntechableTime(60)
    HitLow(2)
    Unknown9016(1)
    Unknown11058('0000000000000000010000000000000000000000')

    def upon_12():
        clearUponHandler(12)
        Hitstop(20)
        ScreenShake(5000, 3000)

@State
def Assault_Low():
    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Low_Atk')

    sprite('jb403_13', 2)  # 1-2
    Unknown1045(30000)
    Unknown8007(100, 1, 0)
    sprite('jb403_14', 2)  # 3-4
    sprite('jb403_01', 2)  # 5-6
    sprite('jb403_02', 2)  # 7-8
    sprite('jb403_03', 2)  # 9-10
    Unknown1051(50)
    Unknown8006(100, 1, 0)
    SFX_3('jbse_03')
    SFX_0('010_swing_sword_2')
    sprite('jb403_04', 2)  # 11-12
    Unknown7007(
        '626a623230345f30000000000000000064000000626a623230345f31000000000000000064000000626a623230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('jb403_05', 2)  # 13-14	 **attackbox here**
    Unknown1084(1)
    GFX_0('jbef403_zanzou', 100)
    GFX_0('jbef403_zanzou2', 100)
    sprite('jb403_06', 2)  # 15-16
    Recovery()
    Unknown2063()
    sprite('jb403_07', 4)  # 17-20
    sprite('jb403_08', 3)  # 21-23
    sprite('jb403_09', 3)  # 24-26
    sprite('jb403_10', 3)  # 27-29
    sprite('jb403_11', 3)  # 30-32
    sprite('jb403_12', 3)  # 33-35
