@State
def RifleShotA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown11001(10, 10, 15)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEff_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(3000)
        Unknown1064(2000)
        physicsXImpulse(150000)
    sprite('RifleShotAtk', 60)	# 1-60	 **attackbox here**
    GFX_0('rrbBulletEff', 0)

@State
def RifleShotB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown11001(10, 10, 15)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEff_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(3000)
        Unknown1064(2000)
        physicsXImpulse(150000)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('RifleShotAtk', 60)	# 1-60	 **attackbox here**
    GFX_0('rrbBulletEff', 0)

@State
def RifleShotEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown11001(10, 10, 15)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown30065(0)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEff_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(3000)
        Unknown1064(2000)
        physicsXImpulse(150000)
    sprite('RifleShotAtk', 60)	# 1-60	 **attackbox here**
    GFX_0('rrbBulletEff', 0)

@State
def AirRollingShot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11068(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
        Unknown53(1)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('AirShotAtk', 4)	# 1-4	 **attackbox here**

@State
def AirRollingShotEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(36)
        Hitstop(2)
        Unknown11001(10, 0, 5)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown30065(0)
        Unknown11091(10)
        Unknown11068(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
        Unknown53(1)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('AirShotAtk', 4)	# 1-4	 **attackbox here**
    sprite('RifleShotAtk', 60)	# 5-64	 **attackbox here**
    teleportRelativeX(-150000)
    Unknown1056(3000)
    Unknown1064(2000)
    physicsXImpulse(150000)
    GFX_0('rrbBulletEff', 0)
    clearUponHandler(54)

    def upon_54():
        Unknown13(25)
        GFX_0('rrbBulletEff_Break', 0)

@State
def RollingShot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(36)
        Hitstop(2)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown23182(3)
        Unknown11108('03000000')
        Unknown30065(0)
        Unknown11091(10)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
        teleportRelativeX(440000)
        Unknown1007(250000)
        Unknown53(1)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('AirShotAtk', 4)	# 1-4	 **attackbox here**

@State
def RollingShotASS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(30000)
        AirUntechableTime(36)
        Hitstop(2)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11042(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
        teleportRelativeX(340000)
        Unknown1007(250000)
        Unknown53(1)
    sprite('AirShotAtk', 4)	# 1-4	 **attackbox here**

@State
def ShotAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(20000)
        PushbackX(30400)
        AirUntechableTime(30)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEffB_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        physicsXImpulse(80000)

        def upon_12():
            Unknown23029(3, 3001, 0)
    sprite('ShotAtk', 60)	# 1-60	 **attackbox here**
    GFX_0('rrbBulletEffB', 0)

@State
def ShotAtk_Assist():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        AttackP1(70)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Unknown11042(1)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')

        def upon_54():
            Unknown13(25)
            GFX_0('rrbBulletEffB_Break', 0)
        Unknown53(1)
        teleportRelativeX(-150000)
        physicsXImpulse(80000)
    sprite('ShotAtk', 60)	# 1-60	 **attackbox here**
    GFX_0('rrbBulletEffB', 0)

@State
def UltimateAssault_AddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(720)
        AttackP2(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11069('UltimateAssault_AddAtk')
        Hitstop(0)
        Unknown11001(0, 0, 0)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11091(30)

        def upon_43():
            if (SLOT_48 == 4312):
                Damage(300)
                Unknown11091(100)
                AttackP1(100)
                AttackP2(100)
                Unknown2037(1)
    sprite('RifleShotAtk', 5)	# 1-5	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)	# 6-10	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)	# 11-15	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)	# 16-20	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)	# 21-25	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)	# 26-30	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)	# 31-35	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    if SLOT_2:
        AttackP2(100)
        Damage(450)
    else:
        AttackP2(60)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(40000)
    AirPushbackY(40000)
    Unknown9202(20)
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)

    def upon_78():
        Unknown23029(3, 4311, 0)

@State
def UltimateAssaultOD_AddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(600)
        AttackP2(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11069('UltimateAssaultOD_AddAtk')
        Hitstop(0)
        Unknown11001(0, 0, 0)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11091(27)

        def upon_43():
            if (SLOT_48 == 4312):
                Damage(240)
                Unknown11091(100)
                AttackP1(100)
                AttackP2(100)
                Unknown2037(1)
    sprite('RifleShotAtk', 3)	# 1-3	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 4-6	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 7-9	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 10-12	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 13-15	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 16-18	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 19-21	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 22-24	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 25-27	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 3)	# 28-30	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('RifleShotAtk', 5)	# 31-35	 **attackbox here**
    Unknown23151(22, 105)
    RefreshMultihit()
    if SLOT_2:
        AttackP2(100)
        Damage(300)
    else:
        AttackP2(60)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(40000)
    AirPushbackY(40000)
    Unknown9202(20)
    Unknown11064(0)
    Unknown11069('')
    clearUponHandler(78)

    def upon_78():
        Unknown23029(3, 4311, 0)

@State
def rrbHitEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 1)	# 1-1
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6869745f706574616c000000000000000000000000000000000000000000')

@State
def rrbHitEff_Slash():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
    sprite('null', 1)	# 1-1
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6869745f706574616c000000000000000000000000000000000000000000')

@State
def rrbHitPetal_Burst():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 1)	# 1-1
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f706574616c5f627572737400000000000000000000000000000000000000')

@State
def rrbHitPetal_Add():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 1)	# 1-1
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6869745f706574616c420000000000000000000000000000000000000000')

@State
def rrbMuzzleEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
    sprite('null', 12)	# 1-12
    GFX_2('rrbef_muzzle')
    GFX_0('rrbMuzzleEff2', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff2():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f6d757a7a6c6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4000)
        Unknown1064(5500)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(1)
    sprite('null', 6)	# 1-6
    sprite('null', 1)	# 7-7
    Unknown3001(180)
    sprite('null', 1)	# 8-8
    Unknown3001(128)

@State
def rrbMuzzleEff_B():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
        Unknown1096(900)
    sprite('null', 12)	# 1-12
    GFX_2('rrbef_muzzle')
    GFX_0('rrbMuzzleEff_B2', 0)
    GFX_0('rrbMuzzleEff_B3', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff_B2():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f6d757a7a6c6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(4000)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(1)
    sprite('null', 6)	# 1-6
    sprite('null', 1)	# 7-7
    Unknown3001(180)
    sprite('null', 1)	# 8-8
    Unknown3001(128)

@State
def rrbMuzzleEff_B3():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown23015(1)
        Unknown3000(0)
        Unknown4061(5)
        Unknown1064(1300)
        Unknown1056(1100)
        Unknown1067(-20)
        Unknown1059(20)
        Unknown1073(180000)
    sprite('vrrrbef_muzzle01', 4)	# 1-4
    sprite('vrrrbef_muzzle02', 1)	# 5-5
    sprite('vrrrbef_muzzle03', 1)	# 6-6
    sprite('vrrrbef_muzzle04', 2)	# 7-8
    Unknown1064(700)
    Unknown1059(5)
    sprite('vrrrbef_muzzle05', 2)	# 9-10

@State
def rrbMuzzleEff_C():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
    sprite('null', 12)	# 1-12
    Unknown4054(12)
    Unknown23067('rrbef_muzzle')
    GFX_0('rrbMuzzleEff_C2', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff_C2():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f6d757a7a6c6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4000)
        Unknown1064(5500)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(12)
    sprite('null', 6)	# 1-6
    sprite('null', 1)	# 7-7
    Unknown3001(180)
    sprite('null', 1)	# 8-8
    Unknown3001(128)

@State
def rrbBulletEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(150000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 1)	# 1-1
    GFX_0('rrbef_bullet_head2', 0)
    GFX_0('rrbef_bullet_head', 0)
    GFX_0('rrbef_bullet_wind01', 0)
    GFX_0('rrbef_bullet_wind02', 0)
    GFX_0('rrbef_bullet_glow', 0)
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)	# 2-2
    GFX_1('rrbef_bullet_dust', 0)
    label(0)
    sprite('null', 1)	# 3-3
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)	# 4-4
    GFX_1('rrbef_bullet_dust', 0)
    GFX_1('rrbef_bullet_ring', 0)
    gotoLabel(0)

@State
def rrbef_bullet_head():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65742e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1096(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_head2():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f4e6f726d616c2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_wind01():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(4000)
        Unknown1064(4000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_wind02():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1096(6000)
        Unknown1064(3000)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_glow():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f676c6f772e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(6000)
        Unknown1064(1800)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbBulletEff_Break():

    def upon_IMMEDIATE():
        Unknown4007(2)
        teleportRelativeX(200000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 8)	# 1-8
    GFX_0('rrbef_bullet_head2_Break', 0)
    GFX_0('rrbef_bullet_head_Break', 0)
    GFX_0('rrbef_bullet_wind01_Break', 0)
    GFX_0('rrbef_bullet_wind02_Break', 0)
    GFX_0('rrbef_bullet_glow_Break', 0)

@State
def rrbef_bullet_head_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65742e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1056(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 6)	# 1-6
    Unknown1067(-1500)
    Unknown1059(-1000)

@State
def rrbef_bullet_head2_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f4e6f726d616c2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(8000)
        Unknown1064(12000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 6)	# 1-6
    Unknown1067(-1500)
    Unknown1059(-1000)

@State
def rrbef_bullet_wind01_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(4000)
        Unknown1064(4000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 8)	# 1-8
    Unknown1067(700)

@State
def rrbef_bullet_wind02_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(6000)
        Unknown1064(3000)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 6)	# 1-6
    Unknown1067(600)

@State
def rrbef_bullet_glow_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f676c6f772e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(6000)
        Unknown1064(1800)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(70)
    sprite('null', 6)	# 1-6

@State
def rrbBulletEffB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(150000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 1)	# 1-1
    GFX_0('rrbef_bullet_head2B', 0)
    GFX_0('rrbef_bullet_headB', 0)
    GFX_0('rrbef_bullet_wind01B', 0)
    GFX_0('rrbef_bullet_wind02B', 0)
    GFX_0('rrbef_bullet_glowB', 0)
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)	# 2-2
    GFX_1('rrbef_bullet_dust', 0)
    label(0)
    sprite('null', 1)	# 3-3
    GFX_1('rrbef_bullet_dust', 0)
    sprite('null', 1)	# 4-4
    GFX_1('rrbef_bullet_dust', 0)
    GFX_1('rrbef_bullet_ringB', 0)
    gotoLabel(0)

@State
def rrbef_bullet_headB():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65742e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1096(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_head2B():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f4e6f726d616c2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_wind01B():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(3000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_wind02B():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(2250)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbef_bullet_glowB():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f676c6f772e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(4500)
        Unknown1064(1350)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 1)	# 1-1
    Unknown1058(25)
    sprite('null', 59)	# 2-60
    Unknown1058(400)

@State
def rrbBulletEffB_Break():

    def upon_IMMEDIATE():
        Unknown4007(2)
        teleportRelativeX(200000)
        Unknown1007(0)
        Unknown2055(60)

        def upon_30():
            Unknown3001(0)
    sprite('null', 8)	# 1-8
    GFX_0('rrbef_bullet_head2B_Break', 0)
    GFX_0('rrbef_bullet_headB_Break', 0)
    GFX_0('rrbef_bullet_wind01B_Break', 0)
    GFX_0('rrbef_bullet_wind02B_Break', 0)
    GFX_0('rrbef_bullet_glowB_Break', 0)

@State
def rrbef_bullet_headB_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65742e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3033()
        Unknown1056(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(180)
        Unknown3013(200)
    sprite('null', 6)	# 1-6
    Unknown1059(-750)
    Unknown1067(-1125)

@State
def rrbef_bullet_head2B_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f4e6f726d616c2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown3032()
        Unknown1096(6000)
        Unknown1064(9000)
        Unknown1072(180000)
        Unknown3007(60)
        Unknown3013(100)
    sprite('null', 6)	# 1-6
    Unknown1059(-750)
    Unknown1067(-1125)

@State
def rrbef_bullet_wind01B_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown1096(3000)
        Unknown1064(3000)
        Unknown3033()
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 8)	# 1-8
    Unknown1067(500)

@State
def rrbef_bullet_wind02B_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f62756c6c65745f77696e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4025(2)
        Unknown53(1)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(2250)
        Unknown1072(180000)
        Unknown3003(50)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(80)
    sprite('null', 6)	# 1-6
    Unknown1067(450)

@State
def rrbef_bullet_glowB_Break():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f676c6f772e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(3)
        Unknown4025(2)
        Unknown53(1)
        teleportRelativeX(-150000)
        Unknown1056(4500)
        Unknown1064(1350)
        Unknown1102(100, 0)
        Unknown3007(60)
        Unknown3013(100)

        def upon_3():
            Unknown3003(70)
    sprite('null', 6)	# 1-6

@State
def rrbCaseEff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)	# 1-60
    GFX_2('rrbef_case')

@State
def rrbCaseEffB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)	# 1-60
    GFX_2('rrbef_caseB')

@State
def rrbCaseEffC():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)	# 1-60
    Unknown4054(12)
    Unknown23067('rrbef_caseC')

@State
def rrbCaseEffD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1056(900)
        Unknown1064(800)
    sprite('null', 60)	# 1-60
    Unknown4054(12)
    Unknown23067('rrbef_caseD')

@State
def rrbGroundEff():

    def upon_IMMEDIATE():
        Unknown1064(700)
        teleportRelativeX(180000)
        teleportRelativeY(-18000)
        Unknown3033()
        Unknown3000(0)
        Unknown4061(5)
        Unknown23015(1)
    sprite('vrrrbef_ground01', 2)	# 1-2
    sprite('vrrrbef_ground02', 2)	# 3-4
    sprite('vrrrbef_ground03', 2)	# 5-6
    sprite('vrrrbef_ground04', 2)	# 7-8
    Unknown3004(-42)
    sprite('vrrrbef_ground05', 2)	# 9-10

