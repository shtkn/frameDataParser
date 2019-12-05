@Subroutine
def SembalnceCheck():
    if (not SLOT_5):
        if (not SLOT_8):
            Unknown13(25)

@State
def AuraFireMaster():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)

        def upon_CLEAR_OR_EXIT():
            if (not SLOT_7):
                Unknown13(25)
    label(0)
    sprite('null', 4)	# 1-4
    GFX_0('AuraFireEff', 103)
    gotoLabel(0)

@State
def AuraFireEff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-25000)
        Unknown1007(255000)
        if Unknown68('0100000000000000000000000000000000000000'):
            Unknown1007(-98000)
            teleportRelativeX(-12000)
        Unknown1010(-25000, 25000)
        Unknown1011(-25000, 25000)
    sprite('null', 5)	# 1-5
    GFX_2('rynef_HairFire')
    sprite('null', 60)	# 6-65
    Unknown4007(0)

@State
def AddAtkFire():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown3038(1)
        Unknown10001(3)
        Unknown23182(3)
        Unknown10000(50)
        ProjectileDurabilityLvl(1)
        Unknown9266(1)
        ChipDamagePct(5)
        Unknown9219(1)
        Unknown23078(1)

        def upon_43():
            callSubroutine('SembalnceCheck')
            if (SLOT_48 == 9901):
                Unknown1096(500)
                Unknown1072(-50000)
            if (SLOT_48 == 9902):
                Unknown1096(500)
                Unknown1072(0)
            if (SLOT_48 == 9903):
                Unknown1096(550)
                Unknown1072(10000)
            if (SLOT_48 == 9904):
                Unknown1096(600)
                Unknown1072(-90000)
            if (SLOT_48 == 9905):
                Unknown1096(400)
                Unknown1072(30000)
            if (SLOT_48 == 9906):
                Unknown1096(600)
                Unknown1072(-85000)
                teleportRelativeX(20000)
                Unknown1007(80000)
            if (SLOT_48 == 9907):
                Unknown1096(400)
                Unknown1072(20000)
            if (SLOT_48 == 9908):
                Unknown1096(500)
                Unknown1072(60000)
    sprite('null', 2)	# 1-2
    GFX_0('rynef_Muzzle_Sembalnce', -1)
    Unknown1099(15)
    sprite('vref_ryn_blowaddatk', 3)	# 3-5	 **attackbox here**
    SFX_3('rynse_03')
    Unknown11108('03000000')
    sprite('null', 16)	# 6-21

@State
def AddAtkFireSpecial():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown3038(1)
        AttackP1(60)
        AttackP2(100)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        Unknown9266(1)
        ChipDamagePct(10)
        Unknown9219(1)
        Unknown23078(1)

        def upon_43():
            callSubroutine('SembalnceCheck')
            if (SLOT_48 == 9909):
                AttackLevel_(5)
                Damage(1100)
                Unknown1096(750)
                AirPushbackY(35000)
                AirUntechableTime(60)
                Unknown1072(-90000)
                teleportRelativeX(80000)
            if (SLOT_48 == 9910):
                AttackLevel_(5)
                Damage(750)
                AirPushbackY(25000)
                Unknown1096(750)
                AirUntechableTime(30)
                Unknown1072(-90000)
            if (SLOT_48 == 9911):
                Unknown1096(300)
                AttackLevel_(3)
                Damage(150)
                Hitstop(2)
                AirPushbackX(-2500)
                AirPushbackY(2000)
                PushbackX(2000)
                AirUntechableTime(35)
            if (SLOT_48 == 9912):
                Unknown1096(300)
                AttackLevel_(3)
                Damage(150)
                Hitstop(2)
                AirPushbackX(15000)
                AirPushbackY(15000)
                PushbackX(2000)
                GroundedHitstunAnimation(2)
                Unknown9130(28)
                Unknown9142(23)
                AirUntechableTime(35)
            if (SLOT_48 == 9913):
                AttackLevel_(5)
                Damage(350)
                GroundedHitstunAnimation(9)
                Hitstop(12)
                AirPushbackX(50000)
                AirPushbackY(15000)
                AirUntechableTime(35)
                Unknown9178(1)
                WallbounceReboundTime(5)
                AirHitstunAfterWallbounce(40)
                Unknown1096(750)
            if (SLOT_48 == 9914):
                Damage(1500)
                AirUntechableTime(60)
                AirPushbackX(5000)
                AirPushbackY(38000)
                Unknown11099(1)
                Unknown11044(1)
                AttackLevel_(5)
                Unknown1096(1000)
                Unknown1072(-90000)
            if (SLOT_48 == 9915):
                Damage(300)
                AirUntechableTime(60)
                Hitstop(2)
                AirPushbackX(3500)
                AirPushbackY(500)
                Unknown11044(1)
                Unknown11069('AssaultCExe')
                AttackLevel_(2)
                Unknown1096(250)
                Unknown1072(-45000)
            if (SLOT_48 == 9916):
                Damage(300)
                AirUntechableTime(60)
                Hitstop(12)
                AirPushbackX(3500)
                AirPushbackY(30000)
                Unknown11044(1)
                Unknown11069('AssaultCExe')
                AttackLevel_(5)
                Unknown1096(500)
                Unknown1072(-90000)
            if (SLOT_48 == 9917):
                Damage(500)
                GroundedHitstunAnimation(9)
                AirPushbackX(60000)
                AirPushbackY(15000)
                Unknown9178(1)
                WallbounceReboundTime(0)
                AirHitstunAfterWallbounce(40)
                Unknown11044(1)
                AttackLevel_(5)
                Unknown1096(1000)
    sprite('null', 2)	# 1-2
    GFX_0('rynef_Muzzle_Sembalnce', -1)
    Unknown1099(15)
    sprite('vref_ryn_blowaddatk', 3)	# 3-5	 **attackbox here**
    SFX_3('rynse_02')
    Unknown11108('03000000')
    sprite('null', 13)	# 6-18

@State
def AddAtkFireUltimate():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown3038(1)
        Damage(100)
        AttackP1(50)
        AttackP2(100)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        Unknown9266(1)
        ChipDamagePct(10)
        MinimumDamagePct(10)
        Unknown11068(1)
        Unknown9219(1)
        Unknown23078(1)

        def upon_43():
            callSubroutine('SembalnceCheck')
            if (SLOT_48 == 9918):
                Damage(1000)
                Hitstop(20)
                MinimumDamagePct(20)
                GroundedHitstunAnimation(9)
                Unknown11056(0)
                AirUntechableTime(60)
                AirPushbackX(60000)
                AirPushbackY(35000)
                AttackLevel_(5)
                Unknown1096(1000)
            if (SLOT_48 == 9919):
                AttackLevel_(4)
                Unknown1096(500)
                PushbackX(1800)
                Unknown11032('40420f006079feffffffffffffffffff')
                teleportRelativeX(90000)
                Unknown1007(30000)
            if (SLOT_48 == 9920):
                AttackLevel_(4)
                Unknown1096(500)
                PushbackX(1800)
                Hitstop(9)
                Unknown11032('40420f006079feffffffffffffffffff')
                teleportRelativeX(90000)
                Unknown1007(30000)
            if (SLOT_48 == 9921):
                AttackLevel_(4)
                Unknown1096(500)
                PushbackX(1800)
                Hitstop(6)
                Unknown11032('40420f006079feffffffffffffffffff')
                teleportRelativeX(90000)
                Unknown1007(30000)
            if (SLOT_48 == 9922):
                AttackLevel_(4)
                Unknown1096(500)
                PushbackX(1800)
                Hitstop(3)
                Unknown11032('40420f006079feffffffffffffffffff')
                teleportRelativeX(90000)
                Unknown1007(30000)
            if (SLOT_48 == 9923):
                AttackLevel_(4)
                Unknown1096(500)
                PushbackX(1800)
                Hitstop(2)
                Unknown11032('40420f006079feffffffffffffffffff')
                teleportRelativeX(90000)
                Unknown1007(30000)
            if (SLOT_48 == 9924):
                AttackLevel_(4)
                Unknown1096(500)
                PushbackX(1800)
                Hitstop(1)
                Unknown11032('40420f006079feffffffffffffffffff')
                teleportRelativeX(90000)
                Unknown1007(30000)
            if (SLOT_48 == 9925):
                AttackLevel_(5)
                Unknown1096(500)
                Hitstop(11)
                Unknown9215()
                AirHitstunAnimation(2)
                GroundedHitstunAnimation(2)
                Unknown9130(35)
                Unknown9142(25)
                Unknown11032('40420f006079feffffffffffffffffff')
                teleportRelativeX(90000)
                Unknown1007(30000)
            if (SLOT_48 == 9926):
                AttackLevel_(5)
                Damage(1000)
                Unknown1096(500)
                Hitstop(12)
                GroundedHitstunAnimation(9)
                AirUntechableTime(60)
                AirPushbackY(45000)
            if (SLOT_48 == 9928):
                AttackLevel_(5)
                Damage(500)
                Hitstop(13)
                AirUntechableTime(60)
                AirPushbackX(10000)
                AirPushbackY(-40000)
                Unknown9190(1)
                Unknown9118(25)
                Unknown9310(10)
                Unknown1096(1000)
    sprite('null', 2)	# 1-2
    GFX_0('rynef_Muzzle_Sembalnce', -1)
    Unknown1099(15)
    sprite('vref_ryn_blowaddatk', 3)	# 3-5	 **attackbox here**
    SFX_3('rynse_03')
    Unknown11108('03000000')
    sprite('null', 13)	# 6-18

@State
def rynef_Muzzle_Sembalnce():

    def upon_IMMEDIATE():
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown23015(6)
        Unknown4013(2)
        Unknown4007(3)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        callSubroutine('SembalnceCheck')
    sprite('null', 2)	# 1-2
    sprite('vref_ryn_muzzleEX01', 2)	# 3-4
    GFX_2('rynef_sembalnce')
    Unknown4009(3)
    sprite('vref_ryn_muzzleEX02', 2)	# 5-6
    sprite('vref_ryn_muzzleEX03', 2)	# 7-8
    sprite('vref_ryn_muzzleEX04', 2)	# 9-10
    Unknown4007(0)
    sprite('vref_ryn_muzzleEX05', 2)	# 11-12
    sprite('vref_ryn_muzzleEX06', 2)	# 13-14
    sprite('null', 20)	# 15-34