@State
def rrb201Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(15000)
        Unknown1007(240000)
    sprite('null', 10)	# 1-10
    GFX_0('rrb201Eff_2', 0)
    GFX_0('rrb201Eff_1', 0)
    GFX_0('rrb201Eff_3', 0)

@State
def rrb201Eff_1():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown4003('72726265663230315f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(3800)
    sprite('null', 10)	# 1-10

@State
def rrb201Eff_2():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown4003('72726265663230315f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(3800)
    sprite('null', 10)	# 1-10

@State
def rrb201Eff_3():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp03')
        Unknown4003('72726265663230315f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(4200)
        Unknown1099(20)
        Unknown3001(90)
        Unknown3004(-11)
    sprite('null', 12)	# 1-12

@State
def rrb202Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-15000)
        Unknown1007(230000)
    sprite('null', 10)	# 1-10
    GFX_0('rrb202Eff_2', 0)
    GFX_0('rrb202Eff_1', 0)
    GFX_0('rrb202Eff_3', 0)

@State
def rrb202Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663230325f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3800)
    sprite('null', 14)	# 1-14

@State
def rrb202Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663230325f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3800)
    sprite('null', 14)	# 1-14

@State
def rrb202Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663230325f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4150)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 12)	# 1-12

@State
def rrb203Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(305000)
        Unknown1096(3700)
    sprite('null', 10)	# 1-10
    GFX_0('rrb203Eff_2', 0)
    GFX_0('rrb203Eff_1', 0)
    GFX_0('rrb203Eff_3', 0)

@State
def rrb203Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663230335f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb203Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663230335f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb203Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663230335f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 8)	# 1-8

@State
def rrb231Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-35000)
        Unknown1007(165000)
    sprite('null', 50)	# 1-50
    GFX_0('rrb231Eff_2', 0)
    GFX_0('rrb231Eff_1', 0)
    GFX_0('rrb231Eff_3', 0)

@State
def rrb231Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663233315f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 12)	# 1-12

@State
def rrb231Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663233315f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 12)	# 1-12

@State
def rrb231Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663233315f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4100)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 12)	# 1-12

@State
def rrb232Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(80000)
    sprite('null', 50)	# 1-50
    GFX_0('rrb232Eff_2', 0)
    GFX_0('rrb232Eff_1', 0)
    GFX_0('rrb232Eff_3', 0)

@State
def rrb232Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663233325f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 16)	# 1-16

@State
def rrb232Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663233325f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 16)	# 1-16

@State
def rrb232Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663233325f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3700)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 16)	# 1-16

@State
def rrb251Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(280000)
    sprite('null', 50)	# 1-50
    GFX_0('rrb251Eff_2', 0)
    GFX_0('rrb251Eff_1', 0)
    GFX_0('rrb251Eff_3', 0)

@State
def rrb251Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663235315f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3600)
    sprite('null', 8)	# 1-8

@State
def rrb251Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663235315f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3600)
    sprite('null', 8)	# 1-8

@State
def rrb251Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663235315f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4000)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 10)	# 1-10

@State
def rrb252Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(0)
        Unknown1007(270000)
    sprite('null', 50)	# 1-50
    GFX_0('rrb252Eff_2', 0)
    GFX_0('rrb252Eff_1', 0)
    GFX_0('rrb252Eff_3', 0)

@State
def rrb252Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663235325f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 10)	# 1-10

@State
def rrb252Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663235325f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 10)	# 1-10

@State
def rrb252Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663235325f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4100)
        Unknown3001(90)
        Unknown3004(-10)
    sprite('null', 10)	# 1-10

@State
def rrb270Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(7000)
        Unknown1007(245000)
    sprite('null', 9)	# 1-9
    GFX_0('rrb270Eff_1', 0)
    GFX_0('rrb270Eff_2', 0)
    GFX_0('rrb270Eff_3', 0)

@State
def rrb270Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663237305f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3800)
    sprite('null', 9)	# 1-9

@State
def rrb270Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663237305f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3800)
    sprite('null', 9)	# 1-9

@State
def rrb270Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663237305f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3900)
        Unknown3001(90)
    sprite('null', 9)	# 1-9

@State
def rrb271Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-100000)
        Unknown1007(15000)
    sprite('null', 4)	# 1-4
    GFX_0('rrb271Eff_1', 0)
    GFX_0('rrb271Eff_2', 0)
    GFX_0('rrb271Eff_3', 0)
    sprite('null', 14)	# 5-18
    GFX_0('rrb271GroundEff', 0)

@State
def rrb271Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663237315f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 14)	# 1-14

@State
def rrb271Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663237315f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 14)	# 1-14

@State
def rrb271Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663237315f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3700)
        Unknown3001(90)
    sprite('null', 14)	# 1-14

@State
def rrb271GroundEff():

    def upon_IMMEDIATE():
        teleportRelativeX(360000)
        teleportRelativeY(0)
    sprite('null', 2)	# 1-2
    Unknown8003(100, 1, 1)

@State
def rrb311Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown4009(0)
        teleportRelativeX(2000)
        Unknown1007(270000)
    sprite('null', 26)	# 1-26
    GFX_0('rrb311Eff_2', 0)
    GFX_0('rrb311Eff_1', 0)
    GFX_0('rrb311Eff_3', 0)
    GFX_0('rrb311MuzzleEff', 0)
    Unknown35()

@State
def rrb311Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663331315f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3800)
    sprite('null', 17)	# 1-17

@State
def rrb311Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663331315f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3800)
    sprite('null', 17)	# 1-17

@State
def rrb311Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663331315f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4200)
        Unknown3001(90)
    sprite('null', 7)	# 1-7
    sprite('null', 9)	# 8-16
    Unknown3004(-10)

@State
def rrb311MuzzleEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeX(300000)
        Unknown1007(25000)
        Unknown1073(60000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb311EndEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1000(-65000)
        teleportRelativeY(285000)
        Unknown4061(6)
        Unknown21004(1)
        Unknown1096(2470)
    sprite('null', 2)	# 1-2
    Unknown4003('72726265663630315f30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72726265663630315f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72726265663630315f30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown4003('72726265663630315f30352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 9-10
    Unknown4003('72726265663630315f30362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown4003('72726265663630315f30372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72726265663630315f30382e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 15-16
    Unknown4003('72726265663630315f30392e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb312Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(10000)
        Unknown1007(260000)
        Unknown1096(3800)
    sprite('null', 11)	# 1-11
    GFX_0('rrb312Eff_2', 0)
    GFX_0('rrb312Eff_1', 0)
    GFX_0('rrb312Eff_3', 0)

@State
def rrb312Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663331325f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 11)	# 1-11

@State
def rrb312Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663331325f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 11)	# 1-11

@State
def rrb312Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663331325f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(90)
        Unknown3004(-5)
    sprite('null', 8)	# 1-8

@State
def rrb312MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-170000)
        Unknown1007(-170000)
        Unknown1072(-140000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb400MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-180000)
        Unknown1007(200000)
        Unknown1072(-100000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb400PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown1007(170000)
        Unknown2055(30)
        sendToLabelUpon(32, 1)
    sprite('null', 2)	# 1-2
    sprite('null', 1)	# 3-3
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    label(0)
    sprite('null', 1)	# 5-5
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    gotoLabel(0)
    label(1)
    sprite('null', 3)	# 6-8
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c5f656e6400000000000000000000000000000000')
    sprite('null', 3)	# 9-11
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')

@State
def rrb400AirPetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(10000)
        Unknown1007(180000)
        Unknown2055(30)
        sendToLabelUpon(32, 1)
    sprite('null', 2)	# 1-2
    label(0)
    sprite('null', 1)	# 3-3
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    gotoLabel(0)
    label(1)
    sprite('null', 3)	# 4-6
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')

@State
def rrb401MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(250000)
        Unknown1007(220000)
        Unknown1072(90000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb401PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown2055(30)
        Unknown1007(30000)
        Unknown1007(150000)
        sendToLabelUpon(32, 1)
    sprite('null', 2)	# 1-2
    sprite('null', 1)	# 3-3
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 1)	# 4-4
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    label(0)
    sprite('null', 1)	# 5-5
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    Unknown4051(0)
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 6-6
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    Unknown4051(0)
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    sprite('null', 1)	# 7-7
    Unknown4051(0)
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    gotoLabel(0)
    label(1)
    sprite('null', 3)	# 8-10
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4051(0)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')

@State
def rrb402MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-120000)
        Unknown1007(35000)
        Unknown1072(-140000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb402PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown2055(30)
        Unknown1000(20000)
        teleportRelativeY(180000)
        sendToLabelUpon(32, 1)
    sprite('null', 2)	# 1-2
    label(0)
    sprite('null', 1)	# 3-3
    Unknown4048(-10000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    Unknown4048(-37000)
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    gotoLabel(0)
    label(1)
    sprite('null', 3)	# 4-6
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 20)	# 13-32

@State
def rrb403MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-160000)
        Unknown1007(380000)
        Unknown1072(-60000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb403PetalEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown2055(60)
        Unknown1000(-40000)
        teleportRelativeY(180000)
        sendToLabelUpon(32, 1)
    sprite('null', 2)	# 1-2
    label(0)
    sprite('null', 1)	# 3-3
    Unknown4048(20000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    Unknown4048(40000)
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    gotoLabel(0)
    label(1)
    sprite('null', 3)	# 4-6
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4048(90000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    sprite('null', 20)	# 13-32

@State
def rrb404Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-5000)
        Unknown1007(265000)
    sprite('null', 6)	# 1-6
    GFX_0('rrb404Eff_2', 0)
    GFX_0('rrb404Eff_1', 0)
    GFX_0('rrb404Eff_3', 0)
    GFX_0('rrb404Eff_4', 0)
    sprite('null', 20)	# 7-26
    GFX_0('rrbGroundEff', 0)

@State
def rrb404Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430345f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 14)	# 1-14

@State
def rrb404Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430345f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 14)	# 1-14

@State
def rrb404Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430345f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown1096(3700)
        Unknown3001(90)
    sprite('null', 6)	# 1-6
    sprite('null', 9)	# 7-15
    Unknown3004(-10)

@State
def rrb404Eff_4():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430345f342e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown1096(3700)
    sprite('null', 14)	# 1-14

@State
def rrb404EndEff():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430345f656e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        teleportRelativeX(-40000)
        Unknown1007(270000)
        Unknown1096(2200)
    sprite('null', 12)	# 1-12

@State
def rrb404MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(145000)
        Unknown1007(5000)
        Unknown1072(90000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)
    GFX_0('rrb404Smoke', 0)

@State
def rrb404MuzzleEff_B():

    def upon_IMMEDIATE():
        teleportRelativeX(145000)
        Unknown1007(5000)
        Unknown1072(92000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_B', 0)
    GFX_0('rrb404Smoke', 0)

@State
def rrb404Smoke():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeY(-10000)
        Unknown1096(500)
        Unknown1064(400)
        Unknown1099(20)
        physicsXImpulse(-5000)
    sprite('vrrrbef_smokeb01', 2)	# 1-2
    sprite('vrrrbef_smokeb02', 2)	# 3-4
    sprite('vrrrbef_smokeb03', 2)	# 5-6
    sprite('vrrrbef_smokeb04', 3)	# 7-9
    sprite('vrrrbef_smokeb05', 3)	# 10-12
    Unknown3004(-28)
    sprite('vrrrbef_smokeb06', 3)	# 13-15
    sprite('vrrrbef_smokeb07', 3)	# 16-18

@State
def rrb405Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
    sprite('null', 2)	# 1-2
    GFX_0('rrb405_Particle', 0)
    GFX_0('rrb405_Smoke', 0)
    GFX_0('rrb405MuzzleEff', 0)

    def upon_IMMEDIATE():
        teleportRelativeX(-160000)
        Unknown1007(380000)
        Unknown1072(-60000)
    sprite('null', 20)	# 3-22
sprite('null', 14)	# 23-36
GFX_0('rrb405_Ani', 0)
endState()

@State
def rrb405_Ani():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4061(0)
        teleportRelativeX(100000)
        Unknown3032()
    sprite('vrrrbef405_01', 2)	# 1-2
    sprite('vrrrbef405_02', 2)	# 3-4
    sprite('vrrrbef405_03', 2)	# 5-6

@State
def rrb405_Particle():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown2055(17)
        Unknown1007(200000)
    label(0)
    sprite('null', 1)	# 1-1
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    gotoLabel(0)

@State
def rrb405_Smoke():

    def upon_IMMEDIATE():
        teleportRelativeX(200000)
        Unknown4010(3)
        Unknown4011(3)
    sprite('null', 1)	# 1-1
    GFX_0('rrb405_RingSmokeB', 0)
    GFX_0('rrb405_DashSmoke', 0)
    sprite('null', 1)	# 2-2
    GFX_0('rrb405_RingSmokeA2', 0)
    sprite('null', 1)	# 3-3
    GFX_0('rrb405_RingSmokeA', 0)
    sprite('null', 1)	# 4-4
    GFX_0('rrb405_RingSmokeC', 0)
    sprite('null', 1)	# 5-5
    GFX_0('rrb405_RingSmokeB2', 0)

@State
def rrb405_DashSmoke():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown1096(400)
        Unknown1064(300)
        Unknown1099(15)
        teleportRelativeX(-100000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_smoke01', 3)	# 1-3
    sprite('vrrrbef_smoke02', 3)	# 4-6
    sprite('vrrrbef_smoke03', 3)	# 7-9
    sprite('vrrrbef_smoke04', 3)	# 10-12
    sprite('vrrrbef_smoke05', 3)	# 13-15
    sprite('vrrrbef_smoke06', 3)	# 16-18

@State
def rrb405_RingSmokeA():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
    sprite('vrrrbef_ringsmokea01', 1)	# 1-1
    Unknown1096(700)
    sprite('vrrrbef_ringsmokea01', 2)	# 2-3
    Unknown1096(780)
    Unknown1099(25)
    sprite('vrrrbef_ringsmokea02', 3)	# 4-6
    sprite('vrrrbef_ringsmokea03', 3)	# 7-9
    sprite('vrrrbef_ringsmokea04', 3)	# 10-12

@State
def rrb405_RingSmokeA2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeX(-180000)
        physicsXImpulse(-3000)
    sprite('vrrrbef_ringsmokea01', 1)	# 1-1
    Unknown1096(500)
    sprite('vrrrbef_ringsmokea01', 3)	# 2-4
    Unknown1096(600)
    Unknown1099(10)
    sprite('vrrrbef_ringsmokea02', 4)	# 5-8
    sprite('vrrrbef_ringsmokea03', 4)	# 9-12
    sprite('vrrrbef_ringsmokea04', 4)	# 13-16

@State
def rrb405_RingSmokeB():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeX(-250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokeb01', 1)	# 1-1
    Unknown1096(500)
    sprite('vrrrbef_ringsmokeb01', 2)	# 2-3
    Unknown1096(600)
    Unknown1099(15)
    sprite('vrrrbef_ringsmokeb02', 3)	# 4-6
    sprite('vrrrbef_ringsmokeb03', 3)	# 7-9
    sprite('vrrrbef_ringsmokeb04', 3)	# 10-12

@State
def rrb405_RingSmokeB2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        teleportRelativeX(100000)
    sprite('vrrrbef_ringsmokeb01', 1)	# 1-1
    Unknown1096(450)
    sprite('vrrrbef_ringsmokeb01', 2)	# 2-3
    Unknown1096(550)
    Unknown1099(5)
    sprite('vrrrbef_ringsmokeb02', 3)	# 4-6
    sprite('vrrrbef_ringsmokeb03', 3)	# 7-9
    sprite('vrrrbef_ringsmokeb04', 3)	# 10-12

@State
def rrb405_RingSmokeC():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown1096(700)
        teleportRelativeX(100000)
    sprite('vrrrbef_ringsmokec01', 1)	# 1-1
    Unknown1096(600)
    sprite('vrrrbef_ringsmokec01', 3)	# 2-4
    Unknown1096(700)
    Unknown1099(10)
    sprite('vrrrbef_ringsmokec02', 4)	# 5-8
    sprite('vrrrbef_ringsmokec03', 4)	# 9-12
    sprite('vrrrbef_ringsmokec04', 4)	# 13-16

@State
def rrb405_Particle():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown2055(17)
        Unknown1007(200000)
    label(0)
    sprite('null', 1)	# 1-1
    Unknown4047(9, 9, 9)
    Unknown4045('72726265665f6d6f76655f706574616c0000000000000000000000000000000000000000')
    Unknown4045('72726265665f737065656400000000000000000000000000000000000000000000000000')
    gotoLabel(0)

@State
def rrb405MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-200000)
        Unknown1007(160000)
        Unknown1072(-90000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb405_Issen():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown6001(1)

        def upon_16():
            Unknown23032(50)
    sprite('null', 40)	# 1-40
    GFX_0('rrb405_Issen01', 0)
    GFX_0('rrb405_Issen02', 0)

@State
def rrb405_Issen01():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown1007(200000)
        Unknown4061(6)
    sprite('null', 1)	# 1-1
    Unknown4047(1, 1, 1)
    Unknown23067('rrbef405_issen')
    teleportRelativeX(-800000)
    Unknown3001(255)
    Unknown1064(3000)
    sprite('null', 1)	# 2-2
    teleportRelativeX(800000)
    Unknown1064(3500)
    sprite('null', 1)	# 3-3
    teleportRelativeX(400000)
    Unknown1056(1300)
    Unknown1064(4000)
    sprite('null', 2)	# 4-5
    Unknown1064(3000)
    sprite('null', 3)	# 6-8
    Unknown1067(-800)
    sprite('null', 3)	# 9-11
    Unknown1067(-100)
    sprite('null', 5)	# 12-16
    Unknown1067(-40)
    sprite('null', 1)	# 17-17
    Unknown1067(-10)
    sprite('null', 1)	# 18-18
    Unknown1064(100)
    Unknown1067(-1)
    sprite('null', 2)	# 19-20
    Unknown3001(0)
    sprite('null', 2)	# 21-22
    Unknown3001(255)
    sprite('null', 1)	# 23-23
    Unknown3001(0)
    sprite('null', 1)	# 24-24
    Unknown3001(255)
    sprite('null', 2)	# 25-26
    Unknown3001(0)
    sprite('null', 2)	# 27-28
    Unknown3001(255)
    sprite('null', 2)	# 29-30
    Unknown3001(0)
    sprite('null', 1)	# 31-31
    Unknown3001(255)
    sprite('null', 2)	# 32-33
    Unknown3001(0)
    sprite('null', 1)	# 34-34
    Unknown3001(255)
    sprite('null', 2)	# 35-36
    Unknown3001(0)
    sprite('null', 1)	# 37-37
    Unknown3001(255)

@State
def rrb405_Issen02():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown4061(6)
        Unknown1007(200000)
    sprite('null', 1)	# 1-1
    Unknown4047(17, 1, 1)
    Unknown23067('rrbef405_issenB')
    teleportRelativeX(-800000)
    Unknown3001(255)
    Unknown1064(3000)
    sprite('null', 1)	# 2-2
    teleportRelativeX(800000)
    Unknown1064(3500)
    sprite('null', 1)	# 3-3
    teleportRelativeX(400000)
    Unknown1056(1300)
    Unknown1064(4000)
    sprite('null', 2)	# 4-5
    Unknown1064(3000)
    sprite('null', 3)	# 6-8
    Unknown1067(-800)
    sprite('null', 3)	# 9-11
    Unknown1067(-100)
    sprite('null', 5)	# 12-16
    Unknown1067(-40)
    sprite('null', 1)	# 17-17
    Unknown1067(-10)
    sprite('null', 1)	# 18-18
    Unknown1064(100)
    Unknown1067(-1)
    sprite('null', 2)	# 19-20
    Unknown3001(0)
    sprite('null', 2)	# 21-22
    Unknown3001(255)
    sprite('null', 1)	# 23-23
    Unknown3001(0)
    sprite('null', 1)	# 24-24
    Unknown3001(255)
    sprite('null', 2)	# 25-26
    Unknown3001(0)
    sprite('null', 2)	# 27-28
    Unknown3001(255)
    sprite('null', 2)	# 29-30
    Unknown3001(0)
    sprite('null', 1)	# 31-31
    Unknown3001(255)
    sprite('null', 2)	# 32-33
    Unknown3001(0)
    sprite('null', 1)	# 34-34
    Unknown3001(255)
    sprite('null', 2)	# 35-36
    Unknown3001(0)
    sprite('null', 1)	# 37-37
    Unknown3001(255)

@State
def rrb406aEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(30000)
        Unknown1007(220000)
        Unknown1096(3900)
        sendToLabelUpon(32, 1)
    sprite('null', 10)	# 1-10
    GFX_0('rrb406aEff_2', 0)
    GFX_0('rrb406aEff_1', 0)
    GFX_0('rrb406aEff_4', 0)
    GFX_0('rrb406aEff_3', 0)

@State
def rrb406aEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036615f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb406aEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036615f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb406aEff_3():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036615f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(90)
    sprite('null', 2)	# 1-2
    sprite('null', 8)	# 3-10
    Unknown3004(-5)

@State
def rrb406aEff_4():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036615f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb406bEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(40000)
        Unknown1007(220000)
        Unknown1096(3700)
        Unknown1072(0)
    sprite('null', 10)	# 1-10
    GFX_0('rrb406bEff_2', 0)
    GFX_0('rrb406bEff_1', 0)
    GFX_0('rrb406bEff_4', 0)
    GFX_0('rrb406bEff_3', 0)

@State
def rrb406bEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036625f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb406bEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036625f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb406bEff_3():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036625f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(70)
    sprite('null', 10)	# 1-10

@State
def rrb406bEff_4():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036625f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
        Unknown4006(2)
    sprite('null', 10)	# 1-10

@State
def rrb406cEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown4007(0)
        Unknown4022(3)
        teleportRelativeX(-250000)
        Unknown1007(-20000)
        Unknown1096(4200)
    sprite('null', 10)	# 1-10
    GFX_0('rrb406cEff_2', 0)
    GFX_0('rrb406cEff_1', 0)
    GFX_0('rrb406cEff_4', 0)
    GFX_0('rrb406cEff_3', 0)

@State
def rrb406cEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036635f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb406cEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036635f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb406cEff_3():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036635f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(70)
    sprite('null', 10)	# 1-10

@State
def rrb406cEff_4():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343036635f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
        Unknown4006(2)
    sprite('null', 10)	# 1-10

@State
def rrb406MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(340000)
        Unknown1007(250000)
        Unknown1072(85000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb407MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
        Unknown1007(5000)
        Unknown1072(90000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)
    GFX_0('rrb404Smoke', 0)

@State
def rrb407EndEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1000(-65000)
        teleportRelativeY(285000)
        Unknown4061(6)
        Unknown21004(1)
        Unknown1096(2470)
    sprite('null', 4)	# 1-4
    Unknown4003('72726265663630315f30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 5-8
    Unknown4003('72726265663630315f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 9-12
    Unknown4003('72726265663630315f30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown4003('72726265663630315f30352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 15-16
    Unknown4003('72726265663630315f30362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 17-18
    Unknown4003('72726265663630315f30372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 19-20
    Unknown4003('72726265663630315f30382e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 21-22
    Unknown4003('72726265663630315f30392e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-30000)
        Unknown1007(320000)
    sprite('null', 12)	# 1-12
    GFX_0('rrb408Eff_2', 0)
    GFX_0('rrb408Eff_1', 0)
    GFX_0('rrb408Eff_4', 0)
    GFX_0('rrb408Eff_3', 0)

@State
def rrb408Eff_1():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 4)	# 1-4
    Unknown4003('72726265663430385f315f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 5-8
    Unknown4003('72726265663430385f315f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 9-12
    Unknown4003('72726265663430385f315f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff_2():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 4)	# 1-4
    Unknown4003('72726265663430385f325f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 5-8
    Unknown4003('72726265663430385f325f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 9-12
    Unknown4003('72726265663430385f325f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff_3():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4300)
        Unknown3001(70)
    sprite('null', 4)	# 1-4
    Unknown4003('72726265663430385f335f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 5-8
    Unknown4003('72726265663430385f335f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 9-12
    Unknown4003('72726265663430385f335f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff_4():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown1096(3700)
    sprite('null', 4)	# 1-4
    Unknown4003('72726265663430385f345f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 5-8
    Unknown4003('72726265663430385f345f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 9-12
    Unknown4003('72726265663430385f345f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-30000)
        Unknown1007(320000)
    sprite('null', 12)	# 1-12
    GFX_0('rrb408Eff_2_Assist', 0)
    GFX_0('rrb408Eff_1_Assist', 0)
    GFX_0('rrb408Eff_4_Assist', 0)
    GFX_0('rrb408Eff_3_Assist', 0)

@State
def rrb408Eff_1_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown1096(3700)
    sprite('null', 2)	# 1-2
    Unknown4003('72726265663430385f315f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72726265663430385f315f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72726265663430385f315f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff_2_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown1096(3700)
    sprite('null', 2)	# 1-2
    Unknown4003('72726265663430385f325f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72726265663430385f325f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72726265663430385f325f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff_3_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp03')
        Unknown1096(4300)
        Unknown3001(70)
    sprite('null', 2)	# 1-2
    Unknown4003('72726265663430385f335f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72726265663430385f335f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72726265663430385f335f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408Eff_4_Assist():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown1096(3700)
    sprite('null', 2)	# 1-2
    Unknown4003('72726265663430385f345f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4003('72726265663430385f345f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4003('72726265663430385f345f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb408PetalEff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        teleportRelativeX(90000)
        Unknown1007(240000)
        Unknown2055(90)
    label(0)
    sprite('null', 1)	# 1-1
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('72726265663430385f706574616c00000000000000000000000000000000000000000000')
    gotoLabel(0)

@State
def rrb409Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown4008(3)
        teleportRelativeX(0)
        Unknown1007(245000)
        Unknown1096(3500)
    sprite('null', 10)	# 1-10
    Unknown26('rrb408Eff_2')
    Unknown26('rrb408Eff_1')
    Unknown26('rrb408Eff_4')
    Unknown26('rrb408Eff_3')
    GFX_0('rrb409Eff_2', 0)
    GFX_0('rrb409Eff_1', 0)
    GFX_0('rrb409Eff_4', 0)
    GFX_0('rrb409Eff_3', 0)
    GFX_0('rrbGroundEff', 0)

@State
def rrb409Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430395f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb409Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430395f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb409Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430395f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(70)
    sprite('null', 10)	# 1-10

@State
def rrb409Eff_4():

    def upon_IMMEDIATE():
        Unknown4003('72726265663430395f342e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown4013(2)
        Unknown3033()
    sprite('null', 10)	# 1-10

@State
def rrb204MuzzleEff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(205000)
        Unknown1007(95000)
        Unknown1072(140000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb320Eff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-40000)
        Unknown1007(150000)
        Unknown1096(3700)
        Unknown1064(3600)
        Unknown1072(-10000)
    sprite('null', 12)	# 1-12
    GFX_0('rrb320PetalEff', 0)
    GFX_0('rrb320Eff_2', 0)
    GFX_0('rrb320Eff_1', 0)
    GFX_0('rrb320Eff_3', 0)

@State
def rrb320Eff_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663332305f312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 12)	# 1-12

@State
def rrb320Eff_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663332305f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 12)	# 1-12

@State
def rrb320Eff_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663332305f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown3032()
        Unknown1007(15000)
        teleportRelativeX(20000)
        Unknown1096(3200)
        Unknown1100(50)
        Unknown3001(120)
        Unknown3004(-12)
        Unknown1073(-10000)
    sprite('null', 12)	# 1-12

@State
def rrb320MuzzleEff():

    def upon_IMMEDIATE():
        teleportRelativeX(-140000)
        Unknown1007(30000)
        Unknown1072(-140000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb320PetalEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        teleportRelativeX(200000)
        Unknown1007(-50000)
    sprite('null', 2)	# 1-2
    Unknown1015(-5000)
    Unknown1021(18000)
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('72726265663332305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown1015(-10000)
    Unknown1021(10000)
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('72726265663332305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown1015(-15000)
    Unknown1021(2000)
    Unknown4047(9, 9, 9)
    Unknown4048(0)
    Unknown4045('72726265663332305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 7-8
    Unknown1015(-10000)
    Unknown1021(-7000)
    Unknown4047(9, 9, 9)
    Unknown4048(-20000)
    Unknown4045('72726265663332305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 9-10
    Unknown1015(-7500)
    Unknown1021(-15000)
    Unknown4047(9, 9, 9)
    Unknown4048(-50000)
    Unknown4045('72726265663332305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 11-12
    Unknown1015(-5000)
    Unknown1021(-30000)
    Unknown4047(9, 9, 9)
    Unknown4048(-70000)
    Unknown4045('72726265663332305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 13-14
    Unknown1015(3000)
    Unknown1021(-30000)
    Unknown4047(9, 9, 9)
    Unknown4048(-90000)
    Unknown4045('72726265663332305f706574616c00000000000000000000000000000000000000000000')

@State
def rrb430Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        sendToLabelUpon(32, 10)
        sendToLabelUpon(33, 20)
        sendToLabelUpon(41, 100)
        Unknown23022(1)
        Unknown3038(1)
    sprite('null', 13)	# 1-13
    GFX_0('rrb430aEff', 0)
    sprite('null', 3)	# 14-16
    GFX_0('rrb430bEff', 0)
    sprite('null', 6)	# 17-22
    GFX_0('rrb430cEff', 0)
    label(0)
    sprite('null', 3)	# 23-25
    GFX_0('rrb430dEff', 0)
    GFX_0('rrb430MuzzleEff_01', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    sprite('rrb430_14', 7)	# 26-32
    GFX_0('rrbCaseEffC', 0)
    gotoLabel(2)
    label(1)
    sprite('rrb430_14', 7)	# 33-39
    GFX_0('rrbCaseEffD', 0)
    label(2)
    sprite('null', 6)	# 40-45
    GFX_0('rrb430eEff', 0)
    GFX_0('rrb430MuzzleEff_02', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(3)
    sprite('rrb430_19', 4)	# 46-49
    GFX_0('rrbCaseEff', 0)
    gotoLabel(0)
    label(3)
    sprite('rrb430_19', 4)	# 50-53
    GFX_0('rrbCaseEffB', 0)
    gotoLabel(0)
    label(10)
    sprite('null', 3)	# 54-56
    sprite('rrb430_17', 2)	# 57-58
    GFX_0('rrbCaseEffB', 0)
    sprite('null', 200)	# 59-258
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 0)
    label(20)
    sprite('null', 60)	# 259-318
    GFX_0('rrb430MuzzleEff_03', 0)
    GFX_0('rrb430Ryuhai', 103)
    GFX_0('rrb430FinishHit', 103)
    sprite('null', 1)	# 319-319
    Unknown14()
    label(100)
    sprite('rrb430_17', 3)	# 320-322
    sprite('rrb430_17', 6)	# 323-328
    GFX_0('rrbCaseEffB', 0)
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 100)

@State
def rrb430aEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(70000)
        Unknown1007(340000)
        Unknown1096(4000)
    sprite('null', 13)	# 1-13
    GFX_0('rrb430aEff_2', 0)
    GFX_0('rrb430aEff_1', 0)
    GFX_0('rrb430aEff_3', 0)
    GFX_0('rrb430aEff_4', 0)

@State
def rrb430aEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330615f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 13)	# 1-13

@State
def rrb430aEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330615f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 13)	# 1-13

@State
def rrb430aEff_3():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330615f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(127)
    sprite('null', 4)	# 1-4
    sprite('null', 10)	# 5-14
    Unknown3004(-5)

@State
def rrb430aEff_4():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330615f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 13)	# 1-13

@State
def rrb430bEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(70000)
        Unknown1007(240000)
        Unknown1096(4000)
    sprite('null', 13)	# 1-13
    GFX_0('rrb430bEff_2', 0)
    GFX_0('rrb430bEff_1', 0)
    GFX_0('rrb430bEff_3', 0)
    GFX_0('rrb430bEff_4', 0)

@State
def rrb430bEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330625f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430bEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330625f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430bEff_3():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330625f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown3001(127)
    sprite('null', 3)	# 1-3
    sprite('null', 7)	# 4-10
    Unknown3004(-5)

@State
def rrb430bEff_4():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330625f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430cEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(20000)
        Unknown1007(400000)
        Unknown1096(4500)
    sprite('null', 3)	# 1-3
    GFX_0('rrb430cEff_2', 0)
    GFX_0('rrb430cEff_1', 0)
    sprite('null', 3)	# 4-6
    Unknown1096(4000)
    teleportRelativeX(20000)
    Unknown1007(80000)

@State
def rrb430cEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330635f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 6)	# 1-6

@State
def rrb430cEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330635f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 6)	# 1-6

@State
def rrb430dEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-40000)
        Unknown1007(265000)
        Unknown1096(3900)
        Unknown1064(3400)
        Unknown1072(-15000)
    sprite('null', 10)	# 1-10
    GFX_0('rrb430dEff_2', 0)
    GFX_0('rrb430dEff_1', 0)
    GFX_0('rrb430dEff_3', 0)
    GFX_0('rrb430dEff_4', 0)

@State
def rrb430dEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430dEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430dEff_3():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown23015(11)
        Unknown4013(2)
        Unknown3001(90)
    sprite('null', 10)	# 1-10

@State
def rrb430dEff_4():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown4006(2)
        Unknown23015(11)
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430dEffB():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-50000)
        Unknown1007(255000)
        Unknown1096(3900)
        Unknown1064(3700)
        Unknown1072(0)
    sprite('null', 10)	# 1-10
    GFX_0('rrb430dEff_2B', 0)
    GFX_0('rrb430dEff_1B', 0)
    GFX_0('rrb430dEff_3B', 0)
    GFX_0('rrb430dEff_4B', 0)

@State
def rrb430dEff_1B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430dEff_2B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown23015(11)
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430dEff_3B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown23015(11)
        Unknown4013(2)
        Unknown3001(90)
    sprite('null', 10)	# 1-10

@State
def rrb430dEff_4B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown4006(2)
        Unknown23015(11)
        Unknown3033()
        Unknown4013(2)
    sprite('null', 10)	# 1-10

@State
def rrb430eEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-30000)
        Unknown1007(260000)
        Unknown1096(4400)
        Unknown1064(3700)
        Unknown1072(10000)
    sprite('null', 10)	# 1-10
    GFX_0('rrb430eEff_2', 0)
    GFX_0('rrb430eEff_1', 0)
    GFX_0('rrb430eEff_3', 0)
    GFX_0('rrb430eEff_4', 0)

@State
def rrb430eEff_1():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)	# 1-10

@State
def rrb430eEff_2():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)	# 1-10

@State
def rrb430eEff_3():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown4010(2)
        Unknown3001(90)
    sprite('null', 10)	# 1-10

@State
def rrb430eEff_4():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4006(2)
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)	# 1-10

@State
def rrb430eEffB():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-45000)
        Unknown1007(260000)
        Unknown1096(4400)
        Unknown1064(4000)
        Unknown1072(5000)
    sprite('null', 10)	# 1-10
    GFX_0('rrb430eEff_2B', 0)
    GFX_0('rrb430eEff_1B', 0)
    GFX_0('rrb430eEff_3B', 0)
    GFX_0('rrb430eEff_4B', 0)

@State
def rrb430eEff_1B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)	# 1-10

@State
def rrb430eEff_2B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)	# 1-10

@State
def rrb430eEff_3B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp03')
        Unknown4013(2)
        Unknown4010(2)
        Unknown3001(90)
    sprite('null', 10)	# 1-10

@State
def rrb430eEff_4B():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4006(2)
        Unknown4013(2)
        Unknown4010(2)
    sprite('null', 10)	# 1-10

@State
def rrb430fEff():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        teleportRelativeX(-50000)
        Unknown1007(250000)
        Unknown1096(4100)
    sprite('null', 3)	# 1-3
    GFX_0('rrb430fEff_2', 0)
    GFX_0('rrb430fEff_1', 0)
    GFX_0('rrb430fEff_4', 0)

@State
def rrb430fEff_1():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp01')
        Unknown4013(2)
    sprite('null', 3)	# 1-3
    Unknown4003('7272626566343330665f312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb430fEff_2():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp02')
        Unknown4013(2)
    sprite('null', 3)	# 1-3
    Unknown4003('7272626566343330665f322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb430fEff_4():

    def upon_IMMEDIATE():
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4013(2)
    sprite('null', 3)	# 1-3
    Unknown4003('7272626566343330665f342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb430MuzzleEff_01():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(280000)
        Unknown1007(420000)
        Unknown1072(30000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_C', 0)

@State
def rrb430MuzzleEff_02():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(300000)
        Unknown1007(400000)
        Unknown1072(45000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff', 0)

@State
def rrb430MuzzleEff_03():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(480000)
        Unknown1007(370000)
        Unknown1072(67000)
    sprite('null', 20)	# 1-20
    GFX_0('rrbMuzzleEff_B', 0)

@State
def rrb430FinishHit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1056(4500)
        Unknown1064(3400)
        Unknown1059(100)
        physicsXImpulse(-15000)
        physicsYImpulse(-5000)
        teleportRelativeX(350000)
        Unknown1007(330000)
        Unknown1072(-23000)
    sprite('null', 24)	# 1-24
    GFX_0('rrb430FinishHit03', 0)
    GFX_0('rrb430FinishHit01', 0)
    GFX_0('rrb430FinishHit02', 0)
    GFX_0('rrb430HitRing', 0)
    Unknown4048(157000)
    Unknown4045('72726265663433305f737065656400000000000000000000000000000000000000000000')
    Unknown4048(157000)
    Unknown4047(1, 1, 1)
    Unknown4045('72726265663433305f737065656442000000000000000000000000000000000000000000')
    GFX_0('rrb430FinishPetal', 0)

@State
def rrb430FinishPetal():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown1056(1000)
        Unknown1064(0)
        Unknown4061(0)
        Unknown3038(1)
    sprite('vrrrbef430_Hit', 1)	# 1-1
    Unknown4048(157000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f756e697175655f706574616c000000000000000000000064000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000019000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000018000000')
    sprite('vrrrbef430_Hit', 1)	# 2-2
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000017000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000016000000')
    sprite('vrrrbef430_Hit', 1)	# 3-3
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000015000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000014000000')
    sprite('vrrrbef430_Hit', 1)	# 4-4
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000013000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000012000000')
    sprite('vrrrbef430_Hit', 1)	# 5-5
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000011000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000010000000')
    SFX_3('rrbse_10')
    sprite('vrrrbef430_Hit', 1)	# 6-6
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000f000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000e000000')
    sprite('vrrrbef430_Hit', 1)	# 7-7
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000d000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000c000000')
    sprite('vrrrbef430_Hit', 1)	# 8-8
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000b000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000a000000')
    sprite('vrrrbef430_Hit', 1)	# 9-9
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000009000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000008000000')
    sprite('vrrrbef430_Hit', 1)	# 10-10
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000007000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000006000000')
    sprite('vrrrbef430_Hit', 1)	# 11-11
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000005000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000004000000')
    sprite('vrrrbef430_Hit', 1)	# 12-12
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000003000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000002000000')
    sprite('vrrrbef430_Hit', 1)	# 13-13
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000001000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000000000000')

@State
def rrb430FinishHit01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown4061(6)
        Unknown3032()
        Unknown23015(10)
        Unknown23122(1)
    sprite('null', 3)	# 1-3
    Unknown4003('72726265663433305f66696e69736830310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 4-7
    Unknown4003('72726265663433305f66696e69736830320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72726265663433305f66696e69736830330000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72726265663433305f66696e69736830340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72726265663433305f66696e69736830350000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72726265663433305f66696e69736830360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb430FinishHit02():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown3033()
        Unknown23015(10)
    sprite('null', 3)	# 1-3
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d41303100000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 4-7
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d41303200000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d41303300000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d41303400000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb430FinishHit03():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown3033()
        Unknown4061(6)
        Unknown21004(1)
        Unknown23015(10)
    sprite('null', 3)	# 1-3
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d42303100000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 4-7
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d42303200000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 8-10
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d42303300000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 11-13
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d42303400000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 14-16
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d42303500000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 17-19
    Unknown4003('72726265663433305f66696e6973685f426c6f6f6d42303600000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb430HitRing():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f73686f636b776176652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(2500)
        Unknown1099(20)
        Unknown1072(-23000)
        Unknown4061(6)
        Unknown21004(1)
    sprite('null', 15)	# 1-15
    sprite('null', 3)	# 16-18
    Unknown3004(-90)

@State
def rrb430Ryuhai():

    def upon_IMMEDIATE():
        Unknown1072(-23000)
    sprite('null', 3)	# 1-3
    sprite('null', 300)	# 4-303
    GFX_0('rrb430Ryuhai_1', 0)
    GFX_0('rrb430Ryuhai_2', 0)
    GFX_0('rrb430Ryuhai_3', 0)

@State
def rrb430Ryuhai_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(2)
        Unknown4006(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(2)
        teleportRelativeY(200000)
        Unknown1096(8000)
        Unknown1064(5000)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(190)
    sprite('null', 1)	# 1-1
    sprite('null', 2)	# 2-3
    Unknown1064(7000)
    sprite('null', 1)	# 4-4
    Unknown1064(6000)
    sprite('null', 20)	# 5-24
    Unknown1067(-100)
    Unknown3004(-10)

@State
def rrb430Ryuhai_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(2)
        Unknown4006(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(2)
        teleportRelativeY(200000)
        Unknown1096(8000)
        Unknown1064(3000)
        Unknown4061(6)
        Unknown21004(17)
        Unknown3001(190)
    sprite('null', 1)	# 1-1
    sprite('null', 2)	# 2-3
    Unknown1064(4000)
    sprite('null', 1)	# 4-4
    Unknown1064(3000)
    sprite('null', 20)	# 5-24
    Unknown1067(-100)
    Unknown3004(-10)

@State
def rrb430Ryuhai_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(2)
        Unknown4006(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(6)
        Unknown21004(1)
        Unknown23015(2)
        teleportRelativeY(200000)
        Unknown1056(6000)
        Unknown1064(2000)
        Unknown3001(128)
    sprite('null', 1)	# 1-1
    sprite('null', 2)	# 2-3
    Unknown1064(3000)
    sprite('null', 1)	# 4-4
    Unknown1064(2000)
    sprite('null', 15)	# 5-19
    Unknown1067(-166)
    Unknown3004(-12)

@State
def rrb430EffOD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        sendToLabelUpon(32, 10)
        sendToLabelUpon(33, 20)
        sendToLabelUpon(41, 100)
        Unknown23022(1)
        Unknown3038(1)
    sprite('null', 13)	# 1-13
    GFX_0('rrb430aEff', 0)
    GFX_0('rrb430aEff_5', 0)
    sprite('null', 3)	# 14-16
    GFX_0('rrb430bEff', 0)
    GFX_0('rrb430bEff_5', 0)
    sprite('null', 6)	# 17-22
    GFX_0('rrb430cEff', 0)
    label(0)
    sprite('null', 3)	# 23-25
    GFX_0('rrb430dEff', 0)
    GFX_0('rrb430dEff_5', 0)
    GFX_0('rrb430MuzzleEff_01', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    sprite('rrb430_14', 7)	# 26-32
    GFX_0('rrbCaseEffC', 0)
    gotoLabel(2)
    label(1)
    sprite('rrb430_14', 7)	# 33-39
    GFX_0('rrbCaseEffD', 0)
    label(2)
    sprite('null', 6)	# 40-45
    GFX_0('rrb430eEff', 0)
    GFX_0('rrb430eEff_5', 0)
    GFX_0('rrb430MuzzleEff_02', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(3)
    sprite('rrb430_19', 4)	# 46-49
    GFX_0('rrbCaseEff', 0)
    gotoLabel(4)
    label(3)
    sprite('rrb430_19', 4)	# 50-53
    GFX_0('rrbCaseEffB', 0)
    gotoLabel(4)
    label(4)
    sprite('null', 3)	# 54-56
    GFX_0('rrb430dEffB', 0)
    GFX_0('rrb430dEff_5', 0)
    GFX_0('rrb430MuzzleEff_01', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(5)
    sprite('rrb430_14', 7)	# 57-63
    GFX_0('rrbCaseEffC', 0)
    gotoLabel(6)
    label(5)
    sprite('rrb430_14', 7)	# 64-70
    GFX_0('rrbCaseEffD', 0)
    label(6)
    sprite('null', 6)	# 71-76
    GFX_0('rrb430eEffB', 0)
    GFX_0('rrb430eEff_5', 0)
    GFX_0('rrb430MuzzleEff_02', 0)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(7)
    sprite('rrb430_19', 4)	# 77-80
    GFX_0('rrbCaseEff', 0)
    gotoLabel(0)
    label(7)
    sprite('rrb430_19', 4)	# 81-84
    GFX_0('rrbCaseEffB', 0)
    gotoLabel(0)
    label(10)
    sprite('null', 3)	# 85-87
    sprite('rrb430_17', 4)	# 88-91
    GFX_0('rrbCaseEffB', 0)
    sprite('null', 200)	# 92-291
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 0)
    label(20)
    sprite('null', 60)	# 292-351
    GFX_0('rrb430MuzzleEff_03', 0)
    GFX_0('rrb430Ryuhai', 103)
    GFX_0('rrb430FinishHit', 103)
    sprite('null', 1)	# 352-352
    Unknown14()
    label(100)
    sprite('rrb430_17', 10)	# 353-362
    GFX_0('rrbCaseEffB', 0)
    Unknown26('rrb430eEff')
    GFX_0('rrb430fEff', 100)

@State
def rrb430aEff_5():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330615f352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(70000)
        Unknown1007(340000)
    sprite('null', 2)	# 1-2
    Unknown1096(1)
    sprite('null', 3)	# 3-5
    Unknown4003('7272626566343330615f352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(4000)
    Unknown1099(300)
    physicsXImpulse(3000)
    physicsYImpulse(-3000)
    sprite('null', 7)	# 6-12
    Unknown3004(-31)

@State
def rrb430bEff_5():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330625f352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(70000)
        Unknown1007(240000)
        Unknown1096(4600)
    sprite('null', 3)	# 1-3
    Unknown1099(300)
    physicsXImpulse(2000)
    physicsYImpulse(-5000)
    sprite('null', 10)	# 4-13
    Unknown3004(-23)

@State
def rrb430dEff_5():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330645f352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(-40000)
        Unknown1007(265000)
        Unknown1096(3900)
        Unknown1064(3400)
    sprite('null', 3)	# 1-3
    Unknown1099(200)
    physicsXImpulse(2000)
    physicsYImpulse(2000)
    sprite('null', 7)	# 4-10
    Unknown3004(-31)

@State
def rrb430eEff_5():

    def upon_IMMEDIATE():
        Unknown4003('7272626566343330655f352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('NormalArts_Temp')
        Unknown3033()
        Unknown4009(0)
        Unknown4061(6)
        Unknown21004(1)
        teleportRelativeX(-40000)
        Unknown1007(265000)
        Unknown1096(3900)
        Unknown1064(3400)
    sprite('null', 3)	# 1-3
    Unknown1099(300)
    physicsXImpulse(2000)
    physicsYImpulse(-2000)
    sprite('null', 7)	# 4-10
    Unknown3004(-31)

@State
def rrb431Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(-40000)
        Unknown1007(220000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 10)
    sprite('null', 8)	# 1-8
    sprite('null', 20)	# 9-28
    GFX_0('rrb431Screen', 0)
    sprite('null', 50)	# 29-78
    GFX_0('rrb431Smoke', 0)
    GFX_0('rrb431Petal_First', 0)
    label(10)
    sprite('null', 50)	# 79-128
    GFX_0('rrb431Tornade', 0)
    GFX_0('rrb431Trail', 0)
    label(0)
    sprite('null', 120)	# 129-248
    Unknown21012('727262343331426c61636b494f0000000000000000000000000000000000000020000000')
    Unknown21012('727262343331547261696c00000000000000000000000000000000000000000020000000')
    Unknown21012('727262343331506574616c5f466972737400000000000000000000000000000021000000')
    Unknown26('rrb431Smoke')
    sprite('null', 1)	# 249-249
    Unknown14()
    label(1)
    sprite('null', 5)	# 250-254
    Unknown21012('72726234333153637265656e000000000000000000000000000000000000000021000000')
    sprite('null', 5)	# 255-259
    Unknown26('rrb431Petal_First')
    Unknown21012('727262343331546f726e6164650000000000000000000000000000000000000020000000')
    Unknown21012('727262343331547261696c00000000000000000000000000000000000000000020000000')
    sprite('null', 10)	# 260-269
    Unknown26('rrb431Smoke')
    sprite('null', 120)	# 270-389
    sprite('null', 1)	# 390-390
    Unknown14()
    label(2)
    sprite('null', 5)	# 391-395
    Unknown21012('72726234333153637265656e000000000000000000000000000000000000000022000000')
    sprite('null', 5)	# 396-400
    Unknown26('rrb431Petal_First')
    Unknown21012('727262343331546f726e6164650000000000000000000000000000000000000020000000')
    Unknown21012('727262343331547261696c00000000000000000000000000000000000000000020000000')
    sprite('null', 10)	# 401-410
    Unknown26('rrb431Smoke')
    sprite('null', 120)	# 411-530

@State
def rrb431Screen():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
        Unknown2055(150)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('null', 180)	# 1-180
    GFX_0('rrb431BlackIO', 0)
    sprite('null', 1)	# 181-181
    Unknown14()
    label(1)
    sprite('null', 120)	# 182-301
    GFX_0('rrb431Petal_Hit', 0)
    GFX_0('rrb431Ryuhai_1', 0)
    GFX_0('rrb431Ryuhai_2', 0)
    GFX_0('rrb431Ryuhai_3', 0)
    GFX_0('rrb431BGLine', 0)
    GFX_0('rrb431Wind', 0)
    sprite('null', 1)	# 302-302
    Unknown14()
    label(2)
    sprite('null', 120)	# 303-422
    GFX_0('rrb431Petal_Hit', 0)
    GFX_0('rrb431Ryuhai_1', 0)
    GFX_0('rrb431Ryuhai_2', 0)
    GFX_0('rrb431Ryuhai_3', 0)
    GFX_0('rrb431BGLine', 0)
    GFX_0('rrb431Wind', 0)
    GFX_0('rrb431Wind_OD', 0)
    sprite('null', 1)	# 423-423
    Unknown14()

@State
def rrb431BlackIO():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f706c616e652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown2054(1)
        Unknown3032()
        sendToLabelUpon(32, 0)
        Unknown23015(2)
        Unknown3007(0)
        Unknown3013(0)
        Unknown3019(0)
        Unknown3001(0)
        Unknown1096(6000)
    sprite('null', 20)	# 1-20
    Unknown3004(9)
    sprite('null', 60)	# 21-80
    Unknown3004(0)
    label(0)
    sprite('null', 40)	# 81-120
    Unknown3004(-4)

@State
def rrb431Ryuhai_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        teleportRelativeY(200000)
        Unknown1096(6000)
        Unknown1064(2000)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(0)
    sprite('null', 1)	# 1-1
    Unknown3001(255)
    sprite('null', 2)	# 2-3
    Unknown3001(255)
    Unknown1064(3500)
    sprite('null', 1)	# 4-4
    Unknown1064(3000)
    sprite('null', 22)	# 5-26
    Unknown1067(-136)
    Unknown3004(-5)

@State
def rrb431Ryuhai_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        teleportRelativeY(200000)
        Unknown1096(6000)
        Unknown1064(1000)
        Unknown3001(0)
        Unknown4061(6)
        Unknown21004(17)
    sprite('null', 1)	# 1-1
    Unknown3001(204)
    sprite('null', 2)	# 2-3
    Unknown3001(204)
    Unknown1064(3000)
    sprite('null', 1)	# 4-4
    Unknown1064(2000)
    sprite('null', 20)	# 5-24
    Unknown1067(-100)
    Unknown3004(-7)

@State
def rrb431Ryuhai_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        teleportRelativeY(200000)
        Unknown1056(6000)
        Unknown1064(1500)
        Unknown3001(0)
    sprite('null', 1)	# 1-1
    Unknown3001(127)
    sprite('null', 2)	# 2-3
    Unknown3001(127)
    Unknown1064(3500)
    sprite('null', 1)	# 4-4
    Unknown1064(2500)
    sprite('null', 15)	# 5-19
    Unknown3004(-5)
    Unknown1067(-166)

@State
def rrb431BGLine():

    def upon_IMMEDIATE():
        Unknown4022(2)
        Unknown2054(1)
        Unknown2055(14)
        teleportRelativeX(-200000)
        teleportRelativeY(200000)
    label(0)
    sprite('null', 2)	# 1-2
    GFX_1('rrbef431_speed03', 0)
    gotoLabel(0)

@State
def rrb431Hit():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f73686f636b776176652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3032()
        Unknown1096(2500)
        Unknown1099(20)
        Unknown1007(150000)
        Unknown1072(-25000)
        Unknown4061(0)
        Unknown21004(9)
    sprite('null', 15)	# 1-15
    sprite('null', 3)	# 16-18
    Unknown3004(-90)

@State
def rrb431Petal_First():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2055(120)
        sendToLabelUpon(33, 1)
        teleportRelativeX(-10000)
    sprite('null', 2)	# 1-2
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 3-4
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 5-6
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 2)	# 7-8
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    Unknown4047(9, 9, 9)
    Unknown4054(0)
    Unknown4045('72726265663433315f737065656430340000000000000000000000000000000000000000')
    sprite('null', 2)	# 9-10
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    gotoLabel(0)
    label(1)
    sprite('null', 2)	# 11-12
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    SFX_3('rrbse_10')
    sprite('null', 2)	# 13-14
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f737065656430340000000000000000000000000000000000000000')
    sprite('null', 2)	# 15-16
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 17-18
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 19-20
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 21-22
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 23-24
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c00000000000000000000000000000000000000000000')

@State
def rrb431Petal_Hit():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
    sprite('null', 5)	# 1-5
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    SFX_3('rrbse_11')
    sprite('null', 5)	# 6-10
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 4)	# 11-14
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    SFX_3('rrbse_10')
    sprite('null', 3)	# 15-17
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 5)	# 18-22
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 5)	# 23-27
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 5)	# 28-32
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 5)	# 33-37
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 6)	# 38-43
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 6)	# 44-49
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 7)	# 50-56
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 7)	# 57-63
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 8)	# 64-71
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 9)	# 72-80
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 10)	# 81-90
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64303100000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')
    sprite('null', 12)	# 91-102
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64303100000000000000000000000000000000')
    Unknown4045('72726265663433315f736d6f6b655f656e64000000000000000000000000000000000000')

@State
def rrb431Tornade():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(0)
        Unknown1000(0)
        teleportRelativeY(0)
        sendToLabelUpon(32, 0)
    sprite('vrrrbef431_tornade01', 3)	# 1-3
    sprite('vrrrbef431_tornade02', 3)	# 4-6
    sprite('vrrrbef431_tornade03', 3)	# 7-9
    sprite('vrrrbef431_tornade01', 2)	# 10-11
    sprite('vrrrbef431_tornade02', 2)	# 12-13
    sprite('vrrrbef431_tornade03', 2)	# 14-15
    sprite('vrrrbef431_tornade01', 2)	# 16-17
    sprite('vrrrbef431_tornade02', 2)	# 18-19
    sprite('vrrrbef431_tornade03', 2)	# 20-21
    sprite('vrrrbef431_tornade01', 2)	# 22-23
    sprite('vrrrbef431_tornade02', 2)	# 24-25
    sprite('vrrrbef431_tornade03', 2)	# 26-27
    sprite('null', 19)	# 28-46
    Unknown14()
    label(0)
    sprite('vrrrbef431_tornade01', 2)	# 47-48
    Unknown3001(200)
    Unknown3004(-20)
    sprite('vrrrbef431_tornade02', 2)	# 49-50
    sprite('vrrrbef431_tornade03', 2)	# 51-52
    sprite('vrrrbef431_tornade01', 2)	# 53-54
    sprite('vrrrbef431_tornade02', 2)	# 55-56
    sprite('vrrrbef431_tornade03', 2)	# 57-58
    sprite('vrrrbef431_tornade01', 1)	# 59-59
    sprite('vrrrbef431_tornade02', 1)	# 60-60
    sprite('vrrrbef431_tornade03', 1)	# 61-61
    sprite('vrrrbef431_tornade01', 1)	# 62-62
    sprite('vrrrbef431_tornade02', 1)	# 63-63
    sprite('vrrrbef431_tornade03', 1)	# 64-64
    Unknown3004(-21)

@State
def rrb431Trail():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f747261696c2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(3)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(11)
        sendToLabelUpon(32, 0)
        Unknown1007(-30000)
        teleportRelativeX(-100000)
        Unknown1056(1000)
        Unknown1064(800)
        Unknown21004(9)
        Unknown3001(15)
    sprite('null', 5)	# 1-5
    GFX_0('rrb431Trail_2', 0)
    GFX_0('rrb431Trail_3', 0)
    Unknown1059(1000)
    Unknown1067(200)
    Unknown3004(30)
    sprite('null', 5)	# 6-10
    Unknown3004(0)
    Unknown1059(400)
    Unknown1067(50)
    sprite('null', 80)	# 11-90
    Unknown1059(100)
    Unknown1067(10)
    label(0)
    sprite('null', 5)	# 91-95
    Unknown21012('727262343331547261696c5f320000000000000000000000000000000000000020000000')
    Unknown21012('727262343331547261696c5f330000000000000000000000000000000000000020000000')
    Unknown1059(-900)
    Unknown1067(-150)
    Unknown3004(-12)
    sprite('null', 5)	# 96-100
    Unknown1059(-500)

@State
def rrb431Trail_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f676c6f772e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(3)
        Unknown2054(1)
        Unknown23015(11)
        Unknown3033()
        sendToLabelUpon(32, 0)
        teleportRelativeX(100000)
        Unknown1056(15000)
        Unknown1064(4500)
        Unknown21004(9)
        Unknown3001(10)
    sprite('null', 10)	# 1-10
    Unknown3004(20)
    sprite('null', 10)	# 11-20
    Unknown3004(0)
    label(0)
    sprite('null', 5)	# 21-25
    sprite('null', 10)	# 26-35
    Unknown3004(-11)

@State
def rrb431Trail_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f676c6f772e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4022(3)
        Unknown2054(1)
        Unknown23015(6)
        Unknown3033()
        sendToLabelUpon(32, 0)
        teleportRelativeX(100000)
        Unknown1056(15000)
        Unknown1064(4500)
        Unknown21004(9)
        Unknown3001(0)
    sprite('null', 5)	# 1-5
    Unknown3004(5)
    sprite('null', 90)	# 6-95
    Unknown3004(0)
    label(0)
    sprite('null', 10)	# 96-105
    sprite('null', 10)	# 106-115
    Unknown3004(-2)

@State
def rrb431Wind():

    def upon_IMMEDIATE():
        Unknown4022(22)
        Unknown2054(1)
        Unknown2055(75)
    sprite('null', 30)	# 1-30
    label(0)
    sprite('null', 4)	# 31-34
    Unknown4045('72726265663433315f737065656430320000000000000000000000000000000000000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f737065656430310000000000000000000000000000000000000000')
    gotoLabel(0)

@State
def rrb431Wind_OD():

    def upon_IMMEDIATE():
        Unknown4022(22)
        Unknown2054(1)
        Unknown2055(75)
        Unknown4061(6)
    sprite('null', 30)	# 1-30
    label(0)
    sprite('null', 4)	# 31-34
    Unknown4047(1, 1, 1)
    Unknown4045('72726265663433315f73706565645f4f4400000000000000000000000000000000000000')
    gotoLabel(0)

@State
def rrb431Smoke():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4022(3)
        Unknown2055(60)
    sprite('null', 3)	# 1-3
    GFX_0('rrb431RingA', 0)
    GFX_0('rrb431Smoke_Start', 0)
    label(0)
    sprite('null', 3)	# 4-6
    GFX_0('rrb431RingA', 0)
    GFX_0('rrb431SmokeB1', 0)
    sprite('null', 3)	# 7-9
    GFX_0('rrb431RingB', 0)
    GFX_0('rrb431RingC2', 0)
    GFX_0('rrb431SmokeB1', 0)
    sprite('null', 3)	# 10-12
    GFX_0('rrb431RingA', 0)
    GFX_0('rrb431SmokeB1', 0)
    sprite('null', 3)	# 13-15
    GFX_0('rrb431RingC', 0)
    GFX_0('rrb431RingB2', 0)
    GFX_0('rrb431SmokeB1', 0)
    gotoLabel(0)

@State
def rrb431RingA():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(-50000)
        Unknown1010(10000, -250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokea01', 1)	# 1-1
    Unknown1096(500)
    sprite('vrrrbef_ringsmokea01', 3)	# 2-4
    Unknown1096(650)
    Unknown1099(40)
    sprite('vrrrbef_ringsmokea02', 4)	# 5-8
    sprite('vrrrbef_ringsmokea03', 4)	# 9-12
    sprite('vrrrbef_ringsmokea04', 4)	# 13-16

@State
def rrb431RingB():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(-50000)
        Unknown1010(100000, -250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokeb01', 1)	# 1-1
    Unknown1096(400)
    sprite('vrrrbef_ringsmokeb01', 3)	# 2-4
    Unknown1096(500)
    Unknown1099(30)
    sprite('vrrrbef_ringsmokeb02', 4)	# 5-8
    sprite('vrrrbef_ringsmokeb03', 4)	# 9-12
    sprite('vrrrbef_ringsmokeb04', 4)	# 13-16

@State
def rrb431RingC():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(-50000)
        Unknown1010(100000, -150000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokec01', 1)	# 1-1
    Unknown1096(400)
    sprite('vrrrbef_ringsmokec01', 3)	# 2-4
    Unknown1096(550)
    Unknown1099(35)
    sprite('vrrrbef_ringsmokec02', 4)	# 5-8
    sprite('vrrrbef_ringsmokec03', 4)	# 9-12
    sprite('vrrrbef_ringsmokec04', 4)	# 13-16

@State
def rrb431RingB2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(200000)
        Unknown1010(100000, -250000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokeb01', 1)	# 1-1
    Unknown1096(600)
    sprite('vrrrbef_ringsmokeb01', 3)	# 2-4
    Unknown1096(700)
    Unknown1099(20)
    sprite('vrrrbef_ringsmokeb02', 4)	# 5-8
    sprite('vrrrbef_ringsmokeb03', 4)	# 9-12
    sprite('vrrrbef_ringsmokeb04', 4)	# 13-16

@State
def rrb431RingC2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(150000)
        Unknown1010(100000, -150000)
        physicsXImpulse(-5000)
    sprite('vrrrbef_ringsmokec01', 1)	# 1-1
    Unknown1096(600)
    sprite('vrrrbef_ringsmokec01', 3)	# 2-4
    Unknown1096(650)
    Unknown1099(25)
    sprite('vrrrbef_ringsmokec02', 4)	# 5-8
    sprite('vrrrbef_ringsmokec03', 4)	# 9-12
    sprite('vrrrbef_ringsmokec04', 4)	# 13-16

@State
def rrb431Smoke_Start():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(150000)
        physicsXImpulse(-15000)
        Unknown1025(10000, 0)
        Unknown1096(500)
        Unknown1099(20)
    sprite('vrrrbef_smoke01', 3)	# 1-3
    sprite('vrrrbef_smoke02', 3)	# 4-6
    sprite('vrrrbef_smoke03', 3)	# 7-9
    sprite('vrrrbef_smoke04', 3)	# 10-12
    sprite('vrrrbef_smoke05', 3)	# 13-15
    Unknown3004(-20)
    sprite('vrrrbef_smoke06', 3)	# 16-18
    Unknown3004(-50)

@State
def rrb431SmokeB1():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        Unknown1007(-250000)
        teleportRelativeX(50000)
        physicsXImpulse(-5000)
        Unknown1096(700)
        Unknown1102(100, -100)
        Unknown1099(20)
    sprite('vrrrbef_smokeb01', 2)	# 1-2
    GFX_0('rrb431SmokeB2', 0)
    sprite('vrrrbef_smokeb02', 2)	# 3-4
    sprite('vrrrbef_smokeb03', 2)	# 5-6
    sprite('vrrrbef_smokeb04', 3)	# 7-9
    sprite('vrrrbef_smokeb05', 3)	# 10-12
    Unknown3004(-28)
    sprite('vrrrbef_smokeb06', 3)	# 13-15
    sprite('vrrrbef_smokeb07', 3)	# 16-18

@State
def rrb431SmokeB2():

    def upon_IMMEDIATE():
        callSubroutine('CommonSmoke')
        Unknown2054(1)
        teleportRelativeX(-150000)
        physicsXImpulse(-15000)
        Unknown1096(1000)
        Unknown1102(100, -100)
        Unknown1099(20)
    sprite('vrrrbef_smokeb01', 2)	# 1-2
    sprite('vrrrbef_smokeb02', 2)	# 3-4
    sprite('vrrrbef_smokeb03', 2)	# 5-6
    sprite('vrrrbef_smokeb04', 3)	# 7-9
    Unknown1026(500, 0)
    sprite('vrrrbef_smokeb05', 3)	# 10-12
    Unknown3004(-28)
    sprite('vrrrbef_smokeb06', 3)	# 13-15
    sprite('vrrrbef_smokeb07', 3)	# 16-18

@State
def rrb431Petal_DDD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
    sprite('null', 14)	# 1-14
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    sprite('null', 14)	# 15-28
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    sprite('null', 16)	# 29-44
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    sprite('null', 16)	# 45-60
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    sprite('null', 16)	# 61-76
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64000000000000000000000000000000000000')
    sprite('null', 16)	# 77-92
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433315f706574616c5f656e64303100000000000000000000000000000000')

@Subroutine
def DDSmokeColor():
    Unknown3019(225)
    Unknown3013(250)
    Unknown3001(255)

@State
def rrb450():

    def upon_IMMEDIATE():
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(41, 100)
        Unknown4007(3)
        Unknown4011(3)
    sprite('null', 32767)	# 1-32767
    GFX_0('RWBY_AHground', -1)
    label(0)
    sprite('null', 6)	# 32768-32773
    GFX_0('rrb450_WhiteOut', -1)
    sprite('null', 20)	# 32774-32793
    GFX_0('rrb450_Jump', -1)
    GFX_0('rrb450Ryuhai', -1)
    sprite('null', 32767)	# 32794-65560
    GFX_0('rrb450_TrailPetal', -1)
    label(1)
    sprite('null', 32767)	# 65561-98327
    Unknown21012('7272623435305f57686974654f7574000000000000000000000000000000000020000000')
    GFX_0('rrb450Flare', -1)
    label(2)
    sprite('null', 8)	# 98328-98335
    sprite('null', 36)	# 98336-98371
    GFX_0('rrb450FinishHit', -1)
    GFX_0('rrb450_Petal', -1)
    sprite('null', 32767)	# 98372-131138
    GFX_0('rrb450_Transition', -1)
    label(100)
    sprite('null', 6)	# 131139-131144
    Unknown21012('525742595f414867726f756e640000000000000000000000000000000000000020000000')

@State
def RWBY_AHground():

    def upon_IMMEDIATE():
        Unknown4003('525742595f414867726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3026(-16777216)
        Unknown1000(0)
        teleportRelativeY(-1000)
        Unknown3032()
        Unknown23015(2)
        sendToLabelUpon(32, 0)
        Unknown4011(3)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 20)	# 32768-32787

@State
def rrb450_Jump():

    def upon_IMMEDIATE():
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        Unknown4007(3)
        teleportRelativeX(50000)
        Unknown1007(20000)
        Unknown4061(0)
    sprite('null', 40)	# 1-40
    GFX_0('rrb450_JumpPetal', 0)
    GFX_0('rrb450_JumpSmoke', 0)

@State
def rrb450_JumpPetal():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4061(0)
        Unknown4010(2)
    sprite('null', 120)	# 1-120
    Unknown4047(9, 9, 9)
    Unknown23067('rrbef450_jumppetal')

@State
def rrb450_JumpSmoke():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 120)	# 1-120
    Unknown23067('rrbef450_jumpsmoke')

@State
def rrb450_TrailPetal():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2055(220)
        Unknown3038(1)
        Unknown1000(0)
        teleportRelativeY(1000000)
    sprite('vrrrbef450_petalex', 5)	# 1-5
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000006000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000005000000')
    sprite('vrrrbef450_petalex', 5)	# 6-10
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000005000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000004000000')
    sprite('vrrrbef450_petalex', 5)	# 11-15
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000004000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000003000000')
    sprite('vrrrbef450_petalex', 5)	# 16-20
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000003000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000002000000')
    sprite('vrrrbef450_petalex', 5)	# 21-25
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000002000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000001000000')
    sprite('vrrrbef450_petalex', 5)	# 26-30
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c0000000000000000000000000000000000')
    Unknown4007(3)
    Unknown1000(0)
    teleportRelativeY(0)
    label(0)
    sprite('vrrrbef450_petalex', 4)	# 31-34
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663435305f747261696c706574616c4200000000000000000000000000000000')
    Unknown4048(45000)
    Unknown4045('72726265663435305f747261696c73706565640000000000000000000000000000000000')
    gotoLabel(0)

@State
def rrb450_WhiteOut():

    def upon_IMMEDIATE():
        Unknown3033()
        sendToLabelUpon(32, 0)
        Unknown23015(1)
        Unknown1096(6000)
        Unknown3000(0)
        Unknown4061(6)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 5)	# 1-5
    sprite('null', 5)	# 6-10
    GFX_0('rrb450_Speed', -1)
    sprite('null', 20)	# 11-30
    Unknown4003('72726265663435305f77686974652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3001(0)
    Unknown3004(13)
    sprite('null', 60)	# 31-90
    Unknown3004(0)
    label(0)
    sprite('null', 1)	# 91-91
    sprite('null', 15)	# 92-106
    clearUponHandler(3)
    Unknown4012(3)
    Unknown1000(0)
    teleportRelativeY(0)
    sprite('null', 40)	# 107-146
    Unknown3004(-7)
    sprite('null', 40)	# 147-186
    Unknown1096(0)
    Unknown21012('7272623435305f5370656564000000000000000000000000000000000000000020000000')
    sprite('null', 40)	# 187-226

@State
def rrb450_Speed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
        sendToLabelUpon(32, 1)
    Unknown2055(260)
    sprite('null', 2)	# 1-2
    Unknown4048(45000)
    Unknown4045('72726265663435305f7370656564000000000000000000000000000000000000ffffffff')
    sprite('null', 3)	# 3-5
    Unknown4048(45000)
    Unknown4045('72726265663435305f7370656564000000000000000000000000000000000000ffffffff')
    sprite('null', 3)	# 6-8
    Unknown4048(45000)
    Unknown4045('72726265663435305f7370656564000000000000000000000000000000000000ffffffff')
    sprite('null', 5)	# 9-13
    Unknown4048(45000)
    Unknown4045('72726265663435305f7370656564000000000000000000000000000000000000ffffffff')
    sprite('null', 5)	# 14-18
    Unknown4048(45000)
    Unknown4045('72726265663435305f7370656564000000000000000000000000000000000000ffffffff')
    label(0)
    sprite('null', 5)	# 19-23
    Unknown4048(45000)
    Unknown4045('72726265663435305f7370656564420000000000000000000000000000000000ffffffff')
    gotoLabel(0)
    label(1)
    sprite('null', 5)	# 24-28
    Unknown4048(45000)
    Unknown4045('72726265663435305f7370656564430000000000000000000000000000000000ffffffff')
    gotoLabel(1)

@State
def rrb450Ryuhai():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1072(-45000)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 3)	# 1-3
    Unknown4012(0)
    sprite('null', 40)	# 4-43
    GFX_0('rrb450Ryuhai_1', 0)
    GFX_0('rrb450Ryuhai_2', 0)
    GFX_0('rrb450Ryuhai_3', 0)

@State
def rrb450Ryuhai_1():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        Unknown1096(8000)
        Unknown1064(5000)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(190)
    sprite('null', 1)	# 1-1
    sprite('null', 2)	# 2-3
    Unknown1064(7000)
    sprite('null', 1)	# 4-4
    Unknown1064(6000)
    sprite('null', 30)	# 5-34
    Unknown1067(-66)
    Unknown3004(-10)

@State
def rrb450Ryuhai_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        Unknown1096(8000)
        Unknown1064(3000)
        Unknown4061(6)
        Unknown21004(17)
        Unknown3001(190)
    sprite('null', 1)	# 1-1
    sprite('null', 2)	# 2-3
    Unknown1064(4000)
    sprite('null', 1)	# 4-4
    Unknown1064(3000)
    sprite('null', 30)	# 5-34
    Unknown1067(-66)
    Unknown3004(-10)

@State
def rrb450Ryuhai_3():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(15)
        Unknown1056(6000)
        Unknown1064(2000)
        Unknown3001(64)
    sprite('null', 1)	# 1-1
    sprite('null', 2)	# 2-3
    Unknown1064(3000)
    sprite('null', 1)	# 4-4
    Unknown1064(2000)
    sprite('null', 25)	# 5-29
    Unknown1067(-100)
    Unknown3004(-12)

@State
def rrb450Flare():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown21010(1)
        Unknown4061(6)
        Unknown1000(-230000)
        teleportRelativeY(60000)
        Unknown2055(380)
        GFX_0('rrb450FlareA', -1)
        GFX_0('rrb450FlareB', -1)
        Unknown1096(1000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 6)	# 32768-32773
    Unknown1000(-220000)
    teleportRelativeY(58000)
    sprite('null', 6)	# 32774-32779
    Unknown1000(-219000)
    teleportRelativeY(56000)
    sprite('null', 3)	# 32780-32782
    Unknown1000(-225000)
    teleportRelativeY(52000)
    sprite('null', 3)	# 32783-32785
    Unknown1000(-230000)
    teleportRelativeY(48000)
    sprite('null', 4)	# 32786-32789
    Unknown1000(-233000)
    teleportRelativeY(46000)
    sprite('null', 10)	# 32790-32799
    sprite('null', 10)	# 32800-32809
    sprite('null', 10)	# 32810-32819
    sprite('null', 10)	# 32820-32829
    sprite('null', 32767)	# 32830-65596
    Unknown1096(0)
    Unknown14()
    Unknown1000(250000)
    teleportRelativeY(500000)

@State
def rrb450FlareA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4013(2)
        Unknown4061(6)
        Unknown4054(6)
        Unknown4047(17, 17, 17)
        Unknown23067('rrbef450_flareA')
    sprite('null', 32767)	# 1-32767

@State
def rrb450FlareB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4025(2)
        Unknown4013(2)
        Unknown4061(6)
        Unknown4054(6)
        Unknown4047(1, 1, 1)
        Unknown23067('rrbef450_flareB')
    sprite('null', 32767)	# 1-32767

@State
def rrb450MuzzleEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown1073(230000)
        teleportRelativeX(-230000)
        Unknown1007(-20000)
    sprite('null', 25)	# 1-25
    GFX_0('rrbMuzzleEff_450', 0)
    sprite('null', 25)	# 26-50
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)	# 51-75
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)	# 76-100
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)	# 101-125
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)	# 126-150
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_15')
    sprite('null', 25)	# 151-175
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_01')
    SFX_3('rrbse_02')
    sprite('null', 25)	# 176-200
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_01')
    SFX_3('rrbse_02')
    sprite('null', 58)	# 201-258
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_01')
    SFX_3('rrbse_02')
    sprite('null', 15)	# 259-273
    GFX_0('rrbMuzzleEff_450', 0)
    SFX_3('rrbse_02')

@State
def rrbMuzzleEff_450():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown4007(2)
        Unknown4006(2)
        teleportRelativeX(-50000)
        Unknown1072(-90000)
        Unknown1096(900)
        Unknown1088(-2000)
    sprite('null', 12)	# 1-12
    Unknown4048(-40000)
    Unknown4045('72726265665f6d757a7a6c650000000000000000000000000000000000000000ffffffff')
    GFX_0('rrbMuzzleEff_450_2', 0)
    GFX_0('rrbMuzzleEff_B3', 0)

@State
def rrbMuzzleEff_450_2():

    def upon_IMMEDIATE():
        Unknown4003('72726265665f6d757a7a6c6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(4000)
        Unknown1088(-3000)
        Unknown1099(150)
        Unknown3007(160)
        Unknown3013(210)
        Unknown23015(1)
    sprite('null', 6)	# 1-6
    sprite('null', 1)	# 7-7
    Unknown3001(180)
    sprite('null', 1)	# 8-8
    Unknown3001(128)

@State
def rrb450FinishHit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1056(5000)
        Unknown1064(4000)
        Unknown1059(100)
        physicsXImpulse(15000)
        physicsYImpulse(9000)
        Unknown1000(-150000)
        teleportRelativeY(50000)
        Unknown1072(157000)
    sprite('null', 24)	# 1-24
    GFX_0('rrb430FinishHit03', 0)
    GFX_0('rrb430FinishHit01', 0)
    GFX_0('rrb430FinishHit02', 0)
    GFX_0('rrb450RyuhaiFinish', -1)
    GFX_0('rrb430HitRing', 0)
    Unknown4048(-23000)
    Unknown4045('72726265663433305f737065656400000000000000000000000000000000000000000000')
    Unknown4048(-23000)
    Unknown4047(1, 1, 1)
    Unknown4045('72726265663433305f737065656442000000000000000000000000000000000000000000')
    GFX_0('rrb450FinishPetal', 0)

@State
def rrb450RyuhaiFinish():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown1072(-23000)
        Unknown1000(-150000)
        teleportRelativeY(50000)
        Unknown1056(4000)
        Unknown1064(3000)
    sprite('null', 3)	# 1-3
    Unknown4012(0)
    sprite('null', 70)	# 4-73
    GFX_0('rrb450Ryuhai_1_Finish', 0)
    GFX_0('rrb450Ryuhai_2_Finish', 0)
    GFX_0('rrb450Ryuhai_3_Finish', 0)
    sprite('null', 70)	# 74-143
    Unknown3001(0)

@State
def rrb450Ryuhai_1_Finish():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown1056(4000)
        Unknown23015(12)
        Unknown4061(0)
        Unknown21004(9)
        Unknown3001(192)
    sprite('null', 1)	# 1-1
    Unknown1064(5000)
    sprite('null', 2)	# 2-3
    Unknown1066(75)
    sprite('null', 10)	# 4-13

    def upon_16():
        Unknown1066(70)
    sprite('null', 13)	# 14-26

    def upon_16():
        Unknown1066(90)
    sprite('null', 2)	# 27-28
    clearUponHandler(16)
    Unknown3003(10)
    sprite('null', 2)	# 29-30
    Unknown3003(1000)
    sprite('null', 2)	# 31-32
    Unknown3003(10)
    sprite('null', 10)	# 33-42
    Unknown3003(1000)
    sprite('null', 2)	# 43-44
    Unknown3003(10)
    sprite('null', 6)	# 45-50
    Unknown3003(1000)
    sprite('null', 2)	# 51-52
    Unknown3003(10)
    sprite('null', 2)	# 53-54
    Unknown3003(1000)
    sprite('null', 2)	# 55-56
    Unknown3003(10)
    sprite('null', 2)	# 57-58
    Unknown3003(1000)

@State
def rrb450Ryuhai_2_Finish():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(12)
        Unknown1056(4000)
        Unknown4061(6)
        Unknown21004(17)
        Unknown3001(160)
    sprite('null', 1)	# 1-1
    Unknown1064(4000)
    sprite('null', 2)	# 2-3
    Unknown1066(75)
    sprite('null', 10)	# 4-13

    def upon_16():
        Unknown1066(70)
    sprite('null', 13)	# 14-26

    def upon_16():
        Unknown1066(90)
    sprite('null', 2)	# 27-28
    clearUponHandler(16)
    Unknown3003(10)
    sprite('null', 2)	# 29-30
    Unknown3003(1000)
    sprite('null', 2)	# 31-32
    Unknown3003(10)
    sprite('null', 10)	# 33-42
    Unknown3003(1000)
    sprite('null', 2)	# 43-44
    Unknown3003(10)
    sprite('null', 6)	# 45-50
    Unknown3003(1000)
    sprite('null', 2)	# 51-52
    Unknown3003(10)
    sprite('null', 2)	# 53-54
    Unknown3003(1000)
    sprite('null', 2)	# 55-56
    Unknown3003(10)
    sprite('null', 2)	# 57-58
    Unknown3003(1000)

@State
def rrb450Ryuhai_3_Finish():

    def upon_IMMEDIATE():
        Unknown4003('72726265663433315f72797568616930322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown23015(12)
        Unknown1056(4000)
        Unknown3001(128)
    sprite('null', 1)	# 1-1
    Unknown1064(2000)
    sprite('null', 2)	# 2-3
    Unknown1066(75)
    sprite('null', 10)	# 4-13

    def upon_16():
        Unknown1066(70)
    sprite('null', 13)	# 14-26

    def upon_16():
        Unknown1066(90)
    sprite('null', 2)	# 27-28
    clearUponHandler(16)
    Unknown3003(10)

@State
def rrb450FinishPetal():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown1056(1000)
        Unknown1064(0)
        Unknown4061(0)
        Unknown3038(1)
    sprite('vrrrbef430_Hit', 1)	# 1-1
    Unknown4048(-23000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f756e697175655f706574616c000000000000000000000064000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000019000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000018000000')
    sprite('vrrrbef430_Hit', 1)	# 2-2
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000017000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000016000000')
    sprite('vrrrbef430_Hit', 1)	# 3-3
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000015000000')
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000014000000')
    Unknown4048(180000)
    sprite('vrrrbef430_Hit', 1)	# 4-4
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000013000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000012000000')
    sprite('vrrrbef430_Hit', 1)	# 5-5
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000011000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000010000000')
    sprite('vrrrbef430_Hit', 1)	# 6-6
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000f000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000e000000')
    sprite('vrrrbef430_Hit', 1)	# 7-7
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000d000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000c000000')
    sprite('vrrrbef430_Hit', 1)	# 8-8
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000b000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c00000000000000000000000a000000')
    sprite('vrrrbef430_Hit', 1)	# 9-9
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000009000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000008000000')
    sprite('vrrrbef430_Hit', 1)	# 10-10
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000007000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000006000000')
    sprite('vrrrbef430_Hit', 1)	# 11-11
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000005000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000004000000')
    sprite('vrrrbef430_Hit', 1)	# 12-12
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000003000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000002000000')
    sprite('vrrrbef430_Hit', 1)	# 13-13
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000001000000')
    Unknown4048(180000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663433305f66696e6973685f706574616c000000000000000000000000000000')

@State
def rrb450_Petal():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown1096(4000)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
    sprite('null', 110)	# 1-110
    Unknown4047(9, 9, 9)
    Unknown23067('rrbef450_petal')

@State
def rrb450_Transition():

    def upon_IMMEDIATE():
        Unknown21004(9)
        Unknown2054(1)
        Unknown1000(0)
        teleportRelativeY(0)

        def upon_3():
            Unknown23057(50)
            Unknown23058(50)
        Unknown2055(70)
    sprite('null', 46)	# 1-46
    GFX_0('rrb450_TransitionL', -1)
    GFX_0('rrb450_TransitionR', -1)
    sprite('null', 100)	# 47-146
    GFX_0('rrb450_Red', -1)

@State
def rrb450_TransitionL():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1210)
        Unknown23015(4)
        Unknown4061(4)
    sprite('rrbef450_transition00_l', 3)	# 1-3
    SFX_3('rrbse_10')
    sprite('rrbef450_transition01_l', 3)	# 4-6
    sprite('rrbef450_transition02_l', 3)	# 7-9
    sprite('rrbef450_transition03_l', 3)	# 10-12
    sprite('rrbef450_transition04_l', 3)	# 13-15
    sprite('rrbef450_transition05_l', 3)	# 16-18
    sprite('rrbef450_transition06_l', 3)	# 19-21
    sprite('rrbef450_transition07_l', 3)	# 22-24
    sprite('rrbef450_transition08_l', 3)	# 25-27
    sprite('rrbef450_transition09_l', 3)	# 28-30
    sprite('rrbef450_transition10_l', 3)	# 31-33
    sprite('rrbef450_transition11_l', 3)	# 34-36
    sprite('rrbef450_transition12_l', 3)	# 37-39
    sprite('rrbef450_transition13_l', 2)	# 40-41
    sprite('rrbef450_transition14_l', 3)	# 42-44
    sprite('rrbef450_transition15_l', 2)	# 45-46
    sprite('rrbef450_transition16_l', 3)	# 47-49
    sprite('rrbef450_transition17_l', 2)	# 50-51
    sprite('rrbef450_transition18_l', 3)	# 52-54
    sprite('rrbef450_transition19_l', 2)	# 55-56
    sprite('rrbef450_transition20_l', 3)	# 57-59
    sprite('rrbef450_transition21_l', 2)	# 60-61
    sprite('rrbef450_transition22_l', 3)	# 62-64
    sprite('rrbef450_transition23_l', 2)	# 65-66
    sprite('rrbef450_transition24_l', 2)	# 67-68
    sprite('rrbef450_transition25_l', 2)	# 69-70
    sprite('rrbef450_transition26_l', 2)	# 71-72
    sprite('rrbef450_transition27_l', 2)	# 73-74
    sprite('rrbef450_transition28_l', 2)	# 75-76

@State
def rrb450_TransitionR():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1210)
        Unknown23015(4)
        Unknown4061(4)
    sprite('rrbef450_transition00_r', 3)	# 1-3
    sprite('rrbef450_transition01_r', 3)	# 4-6
    sprite('rrbef450_transition02_r', 3)	# 7-9
    sprite('rrbef450_transition03_r', 3)	# 10-12
    sprite('rrbef450_transition04_r', 3)	# 13-15
    sprite('rrbef450_transition05_r', 3)	# 16-18
    sprite('rrbef450_transition06_r', 3)	# 19-21
    sprite('rrbef450_transition07_r', 3)	# 22-24
    sprite('rrbef450_transition08_r', 3)	# 25-27
    sprite('rrbef450_transition09_r', 3)	# 28-30
    sprite('rrbef450_transition10_r', 3)	# 31-33
    sprite('rrbef450_transition11_r', 3)	# 34-36
    sprite('rrbef450_transition12_r', 3)	# 37-39
    sprite('rrbef450_transition13_r', 2)	# 40-41
    sprite('rrbef450_transition14_r', 3)	# 42-44
    sprite('rrbef450_transition15_r', 2)	# 45-46
    sprite('rrbef450_transition16_r', 3)	# 47-49
    sprite('rrbef450_transition17_r', 2)	# 50-51
    sprite('rrbef450_transition18_r', 3)	# 52-54
    sprite('rrbef450_transition19_r', 2)	# 55-56
    sprite('rrbef450_transition20_r', 3)	# 57-59
    sprite('rrbef450_transition21_r', 2)	# 60-61
    sprite('rrbef450_transition22_r', 3)	# 62-64
    sprite('rrbef450_transition23_r', 2)	# 65-66
    sprite('rrbef450_transition24_r', 2)	# 67-68
    sprite('rrbef450_transition25_r', 2)	# 69-70
    sprite('rrbef450_transition26_r', 2)	# 71-72
    sprite('rrbef450_transition27_r', 2)	# 73-74
    sprite('rrbef450_transition28_r', 2)	# 75-76

@State
def rrb450_Red():

    def upon_IMMEDIATE():
        Unknown3032()
        sendToLabelUpon(32, 0)
        Unknown23015(4)
        Unknown1096(6000)
        Unknown4061(0)
        Unknown3001(0)
        Unknown3007(225)
        Unknown3013(225)
        Unknown3019(225)
    sprite('rrbef450_transition29', 20)	# 1-20
    Unknown3004(16)
    sprite('keep', 20)	# 21-40
    Unknown26('RWBY_AHground')
    Unknown3010(1)
    Unknown3016(1)
    Unknown3022(1)
    sprite('keep', 15)	# 41-55
    Unknown23102(1)
    Unknown23108(1)
    Unknown23114(1)
    sprite('keep', 10)	# 56-65
    Unknown23102(4)
    Unknown23108(4)
    Unknown23114(4)
    sprite('keep', 30)	# 66-95
    Unknown23102(12)
    Unknown23108(12)
    Unknown23114(12)
    sprite('keep', 40)	# 96-135
    Unknown3010(0)
    Unknown3016(0)
    Unknown3022(0)
    Unknown23102(0)
    Unknown23108(0)
    Unknown23114(0)
    Unknown23099(255)
    Unknown23105(255)
    Unknown23111(255)
    Unknown3004(-8)

@State
def rrb450WinPetal():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown4007(3)
    sprite('null', 180)	# 1-180
    Unknown4047(9, 9, 9)
    Unknown23067('rrbef610_petal_prewarm')

@State
def rrb600Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-150000)
        Unknown1007(100000)
        Unknown2055(120)
        sendToLabelUpon(32, 1)
    sprite('null', 2)	# 1-2
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c00000000000000000000000000000000000000000000')
    Unknown4047(9, 9, 9)
    label(0)
    sprite('null', 2)	# 3-4
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 3)	# 5-7
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c00000000000000000000000000000000000000000000')
    gotoLabel(0)
    label(1)
    teleportRelativeX(15000)
    Unknown1007(15000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 8-9
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 10-11
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 12-13
    teleportRelativeX(30000)
    Unknown1007(25000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 14-15
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 16-17
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 18-19
    teleportRelativeX(15000)
    Unknown1007(30000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 20-21
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 2)	# 22-23
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 3)	# 24-26
    teleportRelativeX(5000)
    Unknown1007(5000)
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')
    sprite('null', 3)	# 27-29
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663630305f706574616c30310000000000000000000000000000000000000000')

@State
def rrb601Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown1096(2470)
        Unknown1000(-65000)
        teleportRelativeY(285000)
        Unknown4061(6)
        Unknown21004(1)
    sprite('null', 6)	# 1-6
    Unknown4003('72726265663630315f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 6)	# 7-12
    Unknown4003('72726265663630315f30312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 6)	# 13-18
    Unknown4003('72726265663630315f30322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 6)	# 19-24
    Unknown4003('72726265663630315f30332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 6)	# 25-30
    Unknown4003('72726265663630315f30342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 31-33
    Unknown4003('72726265663630315f30352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 34-36
    Unknown4003('72726265663630315f30362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 37-39
    Unknown4003('72726265663630315f30372e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 40-42
    Unknown4003('72726265663630315f30382e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 43-44
    Unknown4003('72726265663630315f30392e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rrb610Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeX(-20000)
        Unknown1007(200000)
        Unknown2055(600)
    sprite('null', 10)	# 1-10
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663631305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 8)	# 11-18
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663631305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 6)	# 19-24
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663631305f706574616c00000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 3)	# 25-27
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663631305f706574616c00000000000000000000000000000000000000000000')
    sprite('null', 2)	# 28-29
    Unknown4047(9, 9, 9)
    Unknown4045('72726265663631305f706574616c00000000000000000000000000000000000000000000')
    gotoLabel(0)

    @State
    def rrb612Eff():

        def upon_IMMEDIATE():
            Unknown4007(3)
            teleportRelativeX(130000)
            Unknown1007(200000)
        sprite('null', 3)	# 1-3
        sprite('null', 3)	# 4-6
        teleportRelativeX(-50000)
        Unknown4048(180000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c00000000000000000000000000000000000000000000')
        sprite('null', 3)	# 7-9
        teleportRelativeX(-70000)
        Unknown1007(3000)
        Unknown4048(270000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c00000000000000000000000000000000000000000000')
        sprite('null', 3)	# 10-12
        teleportRelativeX(-70000)
        Unknown1007(-80000)
        Unknown4048(-270000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c30320000000000000000000000000000000000000000')
        sprite('null', 1)	# 13-13
        teleportRelativeX(-30000)
        Unknown1007(-50000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c30320000000000000000000000000000000000000000')
        sprite('null', 2)	# 14-15
        teleportRelativeX(-70000)
        Unknown1007(70000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c30320000000000000000000000000000000000000000')
        sprite('null', 1)	# 16-16
        teleportRelativeX(-70000)
        Unknown1007(50000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c30320000000000000000000000000000000000000000')
        sprite('null', 2)	# 17-18
        teleportRelativeX(-70000)
        Unknown1007(40000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c30320000000000000000000000000000000000000000')
        sprite('null', 1)	# 19-19
        teleportRelativeX(-70000)
        Unknown1007(40000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c00000000000000000000000000000000000000000000')
        sprite('null', 2)	# 20-21
        teleportRelativeX(-70000)
        Unknown1007(40000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c00000000000000000000000000000000000000000000')
        sprite('null', 2)	# 22-23
        teleportRelativeX(-70000)
        Unknown1007(30000)
        Unknown4047(9, 9, 9)
        Unknown4045('72726265663631325f706574616c00000000000000000000000000000000000000000000')

    @Subroutine
    def NormalArts_Temp():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)

    @Subroutine
    def NormalArts_Temp01():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4061(6)
        Unknown21004(1)
        Unknown3032()

    @Subroutine
    def NormalArts_Temp02():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4061(6)
        Unknown21004(2)
        Unknown3032()

    @Subroutine
    def NormalArts_Temp03():
        Unknown4007(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4011(3)
        Unknown4010(3)
        Unknown3032()

    @Subroutine
    def CommonSmoke():
        Unknown3000(0)
        Unknown4061(6)
        Unknown3032()
        Unknown13044(1)

    @State
    def rrbef_kakeai_brg():

        def upon_IMMEDIATE():
            Unknown4009(2)
            Unknown4007(2)
            sendToLabelUpon(32, 0)
            Unknown2055(280)
        label(0)
        sprite('null', 10)	# 1-10
        Unknown4045('72726265665f6b616b6561695f62726730310000000000000000000000000000ffffffff')
        teleportRelativeY(320000)
        gotoLabel(0)

    @State
    def rrbef_kakeai_brg_smoke01():

        def upon_IMMEDIATE():
            Unknown4009(2)
            Unknown1102(0, -300)
            teleportRelativeY(15000)
        sprite('null', 30)	# 1-30
        Unknown4054(11)
        Unknown23067('rrbef_kakeai_brg_smoke01')

    @State
    def rrbef_kakeai_brg_smoke02():

        def upon_IMMEDIATE():
            Unknown4009(2)
            Unknown1102(0, -300)
            Unknown2005()
            teleportRelativeY(15000)
        sprite('null', 30)	# 1-30
        Unknown4054(11)
        Unknown23067('rrbef_kakeai_brg_smoke01')

    @State
    def DDLight():

        def upon_IMMEDIATE():
            Unknown4009(2)
            Unknown4003('65665f64645f6c696768742e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown1096(1300)
        sprite('null', 2)	# 1-2
        sprite('null', 10)	# 3-12
        Unknown23130(39935, 10, 1)
        sprite('null', 10)	# 13-22
        Unknown23130(33023, 10, 1)
        sprite('null', 10)	# 23-32