@State
def LandShotObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4061(1)
        AttackLevel_(3)
        GroundedHitstunAnimation(9)
        AirUntechableTime(27)
        AirPushbackX(15000)
        AirPushbackY(15000)
        Unknown9021(1)
        Unknown9266(1)
        teleportRelativeX(150000)
        Unknown1007(250000)
        Unknown1096(500)
        Hitstop(6)
        Unknown11001(5, 5, 7)

        def upon_43():
            if (SLOT_48 == 4001):
                Unknown30070('4c616e6453686f7441746b4f626a410000000000000000000000000000000000')
                physicsXImpulse(45000)
                physicsYImpulse(-25000)
                Unknown1073(30000)
            if (SLOT_48 == 4002):
                Unknown30070('4c616e6453686f7441746b4f626a420000000000000000000000000000000000')
                physicsXImpulse(50000)
                physicsYImpulse(-15000)
                Unknown1073(17000)
            if (SLOT_48 == 4003):
                Unknown30070('4c616e6453686f7441746b4f626a430000000000000000000000000000000000')
                Unknown2037(1)
                Hitstop(0)
                MinimumDamagePct(10)
                Unknown30065(0)
                physicsXImpulse(50000)
                physicsYImpulse(-15000)
                Unknown1073(17000)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(2)
            clearUponHandler(10)
            Unknown21012('72796e65663430305f42756c6c6574000000000000000000000000000000000020000000')
            Unknown21012('72796e65663430305f547261696c00000000000000000000000000000000000020000000')
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            clearUponHandler(10)
            Unknown21012('72796e65663430305f42756c6c6574000000000000000000000000000000000020000000')
            Unknown21012('72796e65663430305f547261696c00000000000000000000000000000000000020000000')
            sendToLabel(2)
    sprite('vref_ryn_addatk', 32767)	# 1-32767	 **attackbox here**
    Unknown3038(1)
    GFX_0('rynef400_Bullet', -1)
    GFX_0('rynef400_Trail', -1)
    label(1)
    sprite('null', 10)	# 32768-32777
    if SLOT_2:
        GFX_0('ShotHitAtkObj', -1)
    ExitState()
    label(2)
    sprite('null', 10)	# 32778-32787
    GFX_0('LandingAtkObj', -1)
    if SLOT_2:
        Unknown36(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown35()
    ExitState()

@State
def AirShotObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4061(1)
        AttackLevel_(3)
        GroundedHitstunAnimation(9)
        AirUntechableTime(27)
        AirPushbackX(15000)
        AirPushbackY(15000)
        Unknown9021(1)
        Unknown9266(1)
        teleportRelativeX(125000)
        Unknown1007(250000)
        Unknown1096(500)
        Hitstop(0)
        Unknown11001(3, 3, 3)

        def upon_43():
            if (SLOT_48 == 4011):
                Unknown30070('41697253686f7441746b4f626a41000000000000000000000000000000000000')
                physicsXImpulse(25000)
                physicsYImpulse(-25000)
                Unknown1072(46000)
            if (SLOT_48 == 4012):
                Unknown30070('41697253686f7441746b4f626a42000000000000000000000000000000000000')
                physicsXImpulse(35000)
                physicsYImpulse(-25000)
                Unknown1072(37000)
            if (SLOT_48 == 4013):
                Unknown30070('41697253686f7441746b4f626a43000000000000000000000000000000000000')
                Unknown2037(1)
                Hitstop(0)
                MinimumDamagePct(10)
                Unknown30065(0)
                physicsXImpulse(40000)
                physicsYImpulse(-25000)
                Unknown1072(34000)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(2)
            clearUponHandler(10)
            sendToLabel(1)
            Unknown21012('72796e65663430305f42756c6c65745f4169720000000000000000000000000020000000')
            Unknown21012('72796e65663430305f547261696c00000000000000000000000000000000000020000000')

        def upon_LANDING():
            clearUponHandler(2)
            clearUponHandler(10)
            sendToLabel(2)
            Unknown21012('72796e65663430305f42756c6c65745f4169720000000000000000000000000020000000')
            Unknown21012('72796e65663430305f547261696c00000000000000000000000000000000000020000000')
    sprite('vref_ryn_addatk', 32767)	# 1-32767	 **attackbox here**
    Unknown3038(1)
    GFX_0('rynef400_Bullet_Air', -1)
    GFX_0('rynef400_Trail', -1)
    label(1)
    sprite('null', 10)	# 32768-32777
    if SLOT_2:
        GFX_0('ShotHitAtkObj', -1)
    ExitState()
    label(2)
    sprite('null', 10)	# 32778-32787
    GFX_0('LandingAtkObj', -1)
    if SLOT_2:
        Unknown36(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown35()
    ExitState()

@State
def ShotHitAtkObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4061(1)
        AttackLevel_(4)
        Unknown9021(1)
        Unknown9266(1)
        GroundedHitstunAnimation(10)
        AirPushbackX(15000)
        AirPushbackY(15000)
        AirUntechableTime(35)
        Hitstop(0)
        Unknown11001(4, 4, 9)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown1096(500)
    sprite('null', 4)	# 1-4
    Unknown1099(25)
    GFX_0('rynef400_Bomb', -1)
    Unknown3038(1)
    SFX_3('rynse_09')
    sprite('vref_ryn_addatk', 8)	# 5-12	 **attackbox here**
    sprite('null', 4)	# 13-16
    sprite('null', 4)	# 17-20
    Unknown3004(-63)

@State
def LandingAtkObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4061(1)
        AttackLevel_(4)
        Unknown9021(1)
        Unknown9266(1)
        GroundedHitstunAnimation(10)
        AirPushbackX(15000)
        AirPushbackY(15000)
        AirUntechableTime(35)
        Hitstop(0)
        Unknown11001(4, 4, 9)
        Unknown1007(50000)
        Unknown1096(500)
    sprite('null', 4)	# 1-4
    ScreenShake(0, 10000)
    Unknown1099(15)
    GFX_0('rynef400_Bomb_Ground', -1)
    Unknown3038(1)
    SFX_3('rynse_09')
    sprite('vref_ryn_addatk', 12)	# 5-16	 **attackbox here**

@State
def rynef400_Bullet():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('rynef400_Shot')
        Unknown1096(700)
        teleportRelativeX(-11000)
        Unknown1007(-3000)

        def upon_32():
            sendToLabel(0)
            Unknown4007(0)
            Unknown4010(0)
            GFX_1('rynef400_Shot_Delete', -1)
    sprite('null', 60)	# 1-60
    GFX_1('rynef_Muzzle_Add', -1)
    SFX_3('rynse_08')
    label(0)
    sprite('null', 4)	# 61-64
    Unknown1099(-175)

@State
def rynef400_Bullet_Air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('rynef400_Shot')
        Unknown1096(700)
        teleportRelativeX(-11000)
        Unknown1007(9000)

        def upon_32():
            sendToLabel(0)
            Unknown4007(0)
            Unknown4010(0)
            GFX_1('rynef400_Shot_Delete', -1)
    sprite('null', 60)	# 1-60
    GFX_1('rynef_Muzzle_Add', -1)
    SFX_3('rynse_08')
    label(0)
    sprite('null', 4)	# 61-64
    Unknown1099(-175)

@State
def rynef400_Trail():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4006(2)
        Unknown3033()
        Unknown4003('72796e65663430305f747261696c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1056(500)
        Unknown1064(0)
        Unknown1073(-90000)
        sendToLabelUpon(32, 0)
    sprite('null', 10)	# 1-10
    Unknown1067(400)
    sprite('null', 60)	# 11-70
    Unknown1067(0)
    label(0)
    sprite('null', 3)	# 71-73
    Unknown4007(0)
    Unknown1067(-700)
    Unknown3004(-64)

@State
def rynef400_Muzzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(130000)
        Unknown1007(260000)
        Unknown1096(800)
        Unknown1099(10)
    sprite('null', 45)	# 1-45
    GFX_0('rynef_Muzzle', -1)

@State
def rynef401_Muzzle():

    def upon_IMMEDIATE():
        Unknown4009(2)
        teleportRelativeX(130000)
        Unknown1007(260000)
        Unknown1096(800)
        Unknown1099(10)
    sprite('null', 45)	# 1-45
    GFX_0('rynef_Muzzle', -1)

@State
def rynef400_Bomb():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown1099(25)
        Unknown1096(1100)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown23015(6)
        Unknown1077(0, 360000)
    sprite('vref_ryn400_bombB00', 4)	# 1-4
    sprite('vref_ryn400_bombB01', 3)	# 5-7
    Unknown4054(6)
    Unknown4045('72796e65663430305f426f6d625f466972650000000000000000000000000000ffffffff')
    sprite('vref_ryn400_bombB02', 3)	# 8-10
    sprite('vref_ryn400_bombB03', 3)	# 11-13
    sprite('vref_ryn400_bombB04', 2)	# 14-15
    Unknown3022(-54)
    Unknown3016(-38)
    sprite('vref_ryn400_bombB05', 2)	# 16-17
    sprite('vref_ryn400_bombB06', 2)	# 18-19
    sprite('vref_ryn400_bombB07', 2)	# 20-21

@State
def rynef400_Bomb_Ground():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown1099(15)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown1064(800)
        Unknown1000(10000)
        teleportRelativeY(-60000)
        Unknown23015(6)
        Unknown2005()
    sprite('vref_ryn400_bomb00', 2)	# 1-2
    sprite('vref_ryn400_bomb01', 2)	# 3-4
    Unknown4054(6)
    Unknown4045('72796e65663430305f426f6d625f53746f6e6500000000000000000000000000ffffffff')
    sprite('vref_ryn400_bomb02', 3)	# 5-7
    sprite('vref_ryn400_bomb03', 2)	# 8-9
    sprite('vref_ryn400_bomb04', 2)	# 10-11
    Unknown3022(-54)
    Unknown3016(-38)
    sprite('vref_ryn400_bomb05', 2)	# 12-13
    sprite('vref_ryn400_bomb06', 2)	# 14-15
    sprite('vref_ryn400_bomb07', 2)	# 16-17

@State
def rynef400_Flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        GFX_2('rynef400_Flare')
        Unknown1096(100)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1000(-120000)
    teleportRelativeY(232000)
    Unknown1099(80)
    sprite('null', 20)	# 4-23
    Unknown1099(10)
    label(0)
    sprite('null', 3)	# 24-26
    Unknown1000(34000)
    teleportRelativeY(210000)
    Unknown1099(10)

@State
def rynef401_Flare():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        GFX_2('rynef400_Flare')
        Unknown1096(100)
        sendToLabelUpon(32, 0)
    sprite('null', 3)	# 1-3
    Unknown1000(-55000)
    teleportRelativeY(290000)
    Unknown1099(160)
    sprite('null', 20)	# 4-23
    Unknown1099(10)
    label(0)
    sprite('null', 3)	# 24-26
    Unknown1000(110000)
    teleportRelativeY(240000)
    Unknown1099(10)

@State
def rynef_Muzzle():

    def upon_IMMEDIATE():
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown4013(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown23015(6)
    sprite('vref_ryn_muzzle00', 2)	# 1-2
    GFX_2('rynef_MuzzleFlash')
    sprite('vref_ryn_muzzle01', 2)	# 3-4
    sprite('vref_ryn_muzzle02', 2)	# 5-6
    sprite('vref_ryn_muzzle03', 2)	# 7-8
    sprite('vref_ryn_muzzle04', 2)	# 9-10
    sprite('vref_ryn_muzzle05', 2)	# 11-12
    sprite('vref_ryn_muzzle06', 2)	# 13-14
    sprite('null', 20)	# 15-34

@State
def rynef_OD_Begin():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeY(200000)
    sprite('null', 1)	# 1-1
    GFX_1('rynef_OD_aura', -1)
    GFX_0('rynef_OD_Begin_Shockwave', -1)

@State
def rynef_OD_Begin_Shockwave():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1000(20000)
        teleportRelativeY(302000)
    sprite('null', 1)	# 1-1
    GFX_1('rynef_OD_shockwave', -1)

@State
def rynef_EXHIT_A():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    GFX_0('rynef_EXHIT_A01', -1)
    GFX_0('rynef_EXHIT_A02', -1)
    GFX_0('rynef_EXHIT_A03', -1)
    GFX_0('rynef_EXHIT_A04', -1)
    GFX_1('rynef_EXHit', -1)

@Subroutine
def rynef_EXHIT_A_Func():
    Unknown4007(2)
    Unknown4006(2)
    Unknown3000(0)
    Unknown4061(4)
    Unknown1102(-100, 100)
    Unknown1077(-15000, 15000)
    Unknown1061(80)
    Unknown23015(6)
    Unknown3032()

@State
def rynef_EXHIT_A01():

    def upon_IMMEDIATE():
        Unknown1096(1500)
        Unknown1090(300)
        Unknown1099(125)
        Unknown1093(300)
        Unknown1073(210000)
        callSubroutine('rynef_EXHIT_A_Func')
        Unknown23015(15)
        GFX_0('rynef_EXHIT_A_BloomB', -1)
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 2-2
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1101(50)
    sprite('null', 2)	# 9-10
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef_EXHIT_A02():

    def upon_IMMEDIATE():
        Unknown1096(1500)
        Unknown1090(-300)
        Unknown1099(125)
        Unknown1093(-300)
        Unknown1073(30000)
        callSubroutine('rynef_EXHIT_A_Func')
        GFX_0('rynef_EXHIT_A_Bloom', -1)
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 2-2
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1101(50)
    sprite('null', 2)	# 9-10
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef_EXHIT_A03():

    def upon_IMMEDIATE():
        Unknown1096(1000)
        Unknown1090(300)
        Unknown1099(125)
        Unknown1093(300)
        Unknown1073(-30000)
        callSubroutine('rynef_EXHIT_A_Func')
        Unknown23015(15)
        GFX_0('rynef_EXHIT_A_BloomB', -1)
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 2-2
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1101(50)
    sprite('null', 2)	# 9-10
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef_EXHIT_A04():

    def upon_IMMEDIATE():
        Unknown1096(1000)
        Unknown1090(-300)
        Unknown1099(125)
        Unknown1093(-300)
        Unknown1073(150000)
        callSubroutine('rynef_EXHIT_A_Func')
        GFX_0('rynef_EXHIT_A_Bloom', -1)
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 2-2
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1101(50)
    sprite('null', 2)	# 9-10
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef_EXHIT_A_Bloom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown3033()
        Unknown3000(0)
        Unknown4061(4)
        Unknown23015(6)
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f6869743030622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 2-2
    Unknown4003('72796e65663433305f6869743031622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72796e65663433305f6869743032622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72796e65663433305f6869743033622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown4003('72796e65663433305f6869743034622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 9-10
    Unknown4003('72796e65663433305f6869743035622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown4003('72796e65663433305f6869743036622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72796e65663433305f6869743037622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef_EXHIT_A_BloomB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown3033()
        Unknown3000(0)
        Unknown4061(4)
        Unknown23015(15)
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f6869743030622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 2-2
    Unknown4003('72796e65663433305f6869743031622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72796e65663433305f6869743032622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72796e65663433305f6869743033622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown4003('72796e65663433305f6869743034622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 9-10
    Unknown4003('72796e65663433305f6869743035622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown4003('72796e65663433305f6869743036622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72796e65663433305f6869743037622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef_EXHIT_B():

    def upon_IMMEDIATE():
        Unknown1073(-10000)
    sprite('null', 1)	# 1-1
    GFX_0('rynef_EXHIT_B01', -1)
    GFX_0('rynef_EXHIT_B02', -1)
    GFX_0('rynef_EXHIT_B03', -1)
    GFX_0('rynef_EXHIT_B04', -1)

@Subroutine
def rynef_EXHIT_B_Func():
    Unknown4007(2)
    Unknown4006(2)
    Unknown3032()
    Unknown23015(6)
    Unknown1056(3200)
    Unknown1064(4400)
    Unknown1077(10000, -10000)
    Unknown4003('72796e65665f6c696e65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('rynef_EXHIT_B_Bloom', -1)

@State
def rynef_EXHIT_B01():

    def upon_IMMEDIATE():
        callSubroutine('rynef_EXHIT_B_Func')
        Unknown1073(60000)
    sprite('null', 12)	# 1-12

@State
def rynef_EXHIT_B02():

    def upon_IMMEDIATE():
        callSubroutine('rynef_EXHIT_B_Func')
        Unknown1073(120000)
    sprite('null', 12)	# 1-12

@State
def rynef_EXHIT_B03():

    def upon_IMMEDIATE():
        callSubroutine('rynef_EXHIT_B_Func')
        Unknown1073(-60000)
    sprite('null', 12)	# 1-12

@State
def rynef_EXHIT_B04():

    def upon_IMMEDIATE():
        callSubroutine('rynef_EXHIT_B_Func')
        Unknown1073(-120000)
    sprite('null', 12)	# 1-12

@State
def rynef_EXHIT_B_Bloom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown3032()
        Unknown23015(6)
        Unknown4003('72796e65665f6c696e65303062000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 12)	# 1-12

@State
def rynef_EXHIT_C():

    def upon_IMMEDIATE():
        Unknown4003('72796e65665f636972636c6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown1077(200000, 140000)
        Unknown3032()
        Unknown23015(6)
        Unknown1096(1000)
        Unknown1058(35)
        Unknown1058(150)
        GFX_0('rynef_EXHIT_C_Bloom', -1)
    sprite('null', 5)	# 1-5
    Unknown1099(240)
    Unknown1061(35)
    Unknown1093(150)
    sprite('null', 5)	# 6-10
    Unknown1101(60)
    sprite('null', 5)	# 11-15
    Unknown1101(60)
    Unknown3004(-40)

@State
def rynef_EXHIT_C_Bloom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown4025(2)
        Unknown3033()
        Unknown23015(6)
        Unknown4003('72796e65665f636972636c653030622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 15)	# 1-15

@State
def rynef201():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(3)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4061(0)
        Unknown3032()
        teleportRelativeY(242000)
        Unknown1000(120000)
        Unknown13044(1)
    sprite('vref_ryn201_00', 3)	# 1-3
    sprite('vref_ryn201_01', 2)	# 4-5
    sprite('vref_ryn201_02', 2)	# 6-7
    sprite('vref_ryn201_03', 2)	# 8-9

@State
def rynef203_FistAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(2)
        GFX_2('rynef203_FistAura')
    sprite('null', 3)	# 1-3
    Unknown1072(-45000)
    sprite('null', 32767)	# 4-32770
    Unknown1072(-30000)
    teleportRelativeX(30000)
    Unknown1007(-5000)

@State
def rynef203_Fall():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(2)
        GFX_2('rynef203_Fall')
    sprite('null', 4)	# 1-4
    Unknown1059(25)
    Unknown1067(1000)
    sprite('null', 2)	# 5-6
    Unknown1059(0)
    Unknown1067(0)
    label(0)
    sprite('null', 2)	# 7-8
    gotoLabel(0)

@State
def rynef203_ShockWave():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown1000(50000)
    sprite('vref_ryn203_burst00', 1)	# 1-1
    GFX_1('rynef203_Fire', -1)
    Unknown1099(8)
    SFX_3('rynse_06')
    sprite('vref_ryn203_burst00', 2)	# 2-3
    Unknown4007(0)
    sprite('vref_ryn203_burst01', 3)	# 4-6
    sprite('vref_ryn203_burst02', 2)	# 7-8
    sprite('vref_ryn203_burst03', 2)	# 9-10
    sprite('vref_ryn203_burst04', 2)	# 11-12
    sprite('vref_ryn203_burst05', 2)	# 13-14
    sprite('vref_ryn203_burst06', 2)	# 15-16

@State
def rynef203_LandParticle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown1000(20000)
        teleportRelativeY(-10000)
    sprite('null', 1)	# 1-1
    GFX_1('rynef203_LandImpact', -1)
    SFX_0('213_bound_1')
    sprite('null', 15)	# 2-16
    Unknown4007(0)

@State
def rynef2B():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(3)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4061(0)
        Unknown3032()
        teleportRelativeY(242000)
        Unknown1000(70000)
        Unknown13044(1)
    sprite('vref_ryn431B_00', 3)	# 1-3
    sprite('vref_ryn431B_01', 2)	# 4-5
    sprite('vref_ryn431B_02', 2)	# 6-7
    Unknown1007(10000)
    sprite('vref_ryn431B_03', 2)	# 8-9
    sprite('vref_ryn431B_04', 2)	# 10-11
    sprite('vref_ryn431B_05', 2)	# 12-13

@State
def rynef271():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown1096(3700)
        teleportRelativeX(-35000)
        Unknown1007(202000)
        Unknown3001(180)
    sprite('null', 3)	# 1-3
    Unknown4003('72796e65663237315f77696e6430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 12)	# 4-15
    Unknown4003('72796e65663237315f77696e6430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef272():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown1096(3500)
        teleportRelativeX(-60000)
        Unknown1007(152000)
        Unknown3001(180)
        Unknown1072(10000)
    sprite('null', 2)	# 1-2
    Unknown4003('72796e65663237325f77696e6430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 12)	# 3-14
    Unknown4003('72796e65663237325f77696e6430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef272_Muzzle():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
        Unknown1007(270000)
        Unknown1096(700)
        Unknown1099(10)
    sprite('null', 30)	# 1-30
    GFX_0('rynef_Muzzle', -1)
    SFX_3('rynse_02')

@State
def rynef320():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 3)	# 1-3
    GFX_0('rynef320_Bake', -1)
    GFX_0('rynef320_Particle', -1)
    sprite('null', 40)	# 4-43
    Unknown4007(0)
    GFX_0('rynef320_Distortion', -1)

@State
def rynef320_Bake():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(30000)
        Unknown1007(260000)
        Unknown1096(2200)
        Unknown1072(5000)
        Unknown3019(180)
        Unknown1067(40)
        physicsYImpulse(-2000)
        Unknown3033()
    sprite('null', 3)	# 1-3
    Unknown4003('72796e65663332305f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4003('72796e65663332305f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 12)	# 7-18
    Unknown3022(-20)

@State
def rynef320_Particle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        teleportRelativeX(40000)
        Unknown1007(50000)
        Unknown1072(-3000)
    sprite('vref_ryn320EX', 40)	# 1-40
    GFX_0('rynef320_Fire', 0)
    GFX_0('rynef320_Fire', 1)
    GFX_0('rynef320_Fire', 2)
    GFX_0('rynef320_Fire', 3)

@State
def rynef320_Fire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown1096(1100)
    sprite('null', 18)	# 1-18
    GFX_2('rynef_bake_fireA')
    sprite('null', 22)	# 19-40

@State
def rynef320_Distortion():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(90000)
        Unknown1007(280000)
        Unknown1096(1300)
        Unknown1072(5000)
    sprite('vref_ryn320_distortion', 10)	# 1-10
    Unknown3057(1)
    Unknown3058(20000)
    Unknown3059(-2000)

@State
def rynef_6Assist_Speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1000(140000)
        teleportRelativeY(210000)
        Unknown2055(30)
    label(0)
    sprite('null', 2)	# 1-2
    GFX_1('rynef402_Speed_Assist', -1)
    gotoLabel(0)

@State
def rynef402():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 30)	# 1-30
    GFX_0('rynef402_Trail', -1)
    GFX_0('rynef402_Aura', -1)
    GFX_0('rynef402_Distortion', -1)
    GFX_0('rynef402_Speed', -1)
    GFX_0('rynef402_Muzzle', -1)
    SFX_3('rynse_02')
    SFX_3('rynse_04')

@State
def rynef402_Muzzle():

    def upon_IMMEDIATE():
        teleportRelativeX(-150000)
        Unknown1007(230000)
        Unknown1096(1000)
        Unknown1099(10)
        Unknown2005()
    sprite('null', 30)	# 1-30
    GFX_0('rynef_Muzzle', -1)

@State
def rynef402_Trail():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        GFX_0('rynef402_Trail00', -1)
        GFX_0('rynef402_Trail02', -1)
        GFX_0('rynef402_Trail01', -1)
        Unknown1056(500)
        Unknown1064(2500)
        Unknown1000(-30000)
        teleportRelativeY(162000)

        def upon_STATE_END():
            Unknown1096(0)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)	# 1-10
    Unknown1059(300)
    label(0)
    sprite('null', 20)	# 11-30
    Unknown1059(0)
    physicsXImpulse(0)
    label(1)
    sprite('null', 3)	# 31-33
    Unknown1059(0)

    def upon_CLEAR_OR_EXIT():
        Unknown1058(80)
    physicsXImpulse(15000)
    sprite('null', 3)	# 34-36
    Unknown3004(-64)

@State
def rynef402_Trail00():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663430325f747261696c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown4061(5)
        Unknown21004(1)
        Unknown3003(80)
    sprite('null', 32767)	# 1-32767

@State
def rynef402_Trail01():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663430325f747261696c622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown4061(5)
        Unknown21004(3)
    sprite('null', 32767)	# 1-32767

@State
def rynef402_Trail02():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663430325f747261696c30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown4061(5)
        Unknown21004(2)
        Unknown3003(80)
    sprite('null', 32767)	# 1-32767

@State
def rynef402_Distortion():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3057(1)
        Unknown1056(0)
        Unknown1064(1200)
        teleportRelativeY(170000)
        Unknown1000(-170000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('vref_ryn402_distortion', 60)	# 1-60
    Unknown1059(300)
    Unknown3058(10000)
    label(0)
    sprite('keep', 60)	# 61-120
    Unknown1059(0)
    label(1)
    sprite('keep', 9)	# 121-129
    Unknown1059(0)
    Unknown3059(-1111)

@State
def rynef402_Aura():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663430325f6175726130302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown1056(2400)
        Unknown1064(4600)
        Unknown1000(140000)
        teleportRelativeY(170000)
        Unknown3001(100)
        sendToLabelUpon(33, 1)
    sprite('null', 3)	# 1-3
    Unknown1059(1500)
    sprite('null', 30)	# 4-33
    Unknown1059(100)
    label(1)
    sprite('null', 6)	# 34-39
    Unknown1059(100)
    Unknown3004(-16)
    Unknown1067(-50)

@State
def rynef402_Speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1000(140000)
        teleportRelativeY(210000)
        sendToLabelUpon(32, 1)

        def upon_33():
            Unknown14()
    label(0)
    sprite('null', 2)	# 1-2
    GFX_1('rynef402_speed', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 2)	# 3-4
    GFX_1('rynef402_speed01', -1)
    gotoLabel(1)

@State
def rynef402_Singal01():

    def upon_IMMEDIATE():
        Unknown21012('72796e65663430325f547261696c00000000000000000000000000000000000020000000')
        Unknown21012('72796e65663430325f446973746f7274696f6e0000000000000000000000000020000000')
        Unknown21012('72796e65663430325f537065656400000000000000000000000000000000000020000000')
    sprite('null', 1)	# 1-1

@State
def rynef402_Singal02():

    def upon_IMMEDIATE():
        Unknown21012('72796e65663430325f547261696c00000000000000000000000000000000000021000000')
        Unknown21012('72796e65663430325f446973746f7274696f6e0000000000000000000000000021000000')
        Unknown21012('72796e65663430325f417572610000000000000000000000000000000000000021000000')
        Unknown21012('72796e65663430325f537065656400000000000000000000000000000000000021000000')
    sprite('null', 1)	# 1-1

@State
def rynef402_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(10000)
        Unknown1007(42000)
        Unknown3000(0)
        Unknown4061(3)
        Unknown3033()
        Unknown3019(180)
    sprite('vref_ryn402_00', 3)	# 1-3
    SFX_3('rynse_06')
    sprite('vref_ryn402_01', 3)	# 4-6
    GFX_0('rynef402_Fire', 6)
    GFX_0('rynef402_Fire', 5)
    GFX_0('rynef402_Fire', 4)
    GFX_0('rynef402_Fire', 3)
    GFX_0('rynef402_Fire', 2)
    GFX_0('rynef402_Fire', 1)
    sprite('null', 40)	# 7-46
    Unknown3038(1)
    GFX_0('rynef402_Bake', -1)
    Unknown4007(0)
    Unknown4009(0)
    GFX_0('rynef402B_Distortion', -1)

@State
def rynef402_Bake():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(-30000)
        Unknown1007(210000)
        Unknown1096(3100)
        Unknown3019(180)
        Unknown3033()
    sprite('null', 3)	# 1-3
    Unknown4003('72796e65663430325f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 12)	# 4-15
    Unknown3022(-20)

@State
def rynef402_Fire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
    sprite('null', 18)	# 1-18
    GFX_2('rynef402_bake_fireA')
    sprite('null', 22)	# 19-40

@State
def rynef402B_Distortion():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(100000)
        Unknown1007(250000)
        Unknown1096(1183)
        Unknown1072(10000)
    sprite('vref_ryn320_distortion', 10)	# 1-10
    Unknown3057(1)
    Unknown3058(25000)
    Unknown3059(-2500)

@State
def vref_ryn402_Hit():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(0)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown1000(320000)
        teleportRelativeY(237000)
        Unknown1096(1000)
        Unknown1073(7000)
    sprite('vref_ryn_burstA00', 3)	# 1-3
    GFX_0('vref_ryn402_Hit_b', -1)
    sprite('vref_ryn_burstA01', 3)	# 4-6
    Unknown1099(20)
    Unknown4009(2)
    sprite('vref_ryn_burstA02', 3)	# 7-9
    Unknown4007(0)
    Unknown3016(-10)
    sprite('vref_ryn_burstA03', 3)	# 10-12
    Unknown3004(-20)
    sprite('vref_ryn_burstA04', 3)	# 13-15

@State
def vref_ryn402_Hit_b():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown3013(200)
    sprite('vref_ryn_burstA00b', 3)	# 1-3
    sprite('vref_ryn_burstA01b', 3)	# 4-6
    sprite('vref_ryn_burstA02b', 3)	# 7-9
    Unknown3016(-10)
    sprite('vref_ryn_burstA03b', 3)	# 10-12
    Unknown3004(-20)
    sprite('vref_ryn_burstA04b', 3)	# 13-15

@State
def rynef403():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3000(0)
        Unknown4061(3)
        Unknown3033()
        teleportRelativeX(0)
        Unknown1007(260000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('vref_ryn403_00', 60)	# 1-60
    label(0)
    sprite('vref_ryn403_01', 60)	# 61-120
    label(1)
    sprite('vref_ryn403_02', 3)	# 121-123
    SFX_3('rynse_05')
    sprite('null', 40)	# 124-163
    GFX_0('rynef403_Bake', -1)
    GFX_0('rynef403_Particle', -1)
    Unknown4007(0)
    GFX_0('rynef403_Distortion', -1)

@State
def rynef403_Bake():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1007(10000)
        Unknown1096(3700)
        Unknown3019(180)
        Unknown3033()
    sprite('null', 3)	# 1-3
    Unknown4003('72796e65663430335f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(60)
    physicsXImpulse(-1000)
    physicsYImpulse(2300)
    sprite('null', 12)	# 4-15
    Unknown3022(-20)

@State
def rynef403_Particle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3038(1)
        teleportRelativeX(60000)
        Unknown1064(1100)
    sprite('vref_ryn403_02', 6)	# 1-6
    GFX_0('rynef403_FireC', 0)
    GFX_0('rynef403_FireC', 1)
    GFX_0('rynef403_FireC', 2)
    GFX_0('rynef403_FireB', 3)
    GFX_0('rynef403_FireA', 4)
    GFX_0('rynef403_FireA', 5)
    GFX_0('rynef403_FireA', 6)
    GFX_0('rynef403_FireA', 7)
    sprite('keep', 3)	# 7-9
    GFX_0('rynef403_FireD', 1)
    sprite('keep', 60)	# 10-69
    GFX_0('rynef403_FireD', 0)

@State
def rynef403_FireA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 18)	# 1-18
    GFX_2('rynef403_bake_fireC')
    sprite('null', 22)	# 19-40

@State
def rynef403_FireB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 18)	# 1-18
    GFX_2('rynef403_bake_fireA')
    sprite('null', 22)	# 19-40

@State
def rynef403_FireC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 18)	# 1-18
    Unknown4054(11)
    Unknown23067('rynef403_bake_fireB')
    sprite('null', 22)	# 19-40

@State
def rynef403_FireD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1096(950)
    sprite('null', 18)	# 1-18
    Unknown4054(11)
    Unknown23067('rynef403_bake_fireA2')
    sprite('null', 22)	# 19-40

@State
def rynef403_Distortion():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(-30000)
        Unknown1007(280000)
        teleportRelativeX(0)
        Unknown1007(-260000)
        Unknown1096(1100)
        Unknown1056(1200)
        Unknown1073(190000)
    sprite('vref_ryn406_distortion', 12)	# 1-12
    Unknown3057(1)
    Unknown3058(25000)
    Unknown3059(-2083)

@State
def vref_ryn403_Hit():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown1000(370000)
        teleportRelativeY(150000)
        Unknown1096(700)
        Unknown1072(20000)
    sprite('vref_ryn_burstB01', 2)	# 1-2
    Unknown1099(60)
    sprite('vref_ryn_burstB02', 2)	# 3-4
    Unknown4007(0)
    Unknown4009(2)
    Unknown1101(50)
    sprite('vref_ryn_burstB03', 2)	# 5-6
    sprite('vref_ryn_burstB04', 2)	# 7-8
    Unknown1101(50)
    sprite('vref_ryn_burstB05', 2)	# 9-10
    sprite('vref_ryn_burstB06', 2)	# 11-12
    sprite('vref_ryn_burstB07', 2)	# 13-14

@State
def rynef404():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(10000)
        Unknown1007(280000)
        Unknown3033()
        Unknown3001(128)
        Unknown1096(3700)
    sprite('null', 3)	# 1-3
    Unknown4003('72796e65663430345f77696e6430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4003('72796e65663430345f77696e6430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 9)	# 7-15
    Unknown4003('72796e65663430345f77696e6430322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4007(0)

@State
def rynef405():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 5)	# 1-5
    GFX_1('rynef405_smoke', -1)
    GFX_0('rynef405_Muzzle', -1)
    GFX_0('rynef405_Wind', -1)
    sprite('null', 20)	# 6-25
    GFX_0('rynef405_Wind', -1)
    Unknown36(1)
    Unknown1058(60)
    Unknown1066(50)
    Unknown3001(32)
    Unknown35()

@State
def rynef405_Muzzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown3000(0)
        Unknown4061(2)
        Unknown1072(-93000)
        Unknown1064(1400)
        Unknown1099(20)
        teleportRelativeX(-10000)
        Unknown1007(420000)
    sprite('vref_ryn_muzzle00', 3)	# 1-3
    GFX_2('rynef_MuzzleFlash')
    GFX_1('rynef405_aura01', -1)
    sprite('vref_ryn_muzzle01', 3)	# 4-6
    sprite('vref_ryn_muzzle02', 2)	# 7-8
    sprite('vref_ryn_muzzle03', 2)	# 9-10
    sprite('vref_ryn_muzzle04', 2)	# 11-12
    sprite('vref_ryn_muzzle05', 2)	# 13-14
    sprite('vref_ryn_muzzle06', 2)	# 15-16
    sprite('null', 10)	# 17-26

@State
def rynef405_Danger():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(-10000)
        Unknown1007(420000)
    sprite('null', 1)	# 1-1
    GFX_1('rynef405_aura', -1)
    SFX_3('rynse_06')

@State
def rynef405_Wind():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4003('72796e65663430355f77696e64303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(64)
        teleportRelativeX(-10000)
        Unknown1007(420000)
        Unknown1056(3000)
        Unknown1064(2200)
        Unknown1059(40)
        Unknown1067(10)
        Unknown1021(-2000)
        Unknown1072(-3000)
    sprite('null', 15)	# 1-15

@State
def rynef406():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        teleportRelativeX(-20000)
    sprite('null', 3)	# 1-3
    GFX_0('rynef406_Bake', -1)
    GFX_0('rynef406_Particle', -1)
    sprite('null', 12)	# 4-15
    Unknown4007(0)
    GFX_0('rynef406_Distortion', -1)
    sprite('null', 28)	# 16-43
    Unknown4009(0)

@State
def rynef406_Bake():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        teleportRelativeX(350000)
        Unknown1007(260000)
        Unknown1056(2400)
        Unknown1064(2800)
        Unknown3019(180)
        Unknown3033()
    sprite('null', 3)	# 1-3
    Unknown4003('72796e65663430365f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('rynef406_BakeBloom', -1)
    sprite('null', 3)	# 4-6
    Unknown4003('72796e65663430365f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    teleportRelativeX(-60000)
    physicsXImpulse(2000)
    Unknown1064(3100)
    Unknown1059(10)
    Unknown1067(50)
    sprite('null', 12)	# 7-18
    Unknown3022(-20)

@State
def rynef406_BakeBloom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown1096(1700)
        teleportRelativeX(-150000)
    sprite('null', 10)	# 1-10
    GFX_2('rynef406_bloom')

@State
def rynef406_Particle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        teleportRelativeX(50000)
        Unknown1007(-18000)
        Unknown1073(5000)
    sprite('vref_ryn406EX', 3)	# 1-3
    GFX_0('rynef406_FireA', 2)
    GFX_0('rynef406_FireA', 4)
    GFX_0('rynef406_FireA', 1)
    GFX_0('rynef406_FireA', 3)
    sprite('keep', 3)	# 4-6
    GFX_0('rynef406_FireB', 1)
    sprite('keep', 3)	# 7-9
    Unknown1007(40000)
    GFX_0('rynef406_FireB', 0)
    sprite('keep', 28)	# 10-37

@State
def rynef406_FireA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown1096(1200)
    sprite('null', 18)	# 1-18
    GFX_2('rynef406_bake_fire')
    sprite('null', 22)	# 19-40
    Unknown4011(0)
    Unknown4010(0)

@State
def rynef406_FireB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown1096(1200)
    sprite('null', 18)	# 1-18
    GFX_2('rynef406_bake_fireB')
    sprite('null', 22)	# 19-40
    Unknown4011(0)
    Unknown4010(0)

@State
def rynef406_Distortion():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1056(1200)
        Unknown1064(1000)
        teleportRelativeX(50000)
        Unknown1007(260000)
    sprite('vref_ryn406_distortion', 10)	# 1-10
    Unknown3057(1)
    Unknown3058(25000)
    Unknown3059(-2500)

@State
def vref_ryn406_Hit():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown1000(350000)
        teleportRelativeY(250000)
        Unknown1096(700)
    sprite('vref_ryn_burstB01', 2)	# 1-2
    Unknown1099(60)
    sprite('vref_ryn_burstB02', 2)	# 3-4
    Unknown4007(0)
    Unknown4009(3)
    Unknown1101(50)
    sprite('vref_ryn_burstB03', 2)	# 5-6
    sprite('vref_ryn_burstB04', 2)	# 7-8
    Unknown1101(50)
    sprite('vref_ryn_burstB05', 2)	# 9-10
    sprite('vref_ryn_burstB06', 2)	# 11-12
    sprite('vref_ryn_burstB07', 2)	# 13-14

@State
def vref_ryn406_Hit_b():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
        Unknown4006(2)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown3013(200)
    sprite('vref_ryn_burstA00b', 3)	# 1-3
    sprite('vref_ryn_burstA01b', 3)	# 4-6
    sprite('vref_ryn_burstA02b', 3)	# 7-9
    Unknown3016(-10)
    sprite('vref_ryn_burstA03b', 3)	# 10-12
    Unknown3004(-20)
    sprite('vref_ryn_burstA04b', 3)	# 13-15

@State
def rynef430():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
    sprite('null', 1)	# 1-1
    GFX_0('rynef430_Muzzle', -1)
    GFX_0('rynef430_Smoke', -1)
    GFX_0('rynef430_Smoke_Far', -1)
    GFX_0('rynef430_Dash', -1)
    SFX_3('rynse_02')
    sprite('null', 1)	# 2-2
    GFX_0('rynef430_RingSmoke00', -1)
    sprite('null', 1)	# 3-3
    GFX_0('rynef430_RingSmoke01', -1)
    sprite('null', 1)	# 4-4
    GFX_0('rynef430_Smoke2', -1)
    sprite('null', 1)	# 5-5
    GFX_0('rynef430_RingSmoke02', -1)
    sprite('null', 1)	# 6-6
    GFX_0('rynef430_Smoke2', -1)
    sprite('null', 1)	# 7-7
    GFX_0('rynef430_Tornade', -1)
    sprite('null', 1)	# 8-8
    GFX_0('rynef430_Smoke_Far', -1)
    GFX_0('rynef430_RingSmoke03', -1)
    sprite('null', 2)	# 9-10
    GFX_0('rynef430_Smoke', -1)
    sprite('null', 60)	# 11-70
    GFX_0('rynef430_Smoke_Far', -1)

@Subroutine
def rynef430_Smoke_Func():
    Unknown3032()
    Unknown3000(0)
    Unknown4061(3)
    Unknown13044(1)
    Unknown2054(1)
    Unknown4009(2)
    Unknown4011(3)
    physicsXImpulse(-3000)

@State
def rynef430_Smoke():

    def upon_IMMEDIATE():
        callSubroutine('rynef430_Smoke_Func')
        Unknown1096(800)
        Unknown1099(25)
        teleportRelativeX(50000)
        Unknown3026(-2041648)
    sprite('vref_ryn430_smoke00', 1)	# 1-1
    sprite('vref_ryn430_smoke01', 1)	# 2-2
    sprite('vref_ryn430_smoke02', 2)	# 3-4
    sprite('vref_ryn430_smoke03', 2)	# 5-6
    sprite('vref_ryn430_smoke04', 2)	# 7-8
    sprite('vref_ryn430_smoke05', 2)	# 9-10
    Unknown3004(-40)
    sprite('vref_ryn430_smoke06', 3)	# 11-13

@State
def rynef430_Smoke2():

    def upon_IMMEDIATE():
        callSubroutine('rynef430_Smoke_Func')
        Unknown1096(1000)
        Unknown1099(25)
        teleportRelativeX(240000)
        Unknown3026(-2041648)
    sprite('vref_ryn430_smoke00', 1)	# 1-1
    sprite('vref_ryn430_smoke01', 2)	# 2-3
    sprite('vref_ryn430_smoke02', 2)	# 4-5
    sprite('vref_ryn430_smoke03', 2)	# 6-7
    sprite('vref_ryn430_smoke04', 2)	# 8-9
    sprite('vref_ryn430_smoke05', 3)	# 10-12
    Unknown3004(-40)
    sprite('vref_ryn430_smoke06', 3)	# 13-15

@State
def rynef430_Smoke_Far():

    def upon_IMMEDIATE():
        callSubroutine('rynef430_Smoke_Func')
        Unknown23015(11)
        Unknown1096(650)
        Unknown1099(20)
        teleportRelativeX(170000)
        Unknown3026(-5199712)
    sprite('vref_ryn430_smoke00', 1)	# 1-1
    sprite('vref_ryn430_smoke01', 2)	# 2-3
    sprite('vref_ryn430_smoke02', 2)	# 4-5
    sprite('vref_ryn430_smoke03', 2)	# 6-7
    sprite('vref_ryn430_smoke04', 2)	# 8-9
    sprite('vref_ryn430_smoke05', 3)	# 10-12
    Unknown3004(-40)
    sprite('vref_ryn430_smoke06', 3)	# 13-15

@Subroutine
def rynef430_RingSmoke_Func():
    Unknown4009(2)
    Unknown4011(3)
    Unknown3032()
    Unknown1090(10)
    physicsXImpulse(-5000)
    Unknown1072(-35000)
    Unknown3026(-2041648)

@State
def rynef430_RingSmoke00():

    def upon_IMMEDIATE():
        Unknown4003('72796e65665f72696e67736d6f6b6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1500)
        teleportRelativeY(150000)
        teleportRelativeX(-300000)
        callSubroutine('rynef430_RingSmoke_Func')
    sprite('null', 6)	# 1-6
    Unknown1099(200)
    Unknown1093(10)
    sprite('null', 6)	# 7-12
    Unknown3004(-42)
    Unknown1099(100)
    Unknown1093(10)

@State
def rynef430_RingSmoke01():

    def upon_IMMEDIATE():
        Unknown4003('72796e65665f72696e67736d6f6b6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(2000)
        teleportRelativeY(200000)
        teleportRelativeX(-150000)
        callSubroutine('rynef430_RingSmoke_Func')
    sprite('null', 8)	# 1-8
    Unknown1099(300)
    Unknown1093(10)
    sprite('null', 6)	# 9-14
    Unknown3004(-42)
    Unknown1099(150)
    Unknown1093(10)

@State
def rynef430_RingSmoke02():

    def upon_IMMEDIATE():
        Unknown4003('72796e65665f72696e67736d6f6b6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1500)
        teleportRelativeY(180000)
        teleportRelativeX(-100000)
        callSubroutine('rynef430_RingSmoke_Func')
    sprite('null', 6)	# 1-6
    Unknown1099(250)
    Unknown1093(10)
    sprite('null', 6)	# 7-12
    Unknown3004(-42)
    Unknown1099(125)
    Unknown1093(10)

@State
def rynef430_RingSmoke03():

    def upon_IMMEDIATE():
        Unknown4003('72796e65665f72696e67736d6f6b6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1500)
        teleportRelativeY(200000)
        teleportRelativeX(-100000)
        callSubroutine('rynef430_RingSmoke_Func')
    sprite('null', 6)	# 1-6
    Unknown1099(200)
    Unknown1093(10)
    sprite('null', 6)	# 7-12
    Unknown3004(-42)
    Unknown1099(100)
    Unknown1093(10)

@State
def rynef430_Dash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 50)	# 1-50
    GFX_0('rynef430_Trail', -1)
    GFX_0('rynef430_Aura', -1)
    GFX_0('rynef430_Speed', -1)

@State
def rynef430_Trail():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        GFX_0('rynef430_Trail00a', -1)
        GFX_0('rynef430_Trail00b', -1)
        GFX_0('rynef430_Trail02a', -1)
        GFX_0('rynef430_Trail02b', -1)
        GFX_0('rynef430_Trail01a', -1)
        GFX_0('rynef430_Trail01b', -1)
        Unknown1056(900)
        Unknown1064(2500)
        Unknown1000(-140000)
        teleportRelativeY(170000)

        def upon_STATE_END():
            Unknown1096(0)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 12)	# 1-12
    Unknown1059(150)
    label(0)
    sprite('null', 20)	# 13-32
    Unknown1059(0)
    physicsXImpulse(0)
    label(1)
    sprite('null', 3)	# 33-35
    Unknown1059(0)

    def upon_CLEAR_OR_EXIT():
        Unknown1058(80)
    sprite('null', 12)	# 36-47
    Unknown3004(-64)

@State
def rynef430_Trail00a():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c3030522e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown3003(80)
        Unknown4061(5)
        Unknown21004(1)
    sprite('null', 32767)	# 1-32767

@State
def rynef430_Trail00b():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c30304c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown3003(80)
        Unknown1096(2500)
        Unknown4061(5)
        Unknown21004(1)
    sprite('null', 32767)	# 1-32767

@State
def rynef430_Trail01a():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c3031522e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown4061(5)
        Unknown21004(3)
    sprite('null', 32767)	# 1-32767

@State
def rynef430_Trail01b():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c30314c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown1096(2500)
        Unknown4061(5)
        Unknown21004(3)
    sprite('null', 32767)	# 1-32767

@State
def rynef430_Trail02a():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c3032522e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown4061(5)
        Unknown21004(2)
        Unknown3003(80)
    sprite('null', 32767)	# 1-32767

@State
def rynef430_Trail02b():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c30324c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown1096(2500)
        Unknown4061(5)
        Unknown21004(2)
        Unknown3003(80)
    sprite('null', 32767)	# 1-32767

@State
def rynef430_Aura():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663430325f6175726130302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown1056(2400)
        Unknown1064(4600)
        Unknown1000(140000)
        teleportRelativeY(170000)
        Unknown3001(100)
        sendToLabelUpon(33, 1)
    sprite('null', 3)	# 1-3
    Unknown1059(1100)
    sprite('null', 30)	# 4-33
    Unknown1059(100)
    label(1)
    sprite('null', 6)	# 34-39
    Unknown1059(100)
    Unknown3004(-16)
    Unknown1067(-50)

@State
def rynef430_Speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1000(140000)
        teleportRelativeY(210000)
        sendToLabelUpon(32, 1)

        def upon_33():
            Unknown14()
    label(0)
    sprite('null', 2)	# 1-2
    GFX_1('rynef402_speed', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 2)	# 3-4
    GFX_1('rynef402_speed01', -1)
    gotoLabel(1)

@State
def rynef430_DashSingal():

    def upon_IMMEDIATE():
        Unknown21012('72796e65663433305f547261696c00000000000000000000000000000000000020000000')
        Unknown21012('72796e65663433305f547261696c5f446973746f7274696f6e0000000000000020000000')
        Unknown21012('72796e65663433305f537065656400000000000000000000000000000000000020000000')
        Unknown21012('72796e656634303300000000000000000000000000000000000000000000000020000000')
    sprite('null', 1)	# 1-1

@State
def rynef430_DashSingalB():

    def upon_IMMEDIATE():
        Unknown21012('72796e656634303300000000000000000000000000000000000000000000000021000000')
    sprite('null', 1)	# 1-1

@State
def rynef430_DashEnd():

    def upon_IMMEDIATE():
        Unknown21012('72796e65663433305f547261696c00000000000000000000000000000000000021000000')
        Unknown21012('72796e65663433305f547261696c5f446973746f7274696f6e0000000000000021000000')
        Unknown21012('72796e65663433305f417572610000000000000000000000000000000000000021000000')
        Unknown21012('72796e65663433305f537065656400000000000000000000000000000000000021000000')
    sprite('null', 1)	# 1-1

@State
def rynef430_HitA():

    def upon_IMMEDIATE():
        pass
    sprite('null', 30)	# 1-30
    GFX_0('rynef430_HitA_01', -1)
    GFX_0('rynef430_HitA_02', -1)
    GFX_0('rynef430_HitA_03', -1)
    GFX_0('rynef430_HitA_04', -1)
    GFX_0('rynef430_HitA_05', -1)
    GFX_0('rynef_EXHIT_B', -1)
    GFX_1('rynef_ExHit', -1)
    GFX_0('rynef431_Hit_Circle', -1)
    Unknown36(1)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown35()

@Subroutine
def rynef430_HitA_Func():
    Unknown4007(2)
    Unknown3000(0)
    Unknown4061(4)
    Unknown1102(-100, 100)
    Unknown1077(10000, -10000)
    Unknown1061(80)
    GFX_0('rynef430_HitA_Bloom', -1)
    Unknown4015()
    Unknown3032()

@State
def rynef430_HitA_01():

    def upon_IMMEDIATE():
        Unknown1096(2100)
        Unknown1099(30)
        Unknown1073(30000)
        callSubroutine('rynef430_HitA_Func')
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 2-3
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 4-5
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 6-7
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef430_HitA_02():

    def upon_IMMEDIATE():
        Unknown1096(1800)
        Unknown1099(30)
        Unknown1073(100000)
        callSubroutine('rynef430_HitA_Func')
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 2-3
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 4-5
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 6-7
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef430_HitA_03():

    def upon_IMMEDIATE():
        Unknown1096(1500)
        Unknown1099(20)
        Unknown1073(190000)
        callSubroutine('rynef430_HitA_Func')
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 2-3
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 4-5
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 6-7
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef430_HitA_04():

    def upon_IMMEDIATE():
        Unknown1096(2100)
        Unknown1099(30)
        Unknown1073(250000)
        callSubroutine('rynef430_HitA_Func')
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 2-3
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 4-5
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 6-7
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef430_HitA_05():

    def upon_IMMEDIATE():
        Unknown1096(1500)
        Unknown1099(20)
        Unknown1073(320000)
        callSubroutine('rynef430_HitA_Func')
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f68697430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 2-3
    Unknown4003('72796e65663433305f68697430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 4-5
    Unknown4003('72796e65663433305f68697430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 6-7
    Unknown4003('72796e65663433305f68697430332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72796e65663433305f68697430342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72796e65663433305f68697430352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72796e65663433305f68697430362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72796e65663433305f68697430372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef430_HitA_Bloom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown4015()
        Unknown3033()
        Unknown3000(0)
        Unknown4061(4)
        Unknown23015(6)
    sprite('null', 1)	# 1-1
    Unknown4003('72796e65663433305f6869743030622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 2-3
    Unknown4003('72796e65663433305f6869743031622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 4-5
    Unknown4003('72796e65663433305f6869743032622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 6-7
    Unknown4003('72796e65663433305f6869743033622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72796e65663433305f6869743034622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72796e65663433305f6869743035622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72796e65663433305f6869743036622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72796e65663433305f6869743037622e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rynef430_Muzzle():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown3000(0)
        Unknown4061(2)
        Unknown23015(7)
        teleportRelativeY(200000)
        teleportRelativeX(-20000)
        Unknown1096(1400)
        Unknown2005()
        Unknown2054(1)
    sprite('null', 1)	# 1-1
    GFX_0('rynef_Muzzle', -1)

@State
def rynef430_Tornade():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1096(2000)
        Unknown1064(3700)
        Unknown1090(20)
        teleportRelativeY(150000)
        Unknown1072(5000)
        Unknown3026(-128)
        Unknown3001(0)
    sprite('null', 6)	# 1-6
    Unknown1059(200)
    Unknown1067(100)
    Unknown1091(60)
    Unknown3025(-49152, 8)
    Unknown4003('72796e65663433305f746f726e6164652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3004(42)
    sprite('null', 6)	# 7-12
    Unknown3004(-16)
    Unknown1101(50)
    sprite('null', 6)	# 13-18
    Unknown1101(50)

@State
def rynef430_Flare():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1000(110000)
        teleportRelativeY(280000)
        Unknown1096(1500)
    sprite('null', 40)	# 1-40
    GFX_2('rynef430_OD_flare')

@State
def rynef_DDD_Particle():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        teleportRelativeY(280000)
        Unknown1000(250000)
    sprite('null', 1)	# 1-1
    GFX_1('rynef_DDD', -1)

@State
def rynef431():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown4011(3)
        sendToLabelUpon(32, 0)
    sprite('null', 2)	# 1-2
    GFX_0('rynef431_Smoke01', -1)
    sprite('null', 5)	# 3-7
    GFX_0('rynef431_Smoke02', -1)
    sprite('null', 60)	# 8-67
    GFX_0('rynef431_Smoke01', -1)
    label(0)
    sprite('null', 120)	# 68-187
    GFX_0('rynef431_bake', -1)

@State
def rynef431_bake():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4061(0)
        teleportRelativeX(130000)
        Unknown1007(242000)
        Unknown13044(1)
    sprite('vref_ryn431_00', 5)	# 1-5
    sprite('vref_ryn431_01', 3)	# 6-8
    sprite('vref_ryn431_02', 2)	# 9-10
    sprite('null', 5)	# 11-15
    sprite('vref_ryn431_03', 5)	# 16-20
    sprite('vref_ryn431_04', 3)	# 21-23
    sprite('vref_ryn431_05', 2)	# 24-25
    sprite('null', 4)	# 26-29
    sprite('vref_ryn431_00', 4)	# 30-33
    sprite('vref_ryn431_01', 2)	# 34-35
    sprite('vref_ryn431_02', 2)	# 36-37
    sprite('null', 4)	# 38-41
    sprite('vref_ryn431_03', 4)	# 42-45
    sprite('vref_ryn431_04', 2)	# 46-47
    sprite('vref_ryn431_05', 2)	# 48-49
    sprite('null', 3)	# 50-52
    sprite('vref_ryn431_00', 3)	# 53-55
    sprite('vref_ryn431_01', 2)	# 56-57
    sprite('vref_ryn431_02', 1)	# 58-58
    sprite('null', 3)	# 59-61
    sprite('vref_ryn431_03', 3)	# 62-64
    sprite('vref_ryn431_04', 2)	# 65-66
    sprite('vref_ryn431_05', 1)	# 67-67
    sprite('null', 3)	# 68-70
    sprite('vref_ryn431_00', 3)	# 71-73
    sprite('vref_ryn431_01', 2)	# 74-75
    sprite('vref_ryn431_02', 1)	# 76-76

@State
def rynef431_Smoke01():

    def upon_IMMEDIATE():
        callSubroutine('rynef430_Smoke_Func')
        Unknown1096(700)
        Unknown1099(25)
        teleportRelativeX(50000)
        Unknown3026(-2041648)
    sprite('vref_ryn430_smoke00', 1)	# 1-1
    sprite('vref_ryn430_smoke01', 1)	# 2-2
    sprite('vref_ryn430_smoke02', 2)	# 3-4
    sprite('vref_ryn430_smoke03', 2)	# 5-6
    sprite('vref_ryn430_smoke04', 2)	# 7-8
    sprite('vref_ryn430_smoke05', 2)	# 9-10
    Unknown3004(-40)
    sprite('vref_ryn430_smoke06', 3)	# 11-13

@State
def rynef431_Smoke02():

    def upon_IMMEDIATE():
        callSubroutine('rynef430_Smoke_Func')
        Unknown23015(11)
        Unknown1096(550)
        Unknown1099(20)
        teleportRelativeX(160000)
        Unknown3026(-5199712)
    sprite('vref_ryn430_smoke00', 1)	# 1-1
    sprite('vref_ryn430_smoke01', 2)	# 2-3
    sprite('vref_ryn430_smoke02', 2)	# 4-5
    sprite('vref_ryn430_smoke03', 2)	# 6-7
    sprite('vref_ryn430_smoke04', 2)	# 8-9
    sprite('vref_ryn430_smoke05', 3)	# 10-12
    Unknown3004(-40)
    sprite('vref_ryn430_smoke06', 3)	# 13-15

@State
def rynef431_Hit01():

    def upon_IMMEDIATE():
        Unknown1077(30000, -30000)
    sprite('null', 1)	# 1-1
    GFX_0('rynef_EXHIT_A01', -1)
    GFX_0('rynef_EXHIT_A02', -1)
    GFX_0('rynef_EXHIT_A03', -1)
    GFX_0('rynef_EXHIT_A04', -1)
    GFX_0('rynef431_EXHIT_C', -1)
    GFX_1('rynef_ExHit', -1)

@State
def rynef431_EXHIT_C():

    def upon_IMMEDIATE():
        Unknown4003('72796e65665f636972636c6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown1073(180000)
        Unknown3032()
        Unknown23015(6)
        Unknown1096(1000)
        Unknown1058(50)
        Unknown1090(150)
        GFX_0('rynef_EXHIT_C_Bloom', -1)
    sprite('null', 5)	# 1-5
    Unknown1099(240)
    Unknown1061(50)
    Unknown1093(150)
    sprite('null', 5)	# 6-10
    Unknown1101(60)
    sprite('null', 5)	# 11-15
    Unknown1101(60)
    Unknown3004(-40)

@State
def rynef431_BG():

    def upon_IMMEDIATE():
        teleportRelativeY(250000)
        Unknown6001(1)

        def upon_CLEAR_OR_EXIT():
            Unknown23032(50)
    sprite('null', 10)	# 1-10
    GFX_1('rynef431_speed', -1)
    GFX_1('rynef431_bg', -1)
    GFX_0('rynef431_BG01', -1)
    GFX_0('rynef431_BG00', -1)
    sprite('null', 40)	# 11-50
    GFX_1('rynef431_bg', -1)

@State
def rynef431_BG00():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433315f626730302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown3032()
        Unknown23015(15)
        Unknown1056(2000)
        Unknown23118(-16384)
        Unknown1058(110)
    sprite('null', 3)	# 1-3
    Unknown1064(1100)
    sprite('null', 3)	# 4-6
    Unknown1064(1700)
    sprite('null', 3)	# 7-9
    sprite('null', 12)	# 10-21
    Unknown1067(0)

@State
def rynef431_BG01():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433315f626730312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown3033()
        Unknown23015(15)
        Unknown1056(2000)
        Unknown1064(1200)
        Unknown3026(-49152)
        Unknown1058(110)
    sprite('null', 3)	# 1-3
    Unknown1064(1400)
    sprite('null', 3)	# 4-6
    Unknown1064(2000)
    sprite('null', 3)	# 7-9
    sprite('null', 6)	# 10-15
    sprite('null', 30)	# 16-45
    Unknown3004(-8)

@State
def rynef431_Hit_Circle():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433315f636972636c6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown3032()
        Unknown23015(6)
        Unknown1096(1600)
        teleportRelativeY(200000)
        teleportRelativeX(180000)
        Unknown1090(10)
    sprite('null', 5)	# 1-5
    Unknown1099(180)
    Unknown1093(10)
    sprite('null', 5)	# 6-10
    Unknown1101(70)
    sprite('null', 8)	# 11-18
    Unknown1101(70)

@State
def rynef431OD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown4011(3)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 2)	# 1-2
    GFX_0('rynef431_Smoke01', -1)
    sprite('null', 5)	# 3-7
    GFX_0('rynef431_Smoke02', -1)
    sprite('null', 60)	# 8-67
    GFX_0('rynef431_Smoke01', -1)
    label(0)
    sprite('null', 120)	# 68-187
    GFX_0('rynef431_bakeOD', -1)
    label(1)
    sprite('null', 120)	# 188-307
    GFX_0('rynef450_upper', -1)

@State
def rynef431_bakeOD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4061(0)
        teleportRelativeX(130000)
        Unknown1007(242000)
        Unknown13044(1)
    sprite('vref_ryn431_00', 4)	# 1-4
    sprite('vref_ryn431_01', 2)	# 5-6
    sprite('vref_ryn431_02', 2)	# 7-8
    sprite('null', 4)	# 9-12
    sprite('vref_ryn431_03', 4)	# 13-16
    sprite('vref_ryn431_04', 2)	# 17-18
    sprite('vref_ryn431_05', 2)	# 19-20
    sprite('null', 3)	# 21-23
    sprite('vref_ryn431_00', 3)	# 24-26
    sprite('vref_ryn431_01', 2)	# 27-28
    sprite('vref_ryn431_02', 1)	# 29-29
    sprite('null', 3)	# 30-32
    sprite('vref_ryn431_03', 3)	# 33-35
    sprite('vref_ryn431_04', 2)	# 36-37
    sprite('vref_ryn431_05', 1)	# 38-38
    sprite('null', 2)	# 39-40
    sprite('vref_ryn431_00', 2)	# 41-42
    sprite('vref_ryn431_01', 1)	# 43-43
    sprite('vref_ryn431_02', 1)	# 44-44
    sprite('null', 2)	# 45-46
    sprite('vref_ryn431_03', 2)	# 47-48
    sprite('vref_ryn431_04', 1)	# 49-49
    sprite('vref_ryn431_05', 1)	# 50-50
    sprite('null', 2)	# 51-52
    sprite('vref_ryn431_00', 2)	# 53-54
    sprite('vref_ryn431_01', 1)	# 55-55
    sprite('vref_ryn431_02', 1)	# 56-56
    sprite('null', 2)	# 57-58
    sprite('vref_ryn431_03', 2)	# 59-60
    sprite('vref_ryn431_04', 1)	# 61-61
    sprite('vref_ryn431_05', 1)	# 62-62
    sprite('null', 1)	# 63-63
    sprite('vref_ryn431_00', 1)	# 64-64
    sprite('vref_ryn431_01', 1)	# 65-65
    sprite('null', 1)	# 66-66
    sprite('vref_ryn431_03', 1)	# 67-67
    sprite('vref_ryn431_04', 1)	# 68-68
    sprite('null', 1)	# 69-69
    sprite('vref_ryn431_00', 1)	# 70-70
    sprite('vref_ryn431_01', 1)	# 71-71
    sprite('null', 1)	# 72-72
    sprite('vref_ryn431_03', 1)	# 73-73
    sprite('vref_ryn431_04', 1)	# 74-74

@State
def rynef450_upper():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 9)	# 1-9
    GFX_0('rynef450_Upper_Bake', -1)
    sprite('null', 3)	# 10-12
    GFX_0('rynef450_Upper_Particle', -1)
    sprite('null', 40)	# 13-52
    Unknown4007(0)

@State
def rynef450_Upper_Bake():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(30000)
        Unknown1007(260000)
        Unknown1096(2200)
        Unknown1072(5000)
        Unknown3019(180)
        Unknown1067(40)
        physicsYImpulse(-2000)
        Unknown3033()
    sprite('null', 9)	# 1-9
    Unknown4003('72796e65663332305f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4003('72796e65663332305f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 12)	# 13-24
    Unknown3022(-20)

@State
def rynef450_Upper_Particle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        teleportRelativeX(40000)
        Unknown1007(50000)
        Unknown1072(-3000)
    sprite('vref_ryn320EX', 6)	# 1-6
    GFX_0('rynef320_Fire', 0)
    GFX_0('rynef320_Fire', 1)
    GFX_0('rynef320_Fire', 2)
    GFX_0('rynef320_Fire', 3)
    sprite('vref_ryn320EX', 40)	# 7-46
    GFX_0('rynef320_Fire', 0)
    GFX_0('rynef320_Fire', 2)
    GFX_0('rynef320_Fire', 1)
    GFX_0('rynef320_Fire', 3)

@State
def rynef450_Aura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        teleportRelativeY(200000)
        GFX_1('rynef_OD_aura', -1)
    label(0)
    sprite('null', 3)	# 1-3
    GFX_1('rynef450_aura_loop', -1)
    gotoLabel(0)

@State
def rynef450_AuraLoop():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        teleportRelativeY(200000)
        Unknown1000(50000)
    label(0)
    sprite('null', 3)	# 1-3
    GFX_1('rynef450_aura_loop', -1)
    gotoLabel(0)

@State
def rynef450_1st():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown3003(70)
        Unknown1096(3700)
        teleportRelativeX(20000)
        Unknown1007(120000)
        sendToLabelUpon(32, 0)

        def upon_33():
            Unknown4010(0)
    sprite('null', 5)	# 1-5
    Unknown4003('72796e65663435305f77696e6430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)	# 6-10
    Unknown4003('72796e65663435305f77696e6430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 30)	# 11-40
    Unknown4003('72796e65663435305f77696e6430322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 11)	# 41-51
    Unknown4003('72796e65663435305f77696e6430332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('rynef450_1st_Smoke', -1)

@State
def rynef450_1st_Smoke():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown1000(300000)
        teleportRelativeY(0)
    sprite('null', 1)	# 1-1
    GFX_1('rynef450_1st_smoke', -1)

@State
def rynef450_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown4011(3)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)
    sprite('null', 28)	# 1-28
    sprite('null', 300)	# 29-328
    GFX_0('vref_ryn450_Rush3rd', -1)
    sprite('null', 300)	# 329-628
    GFX_0('rynef450_RushHit02', -1)
    sprite('null', 300)	# 629-928

@State
def rynef450_RushHit01():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown3000(0)
        Unknown4061(2)
        Unknown3033()
        Unknown1000(200000)
        teleportRelativeY(70000)
        Unknown1096(700)
        Unknown1072(50000)
    sprite('vref_ryn_burstB01', 2)	# 1-2
    Unknown1099(60)
    sprite('vref_ryn_burstB02', 2)	# 3-4
    Unknown4007(0)
    Unknown4009(3)
    Unknown1101(50)
    sprite('vref_ryn_burstB03', 2)	# 5-6
    sprite('vref_ryn_burstB04', 2)	# 7-8
    Unknown1101(50)
    sprite('vref_ryn_burstB05', 2)	# 9-10
    sprite('vref_ryn_burstB06', 2)	# 11-12
    sprite('vref_ryn_burstB07', 2)	# 13-14

@State
def rynef450_RushHit02():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433315f636972636c6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4006(2)
        Unknown3032()
        Unknown23015(6)
        Unknown1096(1600)
        teleportRelativeY(200000)
        teleportRelativeX(180000)
        Unknown1090(30)
    sprite('null', 5)	# 1-5
    Unknown1099(400)
    Unknown1093(30)
    physicsXImpulse(5000)
    sprite('null', 5)	# 6-10
    Unknown1101(70)
    sprite('null', 5)	# 11-15
    Unknown1101(70)

@State
def rynef450_431bake():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4061(0)
        teleportRelativeX(130000)
        Unknown1007(250000)
        Unknown13044(1)
    sprite('vref_ryn431_00', 3)	# 1-3
    sprite('vref_ryn431_01', 2)	# 4-5
    sprite('vref_ryn431_02', 1)	# 6-6
    sprite('null', 5)	# 7-11
    sprite('vref_ryn431_03', 3)	# 12-14
    sprite('vref_ryn431_04', 2)	# 15-16
    sprite('vref_ryn431_05', 1)	# 17-17

@State
def rynef450_Dash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
    sprite('null', 3)	# 1-3
    GFX_0('rynef450_DashSpeed', -1)
    sprite('null', 1)	# 4-4
    GFX_0('rynef450_Trail', -1)
    GFX_0('rynef450_DashWind', -1)
    GFX_0('rynef430_Smoke', -1)
    sprite('null', 2)	# 5-6
    GFX_0('rynef430_Smoke2', -1)
    sprite('null', 1)	# 7-7
    GFX_0('rynef430_Smoke_Far', -1)
    sprite('null', 1)	# 8-8
    GFX_0('rynef430_Smoke', -1)
    sprite('null', 60)	# 9-68
    GFX_0('rynef430_Smoke_Far', -1)

@State
def rynef450_Trail():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        GFX_0('rynef450_Trail00a', -1)
        GFX_0('rynef450_Trail00b', -1)
        GFX_0('rynef450_Trail02a', -1)
        GFX_0('rynef450_Trail02b', -1)
        GFX_0('rynef450_Trail01a', -1)
        GFX_0('rynef450_Trail01b', -1)
        Unknown1056(1000)
        Unknown1064(2500)
        Unknown1000(-140000)
        teleportRelativeY(170000)

        def upon_STATE_END():
            Unknown1096(0)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 6)	# 1-6
    Unknown3001(0)
    Unknown3004(64)
    Unknown1059(100)
    sprite('null', 6)	# 7-12
    Unknown1059(200)
    label(0)
    sprite('null', 20)	# 13-32
    Unknown1059(0)
    physicsXImpulse(0)
    label(1)
    sprite('null', 3)	# 33-35
    Unknown4009(0)
    sprite('null', 3)	# 36-38
    Unknown1059(0)

    def upon_CLEAR_OR_EXIT():
        Unknown1058(80)
    sprite('null', 12)	# 39-50
    Unknown3004(-64)

@State
def rynef450_Trail00a():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c3030522e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown3003(80)
        Unknown4061(5)
        Unknown21004(1)
    sprite('null', 32767)	# 1-32767

@State
def rynef450_Trail00b():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c30304c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown3003(80)
        Unknown1096(2500)
        Unknown4061(5)
        Unknown21004(1)
    sprite('null', 32767)	# 1-32767

@State
def rynef450_Trail01a():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c3031522e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown4061(5)
        Unknown21004(3)
    sprite('null', 32767)	# 1-32767

@State
def rynef450_Trail01b():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c30314c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown1096(2500)
        Unknown4061(5)
        Unknown21004(3)
    sprite('null', 32767)	# 1-32767

@State
def rynef450_Trail02a():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c3032522e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown4061(5)
        Unknown21004(2)
        Unknown3003(80)
    sprite('null', 32767)	# 1-32767

@State
def rynef450_Trail02b():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663433305f747261696c30324c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown23015(11)
        Unknown1096(2500)
        Unknown4061(5)
        Unknown21004(2)
        Unknown3003(80)
    sprite('null', 32767)	# 1-32767

@State
def rynef450_DashWind():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663430325f6175726130302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3033()
        Unknown1056(2400)
        Unknown1064(4600)
        Unknown1000(140000)
        teleportRelativeY(170000)
        Unknown3001(100)
        sendToLabelUpon(33, 1)
    sprite('null', 3)	# 1-3
    Unknown1059(1100)
    sprite('null', 30)	# 4-33
    Unknown1059(100)
    label(1)
    sprite('null', 6)	# 34-39
    Unknown4009(0)
    Unknown1059(100)
    Unknown3004(-16)
    Unknown1067(-50)

@State
def rynef450_DashSpeed():

    def upon_IMMEDIATE():

        def upon_CLEAR_OR_EXIT():
            Unknown23057(50)
            Unknown23058(50)
    sprite('null', 50)	# 1-50
    GFX_2('rynef450_speedB')

@State
def rynef450_3rd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown21010(1)
        Unknown4011(3)
        Unknown4010(3)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('null', 5)	# 1-5
    GFX_1('rynef450_jumpsmoke', -1)
    sprite('null', 300)	# 6-305
    GFX_0('rynef450_BG_ScrollUp', -1)
    label(0)
    sprite('null', 300)	# 306-605
    label(1)
    sprite('null', 3)	# 606-608
    GFX_0('RWBY_AHground', -1)
    sprite('null', 100)	# 609-708
    GFX_0('rynef450_BG_ScrollDown', -1)
    label(2)
    sprite('null', 5)	# 709-713
    Unknown26('rynef450_AuraLoop')
    GFX_0('rynef450_BG', -1)
    GFX_0('rynef450_GroundShockwave', -1)
    GFX_0('rynef450_GroundShockwave_b', -1)
    GFX_0('rynef450_GroundBloomB', -1)
    GFX_0('rynef450_GroundBloom', -1)
    Unknown4054(0)
    Unknown4045('72796e65663435305f736d6f6b65000000000000000000000000000000000000ffffffff')
    Unknown4045('72796e65663435305f736d6f6b65420000000000000000000000000000000000ffffffff')
    Unknown4054(14)
    Unknown4045('72796e65663435305f736d6f6b65430000000000000000000000000000000000ffffffff')
    GFX_0('rynef450_Hit_Circle', -1)
    GFX_0('rynef450_ScreenFire', -1)
    GFX_0('rynef450_LineWind', -1)
    GFX_0('rynef450_LineWind_b', -1)
    GFX_0('rynef450_Glass00', -1)
    GFX_0('rynef450_Glass00', -1)
    GFX_0('rynef450_Glass00', -1)
    GFX_0('rynef450_Glass01', -1)
    GFX_0('rynef450_Glass01', -1)
    GFX_0('rynef450_Glass02', -1)
    GFX_0('rynef450_Glass02', -1)
    GFX_0('rynef450_Glass03', -1)
    GFX_0('rynef450_Glass03', -1)
    GFX_0('rynef450_Glass03', -1)
    GFX_0('rynef450_Glass10', -1)
    GFX_0('rynef450_Glass10', -1)
    GFX_0('rynef450_Glass10', -1)
    GFX_0('rynef450_Glass10', -1)
    GFX_0('rynef450_Glass11', -1)
    GFX_0('rynef450_Glass11', -1)
    GFX_0('rynef450_Glass11', -1)
    GFX_0('rynef450_Glass11', -1)
    GFX_0('rynef450_Glass20', -1)
    GFX_0('rynef450_Glass20', -1)
    GFX_0('rynef450_Glass20', -1)
    GFX_0('rynef450_Glass20', -1)
    GFX_0('rynef450_Glass20', -1)
    GFX_0('rynef450_Glass20', -1)
    GFX_0('rynef450_Glass21', -1)
    GFX_0('rynef450_Glass21', -1)
    GFX_0('rynef450_Glass22', -1)
    GFX_0('rynef450_Glass22', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass30', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    GFX_0('rynef450_Glass31', -1)
    sprite('null', 90)	# 714-803
    GFX_1('rynef450_glass', -1)
    Unknown26('RWBY_AHground')
    Unknown26('rynef450_GroundBloom')
    Unknown26('rynef450_GroundBloomB')
    sprite('null', 300)	# 804-1103
    GFX_0('rynef450_WhiteOut', -1)

@State
def RWBY_AHground():

    def upon_IMMEDIATE():
        Unknown4003('525742595f414867726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(3)
        Unknown4011(3)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3026(-16777216)
        Unknown1000(0)
        teleportRelativeY(-1000)
        Unknown3032()
        Unknown23015(2)
    sprite('null', 32767)	# 1-32767

@State
def rynef450_Flare():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3026(-16777216)
        Unknown1096(0)
        GFX_2('rynef450_flare')
        Unknown3001(128)
    sprite('null', 6)	# 1-6
    Unknown1099(170)
    Unknown1000(30000)
    teleportRelativeY(280000)
    sprite('null', 8)	# 7-14
    Unknown1099(0)
    Unknown1000(-10000)
    teleportRelativeY(290000)
    sprite('null', 8)	# 15-22
    sprite('null', 8)	# 23-30
    sprite('null', 6)	# 31-36
    sprite('null', 3)	# 37-39
    Unknown1000(-15000)
    teleportRelativeY(310000)

@State
def rynef450_BG_ScrollUp():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown23015(2)
        Unknown3032()

        def upon_CLEAR_OR_EXIT():
            Unknown23057(50)
            Unknown23058(50)
        Unknown23067('rynef450_speed')
    sprite('null', 20)	# 1-20
    Unknown1096(2500)
    Unknown4003('72796e65663435305f62675f7363726f6c6c75702e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)	# 21-28
    Unknown3004(-32)
    Unknown1064(2500)

@State
def rynef450_BG_ScrollDown():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown23015(2)
        Unknown3032()

        def upon_CLEAR_OR_EXIT():
            Unknown23057(50)
            Unknown23058(50)
        GFX_0('rynef450_BG_ScrollDown_Speed', -1)
    sprite('null', 20)	# 1-20
    Unknown1096(2500)
    Unknown4003('72796e65663435305f62675f7363726f6c6c646f776e2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 8)	# 21-28
    Unknown3004(-32)
    Unknown1064(2500)

@State
def rynef450_BG_ScrollDown_Speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1072(180000)
        Unknown23067('rynef450_speed')
    sprite('null', 28)	# 1-28

@State
def rynef450_GroundShockwave():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1096(1400)
        Unknown1099(100)
        Unknown3000(0)
        Unknown4061(4)
        Unknown1007(-30000)
    sprite('vref_ryn450_burst00', 2)	# 1-2
    sprite('vref_ryn450_burst01', 3)	# 3-5
    sprite('vref_ryn450_burst01', 300)	# 6-305
    Unknown1099(3)
    physicsYImpulse(70)

@State
def rynef450_GroundShockwave_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1096(1400)
        Unknown1099(100)
        Unknown3000(0)
        Unknown4061(4)
        Unknown23015(11)
        Unknown1007(-20000)
    sprite('vref_ryn450_burst00b', 2)	# 1-2
    sprite('vref_ryn450_burst01b', 3)	# 3-5
    sprite('vref_ryn450_burst01b', 300)	# 6-305
    Unknown1099(2)
    physicsYImpulse(-30)

@State
def rynef450_Hit_Circle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3032()
        Unknown23015(13)
        Unknown1096(3000)
        Unknown1090(40)
    sprite('null', 5)	# 1-5
    Unknown4003('72796e65663435305f636972636c6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1059(300)
    Unknown1093(40)
    physicsYImpulse(1000)
    sprite('null', 300)	# 6-305
    Unknown4003('72796e65663435305f636972636c6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1101(2)
    physicsYImpulse(50)

@State
def rynef450_GroundBloom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1099(50)
        Unknown4054(15)
        Unknown23067('rynef450_bloom')
        Unknown1099(200)
        Unknown1007(1000)
    sprite('null', 5)	# 1-5
    sprite('null', 300)	# 6-305
    Unknown1099(1)

@State
def rynef450_GroundBloomB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1099(50)
        Unknown4054(8)
        Unknown23067('rynef450_bloomB')
        Unknown1099(200)
        Unknown1007(1000)
    sprite('null', 5)	# 1-5
    sprite('null', 300)	# 6-305
    Unknown1099(1)

@State
def rynef450_SmokeB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(50000)
        Unknown1096(0)
        Unknown23067('rynef450_smokeB')
    sprite('null', 1)	# 1-1
    sprite('null', 4)	# 2-5
    Unknown1096(600)
    Unknown1099(100)
    physicsYImpulse(30000)
    sprite('null', 400)	# 6-405
    Unknown1099(0)
    Unknown1084(1)

@Subroutine
def rynef450_Glass_Func():
    Unknown4007(2)
    Unknown21010(1)
    Unknown4010(2)
    Unknown3033()
    Unknown23118(-20416)

@Subroutine
def rynef450_Glass_Slow():
    Unknown1019(1)
    YAccel(1)
    Unknown19009(1)
    Unknown1076(2)
    Unknown1101(1)

@State
def rynef450_Glass00():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(1200, 400)
        teleportRelativeY(-60000)
        Unknown1025(50000, -50000)
        Unknown1026(90000, 10000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(6)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown1103(200, 100)
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(200)
    YAccel(200)
    Unknown1101(500)

@State
def rynef450_Glass01():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(1200, 400)
        teleportRelativeY(-60000)
        Unknown1025(50000, 90000)
        Unknown1026(90000, 10000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(6)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown1103(200, 100)
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(200)
    YAccel(200)
    Unknown1101(500)

@State
def rynef450_Glass02():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(1200, 400)
        teleportRelativeY(-60000)
        Unknown1025(-50000, -90000)
        Unknown1026(90000, 10000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(6)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown1103(200, 100)
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(200)
    YAccel(200)
    Unknown1101(500)

@State
def rynef450_Glass03():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(900, 3)
        teleportRelativeY(-100000)
        Unknown1025(-90000, 90000)
        Unknown1026(20000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(12)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown1103(200, 100)
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(50)
    YAccel(50)

@State
def rynef450_Glass10():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(800, -200)
        teleportRelativeY(-60000)
        Unknown1025(150000, 0)
        Unknown1026(110000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(6)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(80)
    YAccel(80)

@State
def rynef450_Glass11():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(800, -200)
        teleportRelativeY(-60000)
        Unknown1025(0, -150000)
        Unknown1026(110000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(6)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(80)
    YAccel(80)

@State
def rynef450_Glass20():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(500, 0)
        teleportRelativeY(-100000)
        Unknown1025(60000, -60000)
        Unknown1026(90000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(12)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown1103(-200, -50)
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(50)
    YAccel(50)

@State
def rynef450_Glass21():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(500, 0)
        teleportRelativeY(-100000)
        Unknown1025(120000, 60000)
        Unknown1026(90000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(12)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown1103(-200, -50)
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(50)
    YAccel(50)

@State
def rynef450_Glass22():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(500, 0)
        teleportRelativeY(-100000)
        Unknown1025(-120000, -60000)
        Unknown1026(90000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(10000, -10000)
        Unknown23015(12)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown1103(-200, -50)
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')
    Unknown1019(50)
    YAccel(50)

@State
def rynef450_Glass30():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1102(-500, 0)
        teleportRelativeY(-100000)
        Unknown1025(-90000, 90000)
        Unknown1026(150000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(20000, -20000)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')

@State
def rynef450_Glass31():

    def upon_IMMEDIATE():
        callSubroutine('rynef450_Glass_Func')
        Unknown4003('72796e65663435305f676c61737330322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1062(-600, -400)
        Unknown1070(-600, -400)
        teleportRelativeY(-100000)
        Unknown1025(-90000, 90000)
        Unknown1026(150000, 5000)
        Unknown1077(0, 360000)
        Unknown1078(20000, -20000)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 4)	# 2-5
    Unknown3001(255)
    sprite('null', 300)	# 6-305
    callSubroutine('rynef450_Glass_Slow')

@State
def rynef450_LineWind():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663435305f6c696e6577696e6430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown23015(10)
        Unknown3033()
        Unknown1096(4500)
        Unknown3001(0)
        Unknown1007(200000)
    sprite('null', 2)	# 1-2
    sprite('null', 3)	# 3-5
    Unknown3004(46)
    sprite('null', 300)	# 6-305
    Unknown3004(0)

@State
def rynef450_LineWind_b():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663435305f6c696e6577696e643030622e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown23015(15)
        Unknown3033()
        Unknown1096(4500)
        Unknown3001(0)
        Unknown1007(220000)
    sprite('null', 2)	# 1-2
    sprite('null', 3)	# 3-5
    Unknown3004(46)
    sprite('null', 300)	# 6-305
    Unknown3004(0)

@State
def rynef450_ScreenFire():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663435305f73637265656e5f666972652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown23015(1)
        Unknown3033()
        Unknown1096(2600)
        Unknown3001(0)
        Unknown6001(1)

        def upon_CLEAR_OR_EXIT():
            Unknown23057(50)
            Unknown23058(50)
    sprite('null', 5)	# 1-5
    Unknown3004(52)
    Unknown1099(2)
    physicsYImpulse(50)
    sprite('null', 300)	# 6-305
    Unknown3004(0)

@State
def rynef450_BG():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663435305f62673030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown23015(2)
        Unknown3032()
        Unknown1096(2700)
        Unknown1099(1)
        Unknown3001(0)
        Unknown6001(1)

        def upon_CLEAR_OR_EXIT():
            Unknown23057(50)
            Unknown23058(50)
    sprite('null', 5)	# 1-5
    Unknown3004(52)
    sprite('null', 300)	# 6-305
    Unknown3004(0)

@State
def rynef450_WhiteOut():

    def upon_IMMEDIATE():
        Unknown4003('72796e65663435305f77686974656f75742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown2054(1)
        Unknown21010(1)
        Unknown4011(3)
        Unknown23015(1)
        Unknown3033()
        Unknown1096(2700)
        Unknown1064(3200)
        Unknown3026(-16777216)
        Unknown23118(-16777216)

        def upon_CLEAR_OR_EXIT():
            Unknown23057(50)
            Unknown23058(80)
    sprite('null', 20)	# 1-20
    Unknown3010(5)
    Unknown3016(5)
    Unknown3022(5)
    sprite('null', 10)	# 21-30
    Unknown3010(9)
    Unknown3016(9)
    Unknown3022(9)
    sprite('null', 6)	# 31-36
    Unknown3010(11)
    Unknown3016(11)
    Unknown3022(11)
    sprite('null', 10)	# 37-46
    Unknown23102(7)
    Unknown23108(7)
    Unknown23114(7)
    sprite('null', 30)	# 47-76
    Unknown23102(9)
    Unknown23108(9)
    Unknown23114(9)
    sprite('null', 180)	# 77-256
    Unknown3026(-1)
    Unknown23118(-1)
    sprite('null', 120)	# 257-376
    Unknown3004(-8)

@State
def rynef450_End():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1007(100000)
    sprite('null', 70)	# 1-70
    sprite('null', 300)	# 71-370
    GFX_2('rynef450_smoke_end')

@State
def AstralFirstCamera():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2053(0)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('0300000000000000000000001900000000000000')

        def upon_43():
            if (SLOT_48 == 4501):
                clearUponHandler(43)
                sendToLabel(1)
    label(0)
    sprite('null', 600)	# 1-600
    Unknown20000(1)
    Unknown20001(1)
    Unknown20003(1)
    label(1)
    sprite('null', 1)	# 601-601
    Unknown20000(0)
    Unknown20001(0)
    Unknown20003(0)

@State
def AstralAtkFinal():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown3038(1)
        Unknown2034(0)
        Unknown2053(0)
        AttackLevel_(5)
        Damage(1000)
        AirUntechableTime(180)
        Hitstop(0)
        Unknown11064(1)
        Unknown11023(1)
        Unknown11067(1)
        Unknown11072(1, 100000, 100000)
        Unknown9266(1)
        AirPushbackX(1250)
        AirPushbackY(1250)
        YImpluseBeforeWallbounce(5)
        MinimumDamagePct(100)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1500)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(22)
    sprite('vref_ryn_addatk', 180)	# 1-180	 **attackbox here**
    RefreshMultihit()
    sprite('vref_ryn_addatk', 3)	# 181-183	 **attackbox here**
    RefreshMultihit()
    Damage(28500)
    Unknown11064(3)
    AirPushbackX(25000)
    AirPushbackY(50000)
    Unknown9095()
    Unknown11072(0, 0, 0)